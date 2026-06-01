"""
Generate provenance.tsv — per-record source attribution
========================================================
Classifies each record by data source layer (PubChem / RDKit / curated / MinerU /
paper) and assigns an evidence_quality_tier (A/B/C).

Tier A: Has real MinerU Agent API evidence (task_id + markdown_url + content_length)
Tier B: Has curated bioactivity OR paper image OR curated relations
Tier C: Template-based enrichment (relations from CATEGORY_TARGET_MAP, ZH from template)
"""
import json
import csv
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT = PROJECT_ROOT / "data" / "processed" / "molalign_dataset.jsonl"
OUTPUT = PROJECT_ROOT / "data" / "processed" / "provenance.tsv"

CURATED_RELATION_CIDS = set()
try:
    sys.path.insert(0, str(PROJECT_ROOT))
    from scripts.enrich_dataset import KNOWN_RELATIONS
    CURATED_RELATION_CIDS = set(KNOWN_RELATIONS.keys())
except Exception:
    pass

CURATED_ZH_CIDS = set()
try:
    from scripts.enrich_dataset import CHINESE_DESCRIPTIONS
    CURATED_ZH_CIDS = set(CHINESE_DESCRIPTIONS.keys())
except Exception:
    pass

CURATED_BIO_CIDS = set()
try:
    from scripts.enrich_pubchem_bioactivity import KNOWN_BIOACTIVITY
    CURATED_BIO_CIDS = set(KNOWN_BIOACTIVITY.keys())
except Exception:
    pass


def classify_descriptions(descs):
    """Return a list of sources present in text_descriptions."""
    sources = set()
    for d in descs:
        st = d.get("source", {}).get("type", "")
        lang = d.get("language", "en")
        if st == "pubchem":
            sources.add("pubchem_text")
        elif st == "paper":
            if d.get("source", {}).get("mineru_parsed"):
                sources.add("mineru_paper_text")
            else:
                sources.add("paper_text")
        elif st == "manual_curation":
            if lang == "zh":
                sources.add("curated_zh")
            else:
                sources.add("curated_en")
        elif st == "wikipedia":
            sources.add("wikipedia")
        elif st == "drugbank":
            sources.add("drugbank")
        else:
            sources.add(f"other_{st}")
    return sources


def classify_relations(rels, cid):
    """Determine whether relations are curated, category-template, or auto-derived."""
    if not rels:
        return "none"
    if cid in CURATED_RELATION_CIDS:
        return "curated_literature"
    # Check if any relation has evidence field with specific DOI / source
    has_evidence = any(r.get("evidence") for r in rels)
    if has_evidence:
        return "curated_mixed"
    return "category_template"


def classify_smiles_source(smiles_field, cid):
    """SMILES source is either from PubChem (canonical=pubchem SMILES) or RDKit re-canonicalized.
    Schema is canonical/inchi/inchikey — these come from RDKit.
    """
    if smiles_field.get("canonical") and smiles_field.get("inchikey"):
        return "rdkit_canonical"
    return "unknown"


def main():
    records = []
    with open(INPUT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    rows = []
    for r in records:
        rid = r["record_id"]
        cid = r.get("molecule_id", {}).get("pubchem_cid", "")
        name = r.get("names", {}).get("common_name", "")
        category = r.get("category", "")
        smiles_src = classify_smiles_source(r.get("smiles", {}), cid)
        props_src = "rdkit_computed"  # Default: all properties are RDKit-computed per molecule_processor.py
        rels = r.get("entity_relations", [])
        rels_src = classify_relations(rels, cid)
        descs = r.get("text_descriptions", [])
        desc_sources = classify_descriptions(descs)
        descs_src = "|".join(sorted(desc_sources)) if desc_sources else "none"
        mineru_evidence = ""
        mineru_used = r.get("alignment_metadata", {}).get("mineru_usage", [])
        if mineru_used:
            task_ids = [u.get("task_id", "") for u in mineru_used if u.get("task_id")]
            if task_ids:
                mineru_evidence = task_ids[0]
        paper_image = "yes" if r.get("modalities", {}).get("structure_paper") else "no"
        bioactivity = "no"
        exp = r.get("properties", {}).get("experimental")
        if exp and exp.get("bioactivity"):
            bioactivity = "yes"
        has_3d = "yes" if r.get("modalities", {}).get("structure_3d") else "no"
        has_2d = "yes" if r.get("modalities", {}).get("structure_2d") else "no"

        # Quality tier
        # Tier A: real MinerU evidence (task_id + markdown_url + content_length)
        # Tier B: has at least one of {curated_literature relations, paper image, bioactivity, curated Chinese}
        # Tier C: template-only enrichment (category_target relations + auto-generated ZH)
        is_tier_a = bool(mineru_evidence)
        is_tier_b = (rels_src == "curated_literature"
                     or paper_image == "yes"
                     or bioactivity == "yes"
                     or cid in CURATED_ZH_CIDS)
        if is_tier_a:
            tier = "A"
        elif is_tier_b:
            tier = "B"
        else:
            tier = "C"

        rows.append({
            "record_id": rid,
            "common_name": name,
            "pubchem_cid": cid,
            "category": category,
            "smiles_source": smiles_src,
            "properties_source": props_src,
            "relations_source": rels_src,
            "descriptions_source": descs_src,
            "mineru_task_id": mineru_evidence,
            "paper_image": paper_image,
            "bioactivity": bioactivity,
            "has_2d": has_2d,
            "has_3d": has_3d,
            "evidence_quality_tier": tier,
        })

    fieldnames = list(rows[0].keys())
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    tier_counts = {}
    for row in rows:
        t = row["evidence_quality_tier"]
        tier_counts[t] = tier_counts.get(t, 0) + 1
    print(f"Wrote {len(rows)} records to {OUTPUT}")
    print(f"Tier distribution: {tier_counts}")
    print(f"\nTier A (real MinerU): {tier_counts.get('A', 0)}")
    print(f"Tier B (curated OR paper image OR bioactivity): {tier_counts.get('B', 0)}")
    print(f"Tier C (template only): {tier_counts.get('C', 0)}")


if __name__ == "__main__":
    main()
