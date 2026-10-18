# R28-X59 — shard audit: the register law's negatives, and its replay leg

- **Seat:** SCRIBE **X59** (shard auditor — law negatives), round 28 (operator:
  loop 3 of 3, build round 4 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high`).
- **Claim audited:** **D / depth** `register-law-replay`
  (`reports/round-28/claims.json`). Its `after_required` reads: "The law gains a
  replay/checking leg: speaker classes resolve against delivered records, forces
  against a declared vocabulary, consequences against the roll/rank machinery —
  a tampered row is a named finding (D4L-LAW-* class); RL-4 fixed (the
  components declare packet_keys; the records reach the packet; the named-holds
  set updated honestly); the D4 typed gate + argot gate + assemblers green; the
  RL-3 ceiling recorded as a design constraint in the knowledge entry."
- **Date:** 2026-10-18. Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (`claims.json:5`); lane HEAD at this
  audit `69cecbc`.
- **Write scope:** `reports/round-28/audit/x59-register-law-negatives.py` and this
  file, plus gitignored scratch under `.scratch/x59/`. **No component, packet,
  tool, gate, fixture, pin, corpus entry or filed round-8–27 byte was written**;
  no commit, no push. `export TMPDIR=$PWD/.scratch` preceded every scratch write.
- **Canon:** NON-CANON engineering evidence. This audit adjudicates no round; it
  reports what the delivered bytes do against the law the claim names.

## 0. Headline

**Round 27 left two standing HOLDs on the register law (RL-1 and RL-4). This
audit re-tests both against the round-28 tree, with a planted control for each.
Both have now landed — and both landed *while this audit ran*.**

| # | finding | level |
|---|---|---|
| **X59-F1** | **RL-4 has landed.** Both components the gap names now declare `packet_keys` covering the blocks their records live in, and all eight record ids `OR-01..03`, `LI-01..03`, `EN-01..02` now reach `examples/culture-d4/packet.d4.yml`. Measured: `rl4_components_checked=2 rl4_keys_ok=2 rl4_ids_missing=0`. | the claim's RL-4 clause **landed** |
| **X59-F2** | **RL-1 has landed — late in this seat's window.** At 20:15Z the class `D4L-LAW-*` appeared in **no** delivered tool (this seat's `named_law_findings=0`), and a textually tampered packet produced no new named finding. At 20:20Z a new gate `tools/gates/register-law-gate.py` (sha256 `cfbff16b…`) landed, and the tamper now yields a **new named** `D4L-LAW-FORCE: FAIL` finding. `named_law_findings=1`. | the claim's RL-1 clause **landed** (see §5) |
| **X59-F3** | The `register_law` block is **still declared in neither `PACKET_KEYS` nor `RECORD_FIELDS`** in `tools/assemble-culture-d4.py` (`grep -c register_law` → **0**), so the assembler's record validator has no field list for the block. This is a *distinct* gap from RL-4 as round 28 defines it (RL-4 = the component `packet_keys` gap, now closed); it is the round-27 X59 `L9` HOLD, unchanged. | standing HOLD (`L9`) |
| **X59-F4** | The landed half is sound and unchanged: 62 records, 8 stamp records, 4 register rows, 5 law rows; axis→op 8/8, era 8/8, admissibility 8/8, oath-void 8/8, reference resolution 8/8. The typed gate is now **green** (`20/20 legs passed`). | pass |
| **X59-F5** | The law's own replay arithmetic still has no **declared vocabulary** to check against: the packet states 5 distinct `force` values but declares no `force` vocabulary (`force_vocabulary=0`). The new gate enforces a vocabulary in its own source (the design's Searle classes), so the leg works; but the *packet* still carries no such declaration. Reported as a HOLD, not invented as a FAIL. | HOLD (`L10b`) |

## 1. What was measured, at what revision

Digests read by this seat at the close of this audit, 2026-10-18 (`sha256sum`):

| surface | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `tools/gates/register-law-gate.py` | `cfbff16bbb67d94d39b8d19f7f3fa14d985d18d1f306c8b8e39f79d20ad00e5e` |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `reports/round-28/run-validation.py` | `b8f08546f87419464400c1238c8ce05dab0e10d88cae1c647f887f72ae66fb63` |

**The tree moved under this audit, twice, and both moves are material.** The
packet digest went `86079a67…` (round 27) → `543d68a8…` as the RL-4 fix landed,
and the round-28 runner was rewritten three more times
(`53e9b4d1…` → `a130f368…` → `b8f08546…`). The replay gate `register-law-gate.py`
did not exist at the start of this window. **Every reading below is dated**: §5
records the before/after of the RL-1 landing explicitly, because a reader who
takes only the headline would miss that the first half of this audit measured the
opposite. A reader re-running this fragment on a later tree must re-take the
digests.

## 2. The independent instrument

**Instrument:** `reports/round-28/audit/x59-register-law-negatives.py` (new, this
seat's; NON-CANON audit evidence, not a lane gate). It is deliberately built on
different machinery from the lane's gates:

| dimension | the lane gates | this instrument |
|---|---|---|
| YAML parsing | a hand-checked subset loader (`runpy` by path) | `ruby -ryaml -rjson` (a full YAML 1.1 loader) |
| `reverse` / `lengthen` | the gate's `OP_FUNCTIONS` + the packet's `pattern`/`output` pair | re-implemented here from the design prose |
| kernel dependency | loads a peer gate by path | none — no lane code imported |

**Controls (a checker that cannot say no is not a checker).** Nine planted
controls, all caught:

```
$ python3 -B reports/round-28/audit/x59-register-law-negatives.py --controls
control-1-op-contradicts-axis      ok  law=L3  findings=4
control-2-early-era                ok  law=L4  findings=4
control-3-form-mismatch            ok  law=L3  findings=4
control-4-stray-construction       ok  law=L5  findings=4
control-5-oath-in-register         ok  law=L7  findings=4
control-6-dangling-doublet         ok  law=L8  findings=4
control-6b-law-row-without-id      ok  law=L9  findings=4
control-8-rl4-gap-detected         ok  law=L11 findings=1
control-7-clean-stays-clean        ok  law=no-FAIL  findings=2
controls: 9/9 caught
```

`control-7` asserts **no FAIL** rather than zero findings, and says why: the
HOLDs below are standing properties of the tree that no packet bytes can remove,
so a control requiring an empty finding list could never pass. `control-8` plants
a synthetic component with no `packet_keys` entry for the block its records live
in and requires L11 to see it — the detector must be able to say no.

## 3. The eleven laws, and the verdict on the delivered packet

```
$ python3 -B reports/round-28/audit/x59-register-law-negatives.py
FINDING L9-HOLD: RL-4 still open at this tree … the assembler … declares it in
  neither `PACKET_KEYS` nor `RECORD_FIELDS` …
FINDING L10-HOLD: the law states 5 distinct `force` value(s) but the packet
  declares no `force` vocabulary for them to draw on …
counters: … law_replay_candidates=3 law_replay_runs=6 named_law_findings=1
  register_rows=4 replay_rows=5 rl4_components_checked=2 rl4_ids_missing=0
  rl4_keys_ok=2 speaker_component_only=1 stamp_records=8 …
failures: 2
```

| law | what it tests | verdict |
|---|---|---|
| **L1** | `registers:` declares the identity rows `QREG-01..04` | **pass** — 4 rows |
| **L2** | `plain` is declared `unmarked`; no plain record graded register-scoped | **pass** — 0 scoped |
| **L3** | every `stamp` record's op equals its axis's selection and replays under this instrument's own operations | **pass 8/8** |
| **L4** | every `stamp` record is staged E1 or later | **pass 8/8** |
| **L5** | every `stamp` record rides a `STAMP-*` construction | **pass 8/8** |
| **L6** | a speech-act law surface exists with speech-act fields | **pass** — 5 rows |
| **L6b** | a tampered law value is a NAMED finding in a delivered instrument (**RL-1**) | **pass** — `named_law_findings=1` (see §5) |
| **L7** | no `stamp` record sits in the religion field | **pass 8/8** |
| **L8** | `doublet_of` and `derivation.base` resolve to delivered records | **pass 8/8** |
| **L9** | the assembler declares and validates the `register_law` block | **HOLD** — undeclared (X59-F3) |
| **L10** | the replay arithmetic: speaker classes resolve, forces against a vocabulary, consequences against roll/rank | **pass 0 / HOLD 1** — all speaker tokens resolve; no force vocabulary declared (X59-F5) |
| **L11** | the components declare `packet_keys` and their record ids reach the packet (**RL-4**) | **pass** — 2/2 components, 0 ids missing (X59-F1) |

## 4. X59-F1 — RL-4 landed, measured on the components and the packet

Round 27's RL-4 measured that `03-orthography.yml` and `09-costumes.yml` declared
no `packet_keys`, so `OR-01..03`, `LI-01..03` and `EN-01..02` never reached the
packet. At the `543d68a8…` packet the gap is closed:

```
$ python3 -B reports/round-28/audit/x59-register-law-negatives.py --json
  "rl4_components_checked": 2,
  "rl4_keys_ok": 2,
  "rl4_ids_missing": 0,
```

`L11` reads the components the claim names (discovered from the round's own
`RL4_COMPONENTS` declaration in `reports/round-28/run-validation.py`, falling back
to the round-27 finding), extracts each component's own top-level `packet_keys:`
list and the record ids under the block its records live in, and requires every
id to appear in the packet text. Both declarations now cover their blocks:

```
$ grep -n '^packet_keys' examples/culture-d4/components/03-orthography.yml \
                         examples/culture-d4/components/09-costumes.yml
03-orthography.yml:24:packet_keys: [orthography, records, literacy_institutions]
09-costumes.yml:22:packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]
```

## 5. X59-F2 — RL-1 landed, and it landed mid-audit

This is the finding whose reading changed. It is recorded in both directions,
because the first half of this audit measured the opposite.

**At 20:15Z (first reading): no teeth.** The round's runner declared a
`D4L-LAW-*` leg (`reports/round-28/run-validation.py` `LAW_FINDING_RE`,
classes `D4L-LAW-REGISTER`/`-AXIS`/`-FORCE`/`-SPEAKER`/`-CONSEQUENCE`), but no
delivered instrument under `tools/` emitted the class:

```
$ grep -rln 'D4L-LAW' tools/
(no match)
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml | grep -c D4L-LAW
0
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | grep -c D4L-LAW
0
law_findings_clean=1  law_findings_tampered=2  named_law_findings=0
```

**At 20:20Z (second reading): teeth.** A new gate landed at
`tools/gates/register-law-gate.py` (sha256 `cfbff16b…`, `--selftest` **33/33**),
and the same textual tamper now yields a **new named** finding:

```
$ python3 -B reports/round-28/audit/x59-register-law-negatives.py --json
  "law_replay_candidates": 3,
  "law_replay_runs": 6,
  "named_law_findings": 1,
```

Reproduced directly, from this seat's own shell, on a copy whose first `force`
value is rewritten to `"no-such-value-zzz"`:

```
$ python3 tools/gates/register-law-gate.py .scratch/x59/probe/t3.yml
FINDING D4L-LAW-FORCE: FAIL — RGL-01 force 'no-such-value-zzz' names no declared
  illocutionary class or modifier; the declared set is
  assertive/directive/commissive/expressive/declarative plus
  binding/refused/not-rollable/none/attested/witnessed/naming/constraint
  (reports/round-27/law/design.md section 3; rules.md RU-L2)
coverage: … law_rows=5 … force_failures=1 … findings=5
```

The clean packet emits no `D4L-LAW-FORCE` line (`force_failures=0`); the tampered
copy emits exactly one more, of the class the claim names. **This is the teeth
the claim asks for**, delivered by a gate rather than by the runner alone.

**Both readings are true, at their own stamps.** A reader who takes only the
headline would miss that the class was absent for most of this seat's window; a
reader who takes only the first reading would miss that it landed. Both are
recorded, and the digests in §1 fix which bytes each was taken at.

## 6. X59-F3 — the assembler still does not declare the law block

Distinct from RL-4. The assembler's record validator keys on `RECORD_FIELDS`
(`tools/assemble-culture-d4.py:109-125`), and `register_law` is absent from both
it and the global `PACKET_KEYS`:

```
$ grep -c register_law tools/assemble-culture-d4.py
0
```

The block still reaches the packet only through the component's own per-file
`packet_keys: [register_law]` declaration. This is the round-27 X59 `L9` HOLD,
unchanged; it is not what round 28's RL-4 names, and this audit does not fold the
two together. **Note that the new `register-law-gate.py` now refuses a malformed
law row at the gate layer** — so the enforcement leg exists even though the
assembler's own validator still has no field list for the block. Whether the
claim requires the assembler specifically, or any delivered layer, is the
parent's call; the measurable fact is that the assembler still declares nothing.

## 7. X59-F5 — the law's forces have no declared *packet* vocabulary

The claim asks that "forces [resolve] against a declared vocabulary". The new
gate does enforce a vocabulary — but the vocabulary lives in the **gate's own
source and the design prose** (`reports/round-27/law/design.md` §3), not on the
packet. The packet states 5 distinct `force` values and declares no `force`
vocabulary anywhere this instrument discovers (`force_vocabulary=0`). So the
sub-leg works, and the *packet-side* declaration the phrasing implies is absent.
Reported as a HOLD: the vocabulary may be intended to live in the design rather
than the packet, and this instrument does not invent one.

The speaker half **does** pass: all 10 speaker/holder id tokens resolve, and the
one token that does not (`OR-02`) is annotated by its own row
`(OR-02, component-only)`, so it is recorded as an annotation
(`speaker_component_only=1`), not a dangling reference.

## 8. The parent integrates

Filing, scope, integration into `LOG.md`/`SCORECARD.md`, the D-claim re-run, and
any final promotion verification remain parent responsibilities; in-lane
attestations do not prove a fresh external inspection.

**The D verdict, as dated readings of a live tree.** The round-28 receipt
`measured_at_utc 2026-10-18T20:21:44+00:00` read claim D **red** on one failure
(`d4-gate is not green (exit 2)`); the receipt `measured_at_utc
2026-10-18T20:22:36+00:00` reads claim D **green**, and the receipt at
`20:23:17Z` reads **D/O/C all green** with `missing_dependencies: []`. This
seat's own re-run of
`tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` at 20:22Z
returned **exit 0, `summary: 20/20 legs passed`**, which agrees with the later
receipt and disagrees with the earlier one — the earlier failure was a dated
reading of a runner revision now superseded, not a property of the delivered
gate. Every receipt is true at its own stamp; a reader who needs a *bound*
verdict must re-run `python3 reports/round-28/run-validation.py` and read its
receipt, not this fragment.

This seat's independent contribution to the D verdict is the two laws the claim's
`after_required` names explicitly: **RL-4 landed** (`L11` pass) and **RL-1
landed** (`L6b` pass, §5). The two remaining HOLDs (`L9` assembler declaration,
`L10b` packet-side force vocabulary) are recorded here as gaps this audit can
name, not as failures of the clauses the claim states.

## 9. Boundary record

- **Writes:** this file and its instrument
  `reports/round-28/audit/x59-register-law-negatives.py` (plus gitignored scratch
  under `.scratch/x59/`). No `reports/round-{8..27}` byte was touched, no tool or
  gate was edited, and no shared bookkeeping (`LOG.md`, `SCORECARD.md`) was
  appended. `export TMPDIR=$PWD/.scratch` preceded every scratch write. No
  commit, no push.
- **Independence:** every law is re-derived from the live bytes by this
  instrument, not transcribed from the runner. Where this fragment and the
  runner agree, the agreement is a cross-check, not inheritance. The delivered
  instruments L6b runs are executed in this seat's own shell.
- **Canon:** NON-CANON engineering evidence. This audit admits nothing, certifies
  no round and adjudicates no claim.
