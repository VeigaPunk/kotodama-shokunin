# Loop-1 retrospective — regimen 2, rounds 33–46

Closed 2026-10-19 at lane HEAD `acd37c2`. Loop 1 = 14 positions; 13 executed
(position 13, argon, skipped per operator ruling — antigravity lanes non-functional).
**Score: 9 admitted / 4 honest-stops.**

## Per-round verdicts

| pos | round | provider/model | verdict | notes |
|---|---|---|---|---|
| 1 | 33 | opencode-go deepseek | admitted | regimen-2 opening |
| 2 | 34 | opencode-go deepseek | admitted | |
| 3 | 35 | opencode-go deepseek | admitted | |
| 4 | 36 | hyper->devin deepseek | rejected (D) | stale premise; C/Ca verified |
| 5 | 37 | luna-max | admitted | verify round |
| 6 | 38 | grok->devin | admitted | grok 403 -> devin fallback |
| 7 | 39 | zai glm-flash | admitted | |
| 8 | 40 | zai glm-flash | admitted | |
| 9 | 41 | luna-max | admitted | mid-loop verify |
| 10 | 42 | devin deepseek | rejected (C) | lithic collision ruling |
| 11 | 43 | opencode-go deepseek* | rejected-honest-stop | O+C stale premises; Ca improved |
| 12 | 44 | opencode-go deepseek* | rejected-honest-stop | O landed+improved; C/Ca unverified |
| 13 | 45 | argon | **skipped** | antigravity lanes broken (operator ruling) |
| 14 | 46 | devin swe-2 | admitted | git-hygiene audit — chain clean |

*positions 11/12 scheduled zai/antigravity; operator-redirected to opencode-go.

## What loop 1 produced

- **Corpus:** 211 → 223 entries (six partitions; myth-symbol grew to 26; the lithic
  register landed via r42 C04 after a collision ruling).
- **Operability:** `tools/harness/` gained the couples resolver chain — r42
  `couples-reference-extractor.py` (N6 fix) demoted at r44 by
  `basename-couples-resolver.py` (four-class census authority, 27/27, 223/2730);
  plus `round_runner_conformance.py`, the relative-ROOT template, the
  manifest-roster guard, and the argot-era leg.
- **Calibration:** defect-queue-v2 (38 rows) → r43 dispositions (r38/r39 rows
  classed, successor-pinned); MANIFEST fidelity audited clean at r46.
- **Honest stops:** 4 — r36 (stale premise), r42 (collision), r43 (stale O+C
  premises), r44 (carried-candidate + undelivered gate). The honest-stop rule is
  working as designed: no forced pass.

## Defects carried into loop 2

- `R01-43-12`-class freshness gate — the method is proven (r44 scratch prototype)
  but no durable tool; owner integrator. Loop-2 pre-dispatch should run it manually.
- The stale-premises pattern (claims not re-measured at baseline): r43 and r44 both
  hit it. The r46 audit confirms the ledger stayed honest through them.
- `basename-couples-resolver.py` latent edge: a blank-separated hyphen soft-wrap
  continuation drops tokens (0 live incidence; recorded successor note).
- Antigravity lanes (gemini-3.8-flash, gemini-4-argon) non-functional on this host —
  all three antigravity positions (12, 13 + loop-2/3 argon) skipped or re-routed.
- zai usage exhausted — zai seats route to `openai-codex/gpt-6-luna-max` for the session.

## Loop-2 readiness

Schedule repeats positions 1–14 at rounds 47–60. Provider plan: pos 1–3 opencode-go
64-seat (round-robin keys 1-2 live, 3-7 402'd); pos 4 hyper->devin; pos 5/9 luna-max;
pos 6 grok (devin fallback); pos 7-8 + 11 zai→luna-max (amendment); pos 10 devin;
pos 12-13 antigravity (skip/re-route); pos 14 devin swe-2 audit.
