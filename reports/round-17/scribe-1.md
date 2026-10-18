# R17-D38 — capability-row drafts: `culture-d4-assembly` and `assemble-culture-d4`

Seat: R17-D38 (scribe), round 17 (operator loop 2 of 3, build round 1 of 4;
64 declared workers, `opencode-go/deepseek-v4.1-flash`). Date: 2026-10-18.
Reference revision: `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17
declare); baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit;
`git merge-base --is-ancestor f30b6f8 HEAD` → exit 0). Writes: this file only;
no commit, no push, no filed round 8–16 byte touched.

This is a **draft**, not a SCORECARD landing and not an admission of round 17
or of either capability. Everything here is NON-CANON engineering evidence:
no canon, no lore acceptance, no real-world clearance or rights/attribution
ruling, no promotion. The wave was still in flight when this seat closed
(§6); the parent must re-read the rows against the settled tree.

## 1. Landing format

`SCORECARD.md` capability tables use the columns
`name | demonstrated behavior | command / evidence | first working`
(`SCORECARD.md:43`, `:176`, `:206`). Rounds 8 and 9 landed new rows as a
"Capabilities addendum (round N)" table under the round's axes section.
The parent decides placement; the rows below are written to paste into such
an addendum **only after** the §3 conditions pass.

## 2. Draft rows (conditional — parent integrates)

Proposed heading: "Capabilities addendum (round 17):"

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| culture-d4-assembly | Fresh NON-CANON D4 culture built end-to-end through the typed pipeline: brief → 12 components → typed labels → assembled packet → gate; gate findings exactly equal to the hold set named before implementation; assembly deterministic (twice byte-identical); frozen replay green; d2/d3 paths untouched and green | `python3 reports/round-17/run-validation.py`; `python3 tools/assemble-culture-d4.py --check`; `reports/round-17/` (design hold-set naming, tests, negatives) | round 17 — proposed; only after parent admission |
| assemble-culture-d4 | Durable D4 packet assembler: `--check` byte-identical regeneration on the delivered tree; `--selftest` fixture controls (positive, tamper, malformed, missing, collision, duplicate-id, wrong-type, below-minimum, too-few-files) fail closed; existing d2/d3 assemblers untouched | `python3 tools/assemble-culture-d4.py --selftest`; `python3 tools/assemble-culture-d4.py --check`; `reports/round-17/validation.json` claim O | round 17 — proposed; only after parent admission |

Both rows carry "proposed" in the `first working` cell so a reader cannot
mistake them for admitted capabilities. The two rows are separable: the O
claim's tool is `assemble-culture-d4`; the D claim's demonstration is
`culture-d4-assembly`. If the parent lands one row only, prefer the row whose
claim verified, and keep the other out rather than merging claims.

## 3. Admission conditions (parent-owned binding)

Do not paste either row as demonstrated until all of these hold, each with a
dated command and its observed output:

1. `examples/culture-d4/` exists and the declared counting command
   (`python3 reports/round-17/run-validation.py`, `reports/round-17/claims.json`)
   exits 0 on the delivered tree.
2. The typed-pipeline gate over D4 emits findings exactly equal to the hold
   set named before implementation. **Pre-leg observed:** the hold set is
   named pre-implementation across `reports/round-17/d4/design-brief.md` (D01),
   `design-costume.md` (D04), `design-language.md`, `design-myth-era.md`, the
   `contract.hold_set_declaration` in `reports/round-17/d4/components/01-brief.yml`,
   and `reports/round-17/d4/expected-holds.fragment.json` (D19) — but the
   equality measurement itself awaits the D4 tree (absent at close, §6).
3. Assembly determinism: twice byte-identical (the assembler `--check` leg).
4. Frozen replay of the D4 packet / expected set is green.
5. d2/d3 regressions green at admission time. **Pre-leg observed (this seat,
   2026-10-18T09:32:27Z):** all 13 pinned d2/d3 artifact and tool hashes still
   equal the 09:16:43Z baseline pins; standing legs table §4. Re-run on the
   settled tree — this is a wave-start observation, not admission evidence.
6. NON-CANON markers present; no real-world clearance/attribution claim
   anywhere in the D4 tree.
7. `tools/assemble-culture-d4.py --selftest` and `--check` green; d2/d3
   assembler bytes unchanged vs baseline `f30b6f8`. **Pre-leg observed
   (⟦IC⟧, 2026-10-18T09:34:32Z):** `--selftest` exit 0, 79/79 checks passed,
   no file outside its temp dir touched, at tool hash
   `d5f2693ccc3946e7e31ba91ee56f7b34cc44aa871169f4c27c5cbcb266c6d970` — a
   read-time pin; the tool may be edited later, so re-run at admission.

## 4. Standing legs at wave start (this seat, 2026-10-18T09:17:44Z)

All read-only; raw outputs `.scratch/d38-d39/legs.txt` (scratch, not part of
the deliverable). cwd = lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`.

| leg | command | result |
|---|---|---|
| D2 assembly | `python3 tools/assemble-d2.py --check` | exit 0 — byte-identical deterministic assembly |
| D2 projector selftest | `python3 tools/d2-typed-labels.py --selftest` | exit 0 — 39/39 checks passed |
| D2 projection | `python3 tools/d2-typed-labels.py --check` | exit 0 — byte-identical deterministic projection |
| D3 assembly | `python3 tools/assemble-culture-d3.py --check` | exit 0 — `packet.json` and `packet.gates.yml` both byte-identical |
| D3 frozen | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | exit 0 — findings `[]`, counts total 0 |
| typed pipeline (D2 default) | `python3 tools/gates/typed-pipeline-gate.py` | exit 0 — 16/16 legs; 15 holds + 1 note, 0 fails |
| frozen replay selftest | `python3 tools/replay-frozen.py --selftest` | exit 0 — 79/79 checks passed |
| D4 assembler selftest (⟦IC⟧, 09:34:32Z) | `python3 tools/assemble-culture-d4.py --selftest` | exit 0 — 79/79 checks passed at tool hash `d5f2693c…c6d970` |

Pinned bytes for the "d2/d3 untouched" leg (sha256, measured
2026-10-18T09:16:43Z and re-verified 09:32:27Z, `sha256sum`):
`tools/assemble-d2.py` `8ea6bdde…c8655d`, `tools/assemble-culture-d3.py`
`ba8d19d5…17f014`, `examples/culture-d2/packet.d2.yml` `e0f21509…37b643`,
`examples/culture-d3/packet.json` `bdf635ce…af4829`. Full table in
`reports/round-17/scribe-2.md` §1.

## 5. Limits

- A wave-start green leg is a baseline observation, not admission evidence
  and not proof that no later worker touched d2/d3; re-run at admission.
- Neither row may claim canon, lore acceptance, cultural permission,
  real-language clearance, or a calibrated numeric score.
- The round-17 acceptance runner and receipt are the parent's to run; the
  mid-wave `reports/round-17/validation.json` (acceptance False, named missing
  dependencies) is **not** acceptance evidence, and its recorded runner hash
  no longer matches the current runner bytes.
- Counts above carry their command and date; the 16/16, 39/39, 79/79 counts
  are printed by the tools themselves at the stated times.

## 6. Handoff state (close, 2026-10-18T09:35Z)

- **Landed:** D4 design docs (`reports/round-17/d4/design-{brief,language,myth-era,costume}.md`),
  typed support 1–2 + `expected-holds.fragment.json`, components 01–04 of 12
  under `reports/round-17/d4/components/`, the assembler
  `tools/assemble-culture-d4.py` (selftest 79/79 ⟦IC⟧), all 12 C disposition
  fragments + map-patch + verify receipts, three D negatives, the runner and
  a mid-wave receipt, X01 lessons census, X02 scope + report draft.
- **Absent at close:** `examples/culture-d4/` itself (0 files), the typed
  labels/packet/expected set/frozen manifest for D4, components 05–12, the
  D4 test fragments (D-tests seats), and a settled-tree `validation.json`.
  Sweep: `find examples/culture-d4 -type f` → 0; `ls reports/round-17/d4/components/`
  → 01–04 only (09:34:43Z).
- The parent must re-read these rows against the settled tree; the polling
  cap (60s cadence, 20 minutes) ended the dependency window, not the round.
  Landed-fragment record and poll log: `reports/round-17/scribe-2.md`.
