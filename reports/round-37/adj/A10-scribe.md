- Seat: A10 | scribe | claim A | date 2026-10-19 | baseline 57c8409

# Round 37 — landed-change material (A10)

Draft material for the integrator's adjacency report. This is a descriptive census of recorded round-33–36 work, not a per-surface audit verdict, freeze adjudication, or round-37 acceptance statement.

## Draft — Landed changes

- **Round 33 — shared guidance, corpus index, and example pins.** The round revised `SKILL.md`, removed two lines from `AGENTS.md`, added `REGIMEN.md`, revised `corpus/lessons/README.md` and appended an errata section to `corpus/knowledge/linguistics/register-lexicon-ceilings.md`. It also repointed the contract digests in `examples/culture-d3/{README.md,handoff.md}` and `examples/handoff-packet.sample.{md,yml}`. The filed scorecard records the lessons-index reconciliation, falsifier re-key, open-items ledger, and adjacency audit; it explicitly says no new domain capability landed (`SCORECARD.md:588-600`).
- **Round 34 — handoff successor and adoption audit.** The round filed the `reports/round-34/handoff/declared-in-r7/` packet and `repin.json`, changed `tools/exercise-handoff-e2e.py`, added `tools/harness/receipt_guard_adoption.py` and `op/adoption-inventory.json`, and filed the box-1 re-survey and anchor reissue. The scorecard records the successor packet's measured handoff shape and the adoption inventory's then-filed 29-runner census (`SCORECARD.md:615-617`). Round 35's surface census records five digest-pinned r7 packet files and separately identifies untracked `run.log`, as well as the relevant round-34 surfaces (`reports/round-35/adj/audit-assembled.md:52-55,142-159,257-261`).
- **Round 35 — ten new entries, index revision, and renderer hardening.** The round added six culture-material entries and four myth-symbol entries, updated `corpus/README.md` to revision 2.0, and changed the handoff renderer for the superseded-row `E2E-READSET` diagnostic. The ten paths, read from the committed diff, are:
  - `corpus/knowledge/culture-material/{agrarian-field-system-lexicon,bathing-and-body-hygiene,fire-fuel-light,funerary-material-culture,furniture-interior-lexicon,writing-media-surface-economy}.md`
  - `corpus/knowledge/myth-symbol/{binding-speech-complex,death-afterlife-eschatology,eschatology-world-end-systems,sacred-kingship-mythic-charter}.md`
  The round-35 scorecard describes the partition increase from 201 to 211, the renderer change, and the assembled audit of round-33/34 surfaces (`SCORECARD.md:640-649`). The declaration gives the ten-entry and renderer targets (`reports/round-35/claims.json:22-51`); the assembled audit lists the observed touched surfaces (`reports/round-35/adj/audit-assembled.md:36-60`).
- **Round 36 — timekeeping entry and index revision; no D4 build.** The round added `corpus/knowledge/culture-material/timekeeping-instruments.md` and revised `corpus/README.md` to revision 2.1. Its filed receipt records coverage counts of 212 total (culture-material 25) and a 17-row calibration recount with 15 matches and two dispositioned mismatches (`reports/round-36/validation.json:5-47`; `SCORECARD.md:651-662`). Round 36 was rejected on depth: the declared empty-domain premise was stale because the register forms/law had landed in rounds 26/27, and the receipt says nothing was landed under that failed claim (`reports/round-36/validation.json:49-78,144-165`). The round-36 receipt does not adjudicate the freeze-read-set asymmetry; the separate round-37 A01 result is noted below.

## Boundaries for integration

- This list records paths and changes, not whether their content has zero cross-domain bleed, correct couples, or a faithful re-render. In particular, the ten round-35 additions and the round-36 timekeeping entry still require the separately assigned corpus scan; no finding is closed by naming a file here.
- The round-36 filed-receipt rewrite incident is not a landed deliverable. Its mechanism and observations are recorded separately in `reports/round-36/scribe/S01-integration-draft.md:37-151`; keep incident treatment separate from the intentional corpus/index changes.
- This inventory itself makes no freeze adjudication. A01 has filed an isolated-copy result: `packet.md` and `twin.json` re-rendered byte-identically; A01 classifies omission of `13-register-law.yml` from the read-set as a roster/completeness defect, not a documented skip, while reporting that the component-digest check still detects changed bytes (`reports/round-37/adj/A01-freeze-adjudication.md:5-31`). A01's result does not replace the independent verification assigned to A06/A08 or integrator assembly (`reports/round-37/targets.json:49,54,56,59`). A02 owns the new-entry bleed scan (`targets.json:50`); the round-37 after-required specifies the audit evidence (`reports/round-37/claims.json:25-30`).

## Owed

- A01's result is filed; independent A06/A08 verification and A02's scan of the eleven round-35/36 entries remain assigned before per-surface verdicts can be integrated (`reports/round-37/targets.json:49-50,54,56`; `reports/round-37/claims.json:25-30`). At this check, `Glob reports/round-37/adj/*.md` listed A01, A03, A04, A05, A09, A10, and A11; A02/A06/A08 were absent. This fragment substitutes for none of those results.

## Citations

- `REGIMEN.md:25-50` — audit and evidence contract.
- `reports/round-37/claims.json:25-30`; `reports/round-37/targets.json:49-50,54,56,58-59` — claim A, A01/A02 assignments, independent verification, and this seat's mission.
- `SCORECARD.md:588-600,615-617,640-649,651-666` — rounds 33–36 filed summaries and verdict boundaries.
- `reports/round-35/claims.json:22-35,38-51,54-65` — round-35 ten-entry, renderer, and audit targets.
- `reports/round-35/adj/audit-assembled.md:36-60,142-159,257-261` — round-33/34/35 surface census, pinned r7 members, and untracked `run.log` finding.
- `reports/round-36/validation.json:5-47,49-78,144-165` — round-36 C/Ca results, stale D premise, and rejection.
- `reports/round-36/scribe/S01-integration-draft.md:37-151` — separately recorded round-36 filed-receipt incident.
- `reports/round-37/adj/A01-freeze-adjudication.md:5-31` — A01's separate round-37 re-render and asymmetry result, not a verdict by this inventory.
- Command-output citations, run at `57c8409ba16d9f9e692297198d95e8f2ce5a1937`, from the repository root with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:
  - `git diff --name-status 139e3b6 da68a6d -- SKILL.md AGENTS.md REGIMEN.md SCORECARD.md LOG.md corpus/knowledge/linguistics/register-lexicon-ceilings.md corpus/lessons/README.md examples/ tools/` → the round-33 shared-path set listed above.
  - `git diff --name-status 4a7aede ce103bf -- corpus/README.md corpus/knowledge/ tools/exercise-handoff-e2e.py reports/round-34/handoff/declared-in-r7 reports/round-34/op/adoption-inventory.json` → `corpus/README.md`, the ten round-35 entries listed above, and `tools/exercise-handoff-e2e.py`.
  - `git diff --name-status ce103bf 57c8409 -- corpus/README.md corpus/knowledge/ tools/` → `corpus/README.md` and `corpus/knowledge/culture-material/timekeeping-instruments.md`.
  - `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`; `git status --short -- reports/round-1 ... reports/round-36` → no rows at the time sampled. No round runner was executed.
