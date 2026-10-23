# Falsification review — S724

Draft: /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/row.txt
Source: Essentials of Linguistics, 2nd ed., ch. "11.7 Syntax in early utterances"
(eCampusOntario Pressbooks)

## HTTP results (verbatim)
- `LIVE 403 https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/` — curl default UA, body = CloudFront "403 ERROR / Request blocked" (919 B).
- `LIVE 200 https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/` — plain GET with desktop User-Agent (Firefox/131.0), 142861 B body.
- `CAPTURE 000 https://web.archive.org/web/20260418200819id_/…` on first attempt (TCP connect refused to web.archive.org:443); `CAPTURE try1 200` on retry in the same run, 143477 B body.
- Wayback availability API (archive.org, HTTP 200): closest = `status 200`, `timestamp 20260418200819`, original = the live URL — matches the row's capture cell.

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| live URL | https://ecampusontario.pressbooks.pub/…/11-7-syntax-in-early-utterances/ | YES | 200 on plain GET with ordinary UA; 403 only for curl's default `curl/…` UA | none |
| capture | web.archive.org/web/20260418200819id_/… | YES | 200 fetch of the exact capture URL; availability API confirms timestamp 20260418200819 / same original | none |
| anchor quote | "containing mostly content words like nouns and verbs, with few function words and few inflectional morphemes." | YES | verbatim contiguous hit in body text (normalised 16 words, within 8–25). Context: "…most children start to combine words into phrases of two or even three words. At this early stage, their utterances are usually telegraphic [1], containing mostly content words like nouns and verbs, with few function words and few inflectional morphemes. It can be hard to figure out whether these short utterances have any syntactic structure…" — main prose paragraph, not caption/nav/attribute | none |
| locator claim | "opening paragraph" | YES | quote sits in the first paragraph of body prose directly under the `<h1 class="entry-title"> 11.7 Syntax in early utterances` | none |
| lane locator | LOCATED | YES | `python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'` → `LOCATED https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/` | none |
| citation | Catherine Anderson et al., 2022, "11.7 Syntax in early utterances", Essentials of Linguistics, 2nd edition | YES | page `<title>` = "11.7 Syntax in early utterances – Essentials of Linguistics, 2nd edition"; schema authors "Catherine Anderson; Bronwyn Bjorkman; Derek Denis; Julianne Doner; Margaret Grant; Nathan Sanders; and Ai Taniguchi"; datePublished 2022; Anderson is lead → "Anderson et al., 2022" correct | none |
| kind | book | YES | Pressbooks open textbook | none |
| tier | B | YES (for scope) | open introductory textbook — canonical "strong secondary" for scope "early developmental linguistics: telegraphic speech in children's first multiword utterances"; textbook is not the primary research record, so B (not A) is correct | none |
| scope | early developmental linguistics: telegraphic speech in children's first multiword utterances | YES | page prose: "their utterances are usually telegraphic" + the quote — exact topic match | none |
| teaches | worldbuilders write plausible early child dialogue with content-word-heavy phrases and sparse inflectional marking | YES | consistent with quote + telegraphic context; no invented entity/number | none |
| BULLET (RESTATE) | "Early child phrases favor content words like nouns and verbs but carry fewer inflectional morphemes, shaping terse dialogue" | YES | clause shape `^- (.*) \(S724\)$` OK; 16 content words (≥5); 7 in-order quote words (≥3); novel content words incl. favor/terse/dialogue; longest verbatim copied run = 6 words "content words like nouns and verbs" (≤12). Semantics: "favor content words… fewer inflectional morphemes" restates the quote faithfully; "shaping terse dialogue" is mild applied inference consistent with the telegram gloss (pay per word → few words); no overreach | none |
| shape | 11 cells; tier B; status mined; opened 2026-10-23; recheck 180d; used-by corpus/knowledge/linguistics/language-socialization-and-acquisition.md | YES | draft cell-by-cell re-check | none |
| ACCESS note | live GET 403, capture 200 | YES (accurate) | reproduces exactly: curl-default 403, browser-UA 200, capture 200 | none |

VERDICT: CLEAN every row field verified verbatim against a 200 live fetch and a 200 same-page archive capture; bullet passes RESTATE with no overreach.
