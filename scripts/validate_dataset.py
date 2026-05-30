"""
数据集验证 + 统计报告生成
==========================

用法:
    python scripts/validate_dataset.py --input data/processed/molalign_dataset.jsonl
    python scripts/validate_dataset.py --input data/processed/molalign_dataset.jsonl --report docs/validation_report.json
"""

import os
import sys
import json
import argparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alignment_validator import AlignmentValidator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to JSONL dataset")
    parser.add_argument("--report", default=None, help="Path to save validation report")
    args = parser.parse_args()

    # Load records
    records = []
    with open(args.input, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    print(f"Loaded {len(records)} records from {args.input}")

    # Validate
    validator = AlignmentValidator()
    results = validator.validate_dataset(records)

    # Print summary
    print(f"\n{'='*60}")
    print(f"Validation Report")
    print(f"{'='*60}")
    print(f"  Total:     {results['total']}")
    print(f"  Valid:     {results['valid']}")
    print(f"  Invalid:   {results['invalid']}")
    print(f"  Pass rate: {results['valid']/max(results['total'],1)*100:.1f}%")
    print(f"\n  Statistics:")
    stats = results["statistics"]
    print(f"    Avg descriptions:    {stats['avg_descriptions']}")
    print(f"    Avg relations:       {stats['avg_relations']}")
    print(f"    With paper image:    {stats['with_paper_image']}")
    print(f"    With experimental:   {stats['with_experimental_data']}")
    print(f"    With MinerU usage:   {stats['mineru_used_count']}")

    if results["errors"]:
        print(f"\n  Errors ({len(results['errors'])} records):")
        for rid, errs in list(results["errors"].items())[:10]:
            print(f"    {rid}: {'; '.join(errs[:3])}")

    if results["warnings"]:
        print(f"\n  Warnings ({len(results['warnings'])} records):")
        warning_types = {}
        for rid, warns in results["warnings"].items():
            for w in warns:
                key = w.split(":")[0] if ":" in w else w[:40]
                warning_types[key] = warning_types.get(key, 0) + 1
        for wt, count in sorted(warning_types.items(), key=lambda x: -x[1]):
            print(f"    {wt}: {count}x")

    # Save report
    report_path = args.report or args.input.replace(".jsonl", "_validation.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n  Report saved: {report_path}")

    return results


if __name__ == "__main__":
    main()
