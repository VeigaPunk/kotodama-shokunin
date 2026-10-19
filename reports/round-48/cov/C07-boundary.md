# C07 — boundary verifier (claim C): neighbour dispositions, over-claim and under-claim

- Seat: `C07` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, measured this seat, 2026-10-19), equal to `reports/round-48/claims.json:8`
- Out path: `reports/round-48/cov/C07-boundary.md` (this file)
- Non-author statement: I drafted no cartography fragment and edited none. No r48 C01 entry body existed at my read cut (`find reports/round-48 -type f` → claims, targets, telemetry only), so I audited the **only drafted boundary surface** — r47's filed fragments — and converted the result into a binding boundary contract for the r48 right-sized redraft. After my first cut, K01's right-sized spec (`reports/round-48/scout/K01-rightsized-spec.md:213-231`) and C15's neighbour audit (`reports/round-48/cov/C15-neighbors.md`) were filed; both are reconciled in §4.3 and the verdicts below distinguish **r47 bytes** from **r48 spec**. I wrote only this file.

**Verdict.** The two boundary rulings the mission names both **hold on live bytes**: divination is not a collision, and `cosmology-cosmography.md` owns the T-O **symbolic** diagram while explicitly disclaiming the survey sheet (`:71`, `:102`). The boundary surface is **not yet landing-ready** on four points:

- **O1 (blocking, over-claim; persists into the r48 spec):** the gap sentence `C01:90` says "No entry owns the **made map**" but cites only `:71`/`:102`; the same file's own definition at `cosmology-cosmography.md:27` says cosmography is "how the world is drawn (**maps**), named …". K01's spec row `:217` now cites `:27`, which closes it **if the draft body carries the same sentence**; the row alone does not (the body can still assert the unqualified claim). C15 independently confirms the omission (§4.3).
- **O2 (r47 bytes only; already resolved in the r48 spec):** `C01:99` gave this entry "the plan as a cadastral object"; `architecture-settlement-lexicon.md:95` already says "The grid is **cadastral**". K01's spec row `:223` correctly drops that phrase and says only "land survey as a map-production step". The redraft must not reintroduce it.
- **U1 (blocking, under-claim; persists into the r48 spec):** `agrarian-field-system-lexicon.md` owns the PARCEL and CLAIM institutions, tenure/boundary words and work-unit land measures (`:4`, `:42`, `:114`, `:122-125`). No r47 fragment mentions it (grep: 0 hits in C01–C04), **and K01's 13-row table omits it too** (`K01-rightsized-spec.md:215-229`). A cadastral claim that ignores the prior owner of parcel/claim is an under-coupling.
- **R1 (r47 bytes; anchor fixed in the spec, restatement still open):** `C02:248` restates craft's apprentice→journeyman→master ladder and anchors it at `craft-artisan-lexicon.md:44`; `:44` is the Steel (Japan) material-grading row, `:3` is the topic line, and the ladder table is `:54-65`. `C02:421` then certifies the wrong anchor as "real". K01's spec row `:226` uses the correct `:54-65` anchor; the **body sentence** must still be reduced to a citation-and-delta (§6.7).

Everything else the mission asks about is **PASS** (§3–§4). The neighbour census is measured in §2; the two named cases in §4; exact replacement rows in §6.

---

## 1. What I audited, and against what

The r47 fragments are filed bytes I may read, not edit. Their digests at my read cut:

```
$ sha256sum reports/round-47/cov/C0[1-4]*.md
cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d  C01-entry-a.md   (358 lines)
5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af  C02-entry-b.md
4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5  C03-entry-c.md
cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0  C04-entry-header.md
```

The three boundary surfaces I read:

| Surface | Where | What it dispositions |
|---|---|---|
| C01 §1.1 table | `reports/round-47/cov/C01-entry-a.md:94-103` | 8 neighbours (cosmology, sacred topography, direction, architecture, writing media, Mesoamerica, transport, naming) |
| C02 §7–§8 secondary notes | `C02-entry-b.md:248`, `:300`, `:421`, `:456-460` | craft, vessel, sacred kingship, japan-sengoku (narrative only) |
| C04 `- couples:` | `C04-entry-header.md:159` | the same set as C01, plus "does not own" list at `:162` |

This is a **boundary** audit, not a content audit: I test whether each row's owned/adjacent ruling is true at HEAD, and whether the body actually keeps the boundary the row declares. I do not re-score depth (R03/r48 reviewers do).

---

## 2. Neighbour census at HEAD (measured, not carried)

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' -o -iname '*atlas*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|mappa|survey map|world map|atlas of)' corpus/knowledge/
0
```

Demand, two reproducible readings (same pattern text, different strictness):

```
$ pat='cartograph|mapmak|portolan|cadastr|mappae|mappa mundi|surveyor|theodolit|compass rose|graticule|hereford mappa|lienzos?|stick chart|star chart|world map|map of|maps of|drawn map'
$ grep -rliE "$pat" corpus/knowledge/ | wc -l   → 29
$ grep -rniE "$pat" corpus/knowledge/ | wc -l   → 35

$ pat='cartograph|mapmak|portolan|cadastr|mappa mundi|surveyor|theodolit|compass rose|graticule|star chart|world map|drawn map|lienzo'
$ grep -rliE "$pat" corpus/knowledge/ | wc -l   → 5
$ grep -rniE "$pat" corpus/knowledge/ | wc -l   → 9
  (cosmology-cosmography 2; mesoamerica-primary-sources 4; architecture-settlement 1;
   japan-medieval-sengoku 1; direction-symbolism 1)
```

**Arithmetic correction for the redraft.** `reports/round-44/scout/K02-gap-scout.md:151` states the genuine footprint is "seven files / nine lines", but its own table (`:155-162`) lists **eleven** line anchors across seven files (cosmology ×2, Mesoamerica ×1, architecture ×1, japan ×1, direction ×1, polynesia ×4, timekeeping ×1). The reproducible numbers are **29 files / 35 lines** (broad pattern, as the seed itself reports at `:148`) or **5 files / 9 lines** (cartographic vocabulary only). The honest middle — 7 files / 11 lines — adds the two non-vocabulary handoffs (`polynesia-navigation.md:52`, `timekeeping-instruments.md:50`). The r48 `- gap filled:` must use one of these measured sets and say which pattern produced it; do not copy "seven files / nine lines".

**What the census does and does not prove.** It proves 0 owners, and it proves the demand is by-product/handoff, not omission. It does **not** prove the sheet is unowned in the sense of "no entry says anything about maps": `naming-systems.md:70` says "a map is an archive of coups", and `cosmology-cosmography.md:27` includes maps in cosmography. Both are dispositioned below.

---

## 3. Ruling table — every neighbour, every disposition

Legend: **PASS** = the row's owned/adjacent split is correct at HEAD; **OVER** = the draft claims an object the neighbour owns; **UNDER** = the draft leaves a real owner undispositioned; **RESTATE** = the body reproduces the neighbour's content instead of citing it. Line numbers are in the **live corpus**, re-read this seat.

| # | Neighbour | What it owns (verified) | Draft disposition | Verdict |
|---|---|---|---|---|
| 1 | `myth-symbol/cosmology-cosmography.md` | five world-model axes; T-O as symbolic (`:71`, `:102`); toponyms as cosmographic claims and "a fictional map is a set of etymological arguments" (`:133`); **cosmography = "how the world is drawn (maps)…"** (`:27`) | `C01:96` cites `:71,:102,:133`; `C01:90` names it as "world model"; neither cites `:27`. K01's spec row `:217` now cites `:27` | **OVER (O1)** — the spec row is necessary but not sufficient: the **body sentence** must carry `:27` too (§6.1) |
| 2 | `myth-symbol/sacred-topography-pilgrimage.md` | place register, six holy-site properties, route-as-rite, three route types (`:5`, `:69`), votive economy, shrine institution | `C01:97` takes "representation of a route" and the pilgrimage document; cites `:5,:69` | **PASS** — the diagram (radial/quartered/corridor) stays there; the measured sheet is here. One wording note: `C01:242` lists "scroll, strip, road book" as the itinerary medium, but the itinerary **text** genre is sacred topography's (`:167-168` shelf: Egeria, Petrarch, Ibn Jubayr). Say "the drawn strip, not the itinerary text" (P2) |
| 3 | `myth-symbol/direction-symbolism.md` | orientation frames, cardinal coinage, the compass trap (`:51`); **explicitly rules the compass rose out of the in-world direction code** — "never as a compass rose with a legend" (`:26`) | `C01:98` takes the sheet convention (rose, north arrow, graticule), cites `:51` | **PASS**, and `:26` is *better* evidence than `:51` for the split; add it to the row |
| 4 | `culture-material/architecture-settlement-lexicon.md` | city-plan lexicon, castrum grid, groma sentence, and "**The grid is cadastral**: a state that *measures land* builds this city" (`:95`) | `C01:99` takes "land survey as a map-production step **and the plan as a cadastral object**" | **OVER (O2, r47 bytes)** — the cadastral **plan** is architecture's; cartography takes the drawn **register**. K01's spec row `:223` already drops the phrase; do not reintroduce it (§6.2) |
| 5 | `culture-material/agrarian-field-system-lexicon.md` | the four institutions PARCEL / IMPLEMENT / WATER / CLAIM (`:4`, `:42`); tenure and boundary words; work-unit land measures (jugerum, morgen, acre, hide, carucate — `:122-125`); the claim layer, tithe/rent/sharecropping (`:114`) | absent from C01, C02, C03 and C04 (`grep -n 'agrarian\|parcel\|tenure'` → no table row; `parcel` appears only as a map object at `C01:185,:243`); **also absent from K01's 13-row spec** | **UNDER (U1, blocking for r48)** — add the row (§6.3) |
| 6 | `culture-material/writing-media-surface-economy.md` | seven surface families, cost ladder (`:3`), survivor's ledger (`:81`) | `C01:100` takes map-specific media/reproduction; `C02:196` cites the ladder and the survivor bias; K01 spec row present | **PASS** — the body cites `:64-78`, `:81` and does not restate the seven families |
| 7 | `civilizations/mesoamerica-primary-sources.md` | lienzo / cartographic-history source class; "the copy chain is the evidence" (`:58`) | `C01:101` takes the genre as a map form; `C01:144` quotes the copy-chain rule; K01 spec row present | **PASS** |
| 8 | `culture-material/transport-mobility-lexicon.md` | route + maintenance institution (`:28`), DR-TR-02 (`:117`) | `C01:102` takes "how a route is drawn"; cites both; K01 spec row present | **PASS** |
| 9 | `linguistics/naming-systems.md` | onomastics (`:40`), critical toponymy — "a map is an archive of coups" (`:70`), taboo-shifted place names (`:97`) | `C01:103` takes the toponym layer; `C01:90` quotes `:70`; K01 spec row present | **PASS** — the row must keep `:70` attributed; the "archive of coups" idea is naming's, the sheet application is this entry's |
| 10 | `culture-material/craft-artisan-lexicon.md` | workshop register, seven guild systems and the ladder table (`:54-65`), six-type mark typology (`:76`, Dürer–Raimondi `:87`) | `C02:248` **restates** the ladder; cites `:44` (Steel row) and `:3` (topic line); `C02:421` certifies `:44` as "workshop ladder table … real". K01's spec row `:226` uses `:54-65` | **RESTATE + false anchor (R1)** — the spec anchor is fixed; the **body sentence** must still become citation-and-delta (§6.7) |
| 11 | `culture-material/trade-economy-lexicon.md` | measures and their sacred standardization (`:3`, the four sources at `:17`); guild/contract vocabulary (`:106-116`) | body uses it as a measure owner (`C01:145`) and for the printing privilege (`C02:267`); K01's spec row `:227` dispositions tally/contract (`:92`, `:121`) only | **UNDER (U2)** — the row exists in the spec but the **measure edge** is unstated; add the scale-bar split (§6.4) |
| 12 | `myth-symbol/celestial-symbolism-calendars.md` | constellations/asterisms, planet-as-god identities, calendar mechanics (`:3`) | form typology includes the star chart (`C01:246`); K01's spec adds the row (`:220`) | **RESOLVED in spec** — keep the row; the body must cite the sky owner at the star-chart form (§6.5) |
| 13 | `myth-symbol/sacred-kingship-mythic-charter.md` | mythic charter / eight legitimation channels / royal register (`:3`) | `C02:300` states the legal-vs-mythic charter split; K01's spec adds the row (`:221`) | **PASS-with-note** — promote the C02 sentence into the table (one authoritative surface; C08 P2-1 agrees) |
| 14 | `myth-symbol/divination-omen-systems.md` | sign-reading technology; its own §8 boundary table (`:147-159`) names seven neighbours and **not** cartography | no divinatory material anywhere in C01–C04; K01 spec carries the optional non-collision row (`:222`) | **NOT A COLLISION** — see §4.1 |
| 15 | `culture-material/timekeeping-instruments.md` | five instrument families incl. SKY: gnomon/astrolabe (`:3`, `:24-27`); "longitude at sea" (`:50`) | `C02:72` cites `:50` only; the survey chain names astrolabe/armillary without a row; absent from K01's 13 | **UNDER (U4, P2)** — add the row (§6.6) |
| 16 | `civilizations/polynesia-navigation.md` | wayfinding: horizon compass, steering-star sequence, sky mnemonic, landfall (`:52`); "a mental bearing framework, **not a chart**" (`:60`) | `C02:73` states the "chartless boundary" in prose; absent from K01's 13 | **PASS-with-note** — the prose disposition is correct; promote to a row for one authoritative surface (P2) |
| 17 | `culture-material/material-culture-inference-method.md` | the inference method; perishability — "what survives to be seen; memory politics" (`:69`) | cited as a source at `C02:196`, `C03:168`, `C04:126`; no row | **PASS** — cited, not restated; an optional row is P3 |
| 18 | `civilizations/japan-medieval-sengoku.md` | the periodization caution: "a neat Edo cadastral map must not be treated as a direct Sengoku map" (`:157`) | `C02:478` cites it as a calibration precedent | **PASS** — no row required |
| 19 | `myth-symbol/symbolism-synthesis-method.md` | the five canonical registers — color, animal, number, celestial body, direction (`:23`) | `C01:105` cites `:23` for the register-of-registers rule | **PASS** — see §5 |

No row creates a second owner. The failures are precision failures (what exactly is taken) and completeness failures (an owner left unnamed), not collisions.

---

## 4. The two named cases

### 4.1 Divination — **not a collision** (confirmed)

Measured, not carried — the exact hits, with their context:

```
$ grep -noiE '\bmap\b|maps|cartograph|survey|chart' corpus/knowledge/myth-symbol/divination-omen-systems.md
25:chart     # "... (charter myths of an oracle)"      — substring of "charter"
163:maps     # "The code maps to twelve prescriptions" — verb
214:chart    # "... charter myths of an oracle couple" — substring of "charter"
216:maps     # "... maps directly onto that gate's symbol-ledger row" — verb
```

Four term hits, **zero cartographic objects**: two are the substring inside "charter", two are the verb "maps". There is no `cartograph`, `survey`, `map`-as-noun, `chart`-as-object or projection term in the file. The file's topic (`:3`) is question → technique → closed sign space → licensed reader → prescription. Its own §8 ("Boundary — what this entry does not own", `:147-159`) names celestial-symbolism, cosmology, motif-index, ritual-liminality, naming, the myth-consistency gate and civilization bases — **cartography is not among them**. Geomancy (`:189`) and feng-shui siting are reading technologies; architecture owns the siting/plan, this entry owns the sheet. The draft contains no divinatory material, so **no row is required**; the optional one-line non-collision note is harmless (P3) but must not be presented as a discovered collision.

### 4.2 Cosmography — T-O is symbolic, the survey sheet is not owned (confirmed, with the `:27` gap)

Three live anchors, each re-read:

```
$ sed -n '27p;71p;102p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
:27  **Cosmography** = the projected, inhabited version: how the world is drawn (maps),
     named (toponyms), walked (processions, pilgrimage), and built (cities, temples).
:71  | Medieval Christian: T-O | ... Hereford Mappa Mundi c. 1300;
     T-O diagrams are symbolic, not survey maps (§10) |
:102 ... T-O diagrams are symbolic devices, not cartographic claims.
```

The ruling the mission names is correct: **cosmography owns the world-drawn/cosmogram content; it explicitly disclaims the survey map.** But `:27` is the competing definition — "drawn (maps)" is exactly the phrase a strict one-owner reader will quote against "No entry owns the made map" (`C01:90`). The disclaimers win, but only if the entry shows the reader both. It currently shows one side. That is O1.

`C08-boundary.md` claimed the wording was "resolved in the current revision (`C01:247`)". At the sha I read (`cfb429…`, the same digest R03 read), `C01:247` is the cosmographic **form** row, which says "the form belongs to `cosmology-cosmography.md`" — it contains no `:27` citation, and `grep -n ':27' C01-entry-a.md` returns **0**. Whatever revision C08 read (`a02031…`), the filed bytes at `cfb429…` still omit `:27`. The fix must land in the redraft, not be assumed landed.

### 4.3 Reconciliation with the r48 spec (K01) and C15

Both were filed after my first cut; I read them at the same baseline.

- **Convergence.** C15 independently finds the same `:27` omission (its F1) and the same no-second-owner result for the seven K02 neighbours; my §3 agrees 7/7 on disposition and extension. C15's "7/7 PASS" does **not** contradict O2, because C15 tests disposition/extension/bleed, not the width of the "take" phrase — `C01:99`'s "the plan as a cadastral object" is exactly a take-phrase defect.
- **K01's 13-row table** (`reports/round-48/scout/K01-rightsized-spec.md:215-229`) already closes three of my r47 findings at spec level: it cites `:27` in the cosmology row (`:217`), uses the safe architecture wording ("land survey as a map-production step", `:223`), and uses the correct craft ladder anchor `:54-65` (`:226`). O1 is closed **only if the draft body carries the `:27` sentence as well** — a row is not a body.
- **Still open in K01's spec:** the 13 rows omit `agrarian-field-system-lexicon.md` entirely (U1 — the one live blocking gap for r48); the trade-economy row (`:227`) dispositions tally/contract (`:92`, `:121`) but not the measure edge (`:3`, `:17`), so the scale-bar split (U2) is unstated; the craft row is correct but the **body** sentence (`C02:248`) still restates the ladder (R1); timekeeping and polynesia remain body-only (P2).
- **Net for r48:** four P1 fixes — add the agrarian row, add the measure clause to the trade row, reduce the craft ladder sentence to a citation-and-delta, and carry the `:27` sentence into §1 — plus two P2 rows (timekeeping, polynesia). None changes the entry's topic, partition or length materially.

---

## 5. Register-of-registers check — PASS

`C01:105` claims the map is a "composition register" that owns no component register. Every component it names has a live owner file:

```
$ ls corpus/knowledge/myth-symbol/{color,animal,number,celestial-symbolism-calendars,direction}-symbolism.md
color-symbolism.md  animal-symbolism.md  number-symbolism.md
celestial-symbolism-calendars.md  direction-symbolism.md
$ ls corpus/knowledge/linguistics/numerals-and-measures.md
corpus/knowledge/linguistics/numerals-and-measures.md
```

All five canonical registers from `symbolism-synthesis-method.md:23` exist as files, and the measure register has its own entry. The composition claim is therefore not an orphan claim. **No second owner of any register is created.** The only register-shaped object the draft takes (the "slot grammar") has no prior owner — verified by the 0-topic-owner sweep in §2.

---

## 6. Exact fixes (integrator/redraft-ready)

Fenced blocks below are **draft text for the corpus entry**, not applied bytes. The r48 redraft may merge them.

### 6.1 O1 — cite `:27` and state the split (one sentence in §1 + the row)

Replace the cosmology row (`C01:96` at the audited sha) with:

```markdown
| `myth-symbol/cosmology-cosmography.md` | the five world-model axes (center / layer-count / direction-code / world-shape / age-doctrine); cosmography as "how the world is drawn (maps), named, walked, built" (`:27`); the T-O diagram as a symbolic device (`:71`, `:102`); toponyms as cosmographic claims (`:133`) | the **contrast case**: cosmography owns the world-drawn content and explicitly disclaims the survey sheet (`:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production. It does not restate the five axes, the flat-earth calibration or the cosmogram typology |
```

And in the gap sentence (`C01:90`), after "…as **world model**":

```markdown
(`myth-symbol/cosmology-cosmography.md:27,:71,:102` — cosmography owns what the world is drawn *as*; `:71`/`:102` disclaim the surveyed sheet)
```

The wording rule: **cosmography owns the drawn world-picture; this entry owns the measured sheet.** Do not write "cosmography owns no maps" — `:27` falsifies that sentence.

### 6.2 O2 — split cadastral three ways (architecture vs agrarian vs cartography)

Replace the architecture row (`C01:99`) with:

```markdown
| `culture-material/architecture-settlement-lexicon.md` | the city-plan lexicon, the castrum **grid** and the groma sentence — "The grid is cadastral: a state that *measures land* builds this city" (`:95`); the sacred precinct | the **drawn cadastral register** — the sheet of parcels — and land survey as a map-production step. The built plan and the settlement vocabulary stay there; this entry cites `:95` and does not restate the groma/centuriation chain |
```

This is the precise split: architecture owns the **built cadastral plan**, agrarian owns the **parcel/claim institution**, cartography owns the **drawn register**. `C04:159` currently says architecture "owns the built plan … this entry owns land survey as a map-production step" — that clause is correct; only C01's "plan as a cadastral object" phrase must go.

### 6.3 U1 — add the agrarian row (P1, blocking)

```markdown
| `culture-material/agrarian-field-system-lexicon.md` | the PARCEL and CLAIM institutions, tenure and boundary words, and the work-unit land measures — jugerum, morgen, acre, hide, carucate (`:4`, `:42`, `:114`, `:122-125`) | the **drawn parcel register**: how a parcel, boundary stone and tenure claim are measured and put on a sheet. The parcel institution, the tenure words and the land-measure equivalences stay there; this entry cites them and does not restate the field-system typology |
```

The body already uses the objects (`C01:243` cadastral row: "who holds which parcel, and what is owed?"; `C01:185` parcel boundary vs pacing error; `C02:64` groma→parcels). The row is what makes the use a **coupling** rather than an absorption.

### 6.4 U2 — trade-economy row (P1)

```markdown
| `culture-material/trade-economy-lexicon.md` | measures and their sacred standardization — the four sources (body, substance, action, container) at `:3,:17`; guild and contract vocabulary (`:106-116`) | the **scale bar's declared unit** and the map as a legal/territorial instrument. Metrology, measure standardization and contract grammar stay there |
```

### 6.5 U3 — celestial row (P1)

```markdown
| `myth-symbol/celestial-symbolism-calendars.md` | constellations and asterisms, planet-as-god identities, eclipse omen systems, the sky-as-calendar machinery (`:3`) | the **star chart as a produced document** — observation, projection, print. The sky typology and calendar mechanics stay there; the chart is one output of the sky, not the sky |
```

### 6.6 U4 — timekeeping row (P2)

```markdown
| `culture-material/timekeeping-instruments.md` | the five instrument families as **time** devices, incl. gnomon, sundial and astrolabe (`:3`, `:24-27`); "longitude at sea" (`:50`) | the same instruments used as the **position/angle chain** (theodolite, plane table, cross-staff, compass) and the sheet they produce. The instrument families, resolutions and time institutions stay there |
```

### 6.7 R1 — craft: cite the ladder, do not restate it

`C02:248` currently:

> The trade's internal ladder is the standard one: apprentice → journeyman → master, with a masterpiece and a feast, and with the usual escape hatches (masters' sons, redemption fees) … (`craft-artisan-lexicon.md:44`; the guild ladder is at `:3`, …)

Replace with a citation-and-delta sentence:

```markdown
The trade's rungs are the partition's standard workshop ladder (`culture-material/craft-artisan-lexicon.md:54-65`), cited here, not restated. The map trade's specific twist is that **the surveyor and the engraver are different hands**, so the "author" is often a brand — the publisher's imprint, the cosmographer's name, the crown's privilege. The mark types (`:76-87`) supply the signature vocabulary; the guild models (`:106-116` of `trade-economy-lexicon.md`) stay there.
```

And correct the audit row `C02:421`: `craft-artisan-lexicon.md:44` is the **Steel (Japan) material-grading row** (`| Steel (Japan) | **tamahagane** …`), not the ladder; the ladder header is `:54`, the systems `:56-63`, the design rule `:65`. That is exactly R03 B4, independently reconfirmed here with `sed -n '44p;54p;65p'`.

### 6.8 Optional rows (P2/P3, one surface)

```markdown
| `myth-symbol/sacred-kingship-mythic-charter.md` | the mythic charter and royal register (`:3`) | the **legal charter** — the document that legitimates a claim to ground; the two charters' disagreement is a plot engine |
| `civilizations/polynesia-navigation.md` | wayfinding practice — horizon compass, steering-star sequence, sky mnemonic, landfall (`:52`); explicitly "not a chart" (`:60`) | the drawn chart as one possible output of wayfinding; navigation practice stays there |
```

Divination needs **no row**; if the integrator wants the negative check visible, use one sentence, not a table row: "Divination (`divination-omen-systems.md`) owns the sign-reading technology; a map used as a divination instrument is a reading, not map production."

---

## 7. The boundary contract for the r48 redraft (six pass/fail conditions)

A right-sized entry does not need 19 rows; it needs **every neighbour it actually touches**. Apply:

1. **Surface completeness** — every neighbour named anywhere in the body appears on the single authoritative table. Body-only dispositions (today: sacred-kingship at `C02:300`, polynesia at `C02:73`, timekeeping at `C02:72`) must be promoted or deleted.
2. **Verified anchor** — every row's `file:line` resolves to the described content at the landing HEAD; no row cites a topic line as if it were a table (the `:44`/`:3` failure).
3. **Ownership sentence** — the row says what the neighbour owns in the neighbour's own terms, not in the draft's.
4. **Take sentence** — the row says exactly what this entry takes; the take must be narrower than the neighbour's topic-line claim.
5. **Non-restatement** — the row's "must not restate" clause is true of the body. Today it is not true for craft (§6.7).
6. **Shared-object split** — every shared object is explicitly split: cadastral **plan/grid** (architecture) vs **parcel/claim** (agrarian) vs **drawn register** (cartography); **measure** (trade-economy) vs **scale** (cartography); **astrolabe/gnomon as time** (timekeeping) vs **as position chain** (cartography); **sky** (celestial) vs **star chart** (cartography); **workshop ladder** (craft) vs **map-trade roles** (cartography); **compass rose** (cartography — direction explicitly excludes it at `:26`); **itinerary text** (sacred topography) vs **itinerary map** (cartography).

If all six hold, the boundary audit is PASS and the entry can carry claim C's `after_required` ("audits PASS") without a second owner.

---

## 8. What I verified, and what I did not

**Verified by command this seat** (all at `a01405d`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- Census 223 / culture-material 25; 0 filename owners; 0 narrow topic owners.
- Demand: broad pattern 29 files / 35 lines; cartographic-specific 5 files / 9 lines; per-file counts listed in §2.
- 35 anchors across 18 files, re-read: `cosmology-cosmography.md:27,71,102,133`; `sacred-topography-pilgrimage.md:5,69`; `direction-symbolism.md:26,51`; `architecture-settlement-lexicon.md:95`; `agrarian-field-system-lexicon.md:4,42,114`; `writing-media-surface-economy.md:3,81`; `mesoamerica-primary-sources.md:58`; `transport-mobility-lexicon.md:28,117`; `naming-systems.md:70`; `craft-artisan-lexicon.md:44,54,65,76,87`; `trade-economy-lexicon.md:3,17`; `celestial-symbolism-calendars.md:3`; `divination-omen-systems.md:3,147-152`; `timekeeping-instruments.md:3,50`; `polynesia-navigation.md:52,60`; `material-culture-inference-method.md:69`; `japan-medieval-sengoku.md:157`; `symbolism-synthesis-method.md:23`.
- File presence for all five register owners plus `linguistics/numerals-and-measures.md`.
- The K01 spec's 13 rows and C15's F1 convergence, read at `reports/round-48/scout/K01-rightsized-spec.md:215-229` and `reports/round-48/cov/C15-neighbors.md` (§4.3); every K01 line reference in this file was re-grepped against the spec after a first transcription error (architecture `:223`, craft `:226`, trade `:227`, divination `:222`).

**Not verified / out of seat scope:**

- **The r48 C01 entry body** — none existed at my read cut. If a later draft changes the boundary surface, the row-level verdicts here apply to the r47 bytes; the six-condition contract in §7 and the K01/C15 reconciliation in §4.3 are the reusable parts.
- External cartographic literature — no network at seat time; every Tier B item stays `to-verify`.
- Depth, length and arithmetic outside the boundary surface — C03/C05/R03 own those; I recomputed only the demand counts in §2 because they are the boundary evidence.
- Whether the integrator lands the C entry at all — claim C may be honestly stopped; my verdict constrains the draft, it does not authorize a landing.

## 9. Write surface

This file only — `reports/round-48/cov/C07-boundary.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged; no corpus entry was drafted under `corpus/`. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed. `git status --porcelain` at my write cut showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.

**Axis verdict for this seat:** coverage **not yet +1** — the boundary surface currently over-claims the cadastral plan and under-couples the parcel owner; with §6.1–§6.7 applied, no axis is harmed and the boundary claim is defensible.
