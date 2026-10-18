# R27-D22 — frozen rows for the round-27 register landings and the pin cascade (new rows only)

- round: 27 (operator: loop 3 of 3, build round 3 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R27-D22** (D-scribe 2 of 4).
- claim under draft: `reports/round-27/claims.json` claim **D** (`register-law`)
  for §2–§3, with the claim **O** pin surface named in §4–§6 because the rows
  that close it are the same generation.
- date: 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
  Lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- **final stamp 2026-10-18T19:24:15Z.** The D4 packet moved **twice** inside this
  seat's window (`dd25077b…` → `c5441e3d…`), so the frozen surface has two
  distinct generations to name. §1 records the stamps.
- **writes: this file only** plus gitignored scratch under `.scratch/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write; the frozen
  replays themselves need `TMPDIR` **outside** the repo — §5a).
- **no filed frozen row was edited.** No `MANIFEST.tsv`, no `expected.json`, no
  `freeze.txt`, no `freeze-receipt.json` under `tools/gates/frozen/` or
  `tools/gates/expected/` was touched by this seat. No commit, no push.
- canon: **NON-CANON engineering evidence.** A freeze pins bytes and verdicts,
  never design quality, scholarship or lore standing; a reproduced red verdict
  stays red.

## 1. The stamps — the packet moved twice, and the second freeze is the settled one

All stamps UTC, 2026-10-18. The frozen surface has **three** relevant states,
and a reader who used the middle one would pin bytes that no longer exist.

| stamp | `packet.d4.yml` | `typed-labels.d4.yml` | what happened |
|---|---|---|---|
| 19:19:19 | `dd25077b…` | `d03f6391…` | **the O seats freeze `reports/round-27/pinsweep/baselines/{d4-assembly,d4-typed-labels}/r27-post/`** against the post-*register* packet |
| 19:21:29 | **`c5441e3d…`** | **`072fa806…`** | **the register LAW merges** (`13-register-law.yml` → `register_law:` in the packet). The 19:19 baselines are stale from this instant |
| 19:21:44 | `c5441e3d…` | `072fa806…` | **the O seats freeze `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv`** against the post-*law* bytes — **the settled generation**, replaying **2/2 OK** |
| 19:24:15 (**final**) | `c5441e3d…` | `072fa806…` | stable across three re-reads |

**The consequence is measured and it is the load-bearing finding of this file.**
The `baselines/*/r27-post/` directories frozen at 19:19 are **already stale
against the live tree** — 19 minutes later:

```sh
for d in reports/round-27/pinsweep/baselines/*/r27-post; do
  python3 - "$d" <<'PY'
import json,hashlib,os,sys
j=json.load(open(sys.argv[1]+"/expected.json"))
for k,v in (j.get("inputs") or {}).items():
    if os.path.exists(k):
        live=hashlib.sha256(open(k,"rb").read()).hexdigest()
        if live!=v: print("STALE",k,v[:12],"->",live[:12])
PY
done
# STALE examples/culture-d4/packet.d4.yml  dd25077bc016 -> c5441e3d0b23   (d4-assembly, 1 of 16)
# STALE examples/culture-d4/packet.d4.yml  dd25077bc016 -> c5441e3d0b23   (d4-typed-labels, 2 of 6)
# STALE examples/culture-d4/typed-labels.d4.yml d03f6391fb8d -> 072fa806ed78
```

That is the **designed** behaviour (a baseline pins a snapshot, and the battery's
digest step compares the copy to the pin, never the copy to the live file), and
it is why the successor is the `frozen/r27-post` generation rather than the
`baselines/r27-post` directories. A round-27 baseline successor must be frozen
against `c5441e3d…`/`072fa806…`, which the `baselines/r27-post` pair is not.

## 2. The rows the register landings need (measured today, new rows)

All digests measured 2026-10-18T19:23–19:24Z (`sha256sum`, cwd = lane root).
Column schema is the `MANIFEST.tsv` schema:
`gate  gate_sha256  input  input_sha256  exit_code  finding_count  output  output_sha256  input_snapshot  command`.

### 2.1 The rows that exist today and are replayable — proposed successors

| # | gate | gate_sha256 | input | input_sha256 | exit | count | output_sha256 |
|---|---|---|---:|---:|---:|---:|---|
| **R27-1** | `tools/gates/argot-derivation-gate.py` | `d7a3ad1a6ad1c4c5993b7d74bf8bc96326916f113a07e6472d90ceecd7faf1aa` | `examples/culture-d4/packet.d4.yml` | `c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a` | **0** | 0 | *(stdout sha `d6abd137…` at `c5441e3d`; re-hash at integration)* |
| R27-1b | `tools/gates/argot-derivation-gate.py` | `d7a3ad1a…` | `examples/culture-d4/packet.d4.typed.yml` | `7dff3ea7b40af0b45f9472dec77e7b396489baa1d1f383feb20a42bf18e9f939` | **0** | 0 | *(re-hash at integration)* |
| **R27-2** | `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | `examples/culture-d4/packet.d4.yml` | `c5441e3d…` | 0 | 12 | *(re-hash at integration)* |
| R27-2b | `tools/gates/typed-pipeline-gate.py` | `b749ad07…` | `examples/culture-d4/packet.d4.typed.yml` | `7dff3ea7…` | 0 | 12 | *(re-hash at integration)* |
| **R27-3** | `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | `examples/culture-d4/typed-labels.d4.yml` | `072fa806ed78dc321107e5741dc7e365e4dff613395be1c916d60deaab77fe63` | 0 | 0 | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| **R27-4** | `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `examples/culture-d4/packet.d4.yml` | `c5441e3d…` | 0 | 0 | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |
| **R27-5** | `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | `examples/culture-d4/packet.d4.yml` | `c5441e3d…` | **1** | **14** | `0c613c9d973f3c32bb20f4db7a43a02da7a5edcaa1bc3382531acce21e2a89f7` |
| **R27-6** | `tools/gates/argot-derivation-gate.py` | `d7a3ad1a…` | `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` | **1** | **5** | `556d31d6f66715cbcb0c8dc7d5820e0be60b62fae39e304a79537dad06c205a6` |

**R27-3 and R27-4 are the two rows the O seats already froze** as
`reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` (2 rows, 19:21:44Z,
replaying **2/2 OK** at 19:24Z), and this seat's independent measurements
**agree exactly** — same gate digests, same input digests, same exit codes, same
output shas (`1c8add32…`, `c60820a5…`). Two independent runs, two working
directories, byte-identical verdicts.

Measured verdicts (this seat, 19:23–19:24Z, `TMPDIR=$PWD/.scratch`):

| row | command | exit | findings | notes |
|---|---|---|---:|---|
| **R27-1** | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **0** | 0 | coverage: `records=175 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`. **The register domain is no longer empty** (round 26: `records=156 register_scoped=6 derived_pairs=0`), and `records` moved `170 → 175` when the five `register_law` rows entered the packet |
| R27-1b | `… examples/culture-d4/packet.d4.typed.yml` | 0 | 0 | second row, not a variant |
| **R27-2** | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 12 | **20/20 legs incl. `ok L3b-argot`**; the 12 findings equal `expected-holds.json` (`b9f98381…`, counts 12/0/0) |
| R27-2b | `… examples/culture-d4/packet.d4.typed.yml` | 0 | 12 | **17/17 legs** |
| **R27-3** | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | 0 | 0 | green; **stdout byte-identical (`1c8add32…`) to the round-18, round-22 and 19:19 round-27 rows** — the register landings changed the bytes graded, never this gate's verdict text |
| **R27-4** | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 | green; **stdout byte-identical (`c60820a5…`) to every earlier row**. **Not selftest-capable**: `--selftest` is read as an input path → exit 2. The row must carry no selftest claim |
| **R27-5** | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | **1** | **14** | 7 `NAME-NEAR` REVIEW + 6 `PHON-INVENTORY` FAIL on the six garment glosses + 1 `CROSS-HOLD` HOLD. **Byte-identical output sha `0c613c9d…` across the round-26 row, the register landing and the law landing** — the new records add no naming finding. **A reproduced red stays red** |
| **R27-6** | `python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml` | **1** | **5** | 4 `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`, exactly the committed `.expected`; output sha `556d31d6…`, **unchanged even though the gate itself moved** (`5b5abe78…` → `d7a3ad1a…`) — the fixture's planted set is behaviour-stable across the syllabify fix |

**R27-1 is the row the register capability needs, and it must carry its own
honest scope.** The gate's docstring states it: exit 0 means "every
register-scoped form that states its inputs re-derives", **not** that the stratum
is complete. The round-26 capability row's `derived_pairs > 0` condition is
**met** (`derived_pairs=8`), so the provisional clause may be dropped — but the
row still may not claim completeness, and it may not claim enforcement (no lane
gate reads `registers:` or `register_law:`; see
`reports/round-27/scribe/capability-row.md` §1).

## 3. The cascade, measured at the final stamp

**Two landings turned five filed generations red on their D4 rows**, and the
generations that were green at 19:16 are red at 19:24. Replayed with `TMPDIR`
**outside** the repo:

| generation | rows | at 19:24:15Z | reason | notes |
|---|---:|---|---|---|
| `round-3/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | pins the gates at `291c714` |
| `round-3/attempt-1/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | same class |
| `round-11/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | one row pinned `provenance-audit.py` at a superseded revision |
| `round-18/MANIFEST.tsv` | 2 | **mismatch 2, reproduced 0/2** | `replay_mismatch` | was 1 mismatch at round 26. Both snapshot pins verify; both gates exit 1, "differs from the deterministic projection / assembly". **Superseded in substance by `reports/round-27/pinsweep/frozen/r27-post/`** — its `freeze-receipt.json` names exactly "round-18 rows 2-3 (both mismatch, exit 1)" |
| `round-18/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | row 2 pins `typed-pipeline-gate.py`; the gate moved at round 25 |
| `round-20/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `round-22/d4-repin/MANIFEST.tsv` | 3 | **could-not-evaluate 1, mismatch 2, reproduced 0/3** | mixed | rows 2–3 `replay_mismatch` on the moved D4 artifacts; row 4 `gate_digest_mismatch` (`04ad4bb4…`, superseded twice). **Also superseded in substance by `frozen/r27-post/`** |
| `round-23/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `round-25/gate-input/MANIFEST.tsv` | 6 | **could-not-evaluate 6/6** | `gate_digest_mismatch` | every row pins `typed-pipeline-gate.py` at `879d40bf…` |
| `round-26/gate-input/MANIFEST.tsv` | 6 | **mismatch 2, reproduced 4/6** | `replay_mismatch` | **was 6/6 OK when recorded at 18:08:08Z.** Its two D4 rows pin the pre-register packet; the gate refuses them at `L1-assembler` (exit 2 vs recorded 0) |
| `round-26/post-register/MANIFEST.tsv` | 6 | **mismatch 2, reproduced 4/6** | `replay_mismatch` | **was 6/6 OK at 19:16Z, then red at 19:21Z when the law merged.** Its D4 rows pin the post-*register*, pre-*law* packet. **The clearest instance in the round of a generation going red because the artifact moved, not because it was wrong** |
| **`reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv`** | 2 | **REPLAY OK 2/2** | — | **the settled successor**, frozen 19:21:44Z against `c5441e3d…`/`072fa806…`, with an explicit `supersedes` list naming the round-18 and round-22 rows |

**Independent confirmation of the class.** `reports/round-27/audit/x61-pin-sweep.py`
re-derives every frozen row itself and classifies each mismatch as
**supersession** (the live input the row names no longer hashes to the pinned
value) or **drift** (the live input still hashes to the pin). Its classifier
(`:188-196`) is the right one and this file adopts it. At the final stamp, with
its mirrors forced outside the repo, the classification is
**supersession-heavy and drift-zero** — every red D4 row is red because the
artifact it graded **moved**, not because a pinned byte was tampered with. That
is the single most important sentence in this file for the O claim's disposition.

**The `frozen/r27-post` receipt names its supersessions explicitly**, which is
the bookkeeping the round-26 generation lacked:

```json
"supersedes": [
  "tools/gates/frozen/round-18/MANIFEST.tsv rows 2-3 (both mismatch, exit 1)",
  "tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv rows 2-3 (both mismatch, …)"
],
"reason": "the round-26 register stratum amended … the packet, its typed packet,
  its projection and its hold set all moved. Every earlier D4-adapter row pins the
  pre-register digests and now replays exit 1 (drift). A re-freeze is a new
  generation, never an in-place edit."
```

**A residual bookkeeping gap, named and not smoothed.** The round-26
`post-register` receipt's `supersedes` block names `round-25/gate-input` only; it
does **not** name `round-26/gate-input`, which it supersedes in substance (both
pin the same live gate `b749ad07…` and differ only in the packet they grade).
The correct chain is `round-27/pinsweep/frozen/r27-post` ⊃ `round-26/post-register`
⊃ `round-26/gate-input` ⊃ `round-25/gate-input`, and the middle two links are
each missing one pointer. This seat does not edit a filed receipt.

## 4. The battery baselines, measured

`tools/check-gate-battery.py` discovers `expected.json` under three roots
(`tools/gates/expected/`, `tools/gates/frozen/`, `reports/round-9/baselines/`).
Measured at 19:23Z with the default roots:

```sh
python3 tools/check-gate-battery.py
# summary: battery_exit 0, pass 7, fail 0, unevaluable 0
# coverage "9/9", pinned 19, unevaluable 0
```

Six baselines are discovered under `tools/gates/expected/`; all six read
**`pinned`** (their `gate_sha256` equals the live gate and every declared input
digest equals the snapshot copy inside the baseline directory). **`pinned` does
not mean the live tree agrees with the baseline**, and this file must not let a
reader conclude it does. Recomputed against the live paths:

| baseline | input | pinned | live at final stamp | state |
|---|---|---|---|---|
| `d4-typed-labels/r19-pre` | `examples/culture-d4/packet.d4.yml` | `e7ecd204…` | `c5441e3d…` | **stale** |
| `d4-typed-labels/r19-pre` | `tools/d2-typed-labels.py` | `0da0015f…` | `2819f687…` | **stale** |
| `d4-typed-labels/r20-post` | `examples/culture-d4/packet.d4.yml` | `e7ecd204…` | `c5441e3d…` | **stale** |
| `d4-typed-labels/r20-post` | `tools/d2-typed-labels.py` | `76536a92…` | `2819f687…` | **stale** |
| `d4-typed-labels/r22-post` | `examples/culture-d4/packet.d4.yml` | `e7ecd204…` | `c5441e3d…` | **stale** |
| `d4-typed-labels/r22-post` | `tools/d2-typed-labels.py` | `2819f687…` | `2819f687…` | ok |
| `d4-assembly/r19-pre` | `components/01-brief.yml` | `a2bc3111…` | `feca7bda…` | **stale** |
| `d4-assembly/r19-pre` | `components/04-lexicon.yml` | `74c2561b…` | `d0d4e17c…` | **stale** |

The baseline's own `freeze.txt` states the rule in its own words: "the battery's
digest step … compares the copy to the pin, never the copy to the live file".
The battery is a *snapshot-integrity* check; the live-vs-pin recomputation is a
**different** duty.

**The round-27 successor baselines are on disk and they are already one landing
behind.** `reports/round-27/pinsweep/baselines/{d4-assembly-check-gate,d4-typed-labels-check-gate}/r27-post/`
were frozen at 19:19:19Z against `dd25077b…`/`d03f6391…`, and §1 measures them
**stale against the live tree** (1 of 16 inputs for the assembly baseline, 2 of
6 for the typed-labels baseline). Run as a replacement root they also read
**coverage 2/9, exit 2** — because that root holds only the two D4 baselines and
the battery requires a baseline for all nine registered gates:

```sh
python3 tools/check-gate-battery.py --baselines-root reports/round-27/pinsweep/baselines
# coverage "2/9", pinned 2, unevaluable 0, battery_exit 2
#   lexicon-coverage-audit.py has no committed expected.json under the declared roots
```

So the correct successor action is **two** things: re-freeze the two D4
baselines against `c5441e3d…`/`072fa806…`, **and** keep the default roots in the
battery run (the `--baselines-root` flag replaces the roots rather than adding
to them, which is why the coverage reading drops to 2/9). The two successor rows:

| # | gate | input | verdict | stdout_sha256 |
|---|---|---|---:|---|
| **R27-B1** | `tools/gates/d4-typed-labels-check-gate.py` | `examples/culture-d4/typed-labels.d4.yml` (`072fa806…`) | 0 / 0 | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| **R27-B2** | `tools/gates/d4-assembly-check-gate.py` | `examples/culture-d4/packet.d4.yml` (`c5441e3d…`) | 0 / 0 | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |

Both are **byte-identical stdout to the rows they supersede** — the gates'
verdicts did not change, only the bytes graded. A successor baseline must be a
**new directory**, never an in-place edit (`r22-post/freeze.txt`: "supersedes:
r20-post; previous baseline is filed unchanged").

## 5. Freeze rules a recording seat must honour (binding)

1. **New generation, new rows.** A round-27 generation is a new directory; no
   earlier `MANIFEST.tsv`, `expected.json`, `freeze.txt` or receipt is edited.
2. **A freeze receipt that is not a battery baseline is not named
   `expected.json` under a battery root.** Use `freeze.txt` +
   `freeze-receipt.json` (the round-22/round-25/round-26/round-27 shape).
3. **`TMPDIR` outside the repo, always.** §5a.
4. **A row the gate cannot prove does not enter the file.**
   `d4-assembly-check-gate.py` has no `--selftest` (§2.1 R27-4).
5. **A red verdict reproduces as red.** R27-5 is exit 1 / 14 findings and R27-6
   is exit 1 / 5 findings; neither may be "cleaned".
6. **A `supersedes` pointer is part of the row's content.** §3 measures one
   missing (`round-26/post-register` names `round-25/gate-input`, not the
   intermediate `round-26/gate-input`).
7. **A freeze taken while the tree is still moving is already stale.** §1 is the
   worked instance: the 19:19 baselines were stale 19 minutes later. **Freeze
   after the landing settles, and name the revision you froze against.**
8. **A `run.log` under a battery baseline is gitignored** by `.gitignore:3`
   (`*.log`) and must be force-added by the parent
   (`git check-ignore -v <baseline>/run.log` → `.gitignore:3:*.log`).

### 5a. The `TMPDIR` control

```sh
export TMPDIR=$PWD/.scratch        # inside the repo
python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv
# every row reads mirror_unsafe, exit 2:
#   detail: mirror: temporary root is inside the repo: …/.scratch/replay-frozen-XXXX
```

Re-measured this round by three independent seats (this one, the O seats'
`.scratch/r27-o39/*.out`, and X61's own probe, which prints
`TMPDIR probe on …`). A recording seat that runs the replay from the lane's
usual scratch shape sees a refusal rather than a verdict — the designed
behaviour (`tools/replay-frozen.py:177`). §3's command uses
`/var/tmp/kotodama-r27`.

## 6. The round-27 pin surface beyond the frozen tree (named, not swept here)

The claim **O** sweep covers more than `tools/gates/frozen/`. Measured at the
final stamp, these are the other pinned surfaces and their state:

| surface | state |
|---|---|
| `tools/gates/typed-pipelines.json` | **re-pinned this round** (`35946c8d…` → `be306908…`) to the final packet `c5441e3d…` and projection `072fa806…`; the `L1-profile` leg is green again after the mid-round window in which it read exit 2 |
| `examples/culture-d4/expected-holds.json` | **re-pinned** (`d6136488…` → `b9f98381…`); counts still 12/0/0 |
| `reports/round-26/handoff/declared-in-r5/` (v3 baseline) | **stale**: `v3` exits **1** ("not assembled"). `reports/round-27/pinsweep/v3-baseline-r27/` is the successor row on disk (frozen 19:19:41Z); `reports/round-27/run-validation.py` lists `reports/round-27/handoff/declared-in-r5/expected.json` as a **missing dependency** |
| `v2` handoff | green: `handoff-v2: exit=0 claims=15 links=50/50` |
| `reports/round-26/remainders/r4-twin/`, `v3-baseline-r26/`, `register/v3-baseline-r26/` | pin D4 artifacts the landings moved; `packet_links.py` reports `M-DIGEST-MISMATCH` on each |
| `reports/round-9/baselines/` (legacy battery root) | discovered by the battery; no D4 row, unaffected |
| `reports/round-27/audit/x61-pin-sweep.py` | the independent sweep: `baselines 19/19 pinned` at the final stamp, i.e. every baseline snapshot matches its own pin |

**The v3 chain is the O claim's live surface.** `tools/exercise-handoff-e2e.py`
now resolves `V3_BASELINE_DEFAULT = "reports/round-26/handoff/declared-in-r5/expected.json"`
(the round-26 re-point landed), and that read-set pins the pre-landing D4
artifacts, so the run exits 1. The successor row exists
(`reports/round-27/pinsweep/v3-baseline-r27/`); whether the default is re-pointed
at it is the O seats' action, not this seat's — the `V3_BASELINE_DEFAULT`
constant is a `tools/` byte and this seat writes none.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
mkdir -p /var/tmp/kotodama-r27
sha256sum tools/gates/*.py examples/culture-d4/*.yml examples/culture-d4/*.json \
  examples/culture-d4/components/13-register-law.yml
find tools/gates/frozen -name MANIFEST.tsv | sort
for m in $(find tools/gates/frozen -name MANIFEST.tsv | sort); do
  printf "%-52s " "$m"
  TMPDIR=/var/tmp/kotodama-r27 python3 tools/replay-frozen.py "$m" | tail -1
done
TMPDIR=/var/tmp/kotodama-r27 python3 tools/replay-frozen.py \
  reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv | tail -1      # REPLAY OK 2/2
TMPDIR=/var/tmp/kotodama-r27 python3 tools/replay-frozen.py --json \
  tools/gates/frozen/round-26/post-register/MANIFEST.tsv | tail -1     # 2 mismatch / 4 reproduced
python3 tools/check-gate-battery.py                                     # 7 pass / 0 fail; coverage 9/9
python3 reports/round-27/audit/x61-pin-sweep.py                         # baselines 19/19 pinned
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet              # exit 1 (stale read-set)
python3 tools/exercise-handoff-e2e.py --profile v2 --quiet              # exit 0
```

## 8. Limits

- The rows in §2.1 and §4 are **measured today** on the live tree; they are the
  rows a round-27 generation records. They are not filed — this seat writes no
  `MANIFEST.tsv` and no `expected.json`.
- The successor baselines in §4 are **named, not landed**.
- **Every reading binds to the digest and stamp beside it, and the tree moved
  twice in this seat's window.** §1 is the movement record; a successor must
  re-hash before quoting any digest here. The `frozen/r27-post` generation and
  the `baselines/*/r27-post` directories pin **different** packet bytes.
- A freeze pins bytes and verdicts, never design quality, scholarship, lore
  standing or promotion. This file admits nothing.
