# R27-D08 — the pin cascade: what this landing moved, and what it does not own

- **Seat:** R27-D08 (D axis, register law + syllabify implementation 4 of 8).
  Round 27, loop 3 build 3 of 4, claim **D** `register-law`. Integrator:
  `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990…`; declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The pin surface this landing moves

The D4 packet moved, so every surface that pins a D4 digest moved with it. Four
classes, and only two are this seat's:

| surface | disposition |
|---|---|
| `examples/culture-d4/expected-holds.json` (`packet_sha256`, `projection_sha256`) | **re-pinned by this seat**; the round-26 pins and the same-round revision-1 pins are recorded under `supersedes_pins`; the hold rows are unchanged |
| `tools/gates/typed-pipelines.json` profile `d4` (`packet`, `projection`, `expected`) | **re-pinned by this seat**; two new `repin_history` rows record round 27 revisions 1 and 2 with their reasons; the stale projection digests are preserved under `superseded` |
| `reports/round-22/handoff/declared-in-r2/expected.json` — the default `handoff-v3` baseline | **NOT this seat's** — a filed round-22 byte. `V3_BASELINE_DEFAULT` (`tools/exercise-handoff-e2e.py:1933`) still reads it, so `--profile v3 --quiet` now reads `E2E-DIGEST` (exit 1) naming exactly the **five** D4 read-set files this landing moved: `packet.d4.yml`, `packet.d4.typed.yml`, `typed-labels.d4.yml`, `expected-holds.json` and `components/01-brief.yml` (the last added when revision 2 declared the block in the contract). |
| `reports/round-27/pinsweep/**` — the O seat's r27 freeze generations | **NOT this seat's**. Measured: `reports/round-27/pinsweep/baselines/*/r27-post/expected.json` and `v3-baseline-r27/expected.json` pin `packet.d4.yml dd25077bc016…`, i.e. the **pre-landing** packet. |

## 2. The A/B control that attributes the cascade

Asserted attribution is not evidence. Measured, with the landing staged out and
everything else held constant:

```
$ git stash push -- tools/gates/argot-derivation-gate.py \
      examples/culture-d4/{components/01-brief.yml,expected-holds.json,packet.d4.yml,packet.d4.typed.yml,typed-labels.d4.yml} \
      tools/gates/typed-pipelines.json    # + the new component moved aside
$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4
            v2_subset=equal alias_leg=landed packet_sha256=e3fb1ca5…          # exit 0
$ git stash pop && cp .scratch/r27-d/ab2/13-register-law.yml examples/culture-d4/components/
$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=1 … packet_sha256=(not assembled)
FAIL input-digest: examples/culture-d4/components/01-brief.yml: frozen feca7bda25be… live 649aa111db2e…
FAIL input-digest: examples/culture-d4/expected-holds.json:      frozen d6136488e22f… live 857417e949fb…
FAIL input-digest: examples/culture-d4/packet.d4.typed.yml:     frozen 618a78c90fc0… live 1c4b88088b69…
FAIL input-digest: examples/culture-d4/packet.d4.yml:           frozen dd25077bc016… live 86079a6708a0…
FAIL input-digest: examples/culture-d4/typed-labels.d4.yml:     frozen d03f6391fb8d… live 88a94422b412…
handoff-v3: E2E-DIGEST: 5 read-set file(s) changed since the baseline was frozen
```

Pre-landing green, post-landing red, and the red names **exactly** the five D4
read-set files this landing moved. The cascade is attributable to the register
law landing and to nothing else. The A/B was run twice — once at revision 1
(4 files) and once against the final bytes above (5, `01-brief.yml` joining when
revision 2 declared the block in the contract) — and the landing was restored
byte-for-byte after each, verified by `sha256sum` against §3's ledger.

## 3. Why this seat does not re-point the two stale surfaces

- **The filed round-22 baseline** is a filed byte of a round this seat does not
  own. The freeze rule this lane runs on is *supersede-by-new-file*: the
  round-26 seat recorded the same disposition for the same surface
  (`reports/round-26/register/impl.md` §7: "the filed row must be superseded by
  the seat that owns that surface (the O claim's re-point work), not by this
  one").
- **The r27 pinsweep generations** are the O seat's new rows, authored this
  round. They were frozen at pre-landing digests, which is an **ordering**
  hazard — the O seat swept before this landing — not a defect in either seat's
  work. Re-freezing them is a new generation, and the generation is theirs.

Both are reported with their live digests so the owner can act without
re-deriving anything:

```
examples/culture-d4/packet.d4.yml              86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
examples/culture-d4/typed-labels.d4.yml        88a94422b4123f6b436f9935590d69f081f90e688655ee605f33e0c1305fb68d
examples/culture-d4/packet.d4.typed.yml        1c4b88088b696a131f71af69ad14dda518acdec83dc7e873cfcad6fae5fc2660
examples/culture-d4/expected-holds.json        857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f
examples/culture-d4/components/01-brief.yml    649aa111db2e57a737234330690ea4fbb197039ba8ecf92d6248d1bed8ea793b
examples/culture-d4/components/13-register-law.yml  c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
```

## 4. The re-pins, as new rows

Per the round's rule — **pins are new rows, never edits to a filed receipt** —
the two surfaces this seat owns were re-pinned as follows:

- `expected-holds.json`: the new `packet_sha256`/`projection_sha256` are written
  in place (that file *is* the pin), the previous values move into
  `supersedes_pins` (round-26 pair, plus the same-round revision-1 pair, plus the
  earlier round-22 pair), and the `revision_note` names the round, the change,
  the unchanged hold set and the command.
- `typed-pipelines.json`: a **new** `repin_history` entry per revision, each with
  the round, date, the three digests, the adapter digest, a reason and the
  `recorded_in` receipt; the round-26 entry is left in place above it.

The lane runner's own `claim O` measures a related clause — "drifted D4
surface(s) are not re-pinned by a round-27 row carrying the live digest" — and
names `01-brief.yml`, `packet.d4.typed.yml` and `typed-labels.d4.yml` as still
needing a round-27 row on the O seat's surface. That is the same two-owner split
this section records, measured independently by the runner.

## 5. Measured

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
summary: 20/20 legs passed                                     # L4-pins green
$ python3 tools/check-gate-battery.py | tail -6
"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0
```

The battery's committed-baseline duty is green, which is the strongest available
statement that this seat's re-pins did not tamper any *filed* baseline: the
battery verifies every declared input digest against the snapshot bytes inside
each baseline and the `gate_sha256` pin against the live gate script, and reports
`pinned` — not re-executed, and not a silent pass.

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -3
python3 tools/check-gate-battery.py | tail -6
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet; echo "exit=$?"
python3 -c "import json;print(json.load(open('examples/culture-d4/expected-holds.json'))['supersedes_pins'])"
python3 -c "import json;p=json.load(open('tools/gates/typed-pipelines.json'))['profiles'][0];print([r['round'] for r in p['repin_history']])"
```
