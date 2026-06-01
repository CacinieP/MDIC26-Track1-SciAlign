# MolAlign — Datasheet for Datasets

Following Gebru et al. (2021) "Datasheets for Datasets" — a structured documentation of motivation, composition, collection, preprocessing, uses, distribution, and maintenance.

---

## Motivation

### For what purpose was the dataset created?

MolAlign was created to provide a **cross-modal alignment dataset for pharmaceutical molecules**, supporting training of multimodal foundation models in chemistry and pharmacology. The dataset explicitly links five modality channels (molecular structure, identifiers, properties, scientific text, and entity relations) around each molecule entity.

The dataset is a Track 1 (Sci-Align) submission to the **MDIC26 语料筑基·AGI4S** competition (deadline 2026-05-31), themed "frontier corpus construction for AGI for Science."

### Who created the dataset?

- **Author**: LinguistWantsTech (cacinie@gmail.com)
- **Created using**: Claude Code (claude-opus-4-8) for pipeline scaffolding, data enrichment scripting, and documentation
- **Build date**: 2026-05-15 to 2026-05-31

### Who funded the creation?

Self-funded. No external sponsorship.

### Any other comments?

None.

---

## Composition

### What do the instances that comprise the dataset represent?

Each instance is a **single molecule entity** (a chemical compound), uniquely identified by its PubChem Compound ID (CID). The 820 molecules span 35 pharmacological / chemical categories.

### How many instances are there in total?

**820 records**.

### What data does each instance consist of?

Per-record fields (see [`src/schema.py`](../src/schema.py) for full schema):

| Field | Type | Description |
|-------|------|-------------|
| `record_id` | string | `MOL-NNNNNN` (6-digit zero-padded) |
| `molecule_id.pubchem_cid` | integer | PubChem Compound ID |
| `molecule_id.chembl_id` | string\|null | ChEMBL ID (currently null for all) |
| `molecule_id.drugbank_id` | string\|null | DrugBank ID (currently null) |
| `molecule_id.cas_number` | string\|null | CAS Registry Number (currently null) |
| `smiles.canonical` | string | RDKit canonical SMILES |
| `smiles.isomeric` | string\|null | SMILES with stereochemistry |
| `smiles.inchi` | string | InChI identifier |
| `smiles.inchikey` | string | InChIKey hash |
| `names.iupac_name` | string\|null | IUPAC systematic name |
| `names.common_name` | string\|null | Common drug/chemical name |
| `names.synonyms` | array of string | Up to 20 synonyms |
| `modalities.structure_2d` | object | 2D PNG image, RDKit-generated, 512×512 |
| `modalities.structure_paper` | object\|null | Paper-extracted image (33 records) |
| `modalities.structure_3d` | object\|null | 3D SDF conformer (799 records) |
| `modalities.table_data` | object\|null | (currently null) |
| `properties.physicochemical` | object | MW, ExactMass, LogP, TPSA, HBD, HBA, rotatable bonds, heavy atoms, ring count, formal charge |
| `properties.drug_likeness` | object\|null | Lipinski violations, synthetic accessibility, QED |
| `properties.experimental` | object\|null | Bioactivity (IC50) for 30 records |
| `text_descriptions[]` | array | Scientific descriptions, types: synthesis / bioactivity / mechanism_of_action / pharmacokinetics / clinical_use / safety / general_description / structure_activity_relationship |
| `entity_relations[]` | array | Subject–relation–object triples, types: inhibits / activates / binds_to / metabolized_to / has_substructure / derivative_of / targets / synthesized_from / etc. |
| `alignment_metadata.alignment_confidence` | number | 0–1 |
| `alignment_metadata.validation_status` | string | automated_pass / manual_verified / flagged_for_review |
| `alignment_metadata.mineru_usage[]` | array | MinerU tool usage records (with task_id for real evidence) |
| `alignment_metadata.created_at` | string | ISO 8601 timestamp |
| `alignment_metadata.updated_at` | string | ISO 8601 timestamp |
| `alignment_metadata.version` | string | Dataset version |
| `category` | string | One of 35 categories |

### Is there a label or target associated with each instance?

Not in the supervised-learning sense. The dataset is an **alignment corpus** — the implicit "label" is the cross-modal correspondence between structure, properties, text, and relations around the same entity.

### Is any information missing from individual instances?

Yes. See **Schema Drift** in the audit report:

- 33 records' `structure_paper` field has `images`/`source`/`paper_count` instead of the schema's `image_path`/`source_paper`/`page_number`/`figure_label`
- 30 records' `properties.experimental.bioactivity[]` entries use `source` instead of `source_paper`

### Are relationships between individual instances made explicit?

Yes, indirectly:
- All instances share a common `category` field (35 classes)
- `entity_relations` may link instances of related molecules (e.g., Metabolite → Parent drug) within the same record
- No explicit cross-record links (e.g., no shared target protein → molecule index)

### Are there recommended data splits?

No. The dataset is a corpus, not a labeled training set. For ML use, splitting should be done per-task (e.g., 80/10/10 for property prediction, with stratification on `category`).

### Are there any errors, sources of noise, or redundancies?

- **3D conformer failures**: 21 records (large peptides / macrocycles) where RDKit ETKDGv3 embedding failed; `structure_3d` is null
- **SMILES canonicalization**: All SMILES passed through RDKit `MolToSmiles(mol)`; no stereochemistry loss expected for achiral molecules
- **MW discrepancy**: PubChem returns `MolecularWeight` (average) and RDKit returns `Descriptors.MolWt` (average) — these match to within 0.5 g/mol typically
- **No deduplication**: Records with the same InChIKey (different CID, e.g. salt forms) are not deduplicated

### Is the dataset self-contained, or does it link to or otherwise rely on external resources?

The dataset is **partially self-contained**:
- 2D PNG images and 3D SDF files are bundled in `data/processed/images/2d/` and `data/processed/models/3d/`
- Paper-derived images in `data/processed/images/paper/`
- Source paper PDFs in `data/raw/papers/`
- Parsed MinerU Markdown in `data/raw/parsed_mineru_api/`
- **External dependency**: PubChem REST API (for re-fetching canonical properties if regenerating)

### Does the dataset contain data that might be considered confidential?

No. All molecules are public (PubChem-indexed). All source papers are open-access (Frontiers, MDPI, IJMS, etc.). No patient data, no proprietary chemistry.

### Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?

No. The dataset is purely chemical/biological. It contains no human subjects, no PII, no distressing imagery.

---

## Collection Process

### How was the data associated with each instance acquired?

Three data acquisition channels:

1. **PubChem REST API** (`scripts/build_full_dataset.py`)
   - Compound properties endpoint → canonical SMILES, InChI, InChIKey, MW, XLogP, TPSA, complexity, heavy atoms, HBD/HBA, rotatable bonds, formal charge
   - Synonyms endpoint → up to 20 synonym strings
   - Description endpoint → free-text descriptions

2. **RDKit** (Python library)
   - `Chem.MolToSmiles(mol)` for canonicalization
   - `Chem.Draw.MolToImage(mol, size=(512, 512))` for 2D depiction
   - `AllChem.EmbedMolecule(mol, AllChem.ETKDGv3())` + `MMFFOptimizeMolecule` for 3D
   - `Descriptors.MolWt`, `LogP`, `TPSA`, `NumHDonors`, `NumHAcceptors`, `RingCount`, etc. for property calculation
   - `QED.qed(mol)` for drug-likeness score
   - `sascore.calculateScore(mol)` for synthetic accessibility

3. **MinerU Agent API** (`scripts/mineru_agent_parse.py`)
   - Free tier endpoint: `https://mineru.net/api/v1/agent/parse/file`
   - 12 PDF submissions; 10 success, 2 fail (returned `markdown_url=null`)
   - Each success: stores `task_id`, `markdown_url`, `content_length` for traceability

### What mechanisms or procedures were used to collect the data?

- **CID list curation**: Hand-curated list of 820 PubChem CIDs across 35 drug/chemical categories (no scraping; based on WHO Essential Medicines, DrugBank, and ChEMBL top-100 lists)
- **Rate limiting**: 200ms delay between PubChem API calls
- **RDKit determinism**: All RDKit operations are deterministic given the same RDKit version
- **MinerU manual gating**: 1s delay between MinerU submissions, 5s polling interval

### If the dataset is a sample from a larger set, what was the sampling strategy?

The 820 CIDs are a **convenience sample** of well-known pharmaceutical compounds. Coverage is non-uniform:
- **Headline drugs** (Aspirin, Ibuprofen, Paclitaxel, etc.): Full Tier A/B treatment
- **Long-tail compounds** (rare amino acids, diagnostic agents): Tier C template-only

The dataset is **not** representative of "all pharmaceutical compounds." It is a curated subset chosen for educational and benchmarking purposes.

### Who was involved in the data collection process?

Single author (LinguistWantsTech) with assistance from Claude Code for pipeline scripting.

### Over what timeframe was the data collected?

2026-05-15 to 2026-05-31.

### Were any ethical review processes conducted?

Not applicable — the data is public domain chemistry and open-access papers.

---

## Preprocessing / Cleaning / Labeling

### Was any preprocessing/cleaning/labeling of the data done?

- **SMILES canonicalization**: All SMILES pass through `Chem.MolToSmiles(mol)`
- **InChI computation**: `Chem.MolToInchi(mol)` and `Chem.MolToInchiKey(mol)`
- **2D image rendering**: Fixed 512×512 PNG, white background, default RDKit styling
- **3D conformer generation**: ETKDGv3 with MMFF optimization; failures (21 records) left as null
- **Relation source attribution**: Each relation tagged with `evidence` field if from curated source
- **ZH description templating**: For CIDs without curated Chinese description, auto-generated template applied
- **MinerU usage tagging**: Only records with verifiable `task_id` + `markdown_url` get `mineru_usage` evidence

### Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data?

- Raw PubChem API responses: **not** saved (only properties used)
- Source PDFs: **saved** in `data/raw/papers/`
- MinerU parsed Markdown: **saved** in `data/raw/parsed_mineru_api/`
- PyMuPDF-extracted image dumps: **saved** in `data/raw/parsed/`
- Intermediate MinerU-style JSON: **saved** in `data/raw/parsed/{pdf_name}/mineru_parsed.json`

### Is the software that was used to preprocess/clean/label the data available?

Yes, all scripts in [`scripts/`](../scripts/) and [`src/`](../src/).

---

## Uses

### Has the dataset been used for any tasks already?

- Internal benchmarking of multimodal LLM fine-tuning
- Background dataset for Track 2 (Evo-Eval) and Track 3 (Edu) in the same competition

### Is there a repository that links to any or all papers or systems that use the dataset?

Not yet. This is the first release.

### What (other) tasks could the dataset be used for?

- **Drug-target interaction prediction** (using relations)
- **Cross-modal retrieval** (text → structure, structure → property)
- **Knowledge graph completion** (predicting missing edges)
- **Scientific document generation** (structure + property → paper text)
- **Few-shot learning** for under-represented drug classes (Tier C records)

### Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

Yes:
- **Tier C records (747/820)** are template-based and may bias models toward generic language
- **No negative samples** — models trained on this should not be used for "this drug does NOT inhibit X" claims
- **English-Chinese parallel text** is unaligned at the sentence level (different sources, not translations)
- **Paper images** in Tier A/B may carry copyright of the source paper — redistribution should follow CC-BY-4.0 of the dataset plus fair-use for the underlying paper

### Are there tasks for which the dataset should not be used?

- **Clinical decision support** without human review (insufficient safety data depth)
- **Regulatory submission** (not validated for that use)
- **Adverse drug reaction prediction** (no negative samples, no frequency data)

---

## Distribution

### Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?

Yes, via GitHub: https://github.com/CacinieP/MDIC26-Track1-SciAlign

### How will the dataset will be distributed?

- **Git repository**: Source code, schema, scripts, raw inputs
- **Git LFS or releases**: 820 PNGs (~30MB) + 799 SDFs (~50MB) + 35 paper images
- **Total size**: ~150MB (excluding 13 source PDFs which are themselves open-access)

### When will the dataset be distributed?

Released 2026-05-31. Available now.

### Will the dataset be distributed under a copyright license, and/or under terms of use?

- **Data**: CC-BY-4.0 (attribution required)
- **Code**: MIT License

### Have any third parties imposed restrictions on the data?

No.

### Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?

No. No controlled substances (Schedule I/II), no biological agents, no weapons-related chemistry.

---

## Maintenance

### Who will be supporting/hosting/maintaining the dataset?

Author (LinguistWantsTech) on GitHub.

### How can the owner/curator of the dataset be contacted?

- GitHub issues: https://github.com/CacinieP/MDIC26-Track1-SciAlign/issues
- Email: cacinie@gmail.com

### Is there an erratum?

Yes — see the audit report ([`docs/AUDIT_REPORT.md`](AUDIT_REPORT.md), local-only, not committed):

1. `structure_paper` schema drift (33 records)
2. `bioactivity.source` vs `source_paper` field name (30 records)
3. `DATASET_SCHEMA` defined but never invoked

### Will the dataset be updated?

Yes. Planned updates:
- **v1.1**: Reconcile `structure_paper` schema; fix `bioactivity` field name
- **v1.2**: Expand MinerU paper coverage from 9 → 50+ records
- **v2.0**: Add ChEMBL/DrugBank cross-references; add more curated bioactivity

### If the dataset becomes obsolete, will it be deprecated?

Will be marked deprecated in README; not deleted (CC-BY-4.0 keeps it accessible).

### Will older versions of the dataset continue to be supported/hosted/maintained?

Yes — git history + GitHub releases.

### If others want to extend/augment/built-upon/contribute to the dataset, is there a mechanism for them to do so?

- GitHub pull requests welcome
- Issue tracker for bug reports
- See `docs/technical_report.md` for extension points

---

## References

- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). "Datasheets for Datasets." *Communications of the ACM*, 64(12), 86-92.
- RDKit: Open-Source Cheminformatics. https://www.rdkit.org
- PubChem: Kim, S. et al. (2025). "PubChem 2025 update." *Nucleic Acids Research*.
- MinerU: OpenDataLab. https://github.com/opendatalab/MinerU
- Lipinski, C. A. et al. (1997). "Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings." *Adv. Drug Deliv. Rev.* 23, 3-25.
