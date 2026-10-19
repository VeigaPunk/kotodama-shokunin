- Seat: S02 | scribe | claim O | date 2026-10-19 | baseline 4a7aede

# S02 — final operability receipt (claim O), rev 1 + §8 peer fold

Cut 2026-10-19T08:17:53Z (`date -u +%FT%TZ`) at HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
(`git rev-parse HEAD`); §8 appended at the peer fold (~08:22Z), after
`op/O08-validation-legs.md` and `op/O10-scribe.md` landed. Mission: fold the
O-block verdicts into the claim-O final receipt. **No O-block peer fragment
existed at seat time** — `ls reports/round-35/` then returned only `claims.json`,
`targets.json`, `telemetry/` (round 35 is one 64-seat batch; all peers were in
flight). Per the missing-dependency rule this fragment therefore carries (a) the
before-state measured by this seat against live bytes, (b) one independent finding
this seat found and executed, (c) the acceptance legs the after-state must
satisfy, (d) the regression baseline measured pre-patch, and (e) the owed paths —
plus (f) the §8 fold of the peers that landed before this seat closed. Nothing
here asserts a verdict on fragments it has not read.

## 0. Verdict summary at this cut

| leg | verdict | basis |
|---|---|---|
| before-state defect (R34-N1) | **reproduced** — `KeyError` traceback at `tools/exercise-handoff-e2e.py:3822`, exit 1 | §2, isolated copy, command executed |
| defect mechanism | **pinned to the line** — the frozen r6 baseline pins a member the live `V3_READ_SET` no longer carries | §2.2, measured set diff |
| hardening patch (the O claim's after-state) | **not applied, not verified** — the integrator applies it; no patch bytes exist in any fragment this seat can read | §4; `git status --porcelain` clean except `?? reports/round-35/` |
| second, unreported defect in the same block (S02-F1) | **found, executed, filed here** — the read-set equality leg is one-directional and over-claims its count | §3, experiments A/B |
| regression baseline pre-patch | **measured** — r7 default chain exit 0; both selftest suites exit 0 (v1 17 controls, v3 39 controls; §8.1 corrects the earlier single-suite line) | §5 |
| freeze bytes | **pinned by digest, unmoved** | §6 |
| operability axis for round 35 | **not verified** — `claims.json` O `after_required` unmet at this cut | §4, §7 |

## 1. Isolation and preservation method

Every execution below ran in an isolated `git archive HEAD` copy
(`.scratch/s02-iso`), never in-tree; no `reports/round-*/run-validation.py` was
executed anywhere (F-C13-1 prevention; this seat executed no filed runner at
all). The copy carries the same `AGENTS.md` bytes as the repo root
(`diff .scratch/s02-iso/AGENTS.md AGENTS.md` → identical, 40 lines).

**Preservation, whole tree:** after running the r6 replay, the renderer
selftest and the r7 default chain in the copy, `diff -rq .scratch/s02-iso
.scratch/s02-iso2` (second fresh archive) reports exactly two differences —
the two scratch baselines this seat created (§3). Nothing else moved: the
tool's own write contract is "Writes go only to a fresh directory under
`TMPDIR` (plus `--freeze DIR`)" (`tools/exercise-handoff-e2e.py:93-94`).
Per-artifact check on the frozen r6 directory: `expected.json`, `freeze.txt`,
`packet.md`, `twin.json` byte-identical to `git show HEAD:…` after the runs
(sha256 compared per file). `run.log` in both frozen directories is
**gitignored** (`.gitignore:3` `*.log`; `git check-ignore -v` confirms), so it
is untracked at HEAD and must be preserved by on-disk digest, not by git.

## 2. Before-state, measured (the R34-N1 defect as it stands at HEAD)

### 2.1 The declared counting command, executed

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
  --baseline reports/round-30/handoff/declared-in-r6/expected.json
```

Observed in the isolated copy: **exit 1**, stderr traceback, no named
diagnostic:

```
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
                                                                                             ~~~~~~~~~~~~~~~~^^^^^
KeyError: 'reports/round-20/handoff/claims-map.md'
```

This breaks the tool's own documented contract: "Exit codes (stable messages,
**no traceback**): 0 clean; 1 mismatch — `E2E-DIGEST`, …; 2 could-not-evaluate
— `E2E-ARTIFACT` …, `E2E-BASELINE` …, `E2E-DATA`" (`tools/exercise-handoff-e2e.py:89-93`).
The r34 record already names this: "r6 row refuses replay (exit 1, KeyError
mechanism — named R34-N1)" (`SCORECARD.md:615`; `LOG.md:3612`).

### 2.2 The mechanism, pinned

The drift leg at `tools/exercise-handoff-e2e.py:3819-3824` iterates **the
baseline's** input map and dereferences the **live** digest map:

```python
drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]   # :3819
if drifted:
    for rel in drifted:
        record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")  # :3822  ← KeyError here
    raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: …")  # :3823
```

`assembly.digests.get(rel)` returns `None` for a vanished member (so it is
selected as drifted), and the failure branch then indexes `assembly.digests[rel]`
directly instead of the value it already computed — the KeyError. Measured set
diff between the frozen r6 baseline and the live read set (imported module,
`V3_READ_SET` at `:1935`):

- in baseline, not live: `reports/round-20/handoff/claims-map.md` (1 member)
- in live, not baseline: `reports/round-34/handoff/declared-in-r7/claims-map.md` (1 member)
- both sets are 58 members; `CLAIMS_MAP = "reports/round-34/handoff/declared-in-r7/claims-map.md"` (`:184`)

So the supersession the r34 repin performed (`reports/round-34/handoff/repin.json`,
re-frozen input row `0121559452f2… -> d181de28ccaf…`, `freeze.txt`) moved the
claims-map path; the r6 baseline still pins the old path; the refusal is
correct in intent and wrong in mechanism, exactly as `claims.json` states
(`"the refusal is correct but the mechanism is an unhandled exception"`).

## 3. S02-F1 — the same leg is one-directional and over-claims its count (new, executed)

Not reported by R34-N1. Two scratch baselines were built from the live r7
baseline by this seat (re-signed with the tool's own `v3_baseline_digest`), then
replayed in the isolated copy:

- **A — a live read-set member the baseline never pinned** (baseline 57 inputs,
  live 58; the r7 claims-map row dropped): `--baseline scratch-baseline-A.json`
  → **exit 0**, and the run records `OK   input-digest: 58 read-set digests
  match the frozen baseline` — while only 57 were compared. The record text
  counts `len(V3_READ_SET)` (`:3824`), not the number actually checked, so the
  leg over-claims coverage whenever the sets differ in that direction. The
  re-signed baseline passes `v3_load_baseline` (the integrity digest is
  content-derived and the six declared keys are untouched), so the tamper
  control at `:4449` does not cover this shape.
- **B — a baseline member whose live path is gone** (the r6 shape): same
  `KeyError` at `:3822`, exit 1 — the mechanism of §2 is not r6-specific; any
  superseded member reproduces it.

Reproduction recipe (any isolated copy; the two scratch baselines are rebuilt
by this exact script, so the finding does not depend on this seat's scratch):

```python
import importlib.util, json
spec = importlib.util.spec_from_file_location('e2e', 'tools/exercise-handoff-e2e.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
b = json.load(open('reports/round-34/handoff/declared-in-r7/expected.json'))
a = json.loads(json.dumps(b)); a['inputs'].pop(m.CLAIMS_MAP)          # A: live member unpinned
a['baseline_digest'] = m.v3_baseline_digest(a)
json.dump(a, open('scratch-baseline-A.json', 'w'), indent=1, sort_keys=True)
c = json.loads(json.dumps(b)); c['inputs'].pop(m.CLAIMS_MAP)          # B: superseded member
c['inputs']['reports/round-20/handoff/claims-map.md'] = '0' * 64
c['baseline_digest'] = m.v3_baseline_digest(c)
json.dump(c, open('scratch-baseline-B.json', 'w'), indent=1, sort_keys=True)
```

Severity: **latent, medium**. Today's r7 baseline and the live set agree
exactly, so no current chain is harmed; but the whole point of the r34/r35
supersession flow is that read-set membership moves, and in direction A the
replay silently proceeds with a shrunken comparison and a false count.
**Recommendation to the integrator/O-block:** the hardening should refuse on
**set inequality in either direction** (frozen members missing live *and* live
members absent from the frozen baseline), naming the member(s) and the
direction, and the `input-digest` record should state the number actually
compared. This does not widen the O claim's `after_required`; it closes the
same refusal surface the claim already asks for.

## 4. Acceptance legs for the after-state (for the integrator + validator author)

`claims.json` O `after_required` and `thresholds`, restated as checkable legs.
The patch is applied by the integrator; the numbers below are the pre-patch
values this seat measured (§5), so a leg that is already green pre-patch is a
regression leg, not evidence of the fix.

| leg | command | pre-patch observed | required post-patch |
|---|---|---|---|
| L1 named diagnostic at the r6 replay | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1 + traceback + `KeyError` (§2.1) | exit in **{1,2}**, one line carrying both the `E2E-READSET` token and the literal path `reports/round-20/handoff/claims-map.md`, **no `Traceback` and no `KeyError`** anywhere in combined stdout+stderr — O08 leg O1 is the binding form; `claims.json:48` expects exit 1, exit 2 is the convention-correct class (§8.2) |
| L2 renderer selftest | **v3 suite:** `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` (the suite the new controls belong to; allow ≥ 300 s, measured 39.2 s) | exit 0, `plus 39 controls`, 40 bullet lines | exit 0, **≥ 41 controls** (39 + the two new controls: superseded-row named refusal, preserved E2E-DIGEST path) and ≥ 42 bullet lines — assert the ≥ 41 floor plus the content anchors, not an exact count (§8.1, §8.2) |
| L2b v1 suite (the claim's bare `--selftest` command) | `python3 -B tools/exercise-handoff-e2e.py --selftest` (default `--profile v1`, `:4485`) | exit 0, `plus 17 controls` | unchanged 17 unless the integrator lands controls in `v1_selftest` — **the claim's O counting command names this suite, which is not the one the new controls belong to** (§8.1) |
| L3 r7 default chain unchanged | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, `packet_sha256=45f57132…` | exit 0, same `packet_sha256` (a moved packet digest would mean the patch changed assembly, not diagnostics) |
| L4 designed E2E-DIGEST path preserved | covered by L2's controls; direct controls: `m12a` `:4422` (exit 2 `E2E-BASELINE`), `m12b` `:4430` (exit 1 `E2E-DIGEST` naming the file), `m8` `:4438` (exit 1 `E2E-DIGEST`) | all green pre-patch | unchanged |
| L5 freeze bytes unmoved | `sha256sum reports/round-34/handoff/declared-in-r7/{claims-map.md,expected.json,freeze.txt,packet.md,twin.json}` | §6 digests | identical digests; no `--freeze` executed against `declared-in-r7` (`V3_FROZEN_DIR_DEFAULT` `:1934`) |
| L6 round acceptance | `python3 reports/round-35/run-validation.py` (parent-assembled, isolated-copy discipline) | n/a — validator not authored yet | exits 0 |

L1 must be judged on **both** the exit code and the absence of `Traceback`:
the pre-patch run already exits 1, so an exit-code-only leg would pass on the
unfixed tree.

## 5. Regression baseline measured pre-patch (so post-patch deltas are readable)

- r7 default chain: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`
  → exit 0, `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`
  — the digest equals the r7 `freeze.txt` packet pin.
- renderer selftest — **two suites, both measured** (corrected in §8.1; the
  earlier revision of this bullet conflated the v3 header with the v1 count):
  - **v1 suite**, `python3 -B tools/exercise-handoff-e2e.py --selftest`
    (default `--profile v1`, `:4485`; `v1_selftest` `:1635`, print `:1785`):
    exit 0, header `selftest: OK — positive run (exit 0, fields=16/16,
    glossary-entries=20, findings=0) plus 17 controls:`, 18 bullet lines;
    controls at `:1745` preservation, `:1755` tamper baseline, `:1763` tamper
    read-set, `:1774` re-signed scan expectation, `:1782` missing artifact.
  - **v3 suite**, `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`
    (`v3_selftest` `:4154`, print `:4461`): exit 0 after 39.2 s, header
    `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20,
    findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal,
    alias_leg=landed) plus 39 controls:`, 40 bullet lines; controls at `:4412`
    preservation, `:4422` m12a tamper baseline, `:4430` m12b tamper read-set,
    `:4438` m8 re-typed v2 row, `:4449` re-signed scan expectation, `:4457`
    missing D4 artifact.
- the two controls the claim asks to add do not exist pre-patch in either
  suite: no superseded-row control and no read-set membership control
  (grep over the `results.append` sites, `:1745-1782` and `:4412-4457`).

## 6. Freeze-bytes pin (measured at HEAD, before any patch)

```
34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9  tools/exercise-handoff-e2e.py
d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c  reports/round-34/handoff/declared-in-r7/claims-map.md
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
```

Untracked, so pinned from the working tree rather than from git
(`sha256sum`, in-tree files; `git check-ignore -v` marks both ignored):

```
ffae4ecdcf2558693e9ace21e918572e84d6be6607a5b8a5284805ab7e11136c  reports/round-34/handoff/declared-in-r7/run.log
b5ee33510af0297e162e24bcdcf4aea563cbf7f3d112faf85720587479e3ed47  reports/round-30/handoff/declared-in-r6/run.log
```

**Why the patch cannot move these:** `tools/exercise-handoff-e2e.py` is not a
member of `V3_READ_SET` (`:1935`; its members come from `V1_READ_SET` `:462`,
`TOOLS` `:134-140`, `HARNESS` `:180` and the D2/D4/packet constants — the
renderer itself is absent), and no freeze artifact pins its digest: the only
mentions of `exercise-handoff-e2e` inside the frozen directories are the
`frozen_by` / `run.log` / `packet.md` prose attributions, not digests
(`grep -rn exercise-handoff-e2e reports/round-34/handoff/declared-in-r7/
reports/round-30/handoff/declared-in-r6/`). `packet.md` and `twin.json` are
pinned by `freeze.txt`, and the baseline's `inputs` are digest-pinned inside
`expected.json` — a diagnostic-only patch touches none of them. `run.log` in
both directories is untracked (`.gitignore:3`), so the L5 leg should digest the
on-disk file, not `git show`.

## 7. What this receipt does NOT assert

- No claim that the hardening works: the patch is not in the tree at this cut.
- No verdict on `op/O01`-`O11`, `plan/P02`, `scout/K03`, `review/R04/R05`, or
  `cross/*` — none existed at seat time.
- No freeze re-run, no `--freeze` invocation, no filed-runner execution.
- No operability axis verdict and no round admission; both are the
  integrator's, on the delivered revision.
- S02-F1 is a code-read + executed-scratch finding on the isolated copy; it is
  **not** an in-tree defect today (r7 baseline and live set agree, §2.2).

## 8. Peer fold (appended after the initial cut; §0-§7 stand as the pre-fold revision with the corrections marked in place)

Peers that landed after this seat's cut and are folded here: `reports/round-35/op/O08-validation-legs.md`
and `reports/round-35/op/O10-scribe.md` (`ls reports/round-35/op/` at 08:19:53Z → those two
files only), both read in full. Still absent at this fold: `op/O01`-`O07`, `O09`, `O11`,
`plan/P02`, `scout/K03`, `review/R04`, `review/R05`, and the C/A/cross-block fragments.

### 8.1 Correction — the renderer has two selftest suites (this seat's own error)

The pre-fold revision of §5 and L2 conflated them. Measured, this seat, isolated copy:

| suite | command | header tail | bullet lines |
|---|---|---|---|
| v1 (CLI default) | `python3 -B tools/exercise-handoff-e2e.py --selftest` (`--profile` default `v1`, `:4485`) | `… findings=0) plus 17 controls:` | 18 |
| v3 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | `… alias_leg=landed) plus 39 controls:` | 40 |

The v3 run took 39.2 s and exited 0 (`timeout 280`, output at
`.scratch/s02-selftest-v3-before.txt`). Registration sites: `v1_selftest` `:1635`
(print `:1785`), `v3_selftest` `:4154` (print `:4461`). **The claim's O counting
command is the bare `--selftest` — i.e. the v1 suite — while the two new controls
belong to the v3 suite** (the superseded row is a v3 baseline). This is a named
under-specification of `claims.json`'s counting command, not an in-tree defect:
the acceptance must count the v3 suite (≥ 41) and may pin the v1 suite at 17
(unchanged). O08 §5 and O10's baseline table reached the same 39 independently.

### 8.2 Fold of O08 (binding legs O1-O6)

Agreements: O08's B1 = my §2.1 (same command, same exit 1, same line `:3822`, same
`KeyError`); O08's B2 = my §5 r7 chain (`45f57132…`); O08's B4/B5 = my §6
(nine tracked files SAME as HEAD; `run.log` gitignored, no HEAD reference, so a
before/after digest leg is the only honest form — my §6 pins both on-disk
digests); O08's O4 = my L5; O08's O3 = my L3; O08's O2 = my corrected L2.

Two deltas this receipt adopts:

- **Exit-code policy (O08 §4):** accept exit ∈ {1, 2} with the `E2E-READSET` token
  and the member path on one line, no `Traceback`, no `KeyError`; `claims.json:48`
  says "(expect: exit 1)", so an exit-2 landing must be recorded as a **named
  deviation**, never edited in place. My L1 now reads that way.
- **Two static legs O08 adds that my L-list did not carry:** O5 (the patch is
  present — live renderer sha ≠ `34c85f57…`, `git show HEAD:` sha == `34c85f57…`,
  source contains `E2E-READSET`) and O6 (the validator itself quotes no `--freeze`
  argv literal and names no filed round runner — F-C13-1/freeze fences). The
  integrator should carry both into `run-validation.py`; my §4 legs are a subset.

### 8.3 Fold of O10

O10 independently reproduced the same before-state (exit 1, traceback, `:3822`,
`KeyError`, contract citation `:89`) and the same read-set arithmetic (58/58 with
one member each way, 57 shared). It adds one precision my §2.2 should carry: the
round-20 map **still exists on disk** — `ls -l reports/round-20/handoff/claims-map.md`
→ 24,888 bytes, `sha256sum` → `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`,
which equals the digest the r6 baseline freezes for that path
(`expected.json` `inputs`). So "unresolvable" means *the live read set no longer
names it*, not that the file is gone — a file-existence check would not detect
this class, which is why the diagnostic must name the path and the read-set
relation, not a missing file. O10 also names my S02-F1 and L-list at
`O10-scribe.md` citations (`S02-o-receipt.md:103-131`, `:140-151`) — that peer
reference predates §8.1, so it cites the superseded 17→19 count; §8.1 here is the
correction of record.

### 8.4 S02-F1 is not covered by any O08 leg (gap, filed for the integrator)

O08's O1/O2 exercise the **superseded-member** direction only (a frozen member
missing live). The reverse direction — a **live member the baseline never pinned**,
which replays exit 0 while printing `OK input-digest: 58 read-set digests match the
frozen baseline` when only 57 were compared (§3, experiment A) — has no leg, no
control and no validator anchor in O08. Either the integrator folds the
both-directions membership refusal into the patch (my recommendation, §3) and adds
a control for it, or the validator gains a seventh leg over §3's recipe. Left
silent, the false count at `:3824` stays standing.

### 8.5 Defect filed against S04's machine-readable claim-O leg (not this seat's path to fix)

`reports/round-35/scribe/S04-integration-draft.md:568` carries
`{"id": "O1", "claim": "O", "command": "python3 -B tools/exercise-handoff-e2e.py --selftest", "expect": "exit 0; control count >= 19 (was 17)"}`.
That leg runs the **v1** suite (default `--profile v1`, `:4485`) and would accept
19 controls there, while the same fragment's prose at `:400-406` states the
claim-relevant suite is the **v3** one and that the bare `--selftest` runs a
different, smaller suite — and its own behaviour rows (`:172`, `:174`, `:715-716`)
record 17 controls for that command. As written, the leg is satisfiable without
the v3 controls ever landing (and would fail a correct patch that adds them only
to v3). Correct form per §8.1/§8.2: `command: python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`,
`expect: exit 0; control count >= 41 (was 39)`. S04 is outside this seat's `out`
path, so this is filed here for the integrator, not edited in place.

## Owed

Owed by the integrator at fold time (this revision is not rewritten; the fold is a
new revision). **Landed and folded here:** `op/O08-validation-legs.md`,
`op/O10-scribe.md` (§8).

- `reports/round-35/op/O01-patch-draft.md` — the applied patch bytes and the final
  diagnostic wording/class; without them L1/L2/L2b cannot be re-measured
  post-patch, and O08's O1/O2 regexes stay unpinnable.
- `reports/round-35/op/O02-controls.md` — the two new v3 controls' wording; their
  landing is what moves L2 from 39 to ≥ 41.
- `reports/round-35/op/O03-isolated-verify.md`, `reports/round-35/op/O05-verify.md`,
  `reports/round-35/op/O11-verify-2.md` — the isolated post-patch observations
  (r6 replay exit/code/line, r7 summary, both selftest counts) this receipt's
  after-column must be filled from.
- `reports/round-35/op/O04-regressions.md`, `op/O06-receipt.md`, `op/O07-gap-fill.md`,
  `op/O09-gap-fill.md`, `plan/P02-oa-plan.md`, `scout/K03-keyerror-path.md` — not
  read at this cut; fold any that contradict §2/§3/§5.
- `reports/round-35/review/R04-o-review.md`, `reports/round-35/review/R05-o-review.md`
  — the adversarial passes a "post-review" receipt must fold; `cross/X01`-`X04`
  for trades/conformance.
- `reports/round-35/run-validation.py` — does not exist at this cut; §4 + O08 §6
  are its claim-O spec (O08's O1-O6 is the binding group).
- Decision owed on S02-F1 (§3, §8.4): fold the both-directions membership refusal
  into the patch and add its control, or file it as a routed follow-up with an
  owner.

## Citations

Commands (all run from the repo root or the isolated copy
`.scratch/s02-iso` = `git archive HEAD` at `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`,
with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git rev-parse HEAD`; `git log --oneline -3`; `git status --porcelain`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, KeyError (§2.1)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=45f57132…` (§5)
- `python3 -B tools/exercise-handoff-e2e.py --selftest` → exit 0, `plus 17 controls` (v1 suite, §5, §8.1)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0 after 39.2 s, `plus 39 controls`, 40 bullet lines (§5, §8.1; output `.scratch/s02-selftest-v3-before.txt`)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline scratch-baseline-A.json` → exit 0 with `OK input-digest: 58 read-set digests match the frozen baseline` (§3)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline scratch-baseline-B.json` → exit 1, KeyError at `:3822` (§3)
- `python3 -B -c` module import: `V3_READ_SET` vs `expected.json` `inputs` set diff (§2.2)
- `sha256sum tools/exercise-handoff-e2e.py reports/round-34/handoff/declared-in-r7/*`; `sha256sum reports/round-30/handoff/declared-in-r6/run.log` (§6)
- `git ls-files reports/round-30/handoff/declared-in-r6/ reports/round-34/handoff/declared-in-r7/`; `git check-ignore -v …/run.log`; `cat .gitignore` (§1, §6)
- `diff -rq .scratch/s02-iso .scratch/s02-iso2` (§1)
- `grep -rn exercise-handoff-e2e reports/round-34/handoff/declared-in-r7/ reports/round-30/handoff/declared-in-r6/` (§6)

Files:

- `tools/exercise-handoff-e2e.py:89-93` (exit-code/no-traceback contract), `:93-94` (write surface), `:184` (`CLAIMS_MAP`), `:134-140`,`:180`,`:462`,`:1935` (read-set construction), `:1933-1934` (`V3_BASELINE_DEFAULT`, `V3_FROZEN_DIR_DEFAULT`), `:3819-3824` (drift leg), `:4154` (`v3_selftest`), `:4412`,`:4422`,`:4430`,`:4438`,`:4449`,`:4457` (controls), `:4461-4466` (selftest count line)
- `reports/round-35/claims.json` (claim O: before/after_required/counting_commands/thresholds)
- `reports/round-35/targets.json` (S02 mission + `shared_rules`)
- `reports/round-34/handoff/declared-in-r7/{expected.json,freeze.txt,packet.md,twin.json,claims-map.md}`
- `reports/round-30/handoff/declared-in-r6/{expected.json,freeze.txt,packet.md,twin.json}`
- `reports/round-34/handoff/repin.json`; `LOG.md:3612`, `LOG.md:3630`; `SCORECARD.md:615`
- `.gitignore:3`
- `reports/round-35/op/O08-validation-legs.md` (legs O1-O6, exit-code policy §4, selftest counts §5, static fences O5/O6 — folded in §8.2, §8.4)
- `reports/round-35/op/O10-scribe.md` (independent before-state reproduction, v1/v3 selftest table, round-20 map on disk — folded in §8.3)
- `reports/round-20/handoff/claims-map.md` (24,888 bytes, sha256 `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8` = the r6 baseline's frozen digest for that path; §8.3)
- `tools/exercise-handoff-e2e.py:4485` (`--profile` default `v1`), `:1635`/`:1785` (`v1_selftest` + print), `:1745`,`:1755`,`:1763`,`:1774`,`:1782` (v1 controls), `:4487` (`--selftest`), `:4564` (v3 selftest dispatch)
- scratch (this seat, not durable evidence of the round): `.scratch/s02-iso/`, `.scratch/s02-iso2/`, `.scratch/s02-iso/scratch-baseline-{A,B}.json`, `.scratch/s02-selftest-before.txt`, `.scratch/s02-selftest-v3-before.txt`, `.scratch/s02-r7-before.txt`
