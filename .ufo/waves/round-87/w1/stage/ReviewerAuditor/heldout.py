#!/usr/bin/env python3
"""Bounded author-side CLI probes; expectations independent of candidate."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
BASE = '83846a22ee1e9da7aa52ac505ccebf4455169247'
PACKET = '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'
STAGE = Path(__file__).parent
WORK = Path('/fast/scratch/hyaku/kotodama-r87/ReviewerAuditor')
raw = subprocess.run(['git', '-C', ROOT, 'show', BASE + ':' + PACKET], check=True, capture_output=True).stdout
baseline = json.loads(raw)
cases = []
def add(name, mutate, rc, count=None, finding=None, basis='frozen contract'):
    packet = copy.deepcopy(baseline)
    mutate(packet)
    cases.append((name, json.dumps(packet), rc, count, finding, basis))
add('reverse-record-order', lambda p: p['records'].reverse(), 0, 6)
add('single-record-count', lambda p: p.update(records=p['records'][:1]), 0, 1, basis='held-out non-fixed count')
add('seven-record-count', lambda p: p['records'].append(dict(p['records'][0], id='HELDOUT-07')), 0, 7, basis='held-out non-fixed count')
add('null-known-date', lambda p: p['records'][0]['attestation'].update(value=None), 0, 6)
add('null-clock-object', lambda p: p['records'][0].update(origin=None), 1, finding='CLOCK_MISSING')
add('array-clock-object', lambda p: p['records'][0].update(origin=[]), 1, finding='CLOCK_MISSING')
add('number-clock-date', lambda p: p['records'][0]['origin'].update(value=1700), 1, finding='CLOCK_DATE')
add('boolean-clock-date', lambda p: p['records'][0]['origin'].update(value=True), 1, finding='CLOCK_DATE')
add('object-clock-date', lambda p: p['records'][0]['origin'].update(value={}), 1, finding='CLOCK_DATE')
add('null-clock-reason', lambda p: p['records'][0]['origin'].update(reason=None), 1, finding='CLOCK_REASON')
add('array-clock-reason', lambda p: p['records'][0]['origin'].update(reason=[]), 1, finding='CLOCK_REASON')
add('unicode-blank-reason', lambda p: p['records'][0]['origin'].update(reason='\u2003\t\n'), 1, finding='CLOCK_REASON')
add('missing-clock-value', lambda p: p['records'][0]['origin'].pop('value'), 1, finding='CLOCK_MISSING', basis='held-out unknown must be explicit')
add('blank-record-id', lambda p: p['records'][0].update(id='  '), 1, finding='RECORD_ID')
add('duplicate-after-reorder', lambda p: (p['records'].reverse(), p['records'][1].update(id=p['records'][0]['id'])), 1, finding='RECORD_ID')
add('null-record-field', lambda p: p['records'][0].update(sense=None), 1, finding='RECORD_FIELD')
add('translation-one-day-early', lambda p: p['records'][5]['attestation'].update(value='1889-12-31'), 1, finding='TRANSLATION_CLOCK')
add('translation-equal-day', lambda p: p['records'][5]['attestation'].update(value='1890-01-01'), 0, 6)
add('translation-later-day', lambda p: p['records'][5]['attestation'].update(value='1890-01-02'), 0, 6)
add('translation-unknown-attestation', lambda p: p['records'][5]['attestation'].update(value=None), 0, 6)
add('invalid-translation-date', lambda p: p['records'][5]['translation'].update(translation_date='1890-02-30'), 1, finding='CLOCK_DATE')
add('array-solutions', lambda p: p['records'][3].update(solutions=[]), 2, finding='ATTESTATION_ERROR', basis='held-out malformed nested relationship')
add('array-editorial', lambda p: p['records'][4].update(editorial=[]), 2, finding='ATTESTATION_ERROR', basis='held-out malformed nested relationship')
add('array-translation', lambda p: p['records'][5].update(translation=[]), 2, finding='ATTESTATION_ERROR', basis='held-out malformed nested relationship')
text = json.dumps(baseline)
cases.append(('duplicate-json-key', text.replace('"schema_version": 1', '"schema_version": 1, "schema_version": 2', 1), 2, None, 'ATTESTATION_ERROR', 'held-out ambiguous JSON object'))
cases.append(('top-level-null', 'null', 2, None, 'ATTESTATION_ERROR', 'malformed input'))
manifest = [dict(name=n, expected_rc=rc, expected_records=count, expected_finding=finding, basis=basis) for n, _, rc, count, finding, basis in cases]
(STAGE / 'heldout-expectations.json').write_text(json.dumps(manifest, indent=2) + '\n')
if len(sys.argv) != 2:
    sys.exit('usage: heldout.py ABSOLUTE_CANDIDATE_PATH')
candidate = Path(sys.argv[1]).resolve()
rows = []
for name, text, rc, count, finding, basis in cases:
    packet = WORK / (name + '.json')
    packet.write_text(text)
    result = subprocess.run([sys.executable, '-B', str(candidate), '--packet', str(packet), '--json'], capture_output=True, text=True, timeout=15, cwd=WORK)
    try:
        body = json.loads(result.stdout)
    except ValueError:
        body = None
    ids = [x.get('id') for x in body.get('findings', []) if isinstance(x, dict)] if isinstance(body, dict) else []
    passed = result.returncode == rc
    if finding == 'ATTESTATION_ERROR':
        passed = passed and finding in result.stdout + result.stderr
    elif finding:
        passed = passed and finding in ids
    else:
        passed = passed and isinstance(body, dict) and body.get('records') == count and body.get('findings') == []
    rows.append(dict(name=name, expected_rc=rc, expected_records=count, expected_finding=finding, basis=basis, actual_rc=result.returncode, stdout=result.stdout, stderr=result.stderr, matched=passed))
    (STAGE / 'packets').mkdir(exist_ok=True)
    (STAGE / 'packets' / packet.name).write_text(text)
receipt = dict(candidate=str(candidate), candidate_sha256=hashlib.sha256(candidate.read_bytes()).hexdigest(), baseline_sha256=hashlib.sha256(raw).hexdigest(), total=len(rows), matched=sum(r['matched'] for r in rows), rows=rows)
(STAGE / 'heldout-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(dict(total=receipt['total'], matched=receipt['matched'], mismatches=[r['name'] for r in rows if not r['matched']])))
