# ReviewSec02 — attack on §2 "One-owner boundary" table of the round-50 C entry

Seat: `KotodamaR50-2.ReviewSec02-21` (leaf, read-only). Round 50 falsify wave, lane `kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).

All lane bytes were read from a private clone (`git clone -q --shared … /tmp/ReviewSec02-ab12; git checkout -q 1c779e4a…`)
or via `git -C <lane> show 1c779e4a…:<path>`. The lane working tree was never read for a claim and never touched.
No lane file was edited except this report; no `git add/commit/stash/checkout/reset` and no mutating `jj` command was
run in the lane; the lane jj state, git index, fleet repo, sibling lanes, `MANIFEST.json`, `.ufo/state` and the
watchdog log were not touched. No URL was re-opened (the `ReopenS0xx` seats own that). **Tooling: none installed**
(all pacman transactions are paused host-wide; no install was needed for this seat).

**Note on the lane working tree (author lane is already editing).** At the time this report was written the lane
working tree already carries uncommitted edits to the entry (`git status --porcelain` shows
`M corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`). Those edits were **not** written by this seat
and are **not** the landed bytes. They already apply part of this report's advice: the working tree's §2 `:33` now
cites `cuisine-food-lexicon.md:67,:81,:152`, `:34` cites `transport-mobility-lexicon.md:92,:95`, `:36` cites
`textile-technology.md:22,:27`, and two new rows have been added (`animal-symbolism.md:73,:110`,
`sacred-kingship-mythic-charter.md:65`). Every finding below is stated against the **landed** commit
`1c779e4a…`, which is what the falsify wave attacks; where a fix is already in flight in the working tree it is
noted in the finding. Line numbers quoted in this report are **landed** line numbers.

## Verdict: **PARTIAL**

§2's *device* works and its anchors are stable: every `path:line` in the table resolves at the landed commit,
every neighbour file is byte-identical between base and landed (so no line reference has drifted), and the
one-owner boundary is genuinely asserted in the sense the sibling entries use. But the table as landed does not
hold as a one-owner boundary table:

* **3 of 9 rows mis-describe the anchor they cite** — the ownership cell names a fact that is not on the cited line
  (`:33` milk+meat law; `:34` route class; `:31` "stubble grazing"), and one row's anchor is cited **against** the
  cell it is supposed to support (`:36` `textile-technology.md:27` supports "fleece selection", which the row
  assigns to *this* entry, not to the neighbour);
* **one row's third column claims ownership the cited neighbour line already grants to the neighbour**
  (`:38` "the herd as dung source" — `fire-fuel-light.md:37` already says the dung is "the herds' output");
* **6 of 9 rows' third-column boundaries are never developed anywhere in the body** (the entry's own prose);
* **§2 is materially below the lane's own contract and candidate set** — the contract asks for a lead sentence and
  "15 or more rows"; the table has no lead sentence and 9 rows, and **7 of the contract's 23 candidate neighbours
  are never cited anywhere in the entry**;
* the `civilizations/` row is the **only row in the table with no `path:line` anchor at all**, so the table's own
  header ("Neighbour (anchor)") is false for it;
* and the market register — the one neighbour the entry's own scope and §15 both hand off — has **no row**.

**The author lane is already fixing part of this in the working tree** (uncommitted; not the landed bytes): the
`:33`/`:34`/`:36` anchors are corrected and two rows (`animal-symbolism`, `sacred-kingship`) have been added, taking
§2 from 9 to 11 rows. Each finding below states what the **landed** commit does and notes what is already in flight.
Still open after those in-flight edits: the lead sentence and header (F5), the market row and the seven never-cited
candidate neighbours (F6), the "stubble grazing" phrase and the agrarian water/tenure half (F7), the unanchored
`civilizations/` row (F8), the `(to-verify)` markers (F9), the feed-vocabulary collision and the eight
never-developed third-column boundaries (F3, F4).

Scope executed: (a) every `path:line` anchor cited in §2 opened at the landed commit and checked against the
sentence that cites it; (b) every S-id in the entry (S048–S069) checked against its `corpus/SOURCES.md` row's
`scope`/`teaches`; (c) the §2 table's third column checked against the entry's own body; (d) the table's shape
checked against the build contract and its candidate set; (e) QUALITY criteria 1–6 applied to §2.

---

## F1 (HIGH) — §2 `:33` mis-anchors two of its three ownership claims; `:86` is a **pig** taboo line

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:33` (landed):

```
| `cuisine-food-lexicon.md:67,:86` | yogurt lineages, milk+meat law, Harris's cattle economy (contested) | milking, churning and the dairy chain up to the product |
```

At the landed commit:

```
$ git show 1c779e4a:corpus/knowledge/culture-material/cuisine-food-lexicon.md | sed -n '67p'
| Bacteria+lactobacilli | kimchi (kimjang communal making, UNESCO 2013), sauerkraut, yogurt lineages, idli/dosa batters | seasonal collective labor with a fermentation clock; buried-jar autumn events |          ← yogurt lineages ✓

$ git show 1c779e4a:corpus/knowledge/culture-material/cuisine-food-lexicon.md | sed -n '86p'
- Three rival explanations of the taboo systems — keep all three alive in-world (real scholarship has not settled it): Douglas (1966): the pig is a taxonomic anomaly …; Milgrom (1991): the diet expresses holiness …; Harris (1985): cultural materialism — pigs compete with humans for food and were ecologically costly in the deforested Near East (cf. Herodotus 2.47 on Egyptian pig-avoidance), while cattle are worth more alive (traction, milk, dung) than dead — the cow taboo as economy. …        ← Harris's *cattle* clause IS on :86 ✓

$ git show 1c779e4a:corpus/knowledge/culture-material/cuisine-food-lexicon.md | sed -n '81p'
| Mixing rules | milk + meat separation (Ex 23:19 "kid in its mother's milk", ×3 in Torah); separate dishes; waiting times | no milk+meat law; wine and intoxicants forbidden (Quran 5:90) — the big divergence |        ← "milk+meat law" is HERE, not at :67 or :86

$ git show 1c779e4a:corpus/knowledge/culture-material/cuisine-food-lexicon.md | sed -n '152p'
- Harris's materialist taboos (pig economics, cow economics) — contested by culturalists; strongest case is the pig, weakest the cow. …        ← the "contested" grading is HERE, not at :86
```

Only **"yogurt lineages"** is supported by the cited pair. **"milk+meat law"** is at `:81`, not at `:67` or `:86`.
"Harris's cattle economy" *is* on `:86` (the clause "while cattle are worth more alive (traction, milk, dung) than
dead — the cow taboo as economy"), but the cell's parenthetical **"(contested)"** is not carried by `:86` — the
contest statement is at `:152` ("strongest case is the pig, weakest the cow"), and `:86` says only that "real
scholarship has not settled it" about the *taboo systems* generally.

Why this is a §2 finding and not a §11 finding: this row's whole function is to point a writer at the owner of a
concept. A wrong line hands the writer to the wrong cell — `:81` (mixing rules) is a **taboo/rule** cell, `:67` is a
**fermentation** cell, `:86` is a **pig-taboo** cell. The reader who follows `:67` for "milk+meat law" lands on
kimchi and yogurt; the reader who follows `:86` for "contested" lands on the pig, not the cow.

**Smallest fix.** `:33` → `` `cuisine-food-lexicon.md:67,:81,:86,:152` `` and keep the cell as is; or drop
"milk+meat law" and "(contested)" from the cell and cite `:67,:86` only.

*Already in flight in the working tree:* `:33` now reads `` `cuisine-food-lexicon.md:67,:81,:152` `` — the `:81`
and `:152` anchors are added, which closes the "milk+meat law" and "(contested)" mis-handoffs. Note the working
tree also renames the cell to "Harris's **cow** economics (contested)" while dropping `:86`; `:86` is the only line
that carries the **cattle** clause itself ("while cattle are worth more alive (traction, milk, dung) than dead"),
whereas `:152` carries the contest grading. Keeping `:86` alongside `:152` would preserve both halves.

*(Cross-reference, not re-litigation: the same mis-anchor is independently reported by the §11 seat as `M2` in
`ReviewSec11.md` and the *head* seat as `B2` in `ReviewHead.md`. The §2-specific evidence here is that this row is
the one-owner table row, so a wrong line is a mis-handoff, and that the `(contested)` grading has a separate home at
`:152` — neither sibling report states that.)*

---

## F2 (HIGH) — §2 `:36` cites `textile-technology.md:27` for the *neighbour's* cell, but `:27` supports the **entry's** cell

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:36` (landed):

```
| `textile-technology.md:27` | fibre-to-cloth chain | flock management, shearing season, fleece selection |
```

At the landed commit:

```
$ git show 1c779e4a:corpus/knowledge/culture-material/textile-technology.md | sed -n '27p'
- **Wool technology is the fork that matters**: combed long-staple = **worsted** …; carded short-staple = **woolen** … Ryder (1983) traces fleece evolution: wild sheep are hairy; wool-dominant fleeces are a Bronze-Age artifact of selection — your culture's fleece quality is a *chronology* you can date.

$ git show 1c779e4a:corpus/knowledge/culture-material/textile-technology.md | sed -n '22p'
| wool | *Ovis aries* | shear → wash (suint/urine, lanolin) → card or comb → spin | excellent — scaled fiber grips dye; richest colors are wools | the state economy: Ur III wool-ration workshops, English export, Flemish drapery (Breniquet & Michel 2014) | worsted, woolen, fleece, staple, *Walker/Tucker* = fullers |
```

`:27` is the **fleece-quality / worsted-vs-woolen** bullet — it is the evidence for **"fleece selection"**, which
this row assigns to **this entry's** boundary, not to the neighbour's. The "fibre-to-cloth chain" the neighbour cell
claims is at `:22` (`shear → wash → card or comb → spin`), which is **not cited**.

So the anchor is inverted against its own cell: the cited line evidences the entry's half of the boundary and is
offered as evidence for the neighbour's half.

Two further problems inside the same row, both §2-only:

* **"shearing season" is not developed anywhere in the entry** and, worse, the word *shearing* in the textile file
  never means animal shearing: `textile-technology.md:14` is "**Finish gate** — fulling, nap-raising, shearing
  capacity (§5)" — **cloth**-shearing. A writer who follows this row will place the herd's shearing season inside
  the cloth-finishing gate.
* **"flock management"** is developed, but only as a *hand-off*, not as content: `entry:89` reads
  `| Wool and hair | living animals, shorn or plucked | flock management lives here; cloth stays in \`textile-technology.md:27\` |`.

**Smallest fix.** `:36` → `` `textile-technology.md:22,:27` `` with the neighbour cell rewritten as
"wool prep chain and fleece quality"; and change the entry's boundary cell to "flock management and shearing season;
fleece *choice* for herd selection, distinct from textile's fleece-quality chronology (`textile-technology.md:27`)"
— or drop "shearing season" and "fleece selection" if the entry does not develop them (see F4).

*Already in flight in the working tree:* `:36` now reads `` `textile-technology.md:22,:27` `` with the neighbour cell
"fibre-to-cloth chain; worsted/woollen fork" — the anchor inversion is fixed. The entry's boundary cell becomes
"flock management and shearing season" (i.e. **"fleece selection" is dropped**), which closes the F4 non-development
for that phrase; "shearing season" is still not developed in the body (F4).

*(Cross-reference: `ReviewHead.md` `B2` reports the anchor inversion; `ReviewSec11.md` folds the "fibre-to-cloth
chain" wording into its `M2`. The §2-specific addition here is the `:22` line number for the prep chain and the
`textile-technology.md:14` "shearing capacity" = cloth-shearing collision, which no sibling report states.)*

---

## F3 (MEDIUM-HIGH) — §2 `:34` claims "route class" from `:95`, and its third column collides with the anchor's own "feed vocabulary"

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:34` (landed):

```
| `transport-mobility-lexicon.md:95` | draught capacity chain, route class, load figures | husbandry of riding and pack animals (feed, training, herd share) |
```

At the landed commit:

```
$ git show 1c779e4a:corpus/knowledge/culture-material/transport-mobility-lexicon.md | sed -n '95p'
| Draft | human porterage, ox, horse/mule, camelid, dog, wind | load figure + daily distance + terrain law; harness and feed vocabulary | civilizations/inca.md, civilizations/turkic-steppe.md |

$ git show 1c779e4a:corpus/knowledge/culture-material/transport-mobility-lexicon.md | sed -n '92p'
| Route class | track, paved road, causeway, canal, sea lane, relay corridor | a maintenance institution and a permit regime | `architecture-settlement-lexicon.md`, `calendar-festival-systems.md` |
```

* **"Route class" is a different row, at `:92`.** `:95` is the **Draft** row: it supports "draught" (ox, horse/mule,
  camelid, dog) and "load figures" (load figure + daily distance), but not "route class".
* **"feed" collides.** `:95`'s own words commit the transport file to "harness and **feed** vocabulary" for exactly
  the animals (ox, horse/mule, camelid, dog) whose feed §2 assigns to this entry. §2's third column says the entry
  owns "husbandry of riding and pack animals (**feed**, training, herd share)" while the row it cites says the
  neighbour owns the feed vocabulary for the same animals. The one-owner split is not stated, so the two cells
  compete.
* **"training" and "herd share" are developed nowhere in the entry** (see F4).

**Smallest fix.** `:34` → `` `transport-mobility-lexicon.md:92,:95` ``, and restate the third column as
"husbandry of riding and pack animals — breeding, weaning, herd share; the neighbour's feed and harness vocabulary
stays there".

*Already in flight in the working tree:* `:34` now reads `` `transport-mobility-lexicon.md:92,:95` `` with the
ownership cell reordered to "route class; draught capacity chain and load figures" — the `:92` mis-handoff is fixed.
The third column is **unchanged** ("feed, training, herd share"), so the feed-vocabulary collision and the
"training"/"herd share" non-development (F4) are still open.

*(Cross-reference: `ReviewSec08.md` `P3-a` reports the `:92`/`:95` mis-description; `ReviewHead.md` `B6` reports the
same gloss at the head. The **feed-vocabulary collision** and the "training"/"herd share" non-development are the
§2-specific parts; no sibling report states the collision.)*

---

## F4 (MEDIUM) — six of §2's nine third-column boundaries are never developed in the entry's body

The third column of §2 is where the entry states what it *keeps*. Measured over the whole 199-line entry at the
landed commit:

```
$ for t in "herd composition" "milking" "churning" "the dairy chain" "training" "herd share" "shearing season" "fleece selection" "the herd as dung source"; do printf '%-24s total=%s\n' "$t" "$(grep -oi -- "$t" <entry> | wc -l)"; done
herd composition         total=1        ← the §2 cell itself, nowhere else
milking                  total=1        ← the §2 cell itself, nowhere else
churning                 total=1        ← the §2 cell itself, nowhere else
the dairy chain          total=1        ← the §2 cell itself, nowhere else
training                 total=1        ← the §2 cell itself, nowhere else
herd share               total=1        ← the §2 cell itself, nowhere else
shearing season          total=1        ← the §2 cell itself, nowhere else
fleece selection         total=1        ← the §2 cell itself, nowhere else
the herd as dung source  total=1        ← the §2 cell itself, nowhere else
```

Every one of these nine phrases occurs **exactly once in the whole file** — in the §2 cell that asserts it. The body
carries the *neighbourhood* of these topics but never the terms:

| §2 cell | asserted boundary | what the body actually carries |
|---|---|---|
| `:31` | "herd composition" | `:8` (head couples) "this entry owns the herd's movement logic and composition"; `:47` "species mix and movement are the hedge (S060)"; `:59` "age-grade herd labour". The phrase "herd composition" itself: 0 hits outside §2. |
| `:33` | "milking, churning and the dairy chain up to the product" | `:88` "dairy needs pails, a curd/butter chain and storage" — a **curd/butter** chain, never "milking", "churning" or "dairy chain"; `:88` also carries the S061 plateau-scope problem the §6 seat reports. |
| `:34` | "training, herd share" | `:152` "two to four species and their shares (S048)" is the only "share"; "training" (and trained/broken/halter/saddle/harness/yoke/stable) appears **nowhere**. |
| `:36` | "shearing season, fleece selection" | `:89` "living animals, shorn or plucked; flock management lives here" — the shearing **season** and the **selection criteria** are not stated. |
| `:38` | "the herd as dung source" | `:91` "Dung | any herd | one dung per season: fuel or field" — the entry treats dung as a **product row**, and does not claim the herd as its source; and `fire-fuel-light.md:37` already says the dung **is** "the herds' output, and therefore the fields'". |
| `:32` | "the herded counterpart only" | `:20` in §1 owns the wild/herded contrast, not §2; the phrase appears 0 times outside §2. |

Why this matters for the one-owner table specifically: the third column is the entry's **claim of ownership**. An
ownership claim the entry never exercises is a claim the table cannot support — a writer auditing the table will
find that the entry "owns" milking, churning, training and shearing season, and will look for them in §3–§6, where
they do not exist. QUALITY criterion 4 (usability) and criterion 1 (every factual claim cited or marked
`(to-verify)`) are the rules this runs into: the §2 cells make three-to-four-term factual claims about what the
corpus contains, with **no `(to-verify)` marker anywhere in §2** (`grep -c 'to-verify'` over §2 → 0).

**Smallest fix.** Either (a) add the missing material — one §6 row for the dairy chain with a `(to-verify)` on the
curd/butter specifics, one §4 or §6 cell for shearing season and selection criteria, one §6 cell for the training
of draught and riding stock — or (b) reduce the third-column cells to what the body actually carries:
"herd composition (species and age-grade structure)", "milking and the dairy chain up to the product
(`:88`)", "herd share and the composition of a draught herd", "flock management and fleece choice
(`:89`)", "the herd as dung source (`:91`)".

*Already in flight in the working tree:* only "fleece selection" has been dropped (working-tree total 0); the
other eight phrases still occur exactly once each — in the §2 cell that asserts them — and the body still has no
milking/churning/dairy-chain, training, herd-share, shearing-season or dung-source development.

*(Cross-reference: `ReviewSec11.md` `M2` and `ReviewHead.md` `B2` touch `:33`/`:36` from their own sections; the
"term occurs exactly once, in the cell that asserts it" measurement across all nine cells is this seat's.)*

---

## F5 (MEDIUM) — §2 is below the lane's own contract: no lead sentence, 9 rows against "15 or more", and the header drops "(live anchor)"

The build contract for this entry — `.ufo/waves/round-50/build/ReviewEntryContract.md:62` — reads in full:

```
2. **One-owner boundary.** One sentence, then `| Neighbour | What it owns (live anchor) | This entry's boundary |`, 15 or more rows (§4 is the candidate set).
```

The landed §2:

```
27: ## 2. One-owner boundary
28: (blank)
29: | Neighbour (anchor) | What it owns | This entry's boundary |
30: |---|---|---|
31-39: nine data rows
```

Three deviations, all verifiable:

* **No lead sentence.** Line 28 is blank. The contract asks for "One sentence, then …". Both sibling one-owner
  tables in the same partition carry one: `hunting-foraging-subsistence.md:45` ("The corpus's two regional files
  already own worked seasonal rounds …") and `cartography-and-mapmaking.md:46` ("Cosmography owns the world-drawn
  content …"). The lead sentence is what states the partition rule the table then applies; without it §2 is a
  list, not a boundary.
* **9 data rows, not "15 or more"** — and the two sibling tables carry **19** (`hunting-foraging-subsistence.md:49-67`)
  and **12** (`cartography-and-mapmaking.md:50-61`) data rows, so the landed table is below the house norm as well
  as below the contract.
* **The header drops the contract's "(live anchor)"** and rewrites the first column as "Neighbour (anchor)":
  contract `:62` → ``| Neighbour | What it owns (live anchor) | This entry's boundary |``; landed `:29` →
  ``| Neighbour (anchor) | What it owns | This entry's boundary |``. Both sibling tables use the contract header
  verbatim.

**Smallest fix.** Add a lead sentence at `:28` (one line naming the partition rule — e.g. "The field, the hunt, the
dish, the cloth, the road, the market, the lexicon field and the regional cases are owned elsewhere; this entry owns
the herd as a production system."), restore the contract header verbatim, and add the missing rows (F6).

*Already in flight in the working tree:* the row count has gone from 9 to **11** (`animal-symbolism.md:73,:110` and
`sacred-kingship-mythic-charter.md:65` rows added at working-tree `:39`–`:40`). The **lead sentence is still absent**
(line 28 is still blank), the **header is still drifted** (still `| Neighbour (anchor) | What it owns | …`), and 11 rows
is still below the contract's "15 or more" and below the `hunting-foraging-subsistence.md` sibling's 19.

*(Cross-reference: `ReviewSec01.md` records the "9 rows vs 15 or more" gap as a contract item outside its own §1
scope. What is new here is the **lead sentence** and the **header drift**, neither of which any sibling falsify
report mentions — `grep -l 'lead sentence'` over the falsify directory returns no file.)*

---

## F6 (MEDIUM) — §2 omits the neighbours the lane's own candidate set lists, including the market register the entry's scope and §15 both hand off

The contract's §4 candidate set (`ReviewEntryContract.md:212-236`) lists **23 neighbour paths**, each with a
verified live anchor and a proposed boundary. The landed §2 table has 9 rows. Checking every candidate against the
whole entry:

```
$ for p in <23 candidate basenames>; do printf '%-34s entry_hits=%s\n' "$p" "$(grep -c "$p" <entry>)"; done
hunting-foraging-subsistence           entry_hits=6    table_row=yes
agrarian-field-system-lexicon          entry_hits=6    table_row=yes
transport-mobility-lexicon             entry_hits=5    table_row=yes
fire-fuel-light                        entry_hits=6    table_row=yes
semantic-fields-lexicon-building       entry_hits=6    table_row=yes
trade-economy-lexicon                  entry_hits=4    table_row=yes (money words only)
textile-technology                     entry_hits=4    table_row=yes
cuisine-food-lexicon                   entry_hits=3    table_row=yes
writing-media-surface-economy          entry_hits=1    table_row=NO   ← only hit is the head's "sherd" false positive (entry:4)
ritual-garments                        entry_hits=0    table_row=NO
music-instrument-lexicon               entry_hits=0    table_row=NO
calendar-festival-systems              entry_hits=0    table_row=NO
hero-journey-variants                  entry_hits=0    table_row=NO
source-discipline-calibration          entry_hits=0    table_row=NO
coupling-model                         entry_hits=0    table_row=NO
costume-era-consistency-gate           entry_hits=0    table_row=NO
animal-symbolism                       entry_hits=4    table_row=NO   ← cited only at entry:145 (§10) and in the head/couples lines
sacred-kingship-mythic-charter         entry_hits=3    table_row=NO   ← cited only at entry:141 (§10)
celestial-symbolism-calendars          entry_hits=2    table_row=NO   ← cited only at entry:143 (§10)
mongol / turkic-steppe / scythian-saka / finnic-sami / dine-navajo / inca   ← one bundled `civilizations/` row, no line anchors
calibration-registry                   entry_hits=4    table_row=NO
```

**Seven candidate neighbours are cited nowhere in the entry at all** (`entry_hits=0` above), and an eighth
(`writing-media-surface-economy.md`) has exactly one hit that is not a citation — the head's own "sherd" false
positive at `entry:4`. Each is a live one-owner seam with a verified anchor at the landed commit:

```
$ git show 1c779e4a:corpus/knowledge/culture-material/ritual-garments.md | sed -n '80p'
… The pallium (metropolitan's wool band) is woven from lambs blessed on the feast of St Agnes, 21 January (Fortescue 1912): the office is annually *re-manufactured out of livestock and calendar*. …

$ git show 1c779e4a:corpus/knowledge/culture-material/music-instrument-lexicon.md | sed -n '87p'
| craft-brothers genealogy | Jubal 'father of all who handle harp and flute'; brothers Jabal (tents/livestock) and Tubal-cain (bronze/iron): pastoralist, musician, smith as one family | Genesis 4:19–22 |

$ git show 1c779e4a:corpus/knowledge/culture-material/calendar-festival-systems.md | sed -n '79p'
… poetic month names keyed to season and husbandry (Vendémiaire vintage, Brumaire mist, …) …

$ git show 1c779e4a:corpus/knowledge/myth-symbol/hero-journey-variants.md | sed -n '110p'
1. Assign the pattern family from political economy, not from the protagonist: …; steppe/pastoral → inherited slaying-formula and cattle-raid quests; …

$ git show 1c779e4a:corpus/knowledge/synthesis/source-discipline-calibration.md | sed -n '96p'
- Do not inherit causal recipes such as "delta state → combat cosmogony" or "pastoralism → one hero pattern" as empirical laws from `hero-journey-variants.md`; they are optional design associations, not ethnographic predictions.

$ git show 1c779e4a:corpus/knowledge/synthesis/coupling-model.md | sed -n '150p'
- Costume audit: … imported wool does not require local sheep husbandry; a new sign can be attached to old cloth without replacing the outfit.

$ git show 1c779e4a:corpus/knowledge/verification/costume-era-consistency-gate.md | sed -n '65p'
| MAT-02 | Show cultivation/herding/collection **or** an external supplier and transport path | Local climate cannot grow cotton, therefore no resident can own cotton cloth |
```

Two of these are **calibration** seams that this entry's own body needs and does not have:

* `source-discipline-calibration.md:96` names exactly the error this entry's §13 and §10 could fall into — "pastoralism
  → one hero pattern" as an empirical law. §2 has no row for it, and the entry never cites the file.
* `coupling-model.md:150` ("imported wool does not require local sheep husbandry") is the rule that would let §2's
  textile row distinguish *this entry's* flock management from *imported* wool — the very distinction `:36` currently
  blurs (F2).

And one is the **market register**, which the entry's own head and §15 both hand off but §2 does not:

* `entry:12` (`- scope:`) — "it hands the field, the hunt, the dish, the cloth, the road, **the market**, the lexicon
  field, the animal sign and every canon decision to their owners (**§2**, §15)";
* `entry:199` (§15) — "hands the field, the hunt, the dish, the cloth, the road, **the market**, the lexicon field,
  the animal sign and the shepherd-king to their owners (**§2**)";
* §2 has **no market row** — the trade-economy row (`:35`) covers only "cattle-root money words", and the market
  register's owner line is `trade-economy-lexicon.md:3` ("marketplace registers from haggling suqs to silent barter and
  auction chant"), which the entry **never cites** (`grep -c 'trade-economy-lexicon.md:3' <entry>` → 0).

So the two scope pointers that promise a market hand-off point at a §2 row that does not exist, and at a line the
entry never gives. The hunting neighbour itself pins that owner: `hunting-foraging-subsistence.md:116` ends "the
forager edge of that trade is this entry's, the market register stays at `trade-economy-lexicon.md:3`" — the §2 row
that should carry the market hand-off cites `:69` instead.

**Smallest fix.** Add a market row — ``| `trade-economy-lexicon.md:3,:69` | market, measure and money registers; cattle-root money words | herd-as-wealth composition and transfer rules; the market register stays there |`` — and add rows for the cited-elsewhere neighbours
(`animal-symbolism.md:73,:110`, `sacred-kingship-mythic-charter.md:65`, `celestial-symbolism-calendars.md:28`,
`ritual-liminality.md:63`, `symbolism-synthesis-method.md:69`, `calibration-registry.md:35-39,:142`) and for the seven
never-cited ones, using the verified anchors above.

*Already in flight in the working tree:* the `animal-symbolism.md:73,:110` and `sacred-kingship-mythic-charter.md:65`
rows have been added (working-tree `:39`–`:40`), which closes two of the six "cited elsewhere but no §2 row" gaps.
Still open in the working tree: the **market row** (the trade-economy row is still `:69` only), the
`celestial-symbolism-calendars.md:28`, `ritual-liminality.md:63`, `symbolism-synthesis-method.md:69` and
`calibration-registry.md:35-39,:142` rows, and all **seven never-cited** candidate neighbours
(`writing-media-surface-economy.md`, `ritual-garments.md`, `music-instrument-lexicon.md`,
`calendar-festival-systems.md`, `hero-journey-variants.md`, `source-discipline-calibration.md`,
`coupling-model.md`, `costume-era-consistency-gate.md`).

*(Cross-reference: `ReviewSec13.md` `F5` reports that §2 has no row for the animal sign or the shepherd-king while
§15 hands both to "(§2)"; `ReviewHead.md` `B2`/`B3` and `CriticGapPremise2.md` counterexample 1 report the
head/couples half. **Not** covered by any sibling report: the **market** row and the **seven never-cited candidate
neighbours** — `grep -l 'calendar-festival-systems\|hero-journey-variants\|source-discipline-calibration\|coupling-model\|costume-era-consistency-gate'` over the falsify
directory returns no file, and `grep -l 'market register'` returns no file.)*

---

## F7 (MEDIUM-LOW) — §2 `:31` mis-anchors "stubble grazing" and under-claims the agrarian neighbour's ownership

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:31` (landed):

```
| `agrarian-field-system-lexicon.md:56,:62` | parcel, plough, stubble grazing, manure contract | herd calendar, transhumance movement logic, herd composition |
```

At the landed commit:

```
$ git show 1c779e4a:corpus/knowledge/culture-material/agrarian-field-system-lexicon.md | sed -n '56p'
| heavy-plough open field | heavy clay, needs drainage | plough team (the critical scarce input), communal herding after harvest | rain + drainage ditches | strips in furlongs, common pasture rights, manor court | furlong, selion, headland, "plough-land" | Bloch (to-verify); `carucate`/`virgate` absent corpus-wide (census §1) |

$ git show 1c779e4a:corpus/knowledge/culture-material/agrarian-field-system-lexicon.md | sed -n '62p'
| agropastoral | fields + pasture + transhumance routes | ploughing peak plus herd calendar; manure contracts | rain + wells | mixed: grain parcels + herd rights; manure-for-stubble exchange | fold, transhumance, stubble-right | standard; manure/night-soil euphemism seam — `textile-technology.md:76` |

$ git show 1c779e4a:corpus/knowledge/culture-material/agrarian-field-system-lexicon.md | sed -n '33p'
- What this entry does not take from its siblings, stated as the partition rule: **food-as-meal, taboo, and fermentation stay in `cuisine-food-lexicon.md`; the granary's containers stay in `vessel-container-lexicon.md`; fiber processing stays in `textile-technology.md`; haulage stays in `transport-mobility-lexicon.md`.** This file owns parcel, implement, water, rotation, harvest, storage-as-bulk, and tenure.
```

* "parcel" ✓ (`:56` "strips in furlongs", `:62` "grain parcels"), "plough" ✓ (`:56` "plough team"), "manure contract" ✓
  (`:62` "manure contracts" / "manure-for-stubble exchange").
* **"stubble grazing" is not a phrase at either cited line.** `:56` says "communal herding after harvest"; `:62` says
  "manure-for-stubble exchange" and "stubble-right" — a *right*, not a *grazing practice*. The cell names a
  practice the anchors do not carry.
* **The row's third column claims "herd calendar, transhumance movement logic" — and `:62`, the row the entry cites,
  already owns both**: the agropastoral row's labour cell reads "ploughing peak plus **herd calendar**", its
  settlement cell reads "fields + pasture + **transhumance routes**", and its vocabulary cell lists "fold,
  **transhumance**, stubble-right". The one-owner split and the neighbour's own row disagree on the same two
  concepts.
* The neighbour's declared ownership line (`:33`) is **water and tenure** as well — "This file owns parcel,
  implement, **water**, rotation, harvest, storage-as-bulk, and **tenure**" — and the §2 cell names neither, while the
  entry's own §8 `:110` says "A herd move claims three things: a route, a **water point** and a **pasture**. Each is
  a rule with an owner" without saying the water/pasture-tenure owner is the agrarian file.

**Smallest fix.** `:31` → `` `agrarian-field-system-lexicon.md:33,:56,:62` `` with the ownership cell
"parcel, plough, water, tenure, stubble right, manure contract"; and either drop "herd calendar, transhumance movement
logic" from the third column or state the difference explicitly ("the herd's own calendar and its route logic, as
distinct from the agropastoral row's `agrarian-field-system-lexicon.md:62`").

*(Cross-reference: `ReviewSec08.md` `P3` reports the dropped water/tenure half and the `:62` "herd calendar"
collision; `ReviewSec01.md` `F1` reports the same "herd calendar" collision; `ReviewSec03.md` reports the `:62` anchor
as holding for §3. The §2-specific addition here is the **"stubble grazing"** phrase, which no sibling report flags —
`grep -l 'stubble grazing'` returns `ReviewSec03.md` and `ReviewSec08.md`, both of which treat the row as *holding*.)*

---

## F8 (LOW-MEDIUM) — the `civilizations/` row is the only row in the table with **no anchor**, and the table header promises one

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:39`:

```
| `civilizations/` regional entries | Mongol, Turkic, Scythian, Sámi, Diné, Inca cases and their warnings | general method only; regional herds are cited, never restated |
```

Every other row in §2 carries a `path:line`; this one carries a bare directory. The table's own header (`:29`) is
"Neighbour **(anchor)**", and the contract's header (`:62`) is "What it owns **(live anchor)**" — so this row fails
the table's own declared shape, and a reader cannot check what the six cases own.

The six named cases **are** individually anchored in the body and all six anchors resolve and support their
sentences at the landed commit:

```
mongol.md:40          → entry:43, entry:164   "Mobile pastoralism, urban production, and documentary administration can coexist." ✓
turkic-steppe.md:148   → entry:131, entry:163   "Do not make pastoral production synonymous with economic isolation." ✓
turkic-steppe.md:193   → entry:131               (chronicle bias) ✓
turkic-steppe.md:194   → entry:131               (reject the nomad→civilised ladder) ✓
scythian-saka.md:70    → entry:131               "Do not equate pastoralism with total absence of farming" ✓
finnic-sami.md:140     → entry:64, entry:165     "Do not map herding status directly onto Sámi identity." ✓
finnic-sami.md:150     → entry:11, entry:118     "Large-scale pastoralism has a history…" ✓
dine-navajo.md:125     → entry:118               "do not stage wool pastoralism as unchanged from remote antiquity" ✓
inca.md:128            → entry:65                "'all wool, all alpaca' is too simple" ✓
```

So the row's *content* is honest — but the row itself cannot be audited, and it also silently absorbs the
`animal-symbolism.md:73,:110` "the Mongol five livestock" case that the contract's candidate set treats as a
separate neighbour.

**Smallest fix.** Give the row real anchors: ``| `civilizations/mongol.md:40`, `turkic-steppe.md:148,:193,:194`, `scythian-saka.md:70`, `finnic-sami.md:140,:150`, `dine-navajo.md:125`, `inca.md:128` | the six regional cases and their warnings | general method only; regional herds are cited, never restated |``.

---

## F9 (LOW) — §2 `:32` states the hunting neighbour's ownership without the `(to-verify)` markers its anchor carries

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:32`:

```
| `hunting-foraging-subsistence.md:36,:116` | wild acquisition; meat-for-crops at a farming edge | the herded counterpart only |
```

`hunting-foraging-subsistence.md:116` reads in full at the landed commit:

```
- **Meat as currency** — meat-for-crops exchange with farming neighbours is a design possibility `(to-verify)`; Kelly's publisher abstract (S034) covers variation in exchange among foragers, but does not specify this exchange partner or medium. The specific Mbuti–farmer exchange case `(to-verify)` — Hart & Hart, unopened; the forager edge of that trade is this entry's, the market register stays at `trade-economy-lexicon.md:3`.
```

The anchor marks the meat-for-crops exchange `(to-verify)` **twice** and names Hart & Hart as unopened; the §2 cell
asserts it flat, with no marker. §2 as a whole carries **zero** `(to-verify)` markers (`grep -c 'to-verify'` over
`:27-39` → 0) while the file carries 11 — so this is a systematic gap in the one-owner table specifically: the table
is the part a writer trusts to point at an owner, and it repeats the neighbour's hedged claim as settled.

The row's "wild acquisition" claim at `:36` is **exact** — "the organism or material is not planted, herded or owned
as a standing crop" — and this is the cleanest row in the table.

**Smallest fix.** `:32` → "meat-for-crops at a farming edge `(to-verify)`" (matching the anchor's own marker).

---

## What HOLDS (so the author lane does not re-open settled ground)

1. **Every `path:line` anchor in §2 resolves at the landed commit**, and every neighbour file the table cites is
   byte-identical between base `4ad2683` and landed `1c779e4a`:
   ```
   $ git diff --stat 4ad2683 1c779e4a -- corpus/knowledge/culture-material/hunting-foraging-subsistence.md \
       corpus/knowledge/culture-material/agrarian-field-system-lexicon.md \
       corpus/knowledge/culture-material/cuisine-food-lexicon.md \
       corpus/knowledge/culture-material/transport-mobility-lexicon.md \
       corpus/knowledge/culture-material/trade-economy-lexicon.md \
       corpus/knowledge/culture-material/textile-technology.md \
       corpus/knowledge/linguistics/semantic-fields-lexicon-building.md \
       corpus/knowledge/culture-material/fire-fuel-light.md corpus/knowledge/civilizations/
   (empty output)
   ```
   No line reference in §2 has drifted between base and landed.
2. **`:37` (semantic-fields) is exactly right and is the model row.** `:70` = "Pastoral wealth vocabulary (herd-age,
   herd-color, herd-condition terms) indexes property systems…" ✓; `:105` = "| steppe pastoral | subsistence (herd
   wealth), kin (clan), war (raid), landscape (pasture) | …" ✓; and the third column ("the herd facts the field
   lexicalizes (§5 supplies inputs)") is realised at `entry:71` and §5's five-row table. The `civilizations/` row's
   six cases and the `trade-economy-lexicon.md:69` row ("cattle-root money words") are likewise exact.
3. **`:38`'s neighbour half is exact.** `fire-fuel-light.md:37` = "| Dried dung | the herds' output, and therefore
   the fields' | a hot, fast, smoky fire | a real trade-off against manure; fuel-poor pastoral cultures pay for it in
   soil" — "dung as fuel versus manure" ✓ (the defect in that row is the *third* column, F4).
4. **Every S-id in the entry (S048–S069, 22 rows) resolves to a `corpus/SOURCES.md` row whose `scope` covers its
   entry use** — checked row by row at the landed commit (S048 typology/species portfolio; S049 labour-wealth +
   tenure; S050 culling profile + species order; S051 SPR review; S052 Nuer cattle idiom; S053 the cattle-complex
   label as an etic construct; S054 the open-pasture parable; S055 Ostrom's 2009 §4E; S056 nomadic non-autarkic;
   S057 publisher description only; S058 WoDaaBe movement; S059 the Swedish earmark register; S060 risk management +
   five snouts; S061 yak on the plateau; S062 the ger's portability; S063 camel husbandry as a named skill; S064 the
   ETCSL disputation as a literary fact; S065 the *peku-* gloss, lexical only; S066 EA004 dependence bins; S067 horse
   origins; S068 Andean camelid domestication; S069 the transhumance inscription record). The rows' own scope
   caveats are honoured at the point of use (S057 at `:187`, S062 at `:47`, S063 at `:61`, S065 at `:79`, S069 at
   `:49`). The row-level URL/Gate questions belong to the `ReopenS0xx` seats and are **not** re-litigated here.
5. **Canon hygiene is clean.** §2 asserts no in-world truth (`sed -n '31,39p' | grep -c 'must\|shall\|is true\|always'`
   → 0); §12 is explicitly NON-CANON (`entry:169`); §15 hands every canon decision to lore-shokunin and marks the
   lore intake as pending (`entry:199`).
6. **The C-claim machinery reproduces green from the landed tree** (so the defects above are defects of the §2
   *content*, not of the claim's measurement):
   ```
   $ python3 -B reports/round-28/readme/sweep.py
   rows 226 files 226
   missing_from_index 0 []
   topic_mismatch 0 []
   orphan_rows 0 []
   header_drift {}
   totals_line 226 totals_ok True
   footer_findings [] footer_ok True
   readme_sha256 3ea247db6ae3719f1391a45072f3169b756a5e756d8cec609efa46ffa675d78c
   rc=0
   ```
   culture-material = 28 of 226 (base 225/27), and no sibling lane owns the herding register (the declared
   word-bounded topic sweep hits only this entry; the unbounded form's single hit is `writing-media-surface-economy.md:3`
   "sherd", a non-owner — reported independently by `CriticCoverageCount.md` and `ReviewHead.md` `A1`).

## Residual risk and verification gaps

* **No URL was opened here**, per seat scope. Every S-id judgement above is a scope/anchor/support check against the
  landed `corpus/SOURCES.md` row; the rows' own accuracy is the `ReopenS0xx` seats' verdict.
* I did not attack the "what it owns" prose against the neighbour files *beyond* the cited lines: a neighbour file
  may own a concept at a line the table does not cite (F1, F3, F7 are all instances of that). A full ownership sweep
  of all nine neighbours was not performed — the nine cited lines were the contract of the check.
* The "never developed in the body" measurement (F4) is a lexical one: a synonym would not be found. The body does
  carry near-neighbours (`:88` "curd/butter chain", `:89` "shorn or plucked", `:47` "species mix"), so the finding is
  that the *stated* terms are absent, not that the topics are wholly absent.
* F5's "lead sentence" and "header drift" are contract-conformance findings against `.ufo/waves/round-50/build/
  ReviewEntryContract.md:62`. If the author lane treats that contract as advisory rather than binding, F5 downgrades
  to LOW; F1, F2, F3, F6, F7 do not depend on the contract and stand on the landed bytes alone.

## Commands used (reproducible from a private clone)

```
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/ReviewSec02-ab12
git -C /tmp/ReviewSec02-ab12 checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:<path>
git -C /tmp/ReviewSec02-ab12 diff --stat 4ad2683 1c779e4a -- <neighbour paths>      # empty
python3 -B /tmp/ReviewSec02-ab12/reports/round-28/readme/sweep.py                   # rc 0
```

Author-lane advice, not admission.
