- Seat: D04 | executor (claim D, pin re-freeze plan) | every expected.json / frozen / baseline row the register-form content change invalidates, each as a NEW-row draft (filed rows never edited) | date 2026-10-19 | baseline ce103bf

# D04 — the pin re-freeze list, measured on an isolated copy (not inferred)

**Mission (binding, `reports/round-36/targets.json`, seat D04):** "Pin re-freeze plan:
every expected.json/frozen/baseline row the content change invalidates, each as a
new-row draft (filed rows never edited)."

**Write scope:** this file only. All mutation under `.scratch/d04-iso*` (gitignored).
No filed 1–35 byte written, no `corpus/lessons/*.md`, no `tools/gates/frozen/**`, no
fleet `.ufo/**`, no commit, no push, no install, no network. No
`reports/round-*/run-validation.py` executed in-tree or otherwise (F-C13-1). Every
command ran from the lane root or an isolated `git archive ce103bf` copy with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Why the list is measured, not derived.** A re-pin list built from prose is exactly the
failure the gate standard forbids ("claimed ≠ re-executed", KTD-FR-S-0001). So this seat
applied the content change in three isolated copies and re-ran the pin-reading surfaces.
The digests below are outputs, not predictions. **Because digests are content-dependent,
the *row set* is what this seat owes; the digest values must be re-measured by the
integrator on the bytes actually landed** — D01's §5.1 bytes, D02's component 14, and the
minimal shape this seat applied each produce *different* digests for the same row set
(§2.3). That is a property of the artifact, not an error.

---

## 1. The three isolated copies and what each isolates

| copy | command | contents | what it answers |
|---|---|---|---|
| `.scratch/d04-iso` | `git archive ce103bf \| tar -x` | D01 §5.1 verbatim (`doublets` + comment header), no re-pin | which pin rows *move* on the content change alone |
| `.scratch/d04-iso2` | same | D01 §5.1 **+** the `01-brief.yml` C-04 registry row | whether registry consistency adds a cascade row |
| `.scratch/d04-iso3` | same | D01 §5.1 (compact shape) **+** the full re-pin applied | whether the re-pinned tree converges green |

The pristine archive was verified byte-identical to the live tree before use:

```
$ git archive HEAD | tar -x -C .scratch/d04-iso && cd .scratch/d04-iso
$ sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml \
            examples/culture-d4/typed-labels.d4.yml examples/culture-d4/expected-holds.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
```

All four equal the live tree and the r7 read-set pins (`reports/round-34/handoff/declared-in-r7/expected.json`).

---

## 2. The generated-artifact chain (the landing itself)

### 2.1 The change assembles with **zero tool edits**

Applying D01 §5.1 — one `packet_keys:` extension plus the eight-row `doublets:` block in
`examples/culture-d4/components/04-lexicon.yml`, nothing else — the assembler accepts it
because `doublets` is **already** in its allowlist:

```
$ grep -n "doublets" tools/assemble-culture-d4.py
81:    "registers", "doublets", "sayings", "oaths",
122:    "doublets": ("id",),
469:  - id: DB-01
```

| step | command | observed |
|---|---|---|
| apply | (edit `04-lexicon.yml` only) | `ed7093d6b92111c2…` → `ead390e120488d15…` |
| assemble | `python3 tools/assemble-culture-d4.py` | exit 0, `Wrote examples/culture-d4/packet.d4.yml (103724 bytes)` |
| check | `python3 tools/assemble-culture-d4.py --check` | exit 0 |
| block reached the packet | `grep -c "^doublets:" examples/culture-d4/packet.d4.yml` | `1` |
| projection | `python3 tools/d2-typed-labels.py --packet … --emit …` | exit 1 (the twelve design holds are expected on emit), file written |
| projection check | `python3 tools/d2-typed-labels.py --packet … --check …` | exit 0, `byte-identical deterministic projection` |
| typed packet | `python3 tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml` | exit 0, `Wrote … (110083 bytes, 12 routing row(s))` |
| typed check | `python3 tools/assemble-d4-typed.py --check …` | exit 0 |

**A trap worth naming for the integrator:** `assemble-d4-typed.py --emit` takes its path as
a **required argument**. Run bare (`--emit` with no value) it exits 2 with
`argument --emit: expected one argument` and writes nothing — so a re-pin loop that
invokes it bare silently leaves `packet.d4.typed.yml` stale while every other artifact
moves. Measured both ways; the bare form is the false-green.

### 2.2 The four generated artifacts, before → after (isolated copy, full re-pin)

Measured on `.scratch/d04-iso3` after the re-pin in §3:

| # | artifact | before (`ce103bf`) | after (landed + re-pinned) |
|---|---|---|---|
| 1 | `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b92111c2…` | `b4d71cd8e6964726…` |
| 2 | `examples/culture-d4/packet.d4.yml` | `aac91246cede8840…` | `fc46177a7150ae47…` |
| 3 | `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cfb9d4…` | `84e0f766c76f1476…` |
| 4 | `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384ce56…` | `4adaf00790efdf40…` |

`packet.d4.typed.yml` **does** move — it carries the `doublets` block as a nested
mapping (`diff` shows 97 added lines at `:1431-1528`). This seat initially mis-read it as
unchanged because of the bare-`--emit` trap above; the corrected measurement is the one
recorded here. **All four artifacts move; none may be assumed static.**

### 2.3 Digests are content-dependent — three shapes, three chains

The same *row set* produces different digest values depending on the exact bytes landed.
Recorded so no later seat mistakes a mismatch for a defect:

| route | source component digest | packet | projection | typed packet |
|---|---|---|---|---|
| this seat, D01 §5.1 verbatim (comment header) | `ead390e120488d15…` | `6cebab86f06733f1…` | `2e0703d5967e3f08…` | `d581e0ad5384ce56…`¹ |
| this seat, §5.1 + `01-brief.yml` C-04 row | `b4d71cd8e6964726…` (04) / `df1463c8dc2c00ca…` (01) | `a0c4bced98d32275…` | `98e54aff036663fb…` | `df3fc507275cec45…` |
| this seat, compact shape + full re-pin | `b4d71cd8e6964726…` | `fc46177a7150ae47…` | `84e0f766c76f1476…` | `4adaf00790efdf40…` |

¹ measured before the `--emit` path argument was supplied, i.e. this cell is the stale one
the trap produces; recorded because it is the false-green a re-runner would reproduce.

Cross-seat: D03's Drafts 1+2 state measured `packet 3067107f4a8df6d3…` / projection
`606e44785071bb0f…`; D02's component-14 route measured `packet 66c34ad5a4eb1f3a…` /
projection `105d91181d42a6b3…`; D03's combined state measured `packet 5231e73be696b020…`.
**Six different packet digests for one round's landing.** The integrator re-measures;
this seat's job is the row set.

---

## 3. The re-freeze list — every row the change invalidates

Six live pin surfaces. Each is drafted below as a **new row**; no filed row is edited.

### 3.1 `examples/culture-d4/expected-holds.json` — top-level pointers + a new generation row

**Moves.** Three of the eight D4 self-pins this file participates in:

| pin | before | after | moved? |
|---|---|---|---|
| `packet_sha256` | `aac91246cede…` | packet digest | **yes** |
| `projection_sha256` | `c23b0ab532cf…` | projection digest | **yes** |
| `projector_sha256` | `2819f68769df…` | `2819f68769df…` | no (no tool changes) |

The file's own bytes move (`e6ae9828d6c8…` → `ee0cf710ff0c…` on this seat's copy) because
its top-level pointers are inside it — which is why it is itself pinned by row 3.2 and the
ordering matters (§3.2).

**Draft (new row; filed rows untouched, `active_pin_generation` repointed):**

```json
{
  "id": "round-36-register-doublets",
  "round": 36,
  "date": "2026-10-19",
  "packet_sha256": "<re-measured on landed bytes>",
  "projection_sha256": "<re-measured on landed bytes>",
  "typed_packet_sha256": "<re-measured on landed bytes>",
  "projector_sha256": "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3",
  "revision_note": "round-36 register-form index landing: the packet gains the doublets block (8 rows indexing L-55..L-62). The hold set is UNCHANGED at 12 holds / 0 notes / 0 fails: a pointer-shaped index restates no derivation pair and moves no form off the sound-and-identity channel, so no form slot is owed.",
  "command": "sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml examples/culture-d4/packet.d4.typed.yml",
  "recorded_in": "reports/round-36/depth/D04-repin.md"
}
```

Precedent and constraint: the round-30 row (`round-30-qreg-records`) appended a
predecessor/successor pair and advanced only the two scalar pointers, leaving
`schema`, `counts`, `holds`, `notes`, `revision_note` and `supersedes_pins`
byte-equivalent (`reports/round-30/fixes/qreg-dangles.md`, "Pin cascade"). The hold set
must stay **12/0/0** — verified on this seat's copy: the argot gate still reports
`derived_pairs=8` and the law gate still reports `findings=0`.

### 3.2 `tools/gates/typed-pipelines.json` — a new first-match `d4` generation

**Moves.** Three of the five pinned fields in the first-match generation
`round-30-qreg-records`:

```
MOVED packet     examples/culture-d4/packet.d4.yml         aac91246cede -> fc46177a7150
MOVED projection examples/culture-d4/typed-labels.d4.yml  c23b0ab532cf -> 84e0f766c76f
same  assembler  tools/assemble-culture-d4.py             943f487ba991 -> 943f487ba991
same  adapter    tools/assemble-d4-typed.py               92f5460bcc34 -> 92f5460bcc34
MOVED expected   examples/culture-d4/expected-holds.json  e6ae9828d6c8 -> ee0cf710ff0c
```

**The self-reference, and the ordering that resolves it.** `expected.sha256` pins
`expected-holds.json`, which is *itself* edited by §3.1 — so writing §3.1 changes the
value §3.2 must record. D03 measured the failure mode (`FAIL L1-profile: expected: pins
e6ae9828d6c8, live d18ce2659fc8`) and the fix. **This seat confirms convergence with the
correct order: write `expected-holds.json` first, then pin its post-write digest in
`typed-pipelines.json`, then re-run the gate.** Result on `.scratch/d04-iso3`:

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
declared pipeline: family d4; profile tools/gates/typed-pipelines.json (sha256 94b4e62e…); …
ok   L3b-argot:
ok   L4-pins
summary: 20/20 legs passed          exit=0
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml
summary: 17/17 legs passed          exit=0
```

Converged in one pass under that order. A loop that pins `expected` *before* editing
`expected-holds.json` needs a second pass, and a loop that never re-checks leaves the tree
red — the same self-referential tool-pin subtlety r26 recorded (`SCORECARD.md:330`).

**Draft:** insert a **new first-match** generation (`round-36-register-doublets`) before the
existing `round-30-qreg-records` profile, exactly as round 30 did; the entire existing
`profiles` list remains byte-equivalent as the tail. `load_profile()` is first-match by the
packet's declared `assembly.generator`, so no ordering hazard. Fields moved: `packet.sha256`,
`projection.sha256`, `expected.sha256`. Fields unchanged: `assembler.sha256`, `adapter.sha256`.

### 3.3 `reports/round-34/handoff/declared-in-r7/expected.json` — **FILED: needs a SUCCESSOR, not an edit**

This is the load-bearing one and the hard boundary. The 58-member v3 read set pins **19 D4
surfaces**; the landing moves **5 of them**:

| # | read-set member | r7 pin | after | moved |
|---|---|---|---|---|
| 1 | `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b921…` | source digest | **yes** |
| 2 | `examples/culture-d4/packet.d4.yml` | `aac91246cede…` | packet digest | **yes** |
| 3 | `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cf…` | projection digest | **yes** |
| 4 | `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384…` | typed digest | **yes** |
| 5 | `examples/culture-d4/expected-holds.json` | `e6ae9828d6c8…` | holds digest | **yes** |

The remaining 14 D4 members (all twelve of components 01–12 except 04, `brief.md`,
`ASSEMBLY.md`, `tools/assemble-culture-d4.py`) do **not** move.

**Correction to the round's own count.** D02 §6 and D03 §5 both report "read-set files
whose digest the landing MOVES: 4 of 58", listing expected-holds, packet.d4.typed,
packet.d4 and typed-labels — but **omitting `examples/culture-d4/components/04-lexicon.yml`,
which is read-set member A-37**. The measured count is **5**, not 4. This seat's
independent census over the r7 `inputs` map (re-measured live, not read from prose):

```
$ python3 -c "…compare r7 expected.json inputs against the rebuilt copy…"
5
  examples/culture-d4/components/04-lexicon.yml
  examples/culture-d4/expected-holds.json
  examples/culture-d4/packet.d4.typed.yml
  examples/culture-d4/packet.d4.yml
  examples/culture-d4/typed-labels.d4.yml
```

Recorded as a named correction, not smoothed (`REGIMEN.md`: a trade is reported, never
averaged). It matters because the source component is the one row an integrator is most
likely to forget when the cascade is copied from a summary.

**Two further facts about the read set the integrator needs:**

- The read set pins components **01–12 only** — it does **not** contain
  `13-register-law.yml`, and it will not contain a new `14-register-forms.yml` under
  D02's route. A new component is therefore **unpinned** by the v3 read set; if the round
  lands component 14, the successor freeze should say so rather than imply coverage.
- `tools/gates/typed-pipelines.json` is **not** a read-set member, so §3.2 does not
  cascade into the read set.

**Draft (new row — the r7 bytes must not be edited):** freeze a successor generation, e.g.
`reports/round-36/handoff/declared-in-r8/{packet.md,twin.json,expected.json,freeze.txt,run.log,claims-map.md}`,
and re-point the renderer default. The precedent chain is explicit and four-deep:

```
reports/round-22/handoff/declared-in/        → declared-in-r2/
reports/round-25/v3-supersession/declared-in-r4/
reports/round-26/handoff/declared-in-r5/
reports/round-28/pinsweep/v3-baseline-r28/
reports/round-30/handoff/declared-in-r6/     → reports/round-34/handoff/declared-in-r7/
```

and r26 recorded the mechanism in the same words this seat uses: "successor frozen and
green … but the runner's regression uses the DEFAULT baseline"
(`reports/round-26/register/repin.json`). **A successor freeze alone does not fix the
regression; the default pointer must move with it.**

### 3.4 `tools/exercise-handoff-e2e.py` — the default pointer pair

Two constants must move **together** (round-34 K02's coupling), as a new row:

```
:1937  V3_BASELINE_DEFAULT   = "reports/round-34/handoff/declared-in-r7/expected.json"
:1938  V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"
```

Round 34's own re-point recorded the exact shape and the byte-preservation rule
(`reports/round-34/handoff/repin.json`, `R34-D-default-pointer`: `surface_sha256_before`
`a5e4a8c5…` → `after` `34c85f57…`, control `--profile v3 --quiet` exit 0). The same row
shape applies here, with the successor directory substituted. **Moving this pointer is a
tool edit — integrator-owned, drafted as a row, never applied by this seat.**

Measured consequence of *not* moving it, on `.scratch/d04-iso3`:

```
$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=1 … packet_sha256=(not assembled)
handoff-v3: E2E-DIGEST: 5 read-set file(s) changed since the baseline was frozen:
  examples/culture-d4/components/04-lexicon.yml, examples/culture-d4/expected-holds.json,
  examples/culture-d4/packet.d4.typed.yml …          exit=1
```

The refusal names five members, matching §3.3's corrected count. On the pristine copy the
same command is exit 0 — the causality control.

### 3.5 `reports/round-34/handoff/declared-in-r7/twin.json` — **FILED: successor row**

The twin's `artifact_manifest` pins the D4 tree explicitly. **Five rows move**:

| row | path | r7 pin | after |
|---|---|---|---|
| A-28 | `examples/culture-d4/packet.d4.yml` | `aac91246cede…` | `fc46177a7150…` |
| A-29 | `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384…` | `4adaf00790ef…` |
| A-30 | `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cf…` | `84e0f766c76f…` |
| A-31 | `examples/culture-d4/expected-holds.json` | `e6ae9828d6c8…` | `ee0cf710ff0c…` |
| A-37 | `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b921…` | `b4d71cd8e696…` |

A-32…A-36 and A-38…A-46 do not move. The twin is a read-set member, so it is regenerated
by the successor freeze rather than edited — same rule as §3.3.

### 3.6 `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` — **FILED: needs a successor generation**

All four rows pin the D4 packet/projection and snapshot their own input. Causality control,
run on the pristine copy and then on the landed copy with `TMPDIR=/var/tmp` (outside the
repo — inside-repo `TMPDIR` makes `replay-frozen.py` refuse with `mirror_unsafe`):

| state | command | observed |
|---|---|---|
| pristine `ce103bf` | `python3 tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4 rows reproduced the recorded verdicts` |
| after the landing | same | `REPLAY MISMATCH: 4 mismatch, 0 reproduced of 4 row(s)` |

```
ROW 2 mismatch gate=tools/gates/d4-assembly-check-gate.py        input=…/packet.d4.yml          exit=1/0
ROW 3 mismatch gate=tools/gates/d4-typed-labels-check-gate.py    input=…/typed-labels.d4.yml    exit=1/0
ROW 4 mismatch gate=tools/gates/typed-pipeline-gate.py           input=…/packet.d4.yml          exit=2/0
ROW 5 mismatch gate=tools/gates/typed-pipeline-gate.py           input=…/packet.d4.typed.yml    exit=2/0
```

**Draft:** a new generation, e.g. `reports/round-36/sweep/frozen/r36-post/`, built by the
same freeze script shape as `reports/round-31/sweep/freeze-r31.py`. That script **refuses to
re-freeze over an existing generation** ("A run refuses to re-freeze over an existing
generation; it re-verifies instead"), so the successor must be a new directory — which is
the same rule the r18→r28→r30→r31 chain already followed
(`reports/round-33/calib/r18-d4-adapter-successor.md`: "a successor is a NEW generation —
never an in-place edit").

---

## 4. Surfaces that do **not** need a new row (measured, so the list is honest)

Reporting these is part of the plan: an over-broad re-freeze list is its own defect.

| surface | why it needs no new row | evidence |
|---|---|---|
| `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` | Pins 13 D4 files **by mirror copy**, not by live path. The mirror still resolves inside the baseline, so the battery reads `pinned`. Its snapshot is **already stale** at HEAD (01-brief, 03-orthography, 04-lexicon, 09-costumes all differ from live *before* this landing) — the landing adds no new staleness. §3 of the standard explicitly allows "the live tree may move under them". | battery: `pinned 20`, `coverage 10/10`, `unevaluable 0`, `findings []` — before **and** after the landing |
| `tools/gates/expected/register-law-gate/r30-post/expected.json` | Same mirror mechanism; the law gate over the r30-post **snapshot** packet is still exit 0 (`record_ids=183`, `findings=0`) after the landing, because it grades the snapshot. The live packet now measures `record_ids=191` — a *new* measurement, not an invalidation. | `python3 tools/gates/register-law-gate.py tools/gates/expected/register-law-gate/r30-post/packet.d4.yml` → exit 0 |
| `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}` | All three are already exit 1 at HEAD (their mirrors pin pre-landing projections) — pre-existing, unchanged by this landing. | `… d4-typed-labels-check-gate.py <baseline>/typed-labels.d4.yml` → exit 1 in all three, at HEAD and after |
| `reports/round-26/remainders/r4-twin/twin.json` | Already **8 reds at HEAD**; after the landing it is still **8 reds, the same 8 paths**. The landing introduces no *new* mismatch here. | `packet_links.py --packet … --json \| grep -c M-DIGEST-MISMATCH` → `8` before and after |
| `tools/gates/frozen/round-18/MANIFEST.tsv`, `tools/gates/frozen/round-22/d4-repin/` | Filed historical generations; already superseded and named as such (`r18-d4-adapter-successor.md`). Filed bytes; never edited. | `reports/round-31/sweep/run-sweep.py` `CONTROLS` names them "superseded by later D4 landings (recorded reds stay red)" |
| `examples/culture-d4/ASSEMBLY.md` §5 pins table | **Already stale at HEAD** (01-brief, 03-orthography, 04-lexicon, 09-costumes pinned at pre-r26/r28/r30 values), and it is a read-set member whose bytes do not move. No machine check reads its §5 table (this seat found none — `to-verify`). | `for f in …/components/*.yml; do …` → 4 `STALE` rows at HEAD, unchanged after |
| `corpus/lessons/round-30.md` | Carries the packet digest in filed lesson prose; append-only, never edited. | hard boundary |
| `tools/assemble-culture-d4.py`, `assemble-d4-typed.py`, `d2-typed-labels.py`, `argot-derivation-gate.py`, `register-law-gate.py`, `typed-pipeline-gate.py`, `naming-collision-gate.py` | **No tool byte moves.** The content change is data-only. Verified by digest before/after. | §5 table |

---

## 5. The full row set at a glance

| # | surface | kind | action |
|---|---|---|---|
| 1 | `examples/culture-d4/components/04-lexicon.yml` | source content | edit (integrator applies D01 §5.1 / D02 component 14) |
| 2 | `examples/culture-d4/packet.d4.yml` | generated | regenerate |
| 3 | `examples/culture-d4/typed-labels.d4.yml` | generated | regenerate |
| 4 | `examples/culture-d4/packet.d4.typed.yml` | generated | regenerate (**`--emit PATH` required**) |
| 5 | `examples/culture-d4/expected-holds.json` | pin row | **new** `pin_generations` row + 2 scalar pointers |
| 6 | `tools/gates/typed-pipelines.json` | pin row | **new first-match** `d4` generation (3 fields) |
| 7 | `reports/round-34/handoff/declared-in-r7/expected.json` | **FILED** | successor freeze (`declared-in-r8`); 5 of 58 members |
| 8 | `reports/round-34/handoff/declared-in-r7/twin.json` | **FILED** | successor freeze; 5 manifest rows |
| 9 | `tools/exercise-handoff-e2e.py:1937-1938` | tool | re-point both defaults **together** (new row) |
| 10 | `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | **FILED** | successor generation (`r36-post`); 4/4 rows |

**Ordering (load-bearing):** 1 → 2 → 3 → 4 → 5 → 6 → (re-run gate to confirm convergence)
→ 7/8 → 9 → 10. Writing 6 before 5 leaves `expected.sha256` stale.

## 6. Post-landing leg state (the re-pinned copy is green)

On `.scratch/d04-iso3`, after the full re-pin:

| leg | command | observed | exit |
|---|---|---|---|
| derivation replay | `argot-derivation-gate.py …/packet.d4.yml` | `records=195 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| law gate | `register-law-gate.py …/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=191 registers=17 … dangling=0 findings=0` | 0 |
| typed pipeline (source) | `typed-pipeline-gate.py …/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| typed pipeline (typed) | `typed-pipeline-gate.py …/packet.d4.typed.yml` | `summary: 17/17 legs passed` | 0 |
| d4 assembly gate | `d4-assembly-check-gate.py …/packet.d4.yml` | `byte-identical deterministic assembly` | 0 |
| d4 typed-labels gate | `d4-typed-labels-check-gate.py …/typed-labels.d4.yml` | `byte-identical deterministic projection` | 0 |
| gate battery | `check-gate-battery.py` | `{battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}` / `coverage 10/10, pinned 20` | 0 |
| selftests | argot / law / assemble | `27/27`, `45/45`, `81/81` | 0 |

**The domain stays honest.** `register_scoped=14` and `derived_pairs=8` are unchanged by
the landing — the index block restates no derivation pair, so it inflates no graded
domain. This matches D03 §5b.3 independently.

## 7. Calibration and limits

- **A pin is integrity, never truth.** Every row above asserts *bytes moved*, not that the
  move was correct, not that the register-form index is well-designed, and never clearance.
- **The digest values in §2–§3 are this seat's copy's values, not transferable.** §2.3
  measures six different packet digests for one landing across five seats. The integrator
  re-measures on landed bytes; this fragment owes the **row set** and the **ordering**.
- **`reports/round-36/run-validation.py` does not exist** at write time (`ls` → no such
  file), so claim D's declared counting command could not be run. The per-leg commands in
  §6 stand in as the measured evidence. Recorded, not smoothed.
- **Two-pass hazard is real but order-dependent.** This seat converged in one pass with
  the §5 ordering; D03 measured a two-pass need on a different ordering. Both are recorded.
- **`to-verify`:** whether any machine check reads `examples/culture-d4/ASSEMBLY.md` §5's
  digest table. This seat found none by reading the tools that reference it; absence of
  evidence is recorded as `to-verify`, not as "unchecked".
- **In-tree state note (not this seat's write).** `git status --porcelain` shows
  ` M reports/round-34/validation.json` earlier and ` M reports/round-35/validation.json`
  at this seat's last check, plus `?? reports/round-36/`. Those modifications are other
  seats'/the integrator's; this seat wrote **only** `reports/round-36/depth/D04-repin.md`.
  HEAD is unchanged at `ce103bf5885af00023cdc4a174c17602476cdcf8`.

## Owed

- **`reports/round-36/depth/D02-packet-draft.md` §2.1 field-validation gap** — a
  `register_forms` block absent from `RECORD_FIELDS` gets only generic checks, so a row
  missing `lexicon_id`/`op` assembles silently. The `RECORD_FIELDS` diff is a tool change
  the integrator applies; D03 §5b.4 also left it unexercised. Owner: integrator.
- **The successor freeze itself** (§3.3/§3.4) — `declared-in-r8` plus the two renderer
  default constants. Owner: integrator (tool + filed-adjacent surfaces; this seat may not
  write `tools/exercise-handoff-e2e.py` or freeze a new baseline).
- **The `r36-post` sweep generation** (§3.6) — needs a new freeze run; owner: the round's
  O/integration seat.
- **Route decision** (D01's `doublets` in `04-lexicon.yml` vs D02's new
  `14-register-forms.yml` vs P01's Surface A+B-1) — §2.3 shows each yields a different
  digest chain, so the re-pin values cannot be fixed until the route is chosen. Owner:
  integrator / X00 / R03.
- **Whether a fresh `register-law-gate/r36-post` baseline is wanted** — §4 shows the
  existing r30-post baseline is *not* invalidated (mirror mechanism), so this is a
  candidate row, not an obligation. Owner: integrator.
- **`examples/culture-d4/ASSEMBLY.md` §5's already-stale digest table** — pre-existing, not
  this landing's, but it is the documentation surface a reader would trust. Recorded, not
  repaired (filed-adjacent live file; owner: integrator).

## Citations

Every number above is a command output. Commands ran from the lane root or an isolated
`git archive ce103bf` copy with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
unless a row says `TMPDIR=/var/tmp`.

**Archive provenance and baseline digests**

```
$ git rev-parse HEAD
ce103bf5885af00023cdc4a174c17602476cdcf8
$ mkdir -p .scratch/d04-iso && git archive HEAD | tar -x -C .scratch/d04-iso
$ cd .scratch/d04-iso && sha256sum examples/culture-d4/packet.d4.yml \
    examples/culture-d4/packet.d4.typed.yml examples/culture-d4/typed-labels.d4.yml \
    examples/culture-d4/expected-holds.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
```

**§2.1 the zero-tool-edit route**

```
$ grep -n "doublets" tools/assemble-culture-d4.py
81:    "registers", "doublets", "sayings", "oaths",
122:    "doublets": ("id",),
469:  - id: DB-01
$ python3 tools/assemble-culture-d4.py
Wrote examples/culture-d4/packet.d4.yml (103724 bytes)
$ python3 tools/assemble-culture-d4.py --check        # exit 0
$ grep -c "^doublets:" examples/culture-d4/packet.d4.yml   # 1
$ python3 tools/assemble-d4-typed.py --emit            # exit 2, "expected one argument" — the trap
$ python3 tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml
Wrote examples/culture-d4/packet.d4.typed.yml (110083 bytes, 12 routing row(s))
```

**§2.2/§2.3 the re-pinned chain and shape-dependence**

```
$ cd .scratch/d04-iso3 && sha256sum examples/culture-d4/components/04-lexicon.yml \
    examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
    examples/culture-d4/packet.d4.typed.yml examples/culture-d4/expected-holds.json \
    tools/gates/typed-pipelines.json
b4d71cd8e69647267991d12aa048c164409af5a1b5308cd059d92f700436d621  examples/culture-d4/components/04-lexicon.yml
fc46177a7150ae475c94a92d92ad9f4907024e37788688f4d51ec70d2301b9a2  examples/culture-d4/packet.d4.yml
84e0f766c76f1476b5bffb8537838e2970304d6b3d52ae91daf834f374a45570  examples/culture-d4/typed-labels.d4.yml
4adaf00790efdf40388705c2982a37336bfb98fafd100465ad779da731d44021  examples/culture-d4/packet.d4.typed.yml
ee0cf710ff0ca016b96b427f3523f5e8ec76dcee2bd4eaebbcce9eefe2d28ed0  examples/culture-d4/expected-holds.json
94b4e62ee2aeb8f4559d4615b9a955b4506a7d0fa9343de42792f50e98b56762  tools/gates/typed-pipelines.json
```

Shape-dependence: `.scratch/d04-iso` (comment header) packet `6cebab86f06733f1…`;
`.scratch/d04-iso2` (registry row updated) packet `a0c4bced98d32275…`, projection
`98e54aff036663fb…`, typed `df3fc507275cec45…`; D03 `3067107f4a8df6d3…` /
`5231e73be696b020…`; D02 `66c34ad5a4eb1f3a…`.

**§3.1/§3.2 the pin rows**

```
$ python3 -c "…compare typed-pipelines profiles[0] fields against live bytes…"
MOVED packet     examples/culture-d4/packet.d4.yml         aac91246cede -> fc46177a7150
MOVED projection examples/culture-d4/typed-labels.d4.yml  c23b0ab532cf -> 84e0f766c76f
same  assembler  tools/assemble-culture-d4.py             943f487ba991 -> 943f487ba991
same  adapter    tools/assemble-d4-typed.py               92f5460bcc34 -> 92f5460bcc34
MOVED expected   examples/culture-d4/expected-holds.json  e6ae9828d6c8 -> ee0cf710ff0c
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
summary: 20/20 legs passed      # exit 0 — convergence under the §5 ordering
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml
summary: 17/17 legs passed      # exit 0
```

The D4 self-pin set (`v3_verify_d4_pins`, `tools/exercise-handoff-e2e.py:2225-2252`) — 3 of
8 move: `typed-labels assembly.packet_sha256`, `expected-holds packet_sha256`,
`expected-holds projection_sha256`; the assembler/reader/serializer/projector pins do not.

**§3.3 the read-set census and the correction**

```
$ python3 -c "…r7 expected.json inputs re-measured against the landed copy…"
5
  examples/culture-d4/components/04-lexicon.yml
  examples/culture-d4/expected-holds.json
  examples/culture-d4/packet.d4.typed.yml
  examples/culture-d4/packet.d4.yml
  examples/culture-d4/typed-labels.d4.yml
$ python3 -c "…r7 expected.json inputs…"   # on the PRISTINE archive
0
```

Read-set membership (`tools/exercise-handoff-e2e.py:151-181`, `:1939-1963`): 19 D4 members,
components 01–12 only; `13-register-law.yml` and `tools/gates/typed-pipelines.json` are
**not** members. `reports/round-34/handoff/declared-in-r7/freeze.txt`: "read set: 58 files;
component digests 26/26; d4 pins 8/8". Filed corrections this seat corrects:
`reports/round-36/depth/D02-packet-draft.md` §6 and `reports/round-36/depth/D03-isolated-verify.md`
§5 ("4 of 58").

**§3.4 the default pointer and its failure mode**

```
$ grep -n "V3_BASELINE_DEFAULT\|V3_FROZEN_DIR_DEFAULT\|CLAIMS_MAP" tools/exercise-handoff-e2e.py
188:CLAIMS_MAP = "reports/round-34/handoff/declared-in-r7/claims-map.md"
1937:V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"
1938:V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"
$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet     # landed copy
handoff-v3: E2E-DIGEST: 5 read-set file(s) changed since the baseline was frozen: …
exit=1
```

Precedent row shape: `reports/round-34/handoff/repin.json` `R34-D-default-pointer`
(`surface_sha256_before a5e4a8c5…` → `after 34c85f57…`, control exit 0).

**§3.5 the twin manifest**

```
$ python3 -c "…twin.json artifact_manifest rows re-measured…"
MOVED A-28 examples/culture-d4/packet.d4.yml           aac91246cede -> fc46177a7150
MOVED A-29 examples/culture-d4/packet.d4.typed.yml     d581e0ad5384 -> 4adaf00790ef
MOVED A-30 examples/culture-d4/typed-labels.d4.yml     c23b0ab532cf -> 84e0f766c76f
MOVED A-31 examples/culture-d4/expected-holds.json     e6ae9828d6c8 -> ee0cf710ff0c
MOVED A-37 examples/culture-d4/components/04-lexicon.yml ed7093d6b921 -> b4d71cd8e696
```

**§3.6 the sweep generation and its causality control**

```
$ TMPDIR=/var/tmp python3 tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv
# pristine copy:  REPLAY OK: 4/4 rows reproduced the recorded verdicts
# landed copy:    REPLAY MISMATCH: 4 mismatch, 0 reproduced of 4 row(s)
```

Successor rule: `reports/round-31/sweep/freeze-r31.py` docstring ("A run refuses to
re-freeze over an existing generation; it re-verifies instead"); precedent
`reports/round-33/calib/r18-d4-adapter-successor.md` ("a successor is a NEW generation —
never an in-place edit").

**§4 the surfaces that need no new row**

```
$ python3 tools/check-gate-battery.py | …   # landed copy
{baseline_exit: 0, baselines_found: 20, coverage: "10/10", pinned: 20, unevaluable: 0,
 readings: {pinned: 20}, gates_uncovered: []}   findings []
$ python3 tools/gates/register-law-gate.py tools/gates/expected/register-law-gate/r30-post/packet.d4.yml
coverage: …/r30-post/packet.d4.yml law_rows=5 identity_rows=8 record_ids=183 … findings=0   # exit 0
$ python3 tools/harness/packet_links.py --packet reports/round-26/remainders/r4-twin/twin.json --json \
    | grep -c M-DIGEST-MISMATCH
8      # identical before and after the landing
$ for f in examples/culture-d4/components/*.yml; do …done   # ASSEMBLY.md §5 table
STALE 01-brief.yml / 03-orthography.yml / 04-lexicon.yml / 09-costumes.yml   # already stale at HEAD
```

Battery mirror resolution (`tools/check-gate-battery.py:568-596`): an input resolving
inside the baseline reads `pinned`; only a copy-absent input falls back to the fixed roots
and raises `BASELINE-EXTERNAL-INPUT`.

**§6 post-landing legs** — outputs quoted verbatim in the §6 table; all exits 0.

**Standard and precedent authority**

- `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (byte copy, "the live tree
  may move under them"), §4 (`inputs` map, append-only), §5 (freeze procedure), §6
  (`snapshot_tampered` / `gate_revised` / `unpinned (legacy)`), §10 (digests are integrity,
  not truth).
- `reports/round-26/register/repin.json` — the successor-freeze precedent and the
  "runner's regression uses the DEFAULT baseline" mechanism.
- `reports/round-30/fixes/qreg-dangles.md` — the last successful D4 pin cascade: new
  first-match profile, `pin_generations` rows, two-scalar-pointer advance, hold set 12/0/0.
- `reports/round-34/handoff/repin.json` — the renderer-default re-point row shape.
- `SCORECARD.md:330` — the r26 self-referential tool-pin subtlety.
- `REGIMEN.md` — "a trade is reported, never averaged into an accept"; the
  hard-boundary list.
