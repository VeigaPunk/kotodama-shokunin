#!/usr/bin/env python3
"""Round-95 pre-dispatch counter (frozen; the round's claims are judged on it).

Usage:
  python3 -B reports/round-95/predispatch.py --root <tree> --work <scratch> --base-rev <40hex>

Legs (exit 0 iff every leg prints PASS):

  O0  tool sha256 (named, no target baked in; claims.json names the before sha)
  O1  selftest: rc 0, line `SELFTEST PASS N/N`, N >= 134
  O2  battery95: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=14`
      (fail closed when the stage driver is missing)
  O3  mutation95: `MUTATION-SCORE: <killed>/<total> killed, 0 survived,
      0 broken-pattern` with killed == total and total >= 95
      (fail closed when the stage driver is missing)
  O4  REG regression: `reports/round-95/controls/reg-v5.txt` exists (fail closed
      when missing) and the battery driver's REG section over the tree's tool is
      byte-identical to it
  C1  entry `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`
      present; >= 12000 B; >= 6 h2; one table with >= 5 data rows x >= 3 cols;
      >= 4 of the six frozen sub-topic phrases in h2 headings or table data
      rows; the `- topic:` line byte-equal to the frozen topic
  C2  registry: >= 896 rows; highest id >= S972; >= 3 new rows above S969 with
      tier A|B, status mined, opened 2026-11-05, used-by exactly the entry path
  C3  append-only registry: 0 lines removed vs the base registry; the base
      bytes come from `git -C <root> show <base-rev>:corpus/SOURCES.md` when
      <root> is inside a git work tree, else from the required --base-registry
      file (difflib opcode counting, never grep subtraction)
  C4  census: sources-census.sh validate --file <root>/corpus/SOURCES.md rc 0
  C5  index: tools/check-corpus-index.py --root <root> rc 0

Every missing input (driver, baseline, tree, work) fails its leg closed — never
a zero (kagi r33/r35 class). No network. Scratch only under --work.
"""

import argparse
import difflib
import hashlib
import os
import re
import subprocess
import sys

ENTRY_REL = 'corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md'
FROZEN_TOPIC = ('funerary laments and dirges: the sung speech of mourning — professional keeners '
                'and lament genres, antiphonal and refrain structures, formulaic grief content '
                '(praise of the dead, address to the dead, blame and consolation), gendered '
                'mourning rules, the lament between speech and song, and the design procedure '
                'for a fictional mourning register')
PHRASES = ['professional keeners', 'antiphonal lament', 'lament refrain',
           'praise of the dead', 'gendered mourning rules', 'fictional mourning register']
SELFTEST_FLOOR = 134
BATTERY_REFUSED = 14
MUTATION_FLOOR = 95
NEW_ROW_MIN = 3
ROW_MIN, ROWS_MIN = 3, 5
REG_BASELINE = 'reports/round-95/controls/reg-v5.txt'
BATTERY_DRIVER = '.ufo/waves/round-95/w1/stage/ExecBattery95/battery95.py'
MUTATION_DRIVER = '.ufo/waves/round-95/w1/stage/ExecMutants95/mutants95.py'
CENSUS = '/home/vgpnk/Projects/shokunin/scripts/sources-census.sh'

RES = []


def leg(name, ok, detail):
    RES.append(ok)
    print(f'LEG {name} {"PASS" if ok else "FAIL"} {detail}')
    return ok


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--base-rev', required=True)
    ap.add_argument('--base-registry', default=None,
                    help='file holding the base corpus/SOURCES.md bytes when --root is not a git work tree')
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
    nlegs = 0

    # O0
    tool = os.path.join(root, 'tools/check-advance-evidence.py')
    import hashlib
    if os.path.isfile(tool):
        sha = hashlib.sha256(open(tool, 'rb').read()).hexdigest()
        leg('O0', True, f'tool-sha256 {sha}')
    else:
        sha = None
        leg('O0', False, f'tool missing: tools/check-advance-evidence.py')
    nlegs += 1

    # O1
    ok = False
    detail = 'selftest not run'
    if sha:
        d = os.path.join(work, 'selftest')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', tool, '--selftest', '--work', d])
        m = re.search(r'SELFTEST PASS (\d+)/(\d+)', p.stdout)
        if p.returncode == 0 and m and int(m.group(1)) >= SELFTEST_FLOOR and m.group(1) == m.group(2):
            ok = True
            detail = f'{m.group(1)}/{m.group(2)} floor={SELFTEST_FLOOR} rc=0'
        else:
            detail = (f'rc={p.returncode} '
                      + (f'{m.group(1)}/{m.group(2)} floor={SELFTEST_FLOOR}' if m else 'no SELFTEST PASS line'))
    leg('O1', ok, detail)
    nlegs += 1

    # O2 battery
    bdrv = os.path.join(root, BATTERY_DRIVER)
    ok, detail, reg_lines = False, '', None
    if not os.path.isfile(bdrv):
        detail = f'driver missing: {BATTERY_DRIVER}'
    else:
        d = os.path.join(work, 'battery')
        os.makedirs(d, exist_ok=True)
        p = run([sys.executable, '-B', bdrv, '--tool', tool, '--work', d])
        out = p.stdout
        reg_lines = [l for l in out.splitlines() if l.startswith('REG ')]
        m = re.search(r'BATTERY-SUMMARY survivors=(\d+) unnamed=(\d+) refused=(\d+)', out)
        if m:
            s, u, r = map(int, m.groups())
            if s == 0 and u == 0 and r == BATTERY_REFUSED:
                ok = True
            detail = f'survivors={s} unnamed={u} refused={r} required=0/0/{BATTERY_REFUSED} rc={p.returncode}'
        else:
            detail = f'no BATTERY-SUMMARY line, rc={p.returncode}'
    leg('O2', ok, detail)
    nlegs += 1

    # O3 mutation
    mdrv = os.path.join(root, MUTATION_DRIVER)
    ok, detail = False, ''
    if not os.path.isfile(mdrv):
        detail = f'driver missing: {MUTATION_DRIVER}'
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
    nlegs += 1

    # O4 regression
    base_reg = os.path.join(root, REG_BASELINE)
    ok, detail = False, ''
    if reg_lines is None:
        detail = 'no REG output (battery leg did not run)'
    elif not os.path.isfile(base_reg):
        detail = f'baseline missing: {REG_BASELINE}'
    else:
        want = open(base_reg, encoding='utf-8').read().splitlines()
        if reg_lines == want:
            ok = True
            detail = f'{len(want)} REG lines byte-identical to {REG_BASELINE}'
        else:
            detail = f'REG drift vs {REG_BASELINE}: {len(want)} baseline vs {len(reg_lines)} observed lines'
    leg('O4', ok, detail)
    nlegs += 1

    # C1 entry
    entry_p = os.path.join(root, ENTRY_REL)
    ok, detail = False, ''
    if not os.path.isfile(entry_p):
        detail = 'entry absent'
    else:
        raw = open(entry_p, encoding='utf-8').read()
        size = len(raw.encode('utf-8'))
        heads = [l for l in raw.splitlines() if l.startswith('## ')]
        rows, cols, sep = 0, 0, False
        best = (0, 0)
        for l in raw.splitlines():
            s = l.strip()
            if not s.startswith('|'):
                sep = False
                continue
            if re.match(r'^\|[\s:\-|]+\|$', s):
                sep = True
                cells = 0
                continue
            c = len(l.strip().strip('|').split('|'))
            if sep:
                rows += 1
                cols = c
                best = max(best, (rows, cols))
        anchor_heads = ' '.join(norm(h) for h in heads)
        table_rows = []
        sep = False
        for l in raw.splitlines():
            s = l.strip()
            if not s.startswith('|'):
                sep = False
                continue
            if re.match(r'^\|[\s:\-|]+\|$', s):
                sep = True
                continue
            if sep:
                table_rows.append(norm(l))
        hits = [p for p in PHRASES if norm(p) in anchor_heads or any(norm(p) in t for t in table_rows)]
        tline = next((l for l in raw.splitlines() if l.strip().startswith('- topic:')), '')
        tline_ok = tline.strip() == ('- topic: ' + FROZEN_TOPIC)
        r, c = best
        if (size >= 12000 and len(heads) >= 6 and r >= ROWS_MIN and c >= ROW_MIN
                and len(hits) >= 4 and tline_ok):
            ok = True
        detail = (f'bytes={size} h2={len(heads)} table={r}x{c} phrases={len(hits)}/{len(PHRASES)} '
                  f'topic-line={"equal" if tline_ok else "differ"}')
    leg('C1', ok, detail)
    nlegs += 1

    # C2 registry
    reg_p = os.path.join(root, 'corpus/SOURCES.md')
    ok, detail = False, ''
    rows_by_id = {}
    if not os.path.isfile(reg_p):
        detail = 'registry missing'
    else:
        for line in open(reg_p, encoding='utf-8'):
            if re.match(r'^ {0,3}\|\s*S[0-9]{3,}\s*\|', line):
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) == 11:
                    rows_by_id[cells[0]] = cells
        if not rows_by_id:
            detail = 'no registry rows parsed'
        else:
            ids = sorted(rows_by_id, key=lambda x: int(x[1:]))
            highest = ids[-1]
            new = [i for i in ids if int(i[1:]) > 969]
            good = []
            for i in new:
                c = rows_by_id[i]
                if (c[3] in ('A', 'B') and c[7] == 'mined' and c[8] == '2026-11-05'
                        and c[10] == ENTRY_REL):
                    good.append(i)
            if (len(ids) >= 896 and int(highest[1:]) >= 972 and len(good) >= NEW_ROW_MIN):
                ok = True
            detail = (f'rows={len(ids)} highest={highest} new={len(new)} qualifying={len(good)} '
                      f'(min rows 896, highest >= S972, qualifying >= {NEW_ROW_MIN})')
    leg('C2', ok, detail)
    nlegs += 1

    # C3 append-only
    ok, detail = False, ''
    reg_bytes = open(reg_p, 'rb').read() if os.path.isfile(reg_p) else None
    base_bytes = None
    if reg_bytes is None:
        detail = 'registry missing'
    else:
        p = subprocess.run(['git', '-C', root, 'rev-parse', '--git-dir'],
                           capture_output=True, text=True)
        if p.returncode == 0:
            b = subprocess.run(['git', '-C', root, 'show', f'{a.base_rev}:corpus/SOURCES.md'],
                               capture_output=True)
            if b.returncode == 0:
                base_bytes = b.stdout
            else:
                detail = f'git show base failed rc={b.returncode}: {b.stderr.decode(errors="replace").strip()[:120]}'
        elif a.base_registry and os.path.isfile(a.base_registry):
            base_bytes = open(a.base_registry, 'rb').read()
        else:
            detail = ('root is not a git work tree and no --base-registry file given; '
                      'refusing to score the append-only leg')
    if reg_bytes is not None and base_bytes is not None:
        import io
        base_lines = io.StringIO(base_bytes.decode('utf-8', errors='replace')).readlines()
        land_lines = io.StringIO(reg_bytes.decode('utf-8', errors='replace')).readlines()
        sm = difflib.SequenceMatcher(a=base_lines, b=land_lines, autojunk=False)
        removed = sum(i2 - i1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('delete', 'replace'))
        added = sum(j2 - j1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ('insert', 'replace'))
        ok = removed == 0
        detail = f'added={added} removed={removed} (removed must be 0)'
    leg('C3', ok, detail)
    nlegs += 1

    # C4 census
    p = run(['bash', CENSUS, 'validate', '--file', os.path.join(root, 'corpus/SOURCES.md')])
    ok = p.returncode == 0
    leg('C4', ok, f'census rc={p.returncode}')
    nlegs += 1

    # C5 index
    idx = os.path.join(root, 'tools/check-corpus-index.py')
    if os.path.isfile(idx):
        p = run([sys.executable, '-B', idx, '--root', root])
        ok = p.returncode == 0
        last = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ''
        leg('C5', ok, f'index rc={p.returncode} last: {last[:100]}')
    else:
        leg('C5', False, f'index tool missing: tools/check-corpus-index.py')
    nlegs += 1

    npass = sum(1 for x in RES if x)
    verdict = 'PASS' if npass == nlegs else 'FAIL'
    print(f'PREDISPATCH-95: {verdict} legs={npass}/{nlegs}')
    return 0 if npass == nlegs else 1


if __name__ == '__main__':
    sys.exit(main())
