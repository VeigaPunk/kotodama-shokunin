#!/usr/bin/env python3
"""Round-92 frozen counter: two claims, one instrument.

    python3 -B reports/round-92/measure92.py --root <repo> --lands <40hex> \
        --claim O|C --work <existing-dir> --freeze <40hex> [--receipt PATH] [--json]

Every constant is read from the freeze commit (git show <freeze>:...), never
from the graded tree. The lands revision is materialized with git archive into
<work>/mat; the freeze's own tool, mutant pass and stub are read from the
freeze commit and run against the lands bytes.

Refusals (exit 2): a revision that is not 40-hex, <lands> equal to the frozen
base, or <freeze> not an ancestor of <lands>. <lands> equal to <freeze> is
graded, never passed: it is the do-nothing control. The counter's own leg
table must equal the frozen claims.json legs[claim] list (exit 2,
"refused: LEGCOUNT"); the receipt carries the frozen leg line.

Claim O / operability - the advance-evidence grader v3 (routed round-91
survivor repairs).
  MATERIALIZE  lands materialized with git archive
  TOOL         mat/tools/check-advance-evidence.py sha256 == claims.json O.tool_sha256
  SELFTEST     that tool's --selftest exits 0 and prints SELFTEST PASS N/N, N == O.selftest_checks
  OKCOUNT      the selftest prints exactly O.selftest_checks lines beginning `  ok ` (a printer
               that writes the tally line but not the cases fails here)
  REFUSALS     every O.refusal_cases name is printed as `  ok <name>:`
  MUTATION     the freeze-pinned mutants.py run over the lands tool bytes kills every mutant:
               killed == total >= O.mutation_min, 0 survived, 0 broken-pattern
  MUTRECEIPT   the committed lands receipt reports/round-92/mutation-score.txt exists, names
               the same tool sha256 as the live run, and carries the same MUTATION-SCORE
               numbers (routed round-91 D5: the receipt is asserted, not promised)
  STUB         the freeze's stub control, run through the same OKCOUNT check and the same
               mutation pass, is refused (OKCOUNT fails) and kills 0 mutants. The stub
               receipt is produced here, live, never read from prose.

Claim C / coverage - one new linguistics entry and the registry rows it mines.
  MATERIALIZE  as above
  ENTRY        the freeze's v3 tool, entry mode, run over the lands tree with the claim's
               declared arguments, exits 0 and every declared leg prints PASS
               (ENTRY SHAPE TOPIC NEWIDS UNIQUENESS GATE CAPTURE APPENDONLY)
  INDEX        the freeze's tools/check-corpus-index.py exits 0 over the lands tree
  APPENDONLY   no base registry row removed or cell-changed; at least C.new_ids_min new mined
               A/B rows opened on as_of, cited by the entry and naming it in used-by; the
               entry is in corpus/README.md. A malformed row (fewer than 11 cells) is a leg
               FAIL, never a crash (routed round-91 W3).

Receipts carry, below the frozen-leg line: the stamped revision (--lands), the
evaluated revision (the materialized tree), the lane main tip at run time, the
lands tree hash and the counter's own sha256.

Exit 0 pass, 1 finding, 2 refused (bad arguments or unreadable input).
This counter offers no --selftest: each leg is a subprocess over committed
bytes, and the grader it drives ships its own selftest; the do-nothing and
stub controls are run by this counter at the freeze commit and their receipts
are committed under reports/round-92/controls/.
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
    r = subprocess.run(['git', '-C', root, 'archive', '--format=tar', rev], capture_output=True)
    if r.returncode != 0:
        raise Refused(f'git archive {rev} failed: {(r.stderr or b"").decode(errors="replace").strip()}')
    t = subprocess.run(['tar', '-x', '-C', dest], input=r.stdout, capture_output=True)
    if t.returncode != 0:
        raise Refused(f'tar -x failed: {(t.stderr or b"").decode(errors="replace").strip()}')


def sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def legs_emit(legs, label, receipt=None, as_json=False, frozen_line='', stamps=None):
    lines = []
    if frozen_line:
        lines.append(frozen_line)
    if stamps:
        lines.extend(stamps)
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
    return json.loads(git_show(root, freeze, 'reports/round-92/claims.json'))


def count_ok(out):
    return len(re.findall(r'^  ok ', out, re.M))


def run_mutation(root_mat, freeze_root, freeze, work, tool_override=None):
    mut = os.path.join(work, 'mutants-frozen.py')
    with open(mut, 'w') as f:
        f.write(git_show(freeze_root, freeze, 'reports/round-92/mutants.py'))
    mw = os.path.join(work, 'mut-' + ('stub' if tool_override else 'lands'))
    os.makedirs(mw, exist_ok=True)
    out = os.path.join(work, 'mutation-score-' + ('stub' if tool_override else 'lands'))
    cmd = [sys.executable, '-B', mut, '--root', root_mat, '--work', mw, '--out', out]
    if tool_override:
        cmd += ['--tool', tool_override]
    r = sh(cmd)
    return (r.stdout or '') + (r.stderr or '')


MUT_RE = re.compile(r'MUTATION-SCORE: (\d+)/(\d+) killed, (\d+) survived, (\d+) broken-pattern')


def grade_o(root, lands, freeze, work, cfg):
    legs = []
    mat = os.path.join(work, 'mat')
    materialize(root, lands, mat)
    legs.append(('MATERIALIZE', os.path.isdir(os.path.join(mat, 'tools')), f'lands {lands} materialized',
                 mat if os.path.isdir(os.path.join(mat, 'tools')) else 'no tools/ in the archive'))

    tool_rel = 'tools/check-advance-evidence.py'
    tool = os.path.join(mat, tool_rel)
    want = cfg['O']['tool_sha256']
    got = sha256_file(tool) if os.path.isfile(tool) else ''
    legs.append(('TOOL', got == want, f'{tool_rel} sha256 {want}', got or 'absent'))

    st = os.path.join(work, 'st-o')
    os.makedirs(st, exist_ok=True)
    out, rc = '', None
    if os.path.isfile(tool):
        r = sh([sys.executable, '-B', tool, '--selftest', '--work', st])
        out, rc = (r.stdout or '') + (r.stderr or ''), r.returncode
    m = re.search(r'SELFTEST (PASS|FAIL) (\d+)/(\d+)', out)
    total = int(m.group(3)) if m else 0
    ok = bool(m) and rc == 0 and m.group(1) == 'PASS' and total == cfg['O']['selftest_checks']
    legs.append(('SELFTEST', bool(ok), f'rc 0 and SELFTEST PASS {cfg["O"]["selftest_checks"]}/{cfg["O"]["selftest_checks"]}',
                 (m.group(0) if m else (out.strip().splitlines()[-1:] or ['no verdict line'])[0])))

    oks = count_ok(out)
    legs.append(('OKCOUNT', oks == cfg['O']['selftest_checks'],
                 f'exactly {cfg["O"]["selftest_checks"]} lines beginning "  ok "', f'{oks} ok lines'))

    missing = [c for c in cfg['O']['refusal_cases']
               if not re.search(r'^  ok +' + re.escape(c) + r':', out, re.M)]
    legs.append(('REFUSALS', not missing,
                 f'{len(cfg["O"]["refusal_cases"])} named refusal cases each ok',
                 'all ok' if not missing else 'not ok: ' + ', '.join(missing)))

    mout = run_mutation(mat, root, freeze, work)
    mm = MUT_RE.search(mout)
    killed, total_m, survived, broken = (int(x) for x in mm.groups()) if mm else (0, 0, 0, 0)
    ok = bool(mm) and killed == total_m and total_m >= cfg['O']['mutation_min'] and survived == 0 and broken == 0
    legs.append(('MUTATION', ok,
                 f'killed==total>={cfg["O"]["mutation_min"]}, 0 survived, 0 broken-pattern',
                 mm.group(0) if mm else ((mout.strip().splitlines() or ['no score line'])[-1])))

    # MUTRECEIPT (routed round-91 D5): the committed lands receipt exists, names
    # the same tool sha and carries the same mutation numbers as the live run.
    problems = []
    receipt_rel = cfg['O']['mutation_receipt']
    live_sha = got
    txt = ''
    if not os.path.isfile(os.path.join(mat, receipt_rel)):
        problems.append(f'{receipt_rel} absent from the lands tree')
    else:
        txt = open(os.path.join(mat, receipt_rel), encoding='utf-8', errors='replace').read()
        hs = re.search(r'^# tool sha256 ([0-9a-f]{64})$', txt, re.M)
        if not hs or hs.group(1) != live_sha:
            problems.append(f'receipt tool sha {hs.group(1)[:12] if hs else "absent"} != live {live_sha[:12]}')
        rm = MUT_RE.search(txt)
        if not rm:
            problems.append('receipt carries no MUTATION-SCORE line')
        elif mm and rm.groups() != mm.groups():
            problems.append(f'receipt {rm.group(0)} != live {mm.group(0)}')
    legs.append(('MUTRECEIPT', not problems,
                 'committed lands mutation receipt exists with matching tool sha and score',
                 'clean' if not problems else '; '.join(problems)))

    # STUB: the freeze's stub control must be refused by OKCOUNT and kill no mutant.
    stub_path = os.path.join(work, 'stub-tool.py')
    with open(stub_path, 'w') as f:
        f.write(git_show(root, freeze, cfg['O']['stub_control']))
    st2 = os.path.join(work, 'st-stub')
    os.makedirs(st2, exist_ok=True)
    rs = sh([sys.executable, '-B', stub_path, '--selftest', '--work', st2])
    sout = (rs.stdout or '') + (rs.stderr or '')
    stub_oks = count_ok(sout)
    stub_refused_by_okcount = stub_oks != cfg['O']['selftest_checks']
    sm = run_mutation(mat, root, freeze, work, tool_override=stub_path)
    smm = MUT_RE.search(sm)
    stub_killed = int(smm.group(1)) if smm else -1
    ok = stub_refused_by_okcount and stub_killed == 0
    legs.append(('STUB', ok,
                 'stub refused by OKCOUNT (ok lines != selftest_checks) and kills 0 mutants',
                 f'stub ok lines={stub_oks}; stub mutation: {smm.group(0) if smm else "no score line"}'))
    return legs


def registry_rows(text):
    """id -> cells; malformed rows are kept so the caller can fail them as a
    leg finding instead of crashing (routed round-91 W3)."""
    rows = {}
    for line in text.splitlines():
        m = re.match(r'^ {0,3}\|[ ]*(S\d{3,})[ ]*\|', line)
        if m:
            rows[m.group(1)] = [c.strip() for c in line.strip().strip('|').split('|')]
    return rows


def grade_c(root, lands, freeze, work, cfg):
    legs = []
    mat = os.path.join(work, 'mat')
    materialize(root, lands, mat)
    legs.append(('MATERIALIZE', os.path.isdir(os.path.join(mat, 'corpus')), f'lands {lands} materialized',
                 mat if os.path.isdir(os.path.join(mat, 'corpus')) else 'no corpus/ in the archive'))

    c = cfg['C']
    entry_path = os.path.join(mat, c['entry'])
    tool = os.path.join(work, 'tool-frozen.py')
    with open(tool, 'w') as f:
        f.write(git_show(root, freeze, 'tools/check-advance-evidence.py'))
    base_reg = os.path.join(work, 'base-registry.md')
    with open(base_reg, 'w') as f:
        f.write(git_show(root, cfg['base'], 'corpus/SOURCES.md'))
    base_lesson = os.path.join(work, 'base-lesson.md')
    with open(base_lesson, 'w') as f:
        f.write(git_show(root, cfg['base'], cfg['base_lesson']))

    if not os.path.isfile(entry_path):
        legs.append(('ENTRY', False, f'{c["entry"]} exists at lands', 'entry absent at lands'))
    else:
        args = [sys.executable, '-B', tool, 'entry', '--root', mat,
                '--entry', entry_path,
                '--base-registry', base_reg,
                '--lands-registry', os.path.join(mat, 'corpus/SOURCES.md'),
                '--lesson', os.path.join(mat, cfg['lesson']),
                '--manifest', os.path.join(mat, c['manifest']),
                '--capture-dir', c['capture_dir'],
                '--as-of', cfg['as_of'],
                '--topic', c['topic'],
                '--topic-phrases', c['topic_phrases'],
                '--min-topic-phrases', str(c['min_topic_phrases']),
                '--min-bytes', str(c['min_bytes']),
                '--min-headings', str(c['min_headings']),
                '--min-new-ids', str(c['new_ids_min']),
                '--min-topic-overlap', str(c['min_topic_overlap']),
                '--table-min-rows', str(c['table_min_rows']),
                '--table-min-cols', str(c['table_min_cols']),
                '--min-anchor-span', str(c.get('min_anchor_span', 0)),
                '--base-lesson', base_lesson,
                '--graded', 'corpus/SOURCES.md',
                '--graded', cfg['lesson']]
        r = sh(args)
        out = (r.stdout or '') + (r.stderr or '')
        seen = {name: verdict for verdict, name in re.findall(r'^LEG (PASS|FAIL) (\S+)', out, re.M)}
        missing = [l for l in c['legs'] if l not in seen]
        failed = [l for l in c['legs'] if seen.get(l) == 'FAIL']
        ok = r.returncode == 0 and not missing and not failed
        legs.append(('ENTRY', ok, f'entry mode rc 0 with PASS for {",".join(c["legs"])}',
                     'clean' if ok else f'rc={r.returncode} missing={missing} failed={failed}'))

    idx = os.path.join(work, 'check-corpus-index.py')
    with open(idx, 'w') as f:
        f.write(git_show(root, freeze, cfg['C']['index_tool']))
    r = sh([sys.executable, '-B', idx] + [a.replace('{tree}', mat) for a in c['index_args']])
    out = ((r.stdout or '') + (r.stderr or '')).strip()
    legs.append(('INDEX', r.returncode == 0, 'index tool exit 0 over the lands tree',
                 out.splitlines()[-1] if out else 'no output'))

    base_rows = registry_rows(git_show(root, cfg['base'], 'corpus/SOURCES.md'))
    lands_rows = registry_rows(git_show(root, lands, 'corpus/SOURCES.md'))
    problems = []
    for rid, cells in base_rows.items():
        if rid not in lands_rows:
            problems.append(f'{rid} removed')
        elif lands_rows[rid] != cells:
            problems.append(f'{rid} cells changed')
    entry = open(entry_path, encoding='utf-8', errors='replace').read() if os.path.isfile(entry_path) else ''
    cited = set(re.findall(r'\bS\d{3,}\b', entry))
    new_ids = sorted(set(lands_rows) - set(base_rows))
    qualifying = []
    for rid in new_ids:
        cells = lands_rows[rid]
        if len(cells) < 11:
            problems.append(f'{rid}: malformed row ({len(cells)} cells < 11)')
            continue
        tier, status, opened, used = cells[3], cells[7], cells[8], cells[10]
        if tier in ('A', 'B') and status == 'mined' and opened == cfg['as_of'] \
                and os.path.basename(c['entry']) in used and rid in cited:
            qualifying.append(rid)
    for rid, cells in base_rows.items():
        if len(cells) < 11:
            problems.append(f'base {rid}: malformed row ({len(cells)} cells < 11)')
    if len(qualifying) < c['new_ids_min']:
        problems.append(f'{len(qualifying)} qualifying new ids < {c["new_ids_min"]}')
    readme = git_show(root, lands, 'corpus/README.md')
    if os.path.basename(c['entry']) not in readme:
        problems.append('entry absent from corpus/README.md')
    legs.append(('APPENDONLY', not problems,
                 f'no base row changed or malformed; >={c["new_ids_min"]} new mined A/B rows opened {cfg["as_of"]} cited; README row',
                 'clean' if not problems else '; '.join(problems)))
    return legs


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
        args.root = os.path.abspath(args.root)
        if not re.match(r'^[0-9a-f]{40}$', args.lands):
            raise Refused('--lands must be a full 40-hex revision')
        if not os.path.isdir(args.work):
            raise Refused('--work must be an existing directory')
        freeze = args.freeze or ''
        if not re.match(r'^[0-9a-f]{40}$', freeze):
            raise Refused('--freeze <40hex> is required (constants are read from the freeze commit)')
        cfg = claims(args.root, freeze)
        if args.lands == cfg['base']:
            raise Refused('--lands equals the frozen base; a do-nothing landing cannot pass')
        anc = sh(['git', '-C', args.root, 'merge-base', '--is-ancestor', freeze, args.lands])
        if anc.returncode != 0:
            raise Refused(f'--freeze {freeze[:12]} is not an ancestor of --lands {args.lands[:12]}')
        legs = grade_o(args.root, args.lands, freeze, args.work, cfg) if args.claim == 'O' \
            else grade_c(args.root, args.lands, freeze, args.work, cfg)
        names = [n for n, _ok, _e, _o in legs]
        frozen_legs = cfg['legs'][args.claim]
        frozen_line = f'# frozen legs: {len(frozen_legs)} ({",".join(frozen_legs)})'
        if names != frozen_legs:
            raise Refused(f'LEGCOUNT: counter leg table {names} disagrees with the frozen list {frozen_legs}')
        tree = sh(['git', '-C', args.root, 'show', '-s', '--format=%T', args.lands]).stdout.strip()
        tip = sh(['git', '-C', args.root, 'rev-parse', 'refs/heads/main']).stdout.strip()
        counter_sha = sha256_file(os.path.abspath(__file__))
        stamps = [f'# stamped revision: {args.lands}',
                  f'# evaluated revision: {args.lands} (materialized)',
                  f'# measured revision (lane main): {tip}',
                  f'# tree: {tree}',
                  f'# counter sha256 (self): {counter_sha}']
        return legs_emit(legs, f'MEASURE92-{args.claim}', args.receipt, args.json,
                         frozen_line=frozen_line, stamps=stamps)
    except Refused as exc:
        print(f'MEASURE92_ERROR: {exc}', file=sys.stderr)
        return REFUSED


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
