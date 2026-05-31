#!/usr/bin/env python3
"""
Post-enrichment fixes
=====================
Run AFTER enrich_expanded_dataset.py completes.
1. Fix SMILES canonicalization (RDKit)
2. Link paper images to dataset records
3. Sync JSONL from JSON
"""

import json
import os
from pathlib import Path

from rdkit import Chem

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = BASE_DIR / "data" / "processed" / "molalign_dataset.json"
JSONL_PATH = BASE_DIR / "data" / "processed" / "molalign_dataset.jsonl"
PAPER_DIR = BASE_DIR / "data" / "processed" / "images" / "paper"


def canonicalize(smi: str) -> str | None:
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return None
    return Chem.MolToSmiles(mol)


def fix_smiles(records: list) -> int:
    """Canonicalize SMILES using RDKit."""
    fixed = 0
    for rec in records:
        smiles = rec.get("smiles", {})
        for field in ("canonical", "isomeric"):
            old = smiles.get(field, "")
            if old:
                new = canonicalize(old)
                if new and new != old:
                    smiles[field] = new
                    fixed += 1
    return fixed


def link_paper_images(records: list) -> int:
    """Link paper images from disk to dataset records."""
    if not PAPER_DIR.exists():
        print(f"  Paper dir not found: {PAPER_DIR}")
        return 0

    # Build mapping: mol_id -> list of image paths
    paper_map = {}
    for f in os.listdir(PAPER_DIR):
        mol_id = f.split("_paper_")[0]
        paper_map.setdefault(mol_id, []).append(f"images/paper/{f}")

    # Already-linked count
    already_linked = sum(
        1 for r in records
        if r.get("modalities", {}).get("structure_paper")
    )

    fixed = 0
    for rec in records:
        rid = rec.get("record_id", "")
        if rid in paper_map:
            rec.setdefault("modalities", {})["structure_paper"] = {
                "images": paper_map[rid],
                "source": "MinerU Agent API parsed papers",
                "paper_count": len(paper_map[rid]),
            }
            fixed += 1

    print(f"  Already linked: {already_linked}")
    return fixed


def sync_jsonl(records: list) -> None:
    """Write JSONL from records."""
    with open(JSONL_PATH, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"  Synced JSONL: {len(records)} records")


def main():
    print("=" * 50)
    print("POST-ENRICHMENT FIXES")
    print("=" * 50)

    # Load
    records = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    print(f"Loaded {len(records)} records from {JSON_PATH.name}")

    # 1. Fix SMILES
    print("\n[1/3] Fixing SMILES canonicalization...")
    smi_fixed = fix_smiles(records)
    print(f"  Fixed {smi_fixed} SMILES fields")

    # 2. Link paper images
    print("\n[2/3] Linking paper images...")
    img_fixed = link_paper_images(records)
    print(f"  Fixed {img_fixed} records with paper images")

    # 3. Save JSON
    print("\n[3/3] Saving...")
    JSON_PATH.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"  Saved JSON: {JSON_PATH}")

    # 4. Sync JSONL
    sync_jsonl(records)

    print("\n" + "=" * 50)
    print("DONE. Ready for validation.")
    print("=" * 50)


if __name__ == "__main__":
    main()
