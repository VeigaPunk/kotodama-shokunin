- Seat: R01 | reviewer | claim D | date 2026-10-19 | baseline ce103bf

# R01 — adversarial review of the D block: content authenticity and leg correctness

**Assignment** (`reports/round-36/targets.json`, seat `R01`): role `reviewer`, claim `D`,
mission verbatim: *"Adversarial review of the D block: content authenticity (no fabricated
linguistic claims — sources or to-verify), leg correctness."* Out path:
`reports/round-36/review/R01-d-review.md`.

- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`;
  `git status --porcelain` → `?? reports/round-36/` (no tracked byte moved by this seat).
- **Canon: NON-CANON.** This seat reviews bytes and reports. It admits no claim, certifies no
  round, promotes nothing. A green reading below is a structural reading at a named digest,
  never a verdict on scholarship, never canon (`PROVINCE.md`).
- **Writes**: this file only, plus gitignored scratch under `.scratch/r36-ro1/`. No `corpus/**`,
  no `tools/**`, no filed round-1..35 byte, no `.ufo/**`. No commit, push, install or network.
- **F-C13-1 / freeze rule honoured**: no `reports/round-*/run-validation.py` was executed
  in-tree or in a copy; no `--freeze` of `reports/round-34/handoff/declared-in-r7` was run. The
  only filed code executed is read-only gates and the read-only assembler `--selftest`.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | **Claim D's declared `before` state is false at baseline `ce103bf`.** The register-form domain is **non-empty**: `derived_pairs=8`, `register_scoped=14` | measured, §1 |
| 2 | The domain became non-empty at commit **`4f09c99`** ("round-26: admit D/O/C — register stratum closes the r17 forecast"); it was empty at r25 (`fc13cd2`) and at r26's own HEAD (`1ad491a`) | measured, §2 |
| 3 | `SCORECARD.md:329` already records the closure; the `EMPTY` text the claim quotes is `SCORECARD.md:312`, a **historical r25 row** | measured, §2 |
| 4 | The delivered content is **authentic, not fabricated**: all 175 packet evidence markers are `design-choice`; the packet is declared NON-CANON at `packet.d4.yml:2` and `components/04-lexicon.yml:11` | measured, §3.1 |
| 5 | Every one of the 8 forms **replays clean under my own independent implementation** (8/8) and is **phonotactically legal** under `PHON-01` | measured, §3.2 |
| 6 | All 8 `doublet_of` pointers **resolve to the correct base records** (0 dangling) | measured, §3.3 |
| 7 | The argot leg is **discriminating** (a single-base tamper → `D4L-ARGOT-DERIV`, exit 1); `register-law` leg is green | measured, §4 |
| 8 | **The claim's own `counting_commands` target does not exist yet**: `reports/round-36/run-validation.py` is absent, so claim D's threshold is unmeasurable as filed | measured, §5 |
| 9 | D01 and D03 **independently reach reading 1** on their own instruments; D01's constructive reroute (design the `doublets:` block and the two unimplemented legs, not the filed forms) is the right reading of the claim | §6.1 |
| 10 | **Correction: D03 §3.2's "an emptied domain is silent" does not reproduce.** Deleting the eight record blocks leaves the coverage hold firing — `D4L-ARGOT-COVERAGE: HOLD`, **exit 1**. The r25 failure mode is closed, not reproduced | measured, §6.2 (finding **R01-D-1**) |

**Bottom line for the integrator.** Claim D cannot verify as filed: its falsifiable before→after
has already happened, one round earlier than the claim asserts. This is not a content defect and
not a leg defect — it is a **claim-scope defect**. The adjacent, genuinely open item is the
`head2` empty proper domain (`RL-2`), which is carried in the round-33 ledger with an owner and
which D01 §3 effectively drafts; the integrator decides whether to reroute D onto that. One
correction is owed to the D block itself (**R01-D-1**, §6.2), and it runs in the *favourable*
direction: the coverage hold does catch an emptied domain.

## 1. The load-bearing measurement — claim D's `before` is false

Claim D (`reports/round-36/claims.json:20-26`) declares:

> `"before": "Register-form domain empty (reports/round-25/argot/ + SCORECARD r25 row); register
> law/strata exist but the form class has no instances"`

Measured on the delivered tree at `ce103bf`, with `export TMPDIR=$PWD/.scratch`:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
EXIT=0
```

The gate's own coverage line reports **`derived_pairs=8`** and **`register_scoped=14`** — the
form class has eight instances, each carrying a `derived_from` pointer and a `derivation` pair.
The bytes:

```
$ grep -c "derived_from" examples/culture-d4/packet.d4.yml   → 8
$ grep -c "doublet_of"   examples/culture-d4/packet.d4.yml   → 8
$ grep -c "derivation:"  examples/culture-d4/packet.d4.yml   → 8
$ grep -c 'register: "stamp"' examples/culture-d4/packet.d4.yml → 20 = 8 lexicon forms (L-55..L-62) + 7 `registers:` rows (QREG-02..08) + 5 `register_law:` rows
```

The eight form records are `L-55..L-62`, authored at
`examples/culture-d4/components/04-lexicon.yml:220-243` under the comment
`# ---- the stamp register: register-scoped forms (8) ----`, and merged into the packet at
`examples/culture-d4/packet.d4.yml:1019ff`. Each carries the full field set, e.g. `L-55`
(`packet.d4.yml:1010-1029`):

```
    term: "kit"
    register: "stamp"
    derived_from: "tik"
    derivation:
      op: "reverse"
      base: "tik"
    doublet_of: "L-42"
```

The `registers:` block is present at `packet.d4.yml:1329` with the eight `QREG-01..08` rows, and
`contract.record_fields.registers` declares the field set at `packet.d4.yml:46-54`. So the claim's
`before` — "the form class has no instances" — is contradicted by the delivered bytes.

The claim's `after_required` ("register-form domain non-empty with verified forms; derivation
replay clean over the new forms; law gate exit 0") **already holds** at baseline. A claim whose
before-state equals its after-state cannot verify.

## 2. When it closed, and why the claim's citation is stale

The transition is datable from the packet bytes across the ledger:

```
$ for c in fc13cd2 1ad491a 4f09c99 6c0ac44 ce103bf; do
    echo -n "$c derived_from="; git show $c:examples/culture-d4/packet.d4.yml | grep -c "derived_from"; done
fc13cd2 derived_from=0        # round-25 admit
1ad491a derived_from=0        # round-26 worktree HEAD (claim D's own baseline)
4f09c99 derived_from=9        # round-26 admit
6c0ac44 derived_from=9        # round-27 admit
ce103bf derived_from=9        # round-35 admit — current
```

The landing commit is `4f09c99` ("round-26: admit D/O/C — register stratum closes the r17
forecast; r5 pin chain (devin)"); `git log -S"derived_from" -- examples/culture-d4/packet.d4.yml`
returns exactly that commit.

**The claim quotes a historical row as if it were the current state.** The `EMPTY` text is
`SCORECARD.md:312` — the **round-25** row, whose measured evidence is `reports/round-25/argot/`
at packet `e7ecd204…`. That statement was **true when filed**: at `fc13cd2` the packet carried
zero `derived_from` (above), and `reports/round-25/argot/execution-4.md:79` records
`derived_pairs=0`. Round 26 then closed it, and `SCORECARD.md:329` says so in terms:

> `depth | improved (claim D, capability register-stratum) | The round-17 register forecast CLOSED:
> the stamp attestation register lands in the delivered furnace-league tree — 8 verified register
> forms (tuum/kit/lom/nees/huum/mees/reek/saam) … derivation replay clean (8 derived pairs, 0
> violations over 170 records)`

`reports/round-26/register/review.md:1` (its own summary line) reads *"8 of 8 forms clean, the
required control `D4L-ARGOT-DERIV` fires"*. So the r25 record was closed in r26 and the claim's
`before` describes the r25 tree, not `ce103bf`.

**One narrower reading does survive, and it is worth stating precisely.** The *forecast's exact
mechanism* — the `<id>#plain` / `<id>#quote` slot pair of `Δ1` class 2 — is still absent:

```
$ for p in '#plain' '#quote' 'slot_ref' 'doublets'; do echo -n "$p -> "; grep -c -- "$p" examples/culture-d4/packet.d4.yml; done
#plain -> 0
#quote -> 0
slot_ref -> 0
doublets -> 0
```

But round 26 recorded, with a measurement, that the register had to be **re-hosted on the
furnace-league's own record set** rather than re-lettered (`reports/round-26/register/review.md`
§2, finding `RD-1`: the forecast's `AL-`/`GD-`/`QN-` where-keys do not exist in the delivered
tree), and it declared the forecast closed on that basis. The mechanism gap is therefore a
**recorded and dispositioned design decision**, not an "empty domain" — and the claim's
`after_required` does not ask for the slot mechanism anyway; it asks for "verified forms", which
exist.

## 3. Content authenticity — no fabrication found

### 3.1 Provenance class

Every record in the packet carries a design marker, never an attestation:

```
$ grep -o 'evidence: "[a-z-]*"' examples/culture-d4/packet.d4.yml | sort | uniq -c
    175 evidence: "design-choice"
```

Zero `attested` / `borrowed` / `source` markers. The packet self-declares NON-CANON twice
(`packet.d4.yml:2` `canon: "not canonized (D4 NON-CANON design drill)"`; `components/04-lexicon.yml:11`
`canon: not canonized (D4 design drill)`) and its header at `:3` states *"NON-CANON: this file
proposes a design; it records nothing about any world."* The `follows:` cells point at real,
resolvable corpus method files and real component ids — I verified `F-2` is a live component id
(`components/02-phonology.yml:27`), not a dangling reference, despite appearing 27 times as a
`follows` target in the packet. No linguistic claim about any real language is made: the eight
forms are glossed as design objects ("the mark itself, spoken"), and the etymologies are
design-internal ("reverse of tik (L-42 mark, stamp)").

### 3.2 The forms are arithmetically and phonotactically sound (independent replay)

I re-implemented the two operations myself rather than reading the gate's verdict
(`.scratch/r36-ro1/`):

```
L-55 kit  <- reverse(tik)    = kit   OK
L-56 lom  <- reverse(mol)    = lom   OK
L-57 tuum <- lengthen(tum)   = tuum  OK
L-58 nees <- lengthen(nes)   = nees  OK
L-59 huum <- lengthen(hum)   = huum  OK
L-60 mees <- lengthen(mes)   = mees  OK
L-61 reek <- lengthen(rek)   = reek  OK
L-62 saam <- lengthen(sam)   = saam  OK
replayed 8 of 8
```

Independently, I checked each form against the declared template `(C)V(V)(C)` with the eight
codas `[n,m,s,k,l,r,t,d]` (`components/02-phonology.yml`, `phonotactics_record: PHON-01`): all
8 forms are legal. The rule that selects the operation is the delivered record's own `axis`
(`mark → reverse`, `fire → lengthen`), and the axis values I read off the packet match the
operations used in every row.

### 3.3 No dangling pointers

```
$ python3 -B -c "…id→term map over the packet…"
L-55 doublet_of L-42 -> term='tik'  OK
L-56 doublet_of L-38 -> term='mol'  OK
L-57 doublet_of L-02 -> term='tum'  OK
L-58 doublet_of L-16 -> term='nes'  OK
L-59 doublet_of L-09 -> term='hum'  OK
L-60 doublet_of L-43 -> term='mes'  OK
L-61 doublet_of L-37 -> term='rek'  OK
L-62 doublet_of L-39 -> term='sam'  OK
```

8/8 `doublet_of` targets resolve, and each resolves to the same base the `derivation.base`
names. `L-55..L-62` are new ids (the packet's lexicon is 62 records), so the landing added
records rather than overloading existing ones.

## 4. Leg correctness

**The argot leg is discriminating, not a vacuous pass.** I tampered exactly one record — `L-55`'s
`derived_from`/`derivation.base` from `tik` to `mes` — in a scratch copy and re-ran the gate:

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/r36-ro1/tamper.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kit' (register 'stamp'): declared chain 'reverse' applied to 'mes' yields 'sem'; the stated inputs and rules do not yield the candidate
coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=1 rule_holds=0
EXIT=1
```

Exit 0 on the clean packet is therefore a real pass, not the structural pass-on-empty that r25
correctly flagged (`reports/round-25/argot/execution-4.md:110`).

**Selftests and sibling legs:**

| leg | command | result |
|---|---|---|
| argot selftest | `python3 -B tools/gates/argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed`, exit 0 |
| register-law selftest | `python3 -B tools/gates/register-law-gate.py --selftest` | `selftest: 45/45 checks passed`, exit 0 |
| register-law over packet | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0`, exit 0 |
| typed pipeline | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed`, exit 0 |
| typed-labels projection | `python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | `byte-identical deterministic projection`, exit 0 |
| deterministic assembly | `python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | `byte-identical deterministic assembly`, exit 0 |
| assembler selftest | `python3 -B tools/assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed`, exit 0 |
| battery | `python3 -B tools/check-gate-battery.py` | `battery_exit 0, pass 7, fail 0, unevaluable 0` |

The two named round-26 leg defects are **both closed**, which I confirmed rather than assumed:
`RD-4`/`RL-3` (the gate's `syllabify` disagreed with the design's legality-constrained
maximal-onset rule on 15 of 62 forms) was fixed in round 27 — the current
`tools/gates/argot-derivation-gate.py:153-175` implements the legality test and documents that
the clause "is load bearing, not decoration"; and `RD-5c` (no component owned the register law)
was fixed in round 27 by `components/13-register-law.yml` + the `register_law` packet block,
which is why `register-law-gate` now finds `law_rows=5`.

**Pin state.** The only frozen baseline for the law gate,
`tools/gates/expected/register-law-gate/r30-post/expected.json`, pins
`inputs["examples/culture-d4/packet.d4.yml"] = aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`,
which **equals the current packet digest** (`sha256sum examples/culture-d4/packet.d4.yml` →
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`). I checked this is not a
stale-pin accident: the packet digest has been `aac91246…` from `71cd9d3` (round-30 admit)
through `ce103bf` (round-35), so the r30-post baseline is current and no supersede row is owed.
The r30 "before" digest `543d68a8…` in `reports/round-30/fixes/qreg-dangles.md:29` is the
pre-landing r29 state and is correctly recorded as such. `tools/gates/typed-pipelines.json`
profile `d4` likewise pins `aac91246…`.

**One correction I owe against my own first pass.** I initially invoked
`d4-typed-labels-check-gate.py examples/culture-d4/packet.d4.yml` and read its exit 1
("differs from the deterministic projection") as a drift defect. That was **my** argument error:
the adapter's own usage is `d4-typed-labels-check-gate.py [PROJECTION]`
(`tools/gates/d4-typed-labels-check-gate.py:42`), so passing the packet compares the packet
against itself-as-projection. With the documented projection path the gate exits 0 (§4 table).
No defect; recorded so the error is not inherited.

## 5. The claim's threshold is unmeasurable as filed

Claim D's `counting_commands` is `["python3 -B reports/round-36/run-validation.py"]`, and its
threshold is "forms verified by two independent seats; replay/law/typed legs green; zero
filed-byte edits". At review time:

```
$ find reports/round-36 -type f | sort
reports/round-36/claims.json
reports/round-36/cov/C01-audit.md
reports/round-36/targets.json
reports/round-36/telemetry/availability-attempt-1.json
reports/round-36/telemetry/dispatch-declared.json
```

`reports/round-36/run-validation.py` does not exist, so the claim's own counting command cannot
run. This is expected mid-wave (S01 owes the validation-leg spec) and is not a defect — but it
means claim D's acceptance cannot be evaluated until the runner lands, and even then the runner
would measure an already-satisfied after-state.

## 6. Second pass on the landed D drafts (D01, D03)

Sections 1–5 bind to the delivered baseline bytes. The D drafts landed while this review was being
written, so this section adds a second pass over the two that exist — **D01** (`depth/D01-design.md`)
and **D03** (`depth/D03-isolated-verify.md`). **D02** (packet draft) never landed; **D04–D10** did
not exist at this read (`find reports/round-36 -type f`).

### 6.1 Agreement on the headline — reached independently, four ways

D01 §0 and D03 §1 both state, in their own words, that claim D's `before` is stale, and both
measure it. That is four independent arrivals at my §1 verdict (mine, D01's, D03's, and the sibling
reviewers R02 §2 / R03 §2), on three different instruments: my gate run + grep census, D01's
`git log -S` + table, D03's `load_yaml` parse + own re-derivation. D03's re-derivation of the eight
pairs (`term_match=True`, `base_rec` and `doublet_of` resolving in the same packet, `8/8 clean`)
independently reproduces my §3.2/§3.3 findings. **No disagreement on the premise.**

D01's constructive response is also correct in kind: rather than re-authoring the eight filed
records (dead work that duplicates filed bytes), it designs the surface that is genuinely open —
the `doublets:` block, the base-side pointer, and the two unimplemented legs. That is the right
reading of the claim, and it keeps claim D alive as a depth move without re-landing r26's content.

### 6.2 Correction — D03 §3.2's "an emptied domain is silent" does NOT reproduce

D03 §3.2 reports a domain-emptied probe as `records=179 register_scoped=0 derived_pairs=0
claimed_chains=8 borrow_pairs=0 violations=0`, **exit 0**, and concludes: *"An emptied domain is
silent … This is the r25 failure mode reproduced exactly: a clean exit over an empty domain."*

I tested this directly. Deleting the eight `L-55..L-62` record blocks from a scratch copy of the
packet and re-running the delivered gate (`.scratch/r36-ro1/emptied2.yml`; scratch only, the packet
was never edited):

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/r36-ro1/emptied2.yml
FINDING D4L-ARGOT-COVERAGE: HOLD — packet declares the argot operation(s) head2, reverse and 6 register-scoped form(s), but no record carries a derived_from/derivation pair; the forecast derivation relation is declared, not delivered
coverage: … records=179 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
EXIT=1
```

**The coverage hold fires, at exit 1.** An emptied domain is **not** silent on the delivered gate.
So the r25 failure mode is **closed**, not reproduced — which is the opposite of D03's §3.2
conclusion, and it is the answer to the question D03 raised.

Root cause of the difference, measured (`tools/gates/argot-derivation-gate.py:662-667`): the hold's
guard is `declared_ops and counters["register_scoped"] and not counters["derived_pairs"]`. The gate
counts a record as register-scoped if it declares a `register`, **or its layer does**. Removing the
eight *records* leaves the two layer-level declarations intact — `LY-01 register: "trade"`,
`LY-02 register: "craft"` (`packet.d4.yml`, `layers:` block) — so six loan records stay
register-scoped and the guard is satisfied. My reading is `register_scoped=6`; D03 reports `0`.

Two things follow, and D03/D07 should reconcile them:

1. **D03's row is internally inconsistent.** It reports `records=179` (187 − 8, which matches my
   removal exactly) alongside `borrow_pairs=0`. But 179 records still contains the six borrowed
   records in `LY-01`/`LY-02`, and the gate reports `borrow_pairs=6` over that same population
   (my run). `borrow_pairs=0` with `records=179` cannot both hold on the delivered gate; either the
   transform removed more than the eight blocks, or the counter was read from a different state.
2. **D03's transform was not the one its row describes**, or its reading predates the coverage-hold
   wiring. Either way the *conclusion* it draws — that the gate is silent on an empty domain — is
   false against the delivered bytes, and it is the kind of conclusion that would wrongly license a
   "the leg cannot catch an emptied domain" claim in a later round. Flagged as **R01-D-1**.

**Independent corroboration.** R02 reached the identical result on its own instrument, as
**R02-D-8** (`reports/round-36/review/R02-d-review.md:279-318`): same transform, same
`register_scoped=6` / `borrow_pairs=6`, same fired `D4L-ARGOT-COVERAGE`, exit 1. R02 also names
the precise condition under which the *silent* pass would occur — the register **declarations**
(`LY-01`/`LY-02`) must be stripped as well as the records. Two seats, two implementations, one
result; D03's §3.2 row is the outlier. The underlying gate behaviour is **correct** — no gate change
is owed — and R01-D-1 and R02-D-8 are the same finding and should be filed once.

This is a leg-correctness finding, which is squarely this seat's mission; the fix is D03's/D07's to
make (I do not edit another seat's fragment).

## Owed

- `reports/round-36/review/R01-d-review-drafts.md` — second pass on **D02, D04–D10** when they
  land (D01/D03 are covered in §6). Specifically: whether D04's re-pin list matches R03's finding
  that a D4 component-tree edit reddens the r7 default chain; and whether any draft proposes a
  `head2` stratum (which would newly make `RD-4`/`RL-3` load-bearing).
- Reconciliation of **R01-D-1** (§6.2) by D03 or D07 — the `register_scoped` discrepancy between
  D03's `0` and the delivered gate's `6`.
- `reports/round-36/run-validation.py` — owed by S01; claim D's `counting_commands` target is
  absent, so claim D's threshold is unmeasurable as filed.
- Integrator decision, not a file: claim D's scope. Either re-scope D onto the genuinely open
  `RL-2` (`head2` empty proper domain, `reports/round-26/register/design.md:228`, carried in
  `reports/round-33/calib/open-items-ledger.json` with a `next_touch`) — which is what D01 §3
  effectively drafts — or record claim D as `already-satisfied-at-baseline` /
  rejected-on-premise. Per `REGIMEN.md` ("Admit only when every claim verifies … never force a
  pass"), D cannot be admitted as written.

## Citations

**Claims and targets**
- `reports/round-36/claims.json:20-26` — claim D, its `before`, `after_required`,
  `counting_commands`, `thresholds`.
- `reports/round-36/targets.json` — seat `R01` object; `shared_rules`.
- `REGIMEN.md` — per-round contract, "Admit only when every claim verifies"; position 4
  provider/fallback.

**Measured — domain non-empty**
- `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` →
  `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0
  rule_holds=0`, exit 0.
- `examples/culture-d4/packet.d4.yml:1329` (`registers:`), `:46-54`
  (`record_fields.registers`), `:1010-1029` (`L-55` with `derived_from`/`derivation`/`doublet_of`).
- `examples/culture-d4/components/04-lexicon.yml:220-243` — the stamp-register block, 8 forms.
- `grep -c` counts: `derived_from` 8, `doublet_of` 8, `derivation:` 8.

**Measured — when it closed**
- `git show <c>:examples/culture-d4/packet.d4.yml | grep -c derived_from` → `fc13cd2` 0,
  `1ad491a` 0, `4f09c99` 9, `6c0ac44` 9, `ce103bf` 9.
- `git log -S"derived_from" -- examples/culture-d4/packet.d4.yml` → `4f09c99`.
- `SCORECARD.md:312` — the historical r25 `EMPTY` row (measured at `e7ecd204…`).
- `SCORECARD.md:329` — the r26 row: forecast CLOSED, 8 forms, 8 derived pairs.
- `reports/round-25/argot/execution-4.md:79,108,110` — the r25 `derived_pairs=0` measurement and
  the "structural pass on an empty register domain" caveat (true at r25).
- `reports/round-25/regression.md:76` — the r25 gate line.
- `reports/round-26/register/review.md:1` and §2 (`RD-1`) — 8/8 clean; the register re-hosted
  because the forecast's where-keys do not exist.
- `reports/round-26/register/forms.md` §1 — the authoritative 8-row table `RF-01..RF-08`.
- `#plain`/`#quote`/`slot_ref`/`doublets` → 0 each in `packet.d4.yml`.

**Measured — authenticity**
- `grep -o 'evidence: "[a-z-]*"' packet.d4.yml | sort | uniq -c` → `175 evidence: "design-choice"`.
- `examples/culture-d4/packet.d4.yml:2,3`; `components/04-lexicon.yml:11` — NON-CANON declarations.
- `components/02-phonology.yml:27` — `F-2` is a live component id.
- `components/02-phonology.yml:117-119` `phonotactics_record: PHON-01` — template `(C)V(V)(C)`,
  codas `[n, m, s, k, l, r, t, d]` (line `:119`); my independent legality check: 8/8 legal.
- My replay (`.scratch/r36-ro1/`): 8/8 reproduced; `doublet_of` 8/8 resolve to the named bases.

**Measured — leg correctness**
- Tamper control: `argot-derivation-gate.py .scratch/r36-ro1/tamper.yml` →
  `FINDING D4L-ARGOT-DERIV … L-56 'kit' … 'mes' yields 'sem'`, exit 1.
- `tools/gates/argot-derivation-gate.py:153-175` — the legality-constrained `syllabify`
  (round-27 fix of `RD-4`/`RL-3`).
- `reports/round-27/law/impl-1.md`, `impl-3.md` — the syllabify fix and the 62-form re-verification.
- `tools/gates/expected/register-law-gate/r30-post/expected.json` — `inputs` pin `aac91246…` ==
  current packet digest; `append_only_note`.
- `tools/gates/typed-pipelines.json` — profile `d4` pin `aac91246…`.
- Selftests/battery table in §4.
- `tools/gates/d4-typed-labels-check-gate.py:42` — usage `[PROJECTION]` (my §4 correction).
- `tools/gates/argot-derivation-gate.py:662-667` — the coverage-hold guard
  (`declared_ops and counters["register_scoped"] and not counters["derived_pairs"]`), the source of
  the §6.2 discrepancy.

**Second pass on the landed D drafts (§6)**
- `reports/round-36/depth/D01-design.md:23-66` — D01's independent premise correction and its
  reroute to the genuinely open surface; `:40-44` its `git log -S` landing history.
- `reports/round-36/depth/D01-design.md:98-121` — the four legs re-run at baseline (V-1..V-5),
  matching my §4 table.
- `reports/round-36/depth/D03-isolated-verify.md:29-75` — D03's `load_yaml` census and its own
  `8/8 clean` re-derivation; `:128-155` the tamper-control table and the §3.2 claim.
- `reports/round-36/depth/D03-isolated-verify.md:148-153` — the domain-emptied row
  (`records=179 register_scoped=0 … borrow_pairs=0`, exit 0) that does not reproduce.
- My emptied-domain probes: `.scratch/r36-ro1/emptied.yml` and `.scratch/r36-ro1/emptied2.yml` →
  `FINDING D4L-ARGOT-COVERAGE: HOLD … 6 register-scoped form(s)`, `register_scoped=6`, exit 1.
- Layer-level register declarations that keep the guard satisfied: `packet.d4.yml` `layers:` block,
  `LY-01 register: "trade"`, `LY-02 register: "craft"`.
- Sibling agreements: `reports/round-36/review/R02-d-review.md:26,44` (R02-D-1);
  `reports/round-36/review/R03-cross-review.md:102-131,288`.

**Owed**
- `find reports/round-36 -type f` — at first read only `cov/C01-audit.md` had landed; by the second
  pass `depth/D01-design.md`, `depth/D03-isolated-verify.md`, `cov/C03-verify.md`,
  `cross/X02-conformance.md`, `review/R02-d-review.md`, `review/R03-cross-review.md`,
  `scout/K02-timekeeping-scout.md`, `scribe/S02-telemetry-draft.md` had landed. **D02 and D04–D10
  remain absent.**
- `reports/round-26/register/design.md:228` — `RL-2`, the `head2` empty proper domain (the
  genuinely open adjacent item).
- `reports/round-33/calib/open-items-ledger.json` — the carried item with its `next_touch`.
