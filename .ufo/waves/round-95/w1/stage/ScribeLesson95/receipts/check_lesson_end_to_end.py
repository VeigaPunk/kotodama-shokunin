#!/usr/bin/env python3
"""End-to-end check of the drafted lesson file against the grader in entry mode.

Builds a scratch mini-lane from ExecRegistry95's staged rows, the ScribeEntry95
entry draft and the staged captures, installs THE DRAFTED LESSON FILE as the
round lesson, and runs the grader (v5 base bytes and the v6 candidate) over it.

Read-only with respect to the lane; everything is written under --work.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

spec = importlib.util.spec_from_file_location(
    'g', '/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/base-tool.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
STAGE = LANE + '/.ufo/waves/round-95/w1/stage'
REG = STAGE + '/ExecRegistry95/SOURCES.append.md'
EV = STAGE + '/ExecRegistry95/evidence'
ENTRY = STAGE + '/ScribeEntry95/funerary-lament-dirge-formulae.md'
LESSON = STAGE + '/ScribeLesson95/round-95.md'
AS_OF = '2026-11-05'
HEADER = ('| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'
          '|---|---|---|---|---|---|---|---|---|---|---|')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work', required=True)
    ap.add_argument('--tool', required=True)
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
    shutil.copy(LESSON, os.path.join(root, 'corpus', 'lessons', 'round-95.md'))

    man = {}
    for c in rows:
        rid = c[0]
        url = g.urls(c[1])[-1]
        aq = re.search(r'anchor quote "([^"]*)"', c[5]).group(1)
        cap = 'reports/round-95/evidence/%s.txt' % rid
        shutil.copy(os.path.join(EV, rid + '.txt'), os.path.join(root, cap))
        data = open(os.path.join(root, cap), 'rb').read()
        man[rid] = dict(capture=cap, url=url, http_status=200,
                        fetched_at='2026-11-05T12:00:00-03:00',
                        sha256=hashlib.sha256(data).hexdigest(), quote=aq)
    with open(os.path.join(root, 'reports', 'round-95', 'evidence', 'manifest.json'), 'w',
              encoding='utf-8') as fh:
        json.dump({'as_of': AS_OF, 'rows': man}, fh, indent=1, ensure_ascii=False)

    cmd = [sys.executable, '-B', a.tool, '--root', root, 'entry',
           '--entry', os.path.join(root, 'corpus', 'knowledge', 'linguistics',
                                   'funerary-lament-dirge-formulae.md'),
           '--base-registry', os.path.join(root, 'corpus', 'SOURCES.base.md'),
           '--lands-registry', os.path.join(root, 'corpus', 'SOURCES.md'),
           '--lesson', os.path.join(root, 'corpus', 'lessons', 'round-95.md'),
           '--manifest', os.path.join(root, 'reports', 'round-95', 'evidence', 'manifest.json'),
           '--capture-dir', 'reports/round-95/evidence', '--as-of', AS_OF,
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
    print('tool:', os.path.basename(a.tool), 'sha256:',
          hashlib.sha256(open(a.tool, 'rb').read()).hexdigest()[:16])
    print('rc=', p.returncode)
    out = ((p.stdout or '') + (p.stderr or '')).strip()
    for line in out.splitlines():
        print(' ', line[:230])
    return 0


if __name__ == '__main__':
    sys.exit(main())
