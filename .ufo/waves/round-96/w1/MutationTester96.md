# MutationTester96 — mutation attack on grader v7 (round 96, attempt 1)

Verdict: v7 does NOT pass its own mutation predicate. `mutants96.py` against the v7 lane file scores
**109/112 killed, 3 survived, 0 broken-pattern**, rc 1. Frozen leg O3 requires `killed == total`
and `0 survived`, so O3 fails as measured. Per the kill rule this is recorded as measured; the grader
was not repaired. Survivors are named in section 3.

## 0. Dependency and inputs

- Dependency: `stage/ExecGraderV7/DONE` present on the first bounded check (wait loop, 1 minute). DONE content
  `2e28a289746812b14a07a0645e568f0cee9dfb1789af6cfe6ce88f80c8f053ec`.
- v7 bytes: lane file `tools/check-advance-evidence.py`, sha256 `2e28a289746812b14a07a0645e568f0cee9dfb1789af6cfe6ce88f80c8f053ec`
  (matches `ExecGraderV7/v7-sha.txt` and `DONE`). Copy in scratch (same sha) used for diffs and probes.
- v6 bytes: exported with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 0539276c0e329743200b60e98bf289c540f78864:tools/check-advance-evidence.py`
  to scratch, rc 0, sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (matches the claim).
- Driver lineage: `ExecMutants95/mutants95.py` (sha256 `ff450980dec9e79b3315db276a985ac97df0f950964d751e4416b44c9f3ecf96`,
  95 entries, its v6 receipt 95/95 killed). Copied byte-for-byte to `stage/MutationTester96/mutants96.py`, then edited in
  this seat only: error prefix `MUTANTS96_ERROR`, receipt file name `mutation96-score.txt`, docstring, and 17 appended
  round-96 entries (total 112).

## 1. Totals

| bytes | sha256 | carried 95 | new 17 | total | result |
|---|---|---|---|---|---|
| v6 (red-before) | f7981ba2…ac1fec | 95 killed | 17 broken-pattern (zero matches; refusals absent in v6) | 112 | `MUTATION-SCORE: 95/112 killed, 0 survived, 17 broken-pattern` |
| v7 (after) | 2e28a289…053ec | 94 killed, 1 survived | 15 killed, 2 survived | 112 | `MUTATION-SCORE: 109/112 killed, 3 survived, 0 broken-pattern` |

Before (v6): every carried entry still kills (95/95, identical to the round-95 receipt). The 17 round-96 entries have
no anchor in v6, which the driver reports as broken-pattern (correct: those refusals do not exist there).

## 2. Broken-pattern list

- v7: none (0). Every carried pattern has identical match count on v6 and v7 and is nonzero; every exactly-once
  pattern (head-qualify-off, the round-94 and round-95 exactly-once set, and all 17 new) has count exactly 1 on v7.
  `dispo-fallback-off` (`        m = DISPO_ANY_RE.search(plain)`) has count 1 on v7 and 1 on v6, so no driver fix was needed for it.
- v6 (red-before): the 17 round-96 names, all count 0: nbsp-refuse-off, vt-refuse-off, ff-refuse-off, ls-u2028-off,
  ls-u2029-off, fs-u001c-off, fs-u001d-off, fs-u001e-off, nel-refuse-off, ansi-refuse-off, verdict-window-off,
  verdict-call-off, cyr-idnonascii-off, num2-bracket-off, num2-dash-off, num2-revert-v6, verdict-split-revert.

## 3. Survivors on v7 (findings; not repaired)

All three line numbers are in `kotodama-shokunin/tools/check-advance-evidence.py` (v7).

1. **fs-u001d-off** (new, round 96). Target (v7 line 287):
   `for cpv in ('\u2028', '\u2029', '\u001c', '\u001d', '\u001e'):` → replacement
   `for cpv in ('\u2028', '\u2029', '\u001c', '\u001e'):` (U+001D removed).
   Selftest: rc 0, `SELFTEST PASS 145/145`, zero BAD lines. No v7 pin covers U+001D.
   Probe (`- S001 LOCA<U+001D>TED recheck moved`): v7 refuses `VERDICT-LINESEP`; the mutant returns `{}`, so the
   forged LOCATED line is silently dropped. Real gap: the U+001C–U+001E family is claimed refused, but only U+001C has a pin (FS1).
2. **fs-u001e-off** (new, round 96). Target (v7 line 287): `'\u001d', '\u001e'):` → `'\u001d'):` (U+001E removed).
   Selftest rc 0, `SELFTEST PASS 145/145`, zero BAD. Probe with U+001E: v7 refuses `VERDICT-LINESEP`; the mutant returns `{}`.
   Same gap as survivor 1.
3. **id-lookalike-refuse-off** (carried from round 95, ID1; killed on v6, survives on v7). Target (v7 line 344):
   `            if has_nonascii_letter and re.match(r'^[Ss]\d{3,}$', folded):` → `            if False:`.
   Selftest rc 0, PASS, zero BAD. Cause: v7 adds `_refuse_verdict_channel` (lines 299–300, `ID-NONASCII`) which runs
   before `_refuse_disguised` on every line and refuses the same lookalike ids. Probe over six lookalike ids
   (fullwidth Ｌ001, fullwidth S with ZWSP between S and digits, small-cap ꜱ001, long-s ſ001, Cyrillic а001, fullwidth Ｓ001)
   gave identical outcomes for v7 and the mutant (all `ID-NONASCII`). The v6 branch is therefore shadowed in v7 for every
   probed input; this is a probe-limited equivalence, not a proof. Routed: delete the dead branch, or pin an input only it refuses.

## 4. Round-96 mutants: kill evidence (pin or battery class that catches each)

Every new mutant is killed by the selftest rc≠0 path. Named BAD lines from `work-v7/selftest-<name>.txt`:

| mutant | removed refusal or anchor | BAD pin(s) |
|---|---|---|
| nbsp-refuse-off | VERDICT-NBSP (`'\u00a0' in span`) | round-96 NB1 |
| vt-refuse-off | VERDICT-VT (`'\u000b'`) | round-96 VT1 |
| ff-refuse-off | VERDICT-FF (`'\u000c'`) | round-96 FF1 |
| ls-u2028-off | VERDICT-LINESEP, U+2028 in tuple | round-96 LS1 |
| ls-u2029-off | VERDICT-LINESEP, U+2029 in tuple | round-96 PS1 |
| fs-u001c-off | VERDICT-LINESEP, U+001C in tuple | round-96 FS1 |
| nel-refuse-off | VERDICT-NEL (`'\u0085'`) | round-96 NEL1 |
| ansi-refuse-off | VERDICT-ANSI (`'\u001b'`) | round-96 ANSI1 |
| verdict-window-off | verdict window `for m in re.finditer(...)` replaced by `for m in []` | NB1, VT1, FF1, LS1, NEL1, ANSI1, PS1, FS1 |
| verdict-call-off | call `_refuse_verdict_channel(_rn, _rl)` removed | NB1, VT1, FF1, LS1, NEL1, ANSI1, PS1, FS1, CYR1 |
| cyr-idnonascii-off | ID-NONASCII branch (`if re.search(r'\d{3,}$', core)`) | round-96 CYR1 |
| num2-bracket-off | `\(?\d+[.)]?\)?` removed from `_NUM2` | round-96 BR1 |
| num2-dash-off | `[\u2010-\u2015-]+` removed from `_NUM2` | round-96 DASH1 |
| num2-revert-v6 | `_NUM2.match(t)` replaced by the v6 regex | round-96 BR1, DASH1 |
| verdict-split-revert | `lesson.split('\n')` replaced by `lesson.splitlines()` (line severing restored) | VT1, FF1, LS1, NEL1, PS1, FS1 |

The round-96 pin loop (`selftest`, 8 classes + CYR1 + BR1 + DASH1) is the catching surface. Clean v7 selftest:
`SELFTEST PASS 145/145` (`work-v7/clean-selftest.txt`).

## 5. Stub controls (driver sanity)

- stub1 (`print('stub')`, no SELFTEST PASS line): clean-first refused, `MUTATION-SCORE: 0/112 killed, 112 survived, 0 broken-pattern`, rc 1.
  This is the refused-path control, not the round-95 control shape.
- stub2 (`print("SELFTEST PASS 1/1")`, no grader patterns): `MUTATION-SCORE: 0/112 killed, 0 survived, 112 broken-pattern`, rc 1.
  Same shape as round 95's stub control (95 broken-pattern for 95 entries).

## 6. Commands and return codes

All run with `python3 -B` (commands are reproduced verbatim in the score files' COMMAND lines):

- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 0539276c0e329743200b60e98bf289c540f78864:tools/check-advance-evidence.py > <scratch>/v6/check-advance-evidence-v6.py` → rc 0; sha f7981ba2… (matches claim).
- `sha256sum` on the lane file → 2e28a289… (rc 0); `cp` of the lane file to scratch `v7/` → rc 0, same sha.
- `diff v6 v7 > v6-v7.diff` → rc 1 (differences expected); 82 diff lines.
- Smoke: carried 95 driver against v6 bytes, background job exited 0, `95/95 killed, 0 survived, 0 broken-pattern` (`smoke-v6-run.txt`).
- Pattern-count check (python -B, inline, rc 0): no output rows, i.e. carried v6/v7 counts equal and nonzero, exactly-once = 1.
- New-pattern count check (python -B, inline, rc 0): 112 entries, 112 unique names, all 17 new v7 counts = 1, v6 counts = 0.
- Full driver run v7: `python3 -B mutants96.py --tool <lane>/tools/check-advance-evidence.py --work <scratch>/work-v7` → rc 1 (3 survivors).
- Full driver run v6: `... --tool <scratch>/v6/check-advance-evidence-v6.py --work <scratch>/work-v6` → rc 1 (17 broken-pattern).
- Stub runs: rc 1 and rc 1 (section 5).
- `probe96.py` (python -B, inline probe, rc 0): probes in section 3.
- Score files written to stage with COMMAND and COMMAND-RC lines (rc values above; v7 rc 1, v6 rc 1, stub2 rc 1).

## 7. Tooling

Installed or upgraded tools: none. Tooling record: none. No pacman, no sysctl, no git/jj mutation, no write to
the fleet root or any other lane. The only repo reads were `git show` and `sha256sum`.

## 8. Scratch

`/fast/scratch/hyaku/kotodama-r96/MutationTester96/` (v6, v7, work dirs, probe) is deleted before yield. Every number here regenerates from the commands in section 6.

## 9. Routed to the grader owner (not repaired here)

1. Pin U+001D and U+001E (the v7 FS family). Survivors 1 and 2 are a real forgery path: a verdict with these codepoints is refused in v7 but silently dropped when its refusal is absent.
2. Resolve the shadowed v6 ID-NONASCII branch (survivor 3): delete it, or pin an input only it refuses.
3. Claim O leg O3 (`killed == total, 0 survived`) fails at this measurement; the L1 must record it as measured.

Stage outputs: `stage/MutationTester96/mutants96.py` (sha256 30d2fc8616baf1b5783068f792da41051f7232c680c15a9290900f3d1ee8660c),
`mutation-score-v7.txt`, `mutation-red-before-v6.txt`, `stub-control-allpattern-broken.txt`, `DONE`.
