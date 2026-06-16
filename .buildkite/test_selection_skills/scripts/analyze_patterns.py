#!/usr/bin/env python3
"""Analyze evaluation results across PRs to find miss patterns and suggest rules.

Reads all evaluation_report.json files under the evaluation/ directory,
cross-references with changed_files.txt from each PR's replay inputs, then
outputs a pattern report and suggested additions to test_selection_rules.md.

Usage:
    python analyze_patterns.py [--eval-dir <dir>] [--replay-dir <dir>] [--output <file>]
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def top_dir(path: str) -> str:
    """Return the top-level directory of a test or source path."""
    p = path.replace("\\", "/").split("::")[0]   # strip ::test_fn
    p = p.removeprefix("tests/")
    return p.split("/")[0]


def source_area(path: str) -> str:
    """Return the top-level source area of a changed file (e.g. vllm/model_executor → model_executor)."""
    p = path.replace("\\", "/")
    p = p.removeprefix("vllm/")
    return p.split("/")[0]


def load_pr(pr_dir: Path, replay_base: Path) -> dict | None:
    report_path = pr_dir / "evaluation_report.json"
    if not report_path.exists():
        return None

    report = json.loads(report_path.read_text())
    pr_number = pr_dir.name.removeprefix("pr_")

    changed_files_path = replay_base / f"pr_{pr_number}" / "inputs" / "changed_files.txt"
    changed_files = []
    if changed_files_path.exists():
        changed_files = [
            l.strip() for l in changed_files_path.read_text().splitlines()
            if l.strip() and not l.startswith("#")
        ]

    return {
        "pr_number": pr_number,
        "summary": report.get("summary", {}),
        "false_negatives": report.get("false_negative_details", []),
        "false_positives": report.get("false_positive_details", []),
        "true_positives": report.get("true_positive_details", []),
        "changed_files": changed_files,
    }


# ---------------------------------------------------------------------------
# Pattern analysis
# ---------------------------------------------------------------------------

def analyze(pr_data: list[dict]) -> dict:
    """
    For every (source_area, missed_test_dir) pair across all PRs, count how
    often the LLM missed that test area when that source area was modified.
    Also count how often it was covered (to compute a miss rate).
    """
    # miss_counts[source_area][test_dir] = list of PR numbers where it was missed
    miss_counts: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    # cover_counts[source_area][test_dir] = list of PR numbers where it was covered
    cover_counts: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))

    for pr in pr_data:
        pr_num = pr["pr_number"]
        src_areas = {source_area(f) for f in pr["changed_files"] if f.startswith("vllm/")}
        missed_dirs = {top_dir(fn["failed_test"]) for fn in pr["false_negatives"] if fn.get("failed_test")}
        caught_dirs = {top_dir(tp["matched_failure"]) for tp in pr["true_positives"] if tp.get("matched_failure")}

        for src in src_areas:
            for d in missed_dirs:
                miss_counts[src][d].append(pr_num)
            for d in caught_dirs:
                cover_counts[src][d].append(pr_num)

    return {"miss": miss_counts, "cover": cover_counts}


def suggest_rules(patterns: dict, min_occurrences: int = 1) -> list[dict]:
    """Convert pattern counts into candidate rules sorted by frequency."""
    rules = []
    miss = patterns["miss"]
    cover = patterns["cover"]

    for src, test_dirs in miss.items():
        for test_dir, prs in test_dirs.items():
            if len(prs) < min_occurrences:
                continue
            covered_prs = cover.get(src, {}).get(test_dir, [])
            total = len(prs) + len(covered_prs)
            miss_rate = len(prs) / total if total else 1.0
            rules.append({
                "source_area": src,
                "missed_test_dir": test_dir,
                "miss_count": len(prs),
                "total_prs": total,
                "miss_rate": miss_rate,
                "prs": sorted(prs),
            })

    return sorted(rules, key=lambda r: (-r["miss_rate"], -r["miss_count"]))


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def render_report(pr_data: list[dict], rules: list[dict]) -> str:
    n = len(pr_data)
    lines = [
        f"# Test Selection Pattern Analysis",
        f"",
        f"Evaluated **{n} PR(s)**.",
        f"",
    ]

    # Per-PR summary table
    lines += [
        "## Per-PR Summary",
        "",
        "| PR | Recall | Precision | TP | FN | FP |",
        "|----|--------|-----------|----|----|-----|",
    ]
    for pr in pr_data:
        s = pr["summary"]
        lines.append(
            f"| #{pr['pr_number']} "
            f"| {s.get('coverage_rate', 0):.0%} "
            f"| {s.get('precision_rate', 0):.0%} "
            f"| {s.get('true_positives', 0)} "
            f"| {s.get('false_negatives', 0)} "
            f"| {s.get('false_positives', 0)} |"
        )
    lines.append("")

    # Miss patterns
    lines += [
        "## Miss Patterns",
        "",
        "When code in a source area changes, which test directories were missed?",
        "",
        "| Source area changed | Test dir missed | Miss rate | PRs |",
        "|---------------------|-----------------|-----------|-----|",
    ]
    if rules:
        for r in rules:
            pr_list = ", ".join(f"#{p}" for p in r["prs"])
            lines.append(
                f"| `vllm/{r['source_area']}/` "
                f"| `tests/{r['missed_test_dir']}/` "
                f"| {r['miss_rate']:.0%} ({r['miss_count']}/{r['total_prs']}) "
                f"| {pr_list} |"
            )
    else:
        lines.append("| — | No patterns found yet | — | — |")
    lines.append("")

    # Suggested rules
    lines += [
        "## Suggested Rule Additions",
        "",
        "Add these to `test_selection_rules.md` once patterns are confirmed",
        "across enough PRs (aim for ≥3 occurrences before hardening a rule).",
        "",
    ]
    if rules:
        for r in rules:
            confidence = "⚠️ weak" if r["miss_count"] < 3 else "✅ strong"
            pr_list = ", ".join(f"#{p}" for p in r["prs"])
            lines += [
                f"### Rule: `vllm/{r['source_area']}/` → `tests/{r['missed_test_dir']}/`",
                f"",
                f"**Confidence**: {confidence} ({r['miss_count']} occurrence(s) across {r['total_prs']} PR(s): {pr_list})",
                f"",
                f"```",
                f"When any file under vllm/{r['source_area']}/ changes,",
                f"always include tests/{r['missed_test_dir']}/ in the test selection.",
                f"```",
                f"",
            ]
    else:
        lines += ["No patterns to suggest yet — run more PR evaluations.", ""]

    lines += ["---", f"*Run more PR evaluations to strengthen or refute these patterns.*", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze evaluation results across PRs")
    parser.add_argument("--eval-dir", default=".buildkite/test_selection_skills/evaluation")
    parser.add_argument("--replay-dir", default=".buildkite/test_selection_skills/replay")
    parser.add_argument("--output", default=None, help="Write report to file instead of stdout")
    parser.add_argument("--min-occurrences", type=int, default=1,
                        help="Minimum times a pattern must appear to be reported (default: 1)")
    args = parser.parse_args()

    eval_base = Path(args.eval_dir)
    replay_base = Path(args.replay_dir)

    pr_dirs = sorted(d for d in eval_base.iterdir() if d.is_dir() and d.name.startswith("pr_"))
    if not pr_dirs:
        print(f"No PR evaluation directories found under {eval_base}", file=sys.stderr)
        return 1

    pr_data = []
    for pr_dir in pr_dirs:
        data = load_pr(pr_dir, replay_base)
        if data:
            pr_data.append(data)
            print(f"  Loaded PR #{data['pr_number']}: "
                  f"FN={len(data['false_negatives'])}, "
                  f"FP={len(data['false_positives'])}, "
                  f"changed_files={len(data['changed_files'])}",
                  file=sys.stderr)

    if not pr_data:
        print("No valid evaluation reports found.", file=sys.stderr)
        return 1

    patterns = analyze(pr_data)
    rules = suggest_rules(patterns, min_occurrences=args.min_occurrences)
    report = render_report(pr_data, rules)

    if args.output:
        Path(args.output).write_text(report)
        print(f"Report written to: {args.output}", file=sys.stderr)
    else:
        print(report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
