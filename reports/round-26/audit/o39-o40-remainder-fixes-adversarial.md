# R26-O39..O40 — adversarial review of the round-25 remainder fixes

- **Seat:** O, round-26 claims **R26-O39..O40** (reviewers x2), assignment verbatim:
  "adversarial pass on the remainder fixes."
- **Date:** 2026-10-18. Observation window **18:00:45Z–18:26:31Z** (all stamps from
  `date -u --iso-8601=seconds`; `python3` 3.14.7). Lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`
  (round-26 declaration, 14:59:43−03:00); declared baseline
  `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` (`reports/round-26/claims.json:5`).
- **Write scope:** this file only. Scratch under `.scratch/r26-o39/` (gitignored,
  lane-internal); `export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1`
  preceded every scratch-writing command. No git commit or push. No filed round-8–25
  artifact, tool, gate, packet or shared bookkeeping was edited by this seat. The
  isolated clones this seat created (`.scratch/r26-o39-clone`, `-clone2`, `-ctl`,
  `-ctl2`, `-ctl3`, `-ctl4`, `-ctl5`, `-fr`, `-tw`, `-tw2`) are all lane-internal.
- **Canon:** NON-CANON engineering evidence. This review admits nothing, certifies no
  round, and adjudicates no claim. It measures the remainder fixes against the claim's
  own `after_required` text and reports what it found.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | all three round-25 remainders reproduce **red** at the pre-fix stamp, with exact failure strings | measured |
| 2 | the r4 twin gap is dispositioned by a **new row** (`reports/round-26/remainders/r4-twin/`), not by an edit of the filed round-25 revision — the append-only convention holds | measured |
| 3 | both pin tails are re-pointed by **new rows** and the v2 row replays green; the filed round-20 rows stay byte-identical | measured |
| 4 | **the re-pointed v3 row went stale within ~3 minutes of landing** — the D seat's register-stratum write to `examples/culture-d4/` invalidated it | measured |
| 5 | **the filed r4 checker cannot be made green by the pin re-point**: its red is produced by the round-26 D seat's new `L3b-argot` gate leg, not by the tails it names | measured |
| 6 | the round-26 runner **cannot evaluate** the r4 checker it depends on (invoked `--root` does not exist → exit 2), and records that as a note, not a failure | measured |
| 7 | `reports/round-26/run-validation.py --check` reads **C pass, D pass, O fail** (two O failures, both traceable to the 18:18:32Z `examples/culture-d4/` write) | measured |
| 8 | the r4-twin verifier is **24/24 green at the read set its packet pins** (`--source-root` at `e06581b`), 19/24 on the live-tree default | measured |

**Bottom line for the parent.** The *disposition shape* of the O claim is right —
new rows, filed bytes untouched, controls that fire in both directions, and both
checkers green when given the read set they declare. But `after_required`'s last
two clauses — "the r4 checker green" and "regressions green" — are **not met at
this stamp** on a live tree, and the first of them is not reachable by the work the
O seat did: the r4 checker's red is produced by a different seat's D-claim delivery
(the new `L3b-argot` gate leg). The v3 pin row's red is a moving-target problem
with the same root cause. Both are reported, not absorbed.

## 1. The three remainders, reproduced pre-fix

Everything below ran on **2026-10-18** from the lane root with `TMPDIR=$PWD/.scratch`.
Each row names the command, the date, and the exit code.

| remainder | command | exit | observed |
|---|---|---:|---|
| r4 twin gap | `ls reports/round-25/v3-supersession/declared-in-r4/` (18:00:45Z) | — | `packet.md`, `expected.json`, `freeze.txt`; **no `twin.json`** |
| v2 successor pin | `python3 reports/round-15/handoff/frozen-verify.py --baseline reports/round-20/wart/expected-v2-07-r20.json` (18:01:14Z) | **2** | `V2F-DIGEST: 1 pinned file(s) changed since the freeze: tools/d2-typed-labels.py` |
| v3 packet-baseline pin | `python3 reports/round-20/run-validation.py --check` (18:01:14Z) | **1** | `acceptance_checks_passed: false` |

The round-20 runner's own failure list is the load-bearing artifact here, because it
is the *filed* instrument that names both tails and the third failure this review
turns on. Verbatim, from that run:

```
claim D: v2 successor row not green: reports/round-20/wart/expected-v2-07-r20.json exit 2 — V2F-DIGEST: 1 pinned file(s) changed since the freeze: tools/d2-typed-labels.py
claim D: v3 baseline reports/round-20/handoff/expected.json pins packet e92f5e6775b6… but the run assembled a97a0f0a0a49…
claim O: D4 gate legs summary: 20/20 legs passed != 19/19
```

The first two are the named tails. **The third is not**, and §3 shows it is the one
that decides whether the r4 checker can go green.

## 2. What the O seat landed, and the control on each claim

The O seat's own fragment is `reports/round-26/remainders/pins.md`, with the
machine-readable rows in `pins.json` and the bound checker
`reports/round-26/remainders/pin-repoint-check.py`. This seat re-measured rather
than inheriting.

### 2.1 The r4 twin — a new row, not a filed-byte edit (holds)

`reports/round-26/remainders/r4-twin/` carries `build-twin.py`, `expected.json`,
`twin.json`, `verify-twin.py`. The filed `reports/round-25/v3-supersession/declared-in-r4/`
directory is unchanged — `verify-twin.py` asserts this with its own
`filed-r25-r4-directory-untouched` and `twin-is-a-new-row-not-a-r25-write` controls,
and the round-26 runner's `revision_rows` census records `declared-in-r4` as still
`has_twin: false`. So the gap is dispositioned by an append, which is the filed
convention. The twin's own identity is pinned:

| surface | sha256 | command |
|---|---|---|
| `reports/round-26/remainders/r4-twin/twin.json` | `1874efbc1a6f892d035e47bbfbb8ca228622b26fd622a002ee822594a5420b95` | `sha256sum` (18:23:55Z) |
| `reports/round-26/remainders/r4-twin/expected.json` | `d02a9f2c9e07a0b6acf3e71f8bd18f9082c5202560e2389daa4fd0c9a5daaf90` | `sha256sum` (18:23:55Z) |

Its source packet pin (`5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03`)
matches the filed round-25 revision byte-for-byte, and the twin shape is the r22
sibling shape: `artifact_manifest` 58 / `claim_ledger` 27 / `coupling_edges` 88 /
`open_questions` 10.

**But the twin does not currently pass its own harness judge.** `tools/harness/packet_uncertainty.py`
is green over it (`exit 0`, `claims: 27`, `findings: []`, 18:24:08Z) while
`tools/harness/packet_links.py` is **red** (18:24:08Z):

```
links=106 resolved=106 findings=6
M-DIGEST-MISMATCH [examples/culture-d4/components/01-brief.yml] live sha256 feca7bda25beb6ec… != manifest a2bc3111b8e936d2…
M-DIGEST-MISMATCH [examples/culture-d4/components/04-lexicon.yml] live sha256 d0d4e17cc3c43a11… != manifest 74c2561b7c875c7c…
```

This is the same cause as §2.3 — the D seat's 18:18:32Z write to the D4 tree. The
twin pins the **r4 packet's** manifest digests, which describe the D4 tree as it
stood when the r4 revision was built; the live tree has moved since. The round-26
runner surfaces exactly this (`claim O: twin: reports/round-26/remainders/r4-twin:
tools/harness/packet_links.py is not green over the twin (exit 1)`).

### 2.2 The v2 successor pin — re-pointed, replays green (holds)

`reports/round-26/remainders/v2-successor-r26/expected.json` (`f695b910699ab5310b0853fe38471b7714616973f7deff366e1298888b766bc3`, 18:23:55Z)
is produced by the tail's own filed freezer, `reports/round-15/handoff/frozen-verify.py --freeze`.
Its replay is green:

```
frozen-v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15
statuses={'supported': 8, 'unresolved': 2, 'partial': 5} links=50/50
packet_sha256=24f9dd39bdad…
```
(18:24:08Z, exit 0)

The row differs from its filed predecessor in **exactly two values** — the moved
input `tools/d2-typed-labels.py` (`76536a92…` → `2819f687…`) and the derived
`baseline_digest` (`44b3c299…` → `803ec02f…`) — which this seat confirmed by a
sorted-key `diff` of the two JSON documents, not by reading the seat's claim. The
filed round-20 row is byte-identical (`ad761a61c0c3be068c54c382ce43c88978a6c0c2a0f7493bb46a15063e2ebd04`,
re-measured 18:01:14Z and again at close).

### 2.3 The v3 packet-baseline pin — re-pointed, then invalidated within ~3 minutes (fails)

This is the review's most consequential reading, and it is a **moving-target**
finding rather than a defect in the seat's method.

`reports/round-26/remainders/v3-baseline-r26/` carries the full five-file shape
(`expected.json`, `packet.md`, `twin.json`, `freeze.txt`, `run.log`). Its
`freeze.txt` pins packet `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e`
and twin `d3de56a8be1d28fdcead751aa0ac9364f7b43ff2b8bad71b696f0b57955b4d5c`; both
digests re-verify against the filed bytes (`sha256sum`, 18:05:41Z). Its replay:

| stamp | command | exit | observed |
|---|---|---:|---|
| 18:16Z (this seat) | `python3 tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-26/remainders/v3-baseline-r26/expected.json` | **0** | `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=a97a0f0a0a49…` |
| 18:19:16Z (this seat) | same command | **1** | `handoff-v3: E2E-DIGEST: 6 read-set file(s) changed since the baseline was frozen: examples/culture-d4/components/01-brief.yml, examples/culture-d4/components/04-lexicon.yml, examples/culture-d4/expected-holds.json, …` |

**Cause, measured not inferred.** `git status --porcelain` at 18:19Z lists
`M examples/culture-d4/{components/01-brief.yml,components/04-lexicon.yml,expected-holds.json,packet.d4.typed.yml,packet.d4.yml,typed-labels.d4.yml}`
and `M tools/gates/typed-pipelines.json`; `ls --time-style=full-iso` puts every one
of those six files at **2026-10-18 15:18:32 −03:00** (= 18:18:32Z). The D seat
landed the register stratum into the D4 tree at that stamp, which is *after* the
O seat froze the v3 row (18:04–18:05Z) and *after* this seat's first green replay.

The consequence is that the O seat's own bound checker is red on its own fix:
`python3 reports/round-26/remainders/pin-repoint-check.py --check` → **exit 1,
16/17 controls**, the failing control being `new-v3-row-replays-green` with
`exit: 1` and the `E2E-DIGEST` stdout quoted above (18:19Z and again 18:24:08Z).

This is not a claim that the seat froze a row it had not measured — it did measure
it, and this seat reproduced the green. It is the statement that **any pin over
`examples/culture-d4/` is invalidated the moment the D claim lands**, and the D
claim landed. The round-26 runner records the same cascade:
`claim O: Regression failed: python3 tools/exercise-handoff-e2e.py --profile v3 --quiet (exit 1, 2026-10-18)`.

**The target is still moving at this review's close.** At 18:26:58Z
`examples/culture-d4/packet.d4.yml` carries mtime **2026-10-18 15:25:23 −03:00**
(= 18:25:23Z) — a *second* D-seat write, ~7 minutes after the first — and the
replay is red again on the same command (`E2E-DIGEST: 6 read-set file(s) changed`,
exit 1, 18:26:58Z). So the v3 row's staleness is not a one-off: it is the steady
state while the D claim's register stratum is being landed, and re-pointing it
before that work stops would only schedule another invalidation.

## 3. The decisive control — the r4 checker's red is not the pin tails' red

The O claim's `after_required` ends "the r4 checker green". That checker is the
filed `reports/round-25/v3-supersession/v3-supersession-check.py`, whose controls
this review ran four ways. The variable in each arm is stated; nothing else was
touched.

| arm | construction | r4 checker result |
|---|---|---|
| **A — live lane** | clean clone at HEAD, no modification | **51/52, `passed: false`** |
| **B — rows placed** | both re-pointed rows copied to the frozen runner's *discovery* paths (`reports/round-20/wart/expected-v2-07-r26.json`, `reports/round-20/handoff/expected.json`) | **50/52, `passed: false`** |
| **C — pre-argot gate + rows placed** | as B, plus `git checkout e06581b -- tools/gates/typed-pipeline-gate.py examples/culture-d4/` | **51/52, `passed: false`** |
| **D — the checker's own declared baseline** | clean clone with `e06581b` gate + D4 tree + `reports/round-20/` + `reports/round-23/` restored | **52/52, `passed: true`** |

Each arm's receipt is under `.scratch/r26-o39/`: `r4-independent.json` (A),
`r4-maximal.json` (B), `r4-prefix.json` (C), `r4-frozenroot.json` (D).

**What the arms prove.** Arm D reproduces the round-25 filed receipt exactly —
`52/52 passed`, matching `reports/round-25/v3-supersession/evidence/check-receipt.json`
(`2026-10-18T17:38:40Z`, `passed: True`, `52/52`). So the checker is sound *at the
baseline it declares*, and this seat's harness is faithful. Arm C shows the two
pin tails are **no longer the blocker**: with the rows placed, the positive run
reports **zero** failures, and the only failing control is
`negative-control-carries-declared-open-tails`, whose assertion is
`len([failure for failure in negative_failures if failure.startswith(OPEN_TAIL_V2_ROW) or failure.startswith(OPEN_TAIL_V3_PIN)]) == 2`
(`v3-supersession-check.py:489-493`) — i.e. it demands that the *negative* arm
still carry exactly two tails, and re-pointing them removes both.

Arm B, at the live gate, adds back a single failure in both the positive and the
negative run:

```
claim O: D4 gate legs summary: 20/20 legs passed != 19/19
```

**So the r4 checker's remaining red is produced by the round-26 D seat's `L3b-argot`
leg, not by either remainder this claim owns.** The mechanism is exact:
`reports/round-20/run-validation.py:1119` hard-codes
`elif (int(gate_scan.group(1)), int(gate_scan.group(2))) != (19, 19)`, while
`tools/gates/typed-pipeline-gate.py` now prints `summary: 20/20 legs passed`
(`ok L3b-argot`, `:517-541`). The transition is visible in the git objects:

| revision | `typed-pipeline-gate.py` sha256 | argot leg | D4 legs |
|---|---|---|---|
| `e06581b` (round-24 close, the checker's declared baseline) | `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48` | absent | 19/19 |
| `fc13cd2` (round-25 admit) | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | present | 20/20 |
| HEAD `1ad491a` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | present | 20/20 |

and round-25's own record already named it: `reports/round-25/argot/impl-6.md:32`
("`20/20 legs passed` (was 19/19)"), `reports/round-25/audit/o18-gate-input-adversarial.md:23`
("D4 source 19/19 → **20/20**").

**This makes "the r4 checker green" unreachable by the pin re-point.** Rounds 8–25
are locked, so the hard-coded `19, 19` cannot be corrected in place; and the
checker's `negative-control-carries-declared-open-tails` control *requires* the
tails to still be red in the negative arm, so a successful re-point is what turns
that control off. The two clauses pull in opposite directions once a third,
foreign failure exists. The O seat's own `pins.md` reached the same conclusion
independently and said so rather than absorbing it:

> "The `20/20 != 19/19` gate-legs reading is not this seat's tail. … Reported, not
> absorbed." (`reports/round-26/remainders/pins.md`, §4)

This review confirms that statement by construction, not by quotation.

## 4. The round-26 runner cannot evaluate the checker it depends on

`reports/round-26/run-validation.py:1172` invokes the r4 checker as

```python
checker = run_command("r4-checker", (R4_CHECKER, "--root",
                                     f"{ROUND_DIR}/../.scratch/round-26/checker-clone",
                                     "--check"), timeout=1800)
```

Measured (18:21:10Z, and again at 18:14Z): that path does not exist, so the
checker exits **2** with
`v3-supersession-check.py: error: --root must be an isolated clone with .git under the lane's .scratch`
(`v3-supersession-check.py:568`). The runner handles this by *recording* it:

```python
if checker.get("exit") not in (0, 1):
    measurement["r4_checker"]["note"] = (
        "the round-25 r4 checker needs its own isolated clone under the lane's .scratch; "
        "… a non-{0,1} exit means it could not evaluate in this location")
```

so `r4_checker` in the receipt carries `exit: 2` and **no `passed` key at all**, and
no failure is raised. The O claim's stated requirement — "a checker bound to the
re-pointed rows is green" — is therefore **not measured by the round-26 runner**;
it is skipped silently in the sense that matters (the receipt has no verdict), even
though the skip is documented in the note. A consumer reading only
`claims.O.passed` cannot see that the checker was never evaluated.

The round-26 runner does read the checker's *failures* when it can (`payload.get("positive")`),
and it has a successor path: `measure_pin_tails` accepts a round-26 JSON row that
names each tail and pins the live digest, which `pin-repoint-check.py` supplies.
But that successor is itself red on the v3 tail (§2.3).

## 5. Consolidated state of the round-26 runner

`python3 reports/round-26/run-validation.py --check` (18:21:10Z, exit 1):

| claim | passed | failures |
|---|---|---|
| **C** | **true** | none |
| **D** | **true** | none |
| **O** | **false** | 2 |

The two O failures, verbatim:

```
claim O: twin: reports/round-26/remainders/r4-twin: tools/harness/packet_links.py is not green over the twin (exit 1)
claim O: Regression failed: python3 tools/exercise-handoff-e2e.py --profile v3 --quiet (exit 1, 2026-10-18)
```

Both trace to the 18:18:32Z `examples/culture-d4/` write. Note the timing: an
earlier run of the same runner (18:14Z) read **D fail** with four register-stratum
failures ("the D4 contract's lexicon record_fields do not declare the derivation
relation", "the register-scoped derivation domain is still empty") — the D seat's
work landed between the two stamps and turned D green. The runner is measuring a
live wave.

## 6. What holds, what does not, and what the parent must decide

**Holds (measured by this seat, independently of the O seat's own receipts):**

1. The append-only convention: all three dispositions are **new rows**; the filed
   `declared-in-r4/` directory, `reports/round-20/wart/expected-v2-07-r20.json` and
   `reports/round-20/handoff/expected.json` are byte-identical to the baseline
   revision.
2. Each remainder reproduces red pre-fix and has a control that fires in the
   negative direction (§1).
3. The v2 successor row replays green and differs from its predecessor in exactly
   the two declared values (§2.2).
4. The r4 twin is a new row that preserves the r4 packet's bytes and pins its own
   digest; `packet_uncertainty.py` is green over it (§2.1).
5. The r4 checker reproduces its filed 52/52 at its own declared baseline (§3, arm D).
6. **The r4-twin verifier is 24/24 green at the read set its packet pins** (§6.1).

### 6.1 The r4-twin verifier, run four ways

`reports/round-26/remainders/r4-twin/verify-twin.py --check` is the twin's own
bound checker. It has two independent inputs — `--root` (where the twin is judged)
and `--source-root` (the read set the r4 packet's manifest pins) — and this seat
varied both, because the default couples them to a live tree a concurrent seat is
rewriting. All four runs at 24 controls each:

| arm | `--root` | `--source-root` / `--frozen-root` | result |
|---|---|---|---:|
| live (default) | live clone | default (= root) | **19/24, false** |
| pinned read set | live clone | `e06581b` D4 tree | **23/24, false** |
| pinned read set + pinned frozen root | live clone | as above, `--frozen-root` too | **24/24, true** |
| live | — | — | see below |

Receipts: `.scratch/r26-o39/twin-check.json` (live, 18:27:45Z),
`twin-frozen.json` (18:31:03Z), `twin-frozen2.json` (18:34:41Z), `twin-prefix.json`
(18:38:06Z, **exit 0**).

**What the arms separate.** The live arm's five failures are all downstream of the
18:18:32Z / 18:25:23Z D4 writes: `twin-is-re-derived-from-the-packet` and both
`reproduces-filed-twin:` controls fail because the builder re-derives from a tree
whose `examples/culture-d4/packet.d4.yml` no longer hashes to the manifest's
`e7ecd2045ef0e5f9…` (live `dd25077bc01681bc…`, 18:27Z) — and indeed the verifier
*refuses* to run at all against a mismatched source root, printing
`build-twin: source examples/culture-d4/packet.d4.yml is dd25077bc01681bc… but the
packet pins A-28 at e7ecd2045ef0e5f9… — pass --source-root at the pinned read set`.
At the pinned read set every rebuild and reproduction control passes, and the
residual `frozen-uncertainty-judge-green` failure in the third arm is an
`--require-oq` invocation against a clone whose live tree had moved again mid-run
(it is green in the fourth arm, and green when run directly: `claims=27 findings=0`,
exit 0, 18:28Z). The only control that survives every arm is
`frozen-r25-r4-checker-still-green`, which asserts `r25["passed"] is True`
(`verify-twin.py:272`) — i.e. it inherits §3's cross-claim red.

So the twin, its builder and its verifier are **sound at the read set they declare**;
what is red is everything that re-measures a live `examples/culture-d4/` while the D
claim is landing.

**Does not hold at this stamp:**

7. "The r4 checker green" — unreachable while the D seat's 20-leg gate is live, and
   structurally opposed to the re-point's success by the checker's own negative-arm
   control (§3).
8. "Regressions green" — `exercise-handoff-e2e.py --profile v3 --quiet` exits 1,
   and `pin-repoint-check.py --check` is 16/17 (§2.3, §5).
9. The round-26 runner's r4-checker leg evaluates nothing and reports no verdict (§4).

**For the parent, not for this seat.** Three routes are visible and this review
does not choose among them, because each trades away something the claim text asks
for: (a) re-point the v3 row again *after* the D seat's writes settle — which fixes
§8 but leaves §7 and §9; (b) accept the r4 checker as bound to its own declared
baseline (arm D, 52/52) and grade the round-26 pin rows with the successor checker
instead — which requires the claim's "the r4 checker green" to be read as
"green at its declared baseline", a reading the filed receipt supports but the
claim text does not state; (c) rule that the D seat's gate-leg change is itself a
re-pin event that owes a successor row for `reports/round-20/run-validation.py`'s
hard-coded expectation — which is a D-claim obligation, not an O one. The same
choice recurs for the twin verifier: its 24/24 depends on passing `--source-root`
at the pinned read set, and nothing in the round-26 runner's regression inventory
does so.

## 7. Limits

- **This is not round acceptance.** This review measures the O claim's remainder
  fixes against their `after_required` text at the stamps named. It does not
  adjudicate D or C, does not run the round validator as an authority, and does not
  certify any pin.
- **The wave was live throughout, and two of the findings are consequences of
  that.** Every reading is bound to a stamp; §2.3 and §5 changed *within this
  window* (the v3 row was green at 18:16Z and red at 18:19Z; D was red at 18:14Z and
  green at 18:21Z). A consumer must re-run rather than inherit, and any reading
  taken before 18:18:32Z is false of the current tree.
- **The r4 checker is a frozen instrument and this seat did not modify it.** All
  four arms ran it as filed, in isolated clones, under `.scratch`.
- **The `negative-control-carries-declared-open-tails` reading in arm C is a
  two-sided result and should be read as such.** It is not a defect in the checker:
  that control exists precisely to assert that the tails are *still* open in the
  negative arm. Its failure in arm C is the checker correctly observing that the
  tails are no longer red — which is what the fix was for. The control is
  constructed for a world where the tails are the only red, and that world ended
  when the argot leg landed.
- **The r4-twin verifier was run to completion four ways** (§6.1): 19/24 live,
  23/24 at the pinned read set, **24/24 with `--frozen-root` also pinned** (exit 0,
  18:38:06Z). Its green is conditional on being given the read set its packet pins;
  the live-tree default cannot be green while `examples/culture-d4/` is being
  rewritten, and this review does not claim the default is the intended invocation.
- **The `examples/culture-d4/` surface moved at least twice inside this window**
  (18:18:32Z and 18:25:23Z). Every red this review attributes to that surface is
  bound to a stamp *after* the relevant write; a reading taken before 18:18:32Z is
  false of the current tree, and one taken after 18:25:23Z may be false again.
