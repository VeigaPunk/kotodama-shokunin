# Falsify review — claim C rows S401–S403 (Kongo entry)

Verdict: no actionable finding; all four checks carried for S401, S402, S403.
No defect found; quote-glyph and PDF-extraction notes below are residual risk, not findings.

Method: re-opened each row's URL by ordinary means. S401 plain GET to
https://prm.web.ox.ac.uk/files/mavungupdf → HTTP 200, application/pdf, 9 pages
(2010, matches row provenance); S402 plain GET to
https://openaccess-api.clevelandart.org/api/artworks/168726 → HTTP 200, JSON
(8541 B, object id 168726, accession 2010.432, CC0); S403 plain GET to
https://arthistoriography.wordpress.com/wp-content/uploads/2011/12/mack-fetish.pdf
→ HTTP 200, application/pdf, 14 pages (printed pages 54–62 reached via 180°
page rotation; footers decoded). Text extracted with pypdf and pdfplumber.

## Checked items

- S401 (Pitt Rivers Mavungu PDF): anchor quote 1 — "Mavungu is a type of nkisi known as a nkondi (plural minkondi), which in the past was inadequately glossed as a 'nail fetish'." — CARRIED. Verbatim at section "What is Mavungu?" opening, PDF page 1: "Mavungu is a type of nkisi known as a nkondi (plural minkondi), which in the past was inadequately glossed as a ‘nail fetish’." (23 words; page uses curly ‘ ’, row/lesson use ASCII ').
- S401 anchor 2: "The term nkondi means 'hunter at night'" — CARRIED, same section, page 1: "The term nkondi means ‘hunter at night’, since such figures" (7 words).
- S401 anchor 3: "The nganga himself would often be of an equally striking and frightening appearance during such rituals, wearing a costume with charms attached." — CARRIED, same section, page 2, verbatim (22 words).
- S401 anchor 4: "Such medicine containers were mostly removed from minkisi by missionaries or colonial agents, since this was where their indigenous power was understood to reside." — CARRIED, section "How did Mavungu come to the Museum?", page 4, verbatim (24 words).
- S401 Gate line quote = anchor 1, no second quote. Tier B (docs) fits QUALITY criterion 6: museum-authored interpretive record is strong secondary for nkondi practice and authoritative for its own object; not primary testimony; B correct. Grounds ("The Pitt Rivers record explains nkondi as a night-hunting figure that a nganga worked with nails and medicines for paying clients, and whose power left with its medicines.") equals the row's teaches cell byte-for-byte (ignoring the row's trailing "Seat:" field).
- S401 entry sentences: §9 "Two offices make one object" — "The Pitt Rivers glosses nkondi as 'hunter at night' and calls 'nail fetish' an inadequate gloss (S401, section What is Mavungu?)" CARRIED at stated strength (both phrases on PDF page 1 in that section). Era table (line 115) "nkisi collected by missionaries and colonial agents … S401 (How did Mavungu come to the Museum?)" CARRIED: section says containers "mostly removed from minkisi by missionaries or colonial agents", figures "exchanged, sold, or kept as curios by traders and agents, or else collected by missionaries". Misconception R (line 144) "Mack and the Pitt Rivers reject the label (S403, p. 54; S401, section What is Mavungu?)" CARRIED.
- S402 (Cleveland API record): anchor 1 "This nkisi nkondi (power figure) lacks most of the materials that transformed it into a vessel for a spirit." — CARRIED. Verbatim as JSON description first sentence (tags stripped) (19 words). Locator "object record description, first sentence" correct.
- S402 anchor 2: "Carved by sculptors, minkisi hosted spirits after banganga (priests) placed substances inside to empower them." — CARRIED, second sentence, verbatim (15 words).
- S402 anchor 3: "After the nkisi had served its purpose the nganga removed the materials, stripping it of its spiritual power; the remaining sculpture was discarded." — CARRIED, fourth sentence, verbatim (23 words).
- S402 anchor 4: "Sometimes, Kongo people removed materials as acts of anti-colonial resistance, disempowering minkisi before Europeans seized them." — CARRIED, fifth sentence, verbatim (16 words).
- S402 tier A (docs) fits criterion 6: holding museum on its own accession is primary/authoritative for the exact scope; the row itself notes B only "if stretched to statements about minkisi in general", and the entry uses the row only to attribute what Cleveland's record says. Grounds equals teaches cell byte-for-byte (minus "Seat:" field).
- S402 entry sentences: §9 "Cleveland says sculptors carved and banganga placed the substances (S402, object record description)" CARRIED (second sentence); §9 "Cleveland records disempowering as anti-colonial resistance and says it does not know why its figure was stripped (S402, object record description)" CARRIED (fifth sentence plus "While we don't know why it was disempowered"). Museum label read as museum record, not as study; no over-read.
- S403 (Mack, Journal of Art Historiography 5, 2011): anchor 1 "In the end, the perception of these objects as 'fetish' is an entirely spurious external view which classifies objects regardless of indigenous understanding." — CARRIED. Verbatim on printed p. 54, section "The Myth of the Fetish" (PDF page 3), ASCII quotes match byte-for-byte (23 words).
- S403 anchor 2: "In general, however, all such objects are referred to under the common term nkisi (or plural minkisi) and are thought of as containers." — CARRIED, printed p. 56, section "The Object and its Function", verbatim (23 words).
- S403 anchor 3: "Without these elements the nkisi is neutralised." — CARRIED, p. 56, same section, verbatim (7 words).
- S403 anchor 4: "The powers, however, are not general but personalised and specific to individual objects which often bear their own name." — CARRIED, p. 56, same section, verbatim modulo PDF font-encoding artifact "rvhich" for "which" and line-break hyphen "gen-eral" (19 words).
- S403 tier B (paper) fits criterion 6: open-access peer-reviewed journal article reprint of a 1995 essay, expert secondary interpretation; B correct. Grounds ("Mack defines nkisi as a container of medicines animated by a named power, and calls the outsider label "fetish" a spurious classification.") equals teaches cell byte-for-byte (minus "Seat:" field).
- S403 entry sentences: §9 "Mack writes that all such objects are called nkisi or minkisi and are thought of as containers, neutralised without their medicines (S403, p. 56)" CARRIED: "referred to under the common term nkisi (or plural minkisi) and are thought of as containers" and "Without these elements the nkisi is neutralised"; "calls the 'fetish' view an entirely spurious external one (S403, p. 54)" CARRIED. Misconception R "Mack … reject the label (S403, p. 54; S401, …)" CARRIED. No over-read: the entry's general claims are all attribution readings of Mack's essay.

## Residual risk and verification gaps

- S401 anchor 1 and 2 quote glyphs: page renders curly ‘ ’, row/lesson store ASCII '. Semantically identical; no defect found, but a strict byte-exact verbatim checker would flag a mismatch. No fix offered (normalization is deliberate and consistent with the lesson).
- S403 anchor 4 word "which" extracts as "rvhich" (PDF font encoding); confirmed as a rendering artifact of this scan (other words show the same mapping, e.g. "fetish"→"Gtish" in a page-58 caption) and the sentence is present at the locator. If byte-exact comparison is required by the verifier, it would need a glyph-normalization step for this PDF.
- Not re-run: the Cleveland public HTML page https://clevelandart.org/art/2010.432 (the row reports HTTP 200; only the API record was needed for the quotes). Wayback/redirect details for S403 (final HTTP 200 observed; full redirect chain not captured).
- Tools installed (tooling directive): uv venv at scratch, pypdf 6.21.2, pdfplumber 5.14.0 (channel: uv, reason: PDF text extraction). No system packages touched.
