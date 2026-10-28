# ScoutPathsSearch — round 77, wave 1 (recon: SOURCES.md Paths + Search-log edits for claim C)

Verdict: emitted both required_sections[] items to
`.ufo/waves/round-77/w1/stage/ScoutPathsSearch/sections.md` —
(a) one Search-log note covering the naming-systems assimilation sweep (bound = the 11 staged
naming-theme files; identified 11 / screened 11 / included 1 / excluded 10, per-file reasons,
stop rationale), and (b) a fitting Paths bullet `S897 → S898` (structure before inventory),
matching the round-76 precedent where the claim added its own bullet.

## Base evidence

- Section positions at base: `## Paths` line 853, `## Search log` line 890, `## Leads
  (unopened)` line 904 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show
  211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md | grep -n '^## \|^# '` →
  `26:## Registry / 853:## Paths / 890:## Search log / 904:## Leads (unopened)`.
- Base registry size: 820 `| S` rows — `git … show 211f952…:corpus/SOURCES.md | grep -c '^| S'`
  → `820`; last ids `… S894, S895, S896` (`grep -o '^| S[0-9]*' | tail -5`). Next lane ids
  S897/S898 matches the CLAIMS-DRAFT's "registry 820 → 822".
- Paths precedent: first `## Paths` bullet at base is `- calendar-standard design — S896 →
  S895 → S894: …` — a single line naming the round-76 claim's own new rows; `## Search log`'s
  last note is `**State-standard calendar compilation (round 76).**` with counts
  "Identified 4 theme candidates, screened 4, included 1, excluded 3" and its out-of-bound
  line ("The other 36 staged package files were outside this bound"). The emitted text copies
  both formats.
- Rule text: `/home/vgpnk/Projects/shokunin/CORPUS.md` lines 126–128 — `5. **Search log.**
  PRISMA-inspired, not PRISMA-compliant: question/query, where searched, date, identified /
  screened / included / excluded counts, exclusion reasons, stop rationale. A negative claim
  carries its sweep.` (read via `grep -n -A12 'Search log' /home/vgpnk/Projects/shokunin/CORPUS.md`).

## Counts (all re-run this round)

- `grep -c '^|' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` → `134`
  (header + separator + 132 data rows; MERGE-REPORT.md header states "proposed rows accepted:
  132", ids S859–S990, lane registry stated as 782 pre-merge → 820 at base, consistent).
- Naming-theme file list: `ls
  /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/ |
  grep -c '^naming-systems'` → `11`: amend-2026-10-23{,b,c}.md and amend-2026-10-24{,-r10,
  -r11,-r12,-r13,-r14,-r15,-r16}.md. (No `naming-systems.md` in `knowledge/`; that file exists
  only under `amendments/corpus/knowledge/linguistics/` as the round1+round2 anchor target.)
- Total staged knowledge .md files: `find …/merge/kotodama -name '*.md' -type f | wc -l` →
  `46` = 40 under `knowledge/` + 4 anchor targets under `amendments/` + MERGE-REPORT.md +
  SOURCES.append.md. Bound arithmetic: 40 staged knowledge files − 11 naming-theme = 29
  outside bound (conlang-scholarship ×6, conlang-methodology.amend, calendar/era/heritage/
  worldbuilding ×9, narrative-structure ×5, verification ×9 — per `find` listing).
- Per-file S-id citations: `for f in naming-systems*.md; do grep -o 'S[0-9][0-9][0-9]' "$f" |
  sort -u; done` — adopted entry `amend-2026-10-23.md` cites S886,S888,S889,S890,S891,S896,
  **S897**,S896-region and **S903** (the claim's D1/D2 documents); excluded files cite
  {S906,S907,S911}, {S912,S913,S914,S918}, {S924–S936-family}, {S939–S944}, {S947–S954},
  {S957–S960}, {S963–S966}, {S969,S972–S974}, {S978}, {S988}.
- Staged D1/D2 rows verified against claim: `grep -n '^| S897 \|^| S903 ' SOURCES.append.md` →
  line 45 `| S897 | 魏斌〈單名與雙名：漢晉南方人名的變遷及其意義〉…lishisuo.cssn.cn…t20210316_5318560.shtml`
  and line 51 `| S903 | Kałużyńska, Irena (2025), "Flowers, Plants, and Trees in Female
  Naming in China", *Onomastica* LXIX …onomastica.ijppan.pl/…/574/763/` — both documents match
  the DRAFT's D1/D2.

## Decisions and their basis

- (a) Bound choice: all 11 naming-theme files were screened (headers `ground:`/`topic:`/`source:`
  blocks read verbatim). Identified/screened = 11; included = 1 (only amend-2026-10-23 carries
  both the 姓/名-structure ground and the finite-inventory ground the claim names); excluded =
  10 with per-file reasons taken from each file's own `ground:`/`topic:` text and the DRAFT's
  reject notes (23b held — different ground; 23c field-literature sweep; 24 stale S933 + S934
  doc-duplicate of D2 + S936 bridge; r10 C-tier + unresolved S899/S900 family; r11–r16 the
  《姓名论》 monograph-chase chain — venue, editions, pagination, citation anchors — not this
  ground). This is more defensible than the DRAFT's narrower named-candidate set (4 files):
  the remaining 7 naming files exist in the staged set, so "identified 4" would falsify the
  sweep; "identified 11" is true of the staged directory listing.
- (b) 'none' rejected: r76's `calendar-standard design` bullet is the in-file precedent for a
  claim adding its own Paths bullet; S897 (structure/history) → S898 (classification/inventory)
  is a genuine read order, so a new bullet is emitted instead.

## Unrun / out of scope

- Live re-opens of D1/D2 (403 probe, Wayback captures) — other seats own those legs; not run here.
- The staged S897 row's own `source:` line in the entry file says "fetched 2026-10-23" — the
  search note records re-grounding as the lane's job at admission time, not a wave-1 count.
- No fixture repos created; no scratch dir needed (`mktemp` unused); nothing installed.
- No edits to CLAIMS-DRAFT.md, corpus/, or any lane-tracked file — writes confined to
  `.ufo/waves/round-77/w1/` per seat spec.
