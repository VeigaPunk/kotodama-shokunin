# ConnectorOverlap100 — round 100, adjacency scan of the work-song surface

Seat: ConnectorOverlap100 (connector, axis `adjacency`, milestone r100-v1). Read-only over the lane and
the fleet; wrote only `stage/ConnectorOverlap100/overlap.md` and this report. Base
`60010a55fb5f04ee728070c463b1a57ae1cc17fc`. Nothing committed.

## What was asked and what was done

Scan sibling and adjacent-owner overlap for claim C's surface (`linguistics/work-song-labour-chant.md`,
the six frozen phrases). Four passes: (1) every sibling `PROVINCE.md`/`SKILL.md`; (2) the lane's own
adjacent entries — the seven named linguistics files plus the culture-material files on music, seafaring,
craft, field, trade, textile, metal and dance; (3) an independent ownership sweep on the lane's own
definition; (4) the registry, for an existing work-song source row.

## Result

**No sibling lane claims the work-song surface.** The only adjacent sibling owner is **audio-shokunin**,
and it owns sound *production* (`PROVINCE.md:3-5` "game audio production — SFX … and soundtrack …
verified by headless analysis"), not song as a cultural-linguistic system; it refuses perceptual claims
without a measurable proxy (`:13`). Everything else is either a disclaimer ("Nothing here is oral
knowledge", tabi/mado/tsukuroi/kumitate/game-dev-3d), gate prose ("behavioral", "performance"), or an
unrelated homonym ("temporal-sweep", "division of labour", llama.cpp audio modality, an HTML `audio`
element list). lore owns canon (`PROVINCE.md:3,9,28`), chousa research method (`:3-8`, no oral-history
claim), kotoba prompt/skill craft (`:69` records the split with kotodama).

**In-lane: 14 rows (15 files), all boundary-to-respect, none owning the surface.** The closest seam is
`culture-material/maritime-seafaring-lexicon.md:29`, whose working-register row already reads "commands,
the wage cycle, **the songs that pace shared labour**" with handoff column "**who times the work**" —
a table cell, so adjacency under `corpus/QUALITY.md:373` rule 39, but the one place the lane already
assigns labour-song timing to a non-song entry. Second closest: `material-culture-inference-method.md:15`
couples "work songs" to `orality-formulaic-language`, which carries no work-song phrase and no task-timing
item.

**Ownership sweep (independent, faithful to rule 39): owners = 0 over 271 knowledge files.** Prose
adjacency is 5 files: `civilizations/balts.md` (work song×1), `civilizations/maori.md` (call and
response×1), `culture-material/material-culture-inference-method.md` (work song×1),
`linguistics/funerary-lament-dirge-formulae.md` (work song×2, as a contrast class),
`linguistics/lullaby-child-song-formulae.md` (work song×3, the tune-sharing graph). This reproduces
claim C's frozen before-state (`C8 owners=0`) on the worktree.

**Registry: no existing work-song source.** 941 rows, highest `S1017`, and `grep -inE
'shanty|chantey|work song|worksong|song leader' corpus/SOURCES.md` returns nothing (rc=1). The four new
rows are genuinely new surface, not a re-label of an existing row.

## Contested scope (three, routed to the L1, not absorbed)

1. **C-1** — `material-culture-inference-method.md:15` assigns "work songs" to `orality-formulaic-language`
   in a coupling line, while orality owns only formula composition. Stale pointer vs subtype relation is
   undecided; the fix is a one-way pointer update **outside claim C's surface**, so it must not be edited
   this round.
2. **C-2** — `maritime-seafaring-lexicon.md:29` claims "the songs that pace shared labour" and "who times
   the work". Proposed split: seafaring owns the hull's register row, the new entry owns the song system,
   each citing the other one-way.
3. **C-3** — "work rhythm" invites an acoustic/perceptual claim that is audio-shokunin's by `:13`. The
   entry should design words, roles and timing only; no acoustic statement is needed for claim C.

## Numbers (command, rc)

- `ls -d *-shokunin/PROVINCE.md | wc -l` → 21, rc 0; `ls -d *-shokunin/SKILL.md | wc -l` → 19, rc 0.
- per-lane term sweep over PROVINCE+SKILL → rc 0 (values in `overlap.md` §1).
- python3 owner sweep (topic lines + all headings, normalized containment, six phrases, 271 files) →
  owners=0, rc 0.
- python3 prose sweep → 5 files, rc 0.
- `grep -cE '^\| S[0-9]+ ' corpus/SOURCES.md` → 941, rc 0; highest row `S1017`, rc 0.
- `grep -inE 'shanty|chantey|work song|worksong|song leader' corpus/SOURCES.md` → no output, rc 1.
- `sha256sum audio-shokunin/PROVINCE.md /home/vgpnk/Projects/audio-shokunin-publish/PROVINCE.md` →
  `20d881a6…`, `99ba0e93…`, rc 0 (separate repo, same Owns text).
- `grep -rliE 'work song|shanty|labour chant' shokuknow/{lanes,doctrine}` → no output, rc 1.
- `grep -inE 'song|music|chant|oral'` over lore / kotoba / kotodama PROVINCE.md → no output, rc 1 each.
- `grep -inE 'oral|interview|fieldwork|song|music'` chousa PROVINCE+SKILL → 1 hit `SKILL.md:550`
  "behavioral", rc 0.

## Files not read / absent

`kimi-shokunin/PROVINCE.md` and `SKILL.md` absent (rc=2); `/home/vgpnk/Projects/art-east-asian-design/`
absent (rc=2) though two provinces refuse into it; `shokunin/audio-shokunin-publish/PROVINCE.md` absent —
the publish copy is at `/home/vgpnk/Projects/audio-shokunin-publish/PROVINCE.md` and was read there. No
sibling province or skill file was unreadable for permission or format reasons.

## Tooling and scratch

No tool installed or upgraded (none needed). Scratch `/fast/scratch/hyaku/kotodama-r100/ConnectorOverlap100/`
was created and removed empty. Output: `stage/ConnectorOverlap100/overlap.md`
(sha256 `bf67567b276d12079012f4070a8e115440e353ff981215d0b99e210b5cb79bb5`, 143 lines), DONE last.
