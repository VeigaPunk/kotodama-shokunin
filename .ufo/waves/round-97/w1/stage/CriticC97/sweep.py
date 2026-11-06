#!/usr/bin/env python3
"""CriticC97: frozen-C8-semantics sweep over base (git show) or worktree (open()).
Usage: sweep.py base|work [root]
Read-only. Surfaces = lines starting '- topic:' or markdown headings (same as
predispatch.py sweep_owners). Prints owners, surface hits, and prose/table mentions."""
import os, re, subprocess, sys

PHRASES = ['verbal duel', 'ritual insult', 'flyting', 'song duel', 'boast formula',
           'audience adjudication']
BASE = '1ffc5a83d2c70e3bc581594efbcf32c562ba2569'

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

def load(rel, mode, root):
    if mode == 'base':
        return subprocess.run(['git', 'show', f'{BASE}:{rel}'], capture_output=True,
                              text=True, check=True).stdout
    return open(os.path.join(root, rel), encoding='utf-8', errors='replace').read()

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'work'
    root = sys.argv[2] if len(sys.argv) > 2 else '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
    if mode == 'base':
        ls = subprocess.run(['git', 'ls-tree', '-r', '--name-only', BASE, '--', 'corpus/knowledge'],
                            capture_output=True, text=True, check=True)
        files = [l for l in ls.stdout.splitlines() if l.endswith('.md')]
    else:
        files = []
        for d, _, fs in os.walk(os.path.join(root, 'corpus/knowledge')):
            for f in fs:
                if f.endswith('.md'):
                    files.append(os.path.relpath(os.path.join(d, f), root))
    print(f'{mode} knowledge md files: {len(files)}')
    owners, surface_hits, prose_hits = [], [], []
    for rel in sorted(files):
        txt = load(rel, mode, root)
        for i, line in enumerate(txt.splitlines(), 1):
            s = line.strip()
            is_surface = s.startswith('- topic:') or bool(re.match(r'^#{1,6}\s', s))
            n = norm(s)
            for p in PHRASES:
                if norm(p) in n:
                    (owners.append(rel), surface_hits.append(f'{rel}:{i}: {s[:200]}')) if is_surface \
                        else prose_hits.append(f'{rel}:{i}: [{p}] {s[:200]}')
                    break
    owners = sorted(set(owners))
    print(f'C8 owners: {len(owners)} -> {owners}')
    for h in surface_hits:
        print('  SURFACE ' + h)
    print(f'mentions (topic/heading non-owner surfaces excluded; prose+tables): {len(prose_hits)}')
    for h in prose_hits:
        print('  MENTION ' + h)
    return 0 if len(owners) == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
