# GateFinal — round-64 wave-2 Gate fragment (final)

Axes named: **coverage (C)**, **operability (O)**, **calibration (Ca)**.

Seat scope: rebuild the round-64 lesson `## Gate` block from the **final** 32 `row.txt`
files (post-repair snapshot), verify every quote against its own row's `VERIFY`/`TEST`
line, and run the lane's Gate-quote gate on the fragment. **No product code, counter,
registry, entry, lesson file, jj/git state or index was edited.** No commit, no push,
no jj/git write. Scratch only under
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/GateFinal/`.

## Behavior delivered

1. **Fragment rebuilt from the live tree**, not inherited: `build4.py` parses each
   `.ufo/waves/round-64/rows/*/row.txt`, takes the id, the row's live URL (first
   non-archive URL of the source cell), the quoted span of the anchor cell, and the
   row's own evidence line (`VERIFY:` for mined rows, `TEST2:` for disposition rows).
   Output: 32 lines, one per id, no id missing, no id duplicated.
2. **Every quote verified against its row's own evidence line**: a row is rendered as a
   located quote only when its own evidence line literally starts with `LOCATED`; a row
   whose evidence line is `NOT_LOCATED …` or `not applicable` is rendered in the
   annotated not-located form. The builder asserts that each quote is **verbatim in its
   anchor cell** and **≤25 words**; `LINES=32 PROBLEMS=none`.
3. **Every quote independently re-verified against a live fetch** (not against the
   row's claim): 29/29 rows whose evidence asserts `LOCATED` were located by this
   seat's own fetch of the row's URL — **25 in the live body, 4 (S726, S727, S737,
   S740) in the row's own same-page archive capture** because the live host refused
   the request (`http=000`, `http=429`, `http=000`, `http=403` respectively).
   `mismatched=none`.
4. **Fragment passes the lane's own Gate-quote gate**: `python3 -B tools/check-gate-quotes.py`
   on a scratch lesson carrying the fragment → `GATE_QUOTES: 0 findings`, exit 0 — both
   as a bare probe and **beside a copy of the real `corpus/SOURCES.md`** (so the
   tool's `registry_teaches` / `truncated-grounds` path actually runs). A positive
   control (one 30-word row) → `S999 words=30`, exit 1, proving the tool read these rows.
5. **Cross-checked against the landed registry**: `corpus/SOURCES.md` (675 rows, all of
   S718–S749 present) agrees with every `row.txt` on the anchor quote, the live URL and
   the capture's presence → `PROBLEMS=none`.

## The Gate fragment (all 32 ids, verbatim)

```text
- S718 https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/ (opened 2026-10-23): "Lebanese mothers, compared to American mothers, produced more IDS"
- S719 https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content (opened 2026-10-23): "The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats)."
- S720 https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/ (opened 2026-10-23): "only in items deemed to be words or to contain canonical syllables that may have made them sound like words with language-specific shapes"
- S721 https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/ (opened 2026-10-23): "Proto-conversation can be described as a structured, nonlinguistic vocal exchange between infants and their peers or adults"
- S722 https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/ (opened 2026-10-23): "emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning"
- S723 https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html (opened 2026-10-23): "In overextension, children use a simple word to refer to many different things."
- S724 https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/ (opened 2026-10-23): "containing mostly content words like nouns and verbs, with few function words and few inflectional morphemes."
- S725 https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/ (opened 2026-10-23): "typically developing children were more likely to imitate a maternal use of a grammatical morpheme following a corrective recast"
- S726 https://eric.ed.gov/?id=ED252065 (opened 2026-10-23): "the process of acquiring language is deeply affected by the process of becoming a competent member of a society"
- S727 https://www.cambridge.org/core/journals/language-in-society/article/abs/talking-to-children-in-western-samoa/FCDE86B99916AE58E2870E2A65A852F4 (opened 2026-10-23): "organization of turn-taking and procedures for clarification and interpretation are linked to beliefs and expectations"
- S728 https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf (opened 2026-10-23): "Kaluli mothers use elema ‘say it like this’ to prompt the children to correct"
- S729 https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569 (opened 2026-10-23): "Questions, Imperatives, Reading, Singing, Comfort, and Vocal Play were more frequent in the IDS register compared to the ADS register."
- S730 https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf (opened 2026-10-23): "This chapter focuses on the simultaneous acquisition of two languages from birth, or what is generally referred to as bilingual first language acquisition (BFLA)."
- S731 https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/ (opened 2026-10-23): "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching."
- S732 https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/ (opened 2026-10-23): "bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language"
- S733 https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/ (opened 2026-10-23): "High phonological neighborhood density and lexical frequency promoted sign acquisition, even after controlling for iconicity."
- S734 https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/ (opened 2026-10-23): "The results are consistent with the suggestion that children learn general storytelling skills from adult models."
- S735 https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf (opened 2026-10-23): "The teacher, through her questions and comments, tries to help the children structure and focus their discourse."
- S736 https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full (opened 2026-10-23): "created stories with the assistance of their caregivers and siblings"
- S737 https://eric.ed.gov/?id=ED149852 (opened 2026-10-23): "A sample was considered an example of verbal play if it incorporated an observable manipulation of the sound, semantics and/or syntax of the language."
- S738 https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf (opened 2026-10-23): "in relation to experts’ advice, as they were explicitly instructed not to introduce the language immediately after meeting the children"
- S739 https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf (opened 2026-10-23): "Based on the data obtained, urban parents in Sleman, Yogyakarta used various forms of address when interacting with their children."
- S740 https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early (capture https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early) (opened 2026-10-23): "These overgeneralizations suggest that children are not just memorizing the forms in their input, but also generating novel forms from a rule."
- S741 https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en (opened 2026-10-23): "We know it’s ugly because people tell us it’s ugly."
- S742 https://files.eric.ed.gov/fulltext/EJ1271032.pdf (opened 2026-10-23): "Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other."
- S743 https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 (opened 2026-10-23): "Since this construction has a register specification as “child-directed,”"
- S744 https://www.dictionary.com/browse/ushanka (opened 2026-10-23): NOT LOCATED — re-test `TEST: 200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling`; `TEST2: NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent` — candidate wording (not verified): "a traditional Russian fur cap with earflaps that can be tied up on top"
- S745 https://www.merriam-webster.com/dictionary/tiara (opened 2026-10-23): NOT LOCATED — re-test `TEST: 403 https://www.merriam-webster.com/dictionary/tiara`; `TEST2: NOT_LOCATED https://www.merriam-webster.com/dictionary/tiara HTTPError` — candidate wording (not verified): "a decorative jeweled or flowered headband or semicircle for formal wear"
- S746 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 (opened 2026-10-23): "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters"
- S747 https://www.britannica.com/topic/mortarboard (opened 2026-10-23): NOT LOCATED — re-test `TEST: 403 https://www.britannica.com/topic/mortarboard`; `TEST2: not applicable` — the row anchor cell records no locatable wording
- S748 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html (opened 2026-10-23): "Among the honorary crowns bestowed by the Romans for military achievements"
- S749 https://en.wikipedia.org/wiki/List_of_headgear (opened 2026-10-23): "Headgear is worn for many purposes, including protection against the elements, decoration, or for religious or cultural reasons, including social conventions."
```

The block above is the verbatim content of
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/GateFinal/gate_fragment.md`
(md5 `46aef85ef58287899d43d358d038b906`), the artifact the Gate-quote gate was run
against. The paste was re-verified against that file line-for-line after writing
(see "Paste verification" below); the L1 may copy from either.

### The disposition-evidence appendix (same fragment + the six disposition rows' re-test output)

`accept-c.py`'s REJECTS leg requires the disposition rows' ordinary re-open/status
evidence to be recorded **in the round-64 lesson Gate**. The same fragment with that
evidence appended (`gate_fragment_with_evidence.md`, md5
`c020019a4c4e55458e2a53c7110d5470`) also passes the Gate-quote gate with 0 findings,
because the appendix lines do not begin with `- S###` and are therefore not read as
Gate rows:

```text
Disposition re-open evidence for the six disposition rows (verbatim from each row's own TEST / TEST2 lines):

S744 (rejected) re-open evidence — TEST: 200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling ; TEST2: NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent
S745 (rejected) re-open evidence — TEST: 403 https://www.merriam-webster.com/dictionary/tiara ; TEST2: NOT_LOCATED https://www.merriam-webster.com/dictionary/tiara HTTPError
S746 (queued) re-open evidence — TEST: 200 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 ; TEST2: LOCATED https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447
S747 (rejected) re-open evidence — TEST: 403 https://www.britannica.com/topic/mortarboard ; TEST2: not applicable
S748 (queued) re-open evidence — TEST: 200 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html ; TEST2: LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html
S749 (queued) re-open evidence — TEST: 200 https://en.wikipedia.org/wiki/List_of_headgear ; TEST2: LOCATED https://en.wikipedia.org/wiki/List_of_headgear
```

## Gates run and outcomes (observed, not asserted)

```text
$ python3 -B tools/check-gate-quotes.py <scratch>/lesson_probe.md      # bare probe
GATE_QUOTES: 0 findings
exit=0

$ python3 -B tools/check-gate-quotes.py <scratch>/probe_tree/corpus/lessons/round-64-probe.md
                                                                        # beside a copy of the real corpus/SOURCES.md
GATE_QUOTES: 0 findings
exit=0

$ python3 -B tools/check-gate-quotes.py <scratch>/probe_bad.md        # positive control
<scratch>/probe_bad.md:37 S999 words=30
GATE_QUOTES: 1 findings
exit=1        # the tool was live and read these rows
```

Same two runs on `gate_fragment_with_evidence.md`: `GATE_QUOTES: 0 findings`, exit 0
(bare probe and beside `SOURCES.md`).

```text
$ python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
… S749 OK
CHECK-ROWS: 32/32 clean
```

Builder self-check (every quote verbatim in its anchor cell, ≤25 words, one line per id):

```text
$ python3 -B build4.py
LINES=32 PROBLEMS=none
```

Registry cross-check (`corpus/SOURCES.md`, 675 rows, all of S718–S749 present):

```text
$ python3 -B crosscheck_registry.py
registry_rows_total=675
S718 registry_status=mined tier=A opened=2026-10-23 recheck=180d quote_words=9 live=https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/ capture=yes
… (32 rows) …
PROBLEMS=none
```

Independent live re-verification of every quote (this seat's own fetch, not the row's
claim; live body first, then the row's own same-page capture):

```text
S718 mined live=200 live body            S732 mined live=200 live body
S719 mined live=200 live body            S733 mined live=200 live body
S720 mined live=200 live body            S734 mined live=200 live body
S721 mined live=200 live body            S735 mined live=200 live body
S722 mined live=200 live body            S736 mined live=200 live body
S723 mined live=200 live body            S737 mined live=000 row's same-page archive capture
S724 mined live=200 live body            S738 mined live=200 live body
S725 mined live=200 live body            S739 mined live=200 live body
S726 mined live=000 row's same-page archive capture
                                          S740 mined live=403 row's same-page archive capture
S727 mined live=429 row's same-page archive capture
                                          S741 mined live=200 live body
S728 mined live=200 live body            S742 mined live=200 live body
S729 mined live=200 live body            S743 mined live=200 live body
S730 mined live=200 live body            S744 rejected  NOT LOCATED (row evidence NOT_LOCATED)
S731 mined live=200 live body            S745 rejected  NOT LOCATED (row evidence NOT_LOCATED)
                                          S746 queued   live=200 live body
                                          S747 rejected  NOT LOCATED (row evidence: not applicable)
                                          S748 queued   live=200 live body
                                          S749 queued   live=200 live body (tag-stripped visible text)
SUMMARY row_asserts_located=29 independently_located=29 mismatched=none
```

Split of the 29 (counted from the table above, not asserted):
**25 located in the live body** — S718–S725, S728–S736, S738, S739, S741–S743, S746,
S748, S749 — **4 located in the row's own same-page capture** — S726 (`http=000`),
S727 (`http=429`), S737 (`http=000`), S740 (`http=403`).

Dispositions independently reproduced (the three not-located rows):

```text
https://www.dictionary.com/browse/ushanka      http=200 bytes=65418 effective=https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling   quote absent
https://www.merriam-webster.com/dictionary/tiara  http=403 bytes=5600 effective=unchanged   quote absent
https://www.britannica.com/topic/mortarboard   http=403 bytes=5555 effective=unchanged   quote absent
```

## Defects named

**GF-1 — two divergences between this report's paste and the artifact file were caught by
a machine check and fixed before the report was finalised; the paste is now
byte-identical to `gate_fragment.md`.** The check (`verify_paste.py`) compares the
report's fenced Gate block against the artifact file line-for-line. It reported: (a) the
S746 and S749 lines transposed in the paste, and (b) the three not-located lines missing
the `TEST:` / `TEST2:` labels the artifact carried in its backticks. (a) was a paste
error and was corrected in the report; (b) was an artifact defect — the labels name
which re-test line is which, so the **artifact was rebuilt to carry them** and the gate
was re-run against the rebuilt file (still `GATE_QUOTES: 0 findings`, exit 0). The
artifact was never wrong about a quote, a URL, or a disposition; only the three
not-located lines' inline labelling changed, and the file's md5 moved with it
(`46aef85ef58287899d43d358d038b906`). Receipt below.

**GF-2 — S747 has no quote at all in the repaired row, so the wave-1 fragment's S747
quote must not be restored.** The repaired row's anchor cell reads
`Britannica Mortarboard entry, article lead (intended locator); live fetch 403
(Cloudflare challenge) on 2026-10-23; wording not locatable` — no quoted span at all.
The wave-1 fragment (`.ufo/waves/round-64/w1/ScribeGateQuotes.md`) quoted
`"Britannica's Mortarboard page as evidence for mortarboard use in academic dress"`,
which is the row's own description, not a page quote. The final fragment therefore
renders S747 with its re-test output and **no quoted candidate**, and does not restore
the wave-1 string. The `LessonFinal` seat confirmed this reading in writing.

**GF-3 — S740's live URL does not serve its quote; the row's `VERIFY` names the capture.**
`https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early`
answers **HTTP 403** (5,787-byte Cloudflare challenge) to a plain client; the row's own
`VERIFY:` line names the same-page capture
`https://web.archive.org/web/20210414114152id_/…`, which serves it (HTTP 200, 243,294
bytes; quote present — confirmed by this seat's own fetch of the capture). Following the
`LessonFinal` seat's written answer (round-62's parenthetical shape), the fragment keeps
the **live URL first** in the URL field and carries the capture in parentheses, so the
registry/row identity stays checkable while the reachable locator is visible. The wave-1
fragment carried the live URL with no capture, i.e. a URL that does not serve its quote.

**GF-4 — S735's quote is present in the PDF but `pdftotext` does not extract it;
`pypdf 5.4.0` (the locator's canonical extractor) does.** Same class as wave-1's D5.
Recorded so a later verifier using `pdftotext` alone does not read absence. Measured:
`pdftotext` → not found; `uv run --with pypdf==5.4.0` → located (21 pages, live PDF and
capture both).

**GF-5 — S749's quote is in the page's visible text, not in its raw HTML.** The live
Wikipedia body contains the sentence as `<a …>Headgear</a> is worn for many purposes, …`;
a raw-HTML substring match fails, a tag-stripped visible-text match succeeds. The row's
`TEST2: LOCATED` is correct. Recorded so a later verifier does not read a raw-HTML miss
as a quote defect.

**GF-6 — four rows need their capture, not their live URL, at re-verification time**
(S726 ERIC `http=000`, S737 ERIC `http=000`, S740 UC Press `http=403`, S727 Cambridge
`http=429`). All four quotes locate in the rows' own same-page captures. This is an
availability fact about the hosts, not a quote defect, and it is the same PMC/ERIC/Wayback
intermittency wave-1's D4 recorded.

**GF-7 — the wave-1 fragment and the final fragment differ on nine lines; the final one
supersedes.** Machine diff (`diff_w1_w2.py`): 32 rows each, 9 changed —
**S729** (re-sourced: the wave-1 line pointed at Farran et al. `journal.pone.0151518`
with the quote *"with the Lebanese mothers using more IDS Utterances per Minute…"*; the
final row is Neer et al. 2025 `journal.pone.0326569` with a different quote, and the
landed registry agrees with the new row),
**S739** (quote changed to the row's current anchor, *"Based on the data obtained, urban
parents in Sleman, Yogyakarta…"*),
**S740** (capture added per GF-3),
**S744/S745/S747** (wave-1 rendered them as located quotes; final renders them as the
annotated not-located form),
**S746/S748/S749** (queued candidates; the final fragment's located lines are identical
to wave-1's, with the re-open evidence carried in the appendix rather than inline).
Any sibling report still quoting wave-1's S729/S739 lines is a dated snapshot.

**GF-8 — the rows tree was still moving while this seat ran.** At 23:52 the snapshot had
32 rows; between then and 00:00 five files changed (S721, S723, S726, S729, S735, S737,
S740 — seven by the last census) through concurrent repair seats
(`FixRowS722`, `FixRowS719`, `FixRowS735`, `FixRowS739`, `FixRowsS728S742`,
`FixRowS747`, `ReSourceS729`). The final fragment was rebuilt from the live tree after
those landings; a field-level diff (`diff_quote_url.py`) confirms that the
**(live URL, capture, anchor quote)** of every one of the 32 rows is unchanged between
the 23:54 snapshot and the final build, so the fragment is stable against those
edits — the edits touched tier / teaches / grounds / locator cells, not the quote or URL.
The last census (`/tmp/rows_final.md5`, md5 of the sorted per-file md5 list:
`9518ab880e63d23c5711937de76208ec`) is the state the fragment was built from.

**GF-9 — the lane's Gate-quote checker reads EVERY `- S<digits>` line inside the
`## Gate` section as a Gate row, so note bullets in that section are attributed to real
ids.** Found by independently cross-checking the `LessonFinal` seat's near-final lesson
(`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/LessonFinal/round-64.md`) against the final
rows. That lesson's Gate section holds the 32 pipe-shaped Gate rows **plus** note bullets
that also begin `- S<digits>`: six `S74x … re-open evidence` bullets and four prose
bullets (`- S744, S745, S747 — …`, `- S726 — …`, `- S729 — …`,
`- S719, S722, S728, S735, S739, S742 — …`). Measured on the lesson as written:

```text
lesson as written                          logical_rows=42 distinct_ids=32 duplicated={'S719': 2, 'S726': 2, 'S729': 2, 'S744': 3, 'S745': 2, 'S746': 2, 'S747': 2, 'S748': 2, 'S749': 2}
```

Today this is harmless — every note bullet carries **zero** quoted spans, so the cap
check has nothing to count and the file reports `GATE_QUOTES: 0 findings`, exit 0. It is
a latent trap: injecting a 30-word quoted span into each note bullet in turn makes the
checker attribute the finding to the real id at the **note bullet's** line —
`S719 words=30 over-cap`, `S726 words=30 over-cap`, `S744 words=30 over-cap`, … — even
though each id's real Gate row is within cap (S719 is 23 words). A later editorial change
to any note bullet inside the Gate section can therefore produce a cap finding attributed
to the wrong row, or mask a real one.

Minimal fix, **verified on a scratch copy of the lesson only** (not the lesson, not the
lane): drop the leading `- ` from the six re-open-evidence bullets, and re-prefix the four
id-mentioning note bullets with a non-`- S<digits>` token (e.g. `Note: S719, S722, …`).

```text
lesson with both fixes                     logical_rows=32 distinct_ids=32 duplicated={}
GATE_QUOTES: 0 findings   exit=0            (after both fixes)
```

The scratch copies are `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/GateFinal/lesson_patched.md`
(one fix) and `lesson_patched2.md` (both fixes). The finding was sent to the
`LessonFinal` seat, which owns the lesson file; **this seat did not edit it.** Note for
the record: this seat's own appendix in `gate_fragment_with_evidence.md` is already shaped
so its lines do not start with `- S###`, which is why this seat's fragment shows 32
logical rows, not 42.

**GF-9 — closed.** The `LessonFinal` seat applied both edits to its near-final lesson
(six re-open-evidence bullets de-bulleted; four id-mentioning note bullets re-prefixed
`Note: …`). This seat then re-verified the amended file independently, re-reading it
from disk rather than accepting the seat's report:

```text
lesson sha256: 5b42f334194aab6c5e0d18dc31b46e349e7db52cd7a97c7c7dc971bb12d6682a
lesson bytes: 46435
logical_rows=32 distinct_ids=32 duplicated=none
all ids in S718-S749: True

$ python3 -B crosscheck_lesson.py
… 32 ids: quote ok / url ok …
S747 no-quote-row (NOT LOCATED line expected) / url ok words=None
--- note bullets inside the Gate section that the lane checker also reads as Gate rows ---
(none)
--- lane gate on the lesson file ---
GATE_QUOTES: 0 findings
gate_exit=0
PROBLEMS=none
```

Spot-checks on the amended file: all six `S74x … re-open evidence` lines survive with
their `TEST`/`TEST2` output intact; S740 still carries its capture parenthetical; S744,
S745 and S747 still carry their `NOT LOCATED` annotations, with S747 still asserting no
quotation. The hazard is closed on the file that will be committed.

**GF-10 — my own live/capture split was mis-stated as "26 in the live body, 3 in the
capture", and the error propagated into the `LessonFinal` seat's lesson note.** The
correct split, re-counted from the per-row evidence (not typed): **25 in the live body,
4 in the row's own same-page capture** — S726 (`http=000`), S727 (`http=429`), S737
(`http=000`), S740 (`http=403`) — summing to the 29 rows whose evidence asserts
`LOCATED`. The defect was that S727 was served by its capture (its live attempt answered
`429`) but was excluded from the capture group in the prose summary, so the sentence
read as 26+3+1 = 30 rows for 29. The origin was an earlier run of the fetch script,
which stopped at the live body and listed the capture-served rows separately; the later
run, which falls back to the row's own capture, is the authoritative one. **The
per-row evidence table in this report was always correct** — it shows S727 served by its
capture — so the table and the prose disagreed and the prose was wrong. This seat's
report and the lesson note were both corrected; the correction was sent to the
`LessonFinal` seat with the exact replacement clause. The underlying result is
unaffected: 29/29 located, `mismatched=none`.

**GF-10 — closed.** The `LessonFinal` seat applied the correction to both the lesson's
Gate note and the matching paragraph of its own report (F5b), and this seat re-verified
the amended lesson independently, re-reading it from disk rather than accepting the
seat's report:

```text
sha256: 377f728ec28eae017724a4fa54068c5e2cff3ed89f549f1e3e49bbd6269d5713 bytes: 47245
logical_rows=32 distinct_ids=32 duplicated=none ids_exact=True

Note: live re-verification of the 29 rows whose evidence asserts `LOCATED` was
  carried out independently in wave 2: **29/29 located, `mismatched=none`** —
  25 in the live body, and 4 (S726, S727, S737, S740) in the row's own
  same-page archive capture because the live host refused the request
  (`http=000`, `http=429`, `http=000`, `http=403` respectively)

$ python3 -B crosscheck_lesson.py
… 32 ids: quote ok / url ok …
S747 no-quote-row (NOT LOCATED line expected) / url ok words=None
--- note bullets inside the Gate section that the lane checker also reads as Gate rows ---
(none)
--- lane gate on the lesson file ---
GATE_QUOTES: 0 findings
gate_exit=0
PROBLEMS=none
```

The corrected clause sums to the 29 rows whose evidence asserts `LOCATED`, and the
`## Gate` section still yields 32 logical rows for 32 distinct ids — GF-9 stays closed,
because the correction sits inside the `Note: live re-verification…` bullet rather than a
`- S<digits>` line.

## Cross-check of the LessonFinal seat's near-final lesson (read-only)

```text
$ python3 -B crosscheck_lesson.py
lesson Gate ROW lines found: 32 / 32
S718 quote ok / url ok words=9
… (32 ids) …
S747 no-quote-row (NOT LOCATED line expected) / url ok words=None
--- lane gate on the lesson file ---
GATE_QUOTES: 0 findings
gate_exit=0
PROBLEMS=none
```

Every one of the 32 Gate rows in the lesson carries the row's own anchor quote and the
row's own live URL; S747 carries no quote, as its row requires. The lane's structural
battery was also run against the current lane tree: `tools/check-gate-battery.py` →
`battery_exit 0, pass 7, fail 0, unevaluable 0`.

## Touched surfaces

- **Written by this seat (lane repo):** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w2/GateFinal.md` — this report, and nothing else. No row file, no registry, no entry, no lesson, no counter, no tool, no jj/git state or index.
- **Scratch only:** `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/GateFinal/` — `build.py`, `build2.py`, `build3.py`, `build4.py`, `build_minimal.py`, `live_parallel.py`, `live_reverify.py`, `final_verify.py`, `crosscheck_registry.py`, `crosscheck_lesson.py`, `compare_snap.py`, `diff_quote_url.py`, `diff_w1_w2.py`, `verify_paste.py`, `gate_fragment.md` (md5 `46aef85ef58287899d43d358d038b906`), `gate_fragment_with_evidence.md` (md5 `c020019a4c4e55458e2a53c7110d5470`), `gate_fragment_minimal.md`, `lesson_probe.md`, `probe_bad.md`, `probe_tree/`, `snap3/`, `bodies/`, `cap/`, `lesson_patched.md`, `lesson_patched2.md`, `final_verification.json`, `live_reverify.json`, `fields.txt`, `rows_report.txt`, `notes.txt`.
- **Read only:** `.ufo/waves/round-64/rows/*/row.txt`, `.ufo/waves/round-64/check-rows.py`, `.ufo/waves/round-64/w1/ScribeGateQuotes.md`, `.ufo/waves/round-64/w2/*.md`, `corpus/SOURCES.md`, `corpus/lessons/README.md`, `corpus/lessons/round-62.md`, `corpus/lessons/round-63.md`, `reports/round-64/accept-c.py`, `reports/round-64/accept-ca.py`, `tools/check-gate-quotes.py`, `tools/check-gate-battery.py`, and the `LessonFinal` seat's scratch lesson `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/LessonFinal/round-64.md` (read only; never written by this seat).

## Out of scope / not done

- **The lesson file `corpus/lessons/round-64.md` was not created or edited.** The fragment is handed to the `LessonFinal` seat (message sent with the answers it asked for) and to the L1; the commit shape is the L1's.
- **No counter was edited or run as an acceptance gate.** `accept-c.py` / `accept-o.py` / `accept-ca.py` were not executed. The fragment is **not** an `ACCEPT-C-64` pass and nothing here should be read as one.
- **Bullet quality (RESTATE / caveat fidelity), entry lines, and the counter's own legs were not judged here** — those belong to `CriticRowsFinal`, `CriticEntrySweep`, `CriticRevC`, `RevVerifyC` and the L1.
- **The S740 live-host 403, the ERIC 000s and the Cambridge 429 were characterised, not fixed**; no mitigation was applied to a tool or a counter.
- **Registry/entry reconciliation** (S729's re-source reaching `corpus/SOURCES.md`) was *observed* as already consistent (`PROBLEMS=none`), not performed by this seat.

## Tooling

No tool was installed or updated by this seat — everything used was already present:
system `curl`, `python3` 3.x, `pdftotext` (poppler), and `uv` (used only to run the
locator's own pinned `pypdf==5.4.0` extractor, the same invocation
`reports/round-61/reopen-quote.py` makes). `pacman` was not touched (host-wide pacman
transactions are paused). No `uv tool install`, no `cargo`, no `npm -g`.

## Axis effect

- **Coverage — improved.** The Gate block is complete at 32/32 ids, rebuilt from the
  final post-repair rows, every quote ≤25 words (max 24), and the block passes the
  lane's own Gate-quote gate with 0 findings both bare and beside the real
  `corpus/SOURCES.md`.
- **Calibration — improved.** Three disposition rows are rendered as annotated
  **NOT LOCATED** rather than as located quotes; S747 no longer carries a description
  string dressed as a page quote; S740's URL field names the source and also names the
  capture that actually serves the quote; the six disposition rows' verbatim re-open
  evidence is carried for `accept-c.py`'s REJECTS leg. Every located quote was
  independently re-verified against a live fetch — 29/29, `mismatched=none`.
- **Operability — not harmed, nothing touched.** No counter byte, tool byte, registry
  byte, lesson byte or lane state was modified; the fragment is verified against the
  lane's existing gate, which passes it.

## Paste verification

```text
$ python3 -B verify_paste.py
Gate block in report == gate_fragment.md : YES
Disposition evidence block in report == appendix : YES
gate_fragment.md md5=46aef85ef58287899d43d358d038b906
gate_fragment_with_evidence.md md5=c020019a4c4e55458e2a53c7110d5470
PASTE_VERIFICATION=PASS
exit=0
```

## Hand-off to the L1

1. Take the `## Gate` block from `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/GateFinal/gate_fragment.md`
   (md5 `46aef85ef58287899d43d358d038b906`) — the paste in this report is now verified
   byte-identical to it (GF-1), so either source is safe; the file is the one the gate
   was run against.
2. Append the disposition-evidence appendix (`gate_fragment_with_evidence.md`, same 32
   lines plus the six `TEST`/`TEST2` lines) so `accept-c.py`'s REJECTS leg finds the
   ordinary re-open/status evidence inside the lesson's Gate section; both variants pass
   the Gate-quote gate with 0 findings.
3. Verify after the commit with `python3 -B tools/check-gate-quotes.py corpus/lessons/round-64.md`
   (expect `GATE_QUOTES: 0 findings`, exit 0).
4. Note GF-2/GF-3 in the lesson's own mistake record: a description string is not a
   quote, and a URL that 403s is not a locator.
5. GF-9 is already closed on the lesson the `LessonFinal` seat will hand over: any line
   inside `## Gate` that begins `- S<digits>` is read by the lane's Gate-quote checker
   as a Gate row for that id, so the lesson's note bullets must not begin that way. The
   seat applied the fix and this seat re-verified the amended file independently —
   32 logical rows, 32 distinct ids, no duplicated id, `GATE_QUOTES: 0 findings`, exit 0.
   Confirm it still holds after any further edit to the Gate section.

Report: `.ufo/waves/round-64/w2/GateFinal.md`
