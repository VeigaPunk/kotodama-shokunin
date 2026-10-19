- Seat: C10 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C10 — disposition of open item 10 = OI-10 (calibrated numeric rubric undefined)

**Mission** (`reports/round-33/targets.json`, seat C10): "Same as C01 for item 10."
C01 = *disposition open item 1 from K03's canonical table: verify its status quo at
HEAD (pointer still accurate, dated command), classify fixable-now vs carried, and
produce the disposition with evidence; if fixable, add the exact fix draft.*

## 1. Route reconciliation (what this seat first assumed, and the withdrawal)

K03's canonical table (`reports/round-33/calib/K03-open-items.md`) had not landed
when this seat started (`ls reports/round-33/calib/` → empty at 2026-10-19T03:55Z).
This seat therefore reconstructed the ordering from the filed sources and adopted
route R-A — "9 D13 rows + the 3 D11 box-4 readings" — which made slot 10 the box-4
standing reading 3a. **K03 landed mid-seat and binds otherwise**: its §2 table gives
`OI-10 = calibrated numeric rubric undefined (per-axis verdicts only)`, class
`protocol-gap`, pointer `SCORECARD.md:13-14`, and its seat map reads
"**Seat mapping for the C-lane: C01↔OI-01 … C12↔OI-12 in this order**"
(`K03-open-items.md:75`). R-A is **withdrawn**; nothing of it is dispositioned here.
The withdrawal is recorded (rather than silently dropped) so C13 sees one mapping,
not two.

**Collision context, named not absorbed.** C07 — bound by K03 to OI-07 — took the
rubric item as its *primary* disposition (`calib/C07-item-07.md:31-104`); C15
re-keyed that row to OI-10 and listed this fragment as owed
(`calib/C15-ledger-draft.json` → `owed[]`: "OI-10 is dispositioned through C07's
re-keyed primary row; C10's fragment (K03 binds C10↔OI-10) is owed"); C08 flagged
the same collision independently (`calib/C08-item-08.md:32-36`). This fragment is
the **dedicated seat's** independent disposition of OI-10 and a cross-check of
C07's row; §4 states the agreement/disagreement verdict, §5 hands C13 the
duplicate-resolution material. No second disposition class is proposed.

## 2. Item 10 = OI-10 — the item as filed

- K03 row: `OI-10 | calibrated numeric rubric undefined (per-axis verdicts only) | r5 | protocol-gap | SCORECARD.md:13-14` (`K03-open-items.md:71`).
- Filed wording, `SCORECARD.md:11-16`:

> The old 0–10 estimates had no reproducible mapping from evidence to score. They
> remain historical in Git, not new numeric claims. This table records per-axis
> verdicts and checkable observations instead; defining a calibrated numeric rubric
> remains an explicit protocol-conformance gap. Freshness is historically the
> lowest non-retired axis, not a newly computed scalar. A raw file or marker count
> is not a quality score.

- The same gap is restated at `SCORECARD.md:620-624` ("Debts folded into rounds
  9–28: … reproducible numeric axis rubric"), at `reports/round-5/kotodama.md:54`
  ("no calibrated numeric rubric is claimed"), and at the r32 capability inventory
  (`reports/round-32/dossier-d12-capability-inventory.md:79-81`: "**No calibrated
  numeric rubric exists.** The SCORECARD header's explicit protocol-conformance gap
  stands: verdicts and checkable observations, not scores").
- The carry chain: r5 lesson (`corpus/lessons/round-5.md:113`) → r5 calibration
  critic (`reports/round-5/16-calibration-critic.md:75`: "no numeric rubric invented
  this round") → r26 Q-05-3 carry (`reports/round-26/open-questions/C42.md:43-60`)
  → r26 lessons-index row (`corpus/lessons/README.md:163`, status **open**) → r32
  D13 Decision 4 row (`reports/round-32/dossier-d13-operator-decisions.md:136`).

## 3. Status quo at HEAD — re-verified 2026-10-19 by this seat

HEAD = `139e3b662900557afe54f632b468619593dc9fcb` (= declared baseline;
`git rev-parse HEAD`, 2026-10-19T03:55Z). Commands run from the repo root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| check | command | result |
|---|---|---|
| the header gap stands | `grep -n "rubric" SCORECARD.md` | `14:numeric rubric remains an explicit protocol-conformance gap` and `624:reproducible numeric axis rubric` |
| no rubric in the admission bar | `grep -c "rubric" corpus/QUALITY.md` | `0`, exit `1` (file resolves, 1243 bytes / 23 lines) |
| the r26 carry is still open | `grep -n "Q-05-3" corpus/lessons/README.md` | `163: \| Q-05-3 \| whole-corpus header conformance and numeric-rubric debts remain explicit \| corpus/QUALITY.md \| open \|` |
| the carry refuses invention | `sed -n '43,60p' reports/round-26/open-questions/C42.md` | "**carried.** Owner `corpus/QUALITY.md` … **no** numeric rubric … deliberately left open rather than papered over with an invented rubric. Next touch round 27." |
| r5 provenance | `grep -n "numeric rubric" reports/round-5/kotodama.md` | `54:no calibrated numeric rubric is claimed.` |
| the declared next-touch was never taken | `grep -rn "rubric" reports/round-2[7-9]/ reports/round-3[0-1]/ \| wc -l` | `0` |
| the lane contract is scalar-free | `grep -n "scalar" REGIMEN.md` | `39: … No scalar aggregation; a trade is reported, never averaged into an accept.` |

**Verdict: the pointer is accurate at HEAD and the gap stands exactly as filed —
no drift.** The one movement worth naming is *against* closure: the r26 carry's
declared next touch (round 27) was never taken (0 rubric touches across rounds
27-31, command above), so the touch cannot be inherited as "in progress".

## 4. Disposition (dedicated seat C10)

- **id / item:** OI-10 — calibrated numeric rubric undefined (per-axis verdicts only).
- **class:** `carried-with-owner+reason+next-touch` (K03's class `protocol-gap`; **not**
  fixable-now). The alternative `fixed-with-evidence` is unavailable: nothing has
  been fixed, and the r5→r32 chain above is uniform that nothing *should* be
  invented in-lane.
- **owner:** **operator** — the calibration ruling. Artifact pointer-owner per the
  r26 carry: `corpus/QUALITY.md` (resolves; zero rubric matches, so the debt is
  genuinely unrecorded there, not merely uncited).
- **reason:** no calibrated rubric exists; inventing one is refused on the record
  (`reports/round-26/open-questions/C42.md:58-60`); and the round contract itself
  forbids scalar aggregation (`REGIMEN.md:39`), so a numeric rubric is a
  calibration-standard ruling outside lane authority. A lane-authored rubric would
  contradict the contract it would be measuring.
- **next_touch:** the operator's calibration ruling; until it is issued, the item is
  re-checked at the next regimen-opening calibration audit. **The touch must be
  re-declared, not inherited** — r26 declared "next touch round 27" and rounds
  27-31 took it zero times (§3 command).
- **fix_draft:** **none owed.** K03 assigns bounded fix drafts to OI-04/05/06 and
  OI-07's N1 only (`K03-open-items.md:75-77`); OI-10 is a carry candidate. No rubric
  skeleton is drafted here, deliberately: drafting one would be the papering-over
  the filed record refuses. C14's scope is unaffected.

**Cross-check verdict on C07's re-keyed row (`calib/C07-item-07.md:31-104`,
carried into `C15-ledger-draft.json` rows[9]): AGREE.** Class, owner, reason and
next-touch match this seat's independent disposition; my §3 commands reproduce its
three status checks (`SCORECARD.md:14`; `corpus/QUALITY.md` grep = no matches;
`README.md:163` = open; r27-r31 touches = 0). Two additions this seat makes and
C07/C15 did not carry:

1. `REGIMEN.md:39` — the contract's own no-scalar rule, which is the strongest
   in-lane reason the item cannot be closed by the lane (C07's reason rests on the
   r26 refusal alone).
2. `SCORECARD.md:620-624` — the r8-era debt-folding row that names the rubric debt
   independently of the header sentence; it confirms the gap predates and outlives
   the r26 carry.
   One precision note: Q-05-3 bundles **two** debts (whole-corpus header conformance
   *and* the numeric rubric). OI-10's subject is the rubric half; the header-conformance
   half remains inside the same carry row and is not dispositioned by this fragment.

## 5. Duplicate handling for C13 / C15 / integrator

- OI-10 is dispositioned twice (C07's primary row; this fragment). The two agree in
  every field — this is a **mapping collision** (C07 was bound to OI-07), not a
  contradictory class. Recommend C13 record it as such with C10 as the dedicated row
  of record for OI-10 and C07's row as the cross-check source; C15's ledger may keep
  its current row and swap `source_fragment` to this file, or keep both with the
  collision named. No re-keying of any other row is proposed here.
- If the integrator prefers C07's row verbatim, this fragment's §3 table and the two
  additions in §4 are the only deltas to fold in; nothing else in it needs carrying.
- Nothing in this fragment edits a filed byte, and no promotion/closure/canon
  language appears in it.

## Owed

none — the K03 dependency landed mid-seat and is folded in above; C13's duplicate
reconciliation is C13's artifact, not this seat's.

## Citations

Paths read at HEAD `139e3b6` (2026-10-19):

- `reports/round-33/targets.json` (C10, C01 seat objects)
- `reports/round-33/claims.json` (claim C before/after/thresholds)
- `reports/round-33/calib/K03-open-items.md:1-78` (count conventions; canonical
  twelve table `:60-73`; OI-10 row `:71`; seat map `:75`; fix-draft scope `:75-78`)
- `reports/round-33/calib/C07-item-07.md:1-104,192-232` (primary rubric row,
  findings, citations)
- `reports/round-33/calib/C08-item-08.md:28-40` (collision flag)
- `reports/round-33/calib/C15-ledger-draft.json` (`rows[9]` = OI-10; `owed[]`)
- `SCORECARD.md:11-16,620-624`
- `corpus/QUALITY.md` (full, 23 lines)
- `corpus/lessons/README.md:163`; `corpus/lessons/round-5.md:113`
- `reports/round-5/kotodama.md:54`; `reports/round-5/16-calibration-critic.md:75`
- `reports/round-26/open-questions/C42.md:43-60`
- `reports/round-32/dossier-d12-capability-inventory.md:79-81`
- `reports/round-32/dossier-d13-operator-decisions.md:136`
- `REGIMEN.md:39`

Commands run (2026-10-19, repo root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
- `grep -n "rubric" SCORECARD.md` → `14`, `624`
- `grep -c "rubric" corpus/QUALITY.md` → `0` (exit 1)
- `grep -n "Q-05-3" corpus/lessons/README.md` → `163` (status `open`)
- `grep -rn "rubric" reports/round-2[7-9]/ reports/round-3[0-1]/ | wc -l` → `0`
- `grep -n "numeric rubric" reports/round-5/kotodama.md` → `54`
- `grep -n "scalar" REGIMEN.md` → `39`
- `sed -n '43,60p' reports/round-26/open-questions/C42.md` → the carry text quoted in §3
- `sed -n '79,81p' reports/round-32/dossier-d12-capability-inventory.md` → the inventory reading quoted in §2
- `ls reports/round-33/calib/` at 2026-10-19T03:55Z → empty (K03 absent at seat start)

Superseded first-pass material: an earlier revision of this file dispositioned the
box-4 standing reading 3a (route R-A) and cited `reports/round-24/promotion-review.md:222-232`,
`reports/round-24/box4-bleed.md:46-56,137-149`, `examples/culture-d4/typed-labels.d4.yml:165`,
`tools/d2-typed-labels.py:2997` and `tools/assemble-d4-typed.py --check` (exit 0) /
`--selftest` (12/12) for that mapping. That revision is withdrawn per §1; the
commands remain reproducible but no disposition rests on them here.
