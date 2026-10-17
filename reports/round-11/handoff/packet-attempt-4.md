# Handoff packet — R11-O09 attempt-4 (D3 register payload; deliberately unbound research packet; not canonized)

NON-CANON world-bible handoff packet, kotodama-shokunin → lore-shokunin,
assembled per `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(§4 envelope). Fourth of four independent round-11 assembly attempts
(R11-O06..O09), and the serialization-diverse one: the strict envelope is
carried as a `- field: value` list rather than a table, and the payload draws
the D3 registers that never appear in the lexicon set — names, utterances,
costumes, symbols, and the rank rule — from the live
`examples/culture-d3/` bytes measured below. Only one glossary-shaped table
exists in this document (the 20-row payload); every other table uses
non-glossary column names. Nothing here is canon, a world-bible entry, or
lore acceptance; canon standing is lore's alone. All native spellings are
constructed and unscreened ASCII lowercase.

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)
- handoff_status: prepared-not-accepted (envelope structurally valid; no lore receipt exists)

- packet_id: kotodama.handoff.r11-o09.d3-register-payload
- packet_version: 0.1.0-draft (round-11 assembly shard R11-O09; assembled 2026-10-17 from the live examples/culture-d3 bytes pinned in §artifact-manifest; revised bytes require a new version, contract §9)
- contract_ref: kotodama-lore-adjacency, revision 1.0.0, contract digest sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 (re-measured 2026-10-17 from live bytes; the filed round-7 prose cites the superseded 50c4c2f2…; bilateral same-revision read pending, contract §1/§8)
- producer: kotodama-shokunin (round-11 handoff-assembly shard R11-O09; generative craft and design records only)
- recipient: lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency)
- request_ref: none — no lore brief exists in the repository; assembled as a deliberately unbound research drill (contract §4)
- baseline_bible_ref: none — deliberately unbound research packet; no lore-supplied world-bible revision or digest exists; cannot be imported as canon without a lore baseline and a new reviewed handoff (contract §4)
- artifact_manifest: 12 measured artifacts, digests in §artifact-manifest — packet examples/culture-d3/packet.json sha256:bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829; record counts 6 names / 7 utterances / 4 costumes / 2 symbols / 1 rank rule / 2 beliefs / 3 materials / 4 objects
- subject_refs: namespaced candidate refs only — the live corpus carries the wildcard string cand:kotodama.d3.* (language variety, record-keeper office, voice-of-the-record office, hall assembly institution); no concrete candidate IDs and no lore entity IDs exist; all unresolved, never guessed (contract §4)
- scope: D3 source-bounded hall drill, registers outside the lexicon payload — 6 constructed names N01–N06 (lineage/office/place/personal, era E1); 7 utterances U01–U07 with spoken/written forms and register law; 4 costumes C01–C04 tied to lexemes L17–L20 (C03 a declared RR1 violation); 2 audience-scoped symbols SY01/SY02; 1 invented rank rule RR1; 2 attributed beliefs B01/B02 and 3 materials / 4 objects referenced as context but not payload rows; eras E0/E1 only; no real place
- dependency_manifest: profile kotodama-d3-evidence-coupling/1; SC1 initial /p/ > /f/ (E0→E1, ordinary); AV1 L01→L02 (E1, ritual, hall); NR1 offsets [2,8,20] chosen 8 fictional-nights; RR1 hall plant-cloth visitor prohibition; serializer tools/assemble-d2.py sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d; no floating `latest`
- claim_ledger: CL-RG-01…CL-RG-06 in §claim-ledger — one claim per register family, each with its live record source
- coupling_edges: CE-RG-01…CE-RG-05 in §coupling-ledger — name→lexeme, utterance→lexeme+sound-law, costume→lexeme+material, symbol→audience/era scope, rank rule→costume violation
- requested_decisions: RD-RG-01…RD-RG-05 in §requested-decisions; "accept" always means retain as non-canon candidate material; no decision requests canonization
- validation: live runs observed 2026-10-17 by this worker in §checks-run — assembler `--check` exit 0; evidence-coupling guard exit 0; frozen guard run exit 0; naming gate exit 1 with its expected holds; costume gate exit 1 R-01 only; this envelope exit 0 fields=16/16 glossary-entries=20; the parent acceptance-runner receipt remains pending
- open_questions: OQ-R11-A4-01…06 in §open-questions — sweep unperformed, no receipt/baseline, permission limits, residuals, no calendar, live-vs-filed digest disagreements

## artifact-manifest

Measured with `sha256sum` on 2026-10-17 by this worker from the live bytes
named (repository root).

| artifact_id | path | role | sha256 |
|---|---|---|---|
| A-PACKET | examples/culture-d3/packet.json | assembled deterministic packet (sorted keys, indent 2, final newline) | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| A-GATES | examples/culture-d3/packet.gates.yml | legacy projection (native forms only) | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| A-C-LANG | examples/culture-d3/components/04-language.json | component: phonology, lexicon, names, utterances | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| A-C-RITUAL | examples/culture-d3/components/05-ritual.json | component: beliefs, speech rules, symbols, naming rule | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` |
| A-C-MATERIAL | examples/culture-d3/components/06-material.json | component: eras, materials, objects, costumes, rank rules | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` |
| A-C-EVIDENCE | examples/culture-d3/components/07-evidence.json | component: references, bridges, status, screening | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` |
| A-FROZEN | examples/culture-d3/expected.json | freeze manifest (24 computational input hashes; live digest) | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` |
| A-TOOL-ASSEMBLE | tools/assemble-culture-d3.py | deterministic assembler | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| A-TOOL-GUARD | tools/check-evidence-coupling.py | evidence-coupling guard CLI (stdlib only) | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| A-GATE-HANDOFF | tools/gates/handoff-packet-check.py | the adjacency gate this envelope is validated with | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| A-CONTRACT | corpus/knowledge/synthesis/worldbible-integration-contract.md | pinned adjacency contract (read-only) | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |

## dependency-manifest

- profile `kotodama-d3-evidence-coupling/1` (packet interface; guard CLI contract)
- SC1 sound law `/p/ > /f/`, initial, E0→E1, register `ordinary` (live `packet.sound_changes[0]`)
- AV1 avoidance rule: L01 → L02's E0 form exactly in era E1 / register `ritual` / place `hall` (live `packet.speech_rules[0]`)
- NR1 naming-timing rule: allowed offsets [2, 8, 20] fictional-nights, chosen 8, source S03, `constructed-not-historical` (live `packet.naming_rule`)
- RR1 hall rank rule: invented authority, plant-cloth prohibition for visitors at hall assembly, era E1, no exemptions (live `packet.rank_rules[0]`)
- serializer dependency: `tools/assemble-d2.py` `yaml_lines`, sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d
- phonology context for the payload forms: (C)V(C), 9 consonants, 3 vowels, coda subset n/l/r/s, no onset clusters (live `packet.phonology`)
- prerequisites: the pinned contract digest above; no floating `latest` references

## claim-ledger

| claim_id | kind | evidence_status | summary |
|---|---|---|---|
| CL-RG-01 | naming derivation | constructed (design) | six names N01–N06 are concat derivations of twelve distinct lexicon bases' E1 forms; guard-verified against declared expected strings |
| CL-RG-02 | register law | constructed (design) | seven utterances instantiate SC1 (ordinary) and AV1 (ritual/hall); written forms stay the E0 citation form; U07 shows L01 in the hall stays ordinary-lawful |
| CL-RG-03 | costume-to-lexeme binding | constructed (design) | four costumes bind lexemes L17–L20 and materials M01–M03; C03 is a declared RR1 violation retained visibly |
| CL-RG-04 | sign rules | constructed (design) | SY01/SY02 readings are scoped to the E1 hall and one audience; no colour key and no universal meaning is assigned |
| CL-RG-05 | rank rule | constructed (design) | RR1's authority is invented fiction ("Hall Wardens of the Two Benches"); the prohibition is design, not a real-world clothing law |
| CL-RG-06 | beliefs (context) | unresolved in-world | B01/B02 remain attributed, disagreeing accounts outside this payload's rows; referencing them imports no truth claim |

## coupling-ledger

| edge_id | source | target | relation | justification |
|---|---|---|---|---|
| CE-RG-01 | N01–N06 | L02/L03, L08/L11, L04/L12, L09/L05, L16/L20, L06/L13 | dependency | each name is the concatenation of its two E1 bases; the expected string is replayable by the guard |
| CE-RG-02 | SC1, AV1 | U01–U07 | dependency | ordinary readings use the SC1-changed E1 form; the hall-ritual reading uses AV1's exact substitute; written forms retain E0 |
| CE-RG-03 | C01–C04 | L17–L20, M01–M03 | dependency | costume records bind a lexeme and a material; C03 violates RR1 and is retained as a violation |
| CE-RG-04 | SY01/SY02 | hall audience, era E1 | dependency | each sign's reading is bound to one audience and era; nothing outside that scope is asserted |
| CE-RG-05 | RR1 | C03 | dependency (declared violation) | RR1 prohibits M02 plant-cloth for visitors; C03 records the violation, never repaired into a lawful case |

## requested-decisions

| decision_id | question | alternatives | blocker |
|---|---|---|---|
| RD-RG-01 | retain the six constructed names as candidate labels? | accept as candidates / defer | no real-language sweep (OQ-R11-A4-01), blocking for official approval |
| RD-RG-02 | adopt the register law as instantiated by U01–U07? | accept / return the sound law or the avoidance rule | none |
| RD-RG-03 | adopt the costume bindings including C03's declared violation? | accept as violation / return the rank rule | violation stays visible, never repaired |
| RD-RG-04 | adopt SY01/SY02 with their audience/era scoping? | accept / defer pending institution definition | none |
| RD-RG-05 | which receipt surface and lore baseline apply before any transfer? | no such surface exists yet | blocking for any import (contract §1/§8) |

## checks-run

Observed 2026-10-17 by this worker (read-only runs from the repository root).

| command | exit | observed |
|---|---:|---|
| `python3 tools/assemble-culture-d3.py --check` | 0 | packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | counts.total 0, findings [], profile kotodama-d3-evidence-coupling/1 |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | 0 | findings [] against the live freeze manifest sha256:562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly CROSS-HOLD ×2 + NAME-NEAR REVIEW — expected hold |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly one finding: R-01 [note] C03 declared RR1 violation kept visible; no R-02 — expected hold |
| `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-4.md` | 0 | fields=16/16 glossary-entries=20 findings=0 |
| `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-4.yml` | 0 | fields=16/16 glossary-entries=20 findings=0 (YAML serialization view with a grouped-row envelope) |

## open-questions

- OQ-R11-A4-01: real-language homophone/offensive-association sweep not performed on any constructed name, lexeme, or utterance form; screening unresolved; blocking for official name approval.
- OQ-R11-A4-02: no lore receipt and no baseline bible reference exist; the parent acceptance-runner receipt is pending and is not declared passed.
- OQ-R11-A4-03: cultural-permission limit — invented design; citation of real sources is not permission, no community consultation occurred.
- OQ-R11-A4-04: inherited historical/corpus residuals from the five closed bindings stay open and are repaired by nothing in this payload.
- OQ-R11-A4-05: no calendar — era coordinates are fictional stages; no dates exist; blocking for any era dating.
- OQ-R11-A4-06: live-vs-filed digest disagreement — the round-7 prose cites contract 50c4c2f2… and freeze 74496aa8…; live bytes measure 5f4c02bf… and 562b76cb…. This packet pins the live values and does not rewrite the filed prose.

## glossary payload (inline; D3 registers outside the lexicon — 6 names + 7 utterances + 4 costumes + 2 symbols + 1 rank rule = exactly 20 entries)

This payload deliberately exercises the entry profile's license for
`status: unknown`/derivation statements on records that are **not lexical
entries**: names and costumes carry true derivations, utterances carry
register-law instantiations, and symbols and the rank rule carry sign/rule
statements with no lexical etymology at all. Every cell says which it is; no
real-language etymology is claimed anywhere.

| entry_id | register | form | gloss | etymology (derivation status for non-lexical records) |
|---|---|---|---|---|
| N01 | name (lineage) | sumatalu | lineage name: hearth-record line; era E1 | status: constructed — concat of L02+L03 E1 bases, guard-verified expected sumatalu |
| N02 | name (lineage) | kilanisu | lineage name: measured fold and night tally; era E1 | status: constructed — concat of L08+L11 E1 bases, guard-verified expected kilanisu |
| N03 | name (office) | falulura | office name: boundary token of the hall passage; era E1 | status: constructed — concat of L04+L12 E1 bases, guard-verified expected falulura |
| N04 | name (office) | rumafira | office name: assembly seat witness mark; era E1 | status: constructed — concat of L09+L05 E1 bases, guard-verified expected rumafira |
| N05 | name (place) | amikuru | place name: settlement horn-clasp mark; era E1 | status: constructed — concat of L16+L20 E1 bases, guard-verified expected amikuru |
| N06 | name (personal) | fukasina | personal name: gate announcement visitor sign; era E1 | status: constructed — concat of L06+L13 E1 bases, guard-verified expected fukasina |
| U01 | utterance | fina | spoken pledge (L01), era E1, ordinary, market | status: constructed — SC1-changed E1 ordinary form; written form pina (E0 citation) retained |
| U02 | utterance | suma | spoken pledge (L01), era E1, ritual, hall | status: constructed — AV1 substitute (L02's E0 form) required by register law; written form pina retained |
| U03 | utterance | talu | record line (L03), era E1, ordinary, market | status: constructed — no initial /p/, form unchanged into E1; written form talu |
| U04 | utterance | talu | record line (L03), era E1, ritual, hall | status: constructed — register law leaves the form unchanged; no avoidance trigger for L03 |
| U05 | utterance | falu | boundary token (L04), era E1, ordinary, market | status: constructed — SC1-changed E1 ordinary form; written form palu (E0 citation) retained |
| U06 | utterance | suma | hearth invocation (L02), era E1, ritual, hall | status: constructed — L02 is the AV1 substitute itself; spoken and written forms agree |
| U07 | utterance | fina | spoken pledge (L01), era E1, ordinary, hall | status: constructed — witnesses that avoidance is place/register-limited: L01 in the hall outside the ritual register stays ordinary-lawful |
| C01 | costume | nara | earlier-period felt work garment (translated label); material M01, era E0 | status: constructed — lexeme L17 of the assembled lexicon; lawful wearer scope |
| C02 | costume | salu | later-period felt work garment (translated label); material M01, era E1 | status: constructed — lexeme L18; lawful wearer scope |
| C03 | costume | mila | visitor plant-cloth garment at hall assembly (translated label); material M02, era E1 | status: constructed — lexeme L19; declared RR1 violation, retained visibly, never repaired |
| C04 | costume | kuru | appointed officer horn attachment at hall assembly (translated label); material M03, era E1 | status: constructed — lexeme L20; lawful appointed attachment |
| SY01 | symbol | Bound-cord knot set on the record chest | sign of the record-keeper's office; audience: admitted E1 hall members during a dispute; era E1 | status: constructed — sign→reading rule (packet.symbols[0]); scoped to that hall and era; no colour and no cross-era or universal meaning assigned |
| SY02 | symbol | Plain ring on the speaker's post | sign of the voice-of-the-record office; audience: E1 hall members present when claims are spoken; era E1 | status: constructed — sign→reading rule (packet.symbols[1]); denotes nothing outside that hall and era; no colour and no universal meaning assigned |
| RR1 | rank rule | Hall Wardens of the Two Benches | invented fictional hall authority; prohibits material M02 plant-cloth for visitor wearers at hall assembly; era E1, no exemptions | status: constructed — invented institution, not a real-world clothing law; C03's violation is the declared case |

## assembly-notes (worker R11-O09; not part of the envelope)

Hard-to-populate fields, and what each one required:

- The strict envelope as a `- field: value` list — every value must stay on
  one line (the gate continues an item only on indented lines, and a
  continuation is easy to miss); the long `scope` and `validation` values
  were compressed deliberately, with detail pushed into their sections.
- Payload rows for **non-lexical registers** — the hardest honesty problem
  in this attempt: a symbol or a rank rule has no etymology. Rather than
  fabricate one, each row's status cell states what the record actually is
  (a sign→reading rule, an invented institution) and the table header says
  "etymology (derivation status for non-lexical records)". The profile's
  licensed vocabulary makes this legitimate; nothing is laundered as a
  lexical derivation.
- Utterance rows — the profile's `form` slot cannot express the spoken/
  written split that D3's register law makes load-bearing (U01/U02/U05/U07
  write the E0 citation form but speak another). The written form is carried
  in the status cell, and the claim ledger states the law.
- `artifact_manifest` — measured live; the filed prose's freeze digest
  (74496aa8…) is stale against live bytes (562b76cb…), so copying it would
  have been wrong.
- `artifact_manifest` and `contract_ref` share a second trap: the contract
  digest moved in round 8 (50c4c2f2… → 5f4c02bf…).
- `subject_refs` — only the wildcard `cand:kotodama.d3.*` exists in live
  content; no concrete candidate IDs were ever allocated.
- `request_ref` and `baseline_bible_ref` — no live source at all; both are
  authored `none` values whose wording is load-bearing for the gate
  (HO-BASELINE).
- `validation` — no machine-readable receipts; all six runs were re-executed
  and recorded with observed exits.
- `requested_decisions`, `open_questions` — only in handoff prose, never in
  the generated packet; a tool reading just `packet.json` cannot populate
  them.
- Not hard: `scope`, `dependency_manifest`, `claim_ledger`,
  `coupling_edges`, and the 20 payload rows — every value traces to
  `packet.json` records.
