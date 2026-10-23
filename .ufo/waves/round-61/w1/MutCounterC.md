# MutCounterC — round 61 wave 1

## Axes and scope

- **Coverage:** distinguish each of the 14 ACCEPT-C-61 legs with a cheap rejection fixture.
- **Calibration:** separate killed mutants, surviving final-verdict mutants, and inconclusive baselines.
- **Fidelity:** frozen hashes, bounded runs, isolated writes, and exact restoration.

Revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`. Scratch: `/fast/scratch/hyaku/kotodama-r61/MutCounterC`. Only this report was written in the lane. No sibling sources were modified. No dispatch, background process/job, install, external runtime, browser, PDF tooling, or git/jj write in either live repository was used.

## Result

**14 killed; 1 survived; 0 inconclusive.** Every named leg has an individually distinguishing fixture. There were 48 counter invocations: 15 frozen/mutant/restored triples plus three frozen-byte positive-control runs. All pristine/restored detector assertions passed.

**Survivor: LINES_TWO_IDS.** Its fixture changes `LINES FAIL` to `LINES PASS`, but both versions still end `ACCEPT-C-61: FAIL`, exit 1, because LINK and COPY independently flag the same line as `no-row`. This is a coverage finding for the final-label-only oracle, not evidence that the LINES leg was unexercised: the separate non-bullet LINES fixture killed its dropped-leg mutant. [INFERENCE] No full-PASS distinguishing fixture exists for this particular single-point two-id relaxation while the unchanged LINK/COPY guard rejects every line with two distinct recognised ids. The claim/contract was not changed to manufacture a kill.

**Additional cheap control finding:** the frozen counter passes 20 invented rows sharing one synthetic loopback HTTP document. This performs none of the claimed public-source research. It is a detector fixture, not admitted footwear knowledge or a claim that an external source supports these words.

## Detector and fixtures

Frozen counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`. The canonical counter in the clone was never edited; each candidate began as an exact byte copy in `clone/reports/round-61/mutants/NAME.py`. Each mutation changes one behavior-bearing point only. All candidates were restored to frozen bytes after their mutation run.

For each invalid fixture the bounded behavioral detector expects final label `ACCEPT-C-61: FAIL` **and exit 1**. A correct rejection is detector PASS, not a baseline failure. Accepting it is detector FAIL and kills that mutant. A missing/unexpected label or exit would be inconclusive; none occurred. The positive fixture expects PASS/0. The very same fixture and detector were used before, during and after each mutation.

Fixtures preserve the revision’s actual 235 knowledge files, original registry and instrument bytes. Each adds the footwear entry, index/count updates, and 20 rows (19 for FLOOR); the named deviation is listed below. No base-list or TOTAL changes were made. The locator, access checker and README sweep are unchanged copies from the revision. The accepted `--root` interface isolates each fixture.

Ordinary HTTP GETs fetch `http://127.0.0.1:48661/document` from a foreground detector-owned stdlib HTTP server thread. Its body is exactly these synthetic paragraphs:

> The leather shoes feature stitched uppers and durable soles crafted for practical daily wear.
>
> Ceremonial garments display ornate embroidery with colored threads arranged in elaborate decorative patterns.

No access control was encountered or bypassed. The server is shut down, its socket closed, and its thread joined in `finally` after every batch. Each counter process is wrapped with `timeout 90` and a 100-second parent timeout; all observed processes returned normally. Outer batch commands use `timeout 300`; clone/checkout commands were bounded at 900 seconds. No process tree remains from these completed foreground commands.

Executed from the clone:

```text
timeout 300 python3 -B ../detector.py prepare
timeout 300 python3 -B ../detector.py frozen all
# Independent candidate mutations applied with the edit tool.
timeout 300 python3 -B ../detector.py mutated all
# Every candidate overwritten with the exact pristine byte string.
timeout 300 python3 -B ../detector.py restored all
```

The driver records the precise counter command, full stdout, stderr and exit in `runs/NAME.STAGE.json`. Its generated files are individually below 5 MB. Retained fixture roots are `fixtures/NAME/`; `detector.py`, `pristine-counter.bin`, and `mutations.json` retain the reproducer and mutation evidence.

## Mutants and cheapest constructed distinguishing fixtures

All fixture paths below are under the absolute scratch root above. These are cheap constructed witnesses, not a claim of global cost minimality. Except FLOOR, 20 rows are required by the unchanged floor. LOCATE uses the exact 18/20 boundary for SHARE 0.9.

| Mutant | One-point defect | Fixture deviation | Frozen → mutant → restored | Verdict |
|---|---|---|---|---|
| SET | Drop SET predicate tuple | `fixtures/SET/`: Add one empty knowledge/extra.fixture; SWEEP still sees its 236 Markdown files. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| SWEEP | Drop SWEEP tuple | `fixtures/SWEEP/`: Omit only the new entry index row; the knowledge tree and counts remain 236. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| FLOOR | FLOOR 20 → 19 | `fixtures/FLOOR/`: Cite 19 rows (S652–S670), not 20. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| RANGE | Drop RANGE tuple | `fixtures/RANGE/`: Use S652-53 on the first bullet; only S652 is recognised as an id, while the range detector fires. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| STATUS | Invert not status_bad → bool(status_bad) | `fixtures/STATUS/`: Set S652 status to queued. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| OPENED | Invert not opened_bad → bool(opened_bad) | `fixtures/OPENED/`: Set S652 opened to 2026-10-22. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| USEDBY | Drop USEDBY tuple | `fixtures/USEDBY/`: Replace S652 used-by with another path. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| ACCESS | Drop ACCESS tuple | `fixtures/ACCESS/`: Put the literal bypass marker headless in S652 teaches. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| LINES | Drop LINES tuple | `fixtures/LINES/`: Remove the first cited line’s bullet prefix, leaving one id and good word overlap. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| TOPIC | Check cited line text, not the anchor quote | `fixtures/TOPIC/`: S652 quotes the served non-footwear garments sentence; its bullet adds Shoes and retains quote overlap. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| LINK | LINK_MIN 3 → 2 | `fixtures/LINK/`: First line Durable leather footwear matters. shares exactly leather and durable with its quote. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| COPY | COPY_MAX 12 → 13 | `fixtures/COPY/`: First line pastes exactly the first 13 normalised words of the quote. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| LOCATE | SHARE 1.0 → 0.9 | `fixtures/LOCATE/`: Two of 20 anchors contain imaginary violet ceremonies instead of the served ending: 18/20 located. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| FRESH | Drop FRESH tuple | `fixtures/FRESH/`: Add old S001 URL https://glottolog.org/about.html as the second URL of S652; its first local URL still locates. | FAIL/1 → PASS/0 → FAIL/1 | KILLED |
| LINES_TWO_IDS | Allow len(ids) in (1, 2) at LINES only | `fixtures/LINES_TWO_IDS/`: Put distinct S652 and S653 on the first bullet; all rows and individual quotes remain present. | FAIL/1 → FAIL/1 → FAIL/1 | SURVIVED |

## Required receipts

`counter-sha256` and `exit` below describe the frozen run. `probe=PASS` is used **only** for the allowed FLOOR-only variant (20 → 19); its full mutant run below is also the probe run. All other derived counters are deliberately defective mutants, not allowed probes, so their probe field is n/a. Mutant verdicts/hashes are separately recorded, and do not relabel the frozen predicate.

```text
RECEIPT MutCounterC/valid counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none
RECEIPT MutCounterC/SET counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET
RECEIPT MutCounterC/SWEEP counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SWEEP
RECEIPT MutCounterC/FLOOR counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT MutCounterC/RANGE counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=RANGE
RECEIPT MutCounterC/STATUS counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=STATUS
RECEIPT MutCounterC/OPENED counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=OPENED
RECEIPT MutCounterC/USEDBY counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=USEDBY
RECEIPT MutCounterC/ACCESS counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=ACCESS
RECEIPT MutCounterC/LINES counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=LINES
RECEIPT MutCounterC/TOPIC counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOPIC
RECEIPT MutCounterC/LINK counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=LINK
RECEIPT MutCounterC/COPY counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=COPY
RECEIPT MutCounterC/LOCATE counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=LOCATE
RECEIPT MutCounterC/FRESH counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=FRESH
RECEIPT MutCounterC/LINES_TWO_IDS counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,LINK,COPY
```

One control verdict per case (not mutation verdicts):

```text
CONTROL-MET MutCounterC/valid fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid frozen PASS on synthetic local source
NONE-MET MutCounterC/SET fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET frozen FAIL; no allowed probe run
NONE-MET MutCounterC/SWEEP fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP frozen FAIL; no allowed probe run
CONTROL-MET MutCounterC/FLOOR fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR FLOOR-only probe PASS
NONE-MET MutCounterC/RANGE fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE frozen FAIL; no allowed probe run
NONE-MET MutCounterC/STATUS fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS frozen FAIL; no allowed probe run
NONE-MET MutCounterC/OPENED fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED frozen FAIL; no allowed probe run
NONE-MET MutCounterC/USEDBY fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY frozen FAIL; no allowed probe run
NONE-MET MutCounterC/ACCESS fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS frozen FAIL; no allowed probe run
NONE-MET MutCounterC/LINES fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES frozen FAIL; no allowed probe run
NONE-MET MutCounterC/TOPIC fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC frozen FAIL; no allowed probe run
NONE-MET MutCounterC/LINK fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK frozen FAIL; no allowed probe run
NONE-MET MutCounterC/COPY fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY frozen FAIL; no allowed probe run
NONE-MET MutCounterC/LOCATE fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE frozen FAIL; no allowed probe run
NONE-MET MutCounterC/FRESH fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH frozen FAIL; no allowed probe run
NONE-MET MutCounterC/LINES_TWO_IDS fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS frozen FAIL; no allowed probe run
```

## Before/mutant/after hashes and exact diffs

Every candidate’s before hash and after hash is `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`. The restored-run records read this hash before execution; a final `sha256sum` printed the same hash for the canonical counter and all 15 candidate files. The tool’s whole-file restoration receipts also returned the original snapshot tag `7BE4` for all 15. The locator hash is `cdf71cb38155712fe3fdaeefae828622761837a7ba2a12d0d00dd931ad98f53d`; the base-list hash is `c98a8841f73632e09bf04c61d8dac1c37ae60a076a2f82dfe9bb90cb6b2f6f76`.

### SET

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `c1bc38c51698fa267e0675166f930ba71677dfb87e239ce15e241191468b9de7`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/SET.py
@@ -119,8 +119,7 @@
     live = {os.path.relpath(os.path.join(d, f), root)
             for d, _, fs in os.walk(os.path.join(root, "corpus/knowledge"), followlinks=True) for f in fs}
     added, removed = sorted(live - base), sorted(base - live)
-    legs = [("SET", len(live) == TOTAL and added == [ENTRY] and removed == [],
-             f"count={len(live)} required={TOTAL} added={added} removed={removed}")]
+    legs = []
     sweep = run(root, [sys.executable, "-B", "reports/round-28/readme/sweep.py"])
     if sweep is None:
         return 2
```

### SWEEP

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `cf7c68cedf8050bb18404d17ea823a6ce06200eb34d02dc850ddd1c797cd1867`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/SWEEP.py
@@ -129,8 +129,6 @@
     sweep_ok = (sweep.returncode == 0 and rows is not None and missing is not None
                 and int(rows.group(1)) == TOTAL and int(rows.group(2)) == TOTAL
                 and int(missing.group(1)) == 0)
-    legs.append(("SWEEP", sweep_ok, f"exit={sweep.returncode} {rows.group(0) if rows else 'rows ?'} "
-                 f"{missing.group(0) if missing else 'missing_from_index ?'}"))
     path = os.path.join(root, ENTRY)
     cited, table, rows_per_id, spans, lines = [], {}, {}, [], []
     try:
```

### FLOOR

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `10228085028247d0d78e3e10e55670827fefa2bbc652cc28f7fd10f83b0a9ab6`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/FLOOR.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 19
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

### RANGE

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `ab985f7da819ae95f5b8f232914ef71709f7ac8d034aa132d1a3314ae1089610`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/RANGE.py
@@ -150,7 +150,6 @@
     legs.append(("FLOOR", len(cited) >= FLOOR, f"cited={len(cited)} floor={FLOOR}"))
     range_bad = [s for s in cited if not FIRST_SID <= int(s[1:]) <= LAST_SID
                  or rows_per_id.get(s, 0) != 1 or len(table[s]) != 13]
-    legs.append(("RANGE", not range_bad and not spans, f"bad={range_bad} range_notation={spans}"))
     ok_rows = [s for s in cited if s not in range_bad]
     status_bad = [f"{s}:{table[s][8].strip()}" for s in ok_rows if table[s][8].strip() != "mined"]
     legs.append(("STATUS", not status_bad, f"bad={status_bad}"))
```

### STATUS

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `c50c68ca3b4ee073343d0c563336b4b03d8ae4a9511654c20fe92c583037ca95`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/STATUS.py
@@ -153,7 +153,7 @@
     legs.append(("RANGE", not range_bad and not spans, f"bad={range_bad} range_notation={spans}"))
     ok_rows = [s for s in cited if s not in range_bad]
     status_bad = [f"{s}:{table[s][8].strip()}" for s in ok_rows if table[s][8].strip() != "mined"]
-    legs.append(("STATUS", not status_bad, f"bad={status_bad}"))
+    legs.append(("STATUS", bool(status_bad), f"bad={status_bad}"))
     opened_bad = [f"{s}:{table[s][9].strip()}" for s in ok_rows if table[s][9].strip() != OPENED]
     legs.append(("OPENED", not opened_bad, f"bad={opened_bad}"))
     used_bad = [s for s in ok_rows if ENTRY not in [u.strip() for u in re.split(r"[,;]", table[s][11])]]
```

### OPENED

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `9bd4b68d5733210d4d395053172ee2162b27826b7859c3984d17de63edf14228`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/OPENED.py
@@ -155,7 +155,7 @@
     status_bad = [f"{s}:{table[s][8].strip()}" for s in ok_rows if table[s][8].strip() != "mined"]
     legs.append(("STATUS", not status_bad, f"bad={status_bad}"))
     opened_bad = [f"{s}:{table[s][9].strip()}" for s in ok_rows if table[s][9].strip() != OPENED]
-    legs.append(("OPENED", not opened_bad, f"bad={opened_bad}"))
+    legs.append(("OPENED", bool(opened_bad), f"bad={opened_bad}"))
     used_bad = [s for s in ok_rows if ENTRY not in [u.strip() for u in re.split(r"[,;]", table[s][11])]]
     legs.append(("USEDBY", not used_bad, f"bad={used_bad}"))
     access = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
```

### USEDBY

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `6f33caa5e9bb233cd65beb2fce7401984f134423e88549d2fe5f476ae0153271`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/USEDBY.py
@@ -157,7 +157,6 @@
     opened_bad = [f"{s}:{table[s][9].strip()}" for s in ok_rows if table[s][9].strip() != OPENED]
     legs.append(("OPENED", not opened_bad, f"bad={opened_bad}"))
     used_bad = [s for s in ok_rows if ENTRY not in [u.strip() for u in re.split(r"[,;]", table[s][11])]]
-    legs.append(("USEDBY", not used_bad, f"bad={used_bad}"))
     access = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
     if access is None:
         return 2
```

### ACCESS

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `eb8d90bc60f582179e73e6e21bc8100ed60a66f6e7b868019478cde51ea11a31`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/ACCESS.py
@@ -161,8 +161,6 @@
     access = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
     if access is None:
         return 2
-    legs.append(("ACCESS", access.returncode == 0, f"exit={access.returncode} "
-                 f"{(access.stdout.strip().splitlines() or ['?'])[-1]}"))
     lines_bad = []
     for n, l in lines:
         ids = set(SID.findall(l))
```

### LINES

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `0ffebfc96d6a76089eab57c7910f7570a9a458f236fdcb2032a7a58a9b1d0731`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/LINES.py
@@ -168,7 +168,6 @@
         ids = set(SID.findall(l))
         if not re.match(r"^\s*- ", l) or len(ids) != 1:
             lines_bad.append(f"{n}:{','.join(sorted(ids))}")
-    legs.append(("LINES", bool(lines) and not lines_bad, f"cited_lines={len(lines)} bad={lines_bad}"))
     targets = {s: locator.row_target(table[s]) for s in ok_rows}
     topic_bad = [s for s in ok_rows if not set(locator.normalise(targets[s][1]).split()) & TOPIC_WORDS]
     legs.append(("TOPIC", bool(ok_rows) and not topic_bad, f"rows={len(ok_rows)} bad={topic_bad}"))
```

### TOPIC

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `424944049da351fd1a1bc3bfb7c0d3ce07e2b09163da81cd75895f91c4b8c773`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/TOPIC.py
@@ -170,7 +170,7 @@
             lines_bad.append(f"{n}:{','.join(sorted(ids))}")
     legs.append(("LINES", bool(lines) and not lines_bad, f"cited_lines={len(lines)} bad={lines_bad}"))
     targets = {s: locator.row_target(table[s]) for s in ok_rows}
-    topic_bad = [s for s in ok_rows if not set(locator.normalise(targets[s][1]).split()) & TOPIC_WORDS]
+    topic_bad = [s for s in ok_rows if not any(set(locator.normalise(l).split()) & TOPIC_WORDS for _, l in lines if s in SID.findall(l))]
     legs.append(("TOPIC", bool(ok_rows) and not topic_bad, f"rows={len(ok_rows)} bad={topic_bad}"))
     link_bad, copy_bad = [], []
     for n, l in lines:
```

### LINK

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `9757beca1e5ada6fe845e927b48be6c45fd6e1e39b268c92f2e74e77e80b4d6a`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/LINK.py
@@ -58,7 +58,7 @@
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
-LINK_MIN = 3
+LINK_MIN = 2
 COPY_MAX = 12
 SID = re.compile(r"\bS\d{3,}\b")
 TOPIC_WORDS = frozenset("""
```

### COPY

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `fc314827bf913ef96481cb9a78748bf81f66a93bd6e0657d6419415939383583`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/COPY.py
@@ -59,7 +59,7 @@
 SHARE = 1.0
 OPENED = "2026-10-23"
 LINK_MIN = 3
-COPY_MAX = 12
+COPY_MAX = 13
 SID = re.compile(r"\bS\d{3,}\b")
 TOPIC_WORDS = frozenset("""
 shoe shoes shod unshod barefoot footwear sandal sandals boot boots clog clogs moccasin moccasins
```

### LOCATE

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `fd00b78846042706198c45ab572f0ed4bb65cb28b74a8445f81f4a638afcc2cc`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/LOCATE.py
@@ -56,7 +56,7 @@
 LAST_SID = 699
 FLOOR = 20
 LOCATOR = "reports/round-61/reopen-quote.py"
-SHARE = 1.0
+SHARE = 0.9
 OPENED = "2026-10-23"
 LINK_MIN = 3
 COPY_MAX = 12
```

### FRESH

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `52a757a1c7d522990e7b6b0cd527c2789c20d358da77c9ccc0b4f36f41956389`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/FRESH.py
@@ -211,7 +211,6 @@
     old = {norm(u) for s, cells in table.items() if int(s[1:]) < FIRST_SID
            for u in locator.URL.findall(cells[2])}
     stale = sorted(s for s in targets if any(norm(u) in old for u in targets[s][0]))
-    legs.append(("FRESH", not stale, f"rows_reusing_registry_urls={stale}"))
     for name, ok, detail in legs:
         print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
     verdict = all(ok for _, ok, _ in legs)
```

### LINES_TWO_IDS

Before: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
Mutant: `a1594c15f5c9b3aedd9aa2b5d2c57baee10ead45cbec0cfb26d9d6c75328ee80`  
After: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```diff
--- frozen/accept-c.py
+++ mutants/LINES_TWO_IDS.py
@@ -166,7 +166,7 @@
     lines_bad = []
     for n, l in lines:
         ids = set(SID.findall(l))
-        if not re.match(r"^\s*- ", l) or len(ids) != 1:
+        if not re.match(r"^\s*- ", l) or len(ids) not in (1, 2):
             lines_bad.append(f"{n}:{','.join(sorted(ids))}")
     legs.append(("LINES", bool(lines) and not lines_bad, f"cited_lines={len(lines)} bad={lines_bad}"))
     targets = {s: locator.row_target(table[s]) for s in ok_rows}
```

## Full observed stdout and exit codes

No output below is shortened. Stderr was empty for every invocation. The detector assertion is shown separately from the counter’s own output.

### valid/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR PASS
```

### valid/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR PASS
```

### valid/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/valid
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR PASS
```

### SET/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET
SET FAIL count=237 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md', 'corpus/knowledge/extra.fixture'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### SET/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET`  
Counter SHA-256: `c1bc38c51698fa267e0675166f930ba71677dfb87e239ce15e241191468b9de7`

```text
timeout 90 python3 -B reports/round-61/mutants/SET.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### SET/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/SET.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SET
SET FAIL count=237 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md', 'corpus/knowledge/extra.fixture'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### SWEEP/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP FAIL exit=1 rows 235 files 236 missing_from_index 1 ['culture-material/footwear-codes-terminology.md']
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### SWEEP/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP`  
Counter SHA-256: `cf7c68cedf8050bb18404d17ea823a6ce06200eb34d02dc850ddd1c797cd1867`

```text
timeout 90 python3 -B reports/round-61/mutants/SWEEP.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### SWEEP/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/SWEEP.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/SWEEP
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP FAIL exit=1 rows 235 files 236 missing_from_index 1 ['culture-material/footwear-codes-terminology.md']
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### FLOOR/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=19 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=19 bad=[]
TOPIC PASS rows=19 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=19 cited=19 need=19 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### FLOOR/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR`  
Counter SHA-256: `10228085028247d0d78e3e10e55670827fefa2bbc652cc28f7fd10f83b0a9ab6`

```text
timeout 90 python3 -B reports/round-61/mutants/FLOOR.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=19 floor=19
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=19 bad=[]
TOPIC PASS rows=19 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=19 cited=19 need=19 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### FLOOR/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/FLOOR.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FLOOR
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=19 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=19 bad=[]
TOPIC PASS rows=19 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=19 cited=19 need=19 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### RANGE/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE FAIL bad=[] range_notation=['S652-53']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### RANGE/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE`  
Counter SHA-256: `ab985f7da819ae95f5b8f232914ef71709f7ac8d034aa132d1a3314ae1089610`

```text
timeout 90 python3 -B reports/round-61/mutants/RANGE.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### RANGE/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/RANGE.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/RANGE
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE FAIL bad=[] range_notation=['S652-53']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### STATUS/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS FAIL bad=['S652:queued']
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### STATUS/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS`  
Counter SHA-256: `c50c68ca3b4ee073343d0c563336b4b03d8ae4a9511654c20fe92c583037ca95`

```text
timeout 90 python3 -B reports/round-61/mutants/STATUS.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=['S652:queued']
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### STATUS/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/STATUS.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/STATUS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS FAIL bad=['S652:queued']
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### OPENED/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED FAIL bad=['S652:2026-10-22']
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### OPENED/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED`  
Counter SHA-256: `9bd4b68d5733210d4d395053172ee2162b27826b7859c3984d17de63edf14228`

```text
timeout 90 python3 -B reports/round-61/mutants/OPENED.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=['S652:2026-10-22']
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### OPENED/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/OPENED.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/OPENED
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED FAIL bad=['S652:2026-10-22']
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### USEDBY/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### USEDBY/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY`  
Counter SHA-256: `6f33caa5e9bb233cd65beb2fce7401984f134423e88549d2fe5f476ae0153271`

```text
timeout 90 python3 -B reports/round-61/mutants/USEDBY.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### USEDBY/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/USEDBY.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/USEDBY
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### ACCESS/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS FAIL exit=1 ACCESS: 3 flagged rows, 2 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### ACCESS/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS`  
Counter SHA-256: `eb8d90bc60f582179e73e6e21bc8100ed60a66f6e7b868019478cde51ea11a31`

```text
timeout 90 python3 -B reports/round-61/mutants/ACCESS.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### ACCESS/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/ACCESS.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/ACCESS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS FAIL exit=1 ACCESS: 3 flagged rows, 2 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINES/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=20 bad=['6:S652']
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINES/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES`  
Counter SHA-256: `0ffebfc96d6a76089eab57c7910f7570a9a458f236fdcb2032a7a58a9b1d0731`

```text
timeout 90 python3 -B reports/round-61/mutants/LINES.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### LINES/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/LINES.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=20 bad=['6:S652']
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### TOPIC/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC FAIL rows=20 bad=['S652']
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### TOPIC/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC`  
Counter SHA-256: `424944049da351fd1a1bc3bfb7c0d3ce07e2b09163da81cd75895f91c4b8c773`

```text
timeout 90 python3 -B reports/round-61/mutants/TOPIC.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### TOPIC/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/TOPIC.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/TOPIC
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC FAIL rows=20 bad=['S652']
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINK/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK FAIL min=3 bad=['6:2']
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINK/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK`  
Counter SHA-256: `9757beca1e5ada6fe845e927b48be6c45fd6e1e39b268c92f2e74e77e80b4d6a`

```text
timeout 90 python3 -B reports/round-61/mutants/LINK.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=2 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### LINK/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/LINK.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINK
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK FAIL min=3 bad=['6:2']
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### COPY/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY FAIL max=12 bad=['6:13']
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### COPY/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY`  
Counter SHA-256: `fc314827bf913ef96481cb9a78748bf81f66a93bd6e0657d6419415939383583`

```text
timeout 90 python3 -B reports/round-61/mutants/COPY.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=13 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### COPY/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/COPY.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/COPY
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY FAIL max=12 bad=['6:13']
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LOCATE/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=18 cited=20 need=20 at=2026-10-23T09:44Z not_located=['S652: http://127.0.0.1:48661/document quote-absent', 'S653: http://127.0.0.1:48661/document quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LOCATE/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE`  
Counter SHA-256: `fd00b78846042706198c45ab572f0ed4bb65cb28b74a8445f81f4a638afcc2cc`

```text
timeout 90 python3 -B reports/round-61/mutants/LOCATE.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=18 cited=20 need=18 at=2026-10-23T09:46Z not_located=['S652: http://127.0.0.1:48661/document quote-absent', 'S653: http://127.0.0.1:48661/document quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### LOCATE/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/LOCATE.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LOCATE
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=18 cited=20 need=20 at=2026-10-23T09:46Z not_located=['S652: http://127.0.0.1:48661/document quote-absent', 'S653: http://127.0.0.1:48661/document quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### FRESH/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### FRESH/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH`  
Counter SHA-256: `52a757a1c7d522990e7b6b0cd527c2789c20d358da77c9ccc0b4f36f41956389`

```text
timeout 90 python3 -B reports/round-61/mutants/FRESH.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
ACCEPT-C-61: PASS
exit=0
DETECTOR FAIL
```

### FRESH/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/FRESH.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/FRESH
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINES_TWO_IDS/frozen

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=20 bad=['6:S652,S653']
TOPIC PASS rows=20 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINES_TWO_IDS/mutated

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS`  
Counter SHA-256: `a1594c15f5c9b3aedd9aa2b5d2c57baee10ead45cbec0cfb26d9d6c75328ee80`

```text
timeout 90 python3 -B reports/round-61/mutants/LINES_TWO_IDS.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

### LINES_TWO_IDS/restored

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS`  
Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
timeout 90 python3 -B reports/round-61/mutants/LINES_TWO_IDS.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterC/fixtures/LINES_TWO_IDS
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=20 bad=['6:S652,S653']
TOPIC PASS rows=20 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
DETECTOR PASS
```

## Boundaries

No live built C entry was judged, no code was integrated or shipped, and no claimed-object acceptance run was performed. These are pre-data synthetic counter probes only. No tool installs or updates occurred. The only tooling issue encountered was the read tool treating a ranged internal documentation URL as a topic; it was reported through `xd://report_issue`, and the unranged documentation read succeeded.
