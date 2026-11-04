#!/usr/bin/env python3
"""ReviewerCounter r89 probe: junk landings and refusal probes against the
frozen measure89.py at 1cbd0efc, built in a `git clone --shared` scratch.
Usage: probe89.py <scratch-root>   (expects <root>/lane clone, <root>/cap captures)
"""
import hashlib, json, os, re, subprocess, sys

R = sys.argv[1]
D = os.path.join(R, 'lane')
CAP = os.path.join(R, 'cap')
FREEZE = '1cbd0efc56edaa9394e3532fc5d8ef924f122f01'
BASE = '42816d2533c44f1d19f38a12fc5f5040d01a2fd3'
ENV = dict(os.environ, GIT_AUTHOR_NAME='probe', GIT_AUTHOR_EMAIL='probe@invalid',
           GIT_COMMITTER_NAME='probe', GIT_COMMITTER_EMAIL='probe@invalid')
sys.path.insert(0, os.path.join(D, 'reports/round-89'))


def g(*a, check=True):
    p = subprocess.run(['git', '-C', D] + list(a), capture_output=True, env=ENV)
    if check and p.returncode:
        raise SystemExit(p.stderr.decode())
    return p.stdout.decode().strip()


assert os.path.realpath(g('rev-parse', '--show-toplevel')) == os.path.realpath(D)
g('checkout', '-q', '--detach', '-f', FREEZE)
import controls89 as C  # frozen generator helpers (entry, bump, README_BLOCK, teaches_quote)
import measure89 as M

SRC0 = open(os.path.join(D, 'corpus/SOURCES.md')).read()
README0 = open(os.path.join(D, 'corpus/README.md')).read()
POP = json.load(open(os.path.join(D, 'reports/round-89/claims.json')))['F']['population']
URL = {rid: M.urls(M.rows(SRC0)[rid][1])[0] for rid in POP}
BOILER = {  # site chrome, not the row's teaching
    'S009': 'Conlang Atlas of Language Structures', 'S012': 'Computer Science > Computation and Language',
    'S020': 'Computer Science > Computation and Language', 'S021': 'Computer Science > Computation and Language',
    'S031': 'Best Practices in Research Reporting', 'S033': 'Best Practices in Research Reporting',
    'S084': 'International SignWriting Community', 'S104': 'Creative Commons Attribution 4.0 International License',
    'S105': 'child_language_count', 'S106': 'Subclassification references', 'S107': 'child_language_count',
    'S157': 'International Day of the Intangible Cultural Heritage',
    'S163': 'International Day of the Intangible Cultural Heritage'}
GOOD = list(BOILER)


def put(rel, data):
    p = os.path.join(D, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb' if isinstance(data, bytes) else 'w') as f:
        f.write(data)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def reset():
    g('checkout', '-q', '--detach', '-f', FREEZE)
    g('clean', '-qfd')


def commit(msg):
    g('add', '-A')
    g('commit', '-q', '--allow-empty', '-m', msg)
    return g('rev-parse', 'HEAD')


def run(lands, claim, freeze=FREEZE):
    cmd = [sys.executable, '-B', os.path.join(D, 'reports/round-89/measure89.py'), '--root', D, '--freeze', freeze,
           '--lands', lands, '--claim', claim, '--work', R]
    p = subprocess.run(cmd, capture_output=True)
    return p.returncode, p.stdout.decode(errors='replace'), p.stderr.decode(errors='replace')


def f_lesson(ids, quote_of, extra=''):
    lines = ['# r89 probe\n\n']
    for rid in POP:
        if rid in ids:
            lines.append('- %s LOCATED recheck 90d\u21922027-05-03 %s accessed 2026-11-04: "%s"\n' % (rid, URL[rid], quote_of(rid)))
        else:
            lines.append('- %s NOT-LOCATED: probe\n' % rid)
    return ''.join(lines) + extra


def f_bump(ids):
    return C.bump(SRC0, ids)


def man_entry(rid, url, rel, body, fetched='2026-11-04T19:10:48-03:00'):
    return dict(url=url, http_status=200, fetched_at=fetched, capture=rel, sha256=sha(body))


def f_boiler(extra_lesson='', urlf=None, fetched='2026-11-04T19:10:48-03:00'):
    put('corpus/SOURCES.md', f_bump(GOOD))
    man = {}
    for rid in GOOD:
        body = open(os.path.join(CAP, rid + '.html'), 'rb').read()
        rel = 'reports/round-89/rechecks/%s.html' % rid
        put(rel, body)
        man[rid] = man_entry(rid, urlf(URL[rid]) if urlf else URL[rid], rel, body, fetched)
    put('reports/round-89/rechecks/manifest.json', json.dumps({'rows': man}, indent=1))
    put('corpus/lessons/round-89.md', f_lesson(GOOD, lambda r: BOILER[r], extra_lesson))


def f_selfcap(capture_path, ids=GOOD, lesson_fn=None, urlf=None, src=None):
    put('corpus/SOURCES.md', src if src is not None else f_bump(ids))
    lesson = (lesson_fn or (lambda: f_lesson(ids, lambda r: C.teaches_quote(SRC0, r)[0])))()
    put('corpus/lessons/round-89.md', lesson)
    body = open(os.path.join(D, capture_path), 'rb').read()
    man = {rid: man_entry(rid, urlf(URL[rid]) if urlf else URL[rid], capture_path, body) for rid in ids}
    put('reports/round-89/rechecks/manifest.json', json.dumps({'rows': man}, indent=1))


NEW = ['S936', 'S937', 'S938']
XURL = {'S936': 'https://example.com/', 'S937': 'https://example.net/', 'S938': 'https://example.org/'}
XCAP = {'S936': 'X1', 'S937': 'X2', 'S938': 'X3'}
XQ = 'This domain is for use in documentation examples without needing permission.'


def offtopic_entry(fenced=False):
    body = '# Sourdough starter care\n\n- topic: control\n- sources: %s\n- verified-at: 2026-11-04\n- recheck: 90d\n\n' % ' '.join(NEW)
    sect = ''.join('## Loaf %d\n\n' % i + ('Feed the starter flour and water daily %s. ' % ' '.join(NEW)) * 25 + '\n\n' for i in range(6))
    table = '| a | b | c |\n|---|\n' + ''.join('|%d|\n' % i for i in range(5))
    if fenced:
        return body + '```\n' + sect + table + '```\n' + 'x' * 0
    return body + sect + table


def c_land(entry_text, capture_mode='genuine'):
    put(C.ENTRY, entry_text)
    put('corpus/README.md', README0.replace('## linguistics/ (33)', '## linguistics/ (34)') + C.README_BLOCK)
    add = ''.join('| %s | Probe %s \u2014 %s | web | A | s | a | t | mined | 2026-11-04 | 90d | %s |\n' % (r, r, XURL[r], C.ENTRY) for r in NEW)
    put('corpus/SOURCES.md', SRC0.rstrip('\n') + '\n' + add)
    lesson = ''.join('- %s admit A/mined %s accessed 2026-11-04: "%s"\n' % (r, XURL[r], XQ) for r in NEW)
    put('corpus/lessons/round-89.md', lesson)
    man = {}
    for r in NEW:
        if capture_mode == 'genuine':
            body = open(os.path.join(CAP, XCAP[r] + '.html'), 'rb').read()
            rel = 'reports/round-89/evidence/%s.html' % r
            put(rel, body)
        else:  # capture is the committed lesson file itself
            rel = 'corpus/lessons/round-89.md'
            body = lesson.encode()
        man[r] = man_entry(r, XURL[r], rel, body)
    put('reports/round-89/evidence/manifest.json', json.dumps({'rows': man}, indent=1))


def shadow_src():
    dup = ''.join(l + '\n' for l in f_bump(GOOD).splitlines() if M.ROW_RE.match(l) and l.split('|')[1].strip() in GOOD)
    return SRC0.rstrip('\n') + '\n\n<!-- archived copy\n```\n' + dup + '```\n-->\n'

SCEN = [
    ('F-boilerplate-quote-genuine-capture', 'F', lambda: f_boiler()),
    ('F-capture-is-SOURCES.md', 'F', lambda: f_selfcap('corpus/SOURCES.md')),
    ('F-located-and-not-located-same-id', 'F', lambda: f_boiler(extra_lesson=''.join('- %s NOT-LOCATED: page gone\n' % r for r in GOOD))),
    ('F-NOT_LOCATED-underscore-and-NOT-LOCATED-space', 'F', lambda: f_selfcap('corpus/SOURCES.md', lesson_fn=lambda: f_lesson(GOOD, lambda r: C.teaches_quote(SRC0, r)[0]).replace(' LOCATED recheck', ' NOT LOCATED recheck', 6).replace(' LOCATED recheck', ' NOT_LOCATED recheck'))),
    ('F-wayback-1999-timestamp', 'F', lambda: f_boiler(urlf=lambda u: 'https://web.archive.org/web/19990101000000/' + u)),
    ('F-wayback-suffix-foreign-host', 'F', lambda: f_boiler(urlf=lambda u: 'https://web.archive.org/web/2026/https://evil.invalid/?u=' + u)),
    ('F-fetched_at-prefix-junk', 'F', lambda: f_boiler(fetched='2026-11-04 (not actually fetched)')),
    ('F-shadow-duplicate-rows-in-comment', 'F', lambda: f_selfcap('corpus/SOURCES.md', src=shadow_src())),
    ('C-offtopic-filler-genuine-captures', 'C', lambda: c_land(offtopic_entry())),
    ('C-capture-is-lesson-file', 'C', lambda: c_land(offtopic_entry(), 'self')),
    ('C-headings-table-inside-code-fence-1cell-rows', 'C', lambda: c_land(offtopic_entry(fenced=True))),
]


def main():
    out = []
    for name, claim, build in SCEN:
        reset()
        build()
        lands = commit(name)
        rc, so, se = run(lands, claim)
        verdict = [l for l in so.splitlines() if l.startswith('ACCEPT-')]
        fails = re.findall(r'^LEG FAIL (\S+)', so, re.M)
        extra = ''
        if name.startswith('F-shadow'):
            p = subprocess.run([sys.executable, '-B', os.path.join(D, 'tools/check-sources-recheck.py'), '--registry',
                                os.path.join(D, 'corpus/SOURCES.md'), '--as-of', '2026-11-04', '--window', '90'], capture_output=True)
            first = {}
            for l in open(os.path.join(D, 'corpus/SOURCES.md')).read().splitlines():
                if M.ROW_RE.match(l):
                    first.setdefault(l.split('|')[1].strip(), l.split('|')[10].strip())
            extra = ' recheck-auditor rc=%d %s | first-row recheck S009=%s' % (p.returncode, p.stdout.decode().strip().splitlines()[-1], first['S009'])
        out.append(dict(scenario=name, claim=claim, lands=lands, rc=rc, verdict=verdict, fail_legs=fails, stdout=so, stderr=se, extra=extra))
        print('%s claim=%s rc=%d %s fail=%s%s' % (name, claim, rc, verdict[-1] if verdict else '-', ','.join(fails) or '-', extra))
    # refusal probes
    reset()
    ref = []
    put('reports/round-89/claims.json', '{"broken": ')
    badfreeze = commit('malformed claims freeze')
    landsbad = commit('lands on malformed freeze')
    g('checkout', '-q', '--detach', '-f', BASE)
    offchain = commit('lands off freeze chain')
    g('checkout', '-q', '--detach', '-f', FREEZE)
    g('checkout', '-q', '-b', 'probe-side')
    side = commit('side')
    g('checkout', '-q', '--detach', '-f', FREEZE)
    put('x.txt', 'x')
    main_ = commit('main')
    g('merge', '-q', '--no-ff', '-m', 'merge side', side)
    merged = g('rev-parse', 'HEAD')
    tag = (g('tag', '-a', '-m', 't', 'probe-t', FREEZE), g('rev-parse', 'probe-t'))[1]
    probes = [
        ('uppercase-hex freeze', FREEZE.upper(), FREEZE, 'F'),
        ('short sha lands', FREEZE, FREEZE[:12], 'F'),
        ('annotated tag object as freeze', tag, FREEZE, 'F'),
        ('lands==base', FREEZE, BASE, 'C'),
        ('lands==freeze (do-nothing, graded)', FREEZE, FREEZE, 'C'),
        ('freeze off first-parent (lands from base)', FREEZE, offchain, 'F'),
        ('freeze == base (claims.json absent)', BASE, FREEZE, 'F'),
        ('malformed claims.json at freeze', badfreeze, landsbad, 'F'),
        ('freeze on second-parent only', side, merged, 'F'),
    ]
    for name, fz, ld, cl in probes:
        rc, so, se = run(ld, cl, fz)
        last = (so.strip().splitlines() or ['-'])[-1]
        ref.append(dict(probe=name, freeze=fz, lands=ld, claim=cl, rc=rc, last=last, stderr=se))
        print('REFUSAL %s rc=%d %s' % (name, rc, last[:160]))
    json.dump(dict(scenarios=out, refusals=ref), open(os.path.join(R, 'probe89-results.json'), 'w'), indent=1)
    reset()


main()
