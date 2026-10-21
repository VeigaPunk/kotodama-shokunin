# ReviewSec12 — attack on §12 "NON-CANON worked micro-example" (claim C, round 50)

**Item attacked:** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` §12 (lines 167–172) of the landed round-50 work — *does the worked micro-example apply §11 faithfully, and does it stay clearly non-canon?*
**Landed commit:** `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
**Method:** landed bytes read with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4:…` (never the working tree); every `path:line` anchor opened at the same commit; S-id checked against the landed `corpus/SOURCES.md` row (no URL re-opened — other seats own that). No tools installed (none needed; nothing beyond `git`, `sed`, `grep`).

**Verdict: PARTIAL.**
The non-canon hygiene of §12 **HOLDS** (banner, invented-content declaration, no canon claim, explicit handoff of the stage-ladder refutation to §11's R row). The **application of §11 is PARTIAL**: all eight steps are *named* in the right order, but three step-level decision contents are never exercised (step 2 labour, step 5 herd ceiling by labour and disease, step 8 the taboo half of the taboo+rite pair), step 1's water/dung/fuel is not exercised, and one sentence of the example contradicts another.

---

## Findings (severity order)

### F1 — MEDIUM/HIGH — §12's ritual step writes a rite with no taboo, breaking §11 step 8 and the anchor §11 itself cites

- `pastoralism-animal-husbandry.md:158` — §11 step 8: `| 8 | Ritual | each taboo written with its rite | §10; symbolism-synthesis-method.md:69 |`
- `pastoralism-animal-husbandry.md:171` — §12's ritual element: `ritual — the first lamb of the pass is counted aloud before the herd moves.` There is **no taboo** anywhere in the example: no animal that may not be killed, no forbidden season, no restricted act.
- The anchor §11 step 8 points at is explicit: `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:69` — "**Prey apologetics**: a hunting culture that keys a prey animal symbolically generates apology and release rites for the kill … An animal taboo implies a rite; **write both or neither**." A rite written alone is the "neither" case.
- The entry's own §10 carries the same rule: `pastoralism-animal-husbandry.md:142` — `| Sacrifice economy | offerings drawn from the herd's surplus males | an animal taboo implies a rite (symbolism-synthesis-method.md:69) |`.
- House style shows the fix: the sibling worked example in the same lane writes the taboo half explicitly — `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:174` — "**Taboo boundary:** the drent's true name is spoken only at the weir (forest register handed to `taboo-strata-lifecycle.md`); the grove's nut-trees are sacred-owned".
- As written, §12 exercises §10 row 1 (`pastoralism-animal-husbandry.md:139`, "Herd accounting as poetry", S064) rather than the step-8 decision content, so the one step whose check is a *rule* rather than a cross-reference is the one left unfulfilled.
- **Smallest fix (one clause):** make the first-lamb rite taboo-bound, e.g. `ritual — the first lamb of the pass is never killed before the count; the count is spoken aloud and the lamb is marked instead, then the herd moves.`

### F2 — MEDIUM/HIGH — §12's species and wealth steps omit the labour the entry's own tests demand

- `:152` — §11 step 2: `| 2 | Species | two to four species and their shares (S048) | each species row has forage and labour (§4) |` → §12 (`:171`) gives `species — sheep and goats for wool and cheese, yaks only above the tree line`: **products for two species, a forage line for one species, and no labour for any species**. The step-2 *Check* cell is therefore unmet for all three species (and the forage half unmet for sheep/goats).
- `:155` — §11 step 5: `| 5 | Wealth | herd ceiling set by labour and disease; loan and gift networks | §7; S049 |` → §12 gives only `wealth — lambs lent between lineages after a hard winter`. **No herd ceiling, no labour bound, no disease, no gift network** (only the loan half of "loan and gift networks").
- This is the entry's load-bearing claim: `:22` — `| **Labour-capped herd** | household labour, not pasture alone, sets the herd a family can hold (S049) |` — and S049's grounded content in `corpus/SOURCES.md:78` is "herd wealth tracks household labour". The worked example that is supposed to demonstrate the method never demonstrates the entry's headline test.
- Sibling comparison: `hunting-foraging-subsistence.md:174` carries an explicit `Labour:` element ("both sexes weir and gather; the winter deer drive is men's by rule … a deliberate §7 choice inside the contested range") mapped onto its build-order step 5 (`hunting-foraging-subsistence.md:154`).
- **Smallest fix (one clause each):** `species — sheep and goats for wool and cheese, yaks only above the tree line; each household herds at most N sheep, the ceiling set by the two who can milk and move the flock` and `wealth — lambs lent between lineages after a hard winter; a sick year is the ceiling, not a good one` (adds disease and the labour bound).

### F3 — MEDIUM — §12's ecology step never ties water, dung or fuel in, and drops one of §8's three move-claims

- `:151` — §11 step 1: `| 1 | Ecology | rainfall, forage patchiness, water points | dung, fuel and water tied in (fire-fuel-light.md:37) |` → §12 gives `ecology — a dry valley and wet high meadows`. No **water point**, no **dung**, no **fuel**; the step-1 *Check* cell and the anchor `corpus/knowledge/culture-material/fire-fuel-light.md:37` (the dried-dung row: "a real trade-off against manure; fuel-poor pastoral cultures pay for it in soil") are both left unexercised.
- The same omission breaks the entry's own §8 opening claim at `:110` — "A herd move claims three things: a route, a water point and a pasture." §12's move claims a route (the western pass) and a pasture (the high meadows) but never a water point, so the example does not exercise the proposition it is meant to demonstrate.
- **Smallest fix:** `ecology — a dry valley with one reliable spring and wet high meadows; the herds' dung is dried for fuel, taken from the valley pens` (adds the water point and the dung/fuel answer in one clause).

### F4 — MEDIUM — internal contradiction inside the example: yaks "only above the tree line" but wintering in valley pens

- `:171` — `The **Ketrun** keep sheep, goats and a few yaks on a vertical round: valley pens in winter, …` and, in the same line, `species — … yaks only above the tree line`.
- The yaks are part of the wintering herd (`valley pens in winter`) and the species rule confines them above the tree line; the two cannot both hold if the valley is below the tree line (the example's own "tree line" reference presupposes that).
- The entry's own §4 row is **season-scoped** and does not support the absolute: `:63` — `| Yak | high plateau; summer herds "on pastures at high elevations" (S061) | …` (S061's grounded text, `corpus/SOURCES.md:90`: "warm-season high pastures and campsites; butter as the main milk product; dung as fuel").
- **Smallest fix:** `yaks only above the tree line in summer` (or `the yaks winter in a high side-valley`).

### F5 — LOW — §12's lexicon step exercises 1 of the 5 dimensions §11 step 6 names, and borrows the Nuer naming row without the "like, not as" marker

- `:156` — §11 step 6: `| 6 | Lexicon | age, sex, colour, condition, mark terms from rows 2–5 | §5; semantic-fields-lexicon-building.md:105 |` → §12 gives only `lexicon — sheep named by fleece colour and its placement`. **Age × sex, condition and ownership-mark terms are absent** (they are three of the five rows in §5, `:75`–`:79`).
- The colour × placement pattern is the Nuer row verbatim in mechanics: `:75` — `| Colour × distribution | Nuer cow names follow "its colours and the way in which they are distributed on its body" (S052, ch. I §VIII) |`. §12 uses it with no attribution, and §13's living-practice flag (`:189`) names Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding — **the Nuer are not in that list**, so the borrow is not covered by the entry's own "write fictional herds *like* these mechanics, never *as* these peoples" rule.
- **Smallest fix (either):** extend §12's lexicon clause to `sheep named by fleece colour and its placement, a mechanic borrowed from the Nuer pattern (S052) and not a claim about any people`; and/or add the Nuer to the `:189` living-practice flag list.

### F6 — LOW — §12's relations step shows only the "licence" half of §9's trade-under-pressure row and answers neither of §9's design questions

- `:157` — §11 step 7: `| 7 | Relations | the sedentary neighbour, its power and the exchange form | §9; S056 |` → §12 gives `relations — cheese and wool traded down-valley for grain at a market the farmers license`.
- `:127` (§9) requires both halves: `| Trade under pressure | the sedentary state licenses markets; nomads force them open (S056) | the licence and its price are the plot |`. §12 shows the licence and **no nomad pressure**, and no **price**.
- `:126` (§9) asks the design question the example leaves unanswered: `| Interdependence | livestock, wool, hides out; grain, metal, crafts in | who carries the goods and sets the price? |`.
- S056's row (`corpus/SOURCES.md:85`) grounds all three of "nomads always needed external grain and crafts; sedentary states used trade as political pressure; tribute and gifts from dependent sedentary populations" — §12 uses one third of it and does not cite it (the only S-id in §12 is S055; see "What holds" below).
- **Smallest fix:** `relations — cheese and wool traded down-valley for grain at a market the farmers license, and the Ketrun hold the pass until the toll is cut; the farmers set the price and the Ketrun carry the wool down`.

### F7 — LOW — the mobility label is left unverifiable: "who travels" is the discriminator between §3's transhumant and semi-nomadic rows, and §12 does not say

- `:171` — `mobility — transhumant with herd splitting (the yaks summer apart)`.
- `:49` (§3, transhumant) — `| Transhumant | seasonal movement of people with their livestock; … | two bases; the route is infrastructure | a herd party travels, households stay; herd splitting (S048) | route access is the exposure |`; `:48` (§3, semi-nomadic) — `| Semi-nomadic | part of household travels; a base is held | village or winter camp plus satellite camps | … |`.
- §12 describes a **held winter base** (valley pens) and a seasonal round, i.e. the semi-nomadic signature, while labelling itself transhumant; without stating who moves, the label cannot be checked against either row, and §3's opening instruction (`:43`) is that the rows are "dials inside one economy, never a ladder".
- **Smallest fix:** `mobility — transhumant with herd splitting (the yaks summer apart): the families stay in the valley pens, a herd party takes the flock up`.

---

## What holds (checked, no defect found)

- **Non-canon hygiene: HOLDS.** `:169` — "**NON-CANON.** The people, valley, flocks and numbers below are invented to demonstrate the method; canon belongs to lore-shokunin." The example decides nothing about any world (QUALITY criterion 5): it names no real people, asserts no world fact, and closes by refusing the ladder reading (`:171` "The Ketrun are a different economy from the valley farmers, not an earlier stage of them"), which is the correct, R-coded rebuttal. The banner form matches the lane's house style (`hunting-foraging-subsistence.md:172`, `cartography-and-mapmaking.md:191`).
- **Step order: HOLDS.** §12's inline list `ecology → species → mobility → tenure → wealth → lexicon → relations → ritual` matches §11's steps 1–8 in order, with no step skipped and no step invented.
- **S055 attribution: HOLDS.** The only S-id in §12 is `(Ostrom-style, S055)`; the landed row (`corpus/SOURCES.md:84`, tier A, scope "Ostrom's own 2009 formulation of the design principles … not the 1990 book's wording", anchor "§4E Long-Surviving Resource Institutions, PDF p. 15") covers a *style* attribution for an invented institution, and the entry already derives "rotas, fines, monitors and nested authority as in-world institutions" from the same row at `:115` with the status named ("mainstream as diagnosis; C as a predictive law") — so QUALITY criteria 2 and 6 are satisfied and no in-place tier edit is implied. The example makes no predictive claim about Ostrom's principles.
- **No fabricated or laundered source in §12.** Zero `path:line` anchors and zero `(to-verify)` markers in §12 — appropriate, because every sentence in it is declared-invented, and there is nothing in it that asserts an unverified fact. (The entry as a whole carries 11 `(to-verify)` markers on the claims that do need them.)
- **§11's own anchors verified at 1c779e4 (for the steps §12 invokes):** `myth-symbol/symbolism-synthesis-method.md:69` (taboo ⇒ rite, "write both or neither" — the rule F1 trips), `culture-material/fire-fuel-light.md:37` (dung-as-fuel row — the anchor F3 leaves unexercised), `linguistics/semantic-fields-lexicon-building.md:105` (steppe pastoral field: "subsistence (herd wealth), kin (clan), war (raid), landscape (pasture)" — supports §11 step 6's check), `verification/calibration-registry.md:35-39` (the R/C/B/H/T codes used in `:175` and `:162`) and `verification/calibration-registry.md:142` (stage → social stage is R — supports the closing sentence of §12).
- **Line-anchors still resolve at the landed commit.** `git diff --stat 4ad2683 1c779e4` shows the only `corpus/knowledge` change is the new entry itself, so no cited `path:line` in §11's Check column shifted between the base the entry was written against and the landed commit.

## Residual risk and verification gaps

- **URLs not re-opened** (per the seat split): F4's reading of S061's scope, F5's reading of S052, and F6's reading of S056 rest on the landed `corpus/SOURCES.md` rows and the round-50 Gate quotes in `corpus/lessons/round-50.md`, not on a fresh fetch. If a URL re-open shows S061 is not warm-season-scoped, F4's severity drops to LOW (the internal contradiction in `:171` stands either way).
- **Not in this seat's scope:** the §1–§11 bodies, the header block, the README row and the `SOURCES.md` used-by column are covered by the sibling seats; the §12 findings above are stated as findings *of §12*, and several of them (F1, F2, F3) are evidence that §11's decision cells are not being met by the example that is supposed to demonstrate them.
- **Two possible reads of F1/F2, and why the stricter one is used:** a "micro-example" can legitimately show less than the full method. That defence does not rescue F1 (the rule is a "both or neither" pair, and the sibling entry writes the taboo) and it does not rescue F2 (the omitted element — labour — is the entry's own headline test at `:22` and its S049-grounded claim; the sibling entry writes a `Labour:` element). F3/F5/F6 are graded LOW because they are coverage gaps in a worked example, not contradictions.
- **No `(to-verify)` is required for anything in §12** as written; the fixes proposed above are design clauses, not factual claims, so they must not be turned into citations.

## Recommendation

Admit §12 with the six fixes above (F1 and F2 are the ones that would change a reader's worldbuilding; F3–F7 are one-clause each). The non-canon framing and the S055 citation need no change. This is author-lane advice, not admission.
