- Seat: D03 | executor (claim D, isolated apply-and-verify) | date 2026-10-19 | baseline 9bccc9b

# D03 — isolated apply-and-verify of the D residue legs

**Write scope:** `reports/round-38/depth/D03-isolated.md` only. All mutation under
`.scratch/d03/` (gitignored). No in-tree byte written; no commit, no push, no
network, no install. Every number below is a command output from an isolated
`git archive 9bccc9b` copy. Every leg ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. No
`reports/round-*/run-validation.py` was executed anywhere, in-tree or in a copy
(F-C13-1); no `--freeze` of `reports/round-34/handoff/declared-in-r7` was issued.

## 0. Mission status — D01/D02 never landed; the planner's draft was verified instead

Assigned: *"Isolated verify: apply D01+D02 in a git-archive copy, run assemble-d4
selftest, argot/law/typed legs; capture outputs."*

**D01 and D02 did not land.** Through this seat's whole run,
`reports/round-38/depth/` held `D05-verify.md`, `D07-receipt.md`, `D08-gap-fill.md`,
`D09-scribe.md`, `D10b-verify.md` — and never `D01-f6-design.md` or
`D02-rl8-design.md`. Three other seats sampled the same absence and said so:
D05 (*"D03's fragment does not exist at seat close"*), R01 (*"The D-block fragments
do not exist yet at review time … so the planner can fold it into P01 **before
D01/D02 are written**"*), and P01 (*"`reports/round-38/scout/K01-residue.md` does
not exist at write time"*).

**What this seat verified instead.** The block converged on **P01's §3.4 fenced
draft** as the landing shape: P01 is the planner of record, and both D08 (spare) and
R01 (reviewer) route to the same host. So this seat applied **P01's §3.4 draft
verbatim** to an isolated copy and ran the full mission battery on it (§3). It also
built and measured the **alternative host** D08 names (§4), so the integrator gets
both routes priced rather than one asserted. And it built the **F-6 consumer probe**
(§5) that D10b's mission requires and that no existing leg provides.

So the deliverable is: **the two residue legs, applied in isolation and verified
green with discriminating controls, on both candidate hosts, with the pin cost of
each measured** — plus the baseline expectations any other shape must meet.

## 1. Baseline — isolated `git archive 9bccc9b`, unmodified

Copy: `.scratch/d03/iso-base` (`mkdir -p … && git archive 9bccc9b | tar -x -C …`, 71 MB).

| # | command | result | exit |
|---|---|---|---|
| 1 | `python3 -B tools/assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| 2 | `python3 -B tools/assemble-culture-d4.py --check` | `packet.d4.yml: byte-identical deterministic assembly` | 0 |
| 3 | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| 4 | `python3 -B tools/gates/argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` | 0 |
| 5 | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` | 0 |
| 6 | `python3 -B tools/gates/register-law-gate.py --selftest` | `selftest: 45/45 checks passed` | 0 |
| 7 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` (incl. `ok L3b-argot`) | 0 |
| 8 | `python3 -B tools/gates/typed-pipeline-gate.py --selftest` | `selftest: 19/19 checks passed` | 0 |
| 9 | `python3 -B tools/gates/d4-assembly-check-gate.py` | `byte-identical deterministic assembly` | 0 |
| 10 | `python3 -B tools/gates/d4-typed-labels-check-gate.py` | `byte-identical deterministic projection` | 0 |
| 11 | `python3 -B tools/assemble-d4-typed.py --check` | `byte-identical deterministic typed packet` | 0 |
| 12 | `python3 -B tools/d2-typed-labels.py --packet … --check …` | `byte-identical deterministic projection` | 0 |
| 13 | `python3 -B tools/check-gate-battery.py` | `summary {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}` | 0 |
| 14 | `python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4 rows reproduced the recorded verdicts` | 0 |

Baseline digests (sha256 first 16); in-tree bytes identical to the copy:

```
aac91246cede8840  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56  examples/culture-d4/packet.d4.typed.yml
c23b0ab532cfb9d4  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6  examples/culture-d4/expected-holds.json
ed7093d6b92111c2  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c  examples/culture-d4/components/13-register-law.yml
b5406bcdaf41c595  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0  tools/gates/register-law-gate.py
b749ad07cf171027  tools/gates/typed-pipeline-gate.py
76ecdfdcbf09c3c7  tools/gates/typed-pipelines.json
```

## 2. The two residues, independently reproduced at the baseline

### 2.1 F-6 — no producer, and no consumer either

```
$ grep -rl "derived_forms\|derived_ok" examples tools          # exit 1, no match
```

The argot gate's coverage line emits `records / register_scoped / derived_pairs /
claimed_chains / borrow_pairs / violations / rule_holds`; the projection's coverage
block (`examples/culture-d4/typed-labels.d4.yml:29-47`) carries
`labels_by_kind / typed_labels / rank_rules_* / reconciliation_records`. The
forecast's `derived_forms` / `derived_ok` pair (`reports/round-25/argot/forecast.md:37`,
F-6 of `reports/round-17/d4/design-brief.md:306-307`) is absent from both. This is a
**key-set** gap, not a capability gap — `derived_pairs=8 violations=0` is non-vacuous.
D05 §2.1, D10b §1, R01 §1 and D08 §1 reach the same reading from separate samples.

### 2.2 RL-8 — the era leg is absent, and the declared defect is silent

`RGL-05`'s substance (`reports/round-26/register/rules.md` §5 `REGISTER-ERA-01`;
`examples/culture-d4/components/13-register-law.yml:49`) is *"a `stamp` record with
stage E0 → a defect"*. The defect is constructible; I constructed it. All eight
stamp forms `L-55..L-62` had `stage: E1 → E0` in an isolated copy, re-assembled:

```
assemble-culture-d4.py                                exit 0
argot-derivation-gate.py examples/culture-d4/packet.d4.yml   exit 0, era findings: NONE
register-law-gate.py examples/culture-d4/packet.d4.yml       exit 0, era findings: NONE
```

Neither register leg reads any dating: `grep -n "available_from\|D4L-ERA\|stage"
tools/gates/register-law-gate.py` → no hits; `kind: era` is a member of
`DECLARED_KINDS` (`register-law-gate.py:121`) but the gate grades only *membership*
in that set (`:353-360`). **X02 independently reproduced this exact probe**
(`reports/round-38/cross/X02-honesty.md` §1) with identical output; D05 §2.2, D10b §2,
R01 §2 and D08 §4.1 name the same absence. Five seats agree from separate measurements.

## 3. P01's §3.4 draft — applied verbatim and verified (the authoritative route)

P01's §3.4 puts **both** legs in `tools/gates/argot-derivation-gate.py` — the host
P01 measures as not-an-r7-read-set-member and not battery-registered (§4.2 there),
hence zero pin cost. This seat applied that draft **verbatim** (three hunks: the era
leg, the two F-6 counters, the coverage-line keys) via
`.scratch/d03/make_p01_patch.py` to `.scratch/d03/iso-p01`. All three anchors matched
exactly once; the patch applied cleanly.

### 3.1 The delivered packet — green, non-vacuous, zero era findings

| # | command | result | exit |
|---|---|---|---|
| 1 | `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `coverage: … derived_pairs=8 … violations=0 rule_holds=0 **derived_forms=8 derived_ok=8**` | 0 |
| 2 | `argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` (draft adds no checks; P01 §3.4's control additions are a separate hunk) | 0 |
| 3 | `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| 4 | `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| 5 | `check-gate-battery.py` | `summary {battery_exit: **0**, fail: 0, pass: 7, unevaluable: 0}` | 0 |
| 6 | `d4-assembly-check-gate.py` / `d4-typed-labels-check-gate.py` | both `byte-identical` | 0 |
| 7 | `exercise-handoff-e2e.py --profile v3 --quiet` | `exit=0 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | 0 |
| 8 | `replay-frozen.py …/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4 rows reproduced` | 0 |

**`derived_forms=8 derived_ok=8` is non-vacuous**: the eight stamp forms are real
members, so the agreement is a contract, not an empty-set pass. And the **r7 packet
pin is unchanged** — `sha256sum reports/round-34/handoff/declared-in-r7/packet.md`
→ `45f57132…`, exactly the claim's threshold. P01's "zero pins moved" prediction
**verifies**.

### 3.2 Control B — the C-E1 control fires with exactly 8 findings

All eight stamp forms `stage: E1 → E0` in an isolated copy, re-assembled:

```
assemble-culture-d4.py                                    exit 0
argot-derivation-gate.py examples/culture-d4/packet.d4.yml  exit 1
  D4L-ARGOT-ERA findings: 8   (one per stamp form, L-55..L-62)
  FINDING D4L-ARGOT-ERA: FAIL — register-scoped form L-55 'tuum' (register 'stamp')
    is claimed at stage 'E0'; the register is available_from E1 (13-register-law.yml
    RGL-05, REGISTER-ERA-01 / RL-8)
  coverage: … derived_forms=8 derived_ok=8 …
```

This reproduces r26's prediction **exactly** — 8 findings, exit 1
(`reports/round-26/register/rules.md:151`, C-E1). The leg is non-vacuous and
discriminating.

### 3.3 Control A — the loan-layer trap, confirmed live in the tree

P01 §3.3 warns that scoping the era leg on the gate's own `record_register()`
resolver (which resolves a record's `loan_layer` through the `layers` block) would
false-red the two delivered loan records. I verified the trap is **real in the
delivered bytes**:

```
loan-layer records (register: None, resolved through the layer row):
  L-49 'sal'  loan_layer='Salt-road trade layer'  stage=E1
  L-50 'kar'  loan_layer='Salt-road trade layer'  stage=E1
  L-51 'gul'  loan_layer='Salt-road trade layer'  stage=E1
  L-52 'res'  loan_layer='Salt-road trade layer'  stage=E1
  L-53 'gal'  loan_layer='North-road kin layer'   stage=E0   <- would false-red
  L-54 'mar'  loan_layer='North-road kin layer'   stage=E0   <- would false-red
layer rows: LY-01 register='trade', LY-02 register='craft'
```

`L-53`/`L-54` carry no `register:` of their own and resolve to layer `LY-02`
(`register: craft`) at `stage: E0`. P01's draft scopes on the record's **own**
`register:` field (`if declared_register.casefold() != "stamp": continue`), so both
are skipped and the delivered packet reads **0 era findings** (Control A, exit 0).
A landing that used `record_register()` would emit 2 false FAILs and break the tree.
**This is the single implementation decision most likely to produce a false red, and
P01's draft gets it right.** D08 §4.1 reaches the same scoping conclusion by a
different route (keying on `stage` alone, since the law/identity rows carry none).

## 4. The alternative host — D08's law-gate route, and its measured pin cost

D08 §4.2 puts the RL-8 era leg in `tools/gates/register-law-gate.py` instead, and
names the consequence: a battery baseline re-freeze. This seat built that variant
too (`.scratch/d03/make_candidate_patch.py`, copy `.scratch/d03/iso-cand`) and
measured the cost, so the integrator can see the trade rather than trust either seat.

| # | command | law-gate host | argot-gate host (P01) |
|---|---|---|---|
| 1 | delivered packet, law leg | `era_rows=8 era_failures=0 findings=0`, exit 0 | n/a (leg lives in argot) |
| 2 | `--selftest` | `48/48` (3 era controls added) | `27/27` |
| 3 | `typed-pipeline-gate.py` | `20/20` | `20/20` |
| 4 | `assemble-culture-d4.py --check` | `byte-identical` | `byte-identical` |
| 5 | **`check-gate-battery.py`** | **`battery_exit: 2`**, `baselines: expected/register-law-gate/r30-post` reading **`pinned → gate_revised`** | **`battery_exit: 0`** |
| 6 | E0 control | 8 `D4L-LAW-ERA` FAILs, exit 1 | 8 `D4L-ARGOT-ERA` FAILs, exit 1 |

**The trade, named and not averaged:** the law-gate host is semantically natural
(RGL-05 is *a law row*, and the law gate already declares `kind: era`) but it is
battery-registered, so editing it flips the filed baseline
`tools/gates/expected/register-law-gate/r30-post/expected.json` to `gate_revised` and
the battery to exit 2 (`fail: 0`, `unevaluable: 0` — no gate is failing; the filed
baseline's *pinned gate digest* moved). That requires a **new-row** baseline
generation (`r38-post`) and its mirrored snapshot. The argot-gate host (P01) is
**battery-neutral and read-set-neutral** — zero pins — at the cost of putting a law
rule in the derivation gate. **P01's route is the cheaper landing and is the one this
seat verified end-to-end (§3); D08's route is the more semantically direct one and
costs one new baseline row.** R01 §3 reaches the same split ("each of the two
residues, landed the way its own spec requires, moves a third pinned surface") and
D08 §5 confirms the battery reading. The choice is the integrator's; both are measured.

### 4.1 A bug in this seat's own first law-gate attempt (recorded)

Reading the era floor from `era_rule` **plus** the free-prose `law` field, `QREG-04`'s
law text (*"…a stamp form claimed at **E0** is a defect…"*) made `min()` pick **E0** as
the floor, so the leg never fired and the E0 control stayed green. **Fixed by reading
the floor from the explicit `era_rule` field only** (`QREG-04 era_rule:
"a stamp form is available_from E1"`). Recorded because any landing that derives the
floor from prose reproduces the failure, and because P01's draft avoids the question
entirely by comparing `stage < "E1"` against the constant the spec itself states.

## 5. The F-6 consumer — D10b's hole, closed and measured

D10b's mission is the load-bearing check: *is the emitter's output **consumed**, or
only present?* D10b §2–§3 found that at `9bccc9b` **no consumer reads the counters on
either route** — the `L3b-argot` leg reads only `FINDING D4L-ARGOT-*` lines and the
exit code (`typed-pipeline-gate.py:530-539`), and the projection block is guarded for
byte-equality only, so a projector free to lie passes. R01 §5 names the same
vacuous-pass risk. D03 built and ran the consumer probe
(`.scratch/d03/f6_consumer_probe.py`): it parses the gate's own `coverage:` line and
**re-derives** the two counters from the packet bytes through a fresh parse, sharing
no code path with the gate's `Counter`.

```
$ python3 -B .scratch/d03/f6_consumer_probe.py .scratch/d03/iso-base      # baseline
recount: derived_forms=8 derived_ok=8
emitted: derived_forms=None derived_ok=None
REFUSE: the coverage line omits the F-6 keys                              exit 1

$ python3 -B .scratch/d03/f6_consumer_probe.py .scratch/d03/iso-p01       # P01 route
recount: derived_forms=8 derived_ok=8
emitted: derived_forms=8 derived_ok=8
CONSUMED: the F-6 keys are present and agree with an independent recount   exit 0
```

**This is the falsifiable before→after the F-6 threshold needs**: the probe refuses on
the baseline (keys absent) and passes only when the emitted counters agree with an
independent recount. A key-only emitter, or a lying one, still refuses — D10b's C2/C3
controls. The probe is scratch-side (this seat's verification vehicle), not a filed
gate (§7.3).

## 6. Integration constraints the landing must respect

### 6.1 Pin cost by host — measured, not inferred

| host | in r7 read set? | battery-registered? | measured effect of an edit | route |
|---|---|---|---|---|
| `tools/gates/argot-derivation-gate.py` | **no** | **no** | battery exit 0; v3 exit 0, packet `45f57132…` unchanged; typed 20/20 | **P01 — free, verified §3** |
| `tools/gates/register-law-gate.py` | no | **yes** | battery exit 2 (`gate_revised`); needs new `r38-post` baseline row | **D08 — one new baseline row, measured §4** |
| `tools/d2-typed-labels.py` (projection) | **yes** | yes | v3 **exit 1** `E2E-DIGEST`; `projector_sha256` ×4 + `pin_generations[]` + `typed-pipelines.json` row | D08 §3(B)/P01 §5 R-3 — full projection repin |

The projection route is legal but buys the whole D4 projection repin for the same two
integers, and the projector would have to re-implement `head2`/`reverse`, which
`typed-pipeline-gate.py:519-522` explicitly refuses. P01 §4.2 and D08 §3 both price it
that way. **Both verified routes (P01 argot-host, D08 law-host) touch no
packet/component/pin byte** — see §6.2.

### 6.2 Tool-only changes move no packet or pin

```
                    baseline            P01 route           D08 route
packet.d4.yml       aac91246cede8840    aac91246cede8840    aac91246cede8840
packet.d4.typed.yml d581e0ad5384ce56    d581e0ad5384ce56    d581e0ad5384ce56
typed-labels.d4.yml c23b0ab532cfb9d4    c23b0ab532cfb9d4    c23b0ab532cfb9d4
expected-holds.json e6ae9828d6c82aa6    e6ae9828d6c82aa6    e6ae9828d6c82aa6
typed-pipelines.json 76ecdfdcbf09c3c7   76ecdfdcbf09c3c7   76ecdfdcbf09c3c7
```

So both residue legs as drafted are **pure gate changes**: no packet, component,
projection or pin byte moves, and the r7 packet pin `45f57132…` is untouched by
construction. The only filed artifact either route reddens is the battery baseline in
the D08 route (§6.1). If the integrator instead emits the counters from a component or
the projection, the r36 D03 §5 pin cascade applies and D04's pin plan owns it.

### 6.3 The r31-post frozen manifest survives both legs

`replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` → `REPLAY OK:
4/4 rows reproduced`, exit 0, on **both** the P01 and D08 copies. Unlike a content
landing (r36 D03 §5: `REPLAY MISMATCH: 4 mismatch`), a gate-only change leaves the
frozen rows reproducing, because each row pins the *input* digest, not the gate's.

### 6.4 Opt-in battery registration is out of D's scope

P01 §4.4 measures that registering `argot-derivation-gate.py` in the battery
(`REGISTER_LAW_GATE_NAMES`) makes the battery demand a baseline
(`BASELINE-GATE-UNCOVERED`) — in-scope only with a new `expected/argot-derivation-gate/`
freeze row. That is operability work (the O block), not D's, and it is the collision
R03 should see: **if O registers the argot gate while D grows it, the freeze row must
pin D's post-change bytes, so the freeze must follow D's landing.**

## 7. What the apply-and-verify cannot settle

### 7.1 D01/D02's actual shape is unverified — they never landed

The mission's named inputs do not exist (§0). P01's §3.4 draft is verified here
because it is the planner-of-record's shape and D08/R01 route to the same host; but
**the verdict on D01's and D02's own fenced drafts is owed**, and D05's verdict on
this file is owed (it sampled before D03 wrote). The harness
(`.scratch/d03/apply_and_verify.py --patch d01=<path> --patch d02=<path>`) re-runs
their blocks unchanged, and §1–§3 give the expectations any shape must meet.

### 7.2 The two legs are separable

F-6 and RL-8 both land in the same gate under P01's route but are independent hunks
with independent controls. A round that can land only one should land the F-6 leg
(consumer-probe-verified, zero pins) and carry the era leg with its host decision.

### 7.3 The consumer probe is scratch-side

`.scratch/d03/f6_consumer_probe.py` is this seat's verification instrument. If the
round wants the F-6 threshold enforced permanently, the probe (or D10b's own fenced
draft) must be filed as a tool change — the integrator's decision, and a tool change
this seat drafts rather than applies.

## 8. Reproduce

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/d03/iso-base && git archive 9bccc9b | tar -x -C .scratch/d03/iso-base
python3 -B .scratch/d03/apply_and_verify.py --label baseline

# P01 section 3.4 route (the verified landing shape)
rm -rf .scratch/d03/iso-p01 && mkdir -p .scratch/d03/iso-p01
git archive 9bccc9b | tar -x -C .scratch/d03/iso-p01
python3 -B .scratch/d03/make_p01_patch.py .scratch/d03/iso-p01
cd .scratch/d03/iso-p01
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # derived_forms=8 derived_ok=8, 0 era
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml     # 20/20
python3 -B tools/check-gate-battery.py                                             # battery_exit 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                      # exit 0, packet 45f57132…
cd -; python3 -B .scratch/d03/f6_consumer_probe.py .scratch/d03/iso-p01            # CONSUMED, exit 0
python3 -B .scratch/d03/f6_consumer_probe.py .scratch/d03/iso-base                 # REFUSE, exit 1

# D08 law-gate route (the alternative, with its battery cost)
rm -rf .scratch/d03/iso-cand && mkdir -p .scratch/d03/iso-cand
git archive 9bccc9b | tar -x -C .scratch/d03/iso-cand
python3 -B .scratch/d03/make_candidate_patch.py .scratch/d03/iso-cand
cd .scratch/d03/iso-cand && python3 -B tools/check-gate-battery.py                 # battery_exit 2 (gate_revised)
```

## Owed

1. **`reports/round-38/depth/D01-f6-design.md` and `D02-rl8-design.md` did not
   exist at this seat's every sample.** The mission's assigned inputs could not be
   integrated; the verdict on D01's and D02's actual fenced drafts is owed to the
   integrator (or a re-run of this seat once they land). Owner: D01/D02, then D03.
2. **The host decision is open** (§4): P01 (argot gate, zero pins, verified) vs D08
   (law gate, one new baseline row, measured). The integrator must pick; both routes
   are verified green here. If D08's route is taken, a **new `r38-post` baseline
   generation row** for `tools/gates/expected/register-law-gate/` is owed (a new row,
   never an edit of `r30-post`). Owner: whoever lands the RL-8 leg, with D04.
3. **D05's verdict on this file** — `reports/round-38/depth/D05-verify.md` sampled a
   tree without this fragment and says so explicitly; its verdict on D03 is owed.
   Owner: D05 (or a re-run).
4. **The F-6 consumer probe is scratch-side** (§7.3). To enforce the threshold
   permanently, the probe or D10b's fenced draft must be filed. Owner: integrator.
5. **`head2`'s declared-but-unused state** (r36 K01 §4 residue item 2, R01 §6 `OI-02`)
   is **not** touched — it is not part of the round-38 D claim, and no `head2` domain
   exists. Carried, unmeasured here.
6. **Claim D's third declared counting command**, `python3
   reports/round-38/run-validation.py`, does not exist yet
   (`ls reports/round-38/run-validation.py` → No such file or directory) and may not
   be run in-tree regardless (F-C13-1). `to-verify` until the integrator lands it.

## Citations

**Files read (in-tree, `9bccc9b`)**
- `REGIMEN.md`; `reports/round-38/claims.json:1-30`; `reports/round-38/targets.json` (seat D03 row `depth/D03-isolated.md`; D01/D02 rows; shared rules)
- `reports/round-38/telemetry/{dispatch-declared,availability-attempt-1}.json`
- `reports/round-38/plan/P01-d-plan.md:1-70,70-200,200-330` (the §3.4 fenced draft verified here; the §3.3 loan-layer trap; §4.2 host table; §4.4 battery registration; §5 work order)
- `reports/round-38/depth/D08-gap-fill.md:1-45,128-190` (the F-6 placement table; the law-gate RL-8 route and its battery cost); `reports/round-38/depth/D05-verify.md:1-80`; `reports/round-38/depth/D10b-verify.md:1-130` (Route A/B, the fenced consumer guard); `reports/round-38/review/R01-d-review.md:1-130,213-246`; `reports/round-38/cross/X02-honesty.md` §1; `reports/round-38/adj/A03-verify.md`
- `reports/round-36/scout/K01-register-scout.md:1-40,110,115,210-211`; `reports/round-36/depth/D03-isolated-verify.md:1-80` (pin-cascade and freeze precedent)
- `reports/round-25/argot/forecast.md:25-56` (F-6 = `design-brief.md:306-307`); `reports/round-26/register/rules.md:100-155` (§5 `REGISTER-ERA-01`, C-E1); `reports/round-27/law/impl-8.md:55-80` (`RL-8` owner row)
- `examples/culture-d4/components/13-register-law.yml:49,51-58` (RGL-05, the era floor, the named non-execution)
- `examples/culture-d4/packet.d4.yml` (`registers` QREG-01..08 incl. `QREG-04 era_rule`; loan records `L-49..L-54` at `:969-1002`; layer rows `LY-01/LY-02` at `:1207-1222`); `examples/culture-d4/components/04-lexicon.yml:236-254` (the eight stamp forms, all `stage: E1`); `examples/culture-d4/typed-labels.d4.yml:29-47`
- `tools/gates/argot-derivation-gate.py:543-667` (counters, coverage hold, print), `:917-921`; `tools/gates/register-law-gate.py:119-121,246-380,402-418,635-643`; `tools/gates/typed-pipeline-gate.py:80-84,517-541` (the `L3b-argot` consumer); `tools/check-gate-battery.py:117-132,269,540,840-860`

**Commands run** — tabulated verbatim in §1–§5, all in the isolated copies named in
§0 and §8 (never in-tree), with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:
`git archive 9bccc9b | tar -x`; `assemble-culture-d4.py --selftest/--check`;
`argot-derivation-gate.py <packet>/--selftest`; `register-law-gate.py
<packet>/--selftest`; `typed-pipeline-gate.py <packet>/--selftest`;
`d4-assembly-check-gate.py`; `d4-typed-labels-check-gate.py`;
`assemble-d4-typed.py --check`; `d2-typed-labels.py --packet … --check`;
`check-gate-battery.py`; `exercise-handoff-e2e.py --profile v3 --quiet`;
`replay-frozen.py …/r31-post/MANIFEST.tsv`; `grep -rl "derived_forms\|derived_ok"
examples tools` (exit 1); `sha256sum reports/round-34/handoff/declared-in-r7/packet.md`.

**Scratch (gitignored, not evidence by itself)**: `.scratch/d03/{iso-base,iso-p01,iso-cand,probe}/`,
`.scratch/d03/{apply_and_verify,residue_probes,make_p01_patch,make_candidate_patch,f6_consumer_probe}.py`,
`.scratch/d03/{result-baseline,battery-base,battery-cand,residue-probes}.json`.

**Canon**: NON-CANON engineering evidence. This fragment records an isolated
rehearsal and its measurements; it makes no promotion, canon, clearance or closure
verdict. Both candidate patches are applied **only inside `.scratch/`**; every in-tree
byte named above is unmodified (`git diff 9bccc9b` empty).
