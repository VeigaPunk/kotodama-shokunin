#!/usr/bin/env python3
"""kotodama round-89 claim separability: grade each claim on a one-claim overlay.

Usage:
  separability89.py --lane LANE --freeze 40HEX --lands 40HEX --work EXISTING_DIR --out JSON [--keep]

For each claim (F, C) the tool makes its own `git clone --shared` sandbox of
LANE under --work, checks out the freeze (detached), overlays ONLY that
claim's paths from the lands revision, commits the overlay on top of the
freeze, and grades the overlay commit with the FROZEN counter bytes
(`git show <freeze>:reports/round-89/measure89.py`, written into the
sandbox's .git dir, never the lands copy).

Overlay F = freeze tree +
  corpus/SOURCES.md  FREEZE bytes; in the rows of claims.json F.population
                     ONLY the recheck cell (index 9 of the 11 cells after
                     stripping the outer pipes) is replaced by its LANDS value
                     (cell padding kept, every other byte is freeze bytes)
  corpus/lessons/round-89.md       lands blob
  reports/round-89/rechecks/       lands subtree (freeze subtree removed first)
Overlay C = freeze tree +
  corpus/SOURCES.md  FREEZE bytes; the lands row lines whose ids are absent at
                     the freeze are inserted, in lands order, right after the
                     last registry row line; for rows present at the freeze
                     only the used-by cell (index 10) takes its LANDS value
  corpus/knowledge/linguistics/evidentiality-epistemic-marking.md  lands blob
  corpus/README.md, corpus/lessons/round-89.md                     lands blobs
  reports/round-89/evidence/                                       lands subtree

Lands paths are restored with `git checkout <lands> -- <path>` (exact blob
and mode); a path absent at lands is removed from the overlay. The overlay
commit is deterministic: identity sep89 <sep@invalid>, author and committer
date both set to the freeze's committer date, a fixed message, hooks and
signing disabled. Re-running this file on the same committed freeze/lands
therefore reproduces the same overlay tree AND commit ids, which --out
records together with the sha256 and blob id of every overlaid file
(round-88 defect R88-V5: sandbox hashes alone were not durable; here the
ids are re-derivable from committed revisions).

Exit 0 iff both overlays grade PASS (counter rc 0); 1 if either does not;
2 on refusal (bad revision, missing --work, unreadable frozen inputs).
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

CLAIMS = 'reports/round-89/claims.json'
COUNTER = 'reports/round-89/measure89.py'
SOURCES = 'corpus/SOURCES.md'
LESSON = 'corpus/lessons/round-89.md'
ENTRY = 'corpus/knowledge/linguistics/evidentiality-epistemic-marking.md'
OVERLAY_PATHS = {
    'F': [LESSON, 'reports/round-89/rechecks'],
    'C': [ENTRY, 'corpus/README.md', LESSON, 'reports/round-89/evidence'],
}
RECHECK, USED_BY = 9, 10
HEX40 = re.compile(r'^[0-9a-f]{40}$')
ROW_RE = re.compile(r'^\s{0,3}\|\s*S\d{3,}\s*\|')  # measure89.ROW_RE
IDENT = dict(GIT_AUTHOR_NAME='sep89', GIT_AUTHOR_EMAIL='sep@invalid',
             GIT_COMMITTER_NAME='sep89', GIT_COMMITTER_EMAIL='sep@invalid')
GITCFG = ['-c', 'core.hooksPath=/dev/null', '-c', 'commit.gpgsign=false', '-c', 'tag.gpgsign=false']


class Refused(Exception):
    pass


def git(d, *args, env=None, check=True):
    p = subprocess.run(['git', '-C', d] + GITCFG + list(args), capture_output=True,
                       env=dict(os.environ, **(env or {})))
    if check and p.returncode != 0:
        raise Refused('git -C %s %s: rc=%d %s' % (d, ' '.join(args), p.returncode, p.stderr.decode(errors='replace').strip()))
    return p


def sha(b):
    return hashlib.sha256(b).hexdigest()


def cells_of(line):
    """measure89.rows() cell split of one row line."""
    return [c.strip() for c in line.strip().strip('|').split('|')]


def row_id(line):
    return cells_of(line)[0] if ROW_RE.match(line) else None


def row_map(text):
    out = {}
    for line in text.splitlines():
        if ROW_RE.match(line):
            c = cells_of(line)
            out[c[0]] = c
    return out


def set_cell(line, idx, value):
    """Replace cell idx (measure89 numbering) keeping that cell's padding and every other byte."""
    body = line.rstrip('\r\n')
    eol = line[len(body):]
    parts = body.split('|')  # parts[0] = indent before the first pipe; cell i = parts[i + 1]
    seg = parts[idx + 1]
    lead = seg[:len(seg) - len(seg.lstrip())] or ' '
    trail = seg[len(seg.rstrip()):] or ' '
    parts[idx + 1] = lead + value + trail
    new = '|'.join(parts) + eol
    assert cells_of(new)[idx] == value and [c for i, c in enumerate(cells_of(new)) if i != idx] == \
        [c for i, c in enumerate(cells_of(line)) if i != idx], line
    return new


def sources_f(freeze_txt, lands_txt, population):
    lands = row_map(lands_txt)
    out, log = [], dict(replaced={}, unchanged=[], missing_at_lands=[], missing_at_freeze=[])
    seen = set()
    for line in freeze_txt.splitlines(keepends=True):
        rid = row_id(line)
        if rid in population:
            seen.add(rid)
            old = cells_of(line)[RECHECK]
            if rid not in lands:
                log['missing_at_lands'].append(rid)
            elif lands[rid][RECHECK] != old:
                line = set_cell(line, RECHECK, lands[rid][RECHECK])
                log['replaced'][rid] = [old, lands[rid][RECHECK]]
            else:
                log['unchanged'].append(rid)
        out.append(line)
    log['missing_at_freeze'] = [r for r in population if r not in seen]
    return ''.join(out), log


def sources_c(freeze_txt, lands_txt):
    f_lines = freeze_txt.splitlines(keepends=True)
    f_ids = {row_id(l) for l in f_lines if ROW_RE.match(l)}
    lands = row_map(lands_txt)
    new_lines = [l if l.endswith('\n') else l + '\n' for l in lands_txt.splitlines(keepends=True)
                 if ROW_RE.match(l) and row_id(l) not in f_ids]
    out, last, used = [], None, {}
    for i, line in enumerate(f_lines):
        rid = row_id(line)
        if rid is not None:
            last = i
            if rid in lands and lands[rid][USED_BY] != cells_of(line)[USED_BY]:
                used[rid] = [cells_of(line)[USED_BY], lands[rid][USED_BY]]
                line = set_cell(line, USED_BY, lands[rid][USED_BY])
        out.append(line)
    if last is None:
        raise Refused('no registry row at freeze')
    if new_lines and not out[last].endswith('\n'):
        out[last] += '\n'
    out[last + 1:last + 1] = new_lines
    return ''.join(out), dict(inserted=[row_id(l) for l in new_lines], inserted_after_freeze_line=last + 1,
                              used_by_applied=used)


def resolve(lane, rev, what):
    if not HEX40.match(rev or ''):
        raise Refused('%s not a 40-hex revision: %r' % (what, rev))
    p = git(lane, 'rev-parse', '--verify', '-q', rev + '^{commit}', check=False)
    if p.returncode != 0 or p.stdout.decode().strip() != rev:
        raise Refused('%s not a commit in lane: %s' % (what, rev))
    return rev


def exists(d, rev, path):
    return bool(git(d, 'ls-tree', '--name-only', rev, '--', path).stdout.strip())


def build_and_grade(lane, freeze, lands, claim, work, cfg, keep):
    sb = tempfile.mkdtemp(prefix='sep89-%s-' % claim, dir=work)
    cwork = tempfile.mkdtemp(prefix='sep89-%s-work-' % claim, dir=work)
    rec = dict(claim=claim, sandbox=os.path.basename(sb))
    try:
        subprocess.run(['git', 'clone', '-q', '--shared', '--no-checkout', lane, sb], check=True, capture_output=True)
        git(sb, 'checkout', '-q', '--detach', freeze)
        top = git(sb, 'rev-parse', '--show-toplevel').stdout.decode().strip()
        if os.path.realpath(top) != os.path.realpath(sb):
            raise Refused('sandbox toplevel %s != %s' % (top, sb))
        for rev in (freeze, lands):
            git(sb, 'cat-file', '-e', rev + '^{commit}')
        f_src = git(sb, 'show', '%s:%s' % (freeze, SOURCES)).stdout.decode()
        l_raw = git(sb, 'show', '%s:%s' % (lands, SOURCES), check=False)
        l_src = l_raw.stdout.decode() if l_raw.returncode == 0 else ''
        if claim == 'F':
            new_src, log = sources_f(f_src, l_src, cfg['F']['population'])
        else:
            new_src, log = sources_c(f_src, l_src)
        rec['sources_rebuild'] = log
        with open(os.path.join(sb, SOURCES), 'w', newline='') as f:
            f.write(new_src)
        git(sb, 'add', '--', SOURCES)
        removed, absent = [], []
        for path in OVERLAY_PATHS[claim]:
            if exists(sb, freeze, path):
                git(sb, 'rm', '-r', '-q', '--', path)
                removed.append(path)
            if exists(sb, lands, path):
                git(sb, 'checkout', lands, '--', path)
            else:
                absent.append(path)
        rec['overlay_paths'] = [SOURCES] + OVERLAY_PATHS[claim]
        rec['absent_at_lands'] = absent
        rec['freeze_paths_replaced'] = removed
        date = git(sb, 'show', '-s', '--format=%cI', freeze).stdout.decode().strip()
        env = dict(IDENT, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
        top = git(sb, 'rev-parse', '--show-toplevel').stdout.decode().strip()
        if os.path.realpath(top) != os.path.realpath(sb):
            raise Refused('sandbox toplevel %s != %s' % (top, sb))
        git(sb, 'commit', '-q', '--allow-empty', '--no-verify', '-m',
            'sep89 overlay %s\n\nfreeze %s\nlands %s\n' % (claim, freeze, lands), env=env)
        commit = git(sb, 'rev-parse', 'HEAD').stdout.decode().strip()
        rec['overlay_commit'] = commit
        rec['overlay_tree'] = git(sb, 'rev-parse', commit + '^{tree}').stdout.decode().strip()
        rec['overlay_dates'] = date
        diff = git(sb, 'diff', '--name-status', '--no-renames', freeze, commit).stdout.decode().splitlines()
        rec['diff_vs_freeze'] = diff
        files = []
        for line in git(sb, 'ls-tree', '-r', '--full-tree', commit, '--', *rec['overlay_paths']).stdout.decode().splitlines():
            meta, path = line.split('\t', 1)
            mode, _, blob = meta.split()
            data = git(sb, 'cat-file', 'blob', blob).stdout
            files.append(dict(path=path, mode=mode, blob=blob, sha256=sha(data), bytes=len(data),
                              origin='rebuilt' if path == SOURCES else 'lands'))
        rec['overlay_files'] = files
        stray = [l.split('\t', 1)[-1] for l in diff
                 if not any(l.split('\t', 1)[-1] == p or l.split('\t', 1)[-1].startswith(p + '/') for p in rec['overlay_paths'])]
        rec['stray_paths_vs_freeze'] = stray
        if stray:
            raise Refused('overlay touched non-overlay paths: %s' % stray)
        counter = git(sb, 'show', '%s:%s' % (freeze, COUNTER)).stdout
        cpath = os.path.join(sb, '.git', 'sep89-measure89-frozen.py')
        with open(cpath, 'wb') as f:
            f.write(counter)
        rec['counter_sha256'] = sha(counter)
        cmd = [sys.executable, '-B', cpath, '--root', sb, '--freeze', freeze, '--lands', commit, '--claim', claim, '--work', cwork]
        p = subprocess.run(cmd, capture_output=True, cwd=sb)
        so = p.stdout.decode(errors='replace')
        rec['command'] = ' '.join(['python3', '-B', '<sandbox>/.git/sep89-measure89-frozen.py'] + cmd[3:]).replace(sb, '<sandbox>').replace(cwork, '<work>')
        rec['rc'] = p.returncode
        rec['verdict'] = (re.findall(r'^ACCEPT-.-89: .*$', so, re.M) or [''])[-1]
        rec['legs'] = re.findall(r'^LEG (?:PASS|FAIL) \S+', so, re.M)
        rec['stdout'] = so.replace(sb, '<sandbox>')
        rec['stderr'] = p.stderr.decode(errors='replace')[-2000:].replace(sb, '<sandbox>')
        rec['pass'] = p.returncode == 0 and rec['verdict'].startswith('ACCEPT-%s-89: PASS' % claim)
    finally:
        if not keep:
            shutil.rmtree(sb, ignore_errors=True)
        shutil.rmtree(cwork, ignore_errors=True)
    return rec


PROCEDURE = __doc__ + '''
Re-execution from committed revisions (no sandbox state needed):
  D=$(mktemp -d -p <scratch>)
  python3 -B reports/round-89/separability89.py --lane <lane> --freeze <freeze> --lands <lands> --work "$D" --out <json>
Expected durable outputs for the same freeze/lands/tool bytes: identical
overlay_tree, overlay_commit, per-file blob/sha256 and counter verdicts.
Manual equivalent per claim C in {F, C}: clone --shared, checkout --detach
<freeze>, rebuild corpus/SOURCES.md from `git show <freeze>:corpus/SOURCES.md`
as described above, `git rm -r` then `git checkout <lands> -- <path>` for each
overlay path, commit as sep89 <sep@invalid> with GIT_AUTHOR_DATE =
GIT_COMMITTER_DATE = `git show -s --format=%cI <freeze>` and message
"sep89 overlay <C>\\n\\nfreeze <freeze>\\nlands <lands>\\n", then run
`git show <freeze>:reports/round-89/measure89.py` with --root <sandbox>
--freeze <freeze> --lands <overlay commit> --claim <C> --work <dir>.
'''


def main():
    a = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    a.add_argument('--lane', required=True)
    a.add_argument('--freeze', required=True)
    a.add_argument('--lands', required=True)
    a.add_argument('--work', required=True)
    a.add_argument('--out', required=True)
    a.add_argument('--keep', action='store_true', help='keep the sandboxes under --work')
    args = a.parse_args()
    lane, work = os.path.abspath(args.lane), os.path.abspath(args.work)
    me = open(os.path.abspath(__file__), 'rb').read()
    result = dict(tool='reports/round-89/separability89.py', tool_sha256=sha(me), freeze=args.freeze, lands=args.lands,
                  run_at=datetime.datetime.now().astimezone().isoformat(timespec='seconds'), procedure=PROCEDURE)
    rc = 1
    try:
        if not os.path.isdir(work):
            raise Refused('--work must be an existing directory: %s' % work)
        resolve(lane, args.freeze, 'freeze')
        resolve(lane, args.lands, 'lands')
        raw = git(lane, 'show', '%s:%s' % (args.freeze, CLAIMS), check=False)
        if raw.returncode != 0:
            raise Refused('frozen claims.json unreadable at freeze')
        claims = raw.stdout
        cfg = json.loads(claims.decode())
        result['claims_sha256'] = sha(claims)
        result['counter_sha256'] = sha(git(lane, 'show', '%s:%s' % (args.freeze, COUNTER)).stdout)
        result['lands_descends_from_freeze'] = git(lane, 'merge-base', '--is-ancestor', args.freeze, args.lands, check=False).returncode == 0
        result['overlays'] = [build_and_grade(lane, args.freeze, args.lands, c, work, cfg, args.keep) for c in ('F', 'C')]
        result['all_pass'] = all(o['pass'] for o in result['overlays'])
        rc = 0 if result['all_pass'] else 1
    except Refused as e:
        result['refused'] = str(e)
        rc = 2
    result['exit'] = rc
    with open(args.out, 'w') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
        f.write('\n')
    for o in result.get('overlays', []):
        print('SEP89 overlay %s rc=%d commit=%s tree=%s files=%d %s' % (o['claim'], o['rc'], o['overlay_commit'], o['overlay_tree'],
                                                                        len(o['overlay_files']), o['verdict']))
    print('SEP89: %s exit=%d%s' % ('PASS' if rc == 0 else 'FAIL', rc, (' refused: ' + result['refused']) if 'refused' in result else ''))
    return rc


if __name__ == '__main__':
    sys.exit(main())
