from __future__ import annotations
#!/usr/bin/env python3
"""Canonicalize all SMILES in processed MolAlign outputs using RDKit."""

import json
import sys
from pathlib import Path

from rdkit import Chem

DATASET_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"
DATASET_JSON = DATASET_DIR / "molalign_dataset.json"
DATASET_JSONL = DATASET_DIR / "molalign_dataset.jsonl"


def canonicalize(smi: str) -> str | None:
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return None
    return Chem.MolToSmiles(mol)


def main():
    data = json.loads(DATASET_JSON.read_text(encoding="utf-8"))
    print(f"Loaded {len(data)} records")

    fixed_canonical = 0
    fixed_isomeric = 0
    failed = []

    for rec in data:
        rid = rec.get("record_id", "?")
        smiles = rec.get("smiles", {})

        # Fix canonical SMILES
        old_can = smiles.get("canonical", "")
        if old_can:
            new_can = canonicalize(old_can)
            if new_can is None:
                failed.append((rid, old_can, "canonical"))
                continue
            if new_can != old_can:
                smiles["canonical"] = new_can
                fixed_canonical += 1

        # Fix isomeric SMILES
        old_iso = smiles.get("isomeric", "")
        if old_iso:
            new_iso = canonicalize(old_iso)
            if new_iso is None:
                failed.append((rid, old_iso, "isomeric"))
                continue
            if new_iso != old_iso:
                smiles["isomeric"] = new_iso
                fixed_isomeric += 1

    if failed:
        print(f"\nWARNING: {len(failed)} records failed RDKit parsing:")
        for rid, smi, field in failed[:10]:
            print(f"  {rid} ({field}): {smi}")
        if len(failed) > 10:
            print(f"  ... and {len(failed) - 10} more")

    print(f"\nFixed {fixed_canonical} canonical SMILES")
    print(f"Fixed {fixed_isomeric} isomeric SMILES")

    DATASET_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    DATASET_JSONL.write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in data),
        encoding="utf-8",
    )
    print(f"Saved to {DATASET_JSON}")
    print(f"Saved to {DATASET_JSONL}")


if __name__ == "__main__":
    main()
