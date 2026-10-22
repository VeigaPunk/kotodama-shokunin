# ExecIntegrateRows56 — Round 56 claim C integrator

## Axes and result

- **Operability:** copied the read-only round-55 integrator into `/fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/integrate-rows.py`; default allocation is S359–S418, inclusive, and 61 or more parsed blocks hard-fail before output.
- **Calibration:** removed `_gate_text` entity encoding; Gate quote and Grounds are emitted as UTF-8. Gate Grounds receives the exact normalized teaches value written to the registry row. Character references in report fields fail except `&#124;` inside quote/anchor input; table pipes are escaped only in anchor cells.
- **Demonstration:** all round-55 build reports yielded the expected 99-block overflow; the `ScoutMonsterTheory.md` subset generated S359–S360 with no character references in `rows.md` or `gate.md`, and the quote-checker self-check returned zero findings.

## Files, boundaries, and cause

- Script and generated subset artifacts: `/fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/` only.
- Exclusive report: `.ufo/waves/round-56/build/ExecIntegrateRows56.md`.
- No lane source, registry, lesson, or tool was edited. No installs, git/jj writes, builds, linters, or tests were run. The requested integration demonstrations and checker self-check were run. LSP was unavailable in the provided tool set; this standalone script had no repository symbols to refactor.
- Round-55 lesson evidence: `corpus/lessons/round-55.md:72` contains `&quot;monster&quot;`; `:82` contains `&quot;monstres&quot;` and `&amp;`; `:140` contains `&#8220;`/`&#8221;`. The assigned predecessor at `/fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/integrate-rows.py:121-125` converted table pipes to `&#124;`; `:420-425` encoded ampersands, straight quotes, and curly quotes in `_gate_text`, which was called for Gate URL, locator, quote, and Grounds. A search of the round-55 build reports found these transformations in the embedded integrator source; the opened source report blocks did not contain those references.
- In the generated subset, S359 row teaches and Gate Grounds are byte-identical: `Read a culture's monsters as readable signs: the word warns, mixed bodies defeat classification, and the border punishes those who cross it.` The Gate preserves inner quotation marks by choosing an unused outer quote delimiter, rather than encoding them.
- Entity-reference search on the generated subset returned `No matches found`. The only allowed registry entity is the pipe escape in an anchor when an input anchor contains a pipe; Gate output renders that escape as a literal pipe.

## Runs and retained output

### Initial CLI invocation (before restoring the copied `--reports` option)

Command:

```sh
python3 -B /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build --start 359 --end 418 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/out-overflow
```

Output:

```text
usage: integrate-rows.py [-h] [--start START] [--end END] [--sources SOURCES]
                         [--out OUT] [--self-check] [--checker CHECKER]
                         [--rewrite REWRITE] [--map MAP] [--dry-run]
                         [--used-by USED_BY] [--status STATUS]
                         [--opened OPENED] [--recheck RECHECK]
                         [--max-quote-words MAX_QUOTE_WORDS]
                         [--allow-long-quotes] [--exclude EXCLUDE]
                         [--merge-duplicates] [--no-community-kind]
                         [--merge-keep {first,last}]
integrate-rows.py: error: unrecognized arguments: --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build
```

Exit code: 2. The parser option was restored before the demonstrations below.

### Reserved-block overflow

Command:

```sh
python3 -B /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build --start 359 --end 418 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/out-overflow
```

Output:

```text
INTEGRATE_ERROR /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build/ScoutMonsterLexicon.md:28 NEW-ScoutMonsterLexicon-1 — reserved id block S359-S418 holds 60 blocks; found 99; no output written
```

Exit code: 1.

### Round-55 report subset and self-check

Command:

```sh
python3 -B /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build --start 359 --end 418 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/out-subset --exclude '^(?!.*ScoutMonsterTheory\.md$)' --self-check
```

Output:

```text
SELF_CHECK_COMMAND python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/out-subset/.gate-self-check-pyiyvv_c/corpus/lessons/gate.md
GATE_QUOTES: 0 findings
SELF_CHECK_EXIT 0
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build/ScoutMonsterTheory.md:19 NEW-ScoutMonsterTheory-1 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-55/build/ScoutMonsterTheory.md:50 NEW-ScoutMonsterTheory-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE: files=1 blocks=2 groups=2 ids=S359..S360 rows=2 warnings=2
INTEGRATE_OK rows.md map.tsv gate.md sentences.md -> /fast/scratch/hyaku/kotodama-r56/ExecIntegrateRows56/out-subset
```

Exit code: 0. The two source-report marker warnings are retained as emitted; this was a historical subset demonstration, not a round-56 source land.

## Risks and blockers

- A source quote containing all three supported quote delimiter styles is rejected rather than altered. This preserves quotation text without entities.
- Literal table pipes in non-anchor cells are rejected; only anchor cells may serialize the registry's `&#124;` escape.
- The self-check runs the lane's current `tools/check-gate-quotes.py`; it uses a temporary lesson shell and companion `SOURCES.md` built from generated rows, then removes that temporary fixture.
- No blockers or package changes.

## Unified diff against the assigned read-only round-55 predecessor

```diff
--- integrate-rows.py.round55
+++ integrate-rows.py.round56
@@ -1,5 +1,5 @@
 #!/usr/bin/env python3
-"""integrate-rows.py — kotodama round-55 claim C registry integrator.
+"""integrate-rows.py — kotodama round-56 claim C registry integrator.
 
 Turns seat reports' `### NEW-<Seat>-<n>` blocks into four artefacts:
 
@@ -14,9 +14,9 @@
 map.tsv.
 
 Usage:
-  python3 -B integrate-rows.py --reports <dir> --start 285 \
+  python3 -B integrate-rows.py --reports <dir> --start 359 --end 418 \
       --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
-      --out <dir>
+      --out <dir> --self-check
 
   python3 -B integrate-rows.py --rewrite <file> --map <map.tsv> [--dry-run]
 
@@ -28,15 +28,19 @@
 
 Hard errors (exit 1, nothing written): a block with no url, quotes or teaches
 sentence; an unparseable quote or no quote at most 25 words; a duplicate url
-unless `--merge-duplicates` is set; or a duplicate draft id. Registry id
-collisions are warnings. Stdlib only. Exit codes: 0 success, 1 hard error, 2
-bad invocation or unreadable input.
+unless `--merge-duplicates` is set; a duplicate draft id; a report character
+reference other than the registry pipe escape in an anchor; or more report
+blocks than the inclusive id range. Registry id collisions are warnings.
+Stdlib only. Exit codes: 0 success, 1 hard error, 2 bad invocation or unreadable
+input.
 """
 
 import argparse
 import os
 import re
+import subprocess
 import sys
+import tempfile
 
 # --- block and field grammar -------------------------------------------------
 
@@ -44,6 +48,8 @@
 KEY_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*:\s*(?!/)(?P<val>.*)$")
 BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
 MARKER_RE = re.compile(r"\((?P<did>NEW-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*-\d+)\s*,\s*(?P<loc>[^)]*)\)")
+CHAR_REF_RE = re.compile(r"&(?:#[0-9]+|#[xX][0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]+);")
+
 
 KEY_ALIASES = {
     "citation": "citation",
@@ -118,10 +124,20 @@
     return KEY_ALIASES.get(key)
 
 
-def cell(text):
-    """One table cell: single line, with literal table pipes encoded."""
-    text = re.sub(r"\s+", " ", (text or "").strip())
-    return text.replace("|", "&#124;")
+def cell(text, field):
+    """Normalize a registry cell without emitting entities outside pipe anchors."""
+    raw = text or ""
+    for match in CHAR_REF_RE.finditer(raw):
+        if field == "anchor" and match.group(0) == "&#124;":
+            continue
+        raise ValueError("character reference %r is not permitted in %s field"
+                         % (match.group(0), field))
+    normalized = re.sub(r"\s+", " ", raw.strip())
+    if "|" in normalized:
+        if field != "anchor":
+            raise ValueError("literal table pipe is not permitted in %s field" % field)
+        normalized = normalized.replace("|", "&#124;")
+    return normalized
 
 
 def words(text):
@@ -285,6 +301,19 @@
     return blocks
 
 
+def input_reference_problems(block):
+    """Reject report references, except the registry pipe escape in quote anchors."""
+    problems = []
+    for field, values in block.fields.items():
+        for value in values:
+            for match in CHAR_REF_RE.finditer(value):
+                if field == "quotes" and match.group(0) == "&#124;":
+                    continue
+                problems.append((block, "character reference %r is not permitted in %s field"
+                                 % (match.group(0), field)))
+    return problems
+
+
 def block_quotes(block, problems):
     """Bulleted quotes of a block as (locator, quote, tail, multiple) records."""
     pairs = []
@@ -401,6 +430,7 @@
                         "cell before the row is filed (QUALITY criterion 10)"
                         % bypass.group(0))
 
+    teaches_cell = cell(teaches or "—", "teaches")
     values = {
         "id": sid,
         "source": source,
@@ -408,32 +438,78 @@
         "tier": tier,
         "scope": scope_cell,
         "anchor": anchor,
-        "teaches": teaches or "—",
+        "teaches": teaches_cell,
         "status": args.status,
         "opened": args.opened,
         "recheck": args.recheck,
         "used-by": args.used_by,
     }
-    return [cell(values.get(name, "")) for name in columns], warnings
+    return [cell(values.get(name, ""), name) for name in columns], warnings, teaches_cell
+
 
+def gate_label(text):
+    """Render metadata without quotation spans or HTML character references."""
+    return ((text or "").replace("&#124;", "|")
+            .translate(str.maketrans({
+                '"': "'",
+                "“": "‘",
+                "”": "’",
+                "«": "‹",
+                "»": "›",
+            })))
 
-def _gate_text(text):
-    """Encode nested quotation marks so a Gate row has one quoted span."""
-    return ((text or "").replace("&", "&amp;")
-            .replace('"', "&quot;")
-            .replace("“", "&#8220;")
-            .replace("”", "&#8221;"))
 
+def gate_quote(text):
+    """Choose an unused delimiter so source quotation bytes remain unchanged."""
+    quote = (text or "").replace("&#124;", "|").strip()
+    for opening, closing in (("“", "”"), ("«", "»"), ('"', '"')):
+        if opening not in quote and closing not in quote:
+            return opening + quote + closing
+    raise ValueError("quote contains every supported Gate delimiter; refusing to alter quote text")
+
 
 def gate_line(sid, url, locator, quote, teaches, seat, accessed):
-    """One Gate line with one source quote and the full block teaches sentence."""
-    quote = quote.strip()
-    ground = teaches.strip()
-    if ground and ground[-1] not in ".!?":
-        ground += "."
-    where = ('%s: "%s"' % (_gate_text(locator), _gate_text(quote))) if locator else ('"%s"' % _gate_text(quote))
-    return '- %s — %s — accessed %s — %s. Grounds: %s Seat: %s.' % (
-        sid, _gate_text(url), accessed, where, _gate_text(ground), seat)
+    """Keep Grounds identical to the registry teaches cell."""
+    where = ("%s: " % gate_label(locator)) if locator else ""
+    where += gate_quote(quote)
+    return "- %s — %s — accessed %s — %s. Grounds: %s Seat: %s." % (
+        sid, gate_label(url), accessed, where, teaches, seat)
+
+
+def self_check(args, rows_path, gate_path):
+    """Run the lane quote checker on a lesson shell with matching source rows."""
+    if not args.self_check:
+        return 0
+    with tempfile.TemporaryDirectory(prefix=".gate-self-check-", dir=args.out) as work:
+        corpus = os.path.join(work, "corpus")
+        lessons = os.path.join(corpus, "lessons")
+        os.makedirs(lessons)
+        source_path = os.path.join(corpus, "SOURCES.md")
+        lesson_path = os.path.join(lessons, "gate.md")
+        with open(rows_path, encoding="utf-8") as handle:
+            rows = handle.read()
+        with open(source_path, "w", encoding="utf-8") as handle:
+            handle.write("| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n")
+            handle.write(rows)
+        with open(gate_path, encoding="utf-8") as handle:
+            gate = handle.read()
+        with open(lesson_path, "w", encoding="utf-8") as handle:
+            handle.write("# Round 56 — lesson (kotodama)\n\n")
             handle.write(gate)
+            if gate and not gate.endswith("\n"):
+                handle.write("\n")
+            handle.write("\n## Status\n")
+
+        command = ["python3", "-B", args.checker, lesson_path]
+        print("SELF_CHECK_COMMAND %s" % " ".join(command))
+        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
+                                universal_newlines=True)
+        if result.stdout:
+            sys.stdout.write(result.stdout)
+        if result.stderr:
+            sys.stderr.write(result.stderr)
+        print("SELF_CHECK_EXIT %d" % result.returncode)
+        return result.returncode
 
 
 def integrate(args):
@@ -441,6 +517,8 @@
     if columns != COLUMNS:
         raise ValueError("registry header %r does not match the expected columns %r"
                          % (columns, COLUMNS))
+    if args.end < args.start:
+        raise ValueError("--end must be greater than or equal to --start")
 
     problems, warnings = [], []
     blocks = []
@@ -448,8 +526,18 @@
     for path in files:
         blocks.extend(parse_report(path))
 
+    capacity = args.end - args.start + 1
+    if len(blocks) > capacity:
+        block = blocks[capacity]
+        print("INTEGRATE_ERROR %s:%d %s — reserved id block S%03d-S%03d holds %d blocks; "
+              "found %d; no output written"
+              % (block.path, block.line, block.draft_id, args.start, args.end,
+                 capacity, len(blocks)), file=sys.stderr)
+        return 1
+
     seen_draft = {}
     for block in blocks:
+        problems.extend(input_reference_problems(block))
         if block.draft_id in seen_draft:
             problems.append((block, "draft id %s already used in %s:%d"
                              % (block.draft_id, seen_draft[block.draft_id][0],
@@ -534,7 +622,7 @@
         if sid in existing:
             warnings.append((block, "assigned id %s already exists in the registry; the row would "
                                     "duplicate it" % sid))
-        cells, row_warnings = build_row(block, sid, args, columns)
+        cells, row_warnings, teaches_cell = build_row(block, sid, args, columns)
         rows.append("| " + " | ".join(cells) + " |")
         for message in row_warnings:
             warnings.append((block, message))
@@ -551,10 +639,10 @@
             warnings.append((block, "no quote of at most %d words; the Gate line is flagged"
                              % args.max_quote_words))
             gate.append("- %s — %s — accessed %s — NO USABLE QUOTE (every quote is over %d words). "
-                        "Grounds: %s. Seat: %s." % (sid, url, args.opened, args.max_quote_words,
-                                                   block.text("teaches"), block.seat))
+                        "Grounds: %s Seat: %s." % (sid, gate_label(url), args.opened,
+                                                   args.max_quote_words, teaches_cell, block.seat))
         else:
-            gate.append(gate_line(sid, url, chosen[0], chosen[1], block.text("teaches"),
+            gate.append(gate_line(sid, url, chosen[0], chosen[1], teaches_cell,
                                   block.seat, args.opened))
 
         for member in [block] + members:
@@ -590,6 +678,11 @@
         sentence_lines.append("")
     with open(os.path.join(args.out, "sentences.md"), "w", encoding="utf-8") as handle:
         handle.write("\n".join(sentence_lines).rstrip() + "\n")
+    self_check_status = self_check(
+        args, os.path.join(args.out, "rows.md"), os.path.join(args.out, "gate.md"))
+    if self_check_status:
+        return self_check_status
+
 
     for block, message in warnings:
         print("INTEGRATE_WARN %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
@@ -640,13 +733,18 @@
 def main():
     parser = argparse.ArgumentParser(add_help=True)
     parser.add_argument("--reports", help="directory of seat reports")
-    parser.add_argument("--start", type=int, default=285, help="first S-id to assign")
+    parser.add_argument("--start", type=int, default=359, help="first S-id to assign")
+    parser.add_argument("--end", type=int, default=418, help="last S-id to assign (inclusive)")
     parser.add_argument("--sources", help="path to corpus/SOURCES.md")
     parser.add_argument("--out", help="directory for rows.md, map.tsv, gate.md, sentences.md")
+    parser.add_argument("--self-check", action="store_true",
+                         help="run tools/check-gate-quotes.py on the generated Gate in a lesson shell")
+    parser.add_argument("--checker", default="/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py",
+                        help="quote checker used by --self-check")
     parser.add_argument("--rewrite", help="file whose draft ids are replaced in place")
     parser.add_argument("--map", help="map.tsv used by --rewrite")
     parser.add_argument("--dry-run", action="store_true", help="--rewrite without writing")
-    parser.add_argument("--used-by", default="corpus/knowledge/myth-symbol/monsters-hybrid-beings.md",
+    parser.add_argument("--used-by", default="corpus/knowledge/civilizations/kongo-kingdom.md",
                         help="used-by cell of every row")
     parser.add_argument("--status", default="mined", help="status cell of every row")
     parser.add_argument("--opened", default="2026-10-22", help="opened date in Gate lines and rows")
```
