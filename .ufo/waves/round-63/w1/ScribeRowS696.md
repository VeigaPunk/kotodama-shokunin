# ScribeRowS696 — Roman military crowns

**Disposition: partial candidate; not registry-ready.** The live quote and entry wording are supported, but the required same-page Wayback capture could not be discovered or verified. Do not land the candidate row until a timestamped capture URL is obtained and the quote locates in that capture.

## Behavior

The ordinary-read LacusCurtius transcription of Anthony Rich's “Corona” entry in William Smith's *Dictionary of Greek and Roman Antiquities* (John Murray, London, 1875) covers Roman military crowns, including the *corona obsidionalis*, *corona civica*, and *corona muralis*. The candidate quote is body text in its opening description of military-reward crowns:

> “Among the honorary crowns bestowed by the Romans for military achievements”

The quote is 11 normalized words. The candidate entry line paraphrases the page's distinction among crown forms and purposes; it has 10 content words and exactly one S-id.

### Candidate artifacts (not a completed row)

**Registry row — INCOMPLETE; capture unresolved:**

`| S696 | Anthony Rich, “Corona,” in William Smith’s Dictionary of Greek and Roman Antiquities, John Murray, London, 1875 - https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html ; capture [UNRESOLVED] | book | B | Roman military crowns as rank-coded rewards: corona civica (citizen rescue), corona muralis (wall assault), corona obsidionalis (siege relief) | “Corona,” opening paragraph, sentence 1: “Among the honorary crowns bestowed by the Romans for military achievements” | Roman military crowns rewarded prowess through distinct forms, names and purposes; the article distinguishes civic rescue, wall assault and siege-relief crowns | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

**Entry bullet:**

`- Crowns bestowed by the Romans for military achievements carried distinct forms and assigned purposes. (S696)`

**Gate line:**

`- S696 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html | 2026-10-23 | "Among the honorary crowns bestowed by the Romans for military achievements"`

The Gate line is a candidate only; its capture half remains open.

## Gates

- **Live quote:** LOCATED by the base round-61 locator. The read tool also returned the source page text with this sentence. The independent blind-support reviewer reports the quote inside the `<P CLASS="justify" ID="obsidionalis">` body paragraph, not a caption, alt text, title, or meta field; see `.ufo/waves/round-63/w1/RevRowS696.md` §§2–4. That reviewer marked the live substance and bullet supported.
- **Same-page capture:** NOT-YET-VERIFIABLE. Scribe-side CDX requests returned 403/429 and the final plain curl retry could not connect; no timestamp or id_ capture URL was established. Neither the quote-in-capture condition nor the same-page URL condition has been tested. The row therefore fails the required completeness gate for registration; this is not an `ACCEPT-C-63` result.
- **Counters:** No acceptance counter was run by this seat. There is no ACCEPT-C-63 receipt or PASS/FAIL claim here.

## Touched surfaces

- Scratch artifacts only: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/registry-row.txt`, `entry-bullet.txt`, `gate-line.txt`, `locator-results.txt`, and `review-draft.txt`.
- This report: `.ufo/waves/round-63/w1/ScribeRowS696.md`.
- No product entry or `corpus/SOURCES.md` row was written by this seat.

## Out of scope

No edits to product code, entry, registry, counters, or judge; no use of held `tools/reopen-row.py`; no counter/build/test run; no git or jj write command; no tool install/update; no delegation or background job; no browser or challenge bypass.

## Findings and provenance

1. **Candidate source and URL reuse.** `read` of `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html` returned the Smith/Anthony Rich page text, including the quoted opening clause and the sections on obsidionalis, civica, and muralis. The targeted `grep` checks for both the star-path URL and the no-star path in `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` returned “No matches found.” The no-star live URL returned HTTP 404 and was not selected. The candidate is scoped as `book`, tier B.
2. **Live locator command and output (scribe execution):**

   `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html' 'Among the honorary crowns bestowed by the Romans for military achievements'`

   Full stdout: `LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`

   The bash response did not separately expose this command's process exit status. The independent reviewer reports its own live locator as exit 0 (review report §3); that is separate execution evidence.
3. **Wayback discovery outcomes (scribe side).** The first `read` CDX query for the exact URL (`output=json`, `limit=-5`, `filter=statuscode:200`) failed with HTTP 403. A subsequent exact CDX query failed with HTTP 429; availability and timemap reads also failed HTTP 429. The Wayback wildcard-index read returned only a generic Wayback landing page, without a capture listing. Plain curl returned `429 Too Many Requests`, with `HTTP_STATUS:429`. A later minimal curl query returned `curl: (7) Failed to connect to web.archive.org:443 after 191 ms: Could not connect to server`, `HTTP_STATUS:000`, command exit 7. The exact commands and URLs are in `locator-results.txt`.
4. **Independent review and count discrepancy.** The reviewer report `.ufo/waves/round-63/w1/RevRowS696.md` independently supports the live quote and bullet but also marks capture NOT-YET-VERIFIABLE. It states: `Longest copied run = "bestowed by the Romans for military achievements" (7 words ≤ 12).` Direct token recount of the actual bullet and quote also includes the leading exact word “Crowns”, making the full longest copied run “Crowns bestowed by the Romans for military achievements” (8 words). Both counts are within the 12-word limit; the discrepancy does not change that conclusion. The reviewer's separate CDX attempt reportedly initially returned five rows before later errors; this was not the outcome of the scribe-side CDX requests above.

## Artifact paths

- Scratch directory: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/`
- Registry-row candidate: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/registry-row.txt`
- Entry bullet: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/entry-bullet.txt`
- Gate line: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/gate-line.txt`
- Locator/archive outputs: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/locator-results.txt`
- Draft provenance: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS696/review-draft.txt`
- Independent review report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-63/w1/RevRowS696.md`
- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-63/w1/ScribeRowS696.md`

No tools were installed or updated.