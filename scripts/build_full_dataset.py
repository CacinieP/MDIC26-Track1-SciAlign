"""
MolAlign Full Dataset Builder
==============================
Fetches molecular data from PubChem REST API, computes RDKit properties,
generates 2D/3D structures, and produces a cross-modal alignment dataset
conforming to the MolecularCrossModalAlignment JSON Schema.

Usage:
    python scripts/build_full_dataset.py
    python scripts/build_full_dataset.py --input molecule_db.py --output-dir data/processed
    python scripts/build_full_dataset.py --start-from MOL-000050
    python scripts/build_full_dataset.py --skip-images
    python scripts/build_full_dataset.py --batch-size 30
"""

import os
import sys
import json
import time
import argparse
import logging
import importlib.util
import traceback
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Project path setup -- ensure project root is importable
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# ---------------------------------------------------------------------------
# Optional dependency imports with graceful degradation
# ---------------------------------------------------------------------------
try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    from rdkit import Chem, RDLogger
    from rdkit.Chem import Descriptors, Draw, AllChem, rdMolDescriptors
    from rdkit.Chem.QED import qed
    RDKIT_AVAILABLE = True
    RDLogger.logger().setLevel(RDLogger.ERROR)
except ImportError:
    RDKIT_AVAILABLE = False

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, **kwargs):
        return iterable

from src.alignment_validator import AlignmentValidator

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
PUBCHEM_PROPS = (
    "CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,"
    "MolecularWeight,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount,"
    "RotatableBondCount,HeavyAtomCount,Charge"
)

REQUEST_DELAY = 0.3          # seconds between PubChem requests
MAX_RETRIES = 3
RETRY_BACKOFF = 2            # exponential backoff multiplier
RETRY_STATUS_CODES = (429, 500, 502, 503, 504)


# ---------------------------------------------------------------------------
# HTTP session with built-in retry
# ---------------------------------------------------------------------------

def _build_session() -> "requests.Session":
    """Create a requests Session with retry logic."""
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=RETRY_BACKOFF,
        status_forcelist=RETRY_STATUS_CODES,
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({"Accept": "application/json"})
    return session


# ---------------------------------------------------------------------------
# Molecule DB loader
# ---------------------------------------------------------------------------

def load_molecule_db(path: str) -> Dict[str, Dict[str, Any]]:
    """Load MOLECULE_DB from an arbitrary Python file."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Molecule DB file not found: {path}")

    spec = importlib.util.spec_from_file_location("molecule_db_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "MOLECULE_DB"):
        raise AttributeError(f"{path} does not define MOLECULE_DB")

    return module.MOLECULE_DB


# ---------------------------------------------------------------------------
# PubChem API helpers
# ---------------------------------------------------------------------------

def fetch_batch_properties(
    session: "requests.Session",
    cids: List[int],
) -> Dict[int, Dict[str, Any]]:
    """Fetch properties for a batch of CIDs (max 100 per request)."""
    cid_str = ",".join(str(c) for c in cids)
    url = f"{PUBCHEM_BASE}/compound/cid/{cid_str}/property/{PUBCHEM_PROPS}/JSON"

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=60)
            if resp.status_code == 200:
                props_list = resp.json().get("PropertyTable", {}).get("Properties", [])
                return {p["CID"]: p for p in props_list}
            if resp.status_code in RETRY_STATUS_CODES:
                wait = REQUEST_DELAY * (RETRY_BACKOFF ** attempt)
                logger.warning(
                    f"PubChem returned {resp.status_code}, retry {attempt}/{MAX_RETRIES} in {wait:.1f}s"
                )
                time.sleep(wait)
                continue
            logger.error(f"PubChem returned {resp.status_code} for batch property fetch")
            return {}
        except requests.RequestException as exc:
            wait = REQUEST_DELAY * (RETRY_BACKOFF ** attempt)
            logger.warning(f"Request error (attempt {attempt}/{MAX_RETRIES}): {exc}")
            time.sleep(wait)

    logger.error("Batch property fetch exhausted retries")
    return {}


def fetch_synonyms(
    session: "requests.Session",
    cid: int,
) -> List[str]:
    """Fetch up to 20 synonyms for a CID."""
    url = f"{PUBCHEM_BASE}/compound/cid/{cid}/synonyms/TXT"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=15)
            if resp.status_code == 200:
                lines = [s.strip() for s in resp.text.strip().split("\n") if s.strip()]
                return lines[:20]
            if resp.status_code in RETRY_STATUS_CODES:
                time.sleep(REQUEST_DELAY * (RETRY_BACKOFF ** attempt))
                continue
            return []
        except requests.RequestException:
            time.sleep(REQUEST_DELAY * (RETRY_BACKOFF ** attempt))
    return []


def fetch_description(
    session: "requests.Session",
    cid: int,
) -> str:
    """Fetch the first substantial description text for a CID."""
    url = f"{PUBCHEM_BASE}/compound/cid/{cid}/description/JSON"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=15)
            if resp.status_code == 200:
                infos = resp.json().get("InformationList", {}).get("Information", [])
                for info in infos:
                    desc = info.get("Description", "")
                    if desc and len(desc) > 50:
                        return desc
            if resp.status_code in RETRY_STATUS_CODES:
                time.sleep(REQUEST_DELAY * (RETRY_BACKOFF ** attempt))
                continue
            return ""
        except requests.RequestException:
            time.sleep(REQUEST_DELAY * (RETRY_BACKOFF ** attempt))
    return ""


# ---------------------------------------------------------------------------
# RDKit computation helpers
# ---------------------------------------------------------------------------

def compute_rdkit_props(smiles: str) -> Dict[str, Any]:
    """Compute extended properties from RDKit."""
    if not RDKIT_AVAILABLE:
        return {}
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {}

    mw = Descriptors.ExactMolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)
    rot = Descriptors.NumRotatableBonds(mol)
    ring_count = Descriptors.RingCount(mol)

    lipinski_violations = sum([mw > 500, logp > 5, hbd > 5, hba > 10])

    try:
        qed_score = round(qed(mol), 4)
    except Exception:
        qed_score = None

    return {
        "exact_mass": round(mw, 4),
        "num_h_donors": hbd,
        "num_h_acceptors": hba,
        "num_rotatable_bonds": rot,
        "ring_count": ring_count,
        "lipinski_violations": lipinski_violations,
        "qed_score": qed_score,
    }


def generate_2d_image(smiles: str, output_path: str) -> bool:
    """Generate a 512x512 2D molecular depiction PNG."""
    if not RDKIT_AVAILABLE:
        return False
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    try:
        img = Draw.MolToImage(mol, size=(512, 512))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, "PNG")
        return True
    except Exception as exc:
        logger.debug(f"2D image generation failed for {smiles}: {exc}")
        return False


def generate_3d_conformer(smiles: str, output_path: str) -> bool:
    """Generate a 3D conformer SDF via ETKDGv3 + MMFF optimisation."""
    if not RDKIT_AVAILABLE:
        return False
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    try:
        mol_h = Chem.AddHs(mol)
        params = AllChem.ETKDGv3()
        params.randomSeed = 42
        result = AllChem.EmbedMolecule(mol_h, params)
        if result == -1:
            logger.debug(f"3D embedding failed for {smiles}")
            return False
        try:
            AllChem.MMFFOptimizeMolecule(mol_h, maxIters=200)
        except Exception:
            pass  # optimisation is best-effort
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        writer = Chem.SDWriter(output_path)
        writer.write(mol_h)
        writer.close()
        return True
    except Exception as exc:
        logger.debug(f"3D conformer generation failed for {smiles}: {exc}")
        return False


# ---------------------------------------------------------------------------
# Record builder
# ---------------------------------------------------------------------------

def _safe_float(val: Any, default=None) -> Optional[float]:
    if val is None:
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def _safe_int(val: Any, default=None) -> Optional[int]:
    if val is None:
        return default
    try:
        return int(val)
    except (TypeError, ValueError):
        return default


def build_record(
    record_id: str,
    mol_info: Dict[str, Any],
    pubchem_props: Dict[str, Any],
    synonyms: List[str],
    description: str,
    output_dir: str,
    generate_images: bool = True,
) -> Dict[str, Any]:
    """
    Construct a single cross-modal alignment record conforming to the
    MolecularCrossModalAlignment schema.
    """
    cid = mol_info["pubchem_cid"]
    common_name = mol_info["name"]
    category = mol_info.get("category", "Unknown")

    # ---- SMILES identifiers ------------------------------------------------
    canonical_smiles = (
        pubchem_props.get("CanonicalSMILES")
        or pubchem_props.get("SMILES", "")
    )
    isomeric_smiles = pubchem_props.get("IsomericSMILES") or canonical_smiles
    inchi = pubchem_props.get("InChI", "")
    inchikey = pubchem_props.get("InChIKey", "")

    # ---- Names -------------------------------------------------------------
    iupac_name = pubchem_props.get("IUPACName")
    mol_synonyms = synonyms[:20]

    # ---- Physicochemical properties (PubChem) ------------------------------
    mw = _safe_float(pubchem_props.get("MolecularWeight"), 0)
    logp = _safe_float(pubchem_props.get("XLogP"))
    tpsa = _safe_float(pubchem_props.get("TPSA"))
    hbd = _safe_int(pubchem_props.get("HBondDonorCount"))
    hba = _safe_int(pubchem_props.get("HBondAcceptorCount"))
    rot = _safe_int(pubchem_props.get("RotatableBondCount"))
    heavy = _safe_int(pubchem_props.get("HeavyAtomCount"))
    charge = _safe_int(pubchem_props.get("Charge"), 0)

    # ---- RDKit computed properties -----------------------------------------
    rdkit_extra = compute_rdkit_props(canonical_smiles) if canonical_smiles else {}

    # ---- Generate images ---------------------------------------------------
    img_2d_rel = f"images/2d/{record_id}.png"
    sdf_3d_rel = f"models/3d/{record_id}.sdf"
    img_generated = False
    sdf_generated = False

    if generate_images and canonical_smiles:
        abs_out = os.path.abspath(output_dir)
        img_generated = generate_2d_image(canonical_smiles, os.path.join(abs_out, img_2d_rel))
        sdf_generated = generate_3d_conformer(canonical_smiles, os.path.join(abs_out, sdf_3d_rel))

    # ---- Text descriptions -------------------------------------------------
    text_descriptions = []

    if description:
        text_descriptions.append({
            "type": "general_description",
            "content": description[:2000],
            "source": {
                "type": "pubchem",
                "reference": f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}",
                "section": None,
                "mineru_parsed": False,
            },
            "language": "en",
        })

    # Fallback: always ensure at least one description entry
    if not text_descriptions:
        text_descriptions.append({
            "type": "general_description",
            "content": f"{common_name} (CID {cid}) is classified as {category}.",
            "source": {
                "type": "manual_curation",
                "reference": None,
                "section": None,
                "mineru_parsed": False,
            },
            "language": "en",
        })

    # ---- Alignment confidence & validation status --------------------------
    has_smiles = bool(canonical_smiles)
    has_pubchem_desc = bool(description)
    has_synonyms = len(mol_synonyms) > 0
    has_inchi = bool(inchi)

    completeness_fields = [has_smiles, has_pubchem_desc, has_synonyms, has_inchi]
    completeness_ratio = sum(completeness_fields) / len(completeness_fields)

    if completeness_ratio >= 0.75:
        alignment_confidence = 0.85
    else:
        alignment_confidence = 0.70

    if has_smiles and RDKIT_AVAILABLE:
        mol_check = Chem.MolFromSmiles(canonical_smiles)
        validation_status = "automated_pass" if mol_check is not None else "flagged_for_review"
    else:
        validation_status = "flagged_for_review"

    # ---- Assemble record ---------------------------------------------------
    record = {
        "record_id": record_id,
        "molecule_id": {
            "pubchem_cid": cid,
            "chembl_id": None,
            "drugbank_id": None,
            "cas_number": None,
        },
        "smiles": {
            "canonical": canonical_smiles,
            "isomeric": isomeric_smiles if isomeric_smiles != canonical_smiles else canonical_smiles,
            "inchi": inchi,
            "inchikey": inchikey,
        },
        "names": {
            "iupac_name": iupac_name,
            "common_name": common_name,
            "synonyms": mol_synonyms,
        },
        "modalities": {
            "structure_2d": {
                "rdkit_generated": img_2d_rel if img_generated else None,
                "image_format": "png" if img_generated else None,
                "image_size": "512x512" if img_generated else None,
            },
            "structure_paper": None,
            "structure_3d": {
                "sdf_path": sdf_3d_rel if sdf_generated else None,
                "conformer_method": "RDKit_ETKDG" if sdf_generated else None,
            } if sdf_generated else None,
            "table_data": None,
        },
        "properties": {
            "physicochemical": {
                "molecular_weight": round(mw, 2) if mw else None,
                "exact_mass": rdkit_extra.get("exact_mass"),
                "logp": logp,
                "tpsa": tpsa,
                "hydrogen_bond_donors": hbd,
                "hydrogen_bond_acceptors": hba,
                "rotatable_bonds": rot,
                "heavy_atoms": heavy,
                "ring_count": rdkit_extra.get("ring_count"),
                "formal_charge": charge,
            },
            "drug_likeness": {
                "lipinski_violations": rdkit_extra.get("lipinski_violations"),
                "ghose_violations": None,
                "veber_violations": None,
                "bioavailability_score": None,
                "synthetic_accessibility": None,
                "qed_score": rdkit_extra.get("qed_score"),
            },
            "experimental": None,
        },
        "text_descriptions": text_descriptions,
        "entity_relations": [],
        "alignment_metadata": {
            "alignment_confidence": alignment_confidence,
            "validation_status": validation_status,
            "mineru_usage": [],
            "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "version": "1.0.0",
        },
        "category": category,
    }

    return record


# ---------------------------------------------------------------------------
# Dataset-level operations
# ---------------------------------------------------------------------------

def save_dataset(records: List[Dict], output_dir: str) -> Tuple[str, str]:
    """Save records as both JSONL and JSON."""
    os.makedirs(output_dir, exist_ok=True)

    jsonl_path = os.path.join(output_dir, "molalign_dataset.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    logger.info(f"JSONL saved: {jsonl_path} ({len(records)} records)")

    json_path = os.path.join(output_dir, "molalign_dataset.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    logger.info(f"JSON saved:  {json_path}")

    return jsonl_path, json_path


def validate_dataset(records: List[Dict]) -> Dict[str, Any]:
    """Run the AlignmentValidator over the full dataset."""
    validator = AlignmentValidator()
    results = validator.validate_dataset(records)
    return results


def compute_statistics(records: List[Dict], failed: List[Dict]) -> Dict[str, Any]:
    """Compute summary statistics for the build run."""
    categories = {}
    for rec in records:
        cat = rec.get("category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1

    n = len(records) or 1
    with_2d = sum(1 for r in records if r["modalities"]["structure_2d"].get("rdkit_generated"))
    with_3d = sum(1 for r in records if r["modalities"].get("structure_3d") and r["modalities"]["structure_3d"].get("sdf_path"))
    with_desc = sum(1 for r in records if r["text_descriptions"])
    validated = sum(1 for r in records if r["alignment_metadata"]["validation_status"] == "automated_pass")
    avg_descs = sum(len(r["text_descriptions"]) for r in records) / n
    avg_conf = sum(r["alignment_metadata"]["alignment_confidence"] for r in records) / n

    stats = {
        "total": len(records),
        "failed": len(failed),
        "categories": categories,
        "num_categories": len(categories),
        "with_2d_image": with_2d,
        "with_3d_conformer": with_3d,
        "with_description": with_desc,
        "validated_pass": validated,
        "avg_descriptions": round(avg_descs, 2),
        "avg_alignment_confidence": round(avg_conf, 3),
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    return stats


def print_summary(stats: Dict, failed: List[Dict], output_dir: str, stats_path: str, report_path: str):
    """Print human-readable build summary."""
    print(f"\n{'=' * 64}")
    print(f"  MolAlign Dataset Build Complete")
    print(f"{'=' * 64}")
    print(f"  Total records:       {stats['total']}")
    print(f"  Failed:              {stats['failed']}")
    print(f"  Categories:          {stats['num_categories']}")
    print(f"  With 2D image:       {stats['with_2d_image']}")
    print(f"  With 3D conformer:   {stats['with_3d_conformer']}")
    print(f"  With description:    {stats['with_description']}")
    print(f"  Validated pass:      {stats['validated_pass']}")
    print(f"  Avg descriptions:    {stats['avg_descriptions']}")
    print(f"  Avg confidence:      {stats['avg_alignment_confidence']}")
    print(f"{'=' * 64}")
    print(f"  Output directory:  {output_dir}")
    print(f"  Statistics file:   {stats_path}")
    print(f"  Validation report: {report_path}")
    if failed:
        print(f"\n  Failed molecules (first 10):")
        for entry in failed[:10]:
            print(f"    {entry['id']} ({entry['name']}): {entry['error']}")
    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build the full MolAlign cross-modal alignment dataset"
    )
    parser.add_argument(
        "--input",
        default=os.path.join(PROJECT_ROOT, "molecule_db.py"),
        help="Path to the Python file containing MOLECULE_DB dictionary",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join(PROJECT_ROOT, "data", "processed"),
        help="Output directory for dataset files and images",
    )
    parser.add_argument(
        "--skip-images",
        action="store_true",
        help="Skip 2D PNG and 3D SDF generation",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="PubChem batch size for property fetches (max 100)",
    )
    parser.add_argument(
        "--start-from",
        default=None,
        help="Start from a specific record ID (e.g. MOL-000050) for resume",
    )
    args = parser.parse_args()

    # ------------------------------------------------------------------
    # Pre-flight checks
    # ------------------------------------------------------------------
    if not REQUESTS_AVAILABLE:
        print("ERROR: 'requests' library is required. Install with: pip install requests")
        sys.exit(1)

    if not RDKIT_AVAILABLE:
        print("WARNING: RDKit is not available. Image and property generation will be skipped.")
        print("  Install with: pip install rdkit-pypi")

    # ------------------------------------------------------------------
    # Load molecule database
    # ------------------------------------------------------------------
    logger.info(f"Loading molecule DB from: {args.input}")
    try:
        molecule_db = load_molecule_db(args.input)
    except (FileNotFoundError, AttributeError) as exc:
        logger.error(str(exc))
        sys.exit(1)

    # Sort and optionally slice
    mol_items: List[Tuple[str, Dict]] = sorted(molecule_db.items())
    if args.start_from:
        mol_items = [(k, v) for k, v in mol_items if k >= args.start_from]

    total = len(mol_items)
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    logger.info(f"Building dataset: {total} molecules")
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"RDKit available:  {RDKIT_AVAILABLE}")
    logger.info(f"Generate images:  {not args.skip_images}")

    session = _build_session()

    # ==================================================================
    # Phase 1: Batch fetch PubChem properties
    # ==================================================================
    logger.info("\n=== Phase 1: Batch fetch PubChem properties ===")
    all_props: Dict[int, Dict] = {}
    cids = [v["pubchem_cid"] for _, v in mol_items]

    batch_size = min(args.batch_size, 100)
    for i in range(0, len(cids), batch_size):
        batch = cids[i : i + batch_size]
        batch_num = i // batch_size + 1
        logger.info(f"  Batch {batch_num}: fetching properties for {len(batch)} CIDs ...")
        batch_props = fetch_batch_properties(session, batch)
        all_props.update(batch_props)
        time.sleep(REQUEST_DELAY)

    logger.info(f"  Properties fetched for {len(all_props)}/{len(cids)} molecules")

    # ==================================================================
    # Phase 2: Build records (synonyms + description + images per molecule)
    # ==================================================================
    logger.info("\n=== Phase 2: Build individual records ===")
    records: List[Dict] = []
    failed: List[Dict] = []

    for record_id, mol_info in tqdm(mol_items, desc="Building records", unit="mol"):
        cid = mol_info["pubchem_cid"]
        props = all_props.get(cid, {})

        if not props:
            logger.warning(f"  {record_id} ({mol_info['name']}): no PubChem data, skipping")
            failed.append({
                "id": record_id,
                "name": mol_info["name"],
                "cid": cid,
                "error": "No PubChem data returned",
            })
            continue

        # Fetch synonyms
        synonyms = fetch_synonyms(session, cid)
        time.sleep(REQUEST_DELAY)

        # Fetch description
        description = fetch_description(session, cid)
        time.sleep(REQUEST_DELAY)

        # Build the alignment record
        try:
            record = build_record(
                record_id=record_id,
                mol_info=mol_info,
                pubchem_props=props,
                synonyms=synonyms,
                description=description,
                output_dir=output_dir,
                generate_images=not args.skip_images,
            )
            records.append(record)
        except Exception as exc:
            logger.error(f"  {record_id} ({mol_info['name']}): build error -- {exc}")
            logger.debug(traceback.format_exc())
            failed.append({
                "id": record_id,
                "name": mol_info["name"],
                "cid": cid,
                "error": str(exc),
            })

    # ==================================================================
    # Phase 3: Save dataset files
    # ==================================================================
    logger.info("\n=== Phase 3: Saving dataset ===")
    jsonl_path, json_path = save_dataset(records, output_dir)

    # ==================================================================
    # Phase 4: Validation
    # ==================================================================
    logger.info("\n=== Phase 4: Validation ===")
    if records:
        validation_results = validate_dataset(records)
        report_path = os.path.join(output_dir, "validation_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(validation_results, f, ensure_ascii=False, indent=2)
        logger.info(f"  Validation report: {report_path}")
        logger.info(
            f"  Valid: {validation_results['valid']} / {validation_results['total']}  "
            f"({validation_results['valid'] / max(validation_results['total'], 1) * 100:.1f}%)"
        )
        if validation_results["errors"]:
            logger.warning(f"  Records with errors: {len(validation_results['errors'])}")
            for rid, errs in list(validation_results["errors"].items())[:5]:
                logger.warning(f"    {rid}: {'; '.join(errs[:3])}")
    else:
        report_path = ""
        logger.warning("  No records to validate.")

    # ==================================================================
    # Phase 5: Statistics and summary
    # ==================================================================
    logger.info("\n=== Phase 5: Statistics ===")
    stats = compute_statistics(records, failed)
    stats_path = os.path.join(output_dir, "dataset_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print_summary(stats, failed, output_dir, stats_path, report_path)

    return records, stats


if __name__ == "__main__":
    main()
