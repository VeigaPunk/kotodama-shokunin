# Handoff packet — D3 "Source-Bounded Culture Drill" (deliberately unbound research packet; not canonized)

NON-CANON world-bible handoff packet, kotodama-shokunin → lore-shokunin,
assembled per `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(contract digest pinned below, §contract_ref; bilateral same-revision read
still pending). This is the D3 evidence-coupling drill: a bounded, invented
culture assembled only from the five closed round-6 source bindings by the
deterministic assembler `tools/assemble-culture-d3.py` and checked by the
evidence-coupling guard `tools/check-evidence-coupling.py` (profile
`kotodama-d3-evidence-coupling/1`). This revision describes the actual
assembled packet bytes; it supersedes the round-7 scribe's earlier 0.1.0
draft serialization, whose L04–L16 lexemes, names, and bridge relations were
proposals that differ from the assembled packet. Nothing here is canon, a
world-bible entry, or lore acceptance; canon standing is lore's alone. Era
coordinates E0/E1 are fixture-relative, not BCE/CE and not a reconstructed
civilization. All native spellings are constructed and unscreened ASCII
lowercase; no real-language clearance, community consultation, or cultural
permission is claimed, performed, or granted.

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)
- handoff_status: prepared-not-accepted (envelope structurally valid; no lore receipt exists)

| field | value |
|---|---|
| packet_id | kotodama.handoff.d3-source-bounded-drill |
| packet_version | 0.3.0-draft.md (supersedes the 0.1.0/0.2.0 scribe drafts; freeze manifest expected.json present and the packet-vs-frozen guard run observed exit 0 — see artifact_manifest and validation; final acceptance-run receipt pending) |
| contract_ref | kotodama-lore-adjacency 1.0.0, contract digest sha256:50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1 (§1 pin, re-measured 2026-10-17 from current bytes; bilateral read pending per contract §1/§8) |
| producer | kotodama-shokunin (round-7 D3 workstream; generative craft, evidence-coupling records, and design only) |
| recipient | lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency) |
| request_ref | none — no lore brief exists; assembled as a deliberately unbound research drill (contract §4) |
| baseline_bible_ref | none — deliberately unbound research packet; cannot be imported as canon without a lore baseline and a new reviewed handoff (contract §4) |
| artifact_manifest | packet record examples/culture-d3/packet.json sha256:bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829 — full table of 17 measured artifact digests (4 components, packet, legacy projection, controls, freeze manifest, 2 tools, serializer, 4 closed ledgers, parent reconciliation, contract) in §artifact-manifest below; record counts 2 eras / 20 lexemes / 6 names / 7 utterances / 2 beliefs / 2 symbols / 3 materials / 4 objects / 4 costumes / 1 rank rule / 5 references / 5 bridges |
| subject_refs | namespaced candidate refs `cand:kotodama.d3.*` (language variety, record-keeper office, voice-of-the-record office, hall assembly institution); all unresolved — no lore entity ids supplied |
| scope | D3 source-bounded culture drill: two fictional eras E0 (citation/union stage) and E1 (ordinary-speech stage); 20 constructed lexemes L01–L20; 6 constructed names N01–N06 (lineage/office/place/personal); 7 utterances U01–U07; 2 attributed beliefs B01/B02; 2 audience-scoped symbols SY01/SY02; 3 materials M01–M03; 4 objects O01–O04; 4 costumes C01–C04 (one declared violation); 1 sound law SC1; 1 avoidance rule AV1; 1 timing rule NR1; 1 rank rule RR1; 5 references S01–S05; 5 bridges BR01–BR05; no real place; ASCII lowercase spellings only |
| dependency_manifest | profile kotodama-d3-evidence-coupling/1; SC1 /p/ > /f/ initial E0→E1 ordinary; AV1 L01→L02 ritual/hall; NR1 offsets [2,8,20] chosen 8 fictional-nights; RR1 hall plant-cloth visitor prohibition; serializer tools/assemble-d2.py (yaml_lines loaded read-only) sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d; four closed ledger-file digests for five bindings + parent reconciliation digest pinned in §artifact-manifest; no floating `latest` |
| claim_ledger | CL01–CL13 in §claim-ledger below — constructed-rule, attributed-belief (unresolved), designer-interpretation, and real-world-reference claims with effective round-6 scopes |
| coupling_edges | BR01–BR05 in §bridge-ledger below — relation `method-transfer` (BR01, BR02, BR03, BR05) and `analogy` (BR04), all `asserted_scope: design-only` |
| requested_decisions | RD-01–RD-08 in §requested-decisions below — per-record accept/defer/reject questions for lore; "accept" always means retain as non-canon candidate material, never canonize |
| validation | actual observed runs of 2026-10-17 recorded in §validation (assembler --check exit 0 byte-identical; guard exit 0 findings []; selftest exit 0 — controls.json's 3 positive / 16 domain / 4 malformed cases all passed plus 2 CLI baseline positives and 5 frozen fixtures; legacy naming exit 1 CROSS-HOLD+NAME-NEAR; legacy costume exit 1 R-01 only; frozen guard run exit 0 findings [] against expected.json); the final acceptance-runner receipt remains pending and is not declared passed |
| open_questions | OQ-D3-01…06 in §open-questions below — real-language sweep unperformed, no lore receipt, permission limits, inherited historical residuals (incl. the four round-6 unresolved rows), no calendar, acceptance-runner receipt pending |

## artifact-manifest

Every digest below is **measured** (sha256sum, 2026-10-17) from the actual
bytes named. One path per row — 17 rows, all measured, none pending. The
four component digests equal the packet's own `assembly.source_sha256` block
byte-for-byte; the serializer digest equals `assembly.serializer_sha256`.
The single row `corpus/lessons/round-6-sources/13.json` carries both closed
bindings S03 (R6-13-A) and S04 (R6-13-B). `examples/culture-d3/expected.json`
is the parent-owned freeze manifest: 24 computational input hashes with
predeclared `expected_exit: 0` / `finding_ids: []`, deliberately excluding
this handoff document and the directory README — documentation surfaces stay
**outside the computational freeze** (no self-digest cycle); parent
acceptance pins their final hashes.

| artifact id | path | role | sha256 |
|---|---|---|---|
| A-PACKET | examples/culture-d3/packet.json | assembled deterministic packet (sorted keys, indent 2, final newline) | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| A-GATES | examples/culture-d3/packet.gates.yml | legacy projection (native forms only; trace mapping + 8 projection limits under assembly) | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| A-C-LANG | examples/culture-d3/components/04-language.json | component: phonology, lexicon, names, sound_changes, utterances | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| A-C-RITUAL | examples/culture-d3/components/05-ritual.json | component: beliefs, speech_rules, symbols, naming_rule | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` |
| A-C-MATERIAL | examples/culture-d3/components/06-material.json | component: eras, materials, objects, costumes, rank_rules | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` |
| A-C-EVIDENCE | examples/culture-d3/components/07-evidence.json | component: references, bridges, canon_status, handoff_status, scope_notes, screening | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` |
| A-CONTROLS | examples/culture-d3/controls.json | control expectations: 3 positive / 16 domain / 4 malformed (selftest additionally runs 2 CLI baseline positives and 5 frozen fixtures) | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` |
| A-FROZEN | examples/culture-d3/expected.json | parent-owned freeze manifest: 24 computational input hashes, predeclared expected_exit=0, finding_ids=[]; handoff/README deliberately excluded | `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` |
| A-TOOL-ASSEMBLE | tools/assemble-culture-d3.py | deterministic assembler (writes exactly packet.json + packet.gates.yml; --check read-only) | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| A-TOOL-GUARD | tools/check-evidence-coupling.py | evidence-coupling guard CLI (stdlib only; no eval/network; snapshot mode) | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| A-SERIALIZER | tools/assemble-d2.py | dependency: yaml_lines serializer loaded read-only by the assembler | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| A-S01 | corpus/lessons/round-6-sources/05.json | closed source ledger, audit R6-05-A | `a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb` |
| A-S02 | corpus/lessons/round-6-sources/03.json | closed source ledger, audit R6-03-B | `adb22c9a5f3acee621103c7b9dddeeb1eedba22d9e1d92081e37825b80560cea` |
| A-S03+S04 | corpus/lessons/round-6-sources/13.json | closed source ledger, audits R6-13-A and R6-13-B | `695043562e7e0caeda6693384baca060009c9e3feb2c108f5e8ea6bfc282d71a` |
| A-S05 | corpus/lessons/round-6-sources/09.json | closed source ledger, audit R6-09-A | `0dd2820d1e837b9ab5e503d21f1a891d367d873c9335f9dad80bef3c2da6ac94` |
| A-RECON | reports/round-6/parent-reconciliation.json | effective round-6 scope/kind/URL authority for S01–S05 | `1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162` |
| A-CONTRACT | corpus/knowledge/synthesis/worldbible-integration-contract.md | pinned adjacency contract (read-only) | `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` |

## dependency-manifest

- profile `kotodama-d3-evidence-coupling/1` (packet interface; guard CLI contract)
- SC1 sound law /p/ > /f/, initial, E0→E1, register `ordinary`, applied once at word start only (constructed; packet `sound_changes[0]`)
- AV1 avoidance rule: lexeme L01, era E1, register `ritual`, place `hall` → substitute lexeme L02's E0 form (constructed; packet `speech_rules[0]`; exactly this place/register, no generalized taboo)
- NR1 naming-timing rule: allowed_offsets [2, 8, 20] fictional-nights, chosen_offset 8, source S03, `constructed-not-historical` (the fictional numbers deliberately differ from Gobhila's 10 nights / 100 nights / one year)
- RR1 hall rank rule: authority "Hall Wardens of the Two Benches (invented fictional hall authority)"; prohibit material `plant-cloth` for `visitor` wearers, jurisdiction hall, rite assembly, era E1, no exemptions (C03 retains this as a declared violation, never a lawful case)
- Serializer dependency: `tools/assemble-d2.py` `yaml_lines` loaded read-only by the assembler (no third-party YAML dependency), digest pinned in §artifact-manifest
- Projection adapter note: the component's `coda_subset` is additionally projected as legacy `phonology.coda` so the naming gate enforces the declared coda inventory (recorded in the packet's `assembly.legacy_projection.limits`)
- Fixture anchors: L01 `pina`, L02 `suma`, L03 `talu`, L17 `nara`, L18 `salu`, L19 `mila`, L20 `kuru` (E0 forms); M01 `felt`, M02 `plant-cloth`, M03 `horn`; costume lexemes C01=L17, C02=L18, C03=L19, C04=L20
- prerequisites: the six closed evidence digests above; the pinned contract digest; no floating version references

## claim-ledger

| claim_id | kind | evidence_status | summary |
|---|---|---|---|
| CL01 | generative rule | invented | SC1 /p/ > /f/ word-initially, ordinary register, separates E1 spoken forms from E0 citation forms (L01 `pina`→`fina`; L04 `palu`→`falu`; L05 `pira`→`fira`; L06 `puka`→`fuka`); the ritual citation layer retains E0 forms |
| CL02 | generative rule | invented | AV1 substitutes L02's E0 form `suma` for L01 exactly in era E1 / register `ritual` / place `hall` (witnessed by U02); no generalized taboo outside that place/register |
| CL03 | generative rule | invented | NR1 names may be given at 2, 8, or 20 fictional nights, chosen offset 8 — a constructed discrete set, explicitly not Gobhila's historical timings |
| CL04 | generative rule | invented | RR1 (Hall Wardens of the Two Benches, invented authority) prohibits M02 plant-cloth for visitors in hall assembly (E1); costume C03 records a declared violation of it, retained visibly, not repaired |
| CL05 | generative rule | invented | SY01/SY02 sign→reading rules are audience- and era-scoped constructed conventions of one fictional hall; no colour key and no universal meaning asserted |
| CL06 | attributed in-world belief | invented (contested in-fiction) | B01 (a retired E1 hall usher, via the fictional Ushers' Miscellany): only a claim bound into the hall's cord-record can be pressed against a house; speaking aloud merely announces the binding. B02 (an itinerant E1 tally-reader, opposing account): the cord-bindings are only payout tallies; a claim binds when the voice-of-the-record office speaks it aloud. Both `truth_status: unresolved`; no narrator-certified supernatural event, no copied real rite |
| CL07 | designer interpretation | invented | The E0→E1 staging, the two fictional offices, and the invented hall authority are an author's design genealogy, not a reconstruction of any real civilization (explicitly not Vedic consecration) |
| CL08 | real-world reference | effective round-6 scope: partial-support | S01 (UT Hittite Online Lesson 2, effective kind `secondary-scholarly`, parent spotcheck P04): written Akkadogram vs stated Hittite reading and cult-provenance layering — grounds BR01's method-transfer only; Hattic genealogy legs stay unsupported |
| CL09 | real-world reference | effective round-6 scope: scoped-support | S02 (Louvre E 12026 record, `museum-object`, P02): pleated linen before the New Kingdom as object-level evidence — grounds BR02's method-transfer; supplies no cut, no pleating reconstruction, no universal wearing law |
| CL10 | real-world reference | effective round-6 scope: scoped-support | S03 (Gobhila II,8 in Oldenberg SBE 30 via the parent-pinned Wayback capture, `primary-text`, P03): school-specific discrete naming timings — grounds BR03's method-transfer; the fictional offsets are not the historical prescription |
| CL11 | real-world reference | effective round-6 scope: scoped-support | S04 (Śatapatha III,2,1 in Eggeling SBE 26, `primary-text`, P01): ground sitting-surface vs garment-attached horn, school difference footnote-mediated — grounds BR04's analogy; not a copied rite |
| CL12 | real-world reference | effective round-6 scope: partial-support | S05 (Stolper & Tavernier ARTA 2007.001, `secondary-scholarly`, parent locator correction P05 to printed page 9): institution-specific practical record vs universal speech — grounds BR05's method-transfer; the isolate may not demonstrate general use |
| CL13 | screening statement | unresolved | `screening: {status: unresolved, real_language_sweep_performed: false}` — no real-language homophone/offensive-association sweep has been performed for any D3 spelling; no clearance exists or may be inferred |

## constructed glossary (inline; L01–L20, exact packet lexicon)

All rows are verbatim from the assembled packet (`packet.json` lexicon, 20
records): E0 native citation form, computed E1 ordinary form, packet gloss.
Every etymology is `status: constructed` — an authored design derivation by
the declared sound law; no real-language derivation, borrowing, or
novelty-in-all-languages claim is made. Initial-p lexemes: L01, L04, L05, L06
(four ≥ three required). Unchanged lexemes: sixteen (≥ three required).

| entry_id | E0 form | E1 form | gloss (packet) | etymology |
|---|---|---|---|---|
| L01 | pina | fina | spoken pledge | status: constructed — E0 *pina 'spoken pledge' → E1 fina by SC1 initial /p/ > /f/ (ordinary register); E0 form retained as ritual citation form and as every L01 written_form |
| L02 | suma | suma | hearth invocation | status: constructed — E0 *suma, unchanged into E1 (no initial /p/); supplies AV1's ritual substitute form |
| L03 | talu | talu | record line | status: constructed — E0 *talu, unchanged into E1; readable in ordinary and ritual contexts without any avoidance trigger |
| L04 | palu | falu | boundary token | status: constructed — E0 *palu → E1 falu by SC1 initial /p/ > /f/ |
| L05 | pira | fira | witness mark | status: constructed — E0 *pira → E1 fira by SC1 initial /p/ > /f/ |
| L06 | puka | fuka | gate announcement | status: constructed — E0 *puka → E1 fuka by SC1 initial /p/ > /f/ |
| L07 | tana | tana | thread count | status: constructed — E0 *tana, unchanged into E1 |
| L08 | kila | kila | measured fold | status: constructed — E0 *kila, unchanged into E1 |
| L09 | ruma | ruma | assembly seat | status: constructed — E0 *ruma, unchanged into E1 |
| L10 | masin | masin | marker cord | status: constructed — E0 *masin (coda /n/ within the declared coda subset), unchanged into E1 |
| L11 | nisu | nisu | night tally | status: constructed — E0 *nisu, unchanged into E1; supports NR1's fictional-nights unit |
| L12 | lura | lura | hall passage | status: constructed — E0 *lura, unchanged into E1 |
| L13 | sina | sina | visitor sign | status: constructed — E0 *sina, unchanged into E1 |
| L14 | kalti | kalti | weft edge | status: constructed — E0 *kalti (closed first syllable, coda /l/ licensed), unchanged into E1 |
| L15 | rusi | rusi | appointed token | status: constructed — E0 *rusi, unchanged into E1 |
| L16 | ami | ami | settlement | status: constructed — E0 *ami, unchanged into E1 |
| L17 | nara | nara | felt work-wrap | status: constructed — E0 *nara, unchanged into E1; costume lexeme of C01 (E0) and the M01 work-garment line |
| L18 | salu | salu | plain work-wrap | status: constructed — E0 *salu, unchanged into E1; costume lexeme of C02 |
| L19 | mila | mila | assembly robe | status: constructed — E0 *mila, unchanged into E1; costume lexeme of C03, the declared RR1 violation |
| L20 | kuru | kuru | horn rank-clasp | status: constructed — E0 *kuru, unchanged into E1; costume lexeme of C04, the lawful appointed attachment |

## constructed names (N01–N06, exact packet names)

Formation: concat of the two bases' **E1** forms (guard-verified to yield the
declared native form), era E1 for all six. Display labels are the packet's
English explanatory labels, never native-name claims. All six are mutually
distinct and none equals a lexeme or costume form.

| name_id | bases (E1 concat) | native_form | type | display_label (packet, English) |
|---|---|---|---|---|
| N01 | L02 + L03 (suma + talu) | sumatalu | lineage | lineage name: hearth-record line |
| N02 | L08 + L11 (kila + nisu) | kilanisu | lineage | lineage name: measured fold and night tally |
| N03 | L04 + L12 (falu + lura) | falulura | office | office name: boundary token of the hall passage |
| N04 | L09 + L05 (ruma + fira) | rumafira | office | office name: assembly seat witness mark |
| N05 | L16 + L20 (ami + kuru) | amikuru | place | place name: settlement horn-clasp mark |
| N06 | L06 + L13 (fuka + sina) | fukasina | personal | personal name: gate announcement visitor sign |

## utterances (U01–U07, exact packet utterances)

Register law as declared: ordinary readings use the SC1-changed E1 form;
ritual readings use the E0 citation form unless the exactly matching AV1
substitutes L02's E0 form; written_form is always the original lexeme's E0
form. U07 witnesses that L01 in the hall stays ordinary-lawful (`fina`)
outside the ritual register — avoidance is place/register-limited, never a
generalized taboo.

| id | lexeme | era | register | place | spoken_form | written_form |
|---|---|---|---|---|---|---|
| U01 | L01 | E1 | ordinary | market | fina | pina |
| U02 | L01 | E1 | ritual | hall | suma | pina |
| U03 | L03 | E1 | ordinary | market | talu | talu |
| U04 | L03 | E1 | ritual | hall | talu | talu |
| U05 | L04 | E1 | ordinary | market | falu | palu |
| U06 | L02 | E1 | ritual | hall | suma | suma |
| U07 | L01 | E1 | ordinary | hall | fina | pina |

## bridge-ledger (source → invention; exactly BR01–BR05, all design-only)

Actual relations and targets from the assembled packet: four
`method-transfer` edges and one `analogy`. A partial source stays partial: no
bridge asserts recovered native forms, ancient authenticity, genealogy, or
cross-version monument claims.

| bridge | source (effective scope/kind) | relation | target_ids | mechanism (design transfer) | limits (what is NOT claimed) |
|---|---|---|---|---|---|
| BR01 | S01 (partial-support, secondary-scholarly; P04) | method-transfer | U01, U02 | S01's retrieved lesson gloss marks a written Akkadogram (IṢ-BAT) whose stated Hittite reading differs (ēpta): one written citation form with a distinct spoken realization. D3 copies only that separation: U01/U02 both write L01's E0 citation spelling `pina` as written_form, while the market-ordinary reading uses the SC1-changed E1 form and the hall-ritual reading is governed by the exactly matching AV1 substitute | The written-layer-plus-register coupling is a declared rule of a fictional language, not a claim about Hittite/Hattic scribal practice; mediated English teaching prose; no autograph or Hattic-language text read; Hattic genealogy legs stay unsupported and the source stays partial |
| BR02 | S02 (scoped-support, museum-object; P02) | method-transfer | C01, C02 | S02's museum record dates a pleated linen tunic to late Dynasty 11–early Dynasty 12, a garment feature attested before the period it is sometimes used to date: one object-level trait cannot be an exclusive era marker. D3 transfers that caution — C01 (E0) and C02 (E1) keep the same M01 felt work-garment silhouette, so the two fictional eras are not distinguishable by a single decorative feature; era assignment rides on declared material routes, not object appearance | Design-only on a fictional felt garment; no real textile history claimed and no statement about pleats, linen or felt in any real tradition; museum record carries its own dating caveat; no independent re-dating; field transcription, not running prose; no cutting or pleating reconstruction |
| BR03 | S03 (scoped-support, primary-text; P03) | method-transfer | NR1 | S03 shows a naming-rite timing given as a discrete, school-specific set of named alternatives (ten nights, a hundred nights, or one year) inside one translated grihya prescription. D3 transfers the method, not the numbers: NR1 declares a closed discrete set [2, 8, 20] fictional-nights with chosen offset 8, guard-checkable as a unique integer set | Offsets, unit and chosen value invented; no claim that Gobhila or any school prescribed 2, 8 or 20 nights; no universal ancient practice; translation-mediated English (Oldenberg 1892, including a conjectural emendation), Sanskrit unread; one school's domestic-rule text |
| BR04 | S04 (scoped-support, primary-text; P01) | analogy | O01, O04 | S04 distinguishes, inside one school's translated prescription, skins spread on the ground as a sitting surface (III,2,1.1–9) from a horn tied to the end of a garment as a worn attachment (III,2,1.18). D3 models the surface-versus-worn distinction as separate object slots: O01 ground-surface worn=false, O04 worn attachment worn=true, and the object system forbids a ground surface from becoming a worn garment | O01/O04 belong to an invented office/display system, not a reconstruction of Vedic consecration; no rite, embryo/womb analogy or world symbolism copied; English translation only (Eggeling 1885); the Mādhyandina/Kāṇva attachment difference is known through the translator's footnote; kṛṣṇājina denotes the skin, not the horn; no pan-Vedic dress or immutable black/white symbolism |
| BR05 | S05 (partial-support, secondary-scholarly; P05, printed p. 9) | method-transfer | SY01, B01 | S05 shows an archive in which daily records ran overwhelmingly in Elamite (~15,000–18,000 documents) while a single Old Persian administrative tablet is explicitly described as an isolate that may not demonstrate general use: record languages are institution-specific, and one exceptional record does not universalize a medium. D3 transfers that separation: SY01's reading is scoped to a declared audience and era instead of a universal meaning key, and B01 is one attributed, disagreeing account of a record/voice institution with unresolved truth status | SY01/B01 are constructed attributed fiction; nothing asserted about real Persian religion, Achaemenid administration or subject populations' speech; Behistun cross-version leg and all-subject speech claims unverified; ARTA is mediation, not the archival documents and not confirmation of any unread original |

## requested-decisions

Per-record accept/defer/reject questions with mutually exclusive
alternatives; partial acceptance per record is allowed, and no accepted label
may depend on an unaccepted rule (contract §8 step 8). **Every "accept"
below means: retain as reviewed non-canon candidate material — canon standing
stays lore's alone and none of these decisions requests canonization.**

- RD-01: accept the 20-lexeme packet lexicon and 6-name set as candidate world material (derivations guard-verified), or return any record to the language owner.
- RD-02: register B01/B02 as attributed in-world belief with unresolved truth status, or reject the institution account — never import either as world-fact.
- RD-03: adopt SY01/SY02 sign→reading rules with their declared hall/era/audience scoping, or defer pending in-world institution definition.
- RD-04: adopt era staging E0/E1 as relative design coordinates without dates, or require a calendar first (none exists — OQ-D3-05).
- RD-05: adopt the costume permission matrix including C03's declared RR1 violation (kept visible, not repaired), or return the rank rule.
- RD-06: approve/decline the six constructed names as candidate labels with the real-language sweep still unperformed (blocking for official name approval).
- RD-07: accept the five bridges as design-only method-transfer/analogy edges with their recorded limits, or reject any bridge whose scope is contested.
- RD-08: which receipt surface and lore baseline apply before any transfer (none exists; bilateral same-revision read pending) — blocking for any import.

## validation

**Observed runs, 2026-10-17, all read-only executions by this scribe** (tool
hashes in §artifact-manifest; no outputs were regenerated this session):

```sh
python3 tools/assemble-culture-d3.py --check
# exit 0 — "packet.json: byte-identical deterministic assembly;
#           packet.gates.yml: byte-identical deterministic assembly"

python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json
# exit 0 — {"counts":{"total":0},"exit":0,"findings":[],
#           "profile":"kotodama-d3-evidence-coupling/1"}

python3 tools/check-evidence-coupling.py --selftest
# exit 0 — selftest_passed=true; positive_controls 5/5 = controls.json's
#   3 positive cases (translated-costume-label, ordinary-place-change,
#   belief-reword all stay clean) + 2 CLI baseline positives (repo-cwd,
#   foreign-cwd); domain_controls 16/16 covering all 14 non-DATA
#   diagnostics (16 cases over 14 diagnostic ids); malformed_controls 4/4
#   (exit 2 each: invalid-json, invalid-utf8, wrong-root, missing-file);
#   frozen_checks 5/5 (good=0; tampered-digest/unknown-entry/
#   bool-expected×2 = exit 2 D3-SNAPSHOT)

python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml
# exit 1 — exactly: CROSS-HOLD ×2 (unresolved real-language sweep; no
#   priority language/community named) + NAME-NEAR REVIEW ('E0' vs 'E1',
#   1 edit apart, recall-oriented, not a confusion verdict);
#   NO phonology-sanity FAIL and NO derivation FAIL

python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml
# exit 1 — exactly one finding: R-01 [note] C03 declared RR1 violation
#   (plant-cloth visitor at hall assembly) kept visible; no R-02

python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
# exit 0 — {"counts":{"total":0},"exit":0,"findings":[],
#           "profile":"kotodama-d3-evidence-coupling/1"}
#   against expected.json sha256:74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f
#   600fd74bfeab5480adf5080 (24 computational input hashes verified before
#   verdict; handoff/README deliberately outside the freeze)

python3 tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md
# final observed run for this revision: exit 0 — fields=16/16,
#   glossary-entries=20, findings=0
```

Still pending, honestly not run: the parent acceptance runner's final round
receipt. Freeze verification is not that receipt, not lore acceptance, and
not round completion — the freeze manifest pins computational inputs only,
and no canon, promotion, or completion claim is made anywhere in this
packet.

Guard semantics (contract-pinned, and now observed above): exit 0 valid
bounded model; exit 1 demonstrated profile contradiction with stable finding
ids (D3-CANON, D3-REFERENCE, D3-DIGEST, D3-SCOPE, D3-NATIVE,
D3-DERIVATION, D3-UTTERANCE, D3-TIMING, D3-MYTH, D3-OBJECT, D3-ERA,
D3-RANK, D3-BRIDGE, D3-SYMBOL); exit 2 could-not-evaluate (D3-DATA,
D3-SNAPSHOT), never a traceback. The guard writes no inputs/reports at
normal runs, follows no input-supplied paths outside the closed bindings,
and makes no network requests. Expected legacy holds are confirmed actual
outcomes, not targets to fix: CROSS-HOLD exit 1 (similarity stays a recorded
review, never disabled to buy green), C03's R-01 exit 1, and this envelope
passes structurally while remaining not canonized. Local
generation/derivation checks are not bible-wide consistency and not canon
certification.

## open-questions

- OQ-D3-01: real-language homophone/offensive-association sweep not performed on any constructed form — kotodama pre-publication + lore; blocking for official name approval (screening unresolved). The two CROSS-HOLD review records also name no priority language/community; a bounded sweep must record the languages, channels and date actually searched.
- OQ-D3-02: no lore receipt, no baseline bible reference, and no bilateral same-revision read record exist — both lanes; blocking for any canon import (contract §1, §8).
- OQ-D3-03: cultural-permission limit — this packet is invented design; citation of real sources is not permission, and no community consultation occurred or is claimed; restricted material stays held (contract §10).
- OQ-D3-04: historical/corpus residuals inherited from the closed bindings remain open: Oldenberg's §14 emendation and untranslated Sanskrit (S03); the Kāṇva attachment difference known only through Eggeling's footnote (S04); Hattic genealogy legs and the monographs unread (S01); no independent tomb-group re-dating or cutting reconstruction (S02); Behistun cross-version and subject-speech legs unverified (S05). The four round-6 unresolved rows (R6-02-A, R6-02-B, R6-05-B, R6-07-A) and the fifteen round-5 residual questions stay open; R6-09-B remains partial-support and is not relabeled; nothing here closes them.
- OQ-D3-05: calendar and intercalation unsolved — era offsets are fictional-nights with no date calculation; blocking for any era dating (contract §7).
- OQ-D3-06: resolved this revision — `examples/culture-d3/expected.json` is present (sha256:74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080; 24 computational input hashes; handoff/README deliberately outside the freeze) and the packet-vs-frozen guard run is observed exit 0 / findings []. What remains pending is the parent acceptance runner's final round receipt — legitimately pending, never declared passed. This packet_version stays `*-draft` until that receipt; a freeze is not lore acceptance and not completion of the round arc.

## scope-notes

- Invented genealogy: every D3 native spelling, lexeme, name, utterance and derived form is constructed fiction; no derivation from, alignment with, or recovery of any real language is claimed, and no form is asserted novel across all real languages.
- Cultural-permission limit: no real community, tradition-holder or cultural authority was consulted; institutional patterns in the cited sources are abstracted as design-only methods; no sacred rite, symbol or practice is reproduced, certified, or claimed as culturally authentic or authorized.
- No lore receipt: NON-CANON, handoff_status prepared-not-accepted; submission, delivery, and silence are never acceptance (contract §8).
- Unresolved historical/corpus residuals: S01 and S05 remain partial-support; S03 and S04 are translation-mediated with the Sanskrit unread; inherited residuals stay open (OQ-D3-04) and are repaired by nothing here.
- No canon and no promotion: all reviews are author-side; kotodama never records canon standing, which is lore's alone.
