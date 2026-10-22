# ReviewDOldRows: claim D, no-harm leg

**Seat:** KotodamaR51a3.ReviewDOldRows (leaf reviewer; read-only on the lane; no subagents, no background jobs)
**Round:** 51, attempt 3, FALSIFY wave. Claim D lands as `35f0d49` on declaration `1f97472`. Claim base `bff83ba`. Lane `main` at `9feb69e`.
**Item attacked:** the no-harm leg of claim D (the 11 existing boundary rows keep their neighbours and anchors), the changed shepherd-king row, the new lead sentence, and the new section-5 sentence in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (called "pastoral" below).
**Sources:** no external URL opened. The scope is in-corpus anchors only.

## Verdict

- No-harm leg: **HOLDS**. The 11 existing rows keep their neighbours and anchor strings, and the counts reproduce.
- Item as landed, judged on depth: **HOLDS-WITH-FIXES**. Three medium and five low findings below. Each fix is a wording or citation edit. None changes a printed counter value (base 11/11/11 and lane 15/15/15, both exit 0), and none triggers the claim's falsifier.
- No high-severity findings.

## What holds

1. **Diff scope.** `git diff 1f97472 35f0d49 -- <pastoral>` has three hunks, 9 insertions and 1 deletion: the lead sentence (line 29), one changed row (line 42, sacred-kingship), four new rows (lines 44–47), and the section-5 sentence (line 93). Line numbers are the D-commit numbers.
2. **Old rows unchanged.** Base rows sit at base lines 31–41: agrarian 31, hunting 32, cuisine 33, transport 34, trade 35, textile 36, semantic 37, fire 38, animal 39, sacred 40, civilizations 41. Ten of the eleven are byte-identical in both commits, since no hunk touches them. The sacred row keeps its neighbour and anchor `sacred-kingship-mythic-charter.md:65`; only its two text cells change. Row order is unchanged, and the new rows follow the civilizations row.
3. **Neighbour files untouched.** `git diff --stat 1f97472 9feb69e` lists six files: the pastoral entry, QUALITY.md, README.md, SOURCES.md, the sign-language entry and the round-51 lesson. No neighbour file is among them. `git diff --stat 35f0d49 HEAD` lists five files, none a neighbour. `git diff --stat HEAD` is empty, so the tree is clean.
4. **Counter.** In a private clone at `1f97472`: `rows=11 resolved=11 distinct=11`, exit 0, which matches the claim's "before". At lane HEAD: `rows=15 resolved=15 distinct=15`, exit 0, which matches "after_required". Every old anchor still resolves.
5. **Must-not-cite.** The pastoral entry has no match for `S07[1-9]`, `S0[89]x`, `S1[0-2]x`, `round-51`, `lessons/`, `sign-lang`, `boundary-count` or "sign language". D's added lines cite no S-id, no C entry, no lesson and no counter.
6. **Shepherd-king row, ownership cell.** The anchor at line 65 reads "Mesopotamian kingship: the king as *sipa*, shepherd, with his rule audited by omens and the gods' assembly" and "the ruler is the god's tenant, servant, or shepherd — an office, not a person". The cell "the shepherd-king office, audited by omens and the gods" is supported. The base cell (base line 40) read "the herd ledger that office audits", which put the auditing on the office. Line 65 says the office is audited. D's change corrects that direction.
7. **Section-5 sentence, anchor.** `numerals-and-measures.md:101`: "This entry owns only the *words* — mensural classifiers, counting units (*pair*, *head of cattle*, *dozen*, *score*)". The "belong to" claim is supported.
8. **Old-row anchors.** I read each anchor line. Each one supports its ownership cell as written:
   - agrarian :56 (plough team; communal herding after harvest) and :62 (ploughing peak plus herd calendar; manure contracts; transhumance);
   - hunting :36 (wild source: not planted, herded or owned) and :116 (meat-for-crops, marked `(to-verify)`);
   - cuisine :67 (yogurt lineages), :81 (milk + meat separation), :152 (Harris's cow economics, contested);
   - transport :92 (route class) and :95 (draught: load figure, harness and feed vocabulary);
   - trade :69 (Gmc *fehu*; Lat. *pecūnia* < *pecus* "cattle");
   - textile :22 (wool chain) and :27 (worsted/woolen fork);
   - semantic :70 (pastoral wealth vocabulary) and :105 (steppe bundle: herd wealth, raid, pasture);
   - fire :37 (dried dung: the herd's output, as fuel);
   - animal :73 (Nuer cattle idiom) and :110 (Mongol five livestock as wealth-language);
   - civilizations/ (a directory; see M2 and M3).
9. **New-row anchors.** I checked these because the lead sentence covers them. `ritual-liminality.md:63` names "Vedic agnihotra daily milk oblation; aśvamedha year-long royal horse rite", which supports :44. `symbolism-synthesis-method.md:69` says "An animal taboo implies a rite; write both or neither", which supports the rule but not the phrase in L5. `celestial-symbolism-calendars.md:28` names pastoralists on "milky/river figures", which supports :46 in part (see L5). `numerals-and-measures.md:101` supports :93.
10. **Report folder.** `.ufo`, `.ufo/waves` and `.ufo/waves/round-51` are real directories, not links, so this report sits inside the lane.

## Findings

Paths are relative to `corpus/knowledge/culture-material/` unless shown otherwise.

### M1 (medium): the lead sentence says every row names a body section; 8 of 15 rows name none
- Where: `pastoralism-animal-husbandry.md:29`. The boundary cells at :33, :34, :35, :36, :37, :38, :40 and :43 name no § section. The seven that do (:39 §5, :41 §7 §10, :42 §10, :44–:46 §10, :47 §5) do develop their seams.
- Smallest fix: at :29, change "and the body section named in the boundary cell develops it" to "and any body section named in the boundary cell develops it".

### M2 (medium): the lead sentence says each row names one neighbour and a line; row :43 names a directory of case files
- Where: :29 against :43 (`civilizations/` regional entries, which names six cases). The directory holds many case files, such as `mongol.md`, `turkic-steppe.md` and `inca.md`.
- Smallest fix: at :29, write "names one neighbour (a path:line anchor, or for the regional cases the `civilizations/` directory) and the line that shows what it owns". M1 and M2 can share one edit.

### M3 (medium): the counter accepts a directory row, so "15" does not meet the claim's own wording
- Where: `reports/round-51/claims.json`, claim D, `statement`: "Each row names one distinct in-corpus neighbour by a backticked path:line anchor that resolves". `reports/round-51/boundary-count.py:8-11` (docstring: `dir/` names an existing knowledge directory) and `:46-47` (a token ending in `/` resolves to the directory). Row :43 has no path:line anchor.
- Measured: at lane HEAD, 14 of 15 rows carry a path:line anchor. At base, 10 of 11 do.
- Smallest fix: report the strict count (14 path:line rows plus one directory row) beside 15. Rewording the statement after measuring would be a post-hoc change, so I recommend disclosure. L1 decides.

### L1 (low): the shepherd-king boundary cell adds a reading the anchor does not state, and drops the ledger frame
- Where: :42, "the herd the shepherd image draws on; self-presentation, not administration (§10)". The anchor at :65 says "shepherd" but not "herd", and says nothing about self-presentation. It frames the shepherd as "an office, not a person", audited by omens and the gods. "Self-presentation, not administration" is the entry's own reading. The same phrase sits unlabelled at :154, which predates D.
- Depth: the base cell used "the herd ledger". Section 10's frame at :148 is "The herd is ledger, offering and metaphor at once (design frame, **H**)". The new cell drops "ledger".
- Calibration: `corpus/knowledge/verification/calibration-registry.md:38` (code H) asks that designer choices be labelled.
- Smallest fix: "the herd ledger the shepherd answers for (§10)". That keeps the audit direction line 65 supports and the ledger frame of §10. Label the "not administration" gloss (H), or drop it.

### L2 (low): "aligned with section 10" is only partly true
- Where: :42 says "audited by omens and the gods", which line 65 supports. §10 at :154 says "audited by the gods". D did not touch :154, and no hunk covers it.
- Smallest fix: at :154, write "audited by omens and the gods" (one cell, outside D's diff), or drop "aligned" from the record.

### L3 (low): the anchor's Mesopotamian scope is dropped
- Where: :42 "the shepherd-king office" and :154 "the ruler as shepherd". The anchor at :65 says "Mesopotamian kingship". `calibration-registry.md:37` (code B) reads "no extrapolation by resemblance".
- Smallest fix: write "the Mesopotamian shepherd-king office" at :42, and the same at :154.

### L4 (low): the section-5 sentence adds an uncited practice claim
- Where: :93, "this entry supplies what a herd count records — composition, age and sex, ownership marks". It has no S-id, anchor, `(to-verify)` or code. `corpus/QUALITY.md:5-8` (criterion 1) requires every factual claim to carry a source or `(to-verify)`. Age and sex (S052) and ownership marks (S059) are sourced in §5's table. "Composition" is not sourced.
- Smallest fix: cite S052 and S059 at :93, or mark the sentence (H) if it is read as scope.

### L5 (low): two phrases in the new rows are not on their anchor lines
- Where: :45, "the symbol grammar that enforces it". The anchor, `symbolism-synthesis-method.md:69`, says "An animal taboo implies a rite; write both or neither", and a file-wide search for "symbol grammar" finds nothing. Also :46, "the star calendar". The anchor, `celestial-symbolism-calendars.md:28`, says "farmers anchor on heliacal risings, sailors on star paths, pastoralists on milky/river figures". "Star calendar" is not on that line and not in the file.
- Smallest fix: keep the anchor's own words ("write both or neither"; "heliacal risings"), or cite the sentence that uses the term.

## Residual risk and verification gaps
- The counter checks line ranges only. It does not check that an anchored line supports its ownership cell. I did that by reading the anchor lines in the lane HEAD tree. HEAD equals `35f0d49` for these files, since `git diff --stat 35f0d49 HEAD` excludes them.
- Not run, because they belong to other legs: `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`; `reports/round-51/claims-agree.py`; `reports/round-28/readme/sweep.py`; the declaration dry-run receipt.
- No external URL was opened, and no source leg was checked here.
- The new rows' body development (claim D's "developed or explicitly narrowed") is outside this leg. Other seats cover rows :44–:47.

## Commands run (exit codes)

| # | Command (lane-relative unless shown) | Exit | Result |
|---|---|---|---|
| 1 | `git diff 1f97472 35f0d49 -- <pastoral>` | 0 | three hunks, +9 / -1 |
| 2 | `git log --oneline -8 main` | 0 | HEAD `9feb69e`; `35f0d49`, `1f97472`, `bff83ba` in history |
| 3 | `git diff --stat 1f97472 35f0d49` | 0 | one file, +9 / -1 |
| 4 | `git show 1f97472:<pastoral>`, `git show 35f0d49:<pastoral>`, `git show 35f0d49:<sacred>`, `git show 35f0d49:<numerals>` | 0 each | file contents, read through artifacts |
| 5 | `git diff --stat 35f0d49 HEAD` | 0 | five files, none a neighbour |
| 6 | `git diff --stat HEAD` | 0 | empty (clean tree) |
| 7 | `git diff --stat 1f97472 9feb69e` | 0 | six files, including the pastoral entry |
| 8 | `python3 -B reports/round-51/boundary-count.py` | 0 | `rows=15 resolved=15 distinct=15` |
| 9 | Scratch clone `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewDOldRows`: `git clone -q --shared`; `git checkout -q --detach 1f97472`; `rev-parse --short HEAD`; `python3 -B …/boundary-count.py` | 0 | HEAD `1f97472`; `rows=11 resolved=11 distinct=11` |
| 10 | `ls -ld` on `.ufo`, `.ufo/waves`, `.ufo/waves/round-51`; `realpath -m` on `falsify` | 0 | real directories; path inside the lane |
| 11 | Grep for must-not-cite terms in the pastoral entry | no matches | none |
| 12 | Greps for line numbers and phrases (pastoral, sacred, numerals, ritual, symbolism, celestial) | n/a | lines 29, 42, 93, 146–148, 154; "symbol grammar" and "star calendar" absent from their files |
| 13 | Reads: `reports/round-51/claims.json`; `reports/round-51/boundary-count.py`; `corpus/QUALITY.md`; `corpus/knowledge/verification/calibration-registry.md:33-40`; `corpus/knowledge/civilizations/` listing; 17 old anchor lines; 4 new anchor lines | n/a | as cited above |

## Tooling
No tools installed or updated. The only write outside the lane is the scratch clone. Inside the lane, the only write is this report.
