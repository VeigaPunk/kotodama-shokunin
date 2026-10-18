# R25-D19 — frozen rows for the argot-derivation capability (new rows only)

- round: 25 (operator loop 3 of 3, build 1 of 4; `devin/deepseek-v4-1-flash-high`).
  Seat **R25-D19** (D-scribe 2 of 3).
- claim under draft: `reports/round-25/claims.json` claim **D**,
  capability `argot-derivation-check`.
- date: 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`
  (declared); worktree HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
  All measurements below carry their stamp.
- **writes: this file only** plus gitignored scratch under `.scratch/r25d/`
  (`TMPDIR=$PWD/.scratch` preceded every scratch-writing command; the frozen
  replays themselves need `TMPDIR` **outside** the repo — see §2).
- **no filed frozen row was edited.** No `MANIFEST.tsv`, no `expected.json`, no
  `freeze-receipt.json` under `tools/gates/frozen/` or `tools/gates/expected/`
  was touched. No commit, no push.
- canon: **NON-CANON engineering evidence.** A freeze pins bytes and verdicts,
  never design quality, scholarship or lore standing; a reproduced red verdict
  stays red.

## 1. The frozen-row discipline this file works inside

`tools/gates/frozen/round-18/README.md` states the rule verbatim: "a re-freeze
is a new recording, never an in-place edit", and "the row is added as a NEW row,
never by editing a recorded one". Round-20, round-22 and round-23 each landed a
**new generation directory** rather than editing an earlier one. This file
follows that rule: every row proposed here is a new row, and every superseded
row is *named*, never rewritten.

Two mechanical constraints shape any row that can grade the argot leg:

1. `tools/replay-frozen.py` launches a pinned gate as
   `[python3, tools/gates/<gate>.py, <input>]` — **one path, no flags**
   (`tools/replay-frozen.py:183-186`). A flag-shaped check is not freezable, so
   a thin gate-shaped adapter must exist under `tools/gates/` (the reason rows
   R25-2/R25-3 exist over the D4 peer tools).
2. The whitelist is `*.py` files **directly under** `tools/gates`
   (`gate_path()`, `tools/replay-frozen.py:131-140`). A row naming
   `tools/d2-typed-labels.py` or `tools/assemble-d4-typed.py` is refused
   `gate_not_whitelisted` **before** any digest check.
3. `TMPDIR` must be **outside** the repo, or every row reads
   `mirror_unsafe` exit 2 (`tools/replay-frozen.py:177`). The lane's usual
   `$PWD/.scratch` is inside it. Measured control in §5.

## 2. Generation inventory (re-replayed 2026-10-18T17:36:45Z)

```
find tools/gates/frozen -name MANIFEST.tsv | sort
```

| generation | rows | replay at 17:36:45Z | reason | notes |
|---|---:|---|---|---|
| `round-3/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | pins the gate bytes at `291c714`; the live tree is not that revision (documented at `SKILL.md:459`) |
| `round-3/attempt-1/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | same class |
| `round-11/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | one row pinned `provenance-audit.py` at a superseded revision |
| `round-18/MANIFEST.tsv` | 2 | **mismatch 1, reproduced 1/2** | `replay_mismatch` | row 2 is a **superseded projection pin** — §3 |
| `round-18/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | row 2 pins `typed-pipeline-gate.py`; the gate moved this round |
| `round-20/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `round-22/d4-repin/MANIFEST.tsv` | 3 | **could-not-evaluate 1, reproduced 2/3** | `gate_digest_mismatch` | row 4 pins `typed-pipeline-gate.py` at `04ad4bb4…`; live gate is now `879d40bf…` |
| `round-23/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `round-25/gate-input/MANIFEST.tsv` | 6 | **REPLAY OK 6/6** | — | **the first round-25 generation**, landed 17:32Z and already re-pinned to the settled gate `879d40bf…` |

Replay commands (each run by this seat at 2026-10-18T17:36:45Z):

```sh
mkdir -p /var/tmp/kotodama-r25     # TMPDIR must be OUTSIDE the repo (§5a)
for m in round-3 round-11 round-18 round-18/repin-d2 round-20/repin-d2 \
         round-22/d4-repin round-23/repin-d2 round-25/gate-input; do
  TMPDIR=/var/tmp/kotodama-r25 python3 tools/replay-frozen.py \
    "tools/gates/frozen/$m/MANIFEST.tsv" | tail -1
done
```

**One wave edit turned five generations red at once.** `typed-pipeline-gate.py`
was edited during this round (`04ad4bb4…` → `a6e8d9c8…` → `daeaa722…` →
`879d40bf…`, settled), and every generation that pins that gate in any row now
reads `gate_digest_mismatch` for that row: `round-18/repin-d2`,
`round-20/repin-d2`, `round-22/d4-repin`, `round-23/repin-d2`. This is the
designed fail-closed behaviour ("a later edit to that gate turns the row red by
design — a re-freeze is a new recording, never an in-place edit"), and the
round-25 `gate-input` generation is the correct response: a **new** generation
recording the settled revision, which replays 6/6. The older rows are historical
under named revisions; the parent dispositions them.

## 3. FINDING — `round-18/MANIFEST.tsv` row 2 is a superseded pin, not drift

Measured 2026-10-18T17:30Z, `--json`:

```json
{"line": 2, "gate": "tools/gates/d4-typed-labels-check-gate.py",
 "recorded_gate_sha256": "05f99629…", "recorded_input_sha256": "a59990bb…",
 "recorded_exit": 0, "observed_exit": 1,
 "observed_output_sha256": "e3b0c442…", "status": "mismatch", "reason": "replay_mismatch",
 "stderr_excerpt": "examples/culture-d4/typed-labels.d4.yml differs from the deterministic projection\n"}
```

The attribution matters and is measured, not assumed:

- The **gate digest verifies** (`05f99629…` = the live
  `tools/gates/d4-typed-labels-check-gate.py`, `sha256sum` 17:29Z). So the
  reason is `replay_mismatch`, **not** `gate_digest_mismatch`.
- The **input snapshot verifies** against its own pin
  (`tools/gates/frozen/round-18/inputs/examples/culture-d4/typed-labels.d4.yml`
  = `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d`,
  `sha256sum` 17:25Z). So **no** `snapshot_tampered`.
- The gate launched and exited 1 with the message that the snapshot *differs
  from the deterministic projection*. The live projection is
  `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092`
  (`examples/culture-d4/typed-labels.d4.yml`, `sha256sum` 17:29Z) — the
  **round-22 family-clean** build.

So: the row is honest and its pins are intact; what changed is the projector's
output, and the successor was correctly recorded as a **new row** in a new
generation (`tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv`, 3/3 OK,
projection pin `60b526b0…`). This is the supersession discipline working as
designed — and it is named here because the round-18 generation now reads
**1 mismatch** on a live run, which a future reader must not mistake for a
fresh defect. The disposition (leave the round-18 row as historical under a
named revision, or annotate the generation README) is the parent's; this seat
does not edit a filed row.

## 4. The frozen rows the argot capability needs

The argot gate **landed at 17:30Z** (`tools/gates/argot-derivation-gate.py`),
settled at `07db6e9b…` by 17:33:42Z, and is flagless and single-input by design
(its docstring: "Flagless and single-input, so `tools/replay-frozen.py` can pin
a row"), so a row can grade it without an adapter. What is missing is the
**recording**: `tools/gates/frozen/round-25/` holds only the O claim's
`gate-input/` generation at this stamp. This section supplies the rows the
recording seat would freeze, in the `MANIFEST.tsv` column schema
(`gate  gate_sha256  input  input_sha256  exit_code  finding_count  output  output_sha256  input_snapshot  command`).

### 4.1 Rows that exist today and are replayable (measured, new-generation candidates)

All digests re-measured at 2026-10-18T17:33:42Z (R25-4 at its settled revision
`879d40bf…`; R25-5 is the new argot row).

| # | gate | gate_sha256 | input | input_sha256 | exit | count | output_sha256 |
|---|---|---|---:|---:|---:|---|
| R25-1 | `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 1 | 14 | `0c613c9d973f3c32bb20f4db7a43a02da7a5edcaa1bc3382531acce21e2a89f7` |
| R25-2 | `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` | 0 | 0 | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| R25-3 | `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 0 | 0 | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |
| R25-4 | `tools/gates/typed-pipeline-gate.py` | `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 0 | 12 | `b064da286d2dd02904788fc3fe4f3bd97fe7e88bbcac657cee114d0a607100bd` |
| **R25-5** | `tools/gates/argot-derivation-gate.py` | `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | **0** | 0 | `49060ed39b8725f5f7268a24492adc52e944f80e8eff517541d2a56d0483104f` |

`finding_count` counts `^FINDING ` lines, the replay tool's own definition
(`tools/replay-frozen.py:96-98`). R25-1 records a red verdict (7 `NAME-NEAR`,
6 `PHON-INVENTORY`, 1 `CROSS-HOLD`; **0** matching `DERIV`).

### 4.2 The row that grades the argot leg — now freezeable, and the paired negative

R25-5 is the clean row. The negative row pairs it with the gate's **committed
fixture**, which carries the planted verdict set the forecast's control C-02
asks for:

| # | gate | input | exit | count | note |
|---|---|---|---:|---:|---|
| R25-6 | `tools/gates/argot-derivation-gate.py` (`07db6e9b…`) | `tools/gates/fixtures/argot-derivation-gate.yml` (`c4c35294…`) | **1** | **5** | the fixture's planted set: 4 `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`, matching `tools/gates/fixtures/argot-derivation-gate.expected` (`38a283ff…`, 5 lines) |

Two rows, not one: a green leg with no recorded negative is not evidence that
the leg can fail. The fixture is a committed NON-CANON artifact, so a frozen row
over it is a legitimate recording, and it is the shape the round-17 design asked
for ("a fixture whose quote form ≠ `apply(op, base)` → FAIL, id
`D4L-ARGOT-DERIV`").

This seat measured the fixture in-process (2026-10-18T17:32Z): exit 1, findings
`{D4L-ARGOT-DERIV: 4, D4L-ARGOT-RULE: 1}`, `derived_pairs=8 borrow_pairs=3
violations=4 rule_holds=1`, exactly matching the `.expected` file and the gate's
own `FIXTURE_EXPECTED` constant.

## 5. Measured controls (this seat)

**(a) `TMPDIR` inside the repo → every row reads `mirror_unsafe` exit 2.**

```sh
TMPDIR=$PWD/.scratch python3 tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv
```

Observed 17:26Z: `REPLAY COULD-NOT-EVALUATE: 3 could-not-evaluate, 0 mismatch,
0 reproduced of 3 row(s)`, each row `reason=mirror_unsafe` with
`detail: mirror: temporary root is inside the repo: …/.scratch/replay-frozen-…`.
This is the tool's own fail-closed control (it refuses to mirror inside the
tree it is grading), and it is the precondition the SKILL row records
(`SKILL.md:294`).

**(b) Tampered snapshot → `snapshot_tampered`, gate not launched.** A copy of
the round-22 generation in scratch with one byte appended to its input snapshot:

```sh
mkdir -p .scratch/r25d/clone && cp -a tools .scratch/r25d/clone/ && cp -a examples .scratch/r25d/clone/
printf '\n# tamper control R25-D19\n' >> .scratch/r25d/clone/tools/gates/frozen/round-22/d4-repin/inputs/examples/culture-d4/typed-labels.d4.yml
TMPDIR=/var/tmp/kotodama-r25 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv --repo-root .scratch/r25d/clone
```

Observed 17:26Z: `ROW 2 could-not-evaluate reason=snapshot_tampered … launched=no`,
rows 3 and 4 reproduced, `REPLAY COULD-NOT-EVALUATE: 1 could-not-evaluate,
0 mismatch, 2 reproduced of 3 row(s)`, **exit 2**. The digest check runs before
any gate is launched.

**(c) The replay tool's own selftest.**

```sh
python3 tools/replay-frozen.py --selftest
```

Observed 17:25Z: **`selftest: 79/79 checks passed`, exit 0** (includes the
flag-input, dot-input, stdin, bad-header and mirror controls).

**(d) True-negative control on the delivered derivation-replay surface.** The
only derivation relation the delivered bytes carry is the name-side CX-01
replay. Mutating `morphology.derivation_rules[0]`'s `output` from `{a}{b}` to
`{a}-{b}` in a scratch copy and running the naming gate:

| run | DERIV findings | exit |
|---|---:|---:|
| delivered packet | **0** | 1 |
| mutated packet | **8** (`DERIV-REPLAY`, one per NM-01..NM-08) | 1 |

The leg distinguishes; it does not always fail. This is the negative-control
shape §4.2 proposes to freeze once the argot leg lands.

## 6. Limits and `to-verify`

1. **No row here is frozen by this seat.** The R25-* rows are measured candidate
   rows in this draft; the recording seat writes them. The argot gate is on disk
   and green (§4), so R25-5/R25-6 are freezeable — what is absent is the
   recording, since `tools/gates/frozen/round-25/` holds only the O claim's
   `gate-input/` generation.
2. **Re-pin at integration.** All digests are worktree values at `f74fc940`
   with sibling seats writing. Both `typed-pipeline-gate.py` and
   `argot-derivation-gate.py` moved inside this seat's window; the §2/§4 values
   are the revisions that were **stable for four consecutive 20-second polls**
   (17:35:02Z–17:36:22Z: tpg `879d40bf`, argot `07db6e9b`). A pin from a moving
   revision is `to-verify` by construction.
3. **`replay-frozen` exit codes are not design verdicts.** Exit 0 asserts
   reproduction of the recorded verdict; a reproduced `exit_code=1` row is still
   red (`tools/replay-frozen.py:38-41`).
4. **The supersession cluster is named, not repaired.** §2 and §3 record the
   `gate_digest_mismatch`/`replay_mismatch` rows and leave every filed manifest
   untouched; the disposition is the parent's.
5. **Out of province, reported not absorbed:** the round-25 generation's
   directory name, whether to freeze the argot rows, and the fixture design are
   orchestrator/integration decisions.

## 7. Counting command for this file

```sh
export TMPDIR=$PWD/.scratch
find tools/gates/frozen -name MANIFEST.tsv | sort
for f in $(find tools/gates/frozen -name MANIFEST.tsv | sort); do
  echo "$f rows=$(( $(wc -l < "$f") - 1 ))"; done
mkdir -p /var/tmp/kotodama-r25     # TMPDIR must be outside the repo
for m in round-3 round-11 round-18 round-18/repin-d2 round-20/repin-d2 \
         round-22/d4-repin round-23/repin-d2 round-25/gate-input; do
  TMPDIR=/var/tmp/kotodama-r25 python3 tools/replay-frozen.py \
    "tools/gates/frozen/$m/MANIFEST.tsv" | tail -1; done
python3 tools/replay-frozen.py --selftest | tail -1
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1   # 18/18
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
```

FILES: reports/round-25/scribe/frozen-rows.md | SUMMARY: D19 scribe — frozen-row draft for the argot leg; the gate landed mid-window and settled green (`tools/gates/argot-derivation-gate.py` sha `07db6e9b…`, `--selftest` 18/18, D4 run exit 0), so R25-5 (clean) and R25-6 (the committed fixture's planted 4 `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`) are freezeable but **unrecorded** — `tools/gates/frozen/round-25/` holds only the O claim's `gate-input/` generation; the full generation inventory re-replayed at 17:36:45Z shows one wave edit to `typed-pipeline-gate.py` (`04ad4bb4…`→`879d40bf…`) turning four earlier D2/D4 generations' typed-pipeline rows `gate_digest_mismatch` while the new round-25 `gate-input` generation replays **6/6 OK**, plus the round-18 row-2 superseded-projection finding and the `mirror_unsafe`/`snapshot_tampered`/79-79 selftest controls.
