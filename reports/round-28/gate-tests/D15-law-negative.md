# R28-D15 — the negative: both tampered register-law rows are caught by a named `D4L-LAW-*` finding

- **Seat:** R28-D15 (gate runs 3 of 4), round 28, loop 3 build 4 of 4, claim **D**
  `register-law-replay` (`reports/round-28/claims.json:9-18`).
- **Date:** 2026-10-18 (measurements 20:1x–20:2xZ). Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **Write scope:** this file only; scratch under `.scratch/r28-d13/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No tool,
  gate, packet, component, fixture or filed rounds 8–27 byte was written.
- **Canon:** NON-CANON engineering evidence.

## 0. Verdict

**RL-1 is closed: a tampered register-law row now raises a named `D4L-LAW-*`
finding the clean tree does not carry.** Round 27 measured the opposite — a
tampered row produced "the same 12 findings" as a clean one. This seat's two
plants, run through the delivered leg on a working-tree clone, each add exactly
the finding their tamper should break.

| plant | landed | rebuilt | caught | new named tokens |
|---|---|---|---|---|
| `RGL-01.force` → `no-such-force` | yes | yes | **yes** | **`D4L-LAW-FORCE`** |
| `RGL-01.speaker` `(OR-02)` → `(ZZ-99)` | yes | yes | **yes** | **`D4L-LAW-SPEAKER`** |

The delivered leg is `tools/gates/register-law-gate.py` (new this round, sha256
`cfbff16bbb67d94d39b8d19f7f3fa14d985d18d1f306c8b8e39f79d20ad00e5e`), discovered
by **content** (the `D4L-LAW` class token), not by a hardcoded path.

## 1. The measured clean baseline, and why it is not zero

The delivered leg fires on the **clean** packet, and that is correct rather than
a false positive. It reports four `D4L-LAW-DANGLING` HOLDs — the four
`design_row` citations in the law rows name `QREG-05..08`, which no delivered
record carries:

```
$ python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-05, which no delivered record carries
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-07, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-02 design_row names QREG-06, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-03 design_row names QREG-08, …
coverage: … law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3
           force_failures=0 consequence_failures=0 dangling=4 findings=4
exit 1
```

The round's design seat measured the same four (`reports/round-28/law/design.md`
§3.1) and named them a **real defect**, not a calibration artifact: the law's
prose `cite:` paths all resolve (13/13) while its structured `design_row` ids all
dangle. The leg is honest about it.

**The D15 control therefore grades against the clean baseline's own token set,
not against "empty".** A plant is caught when it **adds** a token the clean run
does not carry. That is the discrimination the claim asks for, and it is the only
reading that works on a leg with a non-empty honest baseline.

## 2. Three ways this seat got the negative wrong first, all fixed

This is recorded because a battery that grades its own bugs as verdicts is worse
than no battery. All three failures were **false reds in the same direction** —
each would have "confirmed" RL-1 for the wrong reason.

### 2.1 The invocation bug — the probe graded its own typo

The first revision ran every discovered instrument with `--packet` and **no
argument**. Every one died on an argparse usage error:

```
reports/round-28/audit/x59-register-law-negatives.py --packet
  exit 2: error: argument --packet: expected one argument
reports/round-28/audit/x60-sweep-completeness.py --packet
  exit 2: error: unrecognized arguments: --packet
```

The battery read those exit-2 runs, found no `D4L-LAW-*` token in the usage
message, and reported "no named finding" — **grading its own typo as a verdict**.

**Fixed** by probing the shape by behaviour: try `--packet PATH`, then a
positional path, then no argument, and keep the first whose invocation is not an
argparse usage error. The probe records every attempt, and a usage error is
explicitly not a verdict. The selftest measures this against a real flagless
instrument on disk.

### 2.2 The discovery bug — non-instruments swept in

The second revision's content discovery swept `reports/round-28/**/*.py` and
picked up **the round's own acceptance runner** and a sibling seat's scratch
poller. Neither is a law instrument: the runner's flag is `--round`, so a
`--packet` probe "succeeded" with the packet swallowed as the round value, and
the poller is transient scratch.

**Fixed** by splitting discovery into two surfaces: **`leg`**
(`tools/gates/*.py`, `tools/*.py`) — where a delivered leg may live, and the
surface the claim's clause names ("no tool under `tools/`") — and **`audit`**
(the round's audit/scribe tools), recorded as corroborating readers only. A
catch by an auditor is not teeth in the pipeline. The audit surface is also not
cloned, because those tools read `reports/round-28/`, which is outside the
clone's read set.

### 2.3 The plant-shape bug — the speaker tamper was invisible for the wrong reason

The third revision's `speaker` plant replaced the whole value with
`"no-such-speaker-class"`, **stripping the `(ID)` parenthetical**. The delivered
leg resolves a speaker by the id inside `Name (ID)`, so with no parenthetical
there was nothing to resolve and the plant was invisible — not because the leg
lacks teeth, but because the plant was malformed. Measured both ways:

```
speaker: "nobody-nowhere (ZZ-99)"        → D4L-LAW-SPEAKER fires
speaker: "no-such-speaker-class"         → no SPEAKER finding (nothing to resolve)
```

**Fixed** by moving the id to an unresolvable one (`mold-keeper (OR-02,
component-only)` → `mold-keeper (ZZ-99)`), which is the shape the round's own
acceptance runner uses and the shape the design's own C-3 control uses. The
selftest now asserts the plant keeps an `(ID)` parenthetical and that its anchor
is a single delivered occurrence.

**The lesson is the seat's own finding:** a tamper control measures the leg only
if the tamper is *of the kind the leg resolves*. A plant that removes the very
structure under test is inert, and an inert plant reads exactly like a missing
leg.

## 3. The controls, and why the clone is the baseline

The plant is a **single-token textual rewrite** of the delivered component bytes,
never a re-serialisation. The anchor names the row (`RGL-01`), not a bare field,
because `force:` appears five times in the component and a bare anchor would
plant into a neighbour.

The control copies the **working tree** into scratch, mutates the component
there, and rebuilds through the lane's own pipeline (`assemble-culture-d4.py` →
`d2-typed-labels.py` → `assemble-d4-typed.py`). A `git clone` would be the wrong
baseline: the round-28 landing is **uncommitted**, so a clone of HEAD carries the
pre-fix tree and the baseline would not be the bytes this round grades.

| control | result |
|---|---|
| the clean copy rebuilds | yes — all three pipeline steps exit 0 |
| the clean copy reproduces the baseline verdict | yes (`D4L-LAW-DANGLING` ×4, exit 1) |
| each plant lands on the delivered bytes | yes, both |
| each plant rebuilds through the lane pipeline | yes, both |
| each planted row is caught by a named finding | **yes, both** — the closing |
| the restored tree returns to the baseline verdict | **yes, both** |

The restore check is now **non-vacuous**: with a leg present, the component is
restored byte-for-byte, the tree rebuilt, and the verdict returns to the clean
baseline's exact token set — so the added finding was the plant's and nothing
else.

## 4. Corroboration

The round's own law auditor agrees independently:

```
$ python3 -B reports/round-28/audit/x59-register-law-negatives.py --packet examples/culture-d4/packet.d4.yml
```

Its own candidate list (the projector and the typed gate) and its `L6b` leg
re-measure the teeth question with different machinery (ruby YAML, its own
operations). This seat's leg is the delivered one; the auditor is the second
opinion. A third peer measurement, seat R28-D17's tamper matrix, runs nine
tamper routes and is the round's broader sweep of the same question.

## 5. Named limits this seat does not close

| limit | measured |
|---|---|
| the leg fires on the clean packet (4 `DANGLING` HOLDs) | `reports/round-28/law/design.md` §3.1 — a real defect, reported not repaired |
| `D4L-LAW-CONSEQUENCE` / `D4L-LAW-DANGLING` are saturated on the clean packet, so a tamper in those classes cannot add a token | the design's C-4/C-6 controls, §3.4 of the same file |
| the leg resolves speakers by record id, not office name | `LD-2` |

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
grep -rln "D4L-LAW" tools/ | wc -l                       # 1 producer (was 0)
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/register-law-gate.py --selftest | tail -1     # 33/33
python3 reports/round-28/gate-tests/run-gate-tests.py             # D15 checks, receipt law_plants
python3 reports/round-28/gate-tests/run-gate-tests.py --selftest  # 31/31
sha256sum tools/gates/register-law-gate.py examples/culture-d4/components/13-register-law.yml
```
