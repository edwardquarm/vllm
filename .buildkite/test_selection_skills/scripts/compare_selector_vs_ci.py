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


def generate_text_table(pr_number: str, ci_evidence: dict, selector_replay: dict, buildkite_jobs: list,
                        metrics: dict, tp: list, fn: list, fp: list) -> str:
    """Generate ASCII comparison table: CI tests run vs LLM selected."""
    lines = []
    w = 100

    # Get build number and data source info
    builds = ci_evidence.get('buildkite_builds', [])
    build_number = builds[0].get('build_number', 'unknown') if builds else 'unknown'
    data_source = "Buildkite API Logs" if any(t.get('source') == 'buildkite_logs' for t in ci_evidence.get('tests_run', [])) else "Buildkite Test Engine"

    lines.append("=" * w)
    title = f"PR #{pr_number} - TEST SELECTION COMPARISON"
    subtitle = f"(Build {build_number} - {data_source})"
    lines.append(title.center(w))
    lines.append(subtitle.center(w))
    lines.append("=" * w)
    lines.append("")

    # Summary metrics
    lines.append("┌" + "─" * (w - 2) + "┐")
    lines.append("│  SUMMARY METRICS".ljust(w - 2) + "│")
    lines.append("├" + "─" * (w - 2) + "┤")
    lines.append(f"│  Coverage (Recall):  {metrics['coverage_rate']:.1%}".ljust(w - 2) + "│")
    lines.append(f"│  Precision:          {metrics['precision_rate']:.1%}".ljust(w - 2) + "│")
    lines.append(f"│  True Positives:     {len(tp)} (LLM selected + CI failed)".ljust(w - 2) + "│")
    lines.append(f"│  False Negatives:    {len(fn)} (CI failed, LLM missed)".ljust(w - 2) + "│")
    lines.append(f"│  False Positives:    {len(fp)} (LLM selected, CI passed)".ljust(w - 2) + "│")
    lines.append("│".ljust(w - 2) + "│")
    lines.append(f"│  Data Source:        {data_source}".ljust(w - 2) + "│")
    if builds:
        build_url = f"https://buildkite.com/{builds[0].get('pipeline', '')}/builds/{build_number}"
        lines.append(f"│  Build URL:          {build_url[:70]}".ljust(w - 2) + "│")
    lines.append("└" + "─" * (w - 2) + "┘")
    lines.append("")

    # CI Approach - Tests actually run by Buildkite
    tests_run = ci_evidence.get('tests_run', [])
    tests_run_count = ci_evidence.get('tests_run_count', len(tests_run))
    failed_tests = ci_evidence.get('tests_failed', [])
    failed_jobs = ci_evidence.get('jobs_failed', [])

    lines.append("┌" + "─" * (w - 2) + "┐")
    lines.append("│  CI APPROACH (Buildkite - actual test failures from logs)".ljust(w - 2) + "│")
    lines.append("├" + "─" * (w - 2) + "┤")
    if failed_tests:
        lines.append(f"│  Total Failed Tests: {len(failed_tests)}".ljust(w - 2) + "│")
        lines.append(f"│  Failed Jobs: {len(failed_jobs)}".ljust(w - 2) + "│")
        lines.append("│".ljust(w - 2) + "│")

        # Group failures by job
        tests_by_job = {}
        for t in failed_tests:
            job_name = t.get('job_name', 'Unknown Job')
            if job_name not in tests_by_job:
                tests_by_job[job_name] = []
            test_name = t.get('test_name', t.get('identifier', ''))
            tests_by_job[job_name].append(test_name)

        for job_name, job_tests in tests_by_job.items():
            lines.append(f"│  [FAIL] {job_name} - {len(job_tests)} test(s) failed".ljust(w - 2) + "│")
            # Show first few tests from this job
            for test in job_tests[:5]:
                test_short = test[:80]
                lines.append(f"│    ✗ {test_short}".ljust(w - 2) + "│")
            if len(job_tests) > 5:
                lines.append(f"│    + {len(job_tests) - 5} more tests in this job".ljust(w - 2) + "│")
            lines.append("│".ljust(w - 2) + "│")

    elif failed_jobs:
        lines.append(f"│  Tests run: N/A (only job-level data available)".ljust(w - 2) + "│")
        lines.append(f"│  Jobs failed: {len(failed_jobs)}".ljust(w - 2) + "│")
        lines.append("│".ljust(w - 2) + "│")
        for j in failed_jobs:
            lines.append(f"│  [FAIL] {j.get('name', 'unknown')[:80]}".ljust(w - 2) + "│")
    else:
        lines.append("│  No CI test failures".ljust(w - 2) + "│")
    lines.append("└" + "─" * (w - 2) + "┘")
    lines.append("")

    # LLM Approach - Tests selected by LLM
    lines.append("┌" + "─" * (w - 2) + "┐")
    lines.append("│  LLM APPROACH (tests selected by LLM)".ljust(w - 2) + "│")
    lines.append("├" + "─" * (w - 2) + "┤")
    llm_selected = selector_replay.get('llm_selected_tests', [])
    lines.append(f"│  Total selected: {len(llm_selected)}".ljust(w - 2) + "│")
    lines.append("│".ljust(w - 2) + "│")

    # Show LLM tests with status
    if tp:
        lines.append("│  WOULD HAVE CAUGHT FAILURES:".ljust(w - 2) + "│")
        for t in tp:
            test_short = t['selected_test'][:55]
            lines.append(f"│  [✓] {test_short}".ljust(w - 2) + "│")
    if fp:
        lines.append("│  SELECTED (no failure in CI):".ljust(w - 2) + "│")
        for t in fp:
            test_short = t['selected_test'][:55]
            lines.append(f"│  [ ] {test_short}".ljust(w - 2) + "│")
    if not llm_selected:
        lines.append("│  (No tests selected by LLM)".ljust(w - 2) + "│")
    lines.append("└" + "─" * (w - 2) + "┘")
    lines.append("")

    # Comparison analysis
    lines.append("┌" + "─" * (w - 2) + "┐")
    lines.append("│  COMPARISON: CI vs LLM".ljust(w - 2) + "│")
    lines.append("├" + "─" * (w - 2) + "┤")
    if failed_tests or failed_jobs:
        if tp:
            lines.append(f"│  ✓ LLM caught {len(tp)}/{len(failed_tests) + len(failed_jobs)} failures ({metrics['coverage_rate']:.0%} coverage)".ljust(w - 2) + "│")
        if fn:
            lines.append(f"│  ✗ LLM MISSED {len(fn)} failure(s):".ljust(w - 2) + "│")
            for f in fn[:5]:
                lines.append(f"│    - {f['failed_test'][:50]}".ljust(w - 2) + "│")
        if not tp and not fn:
            lines.append(f"│  ? No overlap between LLM selection and CI failures".ljust(w - 2) + "│")
    else:
        lines.append(f"│  PR passed CI - no failures to compare".ljust(w - 2) + "│")
        lines.append(f"│  LLM selected {len(llm_selected)} tests (efficiency check only)".ljust(w - 2) + "│")
    lines.append("└" + "─" * (w - 2) + "┘")
    lines.append("")

    # Buildkite CI Jobs summary
    lines.append("┌" + "─" * (w - 2) + "┐")
    lines.append("│  BUILDKITE CI JOBS SUMMARY".ljust(w - 2) + "│")
    lines.append("├" + "─" * (w - 2) + "┤")
    passed_count = sum(1 for j in buildkite_jobs if j.get('state') == 'passed')
    failed_count = sum(1 for j in buildkite_jobs if j.get('state') == 'failed')
    blocked_count = sum(1 for j in buildkite_jobs if j.get('state') == 'blocked')
    lines.append(f"│  Passed: {passed_count} | Failed: {failed_count} | Blocked: {blocked_count}".ljust(w - 2) + "│")
    if failed_jobs:
        lines.append("│".ljust(w - 2) + "│")
        lines.append("│  Failed jobs:".ljust(w - 2) + "│")
        for j in failed_jobs:
            lines.append(f"│    ! {j.get('name', 'unknown')[:50]}".ljust(w - 2) + "│")
    lines.append("└" + "─" * (w - 2) + "┘")

    return "\n".join(lines)


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

    # Write text table
    buildkite_jobs = ci_evidence.get("jobs_run", []) + ci_evidence.get("jobs_failed", [])
    text_table = generate_text_table(pr_number, ci_evidence, selector_replay, buildkite_jobs, metrics, tp, fn, fp)
    (output_dir / "test_comparison_table.txt").write_text(text_table)

    # Write Excel
    if OPENPYXL_AVAILABLE:
        excel_data = generate_excel(pr_number, ci_evidence, selector_replay, buildkite_jobs, metrics, tp, fn, fp)
        if excel_data:
            (output_dir / f"PR{pr_number}_Comparison.xlsx").write_bytes(excel_data)

    # Write simple summary
    summary = f"# Evaluation for PR #{pr_number}\n\n"
    summary += f"Coverage: {metrics['coverage_rate']:.1%}\n\n"
    summary += f"## False Negatives ({len(fn)})\n"
    for f in fn:
        summary += f"- {f['failed_test']}\n"
    summary += f"\n## False Positives ({len(fp)})\n"
    for f in fp:
        summary += f"- {f['selected_test']}\n"
    (output_dir / "evaluation_summary.md").write_text(summary)

    # Write comprehensive SUMMARY.md
    builds = ci_evidence.get('buildkite_builds', [])
    build_number = builds[0].get('build_number', 'unknown') if builds else 'unknown'
    build_url = f"https://buildkite.com/{builds[0].get('pipeline', '')}/builds/{build_number}" if builds else ""

    comprehensive_summary = f"""# PR #{pr_number} Test Selection Evaluation - SUMMARY

## Quick Facts

| Metric | Value |
|--------|-------|
| PR Number | #{pr_number} |
| Buildkite Build | [{build_number}]({build_url}) |
| **Coverage (Recall)** | **{metrics['coverage_rate']:.1%}** |
| **Precision** | **{metrics['precision_rate']:.1%}** |
| True Positives | {len(tp)} |
| **False Negatives** | **{len(fn)}** (LLM missed) |
| False Positives | {len(fp)} (LLM selected but passed) |

## What Actually Failed ({len(failed_tests)} tests)

"""
    # Group failures by job
    tests_by_job = {}
    for t in failed_tests:
        job_name = t.get('job_name', 'Unknown Job')
        if job_name not in tests_by_job:
            tests_by_job[job_name] = []
        test_name = t.get('test_name', t.get('identifier', ''))
        tests_by_job[job_name].append(test_name)

    for job_name, job_tests in tests_by_job.items():
        comprehensive_summary += f"### ❌ {job_name}\n**{len(job_tests)} test(s) failed:**\n"
        for test in job_tests[:20]:
            comprehensive_summary += f"- `{test}`\n"
        if len(job_tests) > 20:
            comprehensive_summary += f"- ... and {len(job_tests) - 20} more\n"
        comprehensive_summary += "\n"

    comprehensive_summary += f"""## What LLM Selected ({len(selected_tests)} targets)

"""
    for t in selected_tests:
        caught = any(tp_item['selected_test'] == t.get('identifier') for tp_item in tp)
        status = "✓" if caught else " "
        comprehensive_summary += f"- [{status}] `{t.get('identifier', '')}` - {t.get('reason', '')}\n"

    comprehensive_summary += f"""
## Data Quality Note

✅ **{ci_evidence.get('status', 'unknown').upper()}** - Data extracted from Buildkite API
- Source: Build {build_number}
- Method: {"Parsed from job logs" if any(t.get('source') == 'buildkite_logs' for t in ci_evidence.get('tests_run', [])) else "Buildkite Test Engine"}

---
Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}
"""

    (output_dir / "SUMMARY.md").write_text(comprehensive_summary)

    # Write README.md
    readme = f"""# PR #{pr_number} - Test Selection Evaluation

## Files in This Directory

- **`SUMMARY.md`** - Executive summary ⭐ **START HERE**
- **`test_comparison_table.txt`** - Visual comparison
- **`evaluation_report.json`** - Machine-readable metrics
- **`evaluation_summary.md`** - Legacy summary

## Key Results

- Coverage: {metrics['coverage_rate']:.1%}
- Precision: {metrics['precision_rate']:.1%}
- Failed Tests: {len(failed_tests)}
- LLM Selections: {len(selected_tests)}

Generated: {now.strftime('%Y-%m-%d')}
"""
    (output_dir / "README.md").write_text(readme)

    print(f"Coverage: {metrics['coverage_rate']:.1%}, Precision: {metrics['precision_rate']:.1%}", file=sys.stderr)
    print(f"TP: {len(tp)}, FN: {len(fn)}, FP: {len(fp)}", file=sys.stderr)
    print(f"Generated comprehensive reports in: {output_dir}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
