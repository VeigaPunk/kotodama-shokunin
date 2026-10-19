# A02 — one-owner verification of the cartography landing (round 47, claim C)

- Seat: `A02` | role: verifier | claim: **C** (coverage) | round 47, loop 2, position 1
- Out path: `reports/round-47/adj/A02-ownership.md` (the only path this seat wrote)
- Observed: **2026-10-19T18:07:49Z**; HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` = `reports/round-47/claims.json:7` `baseline_commit`
- Live partition: **223** entries, `culture-material` **25**, target path **ABSENT**, `git status --porcelain -- corpus/` empty
- Bytes under test: the four fenced draft fragments, not an assembled entry — `C01-entry-a.md` sha256 `cfb42955…`, `C02-entry-b.md` `bfce3aca…`, `C03-entry-c.md` `4b699e06…`, `C04-entry-header.md` `cb5a7489…` (full digests in §8.1). C01/C02 were revised during this wave; the structural findings below were re-checked against the 18:07:49 bytes, and the `- couples:` line is byte-identical across C04 revisions (`cf59ba1f…`, 4096 chars — the same pin C13 reads).

**Verdict: PASS — the cartography entry creates no second owner of any register or topic.** The map is a *composition* system in `culture-material`, explicitly not a member of the symbol-register family; the three mission-named neighbours are clean (cosmology by its own disclaimer, direction by its own disclaimer plus the draft's split, divination by disjoint objects). One ownership edge is undeclared in the draft — the **celestial / star-chart** form — and four ownership-bearing register edges are present in body prose but absent from the machine-readable `- couples:` line. None of these is a second owner in the drafted bytes; they are integration-binding conditions (§7). The live post-landing verdict is **owed**, not passed: the entry is not applied at this HEAD, and V01's live leg remains `could-not-evaluate`.

Scope: this seat adjudicates **ownership only**. C08 owns boundary-table completeness, C13 token resolution, C07 the QUALITY contract, C06 source truth, V01 the post-landing census. I read C08 and C13 only after forming the findings below; agreement is noted, not relied on.

---

## 1. The rule applied — three legs, and what is not a violation

The lane's one-owner rule is a filed precedent, not a slogan:

- `reports/round-42/cov/C05-audit.md:271` — two entries at one topic "would leave the lithic register owned twice — the partition's one-owner rule is violated either way".
- `reports/round-43/cov/C04-contract-audit.md:23` — `N2 topic uniqueness / one-owner rule` marked **FAIL (apply-blocking)**; `:61` — a second entry "would put two entries on one topic … and violate the one-owner rule"; `:152` — a free slug "still creates a second owner".
- `reports/round-43/scout/K02-landing-scout.md:16` — "landing it under a new slug would create a second owner of the same topic".
- `reports/round-47/plan/P01-plan.md:114` — "one owner per topic … verified against the live partition at the landing commit".

I apply three legs:

1. **Topic ownership** — filename, `- topic:`, H1, header fields. A second entry naming the same object is a violation even under a free slug.
2. **Register ownership** — does the entry claim one of the corpus's named symbol registers, or an object an existing entry owns as its register? This is the seat's core question and is *not* answered by C08 (boundary-table completeness) or C13 (token resolution).
3. **Couples discipline** — does the `- couples:` line name every neighbour whose owned object the entry touches, with an ownership split? A body-only split documents the boundary for a reader; a couples edge documents it for the machine gate.

A shared word is **not** a violation. Nor is a method application (the fossil method, the cost ladder) or a composition that cites its components. A violation is a claim of the same *object*: two entries whose scope lines say "we own the X system".

---

## 2. Baseline measured at HEAD `6e9a30d`

```
$ find corpus/knowledge -name '*.md' | wc -l                 -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l           -> 25
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md
                                                              -> ABSENT
$ git status --porcelain -- corpus/                           -> (empty)
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l    -> 0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|graticule|theodolite|compass rose|survey map|lienzo)' corpus/knowledge/ | wc -l
                                                              -> 0
```

The wider probes (11 hits in K01/C05/C07; 13 in C08 with `diagram|cosmogram|plan`) are all metaphor, verb, source title, or an adjacent owner; the nearest is `sacred-topography-pilgrimage.md:5` ("sacred-geography mapping … as a diagram"). No entry names mapmaking as its subject. The partition-level scan (`culture-material/*.md` topics containing map/chart/survey/plan/drawing/diagram) returns zero owners.

**Term overlap between the cartography topic seed and existing `- topic:` lines** (my measurement, exact substrings):

| Seed term | Topic-line owners | Reading |
|---|---:|---|
| `itinerar` | 1 | `sacred-topography-pilgrimage.md:5`, "the fixed itinerary vs the votive ramble" — route typology, not map production |
| `orientation` | 1 | `direction-symbolism.md:3`, "the orientation of prayer and institutions (qibla…)" — the direction register |
| `cosmograph` | 1 real (+2 cross-refs) | `cosmology-cosmography.md:3`; the other two cite it |
| `celestial` | 5 (1 owner + 4 register/cross-ref) | `celestial-symbolism-calendars.md:3` owns the sky; `direction`, `divination`, `symbolism-synthesis-method`, `polynesia` name the register |
| `thematic` | 1 | `maya-classic.md:2` — substring inside "mathe**matic**s"; false positive |
| `cadastr`, `portolan`, `chorographic`, `lienzo`, `atlas`, `graticule`, `theodolite`, `compass rose`, `survey map`, `mapmaking`, `cartograph` | **0** | unowned vocabulary |

So exactly **four** terms in the seed's form typology brush an existing topic line: itinerary, orientation, cosmographic, celestial. The first three are handled by the draft's boundary table; the fourth is not (§3.3, §5).

---

## 3. The register question — what the entry claims, and what it must not claim

### 3.1 The corpus's register family has named owners

- `myth-symbol/symbolism-synthesis-method.md:23` defines the closed family: "the five canonical registers: **color, animal, number, celestial body, direction**", mapped onto value-domains as a grammar.
- `myth-symbol/direction-symbolism.md:3` owns "the direction/spatial register"; its H1 calls itself "the Fifth Register". `:26` adds the explicit disclaimer: an in-world direction code is expressed "never as a compass rose with a legend".
- `myth-symbol/plant-symbolism.md:3` adds flora; `myth-symbol/mineral-stone-symbolism.md:3` adds the lithic register and states the family is "closed at color, animal, number, celestial and direction … plus flora".

Consequence: "register" is a term of art with owners, not a free noun. An entry that presented itself as "the spatial register" or "the map register" would be claiming either `direction-symbolism`'s register (a direct second owner) or an eighth member of a family two entries have already declared closed.

### 3.2 What the cartography draft actually claims — and it disclaims the family

- `C01 §1` (master claim, `C01-entry-a.md:88`): "A map is an argument about space, not a picture of it." The added sentence is the entry's own: "a map is a citation in cartographic form — the survey supplies its precision, the convention supplies its readability, the patron supplies its warrant, and the sheet pays for all three with the omissions it cannot show."
- `C01 §1` one-owner statement (`:105`): "**The map is a composition register, not a symbolic register.** The five canonical symbol registers (`myth-symbol/symbolism-synthesis-method.md:23`) own what a direction, color, number, animal or celestial body *means*; this entry owns only the **syntax of the sheet** — which register may occupy which cartographic slot, and what a blank means." It adds that this is why the entry belongs in `culture-material`: "a made object with a production chain, not a value system".
- `C01 §2.2` (`:145`): "The sheet composes four registers it does not own: **direction** (orientation, the rose), **name** (toponymy), **number** (scale, coordinates, the graticule), and, where the culture has a color code, **color** (political fill). The map owns the *slot grammar* … This entry never coins a component register; it only composes them."
- `C01 §C.4` (`:324`): "No claim that the entry is a sixth *symbolic* register. §1's one-owner statement explicitly makes it a **composition** register in `culture-material`, not a member of the five-register family in `myth-symbol`."
- `C04 - scope:` (`C04:162`): "This entry owns the map as a made instrument and a claim — the survey chain, projection and scale, symbolization, reproduction, and the map's silences." It does not say "register".

**Verdict on the core question: no register is second-owned.** The draft claims a composition syntax, delegates each component register to its owner, and explicitly refuses membership in the family. This is the correct one-owner shape, and it survives the r43/r42 standard because no other entry owns "the map as a made instrument".

**But the disclaimer is load-bearing, and the word is overused.** Measured: **58** occurrences of `\bregister` in **801** fenced body lines, in at least five senses:

| Sense | Example |
|---|---|
| composition register (the entry's own) | `C01:105` |
| route register | `C01 §2.1` itinerary row ("a **route register**") |
| land/cadastral register | `C01 §4.1`; `C02 §5.1`; `C03 §10` |
| working / monument register (product class) | `C02 §6.4` ("The two registers") |
| silence register (a decision artifact) | `C03 §13 DR-CT-06` |

If assembly drops `C01 §1`'s one-owner statement, `§2.2`, or `§C.4`, a reader who sees the `§2` heading "What makes a map a register" plus 58 uses of the word can reasonably infer an eighth register claim. That is a **naming risk, not a second owner** — condition C-A02-1. The safe fix is one sentence in `§1` and, optionally, retitling `§2` to "What makes a map a map — the five-condition test". The heading is also the imported r42 lithic phrase ("the property that makes stone a register", `reports/round-42/cov/C01-entry-1.md:53`; flagged as a mission/template mismatch at `reports/round-47/scout/K02-seed-extract.md:224-228`). The content is cartography-specific; only the template vocabulary travelled.

### 3.3 The register-owner table

| Register / owner | What it owns (cited) | Draft treatment | Verdict |
|---|---|---|---|
| **direction** — `direction-symbolism.md` | direction/spatial register; frames; partitions; left/right; rotation; `:51` compass trap; `:26` "never as a compass rose with a legend" | `C01 §1.1`, `C04 couples` cite `:51`; map convention (which way up, rose, north arrow, graticule) claimed; no direction meaning restated | **PASS**; add `:26` (C-A02-6) |
| **color** — `color-symbolism.md` | what a colour means; dye-scarcity economics | `C01 §3.5`: "The map does not own the code; it cites `color-symbolism.md` and must not invent a color meaning the register does not license" | **PASS in body, couples omission** (C-A02-3) |
| **number** — `number-symbolism.md` / `numerals-and-measures.md` | number symbolism; counting lexicon and measures | `C01 §2.2`: "a measure to `numerals-and-measures.md` and `trade-economy-lexicon.md`" | **PASS in body, couples omission** (C-A02-3) |
| **celestial body** — `celestial-symbolism-calendars.md` | "The naked-eye sky as the worldbuilder's highest-yield symbolic system" (`:3`): sun/moon, planet-god identities, constellation vs asterism naming, eclipse omens, calendar mechanics | `C01 §2.1` star-chart row (`:132`); `C01 §4.1` "Celestial / star chart" form (`:244`); `C02 §5.4` star charts as a stereographic case | **UNDECLARED EDGE** — no couples token, no boundary sentence, 0 mentions of the owner in all four fragments (C-A02-2) |
| **animal** — `animal-symbolism.md` | fauna register, bestiary, crest | 0 hits; not touched | **no edge needed** |
| **five-register method** — `symbolism-synthesis-method.md` | the closed family and its audit (`:23`, `:29`) | `C01 §1`/`§2.2` cite `:23`; `C02 §5.6` calls its symbol set "the map's version of the register grammar"; no family member claimed | **PASS in body, couples omission** (C-A02-3) |
| **lithic** — `mineral-stone-symbolism.md` | lithic register; stone jobs and properties | No stone claim. The "container-name fossil" (`C02 §9`) is a cross-cutting method used by `vessel-container-lexicon.md:71`, `funerary-material-culture.md:22`, and `writing-media-surface-economy.md:62`; `mineral-stone-symbolism.md` has **0** hits for `container`/`fossil` | **PASS**; method application, not re-own |
| **name** — `naming-systems.md` | toponymy, critical toponymy, name taboo | `C01 §1.1`, `C04 couples`; delegation explicit | **PASS** |

The only row that is not a pass is the celestial one. As drafted, the star-chart row is one table row and one form row; it names "Ptolemy's catalogue" and the "Dunhuang star map" as exemplars but does not name constellations, planet-god identities, eclipse omens, or calendar mechanics. So it creates **no second owner today**. But it claims a produced document whose *content* has an owner, and nothing in the draft says where the line is. That is the ownership-bearing condition.

---

## 4. The three mission-named neighbours

### 4.1 `divination-omen-systems.md` — **NO COLLISION**

- Its `- topic:` (`:3`) owns the question → technique → closed sign space → licensed reader → prescription system, with a fourteen-row technique typology, including "Ifa and geomantic 16/256 systems" and "terrestrial and astral omen compendia".
- Its own §8 boundary table (`:147-159`) names celestial omens, cosmology, motif index, ritual liminality, naming, the myth-consistency gate and the civilization bases. **It does not name cartography**, for the right reason: a reading is not a made sheet.
- The only `map` in the file is the verb "the code **maps** to twelve prescriptions" (`:163`); the nearest conceptual overlap is geomancy (`:189`), a sand-figure reading technology, not a survey map.
- The draft contains **zero** divinatory material: word-boundary `divinat|geomanc|omen` = 0 across the 801 fenced body lines (the two raw `omen` substrings are "phenomenon" and "moment"). No geomantic figure, no omen compendium, no map-as-divination-instrument clause.
- `C04 couples` has no divination token; `C01 §1.1` has no divination row.

**Verdict: the objects are disjoint; no couples token is required for ownership.** Documentation note (C-A02-4): add a one-line non-collision row to `§1.1` — "divination owns the sign-reading technology; a map used as a divination instrument is a reading, not map production" — so the mission's named cross-check is visible to C08/V01 and to a later reviser. This agrees with C08's P3-1, independently reached.

### 4.2 `cosmology-cosmography.md` — **NO COLLISION; its disclaimer is the entry's charter**

- `:71` (T-O row): "T-O diagrams are symbolic, **not survey maps** (§10)."
- `:102`: "T-O diagrams are symbolic devices, **not cartographic** claims."
- `:133`: "Toponyms are cosmographic claims … A fictional map is a set of etymological arguments."

The draft quotes `:71`/`:102` in `C01 §1.1`, `C04 - gap filled:` and `C04 couples`; `C01 §1.1` also cites `:133` and delegates the derivation table to `naming-systems.md`. The `§4.1` cosmographic form row says "cosmography owns this form; cited as the contrast case, never restated" — C08 P1-1 rightly asks for the sharper "content vs production" wording, but the ownership direction is correct either way. No five-axis typology, flat-earth calibration, or cosmogram typology is restated.

**Verdict: no second owner.** The positive evidence is the partition's own disclaimer; the draft cites it rather than absorbing it. Condition C-A02-5: keep the `:71`/`:102` quotations through assembly; do not expand the cosmographic form into world-model content.

### 4.3 `direction-symbolism.md` — **NO COLLISION, but the explicit disclaimer `:26` is unused**

- `:3` owns "the direction/spatial register"; `:51` owns the "compass trap" (true vs magnetic north, declination).
- `:26` is the positive disclaimer of the map convention: an in-world direction code is expressed as "ritual regulation, omen lore, house rules, and processional custom — **never as a compass rose with a legend**."

The draft splits correctly: `C01 §1.1` says direction owns "the direction register … the compass trap (`:51`)" and this entry owns "the sheet convention: which way is up, the compass rose, the north arrow, the graticule"; `C04 couples` repeats the split. `C01 §3.4` and `C02 §5.6` use the convention without restating frames, cardinal coinage, partitions, left/right, or rotation. No direction-meaning content was found in the body.

**Verdict: no second owner.** The split rests on `:51` alone. `:26` is the exact sentence that licenses the entry's ownership of the rose/arrow as *map convention rather than emic direction code*, and it is unused (C-A02-6). Adding it makes the boundary as checkable as the cosmology one (`:71`/`:102`).

---

## 5. The remaining neighbours — ownership verdicts

| Neighbour | Owns (cited) | Draft clause | Verdict |
|---|---|---|---|
| `sacred-topography-pilgrimage.md` | place register, route-as-rite, site typology (`:5`); "Sacred geography as a diagram — and the era drift of a holy map" (`:96`); "**The map is a claim**" (`:98`); six drift mechanisms (`:99`) | `C01 §1.1` cites `:5,:69` and claims only how a route is surveyed and drawn; no route-type or drift-mechanism restatement was found | **PASS on ownership**; attribution note C-A02-7: `:98` is a prior articulation of the entry's master claim; cite it (and `cosmology:133`) so the entry generalizes rather than appears to originate |
| `architecture-settlement-lexicon.md` | city-plan lexicon; castrum grid; groma (`:95`) | `C01 §1.1` cites `:95`; claims land survey as a map-production step; `C02 §5.2` cites `:95,:101` | **PASS** |
| `writing-media-surface-economy.md` | seven surface families; cost ladder (`:3`); `- scope:` excludes "printing as an industry beyond the §9 calibration note" (`:33`) | `C01 §1.1` and `C04 couples` split surface economy vs map-specific media/reproduction; `C02 §5.7`/`§6.4` cite the cost ladder; no surface-family list restated | **PASS**; condition C-A02-8: cite `:33` to show the print/reproduction ownership is a declared exclusion, not an assumed gap |
| `transport-mobility-lexicon.md` | ROUTE layer and maintenance institution (`:28`, `:117` DR-TR-02) | `C01 §1.1` claims representation only; `C03 §10` applies the maintenance clause | **PASS** |
| `mesoamerica-primary-sources.md` | lienzo / cartographic-history **source class** and provenance (`:58`) | `C01 §1.1` and `C04 couples` split genre vs source class; `C03 §12` adds living-practice flags; no manuscript inventory restated | **PASS** — the sharpest conditional collision entering the round, disarmed by an explicit split |
| `timekeeping-instruments.md` | five instrument families; astrolabe as SKY timekeeper (`:27`); "longitude at sea" (`:50`) | `C04 couples` cites `:50` and splits "the coordinate problem the map inherits, not the instruments"; `C02 §5.1` cites `:50` | **PASS** |
| `polynesia-navigation.md` | navigation operations; "a mental bearing framework, not a chart" (`:60`); horizon compass etc. (`:52`) | `C04 couples` cites `:52`; `C02 §5.1` states the chartless boundary; no navigation method restated | **PASS** |
| `naming-systems.md` | toponymy; "a map is an archive of coups" (`:70`); name taboo (`:97`) | `C01 §1.1`, `C04 couples` delegate the toponym layer | **PASS** |
| `craft-artisan-lexicon.md` | workshop as speech community; guild ladder; six-type mark taxonomy (`:3,:56-63,:76-87`) | `C02 §7` builds the map trade and cites the ladder/marks; `C04 couples` cites `:44` (the material-grading row, not the ladder — C08 P1-2's citation defect) | **PASS on ownership**; fix the anchor per C08 P1-2 |
| `trade-economy-lexicon.md` | measures and sacred standardization; money words; contract/debt (`:3,:92,:121`) | `C01 §3.6`, `C02 §8` claim the map as a legal/territorial instrument; `C04 couples` cites `:92,:121` | **PASS**; C08 P1-4 asks for a table row |
| `sacred-kingship-mythic-charter.md` | the **mythic** charter of rule; the royal register (`:3`) | `C02 §8.2` states the split: mythic charter there, legal charter here; no couples token | **PASS on ownership; couples omission** (C-A02-3) |
| `mineral-stone-symbolism.md` | lithic register; closed family (`:3`) | no stone claim; container-name fossil is a method applied from `vessel:71`/`funerary:22`/`writing-media:62`; the landed lithic entry has 0 `container`/`fossil` hits | **PASS** — no re-own |
| `synthesis/dialect-faction-map-workflow.md` | dialect-feature mapping (verb) | not touched | **no edge needed** |

Two notes on the table:

- **The "map is a claim" thesis is pre-stated twice.** `sacred-topography:98` says it for holy maps; `cosmology:133` says it for toponyms. `C01 §1` states the general thesis without citing either sentence in the master-claim paragraph (it cites `:5`/`:71`/`:102` elsewhere in `§1.1`). This is not a register collision — a thesis is not an owned object — but the entry should attribute the prior articulations (C-A02-7) so a reviewer does not read it as a duplicated thesis.
- **C02's §9 "container-name fossil" is not a re-own of the lithic draft.** The landed `mineral-stone-symbolism.md` does not contain the mechanism (0 hits); the method is carried by `vessel-container-lexicon.md:71` (ear/lug), `funerary-material-culture.md:22` (sarcophagus) and `writing-media-surface-economy.md:62` (tool-name fossil). C02 applies it to *map* words (`mappa`, `charta`, `atlas`, `portolan`, `cartouche`) and cites the method precedent. No second owner.

---

## 6. Couples verification — actual bytes, and the mechanical blind spot

### 6.1 The line passes

I extracted C04's fenced head block and ran a resolver against the **real entry directory** `corpus/knowledge/culture-material/` (the file will live there; bare culture-material basenames and `../partition/…` paths must resolve from that base):

```
couples physical span: 1 line(s)
backticked .md refs on first line: 21
unresolved: none
required-boundary refs missing: none
other topic owners: none
VERDICT: PASS
```

The eight required boundary edges — cosmology, sacred-topography, direction, architecture, writing-media, transport, mesoamerica, naming — are all on the first physical line. The line sha256 is `cf59ba1f311619dbe527bfb1d3c716ae338f56d601af675e52e343384e9f5663` (4096 chars, 21 tokens), matching C13's pin. Negative controls prove the checker is not vacuous:

- a synthetic copy with the couples field wrapped after the third ref → span 2, 5 required edges off the first line → **FAIL**;
- a synthetic copy with the transport token removed → span 1, 8→7 refs, transport missing → **FAIL**.

### 6.2 The audit gate reads only the first physical line

`reports/round-19/audit/entry-audit.py:74-97` (`couples_targets`) does `re.search(r"^- couples:\s*(.*)$", text, re.M)` and resolves refs from **that one line only**. It does not join continuation lines. Measured corpus-wide: **1 of 223** entries has a couples field wrapped beyond the first physical line — `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, and its first line carries **0** backticked `.md` refs. On that entry the gate resolves zero targets and reports no unresolved refs: a vacuous pass. For the new entry the consequence is concrete — a wrap or a reflow would hide whole ownership edges from the landing gate while the resolver census still read green. C13 warns "do not reflow it into a hard wrap"; this measurement is the reason. Condition C-A02-9: keep the field on one physical line; the integrator should re-count tokens after apply.

### 6.3 Body-cited files absent from the couples line

Extracting only the fenced bodies (801 lines), stripping `:line` suffixes, and resolving basenames against `corpus/knowledge/`: **45** distinct `.md` refs, of which **9** name a real corpus file that is **not** in C04's couples line.

| Absent from couples | Ownership-bearing? | Body already declares the split? |
|---|---|---|
| `myth-symbol/symbolism-synthesis-method.md` | **yes** — the five-register family the entry invokes | `C01 §1` (`:105`), `§2.2` (`:145`); `C02 §5.6` |
| `myth-symbol/color-symbolism.md` | **yes** — the color register | `C01 §3.5`: "The map does not own the code; it cites `color-symbolism.md`" |
| `linguistics/numerals-and-measures.md` | **yes** — the number/measure register | `C01 §2.2`: "a measure to `numerals-and-measures.md`" |
| `myth-symbol/sacred-kingship-mythic-charter.md` | **yes** — mythic vs legal charter | `C02 §8.2` |
| `culture-material/fire-fuel-light.md` | no — archive-destruction case | source use only |
| `culture-material/funerary-material-culture.md` | no — sarcophagus fossil precedent | method use only |
| `synthesis/loanword-material-dating.md` | no — two-clocks rule | method use only |
| `civilizations/maori.md` | no — named-knowledge-holder precedent | living-practice use only |
| `verification/to-verify-triage-protocol.md` | no — to-verify process | process use only |

The four ownership-bearing omissions are not second owners **because the body states the split in each case**. But the `- couples:` line is the machine-readable declaration QUALITY clause 3 (`corpus/QUALITY.md:13-15`) asks for, and C13 cannot see a missing token. Three of the four were explicitly requested by C01's own handoff to C04 (`C01 §C.3`: "should name … `myth-symbol/symbolism-synthesis-method.md` … `linguistics/numerals-and-measures.md` … `verification/to-verify-triage-protocol.md`"); C04's line omits all three. That is a cross-seat integration defect, not an ownership collision. Condition C-A02-3: add the four ownership-bearing tokens (and, at C13's discretion, the five method/source tokens).

### 6.4 Corroboration, not reliance

C08 independently reaches the same ownership verdict and the same celestial/sacred-kingship omissions (P1-5, P1-6, P3-1); C13 independently resolves 21/21. My additions are the register-family analysis (§3), the body-vs-couples count (§6.3), the first-line gate blind spot (§6.2), and the attribution note (§5). Nothing in my verdict depends on their findings.

---

## 7. Binding conditions on the landing

None of these is a second owner in the drafted bytes. They are ordered by ownership weight.

1. **C-A02-1 (register naming, hard).** Keep `C01 §1`'s one-owner statement, `§2.2`'s "composes four registers it does not own", and `§C.4`'s "not a sixth symbolic register" through assembly. Do not retitle the entry as a register. Recommended: add one sentence in `§1` defining "register" as the composition syntax and pointing to `symbolism-synthesis-method.md:23` / `direction-symbolism.md:3`; optionally retitle `§2` to "What makes a map a map". This is the condition that keeps the answer to the mission's question "no".
2. **C-A02-2 (celestial edge, ownership-bearing).** Add `myth-symbol/celestial-symbolism-calendars.md` to `- couples:` and a boundary sentence/row: celestial owns sky objects, constellation naming, planet-god identities and calendar mechanics; cartography owns the star chart as a produced document (observation, projection, print). The draft currently mentions the owner **0** times.
3. **C-A02-3 (ownership-bearing couples, must).** Add `symbolism-synthesis-method.md`, `color-symbolism.md`, `numerals-and-measures.md`, `sacred-kingship-mythic-charter.md` to the couples line, or remove the corresponding body citations. The body splits are already written; the line is what the gate reads.
4. **C-A02-4 (divination disposition, note).** Add the one-line non-collision row to `§1.1`. No couples token required; the objects are disjoint.
5. **C-A02-5 (cosmology, preserve).** Keep the `:71`/`:102` quotations and the "content vs production" wording for the cosmographic form (C08 P1-1); do not expand it into world-model content.
6. **C-A02-6 (direction, strengthen).** Add `:26` ("never as a compass rose with a legend") to the direction row/couples parenthetical, alongside `:51`.
7. **C-A02-7 (attribution, note).** Cite `sacred-topography-pilgrimage.md:98` ("The map is a claim") and `cosmology-cosmography.md:133` ("A fictional map is a set of etymological arguments") where the master claim is stated, so the entry is seen to generalize a filed thesis rather than originate it.
8. **C-A02-8 (writing media, note).** Add `:33` (the scope exclusion of "printing as an industry") to the writing-media parenthetical, so the map-reproduction ownership is a declared transfer.
9. **C-A02-9 (mechanical, hard).** The couples field stays one physical line; the integrator re-counts 21 tokens after apply and does not reflow. A wrapped field is invisible to `entry-audit.py:74-97` (measured on the corpus's one wrapped entry).

---

## 8. Verdict, limits, and what is still owed

### 8.1 Verdict

**PASS — no second owner of any register or topic, in the drafted bytes.** The entry is a composition system in `culture-material`, explicitly not a symbol register; the three mission-named neighbours are clean; the seven K02 neighbours are dispositioned; the couples line resolves 21/21 on one physical line with all eight boundary edges. The residual defects are documentation/coupling (celestial, four register edges), a citation anchor (craft `:44`), and naming clarity ("register"). None is a second owner; C08's P1 list and my conditions are the integration checklist.

### 8.2 Limits — stated, not hidden

- **The entry is not applied.** At 18:07:49Z the live path is absent, the corpus is 223/25 and clean. This is a **pre-landing** ownership verdict on four draft fragments, not a post-landing check on live bytes. V01's live verdict remains `could-not-evaluate`; the post-landing leg must be re-run (Appendix B works on the landed file).
- **The fragments moved during the wave.** C01/C02 were revised repeatedly (C08 pinned earlier shas; C13 observed three C04 container shas). My pin is the 18:07:49 set: C01 `cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d`, C02 `bfce3acaf20e527b949a45b708f1d9e10c9ab9447651375f89075f1c80be3600`, C03 `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5`, C04 `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0`. A later revision voids the line numbers, not the section-level findings; re-run Appendix B on the assembled file.
- **I did not verify** the truth of every `path:line` citation (C06), the boundary table's completeness (C08), the README edit (C09), the staged sweep (C10), or the post-landing census (V01). My couples check verifies resolution and boundary coverage, not the truth of each parenthetical (C13/C06).
- **No corpus write, no tools write, no filed-byte edit, no runner execution, no commit/network.** The only deliverable is this file; the checker and extracted fragments live in disposable `.scratch/a02/`.
- **Could-not-evaluate:** the assembled entry's actual bytes (four fences, no concatenation yet); whether the assembler preserves the disclaimers; whether a later revision adds celestial content. These are named, not inferred as green.

### 8.3 What would flip the verdict to FAIL

- The entry claims to be a symbol register (drops `C01 §1`/`§2.2`/`§C.4` and keeps the "map is a register" heading) — then it is an eighth-register claim and collides with the closed family.
- It calls itself "the spatial register" — direct collision with `direction-symbolism.md:3`.
- It restates the five-axis cosmology typology, the pilgrimage route types, the direction partitions, the city-plan lexicon, the seven surface families, the lienzo provenance table, or the workshop ladder — each is a second owner of a named object. C08's B1–B15 checks these.
- It expands the star-chart section into constellation naming/planet-god identities/eclipse omens without the celestial split — then the undeclared edge becomes a second owner.
- A later seat lands another entry on "the made map" under a different slug — the r43 failure mode; the one-owner rule forbids it regardless of the count.

---

## Appendix A — command transcript (trimmed)

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l                 -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l           -> 25
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md
                                                              -> ABSENT
$ git status --porcelain -- corpus/                           -> (empty)
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l    -> 0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|graticule|theodolite|compass rose|survey map|lienzo)' corpus/knowledge/ | wc -l
                                                              -> 0
# term-overlap: itinerary 1, orientation 1, cosmograph 1(+2 refs), celestial 5,
#   thematic 1 false positive ("mathematics"), all others 0
# register-family owners: symbolism-synthesis-method:23 (five), direction:3 (spatial),
#   plant:3 (flora), mineral:3 (lithic; family closed)
# draft core clause re-check at 18:07:49:
composition register            C01=1
sixth *symbolic                C01=1
Celestial / star chart         C01=1
color-symbolism                C01=1
numerals-and-measures          C01=2
sacred-kingship-mythic-charter C02=2
celestial-symbolism-calendars  C01=0 C02=0 C03=0 C04=0
# fenced bodies: 801 lines; 45 distinct .md refs; 9 resolvable corpus files absent
#   from C04 couples (4 ownership-bearing, 5 method/source); 58 \bregister hits
# divination cross-check: \bdivinat=0, \bgeomanc=0, \bomen=0 in the fenced bodies
#   (raw "omen" substrings are "phenomenon" and "moment")
# couples check against corpus/knowledge/culture-material:
#   span 1 line, 21 refs, 21/21 resolve, 8/8 required, 0 other topic owners -> PASS
#   negative controls: wrapped -> FAIL (2 lines, 5 required off line 1);
#                      missing -> FAIL (transport missing)
# couples line sha256 cf59ba1f311619dbe527bfb1d3c716ae338f56d601af675e52e343384e9f5663, 4096 chars
# entry-audit.py:74-97 reads only the first physical couples line; 1/223 entries
#   is wrapped (phonetics-phonology.md:72-77), with 0 first-line backticked refs
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-19T18:07:49Z
```

## Appendix B — re-runnable one-owner check

Run from the lane root against the assembled or landed entry. The base directory is the entry's real directory, because the couples tokens are entry-relative. Expected on the C04 draft: `PASS`, 1 line, 21 refs, 0 unresolved, 0 missing, 0 other owners.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
ENTRY=corpus/knowledge/culture-material/cartography-and-mapmaking.md
python3 - "$ENTRY" "$(dirname "$ENTRY")" <<'PY'
import os,re,sys,glob
entry,base=sys.argv[1],sys.argv[2]
req=["corpus/knowledge/myth-symbol/cosmology-cosmography.md",
     "corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md",
     "corpus/knowledge/myth-symbol/direction-symbolism.md",
     "corpus/knowledge/culture-material/architecture-settlement-lexicon.md",
     "corpus/knowledge/culture-material/writing-media-surface-economy.md",
     "corpus/knowledge/culture-material/transport-mobility-lexicon.md",
     "corpus/knowledge/civilizations/mesoamerica-primary-sources.md",
     "corpus/knowledge/linguistics/naming-systems.md"]
L=open(entry,encoding='utf-8').read().splitlines()
i=next((k for k,l in enumerate(L) if l.startswith('- couples:')),None)
if i is None: print('FAIL no - couples:'); sys.exit(1)
j=i
while j+1<len(L) and (L[j+1].startswith('  ') or L[j+1].startswith('\t')): j+=1
refs=re.findall(r'`([^`]+\.md)`',L[i])
resolved={}
unres=[]
for r in refs:
    cands=[os.path.normpath(os.path.join(base,r)),os.path.normpath(os.path.join(os.getcwd(),r)),
           os.path.normpath(os.path.join('corpus','knowledge',r))]
    hit=next((c for c in cands if os.path.isfile(c)),None)
    (resolved.__setitem__(r,os.path.realpath(hit)) if hit else unres.append(r))
missing=[r for r in req if not any(os.path.realpath(r)==p for p in resolved.values())]
owners=[]
for f in glob.glob('corpus/knowledge/*/*.md'):
    if os.path.realpath(f)==os.path.realpath(entry): continue
    for n,l in enumerate(open(f,encoding='utf-8'),1):
        if l.startswith('- topic:') and re.search(r'cartograph|mapmak|portolan|cadastr',l,re.I):
            owners.append(f'{f}:{n}')
print(f'couples span: {j-i+1}; refs: {len(refs)}; unresolved: {unres or "none"}')
print(f'required boundary missing: {missing or "none"}; other topic owners: {owners or "none"}')
ok=(j-i+1==1) and not unres and not missing and not owners
print('VERDICT:','PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
PY
```

This checker is ownership-scoped. It does not replace C13's resolver census, C08's B1–B15 boundary checklist, C07's contract audit, or V01's post-landing census; it answers the question this seat was given: **does the cartography entry create a second owner of any register?** The answer, on the drafted bytes, is **no** — provided the nine conditions in §7 are carried into assembly.
