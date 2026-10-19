- Seat: C12 | executor | claim C (item 12 of the twelve standing open items) | date 2026-10-19 | baseline 139e3b6

## 1. Item identification (K03's canonical table was not landed at this seat's cut)

`reports/round-33/calib/K03-open-items.md` does not exist at this seat's cut
(`find reports/round-33 -type f` at 2026-10-19T03:52Z lists only `claims.json`,
`targets.json`, `telemetry/dispatch-declared.json`). Item 12 is therefore derived
from the claim-C enumeration in `reports/round-33/claims.json:44`, which names
exactly twelve components in the D13 table's own order:

1. 12 D4 garment-form holds + owed slots · 2. `head2` empty proper domain ·
3. RL-3 register-lexicon ceiling · 4. box-1 citation conditions 2-4 ·
5-8. cold-run N1 / N4 / N5 / N7 · 9. lore-owned (bilateral read + L0 contract
digest) · 10. calibrated numeric rubric · 11. devin availability
could-not-evaluate · **12. r18 D4-adapter baseline supersession semantics** —
the last row of the D13 Decision-4 table
(`reports/round-32/dossier-d13-operator-decisions.md:138`).

**Item 12 as filed:** "r18 D4-adapter baseline supersession semantics (pins
green, content ages)", on record since r31 sweep §5
(`reports/round-31/final-sweep.md:187-190`); owner unassigned by the dossier's
own preamble (`reports/round-32/dossier-d13-operator-decisions.md:125`).

The r31 §5 wording, verbatim: "The D4 adapter baselines were not re-pinned. The
battery verifies their pins (§2, green); whether their *content* still matches
the live packet is the pins' supersession semantics, reported via the control
rows — a successor baseline is the re-pin seat's surface if the round wants one."

## 2. Status quo re-verified at HEAD (all commands dated 2026-10-19, this seat)

HEAD == the round's declared baseline: `git rev-parse HEAD` →
`139e3b662900557afe54f632b468619593dc9fcb`.

**2.1 The r18 generation is internally intact and byte-stable.**
`git status --porcelain -- tools/gates/frozen tools/gates/expected
examples/culture-d4` → empty output (no filed byte moved).
`tools/gates/frozen/round-18/MANIFEST.tsv:2-3` records two rows, both exit 0;
the r18 input snapshots still hash to the recorded digests:
- `sha256sum tools/gates/frozen/round-18/inputs/examples/culture-d4/typed-labels.d4.yml`
  → `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d`
  == `tools/gates/frozen/round-18/freeze-receipt.json:20` (`input_sha256`);
- `sha256sum tools/gates/frozen/round-18/inputs/examples/culture-d4/packet.d4.yml`
  → `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3`
  == `tools/gates/frozen/round-18/freeze-receipt.json:35`.

**2.2 "Content ages" — measured; the live bytes moved.**
`sha256sum examples/culture-d4/typed-labels.d4.yml` →
`c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`;
`sha256sum examples/culture-d4/packet.d4.yml` →
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` — both ≠
the r18 recorded digests above. The control replay at HEAD:

```
TMPDIR=/var/tmp/kotodama-r33-c12 python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv
ROW 2 mismatch reason=replay_mismatch gate=tools/gates/d4-typed-labels-check-gate.py input=examples/culture-d4/typed-labels.d4.yml exit=1/0 count=0/0 bytes=differ launched=yes
ROW 3 mismatch reason=replay_mismatch gate=tools/gates/d4-assembly-check-gate.py input=examples/culture-d4/packet.d4.yml exit=1/0 count=0/0 bytes=differ launched=yes
REPLAY MISMATCH: 2 mismatch, 0 reproduced of 2 row(s) in tools/gates/frozen/round-18/MANIFEST.tsv
exit=1
```

Exit 1 is the **declared expected code**, not a failure:
`reports/round-31/sweep/run-sweep.py:132-133` declares
`("control-round-18", "tools/gates/frozen/round-18/MANIFEST.tsv", 1, "two rows
mismatch: superseded by later D4 landings (recorded reds stay red)")` and
`reports/round-31/final-sweep.md:158` files the same reading.

Cross-run determinism (three independent runs, byte-identical stdout):
this seat's stdout sha256 =
`bd28f916f9aefacb629c915fb9a732e6e58b0c924bd008b0a2e153b93bc23449` == r31's
filed control row (`reports/round-31/sweep/sweep-receipt.json`,
`control-round-18`, `passed: true`, 2026-10-18) == r32's
(`reports/round-32/sweep/receipt-O06.json`, `control-round-18`, `exit_code: 1`,
`expect_exit: 1`, `passed: true`, `2026-10-19T00:58:19Z`).

**2.3 "Pins green" — re-verified.**
`python3 -B tools/check-gate-battery.py` → exit 0, coverage **10/10**, pinned
**20/20**, uncovered none, `unevaluable: 0` (this run). The D4-adapter baselines
inside the battery roots are `tools/gates/expected/d4-assembly-check-gate/r19-pre/`
and `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/`
— every one reads `"reading": "pinned"` with `gate_sha256` match and `stdout_pin`
match. Precise scope note: the r18 generation itself carries no `expected.json`
by design (`tools/gates/frozen/round-18/README.md:49-50`), so "the battery
verifies their pins" means the D4 adapter pins under `tools/gates/expected/`,
not the r18 receipt.

**2.4 A successor-in-substance exists and replays green.**

```
TMPDIR=/var/tmp/kotodama-r33-c12 python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv
REPLAY OK: 4/4 rows reproduced the recorded verdicts (reproduction only: a reproduced red verdict stays red)
exit=0
```

Its rows carry the same two D4-adapter gates at the live digests
(`reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv:2-3`: typed-labels input
`c23b0ab5…`, packet `aac91246c…`), matching the live `sha256sum` readings in
§2.2.

**2.5 The residual gap (why this is not closed).** No filed artifact names the
r18 generation's successor. The r31-post freeze receipt's `supersedes` field
names only r28-post (`reports/round-31/sweep/frozen/r31-post/freeze-receipt.json:84`),
and r31's control table gives r28-post an explicit successor pointer
(`final-sweep.md:167`) while giving r18 only the disposition text
(`final-sweep.md:158`). `grep -rn "frozen/round-18" reports/round-3{0,1,2}/`
returns control rows and digest registries only — no successor naming.

## 3. Disposition

**class: carried-with-owner+reason+next-touch.**

- **owner:** integrator (round-33 integration). The operator owns any decision
  to want a fresh generation instead (r31 §5: "a successor baseline is the
  re-pin seat's surface if the round wants one").
- **reason:** the semantics is by design and re-verified working at HEAD —
  filed bytes are immutable, the control's exit 1 is its declared expected code
  (`run-sweep.py:132-133`), the battery pins are green (§2.3), and a
  successor-in-substance already replays green (§2.4). There is no defect to
  fix; the debt's substance is satisfied and only its naming is missing (§2.5).
- **next_touch:** round-33 integration applies draft **D12-A** (and optionally
  the **D12-B** legs); if declined, the state is safe as-is and the item
  re-carries to the next regimen.
- **class-transition rule for C13/C15:** if the integrator lands D12-A, this row
  flips to `fixed-with-evidence`, with D12-A as the named fix draft and the §2.2
  + §2.4 replays as its verification.

## 4. Bounded fix drafts (integrator-applied; no filed byte rewritten)

**D12-A — successor-naming record (new file, append-only).**
Target: a NEW file `reports/round-33/calib/r18-d4-adapter-successor.md` (created
by the integrator; this seat writes nothing outside its own out path). Draft
body, ready to land verbatim after digest substitution:

```markdown
# r18 D4-adapter baseline — successor named (round-33 disposition of D13 debt 12)

Filed state (unchanged, append-only): `tools/gates/frozen/round-18/MANIFEST.tsv`
pins two rows at recorded exit 0 (typed-labels.d4.yml a59990bb…, packet.d4.yml
e7ecd204…; freeze-receipt.json:20,:35). The live D4 bytes have since moved
(typed-labels c23b0ab5…, packet aac91246c…), so the generation replays exit 1,
2/2 mismatch — its declared expected code (`reports/round-31/sweep/run-sweep.py:132-133`).

Successor: `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` — same two
D4-adapter gates at the live bytes, replay exit 0, 4/4 reproduced
(`TMPDIR=/var/tmp/... python3 -B tools/replay-frozen.py <manifest>`, 2026-10-19).

Semantics restated: a pin is integrity, never truth; a reproduced red verdict
stays red; filed generations are retained as controls, and a successor is a NEW
generation — never an in-place edit. No promotion or clearance verdict is
claimed here.
```

**D12-B — two validator legs for `reports/round-33/run-validation.py`**
(integrator-owned runner), each with the mirror-safe TMPDIR requirement:

```python
("c12-r18-control",  "TMPDIR=/var/tmp/kotodama-r33-replay python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv",      expect_exit=1),  # 2 mismatch, filed reds stay red
("c12-r31-successor","TMPDIR=/var/tmp/kotodama-r33-replay python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv", expect_exit=0),  # 4/4 reproduced
```

## 5. Named finding N-C12-1 (carried, owner: integrator)

**In-repo TMPDIR silently changes the control's code.** Run with
`TMPDIR=$PWD/.scratch` (the lane's usual scratch setting), the *same* r18 replay
command exits **2**, not 1:

```
ROW 2 could-not-evaluate reason=mirror_unsafe ...
ROW 3 could-not-evaluate reason=mirror_unsafe ...
REPLAY COULD-NOT-EVALUATE: 2 could-not-evaluate, 0 mismatch, 0 reproduced of 2 row(s)
exit=2
```

Measured both ways by this seat (2026-10-19). The requirement is documented
(`tools/gates/frozen/round-18/README.md:56-62`); the finding is that a
round-33 validator leg written without an out-of-repo TMPDIR would read exit 2
and mis-file the control. D12-B above therefore pins the TMPDIR explicitly.
Owner: integrator (the runner is integrator-owned); no lane defect in the tool.

## 6. Alternate reading of "item 12" (keep only if K03 canonicalizes otherwise)

If K03's canonical table instead counts the twelve as the nine D13 rows plus
D11's three box-4 standing readings 3a/3b/3c
(`reports/round-32/dossier-d11-shonen-boxes.md:176-181`), then item 12 is
**reading 3c** and the r18 row is item 9. Disposition of 3c at HEAD, so either
mapping yields a valid row (the integrator keeps exactly one):

- **status quo re-verified:** the negative-provenance line still survives
  exactly once in the live projection —
  `grep -c "examples/culture-d2/" examples/culture-d4/typed-labels.d4.yml` → `1`,
  at `examples/culture-d4/typed-labels.d4.yml:165`, and it is self-distinguishing
  ("the D2 leg's examples/culture-d2/components/11-costumes.yml is not read for
  family d4"). 3b's append-only correction stands at `LOG.md:3312` ("Correction
  to the round-22 entry (append-only; the r22 ledger row stands)").
- **class: carried-with-owner+reason+next-touch** — owner: the next adjacency
  re-survey; reason: D11 files 3a/3b/3c as standing readings, not defects, and
  they hold at HEAD; next_touch: the next regimen's box-4 re-survey, with the
  grep above as its counting command.

## Owed

- `reports/round-33/calib/K03-open-items.md` — missing at this seat's cut
  (2026-10-19T03:52Z tree listing). Integrator: confirm item 12's identity and
  order against K03's canonical table; this fragment dispositions both
  candidates consistently (§3 and §6) so either mapping yields one valid row —
  keep exactly one, drop the other.
- `reports/round-33/calib/C01-item-01.md` … `C11-item-11.md` — none exist at
  this cut (`reports/round-33/calib/` was empty), so no duplicate/contradiction
  check against sibling rows was possible here; C13 owns that cross-check.
- `reports/round-33/calib/C15-ledger-draft.json` — row insertion for item 12
  (§3 fields: item/origin/pointer/status_quo_check/disposition_class/evidence/
  owner/reason/next_touch) is the integrator's assembly step, not this seat's.

## Citations

- `reports/round-33/claims.json:44` — the twelve-item enumeration naming "r18 adapter supersession semantics".
- `reports/round-32/dossier-d13-operator-decisions.md:125,138` — Decision 4 preamble (owner unassigned) and the r18 row.
- `reports/round-31/final-sweep.md:158,167,187-190` — control row for round-18; r28-post successor pointer; §5 supersession wording.
- `reports/round-31/sweep/run-sweep.py:132-133` — declared expected exit 1 + disposition text for control-round-18.
- `reports/round-31/sweep/sweep-receipt.json` (control-round-18) and `reports/round-32/sweep/receipt-O06.json` (control-round-18, `exit_code:1`, `expect_exit:1`, `passed:true`, `stdout_sha256:bd28f916…`).
- `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv:2-3`, `freeze-receipt.json:4,7,84`.
- `tools/gates/frozen/round-18/MANIFEST.tsv:2-3`, `freeze-receipt.json:15,20,30,35`, `README.md:9-16,38,49-50,56-62`.
- Commands run 2026-10-19 (this seat, `TMPDIR` as noted): `git rev-parse HEAD`; `git status --porcelain -- tools/gates/frozen tools/gates/expected examples/culture-d4`; `sha256sum` on the three live D4 inputs and the two r18 snapshots; `TMPDIR=/var/tmp/kotodama-r33-c12 python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv` (exit 1; stdout sha256 `bd28f916…`); same with `TMPDIR=$PWD/.scratch` (exit 2, mirror_unsafe); `TMPDIR=/var/tmp/kotodama-r33-c12 python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` (exit 0, 4/4); `python3 -B tools/check-gate-battery.py` (exit 0, 10/10, 20/20 pinned); `ls tools/gates/expected/d4-*`; `grep -rn "frozen/round-18" reports/round-3{0,1,2}/`; `grep -c "examples/culture-d2/" examples/culture-d4/typed-labels.d4.yml` (=1); `sed -n '3308,3316p' LOG.md`; `find reports/round-33 -type f`.
- Alternate-reading sources: `reports/round-32/dossier-d11-shonen-boxes.md:176-181`; `examples/culture-d4/typed-labels.d4.yml:165`; `LOG.md:3312`.
