# ScoutAmendTriage — triage of the REST of the staged conlang family (round 73, wave 1)

Seat: ScoutAmendTriage (leaf; no delegation, no background jobs, no `task` spawns).
Date: 2026-10-25. Scope: the four staged amend files below, every staged row resolved by
DOCUMENT, fetched live, and span-checked against the amendment text. The DRAFT claims file
(`reports/round-73/claims.json`) was read and never edited; the fleet repo, lane jj/git
state, and the staged package were never mutated.

## Files triaged (staged package, read-only)
- `conlang-scholarship.amend-2026-10-23b.md` — S909 (MGIMO), S910 (Springer DOI)
- `conlang-scholarship.amend-2026-10-23c.md` — S915 (Crossref query); prose cites S769
- `conlang-scholarship.amend-2026-10-24.md` — S929 (Luba PDF), S930 (Schreyer/Crossref); prose cites S806
- `conlang-methodology.amend-2026-10-24.md` — S920 (Wayback/Cambridge), S922 (Crossref negative), S923 (Crossref)

## Fetch hygiene (QUALITY 21/22)
- User-Agent used for **every** live fetch: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` (browser-shaped; recorded in `/tmp/ScoutAmendTriage/UA.txt`).
- Downloads kept in `/tmp/ScoutAmendTriage/` only (never fleet/lane root).
- PDF text extracted with `pdftotext -layout` (poppler 26.08.0, system-provided).
- No tools installed/updated; **pacman not run** (host-wide pause). `curl`, `pdftotext`, `pdfinfo`, `grep`, `wc` all system binaries.
- No challenge wall bypassed: Springer's JS "Client Challenge" page was left unpassed (QUALITY 10).
- Wayback CDX probes filed for the canonical slugs (see below).

## Verdict table

| staged file | row | document | reachable | span present | adopt-candidate this round | reject reason + flip |
|---|---|---|---|---|---|---|
| amend-23b | S909 | Петров П.В., «Сконструированные языки: опыт хронологического описания», Филологические науки в МГИМО 10(3):75–99, DOI 10.24833/2410-2423-2024-3-40-75-99 (CC BY) | YES — HTTP 200, 5,824,942 bytes, application/pdf | YES — English abstract enumerates all nine fields verbatim: 1 year, 2 name, 3 creator, 4 country+city, 5 classification (a priori/a posteriori/mixed), 6 DIAL number, 7 description, 8 sample text (numbers 1–10), 9 references (extraction lines 229–247, article front matter) | N | Verified sound, but out-of-scope this round: the two admitted theme entries fix rows only from staged S881/S882/S892/S893/S901; flip = "reachable, span present → not admitted (beyond the two entries), defer". |
| amend-23b | S910 | Windsor, J.W., "Conlangs in Theoretical Linguistics", in *The Palgrave Handbook of Constructed Languages* (Springer Nature Switzerland, 2026), pp. 343–363, DOI 10.1007/978-3-032-03277-5_15 | YES — Crossref record for the DOI: HTTP 200 (14,874 bytes). `doi.org` → `link.springer.com` returns HTTP 200 but serves a JS "Client Challenge" wall (left unpassed; QUALITY 10) | YES — Crossref record carries title "Conlangs in Theoretical Linguistics", container-title "The Palgrave Handbook of Constructed Languages", page 343–363, issued 2026, publisher Springer Nature Switzerland, ISBN 9783032032768/9783032032775, type book-chapter; sibling `_16` (Tarasov, "Conlangs in Typological Research", 365–392) also resolves | N | NOT the "unreachable" branch of the REJECTS leg: the payload (the DOI metadata record the row was opened as) **is** reachable by ordinary means. Flip = "staged 'unreachable by ordinary means' → reachable via Crossref record; still not admitted (beyond the two entries), defer". |
| amend-23c | S915 | Palgrave Handbook chapter list via Crossref REST query | YES — HTTP 200 (15,969 bytes) | YES — the 19 handbook chapters are the top-ranked items (DOIs …_1–_19, all container "The Palgrave Handbook of Constructed Languages", 2026); gate quote "Conlangs in Typological Research" (_16, Tarasov, 365–392) present; authors/page ranges present | N | Defective as staged: (a) query token "Languistics" misspelled (correct: "Languages") — fuzzy match still surfaces the chapters first; (b) `query.container-title` is a relevance search, not a container-title filter (total-results 730,163; unrelated Palgrave handbooks follow item 19 — round-7 CANNOT-ANSWER already flags this); (c) amendment's "in law" domain is unsupported by the chapter list (chapter _17 is "…in Language Acquisition Studies", not law). Flip = "staged 'nineteen chapters spanning … and law' → 19 chapters confirmed, 'law' claim unsupported, query string defective; not admitted". |
| amend-23c | S769 (campaign id, prose) | cited in prose as "round 5 named the handbook (S769)" | n/a (id citation, not a URL) | n/a | N | Campaign-id defect (S728 class): lane-registry **S769** = Opie, *The Lore and Language of Schoolchildren* (unrelated document). The real cited document is the Palgrave Handbook (S915/S910). Flip = "staged 'handbook S769' → S769 names an unrelated lane row; must never appear in admitted entries (REPOINTED leg)". |
| amend-24 | S929 | Luba, K., "Forschung über künstliche Sprachen: Entwicklung, Funktionen und Beispiele", *Linguistische Treffen in Wrocław* 27 (2025) (I): 385–396 | YES — HTTP 200, 168,723 bytes, application/pdf | YES — span1 "insbesondere drei Hauptgruppen unterscheiden: Plansprachen, künstlerische Sprachen" verbatim on printed p. 387; span2 "interpretativ, explorativ und konfigu-" verbatim (hyphen-split across the printed line break; next line continues "rativ.") | N | Gate location error for span2: it sits on printed p. 390 (internal p. 6), **not** p. 387. Flip = "staged 'both spans p. 387' → span1 p. 387 ✓, span2 p. 390 ✗; content supported, location correction required; not admitted". |
| amend-24 | S930 | Schreyer, C., "Constructed Languages", *Annual Review of Anthropology* 50: 327–344 (2021), DOI 10.1146/annurev-anthro-101819-110152 | YES — Crossref record: HTTP 200 (22,456 bytes) | YES — "Annual Review of Anthropology", "327-344", "Constructed languages, also known as conlangs" all present; abstract's three subjects (creation process, community of conlangers, classroom adoption) match the amendment verbatim; ISSN 0084-6570, author Schreyer, issued 2021-10-21 confirmed | N | Verified sound, but out-of-scope this round; flip = "reachable, span present → not admitted (beyond the two entries), defer". |
| amend-24 | S806 (campaign id, prose) | cited in prose as "the handbook (round 6's S806)" | n/a (id citation) | n/a | N | Campaign-id defect (S728 class): lane-registry **S806** = Jaiswal & Williams, Ayurveda article (unrelated document). The real cited document is the Palgrave Handbook. Flip = "staged 'handbook S806' → S806 names an unrelated lane row; must never appear in admitted entries". |
| methodology-24 | S920 | Sowers-Wills, S., "Phonology from the Inside Out: Constructed Language as a Pedagogical Tool", *Canadian Journal of Linguistics/Revue canadienne de linguistique* (2024), DOI 10.1017/cnj.2024.21, via Wayback capture | YES — HTTP 200, 638,008 bytes, application/pdf (matches round-7 note) | YES — span "students created a phonemic inventory informed by world-language inventories and" verbatim | N | Anchor defect: the span is on **printed p. 310**, §1.3 "Institutional and course details" (internal p. 4), **not** §2.1.2 « Petlang » p. 312 (that section begins on printed p. 313). The amendment's two-task content is itself supported (petlang IPA-chart task in §2.1.2 p. 313; separate inventory-creation sentence in §1.3 p. 310). Flip = "staged '§2.1.2, p. 312' → span present but at §1.3, p. 310; location must be corrected; not admitted". |
| methodology-24 | S922 | Crossref REST journal-list endpoint (negative-result row) | YES — HTTP 200 (196 bytes) | YES — `"total-results":0` and `"items":[]` exactly as served; control query `constructed` returns 3 journals (endpoint matches journal titles) | N | Negative result stands and is the registry's own answer; out-of-scope this round; flip = "verified negative → not admitted (beyond the two entries), defer". |
| methodology-24 | S923 | Goodall, G., "Constructed Languages", *Annual Review of Linguistics* 9: 419–437 (2023), DOI 10.1146/annurev-linguistics-030421-064707 | YES — Crossref record: HTTP 200 (12,490 bytes) | YES — "There are four main types of these constructed languages." and "Annual Review of Linguistics" present; ISSN 2333-9683 confirmed; fourfold taxonomy (philosophical / international auxiliary / fictional / psycholinguistic experiments) present in the deposited abstract | N | Verified sound, but out-of-scope this round; flip = "reachable, span present → not admitted (beyond the two entries), defer". |

## Probed URLs (filed for the Gate)
Live fetches (all with the browser UA above; status → final URL → bytes):
- S909 `https://philnauki.mgimo.ru/jour/article/viewFile/520/524` → 200 → same → 5,824,942
- S910 `https://doi.org/10.1007/978-3-032-03277-5_15` → 200 → `https://link.springer.com/10.1007/978-3-032-03277-5_15` (JS challenge page, 3,038 bytes; not bypassed); `https://api.crossref.org/works/10.1007/978-3-032-03277-5_15` → 200 → 14,874; sibling `…_16` → 200 → 9,638; corrected-spelling variants `…978-3-031-03277-5_15/_16` → 404 (confirm the staged DOI string is the registered one)
- S915 `https://api.crossref.org/works?query.container-title=The+Palgrave+Handbook+of+Constructed+Languistics&rows=40&select=DOI,title,author,page,issued,container-title` → 200 → 15,969; corrected-spelling variant `…Constructed+Languages…` → 200 → 16,006 (returns the same 19 chapters first, then other Palgrave handbooks)
- S929 `https://linguistische-treffen.pl/articles/27/24_luba.pdf` → 200 → same → 168,723
- S930 `https://api.crossref.org/works/10.1146/annurev-anthro-101819-110152` → 200 → 22,456
- S920 `https://web.archive.org/web/20260115005532id_/https://www.cambridge.org/core/services/aop-cambridge-core/content/view/649F8BEDBF579512088F614EB2794B59/S0008413124000215a.pdf/div-class-title-phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool-div.pdf` → 200 → same → 638,008
- S922 `https://api.crossref.org/journals?query=constructed+language&rows=20` → 200 → 196; control `…?query=constructed&rows=20` → 200 → 10,823
- S923 `https://api.crossref.org/works/10.1146/annurev-linguistics-030421-064707` → 200 → 12,490

Wayback CDX probes (output=json, filter=statuscode:200):
- `link.springer.com/chapter/10.1007/978-3-032-03277-5_15` → `[]` (no capture)
- `link.springer.com/book/10.1007/978-3-032-03277-5` → `[]` (no capture)
- `philnauki.mgimo.ru/jour/article/viewFile/520/524` → `[]` (no capture; live site serves the PDF)
- `linguistische-treffen.pl/articles/27/24_luba.pdf` → captures exist (e.g., 20250828140835, 20251015182839, all HTTP 200)

## Located quotes (verbatim, <=25 words; `wc -w`)
| quote | words | location |
|---|---|---|
| "insbesondere drei Hauptgruppen unterscheiden: Plansprachen, künstlerische Sprachen" | 7 | S929, printed p. 387, paragraph beginning «Die wesentlichen Unterschiede zwischen ihnen…» |
| "interpretativ, explorativ und konfigu-" | 4 | S929, printed p. 390, video-game functions sentence (hyphen-split across line break) |
| "students created a phonemic inventory informed by world-language inventories and" | 10 | S920, printed p. 310, §1.3 "Institutional and course details" |
| "Constructed languages, also known as conlangs" | 6 | S930, Crossref deposited abstract (opening) |
| "There are four main types of these constructed languages." | 9 | S923, Crossref deposited abstract (opening) |

## Key findings for the Gate
1. **All 10 rows are adopt-candidate = N this round.** None belongs to the two admitted
   theme entries (conlang-scholarship.md + conlang-scholarship.amend-2026-10-23.md), whose
   rows are fixed from staged S881/S882/S892/S893/S901 only. Adopting any of these would
   exceed the two-entry admission, so each is recorded as not adopted (defer), with the
   technical findings below where defects exist.
2. **S910 is NOT an unreachability reject.** The REJECTS leg conditions S910's rejection on
   its payload staying unreachable by ordinary means; the Crossref record (the artifact the
   row was opened as) resolves HTTP 200 and carries every staged span. Only Springer's own
   landing page is bot-challenged (left unpassed per QUALITY 10).
3. **Campaign-id defects confirmed:** S769 (Opie) and S806 (Ayurveda) in the lane registry
   name unrelated documents; both appear as prose citations in 23c/24. They must not appear
   in admitted entries (REPOINTED leg covers the two theme entries; the REST files are
   outside it).
4. **Anchor/location defects to correct if these ever re-stage:** S929 span2 is p. 390 not
   387; S920 span is §1.3 p. 310 not §2.1.2 p. 312; S915's "in law" domain claim is
   unsupported and its query string misspells "Languistics" (still returns the chapters by
   fuzzy ranking).
5. Verified-sound rows deferred (S909, S910, S930, S922, S923) all remain reachable and
   correctly quoted; nothing here blocks the two theme entries.
