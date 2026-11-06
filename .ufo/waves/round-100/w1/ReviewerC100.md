# ReviewerC100 — Report (round 100, claim C independent review)

Verdict: **claim C PASS (C1-C9 all PASS, no failing leg).** Overall PREDISPATCH-100 on my run:
FAIL legs=14/15 — the only failing leg is O5 (SCORECARD capability row, claim O surface), which
had not landed when I ran the frozen counter; it is outside claim C and outside this seat.
Detailed review: `.ufo/waves/round-100/w1/stage/ReviewerC100/review.md`.

## Files written
- `.ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json` (sha256 db3cb5593eef3d957a176b84ee69e138f2bdbade8e37ce6183c4ceba34c91c27) — the C9 input: JSON list of 10 objects {id,url,http,fresh_sha256,quote_count,attempts}, every http 200 and quote_count 1 observed.
- `.ufo/waves/round-100/w1/stage/ReviewerC100/review.md` (sha256 1292d0744870f802561336a07812957273e9e96a61930e41cc55966293ab447c) — full reopen table, counter table, support table, checks, defects.
- `.ufo/waves/round-100/w1/stage/ReviewerC100/counter.txt` (sha256 db9da8c6be386cfb24de474acbf5fc45e82f21bf7adf88b242c022997f568d37) — frozen-counter output on the landed tree.
- This Report.

## Re-open (all 10 qualifying rows, plain curl -sL --max-time 30, converted as captured)
S1018-S1027: 10/10 http 200 (observed), 10/10 quote_count 1 (observed in fresh bytes), fresh
sha256 == manifest raw capture for S1018-S1023, S1025, S1026. Two byte-drifts, content-identical:
S1024 PDF (842805→842807 B; one FlateDecode stream /Length 886→887 re-serialized server-side,
extracted text identical) and S1027 HTML (43071 B both; all 114 differing bytes are the CDN
nonce+timestamp in a `cdn-cgi/content?id=...` link). S1019/S1021 needed one retry after
302+curl-rc-28 (timeout); S1020 needed the full criterion-38 budget (initial + 3 retries, 20 s
backoff; archive.org datanode hung; 200 on attempt 4). Every attempt is recorded in reopen.json.
Conversion bug in my first driver (tag-strip applied to plain-text djvu URLs mangled OCR noise)
was found and fixed by content-sniffing; lane files were never touched by it (scratch only).

## Counter (frozen bytes, base-rev 60010a55…, rc=1, 183 s)
C1 PASS (bytes=41933 h2=12 table=21x3 phrases=6/6 topic-line=equal) · C2 PASS (rows=951
highest=S1027 new=10 qualifying=10) · C3 PASS (added=10 removed=0 illegal=0) · C4 PASS (census
rc=0) · C5 PASS (CORPUS-INDEX OK 272/272) · C6 PASS (10/10 cited) · C7 PASS (10/10 bound,
captures-verified=15) · C8 PASS (272 files, 0 other owners) · C9 PASS (10 ids re-opened with
count 1, min 3, from my reopen.json). O0-O4 PASS (selftest 40/40; battery 28/28; R99-M2 replay
exact {(UNSUPPORTED-CELL, Yoruba, limit on the praise)}; mutation 36/36); O5 FAIL
(scorecard-capability-rows=0, skill-mentions=2).

## Sentence-support
58 citation markers, 58 supported / 0 unsupported; 2 weak paraphrases flagged in review.md §3
(S1025 "when serious rowing declined"; S1020 "a hundred lashes" / "a rower describes"). German
S1021 claims locate exactly ("der Vorsänger zugleich auch Vorarbeiter"; "wie ein fortgesetztes
Kommando"). No id points at the wrong source.

## Other checks
Phrases: 6/6 in natural h2 headings (§2-§5) plus natural §7 header/data-row hits; no stuffing.
§7 telegraphic cells spot-verified against captures (legend + binding lines make them decodable).
Non-canon: NON-CANON worked example, *design, not sourced* tags, §1 no-canon line, §11 handoff.
PROVINCE deferrals: audio-shokunin (sound), lore-shokunin (canon), chousa (source grading).
README: index line in filename order, `## linguistics/` 44→45, changelog 271→272, footer
convention matched (20th per-round footer). Supersede: 0 of the 10 new rows supersede; registry
diff is a pure append. Defects (non-leg): duplicated §12 ledger paragraph; redundant `- source:`
line; S1020 fetch fragility. No registry row, entry, README, manifest or lane file was edited by
this seat; writes were stage files, this Report, DONE, and scratch (deleted below).

## Numbers (command → rc)
- curl re-opens: 10 ids → 10× http 200 observed (attempts in reopen.json).
- quote counts: ws-collapsed `str.count` of each manifest quote in fresh text → 10× 1.
- counter: `python3 -B predispatch.py --root <lane> --work <scratch>/counter --base-rev 60010a55…` → rc=1 (14/15, O5 fail).
- C8 sweep (mine): 272 files scanned, 0 other owners (python os.walk + topic/heading scan) → rc=0.
- capture shas: 15/15 manifest capture files verified == recorded sha256 (pre-check) → rc=0.
- base registry: 941 rows, highest S1017 (`git show 60010a55:corpus/SOURCES.md`) → rc=0; landed: 951 rows, highest S1027.

## Tooling
No tools installed or upgraded (pdftotext, curl, python3 already present). Rule file read. pacman
untouched. Host sysctls untouched. No git/jj mutations. No sibling or fleet-root writes.

## Blockers
None for claim C. For the round verdict: O5 (claim O registration) still open at measurement
time — the L1 should re-run the counter once the SCORECARD capability row lands; my reopen.json
needs no regeneration.
