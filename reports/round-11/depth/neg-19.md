# R11-D19 — negative: a hold laundered as clean via `compare_only` (attempt + refusal receipts, validator and wired flow)

- seat: **R11-D19** (negative example targeting the wiring, claim D — `d2-typed-pipeline`), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D19 (negative): attempt to launder a hold as clean via compare_only; wiring must refuse; reports/round-11/depth/neg-19.md."
- writes: this file only. Probes, outputs and receipts live under `.scratch/neg-19/` (gitignored; `export TMPDIR=$PWD/.scratch` before every scratch-writing command, `/tmp` unused). No commit, no push; `reports/round-{8,9,10}/**` and every `tools/gates/frozen/**`, `tools/gates/expected/**` byte untouched by this seat.
- canon: NON-CANON test evidence. Nothing here is a culture design, a canon record, a handoff or a real-world claim.
- measurement revision: `e3ef171` (round-11 claims commit; the same baseline `reports/round-11/depth/review-22.md` §2 records). Artefacts under test re-hashed by this seat 2026-10-17T22:01-22:26Z (all hashes sha256):

| artefact | location at receipt | sha256 |
|---|---|---|
| projector | `tools/d2-typed-labels.py` (repo) | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| assembler | `tools/assemble-d2.py` (repo, unchanged all round) | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| live packet | `examples/culture-d2/packet.d2.yml` (repo) | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| D03 typed-wiring adapter | `.scratch/D03/final/repo/tools/assemble-d2-typed.py` (D03 shard; not integrated into `tools/` — the integration landed as the flow below) — same hash in five peer isolations (`.scratch/r11d14/iso-typed{,-2}`, `.scratch/d22/wire{,-2}`) | `95ac9d05ff880234e4fafa33de3cac09db2fee248c760c61fa2dda7631318215` |
| **integrated typed-gate flow** (R11-D05; landed in the repo mid-round, receipted 22:28-22:36Z) | `tools/typed-gate-flow.py` (repo) | `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` |
| derived typed packet + expected set (integrated) | `examples/culture-d2/packet.d2.typed.yml` / `examples/culture-d2/typed-gate.expected.json` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` / `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` |
| projector re-emit (integrator, in-flight) | `examples/culture-d2/typed-labels.d2.yml` (working tree, `M`) | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |
| naming gate used for the contrast | `tools/gates/naming-collision-gate.py` (repo) | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |

Line numbers cited below were read from the working tree on 2026-10-17 (the round-8 design spec's own pointer to the gate's skip at `:1097-1098` has drifted with the gate's later edits; the skip sites verified now are `:1045`, `:1090-1091`, `:1121`, `:1154`).

## 1. The laundering attempt

**Target.** Make a *held* typed label read clean by setting `compare_only: true` on it. The hold in question is D2's owed-form hold: a `translated-label` whose `label_id` has no supplied native/borrowed form (`D2L-FORM-UNRESOLVED`, spec §1.3 R3/R5, `reports/round-8/depth/design-spec.md:159-169`), and the wired flow's own per-row hold (adapter line 181 hard-codes `hold: "D2L-FORM-UNRESOLVED"` on the routing row).

**Why the attempt has a cover story.** `compare_only` is a *declared, licensed* key elsewhere in this lane: the naming gate declares it ("mechanism-fixture record: key-equivalence checks only", `tools/gates/naming-collision-gate.py:93`) and skips such records in its spoken-form collision layer (`:1045`), NAME-NEAR (`:1090-1091`), NAME-LEXEME (`:1121`) and the phonotactics gate (`:1154`). A launderer argues: "this label is a comparison-only fixture; that gate exempts those; so the owed-form hold should not stand." §3.5 receipts the licensed skip live — so the refusal below is a real policy distinction, not a mechanism that never existed.

**Why the wiring must refuse.** Design spec R3 (`reports/round-8/depth/design-spec.md:160-169`): `compare_only` "is therefore **not** a licensed exemption channel for typed labels; a record setting it while unresolved is `D2L-SCOPE` (misuse), not a pass". Anchor in the lane's own assembly record (`examples/culture-d2/ASSEMBLY.md:94`, verified): the unresolved LEX-GAR slots "are not silently filled or bypassed with `compare_only`". Parser negative case 19 / control C12 (`reports/round-8/depth/shard-parser.md:945`, `:973`); skill-table row (`reports/round-8/depth/skill-table-draft.md:233`).

**What counts as laundering (the outcome this negative forbids).** Any of: the `D2L-FORM-UNRESOLVED` hold disappearing for the flagged label; the row's `hold` field emptied; the label or run reading clean/0; the flag being accepted as an explanation ("comparison-only, not a claim" ⇒ no misuse finding and no hold).

## 2. Fixtures

Both package fixtures are the live packet with one block appended at root (strict-loader subset), so every finding other than the probe's is the live packet's own. The two differ by exactly one inserted line: `compare_only: true`.

Appended block (control twin, `.scratch/neg-19/packet-neg19-control.d2.yml`):

```yaml
typed_labels:
  -
    id: LBL-NEG19-01
    owner: 11-costumes
    label_id: LEX-GAR-99
    kind: translated-label
    text: "winter valley coat"
    script: Latn
    representation: english-gloss
    status: to-verify
    era_ids: [E0]
    evidence: "to-verify"
    issues:
      -
        field: scheme
        reason: "english-gloss needs no romanization scheme"
```

Laundered twin (`packet-neg19-compare-only.d2.yml`) inserts `    compare_only: true` after `    evidence: "to-verify"`. Byte delta (`diff`, verbatim): `3357a3358` / `>     compare_only: true` — one line, nothing else.

| package fixture | path (all under `.scratch/neg-19/`) | sha256 | bytes |
|---|---|---|---|
| live packet (positive control) | `examples/culture-d2/packet.d2.yml` (repo) | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | — |
| control twin (hold, no flag) | `packet-neg19-control.d2.yml` | `36423509bc5b5e3c13a4424b01a09a1d7d0b7c86eb5ff1747677cc38be303c6a` | 156436 |
| laundered (hold + flag) | `packet-neg19-compare-only.d2.yml` | `8448f1061c58bd865068e12d1abaeb6efc6f240dcdcbef8ea11b6207beda73f0` | 156459 |

Wired-flow isolations: `.scratch/neg-19/wired/` (lib layout copied: the D03 adapter, `tools/assemble-d2.py`, `tools/d2-typed-labels.py`, `tools/gates/costume-era-consistency-gate.py`, `examples/culture-d2/{packet,typed-labels,components}`) and `.scratch/neg-19/wired2/` (the integrated flow `tools/typed-gate-flow.py` + the gate scripts/fixtures + `examples/culture-d2/{packet,packet.d2.typed,typed-gate.expected,typed-labels,components}`). Nothing in the repo tree was written by the wired runs (the integrated flow's control run used its read-only default mode).

## 3. Refusal receipts — validator layer (projector, the surface the wiring carries findings from)

### 3.1 Positive control — the live packet (exit 1, never clean, never 2)

```sh
python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml            # exit 1, 16 FINDING lines
python3 tools/d2-typed-labels.py --json --packet examples/culture-d2/packet.d2.yml    # exit 1
```

`--json` receipt (`.scratch/neg-19/live.json`): `exit_code: 1`, `ok: false`, stats `{'fail': 0, 'hold': 15, 'labels': 58, 'note': 1}`; findings: `D2L-FORM-UNRESOLVED` ×10 (hold; the ten GAR labels `GAR-01..GAR-10`), `D2L-NATIVE` ×2 (hold; L-15/L-16 acute-vowel reclassification), `D2L-RANK` ×4 (3 hold, 1 note).

### 3.2 Control twin — the owed-form hold fires, alone

```sh
python3 tools/d2-typed-labels.py --packet .scratch/neg-19/packet-neg19-control.d2.yml   # exit 1, 17 FINDING lines
```

Load-bearing line (stdout, verbatim):

```text
FINDING D2L-FORM-UNRESOLVED: [hold] LBL-NEG19-01 — label_id LEX-GAR-99 has no supplied native/borrowed form
```

### 3.3 Laundered twin — the refusal

```sh
python3 tools/d2-typed-labels.py --packet .scratch/neg-19/packet-neg19-compare-only.d2.yml          # exit 1, 18 FINDING lines
python3 tools/d2-typed-labels.py --json --packet .scratch/neg-19/packet-neg19-compare-only.d2.yml   # exit 1
```

Findings on the laundered label (from `.scratch/neg-19/run-neg19.json`, verbatim):

```json
{"code": "D2L-FORM-UNRESOLVED", "detail": "label_id LEX-GAR-99 has no supplied native/borrowed form", "id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "LBL-NEG19-01"}
{"code": "D2L-SCOPE", "detail": "compare_only is not a licensed exemption for typed labels", "id": "D2L-SCOPE", "severity": "fail", "where": "LBL-NEG19-01"}
```

`--json` document: `exit_code: 1`, `ok: false`, stats `{'fail': 1, 'hold': 16, 'labels': 59, 'note': 1}`.

Full output delta between control and laundered (`diff`, verbatim):

```text
18c18,19
< coverage: conflicts=4, findings_hold_or_fail=16, findings_total=17, label_findings_fail=2, label_findings_hold=11, labels_by_kind={'borrowed-strata': 2, 'native-form': 46, 'translated-label': 11}, rank_quarantine_handles=3, rank_rules_component=21, rank_rules_gate_projected=5, rank_rules_normalized=9, rank_rules_unresolved_items=13, reconciliation_records=10, typed_labels=59
---
> FINDING D2L-SCOPE: [fail] LBL-NEG19-01 — compare_only is not a licensed exemption for typed labels
> coverage: conflicts=4, findings_hold_or_fail=17, findings_total=18, label_findings_fail=3, label_findings_hold=11, labels_by_kind={'borrowed-strata': 2, 'native-form': 46, 'translated-label': 11}, rank_quarantine_handles=3, rank_rules_component=21, rank_rules_gate_projected=5, rank_rules_normalized=9, rank_rules_unresolved_items=13, reconciliation_records=10, typed_labels=59
```

The laundering flag bought nothing and cost a fail: the hold count is unchanged (`label_findings_hold=11` both ways — 10 GAR + the probe's), the laundered label still carries its hold, and the flag itself is receipted as `D2L-SCOPE [fail]`. Exit 1 on all three runs; never 0.

### 3.4 Variant — the flag on the source costume record is inert

Setting `compare_only: true` on the packet's costume record itself (which `project_labels` → `_costume_label` rebuilds field-by-field) changes nothing; the key never reaches a projected label. In-memory probe over the live packet (no file written):

```text
base label carries compare_only: False
mutated label carries compare_only: False            # GAR-01 with entry['compare_only']=True
base exit/stats: 2 {'fail': 2, 'hold': 10, 'labels': 58}     # parse_typed_labels-level
mut  exit/stats: 2 {'fail': 2, 'hold': 10, 'labels': 58}
finding sets identical (source-record flag inert): True
```

### 3.5 The licensed channel it tries to borrow — receipted live in another gate

Naming gate over its own fixture (`tools/gates/fixtures/naming-collision-gate.yml`) plus one appended costume record `{id: G-NEG19, garment: "vata coat", ...}`:

```sh
python3 tools/gates/naming-collision-gate.py .scratch/neg-19/naming-neg19-base.yml          # exit 1, 13 finding lines
python3 tools/gates/naming-collision-gate.py .scratch/neg-19/naming-neg19-compare-only.yml  # exit 1, 12 finding lines
```

Base run, verbatim: `FINDING PHON-INVENTORY: FAIL — name G-NEG19 'vata coat': symbol /v/ at position 1 is not in the declared inventory…`. With `compare_only: true` on that record the finding disappears (13→12 lines). The licensed skip is real **there**, for that gate's mechanism-fixture records; the D2 typed-label flow refuses it **here** (§3.3, §4.3). Same key, two policies; the wiring keeps the D2 side closed.

### 3.6 Coverage note — the integrated selftest still does not pin this refusal

`grep -n compare_only tools/d2-typed-labels.py` → 2 hits, both inside the refusal (`:787`, `:789`). The integrated selftest is green while the control is absent: `python3 tools/d2-typed-labels.py --selftest` → `selftest: 39/39 checks passed` (exit 0); the string does not occur in its output. Round-8 shard-parser §5 case 19/C12 asked for this control to be lifted into `--selftest` (`reports/round-8/depth/shard-parser.md:945`, `:973`); it still is not. §3.3/§4 below are the receipts the wiring's test shards can lift.

## 4. Refusal receipts — the round-11 wired flow (D03 adapter and the integrated flow)

Two wired artefacts were receipted. **A — the D03 adapter** `assemble-d2-typed.py` (`95ac9d05…`, §4.1-§4.5; not the artefact that landed in `tools/`). **B — the integrated flow** `tools/typed-gate-flow.py` (`5758e315…`, R11-D05, which landed in the repo while this report was being written, §4.6). Adapter A pins the packet to `assemble-d2.py`'s deterministic assembly, pins the projection to byte-for-byte reproduction by `tools/d2-typed-labels.py`, routes every off-channel label into `typed_channel` rows carrying `hold: "D2L-FORM-UNRESOLVED"`, and carries the projector's findings verbatim. Flow B derives the typed gate packet by marking each `translated-label` record `compare_only: true` **as its mechanism** (its own docstring: "the gate's own declared 'key-equivalence checks only' channel"), and its checks are: typed-packet pin, untyped-records, sound-channel-clean, differential-exact (legacy vs typed, removals exactly the off-records), owed-slots-crosscheck, hold-set-equal to the committed expected set, pins, delta, verdicts, expected-file-current. Runs for A are inside `.scratch/neg-19/wired/`, for B inside `.scratch/neg-19/wired2/`; `TMPDIR` set.

### 4.1 W0 — control over the un-laundered tree: green, holds carried as named rows

```sh
python3 tools/assemble-d2.py --check                                                  # exit 0: byte-identical deterministic assembly
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml       # exit 1 (findings present, report complete)
python3 tools/assemble-d2-typed.py --emit examples/culture-d2/packet.typed.d2.yml     # exit 0
# "Wrote … (163521 bytes, 10 routing rows, 16 findings carried)"
```

GAR-01's routing row in the typed packet (verbatim):

```yaml
    record: "GAR-01"
    kind: "translated-label"
    label_id: "LEX-GAR-01"
    owner: "11-costumes"
    source_field: "garment"
    off_channel_field: "garment_gloss"
    channel: "off-sound-and-identity"
    hold: "D2L-FORM-UNRESOLVED"
```

All ten GAR rows present (`GAR-01..GAR-10`), `typed_channel_rows: 10`, `D2L-FORM-UNRESOLVED` occurs 30× in the artifact (10 rows + 10 carried findings ×2 fields). Typed packet sha256 `bb480e34881c87814f953560ab769aa8705316be64fead67abe1b454bc0ec3b3`.

### 4.2 W2 — source-record injection (`compare_only` on GAR-01 in `11-costumes.yml`): inert, hold intact

Edited the isolation copy of `components/11-costumes.yml` (`compare_only: true` added to GAR-01; file sha `04d3a7a3ba3e0f81eb33ca0376d5aeadb9972f6188e3e3e5b150d3769f561e92`), then re-assembled and re-emitted (the pins require it):

```sh
python3 tools/assemble-d2.py                                                        # exit 0, packet rewritten (156094 bytes)
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml     # exit 1, written
python3 tools/assemble-d2-typed.py --emit examples/culture-d2/packet.typed-w2.d2.yml  # exit 0
# "Wrote … (163544 bytes, 10 routing rows, 16 findings carried)"
```

Verification over the wired output: GAR-01's row unchanged — `hold: "D2L-FORM-UNRESOLVED"`, `channel: "off-sound-and-identity"`; `D2L-SCOPE` occurrences **0**; the projector's GAR-01 hold finding carried verbatim; the typed record still carries `compare_only: true` as an inert unknown key (the adapter does not strip unknown source fields — observation, see §6). Laundering outcome: **refused by inertness** — the flag had no path to the typed-label schema (same code path as §3.4), so the hold is neither removed nor re-labelled.

### 4.3 W3 — packet-bytes injection (the `compare_only` typed label appended to the packet): refused twice

```sh
python3 tools/assemble-d2-typed.py --packet examples/culture-d2/packet.launder.d2.yml   # exit 2
```

stderr, verbatim:

```text
typed-assembly error: examples/culture-d2/packet.launder.d2.yml is not assemble-d2.py's deterministic assembly (156459 bytes vs 156071); re-run tools/assemble-d2.py before wiring
```

The projector over the same laundered bytes (the semantic layer the adapter carries findings from) refuses as in §3.3, verbatim:

```text
FINDING D2L-FORM-UNRESOLVED: [hold] LBL-NEG19-01 — label_id LEX-GAR-99 has no supplied native/borrowed form
FINDING D2L-SCOPE: [fail] LBL-NEG19-01 — compare_only is not a licensed exemption for typed labels
```

### 4.4 W4 — projection-file injection (the flag hand-added to the projection JSON): refused

```sh
python3 tools/assemble-d2-typed.py --projection examples/culture-d2/typed-labels.tampered.d2.yml   # exit 2
```

stderr, verbatim:

```text
typed-assembly error: projection examples/culture-d2/typed-labels.tampered.d2.yml is not reproduced byte-for-byte by tools/d2-typed-labels.py over …/packet.d2.yml; hand-edited or drifted
```

### 4.5 Route table — every injection point and its refusal

| injection route | attempt | refusal | receipt |
|---|---|---|---|
| explicit `typed_labels` entry in a packet the flow reads | `compare_only: true` on the held label | `D2L-SCOPE` fail + hold stands (`D2L-FORM-UNRESOLVED`); exit 1 | §3.3 |
| packet bytes fed to the wired adapter | same append | exit 2, assembler-identity pin; semantics = §3.3 | §4.3 |
| projection JSON fed to the wired adapter | flag hand-added to a label | exit 2, reproduction pin ("hand-edited or drifted") | §4.4 |
| source costume record (component → assembled packet) | flag on GAR-01 | inert: row hold and carried finding unchanged; `D2L-SCOPE` 0 | §4.2 |
| source lexicon/name record | same class as costume (owner rebuild in `project_labels`) | inert by the same code path | §3.4 |
| packet fed to the integrated flow (explicit label + flag) | hold-laundering via the explicit channel | exit 1: `expected-pins`, `typed-packet-pinned`, `hold-set-equal` (18≠16), `owed-slots-crosscheck`, `expected-file-current` fail; never clean | §4.6 I2 |
| source record flagged, the flow's own `compare_only` mechanism imitated on the legacy side | make the legacy channel skip the sound test too | exit 1: `differential-exact — removed 9, off-records 10` + pins fail; `hold-set-equal` still passes (hold intact) | §4.6 I1 |

### 4.6 B — the integrated flow (`tools/typed-gate-flow.py`, R11-D05): receipts

**Control (shipped state, read-only run in the repo tree):**

```sh
python3 tools/typed-gate-flow.py --json      # exit 0
```

All 10 checks ok; 16 findings: `D2L-FORM-UNRESOLVED` ×10 (hold; the ten owed slots named from the component's `form_slot` declarations), `D2L-RANK` ×3 hold + ×1 note, `D2L-NATIVE` ×2 hold (L-15/L-16). The flow's mechanism is itself `compare_only`: the derived typed packet marks each `translated-label` record `compare_only: true` so the gate skips it on the sound channel, while the differential check (`differential-exact — removed 10, off-records 10`) requires the **legacy** channel to keep all ten `PHON-INVENTORY` failures — the exemptions are declaration-bound, and the hold set (`hold-set-equal`, 16 == 16) is the committed expected set.

**I2 — the explicit held label with the flag appended to the packet** (isolated copy `.scratch/neg-19/wired2/`):

```sh
python3 tools/typed-gate-flow.py --json      # exit 1
```

Failed checks (verbatim ids/details): `typed-packet-pinned`; `owed-slots-crosscheck` (an owed slot `LEX-GAR-99` the component never declares); `hold-set-equal — observed 18 findings, expected 16`; `expected-pins — pin mismatch: packet e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643/8448f1061c58bd865068e12d1abaeb6efc6f240dcdcbef8ea11b6207beda73f0`; `expected-file-current`. The attempt adds findings (the hold + the scope fail) instead of removing them; the run is refused, never clean.

**I1 — the flag on the source costume record** (isolated copy; component edited, `assemble-d2.py` re-run exit 0, packet 156094 bytes):

```sh
python3 tools/typed-gate-flow.py --json      # exit 1
```

Failed checks (verbatim): `differential-exact — removed 9, off-records 10` — the *legacy* channel lost GAR-01's phonology failure, exactly the drop the differential exists to catch; `typed-packet-pinned`; `expected-pins — pin mismatch: packet e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643/260d209d86379aea08bb73f209840b205de29ea2f202a390ed52a3c67c3160cf`; `expected-delta-match`; `expected-file-current`. Passing checks include `hold-set-equal` (observed 16 == expected 16) and `owed-slots-crosscheck`: **the hold was not laundered** — the flag bought no exemption; it only broke the differential and the pins, and the flow refused (exit 1).

## 5. What the wiring must keep (the predicate for this negative)

A wired end-to-end run over any laundered input must satisfy all of:

1. the flagged label's `D2L-FORM-UNRESOLVED` hold present — in the routed row (`hold` field) and in the carried findings;
2. `D2L-SCOPE` fail with the message "compare_only is not a licensed exemption for typed labels" **if** the flag ever reaches a typed label record (the wired packet/projection pins make that reachable only through a future assembler change — the validator backstop must stay);
3. non-zero verdict for inputs that violate a pin (exit 2) or carry findings (exit 1); never a clean 0;
4. removing the flag returns the run to the control's finding set exactly (§3.2 vs §3.3);
5. the `typed_channel` coverage check keeps refusing any label the projector typed off-channel but the routing does not carry (adapter `routing_rows`, exercised by its own selftest).

## 6. Status, observations, to-verify

- **Wiring integrated mid-round (22:28-22:36Z).** The integration landed as `tools/typed-gate-flow.py` (`5758e315…`, R11-D05) plus `examples/culture-d2/packet.d2.typed.yml` (`e8a83445…`), `examples/culture-d2/typed-gate.expected.json` (`7ed59731…`) and `reports/round-11/run-validation.py` (`12824903…`, untracked at check time). The D03 adapter (`assemble-d2-typed.py`) was superseded by it; §4.1–§4.5 receipts against the D03 adapter stay valid for that artefact, and §4.6 receipts the integrated flow (including the negative both ways: I1/I2 refused, exit 1). The flow's own `--selftest` was not run by this seat (out of the negative's scope; the D10/D14/D24 shards exercise it), and the D-claim counting command `reports/round-11/run-validation.py` was **not** run by this seat (it writes shared bookkeeping; the integrator's run is the counting receipt) — **to-verify** there: whether the validation run carries this negative's I1/I2 as controls.
- **Observation (not a laundering; relevant to the integrated flow's mechanism).** `compare_only` is now load-bearing in the wiring itself: flow B marks translated-label records with it so the gate skips them (`typed-gate-flow.py` line 167, docstring lines 8-9). That makes it the single most attractive key to smuggle — I1 receipts that its use on the legacy/source side is caught by `differential-exact` (which exists precisely to keep the legacy channel un-laundered), and I2 that it can never carry a hold away (`hold-set-equal`, `owed-slots-crosscheck`). Any future flow change that derives the compare_only marking from the packet rather than the projection would move this negative's ground: keep the marking derivation projection-only.
- **Observation (adapter hygiene).** Adapter A does not strip unknown keys from source records: after §4.2 the typed packet carries `compare_only: true` on the GAR-01 costume record. It is inert in every checked path (the typed packet's costume form field is now `garment_gloss`; the projector never copies the key), but a downstream consumer that ever reads `compare_only` off a typed-packet record would treat it as that consumer's own licensed skip — the naming gate does exactly this (`tools/gates/naming-collision-gate.py:1154`). Strip-or-police is a wiring choice; recorded here, not absorbed.
- **Coverage gap.** §3.6: the refusal is not pinned by any selftest in the repo; the round-8 request to lift case 19/C12 is still open. §3.3's receipt is the liftable case (positive control §3.2 guards the hold side).

## 7. Limits

- Non-canon engineering evidence; admits no round, capability or canon fact.
- Probes are synthetic (one appended label / one appended field); no component, packet, baseline or frozen byte in the repo was modified — the edited component lives only in the isolation copies, and `git status` shows no diff for `examples/culture-d2/components/11-costumes.yml`.
- Checker artefacts read-only: `--check`/frozen replay outside this seat's scope; the wired runs were confined to `.scratch/neg-19/wired/` and `.scratch/neg-19/wired2/` (the integrated flow's control run was the read-only default mode against the repo tree).
- The `D2L-NATIVE` L-15/L-16 holds and `D2L-RANK` findings in the positive control are the live packet's standing state, not probe artifacts.
