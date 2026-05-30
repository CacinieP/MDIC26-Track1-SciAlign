"""
MolAlign 竞赛 PPT 生成
========================
使用 PptxGenJS 风格的 python-pptx 生成竞赛演示文稿
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import os

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color scheme
BG_DARK = RGBColor(0x1a, 0x1a, 0x2e)
BG_ACCENT = RGBColor(0x16, 0x21, 0x3e)
ACCENT_BLUE = RGBColor(0x0f, 0x34, 0x60)
ACCENT_CYAN = RGBColor(0x53, 0xd8, 0xfb)
ACCENT_GREEN = RGBColor(0x48, 0xdb, 0x87)
TEXT_WHITE = RGBColor(0xff, 0xff, 0xff)
TEXT_LIGHT = RGBColor(0xb0, 0xb0, 0xc0)
HIGHLIGHT = RGBColor(0xe9, 0x45, 0x60)


def add_bg(slide, color=BG_DARK):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text(slide, left, top, width, height, text, font_size=18, color=TEXT_WHITE, bold=False, align=PP_ALIGN.LEFT):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = align
    return txBox


def add_bullet_slide(slide, left, top, width, height, items, font_size=16, color=TEXT_LIGHT):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.space_after = Pt(8)
    return txBox


# ================================================================
# Slide 1: Title
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
add_bg(slide)
add_text(slide, 1, 1.5, 11, 1.2, "MolAlign", 48, ACCENT_CYAN, True, PP_ALIGN.CENTER)
add_text(slide, 1, 2.8, 11, 0.8, "分子跨模态对齐数据集", 32, TEXT_WHITE, False, PP_ALIGN.CENTER)
add_text(slide, 1, 3.8, 11, 0.6, "Molecular Cross-Modal Alignment Dataset", 20, TEXT_LIGHT, False, PP_ALIGN.CENTER)
add_text(slide, 1, 5.0, 11, 0.5, "语料筑基 · AGI4S 前沿语料赛道 | Sci-Align 科学对齐数据", 16, ACCENT_GREEN, False, PP_ALIGN.CENTER)
add_text(slide, 1, 6.2, 11, 0.4, "https://github.com/CacinieP/MinerU-AGI4S-Track1", 14, TEXT_LIGHT, False, PP_ALIGN.CENTER)

# ================================================================
# Slide 2: 赛题背景
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "赛题背景与数据范式", 32, ACCENT_CYAN, True)
add_text(slide, 0.8, 1.5, 5.5, 0.6, "Sci-Align 科学对齐数据", 22, ACCENT_GREEN, True)
add_bullet_slide(slide, 0.8, 2.2, 5.5, 3.5, [
    "• 多学科跨模态对齐数据集",
    "• 科学数据间的结构化关联与跨模态一致性",
    "• 科学对象多维一致性表示",
    "• 真正的跨模态科学理解",
    "",
    "核心目标：让大模型准确理解「已知科学」",
    "而非进行复杂的探索与推理",
], 15)

add_text(slide, 7.0, 1.5, 5.5, 0.6, "MinerU 工具链（必须使用）", 22, ACCENT_GREEN, True)
add_bullet_slide(slide, 7.0, 2.2, 5.5, 3.5, [
    "✓ MinerU API — 批量论文 PDF 解析",
    "✓ MinerU Open Source — 本地解析引擎",
    "✓ MinerU Skills — 化学结构提取技能",
    "✓ MinerU Online — 在线快速解析",
    "",
    "要求：构建过程中必须至少使用一项",
    "MinerU 工具链",
], 15)

# ================================================================
# Slide 3: 数据集设计理念
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "数据集设计理念：「分子实体中心」对齐范式", 28, ACCENT_CYAN, True)

# Five modality boxes
modalities = [
    ("🖼️ 分子结构图", "2D/3D 分子结构\n可视化", ACCENT_BLUE),
    ("🔬 分子标识符", "SMILES / InChI\n标准化字符串", RGBColor(0x2d, 0x3a, 0x6e)),
    ("📛 分子命名", "IUPAC / 通用名\n/ 同义词", RGBColor(0x34, 0x49, 0x5e)),
    ("📊 分子属性", "物化参数 / 类药性\n/ 实验数据", RGBColor(0x3a, 0x5a, 0x40)),
    ("📝 科学文本", "合成方法 / 机制\n/ 临床应用", RGBColor(0x40, 0x6e, 0x5a)),
]

for i, (title, desc, color) in enumerate(modalities):
    x = 0.8 + i * 2.4
    shape = slide.shapes.add_shape(1, Inches(x), Inches(1.8), Inches(2.1), Inches(1.8))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    add_text(slide, x + 0.1, 1.9, 1.9, 0.5, title, 14, TEXT_WHITE, True, PP_ALIGN.CENTER)
    add_text(slide, x + 0.1, 2.5, 1.9, 0.8, desc, 11, TEXT_LIGHT, False, PP_ALIGN.CENTER)

# Innovation points
add_text(slide, 0.8, 4.2, 11, 0.6, "三大核心创新", 20, ACCENT_GREEN, True)
add_bullet_slide(slide, 0.8, 4.9, 11, 2.5, [
    "1️⃣ 五模态统一对齐 — 同一分子实体的图、文、数、标、名五类表示在一条记录中完整呈现",
    "2️⃣ 实体关系图谱 — 通过结构化三元组（主语-关系-宾语）描述分子-靶点-代谢物之间的生物学关系",
    "3️⃣ 多来源融合 — PubChem 数据库 + 科学文献论文，实现数据库知识与人可读文本的对齐",
], 14)

# ================================================================
# Slide 4: 数据集统计
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "数据集统计", 32, ACCENT_CYAN, True)

stats = [
    ("120", "分子记录"),
    ("26", "药物类别"),
    ("100%", "2D 结构图"),
    ("99.2%", "3D 构象"),
    ("100%", "MinerU 记录"),
    ("100%", "验证通过率"),
]

for i, (num, label) in enumerate(stats):
    x = 0.8 + i * 2.0
    add_text(slide, x, 1.6, 1.8, 0.8, num, 36, HIGHLIGHT, True, PP_ALIGN.CENTER)
    add_text(slide, x, 2.5, 1.8, 0.4, label, 14, TEXT_LIGHT, False, PP_ALIGN.CENTER)

add_text(slide, 0.8, 3.4, 11, 0.5, "类别覆盖（Top 10）", 18, ACCENT_GREEN, True)
add_bullet_slide(slide, 0.8, 4.0, 5.5, 3.0, [
    "抗生素 (8) | 抗癌药 (8)",
    "神经递质 (7) | 激素 (7)",
    "非甾体抗炎药 (6) | 抗抑郁药 (6)",
    "降压药 (6) | 天然产物 (6)",
    "抗病毒药 (5) | 靶向治疗 (5)",
    "... 共 26 个类别",
], 13)

add_bullet_slide(slide, 7.0, 4.0, 5.5, 3.0, [
    "✓ 五模态对齐：图/SMILES/名称/属性/文本",
    "✓ 中英双语科学文本描述",
    "✓ 实体关系三元组（药物-靶点-代谢物）",
    "✓ RDKit 生成 2D/3D 结构",
    "✓ PubChem 公共数据库溯源",
    "✓ 完整 JSON Schema 定义",
], 13)

# ================================================================
# Slide 5: 技术路线
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "数据构建技术路线", 32, ACCENT_CYAN, True)

stages = [
    ("阶段1", "数据采集", "PubChem REST API\nChEMBL\n科学论文 PDF", RGBColor(0x1a, 0x3a, 0x5c)),
    ("阶段2", "MinerU 解析", "PDF → 结构化文本\n分子结构图提取\n实验表格提取", RGBColor(0x1a, 0x4a, 0x5c)),
    ("阶段3", "跨模态对齐", "SMILES ↔ 2D图 (RDKit)\n图片 → SMILES (OCSR)\n文本 → 分子 (NER)", RGBColor(0x1a, 0x5a, 0x5c)),
    ("阶段4", "质量控制", "SMILES 验证\n属性交叉校验\nSchema 验证", RGBColor(0x1a, 0x6a, 0x5c)),
]

for i, (stage, title, desc, color) in enumerate(stages):
    x = 0.8 + i * 3.1
    shape = slide.shapes.add_shape(1, Inches(x), Inches(1.6), Inches(2.8), Inches(3.5))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    add_text(slide, x + 0.2, 1.7, 2.4, 0.4, stage, 14, ACCENT_CYAN, True, PP_ALIGN.CENTER)
    add_text(slide, x + 0.2, 2.1, 2.4, 0.4, title, 18, TEXT_WHITE, True, PP_ALIGN.CENTER)
    add_text(slide, x + 0.2, 2.7, 2.4, 2.0, desc, 12, TEXT_LIGHT, False, PP_ALIGN.CENTER)

add_text(slide, 0.8, 5.5, 11, 0.5, "工具链依赖", 18, ACCENT_GREEN, True)
add_bullet_slide(slide, 0.8, 6.1, 11, 1.2, [
    "RDKit (分子处理) | PubChem REST API (数据获取) | MinerU (PDF 解析) | MolScribe/DECIMER (图片识别) | ChemDataExtractor (NER)",
], 13)

# ================================================================
# Slide 6: MinerU 集成
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "MinerU 工具链集成", 32, ACCENT_CYAN, True)

tools = [
    ("MinerU API", "REST API 批量解析论文\n提取分子结构图和活性数据表格\n异步任务模式，支持大规模处理"),
    ("MinerU Open Source", "magic-pdf 本地解析\nMarkdown + 图片 + 表格输出\nCPU/GPU 双模式支持"),
    ("MinerU Skills", "化学结构提取技能\n分子图原子-化学键映射\n反应方程式识别"),
    ("MinerU Online", "mineru.net 网页端\n快速解析特定论文\n支持多种文档格式"),
]

for i, (tool, desc) in enumerate(tools):
    y = 1.5 + i * 1.4
    shape = slide.shapes.add_shape(1, Inches(0.8), Inches(y), Inches(2.5), Inches(1.1))
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT_BLUE
    shape.line.fill.background()
    add_text(slide, 0.9, y + 0.15, 2.3, 0.8, tool, 16, ACCENT_CYAN, True, PP_ALIGN.CENTER)
    add_text(slide, 3.6, y + 0.1, 8.5, 1.0, desc, 13, TEXT_LIGHT)

add_text(slide, 0.8, 6.5, 11, 0.5, "✓ 120/120 条数据记录均包含 MinerU 使用记录，覆盖率 100%", 16, ACCENT_GREEN, True)

# ================================================================
# Slide 7: 数据样例
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "数据样例：Aspirin (MOL-000001)", 28, ACCENT_CYAN, True)

# Left: molecule info
add_text(slide, 0.8, 1.5, 6, 0.4, "分子标识", 18, ACCENT_GREEN, True)
add_bullet_slide(slide, 0.8, 2.0, 6, 2.0, [
    "SMILES: CC(=O)OC1=CC=CC=C1C(=O)O",
    "IUPAC: 2-acetyloxybenzoic acid",
    "PubChem CID: 2244 | CAS: 50-78-2",
    "MW: 180.16 | LogP: 1.19 | TPSA: 63.6",
    "2D图 ✓ | 3D SDF ✓ | MinerU ✓",
], 13)

add_text(slide, 0.8, 4.2, 6, 0.4, "实体关系", 18, ACCENT_GREEN, True)
add_bullet_slide(slide, 0.8, 4.7, 6, 2.0, [
    "Aspirin → inhibits → COX-1 (conf: 0.99)",
    "Aspirin → inhibits → COX-2 (conf: 0.99)",
    "Aspirin → metabolized_to → salicylic acid",
    "Aspirin → has_substructure → benzoic acid",
], 13)

# Right: text description
add_text(slide, 7.0, 1.5, 5.5, 0.4, "科学文本描述", 18, ACCENT_GREEN, True)
add_bullet_slide(slide, 7.0, 2.0, 5.5, 4.5, [
    "[EN] Aspirin, also known as acetylsalicylic acid, is a NSAID used to reduce pain, fever, and inflammation...",
    "",
    "[ZH] 阿司匹林（乙酰水杨酸）是非甾体抗炎药的代表药物，通过不可逆地乙酰化COX酶...",
    "",
    "• 来源: PubChem CID 2244 + 手工整理",
    "• 支持中英文双语",
    "• 可直接用于 LLM 训练/评测",
], 13)

# ================================================================
# Slide 8: 五维评分
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 0.8, 0.4, 11, 0.8, "竞赛评审维度对标", 32, ACCENT_CYAN, True)

dims = [
    ("跨模态理解 (20)", "五模态对齐 + 实体关系图谱 + 中英双语", "14-16"),
    ("创新性 (15)", "「分子实体中心」范式 + 26 类药物覆盖", "10-12"),
    ("AI-Ready (30)", "严格 JSON Schema + 100% 验证 + LLM 可用", "18-22"),
    ("工程质量 (20)", "全自动 Pipeline + MinerU 四模式集成", "14-16"),
    ("开放共享 (15)", "GitHub + CC-BY-4.0 + 完整文档", "8-10"),
]

for i, (dim, support, score) in enumerate(dims):
    y = 1.6 + i * 1.1
    add_text(slide, 0.8, y, 3.5, 0.4, dim, 16, TEXT_WHITE, True)
    add_text(slide, 4.5, y, 6, 0.4, support, 13, TEXT_LIGHT)
    add_text(slide, 11.0, y, 1.5, 0.4, score, 18, HIGHLIGHT, True, PP_ALIGN.CENTER)

add_text(slide, 0.8, 7.0, 11, 0.4, "预估总分: 64-76 / 100", 20, ACCENT_CYAN, True, PP_ALIGN.CENTER)

# ================================================================
# Slide 9: Summary
# ================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_text(slide, 1, 1.0, 11, 1.0, "MolAlign 数据集", 44, ACCENT_CYAN, True, PP_ALIGN.CENTER)
add_text(slide, 1, 2.2, 11, 0.6, "面向 AI4S 的分子跨模态对齐数据集", 24, TEXT_WHITE, False, PP_ALIGN.CENTER)

add_bullet_slide(slide, 2, 3.3, 9, 3.0, [
    "🔬 120 个分子 · 26 个药物类别 · 五模态对齐",
    "🧬 中英双语科学文本 · 实体关系图谱",
    "🤖 严格 JSON Schema · 100% 自动化验证",
    "📐 RDKit 2D/3D 结构 · PubChem 公共数据溯源",
    "📦 MinerU 四种工具链全覆盖",
    "📄 完整技术报告 · 开源代码 · 可复现 Pipeline",
], 18, TEXT_WHITE)

add_text(slide, 1, 6.3, 11, 0.5, "https://github.com/CacinieP/MinerU-AGI4S-Track1", 16, ACCENT_GREEN, False, PP_ALIGN.CENTER)
add_text(slide, 1, 6.9, 11, 0.4, "开源协议: CC-BY-4.0 | 数据范式: Sci-Align", 14, TEXT_LIGHT, False, PP_ALIGN.CENTER)

# Save
output_path = "docs/MolAlign_Competition_PPT.pptx"
os.makedirs("docs", exist_ok=True)
prs.save(output_path)
print(f"PPT saved: {output_path}")
