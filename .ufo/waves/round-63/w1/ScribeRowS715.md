# ScribeRowS715 — Round 63

**Disposition: partial; no acceptable S715 row is ready to integrate.** The Smithsonian live-page quote locates, and its archived copy visibly contains the same body-text quote, but the required locator did not locate it in the capture. The required dual-URL source check is therefore incomplete. Candidate artifacts are explicitly marked DRAFT ONLY; do not append them as an accepted row.

## Behavior

This seat performed source research and drafted the three requested S715 artifacts only. No product code or corpus file was changed. The source candidate is the Smithsonian National Museum of American History's “Escaramuza Dress” exhibition. Its body text says: “Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.” This is a narrow, institution-authored account of the sombrero charro in escaramuza attire and its shade function; it does not establish broader charro history.

The read tool opened the live page and a Wayback copy. A timestamp request for `https://web.archive.org/web/20251001000000id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579` resolved to `https://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579`; the archived page showed the exhibition dates (2021-09-17–2022-01-04) and the same quote in its exhibit-description body. However, the prescribed locator returned `NOT_LOCATED ... URLError` on the capture (exit 1), including an encoded-colon retry. The official CDX query and an alternate path spelling each returned HTTP 429. The read-tool page content does not substitute for the required locator result.

A Britannica sombrero page was also opened. Its live and archived locator checks both returned HTTPError (exit 1), so it was rejected. A Smithsonian Postal Museum page returned HTTP 403 to ordinary read and its CDX query returned HTTP 429; it was not used. Registry URL searches found no match for either the Britannica or Smithsonian exhibit URL.

## Gates

- **Source body text:** verified by ordinary read for the Smithsonian exhibit, and visible in the archived copy.
- **Live locator:** PASS for the Smithsonian quote; command and output recorded below.
- **Capture locator:** FAIL / incomplete; repeated locator attempts did not locate the quote. CDX unavailable (HTTP 429).
- **S715 artifact acceptance:** NOT MET. Row rules require the quote to locate on both live and capture URLs. Do not integrate the draft without completing that gate.
- **ACCEPT-C-63:** not run by this leaf seat. S715 is not among the frozen LIVE subset S694, S698, S702, S706, S710, S714; that does not waive this seat's two-URL source requirement.
- No blind support review, acceptance counter, O repair, held `tools/reopen-row.py`, or independent review gate was run here.

### Exact locator commands and outcomes

1. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.britannica.com/topic/sombrero' 'Sombrero, broad-brimmed high-crowned hat made of felt or straw, worn especially in Mexico and the southwestern United States.'` → `NOT_LOCATED https://www.britannica.com/topic/sombrero HTTPError`; exit 1.
2. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20251017084030id_/https://www.britannica.com/topic/sombrero' 'Sombrero, broad-brimmed high-crowned hat made of felt or straw, worn especially in Mexico and the southwestern United States.'` → `NOT_LOCATED https://web.archive.org/web/20251017084030id_/https://www.britannica.com/topic/sombrero HTTPError`; exit 1.
3. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579' 'Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.'` → `LOCATED https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579`; exit 0.
4. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579' 'Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.'` → `NOT_LOCATED https://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579 URLError`; exit 1.
5. Encoded-colon retry: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress%3Aevent-exhib-6579' 'Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.'` → `NOT_LOCATED https://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress%3Aevent-exhib-6579 URLError`; exit 1.
6. HTTP retry: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'http://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579' 'Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.'` → `NOT_LOCATED http://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579 HTTPError`; exit 1.

## Touched surfaces and provenance

- Report: `.ufo/waves/round-63/w1/ScribeRowS715.md` (this file; written once).
- Scratch artifacts only: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS715/S715-row-candidate.md`, `S715-entry-candidate.md`, `S715-Gate-candidate.md`, and `locator-evidence.txt`.
- Read before research: `reports/round-63/claims.json`, the docstrings of `reports/round-63/accept-o.py` and `accept-c.py`, `corpus/lessons/round-62-verifier-spotcheck.md` §5, and `corpus/SOURCES.md` (including S693's row shape).
- No tools installed or updated. No git/jj write commands, tests, counter runs, row/entry/README edits, or live calls to the held re-opener.

## Out of scope and known limits

This is not a successful coverage-row receipt, claim-C verdict, independent review, or counter result. No source candidate met the full two-locator rule within this seat's evidence. A working ordinary Wayback/CDX fetch that lets the prescribed locator confirm the capture quote is the missing prerequisite; the archived page being visible to the read tool is insufficient.

Full command output and archive/CDX read outcomes are in `locator-evidence.txt`. Draft line artifacts remain clearly labeled and are not accepted for integration.
