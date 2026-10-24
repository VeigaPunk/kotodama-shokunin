# RevLedger66 — audit of the round-66 LOG/SCORECARD backfill against the committed receipts

Seat: reviewer (round 67, v2 wave). Lane read-only: no counter executed, no git/jj write, no
lane file touched except this report. No tools installed or upgraded. Target: the R66-D4
backfill drafts

- `.ufo/waves/round-67/stage/log-r66.md` (LOG half)
- `.ufo/waves/round-67/stage/scorecard-r66.md` (SCORECARD half)

checked byte-for-byte against `reports/round-66/telemetry/*` as committed at `65fe8572`
(receipts) / `4589ebdd` (records), plus read-only `git show`/`cat-file`/`sha256sum` and one
read-only census run on a `/tmp` extraction of the `65fe8572` registry blob.

## Ground truth (committed receipts, verbatim values)

All three receipts: measured revision `65fe8572822ef83f1750593af77daddf34a1e337`, tree
`f0681e6ea5bc4d4e1e2a93b42ea460a739358887` (`git rev-parse 65fe8572^{tree}` reproduces it).
Each receipt's `counter sha256 (self)` equals `sha256` of the counter blob at lands —
verified: C `987c4bbc…4f53a`, O `b366c25b…fcc`, Ca `f206095b…cb75`.

| receipt | lines | legs printed | verdict |
|---|---|---|---|
| `final-measures-c.txt` | 17 | REVISION + 12 (FILE,SET,ROWS,ONEID,RESTATE,HOSTS,LINK,APPEND,NOHARM,SWEEP,CAPTURE,TOPIC), all PASS | `ACCEPT-C-66: PASS` |
| `final-measures-o.txt` | 14 | REVISION + 9 (SELFTEST,DIFF,OPTIONS,BOUND,STATIC,MAXRUNS,JOBS,MUT,FIXTURES), all PASS | `ACCEPT-O-66: PASS` |
| `final-measures-ca.txt` | 10 | D1,D2,D3,D4,CRITERION,QUOTES — **D2 FAIL** | `ACCEPT-CA-66: FAIL` |

Key figures inside those bytes: C `lines=52 h1=1 h2=6 h3=0`, `SET missing=[] non-unique=[]`,
`ROWS n=0` (0 *bad* rows — the leg's `n` is `len(row_bad)`, `accept-c.py:257`), `HOSTS hosts=21`,
`APPEND appended=23`, `SWEEP exit=0 readme_sha256 f6e0cb87…`, `NOHARM diff=[games-play-sport-contests.md,
scent-perfume-aromatics-codes.md]`; O `count=63/63`, `diff_lines=428`, `MUT mutants=4 failing=[]`,
`FIXTURES lanes=2 wall=6.2s`, `JOBS j1=1 j4=1 eq=True`; Ca `D2 FAIL
bad=['…final-measures-c.txt:no_carrier','…-o.txt:no_carrier','…-ca.txt:no_carrier']`,
`D3 named=63 present_nonempty=63 dead=1 min=8`, `D4 runs=9 skipped=0`, `QUOTES gate_ids=25`.

Independent re-derivations (read-only, no counter run):

- registry rows: 701 at `94209e8f`; **724** at `65fe8572`, `4589ebdd`, `HEAD` (+23 = S776 + S779–S800).
- entries 239 → 240; `corpus/knowledge/culture-material` 32 → 33.
- tiers: S779–S800 = **A 13 / B 9**; S776 = B (so the 23 appended rows are A 13 / B 10).
- `S753` used-by at `65fe8572` and `HEAD` is `-` (ASCII hyphen), not the em-dash.
- receipt carrier: `git log -1 main -- <receipt>` = `4589ebdd`, `4589ebdd^` = `65fe8572`.
- `4589ebdd` carries exactly the 3 receipts, 41 inserted lines (17+14+10).
- `git diff 94209e8f 4589ebdd -- LOG.md SCORECARD.md` is empty; `git show 4589ebdd:LOG.md`
  has 0 `round-66`/`round 66` hits.
- `git ls-files .ufo/waves/round-66` = 0; wave tree = 18,589 files; `rows/ScoutReject0{1..4}/row-S80{1..4}.txt` exist untracked.
- `git log --all -- reports/round-66/telemetry/census-end.txt` = 0 commits.
- spec `items` = 64, roles 21 reviewer / 18 scout / 6 critic / 5 scribe / 5 mutation-tester /
  4 executor / 2 revenger / 1 connector / 1 sentinel / 1 simplifier; `seat-evidence.txt` names
  63 reports, all present, `dead: ScoutRow01`.
- census on the `65fe8572` registry blob: **E12 ×23**, **W04 ×27**; every used-by target exists
  except S753's `-` (only `—` is the validator skip value) → E11 ×1 by inspection.
- `separability-real.txt`: `SEPARABILITY: 8 findings`, `units=4 ordered_pairs=12
  acceptance_runs=9 skipped=0`.

## Verdict on the drafts

**No draft asserts `PASS` where the frozen verdict was `FAIL`.** Both halves record
`ACCEPT-CA-66: FAIL`, D2 `no_carrier`, `admitted = false` / `rejected-honest-stop`. The only
`D2 PASS` / `ACCEPT-CA-66 PASS` strings are inside the attributed quotation of the filed fleet
report, which is the defect the correction block is meant to expose.

Every checkable number in both drafts matches the receipt bytes except the items below:
64 seats/role mix ✓, 22 survey rows ✓, `hosts=21` ✓, `appended=23` ✓, A13/B9 ✓, 701→724 ✓,
239→240 ✓, 32→33 ✓, 52 lines / 1 H1 / 6 H2 ✓, 63/63 selftest ✓, 428 diff lines ✓, 4/4 mutants ✓,
6.2 s ✓, 9/9 O legs (10 printed lines) ✓, 12/12 C legs (13 printed lines) ✓, 63 named seat
reports / `dead=1` ✓, runs=9 skipped=0 ✓, 8 separability findings ✓, gate_ids=25 ✓,
`4589ebdd` parent = lands ✓, tree `f0681e6e` ✓, `3 files / 41 lines` ✓, `git ls-files` = 0 ✓,
18,589 files ✓, S801–S804 only as untracked fragments ✓, `49 literal hits` false-owner trap ✓
(sourced at `.ufo/waves/round-66/w1/ConnectorSiblings.md:55`).

## Findings

### HIGH

**H1 — the SCORECARD draft states a 24-row SET; the SET leg is 22 rows (or 23 appended).**
`scorecard-r66.md` coverage row: "24-row SET complete and unique, 21 hosts". The frozen leg's
set is `NEW_IDS = [f"S{n}" for n in range(779, 801)]` (`reports/round-66/accept-c.py:50`) —
22 ids — and the receipt prints `SET PASS missing=[] non-unique=[]` over exactly those.
`S776` is *not* in `NEW_IDS`; it enters only through `APPEND` (`appended=23`). Neither 24 nor
the implied set exists. This is the same arithmetic class as the filed "+22 rows 701→724"
defect the draft's own correction block flags, reintroduced one line above it.
Fix: "22-row SET (S779–S800) complete and unique; APPEND appended=23 including the S776
supersession row".

### MEDIUM

**M1 — dead pointer in the SCORECARD correction block.**
`scorecard-r66.md` cites `.ufo/reports/round-66/kotodama.md`. The lane's `.ufo/` contains only
`waves/` (`ls .ufo` → `waves`); the file is the fleet-root
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-66/kotodama.md`. Since every other citation
in both drafts is lane-relative, this reads as a missing lane file. The LOG draft gets it right
("fleet `.ufo/reports/round-66/kotodama.md`"). Fix: prefix `fleet` or write
`../.ufo/reports/round-66/kotodama.md`.

**M2 — "0 word-bounded filename owners at base" is not a receipt value.**
It appears in the SCORECARD coverage row as part of the before-state. No C leg measures base
ownership; the receipt's base-side evidence is `dry-run-c.txt` FAIL (`FILE` absent at `94209e8f`).
The zero is prose from `claims.json` and `.ufo/waves/round-66/w1/RevClaimC.md:8` (literal text
search, line counts, explicitly not semantic proof — `RevClaimC.md:206`). Keep it, but label it
as the claim's author census rather than a leg result, or a spot-check reader will look for a
`BASE` leg that does not exist.

**M3 — the LOG draft's "E11 ×1" is true but not reproducible from the receipt shape.**
The LOG census bullet asserts "E12 ×23 … plus E11 ×1". E12 ×23 and W04 ×27 reproduce exactly
on the `65fe8572` blob; E11 does not reproduce outside the lane because `sources-census.sh`
resolves used-by paths relative to the registry file's directory — a `/tmp` extraction prints
`E11 ×640`. The count is still true: only S753 carries `-`, every other used-by target exists on
disk, and `-` is not the validator skip value (`—` is). Fix the wording to separate the
reproduced counts from the inspected one: "E12 ×23 and W04 ×27 reproduced; E11 ×1 by
inspection (S753 `-`; only `—` is skipped; all other used-by targets exist)".

### LOW

**L1 — "cites S776 ×1 / S753 ×0" is parenthesized-citation-only.** The Ca row's D1 detail is
correct under the leg (`\(S776\)` = 1, `\(S753\)` = 0, `accept-ca.py` D1), but the bare string
`S753` still occurs once in the games entry (`git show 65fe8572:corpus/knowledge/culture-material/
games-play-sport-contests.md | grep -n S753` → line 5, the `verified-at` note "re-pointed S753 ->
S776"). A reader grepping sees 1, not 0. Add "(parenthesized citations)".

**L2 — "no `<base>` assertion" is a leg property, not receipt text.** The O row groups
BOUND/STATIC/MAXRUNS as "exit 2 with `SEPARABILITY_PARTIAL` + `SEPARABILITY_UNRESOLVED` and no
`<base>` assertion". The receipt prints `exit=2 partial=True unresolved=True`, `exit=2`,
`exit=2`; the no-`<base>` condition is the counter's internal predicate. Attribute it to the leg
definition if precision matters.

### Note to the integrator (not a draft defect)

**N1 — R67 D3 cannot police these numbers.** `reports/round-67/accept-ca.py:192-205` checks only
`^#+.*round[ -]?66`, a `round-66`/`Round 66` substring, `axes\s*—\s*round[ -]?66`, and any
`coverage|operability|calibration` co-occurring with `round-66` anywhere in the file. The
SCORECARD intro line already satisfies all three axis regexes at once, and the file contains
`round-65` "coverage" rows that could satisfy them after integration. The leg will pass whether
or not the per-axis rows exist or are numerically true, so the four-row table and its figures
rest on this review, not on the gate. Integrate the table as drafted (with H1 fixed), not a
minimal heading.

## Adjacent cross-reference (outside this seat's r66 scope; verified read-only)

The wave's C-APPEND vs Ca-D4 id conflict is **satisfiable under the L1's per-claim lands
sequencing**, which I checked against the frozen bytes after the interrupt:

- `accept-c.py:70` `EXTRA_IDS={S801..S804}`, `:357` `allowed_new = NEW_IDS ∪ EXTRA_IDS`,
  `BASE=ad5b52b0` (`:62`), evaluated revision from `git rev-parse main` of `--root` (`:175`).
  At a lands commit `A_c` whose registry holds only base + S801–S804 + S805–S828, APPEND's
  `extra=[]` and ROWS still sees 24 mined rows.
- `accept-ca.py` D4's floor is `rej_opened_today >= 4 + 2`; at a later `A_ca` carrying S829+
  rejected rows the floor is met, and Ca's D2 census runs on the `A_ca` registry where the new
  rejects sit inside `## Registry`.
- Claim C's own statement already budgets this: "registry 724 -> 752 rows (S805-S828 plus the
  declared disposition additions S801-S804 as rejected rows — 728 + 24)" (724+4+24=752).

Two conditions make the sequencing real, and they are review-visible:

1. C must be measured only at `A_c`. Re-running `accept-c.py --lands A_c` from the final tip
   (or evaluating C at `A_ca`) prints `APPEND FAIL … extra=[S829…]`; the claim is
   lands-relative, not tip-stable. The r67 LOG/SCORECARD must name each claim's own stamped
   lands revision, never imply a single common revision.
2. `A_r` (S801–S804 + r66 dispositions) must land before `A_c`; otherwise EXTRA_IDS never
   resolves and C's APPEND fails. Commit order is itself the evidence here, which is why
   `check-receipt-seq.py --topo` is post-records evidence only.

I hold no routing authority: recorded here so the integrator does not reconcile the two
counters by conflating their lands revisions.

## Residual risk / verification gaps

- The frozen counters were not re-executed (receipt bytes at `65fe8572` are the record of
  record; a re-run today would measure a moved tip, which is the very failure class R66-D3
  names). All checks above are byte reads, `git` reads, or one read-only census.
- E11 ×1 is inspection-backed, not receipt-backed (M3).
- Review-only C items (blind per-row support, semantic ownership, lore handoff) are outside this
  seat; the drafts correctly leave them open.
- `claims.json` C still says "registry 701 -> 725+" while the landed bytes are 724. Both drafts
  flag the overcount and use 724; the frozen statement is pre-data and unchanged, so no action
  beyond the drafts' existing correction rows.
- The two drafts are stage-only. If the L1 integrates one half and not the other, D3 fails on
  the missing heading — and if it integrates both, H1/M1 would propagate into the canonical
  records verbatim.

Report: .ufo/waves/round-67/w1/RevLedger66.md
