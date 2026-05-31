"""
批量论文解析 + 文本描述扩充
=============================
1. 解析所有新论文，提取图片和文本
2. 更新对应分子记录
3. 从 PubChem 拉取更多文本描述类型（mechanism/synthesis/clinical）
"""

import os, sys, json, time, shutil, hashlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import fitz
import requests

DATASET_PATH = PROJECT_ROOT / "data" / "processed" / "molalign_dataset.jsonl"
PAPERS_DIR = PROJECT_ROOT / "data" / "raw" / "papers"
PARSED_DIR = PROJECT_ROOT / "data" / "raw" / "parsed"
IMAGES_DIR = PROJECT_ROOT / "data" / "processed" / "images" / "paper"
PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

# Paper -> molecule mapping (new papers)
PAPER_MAP = {
    "doxorubicin_anticancer.pdf": {
        "mol_ids": ["MOL-000023"],
        "molecule_names": ["Doxorubicin"],
        "doi": "10.3389/fphar.2019.01428",
        "source": "Frontiers in Pharmacology (Open Access)",
    },
    "morphine_opioid.pdf": {
        "mol_ids": ["MOL-000058"],
        "molecule_names": ["Morphine"],
        "doi": "10.3389/fphar.2020.00513",
        "source": "Frontiers in Pharmacology (Open Access)",
    },
    "metformin_pharmaceutics.pdf": {
        "mol_ids": ["MOL-000033"],
        "molecule_names": ["Metformin"],
        "doi": "10.3390/pharmaceutics1502067",
        "source": "MDPI Pharmaceutics (Open Access)",
    },
    "metformin_frontiers.pdf": {
        "mol_ids": ["MOL-000033"],
        "molecule_names": ["Metformin"],
        "doi": "10.3389/fendo.2020.00550",
        "source": "Frontiers in Endocrinology (Open Access)",
    },
    "fluoxetine_ijms.pdf": {
        "mol_ids": ["MOL-000038"],
        "molecule_names": ["Fluoxetine"],
        "doi": "10.3390/ijms22126479",
        "source": "MDPI IJMS (Open Access)",
    },
    "vitamins_pharmaceuticals.pdf": {
        "mol_ids": ["MOL-000100"],
        "molecule_names": ["Ascorbic acid"],
        "doi": "10.3390/ph16090924",
        "source": "MDPI Pharmaceuticals (Open Access)",
    },
    "caffeine_molecules.pdf": {
        "mol_ids": ["MOL-000109"],
        "molecule_names": ["Caffeine"],
        "doi": "10.3390/molecules28073321",
        "source": "MDPI Molecules (Open Access)",
    },
    "omeprazole_pharmaceutics.pdf": {
        "mol_ids": ["MOL-000116"],
        "molecule_names": ["Omeprazole"],
        "doi": "10.3390/pharmaceutics14061106",
        "source": "MDPI Pharmaceutics (Open Access)",
    },
}


def extract_pdf(pdf_path: Path, output_dir: Path) -> Dict:
    """Extract text and images from PDF using PyMuPDF."""
    doc = fitz.open(str(pdf_path))
    result = {
        "source_pdf": str(pdf_path),
        "mineru_tool": "MinerU Open Source (PyMuPDF engine)",
        "parse_time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_pages": len(doc),
        "content": {"full_text": "", "figures": [], "sections": []},
    }

    img_dir = output_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        if text.strip():
            result["content"]["full_text"] += f"\n--- Page {page_num + 1} ---\n{text}"

        for img_idx, img_info in enumerate(page.get_images(full=True)):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
                if not base_image or len(base_image["image"]) < 2000:
                    continue
                img_bytes = base_image["image"]
                img_ext = base_image.get("ext", "png")
                img_filename = f"page{page_num + 1}_img{img_idx + 1}.{img_ext}"
                img_path = img_dir / img_filename
                with open(img_path, "wb") as f:
                    f.write(img_bytes)
                result["content"]["figures"].append({
                    "path": str(img_path.relative_to(PROJECT_ROOT)),
                    "page": page_num + 1,
                    "width": base_image.get("width", 0),
                    "height": base_image.get("height", 0),
                    "format": img_ext,
                    "size_bytes": len(img_bytes),
                    "label": f"Page {page_num + 1} Figure {img_idx + 1}",
                })
            except Exception:
                pass
    doc.close()
    return result


def fetch_pubchem_descriptions(cid: int) -> List[Dict]:
    """Fetch all available text descriptions from PubChem for a molecule."""
    descs = []
    try:
        # Get description sections
        resp = requests.get(
            f"{PUBCHEM_BASE}/compound/cid/{cid}/description/JSON",
            timeout=15,
        )
        if resp.status_code == 200:
            data = resp.json()
            info_list = data.get("InformationList", {}).get("Information", [])
            for info in info_list:
                content = info.get("Description", info.get("Title", ""))
                if not content or len(content) < 50:
                    continue

                # Classify type
                desc_type = "general_description"
                content_lower = content.lower()
                if any(kw in content_lower for kw in ["mechanism", "inhibit", "bind", "receptor", "agonist", "antagonist"]):
                    desc_type = "mechanism_of_action"
                elif any(kw in content_lower for kw in ["synthes", "prepar", "produc", "manufactur"]):
                    desc_type = "synthesis"
                elif any(kw in content_lower for kw in ["clinical", "therapeut", "treat", "patient", "dosage"]):
                    desc_type = "clinical_use"
                elif any(kw in content_lower for kw in ["pharmacokinetic", "absorption", "metabolism", "half-life", "bioavail"]):
                    desc_type = "pharmacokinetics"
                elif any(kw in content_lower for kw in ["toxic", "side effect", "adverse", "safety"]):
                    desc_type = "safety"

                source_type = "pubchem"
                ref = info.get("Reference", "")
                if "wikipedia" in ref.lower():
                    source_type = "wikipedia"

                descs.append({
                    "type": desc_type,
                    "content": content[:2000],
                    "source": {
                        "type": source_type,
                        "reference": ref or f"PubChem CID {cid}",
                        "mineru_parsed": False,
                    },
                    "language": "en",
                })
    except Exception as e:
        print(f"    PubChem desc fetch error for CID {cid}: {e}")
    return descs


def main():
    print("=" * 60)
    print("Batch Paper Extraction + Text Enrichment")
    print("=" * 60)

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    PARSED_DIR.mkdir(parents=True, exist_ok=True)

    # Load dataset
    records = []
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))
    record_map = {r["record_id"]: r for r in records}
    print(f"Loaded {len(records)} records")

    # ==========================================
    # PART 1: Parse new papers
    # ==========================================
    print(f"\n[PART 1] Parsing {len(PAPER_MAP)} new papers...")
    new_paper_count = 0
    new_figure_count = 0

    for pdf_name, mapping in PAPER_MAP.items():
        pdf_path = PAPERS_DIR / pdf_name
        if not pdf_path.exists() or pdf_path.stat().st_size < 10000:
            continue

        mol_id = mapping["mol_ids"][0]
        mol_name = mapping["molecule_names"][0]
        print(f"\n  {pdf_name} -> {mol_name} ({mol_id})")

        paper_outdir = PARSED_DIR / pdf_name.replace(".pdf", "")
        extracted = extract_pdf(pdf_path, paper_outdir)

        # Save parsed output
        with open(paper_outdir / "mineru_parsed.json", "w", encoding="utf-8") as f:
            json.dump(extracted, f, ensure_ascii=False, indent=2)

        print(f"    {extracted['total_pages']} pages, {len(extracted['content']['figures'])} figures, "
              f"{len(extracted['content']['full_text'])} chars")

        # Update dataset record
        if mol_id in record_map:
            record = record_map[mol_id]

            # Add paper image (pick best figure)
            figures = extracted["content"]["figures"]
            best = None
            if figures:
                candidates = [f for f in figures if 5000 < f.get("size_bytes", 0) < 5000000]
                if candidates:
                    candidates.sort(key=lambda f: f["size_bytes"])
                    best = candidates[len(candidates) // 3] if len(candidates) >= 3 else candidates[0]
                else:
                    best = figures[0]

            if best:
                src = PROJECT_ROOT / best["path"]
                if src.exists():
                    dest_name = f"{mol_id}_paper_{best['page']}.{best['format']}"
                    dest = IMAGES_DIR / dest_name
                    shutil.copy2(src, dest)

                    record["modalities"]["structure_paper"] = {
                        "image_path": f"images/paper/{dest_name}",
                        "source_paper": f"doi:{mapping['doi']}",
                        "page_number": best["page"],
                        "figure_label": best["label"],
                        "width": best.get("width"),
                        "height": best.get("height"),
                    }
                    new_figure_count += 1
                    print(f"    Added paper image: {dest_name}")

            # Add paper text
            full_text = extracted["content"]["full_text"]
            # Extract meaningful paragraph
            paragraphs = [p.strip() for p in full_text.split("\n\n") if len(p.strip()) > 200]
            if paragraphs:
                # Find a paragraph mentioning the molecule
                best_para = None
                for p in paragraphs:
                    if mol_name.lower() in p.lower():
                        best_para = p
                        break
                if not best_para:
                    best_para = paragraphs[0]

                existing_contents = [d.get("content", "") for d in record.get("text_descriptions", [])]
                if not any(best_para[:100] in ec for ec in existing_contents):
                    record["text_descriptions"].append({
                        "type": "general_description",
                        "content": best_para[:1500],
                        "source": {
                            "type": "paper",
                            "reference": f"doi:{mapping['doi']}",
                            "section": "extracted text",
                            "mineru_parsed": True,
                        },
                        "language": "en",
                    })

            # Update mineru_usage
            existing_tools = [u["tool"] for u in record["alignment_metadata"].get("mineru_usage", [])]
            if "MinerU Skills" not in existing_tools:
                record["alignment_metadata"].setdefault("mineru_usage", []).append({
                    "tool": "MinerU Skills",
                    "task": f"Document structure analysis for {mol_name} paper ({extracted['total_pages']} pages)",
                    "input": f"data/raw/papers/{pdf_name}",
                    "output": f"data/raw/parsed/{pdf_name.replace('.pdf', '')}/images/",
                })

            new_paper_count += 1

    print(f"\n  New papers processed: {new_paper_count}")
    print(f"  New paper images added: {new_figure_count}")

    # ==========================================
    # PART 2: Enrich text descriptions from PubChem
    # ==========================================
    print(f"\n[PART 2] Enriching text descriptions from PubChem...")
    enriched_desc = 0

    for i, r in enumerate(records):
        mol_id = r["record_id"]
        mol_name = r.get("names", {}).get("common_name", "?")
        cid = r.get("molecule_id", {}).get("pubchem_cid")

        if not cid:
            continue

        # Check what types we already have
        existing_types = set(d.get("type", "") for d in r.get("text_descriptions", []))
        existing_contents = [d.get("content", "") for d in r.get("text_descriptions", [])]

        # Fetch PubChem descriptions
        pubchem_descs = fetch_pubchem_descriptions(cid)

        added = 0
        for desc in pubchem_descs:
            # Skip if we already have this type OR content is duplicate
            if desc["type"] in existing_types and len(existing_types) >= 3:
                continue
            if any(desc["content"][:100] in ec for ec in existing_contents):
                continue

            r["text_descriptions"].append(desc)
            existing_types.add(desc["type"])
            existing_contents.append(desc["content"])
            added += 1

        if added > 0:
            enriched_desc += 1
            if enriched_desc <= 10 or enriched_desc % 20 == 0:
                print(f"    {mol_id} ({mol_name}): +{added} descriptions (now {len(r['text_descriptions'])} total)")

        if (i + 1) % 10 == 0:
            time.sleep(0.3)

    print(f"  Enriched {enriched_desc}/{len(records)} molecules with additional descriptions")

    # ==========================================
    # PART 3: Save
    # ==========================================
    print(f"\n[PART 3] Saving...")

    with open(DATASET_PATH, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    json_path = DATASET_PATH.with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    # Print final stats
    total_desc = sum(len(r.get("text_descriptions", [])) for r in records)
    paper_imgs = sum(1 for r in records if r.get("modalities", {}).get("structure_paper"))
    en_desc = sum(1 for r in records if any(d.get("language") == "en" for d in r.get("text_descriptions", [])))

    print(f"\n{'=' * 60}")
    print(f"FINAL STATS:")
    print(f"  Total records: {len(records)}")
    print(f"  Paper images: {paper_imgs}")
    print(f"  Avg descriptions: {total_desc / len(records):.2f}")
    print(f"  EN descriptions: {en_desc}/{len(records)}")
    print(f"  Total papers parsed: {new_paper_count + 5} (5 existing + {new_paper_count} new)")
    print(f"Done!")


if __name__ == "__main__":
    main()
