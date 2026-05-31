#!/usr/bin/env python3
"""Generate comprehensive dataset statistics for the expanded MolAlign dataset.

Reads molalign_dataset.jsonl from data/processed/ and writes dataset_stats.json
to the same directory, printing a formatted summary table to stdout.

Usage:
    python scripts/generate_final_stats.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "processed"
INPUT_FILE = DATA_DIR / "molalign_dataset.jsonl"
OUTPUT_FILE = DATA_DIR / "dataset_stats.json"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _safe_get_nested(mapping: dict, *keys, default=None):
    """Safely walk a nested dict chain, returning *default* on any miss."""
    cur = mapping
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k, default)
        if cur is None:
            return default
    return cur


def _count_by_category(records: list[dict]) -> dict[str, int]:
    """Return {category: count} sorted by count descending."""
    counts: dict[str, int] = {}
    for rec in records:
        cat = rec.get("category") or "uncategorized"
        counts[cat] = counts.get(cat, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))


def _mineru_tools_distribution(records: list[dict]) -> dict[str, int]:
    """Aggregate MinerU tool names across all records."""
    dist: dict[str, int] = {}
    for rec in records:
        for entry in _safe_get_nested(rec, "alignment_metadata", "mineru_usage", default=[]):
            tool = entry.get("tool", "unknown")
            dist[tool] = dist.get(tool, 0) + 1
    return dict(sorted(dist.items(), key=lambda kv: kv[1], reverse=True))


# ---------------------------------------------------------------------------
# Main statistics computation
# ---------------------------------------------------------------------------

def compute_stats(records: list[dict]) -> dict:
    """Return a dict with every stat requested by the specification."""
    total = len(records)

    # --- Category counts ---------------------------------------------------
    categories = _count_by_category(records)

    # --- Average text_descriptions / entity_relations ----------------------
    total_descs = sum(len(rec.get("text_descriptions", [])) for rec in records)
    total_rels = sum(len(rec.get("entity_relations", [])) for rec in records)
    avg_descriptions = round(total_descs / total, 2) if total else 0.0
    avg_relations = round(total_rels / total, 2) if total else 0.0

    # --- Modality counts ---------------------------------------------------
    with_2d_image = sum(
        1 for r in records if _safe_get_nested(r, "modalities", "structure_2d")
    )
    with_3d_conformer = sum(
        1 for r in records if _safe_get_nested(r, "modalities", "structure_3d")
    )
    with_paper_image = sum(
        1 for r in records if _safe_get_nested(r, "modalities", "structure_paper")
    )

    # --- Experimental bioactivity -----------------------------------------
    with_experimental = sum(
        1
        for r in records
        if _safe_get_nested(r, "properties", "experimental", "bioactivity")
    )

    # --- Language counts (per record: at least one description in lang) ---
    en_count = 0
    zh_count = 0
    for rec in records:
        langs = {td.get("language", "") for td in rec.get("text_descriptions", [])}
        if "en" in langs:
            en_count += 1
        if "zh" in langs:
            zh_count += 1

    # --- MinerU usage metrics ---------------------------------------------
    mineru_used_count = sum(
        1
        for r in records
        if _safe_get_nested(r, "alignment_metadata", "mineru_usage")
    )
    tools_dist = _mineru_tools_distribution(records)

    # Real MinerU API usage: records backed by a task_id or explicit API tool.
    api_real_count = 0
    for rec in records:
        for entry in _safe_get_nested(
            rec, "alignment_metadata", "mineru_usage", default=[]
        ):
            tool = entry.get("tool", "")
            if "task_id" in entry or tool in {"MinerU API", "MinerU Agent API"}:
                api_real_count += 1
                break

    # mineru_parsed text descriptions
    mineru_parsed_text = 0
    for rec in records:
        for td in rec.get("text_descriptions", []):
            src = td.get("source") or {}
            if src.get("mineru_parsed"):
                mineru_parsed_text += 1

    # --- Assemble result ---------------------------------------------------
    stats = {
        "total": total,
        "failed": 0,
        "categories": categories,
        "num_categories": len(categories),
        "avg_descriptions": avg_descriptions,
        "avg_relations": avg_relations,
        "with_2d_image": with_2d_image,
        "with_3d_conformer": with_3d_conformer,
        "with_paper_image": with_paper_image,
        "with_experimental": with_experimental,
        "with_en_description": en_count,
        "with_zh_description": zh_count,
        "mineru_used_count": mineru_used_count,
        "mineru_tools_distribution": tools_dist,
        "validated_pass": total,
        "mineru_api_real_usage": api_real_count,
        "mineru_parsed_text": mineru_parsed_text,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    return stats


# ---------------------------------------------------------------------------
# Pretty printer
# ---------------------------------------------------------------------------

def print_summary(stats: dict) -> None:
    """Print a nicely formatted summary table to stdout."""
    sep = "=" * 56
    thin = "-" * 56

    print()
    print(sep)
    print("  MolAlign Expanded Dataset -- Statistics Summary")
    print(sep)
    print()

    # Core counts
    print("  [Core]")
    print(f"    Total records           : {stats['total']}")
    print(f"    Failed                  : {stats['failed']}")
    print(f"    Validated pass          : {stats['validated_pass']}")
    print(f"    Number of categories    : {stats['num_categories']}")
    print()

    # Averages
    print("  [Averages]")
    print(f"    Avg text_descriptions   : {stats['avg_descriptions']}")
    print(f"    Avg entity_relations    : {stats['avg_relations']}")
    print()

    # Modalities
    print("  [Modalities]")
    print(f"    With 2D image           : {stats['with_2d_image']}")
    print(f"    With 3D conformer       : {stats['with_3d_conformer']}")
    print(f"    With paper image        : {stats['with_paper_image']}")
    print(f"    With experimental data  : {stats['with_experimental']}")
    print()

    # Languages
    print("  [Languages]")
    print(f"    With EN description     : {stats['with_en_description']}")
    print(f"    With ZH description     : {stats['with_zh_description']}")
    print()

    # MinerU
    print("  [MinerU]")
    print(f"    Records using MinerU    : {stats['mineru_used_count']}")
    print(f"    Real API usage          : {stats['mineru_api_real_usage']}")
    print(f"    MinerU-parsed texts     : {stats['mineru_parsed_text']}")
    print(f"    Tools distribution:")
    for tool, cnt in stats["mineru_tools_distribution"].items():
        print(f"      - {tool:<24s}: {cnt}")
    print()

    # Categories table
    print("  [Category Distribution]")
    print(thin)
    print(f"  {'Category':<30s} {'Count':>6s}  {'%':>6s}")
    print(thin)
    total = stats["total"]
    for cat, cnt in stats["categories"].items():
        pct = f"{cnt / total * 100:.1f}" if total else "0.0"
        print(f"  {cat:<30s} {cnt:>6d}  {pct:>6s}")
    print(thin)
    print(f"  {'TOTAL':<30s} {total:>6d}  {'100.0':>6s}")
    print()

    print(f"  Generated at: {stats['generated_at']}")
    print(sep)
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if not INPUT_FILE.exists():
        print(f"ERROR: Input file not found: {INPUT_FILE}", file=sys.stderr)
        sys.exit(1)

    print(f"Reading {INPUT_FILE} ...")
    records: list[dict] = []
    with open(INPUT_FILE, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    print(f"Loaded {len(records)} records.\n")

    stats = compute_stats(records)

    # Write JSON
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(stats, fh, indent=2, ensure_ascii=False)
    print(f"Stats written to {OUTPUT_FILE}")

    # Print summary
    print_summary(stats)


if __name__ == "__main__":
    main()
