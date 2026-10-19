# O10 — exit-code verifier: contract matrix, executable suite, and the prototype's inverted numbering

- Seat: `O10` | role verifier | claim `O` | round 47, loop 2
- Out path: `reports/round-47/op/O10-exit-codes.md` (the only write by this seat)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`); declared `6e9a30d` (`reports/round-47/claims.json:7`)
- Observation cut: **2026-10-19T17:55Z** (UTC), re-checked at 17:58Z before filing
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root; Python 3.14.7
- Boundary: no filed byte edited; no corpus write or staging; no `reports/round-*/run-validation.py`; no git commit/push/install/network. Fixtures and the suite live only under `.scratch/o10/` plus the fenced copies in this file.

## 1. Verdict

**The durable target `tools/harness/claims-freshness.py` does not exist at this cut, so the exit-code contract is `could-not-evaluate` for the deliverable — not green.** The only extant implementation is the r44 scratch prototype `.scratch/ca01/claims-freshness.py` (`sha256 dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434`). It emits the **right flags** on r43 (O and C STALE, Ca FRESH) but the **wrong exit codes**: 2 for stale, 1 for malformed, and 0 for could-not-evaluate when `--allow-unverifiable` is passed.

I built the conformance suite the integrator and V02 can run verbatim once the tool lands. It is calibrated green (14/14) against a minimal compliant double and red (11/15 failures) against the prototype.

| target | status at cut | basis |
|---|---|---|
| `tools/harness/claims-freshness.py` | **ABSENT → could-not-evaluate** | `ls` returns no such file |
| exit-code conformance suite | **built, self-calibrated** | 14/14 PASS vs compliant double; 11 failures vs prototype |
| `.scratch/ca01/claims-freshness.py` (prototype) | **NONCONFORMING** | stale→2, malformed→1, C-N-E→0 under a flag |

No axis is harmed by this report; the harm is latent in a durable tool that copies the prototype's numbering.

## 2. Contract under test

The closed exit-code contract is stated twice, consistently:

| condition | required code | source |
|---|---|---|
| every claim `FRESH` | **0** | `reports/round-44/review/R01-review.md:246` |
| any claim `STALE` | **1** | `reports/round-44/review/R01-review.md:246`; `reports/round-47/claims.json:41` |
| malformed input (bad JSON, no `baseline_commit`, no `claims`, claim missing `id`/`before`, unknown probe kind) | **2** | `reports/round-44/review/R01-review.md:246` |
| claim declares no checks (`could-not-evaluate`) | **non-zero, never 0** | `reports/round-44/review/R01-review.md:246`; `reports/round-47/claims.json:47` |

The declared check schema is `{clause, probe_kind, target, expect, evidence_command}` under a per-claim `before_checks` list, with the closed probe set `path_absent|path_present|grep_absent|grep_present|count_eq|sha256_eq|topic_owner_absent|capability_present` (`reports/round-44/review/R01-review.md:245`). This seat's suite pins that schema because the exit contract cannot be exercised on a tool that reads a different field.

## 3. Method and fixtures

- Every fixture is a claims file evaluated at the real r43 baseline `7ceff59` in this repo. No fixture repository, no commit, no worktree mutation is needed. The two live facts used are: `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at `7ceff59`, and `corpus/knowledge/no-such-register-o10.md` does not.
- The suite invokes the tool as `python3 -B <tool> --claims <fixture> --root <repo>` and asserts the **exit status only**; text output is inspected only for the optional r43 demo. Exit status is the contract: wrappers must be able to branch on it without parsing prose.
- The `fresh-all` fixture declares two holding clauses; `stale-one` declares one holding and one contradicted clause; `stale-topic` contradicts a `topic_owner_absent` clause against the real lithic owner; `mixed` combines a fresh and a stale claim; `mixed-stale-cne` combines a stale claim with a no-checks claim; `cne-empty`/`cne-missing` declare no evaluable checks; six malformed shapes cover non-JSON, no baseline, no claims, missing id, missing `before`, unknown probe kind, and an unresolvable baseline.
- A suite-level invariant records every exit-0 result and fails if any case other than `fresh-all` returns 0. That is the mechanical form of "exit 0 only for all-fresh".

## 4. Measurements

### 4.1 Durable target absent

```
$ ls -la tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
```

`find reports/round-47 -type f` at the cut shows only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`, `calib/Ca02-resolver-edge.md`. No O-seat tool draft had landed when this seat ran.

### 4.2 Prototype, native inputs and native schema

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json; echo "exit=$?"
[O] operability -- STALE (0/2 premises hold)
[C] coverage -- STALE (2/3 premises hold)
[Ca] calibration -- FRESH (1/1 premises hold)
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
REFUSE: claims O, C have a `before` already false at 7ceff59a0216a8ea21ee43262d9fc72abf770cee; do not dispatch.
exit=2
```

The flags are correct (the O claim's regression condition), but **stale exits 2**. Secondary probes on the same prototype:

| probe | command | exit |
|---|---|---|
| no checks declared | `--claims .scratch/o10/cne.json` | **3** (non-zero, acceptable under "never 0") |
| no checks + override flag | same + `--allow-unverifiable` | **0 → violates never-green** |
| non-JSON | `--claims .scratch/o10/bad.json` | **1** (contract wants 2) |
| selftest | `--selftest` | **1**, `selftest 17/19 FAIL` (matches the r44 review) |

### 4.3 Suite calibration against a compliant double

A 120-line reference double (`.scratch/o10/reference-stub.py`, `sha256 a6b099b7947127276b682a4078d00b918554994a44f81cdbe5b7565e2b1b9828`) implementing `0/1/2/3` exactly:

```
$ python3 -B .scratch/o10/exit-conformance.py --tool .scratch/o10/reference-stub.py --root .
case                       want    got     verdict
fresh-all                  0       0       PASS
stale-one                  1       1       PASS
stale-topic                1       1       PASS
mixed                      1       1       PASS
mixed-stale-cne            nonzero 1       PASS
cne-empty                  nonzero 3       PASS
cne-missing                nonzero 3       PASS
malformed-no-baseline      2       2       PASS
malformed-no-claims        2       2       PASS
malformed-missing-id       2       2       PASS
malformed-missing-before   2       2       PASS
malformed-unknown-probe    2       2       PASS
malformed-bad-baseline     nonzero 2       PASS
malformed-nonjson          2       2       PASS
14 case(s), 0 failure(s)
EXIT-CONFORMANCE: PASS          # suite exit 0
```

This is the suite's own negative control: it is capable of going green, so the red result below is not a permanently failing harness.

### 4.4 Suite against the prototype

With contract-shaped fixtures the prototype treats every claim as ungrounded — it reads `freshness_probes`/mined prose, not `before_checks` — and then adds the exit-code defects:

```
$ python3 -B .scratch/o10/exit-conformance.py --tool .scratch/ca01/claims-freshness.py --root .
case                       want    got     verdict
fresh-all                  0       3       FAIL
stale-one                  1       3       FAIL
stale-topic                1       3       FAIL
mixed                      1       3       FAIL
mixed-stale-cne            nonzero 3       PASS
cne-empty                  nonzero 3       PASS
cne-missing                nonzero 3       PASS
malformed-no-baseline      2       3       FAIL
malformed-no-claims        2       1       FAIL
malformed-missing-id       2       1       FAIL
malformed-missing-before   2       3       FAIL
malformed-unknown-probe    2       3       FAIL
malformed-bad-baseline     nonzero 1       PASS
malformed-nonjson          2       1       FAIL
cne-allow-flag             nonzero 0       FAIL
15 case(s), 11 failure(s)
EXIT-CONFORMANCE: FAIL          # suite exit 1
```

The `malformed-missing-id` failure is an uncaught crash, not a return code: the prototype prints a `TypeError` traceback (`sequence item 0: expected str instance, NoneType found`) and exits 1 through the interpreter, not through its handler.

## 5. Findings

**O10-F1 — blocker: stale and malformed codes are inverted in the only extant implementation.** The r43 native run proves it independently of my schema: `[O] STALE`, `[C] STALE`, `[Ca] FRESH`, then `exit=2`. The contract assigns 1 to stale and 2 to malformed (`R01-review.md:246`). A wrapper that treats 2 as "broken claims file" will silently classify the round's most important refusal as a tool failure; a wrapper that treats non-zero uniformly cannot tell an operator which repair to make. The durable tool must return 1 for the r43 demo and reserve 2 for malformed input.

**O10-F2 — blocker: could-not-evaluate can exit 0.** `.scratch/o10/cne.json` declares a claim with no checks. Default run: exit 3. With `--allow-unverifiable`: exit **0**, while the same run still prints `REFUSE: claims N1 yield no groundable premise`. The claim's threshold is unconditional: "could-not-evaluate != green (exits non-zero when no checks declared)" (`reports/round-47/claims.json:47`). A flag that turns this into 0 makes the gate skippable by the exact operator it is meant to constrain. Recommended: remove the flag, or keep it as a reporting override that still exits non-zero.

**O10-F3 — malformed input is handled by crash or silent fallback, never by exit 2.** Measured: no `claims` list → exit 1 with a clean message; non-JSON → exit 1; missing claim `id` → uncaught `TypeError` traceback; missing `before_checks` → treated as unverifiable (exit 3); **missing `baseline_commit` → the prototype evaluates the worktree** (`source: worktree`) and returns 3 instead of declaring the file malformed. The last is the dangerous one: it silently substitutes live bytes for the declared baseline, which is the r43 defect class in the opposite direction. The durable tool must reject a missing or unresolvable `baseline_commit` with 2 and must never fall back to the worktree.

**O10-F4 — schema: the prototype does not consume the declared `before_checks` list.** All 14 contract-shaped fixtures are reported `UNVERIFIABLE`/`ungrounded` because the prototype mines `before` prose. That is why it cannot be exonerated on stale→1 even if the numbering were fixed: there is no way to declare a checked clause. The durable tool must implement `{clause, probe_kind, target, expect, evidence_command}` per claim (O02's mission) and treat an unknown `probe_kind` as a schema rejection, exit 2 — not as unverifiable, which would silently drop a typo'd clause.

**O10-F5 — precedence must be declared, not inferred.** The contract pins the individual codes but not their order when a file mixes conditions. Recommended and tested: **malformed (2) > stale (1) > could-not-evaluate (any non-zero, 3 recommended) > fresh (0)**, with 0 only when every claim is fresh and every claim declared at least one check. The suite treats `mixed-stale-cne` as non-zero (a compliant tool may choose 1 or 3) and asserts 1 for a pure stale file. O03 should state the precedence in the tool's `--help`/docstring so wrappers do not guess.

**O10-F6 — the r43 demonstration artifact must exit 1, not inherit the prototype's 2.** The O claim requires "a filed demonstration at `reports/round-47/calib/`" that flags r43 O and C stale and Ca fresh (`reports/round-47/claims.json:41`). When O05's annotated claims file lands, the integrator must run it through the durable tool and require exit 1. The suite's `--r43-demo <path>` does exactly this and additionally checks the three verdict tokens (advisory). No such artifact existed at my cut (`reports/round-47/calib/` held only `Ca02-resolver-edge.md`), so this clause is `could-not-evaluate`.

## 6. Requirements the durable tool must meet

| # | requirement | verified by |
|---|---|---|
| R1 | exit 0 iff every claim is fresh and every claim declared ≥1 check | `fresh-all` |
| R2 | exit 1 if any claim is stale, even when other claims are fresh | `stale-one`, `mixed` |
| R3 | exit 2 for non-JSON, missing baseline, missing claims, missing id/before, unknown probe kind | six malformed cases |
| R4 | exit 2, never worktree fallback, for an unresolvable baseline | `malformed-bad-baseline` (non-zero; 2 preferred) |
| R5 | no-checks claim exits non-zero by default and cannot be made 0 by a helper flag | `cne-empty`, `cne-missing`, `cne-allow-flag` |
| R6 | malformed wins over stale; stale wins over C-N-E; 0 only for all-fresh | matrix + exit-0 invariant |
| R7 | no traceback for any malformed shape | malformed cases |
| R8 | r43 annotated demo exits 1 with O,C STALE and Ca FRESH | `--r43-demo` |

## 7. Integration run (exact commands)

Extract the suite from Appendix A, verify its digest, then run it against the landed tool. The expected suite digest is `374f5021373779763616572b1d3442de01bf58e683d934558e47b1d5b3c645f3`.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
awk '/^```python$/{f=1;next} /^```$/{if(f)exit} f' \
  reports/round-47/op/O10-exit-codes.md > .scratch/o10/exit-conformance.py
sha256sum .scratch/o10/exit-conformance.py   # must equal 374f5021…645f3
python3 -B .scratch/o10/exit-conformance.py \
  --tool tools/harness/claims-freshness.py --root . \
  --r43-demo reports/round-47/calib/<annotated-r43-claims>.json
echo "suite_exit=$?"
```

- `suite_exit=0` with `14 case(s), 0 failure(s)` and `r43-demo … PASS` → exit contract conforms.
- `suite_exit=1` → at least one contract clause fails; do not present O as delivered. Record which row failed in `validation.json`.
- `suite_exit=2` → tool absent or uninvokable; that is `could-not-evaluate`, not green.

The suite is fail-closed: a missing tool, a missing r43 demo, or an invocation error never yields exit 0.

## 8. Clause status and open items

| clause | status at cut |
|---|---|
| exit 0 only for all-fresh | suite case defined; durable unverified |
| exit 1 for stale | **prototype violates (2)**; durable unverified |
| exit 2 for malformed | **prototype violates (1 or crash)**; durable unverified |
| C-N-E never green | prototype default 3 (ok), flag path 0 (**violates**) |
| r43 demo exits 1 | artifact absent at cut → could-not-evaluate |

`to-verify`:

- The durable tool's actual check-field name and `expect` type; this suite pins `before_checks` / boolean `expect` from `R01-review.md:245`.
- Whether O03 pins the precedence I recommend in F5; if it chooses a different order, R6 is the only row that needs reinterpretation.
- Which code the durable tool uses for C-N-E (any non-zero passes; 3 is recommended and matches the prototype's default).
- Where O05's annotated r43 file lands; the suite accepts any path via `--r43-demo`.

## 9. Provenance and write surface

| artifact | sha256 |
|---|---|
| `.scratch/o10/exit-conformance.py` (Appendix A) | `374f5021373779763616572b1d3442de01bf58e683d934558e47b1d5b3c645f3` |
| `.scratch/o10/reference-stub.py` (Appendix B) | `a6b099b7947127276b682a4078d00b918554994a44f81cdbe5b7565e2b1b9828` |
| suite run vs compliant double | `5c739ab14ddedd0456d612f3738772a09d2b10c3e5e83839ce08c32853bea38c` |
| suite run vs prototype | `4f7a027110a28d4ed2ab39ce0961de4624a147206ac9ef0c874d26cc72541b8c` |
| prototype at cut | `dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434` |

`git status --porcelain` at the cut: only the pre-existing `?? reports/round-46/review/` and the round-47 tree; no modified tracked file, nothing under `corpus/`. The `.scratch/o10/` fixtures and run logs are transient; the fenced suite and double below are the durable copies.

---

## Appendix A — exit-code conformance suite (verbatim)

```python
#!/usr/bin/env python3
"""Exit-code conformance suite for the r47 claims-freshness gate (seat O10).

Contract under test (reports/round-47/claims.json, claim O):
  exit 0  all claims FRESH
  exit 1  at least one claim STALE
  exit 2  malformed input (bad JSON, no baseline_commit, no claims, claim
          missing id/before, unknown probe kind)
  nonzero could-not-evaluate (claim declares no before_checks) -- never 0

The suite writes only under .scratch/ (fixtures) and reads the lane repo.
It never edits a filed byte and never runs a round runner.

Suite exit codes: 0 = all cases conform; 1 = conformance failure;
2 = could-not-evaluate (tool absent or uninvokable).
"""
import argparse
import json
import os
import re
import subprocess
import sys

BASELINE = "7ceff59"  # r43 baseline, reachable in the lane repo
MINERAL = "corpus/knowledge/myth-symbol/mineral-stone-symbolism.md"
ABSENT = "corpus/knowledge/no-such-register-o10.md"


def envelope(claims, baseline=BASELINE):
    return {
        "round": 47,
        "regimen": "REGIMEN.md",
        "loop": 2,
        "declared_at_utc": "2026-10-19T17:46:52Z",
        "baseline_commit": baseline,
        "axes_in_play": ["coverage", "operability", "calibration"],
        "claims": claims,
    }


def claim(cid, checks, before="synthetic O10 fixture"):
    return {
        "id": cid,
        "axis": "operability",
        "claim": "synthetic exit-code conformance fixture",
        "before": before,
        "after_required": "n/a (fixture)",
        "counting_commands": ["true"],
        "thresholds": "n/a (fixture)",
        "before_checks": checks,
    }


def chk(kind, target, expect, clause="fixture clause"):
    return {
        "clause": clause,
        "probe_kind": kind,
        "target": target,
        "expect": expect,
        "evidence_command": "git show %s:%s" % (BASELINE, target),
    }


FIXTURES = {
    # --- green path -------------------------------------------------------
    "fresh-all.json": envelope([
        claim("F1", [
            chk("path_absent", ABSENT, True, "the gap is unowned"),
            chk("path_present", MINERAL, True, "the witness entry exists"),
        ]),
    ]),
    # --- stale paths ------------------------------------------------------
    "stale-one.json": envelope([
        claim("S1", [
            chk("path_absent", ABSENT, True, "the gap is unowned"),
            chk("path_absent", MINERAL, True, "the register slot is unbuilt"),
        ]),
    ]),
    "stale-topic.json": envelope([
        claim("S2", [
            chk("topic_owner_absent", "lithic", True, "no lithic owner"),
        ]),
    ]),
    "mixed.json": envelope([
        claim("F1", [
            chk("path_absent", ABSENT, True, "the gap is unowned"),
        ]),
        claim("S1", [
            chk("path_absent", MINERAL, True, "the register slot is unbuilt"),
        ]),
    ]),
    "mixed-stale-cne.json": envelope([
        claim("S1", [
            chk("path_absent", MINERAL, True, "the register slot is unbuilt"),
        ]),
        claim("N1", []),
    ]),
    # --- could-not-evaluate ----------------------------------------------
    "cne-empty.json": envelope([
        claim("N1", []),
    ]),
    "cne-missing.json": envelope([
        {"id": "N2", "axis": "operability",
         "claim": "no checks field", "before": "nothing declared"},
    ]),
    # --- malformed --------------------------------------------------------
    "malformed-no-baseline.json": {
        "round": 47, "claims": [claim("M1", [chk("path_absent", ABSENT, True)])]
    },
    "malformed-no-claims.json": {"round": 47, "baseline_commit": BASELINE},
    "malformed-missing-id.json": envelope([
        {"axis": "operability", "before": "x",
         "before_checks": [chk("path_absent", ABSENT, True)]},
    ]),
    "malformed-missing-before.json": envelope([
        {"id": "M2", "axis": "operability",
         "before_checks": [chk("path_absent", ABSENT, True)]},
    ]),
    "malformed-unknown-probe.json": envelope([
        claim("M3", [chk("vibes_absent", ABSENT, True)]),
    ]),
    "malformed-bad-baseline.json": envelope([
        claim("M4", [chk("path_absent", ABSENT, True)]),
    ], baseline="deadbeef"),
}

# (fixture, expectation). expectation is {"exit": N} or {"nonzero": True}.
CASES = [
    ("fresh-all", "fresh-all.json", {"exit": 0}),
    ("stale-one", "stale-one.json", {"exit": 1}),
    ("stale-topic", "stale-topic.json", {"exit": 1}),
    ("mixed", "mixed.json", {"exit": 1}),
    ("mixed-stale-cne", "mixed-stale-cne.json", {"nonzero": True}),
    ("cne-empty", "cne-empty.json", {"nonzero": True}),
    ("cne-missing", "cne-missing.json", {"nonzero": True}),
    ("malformed-no-baseline", "malformed-no-baseline.json", {"exit": 2}),
    ("malformed-no-claims", "malformed-no-claims.json", {"exit": 2}),
    ("malformed-missing-id", "malformed-missing-id.json", {"exit": 2}),
    ("malformed-missing-before", "malformed-missing-before.json", {"exit": 2}),
    ("malformed-unknown-probe", "malformed-unknown-probe.json", {"exit": 2}),
    ("malformed-bad-baseline", "malformed-bad-baseline.json", {"nonzero": True}),
]

NONJSON = "malformed-nonjson.json"


def write_fixtures(dirpath):
    os.makedirs(dirpath, exist_ok=True)
    paths = {}
    for name, payload in FIXTURES.items():
        path = os.path.join(dirpath, name)
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=1)
        paths[name] = path
    path = os.path.join(dirpath, NONJSON)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("not json\n")
    paths[NONJSON] = path
    return paths


def invoke(tool, claims_path, root):
    cmd = [sys.executable, "-B", tool, "--claims", claims_path, "--root", root]
    try:
        proc = subprocess.run(
            cmd, cwd=root, capture_output=True, text=True, timeout=120,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, "", "invoke failed: %s" % exc
    return proc.returncode, proc.stdout, proc.stderr


def tail(text, n=3):
    lines = [ln for ln in text.strip().splitlines() if ln.strip()]
    return " | ".join(lines[-n:])[:400]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tool", default="tools/harness/claims-freshness.py")
    parser.add_argument("--root", default=os.getcwd())
    parser.add_argument("--fixtures", default=".scratch/o10/fixtures")
    parser.add_argument("--r43-demo", default=None,
                        help="optional annotated r43 claims.json (must exit 1)")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.root)
    tool = args.tool if os.path.isabs(args.tool) else os.path.join(root, args.tool)
    if not os.path.isfile(tool):
        print("COULD-NOT-EVALUATE: tool absent at %s" % tool)
        print("suite exit 2 (not green)")
        return 2

    paths = write_fixtures(os.path.join(root, args.fixtures))
    rows = []
    failures = 0
    zero_exits = []

    for name, fixture, expectation in CASES:
        rc, out, err = invoke(tool, paths[fixture], root)
        if rc is None:
            rows.append((name, str(expectation), "INVOKE-FAIL", "FAIL"))
            failures += 1
            continue
        if rc == 0:
            zero_exits.append(name)
        if "exit" in expectation:
            ok = rc == expectation["exit"]
            want = str(expectation["exit"])
        else:
            ok = rc != 0
            want = "nonzero"
        rows.append((name, want, str(rc), "PASS" if ok else "FAIL"))
        if not ok:
            failures += 1
            print("FAIL %-26s want=%-7s got=%-3s stdout=%s stderr=%s"
                  % (name, want, rc, tail(out), tail(err)))
        elif args.verbose:
            print("PASS %-26s want=%-7s got=%d" % (name, want, rc))

    # non-JSON fixture
    rc, out, err = invoke(tool, paths[NONJSON], root)
    if rc is None:
        rows.append(("malformed-nonjson", "2", "INVOKE-FAIL", "FAIL"))
        failures += 1
    else:
        ok = rc == 2
        rows.append(("malformed-nonjson", "2", str(rc), "PASS" if ok else "FAIL"))
        if rc == 0:
            zero_exits.append("malformed-nonjson")
        if not ok:
            failures += 1
            print("FAIL %-26s want=2 got=%d stdout=%s stderr=%s"
                  % ("malformed-nonjson", rc, tail(out), tail(err)))

    # global invariant: exit 0 only for the all-fresh fixture
    illegal = [name for name in zero_exits if name != "fresh-all"]
    if illegal:
        failures += 1
        print("FAIL exit-0 invariant: zero exits observed in %s" % ", ".join(illegal))

    # optional r43 positive regression: annotated claims must exit 1
    if args.r43_demo:
        demo = args.r43_demo if os.path.isabs(args.r43_demo) else os.path.join(root, args.r43_demo)
        if os.path.isfile(demo):
            rc, out, err = invoke(tool, demo, root)
            ok = rc == 1
            rows.append(("r43-demo", "1", str(rc), "PASS" if ok else "FAIL"))
            if not ok:
                failures += 1
                print("FAIL r43-demo want=1 got=%s stdout=%s stderr=%s"
                      % (rc, tail(out), tail(err)))
            else:
                for cid, want in (("O", "STALE"), ("C", "STALE"), ("Ca", "FRESH")):
                    seen = re.search(r"\[%s\].*%s" % (cid, want), out)
                    print("  r43 %s: %s (advisory)" % (cid, "seen" if seen else "not matched"))
        else:
            rows.append(("r43-demo", "1", "ABSENT", "C-N-E"))
            print("COULD-NOT-EVALUATE: r43 demo absent at %s" % demo)

    # advisory (hard if it fires): a flag that turns C-N-E green breaks "never 0"
    try:
        help_proc = subprocess.run(
            [sys.executable, "-B", tool, "--help"], cwd=root,
            capture_output=True, text=True, timeout=40,
        )
        help_text = help_proc.stdout + help_proc.stderr
    except (OSError, subprocess.TimeoutExpired):
        help_text = ""
    if "--allow-unverifiable" in help_text:
        cmd = [sys.executable, "-B", tool, "--claims", paths["cne-empty.json"],
               "--root", root, "--allow-unverifiable"]
        try:
            proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True,
                                  timeout=120)
            rc = proc.returncode
        except (OSError, subprocess.TimeoutExpired):
            rc = None
        ok = rc not in (0, None)
        rows.append(("cne-allow-flag", "nonzero", str(rc), "PASS" if ok else "FAIL"))
        if not ok:
            failures += 1
            zero_exits.append("cne-allow-flag")
            print("FAIL cne-allow-flag: --allow-unverifiable turned C-N-E green (exit %s)" % rc)

    print("\ncase                       want    got     verdict")
    for row in rows:
        print("%-26s %-7s %-7s %s" % row)
    print("\n%d case(s), %d failure(s)" % (len(rows), failures))
    if failures:
        print("EXIT-CONFORMANCE: FAIL")
        return 1
    print("EXIT-CONFORMANCE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Appendix B — compliant reference double (calibration only, not a deliverable)

This file exists only to prove the suite can go green; it must never be landed as the gate. `sha256 a6b099b7947127276b682a4078d00b918554994a44f81cdbe5b7565e2b1b9828`.

```python
#!/usr/bin/env python3
"""Reference test double for the O10 exit-code suite. NOT a deliverable.

Implements only the probe kinds the fixtures use, with the r47 exit contract:
0 fresh, 1 stale, 2 malformed, 3 could-not-evaluate.
"""
import json
import subprocess
import sys


class Malformed(Exception):
    pass


def git(root, *args):
    return subprocess.run(["git", "-C", root] + list(args),
                          capture_output=True, text=True)


def exists(root, commit, path):
    return git(root, "cat-file", "-e", "%s:%s" % (commit, path)).returncode == 0


def read(root, commit, path):
    proc = git(root, "show", "%s:%s" % (commit, path))
    if proc.returncode != 0:
        raise Malformed("cannot read %s at %s" % (path, commit))
    return proc.stdout


def corpus_files(root, commit):
    proc = git(root, "ls-tree", "-r", "--name-only", commit, "--", "corpus/knowledge")
    if proc.returncode != 0:
        raise Malformed("cannot list corpus at %s" % commit)
    return [p for p in proc.stdout.splitlines() if p.endswith(".md")]


def topic_owned(root, commit, needle):
    needle = needle.lower()
    for path in corpus_files(root, commit):
        for line in read(root, commit, path).splitlines():
            if line.startswith("- topic:") and needle in line.lower():
                return True
    return False


PROBES = {
    "path_absent": lambda root, c, t: not exists(root, c, t),
    "path_present": lambda root, c, t: exists(root, c, t),
    "topic_owner_absent": lambda root, c, t: not topic_owned(root, c, t),
}


def main(argv):
    if "--selftest" in argv:
        print("reference stub: no selftest (test double only)")
        return 0
    try:
        claims_path = argv[argv.index("--claims") + 1]
        root = argv[argv.index("--root") + 1] if "--root" in argv else "."
    except (ValueError, IndexError):
        print("claims-freshness: missing --claims", file=sys.stderr)
        return 2
    try:
        with open(claims_path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as exc:
        print("claims-freshness: %s" % exc, file=sys.stderr)
        return 2
    try:
        commit = data.get("baseline_commit")
        if not isinstance(commit, str) or not commit:
            raise Malformed("no baseline_commit")
        if git(root, "rev-parse", "--verify", commit + "^{commit}").returncode != 0:
            raise Malformed("baseline_commit does not resolve: %s" % commit)
        claims = data.get("claims")
        if not isinstance(claims, list):
            raise Malformed("no claims list")
        verdicts = []
        for row in claims:
            if not isinstance(row, dict) or not row.get("id") or not row.get("before"):
                raise Malformed("claim missing id/before")
            checks = row.get("before_checks")
            if checks is None or checks == []:
                verdicts.append((row["id"], "unverifiable"))
                continue
            if not isinstance(checks, list):
                raise Malformed("before_checks not a list")
            stale = False
            for check in checks:
                kind = check.get("probe_kind")
                if kind not in PROBES:
                    raise Malformed("unknown probe_kind %r" % kind)
                expect = check.get("expect")
                if not isinstance(expect, bool):
                    raise Malformed("expect not boolean")
                measured = PROBES[kind](root, commit, check.get("target", ""))
                if measured != expect:
                    stale = True
            verdicts.append((row["id"], "stale" if stale else "fresh"))
    except Malformed as exc:
        print("claims-freshness: %s" % exc, file=sys.stderr)
        return 2
    for cid, verdict in verdicts:
        print("[%s] fixture -- %s" % (cid, verdict.upper()))
    if any(v == "stale" for _, v in verdicts):
        print("REFUSE: stale claims")
        return 1
    if any(v == "unverifiable" for _, v in verdicts):
        print("REFUSE: unverifiable claims")
        return 3
    print("OK: all fresh")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```
