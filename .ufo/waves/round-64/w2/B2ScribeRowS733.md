# S733 source-row findings

## Outcome and evidence

Completed the S733 row artifact at `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/row.txt`. The selected primary paper is Naomi K. Caselli and Jennie E. Pyers (2017), “The Road to Language Learning Is Not Entirely Iconic: Iconicity, Neighborhood Density, and Frequency Facilitate Acquisition of Sign Language,” *Psychological Science* 28(7). PMC metadata confirms the authors, date, journal, volume, issue, and title.

The paper's abstract reports analysis of 58 parental reports of native-signing deaf children's productive acquisition of 332 ASL signs, with iconicity, neighborhood density, and lexical frequency independently facilitating vocabulary acquisition. The Participants section specifies the final sample's ages (8–35 months), that all had a deaf mother, and all but three had a deaf father. The Discussion quote in the row is a direct primary-study finding. Tier A is justified for this paper's own finding about productive ASL vocabulary acquisition in the defined sample; it is not a blanket claim about all deaf children or all sign languages.

## Row artifact

ROW: | S733 | Caselli & Pyers (2017) "The Road to Language Learning Is Not Entirely Iconic: Iconicity, Neighborhood Density, and Frequency Facilitate Acquisition of Sign Language", Psychological Science 28(7) - https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/ ; capture https://web.archive.org/web/20250222070806id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/ | paper | A | productive ASL vocabulary acquisition by native-signing deaf children with deaf parents (all had deaf mothers) | Discussion: "High phonological neighborhood density and lexical frequency promoted sign acquisition, even after controlling for iconicity." | Lets worldbuilders ground early ASL vocabulary growth in frequency and phonological neighborhoods, alongside iconicity. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Worldbuilders can portray early signed vocabulary growth as shaped by neighborhood density and lexical frequency, not iconicity alone. (S733)
VERIFY: LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/
CAPTURE: timestamp=20250222070806; original=https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/
ACCESS: plain curl -sL, HTTP 200, 2026-10-23

The bullet preserves “neighborhood density and lexical frequency” in the quote's order, adds novel content words, and is one clause with a single terminal S733 identifier. The anchor is 15 words, Discussion body text.

## Gates and limits

- Plain-GET source fetch: HTTP 200, final URL unchanged, 174,943 bytes.
- The requested locator command printed `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/` on the first run and again on the required self-check run.
- Self-check: `awk -F'|'` reported 13 fields (11 row cells); the quote count was 15 words; `row.txt` has exactly five labelled lines.
- The required `archive.org/wayback/available` request returned HTTP content `429 Too Many Requests` on both attempts. A Wayback CDX query did return three same-page captures: `20250202172525`, `20250209153416`, and `20250222070806`, all with original `https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/`. The row uses the last capture. A direct GET of that archived URL failed with curl exit code 7 / HTTP status 000; the archive page was not treated as opened-source evidence. The original PMC page was opened successfully.
- The row-level URL+quote locator was run twice; the round-64 `ACCEPT-C-64` harness and its pinned `--row S733` LIVE leg were not run. This report does not claim that the full predicate passed.

## Commands and observed outcomes

Scratch directory creation:

```sh
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733
```

Source open:

```sh
curl -sL --max-time 60 -w '\nHTTP_STATUS:%{http_code}\nFINAL_URL:%{url_effective}\n' 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/' -o /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/article.html && printf 'FETCHED_BYTES:' && wc -c < /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/article.html && printf 'HTML_PATH:%s\n' '/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/article.html'
```
Observed: `HTTP_STATUS:200`, final URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/`, `FETCHED_BYTES:174943`.

Archive availability attempts:

```sh
curl -s 'https://archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/'
curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fpmc.ncbi.nlm.nih.gov%2Farticles%2FPMC5507709%2F'
```
Both returned an HTML `429 Too Many Requests` response.

Capture lookup:

```sh
curl -s --max-time 60 'https://web.archive.org/cdx/search/cdx?url=pmc.ncbi.nlm.nih.gov%2Farticles%2FPMC5507709%2F&output=json&filter=statuscode:200&fl=timestamp,original&collapse=digest'
```
Observed three timestamp/original records listed above. Direct capture retrieval was attempted with:

```sh
curl -sL --max-time 60 -w '\nHTTP_STATUS:%{http_code}\nFINAL_URL:%{url_effective}\n' -o /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/archive.html 'https://web.archive.org/web/20250222070806id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/' && printf 'ARCHIVE_BYTES:' && wc -c < /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/archive.html
```
Observed: status `000`, curl exit code 7; final URL remained the archive URL.

Locator (executed twice, first run and final self-check):

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/' 'High phonological neighborhood density and lexical frequency promoted sign acquisition, even after controlling for iconicity.'
```
Each run printed `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/`.

Row/quote self-check:

```sh
awk -F'|' 'NR==1 {print "ROW_FIELDS:" NF; print "ROW_CELLS:" NF-2}' /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/row.txt && python3 -c "from pathlib import Path; import re; s=Path('/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/row.txt').read_text(); q=re.search(r'Discussion: \\\"([^\\\"]+)\\\"', s).group(1); print('QUOTE_WORDS:', len(q.split())); print('LINES:', len(s.splitlines()))"
```
Observed: `ROW_FIELDS:13`, `ROW_CELLS:11`, `QUOTE_WORDS: 15`, `LINES: 5`.

## Touched surfaces and boundaries

- Created scratch artifact `.../ScribeRowS733/row.txt`; downloaded source HTML to `.../ScribeRowS733/article.html`; attempted archive download to `.../ScribeRowS733/archive.html` (failed as reported).
- Wrote this requested report at `.ufo/waves/round-64/w2/B2ScribeRowS733.md`.
- No corpus entry, registry row, product code, judge, Git index, or lane state was changed. No tool was installed. No acceptance harness/build/test was run.
- Out of scope: integrating S733 into `corpus/SOURCES.md` or the knowledge entry, and asserting the full claim-C predicate.

## Artifact paths

- Row artifact: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/row.txt`
- Opened-source copy: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS733/article.html`
- Scoped report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w2/B2ScribeRowS733.md`
