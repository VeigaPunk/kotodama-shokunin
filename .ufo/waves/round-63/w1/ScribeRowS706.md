# S706 source report — partial; archive evidence blocked

## Behavior
Opened the National Museum of Australia page `https://www.nma.gov.au/learn/diy/roman-soldier-helmet` by ordinary static read. The page title is “Roman soldier’s helmet | National Museum of Australia”; its metadata says created 2018-10-02 and modified 2025-09-25. Under “Did you know ...”, body text (not a caption or image attribute) states: “A typical Roman helmet was called a galea.” The quote is 8 normalized words. The live locator returned `LOCATED` for the exact quote.

The following entry and Gate artifacts are source-supported and ready to reuse:
- The museum calls a typical Roman helmet a galea in its Roman soldier helmet guide (S706)
- S706 | https://www.nma.gov.au/learn/diy/roman-soldier-helmet | 2026-10-23 | "A typical Roman helmet was called a galea."

The entry clause has at least five content words; `typical Roman helmet galea` occur in quote order, with a longest consecutive copied run of three words. The URL did not occur in the frozen `corpus/SOURCES.md` search.

## Gates
- Source: official National Museum of Australia page; tier-A candidate by publisher. Its stable live URL and body quote are verified.
- Live locator: command `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.nma.gov.au/learn/diy/roman-soldier-helmet' 'A typical Roman helmet was called a galea.'`, from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; full output: `LOCATED https://www.nma.gov.au/learn/diy/roman-soldier-helmet`. The tool response showed no nonzero command status.
- Wayback CDX and replay: not verified. Requests returned HTTP 429 or could not connect. No capture timestamp was established, no valid registry row was written, and no locator was run on a capture. S706 is in the frozen LIVE subset; its archived-page portion remains unverified. This is not an ACCEPT-C-63 judgment.

## Findings and exact archive attempts
1. `curl -sS 'https://web.archive.org/cdx/search/cdx?url=www.nma.gov.au/learn/diy/roman-soldier-helmet&output=json&limit=-5&filter=statuscode:200'` returned `<html><body><h1>429 Too Many Requests</h1><p>You have sent too many requests in a given amount of time.</p></body></html>`.
2. Static read of `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.nma.gov.au%2Flearn%2Fdiy%2Froman-soldier-helmet&output=json&limit=-5&filter=statuscode%3A200` failed with HTTP 429.
3. Static read of a CDX query with `fl=timestamp,original,statuscode` and `collapse=digest` failed with HTTP 429.
4. Static read of `https://archive.org/wayback/available?url=https%3A%2F%2Fwww.nma.gov.au%2Flearn%2Fdiy%2Froman-soldier-helmet` failed with HTTP 429.
5. Static read of `https://web.archive.org/web/timemap/link/https://www.nma.gov.au/learn/diy/roman-soldier-helmet` failed with HTTP 429.
6. A direct replay probe at `https://web.archive.org/web/20251001000000id_/https://www.nma.gov.au/learn/diy/roman-soldier-helmet` failed with HTTP 429. This probe did not establish or serve as a discovered capture.
7. Encoded-URL curl retry of CDX with `limit=5` returned `curl: (7) Failed to connect to web.archive.org:443`; exit code 7.

No bot challenge was routed around and no headless browser was used. A verified capture is the only missing evidence for a valid S706 registry row; known source metadata and the proposed row fields are recorded in the scratch artifact, but no placeholder or invalid row line was produced.

## Touched surfaces and out of scope
Wrote this permitted report and the scratch evidence artifact only. No lane source, entry, code, judge, or counter was edited. No git/jj command, counter, test, review gate, or `tools/reopen-row.py` invocation was run; no tool was installed. Other S694–S717 rows and claim O are outside this seat.

## Artifact paths
- Scratch evidence and copyable entry/Gate lines: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS706/S706-source-artifacts.md`
- Report: `.ufo/waves/round-63/w1/ScribeRowS706.md`

Report: .ufo/waves/round-63/w1/ScribeRowS706.md
