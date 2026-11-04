# Independent source audit — round 86 / ScoutGenreSources

Axes: depth + operability. Access date for every opening below: 2026-11-04.

Read frozen claims.json and relevant measure86.py ROWS/ENTRY/ANCHORS predicates; neither was modified. Declared D consumer: `corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md`. Registry untouched. Row fragments have the existing eleven-column schema and proposed B/mined/2026-11-04/180d fields. These are source findings, not an external admission or validator verdict. Freshness pause unchanged; planner-role prohibition has no adjudicated exception here.

## S924 — historical definition, not universal authority

Opened https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Proverb independently through the URL reader. Read both article paragraphs, distinguishing the Wikisource editorial disclaimer/Latin gloss from the 1911 article. Title: “Proverb,” Encyclopaedia Britannica, 11th edition, volume 22. Reader exposes revision oldid 13344958. The short entry has no separate preface.

Located quotes (whitespace folded, each at most 25 words):
- First article paragraph, definition discussion: “of which none has met with universal acceptance.” [8 words].
- First article paragraph, definition discussion: “shortness, sense and salt” [4 words; Howell’s formulation as quoted by the article, not independently opened Howell].
- First article paragraph, after Howell: “omit the chief characteristic, popularity or general acceptance” [9 words].
- Second article paragraph: “There are many popular handbooks giving full collections of proverbs, English and foreign.” [14 words].

Scope: evidence of this encyclopedia’s 1911 account and bibliographic leads. Its dated etymology and aesthetic judgments are not modern linguistic consensus. Bibliographic names are not evidence that their books were opened.

Same-page capture FOUND and opened: https://web.archive.org/web/20260212165937id_/https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Proverb . Both paragraphs and the short literal quote above are present. Canonical-target CDX returned status-200 HTML captures 20251013011527 and 20260212165937. Live/capture article text agrees for the relevant quote; not a byte-equivalence assertion. A separate urllib fetch returned HTTP 403; preserve that transport failure alongside the reader success, not as source inaccessibility.

## S925 — Apperson’s selected historical dictionary

Opened https://archive.org/download/in.ernet.dli.2015.120981/2015.120981.English-Proverbs-And-Proverbial-Phrases-A-Historical-Dictionary_djvu.txt independently. Reader and urllib served the OCR text. Title block identifies G. L. Apperson and *English Proverbs and Proverbial Phrases: A Historical Dictionary*, London/Toronto J. M. Dent; New York E. P. Dutton. No confidently read publication year in the opened title block: do not infer one from the item identifier. Inspected preface pp. vii–ix, arrangement and reference instructions, and A-section body entries “A”, “Above-board”, and “Absence is a shrew.” Full volume was not exhaustively read.

Located quotes, whitespace folded:
- Preface p. vii, paragraph beginning “It is obvious”: “the historical method of treatment can only give an approximation to accuracy.” [13 words].
- Preface p. vii, paragraph beginning “The whole of Ray’s collections”: “except a few offensively dirty or indecent sayings” [8 words]. This is Apperson’s exclusion language, not the scout’s endorsement.
- Preface p. ix, opening paragraph: “The omissions, both of sayings and of illustrations” [8 words].
- Body, “Above-board,” 1753 Richardson example: “All is fair, all is above-board: all is as it was represented.” [13 words]. This is an example reproduced by Apperson, not an independently opened Richardson original.

Admission boundary: a dated literary example is an attestation in a selected compilation, not the proverb’s invention date, earliest oral use, or a census of communal acceptance. Apperson explicitly acknowledges approximation, omissions and exclusion. Historical dictionary examples must retain their reference/edition fields; reader OCR is not a diplomatic transcription.

Independent raw receipt: `S925.txt`; fetch-receipts.json records HTTP 200, 3,136,360 bytes, sha256 a76f9f1ed6f985b824523df071e7f0a0c9c6f1f3e0fd02e3c899796e62c112c9, archive.org redirect to a public download node.

Same-page capture UNRESOLVED, not absent. Availability API returned HTTP 429. Exact canonical download-URL CDX returned HTTP 403. Positive control `https://web.archive.org/cdx/search/cdx?url=example.com&output=json&filter=statuscode%3A200&limit=1` returned a status-200 capture (20020120142510), so the service answered a control, but target failure still proves neither absence nor presence. Flip: ordinary exact-target CDX succeeds and a returned replay is opened with the quote present. Do not substitute an item landing-page capture for this text URL.

## S926 — Tupper’s edition and solution history

Opened https://archive.org/download/riddlesofexeterb00tuppuoft/riddlesofexeterb00tuppuoft_djvu.txt independently through the reader; resolved public download node was ia801605.us.archive.org. Title block: Frederick Tupper, Jr., editor, *The Riddles of the Exeter Book*, Ginn and Company, 1910; preface dated September 1909. Inspected preface pp. vii–viii; introduction discussion of comparison and solutions (pp. lxxix, lxxxiii–lxxxiv); body Notes around Riddle 9; Index of Solutions p. 291. Full edition not exhaustively read. Preserved successful reader receipt in `S926-opened-reader.txt`; separate urllib handshake timed out, retained in fetch-receipts.json.

Located quotes, whitespace folded:
- Preface p. viii, editorial departures: “all departures from the manuscript which originate with the editor are printed in italics.” [15 words].
- Introduction §IV “Solutions of the Exeter Book Riddles,” p. lxxix: “Unlike the Latin riddles of their period, the Anglo-Saxon queries are unaccompanied by their answers.” [16 words].
- Introduction §IV, p. lxxxiii: “The solution of riddles is too uncertain a matter” [10 words].
- Introduction §IV, p. lxxxiv: “Within five years I have modified my own views of as many problems.” [13 words].
- Notes, Riddle 9, opening solution-history paragraph: “To this riddle many solutions have been offered.” [9 words]. No printed page number asserted from the opened excerpt.

The Index OCR line begins “Black type, both in names and in numbers, indicates solutions acce” and is visibly truncated. Reject completing its missing wording as a verified quotation. OCR/plain text cannot reliably preserve the bold distinction between accepted and merely listed solutions, nor the preface’s italic editorial distinction. A scan-image check is required before making typography-dependent claims. Keep Tupper’s numbering edition-specific; do not silently map it to modern numbering. Peer source warning reports the same URL was already used by inherited ORALITY-03: this is renewed/deeper examination, not first source/genre acquisition.

Same-page capture UNRESOLVED, not absent. Availability API returned HTTP 429; exact canonical download-target CDX returned HTTP 403. The same positive control above succeeded. Flip: exact-target CDX succeeds and an ordinary replay opens with relevant passage present. No login, CAPTCHA, private endpoint or paywall bypass attempted.

## Gate — candidate distinctions and flips

- ADMIT candidate (source-bounded B): Apperson’s historical method supplies approximate selected literary attestations, not oral origins. Opened preface explicitly says “can only give an approximation to accuracy.” Flip to refuse this support if the quoted preface is not present in the consulted edition or the entry claims exhaustive first occurrence.
- ADMIT candidate (source-bounded B): Tupper records absent supplied answers and competing/revised scholarly solutions. Preserve editor, edition and numbering; do not universalize his preferences. Flip to refuse if the claim becomes that every riddle has exactly one proven answer.
- REJECT candidate: “Apperson’s earliest printed example dates the invention of each proverb.” Reason: selected/excluded material and explicitly approximate historical method; print attestation is not oral origin. Flip: narrow wording to earliest example located by this named editor, or separately open evidence establishing the stronger individual origin claim.
- REJECT candidate: “Every answer in Tupper’s index is accepted and settled.” Reason: preface says the index records proposed answers; the body documents uncertainty/retractions; OCR truncates a typography legend. Flip: inspect page images and individual notes, label accepted versus proposed for this edition only, and retain alternatives/uncertainty.
- REJECT candidate: “S924 is a universal modern definition of proverbs.” Reason: the 1911 article itself denies universally accepted definitions; it is historical secondary evidence. Flip: attribute its formulation to EB1911 and avoid universality.

## Limits and handoff

Observed: all three specified source URLs independently opened via reader; S924 same-page replay opened; S925 raw download preserved. Archive-query failures remain explicit. No absence-of-capture claims. No code/exported contract changed, so LSP tracing not applicable. No installations, background jobs, delegated work, builds, lint, tests, formatting, registry edits, git/jj mutations or commits. Scratch not created; nothing there to remove. Source rows remain proposed fragments for L1 integration, not a finding that D has landed or its predicate has passed.
