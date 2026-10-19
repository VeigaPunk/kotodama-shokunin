# S01 — round-47 integration draft: one fresh coverage entry, one pre-dispatch gate, one loop-1 ledger

- Seat: `S01` | role: scribe | claim: cross | date 2026-10-19
- Out path: `reports/round-47/scribe/S01-integration-draft.md` (this file only)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`) — equals `reports/round-47/claims.json:7`; `git rev-parse HEAD` at every measurement below
- Contract: `reports/round-47/claims.json` sha256 `7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34`; `reports/round-47/targets.json` sha256 `d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d`
- Cut: **2026-10-19T18:00Z**. This is a mid-wave draft, not a close. The wave census and every absent artifact are stated in §8; absence is `could-not-evaluate`, never green.
- Boundary: this seat wrote zero bytes outside this file. All probes were read-only or lived under disposable `.scratch/`. No filed byte was edited, no corpus byte was staged, no `reports/round-*/run-validation.py` was executed anywhere, and no git/network/install action was taken.

**Status in one line (updated at 18:06Z):** the baseline and all three premises reproduce, and the evidence chains are now largely filed — C has the four draft fragments plus C08/C09/C10/C13 and the audits, O has the core draft plus the r43 demo, the negative control and three verifier reports, Ca has Ca01–Ca06 — but **no claim's `after_required` is met**: there is still no assembled C entry, no README edit applied, no durable O tool, and no filed Ca successor artifact. The honest per-axis status is therefore `could-not-evaluate` (deliverable) with `unchanged` as the measured fallback. The apply order and abort rules are in §6.

---

## §0 — The headline the integrator must read first

1. **The baseline is exact and undrifted.** HEAD = declared baseline = `6e9a30d`; `claims.json` and `targets.json` match the digests pinned in `telemetry/dispatch-declared.json`; corpus = **223** (`25/26/25/29/24/94`); `corpus/README.md` = revision **2.4**, sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`; the r28 sweep exits 0 at `rows 223 files 223`. X05 independently confirms no commit drift, no digest drift, and no ref rewind (`cross/X05-baseline-drift.md` §1).
2. **Claim C's gap is fresh at HEAD, with one wording caveat.** K01, K02, C05 and X00 independently measure **0 filename owners, 0 topic-line owners, 0 header/title owners**, slug absent, sort slot between `calendar-festival-systems.md` and `costume-semiotics.md`. There is **0 prior-round *claim* proposal** and **1 prior-round *scout* naming** — the r44 K02 seed itself; cartography was never drafted or landed (r44 `validation.json:9`). The claim's literal "0 prior-round proposals" is true only relative to r44 K02; the round record should name that provenance precisely (K01 §6.3, X00 §7.1).
3. **The C entry is drafted in four fenced fragments, audited in part, and not yet assembled.** C04 supplies the head block; C01 drafts §§1–4; C02 drafts §§5–9; C03 drafts §§10–15. The seed's ten-section outline is covered, but the assembled entry must **de-duplicate** C01 §3's mechanisms against C02 §5's chain (both treat projection, scale and symbolization); X04 measures the assembled drafts at **800 body lines against a partition norm of 103–221** and calls the volume inflated. C08's boundary audit PASSes ownership (no second owner; divination is not a collision) but lists four missing adjacency rows (craft-artisan, trade-economy, celestial-symbolism, sacred-kingship), one wrong anchor (`craft-artisan-lexicon.md:44` is steel grading; the guild ladder is `:56-63`), and the need to answer `cosmology-cosmography.md:27`'s "cosmography … how the world is drawn (maps)" definition as content-vs-production. X04 also finds C04's `- gap filled:` says "2 files / 3 lines" for `cartograph`, while the measured count is **2 lines** (F-11, F-12). The r47 C01–C03 mission text in `targets.json:21-23` is derived from the **r42 lithic** skeleton ("container-name fossil", "material/trade classes"), not the cartography seed; K02 §9 flags this, and the drafters recovered cartography-specific content (C02 §9 is the *mappa/charta* word bank).
4. **The README arithmetic is fixed, the draft is filed, and the defect is real.** C09's fenced diff uses culture-material `25 → 26`, total `223 → 224`, footer vector `25/26/25/29/24/94 → 25/26/26/29/24/94` (sum **224**), repairs the rev-2.4 prose vector at `corpus/README.md:11` (whose declared post-vector `25/23/26/25/24/94` sums **217**), and builds the row from the entry's `- topic:`. C10's staged 224 tree measures `rows 224 files 224`, `topic_mismatch 0`, `footer_ok True`, exit 0 — and its control D proves the sweep **cannot** see the prose-vector repair, so both checks are required. **C05 writes the vector wrong in three places** (`26/26/25/29/24/94`); do not copy those literals (§9, F-01).
5. **Claim O's target does not exist yet, but the tool is now drafted and the failure modes are measured.** `tools/harness/claims-freshness.py` is absent at HEAD. O01 supplies the 633-line core (sha256 `72c294f2…`); O05 supplies the r43 demo (`O STALE`, `C STALE`, `Ca FRESH`, reference exit 1); O06 supplies the true-`before` negative control (3 fresh, exit 0). O10, O09 and O13 measure the r44 prototype's failures: inverted exit codes, false STALE on the llama phrasing, missing polarity handling, and a probe registry with no coverage. The r43 regression itself is measured by three independent seats at `7ceff59`: extractor present (`d8d23a26…`, selftest 8/8, wrapped 4/4), `mineral-stone-symbolism.md` present (`c99f44ca…`), `reports/round-43/calib/` absent → **r43 O STALE, r43 C STALE, r43 Ca FRESH** (Ca01 §2, X00 §2, P01 §2).
6. **The gate must not claim r44 as a stale catch.** Ca01 §3 measures r44's `before` fields as **true** at `c9f4eaa` (the four-class authority was still a draft; no ownership/absence assertion; no freshness tool). r44's C defect was a **carried candidate in the claim body**, one class over; r44 Ca was a **delivery** failure. The r47 O `before` uses the broad grouping ("r43 and r44 both declared claims on stale premises"); that sentence is `to-verify` and must not become a false selectivity claim. X00 §7.2 reaches the same conclusion independently.
7. **Claim Ca's successor is assembled as 3 defect rows + 2 provider amendments, covering 6 items.** Ca01, Ca02, Ca03 and Ca04 have filed rows; Ca06 assembles them into a fenced `kotodama-defect-queue-successor-v1` object with the parent pinned at `dfc9265d…` and the two provider amendments kept outside `rows[]` as `named-deviation` records. The first two retrospective bullets are folded into one row by design, so the artifact has **5 records for 6 items**; the claim's literal "one row per loop-1 carried item" and Ca06's 3+2 shape need R05/Ca07 to confirm (F-14). Ca07 (integrity) is absent at this cut.
8. **No axis is harmed at this cut; no axis is improved yet.** The only honest verdicts are branches (§5). A green number produced on the wrong tree (224 rows over a carried/duplicated topic, a 223 census re-run after C, a gate green on a worktree read, a queue row classed fixed without a re-run) is the failure mode each branch exists to make red.

---

## §1 — Window, pins, and "first-hand" in this draft

| pin | value | command / source |
|---|---|---|
| lane HEAD / declared baseline | `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` / `6e9a30d` | `git rev-parse HEAD`; `claims.json:7` |
| working tree | only untracked `reports/round-46/review/` and `reports/round-47/`; no tracked modification | `git status --porcelain` |
| corpus total | **223** | `find corpus/knowledge -name '*.md' \| wc -l` |
| partition vector | `linguistics 25 / myth-symbol 26 / culture-material 25 / synthesis 29 / verification 24 / civilizations 94` | per-directory `ls \| wc -l`; sum 223 |
| corpus README | revision **2.4**; totals `:544` = 223; footer `:548` = `25/26/25/29/24/94`; sha256 `7c788a1d…cdcd` | `grep -n '^revision:'`; `sed -n '544,550p'`; `sha256sum` |
| sweep | exit 0; `rows 223 files 223`; `missing 0`; `topic_mismatch 0`; `orphan_rows 0`; `header_drift {}`; `totals_ok True`; `footer_ok True` | `python3 -B reports/round-28/readme/sweep.py` |
| cartography target | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` **absent**; 0 filename owners | `test -e`; `find … -iname '*cartograph*' -o …` |
| freshness tool | **absent** — `tools/harness/claims-freshness.py` does not exist | `ls` |
| r42 witness | sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`; selftest 8/8 | `sha256sum`; `--selftest` (Ca01 §2.4) |
| r44 resolver | sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`; selftest 27/27 | `sha256sum`; `--selftest` (Ca02 §1) |
| parent defect queue | sha256 `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` | `sha256sum reports/round-40/op/defect-queue-v2.json` |
| r43 successor queue | sha256 `77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38` | `sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json` |
| r43 baseline | `7ceff59a0216a8ea21ee43262d9fc72abf770cee` | `git rev-parse 7ceff59`; O10 §4.2 |
| r47 contract digests | claims `7eb16979…1fa34`; targets `d60e5572…9ca3d` | `sha256sum`; `telemetry/dispatch-declared.json` |

"First-hand" means opened or executed by this seat in the window above. Sibling figures are attributed where they appear; I re-derived the corpus census, the README state, the sweep, the cartography ownership probes, the r43 baseline probes, the queue digests and the C04 couples-token count. Where sibling seats disagree, both readings are printed (F-01, F-09).

---

## §2 — Claim C (coverage): the cartography entry

### 2.1 The claim and its measured precondition

`claims.json:26` requires: one entry at the verified-fresh cartography gap; total **223 → 224**; culture-material **25 → 26**; README rev 2.5 with the row in filename order **and** the rev-2.4 prose-vector defect repaired; audits PASS; zero overwrites; freshness re-verified at landing. The `before` is `total 223; cartography is a verified-fresh unowned gap (K02-r44: no owner, no prior proposal, not carried)`.

Measured at `6e9a30d` (this seat; agreeing with K01, K02, C05, X00):

| test | measurement | reading |
|---|---|---|
| filename owners | `find` over `*cartograph*`, `*mapmaking*`, `*portolan*`, `*cadastr*` → **0** | no filename owner |
| exact slug | `cartography-and-mapmaking.md` absent from worktree, index and HEAD | new file (`A`), not `M` |
| topic-line owners | wide pattern → 11 hits (K01/C05/X00) or 13 (C01/C07, wider `chart`/`lienzo` pattern) — **all metaphor, verb, or adjacent register** | 0 owners; the count is pattern-dependent, the ownership verdict is not (F-09) |
| header fields (`gap`/`gap filled`/`scope`/`couples`) | 0 hits for the cartography vocabulary | no hidden owner |
| H1 titles | 2 dialect/lect titles, 0 cartography | no title owner |
| genuine footprint | **7 files / 9 lines**, all by-product or explicit handoff (`cosmology-cosmography.md:71,:102`; `mesoamerica-primary-sources.md:58`; `architecture-settlement-lexicon.md:95`; `direction-symbolism.md:26`; `japan-medieval-sengoku.md:157`; `polynesia-navigation.md:52-74`; `timekeeping-instruments.md:50`) | named-but-unbuilt register; low raw demand, stated honestly |
| prior-round claim proposals | **0** | fresh in the claim sense |
| prior-round scout naming | **1** — r44 K02, the cited seed; never drafted or landed | provenance caveat, not a carriage defect |

The load-bearing citation is the partition's own disclaimer: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` — "T-O diagrams are symbolic, **not survey maps**" — and `:102` — "not cartographic". The partition owns symbolic world diagrams and explicitly leaves the survey sheet unowned. That is the same "named but unbuilt" shape as the r42 lithic gap, but here the disclaimer is explicit rather than inferred.

### 2.2 The drafted entry: four fenced fragments and the seed's ten sections

| seed § | content | drafted in | status |
|---|---|---|---|
| 1 | the map's question; the question fixes the form | C01 §1 | filed |
| 2 | map-form typology (8 forms) | C01 §4 | filed |
| 3 | the survey chain | C02 §5 (seven links) | filed |
| 4 | projection and scale | C01 §3.2–3.3 + C02 §5.4–5.5 | filed twice — de-duplicate |
| 5 | drawing and symbolization | C01 §3.4–3.5 + C02 §5.6 | filed twice — de-duplicate |
| 6 | reproduction and the map trade | C02 §5.7, §7 | filed |
| 7 | the map's silences | C01 §3.1, C02 §8.4 | filed |
| 8 | calibration bank | C03 §12 (13 rows + timestamps/posture) | filed |
| 9 | build order | C03 §10 (nine steps) | filed |
| 10 | decision record + NON-CANON worked example | C03 §11, §13 (`DR-CT-01..12`) | filed |

**Assembly rule.** Head block first (C04 §2), then C01 §§1–4, C02 §§5–9, C03 §§10–15. The integrator must (a) remove the duplicate definitions of projection/scale/symbolization between C01 §3 and C02 §5, keeping one authoritative treatment and cross-references — X04 measures the four fragments at **800 body lines** against a partition norm of 103–221, so assembly must cut, not concatenate; (b) renumber if the assembled body's `§` references no longer match; (c) keep the `- topic:` line as one physical line (sweep's `TOPIC_RE` stops at the next `- word` line); (d) ensure the README row is generated from the **landed** entry's `- topic:`, not from memory (C07 F1, C09 §4, C10 §6); (e) fix C08's P1 boundary-table gaps before filing — add rows for `craft-artisan-lexicon.md` (workshop ladder `:3,:56-63`, marks `:76-87`; `:44` is steel grading, not the ladder), `trade-economy-lexicon.md`, `celestial-symbolism-calendars.md` and `sacred-kingship-mythic-charter.md`, and reword the cosmology row to answer `cosmology-cosmography.md:27` ("how the world is drawn (maps)") as **content** (the world model's drawn form) versus **production** (the new entry's survey→sheet chain); (f) correct C04's `- gap filled:` count: it says `cartograph` is "2 files / 3 lines", but the measured count at `6e9a30d` is **2 files / 2 lines** (`cosmology-cosmography.md:102`; `mesoamerica-primary-sources.md:58`).

**Content checks already filed:** C07 audits the contract at a pre-draft cut and honestly returns `could-not-evaluate` for Q1–Q5 as delivered; its structural legs PASS (path, partition, sort, one-owner, neighbour resolution, README arithmetic). C08 PASSes ownership but files the P1 boundary fixes above; its verdict is "no second owner, divination is not a collision". C13 PASSes all **21/21** `- couples:` tokens (line sha256 `cf59ba1f…`), all Tier-1 direct, and predicts a delta of exactly `+1 entry, +21 refs, +21 direct`. X04 judges the gap real and the method substantive but the assembly volume-inflated. The integrator must re-run C07's §7 script and C08's B1–B15 checklist on the assembled bytes; a pre-draft structural PASS is not a content PASS.

### 2.3 README rev 2.5 — exact anchors, arithmetic, and the staged proof

| line | current | required |
|---|---|---|
| `corpus/README.md:5` | `revision: 2.4 — Round-42 myth-symbol expansion …` | prepend a rev 2.5 block naming the r47 cartography landing |
| `:11` | "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**" (sum **217**) | repair the post-arrow vector to `25/26/25/29/24/94` (sum 223) in the rev-2.4 block; the rev-2.5 note must use `25/26/26/29/24/94` (sum 224) |
| `:234` | `## culture-material/ (25)` | `## culture-material/ (26)` |
| `:240-241` | calendar row, then costume row | insert one row between them, filename order: `- \`cartography-and-mapmaking.md\` — <entry topic byte-equal>` |
| `:544` | `Total knowledge entries: 223.` | `Total knowledge entries: 224.` |
| `:548` | `(total 223 files; directory totals 25/26/25/29/24/94)` | `(total 224 files; directory totals 25/26/26/29/24/94)` |

Arithmetic, computed not copied: `25+23+26+25+24+94 = 217`; `25+26+25+29+24+94 = 223`; `25+26+26+29+24+94 = 224`. The slot order is fixed: `linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`.

**C10's staged proof (a fixture tree under `.scratch`, never landed):** after six exactly-once transforms, the filed sweep reads `parts {…culture-material 26…}`, `rows 224 files 224`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_line 224`, footer `[25,26,26,29,24,94]`, `footer_ok True`, exit 0. Its control matrix proves the green is not trivial: a stale footer, a paraphrased row, a stale section header, a bad order and a bad manifest each fail. **Control D is the important negative:** leaving the rev-2.4 prose vector unrepaired still yields `ok True` — the sweep does not read revision-note vectors. Claim C's threshold names both the sweep and the prose repair, so the integrator needs C10 §5's scoped vector check in addition to the sweep.

**Do not copy C05's vector literals.** `cov/C05-freshness.md:273,275,295` says the post-landing vector is `26/26/25/29/24/94`. That sums 224 but puts the +1 in linguistics instead of culture-material; the correct vector, used by K02, C04, C07, C10 and P01, is `25/26/26/29/24/94`. This is a transcription defect in a freshness-verification fragment; it does not affect C05's ownership verdict (F-01).

### 2.4 Post-landing census delta (informational, not a claim threshold)

C04's `- couples:` line carries **21 distinct `.md` tokens**, all direct, all resolving from `corpus/knowledge/culture-material/` (C04 §4.3). C13 independently verifies **21/21** resolution at Tier-1 direct, pins the field line at sha256 `cf59ba1f311619dbe527bfb1d3c716ae338f56d601af675e52e343384e9f5663` (4,096 chars), and predicts the delta as exactly `+1 entry, +21 refs, +21 direct`. If the assembled entry keeps the line unchanged, the r44 resolver's next census would measure `entries=224`, `refs=2730+21=2751`, `direct=2557`, with the other classes unchanged. **This is still a prediction, not a measurement:** C02's body may add or remove tokens, and no artifact in this round requires the census. Measure after apply; do not assert 2751 as a landed number.

### 2.5 Evidence chain and what is absent

| artifact | role | at this cut |
|---|---|---|
| `scout/K01-gap-recheck.md` | landing-time freshness, prior-proposal audit | **filed** |
| `scout/K02-seed-extract.md` | seed extraction + entry contract + mission-mismatch finding | **filed** |
| `cov/C01-entry-a.md` | §§1–4 draft | **filed** |
| `cov/C02-entry-b.md` | §§5–9 draft | **filed** |
| `cov/C03-entry-c.md` | §§10–15 draft | **filed** |
| `cov/C04-entry-header.md` | head block | **filed** (gap-filled line-count defect F-12) |
| `cov/C05-freshness.md` | independent freshness re-verify | **filed** (vector defect F-01) |
| `cov/C07-contract-audit.md` | QUALITY + convention audit | **filed pre-draft**; must be re-run on assembled bytes |
| `cov/C08-boundary.md` | seven-neighbour boundary audit | **filed**; PASS ownership, P1 table fixes owed |
| `cov/C09-readme.md` | README rev 2.5 fenced diff | **filed**; vector correct, row from `- topic:` |
| `cov/C10-sweep.md` | staged 224 sweep | **filed** (fixture, not the entry) |
| `cov/C13-couples.md` | couples resolution + census delta | **filed**; 21/21 |
| `cov/V01-post-landing.md` | post-landing verification | **pre-landing / could-not-evaluate**, with a staged proof; live check owed |
| `plan/P02-c-plan.md` | C planner | **filed** |
| `cov/C06-source-audit.md`, `C11-scribe.md`, `C12-shelf.md`, `C14-example.md`, `W02-landing-spec.md` | source audit, scribe, shelf, example, landing spec | **absent** |

### 2.6 Verdict candidate (C)

- **`improved`** only if one assembled entry lands at the exact path as `A`; the total is 224 and culture-material 26; the README rev 2.5 edit is a single change with the row byte-equal to the landed `- topic:`; the footer vector is `25/26/26/29/24/94`; the rev-2.4 prose vector is repaired; sweep is `rows 224 files 224`, exit 0; the scoped vector check is exit 0; the audits (C06/C07/C08/C12/C13/C14) PASS on the assembled bytes; and freshness is re-run at the apply HEAD.
- **`unprovable-but-better`** if drafts are complete and the staged proof is green but the landing is withheld (no assembled entry, no README edit). At this cut this is the C candidate.
- **`unchanged`** if no entry lands: the gap remains verified unowned; a scout plus drafts is not a coverage move.
- **`harmed`** if an existing entry is overwritten; if the README row is paraphrased or mis-ordered; if the total is 224 with a duplicated/carried topic; if the footer or the rev-2.4 prose vector is wrong; or if C05's wrong vector is copied into the file.

---

## §3 — Claim O (operability): the durable pre-dispatch freshness gate

### 3.1 The contract the tool must meet

`claims.json:39` requires a durable `tools/harness/claims-freshness.py` that re-derives each claim's `before` at its own `baseline_commit` via `git show`/`ls-tree` (never the worktree), with typed per-clause probes and declared polarity, flags a claim STALE if any clause contradicts its asserted `before`, exits non-zero on stale, and files a demonstration at `reports/round-47/calib/`. The minimum durable contract is R01-44 §4.3 (`reports/round-44/review/R01-review.md:243-250`), restated operationally by P01 §5.

| leg | requirement |
|---|---|
| input | `--claims <claims.json>` + `baseline_commit` from inside the file; **sidecar** `--checks <json>` for filed rounds whose claims may not be edited (P01 §5.2) |
| clause encoding | `{clause, clause_span/clause_text, probe_kind, target, expect, evidence_command}`; `expect` is the **measured state that makes the clause true**, never inferred from prose |
| probe set (closed) | `path_absent`, `path_present`, `grep_absent`, `grep_present`, `count_eq`, `sha256_eq`, `topic_owner_absent`, `capability_present` |
| baseline evaluation | `git ls-tree -r --name-only <sha>`, `git show <sha>:<path>`, `git grep <pat> <sha> -- <path>`; a missing blob yields `could-not-evaluate` for that clause, never a default |
| semantics | **STALE if any clause mismatches; FRESH only if all match; could-not-evaluate when no checks or an unmeasured clause and no mismatch** |
| exit codes | **0** all-fresh; **1** stale; **2** malformed (bad JSON, no `baseline_commit`, unknown probe, missing `expect`, sidecar digest mismatch); **3** could-not-evaluate (never 0) |
| determinism | no timestamps/random in the decision; same bytes → same verdict + exit |
| durability | under `tools/harness/`, stdlib only, no network, no writes to filed paths; a green selftest with the control count computed from the registry |

### 3.2 The r43 regression, measured independently

At the r43 declared baseline `7ceff59`:

| fact | measurement | source |
|---|---|---|
| durable extractor exists | `tools/harness/couples-reference-extractor.py`, sha256 `d8d23a26…d4679cf1`; selftest 8/8, exit 0 | Ca01 §2.4; X00 §2.2; P01 §2 |
| wrapped field reads whole | 4/4 tokens: `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md` | Ca01 §2.1; P01 §2 |
| lithic owner exists | `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, sha256 `c99f44ca…d99f`; topic line `:5` owns "the lithic register" | Ca01 §2.2 |
| counts true | myth-symbol **26**, total **223** | `git ls-tree` at `7ceff59` |
| r43 Ca premise true | `reports/round-43/calib/` absent from the commit | `git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/` → empty |

Verdicts the tool must reproduce: **r43 O STALE** (the durable instrument existed; the claim-named path was the trap), **r43 C STALE** (counts true, ownership false — the mixed-clause proof), **r43 Ca FRESH** (the in-file negative control). Exit **1** for the set. The prototype's earlier output was `O STALE (0/2)`, `C STALE (2/3)`, `Ca FRESH (1/1)`, exit 2; the durable tool's exit must be 1 for stale, not 2.

### 3.3 The r44 boundary — a true `before`, not a stale catch

Ca01 §3 and X00 §3 both measure r44's `before` fields at `c9f4eaa` as **true**: `no four-class census authority exists` (the authority was a draft, landed only by r44 O), `total 223` (no ownership assertion), `no mechanical pre-dispatch freshness check exists` (the tool is absent). r44's C failure was a **carried candidate in the claim body** — the dream entry proposed at `reports/round-42/scout/K02-myth-gaps.md:216` — which R02-44:441 explicitly rules outside R01-43-12. r44's Ca failure was delivery, not premise. Therefore:

- the gate run over r44 must report a true baseline and **must not** claim an r44 stale catch;
- the r47 O `before`'s broad grouping ("r43 and r44 both declared claims on stale premises") is a **to-verify** sentence; the round record should say "r43 narrow stale; r44 carried-candidate defect, adjacent class" (Ca01 §3; X00 §7.2);
- the anti-theater test must not be satisfied by a two-string lookup. The capability probe is what catches r43 O even when the literal path `tools/harness/basename-couples-resolver.py` is absent at baseline (X00 §2.2).

### 3.4 Control set and demonstrations the claim requires

P01 §5.6 gives an 18-row control matrix; the binding subset is: every probe kind exercised both matching and mismatching; a polarity control (flip `expect` → flip verdict); a baseline-not-worktree control (fixture present in worktree, absent at baseline → FRESH); could-not-evaluate (zero checks → exit 3); malformed shapes (4+ → exit 2 each); determinism (two runs identical); the r43 regression; a true-`before` negative control (r44 O/C/Ca at `c9f4eaa`, or a synthetic fresh claim); and the anti-theater mutation (rename r43 O's tool to the existing witness; replace C's literals with live values/synonyms; verdicts unchanged). The llama-herding novel-phrasing trap (R02-44:207-227) must **not** flag: the topic has no owner, so a correct `topic_owner_absent` clause is true.

**Exit-code warning from O10.** The r44 prototype emits the right r43 flags but the **wrong exit codes**: stale → 2, malformed → 1, and could-not-evaluate → 0 under `--allow-unverifiable` (`op/O10-exit-codes.md` §1). A durable tool that copies the prototype's numbering fails the claim's exit contract even with correct flags. O10's 14-control suite is the conformance check.

### 3.5 Evidence chain and what is absent

| artifact | role | at this cut |
|---|---|---|
| `scout/K03-gate-spec.md` | API/probe/exit spec | **filed** |
| `op/O01-tool-core.md` | tool core (633-line fenced head, sha256 `72c294f2…`) | **filed** |
| `op/O05-r43-demo.md` | r43 demo (reference evaluator: O/C STALE, Ca FRESH, exit 1) | **filed** |
| `op/O06-negative-control.md` | true-`before` negative (3 fresh, exit 0) | **filed** |
| `op/O09-traps.md`, `O10-exit-codes.md`, `O13-probe-coverage.md` | trap, exit-code, probe-coverage verifiers | **filed**; prototype fails all three |
| `op/O02-probe-registry.md`, `O03-verdict-contract.md`, `O04-selftest.md`, `O07-anti-theater.md` | tool parts 2/3, selftest, anti-theater | **absent** — the tool cannot be assembled without O02/O03 |
| `op/O08`, `O11`, `O12`, `O14`, `O15`, `V02`, `W01` | remaining verifiers, landing spec, scribe | **absent** |
| `plan/P03-o-plan.md` | O planner | **filed** |
| filed demonstration under `reports/round-47/calib/` | required by the claim | **absent** — the demos live in `op/`, not `calib/` |

### 3.6 Verdict candidate (O)

- **`improved`** only if the tool is durable at the claim path, its selftest is green with the registry-computed count, it flags r43 O and C STALE and Ca FRESH with exit 1, it leaves a true-`before` claim unflagged with exit 0, the anti-theater mutation preserves the verdicts, could-not-evaluate exits non-zero, malformed exits 2, and the demonstration and tool digest are filed.
- **`unprovable-but-better`** at this cut: the method is proven by three independent seats, the contract is executable, but the durable tool and the demonstration are absent. The prototype is red at 17/19 and exits wrong.
- **`unchanged`** if the tool remains a `.scratch` script or a prose checklist.
- **`harmed`** if it greens a stale claim, reds a true one (novel-phrasing false positive), consults the worktree for a verdict, lets could-not-evaluate exit 0, or claims an r44 stale catch.

---

## §4 — Claim Ca (calibration): the loop-1 ledger

### 4.1 The five retrospective bullets

`reports/round-46/loop-1-retrospective.md:43-53` carries:

1. the `R01-43-12`-class freshness gate — method proven at r44, no durable tool, owner integrator (`:45-46`);
2. the stale-premises pattern — r43 and r44 both hit it (`:47-48`);
3. the `basename-couples-resolver.py` latent edge — blank-separated hyphen soft-wrap drops tokens, **0 live incidence** (`:49-50`);
4. the antigravity lanes non-functional — positions 12/13 skipped or re-routed (`:51-52`);
5. zai usage exhausted — zai seats route to `openai-codex/gpt-6-luna-max` for the session (`:53`).

The r47 Ca claim adds the **two MANIFEST ledger schemas** as a sixth item. Ca03 §1 corrects the provenance: that item is **not** in the retrospective; it originates in the r46 Ca01 audit's schema note (`reports/round-46/audit/Ca01-manifest.md:7-8,28-32`) and the r46 receipt limits. That is a provenance correction, not a dropped item.

### 4.2 The assembled successor: 3 defect rows + 2 provider amendments

| record id (Ca06) | loop-1 item | class | owner | cited evidence |
|---|---|---|---|---|
| `r43-stale-premises` | R01-43-12 **and** the stale-premises pattern (the two retrospective bullets are folded into this row by design) | `routed-with-owner` (upgrades to `fixed-with-evidence` only if O lands and G1–G7 pass) | r47 O author + integrator | `reports/round-43/review/R01-review.md:400`; `reports/round-43/validation.json`; `reports/round-44/validation.json`; `reports/round-44/review/R01-review.md:243-250`; Ca01 §5 |
| `r44-resolver-hyphen-after-blank` | latent edge, 0 incidence | `recorded` | next resolver touch (tools/harness maintainer) | `reports/round-44/cross/X01-trades.md:26,114-155`; `reports/round-44/op/O03-defects-verify.md:221-229`; `tools/harness/basename-couples-resolver.py:55-59,73-74`; Ca02 §2 |
| `manifest-ledger-two-schema-evolution` | the two ledger schemas (r46-audit item, not a retrospective bullet) | `recorded` | integrator-of-record (fleet MANIFEST writer) | `reports/round-46/audit/Ca01-manifest.md:5-8,28-35`; `reports/round-46/validation.json` limits; Ca03 §6 |
| `PA-47-01-antigravity-lane-outage` | antigravity outage: position 12 re-routed and executed, position 13 skipped | `named-deviation` — **not** a defect row (`defect_row: false`) | operator (ruling) + integrator (re-route record) | `reports/round-46/loop-1-retrospective.md:51-52`; `reports/round-44/validation.json`; r47 telemetry |
| `PA-47-02-zai-exhaustion-luna-max` | zai exhaustion → luna-max | `named-deviation` — **not** a defect row | operator (exhaustion/substitute) + integrator (dispatch) | `reports/round-46/loop-1-retrospective.md:53`; `reports/round-43/claims.json` dispatch deviation; r47 telemetry |

**Ca06's assembly.** The fenced `kotodama-defect-queue-successor-v1` object pins the parent at `dfc9265d…` (re-measured after assembly), records `parent_bytes_edited: false`, pins the r43 predecessor at `77f9d63e…`, and carries `loop1_coverage` with `retro_carried_bullets: 5`, `retro_bullets_mapped: 5`, `additional_loop1_close_items: 1`, and a six-entry mapping. The first two retrospective bullets map to one row, so the artifact has **5 records for 6 items**; the provider amendments are kept outside `rows[]` to preserve the defect census (38 parent rows + 3 disposition rows). Its `not_requeued` list names r44 C (carried proposal, not stale premise), r44 Ca (same object as the gate's next touch), r42 lithic/r43 Ca (already dispositioned), and the r44 `reasoning_content` / r43 digest-drift findings (round telemetry). **Ca07 (integrity) is absent at this cut; R05/Ca07 must confirm that the claim's literal "one row per loop-1 carried item" is satisfied by this 3+2 shape** (F-14).

### 4.3 Classing rules that must survive assembly

- **`fixed-with-evidence` requires a command output and a landed artifact sha.** Neither Ca01 nor Ca02 nor Ca03 qualifies: the gate is absent, the resolver body may not be edited, and the schema split is not a defect. All three are `routed-with-owner` or `recorded`.
- **Provider amendments are deviations, not defects.** They carry `recorded (named deviation)` and a schedule/telemetry citation; they must not be counted in a defect rate.
- **The r44 instance is not a second narrow stale-premises row.** Ca01 records narrow incidence = r43 O + C (2 claims / 1 round); broad = adds r44 C (3 / 2). The successor should carry the distinction in `class_boundary` and must not double-count. P01's `L1-02` is the same class as `L1-01`, not a second fix target.
- **The parent may not be edited.** `reports/round-40/op/defect-queue-v2.json` stays at `dfc9265d…`; a mismatch is a stop condition, not a warning.

### 4.4 The successor artifact

Expected path: `reports/round-47/calib/queue-successor-r47.json` (or `.md` if the integrator prefers; the claim allows either). Required shape (P01 §6.3):

```
schema: kotodama-defect-queue-successor-v1
round: 47; date: 2026-10-19; baseline_commit: 6e9a30d
parent: reports/round-40/op/defect-queue-v2.json
parent_sha256_at_assembly: dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
prior_successor: {path: reports/round-43/calib/defect-queue-v2-successor-r43.json, sha256: 77f9d63e…}
class_vocabulary: {fixed-with-evidence, routed-with-owner, recorded, could-not-recover}
source_coverage: {retro_bullets: 5, audit_items: 1, rows: 6, dropped: []}
rows: [ six rows, each id/origin/class/owner/reason/next_touch/evidence/verification ]
application_gates: [G1..G6]
```

Acceptance: six rows, parent sha re-measured before and after, zero dropped, every row class in vocabulary, every owner non-empty, every evidence path real at `6e9a30d`, every `fixed` row with a re-run command output. Ca05/Ca07/R05 verify independently.

### 4.5 Verdict candidate (Ca)

- **`improved`** only if the queue-successor lands with all six rows, correct classes, real citations, the parent pinned and unchanged, and the `L1-01` route naming the actual O tool path (or explicitly naming its absence if O failed).
- **`unprovable-but-better`** at this cut: three rows and a verifier are filed; three are absent; no successor artifact exists. The calibration move is designed and partly evidenced, not delivered.
- **`unchanged`** if no successor lands.
- **`harmed`** if a carried item is dropped, the parent is edited, a provider deviation is classed as a defect, or a row is classed `fixed-with-evidence` without a re-run.

---

## §5 — Per-axis verdict candidates

| axis | candidate at this cut | improved requires | harmed if |
|---|---|---|---|
| **coverage** | `could-not-evaluate` (drafts + staged proof; no landing) / `unchanged` as measured | one assembled entry at the exact path as `A`; 224 total, 26 culture-material; README rev 2.5 with row byte-equal, totals 224, footer `25/26/26/29/24/94`, rev-2.4 prose repaired; sweep 224==224; scoped vector check exit 0; audits PASS on the assembled bytes; freshness re-run at apply | overwrite, duplicate/carried topic, mis-ordered or paraphrased row, wrong footer/vector, copied C05 literals |
| **operability** | `could-not-evaluate` (tool absent) / `unprovable-but-better` | durable tool; green selftest with computed count; r43 O/C stale + Ca fresh (exit 1); true-`before` control unflagged (exit 0); anti-theater still flags; C-N-E non-zero; malformed exit 2; demonstration + digest filed | two-string lookup, prose mining, worktree verdict, C-N-E exit 0, prototype's inverted exit codes, false positive on novel phrasing |
| **calibration** | `could-not-evaluate` (3/6 rows; no successor) / `unprovable-but-better` | six-row successor, parent pinned, zero dropped, classes correct, citations real, fixed rows re-run | dropped row, parent edit, provider deviation classed as defect, unfounded `fixed` |
| depth | unchanged | not claimed | — |
| adjacency | unchanged | not claimed; no packet/canon/lore surface | a scope bleed discovered in A01 |
| freshness | unchanged (paused) | not claimed; `freshness_pause_in_force: true` (`claims.json:21`) | a freshness claim or move |

No named non-author reviewer has yet judged the round at this cut (R01–R05, X01–X04, Q01 absent). The "unprovable-but-better only with a named non-author reviewer" condition is therefore **not** met; the candidates above are branches, not verdicts.

---

## §6 — Integrator apply order, exact checks, and do-not list

### 6.1 Order

1. **O first.** It is corpus-independent and its demos are baseline-pinned (`7ceff59`, `c9f4eaa`), so C's +1 cannot contaminate them. Apply the single tool file; run `--selftest`, the r43 demo, the negative control and the anti-theater test; file the demonstration and the tool digest. If O cannot flag r43 O/C without literal prose, O is `could-not-evaluate`, not improved — do not land.
2. **C second, atomically.** Assemble the entry (head + §§1–4 + §§5–9 + §§10–15), de-duplicate overlapping mechanism sections, then apply the entry and the README rev 2.5 edit in one change. Pre-landing checks: exact slug absent; total 223; culture-material 25; sort slot free; `- topic:` byte-equal to the README row; rev-2.4 prose repaired; footer vector `25/26/26/29/24/94`.
3. **Ca third.** Assemble the six-row successor after O's actual path/sha is known; if O did not land, `L1-01` remains `routed-with-owner` naming the absent path. Re-measure the parent sha before and after.
4. **Validate the committed close tree from an isolated copy.** Author `reports/round-47/run-validation.py` but execute it only inside a `git archive` copy under `.scratch/`, with live sentinels before/after (P01 §7.4; `reports/round-39/calib/isolation-replay-protocol.md` I1–I7). Never run a round runner in-tree.

### 6.2 Exact C landing contract

```
target:  corpus/knowledge/culture-material/cartography-and-mapmaking.md   (A, not M)
effect:  total 223 -> 224; culture-material 25 -> 26
README:  :5 new rev 2.5 block; :11 rev-2.4 vector repaired to 25/26/25/29/24/94;
         :234 (25)->(26); row between :240 and :241, byte-equal to the entry topic;
         :544 223->224; :548 footer 25/26/26/29/24/94
checks:  find corpus/knowledge -name '*.md' | wc -l            -> 224
         ls corpus/knowledge/culture-material/*.md | wc -l     -> 26
         python3 -B reports/round-28/readme/sweep.py           -> rows 224 files 224, exit 0
         C10 §5 scoped vector check                            -> rev 2.5 = 224, rev 2.4 = 223, exit 0
         git status --porcelain -- corpus/                     -> one A + one M, zero other corpus lines
         freshness re-run at the apply HEAD                    -> slug absent pre-apply; no second owner post-apply
```

Do **not**: repair the duplicated H1 at `corpus/README.md:1,3` in this delta (carried `R36-README-DUPLICATE-HEADING`; r39/r42 precedent leaves it); edit any filed round byte; copy C05's `26/26/25/29/24/94`; land anything under `corpus/` from a seat; or stage the C10 fixture entry (its body is a stub, only its topic string is load-bearing).

### 6.3 Exact O landing contract

```
target:  tools/harness/claims-freshness.py   (new file; stdlib only; no .scratch path)
selftest: exit 0; N/N with N computed from the registry, not a literal
r43 demo: --claims reports/round-43/claims.json --checks <sidecar>
          -> O STALE, C STALE, Ca FRESH; exit 1
negative: --claims <true-before claims> --checks <sidecar> -> FRESH; exit 0
theater:  mutated sidecar (witness name / live literals) -> same verdicts, exit 1
C-N-E:    no checks -> exit 3 (never 0)
malformed: bad JSON / no baseline / unknown probe / missing expect -> exit 2
witness:  tools/harness/couples-reference-extractor.py sha256 d8d23a26… unchanged
```

The sidecar is the correct shape for filed rounds: r43/r44 `claims.json` may not be edited to add checks. A sidecar whose `claims_source_sha256`/`before_sha256` does not match the live file is malformed, not green.

### 6.4 Exact Ca landing contract

```
target:  reports/round-47/calib/queue-successor-r47.json (or .md)
parent:  reports/round-40/op/defect-queue-v2.json sha256 dfc9265d… (re-measure before and after)
rows:    6 (5 retrospective + 1 r46 audit); dropped: []
classes: fixed-with-evidence | routed-with-owner | recorded | could-not-recover
fixed:   requires command output + landed artifact sha; otherwise routed/recorded
```

### 6.5 Do not commit

- Any second coverage entry, any entry under a different slug, any overwrite of an existing corpus file, any README bump without the entry.
- Any second resolver or gate path; any edit/rename of `tools/harness/couples-reference-extractor.py` or `basename-couples-resolver.py`; any re-freeze of `declared-in-r7`; any packet-surface change.
- Any edit to `reports/round-1..46/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`; any in-tree round-runner execution.
- Any census artifact generated from a shadow root or a 224 tree and presented as the 223 measurement; any successor that edits the parent queue.

### 6.6 What the round runner must measure (spec; never executed in-tree by a seat)

| claim | receipt fields |
|---|---|
| C | `total` 224; `culture_material` 26; `entry_sha256`; `readme_sha256`; `sweep` (rows/files/totals/footer/exit); `topic_owner_hits`; `corpus_status` (one `A` + one `M`, zero other); `readme_vector_sum` 224; `rev24_prose_sum` 223 |
| O | `tool_sha256`; `selftest_rc` 0 + pass count; `r43_demo` verdicts + exit 1; `negative_control` FRESH exit 0; `anti_theater` still stale; `no_checks_exit` 3; `malformed_exit` 2; `determinism` true; `witness_untouched` sha |
| Ca | `successor_sha256`; `rows` 6; classes in vocabulary; `parent_sha256` matches; `dropped` 0; `filed_bytes_diff` empty |
| cross | `fragments_present` vs declared outs; `corpus_modified_lines`; `validation_isolated`; live sentinels before/after |

Absent artifacts are `could-not-evaluate`, not pass. Acceptance is true only when all three claims pass; no scalar averaging.

---

## §7 — SHONEN (four boxes, draft for the fleet report)

**Box 1 — What the round set out to do.** Three debts from loop 1: land one genuinely fresh coverage entry (cartography, the gap the corpus's own cosmography entry explicitly disclaims), make the stale-premises check durable before the next dispatch (R01-43-12), and reconcile the loop-1 retrospective's carried items into a defect-queue successor without editing filed bytes. The round is a build round; it claims no promotion, canon, clearance or closure.

**Box 2 — What is measured and verified at this cut.** The baseline and all three `before` premises reproduce at `6e9a30d`: 223 entries, rev 2.4, sweep green; cartography has 0 owners by filename, topic line, header and title; the r43 regression is measured on committed bytes (`7ceff59`): O and C stale, Ca fresh. The C drafts cover the seed's ten sections; C10 stages a 224 tree and measures `224==224` with a green footer; the rev-2.4 vector's 217 sum is confirmed and the repair target is `25/26/26/29/24/94`. Three Ca rows are filed with measured evidence; the parent queue is pinned at `dfc9265d…`. These are measurements of drafts and baselines, not of a landed tree.

**Box 3 — What is not established.** No claim's `after_required` is met. There is no assembled C entry, no README edit, no O tool, no Ca successor. The content audits (C06/C07/C08/C12/C13/C14) are absent or pre-draft, so QUALITY conformance of the assembled bytes is `could-not-evaluate`. The durable gate's exit codes are not yet correct in any extant implementation (the prototype inverts them). The r44 "stale" grouping is not reproducible under the narrow reading and must not be claimed. C05's vector literals are wrong; the target mission text is lithic-derived; C07's PASS is structural only. Absent seats are `could-not-evaluate`, never green.

**Box 4 — What the next touch must do.** Apply O first, then C atomically, then Ca; re-run the audits on the assembled bytes; measure the post-landing sweep and the scoped vector; verify the gate against the r43 demo, the true-`before` control, the anti-theater mutation, the could-not-evaluate case and the malformed cases; and validate from an isolated copy. If any claim cannot land, record it honestly as `unchanged`/`unprovable` and do not let a green number from the wrong tree enter the ledger. The loop-2 opening round should be judged on the landed tree, not on this draft.

**Honest stop.** At this cut the round is **not admissible**: C and O are drafted/verified-method but unlanded; Ca has three of six rows and no successor. No axis is harmed by what is on disk. The failure modes to avoid are a C landing assembled from overlapping fragments without content audit, an O tool that copies the prototype's exit codes, and a Ca successor that double-counts r44 or drops the provider amendments.

---

## §8 — Wave census at this cut (2026-10-19T18:00Z)

`find reports/round-47 -type f` → **22 files**; **19 of 64 declared outs present**, **45 absent**, plus `claims.json`, `targets.json` and `telemetry/dispatch-declared.json`. Present, by claim:

- **C:** `scout/K01-gap-recheck.md`, `scout/K02-seed-extract.md`, `cov/C01-entry-a.md`, `cov/C02-entry-b.md`, `cov/C03-entry-c.md`, `cov/C04-entry-header.md`, `cov/C05-freshness.md`, `cov/C07-contract-audit.md`, `cov/C10-sweep.md`, `cov/V01-post-landing.md`, `plan/P02-c-plan.md`.
- **O:** `op/O10-exit-codes.md` only.
- **Ca:** `calib/Ca01-stale-premises.md`, `calib/Ca02-resolver-edge.md`, `calib/Ca03-manifest-schemas.md`, `calib/Ca05-verify.md`.
- **Cross:** `cross/X00-connector.md`, `cross/X05-baseline-drift.md`, `plan/P01-plan.md`.

Absent declared outs (all `could-not-evaluate` at this cut): `scout/K03`; `plan/P03`; the O author set `op/O01`–`O09`, `O11`–`O15`, `V02`, `W01`; the C audit/assembly set `cov/C06`, `C08`, `C09`, `C11`–`C14`, `W02`; `calib/Ca04`, `Ca06`, `Ca07`; `adj/A01`–`A03`; `cross/X01`–`X04`, `Q01`; `review/R01`–`R05`; `scribe/S02`, `S03`. A seat's absence is not a failure of the round by itself; it is an unmeasured leg. This draft's own file is filed after the census and is not counted in the 22.

---

## §9 — Integration findings register (this seat)

| id | claim | finding | evidence |
|---|---|---|---|
| **F-01** | C | **C05's post-landing vector is wrong in three places** — `26/26/25/29/24/94` instead of `25/26/26/29/24/94`; it moves the +1 into linguistics. The ownership verdict is unaffected. | `cov/C05-freshness.md:273,275,295`; correct vector at `cov/C04-entry-header.md` §3, `cov/C10-sweep.md` §2-§3, `scout/K02-seed-extract.md` §8.4, `plan/P01-plan.md` §2 |
| **F-02** | C | **The C executor missions are lithic-derived, not cartography.** `targets.json:21-23` says "container-name fossil", "material/trade classes"; the cartography seed has neither in that sense and has ten sections, not fifteen. The drafters recovered content (C02 §9 is the *mappa/charta* word bank), but the assembler must check the assembled body against K02's ten sections and de-duplicate C01 §3 vs C02 §5. | `targets.json:21-23`; `scout/K02-seed-extract.md` §9; `reports/round-42/cov/C01-entry-1.md:44,53,138`; `cov/C02-entry-b.md` §9 |
| **F-03** | O | **r44 is not a narrow stale-premises case.** Ca01 §3 measures all three r44 `before` fields true at `c9f4eaa`; r44's C defect is a carried candidate in the claim body (R02-44:441 rules it outside R01-43-12), and r44 Ca is a delivery failure. The r47 O `before`'s broad grouping must not become a claimed r44 catch. | `calib/Ca01-stale-premises.md` §3; `cross/X00-connector.md` §3, §7.2; `reports/round-44/review/R02-review.md:441` |
| **F-04** | Ca | **The MANIFEST-schema row's provenance is the r46 audit, not the loop-1 retrospective.** The retrospective has five bullets, none naming the schemas. The six-row set is five retrospective + one claim-added audit item; the successor must carry that source-coverage block rather than back-attribute it. | `calib/Ca03-manifest-schemas.md` §1; `reports/round-46/loop-1-retrospective.md:43-53`; `reports/round-46/audit/Ca01-manifest.md:7-8,28-32` |
| **F-05** | O | **The prototype's exit codes are inverted** (stale → 2, malformed → 1, could-not-evaluate → 0 under a flag). The durable tool must implement 0/1/2/3 as contracted; correct flags are not enough. | `op/O10-exit-codes.md` §1, §4; `reports/round-44/review/R01-review.md:246` |
| **F-06** | C | **C07's contract audit predates the draft** and returns `could-not-evaluate` for Q1–Q5 as delivered; its structural legs PASS. It must be re-run on the assembled bytes (its §7 script is the conversion step). A pre-draft PASS is not a content PASS. | `cov/C07-contract-audit.md` §0, §2, §8 |
| **F-07** | C | **V01 is pre-landing, not a post-landing pass.** It measures the 223 baseline and a staged 224 proof, and explicitly labels the live verdict `could-not-evaluate`. Do not file it as a landing PASS. | `cov/V01-post-landing.md` §0-§7 |
| **F-08** | C | **The post-landing resolver delta is a prediction, not a number.** C04's `- couples:` line has 21 distinct tokens; if unchanged, the next census is `entries 224 / refs 2751 / direct 2557`. Measure after apply; do not assert. | `cov/C04-entry-header.md` §4.3; this seat's token count (21/21) |
| **F-09** | C | **The broad topic-hit count is pattern-dependent** (11 vs 13) because C01/C07 include `chart`/`lienzo`; both dispositions reach **0 owners**. The record should state the pattern used, not treat the count as an invariant. | `scout/K01-gap-recheck.md` §3; `cov/C05-freshness.md` §4; `cov/C01-entry-a.md` A.4; `cov/C07-contract-audit.md` §1 |
| **F-10** | C | **No README draft exists** (C09 absent); C10's staged transforms are a model, not the landing prose. The row must be generated from the landed `- topic:` (C07 F1). | `cov/C10-sweep.md` §2, §6; `cov/C07-contract-audit.md` §6 F1 |

---

## §10 — Citations and limits

- Contract: `reports/round-47/claims.json:1-71` (baseline `:7`, axes `:15-18`, pause `:21`, C `:24-35`, O `:37-48`, Ca `:50-59`, non-goals `:61-70`); `reports/round-47/targets.json` (shared rules; seats C01–C14, O01–O15, Ca01–Ca07, S01–S03); `telemetry/dispatch-declared.json` (digests, route, 64 requested, one batched call).
- Baseline: `git rev-parse HEAD` → `6e9a30d…`; `find corpus/knowledge -name '*.md' | wc -l` → 223; partition loop → 25/26/25/29/24/94; `reports/round-28/readme/sweep.py` → rows 223 files 223, exit 0; `sha256sum corpus/README.md` → `7c788a1d…cdcd`; README anchors `:5`, `:11`, `:234`, `:240-241`, `:544`, `:548`.
- C: `reports/round-44/scout/K02-gap-scout.md` (seed; §3.5 boundaries `:181-193`, §3.6 non-carriage `:195-209`, recommendation `:211-227`, outline `:230-247`, shelf `:249-286`, calibration `:288-298`); `scout/K01-gap-recheck.md` §1-§9; `scout/K02-seed-extract.md` §1-§10 (entry contract §8, mission mismatch §9); `cov/C01-entry-a.md` §A-§E; `cov/C02-entry-b.md` §5-§9; `cov/C03-entry-c.md` §10-§15; `cov/C04-entry-header.md` §2-§4; `cov/C05-freshness.md` §3-§9; `cov/C07-contract-audit.md` §0-§9; `cov/C10-sweep.md` §1-§9; `cov/V01-post-landing.md` §0-§8; `plan/P01-plan.md` §2, §4, §7; `plan/P02-c-plan.md`.
- O: `reports/round-44/review/R01-review.md:243-250` (six-part contract), `:239` (polarity), `:241` (17/19 prototype), `:299` (R01-44-14); `reports/round-44/review/R02-review.md:207-227,424-443` (novel-phrasing, family scan, carried-candidate boundary); `reports/round-44/cross/X01-trades.md:247-320`; `reports/round-43/claims.json:27,40,53`; `reports/round-43/review/R01-review.md:400`; `reports/round-43/validation.json`; `reports/round-44/validation.json`; `op/O10-exit-codes.md`; `calib/Ca01-stale-premises.md` §2-§5; `cross/X00-connector.md` §2-§3.
- Ca: `reports/round-46/loop-1-retrospective.md:43-53`; `reports/round-46/audit/Ca01-manifest.md:5-35`; `reports/round-40/op/defect-queue-v2.json` (38 rows; sha `dfc9265d…`); `reports/round-43/calib/defect-queue-v2-successor-r43.json` (sha `77f9d63e…`); `calib/Ca01-stale-premises.md` §1-§6; `calib/Ca02-resolver-edge.md` §1-§5; `calib/Ca03-manifest-schemas.md` §1-§8; `calib/Ca05-verify.md`; `plan/P01-plan.md` §6; `cross/X00-connector.md` §5.
- Corpus contract: `corpus/QUALITY.md:1-23` (provenance, calibration, coupling, usability, canon hygiene); `corpus/knowledge/culture-material/timekeeping-instruments.md:1-10` (head-block house style); `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71,:102` (the survey-map disclaimer); `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:5` (lithic owner at `7ceff59`).
- Limits: (1) the wave was in flight; the absent artifacts in §8 are unmeasured, and no verdict in §5 certifies them. (2) This seat ran no round runner and no `tools/harness/` instrument as a verdict source; the r43 probe values are cited from Ca01/X00/P01 and re-derived where marked. (3) Digest values for the not-yet-landed entry, README, tool and successor are unknown; no digest is invented. (4) Tier B cartography editions/pages are `to-verify`; no external work was fetched or inspected. (5) The C content audit, the O tool verification and the Ca successor integrity remain the integrator's post-apply measurements, not this draft's claims.
