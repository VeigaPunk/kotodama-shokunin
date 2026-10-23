# ExecSyntaxSweep — round 57

## Findings

- The recursive Python syntax sweep found one failure: `reports/round-56/accept-c.py`, line 18. With `SyntaxWarning` promoted to an error, Python 3.14 reports the docstring's `\|` as an invalid escape sequence.
- Minimal fix in the scratch clone: make the module docstring raw by prefixing its opening triple quote with `r`. The script's executable code is unchanged.
- On the scratch clone at `13226c18aa352e3f3d1bfbe567f221acfb8b8344`, the acceptance script exited 0 before and after. Its stdout is byte-identical (`cmp` exit 0); patched stderr is empty, and parsing the patched file with `-W error::SyntaxWarning` exits 0.

## Syntax sweep

Command (run from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; Python processes run sequentially):

```sh
find /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools -type f -name '*.py' -print0 | while IFS= read -r -d '' file; do output=$(python3 -W error::SyntaxWarning -c 'import ast,sys; ast.parse(open(sys.argv[1]).read(), sys.argv[1])' "$file" 2>&1); status=$?; if [ "$status" -ne 0 ]; then printf 'FAIL %s (exit %s)\n%s\n' "$file" "$status" "$output"; fi; done
```

Output (sweep loop exit 0; the per-file parse failure is exit 1):

```text
FAIL /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-56/accept-c.py (exit 1)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import ast,sys; ast.parse(open(sys.argv[1]).read(), sys.argv[1])
                    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/ast.py", line 46, in parse
    return compile(source, filename, mode, flags,
                   _feature_version=feature_version, optimize=optimize)
  File "/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-56/accept-c.py", line 18
    row (a row is any line matching `^\|\s*(S\d{3,})\s*\|`, the access checker's grammar) (a cited id with no row or with two or more rows fails); the entry carries no
                                      ^^
SyntaxError: "\|" is an invalid escape sequence. Did you mean "\\|"? A raw string is also an option.
```

## Scratch clone and minimal unified diff

Clone command (GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset; exit 0):

```sh
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone --no-hardlinks --no-checkout /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane && env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane checkout --detach 13226c18aa352e3f3d1bfbe567f221acfb8b8344 && env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane rev-parse HEAD
```

Output:

```text
Cloning into '/fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane'...
done.
HEAD is now at 13226c1 round-57: declaration revised on claim base 0314aa98 (after the pre-dispatch critics; no data yet) — ACCEPT-C-57 nine legs incl. LOCATE and FRESH, ACCEPT-O-57 seven legs incl. REAL and neutral patches; receipts: controls-c 7/7 as expected, controls-o 16/16 as expected (green passes), locator calibration 38/54 under the revised rules
13226c18aa352e3f3d1bfbe567f221acfb8b8344
```

Patch command (scratch clone, exit 0):

```sh
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane diff --no-ext-diff --unified=3 -- reports/round-56/accept-c.py
```

Output:

```diff
diff --git i/reports/round-56/accept-c.py w/reports/round-56/accept-c.py
index 377bc81..2950275 100644
--- i/reports/round-56/accept-c.py
+++ w/reports/round-56/accept-c.py
@@ -1,5 +1,5 @@
 #!/usr/bin/env python3
-"""Round-56 claim C acceptance (adapted from reports/round-55/accept-c.py: entry path, totals, and RANGE now bounded above by C's reserved block). Run from the lane root:
+r"""Round-56 claim C acceptance (adapted from reports/round-55/accept-c.py: entry path, totals, and RANGE now bounded above by C's reserved block). Run from the lane root:
 
   python3 -B reports/round-56/accept-c.py [--root DIR]
 
```

## Before/after runs

Before patch, in the scratch clone:

```sh
python3 -B reports/round-56/accept-c.py
```

stdout (exit 0):

```text
SET PASS count=232 required=232 added=['corpus/knowledge/civilizations/kongo-kingdom.md'] removed=[]
SWEEP PASS exit=0 rows 232 files 232 missing_from_index 0 []
FLOOR PASS cited=54 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
```

stderr:

```text
/fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane/reports/round-56/accept-c.py:18: SyntaxWarning: "\|" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\|"? A raw string is also an option.
  row (a row is any line matching `^\|\s*(S\d{3,})\s*\|`, the access checker's grammar) (a cited id with no row or with two or more rows fails); the entry carries no
```

After the one-character docstring-prefix patch, in the same scratch clone:

```sh
python3 -B reports/round-56/accept-c.py
```

stdout (exit 0):

```text
SET PASS count=232 required=232 added=['corpus/knowledge/civilizations/kongo-kingdom.md'] removed=[]
SWEEP PASS exit=0 rows 232 files 232 missing_from_index 0 []
FLOOR PASS cited=54 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
```

stderr was empty. Patched-file parse command and output (exit 0):

```sh
python3 -W error::SyntaxWarning -c 'import ast,sys; ast.parse(open(sys.argv[1]).read(), sys.argv[1])' reports/round-56/accept-c.py
exit=0
```

Comparison command and output (exit 0):

```sh
cmp /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/before.stdout /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/after.stdout; stdout_status=$?; cmp /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/before.exit /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/after.exit; exit_status=$?; if test ! -s /fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/after.stderr; then warning_status=0; else warning_status=1; fi; printf 'stdout cmp exit=%s\nexit-status cmp exit=%s\nafter stderr empty (SyntaxWarning absent) check exit=%s\n' "$stdout_status" "$exit_status" "$warning_status"; test "$stdout_status" -eq 0 -a "$exit_status" -eq 0 -a "$warning_status" -eq 0
```

```text
stdout cmp exit=0
exit-status cmp exit=0
after stderr empty (SyntaxWarning absent) check exit=0
```

## Changed paths, risks and blockers

- Lane source files: unchanged. The only source edit is `/fast/scratch/hyaku/kotodama-r57/KotodamaR57.ExecSyntaxSweep/lane/reports/round-56/accept-c.py`, a raw-string docstring prefix; the assigned report is `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-57/build/ExecSyntaxSweep.md`.
- Behavior: the module docstring now treats its regex backslashes literally; acceptance stdout and exit status are unchanged, and the invalid-escape warning is absent.
- Risks: none observed for this one-character docstring change.
- Blockers: none.
