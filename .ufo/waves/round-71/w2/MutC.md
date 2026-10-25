# MutC — mutation probe of `reports/round-71/accept-c.py` (claim C)

Seat: `L1Kotodama71.MutC` (mutation-tester, round 71 wave 2). Lane read-only; all mutation in scratch.

## Verdict

**PASS (counter discriminates).** All 4 mutants KILLED. None is killed by the frozen PASS at the measured revision alone, except M3a: M1, M2 and M3b produce byte-identical output to the frozen counter on the pristine corpus and are killed only by single-leg fault fixtures.

## Setup

- Lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`; counter sha256 `1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4` (lane and scratch identical).
- Scratch: `git archive HEAD | tar -x -C /tmp/mutc71.4ney/lane` (fresh git repo, disposable).
- Driver: `python3 -B /tmp/mutc71-driver.py`. It mutates the scratch counter in place, runs it against each fixture with `--root <fixture>`, restores the pristine bytes in a `finally` block, and checks the sha256 after each mutant. Raw outputs are in `/tmp/mutc71.4ney/out/<counter>__<fixture>.txt`.
- Detector: the same counter invocation on 4 fixture roots (copies of the scratch lane). Kill = the verdict or output differs from the frozen counter on the same root.

| Fixture | Construction | Frozen result |
|---|---|---|
| F0-pristine | unchanged HEAD tree | exit 0, PASS, no failing leg |
| F1-usedby-ghost | S861 used-by cell gets `, corpus/knowledge/culture-material/ghost-entry.md` (entry path kept) | exit 1, FAIL, only `USEDBY-PATHS` fails |
| F2-cited-8 | S869–S873 tokens removed from the entry (13 → 8 distinct ids) | exit 1, FAIL, only `CITED` fails |
| F3-counts-35-242 | `adornment-body-codes.md` deleted (36/243 → 35/242) | exit 1, FAIL, only `COUNTS` fails |

Each fixture makes the frozen counter fail exactly one leg (the targeted one). The baseline is not failing for an unrelated reason, so no result is inconclusive.

## Mutants and results

| Mutant | Edit (single exact match) | F0 | F1 | F2 | F3 | Verdict |
|---|---|---|---|---|---|---|
| M1-usedby-skip | `bad.append((sid, p))` → `pass` | same output (PASS) | **flip FAIL→PASS** | same | same | KILLED by F1 |
| M2-cited-floor-6 | `len(cited) >= 12` → `>= 6` | same output (PASS) | same | **flip FAIL→PASS** | same | KILLED by F2 |
| M3a-counts-35-242 | `(cm == 36) and (ctotal == 243)` → `(cm == 35) and (ctotal == 242)` | **flip PASS→FAIL** (COUNTS) | output diff (+COUNTS fail) | output diff (+COUNTS fail) | **flip FAIL→PASS** | KILLED by F0 and F3 |
| M3b-counts-accept-35-242 | → `(cm in (35, 36)) and (ctotal in (242, 243))` | same output (PASS) | same | same | **flip FAIL→PASS** | KILLED by F3 |

Mutant sha256: M1 `09d84edd…01223`, M2 `3204a4d5…56817`, M3a `5f740adb…fc6`, M3b `5d7cdfa8…a89`.

Key diff lines from the actual output:
- M1/F1: frozen `LEG FAIL USEDBY-PATHS` / `missing-paths=[('S861', 'corpus/knowledge/culture-material/ghost-entry.md')]`; mutant `LEG PASS USEDBY-PATHS` / `missing-paths=[]`, then `ACCEPT-C-71: PASS`.
- M2/F2: frozen `LEG FAIL CITED`; mutant `LEG PASS CITED` with detail `distinct S-ids cited=8 (want >=12)`, then `ACCEPT-C-71: PASS`.
- M3a/F0: frozen `LEG PASS COUNTS`; mutant `LEG FAIL COUNTS` (`culture-material=36 corpus=243 (want 36/243)`), then `ACCEPT-C-71: FAIL`, exit 1.
- M3b/F3: frozen `LEG FAIL COUNTS`; mutant `LEG PASS COUNTS` (`culture-material=35 corpus=242`), then `ACCEPT-C-71: PASS`.

## Restoration evidence

- Before each mutant: `1df995c2207c…`. After restoring each mutant: `1df995c2207c…`, `restore-ok=True` for all 4.
- Restored counter output was identical to the frozen output on all 4 fixtures (`True`).
- Final scratch counter sha256: `1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4`.
- Lane counter sha256 after the probe is unchanged. `git status --short` in the lane shows only sibling-seat files and the existing untracked `reports/round-71/telemetry/measures-c.txt`; this seat wrote nothing besides this file.

## Independent re-derivation (lane)

- `find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*.md' | wc -l` → 36
- `find corpus/knowledge -mindepth 2 -maxdepth 2 -type f -name '*.md' | wc -l` → 243 (recursive count is also 243)
- `grep -oE 'S[0-9]{3,}' <entry> | sort -u | wc -l` → 13 (S861–S873). All rows are at `corpus/SOURCES.md:816-828`.
- `python3 -B reports/round-71/accept-c.py --root .` → all 7 legs PASS, `ACCEPT-C-71: PASS`, exit 0.

## Coverage findings (surviving-on-pristine; not contract changes)

1. **No built-in negative fixtures.** At the measured revision, M1, M2 and M3b are output-equivalent to the frozen counter. The landed PASS receipt alone cannot show that the USEDBY-PATHS, CITED-floor or COUNTS-exactness legs ever bite. Discrimination exists only through external fault fixtures like F1–F3.
2. **CITED detail string is decoupled from the threshold.** The `want >=12` text is a literal, so M2 prints `LEG PASS CITED` next to `cited=8 (want >=12)`. That output contradicts itself, and a reader of the receipt cannot see that the threshold changed.
3. **Docstring overclaims CITED.** It says ">=12 NEW SOURCES rows (S ids opened this round…)", but lines 72–74 count every distinct `S\d{3,}` token in the entry, and nothing reads the `opened` cell (`cells[9]`). New-ness is only approximated by the ROWS leg's requirement that used-by name the entry. An older row whose used-by was edited to name the entry would count.
4. **USEDBY-PATHS is mostly subsumed.** When ROWS passes, every cited row's used-by contains the entry and ENTRY verifies that the entry exists. So USEDBY-PATHS can only catch extra, non-entry ghost paths, which is exactly what F1 had to construct.
5. Minor dead code: the `corpus` variable (line 60) is computed and never used. The docstring says "find | wc -l", but the code uses non-recursive `os.listdir`. The two agree today (243 = 243 recursive).

## Tooling

No installs or updates.
