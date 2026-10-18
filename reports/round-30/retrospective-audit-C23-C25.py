#!/usr/bin/env python3
import argparse
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = '87bfc9956f0fc60e6821fe53b622d0043e28be10'


def load(path):
    return json.loads((ROOT / path).read_text())


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def revision_exists(rev):
    return subprocess.run(['git', 'cat-file', '-e', rev + '^{commit}'], cwd=ROOT,
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def locator_exists(path, first=None, last=None):
    p = ROOT / path
    if not p.exists():
        return False
    if first is None:
        return True
    return p.is_file() and 1 <= first <= (last or first) <= len(p.read_text().splitlines())


def key_exists(path, keys):
    try:
        value = load(path)
        for key in keys:
            value = value[key]
        return True
    except (OSError, ValueError, KeyError, TypeError, IndexError):
        return False


def heading_exists(path, heading):
    return any(line.lstrip('#').strip() == heading
               for line in (ROOT / path).read_text().splitlines() if line.startswith('#'))


def controls():
    p = 'reports/round-29/validation.json'
    good = {
        'real_file': locator_exists(p),
        'missing_file_rejected': not locator_exists('reports/round-30/__C23_missing__.json'),
        'real_line': locator_exists(p, 2),
        'out_of_range_rejected': not locator_exists(p, 999999),
        'backwards_range_rejected': not locator_exists(p, 20, 10),
        'real_key': key_exists(p, ['claims', 'C', 'result', 'law_clean_calibration']),
        'missing_key_rejected': not key_exists(p, ['claims', '__C23_missing__']),
        'real_heading': heading_exists('reports/round-29/recount/audit.md', 'Independent command results'),
        'missing_heading_rejected': not heading_exists('reports/round-29/recount/audit.md', '__C23_missing__'),
        'real_revision': revision_exists(BASE),
        'missing_revision_rejected': not revision_exists('0' * 40),
    }
    raw = (ROOT / p).read_bytes()
    good['altered_bytes_rejected'] = sha256(raw).digest() != sha256(raw + b'\n').digest()
    assert all(good.values()), good
    return good


def numbers():
    receipts = {n: load(f'reports/round-{n}/validation.json') for n in range(8, 30)
                if (ROOT / f'reports/round-{n}/validation.json').is_file()}
    assert len(receipts) == 20
    receipt_bindings = {}
    for n, value in receipts.items():
        path = f'reports/round-{n}/validation.json'
        raw = (ROOT / path).read_bytes()
        assert raw == git('show', f'{BASE}:{path}'), path
        receipt_bindings[str(n)] = sha256(raw).hexdigest()
    log = (ROOT / 'LOG.md').read_text()
    assert '**Round 13 status:** operator-skipped before any work landed' in log
    assert '## 2026-10-18 — Round 22 REJECTED on claim D' in log
    assert not (ROOT / 'reports/round-22/validation.json').exists()
    states = {n: ('admitted' if value['acceptance_checks_passed'] else 'rejected')
              for n, value in receipts.items()}
    states.update({13: 'operator-skipped', 22: 'rejected'})
    assert sorted(n for n, state in states.items() if state == 'rejected') == [11, 17, 22]
    assert Counter(states.values()) == {'admitted': 18, 'rejected': 3, 'operator-skipped': 1}
    loops = {str(i): dict(Counter(state for n, state in states.items() if low <= n <= high))
             for i, low, high in [(1, 8, 16), (2, 17, 24), (3, 25, 29)]}
    assert loops == {'1': {'admitted': 7, 'rejected': 1, 'operator-skipped': 1},
                     '2': {'admitted': 6, 'rejected': 2}, '3': {'admitted': 5}}
    flags = Counter(str(flag['passed']).lower() for v in receipts.values() for flag in v['claims'].values())
    assert flags == {'true': 55, 'false': 2}
    loop3_flags = Counter(str(flag['passed']).lower() for n, v in receipts.items() if n >= 25
                          for flag in v['claims'].values())
    assert loop3_flags == {'true': 15}
    recounts = {}
    for n, expected in [(12, {'match': 12, 'disposition': 77}),
                        (21, {'match': 39, 'disposition': 24}),
                        (29, {'match': 9, 'disposition': 16, 'coverage-limit': 1})]:
        rows = load(f'reports/round-{n}/recount/ledger.json')
        counts = dict(Counter(row['verdict'] for row in rows))
        assert counts == expected
        recounts[str(n)] = {'rows': len(rows), 'verdicts': counts}
    queue = load('reports/round-29/defects/ledger.json')['entries']
    assert len(queue) == len({row['id'] for row in queue}) == 24
    status = dict(Counter(row['status'] for row in queue))
    classes = dict(Counter(row['classification'] for row in queue))
    assert status == {'closed': 3, 'superseded': 2, 'open': 16, 'observation': 3}
    assert classes == {'conformance': 14, 'process': 9, 'bookkeeping': 1}
    availability = {}
    for n in range(25, 29):
        a = load(f'reports/round-{n}/availability.json')
        assert a['route'] == 'devin/deepseek-v4-1-flash-high'
        assert a['requested_workers'] == 64
        assert a['launched_workers'] is None and a['completed_workers'] is None
        availability[str(n)] = {key: a[key] for key in ('route', 'requested_workers', 'launched_workers', 'completed_workers')}
    completions = {}
    for n in range(25, 30):
        section = re.search(rf'^## [^\n]*Round {n} admitted[^\n]*\n(.*?)(?=^## |\Z)', log, re.M | re.S)
        match = re.search(r'(\d+)/64 completed', section.group(1))
        completions[str(n)] = int(match[1])
    assert list(completions.values()) == [26, 24, 24, 24, 17]
    requests = sum(load(f'reports/round-{n}/claims.json')['workers'] for n in range(8, 30) if n != 13)
    assert requests == 1088
    routed = re.findall(r'\((\d+)\)', next(c['before'] for c in load('reports/round-30/claims.json')['claims'] if c['id'] == 'O'))
    assert routed == ['1', '2', '3', '4', '5']
    frows = [json.loads(p.read_text()) for p in (ROOT / 'reports/round-11/recheck').glob('row-*.json')]
    comparable = sum(bool(re.fullmatch(r'[0-9a-f]{64}', row.get('new_hash') or '')) for row in frows)
    stable = sum(row['stable'] is True for row in frows)
    assert (len(frows), comparable, stable) == (192, 189, 147)
    f11 = receipts[11]['claims']['F']
    assert f11['passed'] is False and stable / comparable < .95 and stable / len(frows) < .95
    d26 = receipts[26]['claims']['D']['measurement']['independent_replay']
    pairs = d26['rows']
    assert len(pairs) == d26['pairs'] == d26['agreeing'] == 8
    for row in pairs:
        if row['operation'] == 'reverse':
            result = row['base'][::-1]
        elif row['operation'] == 'lengthen':
            result = re.sub(r'[aeiou]', lambda m: m[0] * 2, row['base'], count=1)
        else:
            raise AssertionError(row)
        assert result == row['term'] == row['replayed']
    law = receipts[29]['claims']['C']['result']['law_clean_calibration']
    assert (law['design_reference']['expected_findings'], law['observed_findings'], law['exit_code']) == (6, 4, 1)
    assert len(law['finding_lines']) == 4 and all('D4L-LAW-DANGLING' in line for line in law['finding_lines'])
    revisions = ['51e5901', '9437788', '3dba77a', 'eb4295c']
    amendments = [git('show', '-s', '--format=%H %cI %s', rev).decode().strip() for rev in revisions]
    full_sweep = load('reports/round-29/recount/r27-full-sweep-reproduction.json')
    assert full_sweep['summary'] == {'exit': 1, 'findings': 31, 'surfaces_enumerated': 117}
    assert len(full_sweep['findings']) == full_sweep['summary']['findings']
    negative = {
        'r11_not_readmitted': states[11] != 'admitted',
        'r17_not_readmitted': states[17] != 'admitted',
        'r22_not_readmitted': states[22] != 'admitted',
        'r22_missing_receipt_not_counted': 22 not in receipts,
        'dispositions_not_exact_matches': recounts['29']['verdicts']['match'] != recounts['29']['rows'],
        'four_not_six_findings': law['observed_findings'] != law['design_reference']['expected_findings'],
        'completion_not_in_availability': all(a['completed_workers'] is None for a in availability.values()),
        'denominator_192_not_0778': round(stable / len(frows), 3) != .778,
        'r30_worklist_not_all_open_defects': len(routed) != status['open'],
    }
    assert all(negative.values()), negative
    return {'closed_round_states_8_29': states, 'loop_state_counts': loops,
            'receipt_count': len(receipts), 'receipt_claim_flags': dict(flags),
            'loop3_receipt_claim_flags': dict(loop3_flags), 'receipt_binding_sha256': receipt_bindings,
            'r22_authority': 'LOG.md:3298-3324; no lane-local validation receipt',
            'recounts': recounts, 'r29_defects': {'rows': len(queue), 'statuses': status, 'classes': classes},
            'r30_scoped_routed_items': len(routed), 'availability': availability,
            'parent_reported_completions_25_29': completions,
            'parent_reported_completion_sum_25_29': sum(completions.values()),
            'declared_requested_workers_excluding_skip_8_29': requests,
            'freshness': {'rows': len(frows), 'comparable': comparable, 'stable': stable,
                          'comparable_ratio': stable / comparable, 'all_row_ratio': stable / len(frows),
                          'original_threshold': .95},
            'r26_pairs_independently_replayed': len(pairs),
            'r26_operation_counts': dict(Counter(row['operation'] for row in pairs)),
            'r29_law_design_delivered_findings': [6, 4],
            'amendments': amendments, 'numeric_negative_controls': negative}


def pointers(document, disclosed_absent=()):
    p = ROOT / document
    raw = p.read_bytes()
    text = raw.decode()
    pattern = re.compile(r'(?<![\w/])((?:reports|tools|corpus|examples)/[A-Za-z0-9_./{}*,\[\]-]+|(?:LOG|SCORECARD|SKILL|SHONEN|PROVINCE|AGENTS|README)\.md)(?::([0-9]+(?:[-–,][0-9]+)*))?')
    found, missing, bad_ranges, templates = set(), [], [], []
    for match in pattern.finditer(text):
        path, locator = match.groups()
        path = path.rstrip('.,')
        if any(c in path for c in '{}*[') or 'round-N/' in path:
            templates.append(path)
            continue
        found.add((path, locator))
    for path, locator in sorted(found, key=lambda x: (x[0], x[1] or '')):
        if not locator_exists(path):
            missing.append(path)
        elif locator:
            count = len((ROOT / path).read_text().splitlines())
            if any(not 1 <= int(n) <= count for n in re.findall(r'\d+', locator)):
                bad_ranges.append([path, locator, count])
    disclosed = []
    for path in set(missing) & set(disclosed_absent):
        contexts = [text[max(0, m.start() - 120):m.end() + 240]
                    for m in re.finditer(re.escape(path), text)]
        if contexts and all(re.search(r'\babsent\b|\bmissing\b|\bno .{0,60}receipt\b', c, re.I | re.S)
                            for c in contexts):
            disclosed.append(path)
    unresolved = sorted(set(missing) - set(disclosed))
    revisions = sorted(set(re.findall(r'`([0-9a-f]{7,40})`', text)))
    bad_revisions = [rev for rev in revisions if not revision_exists(rev)]
    assert raw == p.read_bytes(), 'document changed while scanning'
    return {'document': document, 'sha256': sha256(raw).hexdigest(), 'lines': len(text.splitlines()),
            'literal_citations': len(found), 'literal_paths': len({p for p, _ in found}),
            'missing_paths': sorted(set(missing)), 'disclosed_absences': sorted(disclosed),
            'unresolved_positive_paths': unresolved, 'bad_ranges': bad_ranges,
            'revision_pointers': revisions, 'bad_revisions': bad_revisions,
            'templates_require_context_review': sorted(set(templates)),
            'literal_pointer_check_passed': not (missing or bad_ranges or bad_revisions),
            'positive_reference_check_passed': not (unresolved or bad_ranges or bad_revisions)}


def protected():
    paths = [f'reports/round-{n}' for n in range(8, 30)]
    paths += [f'tools/gates/frozen/round-{n}' for n in range(8, 30)]
    rows = git('ls-tree', '-r', '-z', BASE, '--', *paths).split(b'\0')
    bad, manifest = [], []
    for row in rows:
        if not row:
            continue
        metadata, path_bytes = row.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        name = path_bytes.decode()
        path = ROOT / name
        raw = path.read_bytes() if path.is_file() else None
        expected = git('cat-file', 'blob', oid)
        current_mode = '100755' if path.exists() and path.stat().st_mode & 0o111 else '100644'
        if raw != expected or current_mode != mode:
            bad.append(name)
        manifest.append([name, mode, oid, sha256(expected).hexdigest()])
    assert not bad, bad
    return {'baseline': BASE, 'paths': len(manifest), 'mismatches': bad,
            'manifest_sha256': sha256(json.dumps(manifest, separators=(',', ':')).encode()).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numbers', action='store_true')
    parser.add_argument('--selftest', action='store_true')
    parser.add_argument('--protected', action='store_true')
    parser.add_argument('--pointers', nargs='+')
    parser.add_argument('--disclosed-absent', nargs='*', default=[])
    args = parser.parse_args()
    result = {'date': datetime.now(timezone.utc).isoformat(),
              'command': 'python3 -B reports/round-30/retrospective-audit-C23-C25.py',
              'scope': 'read-only evidence audit; not round admission or historical validator execution'}
    if args.numbers:
        result['numbers'] = numbers()
    if args.selftest:
        result['controls'] = controls()
    if args.protected:
        result['protected'] = protected()
    if args.pointers:
        result['pointers'] = [pointers(path, args.disclosed_absent) for path in args.pointers]
    print(json.dumps(result, indent=2, sort_keys=True))
    return int(any(not r['positive_reference_check_passed'] for r in result.get('pointers', [])))


if __name__ == '__main__':
    raise SystemExit(main())
