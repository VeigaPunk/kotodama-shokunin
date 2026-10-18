# R27-O37 — independent audit of the D4 pin-sweep inventory

- **Seat:** R27-O37 (sweep auditor 1 of 2), round 27, loop 3 build 3 of 4, claim
  **O** `pin-sweep` (`reports/round-27/claims.json`). Assignment: "independent
  re-verification of the sweep inventory (zero missed surfaces)."
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`;
  lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`. Measurements
  19:16–19:36Z.
- **Writes:** `reports/round-27/pinsweep/o37-sweep-inventory-audit.md`,
  `reports/round-27/audit/o37-sweep-inventory-audit.py`,
  `reports/round-27/pinsweep/o37-inventory-receipt.json` only. Scratch under
  `/var/tmp/`. No filed rounds 8–26 byte, no `tools/gates/**` byte, no sibling
  round-27 file written; no commit, no push.
- **Canon:** NON-CANON engineering audit. A pin is integrity, never truth and
  never clearance; a reproduced red verdict stays red. No design-quality claim.

## 0. Correction first: which instrument is "the sweep"

This seat's first pass measured the reach of `reports/round-27/audit/x61-pin-sweep.py`
and reported 20 D4-pinning surfaces "missed by the sweep". **That was the wrong
instrument.** X61 is an *audit* instrument (a peer's check); the **claim-O sweep
itself** is `reports/round-27/pinsweep/sweep.py` (seat `R27-O25..O32`), which
walks families **A–H** by its own docstring. Auditing the auditor instead of the
claimant is the error this section records, and both figures are now reported
separately so the distinction cannot be lost again:

| reach measured | instrument | D4-pinning surfaces reached | missed |
|---|---|---:|---:|
| audit instrument | `reports/round-27/audit/x61-pin-sweep.py` | 9 | 20 |
| **claim-O sweep** | **`reports/round-27/pinsweep/sweep.py`** | **24** | **5** |

Only the second row answers the claim. The corrected result is §2; §3 records the
X61 reach as a separate audit-instrument observation, because it is real but it
is not the claim's.

## 1. Method — the census is built here, from the tree

This seat authored none of the lane's filed round 8–26 artifacts. The instrument
`reports/round-27/audit/o37-sweep-inventory-audit.py`:

1. **Enumerates** every file class in the lane that can carry a digest pin, by
   walking the tree — eight families defined by the auditor, not inherited:

   | family | surface class | files |
   |---|---|---|
   | A | `tools/gates/frozen/**/MANIFEST.tsv` | 11 |
   | B | `tools/gates/expected/**/expected.json` | 6 |
   | C | `tools/gates/frozen/**/expected.json` + `reports/round-9/baselines/**/expected.json` | 13 |
   | D | `tools/gates/frozen/**/freeze-receipt.json` (embedded pin maps) | 4 |
   | E | `reports/**/expected.json` (handoff v2/v3 baselines) | 15 |
   | F | `tools/gates/typed-pipelines.json` (live L1-profile channel) | 1 |
   | G | `examples/**/expected-holds.json` (self-pins) | 2 |
   | H | `reports/**/twin.json` (embedded `artifact_manifest`) | 8 |

2. **Classifies** each as D4-pinning by its own test per family. The G test is
   digest-identity, not name-prefix: the D2 hold set's path shares a prefix but
   its pins are the D2 packet's, so a name test over-fires.

3. **Measures both reaches empirically** — it *runs* each instrument under a
   TMPDIR outside the repo and reads the surfaces each reports on. Reach is
   therefore measured, not parsed from prose: a glob a later edit changes cannot
   silently invalidate the figure, and a documented-but-unimplemented duty cannot
   inflate it. Each receipt names which method produced its reach.

## 2. The corrected result — the claim-O sweep misses 5 D4-pinning surfaces

`python3 -B reports/round-27/audit/o37-sweep-inventory-audit.py --json`
(2026-10-18T19:36Z, lane HEAD `b95fca1`, exit 1):

| measure | value |
|---|---|
| D4-pinning surfaces in this census | **29** |
| enumerated by the claim-O sweep | **24** |
| **missed by the claim-O sweep** | **5** |
| surfaces the claim sweep enumerates in total | 104 (34 named paths + 70 manifest rows) |
| claim sweep's own summary | `exit 1`, `findings 29`, `surfaces_enumerated 104` |

The 5 missed, and why each is or is not a defect:

| # | surface | family | why it is not enumerated |
|---|---|---|---|
| 1 | `examples/culture-d4/expected-holds.json` | G | **defect** — see §2.1 |
| 2 | `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | E | the sweep excludes its own round-27 outputs (`"round-27" in rel`) |
| 3 | `reports/round-27/pinsweep/v3-baseline-r27/twin.json` | H | same guard |
| 4 | `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/expected.json` | E | same guard |
| 5 | `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/expected.json` | E | same guard |

Items 2–5 are the sweep's own newly-frozen rows. Excluding them from its own
drift report is **defensible and arguably correct** — a sweep cannot re-verify
against its own output as if it were an independent surface — but it should be a
*filed* decision, not a silent `round-27` substring guard, because it also
excludes any future round-27 surface that is not the sweep's own. That is a
scope observation, not a defect.

### 2.1 The one real defect: family G enumerates nothing

`walk_holds()` is meant to cover the D4 hold set — the `packet_sha256` /
`projection_sha256` / `projector_sha256` self-pins. It returns **0 rows**. Root
cause, measured on the live file:

```
$ python3 -c "…read examples/culture-d4/expected-holds.json, evaluate the four guards…"
  holds mention culture-d4:            False
  supersedes_pins mention culture-d4:  False
  schema contains d4:                  False
  revision_note contains D4:           False
  -> any true? False  => row kept? False
```

All four of the classifier's guards evaluate **False** on the live D4 hold set,
so the single surface family G exists to cover is filtered out. The guards test
for the literal strings `culture-d4`, `d4`, and `D4`; the delivered file carries
the schema `kotodama-typed-pipeline-holds-v1`, a `supersedes_pins` map keyed by
`packet_sha256` (not by path), and a `revision_note` that spells the culture
"round-27 register-law build" without the token `D4`. **The D4 hold set is
distinguishable from the D2 one by its digest values, which is exactly the test
family G should have used** — and which this seat's own census does use.

Consequence: the sweep's family-G row is `0` surfaces, so the hold set's three
self-pins are never re-verified by the claim sweep. At the 19:36Z stamp those
three pins happen to **hold** against live bytes (`86079a67…`/`88a94422…`/
`2819f687…`), so nothing is currently red — but the claim's "every surface
re-verified" is not established for family G, and a future drift there would go
unreported.

**The sweep already knows.** Its own selftest has 8 controls; the one that
exists precisely to catch this **fails**:

```
$ python3 reports/round-27/pinsweep/sweep.py --selftest     # exit 1
  PASS d4-surfaces-declared            {'n': 8}
  PASS live-d4-reads                   {'missing': []}
  PASS selftest-tmpdir-outside-repo
  FAIL known-green-generation-replays  {'statuses': ['mismatch','mismatch','reproduced',...]}
  PASS known-drifted-generation-replays-red
  PASS manifest-walker-finds-d4-rows   {'d4_rows': 11}
  FAIL hold-walker-finds-the-committed-hold-set   {}
  PASS twin-walker-finds-the-r4-twin
  passed: False  6 / 8
```

So the defect is **honestly reported by its own control** — the tool exits 1 and
names the failing control. The claim should not be read as complete, but neither
should this be read as concealment. (`known-green-generation-replays` also fails:
it replays `round-26/post-register` expecting green, and that generation now
reports 2 mismatches because the D landing moved the bytes it pinned. That is a
stale expectation inside the sweep's control, not a second product defect.)

## 3. The X61 reach, reported separately

The audit instrument `reports/round-27/audit/x61-pin-sweep.py` enumerates 30
files and reaches families **A** (11/11 manifests) and **B/C** (13/13 battery
roots) only. It does not enumerate families D, E, F, G, or H, so 20 of the 29
D4-pinning surfaces are outside its reach. This is an **audit-instrument**
coverage statement — a peer's check is narrower than the claim sweep it checks —
and it is recorded here so the two reaches are never conflated.

An earlier pass of this seat also reported 4 "reach disagreements" between O37
and X61. Those were an artifact of comparing against a *stale filed receipt* of
this tool; after regenerating the receipt from the current instrument the
disagreements are 0. The receipt is regenerated on each run for that reason.

## 4. Independent re-verification of the missed surfaces (this seat's own runs)

Being missed is a coverage finding; whether it *matters* is a measurement. This
seat replayed each surface with the tool that owns it. All commands run
2026-10-18 from the lane root; `TMPDIR` outside the repo.

**E family — handoff baselines** (`tools/exercise-handoff-e2e.py --profile v3 --baseline <row>`):

| surface | exit at 19:29Z | verdict |
|---|---:|---|
| `reports/round-20/handoff/expected.json` | 1 | `E2E-DIGEST`: 7 read-set files changed |
| `reports/round-22/handoff/declared-in/expected.json` | 1 | `E2E-DIGEST`: 7 read-set files changed |
| `reports/round-22/handoff/declared-in-r2/expected.json` | 1 | `E2E-DIGEST`: 6 read-set files changed |
| `reports/round-26/remainders/v3-baseline-r26/expected.json` | 1 | `E2E-DIGEST`: 6 read-set files changed |
| `reports/round-26/register/v3-baseline-r26/expected.json` | 1 | `E2E-DIGEST`: 5 read-set files changed |
| `reports/round-26/handoff/declared-in-r5/expected.json` | 1 | `E2E-DIGEST`: 5 read-set files changed |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | 1 | `E2E-DIGEST`: 4 read-set files changed |

**H family — twin rows** (`tools/harness/packet_links.py --packet <twin> --json`):
7 of 7 red at 19:29Z (5–7 `M-DIGEST-MISMATCH` each).

**D / F / G** (digest comparison against live bytes at the same stamp):

| surface | pins | verdict |
|---|---|---|
| `round-26/post-register/freeze-receipt.json` | `packet.d4.yml`, `packet.d4.typed.yml` | drift |
| `tools/gates/typed-pipelines.json` (d4 profile) | packet, projection, adapter, assembler, expected | **all match live** |
| `examples/culture-d4/expected-holds.json` | `packet_sha256`, `projection_sha256`, `projector_sha256` | **all match live** |

**Movement note.** The D landing was writing D4 artifacts throughout this
window: the live `packet.d4.yml` moved `dd25077b…` → `c5441e3d…` → `86079a67…`.
At 19:19Z two E rows and two H rows were **green**; by 19:29Z all four were red.
Every figure above is stamped; a later reader must re-measure.

## 5. Controls

**Detector controls.** The classifier was exercised in-memory (`--selftest`,
3/3) and on the real tree:

| control | expected | observed |
|---|---|---|
| a `MANIFEST` row naming `examples/culture-d4/packet.d4.yml` | D4-pinning | yes (5 rows in family A) |
| `examples/culture-d2/expected-holds.json` (pins the **D2** packet) | not D4-pinning | correctly excluded — digest-identity, not name-prefix |
| the live D4 hold set | D4-pinning | correctly included (digest-identity) |
| a surface in the instrument's receipt | swept | yes |

**Reach controls.** Both reaches are taken from each instrument's own receipt on
each run. The X61 fallback path (static `rglob` read, used when it cannot run) is
labelled `source-rglob-fallback` in the receipt.

**The decisive control is the sweep's own selftest**: `hold-walker-finds-the-committed-hold-set`
FAILS, which is independent confirmation of §2.1 from the claim sweep's own code.

## 6. Verdict (scoped to this seat's observations)

**The claim-O sweep's inventory is nearly complete: it enumerates 24 of the 29
D4-pinning surfaces in this census, and misses 5 — one of which is a real
defect.** The four non-defect misses are the sweep's own round-27 outputs,
excluded by a `round-27` substring guard. The defect is **family G: the D4 hold
set is filtered out by a string test that its delivered schema does not satisfy,
so its three self-pins are never re-verified.** The hold set's pins currently
hold, so nothing is red — but "every surface re-verified" is not established for
family G, and the sweep's own selftest says so (6/8 controls, exit 1).

This is a **coverage** finding, not a quality or acceptance finding. It does not
say any sweep verdict is wrong.

**To close the claim**, the family-G filter needs a digest-identity test (as this
seat's census uses), the sweep's `known-green-generation-replays` expectation
needs updating for the post-register generation, and the `round-27` exclusion
needs to be a filed scope decision rather than a substring guard. Those are
successor-seat work; this seat may not edit a peer's instrument.

## 7. Limits

- This fragment audits the **inventory and its reach**, not sweep verdicts. It
  re-decides nothing the round runner graded and claims nothing about the
  register law, the syllabify fix, or design quality.
- The live D4 tree moved at least three times during measurement. Every digest
  and exit code is stamped; re-measure rather than cite.
- Reach figures are re-derived on every run of this tool, so a revision to either
  instrument is picked up rather than invalidating a hard-coded number.
- No filed round 8–26 byte, no `tools/gates/**` byte, and no sibling round-27
  seat's file was written by this seat.
