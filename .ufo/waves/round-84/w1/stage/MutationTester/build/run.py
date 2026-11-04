#!/usr/bin/env python3
"""Grade every stub with the frozen counters and with one-line counter mutants."""
import json
import os
import shutil
import subprocess
import sys

S = os.environ.get("SEAT_SCRATCH") or os.getcwd()
REP = os.path.join(S, "rep")
INSTR = os.path.join(S, "instr")
MUT = os.path.join(S, "mut")
WORK = os.path.join(S, "work")
OUT = os.path.join(S, "out")
FREEZE = "3ca2cf288fb593618e0559ea86a36e2dd3110eb8"
FREEZE_R1 = "e160a72e4adf1620e09f812b913d4ece0fcd5243"

COUNTER_MUTS = {
    "C-D-anchors": ("accept-d84.py", "            if len(found) != 1 or found[0] in bad:",
                    "            if len(found) == 0 or found[0] in bad:"),
    "C-O-demo": ("accept-o84.py", "        if got != want:", "        if False and got != want:"),
    "C-O-registry": ("accept-o84.py",
                     '              and ins >= block["min_instruments_at_lands"] and unrowed <= block["max_unrowed_tools"])',
                     '              and ins >= block["min_instruments_at_lands"] and True)'),
}


def sh(*a, **kw):
    return subprocess.run(list(a), capture_output=True, text=True, **kw)


def top(d):
    return sh("git", "-C", d, "rev-parse", "--show-toplevel").stdout.strip()


def build_mutants():
    os.makedirs(MUT, exist_ok=True)
    shutil.copyfile(os.path.join(INSTR, "counterlib.py"), os.path.join(MUT, "counterlib.py"))
    made = {}
    for name, (src, old, new) in COUNTER_MUTS.items():
        text = open(os.path.join(INSTR, src), encoding="utf-8").read()
        assert text.count(old) == 1, (name, text.count(old))
        out = os.path.join(MUT, name + ".py")
        with open(out, "w", encoding="utf-8") as f:
            f.write(text.replace(old, new))
        made[name] = out
    return made


def grade(label, counter, lands, freeze, *, workname=None):
    w = os.path.join(WORK, workname or label)
    shutil.rmtree(w, ignore_errors=True)
    os.makedirs(w)
    sh("git", "-C", REP, "update-ref", "refs/heads/main", lands)
    r = sh(sys.executable, "-B", counter, "--root", REP, "--lands", lands, "--freeze", freeze, "--work", w)
    text = r.stdout + (("\n[stderr]\n" + r.stderr) if r.stderr.strip() else "")
    path = os.path.join(OUT, label + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("=" * 78)
    print(label, "rc=%d" % r.returncode)
    print(text.rstrip())
    return r.returncode, text


def main():
    assert top(REP) == REP, top(REP)
    commits = json.load(open(os.path.join(S, "commits.json"), encoding="utf-8"))
    muts = build_mutants()
    d84 = os.path.join(INSTR, "accept-d84.py")
    o84 = os.path.join(INSTR, "accept-o84.py")
    verdicts = {}

    for name in ("D-good", "D-m1", "D-m1b", "D-m2", "D-m3"):
        rc, text = grade(name, d84, commits[name], FREEZE)
        verdicts[name] = rc
    # drift probe: one lands, two freezes
    rc, text = grade("D-r1@r1-freeze", d84, commits["D-r1"], FREEZE_R1)
    verdicts["D-r1@r1-freeze"] = rc
    rc, text = grade("D-r1@assigned-freeze", d84, commits["D-r1"], FREEZE)
    verdicts["D-r1@assigned-freeze"] = rc

    for name in ("O-m4", "O-m4b", "O-m4c", "O-m5", "O-unrowed"):
        rc, text = grade(name, o84, commits[name], FREEZE)
        verdicts[name] = rc
    # counter mutants
    rc, text = grade("CM-D-anchors--D-m1", muts["C-D-anchors"], commits["D-m1"], FREEZE)
    verdicts["CM-D-anchors--D-m1"] = rc
    rc, text = grade("CM-D-anchors--D-m1b", muts["C-D-anchors"], commits["D-m1b"], FREEZE)
    verdicts["CM-D-anchors--D-m1b"] = rc
    rc, text = grade("CM-O-demo--O-m4c", muts["C-O-demo"], commits["O-m4c"], FREEZE)
    verdicts["CM-O-demo--O-m4c"] = rc
    rc, text = grade("CM-O-registry--O-unrowed", muts["C-O-registry"], commits["O-unrowed"], FREEZE)
    verdicts["CM-O-registry--O-unrowed"] = rc

    # does the committed gate-registry auditor fail the unrowed tool?
    tree = os.path.join(WORK, "audit-unrowed")
    shutil.rmtree(tree, ignore_errors=True)
    os.makedirs(tree)
    sh("git", "-C", REP, "update-ref", "refs/heads/main", commits["O-unrowed"])
    arc = subprocess.run(["git", "-C", REP, "archive", commits["O-unrowed"]], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", tree], input=arc, check=True)
    r = sh(sys.executable, "-B", os.path.join(tree, "tools", "check-gate-registry.py"), "--root", tree)
    print("=" * 78)
    print("AUDIT-UNROWED rc=%d" % r.returncode)
    print(r.stdout.rstrip())
    with open(os.path.join(OUT, "audit-unrowed.txt"), "w", encoding="utf-8") as f:
        f.write("rc=%d\n%s" % (r.returncode, r.stdout))

    with open(os.path.join(OUT, "verdicts.json"), "w", encoding="utf-8") as f:
        json.dump(verdicts, f, indent=1, sort_keys=True)
    print("=" * 78)
    print(json.dumps(verdicts, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
