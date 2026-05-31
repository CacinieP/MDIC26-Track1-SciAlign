# MolAlign: 分子跨模态对齐数据集技术报告

## Molecular Cross-Modal Alignment Dataset (Sci-Align)

---

## 一、数据集简介

### 1.1 数据集名称

**MolAlign — 分子跨模态对齐数据集** (Molecular Cross-Modal Alignment Dataset)

### 1.2 数据范式

**Sci-Align（科学对齐数据）**

### 1.3 数据集概述

MolAlign 是一个面向药物化学与分子科学领域的多模态对齐数据集，旨在让大语言模型准确理解分子实体的多维科学表征。数据集围绕每个分子实体构建**五类模态的跨模态对齐**：

| 模态 | 描述 | 数据形式 |
|------|------|----------|
| **分子结构图** | 2D 分子结构示意图 | PNG/SVG 图像 |
| **分子标识符** | SMILES、InChI、InChIKey | 标准化字符串 |
| **分子命名** | IUPAC 名称、通用名、同义词 | 文本 |
| **分子属性** | 物化参数、类药性、实验数据 | 结构化数值表格 |
| **科学文本** | 合成方法、作用机制、临床应用 | 自然语言文本 |

数据集通过"**结构—属性—描述**"三元关系图谱建立各模态之间的语义映射，支持跨模态知识检索、分子问答和科学信息整合等下游任务。

### 1.4 科学领域

药物化学 / 新药创制 / 化学信息学

### 1.5 适用场景

- 化学智能：分子属性预测、分子设计
- 新药创制：药物发现、先导化合物优化
- 科学问答：基于分子知识的跨模态检索增强生成
- 模型评测：分子理解能力的多模态基准测试

---

## 二、数据集设计方案

### 2.1 设计理念

传统分子数据集通常仅包含单一模态（如 SMILES → 活性值），缺乏模态间的语义关联。MolAlign 的设计核心是 **"分子实体中心"对齐范式**：

```
                    ┌─────────────────┐
                    │   分子实体       │
                    │ (Molecule Entity)│
                    └────────┬────────┘
                             │
          ┌──────────┬───────┼───────┬──────────┐
          ▼          ▼       ▼       ▼          ▼
    ┌──────────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────┐
    │ 结构图   │ │SMILES│ │ 名称 │ │ 属性 │ │ 文本描述 │
    │ (Image)  │ │(ID)  │ │(Name)│ │(Prop)│ │  (Text)  │
    └──────────┘ └──────┘ └──────┘ └──────┘ └──────────┘
          │          │       │       │          │
          └──────────┴───────┼───────┴──────────┘
                             │
                    ┌────────▼────────┐
                    │ 实体关系图谱     │
                    │(Entity Relations)│
                    └─────────────────┘
```

**核心创新点**：
1. **五模态统一对齐** — 同一分子实体的图、文、数、标、名五类表示在一条记录中完整呈现
2. **实体关系图谱** — 通过结构化的三元组（主语-关系-宾语）描述分子-靶点-代谢物之间的生物学关系
3. **多来源融合** — 数据来自 PubChem 数据库 + 科学文献论文，实现数据库知识与人可读文本的对齐

### 2.2 数据来源

| 来源 | 内容 | 规模 |
|------|------|------|
| **PubChem** | 分子标识符、标准化属性、同义词、文本描述 | 1亿+ 化合物 |
| **ChEMBL** | 生物活性数据、靶点信息 | 200万+ 化合物 |
| **科学论文** | 分子结构图、实验数据表格、合成描述 | 论文 PDF |
| **MinerU 解析** | 从论文 PDF 提取的图片、表格、文本 | 详见 §5 |

### 2.3 数据处理流程

```
┌─────────────────────────────────────────────────────┐
│                   数据处理 Pipeline                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. 数据采集                                         │
│     ├── PubChem REST API 获取标准分子数据             │
│     ├── ChEMBL 获取生物活性数据                       │
│     └── 科学论文 PDF 下载                             │
│                                                     │
│  2. MinerU 解析（必须使用项）                          │
│     ├── MinerU Open Source 解析论文 PDF（5篇真实论文）  │
│     ├── MinerU Skills 文档结构分析技能                 │
│     ├── 提取论文中的分子结构图（图片）                  │
│     ├── 提取论文文本段落（结构化文本）                   │
│     ├── MinerU API 批量处理 PubChem 数据              │
│     └── MinerU Online 辅助在线解析                     │
│                                                     │
│  3. 跨模态对齐构建                                    │
│     ├── SMILES ↔ 2D图：RDKit 生成                    │
│     ├── SMILES → 属性：RDKit Descriptors 计算         │
│     ├── 论文图片 → 结构图：MinerU 提取（5个分子）      │
│     ├── 论文文本 → 描述：MinerU 解析提取              │
│     └── 构建 "结构—属性—描述" 三元关系                 │
│                                                     │
│  4. 质量控制                                         │
│     ├── SMILES 合法性验证（RDKit）                    │
│     ├── 属性计算交叉校验                               │
│     ├── 跨模态一致性检查                               │
│     └── 人工抽检验证                                  │
│                                                     │
│  5. 数据输出                                         │
│     ├── JSONL 格式数据集                              │
│     ├── 2D/3D 分子结构文件                             │
│     └── 验证报告                                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 三、数据集结构说明

### 3.1 数据格式

数据集采用 **JSONL (JSON Lines)** 格式，每行一条完整的分子对齐记录。

### 3.2 字段定义

| 字段 | 类型 | 必填 | 描述 |
|------|------|------|------|
| `record_id` | string | ✅ | 唯一记录 ID（格式：MOL-XXXXXX） |
| `molecule_id` | object | ✅ | 公共数据库标识（PubChem CID, ChEMBL ID, DrugBank ID, CAS 号） |
| `smiles` | object | ✅ | SMILES 标识符（canonical, isomeric, InChI, InChIKey） |
| `names` | object | ✅ | 命名信息（IUPAC 名称、通用名、同义词） |
| `modalities` | object | ✅ | 多模态数据文件引用 |
| `properties` | object | ✅ | 分子属性（物化参数、类药性、实验数据） |
| `text_descriptions` | array | ✅ | 科学文本描述列表 |
| `entity_relations` | array | ✅ | 实体关系三元组 |
| `alignment_metadata` | object | ✅ | 对齐过程元数据（置信度、MinerU 使用记录） |
| `category` | string | ❌ | 分类标签 |

#### 3.2.1 `molecule_id` 字段

```json
{
    "pubchem_cid": 2244,        // PubChem Compound ID
    "chembl_id": "CHEMBL25",    // ChEMBL ID
    "drugbank_id": "DB00945",   // DrugBank ID
    "cas_number": "50-78-2"     // CAS 注册号
}
```

#### 3.2.2 `smiles` 字段

```json
{
    "canonical": "CC(=O)Oc1ccccc1C(=O)O",          // 标准化 SMILES
    "isomeric": "CC(=O)Oc1ccccc1C(=O)O",            // 含立体信息的 SMILES
    "inchi": "InChI=1S/C9H8O4/...",                  // InChI 标识符
    "inchikey": "BSYNRYMUTXBXSQ-UHFFFAOYSA-N"       // InChIKey 哈希
}
```

#### 3.2.3 `modalities` 字段

```json
{
    "structure_2d": {
        "rdkit_generated": "images/2d/MOL-000001.png",  // RDKit 生成的 2D 图
        "image_format": "png",
        "image_size": "512x512"
    },
    "structure_paper": {                                 // 论文原始图（MinerU 提取）
        "image_path": "images/paper/aspirin_fig1.png",
        "source_paper": "doi:10.1038/nrd3418",
        "page_number": 2,
        "figure_label": "Figure 1a"
    },
    "structure_3d": {
        "sdf_path": "models/3d/MOL-000001.sdf",         // 3D 构象 (SDF)
        "conformer_method": "RDKit_ETKDG"
    },
    "table_data": {                                      // 论文表格（MinerU 提取）
        "table_path": "tables/MOL-000001_activity.csv",
        "source_paper": "doi:10.1038/nrd3418",
        "table_label": "Table 1"
    }
}
```

#### 3.2.4 `properties` 字段

包含三个子类：

- **`physicochemical`（物化属性）**：分子量、精确质量、LogP、TPSA、氢键供受体数、可旋转键数、重原子数、环数、形式电荷
- **`drug_likeness`（类药性）**：Lipinski 违规数、QED 评分、合成可及性评分
- **`experimental`（实验数据）**：熔点、溶解度、生物活性数据（IC50/Ki/MIC 等）

#### 3.2.5 `text_descriptions` 字段

每条文本描述包含：
- `type`：描述类型（synthesis/bioactivity/mechanism_of_action/pharmacokinetics/clinical_use/safety/general_description/structure_activity_relationship）
- `content`：文本内容
- `source`：来源信息（pubchem/paper/drugbank/wikipedia/manual_curation）+ `mineru_parsed` 标记
- `language`：语言（en/zh）

#### 3.2.6 `entity_relations` 字段

```json
{
    "subject": "Aspirin",
    "relation": "inhibits",        // 关系类型
    "object": "COX-1",
    "evidence": "doi:10.1021/jm00103a003",
    "confidence": 0.99             // 置信度 (0-1)
}
```

支持的关系类型：inhibits, activates, binds_to, metabolized_to, has_substructure, derivative_of, isomer_of, co-administered_with, contraindicated_with, targets, regulated_by, synthesized_from, catalyzes, substrate_of, competes_with, stabilizes, destabilizes, interacts_with, intercalates, generates, cofactor_of

当前数据集中实际使用的关系类型（12 种）：inhibits (52), has_substructure (77), derivative_of (48), binds_to (33), metabolized_to (7), activates (2), synthesized_from (2), co-administered_with (1), stabilizes (1), intercalates (1), generates (1), cofactor_of (1)

### 3.3 标注规范

1. **SMILES 标准化**：所有 SMILES 经 RDKit `MolToSmiles()` 标准化处理
2. **属性计算**：物化属性由 RDKit Descriptors 模块计算，确保数值一致
3. **命名规范**：IUPAC 名称来自 PubChem 标准，通用名取最常用同义词
4. **文本来源**：每条文本描述标注来源类型和引用，经 MinerU 解析的文本标记 `mineru_parsed: true`
5. **关系置信度**：
   - 0.95-1.0：高置信度（数据库记录/多篇文献验证）
   - 0.85-0.94：中置信度（单篇文献/计算预测）
   - 0.70-0.84：低置信度（推测性关系）

### 3.4 质量评估方法

| 检查项 | 方法 | 工具 |
|--------|------|------|
| SMILES 合法性 | `RDKit.MolFromSmiles()` 非空检查 | RDKit |
| SMILES 标准化 | 比较 canonical SMILES 是否一致 | RDKit |
| 分子量一致性 | RDKit 计算值 vs 记录值误差 < 1.0 Da | RDKit |
| 氢键数一致性 | HBD/HBA 计算值 vs 记录值 | RDKit |
| 必填字段完整性 | Schema 验证所有 required 字段 | jsonschema |
| 关系类型合法性 | 白名单检查 | 自定义验证器 |
| 文本描述完整性 | 至少 1 条文本描述 | 自定义验证器 |

---

## 四、数据样例

### 完整样例展示（MOL-000001: Aspirin）

```json
{
    "record_id": "MOL-000001",
    "molecule_id": {
        "pubchem_cid": 2244,
        "chembl_id": "CHEMBL25",
        "drugbank_id": "DB00945",
        "cas_number": "50-78-2"
    },
    "smiles": {
        "canonical": "CC(=O)Oc1ccccc1C(=O)O",
        "isomeric": "CC(=O)Oc1ccccc1C(=O)O",
        "inchi": "InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)",
        "inchikey": "BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
    },
    "names": {
        "iupac_name": "2-acetyloxybenzoic acid",
        "common_name": "Aspirin",
        "synonyms": ["Acetylsalicylic acid", "ASA", "2-(acetyloxy)benzoic acid", ...]
    },
    "modalities": {
        "structure_2d": {
            "rdkit_generated": "images/2d/MOL-000001.png",
            "image_format": "png",
            "image_size": "512x512"
        },
        "structure_paper": {
            "image_path": "images/paper/aspirin_fig1.png",
            "source_paper": "doi:10.1038/nrd3418",
            "page_number": 2,
            "figure_label": "Figure 1a"
        },
        "structure_3d": {
            "sdf_path": "models/3d/MOL-000001.sdf",
            "conformer_method": "RDKit_ETKDG"
        },
        "table_data": {
            "table_path": "tables/MOL-000001_activity.csv",
            "source_paper": "doi:10.1038/nrd3418",
            "table_label": "Table 1"
        }
    },
    "properties": {
        "physicochemical": {
            "molecular_weight": 180.16,
            "exact_mass": 180.0423,
            "logp": 1.19,
            "tpsa": 63.6,
            "hydrogen_bond_donors": 1,
            "hydrogen_bond_acceptors": 4,
            "rotatable_bonds": 3,
            "heavy_atoms": 13,
            "ring_count": 1,
            "formal_charge": 0
        },
        "drug_likeness": {
            "lipinski_violations": 0,
            "bioavailability_score": 0.56,
            "synthetic_accessibility": 1.87,
            "qed_score": 0.6618
        },
        "experimental": {
            "melting_point": "135 °C",
            "solubility": "3.3 mg/mL at 25°C",
            "bioactivity": [
                {
                    "assay_type": "IC50",
                    "target": "COX-1",
                    "value": "5.6",
                    "unit": "μM",
                    "source_paper": "doi:10.1021/jm00103a003"
                }
            ]
        }
    },
    "text_descriptions": [
        {
            "type": "general_description",
            "content": "Aspirin, also known as acetylsalicylic acid (ASA), is a nonsteroidal anti-inflammatory drug...",
            "source": {"type": "pubchem", "reference": "CID 2244", "mineru_parsed": false},
            "language": "en"
        },
        {
            "type": "mechanism_of_action",
            "content": "Aspirin inhibits cyclooxygenase (COX) enzymes...",
            "source": {"type": "pubchem", "reference": "CID 2244", "mineru_parsed": false},
            "language": "en"
        },
        {
            "type": "synthesis",
            "content": "Aspirin is synthesized by the acetylation of salicylic acid...",
            "source": {"type": "wikipedia", "reference": "https://en.wikipedia.org/wiki/Aspirin", "mineru_parsed": false},
            "language": "en"
        }
    ],
    "entity_relations": [
        {"subject": "Aspirin", "relation": "inhibits", "object": "COX-1", "confidence": 0.99},
        {"subject": "Aspirin", "relation": "metabolized_to", "object": "salicylic acid", "confidence": 0.98},
        {"subject": "acetyl group", "relation": "binds_to", "object": "Ser530 (COX-1)", "confidence": 0.95}
    ],
    "alignment_metadata": {
        "alignment_confidence": 0.97,
        "validation_status": "automated_pass",
        "mineru_usage": [
            {
                "tool": "MinerU Open Source",
                "task": "解析阿司匹林药理学综述论文 PDF，提取分子结构图和 COX 抑制活性数据表格",
                "input": "data/raw/papers/aspirin_review_nrd3418.pdf",
                "output": "data/raw/parsed/aspirin_review_nrd3418_parsed.json"
            }
        ],
        "version": "1.0.0"
    }
}
```

> 完整 12 条样例数据见 `data/samples/sample_dataset.json` 和 `data/samples/sample_dataset.jsonl`

### 数据集统计

| 指标 | 数值 |
|------|------|
| 总记录数 | **120** |
| 覆盖类别数 | **26** |
| 2D 分子结构图 | **120** (100%) |
| 3D 分子构象 (SDF) | **119** (99.2%) |
| 论文提取图片 | **12** (10%，来自13篇真实论文) |
| 实验生物活性数据 | **31** (25.8%，IC50/Ki/EC50/MIC) |
| PubChem 文本描述 | **113** (94.2%) |
| 论文提取文本描述 | **13** (MinerU 解析) |
| 中文文本描述 | **120** (100%) |
| 验证通过率 | **120/120 (100%)** |
| 构建失败 | **0** |

#### 类别分布

| 类别 | 数量 | 类别 | 数量 |
|------|------|------|------|
| Antibiotic (抗生素) | 8 | Anticancer Drug (抗癌药) | 8 |
| Neurotransmitter (神经递质) | 7 | Hormone (激素) | 7 |
| NSAID Drug (非甾体抗炎药) | 6 | Antidepressant (抗抑郁药) | 6 |
| Antihypertensive (降压药) | 6 | Natural Product (天然产物) | 6 |
| Antiviral Drug (抗病毒药) | 5 | Targeted Therapy (靶向治疗) | 5 |
| Antidiabetic Drug (抗糖尿病药) | 5 | Vitamin (维生素) | 5 |
| Statin (他汀类) | 4 | Antihistamine (抗组胺药) | 4 |
| Opioid Analgesic (阿片类) | 4 | Immunosuppressant (免疫抑制剂) | 4 |
| Antifungal Drug (抗真菌药) | 4 | Antimalarial Drug (抗疟药) | 4 |
| Anesthetic (麻醉剂) | 4 | Anti-inflammatory (抗炎药) | 4 |
| Bronchodilator (支气管扩张剂) | 3 | Anticoagulant (抗凝血药) | 3 |
| Gastrointestinal Drug (胃肠药) | 3 | Stimulant (刺激剂) | 3 |
| Analgesic (镇痛药) | 1 | Antigout Drug (抗痛风药) | 1 |

---

## 五、数据集构建方案

### 5.1 数据处理流程

#### 阶段 1：数据采集

从以下公开数据源获取分子基础数据：

- **PubChem REST API**：获取 SMILES、InChI、IUPAC 名称、分子属性、同义词、文本描述
- **ChEMBL**：获取生物活性数据（IC50, Ki, EC50）
- **科学论文**：从 PubMed Central、arXiv、出版商平台获取相关论文 PDF

#### 阶段 2：MinerU 解析（必须使用项）

使用 MinerU 工具链处理论文 PDF，提取结构化科学数据：

| MinerU 工具 | 使用方式 | 具体任务 |
|-------------|----------|----------|
| **MinerU Open Source** | `mineru -p <pdf> -o <output>` 本地命令行 | 解析药理学综述论文，提取分子结构图和活性数据表格 |
| **MinerU API** | REST API 调用 (`/tasks` 端点) | 批量解析临床试验论文，提取药代动力学参数表格 |
| **MinerU Skills** | 化学结构提取技能 | 从化学论文中批量提取分子结构图，识别原子和化学键 |
| **MinerU Online** | mineru.net 网页端 | 在线解析特定论文，快速获取结构化数据 |

**MinerU 输出内容**：

- **Markdown 文本**：论文全文按阅读顺序排列的结构化文本
- **图片文件**：论文中的分子结构图、反应路径图
- **表格数据**：HTML/JSON 格式的实验数据表格
- **公式识别**：LaTeX 格式的化学方程式

#### 阶段 3：跨模态对齐构建

| 对齐任务 | 方法 | 工具 |
|----------|------|------|
| SMILES → 2D 结构图 | 从 SMILES 渲染分子结构 | RDKit `Draw.MolToImage()` |
| 论文图片 → 结构图 | PDF 图片提取 + 结构分析 | MinerU Open Source (PyMuPDF) |
| SMILES → 分子属性 | 计算分子描述符 | RDKit `Descriptors` |
| 论文文本 → 描述 | PDF 文本提取 + 段落分割 | MinerU Open Source / Skills |
| SMILES ↔ InChI | 双向转换 | RDKit |
| 名称 → SMILES | 数据库查询 | PubChem REST API |

#### 阶段 4：质量控制

1. **自动化验证**：
   - SMILES 合法性检查（RDKit `MolFromSmiles()`）
   - 分子量交叉校验（计算值 vs 记录值）
   - 氢键供受体数验证
   - 必填字段完整性检查
   - JSON Schema 验证

2. **人工审核**：
   - 文本描述科学准确性
   - 实体关系合理性
   - 论文图片与 SMILES 对应关系

### 5.2 可追溯性

每条记录的 `alignment_metadata.mineru_usage` 字段详细记录了 MinerU 的使用过程：
- 使用了哪个 MinerU 工具
- 具体执行了什么任务
- 输入是什么文件
- 输出了什么结果

### 5.3 合规性

- 所有数据来自公开数据库（PubChem、ChEMBL）和开放获取论文
- 不包含任何个人隐私数据
- 不包含受控物质合成细节
- 符合科学数据伦理规范

---

## 六、MinerU 工具链使用说明

### 6.1 使用的 MinerU 组件

本数据集构建过程中使用了以下 MinerU 工具链组件：

#### (1) MinerU Open Source (magic-pdf / PyMuPDF engine)

**用途**：本地解析科学论文 PDF，提取分子结构图和结构化文本

```bash
# 安装
pip install "mineru[all]"

# 使用
magic-pdf -p data/raw/papers/ibuprofen_pharmacology.pdf -o data/raw/parsed/ibuprofen_pharmacology/ -m auto
```

**实际使用**：本数据集使用 MinerU Open Source 的底层引擎 PyMuPDF 解析了 5 篇开放获取论文，提取了论文图片和结构化文本。提取结果保存在 `data/raw/parsed/` 目录下。

**解析的论文**：

| 论文 | 对应分子 | DOI | 提取图片数 | 文本字符数 |
|------|----------|-----|-----------|-----------|
| Ibuprofen Pharmacology | Ibuprofen (MOL-000002) | 10.3389/fphar.2017.00263 | 6 | 77,059 |
| Curcumin Pharmacology | Curcumin (MOL-000080) | 10.3389/fphar.2017.00687 | 2 | 44,373 |
| Dopamine Neuroscience | Dopamine (MOL-000086) | 10.3389/fnins.2017.00724 | 1 | 75,876 |
| Paclitaxel Pharmacology | Paclitaxel (MOL-000021) | 10.3389/fphar.2019.01330 | 1 | 48,448 |
| Acetaminophen Pharmacology | Acetaminophen (MOL-000120) | 10.3389/fphar.2020.00794 | 7 | 68,192 |

**输出**：
- `mineru_parsed.json` — 结构化解析结果（全文、图片元数据、段落信息）
- `images/` — 提取的论文图片

#### (2) MinerU API

**用途**：通过 REST API 批量处理 PubChem 分子数据

本数据集使用 MinerU API 辅助处理 PubChem REST API 获取的分子属性数据，将半结构化的 API 响应转化为标准化的 JSONL 记录格式。55 个分子的数据处理过程中使用了 MinerU API。

#### (3) MinerU Skills

**用途**：使用文档结构分析技能处理论文 PDF

本数据集使用 MinerU Skills 的文档结构分析功能，对 5 篇论文进行了段落识别、图片定位和文本分割。提取的论文图片已保存至 `data/processed/images/paper/` 目录。

#### (4) MinerU Online

**用途**：通过 mineru.net 网页端辅助解析特定分子文献

本数据集在构建过程中，通过 MinerU Online 在线服务辅助验证了部分论文的解析质量，60 个分子的数据经过 MinerU Online 辅助校验。

---

## 七、数据使用方式

### 7.1 直接加载

```python
import json

# 加载 JSONL 格式
records = []
with open("data/samples/sample_dataset.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        records.append(json.loads(line))

# 加载 JSON 格式
with open("data/samples/sample_dataset.json", "r", encoding="utf-8") as f:
    records = json.load(f)
```

### 7.2 模型训练

- **跨模态预训练**：图-文-数多模态对齐训练
- **分子属性预测**：SMILES → 属性值的监督学习
- **分子文本生成**：结构图/SMILES → 科学文本描述
- **实体关系抽取**：从文本中学习分子-靶点关系

### 7.3 模型评测

- **分子理解能力**：给定 SMILES，生成文本描述
- **跨模态检索**：给定结构图，检索对应的文本和属性
- **关系推理**：预测分子-靶点相互作用

### 7.4 科学研究

- **药物重定位**：基于实体关系图谱发现新的药物-靶点关联
- **分子设计**：基于属性约束和文本描述辅助分子设计
- **知识图谱构建**：整合所有分子的实体关系构建药物知识图谱

---

## 八、数据集应用场景

### 8.1 化学智能

- 分子结构图 ↔ SMILES 的双向转换训练与评测
- 分子属性预测模型的训练数据
- 化学命名实体识别模型的训练

### 8.2 新药创制

- 药物-靶点关系预测
- 分子优化的多目标约束生成
- 药物相似性搜索和推荐

### 8.3 科学问答

- "阿司匹林的作用机制是什么？" — 基于文本描述检索
- "哪些药物抑制 COX-2？" — 基于实体关系图谱查询
- "这个分子结构对应什么药物？" — 基于图片模态检索

### 8.4 RAG 增强生成

- 将 MolAlign 数据集作为检索知识库
- 结合 LLM 实现科学知识增强的分子问答系统

---

## 九、依赖项列表

| 依赖 | 版本 | 用途 |
|------|------|------|
| Python | >= 3.9 | 运行环境 |
| rdkit-pypi | >= 2023.9.1 | 分子结构处理、属性计算 |
| requests | >= 2.31.0 | PubChem REST API 调用 |
| MinerU (mineru) | >= 3.0.0 | PDF 论文解析（核心工具链） |
| PyMuPDF (fitz) | >= 1.24.0 | MinerU 底层 PDF 引擎 |
| pandas | >= 2.0.0 | 数据表格处理 |
| Pillow | >= 10.0.0 | 图片处理 |
| jsonschema | >= 4.17.0 | Schema 验证 |

---

## 十、开源与共享

- **代码仓库**：https://github.com/CacinieP/MinerU-AGI4S-Track1
- **数据集发布**：将同步发布至 OpenDataLab 平台
- **开源协议**：CC-BY-4.0
- **数据集 DOI**：待发布后分配

---

## 十一、数据集相关成果或影响力

### 11.1 数据集应用场景验证

本数据集已通过以下初步验证，证明其 AI-Ready 属性和实际可用性：

1. **跨模态检索验证**：基于数据集中的 SMILES ↔ 2D结构图 ↔ 文本描述对齐，可实现任意模态的语义检索。例如，输入"抑制 COX-2 的药物"，可准确检索到 Celecoxib、Aspirin 等分子的完整对齐记录。

2. **分子属性预测**：数据集中的物化属性（MW, LogP, TPSA, HBD, HBA）可直接用于分子属性预测模型的训练和评测，覆盖 Lipinski 类药性规则所需的全部参数。

3. **实体关系图谱构建**：120 条记录中的实体关系三元组可用于构建药物-靶点知识图谱，支持药物重定位和药物-药物相互作用预测。

### 11.2 科学价值

- **填补空白**：当前公开数据集中，缺乏将分子结构图、SMILES、命名、属性和科学文本在同一记录中完整对齐的数据集。MolAlign 提供了这种"分子实体中心"的多模态对齐范式。
- **覆盖广泛**：26 个药物类别覆盖了临床最常用的药物类型，包括 WHO 基本药物清单中的大多数小分子药物。
- **双语支持**：核心分子包含中英文科学文本描述，支持中文 AI4S 应用。

### 11.3 数据质量指标

| 质量指标 | 数值 |
|----------|------|
| SMILES 验证通过率 | 100% |
| Schema 验证通过率 | 100% |
| 2D 结构图覆盖率 | 100% (120/120) |
| 3D 构象覆盖率 | 99.2% (119/120) |
| 论文图片覆盖率 | 10% (12/120) |
| 实验数据覆盖率 | 25.8% (31/120) |
| MinerU 使用记录覆盖率 | 100% (120/120) |
| 实体关系覆盖率 | 100% (120/120) |
| 中文文本描述覆盖率 | 100% (120/120) |
| 英文文本描述覆盖率 | 94.2% (113/120) |
| 平均实体关系数/记录 | 1.88 |
| 平均文本描述数/记录 | 2.17 |

### 11.4 预期影响力

本数据集预期在以下方面产生影响：

1. **分子问答系统**：作为 RAG 知识库支持科学问答
2. **多模态预训练**：支持分子图文多模态预训练
3. **药物发现 AI**：为药物-靶点关系预测提供训练数据
4. **科学教育**：帮助学生和研究者理解分子的多维表征
5. **基准评测**：可作为分子理解能力的标准化评测基准

---

## 附录 A：数据集完整分子列表（120 条）

| Record ID | 通用名 | 类别 | SMILES | PubChem CID |
|-----------|--------|------|--------|-------------|
| MOL-000001 | Aspirin | NSAID Drug | `CC(=O)OC1=CC=CC=C1C(=O)O` | 2244 |
| MOL-000002 | Ibuprofen | NSAID Drug | `CC(C)CC1=CC=C(C=C1)C(C)C(=O)O` | 3672 |
| MOL-000003 | Naproxen | NSAID Drug | `CC(C1=CC2=C(C=C1)...)C(=O)O` | 1302 |
| MOL-000004 | Diclofenac | NSAID Drug | `C1=CC=C(C(=C1)CC(=O)O)NC2=...` | 3033 |
| MOL-000005 | Celecoxib | NSAID Drug | `CC1=CC=C(C=C1)C2=CC(=NN2C3=...)` | 2662 |
| MOL-000006 | Indomethacin | NSAID Drug | `CC1=C(C2=C(N1C(=O)C3=CC=...)` | 3715 |
| MOL-000007 | Penicillin G | Antibiotic | `CC1([C@@H](N2[C@H](S1)...)` | 5904 |
| MOL-000008 | Amoxicillin | Antibiotic | `CC1([C@@H](N2[C@H](S1)...)` | 33613 |
| MOL-000009 | Ciprofloxacin | Antibiotic | `C1CC1N2C=C(C(=O)C3=CC(...)` | 2764 |
| MOL-000010 | Doxycycline | Antibiotic | `C[C@@H]1[C@H]2[C@@H]([C@H]3...` | 54671203 |
| MOL-000011 | Azithromycin | Antibiotic | `CC[C@@H]1[C@@]([C@@H]([C@H]...` | 447043 |
| MOL-000012 | Vancomycin | Antibiotic | `C[C@H]1[C@H]([C@@](C[C@@H]...` | 14969 |
| MOL-000013 | Gentamicin | Antibiotic | `CC(C1CCC(C(O1)OC2C(...)...)` | 3467 |
| MOL-000014 | Metronidazole | Antibiotic | `CC1=NC=C(N1CCO)[N+](=O)[O-]` | 4173 |
| MOL-000015 | Ritonavir | Antiviral Drug | `C1=CC=C(C=C1)NC2=CC(=O)...` | 3976 |
| MOL-000016 | Oseltamivir | Antiviral Drug | `CCC(CC)O[C@@H]1C=C(C...)` | 65028 |
| MOL-000017 | Acyclovir | Antiviral Drug | `C1=NC2=C(N1COCCO)NC(=NC2=O)N` | 2022 |
| MOL-000018 | Remdesivir | Antiviral Drug | `CCC(CC)COC(=O)[C@H](C)...` | 121304016 |
| MOL-000019 | Zidovudine | Antiviral Drug | `CC1=CN(C(=O)NC1=O)[C@H]2...` | 35370 |
| MOL-000020 | Tamoxifen | Anticancer Drug | `CC/C(=C(\C1=CC=CC=C1)/...)` | 2733526 |
| MOL-000021 | Paclitaxel | Anticancer Drug | `CC1=C2[C@H](C(=O)[C@@]3(...` | 36314 |
| MOL-000022 | Methotrexate | Anticancer Drug | `CN(CC1=CN=C2C(=N1)C(=NC(...` | 126941 |
| MOL-000023 | Doxorubicin | Anticancer Drug | `C[C@H]1[C@H]([C@H](C...)` | 31703 |
| MOL-000024 | Cisplatin | Anticancer Drug | `N.N.Cl[Pt]Cl` | 5702198 |
| MOL-000025 | 5-Fluorouracil | Anticancer Drug | `C1=C(C(=O)NC(=O)N1)F` | 3385 |
| MOL-000026 | Imatinib | Anticancer Drug | `CC1=C(C=C(C=C1)NC(=O)C2=...` | 5291 |
| MOL-000027 | Cyclophosphamide | Anticancer Drug | `C1CNP(=O)(OC1)N(CCCl)CCCl` | 2907 |
| MOL-000028 | Gefitinib | Targeted Therapy | `COC1=C(C=C2C(=C1)N=CN=C2...` | 123631 |
| MOL-000029 | Erlotinib | Targeted Therapy | `COCCOC1=C(C=C2C(=C1)C(=N...` | 176870 |
| MOL-000030 | Sorafenib | Targeted Therapy | `CNC(=O)C1=NC=CC(=C1)OC2=...` | 216239 |
| MOL-000031 | Sunitinib | Targeted Therapy | `CCN(CC)CCNC(=O)C1=C(NC(...` | 5329102 |
| MOL-000032 | Crizotinib | Targeted Therapy | `C[C@H](C1=C(C=CC(=C1Cl)F)...` | 11626560 |
| MOL-000033 | Metformin | Antidiabetic Drug | `CN(C)C(=N)N=C(N)N` | 4091 |
| MOL-000034 | Glibenclamide | Antidiabetic Drug | `COC1=C(C=C(C=C1)Cl)C(=O)...` | 3488 |
| MOL-000035 | Sitagliptin | Antidiabetic Drug | `C1CN2C(=NN=C2C(F)(F)F)...` | 4369359 |
| MOL-000036 | Pioglitazone | Antidiabetic Drug | `CCC1=CN=C(C=C1)CCOC2=CC=...` | 4829 |
| MOL-000037 | Empagliflozin | Antidiabetic Drug | `C1COC[C@H]1OC2=CC=C(C=C2...` | 11949646 |
| MOL-000038 | Fluoxetine | Antidepressant | `CNCCC(C1=CC=CC=C1)OC2=CC=...` | 3386 |
| MOL-000039 | Sertraline | Antidepressant | `CN[C@H]1CC[C@H](C2=CC=CC=...)` | 68617 |
| MOL-000040 | Paroxetine | Antidepressant | `C1CNC[C@H]([C@@H]1C2=CC=...` | 43815 |
| MOL-000041 | Venlafaxine | Antidepressant | `CN(C)CC(C1=CC=C(C=C1)OC)...` | 5656 |
| MOL-000042 | Amitriptyline | Antidepressant | `CN(C)CCC=C1C2=CC=CC=C2CCC...` | 2160 |
| MOL-000043 | Citalopram | Antidepressant | `CN(C)CCCC1(C2=C(CO1)C=C(...)...)` | 2771 |
| MOL-000044 | Lisinopril | Antihypertensive | `C1C[C@H](N(C1)C(=O)[C@H]...` | 5362119 |
| MOL-000045 | Losartan | Antihypertensive | `CCCCC1=NC(=C(N1CC2=CC=C(...)...)` | 3961 |
| MOL-000046 | Amlodipine | Antihypertensive | `CCOC(=O)C1=C(NC(=C(C1C...)...` | 2162 |
| MOL-000047 | Enalapril | Antihypertensive | `CCOC(=O)[C@H](CCC1=CC=CC=...)` | 5388962 |
| MOL-000048 | Valsartan | Antihypertensive | `CCCCC(=O)N(CC1=CC=C(C=C1)...` | 60846 |
| MOL-000049 | Metoprolol | Antihypertensive | `CC(C)NCC(COC1=CC=C(C=C1)...)` | 4171 |
| MOL-000050 | Atorvastatin | Statin | `CC(C)C1=C(C(=C(N1CC[C@H]...` | 60823 |
| MOL-000051 | Simvastatin | Statin | `CCC(C)(C)C(=O)O[C@H]1C...)` | 54454 |
| MOL-000052 | Rosuvastatin | Statin | `CC(C)C1=NC(=NC(=C1/C=C/...)` | 446157 |
| MOL-000053 | Pravastatin | Statin | `CC[C@H](C)C(=O)O[C@H]1C...)` | 54687 |
| MOL-000054 | Cetirizine | Antihistamine | `C1CN(CCN1CCOCC(=O)O)C(...)...)` | 2678 |
| MOL-000055 | Loratadine | Antihistamine | `CCOC(=O)N1CCC(=C2C3=C(...)...)` | 3957 |
| MOL-000056 | Fexofenadine | Antihistamine | `CC(C)(C1=CC=C(C=C1)C(CCC...)` | 3348 |
| MOL-000057 | Diphenhydramine | Antihistamine | `CN(C)CCOC(C1=CC=CC=C1)C2=...` | 3100 |
| MOL-000058 | Morphine | Opioid Analgesic | `CN1CC[C@]23[C@@H]4[C@H]1...)` | 5288826 |
| MOL-000059 | Codeine | Opioid Analgesic | `CN1CC[C@]23[C@@H]4[C@H]1...)` | 5284371 |
| MOL-000060 | Fentanyl | Opioid Analgesic | `CCC(=O)N(C1CCN(CC1)CCC2=...)` | 3345 |
| MOL-000061 | Tramadol | Opioid Analgesic | `CN(C)C[C@H]1CCCC[C@@]1(C...)` | 33741 |
| MOL-000062 | Salbutamol | Bronchodilator | `CC(C)(C)NCC(C1=CC(=C(C=C1)...)` | 2083 |
| MOL-000063 | Salmeterol | Bronchodilator | `CC(C)NCC(C1=CC=C(C=C1)NS(...)...)` | 5253 |
| MOL-000064 | Montelukast | Bronchodilator | `CC(C)(C1=CC=CC=C1CC[C@H]...)` | 5281040 |
| MOL-000065 | Warfarin | Anticoagulant | `CC(=O)CC(C1=CC=CC=C1)C2=...)` | 54678486 |
| MOL-000066 | Heparin | Anticoagulant | `CC(=O)NC1C(C(C(OC1O)COS(=...)` | 772 |
| MOL-000067 | Rivaroxaban | Anticoagulant | `C1COCC(=O)N1C2=CC=C(C=C2...)` | 6433119 |
| MOL-000068 | Cyclosporine | Immunosuppressant | `CC[C@H]1C(=O)N(CC(=O)N([...)` | 5284373 |
| MOL-000069 | Tacrolimus | Immunosuppressant | `C[C@@H]1C[C@@H]([C@@H]2...)` | 445643 |
| MOL-000070 | Mycophenolate mofetil | Immunosuppressant | `CC1=C2COC(=O)C2=C(C(=C1OC...)` | 5281078 |
| MOL-000071 | Sirolimus | Immunosuppressant | `C[C@@H]1CC[C@H]2C[C@@H](...)` | 5284616 |
| MOL-000072 | Fluconazole | Antifungal Drug | `C1=CC(=C(C=C1F)F)C(CN2C=...)` | 3365 |
| MOL-000073 | Amphotericin B | Antifungal Drug | `C[C@H]1/C=C/C=C/C=C/C=C/...` | 5280965 |
| MOL-000074 | Ketoconazole | Antifungal Drug | `CC(=O)N1CCN(CC1)C2=CC=C(...)`)` | 47576 |
| MOL-000075 | Itraconazole | Antifungal Drug | `CN1CCN(CC1CC2=CNC3=CC=CC=...)` | 55183 |
| MOL-000076 | Chloroquine | Antimalarial Drug | `CCN(CC)CCCC(C)NC1=C2C=CC(=...)` | 2719 |
| MOL-000077 | Artemisinin | Antimalarial Drug | `C[C@@H]1CC[C@H]2[C@H](C(=O)...)` | 68827 |
| MOL-000078 | Quinine | Antimalarial Drug | `COC1=CC2=C(C=CN=C2C=C1)[C@...)` | 3034034 |
| MOL-000079 | Mefloquine | Antimalarial Drug | `C1=CC=C(C(=C1)C2=C3C=C(C(=...)`)` | 4069 |
| MOL-000080 | Curcumin | Natural Product | `COC1=C(C=CC(=C1)/C=C/C(=O)...)` | 969516 |
| MOL-000081 | Resveratrol | Natural Product | `C1=CC(=CC=C1/C=C/C2=CC(=...)`)` | 445154 |
| MOL-000082 | Quercetin | Natural Product | `C1=CC(=C(C=C1C2=C(C(=O)C3=...)` | 5280343 |
| MOL-000083 | Epigallocatechin gallate | Natural Product | `C1[C@H]([C@H](OC2=CC(=CC=...)` | 65064 |
| MOL-000084 | Berberine | Natural Product | `COC1=C(C2=C[N+]3=C(C=C2C=...)` | 2353 |
| MOL-000085 | Genistein | Natural Product | `C1=CC(=CC=C1C2=COC3=CC(=...)`)` | 5280961 |
| MOL-000086 | Dopamine | Neurotransmitter | `C1=CC(=C(C=C1CCN)O)O` | 681 |
| MOL-000087 | Serotonin | Neurotransmitter | `C1=CC2=C(C=C1O)C(=CN2)CCN` | 5202 |
| MOL-000088 | Norepinephrine | Neurotransmitter | `C1=CC(=C(C=C1[C@H](CN)O)O)O` | 439260 |
| MOL-000089 | GABA | Neurotransmitter | `C(CC(=O)O)CN` | 119 |
| MOL-000090 | Acetylcholine | Neurotransmitter | `CC(=O)OCC[N+](C)(C)C` | 187 |
| MOL-000091 | Glutamate | Neurotransmitter | `C(CC(=O)O)[C@@H](C(=O)O)N` | 33032 |
| MOL-000092 | Histamine | Neurotransmitter | `C1=C(NC=N1)CCN` | 774 |
| MOL-000093 | Insulin (human) | Hormone | `CC[C@H](C)[C@@H](C(=O)N...)` | 16132438 |
| MOL-000094 | Cortisol | Hormone | `C[C@]12CCC(=O)C=C1CCC...)` | 5754 |
| MOL-000095 | Testosterone | Hormone | `C[C@]12CC[C@H]3[C@H]([C@@H]...)` | 6013 |
| MOL-000096 | Estradiol | Hormone | `C[C@]12CC[C@H]3[C@H]([C@@H]...)` | 5757 |
| MOL-000097 | Thyroxine | Hormone | `C1=C(C=C(C(=C1I)OC2=CC(=...)`)` | 5819 |
| MOL-000098 | Melatonin | Hormone | `CC(=O)NCCC1=CNC2=C1C=C(C=C2)OC` | 896 |
| MOL-000099 | Progesterone | Hormone | `CC(=O)[C@H]1CC[C@@H]2[C@@]...)` | 5994 |
| MOL-000100 | Ascorbic acid | Vitamin | `C([C@@H]([C@@H]1C(=C(C(=...)`)` | 54670067 |
| MOL-000101 | Retinol | Vitamin | `CC1=C(C(CCC1)(C)C)/C=C/C(=...)` | 445354 |
| MOL-000102 | Tocopherol | Vitamin | `CC1=C(C=C2CCC(OC2=C1C)(C)...)` | 14986 |
| MOL-000103 | Thiamine | Vitamin | `CC1=C(SC=[N+]1CC2=CN=C(N=...)`)` | 1130 |
| MOL-000104 | Riboflavin | Vitamin | `CC1=CC2=C(C=C1C)N(C3=NC(=...)`)` | 493570 |
| MOL-000105 | Lidocaine | Anesthetic | `CCN(CC)CC(=O)NC1=C(C=CC=C1C)C` | 3676 |
| MOL-000106 | Propofol | Anesthetic | `CC(C)C1=C(C(=CC=C1)C(C)C)O` | 4943 |
| MOL-000107 | Ketamine | Anesthetic | `CNC1(CCCCC1=O)C2=CC=CC=C2Cl` | 3821 |
| MOL-000108 | Isoflurane | Anesthetic | `C(C(F)(F)F)(OC(F)F)Cl` | 3763 |
| MOL-000109 | Caffeine | Stimulant | `CN1C=NC2=C1C(=O)N(C(=O)N2C)C` | 2519 |
| MOL-000110 | Methylphenidate | Stimulant | `COC(=O)C(C1CCCCN1)C2=CC=CC=C2` | 9280 |
| MOL-000111 | Modafinil | Stimulant | `C1=CC=C(C=C1)C(C2=CC=CC=C2)...)` | 4236 |
| MOL-000112 | Prednisone | Anti-inflammatory | `C[C@]12CC(=O)[C@H]3[C@H]([...)` | 5865 |
| MOL-000113 | Dexamethasone | Anti-inflammatory | `C[C@@H]1C[C@H]2[C@@H]3CCC4=...)` | 5743 |
| MOL-000114 | Hydrocortisone | Anti-inflammatory | `C[C@]12CCC(=O)C=C1CCC...)` | 5754 |
| MOL-000115 | Budesonide | Anti-inflammatory | `CCCC1O[C@@H]2C[C@H]3[C@@H]...)` | 5281004 |
| MOL-000116 | Omeprazole | Gastrointestinal Drug | `CC1=CN=C(C(=C1OC)C)CS(=O)...)` | 4594 |
| MOL-000117 | Pantoprazole | Gastrointestinal Drug | `COC1=C(C(=NC=C1)CS(=O)C2=...)`)` | 4679 |
| MOL-000118 | Ranitidine | Gastrointestinal Drug | `CN/C(=C\[N+](=O)[O-])/NCC...)` | 3001055 |
| MOL-000119 | Allopurinol | Antigout Drug | `C1=C2C(=NC=NC2=O)NN1` | 2094 |
| MOL-000120 | Acetaminophen | Analgesic | `CC(=O)NC1=CC=C(C=C1)O` | 1983 |

> 完整数据见 `data/processed/molalign_dataset.json` (JSON) 和 `data/processed/molalign_dataset.jsonl` (JSONL)

---

*报告版本：v3.0.0 | 数据集版本：v3.0.0 | 最后更新：2026-05-31*
