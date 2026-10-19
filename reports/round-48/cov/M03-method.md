# M03 — method-fidelity verification (claim C)

- Seat `M03` | role verifier | claim **C** (coverage) | round 48, loop 2, position 2
- Out path: `reports/round-48/cov/M03-method.md` (this file). I wrote no other file, staged nothing under `corpus/`, and edited no filed bytes.
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`).
- Mission (verbatim, `reports/round-48/targets.json:67`): *"Method-fidelity verifier: does the entry teach the register METHOD (property->mechanism->classes->scarcity->trade) or just describe maps? Judge it does what a register entry must."*

## Verdict in one line

**The method is taught, not described — PASS on substance — but the only complete cartography body in existence (r47's 739-line draft) fails method fidelity in three places that a right-sized successor must not inherit: a wrong arithmetic demonstration (B1), a worked example that states its one update rule three ways (B7), and a build table that covers 5 of the 8 forms it claims (B9).** At my write cut the r48 body does not exist, so the assembled r48 entry is `could-not-evaluate`; what the round *does* have — the 23-line head block (`reports/round-48/cov/C02-header.md`) and the 27-line worked example (`reports/round-48/cov/M01-example.md`) — carries the method correctly, and §7 below is the binding method-fidelity gate for the assembled body.

---

## 1. What I read, and what did not exist

At seat time, `reports/round-48/` contained `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`, and cov fragments `C02-header.md`, `C04-citations.md`, `C09-couples.md`, `C11-sweep.md`, `C14-example.md`, `C15-neighbors.md`, `M01-example.md`. **No r48 entry body (`C01-entry*.md`) existed.** I therefore verified:

1. the r47 assembled cartography body — the only complete body, and the negative fixture the round is built to correct (`reports/round-47/cov/C01-entry-a.md`, `C02-entry-b.md`, `C03-entry-c.md`);
2. the r48 method-bearing fragments that do exist — `C02-header.md` (head block) and `M01-example.md` (worked example);
3. the live partition, to check that the method target is within house length discipline.

**Body length, measured fence-to-fence at the baseline:**

```
C01 body  lines 86–286   = 201
C02 body  lines 41–401   = 361
C03 body  lines 73–249   = 177
total                        = 739
```

C03's closing fence is four backticks at `C03-entry-c.md:250`; the body ends at `:249`. My 739 reproduces R03's 739 exactly (`reports/round-47/review/R03-c-content.md:26`).

**Live partition** (my own command, not carried):

```
$ python3 -c "import glob,statistics; ls=[sum(1 for _ in open(f)) for f in glob.glob('corpus/knowledge/culture-material/*.md')]; print(len(ls),min(ls),statistics.median(ls),max(ls),round(statistics.mean(ls),1))"
25 103 149 221 150.2
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

So the draft is **739 / 221 = 3.34×** the longest existing entry and **4.96×** the median. Length is not a method defect by itself, but a register method that cannot be stated inside the house band is not yet a usable register method.

---

## 2. The test: what a register entry must do

I derived the five-move test from the mission and checked it against the partition's own register entries. The house skeleton is real, not invented for this seat:

- `corpus/knowledge/culture-material/timekeeping-instruments.md` runs 11 sections: owns/boundary (§1) → classes/resolution (§2) → the biggest design decision (§3) → unit ladder (§4) → institutions (§5) → ownership (§6) → archaeological inference (§7) → calibration (§8) → decision record (§9) → build order (§10) → handoff (§11).
- `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` runs 13: owns/slot (§1) → jobs (§2) → designable properties (§3) → code form (§4) → value language (§5) → axis/boundary/witness (§6) → quarry-to-workshop chain (§7) → what the register cannot do (§8) → cross-register coupling (§9) → build protocol (§10) → decision record + worked culture (§11) → calibration (§12) → handoff (§13).

The cartography draft's 15 sections are the same shape with a lexicon (§9) and a recheck (§14) added. The method obligations I test are:

| Move | Obligation | What counts as teaching, not describing |
|---|---|---|
| **1. Property** | State what the register is, and bound it against neighbours | a definition + a discriminating test that admits and rejects named objects + a one-owner statement |
| **2. Mechanism** | State how the register produces its object/meaning | a chain or mechanism table whose rows force a decision; a weakest-link or equivalent rule |
| **3. Classes** | Give the typology with costs and silences | forms × survey × medium × patron × *what the form cannot show* |
| **4. Scarcity** | Explain the political economy | cost stack, scarcity regimes, prestige currencies, working/monument split |
| **5. Trade** | Explain who makes and sells it | roles, organization models, products, customers, and the conflict each creates |
| **6. Demonstration** | Show the method working once | one NON-CANON example, one rule stated once, a build order, and a decision record the example instantiates |

`corpus/QUALITY.md:16-17` is the admission bar behind move 6: "decision tables, typology tables, checklists, worked examples. No essays."

---

## 3. Move-by-move judgment of the r47 body

All counts below are my own, from the cited line ranges.

### 3.1 Property — PASS

- Master claim and four load-bearing choices: `C01-entry-a.md:88-89`.
- Definition plus five-condition test (ground index, bounded notation, structural selection, conventional readability, reproducibility/citability): `:111`, `:115-121` (5 data rows counted).
- Nine objects dispositioned, including the T-O diagram, portolan, cadastral plan, star chart, stick chart and mental map: `:124-134` (9 data rows). "Partial" is ruled a fail at `:136`, which is the discriminating move.
- One-owner statement: the map is a **composition register**, not a sixth symbolic register (`:105`), with the register-of-registers rule at `:145`.
- Boundary table: 8 rows (`:94-103`), each with "owns / this entry takes, and must not restate".

The property move is genuinely operational: a designer can take an object and answer yes/no. It teaches the register's admission test.

### 3.2 Mechanism — PASS (with a wrong arithmetic demonstration)

- Six meaning mechanisms (selection, projection, scale, orientation, symbolization, authority), each ending in a design lever at `C01-entry-a.md:165, 180, 187, 198, 207, 215` (6 `Design lever.` lines counted).
- Seven-link survey-to-symbol chain, each link carrying "the decision it forces": `C02-entry-b.md:47-55` (7 link rows counted).
- The weakest-link rule, stated once: `C02-entry-b.md:45`.
- Chain failure table with "design use": `C02-entry-b.md:124-133` (8 rows counted).

The one quantitative rule in the mechanism move is the false-precision rule at `C02-entry-b.md:98`, and its arithmetic is wrong (M-D1 below). That matters for method fidelity: the rule is taught by example, and the example teaches the wrong ratio.

### 3.3 Classes — PASS (with a coverage gap)

- Eight forms with survey feed, medium, patron, exemplar and **what each structurally cannot show**: `C01-entry-a.md:238-249` (8 form rows counted). The "cannot show" column is the strongest anti-typology move in the draft.
- Material classes: `:254-263`; trade classes: `:265-276` (8 rows counted); design rules R1–R5: `:280-286`.
- R1 ("pick the question first") and R5 ("state the mixed forms") are real design rules, not descriptions.

The classes move is sound, but the build-order table that is supposed to make it actionable covers only 5 of the 8 forms (M-D3).

### 3.4 Scarcity — PASS

- Cost stack with who bears each cost: `C02-entry-b.md:155-162` (6 rows counted).
- Four scarcity regimes with a plot engine each: `:168-178` (4 rows counted).
- Four prestige currencies: `:182-187` (4 bullets counted); rule at `:187`.
- Working map vs monument map, and its survivor bias: `:191-199`.
- The loop and its four breaks: `:203-210`.
- The governing rule — "the institution that pays for the survey owns the map's politics" (`:164`) — is the kind of claim that changes a design decision.

### 3.5 Trade — PASS-with-fix

- Six roles with owns/sells/failure/anchor: `C02-entry-b.md:224-231` (6 rows counted).
- Organization models: `:235-244`; products: `:254-263`; three customers: `:270-274`; the "one map cannot serve all three" rule at `:276`.
- The trade move is operational: a designer must choose which customer the mapmaker serves.

But the section header says **"five roles"** while the table has **six** (`C02-entry-b.md:218` vs `:224-231`), and the apprenticeship anchor is wrong (M-D4, M-D5). Both are exactly the unverified-count class R03 flagged in r47.

### 3.6 Warrant — PASS

- Five-link warrant chain (warrant → record → attestation → authentication → use): `C02-entry-b.md:282-292` (5 rows counted).
- Performative map: `:294`; authority ladder: `:302-312`; five provenance failures: `:314-320`; contest rule: `:322-330`; eight decisions: `:332-345`.
- The rule "a map's authority is the weakest link in this chain" (`:292`) applies the same method as the survey chain, which is good internal coherence.

This sixth move is not in the mission's five but is load-bearing: without it the entry would describe map production and miss why a sheet is believed.

### 3.7 Demonstration — FAIL (the blocking method defect)

- Build order, nine steps: `C03-entry-c.md:77-87` (9 rows counted). Good.
- Worked example: `:107-152`. It runs the same lagoon twice and uses a storm to stage the dispute — the right shape.
- **But the update rule is stated three incompatible ways:** `:123` says re-survey after any storm that breaches a dike; `:137` says the re-survey is not due until the levy year turns and the joint rule is "after every breach, not every levy year"; `:150` tabulates "after a dike breach, per levy year". The decision record's own DR-CT-09 (`:203`) states the intended rule correctly, so **the example contradicts the decision record it is supposed to instantiate.**
- **And the example names zero decision rows:** `sed -n '107,152p' … | grep -c 'DR-CT-'` → `0`. The reader cannot see which of the 12 rows the example demonstrates.
- Calibration bank: 14 rows (`C03-entry-c.md:158-173`, counted); decision record: 12 rows (`:193-206`, counted); recheck: 9 bullets (`:212-222`, counted); scope: `:231-249`. These are all present and method-complete.

A register entry's worked example is the proof that the method is executable. A self-contradicting example is therefore not a copy-edit problem; it is a method-fidelity failure.

### 3.8 Does it merely describe maps? — No

The draft is not an essay about maps. Evidence: 6 design levers, 7 chain links each with a forced decision, 8 forms each with a structural silence, 8 chain failures each with a design use, 12 decision rows, 9 build steps. Reference material (§3.2 projection families, §9 word bank) sits inside a method, as it does in the partition's timekeeping entry. The defect is **duplication and length**, not shallowness.

---

## 4. Method defects the right-sized successor must not inherit

| ID | Location | Finding | Fix |
|---|---|---|---|
| **M-D1** (B1) | `C02-entry-b.md:98` | `0.2 mm × 50,000 = 10 m`; a 200 m closure is **20×** coarser, but the text says "ten times". Recomputed: `0.2*50000/1000 = 10.0`; `200/10 = 20.0`; `100/10 = 10.0`. | Change "200 m" to "100 m", or "ten times" to "twenty times". Keep the rule. |
| **M-D2** (B7) | `C03-entry-c.md:123, :137, :150` | The one update rule is stated three ways; DR-CT-09 (`:203`) is correct, so the example contradicts its own decision row. | Adopt one rule: Sheet A is current to the levy year; the joint rule is re-survey after every breach. Make `:123` and `:150` say that, keep `:137`, and tag the example with DR-CT-09. |
| **M-D3** (B9) | `C03-entry-c.md:97-103` vs `C01-entry-a.md:240-249` | The "minimum credible build per form" table has 5 data rows (itinerary, cadastral, portolan, chorographic, cosmographic) against 8 forms. Celestial, thematic and lienzo have no minimum build. | Add the three rows, or retitle "five common forms" and state how the other three are priced. Do not leave "per form" over a 5-of-8 table. |
| **M-D4** (new) | `C02-entry-b.md:218` vs `:224-231` | Header says "five roles"; the table has **six** (surveyor, cosmographer, draftsman, engraver/printer, instrument maker, pilot). Counted 6 data rows. | Change the header to "six roles" (do not drop a role to save the count). |
| **M-D5** (B4) | `C02-entry-b.md:248` | The workshop ladder is cited to `craft-artisan-lexicon.md:44`, which is the Steel (Japan) material-grading row. The ladder is `:54` (header), `:56-63` (systems), `:65` (design rule). | Cite `:54-65`; keep `:3` only for the topic-line summary. This is a trade-move evidence failure, not a stylistic one. |
| **M-D6** (new) | `C01-entry-a.md:146-151` vs `:115-121`; `:217-219`; `C02-entry-b.md:109-110` vs `C01-entry-a.md:164,204`; `C03-entry-c.md:73-106` | Method redundancy: the "register audit — five questions" restates the test's own "test question" column; §3.7 restates the §3 intro; C02's blank and boundary-line bullets restate C01's; C03 §10 re-describes mechanisms owned by §3/§5. | Cut the restatements, not the tables. One rule, one authoritative location, later sections cite it. |
| **M-D7** (new) | `C01-entry-a.md:111` vs `:132` | "Ground-indexed" is defined as "referent space" (`:111`) and then used as "ground-indexed, not earth-indexed" for star charts (`:132`). The property test's key term does double duty. | Define the term once as **referent-indexed** (or state "ground = referent space, never earth") and use it consistently. |

**Already repaired in the r48 fragments I could read:** the false-precision class is absent by construction from `M01-example.md` (its only conversion is 1:2,500 → 2.5 m, verified `python3 -c 'print(1*2500/1000)'` → `2.5`); the B4 ladder and B8 cosmography `:27` fixes are carried in `C02-header.md:8`; the example's update rule is stated once and tags DR-CT-01..09 — `M01-example.md` body: 27 lines, 9 unique `DR-CT` ids, `0` hits for the r47 contradiction strings (`after any storm|per levy year|not due until`). That is the right direction.

---

## 5. The r48 method fragments, judged

### 5.1 Head block — PASS

`C02-header.md`'s fenced block is 23 lines (my `awk` fence count = 23; its own claim at `C02-header.md:8`). Method-relevant contents:

- `- topic:` names the object as a **system** (the survey → projection → drawing → reproduction chain), lists all eight forms, and names the calibration posture. It reads as a register slot, not a map file.
- `- gap filled:` dispositions the neighbours and states the boundary against `cosmology-cosmography.md:27` — the competing-definition sentence R03's B8 required. The property move now has a defensible one-owner claim.
- `- scope:` states what the entry does not own, move by move.
- `- recheck:` names the triggers that would invalidate each method claim.

### 5.2 Worked example — PASS

`M01-example.md` is 27 body lines, 9 move rows. It demonstrates the chain rather than describing it:

- every move is tagged to a build step **and** a decision row (DR-CT-01..09);
- the update rule is stated once, in one cell, and Sheet B explicitly declines to restate it;
- the reversal (rockfall) forces a **new class**, not a corrected number — which demonstrates the entry's central method claim (a class boundary is a claim) rather than a drawing lesson;
- `NON-CANON` is in the heading and the opening sentence.

Method-fidelity verdict: **PASS**, conditional on the assembled entry keeping the DR-CT semantics the example tags (if r48 renumbers, the tags must be remapped, not dropped).

---

## 6. Right-size instruction: keep the moves, cut the restatements

The successor should be assembled from r47's tables, not rewritten. One admissible budget that keeps every method move and lands inside the house band:

| Block | r47 lines | Target | Instruction |
|---|---:|---:|---|
| Head block | — | 23 | Use `C02-header.md` as drafted. |
| §1 frame + boundary | 22 | 18 | Keep the 8-row boundary table and the one-owner statement; cut the fiction paragraph to one line. |
| §2 property test | 44 | 24 | Keep definition, 5-condition table, 9-object table; cut the duplicate register audit (`:146-151`). |
| §3 mechanisms | 79 | 14–18 | Convert the six subsections to one 6-row table with a "design lever" column; keep §3.8's 8-question reader checklist. |
| §4 classes | 53 | 24 | Keep the 8-form table with its "cannot show" column; compress materials to 3 lines; keep R1–R5 as one line each. |
| §5 chain | 107 | 22 | Keep chain table, weakest-link rule, instrument→form table, failure table; cut the prose elaboration and C02's restated §3 rules (`:109-110`). |
| §6 scarcity | 68 | 14 | Keep cost stack (6 rows), four regimes (4 rows), working/monument split (1 line), loop (2 lines). |
| §7 trade | 59 | 16 | Keep 6-role table (fix header), 4 products, 3 customers; compress organization models and training. |
| §8 warrant | 68 | 14 | Keep warrant chain (5 rows), authority ladder, 3 failure modes, contest rule; cut the eight-decision prose to the decision record. |
| §9 word fossil | 55 | 7 | Keep 6–8 word rows, the method rule, the false-fossil rule; cut the lexicon-builder. |
| §10 build order | 34 | 10 | Nine one-line steps; each names its output and failure, no re-description. |
| §11 example | 47 | 27 | Use `M01-example.md` as filed (27 lines). |
| §12 calibration | 35 | 12 | Keep 8–10 highest-value rows; drop rows already stated inline. |
| §13 decisions | 21 | 12 | 12 rows, one line each; no change beyond trimming. |
| §14 recheck | 21 | 5 | Keep the triggers only. |
| §15 scope | 19 | 4 | Keep the boundary reminders as one paragraph. |
| **Total** | **739** | **246** | **Cut 493 lines (66.7%); ceiling ~250.** |

Arithmetic checked: section targets sum to `246` (`23+18+24+14+24+22+14+16+14+7+10+27+12+12+5+4` with §3 at 14; at §3=18 the total is 250). This is a budget, not a prediction — the assembled file must be measured with `wc -l`.

**Must not be cut:** the five-condition test and its object table; the seven-link chain and weakest-link rule; the 8-form table's "cannot show" column; the cost stack + scarcity regimes; the 6-role/4-product/3-customer trade tables; the warrant chain; the 12 decision rows; one NON-CANON example. These are the method. The cuts above are restatements, prose elaboration, and reference rows that do not force a decision.

---

## 7. Binding method-fidelity gate for the assembled r48 entry

A draft passes this seat only if all of the following are true on the assembled bytes:

| # | Check | Command / evidence |
|---|---|---|
| M1 | **Property**: definition + a discriminating test + a disposition table with at least 6 objects, including the T-O contrast and a non-terrestrial referent | `grep -c '^| [1-5] |'` on the test table = 5; object table ≥ 6 data rows |
| M2 | **One term**: "referent-indexed" (or "ground" defined once as referent space), used consistently for the star-chart row | `grep -n 'earth-indexed\|referent-indexed\|ground-indexed'` returns one definition and no contradictory use |
| M3 | **Mechanism**: one chain table whose rows carry a forced decision; one weakest-link rule; every mechanism section ends in a lever | chain rows = 7; `grep -c 'Design lever'` ≥ 5 |
| M4 | **Arithmetic**: every conversion recomputed; no ratio stated without its operands | 0.2 mm at 1:50,000 = 10 m; 200 m = 20×, 100 m = 10× |
| M5 | **Classes**: the form table has a "what it cannot show" column; every form claimed as owned has a build row, or the build table is retitled to the forms it covers | form rows vs build rows; no "per form" over a shorter table |
| M6 | **Scarcity**: cost stack + ≥3 regimes + working/monument split | table counts |
| M7 | **Trade**: header count equals table row count; ladder cites `craft-artisan-lexicon.md:54-65`, never `:44` | count header word vs rows; `sed -n '44p'` must not be the ladder |
| M8 | **Demonstration**: one NON-CANON example; one update rule stated once; every example move tagged to a build step and a decision row | r47 contradiction strings = 0; `DR-CT` ids in example = all defined ids |
| M9 | **Decision record**: ≥9 one-line rows, each citing its build step; no duplicate semantics | row count; `grep -o 'DR-CT-[0-9][0-9]' | sort -u` |
| M10 | **Length**: `wc -l` ≤ 250; no rule stated twice across sections (grep the two duplicate sentences) | `wc -l`; duplicate-rule grep |

If M1–M10 pass, the entry does what a register entry must: it defines a register, gives its generative mechanism, types its objects, prices them, explains who owns them, and demonstrates the method once. If any fail, the claim's `after_required` ("audits PASS") is not met.

---

## 8. Limits and what I did not verify

- **No r48 body existed at my write cut**, so I could not certify the assembled entry's method. The gate in §7 is the certification contract, not a clearance.
- I did not verify external sources; my citations are all in-repo `path:line` or fragment lines read at the baseline. The external shelf is C08/C18's lane.
- I did not audit citation anchors generally (C04), boundary disposition row-by-row (C15), length/contract fields (C05), or the worked example's ten controls (C14). My findings overlap those seats only where method fidelity depends on them (B1, B7, B9, B4).
- The §6 budget is one admissible allocation. K01/C01 own the final skeleton; if they choose different section boundaries, the requirement is that the five moves and the demonstration survive and `wc -l` ≤ 250.
- No `run-validation.py` was executed; no git mutation; no network; no writes outside this path.

## 9. Commands run (reproducible)

```
git rev-parse HEAD                                  # a01405d...
find corpus/knowledge -name '*.md' | wc -l          # 223
ls corpus/knowledge/culture-material/*.md | wc -l   # 25
wc -l corpus/knowledge/culture-material/*.md | sort -n   # min 103, median 149, max 221
awk 'NR>=86 && NR<=286' reports/round-47/cov/C01-entry-a.md | wc -l   # 201
awk 'NR>=41 && NR<=401' reports/round-47/cov/C02-entry-b.md | wc -l   # 361
awk 'NR>=73 && NR<=249' reports/round-47/cov/C03-entry-c.md | wc -l   # 177
grep -c '^| [1-7] |' <chain table>                  # 7
grep -c '^| [1-5] |' <test table>                   # 5
grep -c 'Design lever' reports/round-47/cov/C01-entry-a.md   # 6
sed -n '107,152p' reports/round-47/cov/C03-entry-c.md | grep -c 'DR-CT-'  # 0
grep -c '^| DR-CT-' <decision table>                # 12
sed -n '97,103p' reports/round-47/cov/C03-entry-c.md | grep -c '^| '     # 5 build rows
sed -n '240,249p' reports/round-47/cov/C01-entry-a.md | grep -c '^| \*\*' # 8 forms
sed -n '224,231p' reports/round-47/cov/C02-entry-b.md | grep -c '^| \*\*' # 6 roles
python3 -c 'print(0.2*50000/1000, 200/10, 100/10)'  # 10.0 20.0 10.0
python3 -c 'print(1*2500/1000)'                     # 2.5
awk '/^```markdown$/{f=1;next} /^```$/{f=0} f' reports/round-48/cov/M01-example.md | wc -l  # 27
awk '/^````markdown$/{f=1;next} /^````$/{f=0} f' reports/round-48/cov/C02-header.md | wc -l # 23
```
