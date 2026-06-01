# MolAlign: 分子跨模态对齐数据集

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-green.svg)](LICENSE)
[![AGI4S Track 1](https://img.shields.io/badge/Competition-AGI4S%20Track%201-blue)]()

> **语料筑基·AGI4S 前沿语料赛道** — Sci-Align 科学对齐数据

## 📋 项目简介

MolAlign 是一个面向药物化学与分子科学领域的**多模态对齐数据集**，涵盖 **820** 分子实体、**35** 个药理类别。围绕每个分子实体，构建**五类模态的跨模态对齐**，使大语言模型能够准确理解分子的多维科学表征。

### 五类模态对齐

| 模态 | 描述 | 示例 |
|------|------|------|
| 🖼️ **分子结构图** | 2D/3D 分子结构可视化 | PNG 图像、SDF 文件 |
| 🔬 **分子标识符** | SMILES、InChI | `CC(=O)Oc1ccccc1C(=O)O` |
| 📛 **分子命名** | IUPAC、通用名、同义词 | Aspirin / 2-acetyloxybenzoic acid |
| 📊 **分子属性** | 物化参数、类药性、实验数据 | MW=180.16, LogP=1.19 |
| 📝 **科学文本** | 合成、作用机制、临床应用 | "Aspirin inhibits COX-1..." |

## 🗂️ 项目结构

```
MolAlign/
├── data/
│   ├── processed/                    # 完整数据集 (820条)
│   │   ├── molalign_dataset.jsonl    # JSONL 格式 (主文件)
│   │   ├── molalign_dataset.json     # JSON 格式
│   │   ├── dataset_stats.json        # 数据集统计
│   │   ├── validation_report.json    # 验证报告
│   │   ├── images/2d/                # 820 张 2D 分子结构图 (PNG)
│   │   ├── images/paper/             # 论文提取图片文件（覆盖 33 条记录）
│   │   └── models/3d/                # 799 个 3D 分子构象 (SDF)
│   ├── samples/                      # 精选样例 (12条，含完整实体关系)
│   │   ├── sample_dataset.jsonl
│   │   └── sample_dataset.json
│   └── raw/                          # 原始数据
│       └── parsed_mineru_api/        # MinerU Agent API 日志与 89 篇成功解析 Markdown
├── src/
│   ├── schema.py                     # JSON Schema 定义
│   ├── molecule_processor.py         # 分子数据处理器 (RDKit + PubChem)
│   ├── alignment_validator.py        # 跨模态对齐验证器
│   ├── mineru_client.py              # MinerU API 客户端
│   └── pipeline.py                   # Pipeline 主脚本
├── scripts/
│   ├── molecule_db.py                # 分子目标数据库
│   ├── expand_molecule_db.py         # 分子数据库扩展脚本（可选历史脚本）
│   ├── mineru_agent_parse.py         # MinerU Agent API 真实解析器
│   ├── build_full_dataset.py         # 全量数据集构建脚本
│   ├── enrich_expanded_dataset.py    # 统一数据增强脚本
│   ├── build_static_samples.py       # 精选样例生成
│   ├── build_sample_dataset.py       # 动态样例构建
│   └── validate_dataset.py           # 数据集验证脚本
├── docs/
│   └── technical_report.md           # 技术报告文档
├── requirements.txt
├── LICENSE                           # CC-BY-4.0
└── README.md
```

## 🚀 快速开始

### 环境配置

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 生成样例数据

```bash
# 全量数据集构建（820 个分子，需要 RDKit + 网络连接 PubChem）
python scripts/build_full_dataset.py --output-dir data/processed

# 可选：扩展分子数据库（当前提交版本为 820 条）
python scripts/expand_molecule_db.py

# 使用 MinerU Agent API 解析论文（12 个任务，10 个成功 Markdown）
python scripts/mineru_agent_parse.py

# 统一数据增强
python scripts/enrich_expanded_dataset.py

# 修复高优先级一致性问题并重建样例
python scripts/repair_dataset_integrity.py

# 验证数据集
python scripts/validate_dataset.py --input data/processed/molalign_dataset.jsonl --report data/processed/validation_report.json

# 重新生成统计
python scripts/generate_final_stats.py
```

### 使用数据集

```python
import json

# 加载 JSONL
records = []
with open("data/samples/sample_dataset.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        records.append(json.loads(line))

# 查看第一条记录
print(records[0]["names"]["common_name"])  # Aspirin
print(records[0]["smiles"]["canonical"])    # CC(=O)Oc1ccccc1C(=O)O
```

## 🔧 MinerU 工具链使用

本数据集构建过程中真实使用 **MinerU Agent API** 解析论文 PDF。为避免模板化或不可追溯记录，当前版本只在有 `task_id`、`markdown_url` 和本地 Markdown 输出证据的分子记录中填写 `alignment_metadata.mineru_usage`。

| 工具 | 用途 | 使用范围 |
|------|------|----------|
| **MinerU Agent API** | 解析开放获取论文 PDF，获取结构化 Markdown | 99 个提交任务，89 个成功，10 个失败；成功输出共 **4,712,803** 字符 |
| **RDKit** | SMILES 标准化、2D/3D 结构生成、物化属性统一计算 | 820 条记录 |
| **PubChem REST API** | 分子标识符、同义词、基础描述与公共属性来源 | 820 条记录 |

详见 [技术报告 §5-§6](docs/technical_report.md)

## 🔬 MinerU Agent API 真实使用

在数据集扩展过程中，我们通过 **MinerU Agent API** 提交了 **227 个** 药物化学相关论文解析任务，其中 **199 个成功、28 个失败**：

- **成功解析论文数**: 199 篇开放获取论文（涵盖药物化学、分子药理学等领域）
- **失败任务**: 超页数限制（>20 页）或解析失败的论文
- **真实 API 调用**: 每个 API 请求提交真实任务 ID，获取完整解析结果
- **成功解析字符数**: **10,100,002 字符** 结构化 Markdown
- **产生数据记录**: **198 条分子记录**含真实 MinerU 使用证据
- **解析文件存储**: `data/raw/parsed_mineru_api/` 保存 `parsing_log.json` 和解析输出

使用的解析脚本为 `scripts/mineru_agent_parse.py`（原始 12 篇）和 `scripts/expand_mineru_coverage.py`（扩展 215 篇，PMC 开放获取论文，批处理带连接重试）。修复与证据同步脚本为 `scripts/repair_dataset_integrity.py`，它会根据 `parsing_log.json` 只保留真实可追溯的 MinerU 记录。

## 📊 数据集统计

| 指标 | 数值 |
|------|------|
| 总记录数 | **820** |
| 覆盖类别 | **35** (NSAID、抗生素、抗癌药、靶向治疗、降压药、天然产物、抗病毒药、降糖药、抗抑郁药、神经递质、激素、抗真菌药、抗癫痫药、抗组胺药、阿片类镇痛药、利尿药、维生素、抗炎药、抗疟药、他汀类、氨基酸、抗帕金森药、麻醉剂、胃肠药、肌肉松弛剂、诊断试剂等) |
| 2D 分子结构图 | **820** (100%) |
| 3D 分子构象 | **799** (97.4%) |
| 论文提取图片 | **33 条记录**（35 个图像文件） |
| MinerU Agent API 解析 | **227 个任务 / 199 个成功**，**10,100,002 字符** 结构化 Markdown，真实 task_id |
| 实验生物活性 | **30 条** (PubChem curated data) |
| 文本描述（中英文） | **820** (100% 中英双语，平均 2.02 条/分子) |
| 实体关系 | **820** (100%，平均 2.0 条/分子，类别→靶点映射) |
| MinerU 使用记录 | **198 条分子记录 (24.1%)**（来源分层见 provenance.tsv） |
| 验证通过率 | **820/820 (100.0%)** |

## 📖 文档

- [技术报告](docs/technical_report.md) — 完整的数据集设计、构建和使用说明
- [数据集卡 Data Card](docs/data_card.md) — HuggingFace 风格的结构化概览
- [数据集规格表 Datasheet](docs/datasheet.md) — Gebru et al. (2021) 规范的完整 datasheet
- [数据来源分层 Provenance](data/processed/provenance.tsv) — 每条记录的来源标注（smiles / relations / mineru / paper image / bioactivity）和证据质量等级（A/B/C）
- [JSON Schema](src/schema.py) — 数据集的 JSON Schema 定义

## 🏆 赛事信息

- **赛事**: 语料筑基·AGI4S 前沿语料赛道
- **赛道**: 赛道一 — Sci-Align 科学对齐数据
- **截止日期**: 2026年5月31日

## 📄 开源协议

- **数据集**: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- **代码**: [MIT License](LICENSE)

## 🙏 致谢

- [MinerU](https://github.com/opendatalab/MinerU) — 高精度文档解析引擎
- [RDKit](https://github.com/rdkit/rdkit) — 开源化学信息学工具包
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) — 公共化合物数据库
- [MolScribe](https://github.com/thomas0809/MolScribe) — 分子结构图识别
