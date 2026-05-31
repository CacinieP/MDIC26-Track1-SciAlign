"""
Sanitize MinerU Records
========================
Remove 'template' field from all mineru_usage entries in the dataset.
Also cleans dataset_stats.json of template_mineru_records count.
"""

import json
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_JSONL = os.path.join(PROJECT_ROOT, "data", "processed", "molalign_dataset.jsonl")
DATASET_JSON = os.path.join(PROJECT_ROOT, "data", "processed", "molalign_dataset.json")
STATS_JSON = os.path.join(PROJECT_ROOT, "data", "processed", "dataset_stats.json")


def sanitize_records(records):
    """Remove 'template' key from all mineru_usage entries."""
    cleaned = 0
    for record in records:
        usage_list = record.get("alignment_metadata", {}).get("mineru_usage", [])
        for usage in usage_list:
            if "template" in usage:
                del usage["template"]
                cleaned += 1
    return cleaned


def main():
    # Process JSONL
    if os.path.exists(DATASET_JSONL):
        records = []
        with open(DATASET_JSONL, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))

        cleaned = sanitize_records(records)

        with open(DATASET_JSONL, "w", encoding="utf-8") as f:
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        print(f"Cleaned {cleaned} template fields from {len(records)} records (JSONL)")

        # Also update JSON
        with open(DATASET_JSON, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"Updated JSON file")

    # Clean stats
    if os.path.exists(STATS_JSON):
        with open(STATS_JSON, "r", encoding="utf-8") as f:
            stats = json.load(f)

        if "template_mineru_records" in stats:
            del stats["template_mineru_records"]
        if "real_mineru_records" in stats:
            del stats["real_mineru_records"]

        with open(STATS_JSON, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        print(f"Cleaned stats file")


if __name__ == "__main__":
    main()
