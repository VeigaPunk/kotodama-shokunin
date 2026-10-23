# RevToolC — independent review gate, claim O: data-integrity surface (round 63)

Seat: kotodama-r63-w1-RevToolC (leaf, no delegation, no execution of the held tool).
Reviewed bytes: `tools/reopen-row.py` sha256 `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5`
(landed in the lane working tree during this review; byte-identical to the candidate I diffed from
`ExecRepairTool/reopen-row.py`), against the frozen blob `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803`
at `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` (clone at `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-RevToolC/clone`,
full 713-line diff kept as `repair.diff` there). Contract source: docstring of `reports/round-63/accept-o.py`
(sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`, revision 0) and
`reports/round-63/claims.json`. Method: read-only code review of the whole diff plus the counter's fixture/leg
code; the tool was never run (QUALITY 16 hold honored, `--selftest` included); no counter was edited.

## 1. Gzip handling — CLOSED

- Decode order is right: the wire body is read capped, `Content-Encoding` is read lowercased
  (`(headers.get("Content-Encoding") or "").lower()`), and `gunzip` runs inside `fetch()` BEFORE
  `split_content`/charset decode, so body and figcaption matching both see plaintext (GZIP leg: LOCATED and
  CAPTION_ONLY at attempts=1).
- Zip-bomb bound: `zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(raw, GZIP_LIMIT + 1)` bounds the output
  at 64 MiB and the input is already bounded at 4 MiB + 1; memory ceiling ~64 MiB, no decompression loop, and
  `zlib.error` maps to `FatalFetch` (no traceback, attempt counted via `counter[0]`). No unbounded
  `gzip.decompress` anywhere.
- Case handling: header lowercased before the `"gzip" in encoding` test — `GZIP`, `GZip` decode.
- Multiple encodings: only `gzip` is claimed by the claim; `"gzip, gzip"` degrades to one gunzip pass;
  `deflate`/`br` pass through undecoded (residual R-2).

## 2. 4 MiB truncation semantics — CLOSED

- The read is `MAX_BODY_BYTES + 1` in 64 KiB chunks; `truncated = len(body) > MAX_BODY_BYTES`. EOF-based, so a
  body of exactly 4 MiB is not misflagged, and the +1 read is what makes the distinction observable.
- Straddling quote: the contract as frozen ("TRUNCATED when the quote is absent from the read bytes, LOCATED
  when inside") is the right contract, and the artifact states and implements it: matching is a contiguous run
  of whole normalised words over the capped bytes, so a quote that starts before the cap and ends after it is
  absent from the read bytes and yields TRUNCATED — never a partial LOCATED, never a silent ABSENT. Code path:
  2xx, no body match, no caption match, `response.truncated` -> `truncated_seen`; row TRUNCATED only when some
  page answered 2xx and no page gave a clean absence; ranked equal to ABSENT (rank 3), `url=-`, attempts
  unchanged, not transient (single pass).
- TRUNC_NEAR: the search returns before truncation bookkeeping matters, so a quote inside an over-cap body is
  LOCATED. Counter TRUNC leg covers both directions plus `url=-`.
- gzip interplay: the 4 MiB cap applies to the compressed read; decompressed expansion is separately capped at
  64 MiB and the docstring says so. Consequence: a quote at 4.5 MiB decompressed on a gzipped page is
  searchable where the same plain page would be TRUNCATED — a documented, bounded asymmetry (residual R-1).

## 3. Attempts counting across chains — CLOSED

- `follow()` increments `counter[0]` once per HTTP request before issuing it; `run_pass` adds `counter[0]` to
  `attempts` on every exit path. So hops made before a mid-chain failure are counted (302 then a timing-out hop
  = attempts 2), a refused redirect counts exactly the requests actually made (REDIRECT leg: attempts=1 with
  `--allow-private`, attempts=0 without, since the initial loopback URL is refused pre-request), and the 5th
  response being a redirect ends the chain as `FatalFetch` at attempts=5 (REDIRECT_LOOP: UNREACHABLE, hits
  l1=3/l2=2).
- Retries restart the chain with a fresh counter; the transient budget stays 3 per URL per pass, so
  TRANSIENT2/TRANSIENT_PASS totals (3 and 4 via passes) and DEFAULT's 9-attempt burst shape are unchanged.
- No-request classes untouched: MALFORMED rows are filtered by `parse_target` before `refused()`/`follow()`
  (attempts=0, no request, exit 1, no traceback), NO_QUOTE/NOROW still attempts=0.

## 4. REFUSED-on-redirect-refusal vs the round-62 verdict vocabulary — CLOSED

- The repair invents no new token for this case: it reuses `REFUSED` in the round-62 slot. Updated rank table
  is `LOCATED 5 > CAPTION_ONLY 4 > ABSENT 3 = TRUNCATED 3 > UNREACHABLE 2 > REFUSED 1 > MALFORMED 0` —
  TRUNCATED ranked equal to ABSENT and MALFORMED below REFUSED, both as the contract paragraphs demand.
- ROW line shape, REOPEN summary, ordering and exits are unchanged: registry-data outcomes exit 1; invocation
  and unreadable-registry errors exit 2 with a `REOPEN_ERROR` line (`--timeout 0`, `--timeout x` included in
  parse_args validation: float, `> 0`, NaN rejected via `not timeout > 0`, +/-inf rejected explicitly).
- Traceback-freedom is strengthened: `BadUrl`, `gunzip` failure and `http.client.HTTPException` (newly caught —
  this also closes a latent pre-existing crash on `IncompleteRead`/`BadStatusLine`, which inherits
  HTTPException but not OSError) all map to verdicts or transients.
- Redirect policy matches the frozen paragraph exactly: authority = (lowercased host, effective port with
  scheme default); a hop to a different authority must pass `private_host()` even under `--allow-private`; a
  same-authority hop must pass it whenever `--allow-private` is absent. Scheme is intentionally not compared
  (port default differs 80 vs 443, so http->https hops are cross-authority but pass when the target is public —
  live publisher hops keep working). Userinfo is stripped by `.hostname`; bracketed IPv6 literals compare
  bracket-free and lowercased; scheme-relative Locations resolve through `urljoin`; an unresolvable hop host is
  refused (conservative); a 3xx without Location is fatal, counted.

## 5. Regression risk: round-62 GEN classes byte-identical — CLOSED

Walked every class tuple (verdict, attempts, per-path hits, reported url) of the counter's GEN battery against
the new code path: BODY/BODY_SPLIT/PLAIN, all ten CAP_* classes, SCRIPT/ABSENT, TRANSIENT2 (3),
TRANSIENT_PASS (4, via passes), DEAD_ARCHIVE (2, arch url), ARCHIVE_CAPTION, DEAD_THEN_BODY2 (live 3 + arch 1),
BODY_THEN_ARCHIVE (arch hits 0), DEAD (9), GONE (fatal, 1), NOQUOTE/SHORT/NOROW (0 requests) — all reproduce;
plus the eight new classes REDIRECT_OK (2, target url), REDIRECT_MULTI (4), REDIRECT_LOOP (5),
MALFORMED_PORT/MALFORMED_IPV6 (0), GZIP_BODY, TRUNC_FAR (TRUNCATED, url=-), TRUNC_NEAR (LOCATED).
The only behavioral deltas are: (a) the opener is built with `_NoRedirect` — identical for non-3xx answers;
(b) the body is read chunked at cap+1 — same bytes; (c) attempt totals flow through `counter[0]` — same
numbers; (d) 3xx answers return as a `Response` instead of being silently followed by the library — the old
GEN routes contain no 3xx; (e) HTTPException now transient — broadening only. Attempt/pass schedule
(`min(gap,5)` between retries, `gap` between passes) is untouched, so DEFAULT's bursts [3,3,3] with 55-75 s
gaps and PRIV's zero-request refusal survive as-is. `parse_args` keeps last-wins flag parsing (the selftest's
`extra=["--timeout","1","--passes","1"]` composition still resolves correctly).

## Residual risk (all LOW; nothing open at high or medium severity)

- R-1 (low) plain-4MiB vs gzip-64MiB search-surface asymmetry — bounded and documented in the tool docstring.
- R-2 (low) `Content-Encoding` matched by substring `"gzip"`: admits `x-gzip` (harmless, same container);
  other codings are not decoded — only gzip is claimed.
- R-3 (low) a 200 whose gzip stream is corrupt ends that URL fatal, so a row can print UNREACHABLE although a
  2xx was answered; bounded, no request amplification, vocabulary-consistent.
- R-4 (low) 100.64.0.0/10 is not `is_private` on this runtime (verified on python 3.14.8: False) — the
  pre-existing round-62 CGNAT residual, outside this round's routed set, unchanged by the repair.
- R-5 (low) `_resolved` caches DNS for the whole run; a rebinding between the first refusal check and a later
  hop can pass the address check. Pre-existing class; the redirect validator does re-resolve previously unseen
  hop hosts. Review-catalog item, not a counter fixture.
- R-6 (cosmetic, pre-existing) the docstring's "pass verdict" ranking sentence predates the repair and is
  untouched; the operative table is `VERDICT_RANK`.

## Verification gaps

- Static review only; the tool was not executed (QUALITY 16 hold), `--selftest` included. The counter cannot
  observe mid-chain transient attempt accounting, drip (vs stall) bodies beyond the 2 s stall fixture, gzip
  streams larger than 4 MiB compressed, or exactly-4 MiB bodies; those four are argued from code, not measured.
- This verdict is bound to sha256 `0d965ccb…`. If the landed/re-measured bytes change before the first
  accept-o.py run, this gate must be re-run against those bytes.

Records: no tool installs or upgrades were needed (operator rule 2026-10-19: none performed). Writes outside
this report: only under `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-RevToolC/` (clone at the freeze,
`repair.diff`, `reopen-row.diff`). No git/jj commands against the lane or fleet repos; git used read-only
inside my own clone.

VERDICT: NO-OPEN-HIGH-MED
