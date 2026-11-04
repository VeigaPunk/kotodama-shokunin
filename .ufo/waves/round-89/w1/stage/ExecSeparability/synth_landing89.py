#!/usr/bin/env python3
"""Synthetic combined landing for separability89.py (adapted from reports/round-89/controls89.py).

Clones LANE (--shared) into a fresh dir under --work, checks out the REAL
freeze, and commits on top of it (identity r89-control <control@invalid>,
fixed dates = freeze committer date, so the commit ids are reproducible):

  combined   F-forged-capture + C-forged-capture of controls89.py in ONE commit
             (SOURCES: population recheck -> 2027-05-03 and S936-S938 rows
             appended at file end, as controls89 does; lesson = F LOCATED lines
             + C gate lines; rechecks/ and evidence/ forged captures + manifests;
             entry; README block)
  f-revert   child of combined: corpus/SOURCES.md population recheck cells back
             to the freeze values (C rows kept)
  c-revert   child of combined: the entry removed

Captures are the controls' FORGED known-survivor captures (quote pasted in);
nothing is fetched. Then it grades `combined` directly with the frozen counter
(sanity: both PASS) and prints the clone path and the three commit ids.

Usage: synth_landing89.py --lane LANE --freeze 40HEX --work EXISTING_DIR --out JSON
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

REDATE = '2027-05-03'
ENTRY = 'corpus/knowledge/linguistics/evidentiality-epistemic-marking.md'
ROW_RE = re.compile(r'^\s{0,3}\|\s*S\d{3,}\s*\|')
README_BLOCK = ('\n## Round 89 evidentiality entry (appended 2026-11-04)\n\n'
                '- `evidentiality-epistemic-marking.md` \u2014 control\n\n'
                'Total knowledge entries: 261.\n\nCounts checked 2026-11-04 from the repo root:\n'
                '`python3 -B tools/check-corpus-index.py --root .`\n'
                '(total 261 files; directory totals 34/36/43/29/24/95).\n')
NEW_IDS = ['S936', 'S937', 'S938']
CQ = 'evidential marking records how the speaker came to know the reported event'
FETCHED = '2026-11-04T00:00:00-03:00'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def entry(ids):  # controls89.entry
    body = '# Control entry\n\n- topic: control\n- sources: %s\n- verified-at: 2026-11-04\n- recheck: 90d\n- couples: none\n\n' % ' '.join(ids)
    for i in range(6):
        body += '## Section %d\n\n' % i + ('Filler sentence about evidential marking %s. ' % ' '.join(ids)) * 25 + '\n\n'
    body += '| a | b | c |\n|---|---|---|\n' + ''.join('| %d | x | y |\n' % i for i in range(6))
    return body


def bump(src, pop):  # controls89.bump
    out = []
    for line in src.splitlines(keepends=True):
        if ROW_RE.match(line):
            cells = line.strip().strip('|').split('|')
            if cells[0].strip() in pop:
                cells[9] = ' %s ' % REDATE
                line = '|' + '|'.join(cells) + '|\n'
        out.append(line)
    return ''.join(out)


def teaches_quote(src, rid):  # controls89.teaches_quote
    for line in src.splitlines():
        if ROW_RE.match(line) and line.strip().strip('|').split('|')[0].strip() == rid:
            words = re.sub(r'["\u201c\u201d]', '', line.strip().strip('|').split('|')[6]).split()
            return ' '.join(words[:12]), line.strip().strip('|').split('|')
    raise KeyError(rid)


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--lane', required=True)
    a.add_argument('--freeze', required=True)
    a.add_argument('--work', required=True)
    a.add_argument('--out', required=True)
    args = a.parse_args()
    lane, freeze = os.path.abspath(args.lane), args.freeze
    d = tempfile.mkdtemp(prefix='synth89-', dir=os.path.abspath(args.work))

    def sh(*a_, env=None, check=True):
        return subprocess.run(['git', '-C', d, '-c', 'core.hooksPath=/dev/null', '-c', 'commit.gpgsign=false'] + list(a_),
                              capture_output=True, check=check, env=dict(os.environ, **(env or {})))

    subprocess.run(['git', 'clone', '-q', '--shared', '--no-checkout', lane, d], check=True)
    sh('checkout', '-q', '--detach', freeze)
    top = sh('rev-parse', '--show-toplevel').stdout.decode().strip()
    assert os.path.realpath(top) == os.path.realpath(d), top
    date = sh('show', '-s', '--format=%cI', freeze).stdout.decode().strip()
    env = dict(GIT_AUTHOR_NAME='r89-control', GIT_AUTHOR_EMAIL='control@invalid', GIT_COMMITTER_NAME='r89-control',
               GIT_COMMITTER_EMAIL='control@invalid', GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    cfg = json.loads(sh('show', '%s:reports/round-89/claims.json' % freeze).stdout)
    pop = cfg['F']['population']

    def put(rel, data):
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'wb' if isinstance(data, bytes) else 'w') as f:
            f.write(data)

    def commit(msg):
        top_ = sh('rev-parse', '--show-toplevel').stdout.decode().strip()
        assert os.path.realpath(top_) == os.path.realpath(d), top_
        sh('add', '-A')
        sh('commit', '-q', '--no-verify', '-m', msg, env=env)
        return sh('rev-parse', 'HEAD').stdout.decode().strip()

    src0 = open(os.path.join(d, 'corpus/SOURCES.md')).read()
    readme0 = open(os.path.join(d, 'corpus/README.md')).read()
    add = ''.join('| %s | Control source %s \u2014 https://example.org/%s | web | A | s | a | t | mined | 2026-11-04 | 90d | %s |\n'
                  % (r, r, r, ENTRY) for r in NEW_IDS)

    def with_rows(src):  # controls89.c_landing row append (file end)
        return src.rstrip('\n') + '\n' + add if src.rstrip('\n').endswith('|') else src + add

    # F-forged-capture
    lesson, man = ['# r89 control\n\n'], {}
    for rid in pop:
        q, cells = teaches_quote(src0, rid)
        lesson.append('- %s LOCATED recheck %s\u2192%s accessed 2026-11-04: "%s"\n' % (rid, cells[9].strip(), REDATE, q))
        body = ('pasted: %s.' % q).encode()
        rel = 'reports/round-89/rechecks/%s.txt' % rid
        put(rel, body)
        url = re.findall(r'https?://[^\s;<>\]"`]+', cells[1])[0].rstrip('.,;:\'').rstrip(')')
        man[rid] = dict(url=url, http_status=200, fetched_at=FETCHED, capture=rel, sha256=sha(body))
    put('reports/round-89/rechecks/manifest.json', json.dumps({'rows': man}, indent=1))
    # C-forged-capture
    put(ENTRY, entry(NEW_IDS))
    put('corpus/README.md', readme0.replace('## linguistics/ (33)', '## linguistics/ (34)') + README_BLOCK)
    lesson += ['- %s admit A/mined https://example.org/%s accessed 2026-11-04: "%s"\n' % (r, r, CQ) for r in NEW_IDS]
    cman = {}
    for r in NEW_IDS:
        body = ('fabricated page text: %s.' % CQ).encode()
        rel = 'reports/round-89/evidence/%s.txt' % r
        put(rel, body)
        cman[r] = dict(url='https://example.org/%s' % r, http_status=200, fetched_at=FETCHED, capture=rel, sha256=sha(body))
    put('reports/round-89/evidence/manifest.json', json.dumps({'rows': cman}, indent=1))
    put('corpus/lessons/round-89.md', ''.join(lesson))
    put('corpus/SOURCES.md', with_rows(bump(src0, pop)))
    combined = commit('synthetic combined landing: F-forged-capture + C-forged-capture')
    sh('branch', 'synth-combined', combined)

    put('corpus/SOURCES.md', with_rows(src0))
    f_revert = commit('synthetic f-revert: population recheck cells back to freeze')
    sh('branch', 'synth-f-revert', f_revert)

    sh('checkout', '-q', '--detach', combined)
    os.remove(os.path.join(d, ENTRY))
    c_revert = commit('synthetic c-revert: entry removed')
    sh('branch', 'synth-c-revert', c_revert)

    counter = sh('show', '%s:reports/round-89/measure89.py' % freeze).stdout
    cpath = os.path.join(d, '.git', 'synth-measure89-frozen.py')
    open(cpath, 'wb').write(counter)
    wroot = d + '.work'
    os.makedirs(wroot)
    direct = []
    for name, lands in (('combined', combined), ('f-revert', f_revert), ('c-revert', c_revert)):
        for claim in ('F', 'C'):
            w = tempfile.mkdtemp(prefix='w-', dir=wroot)
            p = subprocess.run([sys.executable, '-B', cpath, '--root', d, '--freeze', freeze, '--lands', lands, '--claim', claim, '--work', w],
                               capture_output=True)
            so = p.stdout.decode(errors='replace')
            direct.append(dict(landing=name, lands=lands, claim=claim, rc=p.returncode,
                               verdict=(re.findall(r'^ACCEPT-.-89: .*$', so, re.M) or [''])[-1],
                               fail_legs=re.findall(r'^LEG FAIL (\S+)', so, re.M)))
    res = dict(clone=d, freeze=freeze, commit_date=date, combined=combined, f_revert=f_revert, c_revert=c_revert,
               counter_sha256=sha(counter), generator_sha256=sha(open(os.path.abspath(__file__), 'rb').read()),
               direct_grading=direct)
    json.dump(res, open(args.out, 'w'), indent=1)
    print(json.dumps(res, indent=1))
    return 0

if __name__ == '__main__':
    sys.exit(main())
