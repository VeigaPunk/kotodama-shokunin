# RevMalformed — round-79 W1: malformed calibration-ledger schema

Seat: RevMalformed (reviewer, leaf, no subagents). Lane: `kotodama-shokunin`, base `44f76d456c1b326a71ffdb381590af825cbf11be`.
Status: review and probe only. No lane file edited, no git mutation, no shared file touched. The O guard (`tools/ledger-token-guard.py`) does not exist yet, so nothing here is an implementation check; every "PASS/FAIL/CRASH" below is what the existing round-76 Ca counter did on a fixture.

Stage: `.ufo/waves/round-79/w1/stage/RevMalformed/`

## 1. Scope and inputs read

- Draft: `.ufo/waves/round-79/CLAIMS-DRAFT.md` (O: bounded ledger-token guard; Ca: one S884 correction; pre-freeze, no data landed).
- Rules: `corpus/QUALITY.md` criteria 7, 9, 11, 17, 19, 23, 25, 26, 27, 28, 29 (criterion 11: each clause shown able to fail; criterion 25(a): freeze-pinned constants, refuse non-commit; criterion 29: numbers re-derived from the artifact they name).
- Schema source: the ledger header and clauses in `.ufo/waves/round-73/counters/accept-ca.py` (lines 1-60, committed at base), and the executed loader in `reports/round-76/accept-ca.py` (blob `d58b7ee8…`, file sha256 `c1fc755e…`; the most recent committed Ca counter).
- Committed ledgers, read through `git show 44f76d45:…` only: `reports/round-73/ledger.json` … `reports/round-76/ledger.json`.
- Historical scratch: `.ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json` and `ledger-check-real-base.txt` (scratch probe, not a lane file).

## 2. Method

1. `build_fixtures.py` creates an isolated scratch fixture repo (explicit `git init`, root asserted equal to the fixture dir, fixed commit dates) with `notes.md` at BASE `b953602f88dfa328ff8f21c60a4326a91d42b926`, then commits 63 ledger variants (`fixtures/<ID>.json`) at FIXCOMMIT `cefda0ac…`. Two independent runs produce identical BASE and FIXCOMMIT hashes (verified; the manifest differs only in its scratch `fixture_repo_root` field).
2. Every fixture is a one-field mutation of control C00 (valid 10-pair ledger), so a verdict is attributable to the named field.
3. `probe_malformed.py` runs each fixture through the R76 counter's real `show()`, a verbatim mirror of its `load_frozen` ledger block (lines 893-906), its real `evaluate_pairs()` and its real `leg_ledger()`, after setting the same run state `main_check` sets (lines 2688-2691, 2727). Raw output: `probe-raw.txt`.
4. `summarize.py` derives every count below from `manifest.json` and `probe-raw.txt`. Counts are not typed by hand.
5. `historical_compat.py` checks a proposed strict allowlist against committed ledger bytes: `historical-compat.txt`.

The counter was imported, not run end to end. Its selftest was not run (not requested for this seat).

## 3. Results

Controls (must not be refused): C00 valid control, C01 CRLF, C02 same site and text with a different `observe_cmd` (the committed R74 LC-15/LC-18 shape), C03 documented extra keys. **All four PASS** under R76, so the baseline is valid.

Must-refuse set: 58 fixtures (63 minus 4 controls minus 1 floor case M56, which is a count failure, not malformed input). Derived by `summary.txt`:

| R76 observed on a must-refuse fixture | count | fixtures |
|---|---|---|
| **SILENT-ACCEPT** (LEDGER PASS) | 13 | M11 M17 M19 M20 M21 M22 M24 M57 M42 M48 M49 M50 M51 |
| **CRASH** (uncaught exception, not a verdict) | 9 | M08 M15 M16 M32 M33 M37 M43 M44 M45 |
| refused by FAIL (reason may be incidental) | 36 | all others |

Crash detail (raw lines in `probe-raw.txt`): M08 `pairs: null` → `TypeError` in load; M15 invalid UTF-8 → `UnicodeDecodeError` in `show()`; M16 200 000-deep nesting → `RecursionError` in load; M32/M33 `stated_text` number/list → `TypeError` in evaluate; M37 `parse: true` → `TypeError` in evaluate; M43 `stated_token: 12345` → `AttributeError`; M44 `stated_parse: 5` → `TypeError`; M45 `expected_after: 1` → `AttributeError` in the LEDGER leg.

## 4. Findings (by severity)

**H1 — A missing or empty comparison field is a silent pass (the O/Ca guard's core input).** R76 checks `observed_at_base` only when the key is present (`leg_ledger`: `rec = pair.get(...)`; `if rec is not None and not isinstance(rec, str)`). Missing (M57) passes; empty string (M48) passes; `stated_token: ""` (M42) silently falls back to `stated_text`; the typo key `observed_at_bse` (M49) passes with no error.
- Real instance: `round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json` pair **D11** (REPAIR, `corpus/README.md:755`) has no `observed_at_base`; `ledger-check-real-base.txt` prints `LEDGER-CHECK-77: PASS pairs=11`. The comparison the guard exists to make is skipped for exactly that pair.
- Historical: R73's `reports/round-73/ledger.json` has no `observed_at_base` on any of its 8 pairs (`historical-compat.txt`). The guard must classify R73 as UNSUPPORTED-SHAPE, not PASS.
- Requirement: `observed_at_base` is required per pair, a non-empty string, and missing refuses (never skips).

**H2 — Duplicate keys are silently last-wins.** `json.loads` keeps the final value. M21 (`round` 79 then 76) and M22 (`expected_after` "1" then "9") both PASS. `parse-diag` flags the keys (`dup_keys=['round']`, `['expected_after']`) but nothing refuses. Historical: none of R73–R76 has a duplicate key (`historical-compat.txt`), so refusing costs no committed ledger.
- Requirement: `object_pairs_hook` that refuses a repeated key at any depth.

**H3 — Junk and duplicate pairs are silently counted.** M11 (10 valid pairs plus a string, `null` and number): the load filter `[p for p in … if isinstance(p, dict)]` drops non-objects without a problem record; PASS. M24 (F-11 is F-01 with only the id changed): accepted as a 11th unique pair against a floor of 10; PASS. "Unique" is therefore only by id.
- Requirement: any non-object element REFUSE; exact duplicate `(stated_at, stated_text, observe_cmd)` REFUSE under a different id. Do **not** refuse same site and text with a different `observe_cmd`: C02 and committed R74 LC-15/LC-18 (`corpus/README.md:36`, observed at `65fe857…` and `94209e8…`) are that legitimate shape. `historical-compat.txt` shows no exact duplicate in R73–R76.

**H4 — Exit-code collision: a malformed input can exit as a red leg.** Nine must-refuse inputs escape as uncaught exceptions. The counter's own contract is `EXIT: 0 all … pass; 1 any leg fails; 2 input error or REFUSAL` (`reports/round-76/accept-ca.py:28`). The counter's exception handlers catch only `ValueError`, `OSError`, `FileNotFoundError`, `subprocess.TimeoutExpired`, `re.error` and `ScratchRefused` (`exit-code-probe.txt`). In this interpreter (Python 3.14.8) an uncaught `RecursionError`, `TypeError` or `ValueError` exits **1** (`exit-code-probe.txt`). So a `TypeError` from a bad field produces the same status as a leg FAIL.
- Observed: the interpreter exit codes. Inferred [INFERENCE]: the same status for the whole counter, from the grep of its handlers and the interpreter result; a full-path run was not executed.
- Requirement: every parse and validation path returns exit 2 with a stable `REFUSE:<CLASS>` label; a top-level catch maps any remaining exception to `REFUSE:INTERNAL` with exit 2, never exit 1.

**M1 — Non-finite JSON constants accepted.** `NaN` in an unvalidated pair field (M19) and `Infinity` (M20) PASS. `NaN` as `round` (M18) is refused only incidentally: the message reads `round=nan != frozen round 76`. Historical: none (`historical-compat.txt`: `non-finite constants: none`). Requirement: `parse_constant` refuses.

**M2 — Numeric type drift.** `round: 76.0` PASS (M51), because `76.0 == 76`. `round: true` is refused only because `True != 76`; `bool` is an `int` subclass, so a frozen `1` would accept it. Requirement: `type(x) is int`, excluding bool.

**M3 — No size cap.** An 8 MiB ledger (M17) PASSes. The largest committed ledger is 53 057 B (R74). Proposal: cap 1 MiB, a 20x margin, to be frozen before data.

**M4 — Refusals name the wrong cause.** BOM (M12), trailing `x` (M13), two concatenated documents (M14), empty file (M01/M02), `null` (M03), bare list (M05), and empty array (M04) all FAIL with `round=None != frozen round 76` or `pairs=0` rather than naming BOM, trailing data or the empty file. Requirement: the guard's label names the class (`BOM`, `TRAILING`, `EMPTY`).

**L1 — Falsy coercion.** `parse: 0` (M38) is refused by the LEDGER leg (`parse is not a string`), but `parse_observed` (`if parse:`) would have used the raw stdout for it. `expected_after: ""` (M46) is refused, `observed_at_base: ""` (M48) passes; the two are inconsistent. Requirement: no value is coerced by truthiness.

**L2 — Unknown parse sentinel reads as a regex.** `parse: "count_presence"` (M58, typo of the sentinel) compiles and FAILs only for "has no capture group". Requirement: the guard accepts `count-presence` or a compiling regex with a group, and reports an unknown sentinel by name.

**L3 — Empty pair object.** M59 (`{}` appended) FAILs with seven problems, which is acceptable; the guard should report it as `REFUSE:EMPTY-PAIR`.

## 5. Proposed strict schema for the guard (for ExecGuard and L1; not frozen)

Parse layer, in order (each refusal = exit 2, label):
1. Read bytes; size ≤ 1 MiB → `SIZE`.
2. No UTF-8 BOM → `BOM`. Strict UTF-8 decode → `UTF8`.
3. `json.loads(…, object_pairs_hook=…, parse_constant=…)`: repeated key at any depth → `DUPKEY`; `NaN`/`Infinity`/`-Infinity` → `NONFINITE`. `ValueError` (includes trailing data) → `JSON` (label `TRAILING` when the message says "Extra data"). `RecursionError` → `DEPTH`. Any other exception → `INTERNAL`.
4. Top level must be an object → `TYPE`. Top-level extra keys are allowed (R74 has 27 top-level keys) and are recorded in the receipt, not used.

Header (frozen constants, read with `git show <freeze>:…`):
- `round`: `type(x) is int` and equal to the frozen round → `TYPE`/`MISMATCH`.
- `claim`: exact `"Ca"`. `base`: lowercase 40-hex and equal to the frozen base → `FORMAT`.
- `fleet_pin`: `null` or lowercase 40-hex (R76 `fleet_pin: null` is committed history).
- `pairs`: a list (non-list → `TYPE`); length ≥ frozen `min_pairs` → `FLOOR`; every element an object → `NONDICT`.

Pair (allowed keys only; anything else → `UNKNOWNKEY`):
- Required: `id` (non-empty after strip, exact-unique → `DUPID`); `disposition` ∈ {`REPAIR`,`ANNOTATE`} → `ENUM`; `stated_at` str; `stated_text` non-empty str; `observe_cmd` non-empty list of non-empty str → `TYPE`; `parse` non-empty str that is `count-presence` or compiles with ≥1 group → `REGEX`; `expected_after` non-empty str → `EMPTY`; `observed_at_base` non-empty str → `MISSING`/`EMPTY`/`TYPE`.
- Optional, typed: `stated_parse` str (compiles, ≥1 group); `stated_token` non-empty str (empty → `EMPTY`, never a fallback); `red_at_base` bool; `rederive` str; `why` str; `observed_note` str; `statement_after` object `{path: str, parse: str with group}`; `stated_fleet` object `{path: str, line: int, not bool}`.
- Duplicate content: exact `(stated_at, stated_text, observe_cmd)` under two ids → `DUP-CONTENT`.
- `observe_cmd`: the R76 argv grammar (allowlist, no shell metacharacters, no interpreter) is out of this seat's scope; see routing.

Allowed pair keys (union of R73–R76 history, `historical-compat.txt`): `id disposition stated_at stated_text stated_parse stated_token observe_cmd parse expected_after observed_at_base red_at_base rederive why statement_after stated_fleet observed_note`.

## 6. Historical compatibility (`historical-compat.txt`)

| ledger | bytes | dup keys | non-finite | pairs | keys outside allowlist | required missing | verdict under the proposal |
|---|---|---|---|---|---|---|---|
| R73 | 5 792 | none | none | 8 | none | `observed_at_base` ×8 | **UNSUPPORTED-SHAPE** (honest; not a pass) |
| R74 | 53 057 | none | none | 13 | none | none | admitted shape |
| R75 | 10 646 | none | none | 10 | none | none | admitted shape |
| R76 | 20 203 | none | none | 20 | none | none | admitted shape (`fleet_pin: null`) |

The R77 scratch file (`r77-probe-real-ledger-check.txt`) is not a lane ledger; under the proposal D11 is REFUSE `MISSING`.

## 7. Fixture set (for ExecGuard's selftest, to be frozen before data)

`stage/RevMalformed/manifest.json` gives id, class, description, byte count, sha256, expected strict label and expectation. `fixtures/` holds 61 verified copies (sha256 re-checked); M16 (400 KB) and M17 (8 MiB) are recipe-only and rebuilt by `build_fixtures.py`.

- Must accept (4): C00 C01 C02 C03 (R76 PASS on all four).
- Floor, not malformed (1): M56 (9 pairs; R76 FAIL `pairs=9 < min-pairs=10`).
- Must refuse, by the label the guard should report (derived from `manifest.json`, 58 total):

| label | fixtures |
|---|---|
| EMPTY | M01 M02 M06 M07 M26 M27 M46 M48 M59 |
| TYPE | M03 M04 M05 M08 M09 M10 M11 M25 M28 M32 M33 M34 M35 M36 M37 M38 M43 M44 M45 M47 M50 M51 M52 M53 |
| BOM / TRAILING / UTF8 / DEPTH / SIZE | M12 / M13 M14 / M15 / M16 / M17 |
| NONFINITE | M18 M19 M20 |
| DUPKEY / DUPID / DUP-CONTENT | M21 M22 / M23 / M24 |
| ENUM / REGEX / FORMAT | M29 M30 M31 M54 / M39 M40 M41 M58 / M55 |
| FALSY / UNKNOWNKEY / MISSING | M42 / M49 / M57 |

Note: M51 (`round: 76.0`), M38 (`parse: 0`) and M50 (`red_at_base` string) are labelled TYPE in the manifest.

## 8. Reproduce

```
sh .ufo/waves/round-79/w1/stage/RevMalformed/repro.sh <explicit scratch dir>   # git show of counter blob, fixture build, probe
python3 -B .ufo/waves/round-79/w1/stage/RevMalformed/summarize.py .ufo/waves/round-79/w1/stage/RevMalformed
python3 -B .ufo/waves/round-79/w1/stage/RevMalformed/historical_compat.py <lane> 44f76d456c1b326a71ffdb381590af825cbf11be
```
Fixture build is deterministic (commit hashes identical across runs). The scratch directory was removed after the receipts were copied.

## 9. Not done, and what this does not show

- The O guard is not written. No guard selftest was run, so nothing here shows the guard refuses these fixtures. The expectations in the manifest are a proposal, not a frozen contract.
- The R76 counter was imported and its functions called; its full `main_check` path was not run. The exit-code finding is therefore inferred from grep and an interpreter probe (H4 marked [INFERENCE]).
- Fixtures use only the synthetic `notes.md`; no S-id ≥ 876, no claim-C path, no lane source (separability holds for these bytes).
- Not covered by these fixtures: whether `observed_at_base` *equals the actual observation* (the stated==observed vacuity is MutVacuous's area), the `observe_cmd` argv grammar (SentinelExec, MutRevision), path traversal in `stated_at` (MutPath), and freshness or coverage of any kind (out of scope; no coverage or freshness claim).
- No numeric score and no coverage claim is made.

## 10. Routing and open items for L1

- MutRevision / SentinelExec: the R77 scratch D11 `observe_cmd` is `['grep','-o','-E','Total knowledge entries: [0-9]+','corpus/README.md']` — no revision operand, so it reads whatever `corpus/README.md` is in the directory it runs in, not pinned bytes. The guard grammar must refuse a revision-less observe.
- RevFreeze: the 61 stage fixture copies and the M16/M17 recipes are candidates for the freeze commit (QUALITY 23(b)/25(b)); nothing is committed yet, and the freeze hash is not verifiable from the lane.
- ExecGuard: adopt the parse-layer order in §5 and the label names in §7; refuse, never coerce; top-level catch to exit 2.
- Criterion 23 and QUALITY 25–26: R76's exception path is the crash-as-verdict class in §4 H4. The O guard must not reuse that path; R76 itself is historical and is not repaired here.

## 11. Tools and installs

No tool installed or updated. Interpreter: Python 3.14.8 (system). Git 2.56.0 (system). No `uv`, `npm`, `cargo` or pacman action. Scratch: `/fast/scratch/hyaku/kotodama-r79/RevMalformed*` created explicitly and removed after the receipts were copied; all three scratch directories are gone.

Report: `.ufo/waves/round-79/w1/RevMalformed.md` (relative to `kotodama-shokunin`)
