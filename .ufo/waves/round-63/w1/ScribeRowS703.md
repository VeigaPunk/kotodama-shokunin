# S703 flammeum source check

## Findings
A suitable authorial source was opened by ordinary read: Meghan J. DiLuzio, *A Place at the Altar: Priestesses in Republican Rome*, Princeton University Press (published Nov. 1, 2016), publisher-hosted Introduction PDF, https://assets.press.princeton.edu/chapters/i10895.pdf. The read returned the PDF body text. On printed p. 9, running paragraph text (not a caption or metadata) includes: “Roman brides wore the flammeum, the flaminica’s signature orange-yellow veil, as a good omen”. This is 16 words under the frozen counter’s stated normalization, counted manually. The publisher page independently lists the author, publisher, and publication date.

A search for this exact PDF URL in the frozen `corpus/SOURCES.md` returned no matches. Tier A is proposed for the author’s own book text; this is not a claim about publisher description text.

Draft entry bullet:

`- Roman brides wore the flammeum, a flaminica-linked orange-yellow veil of auspicious significance (S703)`

Draft Gate line:

`- S703 | https://assets.press.princeton.edu/chapters/i10895.pdf | 2026-10-23 | "Roman brides wore the flammeum, the flaminica’s signature orange-yellow veil, as a good omen"`

## Gate status and limits
**S703 is not complete and no registry row is issued.** The required Wayback `id_` capture of this same page could not be obtained: the CDX request and archive availability request each returned HTTP 429. No capture URL was guessed. Consequently neither live nor capture confirmation was run with the base locator, and no `LOCATED` result is claimed. The source URL’s absence from the existing registry is observed, but cross-scribe URL uniqueness was not confirmed.

The specified locator command `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py '<URL>' '<QUOTE>'` was **not run**; this scribe assignment does not invoke another runtime. No acceptance counter, `tools/reopen-row.py`, build, test, or lane integration was run. No ACCEPT-C-63 result or leg pass is claimed. The frozen claims and both counter docstrings were read; their file hashes matched the assignment.

## Exact command outcomes
- `sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-63/accept-o.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-63/accept-c.py` → `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` and `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`.
- `curl -sS --max-time 30 -A 'Mozilla/5.0' 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fassets.press.princeton.edu%2Fchapters%2Fi10895.pdf&output=json&limit=-5&filter=statuscode%3A200'` → response body `<h1>429 Too Many Requests</h1>`; shell exit code was not captured.
- Read calls to the same CDX URL and `https://archive.org/wayback/available?url=https%3A%2F%2Fassets.press.princeton.edu%2Fchapters%2Fi10895.pdf` → failed, HTTP 429.
- Exact URL-pattern search in frozen `corpus/SOURCES.md` → no matches.

## Touched surfaces and out-of-scope
Only the scoped report and scratch evidence bundle were written. No corpus entry, registry row, README, tool, judge, or other lane file was changed. No tool was installed. Claim O, review gates, remaining C rows, and lane-level integration are outside this seat’s work.

Scratch evidence bundle: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS703/ScribeRowS703-evidence.md`

Report: `.ufo/waves/round-63/w1/ScribeRowS703.md`