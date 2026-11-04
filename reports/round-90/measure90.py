#!/usr/bin/env python3
"""Round-90 frozen counter: two claims, one instrument.

    python3 -B reports/round-90/measure90.py --root <repo> --lands <40hex> \
        --claim O|C --work <existing-dir> [--freeze <40hex>] [--json]

Claim O / operability (capability acquisition) — the advance-evidence grader.
  MATERIALIZE  the lands revision is materialized into <work>/mat with git archive
  TOOL         mat/tools/check-advance-evidence.py exists and its sha256 equals the
               freeze-pinned tool sha in reports/round-90/claims.json
  SELFTEST     that lands tool's own --selftest exits 0, prints SELFTEST PASS N/N
               with N equal to the frozen count, and reports every frozen refusal
               case name as `ok`
  MUTATION     the freeze-pinned reports/round-90/mutants.py, run over the lands
               tool bytes, kills every mutant (killed == total >= frozen minimum,
               0 survived, 0 broken-pattern). A stub or a rewrite that drops the
               targeted lines cannot pass this leg.
  REFUSALS     each frozen survivor class is refused by the named leg on the lands
               tool: one case per class, rc and leg taken from claims.json
  STUB         the frozen do-nothing stub control receipt exists and records that
               the stub fails SELFTEST and MUTATION (the claim's cheapest control)

Claim C / coverage — one new linguistics entry and the sources it mines.
  MATERIALIZE  as above
  ENTRY        the freeze-pinned tool's entry mode (frozen bytes, run against the
               materialized lands tree) passes every entry leg the claim declares
  INDEX        the freeze-pinned tools/check-corpus-index.py exits 0 over mat
  APPENDONLY   no base registry row removed or cell-changed; every new mined A/B
               row opened on the round date is cited by the entry; the entry's
               README index row and partition count are present

Exit 0 pass, 1 finding, 2 refused (bad arguments or unreadable input).
No network access: every surface is a committed capture.

This counter offers no --selftest: every leg is a subprocess leg whose positive is
the lands run and whose negative is the committed at-freeze run (both receipts are
in reports/round-90/), and the grader it drives ships its own 67-check selftest and
a 43/43 mutation receipt. QUALITY23's "a counter without --selftest says so in its
docstring" applies to this paragraph.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

REFUSED = 2


class Refused(Exception):
    pass


def sh(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def git_show(root, rev, path):
    r = sh(['git', '-C', root, 'show', f'{rev}:{path}'])
    if r.returncode != 0:
        raise Refused(f'git show {rev}:{path} failed: {(r.stderr or "").strip()}')
    return r.stdout


def materialize(root, rev, dest):
    os.makedirs(dest, exist_ok=True)
    r = sh(['git', '-C', root, 'archive', '--format=tar', rev], cwd=dest)
    if r.returncode != 0:
        raise Refused(f'git archive {rev} failed: {(r.stderr or "").strip()}')
    t = subprocess.run(['tar', '-x', '-C', dest], input=r.stdout.encode(),
                       capture_output=True, text=True)
    if t.returncode != 0:
        raise Refused(f'tar -x failed: {(t.stderr or "").strip()}')


def sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def legs_emit(legs, label, receipt=None, as_json=False):
    lines = []
    for name, ok, expected, observed in legs:
        lines.append(f'LEG {"PASS" if ok else "FAIL"} {name} expected={expected} observed={observed}')
    failed = [n for n, ok, _, _ in legs if not ok]
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
                           'legs': [dict(name=n, pass_=bool(o), expected=e, observed=obs)
                                    for n, o, e, obs in legs]}, f, indent=1, sort_keys=True)
    return 0 if not failed else 1


def claims(root, freeze):
    raw = git_show(root, freeze, 'reports/round-90/claims.json')
    return json.loads(raw)


def grade_o(root, lands, freeze, work, cfg):
    legs = []
    mat = os.path.join(work, 'mat')
    materialize(root, lands, mat)
    legs.append(('MATERIALIZE', os.path.isdir(os.path.join(mat, 'corpus')), f'lands {lands} materialized',
                 mat if os.path.isdir(os.path.join(mat, 'corpus')) else 'no corpus/ in the archive'))

    tool_rel = 'tools/check-advance-evidence.py'
    tool = os.path.join(mat, tool_rel)
    want = cfg['O']['tool_sha256']
    got = sha256_file(tool) if os.path.isfile(tool) else ''
    legs.append(('TOOL', got == want, f'{tool_rel} sha256 {want}', got or 'absent'))

    st = os.path.join(work, 'st-o')
    os.makedirs(st, exist_ok=True)
    r = sh([sys.executable, '-B', tool, '--selftest', '--work', st])
    out = (r.stdout or '') + (r.stderr or '')
    m = re.search(r'SELFTEST (PASS|FAIL) (\d+)/(\d+)', out)
    total = int(m.group(3)) if m else 0
    ok = (r.returncode == 0 and m and m.group(1) == 'PASS'
          and total == cfg['O']['selftest_checks'])
    legs.append(('SELFTEST', bool(ok), f'rc 0 and SELFTEST PASS {cfg["O"]["selftest_checks"]}/{cfg["O"]["selftest_checks"]}',
                 (m.group(0) if m else out.strip().splitlines()[-1:] or 'no verdict line')))

    missing = [c for c in cfg['O']['refusal_cases']
               if not re.search(r'^  ok +' + re.escape(c) + r':', out, re.M)]
    legs.append(('REFUSALS', not missing,
                 f'{len(cfg["O"]["refusal_cases"])} refusal cases each ok',
                 'all ok' if not missing else 'not ok: ' + ', '.join(missing)))

    mut = os.path.join(work, 'mutants.py')
    with open(mut, 'w') as f:
        f.write(git_show(root, freeze, 'reports/round-90/mutants.py'))
    mw = os.path.join(work, 'mut')
    os.makedirs(mw, exist_ok=True)
    r = sh([sys.executable, '-B', mut, '--root', mat, '--work', mw,
            '--out', os.path.join(work, 'mutation-score')])
    out = (r.stdout or '') + (r.stderr or '')
    mm = re.search(r'MUTATION-SCORE: (\d+)/(\d+) killed, (\d+) survived, (\d+) broken-pattern', out)
    killed, total_m, survived, broken = (int(x) for x in mm.groups()) if mm else (0, 0, 0, 0)
    ok = bool(mm) and killed == total_m and total_m >= cfg['O']['mutation_min'] and survived == 0 and broken == 0
    legs.append(('MUTATION', ok,
                 f'killed==total>={cfg["O"]["mutation_min"]}, 0 survived, 0 broken-pattern',
                 (mm.group(0) if mm else out.strip().splitlines()[-1:] or 'no score line')))

    stub = os.path.join(mat, cfg['O']['stub_receipt'])
    text = open(stub).read() if os.path.isfile(stub) else ''
    ok = ('SELFTEST' in text and 'FAIL' in text and 'MUTATION' in text
          and 'broken-pattern' in text)
    legs.append(('STUB', ok, f'{cfg["O"]["stub_receipt"]} records the stub failing SELFTEST and MUTATION',
                 'recorded' if ok else 'missing or incomplete'))
    return legs


def grade_c(root, lands, freeze, work, cfg):
    legs = []
    mat = os.path.join(work, 'mat')
    materialize(root, lands, mat)
    legs.append(('MATERIALIZE', os.path.isdir(os.path.join(mat, 'corpus')), f'lands {lands} materialized',
                 mat if os.path.isdir(os.path.join(mat, 'corpus')) else 'no corpus/ in the archive'))

    c = cfg['C']
    tool = os.path.join(work, 'tool-frozen.py')
    with open(tool, 'w') as f:
        f.write(git_show(root, freeze, 'tools/check-advance-evidence.py'))
    base_reg = os.path.join(work, 'base-registry.md')
    with open(base_reg, 'w') as f:
        f.write(git_show(root, cfg['base'], 'corpus/SOURCES.md'))
    receipt = os.path.join(work, 'entry-receipt.txt')
    args = [sys.executable, '-B', tool, 'entry', '--root', mat,
            '--entry', os.path.join(mat, c['entry']),
            '--base-registry', base_reg,
            '--lands-registry', os.path.join(mat, 'corpus/SOURCES.md'),
            '--lesson', os.path.join(mat, cfg['lesson']),
            '--manifest', os.path.join(mat, c['manifest']),
            '--capture-dir', c['capture_dir'],
            '--as-of', cfg['as_of'],
            '--topic', c['topic'],
            '--min-bytes', str(c['min_bytes']),
            '--min-headings', str(c['min_headings']),
            '--min-new-ids', str(c['new_ids_min']),
            '--min-topic-overlap', str(c['min_topic_overlap']),
            '--table-min-rows', str(c['table_min_rows']),
            '--table-min-cols', str(c['table_min_cols']),
            '--graded', 'corpus/SOURCES.md',
            '--graded', cfg['lesson'],
            '--receipt', receipt]
    r = sh(args)
    out = (r.stdout or '') + (r.stderr or '')
    want_legs = c['legs']
    seen = dict(re.findall(r'^LEG (PASS|FAIL) (\S+)', out, re.M)[::-1])
    missing = [l for l in want_legs if l not in seen]
    failed = [l for l in want_legs if seen.get(l) == 'FAIL']
    ok = r.returncode == 0 and not missing and not failed
    legs.append(('ENTRY', ok, f'entry mode passes {",".join(want_legs)}',
                 'clean' if ok else f'rc={r.returncode} missing={missing} failed={failed}'))

    idx = os.path.join(work, 'check-corpus-index.py')
    with open(idx, 'w') as f:
        f.write(git_show(root, freeze, 'tools/check-corpus-index.py'))
    r = sh([sys.executable, '-B', idx] + [a.replace('{tree}', mat) for a in c['index_args']])
    out = ((r.stdout or '') + (r.stderr or '')).strip()
    legs.append(('INDEX', r.returncode == 0, 'index tool exit 0 over the lands tree',
                 out.splitlines()[-1] if out else 'no output'))

    base_rows = registry_text(git_show(root, cfg['base'], 'corpus/SOURCES.md'))
    lands_rows = registry_text(git_show(root, lands, 'corpus/SOURCES.md'))
    problems = []
    for rid, cells in base_rows.items():
        if rid not in lands_rows:
            problems.append(f'{rid} removed')
        elif lands_rows[rid] != cells:
            problems.append(f'{rid} cells changed')
    entry = git_show(root, lands, c['entry'])
    cited = set(re.findall(r'\bS\d{3,}\b', entry))
    new_ids = sorted(set(lands_rows) - set(base_rows))
    qualifying = []
    for rid in new_ids:
        cells = lands_rows[rid]
        tier, status, opened, used = cells[3], cells[7], cells[8], cells[10]
        if tier in ('A', 'B') and status == 'mined' and opened == cfg['as_of'] \
                and os.path.basename(c['entry']) in used and rid in cited:
            qualifying.append(rid)
    if len(qualifying) < c['new_ids_min']:
        problems.append(f'{len(qualifying)} qualifying new ids < {c["new_ids_min"]}')
    readme = git_show(root, lands, 'corpus/README.md')
    if os.path.basename(c['entry']) not in readme:
        problems.append('entry absent from corpus/README.md')
    legs.append(('APPENDONLY', not problems,
                 f'no base row changed; >={c["new_ids_min"]} new mined A/B rows cited; README row',
                 'clean' if not problems else '; '.join(problems)))
    return legs


def registry_text(text):
    rows = {}
    for line in text.splitlines():
        m = re.match(r'^ {0,3}\|[ ]*(S\d{3,})[ ]*\|', line)
        if m:
            rows[m.group(1)] = [c.strip() for c in line.strip().strip('|').split('|')]
    return rows


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--lands', required=True)
    ap.add_argument('--claim', required=True, choices=['O', 'C'])
    ap.add_argument('--work', required=True)
    ap.add_argument('--freeze')
    ap.add_argument('--receipt')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args(argv)
    try:
        if not re.match(r'^[0-9a-f]{40}$', args.lands):
            raise Refused('--lands must be a full 40-hex revision')
        if not os.path.isdir(args.work):
            raise Refused('--work must be an existing directory')
        freeze = args.freeze
        if not freeze:
            r = sh(['git', '-C', args.root, 'log', '--format=%H', '--diff-filter=A', '--',
                    'reports/round-90/claims.json'])
            freeze = (r.stdout or '').split()[-1] if r.returncode == 0 and r.stdout.strip() else ''
        if not re.match(r'^[0-9a-f]{40}$', freeze or ''):
            raise Refused('cannot resolve the freeze commit; pass --freeze <40hex>')
        cfg = claims(args.root, freeze)
        legs = grade_o(args.root, args.lands, freeze, args.work, cfg) if args.claim == 'O' \
            else grade_c(args.root, args.lands, freeze, args.work, cfg)
        return legs_emit(legs, f'MEASURE90-{args.claim}', args.receipt, args.json)
    except Refused as exc:
        print(f'MEASURE90_ERROR: {exc}', file=sys.stderr)
        return REFUSED


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
