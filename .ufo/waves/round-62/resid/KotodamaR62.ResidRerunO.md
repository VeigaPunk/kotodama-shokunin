VERDICT KotodamaR62.ResidRerunO: HOLDS

Seat: KotodamaR62.ResidRerunO (residual falsify call, claim O). Lane /home/vgpnk/Projects/shokunin/kotodama-shokunin, measured revision a2c5caa59b2d67ce35e53d6ce0217030a66cdd48. Independent sandbox clone at /fast/scratch/hyaku/kotodama-r62/resid/KotodamaR62.ResidRerunO/clone (`git clone` of the lane + `checkout -q a2c5caa…`, GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset; `git status --short` = 0 lines, HEAD = a2c5caa "round-62: claim D — footwear lines 63/74/75/93 repaired in place …"). Python 3.14.8. No tools installed (none needed); no pacman transactions. Nothing written in the lane except this report; all probes under the scratch dir above; every process capped with `timeout`; all servers/threads started were shut down before return.

====================================================================
1. REPRODUCTION — claim O counter, two independent runs
====================================================================
Integrity: `sha256sum reports/round-62/accept-o.py tools/reopen-row.py` in the clone →
  a222a156b95e0f716f0304c85bc38c2eb395f5dad5c9b4810476a87237ca8ba9  reports/round-62/accept-o.py   (== claims.json freeze accept_o_sha256, 9143fc44)
  21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803  tools/reopen-row.py            (tool itself is not hash-frozen)

Command (twice, per assignment): `timeout 1200 python3 -B reports/round-62/accept-o.py` in the clone root.

RUN 1 (full output, exit 0):
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=53 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=53 expected=53 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S4330', 'REFUSED', 0), ('S3743', 'REFUSED', 0), ('S8567', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1280', 'UNREACHABLE', 9)] wall=151s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: PASS
RUN1_EXIT=0

RUN 2 (full output, exit 0):
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=53 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=53 expected=53 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S4743', 'REFUSED', 0), ('S1595', 'REFUSED', 0), ('S1119', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7040', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: PASS
RUN2_EXIT=0

Both runs PASS with different run-time random fixtures (PRIV ids S4330/S3743/S8567 vs S4743/S1595/S1119; DEFAULT id S1280 vs S7040), matching the shape of the L1's sole authoritative run in reports/round-62/telemetry/final-measures.txt (PRIV S1893/S6592/S7009, DEFAULT S1750 wall=150s). The frozen predicate ACCEPT-O-62 (every leg PASS) holds on independent hardware/processes. These runs are attacks/reproductions; the receipt stands untouched.

====================================================================
2. SELFTEST
====================================================================
Command: `timeout 300 python3 -B tools/reopen-row.py --selftest` (clone root). Full output, exit 0:
-- selftest: verdicts --
ok   verdict S1: ('LOCATED', 'attempts=1')
ok   verdict S10: ('LOCATED', 'attempts=2')
ok   verdict S11: ('UNREACHABLE', 'attempts=1')
ok   verdict S12: ('UNREACHABLE', 'attempts=9')
ok   verdict S13: ('NO_QUOTE', 'attempts=0')
ok   verdict S14: ('NO_QUOTE', 'attempts=0')
ok   verdict S15: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S16: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S17: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S18: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S2: ('LOCATED', 'attempts=1')
ok   verdict S3: ('LOCATED', 'attempts=1')
ok   verdict S4: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S5: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S6: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S7: ('ABSENT', 'attempts=1')
ok   verdict S8: ('ABSENT', 'attempts=1')
ok   verdict S9: ('LOCATED', 'attempts=3')
ok   summary: True
ok   exit code: 1
ok   no row: ('NO_ROW', 'attempts=0')
-- selftest: retry bound --
ok   transient hits: 3
ok   transient verdict: ('LOCATED', 'attempts=3')
-- selftest: private refusal --
ok   refused verdict: True
ok   refused hits: 0
ok   refused exit: 1
-- selftest: bad inputs --
REOPEN_ERROR: no row ids given
ok   no ids exit: 2
REOPEN_ERROR: cannot read registry /tmp/reopen-row-selftest-fyyh7el8/nope.md: [Errno 2] No such file or directory: '/tmp/reopen-row-selftest-fyyh7el8/nope.md'
ok   missing registry exit: 2
REOPEN_ERROR: --passes must be an integer >= 1
ok   passes zero exit: 2
REOPEN_ERROR: --gap must be a number >= 0
ok   gap not a number exit: 2
REOPEN_ERROR: unknown option --nope
ok   unknown option exit: 2
REOPEN_ERROR: registry /tmp/reopen-row-selftest-fyyh7el8/BAD.md is not valid UTF-8: 'utf-8' codec can't decode byte 0xff in position 7: invalid start byte
ok   bad utf-8 exit: 2
-- selftest: 32 checks, 0 failures --
SELFTEST_EXIT=0

====================================================================
3. CONTRACT-GAP ANALYSIS — sentences the fixture does not exercise
====================================================================
Method: accept-o.py docstring "Tool contract" paragraph, sentence by sentence, vs GEN/BOUND/… coverage, then local probes (scratch/probe.py, scratch/probe2.py; local HTTP fixture servers + unit calls into the tool module; full outputs in scratch/run1.txt, run2.txt and the probe transcripts below).

[O-1] MEDIUM — Redirects: contract silent; tool auto-follows, and the private-address policy is NOT re-applied to redirect targets.
  Evidence (probe.py P7, run with --allow-private): row URL = serverA/redir, 302 → serverB/body.
    [REDIR] exit=0 ROW S9008 LOCATED attempts=1 url=http://127.0.0.1:36483/redir | REOPEN: 1/1 located
    hitsA/redir=1 hitsB/body=2   (one new request to server B — the redirect target — for this row)
  The tool made 2 HTTP requests but reports attempts=1, and url= names the listed entry URL, not the target.
  Code: tools/reopen-row.py run_pass calls fetcher.refused(url) only on the row's listed URLs (`if fetcher.refused(url): continue`); Fetcher.fetch uses plain urllib.request.urlopen, whose default opener follows 301/302/303/307/308 (cross-host) without consulting refused(). A public entry URL that redirects to a loopback/private address is therefore fetched with no --allow-private — the exact scenario the policy exists for. A public first hop is not reproducible offline (any local host is itself refused), so the bypass itself is code-cited; the probe proves the follow mechanism. claims.json's known residual parks "requests to hosts other than the local fixture server" as review-only; this finding sharpens it (policy bypass + counting delta), it does not contradict the frozen predicate (no redirect fixture exists, legs legitimately PASS).
  Smallest fix: install an opener whose redirect handler re-consults Fetcher.refused() on each Location target (raise a refused-class error), or document the gap in the tool docstring; a later-round counter that wants BOUND-strength coverage must add a redirect fixture class.

[O-2] MEDIUM — attempts= undercounts whenever a redirect chain runs. Contract: "n = HTTP requests and connection attempts made for that row over all passes".
  Evidence (probe.py P8, redirect to itself): actual HTTP requests observed at the server = 5 (stdlib max_repeats=4 for a repeated target); tool printed:
    [LOOP] exit=1 ROW S9009 UNREACHABLE attempts=1 url=- | REOPEN: 0/1 located
  (the give-up HTTPError 302 is classified FatalFetch, ending the URL after one counted attempt). P7 likewise: 2 requests, attempts=1. The GEN/DEFAULT legs cannot see this (no redirects in the fixture).
  Smallest fix: count requests inside a custom redirect handler (or reword the contract sentence); otherwise leave documented.

[O-3] LOW — "Fetch: GET, timeout 30 s" is per socket operation, not a per-request deadline.
  Evidence: P13 — server accepts, never responds: `stall: TransientFetch(timed out) after 30.0 s (FETCH_TIMEOUT=30.0)` (retry budget then applies: 3 attempts/pass × 3 passes, ~14 min worst case per stalling row — bounded, consistent with the design).
  P14 — trickling server (chunks every 11 s, each < 30 s): `trickle: status=200 elapsed=44.0 s (>30 s deadline?) quote_found=True` — any wall time is reachable with a slow drip; no transient, no retry. Contract sentence overstates; behaviour is stdlib semantics. No fixture exercises any of this.
  Smallest fix: one docstring sentence ("timeout is per socket read/connect").

[O-4] LOW — 4 MiB silent truncation. MAX_BODY_BYTES = 4 MiB; fetch() does response.read(MAX_BODY_BYTES) and discards the remainder with no signal; neither tool docstring nor contract mentions the cap.
  Evidence (probe2.py): 5 MiB page, quote in the last bytes → `ROW S9021 ABSENT attempts=1 url=-` (indistinguishable from a genuinely absent quote → a row would be re-opened as ABSENT/failed for a page-size artifact). Same-size page just under the cap → LOCATED. (probe.py P6 first attempt: my own fixture route raised TypeError → server hung up → tool printed UNREACHABLE attempts=9 — incidentally confirming "connection error = transient" and the 3×3 retry bound on a real hangup.)
  Smallest fix: document the cap in the docstring OUTPUT section (a TRUNCATED marker would need a counter revision).

[O-5] LOW — content-encoding is ignored. The tool sends no Accept-Encoding (headers are User-Agent/Accept only) and never decodes Content-Encoding: gzip.
  Evidence (probe.py P4): gzip-compressed HTML containing the quote → `ROW S9004 ABSENT attempts=1 url=-`. Well-behaved servers won't gzip an uncompressed request, but CDN forced compression silently kills every match. Unexercised and undocumented.
  Smallest fix: document; optionally gzip.decompress when Content-Encoding: gzip.

[O-6] INFO — JSON and PDF bodies. Contract sentence "A non-HTML body (text/plain, JSON) is BODY text as a whole": the fixture exercises text/plain only. Probes: application/json with the quote → LOCATED attempts=1 (P2, contract-consistent). application/pdf is not in the contract; the tool treats it as text: an uncompressed text-stream PDF → LOCATED (P3); a real compressed PDF decodes to garbage → ABSENT (same path as O-5).

[O-7] INFO — Non-200 2xx. 204 No Content → `ROW S9005 ABSENT attempts=1 url=-` (P5): consistent with "some URL answered 2xx" → ABSENT; the fixture only serves 200.

[O-8] INFO — Refusal classes. Fixture exercises only 127.0.0.1. Unit probes of Fetcher.refused() without --allow-private: 10.1.2.3, 172.16.0.9, 192.168.1.1, 169.254.169.254, 0.0.0.0, [::1], localhost (resolves to loopback), 240.0.0.1, 198.51.100.7, 203.0.113.9, nosuchhost.invalid → all refused=True without a request (contract-consistent). 100.64.0.1 (CGNAT shared space, RFC 6598) → refused=False: the tool would fetch it; the contract's list does not include shared space, so this is contract-consistent, but the policy is narrower than a security-minded reader might assume. A mixed refused+allowed row is not reachable offline without --allow-private (any local fixture host is itself refused): probe P9 (10.9.9.9 + local server, no flag) → `ROW S9010 REFUSED attempts=0 url=-`, re-confirming PRIV; per-URL refusal is by construction in run_pass (refused URLs are skipped, refused_all only if every URL refused).

[O-9] INFO — Multi-URL retry schedule beyond the fixture's live+arch pairs. P10 (503-always URL + answered-no-match URL, gap 0, 3 passes): `ROW S9011 ABSENT attempts=12 url=-`; server saw /dead +9 (3 attempts × 3 passes) and /absent +3 (1 × 3). The 3-attempts-per-URL-per-pass bound and the "repeat only on transient" rule hold across URLs; the fixture never exercises a multi-URL row that ends ABSENT with transient_seen.

[O-10] INFO — url= convention on redirect matches. P7: url= reports the listed entry URL (/redir), not the redirect target that carried the body. Contract's "the URL that gave the verdict's match" is ambiguous here; the tool consistently reports a listed URL (same as DEAD_ARCHIVE reporting the capture). Worth one clarifying word in a future contract revision.

[O-11] INFO — Text mechanics the fixture never exercises, verified by unit probe (P12) to match the contract: curly-quote spans extracted (“…”, and German „…“); NFKC folding (ﬂag/ﬁne/ｘｙ → flag/fine/xy); unbalanced-paren trim (`url).` → `url`, balanced `url_(a).` kept intact, `url_(a` kept). The fixture does exercise the trailing-dot trim implicitly (its URLs are followed by "." in the source cell and GEN checks url=).

====================================================================
4. RESIDUAL RISK
====================================================================
- F1/F2 (redirects) sit exactly in the neighbourhood claims.json already parks as review-only ("requests to hosts other than the local fixture server are not observable by BOUND"); they do not affect the frozen predicate, but if a later round uses reopen-row.py on live registries, a public→private redirect would be fetched and under-counted. The S693 block's locator targets are the same hosts the entry already cites, so exposure this round is negligible.
- O-4/O-5 can turn a real "quote present" page into a silent ABSENT (large or gzipped pages); for current SOURCES rows (ordinary article pages) the risk is remote.
- Python 3.14.8-specific behaviours (e.g. 100.64/10 not private) could differ under other interpreters; my runs used the host's python3, same as the receipt.

====================================================================
5. VERIFICATION GAPS
====================================================================
- No live fetches: claim O is judged offline by design; S665/S671 live behaviour stays review-only.
- The redirect policy bypass (O-1) is code-cited plus mechanism-proven with --allow-private; the no-flag public-first-hop case was not executed (no offline way to get a resolvable public first hop without touching system resolver state).
- Attempts-undercount magnitudes beyond the 5-request loop and 2-request redirect were not enumerated.

No installs performed. All scratch servers, threads and sockets were shut down; no processes left running; the lane repo is untouched except this report file.
