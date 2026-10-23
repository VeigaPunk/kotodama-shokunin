# ReviewerSeparability — round 64, wave 1

SEPARABILITY re-run of the round-63 check against the round-64 counters.
Seat: `kotodama-r64.ReviewerSeparability`. Base `ff30a205c8d23b35f1ac533740121a955a9fda96`, declaration `097c21d`.
Counters measured: `reports/round-64/accept-{c,o,ca}.py`, byte-identical across all three scratch copies (sha256 groups of 3 each).
Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewerSeparability/{s0,s1,s2}` — full working-tree copies (`.jj`, `.ufo`, `target` excluded; `.git` carried for `git show`/`git diff` legs). Every counter was run under a `PYTHONPATH`-injected `sitecustomize` shim logging every `open()` (pid, mode, path) for the counter and all subprocesses; per-run logs at `trace-{c,o,ca}-s{0,1,2}.log`.

## Fixture states

- **s0 = working tree as found.** Claim C lands absent (no entry file, 0 rows S718–S749 in `corpus/SOURCES.md`, no README index row). Ca lands present. O lands present (counter + unchanged `tools/reopen-row.py`).
- **s1 = s0 + claim C lands**, assembled by `integrate-w2.py` against `.ufo/waves/round-64/rows/` with two reviewer-authored stub contributions (S723, S740 — placeholder `example.org` rows, deliberately non-claim) and a reviewer-authored `readme-row.txt` mirroring the skeleton topic. Result: registry 643→675 rows, entry present, README index row present.
- **s2 = s0 with Ca lands reverted to BASE bytes** (`LOG.md`, `corpus/LOG.md`, `SCORECARD.md` via `git checkout ff30a20 --`; `reports/round-63/telemetry/revisions.txt` deleted — untracked, absent at base), then a **records-only append**: a `## Round 64` LOG section recording the repairs in prose, naming no values (no `final-measures-{c,o}.txt`, no revision hashes, no `A 13 / B 11`, no nit numbers, no separability result string).

## Test (1): claim-C ablation

Commands (run in each scratch root): `python3 -B reports/round-64/accept-{c,o,ca}.py --root .`

**s0 output (C lands absent):**

```
accept-c: FILE FAIL unreadable; ROWS FAIL bad=[S718..S725 :rows=0] checked=26;
  REJECTS FAIL bad=[S744..S749 :rows=0]; ONEID FAIL cited_lines=0;
  RESTATE PASS; HOSTS PASS; LINK PASS;
  APPEND FAIL s687_queued=False base=643 measured=643 +32=False;
  NOHARM FAIL diff=[]; SWEEP FAIL exit=0 topic_row=False;
  LIVE FAIL bad=[S718:no_row S723:no_row S728:no_row S733:no_row S738:no_row S743:no_row]
  ACCEPT-C-64: FAIL exit=1
accept-o: all 23 legs PASS — ACCEPT-O-64: PASS exit=0 (426.6s)
accept-ca: all 7 legs PASS — ACCEPT-CA-64: PASS exit=0
```

**s1 output (C lands present):**

```
accept-c: FILE PASS; ROWS PASS checked=26; REJECTS PASS checked=6; ONEID PASS
  cited_lines=26 tool exit0; RESTATE PASS lines=26; LINK PASS;
  SWEEP PASS exit=0 topic_row=True;
  HOSTS FAIL bad=[S723:example.org S740:example.org]   <- reviewer stubs only
  APPEND FAIL s687_queued=False base=643 measured=675 +32=True  <- S687 flip unlanded
  NOHARM FAIL diff=[]                                   <- main lacks entry commit
  LIVE FAIL bad=[S723:NOT_LOCATED (stub), S733:NOT_LOCATED pmc.ncbi.nlm.nih.gov]
  ACCEPT-C-64: FAIL exit=1 (156.6s incl. network)
accept-o: all 23 legs PASS — ACCEPT-O-64: PASS exit=0 (426.5s, byte-identical verdict)
accept-ca: all 7 legs PASS — ACCEPT-CA-64: PASS exit=0 (byte-identical verdict)
```

**Result:** accept-c FAILs without C lands (s0) and eight of its legs flip FAIL→PASS when C lands appear (s1: FILE, ROWS, REJECTS, ONEID, RESTATE, LINK, SWEEP, +row counts on APPEND); residual s1 FAILs are attributable to stub rows (HOSTS, LIVE S723), an unlanded declared flip (APPEND: S687 still `mined` in the working tree), an uncommitted main (NOHARM diffs `BASE main`, not the working tree), and one network flake (LIVE S733; S718/S728/S738/S743 LOCATED). accept-o and accept-ca produce **identical PASS verdicts in both states** — C's lands are neither necessary nor sufficient inputs to them.

## Test (2): records-only append (no named values)

s2 output:

```
CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
PTRS FAIL score_dead=True stray_dead=True o_fixed=False c_fixed=False
HISTOGRAM FAIL tiers={'A': 13, 'B': 11} correction_present=False
DISPO FAIL items5_7=False s687_flip=False s693_kind=True
REVNAMES FAIL missing=[8d2041fa 38ec1316 0c892ce 80ff34c final-measures-c.txt
  final-measures-o.txt rev-separability.txt census-end.txt]
NITS FAIL seat_reports_nit=True w04_nit=False
R63SEP FAIL result_cited=False dep_class_named=False
ACCEPT-CA-64: FAIL exit=1
```

**Result:** the records-only state fails exactly the named-value legs — **PTRS, HISTOGRAM, REVNAMES all FAIL** as the frozen control claims; DISPO/NITS/R63SEP also fail (named values absent). CANONLOG passes on the record itself, matching the control spec: only the three value-legs are pinned by it. The counter requires Ca's actual lands, not log prose.

## Test (3): cross-claim path reads — dynamic read-sets + static grep

Dynamic (all `open()`s by counter and subprocesses; git binary reads assessed statically — it never opens claim files itself, only object DB + `BASE:` blobs):

| counter | repo paths opened dynamically | other reads (static) |
|---|---|---|
| accept-c | `corpus/SOURCES.md`, `corpus/README.md`, entry (attempted→opened in s1), `corpus/knowledge/**` (238 files, via `sweep.py` child), `reports/round-61/reopen-quote.py`, `tools/check-cited-lines.py` (child) | `git show BASE:corpus/SOURCES.md`, `git diff BASE main -- corpus/knowledge` (NOHARM) |
| accept-o | `tools/reopen-row.py` **only** — zero other lane paths in 292 opens/61 pids | tempdir writes only (`/tmp/accept-o-64-*` synthetic registries incl. a `corpus/SOURCES.md` *inside the fixture home*, never the lane's) |
| accept-ca | `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt` — exactly the four declared lands | `git show BASE:corpus/SOURCES.md` (HISTOGRAM, base bytes) |

Static grep of all three counters for `corpus/knowledge`, `SOURCES`, `README`, `LOG`, `SCORECARD`, `revisions`, `accept-*`, `telemetry`, `.ufo`, `round-6` literals: only own-land paths, shared tools, docstring prose, and the git-history paths above. accept-o's only `SOURCES.md`/`corpus` strings are tempdir fixture paths.

## Dependency classification

**Record dependencies (expected, not inter-claim):**
- `tools/check-cited-lines.py`, `reports/round-28/readme/sweep.py`, `reports/round-61/reopen-quote.py` — shared lane tools executed by accept-c (and reopen-row.py by accept-o). Lane infrastructure; round-63 manifest class REC.
- `git show BASE:*` and `git diff BASE main` — frozen historical bytes / VCS metadata. Notably accept-ca's HISTOGRAM and accept-c's APPEND read `corpus/SOURCES.md` **at BASE**, i.e., frozen bytes — a C-land *path* but never C's claim state; class record, corroborated by s1 pass (s1's registry had 32 appended rows yet ca stayed byte-identically green).
- accept-c SWEEP reading all `corpus/knowledge/**` — reads every entry including would-be C entry; shared-infrastructure sweep, and s1 shows it passing *only when* the C entry+index exist → land coupling of C's own legs, not of other claims' counters.

**Inter-claim dependencies:** **none found.** No counter reads another claim's lands, exports, or working-tree state; no counter's outcome changed under another claim's ablation.

## SEPARABILITY findings

SEPARABILITY: **0 dependency findings** — the three counters are separable: each fails without its own claim's lands and is byte-identically unaffected by another claim's lands. exit=0 on the separability check itself.

## Defects observed during measurement (not separability violations)

1. **Integration kit cannot assemble as shipped:** `integrate-w2.py` aborts — `ScribeEntrySkeleton/entry.md` line 4 (`- source:`) contains literal `S718–S743` while the assembler's id-stripper targets a different sentence ("Round-64 row citations S718–S743 …"); error `generated entry would fail check-cited-lines.py at line 4`. Even past that, `readme-row.txt` is absent → `AssemblyError`. I supplied both fixes in scratch only. Named owner work for ExecIntegrate.
2. **S687 mined→queued flip unlanded:** `corpus/SOURCES.md` line 642 still `mined` in the working tree; accept-c APPEND will FAIL until applied (claim declares "S687 flips mined → queued, logged").
3. **Missing contribution rows:** S723, S740 still absent from `.ufo/waves/round-64/rows/` at measurement time (executors running); my stubs are fixtures, not claim data.
4. **Cited-but-absent telemetry:** claims.json names `telemetry/{controls-c.txt,control-o.txt,mut-o.txt,edge-o.txt}` as receipts/lands; not present in the tree yet (wave in flight).
5. **LIVE leg flake (observation):** S733 locator fetch failed on a live PMC URL (S718/S728/S738/S743 LOCATED); the rev-4 retry budget (3×, 20s apart) was exercised — single-flake residual, matches its receipt class.

## Residual risk / verification gaps

- `open()` tracing covers Python-level reads; `git` binary I/O was attributed statically (it reads object DB, never claim files by path in these counters). `os.stat`/`scandir` unwrapped — swept tool reads were all `open()`-captured; directory enumeration is the declared sweep's own scope.
- accept-c's NOHARM leg compares committed `BASE..main`, so it stays FAIL on any uncommitted working tree by design — cannot be re-verified green until C lands commit; behavior in scratch is consistent, not a finding.
- accept-o's mutants (MUT leg) re-execute the counter itself with `--only` — self-scoring but pinned per-mutant leg; observed kill evidence for all 10 mutants on both runs.

Tools installed: none (python3 3.14.8, git, tar already present).
