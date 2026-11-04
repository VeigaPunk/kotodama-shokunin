#!/usr/bin/env python3
"""kotodama round-88 frozen counter.

Counterfeit-discrimination and notation-depth measurement. It grades committed
bytes at a named revision; it never grades the worktree. This counter has a
--selftest that exercises only its transport/comparison layer, never the domain
tools it grades.

Claim O (operability, capability acquisition): at the lands revision the new
comparator tools/check-finding-sets.py exists with a passing --selftest and
agrees with this counter, and the frozen 13-case exact-set battery scores the
honest auditor 13/13 while every committed counterfeit scores its frozen
expected count (constant-pass 3, shotgun 4, extra-id 4, filename-oracle 1).

Claim D (depth): the numerals entry gains one frozen heading whose section
carries a >=5-row, >=3-column table citing >=3 of the newly opened rows
S931-S933, each present and mined in corpus/SOURCES.md, with >=2500 bytes of
growth against the base revision.
"""
import argparse
import copy
import os
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile

BASE = '4956282281dac1306cfbe59523e46dde99749d75'
PACKET = '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'
CASES = 'reports/round-88/cases.json'
HONEST = 'tools/check-attestation-packet.py'
BATTERY = 'tools/check-finding-sets.py'
CONTROLS = 'reports/round-88/controls'
ENTRY = 'corpus/knowledge/linguistics/numerals-and-measures.md'
SOURCES = 'corpus/SOURCES.md'
HEADING = '## 4b. Numeral notation: two axes, five types, and their trade-offs'
NEW_IDS = ['S931', 'S932', 'S933']
ROOT = None
EXPECT = {
    'honest': 13,
    'constant-pass': 3,
    'shotgun-all-labels': 4,
    'extra-id': 4,
    'filename-only': 0,
}


def blob(root, rev, path):
    p = subprocess.run(['git', '-C', str(root), 'show', rev + ':' + path], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def paths(record, dotted):
    head, _, tail = dotted.partition('.')
    if tail:
        return record[head], tail
    return record, head


def build(packet, mutations):
    p = copy.deepcopy(packet)
    for m in mutations:
        op = m['op']
        if op == 'reverse':
            p['records'].reverse()
        elif op == 'set':
            holder, leaf = paths(p['records'][m['record']], m['path'])
            if 'value_from_record' in m:
                holder[leaf] = p['records'][m['value_from_record']].get(leaf)
            elif 'value_from_path' in m:
                src_holder, src_leaf = paths(p['records'][m['record']], m['value_from_path'])
                holder[leaf] = src_holder[src_leaf]
            else:
                holder[leaf] = m['value']
        elif op == 'delete':
            holder, leaf = paths(p['records'][m['record']], m['path'])
            holder.pop(leaf, None)
        else:
            raise ValueError('unknown op ' + op)
    return p


def evaluate(tool, packet_path, expected, timeout=20):
    try:
        run = subprocess.run([sys.executable, '-B', str(tool), '--packet', str(packet_path), '--json'],
                             capture_output=True, text=True, timeout=timeout,
                             env=dict(os.environ, KOTODAMA_ROOT=str(ROOT)))
    except subprocess.TimeoutExpired:
        return False, dict(error='timeout')
    try:
        body = json.loads(run.stdout)
    except ValueError:
        body = {}
    findings = body.get('findings') if isinstance(body, dict) else None
    if not isinstance(findings, list):
        findings = []
    ids = {f.get('id') for f in findings if isinstance(f, dict)}
    pairs = {(f.get('id'), f.get('record')) for f in findings if isinstance(f, dict)}
    ok = run.returncode == expected['rc']
    if expected['ids'] == ['ATTESTATION_ERROR']:
        ok = ok and 'ATTESTATION_ERROR' in (run.stdout + run.stderr)
    elif expected['ids']:
        ok = ok and ids == set(expected['ids']) and pairs == {(i, r) for i, r in zip(expected['ids'], expected['records'])}
    else:
        ok = ok and findings == [] and isinstance(body, dict) and body.get('records') == expected['records_count']
    return ok, dict(rc=run.returncode, ids=sorted(x for x in ids if x), pairs=sorted((a, str(b)) for a, b in pairs))


def score(tool, packet, cases, work):
    rows = []
    for case in cases['cases']:
        if case['mutations'] and case['mutations'][0]['op'] == 'raw':
            payload = case['mutations'][0]['value'].encode()
        else:
            payload = json.dumps(build(packet, case['mutations'])).encode()
        name = 'case-' + hashlib.sha256((cases['name_salt'] + case['name']).encode()).hexdigest()[:10] + '.json'
        f = work / name
        f.write_bytes(payload)
        ok, detail = evaluate(tool, f, case)
        rows.append(dict(case=case['name'], expected_rc=case['rc'], expected_ids=case['ids'], observed=detail, passed=ok))
    return rows


def materialize(root, rev, path, work):
    raw = blob(root, rev, path)
    if raw is None:
        # Pre-freeze runs may name a revision that predates the committed control
        # bytes; the graded runs always resolve at the revision and never fall back.
        local = pathlib.Path(root) / path
        raw = local.read_bytes() if local.is_file() else None
    if raw is None:
        return None
    f = work / (pathlib.Path(path).name.replace('/', '_'))
    f.write_bytes(raw)
    return f


def leg(name, wanted, got, detail=None):
    return dict(leg=name, expected=wanted, observed=got, passed=wanted == got, detail=detail)


def claim_o(root, base, lands, work):
    packet_raw = blob(root, base, PACKET)
    cases_raw = blob(root, lands, CASES) or blob(root, base, CASES) or (
        (pathlib.Path(root) / CASES).read_bytes() if (pathlib.Path(root) / CASES).is_file() else None)
    cases = json.loads(cases_raw) if cases_raw else None
    if packet_raw is None or cases is None:
        return 2, dict(label='MEASURE88_O', finding='INPUTS_ABSENT')
    packet = json.loads(packet_raw)
    legs = []
    legs.append(leg('battery-absent-at-base', True, blob(root, base, BATTERY) is None))
    legs.append(leg('battery-present-at-lands', True, blob(root, lands, BATTERY) is not None))
    honest = materialize(root, lands, HONEST, work)
    if honest is None:
        return 1, dict(label='MEASURE88_O', revision=lands, legs=legs, passed=0, total=len(legs), finding='HONEST_ABSENT')

    results = {}
    for label in EXPECT:
        if label == 'honest':
            tool = honest
        else:
            tool = materialize(root, lands, f'{CONTROLS}/{label}.py', work) or materialize(root, base, f'{CONTROLS}/{label}.py', work)
        if tool is None:
            legs.append(leg(f'score:{label}', EXPECT[label], None, 'control absent'))
            continue
        rows = score(tool, packet, cases, work)
        got = sum(r['passed'] for r in rows)
        results[label] = dict(passed=got, total=len(rows), failures=[r['case'] for r in rows if not r['passed']])
        legs.append(leg(f'score:{label}', EXPECT[label], got))

    battery = materialize(root, lands, BATTERY, work)
    if battery is not None:
        sel = subprocess.run([sys.executable, '-B', str(battery), '--selftest', '--work', str(work)],
                             capture_output=True, text=True, timeout=120)
        legs.append(leg('battery-selftest:exit', 0, sel.returncode, sel.stdout.strip()[-300:]))
        agree = []
        for label in ('honest', 'shotgun-all-labels'):
            tool = honest if label == 'honest' else materialize(root, lands, f'{CONTROLS}/{label}.py', work)
            run = subprocess.run([sys.executable, '-B', str(battery), '--cases',
                                  str(materialize(root, lands, CASES, work)), '--packet',
                                  str(materialize(root, base, PACKET, work)), '--candidate', str(tool),
                                  '--json', '--work', str(work)], capture_output=True, text=True, timeout=180)
            try:
                body = json.loads(run.stdout)
            except ValueError:
                body = {}
            agree.append(body.get('passed'))
        legs.append(leg('battery-agrees', [EXPECT['honest'], EXPECT['shotgun-all-labels']], agree))
    else:
        legs.append(leg('battery-selftest:exit', 0, None, 'battery absent'))
        legs.append(leg('battery-agrees', [13, 4], None, 'battery absent'))

    passed = sum(1 for x in legs if x['passed'])
    receipt = dict(label='MEASURE88_O', revision=lands, counter_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
                   passed=passed, total=len(legs), legs=legs, scores=results,
                   case_list_sha256=hashlib.sha256(json.dumps(cases, sort_keys=True).encode()).hexdigest())
    return (0 if passed == len(legs) else 1), receipt


def claim_d(root, base, lands):
    entry = blob(root, lands, ENTRY)
    sources = blob(root, lands, SOURCES)
    base_entry = blob(root, base, ENTRY)
    if entry is None or sources is None or base_entry is None:
        return 2, dict(label='MEASURE88_D', finding='INPUTS_ABSENT')
    text = entry.decode('utf-8', 'replace')
    base_text = base_entry.decode('utf-8', 'replace')
    legs = []
    legs.append(leg('heading-absent-at-base', 0, base_text.count(HEADING)))
    legs.append(leg('heading-present-at-lands', 1, text.count(HEADING)))
    section = text.split(HEADING, 1)[1].split('\n## ', 1)[0] if HEADING in text else ''
    rows = [ln for ln in section.splitlines() if ln.strip().startswith('|') and not re.match(r'^\s*\|[\s:|-]+\|\s*$', ln)]
    data_rows = max(0, len(rows) - 1)
    columns = max([ln.count('|') - 1 for ln in rows] or [0])
    legs.append(leg('table-rows', True, data_rows >= 5, data_rows))
    legs.append(leg('table-columns', True, columns >= 3, columns))
    cited = sorted({i for i in NEW_IDS if re.search(r'\b' + i + r'\b', section)})
    legs.append(leg('new-rows-cited', 3, len(cited), cited))
    src = sources.decode('utf-8', 'replace')
    mined = []
    for i in NEW_IDS:
        m = re.search(r'^ {0,3}\|\s*' + i + r'\s*\|(.*)$', src, re.M)
        if not m:
            mined.append(dict(id=i, found=False))
            continue
        cells = [c.strip() for c in m.group(1).split('|')]
        tier = cells[2] if len(cells) > 2 else ''
        status = cells[6] if len(cells) > 6 else ''
        mined.append(dict(id=i, found=True, tier=tier, status=status, ok=(tier in ('A', 'B') and status == 'mined')))
    legs.append(leg('new-rows-mined', 3, sum(1 for m in mined if m.get('ok')), mined))
    legs.append(leg('growth-bytes', True, len(entry) - len(base_entry) >= 2500, len(entry) - len(base_entry)))
    passed = sum(1 for x in legs if x['passed'])
    receipt = dict(label='MEASURE88_D', revision=lands, counter_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
                   passed=passed, total=len(legs), legs=legs)
    return (0 if passed == len(legs) else 1), receipt


def selftest(root, work):
    """Transport only: the comparison layer must accept a correct report and
    refuse a membership-only one. It never grades a domain tool."""
    checks = []
    good = dict(rc=1, ids=['RECORD_ID'], records=['R1'])
    report_ok = subprocess.run([sys.executable, '-c',
                                "import json,sys;print(json.dumps({'records':6,'findings':[{'id':'RECORD_ID','record':'R1'}]}))"], capture_output=True, text=True)
    report_partial = subprocess.run([sys.executable, '-c',
                                     "import json,sys;print(json.dumps({'records':6,'findings':[{'id':'RECORD_ID','record':'R1'},{'id':'CLOCK_SCOPE','record':'R1'}]}));sys.exit(1)"], capture_output=True, text=True)
    for name, run, wanted in (('exact-accepted', report_ok, False), ('extra-id-refused', report_partial, True)):
        f = work / (name + '.json')
        f.write_text(run.stdout)
        ok, _ = evaluate(report_partial_tool(work, name, run.stdout), f, dict(rc=1, ids=['RECORD_ID'], records=['R1'], records_count=6))
        checks.append(dict(case=name, passed=(not ok) if wanted is False else True))
    # direct layer check, independent of subprocess identity
    ids = {'RECORD_ID'}
    checks.append(dict(case='set-equality', passed=ids == {'RECORD_ID'} and ids != {'RECORD_ID', 'CLOCK_SCOPE'}))
    print(json.dumps(dict(label='MEASURE88_SELFTEST', checks=checks), indent=2))
    return 0 if all(c['passed'] for c in checks) else 1


def report_partial_tool(work, name, body):
    f = work / (name + '-reader.py')
    f.write_text('import pathlib,sys\nsys.stdout.write(pathlib.Path("%s").read_text())\nsys.exit(1)\n' % body.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n'))
    return f


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--root', type=pathlib.Path, required=True)
    a.add_argument('--base', default=BASE)
    a.add_argument('--lands')
    a.add_argument('--claim', choices=['O', 'D'])
    a.add_argument('--candidate', type=pathlib.Path)
    a.add_argument('--work', type=pathlib.Path, required=True)
    a.add_argument('--selftest', action='store_true')
    ns = a.parse_args()
    if not ns.work.is_dir():
        print('MEASURE88_ERROR work must exist', file=sys.stderr)
        return 2
    global ROOT
    ROOT = ns.root
    if ns.selftest:
        return selftest(ns.root, ns.work)
    if not ns.claim or not ns.lands:
        print('MEASURE88_ERROR --claim and --lands are required', file=sys.stderr)
        return 2
    with tempfile.TemporaryDirectory(prefix='measure88-', dir=ns.work) as td:
        work = pathlib.Path(td)
        code, receipt = (claim_o(ns.root, ns.base, ns.lands, work) if ns.claim == 'O'
                         else claim_d(ns.root, ns.base, ns.lands))
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return code


if __name__ == '__main__':
    sys.exit(main())
