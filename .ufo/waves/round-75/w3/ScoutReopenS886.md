# S886 independent re-open (W3)

## Fetch and anchor

- Independently fetched `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120` with `curl -sS -L --compressed ... -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'` on 2026-10-27. Observed HTTP **200**, effective URL unchanged, **109335** downloaded bytes; SHA-256 **8a8e49f53b8dad61572589facc06cbb0620f2343c0a5431ef240c3e60f2825ea**. Response is `text/html;charset=UTF-8`; headers included `Vary: User-Agent`. No challenge observed.
- Evidence record `reports/round-75/evidence/S886.txt:3-6,11-17,23-35` records the same UA, HTTP 200, 109335 bytes, prior whole-body SHA-256 `81f256a9993d240f80513ecb8beaa5e62d524d58225465d27add8b14f25eca7c`, visible chars 3526, whole-document window, prior window SHA-256 `7a7a196451f5cf1f70a3610f1e21609edd2ebe79522cc6a765b7cd60c3027b30`, and `quote-found-verbatim: no` despite folded quote found. **Body hash differs**; byte count is unchanged. Thus the page changed at byte level, but not in size.
- **Quote found: YES**, after NFKC and whitespace folding. Its location in the re-opened page's article notice is immediately after the printed title/author line: `Tzvetan Todorov Les catégories du récit littéraire Étudier la « littérarité » et non la littérature : c'est la formule...`. Evidence window line 35 contains this same anchor, while line 37 stores it as the quote. The recorded window remains applicable and contains the quote; line 17's `quote-found-verbatim: no` is consistent with the distinct folded-match check (line 8 yes), not quote absence.

## Registry audit

`corpus/SOURCES.md:841` gives Tier A, justified by this being a primary structuralist article opened page-by-page, and scopes it to discourse temporality/deformation, narrator/character words, and appreciation levels. This tier and scope **agree** with the document/page-level service and its contents: primary article pages are designated p.125 and p.139, although the independent request here directly re-opened the article notice only, not the transcription pages. The `used-by` cell names exactly `corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md`; the other two entry files do not have S886 in their source lines. Recheck cell is `180d`. The row's locator/quote and page references are consistent with the fetched notice and the stated per-page recheck plan.

## Cited-entry claim audit

Only the amendment `corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` cites S886 as a source (source line 4). The base and `.amend-2026-10-23b.md` do not cite S886 in their source lines. S886-credited content is principally at lines 54, 58, 60, 62 and calibration line 71; line 130 notes a transcription artifact.

The fetched notice itself carries the title, author, bibliographic information, and the opening phrase. It does **not** carry the substantive printed-p.125 definition quote or p.139 argument quoted/cited in this amendment. Those statements are attributed to the article at printed pages 125 and 139, with p.139 listed in the registry's explicit page-transcription service. They are not contradicted by the notice; they remain unverified by this assigned independent *article-URL* reopen. Accordingly, I cannot honestly label any of them unsupported by the article based on this page alone, nor claim that this fetch proves them. The key unsupported-by-this-notice assertions are:

- Line 54: `"Le sens (ou la fonction) d'un élément de l'œuvre, c'est sa possibilité d'entrer en corrélation avec d'autres éléments de cette œuvre et avec l'œuvre entière"` and its interpretation that meaning is relational/correlation-based.
- Line 58: the p.139 time/aspect/mode cut, the quoted definitions of aspect and mode, and time as the relation between story time and discourse time.
- Line 60: the p.139 linear-vs-pluridimensional time quotation; simultaneity/linear discourse explanation; necessity of breaking natural succession; Formalists/deformation quotation and conclusion.
- Line 62: the p.139 disposition-of-events quotation and the claimed verse analogy and two-order murder example.
- Line 71: the characterization that Todorov adopts the Formalist sentence and illustrates it with a 1925 Vygotsky text.

These require direct examination of the named p.125 and p.139 transcription pages to resolve. The notice does not say otherwise: it only has the opening formula and bibliographic notice. Therefore verdict **PARTIAL**: anchor and recorded window survive; body hash changed (same byte length); substantive cited prose is not verified by the requested notice reopen, but no contrary finding is established. No invented claim of mismatch to the primary text.
