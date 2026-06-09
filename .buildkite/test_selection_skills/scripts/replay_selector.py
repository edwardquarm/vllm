#!/usr/bin/env python3
"""Replay LLM test selector for a historical PR (Lane 2).

Usage:
    python replay_selector.py <pr_number> [--repo <repo>] [--output-dir <dir>]
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_gh_api(endpoint: str) -> dict:
    """Run a GitHub API call using the gh CLI."""
    cmd = ["gh", "api", endpoint]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {}


def get_pr_diff(pr_number: int, repo: str) -> str:
    """Fetch the diff for a PR."""
    cmd = ["gh", "pr", "diff", str(pr_number), "-R", repo]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else ""


def get_pr_files(pr_number: int, repo: str) -> list[dict]:
    """Fetch changed files for a PR."""
    return run_gh_api(f"repos/{repo}/pulls/{pr_number}/files")


def generate_candidate_mapping(changed_files: list[str], script_dir: Path) -> str:
    """Generate candidate test mapping using build_test_mapping.py."""
    mapping_script = script_dir.parent.parent / "scripts" / "build_test_mapping.py"
    if not mapping_script.exists():
        return "| Changed source file | Candidate test files |\n|---|---|\n| (mapping unavailable) | N/A |"

    files_csv = ",".join(f for f in changed_files if f.endswith(".py") and f.startswith("vllm/"))
    if not files_csv:
        return "| Changed source file | Candidate test files |\n|---|---|\n| (no Python files in vllm/) | N/A |"

    cmd = [sys.executable, str(mapping_script), "--files", files_csv]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else "| (mapping failed) | N/A |"


def read_test_selection_instructions(script_dir: Path) -> str:
    """Read TEST_SELECTION.md."""
    instructions_path = script_dir.parent.parent / "TEST_SELECTION.md"
    return instructions_path.read_text() if instructions_path.exists() else ""


def run_llm_selector(instructions: str, candidate_mapping: str, changed_files: list[str], diff_content: str,
                     model: str) -> str:
    """Run the LLM selector using claude CLI."""
    prompt = f"""You are selecting tests for a PR. Follow the instructions exactly.

## Instructions

{instructions}

## Candidate Tests (pre-filtered from import analysis)

{candidate_mapping}

## Changed Files

{chr(10).join(changed_files)}

## Diff Content

{diff_content}

## Your Task

Based on the instructions, candidate tests, changed files, and diff, output the test directories/files to run.
Follow ALL rules. Use the output format specified in the instructions."""

    # For large prompts, write to temp file and use @file syntax
    if len(prompt) > 50000:
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(prompt)
            prompt_file = f.name
        cmd = ["claude", "-p", "--model", model, f"@{prompt_file}"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else ""
        finally:
            import os
            os.unlink(prompt_file)
    else:
        cmd = ["claude", "-p", "--model", model, prompt]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else ""


def parse_selector_output(output: str) -> tuple[str, list[dict]]:
    """Parse LLM selector output into reasoning and test list."""
    if "---" not in output:
        return output, []

    parts = output.split("---", 1)
    reasoning = parts[0].strip()
    test_section = parts[1].strip() if len(parts) > 1 else ""

    selected_tests = []
    for line in test_section.split("\n"):
        line = line.strip()
        if "|" in line and not line.startswith("|"):
            parts = line.split("|", 1)
            if len(parts) == 2:
                test_path = parts[0].strip()
                reason = parts[1].strip()
                if test_path and test_path.upper() != "NONE":
                    selected_tests.append({
                        "identifier": test_path,
                        "granularity": "unknown",
                        "reason": reason,
                        "source": "llm_selector",
                    })

    return reasoning, selected_tests


def normalize_selector_replay(pr_number: int, repo: str, pr_details: dict, changed_files: list[str],
                              selected_tests: list[dict], notes: list[str], candidate_mapping: str = "",
                              model: str = "haiku") -> dict:
    """Normalize selector replay into standard format."""
    status = "success" if selected_tests else "partial"

    return {
        "pr_number": str(pr_number),
        "repo": repo,
        "status": status,
        "changed_files": changed_files,
        "diff_summary": f"{len(changed_files)} files changed",
        "diff_ref": pr_details.get("head", {}).get("sha", ""),
        "test_dependency_ref": "build_test_mapping.py",
        "test_selection_rules_ref": ".buildkite/TEST_SELECTION.md",
        "selector_command": f"claude -p --model {model}",
        "llm_selected_tests": selected_tests,
        "selection_reasons": [{"identifier": t["identifier"], "reason": t["reason"]} for t in selected_tests],
        "candidate_mapping": candidate_mapping,
        "total_candidates": candidate_mapping.count("`tests/") if candidate_mapping else 0,
        "notes": notes,
    }


def main():
    parser = argparse.ArgumentParser(description="Replay LLM test selector for a historical PR")
    parser.add_argument("pr_number", type=int, help="PR number to replay")
    parser.add_argument("--repo", type=str, default="vllm-project/vllm", help="Repository name")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory")
    parser.add_argument("--skip-llm", action="store_true", help="Skip LLM invocation")
    parser.add_argument("--model", type=str, default=os.environ.get("ATS_SELECTOR_MODEL", "haiku"),
                        help="Claude/LiteLLM model for selector replay")
    args = parser.parse_args()

    pr_number = args.pr_number
    repo = args.repo
    script_dir = Path(__file__).parent

    print(f"Replaying LLM selector for PR #{pr_number}...", file=sys.stderr)

    # Fetch PR details
    print(f"  Fetching PR #{pr_number} details...", file=sys.stderr)
    pr_details = run_gh_api(f"repos/{repo}/pulls/{pr_number}")
    if not pr_details:
        print(f"Error: Could not fetch PR #{pr_number}", file=sys.stderr)
        sys.exit(1)

    # Get changed files
    print("  Fetching changed files...", file=sys.stderr)
    files_data = get_pr_files(pr_number, repo)
    changed_files = [f["filename"] for f in files_data if "filename" in f]
    print(f"  Found {len(changed_files)} changed files", file=sys.stderr)

    # Get diff
    print("  Fetching diff...", file=sys.stderr)
    diff_content = get_pr_diff(pr_number, repo)
    max_diff = 51200
    if len(diff_content) > max_diff:
        diff_content = diff_content[:max_diff] + "\n\n... (truncated)"

    # Generate candidate mapping
    print("  Generating candidate mapping...", file=sys.stderr)
    candidate_mapping = generate_candidate_mapping(changed_files, script_dir)

    # Read instructions
    instructions = read_test_selection_instructions(script_dir)

    # Run LLM selector
    selector_output = ""
    reasoning = ""
    selected_tests = []

    if not args.skip_llm:
        print("  Running LLM selector...", file=sys.stderr)
        selector_output = run_llm_selector(instructions, candidate_mapping, changed_files, diff_content, args.model)
        if selector_output:
            reasoning, selected_tests = parse_selector_output(selector_output)
            print(f"  Selected {len(selected_tests)} test targets", file=sys.stderr)
    else:
        print("  Skipping LLM (--skip-llm)", file=sys.stderr)

    # Write output
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(f".buildkite/test_selection_skills/replay/pr_{pr_number}")

    output_dir.mkdir(parents=True, exist_ok=True)

    notes = [f"Replay performed on {datetime.now(timezone.utc).isoformat()}"]
    replay = normalize_selector_replay(pr_number, repo, pr_details, changed_files, selected_tests, notes,
                                       candidate_mapping, args.model)

    (output_dir / "selector_replay.json").write_text(json.dumps(replay, indent=2) + "\n")
    print(f"  Replay written to: {output_dir / 'selector_replay.json'}", file=sys.stderr)

    # Write inputs
    inputs_dir = output_dir / "inputs"
    inputs_dir.mkdir(parents=True, exist_ok=True)
    (inputs_dir / "changed_files.txt").write_text("\n".join(changed_files) + "\n")
    (inputs_dir / "diff.patch").write_text(diff_content)
    (inputs_dir / "candidate_mapping.md").write_text(candidate_mapping)
    if instructions:
        (inputs_dir / "test_selection_rules.md").write_text(instructions)
    if selector_output:
        (inputs_dir / "raw_selector_output.txt").write_text(selector_output)

    # Print summary
    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"Status: {replay['status']}", file=sys.stderr)
    print(f"Changed files: {len(changed_files)}", file=sys.stderr)
    print(f"Selected tests: {len(selected_tests)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
