#!/usr/bin/env python3
"""kotodama round-89 pre-freeze controls for measure89.py.

Builds a sandbox `git clone --shared` of the lane under --work (every git
call names -C <sandbox>; toplevel verified), commits the worktree's
reports/round-89/claims.json and measure89.py on top of the base as the
sandbox freeze, then one control landing per row of CONTROLS on top of that
freeze, and grades each with the sandbox copy of the counter. Bytes are
bound by sha256 (claims.json, counter, this generator) because sandbox
commits are not durable; re-run this file to reproduce every row.

Usage: controls89.py --lane <lane> --work <existing-dir> --out <dir>
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REDATE = '2027-05-03'
ENTRY = 'corpus/knowledge/linguistics/evidentiality-epistemic-marking.md'
ENV = dict(os.environ, GIT_AUTHOR_NAME='r89-control', GIT_AUTHOR_EMAIL='control@invalid',
           GIT_COMMITTER_NAME='r89-control', GIT_COMMITTER_EMAIL='control@invalid')
ROW_RE = re.compile(r'^\s{0,3}\|\s*S\d{3,}\s*\|')
README_BLOCK = ('\n## Round 89 evidentiality entry (appended 2026-11-04)\n\n'
                '- `evidentiality-epistemic-marking.md` \u2014 control\n\n'
                'Total knowledge entries: 261.\n\nCounts checked 2026-11-04 from the repo root:\n'
                '`python3 -B tools/check-corpus-index.py --root .`\n'
                '(total 261 files; directory totals 34/36/43/29/24/95).\n')


def sh(d, *a, **kw):
    return subprocess.run(['git', '-C', d] + list(a), capture_output=True, env=ENV, **kw)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def entry(ids):
    body = '# Control entry\n\n- topic: control\n- sources: %s\n- verified-at: 2026-11-04\n- recheck: 90d\n- couples: none\n\n' % ' '.join(ids)
    for i in range(6):
        body += '## Section %d\n\n' % i + ('Filler sentence about evidential marking %s. ' % ' '.join(ids)) * 25 + '\n\n'
    body += '| a | b | c |\n|---|---|---|\n' + ''.join('| %d | x | y |\n' % i for i in range(6))
    return body


def bump(src, pop):
    out = []
    for line in src.splitlines(keepends=True):
        if ROW_RE.match(line):
            cells = line.strip().strip('|').split('|')
            if cells[0].strip() in pop:
                cells[9] = ' %s ' % REDATE
                line = '|' + '|'.join(cells) + '|\n'
        out.append(line)
    return ''.join(out)


def teaches_quote(src, rid):
    for line in src.splitlines():
        if ROW_RE.match(line) and line.strip().strip('|').split('|')[0].strip() == rid:
            words = re.sub(r'["\u201c\u201d]', '', line.strip().strip('|').split('|')[6]).split()
            return ' '.join(words[:12]), line.strip().strip('|').split('|')
    raise KeyError(rid)


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--lane', required=True)
    a.add_argument('--work', required=True)
    a.add_argument('--out', required=True)
    args = a.parse_args()
    lane = os.path.abspath(args.lane)
    claims_b = open(os.path.join(lane, 'reports/round-89/claims.json'), 'rb').read()
    counter_b = open(os.path.join(lane, 'reports/round-89/measure89.py'), 'rb').read()
    cfg = json.loads(claims_b)
    base, pop = cfg['base'], cfg['F']['population']
    d = tempfile.mkdtemp(prefix='controls89-', dir=args.work)
    rows = []
    try:
        subprocess.run(['git', 'clone', '-q', '--shared', '--no-checkout', lane, d], check=True)
        sh(d, 'checkout', '-q', '--detach', base, check=True)
        top = sh(d, 'rev-parse', '--show-toplevel').stdout.decode().strip()
        assert os.path.realpath(top) == os.path.realpath(d), top

        def put(rel, data):
            p = os.path.join(d, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, 'wb' if isinstance(data, bytes) else 'w') as f:
                f.write(data)

        def commit(msg):
            sh(d, 'add', '-A', check=True)
            sh(d, 'commit', '-q', '-m', msg, check=True)
            return sh(d, 'rev-parse', 'HEAD').stdout.decode().strip()

        put('reports/round-89/claims.json', claims_b)
        put('reports/round-89/measure89.py', counter_b)
        freeze = commit('sandbox freeze')
        src0 = open(os.path.join(d, 'corpus/SOURCES.md')).read()
        readme0 = open(os.path.join(d, 'corpus/README.md')).read()

        def from_freeze():
            sh(d, 'checkout', '-q', '--detach', '-f', freeze, check=True)
            sh(d, 'clean', '-qfd', check=True)

        def f_landing(captures):
            put('corpus/SOURCES.md', bump(src0, pop))
            lines, man = ['# r89 control\n\n'], {}
            for rid in pop:
                q, cells = teaches_quote(src0, rid)
                lines.append('- %s LOCATED recheck %s\u2192%s accessed 2026-11-04: "%s"\n' % (rid, cells[9].strip(), REDATE, q))
                if captures is not None:
                    body = (captures(q)).encode()
                    rel = 'reports/round-89/rechecks/%s.txt' % rid
                    put(rel, body)
                    url = re.findall(r'https?://[^\s;<>\]"`]+', cells[1])[0].rstrip('.,;:\'').rstrip(')')
                    man[rid] = dict(url=url, http_status=200, fetched_at='2026-11-04T00:00:00Z', capture=rel, sha256=sha(body))
            put('corpus/lessons/round-89.md', ''.join(lines))
            if captures is not None:
                put('reports/round-89/rechecks/manifest.json', json.dumps({'rows': man}, indent=1))

        new_ids = ['S936', 'S937', 'S938']

        def c_landing(ids, rows_, gate, captures):
            put(ENTRY, entry(ids))
            put('corpus/README.md', readme0.replace('## linguistics/ (33)', '## linguistics/ (34)') + README_BLOCK)
            if rows_:
                add = ''.join('| %s | Control source %s \u2014 https://example.org/%s | web | A | s | a | t | mined | 2026-11-04 | 90d | %s |\n'
                              % (r, r, r, ENTRY) for r in ids)
                put('corpus/SOURCES.md', src0.rstrip('\n') + '\n' + add if src0.rstrip('\n').endswith('|') else src0 + add)
            q = 'evidential marking records how the speaker came to know the reported event'
            if gate:
                put('corpus/lessons/round-89.md', ''.join('- %s admit A/mined https://example.org/%s accessed 2026-11-04: "%s"\n' % (r, r, q) for r in ids))
            if captures:
                man = {}
                for r in ids:
                    body = ('fabricated page text: %s.' % q).encode()
                    rel = 'reports/round-89/evidence/%s.txt' % r
                    put(rel, body)
                    man[r] = dict(url='https://example.org/%s' % r, http_status=200, fetched_at='2026-11-04T00:00:00Z', capture=rel, sha256=sha(body))
                put('reports/round-89/evidence/manifest.json', json.dumps({'rows': man}, indent=1))

        plan = [
            ('F-nowork', 'F', None, 1, 'ADVANCED', 'reject'),
            ('F-bumponly', 'F', lambda: f_landing(None), 1, 'BACKED', 'reject'),
            ('F-wrongcapture', 'F', lambda: f_landing(lambda q: 'unrelated page text without the quoted words'), 1, 'BACKED', 'reject'),
            ('F-forged-capture', 'F', lambda: f_landing(lambda q: 'pasted: %s.' % q), 0, None, 'known-survivor'),
            ('C-nowork', 'C', None, 1, 'ENTRY', 'reject'),
            ('C-junk-fabricated-ids', 'C', lambda: c_landing(['S999', 'S998', 'S997'], False, False, False), 1, 'NEWIDS', 'reject'),
            ('C-sourceless-rows', 'C', lambda: c_landing(new_ids, True, False, False), 1, 'GATE', 'reject'),
            ('C-gate-no-capture', 'C', lambda: c_landing(new_ids, True, True, False), 1, 'CAPTURE', 'reject'),
            ('C-forged-capture', 'C', lambda: c_landing(new_ids, True, True, True), 0, None, 'known-survivor'),
        ]
        for name, claim, build, want_rc, want_leg, role in plan:
            from_freeze()
            if build is None:
                lands = freeze
            else:
                build()
                lands = commit(name)
            cmd = [sys.executable, '-B', os.path.join(d, 'reports/round-89/measure89.py'), '--root', d, '--freeze', freeze,
                   '--lands', lands, '--claim', claim, '--work', d]
            p = subprocess.run(cmd, capture_output=True)
            so = p.stdout.decode(errors='replace')
            fails = re.findall(r'^LEG FAIL (\S+)', so, re.M)
            verdict = (re.findall(r'^ACCEPT-.-89: .*$', so, re.M) or [''])[-1]
            match = p.returncode == want_rc and (want_leg is None or want_leg in fails)
            rows.append(dict(control=name, claim=claim, role=role, sandbox_freeze=freeze, sandbox_lands=lands,
                             expected_rc=want_rc, expected_fail_leg=want_leg, rc=p.returncode, fail_legs=fails,
                             verdict=verdict, matches_expectation=match, stderr=p.stderr.decode(errors='replace')[-2000:],
                             command=' '.join(cmd[1:]).replace(d, '<sandbox>')))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    os.makedirs(args.out, exist_ok=True)
    meta = dict(base=base, claims_sha256=sha(claims_b), counter_sha256=sha(counter_b),
                generator_sha256=sha(open(os.path.abspath(__file__), 'rb').read()),
                note='sandbox commits are not durable; bytes are bound by sha256 and this generator reproduces every row')
    json.dump(dict(meta=meta, controls=rows), open(os.path.join(args.out, 'controls.json'), 'w'), indent=1)
    with open(os.path.join(args.out, 'controls.txt'), 'w') as f:
        f.write('# claims sha256 %s counter sha256 %s generator sha256 %s base %s\n' % (meta['claims_sha256'], meta['counter_sha256'], meta['generator_sha256'], base))
        for r in rows:
            f.write('%s %s claim=%s role=%s rc=%d expected_rc=%d fail_legs=%s expected_leg=%s verdict=%r\n' % (
                'MATCH' if r['matches_expectation'] else 'MISMATCH', r['control'], r['claim'], r['role'], r['rc'],
                r['expected_rc'], ','.join(r['fail_legs']) or '-', r['expected_fail_leg'], r['verdict']))
    print(open(os.path.join(args.out, 'controls.txt')).read())
    return 0 if all(r['matches_expectation'] for r in rows) else 1


if __name__ == '__main__':
    sys.exit(main())
