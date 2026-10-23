# MutCounterO — pre-data control for claim O (counter mutation probes)

- Seat: `kotodama-r63-w1-MutCounterO` (mutation tester, leaf; no subagents, no installs).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, rev `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` (freeze; round base `65b393e`).
- Isolated sandbox: `git clone` of the lane at the freeze in `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterO/clone` (GIT_DIR/GIT_WORK_TREE never pointed at the lane). The lane was never modified by this seat.
- Object scored: the **unrepaired base** `tools/reopen-row.py` at the freeze, sha256 `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803` (same bytes as `git show 65b393e:tools/reopen-row.py`; no redirect re-validation, plain `urlopen`, silent 4 MiB read cap, per-socket 30 s timeout, no `--timeout` flag).
- Frozen counter: `reports/round-63/accept-o.py`, sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` — matches the sha named in the round-63 tasking/claims; revision 0, unmodified here.
- All fixtures are offline localhost (`127.0.0.1`) servers built by the counter itself; no live fetch, no browser, no bot-challenge circumvention.
- No tool installs or upgrades were made or needed.

## What was mutated (PROBE copies only, under the scratch clone)

Copied `reports/round-63/accept-o.py` four times inside the scratch clone and changed one behaviour-bearing point each:

```diff
=== probe_drop_redirect.py ===
-            leg("REDIRECT", red_ok,
+            leg("REDIRECT", True,  # PROBE: leg gate dropped

=== probe_trunc_absent.py ===
-    "TRUNC_FAR": ("TRUNCATED", 1, {"live": 1}),
+    "TRUNC_FAR": ("ABSENT", 1, {"live": 1}),  # PROBE: expects ABSENT
@@
-            t_expect.append((sid, "TRUNCATED" if far else "LOCATED", 1))
+            t_expect.append((sid, "ABSENT" if far else "LOCATED", 1))  # PROBE: TRUNC_FAR expects ABSENT

=== probe_timeout_600.py ===
-            leg("TIMEOUT", stc == 1 and stgot == [(stall_sid, "UNREACHABLE", 3)] and wall < 45
+            leg("TIMEOUT", stc == 1 and stgot == [(stall_sid, "UNREACHABLE", 3)] and wall < 600  # PROBE: wall bound weakened
                 and "Traceback" not in (stout + sterr),

=== probe_no_review.py ===
-        leg("REVIEW", not missing and all(verdicts),
+        leg("REVIEW", True,  # PROBE: review gate dropped
```

Probe hashes (the exact counters run):

| probe | sha256 |
|---|---|
| frozen `accept-o.py` | `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` |
| `probe_drop_redirect.py` | `0c562d6899addcb0fed4c9c1244f25a5036df2efa2e76b255399f2e0e1c44564` |
| `probe_trunc_absent.py` | `a1a34931d7bb05ef0fac6189653d68eabb2ded419f7baa8f01795bf87ad7bb7f` |
| `probe_timeout_600.py` | `7f1a463a13583ff8fe5639acbe49ccf9aa2c2e7d365669854da87a6bfb0b2125` |
| `probe_no_review.py` | `486b58c3e092f1f4f7abc2d259f7d69bd3edb63cdf4345765a4cecfa638c5f49` |

Every case below was scored with the same base tool bytes and the same freeze clone; `frozen=` is the verdict of the **unmutated** counter on that same base tool (the pristine receipt below).

## Receipts

```
RECEIPT kotodama-r63-w1-MutCounterO/frozen-base counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW
RECEIPT kotodama-r63-w1-MutCounterO/probe-drop-redirect counter-sha256=0c562d6899addcb0fed4c9c1244f25a5036df2efa2e76b255399f2e0e1c44564 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW
RECEIPT kotodama-r63-w1-MutCounterO/probe-trunc-absent counter-sha256=a1a34931d7bb05ef0fac6189653d68eabb2ded419f7baa8f01795bf87ad7bb7f rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TIMEOUT,REVIEW
RECEIPT kotodama-r63-w1-MutCounterO/probe-timeout-600 counter-sha256=7f1a463a13583ff8fe5639acbe49ccf9aa2c2e7d365669854da87a6bfb0b2125 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW
RECEIPT kotodama-r63-w1-MutCounterO/probe-no-review counter-sha256=486b58c3e092f1f4f7abc2d259f7d69bd3edb63cdf4345765a4cecfa638c5f49 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT
```

## Verdicts per mutated item

- `CONTROL-NONE-MET` (drop REDIRECT leg). The base tool still fails 8 other legs; no overall PASS. The mutation does blind the **only** leg that probes cross-authority refusal: with the gate dropped the REDIRECT line reads PASS while the base leaked to the loopback target (`hits_target=1`, `allow_private=[('S2973','LOCATED',1)]`). GEN/BOUND catch only attempt-count/hop semantics of same-authority redirect classes, not the private-host refusal. Smallest counter change that restores the kill: the unmutated `leg("REDIRECT", red_ok, ...)` gate (as frozen).
- `CONTROL-NONE-MET` (TRUNC_FAR expects ABSENT). The TRUNC leg PASSes under the base (`rows=[('S2426','ABSENT',1),('S2222','LOCATED',1)] want=[('S2426','ABSENT',1),('S2222','LOCATED',1)]`), and with the CLASSES entry swapped GEN's TRUNC_FAR fixture is also blind to silent truncation. No overall PASS (base still fails GEN/ORDER/BOUND/REDIRECT/MALFORMED/GZIP/TIMEOUT/REVIEW). Smallest change that restores the kill: expect `TRUNCATED` in both `CLASSES["TRUNC_FAR"]` and `t_expect`.
- `CONTROL-NONE-MET` (TIMEOUT wall < 600). The base still fails TIMEOUT, but for a different reason: it exits 2 on the unknown `--timeout` flag (`exit=2 rows=[] wall=0.0–0.1s`), so **the wall bound itself is not exercised against this base** — inconclusive for that property, not a kill. [INFERENCE] a tool that accepted `--timeout` but kept a 30 s per-socket budget would take ~90 s on this fixture and pass under `<600` while failing under `<45`; unobserved here. Smallest change that restores the kill: `wall < 45` plus the `--timeout`-flag cases the base already fails.
- `CONTROL-NONE-MET` (REVIEW gate removed). The REVIEW leg PASSes trivially under the base (`reports=4 missing=['RevToolA.md','RevToolB.md','RevToolC.md','rev-hold-lift.md'] clean=0`) yet ACCEPT still FAILs on 8 other legs. Removing the gate would let an otherwise-green repair skip the named independent review artifacts; it does not let the base pass. Smallest change that restores the kill: the unmutated `not missing and all(verdicts)` condition.

Summary: no single one of the four mutations lets the unrepaired base tool reach `ACCEPT-O-63: PASS`; the base is killed independently on 8–9 legs in every probe, so the frozen counter's separation at base is overdetermined. What the probes do establish is that each mutated point is load-bearing *within its leg* (REDIRECT, TRUNC, REVIEW), and that the TIMEOUT wall bound is not testable against this base because the flag does not exist yet.

## Full stdout per run

### 1) frozen accept-o.py vs base — exit=1 (wall 302.7 s; DEFAULT leg alone 150 s)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=61 ["REDIRECT_MULTI:S2133:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2133:url_want=http://127.0.0.1:42963/fvdpvlpi:got=['http://127.0.0.1:42963/bgeytrl']", "TRUNC_FAR:S2624:want=TRUNCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2946:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2946:url_want=http://127.0.0.1:42963/knyfux/stpkuaqzk/jgax:got=['-']", 'MALFORMED_IPV6:S2969:want=MALFORMED/0:got=[]'] summary_ok=False exit=1
ORDER FAIL printed=33 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['TRANSIENT_PASS:live:want=4:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'CAP_ID:live:want=1:hits=0', 'CAP_CLASS_GALLERY:live:want=1:hits=0', 'REDIRECT_OK:live:want=1:hits=0', 'REDIRECT_OK:rtarget:want=1:hits=0', 'CAP_CLASS_THUMB:live:want=1:hits=0', 'CAP_ATTR_TITLE:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2875', 'REFUSED', 0), ('S2410', 'REFUSED', 0), ('S2850', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2770', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2588', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2588', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2582', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2090', 'ABSENT', 1), ('S2335', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2162', 'ABSENT', 1), ('S2183', 'LOCATED', 1)] want=[('S2162', 'TRUNCATED', 1), ('S2183', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

### 2) probe_drop_redirect.py vs base — exit=1 (wall 303.1 s)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=51 ["REDIRECT_LOOP:S2766:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "REDIRECT_OK:S2991:want=LOCATED/2:got=[('LOCATED', 1)]", "REDIRECT_OK:S2991:url_want=http://127.0.0.1:35789/pybyihosu/xdalz:got=['http://127.0.0.1:35789/cpgdnhew']", "GZIP_BODY:S2966:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2966:url_want=http://127.0.0.1:35789/gtcuyci/xicejbn/cqvmiyq:got=['-']", "TRUNC_FAR:S2501:want=TRUNCATED/1:got=[('ABSENT', 1)]"] summary_ok=False exit=1
ORDER FAIL printed=40 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=5', 'REDIRECT_LOOP:l2:want=2:hits=4', 'CAP_ATTR:live:want=1:hits=0', 'CAP_ATTR_ARIA:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'CAP_CLASS_THUMB:live:want=1:hits=0', 'DEAD:live:want=9:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2484', 'REFUSED', 0), ('S2333', 'REFUSED', 0), ('S2173', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2206', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2973', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2973', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2122', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2298', 'ABSENT', 1), ('S2262', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2675', 'ABSENT', 1), ('S2795', 'LOCATED', 1)] want=[('S2675', 'TRUNCATED', 1), ('S2795', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

### 3) probe_trunc_absent.py vs base — exit=1

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=101 ["MALFORMED_PORT:S2128:want=MALFORMED/0:got=[('UNREACHABLE', 9)]", 'MALFORMED_IPV6:S2018:want=MALFORMED/0:got=[]', 'MALFORMED_IPV6:S2018:url_want=-:got=None', 'REDIRECT_LOOP:S2486:want=UNREACHABLE/5:got=[]', 'REDIRECT_LOOP:S2486:url_want=-:got=None', 'ARCHIVE_CAPTION:S2703:want=CAPTION_ONLY/2:got=[]'] summary_ok=False exit=1
ORDER FAIL printed=11 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=0', 'REDIRECT_LOOP:l2:want=2:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'TRANSIENT2:live:want=3:hits=0', 'GONE:live:want=1:hits=0', 'TRUNC_FAR:live:want=1:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2623', 'REFUSED', 0), ('S2384', 'REFUSED', 0), ('S2520', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2081', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2120', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2120', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2116', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2410', 'ABSENT', 1), ('S2324', 'ABSENT', 1)]
TRUNC PASS exit=1 rows=[('S2426', 'ABSENT', 1), ('S2222', 'LOCATED', 1)] want=[('S2426', 'ABSENT', 1), ('S2222', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

### 4) probe_timeout_600.py vs base — exit=1

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=116 ["REDIRECT_MULTI:S2882:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2882:url_want=http://127.0.0.1:44661/djwua:got=['http://127.0.0.1:44661/gqbr/iscgfmd']", 'MALFORMED_IPV6:S2024:want=MALFORMED/0:got=[]', 'MALFORMED_IPV6:S2024:url_want=-:got=None', 'CAP_ATTR_DATA:S2147:want=CAPTION_ONLY/1:got=[]', 'CAP_ATTR_DATA:S2147:url_want=http://127.0.0.1:44661/stortwsdi:got=None'] summary_ok=False exit=1
ORDER FAIL printed=4 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['CAP_ATTR_DATA:live:want=1:hits=0', 'REDIRECT_OK:live:want=1:hits=0', 'REDIRECT_OK:rtarget:want=1:hits=0', 'CAP_ATTR_TITLE:live:want=1:hits=0', 'TRANSIENT2:live:want=3:hits=0', 'BODY_THEN_ARCHIVE:live:want=1:hits=0', 'CAP_ATTR_META:live:want=1:hits=0', 'CAP_ATTR_ARIA:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2369', 'REFUSED', 0), ('S2942', 'REFUSED', 0), ('S2845', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2813', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2321', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2321', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2782', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2914', 'ABSENT', 1), ('S2366', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2087', 'ABSENT', 1), ('S2736', 'LOCATED', 1)] want=[('S2087', 'TRUNCATED', 1), ('S2736', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.1s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

### 5) probe_no_review.py vs base — exit=1

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=91 ["GZIP_BODY:S2216:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2216:url_want=http://127.0.0.1:34761/vzuy/ymvvg:got=['-']", "REDIRECT_MULTI:S2935:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2935:url_want=http://127.0.0.1:34761/ousbmgrg/bcmuqs:got=['http://127.0.0.1:34761/prlwddfm']", "REDIRECT_OK:S2311:want=LOCATED/2:got=[('LOCATED', 1)]", "REDIRECT_OK:S2311:url_want=http://127.0.0.1:34761/xjgs/esgbtnxsp/jkhedgpn:got=['http://127.0.0.1:34761/zptahkdlk']"] summary_ok=False exit=1
ORDER FAIL printed=19 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['GONE:live:want=1:hits=0', 'SCRIPT:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'CAP_CLASS_THUMB:live:want=1:hits=0', 'CAP_ATTR_DATA:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'PLAIN:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2469', 'REFUSED', 0), ('S2526', 'REFUSED', 0), ('S2508', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2727', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2162', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2162', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2674', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2405', 'ABSENT', 1), ('S2227', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2205', 'ABSENT', 1), ('S2665', 'LOCATED', 1)] want=[('S2205', 'TRUNCATED', 1), ('S2666', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW PASS reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

The same lines captured directly from the run files are in scratch at `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-MutCounterO/run_*.out` / `run_*.err` (stderr was empty for all four probe runs).

## Restoration / integrity evidence

- The base tool and the frozen counter were **never edited**: before and after all runs, `tools/reopen-row.py` sha256 = `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803` and `reports/round-63/accept-o.py` sha256 = `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`. No restoration was needed; the four mutants exist only as `reports/round-63/probe_*.py` inside the disposable scratch clone.
- The lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin` was read only (clone source, claims/docstrings); this report is its only write. No git/jj write commands were run there.
- Every run used the freeze rev `80d53ffde7788299b69dbb0bd0436b2b7ddddb95`; fixtures are localhost only; no live request was issued by this seat.
