#!/usr/bin/env python3
"""
Skill wrapper for running the complete PR evaluation workflow.

This script is called when a user invokes the /run_pr_evaluation skill.
It orchestrates all three lanes of the evaluation workflow.

Usage:
    python run_evaluation_skill.py <pr_number> [--repo <repo>] [--output-dir <dir>]
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"\n>>> {description}...")
    print(f"    Command: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=False, text=True)

    if result.returncode != 0:
        print(f"✗ {description} failed with exit code {result.returncode}")
        return False

    print(f"✓ {description} completed successfully")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Run the complete 3-lane offline PR evaluation workflow"
    )
    parser.add_argument(
        "pr_number",
        type=str,
        help="GitHub PR number to evaluate"
    )
    parser.add_argument(
        "--repo",
        type=str,
        default="vllm-project/vllm",
        help="Repository name (default: vllm-project/vllm)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Custom output directory"
    )
    parser.add_argument(
        "--skip-lane-1",
        action="store_true",
        help="Skip CI evidence collection"
    )
    parser.add_argument(
        "--skip-lane-2",
        action="store_true",
        help="Skip LLM selector replay"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run lanes 1 and 2 but skip lane 3"
    )

    args = parser.parse_args()

    # Determine script directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent.parent

    # Python to use
    python = repo_root / ".venv" / "bin" / "python"

    if not python.exists():
        print(f"Error: Python not found at {python}")
        print("Run 'uv venv --python 3.12' first.")
        sys.exit(1)

    print("=" * 60)
    print("  PR EVALUATION WORKFLOW")
    print("=" * 60)
    print(f"  PR Number:  #{args.pr_number}")
    print(f"  Repository: {args.repo}")
    print(f"  Output Dir: {args.output_dir or 'default'}")
    print("=" * 60)

    # Build paths
    evidence_dir = script_dir.parent / "evidence" / f"pr_{args.pr_number}"
    replay_dir = script_dir.parent / "replay" / f"pr_{args.pr_number}"
    output_dir = Path(args.output_dir) if args.output_dir else script_dir.parent / "evaluation" / f"pr_{args.pr_number}"

    ci_evidence_path = evidence_dir / "ci_evidence.json"
    selector_replay_path = replay_dir / "selector_replay.json"

    # Lane 1: Collect CI Evidence
    if not args.skip_lane_1:
        success = run_command(
            [str(python), str(script_dir / "collect_ci_evidence.py"), args.pr_number, "--repo", args.repo],
            "Lane 1: Collecting Buildkite CI evidence"
        )
        if not success:
            print("\n⚠ Lane 1 failed. Continuing anyway...")
    else:
        print(f"\n>>> Skipping Lane 1 (using existing evidence at {ci_evidence_path})")

    # Lane 2: Replay LLM Selector
    if not args.skip_lane_2:
        success = run_command(
            [str(python), str(script_dir / "replay_selector.py"), args.pr_number, "--repo", args.repo],
            "Lane 2: Replaying LLM test selector"
        )
        if not success:
            print("\n✗ Lane 2 failed. Cannot proceed to Lane 3.")
            sys.exit(1)
    else:
        print(f"\n>>> Skipping Lane 2 (using existing replay at {selector_replay_path})")

    # Lane 3: Compare Results
    if args.dry_run:
        print("\n>>> --dry-run specified. Skipping Lane 3 comparison.")
    else:
        if not ci_evidence_path.exists():
            print(f"\n✗ CI evidence not found at {ci_evidence_path}")
            print("   Re-run without --skip-lane-1 or check PR number.")
            sys.exit(1)

        if not selector_replay_path.exists():
            print(f"\n✗ Selector replay not found at {selector_replay_path}")
            print("   Re-run without --skip-lane-2.")
            sys.exit(1)

        lane3_args = [
            str(python), str(script_dir / "compare_selector_vs_ci.py"),
            args.pr_number,
            "--ci-evidence", str(ci_evidence_path),
            "--selector-replay", str(selector_replay_path)
        ]

        if args.output_dir:
            lane3_args.extend(["--output-dir", args.output_dir])

        success = run_command(lane3_args, "Lane 3: Comparing selector vs CI")

        if success:
            print("\n" + "=" * 60)
            print("  EVALUATION COMPLETE!")
            print("=" * 60)
            print(f"\n  Results saved to: {output_dir}/")
            print("\n  Files generated:")
            print(f"    - evaluation_report.json")
            print(f"    - evaluation_summary.md")
            print(f"    - test_comparison_table.txt")
            print(f"    - PR{args.pr_number}_Comparison.xlsx")
            print(f"    - gap_analysis.txt")
            print("\n  To view results:")
            print(f"    cat {output_dir}/evaluation_summary.md")
            print(f"    cat {output_dir}/test_comparison_table.txt")
            print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
