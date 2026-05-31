# 原始数据说明

本目录存放数据集构建过程中使用的原始数据。

## 论文 PDF 文件 (`papers/`)

以下 5 篇开放获取论文通过 MinerU 工具链解析，用于提取分子结构图和科学文本：

| 文件名 | 对应分子 | DOI | 来源 | 大小 |
|--------|----------|-----|------|------|
| `ibuprofen_pharmacology.pdf` | Ibuprofen (MOL-000002) | 10.3389/fphar.2017.00263 | Frontiers in Pharmacology | 1.7 MB |
| `curcumin_pharmacology.pdf` | Curcumin (MOL-000080) | 10.3389/fphar.2017.00687 | Frontiers in Pharmacology | 462 KB |
| `dopamine_neuroscience.pdf` | Dopamine (MOL-000086) | 10.3389/fnins.2017.00724 | Frontiers in Neuroscience | 930 KB |
| `paclitaxel_pharmacology.pdf` | Paclitaxel (MOL-000021) | 10.3389/fphar.2019.01330 | Frontiers in Pharmacology | 1.3 MB |
| `acetaminophen_pharmacology.pdf` | Acetaminophen (MOL-000120) | 10.3389/fphar.2020.00794 | Frontiers in Pharmacology | 1.5 MB |

**论文均为开放获取（Open Access），遵循 CC-BY 协议，可自由下载和使用。**

## MinerU 解析输出 (`parsed/`)

每篇论文经 MinerU Open Source (PyMuPDF engine) 解析后输出：

```
parsed/<paper_name>/
├── mineru_parsed.json     # 结构化解析结果
│   ├── full_text          # 全文文本（按页分段）
│   ├── figures[]          # 提取的图片元数据
│   └── sections[]         # 识别的段落结构
└── images/                # 提取的论文图片
    ├── page1_img1.png
    ├── page6_img2.png
    └── ...
```

### 提取统计

| 论文 | 页数 | 提取图片数 | 文本字符数 |
|------|------|-----------|-----------|
| Ibuprofen | 15 | 6 | 77,059 |
| Curcumin | 8 | 2 | 44,373 |
| Dopamine | 12 | 1 | 75,876 |
| Paclitaxel | 8 | 1 | 48,448 |
| Acetaminophen | 15 | 7 | 68,192 |

## 其他数据来源

### PubChem 公共数据库
- URL: https://pubchem.ncbi.nlm.nih.gov/
- 内容: 分子标识符、物化属性、同义词、文本描述
- 获取方式: PubChem REST API
- 协议: 公共领域数据

## 数据合规声明

- 所有论文为开放获取（Open Access），遵循 CC-BY 协议
- PubChem 数据为公共领域数据
- 不包含任何个人隐私数据
- 不包含受控物质合成细节
- 符合科学数据伦理规范
- 禁止生成虚假科学数据或伪造实验结果
