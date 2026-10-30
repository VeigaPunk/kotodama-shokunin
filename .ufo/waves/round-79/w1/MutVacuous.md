# MutVacuous — round 79 W1: guard mutation, stated token vs observed

Seat: MutVacuous (mutation-tester, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base: `44f76d456c1b326a71ffdb381590af825cbf11be`. Probe base (round-77 ledger base): `211f9526800906e0c585d878d265c37e5e090c15`.
Stage: `.ufo/waves/round-79/w1/stage/MutVacuous/` (fixtures, drivers, raw outputs, `expected-verdicts.json`, `commands.sh`, `SHA256SUMS`).

## 0. Bottom line

1. **Equality is caught, but only as a detail string.** When a pair's stated token equals its observed base token, the round-77 BASEMISMATCH leg fails and lists the pair under `green-at-base` (M1, M2, f01, f02). It is not a stable label and it is not separated from other failures.
2. **Invalid stated tokens are counted as mismatches, so the leg can pass vacuously.** The stated side is never classified as invalid before the equality test. An empty or whitespace-only `stated_token` is treated as a valid red pair (M4, f04, f05). A missing `stated_token` silently becomes the whole `stated_text`, which can never equal a short observation (M3 PASS with 11/11 red; f12 PASS with 10/10 red while every recorded observation was correct).
3. **The observation side is ordered correctly for parse-miss and dead-pin**: those are unobservable, not red (M5, M6, f06, f07). But two observation defects are not classified as invalid: a parse-less output longer than 200 characters is truncated and compared (a stated token equal to the full output counts red, M7/f09), and a multi-match observation silently takes the first occurrence (f08, D11 in the probe).
4. **The `--ledger-check` pre-freeze path cannot see stated == observed at all** (L-stated-eq-observed-D11 PASS). It also accepts empty and whole-sentence stated tokens and an absent `observed_at_base`. Only the lands-time BASEMISMATCH leg compares stated to observed.
5. **The round-77 probe's FAIL is not evidence that stated == observed is caught.** At base the probe ledger's 10 "red" pairs are one shared observation (LOG.md heading count 149) tested against incidental numbers, and its recorded `observed_at_base` is `"1"` where the counter observes `149`. Its only green pair (D11) is green because the observation takes the first of five footer lines.

Verdict for the guard design: the required separation is achievable with a boring classifier (section 5). Nothing here has been implemented; no guard exists at base.

## 1. Scope and what was run

- Read: `CLAIMS-DRAFT.md` (round 79), `corpus/QUALITY.md` criteria 11, 23, 25–29, `corpus/lessons/round-78.md` R78-M1 (line 11), `.ufo/waves/round-77/w2/MutCaLedger.md` (mutation table, e1 survivor), `corpus/lessons/round-78-verifier-spotcheck.md` (routed defects 2/3).
- Counter under test: the round-77 stage copy `.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py` (sha256 `ac2bc93d…489b2e`). **There is no committed round-77 counter at base** (`git ls-tree 44f76d45 -- reports/round-77` is empty). The committed round-76 counter `reports/round-76/accept-ca.py` has the same `stated_token`/`observed_token` code (`:1337`, `:1355–1368`, `leg_basemismatch` `:1644–1679`); that is by code reading only, not run.
- Method: the counter's `leg_basemismatch` and `evaluate_pairs` were called in-process against a base clone (`materialize`, `observed_token`), and `--ledger-check` was run as a subprocess. The counter source was not modified. Clones and scratch were under `/fast/scratch/hyaku/kotodama-r79/MutVacuous/work`, removed after the receipts were copied to the stage.
- Observed values are the counter's own `observed_token` at base (not assumed): D01–D10 = `149`, D11 = `243`. The first run (`out/basemismatch-run1.txt`) assumed `1` for D01 and was superseded by `out/basemismatch-v2.txt` and `out/final-run-raw.txt`; the stage keeps all three for transparency.
- Not run: any guard (none exists), any selftest, build, lint, or test. No lane file was edited. `git status` in the lane shows only untracked `.ufo/waves/round-79/` and `reports/round-79/` (not this seat's).
- Tool installs: none. Used system `python3` (stdlib only) and `git`.

## 2. Mutation table (raw results; full text in `stage/MutVacuous/out/`)

Base observed tokens (counter's `observed_token`): D01–D10 `149`, D11 `243`.

| id | mutant | round-77 BASEMISMATCH result (raw detail, abridged) | verdict | expected guard (unrun) |
|---|---|---|---|---|
| V0 | probe as committed | `FAIL red=10 … green-at-base=['D11'] unobserved/miss=[D01..D10 recorded-observed-at-base='1'!='149']` | red is driven by recorded-observation misses | exit 1, D01–D10 INVALID-OBSREC-MISMATCH, D11 INVALID-OBS-MULTIMATCH |
| V0b | probe minus `observed_at_base` | `FAIL red=10 green-at-base=['D11']` | red = incidental numbers; D11 green via first-match | exit 1 |
| CTRL | `clean-control-v2` (10 truthful pairs, correct `observed_at_base`) | `PASS red=10` | mechanical pass only (tokens are dates/incidental digits) | exit 0 |
| M1 | D11 `stated_token := 243` (new==observed) | `FAIL … green-at-base=['D11']` | caught, as detail text only | exit 1, GREEN-AT-BASE(D11) |
| M2 | every pair stated := observed | `FAIL red=0 green-at-base=[all 11]` | caught | exit 1, GREEN-AT-BASE ×11 |
| M3 | no stated token/parse anywhere, no `observed_at_base` | **`PASS red=11 min=10`** | **VACUOUS PASS** (whole stated text as token) | exit 1, INVALID-STATED-DERIVED ×11 |
| M4 | D02 `'   '`, D03 `''` | **`PASS red=11`** (D02 stated `''` counted red; D03 `''` fell back to whole text) | **invalid counted as mismatch** | exit 1, INVALID-STATED-EMPTY ×2 |
| M5 | D04 parse matches nothing | `FAIL red=9 unobservable=[D04:parse-miss]` | correct ordering | exit 1, INVALID-OBS-PARSEMISS |
| M6 | D05 observe pinned to a dead object | `FAIL red=9 unobservable=[D05:invalid-observe_cmd … dead pin]` | correct ordering | exit 1, INVALID-OBS-DEADPIN |
| M7 | T01 parse-less, stated := full 11,199-char observation | **`PASS red=10`** (T01 counted red against a 200-char truncated observation) | **equality decided against truncated value** | exit 1, INVALID-OBS-OVERCAP |
| M7b | T01 stated := 200-char prefix | `FAIL green-at-base=['T01']` | the prefix is "equal", the full text is "red" | exit 1, INVALID-OBS-OVERCAP |

Fixture-file matrix (`out/fixture-matrix-raw.txt`; LEDGER = `--ledger-check`, BM = BASEMISMATCH leg):

| fixture | LEDGER (r77 counter) | BM (r77 counter) | expected guard |
|---|---|---|---|
| f00 truthful clean | PASS | PASS red=10 | exit 0 |
| f01 C03 stated := observed | FAIL (`'27' not anchored`) | FAIL green=[C03] red=9 | exit 1, GREEN-AT-BASE(C03) |
| f02 all stated := observed | FAIL (8 anchor problems) | FAIL red=0 green=10 | exit 1, GREEN-AT-BASE ×10 |
| f03 C01 no stated token | PASS | PASS red=10 | exit 1, INVALID-STATED-DERIVED(C01) |
| f04 C02 `'   '` | PASS | **PASS red=10** | exit 1, INVALID-STATED-EMPTY(C02) |
| f05 C02 `''` | PASS | **PASS red=10** (C02 stated = whole text) | exit 1, INVALID-STATED-EMPTY(C02) |
| f06 C04 parse-miss | FAIL | FAIL unobservable=[C04] | exit 1, INVALID-OBS-PARSEMISS |
| f07 C05 dead pin | FAIL | FAIL unobservable=[C05] | exit 1, INVALID-OBS-DEADPIN |
| f08 C06 multi-match (5 footers, first taken) | FAIL (rederive artifact) | **PASS red=10** (C06 `'0'` vs first `243`) | exit 1, INVALID-OBS-MULTIMATCH |
| f09 C07 no parse, full text as token | FAIL (parse missing) | **PASS red=10** | exit 1, INVALID-OBS-OVERCAP |
| f10 C08 `observed_at_base` absent | PASS | **PASS red=10** | exit 1, INVALID-OBSREC-MISSING |
| f11 C09 `observed_at_base` = `'1'` (actual `2`) | PASS | FAIL unobserved/miss=[C09] | exit 1, INVALID-OBSREC-MISMATCH |
| f12 every stated token removed, obs recorded correctly | PASS | **PASS red=10** | exit 1, INVALID-STATED-DERIVED ×10 |
| r77-probe-pristine | PASS | FAIL (see V0) | exit 1 |
| L-stated-eq-observed-D11 | **PASS** | n/a | exit 1, GREEN-AT-BASE(D11) |
| L-empty-token-D02 / L-ws-token-D02 | **PASS** | n/a | exit 1, INVALID-STATED-EMPTY(D02) |
| L-whole-sentence | **PASS** | n/a | exit 1, INVALID-STATED-DERIVED |
| L-no-observed-rec | **PASS** | n/a | exit 1, INVALID-OBSREC-MISSING |

Bold = a defect the round-77 leg passes. "Expected guard" is what ExecGuard must output; it is a specification, not a run.

## 3. Answer to the assignment question

**New == observed versus invalid, before mismatch.** The round-77 leg orders the observation side correctly: `obs is None` is unobservable and never red (`accept-ca.py` stage `:1854–1857`), and the parse-miss and dead-pin cases confirm it (M5, M6, f06, f07). It orders the **stated** side incorrectly:

- `stated_token()` returns `(norm(x), True)` for an explicit `stated_token` (`:1525–1526`). `norm("   ")` and `""` are therefore treated as *valid* tokens, the `tok is None` check at `:1859` never fires, and the pair goes to the red/green comparison (`:1862`).
- `stated_token()` treats an empty `stated_token` as absent (`if pair.get("stated_token")` is falsy) and silently falls back to `norm(stated_text)` (`:1528`). A whole sentence never equals a short observation, so it is always red.
- The `stated_parse` branch does the right thing (`:1523`: empty capture → invalid). The two branches are inconsistent.
- The LEDGER anchor check (`:1709`, `tok not in stated_text`) passes both the empty string and the whole text, so `--ledger-check` never rejects them (L-* PASS).

Equality itself (`norm(tok) != norm(obs)`) only collapses whitespace. It is correct for valid inputs (M1, M2). It is wrong when the observed side is truncated (F3) or ambiguous (F4).

## 4. Findings (ranked)

**F1 — HIGH: whole-text stated token gives a vacuous PASS.** `stated_token()` fallback (`:1527–1528`; r76 `:1366–1368`). M3 (no derivation at all, no `observed_at_base`) → `PASS red=11`. f12 (correct `observed_at_base` kept) → `PASS red=10`. Ledger anchor check `:1709` is trivially satisfied (token is a substring of itself). Kill rule for the guard: a token equal to `norm(stated_text)` is INVALID-STATED-DERIVED; no fallback.

**F2 — HIGH: empty/whitespace explicit token is counted as mismatch.** `:1525–1526` (`norm` → `""` returned as valid). f04/M4 red includes a `''` stated token; f05/`''` falls through to F1. Kill rule: `norm(token) == ""` → INVALID-STATED-EMPTY, checked before any comparison, in both branches.

**F3 — HIGH: observation truncated to 200 characters before equality.** `:1497` `norm(out)[:200]` (r76 `:1337`). A stated token equal to the actual 11,199-char output is counted red (M7); the 200-char prefix is green (M7b). The truncation is silent. Kill rule: output longer than 200 after norm → INVALID-OBS-OVERCAP, never truncated.

**F4 — HIGH: multi-match observation takes the first occurrence.** `parse_observed` uses `rx.search` (`:1490`, first match). At base `corpus/README.md` has five `Total knowledge entries:` lines (`:755` 243, `:798` 247, `:819` 249, `:830` 252, `:834` 253; `git grep -n` at `211f9526`). D11 (`corpus/README.md:755`, stated `243`) is green because it reads the first and superseded footer, while REPAIR's `statement_after` (`:1568`, `matches[-1]`) reads the last. f08 shows a multi-match red. Kill rule: `len(matches) != 1` → INVALID-OBS-MULTIMATCH (or an explicit declared occurrence policy, which must be frozen).

**F5 — MEDIUM: `observed_at_base` is optional, and the pre-freeze path does not check its value.** `:1866` only checks when the field is a string. f10 (absent) and L-no-observed-rec PASS. f11 (wrong value) FAILs in BASEMISMATCH but PASSes `--ledger-check`. Kill rule: required, and compared to the actual observation in the ledger check as well.

**F6 — MEDIUM: `--ledger-check` (the "same pair validation LEDGER runs") cannot see stated == observed.** L-stated-eq-observed-D11 PASS. The R78-M1 fix text (`corpus/lessons/round-78.md:11`) asks for the rejection of stated == observed, but the only place it is enforced is the lands-time BASEMISMATCH leg. The guard must apply the equality rule at ledger-check time as well.

**F7 — MEDIUM: the probe's "10 red" is one observation tested against incidental numbers.** D01–D10 share one `observe_cmd` (`git -C . grep -c -E '^#' 211f95 -- LOG.md` = 149) and their `stated_parse '([0-9]+)'` captures the first digit run of a heading or sentence (`## 2026-10-17 …` → `2026`; `II.386.` → `386`; `18-whole/…` → `18`). The "≥10 unique pairs" floor counts ids, not independent observations. The clean control (f00/CTRL) passes on the same mechanism, so the guard can verify mechanics but not claim-bearing tokens. This is a review-only residual under QUALITY 11/29, and it must be named in the freeze, not hidden in a green count. Route: RevFreeze, RevMalformed, L1.

**F8 — MEDIUM (record): the R77 probe's recorded `observed_at_base` values do not match the counter's observation.** D01–D10 record `"1"`; the counter observes `149` at base; D11 has no recorded value. R78-M1's claim that the red-before evidence is "BASEMISMATCH failure on the recorded 11-pair probe" is true only in this sense: the failure comes from these recorded-observation misses (and D11 green), not from the equality rule R78-M1 asks for. Route: ScoutR77Truth.

**F9 — LOW (note): fixture artefacts.** f01/f02 trip `not anchored` at LEDGER level because the control's stated text is a verbatim base line whose digit run is not the observed value. This confounds the LEDGER result for the equality fixtures; the BASEMISMATCH result is unaffected. f08 fails `rederive` parsing and f09 fails the parse-missing and rederive-token checks, both because of how those fixtures were built. Kept as recorded, not repaired.

## 5. Recommended guard grammar (for ExecGuard; boring, one pass per pair, first failing label wins)

1. **Stated side (schema):** explicit `stated_token` or a `stated_parse` with a non-empty capture; `norm(token)` non-empty (INVALID-STATED-EMPTY); token ≠ `norm(stated_text)` (INVALID-STATED-DERIVED); len ≤ 200; token occurs in `stated_text` (INVALID-STATED-NOTANCHORED).
2. **Observed side:** argv allowed by the frozen grammar; object exists in the base clone (INVALID-OBS-DEADPIN); output non-empty (INVALID-OBS-EMPTY); `norm(output)` ≤ 200 chars, no truncation (INVALID-OBS-OVERCAP); exactly one parse match (INVALID-OBS-MULTIMATCH / -PARSEMISS).
3. **Recorded observation:** `observed_at_base` present (INVALID-OBSREC-MISSING) and `norm` equal to the actual observation (INVALID-OBSREC-MISMATCH).
4. **Equality:** `norm(stated) == norm(observed)` → GREEN-AT-BASE (reject, listed, never counted). Only otherwise → MISMATCH.
5. **Exit:** 0 only if every pair is MISMATCH and the floor holds; 1 for any labelled rejection; 2 for refusal or error. Labels are fixed strings, printed one per pair.
6. **Run at `--ledger-check` as well as at lands.** The equality rule must not depend on the lands-time leg.
7. Consider a freeze-level rule that counts **distinct observations** (distinct `observe_cmd` argv) toward the floor, so that shared observations (F7) cannot inflate the red count. This is a freeze decision; the seat does not impose it.

## 6. Fixtures and controls (under the stage)

- `fixtures/` — 19 ledger files: the R77 probe (`r77-probe-pristine.json`, identical to `pristine.json`), the truthful control (`clean-control-v2.json` = `f00`), f01–f12 single-defect mutants derived from the control, and L-* ledger-check mutants.
- `expected-verdicts.json` — per fixture: observed round-77 LEDGER/BASEMISMATCH outcome and expected guard exit and labels. `expected_guard` is marked unrun.
- `driver/mutvacuous-basemismatch.py` (V-series, M1–M7b, ledger-check mutants), `driver/matrix-driver.py` (fixture matrix), `driver/make-fixtures.py`, `driver/build-clean2.py`. `driver/exploration-driver-*.py` are superseded exploration scripts, kept for transparency.
- `out/` — raw outputs: `final-run-raw.txt`, `fixture-matrix-raw.txt`, `ledger-check-mutants.txt`, `baseline.txt`, `basemismatch-run1.txt` (superseded), `basemismatch-v2.txt`, `basemismatch-clean-control-v2.txt`, `ledger-check-clean-control-v2.txt`, `sha256-check.txt`.
- `SHA256SUMS` — 38 entries, verified with `sha256sum -c` (exit 0, all OK).
- Reproduce: `WORK=<explicit scratch> sh .ufo/waves/round-79/w1/stage/MutVacuous/commands.sh` (reads the lane and the round-77 stage counter; writes only under `WORK`).

## 7. Limits (stated)

- Ran the round-77 **stage** counter, not a committed counter. The round-76 committed counter has the same `stated_token`/truncation code, read but not run.
- The leg was called in-process; the lands/freeze wiring, the selftest and the rest of the counter were not exercised.
- No guard exists at base; every "expected guard" entry is a specification for ExecGuard, not a result.
- Mutation coverage is single-defect per fixture plus one all-pairs variant. It does not prove the guard is complete for the whole argv grammar; the observation grammar (`git grep` pins, `:` ambiguity, option injection) belongs to MutRevision/MutPath.
- Semantic falseness (a stated token that is not the claim) is not decidable mechanically (F7).
- Observation cost: each run materialized a base clone; no timeout or output-cap test of the counter's own `run_observe` was done (SentinelLimits).

## 8. Routed to others (not edited here)

- ScoutR77Truth: F8 (recorded `"1"` vs observed `149`; D11 first-match vs REPAIR last-match).
- MutObserved: the observed_at_base cross-check (F5, F8) from the observation side; the probe's values are not an off-by-one.
- MutRevision / MutPath: observation-grammar mutants (pinned objects, `HEAD` in revision slots); the dead-pin case here is only one example.
- RevFreeze / RevMalformed / L1: F7 distinct-observation floor; whether the empty-token and whole-text rules are frozen as criteria.
- ScribeLesson / R78-M1 wording: the red-before claim should say the probe failed on recorded-observation misses and on a first-match green, not on the equality rule.

Report: .ufo/waves/round-79/w1/MutVacuous.md
