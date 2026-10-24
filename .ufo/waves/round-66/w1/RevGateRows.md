# RevGateRows — anchor/row gate review (round 66, w1)

Seat scope: verify that each new S777–S800 row's anchor quote locates in its fetched page, and
attack the row gates of `reports/round-66/accept-c.py`. Read-only on the lane; all probes under
`/tmp`; no tool installs, no lane/jj writes.

## 0. State of the artifacts under review (blocking dependency)

At probe time (2026-10-24T08:29–08:35Z) the row corpus does not exist yet:

- `.ufo/waves/round-66/rows/` contains only two empty dirs (`ScoutReject04/`, `ScoutRow03/`);
  no `row-*.txt` anywhere (`find .ufo/waves/round-66/rows -name 'row-*.txt'` → 0).
- `corpus/SOURCES.md` has no `S776` line and no `S777`–`S800` line (`grep -n 'S776' → none`;
  last row is S775 at line 731).
- `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` does not exist;
  `corpus/knowledge/culture-material/games-play-sport-contests.md` still cites `(S753)` once and
  `(S776)` zero times.
- `reports/round-66/telemetry/` has controls + dry-runs but no `final-measures-*.txt`,
  no `separability-real.txt`.

So **per-row anchor verification of S777–S800 could not be executed**: there is nothing to open
with curl/pdftotext. That is recorded as the round's dependency, and this seat instead did the
verification that *is* possible in scope: the one anchor pair the claim already names
(S753/S776 durability, Ca-D1) and a source-level attack on the row gate itself.

## 1. Findings, by severity

### HIGH-1 — No leg of ACCEPT-C-66 compares an anchor quote to the fetched page; a fabricated anchor passes

`accept-c.py` legs are FILE, SET, ROWS, ONEID, RESTATE, HOSTS, LINK, APPEND, NOHARM, SWEEP,
CAPTURE, TOPIC. None fetches or reads the cited page. `RESTATE` (lines 221–248) compares the
entry bullet only against the **row's own** `anchor_quote(c[5])` and `teaches` cell, using the
counter's own functions. Executed against the frozen module:

```
fabricated RESTATE -> PASS inq=7 cov=0.44 novel=3
```

with an invented anchor (`"The scent guilds of Nineveh sealed vials with lapis dust."`), an
invented teaches cell, and a bullet that restates them. Consequence: ACCEPT-C-66 PASS certifies
*internal consistency of 24 rows with the entry*, not that any quote exists in any source. The
frozen predicate as written is not a coverage proof; the only real defence is the review-only
"blind per-row support", which has no artifact yet. This should be stated in the lesson rather
than implied away by the counter's name.

### HIGH-2 — A row with an empty/no-URL source cell passes ROWS, and a bare `no-capture` token satisfies CAPTURE

- ROWS (lines 205–214; the per-new-id loop begins at 186): `u = row_urls(c[1]); if u: live_urls[sid] = u` — there is no `else:
  row_bad.append(...)`. A row whose source cell has no live URL is never marked bad, and
  `len(c) != 11` is the only structural test.
- CAPTURE (lines 302–311): bad only when `not CAPTURE_RE.search(src) and "no-capture" not in
  src.casefold() and "nocapture" not in src.casefold()`. The token needs no reason string and
  there is no cap on how many rows may use it.
- HOSTS (lines 252–257) ignores hostless rows entirely.

Combination: 10 rows with 10 distinct hosts satisfy HOSTS, while up to 14 rows may carry a
33-character excuse (`no-capture`) and no URL, and ACCEPT-C-66 still passes every leg. The file's
own docstring says "explicit 'no-capture' *reason* token"; the code enforces neither a reason nor
a live-URL requirement. This is the cheapest false stamp available to a build seat, and it is
reachable without any dishonest quote — so it is also a shortcut a well-meaning seat can take
under time pressure.

### HIGH-3 — CAPTURE does not enforce the predicate `claims.json` states ("same-page" capture)

Frozen leg text (claims.json, C): "each new row's source cell carries live URL **and a same-page**
web.archive.org capture or an explicit no-capture reason string". Code:

```
CAPTURE_RE = re.compile(r"web\.archive\.org/web/\d{14}(?:id_|if_|im_)?/\S+", re.IGNORECASE)
```

No comparison against the live URL's normalized path. Proven with the module:

```
src = "https://example.org/live/page ; web.archive.org/web/20260101000000id_/https://unrelated.example.net/other.pdf ."
cross-page capture matches CAPTURE_RE -> True
```

A row can pair any live URL with a capture of any unrelated page and pass. The counter is weaker
than the frozen statement it is supposed to decide; either the code is tightened to compare
`norm_url(live)` with `norm_url(capture target)` (path+host) or the predicate must be revised
before data — it cannot stay as-is and be reported as PASS on the current wording.

### MED-1 — LINK duplicate detection is evadable via query string; captures are not compared

`norm_url` (lines 90–105) keeps the query string. Same document cited as
`https://x.org/a?utm=1` and `https://x.org/a?utm=2` yields two identities
(`norm_url(...) != norm_url(...)` → True), so two "rows" can mine one page. Archive capture URLs
are excluded from `live` and never enter the LINK comparison, so a capture URL cannot collide
with a live URL either. With 24 rows and only 10 required hosts, this is a plausible accidental
duplicate class (publisher pages with tracking params), not just a deliberate one.

### MED-2 — HOSTS uses raw `netloc`, not the normalized host the predicate claims

claims.json says ">=10 distinct **normalized** hosts". Code (252–257) uses
`urllib.parse.urlparse(u).netloc.lower()`; `www.x.org` and `x.org` count as two. `norm_url`
exists and is used only for LINK. Demonstrated: `"www.x.org" != "x.org"`. The 10-host bar can
therefore be met with fewer than 10 distinct publishers.

### MED-3 — Ca D1's receipt does not currently support its own statement, and its "old capture replay" line is a network failure, not a 404

`reports/round-66/telemetry/s753-recapture.txt` (11 lines) contains `status=200
content-type=application/pdf` and the PDF type line, but **no quote text**, **no capture timestamp
`20261024111013`**, and **no `S776`**, so the D1 leg (`accept-ca.py` lines 88–106) fails today on
`quote`, `capture_ts`, `s776`. Its "old capture replay" section records `old_capture status=000` —
a curl connect failure, not an HTTP 404; presenting it as a replay result would be a false stamp.

Independent probe (my own, 2026-10-24T08:31–08:35Z) shows the *substance* of the claim is true:

```
live  GET https://www.penn.museum/.../sowing-seeds.pdf -> 200 application/pdf, 529795 bytes
      sha256 cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632
CDX   penn.museum/.../sowing-seeds.pdf -> 20250926172224 200 application/pdf
                                         20261024111013 200 application/pdf
fresh replay 20261024111013id_/... -> 200 application/pdf 529795 bytes,
      sha256 cb6ff9b8… (identical), pdftotext text identical to live
old replay   20250926172224id_/... -> 302 -> 20261024111013id_/... -> 200 pdf, same sha
```

Note the old capture now **redirects to the fresh one** rather than 404ing, so the D1 defect
premise ("committed capture replays 404") is not reproducible at this timestamp; a receipt must
record what it observed (302 chain) and must not be worded as a 404.

### MED-4 — The S753 anchor does not locate as a contiguous substring under either pdftotext mode; it locates only after whitespace normalization

Anchor cell: `"Versions of mancala are traditionally played across Africa and Asia, with gameplay
and board dimensions varying considerably between different regions."`

```
grep -c 'Versions of mancala are traditionally played across Africa and Asia' raw.txt       -> 0
grep -c 'Versions of mancala are traditionally played across Africa and Asia' layout.txt    -> 0
tr '\n' ' ' | tr -s ' ' | grep -o 'Versions of mancala are traditionally played across Africa and Asia' -> match
```

The sentence straddles a two-column break (…"across Africa" end of column, "and Asia" start of
the next). "Verbatim" is therefore only true modulo newline/column normalization. Any seat
verifying S777–S800 anchors with a naive `grep -F` will get false negatives on multi-column PDFs,
and a seat stitching quotes across columns can produce an anchor that no reader can locate in one
reading pass. The round's standard should say "verbatim after whitespace normalization" and
prefer anchors confined to one line/column.

### LOW-1 — Tier is membership-only; tier inflation is unconstrained

ROWS checks `c[3] in ("A","B")` only — 24 rows could all be A with no consequence. There is no
distribution or justification check and no independent grader inside the counter; the only
brake is review-only support. Worth a sentence in the lesson so a future round does not read
"tier A/B enforced" as "tier earned".

### LOW-2 — D1's status test is a substring test

`accept-ca.py` D1 uses `"200" not in d1` and `"application/pdf" not in d1`. Any occurrence of the
digits `200` anywhere in the receipt (a character count, a year, a byte length) satisfies the
status half. The quote/timestamp/S776 tests are literal and are the real content of the leg; the
status test should anchor to `status=200`.

## 2. What I could not verify (residual risk)

1. **24-row support is entirely unverified** — no row fragments, no entry, no registry diff.
   If the rows land after this seat, the L1 must either re-run this check or require, per row, a
   recorded locate line (extractor, normalization, matched sentence) in a receipt; the counter
   will not do it (HIGH-1).
2. **Capture same-page-ness (HIGH-3), empty-cell rows (HIGH-2), query-duplicates (MED-1), host
   normalization (MED-2)** are code-level facts, proven against the frozen module; they do not
   depend on any network state.
3. The old-capture behavior is Wayback-state-dependent (302 to newest today). A future round
   must not cite a 404 from round 65 without re-probing; conversely my 302 observation must not
   be cited as proof the old capture served the PDF *in September 2025*.
4. `s753-recapture.txt` needs regeneration with: live status/type/bytes, the normalized quote,
   capture timestamp `20261024111013`, replay status/sha256, and the observed old-capture chain.
   Until then Ca-D1 fails.

## 3. Recommended minimum before ACCEPT-C can be called a coverage proof

- Tighten CAPTURE to same normalized path as the live URL, and cap/justify `no-capture` rows
  (e.g. ≤2, each with a reason string and a live-URL 200 probe).
- Reject rows with no live URL in ROWS.
- Normalize host via `norm_url` for HOSTS; drop query from LINK identity or strip tracking params.
- Add one leg that, per row, records extractor + normalized quote location (a receipt the counter
  reads: `anchor-verify.txt` with one line per S-id and the matched sentence), so "verbatim" is
  machine-checked rather than asserted.
- If the predicate is intentionally weaker than the wording, revise the wording pre-data; a
  PASS against weaker code than the printed leg text is a false stamp (HIGH-3).

## 4. Evidence index (all re-runnable)

- live PDF: `curl -o /tmp/s753chk.pdf https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf`
  → 200, 529795 B, sha256 `cb6ff9b8…538632`; `pdftotext` text 12355 B.
- fresh capture: `curl -o /tmp/cap.pdf https://web.archive.org/web/20261024111013id_/…` → 200,
  529795 B, sha256 identical to live; `pdftotext` output byte-identical to live text.
- old capture: `curl -L …/web/20250926172224id_/…` → 302 → `20261024111013` → 200, same sha.
- gate probes: import of `reports/round-66/accept-c.py` (`content_words`, `in_order_coverage`,
  `anchor_quote`, `CAPTURE_RE`, `norm_url`) — outputs quoted inline above.
- No tools installed or upgraded for this seat.

Report: .ufo/waves/round-66/w1/RevGateRows.md
