# ExecCounterSmokeO — smoke + mutation + attack of ACCEPT-O-67

Seat: L1-kotodama-r67.ExecCounterSmokeO (leaf, attack). Time-boxed.
Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated; read-only use).
Lane tip at probe time: `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21`, base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`.
No lane file was mutated; all fixtures were built in `/tmp` (`/tmp/oattack3-*`, `/tmp/o-dirty`). Untracked lane state at probe time was only `.ufo/waves/round-66/`, `.ufo/waves/round-67/rows/`, `.ufo/waves/round-67/w1/`.

## Files changed
- This report only. No tool, counter, registry or corpus bytes touched.

## Verdicts (observed)
| Probe | Result |
|---|---|
| `tools/check-receipt-seq.py --root . --selftest` | **14/14, rc=0** |
| 5 committed mutants under `.ufo/waves/round-67/stage/mut-o/` | each **13/14, rc=1**, exactly the pinned check FAILs, nothing else |
| `accept-o.py` on base clone (`--lands ad5b52b`) | **FAIL, rc=1** — reproduces `telemetry/dry-run-o.txt` leg-for-leg, same counter sha `f21e9b43` |
| `accept-o.py` on live tree (`--lands b78f8b8`) | **ACCEPT-O-67: PASS, rc=0**, 10/10 legs, 3.0 s |
| Adversarial `--topo` over r66 receipts (assignment expectation: all PASS) | **FAIL, rc=1** — see finding 1 |
| Adversarial `--topo` over r67 dry-run receipts | **PASS, rc=0** |

## 1. Headline: the requested r66 `--topo` run does NOT pass at tip
Command (exactly as assigned):
```
python3 -B tools/check-receipt-seq.py --root . --topo \
  reports/round-66/telemetry/final-measures-c.txt \
  reports/round-66/telemetry/final-measures-o.txt \
  reports/round-66/telemetry/final-measures-ca.txt
```
Observed (rc=1):
```
SEQ-reports/round-66/telemetry/final-measures-c.txt FAIL missing_headers=['stamped', 'evaluated']
SEQ-...-o.txt FAIL missing_headers=['stamped', 'evaluated']
SEQ-...-ca.txt FAIL missing_headers=['stamped', 'evaluated']
TOPO-...-c.txt FAIL no_stamp_header
TOPO-...-o.txt FAIL no_stamp_header
TOPO-...-ca.txt FAIL no_stamp_header
RECEIPT-SEQ: FAIL
```
Cause is content, not drift: `git status --porcelain` shows no tracked modification, and the r66 receipts **as committed at their carrier `4589ebdd`** carry only three headers:
```
# counter sha256 (self): 987c4bbc…
# measured revision (lane main): 65fe8572822ef83f1750593af77daddf34a1e337
# tree: f0681e6ea5bc4d4e1e2a93b42ea460a739358887
```
`grep -cE '^# (stamped|evaluated) revision:'` = **0** for r66 receipts, **2** for the r67 dry-run receipts. The r66 protocol predates stamped/evaluated; the tool's design ("a receipt missing a header line is a FAIL, not a skipped check") therefore rejects all three **before** topology runs.

Consequence for claim O wording: `ACCEPT-O-67`'s `R66` leg PASSes on these same files (observed: `R66 PASS bad=[] carrier=4589ebdd parent_of=65fe8572`) because that leg is a hand-rolled regex over `measured revision (lane main)` plus `git log -1`, **not** a call into the tool. That is consistent with the claim text ("--topo-equivalent derivation"), but the claimed re-derivation is not exercised by the tool on the r66 corpus. **Any `post-records.txt` generated from the r66 receipts will record `RECEIPT-SEQ: FAIL` and cannot serve as the commanded green evidence.** Generate it from the r67 receipts:

## 2. The r67 dry-run receipts are fully green at tip (recommended post-records input)
```
python3 -B tools/check-receipt-seq.py --root . --topo \
  reports/round-67/telemetry/dry-run-c.txt:reports/round-67/accept-c.py \
  reports/round-67/telemetry/dry-run-o.txt:reports/round-67/accept-o.py \
  reports/round-67/telemetry/dry-run-ca.txt:reports/round-67/accept-ca.py
```
Observed rc=0: `SEQ…PASS` (all three `stamped=evaluated=measured=ad5b52b0`), `TREE…PASS recorded=de353b04 actual=de353b04` ×3, `SHA…PASS` (recorded `3e5f1a58`/`f21e9b43`/`5e8915ac` == actual, i.e. the committed counters), `TOPO…PASS carrier=b78f8b8e parent=ad5b52b0 stamped=ad5b52b0` ×3, `RECEIPT-SEQ: PASS`.
Note the pairing form `receipt:counter` is what makes the SHA pin evaluate at all (see finding 5).

## 3. Mutant matrix — exactly as pinned, no over-kill
Live-tool selftest: `SELFTEST: 14/14`, rc=0. Each mutant is a **one-line** byte mutant of `tools/check-receipt-seq.py` (`diff -u`, one `-`/`+` pair each):

| mutant | one-line change | selftest | FAIL lines |
|---|---|---|---|
| `mut1_equality_always_true.py` | `eq = (stamped==evaluated==measured)` → `eq = True` | 13/14, rc=1 | `FAIL moved-receipt-fail … equal=True` only |
| `mut2_parent_always_true.py` | `seq.leg(..., parent == h["stamped"], ...)` → `True` | 13/14, rc=1 | `FAIL topo-wrong-parent-fail …` only |
| `mut3_missing_headers_ok.py` | missing-header leg `False` → `True` | 13/14, rc=1 | `FAIL missing-headers-fail …` only |
| `mut4_no_carrier_pass.py` | `no_carrier` leg `False` → `True` | 13/14, rc=1 | `FAIL topo-no-carrier-fail …` only |
| `mut5_tree_unchecked.py` | `actual = rev_parse(stamped^{tree})` → `actual = h["tree"]` | 13/14, rc=1 | `FAIL tree-mismatch-fail … recorded=ffffffff actual=ffffffff` only |

This matches `accept-o.py` `MUT_EXPECT` exactly (one expected FAIL each, zero extra). `MUT PASS mutants=5 bad=[]` on the live run. The mutants also demonstrate the intended kill direction: mut3/mut4 print PASS text in the inner fixture (`SEQ-tools/counter-x.py PASS missing_headers=[…]`, `TOPO-…never.txt PASS no_carrier`) — i.e. the fixtures would have been fooled, and only the selftest assertion catches it.

## 4. Counter smoke: base clone vs live tree
Base clone (`.scratch/eval-base` @ `ad5b52b0`, `--lands ad5b52b0`) — rc=1, STAMP PASS, `SELFTEST/DIFF/OPTIONS/LANDS/TOPO/HEADERS/MUT` FAIL, `R66 PASS`, `FIXTURES PASS lanes=2 wall=0.1s`, `ACCEPT-O-67: FAIL`. Byte-identical shape to the frozen `telemetry/dry-run-o.txt` (same `# counter sha256 (self): f21e9b43…`), so the committed control is reproducible.
Live tree (`--root . --lands b78f8b8`) — rc=0:
```
STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e dirty_tracked=False
SELFTEST PASS exit=0 count=True           DIFF PASS diff_lines=1 status=A
OPTIONS PASS missing=[]                   LANDS PASS exit=1 moved_flag=True
TOPO PASS healthy=0 wrong=1               HEADERS PASS bare=1 moved=1
MUT PASS mutants=5 bad=[]                 R66 PASS bad=[] carrier=4589ebdd parent_of=65fe8572
FIXTURES PASS lanes=2 wall=3.0s           ACCEPT-O-67: PASS
```
The do-nothing control is dead and the real predicate is reachable — as claimed.

## 5. Attacks that SUCCEEDED against the instrument (name, evidence, class)
All fixtures are isolated `/tmp` repos; none touch the lane.

**(a) `--lands` counter-sha pin reads the mutable worktree — rc=0 false PASS.**
Receipt committed **at** lands `B`, declaring `# counter sha256 (self): 7b929435…` where `7b929435…` is the sha of counter text that was **never committed**; the counter committed at `B` hashes to `aa699289…`; the worktree copy holds the never-committed text. Result:
```
LANDS PASS lands=8598fd5d head=8598fd5d moved_past=False
SEQ-telemetry/b.txt PASS … equal=True
TREE-telemetry/b.txt PASS recorded=2adbba96 actual=2adbba96
SHA-telemetry/b.txt PASS tools/counter.py recorded=7b929435 actual=7b929435
RECEIPT-SEQ: PASS                                  (rc=0)
```
Source: `check_counter_sha` calls `read_worktree` first and only falls back to `read_rev(main)`; it never uses the `--lands` revision. This directly contradicts the module docstring "**--lands mode reads committed bytes only**" and `claims.json` receipt_protocol ("committed bytes, never a moved worktree"). Attack class: false stamp / mutable-bytes bypass. Fix direction: in `--lands` mode read the counter via `read_rev(lands, cpath)`; worktree read only in default mode.

**(b) `--lands` accepts a stamped revision that is NOT an ancestor of lands — rc=0 false PASS.**
lands tip `1c177cc8`; receipt stamps `4462279f`, an empty commit on a **side branch** (`git merge-base --is-ancestor 4462279f 1c177cc8` → false) that merely shares the tree. Observed `--lands 1c177cc8` → `SEQ PASS`, `TREE PASS recorded=9572f38f actual=9572f38f`, `SHA PASS`, `RECEIPT-SEQ: PASS`, rc=0. The same receipt under `--topo` correctly FAILs (`TOPO-… FAIL carrier=1c177cc8 parent=09d223f2 stamped=4462279f`). Since the frozen counters are graded at lands and carrier-parentage is deliberately post-records evidence, a mis-stamped lands claim of this shape is invisible to the frozen run and only dies in post-records. Attack class: fabricated anchor / non-ancestor stamp. Fix direction: assert `merge-base --is-ancestor <stamped> <lands>` in `--lands` mode.

**(c) Counter-sha pin is silently skipped when no counter is paired — fabricated sha passes.**
Receipt with `# counter sha256 (self): 000…0` (64 zeros), committed, run as `--topo telemetry/c.txt` → `SEQ PASS`, `TREE PASS`; **no `SHA-` line is printed at all** (`if not cpath or not h["counter_sha"]: continue`). The run only failed for an unrelated carrier reason. Attack class: bypass by omission. Practical impact: the `claims.json` note describes `post-records.txt` as "`--topo` over the three receipts + itself"; if the counters are not named, the round's counter-sha pins are unverified. Use the `receipt:counter` form (finding 2).

**(d) `pair_args` positional footgun.** A bare second argument is a counter **iff** it ends in `.py`; therefore `… --topo r1.txt r2.txt r3.txt tools/check-receipt-seq.py` silently pairs `tools/check-receipt-seq.py` as **r3's** counter, and any `.txt` second argument is silently treated as another receipt. Nothing is reported when a declared `# counter sha256 (self)` has no counter to check — same silent-skip class as (c).

**(e) The frozen counter itself certifies a dirty worktree — `ACCEPT-O-67: PASS` with `dirty_tracked=True`.**
Isolated `git clone --no-local` of the lane at `b78f8b8`, appended one uncommitted line to `tools/check-receipt-seq.py`, then ran the committed `accept-o.py --lands b78f8b8`:
```
# tree: e5bf3a7e802f8bef40fbc68c63bb9662a7145172
# worktree dirty (tracked): True
STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e dirty_tracked=True
SELFTEST PASS … DIFF PASS status=A … OPTIONS PASS … MUT PASS … R66 PASS … ACCEPT-O-67: PASS  (rc=0)
```
Source-derived: `stamp_ok` is `regex(mv_rev) and mv_rev == lands and regex(tree_rev)`; `dirty_flag` is printed but **not** in `stamp_ok`, and `SELFTEST`/`DIFF`/`OPTIONS` read worktree bytes (`root/TOOL`) rather than `git show lands:TOOL`. So the receipt's `# measured revision` + `# tree` attest a commit, while the graded artifact can be uncommitted. The materialized-clone discipline is what saves the real run (the committed control and the live run both show `dirty_tracked=False`), but **no leg enforces it**; the same holds for the counter's own self-sha (recorded, never compared to committed bytes). Attack class: moved/dirty worktree PASS claim — the exact r65/r66 rejection class, relocated to the counter.

**(f) Source-derived, not separately exercised:** `parse_header` takes the **first** match per key, so duplicate `# tree:` / `# stamped revision:` lines are never rejected — a receipt can carry contradictory declarations and pass on the first. Low severity for committed receipts (audited by eye) but it is a text-shadowing hole in a checker whose job is header integrity.

## 6. Residual instrument risk on the MUT leg
`accept-o.py`'s MUT leg is a **stdout text match**: it requires rc=1, `FAIL <pinned>` present, and zero other `^FAIL\s+(\S+)` lines. A mutant that printed `FAIL moved-receipt-fail` from fixture output and exited 1 without breaking the predicate would be certified. Today the five committed mutants are honest one-line sabotages (verified by diff) and the extra-FAIL scan covers the realistic over-kill case; the risk is the certificate being textual, not semantic. No action required for this round; worth a note in the lesson file.

## 7. What I did not verify (named, not hidden)
- No build/lint/test/formatter gates run (wave rule; parent owns post-integration).
- Did not run the mutants against a mutated *copy of the fixtures* (only against the committed selftest fixture set).
- Did not audit `accept-ca.py`'s SEQ leg reading of this tool (sibling seats own Ca).
- Did not test `--lands` where `main` has moved past lands and a receipt changed in an intermediate commit (the `moved_past=True` flag is reported, but I did not construct a receipt-mutating middle commit).

## 8. Tooling / installs
None. Only `git`, `python3` (stdlib), `diff` — all preinstalled. No pacman/uv/npm transactions.

## 9. C-APPEND vs Ca-D4: same-commit conflict is real, empirically confirmed; satisfiable only under per-claim lands sequencing
Raised by CriticFrontier during my run; L1 resolved by sequencing (no counter revision). Verified from the frozen sources and by direct execution:
- `accept-c.py:70` `EXTRA_IDS = {"S801","S802","S803","S804"}`; `:357` `allowed_new = set(NEW_IDS) | EXTRA_IDS`; `:359` `extra_ids = [sid for sid in appended_ids if sid not in allowed_new]`; `:371` `append_ok = not missing_old and not extra_ids and not mutable_bad`.
- `accept-ca.py:226-236` counts registry rows with 11 cells, `c[7]=="rejected"` and `c[8]=="2026-10-24"`, and requires `rej_opened_today >= len(R66_REJECTS) + 2` (= 6). `accept-c.py`'s ROWS leg requires **all** S805-S828 to be `status mined` / tier A|B, so the two extra rejects cannot come from that block; they need fresh ids (S829+).
- **Empirical proof (isolated `/tmp/c-append-probe` clone of the lane, one appended row `| S829 | … | 2026-10-24 |` committed as the tip, run `accept-c.py --lands <probe-tip>`):**
  `STAMP PASS` … `APPEND FAIL appended=1 extra=['S829'] immutable_violations=[]` → `ACCEPT-C-67: FAIL` (rc=1). So the mechanism is exactly as reported: a later-lands reject row poisons the C counter when both are graded at one commit.
- Row arithmetic corroborates: `claims.json` C statement says `registry 724 -> 752 rows (S805-S828 plus the declared disposition additions S801-S804)`; base registry (`git show ad5b52b:corpus/SOURCES.md`) has **724** `S`-rows, and 724+24+4 = 752. With Ca's two extra rejects the same state would be 754 — the two numbers describe *different lands states*, not one inconsistent state.
- **Resolution (L1): per-claim lands separation.** A_r (S801-S804 + r66 dispositions) lands before A_c; claim C's receipt is evaluated in a clone at A_c, where only S805-S828 append over BASE (EXTRA_IDS still covers S801-S804); claim Ca's lands A_ca is later and carries the S829+ rejects (opened 2026-10-24) plus the round-67 lesson, giving D4 `opened_today=6`. No `EXTRA_IDS` revision. The dead `new_rejects` variable at `accept-ca.py:234` (computed, unused) is harmless vestigial code.
- Residual note for Ca's declared lands: `claims.json` Ca `lands` includes `corpus/SOURCES.md`, so the A_ca commit carrying S829+ is inside Ca's declared surface — consistent, provided no C-owned cell mutates after A_c (only status/recheck/used-by flips plus the declared `S753` used-by flip are allowed by `accept-c.py`).

## 10. Integration constraints this seat hands to the L1 (from the O instrument)
1. **One records commit per claim.** `check-receipt-seq.py --topo` requires each receipt's carrier's *immediate parent* to equal its stamped revision (`check_topo`: `parent = carrier^`). If the C and Ca receipts land in the same records commit, only one of them can satisfy that; the other prints `TOPO-… FAIL`. Separate records commits, each immediately after its own lands commit.
2. **Do not build `post-records.txt` from the r66 receipts** (section 1): the tool rejects them for absent `stamped`/`evaluated` headers (`missing_headers`, `no_stamp_header`). Exercise it on the r67 receipts with explicit `receipt:counter` pairs (section 2); without pairs the counter-sha pins are silently skipped (finding 5c).
3. The `--lands` counter-sha leg reads the worktree first (finding 5a) and `--lands` never asserts `stamped` is an ancestor of lands (finding 5b) — run the real receipts from a pristine materialized clone so neither hole is reachable in the recorded evidence, and treat `dirty_tracked=False` as a hand-checked precondition, not a guarantee (finding 5e).

## Blockers
None. Every artifact named by the assignment existed on disk and was read before use.

Report: .ufo/waves/round-67/w1/ExecCounterSmokeO.md
