# R14-D04 — committed receipt refuses before runner effects

- Axis: D / depth (receipt preservation); controls also cover O / operability.
- Prepared: 2026-10-17 local (UTC-03:00). Runtime stamps below are UTC.
- Assignment: without `REFRESH_RECEIPTS`, a runner targeting a committed receipt
  exits **3** and leaves receipt bytes unchanged.
- Status: **PASS for the miniature wired runner**. This fragment does not admit
  round 14 or certify the separately owned production-runner integration.
- Writes: this fragment, `guard/neg-05.md`, and this seat's ignored
  `.scratch/r14-d04-d05/**` fixtures only. No commit/push, no live historical
  runner invocation, and no change to tools or rounds 8–12 by this seat.

## Executed control

At `2026-10-18T00:01:24.630799Z`, with `REFRESH_RECEIPTS` **removed from the
child environment**, the import-based miniature runner targeted an existing
committed receipt in a disposable local clone:

```text
cwd: .scratch/r14-d04-d05/fixture
command: /usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/r14-d04-d05/receipt-writer.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/r14-d04-d05/fixture reports/round-12/validation.json R14-D04-measurement-sentinel
exit: 3
stdout: empty
stderr: receipt_guard: refusing overwrite path=reports/round-12/validation.json committed_sha=a7bc9e9ff05a57515c5efaaa7e50116eb30938ff committed_blob=09caaddb00230605148d195f1cb97e6b1dafbe01; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
```

The stderr quote is the child `stderr` recorded at
`.scratch/r14-d04-d05/negative-results.json`, `tests[0].stderr` (same timestamp).
The exact committed pathname was independently established with
`git -C .scratch/r14-d04-d05/fixture ls-tree -z --full-tree a7bc9e9ff05a57515c5efaaa7e50116eb30938ff -- reports/round-12/validation.json`:
`100644 blob 09caaddb00230605148d195f1cb97e6b1dafbe01` at that pathname.
This uses an existing commit; this seat created no commit.

Before and after SHA-256, obtained by the control's `hashlib.sha256` over
`Path.read_bytes()` on `2026-10-18T00:01:24Z`:

```text
before 773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d
after  773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d
```

The same control asserted the named diagnostic, target pathname, exact override
instruction, empty writer output, and absence of
`R14-D04-measurement-sentinel`. **7/7 assertions passed**. Counting command:
`export TMPDIR=$PWD/.scratch; PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-negatives.py`, run `2026-10-18T00:01:24Z`, exit **0**;
combined with D05, **14/14 assertions passed**. Full raw results remain at
`.scratch/r14-d04-d05/negative-results.json`.

## Runner source and reproducibility

The runner calls `round_runner_main`. In the tested `00:01:24Z` snapshot
(`82eec760…`), the raw API raised `ReceiptGuardError` and the wrapper translated
that refusal to exit 3 before invoking the callback. The later implementation
(`d2297da4…`, tested below) emits the diagnostic and raises `SystemExit(3)`
from the public guard itself. The same miniature runner supports both contracts.
These are actual callback executions, not import-only inspections; a second raw
guard call precedes the intended write.

Exact `.scratch/r14-d04-d05/receipt-writer.py` source:

```python
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "tools" / "harness"))
from receipt_guard import guard_receipt, round_runner_main

receipt = root / sys.argv[2]
sentinel = root / sys.argv[3]


def runner():
    sentinel.write_text("measurement ran\n", encoding="utf-8")
    guard_receipt(receipt, repo_root=root)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text('{"control": "R14-D04-D05", "written": true}\n', encoding="utf-8")
    print("runner: receipt written")
    return 0


raise SystemExit(round_runner_main(runner, receipt, repo_root=root))
```

Observed source digests (`hashlib.sha256`, same counting command/date):

- `tools/harness/receipt_guard.py`:
  `82eec760c45a81bb12a71423ba3137797a5a84f5c70d7f400c02b236dfd60c5e`.
  The clone's tested copy and the live source matched after execution.
- `.scratch/r14-d04-d05/receipt-writer.py`:
  `ae064a5165738a666966ce534f4b6dc581c4708b2bd0ae06b12aa8b49eac215f`.

To repeat, restore the exact runner source above if scratch has been cleaned,
then use a **new** fixture destination from the lane root:

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
FIXTURE=$TMPDIR/r14-d04-d05/repro-committed
git clone --quiet --no-hardlinks . "$FIXTURE"
cp tools/harness/receipt_guard.py "$FIXTURE/tools/harness/receipt_guard.py"
BEFORE=$(sha256sum "$FIXTURE/reports/round-12/validation.json")
env -u REFRESH_RECEIPTS python3 .scratch/r14-d04-d05/receipt-writer.py \
  "$FIXTURE" reports/round-12/validation.json R14-D04-measurement-sentinel
STATUS=$?
test "$STATUS" -eq 3 &&
  test ! -e "$FIXTURE/R14-D04-measurement-sentinel" &&
  test "$BEFORE" = "$(sha256sum "$FIXTURE/reports/round-12/validation.json")"
```

The clone's historical receipt is a fixture copy, never the lane's filed path.
The runner's default callback status is 0, so an ordinary return would not
masquerade as the expected refusal.

## Companion control, integrity, and limits

- `guard/neg-05.md` runs the **same runner and guard** against a missing,
  uncommitted receipt. It exits 0 and writes, disproving an always-refuse guard.
- `export TMPDIR=$PWD/.scratch; PYTHONDONTWRITEBYTECODE=1 python3 tools/harness/receipt_guard.py --selftest`, run `2026-10-18T00:01:24Z`, exited
  **0**, **20/20 controls passed**. Its JSON uses local date `2026-10-17`;
  retained stdout: `.scratch/r14-d04-d05/selftest.json`.
- The counting command compared **609** tracked filed round-8–12 paths against
  the `2026-10-17T23:58:02.030239Z` SHA-256 snapshot at
  `.scratch/r14-d04-d05/filed-before.json`. At `2026-10-18T00:01:24.690526Z`,
  validation receipts were unchanged. The sole differing path was the separately
  assigned R14-D08 `reports/round-12/defects/ledger.json` append
  `FRR-14-EXPOSURE`. Removing exactly the new appended entry reproduced the
  snapshot's committed bytes; unexpected changes: **0**. This is not a claim
  that the whole historical tree had an empty Git diff.
- An initial run at `2026-10-18T00:00:25Z` passed both runtime cases but its
  aggregate script exited 1 because it classified every historical hash change
  as forbidden. The explicit append-only control above accounts for the peer's
  authorized ledger append; it did not relax the receipt-byte assertion or
  alter production code. Initial raw results are preserved at
  `.scratch/r14-d04-d05/negative-results-initial.json`.
- The production round-14 runner was not yet present at the direct check
  `2026-10-18T00:00:34Z`; the 60-second dependency poll detected it at
  `2026-10-18T00:01:49Z`. Its production-main refusal control is below.

## Production-main refusal control

At `2026-10-18T00:03:03.051771Z`, command
`/usr/bin/python3 .scratch/r14-d04-d05/production-committed.py .scratch/r14-d04-d05/production-fixture`
(absolute paths in the raw receipt) imported the **real** round-14 runner from
its independent clone, changed only its in-memory `OUTPUT` constant to
`reports/round-12/validation.json`, and called its unmodified `main([])`.
No runner source, measurement function, or guard was patched. Retargeting
reuses an existing committed receipt without creating a commit or filing a
synthetic round-14 receipt. `REFRESH_RECEIPTS` remained unset.

Result: PASS — exit **3**, no stdout, named committed-path refusal, identical
receipt SHA-256 `773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d`
before/after, and **no fixture `.scratch` directory created**, proving refusal
before the production runner's first measurement-side directory creation.
**7/7 assertions passed**. Command/date for that count:
`export TMPDIR=$PWD/.scratch; PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-production-negatives.py`,
`2026-10-18T00:03:03Z`. The aggregate exited 1 because the separate production
D05 first-run case crashed, as recorded in `guard/neg-05.md`; this is not a
claim that the full production runner was green.

Raw quote/digest/check locations:
`.scratch/r14-d04-d05/production-negative-results-initial.json`, `tests[0]`
and `subjects_sha256`. Guard SHA-256:
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`;
runner SHA-256:
`e0b1133083702220cdf5e4a507ee6cab0200d63d2debe55d7f50b02052c689cf`.
Both fixture copies matched the live sources after the run.

Exact retargeting driver, `.scratch/r14-d04-d05/production-committed.py`:

```python
import importlib.util
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("round14_negative", root / "reports/round-14/run-validation.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.OUTPUT = "reports/round-12/validation.json"
raise SystemExit(module.main([]))
```

The fresh fixture was made by `git clone --quiet --no-hardlinks` using the
existing lane commit, then overlaying the live `tools/` and `reports/round-14/`
trees while excluding `validation.json` and `__pycache__`. This tests actual
runner preflight behavior, but does not certify its late-publication race
boundary or permit any live historical writer invocation.

## Successor-runner recheck

At `2026-10-18T00:05:19.336685Z`, the same driver and committed receipt target
were rechecked in a new clone at `.scratch/r14-d04-d05/production-retry-1`.
Exit **3**, empty stdout, named path/HEAD refusal, unchanged receipt SHA-256
`773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d`, and no
measurement `.scratch` directory all remained true. **7/7 assertions passed**.
The corresponding real first-run CLI now wrote its receipt, as recorded in
`guard/neg-05.md`; combined production assertions: **14/14**, aggregate exit
**0**. Counting command/date:

```sh
# 2026-10-18T00:05:19Z, lane root
export TMPDIR=$PWD/.scratch
R14_NEG_FIXTURE=production-retry-1 PYTHONDONTWRITEBYTECODE=1 \
  python3 .scratch/r14-d04-d05/run-production-negatives.py
```

Raw observations: `.scratch/r14-d04-d05/production-negative-results.json`,
`tests[0]`; subject hashes: `subjects_sha256`. Guard SHA-256 remained
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`.
Successor runner SHA-256:
`fa750dab8d13d5cf9c737b7194c81be1f32da60e5e6f8ff0b2fd315bac6565cc`.
Fixture copies matched both live sources after execution. Standard selftests:
`python3 tools/harness/receipt_guard.py --selftest` at
`2026-10-18T00:03:03Z`: **45/45**, exit **0**;
`python3 reports/round-14/run-validation.py --selftest` at
`2026-10-18T00:05:45Z`: **38/38**, exit **0**. Both used the in-lane TMPDIR and
bytecode-disabled environment; raw JSON is at
`.scratch/r14-d04-d05/selftest-latest.json` and
`.scratch/r14-d04-d05/runner-selftest-latest.json` respectively.

## Final pinned control

The final fresh-fixture run at `2026-10-18T00:07:03.160165Z` repeated the real
`main([])` retargeted committed-receipt control: **exit 3**, receipt unchanged
at SHA-256 `773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d`,
no stdout, no measurement scratch, and the named committed-path/HEAD refusal.
D04 **7/7** and paired D05 **7/7**, aggregate **14/14**, exit **0**.
Counting command (lane root, `2026-10-18T00:07:03Z`):

```sh
export TMPDIR=$PWD/.scratch
R14_NEG_FIXTURE=production-final R14_NEG_OUTPUT=production-final-results.json \
  PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-production-negatives.py
```

Raw observations are retained separately at
`.scratch/r14-d04-d05/production-final-results.json`, `tests[0]`. Tested guard
SHA-256: `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`;
tested runner SHA-256:
`11a1bc71011f16cf4371a15b297355a05419226659bb8d1fb1c70c5aa836d744`.
Both still matched the live sources at the explicit SHA-256 comparison
`2026-10-18T00:07:14.174651Z`; that command also reconfirmed all filed round-8–12
validation receipt hashes match the original snapshot. Runner selftest at
`2026-10-18T00:07:05Z`, command
`python3 reports/round-14/run-validation.py --selftest`, passed **38/38** with
exit **0**; raw stdout `.scratch/r14-d04-d05/runner-selftest-final.json`.
