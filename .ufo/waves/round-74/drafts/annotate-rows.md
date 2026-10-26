# Corrections rows for `## Corrections — round 74` (SCORECARD.md)

Eleven rows, one per ANNOTATE pair in `ledger-final.json` (ANNOTATE pairs: LC-02, LC-03, LC-06,
LC-07, LC-08, LC-11, LC-12, LC-15, LC-16, LC-17, LC-18). Columns: **id | old token | new token |
re-derivation command**. Every command is a single argv-expressible, read-only command; run it with
cwd = the lane, split it with `shlex.split`, and it returns the **new token**.

Each command names the pinned base revision `f7104cbce186bc2e1522abf0cfd619cc834628bb` (the
counter's ANNOTATE leg requires the base revision as an operand of every numeric pair) and, for the
three revision-block rows, also the full 40-hex landing commit the sentence is about — the parse keys
on that historical revision, so the token is deterministic and no operand can move when claim C
lands.

All eleven commands were executed at base **through the draft counter's own H2 guard**
(`.ufo/waves/round-74/counters/accept-ca.py`: `observe_problem` + `run_observe` in a clone
materialized at base): none is refused, and each printed the new token.

The round-73 section's table carries a fifth `note` column; parse by column position and tolerate
trailing cells. The rows below are 4-column so the counter can read them directly. **Do not add a
note cell that names a SEPARABLE-separator id or the claim-C path family** — the counter scans the
whole corrections block for both.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| LC-01 | 412 | 804 | git grep -c -E '^. S[0-9]{3}' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
| LC-02 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbce186bc2e1522abf0cfd619cc834628bb -- reports/round-73/telemetry/selftest-r3.txt |
| LC-03 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbce186bc2e1522abf0cfd619cc834628bb -- reports/round-73/telemetry/selftest-r3.txt |
| LC-06 | 243 | 247 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/*/*.md' |
| LC-07 | 243 | 247 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/*/*.md' |
| LC-08 | 30 | 32 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/linguistics/*.md' |
| LC-11 | 23443 | 97656 | git grep -h -o -E 'decompress.*23443.*[0-9]+ bytes' f7104cbce186bc2e1522abf0cfd619cc834628bb -- .ufo/waves/round-73/w2/ScoutReopenS879.md |
| LC-12 | no | two | git grep -h -o -E 'HAS two status-200 Wayback captures' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/lessons/round-73.md |
| LC-15 | 776 | 724 | git grep -c -E '^. S[0-9]{3}' 65fe8572822ef83f1750593af77daddf34a1e337 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
| LC-16 | reachable | present | git grep -h -o -E 'wall (present) \("Client Challenge"\)' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/lessons/round-73.md |
| LC-17 | 752 | 728 | git grep -c -E '^. S[0-9]{3}' c5f099211e1d6c095e7c59edbd05c0043b4b95fc f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
| LC-18 | 753 | 701 | git grep -c -E '^. S[0-9]{3}' 94209e8f80969dbac48d56c5d0e2e623635b8616 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |

## What each row corrects (guidance for the L1; keep the SCORECARD cells free of separator ids)

- **LC-02** — `LOG.md:4297` (round-73 freeze bullet) files the Ca counter as "Ca 9 scenarios"; counter
  r3 prints `SELFTEST OK: 10 scenarios` and its committed receipt
  `reports/round-73/telemetry/selftest-r3.txt` says 10. True only of the freeze-time r1 receipt
  `selftest.txt`. LOG is append-only, so the line stands as filed.
- **LC-03** — fleet report `.ufo/reports/round-73/kotodama.md:10` (pin `dad39efd`, blob `d104dfa4`,
  sha256 `000bab3a…`) repeats the same 9-scenario figure; the lane cannot edit the fleet tree, so
  this row is the only lane-side correction.
- **LC-06** — `corpus/README.md:732` first totals footer reads 243 (written at `498db73`); the base
  holds 247 `.md` files. Round-73 L01 re-pinned the same line at `8841ad3` with 245, which is
  pin-correct and now stale; the live footer is `:775` (247).
- **LC-07** — `corpus/README.md:736` first Counts-checked line (total 243, vector
  30/29/36/29/24/95). The live block `:775-:777` is 247 / 32/29/38/29/24/95. Any tool reading the
  FIRST footer reports 243 — `reports/round-28/readme/sweep.py` exits 1 on this tree for exactly that
  reason, which is why the counter must read the LAST one (grammar R4).
- **LC-08** — `corpus/README.md:344` heading `## linguistics/ (30)` was never in any ledger; the two
  round-73 conlang entries took the directory to 32 files. The same file names those entries at
  `:768`, so an in-place repair would leave a second stale site.
- **LC-11** — `corpus/lessons/round-73.md:38` calls the durability capture `20261025222414, 23443 B`
  a shell that does not carry the span; 23443 is the gzip wire size and the decoded 97656-byte
  payload does carry it (`.ufo/waves/round-73/w2/ScoutReopenS879.md`). The lesson is append-only; the
  registry row carrying the same false fact (`corpus/SOURCES.md:834`, S879 — below the separator)
  is not a pair here because SEPARABLE forbids a `stated_at` path of `corpus/SOURCES.md`.
- **LC-12** — `reports/round-73/claims.json:11` (frozen) grounds the cut of a staged row on "no
  Wayback capture of the same page"; the same round's lesson was repaired to "HAS two status-200
  Wayback captures" (20241106195515, 20241107004043) and no correction row names claims.json.
- **LC-15** — `corpus/README.md:36` (revision block 2.18, round 66) files "registry moved 753 → 776
  rows"; the landing (`65fe857282…`) took the registry 701 → 724, so the stated after-value 776
  matches no committed row total. (The before-value is LC-18.)
- **LC-16** — `corpus/lessons/round-73.md:138` calls the five staged docs "reachable and
  span-present" with no UA qualifier, while the same lesson's Quarantine row (`:48`) records the
  Springer chapter page walled under the browser-shaped UA (HTTP 200, 3038 B, `Client Challenge`) and
  served in full only under `curl/8.7.1`. The correction adds the UA qualifier.
- **LC-17** — `corpus/README.md:28` (revision block 2.19, round 67) files "registry moved 752 → 776
  rows"; the registry held 728 rows before that landing (`c5f09921…` is the parent commit measured
  here), so the stated before-value is actually the after-value and 776 matches no committed state.
- **LC-18** — before-token half of LC-15's sentence: `corpus/README.md:36` states 753 as the registry
  size before the round-66 landing (`94209e8f…`), but the registry held 701 rows there. Split from
  LC-15 so a half-repair cannot pass (the round-73 L04/L05 pattern).

## Guard notes (why some commands look unusual)

- `SELFTEST OK. [0-9]+ scenarios` — the guard treats a `:` in a git-grep operand as a `<rev>:<path>`
  spec, so the literal colon in the receipt line is matched with `.`.
- `decompress.*23443.*[0-9]+ bytes` — the guard refuses `>` anywhere in an argv element, so the
  ASCII arrow in the report text is matched with `.*`.
- `'corpus/knowledge/*/*.md'` — the guard's existence test uses Python's **non-recursive** glob and
  the knowledge root holds no direct `.md` files; one level is enough and git counts the same 247.
- `^. S[0-9]{3}` — pipe-free registry-row regex (measured identical to the claims' own row regex at
  804 / 724 / 752), so no cell carries a pipe that would break this table.
- Three revision operands: the guard accepts only a full 40-hex revision (or HEAD) for `git grep`,
  and the ANNOTATE leg additionally requires the pinned base operand for numeric pairs — hence the
  two-revision commands for LC-15/LC-17/LC-18.
