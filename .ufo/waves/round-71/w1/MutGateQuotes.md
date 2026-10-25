# MUTGATEQUOTES — Gate-quotes checker mutation test (round 71, wave 1)

- Seat: `L1Kotodama71.MutGateQuotes` (LEAF mutation tester)
- Date: 2026-10-25
- Target: `tools/check-gate-quotes.py` (lane tool, frozen at round-71 base revision `b94a543`)
- Defect class probed: V70-3 (round-70 Gate quote exceeded the ≤25-word cap; the gate must catch any regression in the quote-cap, doubled-locator, html-entity, and file-coverage checks)
- Method: byte-identical copy of the lane tool into a scratch sandbox (`/tmp/mut-gate-quotes/`), 5 single-point mutations, same bounded detector (`--selftest`, 52 cases) on pristine vs each mutant. Lane tool never modified.

## Baseline (pristine)

- Command: `python3 -B pristine.py --selftest`
- Result: exit 0, stderr empty, `SELFTEST: 52/52 pass`, zero FAIL lines
- sha256 pristine = sha256 lane tool = `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`

## Mutations (one per scratch copy, from pristine bytes)

| # | Mutant | Mutation (smallest behavior-bearing point) | Before hash | After hash |
|---|--------|---------------------------------------------|-------------|------------|
| 1 | mut1_drop_overcap.py | `scan_line`: `if words > MAX_WORDS:` → `if False:` (drops the ≤25-word check) | 54981859… | 49efabc401a2ac78e6796b1bdd6e124f918ba2eafb8528d97b18a3d079ab9503 |
| 2 | mut2_cap27.py | `MAX_WORDS = 25` → `MAX_WORDS = 27` (allows a 27-word quote) | 54981859… | 4142167baa113f52d4da4f492460896ad6b5032f9a6402af0c148913855b0648 |
| 3 | mut3_doubled_locator.py | `doubled_locator` return: `bool(quoted_title) and quoted_title in locator` → `False` (allows doubled locators) | 54981859… | bbde924096436d49fb36b54f6518ccf828040801ee14a5033d0dd7eb2bcaa48d |
| 4 | mut4_no_html_entity.py | `decode_html_references.decode`: deleted `found = True` (html-entity never reported; decoding still performed) | 54981859… | ef3c6e041ebbed768e9b62b2eff5b87dd0f9436ea7a9a0ea88b38f39ae9e8e5e |
| 5 | mut5_skip_entity.py | `check`: skip any path whose basename starts with `entity` (reports 0 findings, never opens the file) | 54981859… | fc65f3022f27d9b58e1bce723ec80c4640c71586d79215429a8dfbb27b211b21 |

## Detector results (same bounded detector on each mutant; no baseline failures existed)

### mut1_drop_overcap — KILLED
- Exit 1, `SELFTEST: 45/52 pass`, stderr empty
- Failing cases (7): `26-words`, `curly-26-words`, `anchor-join-27`, `hard-wrapped-26`, `guillemets-26`, `star-bullet-26`, `decoded-quote-marks-over-cap-red` — all want an over-cap finding, got 0/`html-entity` only.
- Confirms: dropping the word-cap check is caught (the exact V70-3 defect class).

### mut2_cap27 — KILLED
- Exit 1, `SELFTEST: 45/52 pass`, stderr empty
- Failing cases (7): same set as mut1 — a 26-word quote and the 27-word anchor-join quote with slide under the raised cap, but the detector expects them red.
- Confirms: a cap drift to 27 words is caught.

### mut3_doubled_locator — KILLED
- Exit 1, `SELFTEST: 48/52 pass`, stderr empty
- Failing cases (4): `doubled-locator-single-quoted-red`, `doubled-locator-double-quoted-red`, `doubled-locator-wayback-note-red`, `decoded-doubled-locator-red` — all want `doubled-locator`, got none/`html-entity` only.
- Confirms: a doubled locator is caught.

### mut4_no_html_entity — KILLED
- Exit 1, `SELFTEST: 34/52 pass`, stderr empty
- Failing cases (18): 7 reference-decoding cases (`numeric-decimal-bare-before-space` … `invalid-out-of-range-codepoint`) want `found=True`; 9 class cases (`html-entity-named-red`, `html-entity-once-per-row`, `double-encoded-ellipsis-decoded-once`, `decoded-truncated-grounds-red`, `decoded-whole-grounds-green`, `decoded-quote-marks-over-cap-red`, `decoded-quote-marks-short-green`, `decoded-ellipsis-red`, `decoded-doubled-locator-red`) lose the `html-entity` finding; 2 behavioural runs (`behavioural-entity-label`, `behavioural-continue-after-unreadable`).
- Confirms: allowing an HTML entity (silencing the `html-entity` report) is caught.

### mut5_skip_entity — KILLED
- Exit 1, `SELFTEST: 50/52 pass`, stderr empty
- Failing cases (2): `behavioural-entity-label` (want exit 1 + `GATE_QUOTES: 1 findings`, got exit 0 + `0 findings`), `behavioural-continue-after-unreadable` (want the entity finding in the mixed run, got `0 findings`).
- Confirms: silently skipping a file is caught.

## Verdict

- All 5 mutants killed by the selftest: every mutated tool reports FAIL cases and exits 1 where the pristine tool reports 52/52 and exits 0. No mutant survived; no baseline failure was observed (pristine = 52/52), so no inconclusive verdicts.
- The gate detector demonstrably catches all five probed defect classes, including V70-3 (cap violation) and the sibling classes (27-word quote, doubled locator, HTML entity, skipped file).

## Restoration / hygiene evidence

- Lane tool untouched: `sha256sum tools/check-gate-quotes.py` still `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` (unchanged at run end); `diff` lane tool vs scratch pristine = identical.
- No lane repo bytes were written by the mutation work; mutations were applied only to scratch copies under `/tmp/mut-gate-quotes/` (declared disposable; kept for evidence, pristine.py retained as the byte-identical reference).
- Sibling lane files, git/jj state, and the lane tool were not modified.
- Tooling installed: none (no installs/updates; Python 3 stdlib only).

## Evidence artifacts

- `/tmp/mut-gate-quotes/pristine.py` — byte-identical copy of the lane tool (sha256 = lane tool)
- `/tmp/mut-gate-quotes/mut{1..5}_*.py` — mutants with recorded hashes above
- Full per-run outputs captured during the run (exit codes, summary lines, and FAIL case lists reproduced above)
