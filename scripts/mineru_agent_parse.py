"""
MinerU Agent API Real Parser
=============================
Uses the free MinerU Agent API (no token needed) to parse PDF papers.
Extracts real Markdown content and updates the dataset with genuine MinerU usage records.

Agent API limits: ≤10MB, ≤20 pages, IP rate limited.
"""

import os
import sys
import json
import time
import logging
import requests

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "papers")
PARSED_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "parsed_mineru_api")
DATASET_JSONL = os.path.join(PROJECT_ROOT, "data", "processed", "molalign_dataset.jsonl")
DATASET_JSON = os.path.join(PROJECT_ROOT, "data", "processed", "molalign_dataset.json")

AGENT_BASE = "https://mineru.net/api/v1/agent"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Map papers to molecules (from existing project structure)
PAPER_MOLECULE_MAP = {
    "ibuprofen_pharmacology.pdf": ["Ibuprofen"],
    "curcumin_pharmacology.pdf": ["Curcumin"],
    "dopamine_neuroscience.pdf": ["Dopamine"],
    "acetaminophen_pharmacology.pdf": ["Acetaminophen", "Paracetamol"],
    "paclitaxel_pharmacology.pdf": ["Paclitaxel"],
    "doxorubicin_anticancer.pdf": ["Doxorubicin"],
    "morphine_opioid.pdf": ["Morphine"],
    "metformin_pharmaceutics.pdf": ["Metformin"],
    "metformin_frontiers.pdf": ["Metformin"],
    "fluoxetine_ijms.pdf": ["Fluoxetine"],
    "vitamins_pharmaceuticals.pdf": ["Ascorbic Acid", "Thiamine", "Riboflavin", "Niacin", "Biotin"],
    "caffeine_molecules.pdf": ["Caffeine"],
    "omeprazole_pharmaceutics.pdf": ["Omeprazole"],
}


def submit_file_parse(file_path, file_name):
    """Submit a file for parsing via Agent API (signed upload)."""
    url = f"{AGENT_BASE}/parse/file"
    data = {
        "file_name": file_name,
        "language": "en",
        "enable_table": True,
        "is_ocr": False,
        "enable_formula": True,
    }

    try:
        resp = requests.post(url, json=data, timeout=30)
        result = resp.json()
        if result.get("code") != 0:
            logger.error(f"Submit failed for {file_name}: {result.get('msg', 'unknown error')}")
            return None, None

        task_id = result["data"]["task_id"]
        file_url = result["data"]["file_url"]

        # Upload the file
        with open(file_path, "rb") as f:
            put_resp = requests.put(file_url, data=f, timeout=60)
            if put_resp.status_code not in (200, 201):
                logger.error(f"Upload failed for {file_name}: HTTP {put_resp.status_code}")
                return None, None

        logger.info(f"Uploaded {file_name}, task_id: {task_id}")
        return task_id, file_name

    except Exception as e:
        logger.error(f"Error submitting {file_name}: {e}")
        return None, None


def poll_result(task_id, timeout=180, interval=5):
    """Poll for parsing result."""
    url = f"{AGENT_BASE}/parse/{task_id}"
    start = time.time()

    while time.time() - start < timeout:
        try:
            resp = requests.get(url, timeout=15)
            result = resp.json()
            state = result.get("data", {}).get("state", "unknown")

            if state == "done":
                md_url = result["data"].get("markdown_url", "")
                logger.info(f"  Task {task_id[:12]}... done!")
                return md_url
            elif state == "failed":
                err = result["data"].get("err_msg", "unknown")
                logger.error(f"  Task {task_id[:12]}... failed: {err}")
                return None
            else:
                elapsed = int(time.time() - start)
                logger.info(f"  Task {task_id[:12]}... {state} ({elapsed}s)")

        except Exception as e:
            logger.warning(f"  Poll error: {e}")

        time.sleep(interval)

    logger.warning(f"  Task {task_id[:12]}... timed out after {timeout}s")
    return None


def download_markdown(md_url, output_path):
    """Download parsed Markdown content."""
    try:
        resp = requests.get(md_url, timeout=60)
        if resp.status_code == 200:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(resp.text)
            return resp.text
        else:
            logger.error(f"Download failed: HTTP {resp.status_code}")
            return None
    except Exception as e:
        logger.error(f"Download error: {e}")
        return None


def update_dataset_with_mineru(parsed_results):
    """Update the dataset with real MinerU API usage records."""
    # Load dataset
    records = []
    with open(DATASET_JSONL, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    # Index by common_name
    name_index = {}
    for rec in records:
        name = rec.get("names", {}).get("common_name", "").lower()
        if name:
            name_index[name] = rec
        # Also index synonyms
        for syn in rec.get("names", {}).get("synonyms", []):
            name_index[syn.lower()] = rec

    updated_count = 0

    for pdf_name, molecules in PAPER_MOLECULE_MAP.items():
        if pdf_name not in parsed_results:
            continue

        md_content = parsed_results[pdf_name]["markdown"]
        task_id = parsed_results[pdf_name]["task_id"]
        if not md_content:
            continue

        seen_records_for_paper = set()
        for mol_name in molecules:
            rec = name_index.get(mol_name.lower())
            if not rec:
                logger.warning(f"  Molecule '{mol_name}' not found in dataset")
                continue
            if rec.get("record_id") in seen_records_for_paper:
                continue
            seen_records_for_paper.add(rec.get("record_id"))

            # Extract relevant text sections from markdown
            text_snippet = extract_relevant_text(md_content, mol_name)

            # Add paper-sourced text description
            if text_snippet:
                descs = rec.get("text_descriptions", [])
                # Check if we already have a paper description from this source
                already_exists = any(
                    d.get("source", {}).get("reference", "").endswith(pdf_name)
                    for d in descs
                )
                if not already_exists:
                    descs.append({
                        "type": "general_description",
                        "content": text_snippet[:1500],
                        "source": {
                            "type": "paper",
                            "reference": pdf_name,
                            "section": None,
                            "mineru_parsed": True
                        },
                        "language": "en"
                    })
                    rec["text_descriptions"] = descs

            # Add real MinerU API usage record
            usage = rec.get("alignment_metadata", {}).get("mineru_usage", [])
            # Check if already has real API record for this paper
            already_has = any(
                u.get("tool") == "MinerU Agent API" and pdf_name in u.get("input", "")
                for u in usage
            )
            if not already_has:
                usage.append({
                    "tool": "MinerU Agent API",
                    "task": f"使用 MinerU Agent API 解析{mol_name}相关论文 ({pdf_name})，提取结构化文本和图表",
                    "input": f"data/raw/papers/{pdf_name}",
                    "output": f"data/raw/parsed_mineru_api/{pdf_name.replace('.pdf', '.md')}",
                    "task_id": task_id,
                    "markdown_url": parsed_results[pdf_name].get("markdown_url"),
                    "content_length": len(md_content),
                    "detail": f"task_id={task_id}, 真实 MinerU Agent API 调用"
                })
                rec.setdefault("alignment_metadata", {})["mineru_usage"] = usage

            updated_count += 1

    # Save updated dataset
    with open(DATASET_JSONL, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    with open(DATASET_JSON, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    logger.info(f"Updated {updated_count} molecule records with real MinerU API data")
    return updated_count


def extract_relevant_text(md_content, molecule_name):
    """Extract text relevant to the molecule from parsed markdown."""
    lines = md_content.split("\n")
    relevant_lines = []
    capturing = False
    capture_count = 0

    # Search for sections mentioning the molecule
    mol_lower = molecule_name.lower()
    mol_variants = [mol_lower]

    # Common variants
    if mol_lower == "paracetamol":
        mol_variants.append("acetaminophen")
    elif mol_lower == "acetaminophen":
        mol_variants.append("paracetamol")
    elif mol_lower == "ascorbic acid":
        mol_variants.append("vitamin c")

    for line in lines:
        line_lower = line.lower()
        if any(v in line_lower for v in mol_variants):
            capturing = True
            capture_count = 0

        if capturing:
            relevant_lines.append(line)
            capture_count += 1
            if capture_count > 50:  # Capture ~50 lines around mention
                capturing = False

    if relevant_lines:
        text = "\n".join(relevant_lines)
        # Clean up
        text = text.strip()
        if len(text) > 2000:
            text = text[:2000]
        return text

    # Fallback: take first meaningful paragraph
    for line in lines:
        if len(line.strip()) > 100 and not line.startswith("#") and not line.startswith("!"):
            return line.strip()[:1500]

    return ""


def main():
    os.makedirs(PARSED_DIR, exist_ok=True)

    # Filter PDFs by size (Agent API limit: 10MB)
    pdf_files = []
    for f in sorted(os.listdir(PAPERS_DIR)):
        if f.endswith(".pdf"):
            path = os.path.join(PAPERS_DIR, f)
            size_mb = os.path.getsize(path) / (1024 * 1024)
            if size_mb <= 10.0:
                pdf_files.append((f, path, size_mb))
            else:
                logger.warning(f"Skipping {f} ({size_mb:.2f}MB > 10MB limit)")

    logger.info(f"Found {len(pdf_files)} PDFs to parse via MinerU Agent API")

    # Phase 1: Submit all files
    tasks = []
    for pdf_name, pdf_path, size_mb in pdf_files:
        logger.info(f"Submitting {pdf_name} ({size_mb:.2f}MB)...")
        task_id, _ = submit_file_parse(pdf_path, pdf_name)
        if task_id:
            tasks.append((task_id, pdf_name, pdf_path))
        time.sleep(1)  # Rate limit between submissions

    logger.info(f"Submitted {len(tasks)} tasks successfully")

    # Phase 2: Wait for all results
    parsed_results = {}
    for task_id, pdf_name, pdf_path in tasks:
        logger.info(f"Waiting for {pdf_name}...")
        md_url = poll_result(task_id, timeout=300, interval=5)

        if md_url:
            output_path = os.path.join(PARSED_DIR, pdf_name.replace(".pdf", ".md"))
            md_content = download_markdown(md_url, output_path)
            parsed_results[pdf_name] = {
                "task_id": task_id,
                "markdown_url": md_url,
                "markdown": md_content or "",
                "output_path": output_path
            }
            if md_content:
                logger.info(f"  Saved {len(md_content)} chars to {output_path}")
        else:
            parsed_results[pdf_name] = {
                "task_id": task_id,
                "markdown_url": None,
                "markdown": "",
                "output_path": None
            }

        time.sleep(2)  # Rate limit between polls

    # Phase 3: Update dataset
    logger.info("Updating dataset with real MinerU API records...")
    updated = update_dataset_with_mineru(parsed_results)

    # Summary
    print(f"\n{'=' * 50}")
    print(f"MINERU AGENT API PARSING RESULTS")
    print(f"{'=' * 50}")
    print(f"Papers submitted: {len(tasks)}")
    print(f"Successfully parsed: {sum(1 for r in parsed_results.values() if r['markdown'])}")
    print(f"Dataset records updated: {updated}")
    print(f"Output directory: {PARSED_DIR}")
    print(f"{'=' * 50}")

    # Save parsing log
    log_path = os.path.join(PARSED_DIR, "parsing_log.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "papers_submitted": len(tasks),
            "results": {k: {"task_id": v["task_id"], "markdown_url": v["markdown_url"],
                           "content_length": len(v["markdown"])} for k, v in parsed_results.items()}
        }, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved parsing log to {log_path}")


if __name__ == "__main__":
    main()
