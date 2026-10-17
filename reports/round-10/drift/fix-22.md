# R10-F22 — stale items: the round-scoped acceptance runners are red on the delivered tree

- seat: freshness stale-fixer (R10-F16..F19). This file is the seat's write; it
  documents dispositions and records no edit to the runners themselves (one of
  them, round 8's, was repaired under `fix-20.md`).
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1…`
- live HEAD at work: `e3a1ec9` (+ worktree edits)

## Items taken from the ledger

| ledger row (0-based) | command | locator | verdict in ledger |
|---|---|---|---|
| 96 | `python3 reports/round-5/run-validation.py` | `SKILL.md:210`; `SCORECARD.md:30,32,33,34,35` | `stale-documented` (no reason text — validator flags it) |
| 104 | same | `SCORECARD.md:30,32-35` | `stale-documented` (F15: fresh clone, identical at `a7bb205`) |
| 113 | `python3 reports/round-6/run-validation.py` | `SCORECARD.md:65-70` | `stale-documented` (F15: `append-only prefix lost: SKILL.md`) |
| 114 | `python3 reports/round-7/run-validation.py` | `SCORECARD.md:92-93` | `stale-documented` (F15: F false, O true) |
| 115 | `python3 reports/round-8/run-validation.py` | `SCORECARD.md:104` | `stale-documented` → **now `stale-fixed`** (`fix-20.md`) |
| 117 | `python3 reports/round-9/run-validation.py` | `SCORECARD.md:133` | `stale-documented` (no reason text — validator flags it) |

## Evidence (this seat, 2026-10-17, isolated mirror at HEAD)

| runner | measured exit | committed receipt at HEAD | cause of the red reading |
|---|---|---|---|
| round-5 | 1 | `acceptance_checks_passed: true` | F: "non-append corpus edit (`corpus/lessons/supplement-opencode-1/sources/ottoman.json`, OTT-06)" — round-8's metadata frontmatter repair; O: battery default exit 2 (`fix-21.md`) |
| round-6 | 1 | `true` | "append-only prefix lost: SKILL.md" — rounds 8-10 legitimately extended `SKILL.md` in place (label-typing table, round-5/6 tables, this round's drift corrections) |
| round-7 | 1 | `false` | filed red (round 7 closed `failed`); re-run adds the same prefix loss + historical inventory totals changed (179 files / 610 raw lines) |
| round-8 | 1 → **0 after `fix-20.md`** | `true` (pre-`e1694ba` commit) | D leg: isolated replay restored gates from HEAD; patched to resolve pins by digest |
| round-9 | 0 | `true` | none — green, and shard-14 §3.2 independently reproduced it |

F15's fresh-clone runs (`R10-F15-battery` rows 104/113/114/115) show the same
failures at revision `a7bb205`, i.e. they are **pre-existing**, not round-10
regressions.

## Dispositions

- **`stale-documented` (round-5, round-6, round-7 runners) — reason**: these are
  round-scoped acceptance runners. Their preservation checks pin their own
  round's delivered tree (append-only `SKILL.md` prefix, historical inventory
  totals, unmodified corpus prefixes). Later rounds legitimately edited those
  surfaces in place, so the runners read red on the delivered tree while their
  filed receipts remain accurate for their own revisions. Weakening or
  re-pinning those checks to make them green would convert an honest historical
  invariant into a silent pass — explicitly rejected. The round receipts'
  own text already binds them to their revisions.
- **`stale-fixed` (round-8 runner)** — see `fix-20.md`; the repair restores the
  pinned revisions rather than relaxing the check.
- **`stale-documented` (round-9 runner, ledger row 117 without reason)** —
  measured **exit 0**, `claim F/O/D: PASS`, `acceptance_checks_passed: true`
  (shard-14 §3.2 reproduced the same). The registry §3 quote of
  `58e8fa4f…`/13 failures is superseded by the landed fix
  (`8e4881309afaacc96f8f6e68f0c31041a9b2accc1c26bb1b20403f563364f5dd`). Ledger
  row 117's `stale-documented` verdict is therefore wrong as filed: it should
  read `current`.

## Control (re-runnable)

- `for n in 5 6 7 8 9; do python3 reports/round-$n/run-validation.py; echo "$n:$?"; done`
  in an isolated mirror → `5:1 6:1 7:1 8:0 9:0` with the patched round-8 runner.
- `git show HEAD:reports/round-$n/validation.json | python3 -c "import json,sys; print(json.load(sys.stdin)['acceptance_checks_passed'])"`
  → `True True False True True` for n=5..9 (the filed states).

## Limits

- Red re-runs do not retroactively invalidate the rounds' own acceptance; they
  measure a later tree. Conversely, the filed green receipts for rounds 5/6 are
  not reproducible on today's tree — that asymmetry is now documented rather
  than hidden.
- No runner check was deleted, weakened or re-pinned by this seat.

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F22-01", "command": "python3 reports/round-5/run-validation.py", "source_locator": "SCORECARD.md:30,32-35", "round10_verdict": "stale-documented", "output_sha256": "2e7d8c0ff2faabafa72e3e132526b0cef6e059b263206ba0b048b9dd91c2fd0a", "exit": 1, "reason": "round-scoped acceptance runner; F reads round-8's corpus frontmatter repair as a non-append edit, O depends on the battery default (fix-21); filed receipt true at its own revision; identical failure at a7bb205 (F15) - documented, checks not weakened", "fix_evidence": "reports/round-10/drift/fix-22.md"},
 {"id": "R10-F22-02", "command": "python3 reports/round-6/run-validation.py", "source_locator": "SCORECARD.md:65-70", "round10_verdict": "stale-documented", "output_sha256": "79440ea7395873dd2cf9e7cde55dc9217ddd61c994579728fd667ab243ca9b9d", "exit": 1, "reason": "round-scoped; 'append-only prefix lost: SKILL.md' because rounds 8-10 legitimately extended SKILL.md in place; filed receipt true at its own revision; identical failure at a7bb205 (F15)", "fix_evidence": "reports/round-10/drift/fix-22.md"},
 {"id": "R10-F22-03", "command": "python3 reports/round-7/run-validation.py", "source_locator": "SCORECARD.md:92-93", "round10_verdict": "stale-documented", "output_sha256": "3ffc98f636827ba13a9743dbabc19e0977c0722887847879bd8c71789bc790ea", "exit": 1, "reason": "filed red (round 7 closed failed); re-run red for the same prefix/totals reasons; round-scoped and consistent with the filed state", "fix_evidence": "reports/round-10/drift/fix-22.md"},
 {"id": "R10-F22-04", "command": "python3 reports/round-9/run-validation.py", "source_locator": "SCORECARD.md:133", "round10_verdict": "current", "output_sha256": "4d300b24a04ff44afdb89c6944174ad8f71056667fd0e5f2044266010943b2f5", "exit": 0, "note": "ledger row 117's stale-documented verdict is wrong as filed: measured exit 0 with F/O/D PASS; runner digest 8e4881309afaacc9 supersedes the registry's 58e8fa4f quote", "fix_evidence": "reports/round-10/drift/fix-22.md"}]
```
