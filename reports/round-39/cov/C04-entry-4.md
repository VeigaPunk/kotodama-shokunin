- Seat: C04 | executor | claim C | date 2026-10-19 | baseline dfb0719

# C04 — verification-partition entry 4 (claim C / coverage)

Target path (first mention = the staging path):
`corpus/knowledge/verification/append-only-record-verification.md` — a new
file; with C01–C03's three it moves verification 20 → 24 and the README to
revision 2.2 (those counts are claim C's deliverable, `reports/round-39/claims.json:13-17`,
not this fragment's).

Topic self-scouted: the round-39 scout (`reports/round-39/scout/K01-verification-gaps.md`)
and the plan (`reports/round-39/plan/P01-plan.md`) had not landed at write time
(probed absent 2026-10-19, see Citations). Per the wave's missing-dependency rule
this seat scouted its own gap, measured the absence sweep recorded in the entry's
`- gap filled:` line, and files the topic decision for X00's collision matrix;
alternates considered and rejected are under §Alternates. The staged bytes below
were self-audited with the round-35 C12 entry-audit instrument before filing
(§Self-audit), so C05 inherits a measured reading, not a fresh claim.

```markdown
# Append-only record verification — the close digest, the closing snapshot, and the successor-row correction

- topic: The verification procedure for **append-only records** — how a filed lane record (a round receipt, a telemetry snapshot, a recount ledger, an index revision, a LOG entry) is verified to have stayed unedited after filing: the open/closed record lifecycle (`open-at-seat-close` with a finalization note), the closing snapshot that fills an open record's fields as a new file, each filled value citing the durable artifact it was read from or recording `could-not-recover` with an owner and reason, the close digest (the record's SHA-256 at close time, recorded by the snapshot that closes it) that turns any later in-place edit into a detectable digest mismatch, and successor-row correction (a correction is a new row or snapshot with its own provenance; the superseded reading is preserved as the dated record it was). Method and lane policy only; canon belongs to lore-shokunin.
- gap filled: the partition states append-only discipline per record type — provenance events (`provenance-audit-ledger-format.md` §8), gate freezes (`gate-frozen-run-standard.md`), generated artifacts (`generated-artifact-roundtrip-verification.md`), triage resolutions (`to-verify-triage-protocol.md`), recorded verdicts (`two-reader-interop-agreement.md:50`), corpus-header repairs vs filed-report corrections (`header-conformance-readings.md:22`) — but no entry owns the general verification procedure for the lane's filed bookkeeping records: who records which digest when, what a closing snapshot must contain, how an in-place edit is detected after the fact, and what a digest match never proves. Absence sweep 2026-10-19 at HEAD dfb0719 over `corpus/knowledge/` (212 files): `grep -rn "closing snapshot" corpus/knowledge/ | wc -l` → **0**; `grep -rn "could-not-recover" corpus/knowledge/ | wc -l` → **0**; `grep -rn "close digest\|digest at close\|digest-at-close" corpus/knowledge/ | wc -l` → **0**; `grep -rln "append-only" corpus/knowledge/ | wc -l` → **12** files, each a per-record-type rule statement, none the closing-snapshot contract or the detection procedure. The one place the full discipline is written is outside the corpus, in the lane's operating rules (`AGENTS.md:32-39`): a live operating rule with no corpus method entry behind it — that missing method entry is this file.
- sources:
  - KTD-AR-S-0001 — `AGENTS.md:32-39`: the close-what-you-open rule — a record filed `open-at-seat-close` with a finalization note is not complete; the integrating parent files a closing snapshot under the same round's `telemetry/` as a new append-only file, never an in-place edit of the original record; each filled value cites the durable artifact it was read from, or records `could-not-recover` with an owner and reason; the snapshot names the record it closes and that record's SHA-256 at close time, so any later in-place edit is detectable as a digest mismatch. This entry methodizes that rule; the rule stays the operator's and remains authoritative over this file.
  - KTD-AR-S-0002 — `AGENTS.md:5-6` (every change recorded in an append-only LOG.md entry with its motivating evidence) and `AGENTS.md:18-25` (each telemetry snapshot names its owner, observation window, counting command and date, durable source paths and SHA-256 digests; unknown counters stay `null` with an owner and reason, never inferred zeroes).
  - KTD-AR-S-0003 — `corpus/knowledge/verification/provenance-audit-ledger-format.md:140-155` (§8, "Append-only rules and active-view reconstruction"): the closest in-corpus ancestor — append at EOF, corrections name `supersedes` IDs, forks are resolved by appending an assessment that names every leaf it supersedes (item 6), and item 10's checkpoint rule: persist the exact closed prefix's byte length and digest against an independently retained anchor, excluding the checkpoint's own bytes, because "a digest printed from a mutable file alone detects no drift". That rule, written for provenance events, is the close digest generalized to all filed records.
  - KTD-AR-S-0004 — `corpus/knowledge/verification/verification-independence-anti-circularity.md:61,144`: the C5 hazard (an in-place edit plus a refresh is undetectable to a tool reading its own pin) and IND-6 (where an artifact self-pins, the anchor lives outside it). Supplies the independence constraint §4 builds on: the close digest lives in the closing snapshot, never only in the record it closes.
  - KTD-AR-S-0005 — `corpus/knowledge/verification/header-conformance-readings.md:22,119-121`: the repair/correction vocabulary this entry adopts — an in-place corpus-header repair is lane-authorized and logged; a correction to a filed report is new bytes with a superseding note, never a rewrite, and never a re-pin of a frozen artifact to bless a change.
  - KTD-AR-S-0006 — `corpus/knowledge/verification/two-reader-interop-agreement.md:50,77`: reader-drift is re-recorded as a new row; no recorded row is edited in place. The verdict-recording precedent this entry extends from agreement readings to all filed records.
  - KTD-AR-S-0007 — `corpus/README.md:43-61,511-518`: the revision convention as in-corpus precedent — revision 1.8 found the counts footer stale, corrected it, and preserved the superseded 199/19 reading "as the dated record it was"; the totals footer carries its own superseded-reading note to this day. A correction is a new dated block; the old reading is never deleted.
  - KTD-AR-S-0008 — `reports/round-20/readme/gaps.md:18-20,54-57`: the measured in-place-edit incident — round-5/6 runners rewrote their filed `validation.json` in place on a later tree; the committed bytes were restored with `git checkout --` and verified clean, and the drift was recorded with digests in the same document rather than by editing the old runners or their receipts; the rows' counts "remain filed and correct; what no longer works is" the reproduction command on the later tree.
  - KTD-AR-S-0009 — `reports/round-37/calib/recount-ledger.json:68,81,94,107`: the four `could-not-reproduce` recount rows, each carrying source round, command, filed-vs-observed, disposition, cause, owner and an evidence pointer — the live example of a record whose rows name their owner and evidence instead of inferring outcomes. The r39 calibration claim dispositions these rows in a successor ledger (`reports/round-39/claims.json:19-24`); this entry supplies the method that successor follows.
  - KTD-AR-S-0010 — `reports/round-39/telemetry/dispatch-declared.json:25`: a live open record at write time — `"closing_snapshot": "open-at-seat-close: owed once validation.json lands"` — the §2 lifecycle state as filed, in this round's own telemetry.
  - KTD-AR-S-0011 — `reports/round-28/readme/sweep.py:1-30`: the footer-leg sweep as the model checker — it re-measures a record's present-tense claim against the live tree instead of trusting the record, and exists because an earlier sweep went green over a claim it never read; the close-digest detector is the same posture applied to a record's own bytes.
  - KTD-AR-S-0012 — NIST SP 800-92, *Guide to Computer Security Log Management* (2006) — log-integrity and protection guidance, cited as literature **(to-verify: not consulted this round; no network in this run)**.
  - KTD-AR-S-0013 — ISO 15489-1:2016, *Information and documentation — Records management* — records-capture and fixity framing, cited as literature **(to-verify: not consulted this round; no network in this run)**.
- calibration: append-only discipline is this lane's house policy, grounded in its own operating rules and incident history (KTD-AR-S-0001, KTD-AR-S-0008), not a published standard it claims to implement; the checkpoint-digest idea is already stated in-corpus for provenance events (KTD-AR-S-0003 §8 item 10) and this entry generalizes it, it does not invent it; NIST SP 800-92 and ISO 15489-1 are engineering and records-management references, cited unread this round and carrying no weight in any procedure row; no real culture is described.
- couples: verification — `verification-method-overview.md` (the philosophy this procedure instantiates: inspectable inputs, an expected result, a possible failure), `provenance-audit-ledger-format.md` (the §8 ancestor; this entry covers the bookkeeping records its event schema does not), `verification-independence-anti-circularity.md` (the IND-6 anchor-outside constraint §4 applies), `gate-frozen-run-standard.md` (the frozen-run surface, which keeps its own entry), `generated-artifact-roundtrip-verification.md` (the regeneration surface, idem), `header-conformance-readings.md` (the repair-vs-correction vocabulary and the corpus-header surface), `to-verify-triage-protocol.md` (where an unverifiable record claim routes), `two-reader-interop-agreement.md` (reader-drift re-recording), `citation-format-and-source-registry.md` (the citation profile the per-field citations follow); synthesis — `../synthesis/generated-artifact-lifecycle.md` (:81, a re-freeze is a new row), `../synthesis/finding-disposition-workflow.md` (:60, the disposition record is append-only), `../synthesis/hold-set-contract-in-brief.md` (:77, a corrected declaration is a new file); lane surfaces — `AGENTS.md` (the operator rule this methodizes), `LOG.md`, `corpus/README.md` (the revision convention), `reports/round-20/readme/gaps.md`, `reports/round-28/readme/sweep.py`, `reports/round-37/calib/recount-ledger.json`, `tools/replay-frozen.py` (the digest-comparing replay §4's detector resembles); siblings — lore-shokunin owns canon; the operator owns the operating rules this entry methodizes.
- source: the measured authority for the gap statement is the absence sweep recorded in `- gap filled:` (commands and counts, run 2026-10-19 at HEAD dfb0719); the design authority is KTD-AR-S-0001, KTD-AR-S-0003 and KTD-AR-S-0004 — the operator rule, the in-corpus checkpoint rule, and the anchor-outside constraint; every procedure row below cites one of these. **No external source was resolved this round** (no network in this run); the two literature citations are marked `(to-verify)` in place and load no procedure row.
- verified-at: 2026-10-19 — written this round at lane HEAD dfb0719, from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Readings taken: the absence-sweep commands in `- gap filled:` (outputs recorded there); partition census `ls corpus/knowledge/verification/*.md | wc -l` → 20 and `ls corpus/knowledge/*/*.md | wc -l` → 212; every cited repo path re-read at its cited lines this round (each line number checked by `grep -n` before citing). **Not done this round:** no external source was fetched (NIST, ISO unconsulted — marked in place); no closing snapshot was filed by this seat and no close digest is pinned in this entry (pins are recorded by the snapshot that closes a record, never inside the method entry); the live examples KTD-AR-S-0009 and KTD-AR-S-0010 were read, not re-dispositioned — that re-disposition is the r39 calibration claim's work, not this entry's.
- recheck: before treating any filed record as unchanged since close (recompute its digest and compare against the closing snapshot's pin); whenever a closing snapshot is filed or amended; whenever a record's current bytes mismatch a recorded close digest (file the mismatch, never repair in place); whenever the lane's operating rules amend the close-what-you-open rule; and before citing this entry's §2 states for any record whose snapshot has not been read. Corrections to this entry are successor rows, never rewrites.
- scope: reference method and lane policy for the verification partition only. This entry decides nothing about any world, records no canon fact, and issues no promotion, clearance or closure verdict about any round, record or artifact — those stay operator- and lore-shokunin-owned. Every `(to-verify)` item above is a backlog row, not an assertion.

## 1. What this entry licenses, and the surfaces it does not re-own

- **The procedure.** Four checks, each falsifiable: (1) the record's lifecycle state is named (§2); (2) a closing snapshot satisfies its contract (§3); (3) a closed record's current bytes match its close digest (§4); (4) every correction is a successor row (§5). §6 gives the controls that make each check able to fail.
- **The record class.** Filed bookkeeping records: round receipts and validation receipts, telemetry snapshots, recount and calibration ledgers, README index revisions, LOG entries, and the per-seat fragments under a round's reports directory. Not covered here, because each keeps its own entry: frozen gate runs (`gate-frozen-run-standard.md`), generated artifacts (`generated-artifact-roundtrip-verification.md`), corpus headers (`header-conformance-readings.md`), and provenance audit events (`provenance-audit-ledger-format.md`).
- **Method statement** (house rule): everything below is reference method and lane policy. Nothing here decides what is true in any world, and a green reading of any check is a structural reading of bytes, never a verdict on the scholarship, never a clearance (§7).

## 2. The record lifecycle

| State | How it is filed | What completes it | Who acts |
|---|---|---|---|
| open (`open-at-seat-close`) | the record is filed with a finalization note naming each field still owed | a closing snapshot under §3 | the actor the operating rule names (for round telemetry, the integrating parent) |
| closed | the closing snapshot exists, satisfies §3, and pins the record's SHA-256 at close | nothing; the state is terminal for the original bytes | the closing actor |
| corrected | a successor row, snapshot or revision block names what it supersedes and carries its own provenance (§5) | nothing; superseded readings stay as the dated record they were | the correcting actor |

- **The load-bearing rule:** an open record is citable only as open. KTD-AR-S-0010 shows the state in the wild: `"closing_snapshot": "open-at-seat-close: owed once validation.json lands"` — a number read from that record before its snapshot lands is a reading of an incomplete record and must be labelled as such.
- **Design lever:** name the state in the citation, not in prose memory. A reader who cannot tell open from closed from the bytes alone is being asked to trust a filing convention that this entry exists to make checkable.

## 3. The closing snapshot contract

A closing snapshot is admissible when all six hold:

1. **New file.** It lives beside the record (for round telemetry, under the same round's `telemetry/`), never as an edit of the original record's bytes (KTD-AR-S-0001).
2. **Named record.** It names the record it closes by path, and that record's SHA-256 at close time — the close digest §4 checks against.
3. **Cited fills.** Each field the finalization note left open is filled with a value citing the durable artifact the value was read from (path, line or command).
4. **Honest gaps.** A field that cannot be recovered records `could-not-recover` with an owner and a reason; unknown counters stay `null` with an owner and reason, never inferred zeroes (KTD-AR-S-0002).
5. **Own provenance.** It carries its own owner, time and sampling window, per the telemetry rules the lane already runs under.
6. **No reclassification.** Filling an open field changes the record's completeness, not its history: the original record's bytes, including its finalization note, stay untouched.

- **Why per-field citations:** a closing snapshot without them is a second assertion, not a verification; with them, each filled value is checkable the way `verification-method-overview.md` requires of any claim — inspectable input, expected result, possible failure.

## 4. The close digest and the detector

- **Who pins.** The closing snapshot records the digest; the record itself never carries its own pin as the only anchor. This is IND-6 applied (KTD-AR-S-0004) and §8 item 10 of KTD-AR-S-0003 stated as a rule: a digest printed from a mutable file alone detects no drift.
- **The detector procedure.** To check a closed record: recompute the SHA-256 of the record's current bytes; compare against the close digest in its closing snapshot. Match → the bytes are unchanged since close. Mismatch → the record was edited after close; file the mismatch as a finding with whatever history is available (git log, reflog), and never restore, re-pin or overwrite to make the comparison pass — the mismatch is information, and erasing it is the C5 hazard KTD-AR-S-0004 names.
- **What each outcome means:**

| Outcome | Means | Does not mean |
|---|---|---|
| match | the bytes are the bytes that were closed | the record is true, correct, or complete; §7 |
| mismatch | an in-place edit happened after close | who edited, why, or which edit is the bad one — that is what the history leg is for |
| no close digest filed | the record is not closed under this procedure | the record is wrong; it is simply outside this procedure's protection |

- **The worked case (KTD-AR-S-0008).** Round 20 measured that round-5/6 runners had rewritten their filed `validation.json` in place on a later tree; the committed bytes were restored with `git checkout --`, verified clean, and the incident was recorded with digests in the same document — the record was protected by restoring history, not by re-pinning the drift.
- **Relation to existing instruments.** `tools/replay-frozen.py` already refuses on `gate_digest_mismatch` for frozen rows, and `reports/round-28/readme/sweep.py` re-measures a present-tense claim against the tree (KTD-AR-S-0011); the close-digest detector is the same posture pointed at bookkeeping records. Whether it should become a standing sweep is DR-AR-08, not decided here.

## 5. Successor-row correction

- **The rule.** A correction to a filed record is a new row, snapshot or revision block with its own provenance, naming what it supersedes; the superseded reading is preserved as the dated record it was (KTD-AR-S-0005, -0006, -0007). This is §8 of KTD-AR-S-0003 (supersession edges point backward; no cycles, no dangling links) applied outside the provenance ledger.
- **The stale-command pattern.** When what drifted is a reproduction command rather than a filed count, the correction records the attribution and leaves the old runner and receipt untouched (KTD-AR-S-0008: the counts "remain filed and correct"; the round-20 document records which commands no longer re-derive, with digests, instead of editing the runners).
- **Forks.** Two unsuperseded successor rows for one record is an unresolved fork: resolved by appending a row that names every leaf it supersedes and explains the evidence, never by silently preferring one (KTD-AR-S-0003 §8 item 6).

## 6. Controls — what makes each check able to fail

| Control | Planted condition | Required result |
|---|---|---|
| edit-after-close | change one byte of a closed record | the recomputed digest mismatches the close digest; §4 files a finding |
| self-pin | the digest is recorded only inside the record itself | the detector reports the anchor as missing, never passes; KTD-AR-S-0003 §8 item 10 |
| inferred-zero | a closing snapshot fills an unknown counter with 0 | violation: the field must be cited or `could-not-recover` (§3 item 4) |
| uncited-fill | a snapshot fills a field with no durable-artifact citation | violation: §3 item 3 |
| in-place-close | "close" a record by editing its original bytes | violation: §3 item 1; the snapshot is a new file |
| deleted-superseded | a correction that removes the superseded reading | violation: §5; the old reading stays as the dated record it was |
| open-cited-as-closed | cite an `open-at-seat-close` record's numbers as settled | violation: §2; the citation must name the state |

## 7. What this procedure never proves

- **A digest match is integrity, not truth.** It says the bytes are unchanged since close; it says nothing about whether what was filed was correct at close (the same boundary `gate-frozen-run-standard.md` draws for frozen runs: digests are integrity, not verification of content).
- **Closed is not verified.** The closing snapshot's citations make its fields checkable; a reader who does not follow a citation has trusted, not checked.
- **Immutability is not tamper-proofing.** An actor who can edit a record's bytes can usually edit or delete its snapshot too; the anchor-outside rule and the incident history raise the cost and leave evidence (git history), they do not make active tampering impossible (the fixity analogy, KTD-AR-S-0003 §8 item 11).
- **The detector is backward-looking.** It sees edits after close only; a record closed with a wrong value stays closed-wrong until a successor row supersedes it (§5), which is why the per-field citations of §3 matter more than the pin.

## 8. Decision record — the rules this entry adopts

1. **Adopted:** every filed record in the lane's bookkeeping surface is either `open-at-seat-close` or closed, and a citation of an open record names it open (§2). Consequence: no number from an open record circulates as settled.
2. **Adopted:** a closing snapshot is a new file that names the record it closes, pins that record's SHA-256 at close time, fills each open field with a durable-artifact citation or `could-not-recover` with owner and reason, and never edits the original record (§3). Consequence: an in-place "closing" is a violation, not a shortcut.
3. **Adopted:** the close digest lives in the snapshot that closes the record, never only inside the record itself (§4; KTD-AR-S-0004). Consequence: a self-pinned record is outside this procedure's protection by construction.
4. **Adopted:** a digest mismatch against a close pin is filed as a finding with the history leg attached; it is never repaired silently, re-pinned to bless the edit, or treated as proof of who edited (§4). Consequence: the mismatch survives as evidence.
5. **Adopted:** corrections are successor rows with their own provenance; superseded readings are preserved as the dated record they were, and stale reproduction commands are recorded as attributions, not fixed by editing old runners (§5). Consequence: the record surface stays append-only in fact, not only in name.
6. **Adopted:** unknown counters and unrecoverable fields stay `null` / `could-not-recover` with an owner and a reason; never inferred zeroes (§3 item 4; KTD-AR-S-0002). Consequence: a gap in the record stays visible in every downstream reading.
7. **Rejected:** treating a digest match as truth, correctness or completeness — the match is never a clearance, and a closed record is never a verified record (§7). Reason: integrity is not verification; the boundary is the one the frozen-run standard already draws.
8. **Open (to-verify):** whether the close-digest detector should be a standing lane instrument — a sweep that recomputes every recorded close digest each round, in the posture of `reports/round-28/readme/sweep.py` — rather than a per-check manual step. Owner: the lane's tooling boundary; not disposed here.

## 9. Handoff note

- This entry ends at the handoff. It supplies: the lifecycle table, the six-item closing-snapshot contract, the detector procedure with its meaning table, the successor-row rules, the control set, and the decision rows. It decides nothing about any world and no verdict about any round.
- **To lore-shokunin and the integrator:** take (a) the lifecycle states wherever a handoff cites a round record, (b) the §3 contract as the shape any closing snapshot must satisfy, (c) §4's detector before quoting any record as unchanged, and (d) any `(to-verify)` items still open — they route through `to-verify-triage-protocol.md`, never into assertion.
- **Known limits of this entry:** the operating rule it methodizes (`AGENTS.md:32-39`) is the operator's and prevails over this file on divergence (file a successor row, never edit either side silently); the two literature anchors were not consulted this round; no close digest was computed or pinned here; the detector is stated as a manual procedure — the standing-sweep question is DR-AR-08.
```

## Self-audit (C05 inherits this reading)

Instrument: the round-35 C12 entry-audit bytes (`reports/round-35/cov/C12-audit-runbook.md`
§5, sha256 973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d),
installed to `.scratch/c04/` by the runbook's own extraction step and run with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

1. `--selftest` → exit 0, SELFTEST PASS.
2. `--fragments` over a scratch copy holding only this fragment, `--stage .scratch/c04/stage`
   → staged to `corpus/knowledge/verification/append-only-record-verification.md`.
3. First audit of the staged bytes → `PASS/review` (24277 bytes): one review-tier
   observation, `bleed-candidate:clearance` at the DR-AR-07 line — the word sat
   more than 70 characters from its negator; read as the ordinary negated sense
   it carries, and the line was reworded in place so the negation is adjacent.
4. Re-audit after the reword → `PASS/clean`, every expectation of the runbook's
   §6 held: 4/4 + 5/5 frontmatter, `verified_at_iso`, `pointers_unresolved: []`,
   `gap_named`, `decision_record`, 0 bleed candidates, 0 stale-pin candidates,
   0 ownership assertions. Both readings are recorded here; the filed bytes are
   the post-reword bytes (measured 2026-10-19 at HEAD dfb0719).

This is a structural reading of the bytes by a digest-pinned third-party
instrument — never a verdict on the scholarship, never an admission; C05's
independent audit and R01's fabrication hunt remain the round's own checks.

## Alternates considered (for the connector)

- **isolation-replay / runner reproduction** — rejected: it is claim Ca's live
  deliverable this round (the protocol is authored under
  `reports/round-39/calib/`, and `reports/round-39/calib/Ca02-replay-verify.md`
  already existed at write time); a corpus entry now would duplicate an
  in-flight artifact instead of filling a partition gap.
- **README index-sweep verification** — viable but weaker: the sweep instrument
  is already self-documenting (`reports/round-28/readme/sweep.py` docstring) and
  its method is folded into this entry's §4 posture; the append-only surface had
  the cleaner zero-hit sweep.
- **telemetry counting/attribution verification** — adjacent (KTD-AR-S-0002) but
  its requested-vs-observed method is an availability topic owned by the
  operator's telemetry rules; folded here only as the §2 lifecycle rows.

## Owed

- `reports/round-39/scout/K01-verification-gaps.md` — the partition-gap scout;
  absent at write time (probed 2026-10-19). My topic is self-scouted; if K01's
  four named topics differ, X00's collision matrix decides, and this fragment's
  §Alternates lists what I considered so a swap costs one message, not a redraft.
- `reports/round-39/plan/P01-plan.md` — the cross-claim plan; absent at write
  time. The entry contract was taken from the round-35/36 landed shape
  (`reports/round-35/cov/C12-audit-runbook.md` §1, `reports/round-35/cov/C04-timekeeping-spare.md`)
  and the verification-partition house style
  (`corpus/knowledge/verification/two-reader-interop-agreement.md`).
- C01–C03 — the sibling entry drafts; unknown at write time, collision handled
  by X00.
- C05 — independent audit of the staged bytes (the §Self-audit reading above is
  the baseline to reproduce or contradict).
- C06 — the README delta must carry this entry's `- topic:` text byte-equal as
  the new verification row (the round-20 repair rule, `corpus/README.md:96-99`),
  in filename order: `append-only-record-verification.md` sorts first among the
  four new rows if C01–C03 land `calibration-*`..`z*`-shaped slugs — C06 owns
  the actual ordering.
- The integrator — the corpus bytes stay fenced here; landing them moves
  verification 20 → 24 and the README to revision 2.2 per claim C.

## Citations

- `reports/round-39/claims.json:13-17,19-24` — claim C's counts/contract and
  claim Ca's successor-ledger work this entry's §5 supplies method for.
- `reports/round-39/targets.json` — `seats[id=C04].mission`, `shared_rules`.
- `reports/round-35/cov/C12-audit-runbook.md:26-52,99,184-185` — the entry
  contract readings (R35-4F-1/R35-5F-1), the instrument digest, and the
  pointer/gap/decision-record checks the §Self-audit ran.
- `reports/round-35/cov/C04-timekeeping-spare.md:10-19` — the r35/36 frontmatter
  shape (topic / gap filled / sources / source / couples / verified-at / recheck
  / scope) replicated here.
- `corpus/knowledge/verification/two-reader-interop-agreement.md` — the
  verification-partition house style (KTD source ids, calibration line, §
  numbered body, adopted/rejected/open decision rows).
- `AGENTS.md:5-6,18-25,32-39` — the operator rules grounded as KTD-AR-S-0001/-0002.
- `corpus/knowledge/verification/provenance-audit-ledger-format.md:140-155` —
  §8, read in full this round (KTD-AR-S-0003).
- `corpus/README.md:43-61,96-99,505-518` — revision 1.8 precedent, the round-20
  verbatim-row rule, the superseded footer reading (KTD-AR-S-0007).
- `reports/round-20/readme/gaps.md:18-20,54-57` — the in-place-edit incident and
  the stale-command precedent (KTD-AR-S-0008).
- `reports/round-37/calib/recount-ledger.json:68,81,94,107` — the four
  could-not-reproduce rows (KTD-AR-S-0009); row dispositions counted by
  `grep -c "could-not-reproduce"` → 6 occurrences of the string, 4 as row
  `disposition` values (the other 2 are the coverage note and a cause string).
- `reports/round-39/telemetry/dispatch-declared.json:25` — the live open record
  (KTD-AR-S-0010).
- `reports/round-28/readme/sweep.py:1-30` — the model checker docstring
  (KTD-AR-S-0011).
- Absence sweep + census outputs, measured 2026-10-19 at lane HEAD
  dfb0719711204b5943432034bd80c8dc248acddd: "closing snapshot" 0; "append-only"
  12 files; "could-not-recover" 0; close-digest variants 0; verification 20
  files; total 212 files. Dependencies probed absent at write time:
  `reports/round-39/scout/`, `reports/round-39/plan/`, `reports/round-39/cov/`
  (created by this fragment). Self-audit instrument selftest exit 0; staged-file
  audit PASS with zero contract defects and zero review observations.
