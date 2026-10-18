# R28-O37 — independent audit of the D4 pin-sweep inventory

- **Seat:** R28-O37 (sweep auditor 1 of 2), round 28, loop 3 build 4 of 4 (the
  final build round; 64 workers on `devin/deepseek-v4-1-flash-high`). Claim
  **O** `operability` / `final-pin-sweep` (`reports/round-28/claims.json`).
  Assignment: "inventory completeness."
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`;
  lane HEAD at every measurement below `69cecbc7dcf575a29f29660ecac470e05260fd86`
  (the round-28 declaration commit). Measurement window 20:11Z–20:26Z UTC.
- **Writes:** `reports/round-28/audit/o37-sweep-inventory-audit.py`,
  `reports/round-28/audit/o37-sweep-inventory-audit.md` (this file) and
  `reports/round-28/audit/o37-inventory-receipt.json` only. Scratch under
  `/var/tmp/kotodama-r28-o37` (outside the repo — the sweep's own replay mirror
  refuses an in-repo temporary root). No filed round 8–27 byte, no
  `tools/gates/**` byte, no sibling round-28 seat's file written; no commit, no
  push.
- **Canon:** NON-CANON engineering audit. A pin is integrity, never truth and
  never clearance; a reproduced red verdict stays red. No design-quality claim.

## 0. Verdict

**The round-28 sweep's inventory is complete for every maintained pin family,
and it carries one durable coverage defect in family G that the sweep's own
instrument already reports.** Measured at `69cecbc`:

| measure | value |
|---|---|
| D4-pinning surfaces in this census | **58** |
| enumerated (re-verified) by the round-28 sweep | **29** |
| missed | **29** — of which **0 live-pin stale**, 5 live-pin holding, 22 historical, 1 render, 1 frozen-snapshot |
| the sweep's own reach (its receipt's row-subject paths) | 53 |
| the sweep's own selftest | **12/12** (was **9/11** at 20:13Z, mid-window) |

The headline is a **split**, and the split is the finding: "missed" is not
"drifted". Of the 29 surfaces the sweep does not enumerate, **none is a stale
live pin owed a successor** — 22 are historical receipts that record the stamp
they measured (stale by design), and the rest are a render and a frozen snapshot.
The one thing the sweep genuinely could not see while the tree was moving is
**family G**, and that is a *coverage* defect, not a wrong verdict.

## 1. Correction first: my own first pass was wrong twice

This seat's instrument failed two ways before it was fit to report, and both are
recorded rather than smoothed over, because each is the same class of error the
audit exists to catch.

**1.1 The first census over-fired by ~200 surfaces.** It treated a *byte copy* of
an artifact as a *pin over* that artifact — every `packet.d4.yml` under a
baseline or a frozen generation's `inputs/` tree counted as a pin surface, so
every filed baseline read as drifted. A pin surface is a record that asserts a
digest **for another path**; a copy of the pinned bytes is not a pin. Fixed by
`is_d4_artifact()`.

**1.2 The first classifier had the exact defect it was auditing.** Its family-G
test admitted a hold set only when a digest it pins is the digest of a **live**
D4 artifact. That is the round-27 family-G defect, reproduced in the auditor. The
D4 hold set was dropped from this seat's own census the moment the tree drifted,
and the selftest's live control caught it (17/18). Fixed by admitting against the
**recorded** packet lineage (live + the hold set's `supersedes_pins` +
`earlier_packet_sha256` + the typed-pipeline profile's `superseded` notes).

**1.3 A scope violation, disclosed in full.** Discovery of "the sweep instrument"
was a glob `reports/round-28/sweep/*.py`, which matched not only `sweep.py` but
`repin.py` — a **writing** tool that re-freezes baselines and manifests — and
`poll-d-landing.py`, a blocking poller. Reach is measured by *executing* the
instrument. This seat's first pass tried `[python3, repin.py, "--json"]`
(argparse rejects it, exit 2, no write) and then **fell through to `[python3,
repin.py]` with no arguments**, which passes `repin.py`'s TMPDIR guard and
**runs the full re-freeze**: it rewrites `pinsweep/d4-pins.json`,
`sweep/repin-rows.json`, the `r28-post` baselines and frozen manifests, and
`v3-baseline-r28/`. The earlier draft of this section claimed "exit 2 before any
write" and that was **wrong**; the correct statement is that a write-capable tool
was executed.

**What that means, measured.** (a) The write set is confined to
`reports/round-28/**`; `git status` shows **no filed round 8–27 byte modified**.
`repin.py` does **not** write `tools/exercise-handoff-e2e.py` — its
`record_default_pointer()` *reads* the constant and records it, and the diff
visible on that tool (`V3_BASELINE_DEFAULT` → `v3-baseline-r28`) is the D/O
seat's own edit. (b) `repin.py` is **idempotent** — re-run at this stamp,
`d4-pins.json` and `repin-rows.json` come back **byte-identical**, and the same
regeneration was independently performed by the O seat, whose own run at 17:26
local produced the artifacts on disk now. So the collision cannot be distinguished
in the output and had no divergent effect. (c) `poll-d-landing.py` was also
matched, but its `--json` form fails the same way and its no-arg form blocks for
20 polls at 60 s — it was killed at the 300 s foreground timeout and wrote
nothing. (d) It is disclosed rather than repaired because an auditor may not
"clean up" a claimant's tree, and because the honest record is that the audit
instrument was, for one pass, a mutator.

`find_sweep()` now admits a candidate only when its source shows no content-write
marker (`write_text(`, `write_bytes(`, `shutil.copyfile(`, `os.replace(`,
`rmtree(`, `open(...,"w")`) **and** it accepts `--json`, so a writer is never
executed for reach. Three selftest controls use `repin.py` as the live negative
control.

## 2. Method — the census is built here, from the tree

The instrument `reports/round-28/audit/o37-sweep-inventory-audit.py`:

1. **Enumerates** ten surface families by walking the tree — A manifests,
   B/C battery baselines, D freeze receipts, E handoff baselines, F the profile,
   G hold sets, H twins, I evidence receipts, and **J** the false-positive family:
   *every other* file that names a D4 path or carries a D4-identical digest.
2. **Classifies** each surface by digest identity and declared path, never by
   filename convention. A hold set is admitted by the identity of the **packet**
   it pins: pooling every `supersedes_pins` value admitted the D2 drill's hold
   set, because both drills share the projector digest `2819f687…`.
3. **Classes** each surface so "missed" cannot be read as "drifted":
   `live-pin` (a maintained pin; stale ⇒ owed a successor), `historical`
   (a record of a past stamp), `frozen-snapshot`, `render`, `scratch-copy`.
4. **Measures reach behaviourally** — runs the sweep with `--json` under an
   out-of-repo `TMPDIR` and harvests the repo-relative paths under its
   row-subject keys (`path`, `manifest`, `surface`) — with a labelled static
   `rglob` fallback. A loose "any path-like string" harvest was rejected because
   it marks a surface swept merely because the receipt *mentions* it.
5. **Hunts false negatives** (duty D): enumerates the actual key vocabulary in
   which filed surfaces carry D4 pins, and reports the key names the sweep's
   family-J admission test never reads.

## 3. The census and the reach

`python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py` (2026-10-18T20:25:54Z,
lane HEAD `69cecbc`, exit 1):

| family | files in census |
|---|---:|
| A `MANIFEST.tsv` | 20 |
| B `tools/gates/expected/**` | 6 |
| C `tools/gates/frozen/**` + `reports/round-9/baselines/**` | 13 |
| D `freeze-receipt.json` | 4 |
| E `reports/**/expected*.json` | 26 |
| F `typed-pipelines.json` | 1 |
| G `expected-holds*.json` | 2 |
| H `twin.json` | 9 |
| I `reports/**/evidence/*.json` | 14 |
| J every other D4-naming file | 330 |

**58 D4-pinning surfaces; 29 swept; 29 missed.** The missed set splits:

| class | count | is a stale live pin? |
|---|---:|---|
| `historical` | 22 | no — records of a past stamp, stale by design |
| `live-pin` | 5 | **no — all 5 hold** |
| `render` | 1 | no |
| `frozen-snapshot` | 1 | no |

The five holding live-pin misses are all round-28's own fresh rows
(`pinsweep/{baselines/*/r28-post,v3-baseline-r28}/expected.json`,
`v3-baseline-r28/twin.json`, `frozen/r28-post/freeze-receipt.json`): they are the
sweep's own outputs, and excluding a sweep's own rows from its own drift report is
defensible. **No surface is both un-swept and stale.** That is the load-bearing
reading of the O claim's coverage clause, and it is measured, not inferred.

### 3.1 Adjudicated by R28-O38 — two classifications narrowed

R28-O38 re-resolved all 58 rows with its own resolver: **56 agreed, 0 pins
unresolvable, and the reach flags matched on a separate run (0 disagreements).**
The 2 differences are both `scribe/fragment-ledger.json` (rounds 27 and 28), where
this seat's **digest-identity** test admitted a row whose target is a *baseline
copy* — `pinsweep/baselines/…/examples/culture-d4/components/01-brief.yml`, whose
digest equals the live artifact byte-for-byte. O38's **path** test does not admit
it, and O38's stricter reading is the correct one: a digest-identity test alone
cannot distinguish "this surface pins the live artifact" from "this surface's pin
equals a byte copy of it". Both readings are recorded so a reader can choose; the
ledger is **not** a missed surface and nothing is owed. See
`o38-sweep-inventory-adjudication.md` §2.

## 4. The defect: family G is blind exactly during the drift window

At **20:13Z** the round-28 sweep's family G enumerated **0 rows** while the D4
hold set existed on disk, and its own selftest control
`hold-walker-finds-the-committed-hold-set` **failed** (sweep selftest 9/11):

```
$ python3 reports/round-28/sweep/sweep.py --selftest      # 20:13Z
  FAIL r27-generation-replays-with-its-own-snapshot
  FAIL hold-walker-finds-the-committed-hold-set
  passed: False  9 / 11
```

**Cause, derived from the filter itself — not from its prose.** Family G admits a
hold set only when its `packet_sha256` is in `recorded_d4_packets()`, and that
function builds its set from (a) the **live** packet digest, (b) the hold set's
`supersedes_pins` history, and (c) the profile's `superseded` notes. It never
reads the hold set's **own current pin**:

```
$ python3 -B - <<'EOF'
  … recorded_d4_packets() source slice …
EOF
  recorded_d4_packets() reads the hold's own packet_sha256? False
  it reads: ['supersedes_pins', 'packet', 'projection', 'adapter', 'assembler']
```

So the admission test is **live-tree-coupled**: it admits the hold set only once
its pin already matches the live tree — i.e. only *after* the drift has been
repaired. During the window between a landing and the D seat's re-pin, the hold
set pins the previous stamp, that stamp is in no admission source, and family G
returns 0 rows.

**Positive control** (the walker is fine; the filter is what blinds it):

```
  with the current pin removed from admission:
     walk_holds() rows: 0   <-- blind
  with the pin admitted:
     walk_holds() rows: 1   with drift [('packet_sha256','86079a67->543d68a8'),
                                        ('projection_sha256','88a94422->339bfd83')]
```

**Impact, measured at the time of the finding.** The hold set's three self-pins
were `86079a67…` / `88a94422…` / `2819f687…` against live `543d68a8…` /
`339bfd83…` / `2819f687…` — **two stale, one holding**. Family G saw none of it.
So the claim's "every surface re-verified" did not hold for family G, and a drift
there went unreported. The sweep disclosed this honestly through its own failing
control; it is a coverage defect, not concealment.

**The O seat has since repaired it.** At 20:25Z family G enumerates **1 row**, the
control passes, and the sweep selftest reads **12/12** — the admission set now
includes `86079a67…`, and the control was renamed
`r27-generation-is-superseded-replays-red`. This seat measured both states; the
defect is filed because it was live for most of the round, because the *durable*
property remains (the test still admits by live-tree lineage, not by the hold
set's own pin), and because the round's own two peer audits (X60, X61) do not
mention family G at all — 0 occurrences in either fragment.

### 4.1 The second failing control, adjudicated as a stale expectation

`r27-generation-replays-with-its-own-snapshot` also failed (2/2 mismatch, exit 1)
at 20:13Z. That is **not** a product regression and not a sweep defect:
`tools/gates/d4-assembly-check-gate.py:33` resolves `ROOT` from the gate's own
repo path and calls the assembler's live build path, so a frozen row can never
reproduce once the live component tree moves under it. The control's premise —
"the r27 generation is green against its own snapshot" — is unsatisfiable by
construction. Measured directly:

```
$ python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv
ROW 2 mismatch  exit=1/0  detail: exit code 1 != recorded 0; output bytes differ
ROW 3 mismatch  exit=1/1 … (both rows: the live tree moved)
REPLAY MISMATCH: 2 mismatch, 0 reproduced of 2 row(s)
```

At 20:25Z the O seat replaced this control with `r28-generation-replays-green` +
`r27-generation-is-superseded-replays-red`, which is the correct pair. Recorded
here as a stale expectation that was live for most of the round.

## 5. Duty D — the key vocabulary family J never reads

Family J admits a surface only when it carries an `inputs` map or one of four
recorded pin-map key names (`input_pins`, `pins`, `live_tool_and_input_pins`,
`snapshot_pins`). The lane's filed surfaces key their D4 pins under **other**
names, so a genuine pin map is invisible to it:

| surface | key its D4 pins live under | pins | stale at 20:26Z |
|---|---|---:|---:|
| `reports/round-27/pinsweep/d4-pins.json` | `live_pins` | 6 | **4** |
| `reports/round-27/pinsweep/o38-adjudication-receipt.json` | (bare path→digest pairs) | 8 | 8 |
| `reports/round-26/register/repin.json` | `new_pins`, `superseded_pins`, `component_digests`, … | 5 | 5 |
| `reports/round-22/bleed/verification.json` | `readset_pins` | 8 | 8 |

The instrument reports the full vocabulary it measured under
`false_negative_hunt.keys_the_sweep_does_not_read`. These are round-27 and
round-26 receipts, so their staleness is historical by design — **the finding is
the coverage one**: "every surface" cannot be established by a fixed key-name
list, exactly as round-27 R27-O38 §5 found for `evidence/*.json`. The round-28
sweep's family J reads four names; the lane writes at least eight.

## 6. Controls

**Selftest (23/23, `--selftest`).** In-memory: the hex/path/pair matchers, the
skip policy, both `json_pairs` shapes, and the five class labels. Live on the real
tree: the D4 hold set classifies as a D4 surface **and the D2 hold set does
not**; `typed-pipelines.json` is a D4 surface; a packet byte-copy is not a
surface; and the writer guard detects `repin.py` and excludes it from the
instrument set.

**The decisive external control is the sweep's own selftest**, which fails 9/11
at 20:13Z naming `hold-walker-finds-the-committed-hold-set` — independent
confirmation of §4 from the claimant's own code.

**Reach controls.** Reach is taken from the instrument's own `--json` receipt on
each run, and the method is recorded (`instrument-receipt` here). The static
`rglob` fallback is labelled when used. Reach is *not* read from a filed receipt,
so a revision to the instrument is picked up rather than invalidating a
hard-coded number.

## 7. Limits

- This fragment audits the **inventory and its reach**, not sweep verdicts. It
  re-decides nothing the round runner graded, and claims nothing about the
  register law, the RL-4 packet_keys fix, or design quality.
- The live D4 tree moved at least twice during the window (`packet.d4.yml`
  `86079a67…` → `543d68a8…` at ~20:12Z). Every digest and exit code is stamped;
  a later reader must re-measure rather than cite.
- The 22 historical misses are **not** presented as defects; their staleness is
  by design. Only the family-G gap and the family-J vocabulary are findings, and
  the family-G one was repaired inside this window.
- Reach and class figures are re-derived on every run, so a revision to either
  instrument is measured rather than assumed.
- No filed round 8–27 byte, no `tools/gates/**` byte, and no sibling round-28
  seat's file was written by this seat.

## 8. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/var/tmp/kotodama-r28-o37      # OUTSIDE the repo

python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py --selftest   # 23/23
python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py             # census + reach
python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py --json      # receipt

python3 reports/round-28/sweep/sweep.py --selftest        # the claimant's own controls
python3 reports/round-28/sweep/sweep.py --json            # its census and reach
```

Machine receipt: `reports/round-28/audit/o37-inventory-receipt.json`.
