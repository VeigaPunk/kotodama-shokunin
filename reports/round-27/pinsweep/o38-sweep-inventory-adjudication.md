# R27-O38 — independent adjudication of the sweep inventory and the family-G defect

- **Seat:** R27-O38 (sweep auditor 2 of 2), round 27, loop 3 build 3 of 4, claim
  **O** `pin-sweep` (`reports/round-27/claims.json`). Assignment: "independent
  re-verification of the sweep inventory (zero missed surfaces)."
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`;
  lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`. Measurements
  19:24–19:37Z.
- **Writes:** `reports/round-27/pinsweep/o38-sweep-inventory-adjudication.md`,
  `reports/round-27/audit/o38-sweep-inventory-adjudication.py`,
  `reports/round-27/pinsweep/o38-adjudication-receipt.json` only. Scratch under
  `/var/tmp/`. No filed rounds 8–26 byte, no `tools/gates/**` byte, no sibling
  round-27 file written; no commit, no push.
- **Canon:** NON-CANON engineering audit. A pin is integrity, never truth and
  never clearance. No design-quality claim.

## 0. Why adjudication, not a second enumeration

Two sweep auditors were assigned. Building a second enumeration and reporting
that the two agree would prove little: two enumerators built on the same idea
agree **by construction**. What a second auditor can independently establish is
whether each of the first's claims survives a different read of the same bytes,
and whether the claim sweep's *own* logic does what it says. So this seat:

1. re-resolves every surface O37 classified as D4-pinning, with its own resolver;
2. re-derives both reaches on separate runs;
3. **re-derives the cause** of the family-G gap O37 found, by evaluating the
   claim sweep's own filter against the live hold set;
4. probes surface families a filename walk could omit.

Instrument: `reports/round-27/audit/o38-sweep-inventory-adjudication.py`.
Resolver shapes: JSON `inputs`/`input_pins` maps; the twin
`{"path": "examples/culture-d4/…", "sha256": "…"}` object; named-key self-pins
(`packet_sha256`, `projection_sha256`); the typed-pipelines profile shape;
`MANIFEST.tsv` column pairs.

## 1. Result — O37's census confirmed; the family-G defect independently reproduced

`python3 -B reports/round-27/audit/o38-sweep-inventory-adjudication.py`
(2026-10-18T19:37Z, lane HEAD `b95fca1`, exit 1):

| measure | value |
|---|---|
| O37 D4 rows adjudicated | **29** |
| reach disagreements (O37 flag vs O38 re-run) | **0** |
| pins unresolvable by O38's resolver | **0** |
| surfaces missed by the **X61 audit** instrument | 20 (18 stale / 2 hold) |
| surfaces enumerated by the **claim-O sweep** (`pinsweep/sweep.py`) | 34 |
| **surfaces missed by the claim-O sweep** | **5** |
| **family-G filter defect reproduced** | **True** |
| un-enumerated probe surfaces found by O38 | **3** |

**Every one of O37's 29 D4 classifications survived independent re-verification**,
and its reach flags matched on a separate instrument run (0 disagreements).

## 2. The family-G defect, reproduced from the claim sweep's own filter

O37 reported that the claim sweep's family G enumerates **0 rows**. This seat
re-derived the *cause* by evaluating the sweep's four guard strings against the
live hold set — not by reading its source, but by applying its test:

```
$ python3 -B reports/round-27/audit/o38-sweep-inventory-adjudication.py
  hold-filter adjudication: kept_by_guards=False is_d4_by_digest=True DEFECT=True
      false: holds mention culture-d4
      false: supersedes_pins mention culture-d4
      false: schema contains d4
      false: revision_note contains D4
```

All four guards evaluate **False** on `examples/culture-d4/expected-holds.json`,
so the one surface family G exists to cover is filtered out. The guards look for
the literal tokens `culture-d4`, `d4`, `D4`; the delivered file carries schema
`kotodama-typed-pipeline-holds-v1`, a `supersedes_pins` map **keyed by digest
name** (`packet_sha256`) rather than by path, and a `revision_note` that says
"round-27 register-law build" without the token `D4`.

**The correct test is digest identity, and it says this file IS a D4 surface:**
`is_d4_by_digest=True` — its `packet_sha256` equals the live
`examples/culture-d4/packet.d4.yml`. That is the test this seat's own census
uses, and it is why O37's census includes the hold set while the sweep's family G
does not.

**Cross-check from the sweep's own code.** Its selftest has 8 controls; the one
written to catch exactly this **fails**:

```
$ python3 reports/round-27/pinsweep/sweep.py --selftest      # exit 1
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

Two independent derivations — this seat's filter evaluation and the sweep's own
control — agree that family G is empty. **The defect is honestly reported by the
instrument that has it**; the tool exits 1 and names the failing control. It is a
defect in coverage, not concealment.

`known-green-generation-replays` also fails: it replays `round-26/post-register`
expecting green, and that generation now reports 2 mismatches because the D
landing moved the bytes it pinned. That is a stale expectation inside the sweep's
control, not a second product defect.

**Current impact is nil and future impact is not.** At the 19:37Z stamp the hold
set's three self-pins all **hold** against live bytes
(`86079a67…` / `88a94422…` / `2819f687…`), so no red verdict is being hidden
today. But a drift there would go unreported, and the claim's "every surface
re-verified" does not hold for family G.

## 3. The claim sweep's other four misses are its own round-27 outputs

| # | surface | why not enumerated |
|---|---|---|
| 1 | `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | the sweep excludes paths containing `round-27` |
| 2 | `reports/round-27/pinsweep/v3-baseline-r27/twin.json` | same guard |
| 3 | `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/expected.json` | same guard |
| 4 | `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/expected.json` | same guard |

Excluding a sweep's own output from its drift report is **defensible** — a sweep
cannot treat its own fresh rows as independent surfaces. The observation is that
this is implemented as a `"round-27" in rel` substring guard rather than a filed
scope decision, so it would also silently exclude any *other* round-27 surface
that carries a pin. That is a scope note for the parent, not a defect.

## 4. The X61 reach, reported separately (do not conflate)

The **audit** instrument `reports/round-27/audit/x61-pin-sweep.py` enumerates 30
files and reaches families **A** (11/11 manifests) and **B/C** (13/13 battery
roots) only — 20 of the 29 D4-pinning surfaces are outside *its* reach. That is a
statement about a peer's check, **not** about the claim sweep, which reaches 24
of 29. The two figures are kept apart in every receipt this seat writes
(`missed_*` vs `claim_sweep_missed`), because O37's first pass conflated them and
reported the audit instrument's 20 as the claim's misses.

### 4.1 The missed set splits 18 stale / 2 hold — it is not "20 stale"

At the 19:29Z stamp, of the 20 surfaces the X61 instrument misses:

- **18 are stale** against live bytes (live findings);
- **2 hold** — `tools/gates/typed-pipelines.json` (d4 profile: packet, projection,
  adapter, assembler, expected — all match live) and
  `examples/culture-d4/expected-holds.json` (all three self-pins match live).

They are **un-swept**, and 18 of them are stale. Reporting them as one "20 stale"
number would be wrong. That split is the reason this seat exists.

### 4.2 One row is stale for a reason that predates this round

`reports/round-26/remainders/v3-baseline-r26/expected.json` — filed by the
**round-26** O seat as the pin-tail re-point — pins the **round-22-era** D4
digests (`packet.d4.yml e7ecd204…`, `typed-labels.d4.yml 60b526b0…`,
`expected-holds.json 3826ba68…`) and its own replayer returns exit 1. Its sibling
`reports/round-26/register/v3-baseline-r26/expected.json`, frozen *after* the
register landing by the D seat, carries the correct post-landing digests. So the
round-26 pin-tail re-point landed a row that was stale when written. A round-26
finding, disclosed here because the round-27 sweep inherits it; this seat may not
edit a filed round-26 byte.

## 5. The false-positive hunt — 3 more pin surfaces, in evidence receipts

O38 probed six families a filename walk could omit (fixture `.expected`,
`run.log`, `packet.md`, `freeze.txt`, `evidence/*.json`, `*.out`). Three carry
independent D4 pins and are enumerated by no instrument this round:

| surface | D4 pins | stale |
|---|---:|---:|
| `reports/round-22/bleed/evidence/attempt-01-verification.json` | 19 | 6 |
| `reports/round-23/wording/evidence/tie-break-check-receipt.json` | 3 | 3 |
| `reports/round-22/bleed/evidence/before-state.json` | 3 | 3 |

25 pins, 12 stale, measured 2026-10-18T19:30Z. These are **evidence receipts**
that captured the D4 tree at a past stamp; their staleness is expected and they
are historical by design. The finding is a coverage one: **a pin surface can live
in an `evidence/*.json` receipt, so "every surface" cannot be established by
filename convention alone.**

## 6. Controls

**Detector controls (in-memory, `--selftest`, 6/6).** The resolver was exercised
on: a JSON `inputs` pin that holds → `holds`; the same pin with a wrong digest →
`stale`; a `MANIFEST.tsv` row pair; and two negative cases (a 63-hex token, a
`culture-d2` path).

**Live controls (on the real tree).** The verdict function is not a constant:

| control | expected | observed |
|---|---|---|
| `tools/gates/typed-pipelines.json` (un-swept, live-pinned) | `holds` | `holds` |
| `reports/round-20/handoff/expected.json` (un-swept, pre-landing) | `stale` | `stale` |
| `reports/round-26/handoff/declared-in-r5/expected.json` (un-swept) | `stale` | `stale` at 19:29Z (was `holds` at 19:19Z) |
| 9 swept surfaces | reach flag matches | 9/9 match |

The third row is the control that matters most: the **same file** read `holds` at
19:19Z and `stale` at 19:29Z, because the D landing wrote the artifact it pins in
between. The resolver did not change; the tree did. That is why every figure in
this fragment carries a stamp.

**Defect control.** The family-G finding is not this seat's assertion alone: the
claim sweep's own `hold-walker-finds-the-committed-hold-set` control fails, and
the tool exits 1. Two independent derivations agree.

**Reach controls.** Both reaches are taken from each instrument's own receipt on
a separate run. An earlier O38 pass compared against O37's *stale filed receipt*
and reported 4 reach disagreements; regenerating that receipt drove it to **0**.
The fallback path (static `rglob` read, used when an instrument cannot run) is
labelled `source-rglob-fallback` in every receipt.

## 7. Environment hazard, measured — `/tmp` exhaustion

The X61 instrument mirrors into a **hardcoded `/tmp`**. During this wave `/tmp`
(a 16G tmpfs) reached 80% under ~64 concurrent workers, and:

- `x61-pin-sweep.py --json` died with `OSError: [Errno 122] Disk quota exceeded`
  mid-mirror, producing **no receipt and exit 0** — a silent could-not-evaluate;
- `tools/replay-frozen.py` and `tools/exercise-handoff-e2e.py` began returning
  **exit 120** with empty output on rows that had been green minutes earlier.

Both are indistinguishable from a verdict at a glance. **Any seat that reads a
bare `exit 120`, or a sweep receipt missing rows, during this wave should treat
it as could-not-evaluate and re-run outside `/tmp`.** O38 therefore carries a
static fallback, and every receipt names its reach method. Disclosed, not
absorbed: `/tmp` pressure is host-level and outside this lane's write scope.

## 8. Verdict (scoped to this seat's observations)

**The claim-O sweep's inventory is nearly complete and carries one real defect.
O37's census is confirmed on all 29 rows; the family-G gap is independently
reproduced and its cause identified.**

- **Coverage:** the claim sweep enumerates 24 of 29 D4-pinning surfaces. Four of
  the five misses are its own round-27 outputs (defensible, but implemented as a
  substring guard); **one is a defect**.
- **Defect (family G):** the sweep's D4 test looks for literal tokens the
  delivered hold set does not carry, so the hold set is filtered out and its
  three self-pins are never re-verified. Digest-identity says the file IS a D4
  surface. The pins currently hold, so nothing is red — but the claim's "every
  surface re-verified" does not hold for family G.
- **Honesty:** the sweep's own selftest fails (6/8) and names the failing
  control, so the gap is disclosed by the instrument that has it.
- **Un-swept ≠ stale:** of the 20 surfaces the *audit* instrument misses, 18 are
  stale and 2 hold. The two figures must not be merged.

**To close the claim**: fix the family-G filter to digest identity; update the
sweep's `known-green-generation-replays` expectation for the post-register
generation; and turn the `round-27` exclusion into a filed scope decision. Those
are successor-seat work; this seat may not edit a peer's instrument.

## 9. Limits

- This fragment **adjudicates** O37's census and the claim sweep's own logic. It
  does not re-enumerate the universe, re-decide any sweep verdict, and claims
  nothing about the register law, the syllabify fix, or design quality.
- The live D4 tree moved at least three times during measurement. Every digest
  and exit code is stamped; a later reader must re-measure.
- The evidence-receipt pins in §5 are historical by design; their staleness is
  **not** presented as a defect, only as proof that the surface class exists.
- No filed round 8–26 byte, no `tools/gates/**` byte, and no sibling round-27
  seat's file was written by this seat.
