# Handoff packet — D1 "Retied Houses" (deliberately unbound research packet; not canonized)

NON-CANON sample world-bible handoff packet, kotodama-shokunin → lore-shokunin,
assembled per `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(contract digest pinned below, §1; bilateral same-revision read pending, OQ-08).
This Markdown serialization supersedes `examples/handoff-packet.sample.yml`,
which carries the same envelope in a YAML serialization the contract does not
default to (the .yml's own validation block records the correction). Every
record derives from the non-canon design fixture D1 in
`corpus/knowledge/synthesis/worked-example-mini-culture.md`. Nothing here is
canon, a world-bible entry, or lore acceptance; canon standing is lore's
alone (§6, §8, §13). Sample at era E2 "Retied" Y183; Y coordinates are
fixture-arbitrary, not BCE/CE (§7).

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)

| field | value |
|---|---|
| packet_id | kotodama.handoff.d1-retied-houses.sample |
| packet_version | 1.0.0-sample.md (supersedes the YAML serialization of the same envelope; pre-freeze sample) |
| contract_ref | kotodama-lore-adjacency 1.0.0, contract digest sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 (§1 pin; bilateral read pending per OQ-08) |
| producer | kotodama-shokunin (round-2 adjacency workstream; generative craft and design records only) |
| recipient | lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency) |
| request_ref | none — no lore brief existed; assembled as an unbound drill (§4, §12) |
| baseline_bible_ref | none — deliberately unbound research packet; cannot be imported as canon without a lore baseline and a new reviewed handoff (§4) |
| artifact_manifest | A-Y payload record examples/handoff-packet.sample.yml sha256:b900549ec51f954dbbcd165066c4dacc60bb9d05aedb4fec00244921b09502e6 (record counts 11/4/20/15/19/20/17 across A1-A7); A-D1 design record corpus/knowledge/synthesis/worked-example-mini-culture.md sha256:e96bc943a04e8f2691f3ba95f9cee5dd3456d3a9439714e0196eaaeeacaa2509 |
| subject_refs | 7 namespaced candidate refs cand:kotodama.d1.* (collective, 3 deities, place, institution, language variety); all unresolved — no lore entity ids supplied (§4) |
| scope | D1 "Retied Houses" design fixture; language family F1 River branch (E2 vernacular + E1 liturgical); eras E0-E2; 20-term lexicon L01-L20; naming ledger; 8 symbol records; 9 costume records; stipulated cool seasonally-flooded river terrace (no real place) |

## dependency_manifest

- P-D1-UNION phonology union stratum @0.1.0-sample (pinned)
- P-D1-E1LIT liturgical register profile @0.1.0-sample (pinned)
- L1 sound law /p/ > /f/ @0.1.0-sample (pinned)
- M1-M7 morphosyntax rules @0.1.0-sample (pinned)
- O1 orthography register-readings @0.1.0-sample (pinned)
- A3 lexicon L01-L20 @0.1.0-sample (pinned); A4 naming grammar @0.1.0-sample (pinned)
- prerequisites: design-record digest in artifact_manifest; no floating version references (§4, §9)

## claim_ledger

13 claims CL01-CL13, each with kind, provenance, evidence status, uncertainty,
and record relations — full statements in artifact A-Y §claim_ledger.

| claim_id | kind | evidence_status | summary |
|---|---|---|---|
| CL01 | generative rule | invented | /p/ > /f/ (L1) separates E2 surface forms from E1 archival forms |
| CL02 | real-world reference | attested | Japanese SOV/suffixing, English SVO (typological comparator only; Dryer 2013 WALS ch.81, Shibatani 1990) |
| CL03 | real-world method | attested (method) | sound correspondences and relative chronology are method, not genealogy proof (Campbell 2013) |
| CL04 | designer interpretation | invented | F1 genealogy E0→E1→E2 is an author's genealogy, not a reconstruction |
| CL05 | attributed in-world belief (B) | invented | three offices hold, open, record; no narrator asserts deity existence |
| CL06 | attributed belief (contested) | contested in-fiction | founding-assembly legend contested; no E0 chronicle supports it |
| CL07 | candidate world-fact | invented (prescription) | E1 ochre-bead restriction, E2 repeal; witness strip stays restricted |
| CL08 | designer interpretation | invented | costume cuts are design choices; no real garment reconstructed (Roach-Higgins & Eicher 1992; Barber 1991) |
| CL09 | real-world heuristic | inferred with bridge | rite-of-passage triad used as heuristic, not law (van Gennep 1960 [1909]) |
| CL10 | designer interpretation | invented | holding/opening/visible-repair is a declared design lens, not a universal |
| CL11 | real-world reference | attested (bibliography) | dress = body modifications and supplements, not garments alone |
| CL12 | historiographic caution | attested (edition) | unilinear development ladders discredited as universal history (Trigger 2006) |
| CL13 | designer interpretation | invented (declared gap) | 20-term lexicon is bounded; body/kin/weather/war unbuilt, not absent |

## coupling_edges

16 typed edges E01-E16 plus change trial T-01 (full mechanisms and justifications
in artifact A-Y §coupling_edges): material affordance → L01 fala (dependency);
L1 → E2 surface forms, place name Fanoluma (dependency); L04+L01 → L11
nalifala oath-cloth → oath rite sign rule (dependency); office institution →
L12 senafala witness strip (dependency); red ochre + removable bead → RR01/RR03
display rules (dependency); "broken loop" → mourning reading (analogy); obsolete
bead → claimed seniority in partisan speech (attributed association); L1 →
rejected hybrid "fanopala" (dependency); Upland /lum/ → L05 luma → L14/L18
(loan dependency); myth variant → theonym Nalisena (dependency); T-01 trials a
hypothetical f > v revision without rewriting records (§12).

| edge_id | source | target | relation |
|---|---|---|---|
| E01 | bast-cloth affordance (MAT1) | L01 fala | dependency |
| E02 | L1 sound law | L01/L02/L11-L20 surface forms | dependency |
| E03 | L1 sound law | N04 Fanoluma (E1 spelling Panoluma retained as dated alias) | dependency |
| E04 | L04 nali + L01 fala | L11 nalifala oath-cloth | dependency |
| E05 | L11 nalifala | oath rite visible-join sign rule | dependency |
| E06 | appointed-witness office | L12 senafala witness strip | dependency |
| E07 | MAT3 ochre + clay bead | RR01 E1 restriction, RR03 E2 repeal | dependency |
| E08 | "broken loop" sign | mourning reading | analogy |
| E09 | obsolete E1 delegate bead | E2 partisan seniority claim | attributed-association |
| E10 | release domain (DE02) | L13 kerafala + unpicked stitches | dependency |
| E11 | naming slot grammar | N01/N02 full-name forms | dependency |
| E12 | myth variant "holds two banks apart" | theonym Nalisena | dependency |
| E13 | E2 charter revision | bead display access (domain persists) | dependency |
| E14 | ritual triad heuristic (S4) | D1 passage rite design | analogy |
| E15 | Upland trade layer /lum/ | L05 luma, L14 fanoluma, L18 Naliluma | dependency |
| E16 | L19 fanofala | rejected hybrid "fanopala" | dependency |

## requested_decisions

8 decisions D-RD-01..D-RD-08 with mutually exclusive alternatives, blockers,
and the partial-acceptance boundary (full text in artifact A-Y): RD-01 accept
language sketch as candidate world material; RD-02 pantheon register as
attributed belief vs world-fact (lore's call); RD-03 sign→reading rules with
era/audience scoping; RD-04 adopt era stages with or without dates; RD-05
adopt E2 costume permissions; RD-06 approve names/aliases and the exonym;
RD-07 accept bounded lexicon with recorded gaps; RD-08 what receipt surface
and baseline apply before any transfer. Partial acceptance per record is
allowed; no accepted label may depend on an unaccepted rule (§8 step 8).

## validation

Local generation/derivation verification, not bible-wide consistency and not
canon certification (§8 step 3). Reproducible runs recorded at round-2 close
(2026-10-17) in the lane LOG and corpus/lessons/round-2-adjacency.md: all six
culture-packet gates plus this checker's selftest were executed against the
committed tool digests; the per-gate exit codes and findings for the A-Y
payload record are listed in its §validation block, and the checker's run over
this Markdown packet is recorded in the round-2 LOG entry. Honest gaps routed
to open questions: real-language name sweep unresolved (OQ-02), lexicon
coverage gaps declared (OQ-01), calendar/astronomy unsolved (OQ-03), physical
textile behaviour untested (OQ-04).

## open_questions

- OQ-01: lexicon coverage gaps (body, kinship, weather, war) — kotodama + lore; blocking for full-lexicon acceptance.
- OQ-02: real-language homophone/offensive-association sweep not performed — kotodama pre-publication + lore; blocking for official name approval.
- OQ-03: calendar and intercalation unsolved — kotodama; blocking for date calculation.
- OQ-04: physical textile behaviour untested — kotodama material; blocking for production claims.
- OQ-05: Upland sister language unsampled — kotodama; blocking for a complete family claim.
- OQ-06: supernatural efficacy unaddressed by design — lore; blocking for world-fact import.
- OQ-07: no baseline bible, entity keys, or receipt surface supplied — lore; blocking for any canon import (§4, §8).
- OQ-08: bilateral same-revision read records do not exist yet — both lanes; blocking for first transfer (§1).

## glossary payload (inline; artifact of the A-Y record, L01-L20)

| entry_id | term | gloss | etymology |
|---|---|---|---|
| L01 | fala | cloth; noun | status: constructed — E0 *pala 'bast-cloth length' → E1 pala → E2 fala (L1) |
| L02 | fano | raised bank; noun | status: constructed — E0 *pano → E1 pano → E2 fano (L1) |
| L03 | tala | river channel; noun | status: constructed — E0 *tala, unchanged E1/E2 |
| L04 | nali | knot; binding obligation; noun | status: constructed — E0 *nali 'knot'; obligation sense lexicalized in E1 |
| L05 | luma | dwelling; membership house; noun | status: constructed — donor /lum/ (Upland, unsampled) → E1 luma by final-/a/ coda repair |
| L06 | sena | witness; to witness; noun/verb | status: constructed — E0 *sena, unchanged; zero conversion licensed (M3) |
| L07 | kera | open; release; verb | status: constructed — E0 *kera 'open'; E1 legal extension 'release' |
| L08 | mori | local pale riverbird; noun | status: constructed — E0 *mori; fictional folk category, not a species claim |
| L09 | ranu | red ochre pigment; noun | status: constructed — E0 *ranu 'ochre'; hue sense by metonymy |
| L10 | weli | unpigmented; pale; modifier | status: constructed — E0 *weli, unchanged E1/E2 |
| L11 | nalifala | oath-cloth; noun | status: constructed — E1 nali-pala → E2 nalifala (L1; CMP) |
| L12 | senafala | witness strip; noun | status: constructed — E1 sena-pala → E2 senafala (L1; CMP) |
| L13 | kerafala | released-edge cloth; noun | status: constructed — E1 kera-pala → E2 kerafala (L1; CMP) |
| L14 | fanoluma | bank-house (place/affiliation); noun | status: constructed — E1 pano-luma → E2 fanoluma (L1 applied twice) |
| L15 | Nalisena | Knot-Witness (theonym); noun | status: constructed — E1 nali-sena → Nalisena (CMP) |
| L16 | Talakera | River-Opener (theonym); noun | status: constructed — E1 tala-kera → Talakera (CMP) |
| L17 | Falasena | Cloth-Witness (theonym); noun | status: constructed — E1 pala-sena; E1 recitation form Palasena retained |
| L18 | Naliluma | Knot-House(s) collective endonym; noun | status: constructed — E1 nali-luma → Naliluma (CMP) |
| L19 | fanofala | bank-work apron; noun | status: constructed — E1 pano-pala → E2 fanofala (L1 applied twice) |
| L20 | keranali | release of a bond; noun | status: constructed — E1 kera-nali → keranali (CMP) |
