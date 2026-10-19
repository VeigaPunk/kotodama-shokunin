- Seat: Ca04 | verifier | Ca | date 2026-10-19 | baseline fd55e1f

# Ca04 — defect-queue-v2 consistency: strict JSON, row count, class vocabulary, duplicate ids

**Mission** (`reports/round-40/targets.json` seat `Ca04`): *"Queue-v2 consistency: strict JSON, row
count, class vocabulary, no duplicate ids."* Ca01's Owed block
(`calib/Ca01-queue-v2.md:469-471`) scopes this seat's checks to the same four plus a mechanical
owner-completeness re-check — all performed.

**Artifact under check at this seat's cut.** The integrator landing
`reports/round-40/op/defect-queue-v2.json` did **not** exist at cut time (`ls reports/round-40/op/`
→ no such directory, 2026-10-19 ~15:00Z). The check therefore targets the exact fenced JSON draft
bytes in `calib/Ca01-queue-v2.md:64-416`, extracted programmatically (regex on the first
```` ```json ```` fence) — never re-typed, never trusted from Ca01's prose. Draft-block digest for
byte-identity at landing: **sha256 `3edb4e52f22d91da343d1662284af9135322912a64e81be173440c41cc598121`,
33,616 bytes** (incl. trailing newline). All checks ran as one python3 script (json stdlib,
TMPDIR=$PWD/.scratch, PYTHONDONTWRITEBYTECODE=1) at HEAD `fd55e1f`, 2026-10-19. No
`reports/round-*/run-validation.py` executed; no filed byte read as writable; no corpus staging; no
git/network/install action.

## Verdict: ALL CONSISTENCY CHECKS PASS (20 checks; 1 first-pass flag adjudicated; 2 phrasing notes)

| # | Check | Result | Measured |
|---|---|---|---|
| 1 | Strict JSON parse | PASS | `json.loads` with `parse_constant` rejecting NaN/Infinity/-Infinity and strict strings: parses clean |
| 2 | No duplicate object keys | PASS | `object_pairs_hook` key census across every object in the document: 0 duplicates |
| 3 | Header consistency | PASS | `schema` `kotodama-defect-queue-v2`; `round` 40; `baseline_commit` `fd55e1f` |
| 4 | Row count ≥ 28 | PASS | **33 rows** (threshold 28 from `claims.json` claim Ca; Ca01 declares 33) |
| 5 | Class vocabulary closed | PASS | exactly {`carried-with-owner`: 25, `fixed-with-evidence`: 8}; no third value anywhere |
| 6 | New class recorded in notes | PASS | `notes` names `fixed-with-evidence` and the reason (r37 queue carried zero verified fixes; 8 rows now close with evidence) |
| 7 | No null ids | PASS | 0 (v1 had 5) |
| 8 | No empty ids | PASS | 0 |
| 9 | No duplicate ids | PASS | 33/33 unique |
| 10 | Field-set parity with v1 | PASS | every v2 row carries exactly the v1 key set {id, origin, class, owner, reason, next_touch, evidence, verification} — Ca01's `notes` claim verified true |
| 11 | Owner/reason/next_touch complete | PASS | 33/33 rows non-null, non-empty; **zero `owner: "unassigned"`** (v1 had 5) — the claim-Ca threshold "every row owner-complete" is met structurally |
| 12 | Fixed rows carry verification | PASS | 8/8 `fixed-with-evidence` rows have non-null `verification` (matches Ca01's notes claim) |
| 13 | v1 named-id coverage | PASS | all 19 named r37 ids present verbatim in v2 |
| 14 | Minted-id mapping | PASS | exactly 5 `R37-O01-CAND-*` ids for v1's exactly 5 `id: null` rows; each minted row's `origin` cites its distinct `id:null row 1..5` (1:1 by the declared order, `defect-queue.json:133-181`) |
| 15 | Census arithmetic | PASS | 19 named + 5 minted + 5 new r38 (`r38-guard-row-blindness`, `r38-frozen-row-asymmetry-census`, `r38-O02-fragment-defects`, `r38-O08-fragment-defect`, `r38-O07-empty-fragment`) + 4 new r39 (`r39-runner-root-regression`, `r39-basename-successor-instrument`, `r39-stray-corpus-staging`, `r39-review-findings-disposition`) = 33; matches `census_coverage` declared 24/5/4/33 and `r37_rows_accounted` 24 |
| 16 | Parent digest | PASS | declared `parent_sha256_at_assembly` `5cf827e2…860d5d` == this seat's `sha256sum reports/round-37/op/defect-queue.json` (filed bytes measured at HEAD fd55e1f) |
| 17 | next_touch route targets (lead-token) | PASS | 31 rows lead with an explicit target: r40 close (12), r41 (2), r42 (2), r43 (1), loop 2 (3), standing (2), external bilateral read (1), none-fixed (8) — every lane round named is in loop-1 positions 40–46 or loop 2/external by declared design (`REGIMEN.md:13-23`); **zero rows route back to r33–39** |
| 18 | First-pass stale-round flag — adjudicated | RESOLVED | a naive `r3x` regex over `next_touch` text flagged 13 rows; the lead-token check shows all 13 are inline citations ("the relative ROOT (… r33 shape…)", "never rewrite the filed r33 record", "the historical r34/r35/r36 records", census-alias names), not route targets — no defect |
| 19 | RC-4 / OI-02 phrasing variance | NOTE | these two next_touch values lack a leading round token but name in-window targets in-text: RC-4 "in the r42-r44 build window"; OI-02 "the implementation slot is r45" behind an operator scoping gate. Routes are loop-1-consistent; flagging as phrasing only, no defect |
| 20 | census_coverage honesty | PASS | `K02_r40_census_rows_seen: null` with the absence reason matches this seat's independent check: `ls reports/round-40/scout/` → K01-touched-census.md, K03-gaps.md only (**K02-queue-scout.md still absent at 15:05:11Z**) — null carried, not an inferred count |

## Consistency observations (non-blocking, filed for the integrator)

- **Class transition coherence**: the 8 `fixed-with-evidence` rows are exactly the rows Ca01's
  per-row table marks fixed (r37 integration ×1, r38 ×3, r39 ×4 by evidence class) and each cites
  a filed SCORECARD/LOG line plus a populated `verification` — the vocabulary move is
  evidence-gated, not label drift. Row-level truthfulness of each fix (origin sampling) is
  **Ca02's** lane (≥30% sample); this seat checked structure, not provenance.
- **Two-filed-rows-one-defect pairs** (`R36-ABSOLUTE-ROOT` ↔ `O12-runner-isolation-hazard`;
  `R36-R7-READSET-13` ↔ `r37-A01-readset-roster-defect`) are kept as separate ids with the alias
  relation stated in both rows' `reason` fields — id uniqueness is preserved and the dedupe
  decision is self-documenting in the artifact; consistent with the r37/r39 canonical-id rulings
  Ca01 cites.
- The draft's `rows` array is internally ordered v1-row-for-v1-row before the 9 new rows —
  diff-friendly for the integrator and for future censuses; noted, not required.

## Owed

- **Landing + landed-bytes re-parse** — the fenced draft lands as
  `reports/round-40/op/defect-queue-v2.json` (integrator-only; Ca01 `## Owed`). On landing,
  byte-identity is one check: landed-file sha256 must equal
  `3edb4e52f22d91da343d1662284af9135322912a64e81be173440c41cc598121`; if the integrator lands
  modified bytes, this seat's checks 1–17 must re-run on the landed file before validation.
  Owner: integrator (land) + Ca04-at-close (re-parse if bytes differ).
- **`scout/K02-queue-scout.md`** — still absent at this seat's cut (15:05:11Z; Ca01 noted absence
  at its earlier cut). The K02 cross-check of the census (minted-id mapping, the 9-new-row count)
  remains owed; Ca01's `census_coverage` null remains correct until it lands.
  Owner: K02, then Ca02/integrator.
- **Origin sampling** — row-content truthfulness vs r38/r39 records is `calib/Ca02-verify.md`
  (landed at this cut; not re-audited by this seat). Owner: Ca02.
- Not executed by this seat: no `reports/round-*/run-validation.py` (in-tree or copy), no filed-byte
  edit, no corpus staging, no git commit/push, no network/install.

## Citations

- `reports/round-40/targets.json` seat Ca04 (mission/out) and `shared_rules`; `reports/round-40/claims.json` claim Ca (`thresholds`: "row count >= 28; every row owner-complete"; `after_required` alignment).
- `reports/round-40/calib/Ca01-queue-v2.md:64-416` (the fenced draft bytes under check), `:469-471` (Ca01's Owed naming this seat's checks), `:57-60` (class + minted-id declarations).
- `reports/round-37/op/defect-queue.json:11-252` (v1 parent: 24 rows, 5 `id:null` at `:133-181`, single-class vocabulary); measured sha256 `5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d` at HEAD fd55e1f.
- This seat's command outputs (2026-10-19, HEAD fd55e1f): the 20-check python3 run (full PASS/FAIL transcript in seat transcript; per-check values in the table above); `ls reports/round-40/op/` → exit 2 (absent); `ls reports/round-40/scout/` → K01/K03 only at 15:05:11Z; draft-block sha256 `3edb4e52…c598121` (33,616 bytes).
- `REGIMEN.md:13-23` (loop-1 positions 41–46 provider/role table used for route-target adjudication).
