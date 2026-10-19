# C06 — claim-C scribe: two-candidate reconciliation and integration-ready assembly

- Seat: `C06` | role scribe | claim **C** (coverage) | round 44
- Baseline: `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (`git rev-parse HEAD`; declared at `reports/round-44/claims.json:7`)
- Observation time: 2026-10-19T17:28:32Z. Working tree: `git status --porcelain` → `?? reports/round-44/` only; `git status --porcelain corpus/` → 0 lines.
- Out path: `reports/round-44/cov/C06-scribe.md` (the only write by this seat).
- This is a **complete rewrite** of this seat's 17:25Z cut, which predated K02, C01 and C05. Fragments landed mid-write and changed the claim's state materially; the earlier cut's "K02 absent / C01 absent / C05 absent" status is superseded here. No corpus byte was staged; no filed byte was edited.

**Assembly status at this cut:** K02, K04, C01 and C05 have landed. **C02 (README), C03 (source audit) and C04 (contract audit) are still absent** (`reports/round-44/cov/` contains C01, C05, C06 only). The claim-C landing is therefore **not complete** and **no bytes have moved**. The central finding is a **two-candidate conflict** that only the integrator can resolve.

---

## 0. Verdict (read this first)

**Two independently verified, genuinely unowned gaps were named; claim C is `+1` only; the round has not chosen between them.**

| | Candidate A | Candidate B |
|---|---|---|
| scout | **K02** (`scout/K02-gap-scout.md:8`) | **K04** (`scout/K04-gap-verify.md:10`) |
| topic | cartography / mapmaking | dream / vision / trance altered-state complex |
| proposed path | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `corpus/knowledge/myth-symbol/dream-vision-trance.md` |
| partition delta | culture-material 25 → 26 | myth-symbol 26 → 27 |
| total | 223 → 224 | 223 → 224 |
| topic-owner test | 11 topic-line hits, all metaphor/verb/handoff; **0 owners** (`K02-gap-scout.md:116-136`) | 2 adjacent hits (divination technique row; Mongol lexical base); **0 owners of the state** (`K04-gap-verify.md:77-103`) |
| filename | free in all six partitions | free in all six partitions |
| sort position | between `calendar-festival-systems.md` and `costume-semiotics.md` (`corpus/README.md:240-241`) | between `divination-omen-systems.md` and `eschatology-world-end-systems.md` (`corpus/README.md:215-216`) |
| demand | low: 29 files/35 lines broad; 7 files/9 genuine cartographic mentions (`K02-gap-scout.md:138-179`) | high: 52/223 on K04's five-family union; 61 with singular `vision` (`K04-gap-verify.md:118-132`; §2.5 below) |
| prior-round status | **not named in any of the five registries** (measured, §2.4) | **named r42 K02 R2**; never landed, re-measured absent (`K04-gap-verify.md:161-166`) |
| draft | **absent** — C01 drafted the other candidate | **complete**: `cov/C01-entry-draft.md`, 483 lines, 70,992 B, 9 head fields |
| collision clearance | **absent** — C05 cleared the other candidate | **present, target-specific**: `cov/C05-collision.md:10,250-255` |
| audits | C02/C03/C04 absent | C02/C03/C04 absent |

The conflict is explicit in the filed fragments themselves:

- K02's candidate screen classifies **dream / vision / trance** as **"carried — reject"** because r42's K02 named it (`scout/K02-gap-scout.md:78`), and selects cartography as "not named in any registry" (`:85`).
- K04 argues the opposite: the r42 proposal was never landed, the file is absent at `c9f4eaa`, and the r44 sweep is a fresh measurement, so the gap is "fresh, not a prior-round carry" (`scout/K04-gap-verify.md:161-166`).
- C01's draft follows K04 and says so: if K02 lands a different gap, "this draft is a **spare**, not the claim's landing; the integrator must choose one gap, not land both" (`cov/C01-entry-draft.md:9`).
- C05's clearance is explicitly **for the dream/trance target only**: "clears *the only target on disk*, not whatever C01 eventually drafts"; if K02 names a different gap, "claim C is `+1` only and only one candidate may land" (`cov/C05-collision.md:17,195,250-255`).

K02 has now landed a different gap. C01's own reconciliation clause is therefore triggered: **the dream/trance draft is a spare unless the integrator rules otherwise.**

**Coverage remains 223. No verdict of `improved` is available at this cut.**

| condition | verdict candidate |
|---|---|
| one candidate lands, C02/C03/C04 pass, one `A` entry + README rev 2.5, sweep 224==224, no overwrite, and the chosen gap satisfies the claim's "not carried" clause | **improved** |
| the draft(s) exist but the selection/landing is withheld or incomplete | **unprovable-but-better** |
| both candidates land (total 225, +2), a duplicate topic lands, or an existing entry is overwritten | **harmed** |
| no candidate lands | **unchanged** (claim C fails as declared) |

**Recommendation (not a decision).** The integrator must rule on the meaning of **"not carried from a prior round"** (`reports/round-44/claims.json:39`) before any bytes move.

- **Default for threshold safety: Candidate A (cartography).** K02's filed screen is the only filed screen that directly rejects the candidate on the "not carried" clause. Cartography is novel in the registries (§2.4). The cost is that C01's ready draft cannot be used; a cartography draft, C05 re-run, and C02/C03/C04 are owed.
- **Candidate B (dream/trance) is defensible only with an explicit, filed overrule** of K02's "carried" classification, with the rationale: the r42 R2 proposal was never landed; the r44 sweep re-measured absence at 223; the claim's remedy is a fresh sweep, not novelty. The draft is complete and C05 has cleared the exact path. Without that recorded overrule, a reviewer can mark the claim's "not carried" threshold failed by citing `K02-gap-scout.md:78`.
- **Do not land both.** Claim C is `+1` (`claims.json:36-47`); landing both makes the tree 225 and violates the declared delta and the non-goal "the single C landing only" (`claims.json:67`).

This seat does not choose, draft, or overrule a scout. It reports the measured state and the consequences.

---

## 1. Measured baseline at scribe time

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```
$ git rev-parse HEAD
c9f4eaa707b6e977ff6e1616463e91f4b8afea5d
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for d in corpus/knowledge/*/; do printf '%-18s %s\n' "$(basename $d)" "$(ls "$d"*.md | wc -l)"; done
civilizations      94
culture-material   25
linguistics        25
myth-symbol        26
synthesis          29
verification       24
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
EXIT=0
$ python3 -B reports/round-28/readme/sweep.py --selftest
selftest: 12/12 checks passed
EXIT=0
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
$ find corpus/knowledge -name '*.md' -print0 | sort -z | xargs -0 sha256sum | sha256sum
45bed989dd61978099193c0718325dc68479b65ba4820a4a9a79c44d0d4b2fee  -
$ git ls-files 'corpus/knowledge/**/*.md' | wc -l
223
```

The claim-C `before` — "total 223" (`claims.json:40`) — is measured true. K02 (`scout/K02-gap-scout.md:16-53`), K04 (`scout/K04-gap-verify.md:14-41`) and C05 (`cov/C05-collision.md:21-91`) report the same baseline and the same README digest; the four measurements agree.

---

## 2. Candidate A — cartography / mapmaking (K02)

### 2.1 The proposal

K02's result line names **cartography / mapmaking** and recommends `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (`scout/K02-gap-scout.md:8`). The master claim: the corpus owns space as cosmology, sacred route and orientation code, but not **the made map** — the survey → projection → drawing → reproduction chain and the map's use as a claim (`:91-95`).

### 2.2 Ownership tests, independently reproduced

```
$ find corpus/knowledge -type f \( -iname '*cartograph*' -o -iname '*mapmaking*' \
    -o -iname '*portolan*' -o -iname '*cadastr*' \) | sort
(no output)
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md; echo $?
1
```

The topic-line test returns **11 hits, all non-owners** (`scout/K02-gap-scout.md:119-136`); this seat reproduced the query and the dispositions:

| entry:line | hit | disposition |
|---|---|---|
| `linguistics/sound-symbolism.md:3` | "the three-way **map**" | metaphor |
| `linguistics/dialect-register-consistency.md:3` | "a built **dialect map**" | metaphor |
| `linguistics/sacred-registers-liturgical-language.md:3` | "ritual events **map** to" | verb |
| `myth-symbol/number-symbolism.md:3` | "a variance **survey**" | statistical sense |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "a **boundary map**" | metaphor |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "sacred-geography **mapping** … as a diagram" | nearest neighbour: the place register/route, not map production |
| `culture-material/ritual-garments.md:3` | "the b.Arakhin 16a **atonement map**" | metaphor |
| `synthesis/dialect-faction-map-workflow.md:2` | "**Map** dialect features" | verb |
| `civilizations/finnic-sami.md:3` | "an **identity map**" | metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | "a reference **map**" | metaphor |
| `civilizations/africa-primary-sources.md:2` | "a bounded **source map**" | metaphor |

**No entry names mapmaking as its subject.**

The load-bearing structural evidence is the partition's own disclaimer:

```
corpus/knowledge/myth-symbol/cosmology-cosmography.md:71
  | Medieval Christian: T-O | … Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic,
    not survey maps (§10) | Isidore, Etymologiae 14 |
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102
  - Calibration: … T-O diagrams are symbolic devices, not cartographic claims. …
```

Cosmography owns the world model and explicitly disclaims the **survey map**; the gap is the made object the disclaimer leaves unowned (`K02-gap-scout.md:155-156,179`).

### 2.3 Slug and sort checks

The slug is free in all six partitions (§2.2). In `culture-material` the ASCII sort places it between `calendar-festival-systems.md` (position 5) and `costume-semiotics.md` (position 6) (`K02-gap-scout.md:219`; reproduced with `ls corpus/knowledge/culture-material/ | nl -ba`). In the README the insertion point is between the calendar row (`corpus/README.md:240`) and the costume row (`:241`).

### 2.4 Prior-round non-carriage

K02 checked `reports/round-19/gaps.md`, `reports/round-35/scout/K01-coverage-census.md`, `reports/round-39/scout/K01-verification-gaps.md`, `reports/round-40/scout/K03-gaps.md` and `reports/round-42/scout/K02-myth-gaps.md` and found no cartography row (`K02-gap-scout.md:196-207`). This seat reproduced the registry grep:

```
$ grep -nE 'cartograph|mapmaking|portolan|cadastr|mappa' \
    reports/round-19/gaps.md reports/round-35/scout/K01-coverage-census.md \
    reports/round-39/scout/K01-verification-gaps.md reports/round-40/scout/K03-gaps.md \
    reports/round-42/scout/K02-myth-gaps.md
(no output)
```

The global report grep is noisy — 75 hits, dominated by `reports/supplement-opencode-1/scratch/**` copies of `mesoamerica-primary-sources.md` and the r42 inherited-bibliography line — but none is a gap proposal. K02's narrower count (7 hits) is consistent with that reading.

### 2.5 Demand — low, and stated

K02's tight vocabulary sweep: **29 files / 35 lines** broad; **7 files / 9 lines** genuine cartographic footprint, several of them disclaimers (`K02-gap-scout.md:138-179`). This is a **named-but-unbuilt register**, not a high-demand omission — the same structural shape as the r42 lithic gap. The claim sets no demand threshold; the weakness is admitted by the scout, not hidden.

### 2.6 README arithmetic and shape test

```
culture-material 25 → 26; total 223 → 224
section order: linguistics 25, myth-symbol 26, culture-material 26, synthesis 29, verification 24, civilizations 94
footer vector: 25/26/26/29/24/94  (sum 224)
row insertion: between corpus/README.md:240 (calendar) and :241 (costume)
total line: corpus/README.md:544 223 → 224
```

Scratch simulation with a stub at the proposed path, the real `sweep()` called via `root_override`:

```
parts {'civilizations': 94, 'culture-material': 26, 'linguistics': 25,
       'myth-symbol': 26, 'synthesis': 29, 'verification': 24}
rows 224 files 224
missing [] ghosts [] mismatch [] drift {}
totals 224 True footer [] True ok True
scratch_removed True
```

Mechanics are green. The row text was a stub; the real row must be the eventual entry's `- topic:` text byte-equal.

---

## 3. Candidate B — dream / vision / trance (K04 + C01 + C05)

### 3.1 The proposal and its ownership tests

K04 names the **dream / vision / trance altered-state complex** at `corpus/knowledge/myth-symbol/dream-vision-trance.md` (`scout/K04-gap-verify.md:10`). This seat reproduced the tests:

| term | topic-owner hits | reading |
|---|---|---|
| `dream` | `myth-symbol/divination-omen-systems.md` | one of fourteen technique rows ("dream-oracles and incubation", `divination-omen-systems.md:3,89`) |
| `incubat` | same file | the incubation technique, not the state |
| `trance` | **0** | unowned |
| `ecsta` | **0** | unowned |
| `vision quest` | **0** | unowned |
| `visionary` | **0** | unowned |
| `shaman` | `civilizations/mongol.md` | "shamanic vocabulary" in a civilization base (`mongol.md:3`) |

Heading test: two adjacent hits — `divination-omen-systems.md:1` (dreams as a reading technology) and `civilizations/australia-aboriginal.md:36` (ancestral **Dreaming/Tjukurpa**, explicitly "not a claim that the tradition concerns ordinary sleep dreams", `:37-38`). No entry owns the state, its induction, the visionary career, or the licensing institution (`K04-gap-verify.md:105-116`).

### 3.2 C01's draft

C01 landed a complete fenced draft at the K04 path (`cov/C01-entry-draft.md`). The draft was revised in place during the round; the current measured cut is:

- **483 lines, 70,992 bytes** (`wc -lc`); the fence opens at `:108` (a four-backtick `markdown` fence) and closes at `:395`; body `:109-394`; lines `:396-483` are a post-fence self-audit.
- Nine head fields: `- gap filled:` `:111`, `- topic:` `:113`, `- sources:` `:115`, `- calibration:` `:121`, `- couples:` `:123`, `- source:` `:125`, `- verified-at:` `:127`, `- recheck:` `:129`, `- scope:` `:131`.
- The `- topic:` line is one physical line of **1,291 characters** (`awk 'NR==113{print length($0)}'` → 1291); the README row must copy it byte-equal, unwrapped.
- The draft's own absence sweep reproduces the ownership tests (`C01-entry-draft.md:14-60`); its demand union is 61, with K04's 52 noted as a narrower regex (`:56-60`).
- X01 independently extracted a 284-line cut of the same draft (`cross/X01-trades.md:487-493`) and measured **14 distinct couples tokens**, all `direct`; the post-C census for this path is `2730+14=2744` if the couples field is unchanged. Re-measure after C01's final cut.
- C01's reconciliation clause is explicit: if K02 lands a different gap, this draft is a spare (`:9`).

This seat spot-checked seven load-bearing in-repo anchors in the draft — `divination-omen-systems.md:52,89,126,147`, `ritual-liminality.md:111`, `animal-symbolism.md:53`, `music-instrument-lexicon.md:96` — all resolve and match the draft's use. That is a spot-check, **not** C03's full source audit; C03 is absent.

### 3.3 C05's clearance

C05 cleared the exact path/topic on eight checks (`cov/C05-collision.md:119-130`): exact path absent; no filename collision; no topic-line owner (two hits adjudicated adjacent); no heading owner (two hits adjudicated); naming convention; near-duplicate similarity max 0.609; sort position 11; partition arithmetic 26→27. A dry run shows the landing delta is exactly two paths: the new file (`A`) and `corpus/README.md` (`M`) (`:148-180`).

**Scope limit:** the clearance is "conditional on claim C drafting that exact topic and slug" (`:10`) and does not cover any other target (`:17,250-255`). C01 did draft that exact path, so the clearance applies to the draft's path; but C05 must still re-run its §7 contract against the draft's exact `- topic:` text before bytes move (`:201-241`), because C05's cut predates C01.

### 3.4 Demand arithmetic

K04 reports 52/223; this seat reproduces the per-family counts and resolves the union:

```
dream  25   shaman 28   vision 14   ecsta 5   trance 4   incubat 2
union dream|shaman|ecsta|trance|incubat        52
+ vision quest                                 52 (subset)
+ visionary                                    52 (subset)
+ visions                                      55 (3 additional files)
+ singular "vision"                            61 (6 further files)
```

**52 is the five-family union**, not the full six-family union; K04's own table lists the vision family at 14 but the union row at 52. The ownership verdict does not depend on the union. C01 uses 61 and marks the difference as regex scope (`C01-entry-draft.md:56-60`). Quote the term set with the number.

### 3.5 README arithmetic and shape test

```
myth-symbol 26 → 27; total 223 → 224
section order: linguistics 25, myth-symbol 27, culture-material 25, synthesis 29, verification 24, civilizations 94
footer vector: 25/27/25/29/24/94  (sum 224)
row insertion: between corpus/README.md:215 (divination) and :216 (eschatology)
total line: corpus/README.md:544 223 → 224
```

Scratch simulation with a stub at the proposed path:

```
parts {'civilizations': 94, 'culture-material': 25, 'linguistics': 25,
       'myth-symbol': 27, 'synthesis': 29, 'verification': 24}
rows 224 files 224
missing [] ghosts [] mismatch [] drift {}
totals 224 True footer [] True ok True
scratch_removed True
```

Mechanics are green; the real row text is C01's 1,291-character `- topic:` line.

---

## 4. The conflict and the decision the integrator owes

### 4.1 The filed contradiction

| fragment | statement |
|---|---|
| `scout/K02-gap-scout.md:78` | Dream/vision/trance: "named r42 R2" → **"carried — reject"** |
| `scout/K04-gap-verify.md:161-166` | The r42 proposal was not landed; the file is absent at `c9f4eaa`; the r44 sweep is re-run at 223 → **fresh, not a prior-round carry** |
| `cov/C01-entry-draft.md:9` | If K02 lands a different gap, this draft is a **spare**; the integrator must choose one |
| `cov/C05-collision.md:17,195,250-255` | The clearance covers the dream/trance target only; if K02 names a different gap, only one candidate may land |

**Independent corroboration.** X01's second read names this "the largest live coordination trade in claim C": two scouts, two gaps, a draft serving the second, and no seat owning the choice (`cross/X01-trades.md:437-481`). It reaches the same do-not-land-both conclusion and notes that dream/trance is a "soft adjacency" (one topic-line hit) rather than a zero-owner gap like cartography.

### 4.2 The textual question

Claim C says: "a genuinely unowned gap ... **verified by a fresh absence sweep at the 223 total, not carried from a prior round**" (`claims.json:39`). Two readings:

1. **Strict novelty (K02).** The gap must not have been named in any prior registry. Dream/trance was named r42 R2, so it is carried; cartography is the only eligible candidate.
2. **Fresh re-measurement (K04/C01).** "Not carried" means the `before` must be re-measured at baseline, not assumed from a prior round. Dream/trance was proposed but never landed; the r44 sweep re-measures it absent at 223, so it is eligible. The r43 defect was a stale premise, not a lack of novelty.

The claim's own `before` supports the second emphasis — "the r43 lithic claim was blocked because its topic was already owned — the correct coverage move is a fresh, verified-unowned gap" (`claims.json:40`) — but the phrase "not carried from a prior round" is broad enough for the first. **Only the integrator can rule.**

### 4.3 Decision table

| option | what it means | what is already ready | what remains | threshold fit |
|---|---|---|---|---|
| **A. Land cartography (K02)** | the novel gap; the dream/trance draft becomes a named spare | K02's sweep/shelf/boundary/outline; the README arithmetic and shape test (§2.6) | a C01 cartography draft (the current C01 draft is the wrong topic), C05 re-run, C02, C03, C04 | strongest on "not carried"; low demand is admitted but not disqualifying |
| **B. Land dream/trance (K04/C01)** | the fresh-measured gap; K02's "carried" screen must be explicitly overruled | K04's sweep; C01's complete draft; C05's target-specific clearance; the README arithmetic and shape test (§3.5) | an explicit filed overrule of `K02-gap-scout.md:78`; C05 re-run against C01's exact topic; C02, C03, C04 | strongest on "freshly measured unowned"; the "not carried" conjunct is contestable without the overrule |
| **C. Land neither** | claim C fails as declared | the two scouts' evidence | none | `unchanged`; coverage stays 223 |
| **D. Land both** | forbidden | — | — | total 225, `+2`, violates `claims.json:36-47` and the non-goal "the single C landing only" (`:67`) |

### 4.4 Recommendation

**Rule explicitly, then execute one option.** For threshold safety, **Option A** is the default: K02's filed screen is the only direct test of the "not carried" clause, and it rejects dream/trance. If the round chooses **Option B**, the overrule must be a filed sentence with the rationale (r42 R2 was proposed, never landed; the r44 sweep re-measured absence at 223; the claim's remedy is a fresh sweep, not novelty), and every citation of K02's screen in the round record must mark it **overruled**, not omit it. Do not let the ready draft silently outrank a filed scout screen. Do not land both.

---

## 5. Evidence-chain assembly map (current status)

| leg | seat | artifact | status at 17:28Z | what remains |
|---|---|---|---|---|
| Gap scout 1 | K02 | `scout/K02-gap-scout.md` | **landed** | names cartography; sweep/shelf/boundary/outline; 410 lines |
| Gap scout 2 | K04 | `scout/K04-gap-verify.md` | **landed** | names dream/trance; sweep/shelf/boundary; 259 lines |
| Entry draft | C01 | `cov/C01-entry-draft.md` | **landed** | dream/trance draft only; a cartography draft is absent |
| README rev 2.5 | C02 | `cov/C02-readme-draft.md` | **absent** | exact diff for the chosen target; arithmetic; rev-2.4 defect note |
| Source audit | C03 | `cov/C03-audit.md` | **absent** | every in-repo path resolves; every line real; external `(to-verify)`; zero fabrication |
| Contract audit | C04 | `cov/C04-contract-audit.md` | **absent** | QUALITY 5/5; naming; gap unowned; boundary accepted |
| Collision verify | C05 | `cov/C05-collision.md` | **landed** | dream/trance path only; re-run required for any other target or the exact C01 topic |
| C scribe | C06 | this file | **landed** | two-candidate reconciliation; README arithmetic for both; acceptance checklist |
| Integration draft | S01 | `scribe/S01-integration-draft.md` | **landed (earlier cut)** | §3.2b covers K04 (`:372-390`); its §3.2 says K02 absent (`:367-368`), which is now false; its precondition 2 (`:402`) assumed one gap |
| Honesty ledger | X02 | `cross/X02-honesty.md` | **landed (earlier cut)** | C-5 "no scout" (`:59-72`) is superseded by K02/K04; C-6/C-7 remain unmeasured |
| Scope / delta | A01 | `adj/A01-scope.md` | **landed** | exact-delta gate §7.1 (`:205-230`); one new entry + README only |
| Connector | X00 | `cross/X00-connector.md` | **landed** | O-census at 223 before C (`:96-116`); integration sequence (`:287-305`) |

**Reconciliation rule.** Measurement wins over assertion, and the latest filed fragment wins over an earlier cut of the same artifact. S01's and X02's "K02 absent" rows are the worked example: true at their timestamps, superseded by K02 at 17:24Z. Do not cite them as current. If two fragments report the same measurement with different numbers, quote both with their term set and HEAD; do not average.

---

## 6. Entry contract and README mechanics for either target

### 6.1 `corpus/QUALITY.md`

| clause | requirement | citation |
|---|---|---|
| Q1 provenance | every factual claim cited/checkable; unverifiable marked `(to-verify)`; no invented sources | `corpus/QUALITY.md:5-8` |
| Q2 calibration | every framework names mainstream / contested / discredited with the reason; pop-mythography flagged | `:9-12` |
| Q3 coupling | `- couples:` names the systems/files connected; an entry that couples nothing is reference, not craft | `:13-15` |
| Q4 usability | decision tables, typology tables, checklists, worked examples; no essays | `:16-17` |
| Q5 canon hygiene | no entry decides what is true in any world; entries end at the handoff | `:18-20` |

### 6.2 Header fields, measured across 223 entries

```
topic 223/223   sources 223/223   couples 223/223   recheck 223/223   verified-at 223/223
source 155      gap filled 30     calibration 18    scope 13          gap 8
```

The recent eight-field order is `gap filled, topic, sources, couples, source, verified-at, recheck, scope` (e.g. `mineral-stone-symbolism.md:3,5,7,11,13,15,17,19`; `timekeeping-instruments.md:3-10`). C01's draft adds `- calibration:` (`C01-entry-draft.md:121`) for nine fields, which satisfies Q2 directly. A `- calibration:` line is optional if an explicit in-body calibration section names the status; silence fails Q2.

### 6.3 README anchors and the two arithmetic paths

```
corpus/README.md:5        revision: 2.4 block begins
corpus/README.md:205      ## myth-symbol/ (26)
corpus/README.md:215      - `divination-omen-systems.md` — …
corpus/README.md:216      - `eschatology-world-end-systems.md` — …
corpus/README.md:234      ## culture-material/ (25)
corpus/README.md:240      - `calendar-festival-systems.md` — …
corpus/README.md:241      - `costume-semiotics.md` — …
corpus/README.md:544      Total knowledge entries: 223.
corpus/README.md:546-548  Counts checked … / command / (total 223 files; directory totals 25/26/25/29/24/94).
```

| target | section header | row insertion | post total | post footer vector |
|---|---|---|---|---|
| cartography (A) | `:234` `(25)` → `(26)` | between `:240` and `:241` | 224 | `25/26/26/29/24/94` (sum 224) |
| dream/trance (B) | `:205` `(26)` → `(27)` | between `:215` and `:216` | 224 | `25/27/25/29/24/94` (sum 224) |

Required edits for either path: prepend a `revision: 2.5 — Round-44 …` block above `:5`; increment the target section header; insert the row in filename order with text **byte-equal to the entry's `- topic:` text, continuations space-joined** (`reports/round-28/readme/sweep.py:74-84,139-147`); change the total line; change the footer vector. C02 owes the exact diff; no README draft exists at this cut.

### 6.4 Two carried README defects

- **Rev 2.4 prose vector is wrong.** `corpus/README.md:10-11` records `25/23/25/29/24/94 → 25/23/26/25/24/94`; the second vector sums **217**, not 223. The live footer at `:548` is `25/26/25/29/24/94` (sum 223). The sweep reads the footer, not revision prose (`sweep.py:164-189`), so the defect passes green. C02 must compute the rev 2.5 vector; repairing the 2.4 sentence is optional and, if done, only as part of the touched block.
- **Duplicated H1.** `corpus/README.md:1` and `:3` both read `# kotodama-shokunin corpus index` — the carried `R36-README-DUPLICATE-HEADING` defect. The r39/r42 precedent is **do not repair it in a coverage delta** (`S01-integration-draft.md:424-448`). Leave it carried.

### 6.5 Shape tests (mechanics only)

Both candidate paths were simulated in `.scratch` with a stub entry, the five README edits applied in memory, and the real `sweep()` called via `root_override`; both returned `rows 224 files 224`, `totals 224 True`, `footer [] True`, `ok True`, and both scratch trees were removed. They prove the arithmetic, not the delivery: the row text was a stub in each, and the real post-apply digest must come from the integrator's tree.

---

## 7. Acceptance checklist for the chosen path

Common to A and B (S01's seven preconditions, `S01-integration-draft.md:394-422`; A01's delta gate, `adj/A01-scope.md:205-230`):

1. **One candidate only.** The integrator rules A or B before any bytes move; the losing candidate is a named spare, not a second landing.
2. **Fresh sweep at 223.** Both candidates have one (K02 §3; K04 §4; reproduced in §2-§3). The chosen gap's topic-owner test must return 0 owners, with every hit adjudicated adjacent.
3. **Filename collision.** The chosen slug is absent in all six partitions; no near-duplicate; naming convention `^[a-z0-9]+(-[a-z0-9]+)*\.md$`.
4. **Draft contract.** One fenced entry, one path, the head fields + calibration, in-corpus anchors resolvable, external items `(to-verify)`, no canon claim, handoff target named.
5. **Pre-landing audits.** C03 source audit, C04 contract audit, C05 collision verify — against the **chosen** draft. A post-apply audit does not satisfy the claim.
6. **Apply as `A`, not `M`.** After application, `git status --porcelain corpus/` shows exactly the new entry plus `corpus/README.md`; any tracked entry showing `M` stops the landing and is restored from HEAD (the r42 overwrite incident, `reports/round-42/validation.json:22`).
7. **Post-apply sweep.** `rows 224 files 224`, `footer_ok True`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, exit 0. A predicted reading is not evidence.
8. **Post-apply ownership re-check.** The sweep has **no duplicate-topic leg** (`reports/round-43/review/R01-review.md:394` R01-43-8; `reports/round-43/cov/C07-scribe.md:161-163`). Re-run the topic-owner test over 224.
9. **O-census ordering.** O's four-class identity is only provable at 223 (`entries=223 ∧ refs=2730 ∧ 2556+166+0+7 ∧ glob=1`). Run/file the census **before** C lands, or measure from a pristine `git archive c9f4eaa` plus the eight lane-root targets; post-C is `entries=224 ∧ refs=2730+N ∧ conservation=true` (`cross/X00-connector.md:96-116,287-305`). For the dream/trance draft X01 measured `N=14` (`cross/X01-trades.md:487-497`), so the expected post-C reading is `refs=2744`; re-measure after C01's final cut. Cartography's `N` is unknown until drafted.
10. **Ca-freshness ordering.** Run the r44 freshness check before C lands; after C, C's own `before` ("total 223") is false by construction (`cross/X00-connector.md:227-232`).

Option-specific:

- **A (cartography):** a new C01 draft on the K02 scope (`scout/K02-gap-scout.md:91-247`); C05's §7 re-run on the new slug/topic (`cov/C05-collision.md:201-241`); C02's row uses the new 1,291-char-scale topic text (length unknown until drafted); the dream/trance draft is retired as a spare by integrator note.
- **B (dream/trance):** a filed overrule of `scout/K02-gap-scout.md:78` with the fresh-measurement rationale; C05's §7 re-run against C01's exact 1,291-character topic (`C01-entry-draft.md:113`); C02's row copies that topic byte-equal; the cartography proposal is retired as a spare.

---

## 8. Integration-ready claim-C summary

> **Claim C (coverage) — unresolved selection; no landing at this cut.**
> Two independently verified, genuinely unowned gaps are on file: **cartography/mapmaking** at `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (K02; 11 topic hits all metaphor/verb/handoff, 0 owners; cosmography disclaims survey maps at `cosmology-cosmography.md:71,102`; low demand, 7 genuine files/9 lines; not in any prior registry) and the **dream/vision/trance complex** at `corpus/knowledge/myth-symbol/dream-vision-trance.md` (K04; 0 owners of the state, 2 adjacent hits; demand 52 on the five-family union, 61 with singular `vision`; named r42 R2 but re-measured absent at `c9f4eaa`).
> C01 drafted **dream/trance** (483 lines, 70,992 B, 9 head fields, 1,291-char topic); C05 cleared that exact path on 8 checks, with a two-path landing delta. X01 measured 14 distinct couples tokens in the draft, so the post-C census for this path is `2730+14=2744` if the field is unchanged (`cross/X01-trades.md:487-497`). C01's own clause makes the draft a **spare** if K02 names a different gap — which K02 now has. K02's filed screen calls dream/trance **"carried — reject"** (`K02-gap-scout.md:78`). Claim C is `+1` only.
> **The integrator must rule on "not carried from a prior round" before bytes move.** Option A (cartography) is the threshold-safe default but needs a new draft and all audits; Option B (dream/trance) is ready but needs an explicit, filed overrule of K02's screen. Do not land both. Coverage remains **223**; no `improved` verdict is available yet.
> Mechanical arithmetic, if either lands: total **224**; sweep **224 == 224**; footer vector `25/26/26/29/24/94` (A) or `25/27/25/29/24/94` (B); both simulated green in `.scratch` and removed.

---

## 9. Risks and traps

| # | risk | evidence | guard |
|---|---|---|---|
| C-R1 | **Two scouted gaps, one claim slot** | K02 `:8,78,85`; K04 `:10`; C01 `:9`; C05 `:17,195` | integrator rules A or B before bytes; loser becomes a named spare |
| C-R2 | "Not carried" is read two ways | `claims.json:39`; K02 `:78`; K04 `:161-166` | the ruling is explicit and filed; do not omit K02's screen from the round record |
| C-R3 | Two seats author the same gap (r42 C01/C04) | `reports/round-42/validation.json:22` | one draft for the chosen gap; no second authoring seat |
| C-R4 | A stale path overwrites an existing entry (r42 animal/plant) | same ruling line | C05's live partition listing; apply as `A`; `git status` gate (A01 `:205-230`) |
| C-R5 | Green 224==224 certifies a duplicate topic | sweep has no ownership leg (`R01-review.md:394`; r43 C07 §3.5) | post-apply topic-owner re-check |
| C-R6 | Rev 2.5 prose vector repeats the 217 defect | `corpus/README.md:10-11`; X02 `:70-72` | C02 shows the arithmetic; integrator sums the vector |
| C-R7 | README row is not byte-equal to the entry's topic | `sweep.py:74-84,139-147` | row generated from `topic_of(draft)`, continuations space-joined; C01's topic is 1,291 chars on one line |
| C-R8 | Row inserted at the wrong sort position | README `:215-216` / `:240-241` | ASCII sort check with the slug inserted |
| C-R9 | Cartography's low demand is read as a weak entry | K02 `:138-179` | the claim sets no demand threshold; the structural disclaimer at `cosmography:71,102` is the argument |
| C-R10 | Dream/trance's shelf risk (Bourguignon/Winkelman/Lambek/Csordas/Vitebsky unregistered) | K04 `:146-159`; C01 `:115-119` | build from the in-corpus shelf; every unretrieved item `(to-verify)` |
| C-R11 | C05's clearance is treated as covering both candidates | C05 `:10,17,250-255` | re-run C05 §7 on the chosen draft's exact topic |
| C-R12 | C's couples tokens silently move O's census denominator | X00 `:96-116`; X01 `:487-497` measures `N=14` for the current dream/trance draft | census at 223 first; post-C `2730+N` (dream path `2744` provisional on the final couples field); one artifact |
| C-R13 | `run-validation.py` is run in-tree | absolute round rule | absent at scribe time; integrator files the receipt outside the tree |
| C-R14 | S01/X02/A01 cuts are cited as current | S01 `:367-368`; X02 `:59-72` | cite them as earlier cuts; this file is the current C assembly |

---

## 10. Reproducibility index

```
git rev-parse HEAD                                                            -> c9f4eaa707b6e977ff6e1616463e91f4b8afea5d
git status --porcelain                                                        -> ?? reports/round-44/ only
find corpus/knowledge -name '*.md' | wc -l                                    -> 223
for d in corpus/knowledge/*/; do ls "$d"*.md | wc -l; done                    -> 94 25 25 26 29 24
python3 -B reports/round-28/readme/sweep.py                                   -> rows 223 files 223, exit 0
python3 -B reports/round-28/readme/sweep.py --selftest                        -> 12/12, exit 0
sha256sum corpus/README.md                                                    -> 7c788a1d…ef31cdcd
find corpus/knowledge -name '*.md' -print0 | sort -z | xargs -0 sha256sum | sha256sum -> 45bed989…d4b2fee

# Candidate A
find corpus/knowledge -type f \( -iname '*cartograph*' -o -iname '*mapmaking*' \
  -o -iname '*portolan*' -o -iname '*cadastr*' \) | sort                       -> no output
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ -> 11 hits, all non-owners
grep -n 'T-O\|survey maps\|not cartographic' corpus/knowledge/myth-symbol/cosmology-cosmography.md -> :71, :102
grep -nE 'cartograph|mapmaking|portolan|cadastr|mappa' reports/round-19/gaps.md ... -> no output
python3 - <<'PY'  # scratch sim: culture-material 26, rows 224, vector 25/26/26/29/24/94, ok True
PY

# Candidate B
find corpus/knowledge -type f \( -iname '*dream*' -o -iname '*trance*' -o -iname '*vision*' \
  -o -iname '*ecsta*' -o -iname '*shaman*' -o -iname '*incubat*' \) | sort    -> no output
grep -rilE -- '^- topic:.*dream' corpus/knowledge/*/*.md                      -> divination-omen-systems.md
grep -rilE -- '^- topic:.*trance' corpus/knowledge/*/*.md                     -> no output
grep -rilE -- '^- topic:.*ecsta' corpus/knowledge/*/*.md                      -> no output
grep -rilE -- '^- topic:.*vision quest' corpus/knowledge/*/*.md               -> no output
grep -rilE -- '^- topic:.*visionary' corpus/knowledge/*/*.md                  -> no output
grep -rilE -- '^- topic:.*shaman' corpus/knowledge/*/*.md                     -> civilizations/mongol.md
grep -rniE '^#{1,4} .*(dream|trance|ecsta|shaman|incubat|vision quest|altered state)' corpus/knowledge -> :1 divination; :36 australia
wc -lc reports/round-44/cov/C01-entry-draft.md                                -> 483 70992
awk 'NR==113{print length($0)}' reports/round-44/cov/C01-entry-draft.md       -> 1291
python3 - <<'PY'  # scratch sim: myth-symbol 27, rows 224, vector 25/27/25/29/24/94, ok True
PY
```

`reports/round-44/run-validation.py` was **not** run: it is absent at scribe time and the round's absolute rule forbids in-tree runner execution. No corpus byte was staged; no filed byte was edited; no git commit/push/network.

---

## 11. Unknowns / to-verify

- **The integrator's ruling is the largest unknown.** Until "not carried from a prior round" is interpreted, neither candidate has a complete claim path: A lacks a draft; B lacks the overrule.
- **C02, C03 and C04 are absent.** No README diff, no source audit, no contract audit exists for either target. C01's seven spot-checked anchors and C05's eight collision checks are not substitutes.
- **C01's draft is unaudited.** Its 1,291-character topic, 9-field head block and in-corpus shelf are measured here only at the shape level; C03 must resolve every backticked path and line.
- **K02's cartography draft does not exist.** Its demand is low (7 genuine files/9 lines); the entry's quality is unknown until drafted.
- **`N` (the chosen entry's distinct couples tokens)** is measured by X01 at **14** for the dream/trance draft's 284-line cut (`cross/X01-trades.md:487-497`), giving `refs=2730+14=2744` if C01's couples field is unchanged; re-measure after the final cut. Cartography's `N` is unknown until drafted. O's post-C census is `refs=2730+N` (`cross/X00-connector.md:96-116`).
- **K04's 52 is the five-family union**; 55 with `visions`, 61 with singular `vision` (§3.4). Do not quote 52 without the term set.
- **No external source was fetched** (no network). All external shelf items remain `(to-verify)`.
- **S01, X02 and A01 were written at earlier cuts.** S01 §3.2 still says K02 is absent (`:367-368`); X02 C-5 still says no scout (`:59-72`). Both are superseded by K02 at 17:24Z; cite them as earlier cuts, not current measurements.
