# S897 — own-work registry row (DRAFT for L1; not appended to `corpus/SOURCES.md`)

Opened 2026-10-30 by seat ScribeLesson (round 79, W1). Own-work: no external URL, no access-control question. Opened by ordinary means (plain read of committed bytes and a committed receipt).

## Row (11 cells, one line)

```
| S897 | kotodama lane own-work: round-77 W2 receipt `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt` (sha256 `6e97b121e98120f7d5fa6378f7cb5eebe6f8e0c520e90bd7c13503b3e124e52b`), the round-77 counter's BASEMISMATCH and REPAIR legs applied in-process to the W1 11-pair Ca probe ledger at base `211f9526800906e0c585d878d265c37e5e090c15` | own-work | A | the lane's own re-runnable gate output, scoped to the recorded `observed_at_base` against the live observation on the round-77 probe ledger at base 211f9526; not an external source, not a freeze verdict, not knowledge | `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt:1` 「LEG FAIL BASEMISMATCH」; `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt:2` 「recorded-observed-at-base='1'!='149'」 | ten recorded base observations `"1"` are false against the live `^#` count `149` at base, so BASEMISMATCH is red on D01-D10 and green on D11; the O guard must reproduce this recorded-versus-live comparison | queued | 2026-10-30 | on-change | — |
```

## Why each cell

- **kind `own-work`**: enum accepted by `scripts/sources-census.sh` (E05). Precedent: S859 and S860 use `own-work` with `tier A` for a repo-path re-runnable check (`corpus/SOURCES.md`, rows S859–S860).
- **tier A**: the contract defines A as "the lane's own re-runnable gate output". `graded-legs.py` and `accept-ca.py` are tracked beside the receipt (`git ls-files` at HEAD), so the scope is re-runnable at base. Tier is curation: if L1 judges the in-process run insufficient, use B and say so.
- **anchor quotes**: counted by `grep -n -F` on the committed receipt. Line 1 is `LEG FAIL BASEMISMATCH`. Line 2 contains `recorded-observed-at-base='1'!='149'` 10 times on one line (`grep -o | wc -l` = 10). Quote length: 4 words, under the 25-word limit.
- **status `queued`, used-by `—`**: the lesson path does not exist until L1 lands it. Census E11 fails a used-by path missing on disk, and W03 flags `mined` with `—`. Flip to `mined` with used-by `corpus/lessons/round-79.md` in the same commit that lands the lesson.
- **recheck `on-change`**: symbolic cadence (census `symbolic()` accepts `^[A-Za-z][A-Za-z0-9 _-]*$`), reported and never judged overdue. The receipt is immutable; the cadence is a change trigger.

## Shape check (`[OBSERVED]`, scratch only)

Scratch fixture `corpus/SOURCES.md` = lane registry with the row inserted after S896 (`receipts/SOURCES.fixture-with-S897.md`). Read-only symlinks to `corpus/knowledge`, `corpus/lessons`, `SKILL.md`, `reports` supply the used-by targets so E11 resolves; without them `validate --file` in scratch reports 753 E11 (fixture-layout noise, not row defects).

| check | base (`44f76d45`) | with S897 row |
|---|---|---|
| `validate --file` exit | 0 | 0 |
| E-codes emitted | 0 | 0 |
| census `rows` | 820 | 821 |
| census `tier.A` | 493 | 494 |
| census `status.queued` | 58 | 59 |
| findings naming S897 | — | 0 |

Receipts: `receipts/validate-base-file.txt`, `receipts/validate-fixture-with-S897.txt`, `receipts/SHA256SUMS.txt`. Root-mode `validate --root <fleet> kotodama` at base prints `kotodama ok` (rc 0; `receipts/census-validate-head.txt`). Root-mode after landing is `[PENDING-TOOL-PROOF]` (lands with L1).

## Not claimed

- No external source, no knowledge coverage, no admission. The row only supports the O guard's red fixture.
- The row does not certify the round-77 ledger as valid; it records the defect.
