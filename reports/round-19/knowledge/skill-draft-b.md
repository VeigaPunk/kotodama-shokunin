> 2026-10-18 integrator erratum: the reviews' red measurements (L2-channel fail; adapter selftest 1/4) were pre-repair states — the integrator's L2-family patch and the adapter bytes fix landed after the review seats measured. Re-verified at close: typed gate 19/19 exit 0; adapter selftest green. Defect A correction: greens cited from runs over the untyped packet now name the typed run explicitly. Defect B (two wrong leg names in skill-draft-b) corrected to the legs the gate actually emits.

# R19-D05 — SKILL.md draft B: derivation replay — the family's own build, named inputs, text transform

- round: 19 (operator loop 2 of 3, build 3 of 4; `reports/round-19/claims.json`,
  claim **D** `depth`; provider `hyper/deepseek-v4.1-flash` per the operator's
  round-19 substitution). Lane: `kotodama-shokunin`.
- shard **D05** (table drafters ×2, second). Assignment (verbatim): "draft the
  exact SKILL.md subsection text (D4-derived decision tables + error-pattern
  rows), every row cited; reports/round-19/knowledge/skill-draft-a.md,
  skill-draft-b.md."
- date: 2026-10-18 (stamps UTC). Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`; declare `169c616`.
- canon: **NON-CANON engineering draft.** Paste-ready draft text for `SKILL.md`;
  no byte of `SKILL.md`, `corpus/**`, `tools/**` or any filed round-8..18
  artifact is edited. The parent owns placement and admission.
- writes: **this file only**, plus gitignored scratch under `.scratch/r19d05/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  commit, no push.
- companion: `reports/round-19/knowledge/skill-draft-a.md` (R19-D04, the
  slot-label routing model). Disjoint: A owns the routing shape, B owns the
  replay/derivation discipline.

## 0. Verdict

**The D4 derivation is now replayable end-to-end and the three named craft
requirements — machine-readable pattern/output pairs, the round-trip corruption
class, the text-transform rule — are each measurable in committed bytes, so the
derivation-replay subsection can be codified with every row cited.** Measured
2026-10-18T11:32:22Z: the full chain runs green —
`tools/assemble-culture-d4.py` → `examples/culture-d4/packet.d4.yml` →
`tools/d2-typed-labels.py --packet … --check` → `typed-labels.d4.yml` →
`tools/assemble-d4-typed.py` → `examples/culture-d4/packet.d4.typed.yml` →
`tools/gates/typed-pipeline-gate.py`, which exits **0** with `summary: 19/19 legs
passed`.

Three readings carry the subsection:

1. **The family's own build is called.** `tools/assemble-d4-typed.py:62` sets
   `SERIALIZER = ROOT / "tools/assemble-culture-d4.py"` — the adapter's
   assembler-identity leg calls the *family's* assembler, never D2's and never a
   re-implementation. The round-17 refusal was exactly this leg bound to D2
   (`reports/round-17/d4/typed-support-1.md` §4 B4/P3).
2. **The round-trip corruption class is named in the tool.** `tools/assemble-d4-typed.py:297-301`:
   "Derive the typed packet by TEXT transform, never re-serializing foreign
   content: the round-trip serializer corrupts regex backslashes, booleans and
   nulls (D4 is the first culture whose packet carries derivations with regex
   patterns)." Recorded as a capability/calibration datum at `SCORECARD.md:176-177`
   and `SCORECARD.md:185`, and in the round-18 admit entry `LOG.md:3252-3253`.
3. **Named inputs are load-bearing.** Measured control, 2026-10-18T11:32Z:
   `python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml`
   exits **1** (`… differs from the deterministic projection`) while the same
   command with `--packet examples/culture-d4/packet.d4.yml` exits **0**
   (`… byte-identical deterministic projection`). A `--check` that does not name
   its packet measures the wrong pair.

## 1. What the subsection must say (the three requirements, stated before the table)

- **R1 — replay the family's own build.** A typed adapter's assembler-identity
  leg must call the *family's* assembler build path. A shared engine that calls
  another family's assembler refuses a correct packet (exit 2) and, worse,
  invites "fixing" the pin instead of the binding.
- **R2 — replay by text transform, never by re-serialization.** When the packet
  carries content a round-trip serializer cannot preserve byte-for-byte (regex
  backslashes, booleans, nulls), the derived artifact must be produced by a text
  transform of the source bytes plus adapter-generated blocks serialized from
  adapter-owned data alone. Re-serializing foreign content is a corruption
  channel, not a normalization.
- **R3 — replay names every input, and its pattern/output pairs are
  machine-readable.** A derivation's committed expectation must be a
  machine-readable document (counts + rows + pins) and its `--check` must name
  every input; a partial invocation measures a different pair and reports a false
  difference.

## 2. Draft SKILL.md subsection text (paste-ready)

Suggested placement: a round-19 subsection under *Gates and probes*
(`SKILL.md:238`), immediately before the gate registry table, or as a sibling of
the round-7 "D3 replay checklist" (`SKILL.md:348`).

```markdown
### Derivation replay — replay the family's own build, by text transform

A typed derivation is replayable only when three things are true at once: the
identity leg calls the *family's* own assembler, the derived artifact is built by
a text transform of the source bytes (never by re-serializing foreign content),
and the replay names every input. The D4 chain is the worked instance.
Executable authorities `tools/assemble-d4-typed.py` (`SERIALIZER`, `:62`;
`text_payload`, `:296-310`) and `tools/gates/typed-pipeline-gate.py`
(`L1-profile`/`L1-assembler`/`L1-projection_freshness`/`L1-coverage`/`L1-build`,
`L2-channel`, `L3-*`, `L4-pins`); flagless resolution
`tools/gates/typed-pipelines.json`; design authority
`reports/round-18/gate/design.md` §0/§1.3/§11 and
`reports/round-17/d4/typed-support-1.md` §4-§5; measured instance
`reports/round-18/d4/determinism.md` §3, `reports/round-18/d4/manifest.md` §2,
`reports/round-18/d4/interop-1.md` §0.

| Replay requirement | Correct shape | Never | Consequence if violated | Citation |
|---|---|---|---|---|
| Assembler identity | the adapter's identity leg calls the family's own assembler build path (`assemble()` on `tools/assemble-culture-d4.py`), and the identity message names the assembler it actually checked | hard-bind the leg to another family's serializer, or re-implement the build inside the adapter | a correct foreign packet is refused (exit 2) and the default family's bytes move | `tools/assemble-d4-typed.py:62`; `reports/round-17/d4/typed-support-1.md` §4 B4 (receipt P3); `reports/round-18/gate/design.md` §1.3 |
| Named inputs | every input is named on the command line (`--packet` **and** the artifact), so the comparison is the pair the caller meant | run `--check <artifact>` alone against a multi-family tool | a false difference: exit 1 "differs" where the named pair exits 0 — measured 2026-10-18T11:32Z | `tools/d2-typed-labels.py --check` measured control (§4) |
| Machine-readable pattern/output pairs | the committed expectation is a machine-readable document: schema, `counts`, the row list, and the digests it is pinned to | a prose or hand-typed expectation; a pinned count with no row list; a row list with no pins | the equality leg cannot be re-run by a stranger, and a re-pin cannot be distinguished from a re-bless | `examples/culture-d4/expected-holds.json` keys `counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema`; `reports/round-17/d4/typed-support-2.md` §2 (comparison key `(id, severity, where)` as a set, `detail` strings pinned); `tools/gates/typed-pipeline-gate.py:696-734` |
| Round-trip corruption class | derive by **text transform**: rewrite the one moved key in place, append adapter-owned blocks serialized from adapter-generated data alone | re-serialize the whole foreign document through a round-trip serializer | regex backslashes, booleans and nulls are mangled; the derived artifact stops matching its source's semantics while still assembling | `tools/assemble-d4-typed.py:296-310`; `SCORECARD.md:176-177,185`; `LOG.md:3252-3253` |
| Text-transform rule | the transform touches exactly the declared key set (`garment` → `garment_gloss`) and nothing else; the moved value stays in the document | a general "normalizer" that rewrites unrelated lines | the transform becomes an unreviewable second assembler; a byte diff cannot localize a change | `tools/assemble-d4-typed.py:296-310` (the loop renames only `^(\s*)garment:` inside `costumes:`) |
| Flagless resolution | a frozen replay row cannot carry flags (`tools/replay-frozen.py` launches `[python3, <gate>, <input>]`), so the family must resolve flaglessly from a sha-pinned profile matched on the packet's declared `assembly.generator` | a family that can only be graded with CLI flags | the row cannot be frozen; a flag-only path is un-replayable by design | `reports/round-18/d4/manifest.md` §2; `tools/gates/typed-pipelines.json` (`schema kotodama-typed-pipelines-v1`, profile `d4`, every field digest-pinned); `tools/gates/typed-pipeline-gate.py:481-485` (a stale pin refuses, exit 2, `L1-profile`) |
| Determinism | two consecutive builds are byte-identical, and `--check` compares bytes without writing | a build whose output embeds a path, a timestamp, or a host name | the artifact is not replayable; a frozen pin moves under an unrelated edit | `tools/assemble-d4-typed.py:369` (`two consecutive builds are not byte-identical`); `reports/round-18/d4/determinism.md` §3 |
| Pre-registration | the expected set is decided elsewhere **before** the tool runs (design table, design-doc union, or a declared acceptance criterion) and any delta is dispositioned in a filed reconciliation | write the expectation from the tool's own printed output | the equality leg has drift teeth but no content teeth — it cannot distinguish "the set is right" from "the set is a copy of the producer" | `reports/round-18/d4/review-2.md` §0/§2 (the landed D4 file equals the projector's live output verbatim); `reports/round-18/d4/holds.md` §3-§4; `corpus/knowledge/verification/verification-independence-anti-circularity.md` §2 (the circularity catalog) |
| Passenger rows | a row emitted by a shared engine for any packet is attributed **per packet** in the expectation, or excluded | let a packet-independent block silently enter a new family's debt set | the equality leg is described as verifying the new family's design debt while the row names records that occur zero times in its packet | measured: the D4 expected file carries 3 `D2L-RANK` holds + 1 note naming `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g`, `SR-01#a\|SR-01#b`, each **0** hits in `examples/culture-d4/packet.d4.yml` (2026-10-18T11:32Z); `reports/round-18/d4/review-4.md` §2; `reports/round-18/d4/holds.md` §5 |
| Freeze-artifact naming | a freeze receipt that is not a battery baseline is not named `expected.json` under a battery root | land a `freeze-receipt.json` under a name the battery discovers as a baseline | the standing battery fails closed on a gate outside its name constant | `reports/round-18/d4/manifest.md` §6 |
```

Thresholds and cautions that are part of the rule:

- **T1 — identity is checked against the declared assembler, and the message
  names it.** An identity leg that still says "assemble-d2.py" while grading a D4
  packet is the round-17 rejection reproduced at a new address
  (`reports/round-18/gate/design.md` §1.1, §11 item 4).
- **T2 — a skipped leg is not an implementation.** A packet declaring no assembler
  must resolve to the documented default, not to "identity not checked"; a
  `return True` branch for non-default input is a laundering channel of the same
  class as a laundered hold (`reports/round-18/gate/design.md` §1.3).
- **T3 — the round-trip class is about *content*, not about determinism.** A
  serializer can be perfectly deterministic and still corrupt a regex backslash;
  determinism (two runs equal) and fidelity (the derived artifact preserves the
  source's content) are separate checks and neither implies the other.
- **T4 — a projection embeds its packet path.** The D2 projection differs from a
  scratch-path emission in exactly two lines (`assembly.packet`, `canon`), so a
  family's projection must be emitted from its canonical path
  (`reports/round-17/d4/typed-support-1.md` §3 P1, F-D18-5).
- Cautions that are part of the rule: exit 0 is not a clearance — it means "the
  emitted findings equal the frozen expected set" and every hold stays open
  (`reports/round-18/d4/manifest.md` §6); a re-pin that changes the hold set is a
  finding, not a pass (`corpus/knowledge/verification/verification-independence-anti-circularity.md`
  §2, §6); a green self-test is capability, not measurement
  (`corpus/knowledge/verification/gate-frozen-run-standard.md` §1).

## 3. Draft error-pattern rows (paste-ready — append to `## Error patterns`)

```markdown
| The adapter's assembler-identity leg calls another family's serializer | the round-17 rejection at a new address: a correct foreign packet is refused exit 2, and the temptation is to re-pin rather than re-bind — call the family's own `assemble()` (`tools/assemble-d4-typed.py:62`; `reports/round-17/d4/typed-support-1.md` §4 B4) |
| A `--check` invoked without naming the packet | measures the wrong pair: exit 1 "differs" where the named pair exits 0 (measured 2026-10-18T11:32Z: `tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml` → 1; with `--packet examples/culture-d4/packet.d4.yml` → 0) |
| The derived artifact is produced by re-serializing foreign content | the round-trip corruption class: regex backslashes, booleans and nulls are mangled while the artifact still assembles — derive by text transform (`tools/assemble-d4-typed.py:296-310`; `SCORECARD.md:185`) |
| A text transform that rewrites lines outside its declared key set | an unreviewable second assembler: the transform must touch exactly the moved keys, and a byte diff must localize any change (`tools/assemble-d4-typed.py:296-310`) |
| An "expected" set written from the tool's own printed output with no locus predating the tool | transcription, not pre-registration: the equality leg then has drift teeth but no content teeth (`reports/round-18/d4/review-2.md` §0/§2; `corpus/knowledge/verification/verification-independence-anti-circularity.md` §2) |
| A shared engine emits a packet-independent block into a new family's expectation | passenger rows: the records occur zero times in the new packet (measured: `TR-04`/`WR-02`/`WR-08`/`SR-01` → 0 hits in `examples/culture-d4/packet.d4.yml`, present in its expected file); attribute per packet or exclude (`reports/round-18/d4/review-4.md` §2) |
| A family that can only be graded with CLI flags | un-replayable by construction: `tools/replay-frozen.py` launches `[python3, <gate>, <input>]`, so the family needs a flagless sha-pinned profile (`reports/round-18/d4/manifest.md` §2; `tools/gates/typed-pipelines.json`) |
| A stale profile pin silently re-pointing a run | refuse, don't adapt: the profile's every field carries its live digest, and a stale pin exits 2 with `L1-profile` until it is re-pinned with a command and a date (`tools/gates/typed-pipeline-gate.py:481-485`; `tools/gates/typed-pipelines.json` `note`) |
| A freeze receipt landed as `expected.json` under a battery root | the standing battery fails closed on a gate outside its name constant — name the receipt distinctly (`reports/round-18/d4/manifest.md` §6) |
```

## 4. Measured basis (so the parent can paste with citations)

Every reading below was taken by this seat, read-only, from the lane root, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, on **2026-10-18**; the
gate revision is `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`
(11:32Z) where it matters.

| command | observed |
|---|---|
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # typed pipeline: gate builds the typed packet via the adapter` | exit **0**, `summary: 19/19 legs passed`; the banner names the declared pipeline (`family d4; profile tools/gates/typed-pipelines.json (sha256 434e90509a1c); assembler tools/assemble-culture-d4.py (sha256 943f487ba991); adapter tools/assemble-d4-typed.py (sha256 087846719041)`) |
| `python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml` | exit **1** — `examples/culture-d4/typed-labels.d4.yml differs from the deterministic projection` |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | exit **0** — `… byte-identical deterministic projection` |
| `grep -n "^SERIALIZER\|^ROUTED_KINDS\|^HOLD\|^CHANNEL" tools/assemble-d4-typed.py` | `:62` `SERIALIZER = ROOT / "tools/assemble-culture-d4.py"`; `:65` `ROUTED_KINDS = ("translated-label",)`; `:66` `HOLD = "D2L-FORM-UNRESOLVED"`; `:67` `CHANNEL = "off-sound-and-identity"` |
| `grep -n "round-trip\|text_payload" tools/assemble-d4-typed.py` | `:296` `def text_payload`; `:297-301` the corruption-class docstring; `:369` the two-builds-not-identical guard |
| `grep -n "L3-\|L2-channel\|L1-assembler\|L4-pins\|L1-profile" tools/gates/typed-pipeline-gate.py` | legs at `:481-485` (`L1-profile`), `:499` (`L1-assembler`), `:696-734` (`L3-*`), `:750` (`L3-routing-consistency`), `:763-791` (`L4-pins`) |
| `grep -c -- "TR-04" examples/culture-d4/packet.d4.yml` (and `WR-02`, `WR-08`, `SR-01`) | **0** each — the D2 rank constants name no delivered D4 record; the same tokens are present **1** each in `examples/culture-d4/expected-holds.json` (passenger rows) |
| `grep -n "rank_rules" examples/culture-d4/packet.d4.yml` | `:1705` — D4 declares its own `RK-01..RK-04`, which the emitted `D2L-RANK` rows do not name |
| `cat tools/gates/typed-pipelines.json` | schema `kotodama-typed-pipelines-v1`; one profile `d4` matched on `assembly_generator: tools/assemble-culture-d4.py`; every path digest-pinned (packet `e7ecd204…`, assembler `943f487b…`, projection `a59990bb…`, expected `09490a27…`; adapter pin `null` with a note) |
| `cat tools/gates/frozen/round-18/MANIFEST.tsv` | 2 rows: `d4-typed-labels-check-gate.py` (`05f99629…`) over `typed-labels.d4.yml`, and `d4-assembly-check-gate.py` (`df1a364b…`) over `packet.d4.yml`; both exit 0, 0 findings — the two thin gates the round-18 freeze could pin (`reports/round-18/d4/manifest.md` §2) |

## 5. Limits and what the parent must decide

1. **The D4 expectations' provenance is contested on record.** `reports/round-18/d4/review-2.md`
   §0 measures the landed `expected-holds.json` as the projector's own output
   verbatim, and `reports/round-18/d4/holds.md` §4 records the delivered
   declaration (6 holds / 0 notes) versus the emitted set (15 / 1). The
   pre-registration row above is drafted from that record; if the parent lands a
   superseding reconciliation, the row's citation changes, not the rule.
2. **The round-18 frozen manifest pins two thin check gates, not the D4 pipeline
   row.** The generalized gate's D4 row is not in `tools/gates/frozen/round-18/`
   (`reports/round-18/d4/manifest.md` §1: the pending row's input did not exist
   at freeze time). A SKILL statement that says "the D4 row replays" must name
   the manifest and the date it actually replays; the two rows that exist replay
   green.
3. **Tool shas move.** The adapter sha observed in the gate banner
   (`087846719041`) and the gate sha (`04ad4bb4…`) are read-time pins. The
   `typed-pipelines.json` profile pins the assembler/projection/expected but
   carries `adapter.sha256: null` with a note to pin it at the first freeze after
   the adapter lands — a follow-up the parent may route.
4. **`SKILL.md` is not edited by this seat.** Draft text only; `SKILL.md` line
   numbers cited above (`:238`, `:348`) shift at landing and must be re-read then.
5. **NON-CANON throughout.** No clearance, no canon, no handoff; hold counts are
   design debt (`AGENTS.md`, `PROVINCE.md`).
