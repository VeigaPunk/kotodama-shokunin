#!/usr/bin/env python3
"""Round-66 MutCounterC probe: 4 byte-mutants of reports/round-66/accept-c.py.

Builds a synthetic land state inside a shared clone of the lane (writes only
under .ufo/waves/round-66/stage/mut-c/), then runs pristine + each mutant on:
  - current lane tip (pre-data): entry absent -> baseline failure expected
  - clean fixture land state
  - one defect land state per mutant (the defect each mutant's relaxation lets
    through while the pristine counter rejects it)

Fixture notes: reports/round-28/readme/sweep.py is a stub printing
"totals_ok True" (fixture double for a leg not under test); everything else is
generated content meeting the pristine counter's own legs.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
STAGE = os.path.join(LANE, ".ufo/waves/round-66/stage/mut-c")
FX = os.path.join(STAGE, "fx")
SRC = os.path.join(LANE, "reports/round-66/accept-c.py")
ENTRY = "corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md"
README = "corpus/README.md"
REGISTRY = "corpus/SOURCES.md"
TOPIC = ("scent, perfume, aromatics and incense codes as material and social "
         "practice, fixture register for the mutation probe")
QUOTE = "amber resin civet floral musk"
TEACHES = ("distillation enfleurage maceration tincture pomade sachet "
           "fumigation censer unguent balsam")

MUTANTS = {
    "M1_coverage_0.8_to_0.99": ("cov >= 0.8", "cov >= 0.99"),
    "M2_oneid_exact_to_atleast": ("if count != 1:", "if count < 1:"),
    "M3_append_count_relaxed": ("append_ok = len(missing_old) == 0",
                                "append_ok = len(missing_old) <= 2"),
    "M4_capture_substring_widened": ('"no-capture" not in src.casefold()',
                                     '"capture" not in src.casefold()'),
}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def sh(args, cwd=None, check=True):
    p = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, text=True)
    if check and p.returncode != 0:
        raise SystemExit(f"FAILED {' '.join(args)}\n{p.stdout}")
    return p


def build_mutants():
    body = open(SRC, encoding="utf-8").read()
    paths = {}
    pristine = os.path.join(STAGE, "pristine.py")
    shutil.copyfile(SRC, pristine)
    paths["pristine"] = pristine
    for name, (old, new) in MUTANTS.items():
        assert body.count(old) == 1, (name, body.count(old))
        text = body.replace(old, new)
        path = os.path.join(STAGE, name + ".py")
        open(path, "w", encoding="utf-8").write(text)
        compile(text, path, "exec")
        paths[name] = path
    return paths


def row(sid, i, defect=False):
    live = f"https://h{i}.example.org/a{i}"
    if defect == "capture":
        src = f"\u201cFixture Source {i},\u201d Fixture Press - {live} ; capture pending"
    else:
        src = (f"\u201cFixture Source {i},\u201d Fixture Press - {live} ; capture "
               f"https://web.archive.org/web/20261010000000id_/{live}")
    cells = [sid, src, "docs", "A" if i % 2 else "B", f"anchor {i}",
             f'claim: "{QUOTE}"', TEACHES, "mined", "2026-10-24", "180d", ENTRY]
    return "| " + " | ".join(cells) + " |"


def bullets(defect=None):
    out = ["# Scent, perfume, aromatics and incense codes", "",
           f"- topic: {TOPIC}", "- source: fixture rows S777-S800", "",
           "## 1. Register", ""]
    for i in range(24):
        sid = f"S{777 + i}"
        if defect == "coverage" and sid == "S777":
            line = ("- distillation enfleurage maceration tincture pomade sachet "
                    "fumigation censer unguent amber resin civet floral musk. "
                    f"({sid})")
        elif defect == "oneid" and sid == "S777":
            line = ("- Resin amber musk civet floral codes the fixture register "
                    f"item. ({sid}) duplicate citation ({sid})")
        else:
            line = ("- Resin amber musk civet floral codes the fixture register "
                    f"item. ({sid})")
        out.append(line)
    return "\n".join(out) + "\n"


def land(state, defect=None):
    reg = open(os.path.join(FX, REGISTRY), encoding="utf-8").read().splitlines()
    fixture_row = re.compile(r"^\|\s*S(\d+)\s*\|")
    reg = [l for l in reg
           if not (fixture_row.match(l)
                   and 777 <= int(fixture_row.match(l).group(1)) <= 800)]
    if defect == "append":
        rows = [l for l in reg if l.startswith("| S")]
        for line in rows[:2]:
            reg.remove(line)
    keep = list(reg)
    new_rows = [row(f"S{777 + i}", i, "capture" if (defect == "capture" and i == 0) else None)
                for i in range(24)]
    keep.extend(new_rows)
    open(os.path.join(FX, REGISTRY), "w", encoding="utf-8").write("\n".join(keep) + "\n")
    open(os.path.join(FX, ENTRY), "w", encoding="utf-8").write(bullets(defect))
    with open(os.path.join(FX, README), encoding="utf-8") as f:
        rd = f.read()
    rd = "\n".join(l for l in rd.splitlines()
                    if "scent-perfume-aromatics-codes.md" not in l)
    rd = rd.rstrip("\n") + f"\n- `scent-perfume-aromatics-codes.md` — {TOPIC}.\n"
    open(os.path.join(FX, README), "w", encoding="utf-8").write(rd)
    open(os.path.join(FX, "reports/round-28/readme/sweep.py"), "w",
         encoding="utf-8").write(
        "import sys\nprint('totals_ok True')\nsys.exit(0)\n")
    sh(["git", "add", "-A"], cwd=FX)
    sh(["git", "-c", "user.name=probe", "-c", "user.email=probe@local",
        "commit", "-q", "-m", f"fixture {state}"], cwd=FX)


def run(script, state):
    sh(["git", "checkout", "-q", "-B", "main", state], cwd=FX)
    p = subprocess.run([sys.executable, "-B", script], cwd=FX,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines = [l for l in p.stdout.splitlines() if l]
    legs = {l.split()[0]: l for l in lines
            if len(l.split()) > 1 and l.split()[1] in ("PASS", "FAIL")}
    fails = [f"{k} {v.split()[1]}" for k, v in legs.items() if v.split()[1] == "FAIL"]
    verdict = lines[-1] if lines else "<no output>"
    return {"state": state, "script": os.path.basename(script),
            "exit": p.returncode, "verdict": verdict, "fails": fails}


def main():
    paths = build_mutants()
    report = {"hashes": {k: sha(v) for k, v in paths.items()},
              "committed_pristine_sha": sha(SRC), "runs": []}
    # current lane tip, pre-data: run pristine with cwd=lane (read-only)
    p = subprocess.run([sys.executable, "-B", SRC], cwd=LANE,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines = [l for l in p.stdout.splitlines() if l]
    report["lane_tip"] = {"exit": p.returncode, "verdict": lines[-1] if lines else "",
                          "fails": [l.split()[0] + " " + l.split()[1] for l in lines
                                    if len(l.split()) > 1 and l.split()[1] == "FAIL"]}
    # fixture
    if os.path.isdir(FX):
        shutil.rmtree(FX)
    sh(["git", "clone", "--shared", "--no-checkout", "-q", LANE, FX])
    sh(["git", "checkout", "-q", "main"], cwd=FX)
    land("clean")
    sh(["git", "checkout", "-q", "-B", "clean"], cwd=FX)
    for d in ("d1_coverage", "d2_oneid", "d3_append", "d4_capture"):
        sh(["git", "checkout", "-q", "-B", d, "clean"], cwd=FX)
        land(d, d.split("_", 1)[1])
    states = ["clean", "d1_coverage", "d2_oneid", "d3_append", "d4_capture"]
    for state in states:
        for name in ["pristine"] + list(MUTANTS):
            report["runs"].append(run(os.path.join(STAGE, name + ".py"), state))
    sh(["git", "checkout", "-q", "-B", "main", "clean"], cwd=FX)
    report["committed_pristine_sha_after"] = sha(SRC)
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
