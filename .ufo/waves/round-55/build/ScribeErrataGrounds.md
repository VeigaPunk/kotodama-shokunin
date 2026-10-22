# ScribeErrataGrounds — the 17 round-54 Gate rows whose Grounds stop mid-clause

- seat: `KotodamaR55.ScribeErrataGrounds` (scribe, axis calibration)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- file of record: `corpus/lessons/round-54.md` (200 lines, sha256 `5b685de288da64a1e451fcb71b88a881eabcc7ba9465f36d55d25f6925620928`)
- assignment: routed defect 1 in `corpus/lessons/round-54-verifier-spotcheck.md` section 5

## Result

All 17 named rows exist (`S241`, `S242`, `S244`, `S248`, `S250`, `S251`, `S253`, `S255`, `S259`, `S263`, `S264`, `S265`, `S275`, `S276`, `S277`, `S278`, `S279`) and all 17 are recoverable. For every row the text after `Grounds: ` is a character-exact prefix of the `teaches:` line of the block that supplied the row, cut at 220 characters of the seat's line as written, with double-quote marks and asterisk emphasis removed, and a full stop appended. Re-running that rule reproduces all 17 grounds byte for byte (17 of 17), so the uncut `teaches:` line is the full grounds text. No row lacks a carrying report.

The cut lands mid-phrase in every case, so each line reads as a sentence that stops: `S241` ends `the masked ancestor is silent and a.`, `S275` ends `the marada heads were not wearable .` (with a stray space before the stop, because the 220th character is a space). The restored tails run from 4 characters (`S242`, `faces valued as material.`) to 389 (`S263`, seven further clauses).

No file in the lane was modified by this seat. The errata lines are the deliverable; the L1 splices them into `corpus/lessons/round-54.md`.

## Method and evidence

- `grep -nE '[a-z,;] ?\. Seat:' corpus/lessons/round-54.md` returns 17 lines: 25, 26, 28, 32, 34, 35, 37, 39, 43, 47, 48, 49, 59, 60, 61, 62, 63. Same ids as the closure lesson's list; the file holds 46 Gate rows in all, with `## Gate` at line 19.
- The row's `Seat:` cell names the report. For each row I took the block in that report whose `url:` line equals the row's URL (17 of 17 matched) and read its `teaches:` line. Every truncated grounds is a prefix of that line, with the quote and emphasis marks removed.
- `S251` (Rubin Museum cham) names `Seat: ScoutNuo`, and the cham block is in `ScoutNuo.md` block `NEW-ScoutNuo-5` at line 104; `ScoutCham.md` exists but supplies no Gate row. The cell is correct, though the seat name is misleading for a cham row.
- `S241` and `S242` are blocks `NEW-ScoutRomanImagines-1` and `-4`; the remaining provenance is in the table below.
- No network, no git, no jj, no installs; the lesson and nine seat reports were read in the working tree. Nothing outside this report was written.

Reconstruction rule, in full, as run:

```python
g = line.split('Grounds: ',1)[1].split(' Seat: ',1)[0]
teach = block_teaches_text
house = teach.replace('"','').replace('*','')
assert g == house[:220] + '.'
```

## The 17 errata lines

- S241 (round-54.md:25): Grounds, in full: the mask is a household portrait kept in a shrine and brought out on a calendar (sacrifices, funerals); the wearer is cast for bodily resemblance and dressed for the dead man's office; the masked ancestor is silent and a living orator speaks for him. (source: .ufo/waves/round-54/build-a2/ScoutRomanImagines.md:66).
- S242 (round-54.md:26): Grounds, in full: the mask set is stored procession equipment and a drawn pedigree at once; admission is a family decision that can be refused, and a claim that can be forged; the wax mask was later replaced by metal faces valued as material. (source: .ufo/waves/round-54/build-a2/ScoutRomanImagines.md:123).
- S244 (round-54.md:28): Grounds, in full: a commedia Mask is a place-plus-class-plus-speech package whose dialect is a deliberately comic stage version of the regional one; the accent is the type's fixed part, while whether the type is honoured or ridiculed depends on the town, the audience and the plot, and the troupe buys protection for that licensed mockery from secular patrons (source: .ufo/waves/round-54/build-a2/ScoutCommedia.md:42).
- S248 (round-54.md:32): Grounds, in full: the mask set is property that travels between institutions, handling belongs to one designated office, reception is a material obligation, inventory is part of the rite, and at the mid-month festival the clan carries the set to a temple. (source: .ufo/waves/round-54/build-a2/ScoutNuo.md:138).
- S250 (round-54.md:34): Grounds, in full: mask removal is a rare, scripted revelation rather than stage business; the masked figure is treated as a presence with effects on the room; no mask design is uniform across regions; and masks have a documented second life as commodities. (source: .ufo/waves/round-54/build-a2/ScoutSriLankaKolam.md:69).
- S251 (round-54.md:35): Grounds, in full: cham is performed by monastics in a monastery courtyard for protection of the community, explicitly not as entertainment, by trained bodies under heavy masks, as a procession of doctrinal roles; the costume is an ensemble of named materials. (source: .ufo/waves/round-54/build-a2/ScoutNuo.md:117).
- S253 (round-54.md:37): Grounds, in full: the surviving commedia mask is a reproducible type-face, cast from a shared wooden form rather than carved as a portrait, worn as a half-mask that leaves the mouth free; its character could change trade while the mask stayed, and the type outlived both its stage role and its genre (source: .ufo/waves/round-54/build-a2/ScoutCommedia.md:62).
- S255 (round-54.md:39): Grounds, in full: office, not wealth or blood alone, earns a mask; the right can be cancelled after death; the masks stood in labelled shrine-recesses off the atrium and were opened and crowned on festal days; the material was wax and the manufacture is a scholarly reconstruction. (source: .ufo/waves/round-54/build-a2/ScoutRomanImagines.md:143).
- S259 (round-54.md:43): Grounds, in full: the mask is a spirit men know they make; sight is a purchased grade; the society is near-universal for men and closed to women; each figure is destroyed after its appearance while its authority continues in a planted bush; masks are clan property that may not be alienated, but masks bought from Tolai or Duke of York owners are personal property that can be sold; producing a clan figure at a mortuary feast is an overt claim of leadership, and unauthorized disclosure (kilung) is fined in pigs. (source: .ufo/waves/round-54/build-a2/ScoutMalagan.md:22).
- S263 (round-54.md:47): Grounds, in full: Gelede as a stage play compared by its author to the Roman theatre and to Noh; the honoured mothers (iya wa, aje) distinguished from the orisa as living persons; the great mask that opens the evening dance as a personification of creative nature; the mothers' reported power to prevent a mask from being removed after the festival and to stop a singer mid-song; viewing of a mask as something granted for a purpose; dancers who perform without knowing the deeper meaning; and, quoting Cambell Flavier, Èfè as the anonymous figure who mocks wrongdoing and praises the deserving without being stung in return. (source: .ufo/waves/round-54/build-a2/ScoutGelede.md:67).
- S264 (round-54.md:48): Grounds, in full: UNESCO's record of the inscribed element — Yoruba-Nago communities across Benin, Nigeria and Togo, celebrated annually after the harvests and at important events and during drought or epidemics; night staging on a public square after preparation in a nearby house, with singers and drummers first; mask carving and costume making as preparatory craft; satire carried by the masks; animal motifs read as power (serpent) and as the mothers' messenger (bird); and UNESCO's assertion that this is the only known masked society also governed by women. (source: .ufo/waves/round-54/build-a2/ScoutGelede.md:35).
- S265 (round-54.md:49): Grounds, in full: a mask policy written by the mask-owning authority itself — sacred from the moment of making, made only for use inside a medicine society, forbidden to exhibit or reproduce, interpreted by nobody outside the societies, and with the veto placed in the using society and the Grand Council rather than in any individual or museum. (source: .ufo/waves/round-54/build-a2/ScoutHaudenosauneeStatement.md:34).
- S275 (round-54.md:59): Grounds, in full: malagan is a family of ritual objects across New Ireland and the Tabar Islands; most were spent in one ceremony and then destroyed, abandoned or sold, a few excepted as kept heirlooms; the marada heads were not wearable and topped plant-fibre figures; rain-making was an inherited office passed from father to son; rights over designs and production sat with clans and clan leaders, and sculptors worked to detailed instructions with offerings at each stage. (source: .ufo/waves/round-54/build-a2/ScoutMalagan.md:42).
- S276 (round-54.md:60): Grounds, in full: the effigy is animated during production, installed, treated as alive, then ritually killed; months of preparation end in an hour; the remains go to the forest to rot or to a mission to be sold; what survives is a named image, and personal names are names of malanggan images passed down as a finite set. (source: .ufo/waves/round-54/build-a2/ScoutMalagan.md:61).
- S277 (round-54.md:61): Grounds, in full: masks are men's business by a myth of stolen technique; the art passes from father to son among the initiated; spirits appear in dreams and commission their own masks; masks are destroyed in the fire after use, so collected examples are rarities; the day dance is for the dead and fertility and is danced by women every two or three years, the night dance belongs to men and forest spirits; kavat chase and frighten the uninitiated and children, and sick children are pushed between a dancer's legs to be healed. (source: .ufo/waves/round-54/build-a2/ScoutMalagan.md:80).
- S278 (round-54.md:62): Grounds, in full: kavat are made for male night dances in which masked spirits come out of the bush and chase women and children; making happens in a sacred shelter; the eyes carry the power and the triangles beneath them are tears; the dancer's gender is marked by the shape of the barkcloth penis-sheath; and this label says the kavat is the mask that is not burned, which the Gandur essay contradicts. (source: .ufo/waves/round-54/build-a2/ScoutMalagan.md:99).
- S279 (round-54.md:63): Grounds, in full: Greek does not lexically separate the face, the mask worn over it, the ancestor image and the person; the mask sense is an ordinary listed meaning, and the same noun carries in person, in bodily presence and the idiom of receiving someone's face. (source: .ufo/waves/round-54/build-a2/ScoutPersonaProsopon.md:34).

### Splice notes

- The house shape of a complete round-54 Gate row ends the grounds with a period and then the line's own separator period, so the text before ` Seat:` reads `..` on all 29 complete rows (for example line 23 `…what the audience is owed.. Seat:`). A spliced row should therefore read `<full grounds>.. Seat: <Seat>.`; the truncated rows currently carry a single `.`.
- The full grounds text is copied from the seat's `teaches:` line with double-quote and asterisk marks removed, the style of every ground on the file (0 of 46 grounds carry a double quote or asterisk). Three source lines lose marks: `ScoutGelede.md:67` and `ScoutPersonaProsopon.md:34` lose 2 double-quote marks each, `ScoutMalagan.md:99` loses 2 asterisks around `not`. If the lesson prefers the marks back, the raw lines are at the cited locators; `S263` and `S279` would then no longer match the file's no-quote ground style.
- `ScoutCommedia.md:42` and `:62` end without a full stop. Their erratum texts stop at `secular patrons` and `its genre`; add the period when splicing.

## Audit table

Cut column: characters of the seat's raw `teaches:` line consumed, before mark removal. Dropped: characters of the full text not present in the row.

| row | round-54.md | visible grounds ends | cut at char | dropped | source |
|---|---|---|---|---|---|
| S241 | 25 | `e masked ancestor is silent and a.` | 220 | 30 | `.ufo/waves/round-54/build-a2/ScoutRomanImagines.md:66` |
| S242 | 26 | `ed by metal faces valued as mater.` | 220 | 4 | `.ufo/waves/round-54/build-a2/ScoutRomanImagines.md:123` |
| S244 | 28 | `ype is honoured or ridiculed depe.` | 220 | 121 | `.ufo/waves/round-54/build-a2/ScoutCommedia.md:42` |
| S248 | 32 | `nth festival the clan carries the.` | 220 | 17 | `.ufo/waves/round-54/build-a2/ScoutNuo.md:138` |
| S250 | 34 | `masks have a documented second li.` | 220 | 18 | `.ufo/waves/round-54/build-a2/ScoutSriLankaKolam.md:69` |
| S251 | 35 | ` roles; the costume is an ensembl.` | 220 | 21 | `.ufo/waves/round-54/build-a2/ScoutNuo.md:117` |
| S253 | 37 | `ld change trade while the mask st.` | 220 | 61 | `.ufo/waves/round-54/build-a2/ScoutCommedia.md:62` |
| S255 | 39 | `ays; the material was wax and the.` | 220 | 43 | `.ufo/waves/round-54/build-a2/ScoutRomanImagines.md:143` |
| S259 | 43 | `hority continues in a planted bus.` | 220 | 276 | `.ufo/waves/round-54/build-a2/ScoutMalagan.md:22` |
| S263 | 47 | `ns the evening dance as a personi.` | 220 | 389 | `.ufo/waves/round-54/build-a2/ScoutGelede.md:67` |
| S264 | 48 | `demics; night staging on a public.` | 220 | 326 | `.ufo/waves/round-54/build-a2/ScoutGelede.md:35` |
| S265 | 49 | `y nobody outside the societies, a.` | 220 | 107 | `.ufo/waves/round-54/build-a2/ScoutHaudenosauneeStatement.md:34` |
| S275 | 59 | `e marada heads were not wearable .` | 220 | 238 | `.ufo/waves/round-54/build-a2/ScoutMalagan.md:42` |
| S276 | 60 | `e sold; what survives is a named .` | 220 | 84 | `.ufo/waves/round-54/build-a2/ScoutMalagan.md:61` |
| S277 | 61 | ` in the fire after use, so collec.` | 220 | 292 | `.ufo/waves/round-54/build-a2/ScoutMalagan.md:80` |
| S278 | 62 | `les beneath them are tears; the d.` | 220 | 166 | `.ufo/waves/round-54/build-a2/ScoutMalagan.md:99` |
| S279 | 63 | `in bodily presence and the idiom .` | 220 | 28 | `.ufo/waves/round-54/build-a2/ScoutPersonaProsopon.md:34` |

`S263` and `S279` lose 2 marks inside the cut, so their visible grounds is 218 characters; the cut is still at 220 of the source line.

## Cross-checks

1. **The cap is exactly 220 characters of the source line, not 220 of the grounds.** That explains the two 218-character rows: `ScoutGelede.md:67` and `ScoutPersonaProsopon.md:34` each have two double-quote marks inside the first 220 characters, which the ground style strips after the cut. No cap constant appears in any committed tool (`grep -rn 220 tools/*.py reports/round-54/*.py scripts/*.sh` returns nothing), so the cut is an authoring step, not a script.
2. **The other 29 Gate rows are complete.** Each equals its seat's whole `teaches:` text (0 characters dropped), so the cap hit only those source lines that ran long. The lesson's measure `[a-z,;] ?\. Seat:` fires on exactly the 17 truncated rows here and on 0 of the 29 complete rows, because a complete row ends `.. Seat:` (double stop) while a cut row ends `. Seat:`.
3. **That shape is round-54's, not a general truncation test.** `corpus/lessons/round-53.md` uses a single stop before ` Seat:` on all its 142 grounds, so the same expression fires on 104 of its 147 Gate rows (counts by round: round-53 104 of 147, round-52 54 of 82, round-51 7 of 61, round-50 0 of 23). Sampled round-53 hits read complete, for example `round-53.md:40` `…so an absolute frame decides where the hands go. Seat: ScribeSec05SpaceTime.` and `:43` `…the survey's own words. Seat: ScribeHeadScope.`. Claim O's `truncated-grounds` class therefore cannot be the lowercase-before-period shape alone; the sound test is "the grounds is a strict prefix of the supplying seat's `teaches:` text" (or the double-stop house shape on this one file), and round-53's seat reports carry no `teaches:` line to cross-reference (`.ufo/waves/round-53/build/ScribeSec05SpaceTime.md`, `ScribeHeadScope.md`: no `teaches:` line).
4. **Overlap with the sibling defect.** `S259`, `S265`, `S275` and `S277` are also on the doubled-locator list (routed defect 2, `.ufo/waves/round-55/build/ScribeErrataDoubled.md`). The two repairs do not collide: that seat replaces only the span between `accessed 2026-10-22 — ` and `. Grounds:`, and none of the 17 restored grounds texts contains a double quote, so splicing cannot create a second quoted span.
5. **Precedent for the file shape.** `corpus/lessons/round-54.md:161` already carries `## Errata to the round-53 lesson's Gate (filed bytes not rewritten)`, which groups rows by id and line and points at a seat report. The 17 lines above fit that section's style; they need a matching heading for round 54 only if the L1 wants the rounds separated.

## Not run, not done

- Did not edit `corpus/lessons/round-54.md` or any other lane file; nothing was spliced, only drafted. No git or jj command ran.
- Did not re-open any quoted URL and did not verify any quote against its source: this seat repairs the grounds text against the seat reports, not against the web. No source rows are claimed here.
- Did not run `reports/round-55/accept-c.py`, `accept-o.py`, `tools/check-gate-quotes.py` or any gate, and did not test the checker against these 17 rows; the shape counts above are my own measurement, not the tool's.
- Did not search other rounds for the same 220-character cut beyond the shape counts in item 3, and could not cross-reference those counts to report text for lack of `teaches:` lines in round-53's reports.
- No tool was installed or upgraded.
