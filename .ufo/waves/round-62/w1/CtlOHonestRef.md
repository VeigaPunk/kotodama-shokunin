# CtlOHonestRef — Claim O (ACCEPT-O-62) honest positive calibration

## Scope and axes

- Axis: **operability** (claim O: a lane tool `tools/reopen-row.py` that re-opens SOURCES rows with a bounded retry, an archived-copy fallback and a body-versus-caption verdict).
- Seat role: **honest positive calibration** — write an *independent* implementation of the full tool contract stated in the frozen counter's docstring, score it three times, and expect PASS 3/3.
- Frozen clone revision: `f0173481047a93c46798f90b68d71d4f169d2642`.
- Frozen counter: `reports/round-62/accept-o.py`, SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` — verified identical before and after every run below.
- Scratch root (all my artefacts): `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/`.
- Implementation lives **only** in my scratch clone (`.../CtlOHonestRef/clone/tools/reopen-row.py`); **nothing** was written into the lane tree except this report. No lane registry, no lane `tools/`, no counter, no counter PROBE copy.
- No installs or updates were performed (no tool was needed; stdlib only). No git/jj write command was run in either repo.
- No labrat probe was dispatched (no spawn key).

## Files changed

| Path (absolute) | Change | SHA-256 |
|---|---|---|
| `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/clone/tools/reopen-row.py` | **new** — the honest implementation (scratch clone only) | `03aa4c4c57d3c6d31f783bb27bc60e67e5978b9cc472837533e286ed5c3c59b7` |
| `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-alwayslocated/tools/reopen-row.py` | **new** — control probe | `c4780400865e406f464a2d1b32e535c0d5976a825450e77c4812067bfbbc61ee` |
| `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-nocaption/tools/reopen-row.py` | **new** — control probe (mutated copy) | see diff section |
| `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-noretry/tools/reopen-row.py` | **new** — control probe (mutated copy) | see diff section |
| `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-noarchive/tools/reopen-row.py` | **new** — control probe (mutated copy) | see diff section |
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-62/w1/CtlOHonestRef.md` | **new** — this report (the one lane write) | — |

Clone provenance (sandboxed, per the lane's clone rule):
`git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin .../clone && git -C .../clone checkout -q f0173481047a93c46798f90b68d71d4f169d2642` → `git -C .../clone rev-parse HEAD` = `f0173481047a93c46798f90b68d71d4f169d2642`.

## Behaviour of the honest implementation

Stdlib only (`argparse`, `html.parser`, `urllib.request`, `ipaddress`, `socket`, `re`, `unicodedata`, `time`).

- **Registry row** — a `| S### |` line; `line.split("|")` cell 2 = source cell, cell 6 = anchor cell (contract numbering, i.e. `cells[2]`/`cells[6]` of the raw split, matching the counter's own registry layout). The row's quote is the first double-quoted span (straight or curly) of the anchor cell.
- **URLs** — every `http(s)` URL of the source cell in order; trailing `.,;:'` and an unbalanced `)` are trimmed. A `; capture <url>` segment therefore yields the live URL first and the archived copy second, which is what drives the fallback.
- **Normalisation** — NFKC → casefold → every run of non-word characters or `_` → one space; the quote's normalised words must appear as a contiguous whole-word run in the normalised text.
- **Body/caption split** (`html.parser`) — BODY = text nodes outside `script`, `style`, `noscript`, `template`, `figcaption` and any element whose `class`/`id` contains `caption` (descendants included). CAPTION = text inside `figcaption` or a caption class/id element, plus the values of `alt`, `title`, `aria-label`, `content` and every `data-*` attribute. Script/style text is neither. A non-HTML body (`text/plain`, JSON) is BODY text as a whole.
- **Fetch** — GET, 30 s timeout, proxies disabled. Transient = HTTP 429, any 5xx, timeout, connection error; retried up to 3 attempts per URL per pass, waiting `min(gap, 5)` s between attempts. Any other HTTP error ends that URL for the pass after one attempt.
- **Private refusal** — without `--allow-private`, a URL whose host is or resolves to loopback/private/link-local/reserved/unspecified, or does not resolve, is refused **without a request** (hence `attempts=0`).
- **Passes** — a pass walks the row's URLs in order and stops at the first BODY match. Pass verdict: LOCATED / CAPTION_ONLY / ABSENT (some URL answered 2xx) / REFUSED (every URL refused) / UNREACHABLE. Another pass runs, after `gap` seconds, only when the pass was not LOCATED and some URL ended on a transient result, up to `--passes` (default 3, `--gap` default 60). The row verdict is the best pass verdict (LOCATED > CAPTION_ONLY > ABSENT > UNREACHABLE > REFUSED).
- **NO_ROW / NO_QUOTE** — no registry row; no quote, a quote under 8 normalised words, or no URL. No request is made in either case.
- **Output** — one line per ID in argument order: `ROW <ID> <VERDICT> attempts=<n> url=<url or ->`, then `REOPEN: <k>/<m> located`. Exit 0 when every row is LOCATED, 1 otherwise, 2 on an input error (no ID, unreadable/invalid-UTF-8 registry, `--passes` not an integer ≥ 1, `--gap` not a number ≥ 0) with a `REOPEN_ERROR` line and no traceback.
- **Independence** — the tool's text names none of `reports/`, `accept-o`, `round-62` (INDEP leg PASS); the counter runs a copy of the tool from a fresh temp directory, so the tool must not depend on its own location.

## Control receipts

Every run below used the frozen counter from my clone at `f0173481047a93c46798f90b68d71d4f169d2642`; the counter file was never edited (no PROBE copy of the counter was needed — I mutated *the tool*, never the counter).

```
RECEIPT CtlOHonestRef/score-1 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlOHonestRef/score-2 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlOHonestRef/score-3 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlOHonestRef/final-verify counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlOHonestRef/probe-alwayslocated counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,EXIT,PRIV,DEFAULT,ERR
RECEIPT CtlOHonestRef/probe-nocaption counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN
RECEIPT CtlOHonestRef/probe-noretry counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT
RECEIPT CtlOHonestRef/probe-noarchive counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
```

### Verdict lines (per item)

```
NONE-MET alwayslocated — no fixture obtained frozen PASS; the existing GEN/BOUND legs already stop the constant answer (wrong verdicts, wrong attempt counts, server sees 0 requests). Smallest counter change that would stop it: none needed.
NONE-MET nocaption — no fixture obtained frozen PASS; the existing GEN leg already stops a tool that folds caption text into the body (CAP_FIG/CAP_CLASS/CAP_ATTR/ARCHIVE_CAPTION expected CAPTION_ONLY, got LOCATED). Smallest counter change that would stop it: none needed.
NONE-MET noretry — no fixture obtained frozen PASS; the existing GEN/BOUND/DEFAULT legs already stop a tool that does not retry (TRANSIENT_PASS/DEAD_THEN_BODY2 wrong attempt counts, server request counts wrong, DEFAULT sees 3 requests instead of 9). Smallest counter change that would stop it: none needed.
NONE-MET noarchive — no fixture obtained frozen PASS; the existing GEN/BOUND legs already stop a tool that ignores the archived copy (DEAD_ARCHIVE/ARCHIVE_CAPTION/DEAD_THEN_BODY2 wrong verdicts, archive path never fetched). Smallest counter change that would stop it: none needed.
```

**Overall control result for claim O: NONE-MET on all four controls** — no cheap fixture that skips the claimed work passes the frozen counter. The frozen predicate is *satisfiable* (my honest implementation passes it 4/4 runs) and *not trivially satisfiable* (four work-skipping fixtures all fail).

## Exact retained evidence

### Score run 1 (`receipts/score-1.txt`) — full stdout, unedited

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5568', 'REFUSED', 0), ('S8355', 'REFUSED', 0), ('S2017', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9651', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

### Score run 2 (`receipts/score-2.txt`) — full stdout, unedited

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4368', 'REFUSED', 0), ('S7266', 'REFUSED', 0), ('S9781', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2051', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

### Score run 3 (`receipts/score-3.txt`) — full stdout, unedited

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1812', 'REFUSED', 0), ('S9295', 'REFUSED', 0), ('S7637', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2110', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

### Post-edit integrity re-run (`receipts/final-verify.txt`) — tool hash identical before and after

```
03aa4c4c57d3c6d31f783bb27bc60e67e5978b9cc472837533e286ed5c3c59b7  clone/tools/reopen-row.py   (before)
03aa4c4c57d3c6d31f783bb27bc60e67e5978b9cc472837533e286ed5c3c59b7  clone/tools/reopen-row.py   (after)
```

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6352', 'REFUSED', 0), ('S2274', 'REFUSED', 0), ('S8211', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3038', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

### Control probe `alwayslocated` — full stdout, unedited

Fixture path: `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-alwayslocated/tools/reopen-row.py` (sha256 `c4780400865e406f464a2d1b32e535c0d5976a825450e77c4812067bfbbc61ee`). It prints `ROW <id> LOCATED attempts=1 url=-` for every ID and makes **zero network requests**.

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=31 ["NOQUOTE:S9046:want=NO_QUOTE/0:got=[('LOCATED', 1)]", "SCRIPT:S5640:want=ABSENT/1:got=[('LOCATED', 1)]", "CAP_ATTR:S4764:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S4198:want=LOCATED/2:got=[('LOCATED', 1)]", "CAP_CLASS:S4352:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "GONE:S7031:want=UNREACHABLE/1:got=[('LOCATED', 1)]"] summary_ok=False exit=0
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['SCRIPT:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'CAP_CLASS:live:want=1:hits=0', 'GONE:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[('S9107', 'LOCATED', 1), ('S4688', 'LOCATED', 1), ('S8094', 'LOCATED', 1)]
DEFAULT FAIL rows=[('S6680', 'LOCATED', 1)] wall=0s hits=0 exit=0
ERR FAIL bad=['missing:exit=0', 'badutf8:exit=0', 'passes0:exit=0', 'gapx:exit=0']
ACCEPT-O-62: FAIL
exit=1
```

### Control probe `nocaption` — full stdout, unedited

Fixture path: `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-nocaption/tools/reopen-row.py`. Mutation: caption text is folded into the body (the body/caption distinction is destroyed).

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=8 ["ARCHIVE_CAPTION:S7665:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "CAP_CLASS:S5000:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S9117:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "CAP_ATTR:S7435:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_ATTR:S8655:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_FIG:S8915:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2474', 'REFUSED', 0), ('S8003', 'REFUSED', 0), ('S6935', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7448', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

### Control probe `noretry` — full stdout, unedited

Fixture path: `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-noretry/tools/reopen-row.py`. Mutation: one attempt per URL per pass (no retry).

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=7 ["TRANSIENT_PASS:S9223:want=LOCATED/4:got=[('UNREACHABLE', 3)]", "DEAD_THEN_BODY2:S2697:want=LOCATED/4:got=[('LOCATED', 2)]", "DEAD:S8414:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]", "DEAD_THEN_BODY2:S2524:want=LOCATED/4:got=[('LOCATED', 2)]", "DEAD:S9135:want=UNREACHABLE/9:got=[('UNREACHABLE', 3)]", "TRANSIENT_PASS:S3510:want=LOCATED/4:got=[('UNREACHABLE', 3)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['TRANSIENT_PASS:live:want=4:hits=3', 'DEAD_THEN_BODY2:live:want=3:hits=1', 'DEAD:live:want=9:hits=3', 'DEAD_THEN_BODY2:live:want=3:hits=1', 'DEAD:live:want=9:hits=3', 'TRANSIENT_PASS:live:want=4:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1925', 'REFUSED', 0), ('S4160', 'REFUSED', 0), ('S9074', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S6381', 'UNREACHABLE', 3)] wall=135s hits=3 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

### Control probe `noarchive` — full stdout, unedited

Fixture path: `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/probe-noarchive/tools/reopen-row.py`. Mutation: only the first URL of the source cell is used (no archived-copy fallback).

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["ARCHIVE_CAPTION:S9421:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S1385:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S9264:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S5086:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S6867:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S4541:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9008', 'REFUSED', 0), ('S5995', 'REFUSED', 0), ('S1847', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1831', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

### Probe diffs (tool mutated, counter untouched)

```diff
--- clone/tools/reopen-row.py            (honest reference)
+++ probe-nocaption/tools/reopen-row.py
@@ -217,7 +219,7 @@
         splitter.close()
     except Exception:
         pass
-    return splitter.body_text(), splitter.caption_text()
+    return splitter.body_text() + " " + splitter.caption_text(), ""
```

```diff
--- clone/tools/reopen-row.py            (honest reference)
+++ probe-noretry/tools/reopen-row.py
@@ -297,7 +299,7 @@
             outcome = "refused"
         else:
             outcome = "transient"
-            for attempt in range(3):
+            for attempt in range(1):
                 attempts += 1
                 kind, payload, extra = fetch_once(url)
```

```diff
--- clone/tools/reopen-row.py            (honest reference)
+++ probe-noarchive/tools/reopen-row.py
@@ -90,7 +92,7 @@
         url = trim_url(raw)
         if url and url not in urls:
             urls.append(url)
-    return urls
+    return urls[:1]
```

Each probe also carries a two-line `# CONTROL PROBE (CtlOHonestRef) -- mutated copy of the honest reference` header. The counter file was **not** copied or edited in any form.

## Why each control fails, mapped to the contract sentence it violates

- **alwayslocated** — violates "Pass verdict: LOCATED (a BODY match), else CAPTION_ONLY … else ABSENT (some URL answered 2xx), else REFUSED … else UNREACHABLE" and "n = HTTP requests and connection attempts made for that row over all passes" (it reports `attempts=1` and makes no request). GEN and BOUND catch it; DEFAULT additionally fails because the DEAD row must show nine real requests and 100–600 s of wall time.
- **nocaption** — violates "HTML is split into BODY text … and CAPTION text". With caption text folded into the body, every caption class is reported LOCATED instead of CAPTION_ONLY. GEN catches it; BOUND/EXIT/PRIV/DEFAULT/ERR still pass, so GEN is the single detector leg here.
- **noretry** — violates "it is retried up to 3 attempts per URL per pass, waiting min(gap, 5) s between attempts". Without the retry the transient classes get the wrong attempt counts and the server sees the wrong request counts. GEN, BOUND and DEFAULT catch it.
- **noarchive** — violates "A pass tries the row's URLs in order" together with the archived-copy fallback (the `; capture <url>` URL is a second URL of the source cell and must be tried). Without it the archive classes are unreachable and the archive path is never requested. GEN and BOUND catch it.

## Risks, blockers, caveats

- **The honest tool is not in the lane.** It exists only at `/fast/scratch/hyaku/kotodama-r62/CtlOHonestRef/clone/tools/reopen-row.py`. A build seat must still produce the lane's `tools/reopen-row.py`; my implementation was deliberately **not** shared with any build seat. (The scratch path and its hash were given to `KotodamaR62.CtlOKeyed` and `KotodamaR62.MutCounterO`, both control/mutation seats that asked for a pristine baseline; `CtlOKeyed` confirmed afterwards that no reference bytes were copied or used, and `MutCounterO` confirmed it completed its probe with its own isolated control. No build seat received the code.)
- **The frozen predicate is satisfiable but only barely in the DEFAULT leg.** DEFAULT demands 100–600 s of wall time for one DEAD row; my implementation lands at 150 s because the default `--gap 60` is waited twice between three passes. A tool that retries without waiting, or that collapses the three passes into one, fails DEFAULT — the leg is load-bearing, not decorative.
- **Legs that share one fault.** ORDER compares the printed ID sequence to the argument order; PRIV compares an ordered tuple of `(id, REFUSED, 0)`. A tool that reverses ROW emission fails both. `MutCounterO` independently observed the same coupling from its own control (disabling ORDER alone left a passing variant, because a full reversal also breaks PRIV).
- **The counter's fixture is local-only.** Every run used the counter's own in-process `ThreadingHTTPServer` on 127.0.0.1 with `--allow-private`; no live page was fetched and no external network was touched. Per the counter's own docstring, live-page behaviour (the S665 caption, the S671 Wayback case) is a wave-2 review item and never a leg — my PASS therefore says nothing about live-page behaviour.
- **No counter copy was made.** Because the mutation was always applied to the *tool*, the "clearly labelled PROBE copy" rule did not trigger; the frozen counter's SHA-256 was verified identical (`bfd17a30…`) before and after every run.
- **No installs, no service restarts, no pacman transaction.** No tooling was missing, so nothing was installed or updated.
- **Process hygiene** — every command was capped with `timeout` (≤ 900 s); all background jobs (the three parallel score runs and the four parallel probe runs) completed and were reaped before this report was written. No process tree of mine is left running.
- **Unchanged, intentionally:** the lane's `reports/round-62/accept-o.py`, `corpus/SOURCES.md`, and the whole lane tree apart from this one report file.

## One-line summary

Claim O's frozen predicate is satisfiable and not trivially satisfiable: an independent stdlib implementation of the full `accept-o.py` contract scores **ACCEPT-O-62: PASS with all nine legs PASS in 4/4 independent runs** (3 scored + 1 post-edit integrity re-run), while **all four work-skipping control fixtures FAIL** the frozen counter — **NONE-MET** on every control, no counter change needed.
