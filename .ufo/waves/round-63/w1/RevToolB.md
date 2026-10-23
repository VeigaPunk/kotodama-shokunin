# RevToolB — Independent claim-O review: malformed-URL & robustness surface

Seat: `kotodama-r63-w1-RevToolB` (reviewer, leaf). Review time: 2026-10-23 ~19:04Z UTC.
Objects: claim O (`ACCEPT-O-63`) — repair of `tools/reopen-row.py`; lane repo
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`; freeze `80d53ff` (round base
`65b393e`); counters `reports/round-63/accept-o.py` (sha256
`a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` verified) and
`accept-c.py` (`3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`
verified). Method: read-only code review + stdlib probes (urllib.parse /
urllib.request / socket). The held tool was never executed (QUALITY 16 hold).

## 0. What was reviewed (state at review time)

* Lane tip: `a4bef27` (wave spec); freeze `80d53ff`; instruments revision 1 at
  `138212a` (pre-data, forced by RevCounterO: REVIEW leg gained substance + open-
  finding-marker checks, TIMEOUT leg pins the requested budget via stall
  timestamps).
* `tools/reopen-row.py` in the lane is still the round-62 held blob
  (`c31ac76a`, identical at 65b393e/80d53ff/tip). No repair is committed.
* The repair seat (ExecRepairTool) has drafted the repair in scratch:
  `reopen-row.py` at 2026-10-23T19:01:44Z, 1218 lines, sha256
  `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5`;
  `compile()` clean. This review evaluates that candidate in full; per the
  claims, RevHoldLift must re-run the gate on the LANDED bytes.
* Update at 19:1xZ: the candidate is now LANDED — commit `dd81fd2` carries
  `tools/reopen-row.py` byte-identical to the reviewed candidate (sha256
  `0d965ccb…`, mode 755; verified against this seat's clone), and instruments
  revisions 5 (`09b8b96`) and 7 (`0cb8cba`) revised the REVIEW leg pre-first-run
  as described in §2.

## 1. Assigned surface — item-by-item

### 1.1 Redirect re-validation (bad port 99999/-1/empty, IPv6, empty host)
**CLOSED-by** the candidate:
* `parse_target()` classifies unparseable port (`.port` ValueError → BadUrl),
  unbalanced bracketed IPv6 (urlsplit ValueError → BadUrl), empty host (hostname
  None → BadUrl), non-http(s) scheme, and port range 1-65535.
* `_NoRedirect(HTTPRedirectHandler)` makes the library never auto-follow;
  `follow()` resolves each Location by hand with `urljoin` (scheme-relative
  covered), compares authority `(lowercased host, effective port 80/443)`, and:
  - cross-authority hop must pass `private_host()` even under `--allow-private`;
  - same-authority hop must pass it in default mode;
  - chain cap 5 requests; a redirect on the 5th response ends the URL fatally;
  - every request in the chain is counted as an attempt.
* userinfo hosts are stripped by `urlsplit().hostname`; IPv6 literals compare by
  hostname; IDNA/punycode hosts resolve through `getaddrinfo` (probed).
* Matches counter expectations: REDIRECT_OK attempts=2/LOCATED/final url;
  REDIRECT_MULTI attempts=4; REDIRECT_LOOP attempts=5 with hits l1=3/l2=2;
  REDIRECT leg attempts=1 REFUSED under --allow-private with 0 target hits, 0
  source hits without the flag. The round-62 SSRF (cross-authority follow) is
  closed.

### 1.2 Malformed registry URLs
**CLOSED-by** the candidate: `run_pass` calls `parse_target()` per URL BEFORE
`refused()` and before `allow_private` short-circuits. Malformed → no request,
attempts=0, no retry, no gap sleep, `MALFORMED` recorded for that URL; row and
run continue; an all-malformed row prints `ROW <ID> MALFORMED attempts=0 url=-`
and the run exits 1 without traceback. `VERDICT_RANK` gained `MALFORMED: 0`
(and `TRUNCATED: 3`), so `process_row` cannot KeyError.

### 1.3 Source cell: live URL fine, capture URL malformed
**CLOSED-by**: per-URL classification — a malformed capture adds `MALFORMED`
to the row's outcomes, never raises; if the live URL answered 2xx without the
quote the row is ABSENT (attempts=1), if all URLs are malformed the row is
MALFORMED. No run abort.

### 1.4 MALFORMED × pass/retry schedule
**CLOSED-by**: malformed is not transient — no retry, no `sleep`; later URLs in
the row and later rows proceed; verdict selection handles all-REFUSED /
all-MALFORMED / mixed-without-TRIED mixtures (REFUSED outranks MALFORMED as
frozen).

### 1.5 Exit-status contract
**CLOSED-by**: registry data errors → clean per-row lines + exit 1 (via
`all_located`); invocation errors (unknown option, missing registry, invalid
UTF-8 registry, `--passes 0`, `--gap x`, `--timeout 0`, non-numeric timeout,
inf/nan) → `REOPEN_ERROR` + exit 2, no Traceback.

### 1.6 Per-request deadline (drip body / budget)
**CLOSED-by**: `--timeout SECONDS` (default 30, must be > 0 and finite) is a
wall budget: `deadline = monotonic() + timeout`; the opener's socket timeout is
the remaining budget and `_read_body` re-checks the deadline between chunks and
re-bounds the socket by `remaining`; a stall/drip body cannot outlive the
budget (expiry → TransientFetch, retried). With the rev1 TIMEOUT leg
(`--timeout 2 --passes 1 --gap 0`, stall endpoint), 3 attempts ≈ 2s each give
span ≥ 3.0s and wall < 20s as required.

### 1.7 Deadline × retry/gap wait (race)
**CLOSED-by**: the only sleeps are `min(gap,5)` between attempts (inside
`run_pass`) and `gap` between passes — both outside `fetch()`; the budget is
per request only, so no race, no starvation, no budget leak into waits.

### 1.8 Companion surfaces (gzip, truncation, attempts)
**CLOSED-by**: `gunzip()` decompresses Content-Encoding gzip (cap 64 MiB of
expansion; zlib error → FatalFetch); `_read_body` reads 4 MiB + 1 byte — one
byte past the cap — so truncation is detected (TRUNCATED when the quote is
absent from the bytes read, LOCATED/CAPTION_ONLY when inside); redirect-chain
requests all count as attempts.

## 2. Findings

* **HIGH — gate: counter revision 1's REVIEW leg was unsatisfiable.**
  The leg required every report to carry the fixed closing token AND to be free
  of the marker regex `\bOPEN\s*[\(\-:]?\s*(HIGH|MEDIUM|MED)\b`. Executing that
  exact regex from the committed counter against the exact token string yields a
  match (the token's own upper-case O-P-E-N, hyphen, H-I-G-H sequence), so any
  report that satisfies the token requirement was necessarily flagged
  `open_findings`: `tokens==4` and an empty taint list were mutually exclusive
  and the leg failed on every possible input.
  **RESOLVED (instruments revision 5 `09b8b96`, then revision 7 `0cb8cba`, both
  pre-first-run):** revision 5 exempted the mandated token from the marker scan
  — the exact remedy proposed here — and revision 7 restored the token
  requirement with a replace-based scan that still catches an inline finding
  next to the token. The repair itself landed at `dd81fd2` (build `0d965ccb`,
  byte-identical to the candidate reviewed below, mode 755 — verified against
  this seat's clone). No longer blocking.
* **LOW (open, pre-existing or cosmetic):**
  - `http://host:` empty-port suffix silently defaults to 80 (parse_target port
    None → default) instead of MALFORMED;
  - control characters inside a URL are not classified malformed (reach the
    wire under --allow-private → server 4xx → FatalFetch; or fail DNS → refused);
  - scheme-only `http://` does not match `URL_RE` → row mislabelled NO_QUOTE;
  - `trim_url` strips a legitimate trailing `.`;
  - an unresolvable host is classified REFUSED (fatal) rather than transient
    (pre-existing semantics).

## 3. Residual risk

* The candidate was reviewed statically before landing; it is now committed
  (`dd81fd2`), and RevHoldLift re-runs the gate on the landed bytes — which are
  byte-identical to what this review traced, so no semantic drift is expected.
* This review is static (code walkthrough, compile check, stdlib probes); the
  tool was not executed, and the counter was not run (control seats). Genuine
  endpoint behaviour (server header edge cases, multi-member gzip) remains for
  the closure's admission-time runs.
* The REVIEW leg was fixed in instruments revisions 5 and 7, and the candidate
  is now the landed bytes (`dd81fd2`): the remaining open items in §2 are all
  LOW; no high/medium surface defect remains in the tool as reviewed.

## 4. Verification gaps

* No execution of the held tool; no first-run counter receipts (not this seat's
  role). Code-level expectations were mapped to every counter leg and fixture
  class with line references.
* Probes used: urlsplit/port/hostname edge cases; urllib.Request control-char;
  urlopen empty-host/scheme-only; getaddrinfo IDNA/punycode; default-opener
  cross-authority redirect follow; the exact marker regex against the token;
  and a re-execution of the revision-7 scan over this report's own updated text
  (token present, zero taint) before writing.

## 5. Verdict

The one HIGH gate item (self-matching marker scan in instruments revision 1) is
RESOLVED by pre-first-run revisions 5 and 7; the repair under review is now the
landed bytes at `dd81fd2`, byte-identical (sha256 `0d965ccb…`) to the candidate
reviewed in §1. Remaining open findings against the landed source: the LOW
items of §2 only. No high- or medium-severity item is open in this seat's
scope. The safety hold may lift per the frozen rule once RevHoldLift re-runs
the gate on the landed bytes and all four reports carry the token.

VERDICT: NO-OPEN-HIGH-MED
