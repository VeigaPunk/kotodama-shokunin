# R8-F15 freshness receipt — kandake / title translation, Nubia-Kush

- Round: 8 (loop 1 of 3, build round 1 of 4), date 2026-10-17
- Baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4`
- Shard: `reports/round-8/targets.json` freshness[14]
- Prior row: R6-12-B (`corpus/lessons/round-6-sources/12.json`, audits[1])
- Entry: `corpus/knowledge/civilizations/nubia-kush.md` (sha256 `351fa833…c4aa0f`, unchanged since round 6)
- Entry locator: section "Kandake: title, translation, and royal-women linguistics", lines 70-88 (table rows 74-78; bullets 80-88); source anchors line 14 `[S32]` and line 80 `[T97, pp. 213-214]`
- Machine twin: `reports/round-8/freshness/R8-F15-receipt.json` (sha256 `295509aa305f7ba488c251375d089f1aa0e6c793b2011b7c10498cff317ad870`)

Question rechecked: kandake/title translation and royal-woman identification against a text/object or
scholarly passage, keeping reigning queen, queen mother, royal imagery and universal gender-system
claims separate.

## Labels (raw vs reconciled)

| Layer | Value | Source |
|---|---|---|
| Raw worker verdict (verbatim) | `supported` | `corpus/lessons/round-6-sources/12.json` audits[1] |
| Raw worker support scope (verbatim) | `partial` | same |
| Reconciled disposition (round 6, carried in targets) | `partial-support` | `reports/round-8/targets.json` freshness[14] |
| Round-8 passage support | `supported` | this receipt |
| Round-8 whole-claim support | `partial-support` (unchanged; evidence upgraded) | this receipt |

## Fresh retrievals (all 2026-10-17, live HTTP)

1. Strabo, *Geography* 17.1.54 (Jones/Loeb trans.), LacusCurtius — the entry's own anchor `[S32]`.
   `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/17A3%2A.html` — HTTP 200, 132,385 bytes,
   sha256 `ab1fa7fa…d617c2`, accessed 2026-10-17T20:12:57Z. Location: fetched-file line 775 (generals,
   Napata, son, ambassadors) and line 778 (Candace's counter-march). Quotes:
   - "Among these fugitive were the generals of Queen Candacê, who was ruler of the Aethiopians in my time — a masculine sort of woman, and blind in one eye."
   - "After this he set out for Napata. This was the royal residence of Candacê; and her son was there, and she herself was residing at a place near by."
   - "But though she sent ambassadors to treat for friendship and offered to give back the captives and the statues brought from Syenê"

2. Strabo 17.1.54, Hamilton–Falconer translation, Perseus (cross-witness for the transcription question).
   `https://www.perseus.tufts.edu/hopper/text?doc=Strab.+17.1.54&fromdoc=Perseus%3Atext%3A1999.01.0239` —
   HTTP 200, 306,662 bytes, sha256 `ab7425af…49f66d`, accessed 2026-10-17T20:13:14Z. Location: fetched-file
   line 465. Quote: "Among the fugitives, were the generals of Candace, queen of the Ethiopians in our time, a masculine woman, and who had lost an eye."

3. Kirsty Rowan, "Revising the Sound Value of Meroitic D" (*Beiträge zur Sudanforschung* 10, 2009),
   SOAS eprint 12838, retrieved via Wayback capture
   `https://web.archive.org/web/20230522185116/https://eprints.soas.ac.uk/12838/1/Revising_the_Sound_Value_of_Meroitic_D.pdf`
   — HTTP 200, 412,409 bytes, sha256 `37c50955…674d73`, accessed 2026-10-17T20:18:14Z. Location: PDF page 7
   of 8, table "(10)" and the /kandake/ sentence. Quotes:
   - "There is an orthographic practice in Meroitic whereby a nasal segment in coda position followed by a consonant is unwritten. Therefore the Meroitic form ekdk kdke is phonemically /kandake/"
   - "Meroitic ekdk (ektk) kdke (ktke) title; Egyptian kntiky; Greek κανδάκη; Ethiopic xan(ə)dākē"

4. Wikipedia, "Kandake" (tertiary). `https://en.wikipedia.org/wiki/Kandake` — HTTP 200, 286,771 bytes,
   sha256 `5a897379…4b67ad`, accessed 2026-10-17T20:13:15Z. Location: raw HTML line 673 (lead), line 925
   (reference 3 = Török 1997 pp. 213–214). Quotes:
   - "was one Meroitic term for a queen or queen mother of Kingdom of Kush. It is attested for six or seven women. Some were rulers, while others were most likely just wives of a king."
   - "A kandake who ruled in her own right bore in addition the title qore, the same title carried by male rulers. Contemporary Greek and Roman sources treated it, incorrectly, as a name."
   - "László Török (1997), The Kingdom of Kush: Handbook of the Napatan–Meroitic Civilization, Brill, pp. 213–214."

5. Wikipedia, "Meroitic language" footnote 38 (tertiary pointer to Hofmann 1981 p. 41).
   `https://en.wikipedia.org/wiki/Meroitic_language` — HTTP 200, 243,892 bytes, sha256 `199eb1f3…399951b5`,
   accessed 2026-10-17T20:16:02Z. Location: raw HTML line 748. Quotes:
   - "The resyllabified /n/ is known, firstly, from transcriptions of Kushite: ⟨kdke⟩, ⟨ktke⟩ \"female ruler\" as Egyptian: ⟨kntı̇ky⟩, Greek: κανδάκη, Latin: Candace"
   - "See, I. Hofmann, Material für eine meroitische Grammatik (…Beiträge zur Afrikanistik 13), Wien 1981, p. 41."

6. Google Books volume page for Hofmann 1981 (bibliographic only, no passage; `retrieved_passage: false`).
   `https://books.google.com/books?id=bHMOAAAAYAAJ&dq=searchwithinvolume&q=hesychius` — HTTP 200, 50,651
   bytes, sha256 `c3ef90bf…21494a`, accessed 2026-10-17T20:16:21Z. Search-within returned 0 hits
   ("Resultados 1-0 de 0"); the page confirms 1981, Afro-Pub, 361 pp.

## Access failures (attempted command + status)

| Leg | Attempt | Result |
|---|---|---|
| Greek original of Strabo 17.1.54 (κανδάκη) | Perseus hopper, two URL forms | HTTP 503 both times; 0 bytes contain "Κανδ" |
| Török 1997 pp. 213-214 | HathiTrust catalog search | HTTP 403 |
| Török 1997 | archive.org advancedsearch API | HTTP 200, `numFound: 0` |
| Hofmann 1981 p. 41 | archive.org item metadata + search-inside (`inside.php`, two queries) | item exists but `access-restricted-item: true`; search-inside HTTP 403 "Item not available" |
| Khan 2012 queen-mother paper | Academia.edu page fetch | HTTP 403 challenge |
| Lohwasser 1999 PDF | `curl` Heidelberg propylaeumdok URL | curl exit 28, connect timeout after 132,929 ms, 0 bytes |
| Rowan 2009 live host | `curl` eprints.soas.ac.uk | curl exit 6, DNS failure (superseded by Wayback capture) |
| IA full-text search host | `curl` ia-fts.archive.org | curl exit 6, DNS failure (classic endpoint used instead) |

## Transcription variance (prior-limit item, now settled at witness level)

The round-6 doubt was the raw "fugitive"/"fugitives" spelling. Fresh fetches show: the entry's cited
witness (LacusCurtius) reads singular "fugitive"; the plural belongs to a *different translation*
(Hamilton–Falconer at Perseus), not to a variant transcription of the same page. The worker's spelling is
faithful to the cited witness. The printed Loeb page image was not retrieved, so print-level typography
remains unverified.

## Leg coverage, round 6 vs round 8

- Reigning-queen/war-report leg (lines 85-86): fresh retrieval, hash- and line-located — passage support confirmed.
- kdke title + nasal caveat (lines 74, 76, 82): upgraded from tertiary-only to a peer-reviewed passage (Rowan 2009); Hofmann p. 41 still unread.
- Queen vs queen-mother contextualization, qore (lines 74, 77-78): newly retrieved but tertiary-grade; citation trail to Török 1997 pp. 213-214, Ashby 2021, Khan 2012 — originals unread.
- Individual ruler identification (line 83): carried forward from round-6 Labia 2018 evidence; not re-retrieved here.
- Royal imagery: not retrieved in this shard; remains unverified by this receipt.
- Universal gender system (line 87): no passage evidences it; the absence-claim is retained, not proven.

## Disposition

Passage support: **supported** (Strabo re-verified fresh; title-translation leg now peer-reviewed).
Whole-claim support: **partial-support** — the disposition is unchanged, with the evidence upgraded and the
unread legs (Hofmann p. 41, Török pp. 213-214, Greek original, Lohwasser, an epigraphic kdke witness)
recorded as documented failures or not-yet-retrieved. Nothing here evidences or refutes a universal gender
system, and the gendered description stays attributed to Strabo.

## Counts (2026-10-17)

6 retrievals (5 substantive passages + 1 bibliographic-only), 7 documented access failures, 12 located
quotes, 0 excerpts over 40 words. Recompute:
`python3 -c "import json;d=json.load(open('reports/round-8/freshness/R8-F15-receipt.json'));r=d['retrievals'];print(len(r),sum(1 for x in r if x.get('retrieved_passage')),len(d['access_failures']))"` → `6 5 7`.

All excerpts were re-verified as contiguous substrings of the saved copies after documented normalization
(HTML tag-strip; PDF whitespace-collapse) — commands and per-source results in the JSON's
`quote_verification` field.
