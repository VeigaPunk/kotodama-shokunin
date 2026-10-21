# ReviewSec10 — falsify attack on §10 (Ritual, myth and symbol of the herd) of the landed C entry

**Item attacked:** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` §10 (lines 133–145), plus the entry-wide in-corpus `path:line` anchors and S-ids that §10 depends on, checked against the row scopes/teaches in `corpus/SOURCES.md`.
**Landed commit read:** `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
**Method:** private clone `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/r50sec10/clone && git -C /tmp/r50sec10/clone checkout -q 1c779e4a…` (read-only; deleted after reading). Every byte quoted below was read at the landed commit in that clone, never from the lane working tree. No lane file was edited except this report; no `git add/commit/stash/checkout/reset`, no mutating `jj` command, no URL was re-opened (URL seats own that; the S064 row was checked as filed).
**Scope note:** the lane working tree carries later uncommitted edits to the same file; those were **not** assessed and are not relied on here. The verdict is against the landed bytes only.
**Tools:** no installs were needed — `git`, `grep`, `awk`, `sed`, `python3` from the base system.

---

## Verdict

**PARTIAL.**

**Holds (verified in-lane):**
- All six in-corpus anchors §10 cites resolve to existing lines at `1c779e4a` and each supports the sentence that cites it: `ritual-liminality.md:63`, `sacred-kingship-mythic-charter.md:65`, `symbolism-synthesis-method.md:69`, `celestial-symbolism-calendars.md:28`, `animal-symbolism.md:73,:110`. No dangling, out-of-range or phantom anchor.
- All **29** body line-anchors across **18** files resolve; the head's in-corpus anchor list (`:6`) is a superset of the body's (no body anchor is missing from it).
- Every anchored file is byte-identical between base `4ad2683` and landed `1c779e4a` (`git diff --stat 4ad2683 1c779e4a -- corpus/knowledge` → only the new entry file, +199 lines), so the header's "re-read at `4ad2683`" is still valid at the landed commit.
- All **22** S-ids in the entry resolve to rows whose `scope`/`teaches` support the use; the round's own acceptance check passes: `C_SID_UNRESOLVED 0` (all 22 rows carry `used-by = corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`).
- §10's two S064 rows are scope-honest: S064's scope is "an emic literary representation, not a description of pastoral practice", and `:139`/`:140` label the count "a literary fact before it is a ritual one" and the ranking "a theological ranking, not evidence of practice" — the row's own teaches ("nightly herd count and tally-stick; Sheep and Grain as rival sisters; the ranking is theological") is carried faithfully. (`ReopenS064.md` independently confirms both entry citations hold.)
- Canon hygiene in §10 holds: the section decides no in-world fact, and §12's example is banner-flagged NON-CANON with canon routed to lore-shokunin.
- The gap premise reproduces exactly at base: 0 filename owners, 0 word-bounded topic owners, and the un-bounded form's single hit is `writing-media-surface-economy.md:3` ("sherd"), as `:4` states; `find corpus/knowledge -name '*.md' | wc -l` → 225 at base, 226 landed; culture-material 27 → 28; `python3 -B reports/round-28/readme/sweep.py` → `rows 226 files 226 / topic_mismatch 0 / exit 0`; README row sits in filename order between `music-instrument-lexicon.md` and `ritual-garments.md`.

**Broken (6 findings):**

| id | severity | locus | defect |
|---|---|---|---|
| **F1** | MODERATE | `:142` | the "Sacrifice economy" mechanism is an **unsourced factual claim**; the row also re-uses the *hunt* register's kill-rite anchor for a herding register, colliding with the corpus's own routing |
| **F2** | MODERATE | `:137–143` | coverage: §10 routes **none** of the three corpus-owned herding ritual registers (flora/hazard plants, omen-reading, the herd's taboo layer) |
| **F3** | MODERATE | `:137–143`, `:173–187` | calibration: §10 carries **no status code anywhere** and §13 has **no bank row** for S064 or for three of §10's five registers |
| **F4** | MODERATE | `:141` | the Shepherd-king Anchor cell **contradicts the line it cites**, and the row imports a settled-state office into a herding register with no scope note and no carry-over of the corpus's Frazer caution |
| **F5** | MODERATE | `:8` | `- couples:` under-declares §10's own dependencies (two cited myth-symbol files are not coupled; §2's boundary table has zero myth-symbol rows though §10 uses five) — QUALITY criterion 3 |
| **F6** | LOW | `:143` | "milk and river figures" mis-transcribes the anchor's "**milky**/river figures" (the Milky Way) and collides with the entry's own dairy register |
| **F7** | LOW | `:135` | "One flock" against the entry's own "herd" and against a mixed-species register |

Smallest fixes are given per finding. **Author-lane advice, not admission.**

---

## F1 (MODERATE) — §10's sacrifice-economy mechanism is an unsourced factual claim, and the row re-uses the hunt register's kill-rite anchor

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:142` (landed):

```
| Sacrifice economy | offerings drawn from the herd's surplus males | an animal taboo implies a rite (`symbolism-synthesis-method.md:69`) |
```

Three defects in one row.

**(a) The Mechanism cell is an uncited empirical claim.** "offerings drawn from the herd's surplus males" asserts how real herding societies make offerings. It carries **no S-id, no in-corpus anchor, and no `(to-verify)` marker**. QUALITY criterion 1 (`corpus/QUALITY.md:5-8`) is explicit: *"every factual claim carries a cited, checkable source … A claim the author cannot verify is marked `(to-verify)` inline — never laundered into assertion."* The rest of the entry is disciplined about this (`:50` "stored feed replaces movement `(to-verify)`", `:65` "puna pasture plus valley exchange `(to-verify)`", `:75` "a sameby may hold one" is at least scoped to Sweden) — §10's row 142 is the one place where a real-world practice is stated flat. There is also no corpus support to fall back on:

```
$ grep -rn -i "surplus male\|surplus males" corpus/knowledge --include=*.md
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:142:   (this line only)
```

So the claim is neither cited nor findable anywhere else in the corpus — a reader cannot check it.

**(b) The Anchor cell is the hunt register's kill-rite anchor, re-used for a different rite.** `symbolism-synthesis-method.md:69` reads:

```
- **Prey apologetics**: a hunting culture that keys a prey animal symbolically generates apology and release rites for the kill — the Circumpolar bear ceremonial is the classic case (Hallowell 1926). An animal taboo implies a rite; write both or neither.
```

The corpus's own hunting register owns that anchor for the hunt case:

```
corpus/knowledge/culture-material/hunting-foraging-subsistence.md:64  | `myth-symbol/animal-symbolism.md` | prey-animal signs, bear ceremonialism, forest register (`:53`,`:114`) | the ecology and kill-sharing; the rite itself stays there |
corpus/knowledge/culture-material/hunting-foraging-subsistence.md:145 | Taboos a prey animal | forest register + kill-rite pair | §8; `symbolism-synthesis-method.md:69` |
```

The pastoralism entry takes the same anchor for a *herding* "sacrifice economy" and says nothing about the transfer.

**(c) The row collides with the corpus's routing rule for sacrifice.** `hunting-foraging-subsistence.md:41`:

```
Failures are diagnostic: a **garden plot** fails 1–2 (agrarian); … a **totem or sacrifice** passes the animal but not production (myth-symbol); …
```

By the corpus's own rule, a sacrifice is myth-symbol's business, and the hunt register hands the kill-rite itself to `animal-symbolism.md` (`:64`). §10 keeps "Sacrifice economy" inside the production register with no boundary sentence. §2's one-owner table (`:31-39`) has no myth-symbol row at all, so the boundary the corpus expects is simply absent.

**Smallest fix:** either (i) cite the mechanism — a real row for pastoral sacrificial practice, with tier and scope — or mark it `(to-verify)`; and (ii) add a one-clause boundary to the row, e.g. "the kill-rite itself is `animal-symbolism.md`'s; this entry owns the herd side of what is offered", plus a §2 row routing sacrifice/kill-rites to `animal-symbolism.md` and to `hunting-foraging-subsistence.md:145` for the taboo→rite pair.

---

## F2 (MODERATE) — §10 routes none of the three corpus-owned herding ritual registers

§10 is the entry's ritual/myth/symbol section and it owns "the herd's ritual ledger" (`:12`, `:199`). Three registers the corpus already owns — and that the *sibling* production register (hunting) hands off explicitly — are absent from §10 and from §2's table.

**(a) Flora and hazard plants — `myth-symbol/plant-symbolism.md`.** The corpus's craft rule for the flora register is subsistence-shaped, which makes it the pastoral register's core:

```
corpus/knowledge/myth-symbol/plant-symbolism.md:19  - **Craft maxim: the flora register is chosen by subsistence, not by taste.** A culture's symbolic plants are overwhelmingly its *staple* plants and its *dangerous* plants — the two sets its labor calendar and its mortality are organized around. Design sequence: fix the staples, then the hazards, th…
corpus/knowledge/myth-symbol/plant-symbolism.md:65  | Osun-Osogbo Sacred Grove | Yoruba (Osogbo, Nigeria); UNESCO list 1118, inscribed 2005; … | the grove as *living parish whose police force…
```

For a herd, "dangerous plants" is a mortality register, not a decorative one, and the hunting register already couples this file (`hunting-foraging-subsistence.md:19` → `myth-symbol/plant-symbolism.md` `:19,:65`). The pastoralism entry never mentions plant-symbolism, and `grep -c "plant-symbolism" corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` → **0**.

**(b) Omen-reading — `myth-symbol/divination-omen-systems.md`.** The corpus owns the omen list as a genre, with a terrestrial/weather row:

```
corpus/knowledge/myth-symbol/divination-omen-systems.md:86  | 9 | Terrestrial omen lists | births, locusts, weather, city events | if-P-then-Q compendium, thousands of entries | scribe-scholar | *Šumma ālu* … | the compendium as a genre: omen literature is a *database* wit…
corpus/knowledge/myth-symbol/divination-omen-systems.md:133  - **The omen list as a data genre.** … the omen archive is the most plausible pre-modern *data* institution a fictional world can have, …
```

Rain, drought, locust and herd-sign omens are the classic pastoral divination register, and the entry's own §3 makes timing-by-sign the production logic ("movement is the production logic, timed to vegetation and season (S058)"). `grep -c "divination-omen\|omen" …pastoralism-animal-husbandry.md` → **0**. §10 has no omen row and no hand-off.

**(c) The herd's taboo layer.** §10's "Sacrifice economy" row is the only place the herd's ritual prohibitions could surface, and the corpus's owners are adjacent and already loaded: `animal-symbolism.md:69` (pig taboo), `:72` (royal limits on slaughter), `:53` (bear ceremonialism), `culture-material/cuisine-food-lexicon.md:86` (milk+meat law — which the entry already routes to at `:33`), and `linguistics/politeness-taboo-euphemism.md` + `linguistics/taboo-strata-lifecycle.md`, which the hunting register couples for the taboo register (`hunting-foraging-subsistence.md:19`). The entry's §5 does carry the Sámi earmark (`:77`) and its §11 step 8 promises "each taboo written with its rite" (`:158`) — but §10 contains **no taboo row and no taboo owner**, so step 8's check has nothing to check against inside §10.

**Smallest fix:** add two rows to §10's table — "Sacred and dangerous plants (herd mortality and forage reserve) → `plant-symbolism.md:19,:65`" and "Omen reading (weather, locust, herd signs) → `divination-omen-systems.md:86,:133`" — and one "Herd taboos (which animal is not killed, not milked, not herded) → `animal-symbolism.md:69,:72` + `cuisine-food-lexicon.md:86`", each with the boundary "the entry owns the herd side; the rite itself stays with the myth-symbol owner" and the matching §2 rows.

---

## F3 (MODERATE) — §10 carries no calibration status, and §13 has no bank row for S064

`corpus/QUALITY.md:9-12` (criterion 2): *"**Calibration** — every framework entry names its status: mainstream / contested / discredited, with the reason. Pop-mythography (Campbell-as-universal, strong Whorf, glottochronology, Frazerian evolutionism) must be flagged as such on first use."*

§10's table (`:137-143`) is the entry's fifth register table and the only one with **no status column at all** — compare:

- §4 species table (`:57-67`) — a `Calibration` column with `**C**`, `**R**` codes;
- §8 tenure table (`:112-116`) — a `Status` column with `**R**`/`**B**` codes;
- §13 calibration bank (`:177-187`) — nine rows, each with a code.

§10's five rows carry codes nowhere; the third column (headed "Anchor") holds free-text use notes ("the count is a literary fact before it is a ritual one", "a theological ranking, not evidence of practice", "self-presentation, not administration", "a subsistence input to sky lore, not a creed"). Two of those five are scope-sensitive claims about a real source (S064) and the "not a creed" row is a substantive claim about how sky figures function for pastoralists — none is coded, and none appears in §13.

**§13's bank covers ten of the entry's twenty-two S-ids and no §10 register.** The bank rows name S048, S050, S051, S052, S053, S054, S055, S056, S057, S067 — and **not S064**, which is the source §10 leans on twice and the only tier-A literary dataset in the section. The sibling hunting register's bank covers eight of its own twelve S-ids, including its tier-A ones, so the house practice is that a scope-limited tier-A source gets a bank row.

**Smallest fix:** add a `Status` column to §10's table (R/C/B/H per `calibration-registry.md:35-39`) and one §13 bank row for S064 — e.g. "A literary disputation is evidence of herding accounting | B — S064 is an emic composition, not a description of practice; use it as a design register, cite it as literature" — plus one for the shepherd-king row if F4 is fixed by keeping the row.

---

## F4 (MODERATE) — the Shepherd-king Anchor cell contradicts the line it cites, and the row transfers a settled-state office with no scope note

`…:141` (landed):

```
| Shepherd-king | the ruler as shepherd, audited by the gods (`sacred-kingship-mythic-charter.md:65`) | self-presentation, not administration |
```

The cited line, in full (`corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:65`):

```
| 3 | **delegation** | the ruler is the god's tenant, servant, or shepherd — an office, not a person | Mesopotamian kingship: the king as *sipa*, shepherd, with his rule audited by omens and the gods' assembly (Jacobsen 1976; Frankfort 1948); Chinese Mandate of Heaven (tianming), where the mandate is *withdrawn* from the corrupt (`corpus/knowledge/culture-material/era-periodization-models.md:67,69`) | the office can be vacated by its grantor: this channel makes deposition a theological act, and it needs a body of interpreters (priests, diviners, historians) |
```

Two problems.

**(a) The Anchor cell contradicts the anchor.** "self-presentation, not administration" is a use note; but the cited row's own cost column says this channel "needs a body of interpreters (priests, diviners, historians)". Read as an assertion about the anchor, the cell is the opposite of what the line says. As a use rule it is defensible; but in a column otherwise used for *what the cited source licenses*, the reader gets the reverse of the source.

**(b) The scope is not carried over.** The attested exemplars at `:65` are a settled agrarian empire's office — the Mesopotamian king as *sipa* and the Chinese Mandate of Heaven. §10 imports that office into "Ritual, myth and symbol of **the herd**" without a scope note. The corpus is explicit that this material carries a comparative-mythology caution that a new register should inherit:

```
corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:179  - **"Divine kingship" is a category with a history, not a type.** It was built by Frazer's comparative program, Hocart's ritual-origin thesis, and Seligman's Egypt–Africa frame; …
corpus/knowledge/myth-symbol/myth-ritual-theories.md:85  | Myth-ritual (Frazer, Hooke) | myth = degraded shadow of ritual | collapsed; Burkert's modest revival stands | rites without texts, divine kingship, mysteries, festival calendars, ritual-decay quarrels | Frazerian universal dying-god; hero-fits-all-22-points |
```

Neither caution reaches §10 (criterion 2 names Frazerian evolutionism as a must-flag case), and §13 has no row for it (F3).

**Smallest fix:** change the Anchor cell to what `:65` actually licenses — e.g. "the office, not the person; the channel ends in a body of interpreters (`sacred-kingship-mythic-charter.md:65`)" — and add a scope clause to the Mechanism cell: "a settled-state office (Mesopotamian *sipa*, Chinese *tianming*) imported as a design register, not an attested herding one". If the Frazerian comparison is intended, carry the caution from `sacred-kingship-mythic-charter.md:179` and `myth-ritual-theories.md:85` into §13.

---

## F5 (MODERATE) — `- couples:` under-declares §10's own dependencies (QUALITY criterion 3)

`corpus/QUALITY.md:13-15` (criterion 3): *"**Coupling** — the `- couples:` line names the systems/files the entry connects. An entry that couples nothing is reference, not craft; it must say so."*

`…:8` (landed) names three myth-symbol owners:

```
myth-symbol — `animal-symbolism.md`, `sacred-kingship-mythic-charter.md`, `ritual-liminality.md` (own the herd's signs, the shepherd-king office and sacrifice typology)
```

But §10 cites **five** myth-symbol files: `animal-symbolism.md` (`:145`), `sacred-kingship-mythic-charter.md` (`:141`), `ritual-liminality.md` (`:135`), `symbolism-synthesis-method.md` (`:142`, and §11 step 8 at `:158`), `celestial-symbolism-calendars.md` (`:143`). Per-file count of the couples line vs. §10:

```
animal-symbolism.md                    couples:1 body§10:1
sacred-kingship-mythic-charter.md      couples:1 body§10:1
ritual-liminality.md                   couples:1 body§10:1
symbolism-synthesis-method.md          couples:0 body§10:1
celestial-symbolism-calendars.md       couples:0 body§10:1
```

The two uncoupled files are load-bearing: `:142` and `:143` are the only anchors for the sacrifice-economy and sky-figures rows, and `:158` builds step 8 of the decision table on `symbolism-synthesis-method.md:69`.

The sibling register entry, which faces the same myth-symbol wall, couples all four of its own and names the line anchors in the same clause (`hunting-foraging-subsistence.md:19`):

```
myth-symbol — `../myth-symbol/animal-symbolism.md` + `../myth-symbol/symbolism-synthesis-method.md` + `../myth-symbol/plant-symbolism.md` + `../myth-symbol/celestial-symbolism-calendars.md` (own the prey-animal sign, the kill-rite rule, the flora register and sky-figure assignment — `:53,:114`,`:47,:69`,`:19,:65`,`:28`)
```

Second, **§2's "One-owner boundary" table (`:31-39`) contains zero myth-symbol rows** even though §10 hands five anchors across the myth-symbol partition and `:199` claims the entry "hands … the animal sign … to their owners (§2, §15)". The two clauses point at different places: the animal-sign hand-off is stated in §2's prose but has no §2 table row, and the couples line lists owners the table never names.

**Smallest fix:** extend the couples clause to all five myth-symbol files with their line anchors, and add the myth-symbol rows §10 actually needs to §2's table — `animal-symbolism.md:73,:110` (herd signs), `sacred-kingship-mythic-charter.md:65` (shepherd-king office), `ritual-liminality.md:63` (sacrifice typology), `symbolism-synthesis-method.md:69` (taboo→rite rule), `celestial-symbolism-calendars.md:28` (sky figures) — plus, if F2 is taken, `plant-symbolism.md:19,:65` and `divination-omen-systems.md:86,:133`.

---

## F6 (LOW) — "milk and river figures" mis-transcribes "milky/river figures"

`…:143` (landed):

```
| Sky figures | pastoralists read milk and river figures (`celestial-symbolism-calendars.md:28`) | a subsistence input to sky lore, not a creed |
```

The anchor reads *"pastoralists on **milky**/river figures"* (`corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:28`), i.e. the Milky Way and rivers. The dropped "y" turns a sky figure into a dairy product — and "milk" is already a loaded term in this same file (`:65` "the only domesticated ungulates"; `:88` "butter is the main milk product in most places (S061)"; `:2` "the herd's ritual ledger"). A reader of `:143` alone gets a register where herders read *milk* figures.

**Smallest fix:** "pastoralists read milky-way and river figures (`celestial-symbolism-calendars.md:28`)" — and quote the anchor's phrase as "milky/river figures".

---

## F7 (LOW) — "One flock" against the entry's own "herd" and a mixed-species register

`…:135` opens "**One flock** is ledger, offering and metaphor at once". The entry's own scope is a mixed-species herd: §4 (`:59-65`) lists cattle, sheep/goat, camel, horse, yak, reindeer, llama/alpaca; §2 and §15 say "herd" throughout ("the herd's ritual ledger", `:199`); §5 is "Herd lexicon"; §10's own title is "…of the herd"; and the S064 source the row leans on is a *sheep*-and-grain poem specifically. "Flock" is the sheep-only word and drops the register's own multi-species point.

**Smallest fix:** "One herd is ledger, offering and metaphor at once" (and "one flock of sheep" only where the S064 poem is the subject).

---

## Notes (not findings)

- The head's in-corpus anchor list (`:6`) declares lines the body never cites — `agrarian-field-system-lexicon.md:80` and `hunting-foraging-subsistence.md:117,:137-146,:170-172` (the sibling's §9 decision table and §12 micro-example, i.e. the templates this entry modelled). The header says "each re-read", so this is a read-list convention the sibling entries also use, not a defect — but the list is not a cite-list, and an auditor should not read it as one.
- `corpus/SOURCES.md:93` (S064) mis-labels its own anchor locator: "lines 130–142 (Grain's third speech)" — per `ReopenS064.md`, the capture shows 130–142 is the closing paragraph of Grain's **second** speech. The §10 row's *use* of S064 is unaffected (both entry citations hold), but §10 is the section that most depends on this row, so the descriptor error sits directly under it. Cross-reference, not a duplicate of that seat's finding.
- The S062 "ger" row and the S063 "Bedu" row are used in §3/§4 and are in scope for the "living practice" flag at `:189`, which lists "Sámi" and "Tibetan" as unqualified living-practice peoples while `:77`/`:116` scope the Sámi material to Sweden. Cross-reference with `ReviewSec13.md`'s F2.

## Verification gaps and residual risk (stated honestly)

- No URL was re-opened from this seat, so every S-id check here is a **row-text** check (scope / teaches / anchor locator / used-by / status / tier), not a re-read of the source. Where a row's own `teaches` field is the only support (S064's "nightly herd count and tally-stick", "rival sisters"), the check is that the entry's sentence stays inside what the row asserts — which it does.
- Whether the corpus's `writing-media-surface-economy.md` §4 cost ladder and `numerals-and-measures.md:110` (khipu) would license a stronger "books" register for §10 is an **author-lane design call**, not a defect I can settle; F1(a) and F2 are stated as missing citation/hand-off, not as a mandate to rewrite the metaphor.
- The "Sacrifice economy" row may be intended as a **design rule** rather than an ethnographic claim; if so, it needs the same treatment the entry gives its other heuristics — the working-tree draft adds a blanket "**H**" statement for uncited cells. If that convention is adopted at the landed file, F1(a) reduces to "mark the cell H", and F3's status column becomes the consistent home for it. On the landed bytes neither exists.
- I did not assess the uncommitted edits now present in the lane working tree; §10's text may already have moved. The findings above are anchored to `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` line numbers.
- No lane mutation: no `git add/commit/stash/checkout/reset`, no mutating `jj` command, no writes outside this report; `/tmp/r50sec10/clone` was removed after reading.

**Report:** `.ufo/waves/round-50/falsify/ReviewSec10.md`
