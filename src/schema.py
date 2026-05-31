"""
Molecular Cross-Modal Alignment Dataset - Schema Definition
============================================================
Sci-Align 数据集的 JSON Schema 定义

每条数据记录围绕一个分子实体，包含五类模态的对齐信息：
1. 分子结构图（2D depiction / 论文原图）
2. SMILES / InChI 标识符
3. IUPAC 名称 / 通用名称
4. 分子属性表格（物化参数、药代参数等）
5. 科学文本描述（合成方法、生物活性、应用场景）

对齐关系通过 "结构—属性—描述" 三元组 + 实体关系图谱表示
"""

DATASET_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "MolecularCrossModalAlignment",
    "description": "分子跨模态对齐数据集 Schema",
    "type": "object",
    "required": [
        "record_id",
        "molecule_id",
        "smiles",
        "names",
        "modalities",
        "properties",
        "text_descriptions",
        "entity_relations",
        "alignment_metadata"
    ],
    "properties": {
        "record_id": {
            "type": "string",
            "description": "数据集内唯一记录 ID",
            "pattern": "^MOL-\\d{6}$"
        },
        "molecule_id": {
            "type": "object",
            "description": "分子在公共数据库中的标识",
            "properties": {
                "pubchem_cid": {"type": "integer", "description": "PubChem Compound ID"},
                "chembl_id": {"type": ["string", "null"], "description": "ChEMBL ID"},
                "drugbank_id": {"type": ["string", "null"], "description": "DrugBank ID"},
                "cas_number": {"type": ["string", "null"], "description": "CAS 注册号"}
            }
        },
        "smiles": {
            "type": "object",
            "description": "SMILES 标识符（多种形式）",
            "properties": {
                "canonical": {"type": "string", "description": "标准化 SMILES"},
                "isomeric": {"type": ["string", "null"], "description": "含立体信息的 SMILES"},
                "inchi": {"type": "string", "description": "InChI 标识符"},
                "inchikey": {"type": "string", "description": "InChIKey 哈希"}
            },
            "required": ["canonical", "inchi", "inchikey"]
        },
        "names": {
            "type": "object",
            "description": "分子命名信息",
            "properties": {
                "iupac_name": {"type": ["string", "null"], "description": "IUPAC 系统命名"},
                "common_name": {"type": ["string", "null"], "description": "通用名称"},
                "synonyms": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "同义词列表"
                }
            }
        },
        "modalities": {
            "type": "object",
            "description": "多模态数据文件引用",
            "properties": {
                "structure_2d": {
                    "type": "object",
                    "properties": {
                        "rdkit_generated": {"type": "string", "description": "RDKit 生成的 2D 结构图路径"},
                        "image_format": {"type": "string", "enum": ["png", "svg"]},
                        "image_size": {"type": "string", "description": "图片尺寸 e.g. 512x512"}
                    }
                },
                "structure_paper": {
                    "type": ["object", "null"],
                    "description": "论文中提取的分子结构图",
                    "properties": {
                        "image_path": {"type": "string", "description": "提取的图片路径"},
                        "source_paper": {"type": "string", "description": "来源论文 DOI"},
                        "page_number": {"type": "integer"},
                        "figure_label": {"type": "string", "description": "图中标签 e.g. 'Figure 1a'"}
                    }
                },
                "structure_3d": {
                    "type": ["object", "null"],
                    "description": "3D 分子构象",
                    "properties": {
                        "sdf_path": {"type": "string", "description": "SDF 文件路径"},
                        "conformer_method": {
                            "type": "string",
                            "enum": ["RDKit_ETKDG", "DFT", "experimental"],
                            "description": "构象生成方法"
                        }
                    }
                },
                "table_data": {
                    "type": ["object", "null"],
                    "description": "论文表格中提取的结构化数据",
                    "properties": {
                        "table_path": {"type": "string", "description": "表格数据文件路径 (CSV/JSON)"},
                        "source_paper": {"type": "string"},
                        "table_label": {"type": "string", "description": "表格标签 e.g. 'Table 2'"}
                    }
                }
            },
            "required": ["structure_2d"]
        },
        "properties": {
            "type": "object",
            "description": "分子物化属性和药代参数",
            "properties": {
                "physicochemical": {
                    "type": "object",
                    "properties": {
                        "molecular_weight": {"type": "number", "description": "分子量 (g/mol)"},
                        "exact_mass": {"type": ["number", "null"], "description": "精确分子量"},
                        "logp": {"type": ["number", "null"], "description": "分配系数 (XLogP3)"},
                        "tpsa": {"type": ["number", "null"], "description": "拓扑极性表面积 (Å²)"},
                        "hydrogen_bond_donors": {"type": ["integer", "null"], "description": "氢键供体数"},
                        "hydrogen_bond_acceptors": {"type": ["integer", "null"], "description": "氢键受体数"},
                        "rotatable_bonds": {"type": ["integer", "null"], "description": "可旋转键数"},
                        "heavy_atoms": {"type": ["integer", "null"], "description": "重原子数"},
                        "ring_count": {"type": ["integer", "null"], "description": "环数"},
                        "formal_charge": {"type": ["integer", "null"], "description": "形式电荷"}
                    }
                },
                "drug_likeness": {
                    "type": ["object", "null"],
                    "properties": {
                        "lipinski_violations": {"type": ["integer", "null"], "description": "Lipinski 违规数"},
                        "ghose_violations": {"type": ["integer", "null"], "description": "Ghose 违规数"},
                        "veber_violations": {"type": ["integer", "null"], "description": "Veber 违规数"},
                        "bioavailability_score": {"type": ["number", "null"], "description": "生物利用度评分"},
                        "synthetic_accessibility": {"type": ["number", "null"], "description": "合成可及性评分 (1-10)"}
                    }
                },
                "experimental": {
                    "type": ["object", "null"],
                    "description": "实验测定数据（来自论文表格）",
                    "properties": {
                        "melting_point": {"type": ["string", "null"]},
                        "solubility": {"type": ["string", "null"]},
                        "bioactivity": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "assay_type": {"type": "string"},
                                    "target": {"type": "string"},
                                    "value": {"type": "string"},
                                    "unit": {"type": "string"},
                                    "source_paper": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            }
        },
        "text_descriptions": {
            "type": "array",
            "description": "科学文本描述（多来源）",
            "items": {
                "type": "object",
                "required": ["type", "content", "source"],
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": [
                            "synthesis",
                            "bioactivity",
                            "mechanism_of_action",
                            "pharmacokinetics",
                            "clinical_use",
                            "safety",
                            "general_description",
                            "structure_activity_relationship"
                        ],
                        "description": "描述类型"
                    },
                    "content": {"type": "string", "description": "文本内容"},
                    "source": {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": ["pubchem", "paper", "drugbank", "wikipedia", "manual_curation"],
                                "description": "来源类型"
                            },
                            "reference": {"type": "string", "description": "DOI 或 URL"},
                            "section": {"type": ["string", "null"], "description": "论文段落引用"},
                            "mineru_parsed": {"type": "boolean", "description": "是否经 MinerU 解析"}
                        },
                        "required": ["type"]
                    },
                    "language": {
                        "type": "string",
                        "enum": ["zh", "en"],
                        "default": "en"
                    }
                }
            },
            "minItems": 1
        },
        "entity_relations": {
            "type": "array",
            "description": "实体关系图谱（结构—功能—描述 三元组）",
            "items": {
                "type": "object",
                "required": ["subject", "relation", "object"],
                "properties": {
                    "subject": {"type": "string", "description": "主体实体"},
                    "relation": {
                        "type": "string",
                        "description": "关系类型",
                        "examples": [
                            "inhibits", "activates", "binds_to", "metabolized_to",
                            "has_substructure", "derivative_of", "isomer_of",
                            "co-administered_with", "contraindicated_with",
                            "targets", "regulated_by", "synthesized_from"
                        ]
                    },
                    "object": {"type": "string", "description": "客体实体"},
                    "evidence": {
                        "type": ["string", "null"],
                        "description": "证据来源"
                    },
                    "confidence": {
                        "type": ["number", "null"],
                        "description": "关系置信度 (0-1)",
                        "minimum": 0,
                        "maximum": 1
                    }
                }
            }
        },
        "alignment_metadata": {
            "type": "object",
            "description": "对齐过程元数据",
            "properties": {
                "alignment_confidence": {
                    "type": "number",
                    "description": "整体对齐置信度 (0-1)",
                    "minimum": 0,
                    "maximum": 1
                },
                "validation_status": {
                    "type": "string",
                    "enum": ["automated_pass", "manual_verified", "flagged_for_review"],
                    "description": "验证状态"
                },
                "mineru_usage": {
                    "type": "array",
                    "description": "MinerU 工具使用记录",
                    "items": {
                        "type": "object",
                        "properties": {
                            "tool": {
                                "type": "string",
                                "enum": [
                                    "MinerU API",
                                    "MinerU Agent API",
                                    "MinerU Open Source",
                                    "MinerU Skills",
                                    "MinerU Online"
                                ]
                            },
                            "task": {"type": "string", "description": "具体任务描述"},
                            "input": {"type": "string", "description": "输入文件/数据"},
                            "output": {"type": "string", "description": "输出文件/数据"},
                            "detail": {"type": "string", "description": "任务详细描述"}
                        }
                    }
                },
                "created_at": {"type": "string", "format": "date-time"},
                "updated_at": {"type": "string", "format": "date-time"},
                "version": {"type": "string", "description": "数据版本号"}
            },
            "required": ["alignment_confidence", "validation_status", "mineru_usage"]
        }
    }
}

# 简化版 Schema 用于快速验证
ALIGNMENT_RECORD_REQUIRED_FIELDS = [
    "record_id",
    "molecule_id",
    "smiles",
    "names",
    "modalities",
    "properties",
    "text_descriptions",
    "entity_relations",
    "alignment_metadata"
]

# 关系类型白名单
VALID_RELATION_TYPES = {
    "inhibits", "activates", "binds_to", "metabolized_to",
    "has_substructure", "derivative_of", "isomer_of",
    "co-administered_with", "contraindicated_with",
    "targets", "regulated_by", "regulates", "synthesized_from",
    "catalyzes", "substrate_of", "competes_with",
    "stabilizes", "destabilizes", "interacts_with",
    "intercalates", "generates", "cofactor_of",
    "used_as", "modulates"
}
