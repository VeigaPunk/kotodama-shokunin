# R18-D20 — reviewer 4/4: SKILL and capability-row drafts, and what may be admitted

- round: 18 (loop 2 of 3, build 2 of 4; 64 workers, `opencode-go-2/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **D** (and the D-side reading of claim O).
- assignment (verbatim): "D R18-D17..D20 (reviewers x4): hold-set hand
  re-derivation; circularity (did the re-pin bless its own change?); cross-check
  vs D2/D3 lessons; SKILL/capability-row drafts; reports/round-18/d4/review-{1..4}.md."
- date: 2026-10-18, stamps UTC. Evidence window 10:19:20Z–10:33Z. HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`. The generalized gate was landing
  throughout: shas `d102fd1d…` (pre) → `b4232690…` → `bba60bc1…` → `edfec5f3…`
  → `7fad95e0…` (10:31Z, 38873 B at the last size read).
- canon: NON-CANON engineering review. Nothing here admits a capability, a
  round, or a canon fact; the parent owns admission and placement.
- writes: **this file only** plus gitignored scratch `.scratch/r18d/`. No
  SKILL.md, SCORECARD.md or MINT.md byte is edited by this seat. No commit.

## 0. Verdict

**Capability drafts exist and are mostly admissible in substance; admission is
not earned yet, and the round-18 D4 leg is one piece short at this stamp.**
`reports/round-18/d4/scribe-3.md` (R18-D23) already drafts the SCORECARD
capability rows and their admission conditions, and `scribe-4.md` (R18-D24)
drafts the ASSEMBLY/README drift table. What no draft yet contains is the
**SKILL.md row set** (the lane's *craft* statements, distinct from the
capability table) and the reviewer's adjudication of which drafted rows may be
pasted and with what limits. Both are drafted below.

The one measured blocker at 10:31Z: the D4 gate run reaches the generalized
legs but stops at `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py`
(exit 2) — the family resolver (`tools/gates/typed-pipeline-gate.py:203-214`)
maps family `d4` to `tools/assemble-d4-typed.py`, which does not exist, and
`examples/culture-d4/packet.d4.typed.yml` does not exist either. Everything
downstream of that (D4 L2 channel leg, D4 L3 equality, the D4 frozen row) is
therefore still unmeasured.

## 1. Adjudication of the drafted capability rows (`scribe-3.md` §2)

| drafted row | reviewer reading |
|---|---|
| `typed-pipeline-gate-declared-assembler` | **admissible on the O axis once the parent admits O**, with one wording bound: the demonstrated fact measured here is "the declared/`family` identity leg resolves a non-D2 assembler (`L1-assembler` ok at gate `7fad95e0…`) and the default D2 path stayed byte-identical" (see §3 below). The row must not say "the D2-bound refusal is gone on the D4 path" without the caveat that the D4 path still exits 2 at L1-build for the missing adapter at this stamp. |
| `culture-d4-gate-verification` | **not admissible yet.** The row's first clause — "the generalized gate runs over `examples/culture-d4/packet.d4.yml` and its emitted finding set equals the D4 expected set exactly" — has no execution to cite at this stamp: the D4 run exits 2 before L2/L3. Admit only after the D4 run exits 0, prints the banner and the 15 holds + 1 note verbatim, and the D4 frozen row (if one is landed) replays green. |
| `d4-pinnable-check-gates` | **admissible in substance now, if the parent wants a small row**: both thin gates exist and forward `--check` verdicts (`tools/gates/d4-typed-labels-check-gate.py`, `tools/gates/d4-assembly-check-gate.py`; measured by the sibling seat 10:26Z exit 0). Bound the wording to "forwards the verdict; adds no semantics", and pin their digests (`05f99629…`, `df1a364b…` per scribe-3) at the moment of admission. |

## 2. Draft SKILL.md rows (craft statements, not capability claims)

These follow the existing SKILL.md idiom (`SKILL.md:20-28` decision table,
`:131-168` error patterns). Suggested placement: a round-18 subsection under
*Gates and probes* (`SKILL.md:238`).

**Error patterns (append to the table):**

| Observation | Reading |
|---|---|
| The "expected" finding set is written from the tool's own printed output, with no locus that predates the tool | transcription, not pre-registration: the equality leg then has drift teeth but no content teeth. Acceptable only when the set was decided elsewhere first (D2: `reports/round-11/depth/design.md` §4.2-§4.5; D3: `examples/culture-d3/expected.json` "fixed before tool implementation"), and the delta is dispositioned in a filed reconciliation. Command showing the shape: `python3 -c "…" ` set-compare of emitted vs committed rows — 0 only-expected / 0 only-emitted is the transcription signature (`reports/round-18/d4/review-2.md` §2) |
| A pre-registration rule that reads "the contract is the equality, not the spelling", applied to **set content** rather than to renames | blank cheque: the rule may license renames of records the design already named (`reports/round-17/d4/typed-support-2.md:80-88` did exactly that, pre-emptively), never the adoption of classes the design did not name. Bound it in the round's own wording |
| A shared engine emits a packet-independent block into a new family's expectation (D2's rank constants: `D2L-RANK` @ `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g`, `TR-04#a\|TR-06#a` + note `SR-01#a\|SR-01#b`) | passenger rows: the records occur **0** times in the new packet (`grep -c` sweep, 2026-10-18). They belong in the expectation only with an explicit per-packet attribution, and the gate's equality leg must not be described as verifying the new family's design debt while they are inside it |
| A `--check` invoked without naming the packet | measures the wrong pair: `tools/d2-typed-labels.py --check` defaults to `--packet examples/culture-d2/packet.d2.yml`, so a D4 file "differs" (exit 1) until the packet is named — after which it is byte-identical (exit 0). Multi-family reproducers must name every input |

**Decision-table row (append / extend "Check a world hangs together"):**

| Intent | Correct surface | Never | Expected output |
|---|---|---|---|
| Gate a second culture family through an existing typed pipeline | declare the family's pipeline (assembler / projection / adapter / expected-holds / packet — packet-declared block or CLI flags), keep the default family's path byte-identical, and add a frozen row for the new family | relaxing the assembler-identity leg to accept arbitrary packet bytes, or repointing the default family's pins to make the new family pass | `L1-assembler` + `L1-expected-holds` green on the declared family, `L3` equality over that family's committed expectation, the default path's stdout byte-identical to its recorded bytes |

## 3. Measured basis for the drafts (so the parent can paste with citations)

| command (cwd = lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18) | gate sha | observed |
|---|---|---|
| `python3 tools/gates/typed-pipeline-gate.py` | `b4232690…`, `bba60bc1…`, `edfec5f3…`, `7fad95e0…` | exit **0**, stdout sha `15cdfbda…` — **byte-identical to the pre-change run** at every sha measured; `16/16 legs passed` |
| `… tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` | as above | exit **0**, stdout sha `9a69985a…` — byte-identical to `tools/gates/frozen/round-11/typed-pipeline/run.log` |
| `… --selftest` | `b4232690…` | exit 0, 12/12 (the D4-addition checks were not in that revision) |
| `… examples/culture-d4/packet.d4.yml` | `7fad95e0…` | exit **2**: `ok L1-assembler`, `ok L1-expected-holds`, `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | — | exit 0, byte-identical |
| `python3 tools/assemble-culture-d4.py --check` | — | exit 0, byte-identical assembly |
| `python3 tools/assemble-d2.py --check`; `python3 tools/assemble-culture-d3.py --check` | — | exit 0 / exit 0 |

Note for the parent: `L1-expected-holds` is a *self-consistency* check over the
declared file (schema, counts vs list lengths — `typed-pipeline-gate.py:363-385`);
it does not and cannot check the set's provenance. The drafts above must not
describe it as validating the D4 debt.

## 4. Admission conditions this reviewer adds to `scribe-3.md` §3

1. **The missing D4 piece is named, not silently skipped.** Either
   `tools/assemble-d4-typed.py` + `examples/culture-d4/packet.d4.typed.yml`
   land (then the full L1→L4 chain is measurable and the D4 channel leg has a
   product), or the round declares in writing that the D4 L3 leg grades the
   projector's output without a typed packet, and records the **absence of the
   D4 channel leg (L2)** as a limit of the D4 verification. The second option
   is a smaller capability and must be described as such.
2. **The A-07 question is answered.** `01-brief.yml` A-07 ("six holds, zero
   notes, zero fails") and the landed expectation (15/1/0) cannot both stand as
   the D4 debt. The parent either lands the owner's re-declaration (a new
   component revision + reassembly) or records the supersession by pointer.
   Until then, no row may say "the D4 hold set is verified" — only "the D4
   emitted set equals the committed D4 expectation".
3. **The counting command is run by its owner and its receipt cited.**
   `python3 reports/round-18/run-validation.py` landed (20805 B at this stamp);
   this seat did not run it (round-14 lesson: a counting command can itself be
   a writer). Admission cites the runner's own receipt, not this review.
4. **The D4 frozen row exists before "replay-frozen green" is written.** No
   round-18 frozen manifest for the D4 row was present at my last check;
   "replay green" is a statement about a specific manifest + digests + date
   (R17 lesson D4).

## 5. Wording discipline (what must not be written)

- Not "the D4 gate passed": the gate's own banner says exit 0 is not a
  clearance; write "the emitted findings equal the committed expectation".
- Not "the D4 hold set was independently verified": the set's author is the
  tool (review-2); write "the set was pre-declared in part, reconciled in
  `reports/round-18/d4/holds.md`, and pinned as the equality target".
- Not "the default path is unchanged" without the three commands and their
  stdout digests (this review's §3 table is citable; a later tree re-measures).
- Not "94" or any coverage number here: the civ map is claim C's business.

## 6. Limits

- The gate file moved five times during this seat's window; §3 pins each
  reading by sha, and a later revision supersedes the readings (round-15
  lesson). If the parent lands after further edits, re-run §3's commands.
- I did not read `scribe-5..8.md` (not present at my last poll); if a later
  scribe drafts SKILL rows, the parent should merge rather than duplicate —
  this file's §2 is offered as the reviewer's version.
- NON-CANON throughout; no promotion, roster or canon claim.
