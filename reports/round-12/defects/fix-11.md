# R12-O11 bounded correction — R10 F-01

- Audit date: 2026-10-17.
- Sweep source: `reports/round-12/defects/sweep-r10.md`, finding F-01.
- Scope: append-only correction of the round-10 baseline/declaration labels. No `LOG.md` or round-8–11 artifact was changed.

## Bounded finding

The round-10 LOG entry labels `eb348f3` as the baseline, but the declared baseline is `9dc18ec1339bffd6f81e74f1a5742464ef578749`; `eb348f3ed4dfa5258be3fba15be0618a1667b962` is the separate declaration commit. This is a one-field metadata correction; the historical LOG entry remains immutable.

## Before control

The round-10 LOG section was compared to the claim declaration and both commit objects with this command at `2026-10-17T20:07:25-03:00`:

```sh
date -Is; python3 - <<'PY'
import hashlib, json, re, subprocess
from pathlib import Path
claims = json.loads(Path('reports/round-10/claims.json').read_text(encoding='utf-8'))
declared = claims['baseline_revision']
declaration = 'eb348f3ed4dfa5258be3fba15be0618a1667b962'
log = Path('LOG.md').read_text(encoding='utf-8')
section = log.split('## 2026-10-17 — Round 10 admitted', 1)[1].split('\n## ', 1)[0]
match = re.search(r'\bbaseline `([^`]+)`', section)
assert match
logged = match.group(1)
print(f'log_baseline={logged} declared_baseline={declared} match={logged == declared or declared.startswith(logged)}')
print(f'logged_value_is_declaration_prefix={declaration.startswith(logged)}')
for label, rev in [('declared_baseline', declared), ('declaration_commit', declaration)]:
    print(f'{label}_object={subprocess.check_output(["git", "show", "-s", "--format=%H %s", rev], text=True).strip()}')
print(f'log_sha256={hashlib.sha256(Path("LOG.md").read_bytes()).hexdigest()}')
PY
```

Observed: `log_baseline=eb348f3 declared_baseline=9dc18ec1339bffd6f81e74f1a5742464ef578749 match=False`; the logged short value is a prefix of the declaration commit, not the declared baseline. Both full commit objects resolve. The pre-correction LOG digest was `5864c5d8771c485d923b7013203770fce8e433106c09e0365aa4cc02c348f277`.

## Append-only correction

Correct metadata for a round-10 report reference:

```json
{
  "round": 10,
  "baseline_revision": "9dc18ec1339bffd6f81e74f1a5742464ef578749",
  "declaration_commit": "eb348f3ed4dfa5258be3fba15be0618a1667b962"
}
```

**Disposition: fixed-with-control (append-only correction).** This fragment supplies the distinct labels without rewriting the historical LOG entry.

## After control

Command run at `2026-10-17T20:07:45-03:00` (immediately preceded by `date -Is`):

```sh
date -Is; python3 - <<'PY'
import hashlib, json, subprocess
from pathlib import Path
text = Path('reports/round-12/defects/fix-11.md').read_text(encoding='utf-8')
blocks = []
in_json = False
json_lines = []
for line in text.splitlines():
    if line == "```json":
        in_json = True
        json_lines = []
    elif in_json and line == "```":
        blocks.append(chr(10).join(json_lines))
        in_json = False
    elif in_json:
        json_lines.append(line)
assert len(blocks) == 1
correction = json.loads(blocks[0])
claims = json.loads(Path('reports/round-10/claims.json').read_text(encoding='utf-8'))
expected_log_hash = '5864c5d8771c485d923b7013203770fce8e433106c09e0365aa4cc02c348f277'
log_hash = hashlib.sha256(Path('LOG.md').read_bytes()).hexdigest()
objects_resolve = all(subprocess.run(['git', 'cat-file', '-e', f'{revision}^{{commit}}']).returncode == 0 for revision in (correction['baseline_revision'], correction['declaration_commit']))
print(f'correction_matches_claim={correction["baseline_revision"] == claims["baseline_revision"]} declaration_separated={correction["declaration_commit"] != correction["baseline_revision"]} commit_objects_resolve={objects_resolve}')
print(f'log_unchanged={log_hash == expected_log_hash} sha256={log_hash}')
assert correction['baseline_revision'] == claims['baseline_revision'] and correction['declaration_commit'] != correction['baseline_revision'] and objects_resolve and log_hash == expected_log_hash
PY
```

Observed: `correction_matches_claim=True declaration_separated=True commit_objects_resolve=True`; `log_unchanged=True`, SHA-256 `5864c5d8771c485d923b7013203770fce8e433106c09e0365aa4cc02c348f277`.
