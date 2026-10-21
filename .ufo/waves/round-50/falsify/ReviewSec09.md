# ReviewSec09 — falsify attack on §9 (pastoral–sedentary relations) and the bias flags of C's entry

Seat: `KotodamaR50-2.ReviewSec09-21` (leaf, read-only; no delegation, no lane mutating git).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
Method: private clone `git clone -q --shared … /tmp/revsec09-XXXX` + `checkout -q 1c779e4…`; every lane byte below was read at the
landed commit, never from the lane working tree. `git archive <base> corpus/knowledge` into `/tmp/revsec09-base` for base-state
reproduction. Both temp trees deleted afterwards (host `/tmp` was at 96 %).

Scope attacked (per assignment): `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` §9 and the bias-flag
paragraphs; every in-corpus `path:line` anchor those sections cite, opened at `1c779e4`; every S-id they cite, checked against the
row's scope/anchor in `corpus/SOURCES.md` (URL re-opening delegated to the `ReopenS056` seat — not redone here).

## Verdict

**PARTIAL.** The section's *evidence* holds: all four in-corpus anchors open at the landed commit and support their sentences
except one, the single external quote is verbatim against the round-50 Gate, and the entry's own `verified-at`/gap-sweep claims
reproduce exactly. The section's *wording* does not hold in three places: one bias flag is anchored to a line that says
something else, two relation rows assert uncited and unmarked facts, and the row-level calibration status that the build wave's
own entry contract required was dropped in landing. All defects are local to one line-range and are fixed by small edits.

## Findings by severity

### F1 — MEDIUM — the "raider → state" ladder is in no anchor, and the cited anchor says something else

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:131` (landed):

> Bias flags: … reject any ladder from "raider" to "state" (`turkic-steppe.md:194`); …

`corpus/knowledge/civilizations/turkic-steppe.md:194` (landed) reads in full:

```
194: - **Colonial/evolutionist bias:** later ethnographies and older comparative scholarship may treat living communities
     as survivals of a primitive stage. Reject a ladder from “nomad/shaman” to “civilized/monotheist”; audit each
     claimed continuity separately.
```

The anchored line rejects a **"nomad/shaman" → "civilized/monotheist"** ladder. It contains no "raider", no "state" endpoint and
no raid-to-state progression. The corpus-wide check:

```
$ grep -rn 'raider' corpus/
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:131:  … reject any ladder from "raider" to "state" …
```

`raider` occurs exactly once in the whole corpus — in the new line that claims it. The two anchors that *do* carry a
nomad→civilisation ladder use different words and are not cited here:

- `corpus/knowledge/civilizations/mongol.md:40` — "This is a working periodization, not a ladder from “primitive nomad” to
  “civilization.”"
- `corpus/knowledge/civilizations/arabia-pre-islamic.md:174` — "**Source-bias warning:** Stillman's pp. 8–9 employ a
  “higher civilizations” contrast … Reject the hierarchy …"

The build-wave draft that produced this line had all three anchors and the scribe's own anchor table recorded the mismatch
verbatim — `.ufo/waves/round-50/build/ScribeSec09Relations.md` (landed), "In-corpus anchors" table:

```
| `civilizations/turkic-steppe.md:194` | "Reject a ladder from 'nomad/shaman' to 'civilized/monotheist'" | bias flag |
| `civilizations/mongol.md:40`         | "not a ladder from 'primitive nomad' to 'civilization.'"     | bias flag |
| `civilizations/arabia-pre-islamic.md:174` | "Source-bias warning … Reject the hierarchy"              | bias flag |
```

The draft's flag read "Reject any ladder from “raider” to “civilized state” (`turkic-steppe.md:194`; `civilizations/mongol.md:40`;
`civilizations/arabia-pre-islamic.md:174`)". Landing kept the mismatched wording, dropped "civilized", dropped the "state" pairing
and dropped the two anchors that would have carried the claim. QUALITY criterion 1 (`corpus/QUALITY.md:5-8`) requires every
factual claim to carry a cited, checkable source; here the citation does not carry the claim.

Smallest fix (one line, `:131`): either restate the flag in the anchors' own words and restore the anchors —
`reject any ladder from "nomad/shaman" to "civilized/monotheist" (`turkic-steppe.md:194`) and from "primitive nomad" to
"civilization" (`mongol.md:40`)` — or, if "raider → state" is the intended flag, cite the source that actually states it and
mark it `(to-verify)` until then. (Note `calibration-registry.md:51` CAL-04 is *not* a usable substitute: it is the
magic→religion→science row.)

### F2 — MEDIUM — two §9 relation rows assert uncited, unmarked facts

`pastoralism-animal-husbandry.md:128-129` (landed):

```
128: | Tribute and tolls | dependent cultivators pay; caravans buy passage | tribute is an income line, not a one-off |
129: | Conquest state   | a mobile empire taxes transit and fields        | name the external rival it forms against `(to-verify)` |
```

- Row 129's "a mobile empire taxes transit and fields" is an unmarked factual assertion with no S-id. The `(to-verify)` marker
  sits in the *Design check* column, i.e. it qualifies "name the external rival", not the proposition "a mobile empire taxes
  transit and fields". QUALITY criterion 1: a claim the author cannot verify is marked `(to-verify)` inline; here the load-bearing
  proposition is neither cited nor marked.
- Row 128's "caravans buy passage" is likewise uncited. S056's registered support covers only "tribute and gifts from dependent
  sedentary populations" (`corpus/SOURCES.md:85`, "what it supports" column) — nothing about tolls or passage.

The build-wave draft carried a separate, sourced "Tolls and passage" row and a "Conquest state" row with an explicit
calibration status ("**contested** — Barfield frontier thesis [B20] vs inter-nomadic-dynamics critique (to-verify)"). Both the
sourced row and the status were dropped at landing, leaving the residues above.

Smallest fix: mark the two propositions `(to-verify)` inline, or cite S056 for the tribute half and add a `(to-verify)` on the
"mobile empire taxes transit" half; restore a Status cell for both rows (see F3).

### F3 — MEDIUM — §9 has no calibration status at all; the build wave's entry contract required a Status column

`pastoralism-animal-husbandry.md:124` (landed) — the §9 table header:

```
| Relation | What moves, who holds the lever | Design check |
```

Three columns, no Status. The sibling §8 table in the same file *does* carry one (`:112` `| Model | Proposition | Status | Design
use |`), so this is an internal inconsistency, and it is also a direct miss of the build wave's own instruction to the section
scribes — `.ufo/waves/round-50/build/ReviewEntryContract.md:206` (landed):

> "**Calibration status vocabulary.** The models use registry codes R/C/B/H/T in a Status column, not QUALITY's
> 'mainmainstream/contested/discredited' words. Follow the models."

The §9 scribe's draft had four columns (`… | Design check | Status |`) with per-row statuses ("mainstream — non-autarky [K19]",
"attested in detail …", "attested …", "**contested** — Barfield frontier thesis …"); landing dropped the column. QUALITY
criterion 2 (`corpus/QUALITY.md:9-12`) requires every framework entry to name its status with the reason.

Smallest fix: add a `Status` column to the §9 table with `mainstream`→`B`/`C` codes per `calibration-registry.md:35-39`, e.g.
Interdependence **B** (steppe nomads, S056 scope), Trade under pressure **B**, Tribute and tolls **B**, Conquest state **C**/`T`.

### F4 — MEDIUM — the Living-practice flag cites a row whose scope says "not current practice", and names three uncited peoples

`pastoralism-animal-husbandry.md:189` (landed):

> **Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063).

Two defects in one sentence:

1. **Scope inversion on S058.** `corpus/SOURCES.md:87` (landed) scopes S058 as "the WoDaaBe seasonal movement system in
   southeastern Niger as observed 1996–97, cattle only; **not current practice**" — the row explicitly refuses the claim it is
   cited for. Its registered support is "seasonal moves follow the rains; mobility as a tool for timing an ecological process;
   named move types"; nothing about the practice being live today. (S059's row is a live agency register — "footer Senast
   uppdaterad 13 december 2024" — and S063's "erosion of skills" implies continuity, so those two are defensible.)
2. **Three of the six named peoples are uncited.** "Mongolian" has row S060 and "Tibetan" has row S061; neither is in the
   citation set. "Maasai" has **no registry row at all**:
   `grep -c 'Maasai' corpus/SOURCES.md` → `0` (the word appears elsewhere in the corpus only in unrelated costume/bead
   entries). A factual claim about a living people with no citable source is a criterion-1 defect.

Smallest fix: cite S060 (Mongolian) and S061 (Tibetan) alongside S058/S059/S063, drop "Maasai" or mark it `(to-verify)`, and
replace the S058 citation with a current source (or state the flag as "herding among these peoples is documented as living
practice in the 1996–97 record, later currency not established here").

### F5 — MEDIUM/LOW — §9's master claim generalises a steppe-nomad source to "a herding economy", uncoded

`pastoralism-animal-husbandry.md:122` (landed):

> A herding economy is non-autarkic by construction: steppe nomads "always experienced a need for external agricultural and
> handicraft products" (S056).

The quote is exact and correctly attributed (see V1 below), and the row's own scope is "Khazanov's own thesis of nomadic
non-autarky …" (`corpus/SOURCES.md:85`) — i.e. the Eurasian steppe nomads of Khazanov's 2019 article, tier A *for that thesis*.
The lead clause then asserts the property of "a herding economy" in general, with no code and no scope marker, while the file's
own practice elsewhere is to bound such claims ("B to that people and period", `:106`; "B — one legal system", `:116`;
"C → R for modern horses", `:185`; S061's "cultural claims bounded to the FAO synthesis", `:63`). The draft had a second,
comparative support for the universality — Digard's 1987 review of Khazanov ("loin d'être autarciques …", D87, tier B) — which
was never registered in `corpus/SOURCES.md` (`grep -n 'Digard' corpus/SOURCES.md` → no row).

Smallest fix: scope the clause — "A herding economy is non-autarkic by construction (**B**, in Khazanov's Eurasian steppe case,
S056)" — or cite a comparative source for the general form.

### F6 — LOW/MEDIUM — "nomads force them open" exceeds S056's registered support

`pastoralism-animal-husbandry.md:127` (landed):

> | Trade under pressure | the sedentary state licenses markets; nomads force them open (S056) | …

`corpus/SOURCES.md:85` registers, for S056, only "nomads always needed external grain and crafts; **sedentary states used trade
as political pressure**; tribute and gifts from dependent sedentary populations". The nomad-side mechanism ("force them open")
is the half that the row does not register. The build-wave scribe had located the sentence that would carry it —
`.ufo/waves/round-50/build/ScribeSec09Relations.md` (landed), K19 second quote: "considered the trade with nomads as a way of
applying a political pressure on them" — "Regional and Interregional Trade", p. 87 — i.e. the *state's* use of trade as
pressure, plus p. 90 "had a certain economic motivation, a desire to acquire lucrative control over the transcontinental
trade" and p. 91 "the merchants passing through the steppes had to pay to the Oghuz nomads for temporary shelter in tents".
The landed row's two halves are both reachable in the source, but only the state-side one is in the registry row, and the
"licensed / forced open" pair is a two-sided mechanism the row does not state.

Smallest fix: extend S056's "what it supports" cell with the located p. 87/90/91 facts (or mark the nomad-side half
`(to-verify)`), and add the §9 Status code per F3.

### F7 — LOW — §7's `(§9)` pointer now dangles

`pastoralism-animal-husbandry.md:104` (landed):

> | Raid | stock taken to rebuild after loss | raids target the form of wealth: animals and people, not grain (§9) |

§9 (`:120-131`) contains no raid content: `grep -n 'raid'` over the landed entry returns only lines 3, 23, 104 and 199 (topic
line, §1's "gift, loan, bridewealth and raid", the §7 row itself, and §15's handoff). The rule therefore points at a section that
does not carry it, and the rule's substance ("animals and people, not grain") is now uncited and unowned. The draft's §9 did
have a "Raiding" row (sourced to Næss & Bårdsen 2023, "The nomads of the steppe zone in central Eurasia typically targeted
livestock and people rather than agricultural produce during their attacks", itself marked *Beckwith 2009:325, to-verify*); N23 was
never registered in `corpus/SOURCES.md`, and the row was dropped at landing.

Smallest fix: either restore a §9 "Raiding" row (with the N23/Beckwith claim marked `(to-verify)` and the source registered) or
re-point §7's rule at its own row / at §13's calibration bank, so the pointer resolves.

### F8 — LOW — "'barbarian' is a calibration defect" is uncoded and unanchored, and is out of step with the corpus's own framing

`pastoralism-animal-husbandry.md:131` (landed) states the flag with no code, no anchor and no source. The corpus precedent for the
phrase exists — `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:197`: "“primitive” is a calibration defect
wherever it appears" — so the phrasing is house style. But the corpus treats "barbarian" as a *source-positioned category to
analyse*, not a defective term: `civilizations/china-tang.md:190` ("“Hu” and “barbarian” are source-positioned classifications, not
neutral racial taxonomies"), `civilizations/greece-classical.md:201` ("historical categories to analyze, not neutral rankings"),
`civilizations/slavs-early.md:196` ("mediated categories, not native Slavic self-descriptions"). Calling it flatly a "calibration
defect" drops the "analyse the category, do not naturalise it" half of the house rule.

Smallest fix: restate as "“barbarian” is a source-positioned category, not a neutral ranking (analyse it; do not import it) —
`china-tang.md:190`", or code it **B** with the reason.

## What verified (the parts that hold)

- **V1 — the S056 quote is verbatim and correctly located.** `corpus/lessons/round-50.md:41` (landed), Gate bullet:
  `S056 — …/chungara-00302.pdf — accessed 2026-10-21 — Abstract, p. 85: "always experienced a need for external agricultural and
  handicraft products". Seat: ScribeSec09Relations.` The entry at `:122` quotes exactly that phrase and attributes it to S056; the
  registry row (`corpus/SOURCES.md:85`) is tier A, opened 2026-10-21, scope "Khazanov's own thesis of nomadic non-autarky and
  trade under political pressure; B for the historical episodes it reports". The entry's use stays inside that scope except for
  F5/F6.
- **V2 — three of four in-corpus anchors support their sentences at the landed commit** (opened line-by-line, not by grep):
  - `civilizations/turkic-steppe.md:193` — "**Chronicle bias:** Chinese dynastic histories … They are indispensable witnesses,
    not transparent recordings of a single indigenous original." → supports "Chinese dynastic histories are indispensable and not
    neutral" (`:131`). ✔
  - `civilizations/turkic-steppe.md:148` — "Do not make pastoral production synonymous with economic isolation." → supports
    "Pastoral is not isolation" (`:131`). ✔
  - `civilizations/scythian-saka.md:70` — "Do not equate pastoralism with total absence of farming: even Herodotus distinguishes
    farming and nomadic Scythians (4.17–20)." → supports "pastoralism is not absence of farming" (`:131`). ✔
  - `civilizations/turkic-steppe.md:194` → does **not** support the sentence it is attached to (F1).
- **V3 — the living-practice rule's anchor holds.** `culture-material/hunting-foraging-subsistence.md:195` — "Write fictional
  systems *like* these mechanics, never *as* these peoples." → supports the entry's rule at `:189` (the *citation set* of that
  sentence is what fails; see F4).
- **V4 — no line drift between base and landed for any cited corpus file.**
  `git diff --stat 4ad2683 1c779e4 -- corpus/` shows only `QUALITY.md`, `README.md`, `SOURCES.md`, `lessons/round-50.md` and the
  new entry. Every `path:line` anchor the entry cites therefore still resolves to the same text at the landed commit (verified for
  this section's anchors by reading the lines at `1c779e4`).
- **V5 — the entry's `verified-at` and `gap filled` claims reproduce exactly at base `4ad2683`.**
  `find corpus/knowledge -name '*.md' | wc -l` → 225; `ls corpus/knowledge/culture-material/*.md | wc -l` → 27;
  `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l` → 0;
  `grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l` → 0; the un-bounded form hits
  exactly one line, `culture-material/writing-media-surface-economy.md:3` ("sherd"), the non-owner the entry names. ✔
- **V6 — the landed index state is as claimed.** At `1c779e4`: 226 knowledge files, 28 in `culture-material/`;
  `python3 -B reports/round-28/readme/sweep.py` → `rows 226 files 226`, `topic_mismatch 0 []`, `orphan_rows 0 []`, `footer_ok True`,
  `exit 0`. The entry's `verified-at` line and the README 2.7 revision text (totals 225→226, `## culture-material/ (27)`→`(28)`,
  footer vector `25/26/27/29/24/94`→`25/26/28/29/24/94`) match the tree. ✔
- **V7 — criterion 3 (coupling) and criterion 5 (canon hygiene) hold for §9.** The `- couples:` line names
  `civilizations/mongol.md, turkic-steppe.md, scythian-saka.md, finnic-sami.md, dine-navajo.md, inca.md` ("regional cases, cited
  never restated") and `lore-shokunin`; §9 itself decides no canon (its "Design check" column asks questions, §12 is marked
  **NON-CANON**, §15 carries the handoff). ✔
- **V8 — criterion 4 (usability) holds for §9.** The relation table plus the §11 step-7 row ("the sedentary neighbour, its power
  and the exchange form | §9; S056") is an actionable build sequence. ✔

## Residual risk and verification gaps

- **Not verified here (delegated):** the S056 PDF itself (p. 85/87/89/90/91) was not re-opened — that is the `ReopenS056` seat's
  job. F5/F6 are decided against the *registry row's* registered scope, which is what the assignment asked for; if the S056
  re-opener shows p. 87/90/91 carry the nomad-side mechanism and the "licensed/forced open" pair, F6 collapses to a
  registry-completeness nit (the SOURCES row's "what it supports" cell still should list it) and F5 stands.
- **Whole-file scope:** I read the whole landed entry but attacked §9, the bias-flag paragraphs and their direct inbound
  references (§7's raid row, §11 step 7, §13's "pure nomad" row, §15's scope). §13's "pure nomad" row is consistent with S056's
  registered support ("nomads always needed external grain and crafts"); no defect found there.
- **Unjudged by this seat:** the O (gates/probe) and Ca (checker/fixture) claims — other seats.
- **Tooling:** no installs or updates were needed or performed (read-only git plumbing, `awk`/`grep` line extraction, one read-only
  `python3` sweep). No credentials, no live-process probing, no lane `jj`/`git` mutation, no writes outside this report.

## Smallest fix set (author-lane advice, not admission)

1. `:131` — restate the ladder flag in the anchors' own words and restore `mongol.md:40` (or drop the anchor and mark
   `(to-verify)`).
2. `:124-129` — add the `Status` column (R/C/B/H/T per `calibration-registry.md:35-39`) that `ReviewEntryContract.md:206`
   required, and give each row a code.
3. `:128-129` — cite S056 for the tribute half; mark "caravans buy passage" and "a mobile empire taxes transit and fields"
   `(to-verify)` inline.
4. `:122` — bound the master clause ("B — in Khazanov's Eurasian steppe case, S056") or add a comparative source row.
5. `:189` — cite S060/S061, drop or `(to-verify)` "Maasai", and stop using S058 (scope: "not current practice") as the evidence
   for a living-practice claim.
6. `:104` — re-point or restore the raid rule so `(§9)` resolves.
