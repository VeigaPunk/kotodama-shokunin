# RevSource — round 79 W1: own-work S897 provenance tier / quote / source benefit

Seat: RevSource (leaf, reviewer). Base `44f76d456c1b326a71ffdb381590af825cbf11be`.
Scope: the own-work S897 registry row the O claim will cite; no external source
claims. Full evidence and raw probe output:
`.ufo/waves/round-79/w1/stage/RevSource/FINDINGS.md` and `stage/RevSource/probes/`.

## Verdicts

**Tier A — correct, observed.** The drafted row cites
`.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt` (committed at base,
sha256 `6e97b121…4e52b`), the executed BASEMISMATCH/REPAIR failure on the round-77
11-pair probe ledger — the exact red-before R78-M1 names. Tier A is grounded by
re-running, not by the contract phrase alone: I copied `graded-legs.py`,
`ledger.json`, `accept-ca.py` (all committed) into scratch and re-executed; the
stdout is **byte-identical** to the committed receipt. The lane tier definition
reserves A for "the lane's own re-runnable gate output"; precedent S859/S860 use
the same shape for own-work rows.

**Quote — ≤25 words, exact path/line, dated 2026-10-30.** Anchor quotes
`:1` 「LEG FAIL BASEMISMATCH」 and `:2` 「recorded-observed-at-base='1'!='149'」
both `grep -n -F`-located on committed bytes; the underlying mismatch is
independently re-derived read-only (`git grep -c -E '^#' 211f9526… -- LOG.md` →
…`:LOG.md:149` vs the probe ledger's recorded `"1"` ×10; D11 green at base,
243=243). Corroborating 20-word prose quote at ScoutLogPairs.md `:14-16` if L1
prefers the audit record.

**Source benefit — real, bounded.** (1) Gives O's red fixture a stable registry
id instead of inline paths (QUALITY 7-safe citation of pre-existing wave
records). (2) Census-integrated: mirror probe shows rows 820→821, tier.A
493→494, `validate --file` exit 0 with zero E-codes. (3) Honest provenance:
kind `own-work` is a census enum; the source cell has URL=(none) so QUALITY
10/16/18 live-fetch obligations do not bind; used-by stays out of
corpus/knowledge — no knowledge-coverage claim. (4) The id is free (0 S897 rows
at base; last id S896), but the round-77 staged external S897 (魏斌/CSSN, still
present read-only in the shokuknow merge package) never landed; the lesson Gate
should minute that lane S897 is now the own-work row so a future revival of that
theme renumbers or supersedes instead of colliding (E03).

## Controls (all run, raw output preserved)

Scratch census mirrors with the row inserted after S896 inside `## Registry`:
as-drafted (queued, used-by `—`) → clean exit 0; tier `D` → `E06`; `mined`+`—`
→ `W03`; `mined`+missing lesson path → `E11`; `mined`+stub lesson → clean for
S897. One construction defect found and kept as a receipt: a row appended at
file end trips `E12 row outside Registry section` — insertion point is after
S896. Consequence for freeze: `queued`+`—` is the only clean pre-land shape;
the `mined` flip must land in the same commit as `corpus/lessons/round-79.md`
(matching ScribeLesson's used-by plan, now control-verified).

## Not claimed

No external source opened; no live fetch; no knowledge admission; the round-79
guard tool itself is `[PENDING-TOOL-PROOF]` (no implementation check run or
claimed). Ca must not cite S897 (J7/SEPARABLE class). Scratch
`/fast/scratch/hyaku/kotodama-r79/RevSource/` removed after receipts copied to
stage. No installs; no git/jj mutations anywhere.
