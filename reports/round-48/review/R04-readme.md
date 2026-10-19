# R04 — README-fix review (non-author)

- Seat: `R04` | role: reviewer | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/review/R04-readme.md` (this file — my only write)
- Non-author statement: I authored none of Ca01–Ca07 and edited no fragment. I re-measured the live bytes at `a01405d` and staged the candidate fix **only** in `.scratch/r04/`. Every number below is a command output in §10 or §12.6. Ca02, Ca03, Ca05 and W02 landed after my first draft; §12 is the review of those filed bytes. Ca01 and Ca04 are still absent (§8).

**One-line judgment.** Both Ca premises hold at HEAD and I reproduce them exactly: the duplicate H1 is live at `corpus/README.md:1,3` (grep count 2), the sweep is heading-blind, and the r47 over-build class is real (nine defects reproduce in the filed bytes; 790 = 51 head + 739 body against a 103–221-line partition). The README repair is **surgical and sweep-neutral** in both measured variants. Two defects in the claim's *wording* must be corrected before integration: (F-1) its third counting command is an in-tree round runner the shared rules forbid executing, and (F-2) the "heading-count control added to the sweep" route is inadmissible because the sweep lives in filed bytes under `reports/round-28/**`. Of the four filed fragments (§12), three are sound and independently reproduced; the integration blockers are (i) the same over-build class carrying **two different row ids** across Ca02 and W02, and (ii) the heading control still being **unwired** — drafted, measured, never invoked.

---

## 1. Measured at HEAD (a01405d)

| Claim element | Command | Output |
|---|---|---|
| duplicate H1 live | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | `2` |
| which lines | `grep -n '^# ' corpus/README.md` | `1:`, `3:` — and **no other H1** (count 2 = 2 lines total) |
| introduced when | `git blame -L1,4 corpus/README.md` | line 1 `49ac1a53` (corpus mint), line 3 `57c8409b` (round-36) |
| how introduced | `git show 57c8409 -- corpus/README.md` | `+# kotodama-shokunin corpus index` + blank inserted above the revision block — an insertion, not a rename |
| sweep green now | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, 0 missing / 0 mismatch / 0 orphan, `totals_ok True`, footer ok, **exit 0**, `readme_sha256 7c788a1d…` |
| sweep is heading-blind | read `reports/round-28/readme/sweep.py:119-212` | checks parts/rows/`- topic:`/section drift/totals line/footer; **no `^#` test anywhere in `sweep()`** |
| sibling headings | `grep -n '^## ' corpus/README.md` | 7 H2: `:177 :205 :234 :261 :293 :320 :417` — all distinct, none duplicated |
| revision history | `grep -c '^revision: 2\.' corpus/README.md` | `6` (2.4 down to 1.9) |
| queue row exists | `grep -n 'R36-README-DUPLICATE-HEADING' reports/round-40/op/defect-queue-v2.json` | `:112`, class `carried-with-owner` (`:112-124`), `next_touch` "remove the redundant title as a separate recorded act, then re-run the sweep plus a heading-count control the sweep lacks" |

The queue row's own `reason` says the repair "must be a separate recorded correction" inside a corpus delta (`:118`). Claim Ca is exactly that separate act: it touches no entry, adds no row, and changes no total. **No rule is broken by fixing it this round.** The r39/r42 "do not touch inside a coverage delta" precedent does not apply, because Ca is not a coverage delta — and any C landing must be applied atomically *after* this fix, so the two do not interleave (§4).

## 2. The repair — two measured variants, both sweep-green

`corpus/README.md` is 575 lines; the defect is lines 3–4 (the duplicated H1 and the blank that the r36 insert brought with it).

**Variant A — delete line 3 only** (minimum diff, keeps the double blank):

```
3d2
< # kotodama-shokunin corpus index
```

**Variant B — delete lines 3–4** (duplicate H1 + its own blank; restores the single-blank shape the file has everywhere else):

```
3,4d2
< # kotodama-shokunin corpus index
<
```

| | HEAD | A | B |
|---|---|---|---|
| `wc -l` | 575 | 574 | **573** |
| `grep -c '^# '` | 2 | **1** | **1** |
| `grep -c '^## '` | 7 | 7 | 7 |
| `grep -c '^revision: 2\.'` | 6 | 6 | 6 |
| sha256 (file bytes) | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | `84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633` | `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` |
| `sweep.py --readme <stage>` | exit 0 | **exit 0**, 223==223 | **exit 0**, 223==223 |

Both staged sweeps print identical part counts, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_line 223`, footer `25/26/25/29/24/94`. The repair removes bytes the instrument never reads; the green is therefore necessary but not sufficient — hence the control in §5.

Note that "delete 2–3" and "delete 3–4" are byte-identical here (lines 2 and 4 are both blank): both yield `H1 / blank / revision` and sha `d407260d…`. Only the *description* differs; the bytes do not. This matters because three fragments describe the same edit with different line pairs (§12).

**Recommended: variant B.** A is defensible (its diff is one line) but leaves `H1 / blank / blank / revision`; B restores the file's one-blank convention and matches what the r36 insert should have been. The claim says "remove the redundant second title"; B removes it plus the orphan blank, no content line. Ca07's "only the second H1 line removed" criterion should be read as "no non-blank line other than the duplicate H1 may change" — both variants satisfy that.

**Acceptance test the integrator must paste** (both variants pass; use the one applied):

```
git show a01405d:corpus/README.md > .scratch/readme.before
diff .scratch/readme.before corpus/README.md        # expect 0 added lines; 1 or 2 deleted (the H1, and a blank)
grep -c '^# kotodama-shokunin corpus index' corpus/README.md   # 1
grep -c '^# ' corpus/README.md                                  # 1
grep -c '^## ' corpus/README.md                                 # 7
grep -c '^revision: 2\.' corpus/README.md                       # 6
python3 -B reports/round-28/readme/sweep.py                     # rows 223 files 223, exit 0
```

A repair that changes any **added** line, any H2, any revision line, or any row is not surgical and must be rejected.

## 3. "As a recorded act" — where the record goes

The claim requires the removal be recorded, and the queue row requires a *separate recorded correction*. Three candidate records exist; only two are correct:

- **Correct — the queue successor row.** Transition `R36-README-DUPLICATE-HEADING` to `fixed-with-evidence` in the r48 successor artifact, with the pasted `grep -c → 1`, the post-fix sweep output, and the new README sha. This is the same shape the r43 successor used for `r39-review-findings-disposition` (`reports/round-43/calib/defect-queue-v2-successor-r43.json:24`), and its G2 gate ("a fixed claim without that output is not admissible") applies. W02's deliverable already carries this row (§12.4).
- **Correct, optional — one clause in rev 2.5.** If C lands in the same apply, C10's rev-2.5 block should say the duplicate H1 was removed in the same act. That keeps the README's own changelog honest without a separate edit.
- **Wrong — a new `revision: 2.4.1` block.** It would collide with C10's rev-2.5 insertion at the same anchor and add a changelog entry for a two-line deletion the queue row already records.

## 4. Cross-claim hazard: the Ca fix shifts every README line anchor C uses

C's README hunks (K02 §5, C10) are specified by line number: `:234` culture-material header, `:240-241` the calendar/costume rows, `:544` totals, `:548` footer, `:5` the rev insertion point, `:11` the prose-vector repair. If Ca applies first, **every one of those moves**:

| anchor | HEAD | after A (−1) | after B (−2) |
|---|---|---|---|
| `revision: 2.4` (rev-2.5 insertion point) | 5 | 4 | **3** |
| prose-vector line (`25/23/25/29/24/94`) | 11 | 10 | **9** |
| `## culture-material/ (25)` | 234 | 233 | **232** |
| `Total knowledge entries: 223.` | 544 | 543 | **542** |
| footer `(total 223 files; …)` | 548 | 547 | **546** |
| first H2 `## linguistics/ (25)` | 177 | 176 | **175** |

**Required integration order and rule:** apply Ca first (it is the recorded defect fix), then apply C's README hunks **by content match** (`## culture-material/ (25)`, the two row texts, `Total knowledge entries: 223.`, the footer vector, the `revision: 2.4` line), never by the stale line numbers quoted in C10 or K02 §5. Applying C's rev-2.5 block at literal line 5 after Ca would land it inside the 2.4 block. Conversely, if C is applied first, Ca's hunk is still "delete the second H1 + one adjacent blank" (the prologue is untouched by C's insertions below it). Either order works; the anchors must be re-derived at apply time. This is the one real cross-claim hazard I found, and it is mechanical, not substantive.

## 5. The heading-count control — where it may live, and what it must assert

**F-2 (blocking on the claim's wording).** `reports/round-28/readme/sweep.py` is a **filed byte** under `reports/round-28/**` (`git ls-files` confirms it is tracked). The round's shared rule forbids editing `reports/round-1..47/**`. Therefore the claim's option "the heading-count control **added to the sweep**" cannot be executed as written. It does not invalidate the claim — the claim also allows "or a durable note filed" — but the integrator must take the second branch and the round record must say so.

**The admissible route:** a new artifact under `tools/` (live surface; `tools/gates/frozen/**` is the only frozen subtree). Ca05's `tools/check-readme-heading.py` is the right shape and I verified it independently (§12.3): 244 lines, stdlib only, read-only, and its placement matches the `tools/check-*.py` convention (`tools/check-craft-exercise.py`, `tools/check-evidence-coupling.py`).

Minimum assertions, each with a planted negative control so the gate cannot be vacuous:

1. `grep -c '^# ' corpus/README.md == 1`.
2. The surviving H1 is **line 1** and byte-equal to `# kotodama-shokunin corpus index`. Count alone is insufficient: deleting line 1 and keeping line 3 passes a count test while changing the file's first line.
3. `grep -c '^## ' == 7`, and the H2 set equals `{linguistics, myth-symbol, culture-material, synthesis, verification, civilizations} + Known gaps (frontier)` — no duplicate H2.
4. `grep -c '^revision: 2\.' == 6` (the changelog is not truncated by a mis-scoped delete).
5. Self-test controls: a fixture with the duplicate → exit 1; the canonical file → exit 0; a fixture with line 1 removed and line 3 kept → exit 1 (proves assertion 2).

Ca05's tool implements 1–3 and 5 (its `H1-NOT-FIRST` rule covers the line-1 requirement) but **not assertion 4** — no revision-count leg. That is acceptable for a heading control (scope discipline: one defect class, one control), provided the acceptance gate keeps the `grep -c '^revision: 2\.'` check that W02's G4 already runs. The control proves the **index header** is single, not that future edits keep it so — hence it must be invoked (§12.3 condition).

## 6. The r47 over-build disposition — class, evidence, and the row's guard-rails

### 6.1 The class is real; every cited defect reproduces

I re-read the filed r47 bytes (not R03's quotations) at HEAD:

| Defect | Cited location | What the bytes actually say | Reproduces |
|---|---|---|---|
| B1 arithmetic | `reports/round-47/cov/C02-entry-b.md:98` | "A line drawn at 0.2 mm on a 1:50,000 sheet claims about 10 m of ground; if the survey closed at 200 m, the drawing asserts **ten times** the available precision" — 0.2 mm × 50,000 = 10 m; 200/10 = **20** | yes |
| B2 unreproducible count | `reports/round-47/cov/C04-entry-header.md:115` | "`grep -rli 'cartograph' …` → **2 files / 3 lines**" — my `grep -rni` is 2 lines / 2 files; `grep -rli` prints files, not lines | yes |
| B3 false accusation | `reports/round-47/cov/C02-entry-b.md:36` | claims the phrase "a map is an archive of coups" is "not in the file"; `corpus/knowledge/linguistics/naming-systems.md:70` contains it **verbatim** | yes |
| B4 mis-cited ladder | `reports/round-47/cov/C02-entry-b.md:248` | cites `craft-artisan-lexicon.md:44` for the ladder; `:44` is the Steel (Japan) grading row; the ladder is `:54-65` | yes |
| B5 cross-refs | `reports/round-47/cov/C03-entry-c.md:79,184` | "the typology in §1–3" / "the typology in §2"; neither is §4.1 | yes |
| B6 wrong section | `reports/round-47/cov/C01-entry-a.md:298` | "Provenance/charter (§9)"; provenance is §8 | yes |
| B7 inconsistent rule | `reports/round-47/cov/C03-entry-c.md:123,137,150` | three incompatible update rules for Map A | yes |
| B8 competing ownership | `reports/round-47/cov/C01-entry-a.md:90,96` | "owns no made map" against `cosmology-cosmography.md:27` "how the world is drawn (maps)" | yes |
| B9 incomplete table | `reports/round-47/cov/C03-entry-c.md:95-103` | 5 form rows against 8 forms at `C01:238-249` | yes |

Volume: the assembly is **790 lines = 51-line head + 739-line body** (`reports/round-47/cross/Q01-final-gate.md:87`, `reports/round-47/review/R01-review.md:90`; R02's component breakdown `201+361+177+51 = 790` at `reports/round-47/review/R02-review.md:419`). My own partition census: `wc -l corpus/knowledge/culture-material/*.md` → min 103 / median 149 / **max 221**, 25 files. So the draft is 3.6× the longest existing entry.

### 6.2 Correct class and framing

- **Class:** `routed-with-owner` (v2 equivalent `carried-with-owner`), **not** `fixed-with-evidence`. r47 correctly refused to land the draft; there is no landed artifact to point at, and nothing about the class is fixed by r48's C claim until C lands at ≤~250 lines. If r48's C lands right-sized, the row may be re-classed at that point with the line count and the audit outputs as evidence — not before.
- **What the row must say:** the defect is *process*, not topic: (a) a draft assembled 3.6× beyond the partition's maximum with no length gate at assembly time, and (b) arithmetic/citation defects (B1–B9) that the pre-apply audit chain did not catch on the assembled bytes (B4, B5, B6, B9 were not caught by any sibling audit; B3's "fix" would have corrupted a correct quote). Cite `reports/round-47/review/R03-c-content.md:188-196` (the B table) and `:96` (volume), plus `Q01-final-gate.md:87`.
- **What the row must not say:** that the entry was landed (it was not); that the topic was wrong or carried (R03 §7 and my read agree the gap is genuine); that the class is fixed by this round's C claim before C actually lands.
- **Owner / next_touch:** owner = C-drafters + integrator (the assembly act); next_touch = (i) r48's right-sized redraft is the first instance and must pass a mechanical `wc -l <= 250` check before the length audit, (ii) a length gate at assembly (run `wc -l` on the assembled body, fail at > ~250) is the durable prevention and should be named as the next touch if no gate lands this round.
- **Parent pin and file:** build `reports/round-48/calib/queue-successor-r48.json`, `parent: reports/round-40/op/defect-queue-v2.json` at sha256 `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` (verified unchanged), plus `predecessor_successor: reports/round-47/calib/queue-successor-r47.json` at `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58` (verified). Do **not** copy the r47 successor's rows into the new file — reference it as the predecessor, the way r47 did with r43. No id collision with earlier artifacts: I enumerated all three queue artifacts (38 + 4 + 3 rows) and none carries an over-build/length row (`grep -niE 'over-?build|length discipline|790'` → no row). The id is genuinely new — but two r48 fragments mint **different** ids for it (§12.5).
- **Carry the README row in the same artifact:** the duplicate-heading row is a second r48 row; it transitions `R36-README-DUPLICATE-HEADING` to `fixed-with-evidence` with the §2 evidence. One successor file, two rows, each with its own verification string.

## 7. Findings on the claim as worded

| ID | Severity | Finding | Required correction |
|---|---|---|---|
| **F-1** | blocking on the claim text | `reports/round-48/claims.json:49` lists `python3 reports/round-48/run-validation.py` as a Ca counting command. The shared rule is absolute: **never run `reports/round-*/run-validation.py` in-tree**. As written, the claim instructs a forbidden act. | Replace with `python3 -B reports/round-28/readme/sweep.py` (already command #2) and let the integrator's isolated validation supply the runner output. Record the substitution in the round record; do not execute the runner in-tree. |
| **F-2** | blocking on the claim text | "the heading-count control added to the sweep" (`claims.json:45`) is inadmissible: `reports/round-28/readme/sweep.py` is a filed byte. | Take the claim's own alternative ("or a durable note filed") and prefer the new `tools/` control (§5, drafted by Ca05). State the filed-byte reason in the queue row. |
| **F-3** | note | The claim's `before` says the README carries the duplicate at "lines 1 and 3" — correct — but does not name the *source commit*. | Optional; the queue row should carry `git blame` → `57c8409b` (r36) so the defect's origin is in the record, not just its symptom. |
| **F-4** | note | The prose-vector defect (`README:11`, "25/23/25/29/24/94 → 25/23/26/25/24/94" sums 220 → 217) belongs to **C's** rev-2.5 edit, not Ca. Ca's diff must not touch it; C's repair must produce `25/26/25/29/24/94` (sums 223) for the *after* side. | Keep the two edits separate; C10's block must carry the arithmetic (`25+26+25+29+24+94 = 223`; post-landing `25+26+26+29+24+94 = 224`). |

I verified the arithmetic myself: `25+23+25+29+24+94 = 220`, `25+23+26+25+24+94 = 217`, `25+26+25+29+24+94 = 223`, `25+26+26+29+24+94 = 224`.

## 8. What I could not evaluate

- **Ca01 and Ca04.** No `Ca01-readme-fix.md` or `Ca04-verify.md` exists at my final read. The edit itself is verified from live bytes and from Ca03/W02's filed measurements (§12), so the absence does not block the apply — but those two declared out paths are unfilled, and the round's write-surface census must record them as missing, not as satisfied.
- **C's rev-2.5 text and the staged 224 sweep.** C10/C11 own those; I verified only the arithmetic and the line-anchor hazard.
- **Any external claim.** None is in scope for Ca.
- **The applied (landed) bytes.** Everything here is measured on staged copies. The delivery certificate is the post-apply sweep plus the heading control on the landed file.

## 9. Axis verdict

- **Calibration: +1, conditional on the apply.** The duplicate-H1 defect has been carried since r36, re-verified five times, and blocked by a do-not-touch convention with no owner — Ca is the first claim to give it a recorded act. Fixing it removes a live index defect at zero cost to the sweep (measured, both variants), and the over-build row gives the r47 failure class a durable home and a concrete prevention (length gate). Neither move touches canon, tools/frozen, or filed bytes.
- **Coverage: no harm.** Ca adds no corpus file and no row; the README's 223 rows and 223 files are unchanged in both variants.
- **No harm to any other axis.** The only cross-claim effect is the line-anchor shift (§4), which is mechanical and resolved by content-anchored application.

**Recommendation: apply the Ca README fix (variant B) as a separate recorded act, install and invoke the heading control, file the two-row successor `queue-successor-r48.json` under one canonical over-build id, then apply C's README hunks by content match. Reject the claim's in-tree runner command (F-1) and its sweep-edit route (F-2).**

## 10. Commands run (all from the lane root, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`, 2026-10-19)

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ git blame -L1,4 corpus/README.md
49ac1a53 … 1) # kotodama-shokunin corpus index
49ac1a53 … 2)
57c8409b … 3) # kotodama-shokunin corpus index
57c8409b … 4)
$ git show 57c8409 -- corpus/README.md        # +H1 +blank inserted above revision 2.1
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing 0 []; topic_mismatch 0 []; orphan_rows 0 []; header_drift {}
totals_line 223 totals_ok True; footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/r04/README.A.md
rows 223 files 223 … footer_ok True; readme_sha256 84e16f56…; exit=0
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/r04/README.B.md
rows 223 files 223 … footer_ok True; readme_sha256 d407260d…; exit=0
$ wc -l corpus/README.md .scratch/r04/README.A.md .scratch/r04/README.B.md
575 / 574 / 573
$ diff corpus/README.md .scratch/r04/README.B.md
3,4d2
< # kotodama-shokunin corpus index
<
$ grep -c '^# ' .scratch/r04/README.{A,B}.md
1 / 1
$ grep -c '^## ' corpus/README.md          # 7
$ grep -c '^revision: 2\.' corpus/README.md  # 6
$ sha256sum corpus/README.md .scratch/r04/README.A.md .scratch/r04/README.B.md
7c788a1d… / 84e16f56… / d407260d…
$ wc -l corpus/knowledge/culture-material/*.md | sort -n   # min 103, median 149, max 221, 25 files
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l        # 2
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l        # 2
$ sed -n '98p' reports/round-47/cov/C02-entry-b.md         # "…200 m… ten times…"
$ sed -n '248p' reports/round-47/cov/C02-entry-b.md        # cites craft-artisan-lexicon.md:44
$ sed -n '44p' corpus/knowledge/culture-material/craft-artisan-lexicon.md  # Steel (Japan) row
$ sed -n '70p' corpus/knowledge/linguistics/naming-systems.md              # "archive of coups" present
$ sed -n '27p' corpus/knowledge/myth-symbol/cosmology-cosmography.md       # "drawn (maps)"
$ sha256sum reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json
dfc9265d… / 9508b6aa…
$ git status --porcelain reports/round-40/op/defect-queue-v2.json   # empty (parent unedited)
$ python3 -c "print(25+23+25+29+24+94, 25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
220 217 223 224
```

## 11. Write surface

This file only — `reports/round-48/review/R04-readme.md`. Staged scratch fixtures under `.scratch/r04/` (disposable; not a deliverable). No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `LOG.md`, `SCORECARD.md`, or fleet byte was edited or staged. No git commit/push, no install, no network, no in-tree `run-validation.py` executed. `git status --porcelain` at write cut: only the pre-existing `?? reports/round-46/review/` and `?? reports/round-48/`.

---

## 12. Addendum — review of the filed Ca fragments

The fragments landed after my first draft. I re-read all four and re-ran every load-bearing measurement rather than trusting their receipts. Sizes: Ca02 227 lines, Ca03 210, Ca05 509, W02 401.

### 12.1 Ca03 — README verifier: PASS

- Its staged hashes match mine **exactly**: recommended variant `d407260d…` (573 lines), alternative `84e16f56…` (574 lines). Two independent generations of the same edit, byte-identical.
- Its heading-shift table (V3: `177→175`, `205→203`, `234→232`, `261→259`, `293→291`, `320→318`, `417→415`) matches my §4 table for the −2 variant.
- Its V7 orthogonality simulation (staged fix + a synthetic rev-2.5 paragraph → 577 lines, H1 count 1, sweep green) is an addition mine did not run; it is the right test for the §4 hazard, and its result is consistent with my content-anchoring recommendation.
- Its conditions on the integrator (apply by content, re-run the sweep on landed bytes, the staged sha is not the post-landing sha) are correct and match §4.
- Precision note, not a defect: §4.1's heading says "delete the blank line and the second H1 (lines 2–3)" while the diff removes lines 3–4. The bytes are identical (§2), so the instruction is harmless, but three fragments name three different line pairs. The apply should name the **content** rule ("second H1 + one adjacent blank"), which W02 does.

### 12.2 Ca02 — over-build disposition: PASS on substance, one dedupe defect

- The fenced JSON **parses** (I extracted and parsed it): one row, id `r47-entry-overbuild-defect-class`, class `routed-with-owner`.
- Every digest it cites re-computes exactly: `R03-c-content.md 7e3e0880…`, `R01-review.md 196328de…`, `validation.json 17f8f1d4…`, `C11-scribe.md 4637ab10…`, the four r47 fragment digests, `cosmology-cosmography.md 165f292b…`, `naming-systems.md d972a1d6…`, `craft-artisan-lexicon.md fd678d82…`, parent `dfc9265d…`, predecessor `9508b6aa…`.
- Its nine B-row live checks reproduce against the filed bytes (I re-ran each independently; §6.1 is the same result).
- Its two-scope handling is the honest fix for the r47 failure mode: 739 body lines (R03's fence extraction) and 790 assembled lines (validation) are quoted with their scopes and **not** subtracted into a third number. Its `indicative_to_verify` sizes (r42 538, r44 485) are whole-fragment `wc -l`; I measured both and they match.
- **Defect (dedupe):** its row id is `r47-entry-overbuild-defect-class`; W02's deliverable JSON uses `r47-overbuilt-entry-draft` for the same class. Two ids for one class is exactly the double-count its own `class_boundary` warns against. The integrator must pick one canonical id and record the other as an alias.
- Its `proposed_control` is correctly marked **not landed**; `grep -rln 'partition band|length in partition' tools/` → no match, confirmed.

### 12.3 Ca05 — heading control: the tool is real; the wiring is not

I extracted the 244-line fenced tool byte-for-byte into `.scratch/r04/tools/check-readme-heading.py` and ran it myself:

```
$ python3 -B .scratch/r04/tools/check-readme-heading.py --selftest
8/8 checks passed                                             exit 0
$ python3 -B … --readme corpus/README.md
h1_lines [1, 3]; findings 1; H1-COUNT lines=[1, 3]             exit 1
$ python3 -B … --readme .scratch/r04/README.B.md
h1_lines [1]; findings 0                                      exit 0
$ python3 -B … --readme .scratch/r04/README.A.md
h1_lines [1]; findings 0                                      exit 0
```

So the tool does what it claims, on my own fixtures as well as Ca05's: it is red on the live defect and green on both candidate fixes, and it covers the line-1 requirement (`H1-NOT-FIRST`) that a bare `grep -c` would miss. It is stdlib-only and read-only; its `tools/check-readme-heading.py` placement matches the `tools/check-*.py` convention.

**The condition:** a drafted tool is not a control. Ca05 says this honestly (§7: "until the integrator adds step 1 of §6, the tool is a tool, not a gate"). The integrator must (a) create the file from the fence, (b) run its selftest, (c) run it **before** the fix to capture the red receipt and **after** to capture the green, and (d) ensure it is invoked in future — ideally as a leg in the integrator-authored `reports/round-48/run-validation.py` (Ca05 §6.1), which is permitted because the rule forbids *running* round runners in-tree, not authoring a validation leg. W02 A.4 currently makes the control optional ("if Ca05's control lands this round"); it must be mandatory.

Gap in coverage: Ca05's tool has no revision-count assertion (§5, assertion 4). That is acceptable scope discipline only if the apply gate keeps W02's `grep -c '^revision: 2\.'` = 6 check.

### 12.4 W02 — landing wire: PASS, one sequencing-wording defect

- Preconditions, postconditions, and gates verified: pre-state sha `7c788a1d…`, post-state `d407260d…` / 573 lines / 143,832 bytes, sweep green 223==223; parent and predecessor pins match my runs; both fenced JSONs parse (2 rows: `R36-README-DUPLICATE-HEADING` `fixed-with-evidence`, over-build row `routed-with-owner`).
- Its A.2 note that `sed -i '2,3d'` and `sed -i '3,4d'` produce identical bytes is correct (the two blanks are interchangeable).
- Its treatment of the 739-vs-790 scope difference repeats Ca02's honest handling and does not derive arithmetic across the three figures (1449 fragment file lines, 739 body, 790 assembled).
- **Defect (wording):** §2.5 says "the H1 removal does not move the `revision:` block". It does: line 5 → 3 (B) or 4 (A). What is true is that the *shape* is unchanged and C's rev-2.5 block still goes immediately above `revision: 2.4` — but that anchor is now line 3/4, not line 5. Its own A.5 handles the C-first branch correctly; the Ca-first sentence should carry the same caveat.
- **Defect (dedupe):** its second row id is `r47-overbuilt-entry-draft` (see §12.2).

### 12.5 Cross-fragment consistency matrix

| Property | R04 (me) | Ca02 | Ca03 | Ca05 | W02 |
|---|---|---|---|---|---|
| chosen variant | B (3–4) | — | B (2–3, same bytes) | 3–4 | 3–4 (either) |
| post-fix sha | `d407260d…` | — | `d407260d…` | `d407260d…` | `d407260d…` |
| post-fix lines | 573 | — | 573 | 573 | 573 |
| H1 count after | 1 | — | 1 | 1 | 1 |
| sweep after | exit 0, 223==223 | — | exit 0, 223==223 | exit 0, 223==223 | exit 0, 223==223 |
| over-build row id | (proposed a class, no id) | `r47-entry-overbuild-defect-class` | — | — | `r47-overbuilt-entry-draft` |
| README close row | required (§3) | — | required (LOG) | — | `R36-README-DUPLICATE-HEADING` |
| heading control | required + spec (§5) | — | stopgap grep | tool drafted + measured | two greps, control optional |

Three integration decisions follow: **(1)** one canonical over-build id (alias the other); **(2)** the heading control is mandatory, created and invoked, with red/green receipts; **(3)** C's README hunks are content-anchored because the Ca fix moves every line number below the prologue.

### 12.6 Addendum commands

```
$ ls reports/round-48/calib/
Ca02-overbuild.md Ca03-readme-verify.md Ca05-heading-control.md W02-landing-spec.md
$ python3 (extract Ca05's 4-backtick fence → .scratch/r04/tools/check-readme-heading.py)
$ wc -l .scratch/r04/tools/check-readme-heading.py
244
$ python3 -B .scratch/r04/tools/check-readme-heading.py --selftest
selftest: 8/8 checks passed          (exit 0)
$ python3 -B .scratch/r04/tools/check-readme-heading.py --readme corpus/README.md
H1-COUNT lines=[1, 3]                (exit 1)
$ python3 -B .scratch/r04/tools/check-readme-heading.py --readme .scratch/r04/README.B.md
h1_lines [1], findings 0             (exit 0)
$ python3 (parse fenced JSON of Ca02 and W02)
Ca02 PARSE OK rows ['r47-entry-overbuild-defect-class'] classes ['routed-with-owner']
W02  PARSE OK rows ['R36-README-DUPLICATE-HEADING','r47-overbuilt-entry-draft']
$ sha256sum reports/round-28/readme/sweep.py reports/round-48/claims.json reports/round-47/claims.json \
            reports/round-47/validation.json reports/round-47/review/R03-c-content.md \
            reports/round-47/review/R01-review.md reports/round-47/cov/C11-scribe.md \
            reports/round-44/scout/K02-gap-scout.md
9b2ccac0… bf8df21b… 7eb16979… 17f8f1d4… 7e3e0880… 196328de… 4637ab10… a72fff27…
   (each equals the digest the fragment claims)
$ sha256sum corpus/knowledge/myth-symbol/cosmology-cosmography.md \
            corpus/knowledge/linguistics/naming-systems.md \
            corpus/knowledge/culture-material/craft-artisan-lexicon.md
165f292b… d972a1d6… fd678d82…   (each equals the fragment's claim)
$ wc -l reports/round-42/cov/C01-entry-1.md reports/round-44/cov/C01-entry-draft.md
538 / 485
$ grep -rln 'partition band\|length in partition' tools/
(no output — Ca02's "no durable control" claim reproduces)
```

**Addendum write surface:** `.scratch/r04/tools/` (extracted fixture, disposable) plus this file's revision. No corpus, tool, or filed-round byte was written.
