# CtlOShortCircuit — claim O short-circuit controls (round 63, wave 1)

seat: kotodama-r63-w1-CtlOShortCircuit (mutation-tester, leaf; no delegation, no background jobs)
date: 2026-10-23
frozen counter run: `reports/round-63/accept-o.py` sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` (byte-identical to the freeze record at 80d53ff; my probe copy has the same sha — the counter was never edited)
measured revision for every receipt: `80d53ffde7788299b69dbb0bd0436b2b7ddddb95`
sandbox: `/fast/scratch/hyaku/kotodama-r63/CtlOShortCircuit/` (clone at the freeze, probe root, pristine root, out/ = calibration iteration, out2/ = scored runs)
lane writes: none (only this report); lane tool/counter hashes were only read, and they moved during the wave — see “Lane observation” below.
installs: none.

## What was tested

Five short-circuit cheats, one switch each, toggled by `PROBE_CHEAT` (environment inherited by the counter's copied tool):

| switch | cheat under test |
|---|---|
| `trunc` | print TRUNCATED for any 2xx body whose `Content-Length` exceeds 4 MiB, without reading the body (the quote may be inside) |
| `malformed` | print MALFORMED only when the authority's port is non-numeric (99999, unbalanced IPv6, empty host not detected) |
| `redirect` | the inverse re-validation rule: follow cross-authority redirects under `--allow-private`, answer REFUSED on a redirect without it |
| `gzip` | decompress `Content-Encoding: gzip` only when the compressed body is under 1 MiB |
| `timeout` | apply `--timeout` only to the first fetch attempt of a URL |

Probe tool: `probe/tools/reopen-row.py` sha256 `b7020d3a0b1364eaf34b3bf9ea88402ae4bca95789e4b441fe03b77657bd2baf`, a copy of the freeze tool (`21e2d767…`) with: a non-following redirect handler, per-hop authority re-validation, malformed-URL detection, `Content-Encoding: gzip` handling, a 4 MiB+1 overrun read with TRUNCATED, a per-request wall budget and the `--timeout SECONDS` flag. Each cheat is a labelled branch at the point the honest path would do the work (`grep -n 'cheat(' probe/tools/reopen-row.py` → lines 367, 450, 462, 472, 494). The honest path (`PROBE_CHEAT=none`) is the positive control: it must pass all 15 legs, or the fixture is wrong.

Fixture disclosure (important): the REVIEW leg reads `.ufo/waves/round-63/w1/RevTool{A,B,C}.md` and `reports/round-63/telemetry/rev-hold-lift.md` under `--root`. To stop a fixture-level REVIEW failure from masking tool legs I placed PROBE FIXTURE STUBS carrying `VERDICT: NO-OPEN-HIGH-MED` in the *probe and pristine roots only* (never in the lane). REVIEW therefore PASSes in every run below and carries **no** evidence about the real review gate; it is identical across cases and decides none of them. With the stubs removed, REVIEW FAILs in all seven runs and changes no other leg.

## Baseline (pristine bytes at the freeze, unrepaired tool 21e2d767)

Command: `cd /fast/scratch/hyaku/kotodama-r63/CtlOShortCircuit/pristine && python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=44 ["REDIRECT_LOOP:S2788:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "MALFORMED_PORT:S2768:want=MALFORMED/0:got=[('UNREACHABLE', 9)]", "REDIRECT_MULTI:S2772:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2772:url_want=http://127.0.0.1:33349/pkra/zczfqmto/sxuthmccp:got=['http://127.0.0.1:33349/qfivyo']", "GZIP_BODY:S2879:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2879:url_want=http://127.0.0.1:33349/pzmcjvl/cbcxxe:got=['-']"] summary_ok=False exit=1
ORDER FAIL printed=42 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=5', 'REDIRECT_LOOP:l2:want=2:hits=4', 'CAP_ATTR:live:want=1:hits=0', 'CAP_CLASS_GALLERY:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'TRANSIENT2:live:want=3:hits=0', 'GONE:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2496', 'REFUSED', 0), ('S2626', 'REFUSED', 0), ('S2899', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2462', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2596', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2596', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2373', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2511', 'ABSENT', 1), ('S2952', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2407', 'ABSENT', 1), ('S2101', 'LOCATED', 1)] want=[('S2407', 'TRUNCATED', 1), ('S2101', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
exit=1
```

Baseline verdict: FAIL, exactly the declared pre-repair state (claims.json: both predicates FAIL at base 65b393e; this run is at 80d53ff whose tool blob is unchanged, 21e2d767). It confirms the counter is not trivially passing; a baseline failure is inconclusive for any single mutant, so every cheat below is scored against the honest positive, not against this baseline.

## Honest positive control (probe tool, all cheats off)

Command: `cd /fast/scratch/hyaku/kotodama-r63/CtlOShortCircuit/probe && PROBE_CHEAT=none python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2876', 'REFUSED', 0), ('S2948', 'REFUSED', 0), ('S2385', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2414', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2870', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2870', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2367', 'MALFORMED', 0), ('S2062', 'MALFORMED', 0), ('S2865', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2329', 'LOCATED', 1), ('S2101', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2315', 'TRUNCATED', 1), ('S2409', 'LOCATED', 1)] want=[('S2315', 'TRUNCATED', 1), ('S2409', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2014', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```

## Cheat 1 — TRUNC without reading the body

Command: `cd probe && PROBE_CHEAT=trunc python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=2 ["TRUNC_NEAR:S2126:want=LOCATED/1:got=[('TRUNCATED', 1)]", "TRUNC_NEAR:S2126:url_want=http://127.0.0.1:45867/ypbdfipdy:got=['-']"] summary_ok=False exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2064', 'REFUSED', 0), ('S2928', 'REFUSED', 0), ('S2975', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2176', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2897', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2897', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2840', 'MALFORMED', 0), ('S2731', 'MALFORMED', 0), ('S2711', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2876', 'LOCATED', 1), ('S2332', 'CAPTION_ONLY', 1)]
TRUNC FAIL exit=1 rows=[('S2626', 'TRUNCATED', 1), ('S2670', 'TRUNCATED', 1)] want=[('S2626', 'TRUNCATED', 1), ('S2670', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2965', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
exit=1
```

RECEIPT CtlOShortCircuit/trunc-cheat counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,TRUNC

Verdict: **NONE-MET**. GEN catches it in the TRUNC_NEAR fixture (quote inside a body that overruns the cap: cheat prints TRUNCATED, expected LOCATED/1 and the live URL); the dedicated TRUNC leg catches the same row again. Smallest counter change that would be needed to keep this catch: none — the existing GEN/TRUNC fixtures already encode “quote inside the read bytes stays LOCATED”.

## Cheat 2 — MALFORMED only for a non-numeric port

Command: `cd probe && PROBE_CHEAT=malformed python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=63 ["MALFORMED_PORT:S2583:want=MALFORMED/0:got=[('UNREACHABLE', 9)]", 'MALFORMED_IPV6:S2471:want=MALFORMED/0:got=[]', 'MALFORMED_IPV6:S2471:url_want=-:got=None', 'SHORT:S2717:want=NO_QUOTE/0:got=[]', 'SHORT:S2717:url_want=-:got=None', 'GONE:S2779:want=UNREACHABLE/1:got=[]'] summary_ok=False exit=1
ORDER FAIL printed=30 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['GONE:live:want=1:hits=0', 'CAP_ID:live:want=1:hits=0', 'BODY:live:want=1:hits=0', 'CAP_ID:live:want=1:hits=0', 'CAP_ATTR_ARIA:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'REDIRECT_OK:live:want=1:hits=0', 'REDIRECT_OK:rtarget:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2453', 'REFUSED', 0), ('S2046', 'REFUSED', 0), ('S2000', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2049', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2329', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2329', 'REFUSED', 0)] exits=1,1
MALFORMED FAIL exit=1 rows=[('S2818', 'UNREACHABLE', 9)] traceback=True
GZIP PASS exit=1 rows=[('S2548', 'LOCATED', 1), ('S2800', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2227', 'TRUNCATED', 1), ('S2996', 'LOCATED', 1)] want=[('S2227', 'TRUNCATED', 1), ('S2996', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2279', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
exit=1
```

RECEIPT CtlOShortCircuit/malformed-cheat counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,MALFORMED

Verdict: **NONE-MET**. GEN catches it twice: MALFORMED_PORT (port 99999 is numeric, so the cheat requests it and reports UNREACHABLE/9 instead of MALFORMED/0) and MALFORMED_IPV6, where the undetected malformed URL raises inside the request path and aborts the GEN run after 30 rows (that abort is what also fails ORDER and BOUND; 23 rows were printed in the earlier iteration, 30 here, both short of 61). The MALFORMED leg catches it directly with a traceback on the stream. Note the catch is partly a crash, not a clean MALFORMED answer: a run that dies mid-registry is still a FAIL, so the leg holds.

## Cheat 3 — inverse redirect rule

Command: `cd probe && PROBE_CHEAT=redirect python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2822', 'REFUSED', 0), ('S2316', 'REFUSED', 0), ('S2351', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2920', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2004', 'LOCATED', 2)] hits_src=1 hits_target=1 no_flag=[('S2004', 'REFUSED', 0)] exits=0,1
MALFORMED PASS exit=1 rows=[('S2606', 'MALFORMED', 0), ('S2516', 'MALFORMED', 0), ('S2708', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2581', 'LOCATED', 1), ('S2646', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2160', 'TRUNCATED', 1), ('S2873', 'LOCATED', 1)] want=[('S2160', 'TRUNCATED', 1), ('S2873', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2682', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
exit=1
```

RECEIPT CtlOShortCircuit/redirect-cheat counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=REDIRECT

Verdict: **NONE-MET**, but GEN does **not** catch it (GEN PASS, 61 rows correct): every GEN redirect class (REDIRECT_OK, REDIRECT_MULTI, REDIRECT_LOOP) hops inside one loopback authority, so the inverse rule is indistinguishable there. The dedicated REDIRECT leg is the only catcher: under `--allow-private` the cheat follows the 302 to the other loopback port (`LOCATED attempts=2`, target hits=1, exit 0), where the rule requires `REFUSED attempts=1` and 0 target hits; without the flag both behave alike (`REFUSED attempts=0`). Smallest counter change that would move this catch into GEN: add a `REDIRECT_CROSS` class whose Location is a second `Fixture`'s port, expected `("REFUSED", 1, {"live": 1, "x": 0})` with the target server's hits asserted 0.

## Cheat 4 — gzip only under 1 MiB

Command: `cd probe && PROBE_CHEAT=gzip python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2464', 'REFUSED', 0), ('S2347', 'REFUSED', 0), ('S2424', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2856', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2436', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2436', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2410', 'MALFORMED', 0), ('S2012', 'MALFORMED', 0), ('S2203', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2623', 'LOCATED', 1), ('S2309', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2843', 'TRUNCATED', 1), ('S2674', 'LOCATED', 1)] want=[('S2843', 'TRUNCATED', 1), ('S2674', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2008', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```

RECEIPT CtlOShortCircuit/gzip-cheat counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none

Verdict: **CONTROL-MET**. The fixture that met it: the whole 15-leg frozen counter, with every gzip body in the counter under 1 MiB — GEN's GZIP_BODY (small body, quote in body) and both GZIP-leg rows (small body / small figcaption). The cheat decompresses those and reports LOCATED and CAPTION_ONLY exactly as expected, so it skips the claimed work (decompress every gzip response) and still gets `ACCEPT-O-63: PASS`, exit 0. GEN does not catch it; the GZIP leg does not either. Smallest counter change that would stop it: one new class, `"GZIP_BIG": ("LOCATED", 1, {"live": 1})`, with a `build()` branch that gzips a body padded past 1 MiB (e.g. the existing 4 MiB pad) with the quote inside; the cheat leaves it compressed, matches nothing, and reports ABSENT (or TRUNCATED if the pad overruns the cap — either way not LOCATED), failing GEN and a matching GZIP-leg row.

## Cheat 5 — timeout only on the first attempt

Command: `cd probe && PROBE_CHEAT=timeout python3 -B reports/round-63/accept-o.py; echo exit=$?`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2645', 'REFUSED', 0), ('S2605', 'REFUSED', 0), ('S2228', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2338', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2255', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2255', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2853', 'MALFORMED', 0), ('S2128', 'MALFORMED', 0), ('S2154', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2476', 'LOCATED', 1), ('S2504', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2276', 'TRUNCATED', 1), ('S2525', 'LOCATED', 1)] want=[('S2276', 'TRUNCATED', 1), ('S2525', 'LOCATED', 1)]
TIMEOUT FAIL exit=None rows=[] wall=120.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
exit=1
```

RECEIPT CtlOShortCircuit/timeout-cheat counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=TIMEOUT

Verdict: **NONE-MET**. GEN does not catch it (no stall class in GEN; 61 rows correct). The TIMEOUT leg catches it: attempt 1 expires at 4 s, attempts 2 and 3 run with no deadline and the counter's own `run_tool(timeout=120)` kills the process group, so `stc=None`, `wall=120.1s`, rows empty, exit 1 — the leg requires exit 1, `UNREACHABLE attempts=3` and wall < 45 s. The honest run does the same leg in 12.1 s. Note the catch is a harness kill at 120 s, not a verdict: any future relaxation of the counter's 120 s runner budget would let this cheat through, so a `STALL` class inside GEN (same fixture, expected UNREACHABLE/3) would be the smallest hardening.

## Receipt summary

| case | frozen | exit | stopped-by | GEN catches? |
|---|---|---|---|---|
| baseline (pristine 21e2d767) | FAIL | 1 | GEN, ORDER, BOUND, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT | n/a (pre-repair) |
| honest probe (all cheats off) | PASS | 0 | none | positive control |
| trunc-cheat | FAIL | 1 | GEN, TRUNC | **yes** (TRUNC_NEAR) |
| malformed-cheat | FAIL | 1 | GEN, ORDER, BOUND, MALFORMED | **yes** (MALFORMED_PORT; MALFORMED_IPV6 aborts the run) |
| redirect-cheat | FAIL | 1 | REDIRECT | **no** (all GEN hops same-authority) |
| gzip-cheat | PASS | 0 | none | **no** — CONTROL-MET |
| timeout-cheat | FAIL | 1 | TIMEOUT | **no** (harness kill at 120 s) |

## Restoration and byte evidence

- Lane tree was never written by this seat. `tools/reopen-row.py` and `reports/round-63/accept-o.py` in `/home/vgpnk/Projects/shokunin/kotodama-shokunin` were only read.
- Frozen bytes: clone at 80d53ff, `tools/reopen-row.py` = `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803`; `reports/round-63/accept-o.py` = `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` (matches the freeze record; `git -C clone status --porcelain` empty).
- Mutant: `probe/tools/reopen-row.py` = `b7020d3a0b1364eaf34b3bf9ea88402ae4bca95789e4b441fe03b77657bd2baf` (one file in a labelled probe copy; `PROBE_CHEAT` selects the cheat at runtime).
- Restored: `restored/reopen-row.py` = `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803`; `cmp -s` against the clone bytes → identical (RESTORED-IDENTICAL). The first calibration iteration used probe revision 0 (sha `68bc8c47…`, wrong `url=` on redirect chains); its full stdout is kept at `/fast/scratch/hyaku/kotodama-r63/CtlOShortCircuit/out/` and is superseded by `out2/` — it is disclosed, not silently dropped.
- Calibration lesson (already learned in the first iteration): a probe that reports the listed URL instead of the final redirect hop fails GEN even with every verdict and attempts count correct (`REDIRECT_OK … url_want=<target>:got=<live>`), so GEN also enforces the reported final URL, not just verdicts.

## Lane observation (not a finding of this seat)

The lane working tree moved while these runs executed: `tools/reopen-row.py` went `21e2d767…` (at the freeze) → `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5`, and `reports/round-63/accept-o.py` went `a751efec…` (freeze) → `46317e55e90443438b72fc6df4539a77bbeab3794b58c3211d15e20ad08538fd` → `7dc784ed83763747a822e3b5597449f41464347687e0e0ad2d45ecf0d2c76af1`, between 15:52 and 16:12 local. All receipts here are against the frozen counter sha `a751efec…` from the clone at 80d53ff, per the control-receipt rule; the L1 should confirm which counter sha the final O receipt names, since `claims.json` allows a counter revision only before the first run on the claimed object.

## What this means for claim O

- Four of the five short-circuit cheats are killed, three of them by the dedicated leg plus GEN and one (redirect) only by its dedicated leg.
- The gzip size threshold survives the frozen counter end to end (`frozen=PASS`): the counter cannot distinguish “decompress all gzip responses” from “decompress small ones”. This is a coverage finding against the frozen fixture, not permission to change the contract; the one-line fix is a large gzip fixture in GEN + GZIP.
- Two catches lean on incidental mechanics rather than a verdict: the malformed cheat fails partly by crashing the GEN run, and the timeout cheat fails because the counter's 120 s runner kill fires — both are real FAILs today, but they are thinner than the TRUNC and REDIRECT catches, which assert a verdict and a hit count against the tool's own output.
