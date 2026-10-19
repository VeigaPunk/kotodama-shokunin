# O13 — probe-coverage verification: every probe kind exercised, none dead, unknown kinds rejected

- Seat: `O13` | role verifier | claim **O** | round 47, loop 2
- Out path: `reports/round-47/op/O13-probe-coverage.md` (the only repo write by this seat)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`, measured 2026-10-19)
- Verification cut: **2026-10-19T17:58Z**; all commands run from the lane root with
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
- Mission (`reports/round-47/targets.json`, seat O13): *every probe kind in the registry is
  exercised by at least one selftest control; no dead probe kinds; the schema rejects unknown
  probe kinds.*
- Boundary: I read filed bytes and the scratch prototype, ran the prototype read-only (its
  selftest and synthetic claims), and wrote `.scratch/o13/**` plus this file. I did not edit a
  filed byte, did not stage under `corpus/`, did not run any `reports/round-*/run-validation.py`,
  and made no git/network/install calls. `git status --porcelain` at the cut shows only the
  pre-existing `?? reports/round-46/review/` and `?? reports/round-47/`.

## 1. Verdict at this cut

| target | status | basis |
|---|---|---|
| Durable `tools/harness/claims-freshness.py` | **could-not-evaluate** | path absent at the cut (`ls: cannot access ...: No such file or directory`); no O-seat out file was filed in `reports/round-47/op/` yet |
| Build candidate `.scratch/ca01/claims-freshness.py` (sha256 `dd88d9e1…`) | **FAIL** on all three criteria | 6 of 13 implemented kinds have no selftest control; 2 contract kinds are not implemented under their contract names; no probe registry exists to check coverage against; unknown kinds are downgraded to STALE, not rejected as malformed |
| Round plan `P01-plan.md` §5.6 control matrix | **FAIL (coverage hole in the plan itself)** | `grep_present` has **zero** controls although it is load-bearing in P01's own r43 demo (`P01-plan.md:281`); `path_present` has only the positive control |

The method is sound and the r43 regression reproduces; the *coverage* of the probe vocabulary
is not. This is a fail at this cut, not a judgment that the approach is wrong.

## 2. What was measured

### 2.1 Prototype identity and selftest

```
$ sha256sum .scratch/ca01/claims-freshness.py
dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434
$ python3 -B .scratch/ca01/claims-freshness.py --selftest ; echo EXIT=$?
...
FAIL  grep_absent hit fails
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL
EXIT=1
```

Two distinct defects:

1. `grep_absent hit fails` uses `glob: corpus/knowledge/beta/*.md`, but the fixture creates only
   `alpha/` and `myth-symbol/` (`.scratch/ca01/claims-freshness.py:733-745`). An empty glob has
   zero hits, so the probe passes and `not passed` fails. A "hit" control that cannot hit is
   not a control; the adjacent partition-scan control does hit.
2. `seventeen checks collected (18)` is a hard-coded count that went stale when an eighteenth
   control was added (`.scratch/ca01/claims-freshness.py:879`). This is exactly what P01 §5.6
   forbids ("the count is computed from the control registry, not a hard-coded literal",
   `reports/round-47/plan/P01-plan.md:309`).

### 2.2 Probe vocabulary implemented vs exercised

The evaluator is an if-chain over 13 kinds (`.scratch/ca01/claims-freshness.py:293-359`), and
selftest probes are passed directly to `evaluate_probe()` (`:747-825`). Static extraction of
both sets:

```
$ python3 -B .scratch/o13/probe-coverage.py .scratch/ca01/claims-freshness.py
probe coverage: .scratch/ca01/claims-freshness.py
  implemented (13): count_eq, count_ge, count_le, glob_absent, glob_present, grep_absent,
                    grep_present, path_absent, path_present, sha256_eq, tool_family_absent,
                    topic_owned, topic_unowned
  exercised   (7): count_eq, glob_absent, grep_absent, path_absent, sha256_eq,
                    tool_family_absent, topic_unowned
  dead kinds  (6): count_ge, count_le, glob_present, grep_present, path_present, topic_owned
  contract missing (2): capability_present, topic_owner_absent
  extra beyond contract: count_ge, count_le, glob_absent, glob_present, tool_family_absent,
                    topic_owned, topic_unowned
  registry: NONE declared (coverage not mechanically enforceable)
  FAIL no_dead_kinds
  FAIL contract_complete
  FAIL registry_declared_and_complete
VERDICT: FAIL
```

"Dead" here means **untested, not broken**. I exercised all six in one synthetic declared-probe
claims file at `6e9a30d`; each returned the correct verdict:

```
[P1] path_present  tools/harness/basename-couples-resolver.py  -> FRESH (1/1)
[P2] glob_present  corpus/knowledge/*/*.md                     -> FRESH (1/1)
[P3] count_le      1000                                        -> FRESH (1/1)
[P4] count_ge      1                                           -> FRESH (1/1)
[P5] grep_present  ^- topic:                                   -> FRESH (1/1)
[P6] topic_owned   myth-symbol/lithic                          -> FRESH (1/1)
exit 0
```

So a regression in any one of these six would ship undetected; none is protected by the
selftest. That is the coverage defect, not a runtime defect.

### 2.3 Contract-name mapping

The r47 contract names a closed set. `reports/round-47/plan/P01-plan.md:247-258` (implementing
`reports/round-44/review/R01-review.md:245`) declares eight:
`path_absent, path_present, grep_absent, grep_present, count_eq, sha256_eq, topic_owner_absent,
capability_present`.

| contract kind | prototype implementation | status |
|---|---|---|
| `path_absent` | yes | exercised (2 controls) |
| `path_present` | yes | **dead** |
| `grep_absent` | yes | exercised (3 controls, one broken) |
| `grep_present` | yes | **dead** |
| `count_eq` | yes | exercised (2 controls) |
| `sha256_eq` | yes | exercised (1 control) |
| `topic_owner_absent` | implemented as `topic_unowned` | exercised, **name differs from contract** |
| `capability_present` | no direct probe; `tool_family_absent` is the inverse heuristic | **missing** |

`topic_unowned` is semantically the probe P01 calls `topic_owner_absent` (it fails when an owner
is found, `.scratch/ca01/claims-freshness.py:333-345`), so this is a naming/schema divergence
rather than a missing capability. `capability_present` is a real gap: P01 §5.2 requires a
capability registry ("the registry is data in the tool, not prose inference",
`reports/round-47/plan/P01-plan.md:260`), and the prototype has no registry at all.

Contract note: `reports/round-47/claims.json:39` lists seven kinds and omits `grep_present`,
while P01 §5.2 (following R01 §4.3) lists eight and P01's demo uses `grep_present` for the
wrapped-field clause (`P01-plan.md:281`). I treat the **eight-kind P01 set as authoritative**;
the tool must implement `grep_present` and control it. If the integrator decides the seven-kind
reading governs instead, `grep_present` must be removed from the registry *and* from P01's demo,
not left implemented-but-dead.

### 2.4 Unknown probe kinds are not rejected as malformed

P01 §5.2: "Unknown `probe_kind`, missing `expect`, or a check with no clause span is malformed"
(`reports/round-47/plan/P01-plan.md:243`); §5.6 control 14 requires exit 2 for unknown probe kind.
Corroborated independently by O10's `O10-F4` (`reports/round-47/op/O10-exit-codes.md:139`): a
typo'd `probe_kind` must be a schema rejection, not `UNVERIFIABLE`/`STALE`.
Measured behavior of the prototype:

```
$ cat .scratch/o13/unknown-kind.json   # one claim, freshness_probes[0].kind = "no_such_probe_kind"
$ python3 -B .scratch/ca01/claims-freshness.py --claims .scratch/o13/unknown-kind.json
[X] operability -- STALE (0/1 premises hold)
  x declared: "freshness_probes[0]"
      probe {"kind": "no_such_probe_kind", ...} -> probe error: unknown probe kind: 'no_such_probe_kind'
summary: 0 fresh, 1 stale, ...
REFUSE: ...
exit 2
EXIT=2
```

The exit code happens to equal 2, but the semantics are wrong on three counts:

- the verdict is **STALE**, not `MALFORMED`;
- the file is not rejected: other claims in the same file are still evaluated and can be `FRESH`;
- the cause is a blanket `except (KeyError, ValueError)` in `analyze_claim`
  (`.scratch/ca01/claims-freshness.py:574`) turning *schema errors* into *failed premises*.

The same catch converts a malformed probe into staleness:

- `{"kind": "path_absent"}` with no `path` → `STALE ... probe error: 'path'`, exit 2;
- unknown kind inside a mixed file → the unknown-kind claim STALE, the other claim FRESH, exit 2.

An explicitly empty `freshness_probes: []` is falsy and silently falls through to legacy prose
mining (`:555-568`), yielding `UNVERIFIABLE` exit 3. That is non-green (acceptable under the
contract's "could-not-evaluate != green") but it is not a schema decision: an explicitly
declared empty check list should be `MALFORMED` or `COULD-NOT-EVALUATE`, never a different mode.

### 2.5 The r43 regression still works

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json >/dev/null
[O]  operability  -- STALE (0/2 premises hold)
[C]  coverage     -- STALE (2/3 premises hold)
[Ca] calibration  -- FRESH (1/1 premises hold)
exit 2
```

This is the required positive regression (O and C stale, Ca fresh). The prototype's stale exit
code is 2 and unverifiable is 3 (`.scratch/ca01/claims-freshness.py:706-710`), which conflicts
with P01's exit contract (stale = 1, malformed = 2, could-not-evaluate = 3,
`reports/round-47/plan/P01-plan.md:265-270`). That is O10/O15 territory, but it means "exit 2"
alone cannot be used as evidence of malformed until the durable tool fixes the mapping. My
acceptance below checks the verdict **word** as well as the code.

## 3. Coverage gaps in the round's own control matrix

P01 §5.6 (`reports/round-47/plan/P01-plan.md:307-330`) enumerates 18 controls. Mapped against
the eight-kind registry:

| kind | controls in P01 §5.6 | gap |
|---|---|---|
| `path_absent` | #1 absent→FRESH, #2 present→STALE | none |
| `path_present` | #3 present→FRESH | **no absent→STALE control** |
| `grep_absent` | #4 no-hit→FRESH, #5 hit→STALE | none |
| `grep_present` | **none** | **zero controls; yet P01 §5.3's O demo depends on four `grep_present` checks (`:281`)** |
| `count_eq` | #6 equal→FRESH, #7 unequal→STALE | none |
| `sha256_eq` | #8 match/mismatch | none |
| `topic_owner_absent` | #9 no-owner/owner | none |
| `capability_present` | #10 absent-with-false/present-with-false | none |

A tool built exactly to P01 §5.6 would therefore still carry one dead kind (`grep_present`) and
one one-sided kind (`path_present`). The matrix needs three additions before the tool can pass
this seat:

1. `grep_present`: no-hit→FRESH and hit→STALE (or hit→FRESH and no-hit→STALE, depending on the
   declared `expect`; both outcomes must be exercised, as with `grep_absent`).
2. `path_present`: absent→STALE.
3. A **registry-completeness control**: the selftest computes the set of registry kinds and
   asserts every kind appears in at least one control, and that no control names a kind outside
   the registry. This is stronger than a hand-maintained count and prevents both dead kinds and
   the `seventeen checks` class of stale assertion.

Also strengthen malformed control #14: assert the output says `MALFORMED` (not `STALE`) and that
a malformed claim prevents a `FRESH` verdict for the file, not merely that the process exits 2.

## 4. Durable-tool acceptance — what O13 will run after the integrator applies

Commands (from lane root, same env):

```
python3 tools/harness/claims-freshness.py --selftest
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json
python3 <extracted-checker> tools/harness/claims-freshness.py --json
python3 tools/harness/claims-freshness.py --claims <unknown-kind-sidecar-or-claims>
python3 tools/harness/claims-freshness.py --claims <missing-expect-sidecar-or-claims>
```

Pass conditions:

1. `--selftest` prints `selftest N/N PASS`, exit 0, with N computed from the control registry.
2. Checker reports: implemented set == the eight P01 contract kinds (or a documented superset
   with every extra kind also exercised); `dead_kinds == []`; a declared registry
   (`PROBE_KINDS` / `PROBE_REGISTRY` / equivalent data table) whose members equal the dispatched
   set exactly.
3. `grep_present` and `path_present` each have both outcomes exercised (closes §3).
4. Unknown `probe_kind` → output contains `MALFORMED`, exit 2, and no claim in the file is
   reported `FRESH`; same for missing `expect` and missing clause span.
5. No registry member is reachable only through legacy mining; if legacy mining is kept, its
   probe kinds are covered by direct controls too.
6. The r43 demo still reports O STALE, C STALE, Ca FRESH with exit 1 (P01 §5.2 mapping).

Status of all six on the durable path at this cut: **could-not-evaluate** (tool absent).

## 5. Reusable checker

Extract the block below to `.scratch/o13/probe-coverage.py` (or anywhere outside `tools/`) and
run it against the assembled tool. It is static, stdlib-only, and never imports the target.
It is functionally identical to the copy used for the measurements above (only docstrings and an
unused debug counter differ; the verdict is the same).

````python
#!/usr/bin/env python3
"""O13 probe-coverage verifier (r47).

Static checks for a claims-freshness gate:
  1. every implemented probe kind is exercised by >=1 selftest control;
  2. every kind in the contract's closed set (P01 s5.2, eight kinds) is implemented;
  3. a module-level probe registry is declared and equals the dispatched set.

Dynamic unknown-kind rejection is a separate invocation (the tool, not this checker):
  python3 TOOL --claims <unknown-kind.json>; echo $?
expect MALFORMED and the P01 exit code for malformed (2), distinct from stale (1).

Usage: probe-coverage.py TOOL.py [--json]
Exit 0 when all three checks pass, 1 otherwise.
"""
import json
import re
import sys

CONTRACT_KINDS = [
    "path_absent",
    "path_present",
    "grep_absent",
    "grep_present",
    "count_eq",
    "sha256_eq",
    "topic_owner_absent",
    "capability_present",
]


def top_level_functions(src):
    starts = [(m.group(1), m.start()) for m in re.finditer(r"^def (\w+)\(", src, re.M)]
    out = {}
    for i, (name, start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else len(src)
        out[name] = src[start:end]
    return out


def string_kinds(text):
    kinds = set()
    for match in re.finditer(
        r"\"(?:kind|probe_kind)\"\s*:\s*\"([a-z0-9_]+)\"", text
    ):
        kinds.add(match.group(1))
    return kinds


def comparison_kinds(text):
    kinds = set()
    for match in re.finditer(r"kind\s*==\s*\"([a-z0-9_]+)\"", text):
        kinds.add(match.group(1))
    for match in re.finditer(r"kind\s+in\s+\(([^)]*)\)", text):
        kinds.update(re.findall(r"\"([a-z0-9_]+)\"", match.group(1)))
    return kinds


def registry_kinds(src):
    for match in re.finditer(
        r"^([A-Z][A-Z0-9_]*PROBE[A-Z0-9_]*|PROBES|PROBE_KINDS|HANDLERS|KINDS)\s*=\s*([\[{])",
        src,
        re.M,
    ):
        start = match.start()
        depth = 0
        for i in range(match.start(2), len(src)):
            ch = src[i]
            if ch in "[{":
                depth += 1
            elif ch in "]}":
                depth -= 1
                if depth == 0:
                    body = src[start:i + 1]
                    return match.group(1), set(re.findall(r"\"([a-z0-9_]+)\"", body))
    return None, set()


def main(argv):
    path = argv[1]
    as_json = "--json" in argv
    src = open(path, "r", encoding="utf-8").read()
    functions = top_level_functions(src)

    evaluator = functions.get("evaluate_probe") or functions.get("probe") or ""
    selftest = functions.get("run_selftest") or functions.get("selftest") or ""
    if not evaluator or not selftest:
        print("could-not-evaluate: need evaluate_probe() and run_selftest()")
        return 1

    implemented = comparison_kinds(evaluator) | string_kinds(evaluator)
    exercised = string_kinds(selftest) | comparison_kinds(selftest)
    reg_name, registered = registry_kinds(src)

    dead = sorted(implemented - exercised)
    uncovered_contract = sorted(set(CONTRACT_KINDS) - implemented)
    extra = sorted(implemented - set(CONTRACT_KINDS))
    registry_missing = sorted(implemented - registered) if registered else sorted(implemented)
    registry_extra = sorted(registered - implemented) if registered else []

    report = {
        "tool": path,
        "implemented": sorted(implemented),
        "exercised": sorted(exercised),
        "dead_kinds": dead,
        "contract_missing": uncovered_contract,
        "contract_extra": extra,
        "registry": {
            "name": reg_name,
            "declared": sorted(registered),
            "missing_from_registry": registry_missing,
            "in_registry_not_dispatched": registry_extra,
        },
        "checks": {
            "no_dead_kinds": not dead,
            "contract_complete": not uncovered_contract,
            "registry_declared_and_complete": bool(registered)
            and not registry_missing
            and not registry_extra,
        },
    }
    report["pass"] = all(report["checks"].values())

    if as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print("probe coverage: %s" % path)
        print("  implemented (%d): %s" % (len(implemented), ", ".join(sorted(implemented))))
        print("  exercised   (%d): %s" % (len(exercised), ", ".join(sorted(exercised))))
        print("  dead kinds  (%d): %s" % (len(dead), ", ".join(dead) or "-"))
        print("  contract missing (%d): %s" % (len(uncovered_contract), ", ".join(uncovered_contract) or "-"))
        print("  extra beyond contract: %s" % (", ".join(extra) or "-"))
        if registered:
            print("  registry %s (%d): %s" % (reg_name, len(registered), ", ".join(sorted(registered))))
            if registry_missing:
                print("  registry missing: %s" % ", ".join(registry_missing))
            if registry_extra:
                print("  registry not dispatched: %s" % ", ".join(registry_extra))
        else:
            print("  registry: NONE declared (coverage not mechanically enforceable)")
        for name, ok in report["checks"].items():
            print("  %s %s" % ("ok  " if ok else "FAIL", name))
        print("VERDICT: %s" % ("PASS" if report["pass"] else "FAIL"))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 6. Findings ledger for the integrator

| # | finding | severity | disposition |
|---|---|---|---|
| O13-1 | 6 of 13 prototype kinds have no selftest control | blocking for O13 | add controls per §3 |
| O13-2 | `grep_present` has zero controls in P01 §5.6 though used in the r43 demo | blocking | add two controls |
| O13-3 | `path_present` has only a positive control | should-fix | add absent→STALE |
| O13-4 | no probe registry constant; dispatch is an if-chain; coverage not enforceable | blocking for criterion 3 | declare registry as data |
| O13-5 | unknown/paramless probe kinds become STALE, not MALFORMED; mixed file still evaluates | blocking | validate schema at load; reject file with exit 2 and `MALFORMED` |
| O13-6 | `capability_present` not implemented; `topic_owner_absent` is named `topic_unowned` | blocking (contract) | implement P01 names |
| O13-7 | selftest red 17/19 (bad beta fixture; hard-coded count) | blocking (O08/O14) | fixture to `myth-symbol`; compute count |
| O13-8 | stale exit is 2, malformed 2, unverifiable 3 | O10/O15 | align with P01: 0/1/2/3 |

## 7. Open items / to-verify

- The durable tool and O01-O04 drafts were not filed at this cut; §4 must be re-run by V02 (or
  by the integrator) after apply. Until then this seat reports **could-not-evaluate** on the
  durable path, not a pass.
- `to-verify`: whether O04's selftest adopts the P01 matrix verbatim or adds controls; if the
  assembled tool diverges from P01's schema, §4's conditions should be re-read against the
  assembled contract, and a divergence from P01 named rather than silently accepted.
- `to-verify`: the seven-vs-eight kind ambiguity (§2.3). I recommend eight; the decision belongs
  to the O12/integrator, not this seat.
