- Seat: K02 | scout | claim O | date 2026-10-19 | baseline 9bccc9b

# R38-K02 — roster-guard scout: how `V3_READ_SET` is built, where the manifest lives, and where the guard belongs

**Mission (verbatim, `reports/round-38/targets.json` seat `K02`):** "Roster-guard scout: how
`v3_freeze` builds the read set (`V3_READ_SET`), where the packet manifest lists components, and
the cleanest guard point; the r7 row's current behavior under the guard (expect: named, not
failed)."

**Write scope.** This file only. No tool, gate, packet, component, fixture, pin, expectation row
or filed round-1..37 byte written; `git status --porcelain` at the stamp reads only
`?? reports/round-38/`. Every control below ran under `.scratch/k02/` (gitignored, built by
`git archive HEAD | tar -x`); the live tree was read, never executed against. No commit, no push,
no install, no network. **No `reports/round-*/run-validation.py` was executed anywhere**, in-tree
or in a copy (F-C13-1); `reports/round-38/run-validation.py` does not exist at this stamp
(`ls` → No such file), so claim O's declared counting command `python3 reports/round-38/run-validation.py`
is `to-verify` and this file uses the underlying renderer commands instead. No re-freeze of
`reports/round-34/handoff/declared-in-r7` — its six filed bytes measure unchanged.

**Stamp.** `date -u +%FT%TZ` → **2026-10-19T11:14:19Z**; `git rev-parse --short HEAD` → `9bccc9b`
(`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`). All measurements from lane root with
`TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`.

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, never clearance.

**Dependencies read from the landed set:** `scout/K01-residue.md` (D-block residue scout),
`op/O04-fix-route.md`, `op/O05-verify-route.md`, `review/R02-o-review.md`, `review/R03-cross-review.md`,
`cross/X02-honesty.md`, `adj/A01-scope.md`. This fragment answers the two questions R03-C1 and R02
left open (which manifest surface the guard must read; which comparison pair it must use) with
measurements, and it falsifies two sibling thresholds.

---

## 0. Headline

1. **The guard reads the source packet, and it works.** `assembly.d4["components"]` — mined at
   `tools/exercise-handoff-e2e.py:2054` from `assembly.source_sha256` — carries **13** members.
   Subtracting `set(V3_READ_SET)` (58) yields exactly one row,
   `examples/culture-d4/components/13-register-law.yml`. **R03-C1's blocking concern is satisfied by
   the guard point this seat measured**: the rendered `reports/round-34/handoff/declared-in-r7/packet.md`
   carries only 12 D4 component rows, so a guard written against the rendered text would pass forever.
2. **All three candidate comparison pairs collapse to the same single gap today.** manifest-vs-read-set,
   manifest-vs-`D4_COMPONENTS`, and `D4_COMPONENTS`-vs-read-set each yield exactly
   `13-register-law.yml` — because `D4_COMPONENTS` is itself exactly the 12 manifest members that the
   read set carries. The pair choice is therefore **not** a today-discriminated decision; it only
   diverges after the fix lands (O04/O05 §D-1). The read-set-relative pair is the one that stays
   correct in both worlds.
3. **The r7 row's behavior under the guard is `named, not failed` — as the claim expects.** Guarded
   r7 default chain → **exit 0**, packet `45f57132…` byte-unchanged, and one new record:
   `component-roster ok=False` naming the member. The guard is D4-scoped and record-only (it never
   raises), which is what keeps the filed chain green.
4. **A global manifest-vs-read-set guard is a 7-row false-red machine** (6 D2 members + the D4 one),
   reproducing R02's Finding 2 independently at this baseline. The guard must be D4-scoped.
5. **New finding, and it falsifies two sibling thresholds.** Under the guard, **six** filed rows
   carry the gap, not one: r2 `declared-in`, r2 `declared-in-r2`, r5, r6, r20 **and** r7. Five of
   them name it and then abort on `E2E-READSET` (their superseded `claims-map.md` member) **before**
   the new check can be reached. So `targets.json` O08's "only the r7 row names; others stay green"
   is **false**, X02 §4a's "r6 and r7 name; r2/r5 green" is **false**, and A01 §3d's "the r7 row
   will fire" is true only under the refuse-variant it warns against. The distinguishing fact is
   **ordering plus r7's unique lack of a superseded member**, measured below.

---

## 1. How the read set is built

`V3_READ_SET` (`tools/exercise-handoff-e2e.py:1939-1963`) is a module-level tuple built by
splicing named constants:

```python
V3_READ_SET = (
    *V1_READ_SET, V2_PACKET_MD, V2_PACKET_YML,
    "examples/culture-d2/components/05-lexicon.yml",   # 4 D2 inputs, literal
    ... , D4_PACKET, D4_TYPED_PACKET, D4_TYPED_LABELS, D4_HOLDS, D4_BRIEF, D4_ASSEMBLY,
    *D4_COMPONENTS,                                    # ← the 12-member tuple, :157-170
    D4_ASSEMBLER, D4_TYPED_TOOL, D4_TYPED_GATE, D4_ASSEMBLY_GATE, D4_READER,
    *D4_RECEIPTS, *HARNESS, CLAIMS_MAP, "reports/round-19/validation.json",
)
```

Measured live (`runpy` over the module, read-only):

```
V3_READ_SET len 58   unique 58
D4_COMPONENTS len 12
D4 members in read set: 12
13-register-law in V3_READ_SET: False
13-register-law in D4_COMPONENTS: False
CLAIMS_MAP  = reports/round-34/handoff/declared-in-r7/claims-map.md
V3_BASELINE_DEFAULT     = reports/round-34/handoff/declared-in-r7/expected.json   (:1937)
V3_FROZEN_DIR_DEFAULT   = reports/round-34/handoff/declared-in-r7                (:1938)
```

`v3_freeze` (`:3997-4145`) does not *derive* the read set; it **consumes the module tuple**. Its
`inputs` map is `{rel: assembly.digests[rel] for rel in V3_READ_SET}` (`:4038`), and `V3Assembly.__init__`
populates `digests` by iterating the same tuple (`:3485-3488`). So the tuple is the single source of
truth for both the read set and the frozen row, and the packet's `A-NN` artifact manifest is a
projection of it (`:2585`, `{rel: f"A-{i:02d}"}`), with `assert_manifest_equality` requiring
`checked == len(V3_READ_SET)` (`:3661-3662`).

**Consequence for the guard:** the packet's *artifact* manifest (`A-NN`, 58 rows) is read-set-derived
and trivially in sync — it can never carry the defect. This confirms O04 §1 and R02 Finding 1 from a
second seat.

---

## 2. Where the packet manifest lists components

The source packet's own component manifest is the `assembly.source_sha256` block
(`examples/culture-d4/packet.d4.yml:2875` header, rows at `:2876-2888`), **13 entries**, the 13th being:

```
examples/culture-d4/packet.d4.yml:2888
  "examples/culture-d4/components/13-register-law.yml": "c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7"
```

The renderer already mines it at `:2054`:

```python
assembly = blocks["assembly"]
components = dict(re.findall(r'^\s{4}"([^"]+)":\s*"([0-9a-f]{64})"', assembly, re.M))
```

and exposes it as `self.d4["components"]` (`:3505`, from `v3_mine_d4` at `:2045-2056`).
`v3_verify_component_digests` (`:2208-2222`) already iterates all 13 and raises `E2E-DIGEST` on
changed bytes.

**The three manifest surfaces, measured, and which one the guard must not use:**

| surface | where | members | carries the 13th? |
|---|---|---|---|
| `assembly.source_sha256` (source packet) | `packet.d4.yml:2875-2888` | **13** | **yes** |
| rendered `packet.md` manifest table | `reports/round-34/handoff/declared-in-r7/packet.md:39+` | 12 D4 rows | **no** (R03 §3.1) |
| packet `artifact_manifest` (`A-NN`) | `packet.d4.yml:3203`; built `:2585` | 58, read-set-derived | n/a — always in sync |

So R03-C1 resolves in favour of `assembly.d4["components"]`, which the draft below uses.

---

## 3. The cleanest guard point

`v3_exercise` (`:3811-3994`) already contains one roster check, and it is **one-directional**:

```python
:3823   dropped = sorted(rel for rel in baseline["inputs"] if rel not in assembly.digests)
:3826-3838   for rel in dropped: record("read-set-roster", False, …)
             raise Failed("E2E-READSET", …)
```

It tests *baseline-named member ∉ live read set* (the superseded-row class). The r7 defect is the
**inverse** direction: *manifest member ∉ read set*. The new check belongs at the same site, and
**ordering matters** — see §5.

**Recommended insertion: immediately after `assembly = V3Assembly(root)` (`:3821`) and before the
`dropped` block (`:3823`).** Rationale: `assembly.d4["components"]` is available there; the existing
`E2E-READSET` refusal keeps priority over the new record; and the new check is then reachable on
every row that reaches the digest legs at all. The measured consequence of this choice — and the
alternative — is quantified in §5.2.

---

## 4. Measured controls

All in `.scratch/k02/{base,g,gsync,gafter,gman}`, fresh `git archive 9bccc9b` copies.

### 4.1 Baseline (unpatched), for comparison

```
.scratch/k02/base   python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
            statuses=16/7/4 v2_subset=equal alias_leg=landed
            packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
.scratch/k02/base   … --profile v3 --selftest  → exit 0, "plus 43 controls"
```

### 4.2 Control 1 — the r7 row is **named, not failed** (the mission's expectation)

```
.scratch/k02/g   python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
exit 0

.scratch/k02/g   … --json --quiet
GUARDED r7 row: exit 0 code None   (16 records, non-ok: ['component-roster'])
  component-roster ok=False |
  examples/culture-d4/components/13-register-law.yml: recorded in the packet component manifest
  (assembly.source_sha256) but not a member of the live read set (58 members) — the roster is
  incomplete (this is not the superseded-row class)
```

Packet sha byte-identical to baseline; the new record names exactly one row; exit 0.

### 4.3 Control 2 — the synced fixture is green

`.scratch/k02/gsync`: the 13th path spliced into `D4_COMPONENTS` (read set 59), then re-frozen into
a scratch baseline.

```
readset len 59 | D4_COMPONENTS len 13
… --freeze .scratch-freeze            → exit 0
… --quiet --baseline .scratch-freeze/expected.json
handoff-v3: exit=0 … packet_sha256=7f0e47909a77ad7f2d82507e8d64b6476a0152e3177d3c45e9d3ef36ba9468ff

SYNCED row: exit 0 code None   (16 records, all ok)
  component-roster ok=True | all 13 manifest components are read-set members
```

`7f0e4790…` matches O04's variant-A packet digest and O05's independent reproduction exactly — a
third seat's confirmation of the read-set-edit cascade. The guard goes green on the synced tree, so
it is not a permanent red.

### 4.4 Control 3 — the full selftest survives the guard

```
.scratch/k02/g   python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest → exit 0
selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105,
          claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 43 controls
```

Same **43** controls as the unpatched tree — the guard adds a *record*, not a control, so the claim's
"selftest green with the new controls" is satisfied only in the sense that the new coverage is a
recorded row. **If the O block's threshold requires a new selftest control, it must be written
separately** (see Owed).

**Note (record-only trade, measured):** the selftest's own positive run runs against the fixture
tree, whose read set is the live 58-member tuple, so its `component-roster` record is `ok=False` too:

```
selftest POSITIVE run: exit 0 code None
  component-roster ok=False | …13-register-law.yml… not a member of the live read set (58 members)
  non-ok records in the positive run: ['component-roster']
```

The assertion at `:4193-4194` checks `code == EXIT_PASS`, not "every record ok", so the control
matrix passes. But it means the round cannot claim "selftest green **with the new control**" from the
record's `ok` value alone — the record is honestly red until the read set is fixed. **That is the
non-vacuity property: the guard's output tracks the defect rather than a constant.**

### 4.5 Control 4 — the guard reads the packet, not a constant (non-vacuity)

`.scratch/k02/gman`: the `13-register-law.yml` row deleted from `assembly.source_sha256`.

```
MANIFEST-MUTATED row: exit 1 code E2E-DIGEST
  verdict: examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256: the tree recorded
           aac91246cede… for examples/culture-d4/packet.d4.yml but the bytes measure 0809…
```

Removing the manifest row moves the packet digest, and the D4 pin leg refuses before the new check
is reached. This proves the guard's input is genuinely the packet's manifest bytes — **a guard keyed
on the constant `D4_COMPONENTS` alone would not have noticed this edit.**

### 4.6 Control 5 — the pair choice and the scope boundary

```
P1  set(assembly.d4["components"]) - set(V3_READ_SET)     → ['…/13-register-law.yml']   (1)
P2  set(assembly.d4["components"]) - set(D4_COMPONENTS)   → ['…/13-register-law.yml']   (1)
P3  set(D4_COMPONENTS) - set(V3_READ_SET)                 → []                          (0)
    set(V3_READ_SET ∩ culture-d4/components) - manifest    → []                          (0)

per-tree manifest vs V3_READ_SET:
  D2: manifest 9  | not-in-read-set 6  | read-set component not-in-manifest 1 (12-rank-rules.yml)
  D3: manifest 4  | not-in-read-set 0  | 0
  D4: manifest 13 | not-in-read-set 1  | 0
GLOBAL (D2 ∪ D3 ∪ D4) - V3_READ_SET → 7 rows
```

**Scope verdict.** A global guard reddens 7 legitimate rows — a harm to operability and a violation
of the claim's own "no new false reds". **D4-scoped is mandatory**, independently reproducing R02
Finding 2. **Pair verdict.** P1/P2/P3 agree today. They diverge only post-fix: if the fix appends the
member to `V3_READ_SET` **without** touching `D4_COMPONENTS` (O05 §D-1's variant B), then P3 stays
**red** (12 vs 13) while P1 and P2 go green. P1 is the pair that is correct in both worlds, because
the read set — not the constant tuple — is what the packet is assembled against. **Recommend P1:
`set(assembly.d4["components"]) - set(V3_READ_SET)`.** This resolves R02's "O01/R02/R03 should pick
the pair deliberately" and answers R03-C1's "the guard reads the roster, not the packet" in the
opposite direction from R03's own worry: it reads **both**, and the packet half is the source.

---

## 5. New finding — six filed rows carry the gap, and ordering is what discriminates

### 5.1 Census (read-only, live tree; every filed v3 baseline)

| filed baseline | inputs | members not in the live read set | manifest members not in the row's inputs |
|---|---|---|---|
| `reports/round-20/handoff/expected.json` | 58 | 1 (`reports/round-20/handoff/claims-map.md`) | 1 (`13-register-law.yml`) |
| `reports/round-22/handoff/declared-in/expected.json` | 58 | 1 | 1 |
| `reports/round-22/handoff/declared-in-r2/expected.json` | 58 | 1 | 1 |
| `reports/round-26/handoff/declared-in-r5/expected.json` | 58 | 1 | 1 |
| `reports/round-30/handoff/declared-in-r6/expected.json` | 58 | 1 | 1 |
| `reports/round-34/handoff/declared-in-r7/expected.json` | 58 | **0** | **1** |

Every row is missing the 13th component from its `inputs`; only r7 has no superseded member.
(For r2/r5/r6 the superseded member is `reports/round-20/handoff/claims-map.md`, matching R02
Finding 5.)

### 5.2 Replayed through the guarded copy

**Insertion before the `dropped` block (`:3823`) — the recommended point:**

| row | exit | code | `component-roster` records | `read-set-roster` records |
|---|---|---|---|---|
| r20 | 1 | `E2E-READSET` | 1 | 1 |
| r2 `declared-in` | 1 | `E2E-READSET` | 1 | 1 |
| r2 `declared-in-r2` | 1 | `E2E-READSET` | 1 | 1 |
| r5 | 1 | `E2E-READSET` | 1 | 1 |
| r6 | 1 | `E2E-READSET` | 1 | 1 |
| **r7** | **0** | **None** | **1** | **0** |

**Insertion after the `dropped` block (the alternative):**

| row | exit | code | `component-roster` | `read-set-roster` |
|---|---|---|---|---|
| r6 | 1 | `E2E-READSET` | **0** | 1 |
| **r7** | **0** | **None** | **1** | **0** |

The after-`dropped` placement still leaves the guarded selftest at exit 0 (43 controls), measured.

**Reading.** Neither placement produces "only the r7 row names" as a *record-count* claim: six rows
carry the gap, and the record is written for five of them under the recommended point. What
distinguishes r7 is (a) it is the only row with **no** superseded member, so it is the only one that
reaches a **green** exit, and (b) it is the only row where the naming record is not preceded by a
refusal. The after-`dropped` placement is the one that yields the literal O08 shape ("only r7 names,
others stay green"), at the cost of suppressing the record on rows that abort earlier — which is a
*reporting* suppression, not a detection change (those rows are already red for an independent
reason).

**This falsifies two sibling thresholds:**

- `targets.json` O08: "every filed frozen row (r2..r7) replayed in isolation under the guard — only
  the r7 row names; others stay green." **False**: r2/r5/r6/r20 are red `E2E-READSET` before the
  guard, and under the recommended placement they also emit the new record. X02 §4a's narrower
  "r6 and r7 name; r2/r5 green" is **also false** — r2 `declared-in`, r2 `declared-in-r2`, r5 and r20
  are red too. (X02 was right that "only r7 names" is unsatisfiable; it under-counted which rows are
  affected.)
- A01 §3d: "a guard which *refuses* on that condition will fire on the r7 row." **True but
  incomplete** — it fires on six rows; r7 is merely the only one it can *reach* without an earlier
  abort, and the only one whose exit stays green. A01's recommendation to *name without refusing*
  is correct and is what the draft below implements.

---

## 6. Draft patch (fenced — integrator applies; **NOT APPLIED**)

```python
# DRAFT — reports/round-38/scout/K02-roster-guard.md §6; NOT APPLIED.
# tools/exercise-handoff-e2e.py, in v3_exercise, immediately after
# `assembly = V3Assembly(root)` (:3821) and before the existing `dropped` block (:3823).
# Comparison pair P1 (§4.6): the packet's own component manifest versus the live read set.
# D4-scoped (a global guard reddens 7 legitimate rows, §4.6) and record-only (never raises,
# so the filed r7 chain stays exit 0, §4.2).
        # component-roster guard: a member the packet's own component manifest
        # (`assembly.source_sha256`, mined at :2054) records but the direct read
        # set omits. Distinct from the superseded-row class below, which reads the
        # opposite direction (baseline inputs vs the live read set).
        roster_gap = sorted(set(assembly.d4["components"]) - set(V3_READ_SET))
        if roster_gap:
            for rel in roster_gap:
                record(
                    "component-roster",
                    False,
                    f"{rel}: recorded in the packet component manifest (assembly.source_sha256) "
                    f"but not a member of the live read set ({len(V3_READ_SET)} members) — "
                    "the roster is incomplete (this is not the superseded-baseline-row class)",
                )
        else:
            record(
                "component-roster",
                True,
                f"all {len(assembly.d4['components'])} manifest components are read-set members",
            )
```

**Inventory prose the landing must also bring in line (docstring only, no digest impact):**
`tools/exercise-handoff-e2e.py:52` ("the twelve D4 components") and `:59` ("— 58 files."); the
renderer's own generated prose at `:2703`, `:2783`, `:2885`, `:2938` already says "thirteen" in the
`:2783` cell only. `:2578`'s row-role label is what O05 §D-1 measured as the functional difference
between insertion variants.

**Optional selftest control (if the O block requires one rather than a record).** The gate's own
discipline for a new clause is a two-direction control. A control added to `v3_selftest` beside the
read-set legs `m13a`/`m13b` (`:4444-4495`) would be:

```python
# DRAFT — reports/round-38/scout/K02-roster-guard.md §6; NOT APPLIED.
        # A1: a fixture whose read set omits a manifest member names exactly that member,
        #     and the run still exits 0 (the record is not a refusal).
        # B1: the synced fixture (13 components) records ok=True.
        # Both fixtures are built by the existing v3_build_fixture_root (:4149-4162) after
        # the member is spliced into D4_COMPONENTS — the fixture copies V3_READ_SET, so the
        # synced case must be produced by the patched tuple, not by editing the fixture.
```

This is `to-verify` until an executor lands it: this seat did not write it, and §4.4 measured that
the record-only guard changes the selftest's control count by **zero** (43 → 43).

---

## 7. What this seat did **not** do

- Did not write, edit or create any tool, gate, packet, component, fixture, pin, expectation row or
  frozen baseline. Every patch exists only inside `.scratch/k02/*` (gitignored).
- Did not run any `reports/round-*/run-validation.py` anywhere (F-C13-1); none exists for round 38.
- Did not re-freeze or touch `reports/round-34/handoff/declared-in-r7` — the six filed bytes measure
  unchanged (`expected.json bbe15887…`, `packet.md 45f57132…`, `twin.json 0e229138…`).
- Did not decide any contested item. Specifically: which comparison pair O01 lands (§4.6 recommends
  P1, does not decide), whether the O block ships a record or a selftest control (§6 offers both),
  and whether the r7 row's naming is cleared by a successor baseline (O04/O05 own that route).
- Did not edit `reports/round-38/claims.json`, `targets.json` or any filed round-1..37 byte.
- Did not commit, push, install, or reach the network.

---

## Owed

- **O01/O02 executor — the pair and the placement are now measured, not assumed.** Land P1
  (`set(assembly.d4["components"]) - set(V3_READ_SET)`) at `:3821`, D4-scoped, record-only. Evidence:
  §4.2, §4.3, §4.6. If a different pair or placement is chosen, re-run §4.6's per-tree census and
  §5.2's replay, because P2 goes green under O05's variant B while P1 does not, and the
  after-`dropped` placement changes which rows emit the record.
- **O08 executor — its threshold is falsified as written.** Rewrite from "only the r7 row names;
  others stay green" to the §5 form: "six filed rows carry the gap; under the guard only r7 exits
  green, and r2/r5/r6/r20 are red `E2E-READSET` for the pre-existing superseded-member class, before
  the new check." Do not report the five pre-existing reds as guard regressions.
- **X02 honesty critic — its §4a count is short by four rows.** The affected set is
  {r20, r2 `declared-in`, r2 `declared-in-r2`, r5, r6, r7}, not {r6, r7}; and r2/r5 are **not** green.
  Evidence: §5.1.
- **R03-C1 — resolved, not merely flagged.** The guard reads `assembly.d4["components"]`
  (`packet.d4.yml`'s `assembly.source_sha256`), not the rendered `packet.md`; §4.5's manifest-deletion
  control shows the input is the packet bytes, not a constant. R03 should close C1 against this
  measurement or state what remains open.
- **If the O block requires a selftest control rather than a record:** the draft in §6 is unmeasured
  and unlanded; the executor owns it. Evidence that it is owed: §4.4 measured 43 → 43 controls.
- **`reports/round-38/run-validation.py` does not exist** at this stamp, so claim O's declared
  counting command is `to-verify`. Owner: the r38 validation-leg seat (S01).
- **Not measured by this seat:** whether the successor-baseline re-freeze (O04 §4 variant C) can land
  in round 38 at all (A01 §3c and O05 §5 both route that to the integrator), and whether
  `tools/gates/expected/` needs a new generation for the **renderer** — the battery's
  `REGISTERED_GATE_NAMES` (`tools/check-gate-battery.py:117-132`) lists gate scripts only and does
  **not** include `tools/exercise-handoff-e2e.py`, so editing the renderer costs no battery baseline
  (`python3 -B tools/check-gate-battery.py` → exit 0, `pass 7 / fail 0 / unevaluable 0`, unchanged).

## Citations

**Files (sha256 measured 2026-10-19T11:14:19Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):**

```
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
```

**Source lines cited:** `tools/exercise-handoff-e2e.py:51-59,157-170,1937-1938,1939-1963,2045-2056`
(`:2054` the manifest regex), `:2208-2222,2255-2262,2570,2578,2585,2588,2703,2783,2885,2938,3485-3488,3505,3608,3661-3662,3811,3821,3823,3826-3838,3951-3957,3997,4038,4149-4162,4165-4169,4193-4194,4444-4495`;
`examples/culture-d4/packet.d4.yml:2875-2888` (manifest; `:2888` the 13th row), `:3203`;
`examples/culture-d4/ASSEMBLY.md:12-24`;
`reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt,claims-map.md}`;
`tools/check-gate-battery.py:117-132,528-547`;
`reports/round-38/{claims.json,targets.json}` (claim O, seats K02/O01/O02/O08);
`reports/round-38/scout/K01-residue.md`; `reports/round-38/op/O04-fix-route.md` §1-§6;
`reports/round-38/op/O05-verify-route.md` §1-§5; `reports/round-38/review/R02-o-review.md`
Findings 1-5; `reports/round-38/review/R03-cross-review.md:32-33,92-160`; `reports/round-38/cross/X02-honesty.md:158-231`;
`reports/round-38/adj/A01-scope.md:120-140`.

**Commands run (all from lane root or the named copy; `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`):**

```
# §1-§2 — read-set and manifest census (read-only, live tree)
python3 -B -c "runpy tools/exercise-handoff-e2e.py; len(V3_READ_SET)"        # 58 unique, 12 D4 components
python3 -B -c "runpy v3_mine_d4('.'); components"                            # 13 members
python3 -B -c "set(components) - set(V3_READ_SET)"                           # ['…/13-register-law.yml']

# §4 — controls in isolated git archive copies of 9bccc9b
mkdir -p .scratch/k02/base && git archive HEAD | tar -x -C .scratch/k02/base
.scratch/k02/base  python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet      # exit 0, 45f57132…
.scratch/k02/base  python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest   # exit 0, plus 43 controls
.scratch/k02/g     (guard drafted at :3821)  … --profile v3 --quiet                   # exit 0, 45f57132…
.scratch/k02/g     … --json --quiet          # exit 0; component-roster ok=False naming 13-register-law.yml
.scratch/k02/g     … --profile v3 --selftest # exit 0, plus 43 controls
.scratch/k02/g     runpy v3_build_fixture_root + v3_freezed_copy + v3_exercise
                                             # positive run exit 0; component-roster ok=False
.scratch/k02/gsync (13th spliced into D4_COMPONENTS; read set 59) … --freeze → exit 0
.scratch/k02/gsync … --quiet --baseline .scratch-freeze/expected.json                # exit 0, 7f0e4790…
.scratch/k02/gsync … --json --baseline …     # component-roster ok=True, all 13 are read-set members
.scratch/k02/gman  (13th row deleted from assembly.source_sha256) … --json --quiet   # exit 1 E2E-DIGEST
.scratch/k02/gafter (guard moved after the dropped block) … --json --quiet --baseline r6  # exit 1, roster 0
.scratch/k02/gafter … --json --quiet --baseline r7   # exit 0, roster 1
.scratch/k02/gafter … --profile v3 --selftest        # exit 0, 43 controls

# §5 — every filed v3 baseline, replayed in the guarded copy
for row in round-20/handoff/expected.json round-22/handoff/{declared-in,declared-in-r2}/expected.json \
           round-26/handoff/declared-in-r5/expected.json round-30/handoff/declared-in-r6/expected.json \
           round-34/handoff/declared-in-r7/expected.json; do
  python3 -B tools/exercise-handoff-e2e.py --profile v3 --json --quiet --baseline "$row"; done
# → 5× exit 1 E2E-READSET (roster 1 + superseded 1), r7 exit 0 (roster 1, superseded 0)

# §7 — the untouched tree
python3 -B tools/check-gate-battery.py                                       # exit 0, pass 7 / fail 0 / unevaluable 0
git status --porcelain                                                       # only "?? reports/round-38/"
sha256sum (filed bytes, unmoved)                                             # as listed above
```
