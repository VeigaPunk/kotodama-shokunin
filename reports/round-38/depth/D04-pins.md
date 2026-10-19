- Seat: D04 | executor (claim D, pins plan) | every expected/frozen/baseline row the new register coverage touches, each as a NEW-row draft | date 2026-10-19 | baseline 9bccc9b

# D04 — the pin re-freeze list for the r38 register coverage, measured not inferred

**Mission (binding, `reports/round-38/targets.json`, seat `D04`):** "Pins plan: every
expected/frozen/baseline row the new coverage touches, as new-row drafts."

**Write scope.** This file only. All mutation under `.scratch/d04-*` (gitignored). No filed
1–37 byte written, no `corpus/lessons/*.md`, no `tools/gates/frozen/**`, no fleet `.ufo/**`,
no commit, no push, no install, no network. **No `reports/round-*/run-validation.py` executed
in-tree or in any copy (F-C13-1)**; no `--freeze` of `reports/round-34/handoff/declared-in-r7`.
Every command ran from the lane root or an isolated `git archive HEAD` copy with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` unless a row says `TMPDIR=/var/tmp`.

**Baseline.** `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`;
`git status --porcelain` → `?? reports/round-38/` only (plus the untracked round-38 fragments
other seats land concurrently). Every digest below was re-measured on these bytes, and the
D4 chain digests are byte-identical to the r36 record (`reports/round-36/depth/D04-repin.md`
§2.2 "before" column), so the r36 row set transfers and is extended here for the two surfaces
r36 did not reach.

**Why measured, not derived.** A re-pin list built from prose is exactly the failure the gate
standard forbids ("claimed ≠ re-executed", KTD-FR-S-0001). So this seat applied each candidate
landing in its own isolated copy and re-ran every pin-reading surface. The digests below are
**outputs**. Because digests are content-dependent, the **row set and the ordering** are what
this seat owes; the digest values must be re-measured by the integrator on the bytes actually
landed.

---

## 0. Headline — the two claims have disjoint pin cascades, and F-6 has two routes

The D claim names two residues: **F-6** (the `derived_forms`/`derived_ok` counters) and
**RL-8** (the law gate's era leg). They touch different pin surfaces and **do not collide**:

| landing | pins that move | measured |
|---|---|---|
| **F-6 route A** — the two keys on the argot gate's own `coverage:` line | **zero** | battery `battery_exit: 0, findings []`; typed pipeline `20/20`; v3 chain exit 0; r31-post `4/4` |
| **F-6 route B** — the two keys in the projection's `coverage` block | **5 live rows** (typed-pipelines profile, expected-holds, r22-post baseline, r7 read set ×3 members) | battery exit 0 but d4-typed-labels selftest `161/163`; typed-pipeline `FAIL L1-profile`; v3 `E2E-DIGEST` refusal |
| **RL-8** — the era emitter in `tools/gates/register-law-gate.py` | **exactly one** new baseline id | battery `battery_exit: 2`, one `BASELINE-GATE-REVISED` on `r30-post` |

**The load-bearing finding for the integrator:** the residue that the claim names *cheapest*
(the counter keys) can be landed at **zero pin cost** if it is emitted by the argot gate, and at
**five-row cost** if it is emitted by the projector. That is a design decision with a measurable
price, and it is the planner's/integrator's, not a pin seat's — but the price is now known
rather than assumed. §3 states both.

**Second finding, a correction to the claim's own instrument count.** The argot gate
`tools/gates/argot-derivation-gate.py` is pinned by **nothing live**: no `expected.json`
anywhere, no `typed-pipelines.json` profile field, **not a battery-registered gate**
(`tools/check-gate-battery.py:117-132` registers it in none of `GATE_NAMES`,
`D4_GATE_NAMES`, `REGISTER_LAW_GATE_NAMES`), and **not a member of the r7 read set**
(`reports/round-34/handoff/declared-in-r7/expected.json#inputs` has 58 members; the only
`tools/gates/*` members are `costume-era-consistency-gate.py`, `d4-assembly-check-gate.py`,
`d4-typed-labels-check-gate.py`, `handoff-packet-check.py`). Measured: `grep -rl
"b5406bcdaf41…"` over `tools/` and `examples/` → only a filed round-38 fragment and filed
reports. So route A's zero-cost result is not an accident of the probe — it is the tree's
actual pin topology, and it is worth naming as a gap: **the argot leg is verified only by the
typed pipeline's `L3b-argot` leg, and its own output has no committed baseline.** A future
round that wants the F-6 counters *checked* rather than merely *printed* must add a baseline,
not just a key.

---

## 1. The pin-surface census — every live row that pins a D4 artifact or tool

Measured by scanning all tracked bytes for each digest (`os.walk`, excluding `.git`,
`.scratch`, `__pycache__`), then splitting live from filed. `filed/other` counts are in §6.

| pinned artifact | digest (baseline) | LIVE surfaces that pin it |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `aac91246cede…` | `expected-holds.json`, `packet.d4.typed.yml`, `typed-labels.d4.yml` (own `assembly.packet_sha256`), `tools/gates/expected/register-law-gate/r30-post/expected.json`, `tools/gates/typed-pipelines.json` |
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cf…` | `expected-holds.json`, `packet.d4.typed.yml`, `tools/gates/typed-pipelines.json` |
| `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384…` | `expected-holds.json` |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c8…` | `tools/gates/typed-pipelines.json` |
| `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b921…` | `packet.d4.yml`, `packet.d4.typed.yml` (both via their own `assembly.source_sha256` blocks) |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac56…` | `packet.d4.yml`, `packet.d4.typed.yml` (same mechanism) — **not** the r7 read set |
| `tools/d2-typed-labels.py` (the projector) | `2819f68769df…` | `tools/gates/typed-pipelines.json` (profile `projector_sha256`-bearing `expected`/`projection` fields + the round-28 note at `:66`), `examples/culture-d4/expected-holds.json:5,13,25,39` (`projector_sha256`), `examples/culture-d2/expected-holds.json`, `tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json` (`inputs`), and the r7 read set (A-20) |
| `tools/gates/register-law-gate.py` | `15f8b23251ca…` | `tools/gates/expected/register-law-gate/r30-post/expected.json` — **twice**: `gate_sha256` **and** `inputs["tools/gates/register-law-gate.py"]` |
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41…` | **none live** |
| `tools/assemble-culture-d4.py` | `943f487ba991…` | 8 live surfaces incl. `packet.d4.yml`'s own `assembly.assembler_sha256`, `typed-pipelines.json`, the r19-pre d4-assembly baseline, and the r7 read set (A-46) |
| `tools/assemble-d4-typed.py` | `92f5460bcc34…` | `packet.d4.typed.yml`, `typed-pipelines.json`, the r7 read set (A-47) |
| `tools/exercise-handoff-e2e.py` | `bfe1c78e479f…` | **none live** (the r7 freeze pins the baseline pair it points at, not the tool) |

**Read this table as the cascade's skeleton.** A change to the *packet* moves rows 1–6; a change
to the *projector* moves row 7; a change to the *law gate* moves row 8; a change to the *argot
gate* moves nothing.

---

## 2. The r7 handoff pair — what the D claim's landing actually moves

The r7 freeze (`reports/round-34/handoff/declared-in-r7/`) is **filed and must not be edited**;
its `--freeze` is forbidden this round. Measured membership of its 58-member `inputs` map:

- **19 D4 members**: `packet.d4.yml`, `packet.d4.typed.yml`, `typed-labels.d4.yml`,
  `expected-holds.json`, `brief.md`, `ASSEMBLY.md`, components `01-brief` … `12-provenance`
  (**12**, not 13 — `13-register-law.yml` is absent), and the four D4 tools
  (`assemble-culture-d4.py`, `assemble-d4-typed.py`, `d2-typed-labels.py`,
  `d4-assembly-check-gate.py`, `d4-typed-labels-check-gate.py`, `costume-era-consistency-gate.py`).
- **`tools/gates/typed-pipelines.json` is NOT a read-set member** — §3's profile re-pin does
  **not** cascade into the read set.
- **`13-register-law.yml` is NOT a read-set member** (r37 A01's adjudicated roster defect,
  carried as `r37-A01-readset-roster-defect` / `R36-R7-READSET-13` in
  `reports/round-37/op/defect-queue.json`). It is covered **transitively**: the packet pins it in
  its own `assembly.source_sha256`, and the read set pins the packet.
- The r7 read set pins `tools/d2-typed-labels.py` directly at A-20
  (`reports/round-34/handoff/declared-in-r7/twin.json`), so **route B moves the read set** and
  route A does not.

**Consequence for the D claim as scoped.** The D claim's `after_required` says "filed bytes
untouched except the two named tool/example artifacts" — the two artifacts are the argot gate
and the law gate. **Neither of those two is a member of the r7 read set.** Therefore, if the
round lands **route A + RL-8**, the r7 default chain stays exit 0 and no successor freeze is
owed. If the round lands **route B** (the projector), the r7 chain reddens and a successor
freeze *is* owed — measured in §3.2.

---

## 3. F-6 — two routes, measured costs

### 3.1 Route A: the keys on the argot gate's own coverage line — **zero pin movement**

Applied to `.scratch/d04-f6gate` (isolated `git archive HEAD` copy): two keys appended to the
`coverage:` print and two arguments added to the format tuple
(`tools/gates/argot-derivation-gate.py:917-921`, the producer the K01 census says does not
exist). Measured output:

```
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 \
  claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0 derived_forms=8 derived_ok=8
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0
selftest: 27/27 checks passed
```

Every pin-reading surface re-run on that copy:

| surface | command | observed |
|---|---|---|
| gate battery | `check-gate-battery.py` | `{battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`, baseline findings `[]` |
| typed pipeline | `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` |
| v3 default chain | `exercise-handoff-e2e.py --profile v3 --quiet` | `exit=0 fields=16/16 links=105/105 packet_sha256=45f57132…` |
| r31-post sweep | `replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4` |
| r26 frozen rows | `replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | `2 mismatch, 4 reproduced` — **identical to pristine**, see §5 |

**New-row draft: none required.** Route A invalidates no row. This is the honest and
non-obvious result: the forecast's F-6 element is a *key-set mismatch*, and landing it in the
gate that already computes the numbers costs nothing.

**Named gap this exposes (not repaired here).** Because no `expected.json` pins the argot
gate, route A's keys are **printed but unchecked** — the same "green over an empty domain"
class K01 §4 F-6 names. If the claim's threshold "the new coverage named (no vacuous-pass)" is
to be met, the round needs **either** route B (where the projection's coverage block *is*
pinned and diffed) **or** a new committed baseline for the argot gate. Recorded as a decision
the integrator must make explicitly; §7 lists the owed baseline.

### 3.2 Route B: the keys in the projection's coverage block — **five live rows move**

Applied to `.scratch/d04-proj` / `.scratch/d04-projonly`: the two keys added to the `coverage`
dict literal (`tools/d2-typed-labels.py:2879-2893`), then the D4 chain regenerated
(`d2-typed-labels.py --emit`, `assemble-d4-typed.py --emit <path>`).

**The chain, before → after (this seat's copy):**

| # | artifact | before (`9bccc9b`) | after (route B) |
|---|---|---|---|
| 1 | `tools/d2-typed-labels.py` | `2819f68769df…` | `0309e45e5dca…` |
| 2 | `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cf…` | `2921ba9a69bf…` |
| 3 | `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384…` | `1c012da026ed…` |
| 4 | `examples/culture-d4/packet.d4.yml` | `aac91246cede…` | `aac91246cede…` (**unchanged**) |
| 5 | `examples/culture-d4/expected-holds.json` | `e6ae9828d6c8…` | **moves** — its `projector_sha256` + `projection_sha256` are inside it |

Note the projector change also moves the **D2** projection: regenerating
`examples/culture-d2/typed-labels.d2.yml` on the patched projector gives
`e40774200215d4…`, not the pinned `a3aa452cd5ae…`. The two families share one projector, so
route B is a **two-family** landing, not a D4-local one. That is a fact about the tool's
design, reported rather than smoothed.

**Rows that move (each a NEW row; no filed row edited):**

| # | surface | what moves | measured refusal |
|---|---|---|---|
| B-1 | `tools/gates/typed-pipelines.json` (`profiles[0]`, the first-match `d4`/`round-30-qreg-records` row) | `projection.sha256` (`c23b0ab532cf` → route-B digest) and `expected.sha256` (`e6ae9828d6c8` → route-B digest); `packet.sha256`, `assembler.sha256`, `adapter.sha256` do **not** move | `FAIL L1-profile: projection: pins c23b0ab532cf, live 2921ba9a69bf (examples/culture-d4/typed-labels.d4.yml)` |
| B-2 | `examples/culture-d4/expected-holds.json` | top-level `projection_sha256` + `projector_sha256`; a new `pin_generations[]` row (the r28/r30 precedent keeps the old rows) | its own bytes move → it is itself pinned by B-1, so ordering matters (§6) |
| B-3 | `tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json` | `inputs["tools/d2-typed-labels.py"]` (`2819f687` → route-B projector digest) — the r22-post **mirror** holds the old projector, so the pin still reads `pinned`; the *gate revision* is unchanged | `d4-typed-labels-check-gate.py --selftest` → `161/163`, failures `mirror: the mirror build is byte-identical to the filed d4 projection` and `boundary compatibility: D2 projection keeps its exact baseline digest` |
| B-4 | `reports/round-34/handoff/declared-in-r7/expected.json` (A-20/A-30/A-31) | `tools/d2-typed-labels.py`, `examples/culture-d4/typed-labels.d4.yml`, `examples/culture-d4/expected-holds.json` | `E2E-DIGEST: … projector_sha256: the tree recorded 2819f68769df… but the bytes measure 0309e45e5dca…` |
| B-5 | `reports/round-34/handoff/declared-in-r7/twin.json` (same three rows) | regenerated by the successor freeze, never edited | — |

**Route B verdict: it is a full D4 cascade plus the read set.** It also breaks a *selftest*
(B-3) and the D2 family. Route A is strictly cheaper for the same two keys.

---

## 4. RL-8 — the era leg — **exactly one new row**

Applied to `.scratch/d04-law` (a marker appended) and `.scratch/d04-lawline` (an
`era_failures=%d` field added to the law gate's coverage line and its format tuple,
`tools/gates/register-law-gate.py:635-641`). Both edits change the gate's bytes, which is what
any RL-8 emitter does.

**The single row:**

| # | surface | action | measured |
|---|---|---|---|
| L-1 | `tools/gates/expected/register-law-gate/r38-post/` — a **new** baseline id | commit a new dir with `expected.json` + `freeze.txt` + `run.log` (+ the mirror inputs); the `r30-post` dir stays byte-identical | battery `{"battery_exit": 2, …}` with one finding: `BASELINE-GATE-REVISED \| expected/register-law-gate/r30-post/expected.json \| gate_sha256 15f8b23251ca2ad0... differs from the live register-law-gate.py 44d7eb1cb73b172a...: re-freeze, never compare across an unnamed revision` |

**Why exactly one, and why it must be a *new* id.** `r30-post/expected.json` pins the law gate
**twice** — `gate_sha256` (`:10`) **and** `inputs["tools/gates/register-law-gate.py"]` (`:20`) — and
carries a `stdout_sha256` (`be9e054d7b4e8dd7…`) that is the digest of its own committed
`run.log`. Adding an era counter to the gate's coverage line changes the gate bytes **and** its
stdout, so the frozen row's verdict can no longer be compared. The standard is explicit
(`corpus/knowledge/verification/gate-frozen-run-standard.md` §6 row 4: "`gate_sha256` differs →
`gate_revised` — could-not-evaluate: re-freeze under the new revision; never compare across an
unnamed one") and §3 ("A later gate revision or input edit produces a **new** baseline.
Existing baselines are never rewritten"). So `r30-post` is **not** edited; `r38-post` is added.

**What does *not* move on RL-8.** Measured on the same copy:

| surface | observed |
|---|---|
| typed pipeline (source) | `summary: 20/20 legs passed` — the law gate is not a pipeline leg |
| r31-post sweep | `REPLAY OK: 4/4` — its four rows run `d4-assembly-check-gate`, `d4-typed-labels-check-gate` ×1, `typed-pipeline-gate` ×2; the law gate is absent |
| r26 frozen rows | `2 mismatch, 4 reproduced` — **identical to pristine** |
| r7 default chain | exit 0 (the read set pins no law-gate row) |
| `register-law-gate.py --selftest` | `45/45` on the line edit — the existing controls still pass |

**The battery's own `10/10` coverage is preserved**: `r38-post` keeps `register-law-gate.py`
covered, so `coverage` stays `10/10` and `gates_uncovered` stays `[]`. The only reading that
changes is the superseded row's `pinned` → `gate_revised`, which is the standard's designed
state for a superseded baseline (`reports/round-30/validation.json` records the same reading
for older rows).

**One design note the integrator needs.** `DECLARED_KINDS` already includes `"era"`
(`tools/gates/register-law-gate.py:121`) and RGL-05 declares the rule
(`examples/culture-d4/components/13-register-law.yml:49`), but `grep -c "D4L-ERA"` over the gate
is **0** — the class is declared and never emitted. RGL-05's own component text says so
(`13-register-law.yml:57`: "The era leg (RGL-05) is specified and unimplemented"). The r38-post
baseline is the row that makes the new emitter **checked** rather than merely present; without
it, RL-8 lands in the same unverified state as F-6 route A.

---

## 5. Causality controls — what is already red at pristine HEAD

A re-pin list that attributes pre-existing reds to the landing is its own defect, so this seat
ran every frozen manifest on the **pristine** archive first (`.scratch/d04-iso`):

| manifest | pristine `9bccc9b` | after route A | after route B | after RL-8 |
|---|---|---|---|---|
| `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4` | `4/4` | `3 mismatch, 1 reproduced` | `4/4` |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | **`2 mismatch, 4 reproduced`** | `2 mismatch, 4` | `3 mismatch, 3` | `2 mismatch, 4` |
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | **`2 mismatch, 4 reproduced`** | `2 mismatch, 4` | `3 mismatch, 3` | `2 mismatch, 4` |

**The r26 post-register/gate-input manifests are already `2 mismatch` at pristine HEAD.** The
mismatching rows are ROW 2/3 (`typed-pipeline-gate.py` over `packet.d4.yml` /
`packet.d4.typed.yml`, recorded `exit 0` vs observed `exit 2`) — i.e. the **round-30 re-pin
moved the packet under these round-26 snapshots**, which the r30 record names as
"superseded" (`tools/gates/frozen/round-26/*/freeze-receipt.json`; the r31 `CONTROLS` list calls
the r18/r22 generations "superseded by later D4 landings (recorded reds stay red)"). So:

- **Route A introduces no new mismatch** (`2 mismatch` before and after — the causality control
  passes).
- **Route B adds one new mismatch** (ROW 4, the D2 packet row, flips from `reproduced` to
  `mismatch` because the shared projector moved) — a second, independent reason route B is the
  expensive route.
- **RL-8 introduces no new mismatch.**

**Reds stay red.** Per `reports/round-31/sweep/run-sweep.py`'s own control language, a
reproduced red verdict stays red; none of these rows is repaired by this round, and none is
claimed as green.

---

## 6. The row set at a glance, and the ordering

| # | surface | kind | action | route |
|---|---|---|---|---|
| 1 | `tools/gates/argot-derivation-gate.py` | tool (F-6 producer) | edit — **zero pin cost** | A |
| 2 | `tools/gates/register-law-gate.py` | tool (RL-8 emitter) | edit | RL-8 |
| 3 | `tools/gates/expected/register-law-gate/r38-post/` | **NEW** baseline id | commit `expected.json` + `freeze.txt` + `run.log` + mirror inputs; `r30-post` untouched | RL-8 |
| 4 | *(route B only)* `tools/d2-typed-labels.py` | tool (projector) | edit | B |
| 5 | *(route B only)* `examples/culture-d4/typed-labels.d4.yml` | generated | regenerate | B |
| 6 | *(route B only)* `examples/culture-d4/packet.d4.typed.yml` | generated | regenerate (**`--emit PATH` required**; bare `--emit` exits 2 and writes nothing — the r36 D04 trap) | B |
| 7 | *(route B only)* `examples/culture-d2/typed-labels.d2.yml` | generated | regenerate — the shared projector moves the D2 family too | B |
| 8 | *(route B only)* `examples/culture-d4/expected-holds.json` | pin row | new `pin_generations[]` row + advance the two scalar pointers | B |
| 9 | *(route B only)* `tools/gates/typed-pipelines.json` | pin row | **new first-match** `d4` generation (2 fields: `projection.sha256`, `expected.sha256`) | B |
| 10 | *(route B only)* `tools/gates/expected/d4-typed-labels-check-gate/r38-post/` | **NEW** baseline id | commit; the r22-post dir stays byte-identical | B |
| 11 | *(route B only)* `reports/round-34/handoff/declared-in-r7/{expected.json,twin.json}` | **FILED** | successor freeze (`declared-in-r8`) + re-point the renderer default pair `tools/exercise-handoff-e2e.py:1937-1938` **together**; **no re-freeze of declared-in-r7** | B |
| 12 | *(route B only)* `reports/round-31/sweep/frozen/r31-post/` | **FILED** | successor generation (`r38-post`) — the freeze script refuses to re-freeze over an existing generation | B |

**Ordering (load-bearing, route B only):** `4 → 5 → 6 → 7 → 8 → 9 → (re-run the typed pipeline
to confirm convergence) → 10 → 11 → 12`. Writing **9 before 8** leaves `expected.sha256` stale
because `expected-holds.json` is itself edited by 8 — the same self-referential pin trap r26
recorded (`SCORECARD.md:330`, `reports/round-26/register/repin.json`). RL-8's row 3 is
independent of the whole F-6 chain and can land in either order.

**Under route A + RL-8 the round's pin work is exactly rows 1, 2, 3 — one new baseline, zero
edits to any generated artifact, zero filed bytes, zero read-set movement.**

---

## 7. Surfaces that need **no** new row (measured, so the list is honest)

An over-broad re-pin list is its own defect. These were checked and do not move under any route:

| surface | why | evidence |
|---|---|---|
| `tools/gates/expected/register-law-gate/r30-post/` | **not** invalidated in place — superseded by `r38-post`; its mirror snapshot still grades its own packet cleanly | `register-law-gate.py <r30-post>/packet.d4.yml` → `record_ids=183 … findings=0`, exit 0 |
| `tools/gates/expected/d4-assembly-check-gate/r19-pre/` | pins 16 inputs **by mirror copy** (12 D4 components + `packet.d4.yml` + `assemble-culture-d4.py` + `assemble-d2.py` + `costume-era-consistency-gate.py`), not by live path; the mirror resolves inside the baseline so the reading stays `pinned` | battery: `pinned 20`, `coverage 10/10`, `unevaluable 0` — **before and after every route** |
| `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post}` | same mirror mechanism; already exit 1 at HEAD (pre-landing mirrors), unchanged by any route | battery readings unchanged |
| `tools/gates/expected/phonology-sanity-gate/r9-pre/`, `tools/gates/frozen/{handoff-packet-check,lexicon-coverage-audit,myth-consistency-gate,naming-collision-gate,phonology-sanity-gate,provenance-audit,round-11,round-18,round-20,round-22,round-23,round-25}` | no D4 artifact or D4 tool among their inputs | digest scan §1; battery `pinned 20` unchanged |
| `tools/gates/frozen/round-18/MANIFEST.tsv`, `round-22/d4-repin/`, `round-23/`, `round-25/` | filed historical generations, already superseded and named as such; their reds stay red | §5 pristine control; `reports/round-31/sweep/run-sweep.py` `CONTROLS` |
| `examples/culture-d4/ASSEMBLY.md` §5 pins table | **already stale at HEAD**; no machine check reads it (this seat found none — `to-verify`); its bytes do not move under route A/RL-8 | r36 D04 §4 |
| `examples/culture-d2/expected-holds.json` | moves **only** under route B (its `projector_sha256` at `:4` pins the shared projector) — not under route A or RL-8 | digest scan §1 |
| `corpus/lessons/round-30.md`, all `reports/round-1..37/**` | filed prose; append-only, never edited | hard boundary |
| `tools/check-gate-battery.py`, `tools/gates/typed-pipeline-gate.py`, `tools/exercise-handoff-e2e.py`, `tools/assemble-culture-d4.py`, `tools/assemble-d4-typed.py` | **no byte moves** under route A or RL-8 | §3.1/§4 measured; the r7 read set pins `assemble-culture-d4.py` (A-46) and `assemble-d4-typed.py` (A-47), neither of which changes |

---

## 8. Calibration and limits

- **A pin is integrity, never truth.** Every row above asserts *bytes moved*, not that the move
  was correct, not that the counter keys or the era leg are well-designed, and never clearance.
- **The digest values in §3–§4 are this seat's copies' values, not transferable.** The route-B
  packet digest is unchanged but the projection/typed-packet digests depend on the exact bytes
  landed; D01/D02/D03 each measured different values for the same row set in r36. The
  integrator re-measures on landed bytes; this seat owes the **row set** and the **ordering**.
- **`reports/round-38/run-validation.py` does not exist** at write time
  (`ls` → No such file), so claim D's declared counting command could not be run. Per F-C13-1 it
  must not be run in-tree regardless. The per-leg commands above stand in as measured evidence.
- **Route choice is not this seat's.** §3 prices both routes; §6 lists the row sets. P01/X00/R03
  and the integrator own the decision. This fragment reports the price, not a preference —
  except the one observation that route B additionally breaks a **selftest** and the **D2
  family**, which is a fact, not a preference.
- **`to-verify`:** whether any machine check reads `examples/culture-d4/ASSEMBLY.md` §5's digest
  table. This seat found none by reading the tools that reference the file; absence of evidence
  is recorded as `to-verify`, not as "unchecked".
- **The r26 pre-existing `2 mismatch`** is recorded as pre-existing, not as a defect this round
  introduces; it is not in this round's scope to repair, and repairing it would mean editing a
  filed generation.
- **In-tree state note (not this seat's write).** `git status --porcelain` shows `?? reports/round-38/`
  only; the round-38 fragments other seats land (`adj/A03-verify.md`, and whatever else lands
  concurrently) are theirs. This seat wrote **only** `reports/round-38/depth/D04-pins.md`.
  HEAD is unchanged at `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`.

## Owed

- **The route decision (§3).** Route A (argot-gate coverage line, zero pin cost, keys printed
  but unchecked) vs route B (projection coverage block, five rows + a selftest + the D2 family,
  keys pinned and diffed). Owner: integrator / X00 / R03 / P01. The row set for each is §6.
- **The `r38-post` register-law baseline (§4)** — the new `expected.json` + `freeze.txt` +
  `run.log` + mirror inputs. It is a **new** generation; `r30-post` must not be edited. Owner:
  the round's O/integration seat, after the era emitter lands.
- **A committed baseline for the argot gate (§3.1)** — if route A is chosen, the F-6 counters
  and the argot leg's own output have **no committed `expected.json`** anywhere and the gate is
  **not battery-registered** (`tools/check-gate-battery.py:117-132`). Meeting the claim's
  "no vacuous-pass" threshold therefore also owes either route B or a new argot-gate baseline
  id (which would raise `gates_registered` from 10 to 11 and change the battery's `10/10`
  coverage string — a selftest expectation at `:37,755,1069-1073`). Owner: integrator; recorded
  as a decision, not performed.
- **The successor freeze (§6 row 11) and the r31-post successor (§6 row 12)** — route B only.
  Owner: integrator (tool + filed-adjacent surfaces; this seat may not write
  `tools/exercise-handoff-e2e.py` or freeze a new baseline).
- **The `13-register-law.yml` read-set membership** — carried in the r37 defect queue
  (`R36-R7-READSET-13`, `r37-A01-readset-roster-defect`) and targeted by the O claim's renderer
  guard. The pin consequence for **this** round: under route A/RL-8 no successor freeze is owed,
  so the roster defect stays carried; under route B the successor freeze should absorb the
  member (r36 D04 §3.3's route). Owner: the O block / integrator.
- **`examples/culture-d4/ASSEMBLY.md` §5's already-stale digest table** — pre-existing, not this
  landing's, but it is the documentation surface a reader would trust. Recorded, not repaired.

## Citations

Every number above is a command output or a `file:line`, taken at
`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` with `TMPDIR=$PWD/.scratch` and
`PYTHONDONTWRITEBYTECODE=1`, unless a row says `TMPDIR=/var/tmp`.

**Baseline and digest scan**

```sh
git rev-parse HEAD                    # 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
git status --porcelain                # ?? reports/round-38/ only
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
  examples/culture-d4/packet.d4.typed.yml examples/culture-d4/expected-holds.json \
  examples/culture-d4/components/{04-lexicon.yml,13-register-law.yml} \
  tools/gates/typed-pipelines.json tools/d2-typed-labels.py \
  tools/gates/{register-law-gate.py,argot-derivation-gate.py} \
  tools/{assemble-culture-d4.py,assemble-d4-typed.py,exercise-handoff-e2e.py}
#   aac91246cede8840… packet.d4.yml            c23b0ab532cfb9d4… typed-labels.d4.yml
#   d581e0ad5384ce56… packet.d4.typed.yml      e6ae9828d6c82aa6… expected-holds.json
#   ed7093d6b92111c2… 04-lexicon.yml           c0d77181ac567c4c… 13-register-law.yml
#   76ecdfdcbf09c3c7… typed-pipelines.json    2819f68769dfc0b5… d2-typed-labels.py
#   15f8b23251ca2ad0… register-law-gate.py    b5406bcdaf41c595… argot-derivation-gate.py
#   943f487ba991d45d… assemble-culture-d4.py  92f5460bcc34ffbb… assemble-d4-typed.py
#   bfe1c78e479f7478… exercise-handoff-e2e.py
# per-digest live-vs-filed split: os.walk over the tree for each digest (excludes .git/.scratch/__pycache__)
```

**The pin census (§1)**

```sh
grep -rl "b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb" tools/ examples/
#   (no live hit — only filed reports and one round-38 fragment)
sed -n '117,132p' tools/check-gate-battery.py
#   GATE_NAMES (7) + D4_GATE_NAMES (2) + REGISTER_LAW_GATE_NAMES (1); argot gate absent
python3 -c "…r7 expected.json inputs…"   # 58 members; D4 components = 12; 13-register-law absent;
                                          # tools/gates/* members = costume-era/d4-assembly/d4-typed-labels/handoff-packet
```

**Route A (§3.1) — isolated `.scratch/d04-f6gate`, `git archive HEAD`**

```sh
# edit: append derived_forms=%d derived_ok=%d to the coverage print (argot-derivation-gate.py:917-921)
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
#   coverage: … derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0 derived_forms=8 derived_ok=8 ; exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest      # 27/27
python3 -B tools/check-gate-battery.py                          # {battery_exit: 0, pass: 7, unevaluable: 0}; findings []
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # 20/20
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet   # exit=0 fields=16/16 links=105/105 packet_sha256=45f57132…
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv   # 4/4
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv # 2 mismatch, 4 reproduced
```

**Route B (§3.2) — isolated `.scratch/d04-proj`, `.scratch/d04-projonly`**

```sh
# edit: two keys in the coverage dict literal (tools/d2-typed-labels.py:2879-2893)
python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit examples/culture-d4/typed-labels.d4.yml
python3 -B tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml
sha256sum examples/culture-d4/{typed-labels.d4.yml,packet.d4.typed.yml,packet.d4.yml}
#   2921ba9a69bfbf9c… typed-labels  1c012da026ed40fd… packet.d4.typed  aac91246cede8840… packet (unchanged)
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
#   FAIL L1-profile: projection: pins c23b0ab532cf, live 2921ba9a69bf
python3 -B tools/gates/d4-typed-labels-check-gate.py --selftest   # 161/163 — mirror + boundary compatibility
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
#   E2E-DIGEST: examples/culture-d4/expected-holds.json projector_sha256: recorded 2819f68769df… bytes measure 0309e45e5dca…
python3 -B tools/check-gate-battery.py                          # battery_exit 0 (mirror rows stay pinned)
python3 -B tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --emit examples/culture-d2/typed-labels.d2.yml
#   e40774200215d4… (pinned a3aa452cd5ae…) — the D2 family moves too
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv  # 3 mismatch, 1 reproduced
```

**RL-8 (§4) — isolated `.scratch/d04-law`, `.scratch/d04-lawline`**

```sh
# edit: append a marker (d04-law) or add era_failures=%d to the law coverage line (d04-lawline, :635-641)
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml   # exit 0
python3 -B tools/gates/register-law-gate.py --selftest                          # 45/45
python3 -B tools/check-gate-battery.py
#   {"battery_exit": 2, "pass": 7, "unevaluable": 0}
#   FINDING BASELINE-GATE-REVISED | expected/register-law-gate/r30-post/expected.json |
#     gate_sha256 15f8b23251ca2ad0... differs from the live register-law-gate.py 44d7eb1cb73b172a...
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv  # 4/4
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv # 2 mismatch, 4 reproduced
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # 20/20
grep -c "D4L-ERA" tools/gates/register-law-gate.py                               # 0
```

**Causality control (§5) — pristine `.scratch/d04-iso`**

```sh
git archive HEAD | tar -x -C .scratch/d04-iso
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv
#   REPLAY MISMATCH: 2 mismatch, 4 reproduced of 6 — the same 2 as after every route
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv  # 4/4
```

**Source lines cited:** `tools/gates/argot-derivation-gate.py:102-103,567,917-921`;
`tools/gates/register-law-gate.py:121,635-641`; `tools/d2-typed-labels.py:2879-2893`;
`tools/gates/typed-pipeline-gate.py:300-345,346-364,520-560`;
`tools/check-gate-battery.py:37,117-132,529-547,629-641,755,1069-1073`;
`tools/exercise-handoff-e2e.py:157-170,1937-1938`;
`examples/culture-d4/components/13-register-law.yml:49,57`;
`examples/culture-d4/expected-holds.json:3-6,11-13,23-26`;
`tools/gates/expected/register-law-gate/r30-post/expected.json:10,20` and its `inputs` map;
`reports/round-34/handoff/declared-in-r7/expected.json:158,172,176`;
`reports/round-34/handoff/declared-in-r7/twin.json` rows `A-20,A-31,A-46,A-47`;
`reports/round-37/op/defect-queue.json` rows `R36-R7-READSET-13`,`r37-A01-readset-roster-defect`;
`corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (append-only, "ids are never
reused"), §6 rows 1–4 (tamper/gate-revision semantics);
`reports/round-26/register/repin.json`; `reports/round-30/fixes/qreg-dangles.md`;
`SCORECARD.md:330`; `reports/round-36/depth/D04-repin.md` §2.2/§3.4/§5;
`reports/round-36/scout/K01-register-scout.md` §3/§4.

Peer fragments read, not absorbed: `reports/round-36/depth/D04-repin.md` (the row set this
fragment extends), `reports/round-36/scout/K01-register-scout.md` (the F-6/RL-8 residue),
`reports/round-38/adj/A03-verify.md` (baseline digests, F-6/RL-8 confirmation),
`reports/round-38/claims.json`, `reports/round-38/targets.json`.
