# R27-X60 — shard audit: sweep completeness

- **Seat:** SCRIBE **X60** (shard auditor — sweep completeness), round 27
  (operator: loop 3 of 3, build 3 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high`).
- **Claim audited:** **O / operability** `pin-sweep` (`reports/round-27/claims.json`).
  Its `after_required` reads: "a single re-pin-and-verify sweep: every frozen
  manifest, battery baseline, expected-holds, and replay row that pins the D4
  surfaces re-verified against the amended packet; drifted rows re-pinned as NEW
  rows; battery 9/9, d4 gate (with register leg) green, all replays green."
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`claims.json:5`); lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- **Write scope:** `reports/round-27/audit/x60-sweep-completeness.py` and this
  file, plus gitignored scratch under `.scratch/x60/`. **No pin, manifest,
  freeze file, baseline, tool, gate, fixture, component, packet or filed
  round-8–26 byte was written**; no commit, no push. The replay mirrors were
  created under `/tmp` (outside the repo), per the tool's own requirement.
- **Canon:** NON-CANON engineering evidence. A coverage audit reports what a
  sweep reaches; it does not adjudicate the round.

## 0. Headline

**The sweep's surface is larger and more layered than a manifest replay reaches.
The round-27 O landing now covers it — the sibling X61 tool was revised twice
while this audit ran, and its final revision reaches every class.**

| # | finding | level |
|---|---|---|
| **X60-F1** | The pin surface is **eight classes**, not one: 11 frozen manifests, 16 gate baselines (6 under `expected/`, 10 under `frozen/`), 3 legacy baselines under `reports/round-9/baselines/`, 13 handoff baselines, 8 twin rows, 1 profile pin file, 9 fixture `.expected` files, 2 `expected-holds.json`. A manifest-only sweep reaches 11 of 81 rows and **0 of 19 baselines**. | coverage map |
| **X60-F2** | The round's usual replay leg (`tools/replay-frozen.py` over `**/MANIFEST.tsv`) **cannot evaluate a baseline at all** — it refuses one as `manifest_malformed`. A sweep that replays manifests and calls the surface clean has not looked at the baselines. | method limit |
| **X60-F3** | **The TMPDIR trap is real and now correctly reported.** `tools/replay-frozen.py` refuses a mirror inside the repo: `TMPDIR=$PWD/.scratch` turns all 6 rows of the round-26 post-register manifest into `mirror_unsafe` (exit 2), while an out-of-repo TMPDIR reproduces 4 and mismatches 2. An in-repo `TMPDIR` therefore makes a green manifest read as a red one. | measured both ways |
| **X60-F4** | The sibling `x61-pin-sweep.py` **was revised while this audit ran** (it gained the `frozen/` and `round-9/baselines/` roots, and its TMPDIR probe now passes its `tmpdir` through). Its first revision reached 6 of 16 baselines and its probe reported an inside-repo tally that its own code could not produce; the final revision reaches 19/19 and reports the real delta. | peer fix, verified |
| **X60-F5** | The D4 hold set moved to `857417e9…` and the D4 packet to `86079a67…`; the round-26 post-register manifest still replays **6/6 exit 0**, and the round-27 typed gate is green (`20/20` source, `17/17` typed). The battery is `exit 0, pass 7, fail 0, unevaluable 0`. | green at the recorded revision |

## 1. Why completeness, not verdicts

The O claim is a **coverage** claim ("every frozen manifest, battery baseline,
expected-holds, and replay row"). A coverage claim is only as strong as its
surface inventory, and the round's own runner measures the surface it chose to
measure. This audit answers the prior question: *how many pin surfaces exist, in
how many classes, and which does a given sweep method reach?* It replays nothing
itself — the round's runner and X61 own replay. Two independent instruments
answer the two halves; a disagreement between them is a reconciliation item.

**Instrument:** `reports/round-27/audit/x60-sweep-completeness.py` (new, this
seat's). Four duties: inventory, coverage matrix, D4-surface touch, TMPDIR
sensitivity. Twelve selftest checks, all passing:

```
$ python3 -B reports/round-27/audit/x60-sweep-completeness.py --selftest
selftest: 12/12 checks passed
```

The X61 rows of the coverage matrix are **read live from the sibling source**
(`x61_baseline_reach()` parses its `roots = [...]` line), not hardcoded. This
matters: a hardcoded snapshot of X61's first revision would have kept reporting a
defect that its own seat fixed mid-audit (X60-F4).

## 2. X60-F1 — the surface, by class

```
$ python3 -B reports/round-27/audit/x60-sweep-completeness.py
INVENTORY
  expected-holds       2
  fixture-expected     9
  frozen-baseline      10
  frozen-manifest      11
  gate-baseline        6
  handoff-baseline     13
  legacy-baseline      3
  profile-pin          1
  twin-row             8
```

| class | members | how discovered |
|---|---|---|
| frozen-manifest | 11 | `tools/gates/frozen/**/MANIFEST.tsv` |
| gate-baseline | 6 | `tools/gates/expected/**/expected.json` |
| frozen-baseline | 10 | `tools/gates/frozen/**/expected.json` |
| legacy-baseline | 3 | `reports/round-9/baselines/**/expected.json` |
| handoff-baseline | 13 | `reports/**/expected.json` carrying `packet_sha256` |
| twin-row | 8 | `reports/**/twin.json` carrying an `artifact_manifest` |
| profile-pin | 1 | `tools/gates/typed-pipelines.json` (the `d4` profile) |
| fixture-expected | 9 | `tools/gates/**/*.expected` |
| expected-holds | 2 | `examples/**/expected-holds.json` |

The three baseline roots are not arbitrary: `tools/check-gate-battery.py`
discovers `expected.json` under all three, which is why the battery can report
`pass 7` while a one-root baseline sweep reports "all pinned".

## 3. X60-F2/F3 — what each method reaches, and the TMPDIR trap

```
COVERAGE
  baseline-only-sweep        reaches=19  misses=11
  replay-frozen-manifests    reaches=11  misses=19
  x61-baseline-duty          reaches=19  misses=0
  x61-manifest-duty          reaches=11  misses=0
```

- **`replay-frozen-manifests`** (the round's usual leg) reaches every manifest and
  **no** baseline. Measured directly:

  ```
  $ python3 tools/replay-frozen.py reports/round-26/handoff/declared-in-r5/expected.json --json
  COULD-NOT-EVALUATE manifest_malformed: manifest: header must carry the documented
  columns [...] : got ['{']
  ```

  A baseline is not a manifest. The method is honest about what it evaluates; the
  reading to avoid is treating "all manifests green" as "all pins green".

- **`x61-baseline-duty`** (final revision) reaches 19/19 — see X60-F4.

**TMPDIR sensitivity, measured both ways** (the round-26 post-register manifest,
6 rows):

```
$ python3 -B reports/round-27/audit/x60-sweep-completeness.py --tmpdir-probe --json
inside-repo   /home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch
              {'could_not_evaluate': 6, 'exit': 2, 'mismatch': 0, 'reproduced': 0, 'rows': 6}
outside-repo  /var/tmp
              {'could_not_evaluate': 0, 'exit': 1, 'mismatch': 2, 'reproduced': 4, 'rows': 6}
```

The inside-repo row is not a defect in the manifest; it is the tool refusing to
run a gate from a mirror inside the tree under test. The practical consequence
for the round: **any sweep script that sets `TMPDIR=$PWD/.scratch` will read every
manifest as `mirror_unsafe`**, and a sweep that treats "could-not-evaluate" as
"not a failure" would silently skip the whole class. The O claim's counting
command must run with an out-of-repo `TMPDIR`, or its replay legs are vacuous.

## 4. X60-F4 — the peer tool moved, and the movement was verified

`reports/round-27/audit/x61-pin-sweep.py` was rewritten twice during this
window. The digests this audit observed:

| revision | sha256 | baselines reached | TMPDIR probe |
|---|---|---|---|
| first read | `c4cffc2b…` (81 lines, fragment) | — | — |
| second read | `c97e442a…` | 6 of 16 (`EXPECTED` only) | inside-repo tallied 6/6 reproduced |
| final read | (live) | 19 of 19 | inside-repo 6 `mirror_unsafe`, outside 4+2 |

Its final revision's own receipt, re-run by this seat:

```
$ TMPDIR=/tmp python3 -B reports/round-27/audit/x61-pin-sweep.py --json
summary: {"baselines": 19, "baselines_pinned": 19, "baselines_not_pinned": 0,
          "manifest_rows": 81, "manifests": 11, "rows_reproduced": 48,
          "rows_mismatched": 8, "rows_unevaluable": 25,
          "mismatch_supersession": 8, "mismatch_drift": 0,
          "gate_digest_mismatch": 25}
tmpdir_probe inside-repo:  6 could-not-evaluate, 6 mirror_unsafe, 0 reproduced
tmpdir_probe outside-repo: 4 reproduced, 2 mismatch
```

The `mismatch_supersession: 8 / mismatch_drift: 0` split is the right shape: a
mismatch whose live input has moved is a supersession (the pinned revision is
gone, the bytes moved on), not genuine drift. Both this seat's probe and X61's now
agree on the TMPDIR delta — two independent measurements of the same property.

**This is reported as a peer fix, not as this seat's work.** X61's own fragment
records the change and credits the naming of the completeness gap; this audit
independently verified the fix by reading its live source and re-running it.

## 5. X60-F5 — the D4 touch surface, at the recorded revision

D4-naming pin artifacts, and whether their pins hold (`--d4`):

| artifact | reading |
|---|---|
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | **6/6 pins hold** |
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | **6/6 pins hold** |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 2/2 pins hold |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 hold, `typed-pipeline-gate.py` stale (superseded) |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | **0 hold** — the X60-F1 defect of round 26, honestly refused |
| `tools/gates/expected/d4-{assembly,typed-labels}-check-gate/*` | gate pin holds, no stale inputs |
| `reports/round-26/register/v3-baseline-r26/expected.json` | packet pin `69ce3877…` (round-26 freeze) |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | packet pin `e3fb1ca5…` (round-27 freeze) |

Green at the recorded revision, from this seat's own commands:

```
$ python3 tools/check-gate-battery.py      → {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml       → summary: 20/20 legs passed
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml → summary: 17/17 legs passed
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
  coverage: … records=175 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
```

The round-25 gate-input generation remains byte-refused (0/6) — that is the
honest, named state round 26 left it in (its pin names a gate revision that was
never committed), and round 26's `post-register` generation supersedes it. This
audit confirms the refusal is stable and does not re-open it.

## 6. What this seat did *not* do

- It did **not** replay a pinned verdict as its own finding; the round's runner
  and X61 do that. It measured the surface and the methods' reach.
- It did **not** edit any pin, manifest, freeze file, baseline, tool, gate,
  fixture, component, packet or sibling fragment. The replay mirrors were created
  under `/tmp`, never in the tree.
- It did **not** claim X61's revision as its own work; it read the sibling's live
  source and re-ran it, and reports the fix as a peer fix.
- It did **not** run `reports/round-27/run-validation.py` as its verdict. It ran
  it once and reports the `protected_filed_artifacts` reading — `passed: true`,
  `protected_paths: 1460`, `differences_total: 0` — as the runner's own receipt,
  not as this audit's measurement.

## 7. Limits

- A receipt binds the bytes it was taken against. Every number above carries its
  command; the tree moved during this window (the packet digest went `dd25077b…`
  → `c5441e3d…` → `86079a67…`), so a re-run must re-take the digests.
- The coverage matrix describes **method reach**, not method correctness. A method
  that reaches a baseline and checks the wrong field would still show as
  reaching it.
- `x61_baseline_reach()` parses the sibling's `roots = [...]` line textually. If
  that line is reformatted, the parser falls back to `EXPECTED` only and says so
  in the note; the selftest asserts the fallback still yields a subset.
- The two HOLDs the X59 seat reports (`L6b`, `L9`) are properties of the register
  law, not of the pin surface; this fragment does not restate them.
- NON-CANON engineering evidence. No promotion, acceptance or clearance is
  claimed.

## 8. Reproduce

```sh
export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1   # OUTSIDE the repo
python3 -B reports/round-27/audit/x60-sweep-completeness.py --selftest   # 12/12
python3 -B reports/round-27/audit/x60-sweep-completeness.py              # inventory + coverage
python3 -B reports/round-27/audit/x60-sweep-completeness.py --d4         # D4 touch
python3 -B reports/round-27/audit/x60-sweep-completeness.py --tmpdir-probe --json
python3 -B reports/round-27/audit/x61-pin-sweep.py --json                # the peer sweep
python3 tools/check-gate-battery.py
```

Receipts (scratch, gitignored): `.scratch/x60/inventory.json`,
`.scratch/x60/tmpdir.json`, `.scratch/x60/battery.json`, `.scratch/x60/x61-final.json`.
