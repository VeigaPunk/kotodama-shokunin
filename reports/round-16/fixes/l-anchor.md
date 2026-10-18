# R16-O02 fix — F9-1: `#L<n>` line-anchor vs record-id collision closed

- Round 16, operability lane (fixer O02). All commands run 2026-10-17
  23:34–23:42 -0300 from the lane root with `TMPDIR=$PWD/.scratch`.
- Tool: `tools/harness/packet_links.py`. Selftest + CLI probes below.
- Finding of record: round-15 `reports/round-15/handoff/review-9.md` §2 F9-1
  (harness, dangling-link class).

## 1. Finding (as routed)

`tools/harness/packet_links.py` compiled `LINE_ANCHOR_RE =
re.compile(r"^L(\d+)$")` and matched it **before** any record-token
semantics in `resolve_link`, so on a `.json` artifact the token `L99` was
consumed as "line 99" and never checked against the JSON bytes. The D3
lexeme namespace (`L01`–`L20`, no hyphen) shares the anchor shape, so a
nonexistent record resolved `ok` whenever the file had that many lines.
Reviewer reproduction, quoted: `python3 tools/harness/packet_links.py
--links "examples/culture-d3/packet.json#L99" --repo-root .` → `ok [...]
(exit 0; "L99" occurs 0 times in the file's 990 lines; line 99 is "},")`.

## 2. Fix

The design already disambiguated this and the harness had not implemented
it — `reports/round-15/handoff/v2-design.md:174-177` defines `<selector>`
as a dotted JSON key path "for JSON-parseable artifacts" OR `L<line-number>`
as "line anchor, any text file", with the worked example at :187 "Line
anchors for non-JSON bytes: `A-10#L3319`". The fix implements that split:

- `resolve_link` (tools/harness/packet_links.py:225, guard
  `if line_anchor and real.suffix != ".json":`): an `L<n>`-shaped token is
  a line anchor **only on non-JSON artifacts**; on a `.json` artifact it
  falls through to the existing JSON-selector branch (key path → exact
  value/element), so a dangling `#L99` is `L-SELECTOR-UNRESOLVED` and a
  real lexeme id (`#L01`) resolves through the bytes.
- Module docstring gains the rule bullet (tools/harness/packet_links.py:19)
  citing v2-design §3.1 and review-9 F9-1; `resolve_link`'s docstring
  grammar note says "line anchor, non-JSON artifacts only".
- Consequence table (`path` = `examples/culture-d3/packet.json`, 990 lines):

| spec | before | after |
| --- | --- | --- |
| `path#L99` (dangling id) | ok (line 99) | `L-SELECTOR-UNRESOLVED` |
| `path#L01` (real id) | ok (line 1, accidental) | ok (record bytes) |
| `A-02#L77` (artifact form, dangling) | ok (line 77) | `L-SELECTOR-UNRESOLVED` |
| `docs/contract.md#L90` (non-JSON anchor) | ok | ok (unchanged) |
| `path:78` / `path:991` (colon form) | ok / `L-LINE-RANGE` | ok / `L-LINE-RANGE` (unchanged) |

Line addressing of JSON bytes keeps working through the colon form
(`path:LINE[-LINE]`), which is unambiguous by construction; the `#L<n>`
form on JSON is now reserved for the record-id space.

## 3. Controls (negative carries its sweep; counts carry command + date)

1. BEFORE, bare (HEAD binary, reviewer probe 1, reproduced 23:35):
   `git show HEAD:tools/harness/packet_links.py > .scratch/packet_links_head.py && python3 .scratch/packet_links_head.py --links "examples/culture-d3/packet.json#L99" --repo-root .` → `ok [examples/culture-d3/packet.json#L99] / links=1 resolved=1 findings=0`, exit 0.
2. AFTER, bare (23:35): `python3 tools/harness/packet_links.py --links "examples/culture-d3/packet.json#L99" --repo-root .` → `L-SELECTOR-UNRESOLVED [examples/culture-d3/packet.json#L99] selector 'L99' resolves to no key path or value in examples/culture-d3/packet.json / findings=1`, exit 1 — exactly the control the reviewer specified.
3. BEFORE, end-to-end via packet (reviewer probe 2, fixture
   `.scratch/r16-o02-e2e.json`: one claim with links
   `["examples/culture-d3/packet.json#L99", "A-02#L77"]`, manifest row
   `A-02 → examples/culture-d3/packet.json`; run 23:40 with `--no-digests`):
   → `links=2 resolved=2 findings=0`, exit 0 (bypass confirmed end-to-end).
4. AFTER, same packet (23:40): → both specs
   `L-SELECTOR-UNRESOLVED`, `links=2 resolved=0 findings=2`, exit 1.
5. Positive twins still resolve (23:41): `python3 tools/harness/packet_links.py --links "examples/culture-d3/packet.json#L01,examples/culture-d3/packet.json#L02" --repo-root .` → `links=2 resolved=2 findings=0`, exit 0; e2e twin with `#L99→#L01` swapped → `ok [examples/culture-d3/packet.json#L01]` (the twin's `A-02#L78` now correctly fails: not a record in the bytes).
6. Regression sweep on the stamped packet (23:41): `python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .` → **`links=50 resolved=50`**, all 50 link specs still resolve, including the packet's `packet.json#L01` (×2) and `packet.json#L02` rows at `packet-v2-05.yml:377,390-391`, which now resolve via record semantics instead of the line-1/line-2 accident. The run's single finding is `M-DIGEST-MISMATCH [tools/harness/packet_links.py] live sha256 66d854... != manifest f81bc9...` — the packet's manifest self-pins the harness file's bytes, so **any** harness edit trips that row until the parent re-stamps the amended packet; it is not a link finding.
7. Line addressing intact (23:42): `--links "examples/culture-d3/packet.json:78,examples/culture-d3/packet.json:991"` → `ok [...:78]` + `L-LINE-RANGE [...:991] line 991 beyond end of examples/culture-d3/packet.json (990 lines)`.
8. Selftests green (23:42): `python3 tools/harness/packet_links.py --selftest` → **38 checks passed**, exit 0; `python3 tools/harness/packet_uncertainty.py --selftest` → 19 checks passed, exit 0 (shared dialect untouched).

## 4. Selftest growth (the standing regression control)

Four fixtures added to `_selftest` (count line is now computed, not
hardcoded): `("data/packet.json#L99", "L-SELECTOR-UNRESOLVED")` — the
dangling-`#L99` rejection; `("A-D3#L99", "L-SELECTOR-UNRESOLVED")` — the
artifact-form variant; `("A-D3#L01", True)` — real lexeme id resolves
through the record index; `("docs/contract.md#L90", True)` — non-JSON
line anchors unchanged. The pre-existing `("data/packet.json#L01", True)`
fixture now exercises record-token semantics (it used to pass as "line 1
exists", which is precisely the collision the reviewer flagged).
26 loop fixtures + 12 non-loop checks = 38, printed by the selftest itself.

## 5. Deliberate behavior change / trade-off

`#L<n>` on a `.json` artifact no longer means "line n". Packets that want
JSON byte positions use `path:LINE` (unchanged); packets that want JSON
records use the id or the dotted key path (`A-02#lexicon.L03`). This
matches v2-design §3.1's grammar as written and closes the bypass on
exactly the record-id shape the design showcases. Non-JSON artifacts keep
both anchor forms (`A-10#L3319`, `path:LINE`).

## 6. Concurrency note and handback

- `tools/harness/packet_links.py` is shared with the round-16 O01 fixer
  (F10-1 edge-source checking, `E-SOURCE-*`); edits were region-disjoint
  (their `resolve_edges`/edge fixtures, my `resolve_link`/link fixtures)
  and the combined diff is +112/−18. The final selftest (38 checks, exit 0)
  covers both fix sets.
- Handback to parent: re-stamp the packet manifest row that pins
  `tools/harness/packet_links.py` when integrating the amended packet, so
  control 6's `M-DIGEST-MISMATCH` clears; the gate battery then re-runs on
  the amended packet as planned.
- Files touched: `tools/harness/packet_links.py`; this report. Scratch
  fixtures kept as evidence: `.scratch/packet_links_head.py`,
  `.scratch/r16-o02-e2e.json`, `.scratch/r16-o02-e2e-positive.json`.
