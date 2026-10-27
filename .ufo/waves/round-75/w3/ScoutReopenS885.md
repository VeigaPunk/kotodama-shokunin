# S885 independent reopen — W3

## Fetch and evidence-window comparison

- Independent plain GET: `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`
- User-Agent sent: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
- Observed response: HTTP **200**, final URL unchanged, **109588 bytes**; SHA-256 **`502b4acf0f73f8b9817f4d60b2703fce87cc9628c09397fdb27a7afa88d8fc48`**.
- Committed receipt `reports/round-75/evidence/S885.txt` records HTTP 200, same UA and URL, **109588 bytes**, but SHA-256 **`20b571d7a6a9bc3835b1406079adeea4279dc2bc4c5e7134c1ce31dbf25de034`**. **Hash equality: no** (same byte length, differing content hash; this is another served body, not byte-identical).
- The receipt's whole-document normalized-text window is 3720 chars (`before=714`, `after=2968`), 3852 UTF-8 bytes, hash `94acd2bac0cc946a9ec295633f40eaa7d1951ad5e945d6a0c5595dfc53958dc7`. Its stored window contains the quote verbatim at the opening of the article body, immediately after the title/author heading: **yes**, «Innombrables sont les récits du monde.» The independent response's exact raw body was not retained after scratch cleanup, so its extracted-text window/hash was not computed independently; quote location on the independent body is therefore not independently confirmed by this fetch.

## Registry and Gate

`corpus/SOURCES.md` S885 row (line 840) says **paper / A**, reason: Tier A because the printed primary article was opened page by page this round. Scope is the article's own structural method: multiple levels, hierarchy, two readings from their articulation, functional-unit classes; it explicitly says five *S/Z* codes are later rework and not to be attributed to this article. Locator is the notice opening sentence for the Gate quote and transcription pages 5, 6, 11 for method. `used-by` lists exactly the three S885-citing entries: base `narrative-structure-frameworks.md`, `...amend-2026-10-23.md`, and `...amend-2026-10-23b.md` (matches grep of source IDs). Recheck is `180d`.

**Tier: agree, with scope caveat.** The primary article is appropriate A evidence for its printed claims, and the row records page-by-page opening. The just-repeated notice fetch alone does not independently establish the page-by-page method evidence; that relies on the cited page-transcription source trail in the row. The Gate anchor quote is present in the committed receipt window, so its quote/window requirement holds. The mutable page response's hash differs from the receipt, despite identical length.

## S885-cited entry claims

Reviewed all S885 hits in the three entries. **No sentence was found that the page does not carry.** The entry statements are supported by the relevant article text: opening universality and media/genre list, no-people-without-narrative and transculturality, the shared-model argument and Saussure/langue analogy (printed p. 1); three levels, progressive integration, hierarchy and horizontal/vertical reading, functional classes, mixed units and expansions (p. 5 and continuation); and the stated debts to Benveniste, Lévi-Strauss, and Todorov (p. 5). The base-entry statement explicitly excludes *S/Z*'s five codes from these pages, consistent with the article's scope. The b-amendment's S885-cited claims concern its p. 5 transcription; the independent notice body does not itself contain that page, so their support is the separately identified page transcription, not the notice fetch.

## Evidence limits

The requested per-entry sentence-by-sentence check against the independent *notice page response* is limited: that response has opening notice text only, whereas the cited framework/method claims quote printed p. 5 and later pages. Those claims are supported by the registry's separately cited transcription pages, but I did not refetch those pages in this seat. Independent fetch evidence (status/bytes/hash/UA) is from the live notice; receipt window evidence is read from the committed evidence file. No tools were installed.