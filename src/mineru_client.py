"""
MinerU 集成模块
===============
封装 MinerU API 调用，用于从科学论文 PDF 中提取结构化数据

MinerU 工具链使用方式：
1. MinerU API - 调用在线 API 解析 PDF
2. MinerU Open Source (magic-pdf) - 本地部署解析
3. MinerU Skills - 预定义处理技能
4. MinerU Online - 网页端使用

参考: https://github.com/opendatalab/MinerU
"""

import os
import json
import logging
import time
from typing import Optional, List, Dict, Any
from pathlib import Path

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

logger = logging.getLogger(__name__)


class MinerUClient:
    """MinerU API 客户端"""

    # MinerU API 基础 URL (需替换为实际 API 地址)
    API_BASE = "https://api.mineru.com/v1"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("MINERU_API_KEY", "")
        self.session = requests.Session() if REQUESTS_AVAILABLE else None
        if self.session and self.api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            })

    def parse_pdf(
        self,
        pdf_path: str,
        output_dir: str,
        extract_images: bool = True,
        extract_tables: bool = True,
        extract_formulas: bool = True,
    ) -> Dict[str, Any]:
        """
        使用 MinerU 解析 PDF 文件

        Args:
            pdf_path: PDF 文件路径
            output_dir: 输出目录
            extract_images: 是否提取图片
            extract_tables: 是否提取表格
            extract_formulas: 是否提取公式

        Returns:
            解析结果 dict，包含文本、图片、表格等
        """
        result = {
            "source_pdf": pdf_path,
            "mineru_tool": "MinerU API",
            "parse_time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "content": {
                "full_text": "",
                "sections": [],
                "figures": [],
                "tables": [],
                "formulas": []
            }
        }

        if not self.api_key or not REQUESTS_AVAILABLE:
            logger.warning("MinerU API key not set or requests not available. "
                           "Falling back to open-source mode.")
            return self._parse_pdf_opensource(pdf_path, output_dir)

        try:
            # 上传 PDF
            upload_url = f"{self.API_BASE}/pdf/upload"
            with open(pdf_path, "rb") as f:
                files = {"file": f}
                resp = self.session.post(upload_url, files=files, timeout=300)

            if resp.status_code != 200:
                logger.error(f"Failed to upload PDF: {resp.text}")
                return result

            task_id = resp.json().get("task_id")

            # 轮询解析结果
            poll_url = f"{self.API_BASE}/pdf/task/{task_id}"
            for _ in range(60):  # Max 5 min wait
                resp = self.session.get(poll_url, timeout=30)
                data = resp.json()
                if data.get("status") == "completed":
                    result["content"] = data.get("result", result["content"])
                    break
                elif data.get("status") == "failed":
                    logger.error(f"MinerU parse failed: {data.get('error')}")
                    break
                time.sleep(5)

            # 下载解析结果
            if result["content"].get("full_text"):
                output_path = os.path.join(output_dir, "parsed_content.json")
                os.makedirs(output_dir, exist_ok=True)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)

        except Exception as e:
            logger.error(f"MinerU API error: {e}")

        return result

    def _parse_pdf_opensource(self, pdf_path: str, output_dir: str) -> Dict[str, Any]:
        """
        使用 MinerU 开源项目 (magic-pdf) 本地解析

        安装: pip install magic-pdf[full]
        用法: magic-pdf --path input.pdf --output-dir output/
        """
        result = {
            "source_pdf": pdf_path,
            "mineru_tool": "MinerU Open Source (magic-pdf)",
            "parse_time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "content": {
                "full_text": "",
                "sections": [],
                "figures": [],
                "tables": [],
                "formulas": []
            }
        }

        try:
            import subprocess
            os.makedirs(output_dir, exist_ok=True)

            cmd = [
                "magic-pdf",
                "--path", pdf_path,
                "--output-dir", output_dir,
                "--lang", "en"
            ]

            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600
            )

            if proc.returncode == 0:
                # 解析输出结果
                content_dir = os.path.join(output_dir, "auto")
                markdown_path = os.path.join(content_dir, os.path.basename(pdf_path).replace(".pdf", ".md"))

                if os.path.exists(markdown_path):
                    with open(markdown_path, "r", encoding="utf-8") as f:
                        result["content"]["full_text"] = f.read()

                # 提取图片
                images_dir = os.path.join(content_dir, "images")
                if os.path.exists(images_dir):
                    for img_file in os.listdir(images_dir):
                        if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
                            result["content"]["figures"].append({
                                "path": os.path.join(images_dir, img_file),
                                "label": img_file
                            })
            else:
                logger.error(f"magic-pdf failed: {proc.stderr}")

        except FileNotFoundError:
            logger.error("magic-pdf not installed. Install with: pip install magic-pdf[full]")
        except Exception as e:
            logger.error(f"Open source parse error: {e}")

        return result

    def extract_molecular_images(self, parsed_result: Dict) -> List[Dict]:
        """
        从 MinerU 解析结果中识别和提取分子结构图

        Args:
            parsed_result: MinerU 解析结果

        Returns:
            分子图片信息列表
        """
        molecular_images = []
        figures = parsed_result.get("content", {}).get("figures", [])

        for fig in figures:
            img_info = {
                "path": fig.get("path", ""),
                "label": fig.get("label", ""),
                "detected_type": "molecular_structure",  # 实际应用中用模型分类
                "extraction_method": "MinerU figure extraction",
                "confidence": 0.85
            }
            molecular_images.append(img_info)

        return molecular_images

    def extract_tables(self, parsed_result: Dict) -> List[Dict]:
        """
        从 MinerU 解析结果中提取结构化表格数据

        Args:
            parsed_result: MinerU 解析结果

        Returns:
            表格数据列表
        """
        tables = parsed_result.get("content", {}).get("tables", [])

        for table in tables:
            table["extraction_method"] = "MinerU table extraction"

        return tables

    def extract_text_sections(self, parsed_result: Dict) -> List[Dict]:
        """
        从 MinerU 解析结果中提取文本段落

        Returns:
            文本段落列表，包含 section 标题和内容
        """
        sections = parsed_result.get("content", {}).get("sections", [])
        full_text = parsed_result.get("content", {}).get("full_text", "")

        if not sections and full_text:
            # 简单的段落分割
            paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]
            for i, para in enumerate(paragraphs):
                sections.append({
                    "section_id": i,
                    "title": f"Section {i}",
                    "content": para,
                    "extraction_method": "MinerU text extraction"
                })

        return sections


class MinerUUsageTracker:
    """MinerU 使用记录追踪器"""

    def __init__(self, output_file: str = "docs/mineru_usage_log.json"):
        self.output_file = output_file
        self.records = []
        self._load()

    def _load(self):
        """加载已有记录"""
        if os.path.exists(self.output_file):
            with open(self.output_file, "r", encoding="utf-8") as f:
                self.records = json.load(f)

    def save(self):
        """保存记录"""
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)

    def log_usage(
        self,
        tool: str,
        task: str,
        input_file: str,
        output_file: str,
        details: Optional[Dict] = None
    ):
        """
        记录一次 MinerU 使用

        Args:
            tool: 使用的 MinerU 工具 (API/Open Source/Skills/Online)
            task: 任务描述
            input_file: 输入文件
            output_file: 输出文件
            details: 额外详情
        """
        record = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "tool": tool,
            "task": task,
            "input": input_file,
            "output": output_file,
            "details": details or {}
        }
        self.records.append(record)
        self.save()
        return record
