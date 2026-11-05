#!/usr/bin/env python3
"""Round-95 mutation driver: 88 carried removals plus seven refusal removals.

Axes: operability, faithful mutation semantics, reproducible evidence.
Each tuple is (name, target, replacement, semantics). The 83 round-93-lineage
entries retain replace-all except head-qualify-off, explicitly exactly-once.
The five round-94 routed entries and seven new removals are exactly-once.
Clean tool selftest must pass before any mutation is scored. A stub lacking the
patterns scores zero kills. All generated files and receipts live under --work.
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys

MUTANTS = [
    ('overlap-bound-to-zero', 'elif max(overlap(quote, teaches), overlap(quote, scope), overlap(quote, anchor)) < args.min_overlap:', 'elif max(overlap(quote, teaches), overlap(quote, scope), overlap(quote, anchor)) < 0:', 'replace-all'),
    ('self-quote-check-off', 'elif q and q in norm(teaches):', 'elif False:', 'replace-all'),
    ('source-quote-check-off', 'if q and q in norm(src):', 'if False:', 'replace-all'),
    ('archive-year-off', 'if int(stamp[:4]) < int(as_of[:4]):', 'if False:', 'replace-all'),
    ('archive-embed-off', 'if embedded not in row_urls:', 'if False:', 'replace-all'),
    ('row-url-off', 'if not row_urls:', 'if False:', 'replace-all'),
    ('capture-dir-off', "    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/') + '/')):\n        return f'capture outside {cap_dir}: {rel}'", "    if False:\n        return f'capture outside {cap_dir}: {rel}'", 'replace-all'),
    ('capture-graded-off', "return f'capture is a graded file: {rel}'", 'pass', 'replace-all'),
    ('sha256-off', "if hashlib.sha256(raw).hexdigest() != str(m.get('sha256', '')):", 'if False:', 'replace-all'),
    ('http-status-off', "if not isinstance(m.get('http_status'), int) or not 200 <= m['http_status'] < 300:", 'if False:', 'replace-all'),
    ('quote-in-capture-off', 'if norm(quote) not in text:', 'if False:', 'replace-all'),
    ('manifest-entry-off', "return 'no manifest entry'", 'return None', 'replace-all'),
    ('manifest-empty-off', "return 'manifest capture empty'", 'return None', 'replace-all'),
    ('duplicate-id-off', 'if lands_dup:', 'if False:', 'replace-all'),
    ('duplicate-url-off', 'if len(owners) > 1:', 'if False:', 'replace-all'),
    ('not-located-variant-off', "verdict = 'NOT-LOCATED' if verdict.startswith('NOT') else 'LOCATED'", "verdict = 'LOCATED'", 'replace-all'),
    ('advanced-not-located-off', "if rid in disp and disp[rid][0] == 'NOT-LOCATED':", 'if False:', 'replace-all'),
    ('window-floor-off', 'if not (lo < d <= hi):', 'if not (as_of < d <= hi):', 'replace-all'),
    ('recheck-iso-off', 'd = as_date(new, rid)', 'd = as_of', 'replace-all'),
    ('not-in-base-off', 'if rid not in base:', 'if False:', 'replace-all'),
    ('othercells-off', 'if moved:', 'if False:', 'replace-all'),
    ('cellcount-off', 'if len(b) != len(l):', 'if False:', 'replace-all'),
    ('min-advanced-off', 'len(advanced) >= args.min_advanced', 'len(advanced) >= 0', 'replace-all'),
    ('disposed-off', 'dispo = [rid for rid in ids if rid not in disp]', 'dispo = []', 'replace-all'),
    ('advance-word-bound-off', 'if len(quote.split()) > args.quote_max_words:\n            meaning.append', 'if False:\n            meaning.append', 'replace-all'),
    ('entry-bytes-off', 'if len(entry.encode()) < args.min_bytes:', 'if False:', 'replace-all'),
    ('entry-headings-off', 'if len(heads) < args.min_headings:', 'if False:', 'replace-all'),
    ('entry-header-key-off', 'if key not in entry:', 'if False:', 'replace-all'),
    ('topic-overlap-off', 'if shared < args.min_topic_overlap:', 'if False:', 'replace-all'),
    ('stem-off', 'if stem_words and stem_hit == 0:', 'if False:', 'replace-all'),
    ('repeat-sentence-off', 'if worst > 2:', 'if False:', 'replace-all'),
    ('table-shape-off', 'if rows < args.table_min_rows or cols < args.table_min_cols:', 'if rows < args.table_min_rows:', 'replace-all'),
    ('newids-opened-off', 'if opened != args.as_of:', 'if False:', 'replace-all'),
    ('newids-usedby-off', 'if os.path.basename(args.entry) not in used and args.entry not in used:', 'if False:', 'replace-all'),
    ('newids-missing-cited-off', 'if missing:', 'if False:', 'replace-all'),
    ('newids-tier-off', "if tier not in ('A', 'B'):", 'if False:', 'replace-all'),
    ('newids-min-off', 'if len(qualifying) < args.min_new_ids:', 'if False:', 'replace-all'),
    ('newids-cited-scope-off', 'scoped = [rid for rid in new_ids if rid in cited]', 'scoped = list(new_ids)', 'replace-all'),
    ('gate-url-off', 'if not any(u in line for u in urls(src)):', 'if False:', 'replace-all'),
    ('gate-date-off', 'if args.as_of not in line:', 'if False:', 'replace-all'),
    ('gate-quote-bounds-off', 'if len(quote.split()) > args.quote_max_words or len(norm(quote)) < args.quote_min_chars:', 'if len(quote.split()) > args.quote_max_words:', 'replace-all'),
    ('gate-min-chars-off', 'or len(norm(quote)) < args.quote_min_chars:', 'or False:', 'replace-all'),
    ('required-arg-off', 'if not getattr(args, req):', 'if False:', 'replace-all'),
    ('phrase-parse-off', "phrases = [p.strip() for p in re.split(r'[;]', args.topic_phrases or '') if p.strip()]", 'phrases = []', 'replace-all'),
    ('phrase-anchor-text-off', "anchor_text = norm(' '.join(hit_heads)) + ' ' + norm('\\n'.join(hit_rows))", "anchor_text = norm(entry) + ' ' + norm('\\n'.join(hit_rows))", 'replace-all'),
    ('uniq-shadow-off', 'if norm_url(u) in base_urls:', 'if False:', 'replace-all'),
    ('phrase-floor-off', 'if len(hits) < phrase_floor:', 'if False:', 'replace-all'),
    ('gate-selfquote-entry-off', "elif q and q in norm(teaches):\n            gate.append(f'{rid}: gate quote is the row teaching cell (self-quote)')", "elif False:\n            gate.append(f'{rid}: gate quote is the row teaching cell (self-quote)')", 'replace-all'),
    ('gate-chrome-entry-off', "if q and q in norm(src):\n            gate.append(f'{rid}: gate quote is copied from the row source cell (title or chrome), not located prose')", "if False:\n            gate.append(f'{rid}: gate quote is copied from the row source cell (title or chrome), not located prose')", 'replace-all'),
    ('graded-shas-off', 'if graded_shas:\n        hit = graded_shas.get(hashlib.sha256(raw).hexdigest())', 'if False:\n        hit = None', 'replace-all'),
    ('appendonly-lesson-off', "if getattr(args, 'base_lesson', None):", 'if False:', 'replace-all'),
    ('appendonly-gained-off', "if rid not in base_disp:\n                moved.append(f'{rid}: gained", "if False:\n                moved.append(f'{rid}: gained", 'replace-all'),
    ('appendonly-flip-off', 'elif base_disp[rid][0] != verdict:', 'elif False:', 'replace-all'),
    ('dispo-anchor-revert', "DISPO_RE = re.compile(r'^(?:[>\\-\\*+\\s]*\\s)?S(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b', re.I)", "DISPO_RE = re.compile(r'^[-*] ?S(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b', re.I)", 'replace-all'),
    ('shadow-norm-off', "u = str(u).strip().split('#', 1)[0]", 'u = str(u).strip()', 'replace-all'),
    ('capture-url-bind-off', "err = surface_error((man_entry or {}).get('url', ''), src, args.as_of)", 'err = None', 'replace-all'),
    ('capture-shared-off', "if len(owners) > 1:\n            capture.append('capture shared by ", "if False:\n            capture.append('capture shared by ", 'replace-all'),
    ('gate-topic-bind-off', 'if bound < args.min_gate_overlap:', 'if False:', 'replace-all'),
    ('anchor-span-off', 'if span < min_span:', 'if False:', 'replace-all'),
    ('topic-prose-off', 'shared = overlap(body_text, args.topic)', 'shared = overlap(entry, args.topic)', 'replace-all'),
    ('gap-entry-graded-off', '[args.lesson, args.lands_registry, args.entry,', '[args.lesson, args.lands_registry,', 'replace-all'),
    ('gap-lands-graded-off', '[args.lesson, args.lands_registry, args.entry,', '[args.lesson, args.entry,', 'replace-all'),
    ('gap-lesson-graded-off', '[args.lesson, args.lands_registry, args.entry,', '[args.lands_registry, args.entry,', 'replace-all'),
    ('gap-traversal-off', "if rel.startswith('/') or '..' in rel.split('/'):", "if rel.startswith('/'):", 'replace-all'),
    ('gap-fetch-offset-optional', "(?:Z|[+-]\\d{2}:\\d{2})$')", "(?:Z|[+-]\\d{2}:\\d{2})?$')", 'replace-all'),
    ('gap-fetch-date-off', "if fm.group(1) != as_of:\n        return f'fetched_at date", "if False:\n        return f'fetched_at date", 'replace-all'),
    ('gap-cap-slash-capture-error-off', "rel.startswith(cap_dir.rstrip('/') + '/')):", "rel.startswith(cap_dir.rstrip('/'))):", 'replace-all'),
    ('gap-port-strip-off', "if (scheme == 'http' and host.endswith(':80')) or (scheme == 'https' and host.endswith(':443')):", 'if False:', 'replace-all'),
    ('norm-fold-scheme-off', "    if scheme in ('http', 'https'):\n        scheme = 'https'", "    if False:\n        scheme = 'https'", 'replace-all'),
    ('norm-www-off', "    if host.startswith('www.'):\n        host = host[4:]", '    if False:\n        host = host[4:]', 'replace-all'),
    ('norm-query-off', "    rest = rest.split('?', 1)[0]", '    rest = rest', 'replace-all'),
    ('norm-pathfold-off', '    rest = rest.lower()', '    rest = rest', 'replace-all'),
    ('capture-symlink-off', "    if os.path.islink(path):\n        return f'capture is a symlink: {rel}'", "    if False:\n        return f'capture is a symlink: {rel}'", 'replace-all'),
    ('capture-textcopy-off', '    if graded_norms:\n        hitn = graded_norms.get(ntext)', '    if False:\n        hitn = None', 'replace-all'),
    ('capture-htmlextract-off', '    text = norm(html_body_text(raw))', "    text = norm(raw.decode('utf-8', errors='replace'))", 'replace-all'),
    ('dispo-fallback-off', '        m = DISPO_ANY_RE.search(plain)', '        m = None', 'replace-all'),
    ('dispo-zwstrip-off', '        stripped = line.strip().translate(ZW_MAP)', '        stripped = line.strip()', 'replace-all'),
    ('baserows-cellcmp-off', '        for i in (0, 1, 2, 3, 4, 5, 6, 8):', '        for i in ():', 'replace-all'),
    ('baserows-delete-off', "        if not lrows:\n            baserow.append(f'{rid}: base row removed from the lands registry')", "        if False:\n            baserow.append(f'{rid}: base row removed from the lands registry')", 'replace-all'),
    ('baserows-leg-off', "    legs.append(('BASEROWS', not baserow,", "    legs.append(('BASEROWS', True,", 'replace-all'),
    ('manifest-shape-off', "    if not isinstance(man_rows, dict):\n        raise Refused('manifest rows is not a JSON object (list where mapping expected)')", "    if False:\n        raise Refused('manifest rows is not a JSON object (list where mapping expected)')", 'replace-all'),
    ('manifest-object-off', "    if not isinstance(man, dict):\n        raise Refused('manifest is not a JSON object')", "    if False:\n        raise Refused('manifest is not a JSON object')", 'replace-all'),
    ('head-qualify-off', "            return len(h.lstrip('#').split()) >= 2", '            return True', 'exactly-once'),
    ('script-strip-off', "s = re.sub(r'(?is)<(script|style)\\b[^>]*>.*?</\\1\\s*>', ' ', s)", 'pass', 'exactly-once'),
    ('comment-strip-off', "s = re.sub(r'(?s)<!--.*?-->', ' ', s)", 'pass', 'exactly-once'),
    ('unescape-off', 'return _html.unescape(s)', 'return s', 'exactly-once'),
    ('dispo-any-casei', "DISPO_ANY_RE = re.compile(r'\\bS(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b')", "DISPO_ANY_RE = re.compile(r'\\bS(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b', re.I)", 'exactly-once'),
    ('baserows-drop-cell8', 'for i in (0, 1, 2, 3, 4, 5, 6, 8):', 'for i in (0, 1, 2, 3, 4, 5, 6):', 'exactly-once'),
    ('combining-refuse-off', "    if _dispo_match(nfkd_nomark.replace('|', ' ').replace('*', ' ').replace('_', ' ')) and not m:", '    if False:', 'exactly-once'),
    ('lrm-refuse-off', '    if _dispo_match(nocf.strip().translate(ZW_MAP).translate(DASH_MAP)) and not m and nocf != stripped:', '    if False:', 'exactly-once'),
    ('tab-refuse-off', "    if '\\t' in stripped and re.search(r'LO\\s+CATED|NOT\\s+LOCATED', stripped, re.I):", '    if False:', 'exactly-once'),
    ('id-lookalike-refuse-off', "            if has_nonascii_letter and re.match(r'^[Ss]\\d{3,}$', folded):", '            if False:', 'exactly-once'),
    ('num1-anchor-off', '\\d+\\.\\d+[.)]?|', '', 'exactly-once'),
    ('rm1-anchor-off', '|[IVXLCDM]+[.)]?|[ivxlcdm]+[.)]?', '', 'exactly-once'),
    ('num2-anchor-off', '            if len(raw) >= 3 and isnum(raw[1]):', '            if False:', 'exactly-once'),
]

NAMES = [m[0] for m in MUTANTS]


def run(tool, work, tag):
    d = os.path.join(work, 'st-' + tag)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    p = subprocess.run([sys.executable, '-B', tool, '--selftest', '--work', d],
                       capture_output=True, text=True)
    out = p.stdout or ''
    return p.returncode, bool(re.search(r'^SELFTEST PASS \d+/\d+$', out, re.M)), out + p.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tool', required=True)
    ap.add_argument('--work', required=True, help='existing scratch directory')
    ap.add_argument('--only', default='', help='comma-separated mutant names')
    args = ap.parse_args()
    if not os.path.isdir(args.work):
        print('MUTANTS95_ERROR: --work must be an existing directory', file=sys.stderr)
        return 2
    if not os.path.isfile(args.tool):
        print('MUTANTS95_ERROR: --tool must be a file', file=sys.stderr)
        return 2
    wanted = [n.strip() for n in args.only.split(',') if n.strip()]
    unknown = [n for n in wanted if n not in NAMES]
    if unknown:
        print('MUTANTS95_ERROR: unknown mutant name(s): ' + ', '.join(unknown), file=sys.stderr)
        return 2
    selected = [m for m in MUTANTS if not wanted or m[0] in wanted]
    with open(args.tool, encoding='utf-8') as f:
        src = f.read()
    rows = ['TOOL sha256=' + hashlib.sha256(src.encode()).hexdigest()]
    # Count all patterns at run start, before executing any mutated tool.
    counts = {name: src.count(old) for name, old, new, semantics in selected}
    clean = os.path.join(args.work, 'clean-tool.py')
    with open(clean, 'w', encoding='utf-8') as f:
        f.write(src)
    rc, passed, out = run(clean, args.work, 'clean')
    with open(os.path.join(args.work, 'clean-selftest.txt'), 'w', encoding='utf-8') as f:
        f.write(out)
    rows.append(f'CLEAN-FIRST selftest_rc={rc} SELFTEST-PASS-line={passed}')
    killed = survived = broken = 0
    if rc != 0 or not passed:
        survived = len(selected)
        rows.append('CLEAN-FIRST REFUSED: no mutant executed')
    else:
        for name, old, new, semantics in selected:
            count = counts[name]
            if count == 0 or (semantics == 'exactly-once' and count != 1):
                broken += 1
                rows.append(f' {name} BROKEN-PATTERN matches={count} semantics={semantics} selftest_rc=n/a')
                continue
            path = os.path.join(args.work, 'mut-' + name + '.py')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(src.replace(old, new))
            rc, passed, out = run(path, args.work, name)
            with open(os.path.join(args.work, 'selftest-' + name + '.txt'), 'w', encoding='utf-8') as f:
                f.write(out)
            status = 'KILLED' if rc != 0 or not passed else 'SURVIVED'
            killed += status == 'KILLED'
            survived += status == 'SURVIVED'
            rows.append(f' {name} {status} matches={count} semantics={semantics} selftest_rc={rc} SELFTEST-PASS-line={passed}')
    rows.append(f'MUTATION-SCORE: {killed}/{len(selected)} killed, {survived} survived, {broken} broken-pattern')
    receipt = '\n'.join(rows) + '\n'
    print(receipt, end='')
    with open(os.path.join(args.work, 'mutation95-score.txt'), 'w', encoding='utf-8') as f:
        f.write(receipt)
    return 0 if killed == len(selected) and not survived and not broken else 1


if __name__ == '__main__':
    sys.exit(main())
