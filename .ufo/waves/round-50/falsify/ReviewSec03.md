# ReviewSec03 — attack on §3 "Pastoral systems typology" table and the political second axis

Seat: `KotodamaR50-2.ReviewSec03-21` (leaf; no delegation, no background jobs).
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`),
lane `kotodama-shokunin` (/home/vgpnk/Projects/shokunin/kotodama-shokunin).
All lane bytes read from a private clone (`git clone -q --shared <lane> /tmp/kr50sec03-4180537 && git checkout -q 1c779e4`),
never from the working tree; `GIT_CEILING_DIRECTORIES=/tmp`. No lane file edited, no jj/git index mutation in the lane,
no install, no delegation. Clone deleted after the run. No source re-opened (other seats own URL re-opening);
the URL-bearing S-ids were checked **against the registry rows' own scope/anchor/teaches fields**, per the ticket.

Slice attacked: `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` **§3, lines 41–53**
(heading, framing sentence, the five-row typology table, the political-axis sentence), plus the registry rows
the slice leans on (`corpus/SOURCES.md` S048, S057, S060, S062, S069) and the two in-corpus anchors the slice cites.

## Verdict: **PARTIAL** (the table's citations hold; the table's *calibration* and its *row set* do not)

Every S-id the slice cites resolves to a registry row whose `scope`/`anchor`/`teaches` field supports the sentence
it is attached to, and the one in-corpus anchor that carries a *load-bearing* claim (`agrarian-field-system-lexicon.md:62`)
is exactly right. But the slice fails on three counts that are the lane's own admission bar:

1. **The table has no calibration status at all** — QUALITY criterion 2 requires every framework entry to name its
   status. The sibling tables in the same file *do* have status columns (`:57` "Calibration", `:112` "Status");
   §3's has none, and §13's bank contains no row covering the typology itself. Eight of the twenty cells in §3
   assert a fact with **neither** a citation nor `(to-verify)` — QUALITY criterion 1 ("never laundered into
   assertion") is broken for those cells.
2. **The typology's row set contradicts the entry's own topic line and README row.** `:3` and `corpus/README.md:297`
   advertise **four** mobility systems (nomadic, transhumant, agro-pastoral, enclosed) — the exact four S048's
   `teaches` field registers. The table delivers **five** rows, the fifth being "Semi-nomadic", which no opened
   source defines and which no calibration row covers. `:153` (§11 build step 3) then instructs the builder to
   choose among **five**. The register's advertised scope and its build order disagree with each other.
3. **The political second axis is a single sentence with no design rule and no canon-safe operationalisation.**
   `:53` names three political types from a tier-B publisher description and then stops; the types never reach
   the decision table (§11), the worked example (§12) or the calibration bank (§13), and the entry's own
   boundary table (§2, nine rows) and scope line (`:12`) do not mention political organisation at all.

The "smallest fix" set below is author-lane advice, not admission.

---

## F1 (HIGH) — §3 carries **no calibration status**, and eight cells assert facts with neither a citation nor `(to-verify)`

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:45` (landed bytes) — the table header:

```
| System | Mobility | Settlement | Labour | Risk strategy |
```

Five columns, **no status column**. Compare the entry's own sibling tables:

* `:57` — `| Species | Ecology | Products | Mobility and labour | Calibration |`
* `:112` — `| Model | Proposition | Status | Design use |`

Both carry a per-row status cell. §3, the register's *primary typology*, carries none. QUALITY `corpus/QUALITY.md:9-12`
(criterion 2) says: *"every framework entry names its status: mainstream / contested / discredited, with the reason."*
§3 is a framework entry; nothing in the file names its status. The §13 bank (`:177-189`) has nine rows, and the
closest one (`:179`, "Nomadism is a rung on a ladder") calibrates the *ladder* claim, not the *typology*:
`awk 'NR>=177 && NR<=190' <entry> | grep -in "typolog\|semi-nomad"` → **no match**. The build seat's own §3 draft
had exactly this column and filled it — `.ufo/waves/round-50/build/ScribeSec03Typology.md:12`:

```
| System | Mobility pattern | Settlement | Labour | Risk strategy | Status / cite |
```

and `:15` gave the Semi-nomadic row `H — design dial between rows 1 and 3; no opened source defines the term (to-verify)`.
**That column was dropped at integration.** The scribe's own closing note (`:65`) records the reason it mattered:
*"Typology rows (semi-nomadic, vertical/horizontal split, enclosed ranching as a pastoral class) are design
categories. None is claimed as an opened-source classification beyond Aryal's three-way list."* Without the column,
that caveat no longer travels with the rows.

Cell-by-cell audit of the twenty content cells of the five-row table (script over the landed bytes; `cite` = the
cell contains `(S0nn)` or a `` `path.md:line` `` anchor, `to-verify` = the cell contains the literal marker):

| line | row | cell | cite | `(to-verify)` |
|---|---|---|---|---|
| 47 | Nomadic | Mobility "household and herd move on a forage cycle" | no | no |
| 47 | Nomadic | Settlement "the ger is "light enough for nomads to carry" (S062)" | yes | no |
| 47 | Nomadic | Labour "household herding; splitting by species and age" | **no** | **no** |
| 47 | Nomadic | Risk "species mix and movement are the hedge (S060)" | yes | no |
| 48 | Semi-nomadic | Mobility "part of household travels; a base is held" | **no** | **no** |
| 48 | Semi-nomadic | Settlement "village or winter camp plus satellite camps" | **no** | **no** |
| 48 | Semi-nomadic | Labour "base keeps the old, young and crop plot `(to-verify)`" | no | yes |
| 48 | Semi-nomadic | Risk "the base is store and drought fallback" | **no** | **no** |
| 49 | Transhumant | Mobility "…horizontal in plains or plateaus, vertical in mountains (S069)" | yes | no |
| 49 | Transhumant | Settlement "two bases; the route is infrastructure" | **no** | **no** |
| 49 | Transhumant | Labour "a herd party travels, households stay; herd splitting (S048)" | yes | no |
| 49 | Transhumant | Risk "route access is the exposure" | **no** | **no** |
| 50 | Agro-pastoral | Mobility "short moves on stubble and fallow, return to village" | **no** | **no** |
| 50 | Agro-pastoral | Settlement "fixed village with fields" | **no** | **no** |
| 50 | Agro-pastoral | Labour "herd calendar collides with the ploughing peak (`agrarian-field-system-lexicon.md:62`)" | yes | no |
| 50 | Agro-pastoral | Risk "crop and herd buffer each other" | **no** | **no** |
| 51 | Enclosed / ranching | Mobility "fenced, individually owned land (S048); stored feed replaces movement `(to-verify)`" | yes | yes |
| 51 | Enclosed / ranching | Settlement "ranch headquarters" | **no** | **no** |
| 51 | Enclosed / ranching | Labour "hired stockmen" | **no** | **no** |
| 51 | Enclosed / ranching | Risk "market and tenure exposure" | **no** | **no** |

**Eight cells** (`:47` Labour, `:48` Mobility/Settlement/Risk, `:49` Settlement/Risk, `:51` Settlement/Labour/Risk —
and, counting the Agro-pastoral pair, ten) assert content with neither a source nor `(to-verify)`. QUALITY
`corpus/QUALITY.md:5-8` (criterion 1): *"A claim the author cannot verify is marked `(to-verify)` inline — never
laundered into assertion."* The provenance gate cannot see this: `python3 -B tools/gates/provenance-audit.py
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` → `INFO to-verify-count: … 11 mark(s) on 11
line(s) / findings=0` — the gate counts marks as inventory, not as coverage of cells.

Four `(to-verify)` markers that the build seat had put on exactly these cells were dropped at integration
(diff of `.ufo/waves/round-50/build/ScribeSec03Typology.md:14-19` against the landed `:47-51`):

| draft row | draft `(to-verify)` on | landed |
|---|---|---|
| Nomadic (`:14`) | "division by age and sex is culture-specific" | `:47` Labour now reads "household herding; **splitting by species and age**" — the claim was *reworded* and the marker dropped with it |
| Semi-nomadic (`:15`) | "no opened source defines the term"; "herd party travels" | `:48` — both gone; only the Labour cell keeps one marker |
| Transhumance, vertical (`:16`) | "two bases: valley village and summer hut"; "vertical/horizontal split itself" | `:49` — both gone |
| Transhumance, horizontal (`:17`) | "fixed latitudinal or plain-to-plain droving on fixed routes, over long distance" | `:49` — gone; the two rows were also merged, so the horizontal/vertical distinction is now carried by a single S069 citation (that part *is* supported — see F5) |

The Nomadic Labour cell is the sharpest instance: the draft's "division by age and sex is culture-specific
`(to-verify)`" became the flat assertion "splitting by species and age", which is a *different, stronger* claim
and is now unsupported. (`ReopenS060.md` independently flags the same cell from the source side: "the Labour cell
"household herding; splitting by species and age" (no citation…)".)

**Smallest fix.** Add the build seat's own column back, one cell per row, and mark the unsupported cells:

```
| System | Mobility | Settlement | Labour | Risk strategy | Status / cite |
|---|---|---|---|---|---|
| Nomadic | … | … | household herding; splitting by species and age `(to-verify)` | … | B — FAO degrees of movement (S048); ger is a Mongol case (S062), not a universal |
| Semi-nomadic | part of household travels; a base is held `(to-verify)` | village or winter camp plus satellite camps `(to-verify)` | base keeps the old, young and crop plot `(to-verify)` | the base is store and drought fallback `(to-verify)` | H — design dial between rows 1 and 3; no opened source defines the term `(to-verify)` |
| Transhumant | … | two bases; the route is infrastructure `(to-verify)` | … | route access is the exposure `(to-verify)` | B — UNESCO decision 14.COM 10.b.2 (S069) |
| Agro-pastoral | short moves on stubble and fallow, return to village `(to-verify)` | fixed village with fields `(to-verify)` | … | crop and herd buffer each other `(to-verify)` | B — FAO agropastoral (S048) |
| Enclosed / ranching | … | ranch headquarters `(to-verify)` | hired stockmen `(to-verify)` | market and tenure exposure `(to-verify)` | B — FAO enclosed/ranching (S048) |
```

and add one §13 bank row:

```
| The five-row mobility typology is FAO's classification | B — S048 registers four degrees of movement (nomadic/transhumant/agropastoral/enclosed); "semi-nomadic" is a lane-added dial `(to-verify)` | name which of the four the culture is closest to, then dial along one axis |
```

---

## F2 (HIGH) — the typology's **row set** contradicts the entry's own topic line, its README row and S048's registered scope

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:3`:

```
- topic: … mobility systems (nomadic, transhumant, agro-pastoral, enclosed); …
```

`corpus/README.md:297` is byte-identical to that topic line (the readme sweep enforces this: `topic_mismatch 0 []`).
**Four** systems. But the table at `:47-51` delivers **five** rows — Nomadic, Semi-nomadic, Transhumant,
Agro-pastoral, Enclosed/ranching — and `:153` (§11 build step 3) instructs the builder to choose among the same
five: `| 3 | Mobility | nomadic / semi-nomadic / transhumant / agro-pastoral / enclosed; splitting rule | §3; … |`.

The registry says four. `corpus/SOURCES.md:77` (S048) `teaches` field, verbatim:

> pastoralism needs conditions where hunting-gathering is not easy; **nomadic/transhumant/agropastoral/enclosed** as
> simplified degrees of movement; herd splitting; herders manage two to four species; the evolutionary-stage
> reading is refuted

Four degrees of movement, and the entry's own framing sentence at `:43` leans on S048 for exactly this: *"read the
rows as dials inside one economy"*. The fifth row, **Semi-nomadic**, is not in S048's registered scope, not in the
topic line, not in the README row, and — as F1 shows — has no calibration status and no source.

This is not a stylistic quibble: the entry's `- scope:` line (`:12`) and §15 (`:199`) both list the register's owned
surface as "species portfolio, mobility, herd management, products, herd wealth and transfer, pasture tenure,
pastoral–sedentary exchange" — and the README index row, which is the lane's own public catalogue of the register,
advertises a four-system typology that the body does not deliver. A worldbuilder reading the README row and then
§11 step 3 gets two different taxonomies.

**Smallest fix.** Pick one and make the whole file agree:
* *Option A (preferred — keep S048's four, delete the invented row).* Delete `:48`, drop "semi-nomadic" from `:153`,
  and note in `:153` that FAO's four are degrees of movement, not a ladder — this also makes `:3`/README correct as
  they stand, and the sibling `hunting-foraging-subsistence.md` typology is likewise built on its own registered
  rows' taxonomy.
* *Option B (keep the fifth row).* Then `:3`, `corpus/README.md:297` and the S048 `teaches` reading must all admit
  it: amend the topic line to "(nomadic, semi-nomadic, transhumant, agro-pastoral, enclosed)", re-run
  `python3 -B reports/round-28/readme/sweep.py` (expect `rows 226 files 226`, `topic_mismatch 0`), and mark the row
  `H` per F1. Note this touches the C claim's README land, so it belongs to the round-50 author lane, not to a
  falsify seat.

---

## F3 (MEDIUM-HIGH) — the political second axis is asserted once and then never used; the entry never claims political organisation in its scope

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:53` — the whole of it:

```
Political organisation is a **second axis**, not a mobility row: segmentary tribes, tribal chiefdoms and peasant
pastoralists (S057). Do not merge the two axes.
```

What holds:

* **The S-id resolves and the labels are the source's own.** `corpus/SOURCES.md:86` (S057) `teaches`: "political
  organisation (segmentary tribe, tribal chiefdom, peasant pastoralist) is an axis separate from mobility" — the
  exact three labels, exactly as the entry uses them. Tier **B**, scope "the book's stated programme and chapter list
  only (publisher description; QUALITY criterion 6); ethnography and conclusions unread". The entry honours that
  limit at `:187`: *"The publisher's summary of a book is the book's argument | B — S057 is a description only
  (QUALITY criterion 6) | cite programme and scope, not conclusions"*. The sibling seat `ReopenS057.md` re-opened the
  page and confirms the Gate quote verbatim at Description ¶1 sentence 2, with the same note I make below (N2).
* **The in-corpus anchor I could check does not contradict it.** `mongol.md:40` (`:43`) reads in full:
  *"This is a working periodization, not a ladder from "primitive nomad" to "civilization." Mobile pastoralism,
  urban production, and documentary administration can coexist."* That supports the "never a ladder" half of `:43`
  exactly (a ladder is rejected; mobility coexists with other production). It does **not** support the "read the rows
  as dials inside one economy" half — that half is the entry's own design move and is fine as method, but the
  anchor is doing less work than the sentence implies.

What breaks:

1. **The second axis is never operationalised.** `grep -n "political\|Political\|segmentary\|chiefdom\|peasant
   pastoralist" <entry>` → **one hit, line 53**. The three political types never reach:
   * the §11 decision table (`:149-158`) — eight build steps, none about political organisation;
   * the §12 worked micro-example (`:167-171`) — the invented Ketrun have a round, a lexicon and a market, and no
     political form at all, so the axis the entry insists is *not* mergeable is never exercised even once;
   * the §2 one-owner boundary table (`:31-39`, nine rows) — no political-organisation neighbour is listed, so
     nothing in the entry says who owns political typology (the regional `civilizations/` entries are listed as
     "Mongol, Turkic, Scythian, Sámi, Diné, Inca cases and their warnings", general method only);
   * the `- scope:` line (`:12`) and §15 (`:199`) — neither mentions political organisation among the owned
     surfaces.
   So the axis is a **canon-adjacent assertion with no design rule**: the entry tells the worldbuilder the two axes
   must not be merged, but gives them nothing to merge and no way to decide among the three types. QUALITY
   criterion 4 (usability) and the sibling `hunting-foraging-subsistence.md` contract (decision table `| If your
   culture… | then the register needs… | and check |` plus `DR-xx` decision rows) both point the same way: a second
   axis that no build step consults is a claim, not a method.
2. **The "separate axis" framing is the lane's, not the source's, and it is not marked as such at the point of
   use.** The S057 registry `teaches` field does say "is an axis separate from mobility", so the row *registers* that
   framing — but the underlying publisher page (per `ReopenS057.md` §6 N2 and the row's own `scope`) never uses the
   words "mobility" or "axis"; the separation is inferred from the labels plus the book's title and ToC. The entry
   marks the tier at `:187` but not the inference at `:53`. `ReopenS057.md` calls this N2 and rates it non-blocking;
   for a **falsify** seat it is the difference between "the source says political organisation is a separate axis"
   and "the lane reads a publisher's chapter list that way".

**Smallest fix.** (a) At `:53`, mark the inference in the same sentence, e.g. *"…(S057 — the three labels are the
publisher's own; the 'second axis' reading is the lane's, from the labels and the book's title/ToC)"*. (b) Add one
§11 build step or one §2 boundary row so the axis has an owner, e.g. a step 9 "Political form — segmentary /
chiefdom / peasant pastoralist; who decides moves" checked against S057, or a §2 row
`| political organisation | segmentary / chiefdom / peasant pastoralist as settlement and tenure positions, not mobility terms (S057) | the axis is named here and carried nowhere else |`.
(c) Exercise it once in §12 so the non-merge instruction is demonstrated.

---

## F4 (MEDIUM) — `:43`'s S048 quotation is not registered in the Gate or in S048's `teaches`, although the row and the Gate both carry *other* S048 quotes

`:43` opens with a direct quotation attributed to S048:

```
"Any classification of this type must be treated as a simplification" (S048): read the rows as dials inside one
economy, never a ladder (`mongol.md:40`).
```

The registry is silent about this sentence:

```
$ grep -rn "Any classification of this type" corpus/SOURCES.md corpus/lessons/round-50.md
(empty — NOT registered)
```

`corpus/lessons/round-50.md:33` (S048's Gate bullet) carries a *different* quote —
`§Classifying pastoral systems: "there is little or no impetus to herd animals"` — and `corpus/SOURCES.md:77`
(S048) `teaches` does not list the simplification sentence either; its `anchor` field lists the sections
(`§Classifying pastoral systems; §Pastoral enterprises (Nomadism, Enclosed systems and ranching); §Pastoral species;
§History and origins of pastoralism`) but the sentence sits in the **Pastoral enterprises lead paragraph**, which the
anchor names only by its two subsections (Nomadism, Enclosed systems and ranching) — not the lead paragraph.

This is not an invented quotation: the build seat located it verbatim at build time
(`.ufo/waves/round-50/build/ScribeSec11Decision.md:32`: *"(g) "Pastoral enterprises › Transhumance": …"Any
classification of this type must be treated as a simplification" (Pastoral enterprises, lead paragraph)"*), and the
sibling seat `ReopenS048.md` §6 re-fetched the page and confirms the string is exact, appearing once, in the first
paragraph of `PASTORAL ENTERPRISES`. **The defect is traceability, not accuracy**: the lane's own registry rule
(`corpus/SOURCES.md:8-10`) is that *every row was opened in the round that wrote it — the round lesson's `## Gate`
holds each row's URL, access date and verbatim quote*. This sentence is a second verbatim S048 quote in the entry
that appears in neither the Gate nor the row's `anchor`/`teaches`. A reader auditing `:43` against the registry
finds nothing.

**Smallest fix.** One of:
* extend the S048 Gate bullet with the second located quote — `corpus/lessons/round-50.md:33` — e.g.
  `… — §Pastoral enterprises, lead paragraph: "Any classification of this type must be treated as a simplification". Grounds the typology-dial framing.`
  (the lesson file is append-only in structure, and round-49's `## Post-review corrections` (2026-10-19) shows the
  lane's own precedent for adding a dated correction section); **or**
* fold the sentence into the row's `anchor` field via a superseding row per `corpus/SOURCES.md:10-13` ("a correction
  is a new row whose `teaches` opens `supersedes S0NN —`").

---

## F5 (LOW-MEDIUM) — the three S-ids the typology leans on are supported by their registry rows; two of them need a scope qualifier at the point of use

Checked against the registry rows' own `scope`/`anchor`/`teaches` (URL re-opening belongs to the sibling seats; I did
not re-open):

| cited | landed sentence | row's registered `teaches` / `scope` | verdict |
|---|---|---|---|
| **S048** `:49` "herd splitting (S048)" | Transhumant Labour | `teaches`: "herd splitting" — verbatim in the registered teaching | **holds** |
| **S048** `:51` "fenced, individually owned land (S048)" | Enclosed/ranching Mobility | `teaches` lists "enclosed" among the four degrees of movement; `anchor` names "§Pastoral enterprises (… Enclosed systems and ranching)" | **holds**, and `ReopenS048.md` §6 confirms the page says "the land is individually owned and usually fenced" |
| **S069** `:49` "horizontal in plains or plateaus, vertical in mountains (S069)" | Transhumant Mobility | `teaches`: "horizontal (plain or plateau) and vertical (mountain) types"; `anchor`: "decision text, sentence 4" | **holds** — and it is the correct replacement for the build seat's dropped `(to-verify)` on the split (draft `:16` "vertical/horizontal split itself `(to-verify)`"), so this part of §3 is *better* than the draft |
| **S062** `:47` "the ger is "light enough for nomads to carry" (S062)" | Nomadic Settlement | `teaches`: "the ger's portability as a derived requirement of the nomadic round"; `anchor`: "Description paragraph, third sentence" | **holds as a quotation**, but see the qualifier below |
| **S060** `:47` "species mix and movement are the hedge (S060)" | Nomadic Risk | `teaches`: "the five snouts as an emic portfolio term; **reliability-seeking risk management**; covariate dzud risk limits risk sharing" | **PARTIAL** — "species mix … is the hedge" is not what the row teaches; `ReopenS060.md` §5 independently confirms "the paper never says species mix is a hedge". Only "movement … is the hedge" survives |

Two qualifiers the rows' own scope fields demand and §3 does not give:

* **S062 is a Mongol case used as the generic nomadic settlement.** The row's `scope`: "UNESCO's own inscription
  record and description of the ger; not pastoral ecology or herd management" — i.e. the ger is *one* nomadic
  dwelling, from one culture. `:47` places it in the Settlement cell of the row whose Migration cell says "household
  and herd move on a forage cycle" for *all* nomads. The entry elsewhere is scrupulous about exactly this move
  (`:59` "social idiom in Nilotic ethnography (S052) is **regional, not a law**"; `:63` "cultural claims bounded to
  the FAO synthesis (S061)"). §3's Nomadic row reads as generic. Smallest fix: "portable dwelling — the Mongol ger
  is 'light enough for nomads to carry' (S062); regional, not a law".
* **S060 is a Mongolian subdistrict study used as the generic nomadic risk strategy.** The row's `scope`:
  "the author's account of Mongolian pastoral risk management in **Bayankhongor** and the five-snouts aggregate as
  reported from the National Statistical Yearbook 2013". `:47` uses it for the Nomadic row unqualified — while the
  same S060 row *is* qualified elsewhere in the entry (`:67` "The Mongolian 'five snouts' … is an emic portfolio term
  (S060)"). Smallest fix: "species mix and movement are the hedge (S060 — Mongolian, regional); movement is the hedge
  `(to-verify)` for species mix".

---

## F6 (LOW) — `:50`'s in-corpus anchor is exact, and is the only load-bearing in-corpus citation in the slice

`:50` Labour cell: `herd calendar collides with the ploughing peak (`agrarian-field-system-lexicon.md:62`)`.
At the landed commit, `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:62` is the agropastoral row
and reads in full:

```
| agropastoral | fields + pasture + transhumance routes | ploughing peak plus herd calendar; manure contracts | rain + wells | mixed: grain parcels + herd rights; manure-for-stubble exchange | fold, transhumance, stubble-right | standard; manure/night-soil euphemism seam — `textile-technology.md:76` |
```

The Labour-signature cell literally reads "ploughing peak plus herd calendar" — the entry's "herd calendar collides
with the ploughing peak" is a faithful compression of it. The file is byte-identical between base `4ad2683` and the
landed commit (`git diff --stat 4ad2683 1c779e4a -- corpus/knowledge/culture-material/agrarian-field-system-lexicon.md`
→ empty), so the line reference is stable. **This anchor holds.**

The one thing §3 does *not* do that its sibling table does: it never says what the **agropastoral row is not** —
`:31` (the §2 boundary table) states the neighbour "owns parcel, plough, stubble grazing, manure contract", and
`:50` cites `:62` for the herd-calendar collision, so the one-owner boundary is respected. Good.

---

## F7 (LOW) — head-anchor hygiene: three head-listed anchors are never cited in the body, and one body citation set is thinner than the head claims

Not a §3 defect (it is the entry's head), recorded because the head's in-corpus list is what a §3 reader trusts to
cover the slice. Head-listed but never cited in the body: `agrarian-field-system-lexicon.md:80`,
`hunting-foraging-subsistence.md:117`, `:137-146`, `:170-172`. (House style check: the sibling
`hunting-foraging-subsistence.md` also lists head anchors it does not cite in the body — `algonquian.md:121` etc. —
so over-listing is the lane's convention, not a violation. Noted, not counted as a defect.)

What *is* worth flagging for §3: the head's in-corpus list (`:6`) includes `civilizations/mongol.md:40` and
`culture-material/agrarian-field-system-lexicon.md:56,:62,:80` — the two anchors §3 actually uses are present and
correct — but the slice's own body citations use **bare basenames** (`:43` `` `mongol.md:40` ``, `:50`
`` `agrarian-field-system-lexicon.md:62` ``) while the head lists **repo-relative paths**
(`civilizations/mongol.md:40`). That is the house convention (`hunting-foraging-subsistence.md` does the same:
head lists `corpus/knowledge/civilizations/algonquian.md`, body cites `` `algonquian.md:143` ``), so it is consistent
— but a reader auditing `mongol.md:40` must know the file is under `civilizations/`, not `culture-material/`
(the build seat flagged this path trap explicitly: `ScribeSec11Decision.md:36` "**Path correction for the lane:**
scythian-saka, mongol, turkic-steppe, finnic-sami and inca live under `corpus/knowledge/civilizations/`, not
`culture-material/`"). Recorded so the lane does not "fix" it in the wrong direction.

---

## What holds (so the author lane does not re-open settled ground)

1. **The gap premise reproduces exactly.** At base `4ad2683`:
   `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l` → **0**;
   `grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l` → **0**;
   the unbounded form hits exactly one non-owner, `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`
   ("sherd") — which is what the entry's `:4` gap line says. Counts `find corpus/knowledge -name '*.md' | wc -l` → 225
   at base, 226 landed; `ls corpus/knowledge/culture-material/*.md | wc -l` → 27 at base, 28 landed.
2. **The readme sweep is green and the topic line is byte-equal to the README row.**
   `python3 -B reports/round-28/readme/sweep.py` → `rows 226 files 226`, `topic_mismatch 0 []`, `orphan_rows 0 []`,
   `footer_ok True`.
3. **Every S-id in the slice resolves, and every one of the 22 S-ids the entry cites resolves to a row whose
   `used-by` names the entry and whose `status` is `mined`.** Scripted over all 22: no unregistered id, no
   `queued`/`rejected` row cited.
4. **§3's two in-corpus anchors resolve at the landed commit and support their sentences** (F6, and `mongol.md:40`
   for the "never a ladder" half of `:43`).
5. **The corpus has no other owner of this register.** `grep -rln "nomad" corpus/knowledge/` → 7 files, all regional
   civilization entries plus `furniture-interior-lexicon.md` (which owns the chest-as-nomad-furniture seam at `:81`
   — the build seat's §3 draft cited that line, and the landed §3 dropped it in favour of S062; the seam is now
   uncited by this entry, which is acceptable but leaves `furniture-interior-lexicon.md:81` as an available,
   already-open in-corpus alternative for the Nomadic Settlement cell). No owner conflict with §3.

---

## Residual risk and verification gaps

* **Not re-verified here (other seats own it):** the URLs behind S048, S057, S060, S062, S069. I checked the
  *registry rows* against the sentences, not the pages. The sibling seats' verdicts, read for cross-check and not
  re-run: `ReopenS048.md` **PARTIAL** (one unscoped "two to four species", outside §3), `ReopenS057.md` **HOLDS**
  (with note N2, which F3 adopts), `ReopenS060.md` **PARTIAL** (the `:47` "species mix" overreach — F5 adopts it),
  `ReopenS062.md` **HOLDS**, `ReopenS069.md` **HOLDS**.
* **Two sibling findings land inside my slice and are adopted here rather than duplicated:** `ReopenS060.md` on
  `:47` ("species mix … is the hedge") and `:47`'s Labour cell; `ReopenS057.md` note N2 on `:53`'s "second axis"
  framing. This report adds what those seats could not see from the source side: the missing status column, the
  row-set contradiction, and the eight uncited/uncovenanted cells.
* **Not checked (out of my slice):** §1 (owned by `ReviewSec01.md`), §2/§11/§13 (owned elsewhere), and the O and Ca
  claims. This report says nothing about the O gates or the Ca checker/fixture.
* **Lane-level observation, not a §3 finding:** `reports/round-50/validation.json` is named as the round receipt in
  the ticket and in `corpus/lessons/round-50.md:3-4`, but it is **not in the landed commit** —
  `git ls-tree -r --name-only 1c779e4a -- reports/round-50` lists ten files and no `validation.json`;
  `git cat-file -e 1c779e4a:reports/round-50/validation.json` → `fatal: path … does not exist`. The file exists in
  the working tree only. Recorded for whichever seat owns the receipt; it does not change the §3 verdict.
* **Disk:** the host is nearly full; my clone (`/tmp/kr50sec03-4180537`, plus a base-commit clone) is deleted after
  this run. No tool was installed (pacman is paused host-wide; nothing was needed).

## Smallest-fix summary for the author lane (author-lane advice, not admission)

1. Restore the build seat's `Status / cite` column on the §3 table and mark the eight-plus unsupported cells
   `(to-verify)`; add one §13 bank row for the typology itself (F1).
2. Resolve the four-vs-five system contradiction between `:3`/README and `:47-51`/`:153` — prefer deleting
   "Semi-nomadic" so the file matches S048's registered four (F2).
3. Mark the "second axis" reading at `:53` as the lane's inference, and give the axis one build step or one
   boundary row plus one worked example (F3).
4. Register the second S048 quotation in the round-50 Gate or in a superseding S048 row (F4).
5. Qualify the two regional sources at point of use: S062 → "the Mongol ger … regional, not a law";
   S060 → "Mongolian, regional", and drop or mark "species mix … is the hedge" (F5).

Nothing here is an admission, and nothing in the lane was edited by this seat.

---

## Addendum — working-tree drift observed after the report was written (read-only observation)

While this seat was finishing, another seat began editing the lane working tree (this seat wrote **only** this file;
`git status` shows `corpus/SOURCES.md`, `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` and
`corpus/lessons/round-50.md` modified, none by me). The verdict above is against the **landed commit
`1c779e4a`** as the ticket requires; the drift is recorded so the author lane knows what is already in flight.

The in-flight working-tree edit already repairs **one** of this report's findings and leaves the others open:

| finding | landed `1c779e4a` | working tree now |
|---|---|---|
| F5 (S060 overreach, `:47`) | Labour "splitting by species and age"; Risk "species mix and movement are the hedge (S060)" | Labour "household herding; splitting by age and health (S060)"; Risk "movement and herd splitting are the hedge (S060)" — **repaired** (matches `ReopenS060.md`) |
| F1 (no status column) | 5 columns, no status | **still 5 columns, no status** — the eight uncited/uncovenanted cells (Semi-nomadic Mobility/Settlement/Risk, Transhumant Settlement/Risk, Enclosed Settlement/Labour/Risk) are unchanged |
| F2 (four vs five systems) | topic line 4, table 5, `:153` 5 | **unchanged** — topic line still "(nomadic, transhumant, agro-pastoral, enclosed)", table still five rows, `:155` still lists five |
| F3 (political axis not operationalised) | one sentence at `:53` | **unchanged** — still one sentence; no §11 step, no §2 row, no §12 exercise |
| F4 (`:43` S048 quote unregistered) | not in Gate or `teaches` | `corpus/lessons/round-50.md` is modified in the working tree; whether the second S048 quote was added there should be re-checked by the integrating seat before the round closes |
| F6 (`:50` agrarian anchor) | exact | unchanged — still correct |

Re-read of the working-tree bytes for the two lines that matter most:

```
$ awk '/^## 3\. Pastoral systems typology/,/^## 4\./' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | head -8
…
| System | Mobility | Settlement | Labour | Risk strategy |
|---|---|---|---|---|
| Nomadic | household and herd move on a forage cycle | portable dwelling — the ger is "light enough for nomads to carry" (S062) | household herding; splitting by age and health (S060) | movement and herd splitting are the hedge (S060) |
| Semi-nomadic | part of household travels; a base is held | village or winter camp plus satellite camps | base keeps the old, young and crop plot `(to-verify)` | the base is store and drought fallback |
…
$ sed -n '3p' … | grep -o "mobility systems ([^)]*)"   →  mobility systems (nomadic, transhumant, agro-pastoral, enclosed)
$ grep -n "semi-nomadic" …                             →  155:| 3 | Mobility | nomadic / semi-nomadic / transhumant / agro-pastoral / enclosed; …
```

So F1–F4 stand against the in-flight edit as well. Note also that the in-flight edit *rewrites* `:47`'s Labour cell
with a fresh `(S060)` citation ("splitting by age and health") — a claim `ReopenS060.md` does not list among the
paper's statements; re-check it against the row's `teaches` ("the five snouts as an emic portfolio term;
reliability-seeking risk management; covariate dzud risk limits risk sharing") before it lands.

Nothing in the lane was edited by this seat.
