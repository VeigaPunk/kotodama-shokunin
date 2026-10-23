# ExecGateBareNumeric — Round 57 O

## Findings

- Scratch implementation: `/fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/check-gate-quotes.py`.
- Scratch clone at `13226c18aa352e3f3d1bfbe567f221acfb8b8344`, with the updated tool copied to `lane/tools/check-gate-quotes.py`.
- SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.
- `HTML_REFERENCE` now accepts decimal and hexadecimal numeric references with an optional `;`, while named references still require a semicolon and the exact HTML5 entity name. The checker continues to decode recognized references once; selftest coverage now includes bare numeric references, malformed forms, invalid code points, and behavioral checks for double decoding, continuing after an unreadable file, and the printed `html-entity` label.
- No files were changed in the lane checkout. No tools were installed.
- LSP was unavailable in the exposed session tool inventory; no LSP result is asserted.

## Exact retained evidence

Scratch clone and source copy command completed with output:

```text
scratch clone and source copy ready
```

Hash command and output:

```text
$ cp /fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/lane/tools/check-gate-quotes.py && sha256sum /fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/check-gate-quotes.py
54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7  /fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/check-gate-quotes.py
```

## Requested acceptance runs

Not run. The fleet-executor instructions assign post-integration verification to the parent and prohibit running checks during the editing wave. No output or exit code is claimed.

Commands for the parent to run (first three from the scratch clone root, last from the lane root):

```text
TMPDIR=/fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/tmp python3 -B reports/round-57/accept-o.py
TMPDIR=/fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/tmp python3 -B reports/round-57/accept-o.py
TMPDIR=/fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/tmp python3 -B reports/round-57/accept-o.py
TMPDIR=/fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/tmp python3 -B reports/round-57/accept-o.py --tool /fast/scratch/hyaku/kotodama-r57/ExecGateBareNumeric/check-gate-quotes.py
```

## Patch against the lane tool

```diff
diff --git i/tools/check-gate-quotes.py w/tools/check-gate-quotes.py
index c4f3ca7..eb86f00 100755
--- i/tools/check-gate-quotes.py
+++ w/tools/check-gate-quotes.py
@@ -61,11 +61,15 @@ Word count rule
     ` ; same URL` shape) a truncated first Grounds is not reported.
   * A row is reported once per offending run and once per new shape; if a run
     has two quote findings, the over-cap count takes precedence.
-  * `html-entity` reports once per row with at least one numeric reference
-    (`&#NNN;` or `&#xHH;`) or a semicolon-terminated named reference whose
-    exact `name;` is in `html.entities.html5`. Bare ampersands, names without
-    a semicolon, and unrecognized names are not references. Each recognized
-    reference is decoded once before the other rules run.
+  * `html-entity` reports once per row with at least one numeric character
+    reference (decimal or hexadecimal, with or without its closing semicolon)
+    or a semicolon-terminated named reference whose exact name is in
+    `html.entities.html5`. Numeric references consume the maximal digit run;
+    named references bind only with `;`. Bare ampersands, names without a
+    semicolon, unrecognized names, and malformed numerics are not references.
+    Invalid numeric code points (`&#0;`, `&#xD800;`, `&#1114112;`) decode to
+    U+FFFD and still report `html-entity`. Each recognized reference is
+    decoded once before the other rules run.
 
 Usage:
   python3 -B check-gate-quotes.py <lesson.md>...
@@ -102,9 +106,9 @@ QUOTE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»')
 WORDISH = re.compile(r"[\w]", re.UNICODE)
 # An ellipsis: the single character or three dots.
 ELLIPSIS = re.compile(r"…|\.\.\.")
-# Supported references require a semicolon; named references are checked
-# against the exact HTML5 entity table before they are decoded.
-HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;|#[xX][0-9A-Fa-f]+;|[A-Za-z][A-Za-z0-9]*;)")
+# Numeric references accept an optional semicolon; named references require
+# one and are checked against the exact HTML5 entity table.
+HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;?|#[xX][0-9A-Fa-f]+;?|[A-Za-z][A-Za-z0-9]*;)")
 HTML5_ENTITIES = html.entities.html5
 
 
@@ -405,6 +409,26 @@ def selftest():
         failures += not ok
         print("%s %s want=%s got=%s" % ("PASS" if ok else "FAIL", name, want, got))
 
+    reference_cases = [
+        ("numeric-decimal-bare-before-space", "&#233 ", ("é ", True)),
+        ("numeric-decimal-bare-before-letter", "&#233w", ("éw", True)),
+        ("numeric-hex-bare-before-space", "&#xE9 ", ("é ", True)),
+        ("numeric-hex-bare-before-nonhex", "&#xE9z", ("éz", True)),
+        ("invalid-zero-codepoint", "&#0;", ("\ufffd", True)),
+        ("invalid-surrogate-codepoint", "&#xD800;", ("\ufffd", True)),
+        ("invalid-out-of-range-codepoint", "&#1114112;", ("\ufffd", True)),
+        ("malformed-decimal-reference", "&#;", ("&#;", False)),
+        ("malformed-hex-reference-empty", "&#x;", ("&#x;", False)),
+        ("malformed-hex-reference-nondigit", "&#xg", ("&#xg", False)),
+        ("named-reference-requires-semicolon", "&copy ", ("&copy ", False)),
+    ]
+    for name, reference, want in reference_cases:
+        got = decode_html_references(reference)
+        ok = got == want
+        failures += not ok
+        print("%s %s want=%r got=%r" %
+              ("PASS" if ok else "FAIL", name, want, got))
+
     class_cases = [
         ("doubled-locator-single-quoted-red",
         lesson("- S900 — URL — accessed 2026-10-22 — Section 'X': \"X\": \"real quote\".\n"),
@@ -440,6 +464,10 @@ def selftest():
         lesson("- S900 — p. 1: &copy;.\n"), None, "html-entity"),
         ("html-entity-once-per-row",
          lesson("- S900 — p. 1: &copy; &amp;.\n"), None, ("html-entity",)),
+        ("double-encoded-ellipsis-decoded-once",
+         lesson('- S900 — p. 1: "one &amp;hellip; two".\n'),
+         None, ("html-entity",)),
+
         ("html-entity-bare-ampersands-green",
         lesson("- S900 — AT&T; R&D; https://example.test/?a=1&b=2 &notaref;\n"),
@@ -480,6 +508,13 @@ def selftest():
             handle.write(b"## Gate\n\n- S900 \xff\n")
         with open(valid_path, "w", encoding="utf-8") as handle:
             handle.write(lesson('- S900 — p. 1: "café".\n'))
+        entity_path = os.path.join(directory, "entity.md")
+        entity_row = "- S901 — p. 1: &copy;.\n"
+        entity_text = lesson(entity_row)
+        entity_line = entity_text.splitlines().index(entity_row.rstrip("\n")) + 1
+        with open(entity_path, "w", encoding="utf-8") as handle:
+            handle.write(entity_text)
+
 
         invalid_out = io.StringIO()
         invalid_err = io.StringIO()
@@ -503,7 +538,37 @@ def selftest():
         failures += not valid_ok
         print("%s utf8-valid-green want=exit-0 got=%s" %
               ("PASS" if valid_ok else "FAIL", valid_code))
-    total = len(cases) + len(class_cases) + 2
+        entity_out = io.StringIO()
+        entity_err = io.StringIO()
+        with contextlib.redirect_stdout(entity_out), contextlib.redirect_stderr(entity_err):
+            entity_code = run([entity_path])
+        entity_finding = "%s:%d S901 html-entity" % (entity_path, entity_line)
+        entity_ok = (entity_code == 1 and not entity_err.getvalue()
+                     and entity_finding in entity_out.getvalue().splitlines()
+                     and entity_out.getvalue().splitlines()[-1] == "GATE_QUOTES: 1 findings"
+                     and any(line.endswith(" html-entity")
+                             for line in entity_out.getvalue().splitlines()))
+        failures += not entity_ok
+        print("%s behavioural-entity-label want=html-entity got=%r" %
+              ("PASS" if entity_ok else "FAIL", entity_out.getvalue().splitlines()))
+
+        mixed_out = io.StringIO()
+        mixed_err = io.StringIO()
+        with contextlib.redirect_stdout(mixed_out), contextlib.redirect_stderr(mixed_err):
+            mixed_code = run([invalid_path, entity_path])
+        mixed_ok = (mixed_code == 2
+                    and mixed_out.getvalue() ==
+                    "%s\nGATE_QUOTES: 1 findings\n" % entity_finding
+                    and mixed_err.getvalue().splitlines()
+                    and mixed_err.getvalue().splitlines()[0].startswith(
+                        "GATE_QUOTES_ERROR: %s: not valid UTF-8 (" % invalid_path)
+                    and "Traceback" not in mixed_err.getvalue())
+        failures += not mixed_ok
+        print("%s behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=%r" %
+              ("PASS" if mixed_ok else "FAIL", (mixed_code, mixed_out.getvalue(),
+                                                 mixed_err.getvalue())))
+
+    total = len(cases) + len(reference_cases) + len(class_cases) + 4
+    print("SELFTEST: %d/%d pass" % (total - failures, total))
+    return 1 if failures else 0
```

## Risks and blockers

- Acceptance/mutant outputs remain unobserved pending the parent-owned verification gate.
- The requested report path `/home/vgpnk/Projects/shokunin/.ufo/waves/round-57/build/ExecGateBareNumeric.md` is outside this executor's write bounds. This report is therefore in the authorized scratch directory.
