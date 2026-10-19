# R01 — whole-round review (non-author)

- Seat: `R01` | role: reviewer | claim: **cross** | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19) — equals `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`), so there is no baseline drift of the r43 kind.
- Out path: `reports/round-48/review/R01-review.md` (this file).
- Non-author statement: I drafted no C or Ca fragment, ran no seat's task, and edited no corpus, tool, queue or README byte. Every judgement below is from live commands at the baseline, the r47 filed bytes, and disposable `.scratch` mirrors. Commands in §10.

**One-line judgment.** Both claims' **premises are true at `a01405d`** — cartography is genuinely unowned (0 filename owners, 0 topic owners, slug absent), the README duplicate-H1 is live (grep count 2 at `:1` and `:3`), and the partition arithmetic is sound. Neither claim's `after_required` is yet met or yet measurable: **zero C or Ca deliverable fragments were filed at my write cut** (`reports/round-48/` held only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`). I found **three blocking defects in the round contract and disposition mechanics** that would let the round repeat r47's failure class even if the entry is good: an unreproducible freshness-gate result, a wrong repair-vector arithmetic in C10, and an unclosed queue row that Ca's fix would leave open. I also found the structural reason r47 reached 790 lines still present in r48's seat plan: **five separate C seats are chartered to write concatenable content blocks**. Per-axis: **coverage not yet moved (223 holds), calibration not yet moved, no axis harmed on disk.**

---

## 1. Artifact census at my write cut

```
reports/round-48/
├── claims.json
├── targets.json
└── telemetry/dispatch-declared.json
```

No `cov/`, `calib/`, `review/` (before this file), `cross/`, `plan/`, `scribe/`, `op/`, `adj/` fragment existed. Consequences, stated rather than papered over:

| Required by the contract | Status at my cut |
|---|---|
| C: entry + header + audits + README rev 2.5 + sweep | **could-not-evaluate** — no draft exists |
| Ca: README fix + over-build queue row + heading control | **could-not-evaluate** — no fix or row filed |
| Freshness gate's declared C/Ca FRESH | **could-not-evaluate** — not reproducible (§6, R01-48-01) |
| Observed dispatch / availability close | owned by S02; only `dispatch-declared.json` exists |

This review therefore judges: (a) each claim's declared `before` premise, (b) the arithmetic and mechanics the round has already committed to, and (c) the full r47 B1–B9 defect class that the C draft must not reproduce. It does **not** certify a landing.

---

## 2. Independent live measurements

Run from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

| Measurement | Command | Output |
|---|---|---|
| HEAD | `git rev-parse HEAD` | `a01405dd36367292255c2652ac0a601f4cd6a0af` |
| Worktree | `git status --porcelain` | only `?? reports/round-46/review/`, `?? reports/round-48/` |
| Entry total | `find corpus/knowledge -name '*.md' \| wc -l` | **223** |
| Partitions | per-directory `ls *.md \| wc -l` | civ 94 / cm **25** / ling 25 / myth 26 / synth 29 / verif 24 |
| Sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`; missing 0; topic_mismatch 0; orphan 0; drift {}; totals 223 ok; footer ok; `readme_sha256 7c788a1d…`; exit 0 |
| Sweep self-test | `… sweep.py --selftest` | **12/12 PASS** — and **none of the 12 counts H1s** |
| Cartography filename owners | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` | **0** |
| Cartography slug | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | No such file |
| Cartography topic owners | `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr\|survey map\|world map\|graticule\|theodolite)' corpus/knowledge/ \| wc -l` | **0** |
| `cartograph` body hits | `grep -rni 'cartograph' corpus/knowledge/` | **2 files / 2 lines**: `myth-symbol/cosmology-cosmography.md:102`, `civilizations/mesoamerica-primary-sources.md:58` |
| `cadastr` body hits | `grep -rni 'cadastr' corpus/knowledge/` | 2: `culture-material/architecture-settlement-lexicon.md:95`, `civilizations/japan-medieval-sengoku.md:157` |
| README H1 count | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | **2** (lines 1 and 3, byte-identical under `cat -A`) |
| README sha | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`, 143,866 bytes |
| Live band | `wc -l corpus/knowledge/culture-material/*.md` | min 103 / **median 149** / max 221 (25 files) |
| Head vs body split | first `^## ` per entry | head min 7 / median 12 / max 42; body min 91 / **median 138** / max 179 |

Arithmetic checks (`python3 -c`): `25+23+26+25+24+94 = 217`; `25+26+25+29+24+94 = 223`; `25+26+26+29+24+94 = 224`.

---

## 3. Claim C — coverage: named-verifier judgment

### 3.1 Premise: PASS, with one qualification

- **Fresh:** the gap is unowned at the baseline by the two tests the claim names (§2). The r44 K02 sweep is the originating proposal, and `reports/round-44/validation.json:9` records "the fresh gap (cartography, K02) has no entry body. No corpus delta", so r45–r47 did not land it. The r47 round re-verified 0 owners and correctly did not land (`reports/round-47/validation.json:9`).
- **Qualification (carried from r47, still live):** `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` defines cosmography as "how the world is drawn (**maps**), named … walked … built". The entry must say in one sentence why that is the *cosmogram/world-picture*, not the surveyed sheet, or the "owns no made map" sentence overstates. r47 R03 filed this as B8 and the r48 C draft has not yet answered it.
- **Sort position:** between `calendar-festival-systems.md` (`corpus/README.md:240`) and `costume-semiotics.md` (`:241`). Checked against the live section listing at `:234-243`; `cartography…` sorts after `calendar…` (`car` > `cal`) and before `costume…` (`car` < `cos`). No `cart*` row exists anywhere else; `corpus/README.md:340` is `carthage.md`, a different partition and a false prefix match.

### 3.2 Contract arithmetic: C10's repair vector is wrong

`reports/round-48/targets.json:28` (C10) says the rev-2.4 repair is:

> "(synthesis 25->29, myth-symbol 23->26, culture-material 26->25 **= 224**)"

Those three corrections applied to the defective prose vector `25/23/26/25/24/94` produce `25/26/25/29/24/94`, which sums to **223**, not 224. Verified against the live line `corpus/README.md:11` (the prose vector that sums to 217) and the correct live footer `corpus/README.md:548` (`25/26/25/29/24/94`, sums 223). The repair of rev 2.4 can only recreate the **223** state; the **224** state belongs to the new rev 2.5 line `25/26/26/29/24/94`. A seat that obeys C10's wording literally will write a claim that its own arithmetic contradicts — the exact r47 failure (unverified arithmetic) reappearing in the round contract. See **R01-48-02**.

### 3.3 Right-sizing: measured, not asserted

r47's assembly was **790 lines = 51 head + 739 body** (`reports/round-47/cross/Q01-final-gate.md:87`; also `reports/round-47/validation.json:9`). My own mechanical count of *every* fenced block in the four fragment files (C04 + C01 + C02 + C03) is 713 lines — that is not the assembly (it includes the audit fences and omits inter-fence prose), so I use Q01's decomposition rather than inventing a second number. R03's "739 body lines" is the body half of the same 790; the `790` and `739` figures are two parts of one measurement, not a conflict.

Against the live band (§2):

| Measure | Live | r47 draft | Factor |
|---|---:|---:|---:|
| total | 103–221, median 149, max 221 | 790 | **3.6× max** |
| body | 91–179, median 138, max 179 | 739 | **4.1× max / 5.4× median** |
| head | 7–42, median 12 | 51 | 1.2× max |

**Budget I will judge the r48 draft against:**

- head ≤ **25** lines (live median 12; includes H1 + all header fields + source shelf),
- body ≤ **180** lines (live max 179; this is a ceiling, not a target),
- total ≤ **205**, hard ceiling **221**. `<=~250` in the claim is a fail-safe, not a target: an entry that lands at 250 becomes the new partition maximum and ships the usability regression r47 was refused for.

At 205 lines the entry still fits the load-bearing skeleton: one register-test table, one survey-chain table, one 8-row form typology, one projection/scale/orientation/symbol section, one reproduction/trade section, one warrant/provenance section, one silences section, one calibration bank, a ≤25-line worked example, recheck + scope. Nothing in that list needs the 240 table rows r47 used.

### 3.4 Structural risk: five C seats are chartered to write concatenable blocks

r47 reached 790 by concatenating three body fragments (358 + 503 + 287 file lines). r48's plan repeats the shape with **five content authors**:

| Seat | `targets.json` | Deliverable |
|---|---|---|
| C01 | `:19` | "the complete entry body … Fenced entry body" |
| C02 | `:20` | header block, "Fenced block" |
| M01 | `:65` | worked micro-example |
| M02 | `:66` | calibration bank |
| E01 | `:81` | boundary table |

If the integrator concatenates all five fences, over-build is mathematically likely regardless of each seat's local discipline. **Recommendation (blocking for the C assembly):** one author, C01, writes the single ≤205-line file; C02/M01/M02/E01 deliver **verifier notes or proposed rows**, not fenced blocks for concatenation; the integrator applies exactly one fenced entry body plus one header, never five fragments. This is the only structural change that prevents the class rather than re-testing it.

### 3.5 Delivery: could-not-evaluate

No draft, so no `after_required` leg is measurable: entry length, contract fields, arithmetic, citation anchors, worked-example consistency, README rev 2.5, and the 224 sweep all remain open. **Coverage is not `improved` at my cut; it is unmeasured.** Nothing on disk harms it.

---

## 4. Claim Ca — calibration: named-verifier judgment

### 4.1 The duplicate heading is live and the sweep is blind to it

- `grep -c` → **2**; `grep -n '^# '` → lines **1** and **3**, byte-identical. `corpus/README.md:5` is the rev-2.4 block, so `:4` is a blank line and the second H1 is a stray duplication.
- The sweep goes **green with the duplicate present** (§2), and its self-test battery (12/12) has no H1 control. The claim's `before` is therefore true, and the "heading-count control the sweep lacks" is a real absence, not a rhetorical one.

### 4.2 The fix is safe — verified in a disposable mirror

I copied `corpus/` and `reports/round-28/readme/sweep.py` into `.scratch/r01/tree[B]` (never editing `corpus/`) and staged two variants. The sweep resolves its lane root from its own path (`sweep.py:44-45`: `HERE` → `LANE`), so the mirror is a faithful harness.

| Variant | Edit | Resulting head | sha256 | bytes | H1 count | Sweep |
|---|---|---|---|---:|---:|---|
| A | delete line 3 only | title, blank, **blank**, revision | `84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633` | 143,833 | 1 | exit 0, all legs green |
| B | delete lines 3–4 (H1 + its blank) | title, blank, revision | `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` | 143,832 | 1 | exit 0, all legs green |

Both satisfy the letter of the claim ("grep count 2 → 1"). **B is the correct act**: removing the title and leaving two blank lines is not a clean repair, and the queue row says "remove the redundant title", not "delete one line". The recorded act must name its variant and the **measured post-apply sha** — A or B, not "should be". My prediction for B is `d407260d…` at 143,832 bytes, which is a prediction until the applied bytes are hashed.

### 4.3 Ordering hazard: the fix shifts every C README anchor

This is the cross-claim defect neither claim's text mentions:

| Anchor used by C | Live | After variant A (−1) | After variant B (−2) |
|---|---:|---:|---:|
| `revision: 2.4` line | 5 | 4 | 3 |
| rev-2.4 prose vector | 11 | 10 | 9 |
| `## culture-material/ (25)` | 234 | 233 | **232** |
| calendar row | 240 | 239 | **238** |
| costume row | 241 | 240 | **239** |
| `Total knowledge entries:` | 544 | 543 | **542** |
| counts footer | 548 | 547 | **546** |

Measured on the staged trees, not computed. If the Ca fix lands first and the C README edit is then applied at the filed line numbers, it edits the wrong lines — the r47 miscite class with a live consequence. **Requirement:** one combined README edit computed by content match (not line number), followed by the sweep and the H1 count as the only delivery certificate. See **R01-48-03**.

### 4.4 Over-build disposition: shape is right, one row is missing

Verified queue facts:

- The parent is `reports/round-40/op/defect-queue-v2.json`, sha256 **`dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`**, which matches the pin in `reports/round-43/calib/defect-queue-v2-successor-r43.json:7`. The successor pattern (new file, parent pinned, never in-place) is correct and must be followed.
- **No over-build / length-discipline row exists** in the v2 queue or the r43 successor (`grep -niE 'over-?build|length discipline|790|right-siz'` → no row hits), so the r47 class is genuinely undispositioned.
- **But `R36-README-DUPLICATE-HEADING` is already a live row**: `reports/round-40/op/defect-queue-v2.json:112-119`, class `carried-with-owner`, owner "integrator to assign a corpus-index editor", `next_touch` "r42 or r44 … remove the redundant title as a separate recorded act, then re-run the sweep plus a heading-count control the sweep lacks". If Ca fixes the heading without adding a `fixed-with-evidence` row for **that id**, the queue still carries the finding open after the repair — a stale row is the same integrity failure as a missing one. Ca02's mission (`targets.json:34`) names only the over-build row.

Class recommendation for the over-build row: **`carried-with-owner` / v2 `carried-with-owner`**, not `fixed-with-evidence`. The r48 right-sized landing proves the class is *avoidable*, not that it is *prevented*; prevention is the length-discipline control (sweep leg or gate probe), which does not exist. `next_touch` should therefore be the control, not the redraft. Note also that the freshness gate cannot express "≤ N lines": its probe vocabulary is closed (`tools/harness/claims-freshness.py:96-106` — `path_absent`, `path_present`, `grep_absent`, `count_eq`, `sha256_eq`, `topic_owner_absent`, `capability_present`), so a length guard needs a new probe kind or a sweep leg. The gate guards topic ownership, exactly as the claim says, and cannot be stretched to entry quality without new code.

### 4.5 Delivery: could-not-evaluate

The fix is **verified in staging**, not applied. The over-build row and the control do not exist. Calibration is not `improved` at my cut.

---

## 5. The r47 B1–B9 class, re-verified from the filed bytes

I re-read every defect independently; all nine are real, and the correct fix for each is pinned here so the r48 C draft and its verifiers do not have to trust a summary.

| ID | r47 site | What I measured | Correct fix |
|---|---|---|---|
| **B1** | `reports/round-47/cov/C02-entry-b.md:98` | The surrounding scale lines are right (`1 mm × 50,000 = 50 m`; `1 mm × 1,000,000 = 1 km`). The bad clause: 0.2 mm on 1:50,000 = **10 m** of ground; a survey closing at 200 m is **20×** coarser, not "ten times". `0.2 × 50,000 = 10,000 mm = 10 m`; `200 ÷ 10 = 20`. | "twenty times", or change 200 m → 100 m. Do not touch the rest. |
| **B2** | `reports/round-47/cov/C04-entry-header.md:115` | `grep -rli 'cartograph'` cannot yield "2 files / 3 lines"; `grep -rni 'cartograph'` → **2 lines / 2 files** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`). `:71` contains "Mappa Mundi" / "survey maps", not the token. | Write 2 files / 2 lines; keep `:71` as the disclaimer citation, uncounted. |
| **B3** | `reports/round-47/cov/C02-entry-b.md:36`, `:501` | The accusation is false. `grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md` → `70:… Every renaming is datable; a map is an archive of coups.` C01's quote is exact; C02's proposed "archive of renamings" would have invented a phrase. | Drop C02's correction. Keep the exact quote; mark any paraphrase as paraphrase. |
| **B4** | `reports/round-47/cov/C02-entry-b.md:248`, audit `:421` | `craft-artisan-lexicon.md:44` is the **Steel (Japan)** material-grading row. The ladder is `:54` (header), `:56-63` (seven systems), `:65` (design rule). | Anchor the ladder at `:54-65`; keep `:44` only for material grading; correct the audit row's description. |
| **B5** | `reports/round-47/cov/C03-entry-c.md:79`, `:184` | The form typology is C01 **§4.1** (`reports/round-47/cov/C01-entry-a.md:238`, "### 4.1 The eight forms"). `:79` says "§1–3"; `:184` says "§2". | Both → §4.1. |
| **B6** | `reports/round-47/cov/C01-entry-a.md:298` | Provenance/charter is **§8** (`reports/round-47/cov/C02-entry-b.md:278`); §9 is the container-name fossil (`:347`). | `§9` → `§8` in the handoff note. |
| **B7** | `reports/round-47/cov/C03-entry-c.md:123`, `:137`, `:150` | Three incompatible update rules: `:123` "re-survey after any storm that breaches a dike"; `:137` "not due until the levy year turns"; `:150` "after a dike breach, per levy year". C14 independently failed this (`reports/round-47/cov/C14-example.md:11` verdict, `:78` FAIL row, §4 at `:92`). | One rule, stated once: sheet A updates at the levy year; the joint rule is after every breach. Make `:123` say that. Then re-run the example audit. |
| **B8** | `reports/round-47/cov/C01-entry-a.md:90,96`; `C04:115` | `cosmology-cosmography.md:27` says cosmography is "how the world is drawn (**maps**)", a competing definition the "owns no made map" sentence never answers. `:71`/`:102` are the disclaimers. | Add the one-sentence boundary: cosmography owns the world-drawn/cosmogram content (`:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production. |
| **B9** | `reports/round-47/cov/C03-entry-c.md:95-103` | The "minimum credible build per form" table has **5** rows (itinerary, cadastral, portolan, chorographic, cosmographic); C01 §4.1 lists **8** (`C01:238-249`). Celestial, thematic, cartographic-history/lienzo missing. | Retitle "five common forms" **or** add the three rows. Do not imply eight. |

Additional audit-chain defect I found while re-reading: `reports/round-47/cov/C14-example.md:206` quotes `:123` as "at the levy year / at the next levy", but the live `C03:123` reads "re-survey after any storm that breaches a dike". The audit was pinned to superseded bytes (Q01 already flagged the chain as superseded, `reports/round-47/cross/Q01-final-gate.md:118`). **Lesson for r48: every verifier must re-read the live draft bytes it certifies; a verdict quoting text that is not in the current fragment is void.** See **R01-48-07**.

---

## 6. Findings

Severity: **B** = must fix before the round can claim either `after_required`; **P2** = should fix; **P3** = note.

### Blocking

**R01-48-01 — The declared freshness-gate result is not reproducible from any filed artifact.**
`reports/round-48/claims.json:21-25` and `reports/round-48/telemetry/dispatch-declared.json` declare "C FRESH; Ca FRESH; O STALE", but `claims.json` carries no `before_checks`/`freshness_probes` for either claim. Re-running the gate on the filed claims:

```
$ python3 tools/harness/claims-freshness.py --claims reports/round-48/claims.json --root .
claims-freshness: round 48 baseline a01405d (a01405dd…)
  [C] COULD-NOT-EVALUATE no before_checks declared; a claim with no declared checks is not fresh
  [Ca] COULD-NOT-EVALUATE no before_checks declared; a claim with no declared checks is not fresh
summary: 0 fresh, 0 stale, 2 could-not-evaluate, 0 malformed
REFUSE: …
exit 3
```

The gate's own contract says a claim with no declared checks is *could-not-evaluate*, never fresh (`tools/harness/claims-freshness.py:45-47`). **Fix:** file the overlay actually used (the `--checks <overlay>` file) and its JSON output under `reports/round-48/telemetry/`, with the gate's baseline and exit code; O01/O04 re-run and file. Until then the round record must mark the declaration `to-verify`, not "fresh". This is the AGENTS.md durability rule applied to the round's own headline evidence.

**R01-48-02 — C10's rev-2.4 repair arithmetic sums 223, not 224.**
`reports/round-48/targets.json:28`. The three corrections named produce `25/26/25/29/24/94 = 223`. **Fix:** split the act explicitly — rev-2.4 repair yields the 223 vector `25/26/25/29/24/94`; the new rev-2.5 line yields `25/26/26/29/24/94 = 224`. Two lines, two sums, each verified. Do not let one sentence claim to deliver both.

**R01-48-03 — Ca's `:3` removal shifts every downstream C README anchor.**
Measured in `.scratch` (§4.3): variant A shifts by −1, variant B by −2, so `:234/:240/:241/:544/:548` become `:233/:239/:240/:543/:547` (A) or `:232/:238/:239/:542/:546` (B). **Fix:** a single combined README edit computed by content match; after apply, re-hash and re-run the sweep and the H1 count. Any C fragment that quotes README line numbers must quote them against one named variant.

**R01-48-04 — Ca must close the existing queue row `R36-README-DUPLICATE-HEADING`.**
`reports/round-40/op/defect-queue-v2.json:112-119` is a live `carried-with-owner` row whose `next_touch` is exactly "remove the redundant title as a separate recorded act, then re-run the sweep plus a heading-count control the sweep lacks". Ca02's mission (`targets.json:34`) names only the over-build row. **Fix:** the successor carries two rows — `fixed-with-evidence` for `R36-README-DUPLICATE-HEADING` (pre/post grep + post-apply sha + sweep output) and the over-build class row. Otherwise the repair leaves a stale open row, which is the same defect in another place.

### Should fix

**R01-48-05 — One author, not five, or the assembly repeats r47.**
`targets.json:19,20,65,66,81` charter five C seats to produce fenced content. r47's 790 lines came from concatenating three. **Fix:** C01 writes the single ≤205-line file; C02/M01/M02/E01 supply notes or row proposals that C01 integrates. The integrator applies one body.

**R01-48-06 — The right-sizing gate cannot be a freshness probe; name the real control.**
The gate's probe vocabulary is closed and cannot express a line ceiling (`claims-freshness.py:96-106`). Ca's "heading-count control" is feasible as a sweep leg (the sweep parses the README at `sweep.py:85` and returns its report at `:195`; the self-test harness is at `:239`), but a new leg without a planted control is itself unverified. **Fix:** Ca05's diff adds a `heading_findings` leg **and** a 13th self-test (a two-H1 fixture must be flagged); the over-build control is either a new probe kind or a documented manual check with owner, not a claimed gate.

**R01-48-07 — Audit verdicts must be re-taken on the current bytes.**
`C14:206` quotes text not present at `C03:123`; the r47 chain certified superseded fragments. **Fix:** every r48 verifier states the sha256 of the fragment it read; the integrator re-runs the length, arithmetic, citation and example legs on the assembled body, not on the pre-assembly fragments. This is the r47 lesson (Q01:118) restated as a r48 gate.

### Note

**R01-48-08 — The `790` vs `739` figures are not in conflict.**
`reports/round-47/validation.json:9` says 790 lines; R03 says 739 body lines; Q01:87 gives `790 lines (51 head + 739 body)`. The round's prose should use the decomposition once, or reviewers will keep re-litigating a non-defect.

---

## 7. Axis verdicts

| Axis | Verdict at my cut | Basis |
|---|---|---|
| **Coverage** | **not moved; not harmed.** Premise green, delivery absent. | 223 entries, 0 owners, no draft (§3.5) |
| **Calibration** | **not moved; harm prevented.** Two contract defects found before they could land, and the README fix is staging-verified. | §3.2, §4.2, §4.3 |
| **Depth / adjacency / freshness / operability** | untouched by this round's declared scope (`claims.json` non_goals), and nothing on disk touches them. | `git status` clean; no corpus write |

**No axis is harmed by anything on disk.** The C topic is the right topic, the Ca fix is the right fix; the defects are in arithmetic, ordering and disposition bookkeeping — all correctable before apply.

---

## 8. Landing gates the integrator must satisfy

1. **C evidence:** one assembled entry body, head ≤25 / body ≤180 / total ≤205 (hard 221), sha256 named; every r47 B1–B9 checked against §5; the `cosmology-cosmography.md:27` sentence present; worked example one update rule; 8-of-8 form table or an explicit "five common forms" title.
2. **Arithmetic:** 223 → 224; culture-material 25 → 26; footer vector `25/26/26/29/24/94`; rev-2.5 sums 224; rev-2.4 repair sums 223.
3. **README:** one combined edit after the Ca fix; heading count 1; sweep `rows 224 files 224`, 0 missing/mismatch/orphan, totals 224, footer ok, exit 0; post-apply sha recorded.
4. **Ca:** post-apply H1 count 1; sweep green; queue successor (new file, parent pinned at `dfc9265d…`) carries **both** `R36-README-DUPLICATE-HEADING` fixed-with-evidence and the over-build class carried-with-owner.
5. **Freshness:** the overlay and its output filed under `reports/round-48/telemetry/`; until then the declaration is `to-verify`.
6. **Write surface:** exactly one new corpus file + `corpus/README.md`; no `M` on any other corpus entry; all seat writes under `reports/round-48/`.

---

## 9. What I did not verify

- **Any C or Ca deliverable.** None was filed at my write cut; §1. My defect table §5 is a review of r47's filed bytes, not of an r48 draft.
- **External bibliography.** No network at seat time; every edition/page remains `(to-verify)`.
- **The r48 freshness overlay.** It does not exist; I could only show the filed claims fail to reproduce FRESH (§6, R01-48-01).
- **The final combined README bytes.** My two variant shas are staging predictions; the applied bytes must be hashed.
- **The queue successor file.** It does not exist; I verified the parent pin and the row that must be closed.
- **Observed dispatch/availability.** S02's scope; only the declaration is on disk.

---

## 10. Commands and write-surface statement

All commands from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223 … totals_ok True … footer_ok True … readme_sha256 7c788a1d… ; exit 0
$ python3 -B reports/round-28/readme/sweep.py --selftest
selftest: 12/12 checks passed ; exit 0
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ grep -rni 'cartograph' corpus/knowledge/          # 2 lines / 2 files
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:…
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:…
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ python3 -c "print(25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
217 223 224
$ wc -l corpus/knowledge/culture-material/*.md | …     # min 103 / median 149 / max 221
$ python3 tools/harness/claims-freshness.py --claims reports/round-48/claims.json --root .
[C] COULD-NOT-EVALUATE … [Ca] COULD-NOT-EVALUATE … exit 3
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
# staging (disposable mirrors; corpus/ never edited)
$ python3 .scratch/r01/tree/reports/round-28/readme/sweep.py    # variant A: H1=1, green, sha 84e16f56…
$ python3 .scratch/r01/treeB/reports/round-28/readme/sweep.py   # variant B: H1=1, green, sha d407260d…
```

**Write surface:** this file only — `reports/round-48/review/R01-review.md`. No `corpus/**`, `tools/**`, queue, README, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. The two README variants exist only under `.scratch/r01/` (disposable). No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed. No re-freeze, no packet-surface change.
