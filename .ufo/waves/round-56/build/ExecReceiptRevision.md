# Receipt revision probe

Axes: operability; calibration.

## Result

The revision test is sensitive: the round-55 receipt fails the unmodified check only because it has no measured-revision line, and passes when that predicate alone is removed. The requested unmodified `run --rev 052f145...` prints the right measured hash but then raises `FileNotFoundError` before running any declared command: commit `052f145` has neither `reports/round-56/claims.json` nor `reports/round-56/separability-manifest.json`. The source calls `declared(clone)` at line 81. A one-line scratch-only patch loads declarations from the current declaration tree (`declared()`) while leaving every declared subprocess's `cwd=clone` at line 83. With that patch, all six commands run in the sandbox at `052f145`; the separability and agreement commands exit 2 because those two inputs are absent at that historical revision.

A supplemental run at the actual declaration commit `b4b7db91...` succeeds as a runner invocation and executes all six commands in its sandbox. This distinguishes the specified revision's missing inputs from the runner's revision-label behavior. The minimal diff below is proposed only; it was not applied to the lane.

## Minimal patch (against lane file)

```diff
--- a/reports/round-56/dry-run.py
+++ b/reports/round-56/dry-run.py
@@ -81 +81 @@
-    for role, command, shell, expected in declared(clone):
+    for role, command, shell, expected in declared():
```

The test copy also set `SCRATCH` to this seat's scratch directory so all generated clones stayed under `/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/`; that test-only isolation override is not part of the proposed diff.

## Runs

### 1. Unmodified check against round-55 receipt

Fixture: scratch copy `negative/reports/round-56/claims.json` contains the round-55 claims; its round-55 separability manifest and receipt are also scratch copies.

Command:

```text
python3 -B /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/negative/reports/round-56/dry-run.py check /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/negative/receipt.txt
```

Output:

```text
MISSING_FROM_RECEIPT []
UNDECLARED_IN_RECEIPT []
MEASURED_REVISION []
RUN_EXIT=1
```

### 2. Requested unmodified run at 052f145

Command (from the scratch lane clone; stdout and stderr were captured in `run-052f145.txt`):

```text
python3 -B reports/round-56/dry-run.py run --rev 052f145cbcff6996c153d460d81ce346ce74bfbc
```

Output:

```text
# dry run 2026-10-22T21:30:01Z
# measured-revision 052f145cbcff6996c153d460d81ce346ce74bfbc (sandbox clone /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-052f145c-7_mys2nr)
Traceback (most recent call last):
  File "/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/lane/reports/round-56/dry-run.py", line 121, in <module>
    sys.exit(main(sys.argv))
             ~~~~^^^^^^^^^^
  File "/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/lane/reports/round-56/dry-run.py", line 113, in main
    return run(label, argv[3])
  File "/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/lane/reports/round-56/dry-run.py", line 81, in run
    for role, command, shell, expected in declared(clone):
                                          ~~~~~~~~^^^^^^^
  File "/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/lane/reports/round-56/dry-run.py", line 41, in declared
    with open(os.path.join(root, "reports/round-56/claims.json"), encoding="utf-8") as handle:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-052f145c-7_mys2nr/reports/round-56/claims.json'
RUN_EXIT=1
```

At `052f145`, `claims.json` and `separability-manifest.json` are absent; the acceptance scripts are present. The failure occurs before the loop, so this original run did not execute any declared commands.

### 3. Sensitivity control: mutated check

The scratch-only mutation removes `or not revisions` from the return condition; no lane file changed.

Command:

```text
python3 -B /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/mutated/reports/round-56/dry-run.py check /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/mutated/receipt.txt
```

Output:

```text
MISSING_FROM_RECEIPT []
UNDECLARED_IN_RECEIPT []
MEASURED_REVISION []
RUN_EXIT=0
```

### 4. Supplemental run at declaration commit b4b7db9 (unmodified declaration lookup)

Command (from the scratch lane clone; stdout and stderr captured in `run-declaration-b4b7db9.txt`):

```text
python3 -B reports/round-56/dry-run.py run --rev b4b7db91a38447bb2c07b0ef436fc9654dcec89c
```

Output:

```text
# dry run 2026-10-22T21:31:49Z
# measured-revision b4b7db91a38447bb2c07b0ef436fc9654dcec89c (sandbox clone /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-b4b7db91-em2o5p8c)
$ python3 -B reports/round-56/accept-c.py
SET FAIL count=231 required=232 added=[] removed=[]
SWEEP FAIL exit=0 rows 231 files 231 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-b4b7db91-em2o5p8c/reports/round-56/accept-c.py:18: SyntaxWarning: "\|" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\|"? A raw string is also an option.
  row (a row is any line matching `^\|\s*(S\d{3,})\s*\|`, the access checker's grammar) (a cited id with no row or with two or more rows fails); the entry carries no
exit 1
# role: C counting; expected pre-landing: exit 1: SET FAIL (count=231 added=[] removed=[]), SWEEP FAIL (exit 0 but rows 231 files 231), FLOOR FAIL (cited=0); RANGE, STATUS, USEDBY PASS vacuously; ACCESS PASS
$ python3 -B reports/round-56/accept-c.py
SET FAIL count=231 required=232 added=[] removed=[]
SWEEP FAIL exit=0 rows 231 files 231 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-b4b7db91-em2o5p8c/reports/round-56/accept-c.py:18: SyntaxWarning: "\|" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\|"? A raw string is also an option.
  row (a row is any line matching `^\|\s*(S\d{3,})\s*\|`, the access checker's grammar) (a cited id with no row or with two or more rows fails); the entry carries no
exit 1
# role: C acceptance; expected pre-landing: fails before landing (exit 1), printing the before value; passes at all seven legs PASS (exit 0): count 232, added [corpus/knowledge/civilizations/kongo-kingdom.md], removed [], rows 232 files 232, missing_from_index 0, cited >= 20, no bad S-id
$ python3 -B reports/round-56/accept-o.py
ENTITY FAIL count=0 missing=[('corpus/lessons/round-55.md', 72, 'S288', 'html-entity'), ('corpus/lessons/round-55.md', 82, 'S298', 'html-entity'), ('corpus/lessons/round-55.md', 88, 'S304', 'html-entity'), ('corpus/lessons/round-55.md', 89, 'S305', 'html-entity'), ('corpus/lessons/round-55.md', 93, 'S309', 'html-entity'), ('corpus/lessons/round-55.md', 96, 'S312', 'html-entity'), ('corpus/lessons/round-55.md', 110, 'S326', 'html-entity'), ('corpus/lessons/round-55.md', 113, 'S329', 'html-entity'), ('corpus/lessons/round-55.md', 125, 'S341', 'html-entity'), ('corpus/lessons/round-55.md', 127, 'S343', 'html-entity'), ('corpus/lessons/round-55.md', 131, 'S347', 'html-entity'), ('corpus/lessons/round-55.md', 132, 'S348', 'html-entity'), ('corpus/lessons/round-55.md', 134, 'S350', 'html-entity'), ('corpus/lessons/round-55.md', 138, 'S354', 'html-entity'), ('corpus/lessons/round-55.md', 140, 'S356', 'html-entity'), ('corpus/lessons/round-55.md', 141, 'S357', 'html-entity')] extra=[]
NOFALSE PASS stray=[]
EXIT FAIL round55=0 fixture=0
DECODE FAIL missing=[('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'truncated-grounds'), ('reports/round-56/fixtures/lessons/entities.md', 9, 'S952', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 11, 'S954', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'words=26'), ('reports/round-56/fixtures/lessons/entities.md', 14, 'S958', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 15, 'S959', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 16, 'S960', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 16, 'S960', 'words=5')] extra=[] moved_exit=0 moved_missing=10 moved_extra=0
KEEP PASS changed=[]
BADUTF8 FAIL exit=1 stderr_first='Traceback (most recent call last):' traceback=True
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 27/27 pass
exit 1
# role: O counting; expected pre-landing: exit 1: ENTITY FAIL (count=0), EXIT FAIL (round55=0 fixture=0), DECODE FAIL (missing all ten; moved_exit=0), BADUTF8 FAIL (exit=1, Traceback); NOFALSE, KEEP, FORMAT, SELFTEST PASS
$ python3 -B reports/round-56/accept-o.py
ENTITY FAIL count=0 missing=[('corpus/lessons/round-55.md', 72, 'S288', 'html-entity'), ('corpus/lessons/round-55.md', 82, 'S298', 'html-entity'), ('corpus/lessons/round-55.md', 88, 'S304', 'html-entity'), ('corpus/lessons/round-55.md', 89, 'S305', 'html-entity'), ('corpus/lessons/round-55.md', 93, 'S309', 'html-entity'), ('corpus/lessons/round-55.md', 96, 'S312', 'html-entity'), ('corpus/lessons/round-55.md', 110, 'S326', 'html-entity'), ('corpus/lessons/round-55.md', 113, 'S329', 'html-entity'), ('corpus/lessons/round-55.md', 125, 'S341', 'html-entity'), ('corpus/lessons/round-55.md', 127, 'S343', 'html-entity'), ('corpus/lessons/round-55.md', 131, 'S347', 'html-entity'), ('corpus/lessons/round-55.md', 132, 'S348', 'html-entity'), ('corpus/lessons/round-55.md', 134, 'S350', 'html-entity'), ('corpus/lessons/round-55.md', 138, 'S354', 'html-entity'), ('corpus/lessons/round-55.md', 140, 'S356', 'html-entity'), ('corpus/lessons/round-55.md', 141, 'S357', 'html-entity')] extra=[]
NOFALSE PASS stray=[]
EXIT FAIL round55=0 fixture=0
DECODE FAIL missing=[('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'truncated-grounds'), ('reports/round-56/fixtures/lessons/entities.md', 9, 'S952', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 11, 'S954', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'words=26'), ('reports/round-56/fixtures/lessons/entities.md', 14, 'S958', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 15, 'S959', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 16, 'S960', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 16, 'S960', 'words=5')] extra=[] moved_exit=0 moved_missing=10 moved_extra=0
KEEP PASS changed=[]
BADUTF8 FAIL exit=1 stderr_first='Traceback (most recent call last):' traceback=True
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 27/27 pass
exit 1
# role: O acceptance; expected pre-landing: fails before landing (exit 1), printing the before value; passes at all eight legs PASS (exit 0)
$ python3 -B tools/check-claim-separability.py reports/round-56/separability-manifest.json
SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/civilizations/kongo-kingdom.md', which is absent from the worktree under '/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-b4b7db91-em2o5p8c'
exit 2
# role: separability; expected pre-landing: exit 2 before landing: SEPARABILITY_INPUT_ERROR naming the absent C land; checker stops at its first absent land, so later legs are unevaluated
$ python3 -B reports/round-56/claims-agree.py
AGREE claims=['C', 'O']
exit 0
```

### 5. Requested revision after the one-line scratch-only patch

The runner now reads the current declaration (`declared()`); its subprocess calls still use `cwd=clone`. Command (from the scratch lane clone; stdout and stderr captured in `run-052f145-patched.txt`):

```text
python3 -B reports/round-56/dry-run.py run --rev 052f145cbcff6996c153d460d81ce346ce74bfbc
```

Output:

```text
# dry run 2026-10-22T21:32:41Z
# measured-revision 052f145cbcff6996c153d460d81ce346ce74bfbc (sandbox clone /fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-052f145c-f7jsk68x)
$ python3 -B reports/round-56/accept-c.py
SET FAIL count=231 required=232 added=[] removed=[]
SWEEP FAIL exit=0 rows 231 files 231 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit 1
# role: C counting; expected pre-landing: exit 1: SET FAIL (count=231 added=[] removed=[]), SWEEP FAIL (exit 0 but rows 231 files 231), FLOOR FAIL (cited=0); RANGE, STATUS, USEDBY PASS vacuously; ACCESS PASS
$ python3 -B reports/round-56/accept-c.py
SET FAIL count=231 required=232 added=[] removed=[]
SWEEP FAIL exit=0 rows 231 files 231 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit 1
# role: C acceptance; expected pre-landing: fails before landing (exit 1), printing the before value; passes at all seven legs PASS (exit 0): count 232, added [corpus/knowledge/civilizations/kongo-kingdom.md], removed [], rows 232, files 232, missing_from_index 0, cited >= 20, no bad S-id
$ python3 -B reports/round-56/accept-o.py
ENTITY FAIL count=0 missing=[('corpus/lessons/round-55.md', 72, 'S288', 'html-entity'), ('corpus/lessons/round-55.md', 82, 'S298', 'html-entity'), ('corpus/lessons/round-55.md', 88, 'S304', 'html-entity'), ('corpus/lessons/round-55.md', 89, 'S305', 'html-entity'), ('corpus/lessons/round-55.md', 93, 'S309', 'html-entity'), ('corpus/lessons/round-55.md', 96, 'S312', 'html-entity'), ('corpus/lessons/round-55.md', 110, 'S326', 'html-entity'), ('corpus/lessons/round-55.md', 113, 'S329', 'html-entity'), ('corpus/lessons/round-55.md', 125, 'S341', 'html-entity'), ('corpus/lessons/round-55.md', 127, 'S343', 'html-entity'), ('corpus/lessons/round-55.md', 131, 'S347', 'html-entity'), ('corpus/lessons/round-55.md', 132, 'S348', 'html-entity'), ('corpus/lessons/round-55.md', 134, 'S350', 'html-entity'), ('corpus/lessons/round-55.md', 138, 'S354', 'html-entity'), ('corpus/lessons/round-55.md', 140, 'S356', 'html-entity'), ('corpus/lessons/round-55.md', 141, 'S357', 'html-entity')] extra=[]
NOFALSE PASS stray=[]
EXIT FAIL round55=0 fixture=0
DECODE FAIL missing=[('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'truncated-grounds'), ('reports/round-56/fixtures/lessons/entities.md', 9, 'S952', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 11, 'S954', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'words=26')] extra=[]
KEEP PASS changed=[]
BADUTF8 FAIL exit=1 stderr_first='Traceback (most recent call last):' traceback=True
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 27/27 pass
exit 1
# role: O counting; expected pre-landing: exit 1: ENTITY FAIL (count=0), EXIT FAIL (round55=0 fixture=0), DECODE FAIL (missing all ten; moved_exit=0), BADUTF8 FAIL (exit=1, Traceback); NOFALSE, KEEP, FORMAT, SELFTEST PASS
$ python3 -B reports/round-56/accept-o.py
ENTITY FAIL count=0 missing=[('corpus/lessons/round-55.md', 72, 'S288', 'html-entity'), ('corpus/lessons/round-55.md', 82, 'S298', 'html-entity'), ('corpus/lessons/round-55.md', 88, 'S304', 'html-entity'), ('corpus/lessons/round-55.md', 89, 'S305', 'html-entity'), ('corpus/lessons/round-55.md', 93, 'S309', 'html-entity'), ('corpus/lessons/round-55.md', 96, 'S312', 'html-entity'), ('corpus/lessons/round-55.md', 110, 'S326', 'html-entity'), ('corpus/lessons/round-55.md', 113, 'S329', 'html-entity'), ('corpus/lessons/round-55.md', 125, 'S341', 'html-entity'), ('corpus/lessons/round-55.md', 127, 'S343', 'html-entity'), ('corpus/lessons/round-55.md', 131, 'S347', 'html-entity'), ('corpus/lessons/round-55.md', 132, 'S348', 'html-entity'), ('corpus/lessons/round-55.md', 134, 'S350', 'html-entity'), ('corpus/lessons/round-55.md', 138, 'S354', 'html-entity'), ('corpus/lessons/round-55.md', 140, 'S356', 'html-entity'), ('corpus/lessons/round-55.md', 141, 'S357', 'html-entity')] extra=[]
NOFALSE PASS stray=[]
EXIT FAIL round55=0 fixture=0
DECODE FAIL missing=[('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 8, 'S951', 'truncated-grounds'), ('reports/round-56/fixtures/lessons/entities.md', 9, 'S952', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 11, 'S954', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'html-entity'), ('reports/round-56/fixtures/lessons/entities.md', 12, 'S955', 'words=26')] extra=[]
KEEP PASS changed=[]
BADUTF8 FAIL exit=1 stderr_first='Traceback (most recent call last):' traceback=True
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 27/27 pass
exit 1
# role: O acceptance; expected pre-landing: fails before landing (exit 1), printing the before value; passes at all eight legs PASS (exit 0)
$ python3 -B tools/check-claim-separability.py reports/round-56/separability-manifest.json
SEPARABILITY_INPUT_ERROR cannot read manifest 'reports/round-56/separability-manifest.json': No such file or directory
exit 2
# role: separability; expected pre-landing: exit 2 before landing: SEPARABILITY_INPUT_ERROR naming the absent C land; checker stops at its first absent land, so later legs are unevaluated
$ python3 -B reports/round-56/claims-agree.py
AGREE_INPUT_ERROR [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/kotodama-r56-measure-052f145c-f7jsk68x/reports/round-56/claims.json'
exit 2
```

All six `$` commands above ran with `cwd=clone` (confirmed from `dry-run.py` line 83 and the printed clone path). Their command exit statuses are recorded in output; the runner's own exit status was 0.

## Lane status, evidence, and blockers

- Lane `git status --porcelain` before and after was identical:

```text
?? .ufo/waves/round-56/build-dispatch.json
?? .ufo/waves/round-56/build-sent-payload.json
?? .ufo/waves/round-56/build-spec.json
?? .ufo/waves/round-56/build/
?? .ufo/waves/round-56/gen-build-spec.py
```

- No lane file was modified. All test copies, generated clones, outputs, and this report are under this seat's scratch directory. No tools were installed.
- Blocker: the requested revision `052f145` predates declaration commit `b4b7db9`; under the proposed one-line change, separability and agreement still correctly report missing inputs at `052f145`. For an expected pre-landing receipt containing the full declaration and manifest, use the declaration commit. The b4b7db9 run above recorded C and O pre-landing failures, separability exit 2 for the absent C land, and agreement exit 0.
- The requested report destination `.ufo/waves/round-56/build/ExecReceiptRevision.md` is outside the permitted write scope. This report is retained at `/fast/scratch/hyaku/kotodama-r56/KotodamaR56.ExecReceiptRevision/ExecReceiptRevision.md`; the final response supplies the same findings to the main agent.
