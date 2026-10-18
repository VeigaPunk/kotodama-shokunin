# R14-O03 — tracker verifier-pointer correction

- Axis: O / operability.
- Date: 2026-10-17.
- Routed item: R10-SWEEP F-04 in `reports/round-12/defects/routed.md:58-64`.
- Disposition: **applied-with-control**; the appended tracker entry records `fixed-with-control`.
- Source payload: `reports/round-12/defects/fix-09.md:35-50`.

## Applied correction and limits

Appended the new top-level `errata` key to `reports/round-10/findings-tracker.json:388-414`. Entry `R14-O03` identifies `final_state.verify_files` as its correction target and carries fix-09's exact `final_state.verify_files` payload, including `findings-verify-3.md`.

The original `final_state.verify_files` at `reports/round-10/findings-tracker.json:381-385` remains the historical list, not the effective corrected list. The effective list is `errata[0].final_state.verify_files` at lines 397-402. Consumers of this correction must resolve the erratum; no filed runner or receipt was edited or executed.

The only insertion into the filed tracker is the trailing `errata` member and its JSON separator. No original finding row, original metadata value, or historical disposition was rewritten. Removing that insertion reconstructs every original tracker byte, including its whitespace. The round-12 source correction is unchanged against the fixed baseline revision.

## Before and after evidence

The pre-edit probe ran at `2026-10-17T23:57:31Z`: the live tracker was byte-identical to `git show a7bc9e9ff05a57515c5efaaa7e50116eb30938ff:reports/round-10/findings-tracker.json`. Its SHA-256 was `5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc`.

The complete reproducible control below ran at `2026-10-17T23:58:18Z` and exited 0. All counts below are from this dated command. Row hashing covers the **raw UTF-8 bytes of the entire findings array**, including row formatting, rather than a normalized JSON serialization. The baseline revision is fixed so later integration commits cannot change the before-side comparison.

```sh
export TMPDIR=$PWD/.scratch
date -u +%Y-%m-%dT%H:%M:%SZ
python3 - <<'PY'
import copy
import hashlib
import json
from pathlib import Path
import subprocess

revision = 'a7bc9e9ff05a57515c5efaaa7e50116eb30938ff'
path = 'reports/round-10/findings-tracker.json'
source = 'reports/round-12/defects/fix-09.md'
before = subprocess.check_output(['git', 'show', f'{revision}:{path}'])
after = Path(path).read_bytes()
filed = json.loads(before)
tracker = json.loads(after)
blocks, lines, in_json = [], [], False
for line in Path(source).read_text(encoding='utf-8').splitlines():
    if line == '```json':
        assert not in_json
        in_json, lines = True, []
    elif in_json and line == '```':
        blocks.append('\n'.join(lines))
        in_json = False
    elif in_json:
        lines.append(line)
assert not in_json and len(blocks) == 1
correction = json.loads(blocks[0])['final_state']['verify_files']
actual = sorted(p.name for p in Path('reports/round-10').glob('findings-verify-*.md'))

def rows_bytes(raw):
    text = raw.decode('utf-8')
    start = text.index('  "findings": ') + len('  "findings": ')
    _, end = json.JSONDecoder().raw_decode(text, start)
    return text[start:end].encode('utf-8')

def check_preservation(raw):
    prefix, payload = raw.split(b',\n  "errata": ', 1)
    payload = payload.decode('utf-8')
    _, end = json.JSONDecoder().raw_decode(payload)
    assert prefix + payload[end:].encode('utf-8') == before, 'filed bytes changed'
    assert rows_bytes(raw) == rows_bytes(before), 'original rows changed'
    assert {k: v for k, v in json.loads(raw).items() if k != 'errata'} == filed

def check_pointer(document):
    entries = [e for e in document['errata'] if e['id'] == 'R14-O03']
    assert len(entries) == 1
    entry = entries[0]
    assert entry['corrects'] == 'final_state.verify_files'
    assert entry['source'] == source
    assert entry['final_state']['verify_files'] == correction == actual
    assert entry['control']['original_rows_sha256_before'] == hashlib.sha256(rows_bytes(before)).hexdigest()
    assert entry['control']['original_rows_sha256_after'] == hashlib.sha256(rows_bytes(after)).hexdigest()

check_preservation(after)
check_pointer(tracker)
assert filed['final_state']['verify_files'] != actual
assert Path(source).read_bytes() == subprocess.check_output(['git', 'show', f'{revision}:{source}'])
negative_controls = []
bad = copy.deepcopy(tracker)
bad['errata'][0]['final_state']['verify_files'].remove('findings-verify-3.md')
try:
    check_pointer(bad)
except AssertionError:
    negative_controls.append('omitted_verifier_rejected')
else:
    raise AssertionError('missing-verifier control did not fail')
bad = copy.deepcopy(tracker)
bad['errata'][0]['final_state']['verify_files'].append('findings-verify-99.md')
try:
    check_pointer(bad)
except AssertionError:
    negative_controls.append('nonexistent_verifier_rejected')
else:
    raise AssertionError('extra-verifier control did not fail')
try:
    check_preservation(after.replace(b'"idx": 0,', b'"idx": 99,', 1))
except AssertionError:
    negative_controls.append('filed_row_mutation_rejected')
else:
    raise AssertionError('row-mutation control did not fail')
print(json.dumps({
    'filed_revision': revision,
    'tracker_sha256_before': hashlib.sha256(before).hexdigest(),
    'tracker_sha256_after': hashlib.sha256(after).hexdigest(),
    'original_rows_count': len(tracker['findings']),
    'original_rows_bytes': len(rows_bytes(after)),
    'original_rows_sha256_before': hashlib.sha256(rows_bytes(before)).hexdigest(),
    'original_rows_sha256_after': hashlib.sha256(rows_bytes(after)).hexdigest(),
    'original_rows_byte_identical': True,
    'all_original_bytes_reconstructed_exactly': True,
    'original_fields_unchanged': True,
    'filed_verifier_count': len(filed['final_state']['verify_files']),
    'effective_verifier_count': len(correction),
    'actual_verifier_count': len(actual),
    'effective_verify_files': tracker['errata'][0]['final_state']['verify_files'],
    'missing': sorted(set(actual) - set(correction)),
    'extra': sorted(set(correction) - set(actual)),
    'source_correction_unchanged': True,
    'negative_controls_passed': negative_controls,
    'status': 'PASS'
}, indent=2))
PY
```

Observed output:

```json
{
  "filed_revision": "a7bc9e9ff05a57515c5efaaa7e50116eb30938ff",
  "tracker_sha256_before": "5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc",
  "tracker_sha256_after": "4b983ae9237dda1b46fba59fac2ce8731a1a924ae9672925757bcc4ebc30def2",
  "original_rows_count": 24,
  "original_rows_bytes": 34978,
  "original_rows_sha256_before": "e61727782a4cd57475fb9fb72ffaf2e503443c93206c6f7f017c1468d7c74d9c",
  "original_rows_sha256_after": "e61727782a4cd57475fb9fb72ffaf2e503443c93206c6f7f017c1468d7c74d9c",
  "original_rows_byte_identical": true,
  "all_original_bytes_reconstructed_exactly": true,
  "original_fields_unchanged": true,
  "filed_verifier_count": 3,
  "effective_verifier_count": 4,
  "actual_verifier_count": 4,
  "effective_verify_files": [
    "findings-verify-1.md",
    "findings-verify-2.md",
    "findings-verify-3.md",
    "findings-verify-4.md"
  ],
  "missing": [],
  "extra": [],
  "source_correction_unchanged": true,
  "negative_controls_passed": [
    "omitted_verifier_rejected",
    "nonexistent_verifier_rejected",
    "filed_row_mutation_rejected"
  ],
  "status": "PASS"
}
```

`git diff --check -- reports/round-10/findings-tracker.json` also exited 0 on 2026-10-17. This worker did not run historical round validators, change shared bookkeeping, or claim the round-wide regression result; those remain the integrator's assigned controls.
