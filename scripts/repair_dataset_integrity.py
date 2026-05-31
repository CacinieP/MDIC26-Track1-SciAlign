#!/usr/bin/env python3
"""Repair high-priority dataset integrity issues.

This script is intentionally conservative:
1. Canonicalize SMILES in both JSON and JSONL outputs.
2. Recompute key physicochemical fields with RDKit so validation uses one
   property standard instead of mixing PubChem and RDKit definitions.
3. Remove template-like MinerU usage records and keep only records backed by
   the real MinerU Agent API parsing log.
4. Download MinerU markdown outputs when URLs are available in the log.
5. Rebuild the sample dataset directly from the processed dataset.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import requests
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, Draw, rdMolDescriptors
from rdkit.Chem.QED import qed


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DATASET_JSONL = PROCESSED_DIR / "molalign_dataset.jsonl"
DATASET_JSON = PROCESSED_DIR / "molalign_dataset.json"
SAMPLES_DIR = PROJECT_ROOT / "data" / "samples"
MINERU_DIR = PROJECT_ROOT / "data" / "raw" / "parsed_mineru_api"
PARSING_LOG = MINERU_DIR / "parsing_log.json"
IMAGE_2D_DIR = PROCESSED_DIR / "images" / "2d"
MODEL_3D_DIR = PROCESSED_DIR / "models" / "3d"


PAPER_MOLECULE_MAP = {
    "acetaminophen_pharmacology.pdf": ["Acetaminophen", "Paracetamol"],
    "caffeine_molecules.pdf": ["Caffeine"],
    "curcumin_pharmacology.pdf": ["Curcumin"],
    "dopamine_neuroscience.pdf": ["Dopamine"],
    "doxorubicin_anticancer.pdf": ["Doxorubicin"],
    "ibuprofen_pharmacology.pdf": ["Ibuprofen"],
    "metformin_frontiers.pdf": ["Metformin"],
    "metformin_pharmaceutics.pdf": ["Metformin"],
    "morphine_opioid.pdf": ["Morphine"],
    "paclitaxel_pharmacology.pdf": ["Paclitaxel"],
}


PAPER_DOI_MAP = {
    "acetaminophen_pharmacology.pdf": "10.3389/fphar.2020.00794",
    "caffeine_molecules.pdf": "10.3390/molecules26195811",
    "curcumin_pharmacology.pdf": "10.3389/fphar.2017.00687",
    "dopamine_neuroscience.pdf": "10.3389/fnins.2017.00724",
    "doxorubicin_anticancer.pdf": "10.3390/ijms221910576",
    "ibuprofen_pharmacology.pdf": "10.3389/fphar.2017.00263",
    "metformin_frontiers.pdf": "10.3389/fendo.2018.00753",
    "metformin_pharmaceutics.pdf": "10.3390/pharmaceutics12030290",
    "morphine_opioid.pdf": "10.3390/molecules26195811",
    "paclitaxel_pharmacology.pdf": "10.3389/fphar.2019.01330",
}


SAMPLE_RECORD_IDS = [
    "MOL-000002",  # Ibuprofen
    "MOL-000021",  # Paclitaxel
    "MOL-000023",  # Doxorubicin
    "MOL-000033",  # Metformin
    "MOL-000058",  # Morphine
    "MOL-000080",  # Curcumin
    "MOL-000086",  # Dopamine
    "MOL-000109",  # Caffeine
    "MOL-000120",  # Acetaminophen
    "MOL-000001",  # Aspirin
    "MOL-000007",  # Penicillin G
    "MOL-000100",  # Ascorbic acid
]


def load_records() -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in DATASET_JSONL.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_records(records: list[dict[str, Any]]) -> None:
    DATASET_JSONL.write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records),
        encoding="utf-8",
    )
    DATASET_JSON.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def canonicalize_smiles(smiles: str, *, isomeric: bool = True) -> str | None:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return Chem.MolToSmiles(mol, isomericSmiles=isomeric)


def repair_smiles_and_properties(record: dict[str, Any]) -> tuple[int, int]:
    smiles = record.get("smiles") or {}
    fixed_smiles = 0
    fixed_properties = 0

    canonical = smiles.get("canonical")
    if canonical:
        canonical_new = canonicalize_smiles(canonical)
        if canonical_new and canonical_new != canonical:
            smiles["canonical"] = canonical_new
            canonical = canonical_new
            fixed_smiles += 1

    isomeric = smiles.get("isomeric")
    if isomeric:
        isomeric_new = canonicalize_smiles(isomeric)
        if isomeric_new and isomeric_new != isomeric:
            smiles["isomeric"] = isomeric_new
            fixed_smiles += 1

    mol = Chem.MolFromSmiles(canonical) if canonical else None
    if mol is None:
        return fixed_smiles, fixed_properties

    props = record.setdefault("properties", {})
    phys = props.setdefault("physicochemical", {})
    drug = props.setdefault("drug_likeness", {})

    exact_mass = round(Descriptors.ExactMolWt(mol), 4)
    values = {
        "molecular_weight": round(exact_mass, 2),
        "exact_mass": exact_mass,
        "logp": round(Descriptors.MolLogP(mol), 2),
        "tpsa": round(rdMolDescriptors.CalcTPSA(mol), 2),
        "hydrogen_bond_donors": Descriptors.NumHDonors(mol),
        "hydrogen_bond_acceptors": Descriptors.NumHAcceptors(mol),
        "rotatable_bonds": Descriptors.NumRotatableBonds(mol),
        "heavy_atoms": mol.GetNumHeavyAtoms(),
        "ring_count": Descriptors.RingCount(mol),
        "formal_charge": Chem.GetFormalCharge(mol),
    }
    for key, value in values.items():
        if phys.get(key) != value:
            phys[key] = value
            fixed_properties += 1

    mw = exact_mass
    logp = values["logp"]
    hbd = values["hydrogen_bond_donors"]
    hba = values["hydrogen_bond_acceptors"]
    lipinski_violations = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
    drug_values = {
        "lipinski_violations": lipinski_violations,
        "qed_score": round(qed(mol), 4),
    }
    for key, value in drug_values.items():
        if drug.get(key) != value:
            drug[key] = value
            fixed_properties += 1

    return fixed_smiles, fixed_properties


def generate_2d_image(smiles: str, output_path: Path) -> bool:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image = Draw.MolToImage(mol, size=(512, 512))
    image.save(output_path, "PNG")
    return True


def generate_3d_conformer(smiles: str, output_path: Path) -> bool:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    try:
        mol_h = Chem.AddHs(mol)
        params = AllChem.ETKDGv3()
        params.randomSeed = 42
        result = AllChem.EmbedMolecule(mol_h, params)
        if result == -1:
            return False
        try:
            AllChem.MMFFOptimizeMolecule(mol_h, maxIters=200)
        except Exception:
            pass
        output_path.parent.mkdir(parents=True, exist_ok=True)
        writer = Chem.SDWriter(str(output_path))
        writer.write(mol_h)
        writer.close()
        return True
    except Exception:
        return False


def ensure_structure_assets(record: dict[str, Any]) -> tuple[int, int, int]:
    """Ensure referenced 2D PNG and 3D SDF assets exist on disk."""
    smiles = (record.get("smiles") or {}).get("canonical")
    if not smiles:
        return 0, 0, 0

    record_id = record["record_id"]
    modalities = record.setdefault("modalities", {})

    generated_2d = 0
    structure_2d = modalities.setdefault("structure_2d", {})
    image_rel = structure_2d.get("rdkit_generated") or f"images/2d/{record_id}.png"
    image_path = PROCESSED_DIR / image_rel
    if not image_path.exists() and generate_2d_image(smiles, image_path):
        generated_2d = 1
    structure_2d["rdkit_generated"] = image_rel
    structure_2d["image_format"] = "png"
    structure_2d["image_size"] = "512x512"

    generated_3d = 0
    failed_3d = 0
    structure_3d = modalities.get("structure_3d")
    if structure_3d is not None:
        sdf_rel = structure_3d.get("sdf_path") or f"models/3d/{record_id}.sdf"
        sdf_path = PROCESSED_DIR / sdf_rel
        if not sdf_path.exists():
            if generate_3d_conformer(smiles, sdf_path):
                generated_3d = 1
            else:
                modalities["structure_3d"] = None
                failed_3d = 1
        if modalities.get("structure_3d") is not None:
            modalities["structure_3d"]["sdf_path"] = sdf_rel
            modalities["structure_3d"]["conformer_method"] = "RDKit_ETKDG"

    return generated_2d, generated_3d, failed_3d


def build_name_index(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    name_index: dict[str, dict[str, Any]] = {}
    for record in records:
        names = record.get("names") or {}
        for name in [names.get("common_name"), names.get("iupac_name")]:
            if name:
                name_index[name.casefold()] = record
        for synonym in names.get("synonyms") or []:
            if synonym:
                name_index[synonym.casefold()] = record
    return name_index


def extract_relevant_text(markdown: str, molecule_name: str, max_chars: int = 1500) -> str:
    lines = [line.strip() for line in markdown.splitlines() if line.strip()]
    needle = molecule_name.casefold()
    aliases = {needle}
    if needle == "acetaminophen":
        aliases.add("paracetamol")
    if needle == "paracetamol":
        aliases.add("acetaminophen")

    for idx, line in enumerate(lines):
        if any(alias in line.casefold() for alias in aliases):
            start = max(0, idx - 2)
            end = min(len(lines), idx + 12)
            snippet = " ".join(lines[start:end])
            return snippet[:max_chars]

    for line in lines:
        if len(line) > 160 and not line.startswith("#") and not line.startswith("!"):
            return line[:max_chars]

    return ""


def download_markdown(pdf_name: str, markdown_url: str | None) -> str:
    output_path = MINERU_DIR / pdf_name.replace(".pdf", ".md")
    if output_path.exists() and output_path.stat().st_size > 0:
        return output_path.read_text(encoding="utf-8", errors="replace")

    if not markdown_url:
        return ""

    try:
        response = requests.get(markdown_url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"WARNING: could not download {pdf_name}: {exc}")
        return ""

    output_path.write_text(response.text, encoding="utf-8")
    return response.text


def repair_mineru_usage(records: list[dict[str, Any]]) -> tuple[int, int, int]:
    name_index = build_name_index(records)

    for record in records:
        metadata = record.setdefault("alignment_metadata", {})
        metadata["mineru_usage"] = []

        # Drop stale paper-derived text snippets. The script adds back only
        # snippets backed by the current parsing log and local markdown file.
        descriptions = []
        for desc in record.get("text_descriptions", []):
            source = desc.get("source") or {}
            if source.get("mineru_parsed"):
                continue
            descriptions.append(desc)
        record["text_descriptions"] = descriptions

    if not PARSING_LOG.exists():
        print(f"WARNING: parsing log not found: {PARSING_LOG}")
        return 0, 0, 0

    log = json.loads(PARSING_LOG.read_text(encoding="utf-8"))
    results = log.get("results", {})
    successful_papers = 0
    failed_papers = 0
    updated_records: set[str] = set()

    for pdf_name, result in sorted(results.items()):
        markdown_url = result.get("markdown_url")
        content_length = int(result.get("content_length") or 0)
        task_id = result.get("task_id")
        if not markdown_url or content_length <= 0:
            failed_papers += 1
            continue

        successful_papers += 1
        markdown = download_markdown(pdf_name, markdown_url)
        output_path = f"data/raw/parsed_mineru_api/{pdf_name.replace('.pdf', '.md')}"

        seen_records_for_paper: set[str] = set()
        for molecule_name in PAPER_MOLECULE_MAP.get(pdf_name, []):
            record = name_index.get(molecule_name.casefold())
            if record is None:
                print(f"WARNING: molecule not found for parsed paper: {molecule_name}")
                continue
            if record["record_id"] in seen_records_for_paper:
                continue
            seen_records_for_paper.add(record["record_id"])

            metadata = record.setdefault("alignment_metadata", {})
            usage = metadata.setdefault("mineru_usage", [])
            usage.append({
                "tool": "MinerU Agent API",
                "task": (
                    f"Parsed {pdf_name} with MinerU Agent API and aligned the "
                    f"structured Markdown output to {record['names']['common_name']}."
                ),
                "input": f"data/raw/papers/{pdf_name}",
                "output": output_path,
                "task_id": task_id,
                "markdown_url": markdown_url,
                "content_length": content_length,
                "detail": (
                    f"task_id={task_id}; markdown_url={markdown_url}; "
                    f"content_length={content_length}"
                ),
            })

            if markdown:
                snippet = extract_relevant_text(markdown, molecule_name)
                if snippet:
                    reference = f"doi:{PAPER_DOI_MAP.get(pdf_name, pdf_name)}"
                    already_exists = any(
                        (desc.get("source") or {}).get("reference") == reference
                        for desc in record.get("text_descriptions", [])
                    )
                    if not already_exists:
                        record.setdefault("text_descriptions", []).append({
                            "type": "general_description",
                            "content": snippet,
                            "source": {
                                "type": "paper",
                                "reference": reference,
                                "section": "MinerU Agent API Markdown excerpt",
                                "mineru_parsed": True,
                            },
                            "language": "en",
                        })

            updated_records.add(record["record_id"])

    return successful_papers, failed_papers, len(updated_records)


def rebuild_samples(records: list[dict[str, Any]]) -> int:
    record_by_id = {record["record_id"]: record for record in records}
    samples = [record_by_id[rid] for rid in SAMPLE_RECORD_IDS if rid in record_by_id]

    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    (SAMPLES_DIR / "sample_dataset.jsonl").write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in samples),
        encoding="utf-8",
    )
    (SAMPLES_DIR / "sample_dataset.json").write_text(
        json.dumps(samples, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return len(samples)


def main() -> None:
    records = load_records()

    smiles_fixed = 0
    properties_fixed = 0
    generated_2d = 0
    generated_3d = 0
    failed_3d = 0
    for record in records:
        smi_count, prop_count = repair_smiles_and_properties(record)
        smiles_fixed += smi_count
        properties_fixed += prop_count
        img_count, sdf_count, sdf_failed = ensure_structure_assets(record)
        generated_2d += img_count
        generated_3d += sdf_count
        failed_3d += sdf_failed

    successful_papers, failed_papers, mineru_records = repair_mineru_usage(records)
    sample_count = rebuild_samples(records)
    write_records(records)

    print("Dataset integrity repair complete")
    print(f"  Records: {len(records)}")
    print(f"  SMILES fields fixed: {smiles_fixed}")
    print(f"  Property fields fixed: {properties_fixed}")
    print(f"  2D images generated: {generated_2d}")
    print(f"  3D conformers generated: {generated_3d}")
    print(f"  3D conformers failed and unset: {failed_3d}")
    print(f"  MinerU Agent API papers: {successful_papers} success, {failed_papers} failed")
    print(f"  Records with real MinerU evidence: {mineru_records}")
    print(f"  Sample records rebuilt: {sample_count}")


if __name__ == "__main__":
    main()
