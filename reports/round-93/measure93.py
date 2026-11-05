#!/usr/bin/env python3
"""Round-93 frozen counter: two claims, one instrument.

Usage: measure93.py --root <lane repo> --freeze <40hex> --lands <40hex> --claim O|C --work <existing dir>
                    [--receipt <path>] [--json]

Every constant is read from the freeze commit (reports/round-93/claims.json at
--freeze), never from the graded tree. The lands tree is materialized with
git archive into --work; nothing in the lane is written.

Claim O / operability - grader v4 and its instruments
  MATERIALIZE  the lands archive carries tools/
  TOOL         tools/check-advance-evidence.py sha256 == O.tool_sha256
  SELFTEST     that tool's --selftest exits 0 and prints SELFTEST PASS N/N, N == O.selftest_checks
  OKCOUNT      the selftest prints exactly O.selftest_checks lines beginning `  ok `
  REFUSALS     every O.refusal_cases name is printed as `  ok <name>:`
  STABILITY    O.stability_runs concurrent selftest runs (separate work dirs) each PASS N/N
               (round-92 routed D3: an intermittent 88/89 was never reproduced)
  MUTATION     the freeze-pinned mutants.py run over the lands tool kills every mutant:
               killed == total >= O.mutation_min, 0 survived, 0 broken-pattern
  MUTRECEIPT   the committed lands receipt names the same tool sha and the same numbers
  BATTERY      the round-92 counterfeit battery (frozen builder, run against the lands tool):
               at most O.battery_survivors_max survivors, the survivor is O.battery_survivor_expected,
               every other attack is refused on a named leg or named diagnostic (no traceback),
               the clean controls stay CLEAN and the refused controls stay refused on their leg
  STUB         the round-92 stub control is refused by OKCOUNT and kills 0 mutants

Claim C / coverage - one new linguistics entry and the registry rows it mines
  MATERIALIZE  the lands archive carries corpus/
  ENTRY        the lands tool's entry mode, with the claim's declared arguments, exits 0 and
               every declared leg prints PASS
  POSITIVE     the same tool grades the round-92 landed entry at its lands revision and passes
               it (no regression on a known-good landing)
  INDEX        tools/check-corpus-index.py exits 0 over the lands tree
  CENSUS       scripts/sources-census.sh validate --file <lands SOURCES.md> exits 0
  APPENDONLY   no base registry row removed or cell-changed; >= C.new_ids_min new mined A/B rows
               opened on as_of, cited by the entry, with used-by naming the entry; the entry is
               listed in corpus/README.md

Exit 0 pass, 1 finding, 2 refused (bad arguments or unreadable input).
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

REFUSED = 2
MUT_RE = re.compile(r'MUTATION-SCORE: (\d+)/(\d+) killed, (\d+) survived, (\d+) broken-pattern')
ROW_RE = re.compile(r'^ {0,3}\|[ ]*(S\d{3,})[ ]*\|')
ROOT_PREFIX = 'reports/round-93/'
R92 = 'reports/round-92/'


class Refused(Exception):
    pass


def sh(cmd, cwd=None, env=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env)


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


def count_ok(out):
    return len(re.findall(r'^  ok ', out, re.M))


def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).replace('\u2019', "'")
    return ' '.join(s.split()).casefold()


def registry_rows(text):
    rows = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(1)] = [c.strip() for c in line.strip().strip('|').split('|')]
    return rows


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
    return json.loads(git_show(root, freeze, ROOT_PREFIX + 'claims.json'))


def run_mutation(mat, freeze_root, freeze, work, tool_override=None):
    mut = os.path.join(work, 'mutants-frozen.py')
    with open(mut, 'w') as f:
        f.write(git_show(freeze_root, freeze, ROOT_PREFIX + 'mutants.py'))
    tag = 'stub' if tool_override else 'lands'
    mw = os.path.join(work, 'mut-' + tag)
    os.makedirs(mw, exist_ok=True)
    out = os.path.join(work, 'mutation-score-' + tag)
    cmd = [sys.executable, '-B', mut, '--root', mat, '--work', mw, '--out', out]
    if tool_override:
        cmd += ['--tool', tool_override]
    r = sh(cmd)
    return (r.stdout or '') + (r.stderr or '')


def battery(mat, work, cfg):
    """Run the frozen round-92 counterfeit battery against the lands tool; return
    (ok, observed) for the BATTERY leg."""
    src_path = os.path.join(mat, 'reports/round-93/battery93.py')
    if not os.path.isfile(src_path):
        return False, 'battery93.py absent from the lands tree'
    bw = os.path.join(work, 'battery-work')
    os.makedirs(bw, exist_ok=True)
    env = dict(os.environ, R93_ROOT=mat, R93_WORK=bw, PYTHONDONTWRITEBYTECODE='1')
    r = sh([sys.executable, '-B', src_path], env=env)
    out = (r.stdout or '') + (r.stderr or '')
    rows = []
    apath = os.path.join(bw, 'attacks.md')
    if os.path.isfile(apath):
        rows = [l for l in open(apath, encoding='utf-8').read().splitlines() if re.match(r'^\| [A-Z]\d[a-z]?\s*\|', l)]
    if not rows:
        return False, f'battery produced no attack table (rc={r.returncode}): {out.strip()[-200:]}'
    survivors = [l.split('|')[1].strip() for l in rows if '| SURVIVOR |' in l]
    refused_unnamed = [l.split('|')[1].strip() for l in rows
                       if 'refused-unnamed' in l and 'rc=1' in l]
    ctrl_fail = []
    for l in rows:
        cid = l.split('|')[1].strip()
        if cid in cfg['battery_controls_clean'] and '| CLEAN |' not in l:
            ctrl_fail.append(cid)
        if cid in cfg['battery_controls_refused'] and f"refused on {cfg['battery_controls_refused'][cid]}" not in l:
            ctrl_fail.append(cid)
    problems = []
    if len(survivors) > cfg['battery_survivors_max']:
        problems.append(f'survivors {",".join(survivors)} > {cfg["battery_survivors_max"]}')
    if survivors and survivors != [cfg['battery_survivor_expected']]:
        problems.append(f'survivor {",".join(survivors)} is not {cfg["battery_survivor_expected"]}')
    if refused_unnamed:
        problems.append('unnamed refusal (traceback): ' + ','.join(refused_unnamed))
    if ctrl_fail:
        problems.append('control drift: ' + ','.join(ctrl_fail))
    named = len(rows) - len(survivors) - len(refused_unnamed)
    observed = f'{len(rows)} attacks: survivors={",".join(survivors) or "none"} named-refusals={named} ' \
               f'unnamed={len(refused_unnamed)}' + ('' if not problems else ' | ' + '; '.join(problems))
    return not problems, observed


def grade_o(root, lands, freeze, work, cfg):
    legs = []
    mat = os.path.join(work, 'mat')
    materialize(root, lands, mat)
    legs.append(('MATERIALIZE', os.path.isdir(os.path.join(mat, 'tools')), f'lands {lands} materialized',
                 mat if os.path.isdir(os.path.join(mat, 'tools')) else 'no tools/ in the archive'))

    tool = os.path.join(mat, 'tools/check-advance-evidence.py')
    want = cfg['O']['tool_sha256']
    got = sha256_file(tool) if os.path.isfile(tool) else ''
    legs.append(('TOOL', got == want, f'tools/check-advance-evidence.py sha256 {want}', got or 'absent'))

    st = os.path.join(work, 'st-o')
    os.makedirs(st, exist_ok=True)
    out, rc = '', None
    if os.path.isfile(tool):
        r = sh([sys.executable, '-B', tool, '--selftest', '--work', st])
        out, rc = (r.stdout or '') + (r.stderr or ''), r.returncode
    m = re.search(r'SELFTEST (PASS|FAIL) (\d+)/(\d+)', out)
    total = int(m.group(3)) if m else 0
    n = cfg['O']['selftest_checks']
    ok = bool(m) and rc == 0 and m.group(1) == 'PASS' and total == n
    legs.append(('SELFTEST', bool(ok), f'rc 0 and SELFTEST PASS {n}/{n}',
                 (m.group(0) if m else (out.strip().splitlines() or ['no verdict line'])[-1])))

    oks = count_ok(out)
    legs.append(('OKCOUNT', oks == cfg['O']['ok_lines_expected'],
                 f'exactly {cfg["O"]["ok_lines_expected"]} lines beginning "  ok "', f'{oks} ok lines'))

    missing = [c for c in cfg['O']['refusal_cases']
               if not re.search(r'^  ok +' + re.escape(c) + r':', out, re.M)]
    legs.append(('REFUSALS', not missing,
                 f'{len(cfg["O"]["refusal_cases"])} named refusal cases each ok',
                 'all ok' if not missing else 'not ok: ' + ', '.join(missing)))

    runs = []
    stdir = os.path.join(work, 'stability')
    os.makedirs(stdir, exist_ok=True)
    procs = []
    for i in range(cfg['O']['stability_runs']):
        d = os.path.join(stdir, f'run{i}')
        os.makedirs(d, exist_ok=True)
        procs.append(subprocess.Popen([sys.executable, '-B', tool, '--selftest', '--work', d],
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
    for p in procs:
        so, se = p.communicate()
        mm = re.search(r'SELFTEST (PASS|FAIL) (\d+)/(\d+)', so or '')
        runs.append(f'rc={p.returncode} {mm.group(0) if mm else "no verdict"}')
    stab_ok = all(x == f'rc=0 SELFTEST PASS {n}/{n}' for x in runs)
    legs.append(('STABILITY', stab_ok, f'{cfg["O"]["stability_runs"]} concurrent selftests, each rc 0 and PASS {n}/{n}',
                 '; '.join(runs)))

    mout = run_mutation(mat, root, freeze, work)
    mm = MUT_RE.search(mout)
    killed, total_m, survived, broken = (int(x) for x in mm.groups()) if mm else (0, 0, 0, 0)
    ok = bool(mm) and killed == total_m and total_m >= cfg['O']['mutation_min'] and survived == 0 and broken == 0
    legs.append(('MUTATION', ok, f'killed==total>={cfg["O"]["mutation_min"]}, 0 survived, 0 broken-pattern',
                 mm.group(0) if mm else ((mout.strip().splitlines() or ['no score line'])[-1])))

    problems = []
    receipt_rel = cfg['O']['mutation_receipt']
    txt = ''
    if not os.path.isfile(os.path.join(mat, receipt_rel)):
        problems.append(f'{receipt_rel} absent from the lands tree')
    else:
        txt = open(os.path.join(mat, receipt_rel), encoding='utf-8', errors='replace').read()
        hs = re.search(r'^# tool sha256 ([0-9a-f]{64})$', txt, re.M)
        if not hs or hs.group(1) != got:
            problems.append(f'receipt tool sha {hs.group(1)[:12] if hs else "absent"} != live {got[:12]}')
        rm = MUT_RE.search(txt)
        if not rm:
            problems.append('receipt carries no MUTATION-SCORE line')
        elif mm and rm.groups() != mm.groups():
            problems.append(f'receipt {rm.group(0)} != live {mm.group(0)}')
    legs.append(('MUTRECEIPT', not problems, 'committed lands mutation receipt names the live tool sha and score',
                 'clean' if not problems else '; '.join(problems)))

    bok, bobs = battery(mat, work, cfg['O'])
    legs.append(('BATTERY', bok, f'<= {cfg["O"]["battery_survivors_max"]} survivor ({cfg["O"]["battery_survivor_expected"]}); '
                 'every other attack refused on a named leg or diagnostic; controls hold', bobs))

    stub_path = os.path.join(work, 'stub-tool.py')
    with open(stub_path, 'w') as f:
        f.write(git_show(root, freeze, cfg['O']['stub_control']))
    st2 = os.path.join(work, 'st-stub')
    os.makedirs(st2, exist_ok=True)
    rs = sh([sys.executable, '-B', stub_path, '--selftest', '--work', st2])
    sout = (rs.stdout or '') + (rs.stderr or '')
    stub_oks = count_ok(sout)
    stub_refused = stub_oks != n
    sm = run_mutation(mat, root, freeze, work, tool_override=stub_path)
    smm = MUT_RE.search(sm)
    stub_killed = int(smm.group(1)) if smm else -1
    legs.append(('STUB', stub_refused and stub_killed == 0,
                 'stub refused by OKCOUNT and kills 0 mutants',
                 f'stub ok lines={stub_oks}; stub mutation: {smm.group(0) if smm else "no score line"}'))
    return legs


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
        f.write(git_show(root, cfg['base'], 'corpus/lessons/round-92.md'))

    def entry_args(entry_file, lesson_file, manifest_file, capture_dir, topic, phrases, min_bytes, min_heads,
                   min_overlap, table_rows, table_cols, min_span, min_phrases, new_ids, lands_registry):
        return [sys.executable, '-B', tool, 'entry', '--root', mat, '--entry', entry_file,
                '--base-registry', base_reg, '--lands-registry', lands_registry,
                '--lesson', lesson_file, '--manifest', manifest_file, '--capture-dir', capture_dir,
                '--as-of', cfg['as_of'], '--topic', topic, '--topic-phrases', phrases,
                '--min-topic-phrases', str(min_phrases), '--min-bytes', str(min_bytes),
                '--min-headings', str(min_heads), '--min-new-ids', str(new_ids),
                '--min-topic-overlap', str(min_overlap), '--table-min-rows', str(table_rows),
                '--table-min-cols', str(table_cols), '--min-anchor-span', str(min_span),
                '--base-lesson', base_lesson, '--graded', 'corpus/SOURCES.md', '--graded', c['lesson'],
                '--min-gate-overlap', '3']

    def legs_of(out_text, rc, expected_legs):
        seen = {name: verdict for verdict, name in re.findall(r'^LEG (PASS|FAIL) (\S+)', out_text, re.M)}
        missing = [l for l in expected_legs if l not in seen]
        failed = [l for l in expected_legs if seen.get(l) == 'FAIL']
        return rc == 0 and not missing and not failed, f'rc={rc} missing={missing} failed={failed}'

    if not os.path.isfile(entry_path):
        legs.append(('ENTRY', False, f'{c["entry"]} exists at lands', 'entry absent at lands'))
    else:
        r = sh(entry_args(entry_path, os.path.join(mat, c['lesson']), os.path.join(mat, c['manifest']),
                          c['capture_dir'], c['topic'], c['topic_phrases'], c['min_bytes'], c['min_headings'],
                          c['min_topic_overlap'], c['table_min_rows'], c['table_min_cols'],
                          c.get('min_anchor_span', 0), c['min_topic_phrases'], c['new_ids_min'],
                          os.path.join(mat, 'corpus/SOURCES.md')))
        out = (r.stdout or '') + (r.stderr or '')
        ok, obs = legs_of(out, r.returncode, c['legs_entry'])
        legs.append(('ENTRY', ok, f'entry mode rc 0 with PASS for {",".join(c["legs_entry"])}',
                     'clean' if ok else obs))

    # POSITIVE: the lands tool grades the round-92 landed entry at its own landing revision
    pos = cfg['C']['positive']
    pos_mat = os.path.join(work, 'mat-r92')
    materialize(root, pos['lands'], pos_mat)
    pos_entry = os.path.join(pos_mat, pos['entry'])
    pos_lesson = os.path.join(pos_mat, pos['lesson'])
    pos_man = os.path.join(pos_mat, pos['manifest'])
    pos_base_reg = os.path.join(work, 'r92-base-registry.md')
    with open(pos_base_reg, 'w') as f:
        f.write(git_show(root, pos['base'], 'corpus/SOURCES.md'))
    pos_base_lesson = os.path.join(work, 'r92-base-lesson.md')
    with open(pos_base_lesson, 'w') as f:
        f.write(git_show(root, pos['base'], pos['base_lesson']))
    pa = [sys.executable, '-B', tool, 'entry', '--root', pos_mat, '--entry', pos_entry,
          '--base-registry', pos_base_reg, '--lands-registry', os.path.join(pos_mat, 'corpus/SOURCES.md'),
          '--lesson', pos_lesson, '--manifest', pos_man, '--capture-dir', pos['capture_dir'],
          '--as-of', pos['as_of'], '--topic', pos['topic'], '--topic-phrases', pos['topic_phrases'],
          '--min-topic-phrases', str(pos['min_topic_phrases']), '--min-bytes', str(pos['min_bytes']),
          '--min-headings', str(pos['min_headings']), '--min-new-ids', str(pos['new_ids_min']),
          '--min-topic-overlap', str(pos['min_topic_overlap']), '--table-min-rows', str(pos['table_min_rows']),
          '--table-min-cols', str(pos['table_min_cols']), '--min-anchor-span', str(pos['min_anchor_span']),
          '--base-lesson', pos_base_lesson, '--graded', 'corpus/SOURCES.md', '--graded', pos['lesson'],
          '--min-gate-overlap', '3']
    rp = sh(pa)
    pout = (rp.stdout or '') + (rp.stderr or '')
    pok, pobs = legs_of(pout, rp.returncode, pos['legs'])
    legs.append(('POSITIVE', pok, f'v4 entry mode passes the round-92 landed entry at {pos["lands"][:12]} ({",".join(pos["legs"])})',
                 'clean' if pok else pobs))

    idx = os.path.join(work, 'check-corpus-index.py')
    with open(idx, 'w') as f:
        f.write(git_show(root, freeze, c['index_tool']))
    r = sh([sys.executable, '-B', idx] + [a.replace('{tree}', mat) for a in c['index_args']])
    out = ((r.stdout or '') + (r.stderr or '')).strip()
    legs.append(('INDEX', r.returncode == 0, 'index tool exit 0 over the lands tree',
                 out.splitlines()[-1] if out else 'no output'))

    lands_sources = os.path.join(mat, 'corpus/SOURCES.md')
    census_tool = c['census_tool']  # the fleet-root census script (read-only, outside the lane)
    rc_census = sh([census_tool, 'validate', '--file', lands_sources]) if os.path.isfile(census_tool) else None
    legs.append(('CENSUS', rc_census is not None and rc_census.returncode == 0,
                 'scripts/sources-census.sh validate --file <lands SOURCES.md> exits 0',
                 'absent' if rc_census is None else f'rc={rc_census.returncode}'))

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
    readme = git_show(root, lands, c['readme'])
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
        return legs_emit(legs, f'MEASURE93-{args.claim}', args.receipt, args.json,
                         frozen_line=frozen_line, stamps=stamps)
    except Refused as exc:
        print(f'MEASURE93_ERROR: {exc}', file=sys.stderr)
        return REFUSED


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
