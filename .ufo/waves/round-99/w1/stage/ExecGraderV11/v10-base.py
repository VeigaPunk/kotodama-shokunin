#!/usr/bin/env python3
"""Grade a registry re-verification advance or a coverage entry against its evidence.

Round-93 successor (v4) to the round-92 revision. The round-92 non-author
closure routed 16 counterfeit survivors plus one unnamed crash
(corpus/lessons/round-92.md R92-M7; CriticClaims92 attacks.md; spot-check §6
item 4). v4 refuses each by name:

  UNIQUENESS (+) the shadow/duplicate URL comparison folds scheme (http->https),
                 strips a leading www., drops the query string and case-folds the
                 path, so scheme-swapped, www-prefixed, query-suffixed and
                 path-case variants of a base or sibling URL still collide
  CAPTURE (+)    a capture text-identical (normalized) to a graded file is
                 refused even when a trailing newline differs; a symlinked
                 capture is refused; the gate quote must occur in the capture's
                 body text (HTML markup, tag attributes and metadata content
                 are stripped before matching)
  TOPIC (+)      a phrase anchor surface is an h2 heading carrying >= 2 raw
                 tokens or a table DATA row (below the |---| separator); the
                 header row and single-token span-gaming headings anchor nothing
  BASEROWS       no base registry row is removed and no identity cell (id,
                 source, kind, tier, scope, anchor, teaches, opened) changes
                 between base and lands (only status, recheck, used-by may move)
  APPENDONLY (+) the disposition scanner strips zero-width characters and also
                 reads dispositions wrapped in bold or table pipes (id and an
                 uppercase LOCATED / NOT LOCATED token anywhere in the line);
                 lowercase prose mentions stay clean
  refusal (+)    a manifest that is not a JSON object, or whose rows are a list,
                 is refused with a named diagnostic (no traceback)

Round-92 v3 history and the advance-mode legs are unchanged.

Round-91 successor (v2) to the round-90 revision. The round-90 falsify wave
(.ufo/waves/round-90/w1/CriticClaims.md, attacks 5, 6, 8) showed the entry mode
passed a bakery-rota off-topic entry (TOPIC token count), shadow/duplicate rows,
a gate quote equal to the row's own teaches cell, a capture byte-copying a
graded file, and a freshness re-verification hidden in the lesson channel.
v2 refuses each of those classes by name in entry mode:

  UNIQUENESS   duplicate ids anywhere in the lands registry; a qualifying new
               row whose URL is already a base row's URL (shadow); two
               qualifying new rows sharing one URL
  GATE (+)     the gate quote may not be a substring of the row's teaching cell
               or of the row's source cell (self-quote and title/chrome classes)
  CAPTURE (+)  a capture whose bytes equal a graded file's bytes is refused even
               under a different path
  TOPIC (+)    declared sub-topic phrases must appear in the entry's h2 headings
               or table cells, not merely in running prose
  APPENDONLY   with --base-lesson: no id outside the round's new rows may gain a
               disposition line or flip its verdict in the round lesson (the
               lesson channel cannot carry a freshness move as coverage)

Round-90 v1 history and the advance-mode legs are unchanged.

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
Round-96 v8 refuses the nine fresh CriticO95 classes named: VERDICT-NBSP (NB1,
U+00A0), VERDICT-VT (VT1), VERDICT-FF (FF1), VERDICT-LINESEP (LS1, with its
U+2029 / U+001C-U+001E family), VERDICT-NEL (NEL1), VERDICT-ANSI (ANSI1),
ID-NONASCII for homoglyph id letters (CYR1), and bracketed/separator-dash
numbered headings (BR1/DASH1, refused on TOPIC). Verdict-channel checks read
lesson lines on \n only, before any splitlines severing. ZWNJ stays benign
(not refused) and F1's TOPIC refusal is unchanged.

Round-97 v9 refuses the seven CriticO96 survivors still passing v8 (measured,
reports/round-97/controls/critic96-on-v8.txt): VERDICT-CTRL names the codepoint
for the remaining C0 controls inside a verdict token (CR1 U+000D, US1 U+001F,
NUL1 U+0000 and family), VERDICT-SEPARATOR names the codepoint for the
remaining Zs space separators (OGH1 U+1680, IS1 U+3000 and family), and
mark-degraded h2 headings (Mn/Me in a numbering token or phrase word) are
refused on TOPIC as HEADING-COMBINING (CM1/CMW2). CR-only line breaks still
parse as line breaks; tabs keep VERDICT-TAB; ZWNJ stays benign.

"""

import argparse
import datetime
import hashlib
import html as _html
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
DISPO_RE = re.compile(r'^(?:[>\-\*+\s]*\s)?S(\d{3,})\b.*?\b(NOT[ _-]?LOCATED|LOCATED)\b', re.I)
# Round-93 v4 (routed R92-M7 A5d/A5e/A5f): an unanchored, case-SENSITIVE fallback
# reads dispositions wrapped in markdown bold or table pipes, and a verdict
# obscured by zero-width characters. Lowercase prose ("S001 located in the
# archive") carries no uppercase verdict token and stays clean.
DISPO_ANY_RE = re.compile(r'\bS(\d{3,})\b.*?\b(NOT[ _-]?LOCATED|LOCATED)\b')
# Round-94 v5 (routed round-93 K1 / dispo-any-casei pin): a case-insensitive view of
# the fallback, used only to DETECT a lowercase unanchored verdict for a named
# refusal; the matching fallback above stays case-sensitive (v4).
DISPO_ANY_RE_I = re.compile(DISPO_ANY_RE.pattern, re.I)
# Round-94 v5 (routed round-93 A1/B1/J1): the verdict-normalisation strip now also
# takes the soft hyphen (U+00AD); ZW_ONLY keeps the v4 zero-width set for the raw
# re-test; DASH_MAP folds typographic dashes to '-' so a dash inside NOT-LOCATED
# written with an en-dash reads as NOT-LOCATED instead of flipping the direction;
# HOMOGLYPH_MAP folds common Cyrillic/Greek lookalike letters, for detection only.
ZW_ONLY = dict.fromkeys(map(ord, '\u200b\u200c\u200d\u2060\ufeff'))
ZW_MAP = dict.fromkeys(map(ord, '\u200b\u200c\u200d\u2060\ufeff\u00ad'))
DASH_MAP = dict.fromkeys(map(ord, '\u2010\u2011\u2012\u2013\u2014\u2015\u2212\uff0d'), '-')
HOMOGLYPH_MAP = {ord(c): t for c, t in (
    '\u0410A \u0412B \u0421C \u0415E \u041dH \u041aK \u041cM \u041eO \u0420P \u0422T \u0425X '
    '\u0430a \u0435e \u043eo \u0440p \u0441c \u0443y \u0445x \u039fO \u03bfo \u0395E \u03b5e').split()}
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


def norm_url(u):
    """Normalize a URL for shadow/duplicate comparison: lowercase the scheme and
    host, drop a #fragment and default ports, strip trailing slashes (round-91
    routed V3: a base url plus a #fragment previously passed the shadow check).
    Round-93 v4 (routed R92-M7 A2c-A2f): the comparison key also folds the scheme
    to https, strips a leading www., drops the query string and case-folds the
    path, so scheme-swapped, www-prefixed, query-suffixed and path-case variants
    of the same page collide. This is a comparison key only: the row cell keeps
    its original URL, and surface/capture binding still compares exact strings."""
    u = str(u).strip().split('#', 1)[0]
    m = re.match(r'^([a-zA-Z][a-zA-Z0-9+.\-]*)://([^/?#]*)(.*)$', u)
    if not m:
        return u.rstrip('/')
    scheme = m.group(1).lower()
    host = m.group(2).lower()
    if (scheme == 'http' and host.endswith(':80')) or (scheme == 'https' and host.endswith(':443')):
        host = host.rsplit(':', 1)[0]
    if scheme in ('http', 'https'):
        scheme = 'https'
    if host.startswith('www.'):
        host = host[4:]
    rest = m.group(3)
    rest = rest.split('?', 1)[0]
    rest = rest.lower()
    return scheme + '://' + host + rest.rstrip('/')


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


def _dispo_match(stripped):
    """v4 matching shape, factored: anchored rule first, then the case-sensitive
    unanchored fallback over unmarked text."""
    m = DISPO_RE.match(stripped)
    if not m:
        plain = stripped.replace('|', ' ').replace('*', ' ').replace('_', ' ')
        m = DISPO_ANY_RE.search(plain)
    return m


def _refuse_verdict_channel(n, line):
    """Round-96 v8 (routed CriticO95 NB1/VT1/FF1/LS1/NEL1/ANSI1/CYR1): read
    the RAW line (before any splitlines severing and before ZW/DASH
    stripping) and refuse a named diagnostic when a plausible disposition
    hides a forged token. Two gated channels: (1) a verdict window - a
    LOCATED/NOT-LOCATED/LO??CATED-like span bounded by whitespace - carrying
    NBSP/VT/FF/line-separator/NEL/ESC characters is refused under the
    VERDICT-* name for that codepoint; (2) a plausible id token carrying a
    non-ASCII letter (homoglyph) is refused as ID-NONASCII before the
    ASCII-id gate ever runs. The ZWNJ U+200C is on no blocklist and stays
    benign (proven by the round-96 ZWNJ1 control). Round-97 v9 (routed
    CriticO96 CR1/US1/NUL1/OGH1/IS1) extends the same window: the remaining
    C0 controls are refused as VERDICT-CTRL and the Zs space separators as
    VERDICT-SEPARATOR, each refusal naming the codepoint; tabs keep the
    VERDICT-TAB channel below."""
    # Gate on a plausible disposition: narrow to windows that look like one.
    _up = line.upper()
    if 'LOCATED' not in _up and 'LO' not in _up and 'ATED' not in _up:
        return
    for m in re.finditer(r'\S*(?:LOCATED|LO[\s\S]{0,10}TED|NOT[\s\S]{0,6}LOCATED)\S*', line, re.I):
        span = m.group(0)
        if '\u00a0' in span:
            raise Refused(f'line {n}: verdict token carries a non-breaking space (VERDICT-NBSP)')
        if '\u000b' in span:
            raise Refused(f'line {n}: verdict token carries a vertical tab (VERDICT-VT)')
        if '\u000c' in span:
            raise Refused(f'line {n}: verdict token carries a form feed (VERDICT-FF)')
        for cpv in ('\u2028', '\u2029', '\u001c', '\u001d', '\u001e'):
            if cpv in span:
                raise Refused(f'line {n}: verdict token carries a line separator (VERDICT-LINESEP)')
        if '\u0085' in span:
            raise Refused(f'line {n}: verdict token carries a NEL (VERDICT-NEL)')
        if '\u001b' in span:
            raise Refused(f'line {n}: verdict token carries an ANSI escape (VERDICT-ANSI)')
        # Round-97 v9 (routed CriticO96 CR1/US1/NUL1/OGH1/IS1): the remaining C0
        # controls and the Zs space separators inside a verdict token are refused
        # by name, each message naming the codepoint. Tabs keep the VERDICT-TAB
        # channel, the codepoints named above keep their v8 refusal names, plain
        # U+0020 stays a legitimate verdict spacing (the anchored rule reads
        # "NOT LOCATED"), and a lone U+000D that only terminates a line never
        # reaches this loop.
        for c in span:
            o = ord(c)
            if o in (0x09, 0x0b, 0x0c, 0x1b, 0x1c, 0x1d, 0x1e, 0x85, 0x20) or c == '\u00a0':
                continue
            if unicodedata.category(c) == 'Cc':
                raise Refused(f'line {n}: verdict token carries control character '
                              f'U+{o:04X} (VERDICT-CTRL)')
            if unicodedata.category(c)[0] == 'M' and o != 0x200c:
                raise Refused(f'line {n}: verdict token carries a combining mark '
                              f'U+{o:04X} (VERDICT-COMBINE)')
            if unicodedata.category(c) == 'Zs':
                raise Refused(f'line {n}: verdict token carries space separator '
                              f'U+{o:04X} (VERDICT-SEPARATOR)')
    for tok in re.findall(r'\S*?[A-Za-z\u0080-\uFFFF]\d{3,}\b', line):
        if not re.fullmatch(r'[Ss]\d{3,}', tok):
            core = tok.strip('|-*<>_`#')
            if len(core) >= 2 and any(ord(c) > 127 and unicodedata.category(c).startswith('L') for c in core):
                # only when the non-ASCII one-letter + 3 digits could be an id
                if re.search(r'\d{3,}$', core):
                    raise Refused(f'line {n}: id token carries a non-ASCII lookalike letter (ID-NONASCII)')
def _refuse_disguised(n, stripped):
    """Round-94 v5 (routed round-93 A1/K1): an id line whose verdict token hides
    behind non-ASCII letters or lowercase spelling is refused on a named
    diagnostic instead of being silently invisible to APPENDONLY.
    Round-95 v6 (routed CriticO94 CD1/LR1/TAB1/ID1): the same applies when the
    verdict token carries a combining mark (Mn), a format character outside
    the zero-width strip set (Cf such as U+200E LRM), or whitespace inside the
    token, and when the id token carries a non-ASCII letter lookalike
    (such as U+A731 in place of S). A verdict token that matches is still
    checked, so a tab inside it cannot pass silently."""
    probe = unicodedata.normalize('NFKC', stripped).translate(HOMOGLYPH_MAP)
    plain = stripped.replace('|', ' ').replace('*', ' ').replace('_', ' ')
    m = _dispo_match(plain)
    if m:
        verdict_raw = m.group(2)
        if any(unicodedata.category(c)[0] == 'M' and ord(c) != 0x200c for c in verdict_raw):
            raise Refused(f'line {n}: verdict token carries a combining mark (VERDICT-COMBINE)')
        if any(unicodedata.category(c) == 'Cf' and ord(c) not in ZW_MAP for c in verdict_raw):
            raise Refused(f'line {n}: verdict token carries a format character (VERDICT-FORMAT)')
    # CD1/LR1 recovery: NFKD strips combining marks from the verdict
    # spelling; stripping out-of-set Cf removes LRM/RLO etc. If either
    # recovered spelling matches but the plain spelling does not, the line
    # is a disguised disposition, refused on its named channel.
    nfkd = unicodedata.normalize('NFKD', stripped)
    nfkd_nomark = ''.join(c for c in nfkd if unicodedata.category(c)[0] != 'M')
    if _dispo_match(nfkd_nomark.replace('|', ' ').replace('*', ' ').replace('_', ' ')) and not m:
        raise Refused(f'line {n}: verdict token carries a combining mark (VERDICT-COMBINE)')
    nocf = ''.join(c for c in stripped if not (unicodedata.category(c) == 'Cf' and ord(c) not in ZW_MAP))
    if _dispo_match(nocf.strip().translate(ZW_MAP).translate(DASH_MAP)) and not m and nocf != stripped:
        raise Refused(f'line {n}: verdict token carries a format character (VERDICT-FORMAT)')
    # Whitespace inside a split verdict word (TAB1): LO<TAB>CATED etc.
    if '\t' in stripped and re.search(r'LO\s+CATED|NOT\s+LOCATED', stripped, re.I):
        raise Refused(f'line {n}: verdict token carries whitespace (VERDICT-TAB)')
    if not re.search(r'\b[Ss]\d{3,}\b', probe):
        return
    if DISPO_ANY_RE_I.search(plain) and not _dispo_match(plain):
        raise Refused(f'line {n}: lowercase verdict token outside the anchored rule (VERDICT-LOWERCASE)')
    if _dispo_match(probe) and not _dispo_match(plain):
        raise Refused(f'line {n}: verdict token carries non-ASCII letters (VERDICT-NONASCII)')


def dispositions(lesson):
    """First disposition per id; every NOT-LOCATED spelling collapses to NOT-LOCATED.
    Round-93 v4: the line is first stripped of zero-width characters; the anchored
    rule keeps its old shape, and a case-sensitive unanchored fallback catches
    bold-wrapped and table-pipe dispositions.
    Round-94 v5 (routed round-93 A1/B1/J1/K1): the verdict-normalisation path also
    strips the soft hyphen and folds typographic dashes to '-', so NOT-LOCATED
    written with an en-dash reads as NOT-LOCATED and is never misparsed as a
    LOCATED flip; a verdict token hidden behind a soft hyphen, non-ASCII letters
    or lowercase spelling is refused on a named diagnostic, never invisible."""
    out = {}
    for _rn, _rl in enumerate(lesson.split('\n'), 1):
        _refuse_verdict_channel(_rn, _rl)
    for n, line in enumerate(lesson.splitlines(), 1):
        stripped = line.strip().translate(ZW_MAP).translate(DASH_MAP)
        m = _dispo_match(stripped)
        if m and '\u00ad' in line and not _dispo_match(line.strip().translate(ZW_ONLY).translate(DASH_MAP)):
            raise Refused(f'line {n}: soft hyphen inside the verdict token (VERDICT-SOFTHYPHEN)')
        if m:
            _refuse_disguised(n, stripped)
        if not m:
            _refuse_disguised(n, stripped)
            continue
        rid, verdict = 'S' + m.group(1), m.group(2).upper().replace('_', ' ').replace('-', ' ')
        verdict = 'NOT-LOCATED' if verdict.startswith('NOT') else 'LOCATED'
        if rid not in out:
            out[rid] = (verdict, stripped)
    return out


def gate_quotes(lesson):
    """id -> list of (line, quoted span), one entry per quoted span on each line
    that names the id, in line order. The first entry is the advance-mode quote;
    entry mode binds every entry (round-93 v4, routed R92-M7 A6f)."""
    out = {}
    for line in lesson.splitlines():
        ids = re.findall(r'\bS\d{3,}\b', line)
        if not ids:
            continue
        for m in QUOTE_RE.finditer(line):
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


def html_body_text(raw):
    """Body text of a capture: HTML markup, comments, script/style blocks and tag
    attributes (including meta content attributes) are stripped before matching,
    so a quote that exists only in raw markup does not count as located body text
    (round-93 v4, routed R92-M7 A6e). Non-HTML bytes pass through unchanged."""
    s = raw.decode('utf-8', errors='replace')
    if '<' not in s[:4096]:
        return s
    s = re.sub(r'(?is)<(script|style)\b[^>]*>.*?</\1\s*>', ' ', s)
    s = re.sub(r'(?s)<!--.*?-->', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return _html.unescape(s)


def capture_error(cap_dir, graded, man_entry, quote, as_of, root, graded_shas=None, graded_norms=None):
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
    if os.path.islink(path):
        return f'capture is a symlink: {rel}'
    try:
        with open(path, 'rb') as f:
            raw = f.read()
    except OSError:
        return f'capture not committed: {rel}'
    if hashlib.sha256(raw).hexdigest() != str(m.get('sha256', '')):
        return f'capture sha256 mismatch: {rel}'
    if graded_shas:
        hit = graded_shas.get(hashlib.sha256(raw).hexdigest())
        if hit:
            return f'capture byte-copies a graded file ({hit}) under a different path: {rel}'
    ntext = norm(raw.decode('utf-8', errors='replace'))
    if graded_norms:
        hitn = graded_norms.get(ntext)
        if hitn:
            return f'capture text-copies a graded file ({hitn}) under a different path: {rel}'
    if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:
        return f'capture http_status not 2xx: {rel}'
    fm = FETCH_RE.match(str(m.get('fetched_at', '')))
    if not fm:
        return f'fetched_at not a local ISO instant with offset: {m.get("fetched_at")!r}'
    if fm.group(1) != as_of:
        return f'fetched_at date {fm.group(1)} != as_of {as_of}'
    text = norm(html_body_text(raw))
    if norm(quote) not in text:
        return f'quote absent from capture body text: {rel}'
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
    # Round-94 v5 (routed round-93 H1): a row value that is not a JSON object is a
    # named refusal, not an AttributeError at the surface/capture loop.
    if not isinstance(man_rows, dict):
        raise Refused('manifest rows is not a JSON object (list where mapping expected)')
    bad_man_rows = sorted(str(rid) for rid, val in man_rows.items() if not isinstance(val, dict))
    if bad_man_rows:
        raise Refused('manifest row value is not a JSON object (list where mapping expected): '
                      + ','.join(bad_man_rows) + ' (MANIFEST-ROW-TYPE)')
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
                seen_url.setdefault(norm_url(u), set()).add(r['id'])
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
    base_rows, _ = registry(read(args.base_registry))
    base_ids = set(r['id'] for r in base_rows)
    lands_rows, lands_dup = registry(read(args.lands_registry))
    lands_ids = set(r['id'] for r in lands_rows)
    lesson = read(args.lesson)
    man = json.loads(read(args.manifest) or '{}')
    if not isinstance(man, dict):
        raise Refused('manifest is not a JSON object')
    man_rows = man.get('rows', man)
    if not isinstance(man_rows, dict):
        raise Refused('manifest rows is not a JSON object (list where mapping expected)')
    # Round-94 v5 (routed round-93 H1): a row VALUE that is a list is a named
    # refusal, not an AttributeError at the GATE/CAPTURE loop.
    bad_man_rows = sorted(str(rid) for rid, val in man_rows.items() if not isinstance(val, dict))
    if bad_man_rows:
        raise Refused('manifest row value is not a JSON object (list where mapping expected): '
                      + ','.join(bad_man_rows) + ' (MANIFEST-ROW-TYPE)')
    as_of = as_date(args.as_of, '--as-of')
    legs = []
    detail = {}

    # Byte digests and normalized text of every graded file, so a capture that
    # copies one is refused even under a different path, byte-exactly (sha map)
    # or modulo whitespace normalization (round-93 v4, routed R92-M7 A3b).
    graded_shas = {}
    graded_norms = {}
    for g in list(args.graded) + [args.lesson, args.lands_registry, args.entry,
                                  args.base_registry, 'corpus/README.md', args.manifest]:
        p = os.path.join(args.root, g)
        if os.path.isfile(p):
            with open(p, 'rb') as f:
                raw = f.read()
            graded_shas[hashlib.sha256(raw).hexdigest()] = g
            graded_norms[norm(raw.decode('utf-8', errors='replace'))] = g

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

    # TOPIC — token overlap, plus the declared sub-topic phrases must appear in
    # h2 headings or table cells (round-90 attack 5: a negation list in running
    # prose cleared a token count; headings and table cells cannot be negated away).
    topic_line = next((l for l in entry.splitlines() if l.strip().startswith('- topic:')), '')
    # round-91 routed V2: the overlap floor is computed on non-heading, non-table
    # prose only, so one bridge sentence cannot carry the whole topic, and the
    # phrase anchors must span more than one heading (a bare list-stuffing h2
    # cannot satisfy them alone).
    body_text = '\n'.join(l for l in entry.splitlines()
                          if not l.strip().startswith('|') and not l.startswith('#'))
    shared = overlap(body_text, args.topic)
    stem_words = [w for w in re.split(r'[-_.]', os.path.basename(args.entry)) if len(w) >= 4]
    stem_hit = sum(1 for w in stem_words if norm(w) in norm(entry))
    problems = []
    if shared < args.min_topic_overlap:
        problems.append(f'entry prose shares {shared} content words with the declared topic < {args.min_topic_overlap}')
    if stem_words and stem_hit == 0:
        problems.append('entry filename words absent from its text')
    phrase_detail = ''
    phrases = [p.strip() for p in re.split(r'[;]', args.topic_phrases or '') if p.strip()]
    phrase_floor = getattr(args, 'min_topic_phrases', 0) or 0
    if phrases and phrase_floor > 0:
        # Round-97 v9 (routed CriticO96 CM1/CMW2): combining marks (categories
        # Mn/Me) in an h2 heading's numbering token or phrase words must not
        # count toward anchoring - a mark-degraded heading is refused on TOPIC
        # by name before any anchor is counted. Precomposed letters (Ll) are
        # unaffected and ZWNJ U+200C (Cf) stays benign (round-96 ZWNJ1 control).
        for _h in heads:
            if any(unicodedata.category(_c)[0] == 'M' for _c in _h):
                problems.append('h2 heading carries a combining mark (HEADING-COMBINING)')
                break
        # Round-98 v10 (routed CriticO97 ROMAN1/SUP1/FWPER1): a numbering token
        # built from non-ASCII numerals (category Nl/No, e.g. U+2160 roman,
        # superscript digits) or ending in a non-ASCII full stop (U+FF0E and
        # similar) is a list mark, not heading content - a heading that would
        # anchor only through it is refused on TOPIC by name. ROMANOK stays
        # clean (the token is stripped, the real heading words anchor).
        def _nonascii_number(tok):
            core = tok.strip('\uFF0E\u3002\uFE52\uFF61.')
            return bool(core) and all(unicodedata.category(c)[0] in ('N', 'L')
                                      or c in '.\uFF0E\u3002\uFE52\uFF61' for c in core) and \
                any(ord(c) > 127 and unicodedata.category(c)[0] == 'N' for c in core) or \
                any(tok.endswith(p) and not tok.endswith('.') or tok[-1:] in '\uFF0E\u3002\uFE52\uFF61' for p in []) or \
                (any(ord(c) > 127 and unicodedata.category(c)[0] == 'N' for c in tok)) or \
                (tok and tok[-1] in '\uFF0E\u3002\uFE52\uFF61' and any(c.isdigit() or unicodedata.category(c)[0] == 'N' for c in tok))
        for _h in heads:
            _toks = _h.lstrip('#').split()
            if len(_toks) >= 1 and _nonascii_number(_toks[0]):
                _rest = [t for t in _toks[1:] if not _nonascii_number(t)]
                if len(_rest) < 1:
                    problems.append('h2 heading numbering token is non-ASCII numerals or full stop (HEADING-NUMBER)')
                    break
        # Round-93 v4 (routed R92-M7 A4a): a heading anchors only when it carries
        # at least two raw tokens after the marks, and a table line anchors only
        # when it is a data row below the |---| separator — the header row and
        # single-token span-gaming headings anchor nothing.
        def _content_toks(h):
            # Round-95 v6 (routed CriticO94 NUM1/RM1/NUM2): for the span count,
            # numbering from every position is not a content token - nested
            # digits ("1.1"), roman numerals (I./II./III./IV./V.), and a
            # second-token number ("Notes 1)") never supply anchor tokens. A
            # second-token number turns the heading into a single content
            # surface: "Notes 1) address" counts as one token.
            raw = h.lstrip('#').split()
            # Round-96 v8 (routed CriticO95 BR1/DASH1): bracketed numbers
            # "(1)" and a separator dash "-" are list marks, not content.
            _NUM2 = re.compile(r'^(\d+[.)]?|\d+\.\d+[.)]?|[IVXLCDM]+[.)]?|[ivxlcdm]+[.)]?|\(?\d+[.)]?\)?|[\u2010-\u2015-]+)$')
            def isnum(t):
                return bool(_NUM2.match(t)) or _nonascii_number(t)
            if len(raw) >= 3 and isnum(raw[1]):
                raw = raw[2:]
            toks = [t for t in raw if not isnum(t)]
            return toks

        def head_anchors(h):
            # v5 shape kept: >= 2 raw tokens after the marks (number counts).
            return len(h.lstrip('#').split()) >= 2

        def head_span_anchors(h):
            # Round-94 v5 (routed round-93 G1): a leading list number is not a
            # heading token for the span count, so "## 1. address" - number plus
            # one bare phrase word - is not a second anchoring surface.
            # Round-95 v6 extends the strip to nested/roman/second-token numbers.
            toks = _content_toks(h)
            return len(toks) >= 2
        qual_rows = []
        sep_seen = False
        for l in entry.splitlines():
            s = l.strip()
            if not s.startswith('|'):
                continue
            if re.match(r'^\|[\s:\-|]+\|$', s):
                sep_seen = True
                continue
            if sep_seen:
                qual_rows.append(l)
        hit_heads = [h for h in heads if head_anchors(h) and any(norm(p) in norm(h) for p in phrases)]
        span_heads = [h for h in heads if head_span_anchors(h) and any(norm(p) in norm(h) for p in phrases)]
        hit_rows = [l for l in qual_rows if any(norm(p) in norm(l) for p in phrases)]
        anchor_text = norm(' '.join(hit_heads)) + ' ' + norm('\n'.join(hit_rows))
        hits = [p for p in phrases if norm(p) in anchor_text]
        # Round-94 v5 (routed round-93 G1): the span counts only headings that
        # anchor without their leading list number.
        span = len(span_heads) + (1 if hit_rows else 0)
        min_span = getattr(args, 'min_anchor_span', 0) or 0
        phrase_detail = f'phrase anchors {len(hits)}/{len(phrases)} spanning {span} heading/table surfaces'
        if len(hits) < phrase_floor:
            problems.append(f'{len(hits)} of {len(phrases)} sub-topic phrases in headings/table cells < {phrase_floor}')
        if span < min_span:
            problems.append(f'phrase anchors span {span} heading/table surfaces < {min_span}')
    legs.append(('TOPIC', not problems, f'>={args.min_topic_overlap} shared content words with the declared topic' + (f'; >={phrase_floor} phrase anchors in headings/table' if phrases and phrase_floor > 0 else ''), 'clean' if not problems else '; '.join(problems) + (('' if not problems else '; ') + phrase_detail if phrase_detail else phrase_detail)))

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
        # Round-94 v5 (routed round-93 I1): a registry row shorter than the
        # eleven-cell census grammar is a named refusal, not an IndexError.
        if len(cells) < 11:
            problems.append(f'{rid}: registry row has {len(cells)} cells < 11')
            continue
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

    # UNIQUENESS — shadow and duplicate classes (round-90 attacks 6/8, V1/V2):
    # no duplicate id anywhere in the lands registry; no qualifying new row
    # whose URL is already a base row's URL; no two qualifying rows sharing a URL.
    uniq = []
    if lands_dup:
        uniq.append('duplicate ids at lands: ' + ','.join(sorted(set(lands_dup))))
    base_urls = {}
    for r in base_rows:
        for u in urls(r['cells'][1] if len(r['cells']) > 1 else ''):
            base_urls.setdefault(norm_url(u), set()).add(r['id'])
    qual_urls = {}
    for rid in qualifying:
        for u in urls(byid[rid][0]['cells'][1] if len(byid[rid][0]['cells']) > 1 else ''):
            qual_urls.setdefault(norm_url(u), []).append(rid)
            if norm_url(u) in base_urls:
                uniq.append(f'{rid}: url shadows base row {",".join(sorted(base_urls[norm_url(u)]))}: {u}')
    for u, owners in qual_urls.items():
        if len(owners) > 1:
            uniq.append('url shared by ' + ','.join(sorted(owners)) + ': ' + u)
    legs.append(('UNIQUENESS', not uniq, 'no duplicate lands id, no base-url shadow, no shared new url', 'clean' if not uniq else '; '.join(uniq)))

    # BASEROWS — round-93 v4 (routed R92-M7 A6a/A6b): a base registry row may not
    # be removed at lands, and its identity cells (id, source, kind, tier, scope,
    # anchor, teaches, opened) may not change; only status, recheck and used-by
    # may move under the append-only registry discipline.
    base_byid = by_id(base_rows)
    lands_byid = by_id(lands_rows)
    baserow = []
    for rid, brows in base_byid.items():
        lrows = lands_byid.get(rid)
        if not lrows:
            baserow.append(f'{rid}: base row removed from the lands registry')
            continue
        b, l = brows[0]['cells'], lrows[0]['cells']
        if len(b) != len(l):
            baserow.append(f'{rid}: cell count {len(b)} -> {len(l)}')
            continue
        # Round-94 v5 (routed round-93 I1): a row shorter than the eleven-cell
        # census grammar is a named refusal, not an IndexError on the identity loop.
        if len(b) < 11:
            baserow.append(f'{rid}: registry row has {len(b)} cells < 11')
            continue
        for i in (0, 1, 2, 3, 4, 5, 6, 8):
            if b[i] != l[i]:
                baserow.append(f'{rid}: identity cell {i} changed: {b[i][:40]!r} -> {l[i][:40]!r}')
    legs.append(('BASEROWS', not baserow,
                 'no base registry row removed; identity cells id/source/kind/tier/scope/anchor/teaches/opened unchanged',
                 'clean' if not baserow else '; '.join(baserow[:6])))

    # GATE + CAPTURE
    gates = gate_quotes(lesson)
    gate, capture = [], []
    cap_owners = {}
    for rid in qualifying:
        row = byid[rid][0]
        src = row['cells'][1]
        teaches = row['cells'][6] if len(row['cells']) > 6 else ''
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
        q = norm(quote)
        if q and q in norm(src):
            gate.append(f'{rid}: gate quote is copied from the row source cell (title or chrome), not located prose')
        elif q and q in norm(teaches):
            gate.append(f'{rid}: gate quote is the row teaching cell (self-quote)')
        # round-91 routed V7: a quote found only in site chrome inside the capture
        # still passes the substring arms; bind it to the row's teaching cell or
        # the manifest's recorded quote by content-word overlap.
        man_q = str((man_rows.get(rid) or {}).get('quote', ''))
        bound = max(overlap(quote, teaches), overlap(quote, man_q))
        if bound < args.min_gate_overlap:
            gate.append(f'{rid}: gate quote shares < {args.min_gate_overlap} content words with teaching/manifest quote (chrome or unrelated)')
        # round-91 routed V12: the manifest surface is bound to the row's own url,
        # and one capture file may not serve two qualifying ids.
        man_entry = man_rows.get(rid)
        err = surface_error((man_entry or {}).get('url', ''), src, args.as_of)
        if err:
            capture.append(f'{rid}: {err}')
        err = capture_error(args.capture_dir, list(args.graded), man_entry, quote, args.as_of, args.root,
                            graded_shas=graded_shas, graded_norms=graded_norms)
        if err:
            capture.append(f'{rid}: {err}')
        rel = str((man_entry or {}).get('capture', '')).strip()
        if rel:
            cap_owners.setdefault(rel, []).append(rid)
    for rel, owners in sorted(cap_owners.items()):
        if len(owners) > 1:
            capture.append('capture shared by ' + ','.join(owners) + ': ' + rel)
    # round-93 v4 (routed R92-M7 A6f): every quoted span after the first on a
    # gate line must bind to the row's teaching cell or manifest quote by content
    # words, like the first; a chrome or unrelated second quote is refused.
    for rid in qualifying:
        row_teaches = byid[rid][0]['cells'][6] if len(byid[rid][0]['cells']) > 6 else ''
        man_q_extra = str((man_rows.get(rid) or {}).get('quote', ''))
        for extra_line, extra_q in gates.get(rid, [])[1:]:
            if len(extra_q.split()) > args.quote_max_words or len(norm(extra_q)) < args.quote_min_chars:
                gate.append(f'{rid}: extra quote {len(extra_q.split())} words / {len(norm(extra_q))} chars out of bounds')
            if overlap(extra_q, row_teaches) < args.min_gate_overlap and overlap(extra_q, man_q_extra) < args.min_gate_overlap:
                gate.append(f'{rid}: extra gate quote shares < {args.min_gate_overlap} content words with teaching/manifest quote (chrome or unrelated)')
    legs.append(('GATE', not gate, 'each new id has a located gate line bound to the row teaching', 'clean' if not gate else '; '.join(gate)))
    legs.append(('CAPTURE', not capture, 'each gate quote occurs in its committed capture', 'clean' if not capture else '; '.join(capture)))

    # APPENDONLY — the lesson channel cannot carry a freshness move as coverage
    # (round-90 attack 8 V4): with --base-lesson, no id outside this round's new
    # rows may gain a disposition line or flip its verdict in the round lesson.
    if getattr(args, 'base_lesson', None):
        base_disp = dispositions(read(args.base_lesson))
        lands_disp = dispositions(lesson)
        moved = []
        for rid, (verdict, _line) in lands_disp.items():
            if rid in set(new_ids):
                continue
            if rid not in base_disp:
                moved.append(f'{rid}: gained a {verdict} line not present at base')
            elif base_disp[rid][0] != verdict:
                moved.append(f'{rid}: disposition {base_disp[rid][0]} -> {verdict}')
        legs.append(('APPENDONLY', not moved, 'no old id gains or flips a disposition in the round lesson',
                     'clean' if not moved else '; '.join(moved)))
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
    base_lesson_path = write('base_lesson.md', lesson_ok)

    def E(graded_extra=(), **over):
        base_args = dict(entry=entry_ok, base_registry=base, lands_registry=lands_e_path, lesson=lesson_e,
                         manifest=man_e, **{'capture_dir': 'reports/round-90/evidence', 'as_of': '2026-11-04',
                                            'topic': topic, 'min_bytes': '1200', 'min_headings': '4',
                                            'min_new_ids': '3', 'min_topic_overlap': '8',
                                            'table_min_rows': '5', 'table_min_cols': '3',
                                            'topic_phrases': 'address;petition;efficacy;table',
                                            'min_topic_phrases': '4', 'min_anchor_span': '3',
                                            'base_lesson': base_lesson_path})
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

    chk('positive entry', ['entry'] + E(), 0, ['PASS legs=9/9'])
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
    chk('gate quote over the word bound', ['entry'] + E(lesson=lesson_longq), 1, ['FAIL GATE', 'out of bounds'])
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
    chk('uncited new row is out of scope', ['entry'] + E(lands_registry=lands_uncited), 0, ['PASS legs=9/9'])
    shortq = write('lesson_shortq.md', ''.join(
        f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: \u201cefficacy register\u201d\n'
        for rid, u in new_rows))
    chk('gate quote below the char floor', ['entry'] + E(lesson=shortq), 1, ['FAIL GATE', 'out of bounds'])
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

    # ---------------------------------------- round-91 v2 entry-mode negatives
    # Attack 5: on-topic tokens carried by running prose alone cleared the old
    # TOPIC; the phrase anchors must sit in h2 headings or table cells.
    proseonly = os.path.join(root, 'corpus/knowledge/myth-symbol/prayer-address.md')
    with open(proseonly, 'w') as f:
        f.write('# Prayer\n\n- topic: prayer address petition efficacy\n- sources: S010\n'
                '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                '## 1. Section one\n\nThe words address petition efficacy table appear here only inside running prose, '
                'never as a heading and never inside the table cells; a negation list clears a token count. '
                'The address petition efficacy table words are listed again to satisfy the old overlap floor, '
                'while no heading of this entry names any of them.\n\n'
                '## 2. Section two\n\n' + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\n| a | b | c |\n|---|---|---|\n' + ''.join(f'| row {i} | x | y |\n' for i in range(5)) + '\nS010 S011 S012\n')
    chk('sub-topic phrases absent from headings', ['entry'] + E(entry=proseonly, min_topic_overlap='1'), 1, ['FAIL TOPIC', 'phrase anchors 0/'])
    dupid_e = write('lands_dupid.md', lands_e + _row('S010', 'https://example.org/dup', 'a second row under S010',
                                                     tier='A', status='mined', opened='2026-11-04',
                                                     used='corpus/knowledge/myth-symbol/prayer-register.md'))
    chk('duplicate lands id in entry mode', ['entry'] + E(lands_registry=dupid_e), 1, ['FAIL UNIQUENESS'])
    shadow_base = write('lands_shadow.md', lands_e.replace('| S010 | https://example.org/a |', '| S010 | ' + url + ' |'))
    chk('new row shadows a base url', ['entry'] + E(lands_registry=shadow_base), 1, ['FAIL UNIQUENESS'])
    shared_url = write('lands_shared.md', lands_e.replace('| S011 | https://example.org/b |', '| S011 | https://example.org/a |'))
    chk('two new rows share one url', ['entry'] + E(lands_registry=shared_url), 1, ['FAIL UNIQUENESS'])
    selfq_rows = []
    for i, (rid, u) in enumerate(new_rows):
        q = 'prayer address petition votive promise register case' if rid == 'S010' \
            else f'prayer address petition votive promise fixed extempore efficacy register case {i}'
        selfq_rows.append(f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: \u201c{q}\u201d\n')
    selfq_e = write('lesson_selfq.md', ''.join(selfq_rows))
    chk('gate quote is the teaching cell', ['entry'] + E(lesson=selfq_e), 1, ['FAIL GATE', 'self-quote'])
    chrome_rows = []
    for i, (rid, u) in enumerate(new_rows):
        q = u if rid == 'S010' else f'prayer address petition votive promise fixed extempore efficacy register case {i}'
        chrome_rows.append(f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: \u201c{q}\u201d\n')
    chrome_e = write('lesson_chrome.md', ''.join(chrome_rows))
    chk('gate quote is from the source cell', ['entry'] + E(lesson=chrome_e), 1, ['FAIL GATE', 'source cell'])
    shutil.copy(lesson_e, os.path.join(ev, 'S010-copy.md'))
    man_copy_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                               fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_copy_rows['S010'] = dict(capture='reports/round-90/evidence/S010-copy.md', url=new_rows[0][1],
                                 http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_copy = _manifest(root, man_copy_rows, 'mcopy.json')
    chk('capture byte-copies a graded file', ['entry'] + E(manifest=man_copy), 1, ['FAIL CAPTURE', 'byte-copies'])
    freshmove = write('lesson_freshmove.md', lesson_e_text
                      + '- S002 NOT-LOCATED recheck unchanged \u2014 https://example.org/other accessed 2026-11-04: '
                        '\u201cunrelated row about dye plants\u201d\n')
    chk('lesson channel re-verification refused', ['entry'] + E(lesson=freshmove), 1, ['FAIL APPENDONLY'])
    gained = write('lesson_gained.md', lesson_e_text
                   + '- S007 LOCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                     '\u201cunrelated row about dye plants and textile trades\u201d\n')
    chk('old id gains a fresh disposition line', ['entry'] + E(lesson=gained), 1, ['FAIL APPENDONLY', 'gained'])
    chk('phrase floor unmet on a real entry', ['entry'] + E(min_topic_phrases='9'), 1, ['FAIL TOPIC', 'phrase anchors'])

    # ------------------------------------------- round-92 v3 entry-mode negatives
    # (routed round-91 survivors, CriticClaims91 attacks.md V10a/V10c/V3/V12/V7/V2/V9)
    bare = write('lesson_bare.md', lesson_e_text
                 + 'S007 NOT-LOCATED recheck unchanged \u2014 https://example.org/other accessed 2026-11-04: '
                   '\u201cunrelated row about dye plants\u201d\n')
    chk('lesson disposition without a marker', ['entry'] + E(lesson=bare), 1, ['FAIL APPENDONLY', 'gained'])
    bareflip = write('lesson_bareflip.md', lesson_e_text
                     + 'S002 NOT-LOCATED recheck unchanged \u2014 https://example.org/other accessed 2026-11-04: '
                       '\u201cunrelated row about dye plants\u201d\n')
    chk('bare marker flips an old disposition', ['entry'] + E(lesson=bareflip), 1,
        ['FAIL APPENDONLY', 'disposition LOCATED'])
    quoted = write('lesson_quoted.md', lesson_e_text
                   + '> - S007 LOCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                     '\u201cunrelated row about dye plants and textile trades\u201d\n')
    chk('lesson disposition behind a blockquote', ['entry'] + E(lesson=quoted), 1, ['FAIL APPENDONLY', 'gained'])
    frag = write('lands_frag.md', lands_e.replace('| S010 | https://example.org/a |',
                                                  '| S010 | ' + url + '#polari |'))
    chk('fragment shadow url', ['entry'] + E(lands_registry=frag), 1, ['FAIL UNIQUENESS'])
    man_wrong_url = _manifest(root, {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt',
                                               url=f'https://registry-example.org/{rid}', http_status=200,
                                               fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows},
                              'mwrongurl.json')
    chk('manifest url not the row url', ['entry'] + E(manifest=man_wrong_url), 1, ['FAIL CAPTURE', 'not a row url'])
    shared_cap = _manifest(root, {rid: dict(capture='reports/round-90/evidence/S010.txt', url=u, http_status=200,
                                            fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows},
                           'mshared.json')
    chk('capture shared by two qualifying ids', ['entry'] + E(manifest=shared_cap), 1, ['FAIL CAPTURE', 'capture shared by'])
    chrome_cap = _cap(root, 'chrome.txt', 'Freemium for Journals platform. ')
    man_chrome_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                                 fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_chrome_rows['S010']['capture'] = 'reports/round-90/evidence/chrome.txt'
    man_chrome = _manifest(root, man_chrome_rows, 'mchrome.json')
    lesson_chrome_own = write('lesson_chrome_own.md', lesson_e_text.replace(
        '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d',
        '\u201cFreemium for Journals platform\u201d'))
    chk('chrome quote as own sentence', ['entry'] + E(lesson=lesson_chrome_own, manifest=man_chrome),
        1, ['FAIL GATE', 'content words'])
    stuffed = os.path.join(root, 'corpus/knowledge/myth-symbol/stuffed.md')
    with open(stuffed, 'w') as f:
        f.write('# Prayer\n\n- topic: prayer as a petitionary address register\n- sources: S010\n'
                '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                '## Address, petition, efficacy and table of the bakehouse\n\n'
                'The address petition efficacy table words appear in this one heading alone, and the '
                'bridge sentence carries the vocative and votive words for the overlap floor; the rest '
                'of this entry is filler prose about the bakery rota and its scheduling needs.\n\n'
                '## 2. Filler\n\n' + ('Feed the starter with flour and water daily and keep the bowl covered overnight. '
                                      'Bakers argue about proofing times and oven temperatures across the district.\n\n' * 3)
                + '| a | b | c |\n|---|---|---|\n' + ''.join(f'| row {i} | x | y |\n' for i in range(5))
                + '\nS010 S011 S012\n')
    chk('phrase anchors in one heading only', ['entry'] + E(entry=stuffed), 1, ['FAIL TOPIC', 'span 1 heading'])
    prosetopic = os.path.join(root, 'corpus/knowledge/myth-symbol/prosetopic.md')
    with open(prosetopic, 'w') as f:
        f.write('# Prosetopic fixture\n\n- topic: prayer as a petitionary address register\n- sources: S010\n'
                '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                '## 1. Filler section\n\n'
                'In this register the prayer uses vocative formulae and votive forms, and the petitionary '
                'address carries the petitioner\u2019s claim before the deity. The wording is settled by custom '
                'and the delivery follows the mood of the moment.\n\n'
                '## 2. More filler\n\n'
                + ('Bakers argue about proofing times and oven temperatures across the district every week.\n\n' * 2)
                + '| prayer | petition | efficacy |\n|---|---|---|\n'
                + ''.join(f'| row {i} | x | y |\n' for i in range(5)) + '\nS010 S011 S012\n')
    chk('topic overlap on prose only', ['entry'] + E(entry=prosetopic), 1,
        ['FAIL TOPIC', 'prose shares 7 content words'])
    base_reg_cap = os.path.join(ev, 'basereg.txt')
    shutil.copy(base, base_reg_cap)
    man_basereg_rows = {rid: dict(capture='reports/round-90/evidence/basereg.txt', url=u, http_status=200,
                                  fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_basereg_rows['S010']['quote'] = 'unrelated row about dye plants and textile trade'
    man_basereg = _manifest(root, man_basereg_rows, 'mbasereg.json')
    lesson_basereg = write('lesson_basereg.md', lesson_e_text.replace(
        '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d',
        '\u201cunrelated row about dye plants and textile trade\u201d'))
    chk('capture byte-copies the base registry', ['entry'] + E(lesson=lesson_basereg, manifest=man_basereg),
        1, ['FAIL CAPTURE', 'byte-copies'])
    readme_copy = os.path.join(ev, 'readme-copy.txt')
    with open(os.path.join(root, 'corpus/README.md'), 'w') as f:
        f.write('# corpus README fixture\n\nideophone vocabulary coverage map row.\n')
    shutil.copy(os.path.join(root, 'corpus/README.md'), readme_copy)
    man_readme_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                                 fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_readme_rows['S010']['capture'] = 'reports/round-90/evidence/readme-copy.txt'
    man_readme = _manifest(root, man_readme_rows, 'mreadme.json')
    chk('capture byte-copies corpus README', ['entry'] + E(manifest=man_readme), 1,
        ['FAIL CAPTURE', 'byte-copies'])
    chk('gate quote unbound on a real entry', ['entry'] + E(min_gate_overlap='40'), 1, ['FAIL GATE', 'content words'])

    def chk_leg(name, args, leg):
        """Round-93 v4: the negative must fail on exactly the named leg. A check that
        passes through a different leg is a fixture-masking survivor (round-93 M1)."""
        r = subprocess.run([sys.executable, '-B', os.path.abspath(__file__)] + args,
                           capture_output=True, text=True)
        out = (r.stdout or '') + (r.stderr or '')
        verdict = [l for l in out.splitlines() if 'EVIDENCE: ' in l]
        ok = r.returncode == 1 and bool(verdict) and verdict[-1].endswith('failed=' + leg)
        checks.append((name, ok, r.returncode, r.returncode, verdict[-1:] or out.strip().splitlines()[-1:]))

    # ------------------------------------------- round-93 v4 entry-mode negatives
    # (routed round-92 survivors, CriticClaims92 attacks.md A2c-A2f, A3b, A4a,
    #  A5d-A5f, A6a-A6g; corpus/lessons/round-92-verifier-spotcheck.md §6 item 4)
    url_variants = [
        ('entry mode: scheme-swapped shadow url refused', 'http://example.org/prayer'),
        ('entry mode: www-prefixed shadow url refused', 'https://www.example.org/prayer'),
        ('entry mode: query-suffixed shadow url refused', 'https://example.org/prayer?ref=lane'),
        ('entry mode: path-case shadow url refused', 'https://EXAMPLE.org/PRAYER'),
    ]
    def url_case(variant):
        # the row, its gate line and its manifest surface all carry the variant, so
        # UNIQUENESS is the only leg that can refuse it
        tag = str(len(checks))
        lands_v = write('lands_v' + tag + '.md', lands_e.replace('| S010 | https://example.org/a |', '| S010 | ' + variant + ' |'))
        lesson_v = write('lesson_v' + tag + '.md', lesson_e_text.replace('https://example.org/a ', variant + ' '))
        man_v = _manifest(root, {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt',
                                           url=(variant if rid == 'S010' else u), http_status=200,
                                           fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows},
                          'mv' + tag + '.json')
        return lands_v, lesson_v, man_v
    for label, variant in url_variants:
        lv, ls, mv = url_case(variant)
        chk_leg(label, ['entry'] + E(lands_registry=lv, lesson=ls, manifest=mv), 'UNIQUENESS')

    # A3b: a capture text-identical to the graded entry modulo one trailing newline.
    entry_copy = os.path.join(ev, 'entry-copy.txt')
    with open(entry_copy, 'w', encoding='utf-8') as f:
        f.write(open(entry_ok, encoding='utf-8').read() + '\n')
    man_entry_copy_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                                     fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_entry_copy_rows['S010'] = dict(capture='reports/round-90/evidence/entry-copy.txt', url=new_rows[0][1],
                                       http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_entry_copy = _manifest(root, man_entry_copy_rows, 'mentrycopy.json')
    lesson_entry_copy = write('lesson_entry_copy.md', lesson_e_text.replace(
        '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d',
        '\u201cThe petition states a want in a fixed order: address, reminder of past favour, request, promise.\u201d'))
    chk_leg('entry mode: newline-padded entry copy capture refused', ['entry'] + E(lesson=lesson_entry_copy, manifest=man_entry_copy), 'CAPTURE')

    # A4a: span gaming — single-token headings and a phrase in the header row.
    gaming = os.path.join(root, 'corpus/knowledge/linguistics/prayer-register.md')
    os.makedirs(os.path.dirname(gaming), exist_ok=True)
    gaming_body = ('# Prayer\n\n- topic: prayer as a petitionary address register\n- sources: S010 S011 S012\n'
                   '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                   '## address\n\nThe vocative formulae of prayer as a petitionary address register vary by rank, '
                   'and the votive promises bind the petitioner to fixed and extempore speech with efficacy claims. '
                   'A prayer opens by naming the deity and stating the petitioner, and the register carries the claim.\n\n'
                   '## petition\n\nThe petition states a want in a fixed order: address, reminder, request, promise. '
                   'Votive promises and vocative formulae make the petitionary register legible to the deity and '
                   'to the community that witnesses the rite of fixed and extempore speech.\n\n'
                   '## efficacy\n\nA prayer claims efficacy through the address, the promise or the speaker. '
                   'Efficacy claims in the petitionary register are graded in the culture, and extempore speech '
                   'carries the weight of the petitioner when the fixed formula is absent.\n\n'
                   '## 4. Results table of the rite\n\nThe vocative formulae vary by rank and the votive promise binds '
                   'the petitioner to a return, which keeps the register of prayer and petition stable across occasions.\n\n'
                   '| table | fixed | extempore |\n|---|---|---|\n| address | rote | improvised |\n'
                   '| petition | set | composed |\n| promise | written | spoken |\n| authority | text | speaker |\n'
                   '| failure | ritual fault | weak speaker |\n\n'
                   'S010 S011 S012 supply the comparative cases and each claim above is bounded to them.\n'
                   + ''.join(f'Sentence {i} of the petitionary register ties a vocative formula to a votive promise and to a claim of efficacy, varied by occasion number {i}. ' for i in range(1, 9)) + '\n')
    with open(gaming, 'w') as f:
        f.write(gaming_body)
    chk_leg('entry mode: single-word heading span gaming refused', ['entry'] + E(entry=gaming), 'TOPIC')

    # A5d/A5e/A5f: dispositions hidden in bold, table rows or zero-width characters.
    bold_disp = write('lesson_bold.md', lesson_e_text
                      + '**S007** LOCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201cunrelated row about dye plants and textile trades\u201d\n')
    chk_leg('entry mode: bold-wrapped disposition refused', ['entry'] + E(lesson=bold_disp), 'APPENDONLY')
    piped_disp = write('lesson_piped.md', lesson_e_text
                       + '| S007 | LOCATED | 2026-11-04 | https://example.org/other2 | unrelated row about dye plants |\n')
    chk_leg('entry mode: table-row disposition refused', ['entry'] + E(lesson=piped_disp), 'APPENDONLY')
    zw_disp = write('lesson_zw.md', lesson_e_text
                    + 'S007 LOC\u200bATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                      '\u201cunrelated row about dye plants and textile trades\u201d\n')
    chk_leg('entry mode: zero-width-obscured disposition refused', ['entry'] + E(lesson=zw_disp), 'APPENDONLY')

    # A6a/A6b: the base registry's identity cells may not move at lands.
    teaches_move = write('lands_teaches.md', lands_e.replace(
        good_teach, 'a flattering self-describing summary of the prayer register row'))
    chk_leg('entry mode: lands rewrite of a base teaches cell refused', ['entry'] + E(lands_registry=teaches_move), 'BASEROWS')
    removed_row = write('lands_removed.md',
                        '\n'.join(l for l in lands_e.splitlines() if not l.startswith('| S002 ')) + '\n')
    chk_leg('entry mode: lands deletion of a base row refused', ['entry'] + E(lands_registry=removed_row), 'BASEROWS')

    # A6c/A6d: symlinked captures are refused, in root or escaping it.
    link_target = os.path.join(root, 'outside-target.txt')
    with open(link_target, 'w') as f:
        f.write('Page text. prayer address petition votive promise fixed extempore efficacy register case 0. Boilerplate.')
    cap_link = os.path.join(ev, 'S010-link.txt')
    if os.path.lexists(cap_link):
        os.remove(cap_link)
    os.symlink(link_target, cap_link)
    man_link_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                               fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_link_rows['S010'] = dict(capture='reports/round-90/evidence/S010-link.txt', url=new_rows[0][1],
                                 http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_link = _manifest(root, man_link_rows, 'mlink.json')
    chk_leg('entry mode: in-root symlink capture refused', ['entry'] + E(manifest=man_link), 'CAPTURE')
    esc_target = os.path.join(work, 'escape-target.txt')
    with open(esc_target, 'w') as f:
        f.write('Page text. prayer address petition votive promise fixed extempore efficacy register case 0. Boilerplate.')
    cap_esc = os.path.join(ev, 'S010-esc.txt')
    if os.path.lexists(cap_esc):
        os.remove(cap_esc)
    os.symlink(esc_target, cap_esc)
    man_esc_rows = dict(man_link_rows)
    man_esc_rows['S010'] = dict(capture='reports/round-90/evidence/S010-esc.txt', url=new_rows[0][1],
                                http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_esc = _manifest(root, man_esc_rows, 'mesc.json')
    chk_leg('entry mode: root-escaping symlink capture refused', ['entry'] + E(manifest=man_esc), 'CAPTURE')

    # A6e: a quote that exists only in raw HTML markup is not located body text.
    _cap(root, 'S010-meta.html',
         '<html><head><meta name="description" content="prayer address petition votive promise fixed '
         'extempore efficacy register case 0"></head><body><p>Freemium preview. The full text is available '
         'to subscribers of the platform and the article body is withheld here.</p></body></html>')
    man_meta_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                               fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_meta_rows['S010'] = dict(capture='reports/round-90/evidence/S010-meta.html', url=new_rows[0][1],
                                 http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_meta = _manifest(root, man_meta_rows, 'mmeta.json')
    chk_leg('entry mode: markup-only capture quote refused', ['entry'] + E(manifest=man_meta), 'CAPTURE')

    # A6g: manifest shape refusals with a named diagnostic, no traceback.
    man_list = os.path.join(ev, 'mlist.json')
    with open(man_list, 'w') as f:
        json.dump({'rows': [{'S010': {}}]}, f)
    chk('entry mode: manifest rows list refused, no traceback', ['entry'] + E(manifest=man_list), 2,
        ['manifest rows is not a JSON object'])
    man_obj = os.path.join(ev, 'mobj.json')
    with open(man_obj, 'w') as f:
        f.write('[]')
    chk('entry mode: manifest not a JSON object refused', ['entry'] + E(manifest=man_obj), 2,
        ['manifest is not a JSON object'])

    # arm pins for the round-92 gap-hunt survivors (MutationTesterV3.md).
    man_trav_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                               fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_trav_rows['S010'] = dict(capture='reports/round-90/evidence/../evidence/S010.txt', url=new_rows[0][1],
                                 http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_trav = _manifest(root, man_trav_rows, 'mtrav.json')
    chk_leg('capture path with .. segment refused', ['entry'] + E(manifest=man_trav), 'CAPTURE')
    man_offset_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                                 fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_offset_rows['S010']['fetched_at'] = '2026-11-04T19:00:00'
    man_offset = _manifest(root, man_offset_rows, 'moffset.json')
    chk_leg('fetch instant without offset refused', ['entry'] + E(manifest=man_offset), 'CAPTURE')
    man_date_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                               fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_date_rows['S010']['fetched_at'] = '2026-11-05T19:00:00-03:00'
    man_date = _manifest(root, man_date_rows, 'mdate.json')
    chk_leg('fetch date differing from as-of refused', ['entry'] + E(manifest=man_date), 'CAPTURE')
    sib_dir = os.path.join(root, 'reports/round-90/evidence-x')
    os.makedirs(sib_dir, exist_ok=True)
    with open(os.path.join(sib_dir, 'S010.txt'), 'w') as f:
        f.write('Page text. prayer address petition votive promise fixed extempore efficacy register case 0. Boilerplate.')
    man_sib_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                              fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_sib_rows['S010'] = dict(capture='reports/round-90/evidence-x/S010.txt', url=new_rows[0][1],
                                http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_sib = _manifest(root, man_sib_rows, 'msib.json')
    chk_leg('capture in a sibling capture dir refused', ['entry'] + E(manifest=man_sib), 'CAPTURE')
    port_row = write('lands_port.md', lands_e.replace('| S010 | https://example.org/a |',
                                                      '| S010 | https://example.org:443/prayer |'))
    lv, ls, mv = url_case('https://example.org:443/prayer')
    chk_leg('entry mode: default-port url shadow refused', ['entry'] + E(lands_registry=lv, lesson=ls, manifest=mv), 'UNIQUENESS')

    # graded-list arm pins: a capture copying the lands registry or the round
    # lesson itself is refused even under the capture dir (non-circular copies).
    lands_anchor_text = lands_e.replace('| docs | A | scope | anchor | prayer address petition votive promise register case | ',
                                        '| docs | A | scope | The petition states a want in a fixed order: address, reminder of past favour, request, promise. | prayer address petition votive promise register case | ', 1)
    lands_anchor_path = write('lands_anchor.md', lands_anchor_text)
    lands_copy = os.path.join(ev, 'lands-copy.txt')
    shutil.copy(lands_anchor_path, lands_copy)
    man_lands_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                                fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_lands_rows['S010'] = dict(capture='reports/round-90/evidence/lands-copy.txt', url=new_rows[0][1],
                                  http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_lands = _manifest(root, man_lands_rows, 'mlandscopy.json')
    lesson_anchor = write('lesson_anchor.md', lesson_e_text.replace(
        '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d',
        '\u201cThe petition states a want in a fixed order: address, reminder of past favour, request, promise.\u201d'))
    chk_leg('capture byte-copies the lands registry refused', ['entry'] + E(lesson=lesson_anchor, lands_registry=lands_anchor_path, manifest=man_lands), 'CAPTURE')
    # The round lesson under test is a file the graded list does NOT name (round-90.md
    # is a byte copy of lesson_e, so it would catch the copy through another arm).
    lesson_x = write('lesson_x.md', lesson_e_text + 'Round note: fixture mirror, no disposition.\n')
    lesson_copy = os.path.join(ev, 'lesson-copy.txt')
    shutil.copy(lesson_x, lesson_copy)
    man_lesson_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                                 fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_lesson_rows['S010'] = dict(capture='reports/round-90/evidence/lesson-copy.txt', url=new_rows[0][1],
                                   http_status=200, fetched_at='2026-11-04T19:00:00-03:00')
    man_lesson = _manifest(root, man_lesson_rows, 'mlessoncopy.json')
    chk_leg('capture byte-copies the round lesson refused', ['entry'] + E(lesson=lesson_x, manifest=man_lesson), 'CAPTURE')
    # Blockquoted lowercase disposition: only the anchored re.I rule reads it (the
    # uppercase fallback does not), so it pins the anchored arm against revert.
    quoted_lc = write('lesson_quoted_lc.md', lesson_e_text
                      + '> - S007 located recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201cunrelated row about dye plants and textile trades\u201d\n')
    chk_leg('entry mode: blockquoted lowercase disposition refused', ['entry'] + E(lesson=quoted_lc), 'APPENDONLY')
    # A6f: a gate line whose first quote is bound and whose second quote is chrome.
    two_quote = write('lesson_two_quote.md', lesson_e_text.replace(
        '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d',
        '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d and '
        '\u201cFreemium for Journals platform\u201d'))
    chk_leg('entry mode: second chrome quote on a gate line refused', ['entry'] + E(lesson=two_quote), 'GATE')

    # ------------------------------------------------ round-94 v5 entry-mode pins
    # (routed corpus/lessons/round-93.md ## Routed to round 94: CriticClaims93
    #  counterfeits A1/B1/G1/H1/I1/J1, the K1 lowercase channel, and the five
    #  MutationTesterV4 mutant classes; one named check per class)
    def unit(name, ok, detail=''):
        checks.append((name, ok, 0, 0, [detail] if detail else []))

    lesson_a1 = write('lesson_a1.md', lesson_e_text
                      + '- S001 L\u041eCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201canother old base row about dye plants\u201d\n')
    chk('round-94 A1: non-ASCII letters in the verdict token refused', ['entry'] + E(lesson=lesson_a1),
        2, ['VERDICT-NONASCII'])
    lesson_b1 = write('lesson_b1.md', lesson_e_text
                      + '- S001 LOCA\u00adTED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201canother old base row about dye plants\u201d\n')
    chk('round-94 B1: soft hyphen inside the verdict token refused', ['entry'] + E(lesson=lesson_b1),
        2, ['VERDICT-SOFTHYPHEN'])
    g1_entry = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1/prayer-register.md')
    os.makedirs(os.path.dirname(g1_entry), exist_ok=True)
    with open(g1_entry, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## 1. address')
                .replace('## 2. The petition', '## 2. petition')
                .replace('## 3. Fixed and extempore', '## 3. efficacy')
                .replace('## 4. Efficacy', '## 4. table')
                .replace('## 5. Table', '## 5. Rites'))
    chk_leg('round-94 G1: numbered phrase-only headings do not anchor', ['entry'] + E(entry=g1_entry), 'TOPIC')
    man_h1_rows = {rid: dict(capture=f'reports/round-90/evidence/{rid}.txt', url=u, http_status=200,
                             fetched_at='2026-11-04T19:00:00-03:00') for rid, u in new_rows}
    man_h1_rows['S011'] = ['not', 'a', 'dict']
    man_h1 = os.path.join(ev, 'mh1.json')
    with open(man_h1, 'w') as f:
        json.dump({'rows': man_h1_rows}, f)
    chk('round-94 H1: manifest row value that is a list refused', ['entry'] + E(manifest=man_h1),
        2, ['MANIFEST-ROW-TYPE'])
    lands_i1 = write('lands_i1.md', lands_e.replace(
        _row('S010', 'https://example.org/a', 'prayer address petition votive promise register case', tier='A',
             status='mined', opened='2026-11-04', used='corpus/knowledge/myth-symbol/prayer-register.md'),
        '| S010 | https://example.org/a | docs | A | scope | anchor | prayer address petition votive promise '
        'register case | mined | 2026-11-04 | 90d |'))
    chk_leg('round-94 I1: registry row shorter than eleven cells refused',
            ['entry'] + E(lands_registry=lands_i1), 'NEWIDS')
    lesson_j1 = write('lesson_j1.md', lesson_e_text
                      + '- S002 NOT\u2013LOCATED recheck unchanged \u2014 https://example.org/other accessed 2026-11-04: '
                        '\u201cunrelated row about dye plants\u201d\n')
    chk('round-94 J1: en-dash NOT-LOCATED reads as NOT-LOCATED, no false flip', ['entry'] + E(lesson=lesson_j1),
        1, ['FAIL APPENDONLY', 'disposition LOCATED -> NOT-LOCATED'])
    lesson_k1 = write('lesson_k1.md', lesson_e_text
                      + 'Round note: S007 located recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201cunrelated row about dye plants and textile trades\u201d\n')
    chk('round-94 K1: lowercase unanchored verdict refused', ['entry'] + E(lesson=lesson_k1),
        2, ['VERDICT-LOWERCASE'])
    # mutant pins (MutationTesterV4 survivors): each check fails when the named
    # mutation is applied to this tool.
    _body_ss = html_body_text(b'<html><head><style>.x { color: red; }</style></head><body>'
                              b'<script>var prayer = "petition";</script>'
                              b'<p>visible prayer address petition body</p></body></html>')
    unit('mutant pin: script and style stripping active (script-strip-off)',
         'var prayer' not in _body_ss and 'color: red' not in _body_ss and 'prayer address petition' in _body_ss)
    _body_cs = html_body_text(b'before visible <!-- prayer address petition votive promise > hidden comment --> after')
    unit('mutant pin: comment stripping active (comment-strip-off)',
         'hidden comment' not in _body_cs and 'before visible' in _body_cs and 'after' in _body_cs)
    _body_ue = html_body_text(b'<p>Tom &amp; Jerry &#65; &quot;quoted&quot; prayer body</p>')
    unit('mutant pin: entity unescape active (unescape-off)',
         '&amp;' not in _body_ue and '&quot;' not in _body_ue
         and 'Tom & Jerry' in _body_ue and 'A "quoted" prayer body' in _body_ue)
    try:
        dispositions('Round note: s001 located in the archive, rechecked against the row.\n')
        unit('mutant pin: lowercase unanchored verdict refused (dispo-any-casei)', False, 'no refusal raised')
    except Refused as exc:
        unit('mutant pin: lowercase unanchored verdict refused (dispo-any-casei)', 'VERDICT-LOWERCASE' in str(exc))
    lands_c8 = write('lands_c8.md', lands_e.replace(_row('S001', url, good_teach),
                                                    _row('S001', url, good_teach, opened='2026-10-20')))
    chk_leg('mutant pin: base row opened cell change refused (baserows-drop-cell8)',
            ['entry'] + E(lands_registry=lands_c8), 'BASEROWS')

    # ------------------------------------------------ round-95 v6 entry-mode pins
    # (routed .ufo/waves/round-94/w1/CriticO94.md survivor recipes CD1, LR1,
    #  TAB1, ID1, NUM1, RM1, NUM2; one named refusal per new class, plus the
    #  head-qualify pin mutated by head-qualify-off)
    lesson_cd1 = write('lesson_cd1.md', lesson_e_text
                      + '- S001 LOCA\u0301TED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201canother old base row about dye plants\u201d\n')
    chk('round-95 CD1: combining mark in the verdict token refused', ['entry'] + E(lesson=lesson_cd1),
        2, ['VERDICT-COMBINE'])
    lesson_lr1 = write('lesson_lr1.md', lesson_e_text
                      + '- S001 LO\u200eCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201canother old base row about dye plants\u201d\n')
    chk('round-95 LR1: LRM inside the verdict token refused', ['entry'] + E(lesson=lesson_lr1),
        2, ['VERDICT-FORMAT'])
    lesson_tab1 = write('lesson_tab1.md', lesson_e_text
                      + '- S001 LO\tCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201canother old base row about dye plants\u201d\n')
    chk('round-95 TAB1: tab inside the verdict token refused', ['entry'] + E(lesson=lesson_tab1),
        2, ['VERDICT-TAB'])
    lesson_id1 = write('lesson_id1.md', lesson_e_text
                      + '- \ua731001 LOCATED recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: '
                        '\u201canother old base row about dye plants\u201d\n')
    chk('round-95 ID1: lookalike small-cap letter in the id token refused', ['entry'] + E(lesson=lesson_id1),
        2, ['ID-NONASCII'])
    num1_entry = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1num1/prayer-register.md')
    os.makedirs(os.path.dirname(num1_entry), exist_ok=True)
    with open(num1_entry, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## 1.1 address')
                .replace('## 2. The petition', '## 2.1 petition')
                .replace('## 3. Fixed and extempore', '## 3.1 efficacy')
                .replace('## 4. Efficacy', '## 4.1 table')
                .replace('## 5. Table', '## 5. Notes'))
    chk_leg('round-95 NUM1: nested numbered phrase-only headings do not anchor', ['entry'] + E(entry=num1_entry), 'TOPIC')
    rm1_entry = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1rm1/prayer-register.md')
    os.makedirs(os.path.dirname(rm1_entry), exist_ok=True)
    with open(rm1_entry, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## I. address')
                .replace('## 2. The petition', '## II. petition')
                .replace('## 3. Fixed and extempore', '## III. efficacy')
                .replace('## 4. Efficacy', '## IV. table')
                .replace('## 5. Table', '## V. Notes'))
    chk_leg('round-95 RM1: roman numbered phrase-only headings do not anchor', ['entry'] + E(entry=rm1_entry), 'TOPIC')
    num2_entry = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1num2/prayer-register.md')
    os.makedirs(os.path.dirname(num2_entry), exist_ok=True)
    with open(num2_entry, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## Notes 1) address')
                .replace('## 2. The petition', '## Notes 2) petition')
                .replace('## 3. Fixed and extempore', '## Notes 3) efficacy')
                .replace('## 4. Efficacy', '## Notes 4) table')
                .replace('## 5. Table', '## Notes 5) Table'))
    chk_leg('round-95 NUM2: second-token numbered phrase-only headings do not anchor', ['entry'] + E(entry=num2_entry), 'TOPIC')
    single_tok = write('entry_singletok.md', '# Prayer\n\n- topic: prayer address petition efficacy\n- sources: S010\n'
                '- verified-at: 2026-11-04\n- recheck: 180d\n\n'
                '## address\n\nSection body one about sourdough scheduling and the bakery rota for the week. '
                + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\n## petition\n\nMore filler about sourdough scheduling for the bakery rota. '
                + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\n## efficacy\n\n' + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\n## table\n\n' + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\n\nS010 S011 S012\n')
    chk('single-token headings anchor no phrase (head-qualify pin)', ['entry'] + E(entry=single_tok, min_topic_phrases='4', min_anchor_span='0', min_topic_overlap='1'), 1, ['FAIL TOPIC', 'phrase anchors 0/4'])
    # ------------------------------------------------ round-96 v8 pins (10)
    _g96tail = ' recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: \u201canother old base row about dye plants\u201d\n'
    _d = {'NB1': 'LO\u00a0CATED', 'VT1': 'LOCA\u000bTED', 'FF1': 'LOCA\u000cTED', 'LS1': 'LOCA\u2028TED', 'NEL1': 'LOCA\u0085TED', 'ANSI1': 'LOCA\u001b[31mTED', 'PS1': 'LOCA\u2029TED', 'FS1': 'LOCA\u001cTED', 'FS2': 'LOCA\u001dTED', 'FS3': 'LOCA\u001eTED'}
    _tok = {'NB1': 'VERDICT-NBSP', 'VT1': 'VERDICT-VT', 'FF1': 'VERDICT-FF', 'LS1': 'VERDICT-LINESEP', 'NEL1': 'VERDICT-NEL', 'ANSI1': 'VERDICT-ANSI', 'PS1': 'VERDICT-LINESEP', 'FS1': 'VERDICT-LINESEP', 'FS2': 'VERDICT-LINESEP', 'FS3': 'VERDICT-LINESEP'}
    for _c in ['NB1', 'VT1', 'FF1', 'LS1', 'NEL1', 'ANSI1', 'PS1', 'FS1', 'FS2', 'FS3']:
        _lf = write(f'lesson_g96{_c}.md', lesson_e_text + f'- S001 {_d[_c]}' + _g96tail)
        chk(f'round-96 {_c}: token carries the codepoint refused', ['entry'] + E(lesson=_lf), 2, [_tok[_c]])
    _lc = write('lesson_g96CYR1.md', lesson_e_text + '- \u0430' + '001 LOCATED' + _g96tail)
    chk('round-96 CYR1: homoglyph id letter refused', ['entry'] + E(lesson=_lc), 2, ['ID-NONASCII'])
    _br1 = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1br1/prayer-register.md')
    os.makedirs(os.path.dirname(_br1), exist_ok=True)
    with open(_br1, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## (1) address').replace('## 2. The petition', '## (2) petition').replace('## 3. Fixed and extempore', '## (3) efficacy').replace('## 4. Efficacy', '## (4) table').replace('## 5. Table', '## (5) Notes'))
    chk_leg('round-96 BR1: bracketed-number phrase-only headings do not anchor', ['entry'] + E(entry=_br1), 'TOPIC')
    _da1 = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1dash1/prayer-register.md')
    os.makedirs(os.path.dirname(_da1), exist_ok=True)
    with open(_da1, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## - address').replace('## 2. The petition', '## - petition').replace('## 3. Fixed and extempore', '## - efficacy').replace('## 4. Efficacy', '## - table').replace('## 5. Table', '## - Notes'))
    chk_leg('round-96 DASH1: separator-dash phrase-only headings do not anchor', ['entry'] + E(entry=_da1), 'TOPIC')

    # ------------------------------------------------ round-97 v9 pins (8)
    # (routed CriticO96 survivors on v8, reports/round-97/controls/critic96-on-v8.txt:
    #  CR1/US1/NUL1/OGH1/IS1 verdict-token channels plus CM1/CMW2 heading channel;
    #  the CR-only line-break control proves a lone U+000D terminating a line
    #  neither severs nor hides a disposition)
    _g97tail = ' recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: \u201canother old base row about dye plants\u201d\n'
    _d97 = {'CR1': ('LOCA\u000dTED', 'VERDICT-CTRL', 'U+000D'),
            'US1': ('LOCA\u001fTED', 'VERDICT-CTRL', 'U+001F'),
            'NUL1': ('LOCA\u0000TED', 'VERDICT-CTRL', 'U+0000'),
            'OGH1': ('LOCA\u1680TED', 'VERDICT-SEPARATOR', 'U+1680'),
            'IS1': ('LOCA\u3000TED', 'VERDICT-SEPARATOR', 'U+3000')}
    for _c in ['CR1', 'US1', 'NUL1', 'OGH1', 'IS1']:
        _tokv, _tokname, _cp = _d97[_c]
        _lf = write(f'lesson_g97{_c}.md', lesson_e_text + f'- S001 {_tokv}' + _g97tail)
        chk(f'round-97 {_c}: token carries the codepoint refused', ['entry'] + E(lesson=_lf),
            2, [_tokname, _cp])
    _cm1e = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1cm1/prayer-register.md')
    os.makedirs(os.path.dirname(_cm1e), exist_ok=True)
    with open(_cm1e, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## 1\u0301. address')
                .replace('## 2. The petition', '## 2\u0301. petition')
                .replace('## 3. Fixed and extempore', '## 3\u0301. efficacy')
                .replace('## 4. Efficacy', '## 4\u0301. table')
                .replace('## 5. Table', '## 5\u0301. Notes'))
    chk('round-97 CM1: combining mark on the heading numbering token refused', ['entry'] + E(entry=_cm1e),
        1, ['FAIL TOPIC', 'HEADING-COMBINING'])
    _cmw2e = os.path.join(root, 'corpus/knowledge/myth-symbol2/g1cmw2/prayer-register.md')
    os.makedirs(os.path.dirname(_cmw2e), exist_ok=True)
    with open(_cmw2e, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## addre\u0301ss')
                .replace('## 2. The petition', '## petition\u0301')
                .replace('## 3. Fixed and extempore', '## efficac\u0301y')
                .replace('## 4. Efficacy', '## tabl\u0301e')
                .replace('## 5. Table', '## Notes'))
    chk('round-97 CMW2: combining mark inside a heading phrase word refused', ['entry'] + E(entry=_cmw2e),
        1, ['FAIL TOPIC', 'HEADING-COMBINING'])
    lesson_cronly = write('lesson_g97CRonly.md', lesson_e_text.replace('\n', '\r'))
    chk('round-97 CR-only line breaks do not sever or hide dispositions', ['entry'] + E(lesson=lesson_cronly),
        0, ['PASS legs=9/9'])
    _g98tail = ' recheck moved \u2014 https://example.org/other2 accessed 2026-11-04: \u201canother old base row about dye plants\u201d\n'
    for _c, _tokv, _tokname, _cp in [('DEL1', 'LOCA\u007fTED', 'VERDICT-CTRL', 'U+007F'),
                                     ('ENC1', 'LOCA\u20ddTED', 'VERDICT-COMBINE', 'U+20DD')]:
        _lf = write(f'lesson_g98{_c}.md', lesson_e_text + f'- S001 {_tokv}' + _g98tail)
        chk(f'round-98 {_c}: token carries the codepoint refused', ['entry'] + E(lesson=_lf), 2, [_tokname, _cp])
    for _c, _rad in [('ROMAN1', ['\u2160.', '\u2161.', '\u2162.', '\u2163.', '\u2164.']),
                     ('SUP1', ['\u00b9.', '\u00b2.', '\u00b3.', '\u2074.', '\u2075.']),
                     ('FWPER1', ['1\uff0e', '2\uff0e', '3\uff0e', '4\uff0e', '5\uff0e'])]:
        _e = os.path.join(root, f'corpus/knowledge/myth-symbol2/g98{_c.lower()}/prayer-register.md')
        os.makedirs(os.path.dirname(_e), exist_ok=True)
        with open(_e, 'w') as f:
            f.write(good_body.replace('## 1. The address', f'## {_rad[0]} address')
                    .replace('## 2. The petition', f'## {_rad[1]} petition')
                    .replace('## 3. Fixed and extempore', f'## {_rad[2]} efficacy')
                    .replace('## 4. Efficacy', f'## {_rad[3]} table')
                    .replace('## 5. Table', f'## {_rad[4]} Notes'))
        chk(f'round-98 {_c}: non-ASCII numbering token refused', ['entry'] + E(entry=_e), 1, ['FAIL TOPIC'])
    _e = os.path.join(root, 'corpus/knowledge/myth-symbol2/g98romanok/prayer-register.md')
    os.makedirs(os.path.dirname(_e), exist_ok=True)
    with open(_e, 'w') as f:
        f.write(good_body.replace('## 1. The address', '## \u2160. The address')
                .replace('## 2. The petition', '## \u2161. The petition')
                .replace('## 3. Fixed and extempore', '## \u2162. Fixed and extempore')
                .replace('## 4. Efficacy', '## \u2163. Efficacy')
                .replace('## 5. Table', '## \u2164. Table'))
    chk('round-98 ROMANOK: roman numeral before heading words stays clean', ['entry'] + E(entry=_e), 0, ['PASS legs=9/9'])

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
    p.add_argument('--topic-phrases', default='')
    p.add_argument('--min-topic-phrases', type=int, default=0)
    p.add_argument('--min-anchor-span', type=int, default=0)
    p.add_argument('--min-gate-overlap', type=int, default=3)
    p.add_argument('--base-lesson', dest='base_lesson', default=None)
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
