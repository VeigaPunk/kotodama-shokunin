# ExecBattery94 — round-94 counterfeit battery and grader driver (claim O, operability)

Stage: `.ufo/waves/round-94/w1/stage/ExecBattery94/` (driver, manifest, fixtures, red-before, SHA256SUMS).
Scratch `/fast/scratch/hyaku/kotodama-r94/ExecBattery94/` deleted before yield.

## Summary line (v4 base, sha256 9799a96c…, verified before the run)

`BATTERY-SUMMARY survivors=4 unnamed=3 refused=0`

Command: `python3 -B stage/ExecBattery94/battery94.py --tool <scratch>/v4-tool.py --work <scratch> --verbose` → rc 0 (`Wall time: 1.55 s`).
The same command with `--emit <stage>` reproduces the identical CLASS and REG lines (`cmp` rc 0, detail lines excluded).

## Red-before table (v4 base)

| class | rc | Traceback | named diagnostic | outcome | what v4 does |
|---|---|---|---|---|---|
| A1 | 0 | no | none | SURVIVOR | Cyrillic O (U+041E) in `LOCATED` of a gained S001 line; APPENDONLY sees no disposition; `ENTRY-EVIDENCE: PASS legs=9/9` |
| B1 | 0 | no | none | SURVIVOR | soft hyphen U+00AD in `LOCA­TED`; not in ZW_MAP; PASS 9/9 |
| G1 | 0 | no | none | SURVIVOR | `## 1. address` … `## 5. Rites`; list number counted as a token; TOPIC passes; PASS 9/9 |
| H1 | 1 | yes | none | UNNAMED | `AttributeError: 'list' object has no attribute 'get'` |
| I1 | 1 | yes | none | UNNAMED | `IndexError: list index out of range` (NEWIDS cells[10]) |
| J1 | 1 | no | `APPENDONLY` on the wrong verdict | UNNAMED | `LEG FAIL APPENDONLY … observed=S001: gained a LOCATED line not present at base` (en-dash read as LOCATED) |
| K1 | 0 | no | none | SURVIVOR | `- note: S001 located recheck moved …`: anchored regex needs line-start id, case-sensitive fallback needs uppercase verdict; PASS 9/9 |

Naming rule used by the driver (manifest field `leg_or_diagnostic_named_any_of`): REFUSED requires rc≠0, no `Traceback`, and one listed token in the output. Tokens for a correct v5 grader:

- A1, B1: `NON-ASCII-VERDICT` or `LEG FAIL APPENDONLY`
- G1: `LEG FAIL TOPIC`
- H1: `LEG FAIL GATE`, `LEG FAIL CAPTURE`, `MANIFEST-ROW-NOT-OBJECT`
- I1: `LEG FAIL NEWIDS`, `REGISTRY-ROW-CELLS`
- J1: `NON-ASCII-VERDICT` or `gained a NOT-LOCATED line`
- K1: `LEG FAIL APPENDONLY`

Disclosure on J1: v4 does print `LEG FAIL APPENDONLY`. I count it UNNAMED because the message reports the wrong verdict (LOCATED for a NOT–LOCATED line), which is the misfire the round-93 critic recorded. A literal leg-name-only reading would count J1 as REFUSED on v4. That is the only class where the choice of rule changes the outcome.

## Regression set against v4 (`REG` lines, same run)

- Round-93 battery grade set (battery93 ATTACKS, 26 cases, set B): G0 CLEAN; A5a CLEAN; A1 SURVIVOR; 22 refused on a named leg (C1c GATE; A2a UNIQUENESS; A2b CAPTURE,GATE; A2c–A2f UNIQUENESS; A3a/A3b CAPTURE; A4a/A4b TOPIC; A5b–A5f APPENDONLY; A6a/A6b BASEROWS; A6c–A6e CAPTURE; A6f GATE); A6g refused-unnamed rc=2 (manifest rows list, `ADVANCE-EVIDENCE_ERROR`, no leg).
- Round-92 V-series (mc.ATTACKS, 7 cases, set B) plus control G0: all seven refused on their named leg (V10a/V10c APPENDONLY, V3 UNIQUENESS, V12 CAPTURE, V7 GATE, V2 TOPIC, V9 CAPTURE); G0 rc 0.
- Note: battery93 `expect=SURVIVE` labels on A2c–A2f, A3b, A4a, A5d–A5f, A6a–A6f are the round-93 labels from before v3/v4; v4 refuses them. These are recorded as current outcomes. The L1 compares v5 against the `REG` lines of `red-before-v4.txt` (same command), not against the labels.

Name clash: the round-93 `A1_chrome_forged_manifest` case in battery93 is not the round-94 class A1 (Cyrillic verdict).

## Fixtures and manifest

- `battery/<class>/` (A1, B1, G1, H1, I1, J1, K1): full mini-lanes (base, lands, lesson, base-lesson, entry, manifest, captures). Each is the battery93 standard G0 lane with one counterfeit applied.
- Stage reproduction: each class fixture re-graded with the v4 tool from the stage copy gives A1 rc 0, B1 rc 0, G1 rc 0, H1 rc 1, I1 rc 1, J1 rc 1, K1 rc 0. Same as in scratch.
- `manifest.json`: schema `kotodama-round-94-battery-manifest-v1`; per class the counterfeit description, `leg_or_diagnostic_named_any_of`, `expected_exit: nonzero`, fixture path. Seven entries.
- Fixture file count: 63 (`find battery -type f`). Per-file sha256 in `SHA256SUMS.txt` (66 lines: 63 fixture files plus battery94.py, manifest.json, red-before-v4.txt).

## Files and sha256

| file | sha256 |
|---|---|
| `stage/ExecBattery94/battery94.py` (driver; copy of reports/round-93/battery93.py extended) | 9496721a1e8a401985d6be802184acb4c03f8718c97b82dd8ce909faafe1a7ea |
| `stage/ExecBattery94/manifest.json` | fe40ebc607242129db1739699581b9298652060a880286818fa243e71d782ef7 |
| `stage/ExecBattery94/red-before-v4.txt` | 9ea82066900c23949a488dbb348efad25cc5c30e7d2f5d618862050579a80f35 |
| `stage/ExecBattery94/SHA256SUMS.txt` | per-file sums for the 63 fixture files and the three above |
| `stage/ExecBattery94/battery/<class>/**` | see SHA256SUMS.txt |
| `.ufo/waves/round-94/w1/ExecBattery94.md` (this file) | not hashed (self) |
| `.ufo/waves/round-94/w1/stage/ExecBattery94/DONE` | sha256 of battery94.py |

Driver contract: `--tool <path>` and `--work <dir>` (refuses a work dir under /tmp); TMPDIR is `<work>/tmp`; builder `reports/round-92/controls/make-counterfeits.py` and battery93 source read only. Optional: `--emit <stage>`, `--verbose`. Exit 0 once the run completes; 2 on usage error. Lines: `TOOL sha256=…`, `CLASS …`, `BATTERY-SUMMARY …`, `REG …`.

## Not measured / out of scope

- No v5 tool exists in this seat, so the battery has no post-fix numbers. The predicate for O's BATTERY leg is the L1's job at integration.
- Mutants (script-strip-off, comment-strip-off, unescape-off, dispo-any-casei, baserows-drop-cell8) belong to ExecMutants94; not touched here.
- K1 is built from the routed description (`dispo-any-casei` channel). The claims file names only the class, not a recipe; the recipe above is mine and is what v4 survives.

## Tooling

None installed or upgraded. No pacman, no sysctl, no network access, no git mutation. Read-only `git show` used once to extract the v4 tool (sha verified 9799a96c…).
