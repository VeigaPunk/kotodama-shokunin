# ReviewerCounterO2 — ATTACK on reports/round-64/accept-o.py (claim O counter, rev3)

Scope: counter file `reports/round-64/accept-o.py` (untracked in the tree, sha256
`c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18`, 1116 lines) and its
receipts, against `tools/reopen-row.py` (byte-identical to base ff30a20; `git diff ff30a20`
empty; 0 hits for `REOPEN_HOSTS`). Host python: 3.14.8. All live runs executed by me this
session; outputs pasted.

## Verdict shape

The frozen command (`python3 -B reports/round-64/accept-o.py --root .`, no `--only`) is
**not weakened** by any defect I found; every new leg I executed passes and every mutant
fails its pin for the intended mechanism. The defects are (a) `--only` semantics that
violate the counter's own contract, (b) a claim-predicate overreach ("exactly"), (c) one
hermeticity exception plus one environmental assumption, and (d) receipt integrity.

---

## Findings by severity

### HIGH

**H1 — `--only` contract is broken two ways; unknown selectors pass vacuously.**
`verdict = all(legs)` (accept-o.py:1110) with `legs` empty ⇒ PASS/exit 0 for any selector
naming no leg, and core legs are silently absent (not even `SKIP`) whenever `run_core`
is False (:445). Observed:

```
$ python3 -B reports/round-64/accept-o.py --only NOSUCHLEG
TOOL SKIP
EDGE_SCHEMEREL SKIP
EDGE_USERINFO SKIP
EDGE_HTTPS SKIP
EDGE_MALTARG SKIP
EDGE_SLASHLESS SKIP
EDGE_308 SKIP
EDGE_5TH200 SKIP
DRIP SKIP
MUT SKIP
ACCEPT-O-64: PASS
exit=0
```

Docstring promises "legs not run print `<LEG> SKIP`"; the 13 core legs print nothing at
all in this mode (the `run_core:` block is skipped wholesale), and a typo'd selector
(`--only EDGE_308,BOGUS` — verified) yields `ACCEPT-O-64: PASS` exit 0 for a partial run.
The frozen predicate is safe only because the frozen command supplies no `--only`. A
revenger should record: acceptance is parameterized and unvalidated selectors are
fail-open. Pre-data fix (counter-side, with a forcing control): exit 2 when `only`
contains names outside the 23-leg set, and emit `SKIP` for core legs too; control: a
run with `--only NOSUCHLEG` must print exit-2.

**H2 — "each mutant fails exactly its pinned leg" is unverifiable as coded.**
claims.json and the docstring MUT text say each mutant "must FAIL its pinned leg" and
rev-3 says the counter "requires the observed failure-leg set to equal its pins". Code
(accept-o.py:1083-1098) runs each mutant inner counter as
`accept-o.py --root mroot --only <pins>`; every unpinned leg prints `SKIP`, so a mutant
that would fail extra legs is indistinguishable from one failing only its pins.
`pinned_fail` tests `failed == pins ⊆ ran_legs`, never `failed ⊆ pins`. Live example:
m8's inner run (`--only GEN,BOUND`) printed only `GEN FAIL …; BOUND FAIL …` while every
other leg was SKIP — we cannot know m8 wouldn't also fail TIMEOUT/EDGE_5TH200. The claim
statement "each fail exactly their pinned leg" is stronger than the mechanism. This is a
declaration-vs-code drift: either narrow the claim to "fails every pinned leg" or pin
"exactly" by running each mutant with all legs and asserting `failed == pins` (forcing
control: a mutant that also breaks e.g. INDEP must make MUT FAIL). Do **not** weaken a
frozen leg; record and propose.

### MEDIUM

**M1 — `--only` does not skip core fixture work (docstring-vs-code drift, and it costs
minutes).** `--only GEN,BOUND` sets `run_core=True` (:445), so the *entire* core block —
including the ~150 s DEAD/DEFAULT fixture (60 s pass schedule) and the stall server —
executes; only the printing is filtered (`leg()` is called with a pre-evaluated `ok`).
EDGE legs are correctly gated by `need()` and skip their fixtures. Evidence: during my
`--only MUT` run, sibling inner runs of m8 were observed live executing
`DEAD.md --allow-private` tool runs (the DEFAULT fixture) under `--only GEN,BOUND`.
Consequence: each m8 inner run takes ~4-5 min inside the 900 s `run_tool` timeout —
works, but the docstring's "runs just the named legs" is false for the 13 core legs.

**M2 — Hermeticity exceptions.**
- *EDGE_USERINFO same-authority control performs a real DNS lookup of a bogus host.*
  The tool fetches `http://u@127.0.0.1:<fx0-port>/<unrouted>`; on this CPython
  (3.14.8) `urllib.request.Request.host` retains userinfo:
  ```
  >>> urllib.request.Request("http://u@127.0.0.1:1/x").host
  'u@127.0.0.1:1'
  URLError gaierror(-2, 'Name or service not known')   0.01 s
  ```
  So the pinned `UNREACHABLE attempts=6` depends on the OS resolver failing
  `u@127.0.0.1`. That is the documented mechanism (routed doc E3b), but it is not
  hermetic: any environment where that name resolves (wildcard/search-domain DNS, a
  hosts entry) makes the target public or fetchable and the leg fails — or worse,
  connects off-fixture. Also version-sensitive: a urllib that strips userinfo changes
  the fixture's meaning (request reaches the unrouted path → attempts=3, not 6).
- *Proxy env is inherited verbatim.* `run_tool` passes the ambient environment; urllib
  honours `http_proxy`/`https_proxy` (no implicit localhost bypass on this runtime).
  A proxy-configured host could route fixture traffic off-loopback. This host exports
  no `*_proxy` (`env | grep -iE proxy` → nothing), so latent here.
Everything else is hermetic: all servers bind `127.0.0.1` (`ThreadingHTTPServer`),
`dead_port()` is a held listen-less socket (connection-refused, loopback), malformed
URLs (port 99999, unbalanced `[2001:db8::1`, empty host) are rejected by `parse_target`
before any request, and `getaddrinfo` is only ever called on `127.0.0.1` / `u@127.0.0.1`.

**M3 — Receipt integrity: duplicated, truncated, and missing receipts.**
- `telemetry/dry-run-o-baseline-copy.txt` (397 B) is byte-identical to
  `telemetry/dry-run-o.txt` (sha256 `635a16b0…` both, `diff` clean) — including the
  random SIDs S2101/S2377/S2378 — so at most one real run backs both filenames; it is
  not evidence of an independent r63-baseline run.
- Both receipts stop at PRIV (legs 1-7); `final-measures-o.txt` (the rev-0/1 full-run
  receipt) stops at line 22 = DRIP with **no MUT line and no `ACCEPT-O-64:` verdict**.
  The docstring's revision-history claim "the prior full run … showed every mutant
  printing FAIL on its pinned leg" has **no surviving receipt** (rev-1 rev history names
  this file as the evidence; the file never reaches MUT).
- claims.json lands/control name `telemetry/mut-o.txt`, `edge-o.txt`, `control-o.txt` —
  **absent** (`ls telemetry/` shows only census/dry-run/final-measures). The declared
  control ("the round-63 counter has no EDGE_/DRIP leg at all (grep receipt)") has no
  receipt; the fact itself checks out — `grep -nE 'EDGE_|DRIP' reports/round-63/accept-o.py`
  → exit 1, zero matches (r63 legs: TOOL INDEP GEN ORDER BOUND EXIT PRIV DEFAULT ERR
  REDIRECT MALFORMED GZIP TRUNC TIMEOUT REVIEW).
- Truncation pattern (all three receipts die mid-run at a multi-minute leg) suggests
  capture under a short timeout; a revenger should require receipts ending in the
  `ACCEPT-O-64:` line.

### LOW (docstring/code drift; no leg semantics harmed)

- **L1** GEN docstring claims "per-path hit counts" — hit counts are pinned only by
  BOUND. GEN pins verdict, `attempts=`, `url=` per row plus the `REOPEN: k/m` summary.
- **L2** REDIRECT docstring pins `url=-`; the code parses without `with_url` — url
  unpinned. Same for MALFORMED (`url=-` claimed, only `(sid,verdict,attempts)` checked).
- **L3** EDGE_USERINFO docstring pins the same-authority control as `UNREACHABLE
  attempts=6`; code asserts `verdict != "REFUSED" and attempts == 6` (:857) — a strict
  superset (any non-REFUSED verdict passes). EDGE_HTTPS does pin the tuple exactly.
  Live evidence this matters little: control observed `UNREACHABLE 6` on both.
- **L4** DRIP docstring pins `UNREACHABLE attempts=3`/`LOCATED attempts=1`, `wall in
  [8,60]`, and "one 64-byte chunk per 1.0 s"; code checks only the verdict pair (attempts
  columns ignored), `wall < 20`, `drip_hits == 3`, `span >= 7.0`, and `chunk` is the
  whole ~55-byte html() fragment, not 64 B. Direction: docstring overclaims.
- **L5** Silent spec change vs r63: the r63 `REVIEW` leg (gating on
  `.ufo/waves/round-63/w1/RevTool{A,B,C}.md` + `reports/round-63/telemetry/rev-hold-lift.md`
  verdict tokens) is dropped in r64. Defensible — those are round-63-only artifacts —
  but "extend the round-63 counter" omits it and the docstring never mentions the drop.
- **L6** The counter is untracked (`??` in `jj`/git status; `git log` shows no commit).
  The docstring names a rev-0 sha256 (`bb0c74a4…`) that cannot be verified against any
  committed blob; the claim's surface is a working-tree file — a revenger should pin by
  hash, not VCS identity. (Note `accept-c.py`/`accept-ca.py` also carry uncommitted `M`
  edits.)

---

## What verified clean (checked, no defect)

- **(1) r63 counter had no EDGE_/DRIP legs — CONFIRMED.** `grep -nE 'EDGE_|DRIP'
  reports/round-63/accept-o.py` → exit 1 (zero matches, code read at lines 381-766).
  All seven r64 EDGE legs correspond 1:1 to the seven CONTROL-MET items in
  `.ufo/waves/round-63/w1/CtlORedirectEdge.md` §4, each implementing that doc's spelled
  "smallest counter change" (scheme-rel, userinfo cross+same, https cross+same,
  malformed target, slashless, 308, 5th-200). DRIP implements rev-hold-lift MEDIUM-1
  (`reports/round-63/telemetry/rev-hold-lift.md`: `read()`→`read1`), and the r64 fixture
  is strictly stronger than the r63 probe (no Content-Length, connection-close end).
- **(2) Docstring legs exist and print — CONFIRMED.** AST scan: all 23 declared legs
  (docstring list == claims.json `legs` list, same order) have `leg()` calls; none
  extra. In a full (no-`--only`) run every leg reaches `leg()` exactly once and prints.
- **(3) MUT pinning — CONFIRMED, all 10.** Every patch needle occurs exactly once in the
  committed tool (scripted `str.count` → 1 each) and each pinned leg is the one the
  patch targets. Live run, full output:
  ```
  $ python3 -B reports/round-64/accept-o.py --only MUT
  MUT PASS bad=[] mutants=10 kill_evidence=[
    "m1->EDGE_SCHEMEREL FAIL rows=[('S2113','LOCATED',2)] tgt_hits=1 src_hits=1 tb=False",
    "m10->EDGE_USERINFO FAIL cross=[('S2265','UNREACHABLE',6)] tgt_hits=0 same_auth=[('S2282','UNREACHABLE',6)] ok=True",
    "m2->EDGE_USERINFO FAIL cross=[('S2630','REFUSED',1)] tgt_hits=0 same_auth=[('S2045','REFUSED',1)] ok=False",
    "m3->EDGE_HTTPS FAIL cross=[('S2485','UNREACHABLE',6)] tgt_hits=0 same_auth=[('S2331','UNREACHABLE',6)] ok=True",
    "m9->EDGE_MALTARG FAIL rows=[] exit=1 tb=True",
    "m5->EDGE_SLASHLESS FAIL rows=[('S2423','UNREACHABLE',2)] dir_hits=0 root_hits=1 exit=1",
    "m6->EDGE_308 FAIL rows=[('S2011','UNREACHABLE',1)] tgt_hits=0 exit=1",
    "m7->EDGE_5TH200 FAIL rows=[('S2752','UNREACHABLE',5,'-')] final=… exit=1",
    "m8->GEN FAIL … REDIRECT_LOOP want UNREACHABLE/5 got 6 …; BOUND FAIL … l2 want 2 hits 3",
    "mread->DRIP FAIL rows=[(UNREACHABLE,3),(LOCATED,1)] wall=90.1s drip_hits=3 span=60.0s"]
  ACCEPT-O-64: PASS
  ```
  Each failure mode is the intended one: m1 follows the `//` target (tgt hit, LOCATED);
  m10's cross verdict flips REFUSED→UNREACHABLE (still fails, though *not* because the
  target was contacted — the bogus-name fetch dies in DNS; worth recording: m10/m3 fail
  via the verdict check, never reaching the fixture page); m2 over-refuses the same-auth
  control (`ok=False`, exactly the doc's M2 shape); m9 tracebacks (rows empty, tb=True);
  m5 hits `/sub/x` (root_hits=1, dir_hits=0); m6 treats 308 as final (UNREACHABLE);
  m7 kills the 5th-200 chain (UNREACHABLE attempts=5); m8 breaks both pinned legs with
  the predicted counts (attempts=6, l2=3); mread lets the drip run 90 s (wall≥20, span 60).
- **(4) EDGE + DRIP legs pass live** (`--only EDGE_…` run, 1.25 s; DRIP 12.6 s):
  ```
  EDGE_SCHEMEREL PASS rows=[('S2725','REFUSED',1)] tgt_hits=0 src_hits=1 tb=False
  EDGE_USERINFO  PASS cross=[('S2639','REFUSED',1)] tgt_hits=0 same_auth=[('S2151','UNREACHABLE',6)] ok=True
  EDGE_HTTPS     PASS cross=[('S2734','REFUSED',1)] tgt_hits=0 same_auth=[('S2113','UNREACHABLE',6)] ok=True
  EDGE_MALTARG   PASS rows=[('S2082','UNREACHABLE',1)] exit=1 tb=False
  EDGE_SLASHLESS PASS rows=[('S2999','LOCATED',2)] dir_hits=1 root_hits=0 exit=0
  EDGE_308       PASS rows=[('S2962','LOCATED',2)] tgt_hits=1 exit=0
  EDGE_5TH200    PASS rows=[('S2544','LOCATED',5,'http://127.0.0.1:46645/cfin-fybrsmq')] … exit=0
  DRIP           PASS rows=[('S2896','UNREACHABLE',3),('S2201','LOCATED',1)] wall=12.1s drip_hits=3 span=8.0s
  ```
  These are the rev-3-changed legs (EDGE_USERINFO pin moved from prose-3 to observed-6;
  MUT matcher rewritten) — both verified working on the actual rev-3 bytes.
- **Needle/target coherence:** m5 needle is the urljoin site (tool:604), m6 the
  REDIRECT_CODES tuple (:144), m7 the follow loop head (:596-600), m8
  `MAX_REQUESTS_PER_CHAIN = 5` (:141), m9 the try/except BadUrl wrap (:605-609), m2 the
  parse_target pair (:606-607), mread the read1 line (:557). All match the follow()
  semantics read in the tool; `counter[0]` counts requests, so `attempts=6` = 3 tries ×
  (source redirect + target fetch) — matches routed doc E3b/E4b and my live runs.

## Residual risk

- The frozen predicate has **no complete rev-3 receipt**: no artifact shows all 23 legs
  + MUT + verdict for the current bytes. Live coverage this session: EDGE×7, DRIP, MUT
  (10/10) PASS on rev-3; legs 1-13 unchanged from rev-0 bytes which passed in the
  truncated rev-0 receipt. A full no-`--only` run (≈15-20 min: GEN ~4 min, DEFAULT ~2.5
  min, MUT ~8-9 min incl. the m8 slow inner run) was **not** executed — remaining risk
  is confined to leg interactions under one process (shared `fx` hit accounting across
  GEN→EDGE→DRIP is per-path and additive, so expected-clean; `used` sid set shared —
  collision only if `fresh_id` repeats, guarded).
- Timing margins are thin in places: DRIP span needs ≥7.0 s (observed 8.0), TIMEOUT span
  ≥3.0 s (observed 4.0), DEFAULT burst spacing assumes `min(gap,5)`=5 s intra-pass sleeps
  and 55-75 s inter-burst gaps — all load-sensitive on a stormed host.
- `EDGE_USERINFO` control's `UNREACHABLE 6` is environment-dependent (M2); a resolver
  that resolves `u@127.0.0.1` flips the leg without any tool change — latent nondeterminism
  in the frozen predicate.
- Mutants m10/m3 fail via verdict-mismatch without contacting the edge target, so they
  wouldn't detect a variant that skips re-validation *and* resolves the userinfo/TLS —
  the kill is real but shallower than the prose implies.

## Unstated assumptions a revenger should record

1. `--only` selectors are unvalidated (fail-open, H1) and suppress no core work (M1).
2. `attempts=` counts HTTP requests including redirect hops, not tool tries — the 6 in
   E3b/E4b pins tool internals, not a spec constant.
3. EDGE/DRIP legs run only with `--allow-private`; EDGE fixtures share the GEN fixture's
   server (`fx0`) but count hits on fresh paths — ordering of legs matters implicitly.
4. `os.path.abspath(__file__)` is the counter's self-identity for mutant inner runs;
   invocation via a different path still resolves to the same file (cwd-dependent).
5. Receipts are expected to be truncated by their capture harness; no receipt currently
   carries a verdict line, so "dry-run PASS" claims rest on leg lines only.
6. No proxy env is exported on the measurement host; if it were, urllib would obey it.
7. `time.monotonic` clock skew is assumed absent (counter and fixture share the clock);
   `dead_port()` sockets are held only by `RESERVED` lifetime.
8. The DEFAULT leg's `4 <= gap <= 10` burst-internal spacing silently pins
   `min(gap, 5) = 5 s` retry sleeps — undocumented in the leg text.

## Tooling record

No installs. Used: repo python3 3.14.8, git (read-only diff/log/status/hash-object),
grep/diff/wc/sha256sum. Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewerCounterO2/mut-run.txt`
(MUT live output). No repo files modified; no commits.
