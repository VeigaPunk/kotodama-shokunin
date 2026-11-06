#!/usr/bin/env python3
"""Round-100 FEASIBILITY reference for the table-support contract (L1-authored control, not the
lane tool). It exists only to show, before any seat runs, that battery100's expectations are
mutually consistent and reachable. The lane tool is tools/check-table-support.py (seat-built).

Contract (frozen in reports/round-100/claims.json, claim O):
  check-table-support.py --entry FILE --evidence DIR [--evidence DIR ...] [--root DIR] [--json]
"""
import argparse
import json
import os
import re
import sys
import unicodedata

WINDOW = 80
SUPPORT_NUM, SUPPORT_DEN = 3, 4   # a cell is supported when best * 4 >= total * 3
STOP = set('''about above after again against also although among another because been before being
below between both could does doing done down during each either even every from further have having
here hers herself himself into itself just like more most much must neither none only onto other
ought ours over same shall should since some such than that their theirs them themselves then there
these they this those though through thus till under until upon very were what when where whether
which while whom whose will with within without would your yours often rather still'''.split())
SID = re.compile(r'\bS\d{3,}\b')
PATH = re.compile(r'`([A-Za-z0-9_./-]+\.md):(\d+)(?:-(\d+))?`')
SEP = re.compile(r'^\s*\|[\s:\-|]+\|\s*$')
HEAD = re.compile(r'^\s*#{1,6}\s')


def fold(s):
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()


def toks(s):
    return re.findall(r'[a-z]+', fold(s))


def stem(t):
    if len(t) > 4 and t.endswith('ies'):
        return t[:-3] + 'y'
    if len(t) > 4 and t.endswith('es') and (t[-3] in 'sxz' or t[-4:-2] in ('ch', 'sh')):
        return t[:-2]
    if len(t) > 3 and t.endswith('s') and not t.endswith('ss'):
        return t[:-1]
    return t


def content(s):
    out = []
    for t in toks(s):
        if len(t) >= 4 and t not in STOP and t not in out:
            out.append(t)
    return out


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def label_words(label):
    return {t for t in toks(re.sub(r'[*_`]', '', label)) if len(t) >= 3 and t not in STOP and t != 'and'}


def tables(lines):
    i, n = 0, len(lines)
    while i < n - 1:
        if lines[i].strip().startswith('|') and SEP.match(lines[i + 1]):
            h = i
            j = i + 2
            rows = []
            while j < n and lines[j].strip().startswith('|'):
                rows.append(j)
                j += 1
            # caption: contiguous non-blank paragraph above the header
            k = h - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            cap = []
            while k >= 0 and lines[k].strip() and not HEAD.match(lines[k]) and not lines[k].strip().startswith('|'):
                cap.insert(0, lines[k])
                k -= 1
            # binding block: contiguous non-blank paragraph below the last row
            m = j
            while m < n and not lines[m].strip():
                m += 1
            bind = []
            while m < n and lines[m].strip() and not HEAD.match(lines[m]) and not lines[m].strip().startswith('|'):
                bind.append(lines[m])
                m += 1
            yield h, rows, ' '.join(cap), bind
            i = j
        else:
            i += 1


def window_best(words, text_toks):
    """max number of distinct cell stems inside any WINDOW consecutive tokens"""
    want = set(words)
    if not want or not text_toks:
        return 0
    best, cnt, have = 0, {}, 0
    st = [stem(t) for t in text_toks]
    for idx, s in enumerate(st):
        if s in want:
            cnt[s] = cnt.get(s, 0) + 1
            if cnt[s] == 1:
                have += 1
        if idx >= WINDOW:
            o = st[idx - WINDOW]
            if o in want:
                cnt[o] -= 1
                if cnt[o] == 0:
                    have -= 1
        best = max(best, have)
    return best


def check(entry_text, evdirs, root):
    lines = entry_text.splitlines()
    findings, scoped = [], 0
    for h, rows, cap, bind in tables(lines):
        if not re.search(r'\brecorded cases?\b', cap, re.I):
            continue
        scoped += 1
        header = cells(lines[h])
        texts_for_line = []
        seen_sid = set()
        for bl in bind:
            texts = []
            for sid in SID.findall(bl):
                path = next((os.path.join(d, sid + '.txt') for d in evdirs
                             if os.path.isfile(os.path.join(d, sid + '.txt'))), None)
                if path is None:
                    if sid not in seen_sid:
                        findings.append({'id': 'NO-CAPTURE', 'line': h + 1, 'sid': sid})
                        seen_sid.add(sid)
                    continue
                seen_sid.add(sid)
                texts.append(toks(open(path, encoding='utf-8', errors='replace').read()))
            for p, a, b in PATH.findall(bl):
                fp = os.path.join(root, 'corpus/knowledge', p) if root else None
                if not fp or not os.path.isfile(fp):
                    findings.append({'id': 'NO-PATH', 'line': h + 1, 'path': p})
                    continue
                src = open(fp, encoding='utf-8', errors='replace').read().splitlines()
                a, b = int(a), int(b or a)
                texts.append(toks('\n'.join(src[a - 1:b])))
            texts_for_line.append((set(toks(bl)), texts, bool(SID.findall(bl) or PATH.findall(bl))))
        for r in rows:
            c = cells(lines[r])
            lw = label_words(c[0])
            bound = [(t, cited) for tokset, t, cited in texts_for_line if lw & tokset]
            label = re.sub(r'[*_`]', '', c[0]).strip()
            if not bound or not any(cited for _, cited in bound):
                findings.append({'id': 'UNBOUND-ROW', 'line': r + 1, 'row': label})
                continue
            support = [t for ts, _ in bound for t in ts]
            allstems = {stem(x) for t in support for x in t}
            for ci, cell in enumerate(c[1:], start=1):
                words = content(cell)
                stems = list(dict.fromkeys(stem(w) for w in words))
                if not stems:
                    continue
                best = max((window_best(stems, t) for t in support), default=0)
                if best * 4 < len(stems) * 3:
                    absent = sorted({w for w in words if stem(w) not in allstems})
                    col = header[ci] if ci < len(header) else str(ci)
                    findings.append({'id': 'UNSUPPORTED-CELL', 'line': r + 1, 'row': label, 'col': col,
                                     'words': absent, 'best': best, 'total': len(stems)})
    return findings, scoped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--entry')
    ap.add_argument('--evidence', action='append', default=[])
    ap.add_argument('--root')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    if not a.entry or not os.path.isfile(a.entry):
        print(f'TABLE_SUPPORT_ERROR entry missing: {a.entry}')
        return 2
    if not a.evidence or any(not os.path.isdir(d) for d in a.evidence):
        print(f'TABLE_SUPPORT_ERROR evidence dir missing: {a.evidence}')
        return 2
    try:
        text = open(a.entry, encoding='utf-8').read()
    except UnicodeDecodeError:
        print('TABLE_SUPPORT_ERROR entry is not valid UTF-8')
        return 2
    f, s = check(text, a.evidence, a.root)
    if a.json:
        print(json.dumps({'findings': f, 'scoped_tables': s}, ensure_ascii=False))
    else:
        for x in f:
            print('FINDING ' + ' '.join(f'{k}={v}' for k, v in x.items()))
        print(f'TABLE-SUPPORT: {len(f)} finding(s) in {s} scoped table(s)')
    return 1 if f else 0


if __name__ == '__main__':
    sys.exit(main())
