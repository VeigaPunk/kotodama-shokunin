# ReviewSupportC — round-64 wave-1 blind support (rows S737–S743, dispositions S744–S749)

Protocol: independent plain `curl -sL --max-time 60` (Firefox UA) of each row's cited live URL on 2026-10-23; text via `pdftotext` (poppler 26.08.0) for PDFs, tag-stripped HTML otherwise; anchor quote located verbatim; BULLET judged for faithful restatement at the row's tier. No row files edited. Fetches in `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewSupportC/fetch/`.

Live statuses (single batch, `curl -w "%{http_code} %{content_type} %{url_effective}"`):

| Row | HTTP | Content-type | Effective URL |
|---|---|---|---|
| S737 | 200 | text/html | eric.ed.gov/?id=ED149852 |
| S738 | 200 | application/pdf (793,536 B) | eprints.bbk.ac.uk/…/47679.pdf |
| S739 | 200 | application/pdf (303,366 B) | journal.uny.ac.id/…/39455/pdf |
| S741 | 200 | text/html (182,475 B) | scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en |
| S742 | 200 | application/pdf (810,771 B) | files.eric.ed.gov/fulltext/EJ1271032.pdf |
| S743 | 200 | application/pdf (201,625 B) | journals.linguisticsociety.org/…/3267/2956/3857 |
| S744 | 200 | text/html | dictionary.com/browse/**khanka**?q=ushanka&noredirect=true&mismatchType=misspelling |
| S745 | **403** | text/html | merriam-webster.com/dictionary/tiara |
| S746 | 200 | text/html | en.wikisource.org/…/1977_Books_and_Pamphlets_July-Dec.djvu/447 |
| S747 | **403** | text/html | britannica.com/topic/mortarboard |
| S748 | 200 | text/html | penelope.uchicago.edu/…/SMIGRA*/Corona.html |
| S749 | 200 | text/html | en.wikipedia.org/wiki/List_of_headgear |

## Mined rows

- **S737 — SUPPORTED.** ERIC record (200) serves abstract verbatim: "A sample was considered an example of verbal play if it incorporated an observable manipulation of the sound, semantics and/or syntax of the language." BULLET restates the operational definition for playful worldbuilding; no overreach at tier A.
- **S738 — SUPPORTED.** PDF (200) contains, in section "CONCEPTUALIZATION OF THE FAMILY, NONHETERONORMATIVE MASCULINITY AND ETHNICITY": "…in relation to experts' advice, as they were explicitly instructed not to introduce the language immediately after meeting the children." Context is Polish. BULLET ("Experts instructed parents not to introduce Polish immediately after meeting the children") faithful.
- **S739 — SUPPORTED.** PDF (200): "Parents can use various terms of address to children depending on situational contexts." verbatim. Minor locator nit: the locator attributes the paragraph to "According to Aledo (2018)" but the quote's sentence cites Farese (2018) in surrounding text; quote itself verifies verbatim and BULLET is faithful. Not a defect against the row's substance; note only.
- **S741 — SUPPORTED.** SciELO HTML (200): Tomás's utterance "We know it's ugly because people tell us it's ugly." verbatim in classroom dialogue. BULLET faithful.
- **S742 — SUPPORTED.** PDF (200), Morning Meeting Greetings, p. 48: "Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other." BULLET (explicit greeting instruction → peer welcome/belonging) is a fair restatement.
- **S743 — SUPPORTED.** PDF (200), §2.2 Child-Directed Verbs: "Since this construction has a register specification as "child-directed," verbs instantiating it are unlikely to be used in adult-directed speech…" BULLET (register marks child-directed verbs as a distinct context-bound pattern) faithful.

No NOT-SUPPORTED and no UNREACHABLE among S737–S743.

## Disposition rows

- **S744 — ground CONFIRMED, rejection stands.** Live GET returned 200 after server-side rewrite to `…/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling` — the exact redirect recorded in TEST. Served page defines Khanka as "a lake in far SE Russia and NE China"; fur-cap/earflap wording absent (grep over page text: no match). Reproduces the recorded mis-match ground; flip not triggered. NOTE vs. the wave-1 seat's stated expectation of "403-blocked": the recorded ground was always the khanka redirect (row.txt TEST shows 200 → khanka), not a 403; observed behavior matches the recorded ground.
- **S745 — CONFIRMED 403-blocked.** Plain GET → HTTP 403, Cloudflare "Just a moment…" challenge body (5,600 B). Recorded ground reproduced; quote untestable, rejection stands.
- **S746 — CONFIRMED reachable; queued-candidate ground reproduced.** HTTP 200; A888375 entry text verbatim: "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters". Consistent with QUEUED-CANDIDATE status (reconstructed wording locatable; exact round-63 wording unrecoverable per row note).
- **S747 — CONFIRMED 403-blocked.** Plain GET → HTTP 403, Cloudflare "Just a moment…" challenge (5,555 B). Recorded ground reproduced.
- **S748 — CONFIRMED reachable.** HTTP 200; first body sentence verbatim: "Among the honorary crowns bestowed by the Romans for military achievements, the most difficult of attainment…" — the 11-word test string locates. Queued-candidate ground reproduced.
- **S749 — CONFIRMED reachable.** HTTP 200; lead sentence verbatim (all 21 words): "Headgear is worn for many purposes, including protection against the elements, decoration, or for religious or cultural reasons, including social conventions." Queued-candidate ground reproduced.

## Verdicts

Coverage axis: all 7 assigned mined rows verify SUPPORTED with verbatim quote hits on live URLs; no falsification found. Calibration/operability: disposition grounds reproduce exactly — S745/S747 403-blocked; S744 200-with-khanka-redirect (matches recorded ground, differs from the seat's stated "403" expectation in mechanism only); S746/S748/S749 reachable with located text. One advisory: S744's row-expected-block mechanism should be phrased as "mis-match redirect" in any future spec wording, though the rejection outcome is unaffected.

Tooling: no installs needed (system poppler `pdftotext` 26.08.0, curl, python3 suffice).
