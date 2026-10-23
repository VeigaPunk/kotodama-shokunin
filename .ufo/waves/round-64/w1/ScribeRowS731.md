# S731 — Child code-switching

## Behavior and finding
Prepared one mined registry row and matching Section 6 bullet on a primary study's finding that DLD diagnosis did not affect the frequency of intrasentential code-switching in the studied Spanish–English children. The quoted passage is in the Discussion subsection “Code-Switching and Language Proficiency.” The row scope is limited to this diagnosis/frequency relationship in children aged 5–7; the article reports 62 children (24 DLD, 38 typical language development).

Tier A is appropriate only for the scoped topic because this is the original peer-reviewed study reporting its own results, not a secondary account. It does not establish that all bilingual children, languages, ages, settings, or switch types behave alike.

## Gates and checks
- Lane locator was run twice for the same live URL and quote; each returned exactly: `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/`.
- Row structure check: `ROW_FIELDS: 13 ROW_CELLS: 11` (13 pipe-delimited fields including the two edge empties); quote count: 21 words; bullet clause count: 19 words.
- `ACCEPT-C-64` was not run. The locator and structure checks are not acceptance-gate evidence; no gate pass is claimed.
- No source conflict was observed.

## Provenance and exact commands
Searches used these queries:
1. `child code-switching bilingual children peer reviewed study open access`
2. `site:pmc.ncbi.nlm.nih.gov child code-switching bilingual children study`
3. `child bilingual code-switching children university repository paper pdf`

Selected record: Maria Kapantzoglou et al. (2021), “Code-Switching and Language Proficiency in Bilingual Children With and Without Developmental Language Disorder,” *Journal of Speech, Language, and Hearing Research* 64(5): 1605–1620, DOI 10.1044/2020_JSLHR-20-00182; PMC full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/ . The full-text citation gives the journal, volume/issue, pages, and April 2021 date. The exact locator quote is from the article's Discussion text, not its abstract, metadata, or a caption.

Page fetch (outcome: `HTTP_STATUS:200`):
```sh
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731 && curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731/article.html -w 'HTTP_STATUS:%{http_code}\n' 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/'
```

Wayback availability check (outcome: `HTTP_STATUS:200`; `available: true`; snapshot `status: 200`; timestamp `20250424085946`; captured original `https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/`):
```sh
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731 && curl -s --max-time 60 'https://archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/' -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731/capture.json -w 'HTTP_STATUS:%{http_code}\n'
```

The corresponding capture URL recorded in the row is `https://web.archive.org/web/20250424085946id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/`. The live text was opened with ordinary `curl`; it returned HTTP 200, so no challenge or paywall route was needed. The archived page itself was not fetched separately.

Locator command (run twice; both outcomes shown above):
```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/' "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching."
```

Final self-check command and outcomes:
```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/' "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching." && awk -F'|' '/^ROW: / { print "ROW_FIELDS:", NF, "ROW_CELLS:", NF-2 }' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731/row.txt && printf '%s\n' "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching." | wc -w && awk -F' ' '/^BULLET:/ { print "BULLET_WORDS_BEFORE_ID:", NF-2 }' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731/row.txt
```
The final self-check printed the locator line, `ROW_FIELDS: 13 ROW_CELLS: 11`, `21`, and `BULLET_WORDS_BEFORE_ID: 20` (that last display includes the S-id token in its subtraction; the separately counted clause is 19 words).

Separate clause-only bullet count (outcome: `19` words):
```sh
awk '/^BULLET:/ { sub(/^BULLET: - /, ""); sub(/ \\(S731\\)$/, ""); print NF }' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731/row.txt
```

## Touched surfaces and out of scope
- Scratch artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS731/article.html`, `capture.json`, and `row.txt`.
- Requested report: `.ufo/waves/round-64/w1/ScribeRowS731.md`.
- No corpus entry, registry, lane tool, or other product file was edited. No software was installed. The acceptance gate and other claims remain out of scope.

## Artifacts
`row.txt` is the submission artifact with the full ROW, BULLET, VERIFY, CAPTURE, and ACCESS lines. The source and Wayback response are retained in the same scratch directory for provenance.