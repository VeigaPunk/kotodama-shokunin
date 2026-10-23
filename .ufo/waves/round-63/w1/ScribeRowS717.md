# Round 63 — S717 scribe report

## Behavior
No product behavior was changed. The Britannica live page's Quick Summary opening paragraph contains a candidate description of the fez's brimless form, flat top, red felt, and tassel. The page identifies the summary as AI-created and warns it may make mistakes; it also says Britannica has no full article on this topic. The candidate is deliberately scoped to that description, not Ottoman dress history.

## Gates
- Live source locator: **LOCATED**, exit 0.
- Capture body: the ordinary reader's date lookup resolved to a Wayback `id_` URL and returned the same Quick Summary text, including the candidate quote.
- Frozen base locator on the HTTPS capture: **NOT_LOCATED** (`URLError`), exit 1 on both attempts. The HTTP variant returned `quote-absent`, exit 1. Therefore the required live-and-capture locator gate is **not met**. The row, entry bullet, and Gate line below are drafts only; do not integrate as verified S717 support.
- CDX retrieval: reader requests returned HTTP 429; ordinary curl and urllib attempts could not connect. The capture timestamp was discovered through a direct Wayback date lookup, not CDX. This does not satisfy the specified CDX process.
- `ACCEPT-C-63` and `ACCEPT-O-63` were not run by this scribe seat; no counter receipt or overall claim verdict is asserted.

## Candidate artifacts (provisional; not admissible until capture locator succeeds)

Registry row:

| S717 | Fez, Encyclopaedia Britannica, updated 2026-07-22 — https://www.britannica.com/topic/fez ; capture https://web.archive.org/web/20260818053727id_/https://www.britannica.com/topic/fez | docs | B | Britannica's basic description of fez silhouette, color/material and tassel; not historical Ottoman dress practice | Quick Summary, opening paragraph, "A fez is a brimless, cylindrical or cone-shaped hat with a flat top, typically made of red felt and often adorned with a tassel." | Britannica's AI-generated quick-summary description of the fez's form, red-felt material and tassel; the page warns the summary may make mistakes, so this is bounded descriptive support, not historical evidence | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |

Entry bullet:

- Brimless cylindrical felt caps often carry a tassel. (S717)

The clause has seven content words (brimless, cylindrical, felt, caps, often, carry, tassel); five appear in quote order. Its longest consecutive verbatim run from the quote is two words.

Gate line:

## Gate
- S717 | https://www.britannica.com/topic/fez | 2026-10-23 | "A fez is a brimless, cylindrical or cone-shaped hat with a flat top, typically made of red felt and often adorned with a tassel."

The quote is 24 whitespace-delimited words (25 if `cone-shaped` is split on its hyphen), within the 8–25 bound either way.

## Commands and observed results
Working directory for lane-relative commands: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

- `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.britannica.com/topic/fez' 'A fez is a brimless, cylindrical or cone-shaped hat with a flat top, typically made of red felt and often adorned with a tassel.'; echo exit=$?` → `LOCATED https://www.britannica.com/topic/fez`; `exit=0`.
- `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260818053727id_/https://www.britannica.com/topic/fez' 'A fez is a brimless, cylindrical or cone-shaped hat with a flat top, typically made of red felt and often adorned with a tassel.'; echo exit=$?` → `NOT_LOCATED https://web.archive.org/web/20260818053727id_/https://www.britannica.com/topic/fez URLError`; `exit=1`. Repeating the same command produced the same result.
- The HTTP locator variant `http://web.archive.org/web/20260818053727id_/https://www.britannica.com/topic/fez` → `NOT_LOCATED ... quote-absent`; `exit=1`.
- Reader request for `https://web.archive.org/web/20260701000000id_/https://www.britannica.com/topic/fez` resolved to `https://web.archive.org/web/20260818053727id_/https://www.britannica.com/topic/fez`; its returned page body contained the quote. This reader result is not a base-locator pass.
- Reader CDX request `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.britannica.com%2Ftopic%2Ffez&output=json&limit=-5&filter=statuscode%3A200` → HTTP 429. The alternate CDX request without the status filter, the Wayback availability API, and timemap endpoint also returned HTTP 429.
- `curl -sS -D - 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.britannica.com%2Ftopic%2Ffez&output=json&limit=-5&filter=statuscode%3A200'` → `curl: (7) Failed to connect to web.archive.org:443 after 191 ms: Could not connect to server`; exit 7.
- Ordinary urllib CDX request with `User-Agent: Mozilla/5.0` raised `urllib.error.URLError: <urlopen error [Errno 111] Connection refused>`; no CDX records were obtained.
- Initial `https://www.britannica.com/topic/fez-headgear` candidate returned HTTP 404 in the reader and was rejected. `functions.grep` for `[Ff]ez` in `corpus/SOURCES.md` returned `No matches found`; the exact `.../topic/fez-headgear` string also had no match. This checks the current registry only; cross-scribe URL uniqueness was not inspected.
- `sha256sum reports/round-63/accept-o.py reports/round-63/accept-c.py` returned:
  ```
  4efaadf2d2ded3024bf020a367789360b330901b442c43f4e74401c801074ee1  reports/round-63/accept-o.py
  3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca  reports/round-63/accept-c.py
  ```
  **Hash conflict:** the assignment specifies O hash `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`, whereas the measured O file hash is `4efaadf2d2ded3024bf020a367789360b330901b442c43f4e74401c801074ee1`. C's measured hash matches the assignment's specified hash `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`. No inference is made about why O differs.

## Touched surfaces and out-of-scope
- Wrote only this required report in the lane repository; no product, registry, entry, counter, or review file was modified.
- Scratch artifacts: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS717/S717-row.md`, `S717-entry-bullet.md`, `S717-gate.md`, and `S717-evidence.md`.
- No tool was installed. No acceptance counter, held product tool, commit, push, deploy, or reviewer gate was run. Entry/registry integration and cross-scribe URL collision checking remain outside this seat's completed evidence.
