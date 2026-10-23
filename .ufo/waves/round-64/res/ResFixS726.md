# ResFixS726 — RF2 repair (S726 tier A→B, abstract-scoped)

Seat: `kotodama-r64.ResFixS726`, leaf. Round 64, residual-repair call. Lane:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated).

Axes: **calibration** (tier authority must match the evidence actually opened and anchored) and
**operability** (row shape/counter constraints preserved). Each move was kept only if it improved
one axis and harmed none.

Write set: `.ufo/waves/round-64/rows/ScribeRowS726/row.txt` (the only lane file edited by this
seat) and this report. No fleet/sibling/lane-jj/lane-index mutation, no commit, no counter run
other than the assigned `check-rows.py`. No packages installed or updated; pacman not invoked.

## Finding addressed (RF2)

`CriticRowsFinal.md` RF2: the row anchors the **ERIC record abstract** (`ERIC record abstract,
numbered claim (1)`) while tier A claimed Ochs and Schieffelin's foundational paradigm itself.
Smallest safe correction, verbatim: "B for the abstract-reported claim, keeping the current quote
and benefit". Assigned wording adds: scope cell explicitly scoped to the abstract-reported claim.

Basis: `corpus/QUALITY.md:29` criterion 6 — "publisher descriptions and abstracts are tier B for
substantive claims about a work, even when accurate; reserve tier A for sources primary or
authoritative for the exact scope." Precedent `corpus/SOURCES.md:131` (S102) is B with the abstract
named in the scope cell ("the paper's reported historical tendency in ASL (journal abstract via
ERIC; JSTOR full text blocked, Cambridge Core HTTP 429)"); S044–S046 are the superseding-row
correction pattern.

## Old vs new cells (11-cell row; only cells 3 and 4 changed)

| # | Field | Old | New |
|---|---|---|---|
| 3 | tier | `A` | `B` |
| 4 | scope | `Ochs and Schieffelin's foundational language acquisition/socialization paradigm` | `ERIC abstract-reported claim of Ochs and Schieffelin's foundational language acquisition/socialization paradigm` |

Byte-identical, verified against the critic's pre-repair snapshot
(`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/CriticRowsFinal/row-snapshot.json`, `rows.S726.cells`):
cells 0,1,2,5,6,7,8,9,10 all SAME; all four labelled lines (`BULLET`, `VERIFY`, `CAPTURE`,
`ACCESS`) SAME. The bullet `- The process of acquiring language is linked to social membership,
giving worldbuilders community-based learner arcs. (S726)` is untouched, as are status `mined`,
opened `2026-10-23`, recheck `180d`, used-by
`corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, the quote (19 normalized
words), teaches (13 words ≤ 25), and both URLs/capture.

The scope wording mirrors the sibling RF3 repair pattern (`ResFixS737.md`: "ERIC abstract-reported
operational definition of …"), giving one convention for abstract-only rows rather than two.

Row SHA-256: pre `da1dda3b407e6597b4d84bcb13e93a1e1eed2f981431e80c2d7116d5105b9522` (matches the
critic's finding-row snapshot, so no concurrent drift before the edit); post
`cda347814c7c2cc440f6ae3bc361090427defc13de02745f8f14dc4555d5f9c7`.

## Checker result

```
$ python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
S726 OK
CHECK-ROWS: 32/32 clean
exit=0
```

One run, no transient failure (full other-seat output captured at
`/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS726/check-rows-post.txt`).

## Independent corroboration of the tier premise

Plain GET, default client UA, HTTP 200 —
`https://eric.ed.gov/?id=ED252065` (body retained at
`/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS726/eric.html`, 12 017 bytes). The page is a
record summary: it carries `Abstract` and `Descriptors` sections, the `(MSE)` marker, and a
separate `Full text` link; it contains the anchored sentence ("deeply affected by the process of
becoming a competent member of a society"). That is an abstract for a work, not the work — B is
the correct claim-scoped tier. The same conclusion is already recorded independently at
`.ufo/waves/round-64/w2/B2ReviewRowS726.md:30,50`.

## Behaviour / invariant checks

- Row shape: 11 cells, no `|` inside any cell (`|` scan of all 11 cells: none), single `ROW:` line,
  four labelled lines in unchanged order.
- Counter compatibility (`reports/round-64/accept-c.py:199-202`): ROWS accepts `A` or `B`; there is
  no tier-count clause anywhere in `accept-c.py` (grep `tier` → only the membership test and
  docstring), and claim C's statement declares row count/registry arithmetic only — no A/B split
  for S718–S743. The A13/B11 split the Ca claim names is the round-63 headgear census
  (`accept-ca.py:16`), untouched by this row.
- Integration path: `integrate-w2.py:127-166` (`collect_contributions`) reads
  `rows/ScribeRow*/row.txt`; `parse_contribution` (`:68-125`) validates labels, 11 cells,
  `status=mined`, and the exact used-by path, and does **not** constrain the tier beyond the two
  accepted values. The edited row satisfies every check it performs (labels unchanged, bullet
  prefix/suffix unchanged, used-by exact).
- Dependent entry: `rows/ScribeEntrySkeleton/entry.md` contains no reference to S726, no "primary"
  or tier assertion, so no dependent claim text needs updating for the downgrade.
- URL identity: unchanged, so the checker's duplicate-URL grouping is unaffected
  (`?id=ED252065` ≠ `?id=ED149852`, per `RegFinalAudit.md:150`).

## Findings (this seat's own repair, plus residual risk seen while checking)

**No blocking or in-scope correctness defect remains.** RF2 is resolved: tier is B and the scope
cell now names the ERIC abstract as the origin of the claim, so the filed authority no longer
exceeds the opened evidence.

- **LOW-1 (assembly hazard, not introduced here).** `.ufo/waves/round-64/stage/rows.txt` (mtime
  20:01) still holds `| S726 | … | paper | A | …`, because the older helper `integrate.py:1-9`
  reads the **wave-1 cache** `~/.cache/hyaku/kotodama-r64/` and rewrites that stage file
  (`integrate.py:150-160`). Re-running `integrate.py` after the repairs would regenerate all rows
  from unrepaired wave-1 drafts and silently discard RF1–RF5. Final assembly must run
  `integrate-w2.py --rows-dir .ufo/waves/round-64/rows`, which reads the repaired contributions.
  Recommend the integration owner either retire `integrate.py`/its stage file or assert the stage
  snapshot's hashes against `rows/` before writing `corpus/`.
- **LOW-2 (stale receipts by design).** `w2/RegFinalAudit.md:15,51` and the hash table in
  `w2/CriticRowsFinal.md` record S726 as A with the pre-repair SHA-256. Those are honest
  pre-repair snapshots and must not be edited; any final receipt or census must recompute tier and
  hash from `rows/ScribeRowS726/row.txt` (post SHA-256 above) rather than restating A.
- **INFO-1 (wording, no action).** The adjective `foundational` is retained. It describes the work
  in the scope cell, matching the descriptor style of S044–S046 and S102 ("the book's stated
  programme"), and the named correction did not ask to drop it; dropping it would widen this
  seat's change beyond tier + abstract scoping. Scribing may trim it if the registry prefers bare
  descriptive scope.

## Verification gaps

- Locator reproducibility: `VERIFY: LOCATED` is not reproducible through the lane locator today —
  eric.ed.gov resets its Firefox UA (`w2/B2ReviewRowS726.md:30,50`). Pre-existing and outside
  RF2's smallest correction; S726 is outside `accept-c.py`'s frozen LIVE_IDS subset, so no counter
  leg probes it. I confirmed the page only by plain GET (HTTP 200), not by the locator.
- The 32/32 line is point-in-time while sibling seats edit other rows; it was clean on the single
  assigned run including S726 OK.
- I did not run `accept-c.py`, `integrate-w2.py`, or any mutation/census tool (not assigned; they
  would write lane or report paths), and I did not re-verify sibling rows' content.

## Custody

Scratch `/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS726/`: `post-row.txt` (post-repair row,
SHA-256 `cda3478…`), `eric.html` (plain-GET body), `check-rows-post.txt` (full checker output).
Report: `.ufo/waves/round-64/res/ResFixS726.md`.
