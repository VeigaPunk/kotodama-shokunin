# ReviewerO97 — non-author review of claim-O landing (round 97, attempt 1)

Reviewer: ReviewerO97 (UFO-FSD reviewer role). Scope: claim O (operability, grader v8 -> v9) only; claim-C legs observed in the same counter run are corroboration, judgment belongs to ReviewerC97. I edited nothing in the lane except my stage dir. Dependency waited for: `.ufo/waves/round-97/w1/stage/ExecGraderV9/DONE` (bounded 60 s loops from 19:32; DONE appeared 21:39:50 containing the v9 sha).

## 1. Frozen counter run (step 1) — my canonical measurement

Command (rc=0, run 21:31-22:0x over the landed lane tree, work strictly in my scratch):

```
TMPDIR=$S python3 -B $L/reports/round-97/predispatch.py \
  --root $L --work $S/counter \
  --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569
```

Output saved at `stage/ReviewerO97/counter.txt` (sha256 28e2a99ec8a4f12b79af6648147f507155a9e4728561248d3b5d24773e5561ef):

```
LEG O0 PASS tool-sha256 1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b (must differ from v8 f29ab013…)
LEG O1 PASS 155/155 floor=154 rc=0
LEG O2 PASS survivors=0 unnamed=0 refused=31 required=0/0/31 traceback-free=True rc=0 pin=receipt=driver
LEG O3 PASS 121/121 killed, 0 survived, 0 broken-pattern (floor total 118) rc=0
LEG O4 PASS 34 baseline REG lines, 34 byte-identical in battery97 output
LEG C1..C8 PASS (entry 36739 B, 13 h2, 7x6 table, 6/6 phrases, topic equal; registry 917 rows highest S993, 8 qualifying; added=9 removed=0; census rc=0; index rc=0; 8/8 cited; 8/8 captured; 269 files scanned, 0 other owners)
PREDISPATCH-97: PASS legs=13/13   (rc=0)
```

Lane-bytes stability guard: `sha256sum` of `tools/check-advance-evidence.py` pre-run and post-run both `1021dc9d…` (unchanged during measurement); battery97.py `79efb67c…`, mutants97.py `f9c623fd…` recorded pre-run, both equal their pins. ExecGraderV9's independent counter run (its `stage/ExecGraderV9/counter.txt`, 21:39:18) matches leg-for-leg.

**Leg judgment (O0-O4): O0 PASS, O1 PASS, O2 PASS, O3 PASS, O4 PASS — first failing leg: none.**

## 2. Pin binding (step 2)

| artifact | recomputed sha256 | pin | receipt | equal? |
|---|---|---|---|---|
| battery97.py | 79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c | battery97.sha256 (same) | BATTERY-SHA256 in battery97-control-v8.txt (same) | YES |
| mutants97.py | f9c623fd384d276ad2b53ea10d67ac021a2fc77a3baca50df33d5e505bd22259 | mutants97.sha256 (same) | DRIVER-SHA256 in mutation97-first.txt (same) | YES |

Commands: `sha256sum <driver>`, `cut -d' ' -f1 <pin>`, `grep '^BATTERY-SHA256|^DRIVER-SHA256' <receipt>`; all rc=0.

mtime order (`stat -c '%y %n'`, rc=0): mutants97.py repair 19:48:00.539 -> mutants97.sha256 pin 20:03:57.334 -> mutation97-first.txt 20:04:05.910 (first receipt; completed in place 20:33:32) -> red-before-v8.txt 20:56:55 -> MutationTester97 DONE 20:59:21. The pin and the first receipt postdate the last driver repair and predate every later mutation run; the driver bytes never changed after the pin (sha equality above re-verified at 21:31 pre-run). Battery side: pin + control receipt written together 19:35:42, before any v9 measurement. Routed round-96 defect 2 (mutation sha not pinned at first measurement) is closed: pinned BEFORE first measurement.

Cross-check of the O2 receipt chain: battery97-control-v8.txt shows TOOL-SHA256 = v8 f29ab013…, survivors=7 unnamed=0 refused=24, with exactly CR1 US1 OGH1 IS1 NUL1 CM1 CMW2 as SURVIVOR and G0/ZWNJ1 CLEAN — matches the frozen CONTROL_SUMMARY=(7,0,24) the counter enforces.

## 3. Shadowed-branch equivalence check (step 3)

Diff v8 (git 1ffc5a83:tools/check-advance-evidence.py, sha f29ab013…, 1938 lines) vs lane v9 (1021dc9d…, 2016 lines): +85/−7. Exactly three new refusal branches, no other logic changes:

| branch | v9 location | mechanism | mutant (equivalence check) | observable outcome change | verdict |
|---|---|---|---|---|---|
| VERDICT-CTRL | v9:319-320, per-char loop in `_refuse_verdict_channel` | C0 controls (minus tab/VT/FF/ESC/FS-GS-RS/NEL skip-list) in verdict window -> `raise Refused(... U+XXXX (VERDICT-CTRL))` | `raise Refused(` -> no-op `_dead_ref(` on line 319 (helper inserted; genuine fall-through, no crash) | selftest 155/155 -> FAIL 152/155 rc=1 (pins CR1/US1/NUL1 fail); battery97 0/0/31 -> 3/0/28, CR1/US1/NUL1 REFUSED->SURVIVOR | NON-SHADOWED |
| VERDICT-SEPARATOR | v9:322-323, same loop | `unicodedata.category(c)=='Zs'` in verdict window -> `raise Refused(... U+XXXX (VERDICT-SEPARATOR))` | no-op on line 322 | selftest FAIL 153/155 (OGH1/IS1 pins); battery97 2/0/29, OGH1/IS1 REFUSED->SURVIVOR | NON-SHADOWED |
| HEADING-COMBINING | v9:738-741, TOPIC section of `grade_entry` | any Mn/Me category char in any `## ` heading -> TOPIC problem `HEADING-COMBINING` | lines 738-741 deleted | selftest FAIL 153/155 (CM1/CMW2 pins); battery97 2/0/29, CM1/CMW2 REFUSED->SURVIVOR | NON-SHADOWED |

No branch's removal left every observable outcome unchanged — no shadowed branch, no dead refusal. Harness: `stage`-external script `shadow_harness.py` in scratch (kept out of the lane); auto-diff branch discovery found the same 3 sites. Harness itself validated on controls first: v8-vs-v8 self-diff -> 0 branches; renamed-diagnostic positive control (VERDICT-NBSP->NBSPX) -> correctly flagged NON-SHADOWED (selftest pin drop + battery class flip). Methods routed from round 96 as claimed. Note: the first positive-control mutant used an undefined-helper path (NameError/traceback) before I fixed the harness; all three v9 branch mutants above ran with clean fall-through semantics (battery rc=0, traceback-free).

## 4. No v8 refusal weakened (step 4)

`python3 -B .ufo/waves/round-96/w1/stage/ExecBattery96/battery96.py --tool <lane v9> --work $S/b96v9` -> rc=0, `BATTERY-SUMMARY survivors=0 unnamed=0 refused=24 traceback=0 clean=2 not-clean=0` (expect survivors=0 refused=24 — exact). Byte-diff of battery96 output over v8 vs over v9: only line 1 (TOOL sha256) differs; all 26 CLASS lines (rc, traceback, named diagnostic, outcome) identical — every battery96 class refused with the same named diagnostic over v9.

## 5. Cosmetic fix behaviour-neutral (step 5)

The v8->v9 diff contains three "Round-96 v7" -> "Round-96 v8" renames (module docstring, `_refuse_verdict_channel` docstring, comment above `_NUM2`), two new docstring paragraphs, one new comment block, and removal of a blank line after `def _refuse_disguised(n, stripped):` (docstring remains the first statement). All are comments/docstrings/whitespace — no code tokens. Behavioural identity confirmed by section 4 (24 refusals byte-identical, same names) and by the 147 v8-era selftest checks still passing inside v9's 155/155 (147 + 8 new round-97 pins).

## Verdict

**Claim O: PASS.** Counter legs O0-O4 all PASS on one run of the frozen counter bytes over the landed tree (13/13 overall, rc=0); pins, receipts, mtime order, branch non-shadowing, battery96-over-v9, and cosmetic neutrality all verified. First failing leg: none.

## Residual risk and verification gaps

- My battery97-over-v8 repro at 19:34 ran pre-final driver bytes (ce59c34b…); the binding control receipt (battery97-control-v8.txt, 19:35:42) was produced with the final pinned bytes 79efb67c…, and all my later battery97 runs (base + 3 mutants, sections 3) used the pinned bytes. No claim rests on the early repro alone; the frozen counter also re-checks the receipt chain.
- Claim-C legs C1-C8 passed inside my run, but I did not audit sourcing quality, capture authenticity, or the entry's content (ReviewerC97's seat; C7 checked capture existence, not provenance).
- The mutation score (121/121) is one measurement; mutants are pattern-targeted (broken-pattern on v8 = 10 for the new ones, per red-before-v8.txt), so a semantically-dead mutant that still matches would count as killed without discriminating. Mitigated by the independent equivalence check in section 3, which tests the same refusal branches end-to-end.
- mtime evidence is filesystem-order only; content binding is the sha triple-equality, which is the stronger guarantee and holds.

## Tooling, sources, environment

- Tools installed/upgraded: none. pacman: not used. Host sysctls: not touched. Disk guard: `bash scripts/hyaku/disk-guard.sh status` rc=0 (403.8G free on /fast/scratch at 19:31).
- Sources opened: none (claim O is repo-internal; no web evidence needed).
- Scratch deleted before yield (trap/finally equivalent: explicit `rm -rf` after artifact copy). Nothing written outside `stage/ReviewerO97/` (counter.txt, review.md, DONE) and my scratch.
