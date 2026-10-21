# ReviewSec13 — falsify attack on §13 (calibration bank, living-practice flag, precision traps), §14 (recheck) and §15 (scope/handoff) of the landed pastoralism entry

Seat: `KotodamaR50-2.ReviewSec13-21` (leaf member; no delegation, no background jobs, no mutating git/jj command in the lane).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
Method: private clone `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/revsec13 && git -C /tmp/revsec13 checkout -q 1c779e4a…` (read-only, deleted afterwards). Every byte below was read at the landed commit in that clone; the lane working tree was not trusted for any landed claim. No lane file was edited; this report is the only write.
URLs were not re-opened (other seats own the URL seats; I checked row scope/anchor text only).

## Verdict

**PARTIAL.** The §13–§15 spine of the entry **holds** where it can be checked inside the lane: every in-corpus `path:line` anchor cited in §13–§15 resolves and supports its sentence; every S-id used in the entry exists in `corpus/SOURCES.md`; nine of the ten §13 rows are honestly calibrated against their row's own scope and anchor; §14's factual statements are true; §15's canon-hygiene claim is grounded and no canon decision is taken anywhere in §13–§15.

Six defects are found, two of them material:

| id | severity | locus | defect |
|---|---|---|---|
| **F1** | MODERATE | `:62` vs `:185` | one proposition, two calibration codes — the Botai row is **C** in §4 and **C → R** in §13; the tier-A row S067 supports R for modern horses |
| **F2** | MODERATE | `:189` | living-practice flag overclaims: 6 peoples, 3 rows; **Maasai has no registry row at all**, and the WoDaaBe row it leans on is scope-blocked ("not current practice") |
| **F3** | LOW–MOD | `:187` | the Status cell of the publisher-summary row mixes a **source tier** with a **claim code**; as a claim code, B is wrong (QUALITY criterion 6 rejects the claim) |
| **F4** | LOW | `:191` | precision-traps paragraph carries no source id and adds "**fixed**" seasonal cycle, which S069 does not support |
| **F5** | LOW | `:199` vs `:31-39` | §15's "(§2)" pointer is wrong in both directions: two handed-off owners have no §2 row, one §2 owner is absent from §15's list |
| **F6** | LOW | `:195` | §14's recheck set omits currency re-checks for exactly the rows whose claims decay (S057/S058/S059/S060/S061/S063) and omits the registry row used by §13 row 1 |

Smallest fixes are given per finding. **Author-lane advice, not admission.**

---

## F1 (MODERATE) — the Botai proposition carries two different calibration codes inside one file

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:62` (§4, species table, Horse row, Calibration cell):

```
| Horse | steppe grassland; winter grazing through snow `(to-verify)` | milk (summer), riding, traction | riding multiplies herd range | modern domestic horses do not descend from the Botai lineage (S067): **C** on Botai-as-origin |
```

`…:185` (§13, calibration bank):

```
| Botai horses are the ancestors of domestic horses | C → R for modern horses — S067 | treat early horse use and modern horse origins as different questions |
```

The row that both cite, `corpus/SOURCES.md:96`:

```
| S067 | Librado et al. 2021, The origins and spread of domestic horses from the Western Eurasian steppes, Nature 598:634–640 — … | paper | A | origins of modern domestic horses (DOM2) and the riding/Yamnaya question as stated in the abstract | Abstract | modern domestic horses do not descend from the Botai lineage; DOM2 spreads from the lower Volga-Don from about 2000 BC | mined | 2026-10-21 | 365d | … |
```

The row's own `teaches` field is a **refutation** ("modern domestic horses do not descend from the Botai lineage"), tier A, anchored in the abstract — i.e. **R** for the proposition "Botai horses are the ancestors of domestic horses", exactly as §13:185 says. §4:62 therefore contradicts §13:185 on the same proposition, and it contradicts the code semantics it declares at `:175`:

```
Codes per `calibration-registry.md:35-39` (R rejected, C contested, B bounded, H heuristic, T to-verify).
```

`corpus/knowledge/verification/calibration-registry.md:36` (C): *"Contested empirical or historical interpretation | Preserve alternatives, scope, and discriminating evidence; **do not report one reading as settled**"*. §4:62 states the negative ("modern domestic horses do not descend from the Botai lineage") as settled fact while labelling the same cell **C** — the stop rule C forbids. QUALITY criterion 2 (`corpus/QUALITY.md:9-12`) requires a named status with the reason; here one proposition has two statuses in one file, and the weaker one is in the row a table-reader will hit first.

**Smallest fix** (single cell, `:62`): replace the trailing `**C** on Botai-as-origin` with `**R** on Botai-as-origin for modern horses (S067; C only for the separate question of whether Botai horses were domesticated at all)`. No §13 change needed — §13:185 is the correct one.

## F2 (MODERATE) — the living-practice flag names six peoples and cites three rows; one of the three is scope-blocked, and one people has no row at all

`…:189`:

```
**Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063). Write fictional herds *like* these mechanics, never *as* these peoples (`hunting-foraging-subsistence.md:195`).
```

The design brake itself is correct and its anchor resolves — `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:195`:

```
**Living-practice flag** (per registry practice): hunting/foraging is a live subsistence and identity system for real peoples today — `algonquian.md:145` warns against repackaging a living round as untouched past, and `inuit.md:136-137` marks the ritual register examples as source-specific. Write fictional systems *like* these mechanics, never *as* these peoples.
```

The provenance of the sentence does not hold:

1. **Maasai has no registry row.** `grep -ci maasai corpus/SOURCES.md` → `0`; no S-row anywhere in the lane mentions Maasai (`grep -rn -i maasai corpus/` hits only `myth-symbol/color-symbolism.md:84`, `culture-material/adornment-body-codes.md:18` — red ochre and beadwork, not herding). A factual claim about a living people with no citable source and no `(to-verify)` is exactly what QUALITY criterion 1 (`corpus/QUALITY.md:5-8`) forbids: *"every factual claim carries a cited, checkable source … never laundered into assertion."*
2. **The WoDaaBe row is explicitly scoped against current practice.** `corpus/SOURCES.md:87` (S058), scope column: *"the WoDaaBe seasonal movement system in southeastern Niger as observed 1996–97, cattle only; not Fulani at large, **not current practice**"*. The flag asserts a present-tense fact ("are living practice") on a row whose scope says it cannot support "current practice" — a QUALITY criterion 6 (*"Source authority stays claim-scoped"*, `corpus/QUALITY.md:29`) mismatch, and it is not marked `(to-verify)`.
3. **The Bedu row is dated testimony.** `corpus/SOURCES.md:92` (S063), scope: *"UNESCO's own inscribed description of the Bedu cultural space; **dated testimony, not ethnography**"*.
4. **Mongolian and Tibetan are named but uncited in the flag**, although rows exist and fit: `corpus/SOURCES.md:89` (S060, Ahearn 2018, Mongolian risk management) and `corpus/SOURCES.md:90` (S061, Wiener/Han/Long 2003, Qinghai-Tibetan Plateau). The parenthetical maps 1:1 onto WoDaaBe/Sámi/Bedu only, so a reader cannot tell which row carries Mongolian or Tibetan — and one of them (Maasai) has no row to map to.

**Smallest fix** (`:189`, one sentence):

```
**Living-practice flag.** Sámi (S059) and Bedu (S063) herding are living practice, as are Mongolian (S060) and Tibetan yak herding (S061); WoDaaBe herding was documented in 1996–97 (S058) and is reported as continuing — current status `(to-verify)`; Maasai herding has no registry row in this lane — `(to-verify)`. Write fictional herds *like* these mechanics, never *as* these peoples (`hunting-foraging-subsistence.md:195`).
```

(If the author wants Maasai carried as sourced rather than flagged, that needs a new append-only S-row — SOURCES.md is append-only per its preamble, `corpus/SOURCES.md:9-12` — i.e. a new round, not an in-place row edit.)

## F3 (LOW–MODERATE) — §13 row 9 puts a source tier in the claim-code column

`…:187`:

```
| The publisher's summary of a book is the book's argument | B — S057 is a description only (QUALITY criterion 6) | cite programme and scope, not conclusions |
```

Two problems in one cell.

* **Claim/code mismatch.** The Claim cell states the bad practice as a proposition. QUALITY criterion 6 (`corpus/QUALITY.md:29`) says plainly: *"publisher descriptions and abstracts are tier B for substantive claims about a work, even when accurate"*. As written, the proposition is **rejected**, i.e. **R** under `verification/calibration-registry.md:35` ("Rejected/discredited as the specified general inference"), not **B** ("Bounded, usable within a named domain", `:37`). The "What to say instead" column is right ("cite programme and scope, not conclusions"), so the *brake* works — only the code label is wrong.
* **The letter is ambiguous between two vocabularies.** Every other row's letter is a claim code (R, C, B, R, C, R, C→R, B); here "B" is S057's *tier* (`corpus/SOURCES.md:86`, tier `B`: *"the book's stated programme and chapter list only (publisher description; QUALITY criterion 6); ethnography and conclusions unread"*). A reader following the header at `:175` reads the B as a claim code.

**Smallest fix** (`:187`): either

```
| The publisher's summary of a book is the book's argument | R — S057 is a publisher description (tier B, QUALITY criterion 6); use it for programme and scope, never for conclusions | cite programme and scope, not conclusions |
```

or restate the claim positively so that B fits: *"A publisher's description may stand for the book's programme and scope"* → **B — S057 (tier B, QUALITY criterion 6)**.

## F4 (LOW) — the precision-traps paragraph carries no source id and adds "fixed"

`…:191`:

```
**Precision traps.** "Nomad" names a mobility strategy and "pastoralist" a livelihood; neither names a stage or a people. "Transhumance" is a fixed seasonal cycle, not any movement.
```

* **No citation at all.** The parallel paragraph in the entry this one was modelled on cites inline: `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:190` — *"…(S033's correction: even 'forager' is contested as an inclusion criterion); 'subsistence' is not 'poverty' (S038's frame)…"*. Here the definitional claims about "nomad"/"pastoralist" and "transhumance" have no row id, against QUALITY criterion 1.
* **"fixed" overreaches the row.** `corpus/SOURCES.md:98` (S069, tier A, UNESCO ICH decision 14.COM 10.b.2): *"transhumance is the **seasonal movement of people with their livestock between regions**; horizontal (plain or plateau) and vertical (mountain) types"*, anchor *"decision text, sentence 4; element page … sentence 1"*. The Gate bullet (`corpus/lessons/round-50.md`, S069) records: *"Two broad types of transhumance can be distinguished: horizontal transhumance, in plain or plateau regions; and vertical transhumance, typically in mountain regions."* Nothing there fixes the route or the cycle; "fixed" is an addition, and it sits next to the entry's own §3 row where transhumance is defined as "seasonal movement of people with their livestock" — a cycle, not a fixed itinerary.

**Smallest fix** (`:191`): drop "fixed" and cite the row: *"…'Transhumance' is a seasonal cycle between regions, not any movement (S069)."*

## F5 (LOW) — §15's "(§2)" pointer does not match §2's boundary table

`…:199` (§15):

```
… hands the field, the hunt, the dish, the cloth, the road, the market, the lexicon field, **the animal sign and the shepherd-king** to their owners (§2).
```

`…:31-39` (§2, One-owner boundary table) has exactly nine rows:

```
| `agrarian-field-system-lexicon.md:56,:62` | … | `hunting-foraging-subsistence.md:36,:116` | … | `cuisine-food-lexicon.md:67,:86` | … |
| `transport-mobility-lexicon.md:95` | … | `trade-economy-lexicon.md:69` | … | `textile-technology.md:27` | … |
| `semantic-fields-lexicon-building.md:70,:105` | … | `fire-fuel-light.md:37` | dung as fuel versus manure | the herd as dung source | `civilizations/` regional entries | … |
```

* **§2 has no row for the animal sign** (`myth-symbol/animal-symbolism.md:73,:110`) **or the shepherd-king** (`myth-symbol/sacred-kingship-mythic-charter.md:65`), yet §15 hands both to "their owners (§2)". Both owners are cited in §10 (`:141` for the shepherd-king, `:145` for the animal sign) and named in the frontmatter couples line (`:8`), but the §2 table — the boundary table — omits them. §2 likewise omits the three ritual owners §10 cites (`ritual-liminality.md:63`, `symbolism-synthesis-method.md:69`, `celestial-symbolism-calendars.md:28`), which §15 claims ownership against ("the herd's ritual ledger").
* **§2 does own `fire-fuel-light.md:37` (dung as fuel),** which §15's handoff list never mentions — so the two lists are not the same list.

**Smallest fix** (one of two, no new content needed): either add the missing rows to §2's table (`animal-symbolism.md:73,:110`; `sacred-kingship-mythic-charter.md:65`; the three ritual owners) — which also makes §2 match the frontmatter anchor list at `:6` — or drop the "(§2)" pointer from `:199` and cite §2 for the eight owners it really lists, §10 for the animal sign and the shepherd-king.

## F6 (LOW) — §14's recheck set does not cover the rows whose claims decay

`…:195`:

```
Before relying on any §13 row, re-check its row id in `corpus/SOURCES.md`; open Herskovits 1926 and Ostrom 1990 before quoting them (only S053 and S055 are opened); re-open S050 and S067 before quoting a date; re-run the head's gap sweeps before claiming the gap is still fresh.
```

Everything in that sentence is **true** (verified below), but the set is aimed at *provenance* (unopened texts, dates, sweeps) and not at *currency*, which is where §13's live claims live:

* S058 (WoDaaBe) — fieldwork 1996–97, scope "not current practice" (`corpus/SOURCES.md:87`);
* S059 (Sámi register) — page footer "Senast uppdaterad 13 december 2024" (`:88`);
* S060 — 2013 Statistical Yearbook data reported in 2018 (`:89`);
* S061 — 2003 book (`:90`);
* S063 — inscription record, "dated testimony" (`:92`);
* S057 — publisher page, tier B, "conclusions unread" (`:86`).

The §13 living-practice flag (F2) is exactly the row that rests on these, and §14 gives it no currency instruction; "re-check its row id" only means re-read the row, not re-open the source. The frontmatter `recheck:` line (`:12`) is stronger in one respect (it pairs S054+S055 "together before writing a commons rule") and weaker in another (it also says nothing about currency), so neither place carries the instruction.

**Smallest fix** (append to `:195`): *"re-open S058 and S063 and re-check S060 and S061 before asserting any of them as living practice today; re-read `verification/calibration-registry.md:142` for the stage-ladder row."*

---

## What holds (checked, no action)

**§13 in-corpus anchors — both resolve and support their sentence.**

* `:175` "Codes per `calibration-registry.md:35-39`" — `corpus/knowledge/verification/calibration-registry.md:35-39` is exactly the five code rows, and the glosses match verbatim: `:35` R "Rejected/discredited as the specified general inference", `:36` C "Contested empirical or historical interpretation", `:37` B "Bounded, usable within a named domain", `:38` H "Heuristic or interpretive framework", `:39` T "Unresolved provenance or claim check | Mark `(to-verify)` inline at the exact dependency". The entry's glosses (rejected / contested / bounded / heuristic / to-verify) are correct.
* `:179` `calibration-registry.md:142` — `…/verification/calibration-registry.md:142` = *"| Stone–Bronze–Iron, dynastic decline or subsistence predicts a total social stage — R | … |"* — supports the stage-ladder row (subsistence as a social stage → R). The parallel brake in the same file is `corpus/knowledge/civilizations/mongol.md:40`: *"This is a working periodization, not a ladder from 'primitive nomad' to 'civilization.' Mobile pastoralism, urban production, and documentary administration can coexist."* — supports §3's "never a ladder" and §11's "mobile pastoralism coexists with other production".
* `:181` S053 — `corpus/SOURCES.md:82`, tier A, scope *"the article's own attribution of the label cattle complex to Herskovits 1926 and its critique of the analyst vocabulary; not Herskovits' text"*, `teaches` *"… Herskovits 1926 itself unopened"*. The row's `(to-verify)` on the 1926 text sits at the right dependency (code T, registry `:39`), and the C code matches the row's *"contested standing"*.
* `:189` `hunting-foraging-subsistence.md:195` — quoted above; supports the "like these mechanics, never *as* these peoples" wording verbatim.

**§13 S-id rows — nine of ten are honestly calibrated against their own row scope/anchor.**

| row | S-id | row scope/anchor says | entry says | verdict |
|---|---|---|---|---|
| `:179` stage ladder | S048 | SOURCES.md:77, tier B, *"the evolutionary-stage reading is refuted"* | R | holds |
| `:180` pure nomad | S056 | :85, tier A, *"nomads always needed external grain and crafts"* | R as description | holds |
| `:181` cattle complex | S053 | :82, A, attribution + critique; 1926 unopened | C + `(to-verify)` | holds |
| `:182` Hardin vs Ostrom | S054/S055 | :83 *"a counterfactual baseline, not a law of pastoral life"*; :84 *"design principles as diagnostic, not a predictive law"* | R as universal; B for open access | holds |
| `:183` Sherratt | S051 | :80, B, *"adoption idiosyncratic and not tied to one century or millennium"* | C | holds (and the sibling seat `ReopenS051.md` opened the live abstract and confirmed all three S051 citations, quote byte-identical to the Gate — the attribution of the quoted clause to Sherratt's own phrasing is therefore supported; no F5-style quote defect here) |
| `:184` bones get smaller | S050 | :79, A, *"herd management … is legible before morphological change"* | R | holds |
| `:185` Botai | S067 | :96, A, *"modern domestic horses do not descend from the Botai lineage"* | C → R | holds — but see **F1** for the §4 contradiction |
| `:186` Nuer | S052 | :81, A, *"not contemporary Nuer practice, not a pastoral universal"* | B | holds (B = bounded to one 1940 ethnography, exactly the registry's `:37` use) |
| `:187` publisher summary | S057 | :86, B, *"the book's stated programme and chapter list only"* | see **F3** | brake holds, code label wrong |

**No phantom identifiers.** Every S-id in the file is in range and exists:

```
$ grep -o 'S0[0-9][0-9]' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | sort -u
S048 … S069      (22 ids, exactly the rows this round opened)
$ for i in <those>; do grep -q "^| $i |" corpus/SOURCES.md || echo "MISSING $i"; done
(no output — none missing)
```

**Gate quotes present.** `corpus/lessons/round-50.md:27-54` carries a `## Gate` bullet for each of S048–S069 with URL, access date 2026-10-21 and a verbatim quote; the S048–S069 rows in `corpus/SOURCES.md:77-98` carry URL, tier, scope, anchor, `teaches`, status `mined`, access date 2026-10-21, recheck 365d, used-by = the new entry. The entry's frontmatter `:8` claim ("each with URL, access date, tier scope and anchor … the round lesson's located quote") is accurate.

**§14's factual statements are true.** `corpus/SOURCES.md:142` (round-50 search log) lists among the opened-but-not-registered leads: *"Herskovits 1926 (all routes 403; S053 carries the attribution) … Ostrom 1990 publisher record …"* — so "only S053 and S055 are opened" is correct in substance: no Herskovits-1926 text and no Ostrom-1990 text was read; S055's own scope says *"not the 1990 book's wording"* (`corpus/SOURCES.md:84`). S053's scope says *"Herskovits 1926 itself unopened"* (`:82`). The re-open of S050/S067 before quoting a date matches their scopes (*"not post-2008 chronology"*, `:79`; aDNA chronology, `:96`). (Minor, non-blocking: the Ostrom 1990 *publisher record* was reached as a lead, so "only S053 and S055 are opened" is true of the texts, not of every URL touched.)

**§15's canon hygiene is clean and grounded.** `corpus/knowledge/synthesis/worldbible-integration-contract.md:15` — *"Initial bilateral acknowledgement is **pending** until those records exist; writing this file is not a substitute for lore's read."*; `:69` — *"An unbound research packet may be retained as reference but cannot be imported as canon without a lore baseline and a new reviewed handoff."* That is exactly what `:199` claims: *"the lore intake of the integration contract is still pending, so every handoff is a candidate, not an import."* QUALITY criterion 5 (`corpus/QUALITY.md:18-20`) is satisfied: §13–§15 contain **no canon decision** — the §13 "What to say instead" column is method, not world truth; §12 (`:167-171`) is explicitly `**NON-CANON.**` with the closing line *"The Ketrun are a different economy from the valley farmers, not an earlier stage of them."*; §15 hands canon to lore-shokunin. The build-wave connector reached the same state from the other side (`.ufo/waves/round-50/build/ConnectSiblingPastoral.md:47`: *"Mark intake as pending, not available"*, citing lore's uncovered `CM-g`).

**Frontmatter counts reproduce.** From the landed clone: `find corpus/knowledge -name '*.md' | wc -l` → `226`; `ls corpus/knowledge/culture-material/*.md | wc -l` → `28`; `python3 -B reports/round-28/readme/sweep.py` → `rows 226 files 226 / missing_from_index 0 / topic_mismatch 0 / footer_ok True`, `exit=0` — matching the `verified-at:` line at `:9`. README row present at `corpus/README.md:297`.

---

## Residual risk / verification gaps

1. **URL-level truth is out of my seat.** I checked row scope/anchor text against entry sentences; the URL re-opens, verbatim-quote presence and tier honesty for S048–S069 are the `ReopenS04x-…`/`ReopenS06x-…` seats' call. Where I wrote "holds", I mean *holds against the row as filed*.
2. **F2 depends on the intent of the parenthetical.** If `(S058, S059, S063)` is read as "the rows this flag leans on" rather than "the rows for each named people", the Maasai gap and the S058 currency gap still stand: one named people has no registry row in the lane, and one cited row's scope says "not current practice" while the sentence asserts the present. A `(to-verify)` on Maasai (and, if the author wants it strong, a current-practice source for WoDaaBe) is the minimum honest repair.
3. **F1 could be read as a deliberate scope split** (C for the Botai-domestication question, R for modern-horse ancestry). If so, §13:185 and §4:62 must say so explicitly; as written the file states one proposition twice with two codes and no scoping sentence.
4. **Not audited here** (other seats): §§1–12's body rows and their per-row S-ids (my §4/§6 cross-references F1 and the S051 note are the only body touches), the README row's `check-readme-revisions.py` behaviour, the receipt guard, the separability checker and the jj probe. I did not run any tool under `tools/` except the read-only `reports/round-28/readme/sweep.py`, which writes only into a temp tree.
5. **Path-form note (non-blocking).** The body cites the registry by bare name (`:175`, `:179`, `:162`) while the frontmatter anchor list (`:6`) spells it `verification/calibration-registry.md`. The bare form is the existing lane convention — the model entry this one was built from uses it verbatim at `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:178` — so I do **not** count it as a defect; it is noted only because a reader resolving `:179` by path prefix will not find the file under `culture-material/`.
6. **No lane mutation.** No `git add/commit/stash/checkout/reset`, no mutating `jj` command, no writes outside this report; the `/tmp/revsec13` clone was removed after reading.

**Tooling:** no installs were needed for this seat — every check used the git clone already present (`git 2.x` from the base system) plus `grep`/`awk`/`find`/`python3` (system). Nothing was installed or updated; no version/channel record is owed.

## Smallest fix, whole set (one authoring pass)

| locus | edit |
|---|---|
| `:62` | `**C** on Botai-as-origin` → `**R** on Botai-as-origin for modern horses (S067; C only for whether Botai horses were domesticated)` |
| `:189` | re-scope the living-practice list to S060/S061/S059/S063, mark WoDaaBe current status `(to-verify)`, mark Maasai `(to-verify)` (or add a new append-only S-row in a later round) |
| `:187` | change the Status cell to `R — S057 is a publisher description (tier B, QUALITY criterion 6); programme and scope only` (or restate the claim positively so B fits) |
| `:191` | drop "fixed"; add `(S069)` |
| `:199` | align the handoff list with §2, or drop the "(§2)" pointer for the animal sign and the shepherd-king and cite §10; add `fire-fuel-light.md:37` to the handed-off list |
| `:195` | append the currency recheck for S058/S063/S060/S061 and the registry re-read for `:142` |

**Report:** `.ufo/waves/round-50/falsify/ReviewSec13.md`
