# K01 — cartography, right-sized: the spec the r47 over-build should have been

- Seat `K01` | role scout | claim **C** (coverage) | round 48, loop 2
- Baseline: HEAD `a01405d` (`git rev-parse --short HEAD`, 2026-10-19); `reports/round-48/claims.json` baseline `a01405d`
- Out path: `reports/round-48/scout/K01-rightsized-spec.md` (this file). No other byte written.
- Mission: re-confirm the gap at HEAD, extract the r44 seed + the r47 draft's load-bearing content, close every R03 B1–B9 defect with its verified fix, and specify a **right-sized entry** (≤250 lines; budget 230) that C01 can draft without re-inheriting the over-build.

**Verdict in one line.** The gap is fresh at `a01405d` (223 total, culture-material 25, zero filename and topic owners); the r47 draft is 790 assembled fenced lines (51 header + 739 body, measured), 4.96× the partition median; the right-sized successor is a **10-section, 230-line** entry (27 header + 203 body, 1.04× the live max 221) that keeps the register method and cuts the fossil bank, the standalone decision-record section, and the duplicated mechanism prose.

---

## 1. Freshness re-confirmed at HEAD `a01405d` (not carried)

All commands run from the lane root 2026-10-19 with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| Probe | Command | Result |
|---|---|---|
| corpus total | `find corpus/knowledge -name '*.md' \| wc -l` | **223** |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | **25** |
| filename owners | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` | **0** |
| slug free | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | No such file |
| topic-line owners | `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr\|atlas\|survey map\|world map\|graticule\|theodolite)' corpus/knowledge/ \| wc -l` | **0** |
| `cartograph` token | `grep -rni 'cartograph' corpus/knowledge/` | **2 files / 2 lines**: `myth-symbol/cosmology-cosmography.md:102`, `civilizations/mesoamerica-primary-sources.md:58` |
| `mapmaking` | `grep -rli 'mapmaking' corpus/knowledge/ \| wc -l` | **0** |
| `portolan` | `grep -rli 'portolan' corpus/knowledge/ \| wc -l` | **0** |
| `graticule` | `grep -rli 'graticule' corpus/knowledge/ \| wc -l` | **0** |
| `theodolite` | `grep -rli 'theodolit' corpus/knowledge/ \| wc -l` | **0** |
| `cadastr` | `grep -rli 'cadastr' corpus/knowledge/` | **2 files**: `culture-material/architecture-settlement-lexicon.md`, `civilizations/japan-medieval-sengoku.md` (periodization caution) |
| broad demand | `grep -rliE 'cartograph\|mapmak\|portolan\|cadastr\|mappa mundi\|surveyor\|theodolit\|compass rose\|graticule\|world map\|drawn map\|map of\|maps of' corpus/knowledge/ \| wc -l` | **28 files / 31 lines** (`grep -rni \| wc -l` → 31) |

The two `cartograph` lines are the partition's own disclaimer and a source-class row, not an owner:

- `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102` — "T-O diagrams are symbolic devices, not cartographic claims"
- `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58` — "Lienzos and cartographic histories … the copy chain is the evidence"

**Not carried.** The only prior proposal is `reports/round-44/scout/K02-gap-scout.md` (its §3.6 checked every registry); rounds 45–46 add none. The freshness gate at declaration returned **C FRESH** (`reports/round-48/claims.json:23`), and this seat's independent probes reproduce that.

**Hierarchy note for the `- gap filled:` line.** `cosmology-cosmography.md:71` still reads "T-O diagrams are symbolic, not survey maps" and `:102` "not cartographic claims"; both contain no `cartograph` token, so they are cited as the **disclaimer**, not counted as hits. This is the B2 fix (§4.1).

---

## 2. What r47 measured, and why it is over-built

Measured this seat by extracting the longest fenced block from each r47 fragment (r47's own assembly convention):

| Block | Lines |
|---|---:|
| `reports/round-47/cov/C04-entry-header.md` (head block) | 51 |
| `reports/round-47/cov/C01-entry-a.md` (§1–§4) | 201 |
| `reports/round-47/cov/C02-entry-b.md` (§5–§9) | 361 |
| `reports/round-47/cov/C03-entry-c.md` (§10–§15) | 177 |
| **Assembled total** | **790** |
| Body only (790 − 51) | **739** |

Both figures in the round are therefore correct once scoped: `claims.json`'s "790-line" is the head+body assembly; R03's 739 is the body. The section split (sum 790, re-derived):

| r47 § | lines | r47 § | lines |
|---|---:|---|---:|
| head | 51 | 8 provenance | 69 |
| 1 frame | 23 | 9 fossil | 55 |
| 2 register test | 45 | 10 build order | 34 |
| 3 mechanisms | 80 | 11 example | 47 |
| 4 forms/trade | 53 | 12 calibration | 35 |
| 5 chain | 108 | 13 decision record | 21 |
| 6 scarcity | 69 | 14 recheck | 21 |
| 7 mapmaker | 60 | 15 scope | 19 |

**Partition discipline** (`wc -l corpus/knowledge/culture-material/*.md | sort -n`): min 103, median **149** (13th of 25), max **221** (`funerary-material-culture.md`), mean 150.2 (3,756 / 25).

- r47 body / median = 739 / 149 = **4.96×**; assembled / max = 790 / 221 = **3.57×**
- Right-sized target 230 / median = **1.54×**; 230 / 221 = **1.04×**; cut = 790 − 230 = **560 lines (−70.9%)**

The over-build is not one bad section; it is 15 sections where 10 carry the method and 5 repeat or embellish it.

---

## 3. The right-sized budget — 230 lines, 10 body sections

Header block **27** + body **203** = **230** (ceiling 250; target band 225–240). Each row names what it absorbs and what it cuts.

| New § | Lines | Absorbs (r47) | Keep | Cut / why |
|---|---:|---|---|---|
| head | 27 | head 51 | H1; `topic` (byte-equal seed); `gap filled` (fresh counts); `sources` (18 in-corpus anchor files + grouped external shelf); `source`; `couples` (21 paths, grouped by partition); `verified-at`; `recheck`; `scope` | 24 lines of field-by-field rationale, 9 sha-pinned digests, 18 single-line external bullets → shelf grouped to 5 lines, all `(to-verify)` |
| 1 ownership | 26 | §1 (23) | master claim; four load-bearing choices; **13-row boundary table** (12 neighbours + divination non-collision) | duplicate ownership prose; add the `cosmology :27` sentence (B8) and four missing neighbours (P2-7) |
| 2 register test | 18 | §2 (45) | five conditions; object table (8 rows); "partial = fail" rule | 27 lines of per-object commentary |
| 3 survey chain | 22 | §5 (108) | 7 links + artifact + failure; weakest-link rule; error budget | 86 lines of instrument history and worked sub-cases |
| 4 projection/scale/symbol | 22 | §3 (80) | projection table (5 rows preserves/distorts); corrected scale paragraph (B1); orientation + compass trap; symbol table (5 rows) | 58 lines of mechanism prose and the duplicate bullets R03 P2-3 flags (`C01:164` vs `C02:109`; `C01:204` vs `C02:110`) |
| 5 form typology | 20 | §4 (53) | **all 8 forms** with question / minimum build / institution / cannot-show (B9) | 33 lines of trade-class prose (moved to §6); "5 of 8" table replaced |
| 6 cost and trade | 20 | §6 (69) + §7 (60) | 4 scarcity regimes; cost stack (4 rows); working-vs-monument; 3 trade rules | 109 lines: six roles, six organisation models, four products, three customers condensed to one 4-row table + rules |
| 7 provenance/legal | 20 | §8 (69) + §13 (21) | warrant chain (5 rows); 4 provenance failures; contest rule; map≠territory reconciliation (P2-1); 4 `DR-CT` rows | 49 lines of authority-ladder prose; no standalone decision-record section |
| 8 build + example | 33 | §10 (34) + §11 (47) | 9 build steps (1 line each, artifact named); one lagoon / two sheets / one storm; **one update rule stated once** (B7) | 48 lines: step rationale, six consequence paragraphs → 4 bullets |
| 9 calibration | 14 | §12 (35) | 8-row bank with R/C/B/H/T codes | 21 lines of row prose |
| 10 recheck/scope | 8 | §14 (21) + §15 (19) | 4 recheck triggers; scope + handoff | 32 lines duplicated in the header's `recheck`/`scope` fields |
| **total** | **203** | 739 | | **cut 536 body + 24 header = 560** |

**Cut whole sections**

1. **§9 container-name fossil (55 lines).** Highest `(to-verify)` density (one section-level mark for 13 OED-level etymologies, R03 P2-6) and lowest decision yield. Retain at most one inline clause in §2 if the register test needs the word *mappa*; otherwise drop. If the integrator wants it back it is a separate entry, not this one.
2. **§13 standalone decision record (21 lines).** Fold the four load-bearing `DR-CT` rows into §7's table; a separate 12-row record is duplication.
3. **Mechanism restatement in §10 (r47).** The build order must **sequence** projection/scale/orientation/symbol, not re-describe them; §4 owns the descriptions.

---

## 4. Section spec, with the defect fixes written out

### 4.1 Head block (27 lines) — exact corrections

Field order must match the measured culture-material convention (`topic, gap filled, sources, source, couples, verified-at, recheck, scope`; cf. `corpus/knowledge/culture-material/timekeeping-instruments.md:3-10`, `bathing-and-body-hygiene.md:3-10`). No `- calibration:` field; the bank lives in §9.

**`- topic:`** — byte-equal to `reports/round-44/scout/K02-gap-scout.md:227` and to the r47 header (`reports/round-47/cov/C04-entry-header.md:114`); verified identical this seat at 775 characters. C10's README row description must be this text after `- topic: ` with no reflow (sweep compares them: `reports/round-28/readme/sweep.py` `topic_of` / `parse_readme`, `ROW_RE` / `TOPIC_RE` at `:60-61`, `:74-95`).

**`- gap filled:`** — fresh sweep at `a01405d`, in this form:

> the corpus owns space as cosmology, space as sacred route, space as orientation code and space as built plan — and owns no made map. The partition's own disclaimer is the charter: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` distinguishes the T-O diagram from "survey maps" and `:102` says T-O diagrams are "not cartographic"; `:27` defines cosmography as "how the world is drawn (maps), named … walked … and built", which is the **world-drawn content**, not the surveyed sheet this entry owns. `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5` owns the place register and `:69` the three route types; `corpus/knowledge/myth-symbol/direction-symbolism.md:51` owns the orientation register; `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` owns the castrum grid and names the groma. Fresh absence sweep 2026-10-19 at lane HEAD `a01405d` over `corpus/knowledge/` (223 files; culture-material 25): filename probe → **0**; slug probe → **No such file**; topic-owner probe → **0**; `grep -rli 'cartograph'` → **2 files**, `grep -rni 'cartograph'` → **2 lines** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`); `mapmaking` / `portolan` / `graticule` / `theodolite` → **0 files each**; `cadastr` → **2 files** (both by-product); broad 13-pattern demand probe → **28 files / 31 lines**, every genuine hit a by-product. Not carried: the only prior proposal is `reports/round-44/scout/K02-gap-scout.md`; rounds 45–46 add none.

This closes **B2** (2 files / 2 lines, `:71` not counted) and **B8** (`:27` sentence).

**`- sources:`** — the in-corpus anchors (18 files / 28 line citations — ledger in §9), then an external shelf grouped to **5 bullets**, every edition/volume/page `(to-verify)`, opening with "not consulted this round (no network at seat time); no unread work is presented as inspected":

1. Harley & Woodward (eds.), *The History of Cartography*; Harley 1989; Wood 1992; Monmonier 1991 — the map-as-claim and map-power frame.
2. Ptolemy, *Geography* (Berggren & Jones 2000); Snyder 1987; Campbell 1987 — projection and the portolan tradition.
3. Kain & Baigent 1992; Buisseret 1992; Jacob 2006; Pickles 2004 — the cadastral/state and theoretical-map strand.
4. Mundy 1996; Boone 2000; Edson 2007 — indigenous and medieval map genres.
5. Dilke 1971; al-Idrisi 1154; *Tabula Peutingeriana* / *Antonine Itinerary*; Ortelius 1570 — survey instruments and the itinerary/atlas forms.

**`- couples:`** — **21 paths**, all verified to exist at `a01405d` and all resolved relative to `corpus/knowledge/culture-material/`: `myth-symbol/{cosmology-cosmography, sacred-topography-pilgrimage, direction-symbolism, celestial-symbolism-calendars, sacred-kingship-mythic-charter, divination-omen-systems}` (6), `culture-material/{architecture-settlement-lexicon, writing-media-surface-economy, transport-mobility-lexicon, craft-artisan-lexicon, trade-economy-lexicon, timekeeping-instruments, material-culture-inference-method}` (7), `civilizations/{mesoamerica-primary-sources, polynesia-navigation, japan-medieval-sengoku}` (3), `linguistics/{naming-systems, writing-systems}` (2), `verification/{calibration-registry, real-world-inspiration-boundaries, myth-consistency-gate}` (3) — 6+7+3+2+3 = 21. Each must name what the neighbour owns and what this entry owns instead; §9 anchors the load-bearing ones.

**`- verified-at:`** — baseline and counts, and the r47 **P2-2** fix: if digests are pinned, say **nine**, not six. Prefer no digests at all in a right-sized header (saves 9 lines); the anchor ledger is the check.

### 4.2 §1 — What this entry owns (26 lines)

- Master claim, stated once: **a map is an argument about space, not a picture of it; its authority comes from the survey chain behind it and its politics from what it omits.**
- Four load-bearing choices in one row each: what is **measured** (survey precision), what is **preserved** (projection/scale), what is **drawn** (selection/symbolization), who may **copy and read** it (reproduction/access).
- 13-row boundary table (§5 below), one line per neighbour: `| neighbour | owns (cite) | this entry owns |`.
- The B8 sentence, verbatim as in §4.1.

### 4.3 §2 — The five-condition register test (18 lines)

Stipulative definition used here: **ground index, bounded notation, structural selection, conventional readability, reproducibility/citability**. Partial satisfaction is a **fail**, and the failure must name what the object is instead. 8-row object table: field book, painting, T-O diagram, itinerary, portolan, cadastral, star chart, stick chart — verdict + "is instead" column. Rule: ranking objects on a "primitive → scientific" ladder is a category error; **test before typing** (r47 §12's anti-colonial calibration becomes one clause here, not a repetition).

Softening required (**P2-5**): the Marshallese stick chart is "not a **positional** map under this entry's stipulative test", not "not a map".

### 4.4 §3 — The survey-to-symbol chain (22 lines)

7-link table, one row each: **select → measure → control → reduce → project → symbolize → reproduce**, with the artifact each link writes and its characteristic failure. Weakest-link rule stated once: *the sheet cannot exceed the weakest link, and the error budget is additive along the chain, not averaged*. Control network = political infrastructure (one sentence, cite `architecture-settlement-lexicon.md:95` for the groma). Field book vs fair copy = one row, not a subsection.

### 4.5 §4 — Projection, scale, orientation, symbol (22 lines)

- Projection table, 5 rows (equirectangular, Mercator, polar azimuthal, local plane, stereographic): preserves / distorts.
- Scale paragraph with the **B1** correction, verbatim:

> At 1:50,000, one millimetre on the sheet is 50 m on the ground; a line drawn at 0.2 mm therefore claims 10 m of ground (0.2 mm × 50,000 = 10,000 mm = 10 m). If the survey closed at 200 m, the drawing asserts **twenty times** the available precision (200 m ÷ 10 m = 20).

- Orientation: convention + the compass trap, citing `direction-symbolism.md:51`; do not restate the direction register.
- Symbol table, 5 rows: legend, boundary line, blank, colour, cartouche — each with "what it can hide".
- Rule stated once: the scale bar, not the representative fraction, survives copying (the FR is a claim; the bar is a measurement).

### 4.6 §5 — Form typology, 8 of 8 (20 lines)

One table, **eight rows**: itinerary/strip, cadastral, chorographic, portolan, celestial/star chart, cosmographic, thematic, cartographic history/lienzo. Columns: **question it answers | minimum credible build | institution it forces | what it structurally cannot show**. This closes **B9** (r47 shipped 5 rows under a "per form" title). Rule: form follows the question, not the era.

### 4.7 §6 — Cost, scarcity and the map trade (20 lines)

Four scarcity regimes (survey labour, control network, drafting skill, reproduction), a 4-row cost stack, working-map vs monument-map, three prestige currencies. Three rules: a copy travels only as far as its warrant; the atlas is a commercial form, not a cartographic one; "state monopoly" is a reproduction claim, not a survey claim. One 4-row role table (surveyor, draughtsman, engraver, publisher) replaces r47's six roles + six organisation models.

### 4.8 §7 — Provenance and the legal instrument (20 lines)

Warrant chain, 5 rows: **warrant → record → attestation → authentication → use**. Four provenance failures. Contest rule: **two accurate maps can contradict each other without either being false; the dispute is decided by dates and warrants, not draughtsmanship.** Map-is-territory reconciliation (**P2-1**), using r47 C02's own formulation:

> a category error as metaphysics, but a performative fact in a registered system; keep the two apart.

Four `DR-CT` rows, e.g. state the interval and trigger on every sheet; name the warrant before the draughtsman; decide the blank before the legend; price the copy before the survey.

### 4.9 §8 — Build order + NON-CANON example (33 lines)

Nine steps, one line each, each naming the artifact it writes: question and reader → survey precision and error budget → control network → projection and scale → orientation → symbol set and legend → medium and reproduction → the silences → the warrant. **Sequence, do not re-describe.**

Worked example: one lagoon, two sheets (a levy cadastral sheet and a pilot chart), one storm. **B7 fix — one update rule, stated once:**

> **A sheet is authoritative for one stated interval and is superseded only at its stated trigger; an event inside the interval is annotated, not redrawn.**

Apply it three times, consistently:

| | Map A — levy sheet | Map B — pilot chart | Joint survey |
|---|---|---|---|
| interval | one levy year | one sounding season | one season |
| trigger | levy-year resurvey | a new guild master | every dike breach |
| storm | annotated, not redrawn | sounding boat corrects the master | forces the new trigger |

The dispute is decided by **which interval was current and which mark authorised the copy**, not by draughtsmanship. The joint survey changes its *stated trigger* to breach — that is the single rule applied, not a second rule. Consequences: 4 bullets (form follows question; two accurate maps can conflict; the blank is a decision; the warrant, not the drawing, decides). Declared **NON-CANON** and invented in the first line of the section.

### 4.10 §9 — Calibration bank (14 lines)

8 rows, codes from `verification/calibration-registry.md:33-39` (R/C/B/H/T verified live):

| Claim | Code | Why |
|---|---|---|
| "a map is neutral/objective" | R | selection, projection, orientation, omission are constitutive |
| "medieval people believed the earth was flat; T-O proves it" | R | sphericity standard; `cosmology-cosmography.md:102`; Russell 1991 |
| "portolan charts are photographically accurate" | C | practical sailing charts with their own distortions |
| "indigenous maps are childlike / merely mental" | R | lienzos are legal-territorial documents (`mesoamerica-primary-sources.md:58`) |
| "the map is the territory" | H (as metaphysics R) | performative fact in a registered system only |
| "cartography diffused one-way from Europe" | C | independent/parallel traditions |
| "the map caused the state" | B | confounded with the fiscal/legal institution that commissioned it |
| "a surviving map was an important map" | B | survivorship bias: `material-culture-inference-method.md:69` |

### 4.11 §10 — Recheck, limits, scope (8 lines)

Four recheck triggers keyed to `file:line` (cosmography `:71`/`:102`, direction `:51`, architecture `:95`, mesoamerica `:58`, perishability `:69`); three limits (no external page was inspected; no accuracy/price/print-run figure is asserted; a living tradition's restricted map routes through `real-world-inspiration-boundaries.md:6` and `myth-consistency-gate.md:34`); scope + handoff in two lines, no canon.

---

## 5. Boundary table — 13 rows, every citation verified live

| Neighbour | Owns (verified at `a01405d`) | This entry owns |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | five-axis world model; T-O symbolic diagram (`:27` "how the world is drawn (maps)"; `:71` "symbolic, not survey maps"; `:102` "not cartographic claims") | the surveyed, projected, reproduced sheet as production |
| `myth-symbol/sacred-topography-pilgrimage.md` | place register (`:5`); three route types (`:69`) | how a route is surveyed and drawn |
| `myth-symbol/direction-symbolism.md` | orientation register; compass trap (`:51`) | map convention: orientation choice, rose, north arrow |
| `myth-symbol/celestial-symbolism-calendars.md` | planet-as-god, constellations, calendar anchoring (`:3`, `:27`) | star chart as a **form**; astral content stays there |
| `myth-symbol/sacred-kingship-mythic-charter.md` | legitimation channels, incl. "regalia as found title-deed" (`:70`) | documentary warrant; the map's charter is not a mythic charter |
| `myth-symbol/divination-omen-systems.md` | sign-reading technology (`:3`) | **not a collision** — no divinatory content; one note makes the negative check visible |
| `culture-material/architecture-settlement-lexicon.md` | built plan; castrum grid + groma (`:95`) | land survey as a map-production step |
| `culture-material/writing-media-surface-economy.md` | seven surface families (`:3`); office/merchant copy class (`:73`) | map-specific media and reproduction |
| `culture-material/transport-mobility-lexicon.md` | route institution (`:28` "a route is only real if someone maintains it"); `DR-TR-02` (`:117`) | the representation of a route |
| `culture-material/craft-artisan-lexicon.md` | workshop ladder (`:54-65`); material grading (`:44`) | mapmaker trade as a craft case |
| `culture-material/trade-economy-lexicon.md` | tally stock/foil (`:92`); split-object authentication (`:121`) | the map as a legal instrument at that boundary |
| `civilizations/mesoamerica-primary-sources.md` | lienzo/cartographic-history source class (`:58`) | cites the genre; does not restate the inventory |
| `linguistics/naming-systems.md` | onomastics/toponymy (`:40`); "a map is an archive of coups" (`:70`) | the toponym layer of the sheet |

Neighbour count: 12 real neighbours + 1 non-collision note = 13 rows. This is K02's 7, plus naming-systems (r47 had it), plus the four R03 §3.3 found missing (**P2-7**), plus divination.

---

## 6. B1–B9 closure checklist

| ID | r47 location (verified) | How this spec closes it | Proof |
|---|---|---|---|
| B1 | `reports/round-47/cov/C02-entry-b.md:98` — "asserts ten times" | §4.5 corrected sentence ("twenty times"); 200 m ÷ 10 m = 20 | arithmetic §7 |
| B2 | `reports/round-47/cov/C04-entry-header.md:115` — "2 files / 3 lines" | §4.1 gap text: 2 files / 2 lines; `:71` cited as disclaimer, not a hit | `grep -rni` → 2 |
| B3 | `reports/round-47/cov/C02-entry-b.md:36` — false accusation against C01's quote | keep `naming-systems.md:70` verbatim ("archive of coups"); reject r47 C02's "renamings" correction | live `:70` |
| B4 | `reports/round-47/cov/C02-entry-b.md:248` and audit row `:421` — ladder cited as `:44` | ladder = `craft-artisan-lexicon.md:54-65`; `:44` only material grading | live `:44`, `:54`, `:65` |
| B5 | `reports/round-47/cov/C03-entry-c.md:79` "§1–3"; `:184` "§2" | new numbering: typology is **§5**, chain **§3**, mechanisms **§4**; every internal ref uses the assembled numbers | §3 budget |
| B6 | `reports/round-47/cov/C01-entry-a.md:298` "Provenance/charter (§9)" | provenance is **§7** in the new layout; handoff note must say §7 | §3 budget |
| B7 | `reports/round-47/cov/C03-entry-c.md:123`, `:137`, `:150` — three incompatible update rules | §4.9 single rule + interval/trigger table | this spec |
| B8 | `reports/round-47/cov/C01-entry-a.md:90,:96`; `C04:115` omit `:27` | §4.1 and §5 row 1 add the `:27` sentence | live `:27` |
| B9 | `reports/round-47/cov/C03-entry-c.md:95-103` — 5 of 8 forms | §4.6 table has **8 rows** | §4.6 |

Also carried in: **P2-1** (map≠territory wording), **P2-2** ("nine" not "six"), **P2-3** (duplicate bullets dropped by the §4 budget), **P2-5** (stick chart softened), **P2-7** (four rows added). **P2-4** (bank consolidation) is moot: the bank is now 8 curated rows, described as principal readings rather than "full". **P2-6** (per-row etymology marks) is moot: the r47 §9 fossil bank is cut.

---

## 7. Arithmetic ledger — every number recomputed

| Claim | Recomputation | Verdict |
|---|---|---|
| 0.2 mm at 1:50,000 = 10 m | 0.2 × 50,000 = 10,000 mm = 10 m | correct |
| 200 m coarser than 10 m by 20× | 200 / 10 = 20 | correct (r47 said ten) |
| 1 mm at 1:50,000 = 50 m | 1 × 50,000 = 50,000 mm = 50 m | correct |
| 1 mm at 1:1,000,000 = 1 km | 1,000,000 mm = 1,000 m | correct |
| r47 assembled 790 | 51 + 201 + 361 + 177 = 790; header 51 + body 739 | correct |
| r47 body 739 | 790 − 51 | correct |
| partition median 149 | 25 sorted values, 13th = 149 | correct |
| r47 / median 4.96× | 739 / 149 = 4.9597 | correct |
| r47 / max 3.57× | 790 / 221 = 3.575 | correct |
| target 230 | 27 header + 203 body; section sum 26+18+22+22+20+20+20+33+14+8 = 203 | correct |
| target / max 1.04× | 230 / 221 = 1.0407 | correct |
| cut 560 | 790 − 230 | correct |
| rev-2.4 written vector sums 217 | 25+23+26+25+24+94 = 217 | defect confirmed |
| rev-2.4 pre-landing vector | 25+23+25+29+24+94 = 220 | correct |
| live vector 223 | 25+26+25+29+24+94 = 223 | correct |
| post-landing vector 224 | 25+26+26+29+24+94 = 224 | correct |
| partition mean 150.2 | 3,756 / 25 = 150.24 | correct |

---

## 8. Landing arithmetic and README rev 2.5 (the C half C10 must draft)

Live anchors (HEAD `a01405d`, verified by `grep -n`):

| Anchor | Live text | After landing |
|---|---|---|
| `corpus/README.md:234` | `## culture-material/ (25)` | `## culture-material/ (26)` |
| `corpus/README.md:240-241` | calendar row, then costume row | new row **between** them (sort: `calendar-` < `cartography-` < `costume-`) |
| `corpus/README.md:544` | `Total knowledge entries: 223.` | `... 224.` |
| `corpus/README.md:548` | `(total 223 files; directory totals 25/26/25/29/24/94).` | `(total 224 files; directory totals 25/26/26/29/24/94).` |
| `corpus/README.md:11` | "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**" (sums 217) | repair to `25/26/25/29/24/94` (sums 223) |
| `corpus/README.md:5` | revision 2.4 block begins | new revision 2.5 block inserted above; the 2.4 block occupies `:5-:13` = 9 lines, so every anchor below shifts by the length of the new block |

Rev-2.5 block must state: one culture-material entry landed (`cartography-and-mapmaking.md`); `## culture-material/` 25 → **26**; totals 223 → **224**; vector `25/26/25/29/24/94` → **25/26/26/29/24/94**; re-measured `python3 reports/round-28/readme/sweep.py`: 224 rows vs 224 files, exit 0.

**Sweep expectation after apply:** parts `{civilizations:94, culture-material:26, linguistics:25, myth-symbol:26, synthesis:29, verification:24}`, `rows 224 files 224`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `totals_line 224`, footer dir totals `[25,26,26,29,24,94]`, exit 0.

**Two-file delta only:** the new entry (A) + this README revision (M). No other `corpus/**` byte.

---

## 9. Citation ledger — every in-corpus anchor used above, re-read live

| `path:line` | Verified content (short) |
|---|---|
| `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` | "how the world is drawn (maps), named (toponyms), walked … and built" |
| `…/cosmology-cosmography.md:71` | "T-O diagrams are symbolic, not survey maps" |
| `…/cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, not cartographic claims" |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | topic line: place register; contains "sacred-geography mapping … as a diagram" |
| `…/sacred-topography-pilgrimage.md:69` | "The three route types" |
| `myth-symbol/direction-symbolism.md:51` | "The compass trap … true or magnetic … declination" |
| `myth-symbol/celestial-symbolism-calendars.md:3` | topic: planet-as-god, constellations, calendar anchoring |
| `…/celestial-symbolism-calendars.md:27` | shared-sky convergence is not evidence of contact |
| `myth-symbol/sacred-kingship-mythic-charter.md:70` | row 8: "the regalia as found title-deed" |
| `myth-symbol/divination-omen-systems.md:3` | topic: question → technique → closed sign space → licensed reader |
| `culture-material/architecture-settlement-lexicon.md:95` | "surveyed with the groma … The grid is cadastral" |
| `culture-material/writing-media-surface-economy.md:3` | topic: the seven surface families |
| `…/writing-media-surface-economy.md:73` | papyrus/paper/cloth — "the office and the merchant" |
| `culture-material/transport-mobility-lexicon.md:28` | "a route is only real if someone maintains it" |
| `…/transport-mobility-lexicon.md:117` | `DR-TR-02` maintenance clause |
| `culture-material/craft-artisan-lexicon.md:44` | Steel (Japan) material-grading row |
| `…/craft-artisan-lexicon.md:54` | table header: System / Apprentice / Journeyman / Master |
| `…/craft-artisan-lexicon.md:65` | design rule (pick a rung, break it deliberately) |
| `culture-material/trade-economy-lexicon.md:92` | Exchequer tally stock/foil |
| `…/trade-economy-lexicon.md:121` | split-object authentication |
| `culture-material/material-culture-inference-method.md:69` | perishability: what survives to be seen |
| `culture-material/timekeeping-instruments.md:50` | "longitude at sea" |
| `civilizations/mesoamerica-primary-sources.md:58` | lienzos / cartographic histories; copy chain is the evidence |
| `linguistics/naming-systems.md:40` | onomastics: anthroponymy/toponymy/theonymy |
| `linguistics/naming-systems.md:70` | "Every renaming is datable; a map is an archive of coups." |
| `verification/calibration-registry.md:33-39` | codes R / C / B / H / T |
| `verification/real-world-inspiration-boundaries.md:6` | recheck trigger for restricted material |
| `verification/myth-consistency-gate.md:34` | do not expose restricted ritual knowledge |

Every path above resolved at `a01405d`; every quoted fragment was read from the live line, not from a report.

---

## 10. What this spec does not do / handoff

- **It is a spec, not the entry.** C01 drafts the 230-line body against §3–§4; C03 recomputes §7's ledger against the drafted bytes; C04 re-resolves §9's ledger against the draft; C05 counts lines and checks the contract; C06 re-runs freshness at landing HEAD; C11 stages the 224 tree and runs the sweep.
- **No staged tree, no sweep run this seat.** The landing arithmetic in §8 is predicted from live anchors, not delivered; the post-apply sweep is the only delivery certificate (`D01`, `C11`).
- **No external source inspected.** The shelf is book-level with every edition/page `(to-verify)`; no accuracy, price, print-run or survival figure is offered.
- **Not re-audited:** the r47 fragments' P2 items beyond those listed, and every r47 citation other than the nine defect sites and the in-corpus anchors in §9. Those remain R03's findings; this seat confirms the defect lines it cites (`C02:36`, `:98`, `:248`, `:421`; `C03:79`, `:95`, `:123`, `:137`, `:150`, `:184`; `C01:298`; `C04:115`).
- **One residual risk.** The 230-line budget is tight for an entry with a 13-row boundary table and an 8-row form table; if C01 overruns, cut §9's bank to 6 rows and §8's consequences to 3 bullets before adding lines to §4–§7. Do not restore the fossil bank or the standalone decision record.

**Write surface:** this file only — `reports/round-48/scout/K01-rightsized-spec.md`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `corpus/lessons/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged; no commit, install, network, or in-tree `run-validation.py`. `git status --porcelain` at write cut showed only the pre-existing `?? reports/round-46/review/` and `?? reports/round-48/`.
