from __future__ import annotations

"""
Expand MinerU paper coverage via free MinerU Agent API
========================================================
Pipeline:
  1. Pick candidate molecules (Tier C in thin-evidence categories)
  2. Search PMC for open-access review papers
  3. Download PDF (must be <=10MB and <=20 pages for free tier)
  4. Submit to MinerU Agent API
  5. Poll for Markdown
  6. Update dataset with new mineru_usage evidence
  7. Save parsing_log.json

Usage:
    python scripts/expand_mineru_coverage.py --max-papers 30 --categories Anticancer,Antibiotic,NaturalProduct
"""
import os
import sys
import json
import time
import logging
import argparse
import requests
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = PROJECT_ROOT / "data" / "raw" / "papers"
PARSED_DIR = PROJECT_ROOT / "data" / "raw" / "parsed_mineru_api"
DATASET_JSONL = PROJECT_ROOT / "data" / "processed" / "molalign_dataset.jsonl"
DATASET_JSON = PROJECT_ROOT / "data" / "processed" / "molalign_dataset.json"

AGENT_BASE = "https://mineru.net/api/v1/agent"
EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def search_pmc_open_access(drug_name: str, max_results: int = 5) -> list:
    """Search Europe PMC for open-access papers on the drug.

    Returns list of {'pmcid', 'title', 'pdf_url', 'page_range_ok'}.
    Uses Europe PMC's REST API which has stable PDF rendering via ?pdf=render.
    Broadens to any open-access article (not just reviews) for better hit rate.
    """
    query = f'({drug_name}) AND (OPEN_ACCESS:Y)'
    params = {
        "query": query,
        "format": "json",
        "pageSize": max_results,
        "resultType": "core",
    }
    try:
        r = requests.get(EPMC_SEARCH, params=params, timeout=20)
        if r.status_code != 200:
            return []
        data = r.json()
    except Exception as e:
        logger.warning(f"Europe PMC search failed for {drug_name}: {e}")
        return []

    results = []
    for rec in data.get("resultList", {}).get("result", []):
        pmcid = rec.get("pmcid", "")
        if not pmcid or not pmcid.startswith("PMC"):
            continue
        # Strip "PMC" prefix
        pmc_num_str = pmcid[3:].lstrip("0")
        if not pmc_num_str.isdigit():
            continue
        pmc_num = int(pmc_num_str)
        # Europe PMC PDF rendering endpoint (stable, returns application/pdf)
        pdf_url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
        # Track page count for prioritizing short papers (MinerU free limit: 20 pages)
        page_count = rec.get("pageInfo", "") or rec.get("pageCount", "")
        results.append({
            "pmcid": pmcid,
            "pmc_num": pmc_num,
            "title": rec.get("title", "")[:200],
            "pdf_url": pdf_url,
            "doi": rec.get("doi", ""),
            "page_count": page_count,
        })
    # Sort: prefer reviews and shorter papers first
    def sort_key(r):
        is_review = 0 if (r.get("title", "").lower().__contains__("review")
                          or r.get("title", "").lower().__contains__("overview")
                          or r.get("title", "").lower().__contains__("advances")) else 1
        return (is_review, r.get("pmcid", ""))
    results.sort(key=sort_key)
    return results


def download_pdf(url: str, out_path: Path, max_mb: float = 9.5, max_retries: int = 3) -> bool:
    """Download a PDF; reject if >max_mb (MinerU free tier limit is 10MB)
    or if the response is not a real PDF (e.g. HTML error page).
    Retries with exponential backoff on connection errors."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(max_retries):
        try:
            r = requests.get(url, timeout=60, stream=True, allow_redirects=True)
            if r.status_code != 200:
                logger.warning(f"Download HTTP {r.status_code} for {url}")
                if r.status_code in (429, 500, 502, 503, 504) and attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return False
            # Verify content-type
            ct = r.headers.get("Content-Type", "").lower()
            if "pdf" not in ct:
                logger.warning(f"Not a PDF (Content-Type: {ct}): {url}")
                return False
            # Check content-length
            cl = r.headers.get("Content-Length")
            if cl and int(cl) > max_mb * 1024 * 1024:
                logger.warning(f"PDF too large ({int(cl)/1e6:.1f}MB): {url}")
                return False
            total = 0
            first_bytes = b""
            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        if not first_bytes:
                            first_bytes = chunk[:4]
                        f.write(chunk)
                        total += len(chunk)
                        if total > max_mb * 1024 * 1024:
                            logger.warning(f"PDF exceeded {max_mb}MB during download, aborting")
                            out_path.unlink()
                            return False
            # Verify PDF magic bytes
            if not first_bytes.startswith(b"%PDF"):
                logger.warning(f"Downloaded file is not a PDF (first bytes: {first_bytes!r})")
                out_path.unlink()
                return False
            return out_path.exists() and out_path.stat().st_size > 1000
        except (requests.exceptions.ConnectionError,
                requests.exceptions.ProxyError,
                requests.exceptions.Timeout,
                ConnectionResetError) as e:
            if attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                logger.warning(f"  download error (attempt {attempt+1}/{max_retries}), retry in {wait}s: {e}")
                time.sleep(wait)
                continue
            logger.warning(f"Download failed after {max_retries} attempts for {url}: {e}")
            return False
        except Exception as e:
            logger.warning(f"Download failed for {url}: {e}")
            return False
    return False


def submit_to_mineru(pdf_path: Path, file_name: str) -> str | None:
    """Submit a PDF to MinerU Agent API; return task_id or None."""
    url = f"{AGENT_BASE}/parse/file"
    data = {
        "file_name": file_name,
        "language": "en",
        "enable_table": True,
        "is_ocr": False,
        "enable_formula": True,
    }
    try:
        r = requests.post(url, json=data, timeout=30)
        result = r.json()
        if result.get("code") != 0:
            logger.warning(f"MinerU submit failed for {file_name}: {result.get('msg')}")
            return None
        task_id = result["data"]["task_id"]
        file_url = result["data"]["file_url"]
        # Upload
        with open(pdf_path, "rb") as f:
            put = requests.put(file_url, data=f, timeout=120)
        if put.status_code not in (200, 201):
            logger.warning(f"Upload failed HTTP {put.status_code}")
            return None
        return task_id
    except Exception as e:
        logger.warning(f"MinerU submit error: {e}")
        return None


def poll_mineru(task_id: str, timeout: int = 300, interval: int = 5) -> str | None:
    """Poll MinerU task; return markdown_url on success."""
    url = f"{AGENT_BASE}/parse/{task_id}"
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=15)
            data = r.json()
            state = data.get("data", {}).get("state", "unknown")
            if state == "done":
                return data["data"].get("markdown_url")
            elif state == "failed":
                err = data["data"].get("err_msg", "unknown")
                logger.warning(f"  task {task_id[:12]}... failed: {err}")
                return None
        except Exception as e:
            logger.warning(f"  poll error: {e}")
        time.sleep(interval)
    return None


def download_markdown(md_url: str, out_path: Path) -> str | None:
    """Download parsed Markdown; return content string."""
    try:
        r = requests.get(md_url, timeout=60)
        if r.status_code == 200:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(r.text, encoding="utf-8")
            return r.text
        return None
    except Exception as e:
        logger.warning(f"  markdown download error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-papers", type=int, default=30)
    parser.add_argument("--categories", type=str,
                        default="Anticancer Drug,Antibiotic,Natural Product,Antihypertensive,Antidiabetic Drug,Antiviral Drug")
    parser.add_argument("--pilot", type=int, default=3, help="Run first N as pilot batch")
    args = parser.parse_args()

    target_cats = set(args.categories.split(","))
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    PARSED_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing parsing_log to avoid re-submitting
    log_path = PARSED_DIR / "parsing_log.json"
    if log_path.exists():
        with open(log_path, "r", encoding="utf-8") as f:
            existing_log = json.load(f)
        already_submitted = set(existing_log.get("results", {}).keys())
    else:
        existing_log = {"results": {}}
        already_submitted = set()

    # Load dataset, find candidates
    records = []
    with open(DATASET_JSONL, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    record_map = {r["record_id"]: r for r in records}

    candidates = []
    for r in records:
        if r.get("category") not in target_cats:
            continue
        if r.get("alignment_metadata", {}).get("mineru_usage"):
            continue
        if r.get("modalities", {}).get("structure_paper"):
            continue
        candidates.append(r)

    # Sort by category priority, then record_id
    cat_priority = {c: i for i, c in enumerate([
        "Anticancer Drug", "Antibiotic", "Natural Product", "Antihypertensive",
        "Antidiabetic Drug", "Antiviral Drug"
    ])}
    candidates.sort(key=lambda r: (cat_priority.get(r.get("category"), 99), r["record_id"]))
    candidates = candidates[:args.max_papers]

    logger.info(f"Will process {len(candidates)} candidate molecules in categories: {target_cats}")
    logger.info(f"  First {args.pilot} are pilot; remaining after pilot success.")

    new_results = {}
    processed = 0
    for rec in candidates:
        rid = rec["record_id"]
        name = rec.get("names", {}).get("common_name", "Unknown")
        cid = rec.get("molecule_id", {}).get("pubchem_cid", "")
        cat = rec.get("category", "")

        if processed >= args.pilot and processed == args.pilot:
            logger.info(f"Pilot of {args.pilot} complete. Continuing with full batch...")

        # Skip if PDF already exists
        safe_name = name.lower().replace(" ", "_").replace("/", "_")
        pdf_name = f"{safe_name}_{cat.lower().replace(' ', '_')}.pdf"
        pdf_path = PAPERS_DIR / pdf_name
        if pdf_name in already_submitted:
            logger.info(f"SKIP {pdf_name} (already in parsing_log)")
            continue

        # 1. Search PMC
        logger.info(f"[{processed+1}/{len(candidates)}] {rid} {name} ({cat}) — searching PMC")
        pmc_results = search_pmc_open_access(name, max_results=3)
        if not pmc_results:
            logger.warning(f"  no PMC results for {name}")
            processed += 1
            time.sleep(1)
            continue

        # Pick first one (could be smarter — prefer reviews with PMC ID order)
        target = pmc_results[0]
        logger.info(f"  found PMC{target['pmc_num']}: {target['title'][:80]}")

        # 2. Download PDF (validate existing file is real PDF; re-download if broken)
        existing_valid = False
        if pdf_path.exists() and pdf_path.stat().st_size > 10000:
            with open(pdf_path, "rb") as _f:
                if _f.read(4) == b"%PDF":
                    existing_valid = True
        if not existing_valid:
            if pdf_path.exists():
                pdf_path.unlink()  # remove broken/HTML file
            if not download_pdf(target["pdf_url"], pdf_path):
                logger.warning(f"  download failed for {pdf_name}")
                processed += 1
                time.sleep(2)
                continue
        logger.info(f"  PDF: {pdf_path.stat().st_size/1024:.1f}KB")

        # 3. Submit to MinerU
        task_id = submit_to_mineru(pdf_path, pdf_name)
        if not task_id:
            logger.warning(f"  submit failed")
            processed += 1
            time.sleep(5)
            continue
        logger.info(f"  task_id: {task_id[:16]}...")

        # 4. Poll for markdown URL
        md_url = poll_mineru(task_id, timeout=300, interval=5)
        if not md_url:
            logger.warning(f"  poll failed / timed out")
            new_results[pdf_name] = {
                "task_id": task_id, "markdown_url": None, "content_length": 0,
                "pmc_id": target["pmcid"], "pmc_num": target["pmc_num"],
                "title": target["title"], "record_id": rid, "molecule": name,
            }
            processed += 1
            time.sleep(5)
            continue

        # 5. Download Markdown
        md_path = PARSED_DIR / pdf_name.replace(".pdf", ".md")
        md_content = download_markdown(md_url, md_path)
        if not md_content:
            logger.warning(f"  markdown download failed")
            processed += 1
            time.sleep(3)
            continue
        logger.info(f"  saved {len(md_content)} chars to {md_path.name}")

        new_results[pdf_name] = {
            "task_id": task_id,
            "markdown_url": md_url,
            "content_length": len(md_content),
            "pmc_id": target["pmcid"],
            "pmc_num": target["pmc_num"],
            "title": target["title"],
            "record_id": rid,
            "molecule": name,
        }

        # 6. Update dataset record with real MinerU evidence
        if rid in record_map:
            r = record_map[rid]
            usage = r.get("alignment_metadata", {}).get("mineru_usage", [])
            already = any(u.get("input", "").endswith(pdf_name) for u in usage)
            if not already:
                usage.append({
                    "tool": "MinerU Agent API",
                    "task": f"Parsed {pdf_name} via MinerU Agent API and aligned Markdown to {name} ({cat}).",
                    "input": f"data/raw/papers/{pdf_name}",
                    "output": f"data/raw/parsed_mineru_api/{pdf_name.replace('.pdf', '.md')}",
                    "task_id": task_id,
                    "markdown_url": md_url,
                    "content_length": len(md_content),
                    "pmc_id": target["pmcid"],
                    "detail": f"task_id={task_id}; markdown_url={md_url}; content_length={len(md_content)}"
                })
                r.setdefault("alignment_metadata", {})["mineru_usage"] = usage
                logger.info(f"  updated {rid} with MinerU evidence")

        processed += 1
        time.sleep(3)  # Rate limit between papers

    # Save updated dataset (atomic write via temp file + rename)
    import tempfile
    for target_path, write_fn in [
        (DATASET_JSONL, lambda f: [f.write(json.dumps(r, ensure_ascii=False) + "\n") for r in records]),
        (DATASET_JSON, lambda f: json.dump(records, f, ensure_ascii=False, indent=2)),
    ]:
        tmp_fd, tmp_path = tempfile.mkstemp(suffix=".tmp", dir=str(target_path.parent))
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                write_fn(f)
            os.replace(tmp_path, str(target_path))
        except BaseException:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise

    # Update parsing_log
    existing_log["results"].update(new_results)
    existing_log["last_expansion"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(existing_log, f, ensure_ascii=False, indent=2)

    success = sum(1 for v in new_results.values() if v.get("markdown_url"))
    total_chars = sum(v.get("content_length", 0) for v in new_results.values())
    print(f"\n{'='*60}")
    print(f"EXPANSION COMPLETE")
    print(f"{'='*60}")
    print(f"Papers attempted: {processed}")
    print(f"Successful parses: {success}")
    print(f"New total chars: {total_chars}")
    print(f"Updated parsing_log: {log_path}")
    print(f"Updated dataset: {DATASET_JSONL}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
