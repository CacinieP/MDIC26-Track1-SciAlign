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
│     ├── MinerU API 批量解析论文 PDF                   │
│     ├── 提取分子结构图（图片）                         │
│     ├── 提取实验数据表格（HTML/JSON）                  │
│     └── 提取文本段落（Markdown）                       │
│                                                     │
│  3. 跨模态对齐构建                                    │
│     ├── SMILES ↔ 2D图：RDKit 生成 + MolScribe 验证   │
│     ├── SMILES → 属性：RDKit Descriptors 计算         │
│     ├── 论文图片 → SMILES：MolScribe/DECIMER 识别     │
│     ├── 文本 → 分子：ChemDataExtractor NER 抽取       │
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

支持的关系类型：inhibits, activates, binds_to, metabolized_to, has_substructure, derivative_of, isomer_of, co-administered_with, contraindicated_with, targets, regulated_by, synthesized_from, catalyzes, substrate_of, competes_with, stabilizes, destabilizes, interacts_with

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
| 总记录数 | 12 |
| 覆盖类别数 | 10（NSAID、抗生素、抗糖尿病、神经递质、天然产物、抗癌药等） |
| 平均文本描述/条 | 2.2 |
| 平均实体关系/条 | 4.8 |
| 含 MinerU 使用记录 | 6/12 (50%) |
| 含论文原始图片 | 6/12 (50%) |

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
| 论文图片 → SMILES | 光学化学结构识别 (OCSR) | MolScribe / DECIMER |
| SMILES → 分子属性 | 计算分子描述符 | RDKit `Descriptors` |
| 文本 → 分子实体 | 化学命名实体识别 (NER) | ChemDataExtractor |
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

#### (1) MinerU Open Source (magic-pdf)

**用途**：本地解析科学论文 PDF，提取分子结构图和实验数据表格

```bash
# 安装
pip install "mineru[all]"

# 使用
mineru -p data/raw/papers/aspirin_review.pdf -o data/raw/parsed/aspirin_review/
```

**输出**：
- `aspirin_review.md` — 结构化 Markdown 文本
- `images/` — 提取的分子结构图
- 内嵌表格以 HTML/JSON 格式保存

#### (2) MinerU API

**用途**：通过 REST API 批量处理大量论文

```python
from src.mineru_client import MinerUClient

client = MinerUClient(api_key="your-api-key")
result = client.parse_pdf(
    pdf_path="data/raw/papers/gefitinib_clinical.pdf",
    output_dir="data/raw/parsed/gefitinib_clinical/"
)
```

#### (3) MinerU Skills

**用途**：使用预定义的化学结构提取技能批量处理化学论文

- 化学结构图检测与裁剪
- 分子结构图中的原子和化学键精确映射
- 反应方程式提取

#### (4) MinerU Online

**用途**：通过 mineru.net 网页端快速解析特定论文

- 访问 https://mineru.net
- 上传 PDF 文件
- 获取结构化解析结果

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
| MinerU (mineru) | >= 3.1.0 | PDF 论文解析 |
| MolScribe | >= 0.1.0 | 分子图片识别 (可选) |
| DECIMER | >= 3.0.0 | 分子图片识别 (可选) |
| ChemDataExtractor | >= 2.0.0 | 化学实体识别 (可选) |
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

## 附录 A：数据集完整样例列表

| Record ID | 通用名 | 类别 | SMILES | PubChem CID |
|-----------|--------|------|--------|-------------|
| MOL-000001 | Aspirin | NSAID Drug | CC(=O)Oc1ccccc1C(=O)O | 2244 |
| MOL-000002 | Caffeine | Stimulant | Cn1cnc2c1c(=O)n(c(=O)n2C)C | 2519 |
| MOL-000003 | Ibuprofen | NSAID Drug | CC(C)Cc1ccc(cc1)C(C)C(=O)O | 3672 |
| MOL-000004 | Penicillin G | Antibiotic | CC1([C@@H](N2[C@H](S1)...)C(=O)O)C | 5904 |
| MOL-000005 | Metformin | Antidiabetic Drug | CN(C)C(=N)NC(=N)N | 4091 |
| MOL-000006 | Dopamine | Neurotransmitter | NCCc1ccc(O)c(O)c1 | 681 |
| MOL-000007 | Curcumin | Natural Product | COc1cc(/C=C/C(=O)...)ccc1O | 969516 |
| MOL-000008 | Tamoxifen | Anticancer Drug | CC/C(=C(\c1ccccc1)/c2ccccc2)N(C)C | 2733526 |
| MOL-000009 | Gefitinib | Targeted Therapy | C1COCCN1c2ncnc3c2nc(n3)... | 123631 |
| MOL-000010 | Ritonavir | Antiviral Drug | CC(C)C1=NC(=CS1)C(=O)NC... | 3976 |
| MOL-000011 | Methotrexate | Antimetabolite | CC(=O)Nc1nc(N)c2nc(=O)n(...)n2c1 | 126941 |
| MOL-000012 | Paclitaxel | Anticancer Drug | CC1=C2C(=O)C(...)C5CC6C(...)C7CCCCC17 | 36314 |

> 完整数据见 `data/samples/sample_dataset.json`

---

*报告版本：v1.0.0 | 最后更新：2026-05-31*
