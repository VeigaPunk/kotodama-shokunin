#!/usr/bin/env python3
"""Audit inherited NON-CANON creative records through a candidate public CLI.

This is not measure87.py, historical evidence, semantic truth, or lore acceptance.
Usage: python -B run-trial.py --tool /absolute/candidate.py --work /isolated/existing
The JSON receipt uses relative subprocess arguments and a symbolic work directory;
no removed scratch path is required to interpret or reproduce its evidence.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

BASE = '83846a22ee1e9da7aa52ac505ccebf4455169247'
SOURCE = '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'
PACKET_SHA256 = '4f631b60b5ea5d5cf42b2ef394d548ff557e4ccaa52f176d7327fead8f34c982'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def trial_cases(packet, raw):
    # Expected relationships are stated here, independently of candidate code.
    yield ('inherited-six', raw, 0, None,
           'Six synthetic records retain distinct attestation/origin clocks, unresolved answers, attributed conjecture and translation dates.')
    changes = [
        ('missing-origin', 0, 'CLOCK_MISSING',
         'An attested synthetic witness cannot replace the required explicit unknown origin clock.',
         lambda r: r.pop('origin')),
        ('translation-backdated', 5, 'TRANSLATION_CLOCK',
         'The target wording cannot acquire its earlier source-language witness date.',
         lambda r: r['attestation'].update(value=r['translation']['source_attestation'])),
        ('conjecture-promoted', 4, 'EDITORIAL_CONFLICT',
         'Conjectured wording must not silently replace the damaged transmitted wording.',
         lambda r: r.update(wording=r['editorial']['conjectured_wording'])),
        ('ambiguous-answer-selected', 3, 'SOLUTION_CONFLICT',
         'An unresolved riddle cannot simultaneously have boat selected as its answer.',
         lambda r: r['solutions'].update(selected='boat')),
        ('origin-promoted-from-witness', 0, '*',
         'Independent creative-packet expectation: an unknown origin must not become the surviving witness date merely by copying it. Any structured refusal suffices; this expectation is outside the frozen counter.',
         lambda r: r['origin'].update(value=r['attestation']['value'])),
    ]
    for name, index, finding, relationship, change in changes:
        value = copy.deepcopy(packet)
        change(value['records'][index])
        yield (name, (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode(),
               1, finding, relationship)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tool', required=True, type=Path)
    parser.add_argument('--work', required=True, type=Path)
    args = parser.parse_args()
    tool = args.tool.resolve()
    work = args.work.resolve()
    if not tool.is_file() or not work.is_dir():
        parser.error('--tool must be a file and --work must be an existing isolated directory')
    packet_file = Path(__file__).resolve().with_name('craft.json')
    raw = packet_file.read_bytes()
    if digest(raw) != PACKET_SHA256:
        parser.error('craft.json differs from the pinned byte-faithful inherited packet')
    packet = json.loads(raw)
    candidate = tool.read_bytes()
    rows = []
    with tempfile.TemporaryDirectory(prefix='domain-trial-', dir=work) as temporary:
        run_dir = Path(temporary)
        (run_dir / 'candidate.py').write_bytes(candidate)
        for name, case_raw, expected_rc, expected_id, relationship in trial_cases(packet, raw):
            filename = name + '.json'
            (run_dir / filename).write_bytes(case_raw)
            command = [sys.executable, '-B', 'candidate.py', '--packet', filename, '--json']
            row = dict(case=name, relationship=relationship,
                       packet_sha256=digest(case_raw), command=command, cwd='$ISOLATED_WORK',
                       expected_rc=expected_rc, expected_finding=expected_id)
            try:
                result = subprocess.run(command, cwd=run_dir, capture_output=True, timeout=15)
                stdout = result.stdout.decode('utf-8', errors='replace')
                stderr = result.stderr.decode('utf-8', errors='replace')
                try:
                    body = json.loads(stdout)
                except ValueError:
                    body = None
                findings = body.get('findings') if isinstance(body, dict) else None
                ids = [f.get('id') for f in findings if isinstance(f, dict)] if isinstance(findings, list) else []
                matches = result.returncode == expected_rc and isinstance(body, dict)
                if expected_id == '*':
                    matches = matches and bool(ids)
                elif expected_id:
                    matches = matches and expected_id in ids
                else:
                    matches = matches and body.get('records') == 6 and findings == []
                row.update(rc=result.returncode, stdout=stdout, stderr=stderr,
                           stdout_sha256=digest(result.stdout), stderr_sha256=digest(result.stderr),
                           observed_findings=ids, matched_expected=bool(matches))
            except subprocess.TimeoutExpired as exc:
                out = exc.stdout or b''
                err = exc.stderr or b''
                row.update(rc=None, error='timeout after 15 seconds',
                           stdout=out.decode('utf-8', errors='replace'),
                           stderr=err.decode('utf-8', errors='replace'),
                           stdout_sha256=digest(out), stderr_sha256=digest(err),
                           matched_expected=False)
            rows.append(row)
    receipt = dict(label='R87_INHERITED_CREATIVE_PACKET_TRIAL',
                   axes=['operability', 'fixture fidelity', 'evidence durability', 'scope preservation'],
                   boundary='Audit of inherited six-record NON-CANON creative packet only; not historical evidence, semantic truth, lore acceptance, or the frozen 12-case counter.',
                   source_revision=BASE, source_path=SOURCE,
                   packet_sha256=digest(raw), candidate_sha256=digest(candidate),
                   runner_sha256=digest(Path(__file__).read_bytes()),
                   python_version=sys.version, matched=sum(row['matched_expected'] for row in rows),
                   total=len(rows), cases=rows)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0 if receipt['matched'] == receipt['total'] else 1


if __name__ == '__main__':
    sys.exit(main())
