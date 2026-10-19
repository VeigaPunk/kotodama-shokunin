# X02 — honesty audit (round 47, claim cross)

- Seat: **X02** | role: critic | claim: **cross**
- Out path: `reports/round-47/cross/X02-honesty.md` (the only repo path this seat wrote)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`), equal to
  `reports/round-47/claims.json:7` and to the commit time `2026-10-19T14:46:42-03:00` = `17:46:42Z`
- Observation window: `2026-10-19T17:47Z`–`18:03Z`; the census below is a snapshot at `18:03Z`
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; read-only git and
  read-only runs of the r44 scratch prototype. No network, no install, no commit, no corpus write,
  no `reports/round-*/run-validation.py` execution.
- Mission (`reports/round-47/targets.json:57`): every claimed number measured not asserted
  (223→224, gate selftest count, reconciliation rows); flag "should work"; verify no seat wrote
  outside its out path and nothing under `corpus/`.

**Verdict at a glance.** The baseline numbers are measured true. The three axis claims are
**not yet measurable as after-states**: no cartography file has landed (223, not 224), the durable
freshness gate does not exist, and the queue-successor artifact is not assembled. Every seat that
was asked to verify one of those after-states and had none to measure said so honestly
(`V01`, `O10`, `O13`), which is the correct behavior. One filed verifier artifact nevertheless
contains a **slot-swapped post-landing vector** (`C05`), and the contract contains three
**overstated or under-specified phrasings** (`C` "0 prior-round proposals"; `O` "r43 and r44 both
… stale premises"; `Ca` "5 carried defects"). Details and exact fixes follow.

---

## 1. Baseline — measured, not asserted

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

| partition | files | sum check |
|---|---:|---|
| linguistics | 25 | |
| myth-symbol | 26 | |
| culture-material | 25 | |
| synthesis | 29 | |
| verification | 24 | |
| civilizations | 94 | |
| **total** | **223** | 25+26+25+29+24+94 = **223** |

```
$ python3 -B reports/round-28/readme/sweep.py --json
exit=0; ok=true; total_rows=223; total_files=223; totals_line=223
footer: total 223, dir_totals [25, 26, 25, 29, 24, 94]
missing_from_index=[]; topic_mismatch=[]; orphan_rows=[]; header_drift={}
readme_sha256=7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

`sha256sum corpus/README.md` reproduces `7c788a1d…1ef31cdcd`. The round's contract digests also
reproduce: `reports/round-47/claims.json` = `7eb16979…1fa34`,
`reports/round-47/targets.json` = `d60e5572…ca3d`, matching
`reports/round-47/telemetry/dispatch-declared.json`. `targets.json` defines **64 unique seat ids
and 64 unique out paths**; 3 contract/telemetry files plus **25 of the 64 seat outs** were filed at
the `18:03Z` snapshot (24 seat outs at `18:01Z`; the round was still filing). The remaining 39
seat out paths were **absent**, not failed — see §7.

---

## 2. Numeric ledger — declared vs measured

| # | quantity | declared | measured at `6e9a30d` | verdict |
|---|---|---|---|---|
| 1 | total entries | 223 → 224 | **223** live and in the `6e9a30d` tree | pre-state true; **224 not yet measured** |
| 2 | culture-material | 25 → 26 | **25** | pre-state true; 26 forecast only |
| 3 | myth-symbol / synthesis / verification / civilizations / linguistics | 26 / 29 / 24 / 94 / 25 | **26 / 29 / 24 / 94 / 25** | true |
| 4 | README footer vector | `25/26/25/29/24/94` | `corpus/README.md:548` = same; sums 223 | true |
| 5 | rev-2.4 prose vector defect | "sums 217 not 223" | `corpus/README.md:11`: `25/23/25/29/24/94 → **25/23/26/25/24/94**`; second tuple sums **217** | **confirmed** |
| 6 | required post-landing vector | "sums 224" | correct tuple is `25/26/26/29/24/94` = **224** | forecast; **slot-verified, not sum-only** |
| 7 | C05's post-landing vector | `26/26/25/29/24/94` (`C05:273,275,295`) | sums **224** but slots are `linguistics=26, culture-material=25`; both are wrong | **FAIL — slot-swapped** |
| 8 | cartography filename owners | 0 | 0 exact vocabulary matches; 3 broad false positives (`dialect-faction-map-workflow.md`, `sacred-topography-pilgrimage.md`, `sacred-kingship-mythic-charter.md`) | true |
| 9 | cartography topic-line owners | 0 | exact pattern 0; broad 11 hits all metaphor/verb/handoff | true |
| 10 | prior-round proposals | "0" | **0 claim proposals before r44; 1 prior scout naming (r44 K02 itself)** | **literal phrase false at r47** (§4.1) |
| 11 | cartography body mentions | by-product only | 2 files / 3 lines: `cosmology-cosmography.md:71,:102`; `mesoamerica-primary-sources.md:58` | true |
| 12 | C04 corpus sha pins | 9 sha256 pins | all **9/9** match the live bytes (script in §4.2) | true |
| 13 | C04 `- couples:` tokens | resolve | **21/21** unique-basename or entry-dir-relative resolve | true |
| 14 | C01/C02/C03/C04 fence parity | fenced drafts | 14 / 6 / 6 / 10 fence lines, all even | true (no unclosed fence) |
| 15 | durable gate | `tools/harness/claims-freshness.py` | **ABSENT** at `18:03Z` | **could-not-evaluate** |
| 16 | prototype selftest | "red 17/19" | `sha256 dd88d9e1…`; `--selftest` → `selftest 17/19 FAIL`, exit 1 | true |
| 17 | prototype r43 verdicts | O and C stale, Ca fresh | **O STALE (0/2), C STALE (2/3), Ca FRESH (1/1)**; `REFUSE`; exit **2** | flags true; **exit code wrong** (§5.1) |
| 18 | prototype r44 negative control | r44 O fresh | **O FRESH (3/3)**; but the same file's C flags STALE (2/3) by mining the claim body | O control true; C overreach noted |
| 19 | r40 queue parent pin | `dfc9265d…` | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` | **unchanged** |
| 20 | r43 successor pin | `77f9d63e…` | `77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38` | true |
| 21 | resolver body pin | `43ce341f…` | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`; `--selftest` → `27/27`, exit 0 | true |
| 22 | Ca04 telemetry sha prefixes | 8 prefixes | all **8/8** reproduce (truncated to 12 chars) | true |
| 23 | requested seats vs observed launches | 64 requested | 64 seat definitions; **no `telemetry/observed-dispatch.json`** at cut | observed launch count **null** |

The two numbers this seat most wants kept separate: **223 → 224 is a forecast**, and **64 requested
is not 64 observed**. The round's own telemetry file is `dispatch-declared` only. Do not write
"64 workers ran" in LOG/SHONEN; record requested 64, observed `null`/could-not-evaluate until an
`observed-dispatch` sample exists.

---

## 3. Claim C — coverage

### 3.1 The gap is real and unowned; the "0 prior-round proposals" phrase is not literal

Independent re-run of the exact ownership tests:

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' \
    -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|survey map|world map)' corpus/knowledge/ | wc -l
0
$ grep -rliE 'cartograph|mapmaking|map-making' reports/ | wc -l
27 (all r44 seed/downstream, r47 seats, and unrelated supplement scratch)
```

Restricted to rounds 1–46, the only file that names cartography is
`reports/round-44/scout/K02-gap-scout.md`, the cited seed. There is no prior claim, no prior draft,
and no prior landing (`reports/round-44/validation.json:9` says "cartography … has no entry body").
So the ownership verdict is green.

But `claims.json:26` and `:34` say **"no prior-round proposal"** / **"confirmed 0 prior-round
proposals"**. At r47, r44 K02 *is* a prior-round scout file that names the gap. `K01` measured this
and flagged it (`reports/round-47/scout/K01-gap-recheck.md:10,243-247,306`). The honest wording is:
**"0 proposals before r44 K02; r44 K02 is the cited seed, never drafted or landed."** This does not
block the landing; leaving the unqualified phrase in LOG/SHONEN would be an accuracy defect.

### 3.2 The post-landing vector: sum equality is not slot equality

`C05` (`reports/round-47/cov/C05-freshness.md:273`) correctly diagnoses the rev-2.4 defect
(220 → 217, not 223) and correctly names the live footer. It then predicts the post-landing vector
as **`26/26/25/29/24/94`** at `:273`, `:275` and `:295`. That tuple sums to 224, so an
arithmetic-only threshold passes it — but the slot order is
`linguistics / myth-symbol / culture-material / synthesis / verification / civilizations`
(`reports/round-28/readme/sweep.py:39-46`). Culture-material moves 25 → 26 in **slot 3**;
linguistics stays 25 in **slot 1**. The correct tuple is **`25/26/26/29/24/94`**.
`C10` independently caught the collision (`reports/round-47/cov/C10-sweep.md:184-206`) and measured
the consequence: feeding C05's tuple to the staged sweep yields
`FOOTER_DIR_TOTALS declared [26,26,25,29,24,94] vs live [25,26,26,29,24,94]`, `ok False`.

This is the single most important procedural finding in the round: **the C threshold's phrase
"the README prose vector sums 224" is too weak to reject the exact defect C05 made.** The acceptance
check must compare the post-arrow tuple slot-by-slot to the live partition order (code in §8.3),
and the integrator must use C10's order, not C05's. `C10`'s own §5 check is still sum-only; it
catches this case only because its staged footer check separately compares slots. Add the slot
check to the prose-vector leg.

### 3.3 What C has actually proved, and what it has not

Proved at `6e9a30d`:

- 223 entries, culture-material 25, sweep green 223==223, footer correct;
- target path absent in worktree, index and HEAD; landing class **A**, not **M**
  (`C05` §7's throwaway-clone `git add` test is sound);
- sort slot between `calendar-festival-systems.md` and `costume-semiotics.md`;
- 9/9 C04 corpus sha pins match live bytes; 21/21 couples tokens resolve;
- C01 §1–4, C02 §5–9, C03 §10–15 and C04's head are all present as even-fenced drafts at the cut.

Not proved: **224**, culture-material 26, a green 224 sweep, the rev-2.5 prose, and the landing-time
re-ownership sweep. `C10`'s stage (`0ab794d8…`, 145,595 bytes) and `V01`'s stage are **staged
proofs, not live measurements**; both seats say so (`C10:6-11,195-204`; `V01:9-15,238-247`).
`V01`'s `PRE-LANDING / could-not-evaluate` verdict is the correct honest verdict, not a failure.

`C07`'s "draft bytes absent" rows (`reports/round-47/cov/C07-contract-audit.md:19-20,55-93`) were
true at its cut but are now overtaken by C01–C04. The contract audit must be re-run against the
assembled draft (C11/Q01) before the C clause can be called PASS; do not read C07's
`could-not-evaluate` rows as either PASS or FAIL.

---

## 4. Claim O — operability

### 4.1 The durable tool does not exist; do not report its after-state

```
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
```

Only scratch builds exist (`.scratch/ca01/claims-freshness.py`, `.scratch/o08/…`,
`.scratch/o05/…`). Under the shared rules no seat may write `tools/`, so the durable artifact is an
**integrator apply**, and the O claim is `could-not-evaluate` at this cut. `O10` and `O13` both say
so explicitly (`O10:12-19`; `O13:20-23`), and `V02` is the post-apply verifier. Any final report
that calls O "green" without a run of the durable path is theater.

### 4.2 The r43 verdicts are independently reproducible — and why they must not come from literals

I ran the r44 prototype read-only on `reports/round-43/claims.json`:

```
[O] operability -- STALE (0/2 premises hold)
  E1a-absence: "no durable instrument implements the r39 basename-couples policy" -> 2 family candidates
  E1b-scratch-only -> 2 family candidates
  (2 clauses ungrounded)
[C] coverage -- STALE (2/3 premises hold)
  E2b partition count 26 = hold; E2a total 223 = hold
  E3a "lithic slot … unbuilt" -> 3 owner hits in mineral-stone-symbolism.md
[Ca] calibration -- FRESH (1/1 premises hold)
  path reports/round-43/calib/dispositions-r38-r39.json absent at 7ceff59
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
REFUSE; exit 2
```

The measured baseline facts behind those flags:

- `7ceff59a0216a8ea21ee43262d9fc72abf770cee` tree contains
  `tools/harness/couples-reference-extractor.py` (sha `d8d23a26…`), whose selftest is **green**
  including "block read yields 4 tokens", and whose live census is
  `entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1`,
  with the one wrapped field reading **4/4** (`phonetics-phonology.md`). Therefore r43 O's clauses
  "no durable instrument implements the policy" and "the wrapped field reads 0/4" are **false**.
  A literal `path_absent` on `basename-couples-resolver.py` would have been true and would **not**
  have flagged — the flag must be a capability probe on the existing extractor. That is exactly the
  anti-theater requirement.
- The `7ceff59` tree contains `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, whose H1
  and `- topic:` own the lithic register. r43 C's `count_eq(26)` and `count_eq(223)` are both true;
  only the **ownership** probe flags. A count-only gate flags 0 of 2 stale claims.
- The `7ceff59` tree has **no** `reports/round-43/calib/` directory; the four r38/r39 queue rows
  remain `carried-with-owner` with no per-finding disposition record. r43 Ca's premise is true → FRESH.

The prototype's O flag is **not clean**: its `tool_family_absent` probe counts
`tools/gates/provenance-audit.py:12` (a gate that merely mentions a missing `- couples:` header) as
a resolver witness. The flag still stands because `couples-reference-extractor.py` is a genuine
witness, but the durable tool must not inherit this false positive; `O13` measured it as
`FAIL no_dead_kinds / contract_complete / registry_declared_and_complete` (`O13:21-23,57-75`).
`O13` also measured that the prototype has 13 implemented kinds but only 7 exercised, lacks
`capability_present` and `topic_owner_absent` under their contract names, and **downgrades unknown
kinds to STALE instead of rejecting them as malformed**. The durable tool's selftest must fix all
three.

### 4.3 Negative control and exit codes

- The r44 O claim is the negative control: at `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`,
  `tools/harness/basename-couples-resolver.py` is **absent** and the six-class extractor is the only
  couples tool. The prototype returns `[O] FRESH (3/3)`, which is correct.
- Caveat: run the control on an **O-only** claims file. On the whole r44 file the prototype also
  returns `[C] STALE (2/3)` and `REFUSE` — but that flag is a **false positive**, not a stale
  premise: its prose miner extracts the pronoun **"its"** from r44 C's sentence "the r43 lithic
  claim was blocked because its topic was already owned" and matches **64 owner hits**, while the
  real `lithic` clause is correctly measured true. `reports/round-47/calib/Ca01-stale-premises.md:129-160`
  and `Ca05:56-80` both classify r44 C as a **carried-candidate** defect, not a stale `before`
  (r44's three `before` fields are all true at `c9f4eaa`). The durable gate must evaluate declared
  `before_checks` only, never free prose, or both the negative control and the r43 C flag become
  uninterpretable.
- Exit codes: the prototype uses **stale → 2**; the contract requires stale → **1**, malformed →
  **2**, could-not-evaluate → non-zero, fresh-all → 0 (`reports/round-44/review/R01-review.md:246`;
  `O10:26-33`). `O10` built and calibrated a 14/14 suite against a compliant double and got 11
  failures against the prototype. That is a correct negative result, not an O deliverable.

### 4.4 The `before` paragraph overstates r44

`reports/round-47/claims.json:40` says: *"r43 and r44 both declared claims on stale premises
(green resolver existed; owned/carried topics)"*. Measured against r44's own file at `c9f4eaa`:

| r44 claim | `before` true at `c9f4eaa`? | actual r44 defect |
|---|---|---|
| O | **yes** — no four-class authority existed | none; O landed and improved |
| C | **yes** (before fields) | claim body re-proposed a carried topic (dream, named r42 K02) — a carried-candidate defect, not stale-premises |
| Ca | **yes** — no mechanical check existed | delivery failure (`validation.json`: `durable_gate_exists: false`) |

`Ca01:131-160` and `Ca05:56-80,208` found this independently. The r43 regression itself is
unaffected (O and C are genuinely stale at `7ceff59`), but the sentence must not be copied into
LOG/SHONEN as measured fact. Write: "r43 O and C were stale at `7ceff59`; r44 C was a
carried-candidate failure one class over; r44 O and Ca were true-premise but undelivered."

---

## 5. Claim Ca — calibration

### 5.1 The "five" is a constructed partition, not the retrospective's own five

The retrospective's carried list (`reports/round-46/loop-1-retrospective.md:43-53`) has **five
bullets**:

1. the `R01-43-12`-class freshness gate;
2. the stale-premises pattern (r43 and r44);
3. the resolver blank/hyphen latent edge;
4. antigravity lanes non-functional;
5. zai exhausted → luna-max.

The claim's five-row set is: stale-premises (Ca01), resolver edge (Ca02), **MANIFEST schemas**
(Ca03), antigravity outage (Ca04), zai-exhaustion (Ca04). Four retrospective bullets map into
Ca01/Ca02/Ca04 (bullets 1+2 merge into Ca01); the fifth row, **MANIFEST schemas, is not in the
retrospective's carried list at all** — it comes from `reports/round-46/audit/Ca01-manifest.md:7-8`
and the r46 review. `Ca03` states this provenance correction itself
(`reports/round-47/calib/Ca03-manifest-schemas.md:25-37`), and `Ca05:204-209` (F1) adds that r46 is
also a per-lane MANIFEST row, so "43–44" is already stale as a boundary.

There is **no silently dropped retrospective item** — that part of the threshold is met. But the
claim's phrase *"loop-1 retrospective names 5 carried defects/amendments"* is not a one-to-one
enumeration. The honest statement is: "the retrospective has five bullets; this successor carries
four classes for them plus one r46-audit schema item, five rows total."

### 5.2 Rows measured

- **Ca01**: `routed-with-owner` to the O claim; correct while the gate is absent
  (`Ca05` F4 calls upgrading it `fixed-with-evidence` now a class error). The r43 O/C measurements
  reproduce (§4.2). Its narrow-vs-broad incidence note (r43 only under the `before` definition;
  r44 C adjacent class) is the accurate reading.
- **Ca02**: resolver sha `43ce341f…` and selftest `27/27` reproduce; parent pin `dfc9265d…`
  reproduces. Its live-incidence claim (**0/223**) is a seat measurement; I did not independently
  re-run the scanner, but `Ca05` re-ran it and reproduced the fixture behavior. Class `recorded` is
  right: no fix, pinned body.
- **Ca03**: schema split S1/S2 is confirmed in-lane by `reports/round-46/audit/Ca01-manifest.md`
  (closure rows 33–42; per-lane 43/44, now also 46). The MANIFEST file itself is a fleet sibling;
  its sha `509305c8…` is **not independently verifiable from inside this repo** — mark `to-verify`,
  owned by the integrator. The item is a schema-evolution record, not a defect.
- **Ca04**: all eight cited telemetry sha prefixes reproduce in-lane. It correctly corrects the
  seat mission's "positions 12/13 skipped": **position 12 (r44) was re-routed to opencode-go and
  executed; position 13 (r45) was skipped** (`Ca04:58-98`). Provider quarantine/redirect state is
  correctly marked `to-verify` with an owner.
- **Ca05**: the independent verifier is strong and honest. Its row-presence table was accurate at
  its cut (Ca01/Ca03/Ca04 absent then); those rows have since filed, so **Ca05's
  `could-not-evaluate` cells are superseded, not final**. Its F1–F5 findings are the right
  should-fix list; F4 (do not upgrade the stale-premises row until the durable gate is demonstrated)
  is binding.
- **Ca06/Ca07** (successor assembly and integrity) were **not filed** at the cut. The Ca
  after-state (`reports/round-47/calib/queue-successor-r47.json` or `.md`) does not exist. Ca is
  therefore also `could-not-evaluate` as a deliverable, even though its factual rows are measured.

---

## 6. "Should work" and other language flags

I scanned every filed round-47 artifact for `should|presumably|probably|likely|assume`.

- Most hits are **design language** in plans/drafts ("should be preserved", "the assembler should
  choose one owner"), not measurement claims. No seat asserted a run it did not perform.
- The three verifiers that could have faked an after-state did not: `V01` explicitly says a
  post-landing PASS "would be theater" (`V01:9-15`); `O10` and `O13` mark the durable tool
  `could-not-evaluate`/absent (`O10:12-19`; `O13:20-23`).
- Real overclaims to fix in synthesis prose, not in seat artifacts:
  1. `claims.json:26,34` — "0 prior-round proposals" (literal false at r47; §3.1).
  2. `claims.json:40` — "r43 and r44 both declared claims on stale premises" (§4.4).
  3. `claims.json:53` — "the retrospective names 5 carried defects" as if the five rows were its
     enumeration (§5.1).
  4. `targets.json:49` — "positions 12/13 skipped" (Ca04 corrects it; §5.2).
  5. `C05:273,275,295` — slot-swapped vector (§3.2).
- `C10`'s and `V01`'s predictions are explicitly conditional on the landed bytes and are **not**
  presented as measured. Keep that framing in LOG/SHONEN: "staged 224 proof" ≠ "224 landed".

---

## 7. Write-surface census (snapshot `18:03Z`)

```
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ git status --porcelain -- corpus tools LOG.md SCORECARD.md
(empty)
$ git diff --stat
(empty)
```

- **No tracked file was modified.** `corpus/`, `tools/`, `LOG.md`, `SCORECARD.md`, `REGIMEN.md`,
  `PROVINCE.md` are byte-clean at the baseline.
- **Nothing was staged under `corpus/`.** Scratch staging exists only under `.scratch/` (C09's
  `tree224`, C10's stage, C11's stage, V01's mirror, O fixtures). That is permitted; the rule
  forbids corpus staging, not scratch.
- **Round-47 files:** 28 at `18:03Z` — 25 seat outs + `claims.json` + `targets.json` +
  `telemetry/dispatch-declared.json`. All 25 seat files map to a declared out path. Telemetry is
  the one non-out category and is explicitly required by `AGENTS.md`; it is not undeclared bleed.
- **39 seat out paths were absent**, including all of O01–O09/O11/O12/O14/O15, Ca06/Ca07, C06/C08/
  C09/C11–C14/W02, all reviewers, A01–A03, X01/X03, K03, S01/S03, Q01. This is a mid-wave
  snapshot; absence is **could-not-evaluate**, not failure. `A03` owns the close census.
- **Pre-existing untracked artifact (not r47's):** `reports/round-46/review/R01-review.md` is
  untracked and **absent from `6e9a30d`**; `X05` flags it as OBS-1 (`X05:324`). It is a filing gap
  in r46 (the review exists in the worktree but not in the commit chain). It is not cited by any
  r47 claim and did not affect the baseline; the integrator should either commit it in a later
  hygiene round or record it as a named exception. Do not cite it as baseline evidence.
- **My writes:** this file, plus `.scratch/x02-base/couples-reference-extractor.py` (read-only
  baseline copy) and `.scratch/x02-sweep-223.json`. No corpus, tools or filed-byte write.

---

## 8. Falsifiable post-integration checklist

Run these after the integrator applies C and O. Expected values are exact.

### 8.1 Census and sweep

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                              # record the apply-time sha
find corpus/knowledge -name '*.md' | wc -l      # 224
ls corpus/knowledge/culture-material/*.md | wc -l  # 26
python3 -B reports/round-28/readme/sweep.py --selftest   # 12/12, exit 0
python3 -B reports/round-28/readme/sweep.py              # rows 224 files 224, totals 224,
                                                         # footer 224 / 25/26/26/29/24/94, exit 0
```

### 8.2 Ownership post-check

```bash
test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo PRESENT
grep -n '^- topic:' corpus/knowledge/culture-material/cartography-and-mapmaking.md
# the entry's own topic must name the map/survey register; the README row must equal this
# text byte-for-byte (sweep.py topic_of), not a paraphrase
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|\bmap\b)' corpus/knowledge/ | wc -l
# pre-landing 9 (all metaphor/verb, dispositioned in K01/C05); post-landing 10 —
# the same 9 unchanged plus the new entry (its topic contains "the map as an instrument").
# Confirm none of the 9 becomes a second owner of the survey→sheet chain.
grep -rliE 'cartograph|mapmak' corpus/knowledge/ | wc -l   # pre 2; post 3 (new entry + 2 by-products)
python3 -B tools/harness/basename-couples-resolver.py --census
# entries=224; the 21 declared couples tokens resolve; no new unresolved/ambiguous token
```

### 8.3 Vector slot check (not a sum check)

```python
import re, sys, os
t = open("corpus/README.md", encoding="utf-8").read()
# live order from the README's own section headers
order = re.findall(r"^## ([a-z-]+)/ \((\d+)\)", t, re.M)
live = [int(n) for _, n in order]
print("live header counts:", live)                     # [25,26,26,29,24,94]
for rev, want in (("2.5", live), ("2.4", [25,26,25,29,24,94])):
    block = re.search(rf"revision: {rev}.*?(?=\nrevision: |\nround-28 C entry|\Z)", t, re.S)
    vecs = re.findall(r"\*\*(\d+(?:/\d+){5})\*\*", block.group(0)) if block else []
    if not vecs:
        print(f"rev {rev}: NO DECLARED VECTOR -> could-not-evaluate"); sys.exit(1)
    got = [int(x) for x in vecs[-1].split("/")]
    print(f"rev {rev}: {got} sum={sum(got)} slots_ok={got == want}")
    if got != want:
        sys.exit(1)
```

Expected: rev 2.5 `[25,26,26,29,24,94]`, slots_ok True; rev 2.4 `[25,26,25,29,24,94]`, slots_ok
True; exit 0. This rejects C05's `[26,26,25,29,24,94]` even though it sums to 224.

### 8.4 O gate

```bash
python3 tools/harness/claims-freshness.py --selftest
# must print its own N/N count and exit 0; any "N/N" cited in LOG must be pasted from this run
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json
# O STALE, C STALE, Ca FRESH; exit 1 (not 2)
python3 tools/harness/claims-freshness.py --claims <r44-O-only fixture>
# O FRESH; exit 0
python3 tools/harness/claims-freshness.py --claims <anti-theater mutation>
# still O STALE (capability/ownership), exit 1
python3 tools/harness/claims-freshness.py --claims <malformed>
# exit 2
python3 tools/harness/claims-freshness.py --claims <no-checks claim>
# non-zero (never 0)
```

Also verify the tool reads `git show 7ceff59:…`, not the worktree: a claim false in the worktree
but true at baseline must not be flagged; a claim true in the worktree but false at baseline must
be. `O11` owns this; `O08`/`V02` re-run it.

### 8.5 Ca successor

```bash
sha256sum reports/round-40/op/defect-queue-v2.json
# must still be dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
python3 - <<'PY'
import json
d=json.load(open("reports/round-47/calib/queue-successor-r47.json"))
rows=d["rows"]
print(len(rows), [r["id"] for r in rows])
PY
```

Expected: five rows covering (1) R01-43-12 routed to the O tool, (2) resolver latent edge recorded,
(3) MANIFEST schemas recorded (with the r46 scope qualifier), (4) antigravity named deviation with
"pos 12 re-routed/executed, pos 13 skipped", (5) zai→luna-max named deviation. Each row: class +
owner + resolving citation; no `fixed-with-evidence` without a re-run command output. Then re-run
`Ca05`/`Ca07` against the filed bytes, not against the earlier absent-row snapshot.

---

## 9. Limits, and what this audit does not claim

- **39 of 64 seats were unfiled at the `18:03Z` snapshot** (25 filed). Later seats were still
  filing while this report was written; re-count at close. Every after-state depending on an
  unfiled seat is `could-not-evaluate`; the close census belongs to `A03`/`Q01`.
- I did not read the fleet `MANIFEST.json` (sibling, outside this repo); Ca03's external sha and
  row counts are `to-verify` for the integrator.
- I did not independently re-run Ca02's 0/223 incidence scanner; I did reproduce the resolver sha,
  its 27/27 selftest, and the parent pin.
- I did not execute anything under `reports/round-*/run-validation.py`; the r47 runner does not
  exist at the cut.
- No network, no external source inspection; the cartography shelf is `(to-verify)` throughout.
- The snapshot counts in §7 will be stale by close. Re-run the census command; do not copy this
  report's file count into LOG as the close count.

**Bottom line for the integrator.** Keep the three claims' current statuses separate:
C is **pre-state verified, after-state forecast**; O is **method verified, deliverable absent**;
Ca is **facts verified, successor not assembled**. The two must-fix accuracy items before any
LOG/SHONEN prose are the **slot-swapped vector** (§3.2) and the **"0 prior-round proposals"**
qualification (§3.1). The two must-fix acceptance items are **slot equality, not sum**, and a
**capability/ownership probe, not a literal path**, for the gate.

---

## 10. Post-snapshot addendum (`18:08Z`)

The wave kept filing after the §7 snapshot. At `18:08Z` there were **45 files** under
`reports/round-47/`: **42 of 64 seat outs** plus `claims.json`, `targets.json` and
`telemetry/dispatch-declared.json`. The new filings do not change the §2–§6 findings; three of them
strengthen or refine them:

- **C05's vector is now corroborated by three independent seats.** `C09`'s staged diff uses
  `25/26/26/29/24/94` (`cov/C09-readme.md:142,211,234`), `C11` records the same defect as D6
  (`cov/C11-scribe.md:147`), and `S01` records it as F-01 (`scribe/S01-integration-draft.md:105,382`).
  F-01 in this audit is therefore not a lone critic's arithmetic; it is a cross-seat reconciliation
  item. C09's diff is still a **draft** (`git apply --check` staged, live pending), so the
  224 after-state remains unmeasured.
- **The O method is independently reproduced, but the deliverable is still absent.** `O05` reports
  the r43 reference evaluator verdict **O STALE / C STALE / Ca FRESH, exit 1** (`op/O05-r43-demo.md:11-19`),
  with the correct observation that a literal `path_absent` gate would pass r43 O while a
  capability probe flags it (`:15,60`). `O06` reports the negative control **3/3 claims, 9/9
  clauses, exit 0**, plus the discriminator that the same control is STALE if evaluated in the
  worktree (`op/O06-negative-control.md:19-31,83-84`). `O12` states the honest bottom line:
  "assembled but not closed", candidate verdict `unprovable-but-better`
  (`op/O12-scribe.md:12-30`). At `18:08Z`, `tools/harness/claims-freshness.py` and
  `reports/round-47/calib/queue-successor-r47.*` are still **absent**; O and Ca after-states remain
  `could-not-evaluate`.
- **The §4.3 caveat is refined, not withdrawn.** O06's fixture is the right form of the control:
  all three claims carry declared `before_checks`, and the gate returns 3/3 fresh. The raw r44 file
  is not a valid control because the prototype's prose miner extracts the pronoun "its" and
  matches 64 owner hits. The durable gate must evaluate **declared clauses only**; this is the
  difference between O06's clean control and the prototype's false flag.
- **Not a C defect:** `S01:303` records the `corpus/README.md:1,3` duplicate H1 as the carried
  `R36-README-DUPLICATE-HEADING` and says not to repair it in the C delta. I measured the duplicate
  at the baseline (`head -3`), and the sweep does not read it. Leave it out of the C landing; it is
  a separate carried item, not part of the 223→224 arithmetic.
- **Write surface unchanged:** at `18:08Z`, `find corpus/knowledge -name '*.md' | wc -l` = **223**,
  culture-material = **25**, and `git status --porcelain -- corpus tools` is empty. No seat wrote
  to a filed byte or to `corpus/`; the close census still belongs to `A03`/`Q01`.

