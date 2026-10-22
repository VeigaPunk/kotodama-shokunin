#!/usr/bin/env python3
"""Round-56 QUALITY criterion 11 controls for claim O, built before dispatch (adapted from
reports/round-55/criterion11-controls-o.py).

  python3 -B reports/round-56/criterion11-controls-o.py <lane-repo> <tree-ish> > reports/round-56/telemetry/criterion11-controls-o.txt

Read-only on the lane: `git archive <tree-ish>` is extracted into a mktemp directory, and every
control copy is built there. Each copy runs the declared argv verbatim from its own root:
  python3 -B reports/round-56/accept-o.py
GREEN  every mechanical clause holds through a stand-in landing that is never landed: the copy's
       tools/check-gate-quotes.py is replaced by a stand-in that prints the expected findings for
       corpus/lessons/round-55.md and the entities fixture, answers the bad-UTF-8 fixture with a
       GATE_QUOTES_ERROR line and exit 2, and hands every other call (rounds 49-54, --selftest) to
       the base tool kept beside it. Expected exit 0.
One RED per mechanical clause direction, each the GREEN stand-in with that clause alone changed by
its nearest near-miss; expected exit 1 with that clause's leg FAIL and every other leg PASS:
  ENTITY         15 of the 16 html-entity triples (S357 at line 141 dropped)
  ENTITY-LINE    S288 reported at line 73 instead of 72 (same S-id set, wrong line)
  ENTITY-EXTRA   S289 (line 73, no reference) also reported html-entity: 17
  NOFALSE        the round-55 run adds `S289 words=26` at line 73
  EXIT           the round-55 run prints the same findings and exits 0
  EXIT-FIX       the fixture run prints the same findings and exits 0
  DECODE         the fixture's S951 truncated-grounds finding is missing (decoded comparison absent)
  DECODE-ESC     the fixture's S955 words=26 finding is missing (entity-quoted span not counted)
  DECODE-FP      the fixture's S953 boundary row (`AT&T;`, `R&D;`) reported html-entity
  ENTITY-DOUBLE  the 16 triples plus a second S288 line-72 finding (one finding per reference)
  DECODE-MOVED   the run-time moved copy of the fixture prints no findings and exits 0 (a checker keyed
                 on the fixture's path)
  DECODE-HEX     the fixture's S958 (hexadecimal references) unreported
  DECODE-ELLIPSIS the fixture's S960 words=5 (decoded &hellip; joining fragments) missing
  KEEP           the round-53 run's last words= line reads one more word (round 54 has no words= line)
  KEEP-EXIT      the round-52 run prints the base output and exits 0
  BADUTF8        the bad-UTF-8 run writes a Traceback after its GATE_QUOTES_ERROR line (exit 2)
  BADUTF8-EXIT   the bad-UTF-8 run prints its GATE_QUOTES_ERROR line and exits 1
  BADUTF8-PATH   the bad-UTF-8 error line does not name the path
  FORMAT-COUNT   the round-55 run's summary counts one finding more than it prints
  FORMAT         the round-55 run adds an unparseable line `<path>:5-6 S903 words=26`
  FORMAT-CRASH   the fixture run writes a traceback to stderr, stdout unchanged
  SELFTEST       `--selftest` exits 1
The script prints sha256 of each instrument it ran and the full revision it archived. Lines carry
no `$ ` prefix, so criterion 9's two-way dry-run check does not read this receipt.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ARGV = ["python3", "-B", "reports/round-56/accept-o.py"]
INSTRUMENTS = ["reports/round-56/accept-o.py", "tools/check-gate-quotes.py",
               "reports/round-56/fixtures/lessons/entities.md", "reports/round-56/fixtures/SOURCES.md",
               "reports/round-56/fixtures/lessons/bad-utf8.md", "reports/round-56/base-gate-keep.txt",
               "corpus/lessons/round-55.md", "reports/round-56/criterion11-controls-o.py"]
ENT = [[72, "S288"], [82, "S298"], [88, "S304"], [89, "S305"], [93, "S309"], [96, "S312"],
       [110, "S326"], [113, "S329"], [125, "S341"], [127, "S343"], [131, "S347"], [132, "S348"],
       [134, "S350"], [138, "S354"], [140, "S356"], [141, "S357"]]
FIXW = [[8, "S951", "html-entity"], [8, "S951", "truncated-grounds"], [9, "S952", "html-entity"],
        [11, "S954", "html-entity"], [12, "S955", "html-entity"], [12, "S955", "words=26"],
        [14, "S958", "html-entity"], [15, "S959", "html-entity"], [16, "S960", "html-entity"],
        [16, "S960", "words=5"]]

STANDIN = r"""#!/usr/bin/env python3
# Stand-in landing for a criterion-11 control copy only; never landed.
import json, os, subprocess, sys
CFG = json.loads(%r)
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "check-gate-quotes-base.py")
args = sys.argv[1:]
if args == ["--selftest"]:
    if CFG["selftest_fail"]:
        print("SELFTEST stand-in FAIL"); sys.exit(1)
    sys.exit(subprocess.run([sys.executable, "-B", BASE] + args).returncode)
if args and args[0].endswith("round-55.md"):
    out = [f"{args[0]}:{n} {s} html-entity" for n, s in CFG["ent"]]
    out += [f"{args[0]}:{n} {s} {d}" for n, s, d in CFG["stray"]]
    extra = [f"{args[0]}:5-6 S903 words=26"] if CFG["badline"] else []
    print("\n".join(out + extra)); print(f"GATE_QUOTES: {len(out) + CFG['count_off']} findings"); sys.exit(CFG["exit55"])
if args and args[0].endswith("moved-copy.md"):
    out = [] if CFG["moved_blind"] else [f"{args[0]}:{n + 2} {s} {d}" for n, s, d in CFG["fix"]]
    print("\n".join(out)); print(f"GATE_QUOTES: {len(out)} findings"); sys.exit(1 if out else 0)
if args and args[0].endswith("entities.md"):
    out = [f"{args[0]}:{n} {s} {d}" for n, s, d in CFG["fix"]]
    print("\n".join(out)); print(f"GATE_QUOTES: {len(out)} findings")
    if CFG["crash"]:
        sys.stderr.write("Traceback (most recent call last):\n  stand-in crash\n")
    sys.exit(CFG["exitfix"])
if args and args[0].endswith("bad-utf8.md"):
    sys.stderr.write(f"GATE_QUOTES_ERROR: {'lesson' if CFG['nopath'] else args[0]}: not valid UTF-8\n")
    if CFG["badtrace"]:
        sys.stderr.write("Traceback (most recent call last):\n  stand-in crash\n")
    print("GATE_QUOTES: 0 findings"); sys.exit(CFG["exitbad"])
r = subprocess.run([sys.executable, "-B", BASE] + args, capture_output=True, text=True)
lines = r.stdout.splitlines()
if CFG["bump53"] and args and args[0].endswith("round-53.md"):
    idx = max(i for i, l in enumerate(lines) if " words=" in l)
    head, n = lines[idx].rsplit(" words=", 1)
    lines[idx] = f"{head} words={int(n) + 1}"
print("\n".join(lines)); sys.stderr.write(r.stderr)
sys.exit(CFG["exit52"] if CFG["exit52"] is not None and args and args[0].endswith("round-52.md") else r.returncode)
"""

GREEN = {"ent": ENT, "stray": [], "badline": False, "exit55": 1, "fix": FIXW, "crash": False,
         "exitfix": 1, "badtrace": False, "exitbad": 2, "bump53": False, "exit52": None,
         "selftest_fail": False, "moved_blind": False, "count_off": 0, "nopath": False}
CONTROLS = [
    ("GREEN", {}, 0, []),
    ("RED-ENTITY", {"ent": [e for e in ENT if e[1] != "S357"]}, 1, ["ENTITY"]),
    ("RED-ENTITY-LINE", {"ent": [[73, "S288"] if e[1] == "S288" else e for e in ENT]}, 1, ["ENTITY"]),
    ("RED-ENTITY-EXTRA", {"ent": ENT + [[73, "S289"]]}, 1, ["ENTITY"]),
    ("RED-NOFALSE", {"stray": [[73, "S289", "words=26"]]}, 1, ["NOFALSE"]),
    ("RED-EXIT", {"exit55": 0}, 1, ["EXIT"]),
    ("RED-EXIT-FIX", {"exitfix": 0}, 1, ["EXIT"]),
    ("RED-DECODE", {"fix": [f for f in FIXW if f[2] != "truncated-grounds"]}, 1, ["DECODE"]),
    ("RED-DECODE-ESC", {"fix": [f for f in FIXW if f[2] != "words=26"]}, 1, ["DECODE"]),
    ("RED-DECODE-FP", {"fix": FIXW + [[10, "S953", "html-entity"]]}, 1, ["DECODE"]),
    ("RED-ENTITY-DOUBLE", {"ent": ENT + [[72, "S288"]]}, 1, ["ENTITY"]),
    ("RED-DECODE-MOVED", {"moved_blind": True}, 1, ["DECODE"]),
    ("RED-DECODE-HEX", {"fix": [f for f in FIXW if f[1] != "S958"]}, 1, ["DECODE"]),
    ("RED-DECODE-ELLIPSIS", {"fix": [f for f in FIXW if f[2] != "words=5"]}, 1, ["DECODE"]),
    ("RED-KEEP", {"bump53": True}, 1, ["KEEP"]),
    ("RED-KEEP-EXIT", {"exit52": 0}, 1, ["KEEP"]),
    ("RED-BADUTF8", {"badtrace": True}, 1, ["BADUTF8"]),
    ("RED-BADUTF8-EXIT", {"exitbad": 1}, 1, ["BADUTF8"]),
    ("RED-BADUTF8-PATH", {"nopath": True}, 1, ["BADUTF8"]),
    ("RED-FORMAT-COUNT", {"count_off": 1}, 1, ["FORMAT"]),
    ("RED-FORMAT", {"badline": True}, 1, ["FORMAT"]),
    ("RED-FORMAT-CRASH", {"crash": True}, 1, ["FORMAT"]),
    ("RED-SELFTEST", {"selftest_fail": True}, 1, ["SELFTEST"]),
]


def main():
    lane, tree = sys.argv[1], sys.argv[2]
    rev = subprocess.run(["git", "-C", lane, "rev-parse", tree], capture_output=True, text=True, check=True).stdout.strip()
    tmp = tempfile.mkdtemp(prefix="kotodama-r56-c11o-")
    try:
        base = os.path.join(tmp, "base")
        os.mkdir(base)
        archive = subprocess.run(["git", "-C", lane, "archive", rev], capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", base], input=archive, check=True)
        print(f"measured-revision {rev} (git archive into a mktemp directory)")
        for p in INSTRUMENTS:
            print(f"sha256 {hashlib.sha256(open(os.path.join(base, p), 'rb').read()).hexdigest()}  {p}")
        print("argv (run from each copy's root): python3 -B reports/round-56/accept-o.py")
        base_run = subprocess.run(ARGV, cwd=base, capture_output=True, text=True)
        print(f"\n## BASE (all-false where the claim adds behaviour; not a control): exit {base_run.returncode}")
        print((base_run.stdout + base_run.stderr).rstrip())
        failures = 0
        for name, delta, want, expect in CONTROLS:
            copy = os.path.join(tmp, name)
            shutil.copytree(base, copy)
            tool = os.path.join(copy, "tools/check-gate-quotes.py")
            os.rename(tool, os.path.join(copy, "tools/check-gate-quotes-base.py"))
            cfg = dict(GREEN, **delta)
            open(tool, "w", encoding="utf-8").write(STANDIN % json.dumps(cfg))
            r = subprocess.run(ARGV, cwd=copy, capture_output=True, text=True)
            legs = re.findall(r"^(\w+) (PASS|FAIL)", r.stdout, re.M)
            failing = [l for l, v in legs if v == "FAIL"]
            ok = r.returncode == want and failing == expect and len(legs) == 8
            failures += not ok
            print(f"\n## {name}: exit {r.returncode} (expected {want}); failing legs {failing}; "
                  f"{'AS EXPECTED' if ok else 'NOT AS EXPECTED'}")
            print((r.stdout + r.stderr).rstrip())
        print(f"\nCONTROLS {len(CONTROLS) - failures}/{len(CONTROLS)} as expected")
        return 1 if failures else 0
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    sys.exit(main())
