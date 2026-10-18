# R30-D28 — five-section composition and delivery review

- Date: 2026-10-18. Axes: depth, operability, historical non-regression.
- Deliverable reviewed: `reports/round-30/craft/skill-draft.md`. Self-review only; not a non-author verifier mark.
- Change boundary: the draft is insert-ready. No SKILL.md/shared file, old receipt, pin, component or tool is edited by this seat.

## The five existing sections remain distinct inputs

| Existing SKILL.md section | Invariant carried into Register craft | Why the new section needs it / witness |
|---|---|---|
| Label typing — translated labels, native forms, borrowed strata | Form kind and provenance are decided before register arithmetic. Legal inventory is not native provenance; borrowing retains donor/adaptation and two clocks | A register is not a fourth form kind and cannot exempt sound bytes. `reports/round-26/register/impl.md` §5; `corpus/knowledge/synthesis/era-language-staging.md` §7 |
| Claim uncertainty typing — supported / partial / unresolved | Each exact claim/edge has a resolving basis; evidence strength is independent of fictional truth and canon status | A successful arithmetic leg cannot upgrade law semantics, historical attestation or a coupled institutional edge. `reports/round-15/handoff/v2-design.md` §2; `corpus/knowledge/synthesis/worldbible-integration-contract.md` §§4,8 |
| Slot-label routing — one row per moved record, the owed slot named once | Move a translated label, do not delete it; routed record IDs equal held record IDs, while design obligations and projected rows are different counts | Supplied register forms do not manufacture a register-unresolved class or clear garment slots. `reports/round-18/d4/holds.md` §4; `reports/round-26/register/impl.md` §5 |
| Derivation replay — replay the family's own build, by text transform | Family assembler identity, named inputs, text fidelity, independent expectations, deterministic builds and append-only new pins are separate checks | Arithmetic replay of forms and reproduction of a frozen artifact are not synonyms. `reports/round-18/d4/manifest.md` §§2,6; `reports/round-29/defects/fix-14.md` |
| Family-clean projection — a family's owned fields cite that family's own records | Choose family-local data and provenance structurally; shared code is permitted, embedded foreign fixture data is not | Same spelling, ID or a linguistic borrowing declaration cannot import the wrong family's registers, offices or ledger. `reports/round-22/bleed/design.md` §§Decision,Required paired controls |

The proposed section also names the seven historically omitted supporting
surfaces and the two new register gates. That is an inventory/discoverability
repair, not a claim that every helper is a user-facing gate or that merely
naming a tool executes it. Box-1 counting and its control are in
`reports/round-30/craft/review-D29-box1.md`.

## Dated direct-command checks

At **2026-10-18T21:53:04Z**, a concurrent read-only batch ran the commands below
with `TMPDIR=$PWD/.scratch`; the relevant packet/projection/adapter/profile
read-set hashes were identical before and after the batch:

```sh
export TMPDIR=$PWD/.scratch
python3 -B tools/assemble-culture-d4.py --check
python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 -B tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
```

All exited **0**. Assembly, projection and typed packet were byte-identical;
the typed gate passed **20/20** legs and retained **12** owed-form HOLDs.
The source packet is the operand of the normal typed-gate command, not its
derived typed-packet output.

At **2026-10-18T21:53:42Z**, these commands also ran:

```sh
export TMPDIR=$PWD/.scratch
python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
python3 -B tools/harness/packet_uncertainty.py --selftest
python3 -B tools/harness/packet_links.py --selftest
python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml
```

The first three exited **0**: projection adapter byte-identical, uncertainty
**19** checks, links **38** checks. The assembly adapter exited **1**, reporting
a difference. The component owner was concurrently landing QREG records; its
own `reports/round-30/fixes/qreg-dangles.md` declares regeneration/pin work
in progress. This later result does **not** invalidate the earlier stable
batch and is not asserted to be a persistent adapter regression: it is a
separate measurement with no stable component-snapshot proof. A fresh settled
assembly-adapter check is required for final integration.

At **2026-10-18T21:54:54Z**, `python3 -B tools/check-gate-battery.py` returned
exit **2**: structural selftests **7/7** passed, **19** discovered baselines
were pinned, live originals were preserved, but registered coverage was
**9/10** and the new law gate had **BASELINE-GATE-UNCOVERED**. This is the
expected fail-closed dependency documented by the registration owner in
`reports/round-30/fixes/battery-registration.md`, not a claim of green
regressions. The orchestrator/baseline owner owes a new law baseline against
settled data and gate bytes. Do not weaken the coverage requirement or revive
the old nine-gate wording to obtain a zero exit.

## Successor assembly check

At **2026-10-18T21:56:24Z**, a before/after hash-stable batch re-ran
`python3 -B tools/assemble-culture-d4.py --check` and
`python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml`,
with `export TMPDIR=$PWD/.scratch`. Both returned **0**, byte-identical
deterministic assembly, for QREG successor packet SHA-256
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`.
This is the new control that resolves the earlier assembly-adapter observation;
it does not erase that recorded transient or close the separate law-selftest
and missing-law-baseline dependencies.

## Adversarial-review precision changes

`reports/round-30/craft/review-D30.md` recommends two bounded documentation
changes. D30-P1 is applied in the projection-adapter row: its forwarded verdict
is explicitly the projector's **`--check` byte-identity** result, not the
label-findings verdict. The control is the source read at
`tools/gates/d4-typed-labels-check-gate.py:48-56` plus the dated adapter exit-0
run above, which coexists with the typed pipeline's twelve owed-form HOLDs.
D30-P2 is applied by explicitly dating the ceiling example
**2026-10-18T21:53:04Z** and calling packet `543d68a8…` pre-integration.
The review's **2026-10-18T21:56:36Z** successor ceiling command records the
same ratios on `aac91246…`; no old digest or result is silently relabeled.
No executable change or historical rewrite is made for either wording fix.

## Deliberate non-claims

- No frozen mirror was launched by this seat, and no historical acceptance runner that writes filed receipts was run. The live-tree/root-relative replay defect remains explicit via `reports/round-29/defects/fix-14.md`; a pin-verification battery is not a verdict replay.
- No new handoff generation was frozen. `tools/exercise-handoff-e2e.py` is indexed with explicit successor-baseline selection; the draft does not claim its old rendered count prose has become current merely because the executable is named. See `reports/round-29/defects/routed.md` §Fresh v3 renderer claim drift.
- No source-access, lore receipt/acceptance, canon, rights or permission finding is inferred. The register choices are NON-CANON system design; every open edge retains its own uncertainty and owner.
- Final round-30 regression/acceptance verification and post-landing box-1 re-survey remain orchestrator actions. The draft and these checks are evidence, not their substitute.
