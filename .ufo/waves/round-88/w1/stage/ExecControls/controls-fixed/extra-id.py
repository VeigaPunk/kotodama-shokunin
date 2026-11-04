#!/usr/bin/env python3
"""Extra-id forger: emits the honest auditor's correctly attributed finding set
plus one more valid label on every dirty packet. Membership of the expected id
still holds, so only exact-set comparison can refuse it.

The honest auditor is resolved in this order: the committed copy materialised
beside this wrapper by the grader (same revision, same work directory); then
KOTODAMA_ROOT/tools; then the nearest ancestor checkout holding tools/."""
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
HONEST_NAME = 'check-attestation-packet.py'


def honest_path():
    sibling = HERE / HONEST_NAME
    if sibling.is_file():
        return sibling
    if os.environ.get('KOTODAMA_ROOT'):
        return pathlib.Path(os.environ['KOTODAMA_ROOT']) / 'tools' / HONEST_NAME
    for ancestor in HERE.parents:
        if (ancestor / 'tools' / HONEST_NAME).is_file():
            return ancestor / 'tools' / HONEST_NAME
    return HERE / HONEST_NAME


def main():
    honest = honest_path()
    if not honest.is_file():
        print(f'CONTROL_HONEST_ABSENT {honest}', file=sys.stderr)
        return 2
    packet = sys.argv[sys.argv.index('--packet') + 1]
    run = subprocess.run([sys.executable, '-B', str(honest), '--packet', packet, '--json'],
                         capture_output=True, text=True)
    if run.returncode != 1:
        sys.stdout.write(run.stdout)
        sys.stderr.write(run.stderr)
        return run.returncode
    body = json.loads(run.stdout)
    body['findings'].append(dict(id='CLOCK_SCOPE', record='invented', detail='extra id'))
    print(json.dumps(body, sort_keys=True, indent=2))
    return 1


if __name__ == '__main__':
    sys.exit(main())
