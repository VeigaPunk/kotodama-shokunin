# Blind-support verification — round 63, seat blind-a

Scope: rows S700, S703, S704, S706 from `corpus/SOURCES.md` (headgear entry). Each row's live URL re-opened by ordinary means (HTTP fetch); anchor quote checked verbatim in body text; capture URL fetched and checked for the same page with the same quote. Verdicts below; all timestamps 2026-10-23.

Method / transports:
- Live HTML: Python stdlib `urllib` with browser User-Agent. Live PDF: same, saved and extracted with `pdftotext` (poppler, preinstalled at /usr/bin/pdftotext — no installs performed this round).
- Captures: `web.archive.org` `id_` URLs via the `read` tool (native reader for HTML, markit for the PDF) — used because direct urllib fetches to web.archive.org were refused (see transport failures).
- Verbatim matching: tag-stripped, entity-unescaped text; whitespace-normalized only. Inline `<em>`/`*…*` italics markup noted where it intersects a quote.

Transport failures met-not-passed:
1. web.archive.org — HTTP 429 Too Many Requests on all four capture URLs via direct urllib fetch (2026-10-23). Recovered: all four captures then fetched successfully via the `read` tool.
2. www.nma.gov.au — HTTP 403 Forbidden on a second urllib refetch of the S706 live page (first urllib fetch had returned 200, 117,827 bytes). Recovered: curl with browser headers returned 200; body contains the quote span (verified below).
3. pdftotext extraction artifact (not a transport failure): live S703 PDF text extracts "orange-­yellow" with a soft hyphen U+00AD at the hyphen; the rendered PDF page shows plain "orange-yellow" (the capture's markit rendering confirms plain "orange-yellow"). Anchor quote matched at rendering level.

---

## S700 — Sikh Coalition, "Identity" — SUPPORTED

- Row: `S700` — https://www.sikhcoalition.org/about-sikhs/identity/ ; capture `https://web.archive.org/web/20261010081315id_/https://www.sikhcoalition.org/about-sikhs/identity/`
- Anchor quote (row, "paragraph 3"): `the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.`
- Live re-open: HTTP 200, final URL identical to row URL, 79,244 bytes. Quote found verbatim in body text, paragraph 3, tag-stripped span:

  > … which can be worn by men and women alike. The turban was historically worn by royalty in South Asia, and **the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.** For a Sikh, wearing a turban asserts a public commitment to maintaining the values and ethics of the tradition, including service, compassion, and honesty.

- Capture re-open (read, native): page title "Identity - Sikh Coalition"; same three body paragraphs as live; quote verbatim in paragraph 3:

  > Perhaps the most visible aspect of the Sikh identity is the turban, which can be worn by men and women alike. The turban was historically worn by royalty in South Asia, and **the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.** For a Sikh, wearing a turban asserts a public commitment to maintaining the values and ethics of the tradition, including service, compassion, and honesty.

- Same page: yes — same title and identical body paragraph sequence (identity/five articles, wedding-ring analogy, turban/sovereignty paragraph, "Click here to learn more about Sikh history" link) on live and capture.

## S703 — DiLuzio, "Introduction," A Place at the Altar (PUP chapter PDF) — SUPPORTED

- Row: `S703` — https://assets.press.princeton.edu/chapters/i10895.pdf ; capture `https://web.archive.org/web/20220209094659id_/https://assets.press.princeton.edu/chapters/i10895.pdf`
- Anchor quote (row, "Introduction, printed p. 9"): `Roman brides wore the flammeum, the flaminica’s signature orange-yellow veil, as a good omen`
- Live re-open: HTTP 200, final URL identical to row URL, 648,910 bytes, `%PDF` confirmed. Extracted with `pdftotext -layout`; quote found on PDF page 9, spanning a printed line break (span joined here):

  > … The flaminica Dialis, on the other hand, served as a template for a wider range of womanly virtues, including especially fidelity in marriage. According to Festus, **Roman brides wore the flammeum, the flaminica’s signature orange-yellow veil, as a good omen** (ominis boni causa, 79L) because she was not permitted to divorce her husband.

  Printed-page check: PDF page 2 is headed "2/Introduction", page 3 "Introduction / 3", page 10 "10 / Introduction" — PDF page N = printed page N, so the quote's page is printed p. 9, as the row claims. (Extraction artifacts: soft hyphen in "orange-­yellow" per transport note 3; line break after "the".)
- Capture re-open (read, markit): same document (Horace epigraph, "Introduction", running "Introduction / N" heads); quote verbatim on markit page 9, immediately preceding the page headed "10 / Introduction":

  > Invoking the rhetoric of exemplarity, Cicero situates Vestal virginity within a familiar discourse about the regulation of female sexuality. The *flaminica Dialis*, on the other hand, served as a template for a wider range of womanly virtues, including especially fidelity in marriage. According to Festus, **Roman brides wore the *flammeum*, the *flaminica*’s signature orange-yellow veil, as a good omen** (*ominis boni causa*, 79L) because she was not permitted to divorce her husband.

- Same page: yes — same chapter PDF; quote on printed p. 9 in both; italic markup (`*…*`) in the markit rendering corresponds to italicized Latin terms in print. Apostrophe in "flaminica’s" is U+2019 in both row anchor and source.

## S704 — Arizona State Museum, "Japanese Samurai Helmet and Half Mask" — SUPPORTED

- Row: `S704` — https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask ; capture `https://web.archive.org/web/20260316015949id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask`
- Anchor quote (row, "construction paragraph"): `This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer.`
- Live re-open: HTTP 200, final URL identical to row URL, 60,413 bytes. Quote found verbatim in body text (tag-stripped span):

  > The laced design coupled with thin high-grade steel made the armor light and allowed samurai to be agile, unlike their European counterparts. **This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer.** This construction, when combined with the signature of the artisan, Hisatada, on the interior, tells us that this is an extremely fine example worn by an important samurai.

- Capture re-open (read, native): page title "Japanese Samurai Helmet and Half Mask | Arizona State Museum"; credit line "Text by Davison Packard Koenig, former Senior Exhibit Coordinator, August 2011" (matches row attribution); quote verbatim in the same construction paragraph:

  > **This *kabuto* is made of 120 individual riveted steel plates, rather than the standard 62 or fewer.** This construction, when combined with the signature of the artisan, Hisatada, on the interior, tells us that this is an extremely fine example worn by an important samurai.

- Same page: yes — same title, same object block (Edo Period, Kabuto signed Hisatada, ASM Catalog Nos. E-2400, E-2402e), same paragraph sequence on live and capture.

## S706 — National Museum of Australia, "Roman soldier's helmet" — SUPPORTED

- Row: `S706` — https://www.nma.gov.au/learn/diy/roman-soldier-helmet ; capture `https://web.archive.org/web/20260218211148id_/https://www.nma.gov.au/learn/diy/roman-soldier-helmet`
- Anchor quote (row, "did-you-know body text"): `A typical Roman helmet was called a galea.`
- Live re-open: first urllib fetch HTTP 200 (117,827 bytes); second urllib refetch HTTP 403 (transport note 2); curl with browser headers HTTP 200. Quote found verbatim in body text, "Did you know" section — raw HTML span (line 799 of saved live HTML):

  > `<p>A typical Roman helmet was called a <em>galea</em>. Some <em>galea</em> were topped with a crest, which could be made of horsehair and was sometimes dyed red.</p>`

  Tag-stripped: "A typical Roman helmet was called a galea. Some galea were topped with a crest, …" — anchor quote verbatim; `<em>` around "galea" is inline italics markup, not part of the quoted words.
- Capture re-open (read, native): page title "Roman soldier's helmet | National Museum of Australia"; metadata `DC.modified "2025-09-25"` (matches row's "modified 2025-09-25"); quote verbatim under "## Did you know ...":

  > **A typical Roman helmet was called a *galea*.** Some *galea* were topped with a crest, which could be made of horsehair and was sometimes dyed red.

- Same page: yes — same title, same Did-you-know paragraph, same instruction steps 1-5 and "Share your creation" section on live and capture.

---

## Summary

| Row | Live quote | Capture quote | Same page | Verdict |
|---|---|---|---|---|
| S700 | yes, ¶3 verbatim | yes, ¶3 verbatim | yes | **SUPPORTED** |
| S703 | yes, printed p. 9 verbatim (line-break + soft-hyphen extraction artifacts noted) | yes, printed p. 9 verbatim | yes | **SUPPORTED** |
| S704 | yes, construction ¶ verbatim | yes, construction ¶ verbatim | yes | **SUPPORTED** |
| S706 | yes, Did-you-know verbatim (`<em>` italics around "galea") | yes, Did-you-know verbatim (`*…*` italics) | yes | **SUPPORTED** |

Residual risk / verification gaps:
- S706 live verification rests on the first urllib fetch (200, quote found by normalized search) plus a later curl fetch whose saved body contains the raw span at line 799; the intervening 403 blocks show the site bot-gates repeat requests, but both successful fetches returned the identical quote span.
- S703 verbatim match is at rendering level: PDF text extraction inserts a soft hyphen in "orange-­yellow" (live pdftotext) and a line break after "the"; the anchor's plain "orange-yellow" matches the rendered/markit text. No character discrepancy beyond these extraction artifacts.
- web.archive.org 429s prevented a second independent direct fetch of the captures; capture verification is via the `read` tool reader renderings (native for HTML rows, markit for the PDF), each showing the full page with the quote.

Tooling record: no installs or upgrades performed this round. Tools used: Python 3.14 stdlib urllib, curl (system), pdftotext (poppler, preinstalled /usr/bin/pdftotext), `read` tool.
