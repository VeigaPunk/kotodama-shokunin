#!/usr/bin/env python3
"""Independent round-90 mutation pass #2 over tools/check-advance-evidence.py.

New single-point mutants of the entry-mode legs the committed 43 do not cover
(SHAPE repetition threshold, TOPIC counter, NEWIDS qualifier cells, GATE
url/date/word bounds, CAPTURE confinement/sha256, 0-3 space registry indents,
duplicate handling). Never edits the source under test: each mutant is a fresh
file in --work, the pristine bytes are hashed before and after.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys

MUTANTS = [
    # --- SHAPE ---------------------------------------------------------
    ('shape-repeat-threshold-3',
     '    if worst > 2:',
     '    if worst > 3:'),
    ('shape-table-row-off-by-one',
     '    if rows < args.table_min_rows or cols < args.table_min_cols:',
     '    if rows < args.table_min_rows - 1 or cols < args.table_min_cols:'),
    # --- TOPIC ---------------------------------------------------------
    ('topic-floor-off-by-one',
     '    if shared < args.min_topic_overlap:',
     '    if shared < args.min_topic_overlap - 1:'),
    ('topic-counts-topic-line-only',
     '    shared = overlap(entry, args.topic)',
     '    shared = overlap(topic_line, args.topic)'),
    # --- NEWIDS qualifier cells ---------------------------------------
    ('newids-status-off',
     "        if status != 'mined':",
     '        if False:'),
    ('newids-basesubtract-off',
     '    new_ids = sorted((lands_ids - base_ids))',
     '    new_ids = sorted(lands_ids)'),
    ('newids-usedby-index-drift',
     '        tier, status, opened, used = cells[3], cells[7], cells[8], cells[10]',
     '        tier, status, opened, used = cells[3], cells[7], cells[8], cells[9]'),
    ('newids-tier-accepts-c',
     "        if tier not in ('A', 'B'):",
     "        if tier not in ('A', 'B', 'C'):"),
    # --- GATE url / date / word bounds --------------------------------
    ('gate-word-bound-plus-12',
     '        if len(quote.split()) > args.quote_max_words or len(norm(quote)) < args.quote_min_chars:',
     '        if len(quote.split()) > args.quote_max_words + 12 or len(norm(quote)) < args.quote_min_chars:'),
    ('gate-char-floor-minus-6',
     '        if len(quote.split()) > args.quote_max_words or len(norm(quote)) < args.quote_min_chars:',
     '        if len(quote.split()) > args.quote_max_words or len(norm(quote)) < args.quote_min_chars - 6:'),
    ('gate-quote-selection-last',
     "            gate.append(f'{rid}: no lesson line with id and quote')\n            continue\n        line, quote = qs[0]",
     "            gate.append(f'{rid}: no lesson line with id and quote')\n            continue\n        line, quote = qs[-1]"),
    ('gate-url-slash-relaxed',
     '        if not any(u in line for u in urls(src)):',
     "        if not any(u.rstrip('/') in line for u in urls(src)):"),
    # --- CAPTURE confinement and sha256 -------------------------------
    ('capture-prefix-boundary-off',
     "    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/') + '/')):\n        return f'capture outside {cap_dir}: {rel}'",
     "    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/'))):\n        return f'capture outside {cap_dir}: {rel}'"),
    ('capture-traversal-guard-off',
     "    if rel.startswith('/') or '..' in rel.split('/'):\n        return f'capture path not relative and confined: {rel}'",
     "    if False:\n        return f'capture path not relative and confined: {rel}'"),
    ('capture-sha256-skip-absent',
     "    if hashlib.sha256(raw).hexdigest() != str(m.get('sha256', '')):",
     "    if m.get('sha256') and hashlib.sha256(raw).hexdigest() != str(m.get('sha256', '')):"),
    ('capture-http-status-widen',
     "    if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:",
     "    if not isinstance(m.get('http_status'), int) or not 100 <= m['http_status'] < 400:"),
    ('capture-fetched-date-off',
     '    if fm.group(1) != as_of:',
     '    if False:'),
    # --- registry parsing under 0-3 leading spaces ---------------------
    ('row-indent-unbounded',
     "ROW_RE = re.compile(r'^ {0,3}\\|[ ]*(S\\d{3,})[ ]*\\|')",
     "ROW_RE = re.compile(r'^ *\\|[ ]*(S\\d{3,})[ ]*\\|')"),
    ('row-indent-zero-only',
     "ROW_RE = re.compile(r'^ {0,3}\\|[ ]*(S\\d{3,})[ ]*\\|')",
     "ROW_RE = re.compile(r'^\\|[ ]*(S\\d{3,})[ ]*\\|')"),
    # --- duplicate handling -------------------------------------------
    ('advanced-dup-length-lenient',
     '        if len(lands.get(rid, [])) != 1:',
     '        if len(lands.get(rid, [])) < 1:'),
    ('shadow-url-threshold-3',
     '        if len(owners) > 1:',
     '        if len(owners) > 2:'),
]


def run(path, work, tag):
    d = os.path.join(work, 'st-' + tag)
    os.makedirs(d, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', path, '--selftest', '--work', d],
                       capture_output=True, text=True)
    head = (r.stdout or '').strip().splitlines()[:1]
    bad = [l.strip() for l in (r.stdout or '').splitlines() if l.strip().startswith('BAD')]
    return r.returncode, (head[0] if head else ''), bad[:3]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tool', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    src = os.path.abspath(args.tool)
    raw = open(src, 'rb').read()
    before = hashlib.sha256(raw).hexdigest()
    text0 = raw.decode()
    clean = os.path.join(args.work, 'clean.py')
    open(clean, 'wb').write(raw)
    rc, clean_head, bad = run(clean, args.work, 'clean')
    rows = []
    if rc != 0:
        print('MUTATION2: FAIL clean tool is not green: ' + clean_head, file=sys.stderr)
        return 1
    for name, old, new in MUTANTS:
        n = text0.count(old)
        if n != 1:
            rows.append(dict(mutant=name, status='BROKEN-PATTERN',
                             detail=f'pattern count {n}'))
            continue
        path = os.path.join(args.work, 'm-' + name + '.py')
        open(path, 'w').write(text0.replace(old, new))
        rc, head, bad = run(path, args.work, name)
        rows.append(dict(mutant=name,
                         status='KILLED' if rc != 0 else 'SURVIVED',
                         sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(),
                         detail=head, bad=bad))
        os.unlink(path)
    after = hashlib.sha256(open(src, 'rb').read()).hexdigest()
    killed = sum(1 for r in rows if r['status'] == 'KILLED')
    broken = [r['mutant'] for r in rows if r['status'] == 'BROKEN-PATTERN']
    survived = [r['mutant'] for r in rows if r['status'] == 'SURVIVED']
    lines = [f'MUTATION-SCORE: {killed}/{len(rows)} killed, {len(survived)} survived, '
             f'{len(broken)} broken-pattern',
             f'tool sha256 {before}',
             f'tool sha256 restored {after} (unchanged={before == after})',
             f'clean selftest green: rc=0 {clean_head}']
    for r in rows:
        extra = '' if not r.get('bad') else ' first_bad=' + r['bad'][0]
        lines.append(f'  {r["status"]:14s} {r["mutant"]} {r.get("detail", "")}'.rstrip() + extra)
    out = '\n'.join(lines)
    print(out)
    open(args.out + '.txt', 'w').write(out + '\n')
    json.dump(dict(tool_sha256=before, restored_sha256=after, total=len(rows), killed=killed,
                   survived=survived, broken=broken, rows=rows), open(args.out + '.json', 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
