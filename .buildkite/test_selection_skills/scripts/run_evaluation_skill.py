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
    parser.add_argument(
        "--selector-model",
        type=str,
        default=None,
        help="Model passed to Lane 2 replay_selector.py"
    )
    parser.add_argument(
        "--with-second-pass",
        action="store_true",
        help="Run second pass agent between Lane 2 and Lane 3"
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
        lane2_args = [str(python), str(script_dir / "replay_selector.py"), args.pr_number, "--repo", args.repo]
        if args.selector_model:
            lane2_args.extend(["--model", args.selector_model])

        success = run_command(
            lane2_args,
            "Lane 2: Replaying LLM test selector"
        )
        if not success:
            print("\n✗ Lane 2 failed. Cannot proceed to Lane 3.")
            sys.exit(1)
    else:
        print(f"\n>>> Skipping Lane 2 (using existing replay at {selector_replay_path})")

    # Lane 2.5: Second Pass Agent
    replay_for_lane3 = selector_replay_path
    if args.with_second_pass and not args.dry_run:
        skills_dir = script_dir.parent
        patterns_file       = skills_dir / "failure_patterns.json"
        second_pass_script  = skills_dir / "after" / "second_pass.py"
        second_pass_instr   = skills_dir / "after" / "SECOND_PASS.md"
        merge_script        = skills_dir / "after" / "merge_second_pass.py"
        augmented_replay    = selector_replay_path.parent / "selector_replay_augmented.json"

        if all(f.exists() for f in [patterns_file, second_pass_script, second_pass_instr, merge_script, selector_replay_path]):
            print("\n>>> Lane 2.5: Running second pass agent...")
            import json, subprocess

            replay_data   = json.loads(selector_replay_path.read_text())
            changed_files = "\n".join(replay_data.get("changed_files", []))
            initial_sel   = "\n".join(
                f"{(t.get('identifier',t) if isinstance(t,dict) else t)} | {(t.get('reason','selected') if isinstance(t,dict) else 'selected')}"
                for t in replay_data.get("llm_selected_tests", [])
            )

            sp_result = subprocess.run(
                [str(python), str(second_pass_script),
                 "--changed-files",     changed_files,
                 "--initial-selection", initial_sel,
                 "--patterns-file",     str(patterns_file),
                 "--instructions",      str(second_pass_instr),
                 "--model", "haiku"],
                capture_output=True, text=True
            )
            additions = sp_result.stdout.strip()
            is_none   = "NONE" in additions.upper() if additions else True

            if additions and not is_none:
                print(f"    Second pass additions:\n" +
                      "\n".join(f"      {l}" for l in additions.splitlines()))
                merge_result = subprocess.run(
                    [str(python), str(merge_script),
                     "--replay",    str(selector_replay_path),
                     "--additions", additions,
                     "--output",    str(augmented_replay)],
                    capture_output=True, text=True
                )
                print(merge_result.stdout.strip())
                replay_for_lane3 = augmented_replay
            else:
                print("    Second pass: no additions — initial selection is complete.")
            print("✓ Lane 2.5 complete")
        else:
            print("\n>>> Skipping Lane 2.5 (second pass files not found)")

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
            "--selector-replay", str(replay_for_lane3)
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
