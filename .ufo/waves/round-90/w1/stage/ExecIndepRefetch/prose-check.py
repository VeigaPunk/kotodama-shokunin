#!/usr/bin/env python3
"""Classify every admitted gate quote as PROSE or CHROME before it lands.

Entry mode's GATE leg (frozen) checks length, url and date only, and CAPTURE only asks that the
quote occur in the capture - where a page's own <title> lives. So a title or nav string passes the
frozen predicate. This is the non-frozen companion check L1 asked for.

    python3 -B prose-check.py --manifest <manifest.json> [--lesson <file>] [--registry <file>]
    python3 -B prose-check.py --selfcheck        # runs on the known chrome traps, no manifest needed

A quote is CHROME when, after the grader's own normalisation, it is
  (a) the capture's <title> text,
  (b) inside the first 200 characters of the capture (the nav/chrome band), or
  (c) the row's own source cell.
Otherwise it is PROSE. Exit 0 all PROSE, 1 any CHROME, 2 nothing to check.
"""
import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CAPS = os.path.join(HERE, 'caps')


def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).replace('\u2019', "'")
    s = ' '.join(s.split()).casefold()
    return re.sub(r'\s+([.,;:!?%\)\]])', r'\1', s)


def title_of(raw):
    m = re.search(r'<title>(.*?)</title>', raw, re.S | re.I)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


def classify(quote, raw, source_cell=''):
    q = norm(quote)
    if not q:
        return 'EMPTY', 'no quote'
    title = norm(title_of(raw))
    if title and q in title:
        return 'CHROME', 'quote is the capture <title>'
    band = norm(raw)[:200]
    if q in band:
        return 'CHROME', 'quote sits in the first 200 chars (nav/chrome band)'
    if source_cell and q in norm(source_cell):
        return 'CHROME', 'quote is the row source cell'
    if q in norm(raw):
        return 'PROSE', 'located prose span'
    return 'ABSENT', 'quote not in this capture'


def rows_from_manifest(path):
    man = json.load(open(path, encoding='utf-8'))
    return man.get('rows', man)


def registry_cells(path):
    out = {}
    if not path or not os.path.isfile(path):
        return out
    for line in open(path, encoding='utf-8', errors='replace'):
        m = re.match(r'^ {0,3}\|[ ]*(S\d{3,})[ ]*\|', line)
        if m:
            out[m.group(1)] = [c.strip() for c in line.strip().strip('|').split('|')]
    return out


def lesson_quotes(path):
    out = {}
    if not path or not os.path.isfile(path):
        return out
    text = open(path, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'^[-*] ?(S\d{3,})\b.*?[\u201c"]([^\u201d"]+)[\u201d"]', text, re.M):
        out.setdefault(m.group(1), m.group(2).strip())
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest')
    ap.add_argument('--lesson')
    ap.add_argument('--registry')
    ap.add_argument('--selfcheck', action='store_true')
    ap.add_argument('--receipt')
    a = ap.parse_args(argv)
    fetch = json.load(open(os.path.join(HERE, 'fetch.json'), encoding='utf-8'))
    by_url = {v['url']: k for k, v in fetch['captures'].items()}
    cands = json.load(open(os.path.join(HERE, 'quote-candidates.json'), encoding='utf-8'))
    lines = []
    if a.selfcheck:
        for rid, rec in sorted(cands.items()):
            raw = open(os.path.join(HERE, rec['prose_candidates'][0]['capture']),
                       encoding='utf-8', errors='replace').read()
            v, why = classify(rec['chrome_trap'], raw)
            lines.append(f'{rid} {v} ({why}) quote={rec["chrome_trap"]!r}')
            for c in rec['prose_candidates']:
                r2 = open(os.path.join(HERE, c['capture']), encoding='utf-8', errors='replace').read()
                v2, why2 = classify(c['quote'], r2)
                lines.append(f'    candidate {v2} ({why2}) quote={c["quote"][:90]!r}')
        verdict = 'SELFCHECK'
    elif not a.manifest or not os.path.isfile(a.manifest):
        print('PROSE-CHECK: no manifest - nothing to classify (not a pass)')
        return 2
    else:
        rows = rows_from_manifest(a.manifest)
        gates = lesson_quotes(a.lesson)
        reg = registry_cells(a.registry)
        for rid, rec in sorted(rows.items()):
            if not isinstance(rec, dict):
                continue
            url = str(rec.get('url', '')).strip()
            slug = by_url.get(url)
            if not slug:
                lines.append(f'{rid} UNFETCHED (no independent capture of {url})')
                continue
            raw = open(os.path.join(CAPS, slug + '.txt'), encoding='utf-8', errors='replace').read()
            quote = str(rec.get('quote', '')).strip() or gates.get(rid, '')
            src = reg.get(rid, [''] * 12)[1] if rid in reg else ''
            v, why = classify(quote, raw, src)
            extra = ''
            if v == 'CHROME' and rid in cands:
                extra = ' | candidate prose span: ' + cands[rid]['prose_candidates'][0]['quote']
            lines.append(f'{rid} {v} ({why}) quote={quote!r}{extra}')
        verdict = 'PROSE-CHECK'
    out = '\n'.join(lines)
    print(out)
    chrome = [l for l in lines if re.match(r'^S\d+ CHROME', l)]
    print(f'{verdict}: {len(lines) - len(chrome)} prose-or-listed / {len(chrome)} CHROME')
    if a.receipt:
        with open(a.receipt, 'w') as f:
            f.write(out + '\n' + f'{verdict}: {len(chrome)} CHROME\n')
    return 1 if chrome else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
