# ScribeRowS707 — round 63 evidence report

## Result

**S707 is not ready to merge.** A FIT Fashion History Timeline body-text quote locates on the live page, but the mandated base locator does not locate that quote in the Wayback capture. Although the ordinary `read` result for the capture displays the quote, this conflicts with the controlling locator result; I do not promote the candidate to accepted evidence. The row, entry bullet, and Gate line below are retained as explicitly marked drafts only. No row or entry was appended to the lane.

## Evidence and findings

Candidate: Kenna Libes, “chaperon,” Fashion History Timeline, Fashion Institute of Technology. The page shows publication 2020-01-19 and update 2026-01-02. The candidate quote is 12 normalized words, from prose in “The Details,” not a caption, alt text, or title:

> “The liripipe, the long hanging portion of what was originally the hood”

The live source URL was absent from the frozen `corpus/SOURCES.md` search results. The proposed entry clause has six content words of at least four letters (Medieval, chaperons, liripipe, long, extension, hood); liripipe → long → hood occur in quote order. No copied run exceeds two consecutive words.

Live locator command, run from the lane root:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://fashionhistory.fitnyc.edu/chaperon/' 'The liripipe, the long hanging portion of what was originally the hood'; echo exit=$?
LOCATED https://fashionhistory.fitnyc.edu/chaperon/
exit=0
```

Wayback discovery by ordinary read: requesting `https://web.archive.org/web/20261023id_/https://fashionhistory.fitnyc.edu/chaperon/` resolved to `https://web.archive.org/web/20260908133544id_/https://fashionhistory.fitnyc.edu/chaperon/`. The read result displayed the same article and quote. However, the required locator on that id_ capture returned:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260908133544id_/https://fashionhistory.fitnyc.edu/chaperon/' 'The liripipe, the long hanging portion of what was originally the hood'; echo exit=$?
NOT_LOCATED https://web.archive.org/web/20260908133544id_/https://fashionhistory.fitnyc.edu/chaperon/ quote-absent
exit=1
```

This is an unresolved evidence conflict; the capture locator result controls row eligibility. CDX attempts were rate-limited/unavailable, so the snapshot was resolved through the ordinary date URL rather than obtained from a successful CDX response:

- `read` CDX URL `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Ffashionhistory.fitnyc.edu%2Fchaperon%2F&output=json&limit=-5&filter=statuscode%3A200` → `ECONNREFUSED`.
- `curl -sS --max-time 45 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Ffashionhistory.fitnyc.edu%2Fchaperon%2F&output=json&limit=-5&filter=statuscode%3A200'` →

```html
<html><body><h1>429 Too Many Requests</h1>
You have sent too many requests in a given amount of time.
</body></html>
```

- `curl -sS --max-time 30 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Ffashionhistory.fitnyc.edu%2Fchaperon%2F&output=json&fl=timestamp,original,statuscode,digest&filter=statuscode%3A200&limit=5'` → same 429 response.
- The ordinary `archive.org/wayback/available` endpoint and `web.archive.org/web/timemap/json` endpoint also returned HTTP 429.

Rejected alternative: `read https://www.britannica.com/topic/chaperon-headgear` returned HTTP 404; no quote was taken from it. `grep` found no `britannica.com/topic/chaperon-headgear` or `fashionhistory.fitnyc.edu/chaperon` URL in the frozen source registry.

## S707 draft artifacts — not accepted for integration

Proposed registry row (structurally formatted, but must not be appended until both locators pass):

```text
| S707 | “chaperon”, Kenna Libes, Fashion History Timeline, Fashion Institute of Technology, published 2020-01-19; updated 2026-01-02 — https://fashionhistory.fitnyc.edu/chaperon/ ; capture https://web.archive.org/web/20260908133544id_/https://fashionhistory.fitnyc.edu/chaperon/ | docs | B | Western European chaperon and liripipe form, especially 14th–15th-century wear | The Details, body paragraph after the opening book citation: "The liripipe, the long hanging portion of what was originally the hood" | the chaperon could be worn as a hooded shoulder-cape with a long hanging liripipe, then arranged as headwear | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

Proposed entry bullet:

```text
- Medieval chaperons used the liripipe as a long extension from a hood (S707)
```

Proposed Gate line:

```text
- S707 | https://fashionhistory.fitnyc.edu/chaperon/ | 2026-10-23 | "The liripipe, the long hanging portion of what was originally the hood"
```

These drafts and locator/provenance outputs are also in `/fast/scratch/hyaku/kotodama-r63/ScribeRowS707/` (paths listed below).

## Gates, scope, and provenance

- This is one S707 evidence seat only. It does **not** establish claim C’s FILE/ROWS/ONEID/RESTATE/LINK/APPEND/NOHARM/SWEEP/LIVE result, nor does it report the blind SUPPORT review. No acceptance counter was run.
- Claim O, its tool repair, counters, and review gates were out of scope and untouched.
- Read the frozen claim statements, the routed-defect lesson §5, and both acceptance-counter docstrings. `sha256sum reports/round-63/accept-o.py reports/round-63/accept-c.py` matched the supplied hashes: `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` and `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca` respectively.
- No installs, git/jj commands, tests, builds, or product edits. No lane data file was touched; only this assigned report was written in the lane.

## Artifact paths

- Lane report: `.ufo/waves/round-63/w1/ScribeRowS707.md`
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS707/S707-registry-row.draft.md`
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS707/S707-entry-bullet.draft.md`
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS707/S707-gate-line.draft.md`
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS707/S707-locator-outputs.txt`
