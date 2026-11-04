#!/usr/bin/env python3
"""Audit trusted local JSON packet structure, not attestation truth or canon.

The four clocks remain separate; null dates need an explicit reason and scope.
Fictional exercise metadata is neither rewritten nor promoted to evidence.
Exit 0: clean; 1: structural findings; 2: ATTESTATION_ERROR input/CLI failure.
Only --selftest writes, under a temporary directory in existing --work.
"""

import argparse
import copy
from datetime import date
import json
from pathlib import Path
import subprocess
import sys
import tempfile


CLOCKS = ('attestation', 'origin', 'collection', 'design')
FIELDS = ('sense', 'wording', 'genre', 'composition_status')


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def iso_date(value):
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f'non-JSON constant: {value}')


def audit(packet):
    if not isinstance(packet, dict) or not isinstance(packet.get('records'), list):
        raise ValueError('packet must be an object with a records array')
    records = packet['records']
    if any(not isinstance(record, dict) for record in records):
        raise ValueError('each record must be an object')
    findings = []
    seen = set()
    for index, record in enumerate(records, 1):
        identity = record.get('id')
        label = identity if text(identity) else f'#{index}'

        def add(code, detail):
            findings.append(dict(id=code, record=label, detail=detail))

        if not text(identity):
            add('RECORD_ID', 'id must be nonblank text')
        elif identity in seen:
            add('RECORD_ID', 'duplicate record id')
        else:
            seen.add(identity)
        for field in FIELDS:
            if not text(record.get(field)):
                add('RECORD_FIELD', f'{field} must be nonblank text')
        for name in CLOCKS:
            clock = record.get(name)
            if not isinstance(clock, dict):
                add('CLOCK_MISSING', f'{name} clock object required')
                continue
            if 'value' not in clock:
                add('CLOCK_MISSING', f'{name}.value must be explicit, including when null')
            elif clock['value'] is not None and not iso_date(clock['value']):
                add('CLOCK_DATE', f'{name}.value must be null or a YYYY-MM-DD date')
            if not text(clock.get('reason')):
                add('CLOCK_REASON', f'{name}.reason must be nonblank even for an unknown date')
            if not text(clock.get('scope')):
                add('CLOCK_SCOPE', f'{name}.scope must be nonblank text')

        for name in ('solutions', 'editorial', 'translation'):
            if name in record and not isinstance(record[name], dict):
                add('RECORD_FIELD', f'{name} must be an object when present')
        solutions = record.get('solutions')
        if isinstance(solutions, dict):
            if solutions.get('status') == 'unresolved' and solutions.get('selected') is not None:
                add('SOLUTION_CONFLICT', 'unresolved solution cannot select an answer')
        editorial = record.get('editorial')
        if isinstance(editorial, dict):
            transmitted = editorial.get('transmitted_wording')
            conjectured = editorial.get('conjectured_wording')
            for name in ('transmitted_wording', 'conjectured_wording'):
                if not text(editorial.get(name)):
                    add('RECORD_FIELD', f'editorial.{name} must be nonblank text')
            if (text(transmitted) and text(conjectured) and transmitted != conjectured
                    and record.get('wording') == conjectured):
                add('EDITORIAL_CONFLICT', 'record wording promotes a different editorial conjecture')
        translation = record.get('translation')
        if isinstance(translation, dict):
            translated = translation.get('translation_date')
            if not iso_date(translated):
                add('CLOCK_DATE', 'translation.translation_date must be a YYYY-MM-DD date')
            attestation = record.get('attestation')
            target = attestation.get('value') if isinstance(attestation, dict) else None
            if False:
                add('TRANSLATION_CLOCK', 'target attestation precedes its translation date')
    return dict(records=len(records), findings=findings)


def emit(body):
    print(json.dumps(body, ensure_ascii=True, sort_keys=True, indent=2))


def selftest(work):
    """Exercise this file's public CLI, not internal audit calls or an oracle."""
    if not work.is_dir():
        raise ValueError('--work must be an existing directory')
    base = dict(id='exercise-A', sense='Invented repair advice.', wording='Mend before sailing.',
                genre='proverb', composition_status='original_exercise')
    for name in CLOCKS:
        base[name] = dict(value=None, reason='Unknown in this fictional exercise.', scope='synthetic')
    packet = dict(status='NON-CANON', boundary='Invented exercises, not source evidence.', records=[base])
    cases = [('clean-first', packet, 0, [], 1)]

    def changed(name, code, label, change):
        value = copy.deepcopy(packet)
        change(value)
        cases.append((name, value, code, [label] if label else [], len(value['records'])))

    for count in (3, 7):
        population = copy.deepcopy(packet)
        population['records'] = [dict(copy.deepcopy(base), id=f'varied-{n}',
                                      wording=f'Invented wording {n}.') for n in range(count)]
        cases.append((f'positive-population-{count}', population, 0, [], count))
    changed('known-leap-date', 0, None,
            lambda p: p['records'][0]['origin'].update(value='2000-02-29'))
    changed('duplicate-id', 1, 'RECORD_ID', lambda p: p['records'].append(copy.deepcopy(base)))
    changed('empty-id', 1, 'RECORD_ID', lambda p: p['records'][0].update(id=' '))
    changed('typed-id', 1, 'RECORD_ID', lambda p: p['records'][0].update(id=[]))
    changed('missing-clock', 1, 'CLOCK_MISSING', lambda p: p['records'][0].pop('origin'))
    changed('typed-clock', 1, 'CLOCK_MISSING', lambda p: p['records'][0].update(origin=[]))
    changed('missing-value', 1, 'CLOCK_MISSING', lambda p: p['records'][0]['origin'].pop('value'))
    changed('blank-reason-unknown', 1, 'CLOCK_REASON', lambda p: p['records'][0]['origin'].update(reason=' '))
    changed('blank-scope', 1, 'CLOCK_SCOPE', lambda p: p['records'][0]['origin'].update(scope=''))
    changed('invalid-calendar', 1, 'CLOCK_DATE', lambda p: p['records'][0]['origin'].update(value='1710-02-30'))
    changed('compact-date', 1, 'CLOCK_DATE', lambda p: p['records'][0]['origin'].update(value='20260101'))
    changed('typed-date', 1, 'CLOCK_DATE', lambda p: p['records'][0]['origin'].update(value=2026))
    for field in FIELDS:
        changed(f'blank-{field}', 1, 'RECORD_FIELD', lambda p, f=field: p['records'][0].update({f: ' '}))
    changed('typed-wording', 1, 'RECORD_FIELD', lambda p: p['records'][0].update(wording={}))
    changed('unresolved-selected', 1, 'SOLUTION_CONFLICT',
            lambda p: p['records'][0].update(solutions=dict(status='unresolved', selected='boat')))
    changed('unresolved-clean', 0, None,
            lambda p: p['records'][0].update(solutions=dict(status='unresolved', selected=None)))
    changed('resolved-selected', 0, None,
            lambda p: p['records'][0].update(solutions=dict(status='resolved', selected='boat')))
    changed('editorial-promoted', 1, 'EDITORIAL_CONFLICT',
            lambda p: p['records'][0].update(editorial=dict(transmitted_wording='Damaged [gap].', conjectured_wording=base['wording'])))
    changed('editorial-separated', 0, None,
            lambda p: p['records'][0].update(editorial=dict(transmitted_wording=base['wording'], conjectured_wording='New conjecture.')))
    changed('typed-editorial', 1, 'RECORD_FIELD', lambda p: p['records'][0].update(editorial=[]))
    for name, target, rc, label in (
            ('translation-backdated', '1780-01-01', 1, 'TRANSLATION_CLOCK'),
            ('translation-equal', '1890-01-01', 0, None),
            ('translation-later', '1900-01-01', 0, None),
            ('translation-unknown', None, 0, None)):
        def translate(p, value=target):
            p['records'][0]['attestation']['value'] = value
            p['records'][0]['translation'] = dict(translation_date='1890-01-01')
        changed(name, rc, label, translate)
    for name, value in (
            ('malformed-json', b'{broken'),
            ('duplicate-json-key', b'{"records":[],"records":[]}'),
            ('duplicate-nested-key', b'{"records":[{"id":"A","id":"B"}]}'),
            ('top-array', []), ('typed-records', {'records': {}}),
            ('typed-record', {'records': [None]}), ('non-json-constant', b'{"records":[],"x":NaN}')):
        cases.append((name, value, 2, ['ATTESTATION_ERROR'], 0))
    checks = []
    with tempfile.TemporaryDirectory(prefix='attestation-selftest-', dir=work) as temp:
        directory = Path(temp)
        for name, value, expected_rc, expected_ids, count in cases:
            fixture = directory / f'{name}.json'
            fixture.write_bytes(value if isinstance(value, bytes) else json.dumps(value).encode('utf-8'))
            command = [sys.executable, '-B', str(Path(__file__).resolve()), '--packet', str(fixture), '--json']
            proc = subprocess.run(command, capture_output=True, text=True, timeout=15)
            try:
                body = json.loads(proc.stdout)
                ids = [finding['id'] for finding in body['findings']]
                shape = (body['records'] == count and all(
                    isinstance(f, dict) and set(f) == {'id', 'record', 'detail'}
                    and all(isinstance(v, str) for v in f.values()) for f in body['findings']))
            except (ValueError, KeyError, TypeError):
                ids, shape = [], False
            passed = proc.returncode == expected_rc and ids == expected_ids and shape and not proc.stderr
            checks.append(dict(case=name, expected_rc=expected_rc, expected_ids=expected_ids,
                               rc=proc.returncode, stdout=proc.stdout, stderr=proc.stderr, passed=passed))
    emit(dict(label='ATTESTATION_SELFTEST', checks=checks,
              passed=sum(check['passed'] for check in checks), total=len(checks)))
    return 0 if all(check['passed'] for check in checks) else 1


def main():
    parser = Parser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--packet', type=Path)
    mode.add_argument('--selftest', action='store_true')
    parser.add_argument('--json', action='store_true', help='emit deterministic JSON (also the default)')
    parser.add_argument('--work', type=Path)
    try:
        args = parser.parse_args()
        if args.selftest:
            if args.work is None:
                raise ValueError('--selftest requires --work EXISTING_DIR')
            return selftest(args.work)
        if args.work is not None:
            raise ValueError('--work is only valid with --selftest')
        packet = json.loads(args.packet.read_text(encoding='utf-8'),
                            object_pairs_hook=unique_object, parse_constant=reject_constant)
        result = audit(packet)
        emit(result)
        return 1 if result['findings'] else 0
    except (OSError, UnicodeError, ValueError, RecursionError, subprocess.TimeoutExpired) as exc:
        emit(dict(records=0, findings=[dict(id='ATTESTATION_ERROR', record='', detail=str(exc))]))
        return 2


if __name__ == '__main__':
    sys.exit(main())
