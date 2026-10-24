# RevClaimCa — attack on claim Ca's dispositions (R65-D1..D4)

Seat: RevClaimCa (leaf reviewer). Milestone r66-v2. Base `94209e8f80969dbac48d56c5d0e2e623635b8616`.
Scope attacked: `reports/round-66/accept-ca.py` (all six legs), `reports/round-66/claims.json`
(claim Ca statement/legs/lands), `corpus/lessons/round-65-verifier-spotcheck.md` §5 + §2 Claim Ca,
`corpus/lessons/round-65.md` R65-M9, and the Ca receipts on disk. Read-only; nothing in the lane mutated.
No tools installed or upgraded (none needed).

**Premise verdict:** 3 of the 4 disposition *choices* are right in kind, but **three of the four
declared legs evidence proxies, not the routed invariant**, and the D2 leg specifically returns PASS on
the exact commit shape the round-65 closure recorded as `RECEIPTS FAIL`. `ACCEPT-CA-66: PASS` can be
printed while R65-D2 and half of R65-D3 remain unrepaired, and while the D1 anchor claim ("byte-exact")
is unsupported by any recorded bytes.

Evidence classes: `[MEASURED]` = command run or predicate executed here; `[CODE]` = cited line of the
frozen counter; `[INFERENCE]` = reasoned from cited bytes, not executed.

---

## HIGH-1 — D2 keys on the receipt's carrier commit, not the records commit: it PASSES the shape R65-D2 routed

`[CODE]` `reports/round-66/accept-ca.py:108-142`: for each receipt, `carrier = git log -1 --format=%H main -- <receipt>`
then `parent(carrier) == stamped`. That is the *receipt file's* last-touching commit — not the round's
records commit, which is what R65-D2 is about.

`[MEASURED]` applying that ancestry predicate verbatim to the round-65 receipts (the run the closure failed):

```
final-measures-c.txt  carrier 53a60275 parent 3b1b5a67 stamp 3b1b5a67 ANCESTRY_LEG PASS
final-measures-o.txt  carrier 53a60275 parent 3b1b5a67 stamp 3b1b5a67 ANCESTRY_LEG PASS
final-measures-ca.txt carrier 53a60275 parent 3b1b5a67 stamp 3b1b5a67 ANCESTRY_LEG PASS
```

Round-65 history (`git log --format='%h %p %s'`) is `3b1b5a6 lands` → `53a6027 file measurements and
prepared wave receipts` → `3e85a61 record final measurements and prepared wave` → `29d0b0f correct
receipt-parent verdict`. `corpus/lessons/round-65.md:103` (R65-M9) states the defect exactly: *"The
records commit at `3e85a610` was not a direct child of lands `3b1b5a67`; an intervening prepared-wave
evidence commit `53a60275` changed `main^`."* The spotcheck §2 Claim Ca recorded the consequence:
`RECEIPTS FAIL lands=53a60275`, `ACCEPT-CA-65: FAIL`.

So: the round-65 defect lives in the **records commit's** parent; the round-66 leg checks the
**receipt commit's** parent. The leg's namesake invariant is therefore not tested, and the new leg is
strictly weaker than the round-65 leg in the one dimension that failed. (Honest limitation: the
round-65 receipts also fail today's `counter sha256 (self):` line format, so a full run would still red
on `counter_sha`; the *ancestry* invariant — the one the leg is named for — passes.)

`[INFERENCE]` Consequence: a lane can satisfy D2 by committing the receipts as a child of any commit it
chooses to stamp, then landing the actual record/lands content later or elsewhere. The spotcheck's own
suggested remedy ("make the receipt leg's expected lands hash the actual parent at run time", §5 D2) is
not implemented; it is only parked in `claims.json` `review_only`, which does not stop ACCEPT-CA-66
from printing PASS. Declining the routed remedy is a legitimate choice; failing to say so in the
disposition and failing to test the routed invariant are not.

**Minimal fix:** per receipt, require (a) the carrier's parent tree to contain the exact blobs the
counter read for every declared land (blob-equality per land path, not a self-reported tree string),
(b) the carrier commit's own diff to touch receipt paths only (no land path), and (c) the lands' carrying
commits to be ancestors-or-equal of the stamped revision.

## HIGH-2 — D2 passes a records-before-lands run: the lands are absent from the stamped revision

`[MEASURED]` synthetic `/tmp/d2fx` (git init; commit A base; write + commit the receipt stamped `A` as
child of `A`; **then** commit the lands file; apply the D2 ancestry+tree predicate at tip):

```
carrier 991dcd82 parent==stamp True tree_line_ok True
lands committed in stamped revision? NO -> lands absent from stamped revision
D2 VERDICT: PASS
```

`[CODE]` the D2 block reads only `rpath`, the carrier, `stamped^{tree}`, and the counter file. It never
opens a land path and never compares the shipped bytes with the measured bytes. So "the receipt commit
is a child of the lands commit" is replaced by "the receipt commit is a child of whatever revision the
lane stamped" — and the stamp is lane-authored. Example that the check would not catch: measure at L,
commit receipts in child of L, then edit the games entry (a Ca land) in a later commit; D2 stays green
while the shipped entry is not the measured entry. This is precisely the "receipt's commit ancestry but
not the lands' real parent" gap.

## HIGH-3 — D1 is a string-shaped receipt: "byte-exact" is recorded nowhere, and a 4-line fabrication passes

`[MEASURED]` fixture: ran the real `accept-ca.py` with `--root /tmp/r66ca` over a telemetry receipt
consisting only of the four strings the leg greps (`status=200`, `application/pdf`, the QUOTE,
`20261024111013`, `S776`) plus an entry citing `(S776)` once:

```
D1 PASS bad=[]
D3 PASS named=8 existing=8 min=8
CRITERION PASS QUALITY criterion 18 names anchor resolvability
QUOTES PASS exit=0 gate_ids=25 clean=True
```

`[CODE]` `accept-ca.py:88-106` greps the receipt for two status tokens, the quote string, the capture
timestamp, and the literal `S776`; nothing else. `[MEASURED]` the *real* `reports/round-66/telemetry/s753-recapture.txt`
contains **no sha256 and no byte comparison**: it records `replay_status=200 content-type=application/pdf
size=529795` for `/tmp/s753-cap.pdf`, the same `size=529795` for `/tmp/old-cap.bin`, and
`pdftotext ... (1 hit)`; there is no digest of the live PDF, the fresh capture, or the old capture.
`claims.json` Ca says *"a fresh capture 20261024111013 replays byte-exact"* — equal `size=` is not
byte-exactness, and the counter cannot tell the difference.

Also in the same receipt, `[MEASURED]`:

- the "CDX: latest captures" section is **empty**; the only CDX row is the row for the lane's own
  Save-Page-Now job (`save new capture ... 20261024111013`), so the fresh capture is not independent
  corroboration of the anchor — it is the lane's own archive request. That is acceptable as a
  durability anchor *if stated*, but it is presented as CDX evidence.
- the first old-capture probe is `old_capture status=000`; a later probe in the same file is
  `old_replay_status=200`, and the disposition then asserts *"the closure's recorded 404 was
  intermittent"*. Two contradictory probes, no declared retry budget, and the favourable one is labelled
  "(final)". `corpus/QUALITY.md` criterion 16 requires a declared retry budget before data and says
  "one transient result must not decide the claim". Either both outcomes are recorded with the budget,
  or the intermittency claim is withdrawn.

**Minimal fix:** record sha256 of (live PDF, fresh-capture replay, old-capture replay) and require
byte equality for the claim as worded (or drop "byte-exact"); scope the QUOTE grep to a `pdftotext:`
output block; record the probe attempts/budget and do not consume the old capture's 200 without the 000.

## MED-4 — D1's disposition leaves the registry lying, and claim C's APPEND leg forbids the contract's own repair

`[MEASURED]` at probe time: `corpus/SOURCES.md:709` S753 is `status=mined`, `used-by
corpus/knowledge/culture-material/games-play-sport-contests.md`; the entry cites `(S753)` once
(`games-play-sport-contests.md:23`) and `(S776)` zero times; no S776 row exists; `stage/s776-gate.md` is
empty.

`[MEASURED]` `corpus/SOURCES.md:9-12` (contract): *"Append-only: only `status`, `recheck` and `used-by`
change in place, each change logged old→new in a round lesson; a correction is a new row whose `teaches`
opens `supersedes S0NN —`."* `[CODE]` `reports/round-66/accept-c.py` APPEND: *"every registry row line
present at base is unchanged at the tip"* (`missing_old == 0`). These collide: the sanctioned repair
(citation moved to a supersession row) makes S753's `used-by` cell false, but any in-place `used-by`
flip reds claim C's APPEND, and no leg anywhere checks that the supersession row's `teaches` opens
`supersedes S753 —` or that the round-66 lesson logs the disposition old→new. The Ca D1 leg does not
read `SOURCES.md` at all.

Residual consequence of the chosen shape: S776 carries the *same URL* as S753, so the repair itself adds
a duplicate-URL row (the W04 class the closure counted at 28) and leaves a `mined` row pointing at a file
that no longer cites it. Not fabricated — contract-permitted at the row level — but it must be named in
the round-66 lesson and (ideally) S753's `used-by`/`status` retired in place with the old→new log the
header requires; then C's APPEND leg must be taught to allow exactly those logged flips (it currently
does not).

## MED-5 — D3 passes on empty files and on an expectation list: the R65-D3 failure class repeats

`[MEASURED]` the fixture above: eight **empty** `.md` files plus a status-free receipt →
`D3 PASS named=8 existing=8 min=8`.

`[CODE]` `accept-ca.py:144-154`: `reported >= 8 and len(existing) == reported and
re.search("(?i)(seat|report|status)", d3)`. The "status" alternative is satisfied by the receipt's own
header. There is **no per-seat status line and no last-error requirement**, although both the docstring
(`:21-24`) and the claim statement promise per-seat status and last-error text for dead seats.

`[MEASURED]` the live `reports/round-66/telemetry/seat-evidence.txt` is a **seed**: its header says
*"status lines added at integration"* and it lists 64 *"seat report files expected"*. A prepared
expectation list is exactly the artifact the round-65 closure refused: *"a prepared taskcall does not
satisfy the ≥8 batched-seat floor"*. The leg cannot distinguish dispatched seats from planned ones
(no taskcall id, no seat ids, no start/end timestamps, no count of dispatched vs returned vs dead).

`[CODE]` `len(existing) == reported` also **punishes honesty**: a dead seat that never wrote its file is
listed with its intended path but has no file → D3 FAIL. The receipt is therefore incentivised to omit
dead seats or to stub empty files (which pass, per the fixture) — the opposite of "retain per-seat
last-error text for dead seats".

**Minimal fix:** require one line per seat with `status=dispatched|done|dead`, `status=dead` ⇒ a non-empty
`last-error:` field; count `done+dead >= 8`; require the single batched taskcall's identity and the
wave's start/end; treat a dead seat as evidence, not as a failed leg.

## MED-6 — D4 cannot evidence the bound, and its no-PARTIAL clause contradicts claim O

`[CODE]` `accept-ca.py:156-161`: `^SEPARABILITY: \d+ findings$` + `acceptance_runs=\d+` +
`"PARTIAL" not in d4`. No elapsed time, no `--budget/--jobs/--timeout` line, no skipped count. A serial
600 s run that happens to finish passes — i.e. the leg does not evidence R65-D4's ask ("returns a verdict
inside a round's budget").

`[MEASURED]` claim O's frozen statement makes `SEPARABILITY_PARTIAL` with exit 2 the *honest* outcome of
a bounded run, and O's legs BOUND/STATIC/MAXRUNS each **require** PARTIAL. So a D4 receipt that honestly
records the partial control (as O's controls do) fails Ca by whole-file substring match, and the two
frozen predicates disagree about the same artifact class. Under `--budget 300` (claims.json
`separability.check`) a skipped run is plausible, in which case a green Ca requires suppressing the
partial — the reverse of the calibration the round is claiming.

**Minimal fix:** the receipt names the exact invocation and wall-clock elapsed; leg requires
`elapsed < budget` and a `skipped=` count; a complete verdict requires `skipped=0`, a partial is accepted
as proof-of-bound but must then be worded as such in the claim (verdict-in-budget, not complete verdict);
scope the PARTIAL substring to the verdict line.

## MED-7 — the measured revision is resolved from cwd, not `--root`

`[CODE]` `accept-ca.py:78` runs `git rev-parse main` with neither `-C root` nor `cwd=root`, while every
other git call uses `git -C root`. Running `accept-ca.py --root <lane>` from another repository stamps
*that* repository's `main` into the receipt header (and `self_sha` still refers to the counter bytes). A
foreign stamp is exactly the round-64/65 receipt-attribution class criterion 17 exists for. Fail-closed:
`git -C root rev-parse main`, and red if it does not resolve.

## MED-8 — Ca→O production dependency for D4 is undeclared

`[MEASURED]` `claims.json` Ca land list = {round-66 lesson, QUALITY, games entry, s753-recapture,
seat-evidence, separability-real, accept-ca.py}; `separability-real.txt` is produced by
`tools/check-claim-separability.py` — an O land, listed in the manifest's O unit — run over
`reports/round-66/separability-manifest.json` (an REC land). `claims.json` separability says only
Ca→REC is declared and *"any [Ca→O] finding is a real defect."* Acceptance itself is independent
(the leg greps strings), but the *evidence provenance* crosses into O: a buggy O instrument produces a
green Ca D4. Either declare it in the same sentence that declares the D2 history-derived dependency, or
have Ca re-derive the verdict's inputs. Related, currently blocking: `reports/round-66/separability-manifest.json`
and `separability-real.txt` do not exist at probe time, so the declared `expected_findings`
(`Ca->REC via land path ...final-measures-c.txt`) cannot yet be produced and ACCEPT-CA-66 cannot pass —
a landing dependency, not (yet) a lane defect.

## LOW-9 — CRITERION is a substring proxy

`[MEASURED]` a one-line fake `18. **Row anchors** must be resolvable and durable.` passes
(`CRITERION PASS`). The leg does not verify the numbering is the next criterion (only the literal `18.`
at line start, after `^\s*`), does not require the S753 class to be named, and the 900-char window can
bleed into criterion 19. At probe time `corpus/QUALITY.md` has 16 and 17 only — unlanded.

## LOW-10 — QUOTES counts ids anywhere in the lesson, so it does not test the Gate

`[MEASURED]` a fake lesson of 25 bare `- S###` lines and no quotes prints `QUOTES PASS exit=0
gate_ids=25 clean=True`. `[CODE]` `accept-ca.py:170-178` scans the whole file for `S(776-800)` and
accepts ≥25 distinct ids. The claim says *"the Gate names the round's new ids"*; prose mentions satisfy
it. Parse the `## Gate` section, require one row per id S776–S800, and require each row to carry a
quoted span.

---

## Residual risk (unattacked / cannot be attacked pre-landing)

1. **D1 durability at closure, not at probe.** The fresh capture `20261024111013` is ~20 min old at
   probe time and was created by the lane's own SPN job; the old capture is flaky (000 then 200).
   Nothing in the claim distinguishes "anchor durable" from "anchor up this afternoon". The disposition
   is contract-shaped but its durability margin is one day old.
2. **D2's self-reference bootstrap.** A green `final-measures-ca.txt` must exist in history *before* the
   run that reads it, so the accepted Ca receipt is necessarily stamped at a commit that already carries
   receipts. If the L1 lands it as one records commit whose parent is the lands commit, the ca receipt's
   own D2 leg reds at run time (its carrier does not exist yet) and the committed receipt must read
   FAIL; if it lands green, it is stamped at a receipts commit, i.e. not a child of the lands commit.
   The claim should state which shape it intends and preserve the red run below a marker
   (criterion 17). Not yet observable — no `final-measures-*.txt` exists at probe time.
3. **Timer/elapsed for D4** never recorded anywhere; my MED-6 fix requires it.

## Verification gaps

- `reports/round-66/separability-manifest.json`, `telemetry/separability-real.txt`,
  `telemetry/final-measures-{c,o,ca}.txt`, `corpus/lessons/round-66.md`, QUALITY criterion 18, the S776
  row, and `stage/s776-gate.md` content were **absent/empty** at probe time (08:32–08:36 local). Every
  landing-dependent statement above is therefore a design finding on the frozen legs, not a verdict on
  the final bytes; the L1 must re-run ACCEPT-CA-66 after integration, and the D3/D1 legs must be
  re-checked then.
- `[MEASURED]` seat files at probe: 8 of 64 expected paths existed, so the real D3 leg reds today only
  for absence, not for status quality.
- Mutation testing of the Ca legs against byte-mutants (e.g. flipping one vouchable string) was done only
  as the /tmp fixture demonstration; a pinned mutant set under `stage/mut-ca/` does not exist.
- The lineage claim "the closure's 404 was intermittent" was not independently re-probed here (external
  network, out of scope for this seat); the receipt's own contradictory probes are the evidence cited.

## Calibration summary

Right disposition, wrong evidence, per defect:

| routed defect | disposition choice | leg evidences | gap |
|---|---|---|---|
| R65-D1 S753 anchor | new supersession row + fresh capture (contract-correct) | string presence + citation move | no replay bytes/digests; registry used-by left false; intermittency claim unsupported |
| R65-D2 receipt-parent | re-derive ancestry at acceptance (reasonable) | receipt *carrier* parent | not the records commit; not the lands' parent; passes the R65-M9 shape |
| R65-D3 dispatch/evidence | dispatch the wave (correct; wave did run) | existence of ≥8 `.md` paths | empty files pass; no per-seat status/last-error; expectation list ≈ prepared taskcall |
| R65-D4 separability bound | bound via the O upgrade (correct) | receipt strings | no elapsed/budget/skipped; no-PARTIAL contradicts O |

`ACCEPT-CA-66: PASS` on the frozen legs is therefore **not** sufficient evidence that R65-D1..D4 are
dispositioned. Recommendation to the L1: keep the dispositions, harden the four legs as above, and do
not let PASS stand as the calibration record without the D2 land-blob check and the D3 status counters.
