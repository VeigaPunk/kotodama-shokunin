# R28-D07 — the controls: every class fires, and the clean packet's findings are real

- **Seat:** R28-D07 (D axis, law-replay implementation 3 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`.
- **Date:** 2026-10-18. Baseline `6c0ac448…`; lane HEAD `69cecbc`.
- **Artifact under test:** `tools/gates/register-law-gate.py`
  (sha256 `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`).
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
- **Canon:** NON-CANON engineering evidence.

## 0. The claim's teeth test, restated

Round 27's RL-1 was not "the law is incomplete". It was that a **tampered** row
produced *the same finding set* as a clean one:

> `force: "no-such-force"` produces no finding anywhere in the pipeline. **The
> law, as landable today, is a declaration with no teeth.**
> — `reports/round-27/law/review.md` §2

So the load-bearing control is not "the clean packet is silent" (the delivered
law has real defects and *is* not silent) but **"a tamper adds a finding the clean
packet does not produce"**. The round runner grades exactly that, over *lines*
rather than class ids, and says why: two classes are already saturated on the
clean bytes, so a further tamper in those classes adds a line without adding a
class (`reports/round-28/run-validation.py`, `law_finding_lines` docstring).

## 1. The selftest: 33 checks, 33 pass

```
$ export TMPDIR=$PWD/.scratch
$ python3 tools/gates/register-law-gate.py --selftest
…
selftest: 33/33 checks passed
```

The battery is built around a **synthetic** law packet whose every clause can be
moved by keyword, plus the delivered packet as the end-to-end control:

| group | checks | what it proves |
|---|---|---|
| clean synthetic | 4 | no class fires on a well-formed row |
| per-clause tamper | 6 | each of force/speaker/consequence fires **and names the row and the value** |
| discriminating | 3 | each tamper fires **and** the clean row is silent — a control that cannot fail is not a control |
| `none` handling | 3 | `none` is accepted, its consequence is not resolved, and `none but wibble` fires |
| row presence | 1 | a dropped `RGL` row fires; a full set does not |
| `design_row` | 3 | dangling fires; resolved silent; empty silent |
| register/axis/kind | 4 | each fires on an unknown value, silent on a declared one |
| coverage | 1 | a packet with no law block fires `COVERAGE`, never a silent pass |
| exit codes | 4 | 0 / 1 / 2 and the unevaluated path names its data class |
| delivered packet | 4 | the real packet replays, and all three of the runner's tampers add a line |

## 2. The three tamper deltas, end to end, through the round runner

The runner builds the tampers itself (`tamper_law_text`: a textual rewrite of the
**first** matching field line, never a re-serialization) and runs the discovered
leg on each. Read back from `reports/round-28/validation.json`:

| tamper | clean lines | tampered lines | added line |
|---|---:|---:|---|
| `force` | 4 | 5 | `FINDING D4L-LAW-FORCE: FAIL — RGL-01 force 'no-such-force' names no declared illocutionary class or modifier; …` |
| `speaker` | 4 | 5 | `FINDING D4L-LAW-SPEAKER: FAIL — RGL-01 speaker names agent id ZZ-99, which resolves to no delivered record: …` |
| `consequence` | 4 | 5 | `FINDING D4L-LAW-CONSEQUENCE: FAIL — RGL-01 consequence 'the act evaporates silently' names no delivered roll/rank machinery; …` |

**Round 27: 12 = 12, no delta. Round 28: +1 per tamper, three of three.**

## 3. The remaining resolutions, controlled directly

The runner builds only three tampers; the leg resolves eight things. The other
five were controlled by a seat-side probe that tampers a **law row** (not the
first matching field anywhere in the packet — a probe anchoring mistake this seat
made once and corrected, see `impl-6.md` §4):

```
$ python3 - <<'PY'   # anchored on the register_law block
… register    added_classes=['D4L-LAW-REGISTER'] lines=1
… axis        added_classes=['D4L-LAW-AXIS']     lines=1
… kind        added_classes=['D4L-LAW-KIND']     lines=1
… design_row  added_classes=[]                   lines=1   (saturated class, new line)
… row-drop    added_classes=['D4L-LAW-ROW']
PY
```

All eight resolutions are therefore controlled: five by direct tamper here, three
by the round runner's own built tampers, and every one by the selftest's synthetic
packet.

## 4. The clean packet's four findings, and why they are not defects of this seat

The clean run emits **four** `D4L-LAW-DANGLING` holds. They are not noise and they
are not repaired here:

```
RGL-01 design_row -> QREG-05    the design row the law claims to implement is not a packet record
RGL-01 design_row -> QREG-07    same
RGL-02 design_row -> QREG-06    same
RGL-03 design_row -> QREG-08    same
```

The `design_row` field cites the sibling design seats' proposed `QREG-05..08`
rows, which **never landed** as packet records; the landed rows are `RGL-01..05`.
The design seat measured the same four dangles independently
(`reports/round-28/law/design.md` §3.1, six findings on its own reader) and named
the owner as `13-register-law.yml`'s. That file is a **filed round-27 artifact**;
repairing it would rewrite a filed byte, which this lane forbids. So the finding
is **reported with its owner**, and the leg's clean baseline is not weakened to
make it disappear — the runner's own docstring anticipates exactly this: "a leg
that fired on nothing would be the defect, not the fix."

The same reasoning covers the design's two `CONSEQUENCE` class-fit findings
(`RGL-04`/`RGL-05` carry constraint statements in a speech-act block). This seat's
leg **scopes the consequence resolution by the row's own `force: none`**, so it
reports 0 for those two where the design's reference probe reports 2 — a
deliberate, declared difference, not a disagreement: the design's §6 owner table
offers "scope the leg's consequence resolution by `kind`" as one of the two
acceptable dispositions, and this leg takes that one.

## 5. A control that cannot fail is not a control — the one this seat removed

The first implementation of the `none` resolution read it by token membership.
Its selftest caught that a value appending garbage to `none` walked through:

```
'none but wibble'  -> []    # the hole
```

Tightened to require a separator after the head word; the same probe now fires.
Recorded in `impl-2.md` §3. **A control the implementation invents for itself is
still a control when it changes the implementation** — this one did.

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/register-law-gate.py --selftest                     # 33/33
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 reports/round-28/run-validation.py --check \
  | python3 -c "import json,sys;d=json.load(sys.stdin);m=d['claims']['D']['measurement']['law_replay'];[print(k, m['clean']['lines'], v['lines_total'], v['added_over_clean']) for k,v in m['tampers'].items()]"
```
