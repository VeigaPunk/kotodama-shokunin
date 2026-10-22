# ExecGateEntity — claim O implementation

## Files and behavior

- Updated `/fast/scratch/hyaku/kotodama-r56/ExecGateEntity/work/check-gate-quotes.py` and copied it to `/fast/scratch/hyaku/kotodama-r56/ExecGateEntity/copy/tools/check-gate-quotes.py` in the lane archive at base `052f145cbcff6996c153d460d81ce346ce74bfbc`.
- Gate rows are classified once as `html-entity` when they carry a semicolon-terminated decimal or hexadecimal numeric reference or a named reference found exactly in `html.entities.html5`. Unrecognized names, names without semicolons, and the bare ampersand cases remain unreported.
- Recognized references are decoded once with `html.unescape` before quote span/count, ellipsis, doubled-locator, and truncated-Grounds checks.
- Invalid UTF-8 now produces the required `GATE_QUOTES_ERROR: <path>: not valid UTF-8 (...)` diagnostic and error exit through the ordinary run path.
- Selftest cases cover named references, once-per-row reporting, bare-ampersand boundary, decoded Grounds (truncated and whole), encoded quote marks (over-cap and short), decoded ellipsis and doubled locator, plus invalid/valid UTF-8.
- No lane implementation source was changed; code and archive copy are under the assigned scratch directory. No tools were installed. LSP was unavailable in the provided tool inventory.

## Commands and evidence

1. Archive and initial tool-copy command:

   `mkdir -p /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/copy /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/work && git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive 052f145cbcff6996c153d460d81ce346ce74bfbc | tar -x -C /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/copy && cp /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/work/check-gate-quotes.py`

   Output: none. Exit code: 0.

2. HTML5 key boundary inspection:

   `python3 -c 'import html.entities; print({name: name in html.entities.html5 for name in ("T;", "D;", "copy;", "quot;", "hellip;")})'`

   Output: `{'T;': False, 'D;': False, 'copy;': True, 'quot;': True, 'hellip;': True}`. Exit code: 0.

3. First diff-capture attempt (the `cp` preceding `&&` succeeded; diff option syntax did not):

   `cp /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/work/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/copy/tools/check-gate-quotes.py && diff -u --label a/tools/check-gate-quotes.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py --label b/tools/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/work/check-gate-quotes.py`

   Output: `error: 2 values required for '<FILES> <FILES>...' but 1 was provided`, followed by the diff usage text. Exit code: 2.

4. Corrected unified-diff capture:

   `diff -u -L a/tools/check-gate-quotes.py -L b/tools/check-gate-quotes.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r56/ExecGateEntity/work/check-gate-quotes.py`

   Output: the patch below. Exit code: 1 (the files differ, as expected).

5. Requested acceptance/checker commands were **not run**: the editing-wave instruction says not to run builds/tests/linters/formatters and assigns post-integration gate execution to the parent. Output: none. Exit code: not applicable.

   - `python3 -B reports/round-56/accept-o.py` (from the scratch lane copy): not run.
   - `python3 -B tools/check-gate-quotes.py corpus/lessons/round-5{0,1,2,3,4,5}.md` (from the scratch lane copy): not run.
   - `python3 -B tools/check-gate-quotes.py --selftest`: not run.

## Unified diff

```diff
--- a/tools/check-gate-quotes.py
+++ b/tools/check-gate-quotes.py
@@ -61,6 +61,11 @@
     ` ; same URL` shape) a truncated first Grounds is not reported.
   * A row is reported once per offending run and once per new shape; if a run
     has two quote findings, the over-cap count takes precedence.
+  * `html-entity` reports once per row with at least one numeric reference
+    (`&#NNN;` or `&#xHH;`) or a semicolon-terminated named reference whose
+    exact `name;` is in `html.entities.html5`. Bare ampersands, names without
+    a semicolon, and unrecognized names are not references. Each recognized
+    reference is decoded once before the other rules run.
 
 Usage:
   python3 -B check-gate-quotes.py <lesson.md>...
@@ -68,17 +73,21 @@
 
 Output: one line per finding on stdout, then a summary line. Existing quote
 findings retain their original detail; shape findings use their class name.
-  <path>:<line> <S-id> words=<n> | doubled-locator | truncated-grounds
+  <path>:<line> <S-id> words=<n> | html-entity | doubled-locator | truncated-grounds
 Exit codes: 0 no findings; 1 findings; 2 could not evaluate (a path is
-missing or unreadable, a file has no `## Gate` section, or no path was
-given; the reason goes to stderr as `GATE_QUOTES_ERROR:`). Read-only, Python
+missing or unreadable, has invalid UTF-8, has no `## Gate` section, or no path
+was given; the reason goes to stderr as `GATE_QUOTES_ERROR:`). Read-only, Python
 3 standard library only, no network.
 """
 
 import argparse
+import contextlib
+import html
+import io
 import os
 import re
 import sys
+import tempfile
 
 # The lane's quotation cap for a Gate quote.
 MAX_WORDS = 25
@@ -93,8 +102,27 @@
 WORDISH = re.compile(r"[\w]", re.UNICODE)
 # An ellipsis: the single character or three dots.
 ELLIPSIS = re.compile(r"…|\.\.\.")
+# Supported references require a semicolon; named references are checked
+# against the exact HTML5 entity table before they are decoded.
+HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;|#[xX][0-9A-Fa-f]+;|[A-Za-z][A-Za-z0-9]*;)")
+HTML5_ENTITIES = html.entities.html5
+
+
+def decode_html_references(line):
+    """Decode each supported HTML reference once and report whether any occurred."""
+    found = False
+
+    def decode(match):
+        nonlocal found
+        reference = match.group(0)
+        if reference.startswith("&#") or reference[1:] in HTML5_ENTITIES:
+            found = True
+            return html.unescape(reference)
+        return reference
+
+    return HTML_REFERENCE.sub(decode, line), found
+
+
 def gate_section(text):
     """The `## Gate` section as [(line_number, line)], or None if absent."""
     lines = text.splitlines()
@@ -226,16 +254,19 @@
         return []
     s_id = row.group(1)
     teaches = teaches or {}
+    decoded_line, has_html_entity = decode_html_references(line)
     findings = []
-    for run, gap_ellipsis in quote_run_details(line):
+    if has_html_entity:
+        findings.append((number, s_id, 0, "html-entity"))
+    for run, gap_ellipsis in quote_run_details(decoded_line):
         words = run_words(run)
         if words > MAX_WORDS:
             findings.append((number, s_id, words, "over-cap"))
         elif gap_ellipsis or any(ellipsis_joins(text) for text in run):
             findings.append((number, s_id, words, "ellipsis-joined"))
-    if doubled_locator(line):
+    if doubled_locator(decoded_line):
         findings.append((number, s_id, 0, "doubled-locator"))
-    if truncated_grounds(line, s_id, teaches):
+    if truncated_grounds(decoded_line, s_id, teaches):
         findings.append((number, s_id, 0, "truncated-grounds"))
     return findings
@@ -281,6 +312,9 @@
         try:
             with open(path, "r", encoding="utf-8") as handle:
                 text = handle.read()
+        except UnicodeDecodeError as exc:
+            results.append((path, None, "not valid UTF-8 (%s)" % exc))
+            continue
         except OSError as exc:
             results.append((path, None, "unreadable: %s" % exc.strerror))
             continue
@@ -307,7 +341,7 @@
             print("GATE_QUOTES_ERROR: %s: %s" % (path, error), file=sys.stderr)
             continue
         for number, s_id, words, reason in findings:
-            detail = reason if reason in ("doubled-locator", "truncated-grounds") else "words=%d" % words
+            detail = reason if reason in ("html-entity", "doubled-locator", "truncated-grounds") else "words=%d" % words
             print("%s:%d %s %s" % (path, number, s_id, detail))
             reasons[reason] = reasons.get(reason, 0) + 1
         total += len(findings)
@@ -402,16 +436,74 @@
         ("doubled-locator-wayback-note-red",
          lesson("- S900 — URL — accessed 2026-10-21 via Wayback 20260605210113 — §2 'Methods': \"Methods\": \"the real quote\".\n"),
          None, "doubled-locator"),
+        ("html-entity-named-red",
+         lesson("- S900 — p. 1: &copy;.\n"), None, "html-entity"),
+        ("html-entity-once-per-row",
+         lesson("- S900 — p. 1: &copy; &amp;.\n"), None, ("html-entity",)),
+        ("html-entity-bare-ampersands-green",
+         lesson("- S900 — AT&T; R&D; https://example.test/?a=1&b=2 &notaref;\n"),
+         None, None),
+        ("decoded-truncated-grounds-red",
+         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was a&hellip;. Seat: Scout.\n"),
+         {"S900": "the keeper was a… guardian."},
+         ("html-entity", "truncated-grounds")),
+        ("decoded-whole-grounds-green",
+         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was owed&hellip;. Seat: Scout.\n"),
+         {"S900": "the keeper was owed…."}, ("html-entity",)),
+        ("decoded-quote-marks-over-cap-red",
+         lesson('- S900 — p. 1: &#8220;%s&#8221;.\n' % long_quotes),
+         None, ("html-entity", "over-cap")),
+        ("decoded-quote-marks-short-green",
+         lesson('- S900 — p. 1: &#8220;one two&#8221;.\n'),
+         None, ("html-entity",)),
+        ("decoded-ellipsis-red",
+         lesson('- S900 — p. 1: &quot;one two&hellip; three four&quot;.\n'),
+         None, ("html-entity", "ellipsis-joined")),
+        ("decoded-doubled-locator-red",
+         lesson('- S900 — URL — accessed 2026-10-22 — Section &quot;X&quot;: '
+                '&quot;X&quot;: &quot;real quote&quot;.\n'),
+         None, ("html-entity", "doubled-locator")),
     ]
     for name, body, source_teaches, want in class_cases:
         findings = scan_text(body, source_teaches)
         got = [] if findings is None else [reason for _, _, _, reason in findings]
-        expected = [] if want is None else [want]
+        expected = ([] if want is None else
+                    list(want) if isinstance(want, (tuple, list)) else [want])
         ok = got == expected
         failures += not ok
         print("%s %s want=%s got=%s" %
               ("PASS" if ok else "FAIL", name, want or "none", ",".join(got) or "none"))
-    total = len(cases) + len(class_cases)
+    with tempfile.TemporaryDirectory(prefix="check-gate-quotes-selftest-") as directory:
+        invalid_path = os.path.join(directory, "invalid-utf8.md")
+        valid_path = os.path.join(directory, "valid-utf8.md")
+        with open(invalid_path, "wb") as handle:
+            handle.write(b"## Gate\n\n- S900 \xff\n")
+        with open(valid_path, "w", encoding="utf-8") as handle:
+            handle.write(lesson('- S900 — p. 1: "café".\n'))
+
+        invalid_out = io.StringIO()
+        invalid_err = io.StringIO()
+        with contextlib.redirect_stdout(invalid_out), contextlib.redirect_stderr(invalid_err):
+            invalid_code = run([invalid_path])
+        invalid_error = invalid_err.getvalue().splitlines()
+        invalid_ok = (invalid_code == 2 and invalid_error
+                      and invalid_error[0].startswith(
+                          "GATE_QUOTES_ERROR: %s: not valid UTF-8 (" % invalid_path)
+                      and "Traceback" not in invalid_err.getvalue())
+        failures += not invalid_ok
+        print("%s utf8-invalid-red want=error-exit-2 got=%s" %
+              ("PASS" if invalid_ok else "FAIL", invalid_error[0] if invalid_error else "none"))
+
+        valid_out = io.StringIO()
+        valid_err = io.StringIO()
+        with contextlib.redirect_stdout(valid_out), contextlib.redirect_stderr(valid_err):
+            valid_code = run([valid_path])
+        valid_ok = (valid_code == 0 and not valid_err.getvalue()
+                    and valid_out.getvalue() == "GATE_QUOTES: 0 findings\n")
+        failures += not valid_ok
+        print("%s utf8-valid-green want=exit-0 got=%s" %
+              ("PASS" if valid_ok else "FAIL", valid_code))
+    total = len(cases) + len(class_cases) + 2
     print("SELFTEST: %d/%d pass" % (total - failures, total))
     return 1 if failures else 0
```

## Risk / blocker

The acceptance and six-lesson runs remain unverified because the editing-wave instruction reserves checks for the parent after integration. The report and source patch are complete; the parent should run those gates at integration time.
