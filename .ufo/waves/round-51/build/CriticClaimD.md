# CriticClaimD — attack on claim D's design (round 51, attempt 3)

Seat: `KotodamaR51a3.CriticClaimD` (critic, leaf). Author-lane advice, never admission.
Read at the lane worktree, tip `1f97472` (the declaration commit on top of `5ab3634`); `git diff --stat bff83ba -- corpus` is empty, so the corpus bytes equal base `bff83ba65bf9559af4d7567e81703059667a0005`.
Counter bytes: `reports/round-51/boundary-count.py` sha256 `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2`, the same in the worktree and at `1f97472`.
Baseline reproduced: `python3 -B reports/round-51/boundary-count.py` printed `rows=11 resolved=11 distinct=11` with exit 0.
No files were written except this report. Mutants ran in memory: the counter module was imported with `python3 -B`, and its `knowledge_index`/`resolve` functions were called on edited copies of the entry's lines. No tools were installed.

## Verdict

D can be met as declared, and it can also be met by filler. The counter checks that rows exist and that line numbers fall inside a file. It does not check relevance, shape, preservation of the old rows, or body development. Seven filler patterns all print a passing `rows=15 resolved=15 distinct=15`.

The distinct rule is wrong for the `civilizations/` group row in both directions:
- It counts a member file as a new neighbour.
- It fails the round-50 repair that would anchor the group row.

Growing the table to 15 repairs only the row-count part of routed defect 2. The round-50 review that measured the defect also found other §2 problems, and most are still open at base: boundaries never developed in the body, no lead sentence, a missing market row, the unanchored group row, and a shepherd-king contradiction. There are also several silent paths by which D could depend on C that the separability checker cannot see.

The counter is frozen in the declaration commit. Editing it now would change the ruler after measurement, the same class of defect as round 50's R50-M5. So every correction below is a landing rule for D or a falsifier for wave 2. None is a counter edit.

## 1. Filler: the counter is satisfiable without new neighbours

What the counter checks (`boundary-count.py:44-60`, `:84-92`):
- Each first-cell token must resolve to a file or directory.
- Each line number only has to satisfy `1 <= start <= last <= length`.
- `distinct` is the size of the set of targets. It is not a one-to-one match between rows and targets.

Nothing reads the ownership cell, the boundary cell, the body, or the base rows.

In-memory mutants. Each adds four rows to the base table unless noted. Cells are `| <first cell> | x | y |`.

| Mutant | First cells added | Printed | Defect it proves |
|---|---|---|---|
| M1 irrelevant real line | `architecture-settlement-lexicon.md:1`, `ritual-liminality.md:1`, `celestial-symbolism-calendars.md:1`, `symbolism-synthesis-method.md:1` | `rows=15 resolved=15 distinct=15` exit 0 | Relevance is unchecked; line 1 is a title line |
| M2 split the group row | `mongol.md:40`, `finnic-sami.md:140`, `dine-navajo.md:125`, `inca.md:128` | 15/15/15 exit 0 | Members of the group row count as new |
| M3 directory tokens | `linguistics/`, `myth-symbol/`, `verification/`, `culture-material/` | 15/15/15 exit 0 | A directory "resolves" with no line at all |
| M4 bare filenames | `ritual-liminality.md`, `symbolism-synthesis-method.md`, `celestial-symbolism-calendars.md`, `calibration-registry.md` | 15/15/15 exit 0 | The `:N` group in `FILE_ANCHOR` (`:25`) is optional, so "path:line" is not enforced |
| M5 old neighbour dropped | delete the `civilizations/` row; add 5 of its members | 15/15/15 exit 0 | "The existing 11 rows keep their neighbours" is unchecked |
| M6 non-one-to-one | row A = `ritual-liminality.md:63` + `celestial-symbolism-calendars.md:28`; row B = `celestial-symbolism-calendars.md:28`; plus 2 more | 15/15/15 exit 0 | Row B names no neighbour of its own |
| M9 whole-file range | `ritual-liminality.md:1-<file length>` with empty ownership and boundary cells | rows=12 resolved=12 distinct=12 exit 0 | A range covering the whole file is accepted, and empty cells pass |
| M11 group plus member | `civilizations/mongol.md:40`, `myth-symbol/`, `ritual-liminality.md:63`, `symbolism-synthesis-method.md:69` | 15/15/15 exit 0 | A directory and a member under it are always distinct |
| M7 control: same file, two spellings | `mongol.md:40` and `civilizations/mongol.md:40` | distinct=14 exit 1 | Robust: both spellings resolve to the same path, so they deduplicate |
| M8 control: out-of-range line | `ritual-liminality.md:1-9999` | resolved=11 of 12, exit 1 | Robust |
| M10 control: second table in §2 | a 2-row narrowing table appended inside §2 | rows=14 resolved=12, exit 1 | Fails closed; any body development inside §2 must not be a table |

Basename collisions: none at base, and C's basename does not collide (checked against the index). A future duplicate basename would make bare-basename anchors fail closed, which is safe.

Real-world instance of the M1 risk: three of the six in-flight row drafts anchor lines whose boundary cells claim more than the line or the body supports (section 3).

Impacted axes: depth (counts without content), quality (usability), calibration.

## 2. The distinct rule for the `civilizations/` group row

Row 11 at `pastoralism-animal-husbandry.md:41`:

```
| `civilizations/` regional entries | Mongol, Turkic, Scythian, Sámi, Diné, Inca cases and their warnings | general method only; regional herds are cited, never restated |
```

- **It double counts.** `resolve` returns the token string `civilizations/` for a directory but an absolute path for a file (`:46-47`, `:60`). The two can never be equal. Any new row naming one of the six already-tabled members, or any other `civilizations/*.md`, raises `distinct` by one (M2, M11). By the Goal's wording ("ONE distinct in-corpus neighbour not already in the table"), those six are already in the table.
- **It blocks the round-50 repair.** Round-50 ReviewSec02 F8 (`.ufo/waves/round-50/falsify/ReviewSec02.md:454-487`) found this was "the only row in the table with no anchor". It also found that the header "Neighbour (anchor)" is false for it. The natural fix is to anchor the row with its six verified member lines. I tested that fix in place, plus four genuine rows: the counter printed `rows=15 resolved=15 distinct=20`, exit 1. Under this ruler, F8 can only stay open or be "repaired" by splitting, which is padding. Splitting into six rows plus four genuine rows gives 20 rows, which also misses the frozen `rows=15`.
- **The before-value relaxes the claim's own definition.** claims.json D.statement says "Each row names one distinct in-corpus neighbour by a backticked path:line anchor that resolves". Row 11 has no `path:line`, so `resolved=11` really means "10 path:line rows plus 1 directory".

Classification: this is a tradeoff the judge must hold, not a defect D can fix this round. The safe reading:
- D adds no row for any `civilizations/*.md` file.
- D leaves row 11 as a disclosed directory row.
- The report and lesson state that `resolved=15` is 14 path:line rows plus 1 directory, and that F8 is carried.
- The right rule for a later counter: expand a directory row to the members it names, so those members are not new; forbid those members in other rows; and require `:N` everywhere.

Impacted axes: depth, discernment (false provenance if "resolved" is read as "anchored").

## 3. Does 11 → 15 repair the routed defect? Only the count

Routed debt item 2, in full (`corpus/lessons/round-50-verifier-spotcheck.md:94`): "Address the commissioned neighbour target **and residual source/content markers** without lowering it." The same verifier wrote at `:47-48`: "no prose-accuracy or complete commissioning claim is granted from file counts."

The commission itself (`.ufo/waves/round-50/build/ReviewEntryContract.md:62`): "One sentence, then `| Neighbour | What it owns (live anchor) | This entry's boundary |`, 15 or more rows (§4 is the candidate set)." The candidate set is `ReviewEntryContract.md:212-236`, 23 paths.

claims.json D.kind narrows the defect to "target 11 of at least 15". Residual items still open at base:

| Round-50 finding | State at base `bff83ba` (evidence) | Does 15 rows fix it? |
|---|---|---|
| ReviewSec02 F4: boundary phrases never developed in the body | each of "milking", "churning", "dairy chain", "shearing season", "dung source", "herded counterpart", "riding and pack", "herd ledger" occurs exactly once, in its own §2 cell (`grep -oi`, count 1 each) | No |
| F5: lead sentence and header | §2 runs header-to-table at `:27-29`, with no sentence; header is "What it owns", not "(live anchor)" | No. Both are counter-neutral, so D may add them |
| F6: market row | `trade-economy-lexicon.md:3` is cited 0 times. Scope `:12` and §15 `:204` hand "the market" to "(§2)". `hunting-foraging-subsistence.md:116` pins the market owner at `trade-economy-lexicon.md:3` | No. Adding `:3` to the existing trade row keeps that neighbour; tested: still 11/11/11 exit 0 |
| F6: 7 never-cited candidates | `ritual-garments`, `music-instrument-lexicon`, `calendar-festival-systems`, `hero-journey-variants`, `source-discipline-calibration`, `coupling-model`, `costume-era-consistency-gate` each have 0 entry hits; `writing-media-surface-economy` has 1, the "sherd" false positive | Partly, only if the new rows come from this set |
| F8: unanchored group row | unchanged | No; blocked by the counter (section 2) |
| ReviewSec10 F4 and round-50.md:126-127: the shepherd-king administration boundary is unexpanded | §2 row 10 boundary "the herd ledger that office audits (§10)" (`:40`) contradicts §10 "self-presentation, not administration" (`:146`). The anchored line `sacred-kingship-mythic-charter.md:65` has the gods auditing the ruler, not the ruler auditing a herd | No |
| Residual content markers | 33 `(to-verify)` markers on 25 lines | No |

Every candidate anchor in the round-50 set still resolves and supports its fragment at current bytes. Re-checked: `writing-media-surface-economy.md:138` ("herd, lime pits"), `ritual-garments.md:80` (the pallium clause is later on that line), `music-instrument-lexicon.md:87`, `calendar-festival-systems.md:79`, `hero-journey-variants.md:110`, `source-discipline-calibration.md:96`, `coupling-model.md:150`, `costume-era-consistency-gate.md:65`. So the honest repair is reachable without filler.

Counterexamples from the six in-flight row drafts (`.ufo/waves/round-51/build/ScribeRow*.md`):
- **Zero-development rows.** `ScribeRowSymbolismSynthesisMeth.md:35` says "No new body text is required". The celestial draft (`ScribeRowCelestialSymbolismCale.md:33`) says "No sentence needed". Three of the six drafts target files §10 already cites (`ritual-liminality`, `symbolism-synthesis-method`, `celestial-symbolism-calendars`). Four rows built that way would be "developed in the body" only through pre-existing §10 text. The count goes up while the entry gains a table line and no new depth.
- **Laundering a `(to-verify)`.** `ScribeRowRitualLiminality.md:17` has the boundary "the herd's culled surplus males are the standing pool of substitute victims". §10 marks surplus-male offerings `(to-verify)` (`:147`), and round-50 ReviewSec10 F1 found them unsourced. `ScribeRowSymbolismSynthesisMeth.md:18` repeats "surplus males". A §2 boundary cell would then assert, without the marker, a claim the body leaves unverified.
- **Contradicting a scope note.** The same draft says the rite audits "the tally-stick count". §10 `:144` says the S064 count is "a literary fact before it is a ritual one".
- **Duplicate authority.** The agrarian row (`:31`) is the calendar owner: "cite that calendar; ... not a second calendar owner". `ScribeRowCalendarFestivalSystem.md:16` adds a second calendar owner unless it is explicitly split (civil and festival statute versus the work calendar). Its `:53` anchor is the Sothic-drift line, which does not support anything about livestock; `:79` and `:121` do.
- **Owner adjacent to C.** `ScribeRowNumeralsAndMeasures.md:17` anchors `numerals-and-measures.md:101,:109`, which support the cell. But C's declared partial owner is `numerals-and-measures.md:107` (finger counting). This is safe only while D's row and body stay off `:103-108` and off finger or body counting.

Smallest safe correction:
- Keep 15 as the target, but write the claim and lesson as "repairs the row-count leg of routed defect 2", not "repairs routed defect 2".
- Draw at least two of the four rows from the round-50 never-cited candidate set.
- Give each new row at least one new body sentence that states the boundary, or move the cell to what the body already says.
- Carry `(to-verify)` into any §2 cell that repeats a marked claim.
- Land the counter-neutral repairs: the lead sentence, and the market anchor `trade-economy-lexicon.md:3` on the existing trade row.
- Disclose F4, F8, the shepherd-king contradiction and the markers as carried.

Impacted axes: depth, calibration, discernment.

## 4. Separability: ways D could silently depend on C

The separability checker has two relevant limits:
- Its static leg matches only the full repo path: `_name_re` at `tools/check-claim-separability.py:602-604`, for land paths absent at base (`:366-368`).
- Its dynamic leg runs each unit's acceptance on base plus that unit's lands, and repairs with one other unit only after a failure (`:647-669`). It never runs the joint tree.

| # | Path to dependency | Caught by the checker? |
|---|---|---|
| S1 | A §2 first cell anchors `sign-languages-manual-modality.md:N` or `linguistics/sign-languages-manual-modality.md:N` | Dynamic leg yes: the row does not resolve on base plus D. Static leg no: the entry convention is knowledge-relative, never `corpus/knowledge/...`. A run of the counter on the landed tree only hides it |
| S2 | Body or head names C by bare or knowledge-relative path, e.g. "manual signalling belongs to `sign-languages-manual-modality.md`" | No (R50-M6 class). The counter ignores the body, and the static leg needs the full path |
| S3 | A prose dependency with no path, e.g. herder whistle or gesture signals deferred to "the sign-language entry", or alternate sign languages used while herding or hunting | No. This also overlaps C's "alternate" register |
| S4 | D cites a source opened this round as S071 or above | Static export regex `\bS(07[1-9]\|0[89]\d\|[1-9]\d\d)\b` catches the literal. A range such as "S070–S071" is also caught |
| S5 | D cites a new source by URL or author-year without an S-id | No. QUALITY criterion 7 (`corpus/QUALITY.md:31`): "Sources a claim cites are that claim's lands" and "inline URLs standing in for the registry rows" do not count. Registering it would need `corpus/SOURCES.md`, which is C's land, so it would overlap. **D can add no external source this round**; body development must use in-corpus anchors and S001–S070 |
| S6 | D edits the entry's `- topic:` line (`:3`) | No. `reports/round-28/readme/sweep.py:139-141` requires the README row (`corpus/README.md:297`, C's land) to equal the topic text. Base plus D passes, and base plus C passes, but the joint tree fails C's sweep. The likely "fix" would be editing C's README, which would put D's bytes in C's land |
| S7 | D updates the head `verified-at` or `gap filled` counts to 227, or reruns the sweep with C present | No. D's bytes would then record C's landing |
| S8 | D names the round-51 lesson in any spelling (`round-51.md`, `lessons/round-51.md`) for Gate quotes or a mistake | Only the full `corpus/lessons/round-51.md` spelling is caught. This is round 50's exact failure in the other claim |
| S9 | D edits `corpus/README.md` to refresh the pastoralism row | Caught as an overlap; listed so nobody "fixes" S6 this way |
| S10 | The counter indexes the whole `corpus/knowledge` tree, and C adds a file | Low risk: no basename collision, and `linguistics/` already exists. If C's name ever collided with a bare-basename anchor, D's count would drop only in the joint tree |

Impacted axes: separability (QUALITY criterion 7), provenance, discernment.

## Falsifiers wave 2 must run on the landed rows

Notation: `E=corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`; `B=bff83ba65bf9559af4d7567e81703059667a0005`. Run in a private clone. The D-only tree is base plus D's two lands, with C's file absent.

1. **Counter on two trees.** Run `python3 -B reports/round-51/boundary-count.py` on the landed tree and on the D-only tree. Both must print exactly `rows=15 resolved=15 distinct=15`, exit 0. Setup for the D-only tree: `git clone -q --shared <lane> W && git -C W checkout -q --detach $B`, copy the landed `$E` into `W`, copy `boundary-count.py` from `1f97472`, then run. This catches S1.
2. **Ruler frozen.** `sha256sum reports/round-51/boundary-count.py` must equal `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2`.
3. **Old rows preserved (M5).** Every first-cell token in the base §2, from `git show $B:$E`, must be present in the landed §2 first cells. Pass: tokens may only be added, for example `:3` on the trade row. Removing a token or a row fails.
4. **New-row shape (M2–M4, M6, M9, M11).** Each of the four new rows must:
   - carry exactly one backticked token in its first cell, matching `^[\w-]+\.md:\d+(-\d+)?(,\s*:\d+(-\d+)?)*$`;
   - not be a directory and not a bare filename;
   - not be any `civilizations/*.md`;
   - have a basename not appearing in any other §2 row;
   - have every range at most 5 lines.
5. **Support, judged by a reader.** For each new row, quote the anchored line and state whether it carries the ownership cell's nouns. Any row whose line does not support it fails D, per the claims.json falsifier. Known weak spot: `calendar-festival-systems.md:53` does not support a livestock reading.
6. **Body development.** For each new row:
   - name the body line outside §2 (outside lines `:27-41` at base numbering) that develops or narrows its boundary;
   - state whether that line is new in D's diff or was already there;
   - report the count of rows relying only on pre-existing §10 text.

   Each §2 boundary phrase must occur at least once outside §2, so `grep -oi '<phrase>' $E | wc -l` must be at least 2.
7. **No laundered markers.** No new §2 cell may assert a claim the body marks `(to-verify)` without carrying the marker. Check "surplus males" specifically: `grep -n 'surplus' $E`.
8. **No duplicate authority.** No two §2 rows may own the same noun unless explicitly split. Check "calendar" (agrarian row versus calendar-festival), "tally" and "count" (numerals versus symbolism-synthesis), and "surplus males" (ritual-liminality versus symbolism-synthesis).
9. **C independence beyond the checker (S2, S3, S8).** On D's added lines, `git diff $B -- $E | grep '^+' | grep -niE 'sign-lang|manual-modality|sign language|fingerspell|homesign|manual code|finger count|round-51|boundary-count'` must return 0 lines.
10. **No new sources (S4, S5).** Added lines contain no `\bS(07[1-9]|0[89]\d|[1-9]\d\d)\b`, no `http`, and no author-year citation lacking an S001–S070 id. `corpus/SOURCES.md` is not in D's diff.
11. **Topic, README and head invariance (S6, S7, S9).**
    - `diff <(git show $B:$E | sed -n 3p) <(sed -n 3p $E)` must be empty.
    - `corpus/README.md` must be absent from D's diff.
    - `python3 -B reports/round-28/readme/sweep.py` must exit 0 on the joint tree.
    - The head must not state 227.
12. **Separability checker.** `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` must exit 0. This is necessary but not sufficient: falsifiers 9–11 cover its blind spots.
13. **Section-2 shape (M10).** §2 contains exactly one table. The header line is still exactly `## 2. One-owner boundary`; renaming it makes the counter exit 2. The entry stays at most 250 lines (204 at base).
14. **Repair-scope honesty.** The D report and lesson must say "row-count leg of routed defect 2" and must list as carried every item not landed: F4 phrases, F5 lead sentence and header, F6 market anchor, F8 group row, the shepherd-king contradiction at `:40` versus `:146`, and 33 `(to-verify)` markers. A wording of "routed defect 2 repaired" fails the round on discernment.

## Unrun checks

- The separability checker was not executed, so it is inspected only. The joint-tree S6 failure is inferred from the code at `sweep.py:139-141` and `check-claim-separability.py:647-669`, not observed.
- No row has landed, so falsifiers 1–14 are unrun.
- I did not locate the origin of the round-50 commission wording beyond `ReviewEntryContract.md:62`.
