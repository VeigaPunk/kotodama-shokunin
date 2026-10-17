# Handoff packet — D2/D3 dual-drill exercise (deliberately unbound research packet; not canonized)

NON-CANON handoff packet, kotodama-shokunin → lore-shokunin, assembled by `tools/exercise-handoff-e2e.py` from the live lane artifacts named in §artifact_manifest: the D2 highland-pastoralist design drill and its typed-label projection, and the D3 source-bounded culture drill with its legacy gate projection. Every field below is derived from those files at assembly time; no prose about the two drills is hand-authored here. This is an operability exercise, not a delivery: no lore brief, no baseline bible and no receipt surface exist, and no canon standing is asserted here. Canon standing is lore's alone (contract §6, §8.7). All native spellings are constructed and unscreened ASCII lowercase; no real-language clearance, community consultation, or cultural permission is claimed, performed, or granted.

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)
- handoff_status: prepared-not-accepted (live value from examples/culture-d3/packet.json: `prepared-not-accepted`; canon status `NON-CANON`)

| field | value |
|---|---|
| packet_id | kotodama.handoff.d2d3-e2e |
| packet_version | 1.0.0 (pure function of the pinned read set; no wall-clock content) |
| contract_ref | kotodama-lore-adjacency 1.0.0, contract digest sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 (§1 pin, re-measured at assembly time from corpus/knowledge/synthesis/worldbible-integration-contract.md; the bilateral same-revision read is still pending) |
| producer | kotodama-shokunin (round-11 handoff-e2e exercise; generative craft and design records only) |
| recipient | lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency) |
| request_ref | none — no lore brief exists; assembled as a deliberately unbound research drill (contract §4) |
| baseline_bible_ref | none — deliberately unbound research packet; cannot be imported as canon without a lore baseline and a new reviewed handoff (contract §4) |
| subject_refs | 8 namespaced candidates, all unresolved — no lore entity ID was supplied and none is guessed (contract §4): `cand:kotodama.d3.language-variety` (witness: examples/culture-d3/packet.json lexicon L01–L20, 20 constructed lexemes), `cand:kotodama.d3.record-keeper-office` (witness: belief B01 attributed to a retired E1 hall usher, as quoted in the fictional Ushers'…), `cand:kotodama.d3.voice-of-the-record-office` (witness: belief B02 attributed to an itinerant E1 tally-reader who worked the same hall's market days,…), `cand:kotodama.d3.hall-assembly-institution` (witness: rank rule RR1 jurisdiction `hall`), `cand:kotodama.d2.culture` (witness: examples/culture-d2/packet.d2.yml name "D2 highland pastoralists — round-3 design drill"), `cand:kotodama.d2.pasture-lineage-institution` (witness: lexicon L-04 `las`), `cand:kotodama.d2.archaic-sky-holder` (witness: pantheon PAN-01 `Halatu`), `cand:kotodama.d2.open-grazing-era` (witness: era record ER-01 "E0 Open Grazing") |
| scope | two unbound design drills, no real place and no dates: D2 "D2 highland pastoralists — round-3 design drill" (eras E0/E1/E2/E3, 40 lexicon records, 8 names, 10 costumes, 9 materials, everyday/ritual/ledger registers, read-only input bytes); D3 examples/culture-d3/packet.json (E0/E1 fixture-relative eras, 20 lexemes, 6 names, 7 utterances, 2 attributed beliefs, 2 symbols, 4 costumes — one declared rank-rule violation — 5 design-only bridges, ordinary/ritual registers); all native spellings are constructed ASCII-lowercase, unscreened, with no ISO code or real language family claimed |

## delivered record sets

The per-set scope detail behind the one-line §scope above, read out of the two packets: every record set is a bounded design construction with no real-world referent asserted.

| record set | source artifact | culture group / region | variety / script | register context | era applicability |
|---|---|---|---|---|---|
| D2 drill records | examples/culture-d2/packet.d2.yml | D2 highland pastoralists — round-3 design drill (highland pastoral, stipulated; no real place) | invented variety; ASCII-lowercase spellings, no ISO code claimed | everyday, ritual and ledger registers | E0/E1/E2/E3 (fixture-relative, not BCE/CE) |
| D3 drill records | examples/culture-d3/packet.json | source-bounded culture drill; one invented hall settlement (no real place) | invented ordinary and ritual citation layers; ASCII-lowercase spellings, no ISO code claimed | ordinary and ritual registers (avoidance rule AV1 scoped to place `hall`) | E0/E1 (fixture-relative, not BCE/CE) |
| glossary payload | examples/culture-d3/packet.json | as above | 20 constructed lexemes with E0 citation and computed E1 ordinary forms | avoidance applies in the ritual register only | E0→E1 |

## artifact_manifest

Every digest below was re-measured (sha256) at assembly time from the bytes on disk — the gate checks digest presence only, this exercise checks equality (design §1). 21 read-set files plus one inline-payload row; the D2 and D3 drills carry no declared packet version, so their bytes are pinned by digest alone.

| artifact_id | path | role | sha256 | records |
|---|---|---|---|---|
| A-01 | corpus/knowledge/synthesis/worldbible-integration-contract.md | pinned adjacency contract §1/§4 authority; interface revision 1.0.0; 16 §4 field names parsed from it | 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 | 28,421 bytes |
| A-02 | examples/culture-d3/packet.json | d3 evidence-coupling payload: 20 lexemes / 6 names / 7 utterances / 2 beliefs / 2 symbols / 3 materials / 4 objects / 4 costumes / 1 rank rule / 5 references / 5 bridges | bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829 | 37,222 bytes |
| A-03 | examples/culture-d3/packet.gates.yml | d3 legacy projection: 12 top-level sections, constructed native forms only in the gate-facing slots | 306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425 | 14,191 bytes |
| A-04 | examples/culture-d3/controls.json | d3 guard control expectations: 4 control classes | f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70 | 7,219 bytes |
| A-05 | examples/culture-d3/expected.json | d3 freeze manifest: 24 computational input hashes; declared exit 0; handoff/README deliberately excluded | 562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc | 3,626 bytes |
| A-06 | examples/culture-d3/components/04-language.json | d3 component: 20 lexicon; 6 names; 7 utterances; 1 sound_changes | fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa | 8,036 bytes |
| A-07 | examples/culture-d3/components/05-ritual.json | d3 component: 2 beliefs; 2 symbols | 20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d | 3,054 bytes |
| A-08 | examples/culture-d3/components/06-material.json | d3 component: 3 materials; 4 objects; 4 costumes; 2 eras; 1 rank_rules | ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7 | 4,415 bytes |
| A-09 | examples/culture-d3/components/07-evidence.json | d3 component: 5 references; 5 bridges | 1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3 | 13,880 bytes |
| A-10 | examples/culture-d2/packet.d2.yml | d2 design drill (read-only input): 40 lexicon / 8 names / 8 pantheon / 10 costumes / 9 materials / 27 rule ids / 29 coupling notes | e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643 | 156,071 bytes |
| A-11 | examples/culture-d2/typed-labels.d2.yml | d2 typed-label channel: 58 labels, 16 findings, 13 unresolved rank items | a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43 | 84,614 bytes |
| A-12 | corpus/lessons/round-6-sources/05.json | closed round-6 source ledger: 6 top-level keys (read-only evidence binding) | a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb | 15,450 bytes |
| A-13 | corpus/lessons/round-6-sources/03.json | closed round-6 source ledger: 8 top-level keys (read-only evidence binding) | adb22c9a5f3acee621103c7b9dddeeb1eedba22d9e1d92081e37825b80560cea | 11,869 bytes |
| A-14 | corpus/lessons/round-6-sources/13.json | closed round-6 source ledger: 6 top-level keys (read-only evidence binding) | 695043562e7e0caeda6693384baca060009c9e3feb2c108f5e8ea6bfc282d71a | 12,783 bytes |
| A-15 | corpus/lessons/round-6-sources/09.json | closed round-6 source ledger: 6 top-level keys (read-only evidence binding) | 0dd2820d1e837b9ab5e503d21f1a891d367d873c9335f9dad80bef3c2da6ac94 | 17,242 bytes |
| A-16 | reports/round-6/parent-reconciliation.json | effective round-6 scope/kind authority: 12 top-level keys | 1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162 | 17,075 bytes |
| A-17 | tools/gates/handoff-packet-check.py | this run's judge; the authoritative verdict authority for the assembled packet | e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575 | 39,451 bytes |
| A-18 | tools/assemble-culture-d3.py | d3 assembler named by the packet's own assembly block | ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014 | 46,374 bytes |
| A-19 | tools/assemble-d2.py | d2 assembler and yaml_lines serializer dependency (read-only) | 8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d | 19,955 bytes |
| A-20 | tools/d2-typed-labels.py | d2 typed-label projection generator | 0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802 | 150,201 bytes |
| A-21 | tools/check-evidence-coupling.py | d3 evidence-coupling guard (read-only) | 849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e | 84,948 bytes |
| A-GLOSS | §glossary payload (inline, this packet) | constructed lexemes re-rendered from the d3 packet's lexicon[] in source order; the payload's source bytes are the d3 packet named above | bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829 | 20 entries |

## dependency_manifest

- profile kotodama-handoff-e2e/1 (this exercise; renderer revision 1.0.0)
- tools/gates/handoff-packet-check.py @sha256:e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575 (the gate this packet is judged by)
- corpus/knowledge/synthesis/worldbible-integration-contract.md @sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 (pinned contract; interface revision 1.0.0)
- examples/culture-d3/packet.json @sha256:bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829; examples/culture-d3/packet.gates.yml @sha256:306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425; examples/culture-d3/expected.json @sha256:562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc (d3 payload, legacy projection, freeze manifest)
- tools/assemble-culture-d3.py @sha256:ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014 and tools/assemble-d2.py @sha256:8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d (assemblers named by the two packets' own assembly blocks; the second is also the yaml_lines serializer, read-only)
- tools/d2-typed-labels.py @sha256:0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802 and tools/check-evidence-coupling.py @sha256:849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e (d2 typed-label generator and d3 evidence-coupling guard, both read-only here)
- examples/culture-d2/packet.d2.yml @sha256:e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643; examples/culture-d2/typed-labels.d2.yml @sha256:a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43 (d2 design drill and its typed-label projection, read-only inputs)
- SC1 sound law /p/ > /f/, initial, E0→E1, register `ordinary` (constructed; examples/culture-d3/packet.json sound_changes[0])
- AV1 avoidance rule: L01 in register `ritual`, place `hall`, substitutes L02 (constructed; examples/culture-d3/packet.json speech_rules)
- NR1 naming-timing rule: offsets [2, 8, 20], chosen 8 fictional-nights, source S03 (constructed-not-historical; examples/culture-d3/packet.json naming_rule)
- RR1 rank rule: authority "Hall Wardens of the Two Benches (invented fictional hall authority)", prohibit material `plant-cloth` for wearer ranks visitor, jurisdiction `hall`, rites assembly, eras E1 (constructed; examples/culture-d3/packet.json rank_rules)
- D2 grammar rule ids M-01–M-27 (27 distinct ids in examples/culture-d2/packet.d2.yml morphology) and 21 lines carrying a `to-verify` flag
- prerequisites: the 13 component digests recorded by the two assemblers' own `assembly.source_sha256` manifests, re-measured and matched at assembly time; every reference above is pinned by exact digest or version (contract §4, §9)

## claim_ledger

Claim kinds are the contract §6 kinds; the two D2 rows are labelled a derived projection (author-side) so they cannot be read as world claims. Statements are read from the live records, not paraphrased from documentation.

| claim_id | kind | evidence_status | summary |
|---|---|---|---|
| D2-CL01 | designer interpretation | derived projection (author-side) | 58 D2 typed labels (46 native-form / 10 translated-label / 2 borrowed-strata) with 16 findings, 15 of them hold-or-fail; the label channel is a projection of the D2 packet's own records (examples/culture-d2/typed-labels.d2.yml coverage) |
| D2-CL02 | designer interpretation | derived projection (author-side), holds open | D2 normalization residuals: 13 unresolved rank items, 3 quarantine handles, 4 conflicts, 10 reconciliation records, 9 material-bridge holds (9 R-MAT-BRIDGE-MISSING) (examples/culture-d2/typed-labels.d2.yml) |
| CL01 | generative rule | invented | SC1 sound law /p/ > /f/ word-initially separates the E1 spoken forms from the E0 citation forms; the ritual citation layer keeps the earlier forms (examples/culture-d3/packet.json sound_changes) |
| CL02 | generative rule | invented | AV1 substitutes L02 for L01 exactly in register `ritual` / place `hall`; no generalized avoidance outside it (examples/culture-d3/packet.json speech_rules) |
| CL03 | generative rule | invented | NR1 allows name-giving at offsets [2, 8, 20] fictional-nights, chosen 8, source S03 (constructed-not-historical) — a constructed discrete set, not a historical prescription (examples/culture-d3/packet.json naming_rule) |
| CL04 | generative rule | invented | RR1 prohibits material `plant-cloth` for wearer ranks visitor in jurisdiction `hall` (E1); the violation recorded in the costume records is retained visibly, never repaired (examples/culture-d3/packet.json rank_rules) |
| CL05 | generative rule | invented | 2 sign→reading rules (SY01–SY02) are audience- and era-scoped conventions of one fictional hall; no colour key and no universal meaning is asserted (examples/culture-d3/packet.json symbols) |
| CL06 | attributed in-world belief | invented; truth status `unresolved` | 2 attributed accounts (B01–B02) with named in-world speakers and opposing readings; no narrator asserts either account, and no supernatural claim is endorsed (examples/culture-d3/packet.json beliefs) |
| CL07 | designer interpretation | invented | The E0/E1 staging, the two invented offices and the invented hall authority are an author's design genealogy, not a reconstruction of any real institution (examples/culture-d3/packet.json scope_notes) |
| CL08 | real-world reference | secondary-scholarly; support partial-support; audit R6-05-A | S01 (https://lrc.la.utexas.edu/eieol/hitol/20) grounds only a design method-transfer: Effective round-6 parent-reconciliation row R6-05-A is partial-support with effective kind secondary-scholarly (authored UT teaching text, not repository scholarship) and carries parent spotcheck P04; the sibling audit R6-05-B on the same… (examples/culture-d3/packet.json references) |
| CL09 | real-world reference | museum-object; support scoped-support; audit R6-03-B | S02 (https://collections.louvre.fr/en/ark:/53355/cl010005890) grounds only a design method-transfer: Effective round-6 parent-reconciliation row R6-03-B is scoped-support, museum-object, with parent spotcheck P02. Object-record attribution carrying the museum's own caveat; not independent re-dating of the Assiut tomb group and no… (examples/culture-d3/packet.json references) |
| CL10 | real-world reference | primary-text; support scoped-support; audit R6-13-A | S03 (https://web.archive.org/web/20231003011254/https://sacred-texts.com/h…) grounds only a design method-transfer: Effective round-6 parent-reconciliation row R6-13-A is scoped-support, primary-text, with the effective URL pinned by parent spotcheck P03 to the exact Wayback capture 20231003011254 of the sacred-texts SBE30 page (the raw worker had… (examples/culture-d3/packet.json references) |
| CL11 | real-world reference | primary-text; support scoped-support; audit R6-13-B | S04 (https://www.wisdomlib.org/hinduism/book/satapatha-brahmana-english/d/…) grounds only a design method-transfer: Effective round-6 parent-reconciliation row R6-13-B is scoped-support, primary-text, with parent spotcheck P01. English translation only (Eggeling 1885); the Madhyandina/Kanva attachment difference is known through Eggeling's footnote 9,… (examples/culture-d3/packet.json references) |
| CL12 | real-world reference | secondary-scholarly; support partial-support; audit R6-09-A | S05 (http://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf) grounds only a design method-transfer: Effective round-6 parent-reconciliation row R6-09-A is partial-support, secondary-scholarly; the parent's effective locator correction (spotcheck P05) places the practical-text quotation on PDF/printed page 9 with the archive composition… (examples/culture-d3/packet.json references) |
| CL13 | screening statement | unresolved | No real-language sweep, novelty check or community consultation has been performed for any D2 or D3 spelling (`real_language_sweep_performed: false`); no clearance or permission may be inferred (examples/culture-d3/packet.json screening) |

## coupling_edges

Typed source→target relations. The D3 bridge ledger is carried row by row from the live records (relation, target ids, mechanism and limits verbatim from the packet); the D2 packet states its couplings per record rather than as an edge list, so it is carried as one aggregate edge.

| edge_id | source | relation | target_ids | mechanism | limits |
|---|---|---|---|---|---|
| D2-EDGES | 29 `coupling_note` fields over examples/culture-d2/packet.d2.yml | dependency (as declared per record) | L-01–L-40, NM-01–NM-08, GAR-01–GAR-10 | each note names the record's own coupling to a lexicon, naming or material record | carried as declared; the exercise neither adjudicates nor repairs the coupling |
| BR01 | S01 | method-transfer (asserted scope `design-only`, kind constructed-rule) | U01, U02 | S01's retrieved lesson gloss marks a written Akkadogram (IS-BAT, romanized) whose explicitly stated Hittite reading differs (epta): one written citation form with a distinct spoken realization, declared inside a single clause. D3 copies only that separation as a constructed rule: U01/U02 both… | Design-only: the written-layer-plus-register-reading coupling is a declared rule of a fictional language, not a claim about how Hittite or Hattic scribal practice worked, and no real-language genealogy is asserted. S01 is partial-support, mediated English teaching prose with tertiary corroborations; no cuneiform… |
| BR02 | S02 | method-transfer (asserted scope `design-only`, kind constructed-rule) | C01, C02 | S02's museum record dates a pleated linen tunic to late Dynasty 11-early Dynasty 12, a garment feature attested before the period it is sometimes used to date, showing that one object-level trait cannot serve as an exclusive era marker. D3 transfers that caution: C01 (E0) and C02 (E1) keep the… | Design-only construction on a fictional felt work garment; no real textile history is claimed and no statement is made about pleats, linen or felt in any real tradition. S02 is scoped-support from a museum object record carrying the museum's own dating caveat; findspot dating is catalogue attribution, not independent… |
| BR03 | S03 | method-transfer (asserted scope `design-only`, kind constructed-rule) | NR1 | S03 shows a naming-rite timing given as a discrete, school-specific set of named alternatives (ten nights, a hundred nights, or one year) inside one translated grihya prescription. D3 transfers the method, not the numbers: NR1 declares a closed discrete set allowed_offsets [2, 8, 20] with unit… | Design-only: the offsets, unit and chosen value are invented; no claim that Gobhila or any school prescribed 2, 8 or 20 nights, and no universal ancient practice is asserted. S03 is translation-mediated English (Oldenberg 1892, including at least one conjectural emendation); the Sanskrit was not read; it is one… |
| BR04 | S04 | analogy (asserted scope `design-only`, kind constructed-rule) | O01, O04 | S04 distinguishes, inside one school's translated prescription, skins spread on the ground as a sitting surface (3.2.1.1-9) from a horn tied to the end of a garment as a worn attachment (3.2.1.18). D3 models that surface-versus-worn distinction as separate object slots: O01 is a ground-surface… | Design-only: O01 and O04 belong to an invented office/display system, not a reconstruction of Vedic consecration; no rite, embryo or womb analogy, or world symbolism is copied. S04 is English translation only (Eggeling 1885); the Madhyandina/Kanva attachment difference is known through the translator's footnote, not… |
| BR05 | S05 | method-transfer (asserted scope `design-only`, kind constructed-rule) | SY01, B01 | S05 shows an archive in which daily records ran overwhelmingly in Elamite (about 15,000-18,000 documents) while a single Old Persian administrative tablet is explicitly described as an isolate that may not demonstrate general use: record languages are institution-specific, and one exceptional… | Design-only: SY01 and B01 are constructed attributed fiction inside a fictional culture; nothing is asserted about real Persian religion, Achaemenid administration or subject populations' speech. S05 is partial-support: the Behistun cross-version leg and all-subject speech claims remain unverified, and the isolate… |

## requested_decisions

Per-record questions for lore, with mutually exclusive alternatives and blockers. `accept` always means retain as non-canon candidate material; it never means canonize.

| record_id | question | alternatives | blocker |
|---|---|---|---|
| RD-01 L01–L20 + N01–N06 | accept the 20 constructed D3 lexemes and 6 names as candidate world material, with the naming rule as proposed? | accept / defer / reject per record | real-language sweep unperformed; names stay namespaced candidates |
| RD-02 B01–B02 | record the attributed accounts as in-world belief, and decide whether either becomes a world-fact? | belief only / belief plus world-fact ruling / defer | canon standing is lore's; truth status stays unresolved here |
| RD-03 SY01–SY02 | adopt the audience- and era-scoped sign→reading rules, including their competing readings? | adopt scoped / adopt with a single reading only / defer | a single reading would drop the recorded counter-reading |
| RD-04 E0/E1 | adopt the relative era stages, with or without dates? | adopt without dates / adopt with dates supplied by lore / defer | no calendar exists; dates are lore's decision |
| RD-05 C01–C04 + RR1 | adopt the costume records and the rank rule, accepting that one costume stays a declared violation? | accept with the violation retained / accept without the violating record / defer | the violation is evidence of the rule's reach, not an error to repair |
| RD-06 N01–N06 + screening | approve the name records, given that no real-language screening has been performed? | approve as provisional / hold until screened / reject | screening is unresolved kotodama-side work, not a lore disposition |
| RD-07 BR01–BR05 | accept the 5 design-only source bridges as method-transfer evidence? | accept as design-only / defer | bridge support is partial or scoped; no real-world fact is claimed |
| RD-08 transfer surface | name the baseline bible revision, entity keys and receipt surface this lane should deliver against? | supply a baseline and receipt surface / keep the lane unbound / defer | no lore baseline exists, so nothing here can be imported as canon |
| RD-D2-01 D2 typed-label channel | record the D2 label channel (58 labels, 15 holds) as a author-side projection to be resolved before any D2 record is handed over? | record as author-side / require resolution first / defer | the channel is a projection of D2 design records, not a delivered payload |
| RD-D2-02 D2 retained holds | decide the disposition of the 13 unresolved D2 rank items and 21 `to-verify` lines? | resolve kotodama-side first / accept with holds recorded / defer | held rows are explicit unknowns and are not promoted by this packet |

## validation

Observed rows only: what this run actually measured, with the command shapes it used. These are local generation and identity checks of one envelope — not bible-wide consistency and not a canon decision (contract §8 step 3).

- read set: 21 files re-measured (`sha256`, same run) against the frozen baseline's `inputs` block; the §artifact_manifest digests are those measured values, not copied from any document
- component digests: 13 digests recorded by the two assemblers' own `assembly.source_sha256` manifests (9 D2, 4 D3) re-measured against the component bytes on disk — all matched, so each packet still describes the files it names
- manifest equality: every §artifact_manifest row's digest equals the sha256 of the file it names, measured in this run; the gate checks digest presence only, so this equality is the exercise's own assertion (design §1, §6.6)
- field agreement: the contract §4 table yields 16 required field names, the gate's own FIELD_NAMES tuple yields 16, and this packet supplies 16 — the three sets are compared, not assumed (design §6.1)
- glossary identity: the 20 rows are the live D3 lexicon in source order (id, E0 form, computed E1 form, gloss) and every etymology carries the record's own status token, which is inside the licensed vocabulary (design §5)
- D2 read-only facts carried into this packet's D2 claim rows: 58 typed labels (46 native-form / 10 translated-label / 2 borrowed-strata), 16 findings (15 hold-or-fail), 13 unresolved rank items, 3 quarantine handles, 4 conflicts, 10 reconciliation records, 9 material-bridge holds
- gate: `python3 tools/gates/handoff-packet-check.py packet.md` over the isolated copy, run from a directory outside the repository; declared expectation, checked after the run — exit 0, fields=16/16, glossary-entries=20, findings=0; the observed values are compared against the frozen baseline in `reports/round-11/handoff/expected.json`, whose run log records the verdict of the run it froze

## open_questions

- OQ-E2E-01: no real-language homophone, offensive-association or novelty sweep has been performed for any D2 or D3 spelling (examples/culture-d3/packet.json screening: unresolved) — kotodama pre-publication + lore; blocking for official name approval.
- OQ-E2E-02: no lore baseline, entity keys, receipt surface or bilateral same-revision read exists for corpus/knowledge/synthesis/worldbible-integration-contract.md (revision 1.0.0) — lore + both lanes; blocking for the first transfer (contract §1, §4, §8).
- OQ-E2E-03: 5 D3 scope notes and 21 D2 `to-verify` lines carry unresolved residuals (partial-support sources, unperformed screening, unresolved rank items) — kotodama; blocking for the affected records, not for this envelope.
- OQ-E2E-04: the D2 and D3 drills are separate design fixtures with no shared chronology, and this packet asserts none; any combined reading is a lore decision — lore; non-blocking.
- OQ-E2E-05: documentation surfaces outside this read set (`examples/culture-d3/handoff.md`, `examples/culture-d3/README.md`, `examples/culture-d2/ASSEMBLY.md`) are excluded from the computational freeze; R11-O01 §7 measured stale digests in their prose. This exercise re-measures the bytes it reads and propagates no documentation figure — kotodama-owned; non-blocking.

## glossary payload (inline; the live D3 lexicon, L01–L20)

All 20 rows are the assembled D3 packet's lexicon in source order (E0 citation form, computed E1 ordinary form, packet gloss). Every etymology carries `status: <record status>` — a constructed design derivation by the declared sound rule, with no real-language derivation, borrowing, or novelty-in-all-languages claim.

| entry_id | E0 form | E1 form | gloss (packet) | etymology |
|---|---|---|---|---|
| L01 | pina | fina | spoken pledge | status: constructed — E0 *pina → E1 fina (changed by SC1 initial /p/ > /f/ (ordinary register)); available_from E0 |
| L02 | suma | suma | hearth invocation | status: constructed — E0 *suma → E1 suma (unchanged into E1); available_from E0 |
| L03 | talu | talu | record line | status: constructed — E0 *talu → E1 talu (unchanged into E1); available_from E0 |
| L04 | palu | falu | boundary token | status: constructed — E0 *palu → E1 falu (changed by SC1 initial /p/ > /f/ (ordinary register)); available_from E0 |
| L05 | pira | fira | witness mark | status: constructed — E0 *pira → E1 fira (changed by SC1 initial /p/ > /f/ (ordinary register)); available_from E0 |
| L06 | puka | fuka | gate announcement | status: constructed — E0 *puka → E1 fuka (changed by SC1 initial /p/ > /f/ (ordinary register)); available_from E0 |
| L07 | tana | tana | thread count | status: constructed — E0 *tana → E1 tana (unchanged into E1); available_from E0 |
| L08 | kila | kila | measured fold | status: constructed — E0 *kila → E1 kila (unchanged into E1); available_from E0 |
| L09 | ruma | ruma | assembly seat | status: constructed — E0 *ruma → E1 ruma (unchanged into E1); available_from E0 |
| L10 | masin | masin | marker cord | status: constructed — E0 *masin → E1 masin (unchanged into E1); available_from E0 |
| L11 | nisu | nisu | night tally | status: constructed — E0 *nisu → E1 nisu (unchanged into E1); available_from E0 |
| L12 | lura | lura | hall passage | status: constructed — E0 *lura → E1 lura (unchanged into E1); available_from E0 |
| L13 | sina | sina | visitor sign | status: constructed — E0 *sina → E1 sina (unchanged into E1); available_from E0 |
| L14 | kalti | kalti | weft edge | status: constructed — E0 *kalti → E1 kalti (unchanged into E1); available_from E0 |
| L15 | rusi | rusi | appointed token | status: constructed — E0 *rusi → E1 rusi (unchanged into E1); available_from E0 |
| L16 | ami | ami | settlement | status: constructed — E0 *ami → E1 ami (unchanged into E1); available_from E0 |
| L17 | nara | nara | felt work-wrap | status: constructed — E0 *nara → E1 nara (unchanged into E1); available_from E0 |
| L18 | salu | salu | plain work-wrap | status: constructed — E0 *salu → E1 salu (unchanged into E1); available_from E0 |
| L19 | mila | mila | assembly robe | status: constructed — E0 *mila → E1 mila (unchanged into E1); available_from E0 |
| L20 | kuru | kuru | horn rank-clasp | status: constructed — E0 *kuru → E1 kuru (unchanged into E1); available_from E0 |
