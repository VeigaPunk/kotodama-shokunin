# ReviewSec01 — attack on §1 "The register property" and its four-test table

Seat: `KotodamaR50-2.ReviewSec01-21` (leaf; no delegation, no background jobs).
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`),
lane `kotodama-shokunin` (/home/vgpnk/Projects/shokunin/kotodama-shokunin).
All lane bytes read from a private clone (`git clone -q --shared <lane> /tmp/r50-review && git checkout -q 1c779e4`),
never from the working tree; `GIT_CEILING_DIRECTORIES=/tmp`. No lane file edited, no jj/git mutation in the lane,
no install, no delegation. Clone deleted after the run.

Target slice attacked: `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` **§1, lines 14–25**
(heading, master claim, four-test table, the dependence dial sentence) and the SOURCES/lesson rows that §1 leans on.

## Verdict: **PARTIAL** (§1 material defect; the surrounding coverage and provenance machinery hold)

The four-test table is mechanically clean, its in-corpus anchors all resolve and support their sentences, its one
external quotation is verbatim against the round lesson's Gate, and its gap premise is reproducible. But §1 itself
carries **three material defects** (F1 contradiction with the entry's own typology, F2 single-ethnography
generalisation, F3 a calibration strip dropped at integration) plus two lesser ones (F4, F5) and two citation-hygiene
notes (F6). Under QUALITY criterion 2 and `verification/calibration-registry.md:39` the §1 framework is presented as
a discovery with **no status code and no reason**, and under QUALITY criterion 1 two of its four tests are asserted
against supports whose own sections mark the facts `(to-verify)`.

The "smallest fix" set below is author-lane advice, not admission.

---

## F1 (HIGH) — the four-test table's *Fails as (owner)* column contradicts the entry's own typology in three places

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:21` (landed bytes):

```
| **Mobility tracks forage** | movement is the production logic, timed to vegetation and season (S058) | a fixed mixed farm: `agrarian-field-system-lexicon.md:62` owns the agropastoral row |
```

`:22`:

```
| **Labour-capped herd** | household labour, not pasture alone, sets the herd a family can hold (S049) | enclosed ranching with wage herders (§3 last row) |
```

Both exemplars are rows of **this** entry's own typology, listed as failures of the register:

* `:50` — `| Agro-pastoral | short moves on stubble and fallow, return to village | fixed village with fields | herd calendar collides with the ploughing peak (\`agrarian-field-system-lexicon.md:62\`) | crop and herd buffer each other |`
  — i.e. §3's own agro-pastoral row *is* "a fixed mixed farm" and *does* cite `agrarian-field-system-lexicon.md:62`.
* `:51` — `| Enclosed / ranching | fenced, individually owned land (S048); stored feed replaces movement \`(to-verify)\` | ranch headquarters | hired stockmen | … |`
  — the "§3 last row" §1:22 points at is "Enclosed / ranching", a member of the typology.
* `:153` — build step 3 offers the register's mobility set as
  `nomadic / semi-nomadic / transhumant / agro-pastoral / enclosed; splitting rule` — so §11 invites the reader to
  build exactly the design §1:21 rejects.
* `:31` — §2's one-owner row says this entry's boundary over `agrarian-field-system-lexicon.md:56,:62` is
  **"herd calendar, transhumance movement logic, herd composition"**. The landed `agrarian-field-system-lexicon.md:62`
  row is `| agropastoral | fields + pasture + transhumance routes | ploughing peak plus **herd calendar**; manure
  contracts | … |` — the "herd calendar" §2:31 claims for this entry sits inside the *other* entry's agropastoral row,
  so the one-owner split and the row assignment disagree.

Sibling model for the same device (`corpus/knowledge/culture-material/hunting-foraging-subsistence.md:43`,
"Failures are diagnostic: a **garden plot** fails 1–2 (agrarian); a **recipe or feast** fails 3 (cuisine); a
**war-bow** fails 2 …; a **totem or sacrifice** …; a **harvest festival** fails 1 (calendar); a **famine food** …"):
every failure exemplar there is *outside* the register's own typology. The pastoral entry's two failure exemplars are
two of its own five typology rows.

**Smallest fix.** Re-cut the two fail cells so no exemplar is a §3 row, and add one half-sentence under the table:
row 2 fail → "a herd kept only to eat crop residues — no movement of its own; the field side stays at
`agrarian-field-system-lexicon.md:62`"; row 3 fail → "a wage-herd unit (feedlot, company ranch): labour hired, not
household"; and under the table: "Agro-pastoral and enclosed (§3) are registers *of this entry* — they fail other
tests, not membership."

## F2 (MEDIUM-HIGH) — "Mobility tracks forage" generalises one WoDaaBe season into the register's universal pass criterion

Entry `:21` states the register's membership condition as "movement is the production logic, timed to vegetation and
season (S058)" for **every** pastoral culture. The row it cites declares the opposite scope —
`corpus/SOURCES.md:87` (S058):

```
… | book | A | the WoDaaBe seasonal movement system in southeastern Niger as observed 1996–97, cattle only;
not Fulani at large, not current practice | chapter y5115e08 item 2 (baartol); chapter y5115e0d | seasonal moves
follow the rains; mobility as a tool for timing an ecological process; named move types | …
```

`verification/calibration-registry.md:37` (**B**) — "Carry population, genre, period, task, and exceptions; **no
extrapolation by resemblance**"; `:38` (**C**) — "do not report one reading as settled"; `:39` (**H**) — "Generate with
it; **label the designer's choices instead of presenting a discovery**". A single 1996–97 WoDaaBe cattle season,
uncoded, is doing the work of the register's defining criterion. The entry scopes S058 correctly everywhere else
(`:153` "S058 for a named-move system"; `:189` living-practice flag), so the defect is local to §1.

**Smallest fix.** `movement is the production logic, timed to vegetation and season — the WoDaaBe case (S058: cattle,
1996–97); the typology in §3 generalises the *form*, not the case` — or mark the cell **H** (designer heuristic).

## F3 (MEDIUM) — §1 carries no calibration status at all; the §1 seat's own calibration block was dropped at integration

QUALITY criterion 2 (`corpus/QUALITY.md:7-9`) requires every framework entry to name its status with the reason, and
the build wave's own contract says it explicitly — `.ufo/waves/round-50/build/ReviewEntryContract.md:77`:
"**Item 2:** each framework claim gets a registry code and a reason". The §1 seat shipped exactly that, in its own
report, with verbatim quotes — `.ufo/waves/round-50/build/ScribeSec01Register.md:18-24`:

```
**Calibration** (QUALITY criterion 2):
- **Mainstream:** the four tests and the mobility typology nomadism → transhumance → agropastoralism (FAO 2001, Pastoral enterprises) …
- **Contested:** "pasture and water must be granted as rights" is Fratkin's policy stance …
- **Discredited frame:** "Pastoralism was seen as an evolutionary stage in human history" (hunting → herding → farming) …
- **Bounded:** the herd-inequality figure … is one Kajiado Maasai study, 1981–85 …
- **Herd is not always capital:** where smuggling or trade lead, "pastoralist economic dependence on livestock is slight." …
- **(to-verify):** Dahl & Hjort 1976, *Having herds* … the book is unopened.
```

The landed §1 (`:14-25`) contains **none** of it: no status word, no registry code, no reason, no pop-mythography
flag at first use. The landed §13 calibration bank (`:177-187`) has 9 rows and covers none of §1's four tests, none of
the register property, and none of the S058 generalisation of F2. The heading itself (`:14`) asserts "**The register
property**" as a discovery of the register, which is precisely what code **H** forbids presenting without a label.

**Smallest fix.** Restore a four-line calibration strip immediately under the §1 table: the four tests are **H**
(designer heuristic, not an established law); "herd management legible before morphological change" is mainstream
within S050's scope; the stage-ladder reading is **R** (S048) and must be flagged on first use in the master claim;
the dependence dial is **B** (EA004 edition-served counts). Each with a one-clause reason.

## F4 (MEDIUM) — §1's per-test evidence was swapped for weaker supports at integration; test 4 now asserts what §7 marks `(to-verify)`

The §1 seat supported three of the four tests with **Bekure & Grandin 1991** (*Maasai herding*, ILCA Systems Study 4)
verbatim quotes and test 2 with FAO 2001's own transhumance definition — `ScribeSec01Register.md:12-16` and
`:34-38`:

```
| **2. Mobility tracks forage**: movement is the production logic, not an episode | transhumance is "the regular
movement of herds among fixed points" [SRC: … y2647e02.htm | same | Transhumance] | …
| **3. Labour-capped herd** … | herd size "determined by the labour needed to manage the herds and flocks" [SRC: …
openknowledge.fao.org/…/x5552e03.htm | same | §1.2, para 1] | …
```

Neither source reached the landed entry: the Bekure 1991 volume was never registered (S048–S069 contain no
Maasai/Bekure row), and S048's own anchor list (`corpus/SOURCES.md:77`) records only "§Classifying pastoral systems;
§Pastoral enterprises (Nomadism, Enclosed systems and ranching); §Pastoral species; §History and origins of
pastoralism" — **not** "§Pastoral enterprises (Transhumance)", "§Overview" or "§Pastoralism and trade", although the
§1 seat opened and quoted all three from the same page (`ScribeSec01Register.md:34-38`).

Landed consequence:

* test 1 (`:20`) rests on **S050**, whose scope is "the 2008 published evidence for when and how sheep, goats, cattle
  and pigs came under management in the Fertile Crescent" (`corpus/SOURCES.md:79`) — a Fertile-Crescent archaeology
  row used as the universal register criterion;
* test 3 (`:22`) rests on **S049**, a policy synthesis (`corpus/SOURCES.md:78`, "not primary ethnography");
* test 4 (`:23`) reads "animals move as gift, loan, bridewealth and raid (§7)" with **no marker**, while the two §7
  rows it leans on are marked `(to-verify)` — `:101` "descent and herd size set the scale `(to-verify)` per culture"
  and `:102` "a loan network is insurance and alliance at once `(to-verify)`". QUALITY criterion 1
  (`corpus/QUALITY.md:5-6`): "A claim the author cannot verify is marked `(to-verify)` inline — **never laundered into
  assertion**."

**Smallest fix.** `:23` → "animals move as gift, loan, bridewealth and raid (§7 — bridewealth scale and loan network
`(to-verify)`)"; and either widen S048's anchor to include "§Pastoral enterprises (Transhumance)" / "§Overview" (append-only
anchor change, logged in the round lesson) or register the Bekure & Grandin 1991 chapter as its own row.

## F5 (LOW-MEDIUM) — S066's Gate bullet is a copy of S065's; §1's quantitative claim has no quoted evidence in the record

`corpus/lessons/round-50.md:50` and `:51`:

```
- S065 — https://www.ahdictionary.com/word/indoeurop.html#IR084700 — accessed 2026-10-21 — entry *peku-, headword
  gloss: "Wealth, movable property. …" Seat: SrcPeku.
- S066 — https://d-place.org/parameters/EA004 — accessed 2026-10-21 — variable Description: "Dependence on animal
  husbandry, relative to other subsistence activities." Seat: SrcPeku.
```

S066 is the D-PLACE EA004 dataset row and is attributed to the same seat as the AHD *peku-* row — a copy-paste, i.e. no
seat of its own opened it. §1:25 then leans on it quantitatively: "the Ethnographic Atlas codes only a small minority
of its societies as near-totally dependent on animal husbandry (S066)". The only quoted S066 evidence anywhere in the
landed record is the variable *Description*; the **value counts** that produce "few societies are near-totally
dependent" (the row's `teaches`, `corpus/SOURCES.md:95`) are quoted nowhere, although the row's anchor is
"variable page Description and Values table". The Gate's job is to hold "each row's URL, access date and verbatim
quote" (`corpus/SOURCES.md:6-8`).

**Smallest fix.** Correct the S066 Gate bullet's seat name and add the Values-table line(s) that show the
near-totally-dependent count; keep §1:25 but consider "(S066, values in the edition served 2026-10-21)".

## F6 (LOW) — two owner citations in §1 are unanchored where every other one carries `path:line`

* `:16` — "the agrarian register about the field" has no anchor (the sibling anchors the same contrast:
  `hunting-foraging-subsistence.md:27` cites `agrarian-field-system-lexicon.md:3`).
* `:23` — the fail cell reads "market sale only: `trade-economy-lexicon.md`" with no line; the seat draft used
  `trade-economy-lexicon.md:3` (`ScribeSec01Register.md:16`).

**Smallest fix.** Add `agrarian-field-system-lexicon.md:3` at `:16` and `trade-economy-lexicon.md:3` at `:23`.

---

## What HOLDS (checked, no defect found)

1. **Every in-corpus `path:line` anchor in the entry resolves at 1c779e4 and supports its sentence** (verified by
   opening each line in the clone; no referenced corpus file changed between base 4ad2683 and the landed commit —
   `git diff --stat 4ad2683 1c779e4 -- corpus/` touches only `QUALITY.md`, `README.md`, `SOURCES.md`, the new entry
   and `lessons/round-50.md`):

   | anchor | line content (abridged) | supports |
   |---|---|---|
   | `culture-material/hunting-foraging-subsistence.md:27` | "…this register argues about the **patch**" | §1:16 "the hunting register argues about the patch" ✓ |
   | `culture-material/hunting-foraging-subsistence.md:36` | "the organism or material is not planted, herded or owned as a standing crop" | §1:20 fail cell quote ✓ |
   | `culture-material/hunting-foraging-subsistence.md:116,:117,:137-146,:170-172,:195` | meat-for-crops `(to-verify)`; storage-as-hinge; §9 decision table; NON-CANON; living-practice flag | §2, §13 ✓ |
   | `culture-material/agrarian-field-system-lexicon.md:56,:62,:80` | heavy-plough row (communal herding after harvest); agropastoral row; secondary-products "(to-verify)" | §2, §3, §11 ✓ |
   | `culture-material/trade-economy-lexicon.md:69` | "Lat. *pecūnia* < *pecus* 'cattle' … Nuer cattle as the idiom of all value" | §5, §2 ✓ |
   | `culture-material/fire-fuel-light.md:37` | "| Dried dung | the herds' output, and therefore the fields' |" | §2, §6, §11 ✓ |
   | `culture-material/textile-technology.md:27` | "**Wool technology is the fork that matters** …" | §2, §6 ✓ |
   | `culture-material/transport-mobility-lexicon.md:95` | "| Draft | human porterage, ox, horse/mule, camelid … |" | §2, §6 ✓ |
   | `culture-material/cuisine-food-lexicon.md:67,:86` | yogurt lineages; pig taboo incl. Harris's cattle-economy reading | §2 ✓ |
   | `linguistics/semantic-fields-lexicon-building.md:70,:105` | "Pastoral wealth vocabulary (herd-age, herd-color …)"; steppe-pastoral bundle | §2, §5, §11 ✓ |
   | `myth-symbol/animal-symbolism.md:73,:110` | Nuer "cattle of money"; "Faunal economy writes the idiom" | §10 ✓ |
   | `myth-symbol/symbolism-synthesis-method.md:69` | "An animal taboo implies a rite; write both or neither." | §10, §11 ✓ |
   | `myth-symbol/sacred-kingship-mythic-charter.md:65` | "the ruler is the god's tenant, servant, or shepherd" | §10 ✓ |
   | `myth-symbol/ritual-liminality.md:63` | calendrical/maintenance rites, milk oblation | §10 ✓ |
   | `myth-symbol/celestial-symbolism-calendars.md:28` | "pastoralists on milky/river figures" | §10 ✓ |
   | `civilizations/mongol.md:40` | "not a ladder … Mobile pastoralism, urban production … can coexist" | §3, §11 ✓ |
   | `civilizations/turkic-steppe.md:148,:193,:194` | "Do not make pastoral production synonymous with economic isolation"; chronicle bias; reject the nomad→civilised ladder | §9, §11 ✓ |
   | `civilizations/scythian-saka.md:70` | "Do not equate pastoralism with total absence of farming" | §9 ✓ |
   | `civilizations/finnic-sami.md:140,:150` | "Do not map herding status directly onto Sámi identity"; "not the eternal condition of all Sámi" | §4, §8, §11 ✓ |
   | `civilizations/dine-navajo.md:125` | "'Traditional' can incorporate introduced animals" | §8 ✓ |
   | `civilizations/inca.md:128` | "'all wool, all alpaca' is too simple" | §4 ✓ |
   | `verification/calibration-registry.md:35-39,:142` | code legend R/C/B/H/T; stage-ladder row | §13, §11 ✓ |

2. **The §1 external quotation is verbatim against the round lesson's Gate.** Entry `:16` — "where hunting-gathering is
   easy, *'there is little or no impetus to herd animals'* (S048)" vs `corpus/lessons/round-50.md:34` — "S048 — … —
   §Classifying pastoral systems: *'there is little or no impetus to herd animals'*". Same string, and inside S048's
   declared scope ("FAO's comparative classification … institutional synthesis, not primary ethnography",
   `corpus/SOURCES.md:77`). Tier B for this use is correct (criterion 6: scoped, not global).

3. **The S-ids cited by §1 all resolve to SOURCES rows whose `used-by` names the entry.** Reproduced the build wave's
   own check (`ReviewEntryContract.md` §2.9 Part B) against the landed bytes: 22 S-ids cited (S048–S069), 0 no-row,
   0 used-by-missing.

4. **The gap premise is reproducible at base, and the coverage counts are real.** In the clone at base 4ad2683:
   `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l` → **0**;
   `grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l` → **0**;
   the un-bounded form hits `culture-material/writing-media-surface-economy.md:3` (the word "sherd" is on that line) —
   exactly as `:4` records. `find corpus/knowledge -name '*.md' | wc -l` → **225**, `ls corpus/knowledge/culture-material/*.md | wc -l`
   → **27** at base; **226 / 28** at 1c779e4. `reports/round-44/scout/K02-gap-scout.md:73` → "| Pastoralism / husbandry | 0 | 0 |
   **named** r35 CM-2 | **carried — reject** |" ✓ (the entry's "round 44 carried pastoralism as a rejected candidate"
   claim is honest). The README sweep is green at the landed commit: `python3 -B reports/round-28/readme/sweep.py` →
   `rows 226 files 226`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `totals_line 226 totals_ok True`,
   `footer_ok True`, exit 0.

5. **Canon hygiene in §1 holds.** §1 decides no canon (it is method-level only). §12:169 begins "**NON-CANON.** The
   people, valley, flocks and numbers below are invented" and the invented name collides with nothing in the corpus
   (`grep -rn "Ketrun"` → only `ScribeSec12Example.md` and the entry itself). §15:199 hands canon to lore-shokunin and
   says the lore intake "is still pending, so every handoff is a candidate, not an import" — the sibling-lane sweep
   report `.ufo/waves/round-50/build/ConnectSiblingPastoral.md` corroborates that lore's intake is unacknowledged
   (`CM-g`), so the entry's hedge is accurate rather than evasive.

6. **The build wave's own mechanical conformance checker passes on the landed bytes** — `ReviewEntryContract.md` §2.9
   Part A (head key order, single H1, no H3+, H2 numbered 1..N, Scope last, Recheck + Calibration H2 present,
   **NON-CANON** present, pipe-table separator, README topic byte-equal, couples partition-labelled, §N refs ≤ H2 count,
   no placeholder words, ≤250 lines) → **PASS**; Part B (S-id → row → used-by) → **PASS**. The defects above are all
   *outside* what that checker tests.

---

## Contract gaps observed outside §1 (logged, not scored against §1)

The landed entry also misses three prose-contract items that the mechanical checker does not test — recorded here so the
author lane can fold them into one edit pass:

* no **decision record** — `grep -o 'DR-PA-[0-9]*'` → NONE, against `ReviewEntryContract.md:69`
  ("**Decision record.** `| ID | Decision | Trigger | Failure if skipped |`. IDs `DR-PA-01…`");
* no build step ends with `*Artifact: …*` (`*Artifact:` count → 0) against `ReviewEntryContract.md:68`;
* the §2 one-owner boundary table has **9** data rows (`:31-39`) against `ReviewEntryContract.md:62` ("15 or more
  rows"); the reviewer's own candidate set (`ReviewEntryContract.md` §4) listed 23 neighbour paths, of which only 9
  reached the table.

## Residual risk and verification gaps

* **Not my scope** (other seats own them): URL re-opens and Gate-quote fidelity for S049–S069; the O operability
  claim and the Ca separability checker/fixture; the README revision row.
* **F2's fix has a source-side dependency**: whether the general form of "mobility tracks forage" can be carried by
  S048's §Transhumance section is a source-seat question (the §1 seat quoted it; S048's registered anchor omits it).
* **F4's fix has a registry dependency**: registering the Bekure & Grandin 1991 chapter would add a row to
  `corpus/SOURCES.md`, which is C's land and append-only — a landed-record change, not a prose edit.
* I did not open any URL (per seat scope); every URL claim here is inherited from the landed SOURCES rows and the
  round-50 Gate, and my S-id findings are about *scope/anchor support*, not about what the pages say.
* The clone `/tmp/r50-review` was removed after the run; the lane working tree was never modified.

## Tooling record

No install, no update. Everything used `git` plumbing, `sed -n`, `grep`, `python3` (system interpreter, stdlib only)
in a throwaway clone under `/tmp`. Nothing was written to the lane except this report.
