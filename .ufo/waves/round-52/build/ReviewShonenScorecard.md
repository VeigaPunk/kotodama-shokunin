# ReviewShonenScorecard — SHONEN.md + SCORECARD round-51 calibration check (round 52, attempt 1)

Seat: `KotodamaR52.ReviewShonenScorecard` (reviewer, leaf, read-only). 2026-10-22.
Assigned item: calibrate every assertion in `SHONEN.md` and the round-51 section of
`SCORECARD.md` (lines 1006–1017) against observed repo state; output a mismatch table and
the SHONEN line edits that would make the self-assessment match. Author-lane advice,
never admission. No files written except this report.

Godspeed axes: **calibration accuracy** (every assertion checked against a command),
**evidence reproducibility** (each row names its re-run command), **edit-actionability**
(paste-ready line edits). Frontier walk kept only moves that improve an axis and harm none.

Lane state during this check (recorded, because the lane is live): HEAD moved
`dea5ece` → `5b7ecfb` mid-check (round-52 commit "claim D wording fixes from
CriticClaimD"); worktree additionally has ` M tools/check-source-access.py` (uncommitted)
and untracked `corpus/lessons/round-52.md`, `.ufo/waves/round-52/`. Worktree counters
below are as of HEAD `5b7ecfb`.

## Headline counts for the round-52 report

- **SHONEN line defects needing edits: 2** (M1, M2 below).
- **Evidence flag: 1** (F1 — the cited final receipt ends on an unresolved QUALITY-9
  two-way line `MISSING_FROM_RECEIPT ['D', 'C']`).
- **Verification gap: 1** (G1 — the `9feb69e` leg of the SCORECARD calibration row).
- **Assertion groups verified green: 14** (table B).
- "Sources registered" figure to use now: **133 rows** (`S001`–`S133`, 133 unique ids):
  **93 mined, 33 queued, 7 rejected** (rejected = S028, S029, S030, S043, S047, S094,
  S132). Will change again at integration when S134+ land.

## Table A — mismatches (assertion, observed, command)

| # | Assertion (file:line) | Observed | Command |
|---|---|---|---|
| M1 | `SHONEN.md:6` — "sources registered in `corpus/SOURCES.md` (**131 opened rows** after round 51, census exit 0 in `reports/round-51/telemetry/final-measures.txt`)" | Wrong label and stale figure. 131 was the **total row count** at `364eeff` (`final-measures.txt` grep block: `131`); at the round-51 tip `2b956d7` the split is **94 mined / 32 queued / 5 rejected**. After the round-52 base `147cfde`: **133 rows — 93 mined / 33 queued / 7 rejected** (S094 `mined`→`rejected` via S132, `corpus/SOURCES.md:123` and `:161`; new S133 `queued` supersedes S097's locator). Not 131 opened rows at any point. | `grep -c '^| S' corpus/SOURCES.md`; `git show 364eeff:corpus/SOURCES.md \| grep -c '^| S'`; `awk -F'\|' '/^\| S/{print $9}' corpus/SOURCES.md \| sort \| uniq -c` (same against `git show 2b956d7:…`) |
| M2 | `SHONEN.md:8` — "round 51 gap sweep → **54 opened sources** → sign-language entry …" | 54 is only the **build-wave Gate snapshot** (`corpus/lessons/round-51.md:26`: "Admitted: 54 rows (52 mined by the new entry, S123 and S124 queued as leads)"). The falsify wave added S125–S131, so round 51's final total is **61 new rows (53 mined, 8 queued)**; today the registry is 133 rows. "Opened" also mislabels the queued rows. | `git show 364eeff:corpus/SOURCES.md \| awk -F'\|' '/^\| S/{id=$2; gsub(/[^0-9]/,"",id); if (id+0>=71) print $9}' \| sort \| uniq -c` → `53 mined / 8 queued` |

## Table B — assertions verified green

| # | Assertion (file:line) | Observed | Command |
|---|---|---|---|
| 1 | `SHONEN.md:5-6` — `SKILL.md:20` Decision table, `:468` Error patterns, `:522` Checklist | All three exact: `20:## Decision table`, `468:## Error patterns`, `522:## Checklist (executable where a tool exists)` | `grep -n -E '^## (Decision table\|Error patterns\|Checklist)' SKILL.md` |
| 2 | `SHONEN.md:8` — "repairs at `364eeff`" | exists, type `commit`; `final-measures.txt` header: `worktree=364eeff0e42c… (lane main tip plus uncommitted records only)` | `git cat-file -t 364eeff` |
| 3 | `SHONEN.md:10` — round-50 counting commands re-run in fresh clones of `1923bfe` and `4ad2683` | both exist, type `commit`; re-run documented with evidence at `SCORECARD.md:983-985` (run-validation → `acceptance_passed: true`) | `git cat-file -t 1923bfe; git cat-file -t 4ad2683` |
| 4 | `SHONEN.md:8` — LOG.md round-51 entry | present at `LOG.md:4040` (trigger, D/C, falsify wave, evidence at `:4046` — "36 reports", "41 seats") | `grep -n 'Round 51' LOG.md` |
| 5 | `SHONEN.md:12` — sign entry §15 hands canon to lore | `corpus/knowledge/linguistics/sign-languages-manual-modality.md:222` (`## 15. Scope`), handoff sentence "lore-shokunin owns whether a signed language exists in-world…" at `:226-227` | read of `:222-247` |
| 6 | `SHONEN.md:12` — sign entry §2 cites every partial owner one-way | `:31` (`## 2. One-owner boundary`); 14 neighbour rows, each with a `name.md:NN` anchor and a boundary cell (e.g. `phonetics-phonology.md:201`, `worldbible-integration-contract.md:17`) | read of `:31-51` |
| 7 | `SHONEN.md:12` — connector sweep found 0 sibling owners + one unowned fleet surface | `.ufo/waves/round-51/build/ConnectSiblingSign.md:17` "No sibling lane owns or partly owns any part of claim C's scope"; `:70` unowned surface = "Real-world accessibility of signed content (WCAG 1.2.6, AAA) has no owner in the fleet" | grep `sibling\|accessibilit` on that file |
| 8 | `SHONEN.md:11` — PROVINCE.md still accurate | `PROVINCE.md:8-13` owns the six knowledge partitions; `:15-19` refuses canon → lore handoff; matches the sign entry's §15 handoff | read of `:1-27` |
| 9 | `SCORECARD.md:1008` — hashes `bff83ba`, `1f97472`, `35f0d49`, `e6b6629`, `da31d3c`, `364eeff`, `9feb69e` | all resolve, type `commit` (also `2b956d7`, `147cfde`, `dea5ece`, `5b7ecfb`) | `git cat-file -t <hash>` loop |
| 10 | `SCORECARD.md:1008,1012,1013` — receipts and their figures | `reports/round-51/telemetry/final-measures.txt`: `rows=15 resolved=15 distinct=15` exit 0; `227` files; linguistics `26`; `footer_live {"total": 227 …} footer_ok True`; `SEPARABILITY: 0 findings`; census `kotodama ok … exit 0` (with 5 W04 duplicate-URL warnings S127–S131 recorded). `declaration-dry-run.txt`: `rows=11 …`, `226`, separability INPUT_ERROR exit 2 disclosed (C's land absent pre-build — expected for a before-receipt) | read of both receipts |
| 11 | `SCORECARD.md:1009` — build 36 seats, falsify 41, round total 77 | `build/` has 37 files = 36 seat reports + `swarm-registry.json`; `falsify/` has 42 = 41 + `swarm-registry.json` | `find .ufo/waves/round-51/build -maxdepth 1 -type f \| wc -l` (same for `falsify`) |
| 12 | `SCORECARD.md:1013` — coverage `226 → 227`, linguistics `25 → 26`, footer total 227 | receipts confirm; current worktree: `227` knowledge files, `26` linguistics; `corpus/README.md:602` "Total knowledge entries: 227." and `:606` "(total 227 files; directory totals 26/26/28/29/24/94)" | `find corpus/knowledge -name '*.md' \| wc -l`; `grep -n '227' corpus/README.md` |
| 13 | `SCORECARD.md:1016` — frontier `70 → 131 rows` (S071–S122 mined, S123–S125 + S127–S131 queued, S126 mined) | arithmetic closes exactly: 61 new rows at close = 53 mined + 8 queued; matches the receipts | same as M2 command |
| 14 | `SHONEN.md:6,8,10,12` — "no non-author verifier on record" | still true mid-wave: `SCORECARD.md:1006` "author-side verdicts, pending non-author closure"; `:1017` "Non-author verification is the hyaku closure's"; no named verifier anywhere in the round-51 section | `grep -n 'non-author' SCORECARD.md` |

Context check for claim D (the L1's report will want it): sign entry S094 lines
**5 at base** (`147cfde` and `2b956d7`, lines 83, 87, 90, 92, 93) → **0** at `dea5ece`
and at HEAD `5b7ecfb`, matching `reports/round-52/claims.json` exactly:
`git show 147cfde:corpus/knowledge/linguistics/sign-languages-manual-modality.md \| awk '/S094/{print NR}'`;
`awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md`.

Depth counter re-run (script read first: stdlib, prints only, read-only):
`python3 -B reports/round-51/boundary-count.py` → `rows=15 resolved=15 distinct=15`, exit 0.

## SHONEN line edits (draft, ready to paste)

`SHONEN.md:6` — replace the parenthetical:

> (131 rows at the round-51 close — 94 mined, 32 queued, 5 rejected; 133 rows after the
> round-52 base `147cfde` — 93 mined, 33 queued, 7 rejected, S094 rejected via S132 —
> census exit 0 in `reports/round-51/telemetry/final-measures.txt`)

`SHONEN.md:8` — replace the chain head:

> round 51 gap sweep → 61 new SOURCES rows (53 mined, 8 queued; the build wave admitted
> 54 per `corpus/lessons/round-51.md`, the falsify wave added S125–S131) → sign-language
> entry → 41-seat falsify wave → …

I do not edit SHONEN.md myself — this seat writes only its report.

## Flag F1 — the cited final receipt closes on an unresolved criterion-9 line

`reports/round-51/telemetry/final-measures.txt`, last block:

> `$ receipt coverage (QUALITY criterion 9 two-way check): declared manifest acceptance argvs present in reports/round-51/telemetry/declaration-dry-run.txt?`
> `MISSING_FROM_RECEIPT ['D', 'C']`

The manifest's acceptance argvs (`reports/round-51/separability-manifest.json`: D =
`sh -c "test \"$(python3 -B reports/round-51/boundary-count.py)\" = 'rows=15 resolved=15 distinct=15'"`;
C = the `find … -eq 227 && sweep && python3 -c` pair) appear in **neither** receipt
verbatim — the dry-run receipt records the bare counting commands only. Since
`SCORECARD.md:1014` leans on criterion 9 (which supersedes 8), this standing `MISSING`
line undercuts citing the receipt as a clean final measure.

Recommendation (L1 decision, not mine to execute): re-issue the declaration dry-run with
the two acceptance argvs included verbatim and regenerate `final-measures.txt` so the
coverage block reports an empty MISSING list — or annotate the calibration row that the
gap is open. Keep the line; it is an honest record. Do not weaken the check.

## Residual risk and unrun checks

- **G1** — `SCORECARD.md:1014` "0 findings, exit 0 at `9feb69e` and `364eeff`": the
  `364eeff` leg is receipt-verified; the `9feb69e` leg was not re-run here (needs a clone;
  sandbox clones are reserved for executor seats). Both hashes exist as commits. Low risk —
  SOURCES is identical between `9feb69e` and `2b956d7` on the row-status level I checked.
- `lessons/round-51.md:94` ("No existing row (S001–S070) changed `status` … this round")
  reads round-wide but the falsify wave flipped S081 `mined`→`queued` (documented at
  `:127` and in commit `10f433c`'s subject; `corpus/SOURCES.md:110` shows it queued,
  used-by `—`). If the lesson is touched again, scope that sentence to the build wave.
- `tools/check-source-access.py` is dirty in the worktree; any census re-run today is not
  byte-identical to the recorded `364eeff` census.
- Small numeric drift risk: the lane is live; figures in Table A are as of HEAD `5b7ecfb`,
  2026-10-22.
- Unrun: separability re-run at `9feb69e`; fresh-clone re-runs of round-50 counters
  (already receipted at `SCORECARD.md:983-985`).

Tooling record: no tools installed or upgraded (none needed; pacman pause respected).
All checks read-only git (`cat-file -t`, `show`, `log`, `diff`, `status`, `rev-parse`),
`find`/`grep`/`awk` counts, and one verified-read-only repo script
(`reports/round-51/boundary-count.py`).
