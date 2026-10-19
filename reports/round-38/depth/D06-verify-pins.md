- Seat: D06 | verifier | claim D | date 2026-10-19 | baseline 9bccc9b

# D06 — verify D04's pin census

**Assignment** (`reports/round-38/targets.json`, seat `D06`): *"Verify D04's pin census."*
Out path `reports/round-38/depth/D06-verify-pins.md`. Binding `shared_rules` read at
`reports/round-38/targets.json`: write only this out path; never edit filed bytes
(`reports/round-1..37/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`);
no git commits/pushes/installs/network; **ABSOLUTE** never run any
`reports/round-*/run-validation.py` in-tree (F-C13-1) — isolated `git archive` copies only;
no re-freeze of `reports/round-34/handoff/declared-in-r7`; every claim cites file:line or
command output; unknowns `to-verify`; never fabricate.

**Verdict in one line.** `reports/round-38/depth/D04-pins.md` **does not exist** at this
seat's final sample, so the verdict on D04 is `could-not-evaluate`. The pin-census material
the round *did* produce (D07 §5, D03 §5, D09 §2.2, P01 §4, X02) landed, and I verified that
material independently by digest and by five isolated battery controls: **it reproduces**,
with three named omissions and one structural asymmetry the census does not record.

## 0. Status of the artifact under verification

```
$ find reports/round-38 -type f | sort
reports/round-38/adj/A01-scope.md        reports/round-38/depth/D03-isolated.md
reports/round-38/adj/A02-receipt.md      reports/round-38/depth/D05-verify.md
reports/round-38/adj/A03-verify.md       reports/round-38/depth/D07-receipt.md
reports/round-38/claims.json             reports/round-38/depth/D09-scribe.md
reports/round-38/cross/X02-honesty.md    reports/round-38/depth/D10b-verify.md
reports/round-38/plan/P01-d-plan.md      reports/round-38/scribe/S02-telemetry-draft.md
reports/round-38/targets.json            reports/round-38/telemetry/{availability-attempt-1,dispatch-declared}.json
$ ls reports/round-38/depth/D04-pins.md
ls: cannot access 'reports/round-38/depth/D04-pins.md': No such file or directory
```

No `depth/D04-pins.md` at any sample. **The comparison against D04's written census is
owed** (see `## Owed`). What follows is therefore (a) a ground-truth census built
independently from the tree, and (b) verification of the pin-census claims that *did* land,
so the integrator has a ready diff the moment D04 appears.

State pins for this fragment:

| pin | value | command |
|---|---|---|
| baseline | `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` | `git rev-parse HEAD` |
| tracked drift | empty | `git diff --stat HEAD` |
| untracked | only `?? reports/round-38/` | `git status --porcelain` |
| stamp | `2026-10-19T11:07:40Z` | `date -u +%FT%TZ` |
| `claims.json` | `45ff6f202a567042…` | `sha256sum reports/round-38/claims.json` |
| `targets.json` | `fe3091b91623f472…` | `sha256sum reports/round-38/targets.json` |

Method: every gate and battery run was issued inside `git archive HEAD | tar -x` copies under
`.scratch/d06/` (gitignored) with `export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1`. No
`reports/round-*/run-validation.py` was executed anywhere, in-tree or in a copy. No `--freeze`
was issued. No in-tree byte was written; the in-tree packet digest was re-checked after every
mutation round (`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`,
unchanged).

## 1. Ground-truth census — every digest-pinned row that could carry a D-claim cascade

The pin architecture has **three** row homes, all of which the battery discovers
(`tools/check-gate-battery.py:148-152`): `tools/gates/expected/`, `tools/gates/frozen/`,
`reports/round-9/baselines/`. A full sweep returns **20** `expected.json` rows, every one
carrying a non-empty `inputs` map:

```
$ python3 - <<'PY'   # sweep of all three roots
... 20 rows, readings: {pinned: 20}
PY
```

`python3 -B tools/check-gate-battery.py` on a pristine isolated copy →
`battery_exit 0`, `baselines_found 20`, `coverage 10/10`, `readings {"pinned": 20}`,
`gates_uncovered []`.

**Which rows pin a gate the D claim can move.** The D claim's two legs edit
`tools/gates/argot-derivation-gate.py` (F-6) and `tools/gates/register-law-gate.py` (RL-8)
(`reports/round-38/claims.json:13-16`). Matching each row's `gate_sha256` against the live
digest of every D-claim-adjacent tool:

| live tool | live sha256 (this seat, `sha256sum`) | pinned in |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` | **nowhere** |
| `tools/gates/register-law-gate.py` | `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169` | `tools/gates/expected/register-law-gate/r30-post/expected.json` |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` | `examples/culture-d4/expected-holds.json` `projector_sha256`; `d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/expected.json` |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | same three rows |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `d4-assembly-check-gate/r19-pre/expected.json` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | `tools/gates/frozen/round-26/{gate-input,post-register}/` manifests + receipts |

```
$ grep -rl b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb tools/gates/expected tools/gates/frozen
(no match, exit 1)
```

So **5** `expected.json` rows pin a live gate in the D claim's blast radius, and the argot
gate — the F-6 host — is pinned by **none of them**.

**The r30-post row, checked digest-for-digest:**

```
pinned gate_sha256  15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169
live   gate sha256  15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169   match True
inputs: examples/culture-d4/packet.d4.yml           aac91246cede8840…  match True
        tools/gates/register-law-gate.py            15f8b23251ca2ad0…  match True
        tools/gates/naming-collision-gate.py        d9e4e8f4f93a21b3…  match True
```

## 2. The D claim's counting commands, re-run on the baseline

```
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
  coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 \
            claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
  dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4…            exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
  coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 \
            force_failures=0 consequence_failures=0 dangling=0 findings=0         exit 0
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
  summary: 20/20 legs passed                                                  exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest   → 27/27 checks passed, exit 0
python3 -B tools/gates/register-law-gate.py --selftest       → 45/45 checks passed, exit 0
python3 -B tools/assemble-culture-d4.py --selftest           → 81/81 checks passed, exit 0
```

`reports/round-38/run-validation.py` **does not exist** (`ls` → No such file or directory),
so claim D's third declared counting command is `to-verify` regardless of any landing.

Independently reproduced: `grep -rl "derived_forms\|derived_ok" examples/ tools/ corpus/`
→ **no match (exit 1)**. K01 r36's F-6 census (`reports/round-36/scout/K01-register-scout.md:115`)
holds at this baseline. `grep -rl "D4L-ERA" examples/ tools/ corpus/` → only
`corpus/lessons/round-18.md`; the era leg is still absent as an executable.

## 3. Verification of the pin-census claims that landed

### 3.1 D07 §5's four "current" rows — all reproduce

`reports/round-38/depth/D07-receipt.md:252-259` states four surfaces are digest-current. Each
re-measured by digest, not read from the file:

| D07 §5 row | D07's value | my independent measurement | verdict |
|---|---|---|---|
| `typed-pipelines.json profiles[0]` packet | `aac91246cede8840…` | `sha256sum examples/culture-d4/packet.d4.yml` → `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` | **verified** |
| … projection | `c23b0ab532cfb9d4…` | `…c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` | **verified** |
| … expected | `e6ae9828d6c82aa6…` | `…e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` | **verified** |
| … assembler / adapter | `943f487ba991d45d…` / `92f5460bcc34ffbb…` | identical to live | **verified** |
| `expected-holds.json` pointers | packet/projection/projector + `active_pin_generation round-30-qreg-records` | all four read from the file, all identical to live | **verified** |
| superseded generation still a row | `pin_generations[0]` round-28 `543d68a82640e1b0…` | present, unedited; `profiles` has 2 rows | **verified** |
| `r30-post` pins packet + gate | `aac91246…` / `15f8b232…` | both match live (§1) | **verified** |

### 3.2 A01 §3a/§3b's blast radius — reproduced with two isolated controls

`reports/round-38/adj/A01-scope.md:§3` claims editing the law gate reds a filed pin and
editing the argot gate does not. Both reproduced in `git archive HEAD` copies, editing
**only** the copy, then restoring from a `cp` backup and re-checking the digest:

```
# 3a — append one comment line to tools/gates/register-law-gate.py (copy only)
new sha 11d050e1fddfd2b0…
python3 -B tools/check-gate-battery.py   → exit 2
  readings {"gate_revised": 1, "pinned": 19}
  BASELINE-GATE-REVISED: gate_sha256 15f8b23251ca2ad0... differs from the live
    register-law-gate.py 11d050e1fddfd2b0...: re-freeze, never compare across an unnamed revision
restored sha 15f8b23251ca2ad0…

# 3b — same append to tools/gates/argot-derivation-gate.py (copy only)
python3 -B tools/check-gate-battery.py   → exit 0
  readings {"pinned": 20}
restored sha b5406bcdaf41c595…
```

The mechanism is at `tools/check-gate-battery.py:525` (`script = gates_dir / gate_name` — the
**live** gate) and `:541-544` (`gate_revised` → exit 2). A01's reading is exact, including
its conclusion that the selftests are not the instrument that catches a gate revision.

### 3.3 D09 §2.2's five-surface table — verified, including the membership rows

D09 claims the projection and `expected-holds.json` are members of `V3_READ_SET`, and that
`typed-pipelines.json` is pinned by the `L1-profile` leg. `V3_READ_SET` is built from named
constants, so a literal string grep is a false negative; expanding the tuple by import:

```
V3_READ_SET len = 58
  typed-labels.d4.yml          present=True   ['examples/culture-d4/typed-labels.d4.yml']
  expected-holds.json          present=True   ['examples/culture-d4/expected-holds.json']
  packet.d4.typed.yml          present=True   ['examples/culture-d4/packet.d4.typed.yml']
  d2-typed-labels.py           present=True   ['tools/d2-typed-labels.py']
  typed-pipelines.json         present=False
  13-register-law.yml          present=False
  argot-derivation-gate.py     present=False
  register-law-gate.py         present=False
D4_COMPONENTS len = 12
```

D09's rows 1–3 verify (`tools/exercise-handoff-e2e.py:1939-1953` for membership,
`:2225-2240` for `v3_verify_d4_pins`, whose docstring reads *"Every pin the D4 tree states
about itself, re-measured against live bytes"*). `V3_READ_SET` is 58 long, matching the 58
`inputs` in `reports/round-34/handoff/declared-in-r7/expected.json` — and that file's D4
component list is exactly 12, with `13-register-law.yml` absent, independently confirming
`reports/round-37/adj/A01-freeze-adjudication.md` and the O claim's premise.

### 3.4 P01 §4's "argot absent from the name constants" — verified verbatim

`tools/check-gate-battery.py:117-132` lists `GATE_NAMES` (7), `D4_GATE_NAMES` (2),
`REGISTER_LAW_GATE_NAMES` (`("register-law-gate.py",)`), `BASELINE_ONLY_GATE_NAMES`,
`REGISTERED_GATE_NAMES`. `argot-derivation-gate.py` appears in **none** of them. P01's
`:272` citation is exact.

## 4. Defects in the landed census — three omissions and one asymmetry

**(a) The F-6 host has no baseline row to update, and is outside the registered set.**
Claim D's `after_required` asks that "pins [be] updated as new rows"
(`reports/round-38/claims.json:16`). For the law gate that is well-defined: `r30-post` exists
and a successor row is owed. For the argot gate there is **no row at all** (§1), and it is
absent from `REGISTERED_GATE_NAMES`, so the battery neither pins it nor counts it in
`coverage 10/10`. Under `corpus/knowledge/verification/gate-frozen-run-standard.md:§1` and
`§6` a gate with a self-test and no committed baseline does **not** meet the two-evidences
clause and the gap is a conformance defect, not a green. D03 §5.1 and D09 §2.2 name the
r30-post successor row; **neither names the argot gate's missing row.** Recommended host for
F-6 (`reports/round-38/plan/P01-d-plan.md:272`) and missing-baseline gate are the same
artifact, so the two facts belong in one place in D04.

**(b) D07 §5's row list is narrower than the tree.** It names `r30-post` as the
`tools/gates/expected/` surface. The sweep finds 5 rows whose `gate_sha256` equals a live
D-claim-adjacent gate (§1). Four are the typed-labels/assembly adapters, which a pure
gate-file edit does not move — so D07's *conclusion* holds — but a census that enumerates
pin surfaces should list them, because the projection route (D09 §2.2, P01 §4) does move
them.

**(c) `tools/gates/typed-pipelines.json` is digest-unenforced by both instruments.** Its live
digest is `76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d`. It is pinned by
**no** `expected.json` (no `inputs` key in any of the 20 rows names it), and it is **not** in
`V3_READ_SET` (§3.3). D07 §5 and D09 §2.2 both list it as a pin surface, which is right — but
nothing verifies its own bytes. `typed-pipeline-gate.py` reads it live and refuses on a stale
pin *inside* it (`L1-profile`), which protects the artifacts it points at, not the file. The
r30-post-style coverage of this file rests on filed prose only
(`reports/round-30/fixes/qreg-dangles.md`, `reports/round-30/audit/x38-law-gate-clean-state.json`).

**(d) The structural asymmetry the census does not record: the battery resolves
`gate_sha256` live and `inputs` mirror-first.** `check-gate-battery.py:570-579` resolves each
`inputs` path against the baseline directory first (`target = base_dir / relative`) and only
falls back to `gates_dir`/`repo_root` when the in-baseline copy is absent, adding
`BASELINE-EXTERNAL-INPUT`. Two controls settle it:

```
# A1 — append a comment to the LIVE packet (examples/culture-d4/packet.d4.yml, copy only)
python3 -B tools/check-gate-battery.py  → exit 0, readings {"pinned": 20}

# A2 — same append to the r30-post MIRROR copy
#      tools/gates/expected/register-law-gate/r30-post/examples/culture-d4/packet.d4.yml
python3 -B tools/check-gate-battery.py  → exit 2
  readings {"pinned": 19, "snapshot_tampered": 1}
  BASELINE-TAMPERED: examples/culture-d4/packet.d4.yml: digest ef3bd7922f01149f... does not
    match the pin aac91246cede8840...
```

So for `r30-post`: a **gate** edit reds the battery (control 3a), but a **live packet** edit
does not — the row is digest-live for the gate and digest-mirrored for the input. That is
the standard's own design (`gate-frozen-run-standard.md:§3` requires a committed copy), and
it is why `r30-post`'s `input_class` reads `live-read-set` with a mirrored read set. It is
worth naming because A01 §3a infers the law-edit blast radius from the gate pin alone, and a
reader could wrongly conclude the packet is likewise live-pinned.

## 5. The cascade D04 owes — new rows, never edits

For each residue leg, stated as a new-row draft (no filed byte moves; the standard forbids
rewriting a baseline to match a new run, `gate-frozen-run-standard.md:73-74`):

| # | landing | row owed | why |
|---|---|---|---|
| 1 | RL-8 era leg in `register-law-gate.py` (`15f8b232…` → new) | a **new baseline id** under `tools/gates/expected/register-law-gate/` (e.g. `r38-post`), carrying the new `gate_sha256`, its own mirrored read set, `expected.exit`/`class`/`findings` measured from a snapshot run, and a README index row | `r30-post` must stay byte-identical; `check-gate-battery.py:541-544` reads the old row `gate_revised` → exit 2 until the new row exists |
| 2 | F-6 counters in `argot-derivation-gate.py` (`b5406bcd…` → new) | **the gate's first baseline row** under `tools/gates/expected/argot-derivation-gate/` (new directory) | no row exists (§1); without one the F-6 host remains two-evidences UNMET |
| 3 | if F-6 lands in the projection instead (`d2-typed-labels.py`) | a new `typed-pipelines.json` `profiles[]` generation row **and** a new `expected-holds.json` `pin_generations[]` row, plus re-pointed top-level pointers | D09 §2.2 rows 2–5; the r26 template `reports/round-26/register/repin.json` carries `new_pins` beside `superseded_pins` |
| 4 | either leg's new digest | a new row in **this round's** fragments (never an edit of r30) | the old digests are filed at `reports/round-30/audit/x38-law-gate-baseline.json`, `reports/round-30/audit/x38-law-gate-clean-state.json`, `reports/round-30/rerun.json` — all three name `b5406bcd…` (measured; `grep -c` → 4, 4, 2) and must not be rewritten |

`13-register-law.yml` (`c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`) is
**not** in `V3_READ_SET` and is **not** in `D4_COMPONENTS` (§3.3), so a D landing that leaves
it alone drags no O-claim re-freeze — D07 §5's third bullet states this correctly and my
measurement confirms it.

## 6. What this fragment does not establish

- It is **not** a verdict on D04; D04 did not land. Every statement above is a verdict on the
  census material that did land, or a ground-truth measurement.
- A digest match is integrity, never truth and never clearance
  (`corpus/knowledge/verification/gate-frozen-run-standard.md:§10`). Nothing here asserts the
  D4 packet is good design, that the register law is correct, or that F-6/RL-8 should be
  landed at all.
- No `--freeze` was issued and no filed round was touched. The r7 pair is untouched
  (`packet.md 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`,
  `twin.json 0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`,
  `expected.json bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`).

## Owed

- **`reports/round-38/depth/D04-pins.md` — owed by D04.** The comparison of §1–§5 against
  D04's written census cannot be made until D04 lands. When it does, the diff to apply is
  §4(a) (argot gate has no row and is unregistered), §4(b) (5 rows pin a live D-claim gate,
  not 1), §4(c) (`typed-pipelines.json` digest-unenforced), §4(d) (gate-live / input-mirror
  asymmetry).
- **`reports/round-38/run-validation.py` — owed by the integrator.** Claim D's third counting
  command cannot run; absent at this sample.
- **The argot gate's first baseline row — owed to whoever lands F-6.** Named as a conformance
  defect, not absorbed here; the fix route is D04's or the integrator's call.

## Citations

- `reports/round-38/targets.json` seat `D06` (`mission`, `out`, `shared_rules`);
  `reports/round-38/claims.json:13-16` (claim D `after_required`), `:8` (dispatch).
- Census/verification targets: `reports/round-38/depth/D07-receipt.md:246-280` (pin surface),
  `:341` (D04's assignment); `reports/round-38/adj/A01-scope.md:§3` (blast radius);
  `reports/round-38/depth/D03-isolated.md:235-275`; `reports/round-38/depth/D09-scribe.md:160-220`;
  `reports/round-38/plan/P01-d-plan.md:244-280`; `reports/round-38/cross/X02-honesty.md:165-192`.
- Instrument: `tools/check-gate-battery.py:117-132` (name constants), `:148-152` (roots),
  `:222` (`BASELINE_ONLY_GATE_NAMES`), `:493-600` (`verify_baseline_spec`), `:525` (live gate),
  `:541-544` (`gate_revised`), `:570-579` (inputs resolution), `:594-600` (expected block).
- Pins: `tools/gates/expected/register-law-gate/r30-post/expected.json` (gate `15f8b232…`,
  inputs packet `aac91246…`, law gate, naming gate); `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/expected.json`;
  `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`;
  `tools/gates/typed-pipelines.json` (`profiles[0]` generation `round-30-qreg-records`, live
  `76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d`);
  `examples/culture-d4/expected-holds.json` (`packet_sha256`, `projection_sha256`,
  `projector_sha256 2819f687…`, `active_pin_generation`, `pin_generations[]`).
- Membership: `tools/exercise-handoff-e2e.py:157-170` (`D4_COMPONENTS`, 12),
  `:1939-1953` (`V3_READ_SET`, 58), `:2225-2240` (`v3_verify_d4_pins`);
  `reports/round-34/handoff/declared-in-r7/expected.json` (58 inputs, no
  `13-register-law.yml`); `reports/round-37/adj/A01-freeze-adjudication.md`.
- Standard: `corpus/knowledge/verification/gate-frozen-run-standard.md` §1 (scope / two
  evidences), §3 (layout, append-only `:73-74`), §4 (`inputs` map, `unpinned (legacy)`),
  §6 (readings, `snapshot_tampered` / `gate_revised`), §10 (digest is integrity, not truth).
- Residue: `reports/round-36/scout/K01-register-scout.md:103-125,208-215`;
  `reports/round-17/d4/design-brief.md:300-310` (F-6 requirement);
  `reports/round-25/argot/forecast.md:37`; `reports/round-26/register/repin.json`
  (`new_pins`/`superseded_pins` template).
- Command evidence, all run by this seat at `9bccc9b` with
  `export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1` in `git archive HEAD` copies under
  `.scratch/d06/`: `check-gate-battery.py` pristine → `exit 0`, `pinned 20`, `coverage 10/10`;
  controls 3a (`gate_revised` → exit 2), 3b (argot → exit 0), A1 (live packet → exit 0),
  A2 (mirror packet → `snapshot_tampered` → exit 2); argot/law/typed legs and the three
  selftests (§2); `sha256sum` sweeps (§1, §3.1); `grep -rl b5406bcd …` → no match (exit 1);
  `grep -rl "derived_forms\|derived_ok" examples/ tools/ corpus/` → no match (exit 1).
  In-tree packet re-checked after every mutation:
  `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`.
