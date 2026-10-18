# R17-C01 — inuit.md Dorais 2010 dead-locator repair (old→new, access evidence, spot-check)

- worker scope: round-17 claim **C** (coverage), fixer 1 of 12, assigned entry
  `corpus/knowledge/civilizations/inuit.md` (round-16 map entry 44, the sole
  stale-documented entry in shard 37–47). Writes this fragment plus the named
  corpus edit and nothing else: no commit, no LOG/README/SCORECARD edit, no
  round-8–16 artifact touched (per AGENTS.md the parent integrates).
- assignment as dispatched: replace the dead Dorais 2010 PDF locator with a live,
  content-verified source (old→new URL + access evidence + entry spot-check); if
  no replacement verifies, update the recheck line naming the attempt. A
  replacement verified, so the fallback did not apply.
- dates/baselines: declared round-17 baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json`);
  observed HEAD at start and at write
  `9b49a4a0fca6ceeab917d401945358fdedeb7e11`; local date 2026-10-18, all probe
  stamps UTC via `date -u` / Python `datetime.now(timezone.utc)`.
- **freshness pause respected:** this is a locator repair routed to a content
  round by round 8 (`reports/round-8/metadata/m03-civ-39-57.md:109`) and carried
  by the round-16 map reason (`reports/round-16/civ-map.json` entry 44). No
  freshness verdict is issued; no other cited link was re-swept, and the entry
  says so.
- **NON-CANON.** Reference/citation hygiene only. No real-world rights, reuse,
  clearance or permission ruling is made or implied here.

## 1. The carried defect (round-16 reason trail, reproduced)

- Round-16 map entry 44: `status: stale-documented`, reason "Dorais 2010 PDF
  locator 404-stable across three independent samples (r8 m03:67, r9 v03:72,
  r16 C04); replacement-locator fix routed to a content round by round 8
  (m03:109)". Shard detail: `reports/round-16/civ/037-047.md:103-111` (this was
  the only stale-documented entry in 37–47; its other two sampled links were
  live and all 14 couples targets resolved).
- Round-17 reconfirmation, old URL, three samples
  `curl -sS -o /dev/null -w '%{http_code}|%{size_download}|%{content_type}' -L --max-time 30 -r 0-1023 <url>`:
  404 / 404 / 404 at 2026-10-18T09:18:08–09Z, body `text/html` (95720 B error
  page), effective URL redirected to `jackmanlaw.utoronto.ca` — the U of T law
  library site relocated and the `sites/default/files/toc/` PDF was not carried
  over. Fourth consecutive round of 404 (r8, r9, r16, r17).

## 2. Replacement adopted — old→new

- old: `https://library.law.utoronto.ca/sites/default/files/toc/Language%20of%20the%20Inuit%20-%20Dorais%20-%202010.pdf`
- new: `https://api.pageplace.de/preview/DT0400.9780773581623_A23657095/preview-9780773581623_A23657095.pdf`
  (pageplace preview, the publisher's e-book distributor; candidate first probed
  and passed by round 9, `reports/round-9/metadata/v03-civ-39-57.md:87`, and
  adopted here after this round's own content check).
- Access evidence (2026-10-18T09:18:09Z): range request → `206|1024|application/pdf`;
  full fetch → `200|515139|application/pdf`; fetched copy
  `sha256 61388588ca884f514c3e29510fc4ba21cb3d14d0b849e2a728eb87502f5f660d`,
  41 pages (`pdfinfo`), pdftotext-extractable.

## 3. Content verification and entry spot-check

Extracted text (`pdftotext -layout`) confirms the preview carries, in order:
title page "The Language of the Inuit" (p. 1); series page "McGill-Queen's Native
and Northern Series"; title page with "LOUIS-JACQUES DORAIS" (txt line 187);
copyright page "© McGill-Queen's University Press 2010" and `isbn 978-0-7735-3646-3`
(txt lines 194–195) — **the ISBN the entry cites**; Library and Archives Canada
CIP record naming the full subtitle "syntax, semantics, and society in the
Arctic" (lines 218–232); the complete Contents (lines 237–267, header at 237,
running header at 261, closing "Index 387" at 267) and the maps/tables list that
follows at 268ff. The file name carries the e-book ISBN 9780773581623; the copyright page of
that same file shows the cited print ISBN — recorded, not conflated.

Entry spot-check of the D row's own claim ("chapters on family, dialects,
linguistic history, literacy; the linked extract verifies edition and chapter
scope, not every grammatical claim") against the preview's ToC:

| D-row claim | ToC chapter verified |
|---|---|
| family | ch. 1 "The Eskaleut Family of Languages" 7 |
| dialects | ch. 3 "The Nunavik Dialect of Inuktitut" 66 (ch. 2 "The Inuit Language" 27) |
| linguistic history | ch. 4 "The Prehistory of the Inuit Language" 88; ch. 5 "Historical Sources and Linguistic Change" 106 |
| literacy | ch. 7 "Literacy and Formal Education" 172 |
| scope caveat | holds — the preview runs front matter → ToC → Preface (xi–xii) → Introduction and into ch. 1, ending mid-table in the dialect inventory, so page-level claims beyond that point remain uncertified by this locator |

## 4. Rejected or unadopted candidates (probed 2026-10-18T09:18–09:20Z)

| candidate | status | disposition |
|---|---|---|
| `https://openlibrary.org/isbn/9780773536463` | 200, 8028 B, but body is a "Human Verification" bot wall; the API route that did return bibliographic JSON at 09:16Z timed out twice afterwards (`000`) | not adopted; flaky and not content-verifiable by plain fetch |
| `https://books.google.com/books?vid=ISBN9780773536463` | 200; page title names "Language of the Inuit: Syntax, Semantics, and Society in the Arctic - Louis-Jacques Dorais" | content-verified alternate, not adopted (viewer page, not a front-matter/ToC document) |
| `https://muse.jhu.edu/book/22942` | 200 but **different book** ("Yellow Power, Yellow Soul") | rejected — live URL, content mismatch; recorded so the id is not reused as this title's locator |
| `https://www.mqup.ca/language-of-the-inuit--the-products-9780773536463.php` | 404 (round-9 rejection reproduced) | rejected |
| `https://search.worldcat.org/title/473657685` | 403 bot wall (round-9 receipt) | not re-probed this round |

## 5. Entry edit receipts (files touched: 1)

`corpus/knowledge/civilizations/inuit.md`, 3 lines changed (`git diff --stat`:
`1 file changed, 3 insertions(+), 3 deletions(-)`):

1. head `- verified-at:` — appended the 2026-10-18 round-17 locator-repair note
   with the old→new URLs, the round-8/9/16 reason trail, and the statement that
   other cited links keep their 2026-10-17 status (kept on one line so the head
   key parse is unchanged).
2. source-table row **D** — dead link replaced by the content-verified preview;
   label "title/copyright/contents" → "front matter and contents preview";
   "linked extract" → "linked preview" in the limitation clause.
3. access line under the table — records the 2026-10-18 locator probe date.

Verification after edit:

- before sha256 `312427a38a52d7ee03d85d11914ced36cc861c38bb246531d6f76353ddd45f0b`
  (36445 B) — **identical to the round-16 receipt** (`reports/round-16/civ/037-047.md:74`,
  `312427a3…0b`), so the pre-edit bytes are the audited ones;
  after sha256 `52c5a11b7b7db949f8f93da199a34a0062a888a180e021b2a124558480ef0c5d`
  (37285 B).
- `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/inuit.md`
  → `INFO scan: files=1 marks=6 mark-lines=6 findings=0 blocked=0`, exit 0;
  to-verify mark count 6, unchanged from the round-16 receipt's "6".
- head keys still parse 1:1 (`topic, sources, couples, verified-at, recheck`),
  each on one line; `- couples:` line untouched, so the 14/14 couples resolution
  receipt still applies.
- the **in-file** D-row URL was re-extracted from the edited file and probed:
  `206|1024|application/pdf` (2026-10-18T09:18:09Z) — the entry now carries a
  live locator, not just this fragment.

## 6. Limits and what remains

- The adopted locator is a distributor-hosted preview; it can move or expire like
  the dead one did. The entry's verified-at note and this fragment carry the
  full old→new trail, and the Google Books alternate above is content-verified
  should a second replacement be needed.
- The preview certifies edition, ISBN, and chapter scope only; it is not a
  full-text reading of the book, and no page-level grammatical claim is
  upgraded by this repair.
- Round-16 map entry 44 may be flipped to `stale-fixed` by the round-17 map
  builder on the strength of this fragment; that flip is the map builder's
  receipt to make, not claimed here.
- Remaining stale-documented entries (the other 11 of round 16) are other
  workers' assignments and are not dispositioned by this fragment.
