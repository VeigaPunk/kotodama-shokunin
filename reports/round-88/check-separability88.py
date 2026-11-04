#!/usr/bin/env python3
"""Measure each frozen predicate on its own lands over the common freeze tree.

Writes only caller scratch; all Git mutation is confined to a verified sandbox.
The pre-dispatch omission of this check remains a procedural defect; a late
successful overlay run cannot backdate that evidence.
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

ap = argparse.ArgumentParser()
ap.add_argument('--root', type=pathlib.Path, required=True)
ap.add_argument('--lands', required=True)
ap.add_argument('--work', type=pathlib.Path, required=True)
ns = ap.parse_args()
freeze = '4b76524c51e1c2f76c99eeb3b629cfac08a44a76'
base = '4956282281dac1306cfbe59523e46dde99749d75'
rows = []
for claim, paths in [('O', ['tools/check-finding-sets.py']), ('D', ['corpus/knowledge/linguistics/numerals-and-measures.md', 'corpus/SOURCES.md'])]:
    scratch = pathlib.Path(tempfile.mkdtemp(prefix='overlay-' + claim + '-', dir=ns.work))
    repo = scratch / 'repo'
    try:
        subprocess.run(['git', 'clone', '--shared', '--no-checkout', str(ns.root), str(repo)], check=True, capture_output=True)
        subprocess.run(['git', '-C', str(repo), 'checkout', '--detach', freeze], check=True, capture_output=True)
        actual = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', '--show-toplevel'], text=True).strip()
        if pathlib.Path(actual).resolve() != repo.resolve():
            raise RuntimeError('sandbox root mismatch')
        for path in paths:
            data = subprocess.check_output(['git', '-C', str(ns.root), 'show', ns.lands + ':' + path])
            target = repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        subprocess.run(['git', '-C', str(repo), 'add', '--'] + paths, check=True, capture_output=True)
        subprocess.run(['git', '-C', str(repo), '-c', 'user.name=round88-fixture', '-c', 'user.email=fixture@invalid.local', 'commit', '-m', 'isolated ' + claim + ' overlay'], check=True, capture_output=True)
        revision = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
        command = [sys.executable, '-B', str(repo / 'reports/round-88/measure88.py'), '--root', str(repo), '--base', base, '--lands', revision, '--claim', claim, '--work', str(scratch)]
        run = subprocess.run(command, capture_output=True, text=True, env=dict(os.environ, KOTODAMA_ROOT=str(repo)))
        rows.append({'claim': claim, 'overlay_paths': paths, 'common_freeze': freeze, 'source_lands': ns.lands,
                     'sandbox_revision': revision, 'rc': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr})
    finally:
        shutil.rmtree(scratch)
print(json.dumps({'label': 'SEPARABILITY88', 'runs': rows}, indent=2))
sys.exit(0 if len(rows) == 2 and all(r['rc'] == 0 for r in rows) else 1)
