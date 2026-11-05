#!/usr/bin/env python3
"""Build the seven routed round-91 counterfeit landings and grade them with
supplied grader binaries (round-92 before/after controls, CriticClaims91
attacks.md findings 1-6 + the shared-capture clause of finding 3).

    python3 -B reports/round-92/controls/make-counterfeits.py \
        --work <existing-dir> --tool v2=<path-to-v2-tool> --tool v3=<path-to-v3-tool>

Each counterfeit is the round-91 critic's fixture recipe rebuilt as a
standalone mini-lane (base registry, lands registry, round lesson, entry,
evidence captures, manifest) under <work>/<attack>/. The compliant G0 landing
is built by the same code with no attack applied (the positive control: a
blanket refuser scores 0/7 named findings on it).

Args set A is accepted by both v2 and v3 (the before tool must be able to run
the same command); set B adds the v3-declared floors (--min-anchor-span,
--min-gate-overlap) and is the command the round-92 counter drives at lands.

Output: <work>/before-v2-counterfeits.txt and <work>/after-v3-refusals.txt.
Exit 0 when every named expectation holds; 1 otherwise.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

HEADER = ('| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'
          '|---|---|---|---|---|---|---|---|---|---|---|')

ENTRY_NAME = 'corpus/knowledge/myth-symbol/prayer-register.md'
TOPIC = 'prayer as a petitionary address register: vocative formulae, votive promises, fixed and extempore speech, efficacy claims'
PHRASES = 'address;petition;efficacy;table'

BASE_ROW_URL = 'https://registry-example.org/base-prayer-notes'
NEW_ROWS = [('S955', 'https://registry-example.org/verlan-case-0'),
            ('S956', 'https://registry-example.org/verlan-case-1'),
            ('S957', 'https://registry-example.org/verlan-case-2')]


def _row(rid, url, teaches, tier='A', status='mined', opened='2026-11-05', used=ENTRY_NAME, recheck='90d'):
    return (f'| {rid} | {url} | docs | {tier} | scope | anchor | {teaches} | {status} | {opened} | {recheck} | {used} |')


def body(own_sentence=None):
    heads = ['## 1. The address', '## 2. The petition', '## 3. Fixed and extempore',
             '## 4. Efficacy', '## 5. Table']
    prose = [
        'A prayer opens by naming the deity in the vocative and stating the petitioner and the petitioner\u2019s standing. The vocative formulae vary by rank and by occasion, and a wrong name is held to spoil the rite.',
        'The petition states a want in a fixed order: address, reminder of past favour, request, promise. The votive promise binds the petitioner to a return offering and is the enforceable half of the exchange.',
        'Fixed prayer is recited by rote and its wording is protected from change by the custody of specialists. Extempore prayer is composed at the moment and its authority rests on the speaker rather than on the text.',
        'A prayer claims efficacy through the address, the promise or the speaker, and the claim is graded in the culture: some prayers are held to compel, others only to petition.',
        'In village practice the two styles alternate: the rote opening is spoken by all, and the extempore core is spoken by the officiant alone while the rest keep a low murmur.',
        'A missed observance is repaired by a renewed promise, and the renewed promise is witnessed, which is why the wording of the witness formula is itself conservative.',
    ]
    parts = ['# Prayer and petition\n',
             '- topic: prayer as a petitionary address register\n- sources: S955 S956 S957\n'
             '- verified-at: 2026-11-05\n- recheck: 180d\n']
    for i, h in enumerate(heads):
        parts.append(f'\n{h}\n\n')
        if i == 0 and own_sentence:
            parts.append(own_sentence + ' ')
        parts.append(prose[i % len(prose)] + '\n')
    parts.append('\n| element | fixed | extempore |\n|---|---|---|\n')
    for row in ('address | rote | improvised', 'petition | set | composed',
                'promise | written | spoken', 'authority | text | speaker',
                'failure | ritual fault | weak speaker'):
        parts.append('| ' + row + ' |\n')
    parts.append('\nS955 S956 S957 supply the comparative cases and each claim above is bounded to them.\n')
    return ''.join(parts)


def build_tree(work, name, attack):
    """Build a mini-lane under work/name; attack None builds the G0 control."""
    root = os.path.join(work, name)
    shutil.rmtree(root, ignore_errors=True)
    ev = os.path.join(root, 'reports/round-90/evidence')
    os.makedirs(ev, exist_ok=True)
    caps = {}
    for i, (rid, u) in enumerate(NEW_ROWS):
        caps[rid] = (f'Page text. prayer address petition votive promise fixed extempore efficacy register case {i}. '
                     'Also site boilerplate and navigation. Freemium for Journals platform.')
    base = os.path.join(root, 'base.md')
    with open(base, 'w') as f:
        f.write(HEADER + '\n'
                + _row('S776', BASE_ROW_URL, 'an old base row about prayer notes and rubrics') + '\n'
                + _row('S001', 'https://registry-example.org/base-old', 'another old base row about unrelated dye plants') + '\n')
    lands_rows = [_row('S776', BASE_ROW_URL, 'an old base row about prayer notes and rubrics'),
                  _row('S001', 'https://registry-example.org/base-old', 'another old base row about unrelated dye plants')]
    urls = {rid: u for rid, u in NEW_ROWS}
    cap_for = {rid: f'reports/round-90/evidence/{rid}.txt' for rid, _ in NEW_ROWS}
    if attack == 'V3':
        urls['S955'] = BASE_ROW_URL + '#polari'
    if attack == 'V12':
        urls['S956'] = 'https://registry-example.org/never-fetched-url'
        cap_for['S956'] = cap_for['S955']
    lesson_lines = []
    for i, (rid, _u) in enumerate(NEW_ROWS):
        lesson_lines.append(f'- {rid} admit A/mined. {urls[rid]} \u2014 accessed 2026-11-05 \u2014 body: '
                            f'\u201cprayer address petition votive promise fixed extempore efficacy register case {i}\u201d')
    if attack == 'V12':
        lesson_lines[1] = ('- S956 admit A/mined. ' + urls['S956'] + ' \u2014 accessed 2026-11-05 \u2014 body: '
                           '\u201cPage text. prayer address petition votive promise fixed extempore efficacy register case 0\u201d')
        man_rows_quote_override = ('S956', 'Page text. prayer address petition votive promise fixed extempore efficacy register case 0')
    else:
        man_rows_quote_override = None
    if attack == 'V7':
        lesson_lines[0] = ('- S955 admit A/mined. ' + NEW_ROWS[0][1] + ' \u2014 accessed 2026-11-05 \u2014 body: '
                           '\u201cFreemium for Journals platform\u201d')
    lesson_text = '\n'.join(lesson_lines) + '\n'
    if attack == 'V10a':
        lesson_text += 'S776 NOT-LOCATED recheck 90d->2027-02-03 accessed 2026-11-05: \u201cno quote needed for a bare line\u201d\n'
    if attack == 'V10c':
        lesson_text += '> - S001 LOCATED noted at recheck accessed 2026-11-05: \u201cblockquote carries the move\u201d\n'
    filler_variants = [
        'The bakehouse rota schedules deliveries and tracks flour costs across the district every week.',
        'Bakers argue about proofing times and oven temperatures, and the apprentice logs the ashes from every second firing.',
        'The guild keeps written records of each run, and the ledger is read aloud at the quarterly meeting.',
        'Sourdough starter care is passed from mother to daughter with the mixing bowl, never written down.',
        'Ovens are fired before dawn so the first batch meets the market bell, and the wood is stacked by the door the night before.',
        'Prices are chalked on a slate beside the counter and wiped clean at closing, which is why so little paper survives.',
    ]
    if attack == 'V2':
        entry_text = ('# Prayer and petition\n\n- topic: prayer as a petitionary address register\n- sources: S955 S956 S957\n'
                      '- verified-at: 2026-11-05\n- recheck: 180d\n\n'
                      '## Address, petition, efficacy and table of the bakehouse rota\n\n'
                      'The address petition efficacy table words appear in this one heading alone, and the '
                      'bridge sentence carries the vocative and votive words for the overlap floor; the rest '
                      'of this entry is filler prose about the bakery rota and its scheduling needs.\n\n')
        for h, a, b in zip(('## 2. Filler one', '## 3. Filler two', '## 4. Filler three'),
                           filler_variants[0::2], filler_variants[1::2]):
            entry_text += f'{h}\n\n{a} {b}\n\n'
        entry_text += ('| element | fixed | extempore |\n|---|---|---|\n'
                       + ''.join('| ' + row + ' |\n' for row in
                                 ('address | rote | improvised', 'petition | set | composed',
                                  'promise | written | spoken', 'authority | text | speaker',
                                  'failure | ritual fault | weak speaker'))
                       + '\nS955 S956 S957 supply the comparative cases and each claim above is bounded to them.\n')
    else:
        entry_text = body(own_sentence='Freemium for Journals platform carries this note.' if attack == 'V7' else None)
    lands = os.path.join(root, 'lands.md')
    with open(lands, 'w') as f:
        f.write(HEADER + '\n' + '\n'.join(lands_rows) + '\n')
    written = set()
    for rid, u in NEW_ROWS:
        if cap_for[rid] in written:
            continue
        written.add(cap_for[rid])
        with open(os.path.join(root, cap_for[rid]), 'w') as f:
            f.write(caps[rid])
    with open(lands, 'a') as f:
        for rid, u in NEW_ROWS:
            f.write(_row(rid, urls[rid], 'prayer address petition votive promise register case') + '\n')
    lesson = os.path.join(root, 'lesson.md')
    with open(lesson, 'w') as f:
        f.write(lesson_text)
    base_lesson = os.path.join(root, 'base-lesson.md')
    with open(base_lesson, 'w') as f:
        f.write('- S776 LOCATED recheck unchanged \u2014 ' + BASE_ROW_URL
                + ' accessed 2026-10-01: \u201can old base row about prayer notes and rubrics\u201d\n')
    entry = os.path.join(root, ENTRY_NAME)
    os.makedirs(os.path.dirname(entry), exist_ok=True)
    with open(entry, 'w') as f:
        f.write(entry_text)
    man_rows = {}
    for rid, u in NEW_ROWS:
        cap = os.path.join(root, cap_for[rid])
        man_rows[rid] = dict(capture=cap_for[rid], url=urls[rid], http_status=200,
                             fetched_at='2026-11-05T09:00:00-03:00',
                             sha256=hashlib.sha256(open(cap, 'rb').read()).hexdigest(),
                             quote=f'prayer address petition votive promise fixed extempore efficacy register case')
    if man_rows_quote_override:
        man_rows[man_rows_quote_override[0]]['quote'] = man_rows_quote_override[1]
    if attack == 'V9':
        capdata = open(base, 'rb').read()
        rel = 'reports/round-90/evidence/S955.txt'
        with open(os.path.join(root, rel), 'wb') as f:
            f.write(capdata)
        man_rows['S955'] = dict(capture=rel, url=urls['S955'], http_status=200,
                                fetched_at='2026-11-05T09:00:00-03:00',
                                sha256=hashlib.sha256(capdata).hexdigest(),
                                quote='an old base row about prayer notes and rubrics')
        lesson_text2 = lesson_text.replace(
            '\u201cprayer address petition votive promise fixed extempore efficacy register case 0\u201d',
            '\u201can old base row about prayer notes and rubrics\u201d')
        with open(lesson, 'w') as f:
            f.write(lesson_text2)
    man = os.path.join(root, 'manifest.json')
    with open(man, 'w') as f:
        json.dump({'rows': man_rows}, f, indent=1)
    return dict(root=root, base=base, lands=lands, lesson=lesson, entry=entry,
                manifest=man, base_lesson=base_lesson)


def run_tool(tool, t, args_set, fixture):
    a = ['--root', fixture['root'], 'entry',
         '--entry', fixture['entry'],
         '--base-registry', fixture['base'],
         '--lands-registry', fixture['lands'],
         '--lesson', fixture['lesson'],
         '--manifest', fixture['manifest'],
         '--capture-dir', 'reports/round-90/evidence',
         '--as-of', '2026-11-05',
         '--topic', TOPIC,
         '--topic-phrases', PHRASES,
         '--min-topic-phrases', '4',
         '--min-bytes', '1200',
         '--min-headings', '4',
         '--min-new-ids', '3',
         '--min-topic-overlap', '8',
         '--table-min-rows', '5',
         '--table-min-cols', '3',
         '--base-lesson', fixture['base_lesson'],
         '--graded', 'corpus/SOURCES.md',
         '--graded', 'lesson.md']
    if args_set == 'B':
        a += ['--min-anchor-span', '3', '--min-gate-overlap', '3']
    r = subprocess.run([sys.executable, '-B', tool] + a, capture_output=True, text=True)
    out = ((r.stdout or '') + (r.stderr or '')).strip().splitlines()
    verdict = out[-1] if out else 'no output'
    return r.returncode, verdict, '\n'.join(out)


ATTACKS = [
    ('V10a', 'APPENDONLY'),
    ('V10c', 'APPENDONLY'),
    ('V3', 'UNIQUENESS'),
    ('V12', 'CAPTURE'),
    ('V7', 'GATE'),
    ('V2', 'TOPIC'),
    ('V9', 'CAPTURE'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work', required=True)
    ap.add_argument('--tool', action='append', default=[],
                    help='name=path; e.g. --tool v2=/path/to/base-tool.py --tool v3=tools/check-advance-evidence.py')
    args = ap.parse_args()
    tools = {}
    for pair in args.tool:
        n, p = pair.split('=', 1)
        tools[n] = p
    fixtures = {}
    for name, _leg in ATTACKS:
        fixtures[name] = build_tree(args.work, name, name)
    g0 = build_tree(args.work, 'G0', None)

    before, before_ok = [], True
    for name, leg in ATTACKS:
        rc, verdict, _full = run_tool(tools['v2'], 'v2', 'A', fixtures[name])
        passed = rc == 0
        before_ok &= passed
        before.append(f'{name}: v2 rc={rc} {verdict}')
    rc, verdict, _ = run_tool(tools['v2'], 'v2', 'A', g0)
    before.append(f'G0: v2 rc={rc} {verdict}')
    before_ok &= rc == 0
    before_txt = ('# before-receipt: the base grader (v2) passes all seven routed counterfeit '
                  'landings and the compliant control (args set A, identical command for both tools)\n'
                  '# defects present = the round-91 CriticClaims91 survivors\n'
                  + '\n'.join(before) + '\n'
                  + f'BEFORE-V2-DEFECT-PRESENT: {"yes" if before_ok else "no"} (7/7 counterfeits pass rc 0, G0 passes)\n')
    with open(os.path.join(args.work, 'before-v2-counterfeits.txt'), 'w') as f:
        f.write(before_txt + '\n')
    print(before_txt)

    after, after_ok = [], True
    for name, leg in ATTACKS:
        rc, verdict, full = run_tool(tools['v3'], 'v3', 'B', fixtures[name])
        named = f'FAIL {leg}' in full
        good = rc == 1 and named
        after_ok &= good
        after.append(f'{name}: v3 rc={rc} {"refused on " + leg if named else "NOT refused on " + leg} :: {verdict}')
    rc, verdict, _ = run_tool(tools['v3'], 'v3', 'B', g0)
    after.append(f'G0: v3 rc={rc} {verdict}')
    after_ok &= rc == 0
    after_txt = ('# after-receipt: the v3 grader refuses every routed counterfeit on its named leg '
                 '(args set B: the counter\'s declared floors added) and keeps the compliant control green\n'
                 + '\n'.join(after) + '\n'
                 + f'AFTER-V3-REFUSED: {"yes" if after_ok else "no"} (7/7 counterfeits rc 1 on the named leg, G0 rc 0)\n')
    with open(os.path.join(args.work, 'after-v3-refusals.txt'), 'w') as f:
        f.write(after_txt + '\n')
    print(after_txt)
    return 0 if (before_ok and after_ok) else 1


if __name__ == '__main__':
    sys.exit(main())
