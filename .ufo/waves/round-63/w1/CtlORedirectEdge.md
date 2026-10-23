# CtlORedirectEdge — round-63 claim O (operability) control receipt

seat: `CtlORedirectEdge` (control seat, leaf)
lane repo: /home/vgpnk/Projects/shokunin/kotodama-shokunin
freeze revision under test: `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` (round base `65b393ef3a4d82bd693cc21b7f96a1231417d522`)
date: 2026-10-23 (UTC); scratch tree: /fast/scratch/hyaku/kotodama-r63/CtlORedirectEdge/
axis: operability (claim O, `reports/round-63/accept-o.py`)

## 0. What this seat did, and what it did not

Scope: the **redirect edges** of the claim-O repair, measured against the
**frozen** counter, offline only (every endpoint a `127.0.0.1` server started by
my own harness). No live URL was fetched, no `tools/reopen-row.py` in the lane
was executed, nothing in the lane repo was written except this report.

All work happened in a sandbox clone made with
`git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin clone && git -C clone checkout -q 80d53ffde7788299b69dbb0bd0436b2b7ddddb95`
under `/fast/scratch/hyaku/kotodama-r63/CtlORedirectEdge/`. No `git`/`jj` write
command was run in the lane repo or the fleet repo.

**Tooling: no installs.** No pacman transaction, no `uv tool install`, no
binary download, no npm/pip install. Everything used is the stock `python3`
(3.14) already present. Nothing was downgraded and no host service was
restarted.

The **counter was never edited**: every run below used the frozen bytes from
the clone (`sha256 a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`). The lane's live counter has since been revised by
other seats (`sha256 ff4091c4510ab60987989067d43fb26cda7345dd12280e05cfd4af8755e33c9d`); I ran that one once as well, and label it as such.

## 1. The honest attempt (the reference "good" tool)

The lane has no repaired `tools/reopen-row.py` at the freeze, so I built one
**in scratch only** (`scratch/honest/tools/reopen-row.py`, produced by
`scratch/patch_honest.py`, a 30-patch script that asserts every replacement
applies exactly once). It implements the claim-O statement literally:

1. redirects are followed by hand (urllib's auto-follow is disabled with a
   `_NoRedirect` handler), each hop re-validated before it is requested;
2. authority = (lowercased host, effective port), userinfo ignored; a hop to a
   different authority is refused **even under `--allow-private`**; without
   `--allow-private` the target must also pass the private-host refusal;
3. a malformed **listed** URL → `ROW <ID> MALFORMED attempts=0 url=-`, exit 1,
   no traceback;
4. `Content-Encoding: gzip` is decompressed before matching;
5. a body that reaches the 4 MiB cap without EOF is `TRUNCATED` when the quote
   is absent from the bytes read, `LOCATED` when it is inside;
6. `--timeout SECONDS` (default 30, number > 0) is a per-request **wall** budget
   over connect + headers + body (a deadline is recomputed per read chunk);
7. at most 5 requests per chain; a redirect received on the 5th response ends
   the URL for the pass as a fatal result; the **final** URL of the chain is the
   one reported.

## 2. Receipts

Counter for receipts A–L: the **frozen** counter from the clone at
`80d53ffde7788299b69dbb0bd0436b2b7ddddb95`, `sha256 a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`. Each run is
`python3 -B reports/round-63/accept-o.py --root <scratch root>` with the tool
under test copied to `<root>/tools/reopen-row.py`.

The REVIEW leg reads four artifacts that live in the lane
(`.ufo/waves/round-63/w1/RevTool{A,B,C}.md`, `reports/round-63/telemetry/rev-hold-lift.md`).
At measurement time `rev-hold-lift.md` did not exist in the lane, so for
receipts A–L I symlinked the lane's real `RevToolA/B/C.md` and supplied a
**scratch stub** carrying only the mandated token at
`<root>/reports/round-63/telemetry/rev-hold-lift.md`. The stub records no
review finding; it exists so that the tool legs, not a missing artifact,
decide the receipt. Receipt M repeats the honest tool against the live lane
artifacts and the live revised counter, where the REVIEW leg fails only for
the missing `rev-hold-lift.md`.

```
RECEIPT CtlORedirectEdge/A-baseline-round62-tool counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN ORDER BOUND REDIRECT MALFORMED GZIP TRUNC TIMEOUT REVIEW
RECEIPT CtlORedirectEdge/B-honest-repair counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/C-M1-scheme-relative-unvalidated counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/D-M2-userinfo-netloc-authority counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/E-M3-https-unvalidated counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/F-M4-malformed-target-unguarded counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/G-M5-relative-no-slash-against-root counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/H-M6-308-not-a-redirect counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/I-M7-fifth-response-always-fatal counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/J-M8-chain-bound-six counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN BOUND
RECEIPT CtlORedirectEdge/K-M9-malformed-target-crash counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/L-M10-userinfo-target-unvalidated counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=
RECEIPT CtlORedirectEdge/M-honest-tool-live-counter-live-artifacts counter-sha256=ff4091c4510ab60987989067d43fb26cda7345dd12280e05cfd4af8755e33c9d rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=REVIEW

Interpretation of the mutant receipts: a receipt whose `frozen=PASS` was
produced by a tool that **skips one piece of the claimed redirect work** is
the control signal — the frozen counter did not notice.

### Receipt A — full stdout (baseline: round-62 tool at the freeze)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=76 ["TRUNC_FAR:S2921:want=TRUNCATED/1:got=[('ABSENT', 1)]", "REDIRECT_LOOP:S2304:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "REDIRECT_OK:S2349:want=LOCATED/2:got=[('LOCATED', 1)]", "REDIRECT_OK:S2349:url_want=http://127.0.0.1:41227/hqschrpnc/gkuoft:got=['http://127.0.0.1:41227/hqadvkaob']", 'MALFORMED_IPV6:S2745:want=MALFORMED/0:got=[]', 'MALFORMED_IPV6:S2745:url_want=-:got=None'] summary_ok=False exit=1
ORDER FAIL printed=25 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=5', 'REDIRECT_LOOP:l2:want=2:hits=4', 'CAP_CLASS_THUMB:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'GZIP_BODY:live:want=1:hits=0', 'REDIRECT_MULTI:c1:want=1:hits=0', 'REDIRECT_MULTI:c2:want=1:hits=0', 'REDIRECT_MULTI:c3:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2464', 'REFUSED', 0), ('S2997', 'REFUSED', 0), ('S2085', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2258', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2550', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2550', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2855', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2421', 'ABSENT', 1), ('S2942', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2919', 'ABSENT', 1), ('S2396', 'LOCATED', 1)] want=[('S2919', 'TRUNCATED', 1), ('S2396', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

### Receipt B — full stdout (honest repair, frozen counter)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2205', 'REFUSED', 0), ('S2236', 'REFUSED', 0), ('S2329', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2576', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2044', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2044', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2653', 'MALFORMED', 0), ('S2424', 'MALFORMED', 0), ('S2763', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2053', 'LOCATED', 1), ('S2762', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2604', 'TRUNCATED', 1), ('S2498', 'LOCATED', 1)] want=[('S2604', 'TRUNCATED', 1), ('S2498', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2851', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```

### Receipts C–L — full stdout of every mutant run

```
########## M1-scheme-relative-unvalidated.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2248', 'REFUSED', 0), ('S2645', 'REFUSED', 0), ('S2131', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2975', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2255', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2255', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2313', 'MALFORMED', 0), ('S2650', 'MALFORMED', 0), ('S2070', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2416', 'LOCATED', 1), ('S2887', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2532', 'TRUNCATED', 1), ('S2551', 'LOCATED', 1)] want=[('S2532', 'TRUNCATED', 1), ('S2551', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2686', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M2-userinfo-netloc-authority.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2976', 'REFUSED', 0), ('S2134', 'REFUSED', 0), ('S2502', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2742', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2218', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2218', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2047', 'MALFORMED', 0), ('S2156', 'MALFORMED', 0), ('S2340', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2647', 'LOCATED', 1), ('S2855', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2769', 'TRUNCATED', 1), ('S2248', 'LOCATED', 1)] want=[('S2769', 'TRUNCATED', 1), ('S2248', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2222', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M3-https-unvalidated.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2293', 'REFUSED', 0), ('S2413', 'REFUSED', 0), ('S2871', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2126', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2676', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2676', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2519', 'MALFORMED', 0), ('S2129', 'MALFORMED', 0), ('S2032', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2048', 'LOCATED', 1), ('S2442', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2153', 'TRUNCATED', 1), ('S2864', 'LOCATED', 1)] want=[('S2153', 'TRUNCATED', 1), ('S2864', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2406', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M4-malformed-target-unguarded.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2551', 'REFUSED', 0), ('S2722', 'REFUSED', 0), ('S2586', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2630', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2755', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2755', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2542', 'MALFORMED', 0), ('S2039', 'MALFORMED', 0), ('S2820', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2843', 'LOCATED', 1), ('S2517', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2634', 'TRUNCATED', 1), ('S2898', 'LOCATED', 1)] want=[('S2634', 'TRUNCATED', 1), ('S2898', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2603', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M5-relative-no-slash-against-root.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2306', 'REFUSED', 0), ('S2330', 'REFUSED', 0), ('S2426', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2044', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2030', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2030', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2163', 'MALFORMED', 0), ('S2884', 'MALFORMED', 0), ('S2523', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2154', 'LOCATED', 1), ('S2450', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2417', 'TRUNCATED', 1), ('S2610', 'LOCATED', 1)] want=[('S2417', 'TRUNCATED', 1), ('S2610', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2114', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M6-308-not-a-redirect.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2815', 'REFUSED', 0), ('S2625', 'REFUSED', 0), ('S2459', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2510', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2516', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2516', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2437', 'MALFORMED', 0), ('S2967', 'MALFORMED', 0), ('S2808', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2863', 'LOCATED', 1), ('S2877', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2555', 'TRUNCATED', 1), ('S2199', 'LOCATED', 1)] want=[('S2555', 'TRUNCATED', 1), ('S2199', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2196', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M7-fifth-response-always-fatal.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2941', 'REFUSED', 0), ('S2286', 'REFUSED', 0), ('S2274', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2558', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2810', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2810', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2380', 'MALFORMED', 0), ('S2209', 'MALFORMED', 0), ('S2667', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2319', 'LOCATED', 1), ('S2504', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2017', 'TRUNCATED', 1), ('S2573', 'LOCATED', 1)] want=[('S2017', 'TRUNCATED', 1), ('S2573', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2901', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M8-chain-bound-six.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=1 ["REDIRECT_LOOP:S2275:want=UNREACHABLE/5:got=[('UNREACHABLE', 6)]"] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l2:want=2:hits=3'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2566', 'REFUSED', 0), ('S2151', 'REFUSED', 0), ('S2687', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2362', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2984', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2984', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2899', 'MALFORMED', 0), ('S2743', 'MALFORMED', 0), ('S2868', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2321', 'LOCATED', 1), ('S2486', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2496', 'TRUNCATED', 1), ('S2189', 'LOCATED', 1)] want=[('S2496', 'TRUNCATED', 1), ('S2189', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2461', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
exit=1
```
```
########## M9-malformed-target-crash.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2187', 'REFUSED', 0), ('S2645', 'REFUSED', 0), ('S2162', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2688', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2034', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2034', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2730', 'MALFORMED', 0), ('S2724', 'MALFORMED', 0), ('S2898', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2801', 'LOCATED', 1), ('S2527', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2663', 'TRUNCATED', 1), ('S2864', 'LOCATED', 1)] want=[('S2663', 'TRUNCATED', 1), ('S2864', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2087', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```
```
########## M10-userinfo-target-unvalidated.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2564', 'REFUSED', 0), ('S2177', 'REFUSED', 0), ('S2193', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2707', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2719', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2719', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2560', 'MALFORMED', 0), ('S2182', 'MALFORMED', 0), ('S2685', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2331', 'LOCATED', 1), ('S2115', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2281', 'TRUNCATED', 1), ('S2505', 'LOCATED', 1)] want=[('S2281', 'TRUNCATED', 1), ('S2505', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2187', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
exit=0
```

### Receipt M — full stdout (honest tool, live revised counter, live lane artifacts)

```
TOOL PASS path=tools/reopen-row.py exists=True executable=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2655', 'REFUSED', 0), ('S2971', 'REFUSED', 0), ('S2290', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2841', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2458', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2458', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2857', 'MALFORMED', 0), ('S2632', 'MALFORMED', 0), ('S2595', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2956', 'LOCATED', 1), ('S2584', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2549', 'TRUNCATED', 1), ('S2049', 'LOCATED', 1)] want=[('S2549', 'TRUNCATED', 1), ('S2049', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2277', 'UNREACHABLE', 3)] wall=6.0s stall_hits=3 span=4.0s
REVIEW FAIL reports=4 token=3 missing=['rev-hold-lift.md'] thin=[] open_findings=[]
ACCEPT-O-63: FAIL
exit=1
```


The live revised counter's REVIEW leg reports `token=3 … open_findings=[]` for
the three real `RevToolA/B/C.md`: the mandated token itself does **not** taint
the scan in the live revision (it strips the token before scanning), so the
only outstanding REVIEW item is the missing `rev-hold-lift.md`.

## 3. Redirect-edge behaviour measured on the honest tool

Harness: `scratch/edge_probe.py` — two local `127.0.0.1` servers, one row per
case, `--passes 1 --gap 0 --allow-private` unless stated. "attempts" is the
row's `attempts=` value; the hit counts are what each server actually saw.

| # | case | honest-tool verdict | target server hit? | note |
|---|---|---|---|---|
| E1 | scheme-relative `Location: //127.0.0.1:<other port>/x` | `REFUSED attempts=1` | **no** | cross-authority hop refused before the request |
| E2 | scheme-relative to the **same** authority | `LOCATED attempts=2`, url = final | yes | same-authority hop followed |
| E3a | `Location: http://u@127.0.0.1:<other port>/x` | `REFUSED attempts=1` | **no** | userinfo ignored in the authority |
| E3b | `Location: http://u@127.0.0.1:<same port>/x` | `UNREACHABLE attempts=6` | **no** | same authority → allowed, but urllib cannot resolve a userinfo host (`Name or service not known`); 3 attempts × 2 passes |
| E4a | `Location: https://127.0.0.1:<closed TLS port>/x` (different port) | `REFUSED attempts=1` | **no** | refused as a cross-authority hop, before any TLS attempt |
| E4b | `Location: https://127.0.0.1:<same port>/x` (server speaks no TLS) | `UNREACHABLE attempts=6` | **no** | same authority → allowed; the TLS failure is transient, so it is retried 3× per pass |
| E5 | `Location: http://127.0.0.1:99999/x` (unparseable port) | `UNREACHABLE attempts=1`, **no traceback** | no | malformed *target* is a fatal hop, not a crash |
| E6 | `Location: sub/target` (relative, no leading slash) from `/dir/page` | `LOCATED attempts=2`, url = `/dir/sub/target` | yes | RFC-style resolution against the directory |
| E7 | `308` with a same-authority target | `LOCATED attempts=2` | yes | GET is safe; 308 preserves the method, so nothing to preserve |
| E8 | chain of exactly 5 requests, the 5th answers 200 | `LOCATED attempts=5`, url = final | yes | 5 requests is within the cap; the 200 is honoured |
| E9 | chain whose 5th response is still a redirect | `UNREACHABLE attempts=5` | yes (5 requests) | fatal end of the pass, no 6th request |
| E10 | chain of 7, first 200 at the 6th | `UNREACHABLE attempts=5` | yes (5 requests) | capped at 5 |
| E11 | cross-authority redirect **without** `--allow-private` | `REFUSED attempts=0` | **no** | the listed URL is refused before any request |

The two answers the assignment asked for explicitly:

* **http→https downgrade to a closed TLS port**: *transient or fatal?* —
  neither, in the honest tool: a **different port** makes it a
  cross-authority hop and it is **refused** (E4a, no request, no TLS
  handshake); the **same port** makes it same-authority, so the hop is
  attempted and the TLS failure is a **transient** error, retried 3× per pass
  and finally `UNREACHABLE attempts=6` (E4b). The frozen counter pins
  **neither** branch.
* **308 with a POST-unsafe method**: irrelevant for this tool — it issues
  only `GET`, and 308 preserves the method, so there is nothing to preserve
  that GET could violate. The only observable difference is whether 308 is
  followed at all, and the frozen counter never sends a 308.

## 4. What the frozen counter pins, and what it leaves unpinned

Verdict line per item. `CONTROL-MET` = a cheap fixture that skips the claimed
work still gets `ACCEPT-O-63: PASS` under the frozen counter (the counter
does not notice). `NONE-MET` = the counter catches it.

| item (redirect edge) | fixture that skipped the work | frozen verdict | verdict line |
|---|---|---|---|
| absolute cross-authority `Location` (different port) refused even under `--allow-private`; target never contacted | baseline round-62 tool (auto-follow) | FAIL, `REDIRECT` leg: `allow_private=[('S2383','LOCATED',1)] hits_target=1` | **NONE-MET** — the counter catches it |
| at most 5 requests per chain | M8 (`MAX_CHAIN_REQUESTS = 6`) | FAIL, `GEN` + `BOUND` (`REDIRECT_LOOP want UNREACHABLE/5 got 6`, `l2 want 2 hits 3`) | **NONE-MET** — the counter catches it |
| a redirect on the 5th response ends the pass as fatal (not located) | M8 above (a 6th request is made) | FAIL, `GEN` + `BOUND` | **NONE-MET** — the counter catches it |
| the **final** URL of the chain is the one reported | baseline round-62 tool | FAIL, `GEN` (`REDIRECT_OK url_want=… got=…`) | **NONE-MET** — the counter catches it |
| scheme-relative `Location` (`//host/x`) re-validated | M1 (skips the check for `//` targets) | PASS | **CONTROL-MET** — fixture: M1; the counter's only cross-authority fixture uses an **absolute** `Location` (`fx2.url(...)`), so a scheme-relative hop to another authority is never exercised. Smallest counter change: in the REDIRECT leg add one more row whose `Location` is `//127.0.0.1:<other port>/x` and assert `REFUSED attempts=1` + target hits 0. |
| `Location` carrying **userinfo** | M10 (skips the check when the target netloc contains `@`); M2 (compares the raw netloc instead of host+effective port) | PASS | **CONTROL-MET** — fixtures: M10, M2; no fixture anywhere uses userinfo. Smallest counter change: one REDIRECT-leg row with `Location: http://u@127.0.0.1:<other port>/x` asserting `REFUSED attempts=1` + target hits 0 (and, for M2, a same-authority userinfo row asserting the hop is *followed*, so that over-refusal is caught too). |
| `https` target re-validated | M3 (skips the check for `https` targets) | PASS | **CONTROL-MET** — fixture: M3; the counter contains no `https` URL at all. Smallest counter change: one REDIRECT-leg row with `Location: https://127.0.0.1:<other port>/x` asserting the target is never contacted, plus a same-port `https` row asserting the transient-vs-fatal classification. |
| malformed redirect **target** (unparseable port) does not crash the tool | M9 (every guard around the target removed) | PASS | **CONTROL-MET** — fixture: M9; M9 really does die with a raw `ValueError` traceback on such a hop (measured), yet the counter scores it `PASS`. The MALFORMED leg only covers malformed **listed** URLs, and the ERR leg only covers bad *invocations*, so no leg observes a crash raised while following a redirect. Smallest counter change: one GEN class whose `Location` is `http://127.0.0.1:99999/x`, asserted to produce no `Traceback` on either stream and exit 1. |
| relative `Location` **without** a leading slash resolved against the directory | M5 (resolves against the server root) | PASS | **CONTROL-MET** — fixture: M5; the counter's redirect fixtures all use leading-slash paths. Smallest counter change: one GEN class with `Location: sub/target` from a `/dir/page` base, asserting the fetched path is `/dir/sub/target` (this is what makes E6's two possible resolutions distinguishable). |
| `308` treated as a redirect | M6 (308 not treated as a redirect) | PASS | **CONTROL-MET** — fixture: M6; the counter's redirect statuses are 301/302/303/307 only. Smallest counter change: one GEN class answering `308`. |
| a chain of exactly 5 requests whose 5th response is **200** is honoured | M7 (the 5th request is always fatal) | PASS | **CONTROL-MET** — fixture: M7; the counter's `REDIRECT_MULTI` is a 4-request chain and `REDIRECT_LOOP`'s 5th response is a redirect, so "5 requests then 200" is never observed. Smallest counter change: one GEN class with four redirects and a 200 on the fifth, asserting `LOCATED` with `attempts=5`. |

Aggregate: **the frozen counter pins 4 of the 11 redirect properties I could
vary** (cross-authority absolute refusal, the 5-request cap, the fatal
5th-redirect, and reporting the final URL) and leaves **7 unpinned**, each of
which a one-fixture addition to the REDIRECT/GEN classes would close.

Note on the "cheap fixture" qualifier: every CONTROL-MET fixture above is a
one-line change to an otherwise conforming tool (skip one `check_target` call,
change one comparison, drop one guard) — i.e. exactly the kind of shortcut a
future edit could introduce.

## 5. Other things the frozen counter does and does not pin (adjacent risk)

* The counter's REDIRECT leg pins the refusal of a cross-authority hop **to a
  different port on the same host**. It does not distinguish host from port:
  a mutant that compared only the host, or only the port, would still be
  caught here, but the case "same port, different host" (e.g.
  `http://localhost:<port>/x` against `http://127.0.0.1:<port>/x`) is not
  exercised at all. It is fail-closed in the honest tool (host strings differ
  → refused) but unpinned.
* The honest tool compares authorities on `(host, effective port)` with the
  host lowercased but **not** IDNA-normalised and without IPv6 bracket
  canonicalisation. Two spellings of one host therefore compare unequal and
  the hop is refused — fail-closed, but unpinned by the counter.
* The claim's "refused even under `--allow-private`" rule makes the tool
  refuse *legitimate* public→public hops that change authority (a CDN
  redirect). That is what the frozen counter's REDIRECT leg demands
  (`hits_target=0` for a different port), so it is the specified behaviour,
  not a defect — but it is an operational cost the L1 should be aware of,
  and the counter pins only the loopback case of it.
* The counter's REVIEW leg is the only leg that depends on artifacts outside
  the tool. At the freeze it fails for every tool (four artifacts missing);
  in my receipts A–L I supplied the missing one as a scratch stub so the
  receipt reflects the tool. The L1 must re-run the counter with the real
  artifacts once `reports/round-63/telemetry/rev-hold-lift.md` lands.

## 6. Risks, blockers, and what I did not do

* **Blocker for the claim, not for me**: `reports/round-63/telemetry/rev-hold-lift.md`
  did not exist in the lane at measurement time, so the REVIEW leg cannot pass
  in the lane as it stands. Receipt M shows every other leg of the live
  revised counter passing against a conforming tool.
* I did not run `tools/reopen-row.py` from the lane repo at all (safety hold);
  every tool I executed was a scratch copy.
* I did not write to the lane repo except this report; no git/jj write command
  was issued anywhere.
* No live URL was fetched; every endpoint was a loopback server started by
  my own harness. The `web.archive.org` CDX API was not needed.
* I did not judge, re-scale or amend the claim or the counter, and I did not
  propose counter text beyond naming the smallest fixture that would close
  each gap.
* The mutation matrix uses the **frozen** counter (revision 0). The lane's
  counter has since been revised (MutCounterO / MutCounterC edits: executable
  TOOL leg, a >1 MiB gzip pad, a stall-span assertion on TIMEOUT, the
  `>= 400 bytes` and OPEN-marker scan on REVIEW). I ran the live revision once
  (receipt M) and it agrees with the frozen revision on every leg my mutants
  touch — the seven unpinned edges are unpinned under **both** revisions,
  because the added fixtures are all in GEN/REDIRECT and none of them uses a
  scheme-relative, userinfo, https, malformed-target, slash-less-relative,
  308, or five-then-200 Location.
* **Provenance note**: this report file was written twice. The first write
  mis-transcribed four lines of pasted counter stdout (row-id lists inside the
  `PRIV`, `TRUNC`, `MALFORMED`, `GZIP` leg lines of receipts A, M, M5, M6 and
  M10). The second write is generated by `scratch/make_report.py`, which
  copies every pasted stdout block byte-for-byte out of the captured run files
  (`scratch/accept-o-baseline.txt`, `scratch/runs4/*.txt`,
  `scratch/runs2/live-counter-honest.txt`), so no hand transcription remains.
  No measurement, verdict or receipt line changed between the two writes.

## 7. Files this seat produced (all under scratch, except this report)

* `scratch/patch_honest.py` — builds the honest repaired tool from the frozen
  clone (30 asserted patches).
* `scratch/honest/tools/reopen-row.py` — the honest repaired tool.
* `scratch/edge_probe.py` — the 11-case redirect-edge harness.
* `scratch/make_mutants.py` — builds mutants M1–M10 from the honest tool.
* `scratch/mutants/M*/tools/reopen-row.py` — the mutants (one skipped
  property each).
* `scratch/run_matrix.py`, `scratch/run_final.py`, `scratch/run_receipts.py` —
  the counter runners (frozen counter, `--root` per variant).
* `scratch/runs/`, `scratch/runs2/`, `scratch/runs3/`, `scratch/runs4/` — the
  captured full stdout of every run quoted above.
* `scratch/edge-*.txt` — the per-case edge tables for the honest tool and for
  each mutant.
* `scratch/make_report.py` — regenerates this report from the captured runs.
