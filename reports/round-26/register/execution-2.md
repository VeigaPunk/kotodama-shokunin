# R26-D14 — argot execution 2: controls (tamper, discrimination, exit codes)

- **Seat:** R26-D14 (D axis, argot execution 2 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`. Stamps UTC.
- **Write scope:** `reports/round-26/register/execution-{1..4}.md` only; scratch
  under `.scratch/r26-d13/` only. No tool, gate, packet, component or filed
  rounds 8–25 byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

Execution 1 established the positive result. A green leg with no control is not
evidence; this execution supplies the negatives. Every fixture lives in scratch
and is run through the **unmodified** gate
(`tools/gates/argot-derivation-gate.py`, sha256 `5b5abe78…`).

## 1. The control battery

Harness: `.scratch/r26-d13/argot-controls.py` (scratch, this seat). Each fixture
is a minimal packet in the gate's declared YAML subset: one register-scoped form
record per rule family, one declared rule. Mutations are single-token edits of
the positive fixture.

```
$ export TMPDIR=$PWD/.scratch
$ python3 .scratch/r26-d13/argot-controls.py --outdir .scratch/r26-d13/controls
```

| # | control | injected change | exit | ids emitted |
|---|---|---|---|---|
| 1 | `positive` | none (the pair is correct) | **0** | — |
| 2 | `reverse-wrong` | `term: nim` → `min` (form ≠ `reverse(min)`) | **1** | `D4L-ARGOT-DERIV` |
| 3 | `head2-wrong` | `term: saalu` → `saalum` (the maximal-**coda** reading) | **1** | `D4L-ARGOT-DERIV` |
| 4 | `rule-wrong` | `term: tikmes` → `tikmess` (declared `CX-01` does not yield it) | **1** | `D4L-ARGOT-DERIV` |
| 5 | `op-unknown` | `op: reverse` → `metathesis` (no such operation or rule) | **1** | `D4L-ARGOT-RULE` |
| 6 | `base-missing` | drop `derived_from` (the half-pair shape) | **0** | — (silent; see §3) |

Measured 2026-10-18T18:02:50Z; full JSON receipt
`.scratch/r26-d13/controls.json`. The verbatim messages:

```
reverse-wrong:
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form C-01 'min' (register 'quote'):
  declared chain 'reverse' applied to 'min' yields 'nim'; the stated inputs and
  rules do not yield the candidate

op-unknown:
FINDING D4L-ARGOT-RULE: HOLD — register-scoped form C-01 'nim': declared
  derivation 'metathesis' is neither a declared argot operation (head2, reverse)
  nor a licensed packet rule (CX-01); replay is not possible
```

Each finding names the record id, the register, the declared chain, the base,
the replayed value and the delivered value — a reader can see *what* disagreed,
not only *that* something did.

## 2. The head2 control is the design's own load-bearing row

Control 3 mutates `saalu` → `saalum`, the reading the design explicitly rejects
("`saalumi` → `saa.lu.mi` → **`saalu`** — explicitly **not** `saalum`, which a
maximal-coda reading would give", `design-language.md:191-196`). The gate's
syllabifier is maximal-onset, so it replays `saalu` and fails the mutated
`saalum`. The control therefore tests **the one row where the two readings
disagree** — the row the design says is why the algorithm is stated at all. It
fires.

## 3. What the battery does *not* catch — named, not silently dropped

Control 6 (`base-missing`) exits **0 with no finding**. Dropping `derived_from`
while keeping `derivation` leaves a record that declares a derivation but no
base, and the gate's `declared_derivation` (`argot-derivation-gate.py:320-340`)
falls back to `derivation.base` — so the pair is still complete and replays
clean. That is correct behaviour for that shape (the base is stated once, in the
mapping), **not** a hole; but it means the battery does not exercise the
genuinely half-declared record (a `derived_from` with **no** `derivation`, or a
`derivation` with no base anywhere). That shape is the lane runner's
`half_pairs` leg (`run-validation.py:611-630`), and it is not this gate's
graded surface. Recorded so the control set is not read as covering it.

Two further gaps are the design's own and are **not** re-discovered here; they
are named in `reports/round-26/argot/D21-adversarial-replay.md` and
`reports/round-26/argot/D22-label-typing-crosscheck.md` (a register form with no
declared derivation is silent; no inventory check; no label-kind concept). This
execution's controls neither close nor contradict them.

## 4. Exit codes and the delivered-surface guarantee

- Every control that *should* fire exits **1**; the positive exits **0**; no
  control exits **2**. The leg is measuring, not failing to read.
- The malformed-input path (`D4L-ARGOT-DATA`, exit 2) is the gate's own fixture
  control (`--selftest` → `malformed-root-is-a-string-exit-2`,
  `malformed-unclosed-flow-exit-2`, `malformed-tab-indent-exit-2`, all `ok`); it
  is not re-run here.
- `python3 tools/gates/argot-derivation-gate.py --selftest` → **`21/21 checks
  passed`**, exit 0 (re-run 2026-10-18T18:00Z).
- The delivered tree is unmodified by this execution: every fixture and receipt
  is under `.scratch/`, and `git status --porcelain` over `examples/` and
  `tools/` is empty at this seat's stamps.

## 5. The control the forecast asked for (C-02)

The round-17 brief's required-controls battery row C-02 is "quote form ≠
`apply(op, base)` → FAIL, id `D4L-ARGOT-DERIV`" (`design-brief.md:456`). Control
2 of §1 is exactly that shape and fires the id. Over the **enriched candidate**
the same control is exercised at stratum scale by the design's own
`probe-bad.yml` (`RF-02 kit` → `kat`), which this seat re-ran independently:

```
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form RF-02 'kat' (register 'stamp'):
  declared chain 'reverse' applied to 'tik' yields 'kit'; the stated inputs and
  rules do not yield the candidate
coverage: … register_scoped=14 derived_pairs=8 violations=1 rule_holds=6
exit 1
```

So C-02 is satisfied on both the minimal control and a stratum-scale fixture,
and the id it names is emitted by a live code path.

## 6. Limits

- The controls tamper **forms and operations**, not the packet's YAML structure
  (that is the gate's own malformed-fixture class) and not the rule table's
  `pattern`/`output` internals (the gate's `D4L-ARGOT-RULE` HOLD class, exercised
  by the design's `probe-rule2-nopair.yml`, which this seat re-ran: 6 HOLDs
  naming the missing pair, exit 1).
- This file claims no repair. The `lengthen`/`LENGTHEN` case defect execution 1
  names is a landing-time consistency item for the D data owners, not a gate
  bug: the gate's exact-match behaviour is what the replay discipline requires.
