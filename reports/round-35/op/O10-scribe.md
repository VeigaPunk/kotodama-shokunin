- Seat: O10 | scribe | claim O | date 2026-10-19 | baseline 4a7aede

# O10 — landed-changes material for the fleet report (claim O)

Written 2026-10-19T08:17Z from the pre-edit tree: HEAD `4a7aede`, worktree
clean apart from `reports/round-35/**`. At write time no O-block dependency
fragment existed (`reports/round-35/` held only `claims.json`, `targets.json`,
`telemetry/`), so **nothing in the "after" column below is an observed
landing** — each after-value is the declared requirement, marked `owed` with
the fragment that must supply it. The integrator fills the after-column from
O01/O03/O05 (drafts + isolated observations); S02's receipt (landed at fold
time) supplies only the before-state and the leg list, and the round reports
claim O unlanded if the patch fragments are absent at close.

## Before state (measured at 4a7aede)

**The defect, reproduced (R34-N1).**

Command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
--baseline reports/round-30/handoff/declared-in-r6/expected.json`

Observed (2026-10-19T08:15Z): exit **1**, stderr traceback, final frames
`File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise` /
`KeyError: 'reports/round-20/handoff/claims-map.md'`. No summary line, no
named diagnostic.

Mechanism, in two lines:
- `tools/exercise-handoff-e2e.py:3819` — `drifted = [rel for rel, digest in
  baseline["inputs"].items() if assembly.digests.get(rel) != digest]`: the
  `.get` yields `None` for a baseline member absent from the live read set, so
  that member enters `drifted` (the refusal is correct).
- `tools/exercise-handoff-e2e.py:3822` — the record call then indexes
  `assembly.digests[rel][:12]` for that same member and raises the `KeyError`.

This breaks the renderer's own documented contract at
`tools/exercise-handoff-e2e.py:89`: "Exit codes (stable messages, no
traceback)".

**Why the r6 member is unresolvable (read-set arithmetic, measured).**

| quantity | value | source |
|---|---|---|
| r6 baseline `inputs` | 58 files, incl. `reports/round-20/handoff/claims-map.md` | `reports/round-30/handoff/declared-in-r6/expected.json` (measured) |
| live `V3_READ_SET` | 58 files, carrying `reports/round-34/handoff/declared-in-r7/claims-map.md` | `tools/exercise-handoff-e2e.py:1935-1958`, constant at `:184` |
| r6-only member | `reports/round-20/handoff/claims-map.md` | measured set difference |
| r7-only member | `reports/round-34/handoff/declared-in-r7/claims-map.md` | measured set difference |
| shared members | 57 | measured set difference |

The round-20 map still exists on disk (24,888 bytes, `reports/round-20/handoff/`)
— the member is unresolvable because the live read set no longer carries it,
not because the file is missing. The r6 row's own refusal is intended
(`repin.json:16-22`); what is missing is the name.

**Diagnostic vocabulary at baseline** (`tools/exercise-handoff-e2e.py:89-93`):
exit 1 — `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC`,
`E2E-LINK`; exit 2 — `E2E-ARTIFACT`, `E2E-BASELINE`, `E2E-DATA`. `grep -c
E2E-READSET tools/exercise-handoff-e2e.py` → **0**: the code claim O prefers is
new; if the landing mirrors an existing code instead, the fleet-report material
must name which one and why.

**Controls and chains at baseline (all re-measured 2026-10-19T08:15-08:17Z).**

| leg | command | observed at 4a7aede |
|---|---|---|
| v1 selftest | `python3 -B tools/exercise-handoff-e2e.py --selftest` | exit 0, "positive run … plus **17 controls**" |
| v3 selftest | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 0, "positive run … plus **39 controls**" (40 bullet lines counted) |
| r7 default chain | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f57132…` |
| r6 row replay | `… --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, unhandled `KeyError` (above) |

**Pinned before-values (sha256).** Renderer `tools/exercise-handoff-e2e.py`
`34c85f57…` (identical to `git show 4a7aede:tools/exercise-handoff-e2e.py |
sha256sum`); r6 baseline `ea1e2927…`; r7 baseline `bbe15887…`; r7 `packet.md`
`45f57132…`; r7 `freeze.txt` `3969954b…`; r7 `claims-map.md` `d181de28…`. The
r6 row pins packet `6ced88ad…` against the live `45f57132…` — a second,
independent reason the r6 replay cannot pass, and part of the intended refusal.

## Landed-changes ledger (after-column owed)

| surface | before (4a7aede) | after (owed) | owed from |
|---|---|---|---|
| `tools/exercise-handoff-e2e.py:3819-3822` — catch site | unhandled `KeyError`, traceback, no name | named diagnostic (`E2E-READSET` or the named alternative) carrying `reports/round-20/handoff/claims-map.md`, exit 1, no traceback | O01 (draft), O03 + O05 (isolated observation, independent) |
| `tools/exercise-handoff-e2e.py` — `v3_selftest` control matrix (insertion beside the m12 controls at `:4414-4430`) | 39 controls | 41 controls: (a) superseded-row named refusal, (b) preserved `E2E-DIGEST` tamper leg | O02, O03 |
| `tools/exercise-handoff-e2e.py` — v1 twin site `:1435-1440` | same `.get`-then-index pattern | decision recorded (fixed, or deliberately out of scope with reason) | O01, R04 |
| renderer digest | `34c85f57…` | new digest recorded as a **new** repin row (the r34 row's `surface_sha256_after` at `reports/round-34/handoff/repin.json:11` is a filed reading, never edited) | integrator |
| `reports/round-35/run-validation.py` | absent | per-claim legs per the spec below | S04, integrator |
| `SCORECARD.md` operability row | r34 row at `SCORECARD.md:616` | r35 row with the measured before→after | integrator |

Nothing else may move: no `--freeze` of `declared-in-r7` (its bytes are pinned;
`claims.json` non_goals), no corpus or `tools/harness/**` edits, and
`reports/round-30/handoff/declared-in-r6/**` stays byte-identical
(`repin.json:4`, `:16-22`).

## Paste-ready fleet-report block (after-values are `⟨owed: …⟩` until filled)

### Landed changes (claim O)

- `tools/exercise-handoff-e2e.py` — the v3 read-set refusal now names the
  unresolvable member instead of dying in `KeyError`: sha256 `34c85f57…` →
  `⟨owed: O03/O05, measured sha256⟩`; selftest `⟨owed: N controls, from O03⟩`
  (baseline 39); the r7 default chain unchanged (exit 0, packet `45f57132…`).
- `reports/round-35/op/` — patch draft (O01), control designs (O02), isolated
  verification (O03/O05), operability receipt (O06/S02).
- Filed bytes: zero writes to `reports/round-1..34/**`,
  `corpus/lessons/*.md`, `tools/gates/frozen/**`, and no `--freeze` run this
  round; the r6 row stays untouched (`⟨owed: O03/O05 preservation count⟩`).

### Before → after measurements (operability)

- **O / operability:** r6-row replay dies with an unhandled `KeyError:
  'reports/round-20/handoff/claims-map.md'` (`tools/exercise-handoff-e2e.py:3822`)
  → `⟨owed: named diagnostic + exit code observed in an isolated copy by
  O03/O05⟩`; r7 default chain exit 0 both sides, packet `45f57132…` unchanged;
  selftest 39 → `⟨owed: N⟩` controls; the designed `E2E-DIGEST` tamper legs
  still trip (m12a exit 2 `E2E-BASELINE`, m12b exit 1 `E2E-DIGEST`, at
  `:4414-4430`).

## Acceptance legs — reconciled with the O-block peers (landed after this cut)

`reports/round-35/op/O08-validation-legs.md` and
`reports/round-35/scribe/S02-o-receipt.md` landed after this seat's write; O08
owns the binding validator spec (legs O1–O6: `E2E-READSET` + the member path on
one line, exit ∈ {1,2}, no `Traceback`/`KeyError` in stdout+stderr). Use O08's
spec; the four points below are what this seat measured that bear on it.

1. **Exit-code leg must not be exit-only.** `claims.json:48` declares
   "(expect: exit 1)"; the renderer's own table puts could-not-evaluate classes
   at exit 2 (`tools/exercise-handoff-e2e.py:89-93`), and O08 §4 accepts {1,2}
   with a named deviation if 2 lands. Either way the **pre-patch** run already
   exits 1, so an exit-code-only leg is green on the unfixed tree — the code
   token, the member path and the absence of `Traceback` are the load-bearing
   assertions.
2. **`--quiet` visibility (measured).** `main()` prints the code line only when
   `not args.quiet` (`tools/exercise-handoff-e2e.py:4603-4604`), so on the
   unpatched renderer a `--quiet` run shows no code at all. O08's O1 asserts the
   token over a `--quiet` run's combined output, and claim O's counting command
   is `--quiet`. So the patch must echo the named line in quiet mode (O08 §3's
   recommended wording does) **or** the leg must drop `--quiet` / read `--json`.
   The integrator should not let these two land unreconciled.
3. **Which selftest hosts the two controls (see R1).** Measured: `--selftest`
   (default `--profile v1`) = 17 controls; `--profile v3 --selftest` = 39
   controls. A control that replays the actual r6 row lands in `v3_selftest`
   (39 → 41, O08's O2); a v1-suite control would be a synthetic membership-drift
   fixture (17 → 19, S02's L2 / S04's §6.3 O1). Assert the suite that actually
   hosts the controls — reconcile before the validator asserts a count.
4. **Preservation.** r6 `expected.json` still `ea1e2927…`; r7 `packet.md`
   `45f57132…`, `freeze.txt` `3969954b…`, `claims-map.md` `d181de28…`,
   `expected.json` `bbe15887…` (S02 §6 pins the same set plus `twin.json`
   `0e229138…` and the two gitignored `run.log` digests).

## Findings for the record (observations, not rulings)

- **F1 — the class has a second site.** `tools/exercise-handoff-e2e.py:1435-1440`
  (`v1_exercise`) uses the identical `.get`-then-index pattern; a v1 baseline
  pinning a member the live `V1_READ_SET` (21 files) no longer carries would
  crash the same way. v3-only hardening leaves it open. Owner: O01/R04 decision.
- **F2 — docstring/constant drift.** The constant (`:184`) and the re-pointed
  function docstring (`:2291`, cited as `:2290` in `reports/round-34/handoff/repin.json:35`)
  name the r7 map, while `tools/exercise-handoff-e2e.py:34` and `:57` still name
  `reports/round-20/handoff/claims-map.md` as the read-set copy surface.
  `to-verify` whether that is intended historical wording or stale text; the
  landing should state which.
- **F3 — digest bookkeeping.** The landing moves the renderer past
  `34c85f57…`, which is the `surface_sha256_after` filed in
  `reports/round-34/handoff/repin.json:11`. Filed rows are never rewritten
  (`repin.json:4`) — the new digest needs a new row. No freeze artifact pins the
  renderer (it is not a `V3_READ_SET` member; S02 §6), so the repin reading is
  the only bookkeeping this touches. Owner: integrator.
- **F4 — `--quiet` visibility** (see acceptance leg 2): claim O's counting
  command as written cannot show the code on stdout.
- **F5 — no second refusal reason hidden.** The r6 replay would also fail the
  packet digest (`6ced88ad…` vs `45f57132…`); the named diagnostic must name
  the read-set member, not mask that the row is superseded on both counts.
- **F6 — the drift leg is one-directional and over-claims its count** (found and
  executed by S02, `reports/round-35/scribe/S02-o-receipt.md:103-131`, not by
  this seat; the code-read half is confirmed here): the comprehension at `:3819`
  iterates **baseline** members only, so a live member the baseline never pinned
  passes silently, and the green record at `:3824` counts `len(V3_READ_SET)`
  rather than the number compared. A both-directions membership refusal (or a
  routed follow-up with an owner) is the integrator's decision; it does not widen
  claim O's `after_required`, and if the patch lands it the fleet-report material
  must say so, because it changes the r6 diagnostic's scope.
- **F7 — the obvious bad fix** (S04's hazard, `reports/round-35/scribe/S04-integration-draft.md:404-413`,
  restated here because it is the patch's main trap): the catch site is the
  same loop that produces the real drift message (`:3820-3822`), so a
  `.get(rel)`-with-default or a bare `continue` would turn a genuine
  digest mismatch into a silent pass. The preserved-leg controls (m12b exit 1
  `E2E-DIGEST`, m12a exit 2 `E2E-BASELINE`) are the discriminator; a patch that
  greens the r6 replay while any of them goes quiet is a rejected patch, not a
  trade.
- **F8 — the mechanism reading is triple-confirmed.** K03
  (`reports/round-35/scout/K03-keyerror-path.md:46-51`), S02 (`S02-o-receipt.md:76-101`)
  and this seat independently pin the same two lines (`:3819` tolerant lookup,
  `:3822` the direct index) and the same member; K03 also records the symmetric
  blind spot F6 describes. No competing mechanism reading exists in the tree.

### Reconciliations owed between peer fragments

- **R1 — selftest host/count.** Three peers disagree and the validator must not
  assert a count the controls do not move. Measured here: `--selftest` (default
  `--profile v1`) = 17 controls; `--profile v3 --selftest` = 39 controls. O08's
  O2 asserts the v3 suite ≥ 41; S02's L2 (`S02-o-receipt.md:143`) and S04's §6.3
  O1 (`S04-integration-draft.md:388-391`, with the two controls listed as
  `--selftest` items 18-19 in §7) assert the v1 suite 17 → 19. Both designs can
  be built — the *actual r6 row* is a v3 baseline, so a control that replays it
  lives in `v3_selftest` (39 → 41), while a v1-suite control would have to be a
  synthetic membership-drift fixture (like S02's scratch baselines) — but only
  one count moves per suite. Decide which suite hosts each control, land the
  controls there, and make the validator assert that suite's count; a v1-only
  assertion does not cover the r6-row refusal unless the control is the
  synthetic analogue.
- **R2 — quiet-mode visibility.** O08's O1 asserts the code token on a `--quiet`
  run's combined output; the unpatched `main()` prints the code line only when
  not quiet (`:4603-4604`). The patch (echo the named line in quiet mode) or the
  leg (drop `--quiet`, or read `--json`) must be reconciled; otherwise a correct
  patch can read as a failed leg. S04's §6.3 O2 keeps `--quiet` and asserts on
  the combined output, so it carries the same requirement.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — exact before/after blocks, final line numbers, v1-site decision.
- `reports/round-35/op/O02-controls.md` — the two control fixtures + expected outputs (and the R1 host decision).
- `reports/round-35/op/O03-isolated-verify.md` — observed after-outputs (isolated `git archive` copy): r6 replay, r7 chain, selftest count.
- `reports/round-35/op/O04-regressions.md` — the regression list this material's "nothing else moves" claim rests on.
- `reports/round-35/op/O05-verify.md` — independent isolated verification (fills every `⟨owed⟩`).
- `reports/round-35/op/O06-receipt.md` — operability receipt numbers (the S02 revision folded by the integrator is `reports/round-35/scribe/S02-o-receipt.md`, landed).
- `reports/round-35/review/R04-o-review.md`, `reports/round-35/review/R05-o-review.md` — adversarial review of the patch and of the isolated evidence.
- `reports/round-35/op/O11-verify-2.md` — second independent isolated verification.

Landed peers this material already folds: `reports/round-35/op/O08-validation-legs.md`,
`reports/round-35/scribe/S02-o-receipt.md`, `reports/round-35/scout/K03-keyerror-path.md`,
`reports/round-35/scribe/S04-integration-draft.md` (§1 Landed-changes draft, §6.3
claim-O legs, §7b new controls; read at fold time).

## Citations

Paths:lines
- `tools/exercise-handoff-e2e.py:34`, `:57`, `:89-93`, `:184`, `:1435-1440`, `:1935-1958`, `:2291`, `:3819-3822`, `:4414-4430`, `:4578`, `:4603-4604`
- `reports/round-30/handoff/declared-in-r6/expected.json` (58 inputs; packet `6ced88ad…`; sha `ea1e2927…`)
- `reports/round-34/handoff/declared-in-r7/expected.json` (58 inputs; packet `45f57132…`; sha `bbe15887…`), `freeze.txt` (`3969954b…`), `claims-map.md` (`d181de28…`), `packet.md` (`45f57132…`)
- `reports/round-34/handoff/repin.json:4`, `:11`, `:16-22`, `:35`, `:50` (R34-N1 routed)
- `reports/round-35/claims.json` (claim O; counting commands; non_goals), `reports/round-35/targets.json` (seat O10; shared_rules)
- `reports/round-35/op/O08-validation-legs.md` (binding validator legs O1–O6; exit-code policy §4; quiet-mode assertion §2 O1)
- `reports/round-35/scribe/S02-o-receipt.md:103-131` (S02-F1, attributed), `:140-151` (its L1–L6 legs, incl. the v1 17→19 count), `:170-200` (freeze-bytes pin, `run.log` gitignore)
- `reports/round-35/scout/K03-keyerror-path.md:46-51` (mechanism pinned independently), `:81` (the symmetric blind spot)
- `reports/round-35/scribe/S04-integration-draft.md:88-109` (§1 Landed-changes draft), `:386-437` (§6.3 claim-O legs O1–O7), `:404-413` (the bad-fix hazard)
- `SCORECARD.md:615-620` (r34 rows), `LOG.md:3612`, `:3630`
- `reports/round-20/handoff/claims-map.md` (present on disk, 24,888 bytes)

Peers read in full at fold time (both landed after this seat's cut):
`reports/round-35/op/O08-validation-legs.md`, `reports/round-35/scribe/S02-o-receipt.md`.

Commands run (all non-freeze modes, in-tree, 2026-10-19T08:14-08:17Z)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, `KeyError: 'reports/round-20/handoff/claims-map.md'` at `:3822`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, packet `45f57132…`
- `python3 -B tools/exercise-handoff-e2e.py --selftest` → exit 0, 17 controls
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0, 39 controls
- `sha256sum tools/exercise-handoff-e2e.py`; `git show 4a7aede:tools/exercise-handoff-e2e.py | sha256sum` → both `34c85f57…`
- `grep -c E2E-READSET tools/exercise-handoff-e2e.py` → 0
- python set difference of the r6/r7 `inputs` maps → r6-only `reports/round-20/handoff/claims-map.md`, r7-only `reports/round-34/handoff/declared-in-r7/claims-map.md`, 57 shared
