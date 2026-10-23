# S724 — sourced row handoff

## Axes and finding
- **Coverage:** one mined S724 row for Section 2, telegraphic speech / early multiword utterances.
- **Source fit:** an open textbook chapter directly states the age range, typical 2–3-word phrases, and relative scarcity of function words and inflectional morphemes.
- **Auditability:** source metadata, captured page, quotation locator, row shape, and word counts are recorded below.

## Row artifact
`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/row.txt`

ROW: | S724 | Catherine Anderson et al., 2022 "11.7 Syntax in early utterances", Essentials of Linguistics, 2nd edition - https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/ ; capture https://web.archive.org/web/20260418200819id_/https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/ | book | B | early developmental linguistics: telegraphic speech in children's first multiword utterances | opening paragraph: "containing mostly content words like nouns and verbs, with few function words and few inflectional morphemes." | Helps worldbuilders write plausible early child dialogue with content-word-heavy phrases and sparse inflectional marking. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |

BULLET: - Early child phrases favor content words like nouns and verbs but carry fewer inflectional morphemes, shaping terse dialogue (S724)

VERIFY: LOCATED https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/

## Tier and provenance
Tier **B**: this is a textbook chapter (strong secondary synthesis), not an original child-language study or primary dataset. Its scope here is the textbook's general description of early telegraphic utterances. The captured chapter identifies *Essentials of Linguistics, 2nd edition*, copyright 2022, and names Catherine Anderson, Bronwyn Bjorkman, Derek Denis, Julianne Doner, Margaret Grant, Nathan Sanders, and Ai Taniguchi as authors. The quote is in the opening body paragraph (captured HTML line 241).

Wayback availability returned `timestamp=20260418200819` and the original URL `https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/`; the capture URL in the row uses the required `id_` form.

## Gates and checks
- Web search query: `telegraphic speech early multiword utterances children linguistics textbook encyclopedia`. The initial result was the NOVA-hosted copy of this chapter; its metadata identified the underlying eCampusOntario *Essentials of Linguistics* chapter, which was selected as the source.
- Wayback availability request: `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fecampusontario.pressbooks.pub%2Fessentialsoflinguistics2%2Fchapter%2F11-7-syntax-in-early-utterances%2F'` — available snapshot, timestamp above.
- Original live GET: `curl --compressed -sL --max-time 60 -D /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/original.headers -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/original.html -w 'HTTP_STATUS:%{http_code}\\nCONTENT_TYPE:%{content_type}\\nSIZE:%{size_download}\\n' 'https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/'` — `HTTP_STATUS:403`, `CONTENT_TYPE:text/html`, `SIZE:919`.
- Opened the archived original via ordinary GET: `curl --compressed -sL --max-time 60 -D /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/original-archive.headers -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/original-archive.html -w 'HTTP_STATUS:%{http_code}\\nCONTENT_TYPE:%{content_type}\\nSIZE:%{size_download}\\n' 'https://web.archive.org/web/20260418200819id_/https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/'` — `HTTP_STATUS:200`, `CONTENT_TYPE:text/html; charset=UTF-8`, `SIZE:36953`.
- Lane locator was run twice from `/home/vgpnk/Projects/shokunin/kotodama-shokunin` with `python3 -B reports/round-61/reopen-quote.py 'https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/' 'containing mostly content words like nouns and verbs, with few function words and few inflectional morphemes.'`; both runs printed exactly the VERIFY line above.
- `awk -F'|' 'NR==1 {print "ROW_FIELDS=" NF}' .../row.txt` returned `ROW_FIELDS=13` (11 cells plus the two boundary fields). Quote word count: 16. Bullet clause word count: 18.
- **Not run:** `ACCEPT-C-64`; this is a single-row handoff, not evidence that the full claim predicate passes.

## Conflicting access evidence (verbatim)
The direct plain GET returned `HTTP_STATUS:403` (also `CONTENT_TYPE:text/html`, `SIZE:919`), while both locator runs on that live URL printed:

`LOCATED https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/`

The quotation was opened and read from the archived copy, which returned HTTP 200. The origin 403 was not routed around; an existing public archive capture was used.

## Surfaces and limits
- Written: this scoped report and `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/row.txt` only.
- Source/access artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/original-archive.html`, `original-archive.headers`, `original.html`, and `original.headers`. Exploratory NOVA-copy artifacts: `archive.html` and `archive.headers` in the same scratch directory.
- No registry or corpus-entry edit, no product-code edit, no acceptance-script run, no test run, and no tool installation. The L1 must integrate the row and run the applicable claim gate.
