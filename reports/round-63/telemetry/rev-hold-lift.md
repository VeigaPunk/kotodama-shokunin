# rev-hold-lift — residual review of the landed bytes of tools/reopen-row.py

Reviewed bytes (two revisions, both verified):
- First review: `git show main:tools/reopen-row.py` at dd81fd29, content sha256
  `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5` (= freeze
  receipt, = claimed build sha 0d965ccb), 1217 lines, mode 100755.
- Re-review after the MEDIUM-1 repair: 42a30dc9 (ancestor of main), blob
  2894d2e, content sha256
  `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0`,
  1222 lines, mode 100755; `git show main:tools/reopen-row.py` and the worktree
  both hash c0f10a84... today. The repair diff vs dd81fd29 is exactly one loop in
  `_read_body`: the greedy `answer.read(want)` becomes `read1(want)` (via a
  getattr fallback to `read`), 6 insertions, 1 deletion, nothing else touched.
- Baseline for the catalog: round-62 65b393e (plain `urllib.request.urlopen`
  auto-following redirects, silent `read(MAX_BODY_BYTES)` cap, bare per-open
  socket timeout).

Method: read-only review plus offline execution only — the built-in `--selftest`
and an independent probe harness served from 127.0.0.1 fixtures (scheme-relative
and userinfo Locations, infinite redirect loop, ftp Location, gzip-expansion
bomb, silent-stall body, dripping body). Probes ran against the commit bytes
extracted with `git show`, not the worktree. No live URL was fetched; the accept
counter was not executed by this seat. No tool installs or upgrades were
performed. Selftest on the patched bytes: 49 checks, 0 failures.

## Closure catalog status on the patched bytes

- Redirect-to-private SSRF incl. cross-authority hop rule: HOLDS. `_NoRedirect`
  stops library-level following; every hop is re-resolved by hand and compared by
  (lowercased hostname, effective port) from `parse_target`; a cross-authority
  hop must pass `private_host` even under `--allow-private`. Selftest S20: REFUSED
  attempts=1 with the hop target untouched (0 hits). Probes on the patched blob:
  scheme-relative `Location: //127.0.0.1:<other-port>/secret` REFUSED attempts=1
  with 0 hits on the target; `ftp://` Location is FatalFetch with no request; a
  5-hop loop ends after exactly 5 requests (UNREACHABLE, not retried because
  FatalFetch is not transient). Userinfo cannot smuggle a private host past the
  check: authority comparison uses `parts.hostname`, which strips userinfo
  (fetch-layer consequence under LOW-1).
- Malformed URLs: HOLDS. Bad port, unbalanced bracketed IPv6, empty host are
  answered `ROW <ID> MALFORMED attempts=0 url=-` (S21-S23), run exits 1 (not 2),
  no traceback, no request; REOPEN_ERROR + exit 2 stays reserved for
  invocation/registry input errors.
- Gzip: HOLDS. Content-Encoding gzip decompressed before matching (S24), 64 MiB
  expansion cap; a bomb whose quote lies past the cap is TRUNCATED attempts=1
  (probe on the patched blob).
- Truncation: HOLDS on read1 semantics. Cap+1 bytes accumulated; body cut at
  4 MiB with quote absent is TRUNCATED (S25), quote inside the read bytes is
  LOCATED (S26), url=- for TRUNCATED; exactly-4 MiB body with EOF is not marked
  cut (`len(body) > MAX_BODY_BYTES`); the gzip-bomb probe re-confirmed the cut
  path through read1 chunking.
- Per-request --timeout budget: HOLDS after the repair, for both failure shapes.
  Silent stall: budget 2 s aborted at 2.0 s. Drip (1 byte per 0.05 s,
  Content-Length 65536): TransientFetch at 2.0 s — before the repair the same
  probe returned only at the server's EOF after 10.0 s, and end-to-end
  `--timeout 1` against a 45 s drip row took 135.1 s for 3 attempts; on the
  patched blob the same row takes 3.2 s for 3 attempts (UNREACHABLE attempts=3).
  Mechanism: HTTPResponse.read1 performs at most one raw socket read, so the
  deadline check between chunks actually runs; the getattr fallback to read()
  is dead on the canonical runtime (urllib's response always exposes read1 —
  proven by the 2.0 s drip result, which only read1 can produce).
- Attempt counting: HOLDS. Per-request counting across hand-walked chains (S19
  redirect = attempts=2), requests already made before a refused hop counted
  (S20 attempts=1), 3 transient attempts per URL per pass (S9; closed port = 9 =
  3 passes x 3), FatalFetch ends the URL after one chain, chain cap counted
  exactly (probe: 5 hits).
- Exit contract: HOLDS. 0 when every row LOCATED, 1 otherwise, 2 on input errors
  with a REOPEN_ERROR line and no traceback; `ROW`/`REOPEN:` formats and argument
  order verified; probe got exit 0 and `REOPEN: 1/1 located` on an all-located
  registry.

## Findings

MEDIUM-1 (per-request --timeout budget not enforced for a dripping body) —
Resolved at 42a30dc9. Original evidence against dd81fd29: `answer.read(want)`
delegated to a greedy BufferedReader read that blocked until `want` bytes or EOF,
so the inter-chunk deadline check never ran during a read and the bounded socket
timeout never fired while a trickle satisfied every recv; budget 2 s vs drip
returned after 10.0 s, and the 45 s drip row ran 135.1 s end-to-end. The repair
replaces the read with read1 (one raw read per iteration), letting the deadline
check run between chunks; on the patched bytes the identical probes return at
2.0 s and 3.2 s respectively, with the stall path, truncation path, selftest
(49/49) and every other probe unchanged. The `read`-fallback branch introduced by
the getattr is dead on the canonical runtime and is not exercised by fixtures;
recorded as a gap, not a finding.

LOW-1 (userinfo URLs fail closed) — Remains. The check layer handles userinfo
hosts correctly, but the fetch layer cannot connect to any userinfo-bearing URL:
stdlib does not strip userinfo from the netloc (Python 3.14.8,
`urlopen("http://x-user@127.0.0.1:9/x")` -> gaierror(-2) 'Name or service not
known'; same through the landed Fetcher). Such a row answers UNREACHABLE after
the full retry schedule (probe: 18 attempts over 3 passes). Fail-closed, no SSRF
consequence, no wrong verdict; exposure in the registry is zero today (0
userinfo-bearing URLs in corpus/SOURCES.md, including the new S694-S717 block).

LOW-2 (doc-text only) — Remains. The docstring's pass-verdict sentence lists
LOCATED > CAPTION_ONLY > ABSENT > REFUSED > UNREACHABLE and predates the new
verdicts; VERDICT_RANK implements TRUNCATED at ABSENT's rank and MALFORMED
lowest, and a row mixing REFUSED and MALFORMED outcomes prints REFUSED while both
verdict definitions say "every URL". Deterministic and conservative; wording nit
only.

## Residual risk and verification gaps

- DNS-rebind TOCTOU: `private_host` resolves at check time; the actual connect
  re-resolves independently, so short-TTL rebinding can pass the preflight.
  Check-time results are cached per host, which narrows but does not close the
  window. Outside the routed catalog; already recorded as the residual LOW class
  in the corpus hold-lift note.
- Refusal classes are exactly the catalog set (loopback, private, link-local,
  reserved, unspecified — verified on this interpreter, including IPv4-mapped
  IPv6 forms, which are caught). Multicast (224.0.0.0/4) and CGNAT (100.64.0.0/10)
  are outside the set; not routed scope.
- Not probed: live IDNA homoglyph hosts (the check is resolution-based, so IDN
  forms are checked via whatever getaddrinfo returns, but no fixture was built);
  proxy environments; chunked-transfer drip variant of the timeout probe (the
  measured drip used Content-Length); the dead read()-fallback branch of the
  repair.
- This seat did not execute reports/round-63/accept-o.py or accept-c.py (receipt
  discipline) and did not run the tool on live URLs (hold). No HIGH or MEDIUM
  finding remains on the bytes at 42a30dc9; LOW-1 and LOW-2 stay recorded for the
  next repair pass.

VERDICT: NO-OPEN-HIGH-MED
