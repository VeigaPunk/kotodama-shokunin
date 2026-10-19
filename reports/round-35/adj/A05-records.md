- Seat: A05 | executor | A | date 2026-10-19 | baseline 4a7aede

# A05 — audit slice: ceilings errata + box-1/reissue records + contract-read-record

**Mission** (`reports/round-35/targets.json`, seat A05): "Audit slice: ceilings
errata + box-1/reissue records + contract-read-record — bilateral/contested items
still routed-not-absorbed." Out: `reports/round-35/adj/A05-records.md`.

**Method.** Every claim below is a re-run, not a re-read: I re-executed the sweeps
the errata reports, re-hashed every digest the records pin, and re-ran the greps
the reissue's counts rest on. Window 2026-10-19, repo root, HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`, env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Read-only: no file outside
this fragment was written (`git status --porcelain` → `?? reports/round-35/` only).

**Surfaces in this slice (4):**

1. `reports/round-33/telemetry/r25-28-devin-reading-errata.json` (+ its subject
   set) — the prior-round availability-reading errata.
2. `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §12 — the ceilings
   errata (the round-33 append-only correction of the entry's head-block sweeps).
3. `reports/round-34/craft/box1-resurvey-durable.json` and
   `reports/round-34/craft/anchor-reissue.md` — the box-1 re-survey receipt and the
   A09 R5 anchor reissue (authorship: `calib/C03-anchor-reissue.md`; source of the
   reissue table: `calib/C09-final-receipt.md` §5/§5.1).
4. `reports/round-33/adj/contract-read-record.md` — the §1 same-revision read
   record (draft: `calib/C08-item-08.md` §4).

## 1. Verdict table

| # | surface | ownership (PROVINCE) | language scan | evidence resolves | verdict |
|---|---|---|---|---|---|
| 1 | availability errata JSON | in-lane (`reports/round-33/telemetry/`, AGENTS.md:17-18) | clean | yes (§2.2) | **GREEN** |
| 2 | ceilings §12 errata | in-lane (`corpus/knowledge/linguistics/` owned partition, `PROVINCE.md:9-11`) | clean | yes (§2.1) | **GREEN** |
| 3 | box-1 durable receipt | in-lane (`reports/round-34/craft/`) | clean | 27/28 row digests; **A05-F1** (§3.1) | **GREEN with named finding** |
| 4 | anchor reissue | in-lane (`reports/round-34/craft/`) | clean | yes; precision note **A05-P1** (§3.2) | **GREEN** |
| 5 | contract-read-record | in-lane (`reports/round-33/adj/`) | clean; scope-negation present | yes (§4) | **GREEN** |

Zero unfiled cross-domain bleed across the five surfaces (§5). Contested/bilateral
items remain routed-not-absorbed (§6).

## 2. Ceilings errata — re-measured

### 2.1 The §12 absence sweeps reproduce exactly

`register-lexicon-ceilings.md:291-317` (§12) claims the head block's five sweeps,
all written as `→ 0` on 2026-10-18, now return ≥ 1 at the post-landing tree. My
re-run at HEAD `4a7aede`, `grep -rl -i "<pat>" corpus/knowledge/ | wc -l`:

| pattern | §12 table (`:297-303`) | my re-run | match |
|---|---|---|---|
| `lexicon ceiling` | 2 | 2 | ✓ |
| `register ceiling` | 1 | 1 | ✓ |
| `derivational ceiling` | 1 | 1 | ✓ |
| `operation-constrained` | 1 | 1 | ✓ |
| `which semantic fields` | 3 | 3 | ✓ |

The finding row also reproduces: `sound-symbolism.md:106` reads "assign **which
semantic fields** carry ideophones", and that file's last move is round 10
(`git log --oneline -1 -- corpus/knowledge/linguistics/sound-symbolism.md` →
`94ca098 round-10: admit C/F/O`), i.e. pre-existing at the round-28 baseline — so
the `X63-F2` **authoring-defect** classification (§12 `:305-311`) is correct, and
it is *routed, never repaired*: `reports/round-28/audit/x63-entry-source-resolvability.md:264`
("It **repairs nothing.** X63-F2 is a corpus write and is routed"). The sibling-landing
rows (`register-strata-attestation.md` §13 amendment at `:315`, this entry itself)
are correctly separated from the defect class (`x63…:3.4`, F1/F3/F4 rows).

### 2.2 The availability errata JSON's citations all resolve

`reports/round-33/telemetry/r25-28-devin-reading-errata.json`:

- `subject` (4 availability records) → all four exist (`reports/round-{25,26,27,28}/availability.json`).
- `reading` (`:6`) → re-measured over all four records: `requested_workers` = 64,
  `launched_workers` = `null`, `completed_workers` = `null`, route
  `devin/deepseek-v4-1-flash-high` in every record. The nulls are live facts, not
  inferred zeroes.
- `do_not_infer` (`:7`) → `reports/round-29/recount/ledger.json:274-285` is the
  R25 row carrying `"clean completions": {"R25": "113/113", …}` under
  `recorded`/`observed` — the seat-marker populations the errata says are *not*
  launch counts. Citation resolves and says what the errata says it says.
- `source_disposition` (`:8`) → `reports/round-29/devin-availability-disposition.md`
  exists. `convention_fix` (`:9`) → `reports/round-30/telemetry/dispatch-stats.json`
  exists and the durable-path rule is live at `AGENTS.md:17-18`; the null convention
  is live at `AGENTS.md:25-26` (both sed-read this window).
- `verified_by` (`:10`) → the draft it names, `reports/round-33/calib/C11-item-11.md`,
  carries the same `reading`/`do_not_infer` strings verbatim (`:205-206`), so the
  filed JSON is the draft, not a rewrite.

## 3. Box-1 / reissue records — re-measured

### 3.1 `reports/round-34/craft/box1-resurvey-durable.json`

**What reproduces.** `skill_lines` 732 and `skill_sha256` `f9bd07c2…` equal live
`SKILL.md` (`sha256sum` → `f9bd07c2bd13…`, `wc -l` → 732). `survey_script_sha256`
`d923ae0f…` equals live `reports/round-30/craft/box1-survey.py`. The hardcoded-date
trap is correctly documented (`:25`; `box1-survey.py:8` is the literal
`"date": "2026-10-18"`, and `:10` is the live `skill_sha256` read). The `supersedes`
row resolves: `reports/round-30/craft/box1-landed-survey.json:4` is still
`83b0a78a…`, filed and unedited. The promotion boundary is explicit and correct
(`:9` `"not_a_promotion_verdict": "…promotion decisions stay operator-owned"`).

**A05-F1 (named finding — one row digest is stale at the delivered revision).**
Of the 28 `rows[]` executable digests, **27 reproduce at HEAD; one does not**:

- `tools/exercise-handoff-e2e.py`: receipt `sha256` = `a5e4a8c5dda9d63c…` (`:149`),
  live at `4a7aede` = `34c85f5773fb1925…`. Measured both ways:
  `git show da68a6d:tools/exercise-handoff-e2e.py | sha256sum` = `a5e4a8c5…` (match);
  `git show 4a7aede:…` = `34c85f57…` (mismatch); `sha256sum tools/exercise-handoff-e2e.py`
  = `34c85f57…` (mismatch).
- Cause, measured: the same admission commit that landed the receipt also changed
  the renderer — `git diff --stat da68a6d 4a7aede -- tools/exercise-handoff-e2e.py`
  → `11 insertions(+), 10 deletions(-)`; the receipt's `measured_at_utc` is
  `2026-10-19T07:11:01Z`, before the commit (`4a7aede` dated `2026-10-19 05:01:17 -0300`
  = 08:01:17Z). The row set therefore describes the pre-integration tree for that
  one row; `skill_sha256` did not move (SKILL.md untouched by the commit), so the
  receipt's own `reverify` rule (`:30`, which anticipates only a moved
  `skill_sha256`) does not cover it.
- Why it went unflagged: the round-34 validator's `leg_box1`
  (`reports/round-34/run-validation.py:238-256`) checks the survey's 28/28
  resolvability, the skill digest, and the receipt's `date`/`skill_sha256`/`resolvable`
  — **never the row digests**; the admitted record's C1-C3 measurement carries only
  the survey tail (`reports/round-34/validation.json`, `claims.C.measurement.legs.C1-C3`).
  The verifier chain measured the row at its own tree (`calib/C07-verify-survey.md:93,135`,
  `calib/C02-receipt-json.md:175-181` — both `a5e4a8c5…`), so each reading is true
  at its stamp; the *delivered* revision is what disagrees.
- **Owner: integrator.** Resolution is a new dated re-extraction (or an errata row)
  naming `a5e4a8c5…` → `34c85f57…` for that one row — never an edit of the filed
  receipt. Note for sequencing: round-35 claim O patches the same file, so this row
  moves **again** in this round; any round-35 box-1 re-run must re-extract rows, and
  the reissue/receipt pair will be stale at close unless the round names both moves.
- Not falsified by this: the claim-C threshold ("28/28 at the new digest") is about
  *path resolvability* at the SKILL digest, and that holds — all 28 paths resolve
  at `4a7aede` (`reports/round-30/craft/box1-survey.py` re-run: `resolvable 28`,
  `unnamed_in_skill []`). The finding is a supersession the record does not name,
  not a broken pin.

### 3.2 `reports/round-34/craft/anchor-reissue.md`

- **Provenance is honest.** The file's header (`:3-4`) names its source as
  `calib/C09-final-receipt.md` §5/§5.1; C09 §5 carries the same table and §5.1 the
  same census and the same `C09-F2` finding (C09 `:5.1` items 1-4), so the reissue
  is a copy-forward, not a re-derivation.
- **The seven live stale cites reproduce exactly**: tree grep
  `grep -rno "SKILL\.md:715\|SKILL\.md:713-715" corpus/lessons/` → 7 sites
  (`README.md:242`, `README.md:244`, `round-32.md:7,33,41,55,57`) — matching the
  reissue's "exactly seven" list (`:35-38`).
- **The retirement is recorded as a retirement, not a shift**: `git show 139e3b6:AGENTS.md | sed -n '42p'`
  → `### 2.2 \`SKILL.md\` — append one item to "## Checklist (executable where a tool exists)" (after :534)`;
  `wc -l AGENTS.md` → 40; `grep -c "append one item" AGENTS.md` → 0 (rc=1). The
  reissue's `R` class (`:33`) and its `SKILL.md` pin movement `715 → 732 lines,
  79fe91d3… → f9bd07c2…` (`:8-10`) both match live bytes.
- **A05-P1 (precision note, not a defect).** The reissue maps the stale
  `SKILL.md:715` cite to `:731-732` (`:35-37`), but the audit one-liner — the token
  the recheck in `corpus/lessons/round-32.md:7,41,55` re-executes — is exactly
  **`:732`** (verified: `sed -n '729,732p' SKILL.md`, the `(audit: python3 -c …)`
  line is `:732`; `:731` is the preceding clause line). The tight map is `:715 → :732`.
  The range is not false (the target lies in it, and C08's G11 files the same
  `:714-715 → :730-732` restructuring), but a reader re-running the cite should be
  given `:732`.
- The reissue contains no canon/promotion/clearance/closure language (grep: 0 hits),
  and its byte-preservation stance ("filed rows citing old anchors stay
  byte-identical as superseded readings", `:6`) is the append-only discipline
  `AGENTS.md` requires.

## 4. Contract-read-record — re-measured

`reports/round-33/adj/contract-read-record.md` (9 lines):

- **The digest pin resolves twice over.** `file_sha256: 5f4c02bf…` equals
  `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` **and**
  `git show 139e3b6:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum`
  — the contract has not moved between the round-33 baseline and HEAD, so the
  record's pin is current, not merely filed.
- **The record itself is unedited since filing**: live
  `sha256sum reports/round-33/adj/contract-read-record.md` = `e415ac6b18e287…`,
  equal to the digest recorded in `reports/round-33/validation.json:1210`.
- **Field set conforms to the contract's own gate**: `worldbible-integration-contract.md:14`
  requires each lane to record `lane, contract_id, revision, file_sha256, reader,
  read_at, evidence_pointer`; the record carries exactly those seven (`:1-8`), with
  `contract_id: kotodama-lore-adjacency` / `revision: 1.0.0` matching the contract's
  `:11`. The `evidence_pointer` (`:8` → `reports/round-33/calib/C08-item-08.md`)
  resolves, and `C08-item-08.md:141-144` is the draft this record instantiates:
  `diff` of the draft block against the filed file shows only the two `<…>` slots
  filled (`reader`, `read_at`) — no field invented, no scope line dropped.
- **Routed-not-absorbed, explicitly.** The record's `scope:` line (`:9`) reads
  "§1 gate only; this record does not represent lore's read, acceptance, receipt,
  or canon standing", and the round-33 assembled audit enforces the same reading:
  `reports/round-33/adj/audit-assembled.md:51` — "It must not be described as
  bilateral acknowledgement." The bilateral half stays open (`C08-item-08.md:113`
  records the reason: "lore's read record is not producible from this lane"), which
  is the correct disposition under `PROVINCE.md:22-25` ("Contested scope → report to
  the integrator, never absorb").

## 5. Language and ownership scan (all five surfaces)

- **Cross-domain bleed: zero hits.** `grep -n -i "game-dev\|game mechanic\|kake\|chousa\|kotoba\|attribution ruling\|rights ruling\|web publish"`
  across all five files → rc=1 (no matches). The refuses-list domains in
  `PROVINCE.md:16-20` appear nowhere.
- **Canon/promotion/clearance/closure language is present only as negation or
  routing.** Every hit, by file: contract-read-record `:9` (scope negation);
  box-1 receipt `:9` (`not_a_promotion_verdict`); ceilings entry `:3` ("canon
  decisions belong to lore-shokunin"), `:8` and `:241` ("NON-CANON"), `:244`
  ("are not canon for any world"), `:274-278` ("Nothing here decides what is true
  in any world … whether they are canon is lore-shokunin's decision"). The
  promotion/clearance/closure trio has **zero** hits in the ceilings entry
  (grep rc=1) and zero in the reissue and the errata JSON.
- **Ownership:** all five surfaces are in-lane — the ceilings entry in the owned
  `corpus/knowledge/linguistics` partition (`PROVINCE.md:9-11`), the four report
  files under this lane's own `reports/round-{33,34}/` (`PROVINCE.md:27-29`), the
  errata under `telemetry/` per `AGENTS.md:17-18`. No sibling path is written or
  claimed; no artifact asserts a lore-side action.
- **Source resolution in the ceilings entry:** every corpus/tool path its head
  block and `couples` row name resolves (15-path spot-check → 0 missing),
  including the measured authority `reports/round-28/ceiling/measure-ceiling.py`
  and the D4 phonology fixture `examples/culture-d4/components/02-phonology.yml`.

## 6. Routed-not-absorbed check (the mission's question)

| contested/bilateral item | state | evidence |
|---|---|---|
| lore's §1 same-revision read (OI-08) | **open, lane-half only**; explicitly not bilateral | `contract-read-record.md:9`; `audit-assembled.md:51`; `C08-item-08.md:113` |
| X63-F2 sweep defect | **routed, not repaired** in the corpus; correction carried append-only in §12 | `x63…:264`; `register-lexicon-ceilings.md:305-317` |
| R25-R28 worker-count nulls | **could-not-evaluate** preserved; no inferred zeroes/64 | errata `:6-7`; re-measured nulls in all four records |
| box-1 promotion standing | **operator-owned**, not asserted | `box1-resurvey-durable.json:9` |
| register-gate vs law-enforceability scope | **reported to the integrator**, not decided | `register-lexicon-ceilings.md:286-289` |

No surface in this slice absorbs a contested decision, and no surface claims a
promotion, clearance, canon or closure verdict.

## Owed

- **A05-F1's resolution** — `reports/round-34/craft/box1-resurvey-durable.json`'s
  `tools/exercise-handoff-e2e.py` row (`a5e4a8c5…` vs live `34c85f57…`) needs a new
  dated supersession row or errata, filed by the integrator after the round-35
  claim-O patch lands (the row moves again in this round). I draft no file edit:
  the receipt is filed round-34 byte and is not mine to rewrite.
- **A05-P1's tightening** — the reissue's `:715 → :731-732` map should be quoted as
  `:715 → :732` by any round-35 record that copies it (the reissue file itself is
  filed and stays as written).
- `reports/round-35/adj/K04-touched-census.md` — not on disk at my reads
  (`ls reports/round-35/` → `claims.json targets.json telemetry`); if K04's census
  names touched surfaces inside my slice that I did not cover, the integrator adds
  them. My surface set is fixed by the A05 mission text itself.
- The A-claim's cross-slice verdict assembly (`adj/A08-audit-draft.md`) consumes
  this fragment's per-surface verdicts; the PROVINCE accuracy re-verification at
  HEAD is A06/A11's surface, not re-done here.

## Citations

- `reports/round-35/targets.json` seat A05 (role executor, claim A, mission, out
  `adj/A05-records.md`); `:5-12` shared rules; `reports/round-35/claims.json:53-65`
  (claim A after_required/thresholds).
- `reports/round-33/telemetry/r25-28-devin-reading-errata.json:1-11` (whole file);
  `reports/round-33/calib/C11-item-11.md:138,205-206`; `reports/round-29/recount/ledger.json:274-285`;
  `reports/round-29/devin-availability-disposition.md`; `reports/round-30/telemetry/dispatch-stats.json`;
  `reports/round-{25,26,27,28}/availability.json` (re-measured: 64 / null / null /
  `devin/deepseek-v4-1-flash-high` in all four); `AGENTS.md:17-18,25-26`.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:3-4,8,241,244,274-289,291-317`;
  `corpus/knowledge/linguistics/sound-symbolism.md:106`;
  `corpus/knowledge/linguistics/register-strata-attestation.md:315,399`;
  `reports/round-28/audit/x63-entry-source-resolvability.md:3.4,264`.
- `reports/round-34/craft/box1-resurvey-durable.json:6-31,33-335` (rows),
  `:9,25,30,149`; `reports/round-30/craft/box1-survey.py:5-13`;
  `reports/round-30/craft/box1-landed-survey.json:2,4`;
  `reports/round-34/run-validation.py:238-256`;
  `reports/round-34/validation.json` (`claims.C.measurement.legs.C1-C3`);
  `reports/round-34/calib/C02-receipt-json.md:175-181`;
  `reports/round-34/calib/C07-verify-survey.md:93,135`;
  `reports/round-34/calib/C04-byte-check.md` (no mention of the renderer row).
- `reports/round-34/craft/anchor-reissue.md:1-42`; `reports/round-34/calib/C09-final-receipt.md` §5/§5.1;
  `reports/round-34/calib/C03-anchor-reissue.md:56-128,140-153`;
  `reports/round-34/calib/C08-verify-reissue.md:63-84,133-140`;
  `reports/round-33/adj/A09-pins.md:85-94,105-114,120-126`.
- `reports/round-33/adj/contract-read-record.md:1-9`;
  `reports/round-33/adj/audit-assembled.md:51`;
  `reports/round-33/calib/C08-item-08.md:4,39-46,101-114,137-150`;
  `reports/round-33/validation.json:211-212,1210`;
  `corpus/knowledge/synthesis/worldbible-integration-contract.md:11,14,15,100,132`;
  `PROVINCE.md:9-11,16-20,22-29`.
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`;
  `git status --porcelain` → `?? reports/round-35/`;
  `for p in "lexicon ceiling" "register ceiling" "derivational ceiling" "operation-constrained" "which semantic fields"; do grep -rl -i "$p" corpus/knowledge/ | wc -l; done` → 2/1/1/1/3;
  `grep -rn -i "which semantic fields" corpus/knowledge/` → 6 lines / 3 files;
  `sed -n '106p' corpus/knowledge/linguistics/sound-symbolism.md`;
  `git log --oneline -1 -- corpus/knowledge/linguistics/sound-symbolism.md` → `94ca098`;
  `sed -n '/### 3.4/,/### 3.5/p' reports/round-28/audit/x63-entry-source-resolvability.md`;
  `sha256sum SKILL.md` → `f9bd07c2…`; `wc -l SKILL.md` → 732;
  `sha256sum reports/round-30/craft/box1-survey.py` → `d923ae0f…`;
  `sed -n '5,13p' reports/round-30/craft/box1-survey.py`;
  python row-digest comparison of all 28 `rows[]` against live, `da68a6d:` and `4a7aede:`
  (27 live=OK, 1 live=DIFF: `tools/exercise-handoff-e2e.py` `a5e4a8c5…` → `34c85f57…`);
  `git diff --stat da68a6d 4a7aede -- tools/exercise-handoff-e2e.py` → `11 insertions(+), 10 deletions(-)`;
  `git log --oneline -3 -- tools/exercise-handoff-e2e.py` → `4a7aede`, `71cd9d3`, `3b13a2f`;
  `git show --stat --name-only 4a7aede | grep "^tools/"` → `tools/exercise-handoff-e2e.py`, `tools/harness/receipt_guard_adoption.py`;
  `grep -rn "SKILL\.md:715\b\|SKILL\.md:713-715" corpus/lessons/ | wc -l` → 7;
  `sed -n '729,732p' SKILL.md`;
  `git show 139e3b6:AGENTS.md | sed -n '42p'`; `wc -l AGENTS.md` → 40; `grep -c "append one item" AGENTS.md` → 0;
  `sha256sum reports/round-33/adj/contract-read-record.md` → `e415ac6b…`;
  `git show 139e3b6:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum` and `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → both `5f4c02bf…`;
  `diff <(sed -n '137,150p' reports/round-33/calib/C08-item-08.md) reports/round-33/adj/contract-read-record.md` → only the two `<…>` slot lines differ;
  `grep -n -i "game-dev\|game mechanic\|kake\|chousa\|kotoba\|attribution ruling\|rights ruling\|web publish"` over the five surfaces → rc=1;
  `grep -n -i "canon\|promotion\|clearance\|closure\|lore"` per surface (hits enumerated §5);
  `ls` spot-check of 15 corpus/tool paths cited by the ceilings entry → 0 missing.
