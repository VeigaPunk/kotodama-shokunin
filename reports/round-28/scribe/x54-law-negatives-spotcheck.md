# X54 — register-law negatives spot-check (round 28)

- **Seat:** SCRIBE X54, round 28 (operator: loop 3 of 3, build 4 of 4; 64 workers
  on `devin/deepseek-v4-1-flash-high`).
- **Assignment (verbatim):** "SCRIBE X54: spot-check (law negatives
  independently)."
- **Claim supported:** **D / depth** — `after_required` reads "The law gains a
  replay/checking leg: speaker classes resolve against delivered records, forces
  against a declared vocabulary, consequences against the roll/rank machinery —
  a tampered row is a named finding (**D4L-LAW-\*** class)" (`reports/round-28/
  claims.json:15`). Its `before` carries round 27's **RL-1**: "a tampered law row
  (`force: 'no-such-force'`) emits the same 12 findings as a clean one".
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (`reports/round-28/claims.json:5`); lane HEAD at every measurement
  `69cecbc7dcf575a29f29660ecac470e05260fd86` (the round-28 declare commit).
- **Command:** `python3 -B reports/round-28/scribe/x54-law-negatives-spotcheck.py`
  (instrument sha256 `4dbb4132abb4b2fd77eb86a08336c680ed5650552189a27881df9aa5b86b4522`;
  receipt `51cb471123fc5f799e81d385fa85a108f2fe2b6c1bdbd56a1f960abbd1bf6470`
  under gitignored `.scratch/x54/final.json`).
- **Write scope:** `reports/round-28/scribe/x54-law-negatives-spotcheck.py` and
  this file, plus gitignored scratch under `.scratch/x54/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write). **No tool, gate,
  component, packet, pin, fixture or shared bookkeeping was edited**; no commit,
  no push; no filed artifact of rounds 8–27 was modified. This seat authored
  none of the artifacts it measures.
- **Canon:** NON-CANON engineering evidence. A spot-check reports what the bytes
  do; it adjudicates no round and blesses no fix.

## 0. Headline

**The law's replay leg did not land, and the round's own acceptance machinery
agrees with this seat that it did not.** Round 28's claim D asks that a tampered
law row become a *named* `D4L-LAW-*` finding. Measured independently on **14
tamper routes** (round 27 measured one), a tampered law row is **still invisible
on the delivered surface**: no tool or gate under `tools/` emits the named class
at all, and every route leaves the projection byte-for-byte unmoved.

| # | finding | severity |
|---|---|---|
| **X54-F1** | **RL-1 reproduces on 14 of 14 routes.** No delivered instrument emits `D4L-LAW-*`; `grep -rln "D4L-LAW" tools/` → nothing. Every tamper route yields **0** law findings, and the non-law projection is **12 findings, unchanged** in all 16 legs. | **the claim's core is unmet** |
| **X54-F2** | **RL-4 is genuinely fixed — both halves that the components own.** `03-orthography.yml` now declares `packet_keys: [orthography, records, literacy_institutions]` and `09-costumes.yml` adds `enforcement`; OR-01..03, LI-01..03, EN-01/02 now appear in the packet and the three blocks left `assembly.skipped_keys`. | the claim's second half holds |
| **X54-F3** | **But RL-4's *third* half is not fixed: the assembler still cannot validate the block.** `register_law` is in neither `PACKET_KEYS` nor `RECORD_FIELDS` of `tools/assemble-culture-d4.py` (`grep -c register_law` → **0**). Measured with my own control on an isolated mirror: stripping an `id` from an `RGL-` row **assembles exit 0** and lands the row with no id, while the *same edit* to a `lexicon` row is refused `exit 2`. | **a real residual defect** |
| **X54-F4** | The law's `force` field has **no declared vocabulary** to check against — the packet supplies none, and the five delivered values are free prose mixing a class, a modifier and an explanation in one string. "forces against a declared vocabulary" therefore has no vocabulary. Independently confirmed by the sibling auditor (`x59` `L10-HOLD`). | the third clause is unmeasurable |
| **X54-F5** | The round-28 **evidence** instruments exist (≥3 discovered; the count drifts upward as sibling seats land — 3 at 17:16Z, 4 by 17:18Z) and two of them independently reach this seat's verdict. `reports/round-28/audit/x59-register-law-negatives.py` run by this seat reports `L6b-HOLD: RL-1 still open … named_law_findings=0`; `reports/round-28/gate-tests/run-gate-tests.py` reports its own D15 checks red with "RL-1 still open at this stamp". | the round knows, and says so |
| **X54-F6** | **Instrument hazard, found by this seat and fixed in-window.** `tools/d2-typed-labels.py` resolves the packet's family from the **parent directory name** (`:2477` `packet_family`), not from content. A tampered copy placed anywhere but a `culture-d4/` directory silently resolves as the **D2 default** and reports **16** findings instead of **12** — for an *unmodified* copy. This seat's first run hit exactly that and produced 16 spurious non-law findings on all 14 routes. The mirror now reproduces the `culture-d4/` shape, and a selftest control asserts both directions. | **a trap for every future sweep** |

## 1. Why the negative control is the measurement

The claim is a **negative** claim — it says tampering must be *caught*. A
negative claim is only as strong as the controls it fails closed on, so this
instrument measures four things no single positive run can:

1. **the clean packet is silent** — the law checker must emit **zero** law
   findings on the delivered bytes, or a checker that fired on everything would
   pass every tamper route.
2. **each tamper route is caught, by name** — at least one finding whose id
   matches the claim's own class token, whose subject names the tampered row.
3. **the tamper is isolated** — a law tamper must not perturb the rest of the
   projection; the non-law count must equal the clean packet's. This catches a
   checker that "catches" tampering by breaking the packet.
4. **prose is not structure** — the false-positive control. Rewording `act` and
   `consequence` must leave the structural verdict unchanged.

## 2. The tamper matrix, in full

All 14 routes were applied by **this seat's own** line-level text transform of
the delivered bytes (never the D seat's probe transform, never a
re-serialization). Every tampered packet still parsed under the projector's own
strict loader, and **every one left the projection's non-law findings at 12** —
the clean value.

| route | row | field | why | parses | law findings | caught | non-law |
|---|---|---|---|---|---|---|---|
| T-01 | RGL-01 | `force` | round 27's RL-1 route, re-run: an undeclared illocutionary force | yes | 0 | **no** | 12 |
| T-02 | RGL-01 | `speaker` | a speaker class that no delivered record carries | yes | 0 | **no** | 12 |
| T-03 | RGL-01 | `speaker` | RL-4's own casualty: legal in `03-orthography.yml`, absent from the packet | yes | 0 | **no** | 12 |
| T-04 | RGL-01 | `consequence` | a record consequence naming a roll no delivered record carries | yes | 0 | **no** | 12 |
| T-05 | RGL-01 | `axis` | an axis outside the packet's declared axis vocabulary | yes | 0 | **no** | 12 |
| T-06 | RGL-02 | `kind` | a law kind outside the delivered kind set | yes | 0 | **no** | 12 |
| T-07 | RGL-03 | `register` | a register name the `registers` block does not declare | yes | 0 | **no** | 12 |
| T-08 | RGL-03 | `force` | RGL-03 declares a not-rollable guest charge; a binding force contradicts it | yes | 0 | **no** | 12 |
| T-09 | RGL-04 | `consequence` | RGL-04's own clause (no segment) reversed in its consequence text | yes | 0 | **no** | 12 |
| T-10 | RGL-05 | `consequence` | RGL-05's own era clause reversed (E0 stamp claims are the named defect) | yes | 0 | **no** | 12 |
| T-11 | RGL-03 | — (row op) | a whole law row removed from the block | yes | 0 | **no** | 12 |
| T-12 | RGL-01 | — (row op) | a duplicated row id | yes | 0 | **no** | 12 |
| T-13 | RGL-01 | `design_row` | a `design_row` naming a QREG id no record carries | yes | 0 | **no** | 12 |
| T-14 | RGL-02 | `cite` | a row whose citation is emptied | yes | 0 | **no** | 12 |
| P-01 | RGL-01 | `act` | prose reword: the structural verdict must not move | yes | 0 | **no** | 12 |
| P-02 | RGL-04 | `consequence` | prose reword of a negative clause | yes | 0 | **no** | 12 |

**0 of 14 caught, by name.** The prose controls (P-01, P-02) also produce
nothing — which is the *correct* answer for them, and is the reason the verdict
below does not read them as a failure. A law checker that has no teeth cannot
distinguish structure from prose; it is silent on both.

## 3. The delivered surface, stated exactly

The claim names a class, not a file. Two kinds of instrument can emit it, and
the difference is the whole point of the spot-check:

| class | where | found | graded |
|---|---|---|---|
| **DELIVERED** — the tree's checking leg, on the surface a downstream consumer would run | `tools/` | **0** | **yes** |
| **EVIDENCE** — the round's own probe / acceptance runner | `reports/round-28/` | ≥3 (drifts as siblings land) | no |

The graded cell is the load-bearing one and it is **0** at every measurement this
seat took, at lane HEAD `69cecbc`. The evidence count is not a verdict and moves
while the wave is still running — at 17:16Z it was 3
(`audit/x59-register-law-negatives.py`, `gate-tests/run-gate-tests.py`,
`run-validation.py`); by 17:18Z a fourth (`sweep/poll-d-landing.py`) had landed.
A spot-check reports what it measured and when.

```
$ grep -rln "D4L-LAW" tools/
(nothing)
$ python3 -B reports/round-28/scribe/x54-law-negatives-spotcheck.py --packet examples/culture-d4/packet.d4.yml
x54-spotcheck: packet=examples/culture-d4/packet.d4.yml delivered_instruments=0 law_findings=0
x54-spotcheck: no delivered instrument names the law's finding class on this packet —
               the law has no replay leg on the delivered surface
```

**This instrument deliberately does not emit the named class itself.** A
spot-check that manufactured the token it is measuring would make its own
negative unmeasurable: the round's discovery harness counts instruments that
*can* emit `D4L-LAW-*`, so a spot-check emitting one on every packet would be
counted as a replay leg and would hide the very absence the claim is about. The
`--packet` mode answers in this seat's own vocabulary and states the absence as
absence.

## 4. The independent corroboration

This seat ran the round's own evidence instruments against the same bytes.

| instrument | run by this seat | result |
|---|---|---|
| `reports/round-28/audit/x59-register-law-negatives.py` | `--packet examples/culture-d4/packet.d4.yml` | `L6b-HOLD: RL-1 still open at this tree … named_law_findings=0`; `L9-HOLD: RL-4 still open`; `L10-HOLD: … no force vocabulary`; `failures: 3` |
| `reports/round-28/gate-tests/run-gate-tests.py` | default | `D15 the tampered force is caught by a named D4L-LAW finding: no new named D4L-LAW token`; `summary: 46/57`; `gap: RL-1 still open at this stamp` |

Three instruments, built on different machinery (this seat's line transform; the
auditor's `ruby -ryaml` loader; the gate-test runner's planted-fixture clone),
reach the same verdict. That is a cross-check, not an inheritance: none imports
another.

### 4.1 The round's own adversarial reviewers reached the same conclusions

Four sibling D seats landed while this seat was measuring, and each independently
found the same things this instrument measured. Recorded here because agreement
across seats built on different machinery is the strongest evidence available,
and because it means the round's own reviewers are not being contradicted by this
spot-check:

| sibling finding | this seat's counterpart |
|---|---|
| `reports/round-28/argot/D17-law-bypass.md`: "the delivered tree still names **no** `D4L-LAW-*` id under `tools/` … the claim's own named artifact does not exist"; "seven law violations pass it silently — including inverting a row's force to its opposite, deleting a row outright, and blanking its consequence" | **X54-F1**, reached independently and with a wider route set (14 routes vs 7) |
| `reports/round-28/argot/D18-force-overmatch.md`: the force predicate is "two independent substring tests composed with `AND`, so membership of the *value* in the vocabulary is never tested" | **X54-F4** — the vocabulary the claim names has nothing to test against |
| `reports/round-28/argot/D19-ab-crosscheck.md` §4 / `D19-F3`: "`packet_family()` reads the family from the packet path's **parent directory name**; the same unmodified packet reads 12 or 16 findings depending only on its parent directory, manufacturing a four-finding phantom delta" | **X54-F6** — found here on first run, in the same way, and fixed in this instrument's mirror |

D17's reading of the round-28 runner is sharper than this seat's and should be
preferred on that point: the runner's `law_check` is the *runner's own* reader,
so the runner catching its own planted tampers is not a delivered replay leg.
This seat's instrument measures the delivered surface only, and reaches the same
0-of-14.

## 5. X54-F3, the residual RL-4 defect, measured with its own control

The claim's RL-4 half says "the components declare `packet_keys`". That half is
**fixed** (X54-F2). But the round-27 RL-4 finding had a second, load-bearing
part — the assembler's *validator* — and it is not fixed.

`tools/assemble-culture-d4.py` validates a block's records only if the block
appears in `RECORD_FIELDS` (`:315`, "missing field(s) … needed by the
gate-facing packet"). `register_law` is absent from both `RECORD_FIELDS` and
`PACKET_KEYS` (`grep -c register_law` → 0). The packet's own
`contract.record_fields.register_law` (declared in `01-brief.yml:179`) is
descriptive prose; nothing enforces it.

Measured on an **isolated full mirror** (`.scratch/x54/iso/`, whose unmodified
baseline reproduces `packet.d4.yml` byte-for-byte at
`543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`):

| control | edit | result |
|---|---|---|
| C1 | strip `id:` from an `register_law` row (`RGL-03`) | **`exit 0`**, packet written (98824 bytes), the row lands with **no `id`** |
| C2 (contrast) | the *same* edit to a `lexicon` row (`L-01`) | **`exit 2`** — `lexicon[0]: missing field(s) ['id'] needed by the gate-facing packet` |

Same edit, same validator, opposite outcome. The law block is the one
record-shaped block the assembler cannot refuse a malformed row in.

**A note on method, recorded because it cost a wasted measurement.** This
control was first attempted by running the live assembler from inside a
`culture-d4`-only scratch copy. That was invalid and reported nothing: the
assembler resolves `ROOT` from its own file location, so it read the **real**
components and ignored the copy entirely. The control above was re-run against a
full mirror of `tools/` and `examples/`, whose baseline is verified
byte-identical first. The live tree was confirmed undamaged afterwards — all
five artifact digests in the receipt match their pre-control values exactly, and
`python3 tools/assemble-culture-d4.py --check` reports `byte-identical
deterministic assembly`.

## 6. X54-F6, the path trap, and why it matters to every future sweep

`tools/d2-typed-labels.py:2477`:

```python
def packet_family(packet_path):
    match = re.fullmatch(r"culture-([a-z0-9]+)", pathlib.Path(packet_path).parent.name)
    return match.group(1) if match else DEFAULT_FAMILY
```

The family is read from the packet's **parent directory name**. A tampered copy
written anywhere else resolves as the D2 default, and the projection is then
computed against D2's machinery:

```
$ python3 tools/d2-typed-labels.py --packet .scratch/x54/ctl/b/packet.d4.yml   # flat copy
coverage: conflicts=4, findings_total=16, rank_rules_component=21, rank_rules_unresolved_items=13
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml # in place
coverage: conflicts=0, findings_total=12, rank_rules_component=4,  rank_rules_unresolved_items=0
```

Both files were byte-identical (`sha256 543d68a8…`). **This seat's first census
run reported 16 non-law findings on all 14 routes because of exactly this** —
not because any tamper moved the projection. The fix is in the instrument: the
mirror reproduces the `culture-d4/` shape, and the selftest now carries controls
in **both** directions — an unmodified mirror copy must project *identically*
(`12 == 12`), and a flat copy must *not* (`16 != 12`), so the trap is asserted
rather than assumed.

This is reported as a hazard for the lane, not just for this seat: any future
sweep that copies the packet to scratch to tamper it will silently measure D2
unless it preserves the directory name. The sibling reviewer reached the same
conclusion independently in `reports/round-28/argot/D19-ab-crosscheck.md` §4
(`D19-F3`), which traces the same mechanism to a *filed round-27 table* — round
27's Route B probe reported `findings_total=16` and the phantom delta looks
exactly like Route B's cost. Two seats hit the same trap on the same day from
different directions; it is a real property of the instrument, not a slip.

## 7. What this seat did not do, and what it cannot say

- **It did not adjudicate the round.** The verdict is `reports/round-28/
  run-validation.py`. This file is evidence for it.
- **It did not measure the `speaker`/`consequence` legs against delivered
  records in the claim's own terms.** The claim's `after_required` names three
  resolutions (speakers against records, forces against a vocabulary,
  consequences against the roll/rank machinery). This seat measured whether a
  tampered row is *caught*, which is the claim's named acceptance test. Whether
  the vocabularies those resolutions need *exist* is the sibling auditor's
  measurement (`x59` `L10`), cited here rather than re-derived.
- **It did not verify the `force` vocabulary's absence beyond the packet.** The
  packet supplies none and the components declare none (`grep` for
  `directive-binding`/`commissive-binding`/`declarative-naming` finds only the
  five law rows' own prose). A vocabulary could exist in a round artifact rather
  than in the delivered tree; the claim's wording points at the delivered tree,
  and that is what was measured.
- **It did not edit anything but its own two files.** No fix is proposed here;
  the repairs are the D seat's and the O sweep's.

## 8. Verdict

| question | answer |
|---|---|
| does the clean packet produce zero law findings? | **yes** — the negative control passes |
| delivered instruments emitting `D4L-LAW-*` | **0** |
| tamper routes caught by name | **0 of 14** |
| every tampered packet still parses? | **yes** (14/14) |
| the rest of the projection unmoved? | **yes** (12 == 12 on all 16 legs) |
| prose routes read as structural findings? | 0 of 2 (correct for a toothless checker) |
| **RL-1 reproduces?** | **yes — the claim's core `after_required` is not met at this HEAD** |

**The law is still a declaration with no teeth on the delivered surface.** Round
28's RL-4 half is genuinely and verifiably improved (X54-F2), but its RL-1 half
— the replay leg the claim's own acceptance test names — is not landed at lane
HEAD `69cecbc`, and the round's own two independent instruments say the same
thing.
