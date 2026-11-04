# MutationTester — round 84 (hyaku run 15), wave 1

**Question.** Do the two frozen round-84 counters reject plausible single-predicate
defects in the claim-D and claim-O artifacts, and which predicate is the weakest?

**Answer in one line.** All five assigned mutants are killed (5/5); the copy-cheat
with a self-consistent trace passes the claim-O counter 8/8, and two of the three
one-line counter mutations are caught by no artifact at all.

---

## 1. Method and fixtures

The round's real artifacts do not exist yet — this wave builds them — so every
mutant is a **synthetic stub**: a single commit whose parent is the frozen
claims/counters commit `3ca2cf28`, touching only that claim's own paths (so
`SEPARABLE` is never the leg that fires). Stubs live in a scratch clone of the
lane with fixture identity (`fixture@round84.invalid`) configured in the clone
only; the clone's `refs/heads/main` is moved to the graded lands so the counter's
branch-tip guard is satisfied. The counters themselves are materialised out of the
frozen blob with `git show`, never read from a worktree, and never modified in
place:

```
python3 -B reports/round-84/accept-d84.py --root <clone> --lands <stub> --freeze 3ca2cf28… --work <dir>
python3 -B reports/round-84/accept-o84.py --root <clone> --lands <stub> --freeze 3ca2cf28… --work <dir>
```

The assigned freeze `3ca2cf28` is revision **r0**; the lane's `main` moved twice
while this seat ran (r1 `e160a72e`, r2 `7e6ee2f8`). Every verdict below is recorded
at r0 as assigned; §5.1 measures what the move does to identical lands bytes.

**Positive control (claim D).** A shape-complete stub entry — 17,131 bytes, 10
`## ` sections, 6 decision rows, 20 anchors over 4 distinct ids, 4 appended
registry rows, `- sources:`/`- source:` header fields split so no line carries two
ids — plus the four `S914`–`S917` rows:

```
LEG ENTRY       PASS bytes=17131/16000 missing=none
LEG ANCHORS     PASS bullets=20/20 ids=4/4 malformed=0
LEG LINT        PASS rc=0 findings=0 line='CITED-LINES: 0 finding(s) in 1 file(s)'
LEG ROWS        PASS rows=841 grew=4 floor=4 problems=none
ACCEPT-D-84: PASS legs=10/10
```

Without that control, a fired leg proves nothing: the counter could be failing
everything. The control also shows that the frozen `- sources:` field cannot list
all four new ids on one line — `check-cited-lines.py` reports `MULTI-ID` — so the
header field has to name them indirectly. That is a real constraint on the entry,
not a defect.

**Positive control (claim O)** is the finding itself: a tool that copies
`examples/sound-laws/expected.tsv` and fabricates a 12-line trace reaches
`ACCEPT-O-84: PASS legs=8/8` (§3).

---

## 2. The five assigned mutants — 5/5 killed

| # | mutant | expected | leg line that fires (verbatim) |
|---|---|---|---|
| m1 | every anchor bullet carries two distinct S-ids | LINT or ANCHORS | `LEG ANCHORS     FAIL bullets=0/20 ids=0/4 malformed=20` **and** `LEG LINT        FAIL rc=1 findings=15 line='CITED-LINES: 15 finding(s) in 1 file(s)'` → `ACCEPT-D-84: FAIL legs=8/10` |
| m2 | 19 anchors against the frozen floor of 20 | ANCHORS | `LEG ANCHORS     FAIL bullets=19/20 ids=4/4 malformed=0` → `ACCEPT-D-84: FAIL legs=9/10` |
| m3 | S914 row with `status=queued` | ROWS | `LEG ROWS        FAIL rows=841 grew=4 floor=4 problems=["S914 status='queued'"]` → `ACCEPT-D-84: FAIL legs=9/10` |
| m4 | tool copies the committed `expected.tsv` to `--out` and derives nothing (reports `c=0`, empty trace) | DEMO | `LEG DEMO        FAIL summary=(12,6,0) floors=(12,6,12) trace=0 rules_fired=0/6` → `ACCEPT-O-84: FAIL legs=7/8` |
| m5 | malformed-input path exits 0 and writes an empty out file | NEGATIVE | `LEG NEGATIVE    FAIL cases=3 problems=["missing-rules rc=0 err=''", "bad-json rc=0 err=''", "empty-from rc=0 err=''"]` → `ACCEPT-O-84: FAIL legs=7/8` |

Two notes on m1. It is killed **twice**: `ANCHORS` rejects the line, and the
independent committed tool `tools/check-cited-lines.py` reports 15 `MULTI-ID`
findings. Fifteen rather than twenty because the five bullets already citing
`S917` gained no second *distinct* id from the appended `See also S917.` — the
duplicate-token blind spot that §3 and §4 exploit. Every other leg of m1 passes,
so neither kill is collateral.

m5 is the cleanest single-predicate kill in the set: the stub passes TOOL,
SELFTEST, DEMO, REGISTRY and SEPARABLE, and only the three negative cases fail.

---

## 3. Survival probes and the counter mutations

A kill only means something if the predicate can also be *satisfied*. Three probes
were run beyond the assigned five, then three one-line mutants of the counters
themselves (applied to copies, never to the lane).

### 3.1 The claim-O predicate accepts a copier

| probe | what it is | result |
|---|---|---|
| m4b | copies `expected.tsv` to `--out`, and writes a 12-line trace that names all six rules and has exactly as many lines as the summary it prints | `LEG DEMO        PASS summary=(12,6,12) floors=(12,6,12) trace=12 rules_fired=6/6` → `ACCEPT-O-84: PASS legs=8/8` — **survives**, and derives nothing |
| m4c | copies the *input* to `--out` (identity derivation) with the same fabricated trace | `LEG DEMO        FAIL derived != expected (182 vs 206 bytes)` → killed, **by the byte compare alone** |

`DEMO` therefore reduces to five checks, all of which a copier satisfies:
`rc == 0`; a single `SOUNDLAWS: <w> words / <r> rules / <c> changes` line; the `w`,
`r` and `c` floors, where the tool chooses all three numbers; `out == expected` for
one fixed example whose bytes the tool can read at run time; and a trace whose
line count equals the tool's own reported `c` and which mentions every rule name.
Nothing binds the output to the *rules*: a lookup table keyed on one question
scores 8/8. Trace shape is equally under-bound: the counter accepts any line with
at least three tab-separated fields and reads column 3 as the rule name
(`len(l.split("\t")) >= 3`), so the `min_trace_columns: 5` constant frozen in
revision r2 is read by no leg — a two-column trace plus a rule name would pass.

So `m4c` shows the only barrier to a wrong derivation is the byte compare, and
`m4b` shows the byte compare can be satisfied without deriving.

### 3.2 Duplicate S-id tokens are guarded by exactly one predicate

| probe | what it is | result |
|---|---|---|
| m1b | one anchor bullet repeats the same id: `- S914 S914: …` | `LEG ANCHORS     FAIL bullets=19/20 ids=4/4 malformed=1`, `LEG LINT        PASS rc=0 findings=0` → killed by `ANCHORS` alone |

`check-cited-lines.py` counts `sorted(set(SID.findall(line)))`, so one id written
twice is invisible to it. `ANCHORS` tests `len(found) != 1` on the raw `findall`,
so it sees the duplicate. There is no third guard.

### 3.3 The three counter mutations, one line each

| mutation | effect on the defect it is meant to catch | caught by another artifact? |
|---|---|---|
| **D·ANCHORS accepts two ids**: `if len(found) != 1` → `if len(found) == 0` | m1 (`S914 … S917`, distinct): `ANCHORS` now prints `PASS bullets=20/20`, but `LINT` still fires and the counter still ends `ACCEPT-D-84: FAIL legs=9/10` — the verdict survives, the predicate does not. m1b (`S914 S914`, one distinct id): `ACCEPT-D-84: PASS legs=10/10` — **survives the whole counter** | partly: `tools/check-cited-lines.py` covers the distinct-id shape only, and is structurally blind to the duplicate-token shape |
| **O·DEMO skips the expected-bytes compare**: `if got != want:` → `if False and got != want:` | m4c (identity derivation): `LEG DEMO        PASS summary=(12,6,12) …` → `ACCEPT-O-84: PASS legs=8/8` — **survives** | no |
| **O·REGISTRY ignores the unrowed-tool cap**: `… and unrowed <= block["max_unrowed_tools"]` → `… and True` | a lands with one extra unregistered `tools/stray-tool.py`: `LEG REGISTRY    PASS gate=(0,77,63,0) unrowed=26 floors=(77,63,25)` → `ACCEPT-O-84: PASS legs=8/8` — **survives** | no: `tools/check-gate-registry.py` over the same tree exits **0** and prints `GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead` with `GATE-REGISTRY-INFO: 26 tools without a row`. The INFO line is emitted; nothing asserts on it. |

The DEMO mutation needed one more control, because the counter ships its own
mutation battery (`--junk`). Running that battery on the same lands with the
unmutated and the DEMO-mutated counter gives the identical result both times:

```
JUNK row-dropped      expect REGISTRY   killed=True
JUNK copy-input       expect DEMO       killed=True
JUNK no-trace         expect DEMO       killed=False
JUNK-O-84: FAIL 2/3
```

The battery's `copy-input` kill is triggered by `LEG DEMO FAIL no trace file`, not
by `derived != expected`, so removing the byte compare changes nothing in it. No
committed artifact re-derives `expected.tsv`.

---

## 4. Score and the weakest predicate

| set | killed | survived | score |
|---|---|---|---|
| the five assigned mutants | 5 | 0 | 5/5 (100%) |
| all eight artifact probes (five + m1b, m4b, m4c) | 7 | 1 (m4b) | 7/8 (87.5%) |
| the three counter mutations | 0 | 2 outright (O·DEMO, O·REGISTRY) plus D·ANCHORS for the duplicate-token shape | 0/3 covered |

`D·ANCHORS` is the only mutation with any independent cover, and that cover
(`check-cited-lines.py`) exists only for the distinct-token shape; for the shape
the mutated leg now admits (`S914 S914`) the counter passes 10/10 and nothing
else objects.

Weakest predicates, ranked by how much defect each admits:

1. **`DEMO`** — the claim's substance. A copier with a fabricated trace scores
   8/8; the predicate is a lookup-table test on a single question whose answer the
   tool can read. The trace is graded only for arity against a number the tool
   itself prints.
2. **`ROWS`** — enforces eleven cells **by count** and four **by value** (`cells[0]`
   id, `cells[7] == "mined"`, `cells[8] == "2026-11-04"`, entry path in `cells[10]`).
   The source cell (URL, HTTP status, byte count, sha256, capture), `kind`, `tier`,
   `scope`, `anchor` and `teaches` are never read. The positive control passed
   `ROWS` with `fixture stub row S914: no network fetch was performed` as the
   source cell and `section 1, paragraph 1` as the anchor. The row contract's
   rule for a rejection — `status=rejected` with its reason and flip condition in
   `teaches` — is unread, because the leg only ever compares `cells[7]` to `mined`.
3. **`ANCHORS`** — the sole guard on duplicate S-id tokens (§3.2). Compensated for
   the distinct-id shape by `LINT`, not for the duplicate shape.
4. **`REGISTRY`** — the unrowed cap is asserted only inside this leg; the committed
   auditor reports the number and exits 0.

`FROZENCFG`, `BEFORE`, `ENTRY`, `SECTIONS`, `DECISIONS`, `SOURCED`, `SEPARABLE`,
`TOOL`, `SELFTEST` and `NEGATIVE` were not broken by any probe: the assigned
mutant for each of the last two fired exactly once, and the rest are count or
byte floors with no cheap satisfier in the probe set.

---

## 5. Two instrument hazards found while probing

### 5.1 The freeze moved twice after the wave was dispatched

The lane's `main` now carries `7e6ee2f8` (revision **r2**), on top of `e160a72e`
(revision **r1**). Between them they rewrite three things in
`reports/round-84/claims.json`:

- r1, claim D: `decision_heading` `## 2. The decision table` → `## 2. Six design decisions`
- r1, claim D: `anchors_heading` `## 4. Attested anchors` → `## 3. Attested anchors`
- r2, claim O: `shape_markers` `SOUNDLAW_ERROR:` → `SOUNDLAW_ERROR`, plus two new
  constants no counter line reads (`semantics`, `min_trace_columns: 5`)

The counters read their constants from `--freeze`, so **the same lands bytes grade
differently** (measured on one r1-shaped stub, commit `0c53513f`):

```
--freeze e160a72e : ACCEPT-D-84: PASS legs=10/10
--freeze 3ca2cf28 : LEG FROZENCFG   FAIL freeze 3ca2cf28 lands 0c53513f sha256 ff545df6c108
                    LEG DECISIONS   FAIL no '## 2. The decision table' section
                    LEG ANCHORS     FAIL no '## 4. Attested anchors' section
                    ACCEPT-D-84: FAIL legs=7/10
```

The `FROZENCFG` failure is structural, not a defect in the entry: no lands
descending from `e160a72e` can have `claims.json` byte-equal to `3ca2cf28`'s. So
grading this round at `3ca2cf28` cannot pass at all, and if the entry is written
to the r1 house shape (which other seats are already reading — `counter-revisions.md`
is modified in the worktree) then grading it at `3ca2cf28` also produces two false
section failures.

The r2 marker relaxation does not move any claim-O verdict in this report: both my
stubs and any tool emitting `SOUNDLAW_ERROR: <label>: <detail>` contain the r2
marker `SOUNDLAW_ERROR`, so `TOOL` passes under either spelling. The r2
`min_trace_columns: 5` is the exception — it is frozen but ungraded (§3.1).

The only self-consistent pair is **r1/r2 headings + `--freeze 7e6ee2f8`**. This
seat was dispatched with `3ca2cf28` and the claim text as written against it; the
conflict belongs to the L1 to settle, and it is a one-flag decision, not a target
change. One bookkeeping note: the revision log at `7e6ee2f8`
(`reports/round-84/counter-revisions.md`) documents r0 and r1 and calls r1
"current", so r2 — the effective revision — has no section there yet.

### 5.2 The frozen junk battery's `no-trace` trial is implementation-sensitive

`m_no_trace` in `accept-o84.py` replaces the **first line containing the substring
`trace`** with `    pass  # trace disabled`. The frozen tool contract's own usage
line — `python3 tools/apply-sound-laws.py apply --rules PATH --input PATH --out
PATH [--trace PATH]` — sits in any compliant docstring, so on both my stubs and,
almost certainly, on the real round-84 tool that line is **documentation**:

```
first line containing 'trace': 'python3 tools/apply-sound-laws.py apply --rules PATH --input PATH --out PATH [--trace PATH]'
rewritten file parses: rc=0
JUNK no-trace         expect DEMO       killed=False
JUNK-O-84: FAIL 2/3
```

The rewritten file still parses, the trace is still written, and the trial reports
`killed=False`. This is identical with the unmutated and the DEMO-mutated counter,
so it is not caused by the mutation. Expect `JUNK-O-84: FAIL 2/3` on a correct
artifact unless its first `trace`-bearing line happens to be executable code —
and do not read that FAIL as a land failure without checking which trial failed.

---

## 6. What the L1 should run

1. Fix the freeze first: `--freeze 7e6ee2f8` (r2) for both counters, with the
   entry written to the r1 headings — or restore the two headings to
   `3ca2cf28`'s values and keep `--freeze 3ca2cf28`. The options are mutually
   exclusive; mixing them yields `ACCEPT-D-84: FAIL legs=7/10` on a correct
   artifact.
2. `python3 -B reports/round-84/accept-d84.py --root . --lands <lands> --freeze 7e6ee2f8 --work <dir>` → expect `PASS legs=10/10`.
3. `python3 -B reports/round-84/accept-o84.py --root . --lands <lands> --freeze 7e6ee2f8 --work <dir>` → expect `PASS legs=8/8`.
4. Before believing the DEMO leg, run the check it cannot do: copy
   `examples/sound-laws/rules.json`, change the `to` of one rule (say
   `final-devoicing` `d`→`t` becomes `d`→`s`), and run `apply` into a *different*
   `--out`. A real applier changes the output; a copier does not. That is a
   thirty-second manual probe and it is the only thing in the round that
   distinguishes §3.1's m4b from a tool.
5. Treat `JUNK-O-84: FAIL 2/3` (§5.2) as an instrument defect to record, not a
   reason to repair the tool.

---

## 7. Bounds honoured

- Wrote only `.ufo/waves/round-84/w1/MutationTester.md` and
  `.ufo/waves/round-84/w1/stage/MutationTester/`. Nothing else in the lane, the
  fleet repo, sibling lanes, `.ufo/state/`, `MANIFEST.json` or `.scratch/` was
  touched. `corpus/SOURCES.md` and `SKILL.md` were read through `git show` only;
  `corpus/QUALITY.md` and `considerthese/` were not read at all.
- No commit, push or mutating git/jj command ran in the lane. All fixture commits
  were made in the scratch clone after asserting
  `git -C <clone> rev-parse --show-toplevel` equals the clone; fixture identity
  was configured in that clone only.
- The four frozen blobs re-read after all work hash to the values in
  `stage/MutationTester/integrity.txt`:
  `accept-d84.py` `efee17ff…`, `accept-o84.py` `cbabd31c…`,
  `counterlib.py` `c3707d1a…`, `claims.json` `d8ee0b97…`.
- No absolute scratch path appears in this report or in any receipt: paths are
  repo-relative or `<clone>` / `<dir>` placeholders.
- The seat scratch directory was removed after the receipts were copied; nothing
  was left behind.
