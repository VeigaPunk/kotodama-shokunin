#!/usr/bin/env python3
"""Deterministic mutation pass over tools/check-advance-evidence.py (round 93).

Successor to reports/round-92/mutants.py (60 pairs; every pair whose target
string survives the v4 edit is carried unchanged, and the one pair whose target
line the v4 edit renamed — phrase-anchor-text-off — carries the renamed target).
Adds, over the round-92 gap hunt (.ufo/waves/round-92/w1/MutationTesterV3.md,
8 of the 9 selftest-level survivors; gap-manifest-graded-off is structurally
unpinnable — a capture cannot byte- or text-copy the graded manifest because the
manifest bytes embed the capture's own sha, a fixed-point no copy can satisfy —
documented in corpus/lessons/round-93.md) and over every round-93 v4 hardening:

  URL comparison folds (scheme, www., query, path case)      A2c-A2f
  capture symlink refusal; normalized text-copy refusal       A6c/A6d, A3b
  capture body-text extraction (HTML markup stripped)         A6e
  disposition scanner: zero-width strip, unanchored fallback  A5d/A5e/A5f
  BASEROWS leg: identity-cell compare, removal detect, leg    A6a/A6b
  manifest shape refusals (object, rows mapping)              A6g
  TOPIC anchor surface rule (heading token floor)             A4a

Each mutant is one textual hardening removal applied to a copy of the tool under
--work; the mutant is KILLED when the mutated tool's own --selftest exits
non-zero; the clean bytes must be green first, and the receipt header carries
the clean run's own rc and first line.

A missing or nonexistent --work is refused with a named diagnostic, rc 2
(routed round-92 R92-M3 / spot-check §6 item 4: the round-92 mutants.py crashed
with FileNotFoundError on a nonexistent --work).

--tool <path> mutates that file instead of <root>/tools/check-advance-evidence.py
(the stub control: a printer that cannot apply the pairs scores 0 killed).

Receipt: reports/round-93/mutation-score.txt (+ .json). No network, no lane
write; the mutants live under --work.
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
    # ---------------- round-91 v2 pairs (entry mode) ----------------
    ('phrase-parse-off', 'phrases = [p.strip() for p in re.split(r\'[;]\', args.topic_phrases or \'\') if p.strip()]', 'phrases = []'),
    ('phrase-anchor-text-off', "anchor_text = norm(' '.join(hit_heads)) + ' ' + norm('\\n'.join(hit_rows))", "anchor_text = norm(entry) + ' ' + norm('\\n'.join(hit_rows))"),
    ('uniq-shadow-off', 'if norm_url(u) in base_urls:', 'if False:'),
    ('phrase-floor-off', 'if len(hits) < phrase_floor:', 'if False:'),
    ('gate-selfquote-entry-off', "elif q and q in norm(teaches):\n            gate.append(f'{rid}: gate quote is the row teaching cell (self-quote)')", "elif False:\n            gate.append(f'{rid}: gate quote is the row teaching cell (self-quote)')"),
    ('gate-chrome-entry-off', "if q and q in norm(src):\n            gate.append(f'{rid}: gate quote is copied from the row source cell (title or chrome), not located prose')", "if False:\n            gate.append(f'{rid}: gate quote is copied from the row source cell (title or chrome), not located prose')"),
    ('graded-shas-off', 'if graded_shas:\n        hit = graded_shas.get(hashlib.sha256(raw).hexdigest())', 'if False:\n        hit = None'),
    ('appendonly-lesson-off', "if getattr(args, 'base_lesson', None):", 'if False:'),
    ('appendonly-gained-off', "if rid not in base_disp:\n                moved.append(f'{rid}: gained", "if False:\n                moved.append(f'{rid}: gained"),
    ('appendonly-flip-off', 'elif base_disp[rid][0] != verdict:', 'elif False:'),
    # ---------------- round-92 v3 pairs (routed round-91 survivors) ----------------
    ('dispo-anchor-revert', "DISPO_RE = re.compile(r'^(?:[>\\-\\*+\\s]*\\s)?S(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b', re.I)", "DISPO_RE = re.compile(r'^[-*] ?S(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b', re.I)"),
    ('shadow-norm-off', "u = str(u).strip().split('#', 1)[0]", "u = str(u).strip()"),
    ('capture-url-bind-off', "err = surface_error((man_entry or {}).get('url', ''), src, args.as_of)", "err = None"),
    ('capture-shared-off', "if len(owners) > 1:\n            capture.append('capture shared by ", "if False:\n            capture.append('capture shared by "),
    ('gate-topic-bind-off', 'if bound < args.min_gate_overlap:', 'if False:'),
    ('anchor-span-off', 'if span < min_span:', 'if False:'),
    ('topic-prose-off', 'shared = overlap(body_text, args.topic)', 'shared = overlap(entry, args.topic)'),
    # -------- round-93 v4 pairs: round-92 gap-hunt arms (red-before receipts) --------
    ('gap-entry-graded-off', '[args.lesson, args.lands_registry, args.entry,', '[args.lesson, args.lands_registry,'),
    ('gap-lands-graded-off', '[args.lesson, args.lands_registry, args.entry,', '[args.lesson, args.entry,'),
    ('gap-lesson-graded-off', '[args.lesson, args.lands_registry, args.entry,', '[args.lands_registry, args.entry,'),
    ('gap-traversal-off', "if rel.startswith('/') or '..' in rel.split('/'):", "if rel.startswith('/'):"),
    ('gap-fetch-offset-optional', "(?:Z|[+-]\\d{2}:\\d{2})$')", "(?:Z|[+-]\\d{2}:\\d{2})?$')"),
    ('gap-fetch-date-off', "if fm.group(1) != as_of:\n        return f'fetched_at date", "if False:\n        return f'fetched_at date"),
    ('gap-cap-slash-capture-error-off', "rel.startswith(cap_dir.rstrip('/') + '/')):", "rel.startswith(cap_dir.rstrip('/'))):"),
    ('gap-port-strip-off', "if (scheme == 'http' and host.endswith(':80')) or (scheme == 'https' and host.endswith(':443')):", "if False:"),
    # ---------------- round-93 v4 pairs (routed round-92 survivors) ----------------
    ('norm-fold-scheme-off', "    if scheme in ('http', 'https'):\n        scheme = 'https'", "    if False:\n        scheme = 'https'"),
    ('norm-www-off', "    if host.startswith('www.'):\n        host = host[4:]", "    if False:\n        host = host[4:]"),
    ('norm-query-off', "    rest = rest.split('?', 1)[0]", "    rest = rest"),
    ('norm-pathfold-off', "    rest = rest.lower()", "    rest = rest"),
    ('capture-symlink-off', "    if os.path.islink(path):\n        return f'capture is a symlink: {rel}'", "    if False:\n        return f'capture is a symlink: {rel}'"),
    ('capture-textcopy-off', "    if graded_norms:\n        hitn = graded_norms.get(ntext)", "    if False:\n        hitn = None"),
    ('capture-htmlextract-off', "    text = norm(html_body_text(raw))", "    text = norm(raw.decode('utf-8', errors='replace'))"),
    ('dispo-fallback-off', '            m = DISPO_ANY_RE.search(plain)', '            m = None'),
    ('dispo-zwstrip-off', '        stripped = line.strip().translate(ZW_MAP)', '        stripped = line.strip()'),
    ('baserows-cellcmp-off', '        for i in (0, 1, 2, 3, 4, 5, 6, 8):', '        for i in ():'),
    ('baserows-delete-off', "        if not lrows:\n            baserow.append(f'{rid}: base row removed from the lands registry')", "        if False:\n            baserow.append(f'{rid}: base row removed from the lands registry')"),
    ('baserows-leg-off', "    legs.append(('BASEROWS', not baserow,", "    legs.append(('BASEROWS', True,"),
    ('manifest-shape-off', "    if not isinstance(man_rows, dict):\n        raise Refused('manifest rows is not a JSON object (list where mapping expected)')", "    if False:\n        raise Refused('manifest rows is not a JSON object (list where mapping expected)')"),
    ('manifest-object-off', "    if not isinstance(man, dict):\n        raise Refused('manifest is not a JSON object')", "    if False:\n        raise Refused('manifest is not a JSON object')"),
    ('head-qualify-off', "            return len(h.lstrip('#').split()) >= 2", "            return True"),
]


def run(tool, work, tag):
    d = os.path.join(work, 'st-' + tag)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', tool, '--selftest', '--work', d],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout or '').strip().splitlines()[:1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--work', required=True)
    ap.add_argument('--out', default='reports/round-93/mutation-score')
    ap.add_argument('--tool', default=None, help='mutate this file instead of <root>/' + TOOL)
    args = ap.parse_args()
    if not os.path.isdir(args.work):
        print('MUTANTS93_ERROR: --work must be an existing directory', file=sys.stderr)
        return 2

    src_path = args.tool or os.path.join(args.root, TOOL)
    with open(src_path, 'rb') as f:
        src = f.read().decode('utf-8')
    src_sha = hashlib.sha256(src.encode('utf-8')).hexdigest()
    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True) if os.path.dirname(args.out) else None

    clean_tool = os.path.join(args.work, 'clean-tool.py')
    with open(clean_tool, 'w') as f:
        f.write(src)
    clean_rc, clean_head = run(clean_tool, args.work, 'clean')
    if clean_rc != 0:
        line = f'MUTATION-SCORE: 0/{len(MUTANTS)} killed, {len(MUTANTS)} survived, 0 broken-pattern (clean tool not green first: rc={clean_rc})'
        print(line)
        with open(args.out + '.txt', 'w') as f:
            f.write(f'# clean sha256 {src_sha}\n# clean selftest rc={clean_rc} {clean_head}\n' + line + '\n')
        return 1

    killed, survived, broken, rows = 0, 0, 0, []
    for name, old, new in MUTANTS:
        if old not in src:
            broken += 1
            rows.append(f'  BROKEN-PATTERN {name}: target string absent from the tool bytes')
            continue
        mut_path = os.path.join(args.work, 'mut-' + name + '.py')
        with open(mut_path, 'w') as f:
            f.write(src.replace(old, new))
        if src.replace(old, new) == src:
            broken += 1
            rows.append(f'  BROKEN-PATTERN {name}: replacement produced no change')
            continue
        rc, head = run(mut_path, args.work, name)
        if rc != 0:
            killed += 1
            rows.append(f'  KILLED {name}: selftest rc={rc}')
        else:
            survived += 1
            rows.append(f'  SURVIVED {name}: selftest rc=0')
    total = len(MUTANTS)
    line = f'MUTATION-SCORE: {killed}/{total} killed, {survived} survived, {broken} broken-pattern'
    print(line)
    print('\n'.join(rows))
    with open(args.out + '.txt', 'w') as f:
        f.write(f'# tool sha256 {src_sha}\n# clean selftest rc={clean_rc} {clean_head}\n' + line + '\n' + '\n'.join(rows) + '\n')
    with open(args.out + '.json', 'w') as f:
        json.dump({'tool_sha256': src_sha, 'clean_rc': clean_rc, 'killed': killed, 'total': total,
                   'survived': survived, 'broken_pattern': broken, 'rows': rows}, f, indent=1, sort_keys=True)
    return 0 if (killed == total and survived == 0 and broken == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
