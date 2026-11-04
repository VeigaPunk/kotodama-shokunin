#!/usr/bin/env python3
"""ExecControls stage runner (round-88, O agreement environment).

Reproduces the committed prefreeze control scores and separates committed-byte
from live-tree evaluation. Read-only against the lane: trees are exported with
`git archive`, a scratch clone carries the tamper and fix experiments. The frozen
counter and frozen cases are never edited; the staged control fix is applied only
inside scratch-clone commits and copied here as a proposal.

Usage: python3 run_controls.py   (writes receipts under the scratch dir and copies
them into this stage directory)
"""
import hashlib
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tarfile

LANE = pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
SCRATCH = pathlib.Path('/fast/scratch/hyaku/kotodama-r88/ExecControls')
STAGE = pathlib.Path(__file__).resolve().parent
PRE = '0c8c733088df8c4f06770c9e714360eed7f29272'
FROZEN = '4b76524c51e1c2f76c99eeb3b629cfac08a44a76'
BASE = '4956282281dac1306cfbe59523e46dde99749d75'
HONEST = 'tools/check-attestation-packet.py'
CONTROLS = ['constant-pass', 'shotgun-all-labels', 'extra-id', 'filename-only']
SCORE_ORDER = ['honest', 'constant-pass', 'shotgun-all-labels', 'extra-id', 'filename-only']
EXPECT = [13, 3, 4, 4, 0]
INHERITED = [12, 3, 12, 12, 12]
ENV_NAME = 'ExecControls'
GIT_ENV = dict(os.environ, GIT_AUTHOR_NAME='ExecControls', GIT_AUTHOR_EMAIL='exec-controls@scratch.invalid',
               GIT_COMMITTER_NAME='ExecControls', GIT_COMMITTER_EMAIL='exec-controls@scratch.invalid')


def sh(args, cwd=None, env=None, check=False):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=env)
    if check and p.returncode != 0:
        raise SystemExit(f'FAILED {args}: rc={p.returncode} {p.stderr}')
    return p


def make_clone(name, rev):
    """Shared clone of the lane checked out detached at rev: a git repo whose working tree is rev."""
    dest = SCRATCH / 'clones' / name
    if dest.exists():
        shutil.rmtree(dest)
    sh(['git', 'clone', '--shared', '--quiet', str(LANE), str(dest)], check=True)
    assert_toplevel(dest)
    sh(['git', '-C', str(dest), 'checkout', '-q', '--detach', rev], check=True)
    return dest


def assert_toplevel(path):
    top = sh(['git', '-C', str(path), 'rev-parse', '--show-toplevel']).stdout.strip()
    if pathlib.Path(top).resolve() != pathlib.Path(path).resolve():
        raise SystemExit(f'host guard: {path} toplevel is {top}')


def measure(label, root, lands, work):
    """Run the FROZEN counter (from the 4b76 export) against a root and lands revision."""
    work.mkdir(parents=True, exist_ok=True)
    frozen_counter = TREES[FROZEN] / 'reports/round-88/measure88.py'
    p = sh(['python3', '-B', str(frozen_counter), '--root', str(root), '--lands', lands,
            '--claim', 'O', '--work', str(work)])
    try:
        body = json.loads(p.stdout)
    except ValueError:
        body = None
    scores = {}
    if body:
        for leg in body.get('legs', []):
            if leg['leg'].startswith('score:'):
                scores[leg['leg'][len('score:'):]] = leg['observed']
    row = [scores.get(k) for k in SCORE_ORDER]
    rec = dict(label=label, root=str(root), lands=lands, rc=p.returncode, stderr=p.stderr[-400:],
               scores=dict(zip(SCORE_ORDER, row)), score_vector=row, expect=EXPECT,
               matches_expect=row == EXPECT,
               finding=body.get('finding') if body else None,
               failed_legs=[l['leg'] for l in body.get('legs', []) if not l['passed']] if body else None,
               body=body)
    (SCRATCH / 'receipts' / f'{label}.json').write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(f"{label:34s} rc={p.returncode} vector={row} expect_ok={row == EXPECT}")
    return rec


def direct(label, tool, packet, cwd, env_extra=None, drop_env=('KOTODAMA_ROOT',)):
    env = {k: v for k, v in os.environ.items() if k not in drop_env}
    env.update(env_extra or {})
    p = subprocess.run(['python3', '-B', str(tool), '--packet', str(packet)], cwd=str(cwd),
                       capture_output=True, text=True, env=env)
    try:
        body = json.loads(p.stdout)
    except ValueError:
        body = None
    rec = dict(label=label, tool=str(tool), rc=p.returncode, stdout_ids=sorted(
        {f.get('id') for f in body.get('findings', [])}) if isinstance(body, dict) else None,
        stderr=p.stderr.strip()[-300:])
    (SCRATCH / 'receipts' / f'{label}.json').write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(f"{label:34s} rc={rec['rc']} ids={rec['stdout_ids']} stderr={rec['stderr'][:90]!r}")
    return rec


def materialise_work(work, files):
    work.mkdir(parents=True, exist_ok=True)
    for src in files:
        shutil.copy2(src, work / src.name)
    return work


def main():
    for d in ('receipts', 'work', 'clones'):
        (SCRATCH / d).mkdir(parents=True, exist_ok=True)
    global TREES
    TREES = {PRE: make_clone('pre', PRE), FROZEN: make_clone('frozen', FROZEN), BASE: make_clone('base', BASE)}
    # 1. the exported frozen counter and controls must match the lane's committed bytes
    lane_sum = sh(['sha256sum', str(LANE / 'reports/round-88/measure88.py')]).stdout.split()[0]
    exp_sum = sh(['sha256sum', str(TREES[FROZEN] / 'reports/round-88/measure88.py')]).stdout.split()[0]
    print('counter sha lane==frozen-export:', lane_sum == exp_sum, lane_sum)

    # 2. committed prefreeze and frozen revisions, plus live-tree and base-lands variants
    work = SCRATCH / 'work' / 'A'
    measure('A1-committed-PRE-lands-PRE', TREES[PRE], PRE, work / 'A1')
    measure('A2-committed-FROZEN-lands-FROZEN', TREES[FROZEN], FROZEN, work / 'A2')
    measure('A3-live-lane-lands-FROZEN', LANE, FROZEN, work / 'A3')
    measure('A4-live-lane-lands-PRE', LANE, PRE, work / 'A4')
    measure('A5-live-lane-lands-BASE', LANE, BASE, work / 'A5')
    measure('A6-committed-BASE-lands-BASE', TREES[BASE], BASE, work / 'A6')

    # 3. direct failure modes of the committed wrappers (no grader materialisation)
    packet_dir = SCRATCH / 'work' / 'B'
    packet_dir.mkdir(parents=True, exist_ok=True)
    dirty_packet = packet_dir / 'dirty.json'
    packet = json.loads(sh(['git', '-C', str(LANE), 'show', f'{BASE}:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json']).stdout)
    packet['records'][0]['id'] = packet['records'][1]['id']
    dirty_packet.write_text(json.dumps(packet))
    ctl = TREES[FROZEN] / 'reports/round-88/controls'
    direct('B1-committed-dir-no-env-shotgun', ctl / 'shotgun-all-labels.py', dirty_packet, packet_dir)
    mw = materialise_work(SCRATCH / 'work' / 'B2', [TREES[FROZEN] / HONEST, ctl / 'shotgun-all-labels.py', ctl / 'extra-id.py'])
    direct('B2-materialised-no-env-shotgun', mw / 'shotgun-all-labels.py', dirty_packet, mw)
    direct('B3-materialised-no-env-extra-id', mw / 'extra-id.py', dirty_packet, mw)
    fx = STAGE / 'controls-fixed'
    mwf = materialise_work(SCRATCH / 'work' / 'B4', [TREES[FROZEN] / HONEST, fx / 'shotgun-all-labels.py', fx / 'extra-id.py'])
    direct('B4-fixed-materialised-no-env-shotgun', mwf / 'shotgun-all-labels.py', dirty_packet, mwf)
    direct('B5-fixed-materialised-no-env-extra-id', mwf / 'extra-id.py', dirty_packet, mwf)
    direct('B6-fixed-committed-dir-no-env-shotgun', fx / 'shotgun-all-labels.py', dirty_packet, fx)

    # 4. scratch clone: tamper live honest, commit the control fix in the scratch repo only
    clone = make_clone('tamper', FROZEN)
    honest_live = clone / HONEST
    original = honest_live.read_text()
    tampered = original.replace("    findings = []\n",
                                "    findings = []\n    if records:\n        findings.append(dict(id='CLOCK_SCOPE', record='tamper', detail='live-only'))\n", 1)
    assert tampered != original, 'tamper anchor missing'
    honest_live.write_text(tampered)
    measure('C1-clone-tampered-live-lands-FROZEN', clone, FROZEN, SCRATCH / 'work' / 'C1')
    sh(['git', '-C', str(clone), 'checkout', '--', HONEST], check=True)

    assert_toplevel(clone)
    sh(['git', '-C', str(clone), 'checkout', '-q', '-b', 'r88-exec-controls-fix', FROZEN], check=True)
    for name in ('shotgun-all-labels.py', 'extra-id.py'):
        shutil.copy2(fx / name, clone / 'reports/round-88/controls' / name)
    sh(['git', '-C', str(clone), 'add', 'reports/round-88/controls'], check=True)
    sh(['git', '-C', str(clone), 'commit', '-q', '-m', 'scratch: exec-controls honest-path fix (not lane)'],
       env=GIT_ENV, check=True)
    fixed = sh(['git', '-C', str(clone), 'rev-parse', 'HEAD']).stdout.strip()
    print('fix commit (scratch clone only):', fixed)
    measure('C2-clone-fixed-committed-lands-FIXED', clone, fixed, SCRATCH / 'work' / 'C2')

    tampered2 = honest_live.read_text().replace("    findings = []\n",
                                                "    findings = []\n    if records:\n        findings.append(dict(id='CLOCK_SCOPE', record='tamper', detail='live-only'))\n", 1)
    honest_live.write_text(tampered2)
    measure('C3-clone-fixed-tampered-live-lands-FIXED', clone, fixed, SCRATCH / 'work' / 'C3')
    sh(['git', '-C', str(clone), 'checkout', '--', HONEST], check=True)

    # 5. counter self-test (transport only) and battery absence at the revisions
    st = sh(['python3', '-B', str(TREES[FROZEN] / 'reports/round-88/measure88.py'), '--root', str(LANE),
             '--selftest', '--work', str(SCRATCH / 'work')])
    (SCRATCH / 'receipts' / 'S1-counter-selftest.json').write_text(st.stdout)
    print('counter --selftest rc', st.returncode)

    # 6. copy receipts and proposal into the stage directory
    out = STAGE / 'receipts'
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(SCRATCH / 'receipts', out)
    diff = sh(['diff', '-u', str(TREES[FROZEN] / 'reports/round-88/controls/shotgun-all-labels.py'),
               str(fx / 'shotgun-all-labels.py')])
    diff2 = sh(['diff', '-u', str(TREES[FROZEN] / 'reports/round-88/controls/extra-id.py'),
                str(fx / 'extra-id.py')])
    (STAGE / 'controls-fixed.diff').write_text(diff.stdout + diff2.stdout)
    digests = {str(p.relative_to(STAGE)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted(STAGE.rglob('*')) if p.is_file() and 'receipts' not in p.parts}
    (out / 'stage-digests.json').write_text(json.dumps(digests, indent=2, sort_keys=True) + '\n')
    print('receipts copied to', out)


if __name__ == '__main__':
    sys.exit(main())
