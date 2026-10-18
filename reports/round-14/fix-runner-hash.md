# R14-O05 — round-10 runner-hash disposition

- Axis: O / operability; evidence depth and calibration are non-regression controls.
- Defect: `R10-RUNHASH`, corresponding to round-12 sweep finding F-06.
- Disposition: **resolved-by-documentation with control**. Reconfirm the existing
  append-only correction, pin the retained final runner, and retain the earlier
  draft prefix as **to-verify**, not as a current or recovered historical pin.
- Scope: this new round-14 record only; no historical runner or receipt is executed
  or rewritten. This is not a new round-10 acceptance run or admission decision.

## Evidence and reconciliation

`reports/round-12/defects/ledger.json:119-123` still routes the unresolved
historical citation. However, `reports/round-12/defects/fix-10.md:52-63` already
supplies the full current digest and dispositions its append-only correction as
`fixed-with-control`; `reports/round-12/defects/routed.md:106-108` explicitly
excludes F-06 from open findings. This record applies and independently verifies
that existing correction, rather than silently changing any of those filed
statuses.

The source of the uncertain prefix is
`reports/round-10/report-draft.md:102` and `:126-131`: the latter binds
`4529ac3d…` to the draft's reported **18:31:40 −03:00** receipt on 2026-10-17,
explicitly calling it an earlier floor, not a verdict. The retained final receipt
instead names the full digest at `reports/round-10/validation.json:808-809`.
The old prefix could describe a transient pre-finalization worktree version,
but neither its full digest nor its bytes have been recovered by this check.
No retained match is not proof that the snapshot never existed.

The fresh control below, executed at **2026-10-17T23:57:48+00:00**, found the
current runner and receipt byte-identical to the round-10 admission commit
`94ca098b8ab03be52ec80f6925538e5e2c0ed327`. Its `git log --all --full-history`
scan of the runner path returned **1 commit, 0 prefix matches**; these counts
refer only to reachable path history in this local repository, not deleted,
unreachable, external, or never-committed snapshots. The observed HEAD was
`a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`.

## Append-only integration payload

```json
{
  "id": "R10-RUNHASH",
  "assignment": "R14-O05",
  "status": "resolved-by-documentation",
  "runner": "reports/round-10/run-validation.py",
  "current_round10_runner_sha256": "23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e",
  "retained_commit": "94ca098b8ab03be52ec80f6925538e5e2c0ed327",
  "retained_runner_git_blob": "03d4c27c8ff615658107700448e2d66dee04f036",
  "receipt": "reports/round-10/validation.json",
  "receipt_sha256": "e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94",
  "historical_prefix": "4529ac3d",
  "historical_prefix_status": "to-verify",
  "historical_prefix_disposition": "Unrecovered draft snapshot; not a current pin and not asserted equivalent to the retained runner.",
  "applies_existing_correction": "reports/round-12/defects/fix-10.md",
  "control": "reports/round-14/fix-runner-hash.md: Control A and Control B"
}
```

Use the full SHA-256 and retained commit above in a new final-state integration
record. Preserve the draft's prefix and time as historical, unverified evidence;
do not replace the old prefix in filed bytes or present the full current digest
as a reconstruction of it. A future historical-resolution claim must supply the
actual old bytes and their full digest in another new record. The separate
`d78da29f…` citation concerns the round-8 runner repair, not the round-10 runner
(`reports/round-12/defects/sweep-r10.md:23-31`), and is not a substitute pin here.

## Control A — retained bytes, receipt binding, history, and preservation

Read-only command executed on 2026-10-17 at the timestamp above, from the lane
root. It imports no round runner and writes no scratch or receipt:

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, subprocess

runner = 'reports/round-10/run-validation.py'
receipt = 'reports/round-10/validation.json'
filed = '94ca098b8ab03be52ec80f6925538e5e2c0ed327'
prefix = '4529ac3d'
expected = '23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e'
def git(*args):
    return subprocess.check_output(['git', *args])
def sha(data):
    return hashlib.sha256(data).hexdigest()
commits = git('log', '--all', '--full-history', '--format=%H', '--', runner).decode().splitlines()
retained = {c: sha(git('show', f'{c}:{runner}')) for c in commits}
live_runner = Path(runner).read_bytes()
filed_runner = git('show', f'{filed}:{runner}')
live_receipt = Path(receipt).read_bytes()
filed_receipt = git('show', f'{filed}:{receipt}')
protected = [f'reports/round-{n}' for n in range(8, 13)]
clean = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', *protected]).returncode
result = {
    'observed_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'head': git('rev-parse', 'HEAD').decode().strip(),
    'filed_commit': filed,
    'runner_git_blob': git('rev-parse', f'{filed}:{runner}').decode().strip(),
    'current_runner_sha256': sha(live_runner),
    'filed_runner_sha256': sha(filed_runner),
    'receipt_runner_sha256': json.loads(live_receipt)['runner_sha256'],
    'filed_receipt_runner_sha256': json.loads(filed_receipt)['runner_sha256'],
    'live_receipt_sha256': sha(live_receipt),
    'filed_receipt_sha256': sha(filed_receipt),
    'runner_matches_filed_bytes': live_runner == filed_runner,
    'receipt_matches_filed_bytes': live_receipt == filed_receipt,
    'runner_history_commits_scanned': len(commits),
    'runner_history': retained,
    'historical_prefix': prefix,
    'historical_prefix_matches': [c for c, digest in retained.items() if digest.startswith(prefix)],
    'filed_rounds_8_through_12_diff_exit': clean,
}
print(json.dumps(result, indent=2, sort_keys=True))
assert {sha(live_runner), sha(filed_runner), json.loads(live_receipt)['runner_sha256'], json.loads(filed_receipt)['runner_sha256']} == {expected}
assert live_runner == filed_runner and live_receipt == filed_receipt
assert retained and not result['historical_prefix_matches']
assert clean == 0
print('CONTROL_A=PASS')
PY
```

Initial observation at **2026-10-17T23:57:48+00:00**: exit **0**,
`CONTROL_A=PASS`; the runner, its committed bytes, and both receipt pins agree
on the full digest in the payload. Both receipt byte hashes equal
`e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94`.
The runner Git blob is `03d4c27c8ff615658107700448e2d66dee04f036` (an object
identifier, not its SHA-256). `historical_prefix_matches=[]`, and
`filed_rounds_8_through_12_diff_exit=0`.

**After-write recheck, not silently treated as green:** executing the delivered
Control A at **2026-10-17T23:58:49+00:00** returned exit **1** solely at
`assert clean == 0`. The runner/receipt bindings and history results remained
identical. The first Control B attempt also reached and failed the same broad
clean-tree assertion after its payload and negative assertions succeeded.
A subsequent read-only command on 2026-10-17,
`git status --short -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12; git diff HEAD -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12`,
identified `reports/round-10/findings-tracker.json` with a new `errata` key
containing `R14-O03`, a concurrent correction outside this assignment. This
worker did not write or revert that path. The integrator owns its preservation
assessment; this record does not claim the broad clean-tree control is green.

## Control B — delivered payload and negative controls

The final task-scoped after-control below verifies the delivered payload and
all its cited filed source paths, independently of the broader shared-tree
cleanliness result (which remains reported separately, not suppressed). The
in-memory negative controls reject the old short prefix, an incorrect full
digest, and altered runner bytes; nothing is planted in any historical artifact.

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, re, subprocess

text = Path('reports/round-14/fix-runner-hash.md').read_text()
record = json.loads(re.search(r'```json\n(.*?)\n```', text, re.S).group(1))
runner = Path(record['runner']).read_bytes()
receipt = Path(record['receipt']).read_bytes()
filed = record['retained_commit']
def git(*args):
    return subprocess.check_output(['git', *args])
def sha(data):
    return hashlib.sha256(data).hexdigest()
def binds(digest, data):
    return len(digest) == 64 and digest == sha(data)
pin = record['current_round10_runner_sha256']
assert record['id'] == 'R10-RUNHASH' and record['assignment'] == 'R14-O05'
assert record['status'] == 'resolved-by-documentation'
assert record['historical_prefix_status'] == 'to-verify'
assert binds(pin, runner)
assert runner == git('show', f"{filed}:{record['runner']}")
assert receipt == git('show', f"{filed}:{record['receipt']}")
assert json.loads(receipt)['runner_sha256'] == pin
assert sha(receipt) == record['receipt_sha256']
assert git('rev-parse', f"{filed}:{record['runner']}").decode().strip() == record['retained_runner_git_blob']
assert pin in Path(record['applies_existing_correction']).read_text()
assert record['historical_prefix'] in Path('reports/round-10/report-draft.md').read_text()
assert not binds(record['historical_prefix'], runner)
assert not binds('0' * 64, runner)
assert not binds(pin, runner + b'\nnegative-control\n')
sources = [record['runner'], record['receipt'],
           'reports/round-10/report-draft.md', record['applies_existing_correction'],
           'reports/round-12/defects/ledger.json',
           'reports/round-12/defects/routed.md',
           'reports/round-12/defects/sweep-r10.md']
for source in sources:
    assert Path(source).read_bytes() == git('show', f'HEAD:{source}'), source
protected = [f'reports/round-{n}' for n in range(8, 13)]
changed = git('diff', '--name-only', 'HEAD', '--', *protected).decode().splitlines()
print('observed_at=' + datetime.now(timezone.utc).isoformat(timespec='seconds'))
print('CONTROL_B=PASS payload_binding=PASS negative_controls=3/3 cited_filed_sources_unchanged=7/7')
print('broader_filed_tree_changed_paths=' + json.dumps(changed))
PY
```

Observed at **2026-10-17T23:59:30+00:00**, executing Control B directly from
this Markdown file: exit **0**,
`CONTROL_B=PASS payload_binding=PASS negative_controls=3/3 cited_filed_sources_unchanged=7/7`.
The separately reported changed-path list was
`["reports/round-10/findings-tracker.json"]`; the broad preservation caveat above
therefore remains. `git diff --check` at the same date/time exited **0**.

This bounded documentation fix does not require historical validator execution.
Round-14 battery/craft/D2/D3 regression receipts and the consolidated routing
ledger remain the respective integration owners' work; this record does not
assert that those independent checks passed.
