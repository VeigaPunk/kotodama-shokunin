# ExecTelemetryDigest — round 74 wave 2 (falsify), seat attack on the telemetry and evidence record

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (all reads `git show <rev>:…`; no lane byte written).
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze F3 `00c408a0af2fa5ddf65af2224152ce258b26d896`;
claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`;
lane `main` at dispatch `1d7add3f7b9eaf6f3349c56c36f6d06325d74236` (plus `92b8d4b`, an orchestrator in-flight
snapshot committed at 23:17 — not inspected as a landing).

AGENTS.md rule attacked (quote, 22 tokens): "Each telemetry snapshot names its owner, observation time or closed
sampling window, counting command and date, durable source paths and SHA-256 digests." Where a status quote is
needed I quote ≤25 tokens verbatim with location.

Work was executed only in my own clone (`/tmp/ExecTelemetryDigest/lane`, `git rev-parse --show-toplevel` = that dir,
`git branch -f main <lands>` inside it). Counters were re-executed there; the lane repo, fleet repo, sibling lanes,
`.ufo/state`, `MANIFEST.json`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `corpus/**`, `reports/**` were read only.
No tool installed (nothing needed); no network fetch made by this seat (fetch hygiene is the evidence seat's lane;
I only read the committed capture headers). Host clock check: local `2026-10-25 23:20 -03`, UTC `2026-10-26 02:20`;
every `2026-10-26T0xZ` stamp in the receipts is the same local day — **no future-date defect** (attack failed).

---

## 1. Inventory at `main` (bytes from `git ls-tree -r --long main`; sha256 from the checked-out blob)

### reports/round-74/telemetry/ (13 files)

| file | bytes | sha256 |
|---|---|---|
| accept-c-73-at-lands.txt | 1298 | `50c60bb67f1691b4c1efbdafe33bd71261509bf939a515f95d3eb16927f5ae1a` |
| accept-ca-73-at-lands.txt | 2895 | `864c94192854f37bfbf5bbf0e58f42fe41c86810cead36e79161700d3f24784e` |
| census-end.txt | 3675 | `d31d2c4536f14a1f1598c7a0a5bccf68f39371d99dd0da29d7f9d2d389fb6506` |
| census-start.txt | 3340 | `1f05f1e9eab616e63d412620d5a450b541c59b930e4fffb3524c526781142dba` |
| controls-c.txt | 4932 | `6241fee7f47333594e553af92bd72e13d67e961c4f6912c2d490fc40497e4bd1` |
| controls-ca.txt | 6303 | `a7eb5c5b5a923ed61d8a1c570eb0efb7c1831a7c6d0d663c3f039cd54bb58d9b` |
| gap-sweep.txt | 6018 | `ac0ac218259cf2ec2b730eb2dc25728453a75157f825797e6333eea6d4ee090e` |
| junk-c.txt | 13593 | `dab2810d9850da030c8e8931153e3285dc1698d47cc4ef8367077e4407587db6` |
| junk-ca.txt | 25049 | `5b9c5070189342054408a297e2ed3a47ce2c974570dbfff1e7a20c1fa57b777c` |
| measures-c.txt | 2225 | `b81ab4397077703543365469e9f5af9b53e45cf0c980a3fa1a55393de2eb3089` |
| measures-ca.txt | 5002 | `11936ad7c8ab60fe7894652b1fc59f3b363c712159ca01fb9b6f1ed433fa6211` |
| selftest-c.txt | 33 | `1e32b1ed2a48eb779ec47747967164b955708f86bbbe765b71c9448edfc5ffbc` |
| selftest-ca.txt | 7736 | `eed1e32b9634b10c05f83d70729b501a081237d8f1f1591843ae6ee6b57420bb` |

Blob identity between freeze and lands (the two that moved are findings F3):

| file | 00c408a blob | 5e4796c / main blob |
|---|---|---|
| controls-c.txt | `d0c4996e20e9…` (5248 B) | `443913837a65…` (4932 B) |
| controls-ca.txt | `c334e826e352…` (8401 B) | `854484618088…` (6303 B) |
| everything else above | unchanged from the freeze blob | — |

Presence by revision (`git cat-file -e <rev>:<path>`):

```
junk-c.txt          00c408a:NO 5e4796c:NO c4bf61a:NO 1d7add3:yes
junk-ca.txt         00c408a:NO 5e4796c:NO c4bf61a:NO 1d7add3:yes
measures-c.txt      00c408a:NO 5e4796c:NO c4bf61a:NO 1d7add3:yes
measures-ca.txt     00c408a:NO 5e4796c:NO c4bf61a:NO 1d7add3:yes
census-end.txt      00c408a:NO 5e4796c:NO c4bf61a:yes 1d7add3:yes
census-start.txt    00c408a:yes 5e4796c:yes c4bf61a:yes 1d7add3:yes
```

### reports/round-74/evidence/ (5 files)

| file | bytes | sha256 |
|---|---|---|
| S877.txt | 9664 | `165951614548401672378ff8b4696f83b7581b17ecf30922e8edfa3c93acdf26` |
| S881.txt | 13762 | `f22e223e39ed7a5fb8049e8e467cbe4d1f57dd330db5a24881c125ffce78c145` |
| S882.txt | 10399 | `e6030849c25eabb7ee742ba4f100977d8b02599191d21cf4c440d4b58e9f7da7` |
| S883.txt | 14238 | `6013c8258e52c34cd622de5021cfbf76302bc9d607c01d459ad841385533aa9c` |
| S884.txt | 14183 | `68bede11dc8d1be3856deb4b61a34fd0886fb6f139eb1128dba41dc812948029` |

Each evidence file carries `url/http/bytes/sha256/fetched/ua/content-type/final-url/extract`, `window-scope:`
(excerpt ×4, `whole-document` for S882) and `window-sha256:` — the capture header shape is complete; UA is the
browser-shaped string required by QUALITY 21/22/24. They are captures, not revision stamps; the EVIDENCE leg reads
them at `<lands>`. I did not re-fetch (out of seat scope); the offline counter cannot prove a fetch and the
non-author re-open is the evidence seat's.

### Counter identity checks (all pass)

```
00c408a / 5e4796c / c4bf61a / 1d7add3 → reports/round-74/accept-c.py
  = 8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a
                             reports/round-74/accept-ca.py
  = 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
.git/waves/round-74/counters/{accept-c,accept-ca}.py at the freeze hash to the same two values.
round-73: 2d1cd914:accept-c.py = 95aee881… , accept-ca.py = 222d4dd6…  (== the two receipts' "counter sha256")
```
Every "counter sha256 (self)" header in `measures-c.txt`, `measures-ca.txt`, `controls-c.txt`,
`controls-ca.txt`, `accept-c-73-at-lands.txt`, `accept-ca-73-at-lands.txt` equals those values.

---

## Findings

### F1 — BLOCKER — the junk-landing receipts the frozen claims cite do not exist at the freeze, and were generated after the data landed

Attacked: "the freeze ships the junk landings it must reject" — QUALITY 25 (b): "The freeze commit carries …
four receipts under `reports/round-<N>/telemetry/`" (`corpus/QUALITY.md:84`), and
`claims.json` C `do_nothing_control` naming `reports/round-74/telemetry/junk-c.txt` / Ca's naming `junk-ca.txt`.

Command and raw output:

```
$ for p in junk-c.txt junk-ca.txt; do printf "%-12s" $p; for r in 00c408a 5e4796c c4bf61a 1d7add3; do \
    printf "%s:%s " $r "$(git cat-file -e $r:reports/round-74/telemetry/$p 2>/dev/null && echo yes || echo NO)"; done; echo; done
junk-c.txt  00c408a:NO 5e4796c:NO c4bf61a:NO 1d7add3:yes
junk-ca.txt 00c408a:NO 5e4796c:NO c4bf61a:NO 1d7add3:yes
$ git log --format='%h %aI %s' -3 1d7add3
1d7add3 2026-10-25T22:50:09-03:00 round-74: junk-landing receipts, measured receipts at each claim's own landing, wave-2 builder
c4bf61a 2026-10-25T22:49:29-03:00 round-74: claim C landing fixes …
5e4796c 2026-10-25T22:46:35-03:00 round-74: claim Ca landing …
```

`junk-c.txt`/`junk-ca.txt` state `generated: 2026-10-26T01:53:19Z` (= 22:53 -03), i.e. **four minutes after claim
C's lands commit** — the red-before receipts were produced after both claims had landed, not at the freeze, and
qualify nothing pre-data. Two of the four receipts QUALITY 25 (b) names are missing at the freeze commit (the
controls pair is present); both are missing at both claims' lands as well. Nothing in either counter reads them
(no leg names them), so no counter verdict depends on them — the record's declared controls are simply not
verifiable from the frozen tree. The per-fixture `lands:` commits (`be68571…`, `aee16f4…`, `e28a368…`, …) are
commits of removed `/tmp/ExecJunkFixtures/...` fixture repos; they exist nowhere in the lane, so the fixture
commits "traveling in the receipt" cannot be re-derived either.

Fix: commit the receipts and the generator *in the freeze commit* next round (create the freeze commit last, after
the junk run), or amend the criterion text to say the receipts land with the claim and are re-derived from the
committed generator; here, have the L1 record the absence explicitly (a `could-not-recover`-style note) rather
than citing paths that do not exist at the frozen commit.

### F2 — HIGH — the junk generator named by both receipts is not the generator at the freeze

```
$ git cat-file blob 86be84892cf79ae07efe75b54e92a94561104118 | sha256sum     # 00c408a:.ufo/…/junk-fixtures.py, 31150 B
d4789c39740de5b6679e63f8fe0b2c54794f9eb358c8e8ab4660de622de9693f
$ git cat-file blob ba10f52ebcb9e2a33b1d321ec571ca1dd3790675 | sha256sum     # 1d7add3:.ufo/…/junk-fixtures.py, 61592 B
ce6505fc7d973ced8ad663ee5201eae4931129684dd9794744f115a49fba6d76
```
`junk-c.txt:1` and `junk-ca.txt:1` carry `generator sha256=ce6505fc…` and `freeze: 00c408a0…`. The generating
program (ce6505fc, 61,592 B) first appears in `1d7add3`; the freeze's program is a different, half-size file
(d4789c39). So the receipts claim to be the frozen toolchain's output while naming a tool that did not exist at
the freeze, and the freeze's own `junk-fixtures.py` has no receipt at all.

Fix: as F1 — freeze after the run; and when a counter/generator is revised after the freeze, record it under a
`counter-revisions.md` (old sha, new sha, reason) as QUALITY 23 requires, instead of letting the receipt's
`freeze:` token denote a toolchain that never coexisted with it.

### F3 — MEDIUM — the freeze commit shipped do-nothing controls measured at the *previous* freeze; they were rewritten in place at the Ca landing

```
$ diff <(git show 00c408a:reports/round-74/telemetry/controls-c.txt) \
       <(git show 5e4796c:reports/round-74/telemetry/controls-c.txt) | head -4
1c1
< # controls-c.txt — claim C do-nothing controls (round 74), measured at freeze de93d91cab5a…
---
> # controls-c.txt — claim C do-nothing controls (round 74), measured at freeze 00c408a0af2f…
3c3
< $ python3 -B reports/round-74/accept-c.py --root . --lands de93d91cab5a… --freeze de93d91cab5a…
```
Same shape for `controls-ca.txt` (header, arg line, `# stamped/# evaluated/# measured`, `# tree`, `# config
sha256`, clone path, and the leg block — at `de93d91c` the C control read `FAIL legs=2/13`, today's stored text
reads `FAIL legs=4/13`). At `main` the stored receipts *are* measured at `00c408a` (I reproduced both, F5/F4), so
the graded bytes are consistent; but the freeze commit — the artifact QUALITY 23 says must carry the freeze run —
carried controls for a superseded freeze, and the corrected text is an in-place edit of a committed receipt. R74-M9
("Three freeze commits, not one") discloses the freeze count, not the receipt replacement.

Fix: land the operative-freeze control receipts in the operative freeze commit; if they must be replaced, append a
new receipt file (`controls-c-r2.txt`) and keep the old bytes below a marker, per QUALITY 17.

### F4 — MEDIUM — the recorded C control command is location-dependent: it omits the `--fleet-root` its CENSUS leg needs

`controls-c.txt:3` records `python3 -B reports/round-74/accept-c.py --root . --lands 00c408a… --freeze 00c408a…`
(no `--fleet-root`). Run verbatim from a clone:

```
LEG FAIL CENSUS
     census script not found: /tmp/ExecTelemetryDigest/scripts/sources-census.sh
ACCEPT-C-74: FAIL legs=3/13
```
With `--fleet-root /home/vgpnk/Projects/shokunin` added, the same revision gives the receipt's value:

```
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r74-fleet-tsfac4wy/kotodama-shokunin/corpus/SOURCES.md
ACCEPT-C-74: FAIL legs=4/13
```
The receipt's 4/13 is only obtainable when the counter is invoked inside the lane directory (whose parent happens
to be the fleet root) — an unrecorded invocation state.

Fix: add `--fleet-root` to the recorded control command (accept-ca already requires it), or make the counter
refuse with a named exit when the census script is absent instead of scoring a leg red for the wrong reason.

### F5 — MEDIUM — the Ca control's STAMP leg depends on lane `main` being the freeze; the receipt reproduces only if that state is re-created

Fresh clone, `main` at claim C's lands:

```
LEG FAIL STAMP
     stamped=evaluated=measured=00c408a0af2f tree=b002eee8627c counter=8052f1e25c36 clone=/tmp/r74-ca-9v5jnov9/lands
     problems=['measured c4bf61a8d722f9168ce0fd8021a6261c000610c5 != lands 00c408a0af2fa5ddf65af2224152ce258b26d896']
ACCEPT-CA-74: FAIL legs=6/11
```
With the clone's `main` pinned to `00c408a` (the recorded `# measured revision (lane main)` state):

```
ACCEPT-CA-74: FAIL legs=7/11      # = controls-ca.txt's recorded value (REPAIR, ANNOTATE, NOSTUB, SEPARABLE red)
```
So the control is faithful to the state it was measured in, but that state (lane main == freeze) no longer exists
and the receipt does not say the invocation must be made from it.

Fix: record the invocation state (lane main, cwd, `--root` identity) in the receipt header, as QUALITY 17/19
already demand for measured revision.

### F6 — MEDIUM — the RECEIPTS leg is TMPDIR-sensitive: the same lands yields PASS with `TMPDIR=/tmp` and FAIL otherwise

Controlled A/B, identical clone, identical counter, only `TMPDIR` changed:

```
# TMPDIR=/home/vgpnk/…/.ufo/waves/round-74/w2-scratch-ExecTelemetryDigest/tmp, lands=c4bf61a
LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854']
     problems=['reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run (bda16ca6deec vs 830235ba31c6)', 'reports/round-74/telemetry/accept-ca-73-at-lands.txt: committed stdout differs from the re-run (55544779204d vs 8d5b3321bae9)']
ACCEPT-CA-74: FAIL legs=9/11
# TMPDIR unset (default /tmp), same lands=c4bf61a
LEG PASS RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=[]
ACCEPT-CA-74: FAIL legs=10/11
```
Cause: the re-executed round-73 stdout embeds its materialized fleet path
(`exit=0 last-line=kotodama ok /tmp/r73-fleet-…/corpus/SOURCES.md`); the comparison normalizes `/tmp/...` only,
so any other `TMPDIR` breaks byte equality on an otherwise correct receipt. A stranger with `TMPDIR` set reads a
spurious FAIL.

Fix: normalize every temp-root prefix (or the whole path field) before comparing stdout, and state the comparison
rule in the counter docstring; re-run the receipt under both settings in the selftest.

### F7 — MEDIUM — the two selftest receipts carry neither the counter sha256 (QUALITY 23) nor owner/revision/command

QUALITY 23 (`corpus/QUALITY.md:77`): "its verdict line, exit code and counter sha256 committed under the round's
telemetry before the falsify wave is dispatched".

```
$ git show main:reports/round-74/telemetry/selftest-c.txt | od -c | head -2
0000000   S   E   L   F   T   E   S   T   :       6   9   /   6   9
0000020   s   c   e   n   a   r   i   o   s  \n   e   x   i   t   =   0
$ git show main:reports/round-74/telemetry/selftest-c.txt | grep -c "sha256\|8d30487"
0
$ git show main:reports/round-74/telemetry/selftest-ca.txt | grep -n "sha256\|8d30487\|8052f1e2\|revision\|tree:" 
(no output)
```
Neither file names the revision, the counter sha, the command or an owner. (Contents do reproduce when run —
see "Attacks that failed" — the defect is provenance, not fidelity.) No telemetry file above names an owner
(`grep -ci owner` = 0 for 12 of 13; `gap-sweep.txt`'s two hits are about sibling-lane ownership), and
`measures-ca.txt` carries no date line at all.

Fix: wrap every receipt with the standard header (`# owner`, `# command`, `# access date`, `# counter sha256`,
`# stamped/evaluated/measured`, `# tree`) and re-emit the selftest receipts under it.

### F8 — MEDIUM — the census receipts are raw stdout with no provenance and no row count; the claims' "804 rows" is not derivable from the bytes

```
$ git show main:reports/round-74/telemetry/census-start.txt | grep -c "804\|808\|rows"
0
$ git show main:reports/round-74/telemetry/census-end.txt | grep -c "804\|808\|rows"
0
$ git show main:reports/round-74/telemetry/census-start.txt | head -1
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
$ git show main:reports/round-74/telemetry/census-start.txt | wc -l   → 30   (28 W04 lines + ok + exit=0)
$ git show main:reports/round-74/telemetry/census-end.txt   | wc -l   → 33   (+ 3 W01 lines)
```
`claims.json`'s `frontier_step.census_start` says "reports/round-74/telemetry/census-start.txt (exit 0, 804 rows)"
— the exit is in the bytes, the row total is not, and the receipt names no owner, revision, command, date or
digest. I verified the totals independently (attack on the *number* failed):

```
git show f7104cb:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'   → 804
git show 00c408a:corpus/SOURCES.md | …                                                           → 804
git show 5e4796c:corpus/SOURCES.md | …                                                           → 804
git show c4bf61a:corpus/SOURCES.md | …                                                           → 808
git show main:corpus/SOURCES.md    | …                                                           → 808
```
`census-end.txt` lists W01 new-row lines for S881, S882, S884 but not S883 — explained, not a defect: W01 is
tier-C-scoped (`scripts/sources-census.sh:31`) and S883's tier cell is `B` (`corpus/SOURCES.md` S883 row), while
all four status cells are `mined`. The census-end receipt itself exists only from claim C's lands (`c4bf61a`),
not at the freeze, so the Ca claim's record has no end census.

Fix: emit the census under a header carrying `--today`, root, revision and sha256 of `corpus/SOURCES.md`, and print
the scanned row total on its own line; then a claim can cite a number that its receipt contains.

### F9 — HIGH — claim Ca's PASS does not hold at the round's integrated tree; the only disclosure is a note inside a post-lands receipt

`claims.json` Ca `after`: "prints ACCEPT-CA-74: PASS legs=11/11 (exit 0)". Fresh clone, serial runs, default TMPDIR:

```
# lands=5e4796c (claim Ca's own landing) — the committed receipt's revision
ACCEPT-CA-74: PASS legs=11/11          exit=0
# lands=c4bf61a (claim C landed on top of it)
LEG FAIL APPENDONLY
     problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
ACCEPT-CA-74: FAIL legs=10/11          exit=1
# lands=1d7add3 (lane main at dispatch)
LEG FAIL APPENDONLY
     problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
ACCEPT-CA-74: FAIL legs=10/11          exit=1
```
Line 832 is the S877 `used-by` cell claim C is required to change; it is not a Ca REPAIR `stated_at`, so the two
frozen claims conflict in one tree. `junk-ca.txt` carries an L1 note saying exactly this ("claim Ca is therefore
measured at its OWN landing commit … Disclosed as a frozen-claims limit, not amended") — but that receipt landed
after both claims, and neither `corpus/lessons/round-74.md:7-9` ("`ACCEPT-CA-74: PASS legs=11/11`"), the LOG, nor
SCORECARD carries the qualification; `grep -n "APPENDONLY\|own landing\|cross-claim"` over
`corpus/lessons/round-74.md SCORECARD.md LOG.md` returns only R74-M9 (about the *earlier* freeze). There is no
receipt and no artifact measuring the integrated tree (`reports/round-74/` has no `validation.json`), so the only
PASS anyone can quote is the intermediate one.

Fix: state the limit where the verdict is quoted (lesson claim line + LOG), and add an integrated-tree receipt
recording the expected APPENDONLY red; do not leave a reader to discover it by re-running at `main`.

### F10 — LOW — `junk-ca.txt` is not the "split" its header claims

`junk-c.txt:1`/`junk-ca.txt:1`: "split from counters/junk-r74-run.txt by the L1". Line-subsequence check against
`main:.ufo/waves/round-74/counters/junk-r74-run.txt`: `junk-c.txt` body 129 lines, all present in order; `junk-ca.txt`
body 181 lines, 4 lines present nowhere in the run —

```
absent: '# NOTE (L1, 2026-10-25): at reference landing T0 the Ca coun…'
absent: '#  (1) APPENDONLY: claim C's required in-place used-by chang…'
absent: '#  (2) SEPARABLE: at the freeze the previously committed con…'
absent: 'expected: FAIL: a Ca-read corrections row cites claim-C rows the claim-C lane ids (SEPARABLE)'
```
(the run says `…cites claim-C rows S881..S884 (SEPARABLE)`). So the receipt is an edited copy — a redaction plus an
inserted note — not a mechanical split; the wording understates the edit (the note is load-bearing, see F9).

Fix: say "edited copy of …; edits: redaction of lane ids, L1 note" in the header, or keep the note in a separate
file so the split stays mechanical.

---

## Attacks that FAILED (the claim survived, with the evidence)

1. **`measures-c.txt` is faithful.** Re-ran the counter at `c4bf61a` in my clone:
   `ACCEPT-C-74: PASS legs=13/13`, exit 0; `diff` against the committed receipt differs **only** in the two `/tmp`
   temp paths (materialized clone dir, `r74-fleet-…/corpus/SOURCES.md`).
2. **`measures-ca.txt` is faithful.** Re-ran at `5e4796c`: `ACCEPT-CA-74: PASS legs=11/11`, exit 0; `diff` differs
   only in the two `/tmp` clone/base-clone lines and the STAMP clone path.
3. **Counter sha256s are correct**, at every revision, and equal the `# counter sha256 (self)` headers (checks
   above). The round-73 receipts carry the round-73 counters' true hashes (`95aee881…`, `222d4dd6…` at `2d1cd914`).
4. **The round-73 PASS-at-lands receipts are real and re-execute.** `RECEIPTS` legs passed
   (`rev=2d1cd9140d3a … problems=[]`) in my `5e4796c` and `c4bf61a` (default-TMPDIR) runs; the committed stdouts
   contain `ACCEPT-C-73: PASS legs=11/11` and `ACCEPT-CA-73: PASS legs=9/9`.
5. **The do-nothing controls are correct for the state they were measured in.** At `--lands=--freeze=00c408a`
   with the clone's `main` pinned to `00c408a`: C `FAIL legs=4/13` (same nine red legs, `GROUND/CENSUS/COLLCHECK/
   FROZENCFG` green) and Ca `FAIL legs=7/11` (same `REPAIR/ANNOTATE/NOSTUB/SEPARABLE` red) — both equal to
   `controls-c.txt`/`controls-ca.txt`. Control 2 reproduces verbatim for both: `REFUSED … exit=2`, and
   `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base f7104cbce186)`.
6. **Both selftest receipts reproduce.** `accept-c.py --selftest` → `SELFTEST: 69/69 scenarios`, exit=0, identical
   to `selftest-c.txt`. `accept-ca.py --selftest` → `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0`,
   exit=0, identical to `selftest-ca.txt` except the temp path and the receipt's two appended annotation lines
   (`exit=0`, the "expected stderr" note). A first attempt failed (`SELFTEST FAIL: expected-after-mismatch exit got
   2 want 1`) because `/tmp` was 100 % full — host pressure, not a counter defect; re-run with `TMPDIR` on `/home`
   passed.
7. **Claim C passes at `main`, not only at its lands** — `ACCEPT-C-74: PASS legs=13/13` at `1d7add3`.
8. **`junk-c.txt` is internally consistent**: each of J1, J2, J3, J9 names its fixture, lands commit, verbatim
   command, `LEG FAIL <LEG>` line(s), exit code and verdict (`9/13`, `12/13`, `8/13`, `12/13`), and `accepted: no`;
   `junk-ca.txt` likewise for J4, J4b, J5–J8 (and J9). I did not re-execute the fixture generator (an unrun check
   is not a pass): my attack on these two files is F1/F2/F10, which are about where and from what tool they exist.
9. **The "804/808 rows" numbers are true** (independent grep counts above), and the `2026-10-26TxxZ` stamps are the
   same local day as the claimed 2026-10-25 access date.

---

## Residual risks for the parent

- The absence of an integrated-tree receipt (F9) is the one artifact I would not accept as-is: a reader who runs
  the frozen command at `main` gets `ACCEPT-CA-74: FAIL legs=10/11`. Either the Ca verdict is quoted with its
  revision (`5e4796c`) everywhere, or the frozen conflict is ruled on by the L0/L1.
- F1/F2 mean QUALITY 25's own clause (b) is not satisfied by the freeze; the criterion's frontier claim should be
  recorded as partly unmet unless the L1 rules the receipts' later landing acceptable.
- F4/F5/F6 are reproducible-with-recipe defects; none changes a claim's verdict when the recipe is followed, but
  each lets a stranger read a different verdict.

## Scratch

Work tree `/tmp/ExecTelemetryDigest/` (clone + raw outputs: `rerun-measures-c.txt`, `rerun-measures-ca.txt`,
`serial-run.txt`, `controls-rerun.txt`, `controls-freeze-state.txt`, `ctl1-c-fleetroot.txt`,
`rerun-ca-clands-defaulttmp.txt`, `ca-selftest-home.txt`). The in-lane scratch directory created for counter
temp trees (`.ufo/waves/round-74/w2-scratch-ExecTelemetryDigest/`) was removed after the runs; no other lane byte
was written.
