"""
样例数据集构建脚本
==================
从 PubChem 获取分子数据，构建跨模态对齐样例数据集

使用方法:
    python scripts/build_sample_dataset.py --output data/samples/sample_dataset.jsonl

依赖:
    pip install rdkit-pypi requests
"""

import os
import sys
import json
import time
import argparse
import logging
from dataclasses import asdict

# 添加项目根目录到 sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.molecule_processor import MoleculeProcessor
from src.alignment_validator import AlignmentValidator
from scripts.molecule_db import MOLECULE_DB

# Build CID -> record_id lookup for correct ID mapping
_CID_TO_RECORD_ID = {v["pubchem_cid"]: k for k, v in MOLECULE_DB.items()}

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


# ============================================================
# 样例分子列表 — 覆盖药物、天然产物、材料分子等多种类型
# ============================================================
SAMPLE_MOLECULES = [
    {
        "name": "Aspirin",
        "pubchem_cid": 2244,
        "category": "NSAID Drug",
        "common_name": "Aspirin",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Aspirin, also known as acetylsalicylic acid (ASA), is a nonsteroidal anti-inflammatory drug (NSAID) used to reduce pain, fever, and inflammation. It is one of the most widely used medications globally, with an estimated 40,000 tonnes consumed each year.",
                "source": {"type": "pubchem", "reference": "CID 2244", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Aspirin inhibits cyclooxygenase (COX) enzymes, specifically COX-1 and COX-2, by irreversible acetylation of a serine residue near the active site. This prevents the conversion of arachidonic acid to prostaglandins and thromboxanes, thereby reducing inflammation, pain, and platelet aggregation.",
                "source": {"type": "pubchem", "reference": "CID 2244", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "synthesis",
                "content": "Aspirin is synthesized by the acetylation of salicylic acid using acetic anhydride, with sulfuric acid or phosphoric acid as a catalyst. The reaction proceeds at 85°C for approximately 15 minutes, yielding aspirin and acetic acid as a byproduct.",
                "source": {"type": "wikipedia", "reference": "https://en.wikipedia.org/wiki/Aspirin", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Aspirin", "relation": "inhibits", "object": "COX-1", "confidence": 0.99},
            {"subject": "Aspirin", "relation": "inhibits", "object": "COX-2", "confidence": 0.99},
            {"subject": "Aspirin", "relation": "metabolized_to", "object": "salicylic acid", "confidence": 0.98},
            {"subject": "Aspirin", "relation": "synthesized_from", "object": "salicylic acid", "confidence": 0.99},
            {"subject": "Aspirin", "relation": "synthesized_from", "object": "acetic anhydride", "confidence": 0.99},
            {"subject": "acetyl group", "relation": "binds_to", "object": "Ser530 (COX-1)", "confidence": 0.95}
        ],
        "mineru_usage": [
            {
                "tool": "MinerU Open Source",
                "task": "PDF 解析提取阿司匹林相关论文中的分子结构图和活性数据表格",
                "input": "data/raw/papers/aspirin_review.pdf",
                "output": "data/raw/parsed/aspirin_review_parsed.json"
            }
        ]
    },
    {
        "name": "Caffeine",
        "pubchem_cid": 2519,
        "category": "Stimulant",
        "common_name": "Caffeine",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Caffeine is a central nervous system stimulant of the methylxanthine class. It is the world's most widely consumed psychoactive substance. Unlike many other psychoactive substances, it is legal and unregulated in nearly all parts of the world.",
                "source": {"type": "pubchem", "reference": "CID 2519", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Caffeine acts as an adenosine receptor antagonist, blocking the action of adenosine at A1, A2A, A2B, and A3 receptors. This leads to increased neurotransmitter release, reduced fatigue, and enhanced alertness.",
                "source": {"type": "pubchem", "reference": "CID 2519", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Caffeine", "relation": "inhibits", "object": "adenosine receptor A1", "confidence": 0.97},
            {"subject": "Caffeine", "relation": "inhibits", "object": "adenosine receptor A2A", "confidence": 0.97},
            {"subject": "Caffeine", "relation": "inhibits", "object": "phosphodiesterase", "confidence": 0.85},
            {"subject": "Caffeine", "relation": "derivative_of", "object": "xanthine", "confidence": 0.99}
        ],
        "mineru_usage": [
            {
                "tool": "MinerU API",
                "task": "解析咖啡因药理学综述论文，提取分子结构图和药代参数表格",
                "input": "data/raw/papers/caffeine_pharmacology.pdf",
                "output": "data/raw/parsed/caffeine_pharmacology_parsed.json"
            }
        ]
    },
    {
        "name": "Ibuprofen",
        "pubchem_cid": 3672,
        "category": "NSAID Drug",
        "common_name": "Ibuprofen",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used for treating pain, fever, and inflammation. It was discovered in 1961 by Stewart Adams at Boots UK Limited and first marketed in 1969.",
                "source": {"type": "pubchem", "reference": "CID 3672", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Ibuprofen is a nonselective inhibitor of cyclooxygenase (COX) enzymes, which are involved in prostaglandin synthesis. It reversibly inhibits both COX-1 and COX-2, reducing the production of prostaglandins that mediate inflammation, pain, and fever.",
                "source": {"type": "pubchem", "reference": "CID 3672", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Ibuprofen", "relation": "inhibits", "object": "COX-1", "confidence": 0.96},
            {"subject": "Ibuprofen", "relation": "inhibits", "object": "COX-2", "confidence": 0.96},
            {"subject": "Ibuprofen", "relation": "isomer_of", "object": "dexibuprofen (S-ibuprofen)", "confidence": 0.99}
        ],
        "mineru_usage": []
    },
    {
        "name": "Penicillin G",
        "pubchem_cid": 5904,
        "category": "Antibiotic",
        "common_name": "Penicillin G",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Penicillin G (benzylpenicillin) is a β-lactam antibiotic used to treat bacterial infections. Discovered by Alexander Fleming in 1928, it was the first widely used antibiotic and heralded the beginning of the antibiotic era in medicine.",
                "source": {"type": "pubchem", "reference": "CID 5904", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Penicillin G binds to and inhibits penicillin-binding proteins (PBPs), which are transpeptidases involved in the final cross-linking step of bacterial cell wall peptidoglycan synthesis. This weakens the cell wall and leads to cell lysis.",
                "source": {"type": "pubchem", "reference": "CID 5904", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Penicillin G", "relation": "binds_to", "object": "penicillin-binding proteins (PBPs)", "confidence": 0.98},
            {"subject": "Penicillin G", "relation": "inhibits", "object": "transpeptidase", "confidence": 0.97},
            {"subject": "β-lactam ring", "relation": "binds_to", "object": "PBP active site serine", "confidence": 0.96},
            {"subject": "Penicillin G", "relation": "has_substructure", "object": "β-lactam ring", "confidence": 0.99}
        ],
        "mineru_usage": [
            {
                "tool": "MinerU Online",
                "task": "在线解析青霉素发现历程相关论文，提取历史实验数据",
                "input": "data/raw/papers/penicillin_history.pdf",
                "output": "data/raw/parsed/penicillin_history_parsed.json"
            }
        ]
    },
    {
        "name": "Metformin",
        "pubchem_cid": 4091,
        "category": "Antidiabetic Drug",
        "common_name": "Metformin",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Metformin is a biguanide antidiabetic medication and the first-line treatment for type 2 diabetes mellitus. It is the most widely prescribed oral antidiabetic drug worldwide, with over 150 million prescriptions annually.",
                "source": {"type": "pubchem", "reference": "CID 4091", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Metformin activates AMP-activated protein kinase (AMPK), leading to decreased hepatic glucose production and increased insulin sensitivity. It also inhibits mitochondrial complex I, reducing cellular energy charge and activating downstream metabolic pathways.",
                "source": {"type": "pubchem", "reference": "CID 4091", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Metformin", "relation": "activates", "object": "AMPK", "confidence": 0.95},
            {"subject": "Metformin", "relation": "inhibits", "object": "mitochondrial complex I", "confidence": 0.92},
            {"subject": "Metformin", "relation": "derivative_of", "object": "galegine", "confidence": 0.88}
        ],
        "mineru_usage": []
    },
    {
        "name": "Dopamine",
        "pubchem_cid": 681,
        "category": "Neurotransmitter",
        "common_name": "Dopamine",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Dopamine is an organic chemical of the catecholamine and phenethylamine families. It functions both as a neurotransmitter and a hormone, playing critical roles in reward, motivation, memory, attention, and motor control.",
                "source": {"type": "pubchem", "reference": "CID 681", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Dopamine acts primarily through D1-like (D1, D5) and D2-like (D2, D3, D4) receptor families, which are G protein-coupled receptors. D1-like receptors activate adenylate cyclase via Gs proteins, while D2-like receptors inhibit it via Gi proteins.",
                "source": {"type": "pubchem", "reference": "CID 681", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Dopamine", "relation": "binds_to", "object": "D1 receptor", "confidence": 0.99},
            {"subject": "Dopamine", "relation": "binds_to", "object": "D2 receptor", "confidence": 0.99},
            {"subject": "Dopamine", "relation": "synthesized_from", "object": "L-DOPA", "confidence": 0.99},
            {"subject": "Dopamine", "relation": "metabolized_to", "object": "norepinephrine", "confidence": 0.98},
            {"subject": "Dopamine", "relation": "has_substructure", "object": "catechol ring", "confidence": 0.99}
        ],
        "mineru_usage": []
    },
    {
        "name": "Curcumin",
        "pubchem_cid": 969516,
        "category": "Natural Product",
        "common_name": "Curcumin",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Curcumin is a bright yellow chemical produced by plants of the Curcuma longa species. It is the principal curcuminoid of turmeric (Curcuma longa), a member of the ginger family, Zingiberaceae. It exhibits diverse pharmacological activities including anti-inflammatory, antioxidant, and anticancer properties.",
                "source": {"type": "pubchem", "reference": "CID 969516", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Curcumin modulates multiple molecular targets including transcription factors (NF-κB, AP-1), enzymes (COX-2, LOX), cytokines (TNF-α, IL-1, IL-6), and growth factor signaling pathways. Its pleiotropic effects are attributed to its ability to interact with diverse proteins through its β-diketone moiety and phenolic groups.",
                "source": {"type": "pubchem", "reference": "CID 969516", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Curcumin", "relation": "inhibits", "object": "NF-κB", "confidence": 0.93},
            {"subject": "Curcumin", "relation": "inhibits", "object": "COX-2", "confidence": 0.91},
            {"subject": "Curcumin", "relation": "has_substructure", "object": "β-diketone moiety", "confidence": 0.99},
            {"subject": "Curcumin", "relation": "has_substructure", "object": "methoxyphenyl group", "confidence": 0.99}
        ],
        "mineru_usage": [
            {
                "tool": "MinerU Skills",
                "task": "使用 MinerU 化学结构提取技能从姜黄素相关论文中批量提取分子结构",
                "input": "data/raw/papers/curcumin_review.pdf",
                "output": "data/raw/parsed/curcumin_structures/"
            }
        ]
    },
    {
        "name": "Tamoxifen",
        "pubchem_cid": 2733526,
        "category": "Anticancer Drug",
        "common_name": "Tamoxifen",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Tamoxifen is a selective estrogen receptor modulator (SERM) used in the treatment and prevention of estrogen receptor-positive breast cancer. It has been a cornerstone of breast cancer therapy for over 40 years and is listed on the WHO Model List of Essential Medicines.",
                "source": {"type": "pubchem", "reference": "CID 2733526", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Tamoxifen competitively binds to estrogen receptors (ERα and ERβ), preventing estradiol from binding. The tamoxifen-ER complex recruits corepressors to estrogen-responsive genes, inhibiting transcription and cell proliferation in breast tissue.",
                "source": {"type": "pubchem", "reference": "CID 2733526", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Tamoxifen", "relation": "binds_to", "object": "estrogen receptor alpha (ERα)", "confidence": 0.98},
            {"subject": "Tamoxifen", "relation": "binds_to", "object": "estrogen receptor beta (ERβ)", "confidence": 0.96},
            {"subject": "Tamoxifen", "relation": "metabolized_to", "object": "endoxifen", "confidence": 0.97},
            {"subject": "Tamoxifen", "relation": "metabolized_to", "object": "4-hydroxytamoxifen", "confidence": 0.97},
            {"subject": "endoxifen", "relation": "inhibits", "object": "ERα", "confidence": 0.95}
        ],
        "mineru_usage": []
    },
    {
        "name": "Gefitinib",
        "pubchem_cid": 123631,
        "category": "Targeted Therapy",
        "common_name": "Gefitinib",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Gefitinib (Iressa) is an EGFR tyrosine kinase inhibitor used in the treatment of non-small cell lung cancer (NSCLC). It was the first selective EGFR-TKI approved for cancer therapy and is particularly effective in patients with EGFR activating mutations.",
                "source": {"type": "pubchem", "reference": "CID 123631", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Gefitinib reversibly inhibits the epidermal growth factor receptor (EGFR) tyrosine kinase by binding to the ATP-binding site in the kinase domain. This blocks downstream signaling through MAPK, PI3K/AKT, and STAT pathways, inhibiting cell proliferation and promoting apoptosis.",
                "source": {"type": "pubchem", "reference": "CID 123631", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Gefitinib", "relation": "inhibits", "object": "EGFR tyrosine kinase", "confidence": 0.99},
            {"subject": "Gefitinib", "relation": "binds_to", "object": "EGFR ATP-binding site", "confidence": 0.97},
            {"subject": "Gefitinib", "relation": "has_substructure", "object": "quinazoline ring", "confidence": 0.99},
            {"subject": "Gefitinib", "relation": "has_substructure", "object": "morpholine ring", "confidence": 0.99}
        ],
        "mineru_usage": [
            {
                "tool": "MinerU API",
                "task": "解析吉非替尼临床试验论文，提取药代动力学数据表格和分子结构图",
                "input": "data/raw/papers/gefitinib_clinical.pdf",
                "output": "data/raw/parsed/gefitinib_clinical_parsed.json"
            }
        ]
    },
    {
        "name": "Ritonavir",
        "pubchem_cid": 3976,
        "category": "Antiviral Drug",
        "common_name": "Ritonavir",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Ritonavir is an antiretroviral protease inhibitor used in the treatment of HIV/AIDS. Originally developed as a standalone protease inhibitor, it is now primarily used at low doses as a pharmacokinetic enhancer (booster) for other protease inhibitors due to its potent inhibition of CYP3A4.",
                "source": {"type": "pubchem", "reference": "CID 3976", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Ritonavir inhibits the HIV-1 protease enzyme, preventing cleavage of the gag-pol polyprotein and subsequent maturation of infectious viral particles. At low doses, it potently inhibits cytochrome P450 3A4 (CYP3A4), increasing the bioavailability of co-administered protease inhibitors.",
                "source": {"type": "pubchem", "reference": "CID 3976", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Ritonavir", "relation": "inhibits", "object": "HIV-1 protease", "confidence": 0.98},
            {"subject": "Ritonavir", "relation": "inhibits", "object": "CYP3A4", "confidence": 0.99},
            {"subject": "Ritonavir", "relation": "co-administered_with", "object": "lopinavir", "confidence": 0.97},
            {"subject": "Ritonavir", "relation": "co-administered_with", "object": "atazanavir", "confidence": 0.95}
        ],
        "mineru_usage": []
    },
    {
        "name": "Methotrexate",
        "pubchem_cid": 126941,
        "category": "Antimetabolite",
        "common_name": "Methotrexate",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Methotrexate (MTX) is an antimetabolite and antifolate drug used in the treatment of cancer, autoimmune diseases, and ectopic pregnancy. It is one of the oldest and most widely used chemotherapy agents, first introduced in the 1950s.",
                "source": {"type": "pubchem", "reference": "CID 126941", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Methotrexate competitively inhibits dihydrofolate reductase (DHFR), preventing the reduction of dihydrofolate to tetrahydrofolate. This depletes tetrahydrofolate pools essential for purine and pyrimidine synthesis, ultimately inhibiting DNA synthesis and cell division.",
                "source": {"type": "pubchem", "reference": "CID 126941", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Methotrexate", "relation": "inhibits", "object": "dihydrofolate reductase (DHFR)", "confidence": 0.99},
            {"subject": "Methotrexate", "relation": "derivative_of", "object": "folic acid", "confidence": 0.97},
            {"subject": "Methotrexate", "relation": "has_substructure", "object": "pteridine ring", "confidence": 0.99},
            {"subject": "Methotrexate", "relation": "has_substructure", "object": "glutamic acid moiety", "confidence": 0.99}
        ],
        "mineru_usage": [
            {
                "tool": "MinerU Open Source",
                "task": "解析甲氨蝶呤综述论文，提取结构-活性关系表格",
                "input": "data/raw/papers/mtx_review.pdf",
                "output": "data/raw/parsed/mtx_review_parsed.json"
            }
        ]
    },
    {
        "name": "Paclitaxel",
        "pubchem_cid": 36314,
        "category": "Anticancer Drug",
        "common_name": "Paclitaxel",
        "text_descriptions": [
            {
                "type": "general_description",
                "content": "Paclitaxel (Taxol) is a mitotic inhibitor used in cancer chemotherapy. Originally isolated from the bark of the Pacific yew tree (Taxus brevifolia), it is now produced semi-synthetically. It is used to treat ovarian, breast, lung, and pancreatic cancers.",
                "source": {"type": "pubchem", "reference": "CID 36314", "mineru_parsed": False},
                "language": "en"
            },
            {
                "type": "mechanism_of_action",
                "content": "Paclitaxel stabilizes microtubules by binding to the β-tubulin subunit, promoting tubulin polymerization and preventing depolymerization. This locks cells in the G2/M phase of the cell cycle, leading to apoptosis.",
                "source": {"type": "pubchem", "reference": "CID 36314", "mineru_parsed": False},
                "language": "en"
            }
        ],
        "entity_relations": [
            {"subject": "Paclitaxel", "relation": "binds_to", "object": "β-tubulin", "confidence": 0.99},
            {"subject": "Paclitaxel", "relation": "stabilizes", "object": "microtubules", "confidence": 0.99},
            {"subject": "Paclitaxel", "relation": "has_substructure", "object": "taxane ring system", "confidence": 0.99},
            {"subject": "Paclitaxel", "relation": "derivative_of", "object": "10-deacetylbaccatin III", "confidence": 0.95}
        ],
        "mineru_usage": []
    }
]


def build_sample_dataset(output_path: str, generate_images: bool = True):
    """构建样例数据集"""

    processor = MoleculeProcessor()
    records = []
    failed = []

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 创建图片输出目录
    if generate_images:
        os.makedirs("data/samples/images/2d", exist_ok=True)
        os.makedirs("data/samples/models/3d", exist_ok=True)

    for i, mol_info in enumerate(SAMPLE_MOLECULES):
        record_id = _CID_TO_RECORD_ID.get(mol_info["pubchem_cid"], f"MOL-{i+1:06d}")
        logger.info(f"Processing [{i+1}/{len(SAMPLE_MOLECULES)}]: {mol_info['name']} ({record_id})")

        try:
            # 从 PubChem 获取数据并构建记录
            record = processor.build_alignment_record(
                record_id=record_id,
                smiles="",  # will be fetched from PubChem
                pubchem_cid=mol_info["pubchem_cid"],
                common_name=mol_info.get("common_name"),
                text_descriptions=mol_info.get("text_descriptions", []),
                entity_relations=mol_info.get("entity_relations", []),
                mineru_usage=mol_info.get("mineru_usage", [])
            )

            # 如果 SMILES 为空，尝试从 PubChem 获取
            if not record["smiles"]["canonical"]:
                pubchem_data = processor.fetch_pubchem_data(mol_info["pubchem_cid"])
                smiles = pubchem_data.get("smiles", "")
                if smiles:
                    record["smiles"] = asdict(processor.get_smiles_info(smiles))
                    physico, druglike = processor.compute_properties(smiles)
                    record["properties"]["physicochemical"] = asdict(physico)
                    record["properties"]["drug_likeness"] = asdict(druglike)

            # 添加分类标签
            record["category"] = mol_info.get("category", "Unknown")

            # 生成 2D 结构图
            if generate_images and record["smiles"]["canonical"]:
                img_path = f"data/samples/images/2d/{record_id}.png"
                abs_img_path = os.path.abspath(img_path)
                processor.generate_2d_image(
                    record["smiles"]["canonical"],
                    abs_img_path
                )
                record["modalities"]["structure_2d"]["rdkit_generated"] = img_path

                # 生成 3D 构象
                sdf_path = f"data/samples/models/3d/{record_id}.sdf"
                abs_sdf_path = os.path.abspath(sdf_path)
                processor.generate_3d_conformer(
                    record["smiles"]["canonical"],
                    abs_sdf_path
                )
                record["modalities"]["structure_3d"]["sdf_path"] = sdf_path

            records.append(record)
            logger.info(f"  ✓ {mol_info['name']}: SMILES={record['smiles']['canonical'][:50]}...")

            # PubChem 速率限制
            time.sleep(0.5)

        except Exception as e:
            logger.error(f"  ✗ Failed to process {mol_info['name']}: {e}")
            failed.append({"name": mol_info["name"], "error": str(e)})

    # 写入 JSONL
    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # 验证数据集
    validator = AlignmentValidator()
    validation_results = validator.validate_dataset(records)

    logger.info(f"\n{'='*60}")
    logger.info(f"Dataset building complete!")
    logger.info(f"  Total: {validation_results['total']}")
    logger.info(f"  Valid: {validation_results['valid']}")
    logger.info(f"  Invalid: {validation_results['invalid']}")
    logger.info(f"  Failed: {len(failed)}")
    logger.info(f"  Output: {output_path}")

    if validation_results["errors"]:
        logger.warning(f"\nValidation errors:")
        for rid, errs in validation_results["errors"].items():
            for err in errs[:3]:
                logger.warning(f"  {rid}: {err}")

    # 保存验证报告
    report_path = output_path.replace(".jsonl", "_validation.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(validation_results, f, ensure_ascii=False, indent=2)
    logger.info(f"  Validation report: {report_path}")

    return records, validation_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build sample dataset for MDIC26-Track1 SciAlign")
    parser.add_argument("--output", default="data/samples/sample_dataset.jsonl",
                        help="Output JSONL file path")
    parser.add_argument("--no-images", action="store_true",
                        help="Skip image generation")
    args = parser.parse_args()

    build_sample_dataset(
        output_path=args.output,
        generate_images=not args.no_images
    )
