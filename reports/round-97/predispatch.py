#!/usr/bin/env python3
"""Round-97 pre-dispatch counter (frozen before any candidate is scored; the round's
claims O and C are judged on it).

Usage:
  python3 -B reports/round-97/predispatch.py --root <tree> --work <scratch> --base-rev <40hex>

Legs (exit 0 iff every leg prints PASS):

  O0  tool sha256 named; PASS only when it differs from the frozen v8 sha
      f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0
  O1  selftest: rc 0, line `SELFTEST PASS N/N`, N == N-total and N >= 154
      (v8 total 147 plus at least one pin for each of the seven round-97 classes)
  O2  battery97: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=31` and traceback=0.
      Fails closed when the stage driver, its pin or its control receipt is missing.
      Pin binding (round-96 closure routed defect 2): the driver's sha256 must equal
      reports/round-97/controls/battery97.sha256 AND the `BATTERY-SHA256 <hex>` line of
      the control receipt reports/round-97/controls/battery97-control-v8.txt, and that
      receipt must show the battery discriminating on v8: `TOOL-SHA256 <v8 sha>` and a
      summary with survivors=7 unnamed=0 refused=24.
  O3  mutation97: `MUTATION-SCORE: <killed>/<total> killed, 0 survived, 0 broken-pattern`
      with killed == total and total >= 118. Pin binding: the driver's sha256 must equal
      reports/round-97/controls/mutants97.sha256 AND the `DRIVER-SHA256 <hex>` line of the
      seat's first-measurement receipt reports/round-97/controls/mutation97-first.txt
      (a driver edited after its first measurement fails this leg).
  O4  REG regression: every line of reports/round-95/controls/reg-v5.txt occurs
      verbatim among the `REG ` lines battery97 prints over the tree's tool
  C1  entry `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` present;
      >= 12000 B; >= 6 h2; one table with >= 5 data rows x >= 3 cols; >= 4 of the six
      frozen phrases in h2 headings or table data rows; the `- topic:` line byte-equal
      to the frozen topic
  C2  registry: >= 911 rows; highest id >= S987; >= 3 new rows (id above S984) with
      tier A|B, status mined, opened 2026-11-05, used-by exactly the entry path
  C3  append-only registry: 0 lines removed vs the base registry (git show base-rev)
  C4  census: sources-census.sh validate --file <root>/corpus/SOURCES.md rc 0
  C5  index: tools/check-corpus-index.py --root <root> rc 0
  C6  every qualifying new id from C2 is cited inside the entry text
  C7  every qualifying new id has at least one capture under reports/round-97/evidence/
  C8  content sweep (round-96 closure routed defect 1: a filename-only zero-owner sweep
      missed a topic-line owner): knowledge files OTHER than the entry whose `- topic:`
      line or any markdown heading carries a frozen phrase (an ownership surface; a passing
      mention in prose or a table cell is not ownership). PASS iff that owner count is 0 on
      --root. (Guard leg: it passes on the base tree by design; its ability to fail is shown
      by reports/round-97/sweep-control.py on the round-96 base with the round-96 phrases.)
"""

import argparse
import difflib
import hashlib
import io
import os
import re
import subprocess
import sys

ENTRY_REL = 'corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md'
FROZEN_TOPIC = ('verbal duelling and ritual insult: contests fought in words — flyting, senna, '
                'song duels and boasting matches; the formula grammar of boast, taunt and riposte; '
                'the audience that adjudicates; the rules that keep an insult ritual rather than '
                'real; and the design procedure for a fictional word-contest whose stakes stay tied '
                'to its contestants, judges and occasions')
PHRASES = ['verbal duel', 'ritual insult', 'flyting', 'song duel', 'boast formula',
           'audience adjudication']
V8_SHA = 'f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0'
SELFTEST_FLOOR = 154
BATTERY_REFUSED = 31
CONTROL_SUMMARY = (7, 0, 24)
MUTATION_FLOOR = 118
NEW_ROW_MIN = 3
ROW_MIN, ROWS_MIN = 3, 5
BASE_HIGHEST = 984
ROWS_MIN_AFTER = 911
HIGHEST_MIN_AFTER = 987
REG_BASELINE = 'reports/round-95/controls/reg-v5.txt'
BATTERY_DRIVER = '.ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py'
BATTERY_PIN = 'reports/round-97/controls/battery97.sha256'
BATTERY_CONTROL = 'reports/round-97/controls/battery97-control-v8.txt'
MUTATION_DRIVER = '.ufo/waves/round-97/w1/stage/MutationTester97/mutants97.py'
MUTATION_PIN = 'reports/round-97/controls/mutants97.sha256'
MUTATION_FIRST = 'reports/round-97/controls/mutation97-first.txt'
EVIDENCE_DIR = 'reports/round-97/evidence'
CENSUS = '/home/vgpnk/Projects/shokunin/scripts/sources-census.sh'

RES = []


def leg(name, ok, detail):
    RES.append(bool(ok))
    print(f'LEG {name} {"PASS" if ok else "FAIL"} {detail}')
    return ok


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


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

    tool = os.path.join(root, 'tools/check-advance-evidence.py')

    # O0 tool identity
    sha = None
    if os.path.isfile(tool):
        sha = sha_file(tool)
        leg('O0', sha != V8_SHA, f'tool-sha256 {sha} (must differ from v8 {V8_SHA})')
    else:
        leg('O0', False, 'tool missing: tools/check-advance-evidence.py')

    # O1 selftest
    ok, detail = False, 'selftest not run'
    if sha:
        d = os.path.join(work, 'selftest')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', tool, '--selftest', '--work', d])
        m = re.search(r'SELFTEST PASS (\d+)/(\d+)', p.stdout)
        if p.returncode == 0 and m and m.group(1) == m.group(2) and int(m.group(1)) >= SELFTEST_FLOOR:
            ok = True
            detail = f'{m.group(1)}/{m.group(2)} floor={SELFTEST_FLOOR} rc=0'
        else:
            detail = (f'rc={p.returncode} '
                      + (f'{m.group(1)}/{m.group(2)} floor={SELFTEST_FLOOR}' if m else 'no SELFTEST PASS line'))
    leg('O1', ok, detail)

    # O2 battery97 (sha-pinned and receipt-bound)
    bdrv = os.path.join(root, BATTERY_DRIVER)
    pin = pin_value(os.path.join(root, BATTERY_PIN))
    rsha, rtext = receipt_value(os.path.join(root, BATTERY_CONTROL), 'BATTERY-SHA256')
    ok, detail, reg_lines = False, '', None
    if not os.path.isfile(bdrv):
        detail = f'driver missing: {BATTERY_DRIVER}'
    elif pin is None:
        detail = f'sha pin missing or malformed: {BATTERY_PIN}'
    elif rsha is None:
        detail = f'control receipt missing or lacks BATTERY-SHA256: {BATTERY_CONTROL}'
    elif not (sha_file(bdrv) == pin == rsha):
        detail = f'battery97 sha {sha_file(bdrv)} pin {pin} receipt {rsha} not all equal'
    else:
        cm = re.search(r'BATTERY-SUMMARY survivors=(\d+) unnamed=(\d+) refused=(\d+)', rtext)
        tm = re.search(r'^TOOL-SHA256 ([0-9a-f]{64})\s*$', rtext, re.M)
        if not (cm and tm and tm.group(1) == V8_SHA and tuple(map(int, cm.groups())) == CONTROL_SUMMARY):
            detail = (f'control receipt does not show survivors/unnamed/refused={CONTROL_SUMMARY} '
                      f'over v8 (summary={cm.groups() if cm else None} tool={tm.group(1) if tm else None})')
        else:
            d = os.path.join(work, 'battery')
            os.makedirs(d, exist_ok=True)
            p = run([sys.executable, '-B', bdrv, '--tool', tool, '--work', d])
            out = p.stdout
            reg_lines = [l for l in out.splitlines() if l.startswith('REG ')]
            m = re.search(r'BATTERY-SUMMARY survivors=(\d+) unnamed=(\d+) refused=(\d+)', out)
            tb = 'traceback=0' in out or 'traceback' not in out.lower()
            if m:
                s, u, r = map(int, m.groups())
                if s == 0 and u == 0 and r == BATTERY_REFUSED and tb:
                    ok = True
                detail = (f'survivors={s} unnamed={u} refused={r} required=0/0/{BATTERY_REFUSED} '
                          f'traceback-free={tb} rc={p.returncode} pin=receipt=driver')
            else:
                detail = f'no BATTERY-SUMMARY line, rc={p.returncode}'
    leg('O2', ok, detail)

    # O3 mutation97 (sha-pinned and first-measurement-bound)
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
        detail = f'mutants97 sha {sha_file(mdrv)} pin {mpin} first-receipt {fsha} not all equal'
    else:
        d = os.path.join(work, 'mutation')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', mdrv, '--tool', tool, '--work', d])
        m = re.search(r'MUTATION-SCORE: (\d+)/(\d+) killed, (\d+) survived, (\d+) broken-pattern', p.stdout)
        if m:
            k, t, sv, bp = map(int, m.groups())
            if k == t and sv == 0 and bp == 0 and t >= MUTATION_FLOOR:
                ok = True
            detail = f'{k}/{t} killed, {sv} survived, {bp} broken-pattern (floor total {MUTATION_FLOOR}) rc={p.returncode}'
        else:
            detail = f'no MUTATION-SCORE line, rc={p.returncode}'
    leg('O3', ok, detail)

    # O4 REG subset regression
    base_reg = os.path.join(root, REG_BASELINE)
    ok, detail = False, ''
    if reg_lines is None:
        detail = 'no REG output (battery leg did not run)'
    elif not os.path.isfile(base_reg):
        detail = f'baseline missing: {REG_BASELINE}'
    else:
        want = [l for l in open(base_reg, encoding='utf-8').read().splitlines() if l.startswith('REG ')]
        missing = [l for l in want if l not in set(reg_lines)]
        if want and not missing:
            ok = True
        detail = f'{len(want)} baseline REG lines, {len(want) - len(missing)} byte-identical in battery97 output'
    leg('O4', ok, detail)

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
                if (c[3] in ('A', 'B') and c[7] == 'mined' and c[8] == '2026-11-05'
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
        removed = sum(i2 - i1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('delete', 'replace'))
        added = sum(j2 - j1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('insert', 'replace'))
        ok = removed == 0
        detail = f'added={added} removed={removed} (removed must be 0)'
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

    # C7 captures
    ev = os.path.join(root, EVIDENCE_DIR)
    if good and os.path.isdir(ev):
        files = os.listdir(ev)
        nocap = [i for i in good if not any(f.startswith(i + '.') or f.startswith(i + '_') for f in files)]
        leg('C7', not nocap, f'qualifying ids with capture: {len(good) - len(nocap)}/{len(good)} missing={nocap}')
    else:
        leg('C7', False, f'evidence dir missing or no qualifying rows: {EVIDENCE_DIR}')

    # C8 content sweep (no other owner of the frozen phrases)
    kfiles = tree_knowledge(root)
    if not kfiles:
        leg('C8', False, 'no knowledge files found')
    else:
        owners = sweep_owners(kfiles, PHRASES, exclude=(ENTRY_REL,))
        leg('C8', not owners, f'files scanned={len(kfiles)} other owners={len(owners)} {owners[:5]}')

    npass = sum(1 for x in RES if x)
    verdict = 'PASS' if npass == len(RES) else 'FAIL'
    print(f'PREDISPATCH-97: {verdict} legs={npass}/{len(RES)}')
    return 0 if npass == len(RES) else 1


if __name__ == '__main__':
    sys.exit(main())
