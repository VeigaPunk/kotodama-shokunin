# ScoutQuarantine (round 76, wave 1) — item-10 quarantine recon

Verdict: slice = 21 rows (unchanged); no planned/candidate row IS a slice row; ZERO rows need a hand-check or fetch this round; one coupling to repair (entry (a) body ids S807/S750/S777).

## 1. Slice re-derived
Command: `R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md; awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' "$R"` -> `.ufo/waves/round-76/w1/stage/ScoutQuarantine/quarantine-slice`
- `wc -l` -> 21; `grep -c 'S[0-9]'` -> 21; `grep -cvE 'S[0-9]+'` -> 0 (every line carries an S-id). sha256 cd9040e1c7e8f2120e5640e98b4d30d14ea3afc322272d9631755799e1883c89.
- ids: S776 S778 S779 S786 S787 S791 S792 S795 S796 S804 S814 S816 S817 S820 S823 S824 S825 S827 (18 payload-absent) + S807` S812` S835` (3 unreachable-class; trailing backtick is a register-cell artifact, same as round 75 noted).
- Count still 21 = round 75's 21.

## 2. Round-75 verdict histogram (round 75 carried round-71's verdicts, `corpus/lessons/round-75.md` lines 137-140)
Command: `cd reports/round-71/telemetry; for p in PRESENT REFUSED UNVERIFIABLE; do echo $p $(grep -c "| $p |" quarantine-verdicts.md); done; grep -cE '^\| S[0-9]{3} \|' quarantine-verdicts.md`
Output: `PRESENT 10` / `REFUSED 7` / `UNVERIFIABLE 4` / `21`. File sha256 at base 98c486b == working tree (3f993b0c…512ea, `git show 98c486b:… | sha256sum` vs `sha256sum`).
PRESENT: S776 S778 S795 S796 S804 S820 S823 S824 S825 S827. REFUSED: S779 S786 S787 S792 S814 S816 S817. UNVERIFIABLE: S791 S807 S812 S835.

## 3. Entry (a) mentions of S807/S750/S777
Command: `grep -n 'S807\|S750\|S777' .../culture-material/calendar-festival-systems.amend-2026-10-24.md`
- :15 `S777` (gap-filled: "the drafter's interpretation PDF was already held (S777)"); :65 and :90 `S807` ("third-party reproduction (S807)"); :86 `S750` ("tier A from the official registry record (S750)").
- These are in-body CITATIONS (each is a parenthetical that names a source as support), not `source:` header lines and not couplings. They are campaign-namespace ids; the header ids S937/S935/S932/S919/S921 are also mentioned in the body (lines 8,31,39,44,59-62,95).
- They do NOT resolve to the intended documents in the lane registry at base (`git show 98c486b:corpus/SOURCES.md | grep -E '^\| *S<id> *\|'`): lane S807 = Li Yong Ming 2021 meridian paper (J. Anatomy); lane S750 = Culin, Games of the North American Indians; lane S777 = absent (no row). Campaign S750 = Names 69(3) DOI, campaign S777 = Japanese naming study (`shokuknow/.ufo/scopes/corpus-expansion-{3,6}/ScoutKotodama.md`) — neither is GB/T 33661 or an interpretation PDF. The register's S807 row (line 333) is yet another document (Onoma DOI 10.34158/ONOMA.51/2016/8, UNVERIFIABLE).
- Consequence for round 76: S807 collides with a slice row id (UNVERIFIABLE, different document); this is not an adoption of the slice row, but if the entry is admitted as staged, it prints a lane-namespace id that points at an unrelated document and, for S807, a slice id. Same for S750 (lane id exists, wrong doc) and S777 (no lane row). This hits the draft's kill rule "a cited campaign-namespace id". Action: re-point by document at admission — S807 (GB/T reproduction) -> planned lane S895 (xingzuobaike; S916), S750 (registry record) -> planned S896/S897 (openstd), S777 (drafter's interpretation PDF) -> a lane row only if the document is already held (unresolved: no lane id found; either drop or open as a row). Do not edit the register row S807 (clearing condition 1).
- Sweep (negative claims): `grep -noE '\bS[0-9]{3,}\b'` over the four entries -> a: S937 S935 S932 S777 S919 S921 S807 S750; b: S938; c: S908 S757(coupling, header :7); d: S916 S719 S718 (coupling). `grep -rnoE '\b(<21 slice ids>)\b'` over merge/kotodama/{knowledge,amendments,SOURCES.append.md,MERGE-REPORT.md}: slice ids found only in entry (a) (S807 x2), `verification/citation-format-and-source-registry.amend-2026-10-24-r11.md` (S791 S792 S795 S796 S824 S825, not a candidate) and `SOURCES.append.md:104` (S791 S795 S796, not a candidate). Candidates b, c, d: 0 slice ids. Planned campaign ids S908 S916 S932 S935 S937 S938 S919 S921: none is in the slice; `git show 98c486b:corpus/SOURCES.md` has no row for any of them (and none for S777).

## 4. Table
| slice row | in candidate set? | verdict carried from round 75 (round-71 standing) | action round 76 |
|---|---|---|---|
| S776 | no | PRESENT | carry; none |
| S778 | no | PRESENT | carry; none |
| S779 | no | REFUSED | carry; none |
| S786 | no | REFUSED | carry; none |
| S787 | no (document = lane S893, round 75) | REFUSED | carry; none |
| S791 | no (slice id appears in non-candidate r11 entry/SOURCES.append) | UNVERIFIABLE | carry; none |
| S792 | no (non-candidate r11 entry only) | REFUSED | carry; none |
| S795 | no | PRESENT | carry; none |
| S796 | no | PRESENT | carry; none |
| S804 | no | PRESENT | carry; none |
| S814 | no | REFUSED | carry; none |
| S816 | no | REFUSED | carry; none |
| S817 | no | REFUSED | carry; none |
| S820 | no | PRESENT | carry; none |
| S823 | no | PRESENT | carry; none |
| S824 | no | PRESENT | carry; none |
| S825 | no | PRESENT | carry; none |
| S827 | no | PRESENT | carry; none |
| S807 | id textually YES in entry (a) :65,:90 (wrong-document namespace collision; not a citation of the slice row's document) | UNVERIFIABLE | verdict unchanged; entry (a) must be re-pointed by document before admission |
| S812 | no | UNVERIFIABLE | carry; none |
| S835 | no | UNVERIFIABLE | carry; none |

Planned rows S908 S916 S932 S935 S937 S938 S919 S921: all outside the slice (not in slice id list; grep above). None cites a slice row by document.

## 5. Hand-checks this round
None required: no slice row's document is cited by any of the four candidates. No fetch performed, no source opened, no install made. Round-75 lesson `## Quarantine` can restate the table by carry-over; it should record that the S807/S750/S777 text collisions are by id only.
Scratch: none created. Unrun: no live re-fetch of any slice row (deliberately).
