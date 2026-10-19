- Seat: Ca02 | verifier | Ca | date 2026-10-19 | baseline fd55e1f

# Ca02 — defect-queue-v2 origin sample: 24 of 33 rows (72.7%) verified against filed records

**Mission** (`reports/round-40/targets.json` seat `Ca02`): *"Sample >=30% of the v2 rows against
their origin records; disagreements filed."* Threshold in `claims.json` claim Ca: row count >= 28,
every row owner-complete.

**Method.** The v2 under test is the fenced JSON in `reports/round-40/calib/Ca01-queue-v2.md`
(33 declared rows). Every sampled row was checked against its **origin records** (the filed r37
queue `reports/round-37/op/defect-queue.json`, LOG.md, SCORECARD.md, r38/r39 round records) and
against **this seat's own HEAD measurements** (2026-10-19, HEAD `fd55e1f`,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`) — never against Ca01's prose. Sample
selection is falsifiability-weighted: all HEAD-mechanically-checkable `fixed-with-evidence` rows,
both worsening claims, every new r38/r39 row whose existence is one command away, plus the alias
lifecycle — so the sample over-represents the rows most likely to hide a wrong claim. The 9
unsampled rows are all static no-movement / external-owner / future-reconciliation rows (listed
under Owed). No filed byte was edited; no `reports/round-*/run-validation.py` was executed; no
corpus byte staged; no git-mutating/network/install action taken.

## Verdict: 24/24 sampled rows MATCH their origins; 0 substantive disagreements; 1 citation-precision finding; 1 sub-claim carried by record

| # | v2 row id | check run by this seat | verdict |
|---|---|---|---|
| 1 | F-C13-1 | incident text at LOG.md:3548-3567 (r5/r6/r7 receipts rewritten in-tree, restored byte-exact, guard-adoption gap, writer `to-verify`); recurrence LOG.md:3695-3698; r33 relative shape confirmed at `reports/round-33/run-validation.py:23`; protocol file exists (`reports/round-39/calib/isolation-replay-protocol.md`, 2829 B); no-recurrence statements at O03-verify.md:34 and r39 S01:80 | MATCH |
| 2 | R36-D-DECLARATION | SCORECARD.md:746-757 — r38 depth row, claim D admitted (r36 register residue), receipt `88db61bf…`; LOG.md:3725-3738 "D (verified)" | MATCH |
| 3 | R36-D-F6 | SCORECARD.md:748-750 (derived_forms=8/derived_ok=8 live, corrected formula); LOG.md:3731-3733 "live counters 8/8" | MATCH |
| 4 | R36-D-RL8 | SCORECARD.md:750 (D4L-ARGOT-ERA, 39/39 controls, argot host per X01 T1); LOG.md:3732-3734 | MATCH |
| 5 | R36-README-E3-PLACEHOLDERS | SCORECARD.md:681-684 ("two `__E3_PLACEHOLDER__` lines (removed; sweep re-green)"); HEAD `grep -n __E3_PLACEHOLDER__ corpus/README.md` → NO_MATCH (exit 1) | MATCH |
| 6 | R36-README-ORDER-CONTIGUITY-REVERIFY | SCORECARD.md:770-772 — r39 coverage row: "README rev 2.2 sweep-green 216==216"; LOG.md:3757-3758 | MATCH |
| 7 | R36-ABSOLUTE-ROOT | six-runner census re-derived: absolute `ROOT = "/home/vgpnk/…"` + `os.chdir` at r34 (:10/:26), r35 (:9/:36), r36 (:8/:13), r37 (:5/:10), r38 (:5/:13), r39 (:5/:13); r33 is the relative shape (:23) | MATCH (line-precision nit, finding N-1) |
| 8 | R36-README-DUPLICATE-HEADING | `grep -n '^# kotodama-shokunin corpus index' corpus/README.md` → lines 1 and 3, count 2; r39 X00-7 at X00-connector.md:252-256 (sweep-blind, separate-recorded-act rule) | MATCH |
| 9 | R37-O01-CAND-HISTORICAL | O01-queue-draft.md:287-293 — candidate_ids [R34-N1, CO4, R35-route-402, R36-route-402], "R34-N1 was explicitly closed in r35 … Do not reopen"; SCORECARD.md:794-795 "remains historical, not a current blocker"; 1:1 minted mapping to the filed fifth id:null row by next_touch text | MATCH |
| 10 | O10-runner-sha256-null | `grep -n runner_sha256` → `reports/round-38/validation.json:130` null, `reports/round-39/validation.json:126` null, `reports/round-36/validation.json:167` null (three receipts); SCORECARD.md:684-685 "carried as O10" | MATCH |
| 11 | O12-runner-isolation-hazard | canonical-id rule at R07-cross-review.md:13 ("O08 and O12 … must merge into one canonical queue item") and r39 X00-4 at :236-239 ("a third row would regress the r37 dedupe"); v2 keeps exactly two rows (O12 + alias) — no third id; successor ledger `recount-ledger-successor.json` folds exactly 4 c-n-r rows R37-Ca-05..08 `reproduced-under-protocol` + the R01-1 ruling in its note; Ca02-replay-verify.md exists | MATCH |
| 12 | basename-couples-policy | policy file exists; SCORECARD.md:774-775 (r39 calibration row: "documented as policy"); R01-review.md:33 "Ca04 verify — D1 reproduced live by this seat; verdicts confirmed" | MATCH |
| 13 | readme-prediction-vs-delivery | r39 X00-3 at X00-connector.md:230-234 ("C06's receipt should predict by staged-tree sha and cite the post-apply sweep"; cites `defect-queue.json:242-251` — row present in the filed queue) | MATCH |
| 14 | r36-in-tree-runner-incident | LOG.md:3695-3698 (r35 runner executed in-tree during r36 wave, restored); no-recurrence: O03-verify.md:34 (r38) + r39 S01:80 (r39, "in-tree or in a copy"); r40 targets.json shared_rules carry the ABSOLUTE rule | MATCH |
| 15 | r37-A01-readset-roster-defect | alias lifecycle shared with #8's row: r37 A01 adjudication ("roster defect, not packet corruption" — SCORECARD.md:678-680); r38 guard sha e5812751… + "r7 chain exit 0, packet 45f57132… byte-identical" at LOG.md:3735-3738 and SCORECARD.md:751-753; loop-2 fix route (no re-freeze round in 41-46, REGIMEN.md:13-23) | MATCH |
| 16 | r38-guard-row-blindness | O03-verify.md:134-140 §3 "The shared blind spot — both filed guards are row-blind" (guard reads live `V3_READ_SET`, never `baseline["inputs"]`); named at LOG.md:3739-3741 and SCORECARD.md:759-762 | MATCH |
| 17 | r38-frozen-row-asymmetry-census | O03-verify.md:171-180 §3.2 four-row G5 table (filed rows measured 12-vs-12 OK vs the asymmetric four); X02-honesty.md:160 §4a "A second filed row carries the same mismatch" + :250-253 (component landed r27); three independent sources (O03, O08, X02) | MATCH |
| 18 | r38-O07-empty-fragment | `wc -c reports/round-38/op/O07-scribe.md` → 0; LOG.md:3741 "O07's 0-byte fragment recorded"; SCORECARD.md:760 | MATCH |
| 19 | r39-runner-root-regression | HEAD read: :2 docstring `"""Round-38 acceptance runner."""` (stale, round-wrong), :5 absolute ROOT, :13 `os.chdir(ROOT)`; spec conflict confirmed: r38 X01-trades.md:365-370 ("copy the reports/round-33/run-validation.py:23 relative-ROOT shape, never the r34/r35 absolute os.chdir shape") and r39 S01:391 ("The ROOT line is the load-bearing one. Five filed runners carry the absolute shape" — five through r38, r39's own is the sixth) | MATCH (line-precision nit, finding N-1) |
| 20 | r39-basename-successor-instrument | landed policy `grep -n -i "blocker\|disposition\|block extraction" reports/round-39/calib/basename-couples-policy.md` → NO_MATCH (D1+D2 not applied, landed verbatim — exactly the choice Ca04-verify.md:107-112 anticipated); D1/D2 substance at Ca04-verify.md:78-105 (wrapped field phonetics-phonology.md:72-77, 4 tokens / 2 phantoms; C12-row-2 blocker leg absent) | MATCH (sub-claim by record, finding N-2) |
| 21 | r39-stray-corpus-staging | LOG.md:3753 "corpus/knowledge/verification/C03-draft.md removed at integration"; SCORECARD.md:777 "the stray C03 staging file (removed, digest-proven)"; twice-observed class framing consistent with LOG.md:3695-3698 analogue | MATCH |
| 22 | r39-review-findings-disposition | R01-review.md:25-34 verdict table carries R01-2..R01-14; `grep -c 'R01-' reports/round-39/validation.json` → 0; LOG.md r39 entry names R01-1 alone (:3759-3760; successor-ledger note folds R01-1); SCORECARD.md:777 names R01-1 alone | MATCH |
| 23 | r38-O02-fragment-defects | O03-verify.md:255-262 §4.1 "D-1 — O02 §2's selftest count `44` is wrong; the artifact yields `45`" (§4 "Defects in O02"); section anchor matches the row's three D-1..D-3 claims | MATCH (D-2/D-3 anchors in the same §4, not line-read) |
| 24 | r38-O08-fragment-defect | O03-verify.md:308-315 §4.4 "D-4 — O08 and O01 declare different patched-tool digests; O08's citation of O01 is false" (O01 declares e5812751…; O08's ae22013b… is a variant) | MATCH |

## Structural + census checks (all PASS)

- **Parent digest**: `sha256sum reports/round-37/op/defect-queue.json` →
  `5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d` — byte-identical to the v2's
  `parent_sha256_at_assembly`. The parent is untouched.
- **Strict JSON**: the fenced block parses with `json.loads` (no trailing commas, no comments).
  33 rows; row count 33 ≥ 28 threshold. Zero duplicate ids. Zero rows with empty `owner`.
  Class vocabulary is exactly {`carried-with-owner`, `fixed-with-evidence`} and the new class is
  declared in the v2 `notes`.
- **Census arithmetic**: r37 parent = 24 rows (this seat's parse), all `carried-with-owner`
  (confirming the v2's "r37 vocabulary had no fixed rows" claim), of which 12 named census rows +
  5 `id: null` rows + 7 later-origin rows = 24. v2 = 24 + 5 r38 rows + 4 r39 rows = 33. The five
  minted ids map 1:1 to the filed id:null rows by next_touch text (all five texts read at the
  filed queue; each v2 origin line quotes its row's text faithfully, incl. the CAND-HISTORICAL
  "preserve the historical r34/r35/r36 records" mapping).
- **Next-touch alignment vs REGIMEN.md:13-23**: r41 = codex mid-loop verify, r42 = devin build,
  r43 = zai-low build, r44 = antigravity-3.8 build, r45 = antigravity-4-argon deep/hard,
  r46 = swe-2 read-only audit — every lane-round next-touch in the sampled rows lands on the
  right position; the two deliberately-not-aligned items (loop-2 re-freeze work; the external
  lore bilateral read) are marked as such in the v2.

## Findings filed (not silently fixed)

- **N-1 (citation precision, minor, owner: Ca01/integrator at landing)**: the v2's
  R36-ABSOLUTE-ROOT, F-C13-1, and r39-runner-root-regression rows cite the r39 runner's chdir as
  `:12`; this seat's `grep -n "os.chdir" reports/round-39/run-validation.py` → **:13**
  (`:12` is `RENDERER_SHA_UNUSED`). The `:5` ROOT and `:2` docstring citations are correct. The
  hazard claim itself is fully verified; only the line number should be corrected when the v2
  lands (`:5,:13`), per the corrections-as-new-records rule.
- **N-2 (sub-claim carried by record, not re-executed)**: the r39-basename-successor-instrument
  row's tail claim — the filed r19 instrument FAILs the admitted sacred-kingship entry (15
  unresolved, exit 2) — is accepted here on Ca04-verify.md:54-63 (exact command + output
  recorded) plus R01's independent D1 confirmation; this seat did not re-run the instrument.
  Re-running it corpus-wide is already the row's own next-touch (r43/r44 successor instrument).
- No substantive disagreements: no sampled row's owner, class, origin, or next-touch contradicts
  its origin records; both worsening claims (O10 null-streak, six-runner absolute census) were
  re-derived first-hand and hold.

## Owed

- **`scout/K02-queue-scout.md`** — still ABSENT at this seat's close (`ls reports/round-40/scout/`
  → K01-touched-census.md, K03-gaps.md only). The K02 cross-check on the census (minted-id
  mapping, r38/r39 finding count) remains open; owner K02, then Ca02 re-sample if the scout
  contradicts anything sampled here. Ca01's `census_coverage.K02_r40_census_rows_seen: null`
  stays correctly open.
- **Unsampled rows (9 of 33 — all static no-movement / external-owner / future-reconciliation)**:
  F-C15-1, RC-4, OI-02, R36-R7-READSET-13 (alias lifecycle sampled via #15),
  R37-O01-CAND-TIMEKEEPING, R37-O01-CAND-R35-AUDIT-F1-F13, R37-O01-CAND-OI-LEDGER,
  R37-O01-CAND-RC-README-PRED, contract-digest-lore-drift. Their v2 fields match the r37 parent
  verbatim on read-through; a full-field sample can ride the r41 verify round.
- **Landing**: the fenced v2 + N-1's line correction land at
  `reports/round-40/op/defect-queue-v2.json` — integrator-only. Owner: integrator.
- **Ca04-consistency.md / Ca03-receipt.md**: mechanical JSON/vocabulary/owner re-check and the
  calibration receipt are separate seats' outs (Ca04, Ca03); this seat's structural checks
  corroborate but do not replace them.

## Citations

- `reports/round-40/targets.json` (seat Ca02 mission/out; shared_rules ABSOLUTE rules);
  `reports/round-40/claims.json` (claim Ca before/after/thresholds: row count >= 28, rows
  owner-complete).
- `reports/round-40/calib/Ca01-queue-v2.md` — the v2 under test (fenced JSON, 33 rows; census_coverage;
  Owed naming this seat).
- `reports/round-37/op/defect-queue.json` — 24 filed rows, 5 `id: null` next_touch texts
  (this seat's python parse; sha256 `5cf827e2…` re-measured).
- `reports/round-37/op/O01-queue-draft.md:287-293` (CAND-HISTORICAL exclusion).
- `reports/round-37/review/R07-cross-review.md:13` (canonical-id merge directive).
- LOG.md — :3548-3567 (F-C13-1 incident), :3695-3698 (r36 recurrence), :3725-3743 (r38 entry:
  D/O verified, named findings), :3745-3761 (r39 entry: C/Ca verified, stray at :3753, R01-1).
- SCORECARD.md — :673-685 (r37 rows + integration repairs: E3 removed, O10 carried),
  :746-762 (r38 row + named findings), :764-779 (r39 row + named findings), :781-795 (routing
  history, "remains historical").
- `reports/round-38/op/O03-verify.md` — :34 (no in-tree execution), :134-140 (§3 row-blindness),
  :171-180 (§3.2 G5 table), :255-262 (§4.1 D-1), :308-315 (§4.4 D-4);
  `reports/round-38/op/O07-scribe.md` (wc -c → 0); `reports/round-38/cross/X01-trades.md:365-370`
  (relative-ROOT ruling); `reports/round-38/cross/X02-honesty.md:160,250-253` (§4a).
- `reports/round-39/cross/X00-connector.md` — :230-234 (X00-3), :236-239 (X00-4), :252-256 (X00-7);
  `reports/round-39/review/R01-review.md:25-34` (verdict table R01-2..R01-14);
  `reports/round-39/calib/Ca04-verify.md:54-63,78-115` (r19-gate FAIL; D1/D2; Owed);
  `reports/round-39/calib/recount-ledger-successor.json` (4 rows + R01-1 note);
  `reports/round-39/calib/isolation-replay-protocol.md`; `reports/round-39/calib/basename-couples-policy.md`
  (grep NO_MATCH); `reports/round-39/scribe/S01-integration-draft.md:80,391,438`;
  `reports/round-39/run-validation.py:2,5,13` (stale docstring, absolute ROOT, chdir);
  `reports/round-38/validation.json:130`, `reports/round-39/validation.json:126`,
  `reports/round-36/validation.json:167` (runner_sha256 null ×3).
- Runner census (this seat, HEAD fd55e1f): absolute ROOT+chdir at
  `reports/round-{34,35,36,37,38,39}/run-validation.py` (grep -n per file); relative at
  `reports/round-33/run-validation.py:23`.
- This seat's HEAD greps: `corpus/README.md` H1 count 2 (lines 1,3); `__E3_PLACEHOLDER__` no-match.
