# Round 63, wave 1 — MutToolNeutral (claim O neutral-patch probe)

Seat: kotodama-r63-w1-MutToolNeutral (mutation-tester, leaf, no delegation, no installs).
Counter under test (frozen, unmodified): `reports/round-63/accept-o.py`
sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`
Clone: `/fast/scratch/hyaku/kotodama-r63/MutToolNeutral/clone`, rev `80d53ffde7788299b69dbb0bd0436b2b7ddddb95`.
Command shape: `cd clone && python3 -B reports/round-63/accept-o.py [--root ../<case>]`, full stdout below.

## 0. Baseline object and workaround

At the sanctioned wait-check, `/fast/scratch/hyaku/kotodama-r63/ExecRepairTool/reopen-row.py`
was byte-identical to the frozen round-62 tool
(sha256 `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803`, no MALFORMED/gzip/TRUNCATED/
--timeout), i.e. not yet the repair. Per assignment I therefore built the neutral baseline:
`/fast/scratch/hyaku/kotodama-r63/MutToolNeutral/repaired.py`
(sha256 `3f664e41a7642d9633551380cb0110980dc101564d4629b577d86decb2c2c44d`), a minimal
implementation of the claim-O contract (redirect re-validation with strict private refusal for
cross-authority hops, 5-request chain cap, MALFORMED, gzip, 4 MiB TRUNCATED, `--timeout` wall budget,
round-62 verdict/retry/exit behaviour). The first six mutants are patches of that implementation.

The executor's repaired artifact landed later
(sha256 `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5`, copied to
`.../MutToolNeutral/art/tools/reopen-row.py`). It was baseline-scored, and the surviving
defect class (per-request deadline) was re-probed on it as `m5art`; hash identical before and
after the run.

Review-gate fixtures: my scratch roots carry stand-in `.ufo/waves/round-63/w1/RevTool{A,B,C}.md`
and `reports/round-63/telemetry/rev-hold-lift.md` containing `VERDICT: NO-OPEN-HIGH-MED` so the
REVIEW leg exercises the tool legs in isolation. These are scratch environment fixtures only;
nothing was written to the lane except this report. The lane review gate's actual outcome is the
reviewers' artifact, not mine.

Environment note: a peer notice (RevToolC) reported an `OPEN-(HIGH|MED)` taint regex in the frozen
counter. The frozen counter at sha `a751efec` that I ran has no such regex — its REVIEW leg is a
literal substring check for the token (the token therefore passes). Not evaluated further here.

## 1. Receipts

One line per case: `RECEIPT <case> counter-sha256=<frozen sha> rev=80d53ff... frozen=<PASS|FAIL> exit=<n> stopped-by=<FAIL legs>`.

```
RECEIPT MutToolNeutral/pristine_impl counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=-
RECEIPT MutToolNeutral/m1_noredirect counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=REDIRECT
RECEIPT MutToolNeutral/m2_nomalformed counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,MALFORMED
RECEIPT MutToolNeutral/m3_nogzip counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,GZIP
RECEIPT MutToolNeutral/m4_notrunc counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,TRUNC
RECEIPT MutToolNeutral/m5_nodeadline counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=-
RECEIPT MutToolNeutral/m6_perfetch counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN
RECEIPT MutToolNeutral/art_pristine counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=-
RECEIPT MutToolNeutral/m5art_nodeadline counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=-
```

## 2. Full stdout per run (never trimmed)

### pristine_impl (`repaired.py`, sha256 3f664e41…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2547', 'REFUSED', 0), ('S2983', 'REFUSED', 0), ('S2640', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2288', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2770', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2770', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2418', 'MALFORMED', 0), ('S2172', 'MALFORMED', 0), ('S2929', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2430', 'LOCATED', 1), ('S2084', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2541', 'TRUNCATED', 1), ('S2728', 'LOCATED', 1)] want=[('S2541', 'TRUNCATED', 1), ('S2728', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2501', 'UNREACHABLE', 3)] wall=12.0s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
```
exit=0, wall 164.62 s.

### m1_noredirect — redirect target followed without re-validation (sha256 5c8f96fa…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2442', 'REFUSED', 0), ('S2616', 'REFUSED', 0), ('S2933', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2705', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2766', 'LOCATED', 2)] hits_src=1 hits_target=1 no_flag=[('S2766', 'REFUSED', 0)] exits=0,1
MALFORMED PASS exit=1 rows=[('S2280', 'MALFORMED', 0), ('S2192', 'MALFORMED', 0), ('S2597', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2162', 'LOCATED', 1), ('S2612', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2069', 'TRUNCATED', 1), ('S2451', 'LOCATED', 1)] want=[('S2069', 'TRUNCATED', 1), ('S2451', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2500', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
```
exit=1. KILLED: cross-authority 302 to the second loopback authority is followed (LOCATED attempts=2, target hit=1) instead of REFUSED attempts=1 with 0 target hits.

### m2_nomalformed — MALFORMED branch removed, parse ValueError propagates (sha256 9305c8d6…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=15 ["MALFORMED_PORT:S2612:want=MALFORMED/0:got=[('UNREACHABLE', 9)]", 'MALFORMED_IPV6:S2540:want=MALFORMED/0:got=[]', 'MALFORMED_IPV6:S2540:url_want=-:got=None', 'ABSENT:S2466:want=ABSENT/1:got=[]', 'ABSENT:S2466:url_want=-:got=None', 'TRUNC_NEAR:S2069:want=LOCATED/1:got=[]'] summary_ok=False exit=1
ORDER FAIL printed=54 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['ABSENT:live:want=1:hits=0', 'TRUNC_NEAR:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'REDIRECT_OK:live:want=1:hits=0', 'REDIRECT_OK:rtarget:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2781', 'REFUSED', 0), ('S2526', 'REFUSED', 0), ('S2977', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2906', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2009', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2009', 'REFUSED', 0)] exits=1,1
MALFORMED FAIL exit=1 rows=[('S2046', 'UNREACHABLE', 9)] traceback=True
GZIP PASS exit=1 rows=[('S2193', 'LOCATED', 1), ('S2077', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2372', 'TRUNCATED', 1), ('S2126', 'LOCATED', 1)] want=[('S2372', 'TRUNCATED', 1), ('S2126', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2712', 'UNREACHABLE', 3)] wall=12.0s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
```
exit=1. KILLED: first malformed row still answers UNREACHABLE/9 (the bad-port parse kills the run's row stream) and the MALFORMED leg shows a Traceback with only one of three rows printed.

### m3_nogzip — Content-Encoding gzip not decoded (sha256 67df33b8…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=2 ["GZIP_BODY:S2521:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2521:url_want=http://127.0.0.1:42333/gtawqx/evob/ivma:got=['-']"] summary_ok=False exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2969', 'REFUSED', 0), ('S2123', 'REFUSED', 0), ('S2141', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2365', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2557', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2557', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2389', 'MALFORMED', 0), ('S2330', 'MALFORMED', 0), ('S2328', 'MALFORMED', 0)] traceback=False
GZIP FAIL exit=1 rows=[('S2507', 'ABSENT', 1), ('S2764', 'ABSENT', 1)]
TRUNC PASS exit=1 rows=[('S2724', 'TRUNCATED', 1), ('S2247', 'LOCATED', 1)] want=[('S2724', 'TRUNCATED', 1), ('S2247', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2077', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
```
exit=1. KILLED by both GEN and the GZIP leg (both gzip rows read as ABSENT).

### m4_notrunc — silent 4 MiB cap, no TRUNCATED verdict (sha256 7c15e755…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=1 ["TRUNC_FAR:S2069:want=TRUNCATED/1:got=[('ABSENT', 1)]"] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2240', 'REFUSED', 0), ('S2812', 'REFUSED', 0), ('S2849', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2049', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2194', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2194', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2054', 'MALFORMED', 0), ('S2825', 'MALFORMED', 0), ('S2334', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2267', 'LOCATED', 1), ('S2608', 'CAPTION_ONLY', 1)]
TRUNC FAIL exit=1 rows=[('S2929', 'ABSENT', 1), ('S2422', 'LOCATED', 1)] want=[('S2929', 'TRUNCATED', 1), ('S2422', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2309', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
```
exit=1. KILLED by GEN and TRUNC (far quote answers ABSENT, near quote still LOCATED — the truncation distinction is what fails).

### m5_nodeadline — no per-request wall deadline, per-socket timeout only (sha256 00a4873d…) — SURVIVED

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2147', 'REFUSED', 0), ('S2470', 'REFUSED', 0), ('S2070', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2063', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2823', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2823', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2691', 'MALFORMED', 0), ('S2115', 'MALFORMED', 0), ('S2196', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2371', 'LOCATED', 1), ('S2362', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2522', 'TRUNCATED', 1), ('S2705', 'LOCATED', 1)] want=[('S2522', 'TRUNCATED', 1), ('S2705', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2913', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
```
exit=0. SURVIVED (coverage finding, section 3).

### m6_perfetch — attempts counted per URL try, not per redirect request (sha256 2c737f85…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=3 ["REDIRECT_MULTI:S2403:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_LOOP:S2687:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "REDIRECT_OK:S2045:want=LOCATED/2:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2465', 'REFUSED', 0), ('S2689', 'REFUSED', 0), ('S2476', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2723', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2973', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2973', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2390', 'MALFORMED', 0), ('S2287', 'MALFORMED', 0), ('S2954', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2089', 'LOCATED', 1), ('S2635', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2354', 'TRUNCATED', 1), ('S2268', 'LOCATED', 1)] want=[('S2354', 'TRUNCATED', 1), ('S2268', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2823', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: FAIL
```
exit=1. KILLED by GEN on all three followed-redirect attempt counts (1 vs 2/4/5). Note the refusal path stays correct (a refused first hop still counts 1) — GEN, not the REDIRECT leg, is the detector.

### art_pristine — executor's repaired artifact (sha256 0d965ccb…)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2556', 'REFUSED', 0), ('S2647', 'REFUSED', 0), ('S2676', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2207', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2751', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2751', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2049', 'MALFORMED', 0), ('S2115', 'MALFORMED', 0), ('S2682', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2668', 'LOCATED', 1), ('S2046', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2147', 'TRUNCATED', 1), ('S2721', 'LOCATED', 1)] want=[('S2147', 'TRUNCATED', 1), ('S2721', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2613', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
```
exit=0, wall 164.70 s. Artifact hash before/after the run: `0d965ccb…` both.

### m5art_nodeadline — artifact with the per-request wall budget removed (sha256 38a5ae77…) — SURVIVED

Patch: `fetch` opener budget set to `self.timeout`; `_read_body` no longer re-aims the socket at the
remaining budget and no longer checks the deadline after each chunk.

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2751', 'REFUSED', 0), ('S2850', 'REFUSED', 0), ('S2721', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2255', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2095', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2095', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2365', 'MALFORMED', 0), ('S2012', 'MALFORMED', 0), ('S2370', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2498', 'LOCATED', 1), ('S2601', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2670', 'TRUNCATED', 1), ('S2618', 'LOCATED', 1)] want=[('S2670', 'TRUNCATED', 1), ('S2618', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2433', 'UNREACHABLE', 3)] wall=12.1s
REVIEW PASS reports=4 missing=[] clean=4
ACCEPT-O-63: PASS
```
exit=0. SURVIVED on the actual artifact.

## 3. Coverage finding (surviving mutant)

**Mutant.** Remove the per-request wall budget and keep only the per-socket timeout
(`m5_nodeadline` on the neutral baseline; `m5art_nodeadline` on the executor's repaired artifact
`0d965ccb…`). This is routed defect 2 ("30 s timeout is per-socket not per-request") reproduced
exactly.

**Why it survives.** The TIMEOUT leg is one endpoint that answers headers, writes 100 bytes, then
blocks for 120 s. A single `read` blocks for the whole `--timeout`; a per-socket timeout of 4 s
fires exactly like a 4 s wall deadline would. Attempts (3), verdict (UNREACHABLE), exit (1) and
wall (12.1 s < 45 s) are identical under both behaviours, so the leg cannot separate them.

**Smallest counter change that would stop it.** Replace the single stall with a drip: after the
headers, send one body byte every `--timeout / 2` seconds for ~`6 × timeout` seconds (keep
Content-Length larger than what is sent). With `--timeout 4` a per-socket timeout never fires
(each gap is 2 s), so the socket-only mutant runs ~24 s per attempt (wall ≫ 45 s or a different
verdict), while a true per-request wall budget aborts each attempt at 4 s (wall ≈ 12 s, attempts=3).
The existing `wall < 45` and `attempts=3` assertions then kill the mutant; no new leg is needed.
A second, independent discriminator is a slow-header case (`urlopen` timeout is per operation),
but the drip body alone is sufficient for this counter.

Residual note: the other five behaviours (cross-authority redirect refusal, MALFORMED, gzip,
TRUNCATED, per-request attempt counting) are each killed by at least one frozen leg, so the
counter's coverage of the routed-defect set is 5/6, with the sixth a genuine blind spot rather
than an implementation-specific artefact (confirmed on both the neutral baseline and the landed
repair).

## 4. Restoration / bounds evidence

- Baseline object `repaired.py` sha256 `3f664e41a7642d9633551380cb0110980dc101564d4629b577d86decb2c2c44d`
  before and after all six patches; each mutant was a separate copy under its own root, and the
  pristine copy in the clone root has the same hash (`clone/tools/reopen-row.py`).
- Artifact copy `art/tools/reopen-row.py` sha256 `0d965ccb…` before and after the artifact baseline;
  the source `/fast/scratch/hyaku/kotodama-r63/ExecRepairTool/reopen-row.py` had the same hash at
  the end. No lane tool file was written or executed in place.
- Mutant hashes: m1 `5c8f96fa…`, m2 `9305c8d6…`, m3 `67df33b8…`, m4 `7c15e755…`,
  m5 `00a4873d…`, m6 `2c737f85…`, m5art `38a5ae77…`. Diffs are the single hunks shown in §2
  headers; no other change in any copy.
- The frozen counter was run unmodified from the clone (`sha256 a751efec…`, identical to the lane
  file at `reports/round-63/accept-o.py`). Only REVIEW stand-ins were added inside scratch roots.
- No tool installs or upgrades were performed. No git/jj write commands were run in the lane or the
  fleet repo; this report is the only lane file written by this seat.

## Verdict

Claim-O neutral-patch probe: 5 of 6 single-behaviour-removal patches are killed by the frozen
counter (m1/m2/m3/m4/m6). The per-request-deadline removal **survives on both the neutral baseline
and the executor's landed repair** (`0d965ccb…`), so ACCEPT-O-63 as frozen cannot distinguish a
per-request wall budget from a per-socket timeout; the TIMEOUT leg needs the drip-body fixture
described in §3. Everything else in the claim-O repair is defended by the frozen legs on offline
fixtures.
