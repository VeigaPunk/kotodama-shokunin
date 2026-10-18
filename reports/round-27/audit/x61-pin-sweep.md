# X61 — independent D4 pin sweep (round 27)

- round 27 (operator: loop 3 of 3, build round 3 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-27/claims.json`) · seat
  **X61** (SCRIBE X61 — pin-sweep double-check) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X61..X62: pin-sweep double-check + frozen
  replay audit."
- date: 2026-10-18. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Claim under check:
  `reports/round-27/claims.json` claim **O** (`operability`, capability
  `pin-sweep`), declared baseline
  `4f09c990d4c17f23b5e2cda0871f81db875635fc`; lane HEAD at every measurement
  below `b95fca1e40f32f7346937ab6426f9ccca60e319f` (round-27 declaration,
  2026-10-18T16:11:04−03:00 = 19:11:04Z).
- canon: **NON-CANON engineering evidence.** This audit admits nothing, certifies
  no round, and grants no promotion. A reproduced red verdict stays red.
- writes: **this file** and its read-only tool
  `reports/round-27/audit/x61-pin-sweep.py`, plus gitignored scratch under
  `.scratch/x61/`. No tool, gate, packet, pin, validator or shared-bookkeeping
  byte was edited; no filed round-8–26 artifact was written; no commit, no push.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command.
- measurement window: 2026-10-18T19:13Z–19:25Z UTC. **The wave was live
  throughout** — `reports/round-27/` grew from 3 files to 80 during this seat's
  reads, and `examples/culture-d4/packet.d4.yml` moved from `dd25077bc016…` to
  `c5441e3d0b23…` mid-window. Every number below names its own stamp; a number is
  not carried forward from an earlier sample.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the pin surface is **11 frozen manifests / 81 rows**; this tool re-derives every row itself and does **not** call `tools/replay-frozen.py` | measured |
| 2 | **48/81 rows reproduced** their recorded exit, finding count and output bytes (at 19:25Z; **50/81** at the 19:22Z sample, before the landing moved two more rows) | measured |
| 3 | **8 rows mismatch — and all 8 are supersessions, 0 drift**: each row's live input no longer hashes to its own `input_sha256` | measured |
| 4 | **25 rows could-not-evaluate — all 25 `gate_digest_mismatch`**: each pins a gate revision no longer on disk | measured |
| 5 | **19/19 committed baselines pinned, 0 findings**, across all three roots `check-gate-battery.py` discovers | measured |
| 6 | the battery's own duty-2 sweep independently reads **19 pinned / 0 findings / 0 uncovered** — the same set, by different machinery | measured (cross-check) |
| 7 | `TMPDIR` inside the repo silently voids the whole manifest surface: the same manifest reads **0 reproduced / 6 `mirror_unsafe`** inside vs **4–6 reproduced / 0 `mirror_unsafe`** outside | **finding X61-B1** |
| 8 | **two generations** (`round-18/repin-d2`, `round-20/repin-d2`) pin all eleven of their snapshots under a *third* generation (`round-11`) | measured (advisory) |
| 9 | the tool's own controls pass **21/21**, including four classifier controls and a check that a missing live file never reads as a supersession | measured |
| 10 | **`tools/gates/frozen/README.md` — the index `gate-frozen-run-standard.md:54` declares — does not exist** | **finding X61-B2** |
| 11 | two peer auditors (X60, and the round-27 D-seat scratch) had already caught the first draft's completeness defect and its no-op `tmpdir_probe`; both are fixed here and the fixes are measured | disclosed |

## 1. Method, and why this is a double-check and not a re-run

The round's own counting command is `python3 reports/round-27/run-validation.py`;
the round's verdict is `reports/round-27/validation.json`, indexed by X56, not
adjudicated here. Claim O's "single re-pin-and-verify sweep" needs a second
instrument that reaches the same surface by different machinery, so this seat
built one:

```sh
export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1      # OUTSIDE the repo — see §4
python3 -B reports/round-27/audit/x61-pin-sweep.py --selftest   # 21/21, exit 0
python3 -B reports/round-27/audit/x61-pin-sweep.py             # text summary
python3 -B reports/round-27/audit/x61-pin-sweep.py --json      # receipt on stdout
```

Differences from `tools/replay-frozen.py` that make agreement evidence rather
than a shared bug:

| step | `replay-frozen.py` | this tool |
|---|---|---|
| pin verification | one pass, raises on the first failure | all three pins evaluated and recorded per row |
| manifest parse | assumes the documented schema | refuses a wrong header or a short row as a `problem`, never guesses |
| gate whitelist | 3-segment path under `tools/gates` | same rule, independently spelled |
| baseline discovery | not its duty | all three battery roots, deduplicated |
| mismatch cause | not classified | re-derives supersession-vs-drift from the live input |
| TMPDIR | refuses an in-repo mirror | same refusal, and the sensitivity is *measured* as a two-run probe |

`tools/replay-frozen.py` is **not** edited by this seat; it is a peer instrument,
and §6 records where the two disagree.

## 2. The manifest sweep — 11 manifests, 81 rows

Command (2026-10-18T19:25Z, TMPDIR outside the repo; **the same command at
19:22Z read 50/81 reproduced / 6 mismatch**, before the round-27 landing moved
two further rows — both samples are recorded because the wave was live):

```sh
python3 -B reports/round-27/audit/x61-pin-sweep.py
```

| manifest | rows | reproduced | mismatch | could-not-evaluate |
|---|---:|---:|---:|---:|
| `round-3` | 7 | 0 | 0 | 7 |
| `round-3/attempt-1` | 7 | 0 | 0 | 7 |
| `round-11` | 11 | 10 | 0 | 1 |
| `round-18` | 2 | 0 | 2 | 0 |
| `round-18/repin-d2` | 11 | 10 | 0 | 1 |
| `round-20/repin-d2` | 11 | 10 | 0 | 1 |
| `round-22/d4-repin` | 3 | 0 | 2 | 1 |
| `round-23/repin-d2` | 11 | 10 | 0 | 1 |
| `round-25/gate-input` | 6 | 0 | 0 | 6 |
| `round-26/gate-input` | 6 | 4 | 2 | 0 |
| `round-26/post-register` | 6 | 4 | 2 | 0 |
| **total (19:25Z)** | **81** | **48** | **8** | **25** |
| *total (19:22Z sample)* | *81* | *50* | *6* | *25* |

### 2.1 The eight mismatches are supersessions, not drift

The round-26 D20 seat fixed a classification rule (`reports/round-26/gate-tests/
D20-replay-frozen.md` §3.1): a mismatch whose **live input has moved** is a
supersession; one whose input still hashes to its pin is genuine drift. This seat
**re-derives** that classification instead of quoting it — the rule is a pure
function of `(live input digest, pinned digest)` and is controlled in §5.

| manifest | row | gate | live input moved | class |
|---|---:|---|---|---|
| `round-18` | 2 | `d4-typed-labels-check-gate.py` | yes | supersession |
| `round-18` | 3 | `d4-assembly-check-gate.py` | yes | supersession |
| `round-22/d4-repin` | 2 | `d4-typed-labels-check-gate.py` | yes | supersession |
| `round-22/d4-repin` | 3 | `d4-assembly-check-gate.py` | yes | supersession |
| `round-26/gate-input` | 2 | `typed-pipeline-gate.py` | yes | supersession |
| `round-26/gate-input` | 3 | `typed-pipeline-gate.py` | yes | supersession |
| `round-26/post-register` | 2 | `typed-pipeline-gate.py` | yes | supersession |
| `round-26/post-register` | 3 | `typed-pipeline-gate.py` | yes | supersession |

**Zero rows are drift.** That is the reading the O claim needs: nothing on the
frozen surface disagrees with a gate while its own input still matches. Every
mismatch is a row a later generation superseded — the register landing moved the
D4 packet twice inside this window (`e7ecd2045ef0…` → `dd25077bc016…` at 19:18Z →
`c5441e3d0b23…` by 19:25Z; `sha256sum examples/culture-d4/packet.d4.yml`), and the
`round-18` / `round-22` projection-and-assembly rows bind the pre-register bytes.
The last two — `round-26/post-register` rows 2 and 3 — moved *after* this seat's
first sample: at 19:22Z that generation read **6/6 reproduced**, at 19:25Z it reads
**4/6**. X62 records the same pair independently (`x62-frozen-record-audit.md` §4)
and names the mechanism: the assembler's deterministic output moved
`dd25077bc016…` → `c5441e3d0b23…`.

### 2.2 The twenty-five could-not-evaluate are all `gate_digest_mismatch`

Every one is a row pinning a gate revision that is not on disk, refused *before*
any gate runs — the documented cascade (`gate-frozen-run-standard.md` §6 step 2;
`reports/round-25/gate-input/freeze.txt` "cascade" paragraph). The mechanism is
the same one the round-26 D20 seat named: a filed row pins the gate *bytes*, so a
later gate revision supersedes its row rather than reproducing it. Restoring the
predecessor blob returns those manifests to full reproduction; **no historical
manifest is edited to chase them**, which is the append-only rule.

- `round-3`, `round-3/attempt-1` (7 each): all seven legacy gate revisions moved.
- `round-11`, `round-18/repin-d2`, `round-20/repin-d2`, `round-23/repin-d2`
  (1 each): the `typed-pipeline-gate.py` row only.
- `round-22/d4-repin` (1): the same `typed-pipeline-gate.py` row.
- `round-25/gate-input` (6): the whole generation pins
  `879d40bf977eef65…`, which is not on disk; the live gate is `b749ad07cf17…`.

## 3. The baseline sweep — 19 baselines, 19 pinned

Command (same run): this tool's duty B. **The first draft of this tool globbed
only `tools/gates/expected/**` and reported `6/6 pinned`.** A peer auditor
(`reports/round-27/audit/x60-sweep-completeness.py`) measured that a method which
globs one root while baselines live under two others is incomplete, and named it.
The defect is fixed and the fix is measured:

| root | baselines | pinned | findings |
|---|---:|---:|---:|
| `tools/gates/expected/` | 6 | 6 | 0 |
| `tools/gates/frozen/` | 10 | 10 | 0 |
| `reports/round-9/baselines/` | 3 | 3 | 0 |
| **total** | **19** | **19** | **0** |

The ten baselines under `tools/gates/frozen/**` carry one input each except
`provenance-audit/{r9-pre,r18-post}` at 20 each; all 26 of their input digests
re-derive. Every `gate_sha256` pin matches the live gate.

**Cross-check (different machinery, same reading).** The canonical battery was
run with TMPDIR under the repo scratch (its documented mode):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B tools/check-gate-battery.py      # exit 0; 7/7 selftests; coverage 9/9
```

Its duty-2 report reads **19 baselines, all `reading: pinned`, 0 findings**, and
its `coverage` field reads **`9/9`**. That is the same 19-element set this tool
found by its own glob — agreement by two independent code paths, which is what
the double-check is for. The battery's `pass: 7` is the *selftest* counter, a
different quantity from `coverage`; the two are deliberately kept apart
(`tools/check-gate-battery.py` docstring, duty 2).

## 4. Finding X61-B1 — `TMPDIR` inside the repo voids the manifest surface

`tools/replay-frozen.py` refuses a temporary mirror whose real path is inside the
repository (`mirror_unsafe`, `tools/replay-frozen.py:177`). The round's own
regimen mandates `export TMPDIR=$PWD/.scratch` before scratch-writing commands —
so a replay taken under that export measures **nothing**: every row refuses
before a gate launches. This tool reproduces the refusal and *measures the delta*
with a two-run probe on the current generation:

| mirror parent | reproduced | mismatch | could-not-evaluate | `mirror_unsafe` |
|---|---:|---:|---:|---:|
| `.scratch` (inside the repo) | **0** | 0 | **6** | **6** |
| `/var/tmp` (outside the repo, 19:25Z) | **4** | 2 | 0 | 0 |
| `/tmp` (outside the repo, 19:22Z) | **6** | 0 | 0 | 0 |

Both runs are of the same manifest
(`tools/gates/frozen/round-26/post-register/MANIFEST.tsv`) at the same revision.
The two outside-repo rows differ because the probe was run twice, across the
round-27 landing that superseded that generation's two D4 rows; **what the probe
establishes is the inside-vs-outside delta (0 vs 4–6 reproduced, 6 vs 0
`mirror_unsafe`), not either outside tally.**
This is not a defect in the tool — refusing an in-repo mirror is correct, because
a mirror inside the tree could let a gate write back into the lane it measures.
It is a defect in *any receipt that reports a replay tally without naming its
TMPDIR*: the round-25 and round-26 seats both recorded the constraint
(`round-25/gate-input/freeze.txt`; `round-26/gate-tests/D20-replay-frozen.md` §4),
and the round-27 sweep must carry it too. Every tally in this fragment names
`TMPDIR=/tmp`.

**Severity.** Advisory-to-blocking depending on what a reader does with a tally.
A `could-not-evaluate: 6` written under the mandated export is indistinguishable
from a real refusal cascade; the two are only separable by the `reason` field.

## 5. Finding X61-B2 — the frozen index the standard declares does not exist

`corpus/knowledge/verification/gate-frozen-run-standard.md:54` lays out the
frozen tree as:

```text
tools/gates/frozen/
  README.md                          # index: baseline id → gate, revision, verdict class
```

Measured (2026-10-18T19:19Z, `test -f tools/gates/frozen/README.md`): **absent**.
Two generation-level READMEs exist (`round-11/README.md`, `round-18/README.md`),
and no round-11..26 generation root carries one. The standard's §5 step 7 also
requires "Commit the baseline with its README index row" — so the index row has
no home for every generation after round 18.

This is **not** this seat's file and is not repaired here: it is a named gap on
the **verification knowledge** surface, handed to the parent. Severity: low for
the round's claims (the manifests and receipts are self-describing), but it is a
documented obligation the tree does not meet, and the standard is the lane's own
knowledge entry — so the gap is in the lane's own claim about itself.

## 6. Where this tool and `replay-frozen.py` disagree, and why

At the same revision and TMPDIR, row-level verdicts agree on all 81 rows:
50 reproduced / 6 mismatch / 25 could-not-evaluate by both instruments
(`tools/replay-frozen.py` per-manifest exit codes, 2026-10-18T19:14Z; this tool,
19:22Z — the same two samples, before the landing moved `round-26/post-register`
rows 2 and 3, which both then read as supersessions). The **exit codes differ in
kind**, not in reading:

| | `replay-frozen.py` | this tool |
|---|---|---|
| exit 0 | every row reproduced | every row reproduced **and** every baseline pinned |
| exit 1 | a mismatch | a mismatch |
| exit 2 | a could-not-evaluate | a could-not-evaluate **or** an unpinned baseline |

This tool therefore exits **2** on today's tree (25 could-not-evaluate) where
`replay-frozen.py` exits 2 on five of the eleven manifests and 0 or 1 on the rest.
Neither reading is "the" verdict: exit 2 outranks exit 1 by design, and a
`gate_digest_mismatch` cascade is a could-not-evaluate, never a pass. The round's
own acceptance is `reports/round-27/validation.json`; this tool informs it and
does not replace it.

## 7. Advisory — two generations pin snapshots in another generation

**All eleven rows** of both `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv`
and `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` name their
`input_snapshot` under `tools/gates/frozen/round-11/typed-pipeline/` — a
*different* generation — and all verify against it (`snapshot_pin_holds: true`).
Measured with an awk over each manifest's `input_snapshot` column
(2026-10-18T19:26Z):

| generation | rows | own snapshot | foreign snapshot rows |
|---|---:|---:|---:|
| `round-11` | 11 | 11 | 0 |
| `round-18/repin-d2` | 11 | **0** | **11** |
| `round-20/repin-d2` | 11 | **0** | **11** |
| `round-23/repin-d2` | 11 | 11 | 0 |

Each re-pin generation reads three distinct round-11 snapshot files. The
standard's §3 shows the snapshot living *inside* the baseline directory
(`<gate-name>/<baseline-id>/packet.yml`), and requires a bare baseline id to
resolve under exactly one gate directory. A generation whose every row reads a
sibling's snapshot is legible — the snapshot is committed, digest-pinned and
byte-identical, and the rows reproduce — but it makes the re-pin directory an
incomplete record of its own read set, and it means a future edit to the
round-11 generation would move twenty-two rows across two later generations at
once. Recorded as an observation, not a finding: the pins hold, and no historical
manifest may be edited to relocate it. `round-23/repin-d2` is the contrast case —
the same re-pin duty, done with its own snapshots.

## 8. Controls

`python3 -B reports/round-27/audit/x61-pin-sweep.py --selftest` → **21/21, exit 0**
(2026-10-18T19:22Z). The controls are in-memory and never touch the lane's frozen
surface:

- positive: a well-formed manifest parses; a legal path resolves; finding
  counting is prefix-anchored (`FINDINGX` is not a finding).
- negative: a wrong header and a short row are refused, not guessed; a
  non-digest pin, a non-whitelisted gate, and five unsafe path spellings
  (absolute, `~`, internal `..`, flag-like) are each refused with their own
  reason id; an in-repo mirror is refused.
- classifier: a moved live input is a supersession, an unmoved one is drift, an
  unreadable one is neither — **and a missing file is not read as a supersession**
  (absence is never evidence that bytes moved).
- resolver: a gate resolves from a bare name, a script path, and a baseline path;
  an unknown name is not guessed.

The two defects a peer auditor found in this tool's first draft are also covered
by controls now: the baseline roots are three (not one), and the `tmpdir` argument
threads through `verify_row` into `run_mirror` so the probe measures a real delta.

## 9. Limits

- **This is reproduction, not correctness.** A reproduced 12-finding D4 row is
  still twelve open holds; a reproduced `exit_code=2` control is still a refusal.
  Nothing here reads a design as clean.
- **The generations bind to today's bytes.** The wave was live during this
  window; a later landing moves the D4 packet again and supersedes more rows. The
  `round-26/post-register` generation read 6/6 at 19:22Z and **4/6 at 19:25Z** —
  the same command, the same revision, two different readings, which is why every
  tally here names its stamp.
- **One root is not the surface.** The 19-baseline figure is a property of the
  three roots `check-gate-battery.py` discovers; a fourth root added later would
  change it, and this tool would have to be taught it.
- **No verdict on the O claim.** Whether 8 supersessions + 25 cascades constitute
  a "sweep" that meets `after_required` is the parent's reading of
  `reports/round-27/validation.json`, not this seat's.
- **The TMPDIR probe uses one manifest.** It is the current generation and the
  one the O claim is about; the refusal is a property of the tool, so the
  mechanism generalises, but the tally does not.
- **`/tmp` was unusable for part of this window** (tmpfs at 80%, `Errno 122 Disk
  quota exceeded` on a mirror copy), so later runs used `TMPDIR=/var/tmp`. The
  probe's two parents were `.scratch` and the ambient `tempfile.gettempdir()`; the
  reading does not depend on which outside-repo parent is used.
