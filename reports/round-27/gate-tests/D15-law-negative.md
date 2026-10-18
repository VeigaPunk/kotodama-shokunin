# R27-D15 — negative: a register-law violation is caught

- **Seat:** R27-D15 (gate runs 3 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law`. Assignment: *"negatives (a law violation caught …)"*.
- **Date:** 2026-10-18. Declared baseline `4f09c990…`; lane HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` at every measurement.
- **Write scope:** as D13 (`reports/round-27/gate-tests/**`), plus gitignored
  scratch. **The control copies the working tree into `.scratch/r27-d13/`, never
  the lane worktree.** No tool, gate, packet, component, projector, pin, fixture
  or filed rounds 8–26 byte written; no commit, no push.
- **Canon:** NON-CANON. The plant is a mutation of a delivered record; it is a
  probe, not a claim about a language.

## 0. Verdict

**A register-law violation is caught: the packet's own era law is violated by a
planted restage, and the named instrument adds a finding the clean tree does not
carry — then the restored tree returns to the baseline verdict exactly.**

| step | exit | findings |
|---|---:|---|
| baseline (lane tree, no plant) | 1 | `['L6b-HOLD', 'L9-HOLD']` |
| clean **copy** of the working tree | 1 | `['L6b-HOLD', 'L9-HOLD']` — identical to baseline |
| copy + plant `L-55 stage: E1 → E0` | 1 | `['L4-FAIL', 'L6b-HOLD', 'L9-HOLD']` — **added: `L4-FAIL`** |
| restored tree (component written back) | 1 | `['L6b-HOLD', 'L9-HOLD']` — **identical to baseline** |

The two baseline holds are the honest state of the claim's *enforcement* leg
(`L6b`: the law is a declaration with no teeth; `L9`: the `register_law` block
is not declared in the assembler's `PACKET_KEYS`/`RECORD_FIELDS`, so its record
validator has no field list for it). Neither is a defect in the law's *content*;
both are named and owned elsewhere. The plant adds exactly one finding and
removes none, which is what makes it a control.

The added finding names the planted record:

```
FINDING L4-FAIL: stamp record(s) staged before E1: L-55
```

## 1. Why the plant is a law violation and not an arbitrary mutation

The packet **declares the law it is violated against**. `RGL-05` — landed this
round at `examples/culture-d4/packet.d4.yml:2668`, in the new `register_law`
block — carries:

> *"consequence: every stamp form is available_from E1 … an E0 stamp claim is a
> defect and E3 is reserved and unoccupied"*

and `QREG-04` (`:1344`) states the same as the register's own era rule. `L-55`
(`tuum`) is a delivered register form, `axis: fire`, `stage: E1`
(`examples/culture-d4/components/04-lexicon.yml:238`). Restaging it to `E0` puts
a delivered register form into an era the packet's own law forbids — so the
violation is **carried by the delivered bytes**, not asserted by the fixture.

The plant is applied to the **component**, then rebuilt through the lane's own
three-step pipeline (`assemble-culture-d4.py` → `d2-typed-labels.py --emit` →
`assemble-d4-typed.py --emit`), so the mutated record reaches the packet by the
same route a real edit would.

### 1.1 Two corrections this seat made to its own control, by running it

Both were found by measurement, not by reasoning, and both are preserved here
because a control's history is part of its evidence.

**(a) The anchor must name `L-55`.** The first version used a bare
`layer: native, stage: E1,` anchor. It replaced the **first** such occurrence,
which is `L-45` — a compound record that is **not** register-scoped. The era law
never saw it, the plant added no finding, and the seat's own check read **red**.

**(b) The control must baseline the working tree, not `git clone`.** The second
version cloned the repo. At this stamp the entire round-27 landing — component
13, the `register_law` block, the syllabify fix — is **uncommitted**, so a clone
of HEAD carries the **pre-law** tree: its baseline read `['L6-HOLD']` while the
lane tree read `['L6b-HOLD']`, and the revert check compared two different
trees. The control now copies the working tree and adds an explicit **clean-copy
check** (§0's second row) so a difference at the plant cannot be the copy.

**A control that plants into the wrong record, or baselines the wrong tree, is
not a control.**

## 2. The instrument, and why this seat does not write its own

The detector is **peer seat X59's** independent auditor,
`reports/round-27/audit/x59-register-law-negatives.py` (sha256
`52672606888e155ddaa1c8d3b710d3999586a4037d4a2ae725339ed794cfcb2a` at this
stamp). It audits nine law rows (`L1` REGISTER-BLOCK, `L2` UNMARKED-SET, `L3`
OPERATION-RULE, `L4` ERA-LAW, `L5` ADMISSIBILITY, `L6` LAW-ROWS, `L7`
OATH-VOID, `L8` DOUBLET-RESOLVES) on deliberately different machinery from the
lane's argot gate: a full YAML 1.1 loader (`ruby -ryaml`) instead of the naming
gate's subset reader, and its own re-implementations of `reverse`/`lengthen`.

**This seat did not re-implement it, and did not fall back to a private
checker.** A negative is only a negative if a **named** instrument catches it; a
detector written by the seat that plants the defect proves only that the seat can
find its own plant. Where the named instrument is absent, the runner records a
gap instead of substituting one.

## 3. The baseline verdict, recorded rather than assumed clean

The lane tree reads `['L6b-HOLD', 'L9-HOLD']` at this stamp:

```
FINDING L6b-HOLD: a tampered law value is not a finding in any delivered gate
(measured: the tampered packet emits the same finding set as the clean one): the
law is a declaration with no teeth — the enforcement leg is unowned
FINDING L9-HOLD: the `register_law` block is landed and every row carries an
`id`, but the assembler declares it in neither `PACKET_KEYS` nor `RECORD_FIELDS`
counters: … law_rows=5 law_wiring_checked=5 register_law_block=5
           speech_act_rows=5 …
```

This is the **post-landing** reading and it is *different in kind* from the
pre-landing one. Before the law landed, `L6` read:

```
FINDING L6-HOLD: the register block declares the register IDENTITY (QREG-01..04)
but no speech-act law rows …
```

So the instrument itself tracked the landing: `law_rows` moved **0 → 5**,
`register_law_block` is now **5**, and the hold moved from *"the law is absent"*
to *"the law is present but unenforced"*. **That second hold is the correct and
honest state of the claim**: the law has landed as a declaration (the claim's
`after_required`), and the enforcement leg is unowned — which the landed
component's own `law_binding.enforcement` field says in its own words, and which
`reports/round-27/law/design.md` §5 prices at seven changes (E-1..E-7).

A control that demanded "clean" on the lane tree would fail on that honest hold.
So the discrimination check is stated against the **baseline verdict**:

- the clean copy must reproduce the baseline **exactly** → `['L6b-HOLD', 'L9-HOLD']`;
- the plant must **add** a finding the baseline does not carry → `L4-FAIL` added;
- the restored tree must return to the baseline **exactly** → `['L6b-HOLD', 'L9-HOLD']`.

## 4. The instrument's own controls

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py --controls
control-1-op-contradicts-axis      ok  law=L3  findings=3
control-2-early-era                ok  law=L4  findings=3
control-3-form-mismatch            ok  law=L3  findings=3
control-4-stray-construction       ok  law=L5  findings=3
control-5-oath-in-register         ok  law=L7  findings=3
control-6-dangling-doublet         ok  law=L8  findings=3
control-6b-law-row-without-id      ok  law=L9  findings=2
control-7-clean-stays-clean        ok  law=no-FAIL  findings=2
controls: 8/8 caught
```

Eight planted law violations, one per row it can plant, plus a clean control that
stays clean. The clean control passes on a tree that still carries `L6b-HOLD`
because the instrument draws its own line: it asserts *no FAIL*, not *no
finding*, so a HOLD on an unenforced law does not make the instrument's own
clean control red. That is the right line — the HOLD is a statement about the
delivered surface, not about the instrument.

Two earlier revisions of the peer file are recorded here as **superseded**
readings, not as defects — the peer seat was mid-edit through the wave, and the
lane's rule is that a re-pin is a new row, never an in-place edit:

| revision | sha256 | reading |
|---|---|---|
| 19:18Z | `1c64798e…` | `6/7`, `control-7` = `MISS` (the clean tree carried `L6-HOLD`) |
| 19:3xZ | `7e3b3559…` | `7/7` |
| final | `52672606…` | **`8/8`** (adds `control-6b-law-row-without-id`, law `L9`) |

**A peer instrument that crashes is recorded, not read as a red.** Mid-wave the
file was briefly in a state where it raised `NameError: name 'ROOT' is not
defined`. A crash is *could-not-evaluate*: it says nothing about whether the
plant is caught. The runner detects a traceback or an out-of-contract exit
(`not in (0, 1, 2)`), records the instrument's digest and tail as a **named gap**,
and skips the discrimination checks rather than reporting them as if the plant
had failed. That keeps a peer's transient breakage from being published as this
seat's negative failing.

## 5. Limits

- **One plant, one law row.** This seat shows the **era** law (`L4`) has teeth.
  The other seven rows are X59's own controls (`7/7 caught`, §4), not this
  seat's.
- **The plant is a mutation, not a language claim.** `L-55 → E0` describes no
  world; it exists to make the detector answer.
- **Green here says nothing about the law's completeness or enforcement.** It
  says a violation of a declared law is caught. Whether the law is *sufficient*
  is the design seats' question, and whether it is *enforced* is unowned —
  `L6b-HOLD` is still open, by design.
- **Stamp-bound and mid-wave.** The round-27 landing is uncommitted; if a further
  edit lands, both the baseline verdict and the peer's control-7 change. The
  runner re-measures both, so the refresh is one command.
