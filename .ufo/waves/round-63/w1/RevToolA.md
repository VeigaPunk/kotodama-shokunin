# RevToolA — independent SSRF review gate (claim O, round 63)

Seat: kotodama-r63-w1-RevToolA (leaf reviewer; read-only).
Date: 2026-10-23. Lane base/freeze: `65b393e`/`80d53ff` (held `tools/reopen-row.py` sha256 `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803`; identical at both revisions).

Artifact reviewed (final candidate repair): `/fast/scratch/hyaku/kotodama-r63/ExecRepairTool/reopen-row.py`, sha256 `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5` (1217 lines, mode 755, AST-compile clean, stable since 2026-10-23 16:01:44 -0300). Earlier intermediate states (byte-identical copy `21e2d767`; docstring-only; `c544973c`) were superseded; the delta from `c544973c` is confined to the `--selftest` tail (fixture-server extra headers, stall server, new offline cases) — every review anchor re-resolves to identical code in the final bytes: `parse_target` 375, `_NoRedirect` 415, `Fetcher.private_host` 452, `follow` 583, `run_pass` 648, `parse_args` 757. Method: static code review only — the held safety hold forbids running the tool; the frozen counter (accept-o.py) is the executable evidence, run by the executor seats. Resolver/parser semantics (IP literals, urlsplit, ipaddress predicates) were probed independently with Python 3 on this host.

## SSRF catalog

1. **Cross-host redirect to 127.0.0.1 / ::1 / RFC1918 / link-local / 0.0.0.0** — CLOSED. `_NoRedirect` (415-419) makes `HTTPRedirectHandler.redirect_request` return None, so the stdlib never auto-follows; a 3xx comes back as a `Response` carrying `Location` (`fetch`, 517-530). `follow` (583-614) resolves each target with `urljoin` and re-runs the refusal before requesting it. `Fetcher.private_host` (452-480) refuses loopback, private, link-local, reserved and unspecified addresses (and unresolvable hosts) from the resolved address set (any private answer ⇒ refused).
2. **Decimal / octal / hex / dotted-less IP literals** (`http://2130706433/`, `0x7f000001`, `017700000001`, `127.1`) — CLOSED. Refusal is resolution-based (`socket.getaddrinfo`, 463-468): probed on this host — `2130706433`, `0x7f000001`, `017700000001`, `127.1` all resolve to `127.0.0.1` ⇒ `is_loopback` ⇒ refused; `::ffff:127.0.0.1` ⇒ `is_loopback`/`is_private` both True ⇒ refused. Applies identically to listed URLs and redirect targets.
3. **Userinfo confusion** (`http://127.0.0.1@public.example/`) — CLOSED. `parse_target` (375-397) uses `parts.hostname`, which is the host after `@` (probed: `hostname == 'public.example'`); the peer the client connects to is that hostname, not the userinfo. A userinfo literal pointing at a private host is still refused because `hostname` is then the private literal.
4. **Scheme-relative Locations** (`Location: //127.0.0.1/x`) — CLOSED. `follow` resolves via `urllib.parse.urljoin(current, location.strip())` (599) and then applies the authority comparison plus refusal, so `//private/...` is caught.
5. **https→http downgrade exposing the same path to a private listener** — CLOSED. Authority equality includes the effective port (605, 602): a scheme change that also changes the port is a cross-authority hop and must pass `private_host` even under `--allow-private`; a same-authority hop is only permitted under `--allow-private` (610).
6. **DNS-rebind limitation** — OPEN, residual, LOW. The policy is IP-based: the refusal resolves at check time and caches per host (`_resolved`, 460-468); the actual connect (urllib/http.client) re-resolves at connect time, and the cache never refreshes. A host that resolves public at check time but private at connect time (attacker-controlled DNS) could be fetched. This is inherent to an IP-based policy and matches the claim's honest limitation; not a HIGH/MEDIUM open finding.
7. **Redirect loops and hop caps** — CLOSED. `follow` bounds each chain at `MAX_REQUESTS_PER_CHAIN = 5` requests, each counted as an attempt (591-592, 613-614); a loop terminates deterministically (e.g. two-host bounce = 5 requests, then `FatalFetch`), and a refused hop ends the URL for the pass.
8. **--allow-private semantics** — CLOSED. Same-authority hops are allowed under `--allow-private` and still re-checked without it (610); cross-authority hops are always re-checked against `private_host` (605-609), exactly the required semantics.

## Related claim-O closures (same artifact, informational)

- Malformed registry URLs (`port 99999`, unbalanced bracketed IPv6, empty host, non-http(s) scheme, out-of-range port) → `parse_target` raises `BadUrl` (386-396); `run_pass` marks the URL MALFORMED without a request (662-667) ⇒ `ROW <ID> MALFORMED attempts=0 url=-`, no traceback, exit 1.
- gzip `Content-Encoding` decoded before matching (`gunzip`, 400-409; called at 509-511); corrupt gzip ⇒ `FatalFetch` (no traceback).
- Truncation: body read capped at `MAX_BODY_BYTES+1` with chunking (`_read_body`, 541-560); verdict TRUNCATED when the quote is absent from the read bytes, LOCATED/CAPTION_ONLY when inside (690-710).
- `--timeout SECONDS` (default 30, number > 0, NaN/±inf rejected, 814-819) is a per-request wall budget: `fetch` computes a monotonic deadline and shapes both the opener timeout and the body-read socket timeout by the remaining budget (495-560); expiry is `TransientFetch` and retries per the schedule (process_row unchanged).
- Redirect-hop counting: each chain request increments the per-URL counter; refused/fatal/transient paths all surface `counter[0]` as attempts (676-689).

## Residual risk and verification gaps

- Probed, not executed: literal-form resolution (glibc `getaddrinfo`), `urlsplit` error/edge behavior, `ipaddress` predicate outcomes (e.g. `::ffff:127.0.0.1` ⇒ loopback+private). These are environment-dependent to a degree; the counter fixtures do not cover every literal form, so the live host's behavior is the verified surface.
- Informational observations (not HIGH/MEDIUM): CGNAT `100.64.0.0/10` and multicast `224/4` are not caught by the checked predicates (probed: `is_private/is_reserved` both False for `100.64.0.1`); connecting to them does not reach a private service in this deployment. `_set_read_timeout` reaches into private stdlib attributes (`fp.raw._sock`) under try/except — brittle across Python versions, functional risk only. Over-refusal risk for Unicode/IDNA hostnames that make `getaddrinfo` raise (refused, safe direction).
- The landed lane copy is still the held version (`21e2d767`); this review applies to the final candidate artifact at the sha above. RevHoldLift must re-run this gate on the landed bytes.
- Executable behavior (attempts, verdicts, exit codes, wall-time bounds) is exercised by the frozen counter; I did not run the tool.

Findings by severity: no HIGH, no MEDIUM open. Residual LOW: DNS-rebind TOCTOU (item 6) — honest, IP-based policy limitation.

VERDICT: NO-OPEN-HIGH-MED
