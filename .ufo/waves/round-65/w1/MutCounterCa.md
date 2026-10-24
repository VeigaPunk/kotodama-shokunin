# MutCounterCa — round-65 mutant probe on `reports/round-65/accept-ca.py` (claim Ca)

Seat: attack, counter/records. Target: the frozen Ca instrument, revision 1,
`reports/round-65/accept-ca.py` (9 legs: R1 R2 R3 R4 R5 R6 R7 CRITERION QUOTES).
Lane tip read at `17c32302c6845c8f164b985a8cb312d3181c8788`; `git status` at start
and end shows the same three untracked entries (`.ufo/waves/round-65/`,
`reports/round-65/`, `tools/check-row-fragments.py`) and no tracked-file change.

Frozen bytes: `e9a13ebbde7ce0f727b6ff8c55dd0ee8e9d9a0672d62849413fbca72312cf215`
before the probe and after it. **No restore was needed: the frozen instrument was
never edited**; all five mutants are copies under
`.ufo/waves/round-65/stage/mut-ca/`, and every run used `python3 -B`.

## What I attacked

The five loosened detectors named in the ticket. Each is a single textual
replacement in a copy of the pristine instrument, asserted to occur exactly once
in the source before substitution (`run-mut-ca.py` builds them that way, so a
stray second match aborts the build rather than silently mutating a second site).

| mutant | pristine line | edit |
|---|---|---|
| m1-r1-tree-any-hex | 109 | `rf"^tree: {re.escape(tree)}$"` → `r"^tree: [0-9a-f]{40}$"` (the `git rev-parse 8bab271c^{tree}` value is still computed and printed, but no longer compared) |
| m2-r2-append-only-dropped | 128 | `leg("R2", r2_original_intact and r2_named, …)` → `leg("R2", r2_named, …)` (the `git show 17c32302:…/revisions.txt` prefix test still runs, but is not required) |
| m3-r7-skeleton-anywhere | 163 | `not re.search(r"skeleton\|await L1", verified_at, …)` → `not re.search(r"skeleton", entry, …)` (whole-file scope, and the `await L1` token dropped) |
| m4-quotes-other-lesson | 72 | `R65_LESSON = "corpus/lessons/round-65.md"` → `"corpus/lessons/round-64.md"` |
| m5-criterion-17-substring | 168-169 | `re.search(r"^1[7-9]\.\s", quality, re.M) and re.search(r"tree hash", quality)` → `re.search(r"17\.", quality)` |

Mutant sha256 (full list in `stage/mut-ca/results.json`):

```
m1-r1-tree-any-hex          6d7618a22484b08381dbeb88f5a7cfe312fafc6126653fa96f09a6ef08b670b3
m2-r2-append-only-dropped   6d4597caa3eb68a60b568e6bb9af38158928481f9b3b6514e21a01131a683595
m3-r7-skeleton-anywhere     418ee9fa7f1e2121cdd2391216c79fe62d316b1e7d5a5bdcec11018e3a1e7471
m4-quotes-other-lesson      b2225c9e7a6c3b7123b3d0d8a7adac8aad79be2c71968af2798f054dc5be7a5e
m5-criterion-17-substring   bb557dd35cbba3392a7c946c058410dc4da183fa4b56146c97adba12fc871dca
pristine (copy of frozen)   e9a13ebbde7ce0f727b6ff8c55dd0ee8e9d9a0672d62849413fbca72312cf215
```

## Detector batteries

1. **Base-bytes conformance** (the committed receipt as oracle). Root = the lane
   root, whose tracked bytes *are* the base revision. Expected leg lines are read
   from `reports/round-65/telemetry/dry-run-ca.txt`. A mutant is killed by that
   receipt if any leg status or detail differs.
2. **False-green admission** (the property test). Six synthetic roots under
   `stage/mut-ca/`: `fixture-green`, where every one of the nine legs is genuinely
   satisfied, plus five variants that are identical except for the single defect
   the corresponding mutant stops checking. Each root is inside the lane repo, so
   the instrument's own `git rev-parse` / `git show 17c32302:…` calls resolve
   against real history, and `tools/check-gate-quotes.py` is the real committed
   tool (copied into each root).

A pre-data baseline failure is not a kill: at base every leg fails by design
(`dry-run-ca.txt` line 1 says "expect FAIL on all legs"), and the pristine
instrument reproduces that receipt line-for-line. So battery 1 can only kill a
mutant that changes behaviour on base bytes; the kill for a loosening that keeps
the base FAIL has to come from battery 2.

`fixture-green` under the **pristine** instrument (all nine PASS, exit 0):

```
R1 PASS restamp=True tree=0ec0e50ea828ca6d8e20298f72af49414692e9e4 repeats_log_score_lessonfinal=True
R2 PASS original_intact=True named=True
R3 PASS log_names_actual_and_wrong=True
R4 PASS honest_wording_patch=True
R5 PASS in_control=True in_log=True
R6 PASS status_correction=True
R7 PASS line='- verified-at: 2026-10-24 - corrected this round; citation check passed.'
CRITERION PASS criterion_with_tree_hash=True
QUOTES PASS exit=0 out=['GATE_QUOTES: 0 findings']
ACCEPT-CA-65: PASS
```

## Result table

| mutant | expectation that dies | false green admitted (fixture) | pristine on that fixture | mutant on that fixture | killed by committed receipt? | verdict |
|---|---|---|---|---|---|---|
| m1-r1-tree-any-hex | receipt tree hash equals the tree of the re-stamped revision (`0ec0e50e…`) | `fixture-d1-wrong-tree`: `tree: 1111111111111111111111111111111111111111` | `R1 FAIL restamp=False tree=0ec0e50e… repeats…=True` → exit 1 | `R1 PASS restamp=True tree=0ec0e50e…` → **ACCEPT-CA-65: PASS**, exit 0 | **NO.** base run byte-identical to `dry-run-ca.txt` (R1 line 4 unchanged) | **SURVIVED** (coverage finding) |
| m2-r2-append-only-dropped | filed record append-only: `revisions.txt` still starts with its `17c32302` bytes | `fixture-d2-append-only-violated`: the file replaced by one correction line | `R2 FAIL original_intact=False named=True` → exit 1 | `R2 PASS original_intact=False named=True` → **PASS**, exit 0 | **NO.** base R2 detail identical (line 5) | **SURVIVED** (coverage finding) |
| m3-r7-skeleton-anywhere | verified-at line carries no stale placeholder (`skeleton` **or** `await L1`) | `fixture-d3-stale-await-L1`: line reads "structure prepared; cited source claims await L1 insertion and review" and the word `skeleton` is gone from the file | `R7 FAIL line='- verified-at: 2026-10-23 - structure prepared; cited source claims await L1 insertion…'` → exit 1 | `R7 PASS line='- verified-at: 2026-10-23 - structure prepared; cited source claims await L1 insertion…'` → **PASS**, exit 0 | **NO.** base R7 line identical (line 10) | **SURVIVED** (coverage finding) |
| m4-quotes-other-lesson | the round-65 lesson's Gate rows are the checked subject | `fixture-d4-long-quote-r65`: a 30-word Gate quotation in `corpus/lessons/round-65.md` | `QUOTES FAIL exit=1 out=['GATE_QUOTES: 1 findings']` → exit 1 | `QUOTES PASS exit=0 out=['GATE_QUOTES: 0 findings']` → **PASS**, exit 0 | **YES — `reports/round-65/telemetry/dry-run-ca.txt` line 12**: receipt `QUOTES FAIL exit=2 out=['GATE_QUOTES: 0 findings']`, mutant prints `QUOTES PASS exit=0 out=['GATE_QUOTES: 0 findings']` (base has no round-65 lesson; the mutant reads the clean round-64 lesson and turns the leg green) | **KILLED** |
| m5-criterion-17-substring | a numbered criterion 17 exists **and** QUALITY carries the tree-hash rule | `fixture-d5-no-criterion-17`: "…listed in section 17.2 of the round-64 spot-check; no criterion row is added and no tree hash is required." | `CRITERION FAIL criterion_with_tree_hash=False` → exit 1 | `CRITERION PASS criterion_with_tree_hash=True` → **PASS**, exit 0 | **NO.** base CRITERION line identical (line 11) | **SURVIVED** (coverage finding) |

Mutant outputs on their own defect fixture, in full (all nine legs PASS, the
target leg included — these are the false greens, verbatim):

```
m1  R1 PASS restamp=True tree=0ec0e50ea828ca6d8e20298f72af49414692e9e4 …   ACCEPT-CA-65: PASS
m2  R2 PASS original_intact=False named=True                                 ACCEPT-CA-65: PASS
m3  R7 PASS line='- verified-at: 2026-10-23 - structure prepared; cited source claims await L1 insertion and'   ACCEPT-CA-65: PASS
m4  QUOTES PASS exit=0 out=['GATE_QUOTES: 0 findings']                        ACCEPT-CA-65: PASS
m5  CRITERION PASS criterion_with_tree_hash=True                              ACCEPT-CA-65: PASS
```

## Exclusivity matrix (rows = instrument, cols = root)

```
                             green   d1-tree  d2-append  d3-r7  d4-quotes  d5-crit
m1-r1-tree-any-hex           PASS    PASS     FAIL       FAIL   FAIL       FAIL
m2-r2-append-only-dropped    PASS    FAIL     PASS       FAIL   FAIL       FAIL
m3-r7-skeleton-anywhere      PASS    FAIL     FAIL       PASS   FAIL       FAIL
m4-quotes-other-lesson       PASS    FAIL     FAIL       FAIL   PASS       FAIL
m5-criterion-17-substring    PASS    FAIL     FAIL       FAIL   FAIL       PASS
pristine                     PASS    FAIL     FAIL       FAIL   FAIL       FAIL
```

Each mutant is green only on `fixture-green` and on its own defect root; no
mutant masks a second defect. That makes each cell a clean single-point result
rather than a compound loosening.

## Base-bytes conformance (receipt as oracle)

```
instrument                   verdict                exit  divergence from dry-run-ca.txt
pristine                     ACCEPT-CA-65: FAIL     1     none (all 9 legs + details identical)
m1-r1-tree-any-hex           ACCEPT-CA-65: FAIL     1     none
m2-r2-append-only-dropped    ACCEPT-CA-65: FAIL     1     none
m3-r7-skeleton-anywhere      ACCEPT-CA-65: FAIL     1     none
m4-quotes-other-lesson       ACCEPT-CA-65: FAIL     1     QUOTES: receipt=FAIL/exit=2 … got=PASS/exit=0 …
m5-criterion-17-substring    ACCEPT-CA-65: FAIL     1     none
```

The pristine instrument reproduces the committed receipt exactly, so the receipt
is a valid, reproducible control. But the receipt pins only the pre-data FAIL
state, and a loosening that leaves base bytes failing is invisible to it: **four
of five mutants pass battery 1 unchanged, and only m4 is killed there.**

## Findings

1. **Four survivors (coverage).** m1, m2, m3, m5 each convert a defective tree
   into `ACCEPT-CA-65: PASS`, and no committed receipt or committed instrument
   detects them: `accept-ca.py` has no mutant-exclusivity leg (compare
   `accept-o.py`'s MUT/MUTEX/FRAG), and `accept-o.py` never executes
   `accept-ca.py` (`grep -n "accept-ca" reports/round-65/accept-o.py` returns
   only its own docstring line 12). The kills in the table above are the fixture
   receipts this probe produced (`stage/mut-ca/results.json`); landing them as a
   committed mutant-exclusivity receipt is what would close the class.
2. **Three survivors leak their defect in the leg detail, one does not.** For m1
   the detail still prints the *true* tree (`tree=0ec0e50e…`) beside a receipt
   holding `1111…`; m2 prints `original_intact=False` while PASS; m3 prints the
   stale `await L1` line while PASS. A reviewer reading the leg line can catch
   those three. m4 and m5 print details indistinguishable from a genuine green
   (`exit=0 out=['GATE_QUOTES: 0 findings']`; `criterion_with_tree_hash=True`),
   so only a receipt comparison (m4) or an independent check (m5) can catch them.
   A leg's PASS detail is therefore not evidence of the property it names.
3. **`skeleton` is the wrong token to key on (m3).** The routed R7 defect is
   "the line still advertises pre-land status". Keying on the literal word
   `skeleton` anywhere in the file lets a one-word rewrite ("skeleton structure
   prepared" → "structure prepared") pass with the substantive defect
   (`await L1 insertion`) intact. The pristine rule's two-token, line-scoped form
   catches it; the mutant's single-token, file-scoped form does not.
4. **`17\.` is not criterion 17 (m5).** `re.search(r"17\.", quality)` matches
   "section 17.2", "2017." or a URL path; the fixture that passes has no
   numbered criterion and no tree-hash rule at all, which is exactly the CRITERION
   leg's subject.
5. **Cross-instrument citation is unbacked (outside the five, worth the L1's
   attention).** `reports/round-65/accept-o.py` lines 12-15 state the round-64
   accept-ca global-token surfaces are closed by "keyed Ca legs
   `reports/round-65/accept-ca.py` revision 1: HISTOGRAM / R63SEP / DISPO legs",
   and `reports/round-65/claims.json` claim O repeats "accept-ca revision 1 keyed
   legs plus NITS value-pair pinning". The frozen `accept-ca.py` revision 1 has no
   HISTOGRAM, R63SEP, DISPO or NITS leg at all (`grep -nE 'leg\("' ` prints only
   R1 R2 R3 R4 R5 R6 R7 CRITERION QUOTES; those four legs exist in
   `reports/round-64/accept-ca.py` at lines 122/129/182/190 and fail in
   `reports/round-64/telemetry/dry-run-ca.txt` lines 4-7). So the accept-ca
   surfaces named in claim O's closure sentence were **dropped, not keyed**, and no
   round-65 receipt pins them. This is a claim-O operability finding routed here
   because it is the reason no committed receipt can kill m1/m2/m3/m5.
6. **Hygiene (not mine).** Two untracked artifacts appeared during the wave that
   this seat did not create: `reports/round-65/__pycache__/accept-c.cpython-314.pyc`
   (01:52:05; this seat only ever executed `accept-ca.py` and
   `tools/check-gate-quotes.py`, both with `-B`, so the pyc is another seat's
   un-`-B` run of `accept-c`) and a 1.4 MB `-.png` at the lane root (01:53:59,
   PNG 1275x1650 — a stray output of some other seat's command). Both are
   untracked residue the L1 should keep out of the integration commit.

## Restoration / integrity evidence

- `reports/round-65/accept-ca.py` sha256 before probe and after all runs:
  `e9a13ebb…cf215` (identical; the file was read, never written).
- No write outside `.ufo/waves/round-65/stage/mut-ca/` and this report. Fixtures,
  mutants and `results.json` are left in place as evidence. `git status
  --porcelain` at start: `?? .ufo/waves/round-65/`, `?? reports/round-65/`,
  `?? tools/check-row-fragments.py`; at end the same three plus two artifacts
  other seats created during the wave (`reports/round-65/__pycache__/`, `-.png`),
  listed in finding 6. No tracked file changed at any point.
- No tool installs or upgrades; no package manager invoked. Python 3.14.8,
  git 2.56.0 as found.

## Reproduce

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 -B .ufo/waves/round-65/stage/mut-ca/run-mut-ca.py     # rebuilds mutants+fixtures, prints both matrices
python3 -B .ufo/waves/round-65/stage/mut-ca/accept-ca.pristine.py --root .ufo/waves/round-65/stage/mut-ca/fixture-green
python3 -B .ufo/waves/round-65/stage/mut-ca/m5-criterion-17-substring.py --root .ufo/waves/round-65/stage/mut-ca/fixture-d5-no-criterion-17
```

Evidence files: `stage/mut-ca/{results.json,diffs.txt,accept-ca.pristine.py,m1…m5.py,fixture-green,fixture-d1…d5}`.

Report: .ufo/waves/round-65/w1/MutCounterCa.md
