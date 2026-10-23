# ScribeTalariaRef — Round 62 W1, claim D

## Axis and candidate

**Axis: depth.** Independent tier-A candidate for the footwear entry’s line 93. The Museum of Classical Archaeology, University of Cambridge page is a museum collection record, not a dictionary. The page describes the Farnese Hermes cast and explicitly identifies the figure through its winged sandals.

**Draft SOURCES row S694 (11 columns; proposed, not applied):**

`| S694 | Farnese Hermes — Museum of Classical Archaeology, University of Cambridge, n.d. — https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes ; capture https://web.archive.org/web/20250711123741id_/https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes | docs | A | Farnese Hermes identification by winged sandals | Opening sentence: "This statue of Hermes, the Greek messenger god, identified by his winged sandals" | The museum's cast record identifies Hermes by his winged sandals and caduceus. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

The source page shows no publication date; `n.d.` is intentional. The quote is a 13-word verbatim fragment of the page’s opening body-text sentence. `grep` of `corpus/SOURCES.md` for this live URL returned **No matches found**.

**Proposed line 93:**

`- The statue of Hermes, a Greek messenger god, is identified by winged sandals. (S694)`

This paraphrases the quote in order; it does not claim more than the quoted identification. It contains seven content words that occur in the quote in order; the longest copied run is below 12 words.

**Draft Gate line:**

`- S694 | https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes | 2026-10-23 | "This statue of Hermes, the Greek messenger god, identified by his winged sandals" — ADMIT: Cambridge museum record, tier A; the live quote is LOCATED and the same body text appears in the 2025-07-11 capture. The capture URL’s locator probe returned NOT_LOCATED (URLError); see evidence below.`

## Evidence and locator outputs

- Static read of the live museum page: its visible body text begins, “This statue of Hermes, the Greek messenger god, identified by his winged sandals and staff (caduceus) in his left hand…” The page identifies itself as the Museum of Classical Archaeology, Cambridge; it describes a cast, with the original at the British Museum.
- Wayback CDX query `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fmuseum.classics.cam.ac.uk%2Fcollections%2Fcasts%2Ffarnese-hermes&output=json&limit=-5&filter=statuscode%3A200` returned a 200 HTML capture for the same original URL at timestamp `20250711123741`.
- Static read of `https://web.archive.org/web/20250711123741id_/https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes` showed the same quoted sentence in the page body, not only in metadata.
- Live locator command and full stdout:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes" "This statue of Hermes, the Greek messenger god, identified by his winged sandals"
LOCATED https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes
```

The command returned normally (exit 0).

- Archived-copy locator probe and full output:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://web.archive.org/web/20250711123741id_/https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes" "This statue of Hermes, the Greek messenger god, identified by his winged sandals"
NOT_LOCATED https://web.archive.org/web/20250711123741id_/https://museum.classics.cam.ac.uk/collections/casts/farnese-hermes URLError
```

This run exited 1. The capture’s text and CDX record were independently confirmed by static reads, but the base locator could not fetch the archived URL in this probe. No retry was made. The live URL itself is LOCATED, so this candidate has a located source; archived-URL fetchability remains a known operational limitation.

## Rejects, gates, and limits

- No opened candidate source was rejected. The existing S688 LacusCurtius/Smith “Talaria” dictionary URL was excluded by the assignment’s explicit no-reuse/non-dictionary constraints; it was not re-opened or re-tested.
- No `ACCEPT-D-62` counter, build, or lane gate was run. This is candidate evidence, not an integration receipt or a claim-D pass.
- Read-only surfaces consulted: `reports/round-62/claims.json`; `corpus/lessons/round-61-verifier-spotcheck.md` §7; `reports/round-62/accept-d.py`; `reports/round-61/reopen-quote.py`; `corpus/SOURCES.md`; `corpus/knowledge/culture-material/footwear-codes-terminology.md`; `corpus/lessons/round-61.md` §Gate. No product files or lesson files were changed. No tools were installed.
- **Only written surface:** `.ufo/waves/round-62/w1/ScribeTalariaRef.md` (this report).