# CritAnchoring — O2 anchoring attack (round 69, attempt 2)

Seat: critic, residual verification call. Target: `reports/round-69/accept-o.py`
(revision 1, committed at `52b92a6`), lane tip `9e82c7b`.
Sandbox: `git clone -q … /tmp/CritAnchoring-r69`; all mutations on copies
under `/tmp/adv`, never in the lane. Lane writes: this file only.

## Verdict — two sentences that must not be collapsed

1. **Frozen predicate: PASS.** On the untouched lane, the canonical command
   prints `ACCEPT-O-69: PASS legs=7/7` and exits 0; the counter's sha256 is
   `08c7ea6149a0212a6ccee7de62a9f5ef2a4efb197235b1586e4b7b91822f7547`,
   identical to the sha recorded in `reports/round-69/telemetry/final-measures-o.txt:1`.
   The claim's stored target (`claims.json` O2 `target: "7/7 legs PASS"`) is met.

2. **The anchoring property the counter is sold on: FAIL.** The docstring states
   "**no leg now trusts the harness's self-report**" and "the spoof that killed
   revision 0 **now fails NEGPROBE**" (`reports/round-69/accept-o.py:15-21`).
   NEGPROBE still adjudicates a harness self-report, and a no-op harness — the
   same rev-0 spoof with **one word changed** (`missing_paths=0` → `missing_paths=1`)
   — reaches `ACCEPT-O-69: PASS 7/7`. So does a harness that prints
   `FAIL` for all three of its own fixtures and exits 2, and so does a checker
   that never opens a used-by path. Four trees that do none of the claimed work
   score identically to the real one.

The record texts do not overstate what was run (`SCORECARD.md:1330`,
`telemetry/controls-rev1.txt` say 7/7 / 5/7 / 6/7, all literally reproduced).
The defect is **discriminating power**, not false provenance. The claim does not
need a withdrawal; it needs the two corrections in F1 and F2 before it can be
used as a gate again.

## 1. Leg by leg — the exact bytes adjudicated, and what each would accept

| Leg | `accept-o.py` lines | Bytes adjudicated | Accepts |
|---|---|---|---|
| STAMP | 168-172 | sha256(running `__file__`) vs sha256(`<root>/reports/round-69/accept-o.py`) | the two hashes equal. Does **not** read any receipt. |
| TOOL | 181 | `os.path.exists(<root>/tools/check-settlement-fixture.py)` | any existing filesystem entry: empty file, 0-byte, a directory. Never executed here. |
| FIXTURE | 183-195 | `<root>/tools/check-supersession-settlement.py --scan --root <counter-built green fixture>`; stdout matched by `SUMMARY_RE`, plus exit code | `rc==0 and pending==0 and missing_paths==0` on a 2-row registry whose used-by file exists. |
| NEGCASE | 196-207 | same checker on `<root>`-side negative fixture (`create_usedby=False`) | `summary present and pending==0 and missing_paths==1`. **`rc` is computed and printed but not in the predicate** (203). |
| LANE | 208-215 | same checker on `<root>` itself | `rc==0 and pending==0 and missing_paths==0`. Observed on the lane: `pending=0 chains=47 usedby_paths=711 missing_paths=0` — non-vacuous in the green direction. |
| NEGPROBE | 216-231 | `<root>/tools/check-settlement-fixture.py --root <counter-built negative fixture>`; **only stdout lines starting `LANE:`** | at least one `LANE:` line containing the substring `missing_paths=1`. **`rc` (227) and the harness's `FIXTURE:`/per-case lines are read into the detail string and never tested.** |
| R68FROZEN | 238-248 | sha256(`<root>/reports/round-68/accept-{o,ca,c}.py`) vs the `# counter sha256 (self): <64hex>` line in `<root>/reports/round-68/telemetry/final-measures-*.txt` | all three pairs equal. Both sides are mutable text in the same tree. |

Two structural facts that drive the findings below:

* The negative fixture differs from the green one in **two** bits, not one:
  `write_fixture` only creates `corpus/knowledge/` inside `if create_usedby:`
  (`accept-o.py:117,120-126`), so the negative tree is `corpus/SOURCES.md`
  alone. Verified:
  `green ['corpus/SOURCES.md','corpus/knowledge/a.md'] dirs=['corpus','corpus/knowledge']`
  vs `negative ['corpus/SOURCES.md'] dirs=['corpus']`.
* NEGPROBE's harness resolves its own checker relative to itself
  (`tools/check-settlement-fixture.py:154-157`, `LANE = dirname(HERE)`), so
  FIXTURE/NEGCASE/LANE and NEGPROBE all reduce to the **same** file
  `<root>/tools/check-supersession-settlement.py` and to two 2-row fixtures.

## 2. Constructions and their exact outputs

Harness replacement used for A/A2 (a `sys.exit` differs only in A2):

```python
#!/usr/bin/env python3
import sys
print("PASS fixture-green rc=0 pending=0 missing_paths=0")
print("PASS fixture-negative rc=1 pending=0 missing_paths=1")
print("PASS fixture-pending rc=1 pending=1 missing_paths=0")
print("FIXTURE: 3/3")
print("LANE: pending=0 missing_paths=1")
sys.exit(1)          # A2: sys.exit(0)
```

It never reads `--root`, never spawns the checker, never creates a fixture.

**A — no-op harness, exit 1 (wrong rc for its own claimed green case):**

```
LEG PASS STAMP     self=08c7ea6149a0 committed=08c7ea6149a0
LEG PASS TOOL      tools/check-settlement-fixture.py
LEG PASS FIXTURE   rc=0 pending=0 missing_paths=0
LEG PASS NEGCASE   rc=0 pending=0 missing_paths=1
LEG PASS LANE      rc=0 pending=0 missing_paths=0
LEG PASS NEGPROBE  harness_on_counter_fixture rc=1 lane_lines=['LANE: pending=0 missing_paths=1']
LEG PASS R68FROZEN mismatched=none
VERDICT: ACCEPT-O-69: PASS legs=7/7
```

**A2 — identical harness, exit 0:** same seven PASS lines, `NEGPROBE … rc=0 …`,
`PASS 7/7`. The exit code is invisible to the leg, so "returns the wrong rc" is
not a discriminator at all.

**A3 — control: the frozen rev-0 `SPOOF_HARNESS` (`accept-o.py:81-89`) reproduced
verbatim, for the record:** `LEG FAIL NEGPROBE … lane_lines=['LANE: pending=0 missing_paths=0']`,
`ACCEPT-O-69: FAIL legs=6/7`. Matches `controls-rev1.txt` exactly. Rev 1 killed
**this literal**, not **this class**.

**A4 — harness that admits total failure, exit 2:**

```python
print("FAIL fixture-green rc=1 pending=0 missing_paths=0")
print("FAIL fixture-negative rc=0 pending=0 missing_paths=0")
print("FAIL fixture-pending rc=0 pending=0 missing_paths=0")
print("FIXTURE: 0/3")
print("LANE: pending=0 missing_paths=1")
sys.exit(2)
```

```
LEG PASS NEGPROBE  harness_on_counter_fixture rc=2 lane_lines=['LANE: pending=0 missing_paths=1']
VERDICT: ACCEPT-O-69: PASS legs=7/7
```

The counter never reads `FIXTURE:`, `fixture-green`, `fixture-negative`, or
`fixture-pending`. A harness may print any verdict it likes for the three cases
it was built for; only the `LANE:` substring counts.

**B — NEGCASE passed for the wrong reason: a checker that never resolves a
used-by path.** One-line replacement of `tools/check-supersession-settlement.py:164`:

```python
missing_paths = ([] if os.path.isdir(os.path.join(root, "corpus", "knowledge"))
                 else ["dir-proxy"])
```

This detects the *directory*, not the used-by file. Score:

```
LEG PASS FIXTURE   rc=0 pending=0 missing_paths=0
LEG PASS NEGCASE   rc=0 pending=0 missing_paths=1
LEG PASS LANE      rc=0 pending=0 missing_paths=0
LEG PASS NEGPROBE  harness_on_counter_fixture rc=1 lane_lines=['LANE: pending=0 missing_paths=1']
VERDICT: ACCEPT-O-69: PASS legs=7/7
```

and its false negative on the actual R68-M1 defect class (directory present,
used-by file absent):

```
false-negative probe (mutated): rc=0 ['SETTLEMENT: pending=0 chains=1 usedby_paths=1 missing_paths=0']
false-negative probe (real):    rc=0 ['SETTLEMENT: pending=0 chains=1 usedby_paths=1 missing_paths=1']
```

A detector that cannot see the class the round is named after scores 7/7,
because the only negative fixture also removes the directory.

**B2 — NEGCASE tolerates an unrelated crash.** Replace the checker's final
`return 1 if pending else 0` (`:167`) with `raise RuntimeError(...)`:

```
LEG FAIL FIXTURE   rc=1 …
LEG PASS NEGCASE   rc=1 pending=0 missing_paths=1
LEG FAIL LANE      rc=1 …
VERDICT: ACCEPT-O-69: FAIL legs=5/7
```

Per-leg: NEGCASE passes with `rc=1` from an unrelated exception. The counter as
a whole still fails (FIXTURE/LANE require rc=0), so this is a leg-level, not
claim-level, weakness — recorded for completeness, not as a claim falsifier.

## 3. Mutation matrix (what notices a broken scan)

| Mutation | Legs that fire | Verdict |
|---|---|---|
| M1 delete used-by detection (always `missing_paths=0`) | NEGCASE, NEGPROBE | FAIL 5/7 — caught |
| M2 lane scan returns 0 unconditionally (`:167` → `return 0`) | none | **PASS 7/7** — uncaught (the lane is already `pending=0`, so the leg is insensitive) |
| M3 pending detection deleted (`pending = []`) | none | **PASS 7/7** — uncaught |
| B dir-proxy detector | none | **PASS 7/7** — uncaught |
| A/A2/A4 harness replaced by a constant printer | none | **PASS 7/7** — uncaught |
| amend `accept-c.py` **and** its receipt line | none (`R68FROZEN` green) | **PASS 7/7** — uncaught |
| amend `accept-o.py` then run canonically (`--root .`) | none (`STAMP` green, both sides `e70646dfe99d`) | **PASS 7/7** — uncaught |

## 4. Findings

**F1 — NEGPROBE is a self-report leg, and its predicate is a constant
(`accept-o.py:224-227`).** `caught = any("missing_paths=1" in l ...)`, then
`ok = bool(lane_lines) and caught`. The harness's exit code is never part of
`ok`; nor is any comparison of the harness's answer to the base checker's own
answer on the same fixture, nor any second fixture. Consequence: every constant
printer whose output contains `LANE: … missing_paths=1` passes, including one
that declares `FIXTURE: 0/3` and exits 2 (A4). Axes: false provenance
(the docstring's "no leg now trusts the harness's self-report"), premature
saturation (the rev-0 attack is treated as closed by a one-literal patch).

Smallest safe correction: make the harness leg **differential and
cross-checked**, using fixtures the counter already builds:
`h_green = harness(green_fx)` must contain `LANE: … missing_paths=0` **and**
`h_neg = harness(negative_fx)` must contain `missing_paths=1`; require each
harness rc to equal the base checker's rc on the same fixture; and require the
harness's `missing_paths` to equal the counter's own `summary()` of the base
checker on that same fixture (two independent computations agreeing, instead of
one output matching a constant). A constant printer cannot satisfy green and
negative simultaneously, and cannot agree with a checker it does not call.
Cheapest alternative that keeps the 7-leg count: keep NEGPROBE but add the
green run and the rc equality to the same leg.

**F2 — the negative fixture under-determines the defect (`accept-o.py:115-126`,
used at `:201` and `:221`).** `create_usedby=False` removes `corpus/knowledge/`
as well as `a.md`, so any predicate keyed on the directory satisfies FIXTURE,
NEGCASE, LANE and NEGPROBE at once (B, 7/7, with the real defect class reported
as `missing_paths=0`). Axes: duplicate authority (all four legs collapse onto
one file plus one distinguishing bit), hidden regression reachable through the
fixture.

Smallest safe correction: always `os.makedirs(corpus/knowledge)` in
`write_fixture`, and in the negative case materialize the directory and omit
only `a.md`. Then the green/negative pair isolates exactly one bit — the
existence of the named used-by path — and the dir-proxy detector reports
`missing_paths=0` on the negative case → NEGCASE FAIL. (Optional, same edit:
a third case whose used-by names an existing *directory*, which the current
checker would call present — that is a separate base-checker question, not
needed to close F2.)

**F3 — no leg ever requires a positive result
(`accept-o.py:183-215`).** FIXTURE requires `pending==0`, NEGCASE requires
`pending==0`, LANE requires `pending==0`. The harness's own pending case
(`tools/check-settlement-fixture.py:138`, `rc==1 and pending==1`) exists but is
never read by any leg. A checker with `pending = []` passes 7/7 (M3), so the
counter cannot distinguish a settlement scanner from one that always says
settled. Smallest correction: add `PEND` using the already-supported
`write_fixture(..., unsettled=True)`: require `pending==1` and `rc==1` from the
counter's own run. This makes the leg set eight, which changes the frozen
leg count — so it belongs in the next declared revision, not this round.

**F4 — STAMP compares a file to itself under the canonical invocation
(`accept-o.py:169-170`).** `HERE = dirname(abspath(__file__))` and
`LANE = dirname(dirname(HERE))`, so with `--root .` from the lane,
`os.path.join(HERE, SELF)` and `os.path.join(root, "reports/round-69", SELF)`
are the same path. Both sides printed `e70646dfe99d` after I appended a
post-data amendment to the counter, and the run still returned `PASS 7/7`.
STAMP can only fire when the invoked script is not the one in `root`
(demonstrated: clone counter vs amended root → `LEG FAIL STAMP self=08c7ea6149a0
committed=e70646dfe99d`). Axes: identity change, false provenance — the leg
advertised as proof that "the counter under test is the committed one" proves
nothing in the only invocation the round ran. Smallest correction: derive the
expected sha from an independently recorded byte string — the
`# counter sha256 (self): 08c7ea…` line already present in
`reports/round-69/telemetry/final-measures-o.txt:1`, or `git cat-file blob
<measured-rev>:reports/round-69/accept-o.py` — and compare the live file to
that. Note neither is a perfect anchor (F5), but both are different bytes from
the ones being tested.

**F5 — R68FROZEN is text against text in the same tree (`accept-o.py:238-248`).**
`recorded_sha` reads a `# counter sha256 (self):` line out of the receipt, so
editing the counter and rewriting line 1 of its receipt keeps the leg green:
`LEG PASS R68FROZEN mismatched=none … ACCEPT-O-69: PASS legs=7/7`. It does
catch a unilateral amendment (the normal case), so it is not useless; it is not
an external anchor. Lower severity. Smallest correction: compare against
`git cat-file blob <measured-rev>:reports/round-68/accept-c.py`, or move the
three shas into `claims.json` (frozen at the declaration commit) and compare to
those.

**F6 — note, not a defect: NEGCASE cannot use `rc` (`accept-o.py:203`).** The
base checker's contract is `return 1 if pending else 0`
(`tools/check-supersession-settlement.py:167`); a missing used-by path never
changes rc (observed `rc=0` on the negative fixture). So the summary line is the
only channel, and the counter's omission of `rc` is correct. Recorded so that
the `rc=0` in the NEGCASE detail string is never later read as corroboration.

## 5. Residual reachability by a do-nothing control

| Leg | Reachable by a control that does nothing? |
|---|---|
| TOOL | yes — any existing file (A5 shows the leg's only discriminator is deletion) |
| STAMP | yes — tautological under `--root .` (F4) |
| FIXTURE | yes — any checker that reports `pending=0 missing=0` on a 2-row registry, including a wrong detector (B, M3) |
| NEGCASE | yes — any checker that reports `missing=1 pending=0` on a tree missing the directory; rc irrelevant (B) |
| LANE | yes — the lane is already all-settled; a broken detector reports `0` identically (B, M2) |
| NEGPROBE | yes — any executable printing `LANE: … missing_paths=1`; no fixture, no rc (A, A2, A4) |
| R68FROZEN | yes — a tree whose counter and receipt agree with each other (F5) |
| R68FROZEN (unilateral edit) | no — it does catch editing only one side |

Net: after revision 1, the counter proves — at best — "a checker file exists and
returns two particular summary lines on two two-row fixtures". It does not prove
that `tools/check-settlement-fixture.py` runs its three cases, and it does not
prove the checker resolves used-by paths. **The declared target "no
do-nothing/spoof control reaches it" is not met.** The frozen 7/7 target, read
literally, is met and honestly reported.

## Reproduction

```
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/CritAnchoring-r69
cd /tmp/CritAnchoring-r69
python3 -B reports/round-69/accept-o.py --root .          # PASS 7/7, exit 0
python3 -B reports/round-69/accept-o.py --selftest        # 3/3
python3 -B tools/check-supersession-settlement.py --scan --root .   # pending=0 chains=47 usedby_paths=711 missing_paths=0
```

Constructions: a driver imports `accept-o.py` as a module, calls
`build_fixture_root(fx, harness=…)`, substitutes one file (the harness, or
`fx/tools/check-supersession-settlement.py`), and calls `evaluate(fx, Result(quiet=True))`.
All fixture roots are `tempfile` trees; nothing outside `/tmp` was written except
this report.

Tool installs: none (nothing needed; `python3` stdlib only).
