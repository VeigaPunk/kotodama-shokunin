# FrontierAudit — round 64 wave 2

Seat: `FrontierAudit` (scout). Axes: coverage, operability, calibration.
Lane read-only except this report. No commit, no jj, no index mutation, no README or registry edit. Tools installed: none.

The brief's premise that line 642 is still `mined` is false for the on-disk file. It is true for the git index and for base `ff30a205`.

## 1. S687 flip — not pending on disk

`corpus/SOURCES.md` line 642, `cells()` index 7 (`reports/round-64/accept-c.py:103-104`, status is `cells(r)[7]`).

| surface | status cell | UTF-8 bytes with trailing `\n` | sha256 |
|---|---|---|---|
| base `ff30a205c8d23b35f1ac533740121a955a9fda96:corpus/SOURCES.md` and the git index (`git show :corpus/SOURCES.md`; index line equals base) | `mined` | 532 | `bb4e15b2319538924b2f9c7f42e47fe017459868c465f96802954e8459409f43` |
| worktree file, re-read this turn | `queued` | 533 | `be5e856ba7e14115fa7ef6ef1286fb4509008ccbdebfdb58764301f1966f4393` |

`git diff -U0 -- corpus/SOURCES.md` is one hunk, `@@ -642 +642 @@`. `git status --short -- corpus/SOURCES.md` is ` M` (unstaged). Cell compare of the two full lines: the only difference is cell 7, `mined` → `queued`. Kind, tier, quote, teaches, opened, recheck, and used-by `—` are unchanged. An early grep in this same turn still showed `mined`; a later read showed `queued`. A concurrent writer applied the cell during this audit. This seat did not.

Old line (base and index):

```
| S687 | Hermes Estate & Attributes, Theoi Greek Mythology (author and date not shown) — https://www.theoi.com/Olympios/HermesTreasures.html | docs | C | Theoi's summary of Hermes' winged boots and Greek/Latin terminology |  WINGED BOOTS & CAP OF HERMES section, first sentence: "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria." | Theoi says Hermes wore winged short leather boots, called pteroeis pedila by Greeks and talaria by Romans. | mined | 2026-10-23 | 180d | — |
```

New line (worktree):

```
| S687 | Hermes Estate & Attributes, Theoi Greek Mythology (author and date not shown) — https://www.theoi.com/Olympios/HermesTreasures.html | docs | C | Theoi's summary of Hermes' winged boots and Greek/Latin terminology |  WINGED BOOTS & CAP OF HERMES section, first sentence: "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria." | Theoi says Hermes wore winged short leather boots, called pteroeis pedila by Greeks and talaria by Romans. | queued | 2026-10-23 | 180d | — |
```

L1 integration does not create this flip. `.ufo/waves/round-64/integrate-w2.py` `registry_output` (`:292-315`) copies existing registry lines and appends S718–S749. It never rewrites S687. `reports/round-64/claims.json` still states the flip as part of claim C, and `accept-c.py` APPEND (`:346-356`) passes only if some `| S687 ` row has `cells()[7] == "queued"`. The worktree cell satisfies that check; the index and base do not. If L1 resets `corpus/SOURCES.md` to the index before landing, APPEND fails again. If L1 commits the current worktree line, the flip is kept, because assembly preserves existing lines.

Calibration: `LOG.md:4156` already says the disposition "is `mined -> queued`, enacted in `corpus/SOURCES.md` by this round's claim C land". That sentence matches the unstaged worktree and does not match HEAD or the index.

## 2. readme-row topic vs skeleton `- topic:`

Match: exact, under the assembler's own rule (`integrate-w2.py:222-227`).

- Skeleton: `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md:3`, one `- topic:` line.
- Row: `.ufo/waves/round-64/rows/ScribeEntrySkeleton/readme-row.txt`, one line, 350 bytes including the trailing newline. The directory listing at the start of this turn had only `entry.md`; the row file was present on the later read. This seat did not write it.
- Filename group: `language-socialization-and-acquisition.md`.
- Topic after the em dash equals the skeleton value, 297 characters, `topic_equal True`.

Shared topic string:

```
language socialization and acquisition as culturally organized participation in language across caregiver interaction, early talk, correction, multilingual life, narrative, literacy, and address — a sourced design reference for fictional language practices, not a universal developmental sequence.
```

## 3. Ownership sweep (re-run)

cwd: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Commands are the wave-1 census pair (`.ufo/waves/round-64/w1/ScribeCensus.md` F1) plus a corpus-wide filename check.

```
$ ls corpus/knowledge/linguistics/ | grep -iE 'socializ|acquisit'
filename_grep_exit=1

$ find corpus/knowledge -type f -name '*.md' -print | grep -iE 'socializ|acquisit'
allfile_grep_exit=1

$ grep -rhE '^- topic:.*socializ' corpus/knowledge/*/*.md | wc -l
0

$ grep -ciE 'socializ' corpus/SOURCES.md
0
sources_grep_exit=1

$ test -f corpus/knowledge/linguistics/language-socialization-and-acquisition.md
ABSENT
linguistics md files: 29
corpus/knowledge md files: 237
```

Result: 0 filename owners, 0 topic-line owners of socialization / of this entry's topic. The entry file is not in the corpus.

Caveat, same as the census and still true: three other `- topic:` lines contain the word *acquisition* and are not this topic.

```
$ grep -rlE '^- topic:.*acquisit' corpus/knowledge --include='*.md'
corpus/knowledge/linguistics/language-shift-obsolescence-revival.md
corpus/knowledge/linguistics/sacred-registers-liturgical-language.md
corpus/knowledge/linguistics/gesture-co-speech-pointing.md
```

Those lines are adult acquisition, sacred-register acquisition, and gesture acquisition. None contains `socializ`.

## 4. Known gaps — proposed bullet (not applied)

`corpus/README.md` has no `## Frontier` heading. The frontier surface is `## Known gaps (frontier)` at line 553. The bullet list runs through line 678. `Total knowledge entries: 237.` is line 680. Nothing in that section names `language-socialization-and-acquisition`. The entry file is still absent, so the bullet must not claim a 238-row sweep.

Proposed minimal bullet, to append after line 678 and before the totals line. Not written to the README.

```
- Round 64 adds one linguistics entry, `linguistics/language-socialization-and-acquisition.md` (language socialization and acquisition as culturally organized participation in language). Not yet a corpus file: 0 filename owners and 0 topic-line owners of that topic. Rounds 5–7 residuals above remain open.
```

## Unknowns

- Which concurrent seat wrote the unstaged S687 cell and `readme-row.txt`. Both appeared during this turn; neither was written here.
- Whether L1 commits the worktree `queued` cell or resets `corpus/SOURCES.md` to the index (`mined`). Only the commit path keeps APPEND's S687 requirement. The assembler will not re-apply the cell.
