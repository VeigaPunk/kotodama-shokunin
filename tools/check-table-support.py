#!/usr/bin/env python3
"""check-table-support.py — table-cell support checker (round 100, claim O).

Rule (frozen in reports/round-100/claims.json, claim O; closes lesson R99-M2,
a section-7 table cell that outran its capture while every frozen leg passed):

  * Scope: a markdown table (header row, separator row, data rows) whose
    caption — the contiguous non-blank, non-heading, non-table paragraph
    immediately above the header — matches /\\brecorded cases?\\b/i.
  * Binding: the contiguous non-blank, non-heading, non-table paragraph
    immediately below the last data row. Each line of it binds every row one of
    whose label tokens (first cell, *_` stripped, NFKD-folded lowercase
    [a-z]+ tokens of length >= 3, not in STOP, not 'and') equals a token of
    the line — token equality, never substring. A line's support is the
    capture <evidence>/<S-id>.txt (first evidence dir holding it) for each
    S\\d{3,} it carries, plus each backticked `path.md:a[-b]` it carries, read
    from <root>/corpus/knowledge/<path> lines a..b.
  * Support: content words of a non-label cell (NFKD-folded, combining marks
    dropped, lowercase [a-z]+ tokens of length >= 4 not in STOP,
    deduplicated) are stemmed by stem() (ies -> y; es after s/x/z/ch/sh;
    trailing s not ss). best = max over single support texts of the number of
    distinct cell stems inside any 80 consecutive tokens. The cell is
    supported iff best*4 >= total*3.
  * Findings: UNSUPPORTED-CELL {line, row, col (header cell text), words
    (folded cell words whose stem occurs in none of the row's support texts,
    sorted), best, total}; UNBOUND-ROW {line, row} when no binding line binds
    the row or none of those lines carries an S-id or path; NO-CAPTURE
    {line, sid} once per table; NO-PATH {line, path}. Each with line.

This checker measures lexical co-location, not meaning: a paraphrase with new
words can be flagged, and a cell built from capture words in a false order
can pass.

CLI:
  check-table-support.py --entry FILE --evidence DIR [--evidence DIR ...]
                         [--root DIR] [--json]
  check-table-support.py --selftest --work DIR    (fixtures only under --work)

--json prints one JSON object {findings: [...], scoped_tables: int}; text mode
prints one FINDING line each and `TABLE-SUPPORT: <n> finding(s) in <t> scoped
table(s)`. rc 1 when findings, 0 when none; rc 2 with a TABLE_SUPPORT_ERROR
line and no traceback on a missing, non-UTF-8 or unreadable entry, a
directory passed as --entry, a missing evidence dir or no --evidence, an
unreadable capture or support file, or a --work under /tmp.
"""
import argparse
import json
import os
import re
import subprocess
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


class ToolError(Exception):
    """Refusal / unreadable-input error: reported as TABLE_SUPPORT_ ERROR, rc 2."""


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
                try:
                    texts.append(toks(open(path, encoding='utf-8', errors='replace').read()))
                except OSError as e:
                    raise ToolError(f'capture unreadable: {sid}: {e}')
            for p, a, b in PATH.findall(bl):
                fp = os.path.join(root, 'corpus/knowledge', p) if root else None
                if not fp or not os.path.isfile(fp):
                    findings.append({'id': 'NO-PATH', 'line': h + 1, 'path': p})
                    continue
                try:
                    src = open(fp, encoding='utf-8', errors='replace').read().splitlines()
                except OSError as e:
                    raise ToolError(f'support file unreadable: {p}: {e}')
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


# ------------------------------------------------------------------ selftest
SELF_EVID = {
    'S9001': ('In the court the singer receives gifts from the chief and rewards from passers-by. '
              'Drummers recite titles of the king. Criticism of the chief is licensed in the song.'),
    'S9002': ('The leader calls each line and the rowing crew answers in chorus, keeping time with the '
              'oars.'),
    'S9003': 'chief ' + ' '.join(['lorem'] * 200) + ' bounty',
    'S9004': 'Each rally sang near the church and the box of drums held the oriki of the town.',
    'S9005': 'chief ' + ' '.join(['lorem'] * 30) + ' bounty',
}
REF_MD = '# Ref\nWeavers sing a slow song at the loom.\n'
CAP3 = '| tradition | singer | limit |'
SEP3 = '|---|---|---|'
REC = 'The columns are filled from the recorded cases this entry cites.'
COURT = '| Court | singer receives gifts | criticism of the chief is licensed |'
TOOL = os.path.abspath(__file__)


def st_entry(caption, header, sep, rows, bind, tail='## 2. Next\n\nText.\n'):
    out = ['# T', '', '## 1. Section', '', caption, '', header, sep] + rows + ['']
    if bind:
        out += bind + ['']
    return '\n'.join(out) + '\n' + tail


def fkey(f):
    i = f.get('id')
    if i in ('UNSUPPORTED-CELL', 'UNBOUND-ROW'):
        return (i, f.get('row'), f.get('col', '') if i == 'UNSUPPORTED-CELL' else '')
    if i == 'NO-CAPTURE':
        return (i, f.get('sid'), '')
    if i == 'NO-PATH':
        return (i, f.get('path'), '')
    return (str(i), '?', '?')


def st_fixture(work, name, text=None, evid=None, root=False, entry_dir=False):
    d = os.path.join(work, name)
    ev = os.path.join(d, 'ev')
    os.makedirs(ev, exist_ok=True)
    for k, v in dict(SELF_EVID, **(evid or {})).items():
        open(os.path.join(ev, k + '.txt'), 'w', encoding='utf-8').write(v)
    rt = os.path.join(d, 'root')
    os.makedirs(os.path.join(rt, 'corpus/knowledge/x'), exist_ok=True)
    open(os.path.join(rt, 'corpus/knowledge/x/ref.md'), 'w', encoding='utf-8').write(REF_MD)
    ent = os.path.join(d, 'entry.md')
    if entry_dir:
        os.makedirs(ent, exist_ok=True)
    elif text is not None:
        open(ent, 'w', encoding='utf-8').write(text)
    return d, ev, rt, ent


def st_run(args):
    return subprocess.run([sys.executable, '-B', TOOL] + args,
                          capture_output=True, text=True, timeout=60)


def st_json_pin(work, name, text, rc, keys, words=None, best=None, scoped=None,
                root=False, evid=None, raw=None):
    d, ev, rt, ent = st_fixture(work, name, text, evid, root)
    if raw is not None:
        open(ent, 'wb').write(raw)
    args = ['--entry', ent, '--evidence', ev]
    if root:
        args += ['--root', rt]
    args.append('--json')
    p = st_run(args)
    try:
        js = json.loads(p.stdout)
        fs = js['findings']
        got = sorted({fkey(f) for f in fs})
    except Exception as e:
        return False, f'rc={p.returncode} json-unparseable ({type(e).__name__})'
    ok = p.returncode == rc and got == sorted(set(keys)) and len(fs) == len(got)
    detail = f'rc={p.returncode} got={got}'
    for k, w in (words or {}).items():
        f = next((f for f in fs if fkey(f) == k), None)
        gw = sorted(f.get('words', [])) if f else None
        ok = ok and gw == sorted(w)
        detail += f' words={gw}'
    for k, (b, t) in (best or {}).items():
        f = next((f for f in fs if fkey(f) == k), None)
        ok = ok and f is not None and f.get('best') == b and f.get('total') == t
        detail += f' best/total={f.get("best") if f else None}/{f.get("total") if f else None}'
    if scoped is not None:
        ok = ok and js.get('scoped_tables') == scoped
        detail += f' scoped={js.get("scoped_tables")}'
    return ok, detail


def st_err_pin(work, name, text=None, evid=None, raw=None, args=None, root=False, entry_dir=False):
    d, ev, rt, ent = st_fixture(work, name, text, evid, root, entry_dir=entry_dir)
    if raw is not None:
        open(ent, 'wb').write(raw)
    if args is None:
        args = ['--entry', ent, '--evidence', ev]
        if root:
            args += ['--root', rt]
        args.append('--json')
    p = st_run(args)
    tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
    ok = p.returncode == 2 and 'TABLE_SUPPORT_ERROR' in (p.stdout + p.stderr) and not tb
    return ok, f'rc={p.returncode} error-line={"TABLE_SUPPORT_ERROR" in (p.stdout + p.stderr)} traceback={tb}'


def st_text_pin(work, name, text, rc, summary, evid=None, root=False):
    d, ev, rt, ent = st_fixture(work, name, text, evid, root)
    args = ['--entry', ent, '--evidence', ev]
    if root:
        args += ['--root', rt]
    p = st_run(args)
    lines = [l.strip() for l in p.stdout.splitlines()]
    tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
    ok = p.returncode == rc and summary in lines and not tb
    return ok, f'rc={p.returncode} summary-present={summary in lines} traceback={tb}'


def selftest_pins():
    F1K = ('UNSUPPORTED-CELL', 'Yoruba', 'limit')
    return [
        ('B1-benign-court',
         lambda w: st_json_pin(w, 'B1', st_entry(REC, CAP3, SEP3, [COURT],
                                                 ['The Court row reports the court singer (S9001).']),
                               0, [])),
        ('B2-stemming-rallies-boxes',
         lambda w: st_json_pin(w, 'B2', st_entry(REC, '| tradition | place | object |', SEP3,
                                                 ['| Town | rallies near churches | boxes of oriki |'],
                                                 ['The Town row reports the town (S9004).']), 0, [])),
        ('B3-out-of-scope-caption',
         lambda w: st_json_pin(w, 'B3', st_entry('A summary of design choices.', CAP3, SEP3,
                                                 ['| Court | zebra xylophone quantum | nebula |'], []),
                               0, [], scoped=0)),
        ('B4-path-line-binding',
         lambda w: st_json_pin(w, 'B4', st_entry(REC, '| tradition | practice | setting |', SEP3,
                                                 ['| Loom | weavers sing slow | song at the loom |'],
                                                 ['The Loom row restates `x/ref.md:2`.']),
                               0, [], root=True)),
        ('B5-diacritic-fold',
         lambda w: st_json_pin(w, 'B5', st_entry(REC, '| tradition | form |', '|---|',
                                                 ['| Town | oríkì drums |'],
                                                 ['The Town row reports the town (S9004).']), 0, [])),
        ('B6-stopwords-ignored',
         lambda w: st_json_pin(w, 'B6', st_entry(REC, CAP3, SEP3,
                                                 ['| Court | with the chief, also from them | singer |'],
                                                 ['The Court row reports the court (S9001).']), 0, [])),
        ('B7-unrecorded-out-of-scope',
         lambda w: st_json_pin(w, 'B7', st_entry('Built from unrecorded cases only.', CAP3, SEP3,
                                                 ['| Court | zebra xylophone quantum | nebula |'], []),
                               0, [], scoped=0)),
        ('B7b-recorded-not-cases-out-of-scope',
         lambda w: st_json_pin(w, 'B7b', st_entry('The recorded ledger explains this table.', CAP3, SEP3,
                                                 ['| Court | zebra xylophone quantum | nebula |'], []),
                               0, [], scoped=0)),
        ('B8-window-80-supported',
         lambda w: st_json_pin(w, 'B8', st_entry(REC, '| tradition | reward |', '|---|',
                                                 ['| Hall | chief bounty |'],
                                                 ['The Hall row reports the hall (S9005).']), 0, [])),
        ('B9-threshold-boundary-3-of-4',
         lambda w: st_json_pin(w, 'B9', st_entry(REC, CAP3, SEP3,
                                                 ['| Court | singer receives gifts zebra |'],
                                                 ['The Court row reports the court (S9001).']), 0, [])),
        ('W1W2-window-boundary-79-80',
         lambda w: st_json_pin(w, 'W1W2', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| Alpha | alpha beta |', '| Gamma | gamma delta |'],
                                                 ['The Alpha and Gamma rows report the cases (S9101).']),
                               1, [('UNSUPPORTED-CELL', 'Gamma', 'practice')],
                               best={('UNSUPPORTED-CELL', 'Gamma', 'practice'): (1, 2)}, scoped=1,
                               evid={'S9101': 'alpha ' + ' '.join(['lorem'] * 78) + ' beta gamma ' + ' '.join(['lorem'] * 79) + ' delta'})),
        ('A2-threshold-boundary-2-of-3',
         lambda w: st_json_pin(w, 'A2', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| Alpha | alpha beta zulu |'],
                                                 ['The Alpha row reports the case (S9102).']),
                               1, [('UNSUPPORTED-CELL', 'Alpha', 'practice')],
                               best={('UNSUPPORTED-CELL', 'Alpha', 'practice'): (2, 3)},
                               evid={'S9102': 'alpha beta lorem lorem lorem'})),
        ('L1-label-token-3-binds',
         lambda w: st_json_pin(w, 'L1', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| Ewe | alpha beta |'],
                                                 ['The Ewe row reports the case (S9103).']),
                               0, [], evid={'S9103': 'alpha beta'})),
        ('L2-label-token-2-must-not-bind',
         lambda w: st_json_pin(w, 'L2', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| If | alpha beta |'],
                                                 ['The If row reports the case (S9104).']),
                               1, [('UNBOUND-ROW', 'If', '')], evid={'S9104': 'alpha beta'})),
        ('L4-and-not-a-label-token',
         lambda w: st_json_pin(w, 'L4', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| Salt and iron | alpha beta |'],
                                                 ['The wind and rain report the case (S9105).']),
                               1, [('UNBOUND-ROW', 'Salt and iron', '')], evid={'S9105': 'alpha beta'})),
        ('C4-multi-line-caption',
         lambda w: st_json_pin(w, 'C4', st_entry('The recorded cases fill this table.\nDesign notes follow.',
                                                 '| tradition | practice |', '|---|',
                                                 ['| Alpha | alpha beta |'],
                                                 ['The Alpha row reports the case (S9106).']),
                               0, [], scoped=1, evid={'S9106': 'alpha beta'})),
        ('F1-unsupported-yoruba',
         lambda w: st_json_pin(w, 'F1', st_entry(REC, CAP3, SEP3, [COURT,
                                              '| Yoruba | drummers recite titles | titles are public property, so any drummer who knows them '
                                              'can assemble the praise |'],
                                              ['The Court and Yoruba rows report the court cases (S9001).']),
                               1, [F1K],
                               words={F1K: ['assemble', 'knows', 'praise', 'property', 'public']},
                               best={F1K: (2, 7)})),
        ('F2-unbound-row',
         lambda w: st_json_pin(w, 'F2', st_entry(REC, CAP3, SEP3, [COURT, '| Hausa | singer receives gifts | chief |'],
                                                 ['The Court row reports the court (S9001).']),
                               1, [('UNBOUND-ROW', 'Hausa', '')])),
        ('F3-no-capture',
         lambda w: st_json_pin(w, 'F3', st_entry(REC, CAP3, SEP3, [COURT],
                                                 ['The Court row reports the court (S9001).',
                                                  'The Court row also reports the court (S9999).']),
                               1, [('NO-CAPTURE', 'S9999', '')])),
        ('F4-no-path',
         lambda w: st_json_pin(w, 'F4', st_entry(REC, CAP3, SEP3, [COURT],
                                                 ['The Court row reports the court (S9001).',
                                                  'The Court row restates `x/missing.md:3`.']),
                               1, [('NO-PATH', 'x/missing.md', '')], root=True)),
        ('F5-no-binding-paragraph',
         lambda w: st_json_pin(w, 'F5', st_entry(REC, CAP3, SEP3, [COURT, '| Town | rallies near churches | drums |'], []),
                               1, [('UNBOUND-ROW', 'Court', ''), ('UNBOUND-ROW', 'Town', '')])),
        ('F6-no-union-per-row',
         lambda w: st_json_pin(w, 'F6', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| Court | singer receives gifts |', '| River | leader calls crew |'],
                                                 ['The Court row reports the court (S9002).',
                                                  'The River row reports the river (S9001).']),
                               1, [('UNSUPPORTED-CELL', 'Court', 'practice'),
                                   ('UNSUPPORTED-CELL', 'River', 'practice')])),
        ('F7-caption-scoped-unsupported',
         lambda w: st_json_pin(w, 'F7', st_entry('Recorded Cases fill this table.', '| tradition | practice |', '|---|',
                                                 ['| Court | zebra quantum xylophone |'],
                                                 ['The Court row reports the court (S9001).']),
                               1, [('UNSUPPORTED-CELL', 'Court', 'practice')],
                               words={('UNSUPPORTED-CELL', 'Court', 'practice'): ['quantum', 'xylophone', 'zebra']})),
        ('F8-binding-broken-by-blank',
         lambda w: st_json_pin(w, 'F8', st_entry(REC, CAP3, SEP3, [COURT], ['Notes without ids.', '',
                                                                  'The Court row reports the court (S9001).']),
                               1, [('UNBOUND-ROW', 'Court', '')])),
        ('F9-two-tables',
         lambda w: st_json_pin(w, 'F9', st_entry(REC, CAP3, SEP3, [COURT], ['The Court row reports the court (S9001).'],
                                                 tail='## 2. Next\n\nThese rows come from recorded cases too.\n\n| tradition | practice |\n|---|---|\n'
                                                      '| River | zebra quantum xylophone |\n\nThe River row reports the river (S9002).\n'),
                               1, [('UNSUPPORTED-CELL', 'River', 'practice')], scoped=2)),
        ('F10-token-not-substring-binding',
         lambda w: st_json_pin(w, 'F10', st_entry(REC, CAP3, SEP3, [COURT],
                                                  ['The courthouse row reports the singer (S9001).']),
                               1, [('UNBOUND-ROW', 'Court', '')])),
        ('F11-window-80-colocation',
         lambda w: st_json_pin(w, 'F11', st_entry(REC, '| tradition | reward |', '|---|', ['| Hall | chief bounty |'],
                                                  ['The Hall row reports the hall (S9003).']),
                               1, [('UNSUPPORTED-CELL', 'Hall', 'reward')],
                               words={('UNSUPPORTED-CELL', 'Hall', 'reward'): []},
                               best={('UNSUPPORTED-CELL', 'Hall', 'reward'): (1, 2)})),
        ('F12-binding-line-no-citation',
         lambda w: st_json_pin(w, 'F12', st_entry(REC, CAP3, SEP3, [COURT], ['The Court row reports the court singer.']),
                               1, [('UNBOUND-ROW', 'Court', '')])),
        ('F13-threshold-three-quarters',
         lambda w: st_json_pin(w, 'F13', st_entry(REC, '| tradition | reward |', '|---|',
                                                  ['| Court | singer receives zebra quantum |'],
                                                  ['The Court row reports the court (S9001).']),
                               1, [('UNSUPPORTED-CELL', 'Court', 'reward')],
                               words={('UNSUPPORTED-CELL', 'Court', 'reward'): ['quantum', 'zebra']},
                               best={('UNSUPPORTED-CELL', 'Court', 'reward'): (2, 4)})),
        ('S-nocapture-deduplicated',
         lambda w: st_json_pin(w, 'SD', st_entry(REC, CAP3, SEP3, [COURT],
                                                 ['The Court row reports the court (S9001).',
                                                  'The Court row also reports the court (S9999).',
                                                  'The Court row again reports the court (S9999).']),
                               1, [('NO-CAPTURE', 'S9999', '')])),
        ('E1-missing-entry', lambda w: st_err_pin(w, 'S_E1', args=None, raw=None) if False else _e1(w)),
        ('E2-bad-utf8', lambda w: st_err_pin(w, 'E2', raw=b'\xff\xfe# T\n| a | b |\n')),
        ('E3-missing-evidence-dir', lambda w: _e3(w)),
        ('E4-no-evidence-arg', lambda w: _e4(w)),
        ('E5-entry-is-directory', lambda w: st_err_pin(w, 'E5', entry_dir=True)),
        ('E6-work-under-tmp-refused', lambda w: _e6(w)),
        ('E7-unreadable-capture', lambda w: _e7(w)),
        ('E7dir-directory-not-a-capture', lambda w: _e7dir(w)),
        ('T1-text-summary-zero',
         lambda w: st_text_pin(w, 'T1', st_entry(REC, CAP3, SEP3, [COURT],
                                                 ['The Court row reports the court singer (S9001).']),
                               0, 'TABLE-SUPPORT: 0 finding(s) in 1 scoped table(s)')),
        ('T2-text-summary-one',
         lambda w: st_text_pin(w, 'T2', st_entry(REC, '| tradition | practice |', '|---|',
                                                 ['| Court | zebra quantum xylophone |'],
                                                 ['The Court row reports the court (S9001).']),
                               1, 'TABLE-SUPPORT: 1 finding(s) in 1 scoped table(s)')),
    ]


def _e1(work):
    d, ev, rt, ent = st_fixture(work, 'E1', '# T\n')
    return st_err_pin(work, 'E1x', args=['--entry', os.path.join(d, 'absent.md'),
                                          '--evidence', ev, '--json'])


def _e3(work):
    d, ev, rt, ent = st_fixture(work, 'E3', '# T\n')
    return st_err_pin(work, 'E3x', args=['--entry', ent, '--evidence', os.path.join(d, 'no-such-dir'),
                                          '--json'])


def _e4(work):
    d, ev, rt, ent = st_fixture(work, 'E4', '# T\n')
    return st_err_pin(work, 'E4x', args=['--entry', ent, '--json'])


def _e6(work):
    # Refusal happens before any write, so nothing is created under /tmp.
    p = st_run(['--selftest', '--work', os.path.join('/tmp', 'tts-probe-' + str(os.getpid()))])
    tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
    ok = p.returncode == 2 and 'TABLE_SUPPORT_ERROR' in (p.stdout + p.stderr) and not tb
    return ok, f'rc={p.returncode} error-line={"TABLE_SUPPORT_ERROR" in (p.stdout + p.stderr)} traceback={tb}'


def _e7(work):
    # An unreadable capture file (chmod 000) must be TABLE_SUPPORT_ ERROR at rc 2
    # with no traceback — the ToolError path (mutant R4 re-raises it and leaks a
    # traceback, which this pin catches).
    d, ev, rt, ent = st_fixture(work, 'E7dir', st_entry(REC, CAP3, SEP3, [COURT],
                                                      ['The Court row reports the court (S7777).']))
    f = os.path.join(ev, 'S7777.txt')
    open(f, 'w', encoding='utf-8').write('chief bounty singer receives gifts')
    os.chmod(f, 0)
    try:
        p = st_run(['--entry', ent, '--evidence', ev, '--json'])
        tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
        ok = p.returncode == 2 and 'TABLE_SUPPORT_ERROR' in (p.stdout + p.stderr) and not tb
        return ok, f'rc={p.returncode} got={p.stdout.strip()[:90]} traceback={tb}'
    finally:
        os.chmod(f, 0o644)


def _e7dir(work):
    # A directory named <S-id>.txt is not a capture: NO-CAPTURE at rc 1, JSON, no traceback.
    d, ev, rt, ent = st_fixture(work, 'E7d', st_entry(REC, CAP3, SEP3, [COURT],
                                                      ['The Court row reports the court (S8888).']))
    os.makedirs(os.path.join(ev, 'S8888.txt'), exist_ok=True)
    p = st_run(['--entry', ent, '--evidence', ev, '--json'])
    tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
    try:
        fs = json.loads(p.stdout)['findings']
        got = sorted({fkey(f) for f in fs})
    except Exception as e:
        return False, f'rc={p.returncode} json-unparseable ({type(e).__name__})'
    ok = p.returncode == 1 and got == [('NO-CAPTURE', 'S8888', ''), ('UNSUPPORTED-CELL', 'Court', 'limit'),
                                        ('UNSUPPORTED-CELL', 'Court', 'singer')] and not tb
    return ok, f'rc={p.returncode} got={got} traceback={tb}'



def selftest(work):
    if not work:
        print('TABLE_SUPPORT_ERROR --selftest requires --work DIR')
        return 2
    if os.path.realpath(work).startswith('/tmp'):
        print('TABLE_SUPPORT_ERROR --work must not live under /tmp')
        return 2
    os.makedirs(work, exist_ok=True)
    pins = selftest_pins()
    npass = 0
    for name, fn in pins:
        try:
            ok, detail = fn(work)
        except Exception as e:
            ok, detail = False, f'exc {type(e).__name__}: {e}'
        npass += bool(ok)
        print(f'PIN {name} {"PASS" if ok else "FAIL"} {detail}')
    print(f'SELFTEST PASS {npass}/{len(pins)}')
    return 0 if npass == len(pins) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--entry')
    ap.add_argument('--evidence', action='append', default=[])
    ap.add_argument('--root')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--work')
    a = ap.parse_args()
    try:
        if a.selftest:
            return selftest(a.work)
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
    except ToolError as e:
        print(f'TABLE_SUPPORT_ERROR {e}')
        return 2
    except Exception as e:  # never a traceback
        print(f'TABLE_SUPPORT_ERROR {type(e).__name__}: {e}')
        return 2


if __name__ == '__main__':
    sys.exit(main())
