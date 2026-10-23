# CtlONoRetry — claim O no-retry controls (pre-data)

Seat: `KotodamaR62.CtlONoRetry`. Axis: **operability** (detector sensitivity of the frozen
O counter to a re-opener that under-retries). Probe axes: frozen-counter integrity, exact
restoration, cheap bounded execution, receipt completeness.

## Scope and detector

Read `reports/round-62/claims.json` (claims D and O, `controls_required_before_data.O`),
the frozen counter's own contract docstring (`reports/round-62/accept-o.py`, `Tool
contract` paragraph), and `skill://godspeed` plus the operator's tooling rules before
probing.

All runs were made in the isolated clone
`/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone`, cloned from the lane and
checked out at `f0173481047a93c46798f90b68d71d4f169d2642` with `GIT_DIR`, `GIT_WORK_TREE`
and `GIT_INDEX_FILE` unset for clone and checkout. The clone HEAD is that revision.

The frozen counter was **never edited**. Its SHA-256 before the first run and after the
final restoration run was identical:

`bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`

The detector command was identical in every scored run (cwd = clone root, no `--root`
override, so the tool is read from the clone's own `tools/reopen-row.py` slot):

```sh
timeout 900 env TMPDIR=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/tmp_<case> \
  PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-62/accept-o.py; echo exit=$?
```

Every process was bounded by `timeout 900`; no background job, service, or long-lived
process of mine was started or left running (`pgrep -af CtlONoRetry` is empty at return).
The counter's own local HTTP fixture and its temporary tool copies stayed under this
seat's scratch tree; **no external fetch was made and no live page was consulted**.
Installs/updates: **none** (no tool was needed for this task).

Frozen predicate: **ACCEPT-O-62: every leg above prints PASS.**

## Mutation base and positive calibration

The mutation base is an independent implementation of the frozen tool contract written
from the counter's `Tool contract` paragraph alone, retained at
`/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/base/reopen-row.py`
(SHA-256 `052628ffd0599455929d5c27bd4f498dac8fdaf233b1f2ae8a4f8044b15a1164`; identical
copy at `honest/tools/reopen-row.py`). It is **not** the lane's tool: the lane slot
`tools/reopen-row.py` was absent for the whole of this seat's work (`ls` on the lane
returned "No such file or directory"), so this base exists only inside the scratch clone
as the parent of the mutations and as the positive-calibration reference.

**Positive calibration: the frozen counter accepts the honest base — every leg PASS,
`ACCEPT-O-62: PASS`, exit 0.** The counter is therefore not vacuous, and every mutant
failure below is attributable to the mutated property rather than to a broken base.

## Results

| Case | Mutated property | Frozen verdict | Legs that failed |
|---|---|---|---|
| honest | none (positive calibration) | PASS, exit 0 | none |
| A | one attempt per URL **and** one pass (`MAX_ATTEMPTS 3→1`, `range(passes)→range(1)`) | FAIL, exit 1 | GEN, BOUND, DEFAULT |
| B | 3 attempts per URL, **one pass** (`range(passes)→range(1)`) | FAIL, exit 1 | GEN, BOUND, DEFAULT |
| C | **no `min(gap,5)` wait between attempts** | **PASS, exit 0** | **none — SURVIVED** |
| D | diagnostic: no wait at all (C **and** the inter-pass gap) | FAIL, exit 1 | DEFAULT |
| E | diagnostic: inter-pass gap capped at `min(gap,5)` instead of `gap` | FAIL, exit 1 | DEFAULT |
| restore | tool slot absent (pristine) | FAIL, exit 1 | TOOL, INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR |

GEN and BOUND fail on exactly the transient/dead classes the assignment predicted for A
and B: `TRANSIENT2`, `TRANSIENT_PASS`, `DEAD`, `DEAD_PORT`, `DEAD_THEN_BODY2`.

### The surviving mutant (the finding of this seat)

**Mutant C removes the contract's `waiting min(gap, 5) s between attempts` clause and the
frozen counter accepts it: `ACCEPT-O-62: PASS`, exit 0, every leg PASS.**

The contract text is unconditional — *"it is retried up to 3 attempts per URL per pass,
waiting min(gap, 5) s between attempts"* — and the DEFAULT leg's docstring fixes the
expected composition of the default run as *"three passes, two 60 s gaps"*. The measured
wall times decompose exactly along those lines and pin the defect:

| Tool | DEFAULT wall | Composition | Counter verdict |
|---|---|---|---|
| honest | 150 s | 2 pass gaps × 60 s + 6 inter-attempt waits × 5 s | PASS |
| C (no inter-attempt wait) | **120 s** | 2 pass gaps × 60 s only | **PASS** |
| E (pass gap capped at 5 s) | 40 s | 6 × 5 s + 2 × 5 s | FAIL (floor 100 s) |
| D (no waits at all) | 0 s | — | FAIL (floor 100 s) |
| B (one pass) | 70 s | 1 pass gap 60 s + 2 waits 5 s | FAIL (also attempts 3 ≠ 9) |
| A (one attempt, one pass) | 60 s | 1 pass gap 60 s | FAIL (also attempts 1 ≠ 9) |

So the DEFAULT leg's floor of `100 <= wall <= 600` (counter line 370) has real teeth
against the inter-pass gap (D and E die) but leaves a **20 s blind window**: the
honest 150 s and the no-inter-attempt-wait 120 s both fall inside `[100, 600]`. The
`DEAD` fixture's `attempts=9` and `hits=9` are also identical for honest and C, because
C still makes all nine requests — it only removes the pause between them.

Smallest counter change that would stop mutant C: raise the DEFAULT leg's wall floor
from `100` to `130` seconds (`accept-o.py` line 370). That rejects C at 120 s and keeps
the honest 150 s passing, with 20 s of separation. A floor of `140` would also work and
leaves more headroom, at the cost of tightening against a slower honest implementation.
No counter revision was made by this seat.

**Revision-window note for the L1.** `claims.json` permits a counter revision "only
before the first run of that counter on the claimed object (O: `tools/reopen-row.py`)".
At the time of this seat's work the lane slot `tools/reopen-row.py` was absent, so that
window appeared open. Whether it is still open is the L1's call, not this seat's; this
report is evidence for it, and the floor change above is the smallest one available.

### Diagnostic cases D and E

D and E were run to locate the boundary of the DEFAULT leg rather than as claimed-work
skippers. D (every wait removed) fails DEFAULT at `wall=0s`; E (inter-pass gap capped at
`min(gap,5)` instead of `gap`) fails DEFAULT at `wall=40s`. Both confirm the leg does
discriminate the *inter-pass* gap; neither touches the inter-attempt wait, which is why
C survives. D and E also both show GEN/BOUND passing, because request *counts* are
unaffected by sleep removal — the only observable is time.

## Exact diffs (single-property, against the honest base)

Mutant A — one attempt per URL, one pass:

```diff
--- honest/tools/reopen-row.py
+++ ctlA/tools/reopen-row.py
@@ -30,7 +30,7 @@
 import urllib.request
 from html.parser import HTMLParser

-MAX_ATTEMPTS = 3
+MAX_ATTEMPTS = 1
 FETCH_TIMEOUT = 30
 URL_RE = re.compile(r"https?://[^\s|]+")
 ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
@@ -339,7 +339,7 @@
     best = None
     best_url = None
     total = 0
-    for index in range(passes):
+    for index in range(1):
         verdict, match_url, transient, attempts = run_pass(
             urls, quote_words, allow_private, gap)
         total += attempts
```

Mutant B — three attempts per URL, one pass:

```diff
--- honest/tools/reopen-row.py
+++ ctlB/tools/reopen-row.py
@@ -339,7 +339,7 @@
     best = None
     best_url = None
     total = 0
-    for index in range(passes):
+    for index in range(1):
         verdict, match_url, transient, attempts = run_pass(
             urls, quote_words, allow_private, gap)
         total += attempts
```

Mutant C — no `min(gap, 5)` wait between attempts (the survivor):

```diff
--- honest/tools/reopen-row.py
+++ ctlC/tools/reopen-row.py
@@ -305,7 +305,6 @@
             status, data, content_type = http_get(url)
             if transient_status(status):
                 if attempt < MAX_ATTEMPTS - 1:
-                    time.sleep(min(gap, 5))
                     continue
                 transient = True
                 break
```

Mutant D — diagnostic, no wait at all:

```diff
--- honest/tools/reopen-row.py
+++ ctlD/tools/reopen-row.py
@@ -305,7 +305,6 @@
             status, data, content_type = http_get(url)
             if transient_status(status):
                 if attempt < MAX_ATTEMPTS - 1:
-                    time.sleep(min(gap, 5))
                     continue
                 transient = True
                 break
@@ -349,7 +348,7 @@
         if verdict == "LOCATED" or not transient:
             break
         if index < passes - 1:
-            time.sleep(gap)
+            pass
     return best, total, best_url
```

Mutant E — diagnostic, inter-pass gap capped at `min(gap, 5)`:

```diff
--- honest/tools/reopen-row.py
+++ ctlE/tools/reopen-row.py
@@ -349,7 +349,7 @@
         if verdict == "LOCATED" or not transient:
             break
         if index < passes - 1:
-            time.sleep(gap)
+            time.sleep(min(gap, 5))
     return best, total, best_url
```

## Fixture hashes (retained under the scratch tree)

| Fixture | SHA-256 |
|---|---|
| `base/reopen-row.py` (== `honest/tools/reopen-row.py`) | `052628ffd0599455929d5c27bd4f498dac8fdaf233b1f2ae8a4f8044b15a1164` |
| `ctlA/tools/reopen-row.py` | `95e9f1b5eb15c3de981f6f7fa5f00257947afb308242980d9e59fecf286509d7` |
| `ctlB/tools/reopen-row.py` | `253917348121213519a68a31d7f6f41370e7450f1a4a7953de9b6f7ebc0fd14f` |
| `ctlC/tools/reopen-row.py` (survivor) | `d29b7533eefc251dff9949cbfb8688570e77ed23ee68b84e2dda1c13f33954c6` |
| `ctlD/tools/reopen-row.py` | `3d5fce1dff5674d0e15dbb7eea83eba2b877fa09776bc089acdf48ee2fd85d95` |
| `ctlE/tools/reopen-row.py` | `2a005f23f622cb6a7f1c22170f32c27808ef7fa52a63625e519f1c6747cdfc9b` |

Each hash was taken from the file actually installed in the clone slot for that case and
is reproduced in the run preamble below. Raw run logs are retained at
`/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/logs/`.

## Full run outputs and receipts

### honest — positive calibration (clone slot, no `--root`)

```text
=== CASE honest (canonical, clone slot, no --root)
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
052628ffd0599455929d5c27bd4f498dac8fdaf233b1f2ae8a4f8044b15a1164  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3508', 'REFUSED', 0), ('S7057', 'REFUSED', 0), ('S8376', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8004', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlONoRetry/honest counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

NONE-MET KotodamaR62.CtlONoRetry/honest fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/honest/tools/reopen-row.py smallest-counter-change=none-needed; the frozen predicate accepts a contract-complete implementation.

### A — one attempt per URL, one pass

```text
=== CASE caseA (clone slot)
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
95e9f1b5eb15c3de981f6f7fa5f00257947afb308242980d9e59fecf286509d7  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=9 ["DEAD:S5727:want=UNREACHABLE/9:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S3646:want=LOCATED/4:got=[('LOCATED', 2)]", "TRANSIENT2:S8962:want=LOCATED/3:got=[('UNREACHABLE', 1)]", "DEAD:S3115:want=UNREACHABLE/9:got=[('UNREACHABLE', 1)]", "TRANSIENT2:S8329:want=LOCATED/3:got=[('UNREACHABLE', 1)]", "TRANSIENT_PASS:S6175:want=LOCATED/4:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD:live:want=9:hits=1', 'DEAD_THEN_BODY2:live:want=3:hits=1', 'TRANSIENT2:live:want=3:hits=1', 'DEAD:live:want=9:hits=1', 'TRANSIENT2:live:want=3:hits=1', 'TRANSIENT_PASS:live:want=4:hits=1', 'TRANSIENT_PASS:live:want=4:hits=1', 'DEAD_THEN_BODY2:live:want=3:hits=1']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8493', 'REFUSED', 0), ('S4915', 'REFUSED', 0), ('S5431', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S2825', 'UNREACHABLE', 1)] wall=60s hits=1 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlONoRetry/caseA counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT

NONE-MET KotodamaR62.CtlONoRetry/caseA fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/ctlA/tools/reopen-row.py smallest-counter-change=none-needed; the frozen predicate rejects a re-opener that makes one attempt per URL in one pass (GEN/BOUND fail on the TRANSIENT*/DEAD* classes as predicted).

### B — three attempts per URL, one pass

```text
=== CASE caseB
counter: bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/reports/round-62/accept-o.py
253917348121213519a68a31d7f6f41370e7450f1a4a7953de9b6f7ebc0fd14f  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=5 ["DEAD:S2673:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]", "TRANSIENT_PASS:S2894:want=LOCATED/4:got=[('UNREACHABLE', 3)]", "DEAD:S3237:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]", "TRANSIENT_PASS:S3304:want=LOCATED/4:got=[('UNREACHABLE', 3)]", "DEAD_PORT:S5455:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD:live:want=9:hits=3', 'TRANSIENT_PASS:live:want=4:hits=3', 'DEAD:live:want=9:hits=3', 'TRANSIENT_PASS:live:want=4:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3235', 'REFUSED', 0), ('S3004', 'REFUSED', 0), ('S5490', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S4734', 'UNREACHABLE', 3)] wall=70s hits=3 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlONoRetry/caseB counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT

NONE-MET KotodamaR62.CtlONoRetry/caseB fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/ctlB/tools/reopen-row.py smallest-counter-change=none-needed; the frozen predicate rejects a re-opener that never runs a second pass (GEN/BOUND fail on DEAD, DEAD_PORT and TRANSIENT_PASS).

### C — no `min(gap, 5)` wait between attempts (SURVIVOR)

```text
=== CASE caseC
counter: bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/reports/round-62/accept-o.py
d29b7533eefc251dff9949cbfb8688570e77ed23ee68b84e2dda1c13f33954c6  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3221', 'REFUSED', 0), ('S8684', 'REFUSED', 0), ('S1387', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9671', 'UNREACHABLE', 9)] wall=120s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlONoRetry/caseC counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

CONTROL-MET KotodamaR62.CtlONoRetry/caseC fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/ctlC/tools/reopen-row.py smallest-counter-change=raise the DEFAULT leg's wall floor from 100 s to 130 s at reports/round-62/accept-o.py line 370 (rejects the survivor at 120 s, keeps the honest 150 s passing); the frozen predicate accepts a re-opener that omits the contract's `waiting min(gap, 5) s between attempts`.

### D — diagnostic: no wait at all

```text
=== CASE caseD
counter: bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/reports/round-62/accept-o.py
3d5fce1dff5674d0e15dbb7eea83eba2b877fa09776bc089acdf48ee2fd85d95  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3057', 'REFUSED', 0), ('S7869', 'REFUSED', 0), ('S4455', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S7859', 'UNREACHABLE', 9)] wall=0s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlONoRetry/caseD counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=DEFAULT

NONE-MET KotodamaR62.CtlONoRetry/caseD fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/ctlD/tools/reopen-row.py smallest-counter-change=none-needed; the frozen predicate rejects a re-opener that waits not at all (DEFAULT wall=0s).

### E — diagnostic: inter-pass gap capped at `min(gap, 5)`

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7315', 'REFUSED', 0), ('S9404', 'REFUSED', 0), ('S8686', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S5341', 'UNREACHABLE', 9)] wall=40s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
```

RECEIPT KotodamaR62.CtlONoRetry/caseE counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=DEFAULT

NONE-MET KotodamaR62.CtlONoRetry/caseE fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/ctlE/tools/reopen-row.py smallest-counter-change=none-needed; the frozen predicate rejects a re-opener whose inter-pass gap is `min(gap,5)` instead of `gap` (DEFAULT wall=40s).

### restore — pristine clone slot (tool absent)

```text
=== CASE restore
counter: bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/clone/reports/round-62/accept-o.py
tool-state=ABSENT
TOOL FAIL path=tools/reopen-row.py exists=False
INDEP FAIL no tool
GEN FAIL no tool
ORDER FAIL no tool
BOUND FAIL no tool
EXIT FAIL no tool
PRIV FAIL no tool
DEFAULT FAIL no tool
ERR FAIL no tool
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlONoRetry/restore counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

NONE-MET KotodamaR62.CtlONoRetry/restore fixture=absent-slot (clone `tools/reopen-row.py` at `f0173481047a93c46798f90b68d71d4f169d2642` has no such path) smallest-counter-change=none-needed; the frozen predicate rejects the missing tool.

### Corroborating runs under a different invocation

The same two cases were additionally scored with `--root` pointing at their own fixture
directory instead of the clone slot, to show the verdict is not an artefact of the
invocation style. Both reproduced the clone-slot result exactly.

caseB via `--root .../ctlB`:

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=5 ["DEAD:S2021:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]", "TRANSIENT_PASS:S5126:want=LOCATED/4:got=[('UNREACHABLE', 3)]", "DEAD:S1998:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]", "TRANSIENT_PASS:S6049:want=LOCATED/4:got=[('UNREACHABLE', 3)]", "DEAD_PORT:S5620:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD:live:want=9:hits=3', 'TRANSIENT_PASS:live:want=4:hits=3', 'DEAD:live:want=9:hits=3', 'TRANSIENT_PASS:live:want=4:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5936', 'REFUSED', 0), ('S9181', 'REFUSED', 0), ('S4492', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S5704', 'UNREACHABLE', 3)] wall=70s hits=3 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlONoRetry/caseB-rootoverride counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT

caseC via `--root .../ctlC`:

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6356', 'REFUSED', 0), ('S9033', 'REFUSED', 0), ('S7516', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8242', 'UNREACHABLE', 9)] wall=120s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlONoRetry/caseC-rootoverride counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

CONTROL-MET KotodamaR62.CtlONoRetry/caseC-rootoverride fixture=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/ctlC/tools/reopen-row.py smallest-counter-change=raise the DEFAULT leg's wall floor from 100 s to 130 s at reports/round-62/accept-o.py line 370; the survivor is accepted under both invocation styles.

## Development iterations of the mutation base (not scored cases)

Two earlier drafts of the honest base were run before the base was finalised; they are
recorded here for full disclosure because they are the reason the base was rewritten, and
they double as an incidental demonstration that GEN/BOUND catch under-retrying. The
first draft failed GEN and BOUND (it re-entered a second pass for rows whose first pass
had already answered non-transiently, inflating `attempts`):

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=14 ["CAP_FIG:S3817:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]", "CAP_CLASS:S7409:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]", "SCRIPT:S9014:want=ABSENT/1:got=[('ABSENT', 3)]", "SCRIPT:S9157:want=ABSENT/1:got=[('ABSENT', 3)]", "ABSENT:S2937:want=ABSENT/1:got=[('ABSENT', 3)]", "ARCHIVE_CAPTION:S8691:want=CAPTION_ONLY/2:got=[('CAPTION_ONLY', 6)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['CAP_FIG:live:want=1:hits=3', 'CAP_CLASS:live:want=1:hits=3', 'SCRIPT:live:want=1:hits=3', 'SCRIPT:live:want=1:hits=3', 'ABSENT:live:want=1:hits=3', 'ARCHIVE_CAPTION:live:want=1:hits=3', 'ARCHIVE_CAPTION:arch:want=1:hits=3', 'ARCHIVE_CAPTION:live:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2629', 'REFUSED', 0), ('S1813', 'REFUSED', 0), ('S3208', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2584', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

The second draft (same behaviour, `wait_between_attempts` plumbing removed) reached
`GEN PASS ... wrong=0`, `BOUND PASS bad=[]`, `DEFAULT PASS ... wall=150s` and
`ACCEPT-O-62: PASS`, exit 0 — the behaviour that became the final honest base.

## Restoration, bounds and non-interference

- Clone state at return: `git status --porcelain` **empty**, HEAD
  `f0173481047a93c46798f90b68d71d4f169d2642`, the clone slot `tools/reopen-row.py`
  **absent** (as at the base revision: `git cat-file -e f017348…:tools/reopen-row.py`
  reports the path does not exist there). The counter's SHA-256 after the final run is
  unchanged (`bfd17a30…`), so no counter byte was touched.
- The lane was written to **only** by this report. No lane source, corpus entry,
  SOURCES row, claims file, counter, or sibling fixture was modified. The lane's
  pre-existing uncommitted edits to `reports/round-62/claims.json` and
  `reports/round-62/separability-manifest.json` were already present when this seat
  started and are not this seat's work.
- All fixtures, logs and the clone remain under
  `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/` (189 MB) for reproduction.
  No file was written under `/home/vgpnk/.omp/`.
- No git/jj write command was run in the lane or in the fleet repo; the only git
  commands were `clone`, `checkout`, `rev-parse`, `cat-file` and `status` inside the
  scratch clone with the git environment variables unset.
- No install or update was performed, so there is nothing to record against the
  operator's tooling directive.

## Verdict

Mutation-kill experiment: **5 of 6 scored cases behaved as the counter's discrimination
requires.** A (one attempt per URL, one pass) and B (one pass) are killed by GEN and
BOUND on the TRANSIENT*/DEAD* classes, exactly as predicted; the honest base is accepted
with every leg PASS, so the counter is not vacuous; D and E are killed by DEFAULT,
showing the leg does police the inter-pass gap.

**One survivor: mutant C (no `min(gap, 5)` wait between attempts) is accepted by the
frozen counter with `ACCEPT-O-62: PASS`, exit 0.** The DEFAULT leg's
`100 <= wall <= 600` window admits both the honest 150 s and the contract-violating
120 s. The smallest counter change that closes the hole is raising that floor to 130 s
at `reports/round-62/accept-o.py` line 370. Whether that revision is still permissible
under the round's "revision only before the first run on the claimed object" rule is the
L1's decision; this seat made no counter edit and judges no claim.

No live fetch, no external source and no build was involved: every observation above
comes from the frozen counter's own offline random local fixture.
