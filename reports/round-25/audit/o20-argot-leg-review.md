# R25-O20 — adversarial review: the argot leg and cross-cutting conformance

- Seat **R25-O20** (reviewer 3 of 3, argot leg + cross-cutting). Round 25
  (operator: loop 3 of 3, build 1 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` — `reports/round-25/targets.json`).
- Date **2026-10-18**. Declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  lane HEAD at review start `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- Assignment (verbatim): "O R25-O18..O20 (reviewers x3): adversarial pass on
  both fixes (bypass paths, supersession honesty)."
- **Write scope: this fragment only.** No `tools/**`, `examples/**`, `corpus/**`,
  `SKILL.md`, or filed round-8–24 byte is edited; no Git mutation. NON-CANON
  engineering evidence.
- **This seat authored none of the artifacts it reviews** — not
  `tools/gates/argot-derivation-gate.py`, not `reports/round-25/argot/**`, not
  `reports/round-25/run-validation.py`, not the frozen round-25 rows.
- Scratch: `.scratch/r25-o18/` (`TMPDIR=$PWD/.scratch` on every scratch write).

## 0. Verdict at a glance

| # | reading | verdict |
|---|---|---|
| 1 | the argot gate exists, selftest green (18/18 at `07db6e9b…`, 21/21 at `5b5abe78…`), and **discriminates** — an independently mutated correct form produces `D4L-ARGOT-DERIV` | **holds** |
| 2 | the canonical D4 run is green over the real packet (156 records, 0 violations) | **holds** |
| 3 | the delta is honest: the forecast is named **not delivered** element by element, with the root cause (a culture that never shipped) | **holds — strongest artifact of the round** |
| 4 | the claim's "the D4 typed gate grows the leg" | **was FAIL as worded at `879d40bf…`; DELIVERED at `bbe3f6ad…`** (`L3b-argot`, 20/20) |
| 5 | the leg is wired into the **battery** and the committed **hold set** | **still FAIL — named by the delta as Δ-step 4 open** |
| 6 | the SKILL.md derivation-relation rule is **still a draft** (`reports/round-25/rule/skill-draft.md`), not landed | **open — orchestrator's** |
| 7 | all three claims pass the counting command at the final revision | **holds** |

## 1. The argot leg: does it actually discriminate?

The claim's core requirement is that a violating form is caught. A gate that
only passes its committed fixture proves nothing; this seat therefore **built
its own violation** by mutating one *correct* row of the committed fixture so
its delivered term no longer equals `head2(base)`:

```sh
# .scratch/r25-o18/argot/mut-q01.yml — Q-01 term saalu -> saalum, derivation unchanged
python3 tools/gates/argot-derivation-gate.py .scratch/r25-o18/argot/mut-q01.yml
```

```
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-01 'saalum' (register 'quote'):
  declared chain 'head2' applied to 'saalumi' yields 'saalu';
  the stated inputs and rules do not yield the candidate
coverage: … records=14 register_scoped=11 derived_pairs=8 borrow_pairs=3
          violations=5 rule_holds=1
exit=1
```

The gate **recomputes** `head2('saalumi') = 'saalu'` and reports the mismatch
against the delivered `'saalum'` — it does not pattern-match the fixture. A
second independent mutation on the **borrow** path (`donor_form: gol → goll`)
likewise produces `D4L-ARGOT-DERIV`, recomputing the layer substitutions. Both
mutations are this seat's own; neither is in the committed fixture.

Selftest (18/18 at `07db6e9b…`, 21/21 at `5b5abe78…`) includes the
discriminating controls by name:
`design-table-rederived-11`, `head2-maximal-onset`, `head2-maximal-coda-differs`,
`head2-single-syllable`, `reverse-involution`, `leg-discriminates`,
`fixture-exits-1`, `fixture-names-the-violating-form`, `positive-control-clean`,
`c-02-negative-control-rejected`.

The `head2-maximal-onset` / `head2-maximal-coda-differs` pair is the one that
matters for the round-17 forecast: the design doc itself said the two
syllabification readings disagree and "a derivation that is not deterministic
cannot be checked". The gate pins the maximal-onset reading and tests the
diverging case.

## 2. The canonical D4 run — green, on an empty domain

```sh
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
# coverage: … records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6
#           violations=0 rule_holds=0
# exit=0
```

`derived_pairs=0`: the delivered packet declares **no** argot derivation pair,
so the derivation leg has an empty domain. The `borrow_pairs=6` half is live and
green. This is exactly what the delta says (F-5 "vacuously satisfied"), and it is
why the delta's honesty matters more than the exit code here — a green exit 0 on
an empty domain is not evidence the capability was exercised.

## 3. The claim's wording vs the delivered shape

The claim's `after_required` says, in three parts:

1. "derivation rules for the register-scoped forms replay against their stated
   inputs (machine-readable pattern/output pairs)" — **delivered**, in the
   sibling gate, over the `morphology.derivation_rules` block
   (`examples/culture-d4/packet.d4.yml:192-195`, `CX-01/02/03`);
2. "a violating form is `D4L-ARGOT-DERIV`" — **delivered**, §1;
3. "**the D4 typed gate grows the leg with selftest controls**" — **at first NOT
   delivered, then delivered mid-review**. At gate `879d40bf…`
   (`grep -c "argot\|ARGOT" tools/gates/typed-pipeline-gate.py` → **0**) the leg
   was a standalone sibling gate, and the delta named that substitution
   explicitly (§8 addendum item 3b: "The new gate is not wired into anything …
   the typed gate does not invoke it … So the leg exists as a **standalone
   script**, not as a pipeline leg"). At gate `bbe3f6ad…` (17:44Z) the typed gate
   **does** carry it: an `L3b-argot` leg (`tools/gates/typed-pipeline-gate.py:852`,
   `ARGOT_GATE` at `:84`) runs the sibling gate as a pipeline leg, and the D4
   source-packet run now reports `ok L3b-argot` at 20/20 legs.

Clause 3 was therefore **satisfied by a later revision during this review**. The
table in §0 row 4 and §4 below record the intermediate state; §4's "wired into
nothing" reading is **superseded for the typed gate** but still true for the
battery and the committed hold set (§4). The delta's substitution naming remains
correct as a record of the state at the time it was written.

## 4. The leg is wired into nothing

Three independent checks, all measured:

| surface | check | at `879d40bf…` | at `bbe3f6ad…` (17:44Z) |
|---|---|---|---|
| the typed gate | `grep -c "argot\|ARGOT" tools/gates/typed-pipeline-gate.py` | **0** | **20** — the `L3b-argot` leg runs the sibling gate |
| the gate battery | `grep -c "argot-derivation" tools/check-gate-battery.py` | **0** | **0** — still absent |
| the committed hold set | `D4L-ARGOT-*` in `examples/culture-d4/expected-holds.json` | **absent** | **absent** (`counts {hold 12, note 0, fail 0}`, all 12 `D2L-FORM-UNRESOLVED`) |

At `879d40bf…` the leg's ids could never enter `pipeline_findings`, so the D4
typed pipeline's verdict was unchanged by the round's argot work — the gate was
real and discriminating (§1) but **advisory-only**. At `bbe3f6ad…` the typed gate
**does** carry the leg (`ok L3b-argot`, 20/20 on the source packet), so a
violation would now surface as a `pipeline_findings` row.

Two gaps remain at `bbe3f6ad…`:

- the leg is still **not in the gate battery** (`tools/check-gate-battery.py`),
  so the battery does not exercise it;
- `D4L-ARGOT-*` is still **absent from the committed hold set**, so the D4 typed
  gate's `expected-holds.json` comparison does not expect an argot row.

The delta records this residual as "Δ-step 4 (the signature, and the expectation
row that makes the leg count) remains open" — accurate for the hold set, and
superseded for the typed-gate wiring.

## 5. The SKILL rule is still a draft

`reports/round-25/rule/skill-draft.md` states in its own header: "**Status:
DRAFT ONLY — `SKILL.md` is not edited by workers.** The orchestrator lands the
subsection below." `grep -c "argot\|derivation-replay" SKILL.md` → **0** at both
gate revisions sampled.

This is the lane's normal division (workers draft, the orchestrator lands), so it
is not a defect in the artifact — but it means the claim's "per the SKILL
derivation-replay discipline" is **not yet a landed discipline**. The rule exists
as a draft with cited sources; the SKILL.md surface does not carry it.

## 6. Cross-cutting: the counting command at the final revision

Run in an isolated clone (`reports/round-25/run-validation.py` sha `4cd6f066…`,
`TMPDIR` under the clone), with the typed gate at `879d40bf…` and the argot gate
at `07db6e9b…` (it moved to `cbe89f4d…` during this review — see §6.1):

```
claim O: PASS
claim D: PASS
claim C: PASS
acceptance_checks_passed: True
```

Claim O's `v3_supersession.claim_rows` reports `states_family_clean_value: true`
and `undispositioned_stale_sentences: []` for all four D4 rows, with
`oq_v3_05.disposition_marked: true` and `successor_candidates:
["reports/round-25/v3-supersession/declared-in-r4"]`.

**State moved under every seat this round.** Between 14:23Z and 14:42Z this seat
observed: the typed gate at three revisions (`04ad4bb4` → `61240b8`-based →
`879d40bf`), the argot gate at three revisions (appearing mid-window, `07db6e9b`
→ `cbe89f4d`), the counting command at four revisions (`2b7a…`-era → `d6e27b91`
→ `4cd6f066`), and the r4 revision's cited checker appearing after the note that
cites it. Every red this seat found was green by the next sample. **This is a
hazard for the parent's close**: the counting command's verdict is only
meaningful at a stated revision, and the round's evidence fragments were written
against different ones.

### 6.1 Re-verification at the argot gate's later revisions

The argot gate moved twice (`07db6e9b…` → `cbe89f4d…` → `5b5abe78…`) and the
**typed** gate three times (`879d40bf…` → `bbe3f6ad…` → `e0c27f96…`) while this
review was open. Re-run at the latest of each:

| check | at `07db6e9b…` / `879d40bf…` | at `5b5abe78…` / `e0c27f96…` |
|---|---|---|
| argot `--selftest` | 18/18 green | **21/21 green** |
| canonical D4 argot run | `derived_pairs=0 borrow_pairs=6 violations=0` | `derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0`, exit 0 |
| own `head2` mutation | 5 `D4L-ARGOT-DERIV` | 5 `D4L-ARGOT-DERIV` |
| own borrow mutation | 5 `D4L-ARGOT-DERIV` | 5 `D4L-ARGOT-DERIV` |
| `grep -c "argot\|ARGOT" tools/gates/typed-pipeline-gate.py` | **0** | **20** — the `L3b-argot` leg |
| D4 source-packet legs | 19/19 | **20/20** (`ok L3b-argot`) |
| `grep -c "argot-derivation" tools/check-gate-battery.py` | **0** | **0** |
| `grep -c "argot\|derivation-replay" SKILL.md` | **0** | **0** |

So the discrimination property (§1) and the empty domain (§2) hold at every
revision sampled; the typed-gate wiring (§3 clause 3, §4) went from **absent to
present**; and the battery + hold-set + SKILL gaps (§4-§5) are unchanged. The
argot gate gained a `claimed_chains=8` counter between the readings — still zero
derived pairs, so §2's "empty domain" reading is unchanged. The figures in §1 and
§2 are quoted from `07db6e9b…`; §6.1 is the re-measurement.

## 7. What this review does NOT establish

- It does not certify the argot gate's derivation tables against the round-17
  design doc's eleven worked derivations line by line; the gate's selftest does
  that internally (`design-table-rederived-11`) and this seat reproduced only the
  discrimination property (§1).
- It does not audit the C claim (`corpus/lessons/README.md`) — a sibling seat
  owns that surface (`reports/round-25/audit/c31-lessons-index-audit.md`).
- It ran no historical validator, so it rewrote no filed receipt.
- The `derived_pairs=0` reading (§2) means this review **cannot** show the
  derivation leg working on real D4 data — only on the fixture. That limitation
  is inherent to the delivered state and is named in the delta.

## 8. Reproduce

The two mutation inputs are rebuilt from the committed fixture by
`reports/round-25/audit/o18-probe-matrix.sh`'s sibling logic; this seat's copies
live under `.scratch/r25-o18/argot/`. To rebuild them without that scratch, take
`tools/gates/fixtures/argot-derivation-gate.yml` and change one correct row's
`term` so it no longer equals the declared chain's output.

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
sha256sum tools/gates/argot-derivation-gate.py         # 5b5abe78… at review close
python3 tools/gates/argot-derivation-gate.py --selftest                    # 21/21
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml  # 0, empty domain
python3 tools/gates/argot-derivation-gate.py .scratch/r25-o18/argot/mut-q01.yml   # 1, D4L-ARGOT-DERIV
python3 tools/gates/argot-derivation-gate.py .scratch/r25-o18/argot/mut-borrow.yml # 1, D4L-ARGOT-DERIV
grep -c "argot\|ARGOT" tools/gates/typed-pipeline-gate.py                  # 0
grep -c "argot-derivation" tools/check-gate-battery.py                     # 0
python3 reports/round-25/run-validation.py                                 # O/D/C PASS
```

Assertions: the selftest prints `21/21` at `5b5abe78…` (`18/18` at `07db6e9b…`);
the D4 run prints `derived_pairs=0` and exit 0; both mutations print
`D4L-ARGOT-DERIV` and exit 1; both `grep -c` print `0`; the counting command
prints `acceptance_checks_passed: True`.
