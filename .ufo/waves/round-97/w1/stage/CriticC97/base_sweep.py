#!/usr/bin/env python3
"""CriticC97: re-run the frozen C8 sweep semantics over the BASE tree.
Read-only: input comes from `git show base:path`. Same surface rule as
predispatch.py sweep_owners: lines starting '- topic:' or markdown headings.
Also prints every surface line containing a phrase, and a full-prose hit list
with file:line for substantive-hit inspection."""
import re, subprocess, sys

BASE = '1ffc5a83d2c70e3bc581594efbcf32c562ba2569'
PHRASES = ['verbal duel', 'ritual insult', 'flyting', 'song duel', 'boast formula',
           'audience adjudication']

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

ls = subprocess.run(['git', 'ls-tree', '-r', '--name-only', BASE, '--', 'corpus/knowledge'],
                    capture_output=True, text=True, check=True)
files = [l for l in ls.stdout.splitlines() if l.endswith('.md')]
print(f'base knowledge md files: {len(files)}')

owners = []
surface_hits = []
prose_hits = []
for rel in files:
    txt = subprocess.run(['git', 'show', f'{BASE}:{rel}'], capture_output=True,
                         text=True, check=True).stdout
    for i, line in enumerate(txt.splitlines(), 1):
        s = line.strip()
        is_surface = s.startswith('- topic:') or bool(re.match(r'^#{1,6}\s', s))
        n = norm(s)
        for p in PHRASES:
            np_ = norm(p)
            if np_ in n:
                if is_surface:
                    owners.append(rel)
                    surface_hits.append(f'{rel}:{i}: {s[:160]}')
                else:
                    prose_hits.append(f'{rel}:{i}: [{p}] {s[:160]}')
                break

owners = sorted(set(owners))
print(f'C8 sweep owners at base: {len(owners)} -> {owners}')
print(f'surface hits: {len(surface_hits)}')
for h in surface_hits:
    print('  SURFACE ' + h)
print(f'prose/table hits (mentions, not ownership): {len(prose_hits)}')
for h in prose_hits:
    print('  MENTION ' + h)
sys.exit(0 if len(owners) == 0 else 1)
