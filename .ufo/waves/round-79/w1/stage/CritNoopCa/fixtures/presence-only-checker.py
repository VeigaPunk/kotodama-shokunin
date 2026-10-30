#!/usr/bin/env python3
"""Straw-man PRESENCE-ONLY checker for the Ca correction (the vacuous shape this
seat attacks). It binds nothing: it passes any tree where a correction record
for S884 exists with a non-empty actual_token, or any note mentioning S884.

This is intentionally weak. Its only job is to demonstrate that the exact junk
payloads in junk-corrections.json flip it to PASS, so the real accept-ca.py
must not look anything like it.

Usage: presence-only-checker.py --repo R --lands L --freeze F
Exit 0 + "PRESENCE: PASS" when a correction-shaped thing is present, else
exit 1 + "PRESENCE: FAIL". Input errors exit 2.
"""
import argparse
import json
import subprocess
import sys

CORRECTION_PATH = "reports/round-79/telemetry/census-correction.json"


def git_show(repo, rev, path):
    p = subprocess.run(
        ["git", "-C", repo, "show", f"{rev}:{path}"],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        return None
    return p.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--lands", required=True)
    ap.add_argument("--freeze", required=True)
    a = ap.parse_args()

    raw = git_show(a.repo, a.lands, CORRECTION_PATH)
    if raw is None:
        print("PRESENCE: FAIL (no correction record at %s)" % CORRECTION_PATH)
        return 1
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        # prose note (J-CA3 class): presence = mentions S884
        ok = "S884" in raw
        print("PRESENCE: %s (prose note mentioning S884: %s)"
              % ("PASS" if ok else "FAIL", ok))
        return 0 if ok else 1
    ok = bool(obj.get("actual_token")) and obj.get("id") == "S884"
    print("PRESENCE: %s (JSON record, non-empty actual_token=%s)"
          % ("PASS" if ok else "FAIL", bool(obj.get("actual_token"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
