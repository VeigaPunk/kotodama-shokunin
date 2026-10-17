# R10-F16 — stale fix: `SKILL.md` checklist block (header claim + calibration vocabulary)

- seat: freshness stale-fixer (R10-F16..F19). **This file is the seat's only
  write**, plus the in-place `SKILL.md` corrections it records (sanctioned by
  the assignment: "fix in place with cited evidence"). No filed report byte was
  rewritten; no commit made.
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749`
- live HEAD at work: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (+ worktree edits)
- `SKILL.md` sha256 before this seat's edits: `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`
  (same as `git show 9dc18ec:SKILL.md`, so the corrections below are the first
  edits to the file this round)

## Items taken from the ledger

Two ledger rows cover one six-line block (`SKILL.md:115-121`):

| ledger row (0-based) | locator | shard | verdict in ledger |
|---|---|---|---|
| 35 | `SKILL.md:119-121` | shard-07 | `stale-documented` (reason: 0 matches for "mainstream") |
| — (shard-06 §06-G, not in the ledger as a row) | `SKILL.md:115` header | shard-06 | `stale-documented` + proposed patch |

- `reports/round-10/drift/shard-06.md` §06-G/§06-H and
  `reports/round-10/drift/shard-07.md` DR-07-01 handed both forward with patch
  text ("owner F15-F18").

## Evidence

- `grep -c -i mainstream corpus/knowledge/synthesis/source-discipline-calibration.md`
  → `0`, exit 1 (2026-10-17, lane root). The cited file's own status set is
  declared at `source-discipline-calibration.md:67` — **S / C / H / R / U / V** —
  and `:94-95` explicitly warns that "contested", "not established" and
  "discredited" are not synonyms.
- `corpus/knowledge/synthesis/source-discipline-calibration.md` sha256
  `3cbc98b4266aea08d2e8b19513ee369b3f0c6727f16f3c40eafe44796f0e4e93` (197 lines),
  so the mismatch is in the `SKILL.md` sentence, not in a moved citation target.
- shard-06 §06-G's sweep found no lane executable that reads a culture packet's
  typological-basis claim (item 1), while item 2's declared-shape check does
  exist as `provenance-audit`'s `missing-calibration` finding family
  (`tools/gates/provenance-audit.py`; registry §2 finding vocabulary
  `missing-calibration`).

## Disposition: `stale-fixed`

Replaced the header's blanket "executable" claim and the three-value
parenthetical with the cited file's own vocabulary and an explicit note of
which item is prose-only.

`SKILL.md:115-121` — before:

```
## Checklist (executable)

- [ ] Every language system cites its typological basis (which real
      language family it draws on and why).
- [ ] Every mythic/symbolic claim names its framework and its calibration
      status (mainstream / contested / discredited — see
      synthesis/source-discipline-calibration.md).
```

after:

```
## Checklist (executable where a tool exists)

- [ ] Every language system cites its typological basis (which real
      language family it draws on and why). No lane executable reads this
      item — prose gap, recorded in `reports/round-10/drift/shard-06.md` §06-G.
- [ ] Every mythic/symbolic claim names its framework and its calibration
      status (per-claim set S/C/H/R/U/V — see
      synthesis/source-discipline-calibration.md:67; `provenance-audit`'s
      `missing-calibration` family checks the declared shape only).
```

## Control (re-runnable)

- `grep -n "mainstream / contested / discredited" SKILL.md` → no output,
  exit 1 (the stale phrase is gone).
- `sed -n '115,122p' SKILL.md` → the corrected block above.
- `grep -c -i mainstream corpus/knowledge/synthesis/source-discipline-calibration.md`
  → `0`, exit 1 (the target file is unchanged by this fix — the sentence now
  matches it instead of contradicting it).
- `SKILL.md` sha256 after the seat's edits: `52d5f4d1be6ac97a143323306eafa9c9649484f25de60de8a3ee7630d8c6792c`
  (one file, five items: this fix, fix-17, fix-18, fix-19 and fix-21's battery-row
  correction; the digest moved from `42e227ea…` to `52d5f4d1…` when the battery
  row landed).

## Limits

- The corrected sentence states only what the cited file declares; it makes no
  claim about whether any corpus entry's calibration status is correct.
- `reports/supplement-opencode-1/…` and other filed reports that used the
  three-value gloss were **not** rewritten — filed report bytes stay frozen.

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F16-01", "command": "grep -c -i mainstream corpus/knowledge/synthesis/source-discipline-calibration.md", "source_locator": "SKILL.md:119-121", "round10_verdict": "stale-fixed", "output_sha256": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa", "exit": 1, "fix_evidence": "reports/round-10/drift/fix-16.md", "note": "sentence re-pointed to the cited file's own S/C/H/R/U/V set (:67); header re-scoped to 'executable where a tool exists'; control: grep for the old phrase returns no match"}]
```
