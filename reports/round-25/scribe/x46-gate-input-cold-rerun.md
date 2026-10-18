# Round 25 — SCRIBE X46 — independent cold re-run of the gate-input fix

- **Seat:** SCRIBE X46, round 25. Claim **O / operability**, tail (a)
  ("gate-input honesty"), per `reports/round-25/claims.json`.
- **Assignment:** independent cold re-run of the gate-input fix — typed packet
  in, source packet in.
- **Date:** 2026-10-18. Commands run 17:24–17:38Z (`python3` 3.14.7,
  `/usr/bin/python3`), `export TMPDIR=$PWD/.scratch` before every
  scratch-writing command; scratch under `.scratch/x46/` (gitignored).
- **Baseline binding:** declared baseline
  `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` (`claims.json:5`); lane HEAD at
  this seat's runs `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this fragment only, plus `.scratch/x46/`. No tool, packet,
  pin, validator or shared-bookkeeping edit; no Git mutation, commit or push;
  no filed round-8–24 byte written. `tools/gates/typed-pipeline-gate.py` was
  **read only** throughout — this seat did not edit it (the O-seat did).

## 0. Headline

**The fix landed mid-run and this seat verified the shipped tool, not a draft.**
The gate was rewritten under this seat between 17:31:08Z and 17:34Z: I measured
**five** digests in that window (`04ad4bb4…` → `6e3b66c6…` → `ec65d655…` →
`36b56392…` → `a6e8d9c8…` → `879d40bf…`). Every post-fix number below is pinned
to the settled revision **`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`**,
which was byte-stable across four samples spanning 17:35:49–17:36:49Z.

**Result:** the typed-packet false red is gone and the source-packet entry is
intact. Independently reproduced, on the shipped bytes:

| Input class | Live gate (pre-fix `04ad4bb4…`) | Shipped gate (`879d40bf…`) |
|---|---|---|
| source packet `examples/culture-d4/packet.d4.yml` | **0, 19/19** | **0, 19/19** |
| derived packet `examples/culture-d4/packet.d4.typed.yml` | **1, 14/16** | **0, 16/16** |
| flagless (D2 default) | 0, 16/16 | **0, 16/16** |
| `--selftest` | 0, 12/12 | **0, 19/19** |

The claim's own counting command now reads the gate-input tail **green** — see §5.

## 1. Pre-fix baseline reproduced cold (17:24–17:30Z, gate `04ad4bb4…`)

| # | Command | Exit | Legs |
|---|---|---|---|
| B1 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 19/19 |
| B2 | `… examples/culture-d4/packet.d4.typed.yml` | **1** | **14/16** |
| B3 | `…` (flagless) | 0 | 16/16 |
| B4 | `… --selftest` | 0 | 12/12 |

B2 carried **8** `DERIV-REPLAY` FAIL lines (`NM-01`…`NM-08`, "rule 'CX-01' does
not apply to stem 'tum+hai' …") and **6** phantom `'null'` routing rows. The
digest `04ad4bb4…` is the `round-22/d4-repin` MANIFEST gate pin, so this was a
live defect on the frozen revision, not a drifted working copy.

## 2. Root causes re-derived independently (not inherited from the O-seat)

### 2.1 The manufactured `DERIV-REPLAY` class, proved at the byte level

Rather than trust the O-seat's hand-rebuild, this seat **instrumented a scratch
copy of the gate** (`.scratch/x46/tree2/`, one added `write_bytes`, no logic
change) to dump the legacy bytes its own typed-input path actually builds, then
ran the naming gate on those bytes:

| Input to `naming-collision-gate.py` | Exit | `DERIV-REPLAY` lines |
|---|---|---|
| committed source `packet.d4.yml` | 1 | **0** |
| committed typed `packet.d4.typed.yml` | 1 | **0** |
| **the gate's own rebuilt legacy bytes** | 1 | **8** |

Neither committed packet emits the class; only the gate's internal rebuild does.

**Cross-check.** My dump hashes
`182f07b9229a44a83ad837df347341be0cd6fcc631e374227fe1376dff1c165e`; the O-seat's
independently derived `.scratch/r25-o1/rebuilt-legacy.yml` hashes the **same**
digest (`cmp` → silent). Two different derivations, byte-equal output.

**The mechanism, with a control.** The rebuild re-escapes one regex:

| file | `morphology.derivation_rules[CX-01].pattern` | value the lane reader resolves |
|---|---|---|
| `packet.d4.yml` | `"^(?P<a>.+)\\\\+(?P<b>.+)$"` | `^(?P<a>.+)\+(?P<b>.+)$` |
| gate rebuild | `"^(?P<a>.+)\\\\\\\\+(?P<b>.+)$"` | `^(?P<a>.+)\\+…` (one backslash too many) |

```
re.match('^(?P<a>.+)\\+(?P<b>.+)$',   'tum+hai') → match,  a='tum' b='hai'
re.match('^(?P<a>.+)\\\\+(?P<b>.+)$', 'tum+hai') → no match
```

The doubled escape makes `\+` a literal backslash-plus, so the rule genuinely
cannot apply and `naming-collision-gate.py:1483` emits `DERIV-REPLAY` for all
eight `CX-01` names. Rebuild cost: 2676 committed lines → 2343, 19 diff hunks,
352 changed lines (also `null` → `"null"` ×3, `false` → `"false"`).

### 2.2 The phantom slots

Six costume routing rows carry an unquoted `owed_slot: null`, which the lane
reader keeps as the four-character string `'null'` (truthy). The pre-fix
`routed_slots` (`:748-749`) tested bare truthiness and omitted the null-ish guard
`moved_field()` already had, so six phantom slots entered the comparison.

## 3. The shipped fix — what actually landed, and how it differs from the filed design

The O-seat's `design.md` proposed a two-part patch (read `config["packet"]`; add
`nullish()`). **The shipped tool is a third variant** — worth naming because the
leg count is a visible contract:

- **L3 (as designed):** a `nullish()` predicate now backs both `moved_field` and
  a new `owed_slot_of()`; `routed_slots` reads through it.
- **L2 (redesigned):** instead of reading `config["packet"]`, the gate reads the
  source the typed packet **declares** under `typed_assembly.packet`, digest-
  checked against the typed packet's own `assembly.packet_sha256`, with a
  four-way precedence and a **named `input_class`** reported in `--json`:
  `source` / `typed-declared-source` / `typed-unresolvable` (exit 2) /
  `typed-stale-source` (exit 2) / `typed-rebuilt` (fallback + fidelity check).
  This is the claim's **first** branch — "a named input-class diagnostic" — not
  the second.
- An intermediate revision briefly added a 17th leg `L2-legacy-source` (typed
  path 17/17); the settled revision folds that into `L2-channel` and is back to
  16 legs on the typed path.

Measured on the shipped bytes: `--json` reports
`{"exit_code": 0, "input_class": "typed-declared-source", "ok": true}` for the
typed packet and `"input_class": "source"` for the source packet.

## 4. Independent verification of the shipped fix

### 4.1 The false red is gone, with the diagnostic detail

Typed run, shipped gate: exit **0**, **16/16**, `DERIV-REPLAY` lines **0**,
`'null'` rows **0**, all 16 legs `ok` (including `ok L2-channel` and
`ok L3-routing-consistency`), `channel: 6 PHON artifact(s) retired, 0 added,
retained lines identical` — the six real field moves and nothing else.

The two new fail-closed diagnostics, exercised by this seat by editing a copy of
the typed packet's `packet_sha256` pin (not by reading the O-seat's fixture):

- stale pin → exit **2**;
- declared source unreadable → exit **2**;
- healthy typed packet (control) → exit **0**.

### 4.2 Behaviour preservation, byte-level (this seat's own runs)

| # | Path | Shipped exit | Byte check |
|---|---|---|---|
| P1 | source packet | 0, 19/19 | stdout sha `b064da28…` = the `round-22/d4-repin` `output_sha256` pin — **match** |
| P2 | flagless D2 default | 0, 16/16 | stdout **byte-identical** (`cmp`) to the pre-fix run |
| P3 | `--selftest` | 0, 19/19 | grew from 12/12 — the fix **added** controls (null-ish truth table, phantom-slot control, declared-source-leg control, input-class controls) |
| P4 | `--selftest-generalized` | 0, 14/14 | unchanged |
| P5 | D2 typed direction | 0, 13/13 | stdout sha `9a69985a…` — **byte-identical** to the filed `round-23/repin-d2/typed-pipeline.out` frozen row |

P1 and P5 are the strong ones: the fix reproduces two filed frozen pin digests
exactly, so it moved no legitimate verdict.

### 4.3 It still fails closed — controls this seat authored

Built from the committed packets with my own edits, run against the shipped gate:

| # | Control | Exit | What fires |
|---|---|---|---|
| C-1 | one routing row deleted (structure intact) | **1** | `FAIL L3-routing-consistency` (holds 12 vs routed 11) |
| C-2 | `owed_slot: "LEX-GAR-99"` smuggled onto the slot-less `GAR-01` row | **1** | `FAIL L3-routing-consistency` — `routed` gains `LEX-GAR-99`; the filter is **not** an amnesty |
| C-3 | `GAR-01`'s moved field renamed back on-channel, routing still claims the move | **1** | `FAIL L2-channel — off-channel lines in the typed run: … GAR-01 …` (the honest diagnostic; pre-fix this input also emitted the manufactured class) |
| C-5 | source packet with its six holds laundered to notes | **2** | `FAIL L1-assembler` — bytes `5c45ba35…` ≠ the assembler's deterministic `e7ecd204…` |

### 4.4 Named residuals (pre-existing; reproduced, not introduced by the fix)

`hold: null` and an absent `hold` key on a moved slot row both leave the shipped
gate at exit 0/16-16 — my R-1/R-2 controls confirm the O-seat's §5.4 R1/R2. They
are gaps on the **source** path too (the source run is 19/19 with the same code),
so the claim's "fails closed and honestly" clause must not be read as "the L3 leg
is now sound".

## 5. The claim's counting command

`reports/round-25/run-validation.py` refuses to run outside an isolated clone, so
this seat built one under `.scratch/x46/clone` (`git clone --shared`), copied the
live round-25 surface in, and ran the documented command
`python3 reports/round-25/run-validation.py --check` (2026-10-18, exit 1):

- **claim O — `gate_input_honesty`: all checks pass.** source `exit 0, 19/19`;
  derived `exit 0, 16/16, failed_legs: []`; `deriv_replay_lines: 0`;
  `nullish_routing: false`; corrupted-packet control `exit 2`; tampered-
  expectation control `exit 1`.
- claim O's **only** failure is the sibling tail: `v3-supersession: D2-CL01
  carries undispositioned passenger prose (15 hold-or-fail)` — **not** the
  gate-input tail this seat was assigned.
- claims **C** and **D** passed at that measurement (`passed=True`, 0 failures).

So the gate-input tail of claim O is independently green; the round as a whole is
not, on the v3-supersession half.

## 6. Pin cascade — measured, resolved by new rows

The gate is sha-pinned by four earlier-generation manifests. Moving its digest
makes exactly one row in each refuse:

| Manifest | Before (gate `04ad4bb4…`) | After (gate `879d40bf…`) | Refused row |
|---|---|---|---|
| `round-18/repin-d2` | 0, 11/11 | **2**, 10/11 | the round-11 typed snapshot |
| `round-20/repin-d2` | 0, 11/11 | **2**, 10/11 | same snapshot |
| `round-22/d4-repin` | 0, 3/3 | **2**, 2/3 | `examples/culture-d4/packet.d4.yml` |
| `round-23/repin-d2` | 0, 11/11 | **2**, 10/11 | the D2 typed packet |

Reason on every refused row: `gate_digest_mismatch — gate: on-disk bytes are not
the pinned revision`.

**Control (this seat).** Replaying the same four manifests against a tree whose
gate differed by one added line collapsed all four to exit 2 *before* the fix —
so the cascade is mechanical, not incidental.

**Resolution is in place:** `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv`
adds **6 new rows** (4 input-class rows + 2 fail-closed control rows), all
pinning `879d40bf…`. I replayed it: **exit 0, 6/6 reproduced, 0 mismatch, 0
could-not-evaluate.** No historical manifest was edited.

**Two failures that must NOT be misread as fix regressions** (both pre-existing,
measured on both revisions):

- `round-18/MANIFEST.tsv` → exit 1, `replay_mismatch` on the
  `d4-typed-labels-check-gate.py` row (superseded by the round-22 family-clean
  re-pin; its successor lives in `round-22/d4-repin`).
- `round-11/MANIFEST.tsv` → exit 2, `gate_digest_mismatch` on its
  `typed-pipeline-gate.py` row, which pins the **pre-repin** gate `d102fd1d…`.

**Restore recipe independently confirmed:** `git show f74fc94:tools/gates/typed-pipeline-gate.py`
hashes exactly `04ad4bb4…`, the predecessor digest.

## 7. Regression sweep (shipped gate, 17:35:04–17:35:20Z)

All green: battery 0 · `assemble-d2 --check` 0 · `assemble-culture-d4 --check` 0 ·
`assemble-d4-typed --check` 0 · `d2-typed-labels --selftest` 163/163 · gate D2
16/16 · gate D4 source 19/19 · gate flagless 16/16 · gate `--selftest` 19/19 ·
`--selftest-generalized` 14/14 · handoff v3 0 · `replay-frozen --selftest` 79/79.
Documented reds reproduce as expected (round-3 live replay exit 2, 7/7
`gate_digest_mismatch`). Full transcript `.scratch/x46/postfix-sweep.txt`.

## 8. Findings for the parent

**X46-F1 (minor, PRE-EXISTING — not introduced by this fix; on the assigned
surface, so reported).** The gate raises an **uncaught `KeyError: 'record'`
traceback** instead of a clean exit 2 when a typed packet (a) carries **no
declared source** — so the rebuild fallback runs — and (b) has a `typed_channel`
row lacking its `record` key. `tools/gates/typed-pipeline-gate.py:671` indexes
`row["record"]` directly.

- Reproduced on the **shipped** gate (`879d40bf…`): exit 1 + traceback.
- Reproduced identically on the **predecessor** (`04ad4bb4…`, line 593) — so it
  is pre-existing, not a regression.
- It contradicts the tool's own documented contract (docstring: "2 =
  could-not-evaluate (… malformed packet, **gate traceback** …)") and its
  selftest claim `ok malformed packet: exit 2, no traceback` — the selftest's
  malformed control is unparseable YAML (`:1131`), which exits 2 cleanly; the
  *semantic* malformation is untested.
- **Not reachable from any committed artifact**: with a declared source present
  the leg returns before the loop, and the two committed packets are well-formed.
  This seat's first attempt to hit it was caused by its own editing bug, which is
  why it is filed as minor with the exact reproduction rather than as a break.
- Suggested control for a future round: a typed packet with no `typed_assembly`
  block and one routing row missing `record` must exit 2 without a traceback.

**No other new defects found.** The typed-input false red is fixed, the source
entry is unchanged, the teeth are intact, and the pinned generations resolve by
new rows.

## 9. Limits

- The fix was **being written while this seat verified it**; five digests were
  observed. All post-fix numbers are pinned to `879d40bf…`, stable across four
  samples over ~60 s, but a later edit would invalidate them (the new frozen rows
  would refuse with `gate_digest_mismatch`, which is intended behavior).
- The validator run in §5 used a clone whose working tree this seat populated
  from the live tree; `v3-supersession` and the parent's acceptance run are
  outside this seat's assignment.
- Repeated sampling cannot prove the gate bytes were never momentarily changed
  between samples.
- §4.4 residuals and §8 F1 are **named, not fixed** — fixing either would move
  the pinned digest again.

## 10. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
G=tools/gates/typed-pipeline-gate.py
sha256sum $G    # 879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126

python3 $G examples/culture-d4/packet.d4.yml            # 0, 19/19
python3 $G examples/culture-d4/packet.d4.typed.yml      # 0, 16/16, 0 DERIV-REPLAY
python3 $G examples/culture-d4/packet.d4.typed.yml --json | head -6   # input_class
python3 $G --selftest                                   # 0, 19/19

python3 .scratch/x46/rebuild-probe.py    # independent rebuild of the legacy bytes
python3 .scratch/x46/x46-controls.py     # C-1/C-2/C-3/C-5 + R-1/R-2 residuals
cmp .scratch/x46/gate-legacy-rebuild.yml .scratch/r25-o1/rebuilt-legacy.yml   # silent

for m in round-18/repin-d2 round-20/repin-d2 round-22/d4-repin round-23/repin-d2; do
  TMPDIR=/tmp python3 tools/replay-frozen.py tools/gates/frozen/$m/MANIFEST.tsv | tail -1
done                                                     # each: 1 refused row
TMPDIR=/tmp python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv | tail -1
                                                         # REPLAY OK: 6/6

# X46-F1
python3 - <<'EOF'
import pathlib, re, subprocess, sys
t = pathlib.Path("examples/culture-d4/packet.d4.typed.yml").read_text()
t = re.sub(r"^typed_assembly:\n(?:[ \t].*\n|\n)*", "", t, count=1, flags=re.M)
t = t.replace('  -\n    record: "LEX-GAR-06"\n', '  -\n', 1)
p = pathlib.Path(".scratch/x46/f1.yml"); p.write_text(t)
r = subprocess.run([sys.executable, "tools/gates/typed-pipeline-gate.py", str(p)],
                   capture_output=True, text=True)
print("exit", r.returncode, "| traceback:", "Traceback" in r.stderr,
      "|", (r.stderr.strip().splitlines() or [""])[-1])
EOF
# → exit 1 | traceback: True | KeyError: 'record'   (expected: exit 2, no traceback)
```

FILES: reports/round-25/scribe/x46-gate-input-cold-rerun.md, .scratch/x46/rebuild-probe.py, .scratch/x46/x46-controls.py, .scratch/x46/postfix-sweep.sh, .scratch/x46/regress.sh, .scratch/x46/verify.sh, .scratch/x46/watch.sh, .scratch/x46/watch2.sh, .scratch/x46/watch3.sh, .scratch/x46/stabilize.sh (scratch is gitignored, lane-internal)

SUMMARY: Independently re-ran the gate-input fix on both input classes — the false red is gone on the shipped gate (`879d40bf…`: typed 14/16→16/16, 0 manufactured findings, 0 phantom slots) while the source entry stays 19/19 and all pinned digests, controls and the pin cascade check out; I re-derived both root causes (my instrumented dump of the gate's own rebuilt bytes is byte-identical to the O-seat's) and filed one new minor pre-existing finding: an uncaught `KeyError: 'record'` traceback at `:671` instead of exit 2 when a typed packet has no declared source and a routing row lacks `record`.
