# MolAlign 分子跨模态对齐数据集技术报告

## 1. 数据集定位

MolAlign 是面向药物化学与分子科学的 Sci-Align 数据集，目标是让模型围绕同一分子实体理解和转换多种科学表示：分子结构图、SMILES/InChI 标识符、命名体系、物化属性、科学文本描述和实体关系。

当前提交版本包含 **820 条分子记录**，覆盖 **35 个药理/化学类别**。数据集主文件为 `data/processed/molalign_dataset.jsonl`，同步提供 JSON、样例集、统计报告和验证报告。

## 2. 模态设计

每条记录以分子实体为中心组织，主要字段如下：

| 模态/字段 | 内容 | 生成或来源 |
| --- | --- | --- |
| `smiles` | canonical SMILES、isomeric SMILES、InChI、InChIKey | PubChem + RDKit 标准化 |
| `names` | IUPAC 名称、通用名、同义词 | PubChem |
| `modalities.structure_2d` | 2D 分子结构图 | RDKit |
| `modalities.structure_3d` | 3D SDF 构象 | RDKit ETKDG |
| `modalities.structure_paper` | 论文图像资源引用 | MinerU 解析流程输出的落盘图像 |
| `properties` | 分子量、LogP、TPSA、HBD/HBA、类药性等 | RDKit 统一重算 |
| `text_descriptions` | 英文与中文科学描述，部分来自 MinerU Markdown | PubChem、人工整理、MinerU Agent API |
| `entity_relations` | 分子-靶点、结构片段、代谢/作用关系 | 规则增强与人工整理 |
| `alignment_metadata` | 对齐置信度、验证状态、MinerU 证据 | 构建脚本生成 |

## 3. 数据来源

| 来源 | 用途 | 当前规模 |
| --- | --- | --- |
| PubChem REST API | 分子标识符、名称、同义词、基础英文描述 | 820 条记录 |
| RDKit | SMILES 标准化、2D/3D 结构生成、物化属性重算 | 820 条记录 |
| MinerU Agent API | 论文 PDF 解析为结构化 Markdown | 12 个任务，10 个成功 |
| 人工/规则整理 | 中文描述、实体关系和类别标签 | 820 条记录 |

为避免不可追溯声明，当前版本不再宣称每条记录都直接使用 MinerU。只有能从 `data/raw/parsed_mineru_api/parsing_log.json` 追溯到 `task_id`、`markdown_url` 和本地 Markdown 文件的记录，才填写 `alignment_metadata.mineru_usage`。

## 4. MinerU 使用情况

### 4.1 Agent API 解析结果

通过 `scripts/mineru_agent_parse.py` 提交了 12 个 MinerU Agent API 解析任务。根据 `data/raw/parsed_mineru_api/parsing_log.json`：

| 指标 | 数值 |
| --- | --- |
| 提交任务数 | 12 |
| 成功任务数 | 10 |
| 失败任务数 | 2 |
| 成功 Markdown 总字符数 | 597,454 |
| 本地 Markdown 文件数 | 10 |
| 含真实 MinerU 证据的分子记录 | 9 |
| 来自 MinerU Markdown 的文本描述 | 10 |

失败任务如下，已在文档中明确保留，不再计入成功解析规模：

| 文件 | 状态 |
| --- | --- |
| `fluoxetine_ijms.pdf` | `markdown_url=null`, `content_length=0` |
| `vitamins_pharmaceuticals.pdf` | `markdown_url=null`, `content_length=0` |

### 4.2 真实证据落盘

成功解析的 Markdown 输出保存在 `data/raw/parsed_mineru_api/`：

- `acetaminophen_pharmacology.md`
- `caffeine_molecules.md`
- `curcumin_pharmacology.md`
- `dopamine_neuroscience.md`
- `doxorubicin_anticancer.md`
- `ibuprofen_pharmacology.md`
- `metformin_frontiers.md`
- `metformin_pharmaceutics.md`
- `morphine_opioid.md`
- `paclitaxel_pharmacology.md`

这些文件与数据集中 9 条分子记录相连：Ibuprofen、Paclitaxel、Doxorubicin、Metformin、Morphine、Curcumin、Dopamine、Caffeine、Acetaminophen。其中 Metformin 对应两篇成功论文。

## 5. 质量控制

### 5.1 SMILES 与属性标准

当前版本使用 RDKit 作为分子结构和属性一致性的统一标准：

1. `smiles.canonical` 与 `smiles.isomeric` 通过 `Chem.MolToSmiles()` 标准化。
2. `properties.physicochemical` 中的分子量、精确质量、LogP、TPSA、HBD、HBA、可旋转键、重原子数、环数和形式电荷由 RDKit 重算。
3. Lipinski 违规数和 QED 分数由 RDKit 重算。

这一修复消除了早期版本中 PubChem 与 RDKit HBA/HBD 定义混用导致的大量验证警告。

### 5.2 验证方式

验证脚本为：

```bash
python scripts/validate_dataset.py --input data/processed/molalign_dataset.jsonl --report data/processed/validation_report.json
```

验证检查包括：

- 必填字段完整性
- SMILES 合法性与 canonical 一致性
- 分子量和 RDKit 属性一致性
- 文本描述字段完整性
- 实体关系字段合法性
- 2D 结构图必备性
- 对齐置信度范围

当前验证结果：

| 指标 | 数值 |
| --- | --- |
| 总记录数 | 820 |
| 有效记录数 | 820 |
| 无效记录数 | 0 |
| 通过率 | 100.0% |
| 论文图像覆盖 | 33 条记录 |
| 实验生物活性覆盖 | 30 条记录 |
| 真实 MinerU 证据覆盖 | 9 条记录 |

## 6. 数据集统计

统计脚本为：

```bash
python scripts/generate_final_stats.py
```

当前统计摘要：

| 指标 | 数值 |
| --- | --- |
| 总记录数 | 820 |
| 类别数 | 35 |
| 2D 结构图 | 820 |
| 3D 构象 | 799 |
| 论文图像覆盖 | 33 条记录 |
| 实验数据覆盖 | 30 条记录 |
| 英文描述覆盖 | 820 |
| 中文描述覆盖 | 820 |
| 平均文本描述数 | 2.02 |
| 平均实体关系数 | 2.0 |
| 真实 MinerU Agent API 任务证据 | 10 |
| 含真实 MinerU 证据的分子记录 | 9 |

## 7. 可复现流程

推荐的重建与修复顺序如下：

```bash
pip install -r requirements.txt

# 1. 构建或更新全量数据集
python scripts/build_full_dataset.py --output-dir data/processed

# 2. 使用 MinerU Agent API 解析论文
python scripts/mineru_agent_parse.py

# 3. 修复高优先级一致性问题并重建样例
python scripts/repair_dataset_integrity.py

# 4. 重新验证
python scripts/validate_dataset.py --input data/processed/molalign_dataset.jsonl --report data/processed/validation_report.json

# 5. 重新生成统计
python scripts/generate_final_stats.py
```

`scripts/repair_dataset_integrity.py` 是当前版本的关键修复脚本，负责同步 JSON/JSONL、重算 RDKit 属性、清理模板化 MinerU 记录、下载 MinerU Markdown 输出并从主数据集重建样例文件。

## 8. 已知限制

1. 论文图像覆盖只有 33 条记录，不能代表 820 条记录均有论文原图。
2. 真实 MinerU 文本证据覆盖 9 条分子记录，其余记录主要由 PubChem/RDKit 和人工/规则整理构建。
3. 实体关系仍有规则增强成分，后续应继续补充 DOI、数据库链接或人工审核标签，提高证据粒度。
4. 两个 MinerU Agent API 任务失败，当前版本已明确标注并从成功统计中排除。

## 9. 协议与合规

数据集采用 CC-BY-4.0 协议发布，代码采用 MIT License。PubChem 数据为公共数据源；MinerU 解析对象为开放获取论文。当前版本避免声明无法追溯的 MinerU 使用记录，并在数据和文档中保留失败任务信息。
