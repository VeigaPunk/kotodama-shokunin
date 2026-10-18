# R27-D12 — the seat's own account: what was measured, what was found, what is left

- **Seat:** R27-D12 (D axis, register law + syllabify implementation 8 of 8).
  Round 27, loop 3 build 3 of 4, claim **D** `register-law`. Integrator:
  `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`;
  declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`. Every
  scratch-writing command was preceded by `export TMPDIR=$PWD/.scratch`.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated.

## 1. The claim, and the verdict

`reports/round-27/claims.json` claim **D** requires: "The register law lands: a
D4 component declares the stamp register's speech-act rules (what may be said
in-register, by whom, with what record consequences), wired into the packet
deterministically; the syllabify disagreement fixed (one algorithm, forms
re-verified); the argot gate + typed gate + assemblers all green with the amended
packet; named holds updated."

| clause | verdict | evidence |
|---|---|---|
| a D4 component declares the law | **met** | `13-register-law.yml`, new, `packet_keys: [register_law]`, RGL-01..05 |
| the three named clauses present | **met** | `clauses: {admissibility: true, agent: true, consequence: true}`, 5/5 rows carry the universal fields |
| wired into the packet deterministically | **met** | three byte-identical regenerations, all exit 0; contract declares the block |
| the syllabify disagreement fixed, one algorithm | **met** | 0 of 70 disagreements against a corrected legality-constrained reader; `is_legal_syllable` states the predicate |
| all 62 forms re-verified | **met** | 62-form set re-run before/after; all 70 delivered forms re-verified |
| the 15 disagreements named before/after | **met, with a correction** | §2 — the pre-fix count was 59 of 62, not 15; round 26's reader was wrong |
| argot gate + typed gate + assemblers green | **met** | argot 0/0, typed 20/20, three regenerations exit 0, battery 7/0/0 |
| named holds updated | **met** | `expected-holds.json` re-pinned, 12/0/0 unchanged, round-27 `revision_note` |

**Lane runner:** `python3 reports/round-27/run-validation.py` → **`claim D: PASS`**.

## 2. The two findings this seat contributes beyond its assignment

### 2.1 The pre-fix disagreement count was wrong by a factor of four

The claim's `before` cites round 26's "15 of 62". Re-measuring with the
corrected legality-constrained reader, **59 of 62** forms disagreed before the
fix — not 15. Round 26's own reader (`.scratch/r26-d-reg/syl.py`, still on disk)
produced `saalumi → saal` in the same output where it reported the design's
worked row `saalu` as agreeing, so its row list is not reproducible from the
delivered bytes. Reported rather than quietly replaced, because the claim cites
the number.

### 2.2 A control run out of place measures the wrong baseline

`tools/d2-typed-labels.py` resolves the D2 rank component relative to the
**packet's own directory**. Two byte-identical packets therefore report different
finding counts:

```
examples/culture-d4/packet.d4.yml          findings_total=12
.scratch/r27-d/ctl/clean.yml  (identical)  findings_total=16
```

Every control in this seat's battery was therefore run **in place** with a
verified byte-for-byte restore. A control harness that copies the packet out of
tree would have reported a 4-hold regression that does not exist. Recorded
because the same trap applies to any future seat running packet-level controls.

## 3. The gaps this seat did NOT close, named

| id | gap | owner |
|---|---|---|
| `LL-3` / `RL-1` | the law has **no replay leg**: a tampered or deleted law row is invisible to every delivered gate (measured three ways, `impl-5.md` §2) | the family-projector amendment the sibling design priced as E-1..E-7 |
| `RL-8` | the **era leg** (`RGL-05`'s substance) is unimplemented: the argot gate has no era concept, so an E0-dated stamp form produces no finding | whoever grows the leg |
| `RL-4` / `LL-8` | `RGL-01`'s `mold-keeper` names an office **absent from the packet** (`03-orthography.yml` declares no `packet_keys`) | a component/schema decision, not this seat's |
| — | the `handoff-v3` regression reads the filed round-22 baseline and now reports `E2E-DIGEST` naming this landing's five D4 read-set files | the O seat's re-point (A/B control in `impl-4.md` §2) |
| — | the O seat's r27 pinsweep generations were frozen at **pre-landing** digests | the O seat's re-freeze |
| — | `design-language.md`'s prose still does not state the legality predicate the gate now implements | the owner of that filed round-17 byte |

## 4. Digest ledger (the bytes this seat's readings bind to)

```
tools/gates/argot-derivation-gate.py                     b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb
examples/culture-d4/components/13-register-law.yml       c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
examples/culture-d4/components/01-brief.yml              649aa111db2e57a737234330690ea4fbb197039ba8ecf92d6248d1bed8ea793b
examples/culture-d4/packet.d4.yml                        86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
examples/culture-d4/typed-labels.d4.yml                  88a94422b4123f6b436f9935590d69f081f90e688655ee605f33e0c1305fb68d
examples/culture-d4/packet.d4.typed.yml                  1c4b88088b696a131f71af69ad14dda518acdec83dc7e873cfcad6fae5fc2660
examples/culture-d4/expected-holds.json                  857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f
tools/gates/typed-pipelines.json                         69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a
```

Pre-landing, for the before/after comparison:
`packet.d4.yml dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67`,
`argot-derivation-gate.py 5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211`.

## 5. Coordination note: this seat landed while a sibling was reviewing

The round-27 law **design** seats (R27-D01..D04) authored
`reports/round-27/law/{design,rules,review}.md` concurrently, and their reviewer
measured this seat's first revision mid-flight and recorded it in their
`review.md` §9a — confirming the zero-new-holds prediction and naming two gaps
(no `force` field; the block undeclared in the contract). Both were closed in
revision 2 (§ `impl-6.md` §4, `impl-2.md` §2). This seat did not read those
sibling artifacts before landing — the design's route and the reviewer's
observations were reconciled **after**, and the reconciliation is recorded rather
than presented as if it had been planned. No sibling file was written.

## 6. What this seat did not do

- Did not write any file outside its declared scope; did not touch
  `reports/round-27/law/{design,rules,review}.md`, `pinsweep/`, `readme/`,
  `audit/`, or `scribe/`.
- Did not modify a filed round-8..26 byte; every superseded pin is a **new row**.
- Did not edit `tools/d2-typed-labels.py`, `tools/assemble-culture-d4.py`,
  `tools/assemble-d4-typed.py`, or `tools/assemble-d2.py`.
- Did not open a family-projector amendment to give the law a replay leg.
- Did not decide the canon question, claim any form as attested, or run a
  real-language resemblance screening.
- Did not `git commit` or `git push`.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-27/run-validation.py                     # claim D: PASS
python3 tools/assemble-culture-d4.py --check
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
python3 tools/check-gate-battery.py | tail -6
sha256sum tools/gates/argot-derivation-gate.py examples/culture-d4/components/13-register-law.yml \
          examples/culture-d4/packet.d4.yml examples/culture-d4/expected-holds.json tools/gates/typed-pipelines.json
```
