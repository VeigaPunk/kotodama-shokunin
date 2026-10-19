# P01 — cross-claim plan (round 48, loop-2 position 2)

- Seat: `P01` | role: planner | claim: **cross** | date 2026-10-19
- Out path: `reports/round-48/plan/P01-plan.md` (this file; no corpus or tool bytes written)
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`); `git status --porcelain` at my read → `?? reports/round-46/review/`, `?? reports/round-48/`
- Contract read: `reports/round-48/claims.json` (C `:27-39`, Ca `:41-52`), `reports/round-48/targets.json` (P01 row `:16`; 64 seats), `reports/round-48/telemetry/dispatch-declared.json` (`:18-21`)
- Inputs read: `reports/round-47/review/R03-c-content.md` (B1–B9 `:188-196`, volume `:92-96`, P2 `:198-212`), `reports/round-47/cross/Q01-final-gate.md` (`:16`, `:87`, `:106`, `:289`), `reports/round-44/scout/K02-gap-scout.md` (`:3.2-3.5`), `reports/round-47/calib/queue-successor-r47.json`, `reports/round-47/calib/Ca06-queue-successor.md`, and the r48 sibling artifacts reconciled here: `reports/round-48/scout/K01-rightsized-spec.md`, `scout/K02-readme-defect.md`, `calib/Ca05-heading-control.md`, `cov/C11-sweep.md`, `cross/N01-numbers.md`; `corpus/QUALITY.md`, `corpus/README.md`, `reports/round-28/readme/sweep.py`, `tools/gates/provenance-audit.py`

**Plan in one line.** Land C only as **one assembled, right-sized entry (target 225–240 lines, hard stop 250)** whose audits run on the **final bytes**, and land Ca as **one README write plus one new successor artifact**; because both claims touch `corpus/README.md`, stage **one final README** and have the integrator apply it once, never as two blind patches with shifting line numbers.

---

## 1. Axes and move conditions

| axis | measured state at `a01405d` | accepted move only if | harm tripwire |
|---|---|---|---|
| **coverage** (lowest non-retired) | 223 total; culture-material 25; cartography slug absent; 0 strict topic owners; 2 `cartograph` lines in 2 files, both by-product | 224 total / 26 culture-material; one entry at 225–240 lines (≤250); audits PASS on the **final assembled bytes**; README rev 2.5 sweep-green 224==224; vector sums 224; no overwrite | landing a carried topic, a second owner of cosmography/pilgrimage/direction/architecture, an over-build again, or an arithmetic/citation defect |
| **calibration** | README has 2 H1s (`:1`, `:3`); rev-2.4 vector prints 217, not 223; no heading-count control; r47 over-build class absent from the queue successor | H1 count 2→1; heading control lands and exits 0; new queue-successor row names the over-build class with owner + next_touch + evidence; sweep still green | deleting revision history, touching another H1/heading, editing a filed round, or marking the over-build row fixed before the landing |
| **process integrity** (binding constraint, not a scored axis) | r47 failed on unverified arithmetic, miscites, and audits pinned to superseded bytes | every number recomputed; every `path:line` re-read; one final byte object audited; only declared out paths written | staging under `corpus/`, editing `reports/round-1..47/**`, running `reports/round-*/run-validation.py` in-tree |

The claims' axes are `coverage` and `calibration` (`claims.json:15-18`). The freshness gate already cleared C and Ca at declaration and dropped O (`telemetry/dispatch-declared.json:18-21`); this plan does **not** re-claim that gate result — it replaces it at landing with direct ownership and collision commands (§3.4, G0).

---

## 2. Measured baseline (commands run by this seat, not asserted)

```text
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo EXISTS || echo ABSENT
ABSENT
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -rni 'cartograph' corpus/knowledge/
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:... T-O diagrams are symbolic devices, not cartographic claims ...
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:| Lienzos and cartographic histories ... |
```

```text
$ grep -c '^# ' corpus/README.md
2
$ sed -n '1,6p' corpus/README.md | nl -ba
     1  # kotodama-shokunin corpus index
     2
     3  # kotodama-shokunin corpus index
     4
     5  revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
     6  myth-symbol entries landed (`mineral-stone-symbolism.md`,
$ grep -n '25/23/26/25/24/94' corpus/README.md
11:the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
$ grep -n 'Total knowledge entries\|total 223 files\|## culture-material' corpus/README.md
234:## culture-material/ (25)
544:Total knowledge entries: 223.
548:(total 223 files; directory totals 25/26/25/29/24/94).
```

```text
$ python3 - <<'PY'
import glob, statistics
lines=[len(open(f).read().splitlines()) for f in glob.glob('corpus/knowledge/culture-material/*.md')]
print(len(lines), min(lines), statistics.median(lines), max(lines))
PY
25 103 149 221
```

```text
$ sha256sum corpus/README.md tools/harness/claims-freshness.py \
    reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d  tools/harness/claims-freshness.py
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json
9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58  reports/round-47/calib/queue-successor-r47.json
```

`reports/round-47/calib/queue-successor-r47.json` parses to **3 rows** + 2 provider amendments; ids are `r43-stale-premises`, `r44-resolver-hyphen-after-blank`, `manifest-ledger-two-schema-evolution`. **No over-build row exists.** It is tracked and clean, and pins its parent at `dfc9265d…`.

### 2.1 Arithmetic ledger (recomputed here; every later draft uses these values)

| expression | result | use |
|---|---:|---|
| 223 + 1 | **224** | total after C |
| 25 + 1 | **26** | culture-material after C |
| 25+26+25+29+24+94 | **223** | live vector (section order: linguistics, myth-symbol, culture-material, synthesis, verification, civilizations) |
| 25+26+26+29+24+94 | **224** | landing vector |
| 25+23+26+25+24+94 | **217** | the rev-2.4 prose defect (understates myth-symbol and synthesis, overstates culture-material) |
| 25+26+25+29+24+94 | **223** | corrected rev-2.4 after-vector |
| 0.2 mm × 50,000 | **10,000 mm = 10 m** | B1 ground precision |
| 200 m ÷ 10 m | **20×**, not 10× | B1 correction |
| 739 ÷ 149 | **4.96 ≈ 5.0×** | r47 body vs median |
| 739 ÷ 221 | **3.34 ≈ 3.3×** | r47 body vs max |
| 790 ÷ 149 | **5.30 ≈ 5.3×** | r47 assembly vs median |
| 790 ÷ 221 | **3.57 ≈ 3.6×** | r47 assembly vs max |

**Correction to the C10 mission shorthand.** `targets.json` C10 phrases the repair as “synthesis 25→29, myth-symbol 23→26, culture-material 26→25 = 224”. Applied literally that produces `25/26/25/29/24/94` = 223, not 224. Use the vectors, not the shorthand: **rev-2.4 repair ends at `25/26/25/29/24/94` (223); rev-2.5 ends at `25/26/26/29/24/94` (224).**

---

## 3. Claim C — right-sized cartography entry

### 3.1 Landing path and freshness contract

- Target: `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (new file; verified absent at `a01405d`).
- Partition: culture-material; slug sorts **after** `calendar-festival-systems.md` and **before** `costume-semiotics.md` (`ls corpus/knowledge/culture-material/ | nl` → calendar 5, costume 6).
- Ownership: 0 filename owners, 0 strict topic owners, 0 prior landing. The r44 K02 seed is this claim's provenance, not carriage; no **other** round proposed the topic (`K02-gap-scout.md:85`, `:197-205`).
- The entry must not become a general history of cartography: it owns the **surveyed, projected, reproduced sheet as production** and ends at the handoff.

### 3.2 Right-sized envelope (the anti-r47 rule; aligned to K01 §3)

K01's measured spec is the binding skeleton: **header 27 + 10 body sections = 230 lines**, target band **225–240**, ceiling **250**. Do not re-open a 15-section skeleton.

| new § | lines | absorbs (r47) | must keep / must cut |
|---|---:|---|---|
| head | 27 | head 51 | H1; one-line `topic` (byte-equal); `gap filled`; grouped 5-bullet external shelf (`(to-verify)`, no digests); 12 in-corpus anchors; `source`; `couples`; `verified-at`; `recheck`; `scope`. Cut the 24 lines of field rationale and 18 single-line external bullets. |
| 1 ownership | 26 | §1 (23) | master claim; four choices; **13-row boundary table** (12 neighbours + divination non-collision); the `cosmology:27` sentence. |
| 2 register test | 18 | §2 (45) | five conditions; 8-row object table; “partial = fail”; stipulative wording for the stick chart. |
| 3 survey chain | 22 | §5 (108) | seven links + artifact + failure; weakest-link rule; error budget. |
| 4 projection/scale/symbol | 22 | §3 (80) | 5-row projection table; corrected B1 scale paragraph; compass trap; 5-row symbol table. |
| 5 form typology | 20 | §4 (53) | **all eight forms** with question / minimum build / institution / cannot-show. |
| 6 cost and trade | 20 | §6+§7 (129) | four scarcity regimes; 4-row cost stack; working vs monument; 4-row role table; three rules. |
| 7 provenance/legal | 20 | §8+§13 (90) | 5-row warrant chain; four provenance failures; contest rule; map-is-territory reconciliation; four `DR-CT` rows folded in. |
| 8 build + example | 33 | §10+§11 (81) | nine build steps, one line each; one lagoon / two sheets / one storm; **one update rule stated once** (B7). |
| 9 calibration | 14 | §12 (35) | 8-row bank with R/C/B/H/T codes. |
| 10 recheck/scope | 8 | §14+§15 (40) | four recheck triggers; limits; scope + handoff. |
| **total** | **230** | 739 | **hard stop 250; do not land >250** |

**Cut whole sections (do not renegotiate upward):**

1. **Standalone container-name fossil bank** (r47 §9, 55 lines) — drop; retain at most one `mappa` clause in §2 if the register test needs it.
2. **Standalone 12-row decision record** (r47 §13, 21 lines) — fold the four load-bearing `DR-CT` rows into §7.
3. **Mechanism restatement in the build order** — §8 sequences; §4 describes.
4. **Duplicate bullets between sections** — “the blank has three readings” and “the boundary line” appear once (`R03:94`, P2-3).

**Kill list (r47 over-build causes, all confirmed in R03):**

1. No second statement of projection/scale/orientation/symbolization in the build order (`R03:94-96`, P2-3).
2. No 240 table rows: cap the entry near **100** table rows; every row must carry a decision.
3. No 29 scattered `(to-verify)` marks: mark at the dependency; a table caption may cover a grouped shelf (`R03:206`, P2-6).
4. No “full bank” overclaim; if inline flags stay inline, say so (`R03:205`, P2-4).
5. No flat contradiction on “the map is the territory”; use §8.6's reconciliation once (`R03:200`, P2-1).
6. No flat “Marshallese stick chart is not a map” verdict; use “not a positional map under this entry's stipulative test” (`R03:209`, P2-5).
7. No “minimum build per form” table that covers 5 of 8; all eight rows (`R03:196`, B9).
8. No false correction of a correct quote: `naming-systems.md:70` really does say “a map is an archive of coups” (`R03:190`, B3).
9. No head block above **27** lines: the r47 head was 51 (`Q01-final-gate.md:87`).
10. No reflowed `- topic:`: it is one physical line and the README row is generated from `topic_of()`, not retyped.

### 3.3 Assembly rule — audit the final bytes, not the fragments

r47's audit chain was pinned to superseded fragments and one fragment falsely “corrected” another (`R03:190`, `:233-249`; `Q01-final-gate.md:118`). Therefore:

1. One assembler (the integrator or a designated scribe) concatenates the header + body into **one fence** at `.scratch/r48-c/entry.md`.
2. Compute `wc -l`, `sha256sum`, and a section/field parse **before** any verifier starts.
3. Every verifier (C03–C09, C12, C14–C18, E01/E02, M03) receives **that path and digest**; a verdict on a fragment is void.
4. If any fix changes the bytes, the assembler re-issues a new digest and the affected verifiers re-run. No “fix applied, audits unchanged”.

### 3.4 Gate sequence

| gate | owner seat(s) | command / evidence | pass condition |
|---|---|---|---|
| **G0 freshness + collision** | C06 | `test -e` slug; `find … -iname`; `grep -rniE '^- topic:.*(cartograph\|mapmak\|portolan\|cadastr)'`; A02 ownership cross-check | slug absent; 0 strict owners; broad hits dispositioned; land as **A**, not M |
| **G1 assembly + length** | assembler, C05 | `wc -l .scratch/r48-c/entry.md`; header-field parse; 1 H1 | 225–240, hard ≤250; H1 + eight header fields; no truncation |
| **G2 arithmetic** | C03 | every number → formula/result table; recompute B1 as 10 m and 20× | zero unchecked numbers; zero wrong arithmetic |
| **G3 citation anchors** | C04 | for every `path:line`: `sed -n 'Np'`/`grep -n` output pasted; every quote verbatim | every anchor resolves to the described content; no B3/B4-style miscite |
| **G4 worked example** | C14, C05 | one rule, stated once; decision ids present; NON-CANON declared | no incompatible restatement; example instantiates the method |
| **G5 boundary** | C07, E01, C15 | **13 rows** (12 neighbours + divination non-collision; the K02 seven are the core); `cosmology:27` sentence | each neighbour “owns / does not restate”; no second owner; no over-claim |
| **G6 shelf/provenance** | C08, C18 | every external item “not consulted”/`(to-verify)`; in-corpus shelf resolves; no fabricated work | no unread work presented as inspected |
| **G7 couples** | C09 | resolver over the final `- couples:` line; every `.md` token resolves at HEAD | 0 dangling tokens; delta recorded |
| **G8 README + staged sweep** | C10, C11 | exact README hunks (`§3.6`); C11's staged-tree recipe (`cp -a` the lane, 136-line fixture already green, `C11-sweep.md` §1–3) re-run on **C01's real topic**; `sweep.py` | `rows 224 files 224`; 0 missing/topic mismatch/orphan; totals 224; footer `25/26/26/29/24/94`; vector sum 224; exit 0 |
| **G9 apply** | W01, N03 | exactly two corpus paths: new entry + modified README; `git status --porcelain corpus/` | one `A` + one `M`; zero other corpus lines |
| **G10 post-landing** | V01, F01, A02, D01 | live recount, live sweep, ownership re-check, README sha | 224 / 26 / ≤250 / H1 1 (with Ca) / sweep green; no second owner |

**Absolute:** the claim's counting command `python3 reports/round-48/run-validation.py` is **not a seat command**. The shared rules forbid running any `reports/round-*/run-validation.py` in-tree; validation is the integrator/fleet step. Seats use the direct commands above.

### 3.5 Exact defect guards (R03 B1–B9 → the check that prevents recurrence)

| defect | required guard in the r48 draft |
|---|---|
| **B1** arithmetic 200 m vs 10 m | state “20×”, or change the closure to 100 m; C03 recomputes `0.2 × 50,000 = 10 m` |
| **B2** unreproducible `cartograph` count | gap statement says exactly **2 files / 2 lines**, names `cosmography:102` and `mesoamerica-primary-sources:58`, and does **not** count `:71` as a `cartograph` hit; use `grep -rni`, never `grep -rli`, for a line count |
| **B3** false accusation | never “correct” a quote without `grep -n` proof; keep `naming-systems.md:70` verbatim; C04 checks the quote |
| **B4** wrong ladder anchor | cite `craft-artisan-lexicon.md:54-65` for the apprentice→journeyman→master ladder; `:44` only for material grading |
| **B5** wrong cross-references | the form typology is **§5** in the K01 skeleton (r47's §4.1); never r47's “§1–3” or “§2” |
| **B6** handoff section | provenance/legal is **§7** in the K01 skeleton; the handoff must cite the section that actually exists (r47's §8 was correct only for r47's 15-section skeleton) |
| **B7** three update rules | one rule only; the worked example names the `DR-CT` rows it instantiates (the right-sized entry keeps four) |
| **B8** “owns no made map” | add: cosmography owns the world-drawn content (`cosmology-cosmography.md:27`, `:71`, `:102`); this entry owns the surveyed/projected/reproduced sheet |
| **B9** 5-of-8 per form | **all eight forms** in K01 §5; a “five common forms” retitle is not acceptable in the right-sized draft |

### 3.6 README rev 2.5 hunks (exact)

Apply to `corpus/README.md` at `a01405d` (sha `7c788a1d…`). Line numbers below are HEAD coordinates. After Ca's H1 removal **every line after the deleted pair shifts by −2** (K02's measured mapping: section header `:234→:232`, calendar/costume rows `:240-241→:238-239`, totals `:544→:542`, footer `:548→:546`); after the rev-2.5 insert they shift again. Use the staged final file (§5), never blind offsets.

1. **Insert rev 2.5 block after the first H1 + blank line** (before `revision: 2.4` at `:5`). Final text:

   ```text
   revision: 2.5 — Round-48 culture-material expansion (2026-10-19): one
   culture-material entry landed (`cartography-and-mapmaking.md`, the r44 K02 gap
   and the r48 right-sized redraft), audited against R03's B1–B9 and the partition
   length band (receipts under `reports/round-48/`); `## culture-material/` moved
   25 → **26**; the totals and footer moved
   223 → **224** and the vector 25/26/25/29/24/94 → **25/26/26/29/24/94**. Re-measured
   with `python3 reports/round-28/readme/sweep.py`: 224 rows vs 224 files, exit 0.
   Non-canon examples and passing structural gates do not certify historical truth.
   ```

   Apply only after G1–G8 pass; the block's audit sentence must be true of the filed receipts.

2. **Repair the rev-2.4 vector** at `:11`. Replace:

   ```text
   the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
   ```

   with:

   ```text
   the vector 25/23/25/29/24/94 → **25/26/25/29/24/94** (the after-vector first
   printed here read 25/23/26/25/24/94, sum 217; corrected in rev 2.5 to the measured
   25/26/25/29/24/94, sum 223). Re-measured with
   ```

   This repairs forward and preserves the defect record; it does not delete rev-2.4.

3. **Section header** `:234`: `## culture-material/ (25)` → `## culture-material/ (26)`.

4. **Row insertion** between the calendar row (`:240`) and costume row (`:241`):

   ```text
   - `cartography-and-mapmaking.md` — <the entry's parsed `- topic:` text, byte-equal>
   ```

   The row is filename-only (no path), and the topic must equal `sweep.py`'s `topic_of()` output exactly.

5. **Totals line** `:544`: `Total knowledge entries: 223.` → `Total knowledge entries: 224.`

6. **Present-tense footer** `:548`: `(total 223 files; directory totals 25/26/25/29/24/94)` → `(total 224 files; directory totals 25/26/26/29/24/94)`. Do **not** edit the superseded-reading paragraph below it; it is a dated record.

### 3.7 Stop rules for C

- Entry >250 lines after one trim pass → **do not land**; return to the assembler. Do not “record an exception”.
- Any G2/G3/G4 failure → do not land; the r47 lesson is that a real topic is not a landing licence.
- Sweep not `224 == 224` or footer vector not `25/26/26/29/24/94` → do not land.
- A second owner appears at landing HEAD → report the collision; do not route around it.
- Only one claim can be recorded improved if only one lands: C and Ca are independent. Do not use Ca's success to colour C.

---

## 4. Claim Ca — README duplicate H1 + over-build disposition

### 4.1 Exact H1 fix

At HEAD (`corpus/README.md:1-4`):

```text
1  # kotodama-shokunin corpus index
2
3  # kotodama-shokunin corpus index
4
```

Target **after the combined C+Ca staging** (§5):

```text
1  # kotodama-shokunin corpus index
2
3  revision: 2.5 — ...
```

Ca applied alone leaves `revision: 2.4` as the first block at line 3; the H1 count is 1 either way. The edit removes the duplicate H1 at `:3` **and its following blank line `:4`**, leaving exactly one blank line between the title and the first revision block. Do not remove `:1`; do not touch any `##` heading; do not touch the `revision: 2.0` duplicate prose at `:42/:44` (out of scope and part of the dated history).

**Separate live defect, disposition only — do not absorb it.** N01 measured a second duplicate-line defect: `corpus/README.md:42` and `:44` both read `revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten`, and `:42` is an orphan header with no body (`N01-numbers.md` §4.1). It is the same stale-duplicate class as the H1 but **not** this claim's object. File it in the r48 successor as an `observations[]` entry (`id: r36-readme-revision-duplicate`, owner integrator, next_touch next README touch, evidence `corpus/README.md:42,44`); do not fold it into the Ca diff, or the Ca edit stops being surgical.

Verification (post-apply; the control is written by the integrator):

```text
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md   # 2 -> 1
$ grep -c '^# ' corpus/README.md                                  # 2 -> 1
$ python3 tools/check-readme-heading.py                      # exit 0, one H1
```

### 4.2 Heading-count control — a new tool, not a sweep edit

`reports/round-28/readme/sweep.py` is **filed bytes** (`reports/round-1..47/**` is immutable) and its docstring lists only index/footer/block legs (`:18-26`); `grep -n 'heading' reports/round-28/readme/sweep.py` returns no match. Adding a heading leg there would violate the shared rules. Therefore:

- New file: `tools/check-readme-heading.py` — Ca05's measured draft (`reports/round-48/calib/Ca05-heading-control.md` §3, 244 lines, stdlib only). It measures **8/8** on `--selftest`, exits **1** on the live README (`H1-COUNT lines=[1,3]`), and exits **0** on the staged copy with lines 3–4 removed (`h1_lines [1]`).
- Behavior: default `corpus/README.md`; `--readme <path>`; `--json`; count ATX headings outside fenced code; require exactly **1** H1; require the H1 to be the first non-blank line; report duplicate same-level headings; exit 0 clean / 1 finding / 2 could-not-evaluate.
- The integrator adds a validation call (or a named durable note if wiring is deferred); either way the control must be runnable post-landing and its output filed. Owner: integrator; next touch: the round-48 validation leg.

### 4.3 Over-build queue successor

New artifact: `reports/round-48/calib/queue-successor-r48.json` (delta, not an edit). Pin:

- parent: `reports/round-47/calib/queue-successor-r47.json`, sha256 `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58`, 3 rows + 2 amendments, unchanged;
- root parent: `reports/round-40/op/defect-queue-v2.json`, sha256 `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`, unchanged;
- predecessor: `reports/round-43/calib/defect-queue-v2-successor-r43.json`, sha256 `77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38`, unchanged.

Required row (one row covering R03 B1–B9; findings may be grouped as arithmetic/count, citations/anchors, example/ownership, completeness):

| field | required content |
|---|---|
| `id` | `r47-overbuild-stale-audit-bytes` |
| `origin` | `reports/round-47/review/R03-c-content.md:188-196` (B1–B9) + `:92-96` (volume) + `reports/round-47/cross/Q01-final-gate.md:16,87,106,289` + `reports/round-47/claims.json` claim C |
| `class` | `routed-with-owner` (`v2_class_equivalent: carried-with-owner`); **not** fixed at authoring time |
| `owner` | r48 C drafters (right-sized redraft) + integrator (landing); process leg: integrator/tools-harness maintainer |
| `reason` | Measured 790 lines (51 head + 739 body) vs partition min/median/max **103/149/221**; 3.6× max, 5.3× median. Nine blocking defects B1–B9; B3 is a false accusation that would have corrupted `naming-systems.md:70`; B2's `cartograph` count is unreproducible. The audit chain was pinned to superseded fragments (`Q01-final-gate.md:118`). The freshness gate now guards **topic ownership**, not **entry quality**. |
| `next_touch` | Close the volume leg only when the r48 entry lands at ≤250 with G2–G4 passing on the final bytes; then the integrator files a **new closing row** with `wc -l`, sha256, arithmetic/citation outputs, and the sweep receipt. Process leg: add a pre-apply draft-quality check (length + arithmetic + anchor resolution) in the next runner/gate round; owner integrator. |
| `evidence` | `R03-c-content.md:188-196`; `:26` (739 body lines); `:96`; `Q01-final-gate.md:87` (790 = 51 + 739), `:106`, `:289`; `R01-review.md:90-92`; `R02-review.md:121-123`; `corpus/knowledge/culture-material/*.md` line census |
| `verification` | Run `wc -l` over the 25 partition files and sort numerically → min 103 / median 149 / max 221; `0.2 mm × 50,000 = 10 m`; `200 m ÷ 10 m = 20`; the R03 B1–B9 re-reads |
| `application_gates` | G1 parent bytes unchanged; G2 every cited line re-read and real; G3 no `fixed-with-evidence` before the post-landing output; G4 new artifact only, never an edit to r47/r43/r40 files |

If the row author cannot reproduce a cited number, mark that finding `to-verify` with owner + reason — never infer.

**Also file the N01 observation in the same successor** (observation, not a defect row):

```json
{"id":"r36-readme-revision-duplicate","class":"recorded",
 "owner":"integrator-of-record (README index)",
 "finding":"corpus/README.md:42 and :44 both read the revision 2.0 header; :42 is an orphan with no body",
 "evidence":"reports/round-48/cross/N01-numbers.md §4.1; corpus/README.md:42,44",
 "next_touch":"next README touch: remove the orphan header or record it as dated history"}
```

The r47 successor is a delta of 3 rows + 2 amendments; adding one row and one observation does not disturb it.

### 4.4 Stop rules for Ca

- H1 count is not exactly 1 after the edit → **do not apply**; rebuild the final README.
- Sweep not green after the edit → do not apply; the H1 removal itself cannot break the index, so a red sweep means a staging bug.
- Any revision-history line other than the duplicate H1 and its blank is removed → do not apply.
- The queue row marks the class fixed before the C landing evidence exists → do not apply.
- Do not edit `reports/round-47/calib/queue-successor-r47.json`; only a new r48 artifact.

---

## 5. Cross-claim ordering — one README, two attributable diffs

C and Ca both modify `corpus/README.md`. If applied as independent patches against HEAD, Ca's line-3 deletion and C's rev-2.5 insertion collide.

**Staging sequence (all in `.scratch`, no corpus write by seats):**

1. Copy HEAD README to `.scratch/r48-readme/00-head.md`.
2. Apply **Ca only** → `.scratch/r48-readme/10-h1-fixed.md`; produce the Ca diff (`00` → `10`). Expected: exactly the duplicate H1 + one blank line removed.
3. Apply **C only** to `10` → `.scratch/r48-readme/20-final.md`; produce the C diff (`10` → `20`). Expected: rev 2.5 block, rev-2.4 vector repair, section header, new row, totals, footer.
4. Run the staged sweep against `20-final.md` + a `.scratch` knowledge tree containing the new entry. Expected: 224/224, footer `25/26/26/29/24/94`, exit 0.
5. Pin `sha256sum 20-final.md`, both diff files, the entry sha, and the sweep receipt.
6. Integrator writes the new entry and **writes `20-final.md` to `corpus/README.md` in one write** (not two sequential patches). Then run the live sweep and heading control.

If Ca fails but C passes, apply C's hunks to HEAD (the H1 stays 2; the sweep does not check it) and record Ca as not improved. If C fails but Ca passes, apply Ca alone and record C as not improved / could-not-evaluate. Never present a partial apply as a completed claim.

**Attribution rule:** the Ca receipt points at the `00 → 10` diff; the C receipt points at `10 → 20` diff. The final README's sha is shared evidence and must be identical in both receipts.

---

## 6. Evidence ledger at close

| claim | required filed evidence | exact close values |
|---|---|---|
| **C** | K01 spec; C01/C02 final fence; assembler digest; C03 arithmetic; C04 anchors; C05 length/contract; C06 collision; C07 boundary; C08 shelf; C09 couples; C10 README; C11 staged sweep; C12 content; C14 example; C15 neighbours; C16 topic; C17 structure; C18 provenance; E01/E02; M01/M02/M03; W01 landing wire; V01 post-landing; N03 safety; A02 ownership; F01 census; D01 delta | total **224**; culture-material **26**; entry **≤250** (target 225–240); README rev **2.5**; vector **25/26/26/29/24/94** = **224**; sweep **224 rows / 224 files**, exit **0**; one `A` + one `M` only |
| **Ca** | K02 defect scout; Ca01 H1 fix; Ca02 successor row; Ca03 H1 verify; Ca04 row verify; Ca05 heading control; Ca06 process row; Ca07 integrity; N02 integrity; W02 landing; R04/X05 reviews | H1 count **2 → 1**; heading control exit **0**; sweep exit **0**; queue row present with class/owner/next_touch/evidence; r47/r43/r40 parent sha **unchanged** |

A claim is not “improved” because its artifacts exist. C is improved only when the entry and README are applied and the live sweep passes; Ca is improved only when the H1 count is 1 and the control runs. Missing evidence → `could-not-evaluate`, named owner and reason.

---

## 7. Prohibited actions and provenance

- Seats write only their declared out path under `reports/round-48/`; no `corpus/` or `tools/` staging.
- No edits to `reports/round-1..47/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`; the r28 sweep is read-only and immutable.
- No `reports/round-*/run-validation.py` in-tree; no re-freeze of `declared-in-r7`; no packet-surface changes.
- No git commits/pushes, installs, or network.
- Unknowns stay `to-verify` with owner + reason.

Commands this seat actually ran: `git rev-parse HEAD`, `git status --porcelain`, `find corpus/knowledge -name '*.md' | wc -l`, `ls corpus/knowledge/culture-material/*.md | wc -l`, the slug/filename/topic greps, `grep -rni 'cartograph'`, `grep -c '^# '`, `grep -n` on README anchors, the Python vector/median arithmetic, `sha256sum` on README/claims-freshness/queue artifacts, the JSON parse of `queue-successor-r47.json`, `wc -l corpus/knowledge/culture-material/*.md`, and `git ls-files --error-unmatch` on the r47 successor. No corpus byte, tool byte, or filed round was modified; this file is the only write.
