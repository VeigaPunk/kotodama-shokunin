# Handoff packet — R11-O06 attempt-1 (D3 live-bytes assembly; deliberately unbound research packet; not canonized)

NON-CANON world-bible handoff packet, kotodama-shokunin → lore-shokunin,
assembled per `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(§4 envelope). This is the first of four independent round-11 assembly
attempts (R11-O06..O09): every value below is read from the live
`examples/culture-d3/` bytes measured in the artifact manifest, not copied
from a filed handoff's prose. Where a filed digest disagrees with live bytes
the live measurement wins and the disagreement is recorded in
§assembly-notes. Nothing here is canon, a world-bible entry, or lore
acceptance; canon standing is lore's alone. Era coordinates E0/E1 are
fixture-relative, not BCE/CE. All native spellings are constructed and
unscreened ASCII lowercase; no real-language clearance or cultural
permission is claimed.

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)
- handoff_status: prepared-not-accepted (envelope structurally valid; no lore receipt exists)

| field | value |
|---|---|
| packet_id | kotodama.handoff.r11-o06.d3-live-bytes |
| packet_version | 0.1.0-draft (round-11 assembly shard R11-O06; assembled 2026-10-17 from the live examples/culture-d3 bytes pinned below; revised bytes require a new version, contract §9) |
| contract_ref | kotodama-lore-adjacency, revision 1.0.0, contract digest sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 (re-measured 2026-10-17 from live bytes; the round-7 handoff prose still cites 50c4c2f2…, superseded by round-8 commit e1694ba; bilateral same-revision read pending, contract §1/§8) |
| producer | kotodama-shokunin (round-11 handoff-assembly shard R11-O06; generative craft and design records only) |
| recipient | lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency) |
| request_ref | none — no lore brief exists in the repository; assembled as a deliberately unbound research drill (contract §4) |
| baseline_bible_ref | none — deliberately unbound research packet; no lore-supplied world-bible revision or digest exists; cannot be imported as canon without a lore baseline and a new reviewed handoff (contract §4) |
| artifact_manifest | 15 measured artifacts, digests in §artifact-manifest — packet examples/culture-d3/packet.json sha256:bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829 (record counts 2 eras / 20 lexemes / 6 names / 7 utterances / 2 beliefs / 2 symbols / 3 materials / 4 objects / 4 costumes / 1 sound change / 1 avoidance rule / 1 timing rule / 1 rank rule / 5 references / 5 bridges) |
| subject_refs | namespaced candidate refs only — the live corpus carries the wildcard string `cand:kotodama.d3.*` (language variety, record-keeper office, voice-of-the-record office, hall assembly institution); no concrete candidate IDs and no lore entity IDs exist; all unresolved, never guessed (contract §4) |
| scope | D3 source-bounded culture drill; two fictional eras E0 (citation/union stage) and E1 (ordinary-speech stage); phonology (C)V(C), 9 consonants, 3 vowels, coda subset n/l/r/s, no onset clusters; 20 constructed lexemes L01–L20; 6 constructed names N01–N06; 7 utterances U01–U07; 2 attributed beliefs B01/B02; 2 audience-scoped symbols SY01/SY02; 3 materials M01–M03; 4 objects O01–O04; 4 costumes C01–C04 (C03 a declared RR1 violation); 1 rank rule RR1; 5 closed references S01–S05; 5 bridges BR01–BR05; no real place; ASCII lowercase spellings only |
| dependency_manifest | profile kotodama-d3-evidence-coupling/1; SC1 initial /p/ > /f/ E0→E1 ordinary register; AV1 L01→L02 ritual substitute (E1, hall); NR1 offsets [2,8,20] chosen 8 fictional-nights; RR1 hall plant-cloth visitor prohibition (E1); serializer tools/assemble-d2.py (yaml_lines, read-only) sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d; closed ledger digests for S01–S05 and parent reconciliation pinned in §artifact-manifest; no floating `latest` |
| claim_ledger | CL01–CL13 in §claim-ledger — generative rules, sign rules, attributed belief, designer interpretation, real-world references with effective round-6 scopes, and the unresolved screening statement, all derived from live packet records |
| coupling_edges | BR01–BR05 in §coupling-ledger — four `method-transfer` edges and one `analogy`, all `asserted_scope: design-only`, each with its recorded limits |
| requested_decisions | RD-01–RD-08 in §requested-decisions — per-record accept/defer/reject questions; "accept" always means retain as non-canon candidate material; no decision requests canonization |
| validation | live runs observed 2026-10-17 by this worker in §checks-run — assembler `--check` exit 0; evidence-coupling guard exit 0 findings []; frozen guard run exit 0; naming gate exit 1 with exactly its expected holds; costume gate exit 1 R-01 only; this envelope exit 0 fields=16/16 glossary-entries=20; the parent acceptance-runner receipt remains pending and is not declared passed |
| open_questions | OQ-R11-A1-01…07 in §open-questions — unresolved real-language sweep, no lore receipt or baseline, permission limits, inherited historical residuals, no calendar, live-vs-filed digest disagreements, acceptance-runner receipt pending |

## artifact-manifest

Every digest below was measured with `sha256sum` on 2026-10-17 by this
worker from the live bytes named (command run from the repository root). The
four component digests equal `packet.json`'s own `assembly.source_sha256`
block; the serializer digest equals its `assembly.serializer_sha256`.
Two live digests disagree with the round-7 handoff prose — see
§assembly-notes; the live measurement is used here.

| artifact_id | path | role | sha256 |
|---|---|---|---|
| A-PACKET | examples/culture-d3/packet.json | assembled deterministic packet (sorted keys, indent 2, final newline) | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| A-GATES | examples/culture-d3/packet.gates.yml | legacy projection (native forms only; trace + 8 projection limits under assembly) | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| A-C-LANG | examples/culture-d3/components/04-language.json | component: phonology, lexicon, names, sound changes, utterances | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| A-C-RITUAL | examples/culture-d3/components/05-ritual.json | component: beliefs, speech rules, symbols, naming rule | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` |
| A-C-MATERIAL | examples/culture-d3/components/06-material.json | component: eras, materials, objects, costumes, rank rules | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` |
| A-C-EVIDENCE | examples/culture-d3/components/07-evidence.json | component: references, bridges, canon/handoff status, scope notes, screening | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` |
| A-CONTROLS | examples/culture-d3/controls.json | control expectations (3 positive / 16 domain / 4 malformed) | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` |
| A-FROZEN | examples/culture-d3/expected.json | freeze manifest: 24 computational input hashes, expected_exit 0, finding_ids [] | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` |
| A-TOOL-ASSEMBLE | tools/assemble-culture-d3.py | deterministic assembler (writes exactly packet.json + packet.gates.yml) | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| A-TOOL-GUARD | tools/check-evidence-coupling.py | evidence-coupling guard CLI (stdlib only) | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| A-TOOL-LABELS | tools/d2-typed-labels.py | typed-label projection tool (read-only over D2; used as cross-reference) | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| A-GATE-HANDOFF | tools/gates/handoff-packet-check.py | the adjacency gate this envelope is validated with | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| A-S01 | corpus/lessons/round-6-sources/05.json | closed source ledger, audit R6-05-A | `a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb` |
| A-S02+S03b | corpus/lessons/round-6-sources/03.json | closed source ledger, audit R6-03-B | `adb22c9a5f3acee621103c7b9dddeeb1eedba22d9e1d92081e37825b80560cea` |
| A-S03+S04 | corpus/lessons/round-6-sources/13.json | closed source ledger, audits R6-13-A and R6-13-B | `695043562e7e0caeda6693384baca060009c9e3feb2c108f5e8ea6bfc282d71a` |
| A-S05 | corpus/lessons/round-6-sources/09.json | closed source ledger, audit R6-09-A | `0dd2820d1e837b9ab5e503d21f1a891d367d873c9335f9dad80bef3c2da6ac94` |
| A-RECON | reports/round-6/parent-reconciliation.json | effective round-6 scope/kind/URL authority for S01–S05 | `1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162` |
| A-CONTRACT | corpus/knowledge/synthesis/worldbible-integration-contract.md | pinned adjacency contract (read-only) | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |

Live record counts (from `packet.json`, measured this session):
beliefs 2 · bridges 5 · costumes 4 · eras 2 · lexicon 20 · materials 3 ·
names 6 · objects 4 · rank_rules 1 · references 5 · sound_changes 1 ·
speech_rules 1 · symbols 2 · utterances 7 — 57 top-level records besides
`assembly`, `name`, `profile`, `canon_status`, `handoff_status`,
`naming_rule`, `phonology`, `scope_notes`, `screening`.

## dependency-manifest

- profile `kotodama-d3-evidence-coupling/1` (packet interface; guard CLI contract)
- SC1 sound law `/p/ > /f/`, initial, E0→E1, register `ordinary` (live `packet.sound_changes[0]`)
- AV1 avoidance rule: lexeme L01, era E1, register `ritual`, place `hall` → L02's E0 form (live `packet.speech_rules[0]`)
- NR1 naming-timing rule: allowed offsets [2, 8, 20] fictional-nights, chosen 8, source S03, status `constructed-not-historical` (live `packet.naming_rule`)
- RR1 hall rank rule: invented authority "Hall Wardens of the Two Benches"; prohibit material `plant-cloth` for `visitor` wearers, jurisdiction hall, rites `assembly`, era E1, no exemptions (live `packet.rank_rules[0]`)
- serializer dependency: `tools/assemble-d2.py` `yaml_lines` loaded read-only by the assembler, sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d
- closed evidence: five bindings over four ledger files plus the parent reconciliation digest, pinned in §artifact-manifest
- prerequisites: the pinned contract digest above; no floating `latest` references

## claim-ledger

| claim_id | kind | evidence_status | summary |
|---|---|---|---|
| CL01 | generative rule | constructed (design) | SC1: initial /p/ > /f/ separates E1 ordinary forms from E0 citation forms; ritual citation layer keeps E0 (live `sound_changes[0]`) |
| CL02 | generative rule | constructed (design) | AV1: L02's E0 form substitutes for L01 exactly in era E1 / register ritual / place hall; no generalized taboo (live `speech_rules[0]`) |
| CL03 | generative rule | constructed (design) | NR1: names may be given at 2, 8, or 20 fictional-nights, chosen offset 8 — a discrete constructed set, not a historical prescription (live `naming_rule`) |
| CL04 | generative rule | constructed (design) | RR1: the invented hall authority prohibits plant-cloth for visitors at hall assembly; C03 records a declared violation retained visibly (live `rank_rules[0]`, `costumes[2]`) |
| CL05 | sign rule | constructed (design) | SY01/SY02 sign→reading rules are audience- and era-scoped conventions of one fictional hall; no colour key and no universal meaning (live `symbols`) |
| CL06 | attributed in-world belief | unresolved in-world | B01 (record-bound claim) and B02 (voice-bound claim) disagree; both `truth_status: unresolved`; neither is a world-fact (live `beliefs`) |
| CL07 | designer interpretation | constructed (design) | E0→E1 staging, the two offices, and the invented hall authority are an author's design genealogy (live `scope_notes[0]`) |
| CL08 | real-world reference | effective R6 scope: partial-support | S01 (UT Hittite Online Lesson 2, secondary-scholarly, spotcheck P04) grounds BR01's method-transfer only (live `references[0]`) |
| CL09 | real-world reference | effective R6 scope: scoped-support | S02 (Louvre E 12026, museum-object, P02) grounds BR02's method-transfer; supplies no cut or pleating reconstruction (live `references[1]`) |
| CL10 | real-world reference | effective R6 scope: scoped-support | S03 (Gobhila II,8 via Oldenberg SBE 30, primary-text, P03) grounds BR03; the fictional offsets are not the historical timings (live `references[2]`) |
| CL11 | real-world reference | effective R6 scope: scoped-support | S04 (Śatapatha III,2,1 via Eggeling SBE 26, primary-text, P01) grounds BR04's analogy (live `references[3]`) |
| CL12 | real-world reference | effective R6 scope: partial-support | S05 (Stolper & Tavernier ARTA 2007.001, secondary-scholarly, P05 p. 9) grounds BR05's method-transfer (live `references[4]`) |
| CL13 | screening statement | unresolved | `screening.real_language_sweep_performed: false` — no real-language homophone or offensive-association sweep has been performed for any D3 spelling (live `screening`) |

## coupling-ledger

| edge_id | source | target | relation | justification (with recorded limits) |
|---|---|---|---|---|
| BR01 | S01 | U01, U02 | method-transfer | written citation form vs distinct spoken realization; design-only, no Hittite/Hattic scribal claim; S01 stays partial-support (live `bridges[0]`) |
| BR02 | S02 | C01, C02 | method-transfer | one object-level trait cannot be an exclusive era marker; no real textile history claimed (live `bridges[1]`) |
| BR03 | S03 | NR1 | method-transfer | discrete school-specific naming timings transferred as a closed set [2,8,20]; numbers invented (live `bridges[2]`) |
| BR04 | S04 | O01, O04 | analogy | sitting-surface vs worn-attachment distinction modelled as separate object slots; not a reconstruction of any rite (live `bridges[3]`) |
| BR05 | S05 | SY01, B01 | method-transfer | institution-specific record languages → audience/era-scoped symbol reading and one attributed, disagreeing account (live `bridges[4]`) |

## requested-decisions

Derived from the live D3 record set (the round-7 prose restatement lives in
`examples/culture-d3/handoff.md` §requested-decisions; `packet.json` itself
carries no decision records — see §assembly-notes). Every "accept" means
retain as reviewed non-canon candidate material; canon standing stays lore's.

| decision_id | question | alternatives | blocker |
|---|---|---|---|
| RD-01 | retain the 20-lexeme lexicon with its SC1 derivations as candidate world material? | accept / return per-record / reject | none |
| RD-02 | register B01/B02 as attributed in-world belief with unresolved truth status? | accept / reject the institution account | never import either as world-fact |
| RD-03 | adopt SY01/SY02 sign→reading rules with their declared hall/era/audience scoping? | accept / defer pending institution definition | none |
| RD-04 | adopt era staging E0/E1 as relative design coordinates without dates? | accept / require a calendar first | no calendar exists (OQ-R11-A1-05) |
| RD-05 | adopt the costume permission matrix including C03's declared RR1 violation? | accept as violation / return the rank rule | violation stays visible, never repaired |
| RD-06 | approve the six constructed names as candidate labels? | accept as candidates / defer | real-language sweep unperformed (OQ-R11-A1-01), blocking for official name approval |
| RD-07 | accept the five bridges as design-only edges with their recorded limits? | accept / reject contested-scope bridges | none |
| RD-08 | which receipt surface and lore baseline apply before any transfer? | no such surface exists yet | blocking for any import (contract §1/§8) |

## checks-run

Observed 2026-10-17 by this worker (read-only runs from the repository root;
`TMPDIR` set to the repo scratch dir; no outputs regenerated).

| command | exit | observed |
|---|---:|---|
| `python3 tools/assemble-culture-d3.py --check` | 0 | packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | counts.total 0, findings [], profile kotodama-d3-evidence-coupling/1 |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | 0 | findings [] against the live freeze manifest sha256:562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly CROSS-HOLD ×2 (unresolved sweep; no priority language named) + NAME-NEAR REVIEW ('E0' vs 'E1'); no phonology or derivation FAIL — expected hold, not a defect |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly one finding: R-01 [note] C03 declared RR1 violation kept visible; no R-02 — expected hold |
| `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-1.md` | 0 | fields=16/16 glossary-entries=20 findings=0 |
| `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-1.yml` | 0 | fields=16/16 glossary-entries=20 findings=0 (YAML serialization view) |

## open-questions

- OQ-R11-A1-01: real-language homophone/offensive-association sweep not performed for any constructed form; screening unresolved — kotodama pre-publication + lore; blocking for official name approval.
- OQ-R11-A1-02: no lore receipt, no baseline bible reference, no bilateral same-revision read record — both lanes; blocking for any canon import (contract §1, §8).
- OQ-R11-A1-03: cultural-permission limit — invented design; citation of real sources is not permission and no community consultation occurred (contract §10).
- OQ-R11-A1-04: historical/corpus residuals inherited from the closed bindings stay open (S01/S05 partial-support; S03/S04 translation-mediated, Sanskrit unread; round-6 unresolved rows unrepaired).
- OQ-R11-A1-05: no calendar or intercalation; era offsets are fictional-nights with no date calculation; blocking for era dating (contract §7).
- OQ-R11-A1-06: live-vs-filed digest disagreement — the round-7 handoff prose cites contract digest 50c4c2f2… and freeze manifest 74496aa8…; live bytes measure 5f4c02bf… and 562b76cb…. This packet pins the live values; the filed prose is history, not a correction target here.
- OQ-R11-A1-07: the parent acceptance-runner receipt is pending and is not declared passed; a freeze is not lore acceptance and not round completion.

## glossary payload (inline; assembled from the live packet.json lexicon, exactly 20 entries L01–L20)

Every either form and gloss is verbatim from the live packet (`packet.json`
`lexicon`); every etymology is `status: constructed` — an authored design
derivation by the declared sound law; no real-language derivation, borrowing,
or novelty-in-all-languages claim is made.

| entry_id | E0 form | E1 form | gloss | etymology |
|---|---|---|---|---|
| L01 | pina | fina | spoken pledge | status: constructed — E0 *pina → E1 fina by SC1 initial /p/ > /f/ (ordinary); available_from E0 |
| L02 | suma | suma | hearth invocation | status: constructed — E0 *suma, unchanged into E1 (no initial /p/); available_from E0 |
| L03 | talu | talu | record line | status: constructed — E0 *talu, unchanged into E1 (no initial /p/); available_from E0 |
| L04 | palu | falu | boundary token | status: constructed — E0 *palu → E1 falu by SC1 initial /p/ > /f/ (ordinary); available_from E0 |
| L05 | pira | fira | witness mark | status: constructed — E0 *pira → E1 fira by SC1 initial /p/ > /f/ (ordinary); available_from E0 |
| L06 | puka | fuka | gate announcement | status: constructed — E0 *puka → E1 fuka by SC1 initial /p/ > /f/ (ordinary); available_from E0 |
| L07 | tana | tana | thread count | status: constructed — E0 *tana, unchanged into E1 (no initial /p/); available_from E0 |
| L08 | kila | kila | measured fold | status: constructed — E0 *kila, unchanged into E1 (no initial /p/); available_from E0 |
| L09 | ruma | ruma | assembly seat | status: constructed — E0 *ruma, unchanged into E1 (no initial /p/); available_from E0 |
| L10 | masin | masin | marker cord | status: constructed — E0 *masin, unchanged into E1 (no initial /p/); available_from E0 |
| L11 | nisu | nisu | night tally | status: constructed — E0 *nisu, unchanged into E1 (no initial /p/); available_from E0 |
| L12 | lura | lura | hall passage | status: constructed — E0 *lura, unchanged into E1 (no initial /p/); available_from E0 |
| L13 | sina | sina | visitor sign | status: constructed — E0 *sina, unchanged into E1 (no initial /p/); available_from E0 |
| L14 | kalti | kalti | weft edge | status: constructed — E0 *kalti, unchanged into E1 (no initial /p/); available_from E0 |
| L15 | rusi | rusi | appointed token | status: constructed — E0 *rusi, unchanged into E1 (no initial /p/); available_from E0 |
| L16 | ami | ami | settlement | status: constructed — E0 *ami, unchanged into E1 (no initial /p/); available_from E0 |
| L17 | nara | nara | felt work-wrap | status: constructed — E0 *nara, unchanged into E1 (no initial /p/); available_from E0 |
| L18 | salu | salu | plain work-wrap | status: constructed — E0 *salu, unchanged into E1 (no initial /p/); available_from E0 |
| L19 | mila | mila | assembly robe | status: constructed — E0 *mila, unchanged into E1 (no initial /p/); available_from E0 |
| L20 | kuru | kuru | horn rank-clasp | status: constructed — E0 *kuru, unchanged into E1 (no initial /p/); available_from E0 |

## assembly-notes (worker R11-O06; not part of the envelope)

Hard-to-populate fields, and what each one required:

- `request_ref` and `baseline_bible_ref` — no live artifact carries either:
  there is no lore brief and no lore bible revision anywhere in the
  repository. Both must be authored as explicit `none` plus the unbound
  research declaration; the gate routes a bare `none` baseline to
  HO-BASELINE REVIEW, so the declaration wording is load-bearing.
- `subject_refs` — the only live content is the wildcard string
  `cand:kotodama.d3.*` in handoff prose; no concrete candidate IDs and no
  lore entity IDs exist. The field can be populated only as explicit
  unresolved candidates.
- `artifact_manifest` and the contract pin — digests must be measured from
  live bytes. Two filed-prose digests are stale: the contract moved in
  round-8 (commit e1694ba): 50c4c2f2… (filed) → 5f4c02bf… (live); the D3
  freeze manifest moved in round-9 (commit 9dc18ec): 74496aa8… (filed) →
  562b76cb… (live). Copied prose digests would have been wrong.
- `validation` — no machine-readable run receipts exist in the D2/D3
  directories; the filed handoff records round-7 runs. Populating this field
  requires actually re-running the commands (six runs recorded above).
- `requested_decisions` and `open_questions` — present only as handoff.md
  prose sections; `packet.json` carries no decision or question records, so
  an assembler reading only generated artifacts must derive them.
- `packet_id`, `packet_version`, `producer` — authored (none of them exist
  in live content); `recipient` is contract-fixed (contract §3).
- Not hard: `scope`, `dependency_manifest`, `claim_ledger`,
  `coupling_edges` — every row traces to `packet.json` records or the
  component files; the 20 glossary entries are the packet lexicon verbatim.
