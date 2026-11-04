#!/usr/bin/env python3
"""ExecBoundary r86 pre-dispatch control probes over the FROZEN counter.

Read-only against the lane repo (git -C ... show/cat-file/rev-list/diff only).
The only git writes anywhere are the frozen counter's own isolated selftest
fixtures inside --work (TemporaryDirectory under this scratch dir).
Emits probes-summary.json next to itself. Modifies nothing in the lane.
"""
import hashlib, json, subprocess, sys, os
from pathlib import Path

LANE = Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
SCRATCH = Path('/fast/scratch/hyaku/kotodama-r86/ExecBoundary')
FR = '16c267832746e1cb98fb42a56180f8d1d12dc18b'
BA = '1e6b10a02b93a981b012987c51399d278fe37fa9'
CFG_PATH = 'reports/round-86/claims.json'
ENTRY = 'corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md'
TOOL = 'tools/check-paragraph-locator.py'
LINT = 'tools/check-cited-lines.py'
IRON = 'reports/round-86/evidence/Iron.html'

def g(*args):
    return subprocess.run(['git', '-C', str(LANE), *args], capture_output=True)

def gout(*args):
    p = g(*args)
    return p.stdout.decode('utf-8', 'replace').strip()

def blob(rev, path):
    p = g('show', f'{rev}:{path}')
    return p.stdout if p.returncode == 0 else None

def sha(b):
    return hashlib.sha256(b).hexdigest()

def snapshot():
    return {
        'HEAD': gout('rev-parse', 'HEAD'),
        'porcelain': gout('status', '--porcelain'),
        'count_objects': gout('count-objects', '-v'),
    }

def main():
    (SCRATCH / 'frozen').mkdir(parents=True, exist_ok=True)
    (SCRATCH / 'work').mkdir(parents=True, exist_ok=True)
    (SCRATCH / 'probes').mkdir(parents=True, exist_ok=True)
    out = {'probe_runner': 'ExecBoundary run_probes.py', 'versions': {
        'python3': subprocess.run([sys.executable, '-V'], capture_output=True, text=True).stdout.strip(),
        'git': gout('--version'),
    }}

    # 1. Extract frozen counter + frozen claims from the freeze blob.
    fr_py = blob(FR, 'reports/round-86/measure86.py')
    fr_cfg = blob(FR, CFG_PATH)
    assert fr_py and fr_cfg, 'frozen counter/claims absent at freeze'
    (SCRATCH / 'frozen' / 'measure86.py').write_bytes(fr_py)
    (SCRATCH / 'frozen' / 'claims.json').write_bytes(fr_cfg)
    out['frozen_counter_sha256'] = sha(fr_py)
    out['frozen_counter_sha_matches_L1_capture'] = out['frozen_counter_sha256'] == '15cf54126850d7f16acaec1cc22174a4a6319107752c7b9ee6028473158f19fe'
    out['frozen_claims_sha256'] = sha(fr_cfg)

    cfg = json.loads(fr_cfg)
    out['cfg'] = {k: cfg[k] for k in ('base', 'date', 'counter', 'lint_sha256')}
    out['cfg']['claims'] = {c: {k: v for k, v in cfg['claims'][c].items() if k in ('entry', 'tool', 'ids', 'legs', 'html', 'quote', 'min_bytes')} for c in ('D', 'O')}
    out['cfg_base_matches_assignment'] = cfg['base'] == BA

    # 2. Blob existence matrix at base/freeze/HEAD.
    HEAD = gout('rev-parse', 'HEAD')
    paths = ['reports/round-86/measure86.py', CFG_PATH, LINT, TOOL, ENTRY, 'corpus/SOURCES.md', 'SKILL.md', IRON, 'corpus/README.md']
    out['existence'] = {rev: {p: blob(rev, p) is not None for p in paths} for rev in (BA, FR, HEAD)}
    out['chain'] = {
        'freeze_in_first_parent_HEAD': FR in gout('rev-list', '--first-parent', HEAD).split(),
        'freeze_in_first_parent_freeze': FR in gout('rev-list', '--first-parent', FR).split(),
        'base_in_first_parent_freeze': BA in gout('rev-list', '--first-parent', FR).split(),
    }

    # 3. Lint authority: pinned sha vs freeze blob.
    lint_blob = blob(FR, LINT)
    out['lint_authority'] = {
        'freeze_blob_present': lint_blob is not None,
        'freeze_blob_sha256': sha(lint_blob) if lint_blob else None,
        'pinned_sha256': cfg['lint_sha256'],
        'match': bool(lint_blob) and sha(lint_blob) == cfg['lint_sha256'],
    }

    # 4. Post-freeze counter drift (freeze vs HEAD) in reports/round-86.
    diff = g('diff', FR, HEAD, '--', 'reports/round-86/')
    (SCRATCH / 'frozen' / 'head-vs-freeze-reports.diff').write_bytes(diff.stdout or b'')
    out['post_freeze_drift'] = {
        'numstat': gout('diff', '--numstat', FR, HEAD, '--', 'reports/round-86/'),
        'claims_blob_unchanged': blob(FR, CFG_PATH) == blob(HEAD, CFG_PATH),
        'counter_blob_unchanged': fr_py == blob(HEAD, 'reports/round-86/measure86.py'),
    }

    # 5. Registry signals in SKILL.md at freeze/HEAD.
    out['registry_scan'] = {}
    for rev in (FR, HEAD):
        s = (blob(rev, 'SKILL.md') or b'').decode('utf-8', 'replace')
        out['registry_scan'][rev[:8]] = {
            'mentions_tool_path': TOOL in s,
            'mentions_paragraph_locator': 'paragraph-locator' in s,
        }

    # 6. Lane snapshot before probes.
    before = snapshot()
    out['lane_snapshot_before'] = before

    # 7. Probe matrix over the frozen counter copy (bytes-identical to freeze blob).
    counters = str(SCRATCH / 'frozen' / 'measure86.py')
    WORK = str(SCRATCH / 'work')
    HEADTREE = gout('rev-parse', 'HEAD^{tree}')
    probes = [
        ('P01_unchanged_base_D', ['--lands', BA, '--freeze', FR, '--claim', 'D']),
        ('P02_unchanged_base_O', ['--lands', BA, '--freeze', FR, '--claim', 'O']),
        ('P03_freeze_lands_D', ['--lands', FR, '--freeze', FR, '--claim', 'D']),
        ('P04_freeze_lands_O', ['--lands', FR, '--freeze', FR, '--claim', 'O']),
        ('P05_head_lands_D', ['--lands', HEAD, '--freeze', FR, '--claim', 'D']),
        ('P06_head_lands_O', ['--lands', HEAD, '--freeze', FR, '--claim', 'O']),
        ('P07_short_rev', ['--lands', HEAD[:7], '--freeze', FR, '--claim', 'D']),
        ('P08_tree_as_lands', ['--lands', HEADTREE, '--freeze', FR, '--claim', 'D']),
        ('P09_unknown_rev', ['--lands', '0' * 40, '--freeze', FR, '--claim', 'D']),
        ('P10_ancestry_flip', ['--lands', BA, '--freeze', HEAD, '--claim', 'D']),
        ('P11_base_as_freeze', ['--lands', HEAD, '--freeze', BA, '--claim', 'D']),
        ('P12_missing_work', ['--lands', FR, '--freeze', FR, '--claim', 'D', '--work', '/nonexistent/ExecBoundary-work']),
        ('P13_symmetric_ancestry', ['--lands', FR, '--freeze', HEAD, '--claim', 'O']),
        ('P14_head_as_freeze', ['--lands', HEAD, '--freeze', HEAD, '--claim', 'D']),
    ]
    out['probes'] = []
    for name, extra in probes:
        cmd = ['python3', '-B', counters, '--root', str(LANE), '--work', WORK] + extra
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120, cwd=str(SCRATCH))
        rec = {'name': name, 'cmd': cmd[2:], 'exit': p.returncode,
               'stdout': p.stdout, 'stderr': p.stderr}
        (SCRATCH / 'probes' / f'{name}.out').write_text(p.stdout)
        (SCRATCH / 'probes' / f'{name}.err').write_text(p.stderr)
        (SCRATCH / 'probes' / f'{name}.rc').write_text(str(p.returncode))
        out['probes'].append(rec)

    # 8. Clean-first counter selftest (frozen counter's own isolated fixtures under work/).
    cmd = ['python3', '-B', counters, '--selftest', '--work', WORK]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=str(SCRATCH))
    out['selftest'] = {'cmd': cmd[2:], 'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
    (SCRATCH / 'probes' / 'selftest.out').write_text(p.stdout)
    (SCRATCH / 'probes' / 'selftest.err').write_text(p.stderr)
    leftovers = [x.name for x in (SCRATCH / 'work').iterdir()]
    out['selftest_leftovers_in_work'] = leftovers

    # 9. Lane snapshot after probes; must be identical.
    after = snapshot()
    out['lane_snapshot_after'] = after
    out['lane_unmutated'] = (
        before['HEAD'] == after['HEAD']
        and before['porcelain'] == after['porcelain']
        and before['count_objects'] == after['count_objects']
    )

    (SCRATCH / 'probes-summary.json').write_text(json.dumps(out, indent=1))
    # Compact console digest.
    for r in out['probes']:
        first = r['stdout'].strip().splitlines()[-1] if r['stdout'].strip() else (r['stderr'].strip() or '<no output>')
        print(f"{r['name']}: exit={r['exit']} :: {first[:150]}")
    print(f"selftest: exit={out['selftest']['exit']} tail={out['selftest']['stdout'].strip().splitlines()[-1] if out['selftest']['stdout'].strip() else '<none>'}")
    print(f"frozen_counter_sha256={out['frozen_counter_sha256']} matches_L1={out['frozen_counter_sha_matches_L1_capture']}")
    print(f"lint_authority_match={out['lint_authority']['match']}")
    print(f"lane_unmutated={out['lane_unmutated']} leftovers={out['selftest_leftovers_in_work']}")
    print(f"post_freeze_drift numstat: {out['post_freeze_drift']['numstat']!r} claims_unchanged={out['post_freeze_drift']['claims_blob_unchanged']} counter_unchanged={out['post_freeze_drift']['counter_blob_unchanged']}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
