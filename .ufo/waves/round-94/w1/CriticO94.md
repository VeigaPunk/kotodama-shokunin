# CriticO94 — operability attack on grader v5 candidate

Summary: **SURVIVORS 7; UNNAMED 0; REFUSED-NAMED 6** (13 new counterfeit classes plus one G0 control; 14 fixtures).

Candidate tested in place (not copied into the lane):
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py`, sha256 `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`.

Driver: `.ufo/waves/round-94/w1/stage/CriticO94/attacks_critic.py`. It imports the wave battery driver `ExecBattery94/battery94.py` (sha256 `9496721a…`) read-only for `configure()` and `grade()`, so the argument shape is the battery's own. Every fixture is built under scratch.

Command (rc 0; the driver completed, the counts are data):
```
CRIT_REPO=/home/vgpnk/Projects/shokunin/kotodama-shokunin CRIT_WORK=/fast/scratch/hyaku/kotodama-r94/CriticO94 \
CRIT_BATTERY=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecBattery94/battery94.py \
CRIT_TOOL=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py \
CRIT_OUT=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/CriticO94/attacks.md \
python3 -B .ufo/waves/round-94/w1/stage/CriticO94/attacks_critic.py
```

## Per-class results (candidate v5)

| id | new class | rc | outcome | Traceback | named leg or diagnostic |
|---|---|---|---|---|---|
| FW1 | fullwidth Latin verdict `ＬＯＣＡＴＥＤ` | 2 | REFUSED-NAMED | no | `line 4: verdict token carries non-ASCII letters (VERDICT-NONASCII)` |
| MA1 | mathematical bold verdict | 2 | REFUSED-NAMED | no | `VERDICT-NONASCII` (same) |
| CD1 | combining acute U+0301 inside `LOCATED` | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| LR1 | LRM U+200E inside `LOCATED` | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| TAB1 | tab inside `LOCATED` | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| ID1 | small-cap S U+A731 in the id token | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| ZWJ1 | ZWJ U+200D (in the strip set; control) | 1 | REFUSED-NAMED | no | `LEG FAIL APPENDONLY … S001: gained a LOCATED line not present at base` |
| CRLF1 | CRLF lesson endings, gained line | 1 | REFUSED-NAMED | no | `LEG FAIL APPENDONLY … S001: gained a LOCATED line` |
| NUM1 | nested numbered phrase heads `## 1.1 address` … | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| RM1 | roman-numbered phrase heads `## I. address` … | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| NUM2 | second-token numbered heads `## Notes 1) address` … | 0 | **SURVIVOR** | no | none; 9/9 PASS |
| SP1 | eleven-cell lands row, id cell indented 4 spaces | 1 | REFUSED-NAMED | no | `LEG FAIL NEWIDS … cited ids missing from registry: S958` |
| MN1 | manifest row value is a dict missing `url` | 1 | REFUSED-NAMED | no | `LEG FAIL CAPTURE … S955: manifest url is not a row url:` |

Traceback check: `grep -c Traceback stage/CriticO94/attacks.md` → 0. UNNAMED is 0 for every class.

Counting: the 13 counterfeits split 7 survivors plus 6 refusals (FW1, MA1, ZWJ1, CRLF1, SP1, MN1). The G0 control reports `CONTROL-CLEAN` (rc 0, `ENTRY-EVIDENCE: PASS legs=9/9`).

## Survivor recipes (minimal bytes)

Each recipe is the one added forged element on top of the G0 fixture. I did not reduce them further, so "minimal" means "as built", not proven minimal.

- **CD1**: lesson line `S001 LOCA\u0301TED recheck 90d accessed 2026-11-05` (combining acute after A). Reads as a LOCATED gain to a human; the tool sees no verdict token.
- **LR1**: lesson line `S001 LO\u200eCATED recheck 90d accessed 2026-11-05` (LRM U+200E). U+200E is not in the tool's ZW_MAP, which strips only U+200B, 200C, 200D, 2060 and FEFF.
- **TAB1**: lesson line `S001 LO<TAB>CATED recheck 90d accessed 2026-11-05`.
- **ID1**: lesson line `\ua731001 LOCATED recheck 90d accessed 2026-11-05` (U+A731 in place of S; DISPO_RE requires ASCII `S`).
- **NUM1**: entry h2 lines `## 1.1 address`, `## 2.1 petition`, `## 3.1 efficacy`, `## 4.1 table`, `## 5. Notes`; all other G0 bytes. The TOPIC span passes.
- **RM1**: entry h2 lines `## I. address`, `## II. petition`, `## III. efficacy`, `## IV. table`, `## V. Notes`; all other G0 bytes.
- **NUM2**: entry h2 lines `## Notes 1) address`, `## Notes 2) petition`, `## Notes 3) efficacy`, `## Notes 4) table`, `## Notes 5) Table`; all other G0 bytes. The leading-number strip does not reach the second token.

## Do-nothing control (v4 base, sha 9799a96c…)

Same 14 fixtures against the v4 base (`git show e7fa8eaf…:tools/check-advance-evidence.py`, scratch copy). Result: `SURVIVORS 9; UNNAMED 0; REFUSED-NAMED 4`. The nine v4 survivors are FW1, MA1, CD1, LR1, TAB1, ID1, NUM1, RM1 and NUM2. v5 closes exactly two of them (FW1 and MA1, via VERDICT-NONASCII). The other eleven counterfeits (CD1, LR1, TAB1, ID1, ZWJ1, CRLF1, NUM1, RM1, NUM2, SP1, MN1) give identical outcomes on v4 and v5.

## Findings for the router

1. v5 is not operability-complete beyond the frozen battery. Seven new classes survive with rc 0 and 9/9 legs: three verdict-token channels (combining mark, LRM, tab) and one id-token channel (U+A731), plus three heading-gaming variants (nested-number, roman, second-token number). Any gained disposition using CD1, LR1, TAB1 or ID1 is invisible to APPENDONLY, which is the freshness-gaining channel the round exists to block.
2. The v5 fix for the verdict channel is a non-ASCII refusal on the verdict token (VERDICT-NONASCII, rc 2). It does not cover combining marks (Mn), format characters outside the strip set (Cf such as LRM), tabs or whitespace inside the verdict, or non-ASCII id letters.
3. The heading fix strips leading `\d+[.)]` only. Roman numerals and a numbered second token pass the floor.
4. Named refusals (SP1 via NEWIDS, MN1 via CAPTURE) carry a named leg, but the MN1 diagnostic is empty after the colon (`manifest url is not a row url: `). It is named but uninformative.

## Tooling and writes

- Installed or upgraded: none. Tooling record: none.
- No pacman, sysctl, git mutations or lane-file writes. The v4 base copy lived in scratch only.
- Stage writes: `stage/CriticO94/attacks_critic.py`, `stage/CriticO94/attacks.md`, `stage/CriticO94/DONE`, this report.
- Scratch `/fast/scratch/hyaku/kotodama-r94/CriticO94` deleted before yield.
