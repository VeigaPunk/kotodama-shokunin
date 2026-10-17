# Handoff packet — R11-O08 attempt-3 (hybrid D2+D3 assembly; deliberately unbound research packet; not canonized)

NON-CANON world-bible handoff packet, kotodama-shokunin → lore-shokunin,
assembled per `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(§4 envelope). Third of four independent round-11 assembly attempts
(R11-O06..O09): one envelope carrying records from **both** live drills — the
D2 highland-pastoralist drill and the D3 source-bounded hall drill — with
every digest measured this session. The two drills are **separate fictional
systems**: this packet is an assembly-level union of two payloads, not a
proposal to merge the cultures, and no row claims cross-system identity or
descent. Deciding whether any relation between them exists is a lore side
decision, out of this lane's province; this packet only reports the union and
keeps each system's records traceable to its own files. Nothing here is
canon, a world-bible entry, or lore acceptance; canon standing is lore's
alone.

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)
- handoff_status: prepared-not-accepted (envelope structurally valid; no lore receipt exists)

| field | value |
|---|---|
| packet_id | kotodama.handoff.r11-o08.d2-d3-union |
| packet_version | 0.1.0-draft (round-11 assembly shard R11-O08; assembled 2026-10-17 from the live D2 and D3 bytes pinned below; revised bytes require a new version, contract §9) |
| contract_ref | kotodama-lore-adjacency, revision 1.0.0, contract digest sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 (re-measured 2026-10-17 from live bytes; filed prose cites the superseded 50c4c2f2…; bilateral same-revision read pending, contract §1/§8) |
| producer | kotodama-shokunin (round-11 handoff-assembly shard R11-O08; generative craft and design records only) |
| recipient | lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency) |
| request_ref | none — no lore brief exists in the repository; assembled as a deliberately unbound research drill (contract §4) |
| baseline_bible_ref | none — deliberately unbound research packet; no lore-supplied world-bible revision or digest exists; cannot be imported as canon without a lore baseline and a new reviewed handoff (contract §4) |
| artifact_manifest | 16 measured artifacts, digests in §artifact-manifest — D3 packet examples/culture-d3/packet.json sha256:bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829; D2 packet examples/culture-d2/packet.d2.yml sha256:e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643; union record counts 12 D3 name-formation bases + 8 D2 name-ledger rows |
| subject_refs | two namespaces, all unresolved — D3: wildcard candidate ref `cand:kotodama.d3.*` (language variety, record-keeper office, voice-of-the-record office, hall assembly institution); D2: authored unresolved candidates cand:kotodama.d2.lexicon, cand:kotodama.d2.naming-ledger, cand:kotodama.d2.costume-ledger, cand:kotodama.d2.rank-system, cand:kotodama.d2.era-staging; no lore entity ids supplied, never guessed (contract §4) |
| scope | union of two drills, each kept in its own era system — D3: fictional eras E0/E1, 20 lexemes, 6 names, 7 utterances, 2 beliefs, 2 symbols, 3 materials, 4 objects, 4 costumes (C03 declared RR1 violation), 1 rank rule, 5 references, 5 bridges; D2: fictional stages E0/E1/E2 with nine named eras, 40 lexemes with 2 loan layers, 8 UP-COMPOUND names, 10 costume records with owed native forms, 9 materials, 7 pantheon agents, 23 roles, 9 motifs, 10 symbols; era labels are per-drill coordinates, never compared or synchronized across the two systems by this packet |
| dependency_manifest | D3: profile kotodama-d3-evidence-coupling/1, SC1 /p/ > /f/, AV1, NR1, RR1 (digests in §artifact-manifest); D2: 15 component ledgers as delivered, serializer tools/assemble-d2.py sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d, projection tools/d2-typed-labels.py sha256:0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802; shared: the pinned contract digest above; no floating `latest` |
| claim_ledger | CL-UN-01…CL-UN-12 in §claim-ledger — per-system claims with their system named in every row, plus the union statement itself |
| coupling_edges | CE-UN-01…CE-UN-06 in §coupling-ledger — intra-system edges only (D3 name derivations from D3 lexemes; D2 name derivations from D2 lexicon; D2 costume→material→era couplings); the packet asserts no inter-system edge and reports that question to lore |
| requested_decisions | RD-UN-01…RD-UN-06 in §requested-decisions; "accept" always means retain as non-canon candidate material; no decision requests canonization |
| validation | live runs observed 2026-10-17 by this worker in §checks-run — D3 assembler `--check` exit 0; D3 guard exit 0; D2 assembler `--check` exit 0; D2 projection `--check` exit 1 (single-line digest drift, recorded); both gates' expected holds recorded; this envelope exit 0 fields=16/16 glossary-entries=20; the parent acceptance-runner receipt remains pending |
| open_questions | OQ-R11-A3-01…06 in §open-questions — union semantics unadjudicated, per-system epochs never synchronized, D2 garment forms owed, projection digest drift, no clearance review, no lore receipt or baseline |

## artifact-manifest

Measured with `sha256sum` on 2026-10-17 by this worker from the live bytes
named (repository root). The D3 side and the D2 side are separate artifact
trees; the union is an envelope-level assembly, so each row names its system.
Post-assembly drift on the D2 projection, recorded rather than re-pinned: it
measured `e70ba1477…` at assembly time (with `--check` exiting 1); at
19:13:43 the parallel round-11 D shard regenerated it to `a3aa452c…`, after
which `--check` exits 0. The row below keeps the assembled-time digest.

| artifact_id | path | role | sha256 |
|---|---|---|---|
| A3-PACKET | examples/culture-d3/packet.json | D3 assembled deterministic packet | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| A3-GATES | examples/culture-d3/packet.gates.yml | D3 legacy projection | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| A3-C-LANG | examples/culture-d3/components/04-language.json | D3 component: phonology, lexicon, names, utterances | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| A3-C-RITUAL | examples/culture-d3/components/05-ritual.json | D3 component: beliefs, speech rules, symbols, naming rule | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` |
| A3-C-MATERIAL | examples/culture-d3/components/06-material.json | D3 component: eras, materials, objects, costumes, rank rules | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` |
| A3-C-EVIDENCE | examples/culture-d3/components/07-evidence.json | D3 component: references, bridges, status, screening | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` |
| A3-FROZEN | examples/culture-d3/expected.json | D3 freeze manifest (24 computational input hashes) | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` |
| A3-CONTROLS | examples/culture-d3/controls.json | D3 control expectations | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` |
| A2-PACKET | examples/culture-d2/packet.d2.yml | D2 assembled packet (15 ledgers) | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| A2-LABELS | examples/culture-d2/typed-labels.d2.yml | D2 typed-label projection (58 labels) | `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` |
| A2-C05 | examples/culture-d2/components/05-lexicon.yml | D2 component: lexicon (40 records, 2 loan layers) | `9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf` |
| A2-C11 | examples/culture-d2/components/11-costumes.yml | D2 component: costumes (10 GAR, 9 CMAT, 3 cloth sources) | `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22` |
| A2-C13 | examples/culture-d2/components/13-naming.yml | D2 component: naming ledger (8 names, 3 rejected) | `e0c01eb22977e76e78251cd0b6f8f0b81d1917ca77c9ead04d06b1559b47b6df` |
| A-TOOL-D2 | tools/assemble-d2.py | shared serializer (D3 assembler loads `yaml_lines` read-only) | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| A-TOOL-D3 | tools/assemble-culture-d3.py | D3 deterministic assembler | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| A-GATE-HANDOFF | tools/gates/handoff-packet-check.py | the adjacency gate this envelope is validated with | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| A-CONTRACT | corpus/knowledge/synthesis/worldbible-integration-contract.md | pinned adjacency contract (read-only) | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |

## dependency-manifest

- D3 side: profile `kotodama-d3-evidence-coupling/1`; SC1 initial /p/ > /f/ (E0→E1, ordinary); AV1 L01→L02 (E1, ritual, hall); NR1 offsets [2,8,20] chosen 8 fictional-nights; RR1 hall plant-cloth visitor prohibition; serializer `tools/assemble-d2.py` `yaml_lines` read-only
- D2 side: 15 component ledgers (digests in §artifact-manifest for the cited three); serializer `tools/assemble-d2.py` sha256:8ea6bdde…; typed-label projection `tools/d2-typed-labels.py` sha256:0da0015f…; live drift notice — the committed projection pinned packet_sha256 8da90b07… while the live D2 packet measured e0f21509…, and the parallel round-11 D shard regenerated the projection at 19:13:43 (now `a3aa452c…`, `--check` exit 0)
- shared: the pinned contract digest above; prerequisites are the two systems' own manifests (each packet keeps its own review path)
- no floating `latest` references

## claim-ledger

| claim_id | kind | system | evidence_status | summary |
|---|---|---|---|---|
| CL-UN-01 | generative rule | D3 | constructed (design) | SC1 initial /p/ > /f/ separates E1 ordinary forms from E0 citation forms, ritual layer keeps E0 |
| CL-UN-02 | generative rule | D3 | constructed (design) | AV1 substitutes L02's E0 form for L01 exactly in E1/ritual/hall; no generalized taboo |
| CL-UN-03 | generative rule | D3 | constructed (design) | NR1 discrete naming offsets [2,8,20] fictional-nights, chosen 8; explicitly not a historical prescription |
| CL-UN-04 | generative rule | D3 | constructed (design) | six names N01–N06 are concat derivations of twelve lexicon bases, guard-verified to yield the declared native forms |
| CL-UN-05 | attributed belief | D3 | unresolved in-world | B01/B02 disagree on record-vs-voice binding; both truth_status unresolved |
| CL-UN-06 | lexicon statement | D2 | design (invented) | 40 lexicon records with two loan layers (kas ← gas; per ← bher), 8 constructions, 2 layers |
| CL-UN-07 | naming rule | D2 | design (invented) | eight UP-COMPOUND names; every base exists in the 40-record lexicon; three rejected candidates retained with reasons |
| CL-UN-08 | garment lexicon gap | D2 | hold (live) | GAR-01..GAR-10 carry English translated labels only; ten D2L-FORM-UNRESOLVED holds; no native form exists |
| CL-UN-09 | rank aggregation | D2 | design with gaps | 21 rank-rule records → 9 normalized → 5 projected; 13 unresolved items; 4 rank conflicts (3 holds, 1 note) |
| CL-UN-10 | union statement (meta) | both | design (assembly) | this envelope is an assembly-level union; it asserts no inter-system identity, descent, contact, or era correspondence; that adjudication is lore's |
| CL-UN-11 | clearance statement | both | unresolved | neither drill has a real-language sweep, novelty check, or community consultation; the D2 legacy naming gate records CROSS-HOLD and D3 screening is unresolved |
| CL-UN-12 | reference scopes | D3 | effective R6 scopes | S01/S05 partial-support, S02/S03/S04 scoped-support; the five bridges stay design-only with recorded limits |

## coupling-ledger

| edge_id | system | source | target | relation | justification |
|---|---|---|---|---|---|
| CE-UN-01 | D3 | L02+L03, L08+L11, L04+L12, L09+L05, L16+L20, L06+L13 | N01–N06 | dependency | each name is the concat of its two E1 bases, guard-verified against the declared expected form |
| CE-UN-02 | D3 | SC1 sound law | L01/L04/L05/L06 E1 forms | dependency | initial /p/ > /f/ derives the ordinary spoken forms; citation forms retained |
| CE-UN-03 | D2 | L-08+L-02, L-03+L-29, L-08+L-04, L-34+L-04, L-17+L-10, L-14+L-34, L-13+L-29, L-09+L-08 | NM-01–NM-08 | dependency | UP-COMPOUND concatenations of live lexicon bases (formation records in 13-naming) |
| CE-UN-04 | D2 | GAR-01..GAR-10 | CMAT-01..09 / export clauses | dependency | costume→material couplings with era tags in scope; nine R-MAT-BRIDGE-MISSING holds carried, not merged |
| CE-UN-05 | D2 | GAR-06 silk (E2) | 10-materials lowland-broadcloth (MAT-07) | dependency (conflicted) | one record, two candidate sources of truth; unresolved and reported (RD-UN-05) |
| CE-UN-06 | both | — | — | (none asserted) | the union asserts no inter-system edge; a relation question is reported to lore, never decided here |

## requested-decisions

| decision_id | question | alternatives | blocker |
|---|---|---|---|
| RD-UN-01 | should the two drills be reviewed as one payload or as two independent handoffs? | one union review / two separate review tracks | lane cannot decide; review structure affects every per-record question below |
| RD-UN-02 | retain the D3 20-lexeme set and six names as candidates? | accept / return per-record | none |
| RD-UN-03 | retain the D2 40-record lexicon and eight names as candidates? | accept / return per-record | no real-language sweep (CL-UN-11) |
| RD-UN-04 | supply or decline the ten owed D2 garment native forms? | author future forms / keep labels review-only | forms do not exist; inventing them in assembly is forbidden |
| RD-UN-05 | resolve the D2 silk vs lowland-broadcloth luxury conflict? | adopt silk / adopt broadcloth / defer | one record, two candidate sources of truth |
| RD-UN-06 | which receipt surface and lore baseline apply before any transfer? | no such surface exists yet | blocking for any import (contract §1/§8) |

## checks-run

Observed 2026-10-17 by this worker (read-only runs from the repository root).

| command | exit | observed |
|---|---:|---|
| `python3 tools/assemble-culture-d3.py --check` | 0 | D3 packet.json and packet.gates.yml byte-identical deterministic assembly |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | counts.total 0, findings [], profile kotodama-d3-evidence-coupling/1 |
| `python3 tools/assemble-d2.py --check` | 0 | D2 packet.d2.yml byte-identical deterministic assembly |
| `python3 tools/d2-typed-labels.py --check examples/culture-d2/typed-labels.d2.yml` | 1 | assembly-time run: differs from the deterministic projection; fresh `--emit` diff is exactly the one-line packet_sha256 drift. After the parallel shard's 19:13:43 regeneration the same command exits 0 (§artifact-manifest) |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly CROSS-HOLD ×2 + NAME-NEAR REVIEW — expected hold |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` | 1 | 17 finding lines (10 PHON-INVENTORY on English labels, 6 NAME-NEAR era pairs, 1 CROSS-HOLD) — expected hold |
| `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-3.md` | 0 | fields=16/16 glossary-entries=20 findings=0 |
| `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-3.yml` | 0 | fields=16/16 glossary-entries=20 findings=0 (YAML serialization view) |

## open-questions

- OQ-R11-A3-01: union semantics are unadjudicated — whether two drills may share one envelope, or each needs its own handoff, is a review-structure decision that belongs to lore and the operator.
- OQ-R11-A3-02: the two systems' era coordinates (D3 E0/E1; D2 E0/E1/E2 plus nine named eras) are never synchronized by this packet; any cross-system chronology would be a lore decision and is not proposed.
- OQ-R11-A3-03: ten D2 garment records still owe native forms; no sweep or clearance exists for either system's spellings.
- OQ-R11-A3-04: the committed D2 typed-label projection drifts from live bytes in exactly the packet_sha256 field; a re-emit belongs to the owning shard.
- OQ-R11-A3-05: D2 carries 13 unresolved rank-rule items and 3 quarantine handles; no subset may be promoted as canon-ready.
- OQ-R11-A3-06: no lore receipt and no baseline bible reference exist; the parent acceptance-runner receipt is pending and is not declared passed.

## glossary payload (inline; union of live records — 12 D3 name-formation bases + 8 D2 names = exactly 20 entries)

Rows 1–12 are the twelve D3 lexemes that actually feed name formation (the
distinct union of N01–N06's bases, deduplicated); rows 13–20 are the eight
D2 accepted names. Every row names its system; no row is derived across
systems. All statuses use the licensed vocabulary; D3 forms are constructed
by SC1 and D2 forms by UP-COMPOUND over live lexicon roots.

| entry_id | system | E0 form | E1 form | gloss | etymology |
|---|---|---|---|---|---|
| L02 | D3 | suma | suma | hearth invocation | status: constructed — E0 *suma, unchanged into E1; base of N01 |
| L03 | D3 | talu | talu | record line | status: constructed — E0 *talu, unchanged into E1; base of N01 |
| L08 | D3 | kila | kila | measured fold | status: constructed — E0 *kila, unchanged into E1; base of N02 |
| L11 | D3 | nisu | nisu | night tally | status: constructed — E0 *nisu, unchanged into E1; base of N02 |
| L04 | D3 | palu | falu | boundary token | status: constructed — E0 *palu → E1 falu by SC1 initial /p/ > /f/; base of N03 |
| L12 | D3 | lura | lura | hall passage | status: constructed — E0 *lura, unchanged into E1; base of N03 |
| L09 | D3 | ruma | ruma | assembly seat | status: constructed — E0 *ruma, unchanged into E1; base of N04 |
| L05 | D3 | pira | fira | witness mark | status: constructed — E0 *pira → E1 fira by SC1 initial /p/ > /f/; base of N04 |
| L16 | D3 | ami | ami | settlement | status: constructed — E0 *ami, unchanged into E1; base of N05 |
| L20 | D3 | kuru | kuru | horn rank-clasp | status: constructed — E0 *kuru, unchanged into E1; base of N05 |
| L06 | D3 | puka | fuka | gate announcement | status: constructed — E0 *puka → E1 fuka by SC1 initial /p/ > /f/; base of N06 |
| L13 | D3 | sina | sina | visitor sign | status: constructed — E0 *sina, unchanged into E1; base of N06 |
| NM-01 | D2 | sunel | — | person name (E0); wind-hand | status: constructed — su (D2 L-08 wind) + nel (D2 L-02 hand/forearm), UP-COMPOUND over live lexicon bases |
| NM-02 | D2 | banwal | — | person name (E0); bone-oath | status: constructed — ban (D2 L-03 bone/lineage substance) + wal (D2 L-29 oath), UP-COMPOUND |
| NM-03 | D2 | sulas | — | clan name (E0); wind-lineage | status: constructed — su (D2 L-08 wind) + las (D2 L-04 lineage), UP-COMPOUND |
| NM-04 | D2 | mirlas | — | clan name (E0); fleece-lineage | status: constructed — mir (D2 L-34 fleece/wool) + las (D2 L-04 lineage), UP-COMPOUND |
| NM-05 | D2 | kolsin | — | place name (E0); pass-snow | status: constructed — kol (D2 L-17 pass) + sin (D2 L-10 snow), UP-COMPOUND |
| NM-06 | D2 | tolmir | — | place name (E0); low-ground fleece | status: constructed — tol (D2 L-14 low ground) + mir (D2 L-34 fleece/wool), UP-COMPOUND |
| NM-07 | D2 | belwal | — | proposed cult address (E0); height-oath | status: constructed — bel (D2 L-13 heights) + wal (D2 L-29 oath); address of an existing provisional theonym, not a new god |
| NM-08 | D2 | hursu | — | proposed cult address (E0); storm-wind | status: constructed — hur (D2 L-09 storm) + su (D2 L-08 wind); proposed avoidance address of a provisional theonym |

## assembly-notes (worker R11-O08; not part of the envelope)

Hard-to-populate fields, and what each one required:

- `scope` across two systems — the hardest field in this attempt: the two
  drills have incompatible era systems (D3's two relative eras vs D2's three
  stages under nine named eras). Populating one `scope` value without
  silently synchronizing them required naming each system's coordinates
  side by side and stating that no cross-system comparison is made.
- `coupling_edges` — every edge had to be intra-system. The natural
  temptation, an inter-system edge, would be a canon decision (out of
  province); the field therefore carries one explicit "none asserted" row
  and reports the question.
- `subject_refs` — two namespaces, one of which (D2) has no live candidate
  refs at all; the D2 candidates are authored and marked unresolved.
- `artifact_manifest` — spans two artifact trees plus shared tools; two
  category errors are easy here: citing a D3 digest as if it covered D2
  bytes, and copying the D2 projection's stale internal digest. Both avoided
  by measuring every row live.
- `dependency_manifest` — must keep the two systems' rule sets apart; the
  D3 profile is not a D2 profile and the serializer is the only shared
  component.
- `glossary payload` — 20 rows had to come from two systems without a
  single cross-derived form; D3 rows use the id space L01–L20, D2 rows
  NM-01–NM-08, each with its system column.
- `validation` — two systems means two command batteries; the D2 projection
  check exits 1 for its recorded digest drift.
- `requested_decisions` and `open_questions` — none exist in either
  artifact tree; the union adds the review-structure question
  (one payload vs two), which no per-system file can supply.
- `packet_id`, `packet_version`, `producer` — authored; `recipient` is
  contract-fixed.
