# X04 — coverage-inflation critique: cartography is a real gap and a real method entry, with five conditions

- Seat: **X04** | role: critic | claim: **C** (coverage) | round 47, loop 2, position 1
- Baseline: `git rev-parse HEAD` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`), equal to `reports/round-47/claims.json:7`
- Out path: `reports/round-47/cross/X04-coverage-critic.md` (this file only)
- Inputs read at HEAD: `claims.json`, `targets.json`; `reports/round-44/scout/K02-gap-scout.md`; `reports/round-44/validation.json`; `reports/round-47/scout/K01-gap-recheck.md`; `scout/K02-seed-extract.md`; `plan/P01-plan.md`; `cov/C01-entry-a.md`; `cov/C02-entry-b.md`; `cov/C03-entry-c.md`; `cov/C04-entry-header.md`; `cov/C05-freshness.md`; `cov/C07-contract-audit.md`; `cov/C10-sweep.md`; the live corpus.
- Writes: this file only. No corpus byte, tool byte, README byte or filed-round byte was written or staged. No `run-validation.py` executed; no commit/push/install/network.
- Canon: NON-CANON critique. This seat decides no world, admits no entry, and certifies no round.

**Verdict in one line:** the cartography gap is **real, unowned, uncollided, and drafted as real method** — C01, C02 and C03 all add decision surfaces the 223 entries do not have, so the `+1` is **not a manufactured topic**. It is not yet a clean `improved`: the boundary table omits the corpus's own definitional claim that cosmography includes drawn maps (`cosmology-cosmography.md:27`); the landed `- gap filled:` line repeats a false `cartograph` line count; the "0 prior-round proposals" wording is literally false at r47 unless the r44 seed is recorded as a named exception; and the assembled drafts total **800 body lines against a partition range of 103–221**, with C02 §5 duplicating C01 §3 on projection, scale, orientation and symbols. The topic is a gain; the assembly as filed is volume-inflated and must be deduplicated before it earns the axis move.

---

## 1. What I measured, not inherited

Commands run from the lane root on 2026-10-19 with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/                 # no corpus modification
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo COLLISION || echo ABSENT
ABSENT
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], ...}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

`LC_ALL=C` sort confirms the proposed slug's slot: `calendar-festival-systems.md` < `cartography-and-mapmaking.md` < `costume-semiotics.md`. The target path is absent, so the landing is an **A** (add), never an **M**. The README section has 25 rows against 25 files (`awk` over `corpus/README.md`).

These reproduce, independently, K01's and C05's premises. I found no collision and no arithmetic drift in the live tree.

---

## 2. Is the gap real? Yes — and the missing method is measurable

### 2.1 Ownership: zero by every test that matters

| Test | Result | Evidence |
|---|---|---|
| filename owner | **0** | only `synthesis/dialect-faction-map-workflow.md` carries `map`, as a verb (`:2`) |
| `- topic:` owner | **0** for the register's vocabulary | `grep -rniE '^- topic:.*(cartograph|mapmaking|map-making|atlas)'` → no owner; the broad 11-hit set is metaphor/verb, dispositioned at `K02-gap-scout.md:122-136` |
| H1/title owner | **0** | two "dialect map" titles, neither cartography (`K01-gap-recheck.md:154-159`) |
| `- couples:` delegation to an unbuilt cartography file | **0** | `grep -rniE '^- couples:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge` → no output |
| target path | **absent** | `test -e` → ABSENT |
| prior landing/draft | **none** | `reports/round-44/validation.json:9`: "the fresh gap (cartography, K02) has no entry body. No corpus delta" |

### 2.2 The demand is thin, and that is stated honestly — but thin demand is not the same as no gap

The broad-vocabulary count is pattern-dependent; all of the following reproduce:

| Pattern | Files | Lines |
|---|---:|---:|
| K02's tight pattern (`cartograph|mapmak|portolan|cadastr|mappae|mappa mundi|surveyor|theodolit|compass rose|graticule|hereford mappa|lienzos?|stick chart|star chart|world map|map of|maps of|drawn map`) | **29** | **35** |
| C04's 20-pattern probe (`cartograph|mapmak|portolan|cadastr|mappa mundi|surveyor|theodolit|compass rose|graticule|world map|drawn map|map of|maps of`) | **28** | **31** |
| Strict word `cartograph` | **2** | **2** |
| `mapmaking`, `portolan`, `graticule`, `theodolite`, `Mercator`, `isobath`, `scale bar`, `map legend` | **0 each** | **0 each** |

The strict `cartograph` lines are `myth-symbol/cosmology-cosmography.md:102` ("not cartographic claims") and `civilizations/mesoamerica-primary-sources.md:58` ("Lienzos and cartographic histories"). **`cosmology-cosmography.md:71` does not contain the word** — it says "not survey maps". This matters because the seed and the header draft count it as a `cartograph` hit (see §4).

### 2.3 The method questions the corpus cannot answer today

The strongest evidence for the gap is not a mention count; it is that five cartographic design questions have **no owner anywhere in the 223**:

1. **Projection and scale.** `Mercator` 0 files, `graticule` 0, `isobath` 0, `scale bar` 0, `map legend` 0. The 21 `projection` hits are all non-cartographic senses (deictic projection, retro-projection, an etic projection); the 18 `triangulat*` hits are method triangulation, not geodetic triangulation.
2. **The map's silences.** `grep -rniE '(map|chart).{0,60}(omit|silenc|blank|not shown)' corpus/knowledge` → no map-context hit.
3. **Map-form typology.** `portolan` 0; `cadastral` only 2 by-product lines (`architecture-settlement-lexicon.md:95`, `japan-medieval-sengoku.md:157`); no entry offers the itinerary/cadastral/chorographic/portolan/cosmographic/thematic/lienzo typology.
4. **The survey-to-sheet chain.** The groma appears in one sentence inside a city-planning entry (`architecture-settlement-lexicon.md:95`); no entry gives the chain, control network, or error budget.
5. **Reproduction as map-specific economics.** `writing-media-surface-economy.md` owns surfaces and the cost ladder, but its `- scope:` explicitly excludes "printing as an industry beyond the §9 calibration note" (`:33`); it has no copperplate/atlas/chart trade class.

Delete the proposed entry and those five questions remain unanswerable. That is the test that separates coverage from padding, and the draft passes it.

---

## 3. The gap's true shape: a disclaimer plus a definitional scope claim — not a delegation

K02 called this a "structurally named but unbuilt register" (`K02-gap-scout.md:179`). That is close, but the precise structure is different from the writing-media precedent, and the difference should change the entry's boundary:

- **Writing-media's precedent was a delegation.** `linguistics/writing-systems.md:7` hands "culture-material/* (clay, papyrus, palm leaf, paper economies)" outward, and the writing-media entry cites that delegation in its `- gap filled:` (`writing-media-surface-economy.md:4`). A dangling handoff existed and the new entry filled it.
- **Cartography has no such delegation.** No `- couples:`, `- gap:`, `- gap filled:` or `- scope:` line names an unbuilt cartography file (measured: 0 hits, §2.1). What exists is:
  - **a definitional scope claim** — `cosmology-cosmography.md:27`: "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." Cosmography says *maps are part of its interface*.
  - **a double disclaimer** — `:71`: "T-O diagrams are symbolic, **not survey maps**"; `:102`: "T-O diagrams are symbolic devices, **not cartographic** claims."

So the corpus does not say "someone should build cartography"; it says *maps belong to the cosmographic interface* and *we do not build the survey-map production chain*. The unowned object is the **chain**, not the word "map".

**Consequence for the draft (the one substantive correction I would require):** the boundary table must dispose `cosmology-cosmography.md:27`, not only `:71`/`:102`. The current tables in `C01-entry-a.md:96` and `C04-entry-header.md:118` name only the disclaimers. A reviewer can legitimately object that the corpus's own frame assigns "how the world is drawn (maps)" to cosmography, so "0 owners" is true of *mapmaking* but not of *maps*. The entry needs one sentence: *cosmography owns the cosmogram — the world drawn as a doctrinal model (:27, :71, :102); this entry owns the surveyed, projected, reproduced sheet that composes it.* Without that row, the one-owner claim is overstated at exactly its strongest competing sentence.

---

## 4. Number audit: what reconciles, what does not

The round is circulating five different demand figures. Four are reproducible; one is not; one attribution is wrong.

| Claim in the wave | Status | Corrected reading |
|---|---|---|
| K02: "tight pattern → 29 files / 35 lines" (`K02-gap-scout.md:148`) | **reproduced exactly** | 29 / 35 with the declared pattern |
| C04: "20-pattern probe → 28 files / 31 lines" (`C04-entry-header.md:76-77`) | **reproduced exactly** | 28 / 31 with the declared pattern; the entry states its pattern, which is the right practice |
| K01/K02: "genuine footprint 7 files / 9 lines" (`K01-gap-recheck.md:23`; `K02-seed-extract.md:236`; `C07-contract-audit.md:165`) | **does not reconcile with its own table** | K02's own §3.4 table lists **7 files / 11 line-refs** (`:151-162`); excluding both cosmology disclaimers gives **6 files / 9 lines**. "7 / 9" matches neither. The qualitative verdict (by-product only) is unaffected; the headline number should not be repeated |
| C04/`- gap filled:`: "`grep -rli 'cartograph'` → 2 files / 3 lines" (`C04-entry-header.md:59`, and the fenced `- gap filled:` at `:115`) | **wrong line count** | strict `grep -rn 'cartograph'` = **2 lines / 2 files** (`cosmology:102`, `mesoamerica:58`). `:71` is a "survey maps" hit, not a `cartograph` hit. `grep -rli` reports files, not lines, so the command as cited cannot produce the stated result. **Fix the landed `- gap filled:` before apply** |
| "11 topic-line hits" (K01/C05/C07) vs "13 broad hits" (C01 `:50-51`) | **both can be true; different patterns** | The entry must state its exact probe in `- gap filled:` so the count is reproducible. C04's `- gap filled:` does state its probes; keep that practice and fix only the strict-word count |

A critic should not manufacture a defect out of pattern choice. The defect is the **unqualified "3 lines"** in the landed gap statement, because a reader who runs the cited command gets a different number and cannot reproduce the sentence. This is the same class as the r43 stale-premise defect, one level down: an evidence sentence that its own command does not produce.

---

## 5. Carried-topic adjudication: confirm C05's reading, record the exception

C05's interpretation note explicitly asks R02/X04 to confirm or reject it (`C05-freshness.md:158`). **I confirm it**, with one wording condition.

The facts:

- K02's own screen defines a candidate as carried if "any prior round's scout/gap/plan registry already named it" (`K02-gap-scout.md:66`).
- At r44, "prior" meant rounds 1–43; cartography had **0 hits** there (`K01-gap-recheck.md:200-206`).
- At r47, r44 K02 is a prior-round scout that names cartography — **1 prior-round naming, 0 prior-round claim proposals, 0 drafts, 0 landings** (`K01-gap-recheck.md:23-26,235`).
- r44's C was blocked on a *different* candidate that had been named at r42 and was drafted anyway; cartography was seed-only and never drafted (`reports/round-44/validation.json:9`).

So the operative distinction is real: **a named seed with no draft is not the same failure as a re-proposed, drafted, previously rejected topic.** C05's reading is correct. But `claims.json:26` says "no prior-round proposal", and the threshold says "confirmed 0 prior-round proposals" (`:34`). At r47 that is literally false unless qualified. The round should use the precise sentence K01 recommends (`K01-gap-recheck.md:239`):

> "No cartography proposal before r44 K02; r44 K02 is the cited seed and was never drafted or landed."

Put it in the entry's `- gap filled:` and in the round record. That converts an unqualified predicate into a named, checkable provenance exception — the same standard r44 was asked to meet for the dream candidate. It does not block the landing.

---

## 6. Manufactured-`+1` test on the filed drafts

All four fragments are now filed: C01 (§1–4), C02 (§5–9), C03 (§10–15) and C04 (the head block). I audit each below. The only remaining `could-not-evaluate` is the assembled bytes themselves and the external shelf, not a missing body draft.

### 6.1 C01 — real method, not a lithic copy

C01's mission was written in r42 lithic language ("the property that makes a map a register", "material/trade classes", "container-name fossil") — see §7. The filed bytes reinterpret those phrases into cartography rather than copying the lithic entry:

- **§2** is a five-condition register test (ground index / bounded notation / structural selection / conventional readability / reproducibility), applied object by object; it is a genuine discrimination procedure, not a definition paragraph (`C01-entry-a.md:109-150`).
- **§3** is six interacting mechanisms — selection, projection, scale, orientation, symbolization, authority — each ending in a design lever (`:152-230`). The projection table (`:169-175`) and the scale-as-survey-ceiling rule (`:182-185`) are exactly the uncovered core identified in §2.3.
- **§4** is the eight-form typology with survey feed, medium, patron, exemplar, and "what it structurally cannot show", plus eight trade classes (`:236-276`). No neighbour has this.

Verdict: **method, not padding.** The one weak spot is §4.2's material classes, which are a compressed restatement risk against writing-media; C01 itself hands the surface economy to `writing-media-surface-economy.md:3` (`:261`), which is the right boundary. C13/C06 should check that no paragraph re-derives the seven surface families.

### 6.2 C03 — real method, and it exercises the chain

C03 is the strongest evidence against the inflation suspicion:

- a nine-step build order, each step with the artifact it must write and the failure if skipped (`C03-entry-c.md:73-105`);
- a two-map NON-CANON worked example (levy sheet vs pilot chart of the same lagoon) that exercises question → chain → projection → orientation → class → blank → reproduction → warrant → update, and produces a dispute decided by dates and warrants, not draughtsmanship (`:107-152`);
- a 14-row calibration bank with R/C/B/H/T statuses and replacement practices (`:154-187`);
- 12 stable decision rows (`DR-CT-01..12`) with rejected alternatives (`:189-208`);
- recheck triggers and a handoff list (`:210-247`).

This is the form QUALITY clause 4 asks for (`corpus/QUALITY.md:16-17`). It is not an essay and not a repackaged neighbour.

### 6.3 C04 — strong header, two defects

Pass: topic byte-equal to the seed (`C04-entry-header.md:218-219`), 23 anchor assertions and 21 couples resolutions (`:230-232`), scope and recheck concrete, Tier B honestly `(to-verify)`.

Defects:
1. **No `cosmology:27`** in the boundary or the gap statement (§3 above).
2. **The `cartograph` line count** in the fenced `- gap filled:` (§4 above).
3. Minor: the header says "the three `cartograph` lines" (`:63`) — same miscitation; fix in both the audit prose and the fenced block.

### 6.4 C02 — real method, and the one material assembly defect

C02 landed after my first cut. It passes the neighbour-restatement test: the groma (`architecture-settlement-lexicon.md:95`), the surface ladder (`writing-media-surface-economy.md:64-78`), the craft marks (`craft-artisan-lexicon.md:76-87`), the vessel fossil (`vessel-container-lexicon.md:71`), and the lienzo rule (`mesoamerica-primary-sources.md:58`) are cited, not re-derived. Its §9 does **not** reuse the lithic *sarcophagus* as the example; it builds a *mappa / charta / atlas / portolan / cartouche* word bank and cites the sarcophagus once, as a method precedent (`C02-entry-b.md:399`). The new material is substantial: the seven-link chain and weakest-link rule (`:42-56`), the control network as political infrastructure (`:77-83`), the field-book/fair-copy reduction (`:85-91`), the four scarcity regimes (`:184-196`), the working-map/monument split (`:207-219`), five trade roles and four products (`:252-293`), the five-link warrant chain (`:327-337`), the **performative map** (`:339-345`), the authority ladder (`:348-357`), the contest rule (`:367-377`), and the etymology bank (`:397-445`).

The defect is not against the neighbours; it is **inside the assembled entry**:

| mechanism | C01 section | C02 section | verdict |
|---|---|---|---|
| projection families | `C01-entry-a.md:169-175` | `C02-entry-b.md:97-104` | same families, same preserves/sacrifices logic — **duplicate** |
| scale (fraction, threshold, false precision, scale bar) | `C01-entry-a.md:180-185` | `C02-entry-b.md:110-116` | **duplicate** |
| orientation (east/south/route/centre/north-up; compass trap) | `C01-entry-a.md:187-196` | `C02-entry-b.md:122` | **duplicate** |
| symbol grammar (point/line/area/text, boundary, blank, legend) | `C01-entry-a.md:198-205` | `C02-entry-b.md:120-131` | **duplicate** |
| capability → form | `C01-entry-a.md:238-247` (question → form) | `C02-entry-b.md:62-69` (capability → form) | complementary axes; cross-reference, do not merge |
| working map vs monument / trade classes | `C01-entry-a.md:265-274` | `C02-entry-b.md:207-219` | overlap; one owner + pointer |

C02's interface note claims "§3 owns what map symbols *mean* … §5 owns how a sheet is *made and combined*" (`C02-entry-b.md:31`). That split does not hold: C01 §3 is itself production — its own heading is "six decisions before a line is drawn" and it runs selection, projection, scale, orientation, symbolization, authority (`C01-entry-a.md:152-213`). Concatenating C01 §3 and C02 §5 as filed gives the reader the same decision surface twice.

**Volume makes this material, not cosmetic.** Measured fenced-body line counts: C01 **199**, C02 **424**, C03 **177** → assembled **800 lines** before the head block. The live culture-material partition is 103–221 lines (median **149**, max **221**, `wc -l corpus/knowledge/culture-material/*.md`). The assembled entry would be **5.4× the median and 3.6× the longest existing entry**. C07 measured the same band and called an out-of-band entry "a review flag, not automatically a fail" (`C07-contract-audit.md:85`); at 3.6× the maximum it is not a flag, it is the dominant property of the entry.

This does not make the topic a manufactured `+1`; it makes the **draft** inflated by assembly. The fix is structural, not editorial:

- Let **C01 §3** own the mechanism tables (selection/projection/scale/orientation/symbolization/authority) and reduce **C02 §5** to the links C01 does not cover: select → measure → control → reduce → reproduce, plus the weakest-link rule and the failure table (§5.1-5.3, §5.7-5.8). C02 §5.4-5.6 become one-line pointers to C01 §3.2-3.5.
- Pick one owner for the working/monument split and the trade-class table (C01 §4.3 or C02 §6.4), and cross-reference the other.
- Target the partition band (≤ ~300 lines assembled). If the integrator wants a longer reference entry, that is a deliberate ruling to record, not a default from concatenation.

If landed undeduplicated, the coverage count is still 224, but the entry is padding by volume — the exact failure this seat exists to catch.

---

## 7. The mission-vs-seed structure mismatch: resolved in substance, not by the planner

K02-seed-extract flagged that the C01–C03 missions describe the r42 lithic skeleton, not the cartography seed (`K02-seed-extract.md:220-231`). I verified it independently:

- `targets.json:21` (C01): "the property that makes a map a register … material/trade classes".
- `targets.json:22` (C02): "scarcity/prestige … provenance/charter … the container-name fossil".
- `targets.json:23` (C03): "sections 10-15".
- The exact phrases come from the lithic draft: `reports/round-42/cov/C01-entry-1.md:53` ("the property that makes stone a register … the container-name fossil") and `:138` (the *sarcophagus* mechanism).

All three drafters adapted the phrases to cartography in substance: C01 turned "register property" into a five-condition test; C02 turned "container-name fossil" into the *mappa/charta* word bank; C03 wrote the seed's §10–15 rather than a 15-section lithic skeleton. **The mission mismatch did not produce filler.** The planner did not resolve it — `P01-plan.md:149` requires the seed spine while the missions it hands out still use the lithic split — so the integrator should audit the assembly against `K02-gap-scout.md:234-247` and the dedup table in §6.4, not against `targets.json:21-23`.

---

## 8. README arithmetic and the prose-vector defect

Measured:

- live: `## culture-material/ (25)` at `corpus/README.md:234`; 25 rows (`:240-241` are calendar then costume); `Total knowledge entries: 223.` at `:544`; footer vector `25/26/25/29/24/94` at `:548` = 223.
- post-landing: culture-material 26; total 224; vector `25/26/26/29/24/94` = 224.
- rev-2.4 defect at `:11`: `25/23/25/29/24/94 → 25/23/26/25/24/94` = **217**. This is worse than a sum slip: three slots are wrong against the live footer — myth-symbol 23 (live 26), culture-material 26 (live 25), synthesis 25 (live 29). C10's diagnosis is correct (`C10-sweep.md:149-154`), and its control D proves the sweep does **not** read revision vectors (`:128`), so "sweep green 224==224" alone cannot satisfy the claim's vector threshold.
- **C05 has a typo in two places**: it says the post-landing vector is `26/26/25/29/24/94` (`C05-freshness.md:275,295`). The correct order is `25/26/26/29/24/94` (linguistics, myth-symbol, culture-material, synthesis, verification, civilizations). C10 and C04 have it right. Fix before the record propagates it.
- The repair should be a **forward correction**: keep the rev-2.4 block as the dated record and add the corrected pair plus a correction sentence in the rev-2.5 block (P01's wording at `P01-plan.md:161` is the right shape). Do not delete history to make the arithmetic green.

---

## 9. Coverage verdict and the conditions I would attach

**Axis judgment candidate: `improved`, conditional.** The gap is real, the landing is an add, no existing entry is overwritten, and every filed body fragment is method. The count is 223 → 224 and the arithmetic is sound. But coverage should not be scored by `rows == files` alone; C07 itself notes the sweep has no duplicate-topic test (`C07-contract-audit.md:194`). The axis is improved only if all five conditions hold:

1. **Boundary condition.** The assembled entry disposes `cosmology-cosmography.md:27` in the boundary table (and cites `:71`/`:102` as the disclaimer). Without it, the entry creates a second *claim* on "how the world is drawn (maps)" even while owning a different object.
2. **Evidence condition.** The landed `- gap filled:` says `cartograph` = **2 lines / 2 files**, not 3; states its broad probe verbatim; and drops the unreconciled `7 files / 9 lines` figure or recomputes it from its own table.
3. **Provenance condition.** The round records the r44-seed exception in the precise form in §5; no unqualified "0 prior-round proposals".
4. **Neighbour condition.** C02 passes it (§6.4): no restatement of the groma, surface ladder, or lithic sarcophagus; the boundary table cites the neighbours by line. C01 §4.2 and C02 §5.7 must remain pointers to writing-media, not second surface inventories.
5. **Assembly condition.** Deduplicate C01 §3 against C02 §5 (§6.4 table) and land near the partition band. At 800 lines as filed, the entry is volume-inflated even though its topic is real. If it lands undeduplicated, coverage is `unchanged` on quality grounds — the count moved, the corpus did not gain a proportionate method.

**Harm check:** no topic duplicate, no overwrite, no second *file* owner. The only second-owner risk is the `:27` scope claim, which condition 1 answers. Failing that, the harm is a boundary defect, not a count defect — the round should not call it a coverage gain and a one-owner violation in the same breath.

**What would have made this a manufactured `+1`:** a draft that re-explained the six neighbours, a "history of cartography" with no decision surface, or a moved README count with no new method. None of the filed bytes is that. The risk has moved from *topic* to *assembly*: the choice is a real entry compressed to the partition's scale, or a real entry landed at 3.6× the partition's maximum. The first is a coverage gain; the second is a gain padded into a liability.

---

## 10. Owed / limits

- **All three body drafts were read** (C01, C02, C03) plus the header (C04). The only remaining `could-not-evaluate` items are the assembled-entry semantic audits (C06/C08/C13), the external shelf (C06/C12), and V01's post-landing check — none of which this seat owns.
- **The 800-line measurement is of the fenced drafts as filed**, not of the assembled file; it excludes the head block and any assembler edits. It is a lower bound on the assembled length.
- **External shelf not audited here.** Tier B is C06/C12's seat; this critique checks only that the drafts mark it `(to-verify)` and do not present it as inspected.
- **Landing-time freshness** is C05/V01's seat; my ownership sweep is pinned to `6e9a30d` and must be re-run at the apply HEAD.
- **No filing defects were introduced.** This seat wrote only this path; `git status --porcelain` shows no change under `corpus/` or `tools/` from this seat.
