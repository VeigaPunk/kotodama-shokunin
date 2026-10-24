# MutCounterC — ACCEPT-C-67 counter mutation probe (r67, w1)

**Seat:** mutation tester, claim C instrument. **Target attacked:**
`reports/round-67/accept-c.py` (frozen rev0, sha256
`3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5`).
**Claim attacked:** C — "every leg of accept-c.py prints PASS" cannot distinguish a
sound instrument from a weakened one; six one-line guard removals each make the
predicate accept a defect it must reject.

**The real counter was never touched.** All mutants are copies under
`.ufo/waves/round-67/stage/mut-c/`. No lane git/jj write was issued; every git
write (add/commit --amend/reset) happened inside a private scratch clone that
was a `cp -a` of the pre-existing `.scratch/eval-base` (base `ad5b52b0…`),
removed after the probe.

## Method (why the runs are meaningful)

`accept-c.py` has no selftest, and at base every data leg fails, so a bare
base run cannot distinguish a mutant from the original (both FAIL). I therefore
built a synthetic **all-legs-PASS fixture** in the private clone
(`stage/mut-c/build_fixture.py`): synthetic entry
`corpus/knowledge/culture-material/medicine-healing-codes.md`, 24 synthetic
rows `S805–S828` on `medharnessNN.example.org` with matching archive captures,
README row + header/totals/footer updated so `sweep.py` is green. Fixture
commit `F=1453811c9e65443820852e1ceb4f1379d2d1736d`, clean tree.

* **Baseline / specificity:** pristine counter on clean fixture bytes →
  `ACCEPT-C-67: PASS`, exit 0 (all 15 legs PASS). All six mutants run on the
  same clean bytes → `ACCEPT-C-67: PASS` too, i.e. no mutant is a
  reject-everything mutant; each weakens exactly one guard.
* **Detection (per mutant):** reset the clone to `F`, plant one defect that the
  guard exists to catch, commit it (`--amend`), then run **pristine** and
  **mutant** on the identical bytes with the identical `--lands`.
* **Verdict rule:** `SURVIVED` = pristine rejects the defect on that leg but the
  mutant passes it. `killed` = mutant still rejects. `INCONCLUSIVE` = pristine
  did not reject (fixture defect, not a finding).

Evidence files: `stage/mut-c/results.txt` (full stdout of all 12 runs + planted
defect patches), `results.json`, `mutants.diff` (the six one-line diffs).

## Mutants, defects, verdicts

| # | mutant file (sha256) | one-line change | leg | planted defect | pristine | mutant | verdict |
|---|---|---|---|---|---|---|---|
| m1 | `m1_oneid_ge1.py` `a3f57c23…` | `if count != 1:` → `if count < 1:` | ONEID | extra bullet citing `(S805)` a second time | `ONEID FAIL` (S805:citations=2) | `ONEID PASS` | **SURVIVED** (leg-local) |
| m2 | `m2_restate_inq_lt2.py` `1906d956…` | `if inq < 3 or cov >= 0.8` → `if inq < 2 or cov >= 0.8` | RESTATE | S805 bullet restates only 2 quote words in order | `RESTATE FAIL` (quote_words=2) | `RESTATE PASS` | **SURVIVED**, `ACCEPT-C-67: PASS` |
| m3 | `m3_append_unbounded.py` `ace35d44…` | `append_ok = … and not extra_ids and …` → drop `not extra_ids` | APPEND | smuggled extra row `S900` appended | `APPEND FAIL` (extra=['S900']) | `APPEND PASS` | **SURVIVED**, `ACCEPT-C-67: PASS` |
| m4 | `m4_capture_skipped.py` `06544038…` | `leg("CAPTURE", not cap_bad` → `leg("CAPTURE", True` | CAPTURE | S805 source cell loses its `web.archive.org/…id_/` capture | `CAPTURE FAIL` (S805:no_capture) | `CAPTURE PASS` | **SURVIVED**, `ACCEPT-C-67: PASS` |
| m5 | `m5_stamp_equal_dropped.py` `75b6e518…` | `stamp_ok = … and mv_rev == lands and …` → drop the equality | STAMP | none in data: `--lands ad5b52b0…` while clone main is the fixture commit (moved worktree) | `STAMP FAIL equal=False` → early `return 1` | `STAMP PASS stamped=ad5b52b0 evaluated=499815c1 equal=False` → `ACCEPT-C-67: PASS` | **SURVIVED**, full PASS |
| m6 | `m6_rows_tier_c.py` `d9cb8713…` | `if c[3] not in ("A", "B")` → `("A", "B", "C")` | ROWS | S805 tier `A` → `C` (tier inflation) | `ROWS FAIL` (S805:tier='C') | `ROWS PASS` | **SURVIVED**, `ACCEPT-C-67: PASS` |

Diffs (verbatim, `stage/mut-c/mutants.diff`):

```diff
-        if count != 1:                                   # m1
+        if count < 1:
-        if inq < 3 or cov >= 0.8 or not novel:            # m2
+        if inq < 2 or cov >= 0.8 or not novel:
-    append_ok = not missing_old and not extra_ids and not mutable_bad   # m3
+    append_ok = not missing_old and not mutable_bad
-    leg("CAPTURE", not cap_bad, f"bad={cap_bad[:8]}")    # m4
+    leg("CAPTURE", True, f"bad={cap_bad[:8]}")
-        and mv_rev == lands and bool(re.fullmatch(...))   # m5
+        and bool(re.fullmatch(...))
-            if c[3] not in ("A", "B"):                    # m6
+            if c[3] not in ("A", "B", "C"):
```

## Findings (coverage, not a contract change)

1. **6/6 mutants survived.** Every guard in the C predicate — citation
   cardinality, quote restatement depth, append boundedness, capture/target
   equality, `evaluated == stamped`, tier A/B — is load-bearing *only when
   someone tests it*. `accept-c.py` carries no negative controls, so a
   weakened counter is still a counter that prints PASS.
2. **Five of six mutants print the full green line on bytes carrying a planted
   defect** (`m2`–`m6` above), i.e. shortcut classes the wave is asked to
   police — duplicate/absent citation, shallow restatement, unbounded append
   (fabricated rows), missing archive capture, stale/moved-worktree lands,
   tier inflation — all become undetectable under a one-token guard removal.
3. **The r66 fix itself holds.** Under the frozen counter the moved-worktree
   case (`m5`'s defect, no counter mutation) is caught at STAMP with
   `equal=False` before any data leg runs; the mutant that drops only the
   equality prints `ACCEPT-C-67: PASS` with `stamped=ad5b52b0
   evaluated=499815c1`. The frozen instrument is correct here; the exposure is
   mutation of the instrument, not of its inputs.
4. **Mitigation already in the contract, and its limit.** Each run prints
   `# counter sha256 (self)`; mutant runs printed `a3f57c23…`,
   `1906d956…`, `ace35d44…`, `06544038…`, `75b6e518…`, `d9cb8713…`, while
   every pristine run printed the frozen `3e5f1a58…`. So a substituted counter
   is visible *if the receipt's counter sha is checked against the frozen
   value*. Recommendation for the L1 (coverage finding, not a predicate edit):
   either add these six negative controls as an `--selftest` block in rev1 of
   accept-c (the O counter already owes 14/14 selftest), or gate the C receipt
   on `counter sha256 == 3e5f1a58…`.
5. Fixture caveat: the fixture is synthetic and exists only to make legs
   reachable; it is not evidence for claim C and no real corpus row was
   invented.

## Cross-counter id bound — verified, and the L1 ruling holds (design finding)

CriticFrontier's r67-w1 alert is **correct at the code/claims level**: `accept-c.py`
binds appended ids to `NEW_IDS ∪ EXTRA_IDS` (`EXTRA_IDS = {S801,S802,S803,S804}`,
line 70; `allowed_new` line 357), while `accept-ca.py` D4 requires
`rej_opened_today >= len(R66_REJECTS) + 2` (lines 226-235) — any `S829+` reject
row in the same registry tip makes C's APPEND print `extra=['S829', …]`. The
frozen claims say the same on their face: C's APPEND leg text reads "additions
bounded to S805-S828 + disposition ids S801-S804", Ca's D4 wants ">=2 rejected
rows opened 2026-10-24" on top of S801-S804. **L1's resolution is per-claim
lands separation (A_r → A_c → A_ca), not a predicate or claims revision**, and
that dissolves the conflict: at A_c only S805-S828 (+ S801-S804) are appended.

I measured the residual hazard the ruling implies — the C receipt is
**lands-specific** and a re-run at A_ca is a false FAIL. Frozen counter, same
fixture data, one extra rejected `S829` row appended (A_ca-like commit):

```
STAMP PASS stamped=1f216d59 evaluated=1f216d59 equal=True
APPEND FAIL missing_old=[] appended=25 extra=['S829'] immutable_violations=[]
ACCEPT-C-67: FAIL
```

Every other leg PASS, so the only delta is the APPEND bound (`stage/mut-c/lands-specificity.txt`).
Consequence for integration: the C receipt must be taken at A_c and never
re-run at A_ca; the receipt's `stamped/evaluated` headers make that explicit,
and interpreting a later re-run belongs to the post-records topo/traceability
step, not to a fresh C verdict. This is a design finding, not a contract change
— no counter, claim or bounds were edited.

## Restoration evidence

* Pristine counter copy `stage/mut-c/accept-c.orig.py` sha256 =
  `3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5` **before**
  and **after** the probe (identical to the lane file, re-hashed at the end of
  `run_mutants.py` and by hand).
* The clone was reset to fixture commit `F` after the last probe, then removed
  (`du 173M` freed). Rebuild recipe: `cp -a .scratch/eval-base stage/mut-c/repoc
  && python3 stage/mut-c/build_fixture.py repoc && python3
  stage/mut-c/run_mutants.py`.
* Lane repo untouched by me: `reports/round-67/accept-c.py` unchanged, no lane
  git/jj writes, no lane index writes; my only working-tree additions are
  untracked files under `.ufo/waves/round-67/`.

## Seat artifacts

`stage/mut-c/`: `m1_oneid_ge1.py`, `m2_restate_inq_lt2.py`,
`m3_append_unbounded.py`, `m4_capture_skipped.py`, `m5_stamp_equal_dropped.py`,
`m6_rows_tier_c.py`, `accept-c.orig.py` (pristine copy), `mutants.diff`,
`results.txt`, `results.json`, `lands-specificity.txt` (A_c vs A_ca-like re-run),
`build_fixture.py`, `run_mutants.py`.
No tools installed; no network used.

Report: .ufo/waves/round-67/w1/MutCounterC.md
