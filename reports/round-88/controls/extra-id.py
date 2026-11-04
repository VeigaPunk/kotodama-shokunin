#!/usr/bin/env python3
"""Extra-id forger: emits the honest auditor's correctly attributed finding set
plus one more valid label on every dirty packet. Membership of the expected id
still holds, so only exact-set comparison can refuse it."""
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(os.environ.get('KOTODAMA_ROOT') or pathlib.Path(__file__).resolve().parents[2])
HONEST = ROOT / 'tools' / 'check-attestation-packet.py'


def main():
    packet = sys.argv[sys.argv.index('--packet') + 1]
    run = subprocess.run([sys.executable, '-B', str(HONEST), '--packet', packet, '--json'],
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
