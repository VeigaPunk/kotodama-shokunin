#!/usr/bin/env python3
"""Round-72 calibration counter; all graded text is read from lands via git show."""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = "b60c7b140c5350caa7d1073711f14092541533f0"
W2 = (
    ".ufo/waves/round-71/w2/RevReceipts.md",
    ".ufo/waves/round-71/w2/RevCounterCa.md",
    ".ufo/waves/round-71/w2/RevSeparability.md",
    ".ufo/waves/round-71/w2/CritGaming2.md",
    ".ufo/waves/round-71/w2/RevRows.md",
    ".ufo/waves/round-71/w2/RevCausality.md",
    ".ufo/waves/round-71/w2/Filler33.md",
)
LESSON = "corpus/lessons/round-71.md"
LOG = "LOG.md"
QUALITY = "corpus/QUALITY.md"
MAP = "corpus/id-renumber-map.json"
RECEIPT = "reports/round-71/telemetry/measures-ca.txt"
FLEET_REPORT = ".ufo/reports/round-72/kotodama.md"
CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"


def git(root, *args, check=True):
    p = subprocess.run(["git", "-C", str(root), *args], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True)
    if check and p.returncode:
        raise RuntimeError(p.stderr.strip() or "git " + " ".join(args) + " failed")
    return p


def blob(root, rev, path):
    return git(root, "show", f"{rev}:{path}").stdout


def passed(name, yes, detail=""):
    print(f"LEG {'PASS' if yes else 'FAIL'} {name}" + (f" — {detail}" if detail else ""))
    return bool(yes)


def census(root, lands):
    # Execute the maintained, read-only census against the committed tree, not worktree bytes.
    with tempfile.TemporaryDirectory(prefix="accept-ca-72-") as td:
        checkout = Path(td) / "tree"
        checkout.mkdir()
        for rel in ("corpus/SOURCES.md",):
            (checkout / rel).parent.mkdir(parents=True, exist_ok=True)
            (checkout / rel).write_text(blob(root, lands, rel), encoding="utf-8")
        # validator takes root as a corpus parent and checks the SOURCES file plus rows;
        # populate the complete committed corpus paths required by its read-only validation.
        paths = git(root, "ls-tree", "-r", "--name-only", lands).stdout.splitlines()
        for rel in paths:
            if not (rel.startswith("corpus/knowledge/") or rel == "corpus/SOURCES.md"):
                continue
            dest = checkout / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(git(root, "show", f"{lands}:{rel}").stdout.encode())
        proc = subprocess.run([CENSUS, "validate", "--root", td, "kotodama"],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return proc.returncode == 0, proc.stdout.strip()


def check(root, lands, fleet_root):
    ok = True
    def leg(n, condition, detail=""):
        nonlocal ok
        ok = passed(n, condition, detail) and ok

    try:
        q = blob(root, lands, QUALITY)
        leg("QUAL20", bool(re.search(r"^20\\. ", q, re.M)), "criterion 20 committed")
        leg("QUAL21", bool(re.search(r"^21\\. ", q, re.M)), "criterion 21 committed")
        found = []
        for p in W2:
            try:
                blob(root, lands, p)
                found.append(True)
            except RuntimeError:
                found.append(False)
        leg("W2FILES", all(found), f"present={sum(found)}/7")

        log = blob(root, lands, LOG)
        round72 = log.split("round 72", 1)[-1] if "round 72" in log else ""
        logchecks = ("S861" in round72 and "S874" in round72 and "S1005" in round72
                     and "<RECORDS>" in round72 and "misroot" in round72)
        leg("LOGCORR", logchecks, "three prior texts named in round-72 log")

        lesson = blob(root, lands, LESSON)
        corrections = lesson.split("## Corrections (round 72)")
        corr = corrections[-1] if len(corrections) == 2 else ""
        lessonchecks = ("S861" in corr and "S992" in corr and "S874" in corr and "S1005" in corr
                        and "10/6/5" in corr and "10/7/4" in corr
                        and "41" in corr and "78" in corr and "40" in corr and "77" in corr)
        leg("LESSONCORR", lessonchecks, "appended correction section covers id map, tally, seats")

        report = blob(root, lands, FLEET_REPORT)
        reportchecks = all(x in report for x in (":57", ":61", "S861", "S992", "supersed"))
        leg("REPORTCORR", reportchecks, FLEET_REPORT)

        maptext = blob(root, lands, MAP)
        mapchecks = all(x in maptext for x in ("65ff151", "99e3d63", "S861", "S992", "S874", "S1005"))
        leg("MAPCORR", mapchecks, MAP)

        receipt = blob(root, lands, RECEIPT)
        stamp = ("64da9e14" in receipt and "f706aacd" in receipt
                 and re.search(r"1ce25fb9.{0,120}64da9e14", receipt, re.S) is None)
        leg("CASTAMP", stamp, "receipt associates true counter sha with 64da9e14")

        cap = ("capoeira-circle-00892" in corr and "20170513162348" in corr
               and "20171120140510" in corr and "20171208155324" in corr and "200" in corr
               and "Capoeira" in round72)
        leg("CAPOEIRA", cap, "appended live and CDX correction cited by LOG")

        diff = git(root, "diff", "-U0", f"{BASE}..{lands}", "--", LOG, LESSON, QUALITY).stdout.splitlines()
        removed = [line for line in diff if line.startswith("-") and not line.startswith("---")]
        leg("APPENDONLY", not removed, f"removed-content-lines={len(removed)}")

        ancestry = git(root, "rev-list", "--ancestry-path", f"{BASE}..{lands}").stdout.splitlines()
        commits = git(root, "log", "--format=%H", f"{BASE}..{lands}").stdout.splitlines()
        lane_commits = [c for c in commits if c]
        reportlast = bool(lane_commits) and all(git(root, "merge-base", "--is-ancestor", c, lands, check=False).returncode == 0 for c in lane_commits)
        reportlast = reportlast and all(x in report for x in (lands, "99e3d63", "b60c7b1"))
        leg("REPORTLAST", reportlast, "lands and inherited commit anchors named")

        good, output = census(root, lands)
        leg("NOHARM", good, output or "census validator exit 0")
    except (RuntimeError, OSError, UnicodeError) as exc:
        print(f"COUNTER ERROR: {exc}")
        return 2

    print(f"ACCEPT-CA-72: {'PASS legs=12/12' if ok else 'FAIL'}")
    return 0 if ok else 1


def selftest():
    with tempfile.TemporaryDirectory(prefix="accept-ca-selftest-") as td:
        root = Path(td)
        git(root, "init", "-q")
        (root / "LOG.md").write_text("unchanged\n")
        (root / "corpus/lessons").mkdir(parents=True)
        (root / "corpus/lessons/round-71.md").write_text("filed text\n")
        (root / "corpus/QUALITY.md").write_text("criterion\n")
        git(root, "add", ".")
        git(root, "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "base")
        base = git(root, "rev-parse", "HEAD").stdout.strip()
        (root / "corpus/lessons/round-71.md").write_text("edited in place\n")
        git(root, "add", ".")
        git(root, "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "rewrite")
        diff = git(root, "diff", "-U0", f"{base}..HEAD", "--", LOG, LESSON, QUALITY).stdout.splitlines()
        removed = [line for line in diff if line.startswith("-") and not line.startswith("---")]
        result = not removed
        print(f"SELFTEST APPENDONLY {'PASS' if not result else 'FAIL'} removed-content-lines={len(removed)}")
        return 0 if removed else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands")
    ap.add_argument("--fleet-root", required=False, default="/home/vgpnk/Projects/shokunin")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.lands:
        ap.error("--lands is required unless --selftest is used")
    return check(Path(args.root).resolve(), args.lands, Path(args.fleet_root).resolve())

if __name__ == "__main__":
    sys.exit(main())
