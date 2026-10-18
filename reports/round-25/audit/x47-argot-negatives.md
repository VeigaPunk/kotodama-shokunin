# R25-X47 — shard audit: the argot-derivation negative controls

- Seat **R25-X47** (SCRIBE X47: shard auditor — argot negatives). Round 25
  (operator: loop 3 of 3, build 1 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` — `reports/round-25/targets.json`).
- Date: **2026-10-18**. All counts carry their command and date; raw receipts
  live in this seat's scratch (`.scratch/r25-x47/`, gitignored) and only this
  fragment is filed.
- Declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`
  (`reports/round-25/claims.json`); lane HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope: this fragment and `reports/round-25/audit/x47-argot-negatives-audit.py`
  only.** No filed round-8–24 byte is edited; no source or gate is changed; no
  round validator is run; no Git mutation. NON-CANON engineering evidence; canon
  standing is lore-shokunin's.

## What this shard audits

The **negative** side of the argot-derivation checking leg: does the pipeline
actually fail a form whose stated inputs and rules do not yield it, and are the
failures it reports real rather than manufactured by the harness? The seat's
tool is `reports/round-25/audit/x47-argot-negatives-audit.py` (stdlib only;
`--selftest` **9/9** controls, exit 0).

## R25-X47-1 — the declared algorithm is stated and deterministic

`reports/round-17/d4/design-language.md` §5 (`:186-217`) fixes two operations:
`head2` (first two syllables, **maximal-onset** syllabification) and `reverse`
(character-level string reversal). This seat re-implemented both from the stated
algorithms and re-derived the design's own eleven worked rows:

```
python3 -B reports/round-25/audit/x47-argot-negatives-audit.py --json
```

**11/11 agree, 0 mismatches** (2026-10-18). The onset/coda disagreement the
design names is reproduced: `saalumi` → `saa.lu.mi` → **`saalu`**, explicitly
**not** `saalum`. The derivation is therefore deterministic and checkable, as
the design claims. **Measured, and the algorithm claim holds.**

## R25-X47-2 — the delivered-state delta (forecast vs delivered)

Measured on the committed bytes (2026-10-18):

| token | `examples/culture-d4/packet.d4.yml` |
|---|---|
| `derived_from` | **0** |
| `derivation:` (record field) | **0** |
| `derived_from`+`derivation` pairs | **0** |
| `D4L-ARGOT-DERIV` rows | **0** |
| distinct `D4L-*` codes present | `D4L-FORM-UNRESOLVED` only |

This seat's independent count agrees with the D seats'
`reports/round-25/argot/current-state.md` §4 and with round 19's read
(`reports/round-19/knowledge/analyst-3.md:87-91`): the argot-derivation leg is
**not delivered** — the forecast element F-3 (`derived_from` + `derivation`
fields) has no delivered instance to check. Any round-25 claim that the leg was
"implemented and executed on D4" must name this delta rather than assert it
away.

## R25-X47-3 — the false red is manufactured by the rebuild (root-caused)

Feeding the derived packet back
(`python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml`)
yields **exit 1, 14/16**, with eight `DERIV-REPLAY` FAIL lines. This seat's
question is whether those eight are findings about the packet or artifacts of
the comparison machinery. They are the latter:

| control (2026-10-18) | `DERIV-REPLAY` lines |
|---|---|
| `naming-collision-gate.py examples/culture-d4/packet.d4.yml` (source) | **0** |
| `naming-collision-gate.py examples/culture-d4/packet.d4.typed.yml` (typed) | **0** |
| `naming-collision-gate.py <gate's own rebuilt legacy packet>` | **8** |

The single root line: the gate's L2 arm rebuilds the legacy packet from the
*parsed typed document* and re-serializes it with the `assemble-d2.py`
`yaml_lines` serializer (`tools/gates/typed-pipeline-gate.py:588-608`), which
**doubles the backslash** in CX-01's pattern. Read through the gate's own loader
(`naming-collision-gate.py:488 load_yaml`):

| surface | `morphology.derivation_rules[CX-01].pattern` | replays `tum+hai` → `tumhai`? |
|---|---|---|
| source packet | `^(?P<a>.+)\+(?P<b>.+)$` | **true** |
| gate's rebuilt legacy packet | `^(?P<a>.+)\\+…` (one escape too many) | **no-match** |

So neither committed packet emits `DERIV-REPLAY`; only the gate's internal
rebuild does. The eight lines are an artifact of the machinery being graded as
if it were evidence about the packet. This seat reached this independently from
the gate output and the byte diff; the O seats' `reports/round-25/gate-input/diagnosis.md`
§3.2 records the same root line from the fix-design side — **two independent
seats, same root**.

**This is the O hazard's negative-control face.** A fix that merely suppresses
the eight lines without restoring the faithful source read would leave the
manufacturing machinery in place; the honest control is that the source packet
already replays clean (0) and must keep doing so.

### Post-patch re-measurement (the fix landed while this audit ran)

The O seats' repair landed in the live tool during this audit. The gate's sha
moved `04ad4bb4…` → `a6e8d9c8…` → `879d40bf977eef65…` (final, stable across
three 25-second samples, 17:33:48–17:34:19Z). This seat re-ran the whole control
set on the final bytes:

| control (patched gate, 2026-10-18) | result |
|---|---|
| `… packet.d4.yml` (documented source entry) | **19/19**, exit 0 — unchanged |
| `… packet.d4.typed.yml` (the false-red input) | **16/16, exit 0, 0 `DERIV-REPLAY`** — the manufactured class is gone |
| `…` (flagless D2 default) | **16/16**, exit 0 — unchanged |
| `… --selftest` | **19/19 checks passed** (was 12/12 pre-patch) |
| N1 dropped routing row | exit 1, `FAIL L2-channel` **and** `FAIL L3-routing-consistency` — still fails closed |
| N2 smuggled `owed_slot: LEX-GAR-99` | exit 1, `FAIL L3-routing-consistency` (`LEX-GAR-99` in routing) — the null-ish filter is not a blanket amnesty |
| N4 self-referential `--legacy-packet` | exit 2, `FAIL L1-assembler` — a wrong declared source is refused |

The patch reads the declared, digest-verified source instead of rebuilding, and
names the input class; the null-ish guard closes the routing leg. **The
manufacturing machinery this shard measured is gone, and every negative control
still fails closed.** Two dated in-flight observations are recorded rather than
hidden: between roughly 17:32:23Z and 17:33:08Z the patched gate's `--selftest`
raised `KeyError: 'owed_slot_of'` (a missing helper while the patch was being
written), and one interim revision printed `FAIL typed input: --json reports the
input class — None`; both cleared by the final `879d40bf…` revision. This
receipt binds the final bytes; an earlier X47 receipt bound `04ad4bb4…`.

## R25-X47-4 — the live replay engine cannot represent the operation

This seat reproduced the D analysis' load-bearing negative independently. The
live lexicon audit (`tools/gates/lexicon-coverage-audit.py`) replays a
construction by substituting `B1`… with the base terms and then
`expected.replace("+", "").replace("-", "")` — a **concatenation-only** model
with no operation field. Fixtures built by this seat from the delivered packet
(scratch only; the delivered tree is untouched):

| # | fixture | result |
|---|---|---|
| N-1 | delivered packet with `L-46 mesar` → `mesor` | `FINDING D-form-mismatch: 'mesor' does not reproduce from bases mes under construction 'CRAFT-AGENT' (expected 'mesar')`, exit **1** — a real defect is caught |
| N-2 | `ARGOT-REVERSE` declared (`pattern: B1`) + base `L-55 min` + derived `L-56 nim` (**correct** reversal) | `FINDING D-form-mismatch: 'nim' does not reproduce … (expected 'min')`, exit **1** — a **false FAIL on a correct derivation** |
| N-3 | same, with the record's form set to `min2` (**wrong** reversal) | byte-identical finding text, exit **1** |

N-2 and N-3 producing the *same* finding is the measurement that matters: under
the **old** model a correct `reverse` derivation and a wrong one are
indistinguishable, and the correct one is a false FAIL. The argot operation
class was **not representable** in the pre-round-25 replay engine — so the
round-25 D claim could not have been satisfied by declaring `ARGOT-REVERSE` in
`constructions`; the engine had to gain the operation, and a control had to pair
the correct form (must pass) with the wrong form (must fail
`D4L-ARGOT-DERIV`).

### R25-X47-4b — the delivered leg closes exactly this gap (verified)

The D seats landed a dedicated gate during this audit,
`tools/gates/argot-derivation-gate.py` (sha `07db6e9b4e01539e…`), with its
committed fixture pair. This seat re-ran its negatives independently and the
discrimination is now correct:

| # | control (this seat, 2026-10-18) | result |
|---|---|---|
| — | `argot-derivation-gate.py --selftest` | **18/18 checks passed**, exit 0 |
| — | fixture run, ids vs `.expected` | **exact match** (4 × `D4L-ARGOT-DERIV`, 1 × `D4L-ARGOT-RULE`), exit 1 |
| — | `examples/culture-d4/packet.d4.yml` | exit 0; `records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0` |
| T-1 | correct pair `makun` → `nukam` (`reverse`) | **exit 0**, `violations=0` — the correct form passes |
| T-2 | wrong operation: `head2` on `makun` → expected `maku`, delivered `nukam` | **exit 1**, `FINDING D4L-ARGOT-DERIV: … declared chain 'head2' applied to 'makun' yields 'maku'; the stated inputs and rules do not yield the candidate` |
| T-3 | tampered correct pair (`min` → `nims`) | exit 1, `D4L-ARGOT-DERIV` naming the true replay (`yields 'nim'`) |

T-1 vs T-2 is precisely the pair the old engine could not distinguish. The
`head2` maximal-onset reading is the fixture's own planted trap (`Q-11
saalum`, the design's named disagreement row), and the gate catches it. The
fixture's scope control — a `symbols` record carrying a `register` and prose
`form:` — is skipped rather than graded, so the gate does not manufacture
findings out of a medium description.

**Reading: the D capability's engine gap is closed and its negatives are real.**
What remains undelivered is the *domain*: `derived_pairs=0` on the D4 packet, so
the leg executes over an empty relation set (see R25-X47-2 and the D seats'
`delta.md`, which names the weigh-court/furnace-league spine divergence as the
cause). Exit 0 on the D4 packet therefore means "nothing to violate", not
"the argot is checked" — and the gate's own `coverage:` line says so.

## Cross-check against the D seats' execution fragments

The D seats' analysis and execution fragments landed while this audit ran
(`reports/round-25/argot/{forecast,current-state,delta,execution-1..4}.md`). This
seat's measurements were taken independently and agree on every point it
measured:

| this seat's measurement | D seats' corresponding reading | agreement |
|---|---|---|
| design table 11/11 re-derived | `forecast.md` §3.1 (verbatim table) | same table, same algorithms |
| 0 `derived_from`/`derivation` pairs; 0 `D4L-ARGOT-DERIV` | `delta.md` §1 F-1/F-3/F-7 **NOT DELIVERED** | agrees |
| 0 `head2`; the 6 `reverse` hits in `tools/` are `sorted(..., reverse=True)` | `delta.md` §1 F-2/F-2b | agrees |
| source packet 0 `DERIV-REPLAY`, rebuilt legacy 8 | `gate-input/diagnosis.md` §3.2(a) (one over-escaped regex) | agrees, independently reproduced |
| N-2 = N-3: correct and wrong reversal both false-FAIL | `delta.md` §"Bottom line" (concatenation replayer) | agrees |

The D seats carry one reading this seat did **not** measure and records as
attribution, not verification: the forecast was written against a **weigh-court
brokerage** culture (spine COUNT × QUOTE) while the landed tree is the
**furnace-league** (FIRE × MARK), so Δ3 "has no domain to grade"
(`delta.md` §"Root cause", path A). If that reading holds, the delta is a
**schema + engine + gate** delta, not a gate delta alone — which strengthens,
not weakens, this seat's conclusion that a declaration-only addition cannot
satisfy the claim.

## Verdict of this seat (scoped)

**Three findings, in the order they were measured.**

1. **The O hazard's negative-control face is real and was manufactured.** The
   eight `DERIV-REPLAY` failures the typed-packet run reported appeared on
   neither committed packet; the gate's own lossy `yaml_lines` rebuild
   double-escaped CX-01's pattern. The O seats' repair, which landed during this
   audit, eliminates them (typed run 14/16 → **16/16**, 0 `DERIV-REPLAY`) while
   every negative control still fails closed (source 19/19, D2 default 16/16,
   `--selftest` 19/19, dropped row exit 1, smuggled slot exit 1, wrong declared
   source exit 2).

2. **The pre-round-25 replay engine could not represent the argot operation.**
   Under `lexicon-coverage-audit.py`'s concatenation-only model a **correct**
   `reverse` derivation was a false FAIL, byte-identically to a wrong one
   (N-2 = N-3). A declaration-only addition could not have satisfied the claim.

3. **The delivered leg closes that gap, and its negatives are real.** The new
   `tools/gates/argot-derivation-gate.py` (sha `07db6e9b…`, `--selftest`
   18/18) discriminates correctly on this seat's own re-run: correct pair
   `makun`→`nukam` **exit 0**; wrong operation **exit 1** with
   `D4L-ARGOT-DERIV`; tampered pair **exit 1**. Its fixture ids match
   `.expected` exactly and its `symbols` scope control is skipped, not graded.

**What remains undelivered is the domain, not the engine.** On the D4 packet the
gate reports `derived_pairs=0` — it executes over an empty relation set — so
exit 0 there means "nothing to violate", not "the argot is checked". The D
seats' `delta.md` names the cause (the round-17 forecast was written against a
weigh-court brokerage; the landed tree is the furnace-league), which this seat
records as attribution rather than its own measurement. The D claim's
`after_required` is therefore **met on the engine leg and short on the domain
leg**: the delta must be named, not absorbed.

This is scribe evidence, not round admission; the parent owns integration and
the verdict.

## Limits and handoff

- The `--selftest` (9/9) is this seat's own in-memory control; the `--json`
  measurement is the filed receipt. Scratch receipts:
  `.scratch/r25-x47/{audit.json,audit-postpatch.json,src-gate.out,typed-gate.out,rebuilt-gate.out,fixture-run.out,d4-argot-gate.out,neg/,indep/}`.
- **Byte binding, two surfaces.** The pipeline receipt was re-measured against
  the patched `typed-pipeline-gate.py` (`879d40bf977eef65…`); the pre-patch
  measurement (gate `04ad4bb4…`, typed run 14/16) is preserved as
  `.scratch/r25-x47/audit.json` and is superseded. The argot-gate readings bind
  `tools/gates/argot-derivation-gate.py` sha `07db6e9b4e01539e…`. A later
  revision of either supersedes this receipt and must be re-run.
- `head2` is implemented here for the design's D4-shaped inputs (vowels
  `aeiou`, doubled vowels as length marks). It is not a general syllabifier and
  is not offered as one.
- The N-1/N-2/N-3 fixtures are this seat's own scratch constructions from the
  delivered packet; they are not proposed additions to any component and were
  never written into `examples/`.
- This seat did not edit the gate, the projector, the packet, or any filed
  round; the two hazards it names are routed to their owners, not fixed here.
