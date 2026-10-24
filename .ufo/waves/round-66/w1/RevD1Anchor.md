# RevD1Anchor — S753 durability repair under attack (r66 v2, claim Ca / R65-D1)

Seat: reviewer, attack. Lane: `kotodama-shokunin`, base `94209e8f80969dbac48d56c5d0e2e623635b8616`.
Observation window: 2026-10-24 11:33:04Z – 11:40Z (all live measurements below are stamped).
Read-only against the lane; the only write is this file. No tool installed, no pacman touched.
Artefacts read first: `reports/round-66/claims.json`, `reports/round-66/accept-ca.py`,
`reports/round-66/telemetry/{controls-ca,dry-run-ca}.txt`, `corpus/SOURCES.md` (header + S753),
`corpus/knowledge/culture-material/games-play-sport-contests.md`,
`corpus/lessons/round-65-verifier-spotcheck.md` §5/§3, fleet `PROTOCOL.md` §Evidence standard.

`lsp` note: this seat's tool set has no `lsp` device, so caller/definition checks here are
`grep`/`read` over Markdown and one Python counter — literal, not semantic proofs. No compiled
code is in scope.

## Answer to the assigned question

**Is S776 (fresh capture `20261024111013`) + the live URL sufficient durability under contract
v1, "a row is a claim only if resolvable at closure"? — Yes, for today's closure, and it is
strictly stronger than S753's own locator. But the round as specified would ship the repair
with a false observation attached, and the frozen predicate does not verify the replay it
claims. Both must be fixed before integration.**

Grounds, measured (not inferred):

- Live URL `https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf`
  → `HTTP/2 200`, `content-type: application/pdf`, `content-length: 529795`,
  `last-modified: Wed, 12 Mar 2025 19:18:25 GMT`, fetched 11:33:04Z with plain `curl`
  (no cookies, no challenge). `sha256 cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632`,
  `sha1 2f5ee6fa0fcf077704bd1934c80a697b6a1a66a2`.
- Capture `20261024111013id_` → `HTTP/1.1 200 OK`, `Content-Type: application/pdf`,
  `Content-Length: 529795`, `memento-datetime: Sat, 24 Oct 2026 11:10:13 GMT`,
  `x-archive-src: spn2-20261024082134-wwwb-spn17.us.archive.org-8004.warc.gz`;
  bytes `sha256 cb6ff9b8…` — **byte-identical to the live fetch**.
- CDX (`/cdx/search/cdx?url=…&output=json`) lists exactly two records, both
  `application/pdf`, both `200`, **digest `F5PON6QPZ4DXOBF5DE2MQCTJPNVBUZVC`** =
  base32→hex `2f5ee6fa0fcf077704bd1934c80a697b6a1a66a2` = `sha1(live bytes)`. The 2025 record
  carries length `-8498789105` (no stored payload); the 2026 record carries `386911`.
- Anchor quote is body text, PDF **page 2** (4-page PDF), under the `WHAT IS MANCALA?` heading —
  not a caption/figure/alt text, so QUALITY 16's body-scope rule is satisfied.

So the row resolves at closure *by replay*, which is the standard the round-65 spotcheck applied
to S753 (`round-65-verifier-spotcheck.md:62`, "resolvable at closure time"), and the same standard
it applied to S771 (`:61`, where a committed capture that 302s to another was accepted with a caveat).

## Findings by severity

### HIGH-1 — The statement's premise is false at review time: `20250926172224` does **not** replay 404

`claims.json` (Ca statement) and `accept-ca.py:9-13` both assert "committed capture
20250926172224 replays 404 although CDX lists 200 pdf". Measured 11:33–11:36Z:

```
/web/20250926172224id_/…sowing-seeds.pdf  → 302, x-archive-redirect-reason: found capture at 20261024111013
/web/20250926172224if_/…sowing-seeds.pdf  → 302, same
/web/20250926172224im_/…sowing-seeds.pdf  → 302, same
follow the 302 → 200 application/pdf, 529795 bytes, sha256 cb6ff9b8… (identical to live)
```

All three modifiers the round-65 spotcheck recorded as 404 (`:62`) now 302 to the fresh payload.
Cause is visible in the CDX row: the 2025 record is a payloadless revisit (negative length, digest
equal to the 2026 capture), so Wayback falls back to the only payload-bearing capture — which is
the one this round created. The round-65 404 was therefore **true when observed** (before
11:10:13Z today) and is **stale now**; this is staleness, not fabrication.

Why it still matters: the lane may not commit a 404 assertion. `PROTOCOL.md` §Evidence standard —
"An evidence pointer must resolve at closure time, not only at write time"; a receipt or lesson
line that says the old capture replays 404 is false against the bytes it ships with. Required
wording in `telemetry/s753-recapture.txt` and `corpus/lessons/round-66.md`:

> 20250926172224 is a payloadless revisit record (CDX digest equal to the 2026 capture, length
> −8498789105); at round-65 closure all three modifiers returned 404. After this round's fresh
> capture 20261024111013 landed, `id_`/`if_`/`im_` all return 302 → 20261024111013 → 200
> application/pdf, byte-identical (sha256 cb6ff9b8…). The row is repaired by the fresh capture,
> not because the old locator is independently durable.

Bonus consequence worth stating: because the old locator now resolves by redirect, the "cite
S776, cite S753 zero times" rule is a policy/durability choice, not the only resolvable option —
the lesson must not present it as "S753 became unresolvable".

### HIGH-2 — `accept-ca.py` D1 cannot fail on the clauses Ca claims: a hand-typed receipt with no network access passes

D1 (`accept-ca.py:88-110`) tests only: `"200" in receipt`, `"application/pdf" in receipt`,
`QUOTE in receipt`, `"20261024111013" in receipt`, `"S776" in receipt`, plus
`len(re.findall(r"\(S776\)", games)) == 1` and `len(re.findall(r"\(S753\)", games)) == 0`.
None of it fetches, hashes, or compares replay bytes.

Measured proof (mutation, outside the lane, `/tmp/d1mut`): a receipt whose own text says
*"FABRICATED RECEIPT — this file was typed by a mutation test. No HTTP request was made."* plus a
`sed` swap of `(S753)`→`(S776)` in the entry yields

```
D1 PASS bad=[]
```

That is the criterion-11 failure verbatim: Ca's statement contains the clause "a fresh capture
20261024111013 replays byte-exact", and no command can show that clause failing. `dry-run-ca.txt`
does not discriminate either — D1 fails at base only because the receipt file is **absent**
(`bad=['live_status','quote','capture_ts','s776','…']`), which is exactly the "a counter a
do-nothing control passes" shape QUALITY's frozen-predicate rule bars: the control proves absence
detection, not fabrication detection.

Remedy (one of two, both acceptable):
1. Strengthen D1's receipt contract *and* the leg: the receipt must carry `replay sha256: <64 hex>`,
   `live sha256: <64 hex>`, `content-length: 529795`, `memento-datetime: 2026-10-24T11:10:13Z`, and
   the CDX line; the leg checks both digests match each other and match `[0-9a-f]{64}`, checks
   `content-length` equals the byte count reported, and checks the capture timestamp equals the
   CDX timestamp string. A typed receipt then has to type two matching 64-hex digests — which it
   can still do, so this raises the bar but does not close it; pair it with (2).
2. Demote "replays byte-exact" and "live URL returns the PDF (200 application/pdf)" into
   `review_only` in `claims.json`, and keep D1 as the record leg it actually is (receipt present,
   shaped, entry citations flipped). QUALITY 11 explicitly allows a human-checked clause when
   declared review-only; it forbids covering it with a weaker stand-in.

### HIGH-3 — The D1 quote string is copyable from the registry and does not occur literally in the PDF

`QUOTE = "Versions of mancala are traditionally played across Africa and Asia"`
(`accept-ca.py:60`) is a prefix of S753's registry anchor, so it can be pasted from
`corpus/SOURCES.md:709` without opening the PDF. And it is **not** literally in the extracted text:

```
$ pdftotext live.bin live.txt; grep -c "Versions of mancala are traditionally played across Africa and Asia" live.txt
0
$ sed -n '48,50p' live.txt
Versions of mancala are traditionally played across Africa
and Asia, with gameplay and board dimensions varying
considerably between different regions.
```

The line break falls exactly inside the checked prefix. Only whitespace-normalized text matches
(`tr '\n' ' ' | tr -s ' '` → match). Therefore a receipt that claims "quote located verbatim" is
false unless it names the extraction and the normalization; the counter should require the tokens
`normalized` (or the two-line form) and the locator `page 2`, so the receipt cannot be
registry-derived prose. This is the same class as R65-M6's gzip-compressed capture note (S771):
a locator that only works after an undeclared transformation.

### MED-1 — S776 is not a registry row today, no leg checks that it exists, and it is outside Ca's declared lands

`corpus/SOURCES.md` at base and in the working tree: 701 rows, max id **S775**, `grep '^| S776 '` →
nothing. So D1 passes with a **dangling** `(S776)` citation: the entry token is counted, the row
behind it is never looked up. That is the fabricated-anchor class this seat was sent to attack.

Structural problem: `SOURCES.md` is **claim C's land** (`claims.json` C.lands). Ca's lands are
`corpus/lessons/round-66.md`, `corpus/QUALITY.md`, the games entry, three telemetry files and
`accept-ca.py`. A row landed by Ca would appear in C's land path and in the separability manifest's
C unit (`separability-manifest.json` C.lands includes `corpus/SOURCES.md`). Either:
- add `corpus/SOURCES.md` to Ca's lands and to the Ca manifest unit, and add a D1 sub-leg that
  resolves S776 in the registry, asserts it is a *new* row, `teaches` opens `supersedes S753 —`,
  `status` is a valid enum, `used-by` names the games entry, and its capture replays; or
- drop the supersession framing: keep one row (S753) with its capture re-pointed, logged old→new
  in the lesson. (The contract's `status` enum is `queued|mined|rejected` — there is no
  `superseded` state, so the flip must be a `teaches`-prefixed successor row.)

Precedent for the flip, checked: S105/S126, S034/S044, S038/S045 all keep the **old** row `mined`
with its historical `used-by` while the entry cites the successor. That is legal append-only
practice, but it means `used-by` can no longer prove S753 is cited — so D1's
`s753_citations == 0` guard must stay and must keep counting the entry, not the registry.

### MED-2 — The fresh capture is self-witnessed by this round, and is the only payload for both records

`x-archive-src: spn2-20261024082134-…` and `memento-datetime 11:10:13Z` show the capture was made
today, inside this wave (SPN2), ~23 minutes before this review. Under QUALITY 10 that is an
ordinary means and legitimate — but it is **durability, not corroboration**: it witnesses that the
page was up at 11:10Z, not that the source is independently archived. The lesson must say so, and
must not phrase S776 as a second independent witness. It also means both CDX records now resolve
through one payload record; if that record is ever excluded the 2025 row returns to 404
(`exclusion.robots` is evaluated on every replay — visible in the replay `server-timing`).
Mitigation worth one line in the row: a second independent pointer (the Expedition 58(1) issue
DOI/landing page) so the repair does not rest on a single SPN capture.

### LOW-1 — Claim C's after-value "registry 701 -> 725+ rows" is unfalsifiable

`claims.json` C now reads "701 -> 725+ rows including the S776 supersession repair and disposition
rows". No leg counts registry rows, and "+" cannot fail. Once the S776 decision in MED-1 is made,
pin an exact number (725 if no successor row, 726 if S776 lands) and have one leg count
`^| S[0-9]` rows — otherwise criterion 11's "each clause shown able to fail" is unmet for the
registry count. (Adjacent to D1, flagged because the S776 decision changes the number.)

### LOW-2 — No future-dated-evidence defect

Capture `11:10:13Z` precedes `controls-*.txt`/`dry-run-*.txt` writes (11:25–11:29Z) and any commit.
`PROTOCOL.md`'s "timestamp at or before the shipping commit" is satisfied.

## Required changes for the integration to be honest

1. `telemetry/s753-recapture.txt`: record the **302**, the redirect reason, the payloadless-revisit
   diagnosis, page 2, whitespace-normalized quote match, `live sha256`, `replay sha256`, both
   equal, `content-length 529795`, `memento-datetime`, and the two CDX rows with their digests and
   lengths. Do not write "404" as a present-tense observation.
2. `accept-ca.py` D1: either the digest/Content-Length/timestamp comparison of HIGH-2 remedy 1, or
   move the fetch/replay clauses to `review_only` in `claims.json` (remedy 2) — not both half-done.
   Add the page/normalization token check of HIGH-3.
3. Decide S776's home (MED-1) and make it a checked object or a logged in-place re-point; then pin
   C's registry after-value (LOW-1).
4. `corpus/lessons/round-66.md`: S753 `used-by`/capture change logged old→new; S776 (if it lands)
   `teaches` opening `supersedes S753 —`; the self-witness sentence of MED-2.

## Residual risk (accepted, not defects)

- Wayback can exclude a capture retroactively; the repair rests on one SPN payload record. Second
  pointer recommended, not required by any criterion.
- `20250926172224` will keep resolving only while a payload-bearing sibling exists; the old row stays
  non-self-sufficient and the lesson should say so rather than declare it fixed.
- The 2025 and 2026 records are the same bytes, so the fresh capture adds a payload, not new
  content; "re-captured" must not be read as "page changed since 2025".

## Verification gaps in this review

- The real-tree D1 was not exercised: `s753-recapture.txt`, the S776 row and the entry swap do not
  exist yet, so D1's PASS/FAIL on integrated bytes is unmeasured here; the fabrication test ran on
  a `/tmp/d1mut` copy with a fabricated receipt (result quoted above).
- Live measurements are point-in-time (11:33–11:36Z). `web.archive.org` rate-limited this seat
  after ~6 requests (`curl: (7)` transient), so each figure above is from one successful
  request; the `if_`/`im_` 302s were re-taken after a 20 s pause and agreed with `id_`.
- No `lsp` server in this seat; no semantic cross-reference proof beyond grep/read.
