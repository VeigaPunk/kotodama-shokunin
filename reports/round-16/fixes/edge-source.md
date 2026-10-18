# R16-O01 / F10-1 — edge `source` resolved through the record index

Fix seat: fixer (O lane shard), round 16, run 2026-10-17T23:36-03:00.
Finding of record: `reports/round-15/handoff/review-10.md` §F10-1
("resolve_edges() never checks the edge source"), owner recipe: "resolve
`source` through the record index exactly like targets. Control: rerun the
pk1 fixture; expected after fix: `E-SOURCE-UNKNOWN`, exit 1."

## Change

`tools/harness/packet_links.py`, `resolve_edges()` (was lines 299-351 at
baseline `16652e822e9dd5d83f7ab9e6078cbf010fc8f7e6`; the function body now
opens with a source gate before the target loop):

- missing/empty `source` column → `E-EDGE-NO-SOURCE` (mirror of the existing
  `E-EDGE-NO-TARGETS`);
- `source` naming no concrete record ID in the `artifact_manifest` index →
  `E-SOURCE-UNKNOWN` (this is the v1-style aggregate class: a prose source
  like "29 coupling_note fields over examples/culture-d2/packet.d2.yml" can
  no longer pass with concrete targets and a real claim id);
- `source` present in the index but its record path not resolving →
  `E-SOURCE-UNRESOLVED` (same `resolve_link` path targets use).

Module docstring and the `resolve_edges` docstring updated to match. No
change to link resolution, target checking, digest verification, or the
packet reader; `resolve_edges` signature unchanged. Diff: 101 insertions,
17 deletions, one file.

## Selftest controls added (31 → 35, all green)

New fixtures in `_selftest`:

1. prose aggregate survivor (the exact review-10 pk1 shape) →
   `E-SOURCE-UNKNOWN`;
2. edge with no `source` at all → `E-EDGE-NO-SOURCE`;
3. aggregate edge-id `D2-EDGES` reused as a source label →
   `E-SOURCE-UNKNOWN` (not a record id);
4. source in index whose path does not resolve → `E-SOURCE-UNRESOLVED`.

Existing edge fixtures (`edges_ok`, `aggregate_like`, `claim_crosswalk`)
gained a valid `source: S01` (new manifest row `A-SRC` →
`data/packet.json`), so their assertions still pin exactly the codes they
pinned before; the clean-edge control now proves a source-validating edge
passes clean. Index-set and digest assertions updated for the added row.

## Commands and results (2026-10-17T23:36-03:00, lane root)

Before (baseline `16652e82`, pre-edit bytes):

```
python3 tools/harness/packet_links.py --selftest
→ selftest: 31 checks passed …  exit 0
python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .
→ links=50 resolved=50 findings=0  exit 0
```

After:

```
python3 tools/harness/packet_links.py --selftest
→ selftest: 35 checks passed (… edge-source resolution: prose aggregate /
  missing / aggregate-id / unresolvable source rejected)  exit 0
python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root . --no-digests
→ links=50 resolved=50 findings=0  exit 0
```

Live pk1 negative control (reviewer reproduction, fixture
`.scratch/r16-f10-1-pk1.yml`, prose-source aggregate survivor plus a
source-less edge, `--no-digests` to keep findings targeted):

```
python3 tools/harness/packet_links.py --packet .scratch/r16-f10-1-pk1.yml --repo-root . --no-digests
→ E-SOURCE-UNKNOWN [E-AGG-SURVIVOR] … E-EDGE-NO-SOURCE [E-NOSRC] …
  findings=2  exit 1
```

That is the review-10 expected-after receipt: `E-SOURCE-UNKNOWN`, exit 1.

Neighbor check (untouched module):
`python3 tools/harness/packet_uncertainty.py --selftest` → 19 checks passed,
exit 0.

## Interaction notes for the parent

- With digests enabled, the filed round-15 packet now reports exactly one
  finding: `M-DIGEST-MISMATCH [tools/harness/packet_links.py]` — the packet's
  `artifact_manifest` pins the pre-edit harness digest. That is the digest
  control working; it clears on the next keyed packet build (the amended
  packet re-pins current bytes). Round-15 filed bytes were not modified.
- F10-4 (review-10) noted `<artifact>#L01` edge specs would line-anchor —
  that is the F9-1 collision fix (separate seat); this fix does not touch
  anchor handling, so no overlap in the diff.
- Scratch fixture lives in `.scratch/` (TMPDIR-prefixed), not a filed
  artifact; safe to prune after the parent re-runs the battery.
