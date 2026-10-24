# CriticR66Dispositions — disposition-fidelity attack on accept-ca.py

Scope: for each R66-D1..D5 (corpus/lessons/round-66-verifier-spotcheck.md §5, lines
102-106), compare the demanded fix against the leg in
reports/round-67/accept-ca.py (rev 0 pre-data). Every leg verified against the
on-disk instruments (`scripts/sources-census.sh`, `corpus/SOURCES.md`,
`LOG.md`/`SCORECARD.md` at base). All defects below are reproducible from the
counter source alone.

## Leg↔defect map (renumbered — attack surface starts here)

| leg | routed defect | leg enforces |
|-----|---------------|--------------|
| D1  | R66-D1 wave evidence | manifest parses, INCLUDE paths tracked at `<lands>:path`, ≥8 seat `.md`, ≥1 EXCLUDE |
| D2  | R66-D2 census/placement | `validate --file` exit 0 on **worktree** SOURCES.md + own placement/S753 checks |
| D3  | R66-D4 ledgers | heading regex + keyword co-occurrence only |
| D4  | R66-D5 reject rows | S801-804 unique/rejected/teaches + ≥6 rejected rows opened 2026-10-24 |
| SEQ | R66-D3 sequencing | substring checks on the three counters' **text** + tool selftest |

The counter's own leg names do not match the routed defect numbers (its "D3" is
R66-D4, its "D4" is R66-D5, R66-D3 is "SEQ"). Cosmetic, but it will mislead every
receipt reader — record as a naming finding for the scribe.

## Cross-cutting defect (enables half the exploits): lands bytes graded on D1 only

`git show`, `rev-parse HEAD`, and `status --porcelain` appear nowhere in the
counter. STAMP pins the `main` **ref** to `--lands`; every other leg except D1's
`cat-file -e` reads the **worktree** (`read()` opens `root/path`; census gets
`--file <worktree path>`). Two live variants of the R66-D3 class remain:

- **Dirty-clone PASS.** Materialize the clone at lands, then hand-edit
  `corpus/SOURCES.md`, `LOG.md`, `SCORECARD.md`, the manifest, and the lesson —
  never commit. STAMP passes (main == lands), every graded byte is uncommitted.
  The receipt claims committed-bytes conformance it never measured. The r66
  defect was "receipt stamped at lands can't see the records commit"; this is
  its mirror — "receipt sees bytes that aren't in the commit it names."
- **Detached-HEAD PASS.** Clone, `git checkout <other>` with doctored files.
  `rev-parse main` still equals lands; all worktree reads grade the wrong tree.

Smallest safe correction (cross-cutting): after STAMP, run
`git status --porcelain` and require empty output and `rev-parse HEAD` == lands;
or read every graded file via `git show <lands>:<path>` (D1 already does half of
this). One subprocess, kills both variants and removes the clone-hygiene
assumption the docstring currently relies on.

## Weakest leg: D3 (R66-D4, ledgers) — content-free PASS

Demand: "LOG.md needs a Round-66 entry and SCORECARD.md needs the round-66 rows."
The leg is pure shape; no claim, number, or verdict is ever compared.

Concrete exploit (all legs still PASS):

```
LOG.md:        ## Round 66
SCORECARD.md:  Axes — round 66
               coverage operability calibration round-66
```

- `^#+.*round[ -]?66\b` matches the heading; the redundant mention check follows.
- `axes\s*—\s*round[ -]?66` matches the scaffold; each axis regex is an
  unordered same-line OR (`{ax}.*round66|round66.*{ax}`), so three bare words on
  one line satisfy all three "rows". No table shape, no verdicts, no scores.
- Base LOG.md/SCORECARD.md have **zero** round-66 mentions (verified), so a
  fabricated retro-entry with invented numbers is indistinguishable from a real
  one — the leg has no anchoring data to check against, and none exists to give
  it. This is a genuine instrument limitation, not just laziness: the honest fix
  is to require the entry to name this round's receipts/claims that *do* exist
  (e.g. `rounds[…]` receipt refs, `ACCEPT-C-67`, or the three counter paths) so
  at least one graded string is falsifiable.
- Same-line co-occurrence also means prose like "coverage, operability and
  calibration were unprovable in round 66" passes as a scorecard table.

Correction: require a table row per axis containing a real verdict token from
the round (PASS/FAIL/HOLDS + a counter or receipt filename); require >N non-
blank lines under the round-66 heading in LOG.

## Second-worst: D2 S753 used-by assert is dead code — repair only backstopped while status==mined

`re.search(r"^\|\s*S753\s*\|", reg)` returns match text `| S753 |` (verified —
the regex ends at the second pipe). `split("|")[1:-1]` → `["S753"]`, `len==1`,
so `len(c753) == 11 and c753[10] != "—"` can never fire. The leg's only live
guard is census E11, which `usedby_findings()` gates on `status == "mined"`
(verified, census line ~560). S753 at base is `mined` with used-by `-` (verified
line 709).

Concrete exploit: flip S753's status cell to `queued` (or `admitted`), keep
used-by `-`. Census skips E11 for non-mined rows, no other E-class fires, census
exits 0, dead-code assert can't fire → D2 PASS with the exact E11 defect
unrepaired. The demanded fix (em-dash) is never checked by anything live.

Secondary fidelity gap in the same leg: the spot-check demands "commit
`census-end.txt`" — the leg never names that file. Exit-0 is the stronger half
of the demand and is enforced; the durable-evidence half is not. Also note the
exit-0 half is stricter than "no E12/E11" (exit 1 on any E-class) — that
direction is correct, other E's cannot hide.

Correction: fix the regex to capture the whole row — `re.search(rf"(?m)^\|\s*{sid}\s*\|[^\n]*", reg)` — then assert `cells[10] == "—"` unconditionally,
and add `MANIFEST`-style check for the committed `census-end.txt`.

## Third: SEQ (R66-D3) — self-grading substring checks, no frozen-sha pin

The leg's entire assertion is that each frozen counter's **text** contains the
strings `--lands`, `required=True`, `stamped revision`, `evaluated revision`,
`mv_rev == lands` (whitespace-normalized). A comment satisfies all five. The
printed self-sha is reported but never compared to a frozen value — nothing in
the instrument notices if a counter was edited after freeze. For accept-ca.py
itself the graded file and the grader are the same mutable file.

Tool check is `"14/14" in st.stdout` — a stub printing that string exits 0.
(accept-o independently exercises the tool, but nothing here prevents the r67
worktree copy from being the stub while committed bytes differ — see
cross-cutting defect.)

Correction: record each counter's sha256 in claims.json (or a committed
freeze-manifest) and assert equality; grade the counters' *behavior* (run
`--lands <wrong-sha>` and require exit 1), not their source text.

## D1 (R66-D1) — real but shapeable

What's enforced: manifest parses, every INCLUDE is tracked at `<lands>:path`
(committed bytes — the only lands-graded leg), ≥8 seat-report paths, ≥1 EXCLUDE.
What isn't:

- Seat count counts **INCLUDE lines**, not paths — `INCLUDE .ufo/waves/round-66/w1/a.md` ×8 passes with one fabricated empty file; content is never graded, so 63 seat reports can be replaced by 8 empty stubs. Demand says "commit wave evidence", which empty files technically satisfy — flag as shape-vs-substance.
- `EXCLUDE` requires only `^EXCLUDE\s+` — `EXCLUDE .` counts as a named exclusion; no reason text is demanded, though the docstring claims "with reasons".
- Manifest itself is read from the worktree — under the dirty-clone variant the committed manifest and the graded manifest differ.
- claims.json's stronger statement ("registry + row fragments + mutant sources tracked at lands") names classes the leg never checks — INCLUDE count is the only constraint beyond seats.

## D4 (R66-D5) — mostly sound; two gaps

S801-804: unique, `status=rejected`, `REJECTED:`/`flip:` in teaches — matches
demand. Placement is transitively backstopped (rows outside `## Registry` →
census E12 → D2 fails). Gaps:

- New r67 rejects need only `status=rejected` + `opened=2026-10-24` — no teaches, no used-by, no existence gate. Two one-line stubs satisfy "≥2 new first-class rejected rows"; "first-class" is unenforced for the rows that matter most (this round's own gate output). Fabricated rejects inflate the sample — add a minimum-cell content check (e.g. teaches contains `REJECTED:` too, used-by names a real counter/gate artifact).
- `new_rejects` is computed (line ~232) but never used — dead code betraying an intended separate count that was never enforced. And S801-804's `opened` cell is unchecked: a restored row carrying any old date passes, while the `opened_today` count then demands 6 *other* new rejects (or the lane backdates silently — either way the demand's "durable sample" is met in shape only). Minor.

## D2 remaining nits

- Counter heading regex `^##\s+\S.*$` requires column-0 start and uses substring `"Registry"`/`"Leads"`; census allows 0-3 leading spaces and exact `Registry`. The divergences mostly cancel through census exit-0 backstop, but a `## Registry Annex` heading before `## Registry` shifts `reg_pos` early (substring match), widening the accepted row range — census still E12s such rows, so transitively caught. Not independently exploitable.

## Addendum — C×Ca joint-satisfiability (L1 ruling + residual)

Verified CriticFrontier's conflict: `accept-c.py` `allowed_new = S805-S828 ∪
{S801-S804}` (line 357) vs Ca D4's ≥2 rejects opened 2026-10-24 beyond S801-804
(ids must be S829+). Base registry frontier confirmed S800 — no base id lets a
reject dodge `extra_ids`. L1's per-claim lands separation resolves it: A_c
(C's receipt) appends only NEW_IDS∪EXTRA_IDS over base; A_ca carries S829+.

Residual hole the resolution creates (record as design finding): **the appended
row set at A_ca is bounded by no counter.** C's APPEND leg holds only at A_c;
rows appended between A_c and A_ca — beyond the S829+ rejects — are checked by
nothing except Ca's D4 count (which only *counts* rejected+today rows) and
census exit-0 (shape/E-classes only). A well-formed `mined`/`queued` row with a
real used-by path (e.g. `| S900 | … | mined | 2026-10-24 | … | LOG.md |`)
sails through A_ca's census (no E-class fires) and D4 (not counted — wrong
status or is counted but status=rejected only matters for the count). So "the
registry grows append-only bounded to declared ids" is true at the C receipt
and unguarded at the Ca receipt — the same stale-receipt class in miniature:
the tip a future verifier opens is not the tip either receipt bounded. Smallest
fix: reuse the dead `new_rejects` computation — Ca's D4 should bound the
A_ca-appended set to `S801-S804 ∪ rejected-opened-today` (and nothing else),
or add a shared APPEND leg to Ca with its own EXTRA_IDS.

Ruling accepted — the joint predicate is satisfiable as sequenced; the finding
is that the sequence leaves the A_ca append window unguarded, not that the
counters must be revised.

## Verdict

D2's demanded exit-0 **is** enforced (stronger than no-E12/E11), but the leg's
own S753 check is dead code and the repair survives only via census's
mined-status gate. D3 (R66-D4) is the weakest leg — fully content-free, PASSes
on a 3-line scaffold, and the fabricated-retro-entry risk is real because the
ledgers are blank at base. Highest-value fixes, in order: (1) worktree-vs-lands
pinning (`git status --porcelain` empty + `HEAD == lands`, or `git show` reads);
(2) D3 content anchoring; (3) S753 regex repair; (4) SEQ sha-pin instead of
substrings; (5) D1 seat dedup/content + manifest-from-lands.

Axes impacted: calibration (receipt integrity — cross-cutting defect), records
fidelity (D3/D4 stubs), conformance (D2 census-end.txt unrecorded, S753).
Tradeoff vs fixable defect: all five corrections are mechanical and cheap; none
requires re-judging the claim. The dirty-clone variant, if unguarded, is a
REJECT-class hole in the very protocol this round exists to prove — the
canonical judge should treat "receipt graded uncommitted bytes while claiming
stamped==evaluated" as disqualifying for Ca.

Dependency noted: `reports/round-67/dispositions/` does not exist yet at lane
tip — D1's manifest is a build-side deliverable; this review attacked the
instrument, not a landed disposition.
