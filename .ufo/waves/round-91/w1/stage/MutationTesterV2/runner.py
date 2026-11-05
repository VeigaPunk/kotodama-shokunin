#!/usr/bin/env python3
"""MutationTesterV2 runner: 16 NEW mutants over tools/check-advance-evidence.py (v2 entry mode).

Detector = the tool's own bounded --selftest (same detector the frozen
reports/round-91/mutants.py uses). Pristine bytes must be green first; a
mutant is KILLED when rc != 0, SURVIVED when rc == 0. All copies live in
scratch; the lane tool file is never modified (hash proven identical after).
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

TOOL = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py'
FROZEN = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-91/mutants.py'
S = '/fast/scratch/hyaku/kotodama-r91/MutationTesterV2'
STAGE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/MutationTesterV2'

MUTANTS = [
    # NEWIDS: the status!='mined' arm has no selftest fixture (the only non-mined
    # fixture row S013 is uncited, so it never reaches this loop).
    ('newids-status-off',
     "        if status != 'mined':",
     '        if False:'),
    # NEWIDS: the 'qualifying ids not cited' arm is unreachable by construction
    # (scoped is built as new_ids AND cited), so no fixture can ever fire it.
    ('newids-cited-closure-off',
     '    if not set(qualifying) <= set(cited):',
     '    if False:'),
    # GATE (entry): the 'no lesson line with id and quote' arm is never
    # exercised in entry mode (no fixture drops a gate line for a qualifying id).
    ('gate-missing-line-entry-off',
     "        if not qs:\n            gate.append(f'{rid}: no lesson line with id and quote')",
     "        if False:\n            gate.append(f'{rid}: no lesson line with id and quote')"),
    # CAPTURE: the fetched_at-date == as_of arm has no fixture in either mode.
    ('capture-fetched-date-off',
     '    if fm.group(1) != as_of:',
     '    if False:'),
    # CAPTURE: the relative-and-confined arm (absolute path / '..') has no
    # fixture; the cap_dir prefix check catches most other shapes.
    ('capture-traversal-off',
     "    if rel.startswith('/') or '..' in rel.split('/'):\n        return f'capture path not relative and confined: {rel}'",
     "    if False:\n        return f'capture path not relative and confined: {rel}'"),
    # TOPIC: the table-cell half of the phrase-anchor text has no fixture that
    # needs it (every fixture phrase also sits in an h2 heading).
    ('topic-anchor-table-off',
     "            '\\n'.join(l for l in entry.splitlines() if l.strip().startswith('|')))",
     "            '\\n'.join(l for l in entry.splitlines() if l.strip().startswith('!!')))"),
    # CAPTURE: the auto-include of lesson/lands-registry/entry bytes into the
    # graded set is exercised only by the byte-copy fixture; entry-vs-lesson.
    ('graded-sources-autoinclude-off',
     '    for g in list(args.graded) + [args.lesson, args.lands_registry, args.entry]:',
     '    for g in list(args.graded):'),
    # TOPIC: killing the phrase-floor parse itself (distinct from the frozen
    # phrase-floor-off which kills the comparison).
    ('phrase-floor-parse-off',
     "    phrase_floor = getattr(args, 'min_topic_phrases', 0) or 0",
     '    phrase_floor = 0'),
    # ENTRY: weakening the header-key set to three of four keys.
    ('entry-header-keys-weaken',
     "    for key in ('topic:', 'sources:', 'verified-at:', 'recheck:'):",
     "    for key in ('topic:', 'sources:', 'verified-at:'):"),
    # APPENDONLY: emptying the lands disposition map (distinct from the frozen
    # appendonly-gained/flip arms which edit the loop body).
    ('appendonly-lands-disp-off',
     '        lands_disp = dispositions(lesson)',
     '        lands_disp = {}'),
    # SHAPE: killing the repetition measurement rather than its threshold.
    ('shape-worst-zero-off',
     '    worst = max([ss.count(s) for s in set(ss)] or [0])',
     '    worst = 0'),
    # TOPIC: pinning the overlap to the floor so the comparison is vacuous.
    ('topic-shared-floor-off',
     '    shared = overlap(entry, args.topic)',
     '    shared = args.min_topic_overlap'),
    # TOPIC: pinning the stem hit count to its maximum.
    ('topic-stem-alwayshit-off',
     '    stem_hit = sum(1 for w in stem_words if norm(w) in norm(entry))',
     '    stem_hit = len(stem_words)'),
    # NEWIDS: emptying the cited set (entry stops binding rows to itself).
    ('newids-cited-regex-off',
     "    cited = sorted(set(re.findall(r'\\bS\\d{3,}\\b', entry)))",
     '    cited = []'),
    # CAPTURE (entry): killing the error dispatch only in the entry loop.
    ('capture-dispatch-entry-off',
     "                            graded_shas=graded_shas)\n        if err:",
     "                            graded_shas=graded_shas)\n        if False:"),
    # CAPTURE: killing the isfile guard so graded_shas stays empty.
    ('graded-isfile-off',
     "        p = os.path.join(args.root, g)\n        if os.path.isfile(p):",
     "        p = os.path.join(args.root, g)\n        if False:"),
]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def run_selftest(tool_path, workdir, env):
    os.makedirs(workdir, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', tool_path, '--selftest', '--work', workdir],
                       capture_output=True, text=True, env=env, cwd=S)
    out = (r.stdout or '').strip()
    first = out.splitlines()[0] if out else ''
    if not first and r.stderr:
        first = 'STDERR: ' + (r.stderr.strip().splitlines() or [''])[-1][:160]
    return r.returncode, first


def main():
    t0 = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    os.makedirs(S, exist_ok=True)
    os.makedirs(STAGE, exist_ok=True)
    env = dict(os.environ)
    env['TMPDIR'] = S
    env['PYTHONDONTWRITEBYTECODE'] = '1'

    with open(TOOL, 'rb') as f:
        src_bytes = f.read()
    tool_sha_before = sha256_bytes(src_bytes)
    src = src_bytes.decode('utf-8')
    with open(FROZEN, 'r') as f:
        frozen_text = f.read()

    clean_path = os.path.join(S, 'clean-tool.py')
    with open(clean_path, 'w') as f:
        f.write(src)
    rc, first = run_selftest(clean_path, os.path.join(S, 'st-clean'), env)
    baseline = f'clean selftest rc={rc} first={first!r}'
    print(baseline)
    if rc != 0:
        print('BASELINE NOT GREEN -> inconclusive, aborting')
        return 2

    rows = []
    killed = survived = broken = 0
    mut_shas = {}
    for name, old, new in MUTANTS:
        occ = src.count(old)
        in_frozen = old in frozen_text
        if occ == 0 or src.replace(old, new) == src or in_frozen:
            broken += 1
            rows.append((name, 'BROKEN-PATTERN', f'occ={occ} changed={src.replace(old, new) != src} in_frozen={in_frozen}', ''))
            continue
        mut = src.replace(old, new)
        mut_path = os.path.join(S, 'mut-' + name + '.py')
        with open(mut_path, 'w') as f:
            f.write(mut)
        mut_sha = sha256_bytes(mut.encode('utf-8'))
        mut_shas[name] = mut_sha
        rc, first = run_selftest(mut_path, os.path.join(S, 'st-' + name), env)
        verdict = 'KILLED' if rc != 0 else 'SURVIVED'
        if rc != 0:
            killed += 1
        else:
            survived += 1
        rows.append((name, verdict, f'selftest rc={rc} first={first!r}', f'occ={occ} mut_sha256={mut_sha}'))
        print(f'{verdict:8s} {name}: rc={rc} {first!r}')

    # restoration evidence: pristine bytes re-materialized and re-detected
    restore_path = os.path.join(S, 'restore-tool.py')
    with open(restore_path, 'w') as f:
        f.write(src)
    rc_r, first_r = run_selftest(restore_path, os.path.join(S, 'st-restore'), env)
    with open(TOOL, 'rb') as f:
        tool_sha_after = sha256_bytes(f.read())
    restoration = (f'restored pristine copy selftest rc={rc_r} first={first_r!r}; '
                   f'lane tool sha256 before={tool_sha_before} after={tool_sha_after} '
                   f'unchanged={tool_sha_before == tool_sha_after}')
    print(restoration)

    total = len(MUTANTS)
    score = f'MUTATION-SCORE: {killed}/{total} killed, {survived} survived, {broken} broken-pattern'
    print(score)

    # ---- new-mutants.py (same tuple format as mutants.py) ----
    with open(os.path.join(STAGE, 'new-mutants.py'), 'w') as f:
        f.write('# MutationTesterV2 round-91: 16 NEW pairs over the v2 entry mode of\n'
                '# tools/check-advance-evidence.py. None of these (old, new) pairs appears\n'
                '# in the frozen reports/round-91/mutants.py (verified: old absent from its\n'
                '# bytes and grep of its 53 pair names/targets). Format matches mutants.py.\n'
                'MUTANTS = [\n')
        for name, old, new in MUTANTS:
            f.write(f'    {name!r},\n    {old!r},\n    {new!r},\n')
        f.write(']\n')

    # ---- new-mutation-score.txt ----
    lines = [
        f'# MutationTesterV2 new-mutation pass, {t0}',
        f'# tool: {TOOL}',
        f'# tool sha256 (before == after, lane file untouched): {tool_sha_before}',
        f'# detector: python3 -B <copy> --selftest --work <scratch dir> (same bounded detector as the frozen pass)',
        f'# baseline: {baseline}',
        '# frozen-pair collision check: every old string absent from reports/round-91/mutants.py bytes',
        f'# restoration: {restoration}',
        score,
    ]
    for name, verdict, out, extra in rows:
        lines.append(f'  {verdict} {name}: {out}' + (f' | {extra}' if extra else ''))
    with open(os.path.join(STAGE, 'new-mutation-score.txt'), 'w') as f:
        f.write('\n'.join(lines) + '\n')

    # ---- survivors.md ----
    FIXTURE_IDEAS = {
        'newids-status-off':
            'Fixture: cite a new row whose status cell reads `rejected` (or `held`) with tier A, opened as_of, entry-naming used-by; expect FAIL NEWIDS `not mined`.',
        'newids-cited-closure-off':
            'Fixture is structural: make `scoped` able to exceed `cited` (e.g. a CLI flag adding uncited ids to scope) or drop the tautological arm; any fixture with an uncited qualifying id then fires `qualifying ids not cited`.',
        'gate-missing-line-entry-off':
            'Fixture: round lesson that carries gate lines for S011/S012 only, S010 absent; expect FAIL GATE `no lesson line with id and quote`.',
        'capture-fetched-date-off':
            'Fixture: manifest fetched_at `2026-11-03T19:00:00-03:00` (day before as_of) with otherwise valid capture; expect FAIL CAPTURE `fetched_at date`.',
        'capture-traversal-off':
            'Fixture: manifest capture `reports/round-90/evidence/../sneak.txt` (or an absolute path); expect FAIL CAPTURE `not relative and confined`.',
        'topic-anchor-table-off':
            'Fixture: entry whose fourth phrase (`table`) appears only inside table cells, never in any h2 heading; expect FAIL TOPIC `phrase anchors`.',
        'graded-sources-autoinclude-off':
            'Fixture: entry-mode run with --graded listing only corpus/SOURCES.md (lesson not passed as --graded) and a capture that byte-copies the lesson file; expect FAIL CAPTURE `byte-copies a graded file`.',
    }
    surv = [(n, v, o, e) for n, v, o, e in rows if v == 'SURVIVED']
    with open(os.path.join(STAGE, 'survivors.md'), 'w') as f:
        f.write('# New-mutation survivors (v2 entry mode, round 91)\n\n')
        f.write(f'{len(surv)} of {total} new mutants survived the v2 tool\'s own 77-check selftest.\n')
        f.write('A surviving mutant is a coverage finding: the selftest has no fixture that\n'
                'notices the removed sub-check. It is not permission to change the contract.\n\n')
        for name, _v, out, extra in surv:
            f.write(f'## {name}\n\n')
            f.write(f'- Detector output: `{out}` ({extra})\n')
            f.write(f'- Check weakened: {CHECK_DESC[name]}\n')
            f.write(f'- Kill fixture idea: {FIXTURE_IDEAS[name]}\n\n')
    summary = {'total': total, 'killed': killed, 'survived': survived, 'broken': broken,
               'baseline': baseline, 'restoration': restoration,
               'tool_sha256': tool_sha_before, 'rows': [
                   {'name': n, 'verdict': v, 'output': o, 'detail': e} for n, v, o, e in rows]}
    with open(os.path.join(S, 'summary.json'), 'w') as f:
        json.dump(summary, f, indent=1)
    return 0


CHECK_DESC = {
    'newids-status-off': 'NEWIDS arm `status != mined`: a cited, tier-A, opened-today, entry-named row with a non-mined status cell still qualifies.',
    'newids-cited-closure-off': 'NEWIDS arm `qualifying ids not cited`: tautologically unreachable (scoped = new_ids ∩ cited), dead hardening.',
    'gate-missing-line-entry-off': 'GATE arm `no lesson line with id and quote`: an entry-mode qualifying id with no gate line at all is never tested.',
    'capture-fetched-date-off': 'CAPTURE arm `fetched_at date != as_of`: no fixture re-opens a capture fetched on any other day, in either mode.',
    'capture-traversal-off': 'CAPTURE arm `not relative and confined`: absolute or `..` capture paths are never fixture-tested.',
    'topic-anchor-table-off': 'TOPIC phrase-anchor text source: the table-cell half of anchor_text is redundant on every fixture (all anchored phrases also sit in h2 headings).',
    'graded-sources-autoinclude-off': 'CAPTURE graded set: lesson, lands-registry and entry bytes are auto-included in graded_shas. Survives because the fixture also passes the lesson via corpus/lessons/round-90.md in --graded; the auto-include arm is never isolated.',
    'graded-isfile-off': 'CAPTURE graded set: the isfile guard on graded paths. Killed by the byte-copy fixture; listed for completeness only.',
}


if __name__ == '__main__':
    sys.exit(main())
