# MutationTester99 — round-99 mutation attack on grader v11

Seat: MutationTester99 (attack only; no grader repair). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `527df3fee305b3454446946e6779ece45456307e`, freeze `b1b80562edfc8f6082aec74bbbf0f25e152708a8`.
No frozen file (`claims.json`, `predispatch.py`, `battery99.py`, `battery99.sha256`, control receipts,
`reports/round-99/controls/` other than the two mutation files) was edited. No commit, no jj mutation,
no model choice. Scratch `/fast/scratch/hyaku/kotodama-r99/MutationTester99` removed before yield.

## 1. Artifacts and shas

| artifact | sha256 | note |
|---|---|---|
| `.ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py` | `cf58e12632037e2d923ec0add6de431374def80d899603f8b067a91852872ffd` | 136 mutants, 27571 B |
| `reports/round-99/controls/mutants99.sha256` | `cf58e126…` | `<sha>  mutants99.py` |
| `reports/round-99/controls/mutation99-first.txt` | first line `DRIVER-SHA256 cf58e126…` | 140 lines, full first-run stdout |
| `.ufo/waves/round-99/w1/stage/MutationTester99/red-before-v10.txt` | first line `DRIVER-SHA256 cf58e126…` | 140 lines, v10 control |

Landed grader under test: `tools/check-advance-evidence.py` sha256
`717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2` (V11-READY matches).
v10 export used for the red-before control: sha256
`d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` (base `527df3fe`).

## 2. Driver

`mutants99.py` keeps the round-98 CLI (`--tool <path> --work <dir> [--only names]`), first stdout line
`DRIVER-SHA256 <sha of its own bytes>`, summary line
`MUTATION-SCORE: <killed>/<total> killed, <survived> survived, <broken> broken-pattern`.
It carries all 128 round-98 mutants unchanged (82 `replace-all`, 46 `exactly-once`) and adds 8
round-99 mutants (all `exactly-once`): 82 + 54 = 136. Every pattern was counted against the final
v11 bytes before the pin: `src.count(old)` gives 136/136 matches, 0 zero-match, 0 multi-match on an
`exactly-once` entry (command in §6, rc 0). Kill oracle: the mutated tool's own `--selftest` first;
a mutant that survives is re-run through frozen `battery99.py` and killed if any battery class
outcome differs from the clean baseline. All 136 were killed by the selftest; the battery fallback
was never needed (`oracle=selftest` on 136 rows, `oracle=battery99` on 0).

Round-99 mutants (mutation text, v11 line, detector):

| mutant | mutation | v11 line | killed by |
|---|---|---|---|
| `heading-widen-all-M` | invariant arm `if (head_anchors(h), head_span_anchors(h)) != (head_anchors(plain), head_span_anchors(plain)):` → `if True:` (refuse every mark, v10 behaviour) | 831 | selftest MCOK1 (Mc on Devanagari) |
| `heading-widen-all-Mn` | same arm → `if any(unicodedata.category(_c) in ('Mn','Me') for _c in h):` (refuse every Mn/Me on any base, v9 behaviour) | 831 | selftest DEVAOK1 (virama U+094D Mn) |
| `heading-mark-base-rule-off` | same arm → `if False:` (CM1, CM1-DEVANAGARI, MARKDASH, ROMANMARK reopen) | 831 | selftest CM1 / MARKDASH |
| `heading-phrase-degradation-off` | phrase arm `if any(norm(p) == norm(bare) for p in phrases):` → `if False:` (CMW2 reopens) | 846 | selftest CMW2 |
| `heading-plain-raw` | `plain = ''.join(_ch for _ch in unicodedata.normalize('NFKD', h)` + the M-filter line → `plain = h` (invariance never fires) | 829-830 | selftest CM1 / MARKDASH |
| `heading-number-restore` | re-insert the v10 HEADING-NUMBER loop after `_nonascii_number` | 771 | selftest NUMOK1 / NUMOK2 |
| `nfkd-me-neuter` | NFKD recovery `... category(c)[0] != 'M'` → `!= 'Mn'` (Me mark survives) | 363 | selftest NFKDME1 |
| `selftest-g99-cm1deva-rc-off` | flip the new CM1-DEVANAGARI pin expected rc `1` → `0` | 2091 | selftest pin |

The three v10 heading mutants (`heading-combining-off`, `cm1-mark-lasttoken-only`,
`cmw2-mark-numbering-only`) still match the v11 pre-filter line and still kill. The four
interim-helper mutants written against the superseded `a56965b5`/`73b0355c` helpers were re-slanted
to the final invariant helper before the final pin (§5).

## 3. First measurement (v11, one run)

Command: `python3 -B .ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py --tool tools/check-advance-evidence.py --work /fast/scratch/hyaku/kotodama-r99/MutationTester99/first2`
→ **rc 0**, wall 1085.60 s. Receipt `reports/round-99/controls/mutation99-first.txt`:

```
DRIVER-SHA256 cf58e12632037e2d923ec0add6de431374def80d899603f8b067a91852872ffd
TOOL sha256=717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2
CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True
… 136 mutant rows …
MUTATION-SCORE: 136/136 killed, 0 survived, 0 broken-pattern
```

Counts on the receipt: `KILLED=136 SURVIVED=0 BROKEN=0`, `oracle-selftest=136 oracle-battery99=0`
(commands in §6, rc 0). **Survivors on v11: none. Broken-pattern on v11: none.**

## 4. Red-before-v10 control

Command: `python3 -B .ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py --tool /fast/scratch/hyaku/kotodama-r99/MutationTester99/v10.py --work /fast/scratch/hyaku/kotodama-r99/MutationTester99/red`
→ **rc 1**, wall 878.11 s. Receipt `red-before-v10.txt`:
`MUTATION-SCORE: 128/136 killed, 2 survived, 6 broken-pattern`.

Broken-pattern (6, all v11-only anchors, `matches=0`): `heading-widen-all-M`,
`heading-widen-all-Mn`, `heading-mark-base-rule-off`, `heading-phrase-degradation-off`,
`heading-plain-raw`, `selftest-g99-cm1deva-rc-off`.

Survivors on v10 (2), with mutation text and line:

* `heading-number-restore` — re-inserts the HEADING-NUMBER loop after the fullwidth-stop arm
  (v10 line 758). **No-op on v10**: v10 already has that loop at lines 759-766, so the duplicate
  changes no outcome (selftest rc 0). It kills on v11, where the loop is absent (NUMOK1/NUMOK2).
* `nfkd-me-neuter` — `nfkd_nomark = ''.join(c for c in nfkd if unicodedata.category(c)[0] != 'M')`
  (v10 line 358) → `!= 'Mn'`. v10 has no NFKDME1 selftest pin; the scratch tool path
  (`/fast/scratch/.../v10.py`) makes the driver's battery99 path derivation return None, so the
  battery fallback did not run. It kills on v11 through the new NFKDME1 pin.

Neither survivor is a v11 defect: both are v10-specific coverage facts (a shared anchor line and a
missing v10 pin). On v11 both are killed by the selftest.

## 5. Superseded freeze (disclosed)

The first freeze (driver sha `8476735f…`) ran against the first v11 byte
`a56965b5…`; the run was stopped after 1 line when ExecGraderV11 reported the tool was being
rewritten. The tool then moved `a56965b5…` → `73b0355c…` → `717341dc…` (final), and the four
round-99 mutants written against the interim module-level helper no longer matched. They were
re-slanted to the final invariant helper (table in §2), the driver was re-verified (136/136
patterns), re-pinned at `cf58e126…`, and the first measurement was re-run once against the landed
bytes. The superseded 1-line receipt is preserved at
`.ufo/waves/round-99/w1/stage/MutationTester99/mutation99-first-superseded-tool-a56965b5.txt`.
No edit to `mutants99.py` followed the final first receipt; driver sha = pin = first-receipt
`DRIVER-SHA256` = `cf58e126…`.

## 6. Commands and rc

| command | rc |
|---|---|
| `git -C … show 527df3fe…:tools/check-advance-evidence.py > /fast/scratch/…/v10.py` | 0 |
| `sha256sum /fast/scratch/…/v10.py` → `d35b13c9…` | 0 |
| `sha256sum tools/check-advance-evidence.py` → `717341dc…` | 0 |
| pattern-count script (import driver; `src.count(old)` over v11) → `total 136 bad 0` | 0 |
| `python3 -m py_compile …/mutants99.py` → `COMPILE_OK` | 0 |
| pre-freeze `--only` check of the 8 round-99 mutants (interim driver before the docstring-only final edit) → `8/8 killed` | 0 |
| `printf '<sha>  mutants99.py' > reports/round-99/controls/mutants99.sha256` | 0 |
| first measurement (§3) → `136/136 killed, 0 survived, 0 broken-pattern` | 0 |
| `grep -c ' KILLED '` → 136; `grep -c ' SURVIVED '` → 0; `grep -c ' BROKEN-PATTERN '` → 0 | 0 |
| `grep -c 'oracle=selftest$'` → 136; `grep -c 'oracle=battery99$'` → 0 | 0 |
| red-before-v10 (§4) → `128/136 killed, 2 survived, 6 broken-pattern` | 1 |
| `sha256sum …/mutants99.py` → `cf58e126…`; `cat …/mutants99.sha256` → same; `head -1 mutation99-first.txt` → same | 0 |

Tooling installed/upgraded: none. Host sysctls untouched; pacman not run.
