# CritTrendObservables — round-73 trend pre-declaration (pre-data)

Seat: critic (leaf; no delegation, no background jobs, no `task` spawns). Date: 2026-10-25.
Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD = base
`8841ad3b896a0227674fa0725b818c999118046f` (`git rev-parse HEAD`; `claims.json` `base`).
No live fetch performed by this seat (no User-Agent clause engaged), no tool installed,
no git write, no mutation of any kind. The only write is this file.

Inputs read: `reports/round-73/claims.json` (DRAFT-v0), `/home/vgpnk/Projects/shokunin/LEARNING.md`
(:29-47, :57-71), `corpus/QUALITY.md` (:29 criterion 6, :37 criterion 10, :41 criterion 12,
:57 criterion 18, :61 criterion 20, :63 criterion 21, and the drafted 22 at
`.ufo/waves/round-73/w1/drafts/quality-22.md`), `SCORECARD.md:1387-1395`,
`corpus/lessons/round-72.md` (:103 UA artefact routing, :104 lane-S869 routing),
`corpus/lessons/round-72-verifier-spotcheck.md` (:31 R2 evidence, :44 amendment precedent,
:59-61 closure verdicts, :66 R2), `/home/vgpnk/Projects/shokunin/CORPUS.md:123-125`,
the two entry drafts, and the wave-1 seat reports
(`ScoutGapSweep.md`, `ScoutS882.md:179`, `ScoutS894` verdict inside
`ScoutQuarantineConlang.md:53,74`, `ScoutAmendTriage.md:66-72`, `RevSowersAccess.md`,
`ScoutS901.md:149`).

---

## 1. The rule this declaration applies

Three clauses, applied without exception:

1. **A trend fires only on its LEARNING.md observable** (LEARNING.md:33-35). Nothing else —
   not a landed claim, not a repaired record, not a new file, not a new criterion — is an
   observable. `SCORECARD.md:1387-1395` is the correction row for the last round that graded
   two trends `improved` with no observable; that row is the failure this seat exists to
   avoid repeating.
2. **Record and instrument work is calibration, never quality and never discernment**
   (QUALITY.md:61, criterion 20: "record/instrument repairs (receipt headers, pointer fixes,
   quote trims, dispositions) are calibration work, never quality or discernment observables").
   A round that repairs records must declare `unchanged` on both trends unless an observable
   fires.
3. **Discernment is checked from outside** (LEARNING.md:41-47). "Self-assessed taste is not
   discernment"; "a subagent the lane dispatched is still the lane". The improved-leg's second
   branch — "a disagreement becomes a lesson that adds a grounded `QUALITY.md` criterion"
   (:35) — therefore takes its disagreement from the non-author record, not from a lane
   seat's own routing. A criterion is the *second* link of that chain; the first link is a
   recorded non-author disagreement.

Reading note, stated so a reviewer can reject it: QUALITY.md:61's literal tail says
"discernment requires a gate decision agreed with an outside spot-check **or** a new
lesson-grounded criterion", which on its own would let a criterion fire discernment with no
outside record. That reading is refused here because it makes clause 3 vacuous — a lane could
self-certify discernment by writing a criterion about its own mistake — and because the
operative precedent does not support it: round 72's closure credited discernment `improved`
only by joining criterion 21 **to** its own spot-check agreement
(`round-72-verifier-spotcheck.md:61`), and the lane's own round-72 filing conceded the point
("non-author agreement is the closure's", `.ufo/reports/round-72/kotodama.md:38`). The
checkable form of the rule: **a criterion fires discernment only when its Ground line names a
non-author record** — a `corpus/lessons/round-*-verifier-spotcheck.md` routed defect or an
operator teaching — never a lane seat's wave report.

---

## 2. Pre-declared verdict table

`fires?` is the pre-data answer. "Report must cite" is the byte the round-73 report must
carry for the verdict to stand; "downgrade" is the exact observation that changes it.

### expansion (LEARNING.md:33)

| # | observable instance | fires? | evidence the report must cite | what downgrades it |
|---|---|---|---|---|
| E1 | Claim C, base entry `linguistics/conlang-scholarship.md` (rows S876/S877) on ground the coverage map did not hold | **YES → `improved`**, conditional | (a) `reports/round-73/telemetry/gap-sweep.txt` committed **before data**, showing 0 `*conlang-scholarship*` files and 0 registry rows for the five venue fragments at `8841ad3b` (seat receipt text: `ScoutGapSweep.md` §"Receipt text"); (b) `ACCEPT-C-73: PASS legs=<n>/<n>` at `<lands>` with the criterion-19 header set (`# stamped/evaluated/measured/tree/counter sha256`); (c) registry diff base..lands adding rows whose ids are ≥ S876, all `mined`, `used-by` = exactly the citing entries; (d) `sources-census.sh validate` exit 0 at lands; (e) one Gate line per new row: URL + access date 2026-10-25 + ≤25-word located quote | ground already held (gap sweep ≠ 0, or a *mined* peer-reviewed conlang-venue row exists at base — see C2); any cited row not `mined`; any `used-by` naming a non-admitted entry (see C4); census ≠ 0; **or an admitted entry failing the bar it was admitted under → `harmed`, not merely not-improved** (see E3) |
| E2 | Claim C, amendment file `conlang-scholarship.amend-2026-10-23.md` (rows S878/S879/S880) | **YES, as an admitted entry — but it is not a second ground unit and not a frontier move.** Precedent is explicit and split: round 72's closure counted "two entries" for expansion (`round-72-verifier-spotcheck.md:59`) and the same file refused to count the co-admitted amendment as a deepening (`:44`) | the amendment's own provenance trio (it has one: draft :1-12) + its three rows inside the same `used-by` set; the report says **"one theme, two admitted files"** | the report claiming two ground units, two frontier areas, or an `adjacency` move on the strength of the second file; or the amendment counted as depth (that is the round-70/round-72 class) |
| E3 | harmed sentinel | **`harmed`** iff an admitted entry fails the bar it was admitted under | the re-open receipt for the failing row + the failing entry line | — (this *is* the downgrade) |

Live E3 candidates found pre-data (each would fail the bar, not merely the count):

- **False provenance limit.** Draft `conlang-scholarship.amend-2026-10-23.md:12` states the
  Sowers-Wills article "was not opened: its DOI resolved to a publisher page answering HTTP 429",
  and :70 says the semester-long element "stays (to-verify): both need the study itself".
  `RevSowersAccess.md` records the opposite for the payload: Crossref/Semantic Scholar/OpenAlex
  each HTTP 200 carrying the abstract span (UA-B recorded), publisher page 429, zero Wayback
  200-captures. QUALITY.md:37 (criterion 10) and :41 (criterion 12) make an unverified
  "unreachable" reason a defect; a landed entry that keeps this line asserts a limit that is
  false. Fix before landing, or the round admits an entry on a false provenance claim.
- **Carrier scoped above its authority.** The base entry's taxonomy claim must rest on
  S877's ch. 1 pages (draft :4 says ch. 1 pp. 8-34 were read) and not on the оглавление alone
  (QUALITY.md:29, criterion 6). The Gate quote must be located on the printed page, not in the
  table of contents.
- **Campaign id.** The staged base entry's prose cites `S728`; lane `corpus/SOURCES.md:683`
  `S728` is Frye 2022 Qaqet child-directed speech, an unrelated document. The draft has
  dropped the sentence (verified: no `S728`/`26C3` token in `drafts/conlang-scholarship.md`),
  so this is a *watch* item, not a live defect — but the Gate must record the 26C3 document's
  disposition truthfully (see C5).

### quality (LEARNING.md:34)

| # | observable instance | fires? | evidence the report must cite | what downgrades it |
|---|---|---|---|---|
| Q1 | Claim Ca — ledger pairs repaired/annotated (R1-R3 and the sweep's pairs) | **NO.** QUALITY.md:61; `SCORECARD.md:1387-1395`. A `REPAIR`/`ANNOTATE` of a SCORECARD/SHONEN/README/SKILL.md statement is not an entry re-verified, deepened or superseded | the ledger pair dispositions + the `## Corrections — round 73` rows; the report must place them under **calibration only** | nothing in Ca can fire it. The single exception to watch: if a `REPAIR` pair's observed token forces a change to a *knowledge entry's claim*, that is a quality event and must be declared as one — no such pair is in the drafted ledger |
| Q2 | Claim C's amendment, co-admitted with its base | **NO.** `round-72-verifier-spotcheck.md:44`: "the amendment co-admitted with its base is one admission event, not a deepening". At base there is no `conlang-scholarship.md` to deepen (verified: `find corpus/knowledge -iname '*conlang-scholarship*'` = 0) | base..lands `corpus/knowledge` diff shows new files only; the report states the one-event rule in words | the report calling the amendment "deepening"/"completing" in trend terms → round-70 class |
| Q3 | Lane-S869 (RAD Benesh) re-verification — the frontier's "maybe" | **Only under both conditions**, else `unchanged`: (i) a committed re-open receipt at `<lands>` naming the page, the UA and the located span; (ii) the citing entry's `verified-at`/`recheck` updated to cite that receipt | `corpus/knowledge/culture-material/dance-performance-movement-codes.md:11,47-49,100` (the entry line: "described by the Royal Academy of Dance as a system for documenting human movement"); the receipt; the entry diff; if criterion 18 fails, the superseding row | **a date bump with no receipt = calibration (`unchanged`)**; a row-carrier swap with the entry line untouched = calibration; span absent from live *and* every capture and the entry left as filed = `harmed` |
| Q4 | harmed sentinel | **`harmed`** iff an entry is found false or stale and left unmarked | the re-open receipt + the unmarked entry line | — |

Q3 status, pre-data: **no seat is assigned it.** `spec.json` holds 37 items; the token `S869`
appears in exactly two prompts — `ScoutQuarantineConlang` (where it is the **staged** S869 =
conlang.org/26c3.pdf, a different namespace) and this seat's own prompt. The lane's round-72
routing (`round-72.md:104`) handed lane-S869 "to the registry-correction chain", and no r73
wave-1 seat is that chain. So the default verdict is `unchanged`, and the frontier item is
**undelivered unless a seat is added or the L1 executes it**.

### discernment (LEARNING.md:35)

| # | observable instance | fires? | evidence the report must cite | what downgrades it |
|---|---|---|---|---|
| D1 | Outside spot-check on round-73's gate decisions | **YES → `improved`** — but only on a non-author record covering ≥1 r73 admit **and** ≥1 r73 reject | the non-author record itself: the round-73 lesson's `## Gate` spot-check result (LEARNING.md:70 requires it there) or the closure's `corpus/lessons/round-73-verifier-spotcheck.md`, with re-opened sources, `agree`/`disagree` + reason, and the reviewer named | no record at report time → **`unchanged` (this is the pre-declared default)**; any `disagree` left unlearned → `harmed` |
| D2 | QUALITY criterion 22 (UA-record clause), ground = `round-72.md:103` (lane seat `ScoutCDXCanonical`) | **NO.** The ground is lane-internal, so the chain's first link is missing (§1 clause 3). The criterion is a record of a class, not evidence that the lane's taste improved | if the round claims the fire anyway: the criterion's Ground line **must** name a non-author record. `drafts/quality-22.md`'s ground does not | filing `improved` on the criterion's existence = `SCORECARD.md:1387-1395` class. Also `harmed` if the criterion lands with no lesson citation at all |
| D3 | Mined mistake R2 (receipt/verdict mismatch, `round-72-verifier-spotcheck.md:66`) and any criterion grounded in it | **NO.** R2 is a receipt-vs-verdict defect: instrument class, excluded from quality *and* discernment by QUALITY.md:61. R2 being an outside record does not help — it is not a *gate decision* | the `## Mistakes` row (class · evidence · captured-by · fix) and the SCORECARD correction row; report it under calibration | the round filing `improved` on the mistake row, or on a receipts criterion derived from it |
| D4 | harmed sentinel — the round against its own new criterion | **`harmed`** iff the Gate files the Sowers-Wills 429 reject in a shape criterion 22 itself forbids (no `UA=… → HTTP 429; retry UA=… → HTTP 429`) **while** `RevSowersAccess.md` records the payload reachable at record tier; also `harmed` if the Gate files S894/S910/26C3 as unreachability rejects (see C5) | `RevSowersAccess.md` verdict lines + the lesson's Gate line + the criterion text | — |
| D5 | calibration axis (not a trend) | Ca's legs move **calibration**, recorded as an axis row only | the ledger + `ACCEPT-CA-73` receipt | recording calibration as quality or discernment |

---

## 3. Direct answers to the three posed questions

**Does an amendment co-admitted with its base count as deepening?** No. `round-72-verifier-spotcheck.md:44`
settles it in the same fact pattern (heritage-taxonomy base + `.amend-2026-10-24-r13.md`):
"one admission event, not a deepening". At round-73 base there is no `conlang-scholarship.md`
at all, so there is nothing to deepen. The amendment counts once, for expansion, as an admitted
entry on the same ground as its base — not twice, and never for quality.

**Does a QUALITY criterion grounded in a routed lesson fire discernment without an outside
spot-check agreement?** No, under the rule in §1. Two consequences: (a) QUALITY 22 alone leaves
discernment `unchanged`; (b) if the closure's spot-check later agrees with r73's admits *and*
rejects, discernment becomes `improved` and the criterion is then part of the evidence, not the
whole of it. The distinction is checkable: read the criterion's Ground line. If it names
`round-72.md`'s Routed section (a lane seat's routing), it is not a non-author disagreement.
If it names a `round-*-verifier-spotcheck.md` routed defect, it is.

**Does repairing records fire quality?** No — QUALITY.md:61 is explicit, and it is the criterion
written *because* round 70 graded exactly that. Ca's whole content (R1 tracking two files, R2's
rerun receipt, R3's SKILL.md registry rows, README footer, append-only annotations) is record
repair. Its axis is calibration. If the round reports `quality: improved` off Ca, the round
repeats the round-70 error with a receipt attached.

---

## 4. Pre-declared headline verdicts

- **expansion: `improved`** — claim C, conditional on E1's legs and on no E3 instance landing.
  Stated as one theme, two admitted files, five mined rows (S876..S880).
- **quality: `unchanged`** — nothing present at base is re-verified, deepened or superseded;
  Ca is calibration; the co-admitted amendment is one admission event. The only route to
  `improved` is Q3, and Q3 has no seat.
- **discernment: `unchanged` at report time** — no non-author record exists at the time the
  lane files. `improved` is available to the closure on D1's evidence; the lane may not claim
  it, and may not claim `unprovable-but-better` either, since LEARNING.md:45-47 requires a
  named non-author judging better "with reasons on record".
- **trade warning:** if C lands and any E3/D4 instance lands with it, the round is
  `expansion: improved` with `discernment: harmed` — report it as a trade, never as learning
  (LEARNING.md:37-38 states the trade rule for expansion/quality; the same discipline governs
  any improved/harmed pair).

---

## 5. Counterexamples found pre-data (each checkable from committed or lane bytes)

**C1 — two different documents are both called S869, and the frontier item does not
disambiguate.** Lane `corpus/SOURCES.md:824` `S869` = RAD Benesh International; staged
`SOURCES.append.md:17` `S869` = "Conlanging 101", 26C3, conlang.org/26c3.pdf (register S786).
`claims.json` C `REJECTS` says "staged S869 conference-paper clause" while the frontier names
"re-verification of S869". A reader joins them by token and concludes the RAD row is the
conference paper. *Correction:* every mention must read "lane S869" or "staged S869", and the
lesson must carry the by-document join for both.

**C2 — "no research venue" is falsifiable; "no mined peer-reviewed venue" is not.**
`ScoutGapSweep.md` §[2] finds nine registry rows matching the conlang pattern, including
`S012` Alper et al. 2025 ConlangCrafter (arXiv paper, queued), `S009` CALS (community atlas,
queued), `S008` Rosenfelder (docs, mined). The claim's GROUND leg is safe (0 owners for the
five fragments) and expansion stands — but the base draft's `ground:`/`gap filled` wording must
say "no *mined* row for a peer-reviewed constructed-language venue", or a reviewer re-running
the sweep finds `S012` and reads the entry's ground as overstated (QUALITY.md:29, criterion 6;
criterion 12's re-test rule).

**C3 — the criterion the round adds is narrower than the defect the round is committing.**
Criterion 22 (draft) demands UA + retry status lines for wall rejects. The live defect in this
round's own entry is not a UA artefact: it is a **payload-tier** confusion — a 429 on the
publisher landing page read as "the study was not opened", while the abstract the entry needs
was served HTTP 200 by Crossref/S2/OpenAlex (`RevSowersAccess.md` §S894 table). A UA-record
clause would not have caught it. *Correction (smallest safe):* criterion 22 carries a second
sentence — a wall on the publisher page does not make a row unreachable when the row's quoted
span is served by a record-tier endpoint; the record tier is probed before any reject — with
`RevSowersAccess.md`'s S894/S910 result as the shown-able-to-fail instance. Without it the
round adds a criterion that its own Gate line would pass while its own entry stays false.

**C4 — `used-by` would name an entry the round does not admit.** `ScoutS882.md:179` proposes
naming both `conlang-scholarship.md` and `worldbuilding-setting-practice.md` in S877's
`used-by`; the second is a staged entry that cites the same document
(`merge/kotodama/knowledge/corpus/knowledge/culture-material/worldbuilding-setting-practice.md:4`)
and is **not** admitted this round. Claim C's ROWS leg requires `used-by` to name "exactly the
admitted entries that cite it". *Correction:* `used-by` = the admitted entries only; the
unadmitted citing entry is recorded in the Gate's not-adopted list.

**C5 — the REJECTS leg, satisfied literally, forces false reject reasons.** It requires the
lesson to refuse "staged S869 conference-paper clause; staged S894/S910 if their payload stays
unreachable by ordinary means". The condition is false for all three: `ScoutQuarantineConlang.md:53`
finds the 26C3 anchor PRESENT (title-page epigraph, p. 1); `:74` finds S894's abstract span
present on the Crossref record; `ScoutAmendTriage.md:68-72` finds S910's spans present on
Crossref and states "S910 is NOT an unreachability reject". `ScoutAmendTriage.md:66-68` also
records the intended disposition: those rows are **deferred for row-set scope**, not refused for
unreachability. *Correction, pre-freeze:* restate the REJECTS parenthetical to the true grounds
(defer, row set fixed at five) and keep the quarantine verdicts as filed; otherwise the Gate
files a reason criterion 12 cannot re-test as true, and D4's harmed branch opens.

**C6 — the ground receipt does not exist yet.** `reports/round-73/telemetry/` contains only
`census-start.txt` (799 rows, exit 0, verified). Claim C's GROUND leg calls for
`gap-sweep.txt` "committed before data". The seat produced the receipt text
(`ScoutGapSweep.md` §"Receipt text") — it must be committed before the registry append, or the
ground leg is asserted rather than measured. Same class, Ca: `reports/round-73/ledger.json` is
absent at the time of writing, and Ca's LEDGER leg requires it committed before data.

**C7 — before-state is live, which is the point.** `git status --porcelain` at base lists
`.ufo/waves/round-72/w1/ScoutMergeScan.md` and `ScribeLesson.md` untracked (Ca's R1 pair), and
`reports/round-72/telemetry/measures-ca.txt` reads FAIL against the SCORECARD's "12/12 PASS"
(R2). Both are calibration inputs; neither is a trend observable.

---

## 6. Smallest safe corrections (ranked; none requires editing frozen bytes)

1. **Pre-freeze, claim C `REJECTS`:** replace the unreachability parenthetical with the
   quarantine verdicts as filed (26C3 PRESENT; S894/S910 record-tier reachable) and state
   deferral for row-set scope. (C5)
2. **Pre-landing, the amendment entry:** rewrite `:12` and `:70` so the limit stated is the true
   one — publisher landing page 429 under both UAs, abstract span opened on the Crossref record
   (HTTP 200, UA-B recorded) — and drop "stays (to-verify)" for anything the record carries.
   (E3, C3)
3. **Criterion 22:** add the record-tier sentence with `RevSowersAccess.md`'s S894 result as the
   control, or do not file the criterion as covering the round's own class. (C3)
4. **Row `used-by`:** admitted entries only; unadmitted citing entries go to the Gate's
   not-adopted list. (C4)
5. **Commit `gap-sweep.txt` and `ledger.json` before data.** (C6)
6. **Disambiguate every S869 token** in the lesson, the frontier item and the report. (C1)
7. **Do not file a trend verdict off Ca, the amendment, criterion 22 or the Mistakes row.**
   (Q1, Q2, D2, D3)

---

## 7. Limits of this seat

- The declaration is pre-data against `claims.json` DRAFT-v0; if the claims are corrected at
  freeze, E1's leg names and Ca's pair set must be re-read against the frozen text. The
  observable definitions in §2 do not move.
- Wave-1 peer reports were read as lane evidence for the downgrade conditions (C2, C3, C4, C5);
  they are lane-authored and cannot supply D1's outside leg.
- No live fetch was made, so no UA is recorded by this seat; `RevSowersAccess.md`'s UA-B
  records stand on that seat's own bytes, not on a re-run here.
