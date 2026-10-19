- Seat: X00 | connector (claim cross) | collision matrix + integration order; the pins cascade for the D claim | date 2026-10-19 | baseline 9bccc9b

# X00 — the collision matrix, the integration order, and the D pins cascade

**Mission (binding, `reports/round-38/targets.json` seat `X00`):** "Collision matrix + integration
order; the pins cascade for the D claim." Out path: this file only.

**Write scope.** This file only. No tool, gate, packet, component, fixture, pin, baseline or filed
round-1..37 byte written. Every mutation below was made inside a `git archive HEAD` copy under
`.scratch/x00/` (gitignored) and never in-tree. No `reports/round-*/run-validation.py` was executed
in-tree or in any copy (F-C13-1); no `--freeze` was issued against
`reports/round-34/handoff/declared-in-r7`. No commit, no push, no install, no network.

**Stamp.** `date -u +%FT%TZ` → **2026-10-19T11:18:44Z**; `git rev-parse HEAD` →
`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git status --porcelain` → `?? reports/round-38/` only.
`python3 -V` → Python 3.14.7. Every command ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, never clearance. This
fragment certifies neither claim; it reports what collides, in what order the drafts must land, and
which pins move — nothing here is round acceptance.

---

## 0. Verdict in one line

**Claim D and claim O share no moving artifact this round, and the round's real collision is
*inside* D** — two candidate hosts for the RL-8 era leg with different pin prices, plus a third
artifact hidden inside one of P01's own fixes. Order: **D's tool bytes first, then O's renderer
guard, then any new baseline row**; the O guard must be **D4-scoped and record-only** or it reds the
r7 default chain and breaks the renderer's own selftest.

| claim | artifacts it moves (this round) | filed pins moved | r7 packet `45f57132…` |
|---|---|---|---|
| **D** — argot host (P01/D03/D08) | `tools/gates/argot-derivation-gate.py` | **none** | unchanged, exit 0 |
| **D** — law host (D02 §2.1) | `tools/gates/register-law-gate.py` + **new** `expected/register-law-gate/r38-post/` | battery reading `pinned → gate_revised` until the new id lands | unchanged, exit 0 |
| **O** — guard (record-only) | `tools/exercise-handoff-e2e.py` | **none** | unchanged, exit 0 |
| **D route B** (projection coverage block) | `tools/d2-typed-labels.py` + 4 generated + 3 pin rows | **full D4 cascade + r7 read set** | **red** (`E2E-DIGEST`) — forbidden this round |

---

## 1. Method, and the one measurement that answers the mission question

Every row below is a command output taken by this seat on an isolated `git archive HEAD` copy of
`9bccc9b`. Baseline controls first, so a later red is attributable:

```
$ python3 -B tools/check-gate-battery.py
  "summary": { "battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0 }
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19   exit 0
```

**The mission question — "does the guard's named-row output change any D leg, or vice versa?" —
answers no, and it answers no by construction, not by luck.** The v3 renderer never invokes either
register gate:

```
$ grep -n "argot\|register-law\|register_law" tools/exercise-handoff-e2e.py
(no output)
```

The D legs run `argot-derivation-gate.py` / `register-law-gate.py` / `typed-pipeline-gate.py` over
`examples/culture-d4/packet.d4.yml`. The O guard reads `baseline["inputs"]` and `V3_READ_SET`. The two
sets do not intersect. This reproduces R03 §2.3 independently and is the matrix's foundation.

### 1.1 The membership facts the matrix rests on (measured, not read)

```
$ python3 -c "<r7 expected.json inputs census>"
inputs: 58            tools/ members: 12
  tools/assemble-culture-d3.py  tools/assemble-culture-d4.py  tools/assemble-d2.py
  tools/assemble-d4-typed.py    tools/check-evidence-coupling.py  tools/d2-typed-labels.py
  tools/gates/costume-era-consistency-gate.py  tools/gates/d4-assembly-check-gate.py
  tools/gates/d4-typed-labels-check-gate.py    tools/gates/handoff-packet-check.py
  tools/harness/packet_links.py                tools/harness/packet_uncertainty.py

PIN   examples/culture-d4/typed-labels.d4.yml      c23b0ab532cfb9d4
PIN   examples/culture-d4/expected-holds.json      e6ae9828d6c82aa6
PIN   tools/d2-typed-labels.py                     2819f68769dfc0b5
FREE  examples/culture-d4/components/13-register-law.yml   (absent)
```

`argot-derivation-gate.py`, `register-law-gate.py`, `typed-pipeline-gate.py` and
`exercise-handoff-e2e.py` are **all absent** from the 58-member read set. That single fact is why
D's tool-only routes and O's guard are pin-neutral, and why route B is not.

---

## 2. The collision matrix

### 2.1 Artifact-by-artifact (the D block × the O block)

| artifact | D touches it? | O touches it? | collision |
|---|---|---|---|
| `tools/gates/argot-derivation-gate.py` (`b5406bcd…`) | **yes** (argot host) | no | none |
| `tools/gates/register-law-gate.py` (`15f8b232…`) | **yes** (law host) | no | none |
| `tools/gates/typed-pipeline-gate.py` (`b749ad07…`) | **only** under P01 §6.2 fix-2 | no | see §5 finding **X00-1** |
| `tools/exercise-handoff-e2e.py` (`bfe1c78e…`) | no | **yes** (the guard) | none |
| `examples/culture-d4/typed-labels.d4.yml` (`c23b0ab532…`) | only under route B | no (this round) | none this round |
| `examples/culture-d4/expected-holds.json` (`e6ae9828…`) | only under route B | no | none this round |
| `reports/round-34/handoff/declared-in-r7/**` | no | no | **zero freeze bytes** |
| `tools/gates/expected/register-law-gate/r30-post/expected.json` | only under the law host | no | none |
| `tools/gates/expected/…` (new `r38-post`) | law host owes it | no | none |

**Conclusion.** On the r7 row the two claims are mechanically independent: the D legs are invisible
to the renderer, and the guard's output reaches no D leg. R03 §2.3 and §0 reach the same verdict from
an independent sample; this seat confirms it by running both edits and reading the renderer's
`grep` census.

### 2.2 The genuine collision is inside D — two hosts, one artifact each

| host | source of the design | measured effect | pins owed |
|---|---|---|---|
| **argot gate** (both legs) | P01 §3.4 fenced draft; D03 §3 verified it verbatim; D08 §3 recommends it | `coverage: … derived_forms=8 derived_ok=8`; `--selftest 27/27`; **battery exit 0**; typed pipeline `20/20`; v3 exit 0 packet `45f57132…` | **zero** |
| **law gate** (era leg) | D02 §2.1 (deliberate deviation from `rules.md:29`); D03 §4 built it too | law coverage gains `era_checked=0 era_failures=0`; **battery exit 2**, two `BASELINE-GATE-REVISED` findings on `r30-post`; v3 exit 0 packet `45f57132…` | **one new baseline id** (`r38-post`) + its mirrored inputs |

Reproduced first-hand (isolated copies `.scratch/x00/{argot,law}`; the argot patch adds the two F-6
keys to the coverage line, the law patch adds the era counters):

```
--- ARGOT HOST ---
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8
  claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0 derived_forms=8 derived_ok=8
selftest: 27/27 checks passed
battery: {"battery_exit": 0, "fail": 0, "pass": 7}
handoff-v3: exit=0 … packet_sha256=45f57132…            typed-pipeline: summary: 20/20 legs passed

--- LAW HOST ---
coverage: … dangling=0 era_checked=0 era_failures=0 findings=0
battery:  "id": "BASELINE-GATE-REVISED"  (×2)   {"battery_exit": 2, "fail": 0, "pass": 7}
handoff-v3: exit=0 … packet_sha256=45f57132…
```

**The price is one new baseline dir, and it is a *third* artifact.** Claim D's `after_required`
(`claims.json:16`) says "filed bytes untouched except the **two named** tool/example artifacts". The
law host needs a third surface — a new `tools/gates/expected/register-law-gate/r38-post/` — which is
not a filed round-1..37 byte (it is a *new* id, so the append-only rule is honoured), but it is
nonetheless a surface the claim did not name. **The argot host keeps the round inside the two.**

### 2.3 The frozen-manifest census — both D routes are replay-neutral

A pin census that only checks the battery would miss the frozen manifests. Measured over every
`MANIFEST.tsv` under `tools/gates/frozen/` and `reports/round-31/sweep/frozen/`:

| manifest | pristine `9bccc9b` | after argot host | after law host |
|---|---|---|---|
| `round-11` | `1 cne, 10 reproduced` | same | same |
| `round-18/repin-d2` | `1 cne, 10 reproduced` | same | same |
| `round-20/repin-d2` | `1 cne, 10 reproduced` | same | same |
| `round-22/d4-repin` | `1 cne, 2 mismatch, 0 reproduced` | same | same |
| `round-23/repin-d2` | `1 cne, 10 reproduced` | same | same |
| `round-25/gate-input` | `6 cne, 0 reproduced` | same | same |
| `round-26/gate-input` | **`2 mismatch, 4 reproduced`** | **same** | **same** |
| `round-26/post-register` | **`2 mismatch, 4 reproduced`** | **same** | **same** |
| `r31-post` | `4/4 reproduced` | `4/4` | `4/4` |

**Both D routes introduce no new mismatch** — the r26 `2 mismatch` is pre-existing at pristine HEAD
(the r30 re-pin moved the packet under those round-26 snapshots; D04 §5 and the r31 `CONTROLS` list
record the same). The causality control passes for both hosts. **Neither `argot-derivation-gate.py`
nor `register-law-gate.py` appears as a row gate in any frozen manifest** (`grep -rl` over
`tools/gates/frozen/` finds them only inside mirrored *input* copies of the packet, never as the
`gate` column). So neither host owes a frozen-manifest re-freeze.

---

## 3. Integration order

The order is load-bearing in three places, and each is a measurement, not a preference.

### 3.1 The sequence

| # | step | owner | why here |
|---|---|---|---|
| 1 | apply D's tool bytes (argot host, or law host + `r38-post`) | integrator | nothing downstream reads them; the argot gate is not read-set, not battery-registered |
| 2 | apply D's selftest controls | integrator | the controls must exist before the new count is pinned (P01 R-2) |
| 3 | apply O's renderer guard (D4-scoped, record-only) | integrator | the guard reads only `V3_READ_SET` and the packet manifest; it consumes no D output |
| 4 | *(law host only)* file `tools/gates/expected/register-law-gate/r38-post/` | integrator | the new baseline must pin the **post-change** gate bytes; a mid-wave freeze is stale on landing (`reports/round-27/pinsweep/repin.py`) |
| 5 | re-run the D legs + battery + v3 chain | integrator | the claim's counting commands and the no-harm proof |
| 6 | *(deferred, next round)* the O fix route: read-set add + successor baseline | integrator | **must not** happen this round — measured red in §3.2 |

**D before O is not a hard dependency** (the two are disjoint), but it is the safe order: if the
integrator takes the law host, step 4 must follow step 1 in the same landing or the battery stays at
exit 2 between them.

### 3.2 The O fix route must be deferred — measured red

Both insertion points for the 13th read-set member were tried, and both red the default chain:

```
# splice into D4_COMPONENTS (position 13)
handoff-v3: exit=1 … packet_sha256=(not assembled)
handoff-v3: E2E-DIGEST: the assembled packet does not match the frozen packet digest

# append at the tail of V3_READ_SET (position 59)
handoff-v3: exit=1 … packet_sha256=(not assembled)
handoff-v3: E2E-DIGEST: the assembled packet does not match the frozen packet digest
```

The assembled packet embeds the read-set count (`exercise-handoff-e2e.py:2825`) and the component
digests, so a read-set edit moves the packet bytes and the filed r7 row (which pins `45f57132…`)
refuses. This reproduces O04 §2, R02 Finding 4 and R03 §6 from a third sample. The fix route is a
**paired move** — read-set add **plus** a successor baseline with the two default constants
re-pointed — and claim O's non-goal ("no re-freeze this round", `claims.json:26`) defers it. **Zero
freeze bytes move in round 38.**

### 3.3 The guard's placement is constrained by the chain and by the selftest

Three variants, each in its own isolated copy, patched only at `exercise-handoff-e2e.py:3823`
beside the existing `dropped` block:

| variant | r7 default chain | r7 `--selftest` | names `13-register-law.yml`? | `--freeze` reachable? |
|---|---|---|---|---|
| **record-only, D4-scoped** (recommended) | **exit 0**, packet `45f57132…` | **exit 0** | **yes** (non-quiet channel) | **yes** — `no tracked value changed`, exit 0 |
| raising, D4-scoped | **exit 1** `E2E-READSET` | **AssertionError** on the positive run | yes (as a failure) | blocked |
| global (all trees) | **exit 1**, 7 named rows | — | yes + 6 D2 false reds | — |

```
# record-only guard, default chain
handoff-v3: exit=0 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19

# record-only guard, named-row channel
FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component manifest but not in the live read set

# record-only guard, --freeze still reachable
read set: 58 files; component digests 26/26; d4 pins 8/8
no tracked value changed since the previous freeze
froze .scratch-x00-refreeze: packet sha256 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19   exit=0

# raising guard, selftest
AssertionError: [('manifest-roster', '…13-register-law.yml: not in the live read set'),
                 ('verdict', '1 manifest member(s) not in the live read set: …')]
```

So the claim's wording "refuses **or** names" (`claims.json:21`) is satisfiable only by **naming**.
This confirms R02 Finding 3 and R03 §5 independently, and adds the `--freeze`-reachability control
that neither seat ran: a refusing guard would block the very remedy (the successor freeze) the claim
defers.

---

## 4. The D pins cascade

### 4.1 Argot host (recommended) — the re-pin list is **empty**

```
tools/gates/argot-derivation-gate.py   b5406bcdaf41c595…   (edited; pinned by NOTHING live)
  battery: exit 0, findings []          v3 chain: exit 0, packet 45f57132… (unmoved)
  typed pipeline: 20/20                 frozen manifests: unchanged (§2.3)
```

The argot gate's digest appears **only in filed prose** — `grep -rl "b5406bcdaf41c595" tools/ examples/`
returns nothing; the hits are all under `reports/round-*` (filed narrative). It is not a read-set
member, not a `typed-pipelines.json` field, and not in `check-gate-battery.py`'s three name tuples
(`GATE_NAMES`, `D4_GATE_NAMES`, `REGISTER_LAW_GATE_NAMES`). **Zero rows move.** Claim D's
`after_required` clause "pins updated as new rows" is therefore met **vacuously**, and P01 §6.4 says
to report it as such rather than tick it — this seat confirms the price is genuinely zero, not
under-measured.

### 4.2 Law host — exactly **one** new row

```
tools/gates/expected/register-law-gate/r30-post/expected.json
  gate_sha256 15f8b23251ca2ad0…   stdout_sha256 be9e054d7b4e8dd7…   expected {exit 0, class clean, findings []}
  live pins on 15f8b23251ca2ad0: exactly this one file (grep -rl over tools/ examples/)
  frozen manifests: register-law-gate is absent from every tools/gates/frozen/** MANIFEST
```

So the cascade is **one** new generation dir (`r38-post/`: `expected.json` + `freeze.txt` + `run.log`
+ mirrored inputs) with the revised gate sha and a recomputed `stdout_sha256`; the `r30-post` dir is
**not** edited (append-only, `gate-frozen-run-standard.md` §3). The battery's `10/10` coverage is
preserved because `register-law-gate.py` stays covered by the new id; the only reading that changes
is the superseded row's `pinned → gate_revised`, which is the standard's designed state.

### 4.3 Route B (projection coverage block) — the cascade the claim forbids

Not re-measured here beyond membership: `tools/d2-typed-labels.py` **is** a read-set member
(`expected.json:176`, `2819f687…`) and `typed-labels.d4.yml` (`c23b0ab532…`) and
`expected-holds.json` (`e6ae9828…`) are too. Editing the projector moves all three, reds the r7 chain
with `E2E-DIGEST`, and breaks the pinned selftest control at `tools/d2-typed-labels.py:3114-3115`.
D04 §3.2, R01 §3, R03 §4 and P01 §4.2 measured the full cascade; this seat confirms the membership
half that makes it unavoidable. **Route B is unavailable this round.**

### 4.4 The `head2` / argot-registration items that are *not* in the cascade

Two surfaces a reader might expect on the list, and neither moves: `examples/culture-d4/ASSEMBLY.md`
§5's digest table (already stale at HEAD, no machine check reads it — `to-verify`, inherited from
D04 §7) and `tools/gates/frozen/**` (no `register-law` entry exists — `grep -rl register-law
tools/gates/frozen/` → no match). Recorded so the cascade is not over-broad.

---

## 5. Named findings

**X00-1 (blocking for one of P01's own fixes) — the `D4L-ARGOT-ERA` id choice is a pin decision, not
a style decision.** P01 §6.2 prices two fixes for the era finding's invisibility to the typed
pipeline. **Fix-1** (emit `D4L-ARGOT-ERA`, name `D4L-ERA`/`RGL-05` in the message) touches **no**
pinned surface. **Fix-2** (keep the id and widen the filter at `typed-pipeline-gate.py:531`) edits
`tools/gates/typed-pipeline-gate.py` (`b749ad07…`), which **is** a row gate in seven filed frozen
manifests. Measured in an isolated copy with one comment byte appended:

```
manifest                  pristine                        pipeline edited
round-26/gate-input       2 mismatch, 4 reproduced        6 could-not-evaluate, 0 reproduced
round-26/post-register    2 mismatch, 4 reproduced        6 could-not-evaluate, 0 reproduced
r31-post                  4/4 reproduced                  2 could-not-evaluate, 2 reproduced
```

Every `typed-pipeline-gate.py` row becomes `could-not-evaluate reason=gate_digest_mismatch`. **Fix-2
is therefore a third artifact with a seven-manifest blast radius, and it contradicts any "zero pin
cost" reading of the D landing.** The matrix recommends **fix-1**. Owner: integrator; the decision
must be recorded, because r26 filed `D4L-ERA` as the id and a reader grepping for it will otherwise
find nothing (P01 §6.2's own note).

**X00-2 (informational, reproduced) — the "only the r7 row names" expectation is false, and the
rendered channel is a trap.** X02 §4a and A02 §F-A02-3 report a second filed row (r6) with the same
manifest/read-set asymmetry. This seat reproduced the general class from the rendered side:

```
filed row                                        rendered packet.md declares   inputs D4 components
round-22/handoff/declared-in                      25 digests (…, 12 D4)         12
round-22/handoff/declared-in-r2                   25 digests (…, 12 D4)         12
round-26/handoff/declared-in-r5                   25 digests (…, 12 D4)         12
round-30/handoff/declared-in-r6                   **26 digests (9 D2, 4 D3, 13 D4)**   12
round-34/handoff/declared-in-r7                   **26 digests (9 D2, 4 D3, 13 D4)**   12
```

Both r6 and r7 declare 13 D4 component digests in their own rendered packet text while carrying 12 in
`inputs`. And the rendered `packet.md`'s **markdown manifest table carries only 12 D4 component rows
for both** (`13-register-law.yml` absent from every `A-NN` row) — so a guard written against the
rendered table is **vacuous on r6 and r7 alike** (R03-C1, confirmed here from the rendered side).
The guard must read the source packet's `assembly.source_sha256` (13 members) against `V3_READ_SET`
(58, 12 D4 components). O08's expectation should be corrected to **"r6 and r7 name; r2/r5/`declared-in`
stay green"**; the existing one-directional guard already reds r2/r5/r6 for the *superseded-row*
class (measured: `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`; r7 exit 0).

**X00-3 (informational) — the r26 frozen reds are pre-existing, so they are not a landing
attribution hazard.** At pristine HEAD, `round-26/gate-input` and `round-26/post-register` are already
`2 mismatch, 4 reproduced`; `round-22/d4-repin` is `1 cne, 2 mismatch`; `round-25/gate-input` is
`6 cne`. Every D route leaves those readings identical (§2.3). A landing record that reports them as
new reds would mis-attribute them; one that reports them as repaired would claim work not done.
**Reds stay red.**

---

## Owed

- **The host decision (D).** Argot host (zero pins, law rule in the derivation gate) vs law host
  (semantically direct, one new baseline row). This seat prices both; it does not choose. Owner:
  integrator, recorded against §2.2 and §4.
- **The era-finding id decision (X00-1).** Fix-1 (pin-neutral) vs fix-2 (seven filed manifests →
  `could-not-evaluate`). Owner: integrator, before the D bytes land.
- **`reports/round-38/run-validation.py`** does not exist (`ls` → No such file or directory), so
  claim D's third declared counting command and both claims' threshold command are `to-verify`
  regardless of what lands. Per F-C13-1 it must not be run in-tree.
- **The O guard draft.** `reports/round-38/op/O01-guard-design.md` was absent at this seat's read
  (`find reports/round-38 -type f` shows `op/` holding only `O04`, `O05`, `O07`). R03-C1's blocking
  question — does O01 parse the rendered `packet.md` or the source packet? — **cannot be verified
  against the actual draft** from here. If O01 reads the rendered table, the guard is vacuous on both
  r6 and r7 (§X00-2). This is the matrix's load-bearing owed input.
- **O08's threshold correction** ("only r7 names" → "r6 and r7 name; r2/r5 green"), owner
  integrator, per X00-2 / X02 §4a / A02 §F-A02-3.
- **The r7 filed row's digest integrity** was re-verified by this seat and is recorded in
  `## Citations`; no filed byte moved at any point in this fragment.

## Citations

**Baseline and digests (measured 2026-10-19T11:18Z, lane root, `TMPDIR=$PWD/.scratch`):**

```
9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26                        git rev-parse HEAD
?? reports/round-38/                                            git status --porcelain
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
```

**Commands run (all in isolated `git archive HEAD` copies under `.scratch/x00/{base,argot,law,pipe,guardrec,guardraise,readset,readset2}`):**

```
# baseline controls
python3 -B tools/check-gate-battery.py                                       # exit 0, 7 pass, unevaluable 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                # exit 0, packet 45f57132…
# the disjointness fact
grep -n "argot\|register-law\|register_law" tools/exercise-handoff-e2e.py    # no output
grep -rl "b5406bcdaf41c595" tools/ examples/                                 # no live hit
grep -rl "15f8b23251ca2ad0" tools/ examples/                                 # 1 hit: expected/register-law-gate/r30-post/expected.json
# the two D hosts
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # derived_forms=8 derived_ok=8, exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest                          # 27/27
python3 -B tools/check-gate-battery.py                                              # argot host: exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml       # law host: era counters, exit 0
python3 -B tools/check-gate-battery.py                                              # law host: exit 2, BASELINE-GATE-REVISED ×2
# frozen-manifest census (pristine / argot / law / pipeline-edited)
python3 -B tools/replay-frozen.py <each MANIFEST.tsv>                        # table in §2.3 and §X00-1
# the O guard variants
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                # record-only: exit 0, 45f57132…
python3 -B tools/exercise-handoff-e2e.py --profile v3                        # names 13-register-law.yml
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest             # record-only: exit 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch-x00-refreeze  # reachable, exit 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                # raising: exit 1 E2E-READSET
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest             # raising: AssertionError
# the O fix route (deferred)
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                # splice: exit 1 E2E-DIGEST
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                # tail append: exit 1 E2E-DIGEST
# the filed-row class
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline <row>/expected.json --quiet  # r2/r5/r6 exit 1 E2E-READSET; r7 exit 0
```

**Source lines cited:** `tools/exercise-handoff-e2e.py:157-170` (`D4_COMPONENTS`, 12 members);
`:1937-1938` (the r7 default pair); `:1939-1963` (`V3_READ_SET`, 58 members); `:2045-2056`
(`v3_mine_d4`, mines 13); `:2208-2222` (`v3_verify_component_digests`); `:2825` (the embedded
read-set count); `:3114-3115` (the pinned D2 baseline digest control);
`:3480-3505` (`V3Assembly`); `:3823-3838` (the existing one-directional roster guard);
`:4165-4199` (the selftest fixture + positive assertion);
`tools/gates/argot-derivation-gate.py:915-921` (the coverage print);
`tools/gates/register-law-gate.py:635-643` (the law coverage print); `:121` (`DECLARED_KINDS`);
`tools/gates/typed-pipeline-gate.py:515-541` (the `D4L-ARGOT-` filter), `:1471` (the coverage
presence test); `tools/check-gate-battery.py:117-132` (the three name tuples);
`tools/gates/expected/register-law-gate/r30-post/expected.json:10,20` (`gate_sha256` ×2);
`tools/gates/typed-pipelines.json` (`profiles[0]`, generation `round-30-qreg-records`);
`examples/culture-d4/expected-holds.json` (`projector_sha256`, `pin_generations`);
`examples/culture-d4/packet.d4.yml:2888` (the 13th component's manifest pin);
`reports/round-34/handoff/declared-in-r7/packet.md:72-83` (the 12 D4 `A-NN` rows), `:279` (the
"9 D2, 4 D3, 13 D4" line); `reports/round-30/handoff/declared-in-r6/packet.md:279` (the same line).

**Peer fragments read, not absorbed:** `reports/round-38/claims.json` (claims D/O, thresholds,
non-goals); `targets.json` (seat X00, O08's expectation, `shared_rules`); `plan/P01-d-plan.md`
(§3.4 draft, §4.2 hosts, §6.2 the id choice, §6.4 the vacuous pin clause); `depth/D02-rl8-design.md`
(§2.1 the law host, §6 the pin cascade); `depth/D03-isolated.md` (§3 the argot host verified, §4 the
law host priced); `depth/D04-pins.md` (§1 the pin census, §3 the two F-6 routes, §5 causality);
`depth/D08-gap-fill.md` (§3/§5 the host trade); `op/O04-fix-route.md` (§2 the paired move, §5 the
repin row); `op/O05-verify-route.md` (§2 D-1, §5 the filed r34/r35 literal assertions);
`review/R02-o-review.md` (Findings 2-6, the 7 false reds); `review/R03-cross-review.md` (§2.3 the
disjointness, §3 C1 the rendered-channel trap, §5 C2 the channel); `cross/X02-honesty.md` (§4a/§4b
the r6 generalization); `adj/A01-scope.md` (§3a-§3d blast radius); `adj/A02-receipt.md` (§F-A02-3);
`adj/A03-verify.md` (independent baseline reproduction); `scout/K01-residue.md`; `scribe/S02-telemetry-draft.md`.
