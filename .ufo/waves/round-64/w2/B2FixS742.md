# S742 row repair findings

## Behavior and gate
- Replaced the three-word section-heading anchor with the full p. 48 body sentence: `Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other.` It is 23 normalized words and is verbatim in the reopened source PDF.
- The revised bullet is `- Morning greetings teach students to expect peer welcome as a shared classroom practice. (S742)`. It has ten content words; `morning`, `greetings`, and `students` occur in that order in the quote; `teach` is novel; no copied run exceeds 12 words.
- The ROW retains the original source, tier A, `mined`, opened date, 180d recheck, used-by path, and capture URL. The quote field no longer puts a quoted section heading before the anchor sentence.

## Exact locator command and outcome
`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://files.eric.ed.gov/fulltext/EJ1271032.pdf' 'Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other.'`

Output: `LOCATED https://files.eric.ed.gov/fulltext/EJ1271032.pdf`

## Evidence and limits
- Independently opened the live PDF through the read URL and observed the quoted sentence under p. 48, “Morning Meeting Greetings.” Reopened the inherited same-page archive URL and observed the same PDF content.
- Attempted `curl -s 'https://archive.org/wayback/available?url=https://files.eric.ed.gov/fulltext/EJ1271032.pdf'`; outcome was HTTP 429 Too Many Requests. The capture timestamp/original below were retained from the inherited row; the archived capture itself was opened successfully.
- Read the `ROWS`/`RESTATE` rules in `reports/round-64/accept-c.py`; did not run the overall acceptance checker. The locator above is the only executed lane command.

## Corrected lines
ROW: | S742 | Shields-Lysiak, Boyd, Iorio Jr., and Vasquez (2020) "Classroom Greetings: More than a Simple Hello", Iranian Journal of Language Teaching Research 8(3), 41–56 - https://files.eric.ed.gov/fulltext/EJ1271032.pdf ; capture https://web.archive.org/web/20250403232101id_/https://files.eric.ed.gov/fulltext/EJ1271032.pdf | paper | A | explicitly taught ritualized greeting routines in one second-grade classroom | p. 48, section Morning Meeting Greetings: "Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other." | Gives worldbuilders a repeatable way to design explicit greeting instruction that builds peer welcome and shared classroom belonging. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Morning greetings teach students to expect peer welcome as a shared classroom practice. (S742)
VERIFY: LOCATED https://files.eric.ed.gov/fulltext/EJ1271032.pdf
CAPTURE: timestamp: 20250403232101; original: https://files.eric.ed.gov/fulltext/EJ1271032.pdf
ACCESS: Opened the live PDF and same-page archived PDF as PDF content on 2026-10-23; Wayback availability API returned HTTP 429.

## Touched surfaces and scope
- Wrote scratch artifact `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS742/row.txt` and this scoped report at `.ufo/waves/round-64/w2/B2FixS742.md`.
- No product code, registry, knowledge entry, other rows, or lane Git/jj state was changed. No tools were installed.
