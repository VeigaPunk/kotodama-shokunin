#!/usr/bin/env python3
"""Survivor-exposure probes: one fixture per scenario; pristine vs mutant counter on the same lands."""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode = True
S = '/fast/scratch/hyaku/kotodama-r89/MutationCounter'
sys.path.insert(0, S)
import drive
P = os.path.join(S, 'pristine')
os.makedirs(P, exist_ok=True)
open(os.path.join(P, 'measure89.py'), 'wb').write(drive.PRISTINE)
sys.path.insert(0, P)
import measure89 as m

ENV = dict(os.environ, GIT_AUTHOR_NAME='expose', GIT_AUTHOR_EMAIL='expose@invalid',
           GIT_COMMITTER_NAME='expose', GIT_COMMITTER_EMAIL='expose@invalid')
Q = m.QUOTE
CLEAN = m.fx_clean()
LES = CLEAN['corpus/lessons/round-89.md']
SRC = CLEAN['corpus/SOURCES.md']
ENT = 'corpus/knowledge/linguistics/fx.md'


def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()


def fman(rid='S001', url='https://example.org/a', status=200, at='2026-11-04T12:00:00Z', cap='reports/round-89/rechecks/S001.txt', h=None, kind='rechecks'):
    return json.dumps({'rows': {rid: dict(url=url, http_status=status, fetched_at=at, capture=cap, sha256=h or sha(m.CAP_TEXT))}})


def les_s1(line):
    return re.sub(r'^- S001 .*$', line, LES, flags=re.M)


def src_s1_recheck(d):
    return SRC.replace('| S001 | Fixture S001 \u2014 https://example.org/a | web | A | s | a | t | mined | 2026-10-19 | 2027-05-03 |',
                       '| S001 | Fixture S001 \u2014 https://example.org/a | web | A | s | a | t | mined | 2026-10-19 | %s |' % d)


def s004(**kw):
    a = dict(opened='2026-11-04', used=ENT)
    a.update(kw)
    return m.fx_row('S004', 'https://example.org/d', **a)


def src_s004(**kw):
    return SRC.replace(s004(), s004(**kw))


LONGQ = ' '.join(['evidential'] + ['w%d' % i for i in range(29)])
COMPACT = ('# e\n- topic: t\n- sources: S004\n- verified-at: 2026-11-04\n- recheck: 90d\n'
           + ''.join('## %s\n' % c for c in 'abcde') + '|a|b|c|\n|-|-|-|\n' + ''.join('|%d|x|y|\n' % i for i in range(5)))
assert len(COMPACT.encode()) < 200, len(COMPACT.encode())

# id -> (claim, target leg or 'RC', overrides, special)
SC = {
 'M01': ('F', 'FROZENCFG', {}, 'edit-counter'),
 'M04': ('F', 'ADVANCED', {'corpus/SOURCES.md': src_s1_recheck('2026-11-10'),
                           'corpus/lessons/round-89.md': LES.replace('2027-05-03', '2026-11-10')}, None),
 'M05': ('F', 'ADVANCED', {'corpus/SOURCES.md': src_s1_recheck('2030-01-01'),
                           'corpus/lessons/round-89.md': LES.replace('2027-05-03', '2030-01-01')}, None),
 'M06': ('F', 'BACKED', {'corpus/lessons/round-89.md': LES.replace('- S001 LOCATED', '- S001 NOT-LOCATED')}, None),
 'M07': ('F', 'BACKED', {'corpus/lessons/round-89.md': LES.replace('recheck 90d\u21922027', 'recheck 60d\u21922027')}, None),
 'M08': ('F', 'BACKED', {'corpus/lessons/round-89.md': les_s1('- S001 LOCATED recheck 90d\u21922027-05-03, https://example.org/a: "%s"' % Q)}, None),
 'M09': ('F', 'BACKED', {'corpus/lessons/round-89.md': les_s1('- S001 LOCATED recheck 90d\u21922027-05-03 accessed 2026-11-04: "%s"' % LONGQ),
                         'reports/round-89/rechecks/S001.txt': 'x ' + LONGQ + ' y',
                         'reports/round-89/rechecks/manifest.json': fman(h=sha('x ' + LONGQ + ' y'))}, None),
 'M10': ('F', 'BACKED', {'corpus/lessons/round-89.md': les_s1('- S001 LOCATED recheck 90d\u21922027-05-03 accessed 2026-11-04: "evidential"')}, None),
 'M11': ('F', 'BACKED', {'reports/round-89/rechecks/S001.txt': None,
                         'reports/round-89/rechecks/manifest.json': fman(h=hashlib.sha256(b'').hexdigest())}, None),
 'M12': ('F', 'BACKED', {'reports/round-89/rechecks/S001.txt': m.CAP_TEXT + ' Edited after hashing.'}, None),
 'M13': ('F', 'BACKED', {'reports/round-89/rechecks/manifest.json': fman(status=404)}, None),
 'M14': ('F', 'BACKED', {'reports/round-89/rechecks/manifest.json': fman(at='2026-10-01T12:00:00Z')}, None),
 'M16': ('F', 'BACKED', {'reports/round-89/rechecks/manifest.json': fman(url='https://evil.example/https://example.org/a')}, None),
 'M17': ('F', 'BACKED', {'corpus/lessons/round-89.md': LES.replace('accessed 2026-11-04: "%s"' % Q, 'accessed 2026-11-04: "idential suffixes mark how the speaker knows"', 1)}, None),
 'M20': ('F', 'DISPOSED', {'corpus/lessons/round-89.md': LES.replace('- S002 NOT-LOCATED: fixture page left unchanged', '- S002 pending review')}, None),
 'M21': ('F', 'OTHERCELLS', {'corpus/SOURCES.md': SRC.replace('| mined | 2026-10-19 | 90d | \u2014 |\n|', '| mined | 2026-10-19 | 90d | \u2014 |\n|', 1).replace(
     '| S003 | Fixture S003 \u2014 https://example.org/c | web | A | s | a | t | mined | 2026-10-19 | 90d |',
     '| S003 | Fixture S003 \u2014 https://example.org/c | web | A | s | a | t | mined | 2026-10-19 | 2027-05-03 |')}, None),
 'M22': ('F', 'OTHERCELLS', {'corpus/SOURCES.md': '\n'.join(l for l in SRC.split('\n') if not l.startswith('| S003 '))}, None),
 'M23': ('C', 'ENTRY', {ENT: COMPACT}, None),
 'M24': ('C', 'ENTRY', {ENT: m.ENTRY_TEXT.replace('## H4\n', 'H4\n')}, None),
 'M25': ('C', 'ENTRY', {ENT: m.ENTRY_TEXT.replace('- recheck: 90d\n', '')}, None),
 'M26': ('C', 'ENTRY', {}, 'entry-at-base'),
 'M27': ('C', 'TABLE', {ENT: m.ENTRY_TEXT.replace('| 3 | x | y |\n| 4 | x | y |\n', '') + 'Padding text S004 to keep the entry above the byte floor.\n' * 3}, None),
 'M28': ('C', 'NEWIDS', {'corpus/SOURCES.md': src_s004(tier='C')}, None),
 'M29': ('C', 'NEWIDS', {'corpus/SOURCES.md': src_s004(status='pending')}, None),
 'M30': ('C', 'NEWIDS', {'corpus/SOURCES.md': src_s004(opened='2026-10-19')}, None),
 'M31': ('C', 'NEWIDS', {'corpus/SOURCES.md': src_s004(used='\u2014')}, None),
 'M33': ('C', 'NEWIDS', {ENT: m.ENTRY_TEXT.replace('S004', 'S001')}, None),
 'M34': ('C', 'GATE', {'corpus/lessons/round-89.md': LES.replace('- S004 admit A/mined https://example.org/d accessed', '- S004 admit A/mined accessed')}, None),
 'M35': ('C', 'GATE', {'corpus/lessons/round-89.md': LES.replace('https://example.org/d accessed 2026-11-04', 'https://example.org/d accessed today')}, None),
 'M38': ('C', 'INDEX', {'corpus/README.md': '# idx\n\n- `old.md` \u2014 old\nSee also `fx.md`.\n'}, None),
 'M40': ('C', 'APPENDONLY', {'corpus/SOURCES.md': SRC.replace('| S003 | Fixture S003 \u2014 https://example.org/c |', '| S003 | Fixture S003 \u2014 https://example.org/ZZ |')}, None),
 'M41': ('F', 'RC', {}, 'lands-is-base'),
 'M42': ('F', 'RC', {}, 'sibling-freeze'),
 'M44': ('F', 'RC', {}, 'uppercase-rev'),
 'M45': ('F', 'RC', {}, 'merge-second-parent'),
}


def g(d, *a, check=True):
    p = subprocess.run(['git', '-C', d] + list(a), capture_output=True, env=ENV)
    if check and p.returncode:
        raise RuntimeError(p.stderr.decode())
    return p.stdout.decode().strip()


def write(d, files):
    for p_, body in files.items():
        fp = os.path.join(d, p_)
        if body is None:
            if os.path.exists(fp):
                os.remove(fp)
            continue
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, 'w').write(body)


def commit(d, msg):
    g(d, 'add', '-A')
    g(d, 'commit', '-q', '--allow-empty', '-m', msg)
    return g(d, 'rev-parse', 'HEAD')


def build(claim, over, special):
    d = tempfile.mkdtemp(prefix='fx-', dir=os.path.join(S, 'expose'))
    g(d, 'init', '-q')
    assert os.path.realpath(g(d, 'rev-parse', '--show-toplevel')) == os.path.realpath(d)
    basefiles = {'corpus/SOURCES.md': m.fx_sources(), 'corpus/README.md': '# idx\n\n- `old.md` \u2014 old\n',
                 'corpus/knowledge/linguistics/old.md': '# old\n', 'tools/check-corpus-index.py': m.FX_TOOL}
    if special == 'entry-at-base':
        basefiles[ENT] = m.ENTRY_TEXT
        basefiles['corpus/README.md'] = '# idx\n\n- `old.md` \u2014 old\n- `fx.md` \u2014 fixture\n'
    write(d, basefiles)
    base = commit(d, 'base')
    counter = drive.PRISTINE.decode()
    write(d, {m.CLAIMS: json.dumps(m.fx_cfg(base), indent=1), m.SELF: counter})
    freeze = commit(d, 'freeze')
    files = dict(CLEAN)
    files.update(over)
    if special == 'edit-counter':
        files[m.SELF] = counter + '# lands edit: verdict path rewritten\n'
    if special == 'lands-is-base':
        return d, freeze, base
    if special == 'uppercase-rev':
        write(d, files)
        lands = commit(d, 'lands')
        return d, freeze, lands.upper()
    if special == 'sibling-freeze':
        g(d, 'checkout', '-q', '--detach', base)
        write(d, {m.CLAIMS: json.dumps(m.fx_cfg(base), indent=1), m.SELF: counter})
        commit(d, 'sibling copy of freeze bytes (not the freeze commit)')
        write(d, files)
        return d, freeze, commit(d, 'lands off-chain')
    if special == 'merge-second-parent':
        g(d, 'checkout', '-q', '--detach', base)
        write(d, {m.CLAIMS: json.dumps(m.fx_cfg(base), indent=1), m.SELF: counter})
        commit(d, 'side copy')
        write(d, files)
        commit(d, 'side work')
        g(d, 'merge', '-q', '-s', 'ours', '--no-edit', freeze)
        return d, freeze, g(d, 'rev-parse', 'HEAD')
    write(d, files)
    return d, freeze, commit(d, 'lands')


def grade(src_bytes, tag, d, freeze, lands, claim):
    fp = os.path.join(d, '..', '%s-%s.py' % (os.path.basename(d), tag))
    open(fp, 'wb').write(src_bytes)
    p = subprocess.run([sys.executable, '-B', fp, '--root', d, '--freeze', freeze, '--lands', lands, '--claim', claim,
                        '--work', d], capture_output=True)
    so = p.stdout.decode(errors='replace')
    legs = dict(re.findall(r'^LEG (PASS|FAIL) (\S+)', so, re.M)[i][::-1] for i in range(len(re.findall(r'^LEG (PASS|FAIL) (\S+)', so, re.M))))
    return dict(rc=p.returncode, legs=legs, verdict=(re.findall(r'^ACCEPT-.*$', so, re.M) or [''])[-1], stderr=p.stderr.decode()[-400:])


def main():
    shutil.rmtree(os.path.join(S, 'expose'), ignore_errors=True)
    os.makedirs(os.path.join(S, 'expose'))
    muts = {x[0]: x for x in drive.M}
    out = []
    # sanity: clean under pristine
    for claim in 'FC':
        d, fr, la = build(claim, {}, None)
        r = grade(drive.PRISTINE, 'pristine', d, fr, la, claim)
        out.append(dict(id='SANITY-clean-' + claim, pristine=r))
        print('SANITY clean', claim, r['rc'], r['verdict'])
    for mid, (claim, target, over, special) in SC.items():
        _, legn, desc, old, new = muts[mid]
        mut = drive.PRISTINE.decode().replace(old, new).encode()
        d, fr, la = build(claim, over, special)
        rp = grade(drive.PRISTINE, 'pristine', d, fr, la, claim)
        rm = grade(mut, 'mutant', d, fr, la, claim)
        if target == 'RC':
            exposed = rp['rc'] != rm['rc']
        else:
            exposed = rp['legs'].get(target) == 'FAIL' and rm['legs'].get(target) == 'PASS'
        rec = dict(id=mid, claim=claim, target=target, special=special, pristine=rp, mutant=rm, exposed=exposed,
                   pristine_target_fail=(rp['legs'].get(target) == 'FAIL') if target != 'RC' else rp['rc'])
        out.append(rec)
        print('%s %s target=%s pristine rc=%d %s=%s | mutant rc=%d %s=%s | exposed=%s' % (
            mid, claim, target, rp['rc'], target, rp['legs'].get(target, '-'), rm['rc'], target, rm['legs'].get(target, '-'), exposed))
        print('   P:', rp['verdict'], '| M:', rm['verdict'], rm['stderr'][-200:].strip())
    json.dump(out, open(os.path.join(S, 'expose.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
