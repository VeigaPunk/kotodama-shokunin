# R23-D04 — round-23 fragment ledger (read-time census of `reports/round-23/**`)

- round: 23 (operator: loop 2, GLM round 1 of 2; 16 workers, zai glm-5.3-flash MAX;
  `reports/round-23/claims.json`, `reports/round-23/targets.json`).
- seat **R23-D04** (fragment ledger). Census `2026-10-18T15:21:54Z`.
- baseline revision `0e81d9d99514631d6717e1ff354d5a5a759aa980` (round-22 close); declare revision
  `7b181a52eb74319e5e5c40cdb1f0a1a1dc652079`.
- canon: **NON-CANON integration ledger.** It admits nothing, certifies no round, and
  edits no byte outside `reports/round-23/integration/`.

## Declared seat plan

| seat group | workers | assignment |
|---|---:|---|
| O-successor-pins | 8 | combined-source successor pins for the final projector/adapter sources (D2 live + frozen pins, v2, D4 profile rows), new rows with before/after digests |
| O-wording | 4 | PLACEHOLDER_RE wording false positive ('unchanged-foreign-path control' in D4-CL08) dispositioned without weakening any placeholder rule |
| D-rule | 4 | family-clean projection rule drafted for SKILL.md from reports/round-22/bleed/design.md; orchestrator lands it |

## Census

23 files at `2026-10-18T15:21:54Z` (`__pycache__/`, `*.pyc`, `*.log` excluded; 1 unassigned).

| path | bytes | sha256 (12) | mtime UTC | owner seat |
|---|---:|---|---|---|
| `reports/round-23/adjacency.md` | 10634 | `c120de1223bc` | 15:15:59 | adjacency scribe |
| `reports/round-23/audit/x05-pins-spotcheck.md` | 7076 | `a77652b86960` | 15:11:15 | auditors |
| `reports/round-23/audit/x09-lessons-audit.md` | 12614 | `0b9d4859740f` | 15:13:50 | auditors |
| `reports/round-23/audit/x09-lessons-audit.py` | 9515 | `ecdfa3455b76` | 15:10:51 | auditors |
| `reports/round-23/audit/x09-lessons-receipt.json` | 16318 | `e7ce1d1223f2` | 15:11:17 | auditors |
| `reports/round-23/audit/x12-retro-spotcheck.md` | 12411 | `c19ea46ae613` | 15:17:00 | auditors |
| `reports/round-23/claims.json` | 1986 | `a8e2b7a6bc6a` | 15:00:40 | declaration (parent) |
| `reports/round-23/fragment-index-x08.md` | 13587 | `9285e2c00172` | 15:20:47 | X scribes (report/index) |
| `reports/round-23/integration/fragment-ledger.json` | 5769 | `784f3db86dd7` | 15:20:42 | integration (R23-D04 fragment ledger) |
| `reports/round-23/integration/fragment-ledger.md` | 4571 | `ea3b1fa39407` | 15:20:42 | integration (R23-D04 fragment ledger) |
| `reports/round-23/integration/ledger-gen.py` | 10817 | `c087c0b70734` | 15:20:50 | integration (R23-D04 fragment ledger) |
| `reports/round-23/integration/log-draft.md` | 5022 | `cb8b3f09b74e` | 15:17:48 | integration (R23-D04 fragment ledger) |
| `reports/round-23/integration/scorecard-draft.md` | 3274 | `e255b6be6aea` | 15:18:03 | integration (R23-D04 fragment ledger) |
| `reports/round-23/rule/fragment-D01.md` | 4582 | `732b554f28ba` | 15:14:44 | D-rule |
| `reports/round-23/rule/fragment-D02.md` | 5118 | `1734e3570c84` | 15:14:44 | D-rule |
| `reports/round-23/rule/fragment-D03.md` | 4360 | `659ff387c63c` | 15:14:44 | D-rule |
| `reports/round-23/rule/skill-draft.md` | 19897 | `044655b8bc0c` | 15:14:44 | D-rule |
| `reports/round-23/scope.md` | 10166 | `fcf59e146f4a` | 15:09:11 | scope auditor |
| `reports/round-23/shonen-survey.md` | 8704 | `d07fb10eda0a` | 15:16:26 | unassigned |
| `reports/round-23/targets.json` | 180 | `817813aeaca6` | 15:00:40 | declaration (parent) |
| `reports/round-23/wording/declared-in-r3/expected.json` | 1330 | `737e54842fff` | 15:21:18 | O-wording |
| `reports/round-23/wording/declared-in-r3/packet.md` | 107119 | `084dc5db9a8d` | 15:19:02 | O-wording |
| `reports/round-23/wording/wording-check.py` | 16593 | `37756c30e9f3` | 15:21:18 | O-wording |

## Reading

- The census is point-in-time; the wave was still writing when it was taken.
  A file arriving after it needs a dated refresh, not an inferred worker failure.
- Owner-seat is inferred from the path shape (prefix and name rules; the
  round-23 targets declare seat counts, not paths); `unassigned` is never
  guessed and any `unassigned` row is a parent reconciliation item.
- The two ledger files are themselves censused: their rows record the
  pre-write version (self-reference); re-run the generator to refresh.
- The counting command for both round-23 claims is
  `python3 reports/round-23/run-validation.py` (declared in
  `reports/round-23/claims.json`); until that runner and its receipt land,
  no claim outcome is certified by this ledger.
- This ledger is the index the parent uses to integrate fragments into
  `LOG.md` / `SCORECARD.md` (drafts: `reports/round-23/integration/log-draft.md`,
  `reports/round-23/integration/scorecard-draft.md`); it is not a verdict and
  not a completeness claim.
