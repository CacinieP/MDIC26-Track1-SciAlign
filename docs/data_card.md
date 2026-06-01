# MolAlign — Data Card

> 分子跨模态对齐数据集 (Sci-Align Track 1) · 820 条记录 · 35 类别

| 字段 | 值 |
|------|----|
| **Dataset Name** | MolAlign (MDIC26-Track1-SciAlign) |
| **Version** | 1.0.0 (release: 2026-05-31) |
| **License** | CC-BY-4.0 (data) / MIT (code) |
| **Language** | English + Chinese (bilingual scientific text) |
| **Domain** | Pharmaceutical chemistry, molecular pharmacology |
| **Records** | 820 |
| **Categories** | 35 (NSAID, Antibiotic, Anticancer, Natural Product, …) |
| **Format** | JSONL (primary) + JSON |
| **Schema** | [`src/schema.py`](../src/schema.py) (JSON Schema draft-07) |
| **Provenance** | [`data/processed/provenance.tsv`](../data/processed/provenance.tsv) |

## What is in this dataset?

MolAlign is a **cross-modal alignment dataset for molecular entities in pharmaceutical chemistry**. Each record centers on a single molecule (identified by PubChem CID) and bundles five modality channels:

1. **2D molecular structure** (PNG image, RDKit-generated, 512×512)
2. **3D molecular conformer** (SDF, ETKDGv3 + MMFF optimized) — 799/820 records
3. **Chemical identifiers** (canonical SMILES, isomeric SMILES, InChI, InChIKey)
4. **Physicochemical & drug-likeness properties** (MW, LogP, TPSA, HBD/HBA, Lipinski violations, QED, synthetic accessibility)
5. **Scientific text** (synthesis, mechanism, pharmacokinetics, clinical use, safety, SAR) in both English and Chinese
6. **Entity relations** (subject–relation–object triples linking molecules to targets, substructures, metabolites)
7. **Paper-derived evidence** for 33 records (extracted from scientific papers)

## What is the data for?

| Use case | Fit |
|----------|-----|
| Training a multimodal molecular LLM (structure ↔ text ↔ property alignment) | ✅ Primary |
| Retrieval-augmented drug discovery (molecule ↔ paper) | ✅ Tier A/B records |
| Property prediction from SMILES | ✅ All 820 records |
| Pharmacovigilance / drug-target knowledge graph | ✅ Tier A/B records |
| Benchmarking scientific text generation | ✅ Tier A/B records |
| Clinical decision support (e.g. drug interaction prediction) | ⚠️ Tier A only (9 records); broader coverage pending |

## Who is this for?

- **NLP researchers** working on scientific document understanding
- **Cheminformatics / AI4Science teams** building molecular foundation models
- **Knowledge graph engineers** constructing pharmacology ontologies
- **NOT suitable for**: clinical-grade drug recommendation (insufficient experimental data depth), personalized medicine (no patient-level data)

## Composition

| Field | Coverage |
|-------|----------|
| 2D structure image | 820 / 820 (100%) |
| 3D conformer | 799 / 820 (97.4%) — 21 records fail RDKit ETKDG embedding (large peptides) |
| English text description | 820 / 820 (100%) |
| Chinese text description | 820 / 820 (100%) |
| Entity relations | 820 / 820 (100%), exactly 2.0 per record (template) |
| Paper-derived image | 33 / 820 (4.0%) |
| Experimental bioactivity | 30 / 820 (3.7%) — 40 curated IC50 entries |
| Real MinerU Agent API evidence | 9 / 820 (1.1%) — 10 successful tasks, 597,454 chars |

## Evidence Quality Tiers

Per-record provenance in [`provenance.tsv`](../data/processed/provenance.tsv). Tier assignment:

- **Tier A** (9 records): Has real MinerU Agent API evidence with `task_id` + `markdown_url` + `content_length` traceability. Ibuprofen, Paclitaxel, Doxorubicin, Metformin, Morphine, Curcumin, Dopamine, Caffeine, Acetaminophen.
- **Tier B** (64 records): Has at least one of: curated literature relations (CID in `KNOWN_RELATIONS`), paper image, bioactivity, or curated Chinese description. Most "headline" drugs (Aspirin, Tamoxifen, etc.) are here.
- **Tier C** (747 records): Template-based enrichment only (category-target relations, auto-generated Chinese). Long-tail molecules in the dataset.

**Why this matters:** A model trained only on Tier C records is essentially learning a template. Tier A/B records are the meaningful training signal.

## Data Sources

| Source | Use | Coverage |
|--------|-----|----------|
| **PubChem REST API** | Canonical SMILES, InChI, synonyms, descriptions, properties | 820 records |
| **RDKit** | SMILES canonicalization, 2D depiction, 3D conformer (ETKDGv3 + MMFF), physicochemical properties | 820 records |
| **MinerU Agent API** | Paper PDF parsing → Markdown | 12 tasks, 10 success, 2 fail (sizes >10MB or IP rate-limited) |
| **Curated literature** | Drug-target relations, bioactivity (IC50), Chinese descriptions | 64 + 30 records |
| **Category templates** | Fallback relations, ZH descriptions for long-tail | 747 records |

**Honest disclosure:** The dataset is structurally complete but evidence-thin. Of 820 records, only 9 (1.1%) carry real MinerU paper-parse evidence. The remainder relies on PubChem + RDKit + curated hand-coding. This is an honest starting point; broader MinerU coverage is the natural next step.

## Collection Process

```
PubChem CID list (820 entries) 
    → PubChem REST API (SMILES, InChI, properties, descriptions)
    → RDKit (canonical SMILES, 2D image, 3D conformer, computed properties)
    → KNOWN_RELATIONS lookup (curated drug-target relations for ~50 CIDs)
    → Category-template relations (auto-generated for remaining CIDs)
    → Chinese descriptions (curated for ~50 CIDs, template for the rest)
    → 12 paper PDFs submitted to MinerU Agent API
        → 10 success: task_id + markdown_url saved; only molecule-mapped records receive evidence
        → 2 fail: fluoxetine_ijms.pdf, vitamins_pharmaceuticals.pdf (sizes within limit, returned markdown_url=null)
    → 5 paper PDFs (subset of above) processed by PyMuPDF for paper-image extraction
    → 33 records get structure_paper (image_path → images/paper/MOL-XXXXXX_paper_N.{png,jpeg})
```

See [`docs/technical_report.md`](technical_report.md) for the full pipeline.

## Known Limitations

1. **Schema drift**: `structure_paper` field in actual data uses `images`/`source`/`paper_count` keys, while `src/schema.py` declares `image_path`/`source_paper`/`page_number`/`figure_label`. Validator currently does not flag this (see audit report).
2. **Template uniformity**: 747/820 records have identical "category-target + substructure" relation template, providing weak learning signal for those records.
3. **No negative samples**: All entities are positive drug examples. No decoy/false-relation examples.
4. **No pharmacokinetic curves**: Only point IC50 values; no time-series, no dose-response curves.
5. **English descriptions**: Sourced from PubChem text + MinerU; not manually edited for consistency.

## Updates & Maintenance

- **Last updated**: 2026-05-31 (commit `fc0973b`)
- **Schema version**: declared in `src/schema.py`; actual data uses evolved schema (see audit report)
- **Next planned updates**:
  - Expand MinerU paper coverage to 50+ records (free Agent API tier)
  - Reconcile `structure_paper` schema with actual data
  - Add more drug-target relations via ChEMBL/DrugBank lookup

## Citation

```bibtex
@misc{molalign2026,
  title={MolAlign: A Cross-Modal Alignment Dataset for Pharmaceutical Molecules},
  author={LinguistWantsTech},
  year={2026},
  howpublished={MDIC26 AGI4S Track 1 — Sci-Align},
  url={https://github.com/CacinieP/MDIC26-Track1-SciAlign}
}
```

## Contact

- GitHub: https://github.com/CacinieP/MDIC26-Track1-SciAlign
- Author: LinguistWantsTech <cacinie@gmail.com>
