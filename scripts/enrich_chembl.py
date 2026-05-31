"""
ChEMBL 生物活性数据填充
=======================
从 ChEMBL REST API 批量拉取 IC50/Ki/EC50 等生物活性数据，
填充到数据集的 properties.experimental.bioactivity 字段。
"""

import os, sys, json, time, logging
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

DATASET_PATH = PROJECT_ROOT / "data" / "processed" / "molalign_dataset.jsonl"
CHEMBL_BASE = "https://www.ebi.ac.uk/chembl/api/data"
HEADERS = {"Accept": "application/json"}
SESSION = requests.Session()
SESSION.headers.update(HEADERS)

# Assay types we care about
TARGET_ASSAY_TYPES = {"IC50", "Ki", "EC50", "Kd", "MIC", "AC50", "Potency"}


def chembl_get(endpoint, params=None, retries=3):
    """GET request to ChEMBL API with retry."""
    url = f"{CHEMBL_BASE}/{endpoint}"
    for attempt in range(retries):
        try:
            resp = SESSION.get(url, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 404:
                return None
            else:
                logger.warning(f"ChEMBL {url} returned {resp.status_code}")
        except requests.RequestException as e:
            logger.warning(f"ChEMBL request failed (attempt {attempt+1}): {e}")
            time.sleep(2)
    return None


def lookup_chembl_id(pubchem_cid):
    """Find ChEMBL ID from PubChem CID via cross-reference."""
    data = chembl_get("molecule", {"molecule_structures__molecule_chembl_id": "", "molecule_properties__undefined": ""})
    # Use direct molecule lookup by PubChem CID
    result = chembl_get(f"compound_record", {"compound_name": str(pubchem_cid), "src_id": "22"})
    if result and result.get("compound_records"):
        for rec in result["compound_records"]:
            if rec.get("compound_chembl_id"):
                return rec["compound_chembl_id"]
    # Fallback: search by molecule
    result = chembl_get(f"molecule.json", {"molecule_structures__standard_inchi_key": ""})
    return None


def fetch_bioactivity(chembl_id, max_records=5):
    """Fetch bioactivity data for a ChEMBL molecule."""
    if not chembl_id:
        return []

    data = chembl_get("activity", {
        "molecule_chembl_id": chembl_id,
        "standard_type": "IC50,Ki,EC50,Kd,AC50",
        "has_projection": "true",
        "limit": max_records * 3,  # Over-fetch to filter
    })

    if not data or not data.get("activities"):
        return []

    bioactivities = []
    seen = set()
    for act in data["activities"]:
        if len(bioactivities) >= max_records:
            break

        assay_type = act.get("standard_type", "")
        value = act.get("standard_value")
        units = act.get("standard_units", "")
        target_name = act.get("target_pref_name", "") or act.get("target_chembl_id", "")
        assay_chembl = act.get("assay_chembl_id", "")

        if not value or not assay_type:
            continue

        key = f"{assay_type}_{target_name}_{value}"
        if key in seen:
            continue
        seen.add(key)

        entry = {
            "assay_type": assay_type,
            "target": target_name or assay_chembl,
            "value": str(value),
            "unit": units,
            "source": f"ChEMBL ({assay_chembl})" if assay_chembl else "ChEMBL",
        }

        # Add DOI if available
        doc = act.get("document_chembl_id", "")
        if doc:
            entry["source_paper"] = f"ChEMBL document: {doc}"

        bioactivities.append(entry)

    return bioactivities


def fetch_chembl_ids_batch(records):
    """Fetch ChEMBL IDs for all records using their existing chembl_id or PubChem CID."""
    chembl_map = {}
    for r in records:
        mol_id = r["record_id"]
        # Use existing chembl_id if available
        existing = r.get("molecule_id", {}).get("chembl_id")
        if existing:
            chembl_map[mol_id] = existing
            continue

        # Try to find via PubChem CID
        cid = r.get("molecule_id", {}).get("pubchem_cid")
        if cid:
            # Use ChEMBL molecule filter by cross-ref
            result = chembl_get("molecule", {"molecule_structures__molecule_chembl_id__in": ""})
            # Direct approach: search ChEMBL by InChIKey
            inchikey = r.get("smiles", {}).get("inchikey", "")
            if inchikey:
                mol_data = chembl_get("molecule", {"molecule_structures__standard_inchi_key": inchikey, "limit": 1})
                if mol_data and mol_data.get("molecules"):
                    chembl_map[mol_id] = mol_data["molecules"][0]["molecule_chembl_id"]
                    continue
            chembl_map[mol_id] = None
        else:
            chembl_map[mol_id] = None

    return chembl_map


def main():
    print("=" * 60)
    print("ChEMBL Bioactivity Data Enrichment")
    print("=" * 60)

    # Load dataset
    records = []
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))
    print(f"Loaded {len(records)} records")

    # Step 1: Get ChEMBL IDs
    print("\n[1/3] Looking up ChEMBL IDs...")
    chembl_ids_found = 0
    for r in records:
        existing = r.get("molecule_id", {}).get("chembl_id")
        if existing and existing != "null":
            chembl_ids_found += 1
    print(f"  Already have {chembl_ids_found}/{len(records)} ChEMBL IDs")

    # Step 2: Fetch bioactivity data
    print("\n[2/3] Fetching bioactivity data from ChEMBL...")
    enriched_count = 0
    total_activities = 0

    for i, r in enumerate(records):
        mol_id = r["record_id"]
        mol_name = r.get("names", {}).get("common_name", "?")
        chembl_id = r.get("molecule_id", {}).get("chembl_id")

        # Skip null/empty chembl_ids
        if not chembl_id or chembl_id == "null":
            # Try InChIKey lookup
            inchikey = r.get("smiles", {}).get("inchikey", "")
            if inchikey:
                mol_data = chembl_get("molecule", {
                    "molecule_structures__standard_inchi_key": inchikey,
                    "limit": 1
                })
                if mol_data and mol_data.get("molecules"):
                    chembl_id = mol_data["molecules"][0]["molecule_chembl_id"]
                    # Update the record's chembl_id
                    r["molecule_id"]["chembl_id"] = chembl_id

        if not chembl_id or chembl_id == "null":
            continue

        activities = fetch_bioactivity(chembl_id, max_records=5)

        if activities:
            # Ensure experimental section exists
            if not r["properties"].get("experimental"):
                r["properties"]["experimental"] = {}

            r["properties"]["experimental"]["bioactivity"] = activities
            enriched_count += 1
            total_activities += len(activities)

            if enriched_count <= 5 or enriched_count % 20 == 0:
                print(f"  [{enriched_count}] {mol_id} ({mol_name}): {len(activities)} activities"
                      + (f" e.g. {activities[0]['assay_type']}={activities[0]['value']} {activities[0]['unit']} vs {activities[0]['target']}"
                         if activities else ""))

        # Rate limit
        if (i + 1) % 10 == 0:
            time.sleep(0.5)

    print(f"\n  Enriched: {enriched_count}/{len(records)} molecules")
    print(f"  Total activity records: {total_activities}")

    # Step 3: Save updated dataset
    print("\n[3/3] Saving updated dataset...")
    with open(DATASET_PATH, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    json_path = DATASET_PATH.with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"  Saved to {DATASET_PATH}")
    print(f"\nDone! {enriched_count} molecules enriched with ChEMBL bioactivity data.")


if __name__ == "__main__":
    main()
