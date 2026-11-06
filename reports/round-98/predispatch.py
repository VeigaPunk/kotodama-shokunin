#!/usr/bin/env python3
"""Round-98 pre-dispatch counter (frozen before any candidate is scored; the round's
claims O and C are judged on it).

Usage:
  python3 -B reports/round-98/predispatch.py --root <tree> --work <scratch> --base-rev <40hex>

Legs (exit 0 iff every leg prints PASS):

  O0  tool sha256 named; PASS only when it differs from the frozen v9 sha
      1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b
  O1  selftest: rc 0, line `SELFTEST PASS N/N`, N == N-total and N >= 160
      (v9 total 155 plus at least one pin for each of the five round-98 classes)
  O2  battery98 (reports/round-98/controls/battery98.py, committed in the freeze commit):
      `BATTERY-SUMMARY survivors=0 unnamed=0 refused=36 traceback=0 clean=3 not-clean=0`.
      Fails closed when the driver, its pin or its control receipt is missing. Pin binding:
      the driver's sha256 must equal reports/round-98/controls/battery98.sha256 AND the
      `BATTERY-SHA256 <hex>` line of reports/round-98/controls/battery98-control-v9.txt, and
      that receipt must show `TOOL-SHA256 <v9 sha>` and survivors=5 unnamed=0 refused=31
      clean=3 not-clean=0.
  O3  mutation98: `MUTATION-SCORE: <killed>/<total> killed, 0 survived, 0 broken-pattern`
      with killed == total and total >= 126. Pin binding: the driver's sha256 must equal
      reports/round-98/controls/mutants98.sha256 AND the `DRIVER-SHA256 <hex>` line of the
      first-measurement receipt reports/round-98/controls/mutation98-first.txt.
  O4  REG regression: every REG line of reports/round-95/controls/reg-v5.txt occurs verbatim
      among the `REG ` lines battery98 prints over the tree's tool
  O5  independent replay: the round-97 critic driver
      .ufo/waves/round-97/w1/stage/CriticO97/attacks_critic97.py (sha pinned below) with
      battery97 (sha pinned below) over the tree's tool: DEL1, ENC1, ROMAN1, SUP1 and FWPER1
      each `outcome=REFUSED-NAMED`; CYRH1, ZWSH1 and BELH1 (benign clean-twin controls) each
      rc=0; tally unnamed=0 traceback=0. Control over v9: reports/round-98/controls/critic97-on-v9.txt
      (survivors=8).
  C1  entry `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` present;
      >= 12000 B; >= 6 h2; one table with >= 5 data rows x >= 3 cols; >= 4 of the six
      frozen phrases in h2 headings or table data rows; the `- topic:` line byte-equal
      to the frozen topic
  C2  registry: >= 921 rows; highest id >= S997; >= 4 new rows (id above S993) with tier
      A|B, status mined, opened 2026-11-05 or 2026-11-06, used-by exactly the entry path
  C3  append-only registry per CORPUS.md rule 2: every base line that the landed file
      removes or replaces must be a registry row whose id is present in the landed file with
      cells id, source, kind, tier, scope, anchor, teaches and opened byte-identical (only
      status, recheck and used-by may change in place); any other removed line fails.
  C4  census: sources-census.sh validate --file <root>/corpus/SOURCES.md rc 0
  C5  index: tools/check-corpus-index.py --root <root> rc 0
  C6  every qualifying new id from C2 is cited inside the entry text
  C7  evidence binding (round-97 closure routed defects 3 and 4): every qualifying id has an
      object in reports/round-98/evidence/manifest.json (a JSON list) with `id`, `quote`,
      `quote_capture` and `captures`; every `captures[].file` exists under the evidence dir
      and its sha256 equals `captures[].sha256`; `quote_capture` names an existing file
      whose whitespace-collapsed text contains the whitespace-collapsed quote exactly once;
      the quote has 1..25 whitespace words; and the registry row's anchor cell contains
      the quote (whitespace-collapsed). Counting command for the report: this leg's detail.
  C8  content sweep: knowledge files OTHER than the entry whose `- topic:` line or any
      markdown heading carries a frozen phrase. PASS iff that owner count is 0 on --root.
      (Guard leg: passes on base by design; reports/round-97/sweep-control.py shows the
      sweep function able to fail.)
  C9  non-author re-open (fabricated captures pass C7 by construction; see
      reports/round-98/controls/forgery/P-C-BOUND.txt): the ReviewerC98 seat's file
      .ufo/waves/round-98/w1/stage/ReviewerC98/reopen.json (a JSON list of objects with `id`,
      `url`, `http`, `fresh_sha256`, `quote_count`) names >= 3 distinct qualifying ids, each
      with http 200, quote_count 1 on freshly fetched bytes, a 64-hex fresh_sha256, and a url
      that occurs in that id's registry source cell.
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

ENTRY_REL = 'corpus/knowledge/linguistics/toast-drinking-speech-formulae.md'
FROZEN_TOPIC = ('toasts and drinking-speech formulae: the toast as a speech act over a shared cup — '
                'health-drinking, libation and the pledge; the toastmaster\'s office and the order of a '
                'toast sequence; the drinking oath and the boast-cup; refusal, reciprocity and the '
                'penalty cup; and the design procedure for a fictional drinking rite whose words stay '
                'tied to its hosts, guests, cups and occasions')
PHRASES = ['toast formula', 'health-drinking', 'toastmaster', 'libation', 'toast sequence',
           'drinking oath']
V9_SHA = '1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b'
SELFTEST_FLOOR = 160
BATTERY_REFUSED = 36
BATTERY_CLEAN = 3
CONTROL_SUMMARY = (5, 0, 31, 3, 0)
MUTATION_FLOOR = 126
NEW_ROW_MIN = 4
ROW_MIN, ROWS_MIN = 3, 5
BASE_HIGHEST = 993
ROWS_MIN_AFTER = 921
HIGHEST_MIN_AFTER = 997
OPENED_OK = ('2026-11-05', '2026-11-06')
REG_BASELINE = 'reports/round-95/controls/reg-v5.txt'
BATTERY_DRIVER = 'reports/round-98/controls/battery98.py'
BATTERY_PIN = 'reports/round-98/controls/battery98.sha256'
BATTERY_CONTROL = 'reports/round-98/controls/battery98-control-v9.txt'
MUTATION_DRIVER = '.ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py'
MUTATION_PIN = 'reports/round-98/controls/mutants98.sha256'
MUTATION_FIRST = 'reports/round-98/controls/mutation98-first.txt'
CRITIC_DRIVER = '.ufo/waves/round-97/w1/stage/CriticO97/attacks_critic97.py'
CRITIC_SHA = '48d8e0f69ac2b482571efa2d0cf48877098f3f61db2e22646d05089ce28ee1e4'
CRITIC_BATTERY = '.ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py'
CRITIC_BATTERY_SHA = '79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c'
CRITIC_MUST_REFUSE = ('DEL1', 'ENC1', 'ROMAN1', 'SUP1', 'FWPER1')
CRITIC_MUST_PASS = ('CYRH1', 'ZWSH1', 'BELH1')
EVIDENCE_DIR = 'reports/round-98/evidence'
CENSUS = '/home/vgpnk/Projects/shokunin/scripts/sources-census.sh'
REOPEN = '.ufo/waves/round-98/w1/stage/ReviewerC98/reopen.json'
REOPEN_MIN = 3

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
        leg('O0', sha != V9_SHA, f'tool-sha256 {sha} (must differ from v9 {V9_SHA})')
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

    # O2 battery98 (sha-pinned, freeze-committed and receipt-bound)
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
        detail = f'battery98 sha {sha_file(bdrv)} pin {pin} receipt {rsha} not all equal'
    else:
        cm = re.search(r'BATTERY-SUMMARY survivors=(\d+) unnamed=(\d+) refused=(\d+) traceback=\d+ '
                       r'clean=(\d+) not-clean=(\d+)', rtext)
        tm = re.search(r'^TOOL-SHA256 ([0-9a-f]{64})\s*$', rtext, re.M)
        if not (cm and tm and tm.group(1) == V9_SHA and tuple(map(int, cm.groups())) == CONTROL_SUMMARY):
            detail = (f'control receipt does not show survivors/unnamed/refused/clean/not-clean={CONTROL_SUMMARY} '
                      f'over v9 (summary={cm.groups() if cm else None} tool={tm.group(1) if tm else None})')
        else:
            d = os.path.join(work, 'battery')
            os.makedirs(d, exist_ok=True)
            p = run([sys.executable, '-B', bdrv, '--tool', tool, '--work', d])
            out = p.stdout
            reg_lines = [l for l in out.splitlines() if l.startswith('REG ')]
            m = re.search(r'BATTERY-SUMMARY survivors=(\d+) unnamed=(\d+) refused=(\d+) traceback=(\d+) '
                          r'clean=(\d+) not-clean=(\d+)', out)
            if m:
                s, u, r, t, c, nc = map(int, m.groups())
                if (s, u, r, t, c, nc) == (0, 0, BATTERY_REFUSED, 0, BATTERY_CLEAN, 0) and p.returncode == 0:
                    ok = True
                detail = (f'survivors={s} unnamed={u} refused={r} traceback={t} clean={c} not-clean={nc} '
                          f'required=0/0/{BATTERY_REFUSED}/0/{BATTERY_CLEAN}/0 rc={p.returncode} pin=receipt=driver')
            else:
                detail = f'no BATTERY-SUMMARY line, rc={p.returncode}'
    leg('O2', ok, detail)

    # O3 mutation98 (sha-pinned and first-measurement-bound)
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
        detail = f'mutants98 sha {sha_file(mdrv)} pin {mpin} first-receipt {fsha} not all equal'
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
        detail = f'{len(want)} baseline REG lines, {len(want) - len(missing)} byte-identical in battery98 output'
    leg('O4', ok, detail)

    # O5 independent critic97 replay (pinned driver and battery)
    cdrv = os.path.join(root, CRITIC_DRIVER)
    cbat = os.path.join(root, CRITIC_BATTERY)
    ok, detail = False, ''
    if not (os.path.isfile(cdrv) and os.path.isfile(cbat)):
        detail = 'critic driver or battery97 missing'
    elif sha_file(cdrv) != CRITIC_SHA or sha_file(cbat) != CRITIC_BATTERY_SHA:
        detail = f'critic pins differ: driver {sha_file(cdrv)} battery {sha_file(cbat)}'
    elif not sha:
        detail = 'tool missing'
    else:
        d = os.path.join(work, 'critic97')
        os.makedirs(d, exist_ok=True)
        env = dict(os.environ, CRIT_WORK=d, CRIT_BATTERY=cbat, CRIT_TOOL=tool,
                   CRIT_OUT_JSON=os.path.join(d, 'out.json'))
        p = run([sys.executable, '-B', cdrv], env=env)
        outc = {}
        for l in p.stdout.splitlines():
            mm = re.match(r'^CLASS (\S+) rc=(\d+) .*outcome=(\S+)\s*$', l)
            if mm:
                outc[mm.group(1)] = (int(mm.group(2)), mm.group(3))
        tm = re.search(r'CRITIC-O97 survivors=(\d+) unnamed=(\d+) refused=(\d+) traceback=(\d+)', p.stdout)
        bad_ref = [c for c in CRITIC_MUST_REFUSE if outc.get(c, (None, None))[1] != 'REFUSED-NAMED']
        bad_pass = [c for c in CRITIC_MUST_PASS if outc.get(c, (None, None))[0] != 0]
        if tm and p.returncode == 0 and not bad_ref and not bad_pass and tm.group(2) == '0' and tm.group(4) == '0':
            ok = True
        detail = (f'tally={tm.group(0) if tm else None} rc={p.returncode} not-refused-named={bad_ref} '
                  f'benign-not-rc0={bad_pass}')
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
    print(f'PREDISPATCH-98: {verdict} legs={npass}/{len(RES)}')
    return 0 if npass == len(RES) else 1


if __name__ == '__main__':
    sys.exit(main())
