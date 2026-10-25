# MutO5 — mutation test of the negative assertion in `tools/check-settlement-fixture.py`

Round 69 · v1 wave · seat MutO5 · judged axis: operability. Date 2026-10-24.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base 793f79746712a79f915bb481215e54bbea8b5e7a).
All mutations were applied to copies under `/tmp/mutO5/`; no production byte was
written, no git/jj state touched, no network, no tool installs.

## Question under test

Does the harness fail when the defect class it claims to catch
(missing used-by path — the round-68 fixture defect R68-M1) is **not** caught?

## Baseline — unmodified harness

Command:

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-settlement-fixture.py --selftest; echo "EXIT=$?"
```

Real output:

```
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3
EXIT=0
```

The negative assertion under test is `tools/check-settlement-fixture.py:128`:

```python
ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 1
```

## Mutations applied (copies in /tmp only)

Setup command (both mutations single-line, verified by `diff -u`):

```
mkdir -p /tmp/mutO5
cp .../tools/check-settlement-fixture.py /tmp/mutO5/harness-mutA.py
cp .../tools/check-supersession-settlement.py /tmp/mutO5/checker-mutB.py
python3 - <<'EOF'   # targeted single-occurrence replacements, count==1 asserted
...
EOF
```

- **MUT-A (assert-flip, the instructed mutation)** — in the harness copy
  `/tmp/mutO5/harness-mutA.py`, line 128 expectation flipped to the
  not-caught value:

  ```diff
  -        ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 1
  +        ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 0
  ```

- **MUT-B (detection-kill, stronger form)** — in a copy of the underlying
  checker `/tmp/mutO5/checker-mutB.py`, the missing-used-by detection is
  killed, then fed to the **unmodified** harness through its own `--checker`
  hook:

  ```diff
  -    missing_paths = [p for _, p in stale if not os.path.exists(os.path.join(root, p))]
  +    missing_paths = []  # MUTATION B: missing-used-by detection killed
  ```

Digests (provenance):

```
f7adb4ba52e0db1a1c20ee33a5b52a0e2288b287866493ed43d800967712f7f8  tools/check-settlement-fixture.py       (orig)
05214b3d7618b47c7ff9c8d9127647b7b7832c0ed748b3271b0266c7f343ad74  tools/check-supersession-settlement.py  (orig)
01dab1a93e8a800b046b0b06d90497beabcfa614455746eb1cf342961cc21ae4  /tmp/mutO5/harness-mutA.py              (mutA)
f44e3c42ccae163d81d032aa19ba2abd160e1f476cd7ff63e464aeb33c716e3f  /tmp/mutO5/checker-mutB.py              (mutB)
```

## Run 1 — mutated harness vs real checker (MUT-A)

Command:

```
python3 -B /tmp/mutO5/harness-mutA.py --checker /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-supersession-settlement.py; echo "EXIT_MUTA=$?"
```

Real output:

```
PASS fixture-green rc=0 pending=0 missing_paths=0
FAIL fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/3
EXIT_MUTA=1
```

`FAIL fixture-negative`, exit 1. Note the detail line still shows the checker
*did* catch the defect (`missing_paths=1`); the mutated harness failed because
its expectation was flipped to the not-caught value. (The copy needs
`--checker` because the harness derives its default checker path from its own
location — a `/tmp` copy without the override exits 2 `CHECKER_MISSING`.)

## Run 2 — unmodified harness vs mutated checker (MUT-B: class not caught)

Command:

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-settlement-fixture.py --checker /tmp/mutO5/checker-mutB.py; echo "EXIT_MUTB=$?"
```

Real output:

```
PASS fixture-green rc=0 pending=0 missing_paths=0
FAIL fixture-negative rc=0 pending=0 missing_paths=0
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/3
EXIT_MUTB=1
```

The negative fixture *has* the R68-M1 defect (used-by file absent); the mutated
checker does not catch it (`missing_paths=0`), and the unmodified harness goes
red: `FAIL fixture-negative`, `FIXTURE: 2/3`, exit 1.

## Findings

- VERDICT: PASS — the harness fails when the defect class it claims to catch is not caught. Directly demonstrated by MUT-B: detection killed → checker reports `missing_paths=0` on the defect-carrying fixture → unmodified harness prints `FAIL fixture-negative` and exits 1.
- VERDICT: PASS — the negative assertion is live and discriminating. The instructed MUT-A (expectation flipped to the not-caught value `missing_paths=0`) also yields `FAIL fixture-negative` and exit 1, while the checker's own output (`missing_paths=1` in the FAIL detail) confirms the defect was present and caught — the failure is attributable to the assertion, not to the checker.
- VERDICT: PASS — mutation localization. Under both mutations `fixture-green` and `fixture-pending` still PASS; only the negative case flips, so the red signal is attributable to the negative-case gate alone (no collateral breakage muddying the signal).
- VERDICT: PASS — baseline sanity. Unmodified harness: `FIXTURE: 3/3`, exit 0 (output above).
- Observation (non-blocking): the negative case does not gate on the checker's exit code (`rc` is captured and echoed but excluded from `ok` at line 128); the current checker returns 0 on missing-paths-only scans, so this is consistent today, but a future checker that exits non-zero on `missing_paths>0` would not be caught by this assertion as written. Recorded as an observation for the L1, not a defect in O2's predicate.
- Scope note: MUT-A/MUT-B lived entirely under `/tmp/mutO5/`; production tools, claims, and acceptance scripts were only read.

VERDICT: PASS
