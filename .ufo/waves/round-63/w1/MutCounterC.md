# MutCounterC — round-63 pre-data control (claim C)

- Seat: `kotodama-r63-w1-MutCounterC` (mutation-tester, leaf — no delegation, no background jobs)
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, measured revision `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` (round base `65b393ef3a4d82bd693cc21b7f96a1231417d522`)
- Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/` (clone + `probes/` + `runs/`)
- Frozen counter: `reports/round-63/accept-c.py`, sha256 `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`
  (matches the declared hash; `reports/round-63/accept-o.py` sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` also matches — not exercised, claim O belongs to other seats)
- Docs read first: `reports/round-63/claims.json` (both predicates), `accept-c.py`/`accept-o.py` docstrings, `corpus/lessons/round-62-verifier-spotcheck.md` §5 (routed defects; §5 item 1 is the O gate, not C).

## No-work / base tree actually scored

Clone of the lane at `80d53ff`, claimed tree **before any claim-C work**:

- `corpus/knowledge/culture-material/headgear-head-covering-codes.md` absent (`git show 80d53ff:<path>` exits 128).
- `corpus/SOURCES.md` has `619` `| S` rows (identical to round base; `git diff 65b393e 80d53ff -- corpus/SOURCES.md corpus/knowledge corpus/README.md` is empty).
- `git status --porcelain` in the clone: empty before and after all probes.

This is the cheapest possible fixture that skips the claimed work (an empty/no-work tree). The unmutated frozen counter must FAIL it, and does.

## Mutants (PROBE copies, outside the lane, diffs shown)

All probes are byte copies of the frozen counter under `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/probes/`; the lane copy was never edited.

| case | mutation | probe sha256 |
|---|---|---|
| M1 | RESTATE copy-run (>12 consecutive verbatim words) check dropped | `190aa7756a01722a9aeac1b16c6a7729f3fa1aaff3f9fbab45c4c7b49f588f8d` |
| M2 | LIVE weakened to 3 of 6 frozen rows (`LIVE_IDS[:3]` = S694, S698, S702) | `f258e057b378be5b340ff3c91ee7d0641c0e7133eec3686067a52a314b9d362a` |
| M3 | LINK leg dropped entirely | `e832ed2d9d15d2ea1be7dd0eafa20348674a1c05d11e723924e9a5559725abe0` |
| M4 | ROWS relaxed to accept tier C | `733352a622aadadcfce0b41945ae07f9eae1a340e619dedd075012051de402c3` |
| ALL | M1+M2+M3+M4 combined | `dd7df0214caca17e0f5c03c0f2bc2553ac61049db8c20dc33a268ffd8f856872` |

### diff frozen -> M1

```diff
--- reports/round-63/accept-c.py
+++ probes/accept-c-m1.py
@@ -235,19 +235,7 @@
                 order_hits += 1
         if order_hits < 3:
             restate_bad.append(f"line{i}:{sid}:in_order={order_hits}")
-        # longest run of consecutive clause words copied verbatim from the quote
-        clause_words = norm_words(clause)
-        best = 0
-        for start in range(len(clause_words)):
-            for length in range(best + 1, len(clause_words) - start + 1):
-                window = clause_words[start:start + length]
-                joined = " ".join(window)
-                if " " + joined + " " in " " + " ".join(qset_seq) + " ":
-                    best = length
-                else:
-                    break
-        if best > 12:
-            restate_bad.append(f"line{i}:{sid}:copy_run={best}")
+        # PROBE M1: copy-run check dropped
     leg("RESTATE", not restate_bad, f"bad={restate_bad[:8]} lines={len(cited)}")
```

### diff frozen -> M2

```diff
--- reports/round-63/accept-c.py
+++ probes/accept-c-m2.py
@@ -298,7 +298,7 @@
     # ---------- LIVE ----------
     live_bad = []
-    for sid in LIVE_IDS:
+    for sid in LIVE_IDS[:3]:  # PROBE M2: only 3 of 6
         if sid not in reg_by_id:
             live_bad.append(f"{sid}:no_row")
             continue
```

### diff frozen -> M3

```diff
--- reports/round-63/accept-c.py
+++ probes/accept-c-m3.py
@@ -250,17 +250,7 @@
             restate_bad.append(f"line{i}:{sid}:copy_run={best}")
     leg("RESTATE", not restate_bad, f"bad={restate_bad[:8]} lines={len(cited)}")
 
-    # ---------- LINK ----------
-    link_bad = []
-    for sid, url in live_urls.items():
-        if not url:
-            continue
-        hits = sum(1 for line in reg_lines if url in line)
-        if hits != 1:
-            link_bad.append(f"{sid}:registry_hits={hits}")
-        if url in text:
-            link_bad.append(f"{sid}:url_in_entry")
-    leg("LINK", not link_bad, f"bad={link_bad[:6]}")
+    # PROBE M3: LINK leg dropped
 
     # ---------- APPEND ----------
```

### diff frozen -> M4

```diff
--- reports/round-63/accept-c.py
+++ probes/accept-c-m4.py
@@ -159,7 +159,7 @@
         source, kind, tier, scope, anchor = cs[1], cs[2], cs[3], cs[4], cs[5]
         teaches, status, opened, recheck, usedby = cs[6], cs[7], cs[8], cs[9], cs[10]
-        if tier not in ("A", "B"):
+        if tier not in ("A", "B", "C"):  # PROBE M4: tier C allowed
             row_bad.append(f"{sid}:tier={tier}")
         if status != "mined":
             row_bad.append(f"{sid}:status={status}")
```

### diff frozen -> ALL

```diff
@@ -159,7 +159,7 @@
-        if tier not in ("A", "B"):
+        if tier not in ("A", "B", "C"):  # PROBE M4: tier C allowed
@@ -235,32 +235,10 @@
-        # longest run of consecutive clause words copied verbatim from the quote
-        clause_words = norm_words(clause)
-        best = 0
-        for start in range(len(clause_words)):
-            for length in range(best + 1, len(clause_words) - start + 1):
-                window = clause_words[start:start + length]
-                joined = " ".join(window)
-                if " " + joined + " " in " " + " ".join(qset_seq) + " ":
-                    best = length
-                else:
-                    break
-        if best > 12:
-            restate_bad.append(f"line{i}:{sid}:copy_run={best}")
+        # PROBE M1: copy-run check dropped
     leg("RESTATE", not restate_bad, f"bad={restate_bad[:8]} lines={len(cited)}")
 
-    # ---------- LINK ----------
-    link_bad = []
-    for sid, url in live_urls.items():
-        if not url:
-            continue
-        hits = sum(1 for line in reg_lines if url in line)
-        if hits != 1:
-            link_bad.append(f"{sid}:registry_hits={hits}")
-        if url in text:
-            link_bad.append(f"{sid}:url_in_entry")
-    leg("LINK", not link_bad, f"bad={link_bad[:6]}")
+    # PROBE M3: LINK leg dropped
 
@@ -298,7 +276,7 @@
-    for sid in LIVE_IDS:
+    for sid in LIVE_IDS[:3]:  # PROBE M2: only 3 of 6
```

## Runs — FULL stdout and exit code

All runs executed as `cd <clone> && timeout 900 python3 -B <counter>`, default `--root` = clone root (the no-work tree). No output was trimmed.

### case base-frozen (sha256 3a531034…f8a5de) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
```

### case base-M1-copyrun-dropped (sha256 190aa775…) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
```

### case base-M2-live-3of6 (sha256 f258e057…) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row']
ACCEPT-C-63: FAIL
```

### case base-M3-link-dropped (sha256 e832ed2d…) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
```

(NOTE: no `LINK` line by construction — the leg was dropped; the verdict still FAILs.)

### case base-M4-tier-c (sha256 733352a6…) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
```

### case base-ALL (sha256 dd7df021…) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row']
ACCEPT-C-63: FAIL
```

### case restored-frozen (sha256 3a531034…f8a5de, run after all mutants) — exit 1

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
```

`diff base-frozen.out restored-frozen.out` → identical; stderr empty in every run.

## Receipts

Legend: `frozen=` is the verdict of the **unmutated** frozen counter on the same no-work tree; `stopped-by=` lists the legs that FAIL in the run named on that line.

```
RECEIPT kotodama-r63-w1-MutCounterC/base-frozen counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
RECEIPT kotodama-r63-w1-MutCounterC/base-M1-copyrun-dropped counter-sha256=190aa7756a01722a9aeac1b16c6a7729f3fa1aaff3f9fbab45c4c7b49f588f8d rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
RECEIPT kotodama-r63-w1-MutCounterC/base-M2-live-3of6 counter-sha256=f258e057b378be5b340ff3c91ee7d0641c0e7133eec3686067a52a314b9d362a rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
RECEIPT kotodama-r63-w1-MutCounterC/base-M3-link-dropped counter-sha256=e832ed2d9d15d2ea1be7dd0eafa20348674a1c05d11e723924e9a5559725abe0 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
RECEIPT kotodama-r63-w1-MutCounterC/base-M4-tier-c counter-sha256=733352a622aadadcfce0b41945ae07f9eae1a340e619dedd075012051de402c3 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
RECEIPT kotodama-r63-w1-MutCounterC/base-ALL counter-sha256=dd7df0214caca17e0f5c03c0f2bc2553ac61049db8c20dc33a268ffd8f856872 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
RECEIPT kotodama-r63-w1-MutCounterC/restored-frozen counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
```

## Verdict

**NONE-MET** — no mutation (and not the frozen counter) lets an empty/no-work tree PASS.

- The frozen counter FAILs the empty tree at exit 1, exactly as intended pre-data (`ACCEPT-C-63: FAIL`).
- M1 and M3 target legs that are already vacuously PASS on an empty tree (`RESTATE lines=0`, `LINK bad=[]`), so removing their teeth cannot flip the verdict.
- M2 still fails LIVE: the first three frozen rows (S694, S698, S702) are also absent (`bad=['S694:no_row','S698:no_row','S702:no_row']`).
- M4 relaxes only the tier check inside ROWS, but ROWS fails earlier (`rows=0` for all 24 ids), so the relaxation is not reached.
- Six legs untouched by the mutations each fail on the empty tree and carry the refusal: FILE, ROWS, ONEID, APPEND, NOHARM, SWEEP. A cheap fixture that skips the claimed work would need to synthesize the entry, 24 registry rows, the base-registry append, a clean cited-lines run, the README/sweep consistency, and three live-located rows — none of the four assigned mutations removes any of those walls on an empty tree.

Mutation-scope findings (latent teeth reductions for a populated tree, not empty-tree passes — the frozen counter catches all four):

- M1: a bullet copying a run >12 words from its row quote would pass RESTATE; the frozen copy-run check rejects it.
- M2: S706/S710/S714 could be NOT_LOCATED and the LIVE leg would still pass; the frozen counter checks all six.
- M3: a live URL duplicated in the entry text or in a second registry line would pass; the frozen LINK leg rejects it.
- M4: a tier-C row would pass ROWS; the frozen ROWS leg rejects it.

## Restoration evidence

- Frozen counter sha256 before first run and after the restored run: both `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`; restored stdout byte-identical to baseline (`diff` clean), stderr empty.
- Clone HEAD `80d53ffde7788299b69dbb0bd0436b2b7ddddb95`; `git status --porcelain` empty after all runs (0 lines).
- Lane `reports/round-63/accept-c.py` never opened for writing by this seat; all mutations confined to PROBE copies under the scratch dir (hashes and diffs above).
- `tools/reopen-row.py` never executed; `reports/round-61/reopen-quote.py` never invoked for data (LIVE short-circuits on missing rows; no network request was made).
- Bounds: no delegation, no background jobs, no installs (no pacman/uv/npm), no git/jj write commands in the lane or the fleet repo; only this report was written in the lane.
