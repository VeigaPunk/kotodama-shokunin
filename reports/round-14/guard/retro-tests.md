# R14-D06..D07 — historical receipt guard replay

Axes: D / committed-receipt protection; O / unchanged filed runners; C / bounded replay evidence.

## Executed result

Command, from the lane root:

```sh
export TMPDIR="$PWD/.scratch"
PYTHONDONTWRITEBYTECODE=1 python3 reports/round-14/guard/retro-tests.py
```

Executed `2026-10-18T00:02:43.159342+00:00` through `2026-10-18T00:02:57.054385+00:00`: exit **0**, **12/12 controls passed**, `passed: true`. Machine-readable evidence, including every child command, date, exit, stdout/stderr, and before/after SHA-256, is `reports/round-14/guard/retro-tests.json`.

Guard bytes tested: `tools/harness/receipt_guard.py`, SHA-256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`. The source was unchanged throughout the replay. The replay harness guards its own receipt both before measurement and immediately before publication through `round_runner_main(..., write_receipt=publish_receipt)`.

## D06 — actual historical runner controls

The harness clones locally with `--no-hardlinks --no-checkout`, checks out a detached historical revision, and copies only the new guard into that disposable clone. The historical runner is neither patched nor replaced. Round-8 and round-9 clone controls execute concurrently; each clone has its own `TMPDIR` below the lane's `.scratch`.

- **Round 8:** exact required checkout `e1694bad6ac96aca45a11ca5746582b275929355`; committed receipt `reports/round-8/validation.json`.
- **Round 9:** actual filing checkout `9dc18ec1339bffd6f81e74f1a5742464ef578749`; committed receipt `reports/round-9/validation.json`. Round 9 does **not** exist at `e1694ba`: the dated `git ls-tree -r --name-only e1694bad6ac96aca45a11ca5746582b275929355 -- reports/round-9` control returned exit 0 and no paths (`retro-tests.json#/round9_absent_at_required_round8_snapshot`). No fictitious round-9 receipt was added to the earlier snapshot.

For each historical checkout, the command above executes these controls:

1. CLI probe refuses the committed receipt with exit **3**, named `RECEIPT-GUARD-COMMITTED` diagnostic, and identical before/after bytes.
2. The importable guard wraps the **real unchanged historical runner**. With `REFRESH_RECEIPTS` removed from the environment, it exits **3** before the runner-entry sentinel or any runner measurement/write. Receipt bytes remain identical.
3. The real unguarded runner is executed **only in the clone**. It changes the committed receipt bytes, proving that the protection is load-bearing rather than a no-op. The fixture receipt is restored before the next control.
4. Literal `REFRESH_RECEIPTS=1` permits the wrapped real runner, creates its entry sentinel, and allows its receipt write. Normal historical runner exit semantics are retained.
5. With the override removed again, the now-dirty committed receipt is refused with exit **3**; dirty bytes remain untouched and the runner is not entered.
6. `git diff --exit-code HEAD -- reports/round-N/run-validation.py` is empty and exits **0** inside the clone; the runner SHA-256 is unchanged.

Named diagnostic location: `retro-tests.json#/cases/0/controls/1/execution/stderr` records:

```text
receipt_guard: refusing overwrite path=reports/round-8/validation.json committed_sha=e1694bad6ac96aca45a11ca5746582b275929355 committed_blob=ca49c2e81c0215abd334bfa4073f907be7fe579e; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
```

The corresponding round-9 refusal is at `retro-tests.json#/cases/1/controls/1/execution/stderr`, bound to its full filing commit and receipt blob.

The adverse round-8 unguarded/refresh controls exit **1** because the clone replay cannot evaluate its D2 frozen rows; they still execute the actual writer and change the receipt from acceptance true to false. The corresponding round-9 controls exit **0**, retain acceptance true, and nevertheless change the receipt bytes. These are intentional preservation controls, **not** a re-adjudication of either historical admission. Full legacy output is retained in each control's `execution.stdout`.

Historical corroboration is separately bound by the dated `git show` commands under `retro-tests.json#/historical_evidence`: both original filed receipts differ from their bytes at the round-11 clobber commit `a3f6fcef2d92a1099581140c81d4264e9a4e2aa3`. A preserved true acceptance flag alone would not have detected the round-9 loss.

## D07 — filed rounds 8–11 remain untouched

Before and after the replay, the same counting command checks exactly these filed runners:

```text
reports/round-8/run-validation.py
reports/round-9/run-validation.py
reports/round-10/run-validation.py
reports/round-11/run-validation.py
```

For that explicit path set, `git diff --exit-code 926c86f8be3cc9307f8f10dce55768c290b6f94d -- ...`, `git diff --cached --exit-code 926c86f8be3cc9307f8f10dce55768c290b6f94d -- ...`, `git diff --exit-code HEAD -- ...`, and `git status --porcelain -- ...` all exit **0** with empty output. Baseline blob SHA-256 values match the live files. Exact expanded commands and dates are in `retro-tests.json#/D07_runners_before` and `retro-tests.json#/D07_runners_after`.

The live lane's round-8–11 runners **and** their `validation.json` files also have identical before/after SHA-256 maps (`retro-tests.json#/main_tree_before_sha256`, `#/main_tree_after_sha256`). The main-tree preservation check does not claim that unrelated concurrent-worker paths are clean.

## Additional regression and limits

At `2026-10-18T00:03:29.106235+00:00`, the command below exited **0**, with `selftest_passed: true` and **45/45 controls passed**, using the same guard SHA-256 as the replay:

```sh
export TMPDIR="$PWD/.scratch"
PYTHONDONTWRITEBYTECODE=1 python3 tools/harness/receipt_guard.py --selftest
```

An initial harness-only control failure exposed relative `runpy` paths, which do not give the historical runners the absolute `__file__` their receipt logic expects. The harness now resolves that execution path; both explicit-refresh controls execute without traceback and prove the corrected path reaches the real writer. No historical runner was changed to accommodate the harness.

The guard is cooperative preflight protection, not a filesystem sandbox or race-proof lock. **Filed rounds 8–11 remain unwired as required; direct invocation of those old runners can still overwrite their receipts.** Use an isolated clone for historical rechecks, not the live lane. The round-14 runner-wiring and append-only exposure erratum are other seats' deliverables; this fragment does not certify them or whole-round admission.

Only the assigned new replay harness, its new receipt, and this evidence fragment were filed by this worker. No `git commit` or push was run; no round-8–12 filed artifact was edited in the live lane. Parent integration records this fragment in append-only `LOG.md`.
