- Seat: S01 | scribe | claim cross | date 2026-10-19 | baseline 9bccc9b

# S01 — round-38 integration dossier: fleet-report material, validation-leg spec, selftest list

**Mission (binding, `reports/round-38/targets.json:209-214`):** *"Integration dossier: fleet-report
material + validation-leg spec + selftest list."* Out path: this file only.

**Status: DRAFT — integration material, not a fleet report, not a validation receipt, not an
acceptance verdict.** Every number below was measured by this seat at the revision and in the
window named in §1 unless it is explicitly attributed to a sibling fragment. Nothing in this file
asserts promotion, canon, clearance or closure; those tokens appear only as negations, as routed
references, or inside quoted scanner patterns (§10).

**Seat context.** This seat is one of the 10 seats the round's single 32-seat batch did not deliver
before the wave was interrupted (§2.4). It is a **completion seat**: the same round, the same
declared claims, the same out path. Its dependency fragments were read from the landed set (K01,
P01, D02–D10b, O04/O05/O07, A01–A03, R01–R03, X02, S02); §11 attributes each folded finding.

---

## §0 — The headline the integrator must read first

**At this seat's cut, not one byte of either declared claim has landed.** `git status --porcelain
-uall` returns 26 rows, **all** of them `?? reports/round-38/…`; `git diff --name-status 9bccc9b`
is empty. So:

| claim | what exists | what does not exist |
|---|---|---|
| **D** (depth) | four independent fenced patch drafts (P01 §3.4; D02 §4; D08 §2.1/§4.2; D10b §4), one isolated apply-and-verify of the planner's draft (D03 §3), two verifier harnesses (D05, D06), a receipt (D07) and a third verifier that found the consumer hole (D10b) | any modified `tools/`, `examples/` or `expected/` byte; the F-6 counters; the RL-8 era leg; the new `expected/register-law-gate/<new>/` baseline |
| **O** (operability) | the fix route documented and priced (O04 §4–§5), independently verified with two defects found (O05 §2–§3), an adversarial review that falsifies the guard's naive shape (R02 F2/F3) and the blocking source-of-truth finding (R03-C1) | any renderer guard; any selftest control; any read-set or manifest change; any freeze byte moved |

Consequences this dossier carries into the leg spec rather than papering over:

1. **Both claims' `after_required` is unreachable at my cut** — the D and O artifacts are drafts,
   and live-tool/example changes are integrator-applied by the round's shared rule
   (`targets.json:6`). A round-38 runner that measures the live tree today measures the *before*
   state for every claim leg.
2. **Both claims' threshold command does not exist.** `ls reports/round-38/run-validation.py` →
   *No such file or directory*; `ls reports/round-38/validation.json` → the same. So claim D's third
   counting command (`claims.json:17`) and both claims' second threshold command
   (`claims.json:23`) are `to-verify` at my cut, and this dossier is a **specification** the
   integrator implements, not a runner this seat ran (§6).
3. **Both claims' acceptance shapes are satisfiable in letter and false in substance as drafted**,
   and three seats say so independently: the RL-8 era leg reads green on a tampered packet today
   (D07 §4.2, D05 §3 C3, K01 §5.3), the F-6 counters have no reader (D10b §2–§3, K01 §3.1), the
   O claim's "r7 sha unchanged" is *already true* (X02 §3), and the O claim's "only the r7 row
   names" is false — r6 names too (X02 §4a, A02 F-A02-3). §7 turns each into a leg with a
   non-vacuous test.
4. **The D block's law-gate leg is not chain-neutral.** Applying the RL-8 draft to
   `tools/gates/register-law-gate.py` reds a filed battery pin (`gate_sha256 15f8b232…`) until a
   **new** baseline id is filed beside `r30-post` — measured three times independently (A01 §3a,
   D04 §4, D08 §4.5, D02 §3.5). Claim D's `after_required` (*"filed bytes untouched except the two
   named tool/example artifacts"*) does not size that cost. §8 lists the owed row.

---

## §1 — Window, state pins, and what "first-hand" means here

| pin | value | command |
|---|---|---|
| lane root | `/home/vgpnk/Projects/shokunin/kotodama-shokunin` | — |
| baseline | `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` | `git rev-parse HEAD`; `git rev-parse 9bccc9b` |
| tracked cleanliness | **empty** — zero modified tracked bytes | `git diff --name-status 9bccc9b` |
| untracked scope | **26 rows** at the pre-write census, all `?? reports/round-38/…`; **27** after this file was written (the new row is this file) | `git status --porcelain -uall \| wc -l` |
| observation window | `2026-10-19T11:14:34Z`–`2026-10-19T11:20Z` | `date -u +%FT%TZ` |
| interpreter | Python **3.14.7** | `python3 -V` |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` | before every python invocation |

Every command in §1–§5 was run by this seat in that window from the lane root. No
`reports/round-*/run-validation.py` was executed anywhere — in-tree or in a copy (F-C13-1,
`targets.json:8`) — no `--freeze` was issued against `reports/round-34/handoff/declared-in-r7`, and
no git-mutating command was run. All mutation-free: this seat's gates and selftests are read-only
or write only into their own temporary mirrors (verified by the digest sweep in §3.4).

**Digests this dossier binds to** (measured at `9bccc9b`, lane root):

```
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d  tools/gates/typed-pipelines.json
943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2  tools/assemble-culture-d4.py
92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0  tools/assemble-d4-typed.py
45ff6f202a56704209144a6f5031a8c2f44a6dfd6ecd3d608cf26db8f793615d  reports/round-38/claims.json
fe3091b91623f47211d673070f7c3d9fac3711c1375361cd27de246c10f7c601  reports/round-38/targets.json
7112af756da589ea359111feb5b2e9ef4b5266566672e16d4e46c2fca8f4599f  reports/round-38/telemetry/dispatch-declared.json
531b2dfa3b619dbba054098f27ed3335f24314ac6aca2288741c46106eb601eb  reports/round-38/telemetry/availability-attempt-1.json
```

The two declaration digests equal `dispatch-declared.json` `durable_sources` (`45ff6f20…`,
`fe3091b9…`) — **cross-check PASS**, the filed declaration is bound to the same bytes this seat
read. They also equal the values S02 measured independently (`S02 §1`).

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, and never clearance.

---

## §2 — Declaration facts, measured

### §2.1 Schema and identity

`claims.json` carries exactly these 12 keys: `round`, `regimen`, `loop`, `position`,
`declared_at_utc`, `baseline_commit`, `dispatch`, `axes_in_play`, `lowest_axis_reasoning`,
`freshness_pause_in_force`, `claims`, `non_goals`. **There is no `baseline_expanded` key** — so the
r36 Trap 1 (declared "expansion" that is the short token) does **not** repeat; the r38 runner must
not assert a 40-hex declared expansion. The declared token is `9bccc9b` (`:7`) and resolves to the
live HEAD (§1).

`axes_in_play` is `["depth", "operability"]` and the two claim objects are exactly
`{D: depth, O: operability}` — distinct axes, and the round's lowest-axis reasoning is filed at
`claims.json:10`. `freshness_pause_in_force: true` (`:11`) and `non_goals[0]` is *"no freshness
axis-move"* (`:26`).

### §2.2 Seat census (reported as a measurement, never as launches)

```
seat_count 32   rows 32   unique ids 32   unique out paths 32   duplicates []
claims {D: 13, O: 10, cross: 6, A: 3}
roles  {executor: 12, verifier: 7, scribe: 4, reviewer: 3, scout: 2, critic: 2, planner: 1, connector: 1}
dirs   {depth: 10, op: 8, cross: 3, adj: 3, review: 3, scout: 2, scribe: 2, plan: 1}
```

### §2.3 F-S01-1 — the seat list carries a claim id `claims.json` does not declare

`targets.json` assigns `claim: "A"` to three seats (A01/A02/A03, `:152-172`) while `claims.json`
declares only `{D, O}` and lists `axes_in_play` without adjacency. This is a **declaration-form
gap**, not a seat-count defect (32 == 32) and not an out-of-lane write. Independently found by
three seats: this seat's census, `A02 §5 F-A02-1`, `A01 §5`, and `S02 §2 F2` (which notes r38 is
the first regimen-2 round with this shape).

**Disposition: routed, not absorbed.** The round-38 runner must record it — a `CO` leg that
*asserts the partition against `claims.json`* would fail a well-formed round, so the leg must
**report the census and name the difference**, and the integrator must either file the A block as
unadjudicated adjacency work or have the runner assert it and fail. The one thing the record must
not do is silently accept a superset as if it were declared.

### §2.4 F-S01-2 — no declared fallback, and the devin re-dispatch is a named deviation

`REGIMEN.md:16` (schedule row 6) is the one row in the table with **no fallback clause**; row 4
alone carries *"fallback devin/deepseek-v4-1-flash-high"* (`REGIMEN.md:14`). `claims.json:8` and
`telemetry/dispatch-declared.json:6-11` declare `xai-oauth / grok-4.7-fast` / 32 requested / 1
batched call and **no fallback key**.

`telemetry/availability-attempt-1.json` records **32 requested / 0 launched / 0 completed / 32
failed** with `failure_class` *"403 out of credits (grok.com)"* and `failure_basis` naming
`agent-516..agent-547`, and dispositions the re-dispatch onto `devin/deepseek-v4-1-flash-high` as a
**NAMED DEVIATION** with owner and reason (`:13`), not as a REGIMEN-authorized fallback.

**Consequences for the runner and the report.**

- The observed route (devin) and the declared allocation (xai-oauth) stay **separate fields**;
  the 32 grok launch failures must not be netted against any devin completions, and no sentence may
  read as though a fallback had been declared.
- The devin batch's own counters (launched / completed / failed / window / actual route) are
  **unknown to this seat** and no fleet round-38 directory exists to hold a native extract — so
  they are `null` with owner `orchestrator (goal-mode parent)` and a reason, never inferred zeroes
  and never a claimed completion rate (`AGENTS.md:15-31`; `S02` `to-verify`).
- `REGIMEN.md:73-75` binds if the devin batch also failed: apply the declared fallback once, else
  file `could-not-dispatch` with owner + reason, and stop after three consecutive such rounds. The
  round-38 runner cannot decide this; it must record whichever state it finds.

### §2.5 The wave's own completeness — 10 declared outputs absent

At my cut `reports/round-38/` holds 26 files: the two declarations, two telemetry records, and 22
landed seat fragments. The declared outputs still absent are:

```
cross/X00-connector.md        op/O01-guard-design.md      op/O02-isolated.md
op/O03-verify.md              op/O06-receipt.md           op/O08-regression.md
scout/K02-roster-guard.md     depth/D01-f6-design.md      cross/X01-trades.md
scribe/S01-integration-draft.md   ← this file (absent before this write)
```

**Recompute, never trust this list** (§12.1). The absence of `depth/D01-f6-design.md` and
`op/O01-guard-design.md` is load-bearing: D03's mission named D01/D02 as its inputs and it never
received them (`D03 §0`), and R03-C1's blocking finding cannot be verified against an O01 draft
that does not exist (`R03 ## Owed`).

---

## §3 — Landed-fragment cross-check: the measurements every block agrees on

Three or more seats reached these without coordinating. They are the round's **premises**, and the
runner's regression floor should assert them.

### §3.1 The three register legs, live

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6
          violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0

$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3
          force_failures=0 consequence_failures=0 dangling=0 findings=0
exit=0

$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
… 12 × FINDING D2L-FORM-UNRESOLVED (GAR-01..06 / LEX-GAR-01..06)
ok   L3b-argot … ok L4-pins
summary: 20/20 legs passed
exit=0
```

Agrees with `K01 §4.3`, `P01 §4.1`, `D03 §3.1`, `D07 §3.2`, `R03 §1`. The typed gate's own
selftest is `19/19` and it reports its pins inline (`projection c23b0ab5…`, `expected e6ae9828…`,
`profile 76ecdfdc…`, `assembler 943f487b…`, `adapter 92f5460b…`).

### §3.2 The frozen r7 pair is byte-unchanged

```
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
```

`45f57132…` is exactly claim O's acceptance threshold (`claims.json:24`). The default v3 chain
re-renders it and exits 0 with **no tree write**:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
            statuses=16/7/4 v2_subset=equal alias_leg=landed
            packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

Agrees with `A02 §3`, `D03 §3.1` (row 7), `R03 §1`, `X02 §3`.

### §3.3 The gate battery and the four selftests

```
$ python3 -B tools/check-gate-battery.py
summary: {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}
originals: {"added": 0, "deleted": 0, "modified": 0, "preserved": true, files_hashed 33}

$ python3 -B tools/gates/argot-derivation-gate.py --selftest   → selftest: 27/27 checks passed
$ python3 -B tools/gates/register-law-gate.py --selftest      → selftest: 45/45 checks passed
$ python3 -B tools/gates/typed-pipeline-gate.py --selftest    → selftest: 19/19 checks passed
$ python3 -B tools/assemble-culture-d4.py --selftest          → selftest: 81/81 checks passed
```

### §3.4 The filed receipts are clean, and the runner census is a revision boundary

The authoritative filed-byte check is a **per-file digest sweep**, not a git pathspec — the filed
runners' own `git status -- 'reports/round-1..N'` scope line is a **dead check** because git treats
that as a literal path (F-S01-2 of `reports/round-36/scribe/S01-integration-draft.md §0.2`). This
seat ran the sound form:

```
$ for f in $(git ls-files 'reports/round-*/validation.json'); do
    L=$(sha256sum "$f" | cut -d' ' -f1); H=$(git show "HEAD:$f" | sha256sum | cut -d' ' -f1)
    [ "$L" != "$H" ] && echo "DRIFT $f"; done
(no output — zero drift across every filed receipt)

$ ls reports/round-*/run-validation.py | wc -l
32        # r5..r37, minus the never-dispatched r13
```

Adding round 38 makes the census **33**, which reddens any filed runner that pins its own census
constant — the r34 runner pins `{"guarded-refresh": 18, …}` and `len(runners) != 29`
(`reports/round-34/run-validation.py:209-211`) and already reds at 30. That is a **revision
boundary**, not a filing error: the runner must read a filed receipt's **digest**, never its
re-computed verdict.

---

## §4 — Fleet-report draft for `.ufo/reports/round-38/kotodama.md`

The fleet root is `/home/vgpnk/Projects/shokunin/.ufo/`; `ls .ufo/reports/round-38/` → *No such
file or directory*, so the report is **parent-owed** (`S02 F9`). The lane repo contains no `.ufo`
directory at all. The four required headings are the tuple the filed runners use
(`reports/round-37/run-validation.py` `SECTIONS`; `reports/round-36/run-validation.py:319`), and
they match the landed `reports/round-37/kotodama.md`. Use them **verbatim**.

### Draft header

```text
# kotodama — round 38 report (2026-10-19)

Regimen 2 (`REGIMEN.md:16`), loop 1, position 6 — the xai-oauth build round. Declared
allocation `xai-oauth / grok-4.7-fast` (xhigh), 32 requested workers, one batched
AgentSwarm (`claims.json:8`; `telemetry/dispatch-declared.json:6-11`).
**Observed route (named deviation, not a declared fallback):** the grok lane returned
`403 out of credits` at launch for **all 32 seats with zero started** —
`telemetry/availability-attempt-1.json:7-13` records requested 32 / launched 0 /
completed 0 / failed 32 (`agent-516..agent-547`). `REGIMEN.md:16` carries **no**
fallback clause (unlike row 4 at `:14`), so the re-dispatch onto
`devin/deepseek-v4-1-flash-high` is filed as a named deviation with owner
`orchestrator (goal-mode parent)`. The batch was then interrupted: **22 of 32 declared
seat outputs landed** before the wave stopped, and 10 were re-dispatched as completion
seats — this report's own seat (S01) is one of them. Declared baseline `9bccc9b`
(`claims.json:7`) = `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`.
Claims D/O on depth/operability (`claims.json:13-24`); freshness axis-move claims stay
paused (`claims.json:11`). Seat accounting: `seat_count: 32`, 32 rows, 32 unique `out`
paths (measured §2.2 of `scribe/S01-integration-draft.md`); the census carries an
**undeclared `A` block** (3 seats) that `claims.json` does not declare — filed as a
declaration-form difference, not a seat-count defect.
Dispatch honesty: allocation declared and digest-pinned; observed launches/completions/
failures for the devin batch are `null` with owner + reason, and the closing snapshot is
owed once `validation.json` lands (`AGENTS.md:32-39`).
```

### Draft — Work performed

```text
- **Depth (claim D):** the declared target is the r36 register residue, correctly
  claimed — (a) the F-6 `derived_forms`/`derived_ok` counters, (b) the RL-8 era leg.
  Measured before-state at `9bccc9b`: `grep -rl "derived_forms\|derived_ok" examples
  tools` → **no match**; `grep -c "D4L-ERA"` over the law gate → **0**; and the gap is
  *demonstrated*, not quoted — an L-55 `stage: "E1"`→`"E0"` tamper (the defect the
  packet's own RGL-05 text calls *"a defect"*, `examples/culture-d4/packet.d4.yml:2863`)
  produces **no finding from either gate** (`violations=0`, `findings=0`, both exit 0).
  The block converged on **P01's §3.4 fenced draft** and verified it in isolation:
  `derived_forms=8 derived_ok=8` (non-vacuous — 8 real stamp forms), the C-E1 control
  fires with exactly 8 era findings, the loan-layer false-red trap is reproduced and
  scoped away, and **every pin surface stays green** (`battery_exit 0`, typed `20/20`,
  v3 exit 0 packet `45f57132…`, r31-post `REPLAY OK 4/4`). Three hazards were named
  rather than smoothed: a key-only emitter has **no reader** (D10b C2/C3), a C1-shaped
  era control would pass vacuously (D05 §3), and the law-gate host reds a filed battery
  pin (A01 §3a, D04 §4, D08 §4.5, D02 §3.5). **Nothing landed under this claim** — all
  artifacts are drafts, and live tool changes are integrator-applied.
- **Operability (claim O):** the declared target is the r37-adjudicated read-set roster
  defect. Measured: `D4_COMPONENTS` is a **12**-tuple (`tools/exercise-handoff-e2e.py:157-170`)
  while the packet manifest records **13** component digests and the r7 `expected.json`
  `inputs` map holds 12 D4 components with `13-register-law.yml` absent. The block found
  the defect is **not r7-only** (r6 carries the same 13-vs-12 asymmetry; X02 §4a,
  A02 F-A02-3) and that a naive guard is a **false-red machine**: a global
  manifest-vs-read-set guard reddens the chain with **7** named rows (6 legitimate D2
  members + the one D4 member), while the D4-scoped **record-only** variant names exactly
  `13-register-law.yml` and keeps the r7 chain at exit 0 (R02 F2/F3). The fix route is a
  **successor baseline**, not a documentation tweak: adding the member moves the assembled
  packet (`45f57132…` → `7ca92109…` tail-insert / `b102aa70…` paired-move) and reds the
  filed r7 row by digest (O04 §2, R02 F4). **Nothing landed under this claim.**
- **Adjacency (claim A — undeclared):** the A block ran as a watch, not as a declared
  axis-move. It measured the round's blast radius (a law-gate edit reds `r30-post`; an
  argot-gate edit is pin-neutral; a read-set add reds the r7 chain), filed the
  *"two named tool/example artifacts"* ambiguity as an unbound declaration, and confirmed
  the round's scope is clean. Whether this block is a watch posture or an undeclared claim
  is the integrator's/operator's call.
```

### Draft — Landed changes

```text
- **No claim artifact landed.** `git diff --name-status 9bccc9b` → empty; all 26 rows of
  `git status --porcelain -uall` are `?? reports/round-38/…`. The D and O deliverables
  exist only as fenced drafts in the round's own fragments.
- The round's **evidence artifacts** (22 landed seat fragments plus this dossier) are
  `reports/round-38/{scout,plan,depth,op,adj,review,cross,scribe}/…` — evidence, not
  product changes. Do not read them as landed bytes.
- If the integrator applies the drafts, the landed set is: `tools/gates/argot-derivation-gate.py`
  (F-6 route A) and/or `tools/d2-typed-labels.py` + `examples/culture-d4/typed-labels.d4.yml`
  + `examples/culture-d4/expected-holds.json` + `examples/culture-d4/packet.d4.typed.yml` +
  `tools/gates/typed-pipelines.json` (F-6 route B), plus `tools/gates/register-law-gate.py`
  and a **new** `tools/gates/expected/register-law-gate/<new-id>/` baseline (RL-8), plus the
  renderer guard in `tools/exercise-handoff-e2e.py` (O). The route choice and the artifact
  roster are the integrator's; the prices are measured in §8.
- Filed bytes: **unchanged**. The r7 pair is byte-identical (`45f57132…` / `0e229138…` /
  `bbe15887…`), zero receipt drift across every filed `validation.json`, and no freeze was
  issued. `corpus/README.md` carries a **live duplicate H1** at `:1` and `:3` (measured;
  A01 §5, A02 F-A02-2) — routed, not absorbed, and not this round's to edit.
```

### Draft — Before → after measurements

Fill from §7's leg table. Rule: every after-value names the fragment that measured it and the
counting command; every before-value below was measured by this seat and is reproducible from §3
and §12.

| axis | before (measured by this seat at `9bccc9b`) | after required (`claims.json`) | status at my cut |
|---|---|---|---|
| depth (D) | no `derived_forms`/`derived_ok` anywhere in `examples/`+`tools/`; no `D4L-ERA` in the law gate; both gaps *demonstrated* by a silent tamper | counters emit and are counted; the era leg runs; argot/law/typed legs green with the new coverage named (no vacuous-pass); pins as new rows | **not landed** — drafts only |
| operability (O) | r7 read set omits `13-register-law.yml` while the packet manifest records 13; `D4_COMPONENTS` is a 12-tuple; nothing detects the class | a selftest-controlled guard names the disagreement (≥2 controls); r7 default chain exits 0 unchanged; the fix route documented; zero freeze bytes moved | **not landed** — drafts only |
| cross | `run-validation.py` absent; 10 declared outputs absent; fleet report / MANIFEST row / LOG entry / SCORECARD row absent; observed-dispatch and closing snapshot owed | runner + receipt; report with 4 headings; MANIFEST/SCORECARD/LOG rows; telemetry closed by a digest-pinned snapshot | **owed** (§8, §9) |

### Draft — SHONEN

```text
No SHONEN box was re-surveyed by this round, and no fragment in this round establishes a
new end-to-end domain-task result. Carry the prior status only as *last recorded*, not as
a round-38 re-verification: `reports/round-36/scribe/S01-integration-draft.md:248-267`
records boxes 1–4 as `verified-with-conditions`, with the box-1 citation conditions, the
box-2 D4 garment/RL-3/head2 debts, the box-3 N1/N4/N5/N7 items and the box-4 standing
readings still noted. Round-38 findings do not alter those records. No promotion decision
is taken or implied; the decision remains operator-owned (`SHONEN.md:10-11`).
```

---

## §5 — The round-38 runner: constants that must NOT be inherited

Cloning `reports/round-37/run-validation.py` verbatim produces a runner that fails a well-formed
round. Every r37 constant that is wrong for r38, with the measured replacement:

| r37 constant / path | r37 value | round-38 value | evidence |
|---|---|---|---|
| `ROUND` | `reports/round-37` | `reports/round-38` | — |
| `COMMAND` | `python3 reports/round-37/run-validation.py` | `python3 reports/round-38/run-validation.py` | `claims.json:17,23` |
| `BASELINE` | `57c8409` | `9bccc9b` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` | §1 |
| seat count | 64 | **32** | `targets.json:3`, measured §2.2 |
| `claims_declared` | `{Ca, O, A}` | `{D: depth, O: operability}` | `claims.json:13-24` |
| calibration input | `calib/recount-ledger.json` (rows ≥ 30) | **absent — r38 is a build round, no `calib/` dir** | `ls reports/round-38/` |
| operability input | `op/defect-queue.json` | **absent** | same |
| fleet report path | `…/.ufo/reports/round-37/kotodama.md` | `…/.ufo/reports/round-38/kotodama.md` | `ls` → No such file |
| closing snapshot | `availability-close-37.json` | `availability-close-38.json` | `AGENTS.md:32-39` |
| `ROOT` | **absolute literal** + `os.chdir(ROOT)` | **relative** — `Path(__file__).resolve().parents[2]` | see below |

**The `ROOT` line is the load-bearing one.** `reports/round-34/run-validation.py:10` and
`reports/round-35/run-validation.py:9` hardcode the live tree and `os.chdir(ROOT)`, which is why a
seat that ran them from inside a `git archive` copy still wrote the **live** receipt — the
conformance incident recorded at `reports/round-36/scribe/S01-integration-draft.md §0.2` and still
open as defect `O12`. `reports/round-33/run-validation.py:23` uses
`ROOT = Path(__file__).resolve().parents[2]` and is immune. **Round 38 must copy the r33 shape**,
so that the "never run in-tree (F-C13-1); isolated `git archive` copies only" rule is mechanically
enforceable rather than a promise.

---

## §6 — Validation-leg spec (machine-checkable)

Format: `id | claim | command/check | expected | parser hint`. `{{}}` = resolve from the landed
fragment and pin the path. Every leg is written so that it is **true and useful whether or not the
integrator applies the drafts** — where the after-state does not exist, the leg records
`could-not-evaluate` rather than passing.

### §6.1 Coherence / schema / declaration legs (cross)

| ID | check | expected |
|---|---|---|
| **CO1** | strict-parse `claims.json`, `targets.json`, `telemetry/dispatch-declared.json` (duplicate keys refused); `round == 38` in all three; `baseline_commit == "9bccc9b"`; `git rev-parse --verify 9bccc9b^{commit}` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; record the declared token and the resolved id **separately** | pass |
| **CO2** | `{c.id: c.axis}` == `{"D": "depth", "O": "operability"}`; `set(axes_in_play) == {"depth","operability"}`; axes distinct; `freshness_pause_in_force is True`; `"freshness"` absent from every claim axis | pass |
| **CO3** | seat census: `len(seats) == 32 == seat_count`; 32 unique ids; 32 unique `out` paths, all under `reports/round-38/`; every `id`/`role`/`mission` non-empty. **Report** `{claims: {D 13, O 10, cross 6, A 3}}` and the role/dir vectors as the measurement | pass |
| **CO4** | **the undeclared `A` block** (§2.3): compare the seat `claim` census against `claims.json.claims`. Do **not** assert equality — **record** the difference with the A-seat ids and route it to the integrator | pass-with-named-difference |
| **CO5** | dispatch shape: assert the **declared** allocation exactly (`xai-oauth`, `grok-4.7-fast`, 32 requested, 1 batched call) across `claims.json` and `dispatch-declared.json`. Then assert that **no fallback key exists** in either and that `REGIMEN.md:16` carries no fallback clause — i.e. assert the *absence* of a declared fallback | pass |
| **CO6** | route deviation: read `availability-attempt-1.json`; assert requested 32 / launched 0 / completed 0 / failed 32 and `failure_class` contains `403`. Record the observed route (`devin/deepseek-v4-1-flash-high`) as a **named deviation** with owner `orchestrator` — never as a declared fallback, never as a leg failure, never netted against completions | pass-with-deviation |
| **CO7** | the devin batch's own counters: if no durable native extract exists, record each of launched/completed/failed/window/actual-route as `null` with owner and reason. **Never infer zero, never infer 32** | could-not-evaluate |
| **CO8** | protected-tree census: enumerate with `git ls-tree -r --name-only <BASELINE>` and a regex walk (`reports/round-(?:[1-9]\|[12][0-9]\|3[0-7])/`, `corpus/lessons/(?!README)`, `tools/gates/frozen/round-`), comparing live bytes to `git show <BASELINE>:<path>` digests. **Never** a literal `reports/round-1..37` pathspec | pass |
| **CO9** | runner census / revision boundary: `ls reports/round-*/run-validation.py \| wc -l` — record the count and the digest of every filed `reports/round-*/validation.json`. Assert **digests**, never a re-computed verdict; a count change is a revision boundary, not a failure | pass |
| **CO10** | godspeed lead: **not machine-checkable from durable artifacts** — prompts are not persisted and `AGENTS.md:30-31` forbids private prompt payloads in telemetry. Record `could-not-evaluate` with owner `orchestrator` and `dispatch-declared.json` as the only evidence. Never score this leg as passed from absence of evidence | could-not-evaluate |
| **CO11** | regression floor: the seven non-mutating tools of §3.3 all exit 0 with the recorded counts, and the receipt digests are unmoved across the run | pass |

### §6.2 Claim-D legs (depth: the register residue)

| ID | check | expected |
|---|---|---|
| **D1** | **before-state** (binding): `grep -rl "derived_forms\|derived_ok" examples tools` → no match (exit 1); `grep -c "D4L-ERA" tools/gates/register-law-gate.py` → 0. Record both as the *before* measurement so the delta is visible | pass |
| **D2** | the three register legs green at the measured revision: argot `derived_pairs=8 violations=0` exit 0; law `findings=0 dangling=0` exit 0; typed `summary: 20/20 legs passed` exit 0 | pass |
| **D3** | **F-6 after-state, both halves.** (a) *emitter*: the two counters appear on whatever surface the integrator chose, and the values are non-vacuous (`derived_forms > 0`). (b) *consumer*: a named leg reads them and goes **red** when they disagree — the D10b hole. A key-only emitter **fails** this leg; record the consumer's path and the disagreeing-value control | pass / failed |
| **D4** | **RL-8 after-state.** The era leg runs **and** an **E0-stamp control** fires with a named finding and non-zero exit. The control must be **C4-shaped** (an E0 stamp form with the construction's own `available_from` widened to E0), not C1-shaped — because `tools/gates/lexicon-coverage-audit.py` already fires `D-stage-mismatch` on the C1 shape, so a C1 control would pass vacuously against work already done (`D05 §3`) | pass / failed |
| **D5** | **the era leg's domain is *forms*, not law rows.** The delivered packet carries ~20 rows with `register: "stamp"` (8 lexicon + 7 QREG + 5 RGL); an era leg that grades all of them emits false reds on the clean packet. Assert the delivered packet yields **0** era findings and that the control yields exactly **8** (`D02 §5` controls 16/18–22; `P01 §3.3`) | pass |
| **D6** | **pin cascade, by route.** F-6 route A (argot gate) → **zero** pin rows move; F-6 route B (projector) → **five** live rows move (`typed-pipelines.json profiles[0]`, `expected-holds.json`, the r22-post baseline, the r7 read set ×3 members) plus a D2 baseline-digest selftest control; RL-8 → **exactly one** new baseline id. Assert the route was **named**, and that `r30-post` was not rewritten in place | pass |
| **D7** | the r7 packet pin is unchanged: `sha256sum reports/round-34/handoff/declared-in-r7/packet.md` → `45f57132…`, and `--profile v3 --quiet` exits 0 | pass |
| **D8** | **two independent verifiers.** Assert the number of *independent* verifier fragments whose evidence was on disk when they ran, and name them. `D05 §0` and `R01 ## Owed` record that D03 was **absent** at their sample; `D03 §0` records that D01/D02 never landed. A "two verifiers" claim built from fragments that could not see their input is **not** met — record the actual pairing | pass / to-verify |

### §6.3 Claim-O legs (operability: the roster guard)

| ID | check | expected |
|---|---|---|
| **O1** | **the guard landed with ≥2 selftest controls** (claim's own threshold): (a) *manifest-member-not-in-readset named*, (b) *in-sync green*. Both controls must assert on the guard's **own record/diagnostic channel**, not on the exit code — a refuse-in-`v3_preflight` guard is **green on the r7 row** (measured, `R03 §5`), so an exit-code control cannot observe the "named" half | pass / failed |
| **O2** | **guard direction**: live manifest members **∖** frozen `inputs`. The existing guard is one-directional — it iterates `baseline["inputs"]` and names members missing from the *live* read set (`tools/exercise-handoff-e2e.py:3823-3836`, `E2E-READSET`), so a live-only 13th member is invisible to it (`A01 §3d`, `R03 §2.2`) | pass |
| **O3** | **guard source of truth** (R03-C1, **blocking**): the guard must read the **source packet's** `assembly.source_sha256`-derived component manifest (`v3_mine_d4`, `tools/exercise-handoff-e2e.py:2045-2056`, which mines **13**), **not** the rendered `reports/round-34/handoff/declared-in-r7/packet.md`, whose markdown table carries only **12** D4 rows. A guard parsing the rendered text passes on the r7 row forever — a false green | pass / failed |
| **O4** | **the guard must not refuse**: r7 default chain exits 0 with `packet_sha256=45f57132…`. The D4-scoped record-only variant satisfies this; the raising variant fails it **and** breaks the renderer's own positive selftest (`R02 F3`) | pass / failed |
| **O5** | **correct the O08 expectation**: the mission's *"only the r7 row names; others stay green"* is **false as written** — r6 carries the same 13-vs-12 asymmetry (`X02 §4a`, reproduced by `A02 F-A02-3`). Assert the corrected form: **r6 and r7 name; r2/r5/`declared-in` stay green**. A guard narrowed until it misses r6 is vacuous on the class the claim exists to catch | pass-with-corrected-expectation |
| **O6** | **ordering against the supersession abort**: isolation runs against r2/r5/r6 abort at `E2E-READSET` (`reports/round-20/handoff/claims-map.md`) **before** any later-added manifest check is reached (`X02 §4b`). The guard must run before the supersession check, or the sweep must bypass the abort — otherwise O08's r2/r5/r6 replays report `E2E-READSET`, not a manifest verdict | pass / to-verify |
| **O7** | **r7 packet sha unchanged** — assert it, and record that it is **already true at baseline**, so it is a **regression guard, not evidence the guard landed** (`X02 §3`) | pass (regression only) |
| **O8** | **zero freeze bytes moved**: `reports/round-34/handoff/declared-in-r7/**` byte-identical; no `--freeze` issued. Record the three digests | pass |
| **O9** | **fix route documented**: the successor-baseline row exists in the round's record (`O04 §5` draft, `schema: kotodama-pin-repoint-v1`), naming the new row, the 59-member read set, the insertion point (**tail**, zero `A-NN` renumbering) and the fact that the fix moves the packet sha (`45f57132…` → `7ca92109…` tail / `b102aa70…` paired). Assert *documented*, not *applied* | pass |

### §6.4 Cross / close legs

| ID | check | expected |
|---|---|---|
| **X1** | fleet report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-38/kotodama.md` with all four headings verbatim, an ISO date, and a citation of `reports/round-38/run-validation.py`. The report lives **outside** this repo, so the integrator writes it | pass / owed |
| **X2** | MANIFEST: a round-38 entry in the fleet-root `MANIFEST.json` `rounds[]`. Measured at my cut: **0** rows with `lane_rounds.kotodama == 38` (252 rows total, last kotodama rows 35/36/37). Absent → record `pending-by-construction` with the integrator as owner | pass / owed |
| **X3** | telemetry: `dispatch-declared.json` `durable_sources` digests equal the live `claims.json`/`targets.json` bytes (**verified true at my cut**, §1); `observed-dispatch.json` exists **or** is recorded owed with owner + reason; `availability-close-38.json` exists **or** is recorded owed. Never infer missing counters | pass / owed |
| **X4** | receipt self-consistency: `round == 38`, exact `counting_command`, `baseline_revision == "9bccc9b"`, per-claim measurements present, `limits` non-empty, `missing_dependencies` ⊇ `target_outputs`, and `acceptance_checks_passed` true only if every leg is green (no `could-not-evaluate` counted as a pass) | pass |
| **X5** | language scan over every `reports/round-38/**` file: zero unadjudicated grant/completion frames; every declared seat `out` path present in the scan (including absent ones, which the scan must name as absent rather than skip) | pass |
| **X6** | declared-output completeness: `missing_dependencies` == the recomputed absent set (§12.1), and `target_outputs` a subset. An empty `missing_dependencies` over an incomplete wave is the false green this leg exists to catch | pass |
| **X7** | **the two named artifacts are unbound** (`A01 §4`, `A02 F-A02-3`): `claims.json:16` says *"filed bytes untouched except the two named tool/example artifacts"* and **no round-38 byte names which two**. Record the ambiguity and require the integrator to bind it before any draft is applied | to-verify |

---

## §7 — The non-vacuous test each claim must survive

This table is the honesty core of the dossier. Each row is a test that **fails today** and would
**pass only if the claim's substance landed**. Taken from `X02 §5` and extended with the
measurements of §3 and §6.

| # | claim | test that is not vacuous | why a green reading fails today |
|---|---|---|---|
| 1 | D / RL-8 | an E0-dated stamp form (C4-shaped) ⇒ **named era finding, non-zero exit**; the clean packet unchanged | measured silent: both gates `violations=0` / `findings=0` on the tampered packet (`D07 §4.2`, `D05 §3 C3`, `K01 §5.3`) |
| 2 | D / F-6 | a **consumer** goes red when `derived_ok` disagrees with the leg's replay | no consumer reads any derivation counter: `L3b-argot` filters to `FINDING D4L-ARGOT-` only (`tools/gates/typed-pipeline-gate.py:530-539`); a *lying* coverage line leaves `20/20 legs passed` (`D10b C3`) |
| 3 | D / counting | `reports/round-38/run-validation.py` exists and passes **in an isolated copy** | absent at baseline (`ls` → No such file) |
| 4 | O / guard | **r6 and r7 name; r2/r5/`declared-in` green** | "only r7 names" is false — r6 mismatches too (`X02 §4a`) |
| 5 | O / guard | the guard is reachable **despite** the `E2E-READSET` abort on r2/r5/r6 | those rows abort earlier today (`X02 §4b`) |
| 6 | O / sha | r7 `45f57132…` unchanged | already true; a regression guard, not evidence (`X02 §3`) |
| 7 | D / era domain | the delivered packet yields **0** era findings over a **non-empty** domain (8 forms checked) | an era leg scoped by the gate's broader `record_register()` fires **2 false findings** on the clean packet (`L-53 'gal'`, `L-54 'mar'`, `P01 §3.3`) — a landing that gets this wrong is rejected, not accepted |

---

## §8 — Integration order, collisions, and the owed row set

**Ordering (binding).**

1. **Decide the F-6 route first** — it decides whether anything else is pinned. Route A (argot gate)
   moves **zero** rows; route B (projector) moves **five** rows plus a D2 baseline-digest selftest
   control and cannot even re-freeze until that control is repaired (`R03 §4`, `D09 §2.2`).
2. **Land the D bytes before the O guard** if both land. The O guard's *fix* route re-renders the
   packet, so a freeze taken mid-wave is stale the moment the register law lands (`O04 §4`
   sequencing note).
3. **File the new battery baseline as its own row** before landing the law-gate draft — never
   repoint `tools/gates/expected/register-law-gate/r30-post/` (`gate-frozen-run-standard.md:74`;
   `A01 §3a`).
4. Then the runner, the telemetry close, the fleet report, then SCORECARD/LOG/MANIFEST.

**The owed new-row set** (drafted by D04 §4, verified by D06 §5, priced by D02 §6):

| # | surface | action | measured trigger |
|---|---|---|---|
| 1 | `tools/gates/expected/register-law-gate/<new-id>/` | **new** baseline dir (gate sha, fresh `run.log`, recomputed `stdout_sha256`); `r30-post` byte-identical | battery `battery_exit 2`, one `BASELINE-GATE-REVISED` on `r30-post` |
| 2 | `tools/gates/typed-pipelines.json` `profiles[0]` | new generation row if F-6 route B | `L1-profile` red |
| 3 | `examples/culture-d4/expected-holds.json` | `projector_sha256` ×4 + `pin_generations[]` row if route B | `E2E-DIGEST: projector_sha256 2819f687… vs …` |
| 4 | `examples/culture-d4/typed-labels.d4.yml`, `packet.d4.typed.yml` | regenerated if route B | `assemble-d4-typed.py --check` staleness |
| 5 | `reports/round-34/handoff/declared-in-r7/**` | **zero bytes move** | `45f57132…` / `0e229138…` / `bbe15887…` |
| 6 | argot-gate baseline (opt-in) | only if the round wants the F-6 counters **checked** rather than printed — registering the argot gate makes the battery demand a baseline for it (`P01 §4.4`, `D04 §3.1`) | `BASELINE-GATE-UNCOVERED` |

**Collision surface.** The only artifact on both blocks' paths is
`examples/culture-d4/typed-labels.d4.yml` — and only under F-6 route B, which is the route the
round's non-goals make unattractive. Under route A the two claims **share no moving artifact**
(`R03-C4`). No two seats write the same file: the 32 `out` paths partition into 8 directories
(§2.2).

**Routed ambiguities the integrator must decide, not the runner.**

- *"The two named tool/example artifacts"* — unbound (§6.4 X7).
- *The undeclared `A` block* — watch posture or undeclared claim (§2.3).
- *The route adjudication for position 6* — no declared fallback (§2.4).
- *The duplicate H1 in `corpus/README.md`* — a live corpus-surface defect, routed
  (`A01 §5`, `A02 F-A02-2`); the r36 placeholder row is already satisfied (`grep -c
  '__E3_PLACEHOLDER__' corpus/README.md` → 0).
- *The F-6 counter domain* — count the 8 `derivation` records or the 10 `route: derived` records
  (`K01 §2.3`, `K01 §7.1`). The forecast's F-3 names the `derived_from` + `derivation` pair, so 8;
  this is a contract decision, not a measurement.

---

## §9 — Telemetry material (draft pointers, not measurements)

This seat does **not** duplicate S02's work. `reports/round-38/scribe/S02-telemetry-draft.md` owns
the record templates; what the integration dossier needs from it is only the close obligation:

- `telemetry/dispatch-declared.json` is filed and its `durable_sources` digests are **verified live**
  (§1). Its `closing_snapshot` field reads `open-at-seat-close: owed once validation.json lands`.
- **Owed at close** (`AGENTS.md:32-39`): an `observed-dispatch.json` (the devin batch's counters —
  `null` with owner + reason where unobservable) and a closing snapshot
  **`telemetry/availability-close-38.json`**, schema `kotodama-availability-closing-snapshot-v1`,
  naming `closes` = `reports/round-38/telemetry/dispatch-declared.json` and `closes_sha256` = its
  digest **at close time** (`7112af75…` at my cut), with `closed_fields`, `could_not_recover`,
  `sources` and owner. The name `availability-close-38.json` is the landed convention
  (`reports/round-{19,25,26,27,28,33,34,35,36,37}/telemetry/availability-close-N.json`) — **not**
  `closing-snapshot.json`, which exists nowhere in the repo.
- **A round is not admitted to `LOG.md` while its own availability record still owes a closing
  snapshot** (`AGENTS.md`). This is a hard gate on the round, not a formality.
- No credentials, authorization headers or private prompt payloads in telemetry. The only route
  string present in the round's declarations is the lane name `xai-oauth` (`A02 §4` measured 0
  credential hits).

---

## §10 — Language and negation posture (binding on every leg)

No leg, fragment, receipt or report in this round asserts promotion, canon, clearance or closure.
Every occurrence of those tokens must be a **negation**, a **routed reference**, or a **quoted
scanner pattern**. The three legitimate shapes, all present in this file: *"no promotion decision is
taken or implied"* (§4 SHONEN draft), *"canon decisions are lore-shokunin's"*
(`PROVINCE.md:20`), and the quoted scanner regexes (§5, §6.1 CO11). The r34/r35 scanner's frame rule
is the contract: **token presence alone never fires; only grant/completion frames do.**

---

## §11 — Landed-fragment cross-check (folded, attributed)

Every fragment below was read in full by this seat. Where a peer's figure agrees with a
measurement in §3 it is marked *converges*; where a peer went further it is marked *extends*.

**§11.1 — The D residue is real, and the block converged on one landing shape.** `K01 §0` names
four findings the block must not build past (F-6's producer does not belong in the argot gate per
the forecast's own counting command; nothing consumes the counters; the F-6 change costs a
re-pin cascade; RL-8's floor is already machine-readable at `registers.QREG-04.era_rule`
`packet.d4.yml:1366`). `P01 §3.4` turns that into a fenced draft hosted in the **argot** gate;
`D03 §3` applies it verbatim in an isolated copy and measures `derived_forms=8 derived_ok=8`,
`battery_exit 0`, typed `20/20`, v3 exit 0, r31-post `REPLAY OK 4/4` — **converges** with this
seat's §3.1/§3.2. `D02 §2.1` deliberately hosts RL-8 in the **law** gate instead and records the
deviation from the site `rules.md:29` named; `D08 §4` prices the same route. So the block carries
**two** measured routes, not one asserted — and §6.2 D6 requires the integrator to **name** the
chosen one.

**§11.2 — D10b found the hole P01's route leaves open, and it is load-bearing.** `D10b §2–§3`
measures that on **both** routes *"no consumer reads the counters"*: `L3b-argot` reads only
`FINDING D4L-ARGOT-*` lines and the exit code (`tools/gates/typed-pipeline-gate.py:530-539`), so a
key-only emitter is green everywhere, and even a **lying** coverage line (`derived_forms=0`,
`violations=99`) leaves `20/20 legs passed`. `D03 §3.1` closes it with a scratch consumer probe
that re-derives the counters through a fresh parse sharing no code path with the gate's `Counter`.
**Extends** P01: the claim's "no vacuous-pass" threshold needs a **reader**, not only a producer.
`R03 §7` records that D03's probe lives under `.scratch/d03/` and is therefore **not filed**, so as
of that review the F-6 threshold had no durable instrument.

**§11.3 — D05's era control narrows the claim, correctly.** `D05 §3` shows
`tools/gates/lexicon-coverage-audit.py` **already fires** `D-stage-mismatch` on an E0-dated stamp
form — driven by *construction availability*, not by RGL-05's register law. Control C4 isolates it:
widen `STAMP-LENGTHEN.available_from` to `E0` and the same defect becomes invisible to **every**
delivered gate. So a D03 "era leg" that merely rides on `D-stage-mismatch` is not the era leg.
**Extends** K01 §5.3 (whose control A is the C1 shape). §6.2 D4 makes the C4 shape the required
control.

**§11.4 — The pin cascade is one-directional and the law-gate leg is the expensive one.**
`A01 §3a/§3b`, `D04 §0/§3/§4`, `D06 §3.2/§3.4`, `D08 §4.5` and `D02 §3.5` independently measure the
same three facts: editing the law gate reds `r30-post` (`gate_sha256 15f8b232…`, one
`gate_revised`); editing the argot gate is **pin-neutral** (its `b5406bcd…` is pinned by no
`expected.json`, is in no battery name constant, and is not an r7 read-set member); and adding the
13th read-set member reds the r7 chain by digest. `A01 §3c` adds the mechanism
(`assert_manifest_equality` asserts `checked == len(V3_READ_SET)`,
`tools/exercise-handoff-e2e.py:3661-3662`). **Converges** with this seat's §8 row set.

**§11.5 — The O guard's naive shape is a false-red machine, and its source of truth is the blocking
issue.** `R02 F2` measures a **global** manifest-vs-read-set guard producing **7** named rows (6
legitimate D2 members + `13-register-law.yml`) and exit 1 — i.e. a guard that *harms* operability.
`R02 F3` measures the two variants: D4-scoped record-only names exactly the one member and keeps the
r7 chain at exit 0; D4-scoped **raising** reds the chain **and** breaks the renderer's own positive
selftest (its fixture freeze pins exactly `V3_READ_SET`, `tools/exercise-handoff-e2e.py:4165-4169`).
So the claim's *"refuses **or** names"* is only satisfiable by **naming**. `R03-C1` adds the
**blocking** finding: a guard written against the rendered `packet.md` (12 D4 rows) is **vacuous** —
it can never name the r7 member; the correct source is the source packet's mined manifest
(`v3_mine_d4`, 13). `R03 §5` supplies the placement constraint that makes the naming compatible with
the r7 row staying green. §6.3 O1/O3/O4 encode all three.

**§11.6 — The O08 expectation is unsatisfiable as written.** `X02 §4a` measures **every** filed v3
row's frozen packet manifest against its frozen `inputs`: r2/r5/`declared-in` agree at 12/12; **r6
and r7 both mismatch** (13 declared vs 12 in `inputs`). `A02 F-A02-3` independently reproduces the
generalization. `X02 §4b` adds that r2/r5/r6 **abort at `E2E-READSET`** before any later-added check
is reached. §6.3 O5/O6 carry both.

**§11.7 — The O fix route is a re-render, not a documentation tweak.** `O04 §2` measures three
variants: splice into `D4_COMPONENTS` → packet `7f0e4790…`, 13 `A-NN` rows renumbered; tail append →
packet `7ca92109…`, zero renumbering (**the cheaper insert**); tail append plus a paired move of
`V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT` to a new row → `b102aa70…`, default chain **exit 0**.
`O05 §2–§5` verifies the route and files two defects against it (variant B leaves the named tuple at
12; variant C's packet digest is path-dependent; the expansion adds no detection power) plus a
cascade surface O04 did not reach — the **filed r34/r35 validators assert the old literals**.
`R02 F4` states the mechanism (the packet embeds `{len(V3_READ_SET)} read-set files`,
`tools/exercise-handoff-e2e.py:2825`). §6.3 O9 requires the row to be **documented**, not applied.

**§11.8 — A01/A03 agree the round's scope is clean, and A01 files the unbound declaration.**
`A01 §3` is the round's scope hazard measurement (§11.4 above). `A01 §4` files the *"two named
tool/example artifacts"* ambiguity. `A03` reproduces A02's evidence base independently (baseline,
tracked diff empty, untracked rows all under `reports/round-38/`, frozen bytes unmoved, r7 pins,
`derived_pairs=8 violations=0`, law `findings=0`, typed `20/20`, selftests `27/27` and `45/45`) —
**converges** with §3. `A02 §5 F-A02-1/F-A02-2` files the undeclared `A` block and the live
`corpus/README.md` duplicate heading. Three seats (A01, A02, D07) reached the round's premises
without coordinating, which is the strongest adjacency signal available this round.

**§11.9 — R01 falsifies four points and one is scope.** `R01 §2–§5` reproduces the era hole,
measures that the era leg moves a **third** pinned surface, prices the two F-6 routes as not
equivalent, and shows the F-6 numbers are a **relabel** whose pass can be vacuous. `R01 §6` rules
`head2` **out of this claim** (its empty proper domain is `OI-02`, carried) and requires the
*after* to show a **new** coverage name and a **new** era finding on a tampered control, not a
re-print of the same numbers. §7 row 1/2 of this dossier is that requirement, formalized.

**§11.10 — Dependency state, and it moved under this seat.** At this seat's first sample
`reports/round-38/` held 25 files (S01 itself absent); at finalization it holds 26 with this file.
The 10 outputs still absent are listed in §2.5. **`depth/D01-f6-design.md` and
`op/O01-guard-design.md` are the two absences that bind**: D03's mission named D01/D02 as its
inputs and never received them (`D03 §0`, `D05 §0`, `R01 ## Owed` all record the absence), and
R03-C1's blocking finding cannot be verified against an O01 draft that does not exist
(`R03 ## Owed`). So §6.3 O3 is written as a **constraint on whatever draft lands**, not as a
verification of a draft this seat could read.

---

## Owed

- **`reports/round-38/run-validation.py` and `reports/round-38/validation.json`** — absent at this
  seat's cut; claim D's third counting command and both claims' threshold command are `to-verify`
  until they land. Owner: the round-38 integrator. It must be written with a **relative `ROOT`**
  (§5) so that the F-C13-1 rule is mechanically enforceable, and it must **never** be run in-tree.
- **Every claim artifact.** No D or O byte has landed (§0). If the integrator applies the drafts,
  the landed set is the roster in §8; until then the fleet report's *Landed changes* section must
  say so plainly rather than list drafts as changes.
- **`depth/D01-f6-design.md`, `depth/D02-rl8-design.md`** — D02 landed (§11.10); D01 did not. D03's
  named inputs. Owner: D01, then the integrator.
- **`op/O01-guard-design.md`, `op/O02-isolated.md`, `op/O03-verify.md`, `op/O06-receipt.md`,
  `op/O08-regression.md`** — the O block's design, isolated verify, verification, receipt and
  regression sweep. Absent. R03-C1 cannot be verified against them. Owner: O block.
- **`scout/K02-roster-guard.md`, `cross/X00-connector.md`, `cross/X01-trades.md`** — absent.
  `X00`'s pins cascade for claim D and `X01`'s trade hunt are therefore not folded here.
- **`reports/round-38/scribe/S01-integration-draft.md`** — this file; it was one of the 10 absent
  outputs and this write closes it.
- **The new `tools/gates/expected/register-law-gate/<new-id>/` baseline** if the RL-8 leg lands
  (§8 row 1). Never repoint `r30-post`. Owner: integrator.
- **The successor-baseline row for the O fix route** (`O04 §5` draft) — documented this round,
  applied in a round that owns the re-freeze. Owner: integrator.
- **Telemetry close** — `observed-dispatch.json` and `availability-close-38.json`; the round is not
  admissible to `LOG.md` while the closing snapshot is owed (§9). Owner: integrator.
- **`../.ufo/reports/round-38/kotodama.md`** (the four-section report §4 supplies), the fleet-root
  `MANIFEST.json` round-38 row (measured: **0** such rows), the `SCORECARD.md` r38 row (measured:
  absent) and the append-only `LOG.md` entry (measured: 0 matches for `Round 38`) — integrator-only
  writes.
- **`corpus/README.md` duplicate H1** — live defect, routed, needs an owner (`A01 §5`).
- **The two named artifacts binding** (§6.4 X7) — must be resolved **before** any draft is applied.
- **Not measured by this seat:** whether the devin batch completed or also failed (§2.4); the
  contents of `depth/D01-f6-design.md` and `op/O01-guard-design.md`; the r6 freeze's own history
  behind its 13-vs-12 asymmetry (carried `to-verify` by `X02`); and whether the round-38 runner
  tolerates the extra keys the telemetry templates add (the runner does not exist).

## Citations

**Binding rules and this seat's assignment.** `reports/round-38/targets.json:3-10` (shared rules;
`:8` F-C13-1), `:209-214` (the S01 seat row: role scribe, claim cross, mission, out path),
`:152-172` (the A block), `:11-236` (all 32 seat rows); `reports/round-38/claims.json:1-28`
(round/loop/position/declared_at/baseline/dispatch/axes/lowest-axis/pause, the two claims with
`before`/`after_required`/`counting_commands`/`thresholds`, and the non-goals);
`REGIMEN.md:16,14,25-50,52-58,66-69,73-75` (position 6 with no fallback, position 4 with one, the
per-round contract, done-when, the deviation rule, the stop rule).

**Measured by this seat.** §1 state pins (`git rev-parse HEAD`, `git diff --name-status 9bccc9b`,
`git status --porcelain -uall | wc -l` → 26, `date -u`, `python3 -V`, the `sha256sum` block);
§2.1–§2.2 (JSON parse of `claims.json`/`targets.json`: 12 keys, no `baseline_expanded`; seat
census); §3.1 (three gates); §3.2 (three `sha256sum`s + `--profile v3 --quiet`); §3.3 (battery +
four selftests); §3.4 (the per-file receipt digest sweep over `git ls-files
'reports/round-*/validation.json'`; `ls reports/round-*/run-validation.py | wc -l` → 32);
§5 (`ls reports/round-38/run-validation.py`, `ls reports/round-38/validation.json`,
`ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-38/`, `grep -c '"round": 38'` over
`MANIFEST.json` → 0 rows, `grep -c "Round 38" LOG.md` → 0, `grep -c '^# kotodama-shokunin corpus
index' corpus/README.md` → 2, the corpus partition vector `21/23/25/29/20/94` and
`ls corpus/lessons/*.md | wc -l` → 33).

**Source lines.** `tools/exercise-handoff-e2e.py:157-170` (`D4_COMPONENTS`, 12),
`:1939-1965` (`V3_READ_SET`), `:2045-2056` (`v3_mine_d4`, mines 13), `:2208-2222`
(`v3_verify_component_digests`), `:2825` (the read-set count in the packet),
`:3661-3662` (`assert_manifest_equality`), `:3823-3836` (the one-directional `E2E-READSET` guard),
`:4165-4169` (the fixture freeze pins `V3_READ_SET`), `:1346`/`:3654` (the two existing
manifest→readset checks); `tools/gates/typed-pipeline-gate.py:84,517-541,530-539`;
`tools/gates/argot-derivation-gate.py:917-921`; `tools/gates/register-law-gate.py:121-122`;
`tools/gates/lexicon-coverage-audit.py:846-867`; `tools/check-gate-battery.py:117-132,130-132,540-545`;
`tools/d2-typed-labels.py:2879-2895,3114-3115`; `tools/assemble-d4-typed.py:127-148`;
`examples/culture-d4/packet.d4.yml:1366,2863,2875-2888`;
`examples/culture-d4/components/13-register-law.yml:49,57`;
`examples/culture-d4/typed-labels.d4.yml:29-47`;
`reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt}`;
`reports/round-34/run-validation.py:10,26,209-211`; `reports/round-35/run-validation.py:9`;
`reports/round-33/run-validation.py:23`; `reports/round-36/run-validation.py:319`;
`reports/round-37/run-validation.py` (`SECTIONS`, the `X1-X3` telemetry block, the close-time
record list); `reports/round-37/validation.json` (key set, `acceptance_checks_passed: true`);
`reports/round-37/telemetry/{observed-dispatch,availability-close-37}.json`;
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-37/kotodama.md` (the four landed headings);
`/home/vgpnk/Projects/shokunin/MANIFEST.json` (252 rows, last kotodama lane rounds 35/36/37);
`corpus/knowledge/verification/gate-frozen-run-standard.md:74`; `PROVINCE.md:9-11,20`;
`SHONEN.md:10-11`; `AGENTS.md:15-39`.

**Round-38 fragments folded, each read in full.** `scout/K01-residue.md` (§0, §2.1–§2.3, §3.1–§3.2,
§4, §5.2–§5.3, §6, §7); `plan/P01-d-plan.md` (§0, §2.1–§2.2, §3.2–§3.4, §4.1–§4.4, §5, §6.1–§6.4);
`depth/D02-rl8-design.md` (§2.1, §3.5, §4, §5, §6, §7); `depth/D03-isolated.md` (§0, §1, §3.1–§3.3,
§4, §5, §6.1–§6.4); `depth/D04-pins.md` (§0, §1, §3.1–§3.2, §4, §5, §7); `depth/D05-verify.md`
(§0, §3); `depth/D06-verify-pins.md` (§3.2, §3.4, §4, §5); `depth/D07-receipt.md` (§0, §3.1–§3.3,
§4.1–§4.2, §5, §Owed); `depth/D08-gap-fill.md` (§2.1–§2.3, §3, §4.2–§4.5); `depth/D09-scribe.md`
(§0, §2.1–§2.3, §5); `depth/D10b-verify.md` (§2, §3, §4, §5, §5b, §6); `op/O04-fix-route.md`
(§1, §2, §4, §5, §6); `op/O05-verify-route.md` (§1, §2, §3, §4, §5); `adj/A01-scope.md` (§3a–§3d,
§4, §5); `adj/A02-receipt.md` (§5 F-A02-1/F-A02-2/F-A02-3/F-A02-4, §6, §7); `adj/A03-verify.md`;
`review/R01-d-review.md` (§1–§6); `review/R02-o-review.md` (F1–F6, the guard-point recommendation);
`review/R03-cross-review.md` (§0, §2.1–§2.3, §3.1–§3.3, §4, §5, §6, §7, §8); `cross/X02-honesty.md`
(§0–§5); `scribe/S02-telemetry-draft.md` (§0–§1, §2 F2/F8/F9, §Owed).

**Prior-round precedent reviewed.** `reports/round-36/scribe/S01-integration-draft.md` (§0.2 the
in-tree-runner incident and F-S01-1/F-S01-2, §4 telemetry material, §5 the four schema traps, §6–§7
the leg spec and the 28 selftest controls, §8 the measurement list, §9 the declaration defects);
`reports/round-37/scribe/S04-integration-draft.md` (the fleet-report draft shape, the runner
specification and the 30-control selftest checklist);
`reports/round-36/validation.json` (`claims.D` failed-as-declared, the residue routed forward);
`reports/round-37/adj/A01-freeze-adjudication.md`; `reports/round-30/fixes/battery-registration.md`;
`reports/round-26/register/repin.json`; `reports/round-37/op/defect-queue.json`
(`R36-R7-READSET-13`, `R36-README-E3-PLACEHOLDERS`, `R36-README-DUPLICATE-HEADING`).

---

*This dossier claims no promotion, no canon, no clearance and no closure. It is integration
material: a fleet-report draft, a leg specification the integrator implements, and a selftest
checklist. A green gate is a measurement, not a verdict, and a draft is not a landed change.*
