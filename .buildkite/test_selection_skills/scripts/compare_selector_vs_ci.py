#!/usr/bin/env python3
"""Compare LLM selector predictions against actual CI failures (Lane 3).

Usage:
    python compare_selector_vs_ci.py <pr_number> --ci-evidence <path> --selector-replay <path>
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False

# Colors
GREEN_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
RED_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
YELLOW_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
HEADER_FILL = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True)


def load_json(path: str) -> dict:
    """Load JSON from a file."""
    try:
        return json.loads(Path(path).read_text())
    except Exception as e:
        print(f"Error loading {path}: {e}", file=sys.stderr)
        return {}


def classify_selections(selected_tests: list[dict], failed_tests: list[dict]) -> tuple[list, list, list]:
    """Classify into true positives, false negatives, false positives.

    A selected test matches a failure if:
    - Exact match: same test file and function
    - File match: selected test file contains the failed test function
    - Directory match: selected directory contains the failed test file
    """
    true_positives, false_negatives, false_positives = [], [], []
    matched = set()

    def test_matches(sel_id: str, fail_id: str) -> bool:
        """Check if selected test matches a failure."""
        sel = sel_id.rstrip("/")
        fail = fail_id.rstrip("/")

        # Exact match
        if sel == fail:
            return True

        # Selected is directory containing failed test
        if sel_id.endswith("/"):
            if fail.startswith(sel) or fail.startswith(sel.rstrip("/")):
                return True

        # Selected file contains failed function (e.g., test_file.py matches test_file.py::test_fn)
        if "::" in fail_id:
            fail_file = fail_id.split("::")[0]
            if sel == fail_file or sel.endswith("/" + fail_file.split("/")[-1]):
                return True

        # Directory containment (selected dir is parent of failed file)
        sel_parts = sel.replace("\\", "/").split("/")
        fail_parts = fail.replace("\\", "/").split("/")
        if len(sel_parts) < len(fail_parts):
            if fail_parts[:len(sel_parts)] == sel_parts:
                return True

        return False

    for selected in selected_tests:
        sel_id = selected.get("identifier", "")
        found = False
        for i, failed in enumerate(failed_tests):
            fail_id = failed.get("identifier", "")
            if test_matches(sel_id, fail_id):
                found = True
                matched.add(i)
                true_positives.append({"selected_test": sel_id, "matched_failure": fail_id, "reason": selected.get("reason", "")})
                break
        if not found:
            false_positives.append({"selected_test": sel_id, "reason": selected.get("reason", "")})

    for i, failed in enumerate(failed_tests):
        if i not in matched:
            false_negatives.append({
                "failed_test": failed.get("identifier", ""),
                "job_name": failed.get("job_name", ""),
                "why_missed": "not_in_candidate_mapping"
            })

    return true_positives, false_negatives, false_positives


def compute_metrics(tp: list, fn: list, fp: list) -> dict:
    """Compute evaluation metrics."""
    coverage = len(tp) / (len(tp) + len(fn)) if (tp or fn) else 1.0
    precision = len(tp) / (len(tp) + len(fp)) if (tp or fp) else 1.0
    return {
        "true_positives": len(tp), "false_negatives": len(fn), "false_positives": len(fp),
        "coverage_rate": round(coverage, 3), "precision_rate": round(precision, 3),
    }



def generate_excel(pr_number: str, ci_evidence: dict, selector_replay: dict, buildkite_jobs: list,
                   metrics: dict, tp: list, fn: list, fp: list) -> bytes:
    """Generate Excel file with 2 sheets."""
    if not OPENPYXL_AVAILABLE:
        return None

    wb = Workbook()

    # Sheet 1: Lane Comparison
    ws1 = wb.active
    ws1.title = "Lane Comparison"
    ws1.append(["Category", "Test/Job", "Source", "Selected?", "Failed?", "Reason"])
    for c in ws1[1]:
        c.fill = HEADER_FILL
        c.font = HEADER_FONT

    row = 2
    for t in tp:
        ws1.append(["TRUE POSITIVE", t['selected_test'], "Both", "YES", "YES", t.get('reason', '')])
        for c in ws1[row]:
            c.fill = GREEN_FILL
        row += 1

    for f in fn:
        ws1.append(["FALSE NEGATIVE", f['failed_test'], "CI Only", "NO", "YES", f.get('why_missed', '')])
        for c in ws1[row]:
            c.fill = RED_FILL
        row += 1

    for f in fp:
        ws1.append(["FALSE POSITIVE", f['selected_test'], "LLM Only", "YES", "NO", f.get('reason', '')])
        for c in ws1[row]:
            c.fill = YELLOW_FILL
        row += 1

    # Sheet 2: Buildkite CI Tests
    ws2 = wb.create_sheet(title="Buildkite CI Tests")
    ws2.append(["Job Name", "State", "Failed?", "Exit Status"])
    for c in ws2[1]:
        c.fill = HEADER_FILL
        c.font = HEADER_FONT

    for job in buildkite_jobs:
        if job.get('state') == 'blocked':
            continue
        state = job.get('state', 'unknown').upper()
        failed = "YES" if state == "FAILED" else "NO"
        ws2.append([job.get('name', ''), state, failed, job.get('exit_status', 'N/A')])
        if state == "FAILED":
            for c in ws2[ws2.max_row]:
                c.fill = RED_FILL
        else:
            for c in ws2[ws2.max_row]:
                c.fill = GREEN_FILL

    from io import BytesIO
    out = BytesIO()
    wb.save(out)
    out.seek(0)
    return out.read()


def main():
    parser = argparse.ArgumentParser(description="Compare LLM selector vs CI failures")
    parser.add_argument("pr_number", type=str)
    parser.add_argument("--ci-evidence", required=True)
    parser.add_argument("--selector-replay", required=True)
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    pr_number = args.pr_number
    now = datetime.now(timezone.utc)

    print(f"Comparing selector vs CI for PR #{pr_number}...", file=sys.stderr)

    # Load inputs
    ci_evidence = load_json(args.ci_evidence)
    selector_replay = load_json(args.selector_replay)

    if not ci_evidence or not selector_replay:
        print("Error: Could not load inputs", file=sys.stderr)
        sys.exit(1)

    # Extract data
    # Use failed_test_list (individual tests with identifier field), not jobs_failed (job-level)
    failed_tests = ci_evidence.get("failed_test_list", [])
    selected_tests = selector_replay.get("llm_selected_tests", [])

    # Classify
    tp, fn, fp = classify_selections(selected_tests, failed_tests)
    metrics = compute_metrics(tp, fn, fp)

    # Output dir
    output_dir = Path(args.output_dir) if args.output_dir else Path(f".buildkite/test_selection_skills/evaluation/pr_{pr_number}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write evaluation report
    report = {
        "pr_number": pr_number,
        "evaluation_status": "success",
        "summary": metrics,
        "true_positive_details": tp,
        "false_negative_details": fn,
        "false_positive_details": fp,
        "notes": [f"Generated on {now.isoformat()}"],
    }
    (output_dir / "evaluation_report.json").write_text(json.dumps(report, indent=2))

    # Write report.md — single output file (follows report.template.md structure)
    builds = ci_evidence.get('buildkite_builds', [])
    # Prefer the main vllm/ci pipeline build over subsidiary pipelines (e.g. intel-ci)
    main_build = next(
        (b for b in builds if b.get('pipeline', '').rstrip('/') == '/ci'),
        builds[0] if builds else {}
    )
    build_number = main_build.get('build_number', 'unknown')
    build_url = f"https://buildkite.com/vllm/ci/builds/{build_number}" if build_number != 'unknown' else ""

    # Group failures by job for use in multiple sections
    tests_by_job: dict = {}
    for t in failed_tests:
        tests_by_job.setdefault(t.get('job_name', 'Unknown Job'), []).append(
            t.get('identifier', t.get('test_name', '')))

    summary_stats = ci_evidence.get('summary_stats', {})
    jobs_run = ci_evidence.get('jobs_run', [])
    n_passed_jobs = sum(1 for j in jobs_run if j.get('state') == 'passed')
    n_failed_jobs = sum(1 for j in jobs_run if j.get('state') == 'failed')
    n_blocked_jobs = sum(1 for j in jobs_run if j.get('state') == 'blocked')

    report_md = f"# PR #{pr_number} — Test Selection Evaluation\n\n"
    report_md += f"> **Build**: [{build_number}]({build_url}) · **Date**: {now.strftime('%Y-%m-%d')}\n\n"

    # --- Metrics ---
    report_md += "## Metrics\n\n"
    report_md += "| Metric | Value |\n|--------|-------|\n"
    report_md += f"| **Recall** | **{metrics['coverage_rate']:.1%}** |\n"
    report_md += f"| **Precision** | **{metrics['precision_rate']:.1%}** |\n"
    report_md += f"| True Positives | {len(tp)} |\n"
    report_md += f"| False Negatives (CI failed, LLM missed) | {len(fn)} |\n"
    report_md += f"| False Positives (LLM selected, passed) | {len(fp)} |\n\n"

    # --- Full CI picture ---
    report_md += "## CI Test Results\n\n"

    if summary_stats:
        total = summary_stats.get('failed', 0) + summary_stats.get('passed', 0) + summary_stats.get('skipped', 0)
        report_md += (f"| Failed | Passed | Skipped | Total |\n"
                      f"|--------|--------|---------|-------|\n"
                      f"| {summary_stats.get('failed', '?')} "
                      f"| {summary_stats.get('passed', '?')} "
                      f"| {summary_stats.get('skipped', '?')} "
                      f"| {total} |\n\n")

    if jobs_run:
        report_md += (f"**CI jobs:** {n_passed_jobs} passed · "
                      f"{n_failed_jobs} failed · {n_blocked_jobs} blocked\n\n")

    # Per-job breakdown: failed jobs with named tests, passing jobs summarised
    if tests_by_job:
        report_md += "### Failed jobs\n\n"
        for job_name, job_tests in tests_by_job.items():
            report_md += f"**❌ {job_name}** — {len(job_tests)} test(s) failed\n\n"
            for test in job_tests:
                report_md += f"- `{test}`\n"
            report_md += "\n"

    # Passing jobs that are relevant (non-blocked, non-empty name)
    passing_jobs = [j for j in jobs_run
                    if j.get('state') == 'passed' and j.get('name', '').strip()]
    if passing_jobs:
        report_md += "### Passing jobs\n\n"
        for j in passing_jobs:
            report_md += f"- ✅ {j['name']}\n"
        report_md += "\n"

    # --- LLM selections ---
    report_md += f"## LLM Selections — {len(selected_tests)} target(s)\n\n"
    report_md += "| | Target | Reason |\n|--|--------|--------|\n"
    for t in selected_tests:
        caught = any(tp_item['selected_test'] == t.get('identifier') for tp_item in tp)
        status = "✅" if caught else "➖"
        report_md += f"| {status} | `{t.get('identifier', '')}` | {t.get('reason', '')} |\n"
    report_md += "\n"

    # --- Gap analysis (auto-derived from test paths) ---
    report_md += "## Gap Analysis\n\n"
    if fn:
        # Extract top-level test directory from a test path
        def top_dir(path: str) -> str:
            p = path.replace("\\", "/").split("::")[0]  # strip ::test_fn
            p = p.removeprefix("tests/")
            return p.split("/")[0]

        failed_dirs = {top_dir(f.get('failed_test', '')) for f in fn if f.get('failed_test')}
        selected_dirs = {top_dir(t.get('identifier', '')) for t in selected_tests if t.get('identifier')}

        missed_dirs = failed_dirs - selected_dirs

        report_md += "**Why the LLM missed:**\n"
        if missed_dirs:
            report_md += (f"- LLM selections covered `{'`, `'.join(sorted(selected_dirs))}` "
                          f"but failures occurred in `{'`, `'.join(sorted(missed_dirs))}`\n")
        for f in fn:
            test = f.get('failed_test', '')
            job = f.get('job_name', '')
            report_md += f"- `{test}` (job: {job}) was not covered by any selection\n"

        report_md += "\n**To improve coverage:**\n"
        for d in sorted(missed_dirs):
            report_md += f"- Add `tests/{d}/` (or relevant sub-paths) to selections when related code changes\n"
        report_md += "\n"
    else:
        report_md += "LLM caught all CI failures — no gap to analyse.\n\n"

    report_md += f"---\n*Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}*\n"

    (output_dir / "report.md").write_text(report_md)

    print(f"Coverage: {metrics['coverage_rate']:.1%}, Precision: {metrics['precision_rate']:.1%}", file=sys.stderr)
    print(f"TP: {len(tp)}, FN: {len(fn)}, FP: {len(fp)}", file=sys.stderr)
    print(f"Generated comprehensive reports in: {output_dir}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
