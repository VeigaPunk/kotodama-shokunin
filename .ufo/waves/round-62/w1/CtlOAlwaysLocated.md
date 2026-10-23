# CtlOAlwaysLocated — Claim O pre-data constant-answer controls

## Scope and axes

- Axis: operability. Probe axes: verdict/attempt fidelity, observed request bounds, exit semantics, input-order preservation, private-host refusal, default timing, and input errors.
- Frozen clone revision: `f0173481047a93c46798f90b68d71d4f169d2642`.
- Frozen counter: `reports/round-62/accept-o.py`, SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` before and after every run.
- Prerequisites read: round-62 claims, round-61 spot-check section 7, frozen counter contract and implementation, godspeed skill, shokunin skill/protocol, and operator install rules.
- Scratch root: `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated`. No lane implementation or registry was edited. No installs or updates. No counter edits or PROBE counter copies.

## Results

| Fixture | Passing legs | Stopping legs | Frozen result |
|---|---|---|---|
| always-located | 4/9: TOOL, INDEP, ORDER, ERR | GEN, BOUND, EXIT, PRIV, DEFAULT | FAIL, exit 1 |
| always-absent | 4/9: TOOL, INDEP, ORDER, ERR | GEN, BOUND, EXIT, PRIV, DEFAULT | FAIL, exit 1 |
| guessed-attempts | 6/9: TOOL, INDEP, ORDER, EXIT, PRIV, ERR | GEN, BOUND, DEFAULT | FAIL, exit 1 |
| archive-marker | 5/9: TOOL, INDEP, ORDER, PRIV, ERR | GEN, BOUND, EXIT, DEFAULT | FAIL, exit 1 |

**Best observed: guessed-attempts, 6/9 legs** (`TOOL INDEP ORDER EXIT PRIV ERR`); `GEN BOUND DEFAULT` reject it. This is a count of detector legs, not a redefinition of the all-legs predicate.

NONE-MET always-located — no fixture obtained frozen PASS; existing GEN/BOUND already stop the constant answer. Smallest counter change needed: none.
NONE-MET always-absent — no fixture obtained frozen PASS; existing GEN/BOUND already stop the constant answer. Smallest counter change needed: none.
NONE-MET guessed-attempts — no fixture obtained frozen PASS; existing GEN/BOUND/DEFAULT stop metadata-only guessed verdicts/counts. Smallest counter change needed: none.
NONE-MET archive-marker — no fixture obtained frozen PASS; existing GEN/BOUND stop treating `/web/` presence as proof. Smallest counter change needed: none.

Mutation verdict: **inconclusive as killed-mutant evidence**, not killed. The pristine revision has no tool and fails; the deliberately defective always-LOCATED baseline also fails. The four controls were rejected, but a failing baseline cannot establish a mutation kill. No surviving/passing control was observed.

## Fixtures and mutations

All four tools make **zero network requests**. They share independent argparse/input-error handling and preserve argument order. The mutations touch only the `answer` function; the frozen counter is unchanged.

- `always-located.py`: every normal ID prints `ROW <id> LOCATED attempts=1 url=-`; summary counts every ID; normal exit 0.
- `always-absent.py`: the single behavior-bearing return changes LOCATED to ABSENT, attempts remains 1; normal exit 1.
- `guessed-attempts.py`: guesses NO_ROW/NO_QUOTE from registry metadata, REFUSED whenever private access is not enabled, and LOCATED for every other row; copies attempt counts from a metadata-based verdict map (0 for structural/refusal outcomes, 2 for a source containing `/web/`, otherwise 1). No fetch, retry, HTML parsing, or caption separation.
- `archive-marker.py`: same metadata checks, then LOCATED/2 only if the source cell contains `/web/`, otherwise ABSENT/1. No page content inspected.

| Preserved fixture path | SHA-256 |
|---|---|
| `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/fixtures/always-located.py` | `d522d1b285cc3f7a09b68a01a81e94553a6e6bbfd7c998f0682497dfbddaef9a` |
| `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/fixtures/always-absent.py` | `3c995f398e796fdef9ddc8cf776e4df14e84e820e53233aca6cc7d35aae4e92f` |
| `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/fixtures/guessed-attempts.py` | `74333352cc6ac2c477ee4b55b29a727cfbed21af66db2c737e2cb0da878d4cd6` |
| `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/fixtures/archive-marker.py` | `079d20028e97049906ea9221a3ba7169b0eb9ae6263d8c68d42d59c5093df351` |

Expected detector: GEN rejects incorrect verdicts or claimed attempt counts, BOUND compares actual server requests (all zero here) against required counts, and DEFAULT requires real nine-request bounded retry and 100–600 seconds elapsed. Literal constants also fail mixed/all-body exit behavior and private refusal. Metadata guessing can pass EXIT/PRIV without implementing reopening, but cannot pass the frozen predicate.

### Exact behavior diffs against always-located baseline

```diff
--- always-located.py
+++ always-absent.py
@@ -15,7 +15,7 @@
 
 
 def answer(sid, rows, args):
-    return "LOCATED", 1
+    return "ABSENT", 1
 
 
 def main():
```

```diff
--- always-located.py
+++ guessed-attempts.py
@@ -15,7 +15,21 @@
 
 
 def answer(sid, rows, args):
-    return "LOCATED", 1
+    cells = rows.get(sid)
+    if cells is None:
+        verdict = "NO_ROW"
+    else:
+        quote = re.search(r'["“]([^"”]+)["”]', cells[6])
+        words = re.sub(r"[\W_]+", " ", unicodedata.normalize("NFKC", quote[1]).casefold()).split() if quote else []
+        if len(words) < 8 or not re.search(r"https?://", cells[2]):
+            verdict = "NO_QUOTE"
+        elif not args.allow_private:
+            verdict = "REFUSED"
+        else:
+            verdict = "LOCATED"
+    guesses = {"LOCATED": 2 if cells and "/web/" in cells[2] else 1,
+               "NO_ROW": 0, "NO_QUOTE": 0, "REFUSED": 0}
+    return verdict, guesses[verdict]
 
 
 def main():
```

```diff
--- always-located.py
+++ archive-marker.py
@@ -15,7 +15,16 @@
 
 
 def answer(sid, rows, args):
-    return "LOCATED", 1
+    cells = rows.get(sid)
+    if cells is None:
+        return "NO_ROW", 0
+    quote = re.search(r'["“]([^"”]+)["”]', cells[6])
+    words = re.sub(r"[\W_]+", " ", unicodedata.normalize("NFKC", quote[1]).casefold()).split() if quote else []
+    if len(words) < 8 or not re.search(r"https?://", cells[2]):
+        return "NO_QUOTE", 0
+    if not args.allow_private:
+        return "REFUSED", 0
+    return ("LOCATED", 2) if "/web/" in cells[2] else ("ABSENT", 1)
 
 
 def main():
```

## Full frozen-counter receipts

Every run used the same unmodified detector from the frozen clone. Working directory: `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/clone`.

```sh
env TMPDIR=/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/tmp PYTHONDONTWRITEBYTECODE=1 timeout 900 python3 -B reports/round-62/accept-o.py
```

The timeout wrapper return code is recorded below as `exit=`. Each counter run creates fresh randomized local fixtures, so generated IDs and diagnostic ordering differ across restored runs. All stderr streams were empty. Raw structured receipts remain under `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/receipts`.

### pristine-no-tool

Tool SHA-256: `ABSENT`; elapsed 0.064 seconds.

```text
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

RECEIPT CtlOAlwaysLocated/pristine-no-tool counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

### always-located

Tool SHA-256: `d522d1b285cc3f7a09b68a01a81e94553a6e6bbfd7c998f0682497dfbddaef9a`; elapsed 0.571 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=31 ["TRANSIENT_PASS:S4231:want=LOCATED/4:got=[('LOCATED', 1)]", "ABSENT:S5204:want=ABSENT/1:got=[('LOCATED', 1)]", "ABSENT:S9425:want=ABSENT/1:got=[('LOCATED', 1)]", "DEAD:S8911:want=UNREACHABLE/9:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S7811:want=CAPTION_ONLY/2:got=[('LOCATED', 1)]", "NOROW:S8356:want=NO_ROW/0:got=[('LOCATED', 1)]"] summary_ok=False exit=0
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['BODY_SPLIT:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'BODY:live:want=1:hits=0', 'ABSENT:live:want=1:hits=0', 'ABSENT:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[('S3612', 'LOCATED', 1), ('S6520', 'LOCATED', 1), ('S1259', 'LOCATED', 1)]
DEFAULT FAIL rows=[('S5088', 'LOCATED', 1)] wall=0s hits=0 exit=0
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/always-located counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,PRIV,DEFAULT

### always-absent

Tool SHA-256: `3c995f398e796fdef9ddc8cf776e4df14e84e820e53233aca6cc7d35aae4e92f`; elapsed 0.574 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=33 ["SHORT:S4778:want=NO_QUOTE/0:got=[('ABSENT', 1)]", "TRANSIENT_PASS:S6709:want=LOCATED/4:got=[('ABSENT', 1)]", "DEAD_ARCHIVE:S8521:want=LOCATED/2:got=[('ABSENT', 1)]", "CAP_ATTR:S5616:want=CAPTION_ONLY/1:got=[('ABSENT', 1)]", "NOROW:S2678:want=NO_ROW/0:got=[('ABSENT', 1)]", "TRANSIENT2:S4315:want=LOCATED/3:got=[('ABSENT', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['TRANSIENT_PASS:live:want=4:hits=0', 'ABSENT:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ABSENT:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'SCRIPT:live:want=1:hits=0', 'TRANSIENT2:live:want=3:hits=0']
EXIT FAIL gen_exit=1 body_exit=1
PRIV FAIL exit=1 rows=[('S6934', 'ABSENT', 1), ('S8571', 'ABSENT', 1), ('S7135', 'ABSENT', 1)]
DEFAULT FAIL rows=[('S1680', 'ABSENT', 1)] wall=0s hits=0 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/always-absent counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,PRIV,DEFAULT

### restored-after-absent

Tool SHA-256: `d522d1b285cc3f7a09b68a01a81e94553a6e6bbfd7c998f0682497dfbddaef9a`; elapsed 0.552 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=31 ["CAP_ATTR:S1563:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "SCRIPT:S2401:want=ABSENT/1:got=[('LOCATED', 1)]", "TRANSIENT_PASS:S2111:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S8454:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD:S4668:want=UNREACHABLE/9:got=[('LOCATED', 1)]", "TRANSIENT_PASS:S5813:want=LOCATED/4:got=[('LOCATED', 1)]"] summary_ok=False exit=0
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['CAP_ATTR:live:want=1:hits=0', 'SCRIPT:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'BODY:live:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[('S9544', 'LOCATED', 1), ('S2710', 'LOCATED', 1), ('S3128', 'LOCATED', 1)]
DEFAULT FAIL rows=[('S9886', 'LOCATED', 1)] wall=0s hits=0 exit=0
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/restored-after-absent counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,PRIV,DEFAULT

### guessed-attempts

Tool SHA-256: `74333352cc6ac2c477ee4b55b29a727cfbed21af66db2c737e2cb0da878d4cd6`; elapsed 0.553 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=23 ["CAP_FIG:S7165:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "ABSENT:S6200:want=ABSENT/1:got=[('LOCATED', 1)]", "TRANSIENT2:S7747:want=LOCATED/3:got=[('LOCATED', 1)]", "CAP_ATTR:S2265:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "GONE:S4619:want=UNREACHABLE/1:got=[('LOCATED', 1)]", "CAP_ATTR:S9743:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['BODY:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'ABSENT:live:want=1:hits=0', 'TRANSIENT2:live:want=3:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'BODY:live:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9265', 'REFUSED', 0), ('S7846', 'REFUSED', 0), ('S3162', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S8915', 'LOCATED', 1)] wall=0s hits=0 exit=0
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/guessed-attempts counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT

### restored-after-guesses

Tool SHA-256: `d522d1b285cc3f7a09b68a01a81e94553a6e6bbfd7c998f0682497dfbddaef9a`; elapsed 0.589 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=31 ["CAP_CLASS:S7988:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "TRANSIENT2:S6176:want=LOCATED/3:got=[('LOCATED', 1)]", "CAP_CLASS:S7986:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "SHORT:S8580:want=NO_QUOTE/0:got=[('LOCATED', 1)]", "NOQUOTE:S9938:want=NO_QUOTE/0:got=[('LOCATED', 1)]", "NOROW:S4562:want=NO_ROW/0:got=[('LOCATED', 1)]"] summary_ok=False exit=0
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['CAP_CLASS:live:want=1:hits=0', 'TRANSIENT2:live:want=3:hits=0', 'CAP_CLASS:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[('S6770', 'LOCATED', 1), ('S4484', 'LOCATED', 1), ('S4831', 'LOCATED', 1)]
DEFAULT FAIL rows=[('S3389', 'LOCATED', 1)] wall=0s hits=0 exit=0
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/restored-after-guesses counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,PRIV,DEFAULT

### archive-marker

Tool SHA-256: `079d20028e97049906ea9221a3ba7169b0eb9ae6263d8c68d42d59c5093df351`; elapsed 0.586 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=25 ["CAP_ATTR:S4418:want=CAPTION_ONLY/1:got=[('ABSENT', 1)]", "CAP_ATTR:S9390:want=CAPTION_ONLY/1:got=[('ABSENT', 1)]", "BODY_SPLIT:S8911:want=LOCATED/1:got=[('ABSENT', 1)]", "ARCHIVE_CAPTION:S6255:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "TRANSIENT_PASS:S2269:want=LOCATED/4:got=[('ABSENT', 1)]", "GONE:S7891:want=UNREACHABLE/1:got=[('ABSENT', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['CAP_ATTR:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0']
EXIT FAIL gen_exit=1 body_exit=1
PRIV PASS exit=1 rows=[('S7597', 'REFUSED', 0), ('S3219', 'REFUSED', 0), ('S2576', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S9392', 'ABSENT', 1)] wall=0s hits=0 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/archive-marker counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,DEFAULT

### restored-after-archive

Tool SHA-256: `d522d1b285cc3f7a09b68a01a81e94553a6e6bbfd7c998f0682497dfbddaef9a`; elapsed 0.575 seconds.

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=31 ["GONE:S3662:want=UNREACHABLE/1:got=[('LOCATED', 1)]", "ABSENT:S4860:want=ABSENT/1:got=[('LOCATED', 1)]", "SHORT:S2319:want=NO_QUOTE/0:got=[('LOCATED', 1)]", "TRANSIENT_PASS:S7982:want=LOCATED/4:got=[('LOCATED', 1)]", "NOROW:S7943:want=NO_ROW/0:got=[('LOCATED', 1)]", "CAP_FIG:S7782:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=0
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['GONE:live:want=1:hits=0', 'ABSENT:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'CAP_FIG:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'SCRIPT:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[('S7385', 'LOCATED', 1), ('S6144', 'LOCATED', 1), ('S5706', 'LOCATED', 1)]
DEFAULT FAIL rows=[('S5983', 'LOCATED', 1)] wall=0s hits=0 exit=0
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOAlwaysLocated/restored-after-archive counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,PRIV,DEFAULT

### restored-no-tool

Tool SHA-256: `ABSENT`; elapsed 0.058 seconds.

```text
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

RECEIPT CtlOAlwaysLocated/restored-no-tool counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

## Restoration evidence

- Initial and final clone `tools/reopen-row.py`: ABSENT (there are no baseline tool bytes to hash). The final no-tool run reproduces the pristine 0/9 failing-leg set.
- Each mutation was followed by exact restoration of the always-LOCATED baseline and the same detector run. Restored SHA-256 on all three restorations: `d522d1b285cc3f7a09b68a01a81e94553a6e6bbfd7c998f0682497dfbddaef9a`, byte equality observed true.
- Counter before/after SHA-256: `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` / `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`; unchanged.
- Restoration record: `/fast/scratch/hyaku/kotodama-r62/CtlOAlwaysLocated/receipts/restoration.json`.
- All spawned finite processes completed and were bounded with timeout <=900 seconds. No background jobs or delegations started; child-process registry was empty at closure.
- The only write in the lane is this scoped report. The scratch fixtures/receipts are retained for reproduction; nothing was integrated, shipped, or judged as an accepted claim.
