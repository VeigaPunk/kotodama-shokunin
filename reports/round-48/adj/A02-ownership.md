# A02 — one-owner verification: cartography (claim C)

- Seat: `A02` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/adj/A02-ownership.md` (this file)
- Non-author statement: I drafted no cartography fragment in r47 or r48. Every judgement below is from live `corpus/` bytes at `a01405d` or from filed r47 bytes, each cited by `path:line`. I edited no corpus byte and staged nothing under `corpus/`.

**Verdict in one line.** **No second owner exists at the baseline, and the cartography landing creates none at the file level** — the slug is free, 0 filenames and 0 `- topic:` lines own the register, and no existing entry's `- couples:` line claims it. The r47 draft carried a claim-level collision with `cosmology-cosmography.md:27` and omitted four adjacencies; the **r48 right-sized draft closes both** (gap line `C02-header.md:115`, split at `C01-entry.md:103`, 12-row table at `:107-118`, ladder corrected to `:54-65`). **Two residuals remain:** the `- couples:` line (`C02-header.md:130`) has 19 tokens and omits the two table neighbours `celestial-symbolism-calendars` and `sacred-kingship-mythic-charter` (expected 21), and the architecture row still cites `:95` without `:101`. File-level ownership is clean; the residual is couples/table self-consistency, not a second owner.

---

## 1. Baseline measured (not carried)

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
```

The live partition is 25 files (`ls corpus/knowledge/culture-material/`), and the proposed slug sorts between `calendar-festival-systems.md` (5th) and `costume-semiotics.md` (6th) — reproduced, not carried.

**Round-48 write surface at my read cut:** `find reports/round-48 -type f` → `claims.json`, `targets.json`, `telemetry/dispatch-declared.json` only. **No r48 entry draft existed**, so §3–§4 test the r47 draft (`reports/round-47/cov/C01-entry-a.md`, `C02-entry-b.md`, `C04-entry-header.md`, `C08-boundary.md`) as the nearest successor artifact, plus the live partition. The successor must re-pass §5's predicates.

---

## 2. What counts as an owner

Four tests, in order of authority. The first two decide ownership; the third proves no prior claim; the fourth tests whether the *new* entry concedes each neighbour's object.

1. **Filename test** — a basename carrying the register's vocabulary.
2. **Topic-line test** — the entry's single `- topic:` line names the register as its subject (`reports/round-28/readme/sweep.py` compares this line to the README row, so it is also the index contract).
3. **Couples-claim test** — does any existing `- couples:` line assert ownership of map/survey production?
4. **Boundary-statement test** — does the new entry name each neighbour's owned object and say what it takes instead, without restating it?

A **body mention is not ownership.** This lane's precedent is explicit: `mineral-stone-symbolism.md:3` landed the lithic register over many by-product mentions, and `plant-symbolism.md:3` landed flora while fauna was owned (`reports/round-44/scout/K02-gap-scout.md` §2). So the ~29 files / ~35 tight hits are dispositioned, not counted.

**Measured test 3:**

```
$ grep -rniE '^- *couples:.*(cartograph|mapmak|survey map|map of|maps )' corpus/knowledge/
(no output)
```

**Measured test 2 — every hit is metaphor, verb, or a handoff (not ownership):**

| `topic:` hit | Why it is not a map owner |
|---|---|
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "purity is … a **boundary map**" — explicit metaphor |
| `synthesis/dialect-faction-map-workflow.md:2` | "**Map** dialect features … onto travel networks" — verb |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "sacred-geography **mapping** … as a diagram" — owns the place register and route, not the made sheet |
| `linguistics/sound-symbolism.md:3`, `linguistics/sociolinguistics-registers.md:3` | "three-way **map**" / "register maps to era" — metaphor/verb |
| `myth-symbol/number-symbolism.md:3` | "variance **survey**" — statistical sense |

No `- topic:` line names cartography, mapmaking, portolan, cadastral or survey as its subject. `grep -rni 'star chart' corpus/knowledge/` → **0** hits, so no entry owns the star-chart artifact either.

---

## 3. The one-owner matrix

Each row is a live register that could be a second owner. "Guard" means the entry may take the listed object **only if** it cites the neighbour and does not restate it. Every live line below was re-read at `a01405d`.

| # | Neighbour (owner) | Live evidence, verbatim fragment | Owned object | What cartography may take | Verdict |
|---|---|---|---|---|---|
| 1 | `myth-symbol/cosmology-cosmography.md` | `:27` "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." `:71` "T-O diagrams are symbolic, not survey maps"; `:102` "T-O diagrams are symbolic devices, not cartographic claims"; `:133` "A fictional map is a set of etymological arguments" | the world model; the T-O **cosmogram**; toponyms as cosmographic claims | the **surveyed, projected, reproduced sheet** as production — *only with the `:27` split stated* | **GUARD — claim-level collision as drafted** (O1) |
| 2 | `myth-symbol/sacred-topography-pilgrimage.md` | `:5` "sacred-geography mapping (a culture's holy sites as a diagram: radial, quartered, linear-corridor, or archipelago)"; `:69` the three route types (fixed itinerary / votive ramble / circuit) | the holy-site typology, route-as-rite, the **site diagram** | the route **as drawn content**; the itinerary/souvenir sheet as a document genre | clear with guard |
| 3 | `myth-symbol/direction-symbolism.md` | `:51` "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic …" | frames of reference, cardinal coinage, rotation, orientation of the dead | the **sheet convention**: which way is up, compass rose, north arrow, graticule (`grep -rni graticule corpus/knowledge/` → 0, so unowned) | clear with guard |
| 4 | `culture-material/architecture-settlement-lexicon.md` | `:95` "surveyed with the **groma** … The grid is cadastral: a state that *measures land* builds this city"; `:101` design lever "(a) … **instrument + founding rite + claim word**" | the built plan, castrum grid, groma sentence, the instrument+rite+claim-word lever | **land survey as a map-production step**; the plan as a cadastral object | clear with guard — add `:101` to the row (O5) |
| 5 | `culture-material/writing-media-surface-economy.md` | `:3` "the **seven surface families** …"; `:69-73` the surface→user→genre ladder; `:78` "Cheapness widens the *base*, it does not redistribute the *authority*" | the surface economy, cost ladder, survivor's ledger | **map-specific media and reproduction** (vellum, cloth, copperplate, atlas) | clear with guard |
| 6 | `culture-material/transport-mobility-lexicon.md` | `:28` "a route is only real if someone maintains it"; `:117` `DR-TR-02` maintenance clause | routes, vehicles, the maintenance institution | **how a route is drawn** — line, stage, season | clear with guard |
| 7 | `linguistics/naming-systems.md` | `:40` onomastics split; `:70` "Every renaming is datable; **a map is an archive of coups**"; `:97` royal-name taboo shifting place spelling | toponymy and critical toponymy | the **toponym layer of the sheet**; the map as a naming archive | clear; do **not** "correct" the `:70` quote to "renamings" — that was r47 B3's false accusation |
| 8 | `civilizations/mesoamerica-primary-sources.md` | `:58` "Lienzos and **cartographic histories** … the copy chain is the evidence" | the lienzo source class and its provenance | the genre as a map form and as a legal document | clear with guard |
| 9 | `culture-material/craft-artisan-lexicon.md` | `:44` "`| Steel (Japan) | **tamahagane** …`" (material grading); `:54` ladder table header; `:56-63` the seven systems; `:65` design rule; `:76-87` mark typology | the workshop register, the apprentice→journeyman→master ladder, the six mark types | the **map trade's** roles, products, customers, licensing | clear **only with the corrected anchor** (O2) |
| 10 | `culture-material/trade-economy-lexicon.md` | `:121` "**Split-object authentication** … the cut object *is* the contract"; `:92` stock/foil tally row | measures and their standardization, contract and debt vocabulary | the map as a **legal/territorial instrument**; the scale bar's declared unit | clear with guard |
| 11 | `myth-symbol/celestial-symbolism-calendars.md` | `:3` topic: the naked-eye sky as symbolic system and calendar anchor; `grep 'star chart'` → 0 | the sky as symbolic/calendrical register | the **star chart as a produced document** (observation, projection, print) | **no second owner; row missing** (O3) |
| 12 | `myth-symbol/sacred-kingship-mythic-charter.md` | `:3` topic: "how a myth system legitimates a ruler — the eight legitimation channels …" | the **mythic charter** of rule and the royal register | the **legal charter** — the document that legitimates a claim to ground | **no second owner; row missing in the authoritative table** (O3) |
| 13 | `myth-symbol/divination-omen-systems.md` | `:3` topic: "question → technique → closed sign space → licensed reader" | the sign-reading technology and its institutions | **nothing** — a map used for divination is a reading, not map production | non-collision; optional note only |
| 14 | `civilizations/polynesia-navigation.md` | `:60` "Thompson's Hawaiian star compass … **A mental bearing framework, not a chart** showing the canoe's absolute position." | navigation knowledge | the **chart as artifact**, not the navigation method | clear; the entry must not convert navigation into map authorship |
| 15 | `myth-symbol/symbolism-synthesis-method.md` | `:23` "the **five canonical registers: color, animal, number, celestial body, direction**" | the five-register symbolic grammar | a **composition** register — not a symbolic one | clear **only if** the entry keeps the negation (O4) |
| 16 | `synthesis/dialect-faction-map-workflow.md` | `:2` "**Map** dialect features … onto travel networks" | a lect/faction workflow | nothing | false positive on the verb; no row needed |

**File-level result:** 16 candidate registers checked; **0 existing owners**; **0 collisions that require a different landing path**. The landing is an **A** (new file), not an **M**, and overwrites nothing.

### 3.1 The r48 right-sized draft, re-checked (filed while this seat ran)

The r48 draft landed after my first read cut: `reports/round-48/cov/C01-entry.md` (473 file lines; 227-line entry, 215 body lines per its own `:9`) and `reports/round-48/cov/C02-header.md` (263 file lines). I re-ran the one-owner tests against those bytes, not only against r47.

| Finding | r47 state | r48 state (cited) | Verdict |
|---|---|---|---|
| **O1** `cosmology-cosmography.md:27` | gap line cited only `:71,:102` | `C02-header.md:115` quotes `:27` and dispositions it; `C01-entry.md:103` states the split; boundary row `C01-entry.md:107` cites `:27,:71,:102` | **CLOSED** |
| **O2** craft ladder anchor | `:44` called the ladder | boundary row `C01-entry.md:115` cites `:54-65`; `grep 'craft-artisan-lexicon.md:44'` in the draft body → no use (only the B4 audit row at `:351` records the fix) | **CLOSED** |
| **O3** boundary coverage | 8 rows; 4 adjacencies missing | authoritative table `C01-entry.md:107-118` now has **12 rows**, including celestial (`:110`), trade (`:116`), craft (`:115`), sacred-kingship (`:118`) | **table CLOSED; couples OPEN** |
| **O4** register claim | "composition register, not a symbolic register" | draft calls itself "the survey-to-sheet register" (`C01-entry.md:70`) and "this register" (§1, `:91`); `grep -c 'sixth register'` over `reports/round-48/` → 0 outside this file | **SAFE — no symbolic-register slot claimed** |
| **O5** architecture `:101` | row cited `:95` only | boundary row `C01-entry.md:111` still cites `:95` only; `grep 'architecture-settlement-lexicon.md:101'` in the draft → none | **OPEN (small)** |

**Residual O3 — the couples line is incomplete.** `C02-header.md:130` carries **19** backticked `.md` tokens, and all 19 resolve relative to `corpus/knowledge/culture-material/`. The line names neither `celestial-symbolism-calendars.md` nor `sacred-kingship-mythic-charter.md` — both of which the authoritative table dispositions at `C01-entry.md:110,:118`. Two r47 tokens (`writing-systems.md`, `era-material-scoped-reconciliation.md`) are dropped, and correctly so: the r48 body cites neither. **Expected after the fix: 21 tokens (19 + the two table neighbours), not 23**; the r47 "21/21" verified-at claim should become "21/21" against the new list, not "23/23".

This is a **completeness** defect, not a second owner: an adjacency that appears in the table but not in `- couples:` is still dispositioned in prose, so no register is claimed twice. But the table-vs-couples mismatch means the one-owner surface is not self-consistent, and the §5 check must test both.

---

## 4. Findings

Status against the r48 draft (see §3.1): **O1 CLOSED, O2 CLOSED, O3 table closed / couples open, O4 safe, O5 open.** The findings are written below in their r47 form so the evidence chain records what was wrong and what changed; each carries its r48 status.

### O1 (closed in r48) — the gap sentence was contradicted by `cosmology-cosmography.md:27`

The r47 head block says:

> `- gap filled:` "the corpus owns space as cosmology … and **owns no made map**." (`reports/round-47/cov/C04-entry-header.md:115`)

It supports that with `:71` and `:102` (the disclaimers) but **not `:27`**, which defines cosmography as "how the world is **drawn (maps)**". A strict one-owner reader asks why `:27` is not already the owner. The answer is defensible — `:27` owns the **world-picture/cosmogram**, while the **surveyed, projected, reproduced sheet** is a different object — but the entry must *say* it. `reports/round-47/cov/C08-boundary.md:156` noticed `:27` and argued it "owns the *world model's* drawn form"; that argument is not in the entry's own gap line or §1, and R03 B8 independently failed the draft on exactly this (`reports/round-47/review/R03-c-content.md` §5.1 B8).

**Required successor wording** (draft, not canon): in the `- gap filled:` line, §1's "what the corpus already owns" paragraph, and the cosmography boundary row, add one sentence of the form:

> Cosmography owns the world-drawn content — the cosmogram and the world model (`cosmology-cosmography.md:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production.

**Falsification predicate after landing:** `grep -c 'cosmology-cosmography.md:27' <entry>` ≥ 1, and the `- gap filled:` line does not contain an unqualified "owns no made map". If the successor drops the `:27` sentence, the one-owner claim is **false** even though no second file exists.

**r48 status: CLOSED.** `C02-header.md:115` quotes `:27` in the `- gap filled:` line; `C01-entry.md:103` states the split ("Cosmography owns the world-drawn content … this entry owns the surveyed, projected, reproduced sheet as production"); boundary row `C01-entry.md:107` cites `:27,:71,:102`.

### O2 (closed in r48) — the craft anchor was the grading row, not the ladder

The r47 couples line and header source list cite `craft-artisan-lexicon.md:44` for "the workshop register and the material-grading vocabulary" (`C04-entry-header.md:127,:159`). Live `:44` is:

```
| Steel (Japan) | **tamahagane** 玉鋼 "ball/jewel-steel" … |
```

The ladder is `:54` (header), `:56-63` (seven systems), `:65` (design rule). `C02-entry-b.md:421` certifies `:44` as the "workshop ladder table … real" — a false verification, which R03 B4 and C08 P1-2 both caught.

**Why this is an ownership finding, not only an anchor bug:** the mapmaker section (`C02-entry-b.md:246-252`) discusses apprentice → journeyman → master. If it cites `:44`, it claims the ladder while pointing at grading, and the boundary row's promise ("cites the ladder and does not restate it") is unverifiable. Fix: cite `:54-65` for the ladder, keep `:44` only for material grading, and correct the audit row's description. C08's fenced row at `reports/round-47/cov/C08-boundary.md:235` already carries the right wording.

### O3 (table closed in r48; couples open) — the authoritative table omitted four adjacencies the body develops

`C01-entry-a.md:94-103` is declared authoritative (`C08-boundary.md:110`; the live one-owner check is `C02-entry-b.md:462`, in the section opening at `:445` — C08's `:481` citation is stale, because live `:481` is an etymology note). It has 8 rows: cosmography, sacred topography, direction, architecture, writing media, Mesoamerica, transport, naming. The body also develops:

- the **map trade** (`C02-entry-b.md:246-252`) → `craft-artisan-lexicon.md`;
- the **map as legal/territorial instrument** (`C02-entry-b.md:300`) → `trade-economy-lexicon.md` and `sacred-kingship-mythic-charter.md`;
- the **star-chart form** (`C01-entry-a.md:246`) → `celestial-symbolism-calendars.md`.

The body has the boundary text for sacred-kingship at `C02-entry-b.md:300` ("that file owns the **mythic charter** … this section owns the **legal charter**"), and C08 supplies integration-ready rows at `:232-237`. But the r47 authoritative table omitted all four, and the `- couples:` line omitted `celestial-symbolism-calendars` and `sacred-kingship-mythic-charter` (21 tokens in r47). The result is **not a second owner**, but the one-owner claim could not be checked from the authoritative surface alone.

**r48 status:** the authoritative table is **fixed** — `C01-entry.md:107-118` has 12 rows, adding `celestial-symbolism-calendars` (`:110`), `trade-economy-lexicon` (`:116`), `craft-artisan-lexicon` (`:115`) and `sacred-kingship-mythic-charter` (`:118`). The couples line is **not** fixed: see the 19-token audit in §3.1 and the corrected expectation below.

**Couples token audit (r47 draft, historical):** `- couples:` at `C04-entry-header.md:159` carries **21** backticked `.md` tokens; all 21 resolve relative to `corpus/knowledge/culture-material/`:

```
OK  architecture-settlement-lexicon.md       OK  ../myth-symbol/cosmology-cosmography.md
OK  writing-media-surface-economy.md         OK  ../myth-symbol/sacred-topography-pilgrimage.md
OK  transport-mobility-lexicon.md            OK  ../myth-symbol/direction-symbolism.md
OK  timekeeping-instruments.md               OK  ../linguistics/naming-systems.md
OK  material-culture-inference-method.md     OK  ../linguistics/writing-systems.md
OK  craft-artisan-lexicon.md                 OK  ../civilizations/mesoamerica-primary-sources.md
OK  trade-economy-lexicon.md                 OK  ../civilizations/polynesia-navigation.md
OK  vessel-container-lexicon.md              OK  ../civilizations/japan-medieval-sengoku.md
OK  ../verification/calibration-registry.md  OK  ../verification/real-world-inspiration-boundaries.md
OK  ../verification/myth-consistency-gate.md OK  ../synthesis/worldbible-integration-contract.md
OK  ../synthesis/era-material-scoped-reconciliation.md
```

No dangling path. The defect is coverage, not resolution. **Corrected expectation:** the r48 line has **19** tokens, so adding the two table neighbours yields **21/21**, not 23/23. The two r47 tokens the r48 draft drops (`writing-systems.md`, `era-material-scoped-reconciliation.md`) are correctly dropped: `grep 'writing-systems\|era-material-scoped'` over the r48 draft returns nothing, so no uncited neighbour is implied.

### O4 (reworded in r48; safe) — no symbolic-register slot claimed

The r47 draft said "The map is a **composition register**, not a symbolic register" (`C01-entry-a.md:105`), citing the five canonical registers at `myth-symbol/symbolism-synthesis-method.md:23` (live: "color, animal, number, celestial body, direction"). That was safe **only** because of the negation: claiming a sixth register would collide with the partition's method file. The r48 draft drops the phrase entirely and calls the entry "the survey-to-sheet **register**" (`C01-entry.md:70`) and "this register" (`:91`), using "register" in the same craft-knowledge sense as "the place register" elsewhere in the corpus. `grep -rni 'sixth register' reports/round-48/` → 0 hits outside this report. **Verdict: safe.** Predicate for the landed entry: no claim to be a *symbolic* register and no "sixth register" string.

### O5 (small fix) — architecture's design lever is owned at `:101`

The authoritative row cites only `:95`. Live `:101` owns the design lever "(a) give every planner culture an **instrument + founding rite + claim word** (groma/plough/pomerium …)". The r47 body uses that lever at `C02-entry-b.md:81` and audits it at `:411`, but the table row does not cite it. **r48 status: OPEN** — `C01-entry.md:111` still cites `:95` only, and `grep 'architecture-settlement-lexicon.md:101'` over the r48 draft returns nothing. Add `:95,:101` to the architecture row so the boundary names both objects.

### What is *not* a finding

- **Divination is not a collision.** `divination-omen-systems.md:3` owns the licensed reader; the cartography draft contains no divinatory material. C08's optional non-collision note is sufficient; no row is required.
- **The 29-file body footprint is not a second owner.** Every genuine cartographic mention is a by-product or an explicit handoff (`cosmology-cosmography.md:71,:102`; `mesoamerica-primary-sources.md:58`; `architecture-settlement-lexicon.md:95`; `direction-symbolism.md:51`; `polynesia-navigation.md:52-74`; `timekeeping-instruments.md:50`). No body mention carries a `- topic:` or `- couples:` ownership claim.
- **The slug is free and the landing is an A.** No overwrite, no `M` on any existing entry.

---

## 5. Post-landing one-owner predicate (for V01 / A04 / F01)

Run from the lane root after the integrator applies C. Every check has a pass condition; any failure is a one-owner failure, not a style note.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
E=corpus/knowledge/culture-material/cartography-and-mapmaking.md

# 1. the file is an add, not a replace (scope corpus/, because README sits at corpus/README.md)
git status --porcelain -- corpus/ | sort
# PASS: exactly "?? $E" plus " M corpus/README.md"; no other corpus path.

# 2. the register has exactly one filename owner (the new file)
find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
# PASS: 1, and it is $E.

# 3. no existing entry gained a map/survey topic
grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|survey map)' corpus/knowledge/ \
  | grep -v "$E" | wc -l
# PASS: 0.

# 4. no existing entry's couples line claims the register
grep -rniE '^- *couples:.*(cartograph|mapmak|survey map)' corpus/knowledge/ \
  | grep -v "$E" | wc -l
# PASS: 0.

# 5. the cosmography split is stated (O1)
grep -c 'cosmology-cosmography.md:27' "$E"          # PASS: >= 1
grep -c 'owns no made map' "$E"                     # PASS: 0 (or qualified in the same line)

# 6. the craft ladder anchor is corrected (O2)
grep -n 'craft-artisan-lexicon.md:44' "$E"          # PASS: only a material-grading use
grep -nE 'craft-artisan-lexicon.md:(54|56-63|65)' "$E"   # PASS: >= 1 ladder citation

# 7. the composition-register negation survives (O4)
grep -c 'sixth register' "$E"                       # PASS: 0
grep -cE 'survey-to-sheet register|composition register' "$E"   # PASS: >= 1 (craft-knowledge sense)

# 8. every couples token resolves, and every boundary-table neighbour has a token
line=$(grep -m1 '^- couples:' "$E")
echo "$line" | grep -o '`[^`]*\.md`' | tr -d '`' | while read p; do
  [ -f "corpus/knowledge/culture-material/$p" ] || echo "MISS $p"; done
echo "$line" | grep -o '`[^`]*\.md`' | wc -l
# PASS: no MISS, and the count is 21 (the r48 19 + celestial + sacred-kingship).
# Then cross-check the table against the couples line:
for n in cosmology-cosmography sacred-topography-pilgrimage direction-symbolism \
         celestial-symbolism-calendars architecture-settlement-lexicon \
         writing-media-surface-economy transport-mobility-lexicon naming-systems \
         craft-artisan-lexicon trade-economy-lexicon mesoamerica-primary-sources \
         sacred-kingship-mythic-charter; do
  grep -q "$n" <(echo "$line") || echo "NO-COUPLES-TOKEN $n"; done
# PASS: no output.

# 9. no neighbour was rewritten to accommodate the new entry
git status --porcelain -- corpus/knowledge | grep -c '^ M'
# PASS: 0. The new entry is untracked ("??"), so any " M" under corpus/knowledge
# is a neighbour rewrite and fails the check. README's " M" lives outside this scope.
```

**Interpretation rule.** Checks 1–4 and 9 are the ownership test: if they pass, no second owner exists at file or topic level and no neighbour was rewritten. Checks 5–8 are the *claim* test: if 5 or 6 fails, the entry asserts a boundary it does not honor and the one-owner verdict is **fail even though the partition is clean**. This distinction is the round's guard against repeating r47, where the file-level ownership was correct (`C08-boundary.md:12`) but the gap sentence and the ladder citation were not.

---

## 6. Could-not-evaluate and `to-verify`

- **The r48 right-sized draft was absent at my first read cut, then filed during this seat.** My initial check (`find reports/round-48 -type f`) returned only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; I therefore tested the r47 draft first, then re-tested the live r48 bytes (`C01-entry.md`, `C02-header.md`) and recorded the status in §3.1 and §4. **The §5 predicates remain the landing gate** — my r48 read is of seat fragments, not of an assembled, landed entry.
- **The post-landing checks have not been run** (nothing landed). §5 supplies them; V01/A04/F01 own the execution.
- **I did not re-run the freshness gate** (`tools/harness/claims-freshness.py`); O01/O04 own that. My own sweep at `a01405d` reproduces the zero-owner result independently.
- **External shelf ownership is not applicable** — external works own no in-corpus register.
- **Cross-claim interactions:** the README revision (Ca/C10/C11) changes the index, not the corpus partition; it cannot create a second owner. No `to-verify` there.

---

## 7. Write surface

This file only — `reports/round-48/adj/A02-ownership.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.

**Bottom line for the integrator:** the cartography landing is **one-owner-safe at the file level** and should remain the C landing. The r48 draft has already closed the two blocking r47 findings — the `cosmology-cosmography.md:27` split (`C02-header.md:115`, `C01-entry.md:103,:107`) and the craft ladder anchor (`:54-65`, not `:44`) — and its authoritative table now covers 12 neighbours (`C01-entry.md:107-118`). **Two edits remain before the evidence chain is filed:** (1) add `../myth-symbol/celestial-symbolism-calendars.md` and `../myth-symbol/sacred-kingship-mythic-charter.md` to the `- couples:` line (`C02-header.md:130`, 19 → 21 tokens, both paths resolve), which makes the couples line match the table; and (2) add `:101` to the architecture boundary row (`C01-entry.md:111`), since that file owns the instrument+founding-rite+claim-word lever, not only the groma sentence. With those two, every §5 predicate passes and the claim "one owner, no second owner" is true and checkable.
