# SKILL.md §Gates and probes — final round-74 rows, round-73 correction note, and the LC-09/LC-10 edit

Post-wave rewrite for round 74 (seat ScribeSkillGates). **SKILL.md is not edited by this seat.**
The canonical writer (L1) applies the three appended rows and the one in-place line below.

- Base: `f7104cbce186bc2e1522abf0cfd619cc834628bb` (lane HEAD at every measurement; `claims.json` `.base`).
- Frozen claims read: `reports/round-74/claims.json` (status FINAL), 13 C legs and 11 Ca legs.
- Counter builds read: `.ufo/waves/round-74/counters/accept-c.py` (read at sha256 `0b63cdc61379…` and
  again at `b5bfb98b89…`, 22:19:51 — the file was being written throughout this seat's window; its
  self-stamped selftest run below is `b038f345…`) and `accept-ca.py` (selftest measured at
  `76d00b88325f…`, later bytes `2ddebefcb1de…`). Both are L1-installable sources;
  `reports/round-74/accept-{c,ca}.py` did not exist at this seat's read.
- Receipts: `reports/round-74/telemetry/` (at this read it holds only `census-start.txt`; every receipt named below is filed at freeze).

Final literal fractions: **C `legs=13/13`**, **Ca `legs=11/11`**. No `<legs>` placeholder appears in any row below.

## 1. Anchor (unchanged at base)

| probe | command | result |
|---|---|---|
| section heading | `grep -n 'Gates and probes' SKILL.md` | `619:## Gates and probes` |
| header row (8 columns) | `git show f7104cbc…:SKILL.md \| grep -n '^\| name \| kind \|'` | line `648` |
| last registry row | `git show f7104cbc…:SKILL.md \| sed -n '704p'` | `accept-ca-73` |
| registry rows at base | `git show f7104cbc…:SKILL.md \| grep -c '^\| accept-'` | `43` |
| counter files at base | `git ls-tree -r --name-only f7104cbc… reports \| grep -c 'accept-.*\.py$'` | `43` |

Insert all three rows **after line 704 and before the blank line 705**; line 706 starts
"The contrastive checker is example-specific…". Column shape is the last row's:
`name | kind | entry command | verdict map | self-test | pinned values | write scope | owner`.
Every row below carries exactly those 8 cells and no `|` inside a cell.

## 2. Rows to append (verbatim)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| accept-c-74 | gate | `python3 -B reports/round-74/accept-c.py --root . --lands <40-hex> --freeze <40-hex>` | Output ends `ACCEPT-C-74: PASS legs=13/13` (exit 0) or `: FAIL legs=<n>/13` (exit 1, n = passing legs). A refused run prints `ACCEPT-C-74: FAIL legs=0/13 (refused: …)` and exits 2: missing, malformed or tree-absent `--lands` or `--freeze`; `--root` without `.git`; `lands` equal to the frozen base; unreadable frozen `claims.json`; a frozen `legs[]` list that is not exactly the thirteen implemented legs (LEGCOUNT); or a materialization failure. `lands == freeze` is graded, not refused: the data legs (ENTRIES, ROWS, GATE, EVIDENCE, REJECTS, INDEX) must read red with FROZENCFG green, exit 1. | `python3 -B reports/round-74/accept-c.py --selftest` — mktemp fixture repos asserting a clean `PASS legs=13/13`, the no-data `FAIL` with ENTRIES and ROWS red and FROZENCFG green, the `lands == base` refusal, the graded `lands == freeze` control and a twelve-leg LEGCOUNT refusal; receipt `reports/round-74/telemetry/selftest-c.txt`. | base `f7104cb…`; constants read by `git show <freeze>:reports/round-74/claims.json` — adopted rows S881..S884 (staged S883/S884/S899/S900), reused row S877, both culture-material entry paths, the by-document map path with its sha256, the gap-sweep fragments and CJK terms, the access date | read-only; all graded bytes come from a temp clone checked out at `--lands` plus a `git archive` of the base, and the counter's own constants from `<freeze>`; the worktree is disclosed only; selftest fixtures live in mktemp dirs | kotodama-shokunin |
| accept-ca-74 | gate | `python3 -B reports/round-74/accept-ca.py --root . --lands <40-hex> --freeze <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` | Output ends `ACCEPT-CA-74: PASS legs=11/11` (exit 0) or `: FAIL legs=<n>/11` (exit 1). Refusals print `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: …)` and exit 2: missing or malformed `--lands` or `--freeze`; missing or non-directory `--fleet-root`; an absent revision; `lands` equal to the frozen base; an unreadable frozen `ledger.json` or `claims.json`; or a frozen leg table that is not exactly the eleven implemented legs (LEGCOUNT). `--main` defaults to `main` and is consumed only by STAMP. | `python3 -B reports/round-74/accept-ca.py --selftest` — measured at counter sha256 `76d00b88325f…`: exit 0, `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`; receipt `reports/round-74/telemetry/selftest-ca.txt` | base `f7104cb…`; freeze-read `claims.json` and `ledger.json`; the ten allowlisted observe executables; `min-pairs`; the fleet pin and report blob; the six inherited round-73 w2 must-track sha256s; the round-73 counters' sha256 `95aee881…` and `222d4dd6…` and the two PASS-at-lands receipts | read-only; clones at `--lands` and at base, a further clone at the round-73 lands for RECEIPTS, temp dirs removed on exit; no worktree byte is graded | kotodama-shokunin |
| accept-c-73 / accept-ca-73 correction | note | — | Base rows stand; three corrections to how they are run and read. (1) `accept-ca-73`'s selftest prints `SELFTEST OK: 10 scenarios` only at counter r3 (sha256 `222d4dd6d408…`, receipt `reports/round-73/telemetry/selftest-r3.txt`); the bytes at the round-73 freeze (sha256 `f8ebb5d8…`, `selftest.txt`) print 9, and r3's `ERROR: base 8841ad3b… is not a commit` stderr line is the expected frozen-base-absent control output, not a failure. (2) `accept-c-73` reaches `PASS legs=11/11` at its lands only when the census script is named: `--fleet-root /home/vgpnk/Projects/shokunin` (measured, `ExecReceiptRerun73.md` §2) or `--census-sh <path>` (same code branch, unmeasured); the flagless form reads `FAIL legs=10/11` (CENSUS). (3) `accept-ca-73` reaches `PASS legs=9/9` at its lands only with `--main 2d1cd9140d3a6c42296d71e4f29587582a4a88c0`; the documented form reads `FAIL legs=8/9` (STAMP) because lane `main` is `f7104cb…`. | — | receipts `reports/round-73/telemetry/selftest-r3.txt`, `.ufo/waves/round-74/w1/receipts/measures-c73-at-lands.txt`, `.ufo/waves/round-74/w1/receipts/measures-ca73-at-lands.txt` | appended note only; no existing byte changed | kotodama-shokunin |

Why the third row is `kind = note`: the round-70 claim-O invariant counts only rows whose kind is
`gate` or `probe` and whose command names an `accept-*.py` (`grep -cE '^\| [^|]+ \| (gate|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py'`).
A `note` row leaves that count at `43 + 2 = 45`, equal to the counter-file count at lands
(`43 + reports/round-74/accept-c.py + accept-ca.py`). A `gate` row with no counter of its own would
break the equality.

## 3. Exact in-place edit for LC-09 / LC-10 (SKILL.md:594)

`ledger-final.json` keeps both pairs as **REPAIR** with `stated_at: SKILL.md:594`:

| pair | stated token at base | observed at base | expected_after |
|---|---|---|---|
| LC-09 | `94 entries` | `95` (`95 files changed, 18546 insertions(+)`) | `95` |
| LC-10 | `92 earlier-civilization` | `93` (`93 files changed, 18198 insertions(+)`) | `93` |

Both pairs name the same line, so one edit satisfies both.

Old bytes (line 594 at base, verbatim; the sentence continues on line 595):

```
- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
```

New bytes:

```
- `corpus/knowledge/civilizations/` — 95 entries: 93 earlier-civilization
```

Line 595 (`  bases plus two source maps (…`) is unchanged, so the sentence still reads
"95 entries: 93 earlier-civilization bases plus two source maps" — consistent with 95 files of
which 2 are `*primary-sources.md`.

Authorization: SKILL.md is not in Ca's protected set, and the APPENDONLY leg permits a non-append
change to a file only on the lines a REPAIR pair's `stated_at` names (`accept-ca.py:1303`
`leg_appendonly` at this read, `-U0` hunks, lines collected in `repair_lines`). SKILL.md:594 is exactly such a line. Nothing else in SKILL.md
may be changed in place this round: the round-73 rows at lines 703–704 are **not** named by any
ledger pair (`ledger-final.json` has 13 pairs, only `LC-09`/`LC-10` at `SKILL.md:594`), so the
round-73 corrections are delivered as the appended `note` row above, not as cell edits.

Verification commands (read-only):

```
git show f7104cbce186bc2e1522abf0cfd619cc834628bb:SKILL.md | grep -n '94 entries\|92 earlier-civilization'
  -> 594:- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization   (one hit)
git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/civilizations/*.md'
  -> 95 files changed, 18546 insertions(+)
git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/civilizations/*.md' ':(exclude)*primary-sources.md'
  -> 93 files changed, 18198 insertions(+)
```

The two adopted entries are `corpus/knowledge/culture-material/worldbuilding-setting-practice{,.amend-2026-10-23}.md`,
so no civilization file is added this round and the repaired `95 / 93` stays true at lands.

## 4. The two controls, with the literals this build prints

| control | command shape | printed verdict | exit |
|---|---|---|---|
| C lands == freeze (nothing landed after the freeze) | `--lands <freeze> --freeze <same>` | intended: `ACCEPT-C-74: FAIL legs=<n>/13` with ENTRIES, ROWS, GATE, EVIDENCE, REJECTS and INDEX red and FROZENCFG green. **Measured red at counter sha256 `b038f345…`: the counter prints `ACCEPT-C-74: PASS legs=13/13` and exits 0** (see §5 item 2) | 1 intended / 0 measured |
| lands == frozen base | `--lands <frozen base> --freeze <later commit>` | `ACCEPT-C-74: FAIL legs=0/13 (refused: lands <base> is the frozen claim base <base> (the do-nothing control: no data landed))` | 2 |
| Ca lands == freeze (no landed data) | `--lands <freeze> --freeze <freeze>` (graded, not refused) | `ACCEPT-CA-74: FAIL legs=<n>/11` with REPAIR, ANNOTATE and RECEIPTS red and FROZENCFG/LEDGER green | 1 |
| Ca lands == frozen base | `--lands <frozen base> --freeze <later>` | `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base <base>)` | 2 |

The frozen C control sentence is "lands == `<freeze>` FAILS with ENTRIES, ROWS, GATE, EVIDENCE,
REJECTS, INDEX red and FROZENCFG green". The current build grades that pair (its main no longer
refuses a non-strict ancestor; only the `--freeze` help text still says "strict ancestor") and its
selftest asserts the graded shape (`freeze-eq-lands`, `accept-c.py:2902`). At the tested build the
assertion is red: the counter PASSes at `lands == freeze`, so the do-nothing shape is currently
vacuously green — the one thing the control exists to catch. The Ca counter grades `lands == freeze`
too and refuses only when `freeze == lands` **and** every leg is green (`accept-ca.py`, the guard
before the PASS print), so a green `lands == freeze` run there is refused.

## 5. Build-state items to close before freeze (measured, not inferred)

1. **`map.sha256` is a placeholder in the frozen claims.** `reports/round-74/claims.json`
   `claims[id=C].map.sha256` reads `FILLED-AT-FREEZE`. FROZENCFG recomputes `git show
   <freeze>:<map.path>` and compares it to that constant, so the leg cannot pass and the
   `# frozen map:` header prints the placeholder. It must be filled in the freeze commit, together
   with the claims byte hash the counter prints.
2. **The C selftest is red: the do-nothing shape passes.** Run with `TMPDIR=/tmp/scg74` on the build
   whose self-stamp reads sha256 `b038f345…` (the file kept changing during the run; it ended at
   `b5bfb98b…`, 22:19:51): `SELFTEST: 68/69 scenarios`, sole failure
   `lands==freeze: expected graded FAIL exit 1, got 0` — the counter printed
   `ACCEPT-C-74: PASS legs=13/13` on a tree with no landed entry, so the control the claim names is
   currently green when it must be red. The clean scenario in the same run did print
   `ACCEPT-C-74: PASS legs=13/13` with `# frozen legs: 13 (ENTRIES,…,FROZENCFG,INDEX)` and
   `# frozen map: … sha256=6ba19017…`, so the leg roster and LEGCOUNT path are live. The structure
   the rows state is settled: `LEGS` has the 13 entries ending `INDEX` (`leg_index` grades
   `corpus/README.md`), a frozen-leg mismatch is a refusal (exit 2), and the refusal prints
   `legs=0/13` from `len(LEGS)`. Reconcile before freeze and file `selftest-c.txt` from the final
   bytes.
3. **The Ca counter changed after its measured selftest.** The run above (`138 checks across 37
   scenarios`) was on sha256 `76d00b88325f…`; the current bytes are `2ddebefcb1de…`. Re-run the
   selftest at freeze and file `selftest-ca.txt` from those bytes if they differ.
4. **Receipt inventory at this read:** `reports/round-74/telemetry/` holds only `census-start.txt`.
   The rows cite the six receipts the claim names (`selftest-c.txt`, `controls-c.txt`, `junk-c.txt`,
   `selftest-ca.txt`, `controls-ca.txt`, `junk-ca.txt`) and the two PASS-at-lands files
   (`accept-c-73-at-lands.txt`, `accept-ca-73-at-lands.txt`); all are filed at freeze.

## 6. Measured runs (read-only; /tmp scratch only)

| command | exit | output |
|---|---|---|
| `python3 -B accept-ca.py --selftest` (sha `76d00b88…`) | 0 | `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0: do-nothing, clean, lands-eq-base, legcount, …` (expected `ERROR:` lines from the CLI scenarios precede it) |
| `python3 -B accept-c.py --selftest` (self-stamp `b038f345…`; file ended `b5bfb98b…`) | 1 | `SELFTEST: 68/69 scenarios`; failure `lands==freeze: expected graded FAIL exit 1, got 0` (the counter printed `ACCEPT-C-74: PASS legs=13/13` at that tree) |
| `python3 -c 'ast.parse(open("accept-ca.py").read())'` | 0 | parses at sha `2ddebefc…` |
| `git show f7104cbc…:SKILL.md \| grep -n '94 entries\|92 earlier-civilization'` | 0 | single hit at line 594 |
| `git diff --shortstat <empty-tree> f7104cbc… -- 'corpus/knowledge/civilizations/*.md'` | 0 | `95 files changed, 18546 insertions(+)` |
| same with `:(exclude)*primary-sources.md` | 0 | `93 files changed, 18198 insertions(+)` |

Nothing was written inside the lane by these runs; the `TMPDIR=/tmp/scg74` fixtures were this
seat's own and were removed at close.

## 7. Out of scope / not done

- SKILL.md not edited, no anchor line touched, no ledger/claims/counter written.
- The C selftest was not run (build incomplete at read); the row's self-test cell cites the code's
  assertions and the freeze-time receipt path, and §5 item 2 states the measurement gap.
- No full data run of either round-74 counter (they need a landed tree and a freeze commit).
- No installs (pacman paused host-wide; nothing needed), no network fetch, so no User-Agent record.
