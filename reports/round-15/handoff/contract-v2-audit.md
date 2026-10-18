# R15-O07 — handoff contract audit re-run over packet v2 (build 05)

- Date: 2026-10-18. Scope: re-run of the round-12 handoff contract audit protocol
  (`reports/round-12/adjacency/contract.md`) over the round-15 packet-v2 bytes,
  closing the round-12 semantic reject; field-by-field §4 comparison, plus the two
  new v2 checks (uncertainty non-boilerplate, claim-to-record link resolution).
- Audited bytes: `reports/round-15/handoff/packet-v2-05.md`
  sha256 `24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b`;
  machine twin `reports/round-15/handoff/packet-v2-05.yml`
  sha256 `39cf4d53b02a1a9026e3a9a302cd1031d1b6a55fc2b8ea9d7b7eb877fa1dfcd6`;
  measured 2026-10-18T00:59:33Z. Earlier same-day revisions of these filenames
  were also measured during the wave (00:47:53Z, 00:54:43Z) and showed two
  transient defects that the packet seats repaired before this audit closed; the
  history is recorded under "Measurements during the build" below. If a later
  keyed build supersedes these digests, this audit's measurements must be
  re-run on the new bytes as a new file — this report is not an edit surface.
- Writes: this report only. No contract, PROVINCE, L0, packet, tool, sibling, or
  filed round-8..14 artifact was changed. All artifacts remain NON-CANON; no
  real-world rights ruling is made; the freshness pause stands.
- Role note: this file is the contract-audit re-run. The per-claim uncertainty
  verification below is real, independently measured evidence (basis-by-basis
  locator resolution), but it is not a substitute for a dedicated
  uncertainty-population receipt if the parent expects one under
  `reports/round-15/`; none existed at audit close other than the D-side drafts.

## Independent measurements

- **2026-10-18T00:26:33Z** — `python3 tools/gates/handoff-packet-check.py --selftest` → exit 0, `selftest: OK — fixture findings 11 across 9 ids; clean control exit 0`. Toolchain-health control.
- **2026-10-18T00:40Z** (mechanism control) — `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-1.yml` → exit 0, `fields=16/16 glossary-entries=20 findings=0`: the gate reads a yml-with-embedded-markdown envelope, the serialization round-11 used and the design cites.
- **2026-10-18T00:36–00:53Z** (negative control) — the round-12 protocol re-run over the round-11 packet `reports/round-11/handoff/packet.md` by this audit's own checker reproduced both rejected findings independently: 15/15 claims with no uncertainty status/basis and no record links; `D2-EDGES` carried as one aggregate range row; 21/21 v1 manifest digests re-measured OK. The protocol that rejected v1 is the protocol applied to packet-v2 below.
- **2026-10-18T00:59:33Z** — `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md reports/round-15/handoff/packet-v2-05.md reports/round-15/handoff/packet-v2-05.yml` → contract `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (unchanged from the §1 pin the round-11/12 audits measured); packet md `24f9dd39…`; packet yml `39cf4d53…`. The packet's `contract_ref` (`## artifact_manifest` A-01 and the envelope table) names the measured contract digest; the bilateral same-revision read is declared still outstanding, not represented as complete.
- **2026-10-18T00:59:33Z** — `python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2-05.md` → exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0`. Shape gate clean on the gate-facing markdown surface.
- **2026-10-18T00:59:33Z** — manifest re-hash (this audit's own checker, same method as the round-12 re-hash): 27 manifest rows, 26 file-backed digests re-measured against live bytes, 26 matched, 0 mismatched, 1 inline payload row (A-GLOSS). Tool pins in `## dependency_manifest` (`tools/harness/packet_links.py @sha256:f81bc9f7…`, `tools/harness/packet_uncertainty.py @sha256:cdcc1931…`) match the live tool bytes measured 2026-10-18T00:54:43Z.
- **2026-10-18T00:59:33Z** — `python3 tools/harness/packet_uncertainty.py --packet reports/round-15/handoff/packet-v2-05.yml --require-oq` → exit 0, `claims=15 findings=0`. The uncertainty tool's own selftest was green from 2026-10-18T00:41Z (it crashed with an IndexError at 00:31Z and was repaired by its owner mid-wave).
- **2026-10-18T00:59:33Z** — `python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml` → exit 0, `links=50 resolved=50 findings=0`.
- **2026-10-18T00:59:33Z** — this audit's independent checker over the markdown surface → exit 0: 15/15 claims with in-vocabulary uncertainty status (8 supported / 5 partial / 2 unresolved); 23/23 basis-cited locators resolve to real repo bytes with the cited token present; 50/50 `record_links` refs resolve; 34/34 coupling edges carry concrete targets (no range aggregates) plus a claims back-link that names a real ledger row; uniqueness, non-placeholder and owner-routing checks all clean.

## Measurements during the build (recorded history, superseded by the close above)

- **2026-10-18T00:47:53Z** — gate on the then-current packet-v2-05.md: exit 1 with one `HO-CANON-CLAIM` at the A-17 manifest row (role prose `"shape gate (this packet's markdown surface is judged by it); envelope + canon + glossary kernel"` tripped the gate's canon-verb span); gate on the then-current yml: exit 1, `fields=0/16`; the uncertainty tool reported 26 grammar findings (no `grounding:` prefixes) and the links tool 34 `E-EDGE-NO-CLAIM`. Owner notes were the packet seats' to act on (O-packet / O-impl), and the 00:48–00:59 iterations repaired every one: the A-17 row now reads `"shape gate judge of the markdown surface; envelope and canon-wording kernel"` (line 53 of the audited bytes), the uncertainty bases now carry the design's clause grammar, and the edges table gained the `claims` column (line 108). No finding from those runs stands against the audited bytes.
- **2026-10-18T00:54:43Z** — gate on the intermediate md `8223307c…`: exit 0, 16/16 + 20/20 + 0; both harness tools exit 0. Superseded only because the packet's generation stamp moves per build; digests above pin the final measured state.

## §4 field comparison (contract `corpus/knowledge/synthesis/worldbible-integration-contract.md` §4, "Handoff envelope")

| §4 field(s) | Audit |
|---|---|
| `packet_id`, `packet_version` | `kotodama.handoff.d2d3-e2e.v2.build05` @ `2.0.0`; the major bump is justified in-packet as a breaking envelope change (required per-claim dimensions added, aggregate edge dissolved) and the packet names what it closes and supersedes (preamble "closes" clause; §9 supersedes discipline). |
| `contract_ref` | ID `kotodama-lore-adjacency`, revision `1.0.0`, digest equals the independently measured contract bytes; the outstanding bilateral same-revision read is stated, not asserted complete (contract §1 wording kept). |
| `producer`, `recipient`, `request_ref` | Roles named (kotodama-shokunin → lore-shokunin); `request_ref: none` qualified by the deliberately-unbound drill, the §4-allowed case. |
| `baseline_bible_ref` | `none` with the deliberate unbound-research declaration adjacent; the packet says its own bytes cannot be imported as canon without a lore baseline and a new reviewed handoff. |
| `artifact_manifest` | 27 rows (26 file-backed + 1 inline); IDs, paths, roles, sha256 digests and record counts present; all 26 file-backed digests re-measured and matched by this audit; new rows pin the round-12 reject artifacts and the round-15 claims declaration (A-22..A-24). |
| `subject_refs` | 8 namespaced candidate IDs, all explicitly unresolved, no lore entity IDs guessed; each carries an in-repo witness. |
| `scope` | Per-set culture/region, variety/script, register and era applicability for both drills; no real place or dates claimed; unscreened-ASCII status restated. |
| `dependency_manifest` | Exact versions/digests for tools and records; named rule records (SC1/AV1/NR1/RR1, M-01–M-27) with their own record pointers; the packet states no dependency floats on `latest`; this audit measured the two tool pins as matching live bytes. |
| `claim_ledger` | **Round-12 finding (contract.md :27) closed.** Every row carries statement, §6 claim kind, evidence status, provenance wording, an `uncertainty` cell (`status: supported/partial/unresolved — basis: …`) and a `record_links` cell; 15/15 rows populated; statuses 8/5/2; every basis cites locators this audit resolved into real bytes. |
| `coupling_edges` | **Round-12 finding (contract.md :28) closed.** The v1 `D2-EDGES` aggregate is gone; 34 atomic typed rows (BR01–BR05 + D2E-01..29, matching the 29 live `coupling_note` fields this audit counted in `examples/culture-d2/packet.d2.yml` plus the 5 live D3 bridges), each with relation, mechanism/justification, limits/applicability, concrete target IDs and a `claims` back-link column. Self-targeted rows are a declared, documented convention for the D2 records' declared non-couplings, not silent aggregates. |
| `requested_decisions` | 10 per-record questions with mutually exclusive alternatives and blockers; `accept` bounded to non-canon candidate retention. |
| `validation`, `open_questions` | 9 validation rows name commands and observed results stamped 2026-10-18T00:47:11Z, including the two v1-comparison controls (v1 ledger: 0/15 uncertainty pairs; v1: 1 aggregate D2 edge vs 29 per-record edges here) — both consistent with this audit's independent v1 control; 7 open-question rows carry lanes and blocking status (OQ-V2-01..07), and OQ-V2-07 names the still-outstanding builder/freeze step with its owner. |

## Uncertainty non-boilerplate verification (new v2 check)

Method: this audit's own checker parsed every `## claim_ledger` row of the audited markdown bytes and, for each `uncertainty` cell, (a) validated the status token against {supported, partial, unresolved}; (b) rejected placeholder/boilerplate basis text and duplicate bases after whitespace normalization; (c) extracted every `path#token` locator from the basis and resolved it against live repo bytes (file exists; token present as a JSON key, string value or list element, or as a word-bounded text match); (d) for `unresolved` rows required a named owner in the basis and a routing reference in `## open_questions`; (e) for `partial` rows required a stated limit. Result on the audited bytes: 23/23 basis locators resolve (e.g. `examples/culture-d2/typed-labels.d2.yml#findings_total`, `reports/round-6/parent-reconciliation.json#R6-05-A`, `examples/culture-d3/packet.json#screening`); zero placeholder, zero duplicate bases; both unresolved rows name owners (kotodama / lore) and are routed (OQ-V2-01, OQ-V2-03 or OQ-V2-04 per the claims cell); every partial row names its unsupported legs. The bases are individually reasoned per claim — no basis restates the status token or copies a sibling row. Cross-check: the O-impl tool independently reports `claims=15 findings=0` with `--require-oq`.

## Claim-to-record link resolution (new v2 check)

Every `record_links` cell was split and each `path#token` spec resolved against live bytes: 50/50 resolve (this audit's checker and `tools/harness/packet_links.py` agree). Direction is claim→record, satisfying §4's "relation to other records"; the edges table carries the inverse `claims` column, so §4's relation requirement holds in both directions. Edge targets are concrete IDs found in the manifest-pinned files; the round-11 range aggregates are absent.

## Governance remainders carried (not packet-content defects; listed with owners)

- Bilateral same-revision read of contract `kotodama-lore-adjacency` 1.0.0 does not exist yet — owner: lore-shokunin plus both lanes (packet OQ-V2-02; contract §1; unchanged since the round-11 and round-12 audits).
- The round-8 L0 contract-digest question keeps its stale `50c4c2f2…` premise while the operational digest is `5f4c02bf…` — owner: integrator/lore, who should answer or retarget it to the current digest and record the both-lane read (round-12 audit's L0 section; `reports/round-11/adjacency.md` §3.1; this audit did not inspect the out-of-lane live L0 surface, so later status changes are to-verify).
- No kotodama-side §1 read record (`lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer`) exists in this repo — owner: kotodama orchestrator (`corpus/lessons/round-2-adjacency.md` §3; v2-design OQ-V2-03).
- The durable builder and frozen `expected.json` baseline had not landed at audit close — owner: O-impl/O-frozen seats, then round-15 integrator (packet OQ-V2-07 names this as a process step, not a packet-content gap). This audit measured the packet bytes, not the builder.
- The audited filenames are keyed builds (`packet-v2-05.*`) while the round runner looks for `packet-v2.md`/`packet.yml` first — owner: round-15 integrator, to land the settled build under the canonical name (a rename, not a byte change, but digests must be re-pinned when it happens).
- `reports/round-15/handoff/shard-1.md` and `shard-2.md` are working fragments of the packet assembly — owner: round-15 integrator, to keep or clear them at integration.
- The yml surface alone gates at `fields=0/16` (no embedded markdown envelope view in the machine twin; measured 00:47:53Z and unchanged in kind at audit close) — owner: O-packet, optional; the contract §4 default serialization is the markdown surface, which passes 16/16 + 20/20, so this is an optimization note, not a conformance gap.

## Lore boundary and PROVINCE

`PROVINCE.md` keeps this lane on generative/coupling craft and routes canon to lore; the packet stays inside that boundary on the audited bytes: `canon_standing: not canonized` marker line; `handoff_status: prepared-not-accepted`; deliberately unbound; subject refs unresolved; screening refusal explicit ("no real-language clearance, community consultation, or cultural permission is claimed, performed, or granted"); uncertainty statuses are declared kotodama-side support language that never mean accepted, import-ready, or canon. Boundary verdict: pass for this exercise; not a lore receipt or transfer authorization. The PROVINCE pointer to the contract file remains accurate (verified by reading both on the audited bytes).

## Disposition

- The round-12 semantic reject is closed on the audited bytes: the claim-ledger uncertainty dimension and the claim-to-record relation key exist, are populated without boilerplate, and resolve; the D2 aggregate edge is dissolved into 34 atomic typed rows with claim back-links; the shape gate reads 16/16 fields, 20 glossary entries, zero findings.
- Keep the packet classified as a successful non-canon exercise, not an accepted handoff; the governance items above keep their lanes and owners.
- Route the builder/freeze completion and the canonical filename landing to the named owners; if the packet bytes move again, re-run this protocol on the new digests as a new file.
- Verdict: GREEN — packet-v2 build 05 satisfies the §4 semantics the round-12 audit named as the reject grounds; the items above are non-blocking remainders, each recorded with its owner.
