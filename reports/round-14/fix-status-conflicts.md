# R14-O07 — round-10 stale-fixed conflict reconciliation

- **Axis:** O / operability; evidence calibration and filed-artifact preservation are constraints.
- **Prepared:** 2026-10-17; worker R14-O07.
- **Route:** `reports/round-12/defects/routed.md:50-56`, R10-SWEEP F-03; underlying audit `reports/round-12/defects/sweep-r10.md:23-31`.
- **Disposition:** resolved-by-documentation. The ledger-consistency defect is resolved by this new correction, not by a retained runner repair. This record does not assert a new runtime pass or change any historical admission.
- **Write scope:** this new round-14 file only. The filed round-10 ledger, round-8 runner, round-10 runner, and receipts are not edited or executed by this worker.

## Single authoritative correction entry

The sole current status for the command below is **`stale-documented`** (documented-stale). Apply this append-only correction when interpreting the filed ledger; do not replace its historical rows or their recorded exits/output hashes. The status is bound to retained runner bytes, not to whether an old repair report exists.

```json
{
  "id": "R14-O07",
  "finding": "R10-SWEEP F-03",
  "disposition": "resolved-by-documentation",
  "command": "python3 reports/round-8/run-validation.py",
  "status": "stale-documented",
  "reason": "The retained round-8 runner is byte-identical to the round-10 admission blob, lacks gate_blob_for_pin, and does not retain the fix-20 repair. Conflicting repair assertions are historical intermediate observations, not the final runner state.",
  "filed_ledger": "reports/round-10/drift/ledger.json",
  "supersedes_ledger_rows_1based": [114, 132, 174],
  "retained_runner": "reports/round-8/run-validation.py",
  "retained_runner_sha256": "7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369",
  "admission_revision": "94ca098b8ab03be52ec80f6925538e5e2c0ed327",
  "unretained_fix20_runner_sha256": "d78da29fdacc75d425e21c21fa2d299deff487f17724e8fa7bd73f5b4fc14735",
  "current_execution_exit": null,
  "current_execution_output_sha256": null,
  "measurement_mode": "Read-only ledger, retained-byte and AST checks; no round validator run.",
  "control": "Read-only reconciliation and planted-status control below",
  "protected_sha256": {
    "reports/round-8/run-validation.py": "7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369",
    "reports/round-10/drift/ledger.json": "9ae5ed2ee5599629cfb331d85fd5028a87c63e41b58d36c65b3a74a1c770b698",
    "reports/round-10/run-validation.py": "23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e",
    "reports/round-10/validation.json": "e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94",
    "reports/round-10/drift/fix-20.md": "eba997031d79ff8d4f791c304a8ac3b067f7c66e5a973a037d089e36cfc8c07c"
  }
}
```

## What is superseded, and what is preserved

The row numbers below are **one-based positions in the filed JSON array**, not old worker-local row numbers. The read-only control below reproduces the enumeration and counts.

- **Row 114, `shard-13`:** `reports/round-10/drift/ledger.json:1027-1034`, source `SCORECARD.md:114,115,116`. Its `stale-fixed` label and post-fix note describe the intermediate `d78da29f…` runner. Preserve the historical exit/output; supersede the implication that this fix survived integration.
- **Row 132, `fix-20`:** `reports/round-10/drift/ledger.json:1190-1197`, source `SCORECARD.md:104`. Its `stale-fixed` label and claim that the filed receipt is superseded do not describe the retained runner. `reports/round-10/drift/fix-20.md:35-49,51-79` remains evidence of a proposed/applied intermediate repair and its reported mirror control, not evidence that those runner bytes were retained.
- **Row 174, `shard-12`:** `reports/round-10/drift/ledger.json:1569-1575`, source `shard-12 receipts table`. Preserve its `stale-documented` verdict and historical failure observation. Supersede only its note's assertion that fix-20 repaired the final runner; that note points back to the same unretained repair.

`LOG.md:3003-3006` records the integrator's reversion: “reverted by the integrator; staleness documented in the ledger instead of back-patched.” The retained `replay_isolated()` still retrieves `HEAD:<gate path>` at `reports/round-8/run-validation.py:1205-1233`, rather than resolving the manifest digest through `gate_blob_for_pin`.

The filed round-10 F pass does not adjudicate this conflict. `reports/round-10/validation.json:800,803` explicitly limits command coverage to ledger presence and says prior-round runners are not executed. `reports/round-10/run-validation.py:622-638` accepts an existing fix-evidence path without binding it to retained runner bytes. This correction does not rewrite or reinterpret that historical structural pass as an independently reproduced repair.

## Read-only reconciliation and planted-status control

**Before-write observation:** 2026-10-17T23:57:38.133469+00:00 at HEAD `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`. Read-only Python enumeration, SHA-256, `git show`, and AST inspection found the row identities and protected digests embedded above; each protected path matched its HEAD blob. The command below is the reproducible counting and after-write control for those same assertions.

Run from the lane root. It writes no scratch files, imports no runner, and invokes no validator. The negative control plants `stale-fixed` only in memory and requires rejection against the actual retained bytes. The positive control accepts the correction's documented-stale status; it is not a replay-success test.

```bash
export TMPDIR="$PWD/.scratch"
python3 -B - <<'PY'
import ast
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

report = Path('reports/round-14/fix-status-conflicts.md')
blocks = re.findall(r'```json\n(.*?)\n```', report.read_text(), re.S)
assert len(blocks) == 1
entry = json.loads(blocks[0])
assert entry['id'] == 'R14-O07'
assert entry['disposition'] == 'resolved-by-documentation'
assert entry['command'] == 'python3 reports/round-8/run-validation.py'
assert entry['status'] == 'stale-documented'
ledger = json.loads(Path(entry['filed_ledger']).read_text())
matched = [(i, row) for i, row in enumerate(ledger, 1)
           if row['command'] == entry['command']]
positions = [i for i, row in matched]
assert positions == entry['supersedes_ledger_rows_1based'] == [114, 132, 174]
verdicts = dict(collections.Counter(row['round10_verdict']
                                   for i, row in matched))
assert verdicts == {'stale-fixed': 2, 'stale-documented': 1}
runner = Path(entry['retained_runner']).read_bytes()
digest = hashlib.sha256(runner).hexdigest()
admission = subprocess.check_output([
    'git', 'show', entry['admission_revision'] + ':' + entry['retained_runner']])
assert runner == admission
assert digest == entry['retained_runner_sha256']
assert digest != entry['unretained_fix20_runner_sha256']
names = {node.name for node in ast.walk(ast.parse(runner.decode()))
         if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
helper_present = 'gate_blob_for_pin' in names
assert not helper_present

def status_supported(status):
    if status == 'stale-fixed':
        return (digest == entry['unretained_fix20_runner_sha256']
                and helper_present)
    return (status == 'stale-documented'
            and runner == admission and not helper_present)

assert status_supported(entry['status'])
assert not status_supported('stale-fixed')
assert entry['current_execution_exit'] is None
assert entry['current_execution_output_sha256'] is None
for name, expected in entry['protected_sha256'].items():
    data = Path(name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == expected, name
    assert data == subprocess.check_output(['git', 'show', 'HEAD:' + name]), name
print('observed_at=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
print('canonical_entries=' + str(len(blocks)))
print('ledger_rows=' + str(len(ledger)))
print('matching_rows_1based=' + json.dumps(positions))
print('historical_matching_verdicts=' + json.dumps(verdicts, sort_keys=True))
print('status=' + entry['status'])
print('retained_runner_sha256=' + digest)
print('runner_matches_round10_admission=True')
print('gate_blob_for_pin_function_present=' + str(helper_present))
print('positive_documented_status_control=PASS')
print('negative_stale_fixed_control=REJECTED')
print('protected_files_unchanged=' + str(len(entry['protected_sha256'])))
print('protected_files_match_HEAD=True')
PY
```

**Prevention control:** do not promote this command back to `stale-fixed` based on the existence of `fix-20.md` or a passing structural receipt. Any successor correction must name a permitted retained artifact, bind its full digest to the actual repair, and provide an isolated runtime control without overwriting filed receipts. The read-only check above must continue rejecting a stale-fixed assertion for the retained `7eaa3678…` runner. The receipt-guard implementation and full round-14 regressions belong to their assigned owners; this file claims neither.

## Executed control receipt

Executed the preceding fenced Bash command verbatim from the lane root on **2026-10-17T23:59:32.866130+00:00**; exit **0**. This is the dated counting command for the row and protected-file counts, not an execution of the historical round-8 command.

```text
canonical_entries=1
ledger_rows=192
matching_rows_1based=[114, 132, 174]
historical_matching_verdicts={"stale-documented": 1, "stale-fixed": 2}
status=stale-documented
retained_runner_sha256=7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369
runner_matches_round10_admission=True
gate_blob_for_pin_function_present=False
positive_documented_status_control=PASS
negative_stale_fixed_control=REJECTED
protected_files_unchanged=5
protected_files_match_HEAD=True
```

The preservation assertion is scoped to the protected paths in the correction entry, not to the entire concurrently edited lane. LOG/SCORECARD and routed-resolution integration remain with the parent; no independent round admission is claimed.
