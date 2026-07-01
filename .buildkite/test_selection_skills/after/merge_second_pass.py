#!/usr/bin/env python3
"""
Merge second pass agent additions into a selector_replay.json.

Reads the original replay, appends second pass additions to
llm_selected_tests, and writes the augmented replay to a new file.

Usage:
    python merge_second_pass.py \
        --replay  replay/pr_43720/selector_replay.json \
        --additions "tests/metrics/ | engine change — failed 3x\ntests/v1/ | v1 worker change" \
        --output  replay/pr_43720/selector_replay_augmented.json
"""

import argparse
import json
from pathlib import Path


def parse_additions(additions_text: str) -> list[dict]:
    """Parse 'path | reason' lines into llm_selected_tests entries."""
    entries = []
    for line in additions_text.strip().splitlines():
        line = line.strip()
        if not line or "NONE" in line.upper() or "|" not in line:
            continue
        path, _, reason = line.partition("|")
        path   = path.strip()
        reason = reason.strip()
        if path:
            entries.append({
                "identifier": path,
                "reason":     f"[second-pass] {reason}",
            })
    return entries


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay",    required=True, type=Path)
    parser.add_argument("--additions", required=True)
    parser.add_argument("--output",    required=True, type=Path)
    args = parser.parse_args()

    replay = json.loads(args.replay.read_text())
    additions = parse_additions(args.additions)

    if not additions:
        print("No additions from second pass — augmented replay is identical to original.")
        # Write the original unchanged so Lane 3 still has a file to read
        args.output.write_text(json.dumps(replay, indent=2))
        return

    original_tests = replay.get("llm_selected_tests", [])

    # Avoid duplicates — skip additions already covered by the initial selection
    existing_paths = {
        (t.get("identifier") if isinstance(t, dict) else t).rstrip("/")
        for t in original_tests
    }

    new_entries = []
    for entry in additions:
        path = entry["identifier"].rstrip("/")
        if not any(
            path == ep or path.startswith(ep) or ep.startswith(path)
            for ep in existing_paths
        ):
            new_entries.append(entry)
            existing_paths.add(path)

    augmented = dict(replay)
    augmented["llm_selected_tests"] = original_tests + new_entries
    augmented["second_pass_additions"] = new_entries
    augmented["second_pass_addition_count"] = len(new_entries)

    args.output.write_text(json.dumps(augmented, indent=2))
    print(f"Merged {len(new_entries)} addition(s) into {args.output}")
    for e in new_entries:
        print(f"  + {e['identifier']}  —  {e['reason']}")


if __name__ == "__main__":
    main()
