# ReviewSupportB — blind per-row support, claim C falsifier, rows S728–S736

Round 64 wave 1. Scoped verdicts on the nine staged rows
`.ufo/waves/round-64/rows/ScribeRowS7{28..36}/row.txt`, blind of every other seat's
report. Each row's located-quote check was **re-run live** at ~2026-10-24T02:0x UTC
against the pinned locator `reports/round-61/reopen-quote.py` (same bytes the LIVE leg
pins; sha taken at base `ff30a205`).

## Method (what "re-run live" meant)

1. Assembled a scratch registry at
   `~/.cache/hyaku/kotodama-r64-w1/ReviewSupportB/corpus/SOURCES.md` containing the nine
   staged `ROW:` lines verbatim, so `reopen-quote.py --row S<n>` exercised **exactly**
   the row's own URL set (live URL first, then the pinned `web.archive.org … id_`
   capture) and its own first anchor quote — identical semantics to the counter's LIVE
   leg.
2. Ran `python3 -B reports/round-61/reopen-quote.py --row S<n>` from that scratch root.
3. For every row, re-fetched the LOCATED document independently and printed the quote's
   ±160-word normalized context to confirm the quote sits in the section the anchor
   names (receipts: `contexts.json` in the scratch dir).
4. Failures were retried before any UNREACHABLE verdict (mirroring the LIVE leg's
   3×-20 s cadence).

## Verdicts

| Row | Verdict | LOCATED at | Receipt |
|-----|---------|-----------|---------|
| S728 | **SUPPORTED** | live ANU PDF `ch08.pdf` | `LOCATED https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf` |
| S729 | **SUPPORTED** | live PLOS ONE article | `LOCATED https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` |
| S730 | **SUPPORTED** | live McGill PDF | `LOCATED https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf` |
| S731 | **SUPPORTED** | Wayback capture 20250424085946 | `LOCATED https://web.archive.org/…/PMC8608171/` (retry; first pass 429) |
| S732 | **SUPPORTED** | Wayback capture 20261003105239 | `LOCATED https://web.archive.org/…/PMC5966288/` (4 locator runs before wayback throttle cleared; independent fetch of the capture — 167,038 B — contains the quote verbatim) |
| S733 | **SUPPORTED** | Wayback capture 20250222070806 | `LOCATED https://web.archive.org/…/PMC5507709/` |
| S734 | **SUPPORTED** | Wayback capture 20250319021450 | `LOCATED https://web.archive.org/…/PMC2614655/` |
| S735 | **SUPPORTED** | live OSU PDF | `LOCATED https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf` |
| S736 | **SUPPORTED** | live Frontiers page | `LOCATED https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full` |

Every one of the nine quoted strings was found **verbatim** in the fetched document
(normalized match; contexts in `contexts.json`). Examples:

- S728: "…schieffelin 1990 for example reports that kaluli mothers use elema say it like
  this to prompt the children to correct their non target like utterances…"
- S732: "…bilingual children in immigrant households sometimes avoid using the family s
  heritage language in favor of the majority language 37 38…"
- S736: "…created stories with the assistance of their caregivers and siblings in the
  social contexts of their homes…"

## Findings

**No row-level defects in S728–S736.** All nine are SUPPORTED.

Nits worth recording (none rise to NOT-SUPPORTED; none affect the row contract):

1. **PMC live pages are captcha-walled** (S731, S732, S733, S734): a plain fetch of
   `pmc.ncbi.nlm.nih.gov` returns HTTP 200 with a 167-char reCAPTCHA interstitial
   ("Checking your browser"), so the live URL is always `quote-absent` and the
   capture does all the vouching. The rows' `ACCESS: plain curl, HTTP 200` claims are
   literally true (the wall itself is 200) but the live body does not contain the
   quote — capture-only location. Legal under the locator's URL order; noted because
   cold re-runs of the whole registry will always fall through to wayback for PMC rows.
2. **Wayback 429 flakiness**: S731 LOCATED on second attempt, S732 needed a fourth
   locator run (~4 min of transient 429s; `curl` on the same capture URL returned 200
   mid-window). S732 is not in the frozen `LIVE_IDS` subset `{S718,S723,S728,S733,S738}`,
   so the counter's LIVE leg is unaffected — but reviewers re-running these rows cold
   should expect intermittent NOT_LOCATED/HTTPError and must retry before judging.
3. **Staging cosmetics**: `row.txt` `CAPTURE:` line for S730 and S735 reads
   `timestamp <ts>` (no `=`) where peers use `timestamp=<ts>`; the capture URL inside
   the ROW line itself is well-formed, so `check-rows.py`/accept-c CAPTURE parsing is
   unaffected. S731's anchor names "Discussion, Code-Switching and Language Proficiency
   paragraph"; the article's actual subsection is "Code-Switching and DLD" — the quote
   is verbatim from that Discussion either way.
4. **Out-of-slice observation for integration**: the context flags S723 and S740 as
   missing contributions; my S728–S736 slice is complete (9/9 row.txt present).

## Tooling

No installs. `uv` (already at `~/.local/bin/uv`) fetched `pypdf==5.4.0` on demand inside
the pinned locator's own `uv run --with` sandbox — channel: uv ephemeral env; reason:
PDF text extraction for S728/S730/S735, mandated by the pinned tool itself.

## Residual risk / gaps

- Quote-context fidelity was judged by window, not full-paper reading: scope cells and
  bullets are plausible restatements, but a deeper semantic-audit seat should spot-check
  whether the *claim* each bullet adds (e.g., S731's "avoid diagnostic shorthand") is a
  fair extrapolation rather than verbatim support.
- Live-URL support for the four PMC rows is currently captcha-dependent; if wayback
  prunes or the captures were taken post-edit, location evidence rests on archive
  fidelity — the capture timestamps predate this round, which is the honest property.

Verdict on the slice: **9/9 SUPPORTED**, no falsifier found in S728–S736.
