#!/usr/bin/env python3
"""Round-97 C8 sweep control: shows the frozen content sweep (predispatch.py sweep_owners) is able
to fail. It replays the round-96 claim-C before-state ("zero owned file at base", taken by a
filename-only sweep) with the round-96 frozen phrases over the round-96 base tree read from git.
Expected: owners >= 1 (myth-symbol/binding-speech-complex.md carries `self-imprecation` in its
topic line and table rows), i.e. the sweep would have refused the round-96 zero-owner premise.
It also prints the round-97 phrase sweep over the round-97 base for the record.

Usage: python3 -B reports/round-97/sweep-control.py --root <lane git tree>
Exit 0 iff the round-96 replay finds >= 1 owner.
"""
import argparse
import importlib.util
import os
import subprocess
import sys

R96_BASE = '0539276c0e329743200b60e98bf289c540f78864'
R97_BASE = '1ffc5a83d2c70e3bc581594efbcf32c562ba2569'
R96_PHRASES = ['oath formula', 'blessing formula', 'curse formula', 'self-imprecation',
               'witness invocation', 'sanction clause']
R96_ENTRY = 'corpus/knowledge/linguistics/oath-blessing-curse-formulae.md'


def git_tree(root, rev):
    ls = subprocess.run(['git', '-C', root, 'ls-tree', '-r', '--name-only', rev, 'corpus/knowledge'],
                        capture_output=True, text=True, check=True).stdout.split('\n')
    out = {}
    for rel in ls:
        if rel.endswith('.md'):
            b = subprocess.run(['git', '-C', root, 'show', f'{rev}:{rel}'], capture_output=True, check=True).stdout
            out[rel] = b.decode('utf-8', errors='replace')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location('pd97', os.path.join(here, 'predispatch.py'))
    pd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pd)
    t96 = git_tree(a.root, R96_BASE)
    o96 = pd.sweep_owners(t96, R96_PHRASES, exclude=(R96_ENTRY,))
    print(f'R96-REPLAY base={R96_BASE} files={len(t96)} owners={len(o96)} {o96}')
    t97 = git_tree(a.root, R97_BASE)
    o97 = pd.sweep_owners(t97, pd.PHRASES, exclude=(pd.ENTRY_REL,))
    print(f'R97-BASE base={R97_BASE} files={len(t97)} owners={len(o97)} {o97}')
    ok = len(o96) >= 1
    print(f'SWEEP-CONTROL: {"PASS" if ok else "FAIL"} (round-96 replay must find >= 1 owner)')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
