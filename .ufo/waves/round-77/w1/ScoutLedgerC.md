# ScoutLedgerC — round 77 RECON (README/index, older files)

Base: `211f9526800906e0c585d878d265c37e5e090c15`. Pairs: `.ufo/waves/round-77/w1/stage/ScoutLedgerC/pairs.json`.

## Observed measurements

- 41 culture-material Markdown files — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/culture-material/ | grep -c '\.md$'`; raw output: `41`.
- Partition counts — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && for d in linguistics myth-symbol culture-material synthesis verification civilizations; do n=$(git ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/$d/ | grep -c '\.md$'); echo "$d: $n"; done`; raw output: `linguistics: 32`, `myth-symbol: 32`, `culture-material: 41`, `synthesis: 29`, `verification: 24`, `civilizations: 95`.
- 253 total Markdown files — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git ls-tree -r --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge | grep -c '\.md$'`; raw output: `253`.
- README section-row counts — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/README.md | awk '/^## /{sec=$0; cnt[sec]=0; order[++n]=sec; next} /^- `.*\.md`/{cnt[sec]++} END{for(i=1;i<=n;i++) printf "%5d  %s\n", cnt[order[i]], order[i]}'`; relevant output: `30 ## linguistics/ (32)`, `41 ## culture-material/ (41)`.
- The exact stale heading/count text exists — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git grep -n -E 'linguistics/ \\(30\\)|culture-material/ \\(36\\)|live directory holds 40 files|section 38 rows|Total knowledge entries: 252|total 252 files' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/README.md`; raw output identifies README lines 791, 811, 812, 830 and 832 (plus the existing heading 32 / 41 matches).
- Directory-vector line discrepancies corroborated — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/README.md | sed -n '789,836p' | awk 'NR>=42 {print}'`; raw lines at absolute README lines 830, 832, 834, 836 show 252 then 253 and vectors ending 40 then 41. Latest line 836 vector is `32/32/41/29/24/95`.
- REPAIR candidates are 5 entries in pairs.json, all on mutable `corpus/README.md`: retained linguistics heading token 30 vs heading token 32; retained culture-material heading token 36 vs 41; round-74 present-tense directory count 40 vs 41; older footer total 252 vs 253; older footer vector total 252 / culture-material 40 vs 253 / 41. The exact observe commands and parsed tokens are recorded in each pair.

## Requested older-file sweep

- `corpus/QUALITY.md` scan — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/QUALITY.md | grep -nE '[0-9]|S[0-9]{3}' | head -60`; raw output shows numbered criteria and historically scoped anchors/examples. I found no independently verified unannotated token mismatch in this file. A broad numeric match is not proof of a mismatch.
- `corpus/lessons/round-74.md` scan — `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/lessons/round-74.md | grep -nE '[0-9]' | head -80`; raw output includes its dated claims and row references. Its explicit R74-M4 `9` vs `10` scenario mismatch is already corrected/annotated: `git grep -n -E 'ACCEPT-C-73: PASS|SELFTEST OK: 10 scenarios|reports/round-73/telemetry/selftest-r3.txt' 211f9526800906e0c585d878d265c37e5e090c15 -- LOG.md SCORECARD.md corpus/lessons/round-75.md corpus/lessons/round-76.md` returns SCORECARD round-74 rows LC-02/LC-03 (9→10), and lesson line 237 says “annotated by ledger rows LC-02/LC-03.” Its stated R74 M4 pair is specifically on LOG.md and fleet report; I did not duplicate it.
- Allowlist issue: round-77 draft allows ANNOTATE only at LOG.md, SCORECARD.md and round-75/76 lessons; it excludes QUALITY.md and round-74 lesson. The README findings are REPAIR-eligible, so the candidate set emitted here is repair-only, not a fabricated mixed set. This seat did not identify a sound, unannotated ANNOTATE candidate in the allowed files.

## Forecast for naming-systems.amend

- If `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` is added as one new Markdown file, the measured base totals forecast 254 overall and 33 linguistics; culture-material remains 41. This follows the base values above plus one file, not a measured post-landing tree. The latest README total/vector and the actual linguistics heading would need to advance (253→254; 32→33). The existing `## linguistics/` section presently contains 30 rows while the heading says 32: two Round-73 addition rows are separately appended, so an index update also needs to honor that layout rather than infer section rows from the heading.

No checks/builds/tests run. No installs. No unresolved tool failures.
