#!/usr/bin/env python3
"""kotodama round-89 counter (claims F / freshness and C / coverage).

Every constant comes from `git show <freeze>:reports/round-89/claims.json`;
every graded byte is read with `git show <lands>:<path>` (QUALITY 19/25/26).
The one repository tool a leg executes (claim C, INDEX) runs the bytes
pinned at the freeze commit over a `git archive` of the lands revision
(QUALITY 28).

Usage:
  measure89.py --root R --freeze F --lands L --claim F|C --work DIR [--receipt PATH]
  measure89.py --selftest --work DIR [--receipt PATH]

Exit 0 PASS, 1 FAIL, 2 refused (never a PASS): a revision that is not a
full 40-hex commit, a freeze off the lands first-parent chain, lands equal
to the frozen base, an unreadable frozen claims.json, or a frozen leg list
that differs from this counter's leg table (LEGCOUNT). lands equal to the
freeze is graded and is the do-nothing control.

Text comparison: NFKC, casefold, every run of non-letter/non-digit
characters becomes one space; a quote matches when its normalised string
occurs inside the normalised capture between word boundaries.

--selftest builds a throwaway git fixture under --work (git -C <fixture>
on every call, toplevel verified), runs this file's public CLI as a
subprocess per scenario, retains raw stdout/stderr/rc, and asserts the
clean scenarios PASS with exit 0 and every mutant exits 1 with its named
`LEG FAIL <NAME>` line observed (QUALITY 35). It removes its fixture.
--work must be an existing directory; nothing is written under /tmp unless
the caller passes such a directory.
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
import tarfile
import io
import unicodedata

CLAIMS = 'reports/round-89/claims.json'
SELF = 'reports/round-89/measure89.py'
LEGS = {
    'F': ['FROZENCFG', 'ADVANCED', 'BACKED', 'DISPOSED', 'OTHERCELLS'],
    'C': ['FROZENCFG', 'ENTRY', 'TABLE', 'NEWIDS', 'GATE', 'CAPTURE', 'INDEX', 'APPENDONLY'],
}
HEX40 = re.compile(r'^[0-9a-f]{40}$')
ROW_RE = re.compile(r'^\s{0,3}\|\s*S\d{3,}\s*\|')
URL_RE = re.compile(r'https?://[^\s;<>\]"`]+')
QUOTE_RE = re.compile(r'"([^"]+)"|\u201c([^\u201d]+)\u201d')
LOCATED_RE = re.compile(r'(?<![A-Za-z-])LOCATED\b')
NOTLOC_RE = re.compile(r'\bNOT-LOCATED\b')


class Refused(Exception):
    pass


def git(root, *args, check=False):
    p = subprocess.run(['git', '-C', str(root)] + list(args), capture_output=True)
    if check and p.returncode != 0:
        raise Refused('git %s: %s' % (' '.join(args), p.stderr.decode(errors='replace').strip()))
    return p


def show(root, rev, path):
    p = git(root, "show", "%s:%s" % (rev, path))
    return p.stdout if p.returncode == 0 else None


def norm(s):
    s = unicodedata.normalize('NFKC', s).casefold()
    return ' '.join(re.sub(r'[^\w]|_', ' ', s).split())


def contains(hay, needle):
    n = norm(needle)
    return bool(n) and (' ' + n + ' ') in (' ' + norm(hay) + ' ')


def rows(text):
    out = {}
    for line in text.splitlines():
        if ROW_RE.match(line):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            out[cells[0]] = cells
    return out


def urls(cell):
    return [u.rstrip('.,;:\'') .rstrip(')') for u in URL_RE.findall(cell)]


def url_ok(candidate, row_cell):
    for u in urls(row_cell):
        if candidate == u or (candidate.startswith('https://web.archive.org/web/') and candidate.endswith(u)):
            return True
    return False


def first_quote(line):
    m = QUOTE_RE.search(line)
    return (m.group(1) or m.group(2)) if m else None


def quote_ok(q, cfg):
    return q is not None and len(q.split()) <= cfg['quote_max_words'] and len(norm(q)) >= cfg['quote_min_chars']


def leg(name, passed, expected, observed):
    return dict(leg=name, passed=bool(passed), expected=expected, observed=observed)


def load_manifest(root, lands, path):
    raw = show(root, lands, path)
    if raw is None:
        return {}
    try:
        return json.loads(raw.decode()).get('rows', {})
    except (ValueError, AttributeError):
        return {}


def capture_check(root, lands, man, rid, row_cell, quote, as_of):
    m = man.get(rid)
    if not isinstance(m, dict):
        return 'no manifest entry'
    cap = show(root, lands, str(m.get('capture', '')))
    if cap is None:
        return 'capture not committed'
    if hashlib.sha256(cap).hexdigest() != m.get('sha256'):
        return 'capture sha256 mismatch'
    if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:
        return 'http_status not 2xx'
    if not str(m.get('fetched_at', '')).startswith(as_of):
        return 'fetched_at not as_of'
    if not url_ok(str(m.get('url', '')), row_cell):
        return 'manifest url not a row url'
    if not contains(cap.decode('utf-8', errors='replace'), quote):
        return 'quote absent from capture'
    return None


def claim_f(root, cfg, base, lands, freeze, work):
    c = cfg['F']
    out = [frozencfg(root, freeze, lands)]
    b_rows = rows(show(root, base, cfg['sources']).decode())
    l_raw = show(root, lands, cfg['sources'])
    l_rows = rows(l_raw.decode()) if l_raw else {}
    lesson = (show(root, lands, cfg['lesson']) or b'').decode('utf-8', errors='replace').splitlines()
    as_of = datetime.date.fromisoformat(cfg['as_of'])
    lo = as_of + datetime.timedelta(days=c['window_days'])
    hi = as_of + datetime.timedelta(days=c['max_days'])
    man = load_manifest(root, lands, c['manifest'])
    advanced, changed, bad = [], [], {}
    for rid in c['population']:
        old, new = b_rows[rid][9], (l_rows.get(rid) or [''] * 11)[9]
        if old == new:
            continue
        changed.append(rid)
        try:
            d = datetime.date.fromisoformat(new)
            if lo < d <= hi:
                advanced.append(rid)
        except ValueError:
            pass
        lines = [x for x in lesson if re.search(r'\b%s\b' % rid, x) and LOCATED_RE.search(x) and not NOTLOC_RE.search(x)]
        good = [x for x in lines if (('recheck %s\u2192%s' % (old, new)) in x or ('recheck %s->%s' % (old, new)) in x) and cfg['as_of'] in x]
        if not good:
            bad[rid] = 'no LOCATED lesson line with recheck old->new and access date'
            continue
        q = first_quote(good[0])
        if not quote_ok(q, cfg):
            bad[rid] = 'lesson quote missing or outside word/char bounds'
            continue
        why = capture_check(root, lands, man, rid, b_rows[rid][1], q, cfg['as_of'])
        if why:
            bad[rid] = why
    out.append(leg('ADVANCED', len(advanced) >= c['advance_min'], '>=%d' % c['advance_min'], len(advanced)))
    out.append(leg('BACKED', not bad, 'every changed population recheck backed', {'changed': len(changed), 'unbacked': bad}))
    undisposed = [rid for rid in c['population']
                  if not any(re.search(r'\b%s\b' % rid, x) and (NOTLOC_RE.search(x) or LOCATED_RE.search(x)) for x in lesson)]
    out.append(leg('DISPOSED', not undisposed, 'every population id has a LOCATED/NOT-LOCATED line', undisposed))
    drift = []
    for rid, cells in b_rows.items():
        lc = l_rows.get(rid)
        if lc is None or len(lc) != len(cells):
            drift.append(rid)
        elif rid in c['population']:
            if [x for i, x in enumerate(cells) if i != 9] != [x for i, x in enumerate(lc) if i != 9]:
                drift.append(rid)
        elif cells[9] != lc[9]:
            drift.append(rid)
    out.append(leg('OTHERCELLS', not drift, 'population: only recheck changes; others: recheck unchanged', drift))
    return out


def frozencfg(root, freeze, lands):
    diff = [p for p in (CLAIMS, SELF) if show(root, freeze, p) != show(root, lands, p)]
    return leg('FROZENCFG', not diff, 'claims.json and counter equal to freeze blobs', diff)


def tables(text):
    found, block = [], []
    for line in text.splitlines() + ['']:
        if line.lstrip().startswith('|'):
            block.append(line.strip())
            continue
        if len(block) >= 2 and re.match(r'^\|[\s:|-]+\|?$', block[1]):
            cols = len([x for x in block[0].strip('|').split('|')])
            found.append((cols, len(block) - 2))
        block = []
    return found


def claim_c(root, cfg, base, lands, freeze, work):
    c = cfg['C']
    out = [frozencfg(root, freeze, lands)]
    entry_raw = show(root, lands, c['entry'])
    at_base = show(root, base, c['entry']) is not None
    text = entry_raw.decode('utf-8', errors='replace') if entry_raw else ''
    head = '\n'.join(text.splitlines()[:80])
    heads = len(re.findall(r'^## ', text, re.M))
    keys = [k for k in c['header_keys'] if not re.search(r'^- %s' % re.escape(k), head, re.M)]
    ok = entry_raw is not None and not at_base and len(entry_raw) >= c['min_bytes'] and heads >= c['min_headings'] and not keys
    out.append(leg('ENTRY', ok, 'absent at base; >=%d bytes; >=%d headings; header keys' % (c['min_bytes'], c['min_headings']),
                   dict(at_base=at_base, bytes=len(entry_raw or b''), headings=heads, missing_keys=keys)))
    t = tables(text)
    out.append(leg('TABLE', any(cols >= c['table_min_cols'] and n >= c['table_min_rows'] for cols, n in t),
                   'a table >=%d cols and >=%d data rows' % (c['table_min_cols'], c['table_min_rows']), t))
    b_rows = rows(show(root, base, cfg['sources']).decode())
    l_raw = show(root, lands, cfg['sources'])
    l_rows = rows(l_raw.decode()) if l_raw else {}
    cited = sorted(set(re.findall(r'\bS\d{3,}\b', text)) - set(b_rows))
    qual, unq = [], {}
    for rid in cited:
        r = l_rows.get(rid)
        if r is None:
            unq[rid] = 'not in lands registry'
        elif r[3] not in ('A', 'B') or r[7] != 'mined' or r[8] != cfg['as_of'] or c['entry'].split('corpus/', 1)[-1] not in r[10] and c['entry'] not in r[10]:
            unq[rid] = 'tier/status/opened/used-by'
        else:
            qual.append(rid)
    out.append(leg('NEWIDS', len(qual) >= c['new_ids_min'] and not unq, '>=%d new mined A/B ids opened as_of, none fabricated' % c['new_ids_min'],
                   dict(qualifying=qual, unqualified=unq)))
    lesson = (show(root, lands, cfg['lesson']) or b'').decode('utf-8', errors='replace').splitlines()
    man = load_manifest(root, lands, c['manifest'])
    gate_bad, cap_bad = {}, {}
    for rid in qual:
        cand = [x for x in lesson if re.search(r'\b%s\b' % rid, x) and cfg['as_of'] in x
                and any(url_ok(u, l_rows[rid][1]) for u in urls(x)) and quote_ok(first_quote(x), cfg)]
        if not cand:
            gate_bad[rid] = 'no gate line with row url, access date and bounded quote'
            continue
        why = capture_check(root, lands, man, rid, l_rows[rid][1], first_quote(cand[0]), cfg['as_of'])
        if why:
            cap_bad[rid] = why
    out.append(leg('GATE', bool(qual) and not gate_bad, 'every qualifying id has a gate line', gate_bad))
    out.append(leg('CAPTURE', bool(qual) and not gate_bad and not cap_bad, 'every gate quote occurs in its committed capture', cap_bad))
    readme = (show(root, lands, c['readme']) or b'').decode('utf-8', errors='replace')
    row_ok = re.search(r'^- `%s` \u2014 ' % re.escape(os.path.basename(c['entry'])), readme, re.M) is not None
    tool = show(root, freeze, c['index_tool'])
    rc = None
    if tool is not None and row_ok:
        tree = os.path.join(work, 'tree-c')
        shutil.rmtree(tree, ignore_errors=True)
        os.makedirs(tree)
        arc = git(root, 'archive', '--format=tar', lands, 'corpus')
        with tarfile.open(fileobj=io.BytesIO(arc.stdout)) as tf:
            tf.extractall(tree, filter=lambda m, p: None if (m.issym() or m.islnk()) else tarfile.data_filter(m, p))
        tp = os.path.join(work, 'index-tool-freeze.py')
        with open(tp, 'wb') as f:
            f.write(tool)
        rc = subprocess.run([sys.executable, '-B', tp] + [a.replace('{tree}', tree) for a in c['index_args']],
                            capture_output=True).returncode
        shutil.rmtree(tree, ignore_errors=True)
    out.append(leg('INDEX', row_ok and rc == 0, 'README row and freeze-pinned index tool rc0', dict(row=row_ok, tool_rc=rc)))
    drift = []
    for rid, cells in b_rows.items():
        lc = l_rows.get(rid)
        if lc is None or len(lc) != len(cells) or [cells[i] for i in (0, 1, 2, 3, 4, 5, 6, 8)] != [lc[i] for i in (0, 1, 2, 3, 4, 5, 6, 8)]:
            drift.append(rid)
    out.append(leg('APPENDONLY', not drift, 'base rows: only status/recheck/used-by may change', drift))
    return out


def resolve(root, rev):
    if not HEX40.match(rev or ''):
        raise Refused('not a 40-hex revision: %r' % rev)
    p = git(root, 'rev-parse', '--verify', '-q', rev + '^{commit}')
    if p.returncode != 0 or p.stdout.decode().strip() != rev:
        raise Refused('not a commit: %s' % rev)
    return rev


def grade(args):
    root = args.root
    freeze, lands = resolve(root, args.freeze), resolve(root, args.lands)
    raw = show(root, freeze, CLAIMS)
    if raw is None:
        raise Refused('frozen claims.json unreadable at freeze')
    cfg = json.loads(raw.decode())
    base = cfg['base']
    if lands == base:
        raise Refused('lands equals frozen base')
    chain = git(root, 'rev-list', '--first-parent', lands, check=True).stdout.decode().split()
    if freeze not in chain:
        raise Refused('freeze is not on the lands first-parent chain')
    frozen_legs = cfg['legs'][args.claim]
    if frozen_legs != LEGS[args.claim]:
        raise Refused('LEGCOUNT frozen %s != counter %s' % (frozen_legs, LEGS[args.claim]))
    legs = (claim_f if args.claim == 'F' else claim_c)(root, cfg, base, lands, freeze, args.work)
    return cfg, legs


def header(root, lands, freeze, claim, n):
    me = open(os.path.abspath(__file__), 'rb').read()
    main = git(root, 'rev-parse', '-q', '--verify', 'refs/heads/main').stdout.decode().strip() or 'n/a'
    tree = git(root, 'rev-parse', lands + '^{tree}').stdout.decode().strip()
    return ['# counter: %s claim %s' % (SELF, claim),
            '# counter sha256 (self): %s' % hashlib.sha256(me).hexdigest(),
            '# stamped revision: %s' % lands,
            '# evaluated revision: %s (all graded bytes via git show)' % lands,
            '# measured revision (lane main): %s' % main,
            '# tree: %s' % tree,
            '# freeze: %s' % freeze,
            '# frozen legs: %d (%s)' % (n, ','.join(LEGS[claim]))]


def run_claim(args):
    n = len(LEGS[args.claim])
    tag = 'ACCEPT-%s-89' % args.claim
    try:
        cfg, legs = grade(args)
    except Refused as e:
        lines = ['%s: FAIL legs=0/%d (refused: %s)' % (tag, n, e)]
        emit(lines, args.receipt)
        return 2
    except Exception as e:  # a crash is a FAIL with a verdict line, never a bare traceback
        lines = ['%s: FAIL legs=0/%d (error: %s: %s)' % (tag, n, type(e).__name__, e)]
        emit(lines, args.receipt)
        return 1
    lines = header(args.root, args.lands, args.freeze, args.claim, n)
    for l in legs:
        lines.append('LEG %s %s expected=%s observed=%s' % ('PASS' if l['passed'] else 'FAIL', l['leg'],
                                                           json.dumps(l['expected']), json.dumps(l['observed'], sort_keys=True)))
    k = sum(l['passed'] for l in legs)
    lines.append('%s: %s legs=%d/%d' % (tag, 'PASS' if k == n else 'FAIL', k, n))
    emit(lines, args.receipt)
    return 0 if k == n else 1


def emit(lines, receipt):
    text = '\n'.join(lines) + '\n'
    sys.stdout.write(text)
    if receipt:
        with open(receipt, 'w') as f:
            f.write(text)


# ---------------------------------------------------------------- selftest
HDR = '| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
FX_TOOL = ('import sys,pathlib\nr=pathlib.Path(sys.argv[sys.argv.index("--root")+1])\n'
           'readme=(r/"corpus/README.md").read_text()\n'
           'miss=[p.name for p in (r/"corpus/knowledge").rglob("*.md") if "`%s`"%p.name not in readme]\n'
           'print("FIXTURE-INDEX", miss); sys.exit(1 if miss else 0)\n')
CAP_TEXT = 'Intro words here. The quick fixture source states that evidential suffixes mark how the speaker knows. More text.'
QUOTE = 'evidential suffixes mark how the speaker knows'
ENTRY_TEXT = ('# Fixture entry\n\n- topic: fixture\n- sources: S004\n- verified-at: 2026-11-04\n- recheck: 90d\n\n'
              + ''.join('## H%d\n\ntext S004 body.\n\n' % i for i in range(5))
              + '| a | b | c |\n|---|---|---|\n' + ''.join('| %d | x | y |\n' % i for i in range(5)))


def fx_row(rid, url, recheck='90d', status='mined', opened='2026-10-19', used='—', tier='A'):
    return '| %s | Fixture %s — %s | web | %s | s | a | t | %s | %s | %s | %s |\n' % (rid, rid, url, tier, status, opened, recheck, used)


def fx_sources(s1='90d', extra='', tweak=None):
    rows_ = [fx_row('S001', 'https://example.org/a', s1), fx_row('S002', 'https://example.org/b'),
             fx_row('S003', 'https://example.org/c')]
    if tweak:
        rows_ = [tweak(r) for r in rows_]
    return '# Sources\n\n' + HDR + ''.join(rows_) + extra


def fx_cfg(base, legs=None):
    return {
        'round': 89, 'base': base, 'as_of': '2026-11-04', 'sources': 'corpus/SOURCES.md',
        'lesson': 'corpus/lessons/round-89.md', 'quote_max_words': 25, 'quote_min_chars': 20,
        'legs': legs or LEGS,
        'F': {'population': ['S001', 'S002'], 'advance_min': 1, 'window_days': 90, 'max_days': 366,
              'manifest': 'reports/round-89/rechecks/manifest.json'},
        'C': {'entry': 'corpus/knowledge/linguistics/fx.md', 'min_bytes': 200, 'min_headings': 5,
              'header_keys': ['topic:', 'sources:', 'verified-at:', 'recheck:'], 'table_min_cols': 3,
              'table_min_rows': 5, 'new_ids_min': 1, 'manifest': 'reports/round-89/evidence/manifest.json',
              'readme': 'corpus/README.md', 'index_tool': 'tools/check-corpus-index.py',
              'index_args': ['--root', '{tree}']},
    }


def fx_clean():
    cap = CAP_TEXT.encode()
    sha = hashlib.sha256(cap).hexdigest()
    new_row = fx_row('S004', 'https://example.org/d', opened='2026-11-04', used='corpus/knowledge/linguistics/fx.md')
    return {
        'corpus/SOURCES.md': fx_sources('2027-05-03', new_row),
        'corpus/lessons/round-89.md': ('# r89\n\n- S001 LOCATED recheck 90d\u21922027-05-03, https://example.org/a accessed 2026-11-04: "%s"\n'
                                       '- S002 NOT-LOCATED: fixture page left unchanged\n'
                                       '- S004 admit A/mined https://example.org/d accessed 2026-11-04: "%s"\n') % (QUOTE, QUOTE),
        'reports/round-89/rechecks/S001.txt': CAP_TEXT,
        'reports/round-89/rechecks/manifest.json': json.dumps({'rows': {'S001': {'url': 'https://example.org/a', 'http_status': 200,
                                                               'fetched_at': '2026-11-04T12:00:00Z', 'capture': 'reports/round-89/rechecks/S001.txt', 'sha256': sha}}}),
        'reports/round-89/evidence/S004.txt': CAP_TEXT,
        'reports/round-89/evidence/manifest.json': json.dumps({'rows': {'S004': {'url': 'https://example.org/d', 'http_status': 200,
                                                               'fetched_at': '2026-11-04T12:00:00Z', 'capture': 'reports/round-89/evidence/S004.txt', 'sha256': sha}}}),
        'corpus/knowledge/linguistics/fx.md': ENTRY_TEXT,
        'corpus/README.md': '# idx\n\n- `old.md` \u2014 old\n- `fx.md` \u2014 fixture\n',
    }


def selftest(work, receipt):
    import tempfile
    os.makedirs(work, exist_ok=True)
    d = tempfile.mkdtemp(prefix='measure89-selftest-', dir=work)
    env = dict(os.environ, GIT_AUTHOR_NAME='selftest', GIT_AUTHOR_EMAIL='selftest@invalid',
               GIT_COMMITTER_NAME='selftest', GIT_COMMITTER_EMAIL='selftest@invalid')
    results, ok = [], True
    try:
        subprocess.run(['git', '-C', d, 'init', '-q'], check=True)
        top = subprocess.run(['git', '-C', d, 'rev-parse', '--show-toplevel'], capture_output=True).stdout.decode().strip()
        if os.path.realpath(top) != os.path.realpath(d):
            raise SystemExit('fixture toplevel mismatch')

        def write(files):
            for p, body in files.items():
                fp = os.path.join(d, p)
                if body is None:
                    if os.path.exists(fp):
                        os.remove(fp)
                    continue
                os.makedirs(os.path.dirname(fp), exist_ok=True)
                with open(fp, 'w') as f:
                    f.write(body)

        def commit(msg):
            subprocess.run(['git', '-C', d, 'add', '-A'], check=True, env=env)
            subprocess.run(['git', '-C', d, 'commit', '-q', '--allow-empty', '-m', msg], check=True, env=env)
            return subprocess.run(['git', '-C', d, 'rev-parse', 'HEAD'], capture_output=True).stdout.decode().strip()

        write({'corpus/SOURCES.md': fx_sources(), 'corpus/README.md': '# idx\n\n- `old.md` \u2014 old\n',
               'corpus/knowledge/linguistics/old.md': '# old\n', 'tools/check-corpus-index.py': FX_TOOL})
        base = commit('base')
        me = open(os.path.abspath(__file__)).read()
        write({CLAIMS: json.dumps(fx_cfg(base), indent=1), SELF: me})
        freeze = commit('freeze')

        def scenario(name, files):
            subprocess.run(['git', '-C', d, 'checkout', '-q', '--detach', freeze], check=True)
            write(files)
            return commit(name)

        clean = fx_clean()
        cases = []

        def mut(**kw):
            f = dict(clean)
            f.update(kw)
            return f
        cap_sha = hashlib.sha256(CAP_TEXT.encode()).hexdigest()
        lands = {
            'clean': scenario('clean', clean),
            'bumponly': scenario('bumponly', mut(**{'reports/round-89/rechecks/S001.txt': None, 'reports/round-89/rechecks/manifest.json': None})),
            'wrongquote': scenario('wrongquote', mut(**{'reports/round-89/rechecks/S001.txt': 'unrelated words only',
                                   'reports/round-89/rechecks/manifest.json': json.dumps({'rows': {'S001': {'url': 'https://example.org/a', 'http_status': 200,
                                    'fetched_at': '2026-11-04T1', 'capture': 'reports/round-89/rechecks/S001.txt',
                                    'sha256': hashlib.sha256(b'unrelated words only').hexdigest()}}})})),
            'badurl': scenario('badurl', mut(**{'reports/round-89/rechecks/manifest.json': json.dumps({'rows': {'S001': {'url': 'https://evil.example/a', 'http_status': 200,
                               'fetched_at': '2026-11-04T1', 'capture': 'reports/round-89/rechecks/S001.txt', 'sha256': cap_sha}}})})),
            'undisposed': scenario('undisposed', mut(**{'corpus/lessons/round-89.md': clean['corpus/lessons/round-89.md'].replace('- S002 NOT-LOCATED: fixture page left unchanged\n', '')})),
            'cellchange': scenario('cellchange', mut(**{'corpus/SOURCES.md': clean['corpus/SOURCES.md'].replace('| S002 | Fixture S002 — https://example.org/b | web | A | s | a | t |', '| S002 | Fixture S002 — https://example.org/b | web | A | s | a | edited |')})),
            'cfgdrift': scenario('cfgdrift', mut(**{CLAIMS: json.dumps(dict(fx_cfg(base), note='drift'), indent=1)})),
            'fakeid': scenario('fakeid', mut(**{'corpus/knowledge/linguistics/fx.md': ENTRY_TEXT + '\nAlso S999.\n'})),
            'nogate': scenario('nogate', mut(**{'corpus/lessons/round-89.md': clean['corpus/lessons/round-89.md'].replace('- S004 admit', '- S00x admit')})),
            'nocapture': scenario('nocapture', mut(**{'reports/round-89/evidence/S004.txt': 'other text entirely, nothing quoted'})),
            'stubtool': scenario('stubtool', mut(**{'tools/check-corpus-index.py': 'import sys; sys.exit(0)\n',
                                 'corpus/README.md': '# idx\n\n- `fx.md` \u2014 fixture\n'})),
            'oldrow': scenario('oldrow', mut(**{'corpus/SOURCES.md': clean['corpus/SOURCES.md'].replace('| S003 | Fixture S003 — https://example.org/c | web | A |', '| S003 | Fixture S003 — https://example.org/c | web | B |')})),
            'shortentry': scenario('shortentry', mut(**{'corpus/knowledge/linguistics/fx.md': '# x\n- topic: t\nS004\n'})),
        }
        plan = [
            ('clean', 'F', 'clean', 0, None), ('clean', 'C', 'clean', 0, None),
            ('nowork', 'F', freeze, 1, 'ADVANCED'), ('nowork', 'C', freeze, 1, 'ENTRY'),
            ('bumponly', 'F', 'bumponly', 1, 'BACKED'), ('wrongquote', 'F', 'wrongquote', 1, 'BACKED'),
            ('badurl', 'F', 'badurl', 1, 'BACKED'), ('undisposed', 'F', 'undisposed', 1, 'DISPOSED'),
            ('cellchange', 'F', 'cellchange', 1, 'OTHERCELLS'), ('cfgdrift', 'F', 'cfgdrift', 1, 'FROZENCFG'),
            ('cfgdrift', 'C', 'cfgdrift', 1, 'FROZENCFG'), ('fakeid', 'C', 'fakeid', 1, 'NEWIDS'),
            ('nogate', 'C', 'nogate', 1, 'GATE'), ('nocapture', 'C', 'nocapture', 1, 'CAPTURE'),
            ('stubtool', 'C', 'stubtool', 1, 'INDEX'), ('oldrow', 'C', 'oldrow', 1, 'APPENDONLY'),
            ('shortentry', 'C', 'shortentry', 1, 'ENTRY'), ('shortentry', 'C', 'shortentry', 1, 'TABLE'),
            ('refuse-base', 'F', base, 2, None), ('refuse-nonhex', 'C', 'abc', 2, None),
        ]
        for name, claim, target, want_rc, want_leg in plan:
            rev = lands.get(target, target)
            p = subprocess.run([sys.executable, '-B', os.path.join(d, SELF), '--root', d, '--freeze', freeze,
                                '--lands', rev, '--claim', claim, '--work', d], capture_output=True)
            so = p.stdout.decode(errors='replace')
            se = p.stderr.decode(errors='replace')
            if want_rc == 0:
                good = p.returncode == 0 and ('ACCEPT-%s-89: PASS legs=%d/%d' % (claim, len(LEGS[claim]), len(LEGS[claim]))) in so and not se.strip()
            elif want_rc == 2:
                good = p.returncode == 2 and 'refused' in so and 'PASS' not in so.replace('LEG PASS', '')
            else:
                good = p.returncode == 1 and ('LEG FAIL %s ' % want_leg) in so
            ok = ok and good
            results.append(dict(scenario=name, claim=claim, lands=rev, expect_rc=want_rc, expect_leg=want_leg,
                                rc=p.returncode, passed=good, stdout=so, stderr=se))
        # LEGCOUNT refusal: a freeze whose leg list differs
        subprocess.run(['git', '-C', d, 'checkout', '-q', '--detach', base], check=True)
        bad_legs = dict(LEGS, F=LEGS['F'] + ['EXTRA'])
        write({CLAIMS: json.dumps(fx_cfg(base, bad_legs), indent=1), SELF: me})
        f2 = commit('freeze-legcount')
        write(clean)
        l2 = commit('lands-legcount')
        p = subprocess.run([sys.executable, '-B', os.path.join(d, SELF), '--root', d, '--freeze', f2, '--lands', l2,
                            '--claim', 'F', '--work', d], capture_output=True)
        so = p.stdout.decode(errors='replace')
        good = p.returncode == 2 and 'LEGCOUNT' in so
        ok = ok and good
        results.append(dict(scenario='refuse-legcount', claim='F', lands=l2, expect_rc=2, expect_leg='LEGCOUNT', rc=p.returncode,
                            passed=good, stdout=so, stderr=p.stderr.decode(errors='replace')))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    clean_rows = [r for r in results if r['scenario'] == 'clean']
    lines = ['# measure89 selftest; counter sha256 (self): %s' % hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
             'selftest: clean -> exit=%s F=%s C=%s' % (','.join(str(r['rc']) for r in clean_rows),
                                                       *['PASS' if r['passed'] else 'FAIL' for r in clean_rows])]
    for r in results:
        lines.append('%s %s %s rc=%d expect_rc=%d expect_leg=%s' % ('OK ' if r['passed'] else 'BAD', r['scenario'], r['claim'],
                                                                    r['rc'], r['expect_rc'], r['expect_leg']))
    k = sum(r['passed'] for r in results)
    lines.append('SELFTEST: %s %d/%d' % ('PASS' if ok else 'FAIL', k, len(results)))
    emit(lines, receipt)
    if receipt:
        with open(receipt + '.json', 'w') as f:
            json.dump(results, f, indent=1)
    return 0 if ok else 1


def main():
    a = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    a.add_argument('--root')
    a.add_argument('--freeze')
    a.add_argument('--lands')
    a.add_argument('--claim', choices=sorted(LEGS))
    a.add_argument('--work', required=True)
    a.add_argument('--receipt')
    a.add_argument('--selftest', action='store_true')
    args = a.parse_args()
    if not os.path.isdir(args.work):
        print('MEASURE89-ERROR --work must be an existing directory')
        return 2
    if args.selftest:
        return selftest(args.work, args.receipt)
    if not (args.root and args.freeze and args.lands and args.claim):
        print('ACCEPT-?-89: FAIL legs=0/0 (refused: --root --freeze --lands --claim required)')
        return 2
    return run_claim(args)


if __name__ == '__main__':
    sys.exit(main())
