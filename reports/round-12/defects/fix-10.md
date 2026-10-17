# R12-O10 bounded correction — R10 F-06

- Audit date: 2026-10-17.
- Sweep source: `reports/round-12/defects/sweep-r10.md`, finding F-06.
- Scope: append-only correction of the current runner-digest pointer. No round-8–11 file was changed.

## Bounded finding

The filed round-10 draft carries the truncated runner prefix `4529ac3d…` as an earlier snapshot, but that prefix does not resolve to a retained revision of the round-10 runner. The correction below supplies the current full digest while preserving the historical snapshot wording; it does not rewrite the draft or the validation receipt.

## Before controls

The current runner digest and the `runner_sha256` field in the filed round-10 validation receipt were compared with this read-only command at `2026-10-17T20:05:15-03:00`:

```sh
date -Is; python3 - <<'PY'
import hashlib, json
from pathlib import Path
runner = Path('reports/round-10/run-validation.py')
receipt = json.loads(Path('reports/round-10/validation.json').read_text(encoding='utf-8'))
actual = hashlib.sha256(runner.read_bytes()).hexdigest()
pinned = receipt.get('runner_sha256')
print(f'current_runner_sha256={actual}')
print(f'receipt_runner_sha256={pinned}')
print(f'match={actual == pinned}')
assert actual == pinned
PY
```

Observed: both digests are `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e`; `match=True`.

The old prefix was searched in all retained blobs for this runner at `2026-10-17T20:05:15-03:00`:

```sh
date -Is; python3 - <<'PY'
import hashlib, subprocess
path = 'reports/round-10/run-validation.py'
prefix = '4529ac3d'
commits = subprocess.check_output(['git', 'log', '--all', '--format=%H', '--', path], text=True).splitlines()
hits = []
for commit in commits:
    result = subprocess.run(['git', 'show', f'{commit}:{path}'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if result.returncode == 0 and hashlib.sha256(result.stdout).hexdigest().startswith(prefix):
        hits.append(commit)
print(f'commits_scanned={len(commits)} prefix={prefix} matches={hits}')
assert not hits
PY
```

Observed: `commits_scanned=1 prefix=4529ac3d matches=[]`. The historic prefix is retained only as a timestamped draft snapshot, not as the current runner pin.

## Append-only correction

For any finalized current-state report reference, use this full runner digest; the old short prefix stays identified as the earlier draft snapshot:

```json
{
  "current_round10_runner_sha256": "23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e",
  "supersedes_as_current_pin": "4529ac3d…"
}
```

**Disposition: fixed-with-control (append-only correction).** This fragment is the correction record; the filed draft and validation receipt remain untouched.

## After control

Command run at `2026-10-17T20:05:59-03:00` (immediately preceded by `date -Is`):

```sh
date -Is; python3 - <<'PY'
import hashlib, json
from pathlib import Path
receipt_text = Path('reports/round-12/defects/fix-10.md').read_text(encoding='utf-8')
runner = Path('reports/round-10/run-validation.py')
validation = json.loads(Path('reports/round-10/validation.json').read_text(encoding='utf-8'))
actual = hashlib.sha256(runner.read_bytes()).hexdigest()
pinned = validation.get('runner_sha256')
corrected = actual in receipt_text
print(f'correction_contains_current_hash={corrected} runner_matches_receipt={actual == pinned}')
print(f'current_runner_sha256={actual}')
assert corrected and actual == pinned
PY
```

Observed: `correction_contains_current_hash=True runner_matches_receipt=True`; current digest is `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e`.
