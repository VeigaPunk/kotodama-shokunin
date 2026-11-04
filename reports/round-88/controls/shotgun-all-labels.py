#!/usr/bin/env python3
"""Label shotgun: runs the honest auditor, then replaces its findings with EVERY
label in the vocabulary on any dirty packet. Exit codes and the clean cases stay
correct, so a membership-only battery cannot tell it from an auditor that
actually attributes one finding. It never decides which label applies."""
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(os.environ.get('KOTODAMA_ROOT') or pathlib.Path(__file__).resolve().parents[2])
HONEST = ROOT / 'tools' / 'check-attestation-packet.py'
LABELS = ['RECORD_ID', 'CLOCK_MISSING', 'CLOCK_REASON', 'CLOCK_DATE', 'RECORD_FIELD',
          'SOLUTION_CONFLICT', 'EDITORIAL_CONFLICT', 'TRANSLATION_CLOCK']


def main():
    packet = sys.argv[sys.argv.index('--packet') + 1]
    run = subprocess.run([sys.executable, '-B', str(HONEST), '--packet', packet, '--json'],
                         capture_output=True, text=True)
    if run.returncode != 1:
        sys.stdout.write(run.stdout)
        sys.stderr.write(run.stderr)
        return run.returncode
    body = json.loads(run.stdout)
    body['findings'] = [dict(id=label, record='shotgun', detail='all labels emitted')
                        for label in LABELS]
    print(json.dumps(body, sort_keys=True, indent=2))
    return 1


if __name__ == '__main__':
    sys.exit(main())
