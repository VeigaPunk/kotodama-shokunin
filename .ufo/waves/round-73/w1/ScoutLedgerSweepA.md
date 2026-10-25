# ScoutLedgerSweepA — calibration ledger sweep, part A (round 73, hyaku run 7)

Seat: `ScoutLedgerSweepA` (leaf). Scope: statements asserting counts, paths, line
numbers, commit hashes, row totals, or pass/fail results in `SHONEN.md`,
`corpus/README.md`, `README.md` (lane root). Roll: read-only + git read-only.
All observations run against the committed tree at HEAD `8841ad3b896a0227674fa0725b818c999118046f`
(= claims.json base). No tools installed (no install needed); no repo bytes mutated.

## Verdict summary

- **7 mismatch rows, mismatches first**, then 15 verified (no-mismatch) rows — 22 total.
- Live/repairable mismatches: README totals line + counts footer + `culture-material/`
  header (all one family, count 243 vs 245; cause: round-72 C landing added two
  tracked-but-unindexed entries without reconciling the corpus index), and two stale
  SKILL.md line citations in SHONEN.md.
- Historical-as-filed (annotate only): SOURCES row-attribution at `2b956d7`,
  "build wave admitted 54", and the rev 2.18 vs rev 2.19 `753` vs `752` registry-number
  contradiction.
- Confirmed matches: claims.json base == HEAD; `*conlang-scholarship*` file count = 0
  (C before-state holds); SOURCES registry = 799 rows ending S875; round-56
  367/35/10 split and round-54 prerequisite 194/34/10 split re-derive exactly.

## Mismatches (first)

| # | stated_at (path:line) | stated text (verbatim, trimmed) | observe command | observed value now | mismatch | disposition |
|---|---|---|---|---|---|---|
| M1 | `corpus/README.md:732` | `Total knowledge entries: 243.` | `find corpus/knowledge -type f -name '*.md' \| wc -l` | 245 | Y | **repairable** (live; = claims Ca R3 candidate) |
| M2 | `corpus/README.md:736` | `(total 243 files; directory totals 30/29/36/29/24/95).` | `find corpus/knowledge/<p> -maxdepth 1 -type f -name '*.md' \| wc -l` per partition | 245 files total; dir totals 30/29/**38**/29/24/95 (culture-material 38 vs 36) | Y | **repairable** (live) |
| M3 | `corpus/README.md:407` | `## culture-material/ (36)` | `find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*.md' \| wc -l` | 38 (dir has `heritage-taxonomy-models.md` + `heritage-taxonomy-models.amend-2026-10-24-r13.md`, neither indexed) | Y | **repairable** (live) |
| M4 | `SHONEN.md:6` | "SKILL.md … `:468` (Error patterns)" | `sed -n '468p' SKILL.md` | `### Registry correction chains`; actual `## Error patterns` is at SKILL.md:505 | Y | **repairable** (live, stale line number) |
| M5 | `SHONEN.md:6` | "SKILL.md … `:522` (Checklist)" | `sed -n '522p' SKILL.md` | a decision-table row, not a checklist; actual `## Checklist (executable where a tool exists)` is at SKILL.md:564 | Y | **repairable** (live, stale line number) |
| M6 | `SHONEN.md:8` | "61 new SOURCES rows (52 mined, 9 queued at `2b956d7`: S081, S123–S125 and S127–S131 queued; … the build wave admitted 54, the falsify wave added S125–S131)" | `git -C <repo> diff 2b956d7^ 2b956d7 -- corpus/SOURCES.md`; `git show 2b956d7:corpus/SOURCES.md`; `find .ufo/waves/round-51/build -maxdepth 1 -type f` | diff adds **0** SOURCES rows at 2b956d7 (nine named ids are present there, all status `queued`); `build/` has 37 files = 36 seat reports + `swarm-registry.json` (54 not re-derivable); `falsify/` has 42 = 41 seats + registry | Y (partial) | **historical-as-filed** (annotate only; round-51 closure record) |
| M7 | `corpus/README.md:36` (rev 2.18) vs `corpus/README.md:28` (rev 2.19) | rev 2.18: "registry moved **753** → 776 rows"; rev 2.19: "registry moved **752** → 776 rows" | `git show <r66 landing 65fe857>:corpus/SOURCES.md`; `git show <r67 landing c58eb84>:corpus/SOURCES.md`; `git show <r68 landing 44c9cc2>:corpus/SOURCES.md` | observed rows: 724 (post-r66), 752 (post-r67), 780 (post-r68) — the two revision blocks contradict each other (753 vs 752) and neither 753 nor 776 matches any sampled committed state; 752 matches only the post-r67 total | Y | **historical-as-filed** (annotate only; internal contradiction) |

## Verified statements (no mismatch)

| # | stated_at | stated text (verbatim, trimmed) | observe command | observed value now | mismatch |
|---|---|---|---|---|
| V1 | `SHONEN.md:6` | "SOURCES.md (412 rows after round 56 — 367 mined, 35 queued, 10 rejected …)" | `git show c8af23f3d0282cd1f6945b9bf54670a8478447a1:corpus/SOURCES.md` → rows + status column | 412 rows; mined 367 / queued 35 / rejected 10 (exact) | N |
| V2 | `SHONEN.md:6` | "census exit 0 in `reports/round-56/telemetry/final-measures.txt`" | `test -f` + content | file exists; census leg prints "exit 0" | N |
| V3 | `SHONEN.md:6` | "the round-53 figure 194/35/9 became 194/34/10 in the round-54 prerequisite `d761ee8`" | `git show d761ee8:corpus/SOURCES.md` → rows + status column | 238 rows; mined 194 / queued 34 / rejected 10 (exact) | N |
| V4 | `SHONEN.md:8` | "repairs at `364eeff` → final receipt `reports/round-51/telemetry/final-measures.txt`" | `git cat-file -e 364eeff^{commit}`; `head` receipt | commit exists; receipt exists; header reads `worktree=364eeff0e42c1ed1ca0180f7c9a76121557568c4` | N |
| V5 | `SHONEN.md:8` | "41-seat falsify wave" | `find .ufo/waves/round-51/falsify -maxdepth 1 -type f \| wc -l` | 42 files = 41 seat reports + `swarm-registry.json` | N |
| V6 | `SHONEN.md:8,10` | commits `2b956d7`, `364eeff`, `d761ee8`, `1923bfe`, `4ad2683` | `git cat-file -e <c>^{commit}` | all five exist | N |
| V7 | `SHONEN.md:12` | "round-51 connector sweep (`.ufo/waves/round-51/build/ConnectSiblingSign.md`) found 0 sibling owners and names one unowned fleet surface (signed web accessibility)" | `git ls-files`; `grep -nE '0 sibling\|zero sibling\|sibling owner\|unowned'` | file tracked; line 27/70/97: zero sibling overlap, unowned AAA 1.2.6 signed-web-accessibility surface named | N |
| V8 | `corpus/README.md:344` | `## linguistics/ (30)` | `find corpus/knowledge/linguistics -maxdepth 1 -type f -name '*.md' \| wc -l` | 30 | N |
| V9 | `corpus/README.md:376` | `## myth-symbol/ (29)` | same pattern | 29 | N |
| V10 | `corpus/README.md:445` | `## synthesis/ (29)` | same pattern | 29 | N |
| V11 | `corpus/README.md:477` | `## verification/ (24)` | same pattern | 24 | N |
| V12 | `corpus/README.md:503` | `## civilizations/ (95)` | same pattern | 95 | N |
| V13 | `corpus/README.md:10-11` | rev 2.21 "registry moved 797 rows (784 base + 13 mined S861–S873)" | `git show 498db73:corpus/SOURCES.md` | 797 rows; last id S873 (accurate snapshot at its landing; current 799 = +S874/S875 from round-72 commit 770100f) | N (historical) |
| V14 | `corpus/README.md:3-9` | rev 2.21 "culture-material/ moved 34 → **36** (the header was stale at 34 against 35 files; the landing fixes it)" | `git show 44c9cc2:corpus/README.md` / `git show 498db73:corpus/README.md` headers | r68 header (35); r71 header (36) — consistent at landing | N (historical) |
| V15 | `corpus/SOURCES.md` tail (context) | registry "currently ends at S875 (799 rows)" | `grep -E '^\| S[0-9]+ \|' corpus/SOURCES.md` | 799 rows; last row S875; HEAD statuses mined 704 / queued 58 / rejected 37 | N |

## Notes for the freeze/ledger

- **M1–M3 cause (one family):** the round-72 C landing (commit `770100f`
  "heritage-taxonomy assimilation — two entries admitted, registry S874/S875 appended
  (797->799)") added `corpus/knowledge/culture-material/heritage-taxonomy-models.md`
  and `heritage-taxonomy-models.amend-2026-10-24-r13.md` (both tracked) **without**
  adding a corpus index row, a revision block, or bumping the totals line / counts
  footer. Hence live tree = 245 `.md` files vs README 243; only `culture-material/`
  header/count is affected. Repair is append-only per the corpus convention (new
  revision block, header 36→38, totals 243→245, footer vector 30/29/38/29/24/95).
- **R3 candidate confirmed:** claims.json Ca before-state ("README 'Total knowledge
  entries: 243' vs find = 245") reproduces exactly at HEAD; it is a live, repairable
  mismatch.
- **C before-state spot-verified:** `find corpus/knowledge -iname '*conlang-scholarship*'`
  → 0 files; 799-row registry → 0 rows naming the five cited source hosts (consistent
  with claim C's before legs).
- **Historical receipt quality:** round-51 and round-56 `final-measures.txt` both exist,
  carry the asserted worktree/stamp revisions, and the census legs exit 0.
- `a1a359d55…` (corpus/README.md rev 1.6) is an intentionally abbreviated digest, not
  a checkable full hash; treated as unverifiable-by-short-hash, not a defect.
- No tools were installed (nothing required; `pacman` untouched). Fetch hygiene: no web
  fetches performed this seat.
