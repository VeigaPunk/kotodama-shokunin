# Handoff packet — F-toy fixture with planted defects (non-canon; gate fixture)

Fixture for `tools/gates/handoff-packet-check.py`. Synthetic; it asserts no
world fact and records no canon. It exists only to drive the planted
findings listed in `handoff-packet-check.expected`, so the defects below are
marked `(planted)` and are not house style.

Planted defects (the expected file lists the same IDs):
- HO-MISSING ×2 — the `validation` and `open_questions` sections are omitted
  entirely.
- HO-EMPTY ×1 — `subject_refs` is `TBD` instead of namespaced candidate IDs.
- HO-BASELINE ×1 — `baseline_bible_ref` is `none` while the packet supplies no
  unbound-packet statement.
- HO-CONTRACT-REF ×1 — `contract_ref` names no revision and no digest.
- HO-MANIFEST-DIGEST ×1 — the manifest names no file digests.
- HO-DEP-FLOAT ×1 — the dependency manifest floats a `latest` reference.
- HO-CANON-MARKER ×1 — the packet never carries the contract's non-canon
  standing statement.
- HO-CANON-CLAIM ×1 — the canon_standing line issues a producer-side
  certification.
- HO-GLOSS-ETYM ×2 — entry GE-02 leaves the etymology cell empty; entry GE-03
  states a status outside the licensed vocabulary.

| field | value |
|---|---|
| `packet_id` | KTD-HO-FIXTURE-0001 |
| `packet_version` | 1.0.0 |
| `contract_ref` | kotodama-lore-adjacency (planted: no revision, no digest) |
| `producer` | kotodama-shokunin (fixture worker) |
| `recipient` | lore-shokunin |
| `request_ref` | fixture brief F-T01 (synthetic) |
| `baseline_bible_ref` | none |
| `subject_refs` | TBD |

## canon_standing

- canon_standing: canonized — the producer certifies this packet as canon (planted)

## artifact_manifest

| artifact_id | kind | path | version | records |
|---|---|---|---|---|
| A1 | system-spec | packets/f-toy/system.md | 1.0.0 | 12 |
| A2 | glossary | inline §glossary payload | 1.0.0 | 3 |
| A3 | glossary | packets/f-toy/onomasticon.md | 1.0.0 | 6 |

## scope

| record_id | culture_group | region | variety | script | register | era |
|---|---|---|---|---|---|---|
| R1 | F-toy (fixture culture) | upland | coast variety | Latn | ritual | E1–E2 |

## dependency_manifest

- F-toy phonology profile `latest` (planted: floating reference)
- F-toy naming rules @1.0.0 (pinned)

## claim_ledger

| record_id | kind | statement | provenance | evidence_status |
|---|---|---|---|---|
| C1 | generative rule | F-toy rule R1 (fixture rule) | rule R1 @1.0.0 | invented (toy language) |

## coupling_edges

| edge_id | source | target | relation | justification |
|---|---|---|---|---|
| E-1 | C1 | a fixture lexicon term | dependency | the derived form uses rule R1 @1.0.0 |

## requested_decisions

| record_id | question | alternatives | blocker |
|---|---|---|---|
| C1 | accept the fixture rule as a design input? | accept / defer / reject | none — fixture only |

## glossary payload (F-toy fixture entries; inline, artifact A2)

| entry_id | form | gloss | etymology |
|---|---|---|---|
| GE-01 | talin | 'song-line' (fixture) | status: constructed (toy formation; no real-world claim) |
| GE-02 | musa | 'spring (season)' (fixture) | |
| GE-03 | kanu | 'hearth' (fixture) | status: plausible (planted: outside the status vocabulary) |