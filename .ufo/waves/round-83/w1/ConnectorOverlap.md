# ConnectorOverlap — round 83 w1, cross-axis overlap scan (claims O, D, C)

Read-only seat. Output: `.ufo/waves/round-83/w1/stage/ConnectorOverlap/overlap.md` (the full
scan: 32-row owners table with quotes, 14 one-way couplings, tool adjacency, contradictions,
and the reconciliation with `stage/ScoutGap/owners.md`).
This file is the scoped report; every number below is reproducible from that file's §1-§6.

Bytes read at the frozen base `3088bd7fe2a55a123214abba7008dcddf12b301c` and the frozen config
`21277b089e3c64c247bb4e0fcb033abfdfa1e668`; the lane worktree is at a later HEAD
(`774cc2e3`), which is never graded here.

Authority (R82-M3): `ScribeRows`' fetch receipts bind the `corpus/SOURCES.md` rows,
`ScoutSources` is the independent second reading, and this file is a third reading of
*ownership adjacency only*. `{WAVE}/stage/ScoutGap/owners.md` (the round-83 run) was **absent** at this seat's
first check and landed at 09:26; it is reconciled in the section below and in `overlap.md` §6, so
the wave holds two owners tables that agree on bytes and differ on the word "owns" (see the reconciliation below).

## Axes

- **Adjacency** — can claim D's 257th file be landed without duplicating a neighbour's
  subject, and can O's and C's new tools be landed without a second, contradicting reading of
  a surface another artefact already reads?
- **Coverage** — all eight mandated knowledge files at line level, the 14 row names, and
  every hit of the two tool greps the assignment names.

## Evidence (headline results)

**D — the eight mandated files, all present, all read.** Ten rows of the scan carry **owns**
(a sub-surface with a decision rule, not the institution); the four headline ones are
`linguistics/kinship-terminology.md:80` (`## 5. Affinal
logic: the marriage rule is usually IN the lexicon`) with the contested-alliance calibration at
`:149`; `culture-material/sumptuary-law-rank-display.md:25,64-69,88` (the wives-through-husbands
clause); `culture-material/trade-economy-lexicon.md:125` (`Germanic *mundr* bride-price in
Grágás; Lat. *dōs* → *dowry, dot*` — the corpus's only bride-price citation base);
`linguistics/naming-systems.md:116` (the life-stage name schedule, marriage slot already
reserved). One states the **handoff** in a single sentence:
`culture-material/ritual-garments.md:104` — `Decide who supplies the cloth; cloth-giving is
dowry politics.` `culture-material/funerary-material-culture.md` has **no marriage surface**
(both hits are cross-references into ritual-garments' *mourning* rows), and
`myth-symbol/guest-right-hospitality-law.md` has two (**`:31`** heritable inter-house bond,
**`:99`** what survives the end) but owns the only breach ladder in the corpus (`:35`, `:101`).

**Two rivals the mandated eight do not contain, and they are the real risk.**
`culture-material/pastoralism-animal-husbandry.md:109` already states D's transfer design rule
— `design each transfer by what moves, who gains rights and what it insures` — for the herd
case, and `:113` states the direction (`stock from groom's kin to bride's kin`, `(to-verify)`),
which is a second direction rule beside `kinship-terminology.md:88`'s terminological one.
`culture-material/adornment-body-codes.md:21` already names bridewealth as jewellery capital and
is the corpus's only citation of the comparative baseline (Goody & Tambiah 1973).
Both are cross-partition (culture-material -> D's myth-symbol home), so the coupling direction
must be written or livestock/jewellery bridewealth gets double-owned.

**O — no tool reads the gate table, but a lapsed claim already defined it.**
`git grep -ln 'Gates and probes' <base> -- tools/` = **0**; the only executable base hit is
`reports/round-73/accept-ca.py:144` (`REGISTRY_HEADING_RE = re.compile(r"^##\s+Gates and
probes\s*$")`), which locates the heading to authorize in-place edits and is satisfied as long
as the heading line stays byte-identical. The important find is
`reports/round-70/claims.json:20`: a prior claim O on the *same* surface with the predicate
`registry row count for reports/round-[0-9]+/accept-[a-z]+\.py equals the enumerated
counter-file count (36)`, landed as 36 rows at `SKILL.md:662-697`
(`reports/round-70/corrections-r69.md:15`), with no counter of its own (round-70 holds no
`.py`). Its regex cannot match the round-81/82 naming `accept-c81.py`, so measured on base
bytes it reads **47 rows vs 53 regex-matching counters** — 6 of the real 11 defects — and it
has no DEAD direction. The root cause of the deficit is therefore a naming-convention drift
plus five rounds of maintenance lapse, not a missing predicate.

**C — nothing reads cited records; two tools are adjacent and neither duplicates.**
`counter-revisions` has **0** `tools/` hits. `reports/round-80/accept-o.py:635` grades only its
own round's record and `reports/round-80/counter-revisions.md` (3534 bytes) is the format
precedent the repaired round-82 record should match; the 0-byte round-82 record is cited by
exactly three committed documents (`SCORECARD.md:1663`,
`corpus/lessons/round-82-verifier-spotcheck.md:207-208`, `corpus/lessons/round-82.md:12`).
`tools/check-cited-lines.py` grades S-id clause scoping (QUALITY 15) — a different defect
class; `tools/check-orphan-evidence.py:93` already masks `<placeholder>` shapes into path
scanners (`<scratch>/reports/x.txt` yields nothing), which the new checker's "0 scratch" leg
must reuse or it will flag the sanctioned form. Nothing in `tools/` checks a record file's
bytes. `corpus/QUALITY.md` ends at `30.` (`:207`), so `^31\. ` is free; criterion 30's section
shape is the precedent; but `access date` appears nowhere in QUALITY while criterion 18
(`:57`) already binds a row's source cell to live URL + same-page capture, so 31 must declare
itself an addition to 18.

**O — the 14 names and the order convention.** The frozen arithmetic makes 14 = **11
base-missing + 3 round-83** (`min_instruments_at_lands: 61` = 58 + 3); this scan reproduces
the frozen `base_missing` list byte for byte. All fourteen stems occur **0** times in SKILL.md
today: no collision. The table's only testable convention (round ascending, the single
`kind = note` row last at `:709`) admits them exactly between `:708` and the note row, in round
order; sorting by *name* string inverts rounds 76 and 81-82 and is the failure mode.

## Reconciliation with `stage/ScoutGap/owners.md`

It landed at 09:26, after this seat's first check, so the wave now holds two owners tables.
They **agree on every byte count**: 9 files / 14 lines for the institutional core, 0 filename
owners of 256, the 257th file, myth-symbol 34 -> 35, no dangling `- couples:` target, and the
same strongest partial owners. Two readings need stating, not merging:

1. **"owns" is two definitions, and both are right.** The round-83 artifact's
   `stage/ScoutGap/owners.md:15` states `0 owns, 7 mentions, 3 hands-off across the ten named
   files` with institution-sense "owns"; this scan reports 10 files that own *a sub-surface with
   a decision rule*. The senses are disjoint, not competing, and the entry needs both. The entry needs both: `0 owners` for its absence claim, the 14 couplings for
   its `- couples:` list. Read against each other without this note, one seat looks wrong.
2. **ScoutGap found a line this scan missed.** `pastoralism-animal-husbandry.md:113` carries a
   material direction rule (`stock from groom's kin to bride's kin`, `(to-verify)`); verified at
   base and added. D therefore has **two** direction rules of different kinds
   (`kinship-terminology.md:88` terminological, `:113` material) and must say which governs.

Conversely, `purity-pollution-boundary-systems.md:186` (their third hands-off) names no
marriage surface at base — it is a does-not-own *list shape*, not a surface D must answer. And
the stray "27" now has a **verified** provenance neither seat should quote: it is the round-82
run's hospitality census (`.ufo/waves/round-82/w1/ScoutGap.md`, sha256 `22ff6a2c…`) at base `c285b2af` — `27 lines in 15 files`, against 255 knowledge files and
0 filename hits, reproduced exactly here — copied into D's `before` from a different surface at a
different base; the entry carrying the sentence does not exist at that base.

**Two ScoutGap artifacts, not one (this replaces an earlier single-seat note).** Two runs share
the seat name: the **round-83** run (`.ufo/waves/round-83/w1/ScoutGap.md`, 6,996 B, sha256
`7a15c2b3…`; `stage/ScoutGap/owners.md`, 23,464 B, `64c32143…`) carries the `0 owns / 7 mentions /
3 hands-off` line at `:61` and the `kinship:88` + `pastoralism:113` direction-rule pair at `:68`,
and is the table this report reconciles; the **round-82** run (`.ufo/waves/round-82/w1/ScoutGap.md`,
10,224 B, `22ff6a2c…`, closed 08:15, with `census.sh`, `gap-census.md` and `raw-transcript.txt`
under its stage) has `grep -c '0 owns'` = 0, `grep -c 'pastoralism:113'` = 0, no `owners.md`, and
holds the 27/15/255 hospitality census at `c285b2af`. Both are unchanged; the earlier "contradicts
all three" reading compared one run's message against the other run's files and is withdrawn.
Cite each line by path and sha; nothing in the evidence above changes.

**The duplicate flag is work-level, not row-level.** The round-82 run's "S905 duplicate of S320"
is not a row fact: at `c285b2af` the registry ends at S903 (0 rows for S90[4-7]), and at
`3088bd7f` S905 is Tacitus *Germania* while S320 is Bellows' 1923 *Poetic Edda* (Gutenberg
#73533) — different works. What stands is that the brief's planned Bellows Hávámál row would
reuse the translation already opened as S320; cite it as "planned Bellows Hávámál row vs S320,
work-level, id contingent", and D reuses S904/S905 with no duplicate claim.

**One consequence neither table may repair.** `corpus/README.md:834` is the live footer —
`Total knowledge entries: 253.` with `directory totals 32/32/41/29/24/95` — against base truth
**256** at `32/34/42/29/24/95`; D's landing makes it 257 while the footer still says 253. The
README's convention is that the landing round appends a block (`:791`, `:802`), but D's
`own_paths` are the entry and `corpus/SOURCES.md` only, and O's are the tool and `SKILL.md`.
Route it to the L1; do not let a seat edit a file it does not own.

## Proposed move (one, bounded)

**Derive one registration key from the row's entry-command cell, not from the row's name, and
use that single key for missing, order, and dead.**

Key = `(round, letter)` parsed out of the cell's `reports/round-<N>/accept-<letters>[<N>].py`
token, so `accept-c-76` and `accept-c81.py` collapse onto the same canon. Three axes from one
function:

1. **Missing** becomes glob-independent: a counter matches any row whose command cell names its
   own path, so a future rename cannot lapse the registry the way `[a-z]+` lapsed it in
   round 81.
2. **Order** becomes checkable: the emitted diagnostics can assert ascending `(round, letter)`
   keys and stop before the note row, which makes "round order, notes at the end" a graded
   property instead of a prose convention.
3. **Dead** becomes exact: a row with no parsed key (the note row's cell is `—`) is excluded
   from DEAD by construction, while still counting as a row in `r`.

Harm check: this changes no D or C byte and no frozen constant. It also fixes the frozen
arithmetic exactly — `r` must remain the **row** count (60 + 14 = 74), not the key count
(73 = 61 counters + 12 non-counter rows), or the `r >= base rows + 14` leg fails on a clean
tree. State in the tool's row and docstring that it supersedes round-70's predicate, or the
corpus keeps two definitions of "registry complete".

## Risks

1. **Rename the heading and a frozen counter reds.** `accept-ca-73` requires
   `^## Gates and probes$` exactly; no suffix, no inserted sub-heading.
2. **DEAD on a clean tree.** The note row (`SKILL.md:709`) names no instrument; a naive DEAD
   rule reports it and the `0 dead` after-state is unreachable.
3. **Line shift.** All 14 rows must enter at 709-722, moving every line >= 709 down 14. 9
   distinct real `SKILL.md:<line>` citations at those lines, 133 occurrences, hot at `:713`
   (38) and `:715` (53). Revision-anchored cites (`17e90b9:SKILL.md:715`) survive; bare ones
   (`corpus/lessons/README.md:261`) go stale, and O's `own_paths` do not include that file —
   route the repair, do not absorb it.
4. **D's title word.** "alliance" inherits `kinship-terminology.md:149`'s contested-alliance
   calibration and `:151`'s "superseded". An entry that states alliance theory as an engine
   contradicts a neighbour; the same token also names `lore-shokunin`'s citation-witness
   "alliance" (`r65-alliance-scout.md:1`), a fleet-grep ambiguity to report, not fix.
5. **Two "what transfers through marriage" tables** if D ignores
   `synthesis/contact-scenario-builder.md:112` and a second **breach ladder** if D ignores
   `guest-right-hospitality-law.md:35,101`.
6. **Frozen census vs measured census.** D's `before` says the institutional core is on "9
   files and in 27 whose-word lines"; base gives **9 files / 14 lines** (19 across `corpus/`,
   13 files; 39 with `bride`). No variant tried yields 27 and no D leg grades the sentence, so
   the reproducible 14/9 is the citable figure and "27" should be quoted by no seat.

7. **The index footer is stale and unowned.** `corpus/README.md:834` says 253 against 256 at
   base, and D's 257th file widens the gap; no claim in this round lists the file in
   `own_paths`, so the round lands a file the index under-counts. Route, do not absorb.
8. **Two direction rules, one author to choose.** `kinship-terminology.md:88` (terms) and
   `pastoralism-animal-husbandry.md:113` (stock, `(to-verify)`) say different things about who
   gives; an entry that blends them silently is the R82-M3 failure inside one file.

## Verification (cheap, repo-relative, no network)

1. Row deficit: `git ls-tree -r --name-only <base> reports/ | grep -E '/accept-[^/]*\.py$' |
   wc -l` = 58; diff the stems against the first cells of the `## Gates and probes` table = 11.
2. Round-70 predicate is red and blind: `git show <base>:SKILL.md | grep -cE '^\| [^|]+\|
   (gate|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py'` = 47, against 58 counters (53
   regex-matching) — the 5 `accept-c81.py`-style names are invisible.
3. Novelty: `git grep -c 'GATE-REGISTRY' <base> -- tools/ reports/` = 0 lines; `git grep -ln
   'Gates and probes' <base> -- tools/` = 0 files.
4. Row-name collision: `git show <base>:SKILL.md | grep -c -- 'accept-o-79'` = 0 (and 0 for
   each of the other thirteen stems).
5. Line-shift exposure: `git grep -ohE 'SKILL\.md:[0-9]{2,4}' <base> -- corpus/ reports/ |
   sed 's/SKILL.md://' | sort -n | uniq -c | awk '$2>=709'` — 9 lines, 133 occurrences.
6. D census: `git grep -inE 'bridewealth|bride-price|bride price|dowry|betroth' <base> --
   corpus/knowledge | wc -l` = 14 in 9 files.
7. C shape: `git cat-file -s <base>:reports/round-82/counter-revisions.md` = 0;
   `git show <base>:reports/round-80/counter-revisions.md | wc -c` = 3534 (format precedent);
   `git show <base>:corpus/QUALITY.md | grep -c '^31\. '` = 0 and `grep -c 'access date'` = 0.

8. Index drift: `git show <base>:corpus/README.md | grep -nE '^Total knowledge entries'` ->
   last at `:834` = 253; `git ls-tree -r --name-only <base> corpus/knowledge | grep -c '\.md$'`
   = 256, per-partition `95/42/32/34/29/24`.

Scratch: the seat's own scratch directory was removed on exit; the only artefacts kept are
this report and `.ufo/waves/round-83/w1/stage/ConnectorOverlap/overlap.md`, both repo-relative.
Nothing left behind.

