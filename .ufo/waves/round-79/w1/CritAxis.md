# CritAxis — round-79 W1 axis-labeling review

Seat: CritAxis (critic, lane-local, no dispatch). Base: `44f76d456c1b326a71ffdb381590af825cbf11be`.
Scope: the draft's axis labeling only — O as capability vs Ca as calibration-records,
and the freshness-paused disclosure. Raw probe output:
`.ufo/waves/round-79/w1/stage/CritAxis/receipts/axis-evidence-probe-raw.txt`
(row blobs: `base-S884-row.txt`, `r78-S884-row.txt`). No lane file edited; no git/jj
mutation; scratch `/fast/scratch/hyaku/kotodama-r79/CritAxis` removed after copying.

Method: read `CLAIMS-DRAFT.md`, corpus/QUALITY.md (7–29), fleet `AXES.md`, and the
exact committed files the draft's labels rest on; ran one read-only probe (receipts
preserved). No build/lint/tests beyond the probe; no counter implementation checked
beyond reading committed sources.

---

## F1 — O's before-state "base: absent" is false provenance for the guard class (fixable)

Draft: "acquire a bounded ledger-token guard for this lane's calibration records…
The target is one working guard (base: absent)".

Committed base state contradicts "absent" as a class:

- `reports/round-74/accept-ca.py` (2,847 lines at base) already is a bounded
  ledger-token guard: `OBSERVE_ALLOW` argv allowlist closing echo/printf/interpreter
  channels (`:166`, refusal at `:815-817`); `LEDGER` leg re-running `observe_cmd`
  argv in a clone at base; `BASEMISMATCH` leg cross-checking recorded
  `observed_at_base` against the re-run observation (`:1137-1199`); `APPENDONLY`,
  `STAMP`, `FROZENCFG` legs; red-befores `junk-ca.txt` J4/J4b (constant printers).
- `.ufo/waves/round-77/w2/MutCaLedger.md:43-84` records the H2 guard executing
  `LEDGER-CHECK-77: PASS pairs=11` over a pristine ledger with mutants killed
  (interpreter, echo, bare name=value, mutable ref) — and names its own survivor
  (`HEAD` in revision position, e1) as a coverage finding.
- QUALITY 25's measured table (`corpus/QUALITY.md`) records both round-74 counters
  reading constants via `git show <freeze>:…`.

What is genuinely absent at base (the honest O before-state):

1. a lane-wide guard in `tools/` — every existing guard is round-scoped under
   `reports/round-<N>/` or `.ufo/waves/`; `tools/` contains no ledger/guard/token
   tool (probe section "guard-absent-check");
2. the R78-M1 rule pair from `corpus/lessons/round-78.md:11`: the frozen ledger
   must store the observed token from its exact pinned-base command, and any pair
   whose stated token equals that observed token must be rejected (round-77's
   candidate check accepted rows whose recorded observation did not equal the
   re-run; red-before = W2's executed BASEMISMATCH failure);
3. a guard whose record class includes census receipts / lane-wide calibration
   records (round-74's counter grades only its own frozen ledger pairs).

Precedent for the correct shape: SCORECARD.md:1330 (round-69 O2) names the
before-state precisely ("no lane-shaped settlement fixture harness at base"). The
draft's "base: absent" lets the O acceptance counter claim green for machinery that
already exists, and hides that O's real delta is (1)+(2)+(3).

Smallest correction: restate the O before as "no lane-wide `tools/` ledger-token
guard; R78-M1 pinned-observation storage and stated==observed rejection absent from
all committed guards; round-scoped guard machinery present (round-74 accept-ca.py,
round-77 ledger-check)", and scope O's after to exactly those deltas.

## F2 — duplicate authority: new guard vs the round-74/77 guard family; O-vs-Ca observation seam (fixable)

The draft requires "Distinct paths and separable evaluation" for O vs Ca but is
silent on O vs the existing guard family. If `tools/ledger-token-guard.py` lands
without naming its relationship to `reports/round-74/accept-ca.py`'s LEDGER/
BASEMISMATCH machinery, the lane holds two authorities over the same calibration
-record class; nothing in the draft says which verdict binds, and QUALITY 28's
"graded object supplies its own judge" class re-opens.

Second seam: O guards "this lane's calibration records" while Ca's correction
appends to the round-78 census receipt record. The draft does not pin O's
observation set. If O's observations include `reports/round-78/telemetry/census-end.txt`
as a guarded record, then at the lands revision O re-derives the S884 mismatch
(receipt still carries the wrong token — the correction is append-only) while Ca's
counter reports unresolved=0: two frozen counters disagree at one revision.

Smallest correction: claims.json O names (a) the guard's relationship to
round-74/77 machinery (supersede / wrap / disjoint record class) and (b) the exact
frozen observation set, explicitly excluding the records Ca's counter owns — or
states that the S884 receipt observation is Ca-counter-only, never O-guarded.

## F3 — Ca's pre-freeze demotion is honest and verified; the draft omits the verdict bindings the demotion requires (fixable)

Draft disposition: the calibration sizing rule requires mismatches in
SCORECARD/SHONEN self-assessment; the census receipt alone is evidence-record
repair, so Ca is rejected before freeze and lands as unclaimed conformance repair.
Verified against committed bytes:

- The wrong token `worldbuilding-setting-practice.amend-2026-10-24-r13.md` appears
  in exactly two lane files: `reports/round-78/telemetry/census-end.txt:33` itself
  and `corpus/lessons/round-78-verifier-spotcheck.md:67` (the routed-defect text).
- SHONEN.md: 0 occurrences of S884, 0 of "used-by". SCORECARD.md's 19 "used-by"
  mentions are generic capabilities/coverage cells; none records the S884 used-by
  token (probe section "SCORECARD used-by contexts").
- The registry row is byte-identical at base and at the round-78 work commit
  (sha256 `551ff520…` both; `r78-S884-row.txt` diff clean), used-by cell =
  `…amend-2026-10-23.md`; the file `…amend-2026-10-24-r13.md` never existed in any
  committed revision and does not exist on disk; only the distinct
  `heritage-taxonomy-models.amend-2026-10-24-r13.md` exists.

So no self-assessment mismatch exists; the demotion is the truthful label, and the
precedent matches: round-64's `final-measures-ca.txt` case
(`corpus/lessons/round-64-verifier-spotcheck.md:52,84`) was routed HIGH,
records-only, as a calibration defect repaired by re-stamp/correction — and
SCORECARD.md:1465 records the convention "Calibration is `improved` only for the
declared ledger pairs".

Gap: the draft does not bind the demoted repair's verdicts. QUALITY 20 requires
record repairs to declare `unchanged` on all three trends, and the unclaimed
correction must not appear as a calibration-axis improvement, an operability
capability-table entry, or a coverage delta (its correction counter is a one-shot
verification artifact, not a repertoire capability — shipping it into the
Capabilities table would invert the axis label the disposition just established).

Smallest correction: the draft states round-79 trend verdicts
expansion/quality/discernment = unchanged; SCORECARD calibration row = unchanged;
no capability-table row for the Ca counter; the correction binds original receipt
digest (sha256 `05b5011a…` for census-end.txt), measured revision (`4b255745…`),
old token, actual token, and leaves census-start/end byte-preserved.

## F4 — freshness-paused disclosure is honest as written; one lowest-axis obligation unstated (fixable)

Draft: "Freshness remains paused by open L0 round-11. No stagnation waiver. No new
numeric axis score." Each clause verifies:

- Pause: `LOG.md:3128` ("Freshness axis-move claims remain paused as recorded in
  SCORECARD.md … and LOG.md"), `SCORECARD.md:134,576,710`, and round-78 closure
  `LOG.md:4361` ("its axis-move remains paused by the unresolved round-11 L0
  question"). Consistent across rounds.
- "No stagnation waiver" is the honest label in both directions: the nudge
  (fleet AXES.md:66-73) waives the lowest-axis obligation only when every axis sits
  at/above the lane's saturation line — and `LOG.md:4361` records "the SCORECARD
  has no saturation evidence for the stagnation nudge", so a claimed waiver would
  be false. The draft claims none. Correct.
- "No new numeric axis score" matches the standing record: numeric rubric is an
  explicit protocol-conformance gap (SCORECARD header); freshness is "historically
  the lowest non-retired axis, not a newly computed scalar".

Gap: with freshness paused and no nudge, fleet AXES.md:33's lowest-axis obligation
still binds ("lowest-scoring non-retired axis"). Past rounds discharged it as
"lowest non-paused axis" (SCORECARD.md:597). The draft labels O "the declared
capability candidate" but never states operability is the lowest non-paused axis
(last O claim: round 69, SCORECARD.md:1330; coverage and calibration carried
rounds 73-78 claims). If that ranking is not written at freeze, the round's axis
choice is unlabeled, and the honesty of the freshness disclosure depends on a
silent step.

Smallest correction: one draft sentence naming operability as the lowest non-paused
axis with the evidence pointers (SCORECARD.md:1330; pause record LOG.md:4361), or
the round report states where the obligation lands.

## F5 — rejected coverage candidate verified at base; registry-delta handling must stay unclaimed (verified, no defect)

Draft: dining/tableware coverage candidate REJECTED pre-freeze; cuisine holds table
grammar/etiquette at lines 90-93; furniture names dining; Assimilation:none; no
considerthese directory; R74 quarantine inspect-only.

- `cuisine-food-lexicon.md:90` "## 6. Etiquette: the table as grammar" — held.
- `furniture-interior-lexicon.md` names dining (lines 3, 52, 57, 73) — held.
- No `considerthese` directory at lane root (probe). Round-74 quarantine section
  exists (`corpus/lessons/round-74.md:131`); the draft alters none of it.

Consistent with the round-78 record: "no new source row was opened or changed"
(LOG.md:4361). Watch item for the freeze, not a defect: S897 (own-work row,
S859/S860 precedent at corpus/SOURCES.md:814-815) will move the registry count
820→821 at lands; per the S859 precedent it must land as a frontier step "(not a
claim)", never as a coverage delta — and per F3 it must not mint a capability row.

---

## Verdicts

- F1, F2, F3, F4: fixable defects in the draft's labels — each is a wording/
  freeze-content correction, not a tradeoff. None requires rejecting O; all four
  bind at freeze (constants, before-states, observation sets, verdicts).
- F5: verified accurate; keep as-is with the S897 watch item.
- No premature saturation: one capability (O) is proposed, not a bundle; the
  existing guard family is the reason F1/F2 must be precise, not a reason to block.

## Probe receipts

- Raw: `.ufo/waves/round-79/w1/stage/CritAxis/receipts/axis-evidence-probe-raw.txt`
  (HEAD, digests `8f753788…` start / `05b5011a…` end census, row hashes, token
  search, absence checks, SCORECARD/SHONEN counts).
- Row blobs: `stage/CritAxis/receipts/base-S884-row.txt`,
  `r78-S884-row.txt` (byte-identical, sha256 `551ff520…`).
- All commands in the receipt are read-only (`git show/log/grep`, `sha256sum`,
  `awk`, `ls`, `find`, `diff`); rerun verbatim from the lane root.

Not run (and not claimed): any counter/selftest execution, live registry or source
access, sibling-lane writes, fleet-root writes. Tool installs: none.
