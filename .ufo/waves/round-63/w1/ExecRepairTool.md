# ExecRepairTool — round 63 wave 1, claim O build seat (repaired `tools/reopen-row.py`)

Seat: `kotodama-r63-w1-ExecRepairTool` (executor, leaf; BUILD side of claim O, "build + attack together").
Date: 2026-10-23. Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; freeze `80d53ffde7788299b69dbb0bd0436b2b7ddddb95`, round base `65b393ef3a4d82bd693cc21b7f96a1231417d522`.
Scope: write the repaired tool only; the L1 (`KotodamaR63`) copies it into the lane. Nothing else in the lane was touched by this seat.

## 1. Artifact

| item | value |
|---|---|
| candidate path (only file this seat produced) | `/fast/scratch/hyaku/kotodama-r63/ExecRepairTool/reopen-row.py` |
| sha256 | `0d965ccb839c5676ca1694e4fe1dd080a9a0adec0878241e62298398a62e32d5` |
| size / lines / mode | 46494 bytes / 1217 lines / 755 (executable) |
| base it was started from | `git show 65b393e:tools/reopen-row.py` (sha256 `21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803`, the round-62 held blob) |
| dependencies | Python 3 standard library only (added `http.client`, `zlib`; `gzip` imported locally inside the selftest) |
| scratch clone | `/fast/scratch/hyaku/kotodama-r63/ExecRepairTool/clone` (git clone of the lane, checked out at `80d53ff`) |

The lane's `tools/reopen-row.py` is still the held round-62 blob — this seat did not modify it.

## 2. Contract implemented (round-62 closure routed defects 1 and 2, plus the residual gaps)

1. **Redirect re-validation (gating, HIGH).** The fetching library never follows a redirect: a `_NoRedirect` handler makes `HTTPRedirectHandler.redirect_request` return `None`, a 3xx comes back as a `Response` carrying `Location`, and `follow()` resolves every hop with `urljoin` against the URL that answered. Each request of the chain counts as one attempt; a chain makes at most **5** requests and a redirect arriving on the 5th answer ends that URL for the pass (`FatalFetch`). A hop whose authority (lowercased host, effective port) differs from the answering URL's must pass the private-host refusal **even under `--allow-private`** (`Fetcher.private_host()` has no `allow_private` exemption; `Fetcher.refused()` keeps the exemption for listed URLs only); without `--allow-private` every hop must pass it. A refused hop ends that URL for the pass; a row whose URLs were all refused (pre-refusal or hop refusal) prints `REFUSED` with the requests actually made counted.
2. **Malformed registry URLs.** `parse_target()` classifies an unparseable port (`parts.port` ValueError), an unbalanced bracketed IPv6 literal (`urlsplit` ValueError), an empty host, and a non-http(s) scheme as malformed *before* any request: `ROW <ID> MALFORMED attempts=0 url=-`, no traceback, exit 1. `MALFORMED` ranks below `REFUSED` (`VERDICT_RANK` gained `MALFORMED: 0`, `TRUNCATED: 3`).
3. **gzip.** A response with `Content-Encoding: gzip` is decompressed with `zlib.decompressobj(16 + MAX_WBITS)`, bounded to 64 MiB of expansion, before the charset decode and the match; an over-long expansion is treated as a cut body.
4. **Truncation.** At most `MAX_BODY_BYTES + 1` bytes are read. A body that fills the cap without EOF is cut: the quote absent from the bytes read answers `TRUNCATED` (rank equal to `ABSENT`, printed `url=-`); the quote inside the read bytes still answers `LOCATED` / `CAPTION_ONLY`.
5. **`--timeout SECONDS`** (default 30, number > 0; invalid or non-positive → `REOPEN_ERROR`, exit 2) is a **per-request wall budget** over connect + head + body against a `time.monotonic()` deadline; the socket's own timeout is re-bound to the remaining budget before the body read; expiry is a transient result and is retried per the schedule.
6. **Everything else byte-compatible:** same verdict set plus `MALFORMED`/`TRUNCATED`, same retry/pass schedule (3 attempts per URL per pass, `min(gap, 5)` s between retries, `--passes`/`--gap` semantics), same caption/body split, same ordering, same output shape `ROW <ID> <VERDICT> attempts=<n> url=<u>`, same summary `REOPEN: <k>/<m> located`, same exit codes (0 all located, 1 otherwise, 2 on input error).

The module docstring states this contract in the tool's own words; the tool's text names none of `reports/`, `accept-o`, `round-63`, `Fixture`, `REOPEN_HOSTS` (INDEP leg).

## 3. Built-in selftest (`--selftest`) — full output, exit 0

```
$ python3 -B reopen-row.py --selftest ; echo exit=$?
-- selftest: verdicts --
ok   verdict S1: ('LOCATED', 'attempts=1')
ok   verdict S10: ('LOCATED', 'attempts=2')
ok   verdict S11: ('UNREACHABLE', 'attempts=1')
ok   verdict S12: ('UNREACHABLE', 'attempts=9')
ok   verdict S13: ('NO_QUOTE', 'attempts=0')
ok   verdict S14: ('NO_QUOTE', 'attempts=0')
ok   verdict S15: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S16: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S17: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S18: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S2: ('LOCATED', 'attempts=1')
ok   verdict S3: ('LOCATED', 'attempts=1')
ok   verdict S4: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S5: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S6: ('CAPTION_ONLY', 'attempts=1')
ok   verdict S7: ('ABSENT', 'attempts=1')
ok   verdict S8: ('ABSENT', 'attempts=1')
ok   verdict S9: ('LOCATED', 'attempts=3')
ok   summary: True
ok   exit code: 1
ok   no row: ('NO_ROW', 'attempts=0')
-- selftest: retry bound --
ok   transient hits: 3
ok   transient verdict: ('LOCATED', 'attempts=3')
-- selftest: private refusal --
ok   refused verdict: True
ok   refused hits: 0
ok   refused exit: 1
-- selftest: bad inputs --
REOPEN_ERROR: no row ids given
ok   no ids exit: 2
REOPEN_ERROR: cannot read registry /tmp/reopen-row-selftest-ou_cmj4w/nope.md: [Errno 2] No such file or directory: '/tmp/reopen-row-selftest-ou_cmj4w/nope.md'
ok   missing registry exit: 2
REOPEN_ERROR: --passes must be an integer >= 1
ok   passes zero exit: 2
REOPEN_ERROR: --gap must be a number >= 0
ok   gap not a number exit: 2
REOPEN_ERROR: --timeout must be a number > 0
ok   timeout zero exit: 2
REOPEN_ERROR: --timeout must be a number > 0
ok   timeout not a number exit: 2
REOPEN_ERROR: unknown option --nope
ok   unknown option exit: 2
REOPEN_ERROR: registry /tmp/reopen-row-selftest-ou_cmj4w/BAD.md is not valid UTF-8: 'utf-8' codec can't decode byte 0xff in position 7: invalid start byte
ok   bad utf-8 exit: 2
-- selftest: redirect chain --
ok   redirect verdict: ('LOCATED', 'attempts=2')
ok   redirect hits: (1, 1)
ok   redirect url: 'http://127.0.0.1:43825/redirtarget'
-- selftest: cross-authority redirect refused --
ok   hop refused: ('REFUSED', 'attempts=1')
ok   hop source hit: 1
ok   hop target untouched: 0
-- selftest: malformed urls --
ok   malformed port: ('MALFORMED', 'attempts=0')
ok   malformed ipv6: ('MALFORMED', 'attempts=0')
ok   malformed empty host: ('MALFORMED', 'attempts=0')
ok   malformed exit: 1
-- selftest: gzip --
ok   gzip verdict: ('LOCATED', 'attempts=1')
-- selftest: truncation --
ok   truncated far: ('TRUNCATED', 'attempts=1')
ok   truncated near: ('LOCATED', 'attempts=1')
ok   truncated url: '-'
-- selftest: request budget --
ok   stall verdict: ('UNREACHABLE', 'attempts=3')
-- selftest: 49 checks, 0 failures --
exit=0
```

(The `REOPEN_ERROR:` lines are the expected stderr of the bad-input cases; the selftest exits 0 with 49 checks and 0 failures. The round-62 selftest had 32 checks; the 17 new ones are the per-defect cases above.)

## 4. Manual run against a scripted local HTTP server (`manual_check.py`, 30-line stdlib server)

Two servers: the source answers `/hop` with a 302 to the *other* port (different authority) and `/gz` with a gzip-encoded body; the target serves `/secret`. The registry holds one hop row, one gzip row and one malformed-port row.

```
$ python3 -B manual_check.py
--- stdout ---
ROW S1 REFUSED attempts=1 url=-
ROW S2 LOCATED attempts=1 url=http://127.0.0.1:38201/gz
ROW S3 MALFORMED attempts=0 url=-
REOPEN: 1/3 located
--- stderr ---
--- exit=1 ---
source hits: {'/hop': 1, '/gz': 1}
target hits: None
```

Cross-port 302 → `REFUSED`, and the target server was never touched (`target hits: None` = no request). gzip body → `LOCATED`. Bad-port URL → `MALFORMED attempts=0`, no traceback, exit 1.

## 5. Counter receipts (frozen counters, my clone, no live fetch, no lane write)

The candidate was scored with the counter **as it stands in the lane**, from the clone at `80d53ff` with the candidate copied over `tools/reopen-row.py`. Two runs are reported because the lane's counter was revised (pre-data) between them; both are full stdout, verbatim.

### 5.1 Counter revision 0 (freeze `80d53ff`), sha256 `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`

```
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2587', 'REFUSED', 0), ('S2630', 'REFUSED', 0), ('S2234', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2369', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2769', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2769', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2130', 'MALFORMED', 0), ('S2414', 'MALFORMED', 0), ('S2402', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2964', 'LOCATED', 1), ('S2013', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2979', 'TRUNCATED', 1), ('S2359', 'LOCATED', 1)] want=[('S2979', 'TRUNCATED', 1), ('S2359', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2431', 'UNREACHABLE', 3)] wall=12.1s
REVIEW FAIL reports=4 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] clean=0
ACCEPT-O-63: FAIL
exit=1
```

### 5.2 Counter revision 4 (lane tip `e42538a`), sha256 `23355bac77f5bc3ed3dae1b44162d5678287b021b8393e17d52a68c7c63b1369`

(The revision adds: TOOL checks the executable bit, TIMEOUT uses `--timeout 2` with a `>= 3.0 s` stall-request span and `< 20 s` wall, REVIEW checks substance/open-finding markers.)

```
TOOL PASS path=tools/reopen-row.py exists=True executable=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2342', 'REFUSED', 0), ('S2634', 'REFUSED', 0), ('S2932', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2421', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2520', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2520', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2752', 'MALFORMED', 0), ('S2317', 'MALFORMED', 0), ('S2045', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2070', 'LOCATED', 1), ('S2615', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2074', 'TRUNCATED', 1), ('S2928', 'LOCATED', 1)] want=[('S2074', 'TRUNCATED', 1), ('S2928', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2242', 'UNREACHABLE', 3)] wall=6.1s stall_hits=3 span=4.0s
REVIEW FAIL reports=4 token=0 missing=['RevToolA.md', 'RevToolB.md', 'RevToolC.md', 'rev-hold-lift.md'] thin=[] open_findings=[]
ACCEPT-O-63: FAIL
exit=1
```

Receipt lines (one per counter run; the counter sha is the sha of the counter actually run, the revision is the lane revision the candidate was scored against):

```
RECEIPT ExecRepairTool/accept-o-rev0 counter-sha256=a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=REVIEW
RECEIPT ExecRepairTool/accept-o-rev4 counter-sha256=23355bac77f5bc3ed3dae1b44162d5678287b021b8393e17d52a68c7c63b1369 rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=REVIEW
```

`stopped-by=REVIEW` only: every leg that measures the artifact (TOOL, INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT) prints PASS in both runs. The REVIEW leg measures the independent review gate, which is not this seat's artifact; it fails because the four review reports were not all present in the clone (and, see §7, because of a defect in the revised leg itself).

Control verdicts for this seat's item (the artifact is the thing under test; no cheap fixture that skips the claimed work can pass):

```
CONTROL-MET: none for the artifact legs — CtlODoNothing (a no-op tool) fails GEN (no ROW lines, wrong verdict set), REDIRECT (no REFUSED row), MALFORMED, GZIP, TRUNC and TIMEOUT; the counter's TOOL/INDEP legs are existence/text legs and cannot be satisfied by a no-op that keeps the file name and the forbidden names out.
```

## 6. Review gate status (for the L1)

* `RevToolA` restated its verdict against the **final** candidate bytes (`0d965ccb…`, 1217 lines, mode 755, AST clean): catalogue items closed (cross-host redirect to loopback/RFC1918/link-local/0.0.0.0; decimal/octal/hex/dotted-less IP literals; userinfo confusion; scheme-relative `Location`; https→http downgrade; redirect loops and the 5-request hop cap; `--allow-private` semantics), one residual LOW (DNS-rebind TOCTOU, inherent to an IP-based policy), token `VERDICT: NO-OPEN-HIGH-MED`.
* `RevToolB` reviewed the same final bytes and also carries the token.
* Still missing for the REVIEW leg: `.ufo/waves/round-63/w1/RevToolC.md` and `reports/round-63/telemetry/rev-hold-lift.md` (the residual review of the LANDED bytes — it can only be produced after the L1 lands the tool).
* The safety hold was honoured: this seat never ran the lane's held `tools/reopen-row.py`; every execution above used the scratch candidate against localhost fixtures only, and no live URL was fetched.

## 7. Defect found in the lane's counter (revision 4) — action needed by the L1

The revised REVIEW leg is self-contradictory: it requires each report to carry the fixed token `VERDICT: NO-OPEN-HIGH-MED`, and its open-finding scan is

```python
if re.search(r"\bOPEN\s*[\(\-:]?\s*(HIGH|MEDIUM|MED)\b", body):
```

which matches the `OPEN-HIGH` **inside the required token itself** (`NO-OPEN-HIGH-MED`: the `-` before `OPEN` is a word boundary, `-` is in the optional punctuation class, `HIGH` follows). Therefore every report that carries the token is classified as `tainted`, `continue`s before the token test, and `tokens` can never reach 4 — the leg can never PASS.

Measured against the reports that exist in the lane right now (read-only replay of the leg's own logic on the lane's files):

```
missing=['RevToolC.md', 'rev-hold-lift.md'] thin=[] tainted=['RevToolA.md', 'RevToolB.md'] tokens=0
```

Minimal counter fix (a revision is allowed before the first run of that counter on the claimed object; no run on the landed repair has happened yet, so this revision is still admissible and must be committed with the receipt that forced it): exclude the verdict token from the marker scan, e.g.

```python
scan = body.replace("VERDICT: NO-OPEN-HIGH-MED", "")
if re.search(r"\bOPEN\s*[\(\-:]?\s*(HIGH|MEDIUM|MED)\b", scan):
```

(equivalently a negative lookbehind `(?<!NO-)`). Without this, the REVIEW leg fails for reasons unrelated to the claim, and the closure's receipt would show a spurious miss.

## 8. Risks, blockers, notes

* **Blocker for the REVIEW leg only**: `RevToolC.md` and `reports/round-63/telemetry/rev-hold-lift.md` do not exist yet, and the revised leg's marker regex needs the fix in §7. Neither is this seat's to produce.
* **Landing note**: the revised TOOL leg requires `tools/reopen-row.py` to be executable; the candidate is mode 755, so a plain copy keeps the bit — but a copy that drops it fails TOOL.
* **Semantics chosen where the contract left room** (all consistent with the counter's expectations): (a) a hop to another authority is checked with the strict private-host check even under `--allow-private`, while a same-authority hop is only re-checked when `--allow-private` is absent; (b) a row whose URLs are *all* refused prints `REFUSED`, a row whose URLs are *all* malformed prints `MALFORMED`, and a mixed malformed/refused row prints `REFUSED` (the higher rank); (c) `TRUNCATED` is used only when a 2xx body was cut at the cap and the quote was absent from the bytes read; (d) a malformed redirect target ends that URL for the pass as a fatal result (no request to it).
* **Residual, documented by the reviewer**: the private-address policy is IP-based and resolution-based, so a DNS-rebind between the check and the connect is not covered (LOW, inherent to the policy).
* **Not done by this seat (out of scope)**: landing the tool in the lane, editing `corpus/QUALITY.md`, `corpus/lessons/round-62.md`, `SCORECARD.md`, running any live fetch, judging, committing or pushing.
* **Installs**: none (stdlib only; no pacman/uv/npm/cargo traffic, no host service touched).

## 9. Where the L1 must go

1. Copy `/fast/scratch/hyaku/kotodama-r63/ExecRepairTool/reopen-row.py` to `tools/reopen-row.py` (keep mode 755) and commit it as the claim-O repair.
2. Fix the REVIEW-leg marker scan as in §7 (counter revision, committed with this report as the forcing receipt) and have `RevToolC` and `RevHoldLift` produce the two missing reports against the landed bytes.
3. Run `python3 -B reports/round-63/accept-o.py` at the lane tip: with the tool landed and the four review reports in place, every leg of §5.2 is expected to print PASS unchanged (the artifact legs were already PASS on these bytes).
