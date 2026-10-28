#!/usr/bin/env python3
"""SCRATCHMIRROR against the REAL round-77 staged artifacts.

Read-only: materializes the lane base tree into scratch, copies the lane's
`.ufo/waves/round-77/assimilation/` directory (untracked staging bytes) next to
it, and calls `leg_scratchmirror` with the draft's row_set.  Prints the leg line
only; nothing is written into the lane.
"""
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"


def main():
    spec = importlib.util.spec_from_file_location(
        "accept_c", os.path.join(HERE, "accept-c.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    scratch = os.environ.get("HYAKU_SCRATCH") or ""
    if not scratch:
        print("ERROR: set HYAKU_SCRATCH to a scratch root", file=sys.stderr)
        return 2
    root = tempfile.mkdtemp(dir=scratch)
    mat = os.path.join(root, "mat")
    mat_base = os.path.join(root, "matbase")
    os.makedirs(mat)
    os.makedirs(mat_base)
    for dest in (mat, mat_base):
        proc = subprocess.run(["git", "-C", LANE, "archive", BASE,
                               "corpus/SOURCES.md"], capture_output=True)
        subprocess.run(["tar", "-x", "-C", dest], input=proc.stdout)
    assim = os.path.join(mat, ".ufo/waves/round-77/assimilation")
    os.makedirs(os.path.dirname(assim))
    shutil.copytree(os.path.join(LANE, ".ufo/waves/round-77/assimilation"),
                    assim)
    cfg = {
        "rows": ["S897", "S898"],
        "row_staged": {"S897": ["S897"], "S898": ["S903"]},
        "entries": ["corpus/knowledge/linguistics/naming-systems"
                    ".amend-2026-10-23.md"],
        "scratch_mirror": {"dir": m.ASSIM, "receipt": None},
    }
    ok = m.leg_scratchmirror({"mat": mat, "mat_base": mat_base, "cfg": cfg})
    print("probe tree: %s (removed by the caller)" % root)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
