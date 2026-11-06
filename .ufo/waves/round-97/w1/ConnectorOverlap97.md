# ConnectorOverlap97 — Report (round 97 w1)

Seat: sibling/adjacent-owner overlap scan for the verbal-duelling and ritual-insult surface
(claim C). Read-only outside my stage. Detail: stage/ConnectorOverlap97/overlap.md.

## Result
- 21 sibling lanes (`ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md | wc -l` → 21, rc 0); all 21 PROVINCE.md read; none unreadable.
- Word-boundaried ten-term pass (flyting, insult, duel, contest, satire, invective, boast, taunt, rap battle, debate) over all sibling PROVINCE.md and SKILL.md: 0 files (`grep -riocE … | grep -v ':0$' | wc -l` → 0, rc 0). Substring pass hits only the fleet word "contested" (game-dev-2d:10, game-dev-3d:36/78, kagi:64, kaidoku:187, kake:45, kotoba:17, kotodama:25, mori:66, souji:189, tsukuroi:570) — arbitration vocabulary, not the surface.
- No sibling claims the surface. lore owns canon (PROVINCE.md:3,9), chousa owns research method (:3-8) — both are boundaries to respect, not overlaps. All other 17 siblings: no overlap. Contested scope: 0 items; nothing routed to the L1.
- In-lane (corpus/knowledge): 0 topic-line/heading owners of the six frozen phrases (grep `(?i)^(?:- topic:|#{1,6} ).*(verbal duel|ritual insult|flyting|song duel|boast formula|audience adjudication)` → No matches found, rc 0); mention-only files: 2 (`grep -rilE 'verbal duel|…' corpus/knowledge | wc -l` → 2, rc 0: orality-formulaic-language.md:112, trickster.md:25,:62 — matches claims.json before-state; arabia-pre-islamic.md:69-73 carries Fakhr/Hijāʾ table cells consistent with the claims.json :71 pointer). The new entry path does not exist yet (glob → Path not found). The frozen zero-owner premise holds by content sweep, the round-96 mistake class fixed by leg C8.
- Eight in-lane neighbours bounded in one sentence each in overlap.md §4 (orality, politeness-taboo, binding-speech, trickster, oath-formulae, greeting-formulae, secret-ludic, games-play-sport-contests as nearest neighbour).
- Risk carried in overlap.md §7: any later heading/topic edit in another knowledge file that takes a frozen phrase flips C8 to FAIL; re-run the two sweeps before scoring seats run.

## Tooling installed
None.

## Files written
- stage/ConnectorOverlap97/overlap.md
- .ufo/waves/round-97/w1/ConnectorOverlap97.md (this file)
- stage/ConnectorOverlap97/DONE (last)
