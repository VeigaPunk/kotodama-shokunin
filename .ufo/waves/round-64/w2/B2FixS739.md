# S739 row repair

## Behavior and gates
- Replaced the inherited section-title anchor with a body sentence from the article's Introduction; retained the same paper, live URL, and archived capture.
- Rewrote the entry bullet. Its content words preserve `parents → various → terms → address → children → contexts` from the quote, and include novel content words.
- Required locator command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf' 'Parents can use various terms of address to children depending on situational contexts.'`
- Outcome: `LOCATED https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf`.
- Counter criteria inspected in `reports/round-64/accept-c.py` (ROWS and RESTATE); `accept-c.py` itself was not run. Manual shape/content review: row has 11 cells; quote has 13 normalized words; bullet has 13 content words, six in-order quote-content matches, seven novel content words, and a longest copied run of five normalized words. These are not a claim that the full C predicate passed.

## Corrected deliverable
ROW: | S739 | Wira Kurniawati, Suhandano, and Bernadette Kushartanti (2021), *Language Socialization in Family Environments Through Terms of Address to Children*, LITERA, 20(2), 250–268 - https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf ; capture https://web.archive.org/web/20240911000056id_/https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf | paper | A | parental use of address terms with children in urban Sleman, Indonesia | introduction, paragraph beginning According to Aledo (2018): "Parents can use various terms of address to children depending on situational contexts." | Helps worldbuilders model how caregivers vary terms of address across situations as children learn community language practices. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Parents use various terms of address with children across changing contexts, shaping culturally situated family communication. (S739)
VERIFY: LOCATED https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf
CAPTURE: timestamp=20240911000056; original=https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf
ACCESS: Live PDF and archived PDF opened; CDX lists timestamp 20240911000056 with identical original URL and status 200/application/pdf. Availability API request returned 429 Too Many Requests.

## Provenance and limits
- The inherited S739 draft was treated as unverified. The live PDF was opened via the static reader and the exact sentence was present in the Introduction; the same archived PDF URL also opened. A CDX query for the PDF returned three status-200 `application/pdf` records, including `20240911000056` with the same original URL.
- Exact archive availability request: `curl -s 'https://archive.org/wayback/available?url=https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf'` → `429 Too Many Requests`. The direct archived PDF and CDX evidence supplied the capture check; no challenge was passed or bypassed.
- Out of scope: no registry or knowledge-entry edit, no lane acceptance run, and no lane Git/jj/index mutation. No tools were installed.

## Touched surfaces
- `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS739/row.txt`
- `.ufo/waves/round-64/w2/B2FixS739.md`
