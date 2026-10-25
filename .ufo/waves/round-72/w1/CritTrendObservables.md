# Round-72 trend verdicts — pre-data declaration (CritTrendObservables)

Scope: declare the only defensible trend verdicts for round 72 BEFORE data, per QUALITY.md
criterion 20 (committed this round as leg QUAL20). Claims Ca (calibration) and C (coverage)
are frozen at `reports/round-72/claims.json`. All repo reads at base
`b60c7b140c5350caa7d1073711f14092541533f0` + current worktree; verified pre-data facts:

- `git show b60c7b1:corpus/QUALITY.md` matches `^20\. ` 0 times and `^21\. ` 0 times —
  criterion 20 was authored in round 71 but never committed; no criterion 21 exists.
- `corpus/lessons/round-72.md` does not exist at base; no `*heritage-taxonomy*` file exists
  anywhere in the lane worktree at base (staged copies live only under shokuknow).
- Staged entry headers (`shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/`
  `heritage-taxonomy-models.md:1-21`, `…amend-2026-10-24-r13.md:1-15`): base entry cites staged
  S863 (ihchina.cn) + S867 (bunka.go.jp) with `verified-at: 2026-10-23`; the amend cites staged
  S967 (Wayback capture of the ihchina register) and is explicitly "an amendment to the
  heritage-taxonomy entry … it changes no category name and withdraws no claim".
- The falsified round-71 Capoeira reject reason ("no Wayback capture under that URL",
  `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md:40`) is the K71 defect that grounds QUALITY 21
  (`claims.json` Ca before-text: "falsified by the canonical-slug captures").

## Verdict table the L1 must file (pre-data, conditional on claims passing at `<lands>`)

| Trend | Verdict | Fires on (observable) | Pre-data condition | If condition fails |
|---|---|---|---|---|
| **expansion** | **improved** | Claim C: net new admitted `knowledge/` entries on verified uncovered ground, each citing mined rows — LEARNING.md expansion clause | C legs ENTRIES/ROWS/REPOINTED/GROUND hold: two entries with full header; exactly S874/S875 added, both `mined`; every `source:` citation names a row ≥ S874 with matching URL; gap sweep re-run at the 797-row registry returns 0 owners; kill rules clean (no quarantine-REFUSED citation; both sources opened 2026-10-25) | C fails → **unchanged**. An entry admitted and later found under its bar → **harmed** (kill rules + CITEDLINES + census foreclose this) |
| **quality** | **unchanged** | none — LEARNING.md quality clause (re-verified/deepened/superseded entry) does not fire | Nothing in Ca or C re-verifies, deepens, or supersedes a standing corpus entry: Ca is records/instrument repair (criterion 20: calibration, never a quality observable); C's two entries are net-new (expansion); the amend co-admitted with its base is one admission event, not a deepening of a pre-existing entry | Only an actual re-check failure of a standing entry (left unmarked) could move this, and none is in scope → would be **harmed** |
| **discernment** | **improved** | QUALITY 21: a disagreement becomes a lesson that adds a grounded QUALITY.md criterion — LEARNING.md discernment clause b | Ca legs QUAL21 + CAPOEIRA hold: criterion 21 committed (CDX canonical-slug probe before ruling "no capture"; every Gate reject records its URL) AND the Capoeira correction is recorded as a lesson (`corpus/lessons/round-71.md` "## Corrections (round 72)" + LOG.md round-72 entry) AND criterion 21's text names that grounding | QUAL21/CAPOEIRA fail → **unchanged**. Criterion 21 lands with no lesson named → **harmed** ("a criterion added with no lesson behind it") |

Contingent corroboration (not the basis): if the round-72 hyaku non-author closure agrees with
the round-72 gate on ≥1 admit AND ≥1 reject (claim C GATE leg records both), discernment clause a
fires independently. Pre-data it cannot be confirmed; do not file on it.

## Why these are the only defensible verdicts

### expansion — improved (claim C fires it)

- LEARNING.md: expansion improves on "net new admitted entries on uncovered ground, each citing
  its coverage-map row". Claim C is exactly that event: 0 `*heritage-taxonomy*` files and 0
  registry rows naming ihchina.cn / bunka.go.jp at base (`claims.json` C before-text); the
  staged base entry itself records the gap sweep returning 0 over the registry
  (staged `heritage-taxonomy-models.md`, "gap filled" header field).
- ROWS leg pins S874/S875 to status `mined` and REPOINTED leg pins every `source:` citation to a
  row ≥ S874 whose URL matches — the "each citing its coverage-map row" half of the observable.
  The staged citations (S863/S867/S967) are re-pointed by document, not arithmetic.
- One vs two entries is immaterial: one net new admitted entry on uncovered ground fires the
  observable; the amend counting as a second entry only strengthens the firing.

### quality — unchanged (nothing fires it)

- Criterion 20 (its text at `corpus/QUALITY.md:61` in the worktree) is explicit: record/instrument
  repairs — receipt headers, pointer fixes, quote trims, dispositions, re-stamps — are calibration
  work, never quality. Ca's entire K71-1..K71-8 correction set is in that class.
- Claim C admits new entries. New entries are the expansion observable; the round-71 precedent
  filed exactly this shape as "expansion improved / quality unchanged" with one new entry
  (`.ufo/reports/round-71/kotodama.md:63-67`).
- Strongest counterexample tested: the amend is a genuine deepening of the base entry (adds the
  register's dated states, resolves round 12's CANNOT-ANSWER §4.3, fresh `verified-at`). Rejected:
  the base entry is not a standing corpus entry — both files are admitted in the same event, so
  the deepening is inside the admission, not an event over the pre-round corpus. Counting it would
  double-count every admission that ships with an amendment and saturate the quality trend
  prematurely. LEARNING.md's quality phrasings ("a weaker entry is superseded", "stale entries
  re-verify") both presuppose pre-existing entries.
- QUALITY 20/21 additions are discernment-side events, not entry quality.

### discernment — improved (QUALITY 21 fires it; the K71 corrections route the lesson)

- Clause b: "a disagreement becomes a lesson that adds a grounded QUALITY.md criterion." Chain:
  filed round-71 reject reason "no Wayback capture under that URL" (internal seat record,
  `ScoutOpenSourcesC.md:40`) is falsified by CDX canonical-slug captures
  (`capoeira-circle-00892`) — a disagreement between the filed gate record and fetched ground
  truth → becomes a lesson (CAPOEIRA leg: correction appended to `corpus/lessons/round-71.md`
  Corrections + cited in LOG.md round-72) → criterion 21 added (QUAL21 leg).
- Precedent that internal recurrence is valid grounding: criterion 20 is self-described as
  "Grounded in round-70 verifier spot-check §5 (V70-4) and its recurrence in round 71
  (CritTrends)" (`corpus/QUALITY.md:61`; `corpus/lessons/round-71.md:58`). CritTrends was a lane
  seat. The lane's canon already accepts a records-vs-truth discrepancy with a lesson record as
  grounding; clause b does not require the disagreement to come from outside.
- False-provenance trap rejected: criterion 20 being COMMITTED in round 72 (QUAL20 leg) is not a
  round-72 discernment event — it was authored round 71, grounded in round-70/71 lessons. Only
  QUALITY 21 counts for round 72. Citing criterion 20's commit as round-72 discernment is exactly
  the "premature saturation" pattern criterion 20 exists to stop.
- Clause a (gate agreed by an outside spot-check on admits AND rejects): C's GATE leg records
  ≥1 admit and ≥1 reject with URL, date, ≤25-word quote — the sample exists — but agreement by a
  non-author must be recorded post-data. File it as corroboration only if the closure lands.

## Named defensible alternatives (and why they lose)

1. **quality — improved (amend deepens base entry).** The only serious rival on quality. It loses
   on the pre-existing-entry requirement and the round-71 precedent, but if the canonical judge
   reads "deepened" without the pre-existing qualifier, this becomes arguable. The L1 table should
   state the basis ("no pre-existing entry re-verified/deepened") so the filing itself blocks the
   misreading.
2. **discernment — unchanged (strict reading: self-discovered records defect is not a
   "disagreement").** Loses on clause b's plain text and criterion 20's internal-recurrence
   precedent — BUT it wins automatically if criterion 21 lands without naming its lesson, or if
   QUAL21/CAPOEIRA legs fail. This is the fallback row, not the primary.
3. **discernment — improved via criterion 20's commit.** Not defensible: false provenance
   (round-71 artifact; round-72 event is the commit = records repair, Ca scope).
4. **Any "harmed" verdict.** No evidence pre-data: no admitted entry is set up to fail its bar,
   and the only harmed trigger in scope is an ungrounded criterion 21 — a fixable defect, below.

## Smallest safe corrections

1. **Criterion 21's text must name its grounding lesson** (e.g. "Grounded in the round-71
   Capoeira reject defect; correction recorded in corpus/lessons/round-71.md Corrections
   (round 72)"), mirroring criterion 20's self-grounding style. Without this, QUAL21 can pass its
   leg while the discernment filing flips to harmed ("criterion added with no lesson behind it").
2. **The L1 trend table must credit only QUALITY 21 for discernment** — not QUALITY 20's commit,
   not the K71 records repairs (quality), not registry growth (expansion already covers the
   entries; SOURCES row growth alone is not expansion per V70-4's correction).
3. **If claim C fails at `<lands>`, expansion must be re-declared unchanged** (the entries were
   not admitted); if Ca fails, discernment reverts to unchanged and quality stays unchanged.
4. Keep the filed table conditional language ("fires at `<lands>` if legs hold") so a failed claim
   cannot leave a stale `improved` on record.

## Evidence index

- `LEARNING.md:31-44` (fleet root) — the three trends table; quality and discernment clauses.
- `corpus/QUALITY.md:61` (worktree) — criterion 20 text; committed count 0 at `b60c7b1`.
- `reports/round-72/claims.json` — Ca legs QUAL20/QUAL21/CAPOEIRA/APPENDONLY/LESSONCORR;
  C legs ENTRIES/ROWS/REPOINTED/GROUND/GATE/REJECTS + both kill_rules.
- Staged entries under `shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/`
  (read-only) — headers and the amend's self-described scope.
- `.ufo/reports/round-71/kotodama.md:63-67` — round-71 filed verdicts (precedent shape).
- `corpus/lessons/round-71.md:58` — trend-observables row; criterion 20 grounding.
- `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md:40` — origin of the falsified Capoeira reject
  reason (internal seat record; the K71 correction's disagreement source).

No tools installed or updated this seat (read-only review; nothing fetched).
