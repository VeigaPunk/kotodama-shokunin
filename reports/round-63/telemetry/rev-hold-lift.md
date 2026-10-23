# rev-hold-lift — residual review of the landed bytes of tools/reopen-row.py

Reviewed bytes: `git show main:tools/reopen-row.py` at dd81fd29; content sha256
`0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5`, equal to
`reports/round-63/telemetry/freeze-sha256.txt` and to the claimed build sha 0d965ccb;
1217 lines; git mode 100755. Compared against the round-62 baseline 65b393e (plain
`urllib.request.urlopen` that auto-follows redirects, a silent `read(MAX_BODY_BYTES)`
cap, and a bare per-open socket timeout) and against the round-62 closure catalog
(redirect-to-private SSRF incl. cross-authority hop rule, malformed URLs, gzip,
truncation, per-request --timeout budget, attempt counting, exit contract).

Method: read-only review plus offline execution only — the built-in `--selftest`
(49 checks, 0 failures) and an independent probe harness served from 127.0.0.1
fixtures (scheme-relative and userinfo Locations, infinite redirect loop, ftp
Location, gzip-expansion bomb, silent-stall body, dripping body). No live URL was
fetched; the accept counter was not executed by this seat (first run belongs to
the counter, not to a review). No tool installs or upgrades were performed.

## Catalog status on the landed bytes

- Redirect-to-private SSRF incl. cross-authority hop rule: HOLDS. `_NoRedirect`
  stops library-level following; every hop is re-resolved by hand and compared by
  (lowercased hostname, effective port) from `parse_target`; a cross-authority hop
  must pass `private_host` even under `--allow-private` (follow(), lines ~640-660).
  Selftest S20: REFUSED attempts=1 with the hop target untouched (0 hits). My probe:
  a scheme-relative `Location: //127.0.0.1:<other-port>/secret` is REFUSED
  attempts=1 with 0 hits on the target; a `ftp://` Location is FatalFetch with no
  request made; a 5-hop loop ends after exactly 5 requests (UNREACHABLE, and not
  retried because FatalFetch is not transient). Userinfo cannot smuggle a private
  host past the check: the authority comparison uses `parts.hostname`, which strips
  userinfo before comparison (fetch-layer consequence under LOW-1).
- Malformed URLs: HOLDS. Bad port, unbalanced bracketed IPv6 and empty host are
  answered `ROW <ID> MALFORMED attempts=0 url=-` (selftest S21-S23), the run exits
  1 (not 2), no traceback, and no request is made; REOPEN_ERROR + exit 2 is
  reserved for invocation/registry input errors.
- Gzip: HOLDS. Content-Encoding gzip is decompressed before matching (S24 LOCATED),
  with a 64 MiB expansion cap; a bomb whose quote lies past the cap is answered
  TRUNCATED attempts=1 by my probe (cut flag propagates into `truncated`).
- Truncation: HOLDS. Cap+1 byte read; a body cut at 4 MiB with the quote absent is
  TRUNCATED (S25), quote inside the read bytes is LOCATED (S26), url=- for
  TRUNCATED; an exactly-4 MiB body with EOF is not marked cut (`len(body) >
  MAX_BODY_BYTES`).
- Per-request --timeout budget: DOES NOT HOLD for dripping bodies — MEDIUM-1 below.
  The silent-stall path is bounded (2s budget aborted at 2.0s).
- Attempt counting: HOLDS. Per-request counting across hand-walked chains (S19
  redirect = attempts=2), requests already made before a refused hop are counted
  (S20 attempts=1), 3 transient attempts per URL per pass (S9; closed port = 9 =
  3 passes x 3), FatalFetch ends the URL after one chain, chain cap 5 counted
  exactly (probe: 5 hits).
- Exit contract: HOLDS. 0 when every row LOCATED, 1 otherwise, 2 on input errors
  with a REOPEN_ERROR line and no traceback (bad-input battery, bad UTF-8 registry,
  missing registry, unknown option); `ROW`/`REOPEN:` line formats and argument
  order verified; my probe got exit 0 and `REOPEN: 1/1 located` on an all-located
  registry.

## Findings

MEDIUM-1 (per-request --timeout budget not enforced for a dripping body).
`_read_body` calls `answer.read(want)` with want = 64 KiB. `http.client.HTTPResponse.read(amt)`
delegates to `io.BufferedReader.read(amt)`, which blocks until amt bytes or EOF, so
the inter-chunk deadline check never runs during a read, and the bounded socket
timeout (`_set_read_timeout`) never fires because every recv is satisfied by the
trickle. Evidence (offline, against the landed Fetcher): budget 2 s, server sends
Content-Length 65536 with 1 byte per 0.05 s — the fetch returned only at the
server's EOF, after 10.0 s (5x budget; a never-closing trickle holds a request for
an arbitrary attacker-chosen duration). End-to-end through main(): --timeout 1
against a 45 s drip row ran 135.1 s for 3 attempts (verdict UNREACHABLE
attempts=3, so counting and verdicts stay sound — this is a liveness failure, not
a false answer or a policy bypass; hence MEDIUM, not HIGH). The docstring and the
claim statement say "a body that stalls or drips cannot outlive it"; only the
stall case does. The counter's TIMEOUT leg uses a stall-then-silent fixture, which
exercises only the bounded path, which is why the leg passes while the drip path
is unguarded. Fix shape: read via `read(1)`/short reads or a non-greedy
`readinto` loop (or `answer.fp.read1`), or shrink the per-read ask and enforce the
deadline inside the read loop, so the check runs between recvs.

LOW-1 (userinfo URLs fail closed). The check layer handles userinfo hosts
correctly, but the fetch layer cannot connect to any userinfo-bearing URL at all:
stdlib does not strip userinfo from the netloc (Python 3.14.8,
`urlopen("http://x-user@127.0.0.1:9/x")` -> gaierror(-2) 'Name or service not
known'; same result through the landed Fetcher). A row whose source URL carries
`user@host` is answered UNREACHABLE after the full retry schedule (my probe: 18
attempts over 3 passes). Fail-closed, no SSRF consequence, no wrong verdict;
exposure in the registry is zero today (0 userinfo-bearing URLs in
corpus/SOURCES.md, including the new S694-S717 block).

LOW-2 (doc-text only). The docstring's pass-verdict sentence lists LOCATED >
CAPTION_ONLY > ABSENT > REFUSED > UNREACHABLE and predates the new verdicts;
VERDICT_RANK implements TRUNCATED at ABSENT's rank and MALFORMED lowest, and a row
mixing REFUSED and MALFORMED outcomes prints REFUSED while both verdict
definitions say "every URL". Deterministic and conservative; wording nit only.

## Residual risk and verification gaps

- DNS-rebind TOCTOU: `private_host` resolves at check time; the actual connect
  re-resolves independently, so short-TTL rebinding can pass the preflight. Check-
  time results are cached per host, which narrows but does not close the window.
  Outside the routed catalog; already recorded as the residual LOW class in the
  corpus hold-lift note.
- Refusal classes are exactly the catalog set (loopback, private, link-local,
  reserved, unspecified — verified on this interpreter, including IPv4-mapped IPv6
  forms, which are caught). Multicast (224.0.0.0/4) and CGNAT (100.64.0.0/10) are
  outside the set; not routed scope.
- Not probed: live IDNA homoglyph hosts (the check is resolution-based, so IDN
  forms are checked via whatever getaddrinfo returns, but no fixture was built);
  proxy environments; HTTP/2 or chunked-drip variants of MEDIUM-1 other than the
  Content-Length drip measured.
- This seat did not execute reports/round-63/accept-o.py or accept-c.py (receipt
  discipline) and did not run the tool on live URLs (hold).

## Disposition

MEDIUM-1 stands against the landed bytes: the closure catalog's per-request
--timeout budget item is not closed for the drip case the docstring itself names.
LOW-1 and LOW-2 are recorded for the next repair pass.
