# C06 — source audit (claim C): every citation in the assembled cartography entry, resolved live

- Seat **C06** | role verifier | claim **C** (coverage) | round 47, loop 2, position 1
- Baseline: `git rev-parse HEAD` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`reports/round-47/claims.json:7`), observed 2026-10-19T18:06Z
- Out path: `reports/round-47/cov/C06-source-audit.md` (this file only; no corpus write, no filed-byte edit)
- Mission (verbatim, `reports/round-47/targets.json:26`): *"Source audit: audit the assembled cartography draft — every backticked in-repo path resolves, every cited line is real, every external source is (to-verify) not asserted-read. Report per-citation status."*
- Audited artifact: the four C fragments assembled in scratch — C04 head (`reports/round-47/cov/C04-entry-header.md`), C01 §§1–4 (`cov/C01-entry-a.md`), C02 §§5–9 (`cov/C02-entry-b.md`), C03 §§10–15 (`cov/C03-entry-c.md`) → `.scratch/c06/assembly.md`, 855 lines, sha256 `2422ca96c2fab0385b1e6f89a8faa4f72134c59cde5522d9d498720b149b0942`. The assembly is a scratch concatenation of the fenced blocks; it is not the integrator's applied bytes.

## Verdict — PASS on every hard source criterion, with three assembly corrections

The assembled entry cites **226 backticked in-repo path records** (225 resolved + the one allowed proposed landing path). **Zero** point at a missing file, a blank single line, an out-of-range line, an unresolved KTD id, or a mismatched digest. All **nine** sha256 pins in the head block match the live files. All **21** `- couples:` targets resolve from `corpus/knowledge/culture-material/`. The `- topic:` line is byte-equal to the r44 seed (775/775 chars). The external shelf is honestly framed: **49 of 53** external-source lines carry an inline `(to-verify)` or a not-consulted marker; the other four are dispositioned below (two are projection names, not citations; two are covered by the head shelf's blanket but should carry inline marks).

| Gate | Result | Evidence |
|---|---|---|
| every backticked in-repo path resolves | **PASS** — 225/225 resolved records, 1 allowed absent (target) | §5, §11 |
| every cited line real | **PASS** — 0 missing/out-of-range/blank single-line | §5; 29 independent needle assertions re-run, 29/29 |
| sha256 pins match | **PASS** — 9/9 | §5; `sha256sum` transcript §B |
| couples resolve | **PASS** — 21/21 | §5 |
| external sources marked | **PASS with 2 recommendations** — 49/53 inline; 4 dispositioned | §8 |
| no unread work presented as inspected | **PASS** — every assertion-word line is a disclaimer | §8.3 |
| section/cross-reference integrity | **2 semantic mismatches** — form typology cited as §2, is §4.1 | §10 |
| head-vs-body count integrity | **1 error** — "six load-bearing anchors", 9 pinned | §10 |

**Landing recommendation: apply after the three corrections in §10.** None is a source-integrity failure; all are one-line edits in draft bytes. The entry should not be applied with the `§2` form references or the "six" wording unchanged.

---

## 1. What was audited, and what was not

Audited:

1. The **r44 seed** `reports/round-44/scout/K02-gap-scout.md` (433 lines, sha256 `a72fff27ee193cc12e689b5a3b485d3c0389bd4317b7810abf745ee441f335f6`) — the only filed C text that predates the fragments. This is the citation source C01–C04 inherited.
2. **Each C fragment** (`C01`, `C02`, `C03`, `C04`) at its own fence, including its seat-report sections.
3. The **assembled fenced entry** (head + §§1–15) in `.scratch/c06/assembly.md`.

Not audited:

- **External works' content.** No network at seat time. This audit certifies that every external item is *marked* unread and that no page, quotation or figure is asserted as inspected; it cannot certify bibliographic accuracy beyond author/year/title-level identity. Unknown edition/page details remain `(to-verify)`.
- **The integrator's final byte assembly.** The scratch assembly concatenates the four fenced blocks in the order C04 → C01 → C02 → C03 with blank lines. The integrator must re-run the gate in §11 on the actual file.
- **Topic quality / boundary correctness** — C07 (contract), C08 (boundary), R03/X04 (content) own those. This seat checks citations, resolution, digests and honesty marks.

## 2. Method — deterministic, re-runnable, baseline-evaluated

The auditor is embedded verbatim in Appendix A. It:

1. Extracts every backticked token that matches a path (`.md/.py/.json/.txt/.yml/.yaml`), including `path:line`, `path:line-line`, `path:line,line` and continuation tokens (`:71`, `:102`) that attach to the previous resolved path.
2. Resolves each path against the live tree with an explicit preference order: repo-relative prefix → corpus-knowledge basename (unique) → repo-root file → same-directory as the last resolved path → unique report path → ambiguous. Relative `../…` couples resolve from `corpus/knowledge/culture-material/`.
3. Evaluates line numbers against **`git show <baseline_commit>:<path>`**, not the worktree. Round-47 draft artifacts do not exist at `6e9a30d`, so the tool falls back to the worktree and labels the record `worktree (untracked at baseline)` rather than pretending they were in the baseline.
4. Treats a **single blank line** as a hard failure; a blank line *inside a range* is reported as `blank-in-range` (a precision warning, not a failure).
5. Checks `sha256` claims by hashing the resolved file bytes (at the baseline when tracked).
6. Checks KTD source ids: every `KTD-*-S-NNNN` must be defined in the same draft. The assembled entry uses none, so the clause is vacuously satisfied.
7. Scans mentioned external authors/works and classifies each line `to-verify-inline`, `covered-by-sources-blanket`, `in-sources-no-marker`, or `body-no-marker`.

Exit contract: `0` all citations resolve; `1` any hard failure; `2` malformed input (missing draft). A count of zero citations is not green — it means the extractor found nothing, which the report must treat as `could-not-evaluate`.

Re-run command:

```text
python3 -B <extracted-audit.py> <staged-entry.md> --commit 6e9a30d \
  --allow-absent cartography-and-mapmaking.md --json <out.json>
```

## 3. Baseline measured at audit time

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe          # == claims.json:7 "6e9a30d"
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory
```

No tracked file was modified by this seat; no corpus byte was staged or written. The only writes are this report and disposable `.scratch/c06/` instruments.

## 4. Per-fragment results

Counts are citation **records**, not unique paths; a `path:line` plus a following `:line` continuation counts twice. Hard failures are per-record.

| Fragment | Records | Hard failures | Where the failures are | External lines | Disposition |
|---|---:|---:|---|---:|---|
| C01 `cov/C01-entry-a.md` | 87 | 2 | **seat-report only**: `cov/C05-freshness.md` (missing `reports/round-47/` prefix) at `C01:79`; bare `targets.json` (ambiguous) at `C01:355`. The fenced §1–4 body contributes **0**. | 13 | 12 inline `to-verify`; 1 body-no-marker is the Russell quotation of `cosmology:102` — an in-corpus source, already registered there |
| C02 `cov/C02-entry-b.md` | 122 | **0** | — | 32 | 11 inline; 21 rely on the head shelf/§9 blanket; 4 survive into the assembly and are dispositioned in §8.3 |
| C03 `cov/C03-entry-c.md` | 74 | **0** | — | 12 | 11 inline; 1 false positive (the Russell quote again) |
| C04 `cov/C04-entry-header.md` | 149 | 1 | **self-audit only**: bare `sweep.py` at `C04:186` is ambiguous among four files (`round-27/readme`, `round-27/pinsweep`, `round-28/readme`, `round-28/sweep`); the surrounding text names round-28/readme. The fenced head contributes **0**. | 21 | all 21 inline `to-verify` |
| **Assembly** | **226** | **0** | — | 53 | 49 inline; 4 without (2 non-citations, 2 covered by the head shelf) |

The two C01 seat-report misses are report-hygiene defects, not entry defects: the fenced body does not contain them, and the assembly audit is clean. They are named because a reviewer following the seat report would hit a dead path.

## 5. The assembled entry — measured results

Artifact: `.scratch/c06/assembly.md`, 855 lines, sha256 `2422ca96c2fab0385b1e6f89a8faa4f72134c59cde5522d9d498720b149b0942`.

```text
DRAFT .scratch/c06/assembly.md  commit=6e9a30d
citations=226  hard_bad=0  sources_block=[5, 47]  blanket=True
external-source lines=53  status={'to-verify-inline': 49, 'body-no-marker': 4}
DIGEST draft:7  corpus/knowledge/myth-symbol/cosmology-cosmography.md -> match
DIGEST draft:8  corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md -> match
DIGEST draft:9  corpus/knowledge/myth-symbol/direction-symbolism.md -> match
DIGEST draft:10 corpus/knowledge/culture-material/architecture-settlement-lexicon.md -> match
DIGEST draft:11 corpus/knowledge/culture-material/writing-media-surface-economy.md -> match
DIGEST draft:12 corpus/knowledge/culture-material/transport-mobility-lexicon.md -> match
DIGEST draft:13 corpus/knowledge/civilizations/mesoamerica-primary-sources.md -> match
DIGEST draft:14 corpus/knowledge/culture-material/timekeeping-instruments.md -> match
DIGEST draft:23 corpus/knowledge/verification/calibration-registry.md -> match
```

Structural facts:

| Check | Measured |
|---|---|
| unique files cited | **38** (33 in `corpus/knowledge/`, 5 in `reports/` or repo root) |
| unique `path:spec` pairs | **50** |
| H1 headings | **1** |
| `- topic:` lines | **1**, byte-equal to the r44 seed (775/775 chars) |
| `- sources:` lines | **1**, detected block lines 5–47 |
| section headings | **§1–§15, contiguous**, no dangling `§N` reference (all 15 exist) |
| `(to-verify)` occurrences | **41** |
| couples targets | **21/21 resolve** from `corpus/knowledge/culture-material/` |
| sha256 pins | **9/9 match** |
| unresolved KTD ids | **0** (none used) |
| external-source assertion words | 6 lines, all disclaimers ("not consulted", "not inspected", "no network") |

The 4 external lines without a marker are:

| Assembly line | Line | Disposition |
|---:|---|---|
| 267 | projection comparison row, `equirectangular, Mercator, stereographic…` | **not a citation** — "Mercator" names a projection, not a work; no mark owed |
| 313 | projection table row, `Mercator` | **not a citation** — same |
| 620 | `Mercator's *Atlas* (1595)` in the §9 word bank | **a bibliographic claim**; covered by the head shelf ("Mercator's atlas — editions `(to-verify)`") and C02 §9's OED-level note, but should carry an inline `(to-verify)` per `citation-format-and-source-registry.md:35` |
| 625 | `Tabula Peutingeriana` as the etymon of "table" | **a bibliographic claim**; covered by the head shelf ("editions `(to-verify)`"), but should carry an inline mark at first use |

---

## 6. The r44 seed — per-citation ledger (the text every fragment inherited)

The seed is a filed r44 byte and was not edited. It carries **137 backticked citation records** → **58 unique raw paths** → **52 unique resolved files** → **63 unique `path:spec` pairs**. **Four hard failures**:

| # | Seed line | Citation | Measured | Verdict |
|---:|---:|---|---|---|
| 1 | `K02-gap-scout.md:375` | `C01-entry-draft.md:9` | resolves to `reports/round-44/cov/C01-entry-draft.md:9`, which is a **blank line** (line 8 is the last text of the preamble; line 10 is `## 1`) | **BAD** — the citation anchors nothing |
| 2 | `K02-gap-scout.md:376` | `reports/round-44/cov/C05-collision.md:10` | line 10 is **blank**; the verdict heading is line 11 | **BAD** — the citation anchors nothing |
| 3 | `K02-gap-scout.md:243` | `cosmography-cosmography.md:102` | **no such file**; the corpus file is `cosmology-cosmography.md` | **BAD** — filename typo; the correct citation is `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102` |
| 4 | `K02-gap-scout.md:204` | `README.md` | ambiguous between `corpus/README.md` and root `README.md`; the line says "Root lane docs", so the intended target is root `README.md` | **WARN** — context resolves it, but the bare token is ambiguous |

Three line-number **alignment** defects (the file resolves and the line is real, but the cited line does not carry the claim attributed to it):

| Seed line | Seed's attribution | Live text at the cited line | Correct anchor |
|---:|---|---|---|
| `:189` / `:193` (boundary table) | `transport-mobility-lexicon.md:28,:35,:117` carries "routes, maintenance, the four-layer mobility system" | `:28` = "a route is only real if someone maintains it"; `:35` = the Inca Qhapaq Ñan row; `:117` = DR-TR-02 (maintenance clause). The **four-layer frame** is at `:4` (topic), `:24` (heading), `:26` (the four layers), `:127` (what the entry supplies) | cite `:4,:24-26` for the frame; `:28,:117` for maintenance |
| `:188` | `sacred-topography-pilgrimage.md:66-69,:124` carries "the three route types … the votive economy" | `:66-67` are the rites-of-passage table rows; `:68` is blank; `:69` is the three route types; `:124` is build step 4 ("Pick the route type"), not the votive economy | route types `:69`; votive economy `:74-77`; `:124` is a build step |
| `:260` | Rykwert/Kostof/Steinhardt at `architecture-settlement-lexicon.md:95-97` | the **body uses** are at `:95` (Rykwert/groma), `:96` (Kostof), `:97` (Steinhardt); the **source registration** is the one-line `- sources:` at `:3` | cite `:3` for registration; `:95-97` for body evidence |

Two shelf-classification corrections:

- **Boone (2000) is already in-corpus.** `symbolism-synthesis-method.md:12` registers "Boone (2000), *Stories in Red and Black*, U Texas Press"; `direction-symbolism.md:8` reuses it. The seed puts Boone in Tier B. It should be **Tier A** (cite `symbolism-synthesis-method.md:12` / `direction-symbolism.md:8`) and remain `(to-verify)` for page-level quotations. Note `mesoamerica-primary-sources.md:17` registers Boone (2007), a different work — do not conflate.
- **The *Tabula Peutingeriana* has one incidental in-corpus mention, not a registration.** `transport-mobility-lexicon.md:8` names it as "the network map" in the cursus publicus source note. That is evidence the object is known in-lane, not a source registration; keep it Tier B with editions `(to-verify)` and cite `:8` only as a coupling, never as "registered at".

The seed's own honesty framing is adequate at shelf level: `:265` says Tier B editions/volumes/page ranges are `to-verify` at authoring and `:286` says every Tier B item must be marked `(to-verify)` for direct quotation. The defect is that the individual bullets do not each carry the mark, and two body lines (`:243` typo; `:375-376` blank anchors) do not survive a mechanical audit.

## 7. Load-bearing citations, re-read live

These are the citations on which the gap claim and the boundary table stand. Each was read at the exact line at `6e9a30d`; the quoted text is the live text, not the seed's paraphrase.

| # | Citation | Live text (excerpt) | Verdict |
|---:|---|---|---|
| 1 | `myth-symbol/cosmology-cosmography.md:71` | "Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, **not survey maps** (§10)" | PASS — the charter disclaimer |
| 2 | `myth-symbol/cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, **not cartographic** claims" | PASS — the flat-earth calibration |
| 3 | `myth-symbol/cosmology-cosmography.md:3,:29` | `:3` "the five independent design axes (center / layer-count / direction-code / world-shape / age-doctrine)"; `:29` the five questions | PASS — the five-axis anchor the boundary table needs; the seed did not cite these lines |
| 4 | `myth-symbol/sacred-topography-pilgrimage.md:5` | "the place register … the holy-site typology … the route as rite" | PASS |
| 5 | `myth-symbol/sacred-topography-pilgrimage.md:69` | "**The three route types.** (a) **Fixed itinerary** … (b) **Votive ramble** … (c) **Circuit**" | PASS — not `:66-69` |
| 6 | `myth-symbol/sacred-topography-pilgrimage.md:74-77` | "## 5. The votive economy — the object, the receipt, the token" | PASS — not `:124` |
| 7 | `myth-symbol/direction-symbolism.md:51` | "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic … declination" | PASS |
| 8 | `culture-material/architecture-settlement-lexicon.md:95` | "surveyed with the **groma** … The grid is **cadastral**: a state that *measures land* builds this city" | PASS; registration is `:3` |
| 9 | `culture-material/writing-media-surface-economy.md:3` | "the seven surface families … each with its preparation chain … cost driver" | PASS; the source block is `:5-27` |
| 10 | `culture-material/transport-mobility-lexicon.md:26` | "**Four layers** — a mobility system is ROUTE … VEHICLE … DRAFT … WORD" | PASS — the four-layer anchor |
| 11 | `culture-material/transport-mobility-lexicon.md:28` | "a route is only real if someone maintains it" | PASS |
| 12 | `culture-material/transport-mobility-lexicon.md:117` | DR-TR-02: "Require a maintenance clause … for every named route and bridge" | PASS |
| 13 | `civilizations/mesoamerica-primary-sources.md:58` | "Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) … Cloth maps/migration-conquest accounts" | PASS; LIEN registration at `:28`; sources block opens `:4` |
| 14 | `civilizations/polynesia-navigation.md:52` | "Distinguish **horizon compass**, **ordered steering-star sequence**, … **latitude/landfall clue**; these are related operations, not synonyms" | PASS; sources line is `:3` |
| 15 | `culture-material/timekeeping-instruments.md:50` | "the minute … longitude at sea" | PASS |
| 16 | `myth-symbol/mineral-stone-symbolism.md:9` | "Inherited bibliography … **not re-fetched in this seat — no network at this run**, so every item below is `(to-verify)`" | PASS — the house convention the cartography shelf follows |
| 17 | `verification/citation-format-and-source-registry.md:35` | "An unresolved reference or untested factual claim carries `(to-verify)` beside that specific reference/claim" | PASS — the rule applied in §8.3 |
| 18 | `corpus/QUALITY.md:5-20` | provenance / calibration / coupling / usability / canon hygiene | PASS — all five clauses are addressed by the assembled entry |

An independent needle check of the 29 assertions the drafts themselves rely on (C04's 23 plus C03's additional lines) returned **29/29 PASS**; the transcript is in §B. This is the "every cited line is real" leg in its strong form: the line exists, is non-blank, and contains the claim being attributed to it.

## 8. Source shelf audit

### 8.1 Tier A — in-corpus registrations, exact lines

| Work | Registration (live) | Body use | Status |
|---|---|---|---|
| Smith (1987), *To Take Place*; Wheatley (1971) | `cosmology-cosmography.md:6` (inside the sources block opened at `:4`) | `:42` (J.Z. Smith caution) | PASS |
| Horowitz (1998), *Mesopotamian Cosmic Geography* | `cosmology-cosmography.md:10` | `:49`, `:96` | PASS |
| Needham (1959), *Science and Civilisation in China* vol. 3 | `cosmology-cosmography.md:12` | `:97`, `:100`, `:114` | PASS |
| Russell (1991), *Inventing the Flat Earth* | `cosmology-cosmography.md:19` and `:102` | `:102`, `:146` | PASS |
| Egeria, *Itinerarium*; Petrarch; Ibn Jubayr; Ibn Baṭṭūṭa | `sacred-topography-pilgrimage.md:167-168` (all marked `(to-verify)` there) | route-document genre | PASS |
| Rykwert (1976); Kostof (1991); Steinhardt (1990) | `architecture-settlement-lexicon.md:3` (one-line sources field) | `:95-97` | PASS; do not cite `:95-97` as the registration |
| LIEN record (UFM Quauhquechollan) | `mesoamerica-primary-sources.md:28` (sources block opens `:4`) | `:58` | PASS |
| Polynesian navigation shelf | `polynesia-navigation.md:3` (sources field) | `:52`, `:63`, `:72`, `:74` | PASS; `:52-74` is body, not registration |
| Surface-economy shelf | `writing-media-surface-economy.md:5-27` (sources block) | `:3` topic; `:48`, `:64-78`, `:81` | PASS |
| **Boone (2000), *Stories in Red and Black*** | **`symbolism-synthesis-method.md:12`; `direction-symbolism.md:8`** | `:27`; `direction:78` | **promote from Tier B to Tier A**; page-level `(to-verify)` |

### 8.2 Tier B — measured in-corpus footprint

Sweep over all 223 entries at `6e9a30d`; counts are files/lines containing the name:

| Work | In-corpus hits | Disposition |
|---|---|---|
| Harley & Woodward; Harley 1989 | 1 line — `civilizations/celts.md:167` "British Library Harley MS 5280" (a manuscript shelfmark) | **false positive**; no registration; keep Tier B |
| Woodward | 0 | Tier B |
| Wood, *The Power of Maps* | 0 | Tier B |
| Monmonier | 0 | Tier B |
| Jacob, *The Sovereign Map* | 0 | Tier B |
| Ptolemy, *Geography* | 6 incidental lines — `writing-systems.md:97` (cartouche), `cosmology-cosmography.md:100` (sphere row), `era-periodization-models.md:13,98` (Ptolemy's Canon), `calendar-festival-systems.md:54` (Ptolemy III), `timekeeping-instruments.md:5` (Ptolemy *Analemma*) | **none is the *Geography***; do not let "Ptolemy" in a body line imply the *Geography* was consulted |
| Campbell (1987) | 0 | Tier B |
| Edson (2007) | 0 | Tier B |
| Kain & Baigent (1992) | 0 true hits (4 lines match `Kain` inside *kaikaina*, *Doukaina*, *kain tayo*) | Tier B |
| Mundy (1996) | 0 | Tier B |
| Boone (2000) | 5 lines / 3 files: `symbolism-synthesis-method.md:12,27`; `direction-symbolism.md:8,78`; `mesoamerica-primary-sources.md:17` (Boone **2007**, a different work) | **Tier A** for 2000; still page-level `(to-verify)` |
| Pickles (2004) | 0 | Tier B |
| Buisseret (ed.) (1992) | 0 | Tier B |
| Snyder (1987) | 0 | Tier B |
| Dilke (1971) | 0 | Tier B |
| al-Idrisi (1154) | 0 | Tier B |
| *Tabula Peutingeriana* | 1 incidental — `transport-mobility-lexicon.md:8` ("*Tabula Peutingeriana* (c. 400 CE) as the network map") | not a registration; keep Tier B; may cite `:8` as a coupling |
| Ortelius (1570); Mercator's atlas | 0 | Tier B |

### 8.3 Honesty check — no unread work presented as inspected

- The head block's shelf opens: "**not consulted this round** (no network at seat time) … every edition, volume and page locator `(to-verify)`; no unread work is presented as inspected" (`C04-entry-header.md:139`).
- C02's body closes §9 with: "All etymologies are standard-shelf but **`to-verify` at OED level** … no network at seat time" (`cov/C02-entry-b.md:419`).
- C03's limits: "No external source was fetched, resolved or page-checked in this seat (no network)" (`cov/C03-entry-c.md:226`).
- Six assertion-word lines in the assembly ("inspected", "consulted", "fetched", "page-checked") were read: every one is a negation or a disclaimer. **No external work is quoted at page level; no page number, figure, percentage or edition is asserted as inspected.**

The only two claims that should gain an inline mark are the two in §5's table (`Mercator's *Atlas* (1595)`; the *Tabula Peutingeriana* etymon). Both are covered by the head shelf's blanket, but `citation-format-and-source-registry.md:35` asks for the mark beside the specific claim.

## 9. Corpus citation-format compliance

| Clause (`verification/citation-format-and-source-registry.md`) | Assembled entry | Verdict |
|---|---|---|
| `(to-verify)` beside the specific unresolved claim (`:35`) | 41 marks; 49/53 external lines inline; two bibliographic claims rely on the shelf blanket | **PASS with 2 recommendations** |
| No fabricated page/edition locators (`:30-31`) | no page-level external locator is asserted; every edition/page is `(to-verify)` | PASS |
| Secondary access must say "original not consulted (to-verify)" (`:33`) | not used — no cited-in chains | PASS (vacuous) |
| KTD ids must resolve to an entry-local registry (`:25`, `:75`) | no KTD ids used; the house style used by `mineral-stone-symbolism.md:9` (path:line + author-year + inherited bibliography) is followed | PASS |
| A bibliography at the top does not support every sentence (`:26`) | body claims carry `path:line`; the shelf supports mechanisms, not world claims | PASS |
| Quotations retain wording; translation status named (`:36`) | all direct quotations are from in-corpus lines, whose editions are registered there; no external work is quoted | PASS |

The entry's in-corpus citation style is consistent with the newest culture-material landings: repo-relative `path:line`, `:line` continuations, `sha256` pins for load-bearing anchors, and an inherited-bibliography paragraph that marks every external item `(to-verify)` (precedent: `mineral-stone-symbolism.md:9`; `writing-media-surface-economy.md:15-27`).

## 10. Corrections before landing (all are draft-byte edits, none is a source failure)

1. **`§2` → `§4.1` for the form typology.** In C03 (assembly lines 684 and 789; C03 file lines 79 and 184):
   - "The sentence names the form (**§2**)" — the form typology is C01 **§4.1** ("The eight forms"; §4 is "Material and trade classes — the map-object typology"). C01 §2 is "What makes a map a register — the five-condition test".
   - "the typology in **§2** is by *question*" — same correction.
   This is the only semantic cross-reference defect; all `§N` targets exist (no dangling refs).
2. **"six load-bearing anchors" → "nine".** `C04-entry-header.md:117` (assembly line 6) says "sha256 pinned for the six load-bearing anchors"; **nine** files are pinned (`cosmology`, `sacred-topography`, `direction`, `architecture`, `writing-media`, `transport`, `mesoamerica`, `timekeeping`, `calibration-registry`; assembly lines 7–14 and 23). The pins themselves are all correct (9/9 match).
3. **Disposition C02 §9 explicitly.** The r44 seed's ten-section outline has **no** "container-name fossil" section; `K02-seed-extract.md:220-232` flagged that the r47 executor missions were copied from the r42 lithic skeleton, which is where that phrase comes from. C02's §9 content is cartography-specific (map/chart/atlas/portolan/cartouche word bank) and its citations resolve, so it is not a source defect — but the integrator must either keep it and record the outline divergence, or drop it. Do not let it displace the seed's §6 reproduction / §7 silences material.
4. **Add inline `(to-verify)` at first use** for `Mercator's *Atlas* (1595)` (assembly line 620) and the *Tabula Peutingeriana* etymon (assembly line 625), per `citation-format-and-source-registry.md:35`.
5. **Tighten the CAL-03 range.** `calibration-registry.md:78–88` includes blank lines 79 and 88; the substantive CAL-03 text is **`:80–87`**. This is a precision warning, not a failure; the current citation resolves.
6. **C01 seat-report path hygiene (not the entry):** `cov/C05-freshness.md` should be `reports/round-47/cov/C05-freshness.md` (`C01-entry-a.md:79`); `targets.json` should carry its round path (`C01-entry-a.md:355`).

No correction requires touching a filed round or a corpus byte. All six are edits to r47 fragments, which belong to their authors or to the integrator's assembly step.

## 11. Landing-time gate for the integrator

1. Extract Appendix A to `.scratch/c06/audit.py`.
2. Assemble the entry at `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (A, never M — the path is absent at `6e9a30d`; `ls` → "No such file or directory").
3. Run, against the **final assembled bytes**:

```text
python3 -B .scratch/c06/audit.py \
  corpus/knowledge/culture-material/cartography-and-mapmaking.md \
  --commit 6e9a30d --allow-absent cartography-and-mapmaking.md --json .scratch/c06/final.json
```

Required output:

```text
citations=<N>  hard_bad=0  sources_block=[a, b]  blanket=True
external-source lines=<M>  status={...}          # no 'in-sources-no-marker'
DIGEST ... -> match   (9 lines)
exit=0
```

Hard-fail conditions — **do not land** if any appears:

- any `BAD` record (missing file, blank single line, out-of-range line, ambiguous citation);
- any `DIGEST ... -> MISMATCH` or `UNRESOLVED`;
- any `in-sources-no-marker` line in the `- sources:` block;
- `citations=0` (the extractor found nothing — treat as could-not-evaluate, not green);
- more than one `- topic:` or `- sources:` line, or no `- topic:`.
- `grep -n 'cosmography-cosmography' <entry>` returns anything (the seed typo reappearing);
- `grep -n 'six load-bearing' <entry>` returns anything (correction 2 not applied);
- the form-typology references still read `§2` (correction 1 not applied).

Allowed absent path: **only** `corpus/knowledge/culture-material/cartography-and-mapmaking.md` itself (the proposed landing). Any other absent path is a failure.

## 12. Limits and owed

- **No network.** External works are audited for *honesty of marking*, not for bibliographic accuracy. Editions, volumes, page ranges and quotations remain `to-verify`; this seat cannot upgrade them.
- **The audit ran on a scratch assembly**, not the integrator's final bytes. The gate in §11 must be re-run after the §10 corrections and after the actual concatenation; the per-fragment results in §4 are not a substitute.
- **The r44 seed is a filed byte**; its four defects and three alignment errors are reported here, not repaired. The blank-line citations (`C01-entry-draft.md:9`, `C05-collision.md:10`) and the `cosmography` typo must not be copied into the entry; the assembled entry does not contain them.
- **No filed byte, corpus byte, gate, or packet surface was edited.** The only writes are this report and `.scratch/c06/` instruments; no commit, no install, no network, no round-runner.
- **Owed to the integrator:** apply the six corrections in §10, then run §11 and file the output. **Owed to C12:** the shelf-content judgment (whether each Tier B work actually supports the use the entry makes of it) remains a reading task; this seat certifies only that the shelf is marked unread and that the in-corpus anchors resolve.

---

## Appendix A — the auditor (verbatim, re-runnable)

Extract this fence to `.scratch/c06/audit.py`; it is the instrument used for every count above. It assumes the lane root as cwd and `git` available.

````python
#!/usr/bin/env python3
"""C06 source auditor (r47, claim C).

Extracts in-repo path citations from a markdown draft and resolves each against
the repository at a given commit (default: worktree). Checks that every cited
line exists and is non-blank. Scans external-source mentions for an honest
(to-verify) / not-consulted marker. Checks sha256 pins and KTD ids.

Usage:
  python3 -B audit.py DRAFT [--commit SHA] [--json OUT] [--allow-absent names]
Exit: 0 all citations resolve; 1 any hard failure; 2 malformed input.
"""
import argparse, re, subprocess, sys, json, os

CITE_RE = re.compile(r'`([^`]+)`')
LINESPEC = re.compile(r'^:\s*(\d+(?:\s*[-–,]\s*\d+)*)\s*$')
PATHLINE = re.compile(r'^(.*?\.(?:md|py|json|txt|ya?ml))(?::\s*(\d+(?:\s*[-–,]\s*\d+)*))?$')
EXTERNAL_WATCH = [
 "Harley","Woodward","Power of Maps","Monmonier","Jacob","Ptolemy","Campbell",
 "Edson","Kain","Baigent","Mundy","Boone","Pickles","Buisseret","Snyder","Dilke",
 "al-Idrisi","Ortelius","Mercator","Peutinger","Antonine","Wheatley","Needham",
 "Horowitz","Russell","Egeria","Petrarch","Ibn Jubayr","Ibn Baṭṭūṭa","Rykwert",
 "Kostof","Steinhardt","Smith, J.Z.","J.Z. Smith","J. Z. Smith",
]

def git_lines(commit, path):
    r = subprocess.run(["git","show",f"{commit}:{path}"],capture_output=True,text=True)
    return r.stdout.splitlines() if r.returncode == 0 else None

def worktree_lines(path):
    try: return open(path,encoding="utf-8").read().splitlines()
    except (FileNotFoundError, IsADirectoryError, UnicodeDecodeError): return None

def build_indices():
    corpus, reports = {}, {}
    for root, idx in (("corpus/knowledge", corpus), ("reports", reports)):
        for dp,_,fs in os.walk(root):
            for f in fs:
                if f.endswith((".md",".json")):
                    idx.setdefault(f,[]).append(os.path.join(dp,f))
    return corpus, reports

CORPUS_IDX, REPORTS_IDX = build_indices()

def resolve(raw, last_resolved, in_report):
    p = raw.strip().rstrip('.,;')
    base = os.path.basename(p)
    cands = []
    if p.startswith(("corpus/","reports/","tools/","templates/","examples/")):
        cands = [p]
    elif p == "README.md":
        cands = ["corpus/README.md","README.md"]
    elif base == "claims.json" and in_report:
        cands = [os.path.join(os.path.dirname(in_report), base)]
    elif p.startswith("../"):
        cands = [os.path.normpath(os.path.join("corpus/knowledge/culture-material", p)),
                 os.path.normpath(os.path.join("corpus/knowledge", p))]
    elif "/" in p:
        cands = [os.path.join("corpus/knowledge", p), p, os.path.join("reports", p)]
    else:
        allc = list(CORPUS_IDX.get(base,[])) + list(REPORTS_IDX.get(base,[]))
        if os.path.isfile(p) and not os.path.isdir(p) and base not in CORPUS_IDX:
            cands = [p]
        elif len(CORPUS_IDX.get(base,[])) == 1:
            cands = list(CORPUS_IDX[base])
        elif len(allc) == 1:
            cands = allc
        elif last_resolved and os.path.isfile(os.path.join(os.path.dirname(last_resolved), base)):
            cands = [os.path.join(os.path.dirname(last_resolved), base)]
        else:
            cands = allc
    seen=[]; cands=[c for c in cands if c not in seen and not seen.append(c)]
    exist=[c for c in cands if os.path.isfile(c)]
    if len(exist) == 1: return exist[0], "unique"
    if len(exist) > 1: return None, "AMBIGUOUS: " + " | ".join(exist[:3])
    if cands: return None, "MISSING (proposed/absent): " + cands[0]
    return None, "MISSING"

def parse_linespec(spec):
    out=[]
    for part in re.split(r',', spec.replace('–','-')):
        part=part.strip()
        if '-' in part:
            a,b=part.split('-',1); out.extend(range(int(a),int(b)+1))
        else: out.append(int(part))
    return out

def audit(md_path, commit=None):
    text=open(md_path,encoding="utf-8").read()
    L=text.splitlines()
    raw=[]
    for i,line in enumerate(L,1):
        if line.strip().startswith('```'): continue
        for m in CITE_RE.finditer(line):
            tok=m.group(1).strip()
            if tok.startswith(("http://","https://","www.")): continue
            if "*" in tok or tok.startswith("$ "): continue
            for pref in ("ls ","find ","grep ","cat ","python3 ","sha256sum ","python3 -B ","-B "):
                if tok.startswith(pref): tok=tok[len(pref):].strip()
            raw.append((i,tok,line))
    results=[]; last=None
    for i,tok,line in raw:
        ls=LINESPEC.match(tok)
        if ls:
            rec={"draft_line":i,"raw":tok,"path":last,"spec":ls.group(1),"resolved":last,
                 "resolution":"(continuation; no prior resolved path)" if not last else "continuation",
                 "ok":bool(last),"line_status":[]}
            if last and os.path.isfile(last):
                LLP=git_lines(commit,last) if commit else worktree_lines(last)
                if LLP is None: LLP=worktree_lines(last); rec["resolution"]+="; worktree (not at baseline)"
                if LLP is not None:
                    for n in parse_linespec(ls.group(1)):
                        multi = ("-" in ls.group(1) or "–" in ls.group(1) or "," in ls.group(1))
                        if 1<=n<=len(LLP):
                            blank=not LLP[n-1].strip()
                            st="blank-in-range" if (blank and multi) else ("BLANK" if blank else "ok")
                            rec["line_status"].append({"spec":str(n),"status":st,"excerpt":LLP[n-1][:120]})
                            if st=="BLANK": rec["ok"]=False
                        else:
                            rec["line_status"].append({"spec":str(n),"status":"OUT-OF-RANGE"}); rec["ok"]=False
            results.append(rec); continue
        pm=PATHLINE.match(tok)
        if not pm: continue
        p,spec=pm.group(1),pm.group(2)
        if not (p.endswith(('.md','.py','.json','.txt','.yml','.yaml')) and ('/' in p or '.' in p)): continue
        full,how=resolve(p,last,None)
        rec={"draft_line":i,"raw":tok,"path":p,"spec":spec,"resolved":full,"resolution":how,"line_status":[]}
        if full: last=full
        rec["ok"]=True
        if not full:
            rec["ok"]=False
        else:
            LLP = git_lines(commit,full) if commit else worktree_lines(full)
            if LLP is None and commit:
                LLP = worktree_lines(full)
                if LLP is not None:
                    rec["resolution"] = (rec["resolution"] or "") + "; worktree (untracked at baseline)"
            if LLP is None:
                rec["ok"]=False; rec["line_status"].append({"spec":"-","status":f"MISSING AT {commit or 'worktree'}"})
            else:
                rec["file_lines"]=len(LLP)
                if not spec:
                    rec["line_status"].append({"spec":"(none)","status":"file resolves; no line asserted"})
                else:
                    multi = ("-" in spec or "–" in spec or "," in spec)
                    for n in parse_linespec(spec):
                        if 1 <= n <= len(LLP):
                            blank = not LLP[n-1].strip()
                            st = "blank-in-range" if (blank and multi) else ("BLANK" if blank else "ok")
                            rec["line_status"].append({"spec":str(n),"status":st,"excerpt":LLP[n-1][:170]})
                            if st == "BLANK": rec["ok"]=False
                        else:
                            rec["line_status"].append({"spec":str(n),"status":f"OUT-OF-RANGE (file {len(LLP)})"})
                            rec["ok"]=False
        results.append(rec)
    src_lo=src_hi=None
    for i,line in enumerate(L,1):
        if re.match(r'^- sources:',line): src_lo=i
        elif src_lo and re.match(r'^- (couples|source|verified-at|recheck|scope):',line):
            src_hi=i; break
    block="\n".join(L[(src_lo-1):(src_hi-1)]) if src_lo else ""
    blanket = any(m in block.lower() for m in ("not consulted this round","not re-fetched in this seat",
                                               "no network at this","no network at seat time",
                                               "every item below is `(to-verify)`"))
    ext=[]
    for i,line in enumerate(L,1):
        if line.strip().startswith('```'): continue
        hits=[w for w in EXTERNAL_WATCH if w in line]
        if not hits: continue
        in_src = bool(src_lo and (src_hi is None or src_lo <= i < src_hi))
        tv = ("to-verify" in line) or ("not consulted" in line.lower()) or ("not inspected" in line.lower())
        status = "to-verify-inline" if tv else ("covered-by-sources-blanket" if (in_src and blanket) else
                 ("in-sources-no-marker" if in_src else "body-no-marker"))
        ext.append({"draft_line":i,"watch":hits,"status":status,"excerpt":line[:200]})
    import hashlib
    digests=[]
    for i,line in enumerate(L,1):
        for m in re.finditer(r'([A-Za-z0-9_./-]+\.md)[^\n]*?sha256\s*`?([0-9a-f]{64})`?', line):
            path,claimed=m.group(1),m.group(2)
            full,how=resolve(path,None,None)
            if not full:
                digests.append({"draft_line":i,"path":path,"status":"UNRESOLVED"}); continue
            if commit:
                r=subprocess.run(["git","show",f"{commit}:{full}"],capture_output=True)
                data=r.stdout if r.returncode==0 else b""
            else:
                data=open(full,"rb").read()
            actual=hashlib.sha256(data).hexdigest()
            digests.append({"draft_line":i,"path":full,"claimed":claimed,"actual":actual,
                            "status":"match" if actual==claimed else "MISMATCH"})
    ids=re.findall(r'\bKTD-[A-Z]+-S-\d{4}\b', text)
    defined=set(re.findall(r'\b(KTD-[A-Z]+-S-\d{4})\b\s*—', text))
    ktd={"ids":sorted(set(ids)),"defined":sorted(defined),
         "unresolved":sorted(set(ids)-defined)}
    return results, ext, {"sources_block":[src_lo,src_hi],"blanket":blanket,
                          "digests":digests,"ktd":ktd}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("draft"); ap.add_argument("--commit"); ap.add_argument("--json")
    ap.add_argument("--allow-absent", default="", help="comma-separated basenames expected absent (proposed landings)")
    a=ap.parse_args()
    if not os.path.isfile(a.draft):
        print(f"MALFORMED: no such draft {a.draft}"); sys.exit(2)
    res,ext,meta=audit(a.draft,a.commit)
    allow={x.strip() for x in a.allow_absent.split(",") if x.strip()}
    for r in res:
        if not r.get("ok") and r.get("resolution","").startswith("MISSING") and os.path.basename(r.get("path","")) in allow:
            r["ok"]=True; r["resolution"]="PROPOSED-ABSENT (allowed): "+r["resolution"]
    bad=[r for r in res if not r.get("ok", True)]
    bad += [d for d in meta.get("digests",[]) if d["status"]!="match"]
    bad += [{"raw":u,"ok":False,"resolution":"unresolved KTD id"} for u in meta.get("ktd",{}).get("unresolved",[])]
    print(f"DRAFT {a.draft}  commit={a.commit or 'worktree'}")
    print(f"citations={len(res)}  hard_bad={len(bad)}  sources_block={meta['sources_block']}  blanket={meta['blanket']}")
    for r in res:
        mark="OK " if r["ok"] else "BAD"
        st="; ".join(f"{s['spec']}:{s['status']}" for s in r["line_status"])
        print(f"{mark} draft:{r['draft_line']:<4} {r['raw']:<48} -> {r['resolved'] or r['resolution']} [{st}]")
    counts={}
    for e in ext: counts[e["status"]]=counts.get(e["status"],0)+1
    print(f"\nexternal-source lines={len(ext)}  status={counts}")
    if meta.get("digests"):
        for d in meta["digests"]: print(f"  DIGEST draft:{d['draft_line']} {d.get('path')} -> {d['status']}")
    if meta.get("ktd") and meta["ktd"]["ids"]:
        print(f"  KTD ids={len(meta['ktd']['ids'])} defined={len(meta['ktd']['defined'])} unresolved={meta['ktd']['unresolved']}")
    for e in ext:
        if e["status"] in ("body-no-marker","in-sources-no-marker"):
            print(f"  EXT-UNMARKED draft:{e['draft_line']} {e['watch']} | {e['excerpt']}")
    if a.json: json.dump({"citations":res,"external":ext,"meta":meta},open(a.json,"w"),indent=1)
    sys.exit(0 if not bad else 1)
````

## Appendix B — command transcript (trimmed)

All commands ran from the lane root on 2026-10-19 with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/

# seed audit
$ python3 -B .scratch/c06/audit.py reports/round-44/scout/K02-gap-scout.md \
    --allow-absent cartography-and-mapmaking.md,dream-vision-trance.md
DRAFT reports/round-44/scout/K02-gap-scout.md  commit=worktree
citations=137  hard_bad=4
  BAD K02:204  README.md                          -> AMBIGUOUS: corpus/README.md | README.md
  BAD K02:243  cosmography-cosmography.md:102     -> MISSING
  BAD K02:375  C01-entry-draft.md:9               -> BLANK
  BAD K02:376  C05-collision.md:10                -> BLANK
# unique raw paths 58; unique resolved 52; unique path:spec 63

# per-fragment
$ python3 -B .scratch/c06/audit.py reports/round-47/cov/C01-entry-a.md --commit 6e9a30d ...
citations=87   hard_bad=2   # both in seat-report sections, not the fenced body
$ python3 -B .scratch/c06/audit.py reports/round-47/cov/C02-entry-b.md --commit 6e9a30d ...
citations=122  hard_bad=0
$ python3 -B .scratch/c06/audit.py reports/round-47/cov/C03-entry-c.md --commit 6e9a30d ...
citations=74   hard_bad=0
$ python3 -B .scratch/c06/audit.py reports/round-47/cov/C04-entry-header.md --commit 6e9a30d ...
citations=149  hard_bad=1   # bare `sweep.py` ambiguous, self-audit section only
  DIGEST ... x9 -> match

# assembly (head + C01 + C02 + C03 fences)
$ python3 -B .scratch/c06/audit.py .scratch/c06/assembly.md --commit 6e9a30d \
    --allow-absent cartography-and-mapmaking.md
DRAFT .scratch/c06/assembly.md  commit=6e9a30d
citations=226  hard_bad=0  sources_block=[5, 47]  blanket=True
external-source lines=53  status={'to-verify-inline': 49, 'body-no-marker': 4}
DIGEST ... x9 -> match
# unique files 38; unique path:spec 50; corpus files 33; (to-verify) 41

# section/cross-reference
$ grep -n '^## ' .scratch/c06/assembly.md | wc -l
15
$ grep -n '§\s*[0-9]' .scratch/c06/assembly.md      # all §1-§15 exist; no dangling
# semantic mismatch found: 'names the form (§2)' and 'the typology in §2' -> §4.1

# topic byte-equality
$ python3 - <<'PY'
seed = open('reports/round-44/scout/K02-gap-scout.md').read().splitlines()[226]
topic = [l for l in open('.scratch/c06/assembly.md') if l.startswith('- topic:')][0]
print(len(seed), len(topic), seed == topic)
PY
775 775 True

# couples
# 21 tokens extracted from the '- couples:' line; 21/21 resolve from corpus/knowledge/culture-material/

# digests (independent sha256sum)
$ sha256sum <the nine pinned files>   # 9/9 equal the head-block values

# needle re-check (29 assertions: C04's 23 + C03's additional)
needle failures: 0 / 29

# seed and assembly identity
$ sha256sum reports/round-44/scout/K02-gap-scout.md .scratch/c06/assembly.md
a72fff27ee193cc12e689b5a3b485d3c0389bd4317b7810abf745ee441f335f6  reports/round-44/scout/K02-gap-scout.md
2422ca96c2fab0385b1e6f89a8faa4f72134c59cde5522d9d498720b149b0942  .scratch/c06/assembly.md
```

---

### One-line handoff

**C06 PASS:** the assembled cartography entry is source-clean (226 citation records, 0 hard failures, 9/9 digests, 21/21 couples, topic byte-equal); apply after correcting the two `§2`→`§4.1` form references, the "six load-bearing anchors" count (nine are pinned), and explicitly dispositioning C02 §9 (not in the r44 seed's outline).
