# ScoutRegistry — round-64 wave 1

Axes: coverage (live-URL uniqueness, no SOURCES collision, same-work), operability (row presence and used-by), calibration (ids S718–S749 vs the live register).

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. No tools installed. Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScoutRegistry/`. Counters not edited.

Live URL = first `https?://…` match in the source cell (column 2) of the `ROW:` line, the same `urls[0]` accept-c.py feeds to LINK. Uniqueness is across staged ROW lines, not raw `grep -o` hits inside a file: every mined capture embeds the live URL, so a file-wide count of 2 is the capture contract, not a second row.

## check-rows

Command (lane root):

```
python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
```

Output (exit 1):

```
S718 OK
S719 OK
S720 OK
S721 OK
S722 OK
S723 PROBLEMS MISSING
S724 OK
S725 OK
S726 OK
S727 OK
S728 OK
S729 OK
S730 OK
S731 OK
S732 OK
S733 OK
S734 OK
S735 OK
S736 OK
S737 OK
S738 OK
S739 OK
S740 PROBLEMS MISSING
S741 OK
S742 OK
S743 OK
S744 OK
S745 OK
S746 OK
S747 OK
S748 OK
S749 OK
CHECK-ROWS: 30/32 clean
```

Directories `ScribeRowS723/` and `ScribeRowS740/` are absent. 30 `row.txt` files present (24 mined + 6 disposition). No live URL, used-by, or quote check is possible for S723 or S740.

## (1) Live URLs — exactly once across staged rows, absent from SOURCES

30/30 present rows have one live URL. Each of those 30 strings is a substring of exactly one staged `ROW:` line (its own). No cross-row live-URL collision. `check-rows.py` would have appended `dup_live_url` and did not.

`grep -F -c -e <live-url> corpus/SOURCES.md` for each of the 30 URLs: count 0, exit 1. None are in the register.

Second substring on the same ROW line (not a second row):

- Mined rows: the second hit is the `web.archive.org` capture embedding the live URL. LINK counts registry lines (`hits != 1`), so this matches the frozen leg.
- S744: live URL also in the anchor cell (`wording tested against https://www.dictionary.com/browse/ushanka`). No capture on that row. Still one ROW line.
- S747: live URL also in the teaches cell (`403 https://www.britannica.com/topic/mortarboard`). Still one ROW line.

| id | live URL |
|---|---|
| S718 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/` |
| S719 | `https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content` |
| S720 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/` |
| S721 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/` |
| S722 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/` |
| S724 | `https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/` |
| S725 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/` |
| S726 | `https://eric.ed.gov/?id=ED252065` |
| S727 | `https://www.cambridge.org/core/journals/language-in-society/article/abs/talking-to-children-in-western-samoa/FCDE86B99916AE58E2870E2A65A852F4` |
| S728 | `https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf` |
| S729 | `https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` |
| S730 | `https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf` |
| S731 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/` |
| S732 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/` |
| S733 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/` |
| S734 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/` |
| S735 | `https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf` |
| S736 | `https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full` |
| S737 | `https://eric.ed.gov/?id=ED149852` |
| S738 | `https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf` |
| S739 | `https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf` |
| S741 | `https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en` |
| S742 | `https://files.eric.ed.gov/fulltext/EJ1271032.pdf` |
| S743 | `https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857` |
| S744 | `https://www.dictionary.com/browse/ushanka` |
| S745 | `https://www.merriam-webster.com/dictionary/tiara` |
| S746 | `https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447` |
| S747 | `https://www.britannica.com/topic/mortarboard` |
| S748 | `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html` |
| S749 | `https://en.wikipedia.org/wiki/List_of_headgear` |

`norm_url` in accept-c.py drops the query, so `eric.ed.gov/?id=…` and `plosone/article?id=…` collapse onto other register hosts. That is not the LINK test (LINK is exact substring). Exact `grep -F` is the check that was run. Do not treat those query-stripped overlaps as collisions.

## (2) Ids S718–S749 vs corpus/SOURCES.md

`grep -F -c '| SNNN |'` and `grep -F -w SNNN` for NNN 718–749: count 0, exit 1, every id.

Register table rows: 643, ids S001–S717 with internal gaps, max id S717. `e0151518`, `PMC4794163`, and `journal.pone.0151518` are also absent (`grep -F`, no matches).

## (3) used-by

All 24 present mined rows: used-by is exactly `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` (11 cells, status `mined`).

All 6 disposition rows: used-by is exactly `—` (U+2014). Status observed, not a defect against this check: S744 rejected, S745 rejected, S746 queued, S747 rejected, S748 queued, S749 queued.

## Defects

1. **Missing rows (operability / coverage).** `ScribeRowS723/row.txt` and `ScribeRowS740/row.txt` are not on disk. check-rows: `S723 PROBLEMS MISSING`, `S740 PROBLEMS MISSING`, `30/32 clean`, exit 1. Their live URLs and used-by cells cannot be checked. Inherited from attempt 1; re-verified this run.

2. **Same-work pair, distinct URLs (coverage).** S718 and S729 are not a URL collision and would not fail LINK, and neither string is in SOURCES.md. Both source cells name the same work: Farran et al. 2016, "Cross-Cultural Register Differences in Infant-Directed Speech: An Initial Study", PLOS ONE 11(3), article e0151518. S718 locates PMC4794163; S729 locates `journal.pone.0151518`. Two mined rows for one article. Not in the frozen URL predicate; it still double-counts a work if both are appended.

## Not collisions

- S748 (Rich, "Corona", Smith 1875, LacusCurtius `…/Corona.html`) shares a book-title phrase with S255 (IMAGO, 1890, Perseus) and the LacusCurtius host pattern with S688 (Talaria). Live URL `grep -F` count 0. Different path, different entry.
- S744 / S747 same-line URL repeats (anchor cell / teaches cell) stay on one ROW line.

## Unresolved

- No row text exists for S723 or S740, so no URL or used-by fact for those ids.
- PMC4794163 was not refetched this run. The same-work call rests on both staged citation strings (title, year, journal, e0151518), not on a live PMC page.

Confidence: high on missing files, grep -F URL/id absence, used-by exactness, and the S718/S729 citation overlap. High that no present live URL collides with another staged row or with `corpus/SOURCES.md`.
