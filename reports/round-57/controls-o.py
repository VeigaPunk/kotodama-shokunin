#!/usr/bin/env python3
r"""Round-57 claim O pre-data controls (addendum §9: score the cheapest skip-the-work control and the
cheapest shortcuts under the frozen counter before any data). Run from the lane root:

  python3 -B reports/round-57/controls-o.py

Each control is a checker scored with `python3 -B reports/round-57/accept-o.py --tool <control>`,
without --seed (as the counting command runs). Expected: every red control exits 1 with
`ACCEPT-O-57: FAIL` and its named legs print FAIL; the green control exits 0 with `ACCEPT-O-57: PASS`.

Built here from the base tool (written under /fast/scratch/hyaku/kotodama-r57/controls-o):
  base       the base tool, tools/check-gate-quotes.py at 86d08883 unchanged (do nothing)
             -> GEN, REAL (bare numeric references unreported) and MUTANTS (three survivors)
  sidcheat   the round-56 build critic's S-id-keyed checker (reports/round-57/controls/sidcheat-tool.py,
             a byte copy of /fast/scratch/hyaku/kotodama-r56/CriticClaimO56/variant-tool.py, sha256
             e3060c1c...), GQ_MODE=sidcheat: the shortcut that passed the round-56 counter -> GEN
  shortlist  base plus the bare-numeric grammar, named references limited to thirteen common names
             (a short-list decoder) -> GEN
  anyamp     base plus the bare-numeric grammar, every `&name;` counted as a reference without the
             HTML5 table (a label-keyed shortcut) -> GEN
  hashpin    base plus the bare-numeric grammar (the whole GEN fix) and a selftest that fails when
             its own file's sha256 changes (kills every on-disk mutant, tests no behaviour) -> MUTANTS
  keepbreak  base with its summary line worded `finding(s)` (an output drift) -> KEEP, FORMAT
  stderrnoise base writing one note line to stderr on every lesson run -> FORMAT
Byte copies of the pre-dispatch critic's checkers (reports/round-57/controls/critic-o/, from
/fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/tools/), each with its EXACT failing-leg set:
  honest                  base + `;?` grammar + five behavioural selftest cases -> GREEN (all PASS)
  cheat-identity          function-identity selftest, no behavioural case      -> exactly MUTANTS
  cheat-replay-identity   replays accept-o's generator from the seed in the path -> GEN, REAL, MUTANTS
  cheat-seatgen-identity  bare numerics only on rows carrying `Seat: Gen.`      -> GEN, REAL, MUTANTS
  red-gen                 honest with hex keeping its `;`                       -> exactly GEN, REAL
  red-multi               honest dropping findings when the last path is unreadable -> exactly MULTI
  red-keep                honest printing the ellipsis class name               -> exactly KEEP
  red-format              honest with a stderr note on large registries         -> exactly FORMAT, REAL
  red-selftest            honest whose --selftest also runs paths (exit 2)      -> exactly SELFTEST
Exit 0 when every control behaves as expected; 1 otherwise.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

BASE = "86d08883e3c2a04f35db1aae7bde6b9d889f53b1"
SCRATCH = "/fast/scratch/hyaku/kotodama-r57/controls-o"
SIDCHEAT = "reports/round-57/controls/sidcheat-tool.py"
SIDCHEAT_SHA = "e3060c1c0daf9e6682c4e4b06d1dab13a5848f76b082cd701826828a5f609a3e"
OLD_RE = 'HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;|#[xX][0-9A-Fa-f]+;|[A-Za-z][A-Za-z0-9]*;)")'
BARE_RE = 'HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;?|#[xX][0-9A-Fa-f]+;?|[A-Za-z][A-Za-z0-9]*;)")'
OLD_TEST = 'if reference.startswith("&#") or reference[1:] in HTML5_ENTITIES:'
SHORT = ('if reference.startswith("&#") or reference[1:] in {"quot;", "amp;", "hellip;", "rsquo;", '
         '"lsquo;", "ldquo;", "rdquo;", "mdash;", "ndash;", "nbsp;", "copy;", "eacute;", "mldr;"}:')
ANY = 'if True:'
SELFTEST_HEAD = 'def selftest():\n    """Cases exercising spans, row shapes, word counts, and ellipsis rules."""\n'
EXPECT = {"base": ["GEN", "REAL", "MUTANTS"], "sidcheat": ["GEN"], "shortlist": ["GEN"], "anyamp": ["GEN"],
          "hashpin": ["MUTANTS"], "keepbreak": ["KEEP", "FORMAT"], "stderrnoise": ["FORMAT"]}
SUMMARY_LINE = 'print("GATE_QUOTES: %d findings" % total)'
RUN_HEAD = '    results = check(paths)\n'


def swap(text, old, new):
    if text.count(old) != 1:
        raise SystemExit(f"CONTROLS_O_INPUT_ERROR anchor not found once: {old[:60]}")
    return text.replace(old, new)


def hashpin(text):
    pin = ('    import hashlib as _h\n'
           '    _own = [l for l in open(__file__, encoding="utf-8").read().split("\\n") if "PINNED_SELF" not in l]\n'
           '    if _h.sha256("\\n".join(_own).encode()).hexdigest() != "%s":  # PINNED_SELF\n'
           '        print("SELFTEST: file changed")\n        return 1\n')
    zero = "0" * 64
    draft = swap(text, SELFTEST_HEAD, SELFTEST_HEAD + pin % zero)
    own = [l for l in draft.split("\n") if "PINNED_SELF" not in l]
    return draft.replace(zero, hashlib.sha256("\n".join(own).encode()).hexdigest())


def build(root):
    base = subprocess.run(["git", "-C", root, "show", f"{BASE}:tools/check-gate-quotes.py"],
                          capture_output=True, text=True, check=True).stdout
    bare = swap(base, OLD_RE, BARE_RE)
    sid = open(os.path.join(root, SIDCHEAT), encoding="utf-8").read()
    if hashlib.sha256(sid.encode()).hexdigest() != SIDCHEAT_SHA:
        raise SystemExit("CONTROLS_O_INPUT_ERROR sidcheat copy differs from the round-56 critic's tool")
    return {"base": base, "sidcheat": sid, "shortlist": swap(bare, OLD_TEST, SHORT),
            "anyamp": swap(bare, OLD_TEST, ANY), "hashpin": hashpin(bare),
            "keepbreak": swap(base, SUMMARY_LINE, 'print("GATE_QUOTES: %d finding(s)" % total)'),
            "stderrnoise": swap(base, RUN_HEAD, RUN_HEAD + '    print("note: scanning", file=sys.stderr)\n')}


CRITIC = "reports/round-57/controls/critic-o"
EXACT = {"honest": [], "cheat-identity": ["MUTANTS"], "cheat-replay-identity": ["GEN", "MUTANTS", "REAL"],
         "cheat-seatgen-identity": ["GEN", "MUTANTS", "REAL"], "red-gen": ["GEN", "REAL"],
         "red-multi": ["MULTI"], "red-keep": ["KEEP"], "red-format": ["FORMAT", "REAL"],
         "red-selftest": ["SELFTEST"]}


def main():
    root = os.getcwd()
    os.makedirs(SCRATCH, exist_ok=True)
    ok_all = True
    tools = {}
    for name, text in build(root).items():
        path = os.path.join(SCRATCH, f"{name}.py")
        open(path, "w", encoding="utf-8").write(text)
        tools[name] = path
    for name in EXACT:
        tools[name] = os.path.join(root, CRITIC, f"{name}.py")
    for name, path in tools.items():
        text = open(path, encoding="utf-8").read()
        env = dict(os.environ, GQ_MODE="sidcheat") if name == "sidcheat" else dict(os.environ)
        done = subprocess.run([sys.executable, "-B", "reports/round-57/accept-o.py", "--tool", path],
                              cwd=root, capture_output=True, text=True, env=env, timeout=900)
        legs = dict(re.findall(r"^([A-Z]+) (PASS|FAIL)\b", done.stdout, re.M))
        failed = sorted(k for k, v in legs.items() if v == "FAIL")
        if name == "honest":
            ok = done.returncode == 0 and "ACCEPT-O-57: PASS" in done.stdout and not failed
            want = "GREEN"
        elif name in EXACT:
            ok = done.returncode == 1 and "ACCEPT-O-57: FAIL" in done.stdout and failed == EXACT[name]
            want = f"exactly {EXACT[name]}"
        else:
            ok = (done.returncode == 1 and "ACCEPT-O-57: FAIL" in done.stdout
                  and all(legs.get(leg) == "FAIL" for leg in EXPECT[name]))
            want = f"at least {EXPECT[name]}"
        ok_all &= ok
        print(f"## control {name} sha256 {hashlib.sha256(text.encode()).hexdigest()} exit {done.returncode} "
              f"failed_legs {failed} expected {want} -> {'AS-EXPECTED' if ok else 'UNEXPECTED'}")
        for line in done.stdout.splitlines():
            print("   " + line[:400])
        if done.stderr.strip():
            print("   stderr: " + done.stderr.strip()[:400])
    print(f"CONTROLS-O-57: {'every control as expected (reds fail, green passes)' if ok_all else 'a control did not behave as expected'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
