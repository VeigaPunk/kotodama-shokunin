#!/usr/bin/env python3
"""Exact-set comparator for attestation-packet auditors (kotodama round 88).

Grades one candidate auditor against a case battery. Each case mutates a
committed base packet (or supplies raw bytes). The candidate runs as
`CANDIDATE --packet FILE --json` on an opaque per-run file name and must match
the case expectation exactly:

- The exit code equals the case rc.
- rc 2: the text ATTESTATION_ERROR appears on stdout or stderr.
- Otherwise stdout is a JSON object whose `findings` is a list of objects with
  string `id` and `record`.
  - Dirty cases: the set of ids equals the expected ids, and the set of
    (id, record) pairs equals the expected pairs. Multiplicity is not compared.
  - Clean cases: no findings, and `records` equals `records_count`.
- Malformed candidate output fails that case. It never aborts the run.

Cases file (JSON): {"cases": [CASE, ...]}. Each CASE has:
  name (unique str), rc (0|1|2), ids (list of str), records (list of str, same
  length as ids), mutations (list), and records_count (int, required when ids
  is empty).
  Mutation ops, applied in order to a deep copy of the base packet:
    {"op":"reverse"}
    {"op":"set","record":I,"path":P, one of "value" | "value_from_record":J |
     "value_from_path":Q}   (path/Q are dotted; value_from_record resolves P in
     record J; value_from_path resolves Q in record I)
    {"op":"delete","record":I,"path":P}
    {"op":"raw","value":S}   (sole mutation; S is the file content verbatim)

Usage:
  check-finding-sets.py --cases CASES.json --packet BASE.json \\
      --candidate AUDITOR.py [--json] --work EXISTING_DIR
  check-finding-sets.py --selftest --work EXISTING_DIR

Output: JSON {"passed", "total", "cases": [{name, passed, expected_rc, rc,
reason}]} on stdout with --json; otherwise a summary and failing reasons.
Input errors print {"error", "passed": 0, "total": 0, "cases": []} on stdout.
Exit: 0 every case passes (or selftest passes); 1 some case fails (or selftest
fails); 2 input or usage error.

Candidate lookup for the selftest honours KOTODAMA_ROOT, then walks up from
this file and then from the working directory, looking for
tools/check-attestation-packet.py. Only writes beneath a temporary directory
created inside --work.
"""

import argparse
import copy
import json
import os
import secrets
import signal
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT = 20
RAW_ERROR = 'ATTESTATION_ERROR'
HONEST_REL = Path('tools', 'check-attestation-packet.py')
VALUE_KEYS = ('value', 'value_from_record', 'value_from_path')


class InputError(Exception):
    """Case list, base packet, or CLI input is unusable; the run is refused."""


class Malformed(Exception):
    """Candidate stdout breaks the auditor contract; the case fails."""


def is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


def load_json(path, what):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError) as exc:
        raise InputError(f'{what} unreadable: {exc}')


def validate_cases(doc):
    cases = doc.get('cases') if isinstance(doc, dict) else None
    if not isinstance(cases, list) or not cases:
        raise InputError('cases must be a non-empty list')
    names = set()
    for case in cases:
        if not isinstance(case, dict):
            raise InputError('each case must be an object')
        name = case.get('name')
        if not isinstance(name, str) or not name or name in names:
            raise InputError(f'case name missing or duplicated: {name!r}')
        names.add(name)
        rc, ids, records = case.get('rc'), case.get('ids'), case.get('records')
        if not is_int(rc) or rc not in (0, 1, 2):
            raise InputError(f'{name}: rc must be 0, 1 or 2')
        if not isinstance(ids, list) or not all(isinstance(x, str) for x in ids):
            raise InputError(f'{name}: ids must be a list of strings')
        if not isinstance(records, list) or not all(isinstance(x, str) for x in records):
            raise InputError(f'{name}: records must be a list of strings')
        if not isinstance(case.get('mutations'), list):
            raise InputError(f'{name}: mutations must be a list')
        if rc == 2:
            if ids != [RAW_ERROR] or records:
                raise InputError(f'{name}: rc 2 needs ids [ATTESTATION_ERROR] and no records')
        elif rc == 0 and ids:
            raise InputError(f'{name}: rc 0 cannot expect findings')
        elif rc == 1 and not ids:
            raise InputError(f'{name}: rc 1 needs expected ids')
        if rc != 2 and len(ids) != len(records):
            raise InputError(f'{name}: ids and records differ in length')
        if not ids and not is_int(case.get('records_count')):
            raise InputError(f'{name}: clean case needs integer records_count')
    return cases


def validate_packet(doc):
    if not isinstance(doc, dict) or not isinstance(doc.get('records'), list):
        raise InputError('base packet must be an object with a records list')
    if any(not isinstance(r, dict) for r in doc['records']):
        raise InputError('base packet records must be objects')
    return doc


def locate(obj, dotted, where):
    parts = dotted.split('.')
    cur = obj
    for part in parts[:-1]:
        if not isinstance(cur, dict) or not isinstance(cur.get(part), dict):
            raise InputError(f'{where}: path {dotted!r} has no object at {part!r}')
        cur = cur[part]
    if not isinstance(cur, dict):
        raise InputError(f'{where}: path {dotted!r} has no object parent')
    return cur, parts[-1]


def read_path(obj, dotted, where):
    holder, leaf = locate(obj, dotted, where)
    if leaf not in holder:
        raise InputError(f'{where}: path {dotted!r} absent in source record')
    return holder[leaf]


def apply_mutation(doc, m, where):
    if not isinstance(m, dict) or not isinstance(m.get('op'), str):
        raise InputError(f'{where}: mutation must be an object with an op')
    records = doc['records']
    op = m['op']
    if op == 'reverse':
        if set(m) != {'op'}:
            raise InputError(f'{where}: reverse takes no arguments')
        records.reverse()
        return
    if op not in ('set', 'delete'):
        raise InputError(f'{where}: unknown op {op!r}')
    index = m.get('record')
    if not is_int(index) or not 0 <= index < len(records):
        raise InputError(f'{where}: record index out of range')
    path = m.get('path')
    if not isinstance(path, str) or not path:
        raise InputError(f'{where}: path must be a non-empty string')
    holder, leaf = locate(records[index], path, where)
    if op == 'delete':
        if set(m) != {'op', 'record', 'path'}:
            raise InputError(f'{where}: delete takes op, record and path only')
        holder.pop(leaf, None)
        return
    sources = [k for k in VALUE_KEYS if k in m]
    if len(sources) != 1 or set(m) != {'op', 'record', 'path', sources[0]}:
        raise InputError(f'{where}: set needs exactly one of {VALUE_KEYS}')
    source = sources[0]
    if source == 'value':
        value = m['value']
    elif source == 'value_from_record':
        other = m['value_from_record']
        if not is_int(other) or not 0 <= other < len(records):
            raise InputError(f'{where}: value_from_record index out of range')
        value = read_path(records[other], path, where)
    else:
        if not isinstance(m['value_from_path'], str):
            raise InputError(f'{where}: value_from_path must be a string')
        value = read_path(records[index], m['value_from_path'], where)
    holder[leaf] = copy.deepcopy(value)


def build_payload(packet, case):
    name = case['name']
    muts = case['mutations']
    if any(isinstance(m, dict) and m.get('op') == 'raw' for m in muts):
        if len(muts) != 1 or not isinstance(muts[0], dict) or set(muts[0]) != {'op', 'value'} \
                or not isinstance(muts[0]['value'], str):
            raise InputError(f'{name}: raw must be the sole mutation and carry a string value')
        return muts[0]['value'].encode('utf-8')
    doc = copy.deepcopy(packet)
    for m in muts:
        apply_mutation(doc, m, name)
    return json.dumps(doc, ensure_ascii=True).encode('ascii')


def run_candidate(candidate, packet_file, cwd):
    """Return (rc, stdout, stderr, failure). failure is set when the process never ran cleanly."""
    try:
        proc = subprocess.run([sys.executable, '-B', str(candidate), '--packet', str(packet_file), '--json'],
                              capture_output=True, timeout=TIMEOUT, cwd=str(cwd))
    except subprocess.TimeoutExpired:
        return None, '', '', f'timeout after {TIMEOUT}s'
    except OSError as exc:
        return None, '', '', f'cannot execute candidate: {exc}'
    return (proc.returncode, proc.stdout.decode('utf-8', 'replace'),
            proc.stderr.decode('utf-8', 'replace'), None)


def findings_of(body):
    if not isinstance(body, dict):
        raise Malformed('stdout JSON is not an object')
    findings = body.get('findings')
    if not isinstance(findings, list):
        raise Malformed('findings is not a list')
    pairs = []
    for finding in findings:
        if not isinstance(finding, dict):
            raise Malformed('finding is not an object')
        ident, record = finding.get('id'), finding.get('record')
        if not isinstance(ident, str) or not isinstance(record, str):
            raise Malformed('finding id and record must be strings')
        pairs.append((ident, record))
    return pairs


def judge(case, rc, out, err):
    if rc != case['rc']:
        return False, f'rc {rc} != expected {case["rc"]}'
    if case['rc'] == 2:
        ok = RAW_ERROR in out + err
        return ok, 'ATTESTATION_ERROR text present' if ok else 'ATTESTATION_ERROR text absent'
    try:
        body = json.loads(out)
    except ValueError:
        return False, 'stdout is not JSON'
    try:
        pairs = findings_of(body)
    except Malformed as exc:
        return False, f'malformed findings: {exc}'
    if not case['ids']:
        if pairs:
            return False, f'{len(pairs)} unexpected finding(s)'
        if not is_int(body.get('records')) or body['records'] != case['records_count']:
            return False, f'records {body.get("records")!r} != expected {case["records_count"]}'
        return True, 'clean: no findings, records match'
    got_ids = {i for i, _ in pairs}
    want_ids = set(case['ids'])
    if got_ids != want_ids:
        return False, f'id set {sorted(got_ids)} != expected {sorted(want_ids)}'
    if set(pairs) != set(zip(case['ids'], case['records'])):
        return False, 'id/record pair set differs from expected'
    return True, 'exact id and pair sets'


def score(candidate, packet, cases, work):
    rows = []
    with tempfile.TemporaryDirectory(prefix='finding-sets-', dir=work) as td:
        scratch = Path(td)
        staged = []
        for case in cases:
            path = scratch / (secrets.token_hex(12) + '.json')
            path.write_bytes(build_payload(packet, case))
            staged.append((case, path))
        timed_out = False
        for case, path in staged:
            if timed_out:
                rows.append(dict(name=case['name'], passed=False, expected_rc=case['rc'], rc=None,
                                 reason='not run: candidate timed out on an earlier case'))
                continue
            rc, out, err, failure = run_candidate(candidate, path, scratch)
            if failure:
                passed, reason = False, failure
                timed_out = failure.startswith('timeout')
            else:
                passed, reason = judge(case, rc, out, err)
            rows.append(dict(name=case['name'], passed=passed, expected_rc=case['rc'], rc=rc, reason=reason))
    return rows


def summarize(rows):
    return dict(passed=sum(1 for r in rows if r['passed']), total=len(rows), cases=rows)


def fail_input(message):
    print(json.dumps(dict(error=message, passed=0, total=0, cases=[]), indent=2, sort_keys=True))
    print(f'check-finding-sets: {message}', file=sys.stderr)
    return 2


# ---------------------------------------------------------------- selftest

PRE = '''#!/usr/bin/env python3
import json, subprocess, sys
HONEST = @HONEST@
packet = sys.argv[sys.argv.index('--packet') + 1]
run = subprocess.run([sys.executable, '-B', HONEST, '--packet', packet, '--json'], capture_output=True, text=True)
'''

EXTRA_ID = '''
if run.returncode == 1:
    body = json.loads(run.stdout)
    body["findings"].append({"id": "CLOCK_SCOPE", "record": "invented", "detail": "extra id"})
    print(json.dumps(body)); sys.exit(1)
sys.stdout.write(run.stdout); sys.stderr.write(run.stderr); sys.exit(run.returncode)
'''

SHOTGUN = '''
LABELS = ["RECORD_ID", "CLOCK_MISSING", "CLOCK_REASON", "CLOCK_DATE", "RECORD_FIELD",
          "SOLUTION_CONFLICT", "EDITORIAL_CONFLICT", "TRANSLATION_CLOCK"]
if run.returncode == 1:
    body = json.loads(run.stdout)
    body["findings"] = [{"id": l, "record": "shotgun", "detail": "all"} for l in LABELS]
    print(json.dumps(body)); sys.exit(1)
sys.stdout.write(run.stdout); sys.stderr.write(run.stderr); sys.exit(run.returncode)
'''

WRONG_RECORD = '''
if run.returncode == 1:
    body = json.loads(run.stdout)
    for f in body["findings"]:
        f["record"] = "WRONG"
    print(json.dumps(body)); sys.exit(1)
sys.stdout.write(run.stdout); sys.stderr.write(run.stderr); sys.exit(run.returncode)
'''

FILENAME_ONLY = '''
import pathlib
TABLE = {"clean": (0, [], 2), "duplicate-id": (1, ["RECORD_ID"], 2),
         "missing-clock": (1, ["CLOCK_MISSING"], 2), "blank-reason": (1, ["CLOCK_REASON"], 2),
         "blank-sense": (1, ["RECORD_FIELD"], 2), "invalid-json": (2, ["ATTESTATION_ERROR"], None)}
rc, ids, records = TABLE.get(pathlib.Path(packet).stem, (1, ["RECORD_ID"], 2))
if rc == 2:
    print("ATTESTATION_ERROR: unreadable packet", file=sys.stderr); sys.exit(2)
print(json.dumps({"findings": [{"id": i, "record": "file", "detail": "name"} for i in ids], "records": records}))
sys.exit(rc)
'''

MALFORMED = {
    'nonjson': "sys.stdout.write('findings: none\\n'); sys.exit(run.returncode)\n",
    'findings-not-list': "print(json.dumps({'records': 2, 'findings': {}})); sys.exit(run.returncode)\n",
    'finding-not-object': "print(json.dumps({'records': 2, 'findings': ['RECORD_ID']})); sys.exit(run.returncode)\n",
    'finding-without-record': "print(json.dumps({'records': 2, 'findings': [{'id': 'RECORD_ID'}]})); sys.exit(run.returncode)\n",
    'body-not-object': "print(json.dumps(['records'])); sys.exit(run.returncode)\n",
    'candidate-crash': "raise RuntimeError('boom')\n",
}


def locate_honest():
    env = os.environ.get('KOTODAMA_ROOT')
    starts = ([Path(env)] if env else []) + [Path(__file__).resolve().parent, Path.cwd()]
    for start in starts:
        for root in [start, *start.resolve().parents]:
            found = root / HONEST_REL
            if found.is_file():
                return found.resolve()
    return None


def fixture_packet():
    def clock():
        return dict(value=None, reason='Unknown in this fictional exercise.', scope='synthetic')

    def record(identity, sense):
        item = dict(id=identity, sense=sense, wording='Mend before sailing.', genre='proverb',
                    composition_status='original_exercise')
        for name in ('attestation', 'origin', 'collection', 'design'):
            item[name] = clock()
        return item

    return dict(status='NON-CANON', boundary='Invented selftest exercises.',
                records=[record('SELF-A', 'Invented repair advice.'), record('SELF-B', 'Invented second sense.')])


def fixture_cases():
    return dict(cases=[
        dict(name='clean', rc=0, ids=[], records=[], records_count=2, mutations=[]),
        dict(name='duplicate-id', rc=1, ids=['RECORD_ID'], records=['SELF-A'],
             mutations=[dict(op='set', record=1, path='id', value_from_record=0)]),
        dict(name='missing-clock', rc=1, ids=['CLOCK_MISSING'], records=['SELF-A'],
             mutations=[dict(op='delete', record=0, path='origin')]),
        dict(name='blank-reason', rc=1, ids=['CLOCK_REASON'], records=['SELF-B'],
             mutations=[dict(op='set', record=1, path='origin.reason', value='  ')]),
        dict(name='blank-sense', rc=1, ids=['RECORD_FIELD'], records=['SELF-B'],
             mutations=[dict(op='set', record=1, path='sense', value=' ')]),
        dict(name='invalid-json', rc=2, ids=['ATTESTATION_ERROR'], records=[],
             mutations=[dict(op='raw', value='{broken')]),
    ])


def write_wrapper(directory, name, honest, body):
    path = directory / f'{name}.py'
    path.write_text(PRE.replace('@HONEST@', repr(str(honest))) + body, encoding='utf-8')
    return path


def cli(args):
    return subprocess.run([sys.executable, '-B', str(Path(__file__).resolve()), *args],
                          capture_output=True, text=True, timeout=300)


def parse(text):
    try:
        return json.loads(text)
    except ValueError:
        return None


def selftest(work):
    honest = locate_honest()
    checks = []

    def check(name, passed, observed):
        checks.append(dict(check=name, passed=bool(passed), observed=observed))

    check('honest-auditor-located', honest is not None, str(honest))
    if honest is None:
        return emit_selftest(checks)
    with tempfile.TemporaryDirectory(prefix='finding-sets-selftest-', dir=work) as td:
        d = Path(td)
        packet = d / 'base-packet.json'
        packet.write_text(json.dumps(fixture_packet()), encoding='utf-8')
        cases = d / 'battery.json'
        cases.write_text(json.dumps(fixture_cases()), encoding='utf-8')
        bad = d / 'bad-cases.json'
        bad.write_text(json.dumps(dict(cases=[dict(name='x', rc=1, ids=['A'], records=[], mutations=[])])),
                       encoding='utf-8')
        unknown = d / 'unknown-op.json'
        unknown.write_text(json.dumps(dict(cases=[dict(name='y', rc=0, ids=[], records=[], records_count=2,
                                                       mutations=[dict(op='shuffle')])])), encoding='utf-8')

        def run_and_score(candidate):
            proc = cli(['--cases', str(cases), '--packet', str(packet), '--candidate', str(candidate),
                        '--json', '--work', str(work)])
            return proc, parse(proc.stdout)

        for label, cand, want_passed, want_rc in (
                ('honest-positive', honest, 6, 0),
                ('extra-id-refused', write_wrapper(d, 'extra', honest, EXTRA_ID), 2, 1),
                ('shotgun-refused', write_wrapper(d, 'shotgun', honest, SHOTGUN), 2, 1),
                ('wrong-record-refused', write_wrapper(d, 'wrong-record', honest, WRONG_RECORD), 2, 1),
                ('filename-only-refused', write_wrapper(d, 'filename', honest, FILENAME_ONLY), 0, 1)):
            proc, body = run_and_score(cand)
            observed = None if body is None else body.get('passed')
            check(label, body is not None and observed == want_passed and proc.returncode == want_rc
                  and body.get('total') == 6 and proc.stderr == '',
                  dict(rc=proc.returncode, passed=observed, total=None if body is None else body.get('total')))
        for label, body_src in MALFORMED.items():
            cand = write_wrapper(d, label, honest, body_src)
            proc, body = run_and_score(cand)
            observed = None if body is None else body.get('passed')
            check(f'malformed-{label}-fails-cases',
                  body is not None and observed == 0 and proc.returncode == 1 and body.get('total') == 6,
                  dict(rc=proc.returncode, passed=observed, stderr_tail=proc.stderr[-200:]))
        hang = write_wrapper(d, 'hang', honest, 'import time\ntime.sleep(60)\n')
        proc, body = run_and_score(hang)
        reasons = [] if body is None else [c['reason'] for c in body.get('cases', [])]
        check('hang-times-out-once',
              body is not None and body.get('passed') == 0 and len(reasons) == 6
              and reasons[0].startswith('timeout') and all(r.startswith('not run') for r in reasons[1:]),
              dict(rc=proc.returncode, reasons=reasons[:2]))
        proc = cli(['--cases', str(bad), '--packet', str(packet), '--candidate', str(honest),
                    '--json', '--work', str(work)])
        check('ids-records-mismatch-refused', proc.returncode == 2 and parse(proc.stdout) is not None
              and 'error' in parse(proc.stdout), dict(rc=proc.returncode))
        proc = cli(['--cases', str(unknown), '--packet', str(packet), '--candidate', str(honest),
                    '--json', '--work', str(work)])
        check('unknown-op-refused', proc.returncode == 2 and parse(proc.stdout) is not None
              and 'error' in parse(proc.stdout), dict(rc=proc.returncode))
        proc = cli(['--cases', str(cases), '--packet', str(packet), '--candidate', str(honest),
                    '--json', '--work', str(d / 'absent')])
        check('missing-work-refused', proc.returncode == 2, dict(rc=proc.returncode))
    return emit_selftest(checks)


def emit_selftest(checks):
    passed = sum(1 for c in checks if c['passed'])
    print(json.dumps(dict(label='FINDING_SETS_SELFTEST', checks=checks, passed=passed, total=len(checks)),
                     indent=2, sort_keys=True))
    return 0 if passed == len(checks) else 1


# ---------------------------------------------------------------- main

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--cases', type=Path, help='case battery JSON')
    parser.add_argument('--packet', type=Path, help='committed base packet JSON')
    parser.add_argument('--candidate', type=Path, help='auditor to grade (runs as CANDIDATE --packet FILE --json)')
    parser.add_argument('--work', type=Path, help='existing directory; scratch is created beneath it')
    parser.add_argument('--json', action='store_true', help='print the JSON result')
    parser.add_argument('--selftest', action='store_true', help='exercise this CLI end to end; needs only --work')
    signal.signal(signal.SIGTERM, lambda signum, frame: sys.exit(128 + signum))
    args = parser.parse_args(argv)

    if args.work is None or not args.work.is_dir():
        return fail_input('--work must name an existing directory')
    work = args.work.resolve()
    if args.selftest:
        if args.cases or args.packet or args.candidate:
            return fail_input('--selftest takes only --work')
        return selftest(work)
    absent = [flag for flag, value in (('--cases', args.cases), ('--packet', args.packet),
                                       ('--candidate', args.candidate)) if value is None]
    if absent:
        return fail_input(f'missing {", ".join(absent)}')
    try:
        cases = validate_cases(load_json(args.cases, 'cases'))
        packet = validate_packet(load_json(args.packet, 'base packet'))
        candidate = args.candidate.resolve()
        if not candidate.is_file():
            raise InputError('candidate is not a file')
        rows = score(candidate, packet, cases, work)
    except InputError as exc:
        return fail_input(str(exc))
    result = summarize(rows)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f'{result["passed"]}/{result["total"]} cases pass')
        for row in rows:
            if not row['passed']:
                print(f'  FAIL {row["name"]}: {row["reason"]}')
    return 0 if result['passed'] == result['total'] else 1


if __name__ == '__main__':
    sys.exit(main())
