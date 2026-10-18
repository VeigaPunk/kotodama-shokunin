# R28-O38 — independent adjudication of the sweep inventory and the family-G filter

- **Seat:** R28-O38 (sweep auditor 2 of 2), round 28, loop 3 build 4 of 4 (the
  final build round; 64 workers on `devin/deepseek-v4-1-flash-high`). Claim
  **O** `operability` / `final-pin-sweep` (`reports/round-28/claims.json`).
  Assignment: "inventory completeness."
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`;
  lane HEAD at every measurement `69cecbc7dcf575a29f29660ecac470e05260fd86`.
  Measurement window 20:24Z–20:28Z UTC.
- **Writes:** `reports/round-28/audit/o38-sweep-inventory-adjudication.py`,
  `reports/round-28/audit/o38-sweep-inventory-adjudication.md` (this file) and
  `reports/round-28/audit/o38-adjudication-receipt.json` only. Scratch under
  `/var/tmp/kotodama-r28-o38` (outside the repo). No filed round 8–27 byte, no
  `tools/gates/**` byte, no sibling round-28 seat's file written; no commit, no
  push.
- **Canon:** NON-CANON engineering audit. A pin is integrity, never truth and
  never clearance. No design-quality claim.

## 0. Why adjudication, not a second enumeration

Two sweep auditors were assigned the same duty. Building a second enumeration and
reporting that the two agree would prove little: two enumerators built on the same
idea agree **by construction**. What a second auditor can independently establish
is whether each of the first's claims survives a **different read of the same
bytes**, and whether the sweep's *own* logic does what it says. So this seat:

1. re-resolves every surface R28-O37 classified as D4-pinning, with its own
   resolver (a different extraction path);
2. re-derives the sweep's reach on a separate run;
3. re-derives the **cause** of the family-G gap by applying the sweep's own
   filter, with a positive control;
4. probes for pin surfaces a filename walk or a fixed key-name list would omit.

## 1. Result

`python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py`
(2026-10-18T20:27:24Z, lane HEAD `69cecbc`, exit 1):

| measure | value |
|---|---|
| O37 rows adjudicated | **58** |
| D4-pinning by this seat's resolver | **56** |
| pin disagreements | **2** — both definitional (§2) |
| pins unresolvable | **0** |
| reach re-derived (separate run) | 53 surfaces, sweep exit 1 |
| **reach disagreements with O37** | **0** |
| family-G filter reads the hold set's own pin | **False** (§3) |
| family G blind at this stamp | **False** — the O seat repaired it inside the window |
| un-enumerated D4 pin maps found | **20** across 8 key names (§4) |

**56 of 58 of O37's classifications survived independent re-verification, and its
reach flags matched on a separate instrument run with 0 disagreements.** The two
disagreements are a definitional difference in the resolver, not a conflict about
the tree, and this seat's stricter reading is the correct one.

## 2. The two disagreements — definitional, and O38's read is the stricter one

Both are `scribe/fragment-ledger.json` (round-27 and round-28):

| surface | O37 | O38 | why |
|---|---|---|---|
| `reports/round-27/scribe/fragment-ledger.json` | D4-pinning | not | resolver definition |
| `reports/round-28/scribe/fragment-ledger.json` | D4-pinning | not | resolver definition |

The ledgers record baseline rows as
`{"path": "pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/01-brief.yml", "sha256": "649aa111…"}`.
That digest **equals** the live `examples/culture-d4/components/01-brief.yml`, so
O37's digest-identity test admits the row — its *target* is a **baseline copy**,
not the live artifact. This seat's resolver requires the target path itself to sit
under `examples/culture-d4/`, so it does not admit it:

```
live 01-brief.yml : 649aa111db2e57a7
r28 baseline copy : 649aa111db2e57a7
byte-identical? True
```

**O38's reading is the correct one, and the difference is instructive**: a
digest-identity test alone cannot distinguish "this surface pins the live D4
artifact" from "this surface's pin happens to equal a byte copy of it". The
stricter path test is right here because the ledger is a *census of baseline
rows*, not a pin over the live packet. O37's classification is not a defect — it
is the correct answer to a slightly looser question — and both are reported so a
reader can choose. The ledger is therefore **not** a missed surface: nothing is
owed.

## 3. The family-G filter, adjudicated from the filter itself

R28-O37 §4 reported that at 20:13Z the sweep's family G enumerated **0 rows**
while the D4 hold set existed, and that the sweep's own selftest control failed
(9/11). This seat re-derived the cause **by applying the sweep's test**, not by
reading its prose.

**The filter's own source does not read the hold set's current pin.** Slicing
`recorded_d4_packets()` out of the sweep:

```
filter_reads_the_holds_own_pin: False
it reads: supersedes_pins, packet, projection, adapter, assembler
```

So admission is built from the **live** packet digest, the hold set's
`supersedes_pins` history, and the profile's `superseded` notes — never from the
hold set's own `packet_sha256`. The test is therefore **live-tree-coupled**: the
hold set is admitted only once its pin already matches the live tree, i.e. only
*after* the drift has been repaired. In the window between a landing and the D
seat's re-pin, the hold set pins the previous stamp, that stamp is in no admission
source, and family G returns 0 rows.

**Positive control — the walker is fine, the filter blinds it:**

```
with the current pin injected into the admission set:
  walk_holds() rows: ['examples/culture-d4/expected-holds.json']
with the pin absent (the drift window):
  walk_holds() rows: []          <-- blind
```

**At this stamp the defect is repaired.** Family G now enumerates 1 row, the
sweep selftest reads **12/12**, and the admission set carries the current pin:

```
family_g_blind: False
walker_rows_as_filed: ['examples/culture-d4/expected-holds.json']
hold_current_packet_sha256: 543d68a8…   live_packet_sha256: 543d68a8…
current_pin_in_admission: True
```

**The durable property remains, and that is why this is filed rather than
closed.** The filter still admits by live-tree lineage rather than by the hold
set's own pin, so the same blindness returns the next time a landing moves the
packet before the hold set is re-pinned. The **repair that closes the class** is
to admit a hold set when *its own* `packet_sha256` is a recorded D4 packet digest
— including the value it currently carries — so that a lagging hold set is
enumerated and *reported as drifted* instead of silently skipped. This seat's own
`d4_lineage()` in the O38 instrument is that corrected test, and it is what
resolves the D4 hold set while still excluding the D2 drill's.

**Independent corroboration.** The sweep's own selftest at 20:13Z failed
`hold-walker-finds-the-committed-hold-set`, naming the gap from the claimant's own
code — two independent derivations agree. **Neither of the round's two peer
audits mentions family G**: 0 occurrences of `family G`, `hold-walker` or
`hold set` in `x60-sweep-completeness.md`, `x61-pin-sweep.md` or
`x62-frozen-record-audit.md`. This is the one part of the sweep surface no other
round-28 seat read.

## 4. Duty D — the key vocabulary no instrument reads

The sweep's family J admits a surface only when it carries an `inputs` map or one
of four recorded pin-map key names. The lane writes its D4 pins under **at least
eight** names. This seat enumerated every filed JSON whose value is a
path→digest map, measured each one's D4 pins and staleness, and reported the key
names the sweep never reads:

| key | surface | D4 pins | stale at 20:27Z |
|---|---|---:|---:|
| `live_pins` | `reports/round-28/pinsweep/d4-pins.json` | 19 | **4** |
| `stale_pins` | `reports/round-27/pinsweep/d4-pins.json` | 6 | 6 |
| `live_d4` | `reports/round-27/pinsweep/sweep-receipt.json` | 7 | 4 |
| `readset_pins` | `reports/round-22/bleed/verification.json` | 19 | 8 |
| `readset_pins` | `reports/round-22/bleed/evidence/attempt-01-verification.json` | 19 | 8 |
| `input_sha256` | `reports/round-1{7,8}/validation.json` | 16/19 | 5/8 |
| `new_pins`, `component_digests`, `generated_artifact_digests` | `reports/round-26/register/repin.json` | 6 each | 5 each |

**20 un-enumerated D4 pin maps across 8 key names.** Most are historical receipts
whose staleness is by design, so this is **not** 20 live findings — it is the
coverage statement that **"every surface" cannot be established by a fixed
key-name list**, exactly as round-27 R27-O38 §5 found for `evidence/*.json` one
round earlier. The round-28 sweep reads four names; the lane writes at least
eight, and the set grows every round.

## 5. Controls

**Detector controls (`--selftest`, 12/12).** In-memory: the hex matcher, both
`walk_pairs` shapes, the bare-field-name negative (a field called `sha256` is not
a target), and both `verdict_of` readings. Live on the real tree: the D4 hold set
resolves to D4 pins **and the D2 hold set resolves to none**; the profile resolves
to D4 pins; the sweep module is import-safe; and the admission set's construction
is checked.

**The D2 control is the decisive one, and it caught a real defect in this seat.**
The D2 hold set carries the *same* key names (`packet_sha256`,
`projection_sha256`) as the D4 one, so a named-key mapping fired on it and the
first selftest read 11/12. Fixed by gating the named-key mapping on **D4 lineage
membership**: a named key maps to a D4 target only when the file's own
`packet_sha256` is a digest the D4 lineage records. That is the same corrected
test §3 recommends for the sweep.

**Positive control for the family-G finding.** The finding is not this seat's
assertion: injecting the current pin into the admission set makes the walker
return the hold set (and, at 20:13Z, its two drifted pins); the sweep's own
control failed at the same stamp. Three independent derivations.

**Reach controls.** Reach is taken from the sweep's own `--json` receipt on a
**separate run** from O37's, and the two agree on all 53 surfaces. Agreement
across two runs is the evidence that reach is stable rather than a snapshot
artifact.

## 6. Verdict (scoped to this seat's observations)

**O37's census is confirmed on 56 of 58 rows; the 2 differences are a resolver
definition, and O38's stricter read is correct. The family-G gap is independently
reproduced and its cause identified from the filter itself; it was repaired inside
this window, but the durable property — admission by live-tree lineage — remains,
and neither peer audit reads that part of the surface.**

- **Coverage:** the round-28 sweep's inventory is complete for every maintained
  family. The misses are historical receipts, renders and its own fresh rows; no
  surface is both un-swept and stale.
- **Defect (family G):** admission is live-tree-coupled, so the hold set is
  enumerated only after the drift is repaired. Filed because the property is
  durable, not because it is currently red.
- **Coverage limit:** 20 un-enumerated D4 pin maps across 8 key names; the sweep
  reads four.
- **Honesty:** both defects were reported by the instrument that has them (the
  sweep's failing control) or by the auditor that made them (this seat's D2
  control and O37's §1.3).

**To close the class:** make family G admit by the hold set's own `packet_sha256`
against the recorded D4 packet lineage (this seat's `d4_lineage()` is the
corrected test), and extend family J's key vocabulary to the names the lane
actually writes. Both are successor-seat work; this seat may not edit a peer's
instrument.

## 7. Limits

- This fragment **adjudicates** O37's census and the sweep's own filter. It does
  not re-enumerate the universe, re-decide any sweep verdict, and claims nothing
  about the register law, the RL-4 fix, or design quality.
- The live D4 tree moved during the window. Every digest and exit code is
  stamped; a later reader must re-measure.
- The 20 un-enumerated pin maps are historical by design; their staleness is
  **not** presented as 20 defects, only as proof that the key vocabulary is wider
  than any fixed list.
- No filed round 8–27 byte, no `tools/gates/**` byte, and no sibling round-28
  seat's file was written by this seat.

## 8. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/var/tmp/kotodama-r28-o38      # OUTSIDE the repo

python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py --selftest  # 12/12
python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py            # adjudication
python3 -B reports/round-28/audit/o38-sweep-inventory-adjudication.py --json     # receipt

python3 reports/round-28/sweep/sweep.py --selftest    # the claimant's own controls
```

Machine receipt: `reports/round-28/audit/o38-adjudication-receipt.json`.
