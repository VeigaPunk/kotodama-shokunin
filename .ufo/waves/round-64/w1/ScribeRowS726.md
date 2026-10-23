# S726 — claim C source finding

## Finding
- **Source:** Ochs, Elinor & Schieffelin, Bambi B. (1982), *Language Acquisition and Socialization: Three Developmental Stories and Their Implications*, Sociolinguistic Working Paper No. 105; official ERIC record `https://eric.ed.gov/?id=ED252065`.
- **Tier A:** This is the original report by the two foundational authors and the official ERIC record for that report; the quoted abstract directly states the language-acquisition/social-membership relationship in scope.
- **Capture:** `timestamp=20240914111851`; `original=https://eric.ed.gov/?id=ED252065`; archive URL is `https://web.archive.org/web/20240914111851id_/https://eric.ed.gov/?id=ED252065` (availability API reported status 200).
- **Access:** Plain curl GET of the ERIC record returned HTTP 200 on 2026-10-23.

## Submitted row artifact
`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS726/row.txt`

ROW: | S726 | Ochs, Elinor & Schieffelin, Bambi B., 1982 "Language Acquisition and Socialization: Three Developmental Stories and Their Implications", Sociolinguistic Working Paper No. 105 - https://eric.ed.gov/?id=ED252065 ; capture https://web.archive.org/web/20240914111851id_/https://eric.ed.gov/?id=ED252065 | paper | A | Ochs and Schieffelin's foundational language acquisition/socialization paradigm | ERIC record abstract, numbered claim (1): "the process of acquiring language is deeply affected by the process of becoming a competent member of a society" | Helps learners connect speech development to the social roles of joining a community | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - The process of acquiring language is linked to social membership, giving worldbuilders community-based learner arcs. (S726)
VERIFY: LOCATED https://eric.ed.gov/?id=ED252065
CAPTURE: timestamp=20240914111851; original=https://eric.ed.gov/?id=ED252065
ACCESS: plain curl GET, HTTP 200, 2026-10-23

## Gates and provenance
- The final lane locator run printed exactly `LOCATED https://eric.ed.gov/?id=ED252065`.
- Row self-check: `awk -F'|'` counted 13 fields (11 cells plus the label/trailing empty fields); quote count 19 words; bullet clause count 15 words.
- Source search queries included `language socialization Ochs Schieffelin paradigm original article`, `Ochs Schieffelin "language socialization" 1984 "Language acquisition and socialization"`, and searches for open-access Ochs/Schieffelin repository texts. ERIC identifies the report as non-journal, published 1982-Nov, 83 pages, and lists Ochs and Schieffelin as authors.

## Commands and observed outcomes
- `curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS726/ochs-schieffelin-1982.pdf -w 'HTTP_STATUS:%{http_code} FINAL_URL:%{url_effective} CONTENT_TYPE:%{content_type}\n' 'https://files.eric.ed.gov/fulltext/ED252065.pdf'` → `HTTP_STATUS:200 FINAL_URL:https://files.eric.ed.gov/fulltext/ED252065.pdf CONTENT_TYPE:application/pdf`.
- `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Ffiles.eric.ed.gov%2Ffulltext%2FED252065.pdf'` → no archived snapshots.
- `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://files.eric.ed.gov/fulltext/ED252065.pdf' 'the process of acquiring language is deeply affected by the process of becoming a competent member of a society'` → `NOT_LOCATED https://files.eric.ed.gov/fulltext/ED252065.pdf quote-absent` (exit 1).
- `curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS726/eric-record.html -w 'HTTP_STATUS:%{http_code} FINAL_URL:%{url_effective} CONTENT_TYPE:%{content_type}\n' 'https://eric.ed.gov/?id=ED252065'` → `HTTP_STATUS:200 FINAL_URL:https://eric.ed.gov/?id=ED252065 CONTENT_TYPE:text/html; charset=utf-8`.
- `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Feric.ed.gov%2F%3Fid%3DED252065'` → available snapshot, status `200`, timestamp `20240914111851`, original `https://eric.ed.gov/?id=ED252065`.
- Locator on the ERIC record with the exact row quote returned `LOCATED https://eric.ed.gov/?id=ED252065`; the required final self-check repeated that same command and result.
- Row count command: `awk -F'|' 'NR==1 {print "ROW_FIELDS:" NF; q=$7; sub(/^[^"]*"/,"",q); sub(/".*$/,"",q); n=split(q,w," "); print "QUOTE_WORDS:" n} NR==2 {b=$0; sub(/^BULLET: - /,"",b); sub(/ \(S726\)$/,"",b); print "BULLET_WORDS:" split(b,w," ")}' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS726/row.txt` → `ROW_FIELDS:13`, `QUOTE_WORDS:19`, `BULLET_WORDS:15`.

## Surfaces, limits, and scope
- Scratch artifacts: `row.txt`, `ochs-schieffelin-1982.pdf`, and `eric-record.html` under `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS726/`.
- This report is the only lane-repository file written. No product code, registry, entry, judge, or other lane surface was changed; no build/test or C-64 acceptance suite was run.
- The direct PDF GET succeeded, but the lane locator could not extract the quote from that PDF (`quote-absent`). The row therefore anchors the exact abstract wording on the official ERIC record, not extracted PDF body text. The PDF itself had no Wayback snapshot; the selected ERIC record does.
- No tools were installed or updated. No other claim or acceptance gate is asserted here.