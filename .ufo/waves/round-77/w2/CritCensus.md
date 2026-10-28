# CritCensus — W2 attack on C base/target counts + SOURCES contract (round 77)

Lane `kotodama-shokunin`, base `211f9526800906e0c585d878d265c37e5e090c15`. Target: the
C claim's count contract — 820 registry rows / 253 knowledge files at base, expected
822/254 at a one-entry/two-row landing — plus row cell shape, statuses, used-by and
append-only rules.

**Verdict: the arithmetic survives falsification — every base number reproduces
independently and the 822/254 landing deltas are internally consistent. But the
count contract is content-blind, and the staged rows carry three concrete defects
that the counters as described will not catch: a permanently wrong provenance cell
in S897, literal `DRAFT CELL` placeholder text in evidence cells, and a tier-A row
grading a document the entry itself grades tier B. 822/254 is achievable with all
three defects live; the counts alone therefore do not witness a correct landing.**

## Independent recount (all against the base blob, not the working tree)

```
$ git -C …/kotodama-shokunin show 211f952…:corpus/SOURCES.md > SOURCES-base.md ; wc -l
953
$ grep -cE '^\| S[0-9]+' SOURCES-base.md
820
$ grep -E '^\| S[0-9]+' … | awk -F'|' '{print NF}' | sort | uniq -c
820 13            # every row exactly 11 cells — zero shape violations
$ … '{gsub(/^ +| +$/,"",$5); print $5}' | sort | uniq -c      # tier
493 A   311 B   16 C
$ … '{gsub(/^ +| +$/,"",$9); print $9}' | sort | uniq -c      # status
725 mined   58 queued   37 rejected
$ grep -oE '^\| S[0-9]+' … | awk 'NR>1 && $1<=p{print "OOR",$1}{p=$1}END{print NR}'
820 — strictly increasing S001…S896, no duplicates
$ git ls-tree -r --name-only 211f952… corpus/knowledge | grep -c '\.md$'
253   (all files are .md, all at depth corpus/knowledge/<dir>/<name>.md)
$ git cat-file -e 211f952…:corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md
ABSENT
```

820/493/311/16/725/58/37 exactly match `reports/round-77/telemetry/census-start.txt`
as quoted in CLAIMS-DRAFT. Landing deltas: +1 file at an absent path → 254; +2 rows
at unused ids (S897/S898 absent from the base blob and from every non-`.ufo` tree
path — `git grep -lE 'S89[78]' <base>` hits only `.ufo/waves/round-6x..7x`
assimilation staging files) → 822. Staged-id space confirms: r77
`assimilation/reg-ids` ends at S896 (line 820), `staged-ids` S897..S904 — the
claimed staged→lane map (S897→D1, S903→S898) is collision-free at document level.

## Findings

### F1 — KILL-GRADE: staged S897 `source` cell asserts false provenance, and the cell is append-only-permanent

`w1/stage/ExecCensusEnd/rows-897-898.md` row 1, source cell (verbatim):

> "live answered HTTP 403 to **both the plain and the browser-shaped request** on
> 2026-10-27 (wall met, not passed); capture status 200"

This directly contradicts the round's own evidence. CLAIMS-DRAFT: "browser-shaped UA
HTTP 200 / 143252-byte article. **Do not claim both UAs were blocked**." The draft
entry's recheck detail: the browser-UA curl answered HTTP 200 / 143,252 bytes; only
`curl/8.7.1` got 403. If this cell lands verbatim, the append-only rule ("only
`status`, `recheck` and `used-by` change in place … a correction is a new row")
makes the false statement *permanently unfixable* — no future round may edit it.
It also trips the claim's own kill rule ("wrong/unopened source … → claim fails as
declared") and poisons the CENSUS leg's E11 anchor resolution (the row's anchor
says "capture 20240111092427" while the claim names the live copy the located
source).

Counterexample: ROWS leg checks id-shape/delta/scope; nothing in the frozen design
diffs a `source` cell's prose against the committed evidence window. The stale cell
passes every count-based check while recording a wall that was never met by the
located source.

Smallest safe correction: before freeze, rewrite the S897 source cell to the live
state (plain-UA 403/162B + browser-UA 200/143,252B, capture as pair), and add a
counter leg (or extend EVIDENCE) asserting each new row's access-provenance tokens
appear in the committed window.

### F2 — `DRAFT CELL` placeholders inside evidence cells pass every shape check

Same file: S897 anchor cell reads `quote located: DRAFT CELL, …`; S898 anchor cell
reads `DRAFT CELL, the located quote and its window s…`. Census checks `NF==13`,
enums, dates — never cell semantics. The claim's target requires "committed
evidence quote windows"; nothing verifies the anchor/`teaches` cells are non-
placeholder or that the `quote located:` string occurs in `reports/round-77/
evidence/S89x.txt`. Round-76 precedent (S894–S896 rows) shows real quote cells are
the convention; landing DRAFT CELL text would violate it silently.

Smallest safe correction: fill both cells pre-freeze; have GATE/EVIDENCE legs grep
each row's quoted span against the committed window file.

### F3 — Tier incoherence: row grades A what the entry grades B

Staged rows: S897 `tier A`, S898 `tier A`. The draft entry's own `- sources:` and
§7 provenance table: S897 "tier B for the claims used here" (its periodization is
the author's own argument; reprint page has no printed page numbers) and S898's
gate evidence — the 88-term count — is "tier B … reported from the author's 2008
monograph and does not re-count". ExecCensusEnd measured the draft mirror at
`tier.A 495` (+2 A). Whether A is defensible per the contract's "original paper"
clause is arguable; what is not arguable is that the row and the entry disagree in
the same landing commit. If the counter ever computes expected tier deltas from the
entry's declared grades, the current rows fail it; if it doesn't, the registry
records a trust grade the consuming entry disavows.

Smallest safe correction: pick one grading. Most contract-consistent: S897 → B
(row+entry agree; census target becomes 494/312/16), S898 → A as *document* tier
with the entry's per-claim B-grade noted only in entry prose (the row tier field
cannot express per-claim grades — flag, not defect).

### F4 — Instrument blind spot: E11 is existence-only, census never back-checks used-by

`usedby_findings()` in `sources-census.sh` (line 539–567) fires E11 only for
`mined` rows whose `used-by` *path* is missing on disk. It never verifies the path
contains a citation of that S-id. ExecCensusEnd's mirror proved it: a *stand-in*
file at the used-by path satisfied E11 with zero content. A landing where the two
rows say `used-by: naming-systems.amend-2026-10-23.md` but the entry cites neither
id still exits 0 — the CITEDLINES leg is the only guard, and it must actually diff
the entry's `source:` lines against the row's used-by, not just count.

### F5 — Census exit-0 is warning-insensitive; existing warnings set the ceiling

Base run: 28×W04 + 4×W01, exit 0. Any landing that *adds* warnings still exits 0.
S898 is safe here (paper ≠ community, tier A); but the claim's "end census exit 0"
is a weak leg — the counter should pin the warning *set* byte-identical to base,
not just the exit code. (ExecCensusEnd did observe "warning set unchanged" on the
mirror — good; make it a leg, not a receipt.)

### F6 — README footer arithmetic is append-only too

Base footer (live block): `Total knowledge entries: 253 … (total 253 files;
directory totals 32/32/41/29/24/95)`. My per-dir recount:
civilizations 95, culture-material 41, linguistics 32, myth-symbol 32, synthesis 29,
verification 24 — vector order is myth-symbol/linguistics/culture-material/
synthesis/verification/civilizations (the r76 footer note "linguistics 30 + 2"
fixes slot 2 as linguistics). Landing must append a *new* live block — convention
keeps older blocks byte-identical — reading `Total knowledge entries: 254`, dir
vector `32/33/41/29/24/95`. Editing the existing block in place would break the
dated-record convention; forgetting the linguistics slot leaves the vector summing
253 against 254 files.

## Confirmed consistent (attacked, did not break)

- **Cell shape**: 820/820 rows NF=13; both staged rows NF=13. No stray `| S###`
  lines outside `## Registry` (lines 26–852; grep total == registry count).
- **Statuses**: vocab {queued,mined,rejected} only; queued/rejected carry
  `used-by: —`; every mined row carries non-`—` used-by; S859/S860 use SKILL.md +
  lesson paths — legal (any existing path), precedent for non-knowledge used-by.
- **Append-only design**: draft entry cites exactly {S897×13, S898×10} — no legacy
  S-ids — so *no* pre-existing row needs `status`/`recheck`/`used-by` edits; the
  diff is a pure 2-line append at S896's tail, preserving id order (E11-ordering
  satisfied only if the entry file exists in the same commit).
- **E04/E12**: no same-document base row for either URL (`grep -i 'lishisuo|onomastica|ijppan'`
  → only S543, a different domain `onomasticafelecan.ro`); staged-ids S897/S903
  map uniquely to D1/D2; misdescribed S934 dedupes to the S898 document, not a row.
- **Date fields**: `opened 2026-10-27` = today; 12 base rows share that opened date
  (S885–S896, rounds 75+76) — the header's opened→lesson lookup stays unique only
  because round-77's search-log note must name "round 77" (r76's entry names
  "round 76"); keep that convention or the gate audit ambiguously picks a lesson.
- **Minor asymmetry**: rows say `recheck 365d`; the entry promises 180d re-open.
  The stricter entry promise governs; flag for consistency, not a violation.

## Impacted axes

C: ROWS (passes counts either way — hence insufficient alone), GATE, EVIDENCE,
CITEDLINES (F4), CENSUS (F5), INDEX (F6), FROZENCFG (tier-delta expectation F3).
F1 maps onto the kill rule "wrong/unopened source or quote" *if landed verbatim*.
All three top findings are fixable pre-freeze cell edits; none requires
re-designing the claim.

## Smallest safe correction (ordered)

1. Rewrite S897 source cell to live-200 truth; fill both rows' anchor/teaches cells.
2. Set S897 tier to B (matches entry grade) or re-grade the entry; then recompute
   the tier-delta the counter asserts (495→494 tier.A if B).
3. Counter legs: byte-identical warning set (F5), used-by↔citation back-reference
   (F4), provenance-token ∈ evidence window (F1), no `DRAFT CELL` literal (F2).
4. Land entry + 2 rows + README block (`254 / 32,33,41,29,24,95`) in one commit;
   end census on the real tree, not a stand-in mirror.

Nothing written outside this report and `/fast/scratch/hyaku/kotodama-r77/CritCensus/`
(scratch: extracted base blob only, deleted before yield).
