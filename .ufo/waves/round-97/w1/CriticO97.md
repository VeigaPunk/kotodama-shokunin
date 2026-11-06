# CriticO97 — round 97 attack seat on grader v9 (operability)

Final tally (attack driver stdout, rc 0): **CRITIC-O97 survivors=8 unnamed=0 refused=17 traceback=0** (v9).
Do-nothing baseline v8 over the identical 28 fixtures: **CRITIC-O97 survivors=19 unnamed=0 refused=6 traceback=0** (rc 0).
CriticO96 replay on v9: **CRITIC-O96 survivors=0 unnamed=0 refused=19 traceback=0** (rc 0). CriticO96 measured survivors=7 on v8.

battery97.py remains the frozen predicate. No grader, driver, pin, or control receipt was edited. Attacks were read-only.

## Dependency deviation (flagged)

`stage/ExecGraderV9/DONE` did not appear in the bounded wait (90 polls x 60 s, service-managed). `stage/ExecGraderV9/V9-READY` did exist and records sha256 `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b`; this equals the current bytes of `tools/check-advance-evidence.py`. I ran the attacks against those bytes through a read-only copy, sha re-checked before and after (unchanged). If the orchestrator considers DONE mandatory, re-run `stage/CriticO97/attacks_critic97.py` after ExecGraderV9 lands; the commands are in attacks.md.

## Attack table

Full per-class table (byte recipe, rc, outcome, named diagnostic, v9 and v8) is in `stage/CriticO97/attacks.md`. Summary:

| class | channel | v9 | v8 |
|---|---|---|---|
| BEL1, SUB1 (Cc) | verdict | REFUSED VERDICT-CTRL | SURVIVOR |
| DEL1 (Cc U+007F) | verdict | **SURVIVOR** | SURVIVOR |
| ENQ1, ENSP1, FIGSP1, THINSP1, HAIRSP1, NNBP1, MMSP1 (Zs) | verdict | REFUSED VERDICT-SEPARATOR | SURVIVOR |
| ENC1 (Me U+20DD) | verdict | **SURVIVOR** | SURVIVOR |
| VS16VT (Mn U+FE0F), CMID1 (id combining) | verdict/id | REFUSED VERDICT-COMBINE | REFUSED VERDICT-COMBINE |
| FEFFVT1 (ZW in token), BOM1 (U+FEFF line start) | verdict/line | REFUSED APPENDONLY | REFUSED APPENDONLY |
| ENCH1 (Me), VSH1 (Mn) heading numbers | heading | REFUSED HEADING-COMBINING, TOPIC | SURVIVOR |
| ROMAN1 (U+2160-64), SUP1 (superscripts) | heading numbers | **SURVIVOR** | SURVIVOR |
| FWPER1 (U+FF0E after digit) | heading number | **SURVIVOR** | SURVIVOR |
| FWNUMH1 (fullwidth digits) | heading number | REFUSED TOPIC | REFUSED TOPIC |
| CYRH1, ZWSH1, BELH1 (junk + clean twin) | heading word | SURVIVOR (benign, see below) | SURVIVOR (benign) |
| NELH1 (NEL in heading word) | heading word | REFUSED TOPIC | REFUSED TOPIC |
| G0, H-CRLF, H-CR | controls | CLEAN x3 | CLEAN x3 |

No TRACEBACK. No REFUSED-UNNAMED on either version.

## Controls and positive checks (rc recorded)

- v9 plain gained `LOCATED` line: rc 1, `FAIL legs=8/9 failed=APPENDONLY` (refusal intact). Same line with U+007F or U+20DD: rc 0, `PASS legs=9/9`.
- v9 ASCII phrase-only heads `1.`..`5.`: rc 1, `FAIL legs=8/9 failed=TOPIC`. With `Ⅰ.`..`Ⅴ.` or `1．`: rc 0, PASS 9/9.
- Battery97 CONTROL over v8 (receipt `reports/round-97/controls/battery97-control-v8.txt`): `BATTERY-SUMMARY survivors=7 unnamed=0 refused=24` (as predicted in the lane's claims). Read, not re-run.
- Fresh codepoints confirmed absent from battery97.py before the run (grep -c, rc 0 each): U+0007, U+007F, U+001A, U+2000, U+2002, U+2007, U+2009, U+200A, U+202F, U+205F, U+20DD, U+FE0F, U+FF0E, U+2160, U+00B9, U+2074, U+FF11 all 0. U+0430 appears only in CYR1 (id letter), U+200B only in a comment.

## The three most dangerous v9 survivors (routed to round 98; NOT implemented)

1. **ENC1** — a gained LOCATED with U+20DD (category Me) passes APPENDONLY unnamed. Fix (one line): refuse any verdict-span byte with `unicodedata.category(c)[0] == 'M'` as `VERDICT-COMBINE` (Mn/Mc/Me). Cause is an inference from the code path (VERDICT-COMBINE tests Mn only); not traced.
2. **ROMAN1 / SUP1 / FWPER1** — non-ASCII numbering tokens count as heading content (ASCII-only `_NUM2`), so phrase-only heads reach the span floor and the span-gaming class reopens. Fix (one line): in `_content_toks`, keep only tokens with `any(c.isalpha() for c in t)`. Heading positive control confirms the ASCII form is refused on TOPIC.
3. **DEL1** — U+007F DELETE passes APPENDONLY unnamed while BEL1/SUB1/NUL1/CR1/US1 are named VERDICT-CTRL. Fix (one line): add U+007F to the verdict-window control set, or refuse any Cc byte in the span. The set itself was not printed; the placement is an inference from the named/unnamed split.

Not dangerous: CYRH1, ZWSH1, BELH1 survive, but each heading also carries a clean copy of the phrase, so they gain no anchor. This is a fixture-design flaw on my side (admitted in attacks.md); they are not forgeries.

## CriticO96 replay on v9 (rc 0)

`CRIT_WORK=<scratch>/replay96 CRIT_BATTERY=battery97.py CRIT_TOOL=v9 python3 -B .ufo/waves/round-96/w1/stage/CriticO96/attacks_critic96.py` → `CRITIC-O96 survivors=0 unnamed=0 refused=19 traceback=0`. CR1 (VERDICT-CTRL), US1 (VERDICT-CTRL), OGH1 (VERDICT-SEPARATOR), IS1 (VERDICT-SEPARATOR), NUL1 (VERDICT-CTRL), CM1 and CMW2 (HEADING-COMBINING + TOPIC) are now named.

## Hashes (sha256sum, rc 0)

- v8 export (`git show 1ffc5a83…:tools/check-advance-evidence.py`): f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0
- v9 (`tools/check-advance-evidence.py` at run time, equal to ExecGraderV9 V9-READY): 1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b
- battery97.py (frozen; equals control pin `reports/round-97/controls/battery97.sha256`): 79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c
- mutants97.py (pin `reports/round-97/controls/mutants97.sha256`): f9c623fd384d276ad2b53ea10d67ac021a2fc77a3baca50df33d5e505bd22259 (not run by this seat)
- Driver `stage/CriticO97/attacks_critic97.py`: 48d8e0f69ac2b482571efa2d0cf48877098f3f61db2e22646d05089ce28ee1e4
- Main output `stage/CriticO97/attacks.md`: 436b3d34d31f872624ba1ac2472ddb012191be0914bea12efd5eebc6917669c8

## Tooling

Installed or upgraded tools: **none**. No pacman, sysctl, git/jj mutation, or write to PATH directories. Read-only `git show`, `grep`, `sha256sum`, `cp` into scratch.

## Writes

- `stage/CriticO97/attacks_critic97.py` (driver), `stage/CriticO97/attacks.md`, `stage/CriticO97/DONE` (last), this Report.
- Scratch `/fast/scratch/hyaku/kotodama-r97/CriticO97` removed before yield.

## Limits

- Fixtures are one-class-per-lesson-or-heading-set; combinations (e.g., ENC1 + a second forged line) were not built.
- Positive control for the ENC1/DEL1 gained lines is the verdict-channel APPENDONLY leg; the 9/9 pass means no leg in v9 caught these, not that they are rendered as LOCATED by any specific viewer.
- The round-98 fixes are proposals from code reading plus the controls above; none was implemented or tested on a patched copy (by rule).
