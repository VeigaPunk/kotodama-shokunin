#!/usr/bin/env python3
"""Grade a registry re-verification advance or a coverage entry against its evidence.

Round-90 successor to the round-89 frozen counter's F/C legs. The round-89
counter passed five counterfeit landings its own wave built
(corpus/lessons/round-89.md R89-M5/M6). This tool refuses each of those
classes by name instead of re-deriving the whole claim:

  advance mode (registry rows re-verified against their live surface)
    ADVANCED   population rows whose recheck moved to an ISO date inside the window
    SHADOW     duplicate ids, duplicate population URLs, or a shadowed population row
    MEANING    the located quote shares content words with the row's `teaches` cell,
               is not a substring of the row's own source cell (site chrome, titles
               and JSON keys fail here) and is not a substring of the row's own
               `teaches` cell (a self-quote restates the lane's summary instead of
               locating prose, so it proves no location)
    ARCHIVE    a web.archive.org surface must carry a 14-digit timestamp whose year
               is the round's year and embed one of the row's URLs exactly
    CAPTURE    captures live under the declared directory, are not the graded files
               themselves, match their manifest sha256/http status and carry a strict
               local ISO fetch time on the round's date
    DISPOSED   one disposition line per population id; every NOT-LOCATED spelling
               variant counts as NOT-LOCATED; an advanced id is never NOT-LOCATED
    OTHERCELLS population rows change only their recheck cell; no base row is removed

  entry mode (one coverage entry and the sources it mines)
    ENTRY      size, heading count and header keys
    SHAPE      a real table and non-repetitive prose
    TOPIC      the entry is about its declared topic (content-word overlap)
    NEWIDS     >= N new mined A/B rows opened on the round's date and cited by the entry
    GATE       each such row has a lesson line: id, URL, access date, quote
    CAPTURE    each gate quote occurs in its committed capture (same rules as above)

Exit 0 pass, 1 finding(s), 2 refused (bad arguments or unreadable input).
No network access: every surface is a committed capture.
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata

ROW_RE = re.compile(r'^ {0,3}\|[ ]*(S\d{3,})[ ]*\|')
ISO_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
CADENCE_RE = re.compile(r'^(\d{1,3})d$')
URL_RE = re.compile(r'https?://[^\s|)]+')
ARCHIVE_RE = re.compile(r'^https://web\.archive\.org/web/(\d{14})/(.+)$')
QUOTE_RE = re.compile(r'\u201c([^\u201d]+)\u201d|"([^"]+)"')
FETCH_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$')
DISPO_RE = re.compile(r'^[-*] ?S(\d{3,})\b.*?\b(NOT[ _-]?LOCATED|LOCATED)\b', re.I)
STOP = set('''a an the and or but if of to in on at for with from by as is are was were be been being
this that these those it its their his her they we you i not no nor so than then there here which who
whom whose what when where why how all any both each few more most other some such only own same too very
can will just should now into over under about after before between during through above below out off
again further once has have had do does did doing also may might must shall would could one two three
'''.split())


class Refused(Exception):
    pass


def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).replace('\u2019', "'")
    s = ' '.join(s.split()).casefold()
    s = re.sub(r'\s+([.,;:!?%\)\]])', r'\1', s)
    return s


def words(s):
    return [w for w in re.findall(r"[a-z][a-z'\-]+", norm(s)) if len(w) >= 4 and w not in STOP]


def overlap(a, b):
    return len(set(words(a)) & set(words(b)))


def read(path):
    try:
        with open(path, 'rb') as f:
            raw = f.read()
    except OSError as exc:
        raise Refused(f'unreadable {path}: {exc.strerror}')
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError:
        raise Refused(f'not UTF-8: {path}')


def registry(text):
    """Rows in file order; duplicate ids are reported, never collapsed."""
    rows, dup = [], []
    seen = {}
    for n, line in enumerate(text.splitlines(), 1):
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        row = dict(id=m.group(1), cells=cells, line=n)
        if row['id'] in seen:
            dup.append(row['id'])
        seen[row['id']] = row
        rows.append(row)
    return rows, dup


def by_id(rows):
    out = {}
    for r in rows:
        out.setdefault(r['id'], []).append(r)
    return out


def urls(cell):
    return [u.rstrip('.,;:\'') for u in URL_RE.findall(cell)]


def as_date(s, label):
    m = ISO_RE.match(str(s).strip())
    if not m:
        raise Refused(f'{label}: not an ISO date: {s!r}')
    try:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        raise Refused(f'{label}: impossible date: {s!r}')


def population(args):
    raw = args.population or ''
    if raw:
        ids = [x.strip() for x in re.split(r'[,\s]+', raw) if x.strip()]
    else:
        ids = [l.strip() for l in read(args.population_file).splitlines() if l.strip()]
    if not ids:
        raise Refused('empty population')
    for i in ids:
        if not re.match(r'^S\d{3,}$', i):
            raise Refused(f'population id malformed: {i!r}')
    return ids


def dispositions(lesson):
    """First disposition per id; every NOT-LOCATED spelling collapses to NOT-LOCATED."""
    out = {}
    for line in lesson.splitlines():
        m = DISPO_RE.match(line.strip())
        if not m:
            continue
        rid, verdict = 'S' + m.group(1), m.group(2).upper().replace('_', ' ').replace('-', ' ')
        verdict = 'NOT-LOCATED' if verdict.startswith('NOT') else 'LOCATED'
        if rid not in out:
            out[rid] = (verdict, line.strip())
    return out


def gate_quotes(lesson):
    """id -> list of (line, first double-quoted span)."""
    out = {}
    for line in lesson.splitlines():
        ids = re.findall(r'\bS\d{3,}\b', line)
        m = QUOTE_RE.search(line)
        if not ids or not m:
            continue
        q = (m.group(1) or m.group(2)).strip()
        for rid in ids:
            out.setdefault(rid, []).append((line, q))
    return out


def capture_text(cap_dir, man_entry, root):
    rel = str((man_entry or {}).get('capture', '')).strip() if isinstance(man_entry, dict) else ''
    if not rel or rel.startswith('/') or '..' in rel.split('/'):
        return ''
    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/') + '/')):
        return ''
    try:
        with open(os.path.join(root, rel), 'rb') as f:
            return norm(f.read().decode('utf-8', errors='replace'))
    except OSError:
        return ''


def capture_error(cap_dir, graded, man_entry, quote, as_of, root):
    m = man_entry
    if not isinstance(m, dict):
        return 'no manifest entry'
    rel = str(m.get('capture', '')).strip()
    if not rel:
        return 'manifest capture empty'
    if rel.startswith('/') or '..' in rel.split('/'):
        return f'capture path not relative and confined: {rel}'
    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/') + '/')):
        return f'capture outside {cap_dir}: {rel}'
    for g in graded:
        if rel == g or rel == os.path.normpath(g):
            return f'capture is a graded file: {rel}'
    path = os.path.join(root, rel)
    try:
        with open(path, 'rb') as f:
            raw = f.read()
    except OSError:
        return f'capture not committed: {rel}'
    if hashlib.sha256(raw).hexdigest() != str(m.get('sha256', '')):
        return f'capture sha256 mismatch: {rel}'
    if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:
        return f'capture http_status not 2xx: {rel}'
    fm = FETCH_RE.match(str(m.get('fetched_at', '')))
    if not fm:
        return f'fetched_at not a local ISO instant with offset: {m.get("fetched_at")!r}'
    if fm.group(1) != as_of:
        return f'fetched_at date {fm.group(1)} != as_of {as_of}'
    text = norm(raw.decode('utf-8', errors='replace'))
    if norm(quote) not in text:
        return f'quote absent from capture: {rel}'
    return None


def surface_error(candidate, row_cell, as_of):
    """A re-opened surface is the row's own URL or a same-year archive of it."""
    cand = str(candidate).strip()
    row_urls = urls(row_cell)
    if not row_urls:
        return 'row carries no URL'
    if cand in row_urls:
        return None
    m = ARCHIVE_RE.match(cand)
    if not m:
        return f'manifest url is not a row url: {cand}'
    stamp, embedded = m.group(1), m.group(2)
    if embedded not in row_urls:
        return f'archive embeds a foreign url: {embedded}'
    if int(stamp[:4]) < int(as_of[:4]):
        return f'archive snapshot {stamp[:4]} predates the round: immutable surface'
    return None


def grade_advance(args):
    base_rows, _ = registry(read(args.base_registry))
    lands_rows, lands_dup = registry(read(args.lands_registry))
    lesson = read(args.lesson)
    man = json.loads(read(args.manifest) or '{}')
    man_rows = man.get('rows', man)
    ids = population(args)
    as_of = as_date(args.as_of, '--as-of')
    lo = as_of + datetime.timedelta(days=args.window_days)
    hi = as_of + datetime.timedelta(days=args.max_days)
    base, lands = by_id(base_rows), by_id(lands_rows)
    disp = dispositions(lesson)
    gates = gate_quotes(lesson)
    graded = list(args.graded)
    legs, advanced = [], []
    detail = {}

    # ADVANCED
    problems = []
    for rid in ids:
        if rid not in base:
            problems.append(f'{rid}: not in base registry')
            continue
        if len(lands.get(rid, [])) != 1:
            problems.append(f'{rid}: {len(lands.get(rid, []))} rows at lands')
            continue
        old = base[rid][0]['cells'][9]
        new = lands[rid][0]['cells'][9]
        if new == old:
            continue
        try:
            d = as_date(new, rid)
        except Refused as exc:
            problems.append(f'{rid}: recheck not ISO ({exc})')
            continue
        if not (lo < d <= hi):
            problems.append(f'{rid}: recheck {new} outside ({lo}, {hi}]')
            continue
        advanced.append(rid)
    ok = not problems and len(advanced) >= args.min_advanced
    legs.append(('ADVANCED', ok, f'>={args.min_advanced} of {len(ids)}', f'{len(advanced)} advanced' + ('' if not problems else '; ' + '; '.join(problems))))
    detail['advanced'] = advanced

    # SHADOW
    shadow = []
    if lands_dup:
        shadow.append('duplicate ids: ' + ','.join(sorted(set(lands_dup))))
    seen_url = {}
    for rid in ids:
        for r in lands.get(rid, []):
            for u in urls(r['cells'][1] if len(r['cells']) > 1 else ''):
                seen_url.setdefault(u, set()).add(r['id'])
    for u, owners in seen_url.items():
        if len(owners) > 1:
            shadow.append('population url in ' + ','.join(sorted(owners)) + ': ' + u)
    legs.append(('SHADOW', not shadow, 'no duplicate id/url and one row per population id', 'clean' if not shadow else '; '.join(shadow)))

    # MEANING + ARCHIVE + CAPTURE per advanced row
    meaning, surface, capture, unbound = [], [], [], []
    for rid in advanced:
        row = lands[rid][0]
        teaches = row['cells'][6] if len(row['cells']) > 6 else ''
        src = row['cells'][1] if len(row['cells']) > 1 else ''
        qs = gates.get(rid, [])
        if not qs:
            meaning.append(f'{rid}: no located line with a quote')
            capture.append(f'{rid}: no gate quote')
            surface.append(f'{rid}: no manifest surface')
            continue
        line, quote = qs[0]
        scope = row['cells'][4] if len(row['cells']) > 4 else ''
        anchor = row['cells'][5] if len(row['cells']) > 5 else ''
        if len(quote.split()) > args.quote_max_words:
            meaning.append(f'{rid}: quote over {args.quote_max_words} words')
        q = norm(quote)
        if q and q in norm(src):
            meaning.append(f'{rid}: quote is copied from the row source cell (title or chrome), not located prose')
        elif q and q in norm(teaches):
            meaning.append(f'{rid}: quote is copied from the row teaching cell (self-quote)')
        elif not words(quote):
            unbound.append(rid)
        elif max(overlap(quote, teaches), overlap(quote, scope), overlap(quote, anchor)) < args.min_overlap:
            meaning.append(f'{rid}: quote shares no content word with teaches/scope/anchor')
        m = man_rows.get(rid)
        err = surface_error((m or {}).get('url', ''), src, args.as_of)
        if err:
            surface.append(f'{rid}: {err}')
        err = capture_error(args.capture_dir, graded, m, quote, args.as_of, args.root)
        if err:
            capture.append(f'{rid}: {err}')
        if rid in disp and disp[rid][0] == 'NOT-LOCATED':
            meaning.append(f'{rid}: advanced while NOT-LOCATED')
    legs.append(('MEANING', not meaning, 'each advanced quote is bound to its row teaching',
                 ('clean' if not meaning else '; '.join(meaning))
                 + ('' if not unbound else f' [non-Latin, unbound: {",".join(unbound)}]')))
    legs.append(('ARCHIVE', not surface, 'each surface is the row url or a same-year archive of it', 'clean' if not surface else '; '.join(surface)))
    legs.append(('CAPTURE', not capture, 'captures confined, hashed, 2xx and quote-bearing', 'clean' if not capture else '; '.join(capture)))

    # DISPOSED
    dispo = [rid for rid in ids if rid not in disp]
    legs.append(('DISPOSED', not dispo, f'{len(ids)}/{len(ids)} ids carry one disposition', 'clean' if not dispo else 'missing: ' + ','.join(dispo)))

    # OTHERCELLS
    cells = []
    for rid in ids:
        if rid not in base or rid not in lands:
            continue
        b, l = base[rid][0]['cells'], lands[rid][0]['cells']
        if len(b) != len(l):
            cells.append(f'{rid}: cell count {len(b)}->{len(l)}')
            continue
        moved = [i for i in range(len(b)) if b[i] != l[i] and i != 9]
        if moved:
            cells.append(f'{rid}: cells moved {moved}')
    legs.append(('OTHERCELLS', not cells, 'population rows change only recheck', 'clean' if not cells else '; '.join(cells)))
    return legs, detail


def table_shape(text):
    rows = [l for l in text.splitlines() if l.strip().startswith('|')]
    if len(rows) < 2:
        return 0, 0
    cols = max(len(r.strip().strip('|').split('|')) for r in rows)
    data = max(0, len(rows) - 2)
    return data, cols


def sentences(text):
    body = re.sub(r'^\|.*$', '', text, flags=re.M)
    body = re.sub(r'^#.*$', '', body, flags=re.M)
    return [s for s in re.split(r'(?<=[.!?])\s+', norm(body)) if len(s.split()) >= 6]


def grade_entry(args):
    entry = read(args.entry)
    base_ids = set(r['id'] for r in registry(read(args.base_registry))[0])
    lands_rows, lands_dup = registry(read(args.lands_registry))
    lands_ids = set(r['id'] for r in lands_rows)
    lesson = read(args.lesson)
    man = json.loads(read(args.manifest) or '{}')
    man_rows = man.get('rows', man)
    as_of = as_date(args.as_of, '--as-of')
    legs = []
    detail = {}

    # ENTRY
    problems = []
    if len(entry.encode()) < args.min_bytes:
        problems.append(f'{len(entry.encode())} bytes < {args.min_bytes}')
    heads = [l for l in entry.splitlines() if l.startswith('## ')]
    if len(heads) < args.min_headings:
        problems.append(f'{len(heads)} h2 < {args.min_headings}')
    for key in ('topic:', 'sources:', 'verified-at:', 'recheck:'):
        if key not in entry:
            problems.append(f'header key {key} absent')
    legs.append(('ENTRY', not problems, f'>={args.min_bytes}B, >={args.min_headings} h2, header keys', 'clean' if not problems else '; '.join(problems)))

    # SHAPE
    rows, cols = table_shape(entry)
    ss = sentences(entry)
    worst = max([ss.count(s) for s in set(ss)] or [0])
    problems = []
    if rows < args.table_min_rows or cols < args.table_min_cols:
        problems.append(f'table {rows}x{cols} < {args.table_min_rows}x{args.table_min_cols}')
    if worst > 2:
        problems.append(f'a sentence repeats {worst}x')
    legs.append(('SHAPE', not problems, f'>={args.table_min_rows} data rows x >={args.table_min_cols} cols, no filler repetition', 'clean' if not problems else '; '.join(problems)))

    # TOPIC
    topic_line = next((l for l in entry.splitlines() if l.strip().startswith('- topic:')), '')
    shared = overlap(entry, args.topic)
    stem_words = [w for w in re.split(r'[-_.]', os.path.basename(args.entry)) if len(w) >= 4]
    stem_hit = sum(1 for w in stem_words if norm(w) in norm(entry))
    problems = []
    if shared < args.min_topic_overlap:
        problems.append(f'entry shares {shared} content words with the declared topic < {args.min_topic_overlap}')
    if stem_words and stem_hit == 0:
        problems.append('entry filename words absent from its text')
    legs.append(('TOPIC', not problems, f'>={args.min_topic_overlap} shared content words with the declared topic', 'clean' if not problems else '; '.join(problems)))

    # NEWIDS
    # NEWIDS: only new rows the entry cites are in the claim's population. An
    # uncited new row (a reject, or a row another surface mines) is out of scope,
    # never a reason to fail this claim.
    new_ids = sorted((lands_ids - base_ids))
    cited = sorted(set(re.findall(r'\bS\d{3,}\b', entry)))
    scoped = [rid for rid in new_ids if rid in cited]
    qualifying = []
    problems = []
    byid = by_id(lands_rows)
    detail['new_ids_all'] = new_ids
    detail['new_ids_cited'] = scoped
    for rid in scoped:
        cells = byid[rid][0]['cells']
        tier, status, opened, used = cells[3], cells[7], cells[8], cells[10]
        if tier not in ('A', 'B'):
            problems.append(f'{rid}: tier {tier} not A/B')
            continue
        if status != 'mined':
            problems.append(f'{rid}: status {status} not mined')
            continue
        if opened != args.as_of:
            problems.append(f'{rid}: opened {opened} != {args.as_of}')
            continue
        if os.path.basename(args.entry) not in used and args.entry not in used:
            problems.append(f'{rid}: used-by does not name the entry')
            continue
        qualifying.append(rid)
    if len(qualifying) < args.min_new_ids:
        problems.append(f'{len(qualifying)} qualifying new ids < {args.min_new_ids}')
    if not set(qualifying) <= set(cited):
        problems.append('qualifying ids not cited: ' + ','.join(sorted(set(qualifying) - set(cited))))
    missing = [c for c in cited if c not in lands_ids]
    if missing:
        problems.append('cited ids missing from registry: ' + ','.join(missing))
    legs.append(('NEWIDS', not problems, f'>={args.min_new_ids} new mined A/B rows opened {args.as_of} and cited', 'clean' if not problems else '; '.join(problems)))
    detail['qualifying'] = qualifying

    # GATE + CAPTURE
    gates = gate_quotes(lesson)
    gate, capture = [], []
    for rid in qualifying:
        row = byid[rid][0]
        src = row['cells'][1]
        qs = gates.get(rid, [])
        if not qs:
            gate.append(f'{rid}: no lesson line with id and quote')
            continue
        line, quote = qs[0]
        if not any(u in line for u in urls(src)):
            gate.append(f'{rid}: gate line does not name the row url')
        if args.as_of not in line:
            gate.append(f'{rid}: gate line lacks the access date')
        if len(quote.split()) > args.quote_max_words or len(norm(quote)) < args.quote_min_chars:
            gate.append(f'{rid}: quote {len(quote.split())} words / {len(norm(quote))} chars out of bounds')
        err = capture_error(args.capture_dir, list(args.graded), man_rows.get(rid), quote, args.as_of, args.root)
        if err:
            capture.append(f'{rid}: {err}')
    legs.append(('GATE', not gate, 'each new id has a located gate line', 'clean' if not gate else '; '.join(gate)))
    legs.append(('CAPTURE', not capture, 'each gate quote occurs in its committed capture', 'clean' if not capture else '; '.join(capture)))
    return legs, detail


def emit(legs, detail, receipt=None, label='', as_json=False):
    lines = []
    for name, passed, expected, observed in legs:
        lines.append(f'LEG {"PASS" if passed else "FAIL"} {name} expected={expected} observed={observed}')
    failed = [n for n, p, _, _ in legs if not p]
    lines.append(f'{label}: {"PASS" if not failed else "FAIL"} legs={len(legs) - len(failed)}/{len(legs)}'
                 + ('' if not failed else ' failed=' + ','.join(failed)))
    out = '\n'.join(lines)
    print(out)
    if receipt:
        with open(receipt, 'w') as f:
            f.write(out + '\n')
        if as_json:
            with open(receipt + '.json', 'w') as f:
                json.dump({'label': label, 'rc': 0 if not failed else 1,
                           'legs': [dict(name=n, pass_=bool(p), expected=e, observed=o) for n, p, e, o in legs],
                           'detail': detail}, f, indent=1, sort_keys=True)
    return 0 if not failed else 1


def cli(args):
    if args.advance:
        return emit(*grade_advance(args), receipt=args.receipt, label='ADVANCE-EVIDENCE', as_json=args.json)
    if args.entry:
        return emit(*grade_entry(args), receipt=args.receipt, label='ENTRY-EVIDENCE', as_json=args.json)
    raise Refused('choose advance or entry')


# ---------------------------------------------------------------- selftest
def _row(rid, url, teaches, recheck='90d', tier='A', status='mined', opened='2026-10-19', used='corpus/knowledge/x.md'):
    return (f'| {rid} | {url} | docs | {tier} | scope | anchor | {teaches} | {status} | {opened} | {recheck} | {used} |')


HEADER = ('| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'
          '|---|---|---|---|---|---|---|---|---|---|---|')


def _cap(work, name, body):
    path = os.path.join(work, 'reports/round-90/evidence', name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(body)
    return path


def _manifest(work, rows, name='manifest.json'):
    path = os.path.join(work, 'reports/round-90/evidence', name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out = {}
    for rid, rec in rows.items():
        cap = str(rec.get('capture', ''))
        p = os.path.join(work, cap) if cap else ''
        sha = hashlib.sha256(open(p, 'rb').read()).hexdigest() if p and os.path.isfile(p) else ''
        out[rid] = dict(rec, sha256=sha)
    with open(path, 'w') as f:
        json.dump({'rows': out}, f, indent=1)
    return path


def _run(args, expect_rc, expect=()):
    r = subprocess.run([sys.executable, '-B', os.path.abspath(__file__)] + args,
                       capture_output=True, text=True)
    got = r.returncode
    joined = (r.stdout or '') + (r.stderr or '')
    ok = got == expect_rc and all(e in joined for e in expect)
    return ok, got, joined.strip().splitlines()[-1:] if joined.strip() else []


def selftest(work):
    root = os.path.join(work, 'st')
    shutil.rmtree(root, ignore_errors=True)
    ev = os.path.join(root, 'reports/round-90/evidence')
    os.makedirs(ev, exist_ok=True)
    base = os.path.join(root, 'base.md')
    good_teach = 'prayer addressed to a named deity through fixed vocative formulae and votive promises'
    url = 'https://example.org/prayer'
    with open(base, 'w') as f:
        f.write(HEADER + '\n' + _row('S001', url, good_teach) + '\n'
                + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    body = 'the fixed vocative formulae address the deity and the votive promise binds the petitioner'
    _cap(root, 'S001.txt', 'Capture. ' + body + ' Also boilerplate.')
    man = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt', url=url,
                                        http_status=200, fetched_at='2026-11-04T19:00:00-03:00')})
    lesson_ok = ('- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url +
                 ' accessed 2026-11-04: \u201c' + body + '\u201d\n'
                 '- S002 LOCATED recheck unchanged \u2014 ' + url + '/other accessed 2026-11-04: '
                 '\u201cunrelated row about dye plants\u201d\n')

    def write(name, text):
        p = os.path.join(root, name)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w') as f:
            f.write(text)
        return p

    lands_ok = write('lands.md', HEADER + '\n'
                     + _row('S001', url, good_teach, recheck='2027-02-03') + '\n'
                     + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    lesson = write('lesson.md', lesson_ok)

    def A(graded_extra=(), **over):
        base_args = dict(base_registry=base, lands_registry=lands_ok, lesson=lesson, manifest=man,
                         **{'capture_dir': 'reports/round-90/evidence', 'as_of': '2026-11-04',
                            'population': 'S001,S002', 'min_advanced': '1'})
        base_args.update(over)
        out = ['--root', root]
        for k, v in base_args.items():
            if v is None:
                continue
            out += ['--' + k.replace('_', '-'), v]
        out += ['--graded', 'corpus/SOURCES.md', '--graded', 'corpus/lessons/round-90.md']
        for g in graded_extra:
            out += ['--graded', g]
        return out

    checks = []

    def chk(name, args, rc, expect=()):
        ok, got, tail = _run(args, rc, expect)
        checks.append((name, ok, rc, got, tail))

    chk('positive advance', ['advance'] + A(), 0, ['PASS legs=7/7'])
    shadow = write('shadow.md', HEADER + '\n'
                   + _row('S001', url, good_teach, recheck='2027-02-03') + '\n'
                   + _row('S001', url, good_teach, recheck='2027-02-03') + '\n'
                   + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('shadow duplicate id', ['advance'] + A(lands_registry=shadow), 1, ['FAIL SHADOW'])
    shadow_url = write('shadowurl.md', HEADER + '\n'
                       + _row('S001', url, good_teach, recheck='2027-02-03') + '\n'
                       + _row('S002', url, 'unrelated row about dye plants and textile trade') + '\n')
    chk('shadow duplicate url', ['advance'] + A(lands_registry=shadow_url), 1, ['FAIL SHADOW'])
    chrome = write('chrome.md', '- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url
                   + ' accessed 2026-11-04: \u201cComputer Science Computation Language Best Practices\u201d\n'
                   '- S002 LOCATED x accessed 2026-11-04: \u201cunrelated row about dye plants\u201d\n')
    chk('chrome quote', ['advance'] + A(lesson=chrome), 1, ['FAIL MEANING'])
    selfq = write('selfq.md', '- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url
                  + ' accessed 2026-11-04: \u201c' + good_teach + '\u201d\n'
                  '- S002 LOCATED x accessed 2026-11-04: \u201cunrelated row about dye plants\u201d\n')
    chk('quote is the source cell', ['advance'] + A(lesson=selfq), 1, ['FAIL MEANING'])
    titled = write('titled.md', HEADER + '\n'
                   + _row('S001', url + ' (The Prayer Book of Example)', good_teach, recheck='2027-02-03') + '\n'
                   + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    lesson_title = write('lesson_title.md', '- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url
                         + ' accessed 2026-11-04: \u201cThe Prayer Book of Example\u201d\n'
                         '- S002 LOCATED x accessed 2026-11-04: \u201cunrelated row about dye plants\u201d\n')
    chk('quote is from the source cell', ['advance'] + A(lands_registry=titled, lesson=lesson_title), 1, ['FAIL MEANING'])
    man_1999 = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt',
                                             url='https://web.archive.org/web/19990101000000/' + url,
                                             http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'm1999.json')
    chk('archive year predates round', ['advance'] + A(manifest=man_1999), 1, ['FAIL ARCHIVE'])
    man_foreign = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt',
                                                url='https://web.archive.org/web/2026/https://evil.invalid/?u=' + url,
                                                http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'mforeign.json')
    chk('archive foreign host', ['advance'] + A(manifest=man_foreign), 1, ['FAIL ARCHIVE'])
    man_fresh = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt',
                                              url='https://web.archive.org/web/20261104000000/' + url,
                                              http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'mfresh.json')
    chk('same-year archive accepted', ['advance'] + A(manifest=man_fresh), 0, ['PASS legs=7/7'])
    os.makedirs(os.path.join(root, 'reports/round-90/elsewhere'), exist_ok=True)
    shutil.copy(os.path.join(ev, 'S001.txt'), os.path.join(root, 'reports/round-90/elsewhere/S001.txt'))
    man_out = _manifest(root, {'S001': dict(capture='reports/round-90/elsewhere/S001.txt', url=url,
                                            http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'mout.json')
    chk('capture outside declared dir', ['advance'] + A(manifest=man_out), 1, ['FAIL CAPTURE'])
    os.makedirs(os.path.join(root, 'corpus/lessons'), exist_ok=True)
    shutil.copy(lands_ok, os.path.join(root, 'corpus/SOURCES.md'))
    man_graded = _manifest(root, {'S001': dict(capture='corpus/SOURCES.md', url=url,
                                               http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'mgraded.json')
    chk('capture is a graded file', ['advance'] + A(manifest=man_graded), 1, ['FAIL CAPTURE'])
    man_junk = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt', url=url,
                                             http_status=200, fetched_at='2026-11-04 (not actually fetched)')}, 'mjunk.json')
    chk('fetched_at prefix junk', ['advance'] + A(manifest=man_junk), 1, ['FAIL CAPTURE'])
    man_500 = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt', url=url,
                                            http_status=503, fetched_at='2026-11-04T19:00:00-03:00')}, 'm503.json')
    chk('capture http 503', ['advance'] + A(manifest=man_500), 1, ['FAIL CAPTURE'])
    dispo_var = write('dispo.md', lesson_ok.replace('- S002 LOCATED', '- S002 NOT_LOCATED'))
    chk('NOT_LOCATED variant is a disposition', ['advance'] + A(lesson=dispo_var), 0, ['PASS legs=7/7'])
    dispo_adv = write('dispoadv.md', '- S001 NOT-LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url
                      + ' accessed 2026-11-04: \u201c' + body + '\u201d\n'
                      '- S002 LOCATED x accessed 2026-11-04: \u201cunrelated row about dye plants\u201d\n')
    chk('advanced while NOT-LOCATED', ['advance'] + A(lesson=dispo_adv), 1, ['FAIL MEANING'])
    near = write('near.md', HEADER + '\n'
                 + _row('S001', url, good_teach, recheck='2027-01-01') + '\n'
                 + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('recheck inside the window floor', ['advance'] + A(lands_registry=near), 1, ['FAIL ADVANCED'])
    othercell = write('othercell.md', HEADER + '\n'
                      + _row('S001', url, good_teach + ' CHANGED', recheck='2027-02-03') + '\n'
                      + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('another cell moved', ['advance'] + A(lands_registry=othercell), 1, ['FAIL OTHERCELLS'])
    removed = write('removed.md', HEADER + '\n' + _row('S001', url, good_teach, recheck='2027-02-03') + '\n')
    chk('base row removed', ['advance'] + A(lands_registry=removed), 1, ['FAIL ADVANCED'])
    chk('min advanced unmet', ['advance'] + A(min_advanced='2'), 1, ['FAIL ADVANCED'])
    chk('missing registry refused', ['advance'] + A(lands_registry=os.path.join(root, 'nope.md')), 2, ['unreadable'])
    chk('bad population refused', ['advance'] + A(population='S1x'), 2, ['malformed'])

    dupid = write('dupid.md', HEADER + '\n'
                  + _row('S001', url, good_teach, recheck='2027-02-03') + '\n'
                  + _row('S001', 'https://example.org/dup', 'another row under the same id') + '\n'
                  + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('duplicate id, distinct urls', ['advance'] + A(lands_registry=dupid), 1, ['FAIL SHADOW'])
    man_embed = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001.txt',
                                              url='https://web.archive.org/web/20261104000000/https://evil.invalid/?u=' + url,
                                              http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'membed.json')
    chk('archive stamp embeds a foreign url', ['advance'] + A(manifest=man_embed), 1, ['FAIL ARCHIVE'])
    chk('capture inside the dir but graded',
        ['advance'] + A(graded_extra=('reports/round-90/evidence/S001.txt',)), 1, ['FAIL CAPTURE'])
    man_sha = json.load(open(man))
    man_sha['rows']['S001']['sha256'] = '0' * 64
    man_sha_path = os.path.join(root, 'reports/round-90/evidence', 'msha.json')
    json.dump(man_sha, open(man_sha_path, 'w'))
    chk('capture sha256 mismatch', ['advance'] + A(manifest=man_sha_path), 1, ['FAIL CAPTURE'])
    _cap(root, 'S001-absent.txt', 'A capture that does not carry the located quote at all.')
    man_absent = _manifest(root, {'S001': dict(capture='reports/round-90/evidence/S001-absent.txt', url=url,
                                               http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'mabsent.json')
    chk('quote absent from capture', ['advance'] + A(manifest=man_absent), 1, ['FAIL CAPTURE'])
    lesson_short = write('lesson_short.md', '- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url
                         + ' accessed 2026-11-04: \u201c' + body + '\u201d\n')
    chk('an id has no disposition line', ['advance'] + A(lesson=lesson_short), 1, ['FAIL DISPOSED'])

    # ------------------------------------------------------------ entry mode
    topic = 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims'
    entry_ok = os.path.join(root, 'corpus/knowledge/myth-symbol/prayer-register.md')
    os.makedirs(os.path.dirname(entry_ok), exist_ok=True)
    good_body = ('# Prayer and petition\n\n- topic: prayer as a petitionary address register\n- sources: S010 S011 S012\n'
                 '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                 '## 1. The address\n\nA prayer opens by naming the deity in the vocative and stating the petitioner. '
                 'The vocative formulae vary by rank and by occasion, and the petitioner names a claim on the god.\n\n'
                 '## 2. The petition\n\nThe petition states a want in a fixed order: address, reminder of past favour, request, promise. '
                 'The votive promise binds the petitioner to a return and is the enforceable half of the exchange.\n\n'
                 '## 3. Fixed and extempore\n\nFixed prayer is recited by rote and its wording is protected from change. '
                 'Extempore prayer is composed at the moment and its authority rests on the speaker rather than the text.\n\n'
                 '## 4. Efficacy\n\nA prayer claims efficacy through the address, the promise or the speaker. '
                 'The claim is graded in the culture: some prayers are held to compel, others only to petition.\n\n'
                 '## 5. Table\n\n| element | fixed | extempore |\n|---|---|---|\n| address | rote | improvised |\n'
                 '| petition | set | composed |\n| promise | written | spoken |\n| authority | text | speaker |\n'
                 '| failure | ritual fault | weak speaker |\n\n'
                 '## 6. Language choice\n\nThe language of prayer is chosen by the address: a god may be addressed only in a sacred register. '
                 'S010 S011 S012 supply the comparative cases and each claim above is bounded to them.\n')
    with open(entry_ok, 'w') as f:
        f.write(good_body)
    new_rows = [('S010', 'https://example.org/a'), ('S011', 'https://example.org/b'), ('S012', 'https://example.org/c')]
    lands_e = HEADER + '\n' + _row('S001', url, good_teach) + '\n' + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n'
    for i, (rid, u) in enumerate(new_rows):
        _cap(root, rid + '.txt', f'Page text. prayer address petition votive promise fixed extempore efficacy register case {i}.')
        lands_e += _row(rid, u, 'prayer address petition votive promise register case', tier='A', status='mined',
                        opened='2026-11-04', used='corpus/knowledge/myth-symbol/prayer-register.md') + '\n'
    lands_e_path = write('lands_entry.md', lands_e)
    man_e = _manifest(root, {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u,
                                       http_status=200, fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}, 'mentry.json')
    lesson_e_text = ''.join(
        f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: '
        f'\u201cprayer address petition votive promise fixed extempore efficacy register case {i}\u201d\n'
        for i, (rid, u) in enumerate(new_rows))
    lesson_e = write('lesson_entry.md', lesson_e_text)

    def E(graded_extra=(), **over):
        base_args = dict(entry=entry_ok, base_registry=base, lands_registry=lands_e_path, lesson=lesson_e,
                         manifest=man_e, **{'capture_dir': 'reports/round-90/evidence', 'as_of': '2026-11-04',
                                            'topic': topic, 'min_bytes': '1200', 'min_headings': '4',
                                            'min_new_ids': '3', 'min_topic_overlap': '8',
                                            'table_min_rows': '5', 'table_min_cols': '3'})
        base_args.update(over)
        out = ['--root', root]
        for k, v in base_args.items():
            if v is None:
                continue
            out += ['--' + k.replace('_', '-'), v]
        out += ['--graded', 'corpus/SOURCES.md', '--graded', 'corpus/lessons/round-90.md']
        for g in graded_extra:
            out += ['--graded', g]
        return out

    chk('positive entry', ['entry'] + E(), 0, ['PASS legs=6/6'])
    filler = os.path.join(root, 'corpus/knowledge/myth-symbol/sourdough.md')
    with open(filler, 'w') as f:
        f.write('# Sourdough starter care\n\n- topic: sourdough starter care\n- sources: S010\n'
                '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                + ''.join(f'## {i}. Care\n\nFeed the starter with flour and water every day and keep it warm.\n\n' for i in range(1, 6))
                + '| a | b | c |\n|---|---|---|\n' + ''.join(f'|{i}|x|y|\n' for i in range(5)) + '\nS010 S011 S012\n')
    chk('off-topic filler entry', ['entry'] + E(entry=filler), 1, ['FAIL TOPIC'])
    filler2 = os.path.join(root, 'corpus/knowledge/myth-symbol/filler2.md')
    with open(filler2, 'w') as f:
        f.write('# Prayer\n\n- topic: prayer address petition votive promise register\n- sources: S010\n'
                '- verified-at: 2026-11-04\n- recheck: 180d\n\n## 1. Prayer\n\n'
                + ('The prayer address petition votive promise register repeats one sentence about the prayer address petition votive promise register in every section. ' * 6)
                + '\n\n## 2. Prayer\n\n| a | b | c |\n|---|---|---|\n'
                + ''.join(f'|{i}|x|y|\n' for i in range(5)) + '\nS010 S011 S012\n')
    chk('repetition filler entry', ['entry'] + E(entry=filler2), 1, ['FAIL SHAPE'])
    missing_id = os.path.join(root, 'corpus/knowledge/myth-symbol/missing.md')
    with open(missing_id, 'w') as f:
        f.write(good_body.replace('S010 S011 S012 supply', 'S010 S011 S999 supply'))
    chk('entry cites a missing id', ['entry'] + E(entry=missing_id), 1, ['FAIL NEWIDS'])
    wrong_open = write('lands_wrong.md', lands_e.replace('| mined | 2026-11-04 |', '| mined | 2026-10-19 |'))
    chk('new id not opened today', ['entry'] + E(lands_registry=wrong_open), 1, ['FAIL NEWIDS'])
    wrong_used = write('lands_used.md', lands_e.replace('myth-symbol/prayer-register.md |', 'myth-symbol/other.md |'))
    chk('used-by does not name the entry', ['entry'] + E(lands_registry=wrong_used), 1, ['FAIL NEWIDS'])
    shutil.copy(lesson_e, os.path.join(root, 'corpus/lessons/round-90.md'))
    man_graded_e = _manifest(root, {rid: dict(capture='corpus/lessons/round-90.md', url=u, http_status=200,
                                              fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}, 'mlessongraded.json')
    chk('entry capture is the lesson', ['entry'] + E(manifest=man_graded_e), 1, ['FAIL CAPTURE'])
    gate_missing = write('lesson_entry2.md', ''.join(
        f'- {rid} admit A/mined. \u2014 accessed 2026-11-04 \u2014 body: '
        f'\u201cprayer address petition votive promise fixed extempore efficacy register case {i}\u201d\n'
        for i, (rid, u) in enumerate(new_rows)))
    chk('gate line without the url', ['entry'] + E(lesson=gate_missing), 1, ['FAIL GATE'])
    tiny = os.path.join(root, 'corpus/knowledge/myth-symbol/tiny.md')
    with open(tiny, 'w') as f:
        f.write('# Prayer\n\n- topic: prayer address petition\n- sources: S010\n- verified-at: 2026-11-04\n- recheck: 180d\n')
    chk('entry too small', ['entry'] + E(entry=tiny, min_bytes='1200'), 1, ['FAIL ENTRY'])
    fewheads = os.path.join(root, 'corpus/knowledge/myth-symbol/fewheads.md')
    with open(fewheads, 'w') as f:
        f.write(good_body.replace('## 3. Fixed and extempore', '**3. Fixed and extempore**')
                .replace('## 4. Efficacy', '**4. Efficacy**'))
    chk('entry too few headings', ['entry'] + E(entry=fewheads, min_headings='5'), 1, ['FAIL ENTRY'])
    nokey = os.path.join(root, 'corpus/knowledge/myth-symbol/nokey.md')
    with open(nokey, 'w') as f:
        f.write(good_body.replace('- recheck: 180d\n', ''))
    chk('entry misses a header key', ['entry'] + E(entry=nokey), 1, ['FAIL ENTRY'])
    smalltable = os.path.join(root, 'corpus/knowledge/myth-symbol/smalltable.md')
    with open(smalltable, 'w') as f:
        f.write(good_body.replace('| petition | set | composed |\n| promise | written | spoken |\n'
                                  '| authority | text | speaker |\n| failure | ritual fault | weak speaker |\n', ''))
    chk('entry table too small', ['entry'] + E(entry=smalltable), 1, ['FAIL SHAPE'])
    thrice = os.path.join(root, 'corpus/knowledge/myth-symbol/thrice.md')
    with open(thrice, 'w') as f:
        f.write(good_body + '\nThe prayer address petition votive promise register repeats here. '
                'The prayer address petition votive promise register repeats here. '
                'The prayer address petition votive promise register repeats here.\n')
    chk('entry repeats a sentence three times', ['entry'] + E(entry=thrice), 1, ['FAIL SHAPE'])
    thin = os.path.join(root, 'corpus/knowledge/myth-symbol/thin.md')
    with open(thin, 'w') as f:
        f.write('# Prayer\n\n- topic: prayer address petition\n- sources: S010\n- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                + ''.join(f'## {i}. Note\n\nShort note.\n\n' for i in range(1, 6)) + 'S010 S011 S012\n')
    chk('entry with headings but under the byte floor', ['entry'] + E(entry=thin), 1, ['FAIL ENTRY'])
    missing_cited = os.path.join(root, 'corpus/knowledge/myth-symbol2/prayer-register.md')
    os.makedirs(os.path.dirname(missing_cited), exist_ok=True)
    with open(missing_cited, 'w') as f:
        f.write(good_body.replace('S010 S011 S012 supply', 'S010 S011 S999 supply'))
    chk('entry cites an id absent from the registry', ['entry'] + E(entry=missing_cited), 1, ['FAIL NEWIDS'])
    lands_tier = write('lands_tier.md', lands_e.replace(
        '| S012 | https://example.org/c | docs | A |', '| S012 | https://example.org/c | docs | C |'))
    chk('new id at tier C', ['entry'] + E(lands_registry=lands_tier), 1, ['FAIL NEWIDS'])
    lesson_nodate = write('lesson_nodate.md', lesson_e_text.replace('accessed 2026-11-04', 'accessed earlier'))
    chk('gate line without the access date', ['entry'] + E(lesson=lesson_nodate), 1, ['FAIL GATE'])
    longq = ' '.join(['prayer address petition votive promise fixed extempore efficacy register'] * 4)
    lesson_longq = write('lesson_longq.md', ''.join(
        f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: \u201c' +
        (longq if rid == 'S010' else f'prayer address petition votive promise fixed extempore efficacy register case {i}') +
        '\u201d\n' for i, (rid, u) in enumerate(new_rows)))
    chk('gate quote over the word bound', ['entry'] + E(lesson=lesson_longq), 1, ['FAIL GATE'])
    chk('no mode refused', ['--root', root], 2, ['choose advance or entry'])

    # ---------------------------------------------- one negative per remaining sub-check
    lands_only = write('lands_only.md', HEADER + '\n'
                       + _row('S001', url, good_teach, recheck='2027-02-03') + '\n'
                       + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n'
                       + _row('S004', 'https://example.org/four', 'a lands-only row about dye plants') + '\n')
    chk('population id not in base', ['advance'] + A(lands_registry=lands_only, population='S001,S002,S004'),
        1, ['FAIL ADVANCED', 'S004: not in base registry'])
    noniso = write('noniso.md', HEADER + '\n'
                   + _row('S001', url, good_teach, recheck='soon') + '\n'
                   + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('recheck not an ISO date', ['advance'] + A(lands_registry=noniso), 1, ['FAIL ADVANCED'])
    longq_a = ' '.join(['the fixed vocative formulae address the deity and the votive promise binds'] * 4)
    lesson_longq_a = write('lesson_longq_a.md', '- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + url
                           + ' accessed 2026-11-04: \u201c' + longq_a + '\u201d\n'
                           '- S002 LOCATED x accessed 2026-11-04: \u201cunrelated row about dye plants\u201d\n')
    chk('quote over the word bound (advance)', ['advance'] + A(lesson=lesson_longq_a), 1, ['FAIL MEANING'])
    nourl = write('nourl.md', HEADER + '\n'
                  + _row('S001', 'no url here', good_teach, recheck='2027-02-03') + '\n'
                  + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('row carries no url', ['advance'] + A(lands_registry=nourl), 1, ['FAIL ARCHIVE', 'row carries no URL'])
    man_one = _manifest(root, {'S002': dict(capture='reports/round-90/evidence/S001.txt',
                                            url='https://example.org/other',
                                            http_status=200, fetched_at='2026-11-04T19:00:00-03:00')}, 'mone.json')
    chk('manifest row absent', ['advance'] + A(manifest=man_one), 1, ['FAIL CAPTURE'])
    man_empty = _manifest(root, {'S001': dict(capture='', url=url, http_status=200,
                                              fetched_at='2026-11-04T19:00:00-03:00')}, 'mempty.json')
    chk('manifest capture empty', ['advance'] + A(manifest=man_empty), 1, ['FAIL CAPTURE'])
    cellcount = write('cellcount.md', HEADER + '\n'
                      + _row('S001', url, good_teach, recheck='2027-02-03').rstrip() + ' extra |\n'
                      + _row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n')
    chk('cell count changed', ['advance'] + A(lands_registry=cellcount), 1, ['FAIL OTHERCELLS'])
    chk('missing manifest refused', ['advance'] + A(manifest=os.path.join(root, 'noman.json')), 2, ['unreadable'])
    nonutf = os.path.join(root, 'nonutf.md')
    with open(nonutf, 'wb') as f:
        f.write(b'| S001 | \xff\xfe |\n')
    chk('non-UTF8 registry refused', ['advance'] + A(lands_registry=nonutf), 2, ['not UTF-8'])
    chk('selftest needs --work', ['--selftest'], 2, ['needs --work'])
    chk('missing --base-registry', ['advance'] + A(base_registry=None), 2, ['missing --base-registry'])
    chk('missing --as-of', ['advance'] + A(as_of=None), 2, ['missing --as-of'])
    chk('bad --as-of', ['advance'] + A(as_of='2026-13-40'), 2, ['impossible date'])
    chk('non-ISO --as-of', ['advance'] + A(as_of='yesterday'), 2, ['not an ISO date'])
    chk('missing population file', ['advance'] + A(population=None, population_file=os.path.join(root, 'nopop.txt')),
        2, ['unreadable'])
    lands_uncited = write('lands_uncited.md', lands_e
                          + _row('S013', 'https://example.org/reject', 'a rejected row about dye plants',
                                 tier='C', status='rejected', opened='2026-11-04', used='corpus/lessons/round-90.md'))
    chk('uncited new row is out of scope', ['entry'] + E(lands_registry=lands_uncited), 0, ['PASS legs=6/6'])
    shortq = write('lesson_shortq.md', ''.join(
        f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: \u201cprayer address\u201d\n'
        for rid, u in new_rows))
    chk('gate quote below the char floor', ['entry'] + E(lesson=shortq), 1, ['FAIL GATE'])
    chk('min new ids unmet', ['entry'] + E(min_new_ids='4'), 1, ['FAIL NEWIDS'])
    twocol = os.path.join(root, 'corpus/knowledge/myth-symbol/twocol.md')
    with open(twocol, 'w') as f:
        f.write(good_body.replace('| element | fixed | extempore |\n|---|---|---|\n'
                                  '| address | rote | improvised |\n| petition | set | composed |\n'
                                  '| promise | written | spoken |\n| authority | text | speaker |\n'
                                  '| failure | ritual fault | weak speaker |\n',
                                  '| element | fixed |\n|---|---|\n| address | rote |\n| petition | set |\n'
                                  '| promise | written |\n| authority | text |\n| failure | ritual |\n'))
    chk('entry table too few columns', ['entry'] + E(entry=twocol), 1, ['FAIL SHAPE'])
    offstem = os.path.join(root, 'corpus/knowledge/myth-symbol/defixio-tabellae.md')
    with open(offstem, 'w') as f:
        f.write(good_body)
    chk('filename stem absent from the entry', ['entry'] + E(entry=offstem), 1, ['FAIL TOPIC'])
    chk('topic overlap below the floor', ['entry'] + E(min_topic_overlap='40'), 1, ['FAIL TOPIC'])

    bad = [(n, got) for n, ok, rc, got, tail in checks if not ok]
    lines = [f'SELFTEST {"PASS" if not bad else "FAIL"} {len(checks) - len(bad)}/{len(checks)}']
    for n, ok, rc, got, tail in checks:
        lines.append(f'  {"ok " if ok else "BAD"} {n}: rc={got}' + ('' if ok else f' tail={tail}'))
    out = '\n'.join(lines)
    print(out)
    return 0 if not bad else 1


def main(argv):
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument('mode', nargs='?', choices=['advance', 'entry'])
    p.add_argument('--root', default='.')
    p.add_argument('--advance', action='store_true')
    p.add_argument('--entry', dest='entry_path')
    p.add_argument('--base-registry')
    p.add_argument('--lands-registry')
    p.add_argument('--lesson')
    p.add_argument('--manifest')
    p.add_argument('--capture-dir', default='')
    p.add_argument('--as-of', default='')
    p.add_argument('--population')
    p.add_argument('--population-file')
    p.add_argument('--min-advanced', type=int, default=1)
    p.add_argument('--window-days', type=int, default=90)
    p.add_argument('--max-days', type=int, default=366)
    p.add_argument('--min-overlap', type=int, default=1)
    p.add_argument('--quote-max-words', type=int, default=25)
    p.add_argument('--quote-min-chars', type=int, default=20)
    p.add_argument('--graded', action='append', default=[])
    p.add_argument('--min-bytes', type=int, default=8000)
    p.add_argument('--min-headings', type=int, default=5)
    p.add_argument('--min-new-ids', type=int, default=3)
    p.add_argument('--min-topic-overlap', type=int, default=8)
    p.add_argument('--table-min-rows', type=int, default=5)
    p.add_argument('--table-min-cols', type=int, default=3)
    p.add_argument('--topic', default='')
    p.add_argument('--receipt')
    p.add_argument('--json', action='store_true')
    p.add_argument('--selftest', action='store_true')
    p.add_argument('--work')
    args = p.parse_args(argv)
    try:
        if args.selftest:
            if not args.work or not os.path.isdir(args.work):
                raise Refused('--selftest needs --work <existing-dir>')
            return selftest(args.work)
        args.advance = args.advance or args.mode == 'advance'
        args.entry = args.entry_path
        if not args.advance and not args.entry:
            raise Refused('choose advance or entry')
        for req in ('base_registry', 'lands_registry', 'lesson', 'manifest', 'as_of'):
            if not getattr(args, req):
                raise Refused(f'missing --{req.replace("_", "-")}')
        if args.advance and not (args.population or args.population_file):
            raise Refused('advance mode needs --population or --population-file')
        return cli(args)
    except Refused as exc:
        print(f'ADVANCE-EVIDENCE_ERROR: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
