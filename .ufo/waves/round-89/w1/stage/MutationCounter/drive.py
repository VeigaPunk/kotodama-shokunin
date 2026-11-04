#!/usr/bin/env python3
"""Mutation driver for measure89.py (scratch only). One --shared lane clone per mutant."""
import concurrent.futures as cf, hashlib, json, os, re, shutil, subprocess, sys

S = '/fast/scratch/hyaku/kotodama-r89/MutationCounter'
LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
REL = 'reports/round-89/measure89.py'
PRISTINE = open(os.path.join(LANE, REL), 'rb').read()
PSHA = hashlib.sha256(PRISTINE).hexdigest()
assert PSHA == '6bc14bcd541239e7d969d74291af46193fca7ac2e46850c40dc420d777cdf040'
CONTROLS = os.path.join(LANE, 'reports/round-89/controls89.py')

# (id, leg, description, old, new)
M = [
 ('M01', 'FROZENCFG', 'counter self-bytes no longer compared (CLAIMS only)',
  "for p in (CLAIMS, SELF) if show", "for p in (CLAIMS,) if show"),
 ('M02', 'FROZENCFG', 'leg always passes',
  "return leg('FROZENCFG', not diff,", "return leg('FROZENCFG', True,"),
 ('M03', 'ADVANCED', 'threshold >= -> >',
  "len(advanced) >= c['advance_min']", "len(advanced) > c['advance_min']"),
 ('M04', 'ADVANCED', 'lower date bound dropped (as_of+90d)',
  "if lo < d <= hi:", "if d <= hi:"),
 ('M05', 'ADVANCED', 'upper date bound dropped (as_of+366d)',
  "if lo < d <= hi:", "if lo < d:"),
 ('M06', 'BACKED/lesson-line', 'LOCATED / not NOT-LOCATED filter dropped',
  "re.search(r'\\b%s\\b' % rid, x) and LOCATED_RE.search(x) and not NOTLOC_RE.search(x)]", "re.search(r'\\b%s\\b' % rid, x)]"),
 ('M07', 'BACKED/recheck', 'old->new reduced to ->new',
  "(('recheck %s\\u2192%s' % (old, new)) in x or ('recheck %s->%s' % (old, new)) in x)", "(('\\u2192%s' % new) in x or ('->%s' % new) in x)"),
 ('M08', 'BACKED/access-date', 'as_of on lesson line not required',
  "or ('recheck %s->%s' % (old, new)) in x) and cfg['as_of'] in x]", "or ('recheck %s->%s' % (old, new)) in x)]"),
 ('M09', 'BACKED/quote-bounds', 'max-words bound dropped',
  "len(q.split()) <= cfg['quote_max_words'] and", ""),
 ('M10', 'BACKED/quote-bounds', 'min-chars bound dropped',
  " and len(norm(q)) >= cfg['quote_min_chars']", ""),
 ('M11', 'BACKED/capture-presence', 'uncommitted capture read as empty bytes',
  "    if cap is None:\n        return 'capture not committed'\n", "    cap = cap if cap is not None else b''\n"),
 ('M12', 'BACKED/sha', 'sha256 check dropped',
  "    if hashlib.sha256(cap).hexdigest() != m.get('sha256'):\n        return 'capture sha256 mismatch'\n", ""),
 ('M13', 'BACKED/http_status', 'http_status check dropped',
  "    if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:\n        return 'http_status not 2xx'\n", ""),
 ('M14', 'BACKED/fetched_at', 'fetched_at check dropped',
  "    if not str(m.get('fetched_at', '')).startswith(as_of):\n        return 'fetched_at not as_of'\n", ""),
 ('M15', 'BACKED/url_ok', 'manifest url check dropped',
  "    if not url_ok(str(m.get('url', '')), row_cell):\n        return 'manifest url not a row url'\n", ""),
 ('M16', 'BACKED/url_ok', 'wayback prefix not required (any URL ending in a row URL)',
  "candidate == u or (candidate.startswith('https://web.archive.org/web/') and candidate.endswith(u))", "candidate.endswith(u)"),
 ('M17', 'BACKED/contains', 'word-boundary padding dropped (raw substring)',
  "return bool(n) and (' ' + n + ' ') in (' ' + norm(hay) + ' ')", "return bool(n) and n in norm(hay)"),
 ('M18', 'BACKED/contains', 'quote-in-capture check dropped',
  "    if not contains(cap.decode('utf-8', errors='replace'), quote):\n        return 'quote absent from capture'\n", ""),
 ('M19', 'DISPOSED', 'leg always passes',
  "out.append(leg('DISPOSED', not undisposed,", "out.append(leg('DISPOSED', True,"),
 ('M20', 'DISPOSED', 'any line naming the id disposes it',
  "if not any(re.search(r'\\b%s\\b' % rid, x) and (NOTLOC_RE.search(x) or LOCATED_RE.search(x)) for x in lesson)]", "if not any(re.search(r'\\b%s\\b' % rid, x) for x in lesson)]"),
 ('M21', 'OTHERCELLS', 'non-population recheck drift not checked',
  "        elif cells[9] != lc[9]:\n            drift.append(rid)\n    out.append(leg('OTHERCELLS'", "    out.append(leg('OTHERCELLS'"),
 ('M22', 'OTHERCELLS', 'row-length / deleted-row check dropped (deleted rows skipped)',
  "        if lc is None or len(lc) != len(cells):\n            drift.append(rid)\n        elif rid in c['population']:", "        if lc is None:\n            continue\n        elif rid in c['population']:"),
 ('M23', 'ENTRY/bytes', 'min_bytes dropped',
  "len(entry_raw) >= c['min_bytes'] and ", ""),
 ('M24', 'ENTRY/headings', 'min_headings off by one',
  "heads >= c['min_headings'] and not keys", "heads >= c['min_headings'] - 1 and not keys"),
 ('M25', 'ENTRY/keys', 'header keys not required',
  "heads >= c['min_headings'] and not keys", "heads >= c['min_headings']"),
 ('M26', 'ENTRY/absent-at-base', 'absent-at-base not required',
  "ok = entry_raw is not None and not at_base and", "ok = entry_raw is not None and"),
 ('M27', 'TABLE', 'data-row minimum dropped',
  "and n >= c['table_min_rows'] for cols, n in t", "and n >= 0 for cols, n in t"),
 ('M28', 'NEWIDS/tier', 'tier C admitted',
  "r[3] not in ('A', 'B')", "r[3] not in ('A', 'B', 'C')"),
 ('M29', 'NEWIDS/status', 'status mined not required',
  "or r[7] != 'mined' or", "or"),
 ('M30', 'NEWIDS/opened', 'opened == as_of not required',
  "or r[8] != cfg['as_of'] or", "or"),
 ('M31', 'NEWIDS/used-by', 'used-by not required',
  " or c['entry'].split('corpus/', 1)[-1] not in r[10] and c['entry'] not in r[10]:", ":"),
 ('M32', 'NEWIDS/fabricated', 'unregistered cited ids tolerated',
  "len(qual) >= c['new_ids_min'] and not unq,", "len(qual) >= c['new_ids_min'],"),
 ('M33', 'NEWIDS/min', 'new_ids_min dropped',
  "len(qual) >= c['new_ids_min'] and not unq,", "not unq,"),
 ('M34', 'GATE', 'gate line need not carry a row URL',
  "                and any(url_ok(u, l_rows[rid][1]) for u in urls(x)) and quote_ok", "                and quote_ok"),
 ('M35', 'GATE', 'gate line need not carry as_of',
  "if re.search(r'\\b%s\\b' % rid, x) and cfg['as_of'] in x\n", "if re.search(r'\\b%s\\b' % rid, x)\n"),
 ('M36', 'CAPTURE', 'cap_bad ignored',
  "bool(qual) and not gate_bad and not cap_bad,", "bool(qual) and not gate_bad,"),
 ('M37', 'INDEX/freeze-pin', 'index tool read from lands not freeze',
  "tool = show(root, freeze, c['index_tool'])", "tool = show(root, lands, c['index_tool'])"),
 ('M38', 'INDEX/readme-row', 'README row not required',
  "out.append(leg('INDEX', row_ok and rc == 0,", "out.append(leg('INDEX', rc == 0,"),
 ('M39', 'APPENDONLY', 'tier cell (3) dropped from compared set',
  "for i in (0, 1, 2, 3, 4, 5, 6, 8)] != [lc[i] for i in (0, 1, 2, 3, 4, 5, 6, 8)]", "for i in (0, 1, 2, 4, 5, 6, 8)] != [lc[i] for i in (0, 1, 2, 4, 5, 6, 8)]"),
 ('M40', 'APPENDONLY', 'source cell (1) dropped from compared set',
  "for i in (0, 1, 2, 3, 4, 5, 6, 8)] != [lc[i] for i in (0, 1, 2, 3, 4, 5, 6, 8)]", "for i in (0, 2, 3, 4, 5, 6, 8)] != [lc[i] for i in (0, 2, 3, 4, 5, 6, 8)]"),
 ('M41', 'refusal/lands==base', 'lands==base refusal removed',
  "    if lands == base:\n        raise Refused('lands equals frozen base')\n", ""),
 ('M42', 'refusal/first-parent', 'freeze-on-chain refusal removed',
  "    if freeze not in chain:\n        raise Refused('freeze is not on the lands first-parent chain')\n", ""),
 ('M43', 'refusal/LEGCOUNT', 'LEGCOUNT refusal removed',
  "    if frozen_legs != LEGS[args.claim]:\n        raise Refused", "    if False:\n        raise Refused"),
 ('M44', 'refusal/HEX40', '40-hex syntax gate removed',
  "    if not HEX40.match(rev or ''):\n        raise Refused('not a 40-hex revision: %r' % rev)\n", ""),
 ('M45', 'refusal/first-parent', 'first-parent dropped (any ancestry)',
  "git(root, 'rev-list', '--first-parent', lands, check=True)", "git(root, 'rev-list', lands, check=True)"),
]


def run(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, **kw)
    return p.returncode, p.stdout.decode(errors='replace'), p.stderr.decode(errors='replace')


def detect(md, src_bytes, tag):
    """Run both detectors against lane clone whose worktree holds src_bytes as measure89.py."""
    lane = os.path.join(md, 'lane')
    with open(os.path.join(lane, REL), 'wb') as f:
        f.write(src_bytes)
    h = hashlib.sha256(open(os.path.join(lane, REL), 'rb').read()).hexdigest()
    st = os.path.join(md, 'st-' + tag); cw = os.path.join(md, 'cw-' + tag); out = os.path.join(md, 'out-' + tag)
    for x in (st, cw):
        os.makedirs(x, exist_ok=True)
    rc1, so1, se1 = run([sys.executable, '-B', os.path.join(lane, REL), '--selftest', '--work', st,
                         '--receipt', os.path.join(md, 'selftest-%s.txt' % tag)])
    rc2, so2, se2 = run([sys.executable, '-B', os.path.join(md, 'controls89.py'), '--lane', lane, '--work', cw, '--out', out])
    bad_st = [l for l in so1.splitlines() if l.startswith('BAD ')]
    mism = [l for l in so2.splitlines() if l.startswith('MISMATCH ')]
    return dict(sha=h, selftest_rc=rc1, selftest_tail=so1.strip().splitlines()[-1:] if so1.strip() else [],
                selftest_bad=bad_st, selftest_stderr=se1[-800:], controls_rc=rc2, controls_mismatch=mism,
                controls_txt=so2, controls_stderr=se2[-800:])


def one(m):
    mid, legn, desc, old, new = m
    md = os.path.join(S, 'm', mid)
    shutil.rmtree(md, ignore_errors=True)
    os.makedirs(md)
    src = PRISTINE.decode()
    n = src.count(old)
    if n != 1:
        return dict(id=mid, leg=legn, desc=desc, error='old string occurs %d times' % n)
    mut = src.replace(old, new).encode()
    run(['git', 'clone', '-q', '--shared', LANE, os.path.join(md, 'lane')], check=True)
    top = run(['git', '-C', os.path.join(md, 'lane'), 'rev-parse', '--show-toplevel'])[1].strip()
    assert os.path.realpath(top) == os.path.realpath(os.path.join(md, 'lane')), top
    shutil.copyfile(CONTROLS, os.path.join(md, 'controls89.py'))
    comp = run([sys.executable, '-c', 'import ast,sys;ast.parse(open(sys.argv[1]).read())', '/dev/stdin'], input=mut)
    mutated = detect(md, mut, 'mutant')
    killed_by = []
    if mutated['selftest_rc'] != 0:
        killed_by.append('selftest')
    if mutated['controls_mismatch'] or mutated['controls_rc'] != 0:
        killed_by.append('controls')
    # restore pristine bytes in the clone and verify hash
    with open(os.path.join(md, 'lane', REL), 'wb') as f:
        f.write(PRISTINE)
    restored_sha = hashlib.sha256(open(os.path.join(md, 'lane', REL), 'rb').read()).hexdigest()
    diff = run(['diff', '-u', '--label', 'pristine', '--label', mid, '/dev/fd/3', '/dev/stdin'], input=mut,
               pass_fds=()) if False else None
    return dict(id=mid, leg=legn, desc=desc, old=old, new=new, parse_rc=comp[0],
                pristine_sha=PSHA, mutant_sha=hashlib.sha256(mut).hexdigest(), restored_sha=restored_sha,
                restored_equal=restored_sha == PSHA, killed_by=killed_by,
                verdict='killed' if killed_by else 'survived', mutated=mutated)


if __name__ == '__main__':
    ids = sys.argv[1:]
    todo = [m for m in M if not ids or m[0] in ids]
    with cf.ThreadPoolExecutor(int(os.environ.get('J', '6'))) as ex:
        res = list(ex.map(one, todo))
    json.dump(res, open(os.path.join(S, 'results.json'), 'w'), indent=1)
    for r in res:
        if 'error' in r:
            print(r['id'], 'ERROR', r['error']); continue
        mu = r['mutated']
        print('%s %-24s %-8s by=%-17s st_rc=%d st_bad=%d ctl_rc=%d mism=%s restored=%s' % (
            r['id'], r['leg'], r['verdict'], ','.join(r['killed_by']) or '-', mu['selftest_rc'], len(mu['selftest_bad']),
            mu['controls_rc'], [x.split()[1] for x in mu['controls_mismatch']], r['restored_equal']))
