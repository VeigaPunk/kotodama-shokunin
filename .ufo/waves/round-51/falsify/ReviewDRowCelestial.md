# ReviewDRowCelestial: attack on claim D, row 46 (celestial anchor)

- Seat: KotodamaR51a3.ReviewDRowCelestial (leaf reviewer; read-only on the lane; no delegation, no background jobs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. Claim D commit 35f0d49; claim base bff83ba; lane tip 9feb69e.
- Access date for every external source: 2026-10-22.
- Judged on: depth.

## Verdict: FAILS (row 46 as landed)

Claim D's stated falsifier is "a non-author review finding that a new row's anchored line does not support its ownership cell". This row triggers it. The anchored line supports the pastoral figure half of the cell, but not "the star calendar". The "river" half also goes beyond what the neighbour and the two sources I opened support. The declared counter still prints `rows=15 resolved=15 distinct=15`, because it checks that anchors resolve, not that they support the cell.

The repair is small (findings F1 to F5). Nothing has been applied. This is a recommendation to the L1: claim D should not be read as HOLDS while row 46 stands as landed.

## Item attacked

Row 46 of section 2 in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (the 14th data row; one of the four new rows at lines 44 to 47):

> `celestial-symbolism-calendars.md:28` | sky figures chosen by subsistence (pastoralists on milky or river figures) and the star calendar | the herd as the subsistence input that selects a sky reading (§10); no second sky-lore or calendar owner

The anchor file is `corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md`. A first read at a guessed `culture-material/` path failed; `glob` found the file.

## Answers to the four questions

**1. Does the anchored line support the cell?** Only in part.

Anchored line `celestial-symbolism-calendars.md:28`, quoted (excerpt): "Three constraints do most of the design work for you: … (2) **subsistence** — farmers anchor on heliacal risings, sailors on star paths, pastoralists on milky/river figures; …"

- "pastoralists on milky or river figures": the words are there. But the line is one clause of a design-frame list, and it has no citation.
- "chosen by subsistence": the line says "anchor on", not "chosen by". Small drift, but it turns a design constraint into a claim about choice.
- "and the star calendar": not in line 28. The neighbour does own star calendars, at its line 88 and at its line 136 heading, but row 46 does not cite them. This half overclaims relative to its anchor.
- "river": the neighbour's own §6 table assigns river figures to riverine-farming societies (line 110) and to irrigation states (line 111). Row 46 inherits that contradiction.

**2. Is the boundary developed or explicitly narrowed in the body, at the section the cell names (§10)?** Only the figure half, and only by restating the anchor.

Body row, entry line 156: "| Sky figures | pastoralists read milky/river figures (`celestial-symbolism-calendars.md:28`) | a subsistence input to sky lore, not a creed |"

- This row predates claim D. At base bff83ba it sits at line 148 (checked with `git grep`). Claim D wrote no body text for row 46.
- It narrows the figure half ("not a creed"). It says nothing about the star calendar or about "no second … calendar owner".
- The cell says the herd "selects a sky reading". The body says only "a subsistence input to sky lore". The cell is stronger than the body.
- The lead sentence (entry line 29) promises that the named body section "develops it". Restating the anchor does not meet that promise.

**3. Does the row duplicate authority, or launder a claim the body marks `(to-verify)`? (Check `surplus`.)**

- Surplus: `grep surplus` on the entry returns one hit, line 155 (the sacrifice row, with `(to-verify)` marked inline). Row 46 makes no surplus claim. No surplus claim is laundered.
- Calendar noun: three §2 rows use "calendar" for different things: line 33 "the agropastoral calendar", line 44 "calendrical rites", line 46 "the star calendar". There is no same-referent double ownership. But the corpus also has `culture-material/calendar-festival-systems.md`, which owns civil and festival calendars and star-anchored new years (its line 118). Row 46 does not name it (F6).
- Laundering: the neighbour's line 28 has no citation and no `(to-verify)`. The neighbour has no `(to-verify)` marker anywhere (grep returned no matches). Row 46 and body line 156 repeat the pastoral claim with no marker. QUALITY criterion 1 forbids exactly this: an unverifiable claim "never laundered into assertion" (F2).

**4. Is it a genuine neighbour or filler?** Genuine as a subject neighbour; filler-grade on the herd side. The second part is my judgement.

- The sky file does own sky figures and star calendars (lines 88 and 136).
- Its only herd-facing lines are line 28 (a generic list of farmers, sailors and pastoralists), line 112 (Greek Hera's milk, glossed "pastoral etiology"), and line 118 ("milk → dairy purity rules"). Row 46 and the body use only line 28.
- The body row would fit farmers or sailors equally well. It names no herd fact that selects a figure.
- The neighbour's couples line (line 20, raw read) names culture-material for "calendrical monumental architecture, harvest economy" and does not name the herd entry. The seam is declared in one direction only.

## Findings

Line numbers are in the herd entry unless marked otherwise.

**F1 (high). The calendar half of the cell has no anchored support** (entry line 46).
- Evidence: answer 1. This triggers claim D's falsifier.
- Smallest fix: keep the cell. Make the first cell one backtick pair holding `celestial-symbolism-calendars.md:28,:88,:136`. Checked read-only: the counter's own `resolve()` accepts `…:28,:88,:136` and returns the file, and returns None for `…:28,:88,:300`, so a dangling line would still fail. Keep all anchors inside that one backtick pair, because the counter checks each backticked token separately. Because the file is the same, `distinct` stays at 15. The full counter has not been re-run after an edit.

**F2 (high). The pastoral sky claim is unsourced and unmarked everywhere it appears** (entry lines 46 and 156; neighbour line 28).
- QUALITY criterion 1 (`corpus/QUALITY.md` lines 5 to 8): "A claim the author cannot verify is marked `(to-verify)` inline — never laundered into assertion."
- Calibration T (`corpus/knowledge/verification/calibration-registry.md:39`): "Mark `(to-verify)` inline at the exact dependency; do not make it load-bearing." Row 46 makes this claim the boundary.
- Calibration H (`calibration-registry.md:38`): "label the designer's choices instead of presenting a discovery." Neighbour line 28 opens as a design frame ("do most of the design work for you"). Row 46 presents the same sentence as what pastoralists "chose".
- The registry already lists this file among routes for sweeping sky-myth claims, marked C/T with "`(to-verify)` for the exact claim" (`calibration-registry.md:183`).
- The entry's own rules forbid the generalisation: line 25 "design a **dial**, not a type"; line 199 "never a pastoral universal".
- External check (see Sources): one people the Baran and Çimen article describes as herding is attested with a milk name (Tuvan). Berezkin lists bird-path names for Kazakh, Kirgiz, Karakalpak and Turkmen (pages 8 to 9) and notes that not all Turks share the concept, so the Turkic picture is mixed, not uniformly bird paths. "Pastoralists" is generalised from one attested case.
- Sibling evidence: `culture-material/hunting-foraging-subsistence.md:13` cites the same neighbour line as "farmers on heliacal risings, sailors on star paths" and leaves out the pastoral clause.
- Smallest fix: add `(to-verify)` after "pastoralists on milky … figures" in the cell (line 46) and in the body row (line 156). Change "chosen by" to "anchor on" to match the line. Narrowing to the attested Tuvan name needs a SOURCES row, which the lane would add; this seat does not add sources.

**F3 (medium). "River" for pastoralists contradicts the neighbour's own table and has no pastoral attestation in the sources I opened** (entry lines 46 and 156).
- Neighbour line 110: river → "riverine-farming cultures with flood calendars". Line 111: river (double) → "irrigation states; astronomy integrated with canal polity". Line 118: river → "a ferry festival and bridge tolls".
- `myth-symbol/cosmology-cosmography.md:39` gives the Milky Way as "Tianhe 'sky river' (China)", a farming-region reading.
- Berezkin 2010 and Baran and Çimen 2026 report no river name for the Milky Way among any pastoral people.
- Smallest fix: delete "river" in line 46 and in line 156.

**F4 (medium). Body development is a pre-existing restatement and never reaches the calendar half** (entry line 156; lead line 29).
- Claim D did not write line 156. It restates line 28 and narrows only the figure half.
- The cell's verb "selects a sky reading" is stronger than the body's "a subsistence input to sky lore".
- Smallest fix: add one §10 sentence, under 40 words, with anchors. It should say that the herd supplies the input the neighbour's milk rule uses (`celestial-symbolism-calendars.md:118`), and that the star calendar stays with `celestial-symbolism-calendars.md:88,:136`. Align the verb to "input".

**F5 (medium). The herd seam is filler-grade and declared in one direction only** (entry lines 46 and 156; neighbour lines 20, 112, 118).
- The neighbour's only herd-product rule, line 118 "milk → dairy purity rules", goes unused.
- The neighbour's couples line (line 20) does not name the herd entry. QUALITY criterion 3 (`corpus/QUALITY.md` lines 13 to 15) asks the couples line to name the systems the entry connects.
- Smallest fix: develop the herd side from neighbour lines 112 and 118, labelled H (`calibration-registry.md:38`), and state what the herd supplies (the milk the rule governs). Do not claim reciprocity; the neighbour's couples line belongs to the neighbour's lane.

**F6 (low). The calendar co-owner is not named** (entry lines 33, 44, 46; `culture-material/calendar-festival-systems.md` lines 19, 26, 118).
- That file's couples line (line 19) and line 26 say the sky layer is `celestial-symbolism-calendars` §8, and that the file itself owns the civil and political machinery. Its line 118 ("Heliacal" row) lists star-anchored new years with "detail in sibling file §5".
- So the star-festival seam is shared by two neighbours. Row 46's "no second … calendar owner" names neither.
- Smallest fix: name the split in prose, without backticks. The counter reads only backticked tokens. A second backticked file in row 46 would make `distinct` exceed `rows` and fail the count.

**INFO.** Entry line 9 contains "the round lesson's located quote". It predates claim D (it is not in D's diff) and concerns the earlier build. It is not a citation added by D.

## Checks that passed

- Declared counter: `rows=15 resolved=15 distinct=15`, exit 0. Row 46 resolves.
- The anchor resolves to one file (`myth-symbol/celestial-symbolism-calendars.md`), and line 28 is in range.
- D's added lines (read in full from `artifact://12663`) contain no S071-or-higher id, no claim-C entry name, no `boundary-count` reference, and no round-51 lesson reference.
- Byte check: the entry's working copy matches commit 35f0d49 (blob `cf1c6f76…`). The neighbour's working copy matches HEAD (blob `c3871ada…`). Neither file changed between 35f0d49 and HEAD.

## Commands run

| # | Command (abridged) | Exit | Key output |
|---|---|---|---|
| 1 | `git --no-pager log --oneline -n 12`; `git --no-pager diff --stat bff83ba 35f0d49`; `git --no-pager diff bff83ba 35f0d49 -- <entry>` | 0 | Tip `9feb69e`; claim `35f0d49`; base `bff83ba`. Entry diff +9/−1 at lines 29–30, 42, 44–47, 93–94. Diff stat: 8 files, 867 insertions, 1 deletion. |
| 2 | `python3 -B reports/round-51/boundary-count.py; echo exit=$?`; `sha256sum reports/round-51/boundary-count.py` | 0 | `rows=15 resolved=15 distinct=15`; `exit=0`; sha256 `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2` |
| 3 | `git --no-pager grep -n "Sky figures" bff83ba -- <entry>` | 0 | line 148 (base) |
| 4 | `git --no-pager grep -n "celestial-symbolism-calendars" bff83ba -- <entry>`; same at 35f0d49 | 0 | base: line 148 only; claim D: lines 46 and 156 |
| 5 | `git rev-parse` and `git hash-object` for the entry and for the neighbour; `git diff --stat 35f0d49 HEAD -- <entry> <neighbour> <calendar-festival>`; `git log --oneline -n 3 -- <neighbour>` | 0 each | Entry `cf1c6f76…` = `cf1c6f76…`; neighbour `c3871ada…` = `c3871ada…`; diff empty; log `e1694ba`, `291c714`, `76c105b` |
| 6 | `python3 -B -c` loading `boundary-count.py` by path (read-only) and calling `resolve()` on three tokens | 0 | `:28` → file; `:28,:88,:136` → file; `:28,:88,:300` → None; `hits_for_celestial_file 1` |
| 7 | `read xd://lsp` | error | "No such tool: xd://lsp. Mounted devices: ast_edit, debug." |
| 8 | `read` (harness): RULES.md, claims.json, QUALITY.md, calibration-registry.md (full; 35–39; 183), boundary-count.py, the entry (full), the neighbour (full; raw lines 20, 28, 86, 88, 110–112, 118, 136), calendar-festival-systems.md (header), `artifact://12663` (D diff), `artifact://13222:117-214` (Baran and Çimen text) | n/a | as quoted above |
| 9 | `read` at a guessed `culture-material/celestial-symbolism-calendars.md` | not found | corrected by `glob` (myth-symbol path) |
| 10 | `glob` for the celestial and calendar-festival files | n/a | two paths found |
| 11 | `grep` (harness): `surplus` (repo-wide and entry); forbidden-citation pattern on the entry; herd, calendar and sky terms on the neighbour, the entry, `civilizations/`, `culture-material/`, `myth-symbol/`; `to-verify` on the neighbour; SOURCES.md for sky and milk terms | n/a | as in the checks above; `to-verify` on the neighbour: no matches |
| 12 | `web_search` (one query) | n/a | summary and leads only; I opened the two PDFs below directly |

Not run: the separability manifest check, `claims-agree.py`, the readme sweep (claim C's item), and any counter re-run after an edit. No sandbox clone was made and no mutation test was needed, because nothing was written.

## Sources opened (access date 2026-10-22)

1. **https://www.folklore.ee/folklore/vol44/berezkin.pdf**. Yuri Berezkin (2010), "The Pleiades as Openings, the Milky Way as the Path of Birds, and the Girl on the Moon", *Folklore: Electronic Journal of Folklore* 44. Found: the "path of birds" Milky Way name is listed for Kazakh (citing Karuts 1911, Potanin 1881, Sidelnikov 1962), Kirgiz, Karakalpak, and Turkmen (up to the mid-19th century), PDF pages 8 to 9. Volga Tatar is also on that list (page 9). The "ski trace" name is "either the only or the most dominant name among Samoyeds and the peoples of Eastern Siberia, Lower Amur and Alaska" (page 9). I read the body text (pages 1 to 17); I did not read the references. No milk or river name for the Milky Way appears for any pastoral people. Tier B (distribution survey; its older citations were not opened). Scope: cosmonym distribution, not herding. Row effect: does not support "river"; does not report the milk clause.
2. **https://www.folklore.ee/folklore/vol98/baran_cimen.pdf**. Buket Baran and Gamze Çimen (2026), "Evaluation of the Concept of Milk among Tuvans and Tatars in an Ethnolinguistic Context Based on Cultural Memory", *Folklore: EJF* 98 (doi 10.7592/FEJF2026.98.baran_cimen, CC BY 4.0). Found: page 3 says Tuvans "have preserved traces of their nomadic lifestyle based on animal husbandry to the present day". Page 16 says "In the Tuvan language, the Milky Way is *Süt Oruu* (D. Monguš 2011: 767), while in the Tatar language it is *Kaz Yulȉ* or *Kiyék Kaz Yulȉ* (TTAS III 241)." Tier B (secondary; the Tuvan name is cited from Monguš 2011, which I did not open). Scope: the milk concept; the Milky Way name is a side note. Row effect: one pastoral people is attested with a milk name. The row does not cite it, and the row still generalises to "pastoralists".

Not opened: other search hits, the Gyarmati 1991 record (bibliographic only), the Monguš 2011 dictionary, Karuts 1911 and the other older works Berezkin cites, and Pseudo-Eratosthenes (the neighbour's Greek milk source).

## Tooling record

- No installs, updates, or package-manager runs. Tools used: git (existing), python3 with the standard library only and `-B` (existing), and the harness read, grep, glob and web tools.
- `lsp`: not available in this seat (`xd://lsp` returns no such tool). The anchored target is a markdown corpus with no code callers or definitions, so I used text grep for literal presence only, as the fallback. I do not present grep output as semantic proof.

## Unrun checks and verification gaps

- Unrun: the separability manifest check (not my item); `reports/round-51/claims-agree.py` (not my item); `reports/round-28/readme/sweep.py` (claim C's item); the full counter after any edit. Only the read-only resolver check ran.
- Gap: I did not open the neighbour's book sources. The Greek "pastoral etiology" gloss rests on Pseudo-Eratosthenes, which I did not check.
- Gap: the pastoral Milky Way literature was checked in two sources only. A sourced pastoral milk or river reading may exist. If one is found and cited, F2 and F3 soften, but F1 (the calendar anchor) still stands.
- Residual risk: the counter cannot detect support errors. A passing 15/15/15 says nothing about F1 to F5, and a reviewer relying on it alone would miss them.
