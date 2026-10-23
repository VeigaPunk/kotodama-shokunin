# Round 63, S705 source scribe report

## Behavior and finding

A candidate source was identified for the Corinthian helmet subtopic: The Metropolitan Museum of Art’s collection record “Bronze helmet of Corinthian type,” object 20.51.2. Its visible artwork-description paragraph states: “The historian Herodotos mentions the Corinthian helmet as part of the equipment of the Greek hoplite (foot soldier).” The record dates the bronze object to ca. 650–600 BCE and describes its form and an early example said to be from Olympia. The sentence appears in the main description text, not a caption, alt attribute, or title.

**S705 is not fully source-verified and is not ready to admit.** The prescribed locator located the quote on the live URL, but could not fetch the archived capture. The capture’s body text was visible through the `read` tool, but that does not replace the required locator result on both URLs.

## Draft artifacts (also saved separately under scratch)

Candidate registry row (draft only):

`| S705 | The Metropolitan Museum of Art (n.d.), “Bronze helmet of Corinthian type,” object no. 20.51.2 (ca. 650–600 BCE) — https://www.metmuseum.org/art/collection/search/250922 ; capture https://web.archive.org/web/20260124155552id_/https://www.metmuseum.org/art/collection/search/250922. | docs | A | the Met record’s account of the Corinthian type’s association with Greek hoplite equipment and its early Olympia example’s form and date | Artwork description paragraph: “The historian Herodotos mentions the Corinthian helmet as part of the equipment of the Greek hoplite (foot soldier).” | The Met ties the Corinthian helmet’s identification to Herodotos’s account of hoplite equipment and describes an early Olympia example’s form and date. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

Candidate entry bullet (draft only):

`- Herodotos mentions Corinthian helmet as equipment of the Greek hoplite infantryman. (S705)`

The clause has seven quote words in quote order (Herodotos, mentions, Corinthian, helmet, equipment, Greek, hoplite); its longest exact copied run is below 12 consecutive words.

Candidate Gate line (draft only):

`- S705 | https://www.metmuseum.org/art/collection/search/250922 | 2026-10-23 | “The historian Herodotos mentions the Corinthian helmet as part of the equipment of the Greek hoplite (foot soldier).”`

The quote is 18 normalized words. These three artifacts are drafts only pending capture locator success.

## Gates

- **S705 quote/source precheck: INCOMPLETE.** Live locator: `LOCATED`; capture locator: `NOT_LOCATED ... URLError`. The capture body was independently visible via the static `read` result, but the required dual-locator confirmation was not achieved.
- **ACCEPT-C-63: not run.** No receipt or claim verdict is made. This leaf prepared only S705 source evidence; no row or entry was integrated into the lane.
- **ACCEPT-O-63 and review gate: not run / out of scope.** No operability repair, review, or safety-hold lift is claimed.

## Commands and observed outcomes

The locator commands ran with cwd `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

1. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.metmuseum.org/art/collection/search/250922' 'The historian Herodotos mentions the Corinthian helmet as part of the equipment of the Greek hoplite (foot soldier).'`
   - Full stdout: `LOCATED https://www.metmuseum.org/art/collection/search/250922`
   - Exit: 0.
2. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260124155552id_/https://www.metmuseum.org/art/collection/search/250922' 'The historian Herodotos mentions the Corinthian helmet as part of the equipment of the Greek hoplite (foot soldier).'`
   - Full stdout: `NOT_LOCATED https://web.archive.org/web/20260124155552id_/https://www.metmuseum.org/art/collection/search/250922 URLError`
   - Exit: 1.
3. `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20250512101432id_/https://www.metmuseum.org/art/collection/search/250922' 'The historian Herodotos mentions the Corinthian helmet as part of the equipment of the Greek hoplite (foot soldier).'`
   - Full stdout: `NOT_LOCATED https://web.archive.org/web/20250512101432id_/https://www.metmuseum.org/art/collection/search/250922 URLError`
   - Exit: 1.
4. `curl -sSIL --max-time 30 'https://web.archive.org/web/20250512101432id_/https://www.metmuseum.org/art/collection/search/250922'`
   - Full output: `curl: (7) Failed to connect to web.archive.org:443 after 172 ms: Could not connect to server`
   - Exit: 7.

Other source observations:

- `read` on the live Met URL returned: `Method: failed`; `Notes: Failed to fetch URL (HTTP 429)`.
- The prescribed live locator nevertheless returned `LOCATED` as above; these outcomes are recorded separately, not reconciled by inference.
- The CDX query for the exact live URL returned 200 snapshots `20230331225031`, `20240518040624`, `20241109121353`, `20250512101432`, and `20260124155552`; each response row’s `original` field was `https://www.metmuseum.org/art/collection/search/250922`. The `read` tool opened the 20260124155552 `id_` capture and displayed the quoted sentence in the main artwork description.
- Exact-URL search in `corpus/SOURCES.md` returned `No matches found` for `https://www.metmuseum.org/art/collection/search/250922`.
- No challenge-solving, headless browser, alternate access path, acceptance counter, tests, package install, or lane-source edit was used.

## Provenance, touched surfaces, and limits

Read-only sources consulted: `reports/round-63/claims.json`, docstrings in `reports/round-63/accept-o.py` and `accept-c.py`, section 5 of `corpus/lessons/round-62-verifier-spotcheck.md`, `corpus/SOURCES.md` including S693, `reports/round-61/reopen-quote.py`, and the live/captured Met page and CDX response. The exact Met URL was not already listed in the registry when searched.

Scratch artifacts:
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS705/S705-row.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS705/S705-entry-bullet.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS705/S705-gate-line.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS705/S705-locators.md`

Only this report was written under the lane’s permitted `Report:` path. No product, judge, counter, registry, knowledge-entry, or README files were changed. No tools were installed or updated. Known limit: local ordinary requests could not connect to `web.archive.org`; this report preserves the locator failures verbatim rather than treating the read-only captured text as locator evidence.