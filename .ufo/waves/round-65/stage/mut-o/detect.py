#!/usr/bin/env python3
"""Bounded behavioral detector for the round-65 FULL/MUTEX/FRAG legs.

Five probes, run against one candidate accept-o.py byte file:

  F   FULL leg under `--only FULL` on a scratch root whose tool is a no-op
      stub.  The subprocess re-run's leg universe is visible in the parent's
      FULL line (`pass=<n>/<denominator> skip=<k>`): the frozen contract is
      23 legs (CORE 13 + EDGE 7 + TOOL,DRIP,MUT) and 3 SKIPs
      (FULL,MUTEX,FRAG).  A FULL --only list that gains FRAG moves the
      observable to /24 and skip=2.
  S   the filtered-run suffix: `--only TOOL` on the stub root must print
      `ACCEPT-O-65: PASS [filtered: 1/26 legs]`; dropping the suffix makes a
      filtered run present as the unfiltered verdict.
  M   MUTEX exactness comparison exercised in-process with pinned measured
      failing-leg sets per mutant (real MUTANTS needles, real comparison
      code, fake measurement transport).  Pristine pins reproduce MUTEX PASS;
      emptying m1's disclosed extras must FAIL with `m1:measured=...`.
  G1  FRAG with a checker whose --selftest exits 1 while the scan prints
      `0 finding(s)`: the frozen leg must FAIL; dropping the selftest
      requirement makes it PASS.
  G2  FRAG with a checker whose scan prints `2 finding(s)` and exits 0:
      the frozen leg must FAIL; weakening `0 finding` to `finding` makes it
      PASS.

Usage: detect.py <candidate.py> <tag>
Exit 0 when the candidate matches the pristine contract, 1 when any probe
deviates (a mutant is detected), 2 on harness error.
"""
import contextlib
import hashlib
import importlib.util
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
REAL_TOOL = os.path.join(LANE, "tools", "reopen-row.py")

STUB_TOOL = "#!/usr/bin/env python3\nimport sys\nsys.exit(0)\n"

FAKE_FRAG_SELFTEST_RED = """#!/usr/bin/env python3
import sys
if "--selftest" in sys.argv:
    print("SELFTEST: FAIL 0/9")
    sys.exit(1)
print("FRAG: 0 finding(s) in 26 file(s)")
sys.exit(0)
"""

FAKE_FRAG_SCAN_RED = """#!/usr/bin/env python3
import sys
if "--selftest" in sys.argv:
    print("SELFTEST: PASS 9/9")
    sys.exit(0)
print("FRAG: 2 finding(s) in 26 file(s)")
sys.exit(0)
"""

MUTANT_ORDER = ["m1", "m10", "m2", "m3", "m9", "m5", "m6", "m7", "m8", "mread"]
EDGE = ["EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS", "EDGE_MALTARG",
        "EDGE_SLASHLESS", "EDGE_308", "EDGE_5TH200"]
MEASURED = {
    "m1": ["EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS"],
    "m10": ["EDGE_USERINFO"],
    "m2": ["EDGE_USERINFO", "EDGE_MALTARG"],
    "m3": ["EDGE_HTTPS"],
    "m9": ["EDGE_MALTARG"],
    "m5": ["EDGE_SLASHLESS"],
    "m6": ["EDGE_308"],
    "m7": ["EDGE_5TH200"],
    "m8": ["GEN", "BOUND"],
    "mread": ["DRIP"],
}
SWEEP_ROWS = [f"{m}:{'+'.join(sorted(MEASURED[m]))}" for m in MUTANT_ORDER]

# tag -> {probe: expected signature}
EXPECT = {
    "m1_full_only_gains_frag": {"F": (["/24", "skip=2", "unexpected_skip=[]"], [])},
    "m2_suffix_marker_removed": {"S": (["ACCEPT-O-65: PASS"], ["[filtered:"])},
    "m3_mutex_m1_extras_emptied": {"M": (["MUTEX FAIL", "m1:measured=", "['EDGE_SCHEMEREL']"], [])},
    "m4_frag_selftest_requirement_dropped": {"G1": (["FRAG PASS", "selftest=exit1", "files=26/26"], [])},
    "m5_frag_scan_check_weakened": {"G2": (["FRAG PASS", "scan=exit0", "files=26/26"], [])},
}
# NOTE ON THE M PROBE BASELINE.  The frozen MUTEX leg is already red on
# pristine bytes: its failed-line regex `^[A-Z_]+ FAIL` cannot match
# EDGE_308 / EDGE_5TH200 (digits), so m6/m7 measure as NONE and SWEEP_EXPECT
# can never be satisfied.  This is an instrument defect, not a mutant.  The M
# probe is therefore differential: pristine must show the m6/m7 regex
# deviations and must NOT show any `m1:measured=`; mutant m3 is attributed
# only if it *adds* the m1 exactness deviation on identical pinned
# measurements.  (Receipt corroboration: dry-run-o.txt already prints
# m6:NONE, m7:NONE at base.)
PRISTINE_ONLY = {
    "F": (["FULL FAIL", "/23", "skip=3", "unexpected_skip=[]"], []),
    "S": (["[filtered: 1/26 legs]"], []),
    "M": (["MUTEX FAIL", "stale_or_mismatch"], ["m1:measured="]),
    "G1": (["FRAG FAIL", "selftest=exit1", "files=26/26"], []),
    "G2": (["FRAG FAIL", "scan=exit0", "files=26/26"], []),
}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def scratch(prefix):
    root = tempfile.mkdtemp(prefix=prefix)
    os.makedirs(os.path.join(root, "tools"))
    return root


def write_stub_tool(root):
    p = os.path.join(root, "tools", "reopen-row.py")
    open(p, "w", encoding="utf-8").write(STUB_TOOL)
    os.chmod(p, 0o755)


def run(candidate, root, only, timeout=300):
    proc = subprocess.run([sys.executable, "-B", candidate, "--root", root,
                           "--only", only], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=timeout, cwd=HERE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), \
        proc.stderr.decode("utf-8", "replace")


def probe_f(candidate):
    root = scratch("probe-f-")
    try:
        write_stub_tool(root)
        rc, out, err = run(candidate, root, "FULL")
        line = next((l for l in out.splitlines() if re.match(r"^FULL (PASS|FAIL) ", l)), None)
        return f"rc={rc} {line} stderr={err.strip()[:120]}", line or out
    finally:
        shutil.rmtree(root, ignore_errors=True)


def probe_s(candidate):
    root = scratch("probe-s-")
    try:
        write_stub_tool(root)
        rc, out, err = run(candidate, root, "TOOL")
        line = next((l for l in out.splitlines() if l.startswith("ACCEPT-O-65:")), None)
        return f"rc={rc} {line}", line or out
    finally:
        shutil.rmtree(root, ignore_errors=True)


def probe_frag(candidate, fake_source):
    root = scratch("probe-g-")
    try:
        write_stub_tool(root)
        fp = os.path.join(root, "tools", "check-row-fragments.py")
        open(fp, "w", encoding="utf-8").write(fake_source)
        os.chmod(fp, 0o755)
        rc, out, err = run(candidate, root, "FRAG")
        line = next((l for l in out.splitlines() if re.match(r"^FRAG (PASS|FAIL) ", l)), None)
        return f"rc={rc} {line}", line or out
    finally:
        shutil.rmtree(root, ignore_errors=True)


def fake_run_tool(tool, cwd, args, timeout=900):
    """Pinned measurements per mutant; the real comparison code consumes them."""
    root = args[args.index("--root") + 1]
    name = os.path.basename(root).split("xroot-", 1)[1]
    failed = set(MEASURED[name])
    legs = list(EDGE) + ["DRIP"] + (["GEN", "BOUND"] if name == "m8" else [])
    lines = [f"{leg} {'FAIL' if leg in failed else 'PASS'} measured={name}"
             for leg in legs]
    return 1, "\n".join(lines) + "\nACCEPT-O-65: FAIL [filtered: 9/26 legs]\n", "", 0.01


def probe_m(candidate, tag):
    root = tempfile.mkdtemp(prefix="probe-m-")
    try:
        os.makedirs(os.path.join(root, "tools"))
        shutil.copyfile(REAL_TOOL, os.path.join(root, "tools", "reopen-row.py"))
        os.chmod(os.path.join(root, "tools", "reopen-row.py"), 0o755)
        rec = os.path.join(root, "reports", "round-65", "telemetry")
        os.makedirs(rec)
        # deliberately STALE receipt (rows below are the pinned measurement,
        # not a fresh sweep): isolates the exactness comparison from the
        # revision-3 receipt-freshness/tool-sha path (which on rev4 crashes
        # with NameError: hashlib before it can compare).
        open(os.path.join(rec, "exactness-sweep-o65.txt"), "w",
             encoding="utf-8").write(
            "# stale receipt for probe isolation\n# rows\n"
            + "\n".join(["x"] * len(SWEEP_ROWS)) + "\n")
        spec = importlib.util.spec_from_file_location(f"cand_{tag}", candidate)
        mod = importlib.util.module_from_spec(spec)
        sys.dont_write_bytecode = True
        spec.loader.exec_module(mod)
        real_run_tool = mod.run_tool
        mod.run_tool = fake_run_tool
        argv = sys.argv
        sys.argv = ["accept-o.py", "--root", root, "--only", "MUTEX"]
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = mod.main()
        finally:
            sys.argv = argv
            mod.run_tool = real_run_tool
        out = buf.getvalue()
        line = next((l for l in out.splitlines() if re.match(r"^MUTEX (PASS|FAIL) ", l)), None)
        return f"rc={rc} {line}", line or out
    finally:
        shutil.rmtree(root, ignore_errors=True)


def main():
    candidate = os.path.abspath(sys.argv[1])
    tag = sys.argv[2]
    print(f"CANDIDATE tag={tag} sha256={sha(candidate)} path={candidate}")
    prose = {
        "F": probe_f(candidate),
        "S": probe_s(candidate),
        "M": probe_m(candidate, tag),
        "G1": probe_frag(candidate, FAKE_FRAG_SELFTEST_RED),
        "G2": probe_frag(candidate, FAKE_FRAG_SCAN_RED),
    }
    expect = dict(PRISTINE_ONLY)
    expect.update(EXPECT.get(tag, {}))
    deviations = []
    for name in ("F", "S", "M", "G1", "G2"):
        observed, raw = prose[name]
        wanted, forbidden = expect[name]
        ok = (all(w in observed for w in wanted)
              and not any(f in observed for f in forbidden))
        print(f"PROBE {name} expected={wanted} forbidden={forbidden} "
              f"ok={ok} observed={observed}")
        if not ok:
            deviations.append(f"{name}:{observed}")
    verdict = "MUTANT_DETECTED" if deviations else "CLEAN"
    print(f"DETECTOR {tag}: {verdict} deviations={deviations}")
    return 1 if deviations else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:  # harness error is never a verdict
        import traceback
        traceback.print_exc()
        print(f"HARNESS_ERROR {error}")
        sys.exit(2)
