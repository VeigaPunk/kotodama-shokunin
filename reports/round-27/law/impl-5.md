# R27-D09 — the control battery: what fires, what does not, and the gap stated plainly

- **Seat:** R27-D09 (D axis, register law + syllabify implementation 5 of 8).
  Round 27, loop 3 build 3 of 4, claim **D** `register-law`. Integrator:
  `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990…`; declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The harness, and the rule it runs under

Every control is a single-token mutation of the **live** packet, written in
place, run against the **unmodified** gates, and followed by a byte-for-byte
restore verified with `cmp`. Scratch receipts:
`.scratch/r27-d/ctl/controls-inplace.json`, `syllabify-control.json`.

**A trap this harness had to learn, and it is worth recording.** A control run on
a *copy* of the packet under `.scratch/` reports `findings_total=16` where the
identical bytes at `examples/culture-d4/packet.d4.yml` report `findings_total=12`
— because `tools/d2-typed-labels.py` resolves the D2 rank component relative to
the packet's own directory. Measured:

```
$ cmp examples/culture-d4/packet.d4.yml .scratch/r27-d/ctl/clean.yml && echo identical
identical
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml    | grep -o findings_total=[0-9]*
findings_total=12
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-d/ctl/clean.yml        | grep -o findings_total=[0-9]*
findings_total=16
```

A control run out of place therefore measures the wrong baseline and would have
reported a 4-hold "regression" that does not exist. Every control below is run
in place for that reason.

## 2. The battery

| # | control | injected change | result | reading |
|---|---|---|---|---|
| C-1 | `law-tampered` | `RGL-01.force` → `no-such-force` | `findings_total=12`, argot `violations=0 rule_holds=0`, both exit as clean | **no finding — gap** |
| C-2 | `law-dropped` | the `RGL-05` row removed | `findings_total=12`, identical | **no finding — gap** |
| C-2b | `law-kind-stripped` | `RGL-01.kind` removed | `findings_total=12`, identical | **no finding — gap** |
| C-3 | `head2-coda-reading` | a register form `saalum` declaring `derivation: head2` from `saalumi` | `FINDING D4L-ARGOT-DERIV`, exit 1, gate replays `saalu` | **fires, correctly** |
| C-3b | `head2-onset-reading` | the same row with `saalu` | exit 0, no finding | **clean, correctly** |

Verbatim, C-3:

```
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form PR-01 'saalum' (register 'quote'):
  declared chain 'head2' applied to 'saalumi' yields 'saalu'; the stated inputs and
  rules do not yield the candidate
```

## 3. What the law controls prove — and it is a negative result

C-1, C-2 and C-2b produce **the same finding count as the clean packet**. Three
independent mutations of the law — a bogus illocutionary force, a deleted row, a
deleted clause classifier — are invisible to every delivered gate.

This is the sibling design's `LL-3` and its review's `RL-1`, and this seat's
measurement confirms it independently: *"the law has no replay leg; a tampered
law row produces the same 12 findings as a clean one."* The law is a
**declaration**, exactly as enforceable as `QREG-02`'s prose was before this
round.

**It is reported as a gap, not presented as a pass.** The claim's
`after_required` asks that the law be *wired into the packet deterministically*
— which it is, and which the lane runner grades — and does not ask for a replay
leg. Building one would require a semantic amendment to the family projector
(`tools/d2-typed-labels.py`), whose full price the sibling design measured as
seven items E-1..E-7 (`reports/round-27/law/design.md` §5), including a new
dispatch branch that resolves a speech act against a **speech** row rather than a
costume row. That amendment is not this seat's to open, and the sibling review
records the same conclusion: *"widening the guard is worse than the hold"*
(`review.md` §3) — it converts an honest `D2L-RANK` hold into a silent
`not-applies`.

## 4. What the law controls do *not* leave unguarded

The gap is enforcement, not coverage. The lane runner's `law_clause_coverage`
leg reads the rows' own text and fails if any of the three named clauses
(admissibility / by-agent / record-consequence) is missing, and it fails if any
row omits a universal record field (`id`, `axis`, `evidence`, `follows`).
Measured on the landed rows:

```
"clauses": {"admissibility": true, "agent": true, "consequence": true}
"rows_with_universal_fields": 5, "rows_total": 5
```

So a row that loses its `act`, its `speaker` or its `consequence` **is** caught —
by the acceptance runner, at claim level. What is not caught is a row that keeps
all its fields and states something false. That distinction is the honest
boundary of this fragment: **schema coverage is measured; semantic truth is
declared.**

## 5. C-3 and C-3b are a matched pair, deliberately

C-3 fires and C-3b does not, on the design's own named row. A control that fires
on both would be measuring nothing; a control that fires on neither would be
measuring nothing either. The pair pins the syllabify fix to the one site the
design says is why the algorithm is stated at all
(`design-language.md:191-196`: the two readings disagree on exactly this row),
and it is the same trap the gate's committed fixture carries as `Q-11`.

## 6. The gate's own selftest is the battery's floor

```
$ python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
selftest: 27/27 checks passed                                  # was 21/21
$ python3 tools/check-gate-battery.py | tail -6
"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0
```

Six new checks pin the syllabify fix and its refusals (§ `impl-3.md` §5). The
battery's duty-1 mirror confirms the seven structural gates' originals are
preserved and their selftests green; duty-2 confirms all nine registered gates
carry pinned baselines.

## 7. Limits of this battery

- Mutations are **single-token text edits** of the live packet. The gate's own
  malformed-input class (`D4L-ARGOT-DATA`, exit 2) is exercised by its selftest,
  not re-run here.
- The battery does not tamper `tools/d2-typed-labels.py` or
  `tools/assemble-culture-d4.py`; their own selftests (163/163, 81/81) carry
  those controls.
- The battery does not exercise the era leg (`RGL-05`'s substance): the gate has
  no era concept, and the sibling design measured the same gap as `RL-8`
  (`rules.md` §5). C-2 deletes the *row*; nothing tests an E0-dated stamp form,
  because nothing can.

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
cat .scratch/r27-d/ctl/controls-inplace.json
cat .scratch/r27-d/ctl/syllabify-control.json
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
python3 tools/check-gate-battery.py | tail -6
```
