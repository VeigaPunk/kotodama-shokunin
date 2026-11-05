#!/usr/bin/env python3
"""Round-96 counterfeit battery and grader driver (ExecBattery96).

Copied from .ufo/waves/round-95/w1/stage/ExecBattery95/battery95.py (sha256
342237cdcc980d6e9eea7e281671e9a7eb168e7731d799ecd4b32ddd7d00fd38, read-only source, frozen) and
extended in place:
  * the tool under test comes from --tool and the scratch dir from --work (no R93_* env);
    TMPDIR for the grader is <work>/tmp; a --work under /tmp is refused;
  * twenty-four battery classes (CLASSES below: A1, B1, G1, H1, I1, J1, K1 plus
    CD1, LR1, TAB1, ID1, NUM1, RM1, NUM2 plus NB1, VT1, FF1, LS1, NEL1, ANSI1,
    CYR1, BR1, DASH1 plus F1) and two CLEAN controls (G0, ZWNJ1) are built as mini-lanes under
    <work>/work/battery/<class>: the first seven recipes from
    .ufo/waves/round-93/w1/CriticClaims93.md and corpus/lessons/round-93.md
    "## Routed to round 94" (as in battery94.py), the seven new ones from
    .ufo/waves/round-94/w1/CriticO94.md "Survivor recipes";
  * the round-93 attack list (ATTACKS, unchanged) and the round-92 V-series (mc.ATTACKS,
    imported read-only from reports/round-92/controls/make-counterfeits.py) form the
    regression set, run against the same --tool;
  * --emit <stage-dir> copies the class fixtures to <stage-dir>/battery/<class>/ and writes
    <stage-dir>/manifest.json.

Usage:
  python3 -B battery96.py --tool <grader.py> --work <scratch-dir> [--verbose] [--emit <stage-dir>]

Output, in order:
  TOOL sha256=<sha> path=<abs tool>
  CLASS <name> rc=<n> traceback=<yes|no> named=<leg-or-diagnostic|none> outcome=<REFUSED|SURVIVOR|UNNAMED>
  BATTERY-SUMMARY survivors=<n> unnamed=<n> refused=<n>
  REG <R93|R92> <id> rc=<n> expect=<...> fail=<legs|none> outcome=<...>   (regression, one per case)
Outcome rules (battery classes): rc 0 -> SURVIVOR; rc != 0 with a manifest-listed token
in the output and no 'Traceback' -> REFUSED; anything else -> UNNAMED. Controls
(G0, ZWNJ1) expect CLEAN: rc 0 -> CLEAN, otherwise NOT-CLEAN data. Exit 0 once the
driver completes (counts are data); exit 2 on a usage error.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import shlex
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True

LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
BUILDER = LANE + '/reports/round-92/controls/make-counterfeits.py'  # frozen fixture builder, read-only
EV = 'reports/round-90/evidence'
IDS = ['S955', 'S956', 'S957']
AS_OF = '2026-11-05'
DEFAULT_URLS = {'S955': 'https://registry-example.org/verlan-case-0',
                'S956': 'https://registry-example.org/verlan-case-1',
                'S957': 'https://registry-example.org/verlan-case-2'}
BASE_URL = 'https://registry-example.org/base-prayer-notes'
TEACH = 'prayer address petition votive promise register case'
DEFAULT_MAN_QUOTE = 'prayer address petition votive promise fixed extempore efficacy register case'
BASE_LESSON = ('- S776 LOCATED recheck unchanged \u2014 ' + BASE_URL
               + ' accessed 2026-10-01: \u201can old base row about prayer notes and rubrics\u201d\n')

spec = importlib.util.spec_from_file_location('mc', BUILDER)
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)

# Set by configure() from --tool and --work.
TOOL = None
SCRATCH = None
WORK = None
ENV = None


def configure(tool, work):
    global TOOL, SCRATCH, WORK, ENV
    TOOL = os.path.abspath(tool)
    SCRATCH = os.path.abspath(work)
    WORK = os.path.join(SCRATCH, 'work')
    ENV = dict(os.environ, TMPDIR=os.path.join(SCRATCH, 'tmp'))
    os.makedirs(os.path.join(SCRATCH, 'tmp'), exist_ok=True)
    os.makedirs(WORK, exist_ok=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def put(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.lexists(path):
        os.remove(path)
    if isinstance(data, bytes):
        with open(path, 'wb') as f:
            f.write(data)
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)


def default_caps():
    return {rid: (f'Page text. prayer address petition votive promise fixed extempore efficacy register case {i}. '
                  'Also site boilerplate and navigation. Freemium for Journals platform.')
            for i, rid in enumerate(IDS)}


def default_quotes():
    return {rid: f'prayer address petition votive promise fixed extempore efficacy register case {i}'
            for i, rid in enumerate(IDS)}


def lands_text(urls, s776_teach=None, s001=True):
    rows = [mc._row('S776', BASE_URL, s776_teach or 'an old base row about prayer notes and rubrics')]
    if s001:
        rows.append(mc._row('S001', 'https://registry-example.org/base-old',
                            'another old base row about unrelated dye plants'))
    rows += [mc._row(rid, urls[rid], TEACH) for rid in IDS]
    return mc.HEADER + '\n' + '\n'.join(rows) + '\n'


def lesson_text(urls, quotes, extra=''):
    lines = [f'- {rid} admit A/mined. {urls[rid]} \u2014 accessed {AS_OF} \u2014 body: \u201c{quotes[rid]}\u201d'
             for rid in IDS]
    return '\n'.join(lines) + '\n' + extra


def base_registry_text():
    return (mc.HEADER + '\n'
            + mc._row('S776', BASE_URL, 'an old base row about prayer notes and rubrics') + '\n'
            + mc._row('S001', 'https://registry-example.org/base-old',
                      'another old base row about unrelated dye plants') + '\n')


class FX:
    def __init__(self, name):
        self.name = name
        self.root = os.path.join(WORK, name)
        shutil.rmtree(self.root, ignore_errors=True)
        os.makedirs(self.root)
        self.base = self.p('base.md')
        self.lands = self.p('lands.md')
        self.lesson = self.p('lesson.md')
        self.base_lesson = self.p('base-lesson.md')
        self.entry = self.p(mc.ENTRY_NAME)
        self.manifest = self.p('manifest.json')

    def p(self, rel):
        return os.path.join(self.root, rel)

    def fixture(self):
        return dict(root=self.root, base=self.base, lands=self.lands, lesson=self.lesson,
                    entry=self.entry, manifest=self.manifest, base_lesson=self.base_lesson)


def standard(name, urls=None, quotes=None, man_quotes=None, entry=None, caps=None, symlinks=None,
             s776_teach=None, s001=True, lesson_extra='', lesson_override=None, manifest_override=None):
    fx = FX(name)
    urls = {**DEFAULT_URLS, **(urls or {})}
    quotes = {**default_quotes(), **(quotes or {})}
    man_quotes = {**{rid: DEFAULT_MAN_QUOTE for rid in IDS}, **(man_quotes or {})}
    caps = {**default_caps(), **(caps or {})}
    symlinks = symlinks or {}
    put(fx.base, base_registry_text())
    put(fx.lands, lands_text(urls, s776_teach, s001))
    put(fx.base_lesson, BASE_LESSON)
    put(fx.lesson, lesson_override if lesson_override is not None else lesson_text(urls, quotes, lesson_extra))
    put(fx.entry, entry if entry is not None else mc.body(None))
    for rid in IDS:
        rel = f'{EV}/{rid}.txt'
        if rid in symlinks:
            if os.path.lexists(fx.p(rel)):
                os.remove(fx.p(rel))
            os.makedirs(os.path.dirname(fx.p(rel)), exist_ok=True)
            os.symlink(symlinks[rid], fx.p(rel))
        else:
            put(fx.p(rel), caps[rid])
    rows = {}
    for rid in IDS:
        rel = f'{EV}/{rid}.txt'
        data = open(fx.p(rel), 'rb').read()  # follows symlinks, as the grader does
        rows[rid] = dict(capture=rel, url=urls[rid], http_status=200,
                         fetched_at='2026-11-05T09:00:00-03:00', sha256=sha(data),
                         quote=man_quotes[rid])
    put(fx.manifest, manifest_override if manifest_override is not None else json.dumps({'rows': rows}, indent=1))
    return fx


def grade(fx):
    a = ['--root', fx.root, 'entry',
         '--entry', fx.entry,
         '--base-registry', fx.base,
         '--lands-registry', fx.lands,
         '--lesson', fx.lesson,
         '--manifest', fx.manifest,
         '--capture-dir', EV,
         '--as-of', AS_OF,
         '--topic', mc.TOPIC,
         '--topic-phrases', mc.PHRASES,
         '--min-topic-phrases', '4',
         '--min-bytes', '1200',
         '--min-headings', '4',
         '--min-new-ids', '3',
         '--min-topic-overlap', '8',
         '--table-min-rows', '5',
         '--table-min-cols', '3',
         '--base-lesson', fx.base_lesson,
         '--graded', 'corpus/SOURCES.md',
         '--graded', 'lesson.md',
         '--min-anchor-span', '3',
         '--min-gate-overlap', '3']
    cmd = [sys.executable, '-B', TOOL] + a
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=SCRATCH)
    out = ((r.stdout or '') + (r.stderr or '')).strip()
    return r.returncode, out, shlex.join(cmd)


# ---- round-93 counterfeit builders (unchanged from battery93.py) -----------

def b_g0():
    return standard('G0')


def b_chrome_noforge():
    return standard('C1c_chrome_noforge',
                    entry=mc.body(own_sentence='Freemium for Journals platform carries this note.'),
                    quotes={'S955': 'Freemium for Journals platform'})


def b_chrome_forged():
    return standard('A1_chrome_forged_manifest',
                    entry=mc.body(own_sentence='Freemium for Journals platform carries this note.'),
                    quotes={'S955': 'Freemium for Journals platform'},
                    man_quotes={'S955': 'Freemium Journals platform prayer address petition'})


def b_url(variant):
    def f():
        return standard('A2_url_' + re.sub(r'\W+', '_', variant)[:24], urls={'S955': variant})
    return f


ENTRY_A3 = mc.body(None)
Q_A3 = 'A prayer opens by naming the deity in the vocative'


def b_a3_exact():
    return standard('A3a_entry_exact_copy', entry=ENTRY_A3, caps={'S955': ENTRY_A3},
                    quotes={'S955': Q_A3}, man_quotes={'S955': 'prayer opens naming deity vocative'})


def b_a3_plus1():
    return standard('A3b_entry_plus_newline', entry=ENTRY_A3, caps={'S955': ENTRY_A3 + '\n'},
                    quotes={'S955': Q_A3}, man_quotes={'S955': 'prayer opens naming deity vocative'})


def _reps(text, reps):
    for a, b in reps:
        assert a in text, a
        text = text.replace(a, b)
    return text


def b_a4_span():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## address'),
        ('## 2. The petition', '## petition'),
        ('## 3. Fixed and extempore', '## efficacy'),
        ('## 4. Efficacy', '## Notes'),
        ('## 5. Table', '## Rites'),
        ('| element | fixed | extempore |', '| table | fixed | extempore |')])
    return standard('A4a_three_minimal_headings', entry=e)


def b_a4_onehead():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## address petition efficacy table'),
        ('## 2. The petition', '## Two'),
        ('## 3. Fixed and extempore', '## Three'),
        ('## 4. Efficacy', '## Four'),
        ('## 5. Table', '## Five')])
    return standard('A4b_all_phrases_one_heading', entry=e)


def b_lesson(extra, name):
    return lambda: standard(name, lesson_extra=extra)


def b_a6d_meta():
    caps = {'S955': ('<!doctype html><html><head><meta name="description" content="'
                     'prayer address petition votive promise fixed extempore efficacy register case 0">'
                     '</head><body><nav>Freemium for Journals platform</nav><script>var x=1;</script>'
                     '</body></html>')}
    return standard('A6e_quote_only_in_meta', caps=caps)


def b_a6f_decoy():
    urls = DEFAULT_URLS
    quotes = default_quotes()
    line1 = (f'- S955 admit A/mined. {urls["S955"]} \u2014 accessed {AS_OF} \u2014 '
             f'\u201c{quotes["S955"]}\u201d \u2014 body: \u201cFreemium for Journals platform\u201d\n')
    rest = ''.join(f'- {rid} admit A/mined. {urls[rid]} \u2014 accessed {AS_OF} \u2014 body: \u201c{quotes[rid]}\u201d\n'
                   for rid in ('S956', 'S957'))
    return standard('A6f_decoy_first_quote', lesson_override=line1 + rest)


def b_a6c_symlink_inroot():
    target = os.path.join(WORK, 'A6c_symlink_inroot_base_lesson', 'base-lesson.md')
    return standard('A6c_symlink_inroot_base_lesson',
                    quotes={'S955': 'an old base row about prayer notes and rubrics'},
                    man_quotes={'S955': 'an old base row about prayer notes and rubrics'},
                    symlinks={'S955': target})


def b_a6d_symlink_outside():
    outdir = os.path.join(SCRATCH, 'outside')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'S955-page.txt')
    put(outfile, default_caps()['S955'])
    return standard('A6d_symlink_outside_root', symlinks={'S955': outfile})


def b_a6a_base_rewrite():
    return standard('A6a_base_row_teaches_rewritten_in_lands',
                    s776_teach='prayer address petition votive promise fixed extempore efficacy register case')


def b_a6b_base_row_dropped():
    return standard('A6b_base_row_S001_dropped_in_lands', s001=False)


def b_a6g_manifest_list():
    return standard('A6g_manifest_rows_as_list', manifest_override=json.dumps({'rows': [1, 2, 3]}))


ATTACKS = [
    # id, expectation, recipe, builder
    ('G0', 'CLEAN', 'Compliant control: set-B grade of the unmodified mini-lane.', b_g0),
    ('C1c', 'REFUSE:GATE', 'Control for attack 1: chrome quote as an own sentence in the entry, manifest quote NOT forged.', b_chrome_noforge),
    ('A1', 'SURVIVE', 'Chrome quote "Freemium for Journals platform" as the gate quote, the same string as the entry\'s own sentence, and the manifest quote field forged to "Freemium Journals platform prayer address petition" so the content-word bind (3 words) passes.', b_chrome_forged),
    ('A2a', 'REFUSE:UNIQUENESS', 'Combined fragment + trailing slash + uppercase host: S955 url "https://REGISTRY-EXAMPLE.org/base-prayer-notes/#polari" (requested combined shadow).', b_url('https://REGISTRY-EXAMPLE.org/base-prayer-notes/#polari')),
    ('A2b', 'REFUSE:GATE/CAPTURE', 'Uppercase scheme "HTTPS://registry-example.org/base-prayer-notes": URL_RE is case-sensitive, so UNIQUENESS sees no url at all; another leg must refuse.', b_url('HTTPS://registry-example.org/base-prayer-notes')),
    ('A2c', 'SURVIVE', 'Scheme swap: S955 url "http://registry-example.org/base-prayer-notes" (same host and path as base S776 under http).', b_url('http://registry-example.org/base-prayer-notes')),
    ('A2d', 'SURVIVE', 'Host prefix: S955 url "https://www.registry-example.org/base-prayer-notes".', b_url('https://www.registry-example.org/base-prayer-notes')),
    ('A2e', 'SURVIVE', 'Query suffix: S955 url "https://registry-example.org/base-prayer-notes?ref=lane".', b_url('https://registry-example.org/base-prayer-notes?ref=lane')),
    ('A2f', 'SURVIVE', 'Path case: S955 url "https://registry-example.org/Base-Prayer-Notes".', b_url('https://registry-example.org/Base-Prayer-Notes')),
    ('A3a', 'REFUSE:CAPTURE', 'Capture file S955.txt is a byte-exact copy of the ENTRY; gate quote is an entry prose sentence; manifest sha = entry sha.', b_a3_exact),
    ('A3b', 'SURVIVE', 'Capture file S955.txt is the ENTRY plus one trailing newline (sha differs from the graded entry, text identical after norm).', b_a3_plus1),
    ('A4a', 'SURVIVE', 'Span gaming: four h2 headings, three of them a single phrase each ("## address", "## petition", "## efficacy"), "table" in the table header row; topical prose otherwise.', b_a4_span),
    ('A4b', 'REFUSE:TOPIC', 'Control for attack 4: all four phrases in one heading, no other heading or table hit (span 1).', b_a4_onehead),
    ('A5a', 'CLEAN', 'Prose sentence "S776 located in the archive, ..." in the lands lesson; S776 base disposition is LOCATED, so no movement.', b_lesson('S776 located in the archive, rechecked against the registry row.\n', 'A5a_prose_S776_located')),
    ('A5b', 'REFUSE:APPENDONLY', 'Prose sentence "S001 located in the archive, ..." in the lands lesson; S001 has no base disposition line (over-fire test on honest prose).', b_lesson('S001 located in the archive, rechecked against the registry row.\n', 'A5b_prose_S001_located')),
    ('A5c', 'REFUSE:APPENDONLY', 'Control for 5b: "S001 NOT located in the archive, ..." prose line (verdict flip spelled with a space).', b_lesson('S001 NOT located in the archive, rechecked against the registry row.\n', 'A5c_prose_S001_not_located')),
    ('A5d', 'SURVIVE', 'Bold-wrapped disposition "**S001** LOCATED recheck 90d accessed 2026-11-05" (under-fire: DISPO_RE anchor needs the id at line start after an optional whitespace-terminated prefix).', b_lesson('**S001** LOCATED recheck 90d accessed 2026-11-05\n', 'A5d_bold_disposition')),
    ('A5e', 'SURVIVE', 'Table-row disposition "| S001 | LOCATED | accessed 2026-11-05 |" in the lands lesson.', b_lesson('| S001 | LOCATED | accessed 2026-11-05 |\n', 'A5e_table_row_disposition')),
    ('A5f', 'SURVIVE', 'Zero-width space inside the verdict: "S001 LOC\\u200bATED recheck 90d accessed 2026-11-05" (renders as LOCATED, regex sees no token).', b_lesson('S001 LOC\u200bATED recheck 90d accessed 2026-11-05\n', 'A5f_zwsp_verdict')),
    ('A6a', 'SURVIVE', 'Invented class: lands registry base row S776 teaches cell rewritten to a flattering string (entry mode has no OTHERCELLS leg; base registry itself unchanged).', b_a6a_base_rewrite),
    ('A6b', 'SURVIVE', 'Invented class: base row S001 deleted from the lands registry (entry mode does not compare lands base rows to base).', b_a6b_base_row_dropped),
    ('A6c', 'SURVIVE', 'Invented class: S955 capture is an in-root SYMLINK to base-lesson.md (not graded, lexically confined path, sha matches target, quote in target bytes). Residual of routed finding 6 (non-graded blob).', b_a6c_symlink_inroot),
    ('A6d', 'SURVIVE', 'Invented class: S955 capture is a SYMLINK escaping the repository root to a file in the scratch dir (lexical confinement only).', b_a6d_symlink_outside),
    ('A6e', 'SURVIVE', 'Invented class: quote exists only in raw HTML markup (meta content attribute) of the capture, not in rendered text; CAPTURE matches raw bytes.', b_a6d_meta),
    ('A6f', 'SURVIVE', 'Invented class: gate line carries a valid first quote (bound, in capture) and a chrome "body:" quote second; only the first quote is ever checked.', b_a6f_decoy),
    ('A6g', 'REFUSE:unnamed', 'Operability probe: manifest with rows as a list (not a dict). Expected: unnamed traceback, not a named leg.', b_a6g_manifest_list),
]


# ---- round-94 battery classes (CriticClaims93 survivors, round-93 routed set) -------

GAINED_TAIL = (' \u2014 https://registry-example.org/base-old accessed ' + AS_OF
               + ': \u201canother old base row about dye plants\u201d\n')


def b94_a1():
    # Cyrillic lookalike O (U+041E) inside the verdict token of a gained S001 line.
    return standard('battery/A1', lesson_extra='- S001 L\u041eCATED recheck moved' + GAINED_TAIL)


def b94_b1():
    # Soft hyphen (U+00AD) inside the verdict token of a gained S001 line.
    return standard('battery/B1', lesson_extra='- S001 LOCA\u00adTED recheck moved' + GAINED_TAIL)


def b94_g1():
    # Numbered phrase-only h2 headings; the list number counts as a token in head_anchors().
    e = _reps(mc.body(None), [
        ('## 1. The address', '## 1. address'),
        ('## 2. The petition', '## 2. petition'),
        ('## 3. Fixed and extempore', '## 3. efficacy'),
        ('## 4. Efficacy', '## 4. table'),
        ('## 5. Table', '## 5. Rites')])
    return standard('battery/G1', entry=e)


def b94_h1():
    # Manifest row value for S955 is a JSON list instead of an object.
    fx = standard('battery/H1')
    m = json.load(open(fx.manifest, encoding='utf-8'))
    m['rows']['S955'] = [m['rows']['S955']['url']]
    put(fx.manifest, json.dumps(m, indent=1))
    return fx


def b94_i1():
    # Lands registry row S955 truncated to four cells.
    fx = standard('battery/I1')
    out = []
    for ln in open(fx.lands, encoding='utf-8').read().splitlines(keepends=True):
        if ln.startswith('| S955 |'):
            ln = '| S955 | ' + DEFAULT_URLS['S955'] + ' | docs | A |\n'
        out.append(ln)
    put(fx.lands, ''.join(out))
    return fx


def b94_j1():
    # En-dash (U+2013) inside NOT-LOCATED on a gained S001 line.
    return standard('battery/J1', lesson_extra='- S001 NOT\u2013LOCATED recheck unchanged' + GAINED_TAIL)


def b94_k1():
    # Lowercase unanchored verdict outside line start: evades the anchored regex and the
    # case-sensitive unanchored fallback in v4.
    return standard('battery/K1', lesson_extra='- note: S001 located recheck moved' + GAINED_TAIL)


def dispo_extra95(token):
    return f'S001 {token} recheck 90d accessed {AS_OF}\n'


def b95_cd1():
    # Combining acute U+0301 inside LOCATED (CriticO94 CD1).
    return standard('battery/CD1', lesson_extra=dispo_extra95('LOCA\u0301TED'))


def b95_lr1():
    # Left-to-right mark U+200E inside LOCATED (CriticO94 LR1).
    return standard('battery/LR1', lesson_extra=dispo_extra95('LO\u200eCATED'))


def b95_tab1():
    # Literal tab inside LOCATED (CriticO94 TAB1).
    return standard('battery/TAB1', lesson_extra=dispo_extra95('LO\tCATED'))


def b95_id1():
    # Small-cap S U+A731 in the id token (CriticO94 ID1).
    return standard('battery/ID1', lesson_extra=f'\ua731001 LOCATED recheck 90d accessed {AS_OF}\n')


def b95_num1():
    # Nested numbered phrase heads "## 1.1 address" etc. (CriticO94 NUM1).
    e = _reps(mc.body(None), [
        ('## 1. The address', '## 1.1 address'),
        ('## 2. The petition', '## 2.1 petition'),
        ('## 3. Fixed and extempore', '## 3.1 efficacy'),
        ('## 4. Efficacy', '## 4.1 table'),
        ('## 5. Table', '## 5. Notes')])
    return standard('battery/NUM1', entry=e)


def b95_rm1():
    # Roman numbered phrase heads "## I. address" etc. (CriticO94 RM1).
    e = _reps(mc.body(None), [
        ('## 1. The address', '## I. address'),
        ('## 2. The petition', '## II. petition'),
        ('## 3. Fixed and extempore', '## III. efficacy'),
        ('## 4. Efficacy', '## IV. table'),
        ('## 5. Table', '## V. Notes')])
    return standard('battery/RM1', entry=e)


def b95_num2():
    # Second-token numbered heads "## Notes 1) address" etc. (CriticO94 NUM2).
    e = _reps(mc.body(None), [
        ('## 1. The address', '## Notes 1) address'),
        ('## 2. The petition', '## Notes 2) petition'),
        ('## 3. Fixed and extempore', '## Notes 3) efficacy'),
        ('## 4. Efficacy', '## Notes 4) table'),
        ('## 5. Table', '## Notes 5) Table')])
    return standard('battery/NUM2', entry=e)


# ---- round-96 battery classes (CriticO95 survivors + round-95 F1, round-95 routed set) -------
# Expected outcomes on a correct v6/v7: NB1, VT1, FF1, LS1, NEL1, ANSI1, CYR1, BR1, DASH1
# survive v6 (rc 0, no named diagnostic) and must be REFUSED on v7; F1 is refused on TOPIC
# by v6 already (round-95 lesson 'The F1 non-numbered variant'). ZWNJ1 is a benign control:
# ZWNJ U+200C inside a table-cell phrase, expected CLEAN rc 0 on both.

def _dispo96(token, line_prefix='- S001 ', name='NB1'):
    return standard('battery/' + name, lesson_extra=line_prefix + token + ' recheck moved' + GAINED_TAIL)


def b96_nb1():
    # NBSP U+00A0 inside the verdict token of a gained S001 line (CriticO95 NB1).
    return _dispo96('LOCA' + chr(0x00A0) + 'TED', name='NB1')


def b96_vt1():
    # Vertical tab U+000B inside the verdict token (CriticO95 VT1).
    return _dispo96('LOCA' + chr(0x0B) + 'TED', name='VT1')


def b96_ff1():
    # Form feed U+000C inside the verdict token (CriticO95 FF1).
    return _dispo96('LOCA' + chr(0x0C) + 'TED', name='FF1')


def b96_ls1():
    # Line separator U+2028 inside the verdict token (CriticO95 LS1).
    return _dispo96('LOCA' + chr(0x2028) + 'TED', name='LS1')


def b96_nel1():
    # NEL U+0085 inside the verdict token (CriticO95 NEL1).
    return _dispo96('LOCA' + chr(0x85) + 'TED', name='NEL1')


def b96_ansi1():
    # ANSI CSI escape ESC U+001B + [31m inside the verdict token (CriticO95 ANSI1).
    return _dispo96('LOCA' + chr(0x1B) + '[31mTED', name='ANSI1')


def b96_cyr1():
    # Cyrillic small a U+0430 in place of the id letter S (CriticO95 CYR1).
    return _dispo96('LOCATED', line_prefix='- ' + chr(0x0430) + '001 ', name='CYR1')


def _entry96(name, reps):
    return standard('battery/' + name, entry=_reps(mc.body(None), reps))


def b96_br1():
    # Bracketed-number phrase heads "## (1) address" etc. (CriticO95 BR1).
    return _entry96('BR1', [
        ('## 1. The address', '## (1) address'),
        ('## 2. The petition', '## (2) petition'),
        ('## 3. Fixed and extempore', '## (3) efficacy'),
        ('## 4. Efficacy', '## (4) table'),
        ('## 5. Table', '## (5) Notes')])


def b96_dash1():
    # Separator-dash phrase heads "## - address" etc. (CriticO95 DASH1).
    return _entry96('DASH1', [
        ('## 1. The address', '## - address'),
        ('## 2. The petition', '## - petition'),
        ('## 3. Fixed and extempore', '## - efficacy'),
        ('## 4. Efficacy', '## - table'),
        ('## 5. Table', '## - Notes')])


def b96_f1():
    # Non-numbered content-free h2 heads "## alpha beta" style (round-95 lesson F1):
    # refusal is a TOPIC span failure on both v5 and v6; the class was routed for the
    # round-96 battery manifest (no battery class carried it in round 95).
    return _entry96('F1', [
        ('## 1. The address', '## alpha beta'),
        ('## 2. The petition', '## gamma delta'),
        ('## 3. Fixed and extempore', '## epsilon zeta'),
        ('## 4. Efficacy', '## eta theta'),
        ('## 5. Table', '## iota kappa')])


def b96_zwnj1():
    # Benign control: ZWNJ U+200C inside a table-cell phrase, expected CLEAN rc 0.
    return standard('battery/ZWNJ1',
                    entry=_reps(mc.body(None), [
                        ('| address | rote | improvised |',
                         '| addr' + chr(0x200C) + 'ess | rote | improvised |')]))


# (class, counterfeit description, tokens a correct grader must print, builder)
# A token is matched as a substring of the combined grader output. 'LEG FAIL <NAME>' is the
# leg line; a bare upper-case token or message is a diagnostic. A refusal that prints a token
# only through the wrong leg does not match (J1 accepts the NOT-LOCATED message, not a LOCATED one).
CLASSES = [
    ('A1', 'Cyrillic lookalike O (U+041E) in the verdict token LOCATED of a gained S001 lesson line; '
           'APPENDONLY sees no disposition.',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'LEG FAIL APPENDONLY'], b94_a1),
    ('B1', 'Soft hyphen (U+00AD) inside the verdict token of a gained S001 lesson line (LOCA\u00adTED).',
     ['NON-ASCII-VERDICT', 'VERDICT-SOFTHYPHEN', 'LEG FAIL APPENDONLY'], b94_b1),
    ('G1', 'Numbered phrase-only h2 headings (## 1. address, ## 2. petition, ## 3. efficacy, ## 4. table, '
           '## 5. Rites): the list number is counted as a heading token.',
     ['LEG FAIL TOPIC'], b94_g1),
    ('H1', 'Manifest row value for S955 is a JSON list, not a JSON object.',
     ['LEG FAIL GATE', 'LEG FAIL CAPTURE', 'MANIFEST-ROW-NOT-OBJECT', 'MANIFEST-ROW-TYPE'], b94_h1),
    ('I1', 'Lands registry row S955 truncated to four cells (| S955 | url | docs | A |).',
     ['LEG FAIL NEWIDS', 'REGISTRY-ROW-CELLS'], b94_i1),
    ('J1', 'En-dash (U+2013) in NOT\u2013LOCATED on a gained S001 lesson line; v4 reads it as LOCATED.',
     ['NON-ASCII-VERDICT', 'gained a NOT-LOCATED line'], b94_j1),
    ('K1', 'Lowercase unanchored verdict "- note: S001 located recheck moved ..." outside line start: '
           'evades the anchored regex and the case-sensitive fallback.',
     ['LEG FAIL APPENDONLY', 'VERDICT-LOWERCASE'], b94_k1),
    ('CD1', 'Combining acute U+0301 inside the verdict token of a gained S001 lesson line '
            '(LOCA\u0301TED, CriticO94 CD1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-COMBINE', 'COMBINING', 'LEG FAIL APPENDONLY'], b95_cd1),
    ('LR1', 'Left-to-right mark U+200E inside the verdict token of a gained S001 lesson line '
            '(LO\u200eCATED, CriticO94 LR1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-FORMAT', 'VERDICT-LRM', 'LEG FAIL APPENDONLY'], b95_lr1),
    ('TAB1', 'Literal tab inside the verdict token of a gained S001 lesson line '
             '(LO\tCATED, CriticO94 TAB1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-WS', 'VERDICT-TAB', 'LEG FAIL APPENDONLY'], b95_tab1),
    ('ID1', 'Small-cap S U+A731 in the id token of a gained S001 lesson line '
            '(\ua731001 LOCATED ..., CriticO94 ID1; verdict token is clean ASCII).',
     ['LEG FAIL APPENDONLY', 'VERDICT-NONASCII', 'NON-ASCII-VERDICT', 'ID-NONASCII'], b95_id1),
    ('NUM1', 'Nested numbered phrase-only h2 headings (## 1.1 address, ## 2.1 petition, ## 3.1 efficacy, '
             '## 4.1 table, ## 5. Notes, CriticO94 NUM1): the nested number counts as a heading anchor.',
     ['LEG FAIL TOPIC'], b95_num1),
    ('RM1', 'Roman numbered phrase-only h2 headings (## I. address, ## II. petition, ## III. efficacy, '
            '## IV. table, ## V. Notes, CriticO94 RM1).',
     ['LEG FAIL TOPIC'], b95_rm1),
    ('NUM2', 'Second-token numbered phrase-only h2 headings (## Notes 1) address, ## Notes 2) petition, '
             '## Notes 3) efficacy, ## Notes 4) table, ## Notes 5) Table, CriticO94 NUM2).',
     ['LEG FAIL TOPIC'], b95_num2),
    ('NB1', 'NBSP U+00A0 inside the verdict token of a gained S001 lesson line '
            '(LOCA\u00a0TED, CriticO95 NB1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-WS', 'VERDICT-NBSP', 'LEG FAIL APPENDONLY'], b96_nb1),
    ('VT1', 'Vertical tab U+000B inside the verdict token of a gained S001 lesson line '
            '(LOCA\u000bTED, CriticO95 VT1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-WS', 'VERDICT-VT', 'LEG FAIL APPENDONLY'], b96_vt1),
    ('FF1', 'Form feed U+000C inside the verdict token of a gained S001 lesson line '
            '(LOCA\u000cTED, CriticO95 FF1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-WS', 'VERDICT-FF', 'LEG FAIL APPENDONLY'], b96_ff1),
    ('LS1', 'Line separator U+2028 inside the verdict token of a gained S001 lesson line '
            '(LOCA\u2028TED, CriticO95 LS1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-WS', 'VERDICT-LINESEP', 'LEG FAIL APPENDONLY'], b96_ls1),
    ('NEL1', 'NEL U+0085 inside the verdict token of a gained S001 lesson line '
             '(LOCA\u0085TED, CriticO95 NEL1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-WS', 'VERDICT-NEL', 'LEG FAIL APPENDONLY'], b96_nel1),
    ('ANSI1', 'ANSI CSI escape ESC U+001B + [31m inside the verdict token of a gained S001 lesson '
             'line (LOCA\u001b[31mTED, CriticO95 ANSI1).',
     ['NON-ASCII-VERDICT', 'VERDICT-NONASCII', 'VERDICT-ESC', 'VERDICT-ANSI', 'LEG FAIL APPENDONLY'], b96_ansi1),
    ('CYR1', 'Cyrillic small a U+0430 in place of the id letter S of a gained '
             'S001 lesson line (\u0430001 LOCATED ..., CriticO95 CYR1).',
     ['LEG FAIL APPENDONLY', 'VERDICT-NONASCII', 'NON-ASCII-VERDICT', 'ID-NONASCII', 'ID-HOMOGLYPH',
      'VERDICT-HOMOGLYPH'], b96_cyr1),
    ('BR1', 'Bracketed numbered phrase-only h2 headings (## (1) address, ## (2) petition, '
            '## (3) efficacy, ## (4) table, CriticO95 BR1).',
     ['LEG FAIL TOPIC'], b96_br1),
    ('DASH1', 'Separator-dash phrase-only h2 headings (## - address, ## - petition, '
              '## - efficacy, ## - table, CriticO95 DASH1).',
     ['LEG FAIL TOPIC'], b96_dash1),
    ('F1', 'Non-numbered content-free h2 headings (## alpha beta, ## gamma delta, '
           '## epsilon zeta, ## eta theta, round-95 lesson F1).',
     ['LEG FAIL TOPIC'], b96_f1),
    ('G0', 'Clean control: unmodified mini-lane, expected CLEAN rc 0.', [], b_g0),
    ('ZWNJ1', 'Benign control: ZWNJ U+200C inside a table-cell phrase (addr\u200cess), '
              'expected CLEAN rc 0.', [], b96_zwnj1),
]


# ---- grading helpers ------------------------------------------------------------

def legs_of(out):
    fails = re.findall(r'FAIL\s+([A-Z]+)', out)
    passes = re.findall(r'PASS\s+([A-Z]+)', out)
    return sorted(set(fails)), sorted(set(passes))


def classify(expect, rc, out):
    fails, passes = legs_of(out)
    if rc == 0:
        return 'SURVIVOR' if expect == 'SURVIVE' else 'CLEAN'
    if rc == 1 and fails:
        return 'refused on ' + ','.join(fails)
    return f'refused-unnamed (rc={rc})'


CONTROL_CLASSES = ('G0', 'ZWNJ1')


def class_outcome(rc, out, tokens, cls=None):
    tb = 'Traceback' in out
    if cls in CONTROL_CLASSES:
        # CLEAN control: rc 0 without traceback -> CLEAN; anything else is data (NOT-CLEAN).
        outcome = 'CLEAN' if (rc == 0 and not tb) else 'NOT-CLEAN'
        return dict(rc=rc, traceback='yes' if tb else 'no', named='none', outcome=outcome, hit=None)
    hit = next((t for t in tokens if t in out), None)
    if rc == 0:
        return dict(rc=rc, traceback='yes' if tb else 'no', named='none', outcome='SURVIVOR', hit=None)
    outcome = 'REFUSED' if (hit and not tb) else 'UNNAMED'
    named = 'none' if hit is None else (hit[len('LEG FAIL '):] if hit.startswith('LEG FAIL ') else hit.replace(' ', '_'))
    return dict(rc=rc, traceback='yes' if tb else 'no', named=named, outcome=outcome, hit=hit)


def run_classes(verbose):
    results = []
    for cls, desc, tokens, builder in CLASSES:
        fx = builder()
        rc, out, _cmd = grade(fx)
        r = class_outcome(rc, out, tokens, cls)
        results.append((cls, desc, tokens, fx, r))
        print(f'CLASS {cls} rc={r["rc"]} traceback={r["traceback"]} named={r["named"]} outcome={r["outcome"]}')
        if verbose:
            fails, _ = legs_of(out)
            obs = [l[:220] for l in out.splitlines() if l.startswith('LEG FAIL')]
            last = (out.strip().splitlines() or [''])[-1][:200]
            print(f'  detail {cls}: fail-legs={",".join(fails) or "none"} last-line={last!r}')
            for o in obs:
                print(f'  detail {cls}: {o}')
    return results


def summarize(results):
    # Totals are over the expected-REFUSE classes only; controls (CLEAN) never count
    # as survivors/refused/unnamed, so a passing ZWNJ1 control does not inflate survivors.
    surv = sum(1 for r in results if r[4]['outcome'] == 'SURVIVOR')
    unnamed = sum(1 for r in results if r[4]['outcome'] == 'UNNAMED')
    refused = sum(1 for r in results if r[4]['outcome'] == 'REFUSED')
    tb = sum(1 for r in results if r[4]['traceback'] == 'yes')
    clean = sum(1 for r in results if r[4]['outcome'] == 'CLEAN')
    not_clean = sum(1 for r in results if r[4]['outcome'] == 'NOT-CLEAN')
    print(f'BATTERY-SUMMARY survivors={surv} unnamed={unnamed} refused={refused} traceback={tb} clean={clean} not-clean={not_clean}')


def run_regression():
    # round-93 attack list (battery93 grade set, unchanged expectations).
    for aid, expect, _recipe, builder in ATTACKS:
        fx = builder()
        rc, out, _cmd = grade(fx)
        fails, _ = legs_of(out)
        outcome = classify(expect, rc, out)
        print(f'REG R93 {aid} rc={rc} expect={expect} fail={",".join(fails) or "none"} outcome={outcome}')
    # round-92 V-series (frozen builder's ATTACKS, graded with set B as in round 93's counter).
    v92 = os.path.join(SCRATCH, 'v92')
    os.makedirs(v92, exist_ok=True)
    cases = [(name, leg, mc.build_tree(v92, name, name)) for name, leg in mc.ATTACKS]
    cases.append(('G0', 'CLEAN', mc.build_tree(v92, 'G0', None)))
    for name, leg, fxd in cases:
        rc, verdict, full = mc.run_tool(TOOL, 'v3', 'B', fxd)
        fails, _ = legs_of(full)
        if leg == 'CLEAN':
            outcome = 'clean' if rc == 0 else f'NOT clean (rc={rc})'
        else:
            named = f'FAIL {leg}' in full
            outcome = f'refused on {leg}' if (rc == 1 and named) else f'NOT refused on {leg} (rc={rc})'
        print(f'REG R92 {name} rc={rc} expect={leg} fail={",".join(fails) or "none"} outcome={outcome}')


def emit_stage(stage, results):
    stage = os.path.abspath(stage)
    dst = os.path.join(stage, 'battery')
    shutil.rmtree(dst, ignore_errors=True)
    os.makedirs(dst, exist_ok=True)
    entries = []
    for cls, desc, tokens, fx, _r in results:
        shutil.copytree(fx.root, os.path.join(dst, cls))
        entries.append(dict(
            class_name=cls,
            counterfeit=desc,
            leg_or_diagnostic_named_any_of=tokens,
            expected_exit='zero' if cls in CONTROL_CLASSES else 'nonzero',
            fixture=f'battery/{cls}',
            grade='battery96.py grade(): entry mode, set B (--min-anchor-span 3 --min-gate-overlap 3), builder floors',
        ))
    man = dict(schema='kotodama-round-96-battery-manifest-v1',
               tool_under_test='tools/check-advance-evidence.py',
               driver='battery96.py',
               classes=entries)
    with open(os.path.join(stage, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(man, f, indent=1, ensure_ascii=False)
        f.write('\n')


def main(argv=None):
    ap = argparse.ArgumentParser(description='Round-96 counterfeit battery driver (battery96.py)')
    ap.add_argument('--tool', required=True, help='grader under test (e.g. tools/check-advance-evidence.py)')
    ap.add_argument('--work', required=True, help='scratch dir (must not be under /tmp)')
    ap.add_argument('--emit', default='', help='stage dir: copy class fixtures to <stage>/battery and write <stage>/manifest.json')
    ap.add_argument('--verbose', action='store_true', help='print detail lines (fail legs, last line) per class')
    a = ap.parse_args(argv)
    work = os.path.abspath(a.work)
    if work == '/tmp' or work.startswith('/tmp/'):
        print('refused: --work must not be under /tmp', file=sys.stderr)
        return 2
    if not os.path.isfile(a.tool):
        print(f'refused: --tool not a file: {a.tool}', file=sys.stderr)
        return 2
    configure(a.tool, work)
    print(f'TOOL sha256={sha(open(TOOL, "rb").read())} path={TOOL}')
    results = run_classes(a.verbose)
    summarize(results)
    run_regression()
    if a.emit:
        emit_stage(a.emit, results)
    return 0


if __name__ == '__main__':
    sys.exit(main())
