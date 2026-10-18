# R28-X60 — shard audit: sweep completeness

- **Seat:** SCRIBE **X60** (shard auditor — sweep completeness), round 28
  (operator: loop 3 of 3, build round 4 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high`).
- **Claim audited:** **O / operability** `pin-sweep` (`reports/round-28/claims.json`).
  Its `after_required` reads: "Final build-round sweep: every frozen/baseline/
  replay surface re-verified; drifted rows re-pinned as new rows; the v3 handoff
  baseline updated if its read set changed; battery 9/9; all replays green."
- **Date:** 2026-10-18. Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (`claims.json:5`); lane HEAD at this
  audit `69cecbc`.
- **Write scope:** `reports/round-28/audit/x60-sweep-completeness.py` and this
  file, plus gitignored scratch under `.scratch/x60/`. **No pin, manifest, freeze
  file, baseline, tool, gate, fixture, component, packet or filed round-8–27 byte
  was written**; no commit, no push. The TMPDIR probe mirrors nothing into the
  repo.
- **Canon:** NON-CANON engineering evidence. A coverage audit reports what a
  sweep reaches; it does not adjudicate the round.

## 0. Headline

**The O claim is a coverage claim, and the surface it must reach is now mapped
with a live read-set duty and a filed-surface duty that round 27 did not have.
The round-28 sweep seat's tool reaches every baseline class; the round's read set
is 14 rows drifted against the live packet; and one filed round-27 artifact was
rewritten in place during this round's window, then restored.**

| # | finding | level |
|---|---|---|
| **X60-F1** | The pin surface is **ten classes**, totalling **69 rows** at this seat's last census (it grew from 65 as the round-28 sweep seats landed new pin rows): 11 frozen manifests, 19 gate/frozen/legacy baselines, 14 handoff baselines, 9 twin rows, 9 fixture `.expected` files, 2 `expected-holds.json`, 1 profile pin, and 4 `pinsweep/baselines/` directories. A manifest-only sweep reaches 11 of those rows and **0 of 19 baselines**. (The round-27 precedent listed eight classes; the class set and the row total are both re-measured here rather than inherited, and the total is a dated reading — it moved 65 → 69 inside this window.) | coverage map |
| **X60-F2** | The usual replay leg (`tools/replay-frozen.py` over `**/MANIFEST.tsv`) **cannot evaluate a baseline at all** — a baseline is not a manifest. A sweep that replays manifests and calls the surface clean has not looked at the baselines. | method limit |
| **X60-F3** | The round-28 sweep seat's baseline duty reaches **19/19** baselines and its manifest duty reaches **11/11** manifests (`roots = [EXPECTED, FROZEN, ROOT / "reports" / "round-9" / "baselines"]`, read live from `reports/round-28/audit/x61-pin-sweep.py:330`). The method limit of X60-F2 is closed by that sibling. | peer tool, verified |
| **X60-F4** | **New duty, real reading: the packet read set.** 35 pin rows read the D4 packet or its projection; **14 are drifted** against the live `543d68a8…` packet — the whole v3 lineage (`declared-in-r5`, the round-26 `v3-baseline-r26` family, `round-27/pinsweep/v3-baseline-r27`) plus the round-11/15/20/22/23/25 handoffs and the round-26 `r4-twin`/`v2-successor-r26` rows. These are exactly the rows the RL-4 packet change moves; the round-28 sweep seat has begun re-pinning them (`reports/round-28/pinsweep/v3-baseline-r28/expected.json` now exists, and is itself in the read set). | measured, live |
| **X60-F5** | **New duty, real reading: a filed round-27 artifact was rewritten in place during round 28.** `reports/round-27/gate-tests/receipt.json` moved from green (exit 0, legs 17/20) to red (exit 2, legs 2) at 20:13:19Z — after the 20:10Z round-28 dispatch — then was restored to its baseline bytes. The round-28 runner independently reports the same divergence in its own `protected_filed_artifacts` block. | protected-surface breach (transient) |
| **X60-F6** | The TMPDIR trap is **currently masked by an upstream red**: `tools/replay-frozen.py` exits 2 both inside and outside the repo on the newest D4 manifest, because the recorded gate/input digests no longer match the amended packet. The in-repo/out-of-repo delta cannot be read while the manifest itself is red; this is disclosed rather than reported as a clean either/or. | measured both ways, both red |

## 1. Why completeness, not verdicts

The O claim is a **coverage** claim ("every frozen/baseline/replay surface"). A
coverage claim is only as strong as its surface inventory, and the round's own
runner measures the surface it chose to measure. This audit answers the prior
question: *how many pin surfaces exist, in how many classes, and which does a
given sweep method reach?* It replays nothing itself — the round's runner and the
sibling pin-sweep seat own replay. Two independent instruments answer the two
halves; a disagreement between them is a reconciliation item.

**Instrument:** `reports/round-28/audit/x60-sweep-completeness.py` (new, this
seat's). Six duties: inventory, coverage matrix, D4-surface touch, TMPDIR
sensitivity, packet read set, filed-surface integrity. Eleven selftest checks,
all passing:

```
$ python3 -B reports/round-28/audit/x60-sweep-completeness.py --selftest
inventory-returns-classes              ok classes=10
inventory-classes-are-lists            ok
coverage-has-methods                   ok methods=4
manifest-method-misses-baselines       ok misses=19
baseline-method-misses-manifests       ok misses=11
negative-empty-method-detected         ok
readset-has-live-packet                ok sha=543d68a82640e1b0
readset-counts-consistent              ok
tmpdir-probe-ran                       ok tools/gates/frozen/round-26/post-register/MANIFEST.tsv
filed-surface-ran                      ok modified=0
negative-tampered-pin-detected         ok
selftest: 11/11 checks passed
```

The sibling rows of the coverage matrix are **read live from the sibling source**
(`sibling_baseline_reach()` parses its `roots = [...]` line), not hardcoded. This
matters: a hardcoded snapshot of a first revision would keep reporting a defect
its own seat fixed.

## 2. X60-F1/F2/F3 — the surface, by class, and what each method reaches

```
$ python3 -B reports/round-28/audit/x60-sweep-completeness.py
INVENTORY
  expected-holds         2
  fixture-expected       9
  frozen-baseline        10
  frozen-manifest        11
  gate-baseline          6
  handoff-baseline       13
  legacy-baseline        3
  pinsweep-baseline-dir  2
  profile-pin            1
  twin-row               8
COVERAGE
  baseline-only-sweep        reaches=19 misses=11
  replay-frozen-manifests    reaches=11 misses=19
  sibling-baseline-duty      reaches=19 misses=0
  sibling-manifest-duty      reaches=11 misses=0
```

| class | members | how discovered |
|---|---|---|
| frozen-manifest | 11 | `tools/gates/frozen/**/MANIFEST.tsv` |
| gate-baseline | 6 | `tools/gates/expected/**/expected.json` |
| frozen-baseline | 10 | `tools/gates/frozen/**/expected.json` |
| legacy-baseline | 3 | `reports/round-9/baselines/**/expected.json` |
| handoff-baseline | 14 | `reports/**/expected.json` carrying `packet_sha256` |
| twin-row | 9 | `reports/**/twin.json` carrying an `artifact_manifest` |
| profile-pin | 1 | `tools/gates/typed-pipelines.json` (the `d4` profile) |
| fixture-expected | 9 | `tools/gates/**/*.expected` |
| expected-holds | 2 | `examples/**/expected-holds.json` |
| pinsweep-baseline-dir | 4 | `reports/round-*/pinsweep/baselines/*` (new this round) |

The table above is the last census this seat took (69 rows); the wave was live,
so the per-class counts are dated readings and grew during the window (65 → 69).
The three baseline roots are not arbitrary: `tools/check-gate-battery.py`
discovers `expected.json` under all three, which is why the battery can report
`pass 7` while a one-root baseline sweep reports "all pinned".

- **`replay-frozen-manifests`** (the round's usual leg) reaches every manifest and
  **no** baseline. A baseline is not a manifest; the method is honest about what
  it evaluates, and the reading to avoid is treating "all manifests green" as
  "all pins green".
- **`sibling-baseline-duty`** reaches 19/19 — the round-27 method limit is fixed
  by the round-28 sweep seat's tool.

## 3. X60-F4 — the packet read set: 35 rows, 14 drifted

New this round, because the RL-4 fix changes the packet surface again.

```
$ python3 -B reports/round-28/audit/x60-sweep-completeness.py --readset
READSET live_packet=543d68a82640e1b0 rows=35 drifted=14
  reports/round-11/handoff/expected.json                       holds=False
  reports/round-15/handoff/expected.json                       holds=False
  reports/round-20/handoff/expected.json                       holds=False
  reports/round-22/handoff/declared-in/expected.json           holds=False
  reports/round-22/handoff/declared-in-r2/expected.json        holds=False
  reports/round-23/wording/declared-in-r3/expected.json        holds=False
  reports/round-25/v3-supersession/declared-in-r4/expected.json holds=False
  reports/round-26/handoff/declared-in-r5/expected.json        holds=False
  reports/round-26/register/v3-baseline-r26/expected.json      holds=False
  reports/round-26/remainders/r4-twin/expected.json            holds=False
  reports/round-26/remainders/v2-successor-r26/expected.json   holds=False
  reports/round-26/remainders/v3-baseline-r26/expected.json    holds=False
  reports/round-27/pinsweep/v3-baseline-r27/expected.json      holds=False
  reports/round-28/pinsweep/v3-baseline-r28/expected.json      holds=False
  … (21 rows hold: the round-9 legacy baselines, the tools/gates/expected and
     frozen families, and the two round-27 pinsweep D4 baselines)
```

This is the read-set duty the O claim's "the v3 handoff baseline updated if its
read set changed" clause implies: a row whose `packet_sha256` no longer matches
the live packet is drifted and must be re-pinned as a NEW row, not overwritten.
The 14 drifted rows are the surface the round-28 sweep must account for. Note
that the round-28 successor row `pinsweep/v3-baseline-r28/expected.json` is
itself in the drifted set at this stamp — the round-28 sweep had begun landing
re-pin rows but had not yet re-pointed the v3 successor at the amended packet.

**The O verdict moved three times inside this window, and each is a dated
reading.** At `measured_at_utc 2026-10-18T20:13:51+00:00` claim O read red
(`8 D4 surface(s) drifted and no round-28 structured re-pin row landed`); at
`20:21:44Z` still red (`replay handoff-v3 is not green (exit 2)`;
`the v3 replay is red and no round-28 successor baseline replays green: the
re-point is missing, not merely unwired`); at `20:23:17Z` the receipt reads
**claim O green** with `missing_dependencies: []`. This seat's read-set duty
independently confirms the surface was real and the re-pin was the work: the
round-28 successor row exists and the drifted set is what the sweep had to
re-point. A reader who needs a *bound* verdict must re-run
`python3 reports/round-28/run-validation.py` and read its receipt, not this
fragment.

## 4. X60-F5 — a filed round-27 artifact was rewritten in place

Measured, then restored. At 20:13:19Z — after the 20:10Z round-28 dispatch —
`reports/round-27/gate-tests/receipt.json` differed from its dispatch baseline:

```
$ git diff 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede -- reports/round-27/gate-tests/receipt.json
- "date": "2026-10-18T20:04:10Z",
+ "date": "2026-10-18T20:13:19Z",
-   "exit": 0,  "legs": 17,  "failed_legs": [],
+   "exit": 2,  "legs": 2,   "failed_legs": [ … ]
```

The round-28 gate-tests runner correctly writes its own receipt at
`reports/round-28/gate-tests/receipt.json`, so this was not a path collision: the
round-27 runner also writes `HERE/receipt.json` (`reports/round-27/gate-tests/run-gate-tests.py:820`),
so a stray invocation of the round-27 runner is the likely mechanism. By the
close of this audit the file was back at its baseline bytes
(`git diff` over the protected range → empty; this seat's `--filed-surface` duty
reads `modified=0`), so the breach was **transient**.

**The round-28 runner independently reports the same divergence**, which is a
cross-check, not inheritance:

```
$ python3 -c "… reports/round-28/validation.json …"
protected_filed_artifacts: {"failures": ["Filed rounds 8-27 or their frozen
  generations differ from the declared baseline"], "measurement": {"differences":
  [{"baseline_blob": "854ed1a37805a7f848ca2d17e8f005a34788b592",
    "observed_blob": "fbc1f4b6c0fa1edbbde738cd7f801575079b881a14f25a1b94e684a35fd5a8f0",
    "path": "reports/round-27/gate-tests/receipt.json"}]}}
```

The runner's reading was taken at 20:13:51Z, inside the window in which the
receipt was red; this seat's reading is the working-tree diff at the same window.
The two agree on the path and on the fact of divergence. That the file was later
restored does not erase the reading: a filed artifact of an admitted round was
written in place during a later round, and the round-20 lesson ("a live-wave
receipt is a dated reading") applies in its sharpest form here — a re-run of a
filed round's own runner can overwrite that round's verdict.

## 5. X60-F6 — the TMPDIR trap, measured both ways (both red)

```
$ python3 -B reports/round-28/audit/x60-sweep-completeness.py --tmpdir-probe
TMPDIR
  inside-repo    exit=2 reproduced=None mismatched=None
  outside-repo   exit=2 reproduced=None mismatched=None
```

Both runs exit 2 on the newest D4 manifest
(`tools/gates/frozen/round-26/post-register/MANIFEST.tsv`), because the recorded
gate and input digests no longer match the amended packet — the manifest is
red for a reason that has nothing to do with TMPDIR. The round-27 X60 measured
the trap cleanly (`inside-repo` → `mirror_unsafe`, `outside-repo` → 4
reproduced / 2 mismatched); **that clean either/or cannot be read on this tree
while the manifest itself is red**, and this audit reports the masking rather
than forcing a false contrast.

## 6. The parent integrates

Filing, scope, integration into `LOG.md`/`SCORECARD.md`, the O-claim re-run, and
any final promotion verification remain parent responsibilities; in-lane
attestations do not prove a fresh external inspection.

## 7. Boundary record

- **Writes:** this file and its instrument
  `reports/round-28/audit/x60-sweep-completeness.py` (plus gitignored scratch
  under `.scratch/x60/`). No pin, manifest, baseline, freeze file, tool, gate,
  fixture, component, packet or filed round-8–27 byte was written; no shared
  bookkeeping was appended; no commit, no push.
- **Independence:** the census table and the coverage matrix were re-derived from
  the live tree by this instrument, not transcribed from the round's runner or a
  sibling fragment. The sibling rows are read live from the sibling source.
- **Canon:** NON-CANON engineering evidence. This audit admits nothing, certifies
  no round and adjudicates no claim.
