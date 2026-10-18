# Round 25 — lessons gate-keeper: a rebuild is not the source, a guard on one field is not a guard on its sibling

source: `reports/round-25/claims.json`; `reports/round-25/targets.json`; `reports/round-25/scope.md`; `reports/round-25/gate-input/diagnosis.md`; `reports/round-25/gate-input/design.md`; `reports/round-25/argot/forecast.md`; `reports/round-25/argot/current-state.md`; `reports/round-25/argot/delta.md`; `reports/round-25/audit/x47-argot-negatives.md`; `reports/round-25/audit/x48-v3-supersession.md`; `reports/round-25/audit/c31-lessons-index-audit.{py,md}`; `reports/round-25/lessons/lessons-index-census.py`; `corpus/lessons/README.md`; `tools/gates/typed-pipeline-gate.py`; `tools/assemble-d2.py`; `tools/gates/naming-collision-gate.py`; `examples/culture-d4/packet.d4.yml`; `examples/culture-d4/packet.d4.typed.yml`; `examples/culture-d4/typed-labels.d4.yml`; `examples/culture-d4/expected-holds.json`; `reports/round-20/handoff/claims-map.md`; `reports/round-17/d4/design-brief.md`; `reports/round-19/knowledge/analyst-3.md`; `corpus/lessons/round-23.md`.

verified-at: opening read-only survey **2026-10-18T17:24:51Z–17:36:38Z** (all stamps from `date -u --iso-8601=seconds`; `python3` 3.14.7). `git rev-parse HEAD` returned `f74fc9403d4b02c8ee76439eb133e3dea9b65b14` — the round-25 declaration commit ("declare loop-3 build-1 claims O/D/C"). The claims' `baseline_revision` is `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`, which is the parent of that commit and resolves as the round-24 close ("admit C/O/D — promotion-review dossier green; LOOP 2 COMPLETE"); the declaration-time baseline binding is therefore correct. `reports/round-25/targets.json` names 64 workers (O-gate-input 10, O-v3-supersession 10, D-argot 24, C-lessons 12, X 8), equal to the claims' 64. The working tree was **not clean** at the stamp: `git status --porcelain` listed 9 paths, all round-25 in-flight evidence. Filed artifacts of rounds 8–24 were not modified by this seat and no filed byte was edited. **The window is not a single revision**: `tools/gates/typed-pipeline-gate.py` moved through at least five digests inside it, and the O gate-input repair landed mid-window (see the two reading tables below); every reading here is bound to the digest named beside it, and in-flight round-25 bytes must be re-read at their final revision (see Dated observations).

recheck: read the round-25 runner's receipt only after it appears; this scribe does not invoke a round validator, refresh a receipt, or edit any round-25 tool. The counting command declared for all three claims is `python3 reports/round-25/run-validation.py` (`reports/round-25/claims.json`, dated 2026-10-18); the file was **absent** at every stamp in this survey window (17:24:51Z–17:36:38Z). A missing dependency is pending, not green: it was polled at 60-second intervals and remained absent. Historical round validators run only in isolated clones with protected hashes checked before and after; every scratch-writing command in this survey ran with `export TMPDIR=$PWD/.scratch` from the lane root (scratch under `.scratch/x38/`, gitignored).

scope: SCRIBE X38 writes only `corpus/lessons/round-25.md`. This is a gate-keeper lesson, not the round verdict, an independent certification of the workers' pin rows, or the orchestrator's integration. The path was unclaimed at the stamp (`grep -rn "corpus/lessons/round-25" reports/round-25/` → no match) and did not exist before this write. Filed rounds 8–24 are read-only; re-pins are new rows/revisions and corrections are new files, never altered historical evidence. Shared LOG/SCORECARD/SKILL integration belongs to the parent and assigned owners. Everything remains NON-CANON; lore owns canon, and no real-world clearance, attribution-rights ruling, or game-mechanics decision is made here.

## Gate

Axes as declared: **O / operability**, **D / depth**, **C / coverage**. The O claim carries two independent hazards — the typed-pipeline gate's false red on derived-packet input, and the stale D4 claim prose in the handoff v3 revision. The D claim is the round-17 argot-derivation forecast. The C claim is the reconciled `corpus/lessons/README.md`. Keep the readings separate: a reproduced diagnosis is not a landed repair, a named delta is not a delivered leg, and an index that passes its own checker is not an index whose bytes held still while it was checked.

### Rule

A gate that grades a derived artifact must reconstruct the artifact's *source* faithfully or decline to grade it; when its own reconstruction is the thing that manufactures findings, the red belongs to the reconstructor, not to the input. A nullish guard written for one field of a routing row does not guard its sibling field, and the two fields are read by the same comparison. A declared refusal is not a reachable refusal: an input-class branch that a prior leg's unguarded read can crash before it is reached fails open, and a selftest that exercises that branch on only one family does not cover the family the round grades. A repair is landed only when the live tool bytes carry it, and a landed repair is not a verified one — the bytes that carry it must still be re-read at their final revision. A design forecast is delivered only when the declared capability exists on disk and has been executed; enumerating what is missing is a delta, and the claim's own text must then say which of the two it is.

### O — operability: the false red is repaired; the input-class refusal has a hole on the generalized family

**(a) The typed-pipeline gate fed its own derived packet.** Reproduced independently from the live bytes **before** the repair landed, with the gate pinned by digest `04ad4bb479562c41…` (unchanged since the round-22 freeze; the sibling `gate-input/diagnosis.md` §1 records the same pin and the same four-row reproduction table — this seat's readings are its own and agree):

| # | command (2026-10-18) | exit | legs | failing legs |
|---|---|---|---|---|
| F1 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | 19/19 | — |
| F2 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **1** | 14/16 | `L2-channel`, `L3-routing-consistency` |

The documented source-packet entry (F1) still passes **19/19** — that half of the claim's acceptance boundary is met at this stamp. F2 is the false red, and it is **two distinct defects, not one**:

1. **`L2-channel` fabricates eight `DERIV-REPLAY` findings.** The gate rebuilds a legacy packet from the typed one (`typed-pipeline-gate.py:586-604`) and grades the rebuild against the typed run. This seat captured that rebuild by spying on `gate_bundle` (`.scratch/x38/capture-rebuild.py` → `.scratch/x38/captured-packet.d2.yml`) and ran the naming gate over both artifacts as a control:

   | artifact | `naming-collision-gate.py` DERIV-REPLAY count |
   |---|---|
   | the gate's own rebuild (`.scratch/x38/captured-packet.d2.yml`) | **8** |
   | the real source packet (`examples/culture-d4/packet.d4.yml`) | **0** |

   Same gate, same tool bytes, same `names:` block. A line-by-line diff over `morphology.derivation_rules` (`sed -n '204,226p'`, both files) shows **exactly one differing line**:

   ```
   <       pattern: "^(?P<a>.+)\\+(?P<b>.+)$"      # source packet
   >       pattern: "^(?P<a>.+)\\\\+(?P<b>.+)$"    # the gate's rebuild
   ```

   The mechanism is `tools/assemble-d2.py:66-69`: `scalar()` returns `json.dumps(value)`, so every string is JSON-quoted on the way out and each backslash is doubled. `re.search` over `tum+hai` with the doubled pattern returns `None` (checked directly, 2026-10-18T17:26Z), so all eight compound names fail their declared rule and the gate reports them as *non-artifact removals*. **The rebuild is the producer of the findings it then reports.** This is the exact hazard SKILL.md's own round-trip-corruption row names ("regex backslashes, booleans and nulls are mangled"; `SKILL.md:189-214`) — the gate's L2 leg violates the discipline its own SKILL section states, so the fix has a documented home rather than needing a new design.

2. **`L3-routing-consistency` compares six owed slots against twelve entries.** The `holds`/`routed` halves agree (12 = 12); only the owed-slot half fails. The observed side is 12 entries, the routing side 18: six phantom `'null'` strings. The cause is a **guard gap inside one file**. `moved_field()` (`typed-pipeline-gate.py:186-196`) correctly null-guards `off_channel_field` — its own docstring says "a missing key or a null-ish value (`null`, `none`, `~`, empty — the lane's reader keeps an unquoted `null` as the string) means the row stays on channel". The sibling read at `:748-749` has **no such guard**:

   ```python
   routed_slots = sorted(row.get("owed_slot") for row in routing
                         if moved_field(row) and row.get("owed_slot"))
   ```

   Measured directly against the live typed packet (2026-10-18T17:27Z): all 12 routing rows are read, the six garment rows carry the Python **string** `'null'` (the reader keeps the unquoted YAML `null` as text, exactly as `moved_field`'s docstring warns), and `'null'` is truthy — so all six survive the filter. The guard exists in the same file, for the same row shape, and was applied to one field but not its sibling.

**The gate-input repair landed during this survey — and it carries one measured gap.** At 17:31:40Z the gate bytes moved (`04ad4bb479562c41…` → … → settled at `879d40bf977eef65…`, 2026-10-18T17:35:54Z). The landed fix takes the claim's **first** branch, and takes it well:

| probe (2026-10-18T17:35:57Z, gate `879d40bf…`) | result |
|---|---|
| `…gate.py examples/culture-d4/packet.d4.yml` (documented source entry) | exit **0**, 19/19 |
| `…gate.py examples/culture-d4/packet.d4.typed.yml` (typed packet fed back) | exit **0**, **16/16**, DERIV-REPLAY lines **0** |
| `…gate.py` (flagless D2 default) | exit **0** |
| `…gate.py --selftest` | exit **0**, **19/19** (was 12/12) |

The fix is the right shape rather than a patch: `typed-pipeline-gate.py:620-635` now grades the typed packet against **the source it declares**, digest-checked against the packet's own `assembly.packet_sha256`, instead of against the gate's own rebuild — with a comment naming this survey's finding class verbatim ("the serializer's `scalar` escapes backslashes a second time and the reader keeps an unquoted `null` as the string, so grading a rebuild manufactures DERIV-REPLAY findings that exist in no file (round-24 cold-run C2)"). The `owed_slot` guard is landed as a named sibling of the existing one (`:213-222`, `owed_slot_of()`, sharing the `nullish()` test with `moved_field`, with the docstring "the two halves of a routing row cannot disagree"), and the comparison at `:841` now uses it. A stale declared source refuses **exit 2 with the class named** (measured: `typed-stale-source`, "the derived artifact is stale against its own source; re-derive it or grade the source"). An unnamed typed packet falls to the rebuild branch, where the round-trip check now fires and reports `typed-unfaithful-rebuild` (measured on a declaration-stripped copy: exit **2**, with the message naming the manufactured delta and the serializer's double-escaping as its cause).

**The gap: the `typed-unresolvable` branch is unreachable for a generalized family.** The new code sets `input_class = "typed-unresolvable"` and refuses exit 2 when a declared source is unreadable (`:649-657`), but **L1 runs before L2** and reads that same path unconditionally. `assembler_identity()` at `:443` does `Path(packet_path).read_bytes()` with no guard, and `:529` passes it `config["packet"]` for a typed input. Measured as a **matched pair** — one byte-level edit per family, the declared source renamed to a nonexistent path, nothing else changed (`.scratch/x38/orphan-{d2,d4}.yml`):

| input | family | result |
|---|---|---|
| `orphan-d2.yml` | default (D2) | exit **2**, `FAIL L2-channel: typed-packet input without its source: … declares source examples/culture-d2/packet.ABSENT.yml, which is unreadable — a typed packet is the pipeline's output, not a gate input` |
| `orphan-d4.yml` | generalized (D4) | exit **1**, **uncaught `FileNotFoundError` traceback** from `typed-pipeline-gate.py:443` |

The asymmetry is not in the L2 logic — both families reach the same `source_named and source_bytes is None` test — it is that L1's `identity_requested` is true only for a non-default assembler (`:508-509`), so only the generalized family reaches the unguarded read first. The selftest's own input-class controls are built on the **D2** fixture (`:1140-1180`, `orphan-typed.yml`), so 19/19 passes while the D4 path crashes. The claim's `after_required` requires the gate to "fail closed and honestly on derived-packet input" with "a named input-class diagnostic … exit 2" — an uncaught traceback is neither closed nor honest, and the claim's own counting command grades the D4 family. This is a **new, dated finding of this survey**, not a re-litigation: the branch exists, is documented, and is untested on the family the round is about.

Acceptance boundary, updated: the source-packet entry still passes **19/19** (met); the typed packet fed back no longer manufactures findings (**met**, 16/16, zero DERIV-REPLAY); the null handling is correct (**met**, with the sibling guard landed); the pin cascade as **new rows** (not verified here — no runner); and the input-class refusal must hold **for the generalized family too** (**not met** — `orphan-d4.yml` exits 1 on a traceback where `orphan-d2.yml` exits 2 with the class named).

**The readings above are revision-bound and the file moved under them.** This seat observed the gate at five distinct digests inside 17:31–17:36Z (`36b56392…`, `a6e8d9c8…` with a `KeyError: 'owed_slot_of'` selftest failure, `879d40bf…`, `daeaa722…`, back to `879d40bf…`). The definitive table is bound to `879d40bf977eef65…`, stable for four consecutive 15-second polls. A consumer must re-run rather than inherit — the earlier red readings (F2 exit 1 / 14/16) were true of `04ad4bb4…` and are false of the settled revision.

**(b) The handoff v3 stale D4 claim prose.** The stale numbers are located and the delta is measured, but the supersession is **not wired in** (re-measured at 17:37:59Z; unchanged from the opening stamp). Three surfaces carry the pre-family-clean prose:

- `reports/round-20/handoff/claims-map.md:97-102` — `D4-CL05`'s statement still reads "carries 16 findings of which 15 are hold-or-fail (12 label holds, 0 label fails)"; `:150-156` — `D4-CL09` still reads "13 unresolved rank items, 3 quarantine handles and 4 conflicts".
- `tools/exercise-handoff-e2e.py:3524-3532` — `OQ-V3-05`'s prose is a **hard-coded string literal**: "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts". A literal cannot self-correct; the live bytes measure `{hold: 12, note: 0, fail: 0}` with `findings_total 12`, `rank_rules_unresolved_items 0`, `rank_quarantine_handles 0`, `conflicts 0` (`examples/culture-d4/typed-labels.d4.yml:28-46`, read 2026-10-18). **Re-measured at 17:37:59Z and unchanged** — the literal still reads the pre-family-clean numbers.
- The D4 rows are parsed from the filed round-20 `claims-map.md` (`exercise-handoff-e2e.py:2289-2319`), so the stale prose has **two** sources, not one.

Correctly current in the same rows: `typed_labels 74` and `labels_by_kind 56/12/6` — the staleness is **partial**, which is why a whole-row diff would misreport it. The sibling `audit/x48-v3-supersession.md` measures the same delta (8 stale assertions in each of the four revisions) with its own 11/11-control tool; this seat's readings are its own and agree. The superseding revision `reports/round-25/v3-supersession/declared-in-r4/packet.md` exists and its `D4-CL05`/`D4-CL09`/`OQ-V3-05` rows carry the family-clean numbers — but the exercise still resolves `V3_BASELINE_DEFAULT = "reports/round-22/handoff/declared-in-r2/expected.json"` (`exercise-handoff-e2e.py:1933-1934`), so **the r4 revision is not the default the validator reads**. The claim's `after_required` requires the prose "corrected … and re-pinned as a new revision (declared-in-r4)" with "the OQ-V3-05 passengers dispositioned". The revision is filed; the wiring is not; the filed `declared-in-r2` bytes remain (correctly) untouched.

**Regression gate.** Every leg named in this survey ran green at its final revision with command and date (2026-10-18T17:35:57Z, HEAD `f74fc94`, gate `879d40bf…`): `assemble-culture-d4.py --check` exit 0 (byte-identical deterministic assembly); `assemble-d4-typed.py --selftest` exit 0 (12/12); `d2-typed-labels.py --selftest` exit 0 (163/163); `typed-pipeline-gate.py --selftest` exit 0 (**19/19**); `exercise-handoff-e2e.py --profile v3` exit 0 (105/105 links, 16/16 fields, 27 claims, statuses 16/7/4); `--profile v2` exit 0. `check-gate-battery.py` reports 9 gates registered, 0 uncovered, 7 pass / 0 fail / 0 unevaluable. The **historical refusals stay visible beside the successor greens**: the pre-repair F2 red (exit 1 / 14/16) was true of gate `04ad4bb4…` and is false of the settled revision, and the frozen round-22/round-23 receipts retain their own verdicts. A green regression leg is not a landed repair — every leg above passes on a tree that still exits 1 on a traceback for the `orphan-d4.yml` input-class control, which no leg in the battery exercises.

### D — depth: the leg landed mid-survey, and it has two measured gaps

The claim's `after_required` asks for the argot-derivation leg **implemented and executed** on D4, with the delivered-vs-forecast delta recorded and any undelivered element "named, not silently dropped". This seat measured the tree **twice**, and the answer changed between the readings — the leg landed at 17:36–17:37Z.

| probe | 17:30:06Z | 17:37:36Z |
|---|---|---|
| files under `tools/` carrying `ARGOT-DERIV` | **0** | **4** (the gate, its fixture, its expected, a `.pyc`) |
| `tools/gates/argot-derivation-gate.py` | absent | present, `sha256 07db6e9b4e01539e…` |
| `grep -c "derived_from" examples/culture-d4/packet.d4.yml` | 0 | **0** |

So the capability now **exists on disk and executes**. `python3 tools/gates/argot-derivation-gate.py --selftest` → exit 0, **18/18** checks, including a `c-02-negative-control-rejected` leg — the exact control the round-17 forecast named (`design-brief.md:456`, "quote form ≠ `apply(op, base)`" → FAIL `D4L-ARGOT-DERIV`). Run against its own fixture the gate is genuinely live, not a stub:

```
coverage: … records=14 register_scoped=11 derived_pairs=8 borrow_pairs=3 violations=4 rule_holds=1
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-12 'kin' (register 'quote'): declared chain 'reverse' applied to 'kin' yields 'nik'; …
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped loan B-03 'gal' (register 'trade'): layer 'West layer' substitutions applied to donor form 'gol' yield 'gol'; …
FINDING D4L-ARGOT-RULE: HOLD — register-scoped form Q-20 'nuka': declared derivation 'someop' is neither a declared argot operation (head2, reverse) nor a licensed packet rule (CX-01); replay is not possible
```

(exit 1 on the fixture — four violating forms plus a non-replayable rule, exactly the ids the forecast specified.)

**Gap 1: on the live D4 packet the leg finds nothing to replay, and the gate exits 0 anyway.**

```
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # exit 0
coverage: … records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0
```

Six register-scoped records, **zero** derived pairs — because the delivered D4 packet still carries no `derived_from`/`derivation` relation field (`grep -c` → 0). The claim says the leg is "executed **on D4**" and that "a violating form is `D4L-ARGOT-DERIV`". Executed, yes; exercised on D4, no — the D4 run is the vacuous case the round's own `argot/delta.md` flagged as F-5 "**VACUOUSLY SATISFIED**: trivially true — there is no argot form and no leg, so no fail can exist. Not a delivery." The leg's own source anticipates this — `argot-derivation-gate.py:528-534` emits `D4L-ARGOT-COVERAGE` ("the forecast derivation relation is declared, not delivered") — but that branch is gated on `declared_ops = packet_declares_ops(packet)`, which is empty here: it reads `derivation_ops` lists (absent from D4) and the `id`/`name`/`kind`/`note`/`description` text of `morphology.derivation_rules` (`:377-383`), and D4's three rules are named `CX-01/02/03` with notes "STACK-COMPOUND …", "CRAFT-AGENT …", "ATTRIBUTIVE …" — neither `head2` nor `reverse` appears, so no operation is detected. **The guard exists and cannot fire on this packet**, and the live D4 run therefore exits **0** with no coverage message. A consumer reading only the D4 exit code sees a green gate over a family that declares no derivations. The fixture's 8 derived pairs prove the engine works; the D4 packet's 0 proves the D4 half of the claim is unmet. This is the schema half of the delta (`delta.md` §1 F-3, "**NOT DELIVERED — no such fields exist**"), still open — and the gate's own docstring is candid about the limit ("A family that declares its argot operations only in prose elsewhere is not detected, and that limit is stated in the module docstring rather than guessed around", `:358-367`), which is the honest way to carry it.

**Gap 2: the leg is not wired into the D4 typed gate or the battery.** The claim requires "the D4 typed gate grows the leg with selftest controls". Measured: `grep -n "argot\|ARGOT" tools/gates/typed-pipeline-gate.py` → **no match**, and the gate's `GATE_NAMES` tuple (`:86-91`) still lists the same five culture gates. `grep -n "argot" tools/check-gate-battery.py` → **no match**; the battery still reports `gates_registered: 9`, `gates_uncovered: []`, unchanged. So the leg is a **standalone** gate, reachable only by invoking it by name. That is a defensible shape — but it is not the shape the claim text declares, and it means the D4 typed gate's 19/19 carries no argot coverage: the new leg is outside the pipeline it was supposed to grow.

Both gaps are consistent with the round's own reading of its state. `argot/delta.md` opens "The round-17 argot-derivation forecast is **not delivered**" and widens the gap to "a **schema + engine + gate** delta, not a gate delta alone"; `argot/forecast.md` enumerates F-1..F-8 verbatim from `reports/round-17/d4/design-brief.md:296-310` and `:456`; `reports/round-25/docs/derivation-relation-docs.md` is explicitly "**DRAFT ONLY** … This seat wrote no `corpus/**` byte". The **engine** element is now delivered (the gate + its 18/18 selftest + the fixture that fires the control). The **schema** element (D4 records carrying the relation) and the **wiring** element (the typed gate growing the leg) are not.

Acceptance boundary: the claim is **partially met**. The honest reading a consumer should carry forward is "engine delivered, schema and wiring open, delta named" — not "delivered", and not "not delivered". Round 19's analysts marked the same forecast design-forecast, not delivered (`reports/round-19/knowledge/analyst-3.md:103-104`); this round has moved it one element forward and left two named.

One pointer the claim names deserves a reading of its own: `corpus/lessons/README.md:130` asserts Q-04-1 as "**delivered round 25** — the argot-derivation leg (claim D) is the adapter". That assertion was **ahead of the tree** at 17:30Z (0 files) and is **half-right** at 17:37Z (the engine exists; the D4 schema and the wiring do not). A consumer reading the index after the round closes must re-measure it rather than inherit it — the standing reason the index's own rule is "re-derivation, not inheritance".

### C — coverage: the index lands and passes its own checker; the checker's inputs moved under it

`corpus/lessons/README.md` landed during this survey window and is the reconciled index the claim asks for. At the settled stamp (2026-10-18T17:30:03Z, `sha256 c1af089541a6c8f6…`, 250 lines, 22 065 B) the C seat's own read-only checker reports:

```
index present: True   lesson files: 24   index rows: 24   queue rows: 49
formats: {'gate-keeper': 13, 'fragment-index': 5, 'plain': 6}
  PASS C31_index_rows_eq_files      PASS C33_formats_documented
  PASS C32_owners_resolve           PASS C34_pins_rederived
  PASS C34b_prose_arithmetic        findings: 0
```

(`python3 -B reports/round-25/audit/c31-lessons-index-audit.py`, 2026-10-18; exit 0.) This seat re-derived the arithmetic **independently and escape-aware** — Markdown table cells must split on `|` while honoring `\|`, which the naive `str.split("|")` does not — and reproduces the README's own declared figures exactly:

| figure | README declares | this seat's independent recount |
|---|---|---|
| lesson files (excluding README) | 24 | **24** |
| queue data rows | 49 | **49** |
| owner class `path` | 37 | **37** |
| owner class `parent` | 9 | **9** |
| owner class `operator` | 3 | **3** |

Format classes re-measured from the bytes agree too: gate-keeper 13, fragment-index 5, plain 6. The `Q-20-3` row is the one row carrying an escaped pipe (`--profile v2\|v3`); under a naive split it yields five cells and the owner column misaligns, which is why an escape-aware reader is required rather than optional. The claim's counting-command requirement ("reproduces the file count") is met: `ls corpus/lessons/*.md | grep -v README | wc -l` → **24**.

**Two dated observations about this index, both of which a consumer must know.**

First, **the index was written while it was being checked, and it changed twice under this seat's reads.** At 17:27:26Z the checker reported `FAIL C32_owners_resolve` with eight unresolvable owners; at 17:28:04Z the same command reported `FAIL` with seven; at 17:28:39Z it reported **all four checks PASS, findings 0**; and between 17:28:39Z and 17:29:57Z the file's digest moved again (`f0a2b24b…` → `c1af0895…`, 240 → 250 lines) before settling. The README's mtime is 14:29:06 local = 17:29:06Z. **The red readings are not evidence that the landed index is defective; they are evidence that the index was in flight**, and this seat's stamp on each reading is what makes that distinguishable. A consumer must re-run the checker against the settled bytes — this survey's greens are bound to `sha256 c1af0895…` only.

Second, **two C-claim tools were written for the same partition and initially disagreed on one row.** `reports/round-25/audit/c31-lessons-index-audit.py` classifies `round-7.md` as **plain** (its `FORMAT_MARKERS` match `^## Gate$` exactly, and round 7's heading is `## Gate candidates` — a prose heading, not a gate block); `reports/round-25/lessons/lessons-index-census.py` initially returned `gate-keeper-survey / gate-block` for the same file, because its `GATE_RE` matched the looser `## Gate …` heading. At the settled revision the census tool carries an explicit `GATE_EXACT_RE` and returns `plain-lesson / gate-heading-prose` (`lessons-index-census.py:100-125`), so **both tools now agree** and the README's §3 statement ("Round 7 is also plain by this classifier: its `## Gate candidates` heading is prose, not a gate section") is correct. Recorded as a resolved two-tool divergence, not a standing defect — but it is the reason the index's format column should be read as one classifier's reading, not as a fact about the file.

The open-question queue is **extracted, not exhaustive**, and the README says so in its own §4; the claim asked for "the open-question queue extracted with an owner per item", which is what landed (49 rows, every owner resolving at the settled revision). One row is a forward pointer rather than a closed item and is named above under D (Q-04-1).

**Third observation, later in the window: the index now carries a row for this very file, and its pin is stale by construction.** By 17:37:18Z the README had gained `:94` — a `round-25.md` row with `bytes=26897 lines=150 sha8=feccf068` — while the file on disk had grown to `32 082 B / 172 lines / sha8 8800a446…` as this seat continued writing it. The C checker reports exactly that:

```
FAIL C34_pins_rederived
  C34-1 pin-drift: [('round-25.md', 'bytes', '26897', 32082),
                    ('round-25.md', 'lines', '150', 172),
                    ('round-25.md', 'sha8', 'feccf068', '8800a446')]
```

This is **the index's own rule working as designed, on the one file that could not hold still**: a lesson file is written once and then pinned, and this lesson was still being written when its row was added. Two consequences the parent must carry. First, the pin is **not a defect of the C seat** — it is an unavoidable ordering artifact, and the fix is to re-measure the row after this file's bytes are final (the README is the C seat's artifact; this scribe does not edit it). Second, and more usefully, it is a **live demonstration of the C claim's central discipline**: a pin taken on bytes that are still moving is not a pin. The README says this in its own §0 ("A consumer must re-measure rather than inherit") and the C31 checker enforces it; the round should treat the `C34-1` finding as evidence that the checker works, not as a C failure.

## Closeout and rejected readings

Before admission, the parent must read the final round-25 receipt and verify: the O gate-input hazard is closed by one of the two permitted branches **with a control** — the typed packet fed back no longer manufactures findings (**measured met**: 16/16, zero DERIV-REPLAY at gate `879d40bf…`), the source-packet entry still passes 19/19, **and** the input-class refusal holds for the generalized family (the `orphan-d4.yml` control must exit 2 with the class named, not 1 on a traceback — **not met at this stamp**); the pin cascade landed as **new rows** with before/after digests; the v3 supersession is **wired** (the r4 revision is what the validator resolves) with the `OQ-V3-05` passengers dispositioned and the filed `declared-in-r2` bytes untouched — **not met at this stamp**; the D leg is **wired into the D4 typed gate** and **exercised on a D4 packet that declares derivations** — the engine is delivered and green on its fixture, but the live D4 run reports `derived_pairs=0` and exits 0 while the gate that was to grow the leg does not invoke it (**partially met: engine delivered, schema and wiring open**); the C index passes its checker against the settled bytes, with the checker's own revision recorded and the `round-25.md` pin re-measured after this lesson's bytes are final; and protected filed artifacts of rounds 8–24 stayed unchanged. Independent spot-check status must be stated separately from the assigned runner's result. This scribe does not grant promotion.

Reject these readings: "the diagnosis is the repair" (a reproduced defect is evidence *about* the defect); "the design document closes the hazard" (a design is not a landed tool byte); "the cold re-run proves the fix" (it re-measures the same unpatched bytes); "the repair landed, so the claim is met" (the landed bytes still exit 1 on the `orphan-d4.yml` input-class control); "the selftest is 19/19, so the input-class branches are covered" (the controls are built on the D2 fixture and never reach L1's unguarded read on the generalized family); "the r4 revision is filed, so the prose is corrected" (filed is not wired; the default still resolves to r2); "the argot gate exists and is green, so claim D is delivered" (it is green on its fixture and vacuous on D4, and the typed gate does not call it); "`derived_pairs=0` with exit 0 is a pass" (zero pairs over six register-scoped records is the F-5 vacuous case the round's own delta names); "the index passes C31–C34, so it is correct" (it passes at one digest, and it passed differently at three earlier digests inside the same window; its own `round-25.md` row is stale by construction); "two tools agreeing makes the format class a fact" (they agree at one revision, and they disagreed at another); "a named delta satisfies the D claim" (the claim's text is a conjunction); "Q-04-1 is delivered because the index says so" (the index is a pointer, and it was written before the tree carried the leg); "a runner exists, so the round has a receipt" (the file appeared at 17:37:14Z; no `validation.json` existed, and it refuses to grade from the lane root); "exit zero anywhere makes every historical refusal green"; or "new evidence rewrites a filed round-22/round-23 verdict."

## Status at the closing stamp

The claims file remains `declared-before-dispatch`. `reports/round-25/run-validation.py` appeared at 17:37:14Z (14:37 local, `59425 B`), but **no `reports/round-25/validation.json` receipt existed** at any stamp through 17:37:36Z, and the runner refuses to grade from the lane root — invoked directly it exits **2** with `could-not-evaluate: run round validators only in an isolated Git clone under the lane's .scratch`, which is the receipt-guard discipline working as declared. This scribe did not run it in a clone (a writer seat's job, not the gate-keeper's). With no receipt, this lesson sets the acceptance boundary and records measurements; **O, D, and C are pending here**, not independently passed. The parent and the assigned runner own the final verdict.

## Dated observations — scoped evidence, not round acceptance

### The worktree was not clean, and round-25 evidence moved under the survey

At **2026-10-18T17:36:38Z**, `git status --porcelain` listed 9 paths, all round-25 in-flight evidence. Within the twelve-minute window `reports/round-25/` grew from `{claims.json, targets.json}` (17:24:51Z) to more than 40 files (17:37:18Z), including the runner, the integration drafts, the argot gate, and the C index. Three artifacts changed behaviour under this seat's reads: `corpus/lessons/README.md` (three digests), `reports/round-25/lessons/lessons-index-census.py` (format classification), and `tools/gates/typed-pipeline-gate.py` (≥5 digests; the O repair landed at ~17:31Z and the file briefly carried a `KeyError: 'owed_slot_of'` selftest failure at digest `a6e8d9c8…` before settling). Every reading in this survey is bound to the digest or command named beside it. **A later reading supersedes nothing here**: re-read the bytes at their final revision before admission.

### The O hazards reproduce on the pinned tool, not a drifted working copy

At the pre-repair stamp the gate bytes were `sha256 04ad4bb479562c41…`, which the sibling `gate-input/diagnosis.md` §1 identifies as the `d4-repin` MANIFEST pin (`tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` row 4). The false red was therefore a defect on the **pinned** tool rather than an artifact of a modified working copy — which is why the frozen replay rows carried the same behaviour, and why the repair requires a **pin cascade** as new rows rather than a silent edit. The serializer at `tools/assemble-d2.py` measured `sha256 8ea6bdde9514ee96…` and the naming gate `sha256 d9e4e8f4f93a21b3…`, both unchanged across this seat's reads; the settled gate measured `879d40bf977eef65…`.

### This seat's own write moves the C claim's checker, and the round must disposition it

Writing this file has a **measured consequence** on the C claim, and recording it is part of the handoff rather than a footnote. The C checker enumerates `corpus/lessons/*.md` and compares that set against the README's rows. Immediately after this file landed (2026-10-18T17:31:23Z, `sha256 da8674123e5dfbc7…`, 137 lines) the same command that reported `findings: 0` at 17:30:03Z reported:

```
formats: {'gate-keeper': 14, 'fragment-index': 5, 'plain': 6}
  FAIL C31_index_rows_eq_files      FAIL C34b_prose_arithmetic
  C31-1 unindexed-file: ['round-25.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [24, 24], 'measured': [24, 25]}}
```

The gate-keeper count moved 13 → 14 because this file carries a `## Gate` block, and the file set moved 24 → 25 because this file exists. **This is not a defect in the C seat's index**: the index was scoped to the round files that existed when it was written, and this scribe's file is a round-25 artifact landing after it. But the claim's own `after_required` says "per-round row … for every round file 1-24" and "counting command reproduces the file count", so the README as filed no longer reproduces its count, and its format histogram understates gate-keeper by one. The C seat then closed most of the gap: by 17:37:18Z the README carried a `:94` row for `round-25.md`, which cleared `C31-1`/`C34-2` and turned the finding into `C34-1` pin-drift instead — the row's pin was taken from this file at 150 lines / 26 897 B while the file was still being written (see the C section's third observation). The parent must therefore re-measure that row once this lesson's bytes are final (the README is the C seat's artifact, not this seat's — this scribe does not edit it), or carry the `C34-1` finding as a **known, named delta** rather than a pass. Leaving the red unremarked would be the silent-staleness failure the C claim exists to prevent. Note the shape: the checker is correct at every stamp, the index was correct for the tree it measured, and the claim's threshold was written as a standing equality that a later legitimate write must break — which is why the counting command, not the prose count, is the durable half of the requirement.

### No file was changed by this seat outside this lesson

This survey executed read-only commands and, where a control required capturing a produced artifact, wrote only under `.scratch/x38/` (gitignored) with `TMPDIR=$PWD/.scratch` exported: `capture-rebuild.py` + `captured-packet.d2.{yml,typed.yml}` (the gate's own L2 rebuild, captured by spying on `gate_bundle`), `poll.sh`/`poll.log` (the 60-second availability poll), `evidence.sh`/`evidence.out`, and `final.sh`/`final.out`. The only repo-tracked file this seat wrote is `corpus/lessons/round-25.md` itself. No validator was executed against a filed receipt; no round-25 tool was edited; no git mutation was made. The rebuild capture is a **produced artifact, not a filed byte** — it is evidence about the gate's behaviour and is not proposed as a repair.
