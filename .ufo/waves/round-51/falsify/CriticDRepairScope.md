# CriticDRepairScope — attack on claim D's repair-first framing (round 51, attempt 3, falsify)

Seat: `KotodamaR51a3.CriticDRepairScope` (critic, leaf). Author-lane attack, never admission.
Item attacked: the repair-first framing of claim D (`reports/round-51/claims.json:17`) against routed debt 2 of `corpus/lessons/round-50-verifier-spotcheck.md`, and how the round-51 lesson disposes of that debt.
Read at lane tip `9feb69e`. The entry `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (below: E) is byte-unchanged after D's commit `35f0d49`. Base B = `bff83ba65bf9559af4d7567e81703059667a0005`.
Writes: this report only. The sandbox is a private clone at `/fast/scratch/hyaku/kotodama-r51a3-falsify/CriticDRepairScope` (realpath checked). No tools were installed. No URLs were opened, because this item rests on in-lane records and no source row.

## Verdict: HOLDS-WITH-FIXES

The round-51 records do not claim more than the row-count leg. The lesson says "Row-count leg only" (`corpus/lessons/round-51.md:17`) and "D repairs the row-count leg of routed debt 2 only" (`:106`). All four named non-landed items are listed as carried in both places:
- body development of the old cell-only phrases;
- the market row;
- the unanchored `civilizations/` row;
- the `(to-verify)` markers.

No record says "routed debt 2 repaired". `SCORECARD.md`, `LOG.md` and `SHONEN.md` have no round-51 text yet.

Two parts of the framing still fail on calibration:
- **The debt is narrowed.** `claims.json:17` and the lesson both drop the debt's "source" half.
- **The new rows add little depth.** D's statement says "the four new rows are developed or explicitly narrowed in the entry body". In fact three of the four new rows re-tabulate neighbours the entry already cited at base, against a §10 that is byte-identical to base. One row's boundary is developed nowhere.

D is **mostly a count move with one genuine seam**: the numerals row plus its §5 sentence. It also lands two real counter-neutral repairs: the lead sentence and the shepherd-king alignment.

## Commands (all exit 0 unless stated)

All run in the lane, read-only, except the D-only tree, which ran in the sandbox.

| # | Command (abridged) | Output |
|---|---|---|
| 1 | `python3 -B reports/round-51/boundary-count.py` (lane) | `rows=15 resolved=15 distinct=15`, exit 0 |
| 2 | `sha256sum reports/round-51/boundary-count.py`; `git show 1f97472:… \| sha256sum` | both `fb1d5c89…b1f14cc2`: ruler frozen |
| 3 | Sandbox: `git checkout --detach B`, copy E from `35f0d49` and the counter from `1f97472`, run the counter. C's entry is absent | `rows=15 resolved=15 distinct=15`, exit 0. The first redirect attempt errored, `failed to redirect … No such file or directory`, because `reports/round-51/` did not exist at B; the fallback `mkdir` then ran |
| 4 | `git diff B 35f0d49 -- E \| grep '^+' \| grep -niE 'sign-lang\|manual-modality\|sign language\|fingerspell\|homesign\|manual code\|finger count\|round-51\|boundary-count' \| wc -l` | `0` |
| 5 | Same added lines: `grep -cE '\bS(07[1-9]\|0[89][0-9]\|[1-9][0-9][0-9])\b\|http'` | `0` (grep exit 1, no match) |
| 6 | Topic line 3, base against D | identical |
| 7 | The 11 base first cells against the first 11 landed first cells | preserved |
| 8 | Citations of each new neighbour in E, base → landed (`grep -o … \| wc -l`) | `ritual-liminality` 3→4; `symbolism-synthesis-method` 4→5; `celestial-symbolism-calendars` 2→3; `numerals-and-measures` **0→2** |
| 9 | sha256 of each of §10–§13, base against landed | §10 `c7a0dff06390` = `c7a0dff06390`; §11, §12 and §13 also identical |
| 10 | `(to-verify)` markers, base / landed | 32 on 24 lines / 32 on 24 lines. The build critic's "33 on 25" is off by one |
| 11 | Boundary-phrase occurrences in landed E (1 means the phrase appears only in its cell) | old: `milking`, `churning`, `dairy chain`, `shearing season`, `dung source`, `herded counterpart` and `riding and pack` are 1 each; `herd ledger` is 0 (removed). New: `can spare` 1, `herd-side cost` 1, `selects a sky reading` 1, `second symbol grammar` 1, `second sky-lore` 1; `what a herd count records` 2; `subsistence input` 2 |
| 12 | Round-50 never-cited candidates in E (`ReviewEntryContract.md` §4) | `ritual-garments`, `music-instrument-lexicon`, `calendar-festival-systems`, `hero-journey-variants`, `source-discipline-calibration`, `coupling-model` and `costume-era-consistency-gate` are 0 each; `writing-media-surface-economy` is 1 (the `sherd` hit) |
| 13 | `grep -c 'trade-economy-lexicon.md:3\b' E` | `0` (grep exit 1): the market owner is still uncited |
| 14 | `numerals-and-measures` in head lines 6–8 | `0` |
| 15 | `git grep` for `routed (debt\|defect)\|debt 2\|defect 2\|row-count leg` in round-51 files | only `claims.json:17`, `round-51.md:17` and `round-51.md:106` |

## Findings

**F1 — medium (calibration, depth). Three of the four new rows are a count move.**
- **Pointers:** E:44, E:45 and E:46.
- **What the rows are:** `ritual-liminality.md:63`, `symbolism-synthesis-method.md:69` and `celestial-symbolism-calendars.md:28`. All three were already in E's head anchor list (E:6) and §10 at base (command 8). §10 is byte-identical to base (command 9).
- **Why it matters:** round 50 recorded "Additional ritual neighbours … remain unexpanded" (`corpus/lessons/round-50.md:126-127`). D converts them into table rows without expanding them. The round-50 inventory (`.ufo/waves/round-50/build/ReviewEntryContract.md` §4) contains only `celestial`, and seven candidates stay at 0 (command 12).
- **The genuine move:** only the numerals row (E:47 plus the §5 sentence at E:93) is a new neighbour relation, 0→2 citations.
- **Smallest fix:** the lesson's Frontier should say that three of the four new rows re-tabulate neighbours §10 already cited, with no new body text.

**F2 — medium (depth; claim statement). One new row's boundary is developed nowhere.**
- **Pointers:** E:45 and E:29.
- **The gap:** row E:45's boundary, "the herd-side cost of each paired taboo and rite (§10)", occurs once (command 11). §10 at E:155 says only "an animal taboo implies a rite … sacrifice belongs to myth-symbol", and §12 pairs a taboo with a rite but gives no cost.
- **Related weakness:** row E:44, "which animals and products the herd can spare (§10)", is developed only by E:155, "surplus males `(to-verify)`". That is a marked, unsourced line.
- **What it contradicts:** D's statement that the new rows are "developed or explicitly narrowed in the entry body". It also contradicts the new lead sentence, "the body section named in the boundary cell develops it".
- **Smallest fix:** either rewrite the E:45 boundary to what §10 says ("the herd side of each taboo–rite pair; no second symbol grammar"), or add one §10 sentence on the herd-side cost.

**F3 — medium (calibration). The new lead sentence states a property that the table does not have.**
- **Pointer:** E:29, "Each row names one neighbour and the line that shows what it owns … and the body section named in the boundary cell develops it".
- **Where it fails:** row E:43 (`civilizations/`) names a directory of six neighbours and gives no line. Eight of the fifteen rows name no body section (command listing of rows without `§`).
- **Why it matters:** this repeats in prose the false "Neighbour (anchor)" header that round 50 flagged (ReviewSec02 F8).
- **Smallest fix:** add "except the `civilizations/` group row, which is carried unanchored", or narrow the sentence to "where a boundary cell names a body section, that section develops it".

**F4 — medium (calibration). The debt's "source" half is dropped.**
- **Pointers:** `round-50-verifier-spotcheck.md:95` against `claims.json:17` and `round-51.md:17`.
- **The narrowing:** debt 2 reads "the commissioned neighbour target **and residual source/content markers**". The claims.json `kind` equates the defect with the count alone ("target 11 of at least 15, not met"). The lesson row retitles it "residual markers" and carries only `(to-verify)`.
- **Residuals not named in round 51:**
  - SOURCES locator errata for S050, S052, S054 and S064 (`round-50.md:109`);
  - S065's teaches-wording correction debt (`round-50.md:121-124`);
  - unregistered leads (FAO `x5439e03.htm`, Goody & Tambiah);
  - no §13 transfer rows (`round-50.md:87`);
  - unopened primary texts: Herskovits 1926, Ostrom 1990, Sherratt 1981 (E §14).
- D cannot repair these this round: `corpus/SOURCES.md` is C's land.
- **Smallest fix:** quote debt 2 in full in the lesson row, and list these source residuals as carried.

**F5 — low (calibration). The carried list is incomplete in two smaller ways.**
- **Header:** the commission's header wording "What it owns (live anchor)" is unmet; E:31 still reads "What it owns".
- **Candidate set:** the round-50 never-cited candidate set (command 12) is not carried.
- **Smallest fix:** add both to `round-51.md:106`.

**F6 — low (provenance). The head does not record D's new anchor.**
- **Pointer:** E:6–10.
- **The gap:** the head anchor list at E:6, which says each anchor was "re-read at `4ad2683`", omits `linguistics/numerals-and-measures.md:101`. The couples line at E:8 omits numerals, celestial and symbolism-synthesis.
- **Smallest fix:** append `linguistics/numerals-and-measures.md:101` to E:6 with "re-read 2026-10-22 at `bff83ba`". This is counter-neutral and leaves topic line 3 and the 227 count untouched.

**F7 — low (calibration). "resolved=15" is not "15 anchored".**
- **Pointer:** `round-51.md:107`.
- **The gap:** `resolved=15` is 14 path:line rows plus one directory row. The Frontier names two counter false positives but not that the directory token counts as resolved.
- **Smallest fix:** add one clause saying so.

## What holds

- **Old cell-only phrases:** all carried, and they stay cell-only, one occurrence each.
- **Market row:** carried accurately (command 13). E:12 and E:212 still route "the market" to §2, which does not hold it.
- **`civilizations/` row:** carried, still unanchored at E:43.
- **`(to-verify)` markers:** carried; 32 remain, unchanged.
- **Shepherd-king contradiction:** genuinely repaired. E:42 now reads "self-presentation, not administration", which matches §10. The anchor `sacred-kingship-mythic-charter.md:65` supports "audited by omens and the gods".
- **Independence from C:** D is independent of C on every test run (commands 3–7).
- **New anchors:** each new row's anchored line carries its owner nouns.
  - `ritual-liminality.md:63`: Vedic agnihotra milk oblation, aśvamedha, "the calendar-owning priesthood's budget".
  - `celestial-symbolism-calendars.md:28`: "pastoralists on milky/river figures".
  - `numerals-and-measures.md:101`: "*head of cattle*".
  - `symbolism-synthesis-method.md:69` supports "An animal taboo implies a rite", but not "the symbol grammar that enforces it". The line is a hunting case. Row-support detail belongs to ReviewDRowSymbolism.

## Unrun checks

- `tools/check-claim-separability.py`, `claims-agree.py` and the round-28 README sweep: not run. They are outside this item.
- No source URL was opened. The item cites no SOURCES row.
