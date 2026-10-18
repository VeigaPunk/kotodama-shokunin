# shard-2 — claim-to-record link resolver (O R15-O04, impl support for O02)

- Date: 2026-10-17 (UTC stamps below are 2026-10-18T00:38–00:47Z). NON-CANON;
  no real-world rights ruling; no canon decision; no filed round-8–14
  artifact touched; packet-v2.yml and its builder are other assignments.
- Deliverable: `tools/harness/packet_links.py` — stdlib-only resolver that
  makes claim-to-record links and coupling edges checkable against real repo
  records, closing the second round-12 reject reason
  (`reports/round-12/adjacency/contract.md:28`, quoted: "D2 is summarized as
  one aggregate dependency edge … That aggregate does not expose each
  source→target relation").

## What it resolves (conforms to v2-design.md §3.1–§3.2)

- Link spec forms: `<path>`, `<path>#<token>`, `<path>:LINE[-LINE]`
  (1-based inclusive), and the design's artifact form
  `<artifact_id>#<selector>` where the id is a row of the packet's own
  `artifact_manifest` and the selector is `L<n>` (line anchor), a dotted
  JSON key path with `[N]` indices (`A-02#sound_changes[0]`), or a literal
  token. Unknown artifact ids fail `L-ARTIFACT-UNKNOWN` instead of
  masquerading as paths.
- JSON selectors: key path first; on a miss, exact value/element search for
  the full selector and then the tail segment (the live D3 packet's lexicon
  is a list of `{id: L01}` rows, so `lexicon.L01` resolves through the id
  value). Non-resolving selectors: `L-SELECTOR-UNRESOLVED`.
- Paths must exist inside the repo root with symlinks resolved — an escape
  is `L-PATH-OUTSIDE`, not a crash (`L-PATH-MISSING` otherwise; bad ranges
  `L-LINE-RANGE`; missing tokens `L-TOKEN-MISSING`).
- Manifest rows: `build_record_index` maps every record id and artifact id
  to its path; `verify_manifest_digests` re-measures live sha256 against
  each row's pinned `digest`/`sha256` (`M-DIGEST-MISMATCH`,
  `M-DIGEST-MISSING`) — design §3.2 assertion 2, on by default in packet
  mode (`--no-digests` to skip).
- Coupling edges: every `target_ids` entry must be one concrete record id in
  the index whose path resolves (`E-TARGET-UNKNOWN`, `E-TARGET-UNRESOLVED`),
  so range tokens like `L-01–L-40` cannot pass as an aggregate edge; an edge
  naming no existing claim id (`claim`/`claims` column) fails
  `E-EDGE-NO-CLAIM`; declared aggregates fail `E-EDGE-AGGREGATE`.
- Same exit contract and deterministic output as shard-1's tool.

## Receipts (commands as run, from the repo root)

- 2026-10-18T00:46:48Z — `python3 tools/harness/packet_links.py --selftest`
  → exit 0, quoted: `selftest: 31 checks passed (path/token/line specs,
  artifact-id refs, JSON key paths, L-anchors, symlink escape, digests,
  record index, aggregate+claim crosswalk rejection)`.
- 2026-10-18T00:38:59Z — real-record smoke, `python3
  tools/harness/packet_links.py --repo-root . --links
  "corpus/knowledge/synthesis/worldbible-integration-contract.md:49-70,
  examples/culture-d3/packet.json#SC1,examples/culture-d3/packet.json#speech_rules,
  reports/round-12/adjacency/contract.md:27,reports/round-12/adjacency/contract.md:28"`
  → quoted `links=5 resolved=5 findings=0`, exit 0 (contract §4 heading line
  and both reject lines resolve; D3 record ids resolve inside pinned JSON).
- 2026-10-18T00:39:05Z — negative controls, same command over
  `examples/culture-d3/packet.json#GHOST` and
  `corpus/knowledge/synthesis/worldbible-integration-contract.md:99999` →
  quoted: `L-TOKEN-MISSING … token 'GHOST' not found` and
  `L-LINE-RANGE … line 99999 beyond end of … (209 lines)`, exit 1.
- 2026-10-18T00:46:48Z — v2-shaped scratch fixture
  (`.scratch/v2-shaped.yml`, design-form refs) → quoted `ok [A-D2L#coverage]`
  / `ok [A-D3#sound_changes[0]]` / `ok [A-D3#lexicon.L01]` /
  `links=3 resolved=3 findings=0`, exit 0. Its manifest rows pin
  `examples/culture-d3/packet.json` at
  `sha256:bdf635ceaed4eb2f…af4829` and
  `examples/culture-d2/typed-labels.d2.yml` at `sha256:a3aa452cd5ae77c3…4a43`
  — the same digests v1's dependency manifest records
  (`reports/round-11/handoff/packet.md`, dependency_manifest section) — and
  the default digest pass re-measured both live files with zero mismatches.
- 2026-10-18T00:46:09Z — v1-shaped twin (one aggregate edge with range
  tokens, no claim column) → quoted: `E-EDGE-NO-CLAIM [D2-EDGES] edge names
  no existing claim id` / `E-TARGET-UNKNOWN [D2-EDGES] target 'L-01–L-40' is
  not a concrete record ID in the artifact_manifest index` /
  `E-TARGET-UNKNOWN [D2-EDGES] target 'NM-01–NM-08' …` / `links=0
  resolved=0 findings=3`, exit 1. Control: the exact v1 `D2-EDGES` shape
  fails mechanically; the v2 twin with per-record edges passes.

## Defects found and fixed during the build, each with its control

1. Failed link rows printed twice in human output (rows loop plus findings
   loop) → rows loop now prints resolved rows only; control: re-run v2 twin,
   each spec appears once, counts unchanged.
2. JSON selector fallback searched the full dotted selector, so
   `lexicon.L01` missed the list-shaped live packet → tail-segment probe
   added; controls: `A-D3#lexicon.L01` resolves against real bytes while
   `A-D3#beliefs.GHOST` and `A-D3#sound_changes[7]` still fail
   `L-SELECTOR-UNRESOLVED` in the selftest.
3. Selftest expectation drift as the grammar grew (per-target findings for
   one aggregate edge; artifact ids entering the record index) — resolver
   behavior was correct; controls: aggregate semantics now isolated in their
   own fixture, claim crosswalk in another.

## Limits (stated, not absorbed)

- Coverage (§3.2.4: no orphan records, no floating claims) and edge-count
  equality with the live relation count are builder-side assertions; this
  tool supplies the primitives (per-link rows, record index, edge
  findings), not the coverage walk.
- Digest equality proves the bytes are unchanged, not that a record count
  interpretation is true.
- The `claim`-column crosswalk checks that named claim ids exist; whether
  the relation is justified is §4 review content, not a resolver verdict.
- No `handoff-packet-check` run is claimed here; the gate pass belongs to
  the packet assignment once `packet-v2.yml` exists.

## Integration cross-check against the landed packet (read-only, routed)

- 2026-10-18T00:48:24Z — `python3 tools/harness/packet_links.py --packet
  reports/round-15/handoff/packet-v2-05.yml --repo-root .` (read-only;
  packet landed from a parallel worker) → quoted: `links=40 resolved=40
  findings=34`, exit 1. The 40 claim-to-record links ALL resolve to real
  repo records — the round-12 "(b)" requirement is met on the live packet.
  All 34 findings are `E-EDGE-NO-CLAIM` (edges D2E-16…D2E-29 and the D3
  bridge rows name no existing claim id in a `claim`/`claims` column,
  v2-design.md §3.1's edge crosswalk); no `L-*` resolution finding, and no
  `M-DIGEST-MISMATCH` surfaced in the code census
  (`Counter({'E-EDGE-NO-CLAIM': 34})`).
- Disposition: this shard does not edit the packet. Delta routed to the
  packet owner + O02 builder: add the edge→claim crosswalk column (or the
  builder passes `claim_ids=None` until it lands). The aggregate-edge
  rejection, record-index, and digest machinery all passed against live
  bytes.
