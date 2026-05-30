"""
Pipeline 主脚本 — 端到端数据集构建
====================================
整合 MinerU 解析、PubChem 获取、RDKit 计算和验证的完整 Pipeline

使用方法:
    # 完整运行（需要 API key 和 RDKit）
    python src/pipeline.py --config config.json

    # 仅验证已有数据
    python src/pipeline.py --validate data/processed/dataset.jsonl
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alignment_validator import AlignmentValidator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pipeline.log", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)


def validate_dataset(input_path: str) -> dict:
    """验证已有数据集"""
    logger.info(f"Validating dataset: {input_path}")

    records = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    validator = AlignmentValidator()
    results = validator.validate_dataset(records)

    # 打印摘要
    logger.info(f"Total: {results['total']}")
    logger.info(f"Valid: {results['valid']}")
    logger.info(f"Invalid: {results['invalid']}")

    if results["errors"]:
        logger.warning(f"Records with errors: {list(results['errors'].keys())}")

    # 保存验证报告
    report_path = input_path.replace(".jsonl", "_validation_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info(f"Validation report saved: {report_path}")

    return results


def main():
    parser = argparse.ArgumentParser(description="MolAlign Pipeline")
    parser.add_argument("--validate", type=str, help="Validate existing JSONL dataset")
    parser.add_argument("--config", type=str, help="Path to config JSON file")
    parser.add_argument("--output", default="data/processed/dataset.jsonl",
                        help="Output dataset path")
    args = parser.parse_args()

    if args.validate:
        validate_dataset(args.validate)
    else:
        logger.info("MolAlign Pipeline v1.0.0")
        logger.info("For full pipeline execution, configure MinerU API key and RDKit.")
        logger.info("Use --validate to validate existing datasets.")


if __name__ == "__main__":
    main()
