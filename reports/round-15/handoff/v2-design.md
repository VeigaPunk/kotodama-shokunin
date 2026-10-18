# Handoff packet v2 — uncertainty schema and claim-to-record links (R15-O01)

- topic: The design of handoff packet v2 (`reports/round-15/handoff/packet-v2.yml`)
  and of the durable builder that freezes it — closing the round-12 semantic
  reject of the round-11 exercise packet by adding (a) a per-claim uncertainty
  dimension `{status: supported|partial|unresolved, basis}` with zero
  boilerplate and (b) machine-checkable claim-to-record links resolving to real
  repo records, while the shape gate still passes 16/16 + 20/20. This document
  is a spec for the O-impl/O-packet/O-frozen owners; it is not a transcript of
  a render and writes no packet or tool bytes.
- sources: `corpus/knowledge/synthesis/worldbible-integration-contract.md` (§4
  claim_ledger row :63 — "uncertainty, and relation to other records";
  coupling_edges row :64 — typed source→target with per-edge applicability and
  justification; §6 dimension table :94–100; §9 versioning :138–157);
  `reports/round-12/adjacency/contract.md` (the reject: claim-ledger finding
  :27, D2 aggregate-edge finding :28, bilateral-ack blocker :20, L0 item :40–42,
  disposition :44–48); `reports/round-11/handoff/contract-check.md` (O12-F1
  :158–179, including the committed-sample fix shape);
  `examples/handoff-packet.sample.yml` (per-claim `uncertainty:` free text and
  `relations:` field, claim_ledger block :186–260);
  `reports/round-11/handoff/design.md` (field-recognition hazards §4, baseline
  siting §8, gate-gap analysis §1); `reports/round-11/handoff/packet.md`
  (v1 ledger :79–95, D2-EDGES aggregate row :103); gate
  `tools/gates/handoff-packet-check.py` (field recognition :274–314, canon
  probes :321–355, glossary-table recognition :363–371);
  `corpus/knowledge/verification/to-verify-triage-protocol.md` (§1 calibration
  vocabulary, §2 atomize-and-freeze intake) and
  `corpus/knowledge/verification/provenance-audit-ledger-format.md` (§1:
  "`supported` does not mean `improved`, and neither means canon").
- couples: claim D (R15) drafts the SKILL.md label-uncertainty decision table
  from §2/§3 here and cross-references the verification partition; O-impl
  builds the builder from §6; O-packet populates packet-v2.yml from §2–§5;
  O-frozen pins `reports/round-15/handoff/expected.json`; O-contract-audit
  re-runs the round-12 audit over v2 per §7; the orchestrator lands LOG.md.
- taken-from: the reject findings, the contract's own §4/§6 wording, the
  committed sample's field shapes, and the gate's measured recognition
  behavior; no new contract terms are invented here.
- verified-at: 2026-10-17 — read-set digests measured with `sha256sum` (§8);
  five gate probes over the gate's own control packet measured in-process
  (§8): a v2-shaped 7-column ledger with atomic edges exits 0 at
  `fields=16/16 … findings=0`; a placeholder basis cell and an
  off-vocabulary status token are gate-invisible (exit 0), which is the
  measured justification for the builder's semantic checks.
- recheck: on any change to the contract, the gate, or the round-11/12 filed
  evidence this design cites; before packet-v2 bytes are frozen; before the
  round-15 contract-audit re-run.

## 0. Scope and out-of-province

Closes the two content-conformance findings of
`reports/round-12/adjacency/contract.md` (:27 uncertainty dimension and
claim-to-record key absent; :28 D2 aggregate edge) inside a new packet — no
filed round-8..14 artifact is edited. Two reject items are **not**
kotodama-closable and are carried as owner-noted open questions (§7):
bilateral same-revision acknowledgment (contract §1) and the round-8 L0
contract-digest question (`50c4c2f2…` vs `5f4c02bf…`). Out of province, as in
round 11: canon standing and any import ruling (lore-shokunin), rights and
permission (operator), research method (chousa), game mechanics. `uncertainty`
status is kotodama-side support language only — per the provenance-audit
format §1 it never means improved, accepted, import-ready, or canon.

## 1. The rejected state, precisely

- **O12-F1** (`reports/round-11/handoff/contract-check.md` :158–179): all five
  round-11 packets carried no uncertainty dimension — measured rows-with-token
  2/13 (A1) down to 1/6 (A4); the committed sample
  (`examples/handoff-packet.sample.yml:186–260`) implements it 13/13 as a
  per-claim `uncertainty:` free-text string plus a `relations:` field. Fix
  shape recorded there: "an `uncertainty` column/field per claim (as the
  sample has), or a stated per-row carrier."
- **Round-12 audit** (`reports/round-12/adjacency/contract.md` :27): the v1
  ledger (`packet.md` :79–95, header `claim_id|kind|evidence_status|summary`)
  has "no explicit per-claim `uncertainty` dimension, and no claim-to-record/
  edge relation key". :28: D2 coupling appears only as the single aggregate
  row `D2-EDGES` (`packet.md` :103) — "does not expose each source→target
  relation with its own applicability and justification as §4 requires."
- **Why the shape gate stayed green**: the gate checks the 16 envelope fields
  for presence/non-placeholder plus five content rules; ledger and edge table
  interiors are free text to it. Measured again this pass (§8, probes D/E): a
  basis cell of exactly `unknown` and a status token `tentative` both exit 0.
  The semantic dimension therefore needs its own checks — the builder's, not a
  gate change (changing `tools/gates/handoff-packet-check.py` is outside the
  v2 file set).

## 2. The uncertainty dimension: `{status, basis}`

### 2.1 Carrier and form

- YAML (source of truth): each claim gains two required keys —
  `uncertainty: {status: <supported|partial|unresolved>, basis: "<text>"}` —
  beside the existing `claim_kind`, `evidence_status`, `statement`, `links`.
- Markdown (gate-facing view): the `claim_ledger` table becomes
  `claim_id | kind | evidence_status | uncertainty_status | uncertainty_basis | links | statement`.
  Column names avoid every gate glossary-header token (`gloss`, `meaning`,
  `form`, `lemma`, `definition`, bare `id`, `etymology*`) and
  `artifact_id`, so the ledger is never misread as a glossary payload (gate
  :363–371; probe A, §8).
- `evidence_status` (contract §6) is **kept, never merged or replaced**:
  claim kind, evidence status, and uncertainty remain three independent
  dimensions (contract §6 table :94–100; triage protocol §1 "keep three
  independent fields"). `uncertainty.status` says how completely *this
  packet's pinned records and checks* ground the claim **exactly as worded**;
  `evidence_status` says what kind of evidence exists (attested / inferred
  with stated bridge / contested with alternatives / invented / `(to-verify)`).

### 2.2 Status enum and definitions

| status | Definition (kotodama-side support only) | Required basis shape |
|---|---|---|
| `supported` | Every element of the claim-as-worded is grounded by named records in this packet's manifest and/or a named check with an observed result in `validation`; nothing open narrows the wording. | `grounding: <manifest artifact id, repo path, or validation check name>; owner` not required |
| `partial` | The claim holds only with a stated restriction — scope limit, translation/mediation, projection-of-records, thin or caveat-carrying source, museum/editorial caveat. | `grounding: <witness>; restriction: <the exact bound>` |
| `unresolved` | A named open question blocks the claim as worded — `(to-verify)`, a hold, pending bilateral read, missing baseline, unperformed screening on which the wording depends. | `grounding: <witness>; open: <question>; owner: <lane>` |

Hard rules:

- Exactly these three tokens; nothing else (`tentative`, `high`,
  `medium`… are builder errors). The token is case-sensitive lowercase.
- The `basis` grammar above is mandatory so the builder can parse it: the
  literal prefixes `grounding:`, `restriction:`, `open:`, `owner:` — one
  `grounding:` always; `restriction:` iff `partial`; `open:` + `owner:` iff
  `unresolved`.
- A status never inherits: an edge or record derived from a `partial`/`unresolved`
  claim carries at least that status, and a more severe one if its own
  grounding is weaker; severity order is `supported` < `partial` < `unresolved`.

### 2.3 Zero-boilerplate: what the builder enforces

The gate cannot see this dimension (probes D/E, §8), so the builder asserts:

1. status ∈ enum, per claim, no gaps (ledger row count == claim count);
2. `basis` non-placeholder and unique across claims after whitespace
   normalization — no two claims share a basis sentence;
3. the `grounding:` witness resolves: a manifest `A-NN` id, a repo path that
   exists, or a check name that appears in `validation`;
4. restriction/open/owner presence matches the status (2.2 table);
5. no basis restates only the status word or the evidence-status token
   (builder rejects a normalized basis shorter than the witness plus one
   specific clause, and rejects any basis equal to `status`/`evidence_status`
   text).

### 2.4 Decision table (input to claim D's SKILL.md table)

Apply to the atomized claim (triage protocol §2.2: one proposition per row):

| Claim archetype (from v1's actual rows) | evidence_status (§6) | uncertainty.status | Basis witness |
|---|---|---|---|
| Generative/design rule reproduced by a named gate or derivation check (v1 CL01–CL05) | invented | `supported` | the gate/check + rule record id |
| Designer interpretation explicitly scoped as author metadata (v1 CL07, D2-CL01 channel description) | invented | `supported` | the source record; wording must keep the design-only scope |
| Real-world reference with a complete audit row, passage-level inspection, and unqualified wording | attested | `supported` | audit row id + locator |
| Real-world reference whose audit is `partial-support`/`scoped-support`, or access is translation-/teaching-mediated (v1 CL08–CL12) | attested or inferred with stated bridge | `partial` | audit row id + the exact restriction (e.g. "Eggeling 1885 translation only") |
| Negative/screening statement ("no sweep performed") documented by a record key (v1 CL13) | invented (fact about the lane's own process) | `supported` for the absence as worded; the dependent approval question goes to `open_questions`, not into this status | the screening key + file |
| Attributed in-world belief; divine/existence truth deliberately unsettled (v1 CL06) | invented; §6 truth-status separate | `supported` for the attribution-as-worded; the truth question stays in `requested_decisions` (lore's) | the belief record id |
| Candidate world-fact / entity mapping awaiting a lore baseline or entity keys | candidate world-fact | `unresolved` | `open: no baseline/entity keys; owner: lore` |
| Rows under an open hold or `to-verify` (D2's 13 unresolved rank items, 21 `to-verify` lines) | `(to-verify)` | `unresolved` | the hold id + owner |

Crosswalk to the verification partition (for claim D to cite): triage
protocol §1 maps `Unknown`→`unresolved`, `Scoped-supported`/`Contested`→
`partial` (restriction preserves the disagreement), `Inspected` with
unqualified wording→`supported`; `Located` alone never rises above
`partial`. Provenance-audit format §1: `supported` ≠ improved ≠ canon.
Gate-frozen-run-standard (`corpus/knowledge/verification/gate-frozen-run-standard.md`)
supplies the freeze discipline the builder's baseline reuses.

## 3. Claim-to-record links

### 3.1 Grammar

Generalizes the committed sample's `relations:` free text
(`examples/handoff-packet.sample.yml:203–260`, e.g. `relations: "A1, A2, A3
(L01, L02, L11-L20), A4 (N04, names)"`) into machine-checkable refs:

```
links: <ref>[, <ref>…]
<ref>  := <artifact_id> "#" <selector>
<selector> := <dotted.json.key.path>   # for JSON-parseable artifacts
            | L<line-number>           # line anchor, any text file
            | <literal-token>          # token must appear in the named file
```

- `<artifact_id>` must be a row of **this packet's** `artifact_manifest`
  (e.g. `A-02`, `A-10`, `A-11` in v1's numbering — v2 re-numbers its own).
  The artifact's path and digest are already pinned by the manifest row; the
  builder re-measures the digest against live bytes (round-11 exercise rule,
  design.md §1 gap 2).
- JSON key paths address records inside the pinned bytes:
  `A-02#lexicon.L01`, `A-02#sound_changes[0]`, `A-07#beliefs.B01`,
  `A-09#bridges.BR03`. Line anchors for non-JSON bytes: `A-10#L3319`.
  Token anchors for projection channels: `A-11#R-MAT-BRIDGE-MISSING`.
- Direction is claim→record. Every `coupling_edges` row gains a `claim`
  column naming the claim(s) that assert it, giving §4's "relation to other
  records" in both directions (claim→record, edge→claim).

### 3.2 Builder assertions (semantic PASS evidence for §7)

1. every claim has ≥1 link; every ref parses; every artifact id ∈ manifest;
2. every named file exists in-repo and its live sha256 equals the manifest
   digest (row count re-measured at build time, never copied from v1's
   measured 21-file read set, which v2 extends with the v2 builder/baseline
   inputs);
3. every selector resolves: JSON key path exists in the parsed file; line
   anchor ≤ file line count; token present in the file bytes;
4. coverage: every delivered record id (D3 lexicon/names/beliefs/symbols/
   costumes/bridges; D2 records surfaced by the packet) appears in ≥1 claim
   link or edge target — no orphan records, no floating claims;
5. edge crosswalk: every edge names ≥1 existing claim id; edge count equals
   the live relation count — the D2 aggregate is gone (§5).

## 4. Serialization: packet-v2.yml and the gate

- `packet-v2.yml` is the structured source of truth (per-claim
  `uncertainty` objects and `links` lists are native YAML there) and carries
  an `envelope_markdown_view` list plus the markdown tables (ledger, edges,
  glossary payload as a literal block) so that
  `python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2.yml`
  itself reports `fields=16/16 glossary-entries=20 findings=0`. Precedent:
  `reports/round-11/handoff/packet-attempt-1.yml` ("YAML serialization of
  … the same envelope and the same 20 glossary rows in a second
  serialization, and its `envelope_markdown_view` list carries the
  `- field: value` form that tools/gates/handoff-packet-check.py
  recognizes") — gate-verified there (contract-check run #3, exit 0).
- The 20-row glossary payload stays byte-derived from
  `examples/culture-d3/packet.json` exactly as in v1 (packet.md :147–171);
  the builder re-asserts ids L01–L20 and live-status equality (round-11
  design §5).
- All round-11 recognition hazards carry over unchanged (design.md §4):
  exact `## field_name` headings; no heading whose text contains a field
  token (`scope`, `validation`, …); `unbound research` proximity kept for
  `HO-BASELINE`; no unnegated `latest` in `dependency_manifest`; the
  `canon_standing: not canonized` marker line; and **no basis/status cell on
  one line with an affirmative canon verb near "canon"** — measured this
  pass: `… certifies canon (probe)` in a basis cell → `HO-CANON-CLAIM`, exit 1
  (§8, probe C1). Pending/negation tokens between verb and canon can mask the
  finding; do not rely on that masking — write non-canon vocabulary in basis
  cells outright.

## 5. Field-by-field delta vs v1 (`reports/round-11/handoff/packet.md`)

| Field | v2 change |
|---|---|
| `packet_id` | unchanged id, new version — see `packet_version` |
| `packet_version` | `2.0.0`: required per-claim dimensions are added to the consumer-facing ledger and the D2 edge aggregate is dissolved — a breaking envelope change under contract §9 ("required-field change… MAJOR when it breaks the declared consumer contract"); the packet names what it supersedes (§9 supersedes/derived_from discipline) |
| `contract_ref` | same ID/revision, digest re-measured at build; bilateral-read-pending wording kept (§7) |
| `artifact_manifest` | read set extended with the v2 builder + baseline + this design's cited artifacts; per-row counts re-measured |
| `claim_ledger` | new columns `uncertainty_status`, `uncertainty_basis`, `links` (§2.1); every claim typed per §2.4 with a parsed basis (§2.3) |
| `coupling_edges` | atomic per-relation rows with a `claim` column: BR01–BR05 as in v1 plus one row per live D2 coupling note (v1 measured 29 `coupling_note` fields, packet.md :45/:103; builder re-measures from `examples/culture-d2/packet.d2.yml` bytes) — the `D2-EDGES` aggregate row is removed (round-12 finding :28) |
| everything else | unchanged from v1's mapped derivation (round-11 design.md §3), re-rendered from live bytes |

## 6. The durable builder (spec for O-impl; name/path may differ)

```
python3 tools/build-handoff-v2.py                  # render -> link checks -> gate -> baseline compare
python3 tools/build-handoff-v2.py --selftest       # control matrix below
python3 tools/build-handoff-v2.py --root DIR       # isolated copy (tamper controls, foreign cwd)
python3 tools/build-handoff-v2.py --baseline PATH  # default reports/round-15/handoff/expected.json
python3 tools/build-handoff-v2.py --json           # one receipt document on stdout
```

- Exit codes: 0 clean; 1 mismatch; 2 could-not-evaluate — stable `V2-*`
  codes, no traceback: `V2-VOCAB` (status enum/grammar), `V2-BASIS`
  (restriction/open/owner mismatch, too-thin basis), `V2-BOILERPLATE`
  (duplicate/placeholder basis), `V2-LINK` (unresolvable ref/selector),
  `V2-COUNT` (coverage/edge-count/entry-count), `V2-DIGEST` (manifest vs
  bytes), `V2-GATE` (gate finding), `V2-SCAN` (scan != expected), `V2-BASELINE`
  (absent/tampered), `V2-DATA` (malformed input).
- Baseline `expected.json` pins: expected exit/scan (`fields=16/16`,
  `glossary_entries=20`, `findings=0`), packet sha256, per-claim
  status histogram and basis-uniqueness pass, link-resolution pass with
  resolved-ref count, input digests — declared before implementation,
  hashes measured from bytes (round-11 design.md §8 shape). **Siting rule:**
  never under `tools/gates/expected/**` or `tools/gates/frozen/**` — the
  battery reads every `expected.json` under those roots and a non-gate
  baseline there is a `BASELINE-GATE-UNCOVERED`/`UNKNOWN` exit-2 (round-11
  design.md §8, measured addendum). `reports/round-15/handoff/expected.json`
  keeps it invisible to the battery by construction.
- `--selftest` control matrix (each: mutate → expect stable code):

| control | mutation | expected |
|---|---|---|
| positive | none | exit 0; scan 16/16 + 20/20 + 0; all links resolve |
| m1 | drop `uncertainty_status` column / key | `V2-VOCAB` |
| m2 | status `tentative` | `V2-VOCAB` |
| m3 | duplicate one basis text | `V2-BOILERPLATE` |
| m4 | basis cell `unknown` | `V2-BOILERPLATE` |
| m5 | `partial` without `restriction:` | `V2-BASIS` |
| m6 | link to an artifact id not in the manifest | `V2-LINK` |
| m7 | link selector `A-02#lexicon.L99` | `V2-LINK` |
| m8 | digest tamper in isolated copy | `V2-DIGEST` |
| m9 | collapse D2 edges back to one aggregate row | `V2-COUNT` |
| m10 | basis cell `… certifies canon (probe)` | gate exit 1 `HO-CANON-CLAIM` → `V2-GATE` |
| isolation / preservation | foreign cwd run; read-set digests before/after | identical result / unchanged |

- One stable summary line for `reports/round-15/run-validation.py`, e.g.
  `handoff-v2: exit=0 fields=16/16 glossary=20/20 findings=0 links=<n>/<n> statuses=<s/p/u> packet_sha256=<…>`.
  Writes only under `TMPDIR` (lane rule `export TMPDIR=$PWD/.scratch`);
  stdlib only; the live read set is never touched.

## 7. What the round-12-style re-audit should find (PASS and named remainders)

Expected verdict over v2: **semantic PASS on the two content findings** —
every claim carries a typed, unique, witness-resolvable uncertainty basis,
and every edge is atomic with per-edge applicability, justification, and
claim back-link (round-12 findings :27, :28 closed). Expected **remaining
gaps, named with owners** (the claim's alternative branch): (a) bilateral
same-revision read of contract `1.0.0` still pending — owner lore + both
lanes; blocks first transfer only (OQ-V2-01); (b) round-8 L0 digest question
(`50c4c2f2…` premise stale vs `5f4c02bf…`) — owner integrator/lore, non-
blocking for envelope work (OQ-V2-02); (c) no kotodama-side §1 read record
yet (`corpus/lessons/round-2-adjacency.md:76`, cited by round-11 audit
§3.1) — owner kotodama orchestrator (OQ-V2-03). These live in v2's
`open_questions` with lanes and blocking status, per §4.

## 8. Design evidence (commands and observed results, 2026-10-17)

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r15o01/probe.py    # probe A, B + C (first form); see below
python3 .scratch/r15o01/probe2.py   # probes A, C1, C2, D, E
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md \
  reports/round-12/adjacency/contract.md reports/round-11/handoff/packet.md \
  reports/round-11/handoff/design.md reports/round-11/handoff/contract-check.md \
  examples/handoff-packet.sample.yml tools/gates/handoff-packet-check.py
```

- Probe A — v2-shaped 7-column claim_ledger + atomic edges with a `claim`
  column, over the gate's own control packet, `evaluate_text` in-process:
  exit 0, `fields=16/16 glossary-entries=2 findings=0` (fixture's 2 rows).
- Probe B — appended `## uncertainty schema` heading: no field hijack
  (`uncertainty` is not a `FIELD_NAMES` member), exit 0, 16/16.
- Probe C1 — basis cell `… certifies canon (probe)`: exit 1,
  `HO-CANON-CLAIM` — the canon-verb hazard reaches basis cells.
- Probe C2 — the same with `would` before the verb: still `HO-CANON-CLAIM`
  here (the pending token sat outside the matched span); first-run variant
  with `established … would … canon` was masked. Lesson: masking is
  span-dependent — do not rely on it (§4 rule).
- Probe D — basis cell exactly `unknown`: exit 0, findings 0 — gate-invisible,
  hence builder check 2 (§2.3).
- Probe E — status token `tentative`: exit 0, findings 0 — gate-invisible,
  hence builder check 1 (§2.3).
- Digests measured: contract
  `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`;
  round-12 contract.md `9fb89a062253a9273196ee8b8122f62598d74ce6b32b124034be5029c44ba0a2`;
  round-11 packet.md `6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f`;
  round-11 design.md `39012d479c6b466572a63931073f9bce07f9eceed2df9f89f3cd83ec932a54df`;
  round-11 contract-check.md `3ccf234a49bdd2bdfaee2caed466dbdc5c868935deb3d5b751830214472ccf22`;
  sample.yml `b900549ec51f954dbbcd165066c4dacc60bb9d05aedb4fec00244921b09502e6`;
  gate `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575`.
  Scratch probe files are not deliverables and are gitignored.

## 9. Ordering, open items, to-verify for the owners

- **Ordering**: this design → O-packet populates `packet-v2.yml` (§2–§5) →
  O-impl lands the builder (§6) → O-frozen pins `expected.json` after the
  packet bytes stop moving (single writer per file; re-pin only with recorded
  reason, round-11 design.md §8) → O-contract-audit re-runs per §7 → claim D
  drafts the SKILL.md table citing §2.4 + the verification partition. If the
  D2 typed-label bytes move mid-round (round-11's O12-F4 lesson), freeze only
  after they stop.
- `to-verify` (impl owners): the live D2 coupling-note count (29 per v1
  measurement) and D3 record ids at build time — always re-measured, never
  copied; whether `run-validation.py` wants the `V2-*` codes verbatim or a
  reduced exit code (X owner).
- Non-blocking, kotodama-owned: none new — v1's OQ-E2E items carry into v2's
  `open_questions` with their lanes and blocking status unchanged.
- This file's footprint: `reports/round-15/handoff/v2-design.md` plus
  gitignored scratch probes under `.scratch/r15o01/`. No filed round-8..14
  artifact, corpus file, tool, or sibling path was written.
