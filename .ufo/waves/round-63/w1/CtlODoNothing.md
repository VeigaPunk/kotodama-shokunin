# CtlODoNothing — PRE-DATA CONTROL, claim O (accept-o.py)

Seat: `kotodama-r63-w1-CtlODoNothing` (mutation-tester / control). Date: 2026-10-23 UTC.
Lane freeze: `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` (round base `65b393ef3a4d82bd693cc21b7f96a1231417d522`).
Counter run unmodified in every case: `reports/round-63/accept-o.py`,
sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` (verified per case).
Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-CtlODoNothing/` (`clone` + `case-a`..`case-d` + `evidence`).
Nothing was written to the lane repo except this report; no git/jj write was run in it. No installs were made.

## Fixtures (each scored by the same frozen counter, run from its own copy)

| case | fixture | bytes changed | tool sha256 before → after |
|---|---|---|---|
| a | clone unchanged (the round-62 tool as committed at the freeze) | none (`diff -r` empty) | `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803` (unchanged) |
| b | records-only edits: a `## Probe note` row in `SCORECARD.md`, a `## Round 63 — probe` line in `LOG.md`, a `## Probe stub` in `corpus/lessons/round-62.md`; code untouched | 3 record files | `21e2d767…b803` → `21e2d767…b803` (unchanged) |
| c | docstring edited to claim the repair, code untouched (`REPAIR CLAIMED IN THIS DOCSTRING (code unchanged): every redirect target is re-validated …; malformed registry URLs answer ROW <ID> MALFORMED …; a gzip Content-Encoding is decoded …; a 4 MiB read that reaches the cap answers TRUNCATED; --timeout SECONDS is a per-request wall budget.`) | `tools/reopen-row.py` docstring only (diff kept at `evidence/c-tool.diff`) | `21e2d767…b803` → `3726576e7a1a7b9def1c8f61f486cf98596b7308418c2d7296f4fd84c95a8e95` |
| d | `tools/reopen-row.py` chmod 644 | mode only | content `21e2d767…b803` (unchanged); mode `755` → `644` |

Command per case: `cd <case> && timeout 900 python3 -B reports/round-63/accept-o.py; echo exit=$?`

## Full stdout, case a — clone unchanged (round-62 tool)

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=51 ["MALFORMED_PORT:S2384:want=MALFORMED/0:got=[('UNREACHABLE', 9)]", "GZIP_BODY:S2847:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2847:url_want=http://127.0.0.1:33511/dyuvrltjq/rusa:got=['-']", 'MALFORMED_IPV6:S2981:want=MALFORMED/0:got=[]', 'MALFORMED_IPV6:S2981:url_want=-:got=None', 'SHORT:S2126:want=NO_QUOTE/0:got=[]'] summary_ok=False exit=1
ORDER FAIL printed=37 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['TRANSIENT2:live:want=3:hits=0', 'TRUNC_FAR:live:want=1:hits=0', 'CAP_CLASS:live:want=1:hits=0', 'REDIRECT_LOOP:l1:want=3:hits=0', 'REDIRECT_LOOP:l2:want=2:hits=0', 'PLAIN:live:want=1:hits=0', 'ABSENT:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2956', 'REFUSED', 0), ('S2739', 'REFUSED', 0), ('S2789', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2969', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2681', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2681', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2171', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2757', 'ABSENT', 1), ('S2792', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2049', 'ABSENT', 1), ('S2584', 'LOCATED', 1)] want=[('S2049', 'TRUNCATED', 1), ('S2584', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

## Full stdout, case b — records-only edits

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=49 ["MALFORMED_PORT:S2751:want=MALFORMED/0:got=[('UNREACHABLE', 9)]", "REDIRECT_MULTI:S2148:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2148:url_want=http://127.0.0.1:36129/wkylg/usengzkf/rzlt:got=['http://127.0.0.1:36129/tnuq']", "REDIRECT_LOOP:S2177:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "REDIRECT_OK:S2082:want=LOCATED/2:got=[('LOCATED', 1)]", "REDIRECT_OK:S2082:url_want=http://127.0.0.1:36129/yxngw/iiijpjb:got=['http://127.0.0.1:36129/tohst']"] summary_ok=False exit=1
ORDER FAIL printed=40 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=5', 'REDIRECT_LOOP:l2:want=2:hits=4', 'TRANSIENT2:live:want=3:hits=0', 'CAP_FIG:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'GZIP_BODY:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2845', 'REFUSED', 0), ('S2369', 'REFUSED', 0), ('S2271', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2762', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2549', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2549', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2768', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2738', 'ABSENT', 1), ('S2455', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2966', 'ABSENT', 1), ('S2421', 'LOCATED', 1)] want=[('S2966', 'TRUNCATED', 1), ('S2421', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.1s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

## Full stdout, case c — docstring claims the repair, code untouched

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=67 ["REDIRECT_MULTI:S2124:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2124:url_want=http://127.0.0.1:45977/kiqxzf:got=['http://127.0.0.1:45977/dlgd']", "REDIRECT_LOOP:S2829:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "GZIP_BODY:S2499:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2499:url_want=http://127.0.0.1:45977/sqcva/ygxtbund:got=['-']", "REDIRECT_OK:S2265:want=LOCATED/2:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER FAIL printed=31 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=5', 'REDIRECT_LOOP:l2:want=2:hits=4', 'CAP_CLASS_THUMB:live:want=1:hits=0', 'CAP_ATTR_ARIA:live:want=1:hits=0', 'CAP_ATTR_TITLE:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'CAP_ATTR:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2910', 'REFUSED', 0), ('S2460', 'REFUSED', 0), ('S2402', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2062', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2487', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2487', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2182', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2175', 'ABSENT', 1), ('S2906', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2365', 'ABSENT', 1), ('S2952', 'LOCATED', 1)] want=[('S2365', 'TRUNCATED', 1), ('S2952', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.0s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

## Full stdout, case d — chmod 644

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=61 wrong=19 ["REDIRECT_LOOP:S2259:want=UNREACHABLE/5:got=[('UNREACHABLE', 1)]", "GZIP_BODY:S2546:want=LOCATED/1:got=[('ABSENT', 1)]", "GZIP_BODY:S2546:url_want=http://127.0.0.1:34741/vzyqf/ffijcokj:got=['-']", "TRUNC_FAR:S2890:want=TRUNCATED/1:got=[('ABSENT', 1)]", "REDIRECT_MULTI:S2285:want=LOCATED/4:got=[('LOCATED', 1)]", "REDIRECT_MULTI:S2285:url_want=http://127.0.0.1:34741/ufzbqzla:got=['http://127.0.0.1:34741/gozjgvi']"] summary_ok=False exit=1
ORDER FAIL printed=56 expected=61 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['REDIRECT_LOOP:l1:want=3:hits=5', 'REDIRECT_LOOP:l2:want=2:hits=4', 'SCRIPT:live:want=1:hits=0', 'CAP_CLASS_GALLERY:live:want=1:hits=0'] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2998', 'REFUSED', 0), ('S2239', 'REFUSED', 0), ('S2329', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2801', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT FAIL allow_private=[('S2123', 'LOCATED', 1)] hits_src=1 hits_target=1 no_flag=[('S2123', 'REFUSED', 0)] exits=0,1
MALFORMED FAIL exit=1 rows=[('S2568', 'UNREACHABLE', 9)] traceback=True
GZIP FAIL exit=1 rows=[('S2066', 'ABSENT', 1), ('S2460', 'ABSENT', 1)]
TRUNC FAIL exit=1 rows=[('S2492', 'ABSENT', 1), ('S2036', 'LOCATED', 1)] want=[('S2492', 'TRUNCATED', 1), ('S2036', 'LOCATED', 1)]
TIMEOUT FAIL exit=2 rows=[] wall=0.1s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

## Receipts

RECEIPT CtlODoNothing/case-a counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW
RECEIPT CtlODoNothing/case-b counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW
RECEIPT CtlODoNothing/case-c counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW
RECEIPT CtlODoNothing/case-d counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,REDIRECT,MALFORMED,GZIP,TRUNC,TIMEOUT,REVIEW

## Verdicts

CONTROL-NONE-MET: (a) clone unchanged — the round-62 tool fails GEN, ORDER, BOUND, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, REVIEW; it cannot reach PASS.
CONTROL-NONE-MET: (b) records-only edits — same FAIL set, byte-identical tool; records are not read by the counter.
CONTROL-NONE-MET: (c) docstring-only repair claim — same FAIL set; the counter scores bytes, not claims (INDEP is a token grep, not a behaviour test).
CONTROL-NONE-MET: (d) chmod 644 — same FAIL set; mode is not tested, the counter runs the tool via `sys.executable`.

So no do-nothing fixture gets PASS; the frozen counter is not met by work-skipping bytes on claim O.

## Vacuously passing legs (coverage notes, no contract change)

On all four do-nothing fixtures six legs PASS: TOOL, INDEP, EXIT, PRIV, DEFAULT, ERR. Notes:

- TOOL tests existence only (`os.path.isfile`), so case (d)'s missing exec bit is invisible; smallest counter change to catch it: `os.access(src, os.X_OK)` in TOOL.
- INDEP is a substring grep on the tool text; a docstring-only claim (case c) passes it by construction. It does not test independence of behaviour, only the absence of the five tokens.
- EXIT, PRIV and DEFAULT are round-62 behaviours that the round-62 tool already has; DEFAULT ran 150 s, bursts `[3,3,3]`, gaps `[60,60]` on every case — they carry no round-63 evidence.
- ERR passes because the round-62 tool rejects the unknown `--timeout` flag through its own REOPEN_ERROR handler (exit 2, `bad=[]`), so `timeout0`/`timeoutx` do not distinguish "supports --timeout but validates it" from "has no --timeout at all". The TIMEOUT leg (which fails here) is what actually tests the flag; the ERR leg alone would be a cheap-pass surface for a later tool that implements everything else but drops `--timeout`.
- The nine failing legs are the discriminating ones; GEN's per-class `wrong` count varies run to run (19/49/51/67) because the shuffled plan lets the unbalanced-IPv6 row raise `ValueError` mid-run and abort the remaining rows — the verdict is stable FAIL regardless.

## Restoration evidence

Mutated bytes were copied to `evidence/` before restore, then the pristine clone bytes were put back:

| file | pre-restore (mutated) sha256 | post-restore sha256 | pristine `clone` sha256 |
|---|---|---|---|
| case-b/SCORECARD.md | `5ce37a4ac1ce3957f8350353ae509055f5f5ee8a756f5c65af88acd728bcea4e` | `55be954ce7f5fb6886f54ad04c55566c1fa7a2be1cac62c5b0edaa4a8486557a` | `55be954c…577a` |
| case-b/LOG.md | `73bb578a706a928f1419416f119cd3d0f6d71422da6d22a278f3855bfabcd7ab` | `937b5f9b268627ca9098ad89bdafbaf7f67f7bbb7512565b5e974565b2ce7566` | `937b5f9b…7566` |
| case-b/corpus/lessons/round-62.md | `f31fb4e49297bdde91e067f9601fd6cb8b83059734c62f27bce1303ac51ca838` | `cc2f35ac76f387b2ee16ead0aac528d679b484e1a129dcbe07134a9bb50df737` | `cc2f35ac…f737` |
| case-c/tools/reopen-row.py | `3726576e7a1a7b9def1c8f61f486cf98596b7308418c2d7296f4fd84c95a8e95` | `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803` | `21e2d767…b803` |
| case-d/tools/reopen-row.py (mode) | `644` (`21e2d767…b803`) | `755` (`21e2d767…b803`) | `755` |

`diff -r --brief clone case-a|b|c|d` prints nothing after restore. Counter bytes were never edited in any case.
