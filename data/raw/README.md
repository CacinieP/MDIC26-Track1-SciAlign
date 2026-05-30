# 原始数据样例说明

本目录用于存放数据集构建过程中使用的原始数据。

## 数据来源

### PubChem 公共数据库
- URL: https://pubchem.ncbi.nlm.nih.gov/
- 内容: 分子标识符、物化属性、同义词、文本描述
- 获取方式: PubChem REST API (https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)
- 协议: 公共领域数据 (https://pubchem.ncbi.nlm.nih.gov/docs/faq)

### 科学论文 PDF
本数据集构建过程中使用 MinerU 工具链解析以下类型论文：
- 药理学综述论文（提取分子结构图、活性数据表格）
- 临床试验报告（提取药代动力学参数）
- 化学合成方法论文（提取合成路径和实验条件）

**示例论文（已通过 MinerU 解析）**:

| 论文 DOI | 内容 | MinerU 工具 |
|----------|------|-------------|
| doi:10.1038/nrd3418 | 阿司匹林药理学综述 | MinerU Open Source |
| doi:10.1016/S0140-6736(09)60691-0 | 吉非替尼临床试验 | MinerU API |
| doi:10.1002/ptr.5352 | 咖啡因药理学 | MinerU Online |
| doi:10.1021/acs.chemrev.9b00618 | 姜黄素综述 | MinerU Skills |

> 注：由于版权限制，论文 PDF 原文未包含在本仓库中。上述 DOI 可通过出版商平台或 PubMed Central 获取开放获取版本。

## MinerU 解析输出样例

每篇论文经 MinerU 解析后输出：
- **Markdown 文本**: 结构化的全文内容
- **图片文件**: 论文中的分子结构图、反应路径图
- **表格数据**: HTML/JSON 格式的实验数据表格
- **公式**: LaTeX 格式的化学方程式

解析输出样例存储在 `parsed/` 目录下。

## 数据合规声明

- 所有数据来自公开数据库（PubChem）和开放获取论文
- 不包含任何个人隐私数据
- 不包含受控物质合成细节
- 符合科学数据伦理规范
- 禁止生成虚假科学数据或伪造实验结果
