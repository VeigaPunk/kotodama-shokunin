#!/usr/bin/env python3
"""Deterministic mutation pass over tools/check-advance-evidence.py (round 90).

Each mutant is one textual hardening removal. A mutant is KILLED when the
tool's own --selftest exits non-zero on it; the clean bytes must be green
first. Receipt: reports/round-90/mutation-score.txt (+ .json). No network,
no lane write: the mutants live in --work.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

TOOL = 'tools/check-advance-evidence.py'

MUTANTS = [
    ('overlap-bound-to-zero', 'elif max(overlap(quote, teaches), overlap(quote, scope), overlap(quote, anchor)) < args.min_overlap:', 'elif max(overlap(quote, teaches), overlap(quote, scope), overlap(quote, anchor)) < 0:'),
    ('self-quote-check-off', 'elif q and q in norm(teaches):', 'elif False:'),
    ('source-quote-check-off', 'if q and q in norm(src):', 'if False:'),
    ('archive-year-off', 'if int(stamp[:4]) < int(as_of[:4]):', 'if False:'),
    ('archive-embed-off', 'if embedded not in row_urls:', 'if False:'),
    ('row-url-off', 'if not row_urls:', 'if False:'),
    ('capture-dir-off', "    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/') + '/')):\n        return f'capture outside {cap_dir}: {rel}'", "    if False:\n        return f'capture outside {cap_dir}: {rel}'"),
    ('capture-graded-off', "return f'capture is a graded file: {rel}'", 'pass'),
    ('sha256-off', "if hashlib.sha256(raw).hexdigest() != str(m.get('sha256', '')):", 'if False:'),
    ('http-status-off', "if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:", 'if False:'),
    ('quote-in-capture-off', 'if norm(quote) not in text:', 'if False:'),
    ('manifest-entry-off', "return 'no manifest entry'", 'return None'),
    ('manifest-empty-off', "return 'manifest capture empty'", 'return None'),
    ('duplicate-id-off', 'if lands_dup:', 'if False:'),
    ('duplicate-url-off', 'if len(owners) > 1:', 'if False:'),
    ('not-located-variant-off', "verdict = 'NOT-LOCATED' if verdict.startswith('NOT') else 'LOCATED'", "verdict = 'LOCATED'"),
    ('advanced-not-located-off', "if rid in disp and disp[rid][0] == 'NOT-LOCATED':", 'if False:'),
    ('window-floor-off', 'if not (lo < d <= hi):', 'if not (as_of < d <= hi):'),
    ('recheck-iso-off', 'd = as_date(new, rid)', 'd = as_of'),
    ('not-in-base-off', 'if rid not in base:', 'if False:'),
    ('othercells-off', 'if moved:', 'if False:'),
    ('cellcount-off', 'if len(b) != len(l):', 'if False:'),
    ('min-advanced-off', 'len(advanced) >= args.min_advanced', 'len(advanced) >= 0'),
    ('disposed-off', 'dispo = [rid for rid in ids if rid not in disp]', 'dispo = []'),
    ('advance-word-bound-off', 'if len(quote.split()) > args.quote_max_words:\n            meaning.append', 'if False:\n            meaning.append'),
    ('entry-bytes-off', 'if len(entry.encode()) < args.min_bytes:', 'if False:'),
    ('entry-headings-off', 'if len(heads) < args.min_headings:', 'if False:'),
    ('entry-header-key-off', "if key not in entry:", 'if False:'),
    ('topic-overlap-off', 'if shared < args.min_topic_overlap:', 'if False:'),
    ('stem-off', 'if stem_words and stem_hit == 0:', 'if False:'),
    ('repeat-sentence-off', 'if worst > 2:', 'if False:'),
    ('table-shape-off', 'if rows < args.table_min_rows or cols < args.table_min_cols:', 'if rows < args.table_min_rows:'),
    ('newids-opened-off', 'if opened != args.as_of:', 'if False:'),
    ('newids-usedby-off', "if os.path.basename(args.entry) not in used and args.entry not in used:", 'if False:'),
    ('newids-missing-cited-off', 'if missing:', 'if False:'),
    ('newids-tier-off', "if tier not in ('A', 'B'):", 'if False:'),
    ('newids-min-off', 'if len(qualifying) < args.min_new_ids:', 'if False:'),
    ('newids-cited-scope-off', 'scoped = [rid for rid in new_ids if rid in cited]', 'scoped = list(new_ids)'),
    ('gate-url-off', 'if not any(u in line for u in urls(src)):', 'if False:'),
    ('gate-date-off', 'if args.as_of not in line:', 'if False:'),
    ('gate-quote-bounds-off', 'if len(quote.split()) > args.quote_max_words or len(norm(quote)) < args.quote_min_chars:', 'if len(quote.split()) > args.quote_max_words:'),
    ('gate-min-chars-off', 'or len(norm(quote)) < args.quote_min_chars:', 'or False:'),
    ('required-arg-off', 'if not getattr(args, req):', 'if False:'),
]


def run(tool, work, tag):
    d = os.path.join(work, 'st-' + tag)
    os.makedirs(d, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', tool, '--selftest', '--work', d],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout or '').strip().splitlines()[:1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--work', required=True)
    ap.add_argument('--out', default='reports/round-90/mutation-score')
    args = ap.parse_args()
    if not os.path.isdir(args.work):
        print('MUTATION: FAIL --work must be an existing directory', file=sys.stderr)
        return 2
    src = os.path.join(args.root, TOOL)
    raw = open(src, 'rb').read()
    clean = os.path.join(args.work, 'clean.py')
    open(clean, 'wb').write(raw)
    rc, clean_head = run(clean, args.work, 'clean')
    rows = []
    if rc != 0:
        print('MUTATION: FAIL clean tool is not green: ' + ' '.join(clean_head), file=sys.stderr)
        return 1
    for name, old, new in MUTANTS:
        text = raw.decode()
        if text.count(old) != 1:
            rows.append(dict(mutant=name, status='BROKEN-PATTERN', detail=f'pattern count {text.count(old)}'))
            continue
        path = os.path.join(args.work, 'm-' + name + '.py')
        open(path, 'w').write(text.replace(old, new))
        rc, head = run(path, args.work, name)
        rows.append(dict(mutant=name, status='KILLED' if rc != 0 else 'SURVIVED',
                         sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(),
                         detail=(head[0] if head else '')))
        os.unlink(path)
    killed = sum(1 for r in rows if r['status'] == 'KILLED')
    broken = [r['mutant'] for r in rows if r['status'] == 'BROKEN-PATTERN']
    lines = [f'MUTATION-SCORE: {killed}/{len(rows)} killed, {len(rows) - killed - len(broken)} survived, '
             f'{len(broken)} broken-pattern',
             f'tool sha256 {hashlib.sha256(raw).hexdigest()}',
             f'clean selftest green: rc=0 {clean_head[0] if clean_head else ""}']
    for r in rows:
        lines.append(f'  {r["status"]:14s} {r["mutant"]} {r.get("detail", "")}'.rstrip())
    out = '\n'.join(lines)
    print(out)
    os.makedirs(os.path.join(args.root, os.path.dirname(args.out)), exist_ok=True)
    open(os.path.join(args.root, args.out + '.txt'), 'w').write(out + '\n')
    json.dump(dict(tool_sha256=hashlib.sha256(raw).hexdigest(), total=len(rows), killed=killed,
                   rows=rows), open(os.path.join(args.root, args.out + '.json'), 'w'), indent=1)
    return 0 if killed >= 28 and not broken else 1


if __name__ == '__main__':
    sys.exit(main())
