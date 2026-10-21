# ReviewSec11 — attack on §11 (decision table, build order, error patterns) of the round-50 C entry

Seat: `KotodamaR50-2.ReviewSec11-21` (leaf, read-only). Round 50 falsify wave, lane `kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes were read from a private clone (`git clone -q --shared … /tmp/rev11-XXXX; git checkout -q 1c779e4a…`) or via
`git show 1c779e4a…:<path>`; the lane working tree was never read for a claim and never touched. No edits to lane files
except this report; no installs; no URL re-opening (URL seats own that).

Scope actually executed: every in-corpus `path:line` anchor in the entry was opened at the landed commit and checked
against the sentence that cites it; every S-id in the entry was checked against its `corpus/SOURCES.md` row's `scope` and
`teaches` fields (and against the filed Gate quote in `corpus/lessons/round-50.md`); §11's eight build steps, its four
error rows, and §4/§12's build-order cross-references were checked for internal consistency; QUALITY criteria 1–6 were
applied to §11 and its neighbours.

## Verdict: **PARTIAL**

The section's skeleton holds: §11's eight steps each resolve to a real section of the same entry, every S-id it cites
(S048, S049, S055, S056, S058) is supported by its row's `teaches` at the tier that row carries, and the four error rows
are correctly coded R under `verification/calibration-registry.md:35-39`. But the section does **not** hold as an
operational build order:

* **3 of the 8 steps carry a Check cell the cited anchor does not support** (steps 1, 5, 6) — step 6 cites the wrong
  line outright;
* **the build order has no products stage**, contradicting §4's own fix order and leaving §6 (and the S051 contest it
  carries) out of the workflow;
* **1 of the 4 error rows cites an anchor that supports a different error pattern**;
* and, one row over, the S051 quotation is presented as Sherratt's wording although the SOURCES row disclaims being
  primary for Sherratt (QUALITY criterion 6).

Everything below is anchored to `file:line` at the landed commit. Commands are reproducible from the private clone.

---

## Findings by severity

### MODERATE

#### M1 — §11 step 6 cites the wrong in-corpus line (`semantic-fields-lexicon-building.md:105`)

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:156`

```
| 6 | Lexicon | age, sex, colour, condition, mark terms from rows 2–5 | §5; `semantic-fields-lexicon-building.md:105` |
```

The step asks for "age, sex, colour, condition, mark terms". At the landed commit:

```
$ sed -n '105p' corpus/knowledge/linguistics/semantic-fields-lexicon-building.md
| steppe pastoral | subsistence (herd wealth), kin (clan), war (raid), landscape (pasture) | sea/coast terms (note the gap) |

$ sed -n '70p' corpus/knowledge/linguistics/semantic-fields-lexicon-building.md
- Pastoral wealth vocabulary (herd-age, herd-color, herd-condition terms) indexes property systems; …
```

`:105` is the *steppe field-bundle* row (a semantic-field inventory); it contains no herd-age/colour/condition vocabulary
at all. The vocabulary the step needs is at `:70` — which the entry itself already uses for exactly this purpose at
`:71` ("A herd vocabulary is a property index … (`semantic-fields-lexicon-building.md:70`)") and lists in the header
anchor list (`:70,:105`). So `:105` in step 6 is a copy of the header's `:105` for the *steppe bundle*, not a support for
the step's own "Decide" cell.

*Smallest fix:* in `:156`, replace `semantic-fields-lexicon-building.md:105` with `semantic-fields-lexicon-building.md:70`
(or `:70,:105` if the steppe bundle is also meant to be consulted).

#### M2 — §2's cuisine one-owner row mis-anchors two of its three claims

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:33`

```
| `cuisine-food-lexicon.md:67,:86` | yogurt lineages, milk+meat law, Harris's cattle economy (contested) | milking, churning and the dairy chain up to the product |
```

At the landed commit:

```
$ sed -n '67p' corpus/knowledge/culture-material/cuisine-food-lexicon.md
| Bacteria+lactobacilli | kimchi … yogurt lineages, idli/dosa batters | seasonal collective labor with a fermentation clock; buried-jar autumn events |     ← yogurt lineages ✓

$ sed -n '86p' corpus/knowledge/culture-material/cuisine-food-lexicon.md
- Three rival explanations of the taboo systems … Douglas (1966): the pig is a taxonomic anomaly …; Milgrom (1991) …; Harris (1985): cultural materialism — pigs compete with humans for food …   ← pig taboos, not a cattle economy

$ sed -n '81p' corpus/knowledge/culture-material/cuisine-food-lexicon.md
| Mixing rules | milk + meat separation (Ex 23:19 "kid in its mother's milk", ×3 in Torah); separate dishes; waiting times | no milk+meat law; wine and intoxicants forbidden (Quran 5:90) …   ← the milk+meat law lives HERE

$ sed -n '152p' corpus/knowledge/culture-material/cuisine-food-lexicon.md
- Harris's materialist taboos (pig economics, cow economics) — contested by culturalists; strongest case is the pig, weakest the cow. …   ← "Harris's cattle economy" lives HERE
```

Only "yogurt lineages" is supported by the cited pair. "milk+meat law" is at `:81` and "Harris's cattle economy" at
`:152` — neither is cited, and `:86` carries Harris for the *pig*, which is the opposite of a cattle economy. This is a
one-owner boundary row: its whole function is to point at the owner, so a wrong line hands the writer to the wrong cell.

*Smallest fix:* cite `cuisine-food-lexicon.md:67,:81,:152` in that row (and add `:81`/`:152` to the header anchor list at
`:6`), or drop "milk+meat law, Harris's cattle economy" from the "What it owns" cell.

#### M3 — the build order has no products stage and contradicts §4's fix order

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:67` vs `:149-158`, and `:171`

```
:67   Fix ecology → species → mobility → products → labour → symbol; a herd with no forage line fails §11 step 1.
:149  | # | Build step | Decide before moving on | Check |          ← §11's table
:158  | 8 | Ritual | each taboo written with its rite | §10; `symbolism-synthesis-method.md:69` |
```

```
$ sed -n '147,166p' …/pastoralism-animal-husbandry.md | grep -c '§6'
0
```

§4 prescribes a six-stage fix order that includes **products** (and labour, symbol). §11's eight steps are Ecology,
Species, Mobility, Tenure, Wealth, Lexicon, Relations, Ritual — **no products step**, and its Check column never
references §6. Consequences:

* §6 (products: meat/milk/fibre/traction/dung) is the entry's only place where the S051 secondary-products contest and
  the S061 "yak butter is the main milk product" live, and a worldbuilder following §11 never produces a product chain;
* §4's "products" stage has no corresponding build step, so the entry states two different build orders;
* the §12 worked example (`:171`) follows §11's eight stages and also skips products — "species — sheep and goats for
  wool and cheese" folds products into species, which is what makes the omission invisible rather than absent.

*Smallest fix:* add a step between 3 (Mobility) and 4 (Tenure) — "Products | milk/meat/fibre/traction/dung chain,
  storage, seasonality | §6; S051 for regional sequences" — and rewrite `:67`'s fix order to the §11 order (or make §4's
  order the single list and drop the duplicate).

#### M4 — the S051 quotation is presented as Sherratt's wording from a row that is explicitly not primary for Sherratt

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:93`

```
Sherratt's "secondary products revolution" — "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction" (S051) — is **C**: the review finds adoption regional and staged, not one horizon (S051).
```

The filed evidence for that string is the review's own abstract sentence, not Sherratt's:

* `corpus/lessons/round-50.md:36` — "- S051 — https://link.springer.com/article/… — accessed 2026-10-21 — **Abstract, opening sentence**: 'a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction'. Seat: SrcSherratt."
* `corpus/SOURCES.md:80` — S051's `scope` field reads: "what Sherratt's secondary-products thesis claims and this review's three-region critique (Central Anatolia, Balkans, North European Plain); **not primary for Sherratt**".

`corpus/QUALITY.md:29` (criterion 6): "publisher descriptions and abstracts are tier B for substantive claims about a work,
even when accurate; reserve tier A for sources primary or authoritative for the exact scope." Rendering an abstract
sentence as Sherratt's own phrasing is a substantive claim about a work, sourced to a row that disclaims exactly that
standing. (Note the entry is otherwise honest here: it grades the claim **C** at `:93` and `:183`. The defect is the
attribution of the quotation, not the calibration.)

*Smallest fix:* attribute the string to the row's actual holder — "Marciniak's summary of Sherratt's thesis: '…'
(S051)" — or drop the quotation marks and paraphrase.

#### M5 — the living-practice flag claims current practice from rows scoped as dated / not current, and names an unsourced people

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:189`

```
**Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063).
```

Row scopes at the landed commit:

* `corpus/SOURCES.md:87` (S058) — "the WoDaaBe seasonal movement system in southeastern Niger **as observed 1996–97, cattle only**; not Fulani at large, **not current practice**";
* `corpus/SOURCES.md:92` (S063) — "UNESCO's own inscribed description of the Bedu cultural space; **dated testimony, not ethnography**";
* `corpus/SOURCES.md:89` (S059) (Sámi) — the agency register, current ✓.

So two of the three ids offered for "are living practice" carry rows that explicitly say they are not current practice.
Independently, the flag names six peoples but cites three ids, and the mapping does not close: **Maasai has no anchor at
all** — `grep -n "Maasai" …/pastoralism-animal-husbandry.md` → line 189 only, with no S-id and no in-corpus
`path:line`; and Mongolian/Tibetan are covered by S060 (Ahearn, Mongolia) and S061 (*The Yak*, Qinghai-Tibetan), which
the flag does not cite.

*Smallest fix:* re-scope the sentence to what the rows carry ("Mongolian, Sámi, Bedu, WoDaaBe and Tibetan herding have
living practitioners today; S058 and S063 describe them as observed/dated"), cite S060/S061 for Mongolian/Tibetan, and
either anchor Maasai (a new S-row) or drop it from the list.

### LOW

#### L1 — §11 step 1's check promises a "water" tie the cited anchor cannot carry

`:151` — `| 1 | Ecology | rainfall, forage patchiness, water points | dung, fuel and water tied in (`fire-fuel-light.md:37`) |`

`fire-fuel-light.md:37` is the "Dried dung" row: "the herds' output, and therefore the fields' | a hot, fast, smoky fire |
a real trade-off against manure; fuel-poor pastoral cultures pay for it in soil" — dung, fuel, manure ✓, water ✗. The file
contains no water content at all:

```
$ grep -ni "wate" corpus/knowledge/culture-material/fire-fuel-light.md
84:- **Firefighting technology.** The bucket chain (a *labor* answer: neighbours, a line, a river); …      ← only "river", in a bucket-chain line
```

*Fix:* keep the dung/fuel tie on `fire-fuel-light.md:37` and either cite a water-bearing anchor for the waterpoint half
or drop "and water" from the check cell.

#### L2 — §11 step 5 asserts an element ("disease") with no source and no `(to-verify)`

`:155` — `| 5 | Wealth | herd ceiling set by labour and disease; loan and gift networks | §7; S049 |`

S049's `teaches` (`corpus/SOURCES.md:78`): "herd wealth tracks household labour; tenure is divided by ecology and the
potential for agriculture; pastoral tenure is a common-property debate, not open access" — labour only. "disease" as a
herd-ceiling factor appears nowhere else in the corpus:

```
$ grep -rni "disease\|epidemic" corpus/knowledge --include=*.md | grep -i "herd\|pastoral"
(no hits)
```

Under QUALITY criterion 1 (`corpus/QUALITY.md:5-8`) an unverifiable factual claim must be marked `(to-verify)` inline.
*Fix:* drop "and disease", or mark it `(to-verify)`.

#### L3 — the header's in-corpus authority list over-declares: four anchors are never used in the body

`:6` claims "In-corpus anchors (repo-relative `path:line`, each re-read at `4ad2683` on 2026-10-21): … `culture-material/hunting-foraging-subsistence.md:27,:36,:116,:117,:137-146,:170-172,:195`; `culture-material/agrarian-field-system-lexicon.md:56,:62,:80`; …"

Body hits for the four unused ones:

```
$ grep -n -- ":117\|:137\|:170" …/pastoralism-animal-husbandry.md      → only line 6 (the header itself)
$ grep -n "agrarian-field-system-lexicon.md:80" …/pastoralism-animal-husbandry.md → no hit
```

`:117` is "Storage as the hinge of rank" (a rank claim with no herding content), `:137-146` is the "## 9. Decision table"
region, `:170-172` the "## 12. NON-CANON worked micro-example" region, and `agrarian-field-system-lexicon.md:80` is the
Sherratt "(to-verify)" note. The entry's own provenance claim therefore lists four documents it never draws on — one of
them (`hunting-foraging-subsistence.md:117`) for a proposition about herding that it does not make.

*Fix:* cite each where it is actually used (or drop the four from the header list).

#### L4 — two quoted strings are not carried by the filed Gate record

* `:43` — `"Any classification of this type must be treated as a simplification" (S048)`. The Gate bullet
  (`corpus/lessons/round-50.md:33`) records only `§Classifying pastoral systems: "there is little or no impetus to herd animals"`.
  The row's `teaches` ("…as simplified degrees of movement") supports the substance, but the quoted sentence is not in
  the filed evidence.
* `:61` — `"camel husbandry" as a named skill (S063)`. The Gate bullet (`corpus/lessons/round-50.md:48`) records only
  `Description ¶2: "The Bedu communities inhabiting this area keep alive a traditional pastoral culture and related skills."`;
  the row's `teaches` says "skills including camel husbandry", but the quoted phrase is not in the recorded quote.

Both are plausible from the rows' anchors, so this is an evidence-record gap rather than a demonstrated misquotation —
but the quotation marks are currently unbacked by the lane's own Gate. *Action:* the URL-reopening seats should confirm or
correct the two strings; if a string is not verbatim, drop the quotation marks.

#### L5 — §11 error row 3 anchors a claim the source does not make

`:164` — `| "Last nomads" doom framing | mobile pastoralism coexists with other production (`mongol.md:40`) | R as forecast |`

`corpus/knowledge/civilizations/mongol.md:40` reads: "This is a working periodization, not a ladder from 'primitive nomad'
to 'civilization'. Mobile pastoralism, urban production, and documentary administration can coexist." That refutes a
*stage ladder* (already its job at `:43`) and supports coexistence; it says nothing about a doom/forecast framing of
"the last nomads", which is what the error-pattern cell names and what the code column grades ("R as forecast").

*Fix:* restate the error pattern to the claim the anchor refutes ("Pastoralism as a stage on a ladder / the last nomads
are the previous era" — `mongol.md:40`), or anchor the doom framing to a source that addresses it.

#### L6 — `dine-navajo.md:125` is cited for a claim it does not carry

`:118` — "State settlement, privatisation and route closure are local history, never a fixed endpoint of mobility
(`finnic-sami.md:150`; `dine-navajo.md:125`)". `finnic-sami.md:150` supports the "has a history / not the eternal
condition" half ✓. `dine-navajo.md:125` reads: "'Traditional' can incorporate introduced animals; do not stage wool
pastoralism as unchanged from remote antiquity." — a claim about imported sheep and land-based practice; it says nothing
about state settlement, privatisation or route closure. *Fix:* narrow the sentence to "pastoralism has a history and is
not the eternal condition", or cite a line that carries the settlement/privatisation claim.

#### L7 — the Gate record for S066 names the wrong seat

`corpus/lessons/round-50.md:50-51`:

```
- S065 — … https://www.ahdictionary.com/word/indoeurop.html#IR084700 … Seat: SrcPeku.
- S066 — … https://d-place.org/parameters/EA004 … Seat: SrcPeku.
```

S066 (D-PLACE EA004) is filed under the seat that opened the AHD *peku-* entry. The entry leans on S066 for a
quantitative statement (`:25`, "the Ethnographic Atlas codes only a small minority of its societies as near-totally
dependent"), whose support is a value-count read that the filed Gate quote does not contain (the quote is only the
variable Description). *Fix:* in a later lesson (append-only per `corpus/SOURCES.md:9-13`), record the EA004 value-count
quote and the true seat.

#### L8 — the §4 ecology column asserts habitat facts with no anchor

`:59-65` — "grass and reliable water", "arid-tolerant small stock", "hot and cold deserts", "steppe grassland", "taiga
and tundra lichen pasture" carry no source and no `(to-verify)`; only yak (`:63`, S061) and llama/alpaca (`:65`, S068)
are anchored. S050's scope is domestication chronology in the Fertile Crescent, not habitat, so the cattle/horse rows
cannot lean on it. *Fix:* cite or mark the ecology cells.

#### L9 — §11 has no failure condition per step (usability, QUALITY criterion 4)

`:149-158` — columns are `# | Build step | Decide before moving on | Check`. The neighbouring decision table in this
partition (`hunting-foraging-subsistence.md:161`) uses `ID | Decision | Trigger | Failure if skipped`. §11's "Decide
before moving on" is the closest thing, but a step with no stated failure mode cannot fail loudly.

#### L10 — compound calibration codes have no precedent in the corpus

`:163` "R as a static type", `:164` "R as forecast", `:180` "R as description". `verification/calibration-registry.md:27`
states the rule these stretch: "A verdict attaches to a proposition, not to an author's entire output, a people, or a
religion"; the neighbouring entry writes the same idea as "R (as universal)"
(`hunting-foraging-subsistence.md:182`). `grep -rn "R as forecast\|R as a static\|R as description" corpus/knowledge` hits
only this file. *Fix:* use bare codes or the parenthesised form.

---

## What holds (checked, no finding)

* **Every S-id cited resolves to a row, and the rows are used within their own scope.** Checked id-by-id against
  `corpus/SOURCES.md:77-98` `scope`/`teaches` and the Gate bullets at `corpus/lessons/round-50.md:33-54`: S048 (typology,
  stage-refutation, herd splitting, "two to four species"), S049 (labour–wealth link, tenure sentence), S050 (culling
  before morphology, 11,000–10,000 BP, regional species order), S051 (contested single horizon — except the attribution,
  M4), S052 (Nuer idiom, cow naming, age/sex terms), S053 (label attribution only; 1926 text marked unopened — a
  QUALITY-6 exemplar at `:181`), S054 (open-pasture parable only), S055 (design principles as diagnosis, not prediction),
  S056 (non-autarky, trade as political pressure), S057 (publisher programme only — the entry uses nothing else and says
  so at `:187`), S058 (seasonal moves/named move types), S059 (earmark institution, Swedish only, marked B), S060 (five
  snouts, dzud risk), S061 (yak summer pastures, butter, dung fuel), S062 (ger portability), S063 (camel husbandry), S064
  (nightly count, rival sisters), S065 (gloss only, "never print the root as settled social history"), S066 (dependence
  bins), S067 (Botai ≠ modern domestic horse), S068 (only domesticated ungulates of the Americas), S069 (horizontal/vertical
  transhumance). All 22 ids in the header are actually used in the body (counts: S048×11 … S069×4) and no id outside
  S048–S069 is cited.
* **Gate-quoted strings that check out verbatim:** "there is little or no impetus to herd animals" (`:16`),
  "Tenure is thus divided by both ecology and the potential for agriculture" (`:110`),
  "Nuer tend to define all social processes and relationships in terms of cattle" (`:106`),
  "Picture a pasture open to all" (`:114`), "developed by the users of a resource" (`:115`),
  "always experienced a need for external agricultural and handicraft products" (`:122`),
  "Every night your count is made and your tally-stick put into the ground" (`:139`),
  "Wealth, movable property" (`:79`), "on pastures at high elevations" (`:63`), "light enough for nomads to carry"
  (`:47`), "five snouts" (`:67`), and the S057 list "segmentary tribes, tribal chiefdoms, and peasant pastoralists"
  (`:53`).
* **In-corpus anchors that resolve to the right lines and support the citing sentence:** `hunting-foraging-subsistence.md:27`
  (the patch), `:36` ("not planted, herded or owned" — quoted exactly), `:116` (meat-for-crops), `:195` (living-practice
  flag); `agrarian-field-system-lexicon.md:56,:62` (parcel/plough/stubble/manure, agropastoral row);
  `trade-economy-lexicon.md:69` (cattle-root money words, *pecūnia*); `transport-mobility-lexicon.md:95` (draught/load
  row, "harness and feed vocabulary"); `animal-symbolism.md:73,:110`; `sacred-kingship-mythic-charter.md:65` (shepherd
  audited by the gods); `symbolism-synthesis-method.md:69` ("An animal taboo implies a rite; write both or neither" —
  supports both §10's sacrifice row and §11 step 8); `celestial-symbolism-calendars.md:28` ("pastoralists on milky/river
  figures"); `mongol.md:40`; `turkic-steppe.md:148,:193,:194`; `scythian-saka.md:70`; `finnic-sami.md:140,:150`;
  `inca.md:128` ("all wool, all alpaca" is too simple — quoted exactly); `calibration-registry.md:35-39,:142` (the stage
  ladder row is exactly the §11/§13 error it is cited for). `textile-technology.md:27` supports "fleece selection" but is
  thinner than the §2 cell's "fibre-to-cloth chain" wording (borderline; folded into M2's fix).
* **Canon hygiene (QUALITY 5):** §12 is explicitly NON-CANON (`:169`), §15 hands every canon decision to lore-shokunin
  and marks the lore intake as still pending so every handoff is "a candidate, not an import" (`:199`); §2 keeps the
  one-owner boundary; no in-world truth is asserted.
* **No unopened-source laundering:** the Herskovits 1926 text is marked unopened at `:11`, `:181`, `:195`; Ostrom's 1990
  book is distinguished from the 2009 lecture at `:195`; S050/S067 dates carry a re-open instruction at `:11`.

---

## Residual risk and verification gaps

1. **Verbatim strings not covered by the filed Gate** (L4): two quotation marks (S048 §Classifying, S063 "camel
   husbandry") and possibly the S051 attribution (M4) need a URL seat to confirm the exact wording; this seat did not
   open URLs by instruction.
2. **Tier-vs-calibration mixing:** §8's Ostrom row grades a predictive law "C" while the row is tier A; that is legitimate
   (calibration code ≠ tier) but it is the kind of pairing that invites a reviewer to read the tier as the verdict.
3. **Header anchor list:** beyond the four unused anchors, the header labels its paths "repo-relative" while they are
   `corpus/knowledge`-relative (`culture-material/…`, `verification/…`). This matches the lane-wide convention in
   `hunting-foraging-subsistence.md:6`, so it is a lane-wide labelling inaccuracy rather than a defect of this entry —
   noted for the lane, not scored here.
4. **§12's worked example** (`NON-CANON`) applies §11 in eight stages and silently drops products (see M3); it should
   either follow the corrected order or say why products are folded in.
5. The `S066` seat misattribution (L7) is a lesson-record defect, not an entry defect, but it weakens the provenance of
   the entry's one quantitative ethnographic statement (`:25`).

## Recommendation to the author lane

The section is not rejected; it is not yet operable. In priority order: fix the step-6 anchor to
`semantic-fields-lexicon-building.md:70` (M1), reconcile the §4 and §11 build orders and give products a step (M3),
correct the §2 cuisine anchors (M2), re-attribute the S051 quotation to the row that holds it (M4), and re-scope the
living-practice flag (M5). L1, L2, L3, L5–L8 are cheap follow-ups in the same file; L4 and L7 need the URL seat and a
later lesson respectively.
