# ReviewSec04 — falsify seat, kotodama round 50 attempt 1

Item attacked: **§4 "Species and ecology decision table"** of
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` as landed in
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`),
plus the in-corpus `path:line` anchors and the S-id → `corpus/SOURCES.md` row-scope
mapping the §4 table (and, for completeness, every anchor and every S-id in the entry).

Lane: kotodama-shokunin, branch `main`. Read-only attack seat; no lane file edited, no
jj/git mutation in the lane, no delegation.

## Verdict

**PARTIAL.** §4's *structure* and every *in-corpus* anchor in the entry hold; the S-id
citations are real rows with the right scope; but §4 carries **one calibration mis-code
that contradicts the entry's own §13** (Botai, F1) and **one systematic provenance gap**
(≈20 factual cells with neither citation nor `(to-verify)`, F2), plus **one registry-anchor
gap** (S050's registered anchor does not cover the two paragraphs §4 leans on, F3).
Nothing found is a fabrication; the defects are calibration/status and provenance
labelling, which is exactly what QUALITY criteria 1–2 police.

## Method (all commands reproducible)

* Landed bytes read from a private clone, never the lane working tree:
  `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/kr50sec04 && git -C /tmp/kr50sec04 checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`
  (base clone `/tmp/kr50sec04-base` at `4ad2683` for the "before" numbers). Both deleted at
  the end of the seat. `GIT_CEILING_DIRECTORIES=/tmp` respected.
* Corpus diff over the landed commit is confined to `corpus/QUALITY.md`, `corpus/README.md`,
  `corpus/SOURCES.md`, the new entry and `corpus/lessons/round-50.md` — so every in-corpus
  `path:line` anchor read at the landed commit is byte-identical to base. Verified by
  `git diff --stat 4ad2683 1c779e4a -- corpus/ reports/ tools/`.
* Anchor resolution: every `file.md:NN` occurrence in the entry (**87 distinct
  (file,line) targets in 68 citation groups**, including the head's `:137-146`,
  `:170-172`, `:35-39` ranges) was extracted and the target line printed **at the landed
  commit**. Every one resolves inside `corpus/knowledge/**` (or `reports/`) and every one
  supports the sentence that cites it (details below).
* S-id audit: all 22 S-ids cited in the entry (`S048`–`S069`) resolve to rows in
  `corpus/SOURCES.md`; every row is `status=mined`, `opened=2026-10-21`, `recheck=365d`,
  `used-by=corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.
* Gate quotes cross-read against `corpus/lessons/round-50.md:33-54` and against the round-50
  source seats under `.ufo/waves/round-50/build/` (in-lane evidence; **no URL was re-opened**,
  per the seat's "do not re-open URLs" bound).
* Head numbers reproduced at base and at the landed commit (below).

## What HOLDS (verified, with evidence)

1. **Every in-corpus anchor in the entry resolves and supports its sentence.** 87 distinct
   (file,line) targets, all read at `1c779e4a`. Spot-verbatims:
   * `civilizations/finnic-sami.md:140` = "Do not map herding status directly onto Sámi
     identity." → supports §4 Reindeer calibration cell (entry:64) and §13 (entry:165). ✔
   * `civilizations/finnic-sami.md:150` = "Large-scale pastoralism has a history; it is not
     the eternal condition of all Sámi communities" → supports entry:118. ✔
   * `civilizations/inca.md:128` = "'all wool, all alpaca' is too simple" → supports §4 Llama
     calibration cell (entry:65) exactly. ✔
   * `culture-material/hunting-foraging-subsistence.md:36` = "not planted, herded or owned as
     a standing crop" → supports the §1 "Fails as (owner)" cell (entry:20). ✔
   * `culture-material/agrarian-field-system-lexicon.md:62` = the `agropastoral` row → supports
     entry:21, :31, :50 (herd calendar collides with the ploughing peak). ✔
   * `linguistics/semantic-fields-lexicon-building.md:70` = "Pastoral wealth vocabulary
     (herd-age, herd-color, herd-condition terms) indexes property systems" → supports the
     §2/§5 use (entry:37, :71). ✔
   * `verification/calibration-registry.md:35-39` = the R/C/B/H/T code table → the entry's
     §13 code legend (entry:175) is exact. ✔
   * `reports/round-44/scout/K02-gap-scout.md:73` = "| Pastoralism / husbandry | 0 | 0 |
     **named** r35 CM-2 | **carried — reject** |" → supports the head's "carried as a rejected
     candidate" sentence (entry:4). ✔
2. **Every S-id in the entry resolves to a row whose scope/anchor supports the citing
   sentence.** Row-by-row check of the 22 rows' `scope`/`anchor`/`teaches` cells against the
   entry's sentences — no row is cited for anything outside its registered scope. Verified
   examples: S052 ("not a pastoral universal" → entry:59 "is regional, not a law"); S057
   (publisher description only, tier B → entry:53, entry:187); S051 (tier B, "not primary for
   Sherratt" → entry:93, :183); S066 ("few societies are near-totally dependent" → entry:25);
   S069 ("horizontal (plain or plateau) and vertical (mountain)" → entry:49).
3. **§4's S061 quote is verbatim from the Gate record.** Entry:63 quotes
   `"on pastures at high elevations"`; `corpus/lessons/round-50.md:46` records the source's
   sentence "During the warm season of summer and autumn, yak are on pastures at high
   elevations and the herdsmen live in campsites" (ch. 8 Overview ¶1). Verbatim fragment. ✔
4. **§4's S068 claim matches its row.** Row `SOURCES.md:97` teaches "camelids are the only
   domesticated ungulates of the Americas; the Andes sustained the only pre-Hispanic pastoral
   societies" → entry:65. ✔
5. **§4's S050 claims match the source seat's per-species record.** The round-50 source seat
   records (`.ufo/waves/round-50/build/SrcZederDomestication.md`, §4 "Per-species and
   per-region detail the entry can actually use"): "*Cattle*: taurine cattle initially
   domesticated in the upper Euphrates valley **ca. 11,000–10,000 B.P.** (paragraph 6)" and
   "*Sheep and goats*: … The *order* is regional and reverses: goats first in the Zagros (Ganj
   Dareh), but **sheep are the initial focus in southeastern Anatolia**". Entry:59 and :60
   state exactly this. (But see F3 on the *registered anchor*, and F1's neighbour problem
   below.)
6. **Entry contract holds.** 8 head fields in order (`- topic:` … `- scope:`, entry:3-12),
   exactly **one** `- topic:` line, **1** H1, **15** H2, **0** H3, decision tables present
   (§3, §4, §5, §6, §7, §8, §9, §10, §11, §13), calibration codes defined by reference to
   `calibration-registry.md:35-39`, lore handoff in §15 (entry:199), §12 explicitly NON-CANON
   (entry:169). No canon decision is taken in §4 or anywhere in the entry.
7. **The head's "before" numbers reproduce at base.** At `4ad2683`:
   `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l` → **0**;
   `grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l` → **0**;
   the unbounded form hits only `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`
   ("sherd"), exactly as the entry records (entry:4); `find corpus/knowledge -name '*.md' | wc -l` → **225**;
   `ls corpus/knowledge/culture-material/*.md | wc -l` → **27**.
8. **The head's "after" numbers reproduce at the landed commit.** `python3 -B
   reports/round-28/readme/sweep.py` → `rows 226 files 226`, `topic_mismatch 0`,
   `missing_from_index 0`, `orphan_rows 0`, `footer_ok True`, exit 0; culture-material = 28.
   README row sits in filename order between `music-instrument-lexicon.md` and
   `ritual-garments.md` (`corpus/README.md:297`), totals line 225 → 226
   (`corpus/README.md:590`), footer vector `25/26/28/29/24/94` (`corpus/README.md:594`).

## Findings

### F1 — Medium — §4 mis-codes a refuted claim as **C** (contested); the entry's own §13 says R

* `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:62` (§4 Horse row,
  Calibration cell): "modern domestic horses do not descend from the Botai lineage (S067):
  **C** on Botai-as-origin".
* `corpus/SOURCES.md:96` (row S067, tier A, scope "origins of modern domestic horses (DOM2)
  … as stated in the abstract", teaches "modern domestic horses **do not** descend from the
  Botai lineage") and `corpus/lessons/round-50.md:52` (Abstract quote: "modern domesticated
  breeds do not descend from the earliest domestic horse lineage …").
* `corpus/knowledge/verification/calibration-registry.md:36` — **C** = "Contested empirical or
  historical interpretation | Preserve alternatives, scope, and discriminating evidence; do not
  report one reading as settled". The registry's C means *do not report one reading as
  settled*; here the source settles it and the entry reports it as settled while labelling the
  claim contested — the code is inverted relative to its definition, and the code's direction
  (preserve alternatives) contradicts the source.
* **The entry contradicts itself**: `…pastoralism-animal-husbandry.md:185` (§13 bank) reads
  "Botai horses are the ancestors of domestic horses | **C → R for modern horses** — S067".
  So §4 says C and §13 says R (for modern horses).
* **Provenance of the stale code**: the author seat's draft (§4) calibrated the horse row
  "CONTESTED — Botai husbandry and DOM2 origin debated; [I] argues one side", where `[I]` was
  Outram 2023 (*Frontiers in Environmental Archaeology*, the side arguing Botai-first) —
  `.ufo/waves/round-50/build/ScribeSec04Species.md`. Outram was **never registered** as an
  S-row; the integrator swapped the source to S067 (Librado 2021, the opposite side) and the
  **C code survived the swap**. A calibration flag cannot be carried across a source swap.
* **Smallest fix**: in §4's Horse calibration cell write "**R** for modern horses (S067);
  early horse *use* is a separate question" — matching §13's own wording. One cell.

### F2 — Medium — §4's Ecology / Products / Mobility columns assert species facts with neither a citation nor `(to-verify)`

QUALITY criterion 1 (`corpus/QUALITY.md:5-8`): "every factual claim carries a cited,
checkable source … A claim the author cannot verify is marked `(to-verify)` inline — never
laundered into assertion." In §4 (entry:55-67) the uncited factual cells are:

| entry line | species | uncited cell content |
|---|---|---|
| :59 | Cattle | Ecology "grass and reliable water"; Products "milk, meat, hide, **blood**, traction"; Mobility "follows water and grass; **age-grade** herd labour" |
| :60 | Sheep/goat | Ecology "**arid-tolerant** small stock"; Products "meat, milk, wool, hair, dung"; Mobility "short to long moves; **fast herd rebuilding**" |
| :61 | Camel | Ecology "**hot and cold deserts**"; Products "milk, meat, hair, carrying"; Mobility "caravan and long-range moves" |
| :62 | Horse | Ecology "steppe grassland"; Products "**milk (summer)**, riding, traction"; Mobility "riding multiplies herd range" |
| :63 | Yak | Ecology "high plateau"; Products "…, **fibre, pack**" (beyond S061's registered teaches, which record only butter + dung fuel) |
| :64 | Reindeer | Ecology "**taiga and tundra lichen pasture**"; Products "meat, hide, transport"; Mobility "migration with the herd" |
| :65 | Llama/alpaca | Ecology "**Andean puna**"; Products "fibre, pack, meat" |

These are load-bearing, not decorative: entry:67 makes the ecology cell decisive ("Fix ecology
→ species → …; a herd with no forage line fails §11 step 1") and §11 step 1 (entry:151) is
built on it.

**Why this is a real defect and not a stylistic quibble** — the round-50 author seat *did*
have sources for most of these cells; they were dropped at S-row registration without the
entry's facts being downgraded to `(to-verify)`:
* `ScribeSec04Species.md` source list: `[F]` Fitak et al. 2020 ("each species possesses a
  variety of adaptations to harsh desert conditions" → camel "hot and cold deserts");
  `[D]` FAO Pastoralist Knowledge Hub Latin America (Andean puna/altiplano → "Andean puna");
  `[J]` Johnsen et al. 2017 (`Reindeer husbandry in Sápmi`: "decline of ground lichen forests",
  "shortened duration of snow cover") → the reindeer ecology cell; `[H]` Zeder 2008 for the
  sheep/goat culling profile → "fast herd rebuilding"; `[I]` Outram 2023 ("Horse milking is
  principally a summer occupation") → "milk (summer)".
* **None of `[A]`, `[B]`, `[C]`, `[D]`, `[E]`, `[F]`, `[G]`, `[I]`, `[J]`, `[K]`, `[L]`, `[M]`,
  `[N]` became an S-row.** `corpus/SOURCES.md` gained only S048–S069
  (verified: `grep -cE '^\| S0(4[89]|5[0-9]|6[0-9]) \|' corpus/SOURCES.md` → 22 rows, none of
  them the draft's list). So the facts travelled into §4 and the citations did not — the exact
  "laundering into assertion" that QUALITY 1 forbids. Note the two places where the
  integrator *did* downgrade the same class of claim — camel domestication dates
  `(to-verify)` (entry:61) and horse snow-grazing `(to-verify)` (entry:62) — which shows the
  intended treatment and makes the unmarked cells inconsistent with it.
* **Smallest fix**: either register the missing sources as S-rows and cite them in the cells
  (the author seat already produced paste-ready candidate rows for most of them), or mark the
  remaining factual fragments `(to-verify)` inline, exactly as the camel and horse cells do.

### F3 — Medium — S050's registered `anchor` does not cover the two paragraphs §4 leans on

* `corpus/SOURCES.md:79` (row S050), `anchor` cell: "Abstract; §Initial Animal Domestication in
  the Fertile Crescent, **paragraph 3 and penultimate paragraph**"; `teaches` cell: "herd
  management (culling young males, keeping females) is legible before morphological change;
  **four species under management c. 11,000–10,000 BP**; species order is regional".
* §4 uses S050 twice for detail that the seat's own per-species record places in **paragraph 5**
  (sheep/goat order: "goats first in the Zagros … sheep are the initial focus in southeastern
  Anatolia") and **paragraph 6** ("taurine cattle initially domesticated in the upper Euphrates
  valley ca. 11,000–10,000 B.P."):
  — `.ufo/waves/round-50/build/SrcZederDomestication.md`, §4 "Per-species and per-region
  detail the entry can actually use (paraphrase, located)".
* Neither ¶5 nor ¶6 is inside the row's registered anchor, and the registered `teaches` cell
  carries the *regionality* of the species order but not the *Zagros / SE Anatolia* attribution
  nor the *upper-Euphrates* site. Under the SOURCES contract the `anchor` cell is what makes a
  citation checkable; entry:59 and :60 therefore cite a row whose locator set does not reach
  the sentences being supported.
* **Smallest fix**: extend S050's `anchor` cell to "Abstract; §Initial Animal Domestication in
  the Fertile Crescent, ¶3, ¶5, ¶6 and penultimate paragraph" (the paragraphs are already
  identified in the seat record; no URL work needed), or cite the paragraph in the entry's
  cells. Note this is a `corpus/SOURCES.md` edit, which is C's land — fine, C owns it.

### F4 — Low/Medium — S063: the entry's "camel husbandry as a named skill" is thinner in the Gate record than in the row's `teaches`

* Entry:61 (Camel row, Mobility cell): `"camel husbandry" as a named skill (S063)`.
* `corpus/SOURCES.md:92` teaches "traditional pastoral culture and skills including camel
  husbandry" — but the **Gate quote** registered in `corpus/lessons/round-50.md:48` is only
  "The Bedu communities inhabiting this area keep alive a traditional pastoral culture and
  related skills." The phrase "camel husbandry" comes from the seat's wider located reading of
  the same paragraph ("traditional medicine, camel husbandry, tent-making craftsmanship, and
  tracking and climbing skills") —
  `.ufo/waves/round-50/build/SrcBedouin.md`, "Quotes and location".
* Not an error, but the row's `teaches` cell asserts more than the Gate bullet the lesson
  preserves, and the entry's cell depends on that assertion.
* **Smallest fix**: extend the S063 Gate bullet in `corpus/lessons/round-50.md:48` with the
  skill-bundle substring (it is already located in the seat record), or reword entry:61 to
  "a named pastoral skill (S063)".

### F5 — Low/Medium — S060's `teaches` claims emic-ness its registered quote does not carry; entry:67 leans on "emic"

* Entry:67: "The Mongolian 'five snouts' — horses, yaks/cattle, camel, goats and sheep — is an
  **emic portfolio term** (S060)"; entry:78 repeats it.
* `corpus/SOURCES.md:89` teaches "the five snouts as an emic portfolio term", but its registered
  anchor is "§2 Bayankhongor province ¶2 (PDF p. 4); Abstract; §1", and the seat's recorded
  quote for that location is a **herd-count** sentence: "In Bayankhongor, the total herd count
  for 2012 was 2,640,831 head of livestock, which is an aggregate of the 'five snouts' represented
  by horses, yaks/cattle, camel, goats and sheep" —
  `.ufo/waves/round-50/build/SrcMongolFiveSnouts.md` (proposed row S048 there).
* The seat's own record notes that the *emic* attestation came from a **different** source
  (Chuluunbaatar 2012, "all together they are – and still are – called the 'five snouts'
  (tavan xošū mal)", an Austrian Academy chapter) that was **never registered** as an S-row.
* **Smallest fix**: the S060 seat should confirm that Ahearn's §1/Abstract itself frames
  "five snouts" as a Mongolian emic term; if it does not, either register the Chuluunbaatar
  row or reword entry:67/:78 to "the five-snouts aggregate (S060)" and drop "emic".

### F6 — Low — §4/§5 drop S059's own scope limit ("the Swedish earmark institution … not Norwegian law")

* `corpus/SOURCES.md:88` scope: "the Swedish earmark institution as stated by the agency that
  keeps the register; **not Norwegian law, not a court holding**".
* Entry:64 (§4 Reindeer row) "earmark institutions (S059)"; entry:77 "a **Sámi** earmark is a
  combination of cuts in both ears and names the owner (S059)"; entry:116 "a **Sámi** earmark is
  personal, usually inherited … (S059) | B — one legal system".
* Entry:116 does scope it as "B — one legal system" ✔, but entry:64 and :77 say "Sámi"
  unqualified where the row is specifically the *Swedish* Sámi Parliament's register.
* **Smallest fix**: "Swedish Sámi earmark" in entry:77 (and "Swedish earmark institutions" in
  entry:64). One word each.

### F7 — Low (outside §4, adjacent) — §13's living-practice sentence cites the Maasai to rows that are not Maasai

* Entry:189: "Mongolian, Sámi, **Maasai**, Bedu, WoDaaBe and Tibetan herding are living practice
  **(S058, S059, S063)**". S058 = WoDaaBe, S059 = Swedish Sámi, S063 = Bedu. **No Maasai source
  is cited**, and the Maasai material in the round-50 draft came from unregistered `[L]` Quinlan
  2016 (Simanjiro) and `[M]` McCabe 2010 (Loliondo) — `ScribeSec04Species.md`.
* **Smallest fix**: register one Maasai source row (the two candidates already exist in the
  seat record) or drop "Maasai" from that sentence's citation set.

### F8 — Low (outside §4, adjacent) — §6 attributes the review's wording to Sherratt

* Entry:93: "Sherratt's 'secondary products revolution' — "a more diversified exploitation of
  secondary applications and products such as milk, wool, textiles, and traction" (S051)".
* `corpus/SOURCES.md:80` (S051): scope "what Sherratt's secondary-products thesis claims and this
  review's three-region critique …; **not primary for Sherratt**"; anchor "Abstract;
  Introduction ¶1–2; …"; the Gate bullet `corpus/lessons/round-50.md:36` records the quote as
  the **Abstract's opening sentence** of Marciniak 2011.
* The quoted words are Marciniak's rendering, not Sherratt's text; the entry presents them as
  Sherratt's phrase. The sentence's own calibration (**C**) is right; the attribution is not.
* **Smallest fix**: "as summarised by Marciniak 2011 (S051): '…'".

### F9 — Low (outside §4, adjacent) — two general register claims lean on narrow rows without their scope limits

* Entry:21 (§1 table) "Mobility tracks forage | movement is the production logic, timed to
  vegetation and season (S058)". `corpus/SOURCES.md:87` scope: "the WoDaaBe seasonal movement
  system in southeastern Niger as observed 1996–97, **cattle only**; not Fulani at large, not
  current practice". A register-general property is stated from a single-people, single-species,
  dated source without the limit. (§11 step 3, entry:153, does scope it: "S058 for a named-move
  system" ✔.)
* Entry:47 (§3 Nomadic row) "species mix and movement are the hedge (S060)". S060's registered
  `teaches` are "the five snouts as an emic portfolio term; reliability-seeking risk management;
  covariate dzud risk limits risk sharing" — "species mix … as the hedge" is a paraphrase
  beyond them, and the row's scope limit (one Mongolian subdistrict, 2012–14) is dropped.
* **Smallest fix**: add "WoDaaBe, cattle, 1996–97 (S058)" / "Mongolia, Bayankhongor (S060)" to
  those two cells, or move the generalisation into §13's bounded rows.

### F10 — Low — "age-grade herd labour" (entry:59) is an undefined term with a collision risk

* Entry:59, Cattle row, Mobility cell: "follows water and grass; **age-grade** herd labour".
  Uncited and undefined in the entry. Elsewhere the corpus uses "age/sex" herd classes
  (`linguistics/semantic-fields-lexicon-building.md:70`: "herd-age, herd-color, herd-condition
  terms"), and the Nuer *age-grade/age-set* system is a separate ethnographic object that the
  entry's S052 row does not cover (S052 teaches "cow names follow colour …; age/sex cattle
  terms" — naming, not age grades).
* **Smallest fix**: write "age- and sex-class herd labour" (no citation needed, it is a method
  term), which removes the collision.

## Canon decisions

None found. §4 decides no canon; §12 is explicitly NON-CANON (entry:169) and §15 hands canon to
lore-shokunin (entry:199). No finding in this seat is a canon finding.

## Residual risk / verification gaps

* I did **not** re-open any URL (seat bound). F3, F4, F5 rest on the round-50 build seats'
  records (`.ufo/waves/round-50/build/SrcZederDomestication.md`, `SrcBedouin.md`,
  `SrcMongolFiveSnouts.md`), not on my own fetch; the parallel source seats should confirm
  them.
* For §1–§3 and §5–§15 I checked **every** in-corpus anchor and **every** S-id's
  scope/anchor fit, but I did not adjudicate every clause of every sentence in those
  sections the way I did for §4; F7–F9 are the clause-level defects found outside §4.
* The §4 author seat (`ScribeSec04Species.md`) shows the landed §4 is a **rewrite**, not the
  seat's draft: the landed table has 5 columns instead of the draft's 7, drops the
  "Symbolic weight" column, drops the mana/Quinlan/Tanzanian value claims and the
  `india-vedic.md:107` anchor, and drops 13 of the seat's 14 opened sources. That pruning is
  why F2 exists: facts were kept while their unregistered sources were discarded. The
  integrator should diff the seat's draft against the landed §4 cell by cell before accepting.
* F1 and F2 are the two that would, on their own, move a coverage verdict to PARTIAL rather
  than HOLDS; F3 is the one that a later round would surface the first time someone re-checks
  S050's anchor against §4.

## Tooling

No installs, no upgrades, no `pacman`/`uv`/`cargo`/`npm` activity; no tool was needed beyond
`git`, `python3`, `grep`, `sed`, `cat` (all pre-installed). Host disk pressure respected: two
small shared clones under `/tmp` (`/tmp/kr50sec04`, `/tmp/kr50sec04-base`), both removed at the
end of the seat. No lane file was edited except this report; no jj/git state was touched in
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
