#!/usr/bin/env python3
"""Round-90 separability harness: claims O and C are causally separable.

    python3 -B reports/round-90/separability90.py --repo <lane> \
        --freeze <40hex> --lands <40hex> --work <existing-dir> \
        [--expect O=PASS,C=FAIL] [--negative] [--receipt PATH]

Claim O (operability) and claim C (coverage) are graded by one frozen counter,
reports/round-90/measure90.py, whose legs read disjoint sets of graded paths.
This harness proves the disjointness is causal, not rhetorical: it materializes
the lands revision with `git archive` (binary tar stream, no checkout), builds
one overlay sandbox per claim that carries ONLY that claim's paths, and runs the
freeze-pinned counter against each overlay.

  overlay O  tools/check-advance-evidence.py, reports/round-90/mutants.py,
             reports/round-90/mutation-score.{txt,json},
             reports/round-90/controls/stub-tool.txt,
             reports/round-90/claims.json, reports/round-90/measure90.py
  overlay C  the claim's entry, corpus/SOURCES.md, corpus/lessons/round-90.md,
             reports/round-90/evidence/, corpus/README.md,
             reports/round-90/claims.json, reports/round-90/measure90.py,
             tools/check-advance-evidence.py (instrument only),
             tools/check-corpus-index.py

Each overlay is a git repository whose object database is an alternate of the
lane's (read-only, no fetch, no lane mutation) and whose single overlay commit
has the lands commit as parent. `git ls-tree` of that commit is asserted to be
exactly the selected paths, so the sandbox cannot smuggle in a sibling path.

Two declared, non-graded extras, both reported on stdout:

  * O_STRUCTURAL  corpus/.overlay-keep (0 bytes). measure90's MATERIALIZE leg
    tests os.path.isdir(mat/corpus) for both claims; git cannot store an empty
    directory, so overlay O carries one empty marker under corpus/. No O leg
    reads it and it is not any claim's graded path.
  * C_SUBSTRATE   corpus/knowledge/** (the other entries). Claim C's INDEX leg
    runs tools/check-corpus-index.py, which counts every partition file against
    corpus/README.md; without the tree the leg fails on MISSING_ROW/HEADER_DRIFT
    for reasons unrelated to C. These files are not O's graded paths and no O
    leg reads them. `--no-substrate` turns the extra off to show the leg fail.

Verdicts: each overlay prints the counter's own verdict line
(`MEASURE90-O: PASS legs=6/6`). The harness prints, for each overlay, which of
the other claim's graded paths were absent from its sandbox.

Exit 0 only when both claims pass in their own overlay, the two overlays are
disjoint, and (with --negative) every deletion proof fails as required. --expect
does not weaken a claim: it renames the exit predicate to "the observed verdicts
equal this requested pattern", which is how the at-freeze demonstration
(O=PASS,C=FAIL) is asserted; the counter's own verdict lines and the CLAIMS: line
always report the truth. Exit 1 on any mismatch, 2 on refused input.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

REFUSED = 2

CLAIMS = 'reports/round-90/claims.json'
MEASURE = 'reports/round-90/measure90.py'
TOOL = 'tools/check-advance-evidence.py'
SHARED = (CLAIMS, MEASURE, TOOL)

O_PATHS = (
    TOOL,
    'reports/round-90/mutants.py',
    'reports/round-90/mutation-score.txt',
    'reports/round-90/mutation-score.json',
    'reports/round-90/controls/stub-tool.txt',
    CLAIMS,
    MEASURE,
)
O_STRUCTURAL = ('corpus/.overlay-keep',)
C_SUBSTRATE = ('corpus/knowledge',)


class Refused(Exception):
    pass


def sh(cmd, cwd=None, input=None, env=None):
    return subprocess.run(cmd, cwd=cwd, input=input, capture_output=True, env=env)


def dec(b):
    return b.decode('utf-8', errors='replace') if isinstance(b, bytes) else (b or '')


def need(res, what):
    if res.returncode != 0:
        raise Refused(f'{what}: rc={res.returncode} {dec(res.stderr).strip()[:400]}')
    return res.stdout


def git(root, *args, input=None):
    return sh(['git', '-C', root, *args], input=input)


def git_show(root, rev, path):
    return dec(need(git(root, 'show', f'{rev}:{path}'), f'git show {rev}:{path}'))


def counter_source(repo, counter):
    """One instrument for both overlays, pinned by sha256.

    The counter is versioned by reports/round-90/counter-revisions.md: the freeze
    holds revision 1, which refuses (rc2) instead of failing a leg when the entry
    is absent. Revisions 2-6 changed only absent-artifact branches, never a leg
    name, threshold or constant, so the harness runs the lane's current instrument
    (the worktree file, or an explicit 40-hex revision) and prints which documented
    revision it is. claims.json stays read from --freeze in every run.
    """
    if re.match(r'^[0-9a-f]{40}$', counter or ''):
        raw = need(git(repo, 'show', f'{counter}:{MEASURE}'), f'git show {counter}:{MEASURE}')
        source = counter
    else:
        path = os.path.join(repo, MEASURE)
        if not os.path.isfile(path):
            raise Refused(f'{MEASURE} is absent from {repo}')
        with open(path, 'rb') as f:
            raw = f.read()
        source = 'worktree'
    sha = hashlib.sha256(raw).hexdigest()
    revs = {}
    table = os.path.join(repo, 'reports/round-90/counter-revisions.md')
    if os.path.isfile(table):
        with open(table, encoding='utf-8') as f:
            for line in f:
                m = re.match(r'^\|\s*(\d+)\s*\|\s*`([0-9a-f]{64})`', line)
                if m:
                    revs[m.group(2)] = int(m.group(1))
    return raw, sha, source, revs.get(sha)


def claim_cfg(repo, freeze):
    try:
        cfg = json.loads(git_show(repo, freeze, CLAIMS))
    except json.JSONDecodeError as exc:
        raise Refused(f'{CLAIMS} at {freeze} is not JSON: {exc}')
    for key in ('O', 'C'):
        if key not in cfg:
            raise Refused(f'{CLAIMS} at {freeze} has no {key} claim')
    return cfg


def c_paths(cfg):
    c = cfg['C']
    return (c['entry'], 'corpus/SOURCES.md', cfg['lesson'], c['capture_dir'],
            'corpus/README.md', CLAIMS, MEASURE, TOOL, c['index_tool'])


def archive_lane(lane, rev, dest):
    """Materialize `rev` with git archive as a binary tar stream."""
    os.makedirs(dest, exist_ok=True)
    ar = sh(['git', '-C', lane, 'archive', '--format=tar', rev])
    if ar.returncode != 0:
        raise Refused(f'git archive {rev}: rc={ar.returncode} {dec(ar.stderr).strip()[:400]}')
    if not ar.stdout:
        raise Refused(f'git archive {rev} produced no bytes')
    t = sh(['tar', '-x', '-C', dest], input=ar.stdout)
    if t.returncode != 0:
        raise Refused(f'tar -x of the {rev} archive: rc={t.returncode} {dec(t.stderr).strip()[:400]}')
    return len(ar.stdout)


def copy_entry(src, dest, rel):
    target = os.path.join(dest, rel)
    os.makedirs(os.path.dirname(target) or dest, exist_ok=True)
    if os.path.islink(os.path.join(src, rel)):
        if os.path.lexists(target):
            os.unlink(target)
        os.symlink(os.readlink(os.path.join(src, rel)), target)
    else:
        shutil.copy2(os.path.join(src, rel), target)


def select(src, dest, specs):
    """Copy only `specs` (files or directory trees) out of the materialized tree."""
    present, absent = [], []
    for spec in specs:
        path = os.path.join(src, spec)
        if os.path.isdir(path):
            found = False
            for dirpath, _dirnames, filenames in os.walk(path):
                for name in sorted(filenames):
                    full = os.path.join(dirpath, name)
                    rel = os.path.relpath(full, src)
                    copy_entry(src, dest, rel)
                    present.append(rel)
                    found = True
            if not found:
                absent.append(spec)
        elif os.path.exists(path) or os.path.islink(path):
            copy_entry(src, dest, spec)
            present.append(spec)
        else:
            absent.append(spec)
    return sorted(present), sorted(absent)


def init_overlay(path, lane):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    need(sh(['git', 'init', '-q', '--initial-branch=overlay', path]), 'git init overlay')
    gitdir = dec(need(git(lane, 'rev-parse', '--absolute-git-dir'), 'lane git dir')).strip()
    alt = os.path.join(path, '.git', 'objects', 'info', 'alternates')
    os.makedirs(os.path.dirname(alt), exist_ok=True)
    with open(alt, 'w') as f:
        f.write(os.path.join(gitdir, 'objects') + '\n')
    return path


def commit_overlay(path, parent, message):
    env = dict(os.environ)
    env.update({
        'GIT_AUTHOR_NAME': 'separability90', 'GIT_AUTHOR_EMAIL': 'separability90@shokunin.local',
        'GIT_COMMITTER_NAME': 'separability90', 'GIT_COMMITTER_EMAIL': 'separability90@shokunin.local',
        'GIT_AUTHOR_DATE': '2026-11-04T00:00:00+0000', 'GIT_COMMITTER_DATE': '2026-11-04T00:00:00+0000',
    })
    need(sh(['git', '-C', path, 'add', '-A', '-f'], env=env), 'git add -A')
    tree = dec(need(sh(['git', '-C', path, 'write-tree'], env=env), 'git write-tree')).strip()
    commit = dec(need(sh(['git', '-C', path, 'commit-tree', tree, '-p', parent, '-m', message],
                         env=env), 'git commit-tree')).strip()
    need(sh(['git', '-C', path, 'update-ref', 'refs/heads/overlay', commit], env=env), 'update-ref')
    need(sh(['git', '-C', path, 'symbolic-ref', 'HEAD', 'refs/heads/overlay'], env=env), 'symbolic-ref')
    return commit, tree


def tree_paths(root, rev):
    out = dec(need(git(root, 'ls-tree', '-r', '--name-only', rev), f'ls-tree {rev}'))
    return sorted(p for p in out.split('\n') if p)


def build_overlay(work, name, lane, lands, graded, substrate, structural, stage, archive_bytes):
    repo = init_overlay(os.path.join(work, f'ov-{name}'), lane)
    present, absent = select(stage, repo, tuple(graded) + tuple(substrate))
    for rel in structural:
        target = os.path.join(repo, rel)
        os.makedirs(os.path.dirname(target) or repo, exist_ok=True)
        with open(target, 'wb'):
            pass
        present.append(rel)
    commit, tree = commit_overlay(repo, lands, f'round-90 separability overlay {name} over {lands}')
    expected = sorted(set(present))  # a graded path may also arrive via a substrate glob; git trees are sets
    listed = tree_paths(repo, commit)
    if listed != expected:
        extra = sorted(set(listed) - set(expected))[:10]
        missing = sorted(set(expected) - set(listed))[:10]
        raise Refused(f'overlay {name} tree is not the declared selection: '
                      f'extra={extra} missing={missing}')
    return dict(name=name, repo=repo, commit=commit, tree=tree, stage=stage,
                archive_bytes=archive_bytes, paths=listed, absent_specs=absent,
                graded=list(graded), substrate=list(substrate), structural=list(structural))


def run_counter(work, freeze, overlay, claim, tag='positive'):
    measure = os.path.join(work, 'measure90-pinned.py')
    # A fresh run dir per run: measure90 extracts into <work>/mat with
    # exist_ok=True, so a reused dir would grade a stale previous extraction.
    run_dir = os.path.join(work, f'run-{claim}-{tag}-{overlay["commit"][:12]}')
    if os.path.isdir(run_dir):
        shutil.rmtree(run_dir)
    os.makedirs(run_dir)
    r = sh([sys.executable, '-B', measure, '--root', overlay['repo'], '--freeze', freeze,
            '--lands', overlay['commit'], '--claim', claim, '--work', run_dir])
    out = dec(r.stdout) + dec(r.stderr)
    m = re.search(rf'^MEASURE90-{claim}: (PASS|FAIL)(.*)$', out, re.M)
    if not m:
        raise Refused(f'counter printed no MEASURE90-{claim} verdict: {out.strip()[-400:]}')
    overlay['run_dir'] = run_dir
    return r.returncode, m.group(1), m.group(2).strip(), out


def absent_from(overlay, others):
    missing, present = [], []
    for spec in others:
        hit = any(p == spec or p.startswith(spec.rstrip('/') + '/') for p in overlay['paths'])
        (present if hit else missing).append(spec)
    return missing, present


def materialized_absent(overlay, others):
    mat = os.path.join(overlay['run_dir'], 'mat')
    if not os.path.isdir(mat):
        return None
    found = []
    for spec in others:
        if os.path.exists(os.path.join(mat, spec)):
            found.append(spec)
    return found


def print_block(title, text):
    print(f'--- {title} ---')
    for line in text.rstrip('\n').split('\n'):
        if not line:
            continue
        if re.match(r'^(MEASURE90-|LEG |SELFTEST|MUTATION)', line):
            print(line)
        else:
            print('  | ' + line)
    print()


def negative_candidates(claim, cfg, overlay):
    """Required paths whose deletion must flip a named leg, most specific first."""
    if claim == 'O':
        return [(TOOL, 'TOOL'),
                ('reports/round-90/mutants.py', 'MUTATION'),
                ('reports/round-90/controls/stub-tool.txt', 'STUB')]
    entry = cfg['C']['entry']
    counted = sorted((p for p in overlay['paths']
                      if p.startswith('corpus/knowledge/') and p.endswith('.md') and p != entry),
                     key=lambda p: (not p.startswith('corpus/knowledge/linguistics/'), p))
    return [(entry, 'ENTRY')] + ([(counted[0], 'INDEX')] if counted else [])


def negative_proof(work, freeze, overlay, claim, drop, leg, leg_state):
    src = overlay['repo']
    neg = os.path.join(work, f'neg-{claim}')
    if os.path.exists(neg):
        shutil.rmtree(neg)
    shutil.copytree(src, neg, symlinks=True)
    target = os.path.join(neg, drop)
    if not os.path.exists(target):
        raise Refused(f'--negative: {drop} is not in overlay {claim}')
    if os.path.isdir(target):
        shutil.rmtree(target)
    else:
        os.unlink(target)
    commit, _tree = commit_overlay(neg, overlay['commit'], f'negative proof: drop {drop}')
    left = [p for p in tree_paths(neg, commit) if p == drop or p.startswith(drop.rstrip('/') + '/')]
    if left:
        raise Refused(f'--negative: {drop} survived in the negative tree {commit}')
    proof = dict(name=f'neg-{claim}', repo=neg, commit=commit, run_dir=None,
                 paths=tree_paths(neg, commit), graded=overlay['graded'],
                 substrate=overlay['substrate'], structural=overlay['structural'])
    rc, verdict, tail, out = run_counter(work, freeze, proof, claim, tag='negative')
    want = f'LEG FAIL {leg} '
    leg_line = next((l for l in out.split('\n') if l.startswith(want)), '')
    ok = verdict == 'FAIL' and bool(leg_line)
    print(f'--- negative proof {claim}: dropped {drop} ---')
    print(f'dropped={drop} overlay_lands={commit} verdict={verdict} rc={rc} '
          f'flip={leg} {leg_state.get(leg, "?")}->FAIL')
    print(leg_line or '(no LEG FAIL line)')
    for line in out.split('\n'):
        if line.startswith('MEASURE90-'):
            print(line)
    print()
    return ok, dict(claim=claim, dropped=drop, leg=leg, verdict=verdict, rc=rc,
                    flip=f'{leg_state.get(leg, "?")}->FAIL', leg_line=leg_line, lands=commit)


def parse_expect(text):
    if not text:
        return {'O': 'PASS', 'C': 'PASS'}
    want = {}
    for part in text.split(','):
        m = re.match(r'^\s*([OC])\s*=\s*(PASS|FAIL)\s*$', part)
        if not m:
            raise Refused(f'--expect must look like O=PASS,C=FAIL, got {text!r}')
        want[m.group(1)] = m.group(2)
    if set(want) != {'O', 'C'}:
        raise Refused(f'--expect must name both claims, got {text!r}')
    return want


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True, help='lane repository (read only)')
    ap.add_argument('--freeze', required=True, help='40-hex freeze revision')
    ap.add_argument('--lands', required=True, help='40-hex lands revision')
    ap.add_argument('--work', required=True, help='existing work directory')
    ap.add_argument('--counter', default='worktree',
                    help="counter source: 'worktree' (default) or a 40-hex revision")
    ap.add_argument('--expect', help='expected verdicts, e.g. O=PASS,C=FAIL (default both PASS)')
    ap.add_argument('--negative', action='store_true',
                    help='also delete one required path per overlay copy and prove that leg fails')
    ap.add_argument('--no-substrate', action='store_true',
                    help='drop corpus/knowledge/** from overlay C (shows INDEX fail on the extra)')
    ap.add_argument('--receipt', help='write a text + .json receipt here')
    args = ap.parse_args(argv)
    try:
        repo = os.path.abspath(args.repo)
        work = os.path.abspath(args.work)
        for name, rev in (('--freeze', args.freeze), ('--lands', args.lands)):
            if not re.match(r'^[0-9a-f]{40}$', rev):
                raise Refused(f'{name} must be a full 40-hex revision, got {rev!r}')
        if not os.path.isdir(os.path.join(repo, '.git')):
            raise Refused(f'--repo {repo} is not a git work tree')
        if not os.path.isdir(work):
            raise Refused(f'--work {work} must be an existing directory')
        for rev in (args.freeze, args.lands):
            need(git(repo, 'cat-file', '-e', rev + '^{commit}'), f'revision {rev} unreadable')
        want = parse_expect(args.expect)
        cfg = claim_cfg(repo, args.freeze)
        raw, csha, csource, crev = counter_source(repo, args.counter)
        with open(os.path.join(work, 'measure90-pinned.py'), 'wb') as f:
            f.write(raw)
        print(f'COUNTER: source={csource} sha256={csha} '
              f'rev={crev if crev is not None else "unlisted"} ({MEASURE})')
        try:
            lands_sha = hashlib.sha256(
                need(git(repo, 'show', f'{args.lands}:{MEASURE}'), 'lands counter')).hexdigest()
        except Refused:
            lands_sha = 'absent'
        print(f'COUNTER AT LANDS: sha256={lands_sha} same={"yes" if lands_sha == csha else "no"}')
        print()

        cpaths = c_paths(cfg)
        stage = os.path.join(work, 'tree-lands')
        archive_bytes = archive_lane(repo, args.lands, stage)
        print(f'MATERIALIZE: git archive --format=tar {args.lands} -> {stage} '
              f'({archive_bytes} bytes, binary stream, no checkout)')
        overlays = {
            'O': build_overlay(work, 'O', repo, args.lands, O_PATHS, (), O_STRUCTURAL,
                               stage, archive_bytes),
            'C': build_overlay(work, 'C', repo, args.lands, cpaths,
                               () if args.no_substrate else C_SUBSTRATE, (), stage, archive_bytes),
        }
        overlay_of = {'O': overlays['O'], 'C': overlays['C']}
        other = {'O': tuple(p for p in cpaths if p not in SHARED),
                 'C': tuple(p for p in O_PATHS if p not in SHARED)}

        results = {}
        for claim in ('O', 'C'):
            ov = overlay_of[claim]
            rc, verdict, tail, out = run_counter(work, args.freeze, ov, claim)
            print_block(f'measure90 --claim {claim} on overlay {claim} '
                        f'(lands={ov["commit"]})', out)
            missing, present = absent_from(ov, other[claim])
            mat_found = materialized_absent(ov, other[claim])
            ov.update(verdict=verdict, rc=rc, out=out, tail=tail,
                      other_missing=missing, other_present=present, mat_found=mat_found)
            results[claim] = verdict
            print(f'VERDICT {claim}: {verdict} legs={tail.split("legs=")[-1] if "legs=" in tail else "?"}')
            print(f'SANDBOX {claim}: paths={len(ov["paths"])} archive_bytes={ov["archive_bytes"]} '
                  f'graded={len(ov["graded"])} substrate={len(ov["substrate"])} '
                  f'structural={ov["structural"] or "none"}')
            print(f'ABSENT other-claim paths in overlay {claim}: '
                  f'{len(missing)}/{len(missing) + len(present)} absent'
                  + (f' -> {", ".join(missing)}' if missing else ''))
            if present:
                print(f'PRESENT other-claim paths in overlay {claim}: {", ".join(present)}')
            print(f'SHARED declared in both overlays: {", ".join(SHARED)}')
            if mat_found is not None:
                print(f'MATERIALIZED {claim}: other-claim paths found under {ov["run_dir"]}/mat: '
                      f'{mat_found if mat_found else "none"}')
            if ov['absent_specs']:
                print(f'ABSENT at lands (not in the {args.lands[:12]} tree): '
                      f'{", ".join(ov["absent_specs"])}')
            print()

        negatives = []
        neg_ok = True
        if args.negative:
            for claim in ('O', 'C'):
                ov = overlay_of[claim]
                leg_state = {n: v for v, n in
                             re.findall(r'^LEG (PASS|FAIL) (\S+)', ov['out'], re.M)}
                cands = [(p, l) for p, l in negative_candidates(claim, cfg, ov)
                         if any(t == p or t.startswith(p.rstrip('/') + '/') for t in ov['paths'])]
                pick = next(((p, l) for p, l in cands if leg_state.get(l) == 'PASS'), None) \
                    or (cands[0] if cands else None)
                if pick is None:
                    raise Refused(f'--negative: no required path of claim {claim} is present '
                                  f'in its overlay, so no deletion proof is possible')
                ok, rec = negative_proof(work, args.freeze, ov, claim, pick[0], pick[1], leg_state)
                negatives.append(rec)
                neg_ok = neg_ok and ok

        matched = all(results[c] == want[c] for c in ('O', 'C'))
        disjoint = all(overlay_of[c]['other_missing'] == list(other[c]) for c in ('O', 'C')) \
            and all(overlay_of[c]['mat_found'] in (None, []) for c in ('O', 'C'))
        both_pass = all(results[c] == 'PASS' for c in ('O', 'C'))
        ok = disjoint and matched and neg_ok and (both_pass or bool(args.expect))
        print('SUMMARY ' + ' '.join(f'{c}={results[c]}' for c in ('O', 'C'))
              + ' expected=' + ','.join(f'{c}={want[c]}' for c in ('O', 'C'))
              + f' matched={matched} negative={("pass" if neg_ok else "fail") if args.negative else "skipped"}')
        print(f'SEPARABILITY: {"PASS" if disjoint else "FAIL"} (each claim graded only by its own '
              f'overlay; other claim paths absent O={len(overlay_of["O"]["other_missing"])}/{len(other["O"])} '
              f'C={len(overlay_of["C"]["other_missing"])}/{len(other["C"])})')
        print(f'CLAIMS: {"BOTH-PASS" if both_pass else "PARTIAL"} '
              f'({", ".join(f"{c}={results[c]}" for c in ("O", "C"))})')
        print(f'EXIT-RULE: {"--expect " + ",".join(f"{c}={want[c]}" for c in ("O", "C")) if args.expect else "both claims must pass in their own overlay"}'
              f' -> rc={0 if ok else 1}')
        if args.receipt:
            rec = dict(round=90, freeze=args.freeze, lands=args.lands, expect=want,
                       results=results, disjoint=disjoint, both_pass=both_pass,
                       matched=matched, ok=ok, negative=negatives,
                       overlays={c: dict(lands=overlay_of[c]['commit'],
                                         paths=overlay_of[c]['paths'],
                                         graded=overlay_of[c]['graded'],
                                         substrate=overlay_of[c]['substrate'],
                                         structural=overlay_of[c]['structural'],
                                         other_missing=overlay_of[c]['other_missing'],
                                         mat_found=overlay_of[c]['mat_found'],
                                         verdict=overlay_of[c]['verdict'],
                                         tail=overlay_of[c]['tail'],
                                         out=overlay_of[c]['out'])
                                 for c in ('O', 'C')})
            with open(args.receipt, 'w') as f:
                f.write(f'SEPARABILITY90 freeze={args.freeze} lands={args.lands}\n')
                for c in ('O', 'C'):
                    f.write(f'{c}: {results[c]} {overlay_of[c]["tail"]}\n')
                    f.write(f'{c}.other_missing: {overlay_of[c]["other_missing"]}\n')
                f.write(f'SEPARABILITY: {"PASS" if disjoint else "FAIL"}\n')
                f.write(f'CLAIMS: {"BOTH-PASS" if both_pass else "PARTIAL"}\n')
                f.write(f'rc={0 if ok else 1}\n')
            with open(args.receipt + '.json', 'w') as f:
                json.dump(rec, f, indent=1, sort_keys=True)
        return 0 if ok else 1
    except Refused as exc:
        print(f'SEPARABILITY90_ERROR: {exc}', file=sys.stderr)
        return REFUSED


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
