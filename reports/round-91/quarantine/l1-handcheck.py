#!/usr/bin/env python3
"""Round-91 L1 hand-check of the kotodama slice of the shokuknow absent-defect register.

Adopt nothing: this script only produces a per-row verdict with the argv it used.
For every row it fetches the cited URL once (curl, plain HTTP, 30 s), strips tags
and normalises whitespace, then tests each span of the cited quote (split on
`<br>` and on the ellipsis) against the fetched text.

Verdict classes
  LOCATED      every fragment of every span occurs in the fetched body
  PARTIAL      some fragments occur, at least one does not
  ABSENT       the fetch succeeded and no fragment occurs
  UNREACHABLE  network error, timeout, TLS failure or a 4xx/5xx status
  UNVERIFIABLE the register row carries prose instead of a quote

Usage: python3 l1-quarantine-handcheck.py --out <dir> [--rows PATH]
"""
import argparse
import csv
import hashlib
import html
import os
import re
import subprocess
import time
import sys

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'


PUNCT_FOLD = str.maketrans({'\uff0c': ',', '\u3001': ',', '\u3002': '.', '\uff1a': ':',
                            '\uff1b': ';', '\uff08': '(', '\uff09': ')', '\u300c': '"',
                            '\u300d': '"', '\u300e': '"', '\u300f': '"', '\u2026': '...'})
PUNCT_FOLD.update()


def fold(s):
    s = s.translate(PUNCT_FOLD)
    s = s.replace('（', '(').replace('）', ')')
    s = re.sub(r'\s*([,\.:;])\s*', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def norm(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def fragments(cell):
    cell = cell.strip()
    if cell.startswith('`'):
        cell = cell[1:]
    if cell.endswith('`'):
        cell = cell[:-1]
    out = []
    for span in re.split(r'<br\s*/?>', cell):
        span = span.strip().strip('`').strip()
        if not span:
            continue
        for frag in re.split(r'…|\.\.\.', span):
            frag = norm(frag)
            if len(frag) >= 6:
                out.append(frag)
    return out


def fetch(url, cap, workdir):
    """Fetch once, retrying only transient failures (network error, 429, 5xx)."""
    dest = os.path.join(workdir, 'body')
    cmd = ['curl', '-sS', '-L', '--max-time', '45', '-A', UA, '-o', dest, '-w', '%{http_code}', url]
    last = (None, 'no attempt', 0, '')
    for attempt in range(3):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            last = (None, 'timeout', 0, '')
        else:
            code = (r.stdout or '').strip()
            if r.returncode != 0:
                last = (None, f'curl rc={r.returncode} {(r.stderr or "").strip()[:120]}', 0, '')
            elif not os.path.isfile(dest):
                last = (None, 'no body', 0, '')
            else:
                body = open(dest, 'rb').read()
                sha = hashlib.sha256(body).hexdigest()
                if re.match(r'^2\d\d$', code) or (code.isdigit() and int(code) not in (408, 429) and int(code) < 500):
                    return body, code, len(body), sha
                last = (body, code, len(body), sha)
        time.sleep(2 + 3 * attempt)
    return last


WALL_MARKERS = ('Client Challenge', 'JavaScript is disabled in your browser',
                'Please enable JavaScript', 'checking your browser',
                'Just a moment', 'cf-browser-verification', 'Access Denied',
                '请求过于频繁', '访问过于频繁', '人机验证')


def sniff_charset(raw):
    head = raw[:4096]
    m = re.search(rb'charset=["\']?\s*([A-Za-z0-9_\-]+)', head, re.I)
    if m:
        return m.group(1).decode('ascii', 'replace').lower()
    return 'utf-8'


def body_texts(path):
    """Return (kinds, texts): decoded raw text, tag-stripped text, and pdftotext text."""
    raw = open(path, 'rb').read()
    kinds = []
    texts = []
    if raw[:5] == b'%PDF-':
        kinds.append('pdf')
        try:
            r = subprocess.run(['pdftotext', '-q', '-enc', 'UTF-8', path, '-'],
                               capture_output=True, timeout=120)
            texts.append(norm(r.stdout.decode('utf-8', 'replace')))
        except Exception:
            kinds.append('pdf-extract-failed')
        return kinds, texts
    is_html = b'<html' in raw[:8192].lower() or b'<!doctype' in raw[:8192].lower() or b'<head' in raw[:8192].lower()
    kinds.append('html' if is_html else 'raw')
    cs = sniff_charset(raw)
    decoded = None
    order = [cs] + [e for e in ('utf-8', 'gb18030', 'euc_jp', 'shift_jis', 'big5') if e != cs]
    for enc in order:
        try:
            decoded = raw.decode(enc)
            break
        except (UnicodeDecodeError, LookupError):
            continue
    if decoded is None:
        decoded = raw.decode('latin-1', 'replace')
    kinds.append(f'charset:{cs}')
    text = norm(decoded)
    if any(m in decoded for m in WALL_MARKERS):
        kinds.append('wall')
    texts.append(text)
    return kinds, texts


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--rows', default='reports/round-91/quarantine/slice.tsv')
    ap.add_argument('--work', required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    os.makedirs(a.work, exist_ok=True)
    rows = list(csv.DictReader(open(a.rows, encoding='utf-8'), delimiter='\t'))
    recs = []
    counts = {}
    for row in rows:
        rid = row['id'].strip()
        url = row['url'].strip()
        cell = row['cited_quote_or_prose']
        frs = fragments(cell)
        workdir = os.path.join(a.work, rid)
        os.makedirs(workdir, exist_ok=True)
        if not frs:
            verdict, anchor, sha, status, size, kind = 'UNVERIFIABLE', '', '', '', 0, ''
        else:
            body, code, size, sha = fetch(url, None, workdir)
            if body is None:
                verdict, anchor, status, kind = 'UNREACHABLE', '', code, ''
            else:
                status = code
                kindlist, texts = body_texts(os.path.join(workdir, 'body'))
                kind = '+'.join(kindlist)
                joined = '\n'.join(texts)
                folded = fold(joined)
                hits = [f for f in frs if f in joined or fold(f) in folded]
                if not re.match(r'^2\d\d$', str(status)):
                    verdict, anchor = 'UNREACHABLE', ''
                elif 'wall' in kindlist:
                    verdict, anchor = 'UNREACHABLE', ''
                elif len(hits) == len(frs):
                    verdict = 'LOCATED'
                    anchor = hits[0][:200]
                elif hits:
                    verdict = 'PARTIAL'
                    anchor = hits[0][:200]
                else:
                    verdict = 'ABSENT'
                    anchor = ''
        counts[verdict] = counts.get(verdict, 0) + 1
        recs.append({'id': rid, 'round': row['round'], 'class': row['class'].strip('`'),
                     'verdict': verdict, 'http': status, 'body_kind': kind, 'bytes': size,
                     'body_sha256': sha, 'anchors_expected': len(frs), 'anchor': anchor, 'url': url})
        print(f'{rid}\t{verdict}\thttp={status}\tkind={kind}\tbytes={size}\tfrags={len(frs)}')
    out = os.path.join(a.out, 'l1-handcheck.tsv')
    with open(out, 'w', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(recs[0].keys()), delimiter='\t')
        w.writeheader()
        w.writerows(recs)
    summary = ', '.join(f'{k}={v}' for k, v in sorted(counts.items()))
    print(f'L1-HANDCHECK: rows={len(recs)} {summary}')
    print(f'receipt: {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
