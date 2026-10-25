# Round-69 w2 residual verification — mutation probe of the O2 settlement harness

Seat: `L1Kotodama69.MutHarness` (mutation tester). Lane: `kotodama-shokunin`, round 69 attempt 2.
Scope: ALREADY-LANDED final measures. Read-only on the lane; all mutation work in a disposable clone.

| item | value |
|---|---|
| lane tip under test | `9e82c7b47651e0aba6ee05cc19770f78bf120cfd` (`9e82c7b`) |
| clone | `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/MutHarness-r69` |
| targets | `tools/check-settlement-fixture.py`, `tools/check-supersession-settlement.py` |
| O2 counter under test | `reports/round-69/accept-o.py` (sha256 `08c7ea61…f7547`) |
| detector set | D1 harness selftest · D2 `accept-o.py --root .` · D3 checker selftest (supplementary) |

## 1. Green baseline (before any mutation)

```
$ cd /tmp/MutHarness-r69
$ sha256sum tools/check-settlement-fixture.py tools/check-supersession-settlement.py
f7adb4ba52e0db1a1c20ee33a5b52a0e2288b287866493ed43d800967712f7f8  tools/check-settlement-fixture.py
05214b3d7618b47c7ff9c8d9127647b7b7832c0ed748b3271b0266c7f343ad74  tools/check-supersession-settlement.py

$ python3 -B tools/check-settlement-fixture.py --selftest
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3                                    (rc=0)

$ python3 -B reports/round-69/accept-o.py --root .
LEG PASS STAMP self=08c7ea6149a0 committed=08c7ea6149a0
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 pending=0 missing_paths=0
LEG PASS NEGCASE rc=0 pending=0 missing_paths=1
LEG PASS LANE rc=0 pending=0 missing_paths=0
LEG PASS NEGPROBE harness_on_counter_fixture rc=1 lane_lines=['LANE: pending=0 missing_paths=1']
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: PASS legs=7/7                       (rc=0)

$ python3 -B tools/check-supersession-settlement.py --selftest
PASS pending-detected / settled-active / settled-retired-closed / settled-split /
     ledger-clean / ledger-inconsistent-rejected / unreadable-exit-2
SELFTEST: 7/7                                    (rc=0)
```

Baseline confirmed. Every mutant below was applied alone to the pristine clone, all three
detectors were run, and the file was restored to its exact bytes before the next mutant.

## 2. Mutation table

`K` = killed (detector failed as it must), `S` = survived (detector green).
Baseline row is the control. Rows marked **gap** are survivors.

| # | assigned defect | file:line | patch (one line shown per mutant) | D1 harness selftest | D2 accept-o legs | D3 checker selftest | verdict |
|---|---|---|---|---|---|---|---|
| — | baseline | — | none | 3/3 rc0 | 7/7 rc0 | 7/7 rc0 | control |
| M1 | (a) drop missing-used-by detection | checker:164 | `missing_paths = []` | **FAIL** `fixture-negative … missing_paths=0` 2/3 rc1 | **FAIL** NEGCASE + NEGPROBE 5/7 rc1 | 7/7 rc0 | **K** |
| M2 | (b) always rc=0 (checker) | checker:167 | `return 0` | **FAIL** `fixture-pending rc=0 pending=1` 2/3 rc1 | 7/7 rc0 (blind) | **FAIL** `pending-detected` 6/7 rc1 | **K** (by D1 only) |
| M2b | (b) always rc=0 (harness) | harness:183 | `return 0` | 3/3 rc0 | 7/7 rc0 | 7/7 rc0 | **S — gap** |
| M3 | (c) hard-code summary (harness `LANE:` line) | harness:179‑180 | `print("LANE: pending=0 missing_paths=0")` | 3/3 rc0 | **FAIL** NEGPROBE `lane_lines=['LANE: pending=0 missing_paths=0']` 6/7 rc1 | 7/7 rc0 | **K** |
| M4 | (d) skip malformed-row branch | checker:85 | `if False and len(c) != 11:` | 3/3 rc0 | 7/7 rc0 | 7/7 rc0 | **S — gap** |
| M5 | (e) invert active-state classification | checker:127 | `… and not s_used and t_st == "queued"` | **FAIL** green + negative 1/3 rc1 | **FAIL** FIXTURE, NEGCASE, LANE(`pending=30`) 4/7 rc1 | **FAIL** `settled-active` 6/7 rc1 | **K** |
| M6 | (e) swap closed↔retired labels | checker:123‑126 | bodies exchanged | 3/3 rc0 | 7/7 rc0 | 7/7 rc0 | **S — gap** |
| M7 | harness negative-case assertion weakened | harness:128 | drop `and s["missing_paths"] == 1` | 3/3 rc0 | 7/7 rc0 | 7/7 rc0 | **S — gap** |
| M8 | (c) hard-code summary (checker `SETTLEMENT:` line) | checker:165‑166 | `pending=0 … missing_paths=0` | **FAIL** negative + pending 1/3 rc1 | **FAIL** NEGCASE + NEGPROBE 5/7 rc1 | 7/7 rc0 | **K** |

Score: **5 killed / 9 mutants; 4 survivors** (M2b, M4, M6, M7).

## 3. Per-mutant evidence (output tails)

### M1 — drop missing-used-by detection (killed)
`tools/check-supersession-settlement.py:164`
```diff
-    missing_paths = [p for _, p in stale if not os.path.exists(os.path.join(root, p))]
+    missing_paths = []
```
```
D1: FAIL fixture-negative rc=0 pending=0 missing_paths=0   FIXTURE: 2/3  rc=1
D2: LEG FAIL NEGCASE rc=0 pending=0 missing_paths=0
    LEG FAIL NEGPROBE harness_on_counter_fixture rc=1 lane_lines=['LANE: pending=0 missing_paths=0']
    ACCEPT-O-69: FAIL legs=5/7  rc=1
D3: SELFTEST: 7/7 (survives — no missing-path fixture in the checker's own battery)
```

### M2 — checker always exits 0 (killed by D1 only; **accept-o is blind**)
`tools/check-supersession-settlement.py:167`
```diff
-    return 1 if pending else 0
+    return 0
```
```
D1: FAIL fixture-pending rc=0 pending=1 missing_paths=0   FIXTURE: 2/3  rc=1
D2: ACCEPT-O-69: PASS legs=7/7  rc=0      <-- no accept-o leg requires the checker to exit non-zero on pending
D3: FAIL pending-detected   SELFTEST: 6/7  rc=1
```
The O2 counter never asserts a negative exit code from `--scan`; LANE asserts `rc==0` on a clean
lane, NEGCASE/NEGPROBE read the summary only. Only the harness's `fixture-pending` case catches this.

### M2b — harness always exits 0 (**survivor, gap**)
`tools/check-settlement-fixture.py:183`
```diff
         if s["pending"] or s["missing_paths"]:
             rc = 1
-    return rc
+    return 0
```
```
D1: FIXTURE: 3/3 rc=0 · D2: ACCEPT-O-69: PASS legs=7/7 rc=0 · D3: 7/7 rc=0
```
Controlled probe, identical input (`/tmp/mh-negfx`, missing_paths=1), identical stdout:
```
$ python3 -B tools/check-settlement-fixture.py --root /tmp/mh-negfx
LANE: pending=0 missing_paths=1
pristine rc=1   mutated rc=0
```
Kill condition absent: NEGPROBE stores `rc` only inside its detail string and never asserts it;
the harness selftest never inspects its own process exit code.

### M3 — harness hard-codes the LANE summary (killed)
`tools/check-settlement-fixture.py:179-180`
```diff
-        print("LANE: pending=%d missing_paths=%d" % (
-            s["pending"], s["missing_paths"]))
+        print("LANE: pending=0 missing_paths=0")
```
```
D1: FIXTURE: 3/3 rc=0
D2: LEG FAIL NEGPROBE harness_on_counter_fixture rc=1 lane_lines=['LANE: pending=0 missing_paths=0']
    ACCEPT-O-69: FAIL legs=6/7 rc=1
```
Killed by NEGPROBE — exactly the leg revision 1 was added for.

### M4 — malformed-row branch skipped (**survivor, gap**)
`tools/check-supersession-settlement.py:85`
```diff
-        if len(c) != 11:
+        if False and len(c) != 11:
```
```
D1: FIXTURE: 3/3 rc=0 · D2: ACCEPT-O-69: PASS legs=7/7 rc=0 · D3: SELFTEST: 7/7 rc=0
```
Behavioural probe (9-cell registry row, same file, both builds):
```
mutant : ValueError: not enough values to unpack (expected 11, got 9)  -> traceback, no SETTLEMENT line, rc=1
pristine: SETTLEMENT: pending=0 chains=0 usedby_paths=0 missing_paths=0  rc=0
```
No fixture in D1, D2 or D3 contains a malformed row (all fixture registries are 11-cell; the live
lane registry has 783 rows, 0 malformed). The defect is real (crash on a truncated row) and unobserved.

### M5 — inverted active-state classification (killed)
`tools/check-supersession-settlement.py:127`
```diff
-        elif s_st == "mined" and s_used and t_st == "queued":
+        elif s_st == "mined" and not s_used and t_st == "queued":
```
```
D1: FAIL fixture-green rc=1 pending=1; FAIL fixture-negative rc=1 pending=1   FIXTURE: 1/3  rc=1
D2: LEG FAIL FIXTURE / NEGCASE / LANE (LANE: pending=30 missing_paths=0)  ACCEPT-O-69: FAIL legs=4/7 rc=1
D3: FAIL settled-active   SELFTEST: 6/7
```
This is the state-machine inversion an operator would actually write, and every layer sees it.

### M6 — closed/retired labels swapped (**survivor, gap**)
`tools/check-supersession-settlement.py:123-126`
```diff
         if t_st == "rejected":
-            cls = "settled-closed"
+            cls = "settled-retired"
         elif s_st == "rejected":
-            cls = "settled-retired"
+            cls = "settled-closed"
```
```
D1: 3/3 rc0 · D2: ACCEPT-O-69: PASS legs=7/7 rc0 · D3: SELFTEST: 7/7 rc0
lane label counts, pristine : SETTLED-CLOSED 12 / SETTLED-RETIRED 4
lane label counts, mutated   : SETTLED-CLOSED  4 / SETTLED-RETIRED 12
```
16 live chains are mislabelled and no leg notices, because every detector asserts only the
`pending` count (and, in the checker selftest, `rc==0` for the combined retired/closed fixture).

### M7 — harness negative assertion weakened (**survivor, gap**)
`tools/check-settlement-fixture.py:128`
```diff
-        ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 1
+        ok = s is not None and s["pending"] == 0
```
```
D1: FIXTURE: 3/3 rc=0 · D2: ACCEPT-O-69: PASS legs=7/7 rc=0
```
Discriminating probe (both harness builds against a do-nothing checker that prints
`SETTLEMENT: pending=0 … missing_paths=0` and exits 0):
```
pristine harness vs do-nothing checker : PASS green, FAIL negative, FAIL pending   1/3 rc=1
M7       harness vs do-nothing checker : PASS green, PASS negative (wrong), FAIL pending  2/3 rc=1
```
The weakening is invisible to D1/D2 because the counter's NEGPROBE builds its own fixture and the
counter's selftest spoofs the *harness file*, not the checker behind it.

### M8 — checker hard-codes the SETTLEMENT summary (killed)
`tools/check-supersession-settlement.py:165-166`
```diff
-    print(f"SETTLEMENT: pending={len(pending)} chains={len(chains)} "
-          f"usedby_paths={len(stale)} missing_paths={len(missing_paths)}")
+    print(f"SETTLEMENT: pending=0 chains={len(chains)} "
+          f"usedby_paths={len(stale)} missing_paths=0")
```
```
D1: FAIL fixture-negative (missing_paths=0) + FAIL fixture-pending (pending=0)   FIXTURE: 1/3 rc=1
D2: LEG FAIL NEGCASE; LEG FAIL NEGPROBE   ACCEPT-O-69: FAIL legs=5/7 rc=1
D3: SELFTEST: 7/7 (survives — the checker battery checks rc, not the printed numbers)
```

## 4. Gaps (mutations no leg kills) — exact patches

1. **M2b — harness exit code is unasserted.**
   `tools/check-settlement-fixture.py:183`: `return rc` → `return 0`.
   Nothing in D1/D2 asserts the harness's rc on a dirty `--root` scan (NEGPROBE greps the `LANE:`
   line and discards rc). A harness that always exits 0 still declares `missing_paths=1` in text.
2. **M4 — malformed-row handling is untested.**
   `tools/check-supersession-settlement.py:85`: `if len(c) != 11:` → `if False and len(c) != 11:`.
   Every fixture registry in all three batteries is 11-cell; a 9-cell row turns the scanner into an
   uncaught `ValueError` traceback with no summary line.
3. **M6 — settled-closed / settled-retired labels are unasserted.**
   `tools/check-supersession-settlement.py:123-126` (bodies swapped). All detectors assert only
   `pending`; 12 CLOSED + 4 RETIRED live chains flip labels with no failure.
4. **M7 — the harness's own negative assertion is unasserted.**
   `tools/check-settlement-fixture.py:128` (drop `and s["missing_paths"] == 1`).
   No detector exercises the real harness against a spoofed *checker*; accept-o's selftest spoofs
   the harness itself (SPOOF_HARNESS), so the real harness's assertions are never the subject.
5. **Related accept-o hole (not a survivor, a detection gap):** M2 (checker always rc=0) leaves
   `accept-o.py` at 7/7 PASS. No accept-o leg requires `--scan` to exit 1 on a pending chain;
   only the harness's `fixture-pending` case enforces it. If the harness case were also weakened
   (M7-style), the rc contract would be completely unguarded.

## 5. Restoration evidence

Every mutant was reverted with the inverse edit; the byte check after each revert matched the
pristine hash (recorded immediately after the mutant run, before the next mutant).

| file | pristine sha256 (before) | after all mutants | git status |
|---|---|---|---|
| `tools/check-settlement-fixture.py` | `f7adb4ba…12f7f8` | `f7adb4ba…12f7f8` | clean |
| `tools/check-supersession-settlement.py` | `05214b3d…43ad74` | `05214b3d…43ad74` | clean |

Mutant-by-mutant file states observed (sha256 prefix), each restored before the next:

| mutant | mutated file hash | restored? |
|---|---|---|
| M1 | `a814e180…be66916` | yes |
| M2 | `f12aba65…216ce8b0d` | yes |
| M2b | `c1ddabd8…a0e16f` | yes |
| M3 | `cd7a1b01…f52fdd` | yes |
| M4 | `0650424c…555a000` | yes |
| M5 | `10e920bd…b16c92b7` | yes |
| M6 | `190f0a95…ed47df27` | yes |
| M7 | `688f8710…d4062451` | yes |
| M8 | `772e2aea…fc16c70` | yes |

`git status --porcelain` in `/tmp/MutHarness-r69` → 0 lines after the last revert.

Restored control (post-mutation, pristine bytes), re-run in full:

```
$ python3 -B tools/check-settlement-fixture.py --selftest
PASS fixture-green / fixture-negative / fixture-pending      FIXTURE: 3/3      rc=0
$ python3 -B reports/round-69/accept-o.py --root .
ACCEPT-O-69: PASS legs=7/7                                   rc=0
$ python3 -B tools/check-supersession-settlement.py --selftest
SELFTEST: 7/7                                                rc=0
$ python3 -B tools/check-settlement-fixture.py --root /tmp/mh-negfx
LANE: pending=0 missing_paths=1                              rc=1   (rc contract restored)
```

## 6. Verdict — is the harness mutation-effective?

**FAIL (partial).** 5 of 9 mutants killed; **4 survive**.

| assigned class | mutant | verdict |
|---|---|---|
| (a) drop missing-used-by detection | M1 | PASS — killed by D1 `fixture-negative`, D2 `NEGCASE`+`NEGPROBE` |
| (b) always rc=0 | M2 (checker) | PASS — killed by D1 `fixture-pending` (D2 blind) |
| (b) always rc=0 | M2b (harness) | **FAIL — unkilled** |
| (c) hard-code pending=0 missing_paths=0 | M8 (checker) / M3 (harness) | PASS — killed by D1, and by D2 `NEGPROBE` |
| (d) skip malformed-row branch | M4 | **FAIL — unkilled (no leg at all)** |
| (e) invert state classification | M5 (active) | PASS — killed by D1/D2/D3 |
| (e) invert state classification | M6 (closed↔retired labels) | **FAIL — unkilled** |
| harness's own negative assertion | M7 | **FAIL — unkilled** |

What the detectors are actually strong at: the round-68 defect class (a missing used-by file) and
fabricated summaries on the checker's `SETTLEMENT:` line are triple-covered; a harness that lies
in its `LANE:` line is caught by `NEGPROBE`. The holes are uniform: **nothing asserts labels
other than `pending`, nothing asserts the harness's exit code, and no fixture ever feeds a
malformed registry row.** No contract was changed by this probe; the survivors are coverage
findings only.

Files touched: this report is the only lane write. All mutation work was confined to
`/tmp/MutHarness-r69` (pristine hashes above) and `/tmp/mh-negfx`, `/tmp/mh-spoofchk` (throwaway
probe fixtures). No tool installs were needed.
