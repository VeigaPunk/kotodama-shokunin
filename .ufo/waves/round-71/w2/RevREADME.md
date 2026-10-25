# RevREADME — round 71 wave 2 (falsify seat)

Scope: `corpus/README.md` revision 2.21 against the observed claim-C landing at lane HEAD `14c88d9`
(base = `65ff151`, parent of data commit `498db73`). Read-only; no lane writes besides this file.
No tools installed or updated.

## Verdict: PASS. No actionable findings.

| Check | Command | Observed | Result |
|---|---|---|---|
| README sweep | `python3 reports/round-28/readme/sweep.py` | rows 243 / files 243; missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}; totals_line 243; footer 243 `30/29/36/29/24/95`, footer_ok True; sha256 `7c17fd0c…a6ba83` | PASS (exit 0) |
| Revision labels | `python3 tools/check-readme-revisions.py` | 28 labels strictly decreasing 2.21…1.3; **findings 0**; 1 warning (see R1) | PASS (exit 0) |
| Row order | rows under `## culture-material/` extracted, then `LC_ALL=C sort -c`, then `diff` against `ls corpus/knowledge/culture-material/*.md` | 36 rows, sorted, equal to the file set. `dance-performance-movement-codes.md` is at README:418, between `cuisine-food-lexicon.md` (417) and `dress-through-eras.md` (419) | PASS |
| Topic verbatim | README:418 compared with entry line 20 `- topic:` | byte-equal text | PASS |
| Header 34→36, "stale at 34 against 35 files" | `git show 65ff151:corpus/README.md \| grep '^## culture-material/'` → `(34)`; `git ls-tree --name-only 65ff151 corpus/knowledge/culture-material/ \| grep -c '\.md$'` → 35; HEAD → `(36)` and 36 files | matches the claim | PASS |
| Totals and footer 242→243 | base README:723 `Total knowledge entries: 242.`, :727 `total 242 … 30/29/35/29/24/95`; HEAD :732 `243`, :736 `243 … 30/29/36/29/24/95` | matches the claim | PASS |
| Registry 784 + 13 = 797 | `grep -cE '^\| ?S[0-9]+' corpus/SOURCES.md` → 797 (base 784); S861–S873 unique count 13; `uniq -d` on IDs → none | matches the claim | PASS |
| 0 base owners | frozen `before` sweeps re-run against base blobs (find `*danc*` and the topic-line grep in culture-material) | both empty at base; at HEAD the only owner is the entry. `python3 reports/round-71/accept-c.py` → `ACCEPT-C-71: PASS`, all 7 legs PASS, exit 0 | PASS |

## Residual notes (no fix required)

- **R1 — REVISION-ORPHAN warning is pre-existing and not caused by 2.21.** At HEAD it spans lines 225–236; at base (`--readme` on the `65ff151` blob) it spans 214–225, the same paragraph shifted down by the 11 lines the 2.21 block adds. The paragraph was introduced in `3b13a2f` (round 28). It is a warning, not a finding.
- **R2 — "0 word-bounded … topic-line owners" leaves its scope implicit.** The frozen sweep covers only `corpus/knowledge/culture-material/`, and the 2.21 prose does not say so. Corpus-wide, the base topic line of `civilizations/lakota-plains.md` contains a word-bounded "Sun Dance". That is a passing mention, not a register owner, so the claim holds in substance. The prose is just less precise than `claims.json`, which also omits the directory scope but points to the `before` commands.
- **R3 — the frozen pattern `\bdanc\b` cannot match "dance"** (`echo dance | grep -cE '\bdanc\b'` → 0); CritClaimSizing raised this in wave 1. I re-ran the base sweep with stems (`\b(danc[a-z]*|choreograph[a-z]*|performanc[a-z]*|movement culture)\b`) over the base culture-material topic lines and got 0 hits, so the 0-owner fact survives the stronger pattern.

## Verification gaps

- No LSP applies (Markdown and Python scripts). All checks are direct command runs at HEAD plus `git show` reads of base blobs.
- Untracked `reports/round-71/telemetry/measures-c.txt` exists in the working tree. I did not inspect it because it is out of scope.
