# CritCaCounterVacuity — attack on claim Ca's 12 legs (vacuity class)

Seat: L1Kotodama72.CritCaCounterVacuity (leaf, no dispatch). Round 72, wave 1.
Frozen claims: `reports/round-72/claims.json` (Ca, 12 legs). Base: `b60c7b1`.
Scope: four scenarios applied leg-by-leg; each vacuity named with the exact leg,
local evidence, impacted axes, and the smallest receipt-level fix. No lane bytes
mutated; no tools installed (no install needed; pacman paused host-wide).

Method note: `reports/round-72/accept-ca.py` does not exist yet (executors author
it); the round-71 counter (`reports/round-71/accept-ca.py`) sets the house idiom
(per-leg `LEG PASS/FAIL` prints, `--lands`, materialized-clone protocol per
QUALITY 19). All findings below are therefore stated as *requirements on the
counter and its receipt*, which is where every vacuity is closable without
touching the frozen leg text.

## Verified local evidence (all against b60c7b1 / 1d1b4325)

- Three superseded LOG.md round-71-entry lines, old text at `1d1b4325:LOG.md`,
  new text at `b60c7b1:LOG.md` (in-place rewrites, ancestors of base):
  - :4267 header — old `records '<RECORDS>'.` → new `records '1d1b4325'; final
    receipts '3764c2df' / re-stamps '7179d6d6'.` (rewritten at 1721fbd)
  - :4274 Item 10 — old `renumber map (S861→S992 by document)` → new
    `(S874→S1005 by document)` (rewritten at 27db4ce/99e3d63)
  - :4275 Misroot — old `Fleet status lists only driver state and
    orchestrator-owned scratch; no lane file misplaced.` → new
    `Seven wave-1 fetch artifacts (s795.pdf, s796.pdf, s804/s814/s816/s817.html,
    s820.pdf) … fleet copies deleted at 'ccadb59' …` (rewritten at 1721fbd)
- Fleet report (fleet root, OUTSIDE the lane repo):
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-71/kotodama.md`
  :57 = `map S861→S992 recorded for adoption. Census: exit 0 at start`;
  :61 = `**Assimilation: none** … renumber map by document (S861→S992) …
  Quarantine verdicts: 21 rows (PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5).`
- Tally truth: `reports/round-71/telemetry/quarantine-verdicts.md:36` —
  `Tally: PRESENT 10 · REFUSED 7 · UNVERIFIABLE 4 = 21 (re-derived by
  RevQuarantine; S816→REFUSED, S778→PRESENT)`. Filed 10/6/5 lives at fleet
  report :61, `LOG.md:4270` (Claim Ca line), lesson :80 and :95.
- Fourth stale line, NOT in LOGCORR's frozen three: `LOG.md:4270` records
  `Item-10 quarantine table 21 rows (PRESENT 10 / REFUSED 6 / UNVERIFIABLE 5)`.
- `corpus/lessons/round-71.md` stale: :8 `wave 2: 41 seats (below). Round
  total 78 seats`; :80 `(PRESENT 10 · REFUSED 6`; :95 `verdicts 10/6/5
  re-confirmed`. w2 seat truth: `.ufo/waves/round-71/w2/spec.json` items = 40.
- Capoeira at base: `corpus/lessons/round-71.md:36` — `Capoeira (no capture;
  flip: Flamenco)` → a whole-lesson `grep -i capoeira` matches AT BASE.
  `LOG.md` has no capoeira mention at base.
- `corpus/QUALITY.md` at base: `grep -c '^20\. ' = 0`, `'^21\. ' = 0`
  (criterion 20 exists only as the uncommitted worktree diff).
- `reports/round-71/telemetry/measures-ca.txt` committed at base; top block
  pairs counter sha `1ce25fb9…` with stamp `64da9e14…`; true counter
  `f706aacd…` preserved below `# original bytes preserved below`.
- w2 files: 2 tracked-at-base, modified in worktree (`Filler30.md`,
  `RevReceipts.md`); 5 untracked (`CritTrends.md`, `Filler28.md`,
  `Filler36.md`, `RevCounterCa.md`, `RevEntry.md`).
- Renumber map: `.ufo/waves/round-71/assimilation/id-renumber-map.json` —
  at `65ff1510`: `next_free S861`, `span S861→S992`; at `99e3d63`:
  `next_free S874`, `span S874→S1005`.
- Lane `SCORECARD.md` (1395 lines): round rows through the round-70 corrections
  table and round-70 trend-correction row (:1362–1387); NO round-71 rows yet.
  V70-4 precedent: corrections land as SCORECARD rows.

## Scenario A — corrections filed, round-72 fleet report never names :57/:61

Pass set under a correct counter: 11/12 (all but REPORTCORR). The scenario is
a genuine REPORTCORR failure, not itself a vacuity — the vacuity is in how
REPORTCORR can be implemented green anyway:

- **Vacuity A1 (out-of-repo authority).** The filed fleet report lives at the
  fleet root, outside `--root .`. A counter that checks a lane-local copy, its
  own receipt text, or any file the lane controls, certifies a correction the
  filed artifact never received. REPORTCORR passes; the canonical report stays
  wrong. False provenance, calibration axis.
- **Vacuity A2 (no filed-bytes guard).** Nothing in the legs verifies the
  round-71 fleet report still says S861→S992 at :57/:61. A seat that rewrites
  the filed report in place (kill-rule violation) leaves REPORTCORR-able text
  in the round-72 report; only the kill rule (judge-side) catches it.
- **Receipt-level fix.** accept-ca.py REPORTCORR must (1) open
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotodama.md` and
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-71/kotodama.md` by absolute
  path and fail closed if unreadable; (2) require in the round-72 report the
  tokens `:57`, `:61`, and `S861→S992` (accept both `→` and `->` spellings);
  (3) assert the round-71 report's lines 57 and 61 still contain `S861→S992`
  and its sha256 equals the base-era value (filed bytes untouched). Receipt
  prints both sha256s and the two awk-extracted lines.

## Scenario B — LOGCORR names only 2 of the 3 superseded lines

Pass set under a correct counter: 11/12 (LOGCORR fails). Vacuity:

- **Vacuity B1 (partial-credit grep).** One alternation grep (`S861|<RECORDS>|misroot`)
  or an existence check on "a corrections line" passes 2-of-3. The frozen leg
  text enumerates three lines; the counter must not collapse them.
- **Vacuity B2 (unscoped grep).** Old strings survive in git history, not in
  the worktree; but `S861→S992` and `capoeira`-class tokens appear elsewhere in
  LOG.md (e.g. round-72's own report-naming). A whole-file grep can match text
  unrelated to the round-72 entry.
- **Receipt-level fix.** Three independent sub-legs, each scoped to the text of
  the `## Round 72` entry at <lands>, each requiring old AND new:
  LOGCORR-1 `S861→S992` + `S874→S1005`; LOGCORR-2 `<RECORDS>` + `1d1b4325`
  (plus `3764c2df`/`7179d6d6`); LOGCORR-3 `no lane file misplaced` +
  `Seven wave-1 fetch artifacts`/`s795.pdf`/`ccadb59`. Strongest form (kills
  B1 structurally): the counter derives the truth itself —
  `git diff 1d1b4325..b60c7b1 -- LOG.md` restricted to the round-71 entry hunk
  yields exactly three changed lines; require the round-72 entry to quote each
  removed line verbatim and name each replacement. 2-of-3 then cannot pass.
- **Residual finding (beyond frozen scope).** `LOG.md:4270` (Claim Ca line,
  tally 10/6/5) is a fourth stale line the frozen three do not cover; every
  leg can pass while a filed LOG statement contradicts the table (10/7/4).
  Smallest safe correction: the round-72 report names it, and the counter's
  receipt prints it as a named residual so the judge sees the divergence;
  do not rewrite LOG.md:4270 (kill rule).

## Scenario C — QUAL21 committed, Capoeira evidence not appended

Pass set under a correct counter: 11/12 (CAPOEIRA fails; QUAL21 is independent
and passes). Vacuities:

- **Vacuity C1 (base-true whole-file grep).** `grep -i capoeira
  corpus/lessons/round-71.md` matches at base (:36 `Capoeira (no capture; flip:
  Flamenco)`). A whole-lesson or whole-file check passes with ZERO round-72
  correction appended. The single most likely vacuous green in this claim.
- **Vacuity C2 (one-site check).** The leg is two-site: lesson corrections
  section AND LOG round-72 entry. Checking either passes the missing half.
- **Vacuity C3 (prose-only evidence).** "live 200 + CDX captures under
  capoeira-circle-00892" asserts fetched bytes; with no fetch receipt the
  correction is unverified text (QUALITY 12 territory).
- **Receipt-level fix.** CAPOEIRA requires, all in the counter: (1) the slug
  `capoeira-circle-00892` in the `## Corrections (round 72)` section of the
  lesson (section-scoped, not file-scoped); (2) the same slug in the LOG round-
  72 entry; (3) a committed fetch receipt (e.g.
  `reports/round-72/telemetry/capoeira-cdx.txt`) containing a live `200` for
  the source URL and ≥1 CDX capture line naming `capoeira-circle-00892` with
  timestamp, cited by path from both the lesson and LOG. All three conjuncts
  print in the receipt.

## Scenario D — APPENDONLY runs over a file set missing SCORECARD.md

Pass set: 12/12 — APPENDONLY passes vacuously. Worst scenario: a fully green
claim while a watched-adjacent record is rewritten.

- **Vacuity D1 (unchecked ledger).** The frozen set is {LOG.md,
  corpus/lessons/round-71.md, corpus/QUALITY.md}. Lane `SCORECARD.md` is the
  per-round claims/trend ledger with an explicit corrections precedent
  (round-70 corrections table + trend-correction row, :1362–1387; V70-4 landed
  exactly such a row). A round-72 correction row is plausible work; an in-place
  edit of SCORECARD's filed rows is invisible to every leg. Duplicate authority:
  SCORECARD rows contradicting LOG/lesson would survive a PASS.
- **Vacuity D2 (sibling gap: measures-ca.txt).** CASTAMP's target
  (`reports/round-71/telemetry/measures-ca.txt`) is also outside APPENDONLY; if
  the re-stamp rewrites the top block instead of appending below a marker, no
  leg sees it. The wrong-sha defect this claim exists to fix would be re-born.
- **Vacuity D3 (dirty-worktree grading).** `git diff b60c7b1..<lands>` over
  committed trees is sound only if the counter runs inside a materialized
  clone at <lands> (QUALITY 19); run in the live worktree it can be fed staged
  fiction.
- **Receipt-level fix.** accept-ca.py: (1) runs the frozen three-file `-U0`
  no-removed-lines diff exactly as worded; (2) CASTAMP additionally diffs
  `reports/round-71/telemetry/measures-ca.txt` base..lands and requires
  zero removed lines plus the marker `# original bytes preserved below` and
  the original block verbatim below it; (3) APPENDONLY additionally runs
  `git diff --name-only b60c7b1..<lands>` over all tracked files and prints it;
  every changed tracked file must be accounted for — the three append-only
  files, the seven w2 seat files (W2FILES), measures-ca.txt (CASTAMP), or new
  files under `reports/round-72/` / `.ufo/waves/round-72/`; `SCORECARD.md` must
  show zero diff (or, if a correction row is landed, pure appends disclosed in
  the receipt). (4) the receipt carries the QUALITY 17/19 header lines
  (stamped/evaluated/measured revision, tree, counter sha) pinning <lands>.

## Summary table

| Scenario | Legs passing (correct counter) | Vacuous green risk | Fix locus |
|---|---|---|---|
| A: report never names :57/:61 | 11/12 (REPORTCORR fails) | A1 out-of-repo authority; A2 filed bytes unguarded | counter reads fleet root by absolute path; sha + line assertions |
| B: LOGCORR 2-of-3 | 11/12 (LOGCORR fails) | B1 partial grep; B2 unscoped grep; + unstated 4th line LOG:4270 | three old→new sub-legs or self-derived `git diff 1d1b4325..b60c7b1` hunk match; residual printed |
| C: QUAL21 yes, Capoeira no | 11/12 (CAPOEIRA fails) | C1 base-true grep (`capoeira` at lesson:36); C2 one-site; C3 prose-only | section-scoped slug check on both files + committed fetch receipt |
| D: APPENDONLY set missing SCORECARD.md | 12/12 (all pass) | D1 SCORECARD rewrite invisible; D2 measures-ca rewrite invisible; D3 worktree grading | whole-tree changed-file accounting + CASTAMP pure-append sub-check + clone protocol |

Every fix is counter/receipt-level; none rewords a frozen leg. The one item the
frozen text cannot reach (LOG:4270 tally) is a judge-visible residual, not a
leg defect — flagging, not failing.

Report: .ufo/waves/round-72/w1/CritCaCounterVacuity.md
