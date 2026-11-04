# ExecBeforeState — red-before receipts for round-84 claims D and O

Wave `kotodama-r84-v1` (12 seats), milestone `r84-v1`. Role: measure, read-only.

**Verdict: both claims are red before, with the numbers the counters grade.** Every base
number was read from the base tree `81499ee4`; no base number is taken from the working
tree. The two frozen `BEFORE` legs are green when recomputed with the counters' own
helpers, which is exactly what a red-before receipt must show: the world before the
claim artifacts is the world the counters expect.

Full receipts: `.ufo/waves/round-84/w1/stage/ExecBeforeState/before.md` (55 KB, every
command, raw output and exit code) and `.../before.json` (numbers). Per-entry stdout /
stderr / rc and the normalised command index: `.../receipts/`.

## Revision pins and measurement window

| pin | value | evidence |
|---|---|---|
| base | `81499ee45b5751d388fefc78583810878de01ecd` | `P3` |
| freeze named by the dispatch | `3ca2cf288fb593618e0559ea86a36e2dd3110eb8` (r0) | `P4` |
| freeze r1 (pre-dispatch) | `e160a72e4adf1620e09f812b913d4ece0fcd5243` | `P5b` |
| freeze r2 = lane tip | `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` | `P5c`, `P0`, `P0d` |
| measured | 2026-11-04T13:34:49Z → 13:34:51Z | `P0b`, `P0e` |
| base is an ancestor of the tip | rc 0 | `P6` |
| base..HEAD diff under `tools`/`examples`/`SKILL.md` | empty | `P8`, `P9` |

The lane tip moved from r0 to r2 **before** this seat ran (`X17`, both commits marked
pre-dispatch). All base numbers below are invariant to that movement.

## Claim D — red before (depth)

| quantity | measured | expected | verdict |
|---|---|---|---|
| `.md` files under `corpus/knowledge` at base | 257 | 257 | MATCH |
| non-`.md` files under `corpus/knowledge` at base | 0 | — | — |
| partitions (civilizations / culture-material / linguistics / myth-symbol / synthesis / verification) | 95 / 42 / 32 / 35 / 29 / 24 | sums to 257 | MATCH |
| registry rows, seat grammar `^ {0,3}\| *S[0-9]{3,}` | 837 | 837 | MATCH |
| registry rows, counter `ROW_LINE` (accept-d84.py:39) | 837 | 837 | MATCH |
| registry rows via the counter's own `registry_rows()` | 837, 0 malformed, 11-cell every row | 837 | MATCH |
| registry `\|`-start lines | 839 (= 837 + header + separator) | — | — |
| registry id range | `S001` … `S913`, 0 duplicate ids, 0 ids ≥ `S914` | S913 last | MATCH |
| `S913` row cell count | 11 | 11-cell row contract | MATCH |
| filename sweep `witch\|witches\|witchcraft\|sorcer\|sorcery\|malefic` | 0 owning basenames | 0 | MATCH |
| matter-of-subject `^- topic:` scan | 0 files | 0 | MATCH |
| word-boundary occurrence census | **19 lines across 11 files** | prose says 19 / 10 | 19 MATCH, files DIVERGE (F2) |
| `- gap filled:` lines naming the surface | **1 raw line, 0 ownership claims** | brief says 0 | DIVERGE as instrument (F1) |
| entry path at base | absent (`git cat-file` rc 128); absent in worktree | absent | MATCH |
| myth-symbol sibling files | 35 | — | — |
| rows `S914` / `S915` / `S916` / `S917` | 0 / 0 / 0 / 0 (combined 0) | 0 | MATCH |

The four sweeps from ScoutGapWitch's brief were re-run independently and are printed raw
in `before.md` §3 (`D3a`-`D3i`); §4 repeats them in the brief's literal working-tree form
(`W1`-`W4`) and the two agree byte for byte. Positive controls: 257 files carry `^- topic:`;
60 files carry `^- gap filled:`; the unanchored pattern matches 148 files across
`corpus` + `reports`, so the zero in `corpus/knowledge` is not a dead instrument (`D3j`,
`D3k`, `D3l`).

The single `- gap filled:` hit is
`corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4`: its subject is
protective objects and it quotes `witch mark` inside a sweep ledger that reports the term
occurs in 0 files. A word-boundary variant still matches it (`V6`, `V7`), so this is a
reading of the line, not a stricter regex.

## Claim O — red before (operability)

| quantity | measured | expected | verdict |
|---|---|---|---|
| `git ls-tree … tools examples \| grep -ciE 'sound.?law\|soundchange'` | 0 | 0 | MATCH |
| `git grep -c SOUNDLAWS <base> -- tools examples reports` | 0 lines (empty stdout, rc 1) | 0 | MATCH |
| `SOUNDLAWS` blobs under `tools`+`examples` at base | 0 | 0 | MATCH |
| `SOUNDLAW_ERROR` at base | absent | — | — |
| `examples/sound-laws` at base | absent (`cat-file` rc 128); 0 files | absent | MATCH |
| `examples/` at base | 68 files in 6 top-level entries | — | — |
| neighbouring checker `tools/check-craft-exercise.py` | present (rc 0) | present | — |
| gate registry at **base** | `0 missing / 74 registered / 61 instruments / 0 dead`; `25 tools without a row`; rc 0 | same | MATCH |
| gate registry at **lane tip** | `2 missing / 74 registered / 63 instruments / 0 dead`; `25 tools without a row`; rc 1 | not stated | DIVERGE from the claim's base sentence (F3) |

Tip `MISSING` lines are exactly `reports/round-84/accept-d84.py` and
`reports/round-84/accept-o84.py`. The tip reading was taken twice: from committed bytes
materialised into a scratch tree (`O4a`) and from the live worktree (`O4b`); the two are
byte-identical (`gate_worktree_equals_materialised_tip`). Context at base: 61
`reports/round-*/accept-*.py` instruments, 30 top-level `tools/*.py`, 246 registry table
lines, 0 files under `reports/round-84/`.

Content-level context (not part of the frozen `BEFORE` leg): at base 10 tool files and 11
example files mention sound laws in phonology prose (`O1g`, `O1h`, `O1i`), and 54 report
files mention them. The claim's sentence is about *name* hits and about a tool that
*applies* rules; both hold. The marker `SOUNDLAWS` exists only at the freeze, in the two
round-84 report files (`O2b`, `O2c`).

## The frozen `BEFORE` legs, recomputed with the counters' own code

`B1` imports `reports/round-84/accept-d84.py` at the tip and replays its `before()` body
(lines 106-127) against the base tree; `D2c` calls the counter's `knowledge_files()` and
`registry_rows()` rather than a reimplementation. Results:

- `D_BEFORE_OK=True` — `entry_at_base=False files=257/257 rows=837/837 owned=none`
- `O_BEFORE_OK=True` — `tool_at_base=False example_files=0 marker_files=0`

Both legs are green before any claim artifact exists; every claim leg is still red. That
is the state the round's counters were frozen to expect.

## Calibration findings the wave needs

Full text with citations is `before.md` §12 (F1-F6); `before.json` carries them as
`findings`. Short form:

1. **F1 (D).** The scout brief's literal `- gap filled:` test returns 1 at base, not 0.
   The frozen claim's wording ("no `- gap filled:` owner for the surface") survives;
   the brief's command-level `= 0` does not. Do not gate on the literal regex.
2. **F2 (D).** Word census is 19 lines over **11** files; the frozen prose says 10. The
   counter does not grade the file count. Do not quote 10 as measured.
3. **F3 (O).** The claim's registry sentence is a **base** reading. At the tip the same
   auditor reads `2 missing / 74 registered / 63 instruments / 0 dead`: the instrument
   floor (`i >= 63`) is already met, and the remaining deficit is the two rows plus
   registered `74 → >= 77`. A seat expecting 61 instruments at the tip will measure 63.
4. **F4 (O).** The counter runs `["--selftest"]` (accept-o84.py:117) and requires the
   literal `--selftest` in the tool's bytes (`shape_markers`, `X6`); the frozen tool
   contract's canonical spelling is `selftest`, and the bench spec writes
   "`--selftest` (alias `selftest`)". A tool implementing only `selftest` fails
   `SELFTEST` and `TOOL`. Support both, keep the literal in the source.
5. **F5 (D+O).** The dispatch names freeze r0, but the lane tip is r2. Two graded claim-D
   constants moved between them — `decision_heading` `## 2. The decision table` →
   `## 2. Six design decisions`, `anchors_heading` `## 4. Attested anchors` →
   `## 3. Attested anchors` — and claim O's marker lost its colon. The seat specs match
   the tip; the wave context's claim text matches r0. Entries written to one heading pair
   fail `DECISIONS`/`ANCHORS` under the other freeze. `FROZENCFG` also requires the lands
   `claims.json` to be byte-identical to the freeze's.
6. **F6 (D+O).** `SEPARABLE` forces **all of claim O's bytes to land strictly before
   claim D's first commit** (`claim_span` parent plus the `blob_sha(parent) ==
   blob_sha(lands)` foreign-path test; `counterlib.py:138-156`,
   `accept-d84.py:216`, `accept-o84.py:209`). D first, or one combined commit, fails
   D's `SEPARABLE` (and a combined commit fails O's too).

## Evidence and receipts

- `.ufo/waves/round-84/w1/stage/ExecBeforeState/before.md` — 120 measurement entries,
  each with the normalised command, raw stdout, stderr and exit code.
- `.ufo/waves/round-84/w1/stage/ExecBeforeState/before.json` — the same numbers,
  expectations, verdicts and findings.
- `.../receipts/index.tsv` + `<id>.stdout` / `<id>.stderr` / `<id>.rc` — raw receipts.
- `.../receipts/repro-check.txt` — replay rule and result: the committed method
  reproduces **111 of 120** entries byte-for-byte; the nine exclusions are the entries
  that read the clock, the lane HEAD or the live worktree.
- `.../method/` — normalised drivers and helpers, pinned to the measured tip.

No absolute scratch path is cited in any committed file; replay commands use `${STAGE:?}`
and `${LANE:?}`.

## Files changed

Only this report and `stage/ExecBeforeState/` (`before.md`, `before.json`, `receipts/`,
`method/`). No git or jj mutation; no commit, push, or branch move. No lane file outside
the stage directory was written.

Tooling: nothing was installed, upgraded or run through a package manager; all
measurement used the host's existing `git`, `grep`, `find`, `coreutils` and `python3`
(stdlib only). No pacman transaction was attempted.

## Risks

- **Freeze in flux.** The freeze advanced twice during dispatch. If a grader is handed
  r0 while the seats were built from r2, claim D's heading legs fail on a correct entry.
  The landing commit must name one hex and use that revision's `claims.json`.
- **Landing order.** F6 is a hard constraint; it is not visible from either claim's
  prose, only from the counter code.
- **Point-in-time gate reading.** `O4a`/`O4b` are a snapshot of `7e6ee2f8`. Concurrent
  seats write only under `.ufo/…/stage/`, and the graded surfaces were unchanged from
  base at measurement: `tools`, `examples` and `SKILL.md` are byte-identical (`P8`,
  `P9`), and so are `corpus/knowledge` and `corpus/SOURCES.md` (`D1d`, `D2d`). `P1b`
  records the exact dirt seen — the L1's in-flight `counter-revisions.md`, `telemetry/`,
  and an untracked `corpus/lessons/round-84.md` outside the graded surfaces.
- **The 1 gap-filled line** will be rediscovered by anyone re-running the brief's literal
  command; the report and `before.md` F1 give the reading so it is not mistaken for an
  owner.

## Blockers

None. The seat's scratch directory (outside the repository) was created for the
measurement and removed after the receipts were copied into
`.ufo/waves/round-84/w1/stage/ExecBeforeState/`; nothing was left behind.
