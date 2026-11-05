#!/usr/bin/env python3
"""Pick a byte-exact gate quote per round-95 row: a substring of the RAW capture
bytes (no whitespace normalisation), <= 25 words, >= 20 chars, not contained in
the row's source cell or teaches cell, >= 4 content words shared with teaches.

Read-only; prints candidates.
"""
import importlib.util
import os
import re

spec = importlib.util.spec_from_file_location(
    'g', '/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/base-tool.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

REG = ('/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/'
       'ExecRegistry95/SOURCES.append.md')
EV = ('/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/'
      'ExecRegistry95/evidence')

for line in open(REG, encoding='utf-8'):
    if not re.match(r'^\|\s*S\d{3,}\s*\|', line):
        continue
    c = [x.strip() for x in line.rstrip('\n').strip('|').split('|')]
    rid, src, teaches = c[0], c[1], c[6]
    raw = open(os.path.join(EV, rid + '.txt'), encoding='utf-8', errors='replace').read()
    # candidate spans: maximal runs of non-newline text, cut into word windows
    segs = raw.split('\n')
    cands = []
    for seg in segs:
        w = seg.split()
        for L in range(5, 26):
            for start in range(0, max(0, len(w) - L + 1)):
                q = ' '.join(w[start:start + L])
                if len(q) < 25 or len(q.split()) > 25:
                    continue
                if raw.count(q) != 1:
                    continue
                if '"' in q or '“' in q or '”' in q:
                    continue
                if g.norm(q) in g.norm(teaches) or g.norm(q) in g.norm(src):
                    continue
                ov = g.overlap(q, teaches)
                if ov < 4:
                    continue
                cands.append((ov, len(q.split()), q))
    cands.sort(key=lambda t: (-t[0], t[1]))
    print('==', rid, 'candidates', len(cands))
    seen = set()
    n = 0
    for ov, wn, q in cands:
        if q in seen:
            continue
        seen.add(q)
        print('   ov=%d words=%d %r' % (ov, wn, q))
        n += 1
        if n >= 6:
            break
