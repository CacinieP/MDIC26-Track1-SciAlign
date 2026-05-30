# MolAlign: 分子跨模态对齐数据集

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-green.svg)](LICENSE)
[![AGI4S Track 1](https://img.shields.io/badge/Competition-AGI4S%20Track%201-blue)]()

> **语料筑基·AGI4S 前沿语料赛道** — Sci-Align 科学对齐数据

## 📋 项目简介

MolAlign 是一个面向药物化学与分子科学领域的**多模态对齐数据集**。围绕每个分子实体，构建**五类模态的跨模态对齐**，使大语言模型能够准确理解分子的多维科学表征。

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
│   ├── processed/                    # 完整数据集 (120条)
│   │   ├── molalign_dataset.jsonl    # JSONL 格式 (主文件)
│   │   ├── molalign_dataset.json     # JSON 格式
│   │   ├── dataset_stats.json        # 数据集统计
│   │   ├── validation_report.json    # 验证报告
│   │   ├── images/2d/                # 120 张 2D 分子结构图 (PNG)
│   │   └── models/3d/                # 119 个 3D 分子构象 (SDF)
│   ├── samples/                      # 精选样例 (12条，含完整实体关系)
│   │   ├── sample_dataset.jsonl
│   │   └── sample_dataset.json
│   └── raw/                          # 原始数据
├── src/
│   ├── schema.py                     # JSON Schema 定义
│   ├── molecule_processor.py         # 分子数据处理器 (RDKit + PubChem)
│   ├── alignment_validator.py        # 跨模态对齐验证器
│   ├── mineru_client.py              # MinerU API 客户端
│   └── pipeline.py                   # Pipeline 主脚本
├── scripts/
│   ├── molecule_db.py                # 120 分子目标数据库
│   ├── build_full_dataset.py         # 全量数据集构建脚本
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
# 全量数据集构建（120个分子，需要 RDKit + 网络连接 PubChem）
python scripts/build_full_dataset.py --output-dir data/processed

# 精选样例（12个分子，含完整实体关系和 MinerU 记录）
python scripts/build_static_samples.py

# 验证数据集
python scripts/validate_dataset.py --input data/processed/molalign_dataset.jsonl
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

本数据集构建过程中使用了 MinerU 工具链的四种模式：

| 工具 | 用途 |
|------|------|
| **MinerU Open Source** | 本地解析论文 PDF，提取分子结构图和表格 |
| **MinerU API** | 批量处理大量论文，自动化解析 |
| **MinerU Skills** | 化学结构提取技能，分子图识别 |
| **MinerU Online** | 网页端快速解析特定论文 |

详见 [技术报告 §5-§6](docs/technical_report.md)

## 📊 数据集统计

| 指标 | 数值 |
|------|------|
| 总记录数 | **120** |
| 覆盖类别 | **26** (NSAID、抗生素、抗癌药、神经递质、激素、维生素等) |
| 2D 分子结构图 | **120** (100%) |
| 3D 分子构象 | **119** (99.2%) |
| 文本描述（中英文） | **120** (100% 含中文) |
| 实体关系（平均/条） | **1.9** (100% 覆盖) |
| MinerU 使用记录 | **120** (100%) |
| 验证通过率 | **100%** |

## 📖 文档

- [技术报告](docs/technical_report.md) — 完整的数据集设计、构建和使用说明
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
