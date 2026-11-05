#!/usr/bin/env python3
"""ExecBeforeBundles: build three synthetic counterfeit entry bundles and run
the frozen v1 grader (base d39434b3 bytes) and the working-tree v2 grader in
entry mode over each, mirroring the frozen counter's grade_c argument list.
Bundles are synthetic grader-discrimination fixtures, not evidence about any
real source. Writes only under the seat stage dir and this scratch dir."""
import hashlib, json, os, re, shlex, shutil, subprocess, sys, unicodedata

SCRATCH = '/fast/scratch/hyaku/kotodama-r91/ExecBeforeBundles'
STAGE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecBeforeBundles'
LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
BUNDLES = os.path.join(STAGE, 'bundles')
V1 = os.path.join(SCRATCH, 'v1', 'check-advance-evidence.py')
V2 = os.path.join(LANE, 'tools', 'check-advance-evidence.py')
BASE_SHA = 'd39434b3bc8458e1b66edd2d0d0fea9ea32f3331'
AS_OF = '2026-11-05'
FETCHED = '2026-11-05T12:00:00-03:00'
TOPIC = ('secret, ludic and anti-language registers: argot and cant as closed in-group vocabularies, '
         'anti-languages as social structure maintained through conversation, backslang and reversal games, '
         'ludling and Pig Latin style word play, in-group concealment and identity functions, and the design '
         'procedure for a fictional secret register')
PHRASES = 'argot;anti-language;backslang;ludling;cant;in-group concealment'
ENTRY_REL = 'corpus/knowledge/bakery-rota.md'
ENTRY_BASENAME = os.path.basename(ENTRY_REL)
LESSON_REL = 'corpus/lessons/round-91.md'
CAPDIR = 'reports/round-91/evidence'
SHADOW_SOURCE_URL = 'https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Ship'  # base row S900

# --- normalization helpers copied verbatim from the frozen v1 grader ---
STOP = set('''a an the and or but if of to in on at for with from by as is are was were be been being
this that these those it its their his her they we you i not no nor so than then there here which who
whom whose what when where why how all any both each few more most other some such only own same too very
can will just should now into over under about after before between during through above below out off
again further once has have had do does did doing also may might must shall would could one two three
'''.split())

def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).replace('\u2019', "'")
    s = ' '.join(s.split()).casefold()
    s = re.sub(r'\s+([.,;:!?%\)\]])', r'\1', s)
    return s

def words(s):
    return [w for w in re.findall(r"[a-z][a-z'\-]+", norm(s)) if len(w) >= 4 and w not in STOP]

def overlap(a, b):
    return len(set(words(a)) & set(words(b)))

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

# --- synthetic entry: bakery scheduling prose, deliberately carrying enough
# content words shared with the round-91 topic string to clear v1's overlap leg ---
ENTRY_TEXT = '''# Sourdough Bakery Shift Rota and Scheduling Practice

- topic: sourdough bakery shift scheduling and bench procedure
- sources: S952, S953, S954
- verified-at: 2026-11-05
- recheck: 90d

This entry documents the shift rota and scheduling practice of a mid-size sourdough bakery
as it is actually run on the bench, not as a franchise manual imagines it. The rota is the
bakery's quiet operating system: it decides who scales flour at four in the morning, who
shapes at six, who bakes at seven, and who stays for the mid-morning counter. Every
procedure below was written against a real week of production, and each one exists because
some shift once lost a morning to its absence.

## Why the rota is the load-bearing schedule

A sourdough bakery does not sell bread it forgot to schedule. The dough moves on its own
clock, and the rota exists to put human hands where the dough will need them. When the
rota slips, the visible damage is a late first bake; the invisible damage is a bench crew
that has stopped trusting the schedule and started improvising, which costs more hours
than any single late loaf. The head baker owns the rota; the rota owns the week.

Scheduling a sourdough shift starts from the levain build, backwards. The evening planner
writes the target bake time first, then works back through shaping, bulk ferment, and the
levain clock, and only then assigns names to the steps. A rota written in the other
direction, names first, always discovers at four in the morning that the person scheduled
to shape has no dough ready, and the whole structure of the day has to be rebuilt while
the oven sits hot and empty.

## The closed cant of the bench

Every long-standing bench develops its own working cant: short names for stations and
steps that outsiders find opaque. The walk-in is the vault, the proofer is the warm room,
the first bake is the early, and the scraper everyone fights over is called the widow.
The cant is not a mystique; it is a scheduling device, because a handover that says
"scaled the early, vault is full, widow needs oil" moves faster and drops fewer details
than a paragraph of plain prose would. New hires are handed a one-page glossary, and the
bench argot grows a little every season.

The bench keeps a closed list of starter addresses, one row per leaven, so no two bakers
feed the same jar under different names. The word for that list is the ledger, and the
head baker alone writes into it. That small secret of bookkeeping is the difference
between a stable house culture and a drifting one; when the ledger and the jars disagree,
the ledger wins, and the bread keeps its flavour.

## Scheduling registers and their structure

The bakery keeps three scheduling registers, and their structure has not changed in six
years. The wall register is a grid of names against tasks and holds the week. The bench
register is the working copy, a clipboard that travels with the shift and absorbs
corrections. The ledger register records what actually happened, hour by hour, and it is
the register that settles arguments. A rota change is not real until it has crossed from
the wall to the bench and survived into the ledger.

The design of the rota follows a fixed seasonal procedure. In spring the planner moves the
first bake earlier as days warm; in high summer the bulk ferment is shortened and the
night shift grows; in autumn the schedule relaxes; in winter the second mixing is pushed
to mid-morning. The procedure is reviewed every equinox at a meeting that lasts one hour
and produces at most three changes, because a rota redesigned wholesale twice a year is a
rota nobody follows.

## Address books and the social order of the shift

The address book of suppliers sits next to the flour bin, and it is scheduled work to
maintain it: every Monday the early shift confirms one page of addresses, so the whole
book is verified in a month without a single long telephone session. A dead address in
that book costs a morning; a whole dead book costs a season. The Monday procedure is
written on the book's inside cover and has outlived three head bakers.

The social order of the bench is scheduled as deliberately as the ovens. The early shift
works in near silence and the morning conversation happens at the pass, standing, over
the cooling rack, in the ten minutes after the first bake leaves the oven. That
conversation is where the day's corrections trade hands, and the rota protects it: the
shift overlap is arranged so the night crew and the morning crew meet at the pass, not in
the doorway.

## Prayer, petition and vow at the pass

The bench has its own small liturgy, half joke and half habit. A new leaven is greeted
with a prayer for a clean rise; a baker sent to beg a bag of flour from the café next
door calls it a petition and logs it in the ledger as borrowed; and the promise a closer
makes to the early shift, that the walk-in is defrosted and the bins are out, is called
the vow and is checked first thing, before the flour is scaled. None of this appears in
the franchise manual, and every functioning bakery the author has worked in kept some
version of it, because small ritual marks the handover points that plain scheduling
language blurs.

## The reversal of the proof order

Once a fortnight the planner orders a deliberate reversal of the proof order, sending the
slower doughs to the warm room first and the fast ones last. The reversal is a diagnostic:
if the bake comes out even under a reversed order, the rota's fermentation times are
still honest, and if it comes out lopsided, some clock has drifted and the schedule gets
rebuilt from the levain backwards again. The reversal week is marked on the wall register
in red so nobody is surprised by a slower morning.

## Word games on the board

The chalkboard above the sink carries the shift list, and the bench plays small word
games on it between jobs: the baker who names the daily special gets to style the board,
and on slow afternoons the crew runs naming games against the glossary, inventing a bench
word for a new tool and retiring the loser. The play is unserious and its effect is not;
a crew that names its stations precisely hands over precisely, and the handover is where
scheduling succeeds or fails.

## Weekly rota template

The template below is the wall register as it is actually drawn, one row per station and
shift, with the bench term for each task in the third column so the glossary stays alive.

| Day | Early shift task | Bench term | Handover note |
|---|---|---|---|
| Mon | Scale flour for the first bake | the four o'clock | confirm one address book page |
| Tue | Shape and load the hearth | the early | bench argot on the board, widow oiled |
| Wed | Feed and turn the levain | vault duty | ledger rows before ledger register |
| Thu | Warm-room turns on the fortnight reversal | the red week | compare proof against plan |
| Fri | First bake and counter handover | the pass talk | ten minutes, standing, at the rack |
| Sat | Deep clean and glossary review | the widow's day | retire one bench word if stale |

## Scaling the levain across shifts

The levain clock is the one schedule the rota cannot move, so the rota moves around it.
The evening shift scales the levain at nine, the night shift turns it at midnight and at
three, and the morning shift finds it ready at five thirty. Each turn is initialed on the
bench register, and a missed initial is treated as a missed turn, because a levain that
nobody admits to feeding is a levain nobody watches. The head baker reads the initials
before the first bake and adjusts the day's schedule once, in writing, if any clock has
slipped.

## Handover procedure

The handover procedure is four lines long and pinned inside the clipboard. One: read the
bench register aloud, corrections included. Two: walk the room, vault to pass, with the
incoming baker. Three: the outgoing baker names the one thing most likely to go wrong
before the next handover. Four: both sign the ledger register. The procedure takes eight
minutes and there is no shorter form of it; every attempt to compress the handover into a
text message has produced a lost morning within a month.

## Contingency: oven failure

The rota carries one contingency plan, for oven failure, and it is scheduled as a
rehearsal twice a year. The plan moves the first bake to the café's deck oven two doors
down, shifts shaping ninety minutes earlier, and reassigns the counter staff to the night
bench. The rehearsal is run cold, with chalk only, in twenty minutes; the real plan has
been needed once in six years, and the shift that ran it lost no bake because the
rehearsal had already assigned every name.

## Cleaning and close-down

Close-down is scheduled work, not a mood. The closer strips the bench, oils the widow,
defrosts the walk-in on the fortnight, and leaves the word board facing the pass for the
morning crew. The bins go out, the floor gets squeegeed, and the closer writes the vow:
one line in the ledger register naming what is ready for the morning. The early shift
checks the vow before scaling flour, and a broken vow is written into the ledger the same
way a missed bake is, without drama and without exception.

## Record-keeping and the ledger register

The ledger register is the bakery's memory, and it is scheduled into the rota like any
other task: the last fifteen minutes of every shift are ledger minutes. The keeper writes
what was planned, what happened, and what the next shift should watch, in that order,
with times. At the end of the season the ledgers are read once, and the scheduling
procedure for the next season is drafted from them, which is why the entry insists that
records are part of the rota rather than an afterthought to it.

## The flour order and the calendar

The flour order sits outside the rota but pins it. Orders land Tuesday and Friday, and
the rota assumes the Tuesday delivery is stacked by the time the early shift scales at
four; if the supplier slips, the planner moves the rye builds to Friday before anything
else, because rye is the flour the schedule misses most. The flour calendar is written
on the same wall register as the shifts, in a column of its own, so a late truck is
visible to the whole bench rather than being a private surprise of the person who opens
the door to it. The delivery column has saved more mornings than any other line the
planner keeps, and it costs one stroke of chalk per week.

Ordering is scheduled work with a procedure of its own. The early shift counts the bin
weights on Monday, the planner converts the counts into an order on Monday afternoon,
and nobody adjusts the order after Tuesday noon except the head baker, who is the only
name allowed to call in a gap. That single-name rule is written into the address book's
inside cover next to the confirmation procedure, and it has ended the old habit of two
bakers independently telephoning the mill and doubling a delivery that then sat in the
passage for a week.

## When the rota and the calendar fight

Twice a year the town calendar fights the rota: the market weekend, when the counter
doubles its staff, and the winter fair, when the first bake moves two hours earlier and
the night shift absorbs the difference. The procedure for both is written as a one-page
overlay: names are borrowed from the quiet shifts of the same week, the borrowed names
are written in the wall register margin, and the ledger register records the borrowing
so the following week's schedule can pay the hours back in rest rather than in money.
The overlay is deliberate design, not heroics, and the bench treats a fair week that
relies on improvisation as a planning failure even when the bread sells out.

## Training a new hire onto the rota

A new hire spends the first week on the early shift with one sponsor, and the sponsor's
name sits in the rota next to theirs for five days. The first three mornings are spent
only scaling and observing; the fourth morning the hire shapes under supervision; the
fifth morning the hire runs the pass talk with the sponsor standing back. The glossary
is read aloud on the first morning, bench word by bench word, and the hire keeps the
one-page version in a pocket for a month. Training is scheduled in the same register as
production, not arranged verbally in the doorway, because a training promise made in
words alone is the first casualty of a busy Friday.

## Glossary of bench terms

The glossary is reviewed on Saturday mornings and changes by one term at a time. Terms
retire when the tool or station they name disappears; terms enter when a correction
repeats three times and gets shortened into a word. The current glossary holds forty-one
terms, and the shortest, pass, names the most scheduled place in the bakery: the counter
end of the bench where every conversation, correction and handover in this entry
happens.
'''

R3 = [
    ('S952', 'Bench Rota Handbook, 2026 printing (synthetic fixture, not a source), https://fixture.example.org/rota/handbook-2026.html — counterfeit registry row built only to exercise the grader',
     'the head baker sets the levain clock by the evening shift, not by the calendar',
     'the levain is scaled at nine in the evening so the morning bench can shape by six'),
    ('S953', 'Starter Ledger of the house leavens (synthetic fixture, not a source), https://fixture.example.org/rota/starter-ledger.html — counterfeit registry row built only to exercise the grader',
     'the head baker records each retired starter in the closed ledger of addresses',
     'every retired starter keeps its own row in the ledger and no jar is fed under two names'),
    ('S954', 'Night Shift Notes of the ovens (synthetic fixture, not a source), https://fixture.example.org/rota/night-shift-notes.html — counterfeit registry row built only to exercise the grader',
     'the night crew leaves the word board facing the pass for the morning conversation',
     'the word board is left facing the pass so the morning crew can read the night notes'),
]


def entry_for_bundle():
    return ENTRY_TEXT


def make_row(rid, cite, teaches):
    return (f'| {rid} | {cite} | docs | A | scope | anchor | {teaches} | mined | {AS_OF} | 90d | {ENTRY_REL} |')


def build_bundle(name, shadow=False, selfquote=False):
    broot = os.path.join(BUNDLES, name)
    shutil.rmtree(broot, ignore_errors=True)
    for d in ('corpus/knowledge', 'corpus/lessons', os.path.join(CAPDIR)):
        os.makedirs(os.path.join(broot, d), exist_ok=True)
    base_bytes = open(os.path.join(SCRATCH, 'base-SOURCES.md'), encoding='utf-8').read()
    base_lesson_bytes = open(os.path.join(SCRATCH, 'base-lesson.md'), encoding='utf-8').read()

    rows = []
    for rid, cite, teaches, quote in R3:
        c = cite
        if shadow and rid == 'S954':
            c = cite.replace('https://fixture.example.org/rota/night-shift-notes.html', SHADOW_SOURCE_URL)
        if selfquote and rid == 'S953':
            quote = teaches  # gate quote equals the row's teaching cell text exactly
        rows.append((rid, c, teaches, quote))

    with open(os.path.join(broot, 'corpus/SOURCES.md'), 'w', encoding='utf-8') as f:
        f.write(base_bytes.rstrip('\n') + '\n' + '\n'.join(make_row(r[0], r[1], r[2]) for r in rows) + '\n')
    with open(os.path.join(broot, ENTRY_REL), 'w', encoding='utf-8') as f:
        f.write(entry_for_bundle())

    lesson = ['# Round 91 gates (synthetic counterfeit fixture — not lane evidence)', '']
    for rid, cite, teaches, quote in rows:
        url = re.search(r'https?://[^\s|)]+', cite).group(0)
        lesson.append(f'- {rid} LOCATED — “{quote}” — {url} accessed {AS_OF}, section 2; '
                      f'synthetic fixture quote located in the committed capture file.')
    with open(os.path.join(broot, LESSON_REL), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lesson) + '\n')

    manifest_rows = {}
    for rid, cite, teaches, quote in rows:
        cap_rel = f'{CAPDIR}/{rid}.txt'
        body = (f'Synthetic capture fixture for grader discrimination; this file is not evidence '
                f'about any real source.\nBench note, {AS_OF}.\n\n'
                f'{quote}\n\nFurther synthetic padding follows so the capture is not a single line.\n'
                f'The rota procedure continues in the handbook the fixture pretends to summarize.\n')
        p = os.path.join(broot, cap_rel)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(body)
        manifest_rows[rid] = {
            'capture': cap_rel,
            'sha256': hashlib.sha256(body.encode()).hexdigest(),
            'http_status': 200,
            'fetched_at': FETCHED,
            'url': re.search(r'https?://[^\s|)]+', cite).group(0),
            'note': 'synthetic counterfeit fixture, built by seat ExecBeforeBundles on 2026-11-05',
        }
    with open(os.path.join(broot, CAPDIR, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump({'rows': manifest_rows}, f, indent=1)
    return broot


def precheck():
    entry = entry_for_bundle()
    problems = []
    if len(entry.encode()) < 12000:
        problems.append(f'entry {len(entry.encode())}B < 12000')
    heads = [l for l in entry.splitlines() if l.startswith('## ')]
    if len(heads) < 6:
        problems.append(f'{len(heads)} h2 < 6')
    for key in ('- topic:', '- sources:', '- verified-at:', '- recheck:'):
        if key not in entry:
            problems.append(f'header key {key} absent')
    r, c = table_shape(entry)
    if r < 5 or c < 3:
        problems.append(f'table {r}x{c} < 5x3')
    ss = sentences(entry)
    worst = max([ss.count(s) for s in set(ss)] or [0])
    if worst > 2:
        problems.append(f'sentence repeats {worst}x')
    shared = overlap(entry, TOPIC)
    if shared < 10:
        problems.append(f'overlap {shared} < 10')
    stem_hits = sum(1 for w in ('bakery', 'rota') if norm(w) in norm(entry))
    if stem_hits != 2:
        problems.append('filename stems absent')
    cited = sorted(set(re.findall(r'\bS\d{3,}\b', entry)))
    if cited != ['S952', 'S953', 'S954']:
        problems.append(f'cited ids {cited}')
    phrase_anchor = norm(' '.join(heads)) + ' ' + norm('\n'.join(
        l for l in entry.splitlines() if l.strip().startswith('|')))
    hits = [p for p in PHRASES.split(';') if norm(p) in phrase_anchor]
    return problems, dict(bytes=len(entry.encode()), h2=len(heads), table=f'{r}x{c}',
                          overlap=shared, worst_repeat=worst, cited=cited,
                          v2_phrase_anchors=hits)


def run(label, argv):
    r = subprocess.run(argv, capture_output=True, text=True, cwd=SCRATCH)
    return {'label': label, 'cmd': shlex.join(argv), 'stdout': r.stdout, 'stderr': r.stderr,
            'rc': r.returncode}


def main():
    os.environ['TMPDIR'] = SCRATCH
    problems, facts = precheck()
    print('PRECHECK:', 'clean' if not problems else problems, json.dumps(facts))
    if problems:
        return 1
    results = []
    bundle_cfg = [('bundle-bakery', {}), ('bundle-shadow', {'shadow': True}),
                  ('bundle-selfquote', {'selfquote': True})]
    for name, kw in bundle_cfg:
        broot = build_bundle(name, **kw)
        entry_abs = os.path.join(broot, ENTRY_REL)
        lesson_abs = os.path.join(broot, LESSON_REL)
        lands_abs = os.path.join(broot, 'corpus/SOURCES.md')
        man_abs = os.path.join(broot, CAPDIR, 'manifest.json')
        base_reg_abs = os.path.join(SCRATCH, 'base-SOURCES.md')
        base_lesson_abs = os.path.join(SCRATCH, 'base-lesson.md')
        common = ['entry', '--root', broot, '--entry', entry_abs,
                  '--base-registry', base_reg_abs, '--lands-registry', lands_abs,
                  '--lesson', lesson_abs, '--manifest', man_abs,
                  '--capture-dir', CAPDIR, '--as-of', AS_OF, '--topic', TOPIC,
                  '--min-bytes', '12000', '--min-headings', '6', '--min-new-ids', '3',
                  '--min-topic-overlap', '10', '--table-min-rows', '5', '--table-min-cols', '3',
                  '--graded', 'corpus/SOURCES.md', '--graded', LESSON_REL]
        results.append(run(f'v1 x {name}', [sys.executable, '-B', V1] + common))
        v2_extra = ['--topic-phrases', PHRASES, '--min-topic-phrases', '4',
                    '--base-lesson', base_lesson_abs]
        # grade_c ordering: the three extras sit right after the --topic value
        v2argv = [sys.executable, '-B', V2] + common[:19] + v2_extra + common[19:]
        results.append(run(f'v2 x {name}', v2argv))
    out = ['# ExecBeforeBundles — BEFORE state of claim O, entry mode, frozen v1 vs working-tree v2',
           f'date: 2026-11-05; lane repo: {LANE}; base: {BASE_SHA}',
           '',
           '## Grader bytes',
           f'$ git -C {LANE} show {BASE_SHA}:tools/check-advance-evidence.py > {V1}   (rc 0)',
           '$ sha256sum <v1 bytes> <lane>/tools/check-advance-evidence.py',
           f'121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed  {V1}',
           f'88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093  {V2}',
           '',
           f'PRECHECK of the synthetic entry: {json.dumps(facts)}',
           '',
           '## Runs — argv mirrors reports/round-91/measure91.py grade_c;',
           '## v1 drops --topic-phrases --min-topic-phrases --base-lesson (its CLI lacks them).', '']
    for res in results:
        out.append(f'### {res["label"]}  rc={res["rc"]}')
        out.append('$ ' + res['cmd'])
        out.append('[stdout]')
        out.append(res['stdout'].rstrip('\n'))
        if res['stderr'].strip():
            out.append('[stderr]')
            out.append(res['stderr'].rstrip('\n'))
        out.append('')
    path = os.path.join(STAGE, 'before-bundles.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('WROTE', path)
    for res in results:
        legs = [l for l in res['stdout'].splitlines() if l.startswith('LEG ')]
        verdict = res['stdout'].strip().splitlines()[-1] if res['stdout'].strip() else 'no output'
        print(f'{res["label"]}: rc={res["rc"]} verdict={verdict}')
        for l in legs:
            print('   ', l)
    return 0


if __name__ == '__main__':
    sys.exit(main())
