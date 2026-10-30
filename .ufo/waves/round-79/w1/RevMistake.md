# RevMistake — R78 fix "shown able-to-fail": historical red + same-command fixture proof

Seat: RevMistake (round-79 W1 reviewer). Date: 2026-10-30.
Lane base: `44f76d456c1b326a71ffdb381590af825cbf11be` (read-only; lane `git status --porcelain` shows only this round's untracked `.ufo/waves/round-79/`, `reports/round-79/`).
Scope: the R78-M1 fix text in `corpus/lessons/round-78.md:11` (committed `4b255745`) and its two cited evidence classes — the historical red and the same-command fixture proof. No lane/shared file edited; no git/jj mutation; no tool installs; no scratch needed (probes were read-only `git grep`/`git show` against committed bytes). Raw probe output: `.ufo/waves/round-79/w1/stage/RevMistake/probe-receipts.txt`.

## Verdict

- **Historical red: PRESENT.** W2's executed BASEMISMATCH failure on the recorded 11-pair probe is committed verbatim and re-derives today (probe 1 below: the ledger's own `observe_cmd` returns `149` at pinned base `211f9526800906e0c585d878d265c37e5e090c15`, while D01–D10 record `observed_at_base:"1"`; D11 is green-at-base `243==243`).
- **Same-command fixture proof: ABSENT.** The cited red and the operational green on the same input are *different commands*: the red was produced by a W2 import-driver calling `leg_basemismatch` directly; the command actually run on the probe (`--ledger-check`) is **green on the exact defect class** (committed V02 control). No command that both gates and fails on the recorded probe exists at base. Routed defect 3 of `corpus/lessons/round-78-verifier-spotcheck.md:68` stands: the fix is proposed, not demonstrated able-to-fail.

## F1 (HIGH) — the cited red and the green are not the same command

The R78-M1 fix (`corpus/lessons/round-78.md:11`) names its red-before as "W2's executed `BASEMISMATCH` failure on the recorded 11-pair probe". What was executed (`ExecCaPass.md` §5.2, §6):

- Command: `graded-legs.py` — a bespoke W2 driver that *imports* the round-77 counter (`accept-ca.py`, sha256 `ac2bc93d…`) and calls `evaluate_pairs` + `leg_basemismatch` + `leg_repair` in-process. It is not the counter CLI, not `--ledger-check`, not `--selftest`, and not any command that ships at base.
- Committed raw receipt `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt`:
  `LEG FAIL BASEMISMATCH red=10 min=10 ids=['D01'..'D10'] green-at-base=['D11'] unobserved/miss=["D01:recorded-observed-at-base='1'!='149'", …×10]` / `BASEMISMATCH_PASSED=False`; `LEG FAIL REPAIR red=["D11(statement='253' truth='243')"]`.

The command actually run on the same recorded probe by W1, and re-run green by W2 in three forms, is the pre-freeze build check:

- `python3 -B accept-ca.py --ledger-check probe-real-ledger.json --root <lane> --base 211f9526… --work <scratch>` → `LEDGER-CHECK-77: PASS pairs=11`, exit 0 (committed `.ufo/waves/round-77/w2/stage/ExecCaPass/lc-cwdscratch.out`; W1 receipt `ledger-check-real-base.txt`).

Same input family, opposite verdicts, *different commands*. The split-brain is by construction, confirmed in the counter source: `pair_problems()` type-checks `observed_at_base` only (`accept-ca.py:1712-1714`: `rec is not None and not isinstance(rec, str)`) and never compares it to the executed observation; the recorded-vs-actual comparison and the stated==observed refusal live only in `leg_basemismatch` (`accept-ca.py:1866-1876`). `run_ledger_check`'s own docstring grades "nothing else" (`accept-ca.py:3904-3969`).

**Decisive committed control.** `.ufo/waves/round-77/w2/stage/ExecCaPass/controls/V02-fabricated-observation.json` sets every pair's `observed_at_base="999"`, `expected_after="999"` — fabricated against the same observation that really yields `149` — and its committed output `.out` reads `LEDGER-CHECK-77: PASS pairs=11` (exit 0, admitted-green control). So the single command that was exercised on the historical probe greens the precise defect class R78-M1's fix targets. Under QUALITY 11 (each clause names the command that checks it and that command must be able to fail) and the QUALITY 23 addendum (a mutant's redness counts only against a green-first clean run of the *same* command), this pair cannot demonstrate the fixed behavior able-to-fail: there is no same-command red/green pair anywhere in the citation.

## F2 — historical red verified present (re-derived 2026-10-30)

- Probe 1 (raw in stage receipt): `git grep -c -E '^#' 211f9526800906e0c585d878d265c37e5e090c15 -- LOG.md` → `211f9526800906e0c585d878d265c37e5e090c15:LOG.md:149`, exit 0 — byte-for-byte the token the W2 receipts quote (ScoutLogPairs §3; ExecCaPass §5.1). The observation is read-only, pinned to a committed revision, and matches the recorded `observed_raw` in W2. Genuinely historical.
- Probe 2: `git show 211f9526…:corpus/README.md | grep -n "Total knowledge entries"` → `243`@755, `247`@798, `249`@819, `252`@830, `253`@834 — confirming the D11 site map (first-match parse `243` vs last-match `253`) that produces `green-at-base=['D11']` and the REPAIR red.
- Both defect classes the fix names have an executed historical instance: recorded≠actual (D01–D10, one shared observation across ten ids) and stated==observed (D11).
- The receipts are durable: every W2 file cited is tracked (`git ls-files .ufo/waves/round-77/w2/` — reports and stage receipts committed).

## F3 — no green exists for any fixed command (freeze-blocking)

At base `44f76d45` there is no round-79 guard/counter implementation; the R78 lesson itself says "This remains a routed lesson, not a round-78 implementation claim", and the round-78 verifier spot-check routed defect 3 (`corpus/lessons/round-78-verifier-spotcheck.md:68`) repeats "proposed but not yet demonstrated able-to-fail; per CORPUS.md it does not count as landed until red-before evidence is committed." My read confirms: the fix's able-to-fail evidence does not exist yet, because the fixed command does not exist yet. This is a freeze requirement for O (and the same shape applies to Ca's correction counter), not a historical-evidence problem.

## F4 (LOW) — two citation cautions

1. **Count the red honestly.** D01–D10 are one physical observation (`git grep -c -E '^#' … -- LOG.md`) wearing ten ids — probe 4 of the stage receipt: ten identical `"observed_at_base": "1"` fields sharing one `observe_cmd`/`rederive`/`parse`. The historical red is therefore two defect instances (recorded≠actual ×10 syntactic; stated==observed ×1), not eleven independent observations. Accurate as cited ("failure on the recorded 11-pair probe"), but freeze fixtures should model the two classes separately.
2. **Do not underclaim the round-77 selftest either.** The round-77 counter's own `--selftest` already carries same-command red+green for BASEMISMATCH on *synthetic* fixtures — scenarios `fabricated-base-observation` (sets `pairs[0]["observed_at_base"]="0"`, expects `{"BASEMISMATCH":"FAIL","LEDGER":"PASS"}`) and `green-pair` (expects `{"BASEMISMATCH":"FAIL","LEDGER":"PASS"}`), source `accept-ca.py:3705-3727`, coverage map `:3851`; receipt `selftest.out` committed and re-run byte-identical by W2 (`ExecCaPass.md` §2, `SELFTEST: 199/199`). That demonstrates the round-77 *leg function* firing on synthetic data — which W2 never disputed — not the fixed guard, and not on the historical probe. Cite it as leg-function provenance only.

## What the freeze must show (requirements for ExecGuard / ExecOCounter / ExecCaCounter / ScribeClaims)

Derived from QUALITY 11, 12, 23 (+addendum), 25(b), 26:

1. **One declared command, both colors.** The acceptance command named in `claims.json` (guard probe command and/or counter acceptance leg) must be run **verbatim** on one fixture family: a clean fixture that exits 0 in the same receipt, then the same command on (a) a fixture whose recorded `observed_at_base` ≠ the re-run observation and (b) a fixture with stated token == observed token — each printing its stable red label and non-zero exit. The W2 `graded-legs.py` import-driver shape does not qualify (it is not the declared command), and a `--ledger-check`-shaped build check that stays green on V02 does not qualify.
2. **Clean-green-first in the same receipt** (QUALITY 23 addendum limb 2): the receipt's first scenario line must be `clean -> exit=0` before any mutant row; a red mutant compared against a red clean baseline counts for nothing.
3. **Historical anchor for the Ca lesson, re-derived at the named revision** (QUALITY 12/29): the mismatch=1 statement must name `reports/round-78/telemetry/census-end.txt` at `4b255745…` and the registry blob at the same revision; my probes show the method (read-only `git grep`/`git show` at the pinned 40-hex) that satisfies this.
4. **Committed receipts at the FREEZE commit, lands absent** (QUALITY 23/25b): selftest receipt plus the junk/do-nothing landings the counter must reject, all generated at freeze, not typed.

## Commands run (all read-only against the lane; raw output preserved)

```
git grep -c -E '^#' 211f9526800906e0c585d878d265c37e5e090c15 -- LOG.md
git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/README.md | grep -n "Total knowledge entries"
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD ; git -C … status --porcelain
grep -o '"observed_at_base": "[^"]"' .ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json | sort | uniq -c
```

## Verification gaps / unrun

- I did not re-execute `graded-legs.py` or `--selftest`: both are historical receipts already committed and independently re-run byte-identical by W2 (`ExecCaPass.md` §2, §6); re-running them would add no information about the *fixed* command, which does not exist at base.
- The round-79 O guard / Ca correction counter do not exist at base; their able-to-fail evidence is by definition unrun and is owed at freeze per F3.
- Adjacent known survivor (out of this seat's scope, cross-ref only): MutCaLedger §2 `HEAD`-in-revision-position coverage finding.
- No model parameters, no live network access, no pacman/host changes this seat.
