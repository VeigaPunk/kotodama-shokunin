# R17-D37 — reviewer: D2/D3-lesson cross-check

- **Seat:** R17-D37 (reviewer, claim D `culture-d4-assembly`), round 17 (operator
  loop 2 of 3, build round 1 of 4; 64 declared workers, `opencode-go/deepseek-v4.1-flash`).
- **Assignment (verbatim):** "D4 R17-D33..D37 (reviewers x5): internal consistency;
  language sketch soundness; myth-costume coupling; hold-set hand re-derivation;
  D2/D3-lesson cross-check. reports/round-17/reviews/review-<n>.md."
- **Date / clock:** 2026-10-18, local -03:00; measurements 09:4x–09:58Z. Wave in
  flight; statements pinned to review-1 §1 digests plus the filed reports cited.
- **Write scope:** this file only, plus scratch under `.scratch/r17-review/`. No
  artifact under `examples/`, `tools/`, `reports/round-{8..16}/`, or `corpus/` was
  written; no commit, no push.
- **Canon:** NON-CANON engineering review. Nothing here is canon, a lore receipt,
  a handoff, or a real-world clearance/rights statement.

## 0. Verdict

**The D4 build absorbed the load-bearing D2/D3 lessons that are exercisable at
this stamp, and the ones that are not are blocked on the typed chain (F6,
review-4), not on a regression.** The strongest carry-overs are measured: no
`compare_only` exemption anywhere (sweep = 0); material reconciliation by slot id
(`material_ref`) with the human label kept beside it; deterministic assembly with
a real missing-output control (selftest 81/81, my run); NON-CANON declared with
the naming gate's `CROSS-HOLD` retained and no clearance claim; d2/d3 paths and
tools byte-untouched and green (my re-runs). One runner-side defect is filed
(F8): the round-17 runner's clearance detector is **negation-blind** — it read
"not accepted by lore-shokunin" as an acceptance claim, and the tree was reworded
to avoid it. The detector itself is unchanged; a future artifact using the
natural phrasing will trip it again. The D2 gate-shape lessons that need the typed
chain (banner, assembler-identity leg, hold keying/canonicalization, TMPDIR
replay, manifest placement) are tracked in §2 as **open requirements**, not as
passes.

## 1. Lesson-by-lesson status

Sources: `reports/round-11/depth/review-20.md` (D2 wiring findings F1–F10),
`reports/round-14/lessons-audit.md`, `reports/round-14/loop1-retrospective.md`
(D2/D3 historical lessons), `reports/round-15/handoff/review-9.md` (F9-1/F9-2),
`reports/round-16/verify.md` (F10-1). Each row is my measurement or an explicitly
cited measurement.

| lesson | D4 status at this stamp | evidence |
|---|---|---|
| D2-F2 `compare_only` is not a licensed exemption channel | **held** — no `compare_only` anywhere in the D4 tree; the design's Δ8 requirement ("register is never compare_only") has no live instance to fail | `grep -rn "compare_only" examples/culture-d4/` → 0 (09:57Z) |
| D2-F3 `--check` must not be blind (missing baseline ⇒ not green) | **held for the assembler** — `--check` exits 1 on a missing output and 1 on tamper; positive exits 0; my runs + selftest controls | `python3 tools/assemble-culture-d4.py --selftest` → `81/81 checks passed`, exit 0 (09:56Z); `--check` exit 0 on the delivered tree (09:45Z, 09:50Z) |
| D2-F5 assembler-identity leg calls the assembler's own build | **open** — no D4 adapter exists; the design requires the leg to call `assemble-culture-d4.py`'s `assemble()` (docstring: "the callable build path the D4 typed adapter's assembler-identity leg calls") | `ls tools/` → `assemble-culture-d4.py` only |
| D2-F7 replay needs `TMPDIR` outside the repo | **verified** — the round-11 manifest replays 11/11 with `TMPDIR=/tmp` and exits 2 `mirror_unsafe` with an in-lane `TMPDIR`; the round-17 runner already runs replay with `tmpdir="/tmp"` | my runs 09:20Z and 09:57:48Z; `run-validation.py` replay leg |
| D2-F9/F10 hold keying and `where` canonicalization | **open (requirement)** — the declared set keys `(id, severity, where)` with `where = GAR-0n` (record id); R17-D17 measured the pinned engine emitting **both** `GAR-0n` and `LEX-GAR-0n` rows — a D4 projector must canonicalize to the declared `where` | declared set: `01-brief.yml` `contract.hold_set_declaration`; D17 measurement: `reports/round-17/d4/typed-run.md` §5 |
| D2-F4 holds printed verbatim with the banner | **open** — no D4 gate exists; the D2 gate's banner/hold-printing discipline is the template (`tools/gates/typed-pipeline-gate.py:24-37`) | `ls tools/` |
| D2-F6 baseline/manifest placement must not trip the battery | **held** — the round-17 manifest landed at `reports/round-17/tests/frozen/MANIFEST.tsv` (6 rows, packet `2776d85c…35d72`), sits on the runner's discovery glob (`reports/round-17/**`), and replays green: `REPLAY OK: 5/5 rows reproduced`, exit 0 (my run 09:58:46Z, `TMPDIR=/tmp`) | manifest + my replay run; runner `MANIFEST_GLOBS` |
| D3 slot-id reconciliation, never by label | **held (after a mid-wave catch)** — costumes carry `material_ref: CMAT-0n` (slot id) beside `material` (human name); D17 measured the 09:42Z revision failing name-matching (6 `R-MAT-UNRESOLVED-REF`) and the 09:49Z revision clean | packet `costumes[*].material_ref`; `typed-run.md` §5 |
| D3 freeze discipline: pins from delivered bytes, never guessed | **held so far** — the fragment carries null pins with a stated reason; no expected file has been written yet (F6) | `expected-holds.fragment.json` `pins_note` |
| D3 controls: positive/domain/malformed fixtures | **held for the assembler** (positive, tamper, malformed, missing, collision, duplicate-id, wrong-type, too-few controls); **open** for the typed gate | `--selftest` 81/81 (mine); no D4 gate |
| D3 declared-violation-retained class | **N/A by design** — the landed registry declares no costume violation; the divergent brief's Δ7 "one R-01 note" signature does not describe this tree | review-3 §1.3; `ASSEMBLY.md` §6 |
| Round-16 F10-1/F9-1/F9-2 (edge source, `#L<n>` anchor, link coverage) | **N/A to this claim** — they govern the packet-v2 handoff, which D4 does not carry; the `#L<n>` lesson does apply to evidence-file locators: my five reviews use plain paths (sweep: no `#L` specs in `reports/round-17/reviews/`) | scope: `reports/round-16/verify.md`; my review files |
| "d2/d3 untouched and green" (round-17 claim D leg) | **held** — d2/d3 example bytes and the three tools show 0 modifications vs HEAD; the five baseline commands exit 0 | `git status --porcelain` on the pinned paths → 0 lines; typed gate 16/16, D2 assembler/adapter/projector `--check`, D3 `--check` all exit 0 (09:37Z and 09:57:46Z) |
| NON-CANON declaration and no clearance claim | **held** — tree declares NON-CANON; naming gate `CROSS-HOLD` retained; clearance-pattern sweep now 0 hits (after the F8 rewording) | my sweep 09:5xZ; naming gate exit 1 with `CROSS-HOLD` |

## 2. Findings

### F8 (medium, runner) — the clearance detector is negation-blind

- `reports/round-17/run-validation.py:131`:
  `re.compile(r"(?i)\b(approved by lore|accepted by lore|lore[- ]accepted)\b")`.
- Demonstration (my run, 09:57Z): the regex matches
  `"…not accepted by lore-shokunin"` (the natural NON-CANON phrasing) and does
  **not** match `"no lore acceptance is claimed or implied."`.
- Live effect measured this round: the O seat's runner snapshot
  (`.scratch/r17-o/validation-check.json`, 06:44 local) failed claim D partly on
  `clearance/acceptance claim found: [{'path': 'examples/culture-d4/brief.md',
  'match': 'accepted by lore'}]` — a false positive on a disclaimer. The tree was
  then reworded (`brief.md` now says "no lore acceptance is claimed or implied"),
  and my sweep shows 0 hits — so the **tree-side workaround works**, but the
  detector still cannot distinguish a claim from its negation.
- Owner: runner author / parent. Control: a runner selftest fixture containing
  `"not accepted by lore-shokunin"` must **not** be flagged (expected: no
  `clearance/acceptance claim found` failure), and a genuine
  `"accepted by lore-shokunin"` must still be flagged. Until then, the workaround
  is a per-file phrasing constraint on the D4 tree, not a fixed guard.

### F9 (low, claim hygiene) — lesson status is not admission evidence

The §1 table records what is held and what is open; the open rows (F5/F4/F9/F10/F6
classes) are exactly the legs the typed chain must carry. No promotion is implied
by the held rows: a green assembler selftest is not a green typed pipeline, and
the D2 gate's 16/16 is D2's, not D4's.

## 3. Limits

- All measurements are read-only; the counting command was not run by this seat
  (it writes `reports/round-17/validation.json`). The O seat's snapshot is cited
  as filed, with its date.
- D17's measurements (12-hold diagnostic, `LEX-GAR` regex crash, rank-leg
  mis-binding) are cited as theirs; I reproduced the refusal and the sweeps only.
- The wave was in flight; a later tree is a re-run event.
- No canon, lore, rights, or clearance judgment is made or implied.
