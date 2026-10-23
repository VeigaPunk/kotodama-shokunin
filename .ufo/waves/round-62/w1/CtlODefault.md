# Claim O default-schedule controls — CtlODefault
## Scope and axes
Operability controls only: contract discrimination, real-time retry placement, and exact restoration. No lane implementation was judged or integrated. An independent stand-in was created only in isolated scratch clones at the assigned frozen revision.
- Revision: `f0173481047a93c46798f90b68d71d4f169d2642`.
- Frozen counter: `reports/round-62/accept-o.py`, SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`. It was never modified, including in a probe copy.
- Scratch root: `/fast/scratch/hyaku/kotodama-r62/CtlODefault/`.
- Pristine fixture: `/fast/scratch/hyaku/kotodama-r62/CtlODefault/clone/tools/reopen-row.py`, SHA-256 `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4`.
- All six controls ran concurrently in separate clones; real sleeps were not mocked or accelerated. Each counter was invoked as `timeout 900 python3 -B reports/round-62/accept-o.py` with its clone as cwd, `TMPDIR` under its scratch case, bytecode disabled, and GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset. Every spawned command completed; no background jobs or child process trees remain.
- No installs, network source research, lane code changes, or counter changes. The only authored lane file is this write-once report. Authored fixtures and evidence files are each below 5 MB.
## Result
**The 100–600 s DEFAULT window plus nine reported attempts and nine observed HTTP hits do not pin the contract.** Default gap=200 survives at 430 s; moving the 60 s delay from between passes to between attempts survives at 360 s. Both receive full frozen ACCEPT-O-62: PASS, not merely a passing DEFAULT leg. Four other controls are killed only by DEFAULT. All pristine and restored runs pass.
| Mutant | Expected detector | DEFAULT output | Frozen exit | Mutation verdict |
|---|---|---|---|---|
| passes1 | DEFAULT FAIL | `DEFAULT FAIL rows=[('S3761', 'UNREACHABLE', 3)] wall=10s hits=3 exit=1` | 1 | killed |
| gap0 | DEFAULT FAIL | `DEFAULT FAIL rows=[('S2106', 'UNREACHABLE', 9)] wall=0s hits=9 exit=1` | 1 | killed |
| gap5 | DEFAULT FAIL | `DEFAULT FAIL rows=[('S1369', 'UNREACHABLE', 9)] wall=40s hits=9 exit=1` | 1 | killed |
| gap200 | DEFAULT FAIL | `DEFAULT PASS rows=[('S3576', 'UNREACHABLE', 9)] wall=430s hits=9 exit=1` | 0 | survived |
| sleep150 | DEFAULT FAIL | `DEFAULT FAIL rows=[('S5929', 'UNREACHABLE', 1)] wall=150s hits=1 exit=1` | 1 | killed |
| attemptgap60 | DEFAULT FAIL | `DEFAULT PASS rows=[('S9923', 'UNREACHABLE', 9)] wall=360s hits=9 exit=1` | 0 | survived |

`passes1` changes only the default pass count. `gap0`, `gap5`, and `gap200` each change only the default gap. `sleep150` adds a transient-positive-gap branch that sleeps 150 s and returns after the first request, without retrying; explicit --gap 0 retains the pristine behavior, so this isolates DEFAULT. `attemptgap60` removes the inter-pass wait and uses the configured gap, rather than min(gap, 5), between retry attempts. Neither survivor fakes attempt counts or fixture classes.

[INFERENCE] With negligible local request overhead and gap >=5, the normal nine-request schedule lasts approximately `2*gap + 30` seconds. Thus the frozen window admits gaps roughly 35–285 s, including 200 s; it is not a test of default gap=60. The misplaced six 60 s retry waits likewise fit the window.

## Per-item control verdicts
NONE-MET CtlODefault/passes1 fixture=/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/passes1.py; frozen=FAIL; stopped-by=DEFAULT; no counter change needed to stop this fixture.

NONE-MET CtlODefault/gap0 fixture=/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/gap0.py; frozen=FAIL; stopped-by=DEFAULT; no counter change needed to stop this fixture.

NONE-MET CtlODefault/gap5 fixture=/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/gap5.py; frozen=FAIL; stopped-by=DEFAULT; no counter change needed to stop this fixture.

CONTROL-MET CtlODefault/gap200 fixture=/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/gap200.py; frozen=PASS; violates default scheduling. Smallest counter edit that would stop this observed fixture: change DEFAULT wall upper bound 600 to 200 ([INFERENCE], proposed only, not run).

NONE-MET CtlODefault/sleep150 fixture=/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/sleep150.py; frozen=FAIL; stopped-by=DEFAULT; no counter change needed to stop this fixture.

CONTROL-MET CtlODefault/attemptgap60 fixture=/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/attemptgap60.py; frozen=PASS; violates default scheduling. Smallest counter edit that would stop this observed fixture: change DEFAULT wall upper bound 600 to 200 ([INFERENCE], proposed only, not run).

A narrower total-time window would kill these two observed survivors but would still not establish where the waits occurred. The contract-preserving detector improvement is to record request timestamps and check the DEAD row's eight successive gaps against the expected pattern approximately `5,5,60,5,5,60,5,5` seconds, with a declared scheduling tolerance, alongside existing nine-hit and verdict checks. This is a coverage finding, not a contract revision; no counter alteration was performed.

## Mutation and restoration evidence
Each case was scored pristine, then mutated, then exactly restored with the same frozen full detector. The table records actual SHA-256 values. Every restored file also compared byte-for-byte equal to the pristine fixture; every restored counter retained its frozen hash. No baseline failure or inconclusive case occurred.

| Case | Pristine SHA-256 | Mutant SHA-256 | Restored SHA-256 | Exact bytes |
|---|---|---|---|---|
| passes1 | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | `3825f65da4bc499b82155662ed995551561d8395e31634b38173c08914aa6b4f` | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | True |
| gap0 | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | `bcd87d9cb23b098fbf27a3811c4aaae9dd1492f28f043f63597b28cecba54dff` | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | True |
| gap5 | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | `411461999ce56a63a3035c33fcd9ae6c5387dffe5467b4c5bf46c9d7bfd960a6` | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | True |
| gap200 | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | `c14f57a81b9853e992480ccf742898bccbf692fd3ce6fdd06a8f2d1ebc95c718` | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | True |
| sleep150 | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | `0e17532beb8e19e7195cdb241cf4282207347f1027449ff6ed22f09e7bf44f20` | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | True |
| attemptgap60 | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | `0fed2f310dcdc086852e145a98049057f65d41d62a0bed7a5314b4734c8b43cc` | `5ac5570b7e176c2104581299ce0807e28116a81a0d2837b6df29a172fa1cb9a4` | True |

Retained mutant bytes are in `/fast/scratch/hyaku/kotodama-r62/CtlODefault/fixtures/{passes1,gap0,gap5,gap200,sleep150,attemptgap60}.py`; the tested `*/clone/tools/reopen-row.py` files are restored. Exact fixture diffs (not counter diffs): `/fast/scratch/hyaku/kotodama-r62/CtlODefault/mutations.diff`. Raw complete evidence: `/fast/scratch/hyaku/kotodama-r62/CtlODefault/all-runs.json`, with separate `pristine-runs.json`, `mutant-runs.json`, and `restored-runs.json`.

## Exact mutant diffs

```diff
--- pristine/reopen-row.py
+++ passes1/reopen-row.py
@@ -146,7 +146,7 @@
 def main():
     parser = Parser()
     parser.add_argument("--registry", default="corpus/SOURCES.md")
-    parser.add_argument("--passes", type=int, default=3)
+    parser.add_argument("--passes", type=int, default=1)
     parser.add_argument("--gap", type=float, default=60)
     parser.add_argument("--allow-private", action="store_true")
     parser.add_argument("ids", nargs="*")

--- pristine/reopen-row.py
+++ gap0/reopen-row.py
@@ -147,7 +147,7 @@
     parser = Parser()
     parser.add_argument("--registry", default="corpus/SOURCES.md")
     parser.add_argument("--passes", type=int, default=3)
-    parser.add_argument("--gap", type=float, default=60)
+    parser.add_argument("--gap", type=float, default=0)
     parser.add_argument("--allow-private", action="store_true")
     parser.add_argument("ids", nargs="*")
     try:

--- pristine/reopen-row.py
+++ gap5/reopen-row.py
@@ -147,7 +147,7 @@
     parser = Parser()
     parser.add_argument("--registry", default="corpus/SOURCES.md")
     parser.add_argument("--passes", type=int, default=3)
-    parser.add_argument("--gap", type=float, default=60)
+    parser.add_argument("--gap", type=float, default=5)
     parser.add_argument("--allow-private", action="store_true")
     parser.add_argument("ids", nargs="*")
     try:

--- pristine/reopen-row.py
+++ gap200/reopen-row.py
@@ -147,7 +147,7 @@
     parser = Parser()
     parser.add_argument("--registry", default="corpus/SOURCES.md")
     parser.add_argument("--passes", type=int, default=3)
-    parser.add_argument("--gap", type=float, default=60)
+    parser.add_argument("--gap", type=float, default=200)
     parser.add_argument("--allow-private", action="store_true")
     parser.add_argument("ids", nargs="*")
     try:

--- pristine/reopen-row.py
+++ sleep150/reopen-row.py
@@ -123,6 +123,9 @@
             for attempt in range(3):
                 status, body, caption = fetch(url)
                 attempts += 1
+                if status == "TRANSIENT" and args.gap:
+                    time.sleep(150)
+                    return "UNREACHABLE", attempts, "-"
                 if status == "TRANSIENT" and attempt < 2:
                     time.sleep(min(args.gap, 5))
                     continue

--- pristine/reopen-row.py
+++ attemptgap60/reopen-row.py
@@ -124,7 +124,7 @@
                 status, body, caption = fetch(url)
                 attempts += 1
                 if status == "TRANSIENT" and attempt < 2:
-                    time.sleep(min(args.gap, 5))
+                    time.sleep(args.gap)
                     continue
                 break
             if status == "TRANSIENT":
@@ -139,7 +139,6 @@
             best, best_url = current, current_url
         if best == "LOCATED" or not transient or pass_index + 1 == args.passes:
             break
-        time.sleep(args.gap)
     return best, attempts, best_url
 
 
```

## Full frozen-counter receipts
Every stdout below is complete and untrimmed. All stderr was empty. The trailing `exit=` is the captured process exit code, equivalent to the required shell echo. Each run used an independently generated offline local fixture, as the frozen counter specifies.

### baseline-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2110', 'REFUSED', 0), ('S2286', 'REFUSED', 0), ('S4102', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8969', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/baseline-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### passes1-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5780', 'REFUSED', 0), ('S6031', 'REFUSED', 0), ('S3109', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4098', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/passes1-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### gap0-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2141', 'REFUSED', 0), ('S4917', 'REFUSED', 0), ('S7108', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8513', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap0-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### gap5-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6356', 'REFUSED', 0), ('S2292', 'REFUSED', 0), ('S9501', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1901', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap5-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### gap200-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6711', 'REFUSED', 0), ('S3153', 'REFUSED', 0), ('S5049', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8463', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap200-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### sleep150-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9118', 'REFUSED', 0), ('S8506', 'REFUSED', 0), ('S3902', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7904', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/sleep150-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### attemptgap60-pristine

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4976', 'REFUSED', 0), ('S6588', 'REFUSED', 0), ('S5355', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1060', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/attemptgap60-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### passes1-mutated

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1389', 'REFUSED', 0), ('S5027', 'REFUSED', 0), ('S2358', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S3761', 'UNREACHABLE', 3)] wall=10s hits=3 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODefault/passes1-mutated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=DEFAULT

### gap0-mutated

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7137', 'REFUSED', 0), ('S9848', 'REFUSED', 0), ('S7610', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S2106', 'UNREACHABLE', 9)] wall=0s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODefault/gap0-mutated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=DEFAULT

### gap5-mutated

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2071', 'REFUSED', 0), ('S2767', 'REFUSED', 0), ('S8394', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S1369', 'UNREACHABLE', 9)] wall=40s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODefault/gap5-mutated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=DEFAULT

### gap200-mutated

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3749', 'REFUSED', 0), ('S4530', 'REFUSED', 0), ('S5838', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3576', 'UNREACHABLE', 9)] wall=430s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap200-mutated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### sleep150-mutated

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5749', 'REFUSED', 0), ('S5473', 'REFUSED', 0), ('S8173', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S5929', 'UNREACHABLE', 1)] wall=150s hits=1 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODefault/sleep150-mutated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=DEFAULT

### attemptgap60-mutated

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4716', 'REFUSED', 0), ('S3784', 'REFUSED', 0), ('S2211', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9923', 'UNREACHABLE', 9)] wall=360s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/attemptgap60-mutated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### passes1-restored

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5870', 'REFUSED', 0), ('S2022', 'REFUSED', 0), ('S5084', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7128', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/passes1-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### gap0-restored

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5105', 'REFUSED', 0), ('S5893', 'REFUSED', 0), ('S4568', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4337', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap0-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### gap5-restored

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6687', 'REFUSED', 0), ('S2385', 'REFUSED', 0), ('S5723', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2566', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap5-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### gap200-restored

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8627', 'REFUSED', 0), ('S9932', 'REFUSED', 0), ('S7871', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4931', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/gap200-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### sleep150-restored

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1490', 'REFUSED', 0), ('S2007', 'REFUSED', 0), ('S7068', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4004', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/sleep150-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### attemptgap60-restored

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5139', 'REFUSED', 0), ('S3720', 'REFUSED', 0), ('S6724', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6611', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlODefault/attemptgap60-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
