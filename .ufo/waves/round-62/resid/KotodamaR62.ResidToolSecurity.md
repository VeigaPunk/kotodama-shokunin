VERDICT KotodamaR62.ResidToolSecurity: MIXED

Security & robustness review of tools/reopen-row.py @ a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 (lane
/home/vgpnk/Projects/shokunin/kotodama-shokunin). Read-only seat: no lane writes; all probes ran under
/fast/scratch/hyaku/kotodama-r62/resid/KotodamaR62.ResidToolSecurity/ (fixture HTTP server on dual-stack
port 39171; registry fixtures in scratch). No tooling installs performed (channel records: none).

================================================================================
FINDINGS (severity-ranked)
================================================================================

[1] HIGH — Redirect chain bypasses the private-host refusal entirely, with or without --allow-private
    Files: tools/reopen-row.py lines 339-401 (Fetcher.refused/fetch), 447 (run_pass), 370-387 (urlopen).
    Mechanism: refusal is evaluated exactly once on the row's initial URL, before urlopen(). urllib's
    default HTTPRedirectHandler then follows up to 10 redirects with no re-check of the target host or
    scheme. A public URL that 302s to 127.0.0.1 / ::1 / RFC1918 space is fetched regardless of policy.

    Repro (local fixture; public hop = host's own global IPv6 address, redirect targets private):
      # fixture_server.py routes:
      #   /redir127 -> 302 Location: http://127.0.0.1:39171/secret
      #   /redir6   -> 302 Location: http://[::1]:39171/secret
      #   /redir10  -> 302 Location: http://10.255.255.2/
      #   /secret    -> 200 HTML containing the row quote
      $ timeout 240 python3 -B .../tools/reopen-row.py --registry <scratch>/reg.md \
          --passes 3 --gap 0 SR_redir127 SR_redir6 SR_redir10 ...   # NO --allow-private
      ROW SR_redir127 LOCATED attempts=1 url=http://[2804:14d:5c56:36ef:fe9d:5ff:fe5e:5dbe]:39171/redir127
      ROW SR_redir6 LOCATED attempts=1 url=http://[2804:14d:5c56:36ef:fe9d:5ff:fe5e:5dbe]:39171/redir6
      ROW SR_redir10 UNREACHABLE attempts=3 url=-     (redirect followed into 10.255.255.2; 3x30s timeouts)
      Fixture hit log confirms the private endpoints were contacted:
        /secret ::ffff:127.0.0.1      (redirect target reached over IPv4 loopback)
        /secret ::1                   (redirect target reached over IPv6 loopback)
      Direct probe using the tool's own Fetcher.fetch (allow_private=False):
        public->127.0.0.1 redirect: refused(initial)=False, status=200 len(body)=147 ctype='text/html; charset=utf-8'
      Same redirect following observed when re-run WITH --allow-private (identical first two rows), i.e.
      the flag has no effect on redirect hops.

    Smallest fix: install a custom opener whose HTTPRedirectHandler re-runs `refused()` on every Location
    target (and rejects non-http(s) schemes) before following; on refusal raise/reclassify as FatalFetch
    ("redirect refused") so the row ends REFUSED/UNREACHABLE without a request.

[2] MEDIUM — Malformed URL inputs produce raw Python tracebacks (documented contract violated)
    Docstring (lines 73-75): input errors print REOPEN_ERROR, exit 2, "no traceback is shown".
    main() guards only parse_args/load_registry; the per-row loop (process_row -> run_pass ->
    fetcher.refused) is unguarded. Observed:
      $ timeout 60 python3 -B .../tools/reopen-row.py --registry <scratch>/reg.md --passes 3 --gap 0 SR_badport
      ...
      ValueError: Port out of range 0-65535          # http://example.com:99999/x
      EXIT=1
      $ timeout 60 python3 -B .../tools/reopen-row.py --registry <scratch>/reg.md --passes 3 --gap 0 SR_badipv6
      ...
      ValueError: Invalid IPv6 URL                   # http://[::1/secret
      EXIT=1
    Smallest fix: wrap the ID loop of main() in try/except Exception; print "REOPEN_ERROR: <exc>" to
    stderr and return 2 (mirroring existing InputError handling).

[3] LOW — Private-address classification gap: CGNAT 100.64.0.0/10 and 6to4 relay 192.88.99.0/24 are allowed
    refused() refuses loopback/private/link-local/reserved/unspecified via ipaddress. ipaddress does not
    classify RFC 6598 (100.64.0.0/10) or RFC 3068 (192.88.99.0/24) as private/reserved:
      $ python3 -c "import ipaddress; print(ipaddress.ip_address('100.64.0.1').is_private, ipaddress.ip_address('192.88.99.1').is_private)"
      False False
    Tool therefore attempted connections: SR_cgnat (http://100.64.0.1:39171/secret) -> UNREACHABLE
    attempts=3 (wall ~90 s), i.e. NOT refused. Smallest fix: add explicit networks (or after existing
    checks `if not ip.is_global: return True`).

[4] LOW — Silent 4 MiB response truncation yields wrong verdicts
    fetch() calls response.read(MAX_BODY_BYTES) (4 MiB) with no Content-Length check and no truncation
    signal. Fixture /big streams 6 MiB HTML whose quote sits beyond the cap; tool reported:
      ROW SR_big ABSENT attempts=1 url=-     (quote present but unread)
    No warning is emitted. Smallest fix: when Content-Length exists and exceeds the cap, reject or mark
    the fetch (read a bounded amount, then treat as ABSENT-with-truncation or fatal for that URL).

[5] LOW — Compressed responses are silently misparsed (false negatives)
    No Accept-Encoding is requested and Content-Encoding is never decoded. Fixture /gzip serves the quote
    page gzip-encoded (Content-Encoding: gzip); tool reported:
      ROW SR_gzip ABSENT attempts=1 url=-
    Smallest fix: send Accept-Encoding: identity, or decode gzip/deflate when the header is present.

[6] LOW — No aggregate wall-clock budget; a single dead URL can stall a row for minutes
    Timeout is per-socket (30 s). SR_slow (connection accepted, response after 45 s): UNREACHABLE
    attempts=9 in 270.4 s (3 passes x 3 attempts x 30 s + zero gaps). Bounded, but serial; worst-case
    per-row scales with URL count. Smallest fix: add an overall per-row/per-pass deadline (e.g. cap total
    seconds) and document it.

================================================================================
POSITIVE CONTROLS (verified, hold at this revision)
================================================================================
- Direct URLs refused WITHOUT a request (attempts=0), no --allow-private: 127.0.0.1, localhost (DNS
  name resolving to loopback), [::1], [::ffff:127.0.0.1] (IPv4-mapped IPv6), 0.0.0.0, 2130706433
  (decimal), 017700000001 (octal), 0x7f000001 (hex), 192.168.0.253 (RFC1918), 10.0.0.1, 169.254.1.1
  (link-local), and http://evil@127.0.0.1:39171/secret (userinfo). The DNS-resolution-based check covers
  obfuscated numeric forms correctly for initial URLs.
- Response reads are memory-bounded (4 MiB cap); per-socket timeouts exist; no shell/subprocess usage
  anywhere (no argument injection vector); parse_args is manual but safe; output uses %-formatting only.

================================================================================
RESIDUAL RISK / VERIFICATION GAPS
================================================================================
- DNS-rebinding TOCTOU: refused() resolves and caches addresses, then urlopen() resolves again when
  connecting; an attacker flipping DNS between the two checks could reach a private IP even without
  redirects. Not exercised here (would need a controllable split-horizon DNS).
- HTTP->HTTPS redirects are expected to be followed (both http(s); TLS verified with the default
  context); not explicitly probed.
- Redirects to file:// / data: / ftp:// were NOT followed empirically (both tool run and direct
  Fetcher.fetch raised FatalFetch HTTP 302, i.e. urllib aborted at the scheme change), so local-file
  disclosure via redirect was not observed; a scheme allowlist in the redirect handler is still
  recommended as defense-in-depth (default opener includes FileHandler/FTPHandler/DataHandler).
- The offline counter reports/round-62/accept-o.py was not run (repeat-only seat; security scope). Its
  fixtures run under --allow-private and are unaffected by the findings above.

Smallest fixes per finding are attached inline; the first two are the ones that change observable
security posture. No tooling installs were made during this review.
