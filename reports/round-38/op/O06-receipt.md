- Seat: O06 | executor | claim O | date 2026-10-19 | baseline 9bccc9b

# O06 — operability receipt: claim O before→after, the guard's measured behavior, and the channel the naming actually lands on

**Assignment** (`reports/round-38/targets.json`, seat `O06`): *"Operability receipt draft."* Out path
`reports/round-38/op/O06-receipt.md`. Binding `shared_rules` (`targets.json:3-9`): write only this
out path under `reports/round-38/`; never edit filed bytes (`reports/round-1..37/**`,
`corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`) — tool/example changes are DRAFTED
as fenced blocks for the integrator; no git commits/pushes/installs/network; **ABSOLUTE** never run
any `reports/round-*/run-validation.py` in-tree (F-C13-1), isolated `git archive` copies only, and
**no re-freeze of `reports/round-34/handoff/declared-in-r7`**; every claim cites file:line or command
output, unknowns are `to-verify`, never fabricate.

**Status: DRAFT receipt.** This seat landed nothing: no renderer byte, no packet byte, no pin, no
filed byte. Every number below is a first-hand measurement taken by this seat at baseline
`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` in the window `2026-10-19T11:14:27Z`–`11:2x Z` (§1).
The three guard variants in §3 are **this seat's own prototype drafts**, built in isolated
`git archive` copies under `.scratch/o06/` — they are not O01's design and must not be read as one.
No in-tree `run-validation.py` ran; no `--freeze` was issued against the r7 pair.

**Why this receipt carries measurements its mission did not ask for.** The O block's design and
verification seats — `O01` (guard design), `O02` (isolated verify), `O03` (independent verify),
`O08` (regression sweep) — are **absent from the landed set** (§6). The round's only landed O
executor evidence is `O04` (fix route) and `O05` (route verify), plus this receipt. So the guard's
*behavior* is owed by four missing seats, and §3 supplies the measured controls in their place,
attributed to this seat and marked as prototypes.

---

## 0. Headline — the claim's own counting command cannot observe the guard's naming

Claim O (`reports/round-38/claims.json:19-24`) asks for *"a renderer guard (v3 manifest-vs-read-set
completeness check, selftest-controlled) that **refuses or names** when a frozen baseline's read set
and the packet's own component manifest disagree"*. Its thresholds are *"selftest green with the new
controls; r7 packet sha unchanged 45f57132…"* and its first counting command is
`python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`.

Measured, in an isolated copy with a D4-scoped guard inserted at `tools/exercise-handoff-e2e.py:3821`
(§3):

| guard shape | r7 default chain | r7 packet sha | name visible to `--quiet`? | name visible to verbose stdout / `--json`? | `--selftest` |
|---|---|---|---|---|---|
| **record-only** (names, never raises) | **exit 0** | `45f57132…` unchanged | **no — 0 hits** | **yes** (`FAIL manifest-roster: …13-register-law.yml…`; 1 row in `checks[]`) | **exit 0, 43 controls** |
| **raising** (`raise Failed("E2E-READSET", …)`) | exit 1 `E2E-READSET` | `(not assembled)` | n/a | yes | **exit 1 — the positive run fails** |

The claim's wording is satisfiable only by the **record-only** shape (R02 Finding 3; independently
reproduced here), and under that shape **the claim's own counting command (`--quiet`) prints zero
naming hits**. The naming survives only on the verbose stdout line and in the `--json` receipt
document (`checks[]`, one row with `"ok": false`). A verifier who runs the claim's declared command
and greps for the guard's output will read "guard absent". That is the single load-bearing
operability finding of this receipt, and it is a **channel** defect in the claim's acceptance shape,
not in the guard.

Second measured finding, and it changes the expectation: the guard is a **live-tree** check, not a
per-row check. Under a D4-scoped guard, **every filed v3 row replay emits the same named row**
(§4.3) — r2, r5, r6 and r7 all name `13-register-law.yml`, because the mismatch is a property of the
live `D4_COMPONENTS` tuple (12) against the live D4 source manifest (13), independent of which
baseline is loaded. The correct reading of the acceptance expectation is therefore **"the guard names
on every row; r7 is the only row whose exit stays 0"** — not *"only the r7 row names"*
(`targets.json` O08; falsified independently by X02 §4a and A02 F-A02-3).

---

## 1. Measurement window and state pins

| pin | value | command |
|---|---|---|
| lane root | `/home/vgpnk/Projects/shokunin/kotodama-shokunin` | — |
| baseline | `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` | `git rev-parse HEAD` |
| working tree | clean except this round's own directory | `git status --porcelain` → only `?? reports/round-38/` |
| stamp | `2026-10-19T11:14:27Z` | `date -u +%FT%TZ` |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` | before every scratch-writing command |
| isolated copies | `.scratch/o06/base` (`git archive HEAD`), `g-rec`, `g-raise`, `g-sync` | §3 |

### 1.1 Digests — the bytes every reading below binds to

```
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
```

`45f57132…` is exactly the digest `claims.json:24` names as claim O's acceptance threshold; it is
**unchanged**, and this seat issued no freeze against the r7 pair.

---

## 2. Before — the defect and the guard's absence, both measured

### 2.1 The roster asymmetry, at the instrument level

```
$ python3 - <<'PY'   # ast over tools/exercise-handoff-e2e.py
D4_COMPONENTS len: 12          # :157-170
V3_READ_SET len: 58            # :1939-1965
PY
$ python3 -c 'runpy …; v3_mine_d4(".")'    # isolated copy
v3_mine_d4 components                       : 13
13-register-law in mined components         : True
mined-but-not-in-read-set                   : ['examples/culture-d4/components/13-register-law.yml']
V3Assembly(".").digests len                 : 58
component_checked/matched                   : 26 26
d4_pins_checked/matched                     : 8 8
```

So the mismatch is **D4 source-manifest (13, mined by `v3_mine_d4`, `:2045-2056`) vs the live read
set (58 members, of which 12 are D4 components)**. The 13th component *is* measured transitively
(`v3_verify_component_digests`, `:2208-2222`, 26/26 matched), which is why the defect is a
roster/completeness defect and not an integrity bypass — the r37 adjudication's reading
(`reports/round-37/adj/A01-freeze-adjudication.md:5,26-35`), reproduced here.

### 2.2 The guard class does not exist

```
$ grep -rn "manifest-roster\|manifest-vs-readset\|manifest_vs_readset" tools/ examples/   # exit 1, no match
```

The only roster check present is the **one-directional** one at `:3823-3838`
(`dropped = baseline["inputs"] ∖ assembly.digests` → `E2E-READSET`), whose direction is
*frozen-baseline member ∉ live read set*. The r7 class is the **opposite** direction and is invisible
to it. So claim O's "land a renderer guard" is a new *direction* at an existing site, confirmed
independently by A01 §3d and R02 Finding 1.

Two further presence checks exist in the **manifest→readset** direction (`:1346`, `:3654`:
"manifest row {artifact_id} names {path}, which is not in the read set"). Both walk the *rendered*
manifest's rows, so neither can see a member the rendered manifest omits (§2.3).

### 2.3 The rendered manifest is read-set-derived — the trap R03-C1 names, reproduced

```
source examples/culture-d4/packet.d4.yml (assembly.source_sha256), component digests : 13
rendered reports/round-34/handoff/declared-in-r7/packet.md, markdown table rows A-NN  : 58
  of which examples/culture-d4/components/ rows                                       : 12
  13-register-law present                                                             : False
  12-provenance   present                                                             : True
```

And it is uniform across the filed set — every filed row's rendered `packet.md` carries **58 rows /
12 D4 rows / no `13-register-law`**, while the *source* packet carries 13:

| filed row | rendered `packet.md` rows | rendered D4 rows | `has13` | source-manifest D4 (mined) |
|---|---:|---:|---|---:|
| `reports/round-22/handoff/declared-in` | 58 | 12 | False | 13 |
| `reports/round-22/handoff/declared-in-r2` | 58 | 12 | False | 13 |
| `reports/round-26/handoff/declared-in-r5` | 58 | 12 | False | 13 |
| `reports/round-30/handoff/declared-in-r6` | 58 | 12 | False | 13 |
| `reports/round-34/handoff/declared-in-r7` | 58 | 12 | False | 13 |

**Consequence for the guard.** A guard written against the rendered `packet.md` compares 12 against
58 and is silent on every row forever — a vacuous pass that reads green. The guard must read the
**source** packet's `assembly.source_sha256` via the already-existing `v3_mine_d4`
(`assembly.d4["components"]`), which is what §3's prototypes do. This is R03-C1, independently
reproduced here (R03 §3.1-§3.3), and it is the reason the "in-sync green" selftest control must be
built on the source channel.

---

## 3. The guard's measured behavior — this seat's prototypes (drafts, not O01's design)

### 3.1 Method

Three isolated `git archive HEAD` copies under `.scratch/o06/`. In each, one guard block was
inserted immediately after `assembly = V3Assembly(root)` (`tools/exercise-handoff-e2e.py:3821`),
**before** the existing `dropped` block at `:3823` so the existing check keeps priority and the new
record is still emitted:

```python
        # prototype: D4-scoped manifest-vs-read-set guard (record-only)
        _manifest_d4 = sorted(rel for rel in assembly.d4["components"] if rel not in set(V3_READ_SET))
        if _manifest_d4:
            for rel in _manifest_d4:
                record("manifest-roster", False,
                       f"{rel}: in the packet component manifest but not in the live read set "
                       f"({len(V3_READ_SET)} members)")
```

`assembly.d4["components"]` is the `v3_mine_d4` map (13 members, §2.1); `assembly.digests` is keyed
by `V3_READ_SET` only (`:3483-3486`), so `- set(V3_READ_SET)` and `- assembly.digests.keys()` are
identical. The raising variant adds one line:

```python
            raise Failed("E2E-READSET",
                         f"{len(_manifest_d4)} packet-manifest member(s) are not in the live read set: "
                         f"{', '.join(_manifest_d4)}")
```

### 3.2 Record-only: names, keeps r7 green, selftest green — and the name is channel-bound

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet          # in g-rec
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19     exit 0

$ … --profile v3 --quiet | grep -c manifest-roster                       → 0     ← the claim's own command
$ … --profile v3         | grep -c manifest-roster                       → 1
FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component
  manifest but not in the live read set (58 members)
$ … --profile v3 --quiet --json | checks[] manifest-roster rows          → 1  (ok=False)
$ … --profile v3 --selftest   → "selftest: OK — positive run … plus 43 controls:"  exit 0
```

The name lands on **stdout, suppressed by `--quiet`** (`:4652`, `if not args.quiet:` before the
record loop) and in the **`--json` receipt** (`:4687`, `checks: records`). Both survive; `--quiet`
alone does not. The selftest's positive run stays green because the record-only guard never raises,
and the selftest fixture pins the **live** read set at freeze (`v3_build_fixture_root`, `:4149`;
`:4165-4168`), so it reproduces the same asymmetry without failing.

**Ordering constraint, measured.** Because the prototype sits *before* `:3823`, a superseded-row
replay emits the new `manifest-roster` row **and then** the pre-existing `E2E-READSET` (§4.3). Placed
*after* `:3838`, the pre-existing raise would abort first and the new naming would never be emitted
on those rows. The placement is therefore load-bearing for the naming's observability.

### 3.3 Raising: reds the r7 chain and breaks the selftest's own positive run

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet          # in g-raise
handoff-v3: exit=1 … packet_sha256=(not assembled)
handoff-v3: E2E-READSET: 1 packet-manifest member(s) are not in the live read set:
  examples/culture-d4/components/13-register-law.yml                                 exit 1

$ … --selftest
  File ".scratch/o06/g-raise/tools/exercise-handoff-e2e.py", line 4194, in v3_selftest
    assert code == EXIT_PASS, [(r["check"], r["detail"]) for r in records if not r["ok"]]
AssertionError: [('manifest-roster', '…13-register-law.yml: in the packet component manifest but not
  in the live read set (58 members)'), ('verdict', '1 packet-manifest member(s) …')]           exit 1
```

So *"refuses"* in the claim's wording contradicts the claim's own threshold *"the r7 default chain
still exits 0 unchanged"* and breaks the selftest. R02 Finding 3, reproduced.

### 3.4 In-sync control: the guard goes silent, but the default chain is red for a different reason

In `g-sync` the 13th member was added to `D4_COMPONENTS` (read set 59, manifest 13, i.e. in sync):

```
$ … --profile v3 | grep -c manifest-roster                               → 0    (guard silent, correct)
$ … --profile v3 --quiet
handoff-v3: exit=1 … packet_sha256=(not assembled)
handoff-v3: E2E-DIGEST: the assembled packet does not match the frozen packet digest
```

The guard's "in-sync green" half is observable only in the **selftest fixture** (which freezes the
live 59-member read set), not against the filed r7 baseline — the r7 row pins the 58-member packet
(`45f57132…`). The two halves of the claim's threshold therefore live on **two different baselines**,
and a verifier must not read the `E2E-DIGEST` on a synced live tree as a guard failure.

### 3.5 The guard does not block its own remedy

```
$ … --profile v3 --freeze .scratch/o06/frz      # record-only guard, isolated copy
no tracked value changed since the previous freeze
froze …: packet sha256 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
                                                                                  exit 0
```

`v3_freeze` calls `v3_preflight` (`:3997-4005`), and the record-only guard is non-refusing on the
read-set side, so the re-freeze fix route stays reachable. A *raising* guard would make the fix route
unreachable — R03-C2's constraint, confirmed by this control.

---

## 4. After → the grading surface a landing must move, and what the receipt can/cannot grade

### 4.1 The claim's declared counting commands, and their runnability

| # | command (`claims.json:23`) | runnable now? | observed |
|---|---|---|---|
| 1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | **yes** | exit 0, `packet_sha256=45f57132…` — and, under a record-only guard, **0 naming hits** (§0) |
| 2 | `python3 reports/round-38/run-validation.py` | **no** — `ls` → No such file or directory | `to-verify`; and per F-C13-1 never runnable in-tree regardless |

So **half** the claim's declared verification surface is absent at write time, and the half that
exists cannot observe the guard's naming. Both halves must be repaired by the integrator before the
claim is gradeable (§7, Owed).

### 4.2 The two selftest controls the claim requires, as falsifiable gates

`claims.json:21` requires *">=2 selftest controls (manifest-member-not-in-readset named; in-sync
green)"*. From §3's measurements the controls must assert on the **record channel**, not the exit
code, and on the **source** manifest, not the rendered text:

| control | asserted over | expected (measured basis) |
|---|---|---|
| manifest-member-not-in-readset **named** | the `records` list (`checks[]` in `--json`; verbose stdout) | one row naming `examples/culture-d4/components/13-register-law.yml`; **exit unaffected (0)** — §3.2 |
| in-sync **green** | the same channel, in the selftest fixture | zero `manifest-roster` rows — §3.4 |
| r7 default chain unchanged | `--profile v3` exit + packet sha | exit 0, `45f57132…` — §3.2 |
| r7 `--freeze` still reachable | `v3_freeze` path | not blocked — §3.5 |
| **source** manifest, not rendered | the guard's own read | `assembly.d4["components"]` (13), never the rendered table (12) — §2.3, §3.1 |

The existing selftest has 43 controls and the read-set family is `m12a/m12b/m13a/m13b/m14a/m14b`
(`:4438-4509`); a new control pair should extend that family, and the positive run must stay green
(§3.2) — which the **raising** variant fails (§3.3).

### 4.3 The regression expectation, corrected by measurement

Under the record-only prototype, replaying each filed row against the live tree:

| filed row | new `manifest-roster` row | pre-existing `E2E-READSET` | exit |
|---|---|---|---|
| `declared-in-r2` | names `13-register-law.yml` | names `reports/round-20/handoff/claims-map.md` | 1 |
| `declared-in-r5` | names `13-register-law.yml` | names `…claims-map.md` | 1 |
| `declared-in-r6` | names `13-register-law.yml` | names `…claims-map.md` | 1 |
| `declared-in-r7` | names `13-register-law.yml` | none | **0**, packet `45f57132…` |

Three readings follow, each of which contradicts a different filed expectation:

1. **`targets.json` O08's "only the r7 row names; others stay green" is unsatisfiable.** The guard
   names on **every** row (§0, §2.3) because it compares the live tuple against the live source
   manifest — no baseline can change that. The correct form is *"the guard adds exactly one named row
   per replay (`13-register-law.yml`); r7 is the only row whose exit is 0; the other three rows' exit
   1 is the pre-existing `E2E-READSET` supersession, not a guard regression"*. X02 §4a/§4b and
   A02 F-A02-3 reached the same correction independently; this seat's contribution is the direct
   guard measurement rather than the manifest census.
2. **The guard's row must be distinguishable from the existing `read-set-roster` row.** Both classes
   currently use `ok=False` records in the same run (§4.3 row 1 emits two `False` rows). R02's
   guard-point recommendation says the detail must distinguish them; the prototype uses a distinct
   `check` name (`manifest-roster` vs `read-set-roster`) and a distinct detail prefix.
3. **O08's mission cannot be executed as written.** Replaying r2/r5/r6 aborts at `E2E-READSET` unless
   the guard is placed before `:3823` (§3.2), and even then the row's verdict is not a *manifest*
   verdict. X02 §4b finding 1 said the same.

### 4.4 What a landing still owes (the after-state this receipt cannot measure)

Nothing in the O block has landed. The measured after-state requires: (a) the guard in
`tools/exercise-handoff-e2e.py` reading `assembly.d4["components"]`, record-only, placed before
`:3823`; (b) the two selftest controls on the record channel; (c) the corrected O08 expectation
(§4.3); (d) the fix-route cascade decided (§5). Items (a)-(c) are the integrator's, informed by
§3-§4. None of them is a filed byte.

---

## 5. The fix route and its cascade (O04/O05), carried not absorbed

O04 (`reports/round-38/op/O04-fix-route.md`) and O05 (`reports/round-38/op/O05-verify-route.md`) own
this; this receipt records only what the cascade means for claim O's acceptance, and reproduces the
one measurement that decides it:

- A read-set-only edit is a **red** default chain: adding the 13th member to `D4_COMPONENTS` leaves
  the r7 baseline pinning the 58-member packet → `E2E-DIGEST`, exit 1. Reproduced here in `g-sync`
  (§3.4) and independently by A01 §3c, R02 Finding 4, R03 §6.
- So the fix is the **paired move** (read-set add **plus** the two default constants re-pointed to a
  successor row), landed by the next re-freeze; **zero freeze bytes move this round**.
- **Two filed runners assert the old literals and will red on the re-point** (O05 §5). Measured:

```
$ grep -n "declared-in-r7" reports/round-34/run-validation.py reports/round-35/run-validation.py
reports/round-34/run-validation.py:23:R7 = f"{ROUND}/handoff/declared-in-r7"
reports/round-35/run-validation.py:22:R7 = "reports/round-34/handoff/declared-in-r7"
reports/round-35/run-validation.py:225:    for moved in ('V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"',
reports/round-35/run-validation.py:226:                    'V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"'):
```

  r34's `D5` leg (`:177-178`) and r35's `O7` leg (`:225-226`) require those exact strings to be
  **present** in the renderer; after the re-point both are absent. Filed bytes cannot be edited, so
  the landing must record those legs as superseded (or land in a round that does not re-run r34/r35).
- The r30-post battery pin (`tools/gates/expected/register-law-gate/r30-post/expected.json:10`,
  `gate_sha256 15f8b232…`) is **not** touched by the O block — the O guard edits
  `tools/exercise-handoff-e2e.py`, which the battery does not register
  (`tools/check-gate-battery.py:117-132` lists 7 + 2 + 1 gate names; the renderer is not among them).
  Measured: `python3 -B tools/check-gate-battery.py` → `exit=0, pass 7, unevaluable 0`.

---

## 6. Round-38 record state this receipt depends on

| seat | out path | landed? | consequence for claim O |
|---|---|---|---|
| `O01` guard design | `op/O01-guard-design.md` | **absent** | no design draft to verify; §3 supplies a measured prototype in its place |
| `O02` isolated verify | `op/O02-isolated.md` | **absent** | no isolated guard verification owed to O01 |
| `O03` verifier | `op/O03-verify.md` | **absent** | no independent verification of O02 |
| `O04` fix route | `op/O04-fix-route.md` | landed | §5 carries it |
| `O05` route verify | `op/O05-verify-route.md` | landed | §5 carries it (D-1/D-2 defects noted) |
| `O07` scribe | `op/O07-scribe.md` | landed, **0 bytes** | empty file — no landed-changes material for the O block |
| `O08` regression sweep | `op/O08-regression.md` | **absent** | §4.3 measures the sweep directly |

`reports/round-38/run-validation.py` is **absent**; claim O's second counting command and its
threshold command are `to-verify` until the integrator lands it (§4.1). O05's `D-1` (variant B is not
"equal functional coverage") and `D-2` (variant C's packet digest is a function of the successor
directory's literal name) remain open in O04's draft and are the integrator's reconciliation.

---

## 7. Counting commands for this receipt

Every command below was run by this seat, at the revision in §1, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. None is a round runner; none writes to the
repo except scratch under `.scratch/o06/`.

```sh
# state pins
git rev-parse HEAD                                   # 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
git status --porcelain                               # only "?? reports/round-38/"
date -u +%FT%TZ                                      # 2026-10-19T11:14:27Z
sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json} \
          tools/exercise-handoff-e2e.py examples/culture-d4/components/13-register-law.yml

# before-state census (§2)
python3 -c 'ast over tools/exercise-handoff-e2e.py'          # D4_COMPONENTS 12, V3_READ_SET 58
python3 -c 'runpy; v3_mine_d4(".")'                          # mined 13; 13-register-law not in read set
grep -rn "manifest-roster" tools/ examples/                  # exit 1, no guard class exists
python3 -c 'regex census: rendered packet.md rows'           # 58 rows / 12 D4 / has13 False
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet   # exit 0, packet 45f57132…

# the guard prototypes (§3) — isolated copies only
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet   # g-rec: exit 0, packet 45f57132…
python3 -B tools/exercise-handoff-e2e.py --profile v3           # g-rec: 1 manifest-roster FAIL row
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet | grep -c manifest-roster   # 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --json                      # 1 row, ok=False
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest                          # g-rec exit 0 (43 controls)
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet   # g-raise: exit 1 E2E-READSET
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest                          # g-raise exit 1, AssertionError
python3 -B tools/exercise-handoff-e2e.py --profile v3           # g-sync: 0 manifest-roster rows
python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/o06/frz           # exit 0, no change

# filed-row replay under the guard (§4.3) — isolated copy
for row in r2 r5 r6 r7: python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline <row> --quiet

# fix-route cascade (§5)
grep -n "declared-in-r7" reports/round-34/run-validation.py reports/round-35/run-validation.py
python3 -B tools/check-gate-battery.py                       # exit 0, pass 7, unevaluable 0
ls reports/round-38/run-validation.py                        # No such file or directory
```

## Owed

| # | owed artifact | owner | reason |
|---|---|---|---|
| 1 | The **guard landing** in `tools/exercise-handoff-e2e.py`: D4-scoped, **record-only**, reading `assembly.d4["components"]` (source manifest), inserted before `:3823` | integrator (per O01's design, absent) | §3 measures the shape; nothing has landed. A rendered-manifest guard is vacuous (§2.3). |
| 2 | The **two selftest controls** on the record channel, plus the corrected O08 expectation | integrator | §4.2/§4.3; `targets.json` O08's wording is unsatisfiable as filed and this seat may not edit it. |
| 3 | `op/O01-guard-design.md`, `op/O02-isolated.md`, `op/O03-verify.md`, `op/O08-regression.md` | the four missing seats | absent from the landed set (§6); §3-§4 stand in for the measurements, not for the seats. |
| 4 | `op/O07-scribe.md` is **0 bytes** | integrator / O07 | no landed-changes material exists for the O block; the file is present but empty. |
| 5 | `reports/round-38/run-validation.py` | integrating parent | absent; claim O's counting command 2 and threshold command are `to-verify` (§4.1). |
| 6 | O04 `D-1` / `D-2` reconciliation | integrator | O05's defects in O04's draft (B's coverage claim; C's path-dependent digest) remain open in the filed draft. |
| 7 | The r34 `D5` / r35 `O7` literal-assertion decision at landing | integrator | §5; filed bytes cannot be edited. |
| 8 | The **claim's acceptance channel** | integrator / operator | §0: the claim's own `--quiet` counting command cannot observe the guard's naming. Either the command or the acceptance reading must change; this seat reports it and does not re-scope the round. |

## Citations

- Binding rules and this seat's assignment: `reports/round-38/targets.json:3-9` (shared rules; `:8`
  F-C13-1), `:139-144` (O06 row, out path), `:230-235` (O08 row and its expectation),
  `:104-149` (the O block).
- Claim O: `reports/round-38/claims.json:9,19-24,26-27` (claim text, thresholds, counting commands,
  non-goals).
- Renderer internals: `tools/exercise-handoff-e2e.py:157-170` (`D4_COMPONENTS`, 12);
  `:1939-1965` (`V3_READ_SET`, 58); `:2045-2056` (`v3_mine_d4`, 13); `:2208-2222`
  (`v3_verify_component_digests`, 26/26); `:3480-3510` (`V3Assembly`; `digests` keyed by the read
  set); `:3645-3662` (`assert_manifest_equality`, `checked == len(V3_READ_SET)`);
  `:3821-3838` (the existing one-directional roster guard, `read-set-roster`/`E2E-READSET`);
  `:1346`,`:3654` (the two rendered-manifest presence checks); `:3997-4005` (`v3_freeze` →
  `v3_preflight`); `:4149-4194` (`v3_build_fixture_root`, the positive run, the read-set fixture pin);
  `:4438-4509` (controls `m12a`..`m14b`); `:4568-4574` (the CLI flags); `:4652`,`:4660`,`:4687`
  (the `--quiet` / `--json` output paths).
- Defect and adjudication: `reports/round-37/adj/A01-freeze-adjudication.md:5,24-35`;
  `reports/round-37/op/defect-queue.json` (`R36-R7-READSET-13`, `r37-A01-readset-roster-defect`).
- Filed rows and pins: `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json}`
  (`58` inputs, 12 D4 rows, `packet_sha256 45f57132…`, `twin_sha256 0e229138…`);
  `reports/round-22/handoff/{declared-in,declared-in-r2}/`, `reports/round-26/handoff/declared-in-r5/`,
  `reports/round-30/handoff/declared-in-r6/` (each 58 rows / 12 D4 rows / no `13-register-law`).
- Cascade: `reports/round-34/run-validation.py:23,177-178`; `reports/round-35/run-validation.py:22,225-226`;
  `tools/check-gate-battery.py:117-132` (registered gate names; the renderer is not among them);
  `tools/gates/expected/register-law-gate/r30-post/expected.json:10` (`gate_sha256 15f8b232…`).
- Sibling fragments read in full and folded: `reports/round-38/op/O04-fix-route.md` (§1-§6, the fix
  route and its repin row), `op/O05-verify-route.md` (§1-§6, D-1/D-2 and the r34/r35 cascade),
  `review/R02-o-review.md` (Findings 1-6, the guard-point recommendation),
  `review/R03-cross-review.md` (C1-C4), `cross/X02-honesty.md` (§3, §4a/§4b),
  `adj/A01-scope.md` (§3a-§3d), `adj/A02-receipt.md` (F-A02-3), `adj/A03-verify.md`,
  `depth/D07-receipt.md` (§0, §5, §Owed 6), `scribe/S02-telemetry-draft.md`.
- Command/output evidence: §1 (`git rev-parse`, `git status --porcelain`, `date -u`, `sha256sum`),
  §2 (ast census, `v3_mine_d4` runpy census, the `grep` for the guard class, the rendered-manifest
  regex census), §3 (the three prototype variants: exits, packet shas, the `grep -c` counts on
  verbose vs `--quiet`, the `--json` row, both selftests, the `--freeze` run), §4.3 (the four
  filed-row replays), §5 (`grep` on the two filed runners, the battery run, `ls` on the absent
  runner).

---

*This receipt claims no promotion, no canon, no clearance and no closure. A green gate is a
measurement, not a verdict. The substantive additions beyond O04/O05 are §3 (the guard's behavior
measured directly, with the two controls and the ordering constraint) and §0/§4.1 (the claim's own
counting command cannot observe the guard's naming).*
