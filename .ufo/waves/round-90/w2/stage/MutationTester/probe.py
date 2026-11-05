#!/usr/bin/env python3
"""Differential probes for the surviving mutants of the second pass.

For each survivor, call the same grader functions on the same crafted fixture
with the clean bytes and the mutant bytes, and print both observables. This
separates 'survived because no fixture reaches the code' (a real coverage gap)
from 'equivalent mutant' (no observable difference at all).
"""
import hashlib
import importlib.util
import os
import shutil
import sys
import types

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
import mut2  # noqa: E402

CLEAN_TOOL = os.path.join(BASE, 'lands/tools/check-advance-evidence.py')
WORK = os.path.join(BASE, 'work/probe')
CAPDIR = 'reports/round-90/evidence'
QUOTE = 'the fixed vocative formulae address the deity and the votive promise binds the petitioner'
TEACH = 'prayer addressed to a named deity through fixed vocative formulae and votive promises'
URL = 'https://example.org/prayer'
TOPIC = ('prayer as a petitionary address register: vocative formulae, votive promises, '
         'fixed and extempore speech, efficacy claims')


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mutant_path(name):
    text = open(CLEAN_TOOL).read()
    for n, old, new in mut2.MUTANTS:
        if n == name:
            p = os.path.join(WORK, 'mut', name + '.py')
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, 'w').write(text.replace(old, new))
            return p
    raise KeyError(name)


def newroot(tag):
    root = os.path.join(WORK, 'root-' + tag)
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(os.path.join(root, CAPDIR), exist_ok=True)
    return root


def mkfile(root, rel, body):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(body)
    return p


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


# ---------------------------------------------------------------- capture probes
def cap_probe(root, mod, rel, entry_over):
    body = 'Capture. ' + QUOTE + ' Also boilerplate.'
    p = mkfile(root, rel, body)
    entry = dict(capture=rel, url=URL, http_status=200,
                 fetched_at='2026-11-04T19:00:00-03:00', sha256=sha(p))
    entry.update(entry_over)
    return mod.capture_error(CAPDIR, ['corpus/SOURCES.md', 'corpus/lessons/round-90.md'],
                             entry, QUOTE, '2026-11-04', root)


def p_capture_traversal(root, mod):
    return cap_probe(root, mod, CAPDIR + '/../../secret/leak.txt', {})


def p_capture_sha_absent(root, mod):
    return cap_probe(root, mod, CAPDIR + '/S001.txt', {'sha256': ''})


def p_capture_http_302(root, mod):
    return cap_probe(root, mod, CAPDIR + '/S001.txt', {'http_status': 302})


def p_capture_fetched_prev_day(root, mod):
    return cap_probe(root, mod, CAPDIR + '/S001.txt',
                     {'fetched_at': '2026-11-03T19:00:00-03:00'})


def p_capture_prefix_sibling(root, mod):
    return cap_probe(root, mod, 'reports/round-90/evidence-extra/S001.txt', {})


# ---------------------------------------------------------------- registry probes
def p_row_indent_4(root, mod):
    row4 = '    | S777 | https://example.org/x | docs | A | s | a | t | mined | 2026-11-04 | 90d | u |'
    rows, dup = mod.registry(row4)
    return f'ids={[r["id"] for r in rows]} dup={dup}'


def p_row_indent_1(root, mod):
    row1 = ' | S777 | https://example.org/x | docs | A | s | a | t | mined | 2026-11-04 | 90d | u |'
    rows, dup = mod.registry(row1)
    return f'ids={[r["id"] for r in rows]} dup={dup}'


# ---------------------------------------------------------------- entry fixtures
TABLE_ROWS = ('| address | rote | improvised |\n| petition | set | composed |\n'
              '| promise | written | spoken |\n| authority | text | speaker |\n'
              '| failure | ritual fault | weak speaker |\n')


def entry_body(table_rows=5, cite='S010 S011 S012'):
    rows = ['| address | rote | improvised |', '| petition | set | composed |',
            '| promise | written | spoken |', '| authority | text | speaker |',
            '| failure | ritual fault | weak speaker |'][:table_rows]
    table = '| element | fixed | extempore |\n|---|---|---|\n' + '\n'.join(rows) + '\n'
    return (
        '# Prayer and petition\n\n- topic: prayer as a petitionary address register\n'
        '- sources: S010 S011 S012\n- verified-at: 2026-11-04\n- recheck: 180d\n\n'
        '## 1. The address\n\nA prayer opens by naming the deity in the vocative and stating the petitioner. '
        'The vocative formulae vary by rank and by occasion, and the petitioner names a claim on the god.\n\n'
        '## 2. The petition\n\nThe petition states a want in a fixed order: address, reminder of past favour, request, promise. '
        'The votive promise binds the petitioner to a return and is the enforceable half of the exchange.\n\n'
        '## 3. Fixed and extempore\n\nFixed prayer is recited by rote and its wording is protected from change. '
        'Extempore prayer is composed at the moment and its authority rests on the speaker rather than the text.\n\n'
        '## 4. Efficacy\n\nA prayer claims efficacy through the address, the promise or the speaker. '
        'The claim is graded in the culture: some prayers are held to compel, others only to petition.\n\n'
        '## 5. Table\n\n' + table + '\n'
        '## 6. Language choice\n\nThe language of prayer is chosen by the address: a god may be addressed only in a sacred register. '
        + cite + ' supply the comparative cases and each claim above is bounded to them.\n')


NEW_IDS = [('S010', 'https://example.org/a'), ('S011', 'https://example.org/b'),
           ('S012', 'https://example.org/c')]
GATE_QUOTE = 'prayer address petition votive promise fixed extempore efficacy register case'


def entry_fixture(root, mod, table_rows=5, status='mined', cite='S010 S011 S012',
                  row_urls=None, lesson_over=None, extra_base_cited=False):
    url = {rid: u for rid, u in NEW_IDS}
    if row_urls:
        url.update(row_urls)
    base = mod.HEADER + '\n' + mod._row('S001', URL, TEACH) + '\n' \
        + mod._row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n'
    mkfile(root, 'base.md', base)
    lands = base
    entry_rel = 'corpus/knowledge/myth-symbol/prayer-register.md'
    for rid, u in NEW_IDS:
        lands += mod._row(rid, url[rid], 'prayer address petition votive promise register case', tier='A',
                          status=status, opened='2026-11-04', used=entry_rel) + '\n'
        mkfile(root, f'{CAPDIR}/{rid}.txt', f'Page text. {GATE_QUOTE} {rid}.')
    mkfile(root, 'lands.md', lands)
    entry = mkfile(root, entry_rel, entry_body(table_rows, cite))
    man = {}
    for rid, u in NEW_IDS:
        p = os.path.join(root, f'{CAPDIR}/{rid}.txt')
        man[rid] = dict(capture=f'{CAPDIR}/{rid}.txt', url=url[rid], http_status=200,
                        fetched_at='2026-11-04T19:00:00-03:00', sha256=sha(p))
    mkfile(root, 'manifest.json', __import__('json').dumps({'rows': man}))
    lines = []
    for rid, u in NEW_IDS:
        q = GATE_QUOTE + (' ' + rid if lesson_over is None else ' ' + rid)
        lines.append(f'- {rid} admit A/mined. {u} \u2014 accessed 2026-11-04 \u2014 body: \u201c{q}\u201d')
    if lesson_over:
        lines = lesson_over(lines)
    mkfile(root, 'lesson.md', '\n'.join(lines) + '\n')
    args = types.SimpleNamespace(
        entry=entry, base_registry=os.path.join(root, 'base.md'),
        lands_registry=os.path.join(root, 'lands.md'), lesson=os.path.join(root, 'lesson.md'),
        manifest=os.path.join(root, 'manifest.json'), capture_dir=CAPDIR, as_of='2026-11-04',
        topic=TOPIC, min_bytes=1200, min_headings=4, min_new_ids=3, min_topic_overlap=8,
        table_min_rows=5, table_min_cols=3, quote_max_words=25, quote_min_chars=20,
        graded=['corpus/SOURCES.md', 'corpus/lessons/round-90.md'], root=root)
    return args


def leg(legs, name):
    for n, passed, expected, observed in legs:
        if n == name:
            return f'{name}:{"PASS" if passed else "FAIL"} {observed}'
    return f'{name}:absent'


ENTRY_ARGS = dict(table_rows=5, status='mined', cite='S010 S011 S012', row_urls=None,
                  lesson_over=None)


def p_entry_table_4rows(root, mod):
    a = entry_fixture(root, mod, **dict(ENTRY_ARGS, table_rows=4))
    return leg(mod.grade_entry(a)[0], 'SHAPE')


def p_topic_floor(root, mod):
    a = entry_fixture(root, mod, **ENTRY_ARGS)
    shared = mod.overlap(open(a.entry).read(), TOPIC)
    a.min_topic_overlap = shared + 1
    return leg(mod.grade_entry(a)[0], 'TOPIC')


def p_entry_status_retired(root, mod):
    a = entry_fixture(root, mod, **dict(ENTRY_ARGS, status='retired'))
    return leg(mod.grade_entry(a)[0], 'NEWIDS')


def p_entry_base_cited(root, mod):
    a = entry_fixture(root, mod, **dict(ENTRY_ARGS, cite='S001 S010 S011 S012'))
    return leg(mod.grade_entry(a)[0], 'NEWIDS')


def p_entry_url_trailing_slash(root, mod):
    a = entry_fixture(root, mod, **dict(ENTRY_ARGS, row_urls={'S010': 'https://example.org/a/'}))

    def slash(lines):
        return [lines[0].replace('https://example.org/a/', 'https://example.org/a')] + lines[1:]
    a = entry_fixture(root, mod, **dict(ENTRY_ARGS, row_urls={'S010': 'https://example.org/a/'},
                                        lesson_over=slash))
    return leg(mod.grade_entry(a)[0], 'GATE')


def p_entry_quote_order(root, mod):
    def decoy(lines):
        return ['- S010 LOCATED recheck \u2014 https://example.org/a accessed 2026-11-04: '
                f'\u201c{GATE_QUOTE} S010\u201d',
                '- S010 admit A/mined. accessed 2026-11-04 \u2014 body: \u201c' + GATE_QUOTE + ' S010\u201d'] \
            + lines[1:]
    a = entry_fixture(root, mod, **dict(ENTRY_ARGS, lesson_over=decoy))
    return leg(mod.grade_entry(a)[0], 'GATE')


# ---------------------------------------------------------------- advance fixture
def p_advance_dup(root, mod):
    base = mod.HEADER + '\n' + mod._row('S001', URL, TEACH) + '\n' \
        + mod._row('S002', 'https://example.org/other', 'unrelated row about dye plants and textile trade') + '\n'
    mkfile(root, 'base.md', base)
    mkfile(root, 'lands.md', base.replace('| S001 | ' + URL + ' | docs | A | scope | anchor | ' + TEACH +
                                         ' | mined | 2026-10-19 | 90d | corpus/knowledge/x.md |',
                                         '| S001 | ' + URL + ' | docs | A | scope | anchor | ' + TEACH +
                                         ' | mined | 2026-10-19 | 2027-02-03 | corpus/knowledge/x.md |')
          + mod._row('S001', URL, TEACH, recheck='2027-02-03') + '\n')
    mkfile(root, 'lesson.md',
           '- S001 LOCATED recheck 90d\u21922027-02-03 \u2014 ' + URL + ' accessed 2026-11-04: '
           '\u201c' + QUOTE + '\u201d\n'
           '- S002 LOCATED unchanged \u2014 https://example.org/other accessed 2026-11-04: '
           '\u201cunrelated row about dye plants\u201d\n')
    mkfile(root, f'{CAPDIR}/S001.txt', 'Capture. ' + QUOTE + ' Also boilerplate.')
    man = {'S001': dict(capture=f'{CAPDIR}/S001.txt', url=URL, http_status=200,
                        fetched_at='2026-11-04T19:00:00-03:00',
                        sha256=sha(os.path.join(root, f'{CAPDIR}/S001.txt')))}
    mkfile(root, 'manifest.json', __import__('json').dumps({'rows': man}))
    args = types.SimpleNamespace(
        base_registry=os.path.join(root, 'base.md'), lands_registry=os.path.join(root, 'lands.md'),
        lesson=os.path.join(root, 'lesson.md'), manifest=os.path.join(root, 'manifest.json'),
        capture_dir=CAPDIR, as_of='2026-11-04', population='S001,S002', population_file=None,
        min_advanced=1, window_days=90, max_days=366, min_overlap=1, quote_max_words=25,
        quote_min_chars=20, graded=['corpus/SOURCES.md', 'corpus/lessons/round-90.md'], root=root)
    legs, _ = mod.grade_advance(args)
    return leg(legs, 'ADVANCED') + ' | ' + leg(legs, 'SHADOW')


PROBES = [
    ('shape-table-row-off-by-one', p_entry_table_4rows),
    ('topic-floor-off-by-one', p_topic_floor),
    ('newids-status-off', p_entry_status_retired),
    ('newids-basesubtract-off', p_entry_base_cited),
    ('gate-url-slash-relaxed', p_entry_url_trailing_slash),
    ('gate-quote-selection-last', p_entry_quote_order),
    ('capture-traversal-guard-off', p_capture_traversal),
    ('capture-sha256-skip-absent', p_capture_sha_absent),
    ('capture-http-status-widen', p_capture_http_302),
    ('capture-fetched-date-off', p_capture_fetched_prev_day),
    ('capture-prefix-boundary-off', p_capture_prefix_sibling),
    ('row-indent-unbounded', p_row_indent_4),
    ('row-indent-zero-only', p_row_indent_1),
    ('advanced-dup-length-lenient', p_advance_dup),
]


def main():
    clean = load(CLEAN_TOOL, 'cleanmod')
    names = sys.argv[1:] or [n for n, _ in PROBES]
    out = []
    for name, fn in PROBES:
        if name not in names:
            continue
        root_c = newroot(name + '-c')
        root_m = newroot(name + '-m')
        try:
            obs_c = fn(root_c, clean)
        except Exception as exc:  # noqa: BLE001
            obs_c = f'EXC {type(exc).__name__}: {exc}'
        mut = load(mutant_path(name), 'mutmod')
        try:
            obs_m = fn(root_m, mut)
        except Exception as exc:  # noqa: BLE001
            obs_m = f'EXC {type(exc).__name__}: {exc}'
        same = obs_c == obs_m
        out.append(f'{"EQ  " if same else "DIFF"} {name}\n     clean  : {obs_c}\n     mutant : {obs_m}')
    text = '\n'.join(out)
    print(text)
    open(os.path.join(BASE, 'out', 'probes.txt'), 'w').write(text + '\n')


if __name__ == '__main__':
    main()
