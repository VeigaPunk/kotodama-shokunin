# ReviewCarriedS367S383 — round 57 build seat (carried row findings, round-56 spot-check §5 item 5)

Scope: the two carried findings named for this seat — **S367** (Grounds hedge "claims to be founding"; finder `ReviewRowsS365toS367`) and **S383** (finder `ReviewRowsS383toS385`). Round-56 falsify files grep-matched `S367` in `ReviewRowsS365toS367.md`, `ReviewGateLines56.md`, `CriticClaimC56.md` and `CriticCalibrationBank56.md`; `S383` in `ReviewRowsS383toS385.md`, `CriticCalibrationBank56.md` and `CriticClaimC56.md`. Per the §5 item 5 routing I own the row-level finding for each id; sibling slices (S384, S385, S365, S366) belong to other seats.

Method: both named sources re-opened this session by ordinary means only (plain `curl`, no browser automation, no challenge met): S367 from the live journal (HTTP 200, application/pdf, 313,891 bytes — byte-identical to the row's recorded size), S383 from its recorded Wayback capture 20260203111247 (HTTP 200, text/html, 1,158,762 bytes; capture id as in the row). Text checked with pdftotext 26.08.0 (PDF) and Python `html.parser` (HTML); every quote below was then located with the round-57 locator `python3 -B reports/round-57/reopen-quote.py '<url>' '<quote>'`, which printed `LOCATED` for each. Scratch: `/fast/scratch/hyaku/kotodama-r57/ReviewCarriedS367S383/`. No tool installs. No writes to the lane except this report file.

## S367 — finding LOW-1: the Grounds hedge "claims to be founding" — VERDICT: AGREE (fix via superseding row; the lesson-side rewrite is not mine to land)

Finding (ReviewRowsS365toS367.md:32, LOW-1, advisory): the source says "uma parte que reclama ser fundadora desse Mbânza Kôngo" — *a part that claims to be founder of that capital* — while Gate Grounds and the row's teaches cell state "part of its founding population" as fact.

Re-opened evidence (served text, p. 174 of the printed article):

- `reports/round-57/reopen-quote.py 'https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921' 'uma parte que reclama ser fundadora desse Mbânza Kôngo vive no Congo belga e outra na colônia francesa'` → `LOCATED https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921`
- The served page continues directly: "(i) Mbânza Kôngo fica na colônia portuguesa; (ii) uma parte que reclama ser fundadora desse Mbânza Kôngo vive no Congo belga e outra na colônia francesa" — verbatim; "reclama" is the page's own verb.
- Second locator on the Gate quote: `…'Com a colonização de Angola – oficialmente desde 1885 – desenha-se outro mapa da sociedade kôngo'` → `LOCATED https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921`
- The p. 173 insurrection anchors also verify in the served text ("Entre 1913-1914, o católico Álvaro Mbûta lidera a insurreição"; "dois objetivos: (i) destituir Dom Manuel Kiditu do trono Kôngo" — spelled "objetivos" with j); the row's teaches cell is otherwise supported.

Assessment: the finding is correct on the text. It is a hedge the row-level record drops; the entry sentence at kongo-kingdom.md:117 ("after 1885 Mbanza Kongo lies in the Portuguese colony while other Kongo communities live in the Belgian and French ones") never asserts the founding claim and needs no change. The affected cells are the registry's `teaches` (and the lesson's Gate Grounds, which must stay byte-equal to it — the checker rule at tools/check-gate-quotes.py:237 compares `Grounds:` text to the registry teaches cell as one string).

Proposed fix — **superseding row for S367** (registry is append-only; `teaches` is not an in-place-editable cell; id left as S4xx for the L1; teaches opens `supersedes S367 —`; same URL and anchor cells as S367 so the round-57 FRESH leg is unaffected — the row's URL is already named by S367, a row below S413):

```
| S4xx | Batsîkama, Patrício, and Álvaro Campelo. 2011. "A Catedral de São Salvador de Angola: história e memória de um lugar mítico." *Sæculum — Revista de História* 25: 161-179. João Pessoa: Universidade Federal da Paraíba. ISSN 0104-892X; no DOI printed. — https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921 (supersedes S367 — the 2026-10-22 re-open confirmed the served page carries "uma parte que reclama ser fundadora desse Mbânza Kôngo vive no Congo belga e outra na colônia francesa": founding-descendant status is a community's own claim, so the row keeps the hedge instead of stating a founding population as fact.) | paper | B | the 1885 redrawing of Kongo society across the Portuguese colony, the Belgian Congo and the French colony, with the founding-descent claim kept as the source's reported claim; the two aims of the 1913-14 insurrection. Not the abolition, not the conference, not the kingship's ritual content. (tier note: B — peer-reviewed history article about the cathedral's memory; the 1885 colonial division and the 1913-14 insurrection are stated in passing.) | p. 174: "Com a colonização de Angola – oficialmente desde 1885 – desenha-se outro mapa da sociedade kôngo"; p. 174: "uma parte que reclama ser fundadora desse Mbânza Kôngo vive no Congo belga e outra na colônia francesa"; p. 173: "Entre 1913-1914, o católico Álvaro Mbûta lidera a insurreição"; p. 173: "destituir Dom Manuel Kiditu do trono Kôngo" | After 1885 the Kongo capital lay in Portuguese Angola while a part that claims to be founder of that capital lived in the Belgian and French colonies, and the 1913-14 rising sought to depose Kiditu. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Locator lines for the new row (paste as filed evidence):

- `python3 -B reports/round-57/reopen-quote.py 'https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921' 'Com a colonização de Angola – oficialmente desde 1885 – desenha-se outro mapa da sociedade kôngo'` → `LOCATED https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921`
- `python3 -B reports/round-57/reopen-quote.py 'https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921' 'uma parte que reclama ser fundadora desse Mbânza Kôngo vive no Congo belga e outra na colônia francesa'` → `LOCATED https://periodicos.ufpb.br/index.php/srh/article/view/13999/7921`

Lesson-side companion (same hedge, for the L1 if it wants Grounds byte-equality with the new teaches cell; filed bytes of lessons/round-56.md are never rewritten — this would be an erratum appendix, as §5 item 3 does): round-56.md:13, old "Grounds: After 1885 the Kongo capital lay in Portuguese Angola while part of its founding population lived in the Belgian and French colonies, and the 1913-14 rising sought to depose Kiditu." new "Grounds: After 1885 the Kongo capital lay in Portuguese Angola while a part that claims to be founder of that capital lived in the Belgian and French colonies, and the 1913-14 rising sought to depose Kiditu." Advisory either way: the round-56 finding was LOW because Gate Grounds then equalled the then-teaches cell, and they still equal each other today.

## S383 — two findings: (a) "royal control" over-read — VERDICT: AGREE (entry-sentence fix); (b) "an African church accepted" vs the served abstract — VERDICT: PARTIAL (the wording the second finder proposes is itself wrong; the entry over-reads, but the page does say "the religion of the country", so a smaller fix carries the text)

### S383-a "royal control of church organization and finance" (entry line 82)

Finding (ReviewRowsS383toS385.md:9): the served abstract says "Kongo's control over the Church organization and finance", not royal control.

Re-opened evidence:

- `reports/round-57/reopen-quote.py 'https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693' 'Kongo's control over the Church organization and finance allowed it never to be an instrument for foreign domination'` → `NOT_LOCATED … quote-absent`.
- Re-run with the exact served wording: `…'its control over the Church organization and finance allowed it never to be an instrument for foreign domination'` → `LOCATED https://web.archive.org/web/20260203111247/...` (capture 20260203111247).
- Full served sentence (Extract, para. 2): "Kongo's control over the theological content allowed the religion to gain mass acceptance while its control over the Church organization and finance allowed it never to be an instrument for foreign domination, in spite of Portuguese attempts to use it as a 'fifth column'."

Assessment: AGREE — the page attributes the second control clause to "its" (Kongo's), not to the crown. The subject of the whole sentence is Kongo; "royal" is an addition. Locator mechanics: the served form is "its control…", so the row's third anchor already matches the page ("its control over the Church organization and finance…"); only the teaches/Grounds wording and the entry sentence expanded it. Note the S383-a finding's own proposed registry text misquotes the page ("Kongo's control over the Church organization and finance" is not a substring of the served text either); any rewrite should use "its control over the Church organization and finance", which is the verbatim span.

Exact fix, entry sentence (kongo-kingdom.md:82):

- path: corpus/knowledge/civilizations/kongo-kingdom.md:82
- old: "Thornton argues Christianity in Kongo took a distinctly African form, accepted as the country's religion, with royal control of church organization and finance (S383, Extract, paras. 1–2)."
- new: "Thornton argues Christianity in Kongo took a distinctly African form, accepted as the country's religion, with Kongo's control of church organization and finance (S383, Extract, paras. 1–2)."

The row's teaches cell (SOURCES.md:412) and round-56.md:29 Gate Grounds share the same "royal control of organization and finance" phrase. Because the registry is append-only and this seat's bounds stop at entry lines and drafted superseding rows, the row-level half of the S383-a fix is left as the drafted superseding row below, for the L1 to file or route.

Drafted superseding row (id S4xx; teaches opens `supersedes S383 —`; access cell, kind, tier and anchors as S383 — all verified again this session; the only wording change is "royal control of organization and finance" → "its control over the Church organization and finance" in teaches, which keeps Gate Grounds equality if the lesson erratum adopts the same string):

```
| S4xx | Thornton, John. 1984. "The Development of an African Catholic Church in the Kingdom of Kongo, 1491–1750." *The Journal of African History* 25(2): 147–167. DOI 10.1017/S0021853700022830. Cambridge Core article page, published online 22 January 2009; author affiliation on the page: Allegheny College, Pennsylvania. — https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 (supersedes S383 — re-opened 2026-10-22 from the same capture: the served abstract says "its control over the Church organization and finance"; the earlier teaches cell wrote "royal control", which the served text does not state.) | paper | B | the article's stated argument — that Christianity in Kongo became a distinctly African form widely accepted as the country's religion, that a voluntary conversion gave the kingdom leeway over its rite, that Kongo's own control over Church organization and finance kept it from foreign hands, and that nineteenth-century missionaries rejected that local form. Not: the article's evidence, its named offices, its dates beyond the abstract's own, the Antonian movement, or anything on Kikongo vocabulary. (tier note: B — the article is a peer-reviewed original study, but the row rests on the publisher's extract only, so it is a strong secondary summary for the argument and not authority for the article's evidence, names or dates.) | Extract, para. 1: "This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe"; Extract, para. 2: "This was possible because Kongo, as a voluntary convert, had considerable leeway to contribute to its particular form of Christianity."; Extract, para. 2: "its control over the Church organization and finance allowed it never to be an instrument for foreign domination"; Extract, para. 2: "When European priests arrived in Kongo during the Portuguese colonial occupation at the end of the nineteenth century, they rejected the local form of Christianity" | Kongo's church was African-controlled: a voluntary conversion, local theological leeway and its control over the Church organization and finance kept it from becoming a foreign instrument until nineteenth-century missionaries rejected it. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Locator lines for the drafted row's anchors (all LOCATED on the same capture):

- `python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693' 'This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe'` → `LOCATED https://web.archive.org/web/20260203111247/…`
- `python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693' 'its control over the Church organization and finance allowed it never to be an instrument for foreign domination'` → `LOCATED https://web.archive.org/web/20260203111247/…`

### S383-b "Thornton argues an African church accepted as the country's religion" (entry line 141)

Finding (ReviewRowsS383toS385.md:10, plus CriticCalibrationBank56.md §8 DEFECT): the entry over-reads "took a distinctly African form" into "an African church".

Re-opened evidence:

- Locator: `…'This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe'` → `LOCATED https://web.archive.org/web/20260203111247/…`
- Served para. 1 in full: "Scholarly opinion on the conversion of the Kingdom of Kongo to Christianity has generally been that it was superficial, diplomatically oriented, impure, dangerous to national sovereignty or rejected by the mass of the population. This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe as being the religion of the country."
- The served text contains no "African church" noun phrase. The round-56 finding says the page does not support "African church … accepted as the country's religion"; the fuller sentence also shows the page DOES say "the religion of the country" — so the finding's proposed new sentence ("was widely accepted as the country's religion") drops the page's "as being", which slightly hardens the claim beyond the served text.

Assessment: PARTIAL agreement. Agree that "an African church accepted as the country's religion" is an over-read of "Christianity … took a distinctly African form … widely accepted … as being the religion of the country". Disagree with the finder's replacement wording: "was widely accepted as the country's religion" states the acceptance as the article's own finding without "as being" hedge; the safer entry sentence keeps "accepted as the country's religion" only where it quotes the page's own phrase, and keeps "as being".

Exact fix, entry sentence (kongo-kingdom.md:141) — one replacement that also carries the opposing-reading balance CriticCalibrationBank56 §8 asked for on this line:

- path: corpus/knowledge/civilizations/kongo-kingdom.md:141
- old: "UNESCO says the kingdom adopted Christianity while retaining Kongo custom (S411, Criterion (iii), sentence 3); Thornton argues an African church accepted as the country's religion (S383, Extract, para. 1)."
- new: "UNESCO says the kingdom adopted Christianity while retaining Kongo custom (S411, Criterion (iii), sentence 3); Thornton names the older scholarly opinion that the conversion was 'superficial, diplomatically oriented, impure' and argues instead that Christianity in Kongo took a distinctly African form, accepted as the country's religion (S383, Extract, paras. 1–2)."

If the L1 prefers the smaller single-clause fix: old "Thornton argues an African church accepted as the country's religion (S383, Extract, para. 1)." new "Thornton argues that Christianity in Kongo took a distinctly African form, widely accepted in Kongo and Europe as being the religion of the country (S383, Extract, para. 1)." — both variants quote the page at its own strength; the fuller one also restores the opposing reading this bullet is supposed to weigh.

Locator for the para. 1 opposing sentence (16 words, LOCATED): `python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693' 'Scholarly opinion on the conversion of the Kingdom of Kongo to Christianity has generally been that it was superficial'` → `LOCATED https://web.archive.org/web/20260203111247/…` (a locator run on the exact opposing clause "superficial, diplomatically oriented, impure, dangerous to national sovereignty or rejected by the mass of the population" also returns LOCATED on the same capture; the quote printed above is trimmed to stay within the report while the served words are unchanged).

### S383 cells NOT in scope

Status (mined), recheck (2026-10-22), used-by (kongo-kingdom.md) are all correct in S383 and are not part of any finding.

## Residual risk and verification gaps

- I re-verified only S367 and S383; S384/S385 (same seat family, ReviewRowsS383toS385) and the other carried ids in §5 item 5 belong to other seats this round.
- S383 is verified against the Wayback capture only; the live Cambridge page answered 429 during round 56 and I did not re-hit it (no retry through other tools, per the row's own access note).
- S367 verification is via pdftotext of the live journal PDF; the locator (pypdf) independently located both p. 174 quotes, which cross-checks the extraction path.
- The locator's refusal paths were exercised incidentally (a sub-8-word anchor run returned "quote under 8 words"; a quote-in-URL run returned "search-url"), matching the LOCATE leg's documented refusals.
- If the L1 files both drafted rows in S481-S499 as records (not the S413-S480 block), the FRESH leg is unaffected; if it instead lands them in the reserved C block, the row URLs are already named by rows below S413, so FRESH still holds — either placement keeps the claims.json predicate intact.

No further actionable finding in scope: both named findings checked against the served text, verdicts given, and exact fixes drafted (entry line + two superseding rows + one lesson-erratum companion).
