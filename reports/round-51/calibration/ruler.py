#!/usr/bin/env python3
"""Independent R51 CLI ruler; no candidate imports, source rewrites or Git writes.

Run only after Main approves and lands this instrument and its oracle. A run
measures the explicitly selected checker bytes; it never updates expectations.
Temporary plain-file WORKTREE inputs stay under the required --scratch path.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(receipt, code, reason=None):
    receipt['exit_code'] = code
    receipt['verdict'] = {0: 'match', 1: 'mismatch', 2: 'unevaluable'}[code]
    receipt['stop_reason'] = reason
    receipt['matched'] = sum(row.get('matched', False) for row in receipt['cases'])
    receipt['observed_runs'] = sum(row.get('actual', {}).get('exit') is not None
                                   for row in receipt['cases'])
    receipt['remaining_notObserved'] = sum(row['status'] == 'notObserved'
                                           for row in receipt['cases'])
    print(json.dumps(receipt, indent=2))
    return code


def semantic_result(run):
    """Read stable CLI identities, not explanatory wording or whitespace."""
    lines = [line.strip() for line in run.stdout.splitlines() if line.strip()]
    # NOTE is a known informational protocol class; retain its raw wording only.
    errors = [line.strip() for line in run.stderr.splitlines()
              if line.strip()
              and line.strip().split(maxsplit=1)[0] != 'SEPARABILITY_NOTE']
    if run.returncode == 2 and not lines and len(errors) == 1:
        if errors[0].split(maxsplit=1)[0] != 'SEPARABILITY_INPUT_ERROR':
            raise ValueError('unrecognized could-not-evaluate classification')
        result = {'exit': 2, 'classification': 'input_error',
                  'finding_class': 'SEPARABILITY_INPUT_ERROR'}
        error_id = re.search(r'\bREFERENCE_(OUTSIDE_REPOSITORY|AMBIGUOUS)\b',
                             errors[0])
        if error_id:
            locations = re.findall(r'([\w./-]+):([1-9]\d*)(?![\w.])',
                                   errors[0])
            if len(locations) != 1:
                raise ValueError('reference error has no unique citing location')
            result.update(error_id=error_id.group(),
                          citing_path=locations[0][0],
                          citing_line=int(locations[0][1]))
        return result
    if run.returncode not in (0, 1) or errors or not lines:
        raise ValueError('output does not declare a comparable verdict')
    summaries = [line for line in lines if line.startswith('SEPARABILITY:')]
    if len(summaries) != 1:
        raise ValueError('missing or duplicate finding-count declaration')
    summary = re.fullmatch(r'SEPARABILITY:\s*(\d+)(?:\s+.*)?', summaries[0])
    if summary is None:
        raise ValueError('finding-count declaration is not numeric')
    findings = []
    for line in lines:
        if line == summaries[0]:
            continue
        pieces = line.split(maxsplit=2)
        edge = (re.fullmatch(r'([A-Za-z][A-Za-z0-9_-]*)->'
                             r'([A-Za-z][A-Za-z0-9_-]*)', pieces[1])
                if len(pieces) >= 2 and pieces[0] == 'SEPARABILITY_DEPENDENCY'
                else None)
        if edge is None:
            raise ValueError('unknown or unparseable finding class')
        targets = re.findall(r"""['"]([^'"]+)['"]""", line)
        locations = re.findall(r'([\w./-]+):([1-9]\d*)(?![\w.])', line)
        if len(targets) != 1 or len(locations) != 1:
            raise ValueError('dependency has no unique target/citing location')
        findings.append({'finding_class': 'SEPARABILITY_DEPENDENCY',
                         'owner': edge.group(1),
                         'dependency_owner': edge.group(2),
                         'canonical_target': targets[0],
                         'citing_path': locations[0][0],
                         'citing_line': int(locations[0][1])})
    declared = int(summary.group(1))
    if declared != len(findings) or (run.returncode == 0) != (declared == 0):
        raise ValueError('exit/count/finding identities contradict each other')
    return {'exit': run.returncode, 'classification': 'findings',
            'declared_findings': declared, 'findings': findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tool', type=Path, required=True)
    parser.add_argument('--tool-revision', required=True,
                        help='Parent-selected landed revision holding the checker')
    parser.add_argument('--tool-sha256', required=True,
                        help='Parent-selected checker byte digest, not inferred output')
    parser.add_argument('--lane', type=Path, required=True)
    parser.add_argument('--oracle', type=Path, required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    args = parser.parse_args()
    tool, lane = args.tool.absolute(), args.lane.absolute()
    receipt = {'ruler_sha256': digest(Path(__file__)), 'cases': [],
               'selected_tool': str(tool),
               'parent_selected_tool_sha256': args.tool_sha256,
               'parent_selected_tool_revision': args.tool_revision,
               'limit': 'Bounded CLI reference-name cases, not universal separability.'}
    env = dict(os.environ)
    for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE',
                'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES',
                'GIT_COMMON_DIR', 'GIT_NAMESPACE'):
        env.pop(key, None)
    try:
        receipt['oracle_sha256'] = digest(args.oracle)
        oracle = json.loads(args.oracle.read_text())
        cases = oracle.get('cases') if isinstance(oracle, dict) else None
        if not isinstance(cases, list) or not cases:
            raise ValueError('oracle requires a nonempty cases list')
        receipt['cases'] = [
            {'id': case.get('id') if isinstance(case, dict) else None,
             'status': 'notObserved', 'matched': False,
             'expected': case.get('expected') if isinstance(case, dict) else None}
            for case in cases]
        identities = set()
        for case in cases:
            if not isinstance(case, dict):
                raise ValueError('case must be an object')
            identity, expected = case.get('id'), case.get('expected')
            if (not isinstance(identity, str)
                    or re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', identity) is None
                    or identity in identities):
                raise ValueError('case identities must be nonempty and unique')
            identities.add(identity)
            if (not isinstance(expected, dict) or not expected
                    or type(expected.get('exit')) is not int
                    or expected['exit'] not in (0, 1, 2)):
                raise ValueError('case requires nonempty typed expectations')
            if expected.get('classification') == 'findings':
                if (type(expected.get('declared_findings')) is not int
                        or not isinstance(expected.get('findings'), list)
                        or expected['declared_findings'] != len(expected['findings'])):
                    raise ValueError('finding expectations require count and identities')
            elif (expected.get('classification') != 'input_error'
                  or expected.get('finding_class') != 'SEPARABILITY_INPUT_ERROR'
                  or expected['exit'] != 2):
                raise ValueError('unknown expected verdict classification')
            if not all(isinstance(case.get(key), str) and case[key]
                       for key in ('citer', 'reference', 'target')):
                raise ValueError('case requires its three nonempty input strings')
        requested_base = oracle.get('base')
        if not isinstance(requested_base, str) or not requested_base:
            raise ValueError('oracle requires its base revision')
        receipt['oracle_base'] = requested_base
        receipt['git_metadata'] = []
        for name, revision in (('base', requested_base),
                               ('tool_revision', args.tool_revision)):
            argv = ['git', '--no-lazy-fetch', '-C', str(lane),
                    'rev-parse', '--verify', revision + '^{commit}']
            run = subprocess.run(argv, cwd=lane, env=env, capture_output=True,
                                 text=True, timeout=60, check=False)
            receipt['git_metadata'].append(
                {'name': name, 'argv': argv, 'exit': run.returncode,
                 'stdout': run.stdout, 'stderr': run.stderr})
            resolved = run.stdout.strip()
            if run.returncode or re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}',
                                              resolved) is None:
                raise ValueError('cannot resolve requested ' + name + ' commit')
            receipt['resolved_' + name] = resolved
        source_path = 'tools/check-claim-separability.py'
        argv = ['git', '--no-lazy-fetch', '-C', str(lane), 'cat-file', 'blob',
                receipt['resolved_tool_revision'] + ':' + source_path]
        blob = subprocess.run(argv, cwd=lane, env=env, capture_output=True,
                              timeout=60, check=False)
        receipt['tool_source'] = {
            'revision': receipt['resolved_tool_revision'], 'path': source_path,
            'argv': argv, 'exit': blob.returncode,
            'blob_sha256': hashlib.sha256(blob.stdout).hexdigest(),
            'stderr': blob.stderr.decode('utf-8', 'replace')}
        receipt['tool_sha256'] = digest(tool)
        if (blob.returncode or receipt['tool_sha256'] != args.tool_sha256
                or receipt['tool_source']['blob_sha256'] != args.tool_sha256):
            raise ValueError('selected checker bytes do not match Parent/source pins')
        args.scratch.mkdir(parents=True, exist_ok=True)
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        return emit(receipt, 2, type(exc).__name__ + ': ' + str(exc))

    for index, case in enumerate(cases):
        row = receipt['cases'][index]
        row['status'] = 'unsettled'
        try:
            with tempfile.TemporaryDirectory(prefix='r51-' + case['id'] + '-',
                                             dir=args.scratch) as directory:
                root = Path(directory)
                source = root / case['citer']
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_text(('reference-fixture\n' * 7)
                                  + case['reference'] + '\n')
                target = root / case['target']
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text('# Evidence\n')
                c_lands = [case['citer']]
                if case.get('same_owner'):
                    c_lands.append(case['target'])
                    (root / 'record.txt').write_text('unrelated record\n')
                    record_lands = ['record.txt']
                else:
                    record_lands = [case['target']]
                manifest = {
                    'schema': 'kotodama-separability-manifest-v1',
                    'base': receipt['resolved_base'],
                    'claims': [
                        {'id': 'C', 'role': case.get('citer_role', 'claim'),
                         'tree': 'WORKTREE', 'lands': c_lands, 'exports': []},
                        {'id': 'REC', 'role': 'record', 'tree': 'WORKTREE',
                         'lands': record_lands, 'exports': []},
                    ],
                }
                if case.get('manifest_error') == 'missing-base':
                    del manifest['base']
                elif case.get('manifest_error') == 'unknown-key':
                    manifest['undeclared'] = True
                elif case.get('manifest_error') == 'noncanonical-land':
                    manifest['claims'][0]['lands'] = ['corpus/../corpus/SOURCES.md']
                input_path = root / 'manifest.json'
                input_path.write_text(json.dumps(manifest))
                row['argv'] = [sys.executable, '-B', str(tool), str(input_path),
                               '--lane', str(lane), '--root', str(root)]
                run = subprocess.run(row['argv'], cwd=root,
                                     env=dict(env, TMPDIR=str(root)),
                                     capture_output=True, text=True,
                                     timeout=60, check=False)
                row['actual'] = {'exit': run.returncode, 'stdout': run.stdout,
                                 'stderr': run.stderr}
                try:
                    semantic = semantic_result(run)
                except ValueError as exc:
                    row['status'] = 'unevaluable'
                    return emit(receipt, 2, str(exc))
                row.update(status='observed', semantic=semantic)
                row['matched'] = all(semantic.get(key) == value
                                     for key, value in case['expected'].items())
        except subprocess.TimeoutExpired as exc:
            row['actual'] = {
                'exit': None,
                'stdout': (exc.stdout.decode('utf-8', 'replace')
                           if isinstance(exc.stdout, bytes) else exc.stdout or ''),
                'stderr': (exc.stderr.decode('utf-8', 'replace')
                           if isinstance(exc.stderr, bytes) else exc.stderr or '')}
            row['stop_reason'] = 'timeout'
            return emit(receipt, 2, 'current CLI timed out; no retry')
        except OSError as exc:
            row['stop_reason'] = type(exc).__name__ + ': ' + str(exc)
            return emit(receipt, 2, 'current case unsettled; no retry')
    return emit(receipt, 0 if receipt['cases']
                and all(row['matched'] for row in receipt['cases']) else 1)


if __name__ == '__main__':
    sys.exit(main())
