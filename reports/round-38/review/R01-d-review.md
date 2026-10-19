- Seat: R01 | reviewer | claim D | date 2026-10-19 | baseline 9bccc9b

# R01 — adversarial review of the D block

Write scope: this file only. No tool, gate, packet, component, pin, battery
baseline, or filed byte written; every mutation below was made inside a
`git archive` copy under `.scratch/` and never in-tree. No in-tree
`run-validation.py` was executed (F-C13-1). Measurement stamp
**2026-10-19**, cwd = lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Verdict in one line.** Claim D's `before` is **true** this round (unlike r36's
stale premise) and both residues are **real and reproducible** — but the claim's
`after_required` phrase "filed bytes untouched except the **two named**
tool/example artifacts" is **false as written**: each of the two residues, landed
the way its own spec requires, moves a **third** pinned surface (a new battery
baseline for RL-8; a four-way re-pin for F-6-in-the-coverage-block). The claim
also inherits a vacuous-pass risk on F-6 that no named consumer closes. Review
returns the D block for a scope correction; it does **not** reject the residue
itself.

The D-block fragments do not exist yet at review time (`ls reports/round-38`
→ `claims.json`, `targets.json`, `telemetry/` only). This review is therefore
built entirely from independent measurement of the baseline tree, so the planner
can fold it into P01 before D01/D02 are written.

## 1. The `before` is true — measured, not read

Claim D states the before as "r36 K01: no derived_forms/derived_ok emitter
anywhere in examples/ or tools/; RL-8 era leg missing". Both halves hold at
`9bccc9b`:

```
$ grep -rn "derived_forms\|derived_ok" examples tools
(no output, exit 1)

$ grep -n "derived_pairs" tools/gates/argot-derivation-gate.py
567, 662, 835, 917, 919   # the only counters that exist
```

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14
          derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0

$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 …
          force_failures=0 consequence_failures=0 dangling=0 findings=0
exit 0
```

The era leg is absent by construction: `grep -n "era\|stage\|E0\|E1"` over
`tools/gates/argot-derivation-gate.py` returns only docstring/op-name hits — no
era token is graded; `register-law-gate.py` carries `kind: era` in
`DECLARED_KINDS` (`:121`) but that only *shapes* the row, it does not grade the
dating. `examples/culture-d4/components/13-register-law.yml` says so itself in
its own `enforcement:` field: "The era leg (RGL-05) is specified and
unimplemented — tools/gates/argot-derivation-gate.py has no era concept".

**Positive finding for the planner:** the r36 rejection cause (stale premise) is
not repeated here. The claim's `before` is accurate, and the two residues are the
ones r36 K01 §4 named. Claim D is correctly scoped *in substance*.

## 2. FALSIFIER F1 — the RL-8 era leg is a real hole (reproduced)

I built an isolated archive and injected one E0-dated stamp form (`L-99`,
`term: tuum`, `stage: E0`, `register: stamp`, `derived_from: tum`,
`derivation: {op: lengthen, base: tum}`) that **replays correctly** (so no
`D4L-ARGOT-DERIV` confound — my first probe used a non-replaying form and was
discarded for exactly that reason).

```
# .scratch/r38-r01b, mutated packet only
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … derived_pairs=9 … violations=0 …            exit 0
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … findings=0 …                                exit 0
$ python3 -B tools/gates/costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml
(no findings)                                           exit 0
```

RGL-05's own `consequence` calls an E0 stamp claim "a defect", and its own
`era_rule` is `available_from E1` — yet an E0 stamp form that satisfies every
other leg produces **zero findings from every gate**. The only thing that
noticed the packet change was the typed pipeline's `L1-profile` pin
(`packet: pins aac91246cede, live 512ca5c6dd84`, exit 2) — a *drift* alarm, not
an era check. **F1 confirms the residue is real and worth landing.**

## 3. FALSIFIER F2 — landing the era leg moves a third pinned surface

The claim's `after_required` says "filed bytes untouched except the two named
tool/example artifacts". The RL-8 leg lives in `register-law-gate.py`, which is
**pinned by digest in the gate battery**:

```
$ sed -n '1,12p' tools/gates/expected/register-law-gate/r30-post/expected.json
  "gate_sha256": "15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169",
  "tools/gates/register-law-gate.py": "15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169"
```

I perturbed one line of `register-law-gate.py` in a fresh archive (the D02
landing, simulated) and ran the battery live:

```
$ python3 -B tools/check-gate-battery.py
baselines.summary: {"baseline_exit": 2, "pinned": 19,
                    "readings": {"gate_revised": 1, "pinned": 19}, "unevaluable": 1}
finding: {"id": "BASELINE-GATE-REVISED", "state": "gate_revised",
          "detail": "gate_sha256 15f8b23251ca2ad0... differs from the live
                     register-law-gate.py 65e5638cf164cff7...:
                     re-freeze, never compare across an unnamed revision"}
exit 2   (was exit 0)
```

**Control, run in the same environment to rule out a confound.** The archive
omits the gitignored `run.log` files, which the battery reads for `stdout_pin`.
An *unmodified* archive run in the same run.log-less state is clean:

```
# .scratch/r38-r01f, unmodified archive
$ python3 -B tools/check-gate-battery.py
baselines.summary: {"baseline_exit": 0, "pinned": 20, "unevaluable": 0}
exit 0
```

So the exit 0→2 flip is driven **solely** by the `gate_sha256` pin, not by the
absent `run.log`. **F2: D02's landing requires a new battery baseline under
`tools/gates/expected/register-law-gate/` — a third artifact the claim's "two
named" list omits.** This is a re-freeze of a *battery baseline*, not of the
pinned r7 row, so it is permitted by the non_goals — but it must be *named* in
`after_required` and in D04's pin plan, or the landing will leave the battery at
exit 2 and the round cannot be admitted.

## 4. FALSIFIER F3 — F-6 is reachable two ways, and they are not equivalent

The forecast's F-6 is verbatim: "the **coverage block reports** `derived_forms`
and `derived_ok` counts that agree" (`reports/round-25/argot/forecast.md:40`).
The coverage block lives in `examples/culture-d4/typed-labels.d4.yml:28-47`
(`typed_labels: 82`, `labels_by_kind`, …), which is **pinned in four live
places**:

```
examples/culture-d4/expected-holds.json:4   "projection_sha256": "c23b0ab532cf…"
examples/culture-d4/packet.d4.typed.yml:2870 projection_sha256: "c23b0ab532cf…"
tools/gates/typed-pipelines.json:21         "sha256": "c23b0ab532cf…"
tools/exercise-handoff-e2e.py  V3_READ_SET    (member) + r7 expected.json inputs (member)
```

I tested both routes in isolated archives.

**Route A — coverage block (the forecast's literal ask).** Adding
`"derived_forms": 8, "derived_ok": 8` beside `"typed_labels": 82`:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=1
handoff-v3: E2E-DIGEST: examples/culture-d4/expected-holds.json projection_sha256:
            the tree recorded c23b0ab532cf… but the bytes measure f9eb292b19ee…

$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
FAIL L1-profile: projection: pins c23b0ab532cf, live f9eb292b19ee    exit 2
```

**Route B — stdout only (the "documented equivalent").** Renaming the argot
gate's own print to `derived_forms=%d derived_ok=%d`:

```
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14
          derived_forms=8 derived_ok=8 claimed_chains=8 borrow_pairs=6 violations=0
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet      exit 0
$ python3 -B tools/gates/typed-pipeline-gate.py …  summary: 20/20 legs passed  exit 0
$ python3 -B tools/check-gate-battery.py --selftest  SELFTEST OK 44/44        exit 0
```

**F3: the two routes are not equivalent, and the claim conflates them.**
- Route A meets the forecast's wording but is a **re-pin cascade**:
  `typed-labels.d4.yml`, `expected-holds.json`, `packet.d4.typed.yml`,
  `typed-pipelines.json` (and a new pin generation) all move. "Filed bytes
  untouched except the two named artifacts" is false under Route A.
- Route B is pin-safe (verified: no v3/pipeline/battery movement) but does
  **not** satisfy the forecast's "coverage block" wording — it is a divergence,
  and r26's own precedent (`execution-3.md:74`) is that such a divergence must
  be **named as a divergence**, not silently claimed as F-6 closure.

The claim's parenthetical "(or a documented equivalent the legs can count)"
points at Route B, and the argot gate is **not** in `V3_READ_SET`, **not** in
`GATE_NAMES`/`D4_GATE_NAMES`/`REGISTER_LAW_GATE_NAMES` (`check-gate-battery.py:117-132`),
and **not** digest-pinned anywhere live (`grep -rn b5406bcd examples tools` → no
match). So Route B is genuinely free. **The D block must choose one route and
state it; "or a documented equivalent" cannot cover both.**

## 5. FALSIFIER F4 — the F-6 numbers are a relabel, and the pass can be vacuous

The counters already exist under other names: `derived_pairs=8`,
`violations=0`. So `derived_forms`/`derived_ok` = `derived_pairs` /
`derived_pairs - violations` = **8 / 8**. Two vacuous-pass hazards follow, both
of which the claim's threshold ("the new coverage named (no vacuous-pass)")
requires the D block to close:

1. **No consumer exists.** Nothing in `examples/` or `tools/` reads a
   `derived_forms`/`derived_ok` key — `grep -rn "derived_forms\|derived_ok"
   examples tools` → no match at baseline. A key that is emitted and read by
   nothing is *present*, not *consumed*. This is exactly the guard D10b is
   assigned ("consumed by the argot leg (not just present)") — **D10b must
   demand a named reader, or the emission is decoration.**
2. **"counts that agree" is vacuous over `violations=0`.** Over the delivered
   tree `derived_forms == derived_ok` trivially (8 == 8), which is F-5
   restated. "Agreement" only carries information if a control proves the two
   can **disagree**. The D block must land a control (a mutated packet where
   `derived_ok < derived_forms`) and pin the disagreeing reading, or F-6 adds
   no discriminating power over the `violations` counter that already exists.

## 6. Points the D block should carry into D01/D02/D03/D04/D10b

- **`head2` is out of this claim.** Claim D is only (a) F-6 counters, (b) RL-8
  era leg. `head2`'s empty proper domain is `OI-02` and stays carried — do not
  let D08 "gap-fill" absorb it as new depth; that would be scope bleed.
- **Baseline before→after is already measurable and honest**: `derived_pairs=8
  violations=0` / `findings=0`, both exit 0 (verified twice above). The
  *after* must show a **new** coverage name and a **new** era finding on a
  tampered control — not a re-print of the same numbers.
- **Three independent verifiers are named** (D03, D05, D10b); the threshold is
  met *only if* D10b's consumer check is real (see §5.1).
- **`python3 reports/round-38/run-validation.py` does not exist yet**
  (`ls reports/round-38/run-validation.py` → No such file). The claim's third
  counting command is `to-verify` until the integrator lands it, and it must
  never be run in-tree (F-C13-1) — isolated `git archive` copies only.
- **The r7 packet digest is unchanged** at review time:
  `sha256sum reports/round-34/handoff/declared-in-r7/packet.md` →
  `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, matching
  the claim's `thresholds`. No re-freeze occurred and none is owed this round.

## Owed

- **Planner (P01):** correct the D claim's `after_required` to name the **third**
  artifact — a new `tools/gates/expected/register-law-gate/` battery baseline —
  and to fix the F-6 route (Route A re-pin vs Route B stdout divergence) as a
  named choice, per §3–§4. Owner: P01.
- **D02:** landing the era leg must include the battery-baseline re-freeze, or
  `check-gate-battery.py` stays exit 2 and the round cannot be admitted (§3).
- **D01/D10b:** if Route B is chosen, name the reader (the "consumed" leg) and
  the disagreeing control; if Route A, enumerate the four-file re-pin (§4–§5).
- **Integrator:** land `reports/round-38/run-validation.py`; it is `to-verify`
  for this seat and must not be run in-tree.
- **Not measured by this seat:** the D-block fragments themselves (absent at
  review time), so this review does not adjudicate D01/D02's design details —
  only the claim's scope and the two residues' falsifiability.

## Citations

Files (sha256 measured 2026-10-19, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/expected/register-law-gate/r30-post/expected.json#gate_sha256
```

Commands run (all from lane root, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; every mutation inside `.scratch/r38-r01{,b,c,e,f}`,
a `git archive HEAD` copy):

```
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml      # exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest                         # 27/27
python3 -B tools/gates/register-law-gate.py --selftest                             # 45/45
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml    # 20/20
python3 -B tools/assemble-culture-d4.py --check                                    # byte-identical
python3 -B tools/assemble-d4-typed.py --selftest                                   # 12/12
python3 -B tools/check-gate-battery.py --selftest                                  # 44/44
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                      # exit 0, 45f57132
grep -rn "derived_forms\|derived_ok" examples tools                               # no match, exit 1
# isolated probes (archives):
#   r38-r01b  E0 stamp form injected  -> argot/law/costume-era all exit 0
#   r38-r01c  F-6 keys in coverage block -> v3 exit 1 (E2E-DIGEST), pipeline L1-profile FAIL
#   r38-r01d  argot stdout renamed -> v3 exit 0, pipeline 20/20, battery 44/44
#   r38-r01e  register-law-gate.py perturbed -> battery exit 2, BASELINE-GATE-REVISED
#   r38-r01f  unmodified archive -> battery exit 0 (control)
```

Source lines cited: `reports/round-25/argot/forecast.md:40` (F-6 verbatim);
`reports/round-26/register/execution-3.md:74` (F-6 "not designed");
`reports/round-26/register/rules.md:128` and `reports/round-27/law/impl-8.md:68`
(RL-8 specified/unimplemented); `reports/round-36/scout/K01-register-scout.md:103-139`;
`reports/round-36/validation.json:49-60`; `examples/culture-d4/components/13-register-law.yml`
(`enforcement:`, `era_rule`); `examples/culture-d4/packet.d4.yml:2788-2880`;
`examples/culture-d4/typed-labels.d4.yml:28-47`;
`tools/gates/register-law-gate.py:114-122`;
`tools/gates/argot-derivation-gate.py:567,662,917-919`;
`tools/check-gate-battery.py:117-132`; `tools/gates/typed-pipelines.json:15-40`;
`tools/gates/expected/register-law-gate/r30-post/expected.json:10,20`.
