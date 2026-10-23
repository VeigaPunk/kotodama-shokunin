# ScribeGateQuotes — round 64 wave 1 (lesson Gate fragment)

Axes named: **coverage (C)**, **operability (O)**, **calibration (Ca)**.

Seat scope: build the round-64 lesson Gate fragment from `.ufo/waves/round-64/rows/*/row.txt`
(S718–S749), verify every quote against its row's `VERIFY`/`ROW` content, and name every
defect. **No product code, counter, registry, entry, lesson file, jj/git state or index was
edited.** No commit, no push. Scratch only under
`/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeGateQuotes/`.

## Behavior delivered

1. **Fragment built** from the 32 staged `row.txt` contributions (26 mined S718–S743 + 6
   disposition S744–S749). One line per id in the mandated format, quotes trimmed to ≤25
   words without altering word order.
2. **Every quote verified against its row's own content**: the quoted span is present
   verbatim in that row's `ROW` line (anchor cell), and the row's `VERIFY`/`TEST2` evidence
   line was read for each id.
3. **Live re-verification** of the located claims: independent `curl --compressed` fetches of
   the live URL and of the row's own archive capture, with the lane locator
   `reports/round-61/reopen-quote.py` run in `--row` mode against a scratch registry copy
   (same bytes the counter's `LIVE` leg resolves).
4. **Fragment passes the lane's own Gate-quote gate**: `tools/check-gate-quotes.py` on a
   scratch lesson containing the fragment → `GATE_QUOTES: 0 findings`, exit 0; a positive
   control (one 30-word row) → `S999 words=30`, exit 1, proving the tool was live and read
   these rows.

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
- S729 https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518 (opened 2026-10-23): "with the Lebanese mothers using more IDS Utterances per Minute across both Registers than the American mothers"
- S730 https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf (opened 2026-10-23): "This chapter focuses on the simultaneous acquisition of two languages from birth, or what is generally referred to as bilingual first language acquisition (BFLA)."
- S731 https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/ (opened 2026-10-23): "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching."
- S732 https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/ (opened 2026-10-23): "bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language"
- S733 https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/ (opened 2026-10-23): "High phonological neighborhood density and lexical frequency promoted sign acquisition, even after controlling for iconicity."
- S734 https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/ (opened 2026-10-23): "The results are consistent with the suggestion that children learn general storytelling skills from adult models."
- S735 https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf (opened 2026-10-23): "The teacher, through her questions and comments, tries to help the children structure and focus their discourse."
- S736 https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full (opened 2026-10-23): "created stories with the assistance of their caregivers and siblings"
- S737 https://eric.ed.gov/?id=ED149852 (opened 2026-10-23): "A sample was considered an example of verbal play if it incorporated an observable manipulation of the sound, semantics and/or syntax of the language."
- S738 https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf (opened 2026-10-23): "in relation to experts’ advice, as they were explicitly instructed not to introduce the language immediately after meeting the children"
- S739 https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf (opened 2026-10-23): "Parents can use various terms of address to children depending on situational contexts."
- S740 https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early (opened 2026-10-23): "These overgeneralizations suggest that children are not just memorizing the forms in their input, but also generating novel forms from a rule."
- S741 https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en (opened 2026-10-23): "We know it’s ugly because people tell us it’s ugly."
- S742 https://files.eric.ed.gov/fulltext/EJ1271032.pdf (opened 2026-10-23): "Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other."
- S743 https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 (opened 2026-10-23): "Since this construction has a register specification as “child-directed,”"
- S744 https://www.dictionary.com/browse/ushanka (opened 2026-10-23): "a traditional Russian fur cap with earflaps that can be tied up on top"
- S745 https://www.merriam-webster.com/dictionary/tiara (opened 2026-10-23): "a decorative jeweled or flowered headband or semicircle for formal wear"
- S746 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 (opened 2026-10-23): "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters"
- S747 https://www.britannica.com/topic/mortarboard (opened 2026-10-23): "Britannica’s Mortarboard page as evidence for mortarboard use in academic dress"
- S748 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html (opened 2026-10-23): "Among the honorary crowns bestowed by the Romans for military achievements"
- S749 https://en.wikipedia.org/wiki/List_of_headgear (opened 2026-10-23): "Headgear is worn for many purposes, including protection against the elements, decoration, or for religious or cultural reasons, including social conventions."
```

Scratch copy: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeGateQuotes/gate_fragment.md`
(plus `records.json`, `defects.txt`, `build_fragment.py`, `crosscheck.py`, `locate_out.txt`,
`capture_out.txt`, `lesson_probe.md` in the same directory).

**Word cap:** longest quoted span in the fragment is **24 whitespace words** (S737, S719);
nothing needed trimming. `tools/check-gate-quotes.py` (the lane's 25-word Gate cap) reports
`GATE_QUOTES: 0 findings` on this fragment, exit 0; positive control with one 30-word row
reports `S999 words=30`, exit 1.

## Gates run and outcomes (observed, not asserted)

```text
$ python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
… S743 OK
S744 OK
S745 OK
S746 OK
S747 OK
S748 OK
S749 OK
CHECK-ROWS: 32/32 clean
```

```text
$ python3 -B tools/check-gate-quotes.py /home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeGateQuotes/lesson_probe.md
GATE_QUOTES: 0 findings
exit=0
```

```text
$ python3 -B tools/check-gate-quotes.py /home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeGateQuotes/probe_bad.md
probe_bad.md:39 S999 words=30
GATE_QUOTES: 1 findings
exit=1        # positive control: the tool read these rows
```

Locator, `--row` mode against a scratch `corpus/SOURCES.md` built from the 32 staged `ROW:`
lines (same bytes the counter's `LIVE` leg resolves):

```text
=== S723 LOCATED https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html
=== S728 LOCATED https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf
=== S738 LOCATED https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf
=== S743 LOCATED https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857
=== S740 LOCATED https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early
=== S718 LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/     (after a cooldown)
=== S733 NOT_LOCATED … quote-absent; … HTTPError                        (intermittent, see D4)
```

Independent `curl --compressed` fetch of each row's **live** URL and of its **own archive
capture**, with the row's own anchor quote matched under the locator's normalisation
(NFKC, casefold, `\W_`→space):

```text
S718 live 200 located=True     S718 cap_id_ 200 located=True
S720 live 200 located=True     S720 cap_id_ 200 located=True
S721 live 200 located=True     S721 cap_id_ 200 located=True
S722 live 200 located=True     S722 cap_id_ 200 located=True
S725 live 200 located=True     S725 cap_id_ 200 located=True
S727 live 429 located=False    S727 cap_id_ 200 located=True
S731 live 200 located=True     S731 cap_id_ 200 located=True
S732 live 200 located=True     S732 cap_id_ 200 located=True
S733 live 200 located=True     S733 cap_id_ 200 located=True
S734 live 200 located=True     S734 cap_id_ 200 located=True
S719 live 200 located=False    (PDF: pdftotext extraction → quote present in the PDF; locator LOCATED)
S726 live 200 located=True     S723 live 200 located=True
S724 live 200 located=True     S728 live 200 located=True  (pdftotext → located=True)
S729 live 200 located=True     S730 live 200 located=True  (pdftotext → located=True)
S735 live 200 located=False    (pdftotext False; pypdf 5.4.0 → located=True; locator LOCATED)
S736 live 200 located=True     S737 live 200 located=True
S738 live 200 located=True     S739 live 200 located=True  (pdftotext → located=True)
S740 live 403 located=False    S741 live 200 located=True
S742 live 200 located=True     S743 live 200 located=True  (pdftotext → located=True)
```

Disposition rows, independent fetch of the cited URL:

```text
S744 http=200 bytes=65407 located=False   (server rewrite to /browse/khanka?q=ushanka…)
S745 http=403 bytes=5601  located=False   (Cloudflare challenge)
S746 http=200 bytes=61181 located=True
S747 http=403 bytes=5556  located=False   (Cloudflare challenge)
S748 http=200 bytes=65206 located=True
S749 http=200 bytes=494980 located=True
```

## Defects named

**D1 — the inherited "S723 and S740 are missing" defect is stale; both rows landed during
this wave. The fragment is complete at 32/32.**
`check-rows.py` first printed `S723 PROBLEMS MISSING`, `S740 PROBLEMS MISSING`,
`30/32 clean`; later the same command printed `CHECK-ROWS: 32/32 clean`. Both row dirs now
exist under `.ufo/waves/round-64/rows/` with full `ROW/BULLET/VERIFY/CAPTURE/ACCESS`
content, and both are quoted in the fragment above. Any sibling report still asserting
"30/32 clean" or "S723/S740 missing" is a dated snapshot, not the current tree.

**D2 — three disposition rows cannot appear in a Gate list as located quotes: S744, S745,
S747.** Their own rows record the failure:
- S744 `TEST: 200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling`,
  `TEST2: NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent`;
- S745 `TEST: 403 https://www.merriam-webster.com/dictionary/tiara`,
  `TEST2: NOT_LOCATED … HTTPError`;
- S747 `TEST: 403 https://www.britannica.com/topic/mortarboard`, `TEST2: not applicable`.
My independent fetch reproduces all three (200-with-khanka-rewrite / 403 / 403; quote absent
in all three). Final receipt, `curl -sL --compressed` with the browser UA, showing the
effective URL after the rewrite:

```text
https://www.dictionary.com/browse/ushanka http=200 bytes=17359 final=https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling
https://www.merriam-webster.com/dictionary/tiara http=403 bytes=3364 final=https://www.merriam-webster.com/dictionary/tiara
https://www.britannica.com/topic/mortarboard http=403 bytes=3228 final=https://www.britannica.com/topic/mortarboard
```

The quoted strings in the fragment for these three ids are therefore
**candidate wordings, not located quotes** — S747's is not even a page quote (it is the
row's description "Britannica's Mortarboard page as evidence for mortarboard use in academic
dress"). Committing the S744/S745/S747 lines into `corpus/lessons/round-64.md` as located
quotes would put three unverifiable quotes in the lane's permanent lesson record.
**Recommendation to the L1 (not applied here — lesson file untouched):** commit the 29 lines
for S718–S743 plus S746, S748, S749 in the Gate list, and record S744/S745/S747 in a
separate rejection note carrying their `TEST`/`TEST2` evidence, in the shape round-63's
lesson used for rejects (`corpus/lessons/round-63.md:27-31`). If the L1 prefers all 32 lines
in the list, the three must be annotated as *not located* rather than presented as located.
The quoted text is reproduced verbatim above so the L1 can cut the three lines without
re-deriving them.

**D3 — S740's `VERIFY` line names the archive capture, not the live URL, and the live URL is
unreadable to a plain client.** `VERIFY: LOCATED https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early`,
while the fragment's URL field carries the live URL `https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early`.
Observed: live GET → **HTTP 403** (5,788-byte Cloudflare "Just a moment…" challenge); capture
GET → HTTP 200, 243,294 bytes, quote present, three consecutive fetches; locator `--row`
→ `LOCATED …/web.archive.org/web/20210414114152id_/…`. The quote is real and located, but
**only at the capture**. The fragment's URL field is therefore, for S740 alone, a URL that
does not serve the quote. Recommendation: for S740 use the capture URL in the URL field, or
keep the live URL and add the capture in parentheses after the date (the shape round-62's
lesson used: `- S693 | https://www.dictionary.com/browse/talaria (capture https://web.archive.org/web/20240529024530id_/…) | 2026-10-23 | "…"`).
No other row has this shape: all other 31 rows' `VERIFY` lines name their live URL and the
live URL carries the quote.

**D4 — PMC live URLs intermittently serve a bot-wall instead of the article, and the
locator then reports `quote-absent` on a URL that does carry the quote.** Reproduced: the
locator's urllib fetch of `https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/` returned a
167-character reCAPTCHA interstitial ("Checking your browser"), while `curl` with the same
Firefox UA returned the full 197,471-byte article with the quote at normalized offset 3977.
Row-mode locator runs for S718 alternated `NOT_LOCATED … quote-absent` and `LOCATED` across
runs; S733 likewise. The Wayback `id_` capture for the same rows is stable under
`curl --compressed` (HTTP 200, quote present) but the locator's urllib fetch of
`web.archive.org` intermittently got **HTTP 429**, which its retry ladder turns into
`HTTPError` after three tries. This is an availability/receipt-quality issue for claim C's
`LIVE` leg (which pins `reports/round-61/reopen-quote.py` and retries 3×20 s), not a defect in
the quotes: every PMC row's quote was located in both the live body and the row's own
capture when fetched with `curl --compressed`. **Nothing here weakens any frozen leg; the
counter was not edited.** Proposed as a routing note for the L1: the `LIVE` subset
(`S718, S723, S728, S733, S738, S743`) includes two PMC rows (S718, S733) whose live leg
depends on a bot-wall that intermittent 429s are defeating; a re-run with spacing, or an
observation that the capture alone carries the quote, is the honest mitigation.

**D5 — one locator-vs-`curl` extraction difference on S735 (PDF).** `pdftotext` on the live
Michaels 1981 PDF does not yield the quote (extraction inserts line breaks mid-phrase),
while the locator's canonical `pypdf 5.4.0` path does, and the locator prints `LOCATED` for
S735. The quote is present in the PDF (context: "…to describe an object or give a narrative
account about some past event to the entire class. The teacher, through her questions and
comments, tries to help the children structure and focus their discourse."). Not a quote
defect; recorded so a later verifier using a different PDF extractor does not read it as
absence.

## Touched surfaces

- **Written by this seat:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w1/ScribeGateQuotes.md` (this report) — the only lane-repo byte written.
- **Scratch only:** `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeGateQuotes/` — `gate_fragment.md`, `records.json`, `defects.txt`, `build_fragment.py`, `crosscheck.py`, `cap_curl.py`, `curl_check.py`, `pmc_check.py`, `mkbatch.py`, `mkcapbatch.py`, `locate_batch.sh`, `capture_batch.sh`, `locate_out.txt`, `capture_out.txt`, `lesson_probe.md`, `probe_bad.md`, `rowmode/corpus/SOURCES.md`.
- **Read only:** `.ufo/waves/round-64/rows/*/row.txt`, `.ufo/waves/round-64/check-rows.py`, `.ufo/waves/round-64/claims.json`, `reports/round-64/accept-c.py`, `reports/round-61/reopen-quote.py`, `tools/check-gate-quotes.py`, `corpus/lessons/round-62.md`, `corpus/lessons/round-63.md`, `corpus/lessons/README.md`, `corpus/SOURCES.md`, sibling w1 reports.

## Out of scope / not done

- **The lesson file `corpus/lessons/round-64.md` was not created or edited.** The fragment is
  handed over for the L1 to commit, as instructed. The commit shape for S744/S745/S747 is
  D2's recommendation, not an applied change.
- **No counter was edited or run as an acceptance gate.** `accept-c.py`, `accept-o.py`,
  `accept-ca.py` were not executed; the fragment is not an `ACCEPT-C-64` pass and nothing here
  should be read as one.
- **No registry, entry, README, LOG, SCORECARD, SOURCES row or `stage/` artifact was
  touched.** No commit, push, jj operation, or git-index mutation.
- **Bullet quality (RESTATE / caveat fidelity) was not judged here** — `CriticEntrySweep`,
  `ReviewSupportA/B/C/D` own that. This seat checked quote presence, quote length, and
  located-vs-not disposition only.
- **The `S718`/`S733` PMC wall (D4) was characterised, not fixed**; no mitigation was applied
  to the tool or the counter.

## Tooling

No tool was installed or updated this seat. Everything used was already present: system
`curl`, `python3` 3.x, `pdftotext` (poppler), `uv` (used only to run the locator's own
pinned `pypdf==5.4.0` helper, which the locator script invokes itself). `pacman` was not
touched (host-wide pacman transactions are paused).

## Axis effect

- **Coverage — improved.** The lesson Gate fragment is complete: 32/32 ids, each with a
  quote taken from its own row and each within the lane's 25-word Gate cap, verified by the
  lane's own Gate-quote gate. Two rows that the inherited attempt-1 left missing (S723, S740)
  are present and quoted.
- **Calibration — improved.** Three disposition rows are identified whose quotes are *not*
  located on their cited URLs (D2) and one row whose URL field does not serve its quote
  (D3); an unverified quote cannot silently enter the permanent lesson record. The PMC
  wall (D4) is recorded as an availability limit on the live leg rather than as a quote
  failure.
- **Operability — not harmed, nothing touched.** No counter byte, tool byte, registry byte or
  lane state was modified; the fragment is verified against the lane's existing gate, which
  passes it.
