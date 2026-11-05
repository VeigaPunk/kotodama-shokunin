#!/usr/bin/env python3
"""Does a gate line bind to the round-95 rows as ExecRegistry95 staged them?

Three gate-quote choices per row, all exact single-occurrence substrings of the
committed capture, all <= 25 words:
  anchor  -- the anchor quote recorded in the registry row's anchor cell
  alt     -- a located span that is NOT contained in the row's teaches cell and
             shares >= 3 content words with it
The registry rows are the staged ExecRegistry95/SOURCES.append.md, unamended.

Read-only with respect to the lane; everything is written under --work.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

import importlib.util

spec = importlib.util.spec_from_file_location(
    'g', '/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/base-tool.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
STAGE = LANE + '/.ufo/waves/round-95/w1/stage'
REG = STAGE + '/ExecRegistry95/SOURCES.append.md'
EV = STAGE + '/ExecRegistry95/evidence'
ENTRY = STAGE + '/ScribeEntry95/funerary-lament-dirge-formulae.md'
AS_OF = '2026-11-05'

# Located spans chosen from the committed captures: exact single occurrence,
# <= 25 words, not contained in the teaches cell, >= 3 content words shared.
ALT = {
    'S970': 'the antiphonal way of performing Seto songs makes it possible for the lead singer',
    'S971': 'The antiphonal nature of voceru performance, though not discussed in detail here, suggests that Corsican lament served a similar',
    'S972': 'Although primal instinct may be at its core, the keen was a sacred improvised chant that evolved over many centuries.',
    'S973': 'keening woman—both representing and maintaining community Catholicism— was important in the role of the female professional mourner who performed ritualized laments.',
    'S974': 'Now, in a recitation, Sima praises the good deeds and grace of the deceased, beseeching Pridon to take good care, in',
}

HEADER = ('| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'
          '|---|---|---|---|---|---|---|---|---|---|---|')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work', required=True)
    ap.add_argument('--tool', default='/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/base-tool.py')
    ap.add_argument('--mode', default='alt', choices=('anchor', 'alt'))
    a = ap.parse_args()
    work = os.path.abspath(a.work)
    root = os.path.join(work, 'tree')
    shutil.rmtree(root, ignore_errors=True)
    for d in ('corpus/knowledge/linguistics', 'corpus/lessons', 'reports/round-95/evidence'):
        os.makedirs(os.path.join(root, d))
    os.makedirs(os.path.join(work, 'tmp'))

    rows = []
    for line in open(REG, encoding='utf-8'):
        if re.match(r'^\|\s*S\d{3,}\s*\|', line):
            rows.append([c.strip() for c in line.rstrip('\n').strip('|').split('|')])
    with open(os.path.join(root, 'corpus', 'SOURCES.md'), 'w', encoding='utf-8') as fh:
        fh.write(HEADER + '\n')
        for c in rows:
            fh.write('| ' + ' | '.join(c) + ' |\n')
    with open(os.path.join(root, 'corpus', 'SOURCES.base.md'), 'w', encoding='utf-8') as fh:
        fh.write(HEADER + '\n')
    shutil.copy(ENTRY, os.path.join(root, 'corpus', 'knowledge', 'linguistics',
                                    'funerary-lament-dirge-formulae.md'))

    man_rows = {}
    lesson = []
    for c in rows:
        rid = c[0]
        url = g.urls(c[1])[-1]
        aq = re.search(r'anchor quote "([^"]*)"', c[5]).group(1)
        quote = aq if a.mode == 'anchor' else ALT[rid]
        cap = 'reports/round-95/evidence/%s.txt' % rid
        shutil.copy(os.path.join(EV, rid + '.txt'), os.path.join(root, cap))
        data = open(os.path.join(root, cap), 'rb').read()
        man_rows[rid] = dict(capture=cap, url=url, http_status=200,
                             fetched_at='2026-11-05T12:00:00-03:00',
                             sha256=hashlib.sha256(data).hexdigest(), quote=aq)
        lesson.append('| %s | %s | %s | 200 | “%s” | sha256 |' % (rid, url, AS_OF, quote))
    with open(os.path.join(root, 'corpus', 'lessons', 'round-95.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lesson) + '\n')
    if os.environ.get('NO_MANIFEST_ROWS') != '1':
        with open(os.path.join(root, 'reports', 'round-95', 'evidence', 'manifest.json'), 'w',
                  encoding='utf-8') as fh:
            json.dump({'as_of': AS_OF, 'rows': man_rows}, fh, indent=1, ensure_ascii=False)

    cmd = [sys.executable, '-B', a.tool, '--root', root, 'entry',
           '--entry', os.path.join(root, 'corpus', 'knowledge', 'linguistics',
                                   'funerary-lament-dirge-formulae.md'),
           '--base-registry', os.path.join(root, 'corpus', 'SOURCES.base.md'),
           '--lands-registry', os.path.join(root, 'corpus', 'SOURCES.md'),
           '--lesson', os.path.join(root, 'corpus', 'lessons', 'round-95.md'),
           '--manifest', os.path.join(root, 'reports', 'round-95', 'evidence', 'manifest.json'),
           '--capture-dir', 'reports/round-95/evidence',
           '--as-of', AS_OF,
           '--topic', 'funerary laments and dirges: the sung speech of mourning — professional keeners '
                      'and lament genres, antiphonal and refrain structures, formulaic grief content '
                      '(praise of the dead, address to the dead, blame and consolation), gendered '
                      'mourning rules, the lament between speech and song, and the design procedure '
                      'for a fictional mourning register',
           '--topic-phrases', 'professional keeners;antiphonal lament;lament refrain;'
                              'praise of the dead;gendered mourning rules;fictional mourning register',
           '--min-topic-phrases', '4', '--min-bytes', '12000', '--min-headings', '6',
           '--min-new-ids', '3', '--min-topic-overlap', '8', '--table-min-rows', '5',
           '--table-min-cols', '3',
           '--base-lesson', os.path.join(root, 'corpus', 'lessons', 'round-95.md'),
           '--graded', 'corpus/SOURCES.md', '--graded', 'corpus/lessons/round-95.md',
           '--min-anchor-span', '3', '--min-gate-overlap', '3']
    env = dict(os.environ, TMPDIR=os.path.join(work, 'tmp'))
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=work)
    print('mode=%s tool=%s' % (a.mode, os.path.basename(a.tool)))
    print('rc=', p.returncode)
    out = ((p.stdout or '') + (p.stderr or '')).strip()
    for line in out.splitlines():
        print(' ', line[:240])
    return 0


if __name__ == '__main__':
    sys.exit(main())
