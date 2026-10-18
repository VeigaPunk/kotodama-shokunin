# shard-1 — uncertainty-field validator (O R15-O03, impl support for O02)

- Date: 2026-10-17 (UTC stamps below are 2026-10-18T00:3x–00:4xZ). NON-CANON;
  no real-world rights ruling; no canon decision; nothing here edits a filed
  round-8–14 artifact or the packet itself (packet-v2.yml and its builder are
  other assignments).
- Deliverable: `tools/harness/packet_uncertainty.py` — stdlib-only validator
  for the per-claim uncertainty dimension the round-12 audit found absent
  (`reports/round-12/adjacency/contract.md:27`, quoted: "the table has no
  explicit per-claim `uncertainty` dimension"). It closes the
  gate-invisibility gap the design names (`reports/round-15/handoff/
  v2-design.md:41-42`, probes D/E): a placeholder basis or off-vocabulary
  status token is now a hard finding.

## What it enforces (conforms to v2-design.md §2.2–§2.3)

- `uncertainty: {status: <supported|partial|unresolved>, basis: "<text>"}`
  on every claim; exact key set (extra/missing keys flagged: `U-FIELD-EXTRA`,
  `U-FIELD-PARTIAL`); missing field entirely: `U-FIELD-MISSING`.
- Status vocabulary is exactly the three design tokens (`U-STATUS-VOCAB`
  otherwise).
- Basis grammar (§2.2 hard rules): mandatory literal `grounding:` clause
  (`U-BASIS-NO-GROUNDING`); `restriction:` iff `partial`
  (`U-BASIS-NO-RESTRICTION`); `open:` + `owner:` iff `unresolved`
  (`U-BASIS-NO-OPEN`, `U-BASIS-NO-OWNER`). `parse_basis(basis)` exposes the
  slots so the O02 builder can resolve witnesses.
- Zero boilerplate: non-empty (`U-BASIS-EMPTY`), ≥ `--min-basis-len` chars
  (default 40, `U-BASIS-SHORT`), boilerplate-token free (`U-BASIS-BOILERPLATE`),
  unique across claims after whitespace+casefold normalization
  (`U-BASIS-DUPLICATE`; deliberately stricter than the design's
  whitespace-only rule — documented here so the builder can relax it by
  passing its own comparer if needed), and never a bare restatement of the
  status or evidence_status token (`U-BASIS-RESTATES`).
- Optional `--require-oq`: every `unresolved` claim must be referenced by an
  `open_questions` row (`U-OQ-UNROUTED`), keeping unresolved items routed
  rather than dropped.
- Reads JSON or the lane's `yaml_lines()` dialect
  (`tools/assemble-d2.py:72-95`), compact `- key: value` items included, via
  a parser shared in shape with `tools/harness/packet_links.py`.
- Exit contract: 0 = no findings, 1 = findings, 2 = usage/IO. Output is
  deterministic (no clocks/paths) so the builder can freeze it.

## Receipts (commands as run, from the repo root)

- 2026-10-18T00:45:27Z and 00:46:48Z — `python3
  tools/harness/packet_uncertainty.py --selftest` → exit 0, quoted:
  `selftest: 19 checks passed (uncertainty rules, boilerplate, oq routing,
  yaml_lines dialect compact+bare)`. 19 fixtures: clean trio, routed and
  unrouted unresolved cross-checks, and negatives X1–X14 covering missing
  field, non-map, extra key, partial key set, off-vocabulary status, empty/
  short/boilerplate basis, duplicate basis, near-miss non-duplicate,
  missing grounding, partial-without-restriction, unresolved-without-owner,
  and a status-restating basis.
- 2026-10-18T00:46:48Z — `python3 tools/harness/packet_uncertainty.py
  --packet .scratch/v2-shaped.yml` (scratch fixture with design-form bases)
  → `claims=2 findings=0`, exit 0.
- 2026-10-18T00:39:35Z — same command over the v1-shaped twin (claims with
  no uncertainty field, the round-12 reject shape) → quoted:
  `U-FIELD-MISSING [D2-CL01] claim has no uncertainty field` /
  `U-FIELD-MISSING [CL01] …` / `claims=2 findings=2`, exit 1. Control: the
  reject is mechanically visible, not prose.
- 2026-10-18T00:39:59Z — duplicate-basis control: two claims sharing one
  basis → quoted: `{"code": "U-BASIS-DUPLICATE", "claim_id": "B", "detail":
  "basis identical to claim A"}`.

## Defects found and fixed during the build, each with its control

1. Dialect parser missed compact `- key: value` items → added
   `_expand_inline_dashes` (bare-identifier keys only, so scalar items like
   `- docs/x.md:53-70` stay scalars); control: compact + bare-dash dialect
   fixtures in the selftest must both parse to identical claims.
2. Sibling bare-dash items broke sequence parsing (break compared the
   content column, not the dash column) → `_parse_block` sequence loop now
   keys on the first item's dash column; control: the bare-dash fixture
   (`  -` then keys two columns deeper, the exact `yaml_lines()` emission).
3. Three selftest expectations were themselves wrong (duplicate-detection
   fixtures reusing the base basis; a "duplicate" that differed; an
   over-nested scalar list) — validator behavior was correct in all three;
   controls: the corrected fixtures isolate one defect each, X10 proves a
   near-miss (`basis + "!"`) stays clean.

## Limits (stated, not absorbed)

- Witness RESOLUTION (§2.3 check 3: manifest id / repo path / check name) is
  checked for presence here; resolving it to live bytes is the link
  resolver's job (shard-2) plus the builder's digest re-measurement.
- The 40-char floor and casefold dedup are heuristic strengthenings of
  "zero boilerplate"; they bound sloppiness, they do not judge truth.
- Coverage of the verification partition (which archetype maps to which
  status) is claim D's SKILL.md table, crosswalked in v2-design.md §2.4;
  this tool does not classify claims automatically.
- Counts above are tool-fixture counts, not packet claims; no
  `handoff-packet-check` run is claimed here — the shape gate belongs to
  the packet assignment (`packet-v2-05.yml` landed from a parallel worker
  mid-round; see the integration cross-check below).

## Integration cross-check against the landed packet (read-only, routed)

- 2026-10-18T00:48:12Z — `python3 tools/harness/packet_uncertainty.py
  --packet reports/round-15/handoff/packet-v2-05.yml --json` (read-only;
  `packet-v2-05.yml` landed from a parallel packet worker this session) →
  the dialect parser reads the packet natively: `claims: 15`, zero parse
  errors. Findings: 26, all basis-grammar: 13× `U-BASIS-NO-GROUNDING`,
  5× `U-BASIS-NO-RESTRICTION`, 4× `U-BASIS-NO-OPEN`, 4× `U-BASIS-NO-OWNER`.
  Spot check 2026-10-18T00:48:24Z, claim CL01 basis quoted: `grounding`
  content is present as free text (`examples/culture-d3/packet.json#SC1
  sound_changes[0] declares /p/ greater-than /f/ …`) but without the
  design's literal `grounding:` prefix (`reports/round-15/handoff/
  v2-design.md:118-121`: "The `basis` grammar above is mandatory so the
  builder can parse it: the literal prefixes").
- Disposition: this shard does not edit the packet (not my file). The delta
  is routed to the packet owner + O02 builder: either the bases gain the
  literal prefixes, or the builder calls this validator with a relaxed
  grammar mode. Status vocabulary, per-claim coverage (15/15), uniqueness,
  and boilerplate checks produced no findings on the live packet.
