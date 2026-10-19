- Seat: R02 | reviewer | claim D | date 2026-10-19 | baseline ce103bf

# R02 — second D pass: the isolated verifications' evidence

**Mission** (`reports/round-36/targets.json`, seat `R02`): "Second D pass: the isolated
verifications' evidence." Out path `reports/round-36/review/R02-d-review.md`. Shared rules read at
`reports/round-36/targets.json` `shared_rules`; the F-C13-1 rule was honoured — **no
`reports/round-*/run-validation.py` was executed in-tree or anywhere**, and no `--freeze` of
`reports/round-34/handoff/declared-in-r7` was attempted (its bytes are pinned).

**Method.** Every command below ran from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, or inside my own isolated
`git archive ce103bf | tar -x` copy at `.scratch/r02-iso/` (untracked; `git status --porcelain
examples/ tools/` empty at every read). Baseline `ce103bf5885af00023cdc4a174c17602476cdcf8`
(`git rev-parse ce103bf`). The only write is this fragment.

**Dependency note.** The mission names "the isolated verifications" (plural) — i.e. the D block's
`depth/D03-isolated-verify.md` and `depth/D07-verify.md`. At the time §1–§7 were written **neither
existed** (`find reports/round-36 -type f` → `claims.json`, `cov/C01-audit.md`,
`cross/X02-conformance.md`, `depth/D01-design.md`, `targets.json`, `telemetry/*`), so this seat
**produced its own** isolated verification — the same evidence class the mission asks for (§3).
`depth/D03-isolated-verify.md` landed during the run and is audited in **§8**; `depth/D07-verify.md`
is still absent and stays owed.

## 1. Verdicts

1. **Claim D's `before` is stale — independently reproduced (R02-D-1).** The claim asserts the
   register-form domain is empty. It is not, at `ce103bf`. Reached independently of
   `depth/D01-design.md` §0 and `depth/D03-isolated-verify.md` §1, which state the same finding
   from their own measurements.
2. **Both register legs are green and discriminating on an isolated copy (R02-D-2, R02-D-3).**
   Isolated and in-tree stdout are **byte-identical**; my own tamper controls fire the named
   finding classes.
3. **The eight register forms re-derive from raw packet bytes under my own parser (R02-D-4).**
   8/8 clean, including the `axis → op` rule.
4. **No live pointer is stale; 25 non-matching rows are append-only history, not drift
   (R02-D-5).** Censused, not assumed.
5. **Real open gap (R02-D-6): the register-*form* leg has no baseline row and is unregistered in
   the gate battery.** The register-*law* leg got both (`r30-post`, registered). Claim D's
   "re-pin as new rows" is therefore **half done** — the half that is missing is the one that
   grades the forms.
6. **The claim's own counting command does not exist (R02-D-7).** `reports/round-36/run-validation.py`
   is absent, so `python3 -B reports/round-36/run-validation.py` cannot be run by anyone at this
   stamp. Filed as a gap, not run.
7. **`depth/D03-isolated-verify.md` audited: §2's 15 legs reproduce exactly, §3.2's
   `domain-emptied` control does not reproduce as written (R02-D-8).** The named transform yields
   `register_scoped=6`, `borrow_pairs=6`, exit 1 and a fired `D4L-ARGOT-COVERAGE` hold — not the
   row's `0`/`0`/`0`. D03's "coverage-hold limit" remedy is therefore **not owed** as stated; the
   guard is narrower than reported. §8.

## 2. R02-D-1 — the stale premise, measured

The claim's `before` (`reports/round-36/claims.json`, claim `D`):

> "Register-form domain empty (`reports/round-25/argot/` + SCORECARD r25 row); register law/strata
> exist but the form class has no instances"

Measured at `ce103bf`, with the counting commands:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0

$ grep -c "derived_from" examples/culture-d4/packet.d4.yml          # → 9 (8 lexicon + 1 contract field list)
$ python3 -c "…"   # lexicon block census
lexicon records: 62
with derived_from: 8
with derivation: 8
with doublet_of: 8
with register: 8
```

| the claim's `before` asserts | measured at `ce103bf` | evidence |
|---|---|---|
| register-form domain empty | **8 register forms delivered** | `examples/culture-d4/components/04-lexicon.yml:236-243` (`L-55..L-62`) |
| "the form class has no instances" | 8 instances, each `register: stamp` with `derived_from` + `derivation{op,base}` + `doublet_of` | same lines; packet rows at `packet.d4.yml:1009-1183` (L-56 at `:1009`, L-62's block ends at `:1183`, `layers:` begins `:1184`) |
| register law "exists" | `registers:` (QREG-01..08) **and** `register_law:` (RGL-01..05) both top-level keys | `packet.d4.yml` key census; `registers:` at `:1329`, `register_law:` at `:2788` |
| the checking legs | argot exit 0 `violations=0`; law exit 0 `findings=0` | §3 |

The r25 record the claim cites is honest for its own stamp — `reports/round-25/argot/current-state.md:76`
reads `registers` top-level packet key → **no**; `:97` reads `registers` **ABSENT**, `doublets`
**ABSENT**; `SCORECARD.md:312` records "the register-form domain in the delivered D4 packet is
EMPTY". All three are true of the r25 tree. The closure landed in **r26** (stratum) and **r30**
(QREG amendment), both ancestors of `ce103bf`:

```
$ git log --oneline -S "register: stamp" -- examples/culture-d4/components/04-lexicon.yml
11df1fd round-30 wave integration: QREG landing, speaker candidate, law baseline, craft synthesis draft, telemetry
4f09c99 round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)
```

**Consequence for claim D.** Its `after_required` — "register-form domain non-empty with verified
forms (derivation replay clean over the new forms; law gate exit 0 over them; typed pipeline holds
updated with named gaps)" — is **already satisfied at the baseline**. The claim cannot move the
depth axis by building content that is delivered. Two independent seats (D01 §0, this one) reached
that reading separately; it is not one seat's opinion.

## 3. R02-D-2/R02-D-3 — the isolated verification, and its teeth

I built my own isolated copy rather than trusting a sibling's:

```
$ rm -rf .scratch/r02-iso && mkdir -p .scratch/r02-iso && git archive ce103bf | tar -x -C .scratch/r02-iso
$ find .scratch/r02-iso -name "*.py" | wc -l      # → 188
```

| # | leg | command | in-tree result | isolated result | exit |
|---|---|---|---|---|---|
| I-1 | derivation replay | `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs=8 violations=0 rule_holds=0` | **byte-identical** to in-tree | 0 |
| I-2 | replay selftest | `tools/gates/argot-derivation-gate.py --selftest` | `27/27 checks passed` | `27/27 checks passed` | 0 |
| I-3 | law gate | `tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 findings=0` | **byte-identical** to in-tree | 0 |
| I-4 | law selftest | `tools/gates/register-law-gate.py --selftest` | `45/45 checks passed` | `45/45 checks passed` | 0 |
| I-5 | D4 assembly | `tools/assemble-culture-d4.py --selftest` | — | `81/81 checks passed` | 0 |
| I-6 | D4 assembly check | `tools/assemble-culture-d4.py --check` | — | `packet.d4.yml: byte-identical deterministic assembly` | 0 |
| I-7 | typed assembly check | `tools/assemble-d4-typed.py --check` | — | `packet.d4.typed.yml: byte-identical deterministic typed packet` | 0 |
| I-8 | typed-labels gate | `tools/gates/d4-typed-labels-check-gate.py --selftest` | — | `163/163 checks passed` | 0 |
| I-9 | typed pipeline | `tools/gates/typed-pipeline-gate.py --selftest` | — | `19/19 checks passed` | 0 |
| I-10 | gate battery | `tools/check-gate-battery.py` | `pass 7, fail 0, unevaluable 0` | — | 0 |
| I-11 | handoff v3 e2e | `tools/exercise-handoff-e2e.py --profile v3 --quiet` | `fields=16/16 … findings=0 links=105/105 claims=27` | — | 0 |
| I-12 | replay-frozen selftest | `tools/replay-frozen.py --selftest` | — | `79/79 checks passed` | 0 |

```
$ diff /tmp/iso-argot.txt /tmp/live-argot.txt   && echo "argot IDENTICAL"          # → argot IDENTICAL
$ diff /tmp/iso-law.txt   /tmp/live-law.txt     && echo "register-law IDENTICAL"   # → register-law IDENTICAL
```

**The teeth controls (R02-D-3).** A green leg over a delivered packet is only evidence if the leg
can go red. I built two tampers from the delivered bytes myself (scratch copies under
`/tmp/r02probe/`, never in-tree) and ran the **isolated** gate over them:

```
# tamper 1 — register_law: RGL-01 force -> "no-such-force"
$ python3 -B tools/gates/register-law-gate.py /tmp/r02probe/t-force.yml
FINDING D4L-LAW-FORCE: FAIL — RGL-01 force 'no-such-force' names no declared illocutionary class or modifier; the declared set is assertive/directive/commissive/expressive/declarative plus binding/refused/not-rollable/none/attested/witnessed/naming/constraint (reports/round-27/law/design.md section 3; rules.md RU-L2)
coverage: … law_rows=5 … force_failures=1 … findings=1
exit=1

# tamper 2 — the register FORM: L-56 derived_from "tik" -> "mol"
$ python3 -B tools/gates/argot-derivation-gate.py /tmp/r02probe/t-deriv.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kit' (register 'stamp'): declared chain 'reverse' applied to 'mol' yields 'lom'; the stated inputs and rules do not yield the candidate
coverage: … derived_pairs=8 … violations=1 rule_holds=0
exit=1
```

Both tampers add **exactly one** named finding, naming the row and the value, and both legs are
silent on the untouched packet. The register-form leg is therefore **not** a vacuous pass over the
new domain: it resolves each form's own stated inputs and refuses a mismatched one. The law leg's
teeth were the r27 `RL-1` defect and are now real (`tools/gates/register-law-gate.py` docstring).

## 4. R02-D-4 — the eight forms, re-derived from raw packet bytes

Independently of the gate, I parsed the packet's own `lexicon` block with my own line-based reader
(not the naming gate's loader) and re-applied the declared operations. The rule under test is
`QREG-03`'s `operation_rule: "axis mark -> reverse; axis fire -> lengthen"`
(`components/04-lexicon.yml:252`).

| form | base | op | derived | axis | rule demands | derives | base delivered | `doublet_of` resolves | collision-free |
|---|---|---|---|---|---|---|---|---|---|
| `L-55 tuum` | `tum` | lengthen | `tuum` | fire | lengthen | yes | yes | `L-02` | yes |
| `L-56 kit` | `tik` | reverse | `kit` | mark | reverse | yes | yes | `L-42` | yes |
| `L-57 lom` | `mol` | reverse | `lom` | mark | reverse | yes | yes | `L-38` | yes |
| `L-58 nees` | `nes` | lengthen | `nees` | fire | lengthen | yes | yes | `L-16` | yes |
| `L-59 huum` | `hum` | lengthen | `huum` | fire | lengthen | yes | yes | `L-09` | yes |
| `L-60 mees` | `mes` | lengthen | `mees` | fire | lengthen | yes | yes | `L-43` | yes |
| `L-61 reek` | `rek` | lengthen | `reek` | fire | lengthen | yes | yes | `L-37` | yes |
| `L-62 saam` | `sam` | lengthen | `saam` | fire | lengthen | yes | yes | `L-39` | yes |

```
register forms: 8
FAILURES: []
```

All eight satisfy: the form equals `op(base)`; the op is the one `QREG-03`'s axis rule selects;
`derived_from` names the base; the base is a delivered `term`; `doublet_of` resolves to a delivered
record id; and the form string is unique across the lexicon. This is a **second, independent**
derivation of the r26 `forms.md` §1 table on the post-r30 bytes — the table's own claims reproduce.

## 5. R02-D-5 — the pin census: no live pointer is stale

I censused every `(surface, digest)` pair naming a D4 path across `tools/gates/{expected,frozen}/**`:

```
rows found: 35   matched-live: 10   non-matching: 25
```

The distinction that matters is **live-read-set rows vs historical/mirror rows**, not the raw count:

- **Live-pointer rows — all match live bytes (10/10).**
  - `tools/gates/typed-pipelines.json`, profile `d4`, first-match row: packet `aac91246…`,
    assembler `943f487b…`, projection `c23b0ab5…`, expected `e6ae9828…` — every one equals the
    live `sha256sum`.
  - `examples/culture-d4/expected-holds.json` top-level: packet `aac91246…`, projection
    `c23b0ab5…`, projector `2819f687…` — live.
  - `tools/gates/expected/register-law-gate/r30-post/expected.json`, `input_class:
    "live-read-set"`: packet `aac91246…`, gate `15f8b232…`, dependency `d9e4e8f4…` — live.
- **The 25 non-matching rows are append-only history, and their own discipline requires them to
  stay stale.** They live under `frozen/round-18`, `frozen/round-22/d4-repin`,
  `frozen/round-25/gate-input`, `frozen/round-26/{gate-input,post-register}`, and
  `expected/d4-{assembly,typed-labels}-check-gate/{r19-pre,r20-post,r22-post}`. Two spot checks
  confirm each pins its **own** snapshot, not the live tree:
  `expected/d4-assembly-check-gate/r19-pre/packet.d4.yml` hashes `e7ecd204…` = that row's own pinned
  value; `expected/d4-typed-labels-check-gate/r22-post/typed-labels.d4.yml` hashes `60b526b0…` =
  its pin. `gate-frozen-run-standard.md` §3 requires a new baseline id rather than an edit, so
  these *must not* be re-pointed. Recording them as "drift" would be the error.

So the r30 re-pin chain is intact and no live consumer reads a superseded packet. `reports/round-35/validation.json`
independently agrees (`acceptance_checks_passed: true`).

## 6. R02-D-6 — the open gap: the form leg has no baseline and no registration

Claim D's `after_required` asks for the register legs to be "re-pin[ned] as new rows". Half of that
is done and half is not:

| leg | script | baseline row under `expected/`/`frozen/` | registered in `tools/check-gate-battery.py` |
|---|---|---|---|
| register **law** | `tools/gates/register-law-gate.py` | **yes** — `expected/register-law-gate/r30-post/` | **yes** — `REGISTER_LAW_GATE_NAMES` |
| register **form** (derivation replay) | `tools/gates/argot-derivation-gate.py` | **no** | **no** |

Measured:

```
$ grep -rn "argot-derivation-gate.py" tools/gates/frozen/ tools/gates/expected/
# every hit is prose *inside a mirrored packet* (a derivation_ops_note) or a docstring reference in
# the mirrored law gate — none is a baseline's gate_script/gate field.
$ python3 -c "… gate_script census across every expected.json …"
  tools/gates/register-law-gate.py              rows=1
  argot-derivation-gate present as gate_script? False

$ python3 -c "… import tools/check-gate-battery.py …"
  REGISTERED        : (… 'register-law-gate.py')
  count registered  : 10
  argot registered? : False
  baseline summary  : {'baselines_found': 20, 'pinned': 20, 'coverage': '10/10', …}
```

The battery is now **10/10 / 20 pins** — the r30 `9/10 BASELINE-GATE-UNCOVERED` dependency
(`reports/round-30/fixes/battery-registration.md:11`, `reports/round-30/verify.md:22`) **is closed**
for the law gate, because `r30-post` landed. But the derivation-replay leg — the one that grades the
eight register forms this claim is about — was never given the same treatment. It runs inside the
per-round runners (`reports/round-28/run-validation.py:232-233`, `reports/round-29/run-validation.py:73-74`,
`reports/round-30/run-validation.py:67-68`) but has no frozen verdict row and no battery
registration, so nothing replays its verdict outside a round runner.

This is the residue of claim D that is genuinely actionable and that the claim's own wording
("re-run the register legs (derivation replay, law gate, typed pipeline), and re-pin as new rows")
covers. It is **not** built by this seat — a baseline row is an integrator landings under
`tools/gates/expected/`, outside this seat's write scope (`reports/round-36/targets.json`
`shared_rules`). Recorded here so it is not discovered late.

## 7. R02-D-7 — the claim's counting command is not on disk

Claim D's `counting_commands` is `["python3 -B reports/round-36/run-validation.py"]`, and the
thresholds say "replay/law/typed legs green". At this stamp:

```
$ ls reports/round-36/run-validation.py
ls: cannot access 'reports/round-36/run-validation.py': No such file or directory
```

The runner is owed by `scribe/S01-integration-draft.md`. Until it lands, no seat can produce the
claim's own acceptance evidence, and my isolated legs above are the substitute. Filed, not run —
running it in-tree would breach F-C13-1 in any case, and it does not exist to run.

## 8. R02-D-8 — audit of `depth/D03-isolated-verify.md`: 14/15 legs agree, one control is unreproducible

`depth/D03-isolated-verify.md` landed after §1–§7 were written, so this section is the
mission's actual subject: **auditing the isolated verification's evidence**. I rebuilt my own
isolated copy (`.scratch/r02-iso`, §3) and re-ran D03's §2 leg table.

**D03 §2 rows 1–15 — independently reproduced, all 15 exit codes agree.** My I-1..I-12 (§3) plus
D03's additional rows (`assemble-d4-typed --selftest` 12/12, `typed-pipeline-gate` on the packet
20/20, `replay-frozen` on `r31-post` 4/4) match D03's results, and D03's §2 baseline digests match
mine exactly (`aac91246cede8840`, `c23b0ab532cfb9d4`, `d581e0ad5384ce56`, `e6ae9828d6c82aa6`,
`04-lexicon.yml ed7093d6b92111c2`, `13-register-law.yml c0d77181ac567c4c`). Two independent
isolated copies, two seats, same numbers — the §2 leg table is sound.

**D03 §3.2 ("domain-emptied") does not reproduce as written — R02-D-8.** D03 states:

> `domain-emptied` | remove the 8 `L-55..L-62` record blocks | `records=179 register_scoped=0
> derived_pairs=0 claimed_chains=8 borrow_pairs=0 violations=0 rule_holds=0` | 0

I performed exactly the named transform on the live packet (removing the eight `L-55..L-62`
record blocks from the `lexicon:` block, leaving the `registers:` and `register_law:` blocks
untouched) and ran the **isolated** gate:

```
$ python3 -B tools/gates/argot-derivation-gate.py /tmp/r02probe/empty-domain.yml
FINDING D4L-ARGOT-COVERAGE: HOLD — packet declares the argot operation(s) head2, reverse and 6 register-scoped form(s), but no record carries a derived_from/derivation pair; the forecast derivation relation is declared, not delivered
coverage: /tmp/r02probe/empty-domain.yml records=179 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit=1
```

**Three of D03's four numbers differ** (`register_scoped=6` not 0, `borrow_pairs=6` not 0,
`exit=1` not 0), and the emitted finding is the opposite of D03's reading. I then reproduced
D03's exact numbers only by applying a **wider** transform than the one named — removing the eight
records *and* stripping every register-scoping field outside the `registers:`/`register_law:`
blocks:

```
$ python3 -B tools/gates/argot-derivation-gate.py /tmp/r02probe/empty-all.yml
coverage: /tmp/r02probe/empty-all.yml records=179 register_scoped=0 derived_pairs=0 claimed_chains=8 borrow_pairs=0 violations=0 rule_holds=0
exit=0
```

So D03's row is reproducible under *a* transform, but not under the transform the row names, and
the row's stated numbers and exit code correspond to the unnamed one.

**Why this matters, and what it does not change.** D03's §3.2 *conclusion* — "an emptied domain is
silent; this is the r25 failure mode reproduced exactly" — is **half right, and the half it gets
wrong is the load-bearing half**:

- The gating condition is `tools/gates/argot-derivation-gate.py:662`:
  `if declared_ops and counters["register_scoped"] and not counters["derived_pairs"]`.
- Removing only the eight form records leaves `register_scoped=6` (the six loan-layer records that
  inherit a `register` from `LY-01`/`LY-02`), so the hold **fires**: `D4L-ARGOT-COVERAGE`, exit 1.
- `register_scoped=0` — the silent pass — requires the register *declarations* to be stripped too.

So the guard is **not** defeated by removing the derived pairs alone; it is defeated only when the
register scoping itself is gone, and in that case there is genuinely nothing to grade. That is a
materially narrower limit than D03 reports, and it is a *better* result for the leg: the r25
failure mode is largely already closed by the `register_scoped` term. D03's own remedy row
("Owner: whichever seat owns gate changes this round, or a future round") is therefore
**not owed** on the evidence as written — a gate change would be a fix for a defect that the
correctly-stated control does not show. I record this as a **finding against D03's §3.2
provenance**, not a claim that D03 fabricated: the likely cause is that D03's `.scratch-probe/`
file was built by a transform that also dropped the loan-layer/`registers` scoping, and the row's
description of it is incomplete. Re-running D03's exact probe file would settle it; that file is
gitignored (`.scratch/d03/`) and not filed, so it cannot be re-inspected from the record.

**Disposition requested of the parent:** either D03 corrects §3.2's command description and
numbers, or its "coverage-hold limit" owed item is withdrawn as unreproducible. The parent should
not carry D03's §3.2 limit forward as a gate defect without the corrected transform.

## Owed

- `reports/round-36/depth/D03-isolated-verify.md` §3.2 — audited here (§8): §2's 15 legs
  reproduce exactly, but the `domain-emptied` row's named transform does not produce its stated
  numbers (`register_scoped=6`/`borrow_pairs=6`/`exit=1` under the named transform, vs the row's
  `0`/`0`/`0`). Corrected transform is in §8. Owner: D03 or the integrator.
- `reports/round-36/depth/D07-verify.md` — the independent isolated-copy verifier's fragment is
  still absent at my close; it should rebuild `.scratch/d03/iso` from `git archive ce103bf` and
  re-run D03 §2 rows 1–15 and §4 rows 1–4, and re-test §3.2 with the §8 correction.
- `reports/round-36/run-validation.py` — absent, so claim D's declared counting command cannot run
  (§7). Owner: `scribe/S01-integration-draft.md`.
- The register-form leg's baseline row + battery registration (§6) — outside this seat's write
  scope; owner: integrator. Named so the claim's "re-pin as new rows" is not recorded as complete.

## Citations

- Claim and thresholds: `reports/round-36/claims.json` (claim `D`, `before`, `after_required`,
  `counting_commands`, `thresholds`).
- Seat mission / out path / shared rules: `reports/round-36/targets.json` (seat `R02`,
  `shared_rules`).
- Stale-premise sources: `reports/round-25/argot/current-state.md:76,97`;
  `reports/round-25/argot/delta.md:55` (A-7); `SCORECARD.md:312`; closure at
  `reports/round-26/register/forms.md` §1 and `reports/round-30/fixes/qreg-dangles.md`.
- Delivered forms: `examples/culture-d4/components/04-lexicon.yml:236-243`; rule at
  `:252` (`QREG-03`); packet rows at `examples/culture-d4/packet.d4.yml:1009-1183`.
- Legs: `tools/gates/argot-derivation-gate.py` (live `b5406bcdaf41c595…`),
  `tools/gates/register-law-gate.py` (live `15f8b23251ca2ad0…`),
  `tools/check-gate-battery.py:118-131` (`GATE_NAMES`, `D4_GATE_NAMES`, `REGISTER_LAW_GATE_NAMES`).
- Pins: `tools/gates/typed-pipelines.json` (profile `d4`); `examples/culture-d4/expected-holds.json`;
  `tools/gates/expected/register-law-gate/r30-post/expected.json`; the historical rows under
  `tools/gates/frozen/round-{18,22,25,26}/` and `tools/gates/expected/d4-*-check-gate/{r19-pre,r20-post,r22-post}/`.
- Live digests at the census: `packet.d4.yml aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`;
  `packet.d4.typed.yml d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182`;
  `typed-labels.d4.yml c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`;
  `expected-holds.json e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3`.
- Prior-round consumers: `reports/round-28/run-validation.py:232-233`;
  `reports/round-29/run-validation.py:73-75`; `reports/round-30/run-validation.py:67-68`.
- D03 audit (§8): `reports/round-36/depth/D03-isolated-verify.md` §2 (leg table, digests), §3.2
  (`domain-emptied` row), §5 (pin cascade), `## Owed` item 4 (the coverage-hold limit this
  fragment disputes); gating condition at `tools/gates/argot-derivation-gate.py:662`, counter at
  `:562`, hold id at `:50`. Reproductions in `.scratch/r02-iso` over
  `/tmp/r02probe/empty-domain.yml` (named transform) and `/tmp/r02probe/empty-all.yml` (wider
  transform reproducing D03's numbers).
- Battery-dependency history: `reports/round-30/fixes/battery-registration.md:11,50,76,97`;
  `reports/round-30/verify.md:22,45`.
- Baseline discipline: `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`
  (`layout_note`), `…/d4-typed-labels-check-gate/r20-post/expected.json` (`layout_note`).
- Canon: NON-CANON engineering evidence. This seat grants no promotion, clearance, canon or
  closure verdict; canon standing is lore-shokunin's.
