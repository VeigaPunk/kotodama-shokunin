# R14-D05 — missing receipt keeps the first-run write path green

- Axis: O / operability, supporting D / depth (non-overblocking receipt guard).
- Prepared: 2026-10-17 local (UTC-03:00). Runtime stamps below are UTC.
- Assignment: without `REFRESH_RECEIPTS`, a runner with a **missing** receipt
  writes normally. This means a first-run pathname absent from both `HEAD`
  and the worktree, not a deleted working copy of a committed receipt.
- Status: **PASS for the miniature wired runner**; not a round-14 admission or
  a certification of the separately owned production-runner integration.
- Writes: this fragment, `guard/neg-04.md`, and this seat's ignored
  `.scratch/r14-d04-d05/**` fixtures only. No live historical writer was run.

## Executed control

At `2026-10-18T00:01:24.656922Z`, with `REFRESH_RECEIPTS` **removed from the
child environment**, the exact same guarded runner used by D04 targeted a
missing, uncommitted receipt in the disposable clone:

```text
cwd: .scratch/r14-d04-d05/fixture
command: /usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/r14-d04-d05/receipt-writer.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/r14-d04-d05/fixture reports/round-14/validation.json R14-D05-measurement-sentinel
exit: 0
stdout: runner: receipt written
stderr: empty
```

The stdout quote is the child `stdout` recorded at
`.scratch/r14-d04-d05/negative-results.json`, `tests[1].stdout` (same timestamp).
Independent `git -C .scratch/r14-d04-d05/fixture ls-tree -z --full-tree a7bc9e9ff05a57515c5efaaa7e50116eb30938ff -- reports/round-14/validation.json`
returned exit 0 and **empty** output. `Path.is_file()` was false before the
runner. The callback then created `R14-D05-measurement-sentinel` and wrote
these exact receipt bytes, including the final LF:

```json
{"control": "R14-D04-D05", "written": true}
```

Before/after SHA-256 from `hashlib.sha256` over `Path.read_bytes()`, same run:

```text
before absent
after  586e41680cf13f5184efba094076f4912f131c54db404fd2660b770564bc0e13
```

**7/7 assertions passed**: exit 0, absent from the commit, absent on disk before
execution, receipt created, exact payload, measurement sentinel present, and
writer-completion output present. Counting command:
`export TMPDIR=$PWD/.scratch; PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-negatives.py`, run `2026-10-18T00:01:24Z`, exit **0**;
combined with D04, **14/14 assertions passed**. Raw results remain at
`.scratch/r14-d04-d05/negative-results.json`.

## Reproduce and interpret

`guard/neg-04.md` includes the exact runner source and provenance. Restore it
there if ignored scratch has been cleaned, then run from the lane root with a
**new** fixture destination:

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
FIXTURE=$TMPDIR/r14-d04-d05/repro-missing
git clone --quiet --no-hardlinks . "$FIXTURE"
cp tools/harness/receipt_guard.py "$FIXTURE/tools/harness/receipt_guard.py"
git -C "$FIXTURE" ls-tree -z --full-tree HEAD -- reports/round-14/validation.json
test ! -e "$FIXTURE/reports/round-14/validation.json" &&
  env -u REFRESH_RECEIPTS python3 .scratch/r14-d04-d05/receipt-writer.py \
    "$FIXTURE" reports/round-14/validation.json R14-D05-measurement-sentinel &&
  test -f "$FIXTURE/reports/round-14/validation.json" &&
  test -f "$FIXTURE/R14-D05-measurement-sentinel"
sha256sum "$FIXTURE/reports/round-14/validation.json"
```

Before executing, require the `ls-tree` result to be empty. If the production
round-14 receipt has since been committed, select a fresh first-run pathname
absent from `HEAD` and substitute it consistently. Do not delete or refresh a
live filed receipt to manufacture this test.

Tested guard SHA-256:
`82eec760c45a81bb12a71423ba3137797a5a84f5c70d7f400c02b236dfd60c5e`.
Runner SHA-256:
`ae064a5165738a666966ce534f4b6dc581c4708b2bd0ae06b12aa8b49eac215f`.
Both were recorded by the counting command on `2026-10-18T00:01:24Z`; the
copied guard still matched the live source after the run.

The paired D04 control targets a receipt genuinely present in the clone's
committed tree and exits 3 before the callback. Together the two controls
establish selective protection, rather than an unconditional refusal or an
unconditional writer. No `REFRESH_RECEIPTS=1` permission is used in either case.
The shipped guard selftest separately passed **20/20**, exit **0**, with
`python3 tools/harness/receipt_guard.py --selftest` on
`2026-10-18T00:01:24Z` (local JSON date `2026-10-17`), retained at
`.scratch/r14-d04-d05/selftest.json`.

The miniature first-run **receipt write** is green. That miniature receipt is
not the production round-14 validation schema, and it does not prove that all
production claims or the round acceptance runner are green. The live
filed-artifact integrity comparison and its separately authorized ledger-append
accounting are recorded in `guard/neg-04.md`; no filed validation receipt changed.

## Historical production first-run blocker — resolved on recheck

The first production observation was blocked at the revision below; it is not
counted as a passing run. At `2026-10-18T00:03:03.091483Z`, command
`/usr/bin/python3 reports/round-14/run-validation.py` in the independent
`.scratch/r14-d04-d05/production-fixture` (current tools and round-14 evidence
overlaid onto the existing-commit clone; no validation receipt copied), with
`REFRESH_RECEIPTS` unset, exited **1** with no receipt and this exception:

```text
NameError: name 'round14_markdown' is not defined
```

Quote location: `.scratch/r14-d04-d05/production-negative-results-initial.json`,
`tests[1].stderr`; traceback names the fixture runner's `validate()` call at
line 553. Read-only source inspection found `round14_evidence()` defined at
line 308 while `validate()` still called `round14_markdown()`. The guard
permitted first-run measurement, but this unrelated runner error prevented
publication.

Subject SHA-256s (same control command/date): guard
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`;
runner `e0b1133083702220cdf5e4a507ee6cab0200d63d2debe55d7f50b02052c689cf`.
Fixture and live sources matched after execution. Counting command:
`export TMPDIR=$PWD/.scratch; PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-production-negatives.py`, run
`2026-10-18T00:03:03Z`, aggregate exit **1**. D04's production refusal control
in the same run passed; no filed receipt bytes changed. This seat edited no
runner source; the successor revision was delivered by its assigned owner.

## Production first-run recheck — receipt publication succeeds

Result: PASS — the real first-run CLI writes a real validation receipt, without
override or exception, and preserves its normal acceptance exit semantics.
This result is about **publication**, not admission of the copied round.

At `2026-10-18T00:05:19.379203Z`, command
`/usr/bin/python3 reports/round-14/run-validation.py`, cwd
`.scratch/r14-d04-d05/production-retry-1`, with `REFRESH_RECEIPTS` unset,
produced a parseable round-14 receipt at the previously missing/uncommitted
`reports/round-14/validation.json`. Its `round` was 14 and `runner` was
`reports/round-14/run-validation.py`. Before SHA-256 was absent; after was:

```text
46028246ddf9aa5764eaedbbdf2baf08d028ec817da03301fe9e2ff60c5cbe5a
```

Exit was **1**, stderr **empty**, and stdout included:

```text
claim O: FAIL
claim D: FAIL
claim C: FAIL
acceptance_checks_passed: False
```

Quote location: `.scratch/r14-d04-d05/production-negative-results.json`,
`tests[1].stdout`. The fixture copied an in-flight round, including this
fragment's then-unresolved historical observation, and did not overlay shared
SCORECARD or historical-ledger changes. Its negative acceptance is therefore
not an integrated verdict on the settled lane. Crucially, it is an ordinary
serialized `acceptance_checks_passed: false` receipt with the matching normal
exit 1, **not** guard refusal, a traceback, or a false claim of exit 0. The
miniature runner above independently establishes the clean exit-0 write path.

**7/7 production first-run assertions passed**: normal acceptance exit preserved,
receipt created, correct runner/round schema, no receipt-guard refusal,
measurement scratch created, committed fixture receipt bytes unchanged, and
`filed_rounds.changed_during_validation == []`. Together with D04's production
refusal recheck, **14/14** passed. Counting command, run
`2026-10-18T00:05:19Z`, aggregate exit **0**:

```sh
export TMPDIR=$PWD/.scratch
R14_NEG_FIXTURE=production-retry-1 PYTHONDONTWRITEBYTECODE=1 \
  python3 .scratch/r14-d04-d05/run-production-negatives.py
```

Subject SHA-256s: guard
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`;
runner `fa750dab8d13d5cf9c737b7194c81be1f32da60e5e6f8ff0b2fd315bac6565cc`.
Both fixture copies still matched the live sources after execution.

Standard selftests also passed: guard **45/45**, exit **0**,
`python3 tools/harness/receipt_guard.py --selftest` at
`2026-10-18T00:03:03Z`, raw `.scratch/r14-d04-d05/selftest-latest.json`;
runner **38/38**, exit **0**,
`python3 reports/round-14/run-validation.py --selftest` at
`2026-10-18T00:05:45Z`, raw `.scratch/r14-d04-d05/runner-selftest-latest.json`.
Both commands used `export TMPDIR=$PWD/.scratch` and disabled bytecode writes.

## Final pinned control

At `2026-10-18T00:07:03.201582Z`, a final fresh fixture at
`.scratch/r14-d04-d05/production-final` repeated the exact production CLI
`/usr/bin/python3 reports/round-14/run-validation.py`, with the receipt absent
from disk and `HEAD`, and `REFRESH_RECEIPTS` unset. A valid round-14 validation
receipt was written; SHA-256:
`fd4b8b7d1537714d4e956f062131db4384ed63417d987f7c6fe71b525ced18c3`.
The CLI returned normal acceptance **exit 1** with `acceptance_checks_passed:
false` and empty stderr; **no exception or receipt-guard refusal** occurred.
Missing routed integration artifacts and un-overlaid shared amendments explain
the copied round's negative acceptance, which is not claimed as green.

D05's publication assertions were **7/7**; together with D04, **14/14**,
aggregate exit **0**. Counting command (lane root, `2026-10-18T00:07:03Z`):

```sh
export TMPDIR=$PWD/.scratch
R14_NEG_FIXTURE=production-final R14_NEG_OUTPUT=production-final-results.json \
  PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-production-negatives.py
```

Raw observations: `.scratch/r14-d04-d05/production-final-results.json`,
`tests[1]`. Tested guard SHA-256:
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`;
tested runner SHA-256:
`11a1bc71011f16cf4371a15b297355a05419226659bb8d1fb1c70c5aa836d744`.
The explicit source/filed-receipt SHA-256 comparison at
`2026-10-18T00:07:14.174651Z` matched both tested subjects to the live tree and
all filed round-8–12 validation receipts to the original snapshot. Runner
selftest at `2026-10-18T00:07:05Z`, command
`python3 reports/round-14/run-validation.py --selftest`, passed **38/38**,
exit **0**; raw stdout `.scratch/r14-d04-d05/runner-selftest-final.json`.
