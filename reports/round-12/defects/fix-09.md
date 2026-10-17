# R12-O09 bounded correction — R10 F-04

- Audit date: 2026-10-17.
- Sweep source: `reports/round-12/defects/sweep-r10.md`, finding F-04.
- Scope: append-only correction record for the omitted verifier pointer. No round-8–11 file was changed.

## Bounded finding

The filed `reports/round-10/findings-tracker.json` `final_state.verify_files` list omits the existing `findings-verify-3.md`. The round-10 sweep classifies this as a low-severity summary-field transcription defect and requires corrections in a new record, not a rewrite of the filed tracker.

## Before control

A first probe at `2026-10-17T19:57:05-03:00` compared `glob.glob()` paths (`reports/round-10/...`) directly with the tracker's basenames (`findings-verify-*.md`). It printed `listed_count=3 actual_count=4` and incorrectly listed all four paths as omitted. This was a control-normalization error, not a repository finding; it was not used for disposition. The following corrected command normalizes both sides to basenames.

Command run at `2026-10-17T19:57:12-03:00`:

```sh
python3 - <<'PY'
import glob, json
from pathlib import Path
with open('reports/round-10/findings-tracker.json', encoding='utf-8') as f:
    tracker = json.load(f)
listed = tracker['final_state']['verify_files']
actual = sorted(Path(p).name for p in glob.glob('reports/round-10/findings-verify-*.md'))
omitted = sorted(set(actual) - set(listed))
print(f"listed_count={len(listed)} actual_count={len(actual)} omitted_count={len(omitted)}")
print(f"listed={listed}")
print(f"actual={actual}")
print(f"omitted={omitted}")
PY
```

Observed: `listed_count=3 actual_count=4 omitted_count=1`; `omitted=['findings-verify-3.md']`. The pre-correction tracker digest, measured by `sha256sum reports/round-10/findings-tracker.json` at `2026-10-17T20:00:17-03:00`, was `5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc`.

## Append-only correction

Replacement value for `final_state.verify_files` (the established tracker convention is basenames):

```json
{
  "final_state": {
    "verify_files": [
      "findings-verify-1.md",
      "findings-verify-2.md",
      "findings-verify-3.md",
      "findings-verify-4.md"
    ]
  }
}
```

**Disposition: fixed-with-control (append-only correction).** This fragment supplies the corrected verifier list as the replacement record, without back-patching the filed round-10 tracker. The round-12 defect ledger can cite this fragment as the fix evidence.

## After control

The first post-control attempt at `2026-10-17T20:00:55-03:00` printed matching counts, but its unanchored code-fence parser was not sufficiently discriminating. A repeat at `2026-10-17T20:01:27-03:00` failed at the one-block assertion because it also matched a fence-like substring inside the embedded command. Both results are superseded; this was a control-parser issue, not a mismatch in the corrected list or the filed tracker.

The corrected line-exact-fence control ran at `2026-10-17T20:04:54-03:00` (immediately preceded by `date -Is`):

```sh
date -Is; python3 - <<'PY'
import glob, hashlib, json, re
from pathlib import Path
receipt = Path('reports/round-12/defects/fix-09.md').read_text(encoding='utf-8')
blocks = []
in_json = False
json_lines = []
for line in receipt.splitlines():
    if line == "```json":
        in_json = True
        json_lines = []
    elif in_json and line == "```":
        blocks.append(chr(10).join(json_lines))
        in_json = False
    elif in_json:
        json_lines.append(line)
assert len(blocks) == 1
correction = json.loads(blocks[0])['final_state']['verify_files']
actual = sorted(Path(p).name for p in glob.glob('reports/round-10/findings-verify-*.md'))
missing = sorted(set(actual) - set(correction))
extra = sorted(set(correction) - set(actual))
tracker_hash = hashlib.sha256(Path('reports/round-10/findings-tracker.json').read_bytes()).hexdigest()
expected_hash = '5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc'
print(f'correction_count={len(correction)} actual_count={len(actual)} missing={missing} extra={extra}')
print(f'tracker_hash_unchanged={tracker_hash == expected_hash} sha256={tracker_hash}')
assert correction == actual and tracker_hash == expected_hash
PY
```

Observed: `correction_count=4 actual_count=4 missing=[] extra=[]`; `tracker_hash_unchanged=True`, SHA-256 `5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc`. The correction contains every live verifier basename; the filed tracker bytes remain untouched.
