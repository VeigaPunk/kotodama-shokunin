# Round 51 attempt 3, falsify wave: CriticDSeparability

Seat: `KotodamaR51a3.CriticDSeparability` (critic, leaf, read-only on the lane). Date 2026-10-22. Author-lane attack, never admission.

**Item attacked:** claim D's independence from claim C. D is the pastoralism section-2 boundary table, which grows from 11 to 15 rows in commit `35f0d49`. D must not cite the C entry, any S-id from S071 up, or the round-51 lesson.

**Verdict: HOLDS.** D's landed bytes do not depend on C:

- No form of C's name, sources or round-51 records appears in D's bytes: no path, no S-id from S071 up, no URL, no author or host, and no lesson reference.
- The counter reads `rows=15 resolved=15 distinct=15` on the tree that lacks C.
- The separability checker exits 0.

One finding is about calibration of the instrument, not about D. A clean checker run would not have caught a D-to-C dependency written the way this corpus usually writes citations. D's independence therefore rests on the manual searches below as much as on the checker's exit 0.

## Trees

- Lane tip: `9feb69ec8ef3de00c2de41eea0286ad5031eab17`, which is also `main` and `origin/main`.
- Private clone: `/fast/scratch/hyaku/kotodama-r51a3-falsify/CriticDSeparability` (checked with `realpath`), made with `git clone -q --shared`.
- The D entry blob is the same at D's commit and at the tip: `git rev-parse 35f0d49:$E HEAD:$E` gives `cf1c6f76…` twice.
- D's commit is an ancestor of C's commit: `git merge-base --is-ancestor 35f0d49 da31d3c` exits 0. D was committed at 06:33:02 and C at 06:42:21 (-0300).

Here `E=corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.

## Commands, output, exit codes

| # | Command (where) | Output | Exit |
|---|---|---|---|
| 1 | `git show --stat 35f0d49` (lane, read-only) | 1 file: `$E`, 9 insertions, 1 deletion | 0 |
| 2 | `git diff 1f97472 35f0d49` (lane) | Hunks only at entry lines 29, 37–47 and 93. Four rows were added (`ritual-liminality.md:63`, `symbolism-synthesis-method.md:69`, `celestial-symbolism-calendars.md:28`, `numerals-and-measures.md:101`). The shepherd-king row was rewritten. A lead sentence and a numerals seam sentence were added. | 0 |
| 3 | `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` (clone at tip) | `SEPARABILITY: 0 findings` / `SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2` | 0 |
| 4 | `python3 -B tools/check-claim-separability.py --selftest` (clone) | `selftest: 56/56 checks passed …` | 0 |
| 5 | `python3 -B reports/round-51/boundary-count.py` (clone at tip) | `rows=15 resolved=15 distinct=15` | 0 |
| 6 | Same counter on `git archive 35f0d49` (D's tree before C landed; 226 knowledge files; C entry absent) | `rows=15 resolved=15 distinct=15` | 0 |
| 7 | Same counter on base `bff83ba` plus D's two lands only (C entry absent; 226 files) | `rows=15 resolved=15 distinct=15` | 0 |
| 8 | `sha256sum reports/round-51/boundary-count.py`; `git diff --quiet 1f97472 HEAD -- reports/round-51/boundary-count.py` | `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2` (matches the frozen hash in the build-wave `CriticClaimD.md`); unchanged | 0 / 0 |
| 9 | `python3 -B reports/round-51/claims-agree.py` (clone) | `AGREE claims=['C', 'D']` | 0 |
| 10 | Per-commit check for edits to `corpus/README.md` and `corpus/SOURCES.md` | `1f97472`: none; `35f0d49`: none; `da31d3c`: both; `9feb69e`: none | 0 |
| 11 | `git diff --quiet bff83ba HEAD` for the five anchor files of the rewritten and new rows | No change from base to tip, so C moved no line that D anchors | 0 |
| 12 | Duplicate-basename sweep at tip: `find corpus/knowledge -name '*.md' -printf '%f\n' \| sort \| uniq -d` | Empty. C adds no basename that would make a bare-basename anchor ambiguous to the counter. | 0 |

### Text searches in D's 10 added lines and in the whole entry at tip

Every pattern below returned `added=0`. For the whole entry at tip, the counts are:

- `sign-languages-manual-modality`: 0.
- `linguistics/sign`: 0.
- `sign.language`: 0.
- `[Mm]anual`: 0.
- Prose-deferral words `whistle`, `signal`, `alternate`, `the sign`, `kinesic`, `homesign`, `deaf`, `fingerspell`, `gesture`, `finger`: 0.
- `\bsign`: 5 at tip, all base text in the sense "the animal sign" ("design" does not match). The matches are at lines 8, 12, 41, 158 and 212, all of them outside D's diff hunks and present at base.
- S-ids from S071 up (regex `\bS(07[1-9]|0[89][0-9]|[1-9][0-9][0-9])\b`): 0.
- `https?://`: 0.
- `round-51`, `round 51`, `round51`, `R51`, `lessons`, `boundary-count`: 0.
- `lesson`: 1, at line 9. That line is base text, the S048–S069 source line from round 50, and it refers to that round's lesson. Entry lines 1–12 are byte-identical from base to tip (`diff` exit 0).

Other entry-wide checks at tip:

- S-ids at tip equal S-ids at base: exactly S048–S069.
- Author-year tokens (`[A-Z][A-Za-z-]+ (19|20)[0-9]{2}`): the set at base and the set at tip are identical (`diff` exit 0).
- Exhaustive check against C's sources. I took the 54 rows S071–S124 from `corpus/SOURCES.md`, with 54 URLs, 37 hosts and 41 lead names. None of the URLs or hosts appears in `$E`. Of the lead names, only the word "The" matches, 10 times both at base and at tip; it is not a citation.
- The figure 227 does not appear in the entry, so D records nothing about C's landing.

## Mutation controls (clone only; each restored with `git checkout -- $E`)

These test whether the checker's exit 0 actually covers the citation forms D could have used.

| Plant in D | Checker result | Exit |
|---|---|---|
| M1: prose line citing `` `sign-languages-manual-modality.md:39` `` (bare basename) | `SEPARABILITY: 0 findings` | **0, missed** |
| M2: prose line citing `` `linguistics/sign-languages-manual-modality.md:39` `` (knowledge-relative, the corpus convention) | `SEPARABILITY: 0 findings` | **0, missed** |
| M3: the full repo path `corpus/knowledge/linguistics/sign-languages-manual-modality.md` | `D->C via land path … named at …:214` | 1, caught |
| M4: `(S071)` | `D->C via export '\bS(07[1-9]|0[89]\d|[1-9]\d\d)\b' matched …:214` | 1, caught |
| M5: swap the row anchor `numerals-and-measures.md:101` for `sign-languages-manual-modality.md:39` (counter still prints 15/15/15 at tip) | `D->C via acceptance … fails on base+D.lands (rc=1) and passes on base+D.lands+C.lands` | 1, caught |
| M6: S071's URL `https://archive.org/details/micro_IA41153455_0834` with no S-id | `SEPARABILITY: 0 findings` | **0, missed** |
| M7: `Stokoe 1960` with no S-id | `SEPARABILITY: 0 findings` | **0, missed** |
| Restore | `SEPARABILITY: 0 findings`; clone working tree clean (`git status --porcelain` shows 0 lines) | 0 |

**Proposed fix, tested as a control.** I made a copy of the manifest with one extra export on C, `\bsign-languages-manual-modality\b`, and kept the copy in the clone only; it is now deleted.

- At the clean tip it reports 0 findings and exits 0. The export-novelty check passes; there was no exit 2.
- M1 gives `D->C via export '\bsign-languages-manual-modality\b' matched …:214`, exit 1.
- M2 gives the same finding, exit 1.

## Sources opened

None. D adds no external source: no URL, no author-year citation and no S-id beyond S048–S069, all present at base. My item asks for none, so no URL was opened for this seat.

## Findings

1. **Medium (calibration; the instrument, not D).**
   - **Problem:** The checker's exit 0 does not cover the forms the corpus actually uses to cite another entry or source:
     - the bare basename;
     - the knowledge-relative path;
     - a URL with no S-id;
     - an author-year citation with no S-id.

     M1, M2, M6 and M7 above all exit 0. The only static legs that work are the full repo path and the S-id export (M3, M4). The dynamic leg catches only dependencies inside the table (M5).
   - **Pointers:**
     - The blind spot is in the full-path-only name matcher, `tools/check-claim-separability.py:602-604`, and in C's single export in `reports/round-51/separability-manifest.json`.
     - The build-wave critic predicted it as S2, S3 and S5 in `.ufo/waves/round-51/build/CriticClaimD.md`.
     - The round lesson records the blind spot only for the C-to-REC direction, at `corpus/lessons/round-51.md:16` and `:108`. It does not record it for D to C.
   - **Effect on D:** none. The exhaustive searches above show D uses none of these forms.
   - **Smallest fix:** add one sentence to `corpus/lessons/round-51.md` at `:108`. It should say that the D-to-C direction has the same relative-path and inline-URL blind spot, and that this falsify report's search receipt covers it. Do not edit the frozen manifest after landing. At the next declaration, add the new entry's basename as an export (control above: catches M1 and M2, novelty holds). Pair it with a declared grep of the claim's URL and author list.

2. **Low (depth and provenance of the head, not separability).**
   - **Problem:** The new row anchor `numerals-and-measures.md:101` is missing from the head's in-corpus anchor list at `$E:6`. The other three new anchors are already listed there from base: `ritual-liminality.md`, `symbolism-synthesis-method.md` and `celestial-symbolism-calendars.md`.
   - **Pointer:** `$E:6` against `$E:47` and `$E:93`.
   - **Smallest fix:** append `` `linguistics/numerals-and-measures.md:101` `` to the line-6 anchor list. This adds no C dependency, because the file exists at base and is unchanged to the tip. Leave `verified-at` alone: refreshing it with the joint-tree count of 227 would record C's landing (the build-wave critic's S7).

3. **Low (process, this seat).** I extracted the archive for command #6 briefly into a sibling folder, `/fast/scratch/hyaku/kotodama-r51a3-falsify/CriticDSeparability-pre-c`, instead of under my seat path. It was outside the lane and fleet repo, and I deleted it right after the run. Command #7 then ran inside the seat path (`.../CriticDSeparability/.dtree`, removed afterwards). No lane file was written except this report.

**Checked and holding:**

- The rewritten shepherd-king row (`$E:42`) agrees with §10 (`$E:154`, "self-presentation, not administration").
- The anchored lines exist at base and contain the owned content:
  - `ritual-liminality.md:63`: the Vedic agnihotra milk oblation and the aśvamedha royal horse rite.
  - `celestial-symbolism-calendars.md:28`: "pastoralists on milky/river figures".
  - `numerals-and-measures.md:101`: "counting units (*pair*, *head of cattle* …)".
  - `sacred-kingship-mythic-charter.md:65`: "audited by omens and the gods' assembly".
- C names neither the pastoralism entry nor herding. No S071+ row in `corpus/SOURCES.md` names the pastoralism entry.
- The two entries do not contradict each other about `numerals-and-measures.md`. D anchors line 101 for counting words; C anchors line 107 for finger counting.

**Not assessed (other seats' items):** whether every word in the new rows' ownership cells is supported, for example "the symbol grammar that enforces it" against the single bullet at `symbolism-synthesis-method.md:69`, and "the star calendar" at `celestial-symbolism-calendars.md:28`.

## Unrun

- I did not open any external source; none is in scope for D.
- I did not run `reports/round-28/readme/sweep.py` or the C count; both belong to C's item.

## Impacted axes

- **Calibration:** finding 1, a checker exit 0 that is weaker evidence than it reads.
- **Depth:** finding 2, minor.
- **No defect in D's separability.**

## Tools

None installed or updated.
