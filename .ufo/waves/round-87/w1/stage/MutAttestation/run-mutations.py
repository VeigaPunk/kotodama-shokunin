#!/usr/bin/env python3
"""Run three exact branch-disable mutations without editing the candidate source."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

REVISION = '2a3b5643899c3520867ae930593cafef6ef19cad'
LANE = Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
STAGE = LANE / '.ufo/waves/round-87/w1/stage/MutAttestation'
SCRATCH = Path('/fast/scratch/hyaku/kotodama-r87/MutAttestation')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def run(command):
    try:
        result = subprocess.run(command, cwd=SCRATCH, capture_output=True,
                                text=True, timeout=120)
        return dict(command=command, rc=result.returncode,
                    stdout=result.stdout, stderr=result.stderr)
    except subprocess.TimeoutExpired as error:
        return dict(command=command, rc=None, timeout=True,
                    stdout=(error.stdout or b'').decode(errors='replace'),
                    stderr=(error.stderr or b'').decode(errors='replace'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--mutations', type=Path, required=True)
    args = parser.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    original = args.candidate.read_bytes()
    active = SCRATCH / 'candidate.py'
    active.write_bytes(original)
    (STAGE / 'pristine-candidate.py').write_bytes(original)
    mutations = json.loads(args.mutations.read_text())
    receipt = dict(axis='operability', revision=REVISION,
                   candidate_source=str(args.candidate),
                   baseline_sha256=digest(original), python=sys.version,
                   frozen_counter_sha256=digest((STAGE / 'frozen-measure87.py').read_bytes()),
                   frozen_claims_sha256=digest((STAGE / 'frozen-claims.json').read_bytes()),
                   probes=[])

    def detect(label):
        work = SCRATCH / label
        work.mkdir()
        return dict(sha256=digest(active.read_bytes()),
                    selftest=run([sys.executable, '-B', str(active), '--selftest', '--work', str(work)]),
                    battery=run([sys.executable, '-B', str(STAGE / 'frozen-measure87.py'),
                                 '--root', str(LANE), '--revision', REVISION,
                                 '--candidate', str(active), '--work', str(work)]))

    try:
        for mutation in mutations:
            name = mutation['name']
            old = mutation['old'].encode()
            new = mutation['new'].encode()
            if original.count(old) != 1:
                raise ValueError(f'{name}: exact original branch must occur once')
            probe = dict(mutant=name, expected_detector=mutation['expected_detector'],
                         old=mutation['old'], new=mutation['new'])
            receipt['probes'].append(probe)
            active.write_bytes(original)
            probe['pristine'] = detect(name + '-pristine')
            mutated = original.replace(old, new, 1)
            (STAGE / (name + '-mutant.py')).write_bytes(mutated)
            try:
                active.write_bytes(mutated)
                probe['mutated'] = detect(name + '-mutated')
            finally:
                active.write_bytes(original)
                probe['restored_sha256'] = digest(active.read_bytes())
            probe['restored'] = detect(name + '-restored')
            clean = all(probe[state][detector]['rc'] == 0
                        for state in ('pristine', 'restored')
                        for detector in ('selftest', 'battery'))
            probe['verdict'] = ('inconclusive' if not clean else
                                'killed' if any(probe['mutated'][d]['rc'] == 1
                                                for d in ('selftest', 'battery')) else
                                'survived' if all(probe['mutated'][d]['rc'] == 0
                                                  for d in ('selftest', 'battery')) else
                                'inconclusive')
            (STAGE / 'mutation-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    finally:
        active.write_bytes(original)
        receipt['final_restored_sha256'] = digest(active.read_bytes())
        receipt['exact_restoration'] = active.read_bytes() == original
        receipt['source_unchanged'] = args.candidate.read_bytes() == original
        (STAGE / 'restored-candidate.py').write_bytes(active.read_bytes())
        shutil.rmtree(SCRATCH)
        receipt['scratch_removed'] = not SCRATCH.exists()
        (STAGE / 'mutation-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
