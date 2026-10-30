# Round 79 — kotodama pre-data lesson sections (DRAFT, not filed)

Seat: ScribeLesson (W1). Lane base `44f76d456c1b326a71ffdb381590af825cbf11be` (= HEAD at observation). Draft target for L1: `corpus/lessons/round-79.md`. Nothing here is landed. Tags: `[OBSERVED]` = re-opened by this seat from committed bytes or a committed receipt; `[INFERENCE]` = reasoning from observed bytes; `[PENDING-TOOL-PROOF]` = no executed check exists yet.

## Gate

No claim frozen. No knowledge entry admitted. No source row landed. Pre-freeze dispositions:

- **Dining / tableware coverage candidate — REJECTED, already held.** Content overlap, not a missing gap. Re-test output (`[OBSERVED]`, read-only grep at base, receipt `.ufo/waves/round-79/w1/stage/ScribeLesson/receipts/dining-retest.txt`):

  ```
  $ grep -n "^## 6" corpus/knowledge/culture-material/cuisine-food-lexicon.md
  90:## 6. Etiquette: the table as grammar
  $ grep -n -i "dining" corpus/knowledge/culture-material/furniture-interior-lexicon.md
  73:- **Boards and trestles first.** For most of European history the dining table was boards laid on trestles ...
  99:- **"The dining table and chair set is ancient."** The fixed table with individual chairs is an early modern arrangement ...
  ```

  `cuisine-food-lexicon.md` §6 (`:90-93`) holds table grammar and etiquette; `furniture-interior-lexicon.md` (`:73`, `:99`) holds the dining table as furniture. The round-79 draft's pre-freeze statement matches these bytes. Reject reason is review-only under QUALITY criterion 11 (overlap is a judgment); the grep output is the measurable part.

- **Ca (census-record correction) — candidate; no self-assessment mismatch found by this seat.** `[OBSERVED]` The only literal `S884` hits in `SCORECARD.md` and `LOG.md` are `SCORECARD.md:1480` (`reports/round-74/evidence/S884.txt`, quote 「这个我肯定考虑过」) and LOG/SCORECARD census lines that name `census-end.txt` generically. None names the S884 used-by token or the round-78 census-end receipt. `SHONEN.md` has no S884 or census-end reference. Per the draft's own pre-freeze rule (`CLAIMS-DRAFT.md`, "Pre-freeze scope disposition"), Ca is rejected as a claim before freeze unless L1 finds a corresponding self-assessment row; its correction lands as unclaimed conformance repair. `[INFERENCE]` The census-end defect is an evidence-record defect (QUALITY criterion 17), not a SCORECARD calibration statement.

- **O (ledger-token guard) — candidate, pre-freeze.** No counter exists in this seat. Its red fixtures are the round-77 probe ledger facts recorded in R79-M2 below. `[PENDING-TOOL-PROOF]`

- **Source registry.** No external source opened in this seat; no web access. One own-work row is drafted for L1 (`S897`, see `s897-row.draft.md`), tier A scoped to the lane's own re-runnable gate output, status `queued`, opened `2026-10-30`, used-by `—` until the lesson lands in the same commit (census E11 requires an existing used-by path).

- **Freshness** remains paused by open L0 round-11 (not touched here).

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R79-M1 | evidence record (routed defect 2 from round-78 spot-check): `reports/round-78/telemetry/census-end.txt:33` records S884 used-by `…worldbuilding-setting-practice.amend-2026-10-24-r13.md`; the registry it claims to validate carries `…amend-2026-10-23.md` | `reports/round-78/telemetry/census-end.txt:33` (sha256 `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`); `reports/round-78/telemetry/census-start.txt:33` (`…10-23.md`); `corpus/SOURCES.md:839` field 12 at `44f76d45` and at `4b255745` (`…10-23.md`); `corpus/knowledge/culture-material/` has no `…24-r13.md` file | non-author spot-check of round 78 (`corpus/lessons/round-78-verifier-spotcheck.md:66-67`); re-observed by this seat 2026-10-30 | Append-only correction (no rewrite of `census-end.txt`): bind the sha256 above, the measured revision (receipt carries no revision stamp; committed in `4b255745`), old token and actual token read from the row. Frozen counter must re-derive mismatch=1 at base and 0 after the correction. Do-nothing, lying correction, wrong revision and a changed receipt must each fail. `[PENDING-TOOL-PROOF]` (no counter exists). |
| R79-M2 | calibration pointer + unproven fix (routed defect 3): R78-M1 cites `ExecCaPass:24-34` for the red evidence; that range is the verdict header | Exact red: `.ufo/waves/round-77/w2/ExecCaPass.md:265-278` and receipt `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt:1-6` (sha256 `6e97b121e98120f7d5fa6378f7cb5eebe6f8e0c520e90bd7c13503b3e124e52b`). `MutCaLedger.md:43-84` is the D07 `HEAD` survivor (row e1 at `:53`), not BASEMISMATCH. | round-77 W2 `ExecCaPass` (graded legs) and `ScoutLogPairs` (`:45-57`, `:64-80`); re-observed by this seat | Correct the R78-M1 pointer in a new round-79 record (append-only; do not edit round-78.md). Build-check fix: `--ledger-check` must compare each recorded `observed_at_base` with the live observation and refuse `stated == observed`. Red-before must be a committed `--ledger-check` run on the probe showing FAIL for D01–D10 and D11 and for control V02 (`controls-summary.txt:83`, currently `rc=0`, fabricated `"999"` passes). `[PENDING-TOOL-PROOF]` |

### R79-M2 observed red, in full (`[OBSERVED]`)

```
graded-legs.txt:1  LEG FAIL BASEMISMATCH
graded-legs.txt:2  red=10 min=10 ids=['D01'..'D10'] green-at-base=['D11']
                   unobserved/miss=["D01:recorded-observed-at-base='1'!='149'", ... (D01–D10)]
graded-legs.txt:3  BASEMISMATCH_PASSED=False
graded-legs.txt:4  LEG FAIL REPAIR
graded-legs.txt:5  green=[] red=["D11(statement='253' truth='243')"]
graded-legs.txt:6  REPAIR_PASSED=False
```

Base facts re-observed by this seat (`receipts/observation-receipt.txt`): `git show 211f9526…:LOG.md | grep -c '^#'` = `149`; `corpus/README.md` at `211f9526` has totals `243 (:755)`, `247 (:798)`, `249 (:819)`, `252 (:830)`, `253 (:834)`.

Mechanism (`[OBSERVED]` in ExecCaPass §5.1 and ScoutLogPairs §2): D01–D10 share one `observe_cmd` returning `149`, yet record `observed_at_base: "1"`; the build check passes them because `observed_at_base` is type-checked only (`accept-ca.py:1712-1714`), while the BASEMISMATCH leg reads it at `:1866`. D11 observes the line it states, so stated = observed = `243` and it is not red at base.

Scope limits, stated (`[OBSERVED]`): the graded run was in-process (`graded-legs.py` calls the counter's leg functions with `lands = base = 211f9526`); no freeze, no lands tree and no `--selftest` leg of a fixed counter exist. The BASEMISMATCH half reads base only. The REPAIR half was measured with lands = base. ExecCaPass §5.2 says the same.

## Pending tool proof vs observed evidence

| item | status | basis |
|---|---|---|
| Round-77 probe ledger wrong `observed_at_base` (10 pairs) and D11 not red at base | `[OBSERVED]` | `graded-legs.txt:1-6`; `token-evidence.txt`; base `git show` re-run |
| Round-77 `--ledger-check` PASS 11 while the ledger fails BASEMISMATCH and REPAIR | `[OBSERVED]` | `ExecCaPass.md` §3, §5.2 |
| Build check admits fabricated `observed_at_base` (V02) | `[OBSERVED]` (W2 receipt) | `controls-summary.txt:83` `rc=0 want=0 OK` |
| `HEAD` accepted in revision position (D07 survivor) | `[OBSERVED]` (W2 receipt) | `MutCaLedger.md:53`, `:58-88` |
| Proposed R78-M1 fix (store observed token; refuse stated == observed) makes the build check red | `[PENDING-TOOL-PROOF]` | no implementation in `accept-ca.py`; W2 named it advisory only |
| Ca correction turns mismatch 1 → 0 under a frozen counter, and fails do-nothing / lying / wrong-revision / changed-receipt controls | `[PENDING-TOOL-PROOF]` | no counter; correction not written |
| Round-74 `fabricated-base-observation` control reds BASEMISMATCH | `[OBSERVED]` but for the round-74 counter only | `reports/round-74/telemetry/selftest-ca.txt:32` |
| Dining rejection correct as a "held" reason | `[OBSERVED]` overlap; review-only judgment | grep output above |

## Trends

- expansion: unchanged (no admitted entry, no registry landing).
- quality: unchanged (no entry re-verified or superseded).
- discernment: unchanged (no outside gate decision sampled by this seat).

## Routed to round 80

1. L1: decide Ca per the pre-freeze rule; if kept, land the append-only census correction (R79-M1) separably from O.
2. L1: land `S897` with the lesson in one commit (used-by = lesson path) or keep `queued` with used-by `—`.
3. O: a bounded ledger-token guard with committed red/green fixtures; `[PENDING-TOOL-PROOF]` for every clause.
