# R20-D17 — contract-v2 audit re-run over handoff packet v3 (keyed builds 13→16)

- seat: R20-D17 (contract audit re-run), lane
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- date: 2026-10-18. Baseline revision
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (round-19 admit); observed HEAD
  `122086bce0aa577bec221bb2d37eedf20f4f3ed2` ("round-20: declare claims D/O/C").
  All readings UTC; lane clock UTC−03:00.
- protocol: the round-15 contract audit (`reports/round-15/handoff/
  contract-v2-audit.md`) re-run over the v3 bytes — field-by-field §4
  comparison, the two v2 semantic checks (uncertainty non-boilerplate,
  claim-to-record link resolution) — extended with the v3 deltas the round-20
  design fixes: the D4 rows, the v2-subset equality control (`design.md` §6.3)
  and the D4 link surface.
- audited bytes: **`reports/round-20/handoff/packet-v3-16.md`, sha256
  `9f37c08af9bd56fce668ccb42bd34351d21e650c49e27898ff7736a70dfdd730`,
  measured 2026-10-18T13:14:5xZ** (generation stamp 13:14:00Z). Builds 14–16
  are content-identical apart from the build key and run stamps (byte diff
  verified); build 13's first render (sha `3ce440d5…`, 13:10:22Z) carried the
  defects recorded in §3, and its repaired re-render (sha `5b3b8ae6…`,
  13:13:14Z) is the state builds 14–16 carry forward. The machine twin and the
  v3 baseline had not landed at audit close; twin legs are marked as declared,
  not re-measured.
- writes: **this file** plus the seat's other assigned round-20 fragments and
  gitignored scratch under `.scratch/r20-d17/` (`TMPDIR=$PWD/.scratch` before
  every scratch-writing command). No packet, tool, corpus, or filed round-8..19
  byte was written by this seat. No commit, no push.
- canon: NON-CANON engineering evidence. This audit is not a lore receipt, not
  an acceptance, and makes no rights ruling.

## 0. Verdict

**PASS on the §4 semantics, on the round-12 reject grounds, and on the v3
deltas; one advisory and two minor remainders are named with owners.** The
repaired build carries 27 claims (`{supported 16, partial 7, unresolved 4}`),
every basis unique, grammar-complete and witness-resolvable (46/46 locators),
92/92 claim-to-record links resolving (the 50 carried v2 links + 42 D4 links),
56/56 manifest digests matching live bytes, 94 atomic coupling edges with
claim back-links, the gate at `fields=16/16 glossary-entries=20 findings=0`,
and the v2-subset equality control **equal on the markdown surface** (this
seat's independent re-derivation). The initial build-13 render's major defect
(character-split `links` cells on the 15 carried rows) was repaired in the
re-render and is recorded in §3 as build history — this audit closes on the
repaired bytes.

| id | severity | finding (state on the audited build) | owner |
|---|---|---|---|
| F-A6 | advisory | bases of D2-CL02 and D4-CL09 share a 15-token tail ("none of them is promoted by this packet; owner: kotodama, blocking for the affected D2 …"); not a validator failure (bases are not exact duplicates), named for the packet seat's decision | packet seat (advisory) |
| F-A7 | minor | the CL01 basis names two D3 check events (`tools/assemble-culture-d3.py --check`, `tools/check-evidence-coupling.py`) that the `validation` section never names; the manifest rows A-18/A-21 carry the results, so the traceability exists but not in `validation` | packet seat (minor) |
| F-A3 | minor (reduced) | three `validation` rows (carried-body re-measurement, v2-subset equality, record coverage inventory) still name `python3 .scratch/r20-d13/build-v3.py --key 16` as their command — a gitignored scratch receipt that will not be filed with the round | packet seat / integrator |
| F-INT-1 | major (round-level, not packet-content) | the packet markdown carries 12 D4 claims / 27 total, while the exercise's filed twin and frozen baseline carry 9 / 24; the packet's own validation row (`claims=27`, `links=102`) is false against the filed twin (`24`, `61`). Cross-surface divergence dispositioned in `interop.md` §4 | packet seat + impl seat + integrator |

## 1. Independent measurements

All commands from the lane root with `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`, 2026-10-18.

- **13:14:5xZ** — `python3 tools/gates/handoff-packet-check.py reports/round-20/handoff/packet-v3-16.md`
  → exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0`.
- **13:14:5xZ** — this audit's independent reader
  (`.scratch/r20-d17/auditlib.py`, own parser, no harness imports) over the
  markdown: 27 claims, statuses `{16 supported, 7 partial, 4 unresolved}`;
  basis locators 46/46; links 92/92 (50 v2 + 42 D4); coupling edges 94, 0
  without a claim back-link; manifest 56/56 matched; **0 findings**.
- **13:14:5xZ** — v2-subset comparison
  (`.scratch/r20-d17/interop.py subset reports/round-15/handoff/packet-v2-05.md reports/round-20/handoff/packet-v3-16.md`):
  15/15 rows equal on `kind`, `evidence_status`, `status`, `basis`, `links`
  → `v2_subset: equal`.
- **13:14:5xZ** — adversarial checker (`.scratch/r20-d17/advlib.py`): 3
  findings (F-A6 + 2 × `ADV-VALIDATION-CITE` on CL01 = F-A7); shortest basis
  244 chars; 0 exact duplicates; 0 self-references; 0 dangling links.
- **13:14:5xZ** — the packet's own `validation` rows read (declared, not
  re-measured by this seat): `claims=27 findings=0`; `links=102 resolved=102`;
  D4 typed pipeline 19/19; five D4 structural gate runs; three D4 determinism
  runs; the alias-evidence row (no-D2-mirror positive + restored-tree
  negative, both exit 0); battery `pass 7, fail 0`; d4 adapter selftest 12/12
  without the D2 tree; d2/d4 projector selftest 50/50; d2 pipeline control
  13/13; record coverage 162 declared / 79 carried / 83 by the manifest index.
- **13:07Z** (independent flip evidence, before this build) — a scratch mirror
  holding `tools/` + `examples/culture-d4` **without** `examples/culture-d2`:
  `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml
  --check examples/culture-d4/typed-labels.d4.yml` → exit 0, "byte-identical
  deterministic projection". D4-CL08's `supported` typing is evidence-keyed.

### Controls (the protocol's own falsifiability)

| control | command | observed |
|---|---|---|
| toolchain health | `handoff-packet-check.py --selftest` | exit 0, `selftest: OK — fixture findings 11 across 9 ids` |
| negative control (the protocol that rejected v1) | this audit's reader over `reports/round-11/handoff/packet.md` | 0 v2 claims parsed, 1 `D17-LEDGER-SHAPE` finding, 6 edge rows without a claim back-link — the round-12 reject reproduced |
| positive control (v2 known-good) | this audit's reader over `reports/round-15/handoff/packet-v2-05.md` | 15 claims 8/5/2; basis locators 23/23; links 50/50; findings = the 2 documented digest drifts |
| mechanism control | `handoff-packet-check.py reports/round-11/handoff/packet-attempt-1.yml` | exit 0, `fields=16/16 glossary-entries=20 findings=0` |
| link negative control | `packet_links.py --links "packet.d4.yml#ER-99,typed-labels.d4.yml#no_such_block,expected-holds.json#counts"` | exit 1: 2 × `L-TOKEN-MISSING`, third ok |
| uncertainty negative controls | five synthetic claim sets through `packet_uncertainty.py --claims-json` | `U-BASIS-DUPLICATE`, `U-BASIS-NO-RESTRICTION`, `U-BASIS-NO-OWNER`, `U-STATUS-VOCAB`, `U-BASIS-SHORT` — all fired |

## 2. §4 field comparison

| §4 field(s) | audit |
|---|---|
| `packet_id`, `packet_version` | `kotodama.handoff.d2d3d4-e2e.v3.build16` @ `3.0.0`; the major bump is justified in-packet (third source's rows; manifest growth) and the supersedes clause names the v2 build that stays filed. |
| `contract_ref` | ID `kotodama-lore-adjacency`, revision `1.0.0`; digest re-measured by this seat: `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`, equal to the packet's value; the pending bilateral read is stated, not asserted complete. |
| `producer`, `recipient`, `request_ref` | roles named; `request_ref: none` qualified by the deliberately-unbound drill. |
| `baseline_bible_ref` | `none`, adjacent to the unbound-research declaration. |
| `artifact_manifest` | 57 rows (56 file-backed + A-GLOSS inline); the D4 read set enters as A-27..A-53; the moved tool pins are recorded as NEW rows in-row (A-20 `d2-typed-labels.py` old pin `0da0015f…` → `76536a92…`; A-25 `packet_links.py` old pin `f81bc9f7…` → `66d854cc…`) — the operator's re-pin discipline; **56/56 re-measured rows matched at 13:14:5xZ**. |
| `subject_refs` | 12 namespaced candidates, all unresolved, D4 candidates in the same form with in-repo witnesses; no lore entity id guessed. |
| `scope` | three drills; the D4 block names the fictional basin league, isolate speech with one unmodelled sister variety, fixture-relative E0–E3 (E3 reserved/unoccupied), 54 lexemes, 6 garments each owing a slot; no real place, no dates; unscreened-ASCII restated. |
| `dependency_manifest` | D2/D3/D4 tools and records pinned by digest or exact id; the D4 gates and harness validators pinned; no floating `latest` (gate-verified). |
| `claim_ledger` | **Round-12 finding closed on the carried rows and implemented on the D4 rows.** 27 rows, seven-column v3 shape; every row carries `uncertainty_status` + `uncertainty_basis`; census `{16 supported, 7 partial, 4 unresolved}`; D4-CL08 `supported` on the measured alias run. The 15 carried rows are equal to the v2 packet's rows on all five comparable fields after whitespace normalization (this seat's check). |
| `coupling_edges` | 94 atomic typed rows with `target_ids`, `claims` back-link, mechanism and limits; the v1 `D2-EDGES` aggregate stays absent; 0 rows lack a claim back-link (this seat's count). |
| `requested_decisions` | carried v2 rows + `RD-D4-01..05`; alternatives and blockers stated. |
| `validation`, `open_questions` | 20 validation rows with commands and observed results (F-A7, F-A3 name the two traceability remainders); `open_questions` carries OQ-V2-01..07 plus OQ-V3-01..07 naming every unresolved claim. |

## 3. Build history (measured during the wave; superseded by §0's audited bytes)

- **13:11–13:12Z, build 13 first render** (`3ce440d5…`, stamp 13:10:22Z):
  - **F-A1 (major)**: the 15 v2-carried rows' `links` cells were character-split
    (`e; x; a; m; p; l; e; s; …`) — the renderer joined the links *string*
    char-by-char; the 12 D4 rows were clean. My independent subset check
    returned `DRIFT` on the `links` field for 15/15 rows while the packet's own
    subset row claimed "15/15 rows equal" — its control read the machine twin,
    not the markdown surface it certifies.
  - F-A2: manifest 51/56–54/56 matched as the D4 tree re-emitted live.
  - F-A3/F-A4/F-A5: validation commands deferred to the build receipt; two
    placeholder/blank observation rows; stale v2 preamble (timestamp, row
    count).
- **13:13:14Z, repaired re-render** (`5b3b8ae6…`): links repaired (92/92
  resolve), manifest 56/56, commands restored in the validation rows, preamble
  corrected. This seat re-measured; every F-A1/A2/A4/A5 reading closed.
- **13:13:50–13:14:03Z, builds 14–16**: content-identical apart from key and
  stamps (byte diff verified). No in-place edit of a frozen byte: each repair
  landed as a new keyed file.

## 4. Uncertainty non-boilerplate verification (v2 check, v3 bytes)

Method: this audit's own checker parsed every `claim_ledger` row of the
audited markdown and, per row, validated the status token against
`{supported, partial, unresolved}`, rejected placeholder and
whitespace-normalized-duplicate bases, enforced the clause grammar
(`grounding:` always; `restriction:` iff partial; `open:` + `owner:` iff
unresolved), resolved every `path#token` locator in the basis against live
bytes, and checked that no basis opens by restating its status.

Result on the audited bytes: **46/46 basis locators resolve**; zero
placeholder, zero exact-duplicate bases; every partial row carries a
restriction; every unresolved row carries open + owner; no basis restates its
status token. **F-A6** (advisory): the D2-CL02 / D4-CL09 pair shares a 15-token
tail — below exact-duplicate detection, above this audit's template heuristic,
named rather than absorbed.

## 5. Claim-to-record link resolution (v2 check, v3 bytes)

- Carried v2 rows: 50/50 resolve on the markdown surface (the build-13 defect
  is repaired).
- D4 rows: 42/42 resolve, all into `examples/culture-d4/**` and the round-18
  receipts; the pre-render control resolved the 37 unique `claims-map.md` specs
  37/37 under two independent resolvers (`review-adversarial.md` §2).
- Edges: 94 rows, each naming a claim id (this seat's count); the inverse
  direction (§4 "relation to other records") holds.
- The packet's twin leg (`links=102 resolved=102`) is contradicted by the filed
  twin at this stamp: `reports/round-20/handoff/twin.json` (sha `b3e2bad7…`)
  measures **24 claims / 61 links / 48 edges** under the harness readers, while
  the markdown carries 27 claims / 92 links / 94 edges. The two surfaces are
  the round's central integration divergence and are dispositioned in
  `interop.md` §4 (F-INT-1): the packet's validation row measured a twin that
  is not the filed one, and the D4 claim census differs (12 vs 9) between the
  packet seat's render and the exercise tool's assembly.

## 6. Governance remainders carried (not packet-content defects)

- Bilateral same-revision read of contract 1.0.0 still pending — owner: lore +
  both lanes (OQ-V3-01).
- Round-8 L0 contract-digest question — owner: integrator/lore, non-blocking
  (OQ-V3-02).
- No kotodama-side §1 read record — owner: kotodama orchestrator (OQ-V3-03).
- D4 residuals (12 form holds + 3 rank holds + 1 note; 13 unresolved rank
  items; 4 conflicts) carried open, not resolved by the packet (OQ-V3-05).
- The round-19 alias wart: closed in the projector at this build (per-family
  resolution landed; D4-CL08 re-typed on the measured run; the packet's
  adapter-selftest row now records the mirror-without-D2 run 12/12) — the
  remaining re-pin cascade is recorded in `regression-v2.md` §0 F19-1/F19-2.

## 7. Lore boundary and PROVINCE

`PROVINCE.md` keeps this lane on generative/coupling craft and routes canon to
lore. The audited bytes stay inside that boundary: `canon_standing: not
canonized`; `handoff_status: prepared-not-accepted`; deliberately unbound;
subject refs unresolved; screening refusal explicit; uncertainty statuses are
kotodama-side support language and never mean accepted, import-ready, or canon.
Boundary verdict: pass for this exercise; not a lore receipt or transfer
authorization.

## 8. Disposition

- **Verdict: PASS-with-named-minors on the audited build.** The round-12 reject
  grounds stay closed; the D4 rows are conformant, witnessed and linked; the
  gate and the v2-subset control are green on the surface this seat measured.
- Route F-A6 (advisory), F-A7 and F-A3 (minors) to the packet seat; none blocks
  the D claim's own reading.
- Re-run this protocol on any superseding keyed build as a new file; this
  report is not an edit surface.
