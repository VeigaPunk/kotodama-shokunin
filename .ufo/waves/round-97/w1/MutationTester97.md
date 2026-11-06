# MutationTester97 — round-97 mutation probe of grader v9

Seat: MutationTester97 (attack seat; never repairs the grader). Wave: round-97/w1.
Dependency: waited for `.ufo/waves/round-97/w1/stage/ExecGraderV9/V9-READY` with the bounded
loop (`for i in $(seq 1 90); do [ -f <dep> ] && break; sleep 60; done`); marker appeared after
~24 min containing `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b`.

## Verdict

- Frozen driver: `mutants97.py`, sha256 `f9c623fd384d276ad2b53ea10d67ac021a2fc77a3baca50df33d5e505bd22259`,
  pin `reports/round-97/controls/mutants97.sha256` = `f9c623fd384d276ad2b53ea10d67ac021a2fc77a3baca50df33d5e505bd22259  mutants97.py`.
- Official first measurement (lane v9 `tools/check-advance-evidence.py`, sha256
  `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b`):
  `MUTATION-SCORE: 121/121 killed, 0 survived, 0 broken-pattern`, driver rc=0. No survivors.
- Red-before (v8 bytes `f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0`):
  `MUTATION-SCORE: 111/121 killed, 0 survived, 10 broken-pattern`, driver rc=1. The 10
  round-97 mutants have no anchor on v8 (v8 lacks the refusal surface entirely); the 111
  carried mutants all kill on v8.
- Broken-pattern on v9: none. Survivors on v9: none (nothing to name). Survivors on v8: none.

## Files written (all sha256 measured)

| file | sha256 |
|---|---|
| `.ufo/waves/round-97/w1/stage/MutationTester97/mutants97.py` | `f9c623fd384d276ad2b53ea10d67ac021a2fc77a3baca50df33d5e505bd22259` (20791 B, frozen at pin time) |
| `reports/round-97/controls/mutants97.sha256` | pin, written before the first measurement |
| `reports/round-97/controls/mutation97-first.txt` | `56759fe3fda92c4dbfd79a1670d91a122e765becd515252e48640520e39ecc45`, 125 lines, first line `DRIVER-SHA256 f9c623fd…` |
| `.ufo/waves/round-97/w1/stage/MutationTester97/red-before-v8.txt` | `74c62f1636eb36c512bff7e30b7d19297c062b4d698a899b8afaa18bac7e9c0d`, first line `DRIVER-SHA256 f9c623fd…` |
| `.ufo/waves/round-97/w1/MutationTester97.md` | this report |
| `.ufo/waves/round-97/w1/stage/MutationTester97/DONE` | written last, contains the mutants97.py sha |

## Driver construction

`mutants97.py` = frozen round-96 `mutants96.py` with: round-97 docstring;
`mutation96-score.txt`→`mutation97-score.txt`; `MUTANTS96_ERROR`→`MUTANTS97_ERROR` (3 sites);
a `DRIVER-SHA256 <sha256 of own bytes>` first stdout line (printed right after argparse,
`flush=True`); and 10 new mutant tuples appended to `MUTANTS`. CLI unchanged
(`--tool <path> --work <dir>`, optional `--only`); summary line unchanged
(`MUTATION-SCORE: <killed>/<total> killed, <survived> survived, <broken> broken-pattern`).
The 111 carried tuples are byte-identical to round-96.

Pattern re-verification before freeze (both via importlib count and the generator's
post-write assert pass): all 111 carried `old` patterns match on v9; every `exactly-once`
entry matches exactly once; zero-match list empty; nothing needed fixing. New-mutant
patterns were sliced mechanically from the v9 bytes (never retyped).

## The 10 round-97 mutants (all `matches=1 semantics=exactly-once`, all KILLED on v9)

3 remove the new named refusals whole; 7 remove a per-class anchor (one per CriticO96 class).

| name | class(es) | v9 anchor (line) | mutation |
|---|---|---|---|
| `verdict-ctrl-off` | CR1+US1+NUL1 | `_refuse_verdict_channel`, 318–320 | `if o < 0x20:` → `if False:` (VERDICT-CTRL refusal removed) |
| `verdict-separator-off` | OGH1+IS1 | 321–323 | `if unicodedata.category(c) == 'Zs':` → `if False:` (VERDICT-SEPARATOR removed) |
| `heading-combining-off` | CM1+CMW2 | 738 | `for _h in heads:` → `for _h in []:` (HEADING-COMBINING loop removed) |
| `cr1-allow-000d` | CR1 | 316 | verdict-window allowlist `(0x09, 0x0b, 0x0c, 0x1b, …)` gains `0x0d` |
| `us1-allow-001f` | US1 | 316 | allowlist gains `0x1f` before `0x85` |
| `nul1-allow-0000` | NUL1 | 316 | allowlist gains `0x00` |
| `ogh1-zs-exempt-1680` | OGH1 | 321 | `== 'Zs':` → `== 'Zs' and o != 0x1680:` |
| `is1-zs-exempt-3000` | IS1 | 321 | `== 'Zs':` → `== 'Zs' and o != 0x3000:` |
| `cm1-mark-lasttoken-only` | CM1 | 739 | mark check `for _c in _h):` → `for _c in _h.split()[-1]):` (marks confined to the numbering token escape) |
| `cmw2-mark-numbering-only` | CMW2 | 739 | mark check → `for _t in _h.split() if re.match(r'^[0-9(.\[\)]+[.)]?$', _t) for _c in _t):` (marks in phrase words escape) |

## Commands and rc (chronological)

1. `git show 1ffc5a83d2c70e3bc581594efbcf32c562ba2569:tools/check-advance-evidence.py > $S/v8-check-advance-evidence.py && sha256sum …` — rc 0, sha `f29ab013…` (v8 bytes verified).
2. `sha256sum tools/check-advance-evidence.py` (after V9-READY) — rc 0, sha `1021dc9d…`; byte-identical scratch snapshot `cp` rc 0.
3. Carried-pattern counts on v8 and v9 (importlib, `src.count(old)` per tuple) — rc 0; zero-match `[]`, exactly-once≠1 `[]` on both.
4. `python3 gen97.py` (scratch generator; writes stage/mutants97.py, asserts every new `old` count==1 on v9) — rc 0, printed `mutants 121`, `broken-vs-v9: []`, sha `f9c623fd…`.
5. Dev full run vs scratch v9 copy: `python3 -B stage/mutants97.py --tool $S/v9-check-advance-evidence.py --work $S/dev9full` — rc 0, `MUTATION-SCORE: 121/121 killed, 0 survived, 0 broken-pattern` (pre-freeze confirmation; receipt kept in scratch).
6. Dev full run vs scratch v8 (111-mutant draft driver) — rc 0, `MUTATION-SCORE: 111/111 killed, 0 survived, 0 broken-pattern` (carried table healthy on v8).
7. Pin write: `printf '%s  mutants97.py\n' f9c623fd… > reports/round-97/controls/mutants97.sha256` — rc 0; re-read shows `f9c623fd…  mutants97.py`.
8. **First measurement (run once, lane v9):** `python3 -B .ufo/waves/round-97/w1/stage/MutationTester97/mutants97.py --tool tools/check-advance-evidence.py --work $S/first > reports/round-97/controls/mutation97-first.txt` — driver rc 0 (service log `rc=0`); receipt: `TOOL sha256=1021dc9d…`, `CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True`, 121 KILLED rows, 0 SURVIVED, 0 BROKEN, `MUTATION-SCORE: 121/121 killed, 0 survived, 0 broken-pattern`.
9. Red run: same frozen driver vs scratch v8 bytes `> stage/MutationTester97/red-before-v8.txt` — driver rc 1 (service log `rc=1`); receipt: `TOOL sha256=f29ab013…`, `CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True`, 111 KILLED, 0 SURVIVED, 10 BROKEN-PATTERN, `MUTATION-SCORE: 111/121 killed, 0 survived, 10 broken-pattern`. Broken list = exactly the 10 round-97 names above.
10. Lane v9 bytes untouched by the probe (driver mutates only its `--work` copies): final `sha256sum tools/check-advance-evidence.py` — rc 0, still `1021dc9d…`. No restoration needed; no lane byte was ever modified.

## Notes

- Every DRIVER-SHA256 line in both receipts equals the pin (`f9c623fd…`), printed from the
  frozen file bytes at run time — pin == first-receipt sha == red-receipt sha == current file sha.
- Survivors: none on v9 and none on v8, so there is no survivor to name; the only non-kill
  class is the 10 broken-pattern entries on v8, named above with their mutation text.
- No grader repair was made or attempted (ExecGraderV9 owns that).
- Tooling installs: none (no new tools needed; pacman untouched).
- Scratch `/fast/scratch/hyaku/kotodama-r97/MutationTester97/` deleted before yield.
