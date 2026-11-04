#!/usr/bin/env python3
"""Frozen finite public-CLI discrimination battery; not a truth/semantic oracle."""
import argparse
import copy
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

PACKET = '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'
TOOL = 'tools/check-attestation-packet.py'
BASE = '83846a22ee1e9da7aa52ac505ccebf4455169247'

def blob(root, rev, path):
    p = subprocess.run(['git', '-C', str(root), 'show', rev + ':' + path], capture_output=True)
    return p.stdout if p.returncode == 0 else None

def cases(packet):
    out = [('positive-six', copy.deepcopy(packet), 0, None)]
    def add(name, code, label, change):
        p = copy.deepcopy(packet)
        change(p)
        out.append((name, p, code, label))
    add('duplicate-record', 1, 'RECORD_ID', lambda p: p['records'][1].update(id=p['records'][0]['id']))
    add('missing-clock', 1, 'CLOCK_MISSING', lambda p: p['records'][0].pop('origin'))
    add('blank-reason', 1, 'CLOCK_REASON', lambda p: p['records'][0]['origin'].update(reason='  '))
    add('invalid-date', 1, 'CLOCK_DATE', lambda p: p['records'][0]['attestation'].update(value='1710-02-30'))
    add('blank-sense', 1, 'RECORD_FIELD', lambda p: p['records'][0].update(sense=' '))
    add('unresolved-selected', 1, 'SOLUTION_CONFLICT', lambda p: p['records'][3]['solutions'].update(selected='boat'))
    add('conjecture-promoted', 1, 'EDITORIAL_CONFLICT', lambda p: p['records'][4].update(wording=p['records'][4]['editorial']['conjectured_wording']))
    add('translation-backdated', 1, 'TRANSLATION_CLOCK', lambda p: p['records'][5]['attestation'].update(value=p['records'][5]['translation']['source_attestation']))
    add('unknown-explicit', 0, None, lambda p: p['records'][0]['attestation'].update(value=None, reason='Unknown in this exercise.'))
    add('reordered-records', 0, None, lambda p: p['records'].reverse())
    out.append(('invalid-json', b'{broken', 2, 'ATTESTATION_ERROR'))
    return out

def evaluate(tool, packet, work):
    rows = []
    for name, value, expected_rc, expected_id in cases(packet):
        f = work / (name + '.json')
        f.write_bytes(value if isinstance(value, bytes) else json.dumps(value).encode())
        try:
            p = subprocess.run([sys.executable, '-B', str(tool), '--packet', str(f), '--json'], capture_output=True, text=True, timeout=15)
            try:
                body = json.loads(p.stdout)
            except ValueError:
                body = {}
            ids = [x.get('id') for x in body.get('findings', []) if isinstance(x, dict)] if isinstance(body, dict) else []
            passed = p.returncode == expected_rc
            if expected_id == 'ATTESTATION_ERROR':
                passed = passed and expected_id in (p.stdout + p.stderr)
            elif expected_id:
                passed = passed and expected_id in ids
            else:
                passed = passed and isinstance(body, dict) and body.get('records') == 6 and body.get('findings') == []
            rows.append(dict(case=name, expected_rc=expected_rc, expected_id=expected_id, rc=p.returncode, stdout=p.stdout, stderr=p.stderr, passed=passed))
        except subprocess.TimeoutExpired:
            rows.append(dict(case=name, expected_rc=expected_rc, expected_id=expected_id, rc=None, passed=False, error='timeout'))
    return rows

def main():
    a = argparse.ArgumentParser()
    a.add_argument('--root', type=pathlib.Path, required=True)
    a.add_argument('--revision', required=True)
    a.add_argument('--candidate', type=pathlib.Path)
    a.add_argument('--work', type=pathlib.Path, required=True)
    a.add_argument('--selftest', action='store_true')
    ns = a.parse_args()
    if not ns.work.is_dir():
        print('MEASURE87_ERROR work must exist', file=sys.stderr)
        return 2
    packet_raw = blob(ns.root, BASE, PACKET)
    if not packet_raw:
        print('MEASURE87_ERROR baseline packet unavailable', file=sys.stderr)
        return 2
    packet = json.loads(packet_raw)
    with tempfile.TemporaryDirectory(prefix='measure87-', dir=ns.work) as td:
        work = pathlib.Path(td)
        if ns.selftest:
            # Transport-only oracle: fixture filenames encode independent expectations.
            # This tests the battery's subprocess/exit/JSON comparison, never the domain tool.
            expected = {n: (rc, label) for n, _, rc, label in cases(packet)}
            oracle = "import pathlib,json,sys\nm=" + repr(expected) + "\nn=pathlib.Path(sys.argv[sys.argv.index('--packet')+1]).stem\nrc,label=m[n]\nprint(json.dumps({'records':6,'findings':[] if label is None else [{'id':label}]}))\nsys.exit(rc)\n"
            checks = []
            for name, source, wanted in (
                ('clean-transport', oracle, 12),
                ('constant-pass', "import json\nprint(json.dumps({'records':6,'findings':[]}))\n", 3),
                ('constant-reject', "import json,sys\nprint(json.dumps({'records':6,'findings':[{'id':'RECORD_ID'}]}))\nsys.exit(1)\n", 1),
                ('non-json', "print('not json')\n", 0),
            ):
                tool = work / (name + '.py')
                tool.write_text(source)
                rows = evaluate(tool, packet, work)
                got = sum(r['passed'] for r in rows)
                checks.append(dict(case=name, expected_passed=wanted, observed_passed=got, passed=got == wanted))
            print(json.dumps(dict(label='MEASURE87_SELFTEST', checks=checks), indent=2))
            return 0 if all(c['passed'] for c in checks) else 1
        raw = ns.candidate.read_bytes() if ns.candidate else blob(ns.root, ns.revision, TOOL)
        if raw is None:
            print(json.dumps(dict(label='MEASURE87', revision=ns.revision, passed=0, total=12, finding='TOOL_ABSENT')))
            return 1
        tool = work / 'candidate.py'
        tool.write_bytes(raw)
        rows = evaluate(tool, packet, work)
        passed = sum(r['passed'] for r in rows)
        receipt = dict(label='MEASURE87', revision=ns.revision, candidate_sha256=hashlib.sha256(raw).hexdigest(), counter_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(), baseline_packet_sha256=hashlib.sha256(packet_raw).hexdigest(), passed=passed, total=len(rows), cases=rows)
        print(json.dumps(receipt, indent=2))
        return 0 if passed == len(rows) else 1

if __name__ == '__main__':
    sys.exit(main())
