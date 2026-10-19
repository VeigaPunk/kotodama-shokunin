# R02 — independent cross-claim review: axis harm

- Seat: `R02` | role reviewer | claim **cross** | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`baseline_commit: a01405d`)
- Out path: `reports/round-48/review/R02-review.md` (this file)
- Non-author statement: I drafted no C or Ca fragment and edited no fragment. Every number below is from a command in §8 or a re-read of the cited file at `a01405d`. I wrote only this file.

**One-line judgment.** The round's two claims are correctly scoped and the baseline is clean, but the *contract* contains three defects that will produce a wrong or unsafe landing if followed literally: (1) the Ca claim calls the README duplicate heading a "live defect" without naming that it is a **carried queue row from r36** whose `next_touch` was r42/r44 and whose r39-X00-7 rule demands a *separate recorded act*; (2) `targets.json` C10 tells the README drafter to repair the rev-2.4 vector "= 224" when the repaired rev-2.4 vector must sum **223** (computed below); (3) the C draft's 250-line budget is arithmetically incompatible with keeping r47's 240 table rows, so "right-sized" has to be defined as row *selection*, not prose trimming. None of these is an axis harm yet; each is a landing defect waiting for an executor to inherit it. **Post-cut (§9) adds the one live blocker: the filed entry and the filed README row carry different `- topic:` texts, and the staged 224 sweep is red on `topic_mismatch 1` until the entry is normalized to the 766-char seed text.**

---

## 1. Baseline, measured (not carried)

| Fact | Value | Command (¥8) |
|---|---|---|
| HEAD | `a01405dd36367292255c2652ac0a601f4cd6a0af` | `git rev-parse HEAD` |
| Worktree | only `?? reports/round-46/review/`, `?? reports/round-48/` | `git status --porcelain` |
| Total entries | **223** | `find corpus/knowledge -name '*.md' \| wc -l` |
| Partitions | linguistics 25 / myth-symbol 26 / culture-material 25 / synthesis 29 / verification 24 / civilizations 94 = 223 | `ls corpus/knowledge/*/*.md` by partition |
| Cartography owners | **0** filename, **0** topic line | `find -iname '*cartograph*' …`, topic grep |
| `cartography-and-mapmaking.md` | absent | `ls` → No such file |
| README | 575 lines, sha256 `7c788a1d…f4679cf1`, 223 bullet rows, **H1 count 2** (`:1`, `:3`), H2 count 7 | `wc -l`, `grep -c '^# '` |
| README totals / footer | `:544` 223; `:546-548` `25/26/25/29/24/94` | `grep -n` |
| Sweep | rows 223 == files 223, 0 missing/ghost/mismatch/drift, footer ok, **exit 0** | `python3 -B reports/round-28/readme/sweep.py` |
| culture-material lengths | n 25, min 103, median 149, max 221, mean 150.2 | `wc -l … \| sort -n` + Python |

The claim's `before` fields for C and Ca are true at `a01405d`. C is fresh: a global grep of `reports/` for `cartograph|mapmaking` outside r44–r48 returns only frozen-input copies of `mesoamerica-primary-sources.md` (6 scratch files), no proposal, and `corpus/lessons/` has 0 hits. Ca's `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` = **2**.

---

## 2. What was reviewable at my write cut — and what was not

At my read, `reports/round-48/` contained only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`. **No scout, planner, executor, or verifier fragment existed**, so this review is of:

1. the live baseline and the round contract (`claims.json`, `targets.json`);
2. the r47 evidence the contract is built on (`reports/round-47/review/R03-c-content.md`, the r47 fragments it cites, `reports/round-47/validation.json`);
3. the r44 cartography seed and the r36–r40 README-defect record.

Per-fragment review (does C01's draft repeat B1–B9? does Ca02's row cite real paths?) is **`could-not-evaluate`** here and must be re-run by R03/R04/X01 against the filed fragments. What follows is the part a non-author can settle independently: whether the *round* can harm an axis if executed as written.

**Addendum, written after the wave landed.** Fragments were filed while this review was being written. §9 below is a post-cut review of the artifacts that now exist (C01's entry, C10's patches, C11's fixture, Ca02/W02, C03). The §1–§8 findings stand; where a later fragment already caught one, §9 says so and credits it rather than claiming novelty.

---

## 3. Claim C (coverage): is the +1 real, and where can it harm?

### 3.1 The gap is real and the count arithmetic is correct

- 0 filename owners, 0 topic-line owners at 223; slug free; landing is an **A** (new file), not an M.
- Total 223 → 224 and culture-material 25 → 26 are correct. The rev-2.5 footer vector must be **`25/26/26/29/24/94` = 224** (verified sum).
- No existing entry is overwritten; the sort position between `calendar-festival-systems.md` and `costume-semiotics.md` holds at HEAD (README `:240-241`).

### 3.2 The "over-build" number is now reconciled — and the reconciliation matters

The round brief says "r47's 790-line over-build"; R03 says "739 body lines". Both are right, and I reproduce the bridge:

- r47 files: C01 358 + C02 503 + C03 287 + C04 301 = **1449** file lines.
- Entry sections C01+C02+C03 (raw extraction, including headings/blanks) = **749** lines, 17,619 words.
- R03's **739** is a 10-line boundary difference on that same extraction (words differ by 18: 17,601 vs 17,619) — same text.
- r47's head block is **51** lines (`C04:112-162`). **739 + 51 = 790**, which is exactly the figure `reports/round-47/validation.json` uses. My extraction gives 749 + 51 = **800** (raw, boundary-inclusive).

Consequence for Ca: the disposition row may cite **790** only with the extraction method (`739 body + 51 head`), because an unqualified `wc -l` on a naive assembly gives 800. R03's own P2-3 asked for "≤300 lines"; the round's 250 target is stricter, and that is the right direction.

### 3.3 The 250-line budget is arithmetically a table-row budget

r47's 790 lines contain **240 table rows** (my count: 240 `^|` lines), i.e. 30.4% of lines. At the same density, a 250-line entry can carry only ~**76** table rows. So "right-sized" cannot mean "keep the tables, cut the prose" (R03's advice) *and* ≤250 lines — the two are incompatible. The C draft must decide **which rows earn their line**, roughly a 2/3 cut of r47's row count, while keeping the load-bearing tables (form typology with "what it cannot show", failure table, warrant chain, decision record). This is the concrete anti-over-build test: if the assembled file is ≤250 lines, the row count is necessarily ≤~80 and the draft has selected.

Also note the head block counts: the file's `wc -l` includes `- topic:` / `- gap filled:` / `- sources:` / `- couples:` / `- source:` / `- verified-at:` / `- recheck:` / `- scope:`. Budget the body at ~220-235.

### 3.4 B1–B9 are real — I re-verified six of nine against filed bytes

The contract says the draft must avoid "all 9 of R03's blocking defects". I re-read the source lines rather than trusting the summary:

| ID | Independent check | Verdict |
|---|---|---|
| B1 | `C02:98` says `0.2 mm … claims about 10 m … 200 m … ten times`; `0.2 × 50,000 = 10,000 mm = 10 m`; `200/10 = 20` | **real** — "twenty times"; fix by changing 200 m → 100 m or ten → twenty |
| B2 | `C04:59` says `grep -rli 'cartograph' … # 2 files / 3 lines`; live `grep -rni 'cartograph'` = **2 lines, 2 files** (`cosmography:102`, `mesoamerica:58`) | **real** — `-l` lists files, not lines; `:71` has no `cartograph` token |
| B3 | `C02:36` and `:501` accuse C01 of quoting a phrase "not in the file"; `grep -c 'archive of coups' naming-systems.md` = **1** at `:70` | **real false accusation** — applying C02's "correction" would corrupt a correct quote |
| B4 | `craft-artisan-lexicon.md:44` = `| Steel (Japan) | tamahagane …`; ladder header at `:54`, systems `:56-63`, rule `:65` | **real** — anchor must be `:54-65` |
| B5 | `C03:79` "typology in §1–3"; `C03:184` "typology in §2"; C01 `:234` = §4, `:238` = §4.1 | **real** — both must say §4.1 |
| B6 | `C01:298` "Provenance/charter (§9)"; C02 `:278` = §8, `:347` = §9 | **real** — §9 → §8 |
| B7 | `C03:123` "re-survey after any storm that breaches a dike"; `:137` "the re-survey is not due until the levy year turns"; `:150` table "after a dike breach, per levy year" | **real** — three statements of one rule; adopt one and state it once |
| B9 | `C03:99-103` has 5 form rows (header `:97-98`); `C01:238-249` lists 8 forms | **real** — 5 of 8 |

(B8 — the competing cosmography definition at `cosmology-cosmography.md:27`, "how the world is drawn (maps)" — is also real; I read `:27` live. The right-sized draft can satisfy it in one sentence without a new section.)

**Harm vector to watch:** these nine defects are all *cheap to inherit* because they are copied from the seed material. The r48 draft is a redraft, not a copy — the verification legs (arithmetic, citation anchor, worked-example consistency, per-form completeness) must run on the **assembled final bytes**, not on a pre-fix assembly. r47's failure was partly that pre-fix verdicts were filed as PASS.

### 3.5 Gap-count honesty

The `- gap filled:` line must cite measured counts with the command. My verified term table:

| Term | files | lines |
|---|---:|---:|
| `cartograph` | 2 | **2** |
| `mapmak` | 0 | 0 |
| `portolan` | 0 | 0 |
| `cadastr` | 2 | 2 |
| `mappa` | 2 | 2 |
| `survey map` | 1 | 1 |
| `compass rose` | 1 | 1 |
| `graticule` / `theodolite` | 0 / 0 | 0 / 0 |
| `lienzo` | 1 | 4 |
| broad pattern (K02's list) | 28 | — |

Any "3 lines" claim is B2 recurring. Any claim of high demand is the r43 lesson recurring.

### 3.6 Coverage axis verdict

**Coverage: +1 genuine, no harm if the length and defect legs are enforced.** The topic is unowned, the nearest neighbours disclaim the object (`cosmology-cosmography.md:71,:102`), and the partition has every adjacent production system but no made-map entry. The axis is only at risk if the draft is r47's bytes renamed or if the audits are declared rather than run.

---

## 4. Claim Ca (calibration): the README fix and the over-build disposition

### 4.1 The duplicate H1 is not new — it is a carried queue row, and that changes the disposition

- Introduced by **commit `57c8409b`** ("round-36: REJECTED on D …"), which inserted the rev-2.1 block and duplicated the title at `:3` (`git blame -L 1,6`).
- Queued as **`R36-README-DUPLICATE-HEADING`** at `reports/round-37/op/defect-queue.json:103-131`; carried into `reports/round-40/op/defect-queue-v2.json:112`.
- The v2 row's own text: `class: carried-with-owner`; owner "integrator to assign a corpus-index editor"; `next_touch: r42 or r44 (corpus-owning build round): remove the redundant title as a separate recorded act, then re-run the sweep plus a heading-count control the sweep lacks`; reason cites r39 X00-7: "do-not-touch inside any corpus delta … repair must be a separate recorded correction."
- `reports/round-39/cross/X00-connector.md:252-256` is that rule verbatim.

So Ca is a **queue close with two missed touches** (r42 and r44 passed without doing it), not a fresh find. The r48 successor must:

1. cite id `R36-README-DUPLICATE-HEADING` and reclass it `fixed-with-evidence`;
2. paste the re-run commands and outputs (sweep + heading control + grep count);
3. state the r42/r44 miss rather than implying r48 was the scheduled touch;
4. not create a second row for the same defect (id collision checked: none of `r47-overbuilt-entry-class`, `r48-overbuild-entry-class`, `r47-build-quality-class` exists — all free).

### 4.2 The edit and its measured effect

Exact staged test (in `.scratch`, no corpus write): `sed '3,4d' corpus/README.md` → **573 lines**, H1 count **1**, H2 count **7**, sweep **exit 0**, 223 == 223, footer unchanged, staged sha256 `d407260d…b3190079`.

Two integration facts the contract does not state:

- **Line-number drift.** Removing `:3-4` shifts every later line by −2: `Total knowledge entries` moves 544 → **542**; the `Counts checked` footer 546 → **544**; the culture-material header 234 → **232**. Filed reports cite `README:544`, `:548`, `:234`, `:240-241` (e.g. `reports/round-44/scout/K02-gap-scout.md:307-314`). Those citations are filed bytes and cannot be edited. The sweep parses by regex, so nothing breaks mechanically, but the round record should state the −2 drift once, or the integrator should prefer the blank-line variant (replace `:3` with an empty line) if zero drift is valued. I recommend the delete + recorded drift; the blank-line variant leaves a double blank line in a 573-line index and is cosmetically wrong.
- **Apply order.** Ca's hunk is at `:1-4`; C's rev-2.5 hunk inserts at `:5`. If **C lands first**, the duplicate H1 is still at `:3` and Ca's hunk applies unchanged. If **Ca lands first**, C's `:5` context shifts to `:3` and its diff must be regenerated. The contract's counting commands do not fix an order; §6 fixes one.

### 4.3 The sweep is demonstrably blind to README prose — measured, not asserted

I staged a copy with the entire `revision: 2.4 …` line deleted (line 5) and ran the sweep: **exit 0, 223 == 223, footer ok**. The sweep reads rows, section headers, the totals line and the `Counts checked` footer; it never reads the H1 or the revision prose. Its selftest is 12/12 with no heading control (`reports/round-28/readme/sweep.py` selftest list).

The required control (Ca05's draft should be this, not a prose note):

- `H1_RE = re.compile(r"^# ", re.M)` — the space excludes `##`; assert `len(H1_RE.findall(text)) == 1` **and** the first line equals `# kotodama-shokunin corpus index`.
- Assert it against the **staged** README via the sweep's existing `--readme` flag (verified to work), so the control can be planted-tested without touching `corpus/`.
- Selftest controls: (a) duplicate the H1 in a fixture → fails; (b) delete it → fails; (c) correct file → passes. A control that only asserts "1" without a planted duplicate is the r27-style footer-blind green again.

A one-shot `grep -c '^# ' == 1` check is acceptable as the durable note **only** if it is filed with a date, command and owner; the r37 row explicitly asks for "a heading-count control the sweep lacks", which reads as an instrument, not a one-off.

### 4.4 The over-build disposition row

What must be true of the row (Ca02/Ca06):

- class `routed-with-owner`, not `fixed` — no redraft has landed at the time the row is filed;
- owner = r48/r49 C drafter + the C-claim verifier legs (arithmetic / citation / length), next_touch = the right-sized redraft and its re-run audits;
- evidence must cite: `reports/round-47/validation.json` (`C: unchanged-blocked`, "790 lines vs live partition max 221 with 9 blocking defects"), `reports/round-47/review/R03-c-content.md` B1–B9, the partition stats (103/149/221/150.2), and the 739+51=790 extraction note;
- parent pin `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` and r47 successor sha `9508b6aa…` with a statement that neither is edited.

The class is wider than "too long": the row should name the **compound** failure — a draft whose length exceeds the partition band *and* whose arithmetic/citation legs were not run before a PASS verdict. Length alone would be a style note; length plus B1–B9 is the admission defect. The r48 freshness gate guards topic ownership only, which is exactly why this class needs the row.

### 4.5 Calibration axis verdict

**Calibration: +1 if executed as a close, 0 or −1 if filed as a new unlinked row.** The fix itself is safe (staged sweep green, H1 2→1, no other heading touched — H2 count stays 7). The risk is bookkeeping: a successor that does not close `R36-README-DUPLICATE-HEADING` would leave the v2 ledger claiming a live defect after the bytes are fixed, which is worse than not fixing it.

---

## 5. Findings

Severity: **B** = must resolve before apply; **P2** = should fix; **N** = note.

| ID | Sev | Claim | Finding | Evidence / fix |
|---|---|---|---|---|
| **R02-F1** | B | Ca | The duplicate H1 is the carried row `R36-README-DUPLICATE-HEADING`, introduced by `57c8409b`, whose `next_touch` was r42/r44 and whose r39 X00-7 rule requires a **separate recorded act**. Ca must close that id in the r48 successor and record the two misses. | `git blame -L 1,6`; `defect-queue.json:103-131`; `defect-queue-v2.json:112`; `X00-connector.md:252-256` |
| **R02-F2** | B | both | Apply order is unspecified. C's rev-2.5 hunk is authored at `:5`; applying Ca first shifts it to `:3` and the diff fails. Fix: C first, then Ca; `git apply --check` before each; do not fold the H1 removal into C's hunk. | §4.2; README `:1-13` |
| **R02-F3** | B | Ca | The contract's "repair the rev-2.4 prose-vector … = 224" (C10) is wrong arithmetic. The rev-2.4 repair describes the **223** state and must read `25/26/25/29/24/94` = 223. Only the rev-2.5 vector is `25/26/26/29/24/94` = 224. Writing 224 into the rev-2.4 sentence falsifies the historical record. **P01:102 and C10 §2 already correct this**; the remaining defect is that `targets.json` still says "= 224", so the integrator must read P01/C10, not the target shorthand. | Sums: 220 / 217 / 223 / 224 (verified, §8); `reports/round-48/plan/P01-plan.md:102`; `cov/C10-readme.md:55`; r47 C09 §2.2 had it right |
| **R02-F4** | B | Ca | The heading-count control must be an instrument with planted controls, not a claim. The sweep is blind to H1 and to revision prose — a staged copy with the rev-2.4 line deleted still exits 0. | §4.3; sweep selftest 12/12 |
| **R02-F5** | P2 | C | 250 lines and 240 table rows are incompatible. Right-sizing is row selection (~≤80 rows); budget the body at ~220-235 after the head block. | §3.3; 240 `^|` lines measured |
| **R02-F6** | P2 | C | The over-build figure needs its extraction method. 790 = 739 body (R03) + 51 head; a naive extraction gives 800. Cite the method or the number is unreproducible (the B2 defect class in prose). | §3.2 |
| **R02-F7** | P2 | C | The gap line must use `-n` line counts, not `-l` file counts. `cartograph` is 2 files **2 lines**, not 3. | §3.5; B2 |
| **R02-F8** | P2 | C | B1, B2, B3, B4, B5, B6, B7, B9 all reproduce against the filed r47 bytes (six re-verified line-by-line here; B8 at `cosmology-cosmography.md:27` also real). The redraft must pre-empt each with a mechanical check, and the audits must run on the assembled bytes. | §3.4 |
| **R02-F9** | N | Ca | Removing `:3-4` shifts later lines by −2 (544→542, 546→544). Record the drift once in the round note; filed citations cannot be edited. | §4.2 |
| **R02-F10** | N | Ca | The successor row must pin the parent (`dfc9265d…`) and the r47 successor (`9508b6aa…`) unchanged, and must not add a second row for the dup heading. | `sha256sum`; `defect-queue-v2.json` |
| **R02-F11** | N | C | The r48 claims/targets digests match the dispatch record (`bf8df21b…`, `d029eaa1…`), and `baseline_commit` equals HEAD — no r43-style drift at declaration. | `telemetry/dispatch-declared.json` |
| **R02-F12** | N | both | No seat fragment existed at my cut, so executor-level harm (a verifier certifying an unaudited draft) is `could-not-evaluate` here. R03/R04/X01 must judge the filed bytes. | §2 |

---

## 6. What the integrator should enforce, in order

1. **C, draft stage:** assemble the entry; `wc -l` ≤ 250; count `^|` rows and record the selection versus r47's 240; run the arithmetic, citation-anchor, worked-example and per-form legs on the assembled bytes; re-run the gap sweep at the landing HEAD.
2. **C, apply stage:** new file only + README rev-2.5 hunk (row in filename order, header 25→26, totals 223→224, footer `25/26/26/29/24/94`, rev-2.4 vector repaired to `25/26/25/29/24/94` = 223). Run the sweep: 224 == 224, exit 0.
3. **Ca, apply stage:** *separately*, delete `corpus/README.md:3-4` only. Run the sweep (still green) and the new heading control (H1 == 1, line 1 is the title). Record the −2 line drift.
4. **Ca, ledger stage:** file the r48 queue successor with two rows — the dup-heading close (`fixed-with-evidence`, id `R36-README-DUPLICATE-HEADING`) and the over-build class (`routed-with-owner`, evidence r47 R03 B1–B9 + validation), parent pinned.
5. **Do not** let C's hunk touch the H1 (X00-7) and do not let Ca's hunk touch any revision prose.

---

## 7. Not verified / could-not-evaluate

- **Every r47 B-defect**: I re-read six plus B8 line-by-line; B2/B3/B4/B7/B9 were read at the cited lines, B1 arithmetic recomputed, B5/B6 cross-references checked against the H2 list. I did not re-audit every one of the 226 citation records in the r47 draft — C06's exhaustive pass is the owner.
- **Any executor fragment for r48** — none existed at my cut (§2). This review cannot certify a draft it never saw.
- **Any external bibliographic detail** — no network; editions/pages remain `to-verify`, as they should.
- **The post-apply sweep at 224** — only C11's staged tree and the integrator's apply can produce it; my README test was the 223 state.
- **The freshness gate's live run** — O01/O04 own the replay; I read the dispatch declaration only.

---

## 8. Commands and write-surface statement

All run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access …: No such file or directory
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ grep -rni 'cartograph' corpus/knowledge/
cosmology-cosmography.md:102: … not cartographic …
mesoamerica-primary-sources.md:58: | Lienzos and cartographic histories …
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -c '^# ' corpus/README.md
2
$ grep -c '^## ' corpus/README.md
7
$ grep -cE '^- `[a-z0-9._-]+\.md`' corpus/README.md
223
$ wc -l corpus/README.md
575
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223 … totals_line 223 totals_ok True … footer_ok True … exit 0
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ python3 -B reports/round-28/readme/sweep.py --selftest
selftest: 12/12 checks passed          # no H1 control among the controls

# Ca staged edit (scratch only; corpus untouched)
$ sed '3,4d' corpus/README.md > .scratch/r02/readme-fixed.md
$ wc -l .scratch/r02/readme-fixed.md            → 573
$ grep -c '^# ' .scratch/r02/readme-fixed.md    → 1
$ grep -c '^## ' .scratch/r02/readme-fixed.md   → 7
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/r02/readme-fixed.md
rows 223 files 223 … footer_ok True … exit 0
$ sha256sum .scratch/r02/readme-fixed.md
d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
# line drift: totals 544 -> 542; footer 546 -> 544

# Sweep blindness control (in .scratch): delete the rev-2.4 line
$ sed '5d' corpus/README.md > .scratch/r02/readme-no-rev.md
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/r02/readme-no-rev.md
rows 223 files 223 … exit 0            # a corrupted revision history still passes

# Arithmetic
$ python3 -c "print(25+23+25+29+24+94, 25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
220 217 223 224
$ python3 -c "print(0.2*50000, 200/10)"
10000.0 20.0

# r47 over-build reconciliation
C01 358 + C02 503 + C03 287 + C04 301 = 1449 file lines
entry sections C01+C02+C03 = 749 raw lines / 17,619 words
R03: 739 body lines / 17,601 words (10-line boundary delta)
head block C04:112-162 = 51 lines   →  739 + 51 = 790 (r47 validation.json)

# Queue / provenance
$ git blame -L 1,6 corpus/README.md
49ac1a53 :1 / :2      (initial)
57c8409b :3 / :4      (round-36 commit — duplicate H1 introduced)
7ceff59a :5 / :6      (revision 2.4)
$ grep -n 'R36-README-DUPLICATE-HEADING' reports/round-37/op/defect-queue.json reports/round-40/op/defect-queue-v2.json
…:103 / …:112
$ sha256sum reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json
dfc9265d…a3253907  …   9508b6aa…4b1fece58
$ sha256sum reports/round-48/claims.json reports/round-48/targets.json
bf8df21b…00535292  …   d029eaa1…aaa20446

# B-defect spot re-reads
$ grep -c 'archive of coups' corpus/knowledge/linguistics/naming-systems.md → 1 (:70)
$ sed -n '44p' corpus/knowledge/culture-material/craft-artisan-lexicon.md → | Steel (Japan) | tamahagane …
$ sed -n '27p' corpus/knowledge/myth-symbol/cosmology-cosmography.md → … how the world is drawn (maps) …
$ sed -n '79p;184p' reports/round-47/cov/C03-entry-c.md → §1–3 / §2
$ sed -n '123p;137p;150p' reports/round-47/cov/C03-entry-c.md → three update rules
$ sed -n '97,103p' reports/round-47/cov/C03-entry-c.md → 5 form rows
```

---

## 9. Post-cut fragment review (artifacts that landed while §1–§8 were being written)

The wave filed fragments after my baseline read. This section is the review of those bytes; it does not revise §1–§8, and it credits fragments that already caught a finding rather than claiming it twice.

### 9.1 Coverage artifact — C01's entry is right-sized, and the B-defect shapes are gone

Measured from `reports/round-48/cov/C01-entry.md`, fenced body extracted (largest fence, trailing blanks stripped):

```
lines 227   words 4,545   H1 1   H2 14   table rows 81   (to-verify) 10
```

Against r47: **790 → 227 lines (−71.3%)**, table rows **240 → 81 (−66.3%)**, words 17,601 → 4,545. This confirms §3.3's prediction: a 250-line budget is a *row-selection* budget, and the draft cut rows at almost exactly the predicted ratio (~76 predicted, 81 actual). The entry is 1.03× the partition max (221), not 3.6×.

Spot checks of the nine r47 defects in the new bytes:

| Defect | C01's bytes | Verdict |
|---|---|---|
| B1 | entry:66 — "a **20× overstatement**" (200 m vs 10 m) | fixed |
| B2 | entry:3 — "`grep -rni 'cartograph' … 2 lines in 2 files" | fixed |
| B3 | entry:147, :6 — "a map is an archive of coups" used verbatim, "not corrected" | fixed |
| B4 | entry:46 — ladder cited `:54-65`, with `:44` explicitly the material-grading row | fixed |
| B9 | entry:70-97 — **8** form rows | fixed |
| B5/B6/B7/B8 | section cross-refs, one update rule, cosmography `:27` sentence | not exhaustively re-read here; C04/C14/C15/C17 own them. The `:27` boundary is present at entry:3 and the boundary table (entry:32-50) names it |

**No axis harm from the body.** It is method, not renamed r47 bloat: the etymology bank, the duplicated mechanism prose and the standalone decision-record padding that R03 flagged are absent, while the register test, survey chain, form table and calibration bank survive. Whether it is *good* is R03's judgment (absent at my read) — but the over-build class is not repeated on the measured numbers.

### 9.2 Blocking cross-fragment defect — three different `- topic:` lines, and the sweep goes red

This is the finding no other filed fragment carries, and it is the one that would fail the landing:

| Source | `- topic:` length | sha256 (first 16) | Matches seed? |
|---|---:|---|---|
| `reports/round-44/scout/K02-gap-scout.md` (seed) | 766 | `bc7274f411cc6977` | — |
| `reports/round-48/cov/C02-header.md` (head block) | 766 | `bc7274f411cc6977` | **yes** |
| `reports/round-48/cov/C10-readme.md` (README row) | 766 | `bc7274f411cc6977` | **yes** |
| `reports/round-48/cov/C01-entry.md` (its included head block) | **1,045** | `23d94f4122d6ab88` | **no** |
| `reports/round-48/cov/C13-scribe.md` (§5 candidate) | **1,103** | (its own wording, "reduction") | **no** |

The sweep compares the README row to the entry's `- topic:` **byte-for-byte after space-joining** (`reports/round-28/readme/sweep.py:74-82`, `:139-140`). I staged the exact landing shape in `.scratch/r02d/`: 224-file tree + C01's body as `cartography-and-mapmaking.md` + C10's patch-A README (595 lines, sha `5767d3c4…`), then ran a copied sweep at the same relative depth:

```
rows 224 files 224
topic_mismatch 1 ['culture-material/cartography-and-mapmaking.md']
totals_line 224 totals_ok True
footer_ok True
```

Replacing only the entry's `- topic:` block with the 766-char seed text (line count unchanged, 227) turns the same tree **green**:

```
rows 224 files 224
topic_mismatch 0 []
totals_line 224 totals_ok True
footer_ok True
```

So the landing is one line away from red, and the fix is mechanical: **the assembled entry must carry the 766-char seed topic verbatim** (the same text C02 and C10 already use), regardless of which body lands. C01's own file says the two "must agree byte-for-byte" (`C01-entry.md:67`) but then includes a different text; C13's fallback candidate is a third text. The integrator must normalize, not trust.

**Second assembly hazard in the same place: two head blocks.** C01's fence is the complete entry (H1 + 11 fields + body, 227 lines). C02's head fence is 24 lines and also carries an H1 and the fields. A naive concatenation gives ~251 lines, **two H1s** and duplicate `- topic:`/`- gap filled:` fields — the first of which the sweep would read. The only correct assembly is **C02's head block + C01's body starting at `## 1.`**, which measures **24 + 215 = 239 lines**, not 227 and not 250. C05 (length/contract) is the seat that should certify this; it is absent at my read, so this instruction must be in the landing wire (W01) explicitly.

### 9.3 README patches — C10 is byte-correct; C11 is a fixture, not the landing bytes

I applied both C10 variants myself with `patch -p1` in `.scratch`:

- **Patch A** (against live 575-line README): applies clean, **595 lines**, sha256 `5767d3c43d286e0863c44c55cfd1ebe8d13e7d8cd5a19c5d2c3424bc0e25648f` — exactly C10's stated post. Totals at `:564`, footer `:566`; rev 2.5 above rev 2.4; `+24/−4` net `+20`.
- **Patch B** (against the 573-line post-Ca file): applies clean, **593 lines**, sha256 `3960c5e2753a1cb2f8a7345b9f7210ad35405da9fe1189f0fb590772a22cebc7` — exactly C10's stated post. Totals at `:562`.

The rev-2.4 repair in both is `25/23/25/29/24/94 → 25/26/25/29/24/94` = **223**, which is correct. C10 is the landing byte source.

C11's staged README is a **different** artifact: 589 lines, sha `8b025254…`, rev 2.5 block at `:14` (after rev 2.4 at `:4`), totals at `:557`. It is explicitly a method fixture with a 136-line fixture entry, not C10's patch and not C01's body. Its rev block violates the file's newest-first order. C10 §3.3.3 already flags this; I confirm it independently from the staged bytes (`.scratch/r48-c11/stage/corpus/README.md:13-23`). **Do not lift C11's numbers or block**; use C10 A/B and re-run the sweep on the real entry.

### 9.4 Ca artifacts — the queue close exists; the row id does not agree

- **The carried row is closed in W02.** `calib/W02-landing-spec.md:203` files `R36-README-DUPLICATE-HEADING` as a closing row with the parent pinned — which resolves F1. `calib/Ca01-readme-fix.md` is now filed and drafts the same deletion; W02's note that `sed -i '2,3d'` and `'3,4d'` produce identical bytes is correct (both leave title / blank / revision 2.4; 573 lines, sha `d407260d…`). Ca03's independently staged verification agrees.
- **Row-id divergence remains.** `Ca02:107` mints `r47-entry-overbuild-defect-class`; `W02:215` mints `r47-overbuilt-entry-draft` for the same class. R04 already flags it (`R04-readme.md:249`); I confirm it from both fenced JSON blocks. One class, one id: the integrator must pick one and record the other as an alias, or the successor will double-count (the very thing `class_boundary` warns about).
- **Ca02's class content is sound**: `routed-with-owner`, evidence B1–B9 with anchors, parent pin `dfc9265d…`, no filed-byte edit, and a reclass gate that requires pasted landing measurements. I re-verified B1/B2/B3/B4/B7/B9 anchors in §3.4; Ca04 also re-verified all nine.

### 9.5 Still `could-not-evaluate` at my final read

`cov/C05-length-contract.md`, `calib/N02-integrity.md`, `cross/Q01-final-gate.md`, `cross/X03-overbuild.md`, `review/R03-c-content.md`, `review/R05-gate-use.md` were absent. The length/contract certification (C05) is the one that would have caught §9.2 directly; it must run on the assembled 239-line file with the normalized topic. Everything else in §9 is measured from filed bytes.

### 9.6 Findings added by §9

| ID | Sev | Claim | Finding | Evidence |
|---|---|---|---|---|
| **R02-F13** | **B** | C | Three different `- topic:` texts; C01's 1,045-char text makes the staged 224 sweep red (`topic_mismatch 1`); the seed text makes it green. Normalize to the 766-char seed/C02/C10 text before apply. | §9.2; `sweep.py:74-82`; staged `.scratch/r02d` |
| **R02-F14** | **B** | C | Two head blocks (C01's and C02's) must not be concatenated: naive assembly gives two H1s and duplicate fields. Correct assembly = C02 head + C01 body from `## 1.` = **239 lines**. | §9.2; C01:67; C02 fence |
| **R02-F15** | P2 | C | C13's §5 is a third independent entry candidate (181 lines, 1,103-char topic) written because no sibling existed at its cut. It is a fallback, not a second landing; the round must name C01's body (normalized) as the single byte source. | `C13-scribe.md:6,103`; §9.2 table |
| **R02-F16** | P2 | Ca | Ca02 and W02 mint different ids for the one over-build row. Pick one canonical id, alias the other. (R04 caught it; confirmed here.) | `Ca02:107`; `W02:215`; `R04:249` |

**Updated axis statement.** Coverage is still +1 genuine and the body now exists at 227 lines with the r47 defect shapes fixed; the only blocking risk is assembly (F13/F14), not content. Calibration is +1 if the queue close uses one id — the fix bytes themselves are byte-verified (patch A/B). No axis is harmed by any filed byte; both blockers are one-line/normalization problems caught before apply.

---

**Write surface:** this file only — `reports/round-48/review/R02-review.md`. `corpus/**`, `tools/**`, `README`, `LOG.md`, filed rounds, `tools/gates/frozen/**` and fleet `.ufo/**` were read, not written; the only writes outside this file were disposable `.scratch/r02/` copies. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
