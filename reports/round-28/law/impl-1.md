# R28-D05..D12 (integrator) — the law gains a replay leg, RL-4 closes

- **Seat:** R28-D05..D12 (D axis, law-replay implementation, 8 seats; **this file
  is the integrator's** — one seat owns every touched file). Round 28, loop 3 of
  3, build 4 of 4 — the last build round. Claim **D** `register-law-replay`
  (`reports/round-28/claims.json`).
- **Date:** 2026-10-18. Baseline revision
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (round-27 admit); lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86` ("round-28: declare claims D/O/C").
- **Design authority (siblings, same round, read first):**
  `reports/round-28/law/design.md` (R28-D01 — the leg's three resolutions and the
  six `D4L-LAW-*` classes), `vocab.md` (R28-D02 — the declared vocabularies),
  `rl4-delta.md` (R28-D03 — the RL-4 fix priced, the pin cascade), `review.md`
  (R28-D04). This seat lands what they specified; it does not re-design it.
- **Write scope (every byte this seat wrote):**
  `tools/gates/register-law-gate.py` (**new**),
  `examples/culture-d4/components/03-orthography.yml` (the `packet_keys`
  declaration), `examples/culture-d4/components/09-costumes.yml` (the same),
  `examples/culture-d4/{packet.d4.yml, typed-labels.d4.yml, packet.d4.typed.yml}`
  (regenerated), `examples/culture-d4/expected-holds.json` (re-pinned, new rows),
  `tools/gates/typed-pipelines.json` (re-pinned, new history row), and
  `reports/round-28/law/impl-{1..8}.md`. Scratch under `.scratch/r28-d/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write). No filed
  round-8..27 byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated. No clearance claimed.

## 0. The two round-27 gaps, and where each closes

| gap | round-27 id | closed at |
|---|---|---|
| the law has **no replay leg** — a tampered row is invisible | `review.md` §2 (RL-1) | §2 of this file: `tools/gates/register-law-gate.py` |
| `03-orthography.yml` / `09-costumes.yml` declare no `packet_keys`, so OR/LI/EN never reach the packet | `review.md` §5 (RL-4) | §3 of this file: the two declarations + the regeneration |

Both are **implementation**, not design. The design for each was authored by the
sibling seats this round (`design.md`, `vocab.md`, `rl4-delta.md`) and this seat
lands it rather than re-designing it. The design seat named the intended site and
class set exactly (`design.md` §2, §4 route B, limit `LD-9`), and the landed file
reproduces them.

## 1. The route, and why it is the cheap one

The law sits in the `register_law` block (Route A, round 27). The alternative
(`property.kind: register` rows in `rank_rules`) routes into the family
projector's **costume-rank** resolver, whose `verdict_for` reads `row["material"]`,
`row["garment"]`, `row["badge_office"]` — fields a speech act does not have — and
whose membership guard, widened, turns an honest hold into a silent `not-applies`
(round 27 measured both; `reports/round-27/law/review.md` §3).

This seat builds the **standalone checking leg** instead. It adds **zero** rows,
**zero** holds, and **zero** projector bytes: it reads the packet and reports.

```
$ python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-05, which no delivered record carries: …
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-07, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-02 design_row names QREG-06, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-03 design_row names QREG-08, …
coverage: examples/culture-d4/packet.d4.yml law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=4 findings=4
```

**The four clean-packet findings are real, and §6 records them rather than
laundering them.** The `design_row` tokens name the sibling design seats'
proposed rows `QREG-05..08`, which never landed as packet records; the landed rows
are `RGL-01..05`. That is the design's own measured finding (`design.md` §3.1)
and it is a defect in a **filed round-27 artifact** — not this seat's to rewrite.

## 2. The replay leg

`tools/gates/register-law-gate.py` (new; sha256 `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`).
It parses the packet through the same stdlib YAML-subset reader the family uses
(`tools/gates/naming-collision-gate.py`, loaded read-only by path, digest printed
on every run) and replays **eight resolutions**, each against the packet's own
blocks. Full detail in `impl-2.md`; the finding classes and their controls in
`impl-3.md`.

**Its teeth, measured on the three tampers the round runner builds.** Each tamper
is a textual rewrite of one value (`reports/round-28/run-validation.py`
`tamper_law_text`), never a re-serialization:

| tamper | clean lines | tampered lines | added |
|---|---:|---:|---|
| `force: "no-such-force"` | 4 | 5 | `D4L-LAW-FORCE` |
| `speaker: "nobody-nowhere (ZZ-99)"` | 4 | 5 | `D4L-LAW-SPEAKER` |
| `consequence: "the act evaporates silently"` | 4 | 5 | `D4L-LAW-CONSEQUENCE` |

Round 27 measured **12 = 12** on the same force tamper: no delta. The delta is
now +1 per tamper. That is RL-1 closed.

## 3. RL-4: the `packet_keys` fix

Two one-line declarations, both recorded with their reasoning in the component
headers:

- `03-orthography.yml` — `packet_keys: [orthography, records, literacy_institutions]`
- `09-costumes.yml` — `packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]`

Measured on the regenerated packet: all eight ids now ride a **record** block,
and the `assembly.skipped_keys` ledger no longer routes them away. Full detail,
including what was deliberately *left* component-only, in `impl-4.md`.

## 4. What was regenerated, and the pins that moved

Three generated artifacts rebuilt by the delivered tools (never hand-edited), all
three `--check` byte-identical afterwards; two pin surfaces re-pinned as **new
rows**. Full detail in `impl-5.md`.

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` |
| `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` |
| `examples/culture-d4/expected-holds.json` | `65f5a03e092fb4bb1e04f26d73180ca411c1f91bd29d2f1912d275407e15e423` |

## 5. The acceptance run, at this tree

```
$ python3 reports/round-28/run-validation.py
claim D: PASS
claim O: PASS
claim C: PASS
acceptance_checks_passed: True
```

The D claim's own measurement, read back from the receipt:

| # | condition | measured |
|---|---|---|
| 1 | the law block exists, is component-owned, is machine-readable | 4 `registers` rows + 5 `register_law` rows; declared by `04-lexicon.yml` and `13-register-law.yml`; both in `contract.record_fields` |
| 2 | this runner's own law reader | 4 findings, all `D4L-LAW-DANGLING` (recorded, not graded — the runner grades the delta) |
| 3 | a delivered tool names the `D4L-LAW-*` class | `tools/gates/register-law-gate.py` |
| 4 | a tamper adds a named line over clean | **+1** per tamper, three of three |
| 5 | the three regenerations are byte-identical | `d4-assembly` 0, `d4-adapter` 0, `d4-projection` 0 |
| 6 | the gates are green | argot exit 0 (`violations=0 rule_holds=0`), typed gate **20/20** legs, both D4 adapters exit 0 |
| 7 | RL-4 closed | 8 of 8 ids reach the packet as records; `still_skipped` empty |
| 8 | the hold set revised honestly | revision note names the round-28 landing and the RL-4 fix; 12/0/0 unchanged; `supersedes_pins` carries the r27 pins |
| 9 | the D artifact names the landing and carries a receipt | all five tokens present |

Full command-by-command verdicts, with the wider battery and replay surfaces, in
`impl-8.md`.

## 6. What this seat did not do

- **Did not repair the four `design_row` dangles or the two `CONSEQUENCE`
  class-fit findings.** They are defects of `13-register-law.yml`, a **filed
  round-27 artifact**; repairing it would rewrite a filed byte. Reported with a
  named owner (`design.md` §6) instead. `impl-6.md` records them in full.
- **Did not amend `tools/d2-typed-labels.py`** or `tools/gates/typed-pipeline-gate.py`.
  The standalone route was chosen precisely so no projector byte moves; both
  remain at their round-27 digests and both are green.
- **Did not wire the new gate into the typed pipeline or the battery.** That is a
  deliberate choice with a measured reason: `typed-pipeline-gate.py` is
  byte-pinned GREEN in the filed round-26 manifests, so adding a sibling
  invocation would drift a frozen replay surface the O seat has already swept.
  The leg is discovered by the round runner, which walks every `tools/**/*.py`
  naming the class. Recorded as limit `LD-9`'s successor in `impl-7.md`.
- **Did not register a battery baseline for the new gate.** Registering makes the
  battery *ask* for a committed baseline; without one it reads
  `BASELINE-GATE-UNCOVERED` and forces exit 2. The gate therefore stays outside
  the nine-gate registered set and is exercised by its own `--selftest` and by the
  round runner. Stated, not left implicit.
- **Did not touch the RL-3 ceiling** — that is claim C's, and this seat reads its
  measurement only.
- **Did not commit or push.**

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/register-law-gate.py --selftest | tail -1            # 33/33
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 tools/assemble-culture-d4.py --check                             # byte-identical
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1   # 20/20
python3 reports/round-28/run-validation.py                               # D/O/C PASS
sha256sum examples/culture-d4/{packet.d4.yml,typed-labels.d4.yml,packet.d4.typed.yml,expected-holds.json} tools/gates/register-law-gate.py
```
