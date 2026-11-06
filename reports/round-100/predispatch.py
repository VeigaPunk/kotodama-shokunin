#!/usr/bin/env python3
"""Round-100 pre-dispatch counter (frozen in the freeze commit before any seat runs; the round's
claims O and C are judged on it).

Usage:
  python3 -B reports/round-100/predispatch.py --root <tree> --work <scratch> --base-rev <40hex>

Legs (exit 0 iff every leg prints PASS):

  O0  tools/check-table-support.py exists (absent at base); its sha256 is printed
  O1  selftest: `--selftest --work <dir>` rc 0, line `SELFTEST PASS N/N` with N >= 24
  O2  battery100 (reports/round-100/controls/battery100.py, freeze-committed):
      `BATTERY-SUMMARY cases=28 pass=28 fail=0 traceback=0`, rc 0. Pin binding: the driver's
      sha256 must equal reports/round-100/controls/battery100.sha256 AND the `BATTERY-SHA256`
      line of both control receipts (battery100-control-base.txt: TOOL-MISSING, fail;
      battery100-feasibility.txt: the L1 feasibility reference, pass=28). Fails closed when any
      of the three is missing.
  O3  historical replay of lesson R99-M2 on real lane bytes: run the tool (--json) on the tree's
      praise entry and on a scratch copy whose `| Yoruba |` row has its LAST cell replaced by the
      round-99 attempt-1 text (R99M2_CELL), both with --root <tree> and one --evidence per
      existing reports/round-*/evidence dir (sorted). PASS iff the forged run's rc == 1 and the
      finding-key sets differ by exactly {(UNSUPPORTED-CELL, Yoruba, <last header cell>)}
      (forged minus actual) and nothing else (actual minus forged empty). Keys as in battery100.
  O4  mutation100: `MUTATION-SCORE: <k>/<t> killed, 0 survived, 0 broken-pattern`, k == t,
      t >= 20. Pin binding: driver sha256 == reports/round-100/controls/mutants100.sha256 ==
      `DRIVER-SHA256` line of reports/round-100/controls/mutation100-first.txt.
  O5  capability registration: SCORECARD.md has a table row naming `check-table-support.py`
      below a `## Capabilities` heading line, and SKILL.md names `check-table-support.py`.
  C1  entry `corpus/knowledge/linguistics/work-song-labour-chant.md` present; >= 12000 B;
      >= 6 h2; one table with >= 5 data rows x >= 3 cols; >= 4 of the six frozen phrases in h2
      headings or table data rows; the `- topic:` line byte-equal to the frozen topic
  C2  registry: >= 945 rows; highest id >= S1021; >= 4 new rows (id above S1017) with tier A|B,
      status mined, opened 2026-11-06 or 2026-11-07, used-by exactly the entry path
  C3  append-only registry per CORPUS.md rule 2 (only status, recheck and used-by may change in
      place; any other removed base line fails)
  C4  census: sources-census.sh validate --file <root>/corpus/SOURCES.md rc 0
  C5  index: tools/check-corpus-index.py --root <root> rc 0
  C6  every qualifying new id from C2 is cited inside the entry text
  C7  evidence binding in reports/round-100/evidence/manifest.json (JSON list): capture sha256s
      match, quote 1..25 words occurring exactly once (whitespace-collapsed) in quote_capture,
      quote inside the registry row's anchor cell
  C8  content sweep: knowledge files OTHER than the entry whose `- topic:` line or any heading
      carries a frozen phrase; PASS iff 0 (guard leg; passes on base by construction)
  C9  non-author re-open: .ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json names >= 3
      distinct qualifying ids, each http 200, quote_count 1, 64-hex fresh_sha256, url occurring
      in that id's registry source cell
"""

import argparse
import difflib
import json
import hashlib
import io
import os
import re
import subprocess
import sys

ENTRY_REL = 'corpus/knowledge/linguistics/work-song-labour-chant.md'
FROZEN_TOPIC = ('work song and labour chant: song that times and coordinates shared labour — the song '
                'leader\'s call and the crew\'s response; hauling, rowing, pounding, field and craft songs and '
                'how their rhythm fits the task; the shanty and other occupational repertories; improvised '
                'verses, complaint and satire licensed by the work; and the design procedure for a fictional '
                'work-song tradition whose songs stay tied to their task, crew, leader and setting')
PHRASES = ['work song', 'call and response', 'song leader', 'shanty', 'hauling song', 'work rhythm']
TOOL_REL = 'tools/check-table-support.py'
SELFTEST_FLOOR = 24
BATTERY_DRIVER = 'reports/round-100/controls/battery100.py'
BATTERY_PIN = 'reports/round-100/controls/battery100.sha256'
BATTERY_CONTROLS = ('reports/round-100/controls/battery100-control-base.txt',
                    'reports/round-100/controls/battery100-feasibility.txt')
BATTERY_CASES = 28
MUTATION_DRIVER = '.ufo/waves/round-100/w1/stage/MutationTester100/mutants100.py'
MUTATION_PIN = 'reports/round-100/controls/mutants100.sha256'
MUTATION_FIRST = 'reports/round-100/controls/mutation100-first.txt'
MUTATION_FLOOR = 20
PRAISE_REL = 'corpus/knowledge/linguistics/praise-poetry-panegyric.md'
R99M2_CELL = 'titles are public property, so any drummer who knows them can assemble the praise'
NEW_ROW_MIN = 4
ROW_MIN, ROWS_MIN = 3, 5
BASE_HIGHEST = 1017
ROWS_MIN_AFTER = 945
HIGHEST_MIN_AFTER = 1021
OPENED_OK = ('2026-11-06', '2026-11-07')
EVIDENCE_DIR = 'reports/round-100/evidence'
CENSUS = '/home/vgpnk/Projects/shokunin/scripts/sources-census.sh'
REOPEN = '.ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json'
REOPEN_MIN = 3

RES = []


def leg(name, ok, detail):
    RES.append(bool(ok))
    print(f'LEG {name} {"PASS" if ok else "FAIL"} {detail}')
    return ok


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def run(cmd, **kw):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, **kw)
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(cmd, 124, '', 'timeout')


def sha_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def pin_value(p):
    try:
        toks = open(p, encoding='utf-8').read().split()
    except OSError:
        return None
    return toks[0] if toks and re.fullmatch(r'[0-9a-f]{64}', toks[0]) else None


def receipt_value(p, key):
    try:
        text = open(p, encoding='utf-8').read()
    except OSError:
        return None, ''
    m = re.search(r'^' + re.escape(key) + r' ([0-9a-f]{64})\s*$', text, re.M)
    return (m.group(1) if m else None), text


def sweep_owners(files_text, phrases, exclude=()):
    """files_text: {relpath: text}. Return sorted relpaths (not in exclude) whose `- topic:` line
    or any markdown heading carries a phrase (norm containment). Prose and table cells are
    mentions, not ownership, and are not scanned."""
    owners = []
    nph = [norm(p) for p in phrases]
    for rel, text in files_text.items():
        if rel in exclude:
            continue
        surf = [norm(l.strip()) for l in text.splitlines()
                if l.strip().startswith('- topic:') or re.match(r'^#{1,6}\s', l.strip())]
        if any(p in t for p in nph for t in surf):
            owners.append(rel)
    return sorted(owners)


def tree_knowledge(root):
    out = {}
    kd = os.path.join(root, 'corpus/knowledge')
    for d, _, fs in os.walk(kd):
        for f in fs:
            if f.endswith('.md'):
                p = os.path.join(d, f)
                out[os.path.relpath(p, root)] = open(p, encoding='utf-8', errors='replace').read()
    return out


def tool_json(tool, entry, root, evdirs):
    args = [sys.executable, '-B', tool, '--entry', entry, '--root', root, '--json']
    for d in evdirs:
        args += ['--evidence', d]
    p = run(args, timeout=300)
    try:
        js = json.loads(p.stdout)
        keys = set()
        for f in js['findings']:
            i = f.get('id')
            if i in ('UNSUPPORTED-CELL', 'UNBOUND-ROW'):
                keys.add((i, f.get('row'), f.get('col', '') if i == 'UNSUPPORTED-CELL' else ''))
            elif i == 'NO-CAPTURE':
                keys.add((i, f.get('sid'), ''))
            elif i == 'NO-PATH':
                keys.add((i, f.get('path'), ''))
            else:
                keys.add((str(i), '?', '?'))
        return p.returncode, keys, None
    except Exception as e:
        return p.returncode, None, f'unparseable ({type(e).__name__}) stderr={p.stderr[-160:]!r}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--base-rev', required=True)
    ap.add_argument('--base-registry', default=None,
                    help='file with base corpus/SOURCES.md bytes when --root is not a git work tree')
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    work = os.path.abspath(a.work)
    if not os.path.isdir(work):
        print(f'REFUSED --work must be an existing directory: {work}')
        return 2
    if os.path.realpath(work).startswith('/tmp'):
        print(f'REFUSED --work must not live under /tmp: {work}')
        return 2
    if not os.path.isdir(root):
        print(f'REFUSED --root must be an existing directory: {root}')
        return 2

    tool = os.path.join(root, TOOL_REL)

    # O0 tool presence
    sha = sha_file(tool) if os.path.isfile(tool) else None
    leg('O0', sha is not None, f'tool-sha256 {sha}' if sha else f'tool missing: {TOOL_REL}')

    # O1 selftest
    ok, detail = False, 'selftest not run (tool missing)'
    if sha:
        d = os.path.join(work, 'selftest')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', tool, '--selftest', '--work', d], timeout=600)
        m = re.search(r'SELFTEST PASS (\d+)/(\d+)', p.stdout)
        if p.returncode == 0 and m and m.group(1) == m.group(2) and int(m.group(1)) >= SELFTEST_FLOOR:
            ok = True
            detail = f'{m.group(1)}/{m.group(2)} floor={SELFTEST_FLOOR} rc=0'
        else:
            detail = (f'rc={p.returncode} '
                      + (f'{m.group(1)}/{m.group(2)} floor={SELFTEST_FLOOR}' if m else 'no SELFTEST PASS line'))
    leg('O1', ok, detail)

    # O2 battery100 (pinned, receipt-bound)
    bdrv = os.path.join(root, BATTERY_DRIVER)
    pin = pin_value(os.path.join(root, BATTERY_PIN))
    rshas = [receipt_value(os.path.join(root, r), 'BATTERY-SHA256')[0] for r in BATTERY_CONTROLS]
    ok, detail = False, ''
    if not os.path.isfile(bdrv):
        detail = f'driver missing: {BATTERY_DRIVER}'
    elif pin is None:
        detail = f'sha pin missing or malformed: {BATTERY_PIN}'
    elif any(r is None for r in rshas):
        detail = f'control receipt missing or lacks BATTERY-SHA256: {BATTERY_CONTROLS}'
    elif not all(sha_file(bdrv) == pin == r for r in rshas):
        detail = f'battery sha {sha_file(bdrv)} pin {pin} receipts {rshas} not all equal'
    elif not sha:
        detail = 'tool missing'
    else:
        d = os.path.join(work, 'battery')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', bdrv, '--tool', tool, '--work', d], timeout=900)
        m = re.search(r'BATTERY-SUMMARY cases=(\d+) pass=(\d+) fail=(\d+) traceback=(\d+)', p.stdout)
        if m:
            n, ps, f, tb = map(int, m.groups())
            ok = p.returncode == 0 and n == BATTERY_CASES and ps == n and f == 0 and tb == 0
            fails = [l.split()[1] for l in p.stdout.splitlines() if l.startswith('CASE ') and ' FAIL ' in l]
            detail = f'cases={n} pass={ps} fail={f} traceback={tb} rc={p.returncode} failing={fails[:8]}'
        else:
            detail = f'no BATTERY-SUMMARY line rc={p.returncode}'
    leg('O2', ok, detail)

    # O3 historical replay of R99-M2 on real bytes
    ok, detail = False, ''
    pe = os.path.join(root, PRAISE_REL)
    evdirs = sorted(os.path.join(root, 'reports', d, 'evidence') for d in os.listdir(os.path.join(root, 'reports'))
                    if re.fullmatch(r'round-\d+', d) and os.path.isdir(os.path.join(root, 'reports', d, 'evidence'))) \
        if os.path.isdir(os.path.join(root, 'reports')) else []
    if not sha:
        detail = 'tool missing'
    elif not os.path.isfile(pe):
        detail = f'praise entry missing: {PRAISE_REL}'
    else:
        txt = open(pe, encoding='utf-8').read().split('\n')
        yi = [i for i, l in enumerate(txt) if re.match(r'^\|\s*Yoruba\s*\|', l)]
        hdr = None
        if len(yi) == 1:
            j = yi[0]
            while j > 0 and txt[j - 1].strip().startswith('|'):
                j -= 1
            hdr = [c.strip() for c in txt[j].strip().strip('|').split('|')]
            cs = txt[yi[0]].split('|')
            cs[-2] = ' ' + R99M2_CELL + ' '
            txt[yi[0]] = '|'.join(cs)
        if hdr is None:
            detail = f'Yoruba row not found exactly once (found {len(yi)})'
        else:
            fp = os.path.join(work, 'r99m2-forged.md')
            open(fp, 'w', encoding='utf-8').write('\n'.join(txt))
            rc_a, ka, ea = tool_json(tool, pe, root, evdirs)
            rc_f, kf, ef = tool_json(tool, fp, root, evdirs)
            want = {('UNSUPPORTED-CELL', 'Yoruba', hdr[-1])}
            if ka is None or kf is None:
                detail = f'tool output unparseable actual={ea} forged={ef}'
            else:
                ok = rc_f == 1 and (kf - ka) == want and not (ka - kf)
                detail = (f'actual rc={rc_a} findings={len(ka)}; forged rc={rc_f} findings={len(kf)}; '
                          f'forged-minus-actual={sorted(kf - ka)} actual-minus-forged={sorted(ka - kf)} '
                          f'evidence-dirs={len(evdirs)}')
    leg('O3', ok, detail)

    # O4 mutation100 (pinned, first-receipt-bound)
    mdrv = os.path.join(root, MUTATION_DRIVER)
    mpin = pin_value(os.path.join(root, MUTATION_PIN))
    fsha, _ = receipt_value(os.path.join(root, MUTATION_FIRST), 'DRIVER-SHA256')
    ok, detail = False, ''
    if not os.path.isfile(mdrv):
        detail = f'driver missing: {MUTATION_DRIVER}'
    elif mpin is None:
        detail = f'sha pin missing or malformed: {MUTATION_PIN}'
    elif fsha is None:
        detail = f'first-measurement receipt missing or lacks DRIVER-SHA256: {MUTATION_FIRST}'
    elif not (sha_file(mdrv) == mpin == fsha):
        detail = f'mutants100 sha {sha_file(mdrv)} pin {mpin} first-receipt {fsha} not all equal'
    elif not sha:
        detail = 'tool missing'
    else:
        d = os.path.join(work, 'mutation')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', mdrv, '--tool', tool, '--work', d], timeout=3000)
        m = re.search(r'MUTATION-SCORE: (\d+)/(\d+) killed, (\d+) survived, (\d+) broken-pattern', p.stdout)
        if m:
            k, t, sv, bp = map(int, m.groups())
            ok = k == t and sv == 0 and bp == 0 and t >= MUTATION_FLOOR
            detail = f'{k}/{t} killed, {sv} survived, {bp} broken-pattern (floor total {MUTATION_FLOOR}) rc={p.returncode}'
        else:
            detail = f'no MUTATION-SCORE line, rc={p.returncode}'
    leg('O4', ok, detail)

    # O5 capability registration
    ok, detail = False, ''
    sc = os.path.join(root, 'SCORECARD.md')
    sk = os.path.join(root, 'SKILL.md')
    if os.path.isfile(sc) and os.path.isfile(sk):
        in_cap, rows = False, 0
        for l in open(sc, encoding='utf-8', errors='replace'):
            if l.startswith('## '):
                in_cap = l.startswith('## Capabilities')
            elif in_cap and l.lstrip().startswith('|') and 'check-table-support.py' in l:
                rows += 1
        skn = open(sk, encoding='utf-8', errors='replace').read().count('check-table-support.py')
        ok = rows >= 1 and skn >= 1
        detail = f'scorecard-capability-rows={rows} skill-mentions={skn}'
    else:
        detail = 'SCORECARD.md or SKILL.md missing'
    leg('O5', ok, detail)

    # C1 entry
    entry_p = os.path.join(root, ENTRY_REL)
    ok, detail, entry_text = False, '', ''
    if not os.path.isfile(entry_p):
        detail = 'entry absent'
    else:
        raw = open(entry_p, encoding='utf-8').read()
        entry_text = raw
        size = len(raw.encode('utf-8'))
        heads = [l for l in raw.splitlines() if l.startswith('## ')]
        best = (0, 0)
        rows, cols, sep = 0, 0, False
        table_rows = []
        for l in raw.splitlines():
            s = l.strip()
            if not s.startswith('|'):
                sep = False
                rows = 0
                continue
            if re.match(r'^\|[\s:\-|]+\|$', s):
                sep = True
                rows = 0
                continue
            c = len(s.strip('|').split('|'))
            if sep:
                rows += 1
                cols = c
                best = max(best, (rows, cols))
                table_rows.append(norm(l))
        anchor_heads = ' '.join(norm(h) for h in heads)
        hits = [p for p in PHRASES if norm(p) in anchor_heads or any(norm(p) in t for t in table_rows)]
        tline = next((l for l in raw.splitlines() if l.strip().startswith('- topic:')), '')
        tline_ok = tline == ('- topic: ' + FROZEN_TOPIC)
        r, c = best
        if (size >= 12000 and len(heads) >= 6 and r >= ROWS_MIN and c >= ROW_MIN
                and len(hits) >= 4 and tline_ok):
            ok = True
        detail = (f'bytes={size} h2={len(heads)} table={r}x{c} phrases={len(hits)}/{len(PHRASES)} '
                  f'topic-line={"equal" if tline_ok else "differ"}')
    leg('C1', ok, detail)

    # C2 registry
    reg_p = os.path.join(root, 'corpus/SOURCES.md')
    ok, detail = False, ''
    rows_by_id, good = {}, []
    if not os.path.isfile(reg_p):
        detail = 'registry missing'
    else:
        for line in open(reg_p, encoding='utf-8'):
            if re.match(r'^ {0,3}\|\s*S[0-9]{3,}\s*\|', line):
                cells = [x.strip() for x in line.strip().strip('|').split('|')]
                if len(cells) == 11:
                    rows_by_id[cells[0]] = cells
        if not rows_by_id:
            detail = 'no registry rows parsed'
        else:
            ids = sorted(rows_by_id, key=lambda x: int(x[1:]))
            highest = ids[-1]
            new = [i for i in ids if int(i[1:]) > BASE_HIGHEST]
            for i in new:
                c = rows_by_id[i]
                if (c[3] in ('A', 'B') and c[7] == 'mined' and c[8] in OPENED_OK
                        and c[10] == ENTRY_REL):
                    good.append(i)
            if (len(ids) >= ROWS_MIN_AFTER and int(highest[1:]) >= HIGHEST_MIN_AFTER
                    and len(good) >= NEW_ROW_MIN):
                ok = True
            detail = (f'rows={len(ids)} highest={highest} new={len(new)} qualifying={len(good)} '
                      f'(min rows {ROWS_MIN_AFTER}, highest >= S{HIGHEST_MIN_AFTER}, qualifying >= {NEW_ROW_MIN})')
    leg('C2', ok, detail)

    # C3 append-only
    ok, detail = False, ''
    reg_bytes = open(reg_p, 'rb').read() if os.path.isfile(reg_p) else None
    base_bytes = None
    if reg_bytes is None:
        detail = 'registry missing'
    else:
        p = subprocess.run(['git', '-C', root, 'rev-parse', '--git-dir'], capture_output=True, text=True)
        if p.returncode == 0:
            b = subprocess.run(['git', '-C', root, 'show', f'{a.base_rev}:corpus/SOURCES.md'],
                               capture_output=True)
            if b.returncode == 0:
                base_bytes = b.stdout
            else:
                detail = f'git show base failed rc={b.returncode}'
        elif a.base_registry and os.path.isfile(a.base_registry):
            base_bytes = open(a.base_registry, 'rb').read()
        else:
            detail = 'no git tree and no --base-registry; append-only leg refused'
    if reg_bytes is not None and base_bytes is not None:
        base_lines = io.StringIO(base_bytes.decode('utf-8', errors='replace')).readlines()
        land_lines = io.StringIO(reg_bytes.decode('utf-8', errors='replace')).readlines()
        sm = difflib.SequenceMatcher(a=base_lines, b=land_lines, autojunk=False)
        removed_lines = [l for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('delete', 'replace')
                         for l in base_lines[i1:i2]]
        added = sum(j2 - j1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('insert', 'replace'))

        def cells_of(line):
            if not re.match(r'^ {0,3}\|\s*S[0-9]{3,}\s*\|', line):
                return None
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            return c if len(c) == 11 else None

        landed_rows = {}
        for l in land_lines:
            c = cells_of(l)
            if c:
                landed_rows.setdefault(c[0], []).append(c)
        allowed, illegal = 0, []
        for l in removed_lines:
            c = cells_of(l)
            fixed = (0, 1, 2, 3, 4, 5, 6, 8)
            if c and any(all(n[k] == c[k] for k in fixed) for n in landed_rows.get(c[0], [])):
                allowed += 1
            else:
                illegal.append((c[0] if c else l[:40].strip()))
        ok = not illegal
        detail = (f'added={added} removed={len(removed_lines)} in-place-status/recheck/used-by={allowed} '
                  f'illegal={len(illegal)} {illegal[:5]}')
    leg('C3', ok, detail)

    # C4 census
    p = run(['bash', CENSUS, 'validate', '--file', os.path.join(root, 'corpus/SOURCES.md')])
    leg('C4', p.returncode == 0, f'census rc={p.returncode}')

    # C5 index
    idx = os.path.join(root, 'tools/check-corpus-index.py')
    if os.path.isfile(idx):
        p = run([sys.executable, '-B', idx, '--root', root])
        last = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ''
        leg('C5', p.returncode == 0, f'index rc={p.returncode} last: {last[:100]}')
    else:
        leg('C5', False, 'index tool missing: tools/check-corpus-index.py')

    # C6 cited in entry
    if entry_text and good:
        uncited = [i for i in good if not re.search(r'\b' + i + r'\b', entry_text)]
        leg('C6', not uncited, f'qualifying ids cited in entry: {len(good) - len(uncited)}/{len(good)} uncited={uncited}')
    else:
        leg('C6', False, 'entry or qualifying rows absent')

    # C7 evidence binding (manifest, capture hashes, quote count, anchor cell)
    ev = os.path.join(root, EVIDENCE_DIR)
    mp = os.path.join(ev, 'manifest.json')

    def ws(s):
        return re.sub(r'\s+', ' ', s).strip()

    if not good:
        leg('C7', False, 'no qualifying rows')
    elif not os.path.isfile(mp):
        leg('C7', False, f'manifest missing: {EVIDENCE_DIR}/manifest.json')
    else:
        try:
            man = json.load(open(mp, encoding='utf-8'))
        except (OSError, ValueError) as e:
            man = None
            leg('C7', False, f'manifest unreadable: {type(e).__name__}')
        if man is not None:
            byid = {}
            if isinstance(man, list):
                for e in man:
                    if isinstance(e, dict) and isinstance(e.get('id'), str):
                        byid.setdefault(e['id'], e)
            fails, ncap = [], 0
            for i in good:
                e = byid.get(i)
                if e is None:
                    fails.append(f'{i}:no-manifest-entry')
                    continue
                caps = e.get('captures')
                if not isinstance(caps, list) or not caps:
                    fails.append(f'{i}:no-captures')
                    continue
                capbad = False
                for cp in caps:
                    f = cp.get('file') if isinstance(cp, dict) else None
                    fp = os.path.join(ev, f) if isinstance(f, str) and '/' not in f else None
                    if not fp or not os.path.isfile(fp) or sha_file(fp) != cp.get('sha256'):
                        capbad = True
                    else:
                        ncap += 1
                if capbad:
                    fails.append(f'{i}:capture-sha')
                    continue
                q, qc = e.get('quote'), e.get('quote_capture')
                if not (isinstance(q, str) and isinstance(qc, str) and '/' not in qc
                        and os.path.isfile(os.path.join(ev, qc))):
                    fails.append(f'{i}:no-quote-capture')
                    continue
                if not (1 <= len(q.split()) <= 25):
                    fails.append(f'{i}:quote-words={len(q.split())}')
                    continue
                txt = ws(open(os.path.join(ev, qc), encoding='utf-8', errors='replace').read())
                cnt = txt.count(ws(q))
                if cnt != 1:
                    fails.append(f'{i}:quote-count={cnt}')
                    continue
                if ws(q) not in ws(rows_by_id[i][5]):
                    fails.append(f'{i}:quote-not-in-anchor')
            leg('C7', not fails, f'qualifying ids bound: {len(good) - len(fails)}/{len(good)} '
                                 f'captures-verified={ncap} failures={fails[:6]}')

    # C8 content sweep (no other owner of the frozen phrases)
    kfiles = tree_knowledge(root)
    if not kfiles:
        leg('C8', False, 'no knowledge files found')
    else:
        owners = sweep_owners(kfiles, PHRASES, exclude=(ENTRY_REL,))
        leg('C8', not owners, f'files scanned={len(kfiles)} other owners={len(owners)} {owners[:5]}')

    # C9 non-author re-open of qualifying rows
    rp = os.path.join(root, REOPEN)
    ok, detail = False, ''
    if not good:
        detail = 'no qualifying rows'
    elif not os.path.isfile(rp):
        detail = f'reopen file missing: {REOPEN}'
    else:
        try:
            ro = json.load(open(rp, encoding='utf-8'))
        except (OSError, ValueError) as e:
            ro = None
            detail = f'reopen file unreadable: {type(e).__name__}'
        if ro is not None:
            okids = set()
            for e in (ro if isinstance(ro, list) else []):
                if not isinstance(e, dict):
                    continue
                i, u = e.get('id'), e.get('url')
                if (i in good and isinstance(u, str) and u and u in rows_by_id[i][1]
                        and e.get('http') == 200 and e.get('quote_count') == 1
                        and isinstance(e.get('fresh_sha256'), str)
                        and re.fullmatch(r'[0-9a-f]{64}', e['fresh_sha256'])):
                    okids.add(i)
            ok = len(okids) >= REOPEN_MIN
            detail = f'qualifying ids re-opened with count 1: {len(okids)} (min {REOPEN_MIN}) {sorted(okids)}'
    leg('C9', ok, detail)

    npass = sum(1 for x in RES if x)
    verdict = 'PASS' if npass == len(RES) else 'FAIL'
    print(f'PREDISPATCH-100: {verdict} legs={npass}/{len(RES)}')
    return 0 if npass == len(RES) else 1


if __name__ == '__main__':
    sys.exit(main())
