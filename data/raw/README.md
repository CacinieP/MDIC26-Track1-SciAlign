# 原始数据说明

本目录存放 MolAlign 数据集构建过程中使用的原始数据和 MinerU 解析证据。

## MinerU Agent API 解析输出

目录：`data/raw/parsed_mineru_api/`

当前版本保留 12 个 MinerU Agent API 任务的解析日志，其中 10 个任务成功生成 Markdown，2 个任务失败。

| 指标 | 数值 |
| --- | --- |
| 提交任务数 | 12 |
| 成功任务数 | 10 |
| 失败任务数 | 2 |
| 成功 Markdown 总字符数 | 597,454 |
| 本地 Markdown 文件数 | 10 |

失败任务已保留在 `parsing_log.json` 中：

| 文件 | 状态 |
| --- | --- |
| `fluoxetine_ijms.pdf` | `markdown_url=null`, `content_length=0` |
| `vitamins_pharmaceuticals.pdf` | `markdown_url=null`, `content_length=0` |

成功输出文件：

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

这些 Markdown 文件由 `scripts/repair_dataset_integrity.py` 根据 `parsing_log.json` 中的 `markdown_url` 下载并落盘。数据集中只有能够追溯到真实 `task_id` 的分子记录才填写 `alignment_metadata.mineru_usage`。

## 论文 PDF 文件

原始 PDF 文件如存在，应放在 `data/raw/papers/`。当前仓库保留了 MinerU Agent API 的任务日志和 Markdown 输出作为可审计证据；失败任务不计入成功统计。

## 其他数据来源

### PubChem 公共数据库

- URL: https://pubchem.ncbi.nlm.nih.gov/
- 内容：分子标识符、物化属性、同义词、文本描述
- 获取方式：PubChem REST API
- 协议：公共领域数据

### RDKit

- 用途：SMILES 标准化、2D 分子图生成、3D 构象生成、物化属性重算
- 当前版本使用 RDKit 作为属性一致性的统一标准，避免 PubChem 与 RDKit HBA/HBD 定义混用。

## 数据合规声明

- PubChem 数据为公共领域数据。
- MinerU 解析任务面向开放获取论文。
- 不包含个人隐私数据。
- 不包含受控物质合成细节。
- 失败解析任务保留原始日志，不伪造成成功结果。
- 禁止生成虚假科学数据或伪造实验结果。
