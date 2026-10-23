# CtlOOrderErr — Round 62 wave 1 pre-data mutation controls
## Scope and axes
- Operability: ORDER (argument order and multiplicity) and ERR (error exit status, UTF-8 traceback suppression, passes lower bound). Calibration: positive baselines and exact restoration.
- Read the round-62 claims, the round-61 verifier spot-check section 7, Godspeed and operator rules before probing. No lane implementation or counter was edited. This report is the only lane write. No tools installed or updated.
- Revision: `f0173481047a93c46798f90b68d71d4f169d2642`. Clone: `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`.
- Frozen counter: `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py`; SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`. It was unchanged in every run. Predicate: `ACCEPT-O-62: every leg above prints PASS.`
- Independent honest calibration tool: `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/honest-control.py`, SHA-256 `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d`. It names none of the forbidden counter/lane strings.
- Each case lived under `clone/control-cases/<case>/tools/reopen-row.py`; the frozen counter was invoked from the clone with its documented `--root` pointing to that isolated case root. Each invocation used the same detector, with its own runtime-random local fixture. The seven independent cases ran concurrently in each of three joined, foreground stages: pristine, mutant, restored.
- All counter processes were capped by `timeout 300`, with a 330-second parent wait bound; tool diagnostics used `timeout 10` and a 15-second parent bound. `TMPDIR=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/tmp` and `PYTHONDONTWRITEBYTECODE=1` kept runtime files in scratch. Counter process groups were killed/reaped after each run. No background jobs or subagents were dispatched.

## Results
| Case | Expected detector | Actual failing legs | Mutant verdict |
|---|---|---|---|
| sorted | ORDER | ORDER, PRIV | KILLED |
| reversed | ORDER | ORDER, PRIV | KILLED |
| deduplicated | ORDER | none | SURVIVED |
| twice | ORDER | GEN, ORDER, PRIV, DEFAULT | KILLED |
| bad-input-exit1 | ERR | ERR | KILLED |
| badutf8-traceback | ERR | ERR | KILLED |
| passes0-as1 | ERR | ERR | KILLED |

All seven pristine and all seven restored runs passed. Six mutants were killed; deduplication survived. No baseline failure was counted as a kill. All 21 full counter outputs and exit codes are reproduced below.

### Coverage finding and smallest stopper
`CONTROL-MET CtlOOrderErr/deduplicated fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/deduplicated/tools/reopen-row.py`: one-line de-duplication skips the required repeated output for a repeated ID yet passes the frozen counter. The supplemental bounded call with `S3333 S1111 S2222 S1111` emitted only three ROW lines and still summarized `REOPEN: 0/4 located`; pristine/restored emitted four. The counter creates all argument IDs through `fresh_id()`, so its ORDER leg never exercises repeated arguments.

Smallest counter change that would stop this control: add one separate duplicate-ID call (for example an existing NOROW ID twice, `--passes 1 --gap 0`) and include in ORDER the exact parsed ID list including multiplicity, two NO_ROW/0 results, summary `REOPEN: 0/2 located`, exit 1. Do not simply append duplicates to GEN: its current by-ID comparison assumes one output per distinct ID. This is a detection recommendation, not a contract change; no counter was modified.
`NONE-MET CtlOOrderErr/sorted fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/sorted/tools/reopen-row.py`: frozen ORDER,PRIV already stops this defect; no counter change required.
`NONE-MET CtlOOrderErr/reversed fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/reversed/tools/reopen-row.py`: frozen ORDER,PRIV already stops this defect; no counter change required.
`NONE-MET CtlOOrderErr/twice fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/twice/tools/reopen-row.py`: frozen GEN,ORDER,PRIV,DEFAULT already stops this defect; no counter change required.
`NONE-MET CtlOOrderErr/bad-input-exit1 fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/bad-input-exit1/tools/reopen-row.py`: frozen ERR already stops this defect; no counter change required.
`NONE-MET CtlOOrderErr/badutf8-traceback fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/badutf8-traceback/tools/reopen-row.py`: frozen ERR already stops this defect; no counter change required.
`NONE-MET CtlOOrderErr/passes0-as1 fixture=/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/mutants/passes0-as1/tools/reopen-row.py`: frozen ERR already stops this defect; no counter change required.

## One-line mutations and hashes
Every working case began and ended with exact bytes SHA-256 `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d`. The retained mutants below are separate evidence snapshots, not the restored working copies.

| Case | Before SHA-256 | Mutant SHA-256 | Restored SHA-256 |
|---|---|---|---|
| sorted | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `392ccfab35c8010ba06760d005340e248a4eaf864989bb6b6472328be98e0c26` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |
| reversed | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `adb89bad6e1a975623f3d5f2a4bcc93fc812ab4e90b7856a5066cd7f576b42e1` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |
| deduplicated | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `e7062f54d093c193151dcde590c1377047146397c66741e5a979025bf8878c5f` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |
| twice | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `e4de471928ec497ca8d281d6101d98de38a61c01b12849dfe1fb64aed195ff1c` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |
| bad-input-exit1 | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `49b2344c477cf9869bc76899096b967e7f7898ae37a853ee521a04ad292f4407` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |
| badutf8-traceback | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `b92c61af500214ad621cbff53e5e9c1a65bd3bc50e95f242352c901cab18551a` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |
| passes0-as1 | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` | `ed9e31129a6faeec8f3ae8d05e2d41c7711489e8a20661ea41ede90cbaf45b69` | `d892ab7264e3b5407de0543d9e2ff0918ece5a7f883d2c1adf33dfab14eb829d` |

### sorted

```diff
--- honest-control.py
+++ sorted/tools/reopen-row.py
@@ -179,7 +179,7 @@
         if cells and re.fullmatch(r"S\d{3,}", cells[0]):
             registry[cells[0]] = cells
     results = [reopen(sid, registry, passes, args.gap, args.allow_private) for sid in args.ids]
-    for sid, verdict, attempts, url in results:
+    for sid, verdict, attempts, url in sorted(results):
         print(f"ROW {sid} {verdict} attempts={attempts} url={url}")
     located = sum(row[1] == "LOCATED" for row in results)
     print(f"REOPEN: {located}/{len(results)} located")
```

### reversed

```diff
--- honest-control.py
+++ reversed/tools/reopen-row.py
@@ -179,7 +179,7 @@
         if cells and re.fullmatch(r"S\d{3,}", cells[0]):
             registry[cells[0]] = cells
     results = [reopen(sid, registry, passes, args.gap, args.allow_private) for sid in args.ids]
-    for sid, verdict, attempts, url in results:
+    for sid, verdict, attempts, url in reversed(results):
         print(f"ROW {sid} {verdict} attempts={attempts} url={url}")
     located = sum(row[1] == "LOCATED" for row in results)
     print(f"REOPEN: {located}/{len(results)} located")
```

### deduplicated

```diff
--- honest-control.py
+++ deduplicated/tools/reopen-row.py
@@ -179,7 +179,7 @@
         if cells and re.fullmatch(r"S\d{3,}", cells[0]):
             registry[cells[0]] = cells
     results = [reopen(sid, registry, passes, args.gap, args.allow_private) for sid in args.ids]
-    for sid, verdict, attempts, url in results:
+    for sid, verdict, attempts, url in {row[0]: row for row in results}.values():
         print(f"ROW {sid} {verdict} attempts={attempts} url={url}")
     located = sum(row[1] == "LOCATED" for row in results)
     print(f"REOPEN: {located}/{len(results)} located")
```

### twice

```diff
--- honest-control.py
+++ twice/tools/reopen-row.py
@@ -179,7 +179,7 @@
         if cells and re.fullmatch(r"S\d{3,}", cells[0]):
             registry[cells[0]] = cells
     results = [reopen(sid, registry, passes, args.gap, args.allow_private) for sid in args.ids]
-    for sid, verdict, attempts, url in results:
+    for sid, verdict, attempts, url in results + results:
         print(f"ROW {sid} {verdict} attempts={attempts} url={url}")
     located = sum(row[1] == "LOCATED" for row in results)
     print(f"REOPEN: {located}/{len(results)} located")
```

### bad-input-exit1

```diff
--- honest-control.py
+++ bad-input-exit1/tools/reopen-row.py
@@ -191,4 +191,4 @@
         sys.exit(main())
     except InputError as error:
         print(f"REOPEN_ERROR {error}", file=sys.stderr)
-        sys.exit(2)
+        sys.exit(1)
```

### badutf8-traceback

```diff
--- honest-control.py
+++ badutf8-traceback/tools/reopen-row.py
@@ -171,7 +171,7 @@
         raise InputError("--gap must be a finite number >= 0")
     try:
         text = Path(args.registry).read_text(encoding="utf-8")
-    except (OSError, UnicodeError) as error:
+    except OSError as error:
         raise InputError(str(error)) from None
     registry = {}
     for line in text.splitlines():
```

### passes0-as1

```diff
--- honest-control.py
+++ passes0-as1/tools/reopen-row.py
@@ -164,7 +164,7 @@
     parser.add_argument("--allow-private", action="store_true")
     parser.add_argument("ids", nargs="+")
     args = parser.parse_args()
-    passes = args.passes
+    passes = args.passes or 1
     if passes < 1:
         raise InputError("--passes must be an integer >= 1")
     if not math.isfinite(args.gap) or args.gap < 0:
```

## Full frozen-counter receipts

Each JSON receipt, including command, cwd, full stdout/stderr, exit, wall time and hashes, is retained at `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/<case>-<phase>.json`; combined: `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/all-runs.json`. No counter PROBE copy was used.

### sorted-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/sorted
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3681', 'REFUSED', 0), ('S1793', 'REFUSED', 0), ('S1066', 'REFUSED', 0)]
DEFAULT PASS rows=[('S5108', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/sorted-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### sorted-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/sorted
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER FAIL printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV FAIL exit=1 rows=[('S4417', 'REFUSED', 0), ('S5070', 'REFUSED', 0), ('S7317', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6388', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```
stderr: empty.

`RECEIPT CtlOOrderErr/sorted-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ORDER,PRIV`

### sorted-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/sorted
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9848', 'REFUSED', 0), ('S8954', 'REFUSED', 0), ('S2245', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6165', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/sorted-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### reversed-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/reversed
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5752', 'REFUSED', 0), ('S7247', 'REFUSED', 0), ('S5244', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1690', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/reversed-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### reversed-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/reversed
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER FAIL printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV FAIL exit=1 rows=[('S6802', 'REFUSED', 0), ('S6584', 'REFUSED', 0), ('S5890', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7185', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```
stderr: empty.

`RECEIPT CtlOOrderErr/reversed-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ORDER,PRIV`

### reversed-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/reversed
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9142', 'REFUSED', 0), ('S4253', 'REFUSED', 0), ('S4324', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3037', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/reversed-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### deduplicated-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/deduplicated
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4702', 'REFUSED', 0), ('S7680', 'REFUSED', 0), ('S2029', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9935', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/deduplicated-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### deduplicated-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/deduplicated
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7209', 'REFUSED', 0), ('S3554', 'REFUSED', 0), ('S1787', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4050', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/deduplicated-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### deduplicated-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/deduplicated
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9482', 'REFUSED', 0), ('S4284', 'REFUSED', 0), ('S4818', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1251', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/deduplicated-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### twice-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/twice
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2564', 'REFUSED', 0), ('S4753', 'REFUSED', 0), ('S6956', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2498', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/twice-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### twice-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/twice
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=37 ["SHORT:S7858:want=NO_QUOTE/0:got=[('NO_QUOTE', 0), ('NO_QUOTE', 0)]", "GONE:S2849:want=UNREACHABLE/1:got=[('UNREACHABLE', 1), ('UNREACHABLE', 1)]", "BODY_SPLIT:S7178:want=LOCATED/1:got=[('LOCATED', 1), ('LOCATED', 1)]", "BODY:S1523:want=LOCATED/1:got=[('LOCATED', 1), ('LOCATED', 1)]", "DEAD:S6025:want=UNREACHABLE/9:got=[('UNREACHABLE', 9), ('UNREACHABLE', 9)]", "SHORT:S4374:want=NO_QUOTE/0:got=[('NO_QUOTE', 0), ('NO_QUOTE', 0)]"] summary_ok=True exit=1
ORDER FAIL printed=74 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV FAIL exit=1 rows=[('S9293', 'REFUSED', 0), ('S4435', 'REFUSED', 0), ('S8229', 'REFUSED', 0), ('S9293', 'REFUSED', 0), ('S4435', 'REFUSED', 0), ('S8229', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S7315', 'UNREACHABLE', 9), ('S7315', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```
stderr: empty.

`RECEIPT CtlOOrderErr/twice-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,ORDER,PRIV,DEFAULT`

### twice-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/twice
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5760', 'REFUSED', 0), ('S3004', 'REFUSED', 0), ('S6491', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9994', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/twice-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### bad-input-exit1-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/bad-input-exit1
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6095', 'REFUSED', 0), ('S2755', 'REFUSED', 0), ('S8443', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7826', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/bad-input-exit1-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### bad-input-exit1-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/bad-input-exit1
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1091', 'REFUSED', 0), ('S6541', 'REFUSED', 0), ('S6682', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7769', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR FAIL bad=['no-id:exit=1', 'missing:exit=1', 'badutf8:exit=1', 'passes0:exit=1', 'gapx:exit=1']
ACCEPT-O-62: FAIL
exit=1
```
stderr: empty.

`RECEIPT CtlOOrderErr/bad-input-exit1-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ERR`

### bad-input-exit1-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/bad-input-exit1
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5208', 'REFUSED', 0), ('S3551', 'REFUSED', 0), ('S4101', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9057', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/bad-input-exit1-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### badutf8-traceback-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/badutf8-traceback
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4492', 'REFUSED', 0), ('S2005', 'REFUSED', 0), ('S6795', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4973', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/badutf8-traceback-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### badutf8-traceback-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/badutf8-traceback
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2298', 'REFUSED', 0), ('S7838', 'REFUSED', 0), ('S4628', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6162', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR FAIL bad=['badutf8:exit=1']
ACCEPT-O-62: FAIL
exit=1
```
stderr: empty.

`RECEIPT CtlOOrderErr/badutf8-traceback-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ERR`

### badutf8-traceback-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/badutf8-traceback
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5403', 'REFUSED', 0), ('S2771', 'REFUSED', 0), ('S7988', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8463', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/badutf8-traceback-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### passes0-as1-pristine

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/passes0-as1
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1843', 'REFUSED', 0), ('S8822', 'REFUSED', 0), ('S8485', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3947', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/passes0-as1-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

### passes0-as1-mutant

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/passes0-as1
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7512', 'REFUSED', 0), ('S5093', 'REFUSED', 0), ('S5314', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8598', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR FAIL bad=['passes0:exit=1']
ACCEPT-O-62: FAIL
exit=1
```
stderr: empty.

`RECEIPT CtlOOrderErr/passes0-as1-mutant counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ERR`

### passes0-as1-restored

Command (cwd `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone`):

```text
timeout 300 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/reports/round-62/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/passes0-as1
```

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3849', 'REFUSED', 0), ('S6908', 'REFUSED', 0), ('S6319', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2343', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```
stderr: empty.

`RECEIPT CtlOOrderErr/passes0-as1-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none`

## Full supplemental diagnostic output

These are direct bounded tool calls, not frozen-counter scores. Fixtures: `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md` and `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/invalid-utf8.md`. JSON: `/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/diagnostics.json`.

### sorted/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### sorted/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S1111 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S3333 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### reversed/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### reversed/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S3333 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### deduplicated/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### deduplicated/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### twice/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### twice/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### bad-input-exit1/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR the following arguments are required: ids
```
`exit=2`

### bad-input-exit1/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR the following arguments are required: ids
```
`exit=1`

### badutf8-traceback/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/invalid-utf8.md S1234`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR 'utf-8' codec can't decode byte 0xff in position 10: invalid start byte
```
`exit=2`

### badutf8-traceback/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/invalid-utf8.md S1234`

stdout:
```text
```
stderr:
```text
Traceback (most recent call last):
  File "/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/badutf8-traceback/tools/reopen-row.py", line 191, in <module>
    sys.exit(main())
             ~~~~^^
  File "/fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/clone/control-cases/badutf8-traceback/tools/reopen-row.py", line 173, in main
    text = Path(args.registry).read_text(encoding="utf-8")
  File "/usr/lib/python3.14/pathlib/__init__.py", line 788, in read_text
    return f.read()
           ~~~~~~^^
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 10: invalid start byte
```
`exit=1`

### passes0-as1/pristine

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md --passes 0 S1111`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR --passes must be an integer >= 1
```
`exit=2`

### passes0-as1/mutant

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md --passes 0 S1111`

stdout:
```text
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/1 located
```
stderr:
```text
```
`exit=1`

### sorted/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### reversed/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### deduplicated/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### twice/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md S3333 S1111 S2222 S1111`

stdout:
```text
ROW S3333 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
ROW S2222 NO_ROW attempts=0 url=-
ROW S1111 NO_ROW attempts=0 url=-
REOPEN: 0/4 located
```
stderr:
```text
```
`exit=1`

### bad-input-exit1/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR the following arguments are required: ids
```
`exit=2`

### badutf8-traceback/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/invalid-utf8.md S1234`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR 'utf-8' codec can't decode byte 0xff in position 10: invalid start byte
```
`exit=2`

### passes0-as1/restored

Arguments: `--registry /fast/scratch/hyaku/kotodama-r62/CtlOOrderErr/repeated-id.md --passes 0 S1111`

stdout:
```text
```
stderr:
```text
REOPEN_ERROR --passes must be an integer >= 1
```
`exit=2`

## Restoration and process evidence
- All seven case tools were restored in a `finally` block immediately after mutant scoring, even if a detector had failed. Exact byte equality against the saved original was observed for every case, and all seven restored frozen-detector runs passed.
- The main scratch clone tool and saved honest copy were never mutated. The counter hash after all runs remained `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`.
- Every started subprocess returned and was reaped; its isolated process group received cleanup, with no persistent jobs or services. The local HTTP servers belonged to the terminated counters.
- Installs/updates: none. External source fetches: none. Lane/fleet source writes: none; only this requested report is written in the lane.
