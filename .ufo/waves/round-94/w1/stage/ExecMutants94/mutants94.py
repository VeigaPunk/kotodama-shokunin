#!/usr/bin/env python3
"""Deterministic mutation pass over tools/check-advance-evidence.py (round 94).

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
--work; the mutant is KILLED when the mutated tool's own --selftest exits non-zero
or does not print the SELFTEST PASS line; the clean bytes must be green first.

A missing or nonexistent --work is refused with a named diagnostic, rc 2
(routed round-92 R92-M3 / spot-check §6 item 4: the round-92 mutants.py crashed
with FileNotFoundError on a nonexistent --work).

--tool <path> (required) is the tool whose bytes are mutated; --work (required) must exist.
(the stub control: a printer that cannot apply the pairs scores 0 killed).

Receipt: <work>/mutation94-score.txt (no network, no lane write; every copy and
mutant lives under --work).
"""

import argparse
import hashlib
import os
import shutil
import subprocess
import sys


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
    # -------- round-94 routed classes (corpus/lessons/round-93.md, "## Routed to round 94") --------
    ('script-strip-off', "s = re.sub(r'(?is)<(script|style)\\b[^>]*>.*?</\\1\\s*>', ' ', s)", 'pass'),
    ('comment-strip-off', "s = re.sub(r'(?s)<!--.*?-->', ' ', s)", 'pass'),
    ('unescape-off', 'return _html.unescape(s)', 'return s'),
    ('dispo-any-casei', "DISPO_ANY_RE = re.compile(r'\\bS(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b')", "DISPO_ANY_RE = re.compile(r'\\bS(\\d{3,})\\b.*?\\b(NOT[ _-]?LOCATED|LOCATED)\\b', re.I)"),
    ('baserows-drop-cell8', 'for i in (0, 1, 2, 3, 4, 5, 6, 8):', 'for i in (0, 1, 2, 3, 4, 5, 6):'),
]

NAMES = [m[0] for m in MUTANTS]

# Round-93 entries keep their replace-all semantics (six match 2-3 sites on v4); a
# pattern that is absent is refused for every entry. The five routed patches must
# match exactly once, else the mutant is refused as BROKEN-PATTERN.
ROUTED = ('script-strip-off', 'comment-strip-off', 'unescape-off', 'dispo-any-casei', 'baserows-drop-cell8')


def run(tool, work, tag):
    d = os.path.join(work, 'st-' + tag)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', tool, '--selftest', '--work', d],
                       capture_output=True, text=True)
    out = r.stdout or ''
    return r.returncode, 'SELFTEST PASS' in out, out.strip().splitlines()[:1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tool', required=True, help='tool bytes to mutate; read only, every mutant is a copy under --work')
    ap.add_argument('--work', required=True, help='existing scratch directory; all copies, mutants and the receipt live here')
    ap.add_argument('--only', default='', help='comma-separated mutant names; default is the full set')
    args = ap.parse_args()
    if not os.path.isdir(args.work):
        print('MUTANTS94_ERROR: --work must be an existing directory', file=sys.stderr)
        return 2
    if not os.path.isfile(args.tool):
        print(f'MUTANTS94_ERROR: --tool is not a file: {args.tool}', file=sys.stderr)
        return 2
    wanted = [n.strip() for n in args.only.split(',') if n.strip()]
    unknown = [n for n in wanted if n not in NAMES]
    if unknown:
        print(f'MUTANTS94_ERROR: unknown mutant name(s): {", ".join(unknown)}', file=sys.stderr)
        return 2
    selected = [m for m in MUTANTS if not wanted or m[0] in wanted]

    with open(args.tool, 'rb') as f:
        src = f.read().decode('utf-8')
    src_sha = hashlib.sha256(src.encode('utf-8')).hexdigest()

    clean_tool = os.path.join(args.work, 'clean-tool.py')
    with open(clean_tool, 'w') as f:
        f.write(src)
    clean_rc, clean_pass, clean_head = run(clean_tool, args.work, 'clean')
    if clean_rc != 0 or not clean_pass:
        line = f'MUTATION-SCORE: 0/{len(selected)} killed, {len(selected)} survived, 0 broken-pattern (clean tool not green first: rc={clean_rc})'
        print(line)
        return 1

    killed, survived, broken, rows = 0, 0, 0, []
    for name, old, new in selected:
        n = src.count(old)
        if n == 0 or (name in ROUTED and n != 1):
            broken += 1
            rows.append(f'  BROKEN-PATTERN {name}: pattern matched {n} times (absent, or a routed patch not exactly once)')
            print(f'MUTANT {name} BROKEN-PATTERN selftest_rc=n/a')
            continue
        mut_path = os.path.join(args.work, 'mut-' + name + '.py')
        with open(mut_path, 'w') as f:
            f.write(src.replace(old, new))
        rc, passed, head = run(mut_path, args.work, name)
        if rc != 0 or not passed:
            killed += 1
            status = 'KILLED'
        else:
            survived += 1
            status = 'SURVIVED'
        rows.append(f'  {status} {name}: selftest rc={rc} SELFTEST-PASS-line={passed}')
        print(f'MUTANT {name} {status} selftest_rc={rc}')
    total = len(selected)
    line = f'MUTATION-SCORE: {killed}/{total} killed, {survived} survived, {broken} broken-pattern'
    print(line)
    with open(os.path.join(args.work, 'mutation94-score.txt'), 'w') as f:
        f.write(f'# tool sha256 {src_sha}\n# clean selftest rc={clean_rc} {clean_head}\n' + line + '\n' + '\n'.join(rows) + '\n')
    return 0 if (killed == total and survived == 0 and broken == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
