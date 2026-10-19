# R02 — non-author review: C is real method but assembly-defective; O is proven in scratch but undelivered; Ca is filed and pinned

- Seat: `R02` | role: reviewer (non-author) | claim: **cross** | round 47, loop 2, position 1
- Out path: `reports/round-47/review/R02-review.md` (the only write by this seat)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`; equals `reports/round-47/claims.json:7`)
- Review cut: **2026-10-19T18:05Z** (UTC). Artifacts filed after this cut are not assessed; the round was still filing when this review closed.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.
- Boundary: I read filed bytes and seat artifacts; I ran read-only probes, the live resolver, the r43 witness, and scratch reference evaluators. I did not edit a filed byte, did not stage under `corpus/`, did not run `reports/round-*/run-validation.py`, and made no git/network/install calls. `git status --porcelain` at the cut: only `?? reports/round-46/review/` and `?? reports/round-47/`; no tracked modification, no corpus delta.

## 1. Verdict summary at the cut

| claim / axis | verdict at this cut | basis |
|---|---|---|
| **C — coverage** | **premise GREEN; after_required NOT MET; draft quality real, assembly defective; no axis harm** | 223 / culture-material 25, zero owners, slug free; no landing. Drafts are 790 fenced lines vs the partition's 103–221 (max 221) and still carry a wrong `cartograph` count, an un-disposed `cosmology:27`, and a wrong craft-ladder anchor. Several C audits were pinned to superseded draft bytes. |
| **O — operability** | **could-not-evaluate on the durable deliverable; method independently demonstrated in scratch; no axis harm** | `tools/harness/claims-freshness.py` is absent. The O08 scratch reference is green 15/15 and reproduces the required r43 verdicts (O STALE, C STALE, Ca FRESH, exit 1); O06's negative control is FRESH at `c9f4eaa`, exit 0. The prototype is red 17/19 and nonconforming on exit codes. |
| **Ca — calibration** | **improved at the filed-artifact level; integrity check still owed; no axis harm** | Ca01–Ca04 rows filed; Ca06 successor contains 3 defect rows + 2 named deviations, maps 5/5 retrospective bullets + the r46 MANIFEST item, and pins the parent at `dfc9265d…`. No filed byte edited; parent unchanged. Ca07 absent. |
| **cross — axis harm** | **none observed at the cut** | corpus 223, `git diff` empty, parent queue digest unchanged, no corpus staging, no filed-byte edit. The harm risks are in the not-yet-applied assembly (C volume/dedup; O missing tool; C05's vector slip). |

**One-line judgment:** the round has three credible evidence chains, but only Ca is currently complete enough to call improved. C is a real gap with a real method draft that must be deduplicated and corrected before it earns the count; O has a proven method and no durable deliverable.

---

## 2. Claim C — coverage

### 2.1 The premise is true at the baseline (my commands, not a seat summary)

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '…/cartography-and-mapmaking.md': No such file or directory
$ find corpus/knowledge \( -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' \) -type f | wc -l
0
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223
missing_from_index 0 []  topic_mismatch 0 []  orphan_rows 0 []  header_drift {}
totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

The broad topic-line probe returns 11 hits, all metaphor, verb, statistical "survey", or handoff; the strict register probe (`cartograph|mapmak|portolan|cadastr`) returns 0. I re-read the load-bearing near-misses:

- `myth-symbol/cosmology-cosmography.md:71` — "T-O diagrams are symbolic, not survey maps"; `:102` — "not cartographic claims". These are disclaimers, not ownership.
- `myth-symbol/cosmology-cosmography.md:27` — "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." This is the strongest competing sentence and is discussed in §2.4.
- `myth-symbol/sacred-topography-pilgrimage.md:5` — the place register and route, not map production.
- `culture-material/architecture-settlement-lexicon.md:95` — the castrum grid/groma handoff.
- `civilizations/mesoamerica-primary-sources.md:58` — the lienzo source class.

The slug is free and sorts between `calendar-festival-systems.md` and `costume-semiotics.md`; the landing is an **A** (add), not an **M** (modify). I reproduced the sort insertion:

```
calendar-festival-systems.md
cartography-and-mapmaking.md
costume-semiotics.md
```

**Freshness verdict:** `FRESH-OWNERSHIP`. The only prior-round naming is the r44 K02 seed; there are zero prior-round cartography claims, drafts, or landings. I scanned reports/round-1..43 and round-46: zero `cartograph|mapmaking` hits. The r44 seed is the cited source; r44 validation records "the fresh gap (cartography, K02) has no entry body" (`reports/round-44/validation.json:9`). This is materially different from r44's dream failure, which was named at r42 and then drafted anyway.

### 2.2 "0 prior-round proposals" is literally false; scope it

`reports/round-47/claims.json:26` and the threshold (`:34`) say "no prior-round proposal" / "confirmed 0 prior-round proposals". At r47, `reports/round-44/scout/K02-gap-scout.md` **is** a prior-round scout that recommends this exact landing. The correct, checkable sentence is K01's:

> "No cartography proposal before r44 K02; r44 K02 is the cited seed and was never drafted or landed."

K01 (`scout/K01-gap-recheck.md:230-239`), C05 (`cov/C05-freshness.md:158`), and X00 (`cross/X00-connector.md:422-430`) all flag the same wording issue. I confirm the reading: a seed-only candidate with no draft is not the r44 carried-proposal failure. **This is a recording defect, not a landing blocker**; the integrator should use the scoped sentence in the entry's `- gap filled:` and in the round record, and should not repeat the unqualified phrase in LOG/SHONEN.

### 2.3 The README rev-2.4 prose-vector defect is real; the repair arithmetic is correct

`corpus/README.md:10-11` (rev 2.4) reads:

```
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**
```

Measured: the left vector sums 220 (correct for rev 2.3's 220 total); the right vector sums **217**, not 223. The live footer (`corpus/README.md:548`) is `25/26/25/29/24/94` = 223. The slot order is fixed by `reports/round-28/readme/sweep.py:39-46` and the footer: linguistics / myth-symbol / culture-material / synthesis / verification / civilizations. The defect is a three-slot rotation: myth-symbol's new 26 was written into culture-material's slot, culture-material's 25 into synthesis's, and synthesis's 29 was dropped.

Required state:

| vector | sum | status |
|---|---:|---|
| `25/23/25/29/24/94` | 220 | rev 2.3 pre-vector (correct) |
| `25/23/26/25/24/94` | 217 | rev 2.4 as filed (defect) |
| `25/26/25/29/24/94` | 223 | corrected rev 2.4 |
| `25/26/26/29/24/94` | 224 | rev 2.5 post-landing |

C09's fenced diff (`cov/C09-readme.md:77-160`) implements exactly this: it inserts rev 2.5, corrects the rev-2.4 pair to sum 223, changes the section header 25 → 26, inserts the row between calendar and costume, and moves totals/footer to 224. Its staged sweep is green 224 == 224. I independently checked the arithmetic and the diff's four hunks; the vector values are right.

**Cross-seat defect — C05 is wrong and must not be copied.** C05 predicts the post-landing vector as `26/26/25/29/24/94` at `cov/C05-freshness.md:273` and `:295`. That sums to 224 but the slots are wrong: culture-material moves in slot 3, so the correct vector is `25/26/26/29/24/94`. C10 independently caught this (`cov/C10-sweep.md:184-208`) and demonstrated that a footer carrying C05's vector fails the sweep with `FOOTER_DIR_TOTALS`. C09, C10, C04, P01, P02, X00 and V01 all use the correct vector. **The integrator must use `25/26/26/29/24/94`; C05's pair of lines should be corrected or superseded, not propagated.**

### 2.4 Draft quality: real method, not filler

I read all four draft fragments (C01 §1–4, C02 §5–9, C03 §10–15, C04 head block). The content is domain-specific and method-bearing:

- **C01** gives a five-condition register test (ground index / bounded notation / structural selection / conventional readability / reproducibility), applies it object by object, and adds six production mechanisms (selection, projection, scale, orientation, symbolization, authority). The five-condition test is a genuine discrimination procedure, not a definition paragraph.
- **C02** gives the seven-link survey-to-symbol chain and weakest-link rule, the control network as political infrastructure, the field-book/fair-copy reduction, the four scarcity regimes, the working-map/monument split, five trade roles and four products, the five-link warrant chain, the performative map, the authority ladder, and a `mappa/charta/atlas/portolan/cartouche` word bank. The word bank is cartography-specific, not a lithic copy: the *sarcophagus* is cited once as a method precedent, not reused as the example.
- **C03** gives a nine-step build order with the artifact each step must write, a two-map NON-CANON worked example (levy sheet vs pilot chart of the same lagoon), a 14-row calibration bank with R/C/B/H/T statuses, 12 decision rows (`DR-CT-01..12`), recheck triggers, and a handoff.
- **C04** gives the full head block; the `- topic:` is byte-equal to the r44 seed (766 content characters; line length 775 including `- topic: `). Its 21-token `- couples:` field resolves 21/21 from the entry directory (I re-ran the resolver). Its in-corpus anchors are extensive; my spot checks of 17 load-bearing lines passed.

This is not a manufactured `+1`. The gap is a named-but-unbuilt register, and the drafts add decision surfaces the 223 entries do not have (projection/scale, the survey chain, the map's silences, reproduction economics, the legal/performative map).

### 2.5 Assembly defects that must be fixed before apply

These are the substantive review findings. They are about the **assembled entry**, not the topic.

**C-D1 — length is far outside the partition band.** Measured fenced-body lines at my cut:

| fragment | fenced lines |
|---|---:|
| C01 §1–4 | 201 |
| C02 §5–9 | 361 |
| C03 §10–15 | 177 |
| C04 head block | 51 |
| **assembled** | **790** |

The live culture-material partition is 103–221 lines, median 149, max 221 (`wc -l corpus/knowledge/culture-material/*.md`). 790 is **5.3× the median and 3.6× the longest existing entry**. C07's own pre-staging check sets a 100–260 line band (`cov/C07-contract-audit.md:347`), which the assembled entry would fail. X04 measured the same problem at 800 body lines (`cross/X04-coverage-critic.md:11,190-200`). C02 was revised during the wave to reduce §5.4–5.6 to pointers to C01 §3 (good), but the total remains far out of band.

**C-D2 — the boundary table omits the corpus's own `cosmology:27` definition.** `cosmology-cosmography.md:27` says cosmography is "how the world is drawn (maps), named, walked, and built". C01 §1.1 (`cov/C01-entry-a.md:96`) and C04's `- gap filled:` (`cov/C04-entry-header.md:115`) cite only `:71`/`:102`, the disclaimers. C08 noticed the competing definition (`cov/C08-boundary.md:140-144`) but treated it as a wording issue in C01 §4.1, not as a required boundary statement. X04 is stricter (`cross/X04-coverage-critic.md:99-101`): the entry should add one sentence — *cosmography owns the cosmogram/world-drawn content (`:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production* — so the one-owner claim is not overstated at its strongest competing sentence. I agree with X04.

**C-D3 — the fenced `- gap filled:` miscounts `cartograph`.** It says `grep -rli 'cartograph'` → "2 files / 3 lines" and attributes the lines to `cosmology-cosmography.md:71,:102` plus `mesoamerica-primary-sources.md:58` (`cov/C04-entry-header.md:115`). Measured: strict `grep -rn 'cartograph' corpus/knowledge` returns **2 lines in 2 files** (`cosmology:102`, `mesoamerica:58`); `grep -rli` lists files, not lines, so the cited command cannot produce "3 lines"; and `:71` contains "Mappa Mundi" / "survey maps", not the word `cartograph`. This is the same class as the r43 stale-premise defect one level down: an evidence sentence its own command does not produce. Fix to "2 lines / 2 files" and state the exact probe. X04 found the same (`cross/X04-coverage-critic.md:114`).

**C-D4 — a wrong craft-ladder anchor.** C02 §7.3 cites `craft-artisan-lexicon.md:44` for the apprentice→journeyman→master ladder (`cov/C02-entry-b.md:267`). Line 44 is the steel material-grading row; the guild ladder is at `:56-63` (Germanic, London, Ottoman, Persianate, Chinese, Japanese, Indian, non-guild). C08's P1-2 (`cov/C08-boundary.md:173-175`) is correct. Fix the anchor to `:3,:56-63` and keep `:44` only for material grading; C04's couples parenthetical ("material-grading vocabulary — `:44`") is defensible for the grading half but should not imply the ladder.

**C-D5 — four boundary rows are missing from the table, although the body develops them.** C08 names craft-artisan-lexicon, trade-economy-lexicon, celestial-symbolism-calendars, and sacred-kingship-mythic-charter as P1 rows (`cov/C08-boundary.md:168-186`). The body does develop the mapmaker trade, the legal/territorial instrument, the star-chart form, and the legal-vs-mythic charter; the table should carry the "owns / does not restate" rows. C08's fenced rows (`:215-219`) are integration-ready.

**C-D6 — the executor missions were written in r42 lithic language.** `targets.json:21-23` says "the property that makes a map a register", "material/trade classes", "container-name fossil" — phrases copied from the r42 lithic draft (`reports/round-42/cov/C01-entry-1.md:44,53,138`). The drafters adapted them in substance (C01's five-condition test, C02's `mappa/charta` bank), so the mismatch did **not** produce filler. But the planner did not reconcile the missions: P01 §4.3 asks for the seed spine while handing out the lithic split (`plan/P01-plan.md:133-150`). The integrator should audit the assembly against `reports/round-44/scout/K02-gap-scout.md:234-247`, not against `targets.json:21-23`. K02 flagged this first (`scout/K02-seed-extract.md:220-231`); X04 independently confirms the substance was adapted (`cross/X04-coverage-critic.md:204-213`).

### 2.6 Audit chain status: not landing-ready

The C claim's `after_required` says "audits PASS". At my cut, that is not true:

| audit | status |
|---|---|
| C05 freshness | PASS on ownership; **wrong post-landing vector at `:273,:295`** |
| C06 source audit | **absent** |
| C07 contract audit | filed, but **pre-bytes**: it explicitly marks all QUALITY clauses `could-not-evaluate` because the drafts did not exist at its cut (`cov/C07-contract-audit.md:8,18-20`) |
| C08 boundary | filed, but pinned to C01 `b0ee0d6d…`, C02 `3fc24d3e…`, C04 `6285ad62…`; current bytes are C01 `cfb42955…`, C02 `bfce3ac…`, C04 `cb5a7489…` (C03 unchanged). Its P1 findings still reproduce where I re-checked, but the audit must be re-run on the final bytes. |
| C10 sweep | PASS on a staged fixture; control D correctly proves the sweep does not read revision vectors |
| C12 shelf | **absent** |
| C13 couples | PASS on the **field**: the `- couples:` line hash `cf59ba1f…` (with trailing newline) still matches the current C04, even though the container changed; 21/21 direct, +21 refs. Re-run after assembly. |
| C14 worked example | **absent** |
| V01 post-landing | **staged only**; live verdict `could-not-evaluate` (`cov/V01-post-landing.md:9-17`) |

C08's stale pins are not a contradiction of its findings — I re-read the two key citations and they still fail — but they mean the C evidence chain cannot be filed as "audits PASS" without a re-run on the assembled entry. The integrator should also re-run C05's ownership sweep at the apply-time HEAD and C13's field audit after assembly.

### 2.7 C verdict

**No axis is harmed by anything on disk.** The gap is real, the landing is an add, and the drafts are method. But the claim is **not yet improved**: the entry is 3.6× the partition's maximum, C01 §3 and C02 §5.4–5.6 still share the projection/scale/orientation/symbol decision surface (C02 has been substantially reduced to pointers since X04's first cut, but the remaining entries are long and the symbol/blank rules are still restated in production terms), and it carries an unreproducible `cartograph` count plus an un-disposed `cosmology:27`. If landed as-is, the count moves to 224 but the entry is volume-inflated; if trimmed, corrected, and re-audited, coverage is a genuine improvement.

---

## 3. Claim O — operability

### 3.1 The r43 stale premises are real; I reproduced them from baseline bytes

At `7ceff59` (r43's baseline):

```
$ git ls-tree --name-only 7ceff59 tools/harness/
tools/harness/couples-reference-extractor.py
… (six other tools)
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
… PASS N6 regression guard: block read yields 4 tokens
['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
SELFTEST OK: 8/8
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -
$ git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/
(no output)
```

So:

- r43 O's `before` ("no durable instrument implements the r39 basename-couples policy"; "the wrapped field reads 0/4") is **false on both clauses** at its own baseline.
- r43 C's `before` ("lithic slot named but unbuilt") is **false on ownership** at its own baseline; its counts 26/223 are true.
- r43 Ca's `before` ("no per-finding disposition on record") is **true** at its own baseline; the disposition artifact is absent.

This matches r43's validation (`reports/round-43/validation.json`), R01-43-12, X00 §2, O05, and Ca01/Ca05. The regression's factual base is solid.

### 3.2 The method is independently demonstrated — in scratch, not in the durable path

The durable target is absent:

```
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
```

What exists is a scratch reference evaluator (`O08`), which I ran read-only:

```
$ sha256sum .scratch/o08/claims-freshness.py
009a51182979c60355a56e6d7b4ae82a4c8a4ebdfae5f41445e967a4bf8d3d6c
$ python3 -B .scratch/o08/claims-freshness.py --selftest
… SELFTEST OK: 15/15 controls
rc=0
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o08/r43-checks.json
[O] STALE
  - capability_present: MISMATCH
  - capability_present: MISMATCH
[C] STALE
  - count_eq: MATCH
  - count_eq: MATCH
  - topic_owner_absent: MISMATCH
[Ca] FRESH
  - path_absent: MATCH
summary: STALE (exit 1)
rc=1
```

The reference also survives the anti-theater mutations:

```
$ … --claims .scratch/o08/r43-mutated-prose.json   → STALE, rc 1
$ … --claims .scratch/o08/r43-mutated-target.json  → STALE, rc 1
```

and the naive variant is the control that shows why typed probes matter:

```
$ … --claims .scratch/o08/r43-naive.json           → FRESH, rc 0
```

That is the anti-theater property: a literal-path/count gate would pass r43 O (the named successor path was absent at baseline); the capability probe does not. O05's demo reaches the same verdicts (`op/O05-r43-demo.md:219-243`); O06's negative control is FRESH 3/3, 9/9 clauses at `c9f4eaa`, exit 0, and flips O stale only at HEAD, proving baseline-vs-worktree discrimination (`op/O06-negative-control.md:270-310`). O10 built a 14-case exit-code suite that is green against a compliant double and red 11/15 against the prototype, and found the prototype's codes inverted (stale → 2, malformed → 1) and `--allow-unverifiable` turning could-not-evaluate into exit 0 (`op/O10-exit-codes.md:103-141`). O13 found 6 of 13 prototype probe kinds dead, no declared probe registry, `capability_present` missing/renamed, and unknown kinds downgraded to STALE rather than MALFORMED (`op/O13-probe-coverage.md:61-159`).

**What this proves:** the method is feasible, the r43 positive regression is correct, and the negative control is real. **What it does not prove:** the durable deliverable. The claim says "tools/harness/claims-freshness.py durable with a green selftest"; at this cut that file does not exist. A scratch reference is evidence about the method, not about the lane.

### 3.3 The O claim's historical parenthesis overstates r44

`claims.json:40` says "r43 and r44 both declared claims on stale premises (green resolver existed; owned/carried topics)". The narrow facts:

- r43 O and r43 C are the two stale `before` sentences named by R01-43-12.
- r44 O's `before` ("no four-class census authority") was **true** at `c9f4eaa`; r44 O landed and was recorded `improved`.
- r44 C's failure was a **carried candidate** (dream, named at r42 K02), not an owned topic; R02-44 itself ruled it outside the stale-premises class.
- r44 Ca was a **delivery** failure, not a stale premise.

X00 §7.2, Ca01 §3, Ca05 F3, and P03 all flag this. The actionable clause — "no durable gate exists" — is true; the historical parenthesis is imprecise. The integrator should not repeat "r43 and r44 both declared claims on stale premises" in LOG/SHONEN; write "r43 O/C stale; r44 C carried-candidate; r44 Ca undelivered".

### 3.4 O verdict

**could-not-evaluate on the deliverable; no axis harm.** The method is demonstrated, but the durable tool, its green selftest, the r43 demo from the durable path, the anti-theater run from the durable path, and the negative control from the durable path are all still owed. The honest verdict at this cut is **not improved**. If O01–O04/O07 land a durable tool before close, re-run O08/V02 and O10's suite; otherwise the round should record O as delivered-in-method but undelivered-in-artifact, not as a partial pass.

---

## 4. Claim Ca — calibration

### 4.1 Coverage of the loop-1 carried list

`reports/round-46/loop-1-retrospective.md:43-53` names five carried items. Ca06's `loop1_coverage` maps them 5/5 with zero dropped, plus the r46 audit's MANIFEST schema note as the claim's additional item (`calib/Ca06-queue-successor.md:55-74,237-287`):

| retrospective item | Ca disposition | class |
|---|---|---|
| freshness gate absent (`:45-46`) | `r43-stale-premises` | `routed-with-owner` |
| stale-premises pattern (`:47-48`) | same row (same class, narrow incidence r43 O+C) | `routed-with-owner` |
| resolver latent edge (`:49-50`) | `r44-resolver-hyphen-after-blank` | `recorded` |
| antigravity outage (`:51-52`) | `dev-antigravity-outage` | `named-deviation` |
| zai exhaustion (`:53`) | `dev-zai-exhaustion` | `named-deviation` |
| r46 MANIFEST schemas (audit) | `manifest-ledger-two-schema-evolution` | `recorded` |

The two provider rows are deliberately outside `rows[]` and outside the defect count, following the parent queue's own "telemetry deviations NOT defect rows" practice (`reports/round-40/op/defect-queue-v2.json:8`). This is the correct classing: no rule breach is alleged, and the requested/observed split is kept.

### 4.2 Independent checks of the rows

- **Ca01 (stale premises):** class `routed-with-owner` is correct because the O tool does not exist. The row's measurement at `7ceff59` reproduces (I ran the same git probes). It does not claim a fix; the reclass gates G1–G7 are explicit, including "durable path", "green selftest", "r43 O/C stale + Ca fresh", "negative control", "anti-theater", "baseline not worktree", and "could-not-evaluate is not green". Good discipline.
- **Ca02 (resolver latent edge):** I reproduced the defect from the current pinned body: `couples_block` on the inline fixture returns `['language — `tone-']`, `field_refs` returns `set()`, while the r42 witness reads 2 tokens. My corrected live scan (a true blank line, then an indented hyphen continuation) returns **0** hits over 223 entries. The class `recorded` and the `0/223` scope are correct. The parent pin matches.
- **Ca03 (MANIFEST schemas):** the two schemas are documented with field sets and a live ledger digest. Ca03 correctly scopes S2 to r46 as well as 43/44 (`calib/Ca03-manifest-schemas.md:62-87`), which addresses Ca05's F1. The ledger digest is an observation-window pin, not a claim of immutability; that is the right treatment for a live sibling ledger.
- **Ca04 (provider amendments):** it corrects the mission's "positions 12/13 skipped" to the measured "position 12 re-routed and executed; position 13 skipped" and keeps the zai exhaustion vs interruption ambiguity as `to-verify` rather than laundering "interrupted x2" into "quota exhausted" (`calib/Ca04-provider-amendments.md:87-99,163-200`). This is exactly the kind of precise wording Ca05 F2 asked for.
- **Ca05 (independent verifier):** it re-measured the rows rather than trusting them; its F1–F5 are real precision findings, and F4 (do not mark fixed without a durable tool + demo) is the correct bar.
- **Ca06 (successor assembly):** the fenced JSON has 3 defect rows + 2 named deviations, parent pin `dfc9265d…` re-checked after assembly, predecessor pin `77f9d63e…`, `loop1_coverage` 5/5 + 1, and no `fixed-with-evidence` rows. The `source_fragments` digests are pinned. It notes Ca04 was absent at assembly and provides G8 to reconcile by evidence rather than duplicate; Ca04 has since landed, so the integrator must apply G8.

### 4.3 Integrity

```
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
$ git status --porcelain -- reports/round-40/op/defect-queue-v2.json
(empty)
$ git diff --stat
(empty)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

The parent is byte-identical at `6e9a30d` and in the worktree; no `.scratch` successor edited it. No filed byte was edited. The only corpus count is still 223/25; Ca made no corpus delta.

### 4.4 Ca verdict

**Improved at the filed-artifact level; integrity check still owed.** Ca06 is a complete successor draft: every loop-1 carried item reaches a class with an owner and cited evidence, the provider amendments are named deviations, and no `fixed` claim is made without a landed artifact. The remaining obligations are Ca07 (independent successor-integrity recheck), the Ca04/Ca06 G8 reconciliation (do not double-count the two deviations), and the integrator's decision whether to apply the fenced JSON as `queue-successor-r47.json`. No axis harm.

---

## 5. Axis-harm ledger

| risk | claim | status at the cut | tripwire |
|---|---|---|---|
| C lands a carried/duplicate topic | C | **No.** 0 owners; only r44 K02 seed; no pre-r44 naming; no draft/landing. | Scoped wording for "0 prior-round proposals"; re-run ownership at apply HEAD. |
| C creates a second owner via `cosmology:27` | C | **Open.** The table disposes `:71/:102` but not `:27` ("how the world is drawn (maps)"). | Add the content-vs-production sentence/row (X04 §3, C08 P1-1). |
| C volume-inflates the partition | C | **Open.** 790 fenced lines vs 103–221 (median 149, max 221). | Deduplicate C01 §3 vs C02 §5; target ≤300 lines or record a deliberate exception. |
| C README arithmetic wrong | C | **No.** C09's diff is correct; C10 staged green. **But C05's `26/26/25/29/24/94` is wrong.** | Use `25/26/26/29/24/94`; correct/supersede C05. |
| C evidence sentence unreproducible | C | **Open.** `cartograph` "2 files / 3 lines" is actually 2 lines / 2 files; `:71` is not a `cartograph` hit. | Fix the fenced `- gap filled:` before apply. |
| C audit chain claims PASS on stale bytes | C | **Open.** C08 pins C01/C02/C04 hashes that no longer match; C07 is pre-bytes; C06/C12/C14 absent. | Re-run C06/C07/C08/C12/C13/C14 on the assembled entry. |
| O gate is theater | O | **Not demonstrated; the scratch reference survives prose/target mutations and the naive gate fails.** | Require the durable path to reproduce the mutation results. |
| O overclaims r44 | O | **Open in the claim text.** r44 O was true/improved; r44 C was carried, not owned. | Fix LOG/SHONEN wording; do not call r44 a stale-before case. |
| O durable tool absent | O | **Open.** `tools/harness/claims-freshness.py` absent; only scratch references. | Land O01–O04; run O08/V02/O10 from the durable path. |
| Ca edits filed bytes | Ca | **No.** `git diff` empty; parent digest unchanged; no corpus writes. | Ca07 + G1–G8. |
| Ca double-counts provider rows | Ca | **Open integration risk.** Ca04 and Ca06 both author antigravity/zai rows; Ca06's G8 anticipates reconciliation. | Reconcile by id/evidence; keep deviations out of `rows[]`. |
| Write surface bleed | cross | **No.** Only `reports/round-47/**` (plus the pre-existing untracked `reports/round-46/review/`). No tracked modification. | A03 census; X05 OBS-1 classifies the r46 review. |

**No axis is harmed by the bytes on disk.** The harm risks are all in the not-yet-applied assembly and in the evidence chain's stale pins.

---

## 6. What I would require before admission

### C

1. Fix the fenced `- gap filled:`: `cartograph` = **2 lines / 2 files** (`cosmology:102`, `mesoamerica:58`); state the exact probe; do not count `:71` as a `cartograph` hit.
2. Add the `cosmology:27` disposition (content vs production), or a boundary row that cites it explicitly.
3. Merge C08's four P1 rows (craft, trade, celestial, sacred-kingship) and fix the craft-ladder anchor to `:3,:56-63` (keep `:44` for material grading only).
4. Deduplicate C01 §3 against C02 §5.4–5.6; target the partition band. If the integrator wants a longer reference entry, record a deliberate ruling — do not let concatenation decide.
5. Re-run C06/C07/C08/C12/C13/C14 on the assembled entry bytes; C07's `could-not-evaluate` is not a pass, and C08's pins are stale.
6. Use `25/26/26/29/24/94` everywhere; never C05's `26/26/25/29/24/94`.
7. Regenerate the README row from the landed `- topic:` (C09 §3.1); keep the topic byte-equal.

### O

1. Land `tools/harness/claims-freshness.py` from the O01–O04 drafts (the O08 reference is not the deliverable).
2. `--selftest` green with the control count computed from the registry; no dead probe kinds; the eight-kind contract (or a documented superset) implemented; unknown kinds → MALFORMED/exit 2, not STALE.
3. Run the r43 annotated demo from the durable path: O STALE, C STALE, Ca FRESH, exit 1.
4. Run the r44 negative control: FRESH, exit 0; run the anti-theater mutations: still STALE; run the baseline-vs-worktree discriminator; run the could-not-evaluate and malformed cases (non-zero / exit 2).
5. Fix the r44 overstatement in LOG/SHONEN before it is recorded.

### Ca

1. Apply Ca06's fenced JSON as `queue-successor-r47.json` (or record why the `.md` artifact is the successor).
2. Run Ca07's integrity check: every cited path/sha resolves; parent `dfc9265d…` unchanged; no `fixed` row without a re-run.
3. Reconcile Ca04's `PA-47-01/02` with Ca06's `dev-antigravity-outage`/`dev-zai-exhaustion`; do not duplicate the two deviations.
4. If O lands, file a **new** closing row for `r43-stale-premises`; never edit Ca06 or the parent.

---

## 7. Could-not-evaluate / to-verify at this cut

- **O durable tool** — absent; the entire O `after_required` is unproven on the durable path. Owner: O01–O04 + integrator.
- **C06 source audit, C12 shelf, C14 example** — absent. C07 is pre-bytes. C08's pins are stale for C01/C02/C04. C05 has the vector slip. V01 is staged-only.
- **Ca07 successor integrity** — absent; Ca06's rows are not independently checked for path/sha integrity beyond Ca05's input check.
- **`reports/round-47/run-validation.py`** — absent at the cut; the claims' counting command cannot run in-tree anyway (the absolute rule), so the integrator must author it and run it in isolation.
- **C04 self-audit length** — it reports "seed_len 758 / mine_len 758"; measured line length is 775 (content 766), byte-equality is true. The equality claim is correct; the length number is stale.
- **C05's vector** — `26/26/25/29/24/94` at `:273,:295`; correct is `25/26/26/29/24/94`.
- **X05 OBS-1** — `reports/round-46/review/R01-review.md` is untracked, created after the baseline; not cited by any r47 claim. A03 should classify it; do not treat it as baseline evidence.
- **r47 C02/C01 revisions** — C02 was revised during the wave (fenced body 424 → 361; §5.4–5.6 reduced to pointers), C01/C04 also changed hashes. My findings are against the current bytes listed in §8; any later edit invalidates the corresponding pin.

---

## 8. Evidence appendix (commands and key outputs)

All commands from the lane root, 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ git diff --stat
(empty)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223 … totals_line 223 totals_ok True … footer_ok True … exit=0
$ sha256sum corpus/README.md reports/round-40/op/defect-queue-v2.json
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json
$ git ls-tree --name-only 7ceff59 tools/harness/
tools/harness/couples-reference-extractor.py
…
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
… SELFTEST OK: 8/8, exit 0
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -
$ git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/
(no output)
$ ls tools/harness/claims-freshness.py
No such file or directory (exit 2)
$ sha256sum .scratch/o08/claims-freshness.py
009a51182979c60355a56e6d7b4ae82a4c8a4ebdfae5f41445e967a4bf8d3d6c
$ python3 -B .scratch/o08/claims-freshness.py --selftest
SELFTEST OK: 15/15 controls, rc 0
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o08/r43-checks.json
[O] STALE … [C] STALE … [Ca] FRESH … summary: STALE (exit 1), rc 1
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o08/r43-mutated-prose.json
STALE, rc 1
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o08/r43-mutated-target.json
STALE, rc 1
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o08/r43-naive.json
FRESH, rc 0
$ grep -rn 'cartograph' corpus/knowledge | wc -l
2            # cosmology:102, mesoamerica:58 (2 files)
$ sed -n '27p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
- **Cosmology** = … **Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples).
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221
$ python3 (fenced-body line counts at cut)
C01 201, C02 361, C03 177, C04 51 → 790
$ python3 (C04 couples extraction)
21 tokens, 21/21 resolve; line sha256 cf59ba1f… (with trailing newline)
$ python3 (C04 topic vs seed)
byte_equal True; line length 775, content 766
$ sha256sum reports/round-47/cov/C01-entry-a.md reports/round-47/cov/C02-entry-b.md reports/round-47/cov/C03-entry-c.md reports/round-47/cov/C04-entry-header.md
cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d  C01
bfce3acaf20e527b949a45b708f1d9e10c9ab9447651375f89075f1c80be3600  C02
4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5  C03
cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0  C04
```

Artifacts read (selective, non-exhaustive): `scout/K01-gap-recheck.md`, `scout/K02-seed-extract.md`, `scout/K03-gate-spec.md`, `plan/P01-plan.md`, `plan/P02-c-plan.md`, `plan/P03-o-plan.md`, `cov/C01-entry-a.md`, `cov/C02-entry-b.md`, `cov/C03-entry-c.md`, `cov/C04-entry-header.md`, `cov/C05-freshness.md`, `cov/C07-contract-audit.md`, `cov/C08-boundary.md`, `cov/C09-readme.md`, `cov/C10-sweep.md`, `cov/C13-couples.md`, `cov/V01-post-landing.md`, `op/O05-r43-demo.md`, `op/O06-negative-control.md`, `op/O10-exit-codes.md`, `op/O13-probe-coverage.md`, `calib/Ca01-stale-premises.md`, `calib/Ca02-resolver-edge.md`, `calib/Ca03-manifest-schemas.md`, `calib/Ca04-provider-amendments.md`, `calib/Ca05-verify.md`, `calib/Ca06-queue-successor.md`, `cross/X00-connector.md`, `cross/X04-coverage-critic.md`, `cross/X05-baseline-drift.md`.

No command wrote outside `.scratch` or this out path. No filed byte was edited. Nothing under `corpus/` was staged. No `reports/round-*/run-validation.py` was executed. No git mutation, network, or install occurred.
