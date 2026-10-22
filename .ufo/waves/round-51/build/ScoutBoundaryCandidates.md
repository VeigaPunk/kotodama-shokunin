# ScoutBoundaryCandidates — claim D, §2 neighbour candidates

Seat: `KotodamaR51a3.ScoutBoundaryCandidates` (leaf scout, read-only, no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at `1f97472` ("round-51: attempt 3 declaration"); the entry's
bytes equal base `bff83ba` — `git status --porcelain` shows only `?? .ufo/waves/round-51/`, and the §2 table still has
11 data rows. All corpus facts below were re-read in this session from the lane worktree. No lane file was written
except this report. **Tooling: nothing installed** (no pacman, no uv/npx; nothing was needed).

## 1. The 11 current neighbours (entry §2, lines 27–41)

| # | first-cell anchor | neighbour |
|---|---|---|
| 1 | `agrarian-field-system-lexicon.md:56,:62` | culture-material/agrarian-field-system-lexicon.md |
| 2 | `hunting-foraging-subsistence.md:36,:116` | culture-material/hunting-foraging-subsistence.md |
| 3 | `cuisine-food-lexicon.md:67,:81,:152` | culture-material/cuisine-food-lexicon.md |
| 4 | `transport-mobility-lexicon.md:92,:95` | culture-material/transport-mobility-lexicon.md |
| 5 | `trade-economy-lexicon.md:69` | culture-material/trade-economy-lexicon.md |
| 6 | `textile-technology.md:22,:27` | culture-material/textile-technology.md |
| 7 | `semantic-fields-lexicon-building.md:70,:105` | linguistics/semantic-fields-lexicon-building.md |
| 8 | `fire-fuel-light.md:37` | culture-material/fire-fuel-light.md |
| 9 | `animal-symbolism.md:73,:110` | myth-symbol/animal-symbolism.md |
| 10 | `sacred-kingship-mythic-charter.md:65` | myth-symbol/sacred-kingship-mythic-charter.md |
| 11 | `civilizations/` (directory token, no line anchor) | civilizations/* regional entries (Mongol, Turkic, Scythian, Sámi, Diné, Inca) |

Head line 8 already declares `myth-symbol/ritual-liminality.md` as a couple and line 6 already lists
`symbolism-synthesis-method.md:69`, `ritual-liminality.md:63`, `celestial-symbolism-calendars.md:28` and
`calibration-registry.md:35-39,:142` as in-corpus anchors — none of the four has a §2 row today. That is the gap the
four new rows close.

## 2. Enumeration: other corpus/knowledge files with herding lines

Pattern used (word-bounded, case-insensitive, `corpus/knowledge/` root):

```
grep -rniP --include='*.md' -c '\b(herd(ing|er|ers|s)?|livestock|flock|shepherd|shepherding|cattle|sheep|goat|horse|camel|reindeer|yak|milking|milk|wool|dairy|nomad\w*|transhuman\w*|pastoral\w*|ranch\w*|graz\w*|pasture\w*|drover|droving|bridewealth)\b' corpus/knowledge/
```

104 files match; minus the 10 file-named neighbours above = **94 candidate files: 46 outside `civilizations/`, 48 under `civilizations/`**.

Outside `civilizations/` (hits in brackets) — culture-material: dress-through-eras (10), furniture-interior-lexicon (4),
warrior-material-culture (3), ritual-garments (3), costume-semiotics (2), architecture-settlement-lexicon (2),
music-instrument-lexicon (2), adornment-body-codes (2), funerary-material-culture (2), writing-media-surface-economy (2),
calendar-festival-systems (1), material-culture-inference-method (1), vessel-container-lexicon (1),
timekeeping-instruments (1); linguistics: semantics-pragmatics (3), color-terminology (3), numerals-and-measures (2),
phonetics-phonology (1), historical-linguistics (1), politeness-taboo-euphemism (1), language-contact (1),
naming-systems (1), orality-formulaic-language (1), dialect-register-consistency (1);
myth-symbol: celestial-symbolism-calendars (6), ritual-liminality (4), hero-journey-variants (3), color-symbolism (2),
purity-pollution-boundary-systems (2), symbolism-synthesis-method (1), myth-ritual-theories (1), trickster (1),
direction-symbolism (1), plant-symbolism (1); synthesis: coupling-model (10), era-myth-language-costume-matrix (8),
costume-language-coupling-table (6), worked-example-mini-culture (3), multi-culture-creole-workshop (3),
source-discipline-calibration (3), urban-rural-register-ecology (1), migration-founder-effects (1),
conlang-blueprint-template (1); verification: myth-consistency-gate (2), costume-era-consistency-gate (2),
gate-frozen-run-standard (1).

The 48 `civilizations/*` files are **not eligible** as new rows: row 11 already names "Mongol, Turkic, Scythian, Sámi,
Diné, Inca cases and their warnings" and owns the regional cases as a class, so a specific `civilizations/mongol.md`
row would restate row 11 even though the counter would accept it as a distinct target.

Pattern note (calibration): a looser `camp\w*|tent\w*` probe is a trap — `\bcamp\w*\b` matches "campaign" and
`\btent\w*\b` matches "tentative", which produced false 9–15-hit files (`amazigh-berber.md`, `comparative-frameworks.md`,
`era-language-staging.md`, `loanword-material-dating.md`, `lexicon-coverage-audit.md`). Direct line reads show those
files carry no herding line at all. `verification/calibration-registry.md` also carries "steppe" only at `:7`, `:13`,
`:109` — its candidacy rests on the status vocabulary, not on a pastoral word.

## 3. Ranked candidates

Contract seed: `ReviewEntryContract.md` §4 (lines 208–241) lists 23 candidates. Seven are table rows today
(hunting, agrarian, transport, fire-fuel, semantic-fields, animal-symbolism, sacred-kingship) and the `civilizations/`
row absorbs six more (turkic-steppe, mongol, scythian-saka, finnic-sami, dine-navajo, inca). **Ten of the 23 have no
row**: writing-media-surface-economy, ritual-garments, music-instrument-lexicon, calendar-festival-systems,
hero-journey-variants, celestial-symbolism-calendars, source-discipline-calibration, coupling-model,
costume-era-consistency-gate, calibration-registry — four of which are ranked below.

Ranked by (a) the anchored line supporting a real ownership cell, (b) the boundary already developed or explicitly
narrowed in the entry body (claim D's own requirement), (c) precedent in a sibling boundary table.

### 1. `verification/calibration-registry.md:35-39,:142` — recommended

* Anchored lines, verbatim: `:35` "| R | Rejected/discredited as the specified general inference | Do not use as evidence …";
  `:36` C; `:37` B "Bounded, usable within a named domain"; `:38` H "Heuristic or interpretive framework, not an established
  causal law"; `:39` T "Unresolved provenance or claim check | Mark `(to-verify)` inline at the exact dependency";
  `:142` "| Stone–Bronze–Iron, dynastic decline or subsistence predicts a total social stage — R | …".
* Owns (`:3`): "Master claim-level calibration registry for the linguistic-cultural corpus"; it defines the code vocabulary.
* This entry keeps: the code **assignment** to pastoral claims and the inline `(to-verify)` marking; the definitions stay.
* Body already touches it, three times: `:180` (§13 opener) "Codes per `calibration-registry.md:35-39` (R rejected, C
  contested, B bounded, H heuristic, T to-verify)"; `:167` and `:184` (§11/§13 error rows cite `:142`); also `:47` (§3)
  cites `:35-39`. Not in the table, not in the `couples:` line — the only ranked candidate no visible scribe seat covers.

### 2. `myth-symbol/ritual-liminality.md:63` — recommended

* Anchored line: "| calendrical / maintenance | feed the machine that keeps time | Aztec veintena rites … Vedic agnihotra
  daily milk oblation; aśvamedha year-long royal horse rite … | the calendar-owning priesthood's budget |".
* Owns (`:3`): the rite toolkits (van Gennep's grammar, Turner's liminality, the rite-class typology).
* Keeps: the herd ledger that feeds the rite; the rite class and its budget stay there.
* Body already narrows it at `:140` (§10 opener): "write the rite from the herd's books outward (`ritual-liminality.md:63`)";
  head `couples:` line 8 also names it.

### 3. `myth-symbol/celestial-symbolism-calendars.md:28` — recommended

* Anchored line: "(2) **subsistence** — farmers anchor on heliacal risings, sailors on star paths, pastoralists on
  milky/river figures".
* Owns (`:3`): the naked-eye sky as symbolic system — sun/moon gender, planet-as-god chains, constellations, Milky Way.
* Keeps: the subsistence input only; the sky figure, its etiology and its calendar stay there.
* Body already narrows it at `:148` (§10 "Sky figures" row): "a subsistence input to sky lore, not a creed". Sibling
  precedent: `hunting-foraging-subsistence.md` §2 cites the same file at `:28,:118`.

### 4. `myth-symbol/symbolism-synthesis-method.md:69` — recommended

* Anchored line: "**Prey apologetics**: a hunting culture that keys a prey animal symbolically generates apology and
  release rites for the kill … An animal taboo implies a rite; write both or neither."
* Owns (`:3`): the substrate-first symbolic-grammar method across the five registers; the taboo→rite rule.
* Keeps: the offering drawn from the herd's surplus males; the synthesis method and sacrifice typology stay there.
* Body already uses it twice: `:147` (§10 "Sacrifice economy" row) and `:163` (§11 step 8). Sibling precedent: hunting §2
  cites it at `:47,:69`.

### 5. `linguistics/kinship-terminology.md:49,:63` — strong alternate

* Anchored lines: `:49` "| Eskimo | bilateral kindred, no unilineal groups; neolocal residence … | family isolates …";
  `:63` "Goody (1983): the European shift toward Eskimo-type terms tracks the **Church's prohibited-degrees marriage law**
  … law, not subsistence, moved the lexicon."
* Note: this file is **outside the §2 enumeration** — it has 0 hits for the herding word pattern (verified by direct
  line grep). Its candidacy rests on the entry's own §7 descent coupling (`:105`) and on the hunting sibling's identical
  row, not on a pastoral keyword.
* Owns (`:3`): Murdock's six terminology types and what each encodes "weakly" about descent, residence and marriage.
* Keeps: descent as a herd-transfer input; the kin terms and their merging fingerprints stay there.
* Body already touches the boundary at `:105` (§7 bridewealth row): "descent and herd size set the scale `(to-verify)` per
  culture". Sibling precedent: hunting §2 has exactly this row (`:49,:63`, "kin/economy couplings, Goody caution").

### 6. `culture-material/architecture-settlement-lexicon.md:33` — strong alternate

* Anchored line: "**Mongolian ger**: **khana** lattice walls, **uni** roof poles, **toono** crown ring (smoke hole = the
  sky opening directly above the hearth), **bagana** doorposts, door to the south; the dwelling is a portable cosm…".
* Owns (`:2`): built-environment vocabulary — houses, roofs, thresholds, cities and the naming logic of house parts.
* Keeps: the herd's mobility cycle and the camp's placement; the dwelling and its part-names stay there.
* Body already touches it at `:51` (§3 Nomadic row): "portable dwelling — the ger is 'light enough for nomads to carry'
  (S062, Mongolia)". Do **not** anchor this row on `:63` ("grain in a kura? cattle under the floor?") — that is a passing
  mention inside Rapoport's argument, not an ownership line.

### 7. `culture-material/vessel-container-lexicon.md:35,:110` — strong alternate

* Anchored lines: `:35` "| TRANSPORT | survive the road; shaped for stacking, tying, carrying; often standardised so it
  can be counted | … skin bag, waterskin; *masu* box; barrel/cask …"; `:110` "| Skin and textile | waterskin, leather
  bottle, sacks, bales, net bags | couples to textile-technology.md …".
* Owns (`:3`): the container as a cultural system — the COOKING/STORAGE/TRANSPORT/SERVING jobs and the six naming strategies.
* Keeps: the herd product and its season; the vessel, its job and its name stay there.
* Body already touches it at `:92` (§6 milk row): "dairy needs pails, a curd/butter chain and storage". Sibling precedent:
  hunting §2 cites the same file at `:126` ("vessels, pottery/sedentism calibration").

### 8. `culture-material/writing-media-surface-economy.md:47,:138`

* Anchored lines: `:47` "the animal or the marsh — parchment consumes a herd over years, papyrus consumes a harvest";
  `:138` "| parchment | the scriptorium: herd, lime pits, frames, copying room | herd years ahead of text demand …".
* Owns (`:3`): the surface economy of inscription (the seven surface families and their prices).
* Keeps: hide as a herd product and its supply lead time; the surface, its preparation and its cost stay there.
* Body touches the product without citing it: `:88` (§6 row) "| Meat, hide, bone, blood | the dead animal (one harvest) |".
  Listed in the round-50 build contract §4 as a candidate; no body citation yet, so a row here needs a §6 sentence.

### Named, not ranked (9–12)

`culture-material/ritual-garments.md:80` (pallium "woven from lambs blessed on the feast of St Agnes … the office is
annually *re-manufactured out of livestock and calendar*" — contract §4 candidate, no body touch);
`culture-material/calendar-festival-systems.md:79,:121` (`:79` "poetic month names keyed to season and husbandry";
`:121` "1 Elul for cattle tithes" — real anchors, but the agrarian row already owns the agropastoral calendar);
`myth-symbol/hero-journey-variants.md:110` ("steppe/pastoral → inherited slaying-formula and cattle-raid quests");
`linguistics/semantics-pragmatics.md:13,:22` ("Lexical elaboration = many near-synonyms on one dimension (rice
terminologies, herd vocabularies)" — the entry's `:5` rule "write 'a very large set', never a number" states the same
rule uncited); `synthesis/coupling-model.md:150` ("imported wool does not require local sheep husbandry");
`verification/costume-era-consistency-gate.md:65` (MAT-02 "Show cultivation/herding/collection **or** an external
supplier"); `culture-material/adornment-body-codes.md:21` (jewellery as bridewealth capital — overlaps §7's bridewealth row).

### Filler flags (a herding word appears, but no boundary to draw)

dress-through-eras (wool as a costume material, 10 hits), furniture-interior-lexicon:81 (chest "of the poor and the
nomad"), costume-semiotics:125, purity-pollution-boundary-systems:34,:57 (the wool-linen ban and milk-meat separation are
already routed to the cuisine and animal-symbolism rows), warrior-material-culture:33,:61 ("linen/flock supply"; horse
insignia), funerary-material-culture:113 (black-wool mourning market), music-instrument-lexicon:87 (Jabal "tents/livestock"
inside a genealogy cell — marginal), timekeeping-instruments:5 and material-culture-inference-method:13 (bibliography
lines), naming-systems:84 (a steppe state as a place name), color-symbolism:62, color-terminology:63,
celestial-symbolism-calendars:104 (horse-eyesight), ritual-liminality:37 (milk as a sensory pole in a Turner summary),
myth-consistency-gate:150, and every `synthesis/` file whose hits sit inside an invented worked example
(era-myth-language-costume-matrix, costume-language-coupling-table, multi-culture-creole-workshop, worked-example-mini-culture,
urban-rural-register-ecology:129, migration-founder-effects:149).

## 4. Counter dry run (simulated, no lane write)

Loaded the real counter as a module (`importlib` from `reports/round-51/boundary-count.py`), used its own
`knowledge_index`, `SECTION`, `TOKEN` and `resolve` against the lane's real bytes, and appended the four recommended rows
to the 11 extracted §2 rows **in memory** (entry file untouched):

```
section rows now: 11 | after 4 new: 15
SIMULATED: rows=15 resolved=15 distinct=15 -> exit 0
already-in-table collisions: []
```

Every one of the four anchors resolves to a distinct file; none collides with a target already in the table; `:35-39` and
`:142` are inside `calibration-registry.md` (190 lines), `:63` inside `ritual-liminality.md` (136), `:28` inside
`celestial-symbolism-calendars.md` (175), `:69` inside `symbolism-synthesis-method.md` (172). The four rows name no
`S071+` id and no path from claim C.

Two counter facts the executor should keep in mind: the counter reads **only the first cell** of each row
(`row.split("|")[1]`) and counts rows up to the next `## ` heading; and it accepts a bare `file.md` token with no line
number (its regex makes the `:line` group optional), so resolution alone will not police the claim — a reviewer will.
The current table puts anchors in the first cell; the hunting sibling instead puts bare paths in the first cell and
anchors in the middle cell (`hunting-foraging-subsistence.md:47-67`, 20 data rows). Keep the pastoralism layout.

## 5. Result and unrun checks

* Delivered: the 11 current neighbours, the 94-file word-bounded enumeration (46 outside `civilizations/`), 8 ranked
  candidates with verbatim anchor lines, ownership, kept boundary and the body section/line that already touches it, plus
  filler flags.
* Recommended four for the 11 → 15 step: `verification/calibration-registry.md:35-39,:142`,
  `myth-symbol/ritual-liminality.md:63`, `myth-symbol/celestial-symbolism-calendars.md:28`,
  `myth-symbol/symbolism-synthesis-method.md:69` — all four boundaries are already developed or explicitly narrowed in the
  body (`:180`, `:140`, `:148`, `:147`/`:163`), so the four rows need no new body prose to satisfy claim D; alternates
  5–7 are equally resolvable if the L1 prefers a wider partition spread (one verification, three myth-symbol rows as
  ranked; swapping in kinship/architecture/vessel trades a myth-symbol row for culture-material or linguistics).
* Unrun: the counter itself was never executed on a tree containing the edit (scout seat, no sandbox clone, no lane
  write) — the §4 result is a simulation through the counter's own functions, not the CLI. No external URL was opened
  (this seat has no frontier-step duty). No `run-validation.py`, `sweep.py` or separability command was run. The
  round-50 `ReviewSec02.md` was read for the §2 review contract only; its findings F5 (no lead sentence, header drift
  `| Neighbour (anchor) |` vs the contract's `| Neighbour | What it owns (live anchor) |`, 9→15 rows) are still open at
  this base and are the L1's to route.
