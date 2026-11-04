#!/usr/bin/env python3
"""Reproduce round88 measurements at one committed revision, not the live tree."""
import argparse
from collections import Counter
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

P = argparse.ArgumentParser()
P.add_argument('--lands', required=True)
P.add_argument('--out', type=pathlib.Path, required=True)
P.add_argument('--work', type=pathlib.Path, required=True)
a = P.parse_args()
root = pathlib.Path(__file__).resolve().parents[2]
base = '4956282281dac1306cfbe59523e46dde99749d75'
freeze = '4b76524c51e1c2f76c99eeb3b629cfac08a44a76'
a.out.mkdir(parents=True, exist_ok=True)

def blob(rev, path):
    return subprocess.check_output(['git', '-C', str(root), 'show', rev + ':' + path])

def registry(rev):
    rows = {}
    for line in blob(rev, 'corpus/SOURCES.md').decode().splitlines():
        if re.match(r'^ {0,3}\|\s*S[0-9]{3,}\s*\|', line):
            cells = [s.strip() for s in line.strip().strip('|').split('|')]
            rows[cells[0]] = (line, cells)
    return rows

before, after = registry(base), registry(a.lands)
counts = lambda rows: {'rows': len(rows), 'tiers': dict(Counter(v[1][3] for v in rows.values())), 'status': dict(Counter(v[1][7] for v in rows.values()))}
(a.out / 'registry-counts.json').write_text(json.dumps({'base': base, 'lands': a.lands, 'before': counts(before), 'after': counts(after), 'old_rows_changed': [k for k in before if k not in after or before[k][0] != after[k][0]], 'added': sorted(set(after) - set(before))}, indent=2) + '\n')
changed = subprocess.check_output(['git', '-C', str(root), 'diff', '--name-only', base, a.lands, '--', 'PROVINCE.md', 'corpus/knowledge'], text=True).splitlines()
pins = {p: {'freeze': hashlib.sha256(blob(freeze, p)).hexdigest(), 'lands': hashlib.sha256(blob(a.lands, p)).hexdigest()} for p in ['reports/round-88/measure88.py', 'reports/round-88/claims.json', 'reports/round-88/cases.json', 'tools/check-attestation-packet.py']}
(a.out / 'noharm.json').write_text(json.dumps({'base': base, 'lands': a.lands, 'changed_knowledge_or_province': changed, 'pins': pins, 'old_registry_rows_unchanged': all(k in after and v[0] == after[k][0] for k, v in before.items()), 'bound': 'Path/byte preservation, not universal semantic no-harm.'}, indent=2) + '\n')
receipts = {}
with tempfile.TemporaryDirectory(prefix='r88-final-', dir=a.work) as tmp:
    work = pathlib.Path(tmp)
    clone = work / 'repo'
    subprocess.run(['git', 'clone', '--shared', '--no-checkout', str(root), str(clone)], check=True, capture_output=True)
    subprocess.run(['git', '-C', str(clone), 'checkout', '--detach', a.lands], check=True, capture_output=True)
    counter = work / 'measure88-frozen.py'
    counter.write_bytes(blob(freeze, 'reports/round-88/measure88.py'))
    env = dict(os.environ, KOTODAMA_ROOT=str(clone), PYTHONDONTWRITEBYTECODE='1', TMPDIR=str(work))
    def run(label, args):
        command = ['python3', '-B'] + args
        p = subprocess.run(command, cwd=clone, env=env, capture_output=True, text=True, timeout=600)
        receipt = {'revision': a.lands, 'tree': subprocess.check_output(['git', '-C', str(clone), 'rev-parse', a.lands + '^{tree}'], text=True).strip(), 'command': command, 'environment': {'KOTODAMA_ROOT': 'caller-owned shared clone checked out at revision'}, 'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
        try: receipt['body'] = json.loads(p.stdout)
        except ValueError: pass
        receipts[label] = receipt
        (a.out / (label + '.json')).write_text(json.dumps(receipt, indent=2) + '\n')
    for claim in ['O', 'D']:
        run('lands-' + claim.lower(), [str(counter), '--root', str(clone), '--base', base, '--lands', a.lands, '--claim', claim, '--work', str(work)])
    run('declared-d-missing-work', [str(counter), '--root', '.', '--base', base, '--lands', a.lands, '--claim', 'D'])
    run('tool-selftest', ['tools/check-finding-sets.py', '--selftest', '--work', str(work)])
    for label in ['honest', 'constant-pass', 'shotgun-all-labels', 'extra-id', 'filename-only']:
        candidate = 'tools/check-attestation-packet.py' if label == 'honest' else 'reports/round-88/controls/' + label + '.py'
        run('direct-' + label, ['tools/check-finding-sets.py', '--cases', 'reports/round-88/cases.json', '--packet', '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json', '--candidate', candidate, '--json', '--work', str(work)])
    run('index', ['tools/check-corpus-index.py', '--root', '.'])
    run('registry', ['tools/check-gate-registry.py', '--root', '.'])
    run('cited-lines', ['tools/check-cited-lines.py', 'corpus/knowledge/linguistics/numerals-and-measures.md'])
    run('current-cited-records', ['tools/check-cited-records.py', '--root', '.', '--from-round', '88', '--bind-round', '88'])
print(json.dumps({key: {'rc': val['rc'], 'passed': val.get('body', {}).get('passed'), 'total': val.get('body', {}).get('total'), 'output': val['stdout'][-180:]} for key, val in receipts.items()}, indent=2))
