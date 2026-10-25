#!/usr/bin/env python3
r"""Round-72 calibration acceptance counter — claim Ca (K71-1..K71-8 corrections).

Implements the 12 frozen legs of reports/round-72/claims.json (v2, pre-data
corrections F1-F9 applied). Every graded byte is read from the lands revision
via `git show`; the fleet report is read from the fleet repo by absolute path
(fail closed if unreadable). Whole-tree accounting: every tracked file changed
in base..lands must map to an authorized round-72 path, and the enumerated
filed set (LOG.md, corpus/lessons/round-71.md, corpus/QUALITY.md,
.ufo/waves/round-71/, reports/round-71/ minus the new CASTAMP receipt) must
show zero removed content lines.

Exit: 0 all legs pass; 1 any leg fails; 2 input error.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile

BASE = "b60c7b140c5350caa7d1073711f14092541533f0"
FLEET = "/home/vgpnk/Projects/shokunin"
FLEET_REPORT_R71 = ".ufo/reports/round-71/kotodama.md"
FLEET_REPORT_R72 = ".ufo/reports/round-72/kotodama.md"
KNOWN_R71_REPORT_COMMITS = {"861dcb6b", "bc418b99", "fb8495ef", "98873dfd", "8380f703"}
W2_FILES = (
    ".ufo/waves/round-71/w2/Filler30.md",
    ".ufo/waves/round-71/w2/RevReceipts.md",
    ".ufo/waves/round-71/w2/CritTrends.md",
    ".ufo/waves/round-71/w2/Filler28.md",
    ".ufo/waves/round-71/w2/Filler36.md",
    ".ufo/waves/round-71/w2/RevCounterCa.md",
    ".ufo/waves/round-71/w2/RevEntry.md",
)
CASTAMP = "reports/round-71/telemetry/measures-ca-restamp-64da9e14.txt"
AUTHORIZED_PREFIXES = (
    "LOG.md", "SCORECARD.md", "corpus/", "reports/round-72/",
    "reports/round-71/telemetry/measures-ca-restamp-64da9e14.txt",
    ".ufo/waves/round-71/w2/", ".ufo/waves/round-72/",
)


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True)


def show(root, rev, path):
    r = git(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def leg(name, passed, detail=""):
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


def in_range(root, lands, commit):
    if not commit:
        return False
    a = git(root, "merge-base", "--is-ancestor", commit, lands)
    b = git(root, "merge-base", "--is-ancestor", BASE, commit)
    return a.returncode == 0 and b.returncode == 0


def section_of(text, heading_re):
    lines = text.splitlines()
    out, started = [], False
    for line in lines:
        if heading_re.match(line):
            started = True
            out.append(line)
            continue
        if started and re.match(r"^##\s", line) and not heading_re.match(line):
            break
        if started:
            out.append(line)
    return "\n".join(out)


def main_check(root, lands, fleet_root):
    ok = True

    # --- QUAL20 ---
    q = show(root, lands, "corpus/QUALITY.md") or ""
    n20 = len(re.findall(r"^20\. ", q, re.M))
    ok &= leg("QUAL20", n20 == 1, "count=%d" % n20)

    # --- W2FILES ---
    missing = [f for f in W2_FILES
               if git(root, "cat-file", "-e", "%s:%s" % (lands, f)).returncode != 0]
    ok &= leg("W2FILES", not missing, "missing=%s" % missing if missing else "7/7 committed")

    # --- LOGCORR: three superseded lines, each old->new named in the round-72 entry ---
    log = show(root, lands, "LOG.md") or ""
    m72 = re.search(r"^## Round 72\b.*?(?=^## Round |\Z)", log, re.M | re.S)
    entry72 = m72.group(0) if m72 else ""
    sub = {
        "idmap": ("S861→S992" in entry72 and "S874→S1005" in entry72 and "99e3d63" in entry72),
        "records": ("<RECORDS>" in entry72 and "1721fbd" in entry72),
        "misroot": ("misroot" in entry72 and "1721fbd" in entry72 and "ccadb59" in entry72),
        "tally": ("10/6/5" in entry72 and "10/7/4" in entry72),
    }
    bad = [k for k, v in sub.items() if not v]
    ok &= leg("LOGCORR", not bad, "missing=%s" % bad if bad else "4 old->new items named")

    # --- LESSONCORR ---
    lesson71 = show(root, lands, "corpus/lessons/round-71.md") or ""
    corr = section_of(lesson71, re.compile(r"^## Corrections \(round 72\)"))
    csub = {
        "heading": bool(corr),
        "idmap": ("S861→S992" in corr and "S874→S1005" in corr),
        "tally": ("10/6/5" in corr and "10/7/4" in corr),
        "seats": ("41" in corr and "40" in corr and "78" in corr and "77" in corr),
    }
    bad = [k for k, v in csub.items() if not v]
    ok &= leg("LESSONCORR", not bad, "missing=%s" % bad if bad else "corrections section complete")

    # --- REPORTCORR (fleet repo, fail closed) ---
    r = git(fleet_root, "log", "--format=%H", "-1", "--", FLEET_REPORT_R72)
    rev = r.stdout.strip()
    report = None
    if rev:
        report = show(fleet_root, rev, FLEET_REPORT_R72)
    rep_ok = (report is not None and ":57" in report and ":61" in report
              and "S861→S992" in report)
    ok &= leg("REPORTCORR", rep_ok,
              "fleet-rev=%s" % (rev[:12] if rev else "MISSING"))

    # --- MAPCORR ---
    msub = ("65ff151" in entry72 and "99e3d63" in entry72 and "784" in entry72
            and "797" in entry72 and "S861→S992" in entry72 and "S874→S1005" in entry72)
    ok &= leg("MAPCORR", msub, "old 65ff151 (784/2/S861) -> new 99e3d63 (797/15/S874) recorded")

    # --- CASTAMP ---
    stamp = show(root, lands, CASTAMP)
    ssub = bool(stamp) and "64da9e14" in stamp and "f706aacd" in stamp \
        and "1ce25fb9" in stamp
    if stamp:
        c = git(root, "log", "--diff-filter=A", "--format=%H", "-1", "--", CASTAMP)
        commit = c.stdout.strip()
        ssub = ssub and in_range(root, lands, commit)
    else:
        commit = ""
    ok &= leg("CASTAMP", ssub, "commit=%s" % (commit[:12] if commit else "MISSING"))

    # --- QUAL21 ---
    m21 = re.search(r"^21\. .*$", q, re.M)
    text21 = m21.group(0) if m21 else ""
    qsub = bool(m21) and "CDX" in text21 and "canonical" in text21 \
        and "reject" in text21 and "URL" in text21
    ok &= leg("QUAL21", qsub, text21[:90])

    # --- CAPOEIRA (section-scoped, base-true lesson grep is not enough) ---
    cap_lesson = "capoeira-circle-00892" in corr and "20170513162348" in corr
    cap_log = "capoeira-circle-00892" in entry72
    ok &= leg("CAPOEIRA", cap_lesson and cap_log,
              "lesson=%s log=%s" % (cap_lesson, cap_log))

    # --- APPENDONLY: enumerated filed set zero removed lines + whole-tree accounting ---
    d = git(root, "diff", "-U0", "%s..%s" % (BASE, lands), "--",
            "LOG.md", "corpus/lessons/round-71.md", "corpus/QUALITY.md",
            ".ufo/waves/round-71", "reports/round-71")
    removed = len(re.findall(r"^-(?![-])", d.stdout, re.M))
    names = git(root, "diff", "--name-only", "%s..%s" % (BASE, lands))
    changed = [l for l in names.stdout.splitlines() if l.strip()]
    unauthorized = [p for p in changed
                    if not p.startswith(AUTHORIZED_PREFIXES)]
    # fleet round-71 report untouched
    fr = git(fleet_root, "log", "--format=%H", "-1", "--", FLEET_REPORT_R71)
    fleet_rev = fr.stdout.strip()
    fleet_ok = any(fleet_rev.startswith(k) for k in KNOWN_R71_REPORT_COMMITS)
    ok &= leg("APPENDONLY", removed == 0 and not unauthorized and fleet_ok,
              "removed=%d unauthorized=%s fleet-r71-last=%s"
              % (removed, unauthorized, fleet_rev[:12]))

    # --- REPORTLAST ---
    n = git(root, "rev-list", "--count", "%s..%s" % (BASE, lands))
    count = n.stdout.strip()
    rl = bool(report) and lands[:7] in report and "b60c7b1" in report \
        and "99e3d63" in report
    ok &= leg("REPORTLAST", rl, "commits=%s report-names-lands=%s"
              % (count, rl))

    # --- NOHARM: census over the registry bytes at lands, materialized ---
    with tempfile.TemporaryDirectory(prefix="r72-census-") as td:
        lane_dir = os.path.join(td, "kotodama-shokunin")
        os.makedirs(lane_dir)
        arc = git(root, "archive", lands, "corpus", "SKILL.md")
        proc_arc = subprocess.run(["tar", "-x", "-C", lane_dir],
                                  input=arc.stdout.encode(), capture_output=True)
        if proc_arc.returncode != 0 or not os.path.isfile(
                os.path.join(lane_dir, "corpus", "SOURCES.md")):
            ok &= leg("NOHARM", False, "corpus materialization failed")
        else:
            conf = show(fleet_root, "HEAD", "shokunin.conf")
            with open(os.path.join(td, "shokunin.conf"), "w") as fh:
                fh.write(conf or "")
            script = os.path.join(fleet_root, "scripts/sources-census.sh")
            proc = subprocess.run([script, "validate", "--root", td, "kotodama"],
                                  capture_output=True, text=True)
            ok &= leg("NOHARM", proc.returncode == 0,
                      "census exit=%d" % proc.returncode)

    print("ACCEPT-CA-72: %s legs=12/12" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="round-72 calibration counter (claim Ca)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", required=True)
    ap.add_argument("--fleet-root", default=FLEET)
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    if not re.fullmatch(r"[0-9a-f]{40}", args.lands):
        print("ERROR: --lands must be 40 hex", file=sys.stderr)
        return 2
    return main_check(root, args.lands.lower(), args.fleet_root)


if __name__ == "__main__":
    sys.exit(main())
