- Seat: D06 | executor | claim D (depth) | date 2026-10-19 | baseline da68a6d

# D06 — twin.json shape parity + expected.json content for `reports/round-34/handoff/declared-in-r7/`

Mission (targets.json, seat D06): "Twin + expected.json design: the twin.json shape
parity checks and the expected.json content (packet_sha256 placeholder, links
expectations, uncertainty expectations) mirroring declared-in-r6's expected.json
structure." Out path: `reports/round-34/depth/D06-twin-expected.md`.

The r7 pair must be a **shape-identical, value-current** successor of
`reports/round-30/handoff/declared-in-r6/`: same 7-key `twin.json`, same 26-key
`expected.json`, same 58-entry read set — with the five stale prose surfaces of §C
swapped to live numbers and every hash re-measured. The parity suite defined in §A
(31 assertions) was run today against the r6 pair and is **31/31 green**, so it is
calibrated before it is pointed at r7.

Everything below was measured at `da68a6d` by read-only means: no round runner was
executed, no filed byte was written.

## A. `twin.json` contract and parity suite

### A.1 Where the twin comes from

- Built by `v3_build_twin` — `tools/exercise-handoff-e2e.py:2621-2671`; called at `:3602-3605`.
- Serialized at `:3606` as `json.dumps(twin, indent=1, sort_keys=True, ensure_ascii=False) + "\n"`;
  `twin_sha256` is the sha256 of exactly that text (`:3607`).
- It is a **projection of the delivered Markdown**: `claim_ledger` and `coupling_edges`
  come from the parsed packet tables (`:2644-2670`), so the byte the gate sees and the
  byte the harness judges are the same byte (`:2621-2627`).
- Judged by `tools/harness/packet_uncertainty.py --require-oq` and
  `tools/harness/packet_links.py` (`:3725-3760`).

### A.2 Shape (r6, and required of r7)

| key | type / size | source | r7 expectation |
|---|---|---|---|
| `packet_id` | str | `V3_PACKET_ID` (`:1931`) | `kotodama.handoff.d2d3d4-e2e` |
| `packet_version` | str | `V3_PACKET_VERSION` (`:1932`) | `3.1.1` (bump only if the renderer's version constant is bumped) |
| `profile` | str | `V3_PROFILE` (`:1930`) | `kotodama-handoff-e2e/3` |
| `artifact_manifest` | list, 58 | `V3_READ_SET` order (`:2628-2639`), ids `A-{n:02d}` by `enumerate(..., start=1)` (`:3603`) | 58 rows, identical order |
| `claim_ledger` | list, 27 | `parse_ledger(packet)` rows (`:2644-2654`) | 27 rows; row set pinned at `:2605-2606` (15 v2 + 12 D4) |
| `open_questions` | list, 10 | renderer list: v2 rows + `OQ-V3-04..06` (`:3508-3541`) | 10 rows (`OQ-V2-01..07`, `OQ-V3-04..06`) |
| `coupling_edges` | list, 88 | `parse_edges(packet)` rows (`:2657-2670`) | 88 rows = 34 v2 + 54 `D4E-` |

Row-level shapes: ledger rows carry exactly
`{claim_id, claim_kind, evidence_status, uncertainty{status, basis}, links, statement}`;
edge rows exactly `{edge_id, source, relation, target_ids, claims, applicability,
mechanism, limits, declared_in}`; `record_ids` appears on exactly four manifest rows
(the D2 packet, the D3 packet, the reconciliation, the D4 packet — `:2631-2638`);
`unresolved_claims: "—"` is the "none" token (`:3521`).

### A.3 The 31 parity checks (P1–P16)

| # | assertion |
|---|---|
| P1 | `sha256(packet.md)` == `expected.packet_sha256` == the `packet_sha256:` line in `freeze.txt` |
| P2 | re-serializing the landed `twin.json` with the renderer rule reproduces the file byte-for-byte and its sha256 == `expected.twin_sha256` == the `twin_sha256:` line |
| P3 | twin top-level key set is exactly the seven above (no extras, no omissions) |
| P4 | manifest rows == `V3_READ_SET` order with `A-NN` ids; P4b each `sha256` == `expected.inputs[path]`; P4c manifest paths == `inputs` keys |
| P5 | `record_ids` only on the four named rows |
| P6 | ledger ids in order == `expected.claim_ids`; P6b row shape + non-empty links; P6c census == `expected.uncertainty.statuses` |
| P7 | open-question ids == `OQ-V2-01..07` + `OQ-V3-04..06`; P7b every `unresolved` claim is referenced by an OQ row (the `--require-oq` contract) |
| P8 | 88 edges = 34 v2 + 54 `D4E-`; P8b the 34 v2 rows are byte-equal to the filed `reports/round-15/handoff/packet-v2-05.yml` rows (`:3680-3691`); P8c edge `claims` ⊆ ledger ids; P8d edge row shape |
| P9 | Σ ledger `links` == `expected.links.links` == `resolved` == 105, `findings` == 0 |
| P10 | ledger row count == `expected.uncertainty.claims` == 27, `findings` == `require_oq_findings` == 0 |
| P11 | contract digest recomputed from `inputs`; 26/26 component digests and 8/8 D4 pins matched; `gate_scan` == `expected_scan` == `V3_DECLARED` (`:1960-1967`, enforced at `:3797-3802`); constants equal the twin's three constants; glossary ids `L01..L20` |
| P12 | `baseline_digest` == `v3_baseline_digest(expected)` (`:3763-3768`) |
| P13 | `field_digests` keys == `FIELD_NAMES` (16) == the fields extracted from `packet.md`; P13b each digest equals sha256 of the delivered field value |
| P14 | `twin.claim_ledger` re-derived from `packet.md` via `parse_ledger` + the `:2644-2654` mapping is row-for-row equal; P14b same for `coupling_edges` via `parse_edges` |
| P15 | every twin open-question row is the exact packet bullet `- {id}: {question}`, plus ` (unresolved claims: {tok})` unless `tok` is the `—` none-token |
| P16 | `freeze.txt` records the same measured values as `expected.json` (hashes, date/author, census, read set, component pins, D4 pins) |

### A.4 Witness run (r6 pair, this session)

```
$ python3 .scratch/d06/parity_check.py reports/round-30/handoff/declared-in-r6
PASS P1 packet_sha256 — measured 6ced88ad009f… exp 6ced88ad009f…
PASS P2 twin_sha256 canonical — measured 6633443d70ce…
PASS P3 twin key set — 7 keys
PASS P4 manifest order+ids — 58 rows vs read set 58
PASS P4b manifest digests == inputs — all 58 match
PASS P4c manifest paths == inputs keys
PASS P5 record_ids rows — [d2 packet, d3 packet, d4 packet, reconciliation]
PASS P6 ledger id order == expected.claim_ids — 27 rows
PASS P6b ledger row shape
PASS P6c census == expected.uncertainty.statuses — {'supported': 16, 'partial': 7, 'unresolved': 4}
PASS P7 open_question ids / P7b every unresolved claim referenced
PASS P8 edge count — 88 rows, 34 v2, 54 D4E   PASS P8b v2 rows byte-equal filed yml
PASS P8c/P8d edge claims ⊆ ledger, edge row shape
PASS P9 links expectation — 105 link tokens
PASS P10 uncertainty expectation — claims 27
PASS P11…P11f cross_refs, declared constants, constants, glossary ids
PASS P12 baseline_digest
PASS P13/P13b field_digests — 16 fields, 0 mismatches
PASS P14/P14b twin re-derived from packet.md — 27 rows / 88 rows
PASS P15 open-question text parity with packet.md — mismatches: []
PASS P16 freeze.txt == expected.json measured values

31/31 parity checks passed
```

Independent judge legs on the same twin (read-only):

```
$ python3 tools/harness/packet_uncertainty.py --packet reports/round-30/handoff/declared-in-r6/twin.json --require-oq --json
{"tool": "tools/harness/packet_uncertainty.py", "claims": 27, "findings": []}          # exit 0
$ python3 tools/harness/packet_links.py --packet reports/round-30/handoff/declared-in-r6/twin.json --repo-root . --json
{"tool": "tools/harness/packet_links.py", "links_checked": 105, "resolved": 105, "findings": []}   # exit 0
$ python3 tools/gates/handoff-packet-check.py packet.md   # isolated copy, foreign cwd
INFO scan: fields=16/16 glossary-entries=20 findings=0                                  # exit 0
```

## B. `expected.json` content

### B.1 Ground rules the r7 file must satisfy

- Written by `v3_freeze` (`:4075-4126`) with the same canonical JSON rules, five files
  written per freeze: `expected.json`, `packet.md`, `twin.json`, `run.log`, `freeze.txt`.
- `baseline_digest` is self-integrity over the payload minus itself (`:3763-3768`); the
  loader rejects any hand edit and any declared-constant drift (`:3781-3802`), so every
  edit to the packet **must** be followed by a re-freeze, never by patching `expected.json`.
- The `inputs` map is the drift detector: every read-set digest must match at exercise
  time or the run fails `input-digest` (`:3818-3823`).

### B.2 The 26 keys, by class

**Class 1 — fixed by the renderer's declared block** (`:1960-1975`, enforced `:3797-3802`):
`profile`, `packet_id`, `packet_version`, `expected_exit`=0, `expected_finding_ids`=[],
`expected_scan`={fields `16/16`, glossary_entries 20, findings 0},
`expected_uncertainty_findings`=0, `expected_links_findings`=0,
`expected_links_unresolved`=0, `declared_expectation`, `limits`, `frozen_by`.

**Class 2 — pre-determined at HEAD (all measured this session, all equal to r6's)**:

| key | r7 value | evidence |
|---|---|---|
| `inputs` | **byte-equal to r6's 58-entry map** | every read-set file re-hashed at `da68a6d`: 58 present, 0 missing, **0 drifted** |
| `counts` | **byte-equal to r6's block** (20 values: claims 27, edges 88, d4_claims 12, d4_edges 54, d4_typed_labels 82, d4_holds 12, d2_typed_labels 58, d2_lexicon 40, d2_names 8, d2_coupling_notes 29, d2_to_verify_lines 21, d3_lexicon 20, d3_names 6, d3_bridges 5, d3_references 5, d4_lexicon 62, d4_symbols 8, d4_costumes 6, d4_rank_rules 4, d4_era_records 8) | re-measured from live bytes; `claims`/`edges`/`d4_*` row counts are additionally pinned by `:2605-2606` |
| `claim_ids` | 27 ids in ledger order, **equal to r6's** | `V3Assembly(root).ledger` at HEAD |
| `glossary_entry_ids` | `L01..L20` | `:3507`, `:4018` |
| `v2_subset_digest` | `ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b` — **invariant** under any D4-prose fix | `v3_subset_digest` filters to the 15 v2 ids (`:3437-3453`) |
| `cross_refs.contract_id` / `.contract_revision` / `.contract_digest` | `kotodama-lore-adjacency` / `1.0.0` / `sha256:5f4c02bf…` | contract digest recomputed from `inputs` |
| `cross_refs.component_digests_checked/matched`, `.d4_pins_checked/matched`, `.gate_exit`, `.gate_scan` | 26/26, 8/8, 0, `{16/16, 20, 0}` | `:3505-3506`; gate run on the r6 packet: exit 0 |
| `cross_refs.gate_stdout_sha256` | `7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685` — **content-independent** | sha256 of the gate's single stdout line `INFO scan: fields=16/16 glossary-entries=20 findings=0\n`, verified equal to r6's value |
| `alias_state` | `landed` | `V3_ALIAS_WITNESS_TOKENS` (`:1976-1978`) |
| `frozen_at` | `2026-10-19` | freeze date |
| `links` | `{exit 0, findings 0, links 105, resolved 105}` | conditional: holds iff the ledger link cells are untouched; otherwise re-measure |
| `uncertainty` | `{claims 27, statuses {supported 16, partial 7, unresolved 4}, exit 0, findings 0, require_oq_findings 0}` | conditional: holds iff the status column is untouched (the four unresolved ids are `CL13`, `D2-CL02`, `D4-CL09`, `D4-CL12`) |

**Class 3 — recompute at freeze (placeholders in the template)**:
`packet_sha256`, `twin_sha256`, `field_digests` (16 keys), `baseline_digest`
(and `gate_stdout_sha256`, re-measured even though it is expected to be the constant above).

### B.3 Template (r7), with placeholders

The literal body of the r7 `expected.json` before the freeze — class 2 values are filled,
class 3 values are marked. `field_digests` is the 16 `FIELD_NAMES` in gate order:
`packet_id, packet_version, contract_ref, producer, recipient, request_ref,
baseline_bible_ref, artifact_manifest, subject_refs, scope, dependency_manifest,
claim_ledger, coupling_edges, requested_decisions, validation, open_questions`.
`inputs` is r6's map verbatim (58 entries), certified equal by the command in §B.4.

```json
{
 "alias_state": "landed",
 "baseline_digest": "<RECOMPUTE-AT-FREEZE>",
 "claim_ids": ["D2-CL01","D2-CL02","CL01","CL02","CL03","CL04","CL05","CL06","CL07","CL08","CL09","CL10","CL11","CL12","CL13",
               "D4-CL01","D4-CL02","D4-CL03","D4-CL04","D4-CL05","D4-CL06","D4-CL07","D4-CL08","D4-CL09","D4-CL10","D4-CL11","D4-CL12"],
 "counts": {"claims":27,"edges":88,"d2_coupling_notes":29,"d2_lexicon":40,"d2_names":8,"d2_to_verify_lines":21,
            "d2_typed_labels":58,"d3_bridges":5,"d3_lexicon":20,"d3_names":6,"d3_references":5,"d4_claims":12,
            "d4_costumes":6,"d4_edges":54,"d4_era_records":8,"d4_holds":12,"d4_lexicon":62,"d4_rank_rules":4,
            "d4_symbols":8,"d4_typed_labels":82},
 "cross_refs": {"component_digests_checked":26,"component_digests_matched":26,
                "contract_digest":"sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069",
                "contract_id":"kotodama-lore-adjacency","contract_revision":"1.0.0",
                "d4_pins_checked":8,"d4_pins_matched":8,"gate_exit":0,
                "gate_scan":{"fields":"16/16","findings":0,"glossary_entries":20},
                "gate_stdout_sha256":"7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685"},
 "declared_expectation": "exit 0 / findings [] / uncertainty+links findings 0 with every link resolved, fixed before implementation; hashes measured from bytes, never generated from a printed verdict",
 "expected_exit": 0,
 "expected_finding_ids": [],
 "expected_links_findings": 0,
 "expected_links_unresolved": 0,
 "expected_scan": {"fields":"16/16","findings":0,"glossary_entries":20},
 "expected_uncertainty_findings": 0,
 "field_digests": {"<16 FIELD_NAMES>": "<RECOMPUTE-AT-FREEZE>"},
 "frozen_at": "2026-10-19",
 "frozen_by": "tools/exercise-handoff-e2e.py --profile v3",
 "glossary_entry_ids": ["L01","L02","…","L20"],
 "inputs": {"<58 rel→sha256 entries>": "== r6 map, byte-for-byte"},
 "limits": "pins computational inputs only; not lore acceptance, not canon, not completion of the round arc; documentation surfaces excluded",
 "links": {"exit":0,"findings":0,"links":105,"resolved":105},
 "packet_id": "kotodama.handoff.d2d3d4-e2e",
 "packet_sha256": "<RECOMPUTE-AT-FREEZE>",
 "packet_version": "3.1.1",
 "profile": "kotodama-handoff-e2e/3",
 "twin_sha256": "<RECOMPUTE-AT-FREEZE>",
 "uncertainty": {"claims":27,"exit":0,"findings":0,"require_oq_findings":0,
                 "statuses":{"partial":7,"supported":16,"unresolved":4}},
 "v2_subset_digest": "ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b"
}
```

### B.4 Certified pre-determination (run this to reproduce)

```
$ python3 - <<'EOF'
import json, hashlib, importlib.util
s=importlib.util.spec_from_file_location("e2e","tools/exercise-handoff-e2e.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
a=m.V3Assembly(m.ROOT); r6=json.load(open('reports/round-30/handoff/declared-in-r6/expected.json'))
live={rel: hashlib.sha256(open(rel,'rb').read()).hexdigest() for rel in m.V3_READ_SET}
print('inputs == r6:', live == r6['inputs'], len(live))
print('claim_ids == r6:', [r['claim_id'] for r in a.ledger] == r6['claim_ids'])
print('census:', m.v3_status_census(a.ledger), ' v2_subset == r6:', a.v2_subset_digest == r6['v2_subset_digest'])
EOF
inputs == r6: True 58
claim_ids == r6: True
census: {'supported': 16, 'partial': 7, 'unresolved': 4}  v2_subset == r6: True
```

### B.5 Predicted delta from r6 (what the freeze will move)

| key | movement |
|---|---|
| `packet_sha256`, `twin_sha256` | new (prose changed → bytes changed) |
| `field_digests.claim_ledger` | new — the four D4 rows are rewritten |
| `field_digests.open_questions` | new — `OQ-V3-05` is rewritten |
| the other 14 `field_digests` | unchanged (`validation`, `artifact_manifest`, `dependency_manifest` already carry live numbers — see §C.3) |
| `frozen_at`, `baseline_digest` | new |
| `gate_stdout_sha256` | expected unchanged (verified constant) |
| everything else | byte-stable |

## C. What the D-claim must actually move (evidence, and one contested point)

### C.1 The staleness is prose-only, not data drift

- The renderer at HEAD assembles **byte-identical** r6 bytes: `V3Assembly(root).packet_sha256`
  = `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` = r6's frozen value;
  twin = `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e`. No read-set
  file has changed (58/58 digests equal). So a plain re-freeze cannot fix anything — the
  renderer source must change.

### C.2 Exactly five stale surfaces (all in `packet.md`)

| surface | cites | live |
|---|---|---|
| `claim_ledger` `D4-CL05` (`packet.md:148`) | `typed_labels 74`, native-form 56, `findings_total 16`, `findings_hold_or_fail 15`, `labels 74` | `typed-labels.d4.yml:46` `typed_labels 82`, `:37` native-form 64, `:32` findings_total 12, `:31` findings_hold_or_fail 12 |
| `claim_ledger` `D4-CL06` (`:149`) | `hold 15, note 1, fail 0` | `expected-holds.json:47-49` `hold 12, note 0, fail 0` |
| `claim_ledger` `D4-CL07` (`:150`) | conflicts 4, quarantine handles 3 | `typed-labels.d4.yml:30` conflicts 0, `:40` rank_quarantine_handles 0 |
| `claim_ledger` `D4-CL09` (`:152`) | unresolved rank items 13, quarantine 3, conflicts 4 | `:44` 0, `:40` 0, `:30` 0 |
| `open_questions` `OQ-V3-05` (`:307`) | "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts" | hold set 12/0/0; 0/0/0 as above |

### C.3 The packet already contradicts itself

`artifact_manifest` rows `A-30` (`:68`) and `A-31` (`:69`) and the `validation` field
already carry the live numbers ("82 labels (64 native-form …), 12 findings, 0 unresolved
rank items"; "hold set 12 holds / 0 note"; "typed channel 82 labels … 12 findings (12
hold-or-fail), 0 unresolved rank items, 0 quarantine handles"). Note that the D2 numbers
that look identical to the stale D4 ones (`16 findings / 15 hold-or-fail / 13 unresolved /
3 quarantine / 4 conflicts`) are **live-true for D2** (`examples/culture-d2/typed-labels.d2.yml`
coverage block), which is how the D4 rows' copied figures went unnoticed — an audit that
greps bare integers will false-positive on the D2 rows; the audit must be path-scoped to
the D4 rows (§D.3).

### C.4 Where the stale text is pinned (contested scope — integrator/operator decision)

- The four D4 ledger rows are **parsed verbatim from filed bytes**:
  `reports/round-20/handoff/claims-map.md:99`, `:104` (CL05 figures), `:107`, `:119`,
  `:150` (CL06/07/09 figures) via `v3_parse_claims_map` (`tools/exercise-handoff-e2e.py:2290-2307`,
  called at `:3511`), which is why the packet "carries them verbatim" (`:2566`).
- `OQ-V3-05` is hardcoded in the renderer (`:3523-3532`).
- Consequence: claim D's "rewrites the claim-ledger/OQ prose to live numbers" is only
  reachable by a **renderer-side supersession** of the four filed rows (declare the live
  re-read and name the superseded r20 figures), because `reports/round-20/**` is a filed
  round byte this round may not edit. That is a shared-file change and must be drafted as
  before/after text by the owning D seat and applied by the integrator — I do not land it,
  and I record the divergence rather than absorbing it. `OQ-V3-05` is a plain renderer prose
  edit with no filed-source conflict.
- Statuses are not in dispute: keeping `D4-CL05/06/07` `supported` and `D4-CL09` `unresolved`
  keeps the census at 16/7/4, keeps `D4-CL09` referenced by `OQ-V3-05` (so `--require-oq`
  stays green) and keeps `unresolved_claims` non-empty.

## D. Recipe for the r7 pair (integrator)

1. Land the packet + the renderer edits, then freeze into the r7 dir (writer step, not a seat step):
   `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7`
   → writes `expected.json`, `packet.md`, `twin.json`, `run.log`, `freeze.txt` (`:4075-4126`),
   refusing to freeze anything that fails preflight/gate/semantics (`:3981-4005`).
2. Move the defaults (`tools/exercise-handoff-e2e.py:1933-1934`) from
   `reports/round-30/handoff/declared-in-r6` to the r7 dir — drafted as before/after text in the
   owning fragment, applied by the integrator; the r6 dir stays as filed, and the re-pin
   cascade rows must name it superseded, not erased.
3. Re-run the suite against the landed pair: `python3 .scratch/d06/parity_check.py reports/round-34/handoff/declared-in-r7`
   → expect 31/31; then the judge legs (`packet_uncertainty.py --require-oq --json` →
   `claims 27, findings []`; `packet_links.py --json` → `links_checked == resolved`, `findings []`).
4. Stale audit (two independent seats, per claims.json threshold): grep the five stale token
   families **only inside the D4 ledger rows and `open_questions`** of the delivered packet —
   `typed_labels 74`, `labels 74`, `native-form 56`, `findings_total 16`, `findings_hold_or_fail 15`,
   `hold 15`, `note 1, fail 0`, `thirteen unresolved`, `three quarantine`, `four conflicts`,
   `13 unresolved`, `3 quarantine`, `4 conflicts`, `conflicts (4)`, `quarantine handles (3)` —
   and confirm every live counterpart appears (82 / 64 / 12 / 12 / 6 / 12 holds / 0 note / 0 fail / 0 / 0 / 0).
   Expect zero hits in those two surfaces and *do not* flag the D2 rows, whose 16/15/13/3/4 are live-true.
5. `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0 with `packet_sha256` equal to
   `freeze.txt` (the frozen-packet/frozen-twin legs, `:3932-3947`).

## E. Embedded sources

### E.1 `parity_check.py` — the suite as run (verbatim source; save beside the round as a tool, run with `python3 parity_check.py <pair-dir>`)

```python
#!/usr/bin/env python3
"""twin.json shape-parity + expected.json consistency checker (D06, round 34).

Read-only: it never writes into the repo. Run against a frozen pair dir:

  python3 .scratch/d06/parity_check.py reports/round-30/handoff/declared-in-r6
"""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("e2e", REPO / "tools/exercise-handoff-e2e.py")
E2E = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(E2E)

TWIN_KEYS = ["artifact_manifest", "claim_ledger", "coupling_edges", "open_questions",
             "packet_id", "packet_version", "profile"]
ROW_KEYS = ["claim_id", "claim_kind", "evidence_status", "links", "statement", "uncertainty"]
EDGE_KEYS = ["applicability", "claims", "declared_in", "edge_id", "limits", "mechanism",
             "relation", "source", "target_ids"]
UNC_KEYS = ["basis", "status"]
MANIFEST_KEYED = ("examples/culture-d2/packet.d2.yml", "examples/culture-d3/packet.json",
                  "reports/round-6/parent-reconciliation.json", "examples/culture-d4/packet.d4.yml")

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main(pair_dir):
    d = Path(pair_dir)
    packet = (d / "packet.md").read_text(encoding="utf-8")
    twin_text = (d / "twin.json").read_text(encoding="utf-8")
    twin = json.loads(twin_text)
    exp = json.loads((d / "expected.json").read_text(encoding="utf-8"))
    freeze = (d / "freeze.txt").read_text(encoding="utf-8")

    # P1 crypt. packet bytes vs expected + freeze.txt
    pkt = hashlib.sha256(packet.encode("utf-8")).hexdigest()
    check("P1 packet_sha256", pkt == exp["packet_sha256"] and f"packet_sha256: {pkt}" in freeze,
          f"measured {pkt[:12]}… exp {exp['packet_sha256'][:12]}…")

    # P2 twin canonical serialization (renderer rule: indent=1, sort_keys, ensure_ascii off, + "\n")
    canon = json.dumps(twin, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    twin_hash = sha256_text(twin_text)
    check("P2 twin_sha256 canonical", canon == twin_text and twin_hash == exp["twin_sha256"]
          and f"twin_sha256: {twin_hash}" in freeze, f"measured {twin_hash[:12]}…")

    # P3 twin top-level key set is exactly the seven, in the renderer's emitted order
    check("P3 twin key set", sorted(twin.keys()) == TWIN_KEYS, f"{len(twin)} keys: {sorted(twin.keys())}")

    # P4 manifest = V3_READ_SET order, A-NN ids, digests equal expected.inputs
    man = twin["artifact_manifest"]
    read_set = list(E2E.V3_READ_SET)
    order_ok = len(man) == len(read_set) == 58 and all(
        r["artifact_id"] == f"A-{i:02d}" and r["path"] == read_set[i - 1] for i, r in enumerate(man, 1))
    dig_ok = all(r["sha256"] == exp["inputs"].get(r["path"]) for r in man)
    check("P4 manifest order+ids", order_ok, f"{len(man)} rows vs read set {len(read_set)}")
    check("P4b manifest digests == inputs", dig_ok, "all 58 match" if dig_ok else "mismatch")
    check("P4c manifest paths == inputs keys", {r["path"] for r in man} == set(exp["inputs"]), "")

    # P5 record_ids only where the renderer adds them
    keyed = sorted(r["path"] for r in man if "record_ids" in r)
    check("P5 record_ids rows", keyed == sorted(MANIFEST_KEYED), f"{keyed}")

    # P6 claim_ledger shape: keys, order vs expected.claim_ids, census, links
    led = twin["claim_ledger"]
    ids = [r["claim_id"] for r in led]
    check("P6 ledger id order == expected.claim_ids", ids == exp["claim_ids"], f"{len(ids)} rows")
    shape_ok = all(sorted(r.keys()) == ROW_KEYS and sorted(r["uncertainty"].keys()) == UNC_KEYS
                   and isinstance(r["links"], list) and r["links"] for r in led)
    check("P6b ledger row shape", shape_ok, "6 keys + uncertainty{status,basis} + non-empty links")
    census = {s: sum(1 for r in led if r["uncertainty"]["status"] == s)
              for s in ("supported", "partial", "unresolved")}
    check("P6c census == expected.uncertainty.statuses", census == exp["uncertainty"]["statuses"], f"{census}")

    # P7 open_questions: ids, and every unresolved claim referenced (--require-oq contract)
    oq = twin["open_questions"]
    oq_ids = [r["id"] for r in oq]
    check("P7 open_question ids", oq_ids == [f"OQ-V2-0{i}" for i in range(1, 8)] + ["OQ-V3-04", "OQ-V3-05", "OQ-V3-06"],
          f"{oq_ids}")
    referenced = set()
    for row in oq:
        for tok in str(row.get("unresolved_claims", "")).replace(" ", "").split(","):
            if tok:
                referenced.add(tok)
    unresolved = {r["claim_id"] for r in led if r["uncertainty"]["status"] == "unresolved"}
    check("P7b every unresolved claim is referenced by an OQ", unresolved <= referenced,
          f"unresolved {sorted(unresolved)}")

    # P8 coupling_edges: count, the 34 v2 rows byte-equal the filed yml rows, claims ⊆ ledger
    edges = twin["coupling_edges"]
    v2_expected = E2E.v3_load_v2_edges(str(REPO))
    v2_ids = {r["edge_id"] for r in v2_expected}
    carried = [r for r in edges if r["edge_id"] in v2_ids]
    check("P8 edge count", len(edges) == exp["counts"]["edges"] == 88 and len(carried) == 34
          and sum(1 for r in edges if r["edge_id"].startswith("D4E-")) == 54,
          f"{len(edges)} rows, {len(carried)} v2, {sum(1 for r in edges if r['edge_id'].startswith('D4E-'))} D4E")
    check("P8b v2 edge rows byte-equal filed yml", carried == v2_expected, "34 rows equal" if carried == v2_expected else "differs")
    check("P8c edge claims ⊆ ledger", all(set(r["claims"]) <= set(ids) for r in edges), "")
    check("P8d edge row shape", all(sorted(r.keys()) == EDGE_KEYS for r in edges), f"{len(edges)} rows")

    # P9/P10 semantics expectations vs the harness judges
    links_checked = sum(len(r["links"]) for r in led)
    check("P9 links expectation", links_checked == exp["links"]["links"] == 105
          and exp["links"]["resolve" if False else "resolved"] == 105 and exp["links"]["findings"] == 0,
          f"{links_checked} link tokens")
    check("P10 uncertainty expectation", len(led) == exp["uncertainty"]["claims"] == 27
          and exp["uncertainty"]["findings"] == 0 and exp["uncertainty"]["require_oq_findings"] == 0,
          f"claims {len(led)}")

    # P11 cross_refs + declared constants
    xr = exp["cross_refs"]
    check("P11 contract digest from inputs", xr["contract_digest"] == "sha256:" + exp["inputs"]["corpus/knowledge/synthesis/worldbible-integration-contract.md"], "")
    check("P11b component/d4 pin matches", xr["component_digests_checked"] == xr["component_digests_matched"] == 26
          and xr["d4_pins_checked"] == xr["d4_pins_matched"] == 8, "")
    check("P11c gate scan == declared", xr["gate_scan"] == exp["expected_scan"] == E2E.V3_DECLARED["expected_scan"], f"{xr['gate_scan']}")
    declared_ok = all(exp[k] == E2E.V3_DECLARED[k] for k in E2E.V3_DECLARED)
    check("P11d declared constants enforced by loader", declared_ok, "")
    check("P11e constants", exp["profile"] == E2E.V3_PROFILE and exp["packet_id"] == E2E.V3_PACKET_ID
          and exp["packet_version"] == E2E.V3_PACKET_VERSION and twin["profile"] == exp["profile"]
          and twin["packet_id"] == exp["packet_id"] and twin["packet_version"] == exp["packet_version"], "")
    check("P11f glossary ids", exp["glossary_entry_ids"] == [f"L{i:02d}" for i in range(1, 21)], "")

    # P12 baseline self-integrity digest
    check("P12 baseline_digest", exp["baseline_digest"] == E2E.v3_baseline_digest(exp), "")

    # P13 field_digests cover the gate's 16 fields and hash the delivered values
    fv = E2E.extract_field_values(packet)
    check("P13 field_digests keys == FIELD_NAMES",
          sorted(exp["field_digests"].keys()) == sorted(E2E.FIELD_NAMES) == sorted(fv.keys()),
          f"{len(exp['field_digests'])} fields")
    bad = [n for n, dig in exp["field_digests"].items() if sha256_text(fv.get(n, "")) != dig]
    check("P13b each field digest matches the delivered field value", not bad, f"mismatches: {bad}")

    # P14 twin is a projection of the delivered packet bytes (ledger+edges re-derived)
    rel = E2E.parse_ledger(packet)
    red = [{"claim_id": r["claim_id"], "claim_kind": r["kind"], "evidence_status": r["evidence_status"],
            "uncertainty": {"status": r["uncertainty_status"], "basis": r["uncertainty_basis"]},
            "links": list(r["links"]), "statement": r["statement"]} for r in rel]
    ree = [{k: (list(v) if isinstance(v, list) else v) for k, v in r.items()} for r in E2E.parse_edges(packet)]
    check("P14 twin.claim_ledger re-derived from packet.md", red == led, f"{len(red)} rows")
    check("P14b twin.coupling_edges re-derived from packet.md", ree == edges, f"{len(ree)} rows")

    # P15 open_questions text parity: each twin row is the exact packet bullet, plus
    # "(unresolved claims: X)" unless the claim set is the em-dash "none" token (renderer rule).
    packet_lines = packet.splitlines()
    oq_bad = []
    for row in oq:
        want = f"- {row['id']}: {row['question']}"
        tok = row.get("unresolved_claims")
        if tok not in (None, "", "—"):
            want += f" (unresolved claims: {tok})"
        if want not in packet_lines:
            oq_bad.append(row["id"])
    check("P15 open-question text parity with packet.md", not oq_bad, f"mismatches: {oq_bad}")

    # P16 freeze.txt carries the same measured pair as expected.json
    f_ok = (f"packet_sha256: {exp['packet_sha256']}" in freeze and f"twin_sha256: {exp['twin_sha256']}" in freeze
            and f"frozen: {exp['frozen_at']} by {exp['frozen_by']}" in freeze
            and f"claims: {len(led)} statuses {census['supported']}/{census['partial']}/{census['unresolved']}" in freeze
            and f"read set: {len(read_set)} files; component digests {xr['component_digests_matched']}/"
                f"{xr['component_digests_checked']}; d4 pins {xr['d4_pins_matched']}/{xr['d4_pins_checked']}" in freeze)
    check("P16 freeze.txt == expected.json measured values", f_ok, "")

    for name, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" — {detail}" if detail else ""))
    bad = [n for n, ok, _ in results if not ok]
    print(f"\n{len(results) - len(bad)}/{len(results)} parity checks passed"
          + (f"; FAILED: {bad}" if bad else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
```

### E.2 Machine-generated r7 template (placeholders marked)

Generated by importing the renderer read-only and filling class-2 values; `inputs` is carried in full so the integrator can diff the frozen file against it
(`diff <(python3 …template…) reports/round-34/handoff/declared-in-r7/expected.json` shows only the class-3 lines when the pre-determination holds).

```json
{
 "alias_state": "landed",
 "baseline_digest": "<RECOMPUTE-AT-FREEZE>",
 "claim_ids": [
  "D2-CL01",
  "D2-CL02",
  "CL01",
  "CL02",
  "CL03",
  "CL04",
  "CL05",
  "CL06",
  "CL07",
  "CL08",
  "CL09",
  "CL10",
  "CL11",
  "CL12",
  "CL13",
  "D4-CL01",
  "D4-CL02",
  "D4-CL03",
  "D4-CL04",
  "D4-CL05",
  "D4-CL06",
  "D4-CL07",
  "D4-CL08",
  "D4-CL09",
  "D4-CL10",
  "D4-CL11",
  "D4-CL12"
 ],
 "counts": {
  "claims": 27,
  "d2_coupling_notes": 29,
  "d2_lexicon": 40,
  "d2_names": 8,
  "d2_to_verify_lines": 21,
  "d2_typed_labels": 58,
  "d3_bridges": 5,
  "d3_lexicon": 20,
  "d3_names": 6,
  "d3_references": 5,
  "d4_claims": 12,
  "d4_costumes": 6,
  "d4_edges": 54,
  "d4_era_records": 8,
  "d4_holds": 12,
  "d4_lexicon": 62,
  "d4_rank_rules": 4,
  "d4_symbols": 8,
  "d4_typed_labels": 82,
  "edges": 88
 },
 "cross_refs": {
  "component_digests_checked": 26,
  "component_digests_matched": 26,
  "contract_digest": "sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069",
  "contract_id": "kotodama-lore-adjacency",
  "contract_revision": "1.0.0",
  "d4_pins_checked": 8,
  "d4_pins_matched": 8,
  "gate_exit": 0,
  "gate_scan": {
   "fields": "16/16",
   "findings": 0,
   "glossary_entries": 20
  },
  "gate_stdout_sha256": "<RECOMPUTE-AT-FREEZE>"
 },
 "declared_expectation": "exit 0 / findings [] / uncertainty+links findings 0 with every link resolved, fixed before implementation; hashes measured from bytes, never generated from a printed verdict",
 "expected_exit": 0,
 "expected_finding_ids": [],
 "expected_links_findings": 0,
 "expected_links_unresolved": 0,
 "expected_scan": {
  "fields": "16/16",
  "findings": 0,
  "glossary_entries": 20
 },
 "expected_uncertainty_findings": 0,
 "field_digests": {
  "artifact_manifest": "<RECOMPUTE-AT-FREEZE>",
  "baseline_bible_ref": "<RECOMPUTE-AT-FREEZE>",
  "claim_ledger": "<RECOMPUTE-AT-FREEZE>",
  "contract_ref": "<RECOMPUTE-AT-FREEZE>",
  "coupling_edges": "<RECOMPUTE-AT-FREEZE>",
  "dependency_manifest": "<RECOMPUTE-AT-FREEZE>",
  "open_questions": "<RECOMPUTE-AT-FREEZE>",
  "packet_id": "<RECOMPUTE-AT-FREEZE>",
  "packet_version": "<RECOMPUTE-AT-FREEZE>",
  "producer": "<RECOMPUTE-AT-FREEZE>",
  "recipient": "<RECOMPUTE-AT-FREEZE>",
  "request_ref": "<RECOMPUTE-AT-FREEZE>",
  "requested_decisions": "<RECOMPUTE-AT-FREEZE>",
  "scope": "<RECOMPUTE-AT-FREEZE>",
  "subject_refs": "<RECOMPUTE-AT-FREEZE>",
  "validation": "<RECOMPUTE-AT-FREEZE>"
 },
 "frozen_at": "2026-10-19",
 "frozen_by": "tools/exercise-handoff-e2e.py --profile v3",
 "glossary_entry_ids": [
  "L01",
  "L02",
  "L03",
  "L04",
  "L05",
  "L06",
  "L07",
  "L08",
  "L09",
  "L10",
  "L11",
  "L12",
  "L13",
  "L14",
  "L15",
  "L16",
  "L17",
  "L18",
  "L19",
  "L20"
 ],
 "inputs": {
  "corpus/knowledge/synthesis/worldbible-integration-contract.md": "5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069",
  "corpus/lessons/round-6-sources/03.json": "adb22c9a5f3acee621103c7b9dddeeb1eedba22d9e1d92081e37825b80560cea",
  "corpus/lessons/round-6-sources/05.json": "a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb",
  "corpus/lessons/round-6-sources/09.json": "0dd2820d1e837b9ab5e503d21f1a891d367d873c9335f9dad80bef3c2da6ac94",
  "corpus/lessons/round-6-sources/13.json": "695043562e7e0caeda6693384baca060009c9e3feb2c108f5e8ea6bfc282d71a",
  "examples/culture-d2/components/05-lexicon.yml": "9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf",
  "examples/culture-d2/components/09-eras-calendar.yml": "540a9339627fdcb802a7f59915a3c72e8234fff37c4a771783382af9c863b030",
  "examples/culture-d2/components/11-costumes.yml": "b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22",
  "examples/culture-d2/components/12-rank-rules.yml": "28696a5a70404984fbf1a453f66c9e7618e318ebf93f25bce461fdb7dfcd35a3",
  "examples/culture-d2/packet.d2.yml": "e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643",
  "examples/culture-d2/typed-labels.d2.yml": "a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43",
  "examples/culture-d3/components/04-language.json": "fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa",
  "examples/culture-d3/components/05-ritual.json": "20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d",
  "examples/culture-d3/components/06-material.json": "ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7",
  "examples/culture-d3/components/07-evidence.json": "1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3",
  "examples/culture-d3/controls.json": "f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70",
  "examples/culture-d3/expected.json": "562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc",
  "examples/culture-d3/packet.gates.yml": "306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425",
  "examples/culture-d3/packet.json": "bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829",
  "examples/culture-d4/ASSEMBLY.md": "37b6a98901bd4244b166398fecf6d9472b9ac36ed4028fb57b240fd4d44fee2a",
  "examples/culture-d4/brief.md": "00aa85ff6f9959fa8388f6d05a2c074c965e4bf843c27a8969476f3472c5eed2",
  "examples/culture-d4/components/01-brief.yml": "a1e532ad05a9ee2bbc2f0a0cce56127338110942389630b1ace1918f7f2ade9e",
  "examples/culture-d4/components/02-phonology.yml": "7aa9cac5c030dfb39fbe5a90d04ea5d94f130f7a7e28b5bbb17ff2773ab0a42a",
  "examples/culture-d4/components/03-orthography.yml": "0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b",
  "examples/culture-d4/components/04-lexicon.yml": "ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d",
  "examples/culture-d4/components/05-naming.yml": "b154d80700c47719dcf8395f6017f68c00c21a5eea79965d205df4bdbb688e0c",
  "examples/culture-d4/components/06-myth.yml": "2ca4935d8dc33899a98ebfe2212f73ca5efadee56e7720b59a592416fd3a6b9d",
  "examples/culture-d4/components/07-symbolism.yml": "5da857dc832c69b71fe1ac51f80232b63527e8e953abe6d93e26836c28c1c80c",
  "examples/culture-d4/components/08-eras.yml": "1c9202e3730530a5e82dc57b3e1622b13f94cfd27c4581d90a0b95d8c11f50a0",
  "examples/culture-d4/components/09-costumes.yml": "f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23",
  "examples/culture-d4/components/10-ritual-calendar.yml": "5a8d41b4bc58997a8181c8f5ae8f2c279b48c92b76f6728deec23713a1ab85a2",
  "examples/culture-d4/components/11-contact-history.yml": "7b6932aff32871c587834ad7d42a237836b01e4188eee118b7203c6ddfddaa9c",
  "examples/culture-d4/components/12-provenance.yml": "540f7d2258f3a4000f1aa670742b88b440d2ce107ace49d4246f00c7726d8d69",
  "examples/culture-d4/expected-holds.json": "e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3",
  "examples/culture-d4/packet.d4.typed.yml": "d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182",
  "examples/culture-d4/packet.d4.yml": "aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3",
  "examples/culture-d4/typed-labels.d4.yml": "c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e",
  "reports/round-15/handoff/packet-v2-05.md": "24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b",
  "reports/round-15/handoff/packet-v2-05.yml": "39cf4d53b02a1a9026e3a9a302cd1031d1b6a55fc2b8ea9d7b7eb877fa1dfcd6",
  "reports/round-18/d4/determinism.md": "0b867388e736534bb03b2605334ecef9dba51e5966eebf4e47676831b5164dfc",
  "reports/round-18/d4/holds.md": "4b9321c8414a87bea35aac01b76afbc351c0b509d562ba4ceb47312cf857e78b",
  "reports/round-18/d4/manifest.md": "317fa361ad75b971b0a9d067099dfb48742947ce29cd49fac7a2f63d9be96024",
  "reports/round-18/d4/replay.md": "832eeeb9a93a1925c6815cea9e294bb772373a4c47ca329401e3dd015df7751b",
  "reports/round-19/validation.json": "7dbc346ccab15be1997139989511479f969b250c300168f391b8c4e491d5cb74",
  "reports/round-20/handoff/claims-map.md": "4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8",
  "reports/round-6/parent-reconciliation.json": "1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162",
  "tools/assemble-culture-d3.py": "ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014",
  "tools/assemble-culture-d4.py": "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2",
  "tools/assemble-d2.py": "8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d",
  "tools/assemble-d4-typed.py": "92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0",
  "tools/check-evidence-coupling.py": "849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e",
  "tools/d2-typed-labels.py": "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3",
  "tools/gates/costume-era-consistency-gate.py": "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f",
  "tools/gates/d4-assembly-check-gate.py": "df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a",
  "tools/gates/d4-typed-labels-check-gate.py": "05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841",
  "tools/gates/handoff-packet-check.py": "e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575",
  "tools/harness/packet_links.py": "66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899",
  "tools/harness/packet_uncertainty.py": "cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26"
 },
 "limits": "pins computational inputs only; not lore acceptance, not canon, not completion of the round arc; documentation surfaces excluded",
 "links": {
  "exit": 0,
  "findings": 0,
  "links": 105,
  "resolved": 105
 },
 "packet_id": "kotodama.handoff.d2d3d4-e2e",
 "packet_sha256": "<RECOMPUTE-AT-FREEZE>",
 "packet_version": "3.1.1",
 "profile": "kotodama-handoff-e2e/3",
 "twin_sha256": "<RECOMPUTE-AT-FREEZE>",
 "uncertainty": {
  "claims": 27,
  "exit": 0,
  "findings": 0,
  "require_oq_findings": 0,
  "statuses": {
   "partial": 7,
   "supported": 16,
   "unresolved": 4
  }
 },
 "v2_subset_digest": "ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b"
}
```

## Owed

- `reports/round-34/depth/D05-packet-draft.md` — the packet draft the P1/P2/P13/P14/P15 checks
  will be pointed at. Absent at the time of writing, so every hash-bearing value above is a
  class-3 placeholder; the suite itself is already calibrated against the r6 pair.
- `reports/round-34/depth/D07-gate-run.md`, `reports/round-34/depth/D08-links-uncertainty.md` —
  independent gate and links/uncertainty legs on the same draft; their measured `links`/`claims`
  numbers must be reconciled with the class-2 conditionals in §B.2 (`links` 105/105, census 16/7/4).
- Integrator-owned, not seat-owned: the renderer supersession edit of the four filed r20 D4 rows
  (§C.4), the freeze step (§D.1) and the default re-point (§D.2).

## Citations

Paths and lines relied on (all read-only):

- `reports/round-34/targets.json` — seat D06 object (`mission`, `out: depth/D06-twin-expected.md`, `shared_rules`)
- `reports/round-34/claims.json` — claim D before/after, thresholds, non-goals
- `REGIMEN.md` — round contract
- `tools/exercise-handoff-e2e.py:1930-1934`, `:1935-1959`, `:1960-1978`, `:2261-2307`, `:2566`, `:2599-2618`,
  `:2621-2671`, `:3437-3453`, `:3505-3541`, `:3552-3607`, `:3640-3691`, `:3693-3760`, `:3763-3803`,
  `:3818-3823`, `:3978-4005`, `:4007-4073`, `:4075-4126`, `:4146-4150`
- `reports/round-30/handoff/declared-in-r6/expected.json:1-208` (26 keys; `inputs` `:124-183`, `counts` `:33-54`,
  `cross_refs` `:55-70`, `field_digests` `:82-99`, `links` `:185-190`, `uncertainty` `:196-206`)
- `reports/round-30/handoff/declared-in-r6/twin.json:2`, `:779`, `:1210`, `:2576`, `:2628-2630`
- `reports/round-30/handoff/declared-in-r6/freeze.txt:1-8`, `run.log:1-14`
- `reports/round-30/handoff/declared-in-r6/packet.md:68`, `:69`, `:148`, `:149`, `:150`, `:152`, `:307`
- `reports/round-20/handoff/claims-map.md:99`, `:104`, `:107`, `:119`, `:150`, `:251`
- `examples/culture-d4/typed-labels.d4.yml:30`, `:31`, `:32`, `:37`, `:40`, `:44`, `:46`
- `examples/culture-d4/expected-holds.json:47-49`
- `examples/culture-d2/typed-labels.d2.yml` coverage block (live D2 figures)
- `tools/harness/packet_links.py:729-801`, `tools/harness/packet_uncertainty.py:556-608`,
  `tools/gates/handoff-packet-check.py:27-28`

Commands run (read-only; no round runner executed):

- `python3 .scratch/d06/parity_check.py reports/round-30/handoff/declared-in-r6` → `31/31 parity checks passed`
- `python3 tools/harness/packet_uncertainty.py --packet …/declared-in-r6/twin.json --require-oq --json` → claims 27, findings [], exit 0
- `python3 tools/harness/packet_links.py --packet …/declared-in-r6/twin.json --repo-root . --json` → 105/105, exit 0
- `python3 tools/gates/handoff-packet-check.py packet.md` (isolated temp copy, foreign cwd) → exit 0, `fields=16/16 glossary-entries=20 findings=0`
- `V3Assembly(root)` read-only import (no writes): `packet_sha256 6ced88ad…`, `twin_sha256 6633443d…`, census 16/7/4, 58 read-set digests == r6 `inputs`, 26/26 component digests, 8/8 D4 pins
