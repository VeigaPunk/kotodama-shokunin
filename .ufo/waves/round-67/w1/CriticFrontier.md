# CriticFrontier — attack on the rejected-row requirement (R66-D5 leg, accept-ca.py:D4)

Attacked: `reports/round-67/accept-ca.py` D4 (`:207-239`), cross-checked against
`reports/round-67/accept-c.py` (`NEW_IDS`/`EXTRA_IDS`/APPEND `:67-72,249-375`),
`reports/round-67/claims.json` C+Ca statements, `scripts/sources-census.sh`
(E03/E04/E12 rules), base `corpus/SOURCES.md`, r66 committed-row fragments, and
the r67 drafts already on disk.

## F1 — FATAL: ACCEPT-C-67 and ACCEPT-CA-67 are jointly unsatisfiable

D4 requires `rej_opened_today >= len(R66_REJECTS) + 2 = 6` rows with
`status=rejected` AND `opened==2026-10-24` (`accept-ca.py:226,235`). Enumerate
every legal id for the ≥2 extra rejected rows:

| id space for a new rejected row | verdict under frozen accept-c.py |
|---|---|
| S805–S828 (NEW_IDS) | ROWS leg `:267` requires `c[7]=='mined'` → FAIL |
| S801–S804 (EXTRA_IDS) | D4 `nonunique` (`:228-231`) + census E03 → FAIL |
| any other fresh id (S777, S778, S829+) | APPEND `extra_ids` (`:356-358`) → FAIL |
| any base id S001–S800 | APPEND immutable (`:360-371`): `opened` (c[8]) may not change; `rejected`+`2026-10-24` needs both → FAIL |
## F1 — C-APPEND vs Ca-D4 id conflict: unsatisfiable at a single lands commit — RESOLVED by L1 per-claim lands split (design finding stands)

D4 requires `rej_opened_today >= len(R66_REJECTS) + 2 = 6` rows with
`status=rejected` AND `opened==2026-10-24` (`accept-ca.py:226,235`). Enumerate
every legal id for the ≥2 extra rejected rows **at one lands commit**:

| id space for a new rejected row | verdict under frozen accept-c.py |
|---|---|
| S805–S828 (NEW_IDS) | ROWS leg `:267` requires `c[7]=='mined'` → FAIL |
| S801–S804 (EXTRA_IDS) | D4 `nonunique` (`:228-231`) + census E03 → FAIL |
| any other fresh id (S777, S778, S829+) | APPEND `extra_ids` (`:356-358`) → FAIL |
| any base id S001–S800 | `opened` (c[8]) immutable under APPEND (`:368-369`) → date can't move; but see F2: status CAN flip |

Triple-confirmed (this seat; CriticSizing FINDING 1; ScribeGateRows F7 replayed
the APPEND branch: base + one S829 → `appended=['S829'] extra=['S829']
append_ok=False`; ScoutReject2 source-level). The wave's pipeline already
drafted the losing move: `rows/ScoutReject{1,2}/row-S829..S832.txt` all carry
`| rejected | 2026-10-24 |`.

**L1 resolution (no counter revision):** per-claim lands commits — A_r (S801–S804
+ r66 dispositions) → A_c (C's lands: only S805–S828 over base, APPEND clean) →
A_ca (Ca's lands: adds S829+ rejects + lesson). APPEND's bound stays; D4 sees
≥6 dated rejects at A_ca. Correct within the letter — **design finding,
recorded per L1's ruling**:

- No single commit satisfies the joint predicate; the three receipts will
  stamp three different lands revisions. A non-author verifier replaying "the
  wave's accepted state" finds no revision where all claims hold at once.
- Claim C's own statement — "registry 724 -> 752 rows" — is true only
  transiently at A_c. At wave tip (A_ca + records) the registry is 756; the
  committed claim text is false against tip bytes. Transient-truth receipts
  are a new provenance shape; worth a QUALITY note if this becomes a pattern.
- claims.json's frozen text (`728 + 24` arithmetic, the D4 leg line ">=2
  rejected rows opened 2026-10-24 from the round-67 gate") still does not name
  where the two rejects get ids; the sequencing works only because accept-ca
  never re-checks APPEND at A_ca — a delegated-invariant dependency again.

Dead-code tell: `new_rejects` computed at `accept-ca.py:232-234`, never used.

## F2 — THE LIVE ATTACK (demonstrated): flip two mined rows → D4 PASS with ZERO new gate rejects

RevWaveShape ran the construction on a scratch clone (base tree + registry
edits): append S801–S804 as rejected/2026-10-24 AND flip two already-mined
base rows opened 2026-10-24 (S750, S751) `mined`→`rejected` in place, all
other cells untouched. Result measured:
`D4 PASS bad=[] r66_rejects=4 opened_today=6` and
`APPEND PASS missing_old=[] appended=4 extra=[] immutable_violations=[]`.

Mechanism: APPEND treats `status` (cell 7) as in-place mutable
(`accept-c.py:368-369`: `oc[:7]==nc[:7] and oc[8]==nc[8]` → status/recheck/
used-by flips are legal), while D4 counts by the `opened` cell, not by append
(`accept-ca.py:235`). Base holds 49 eligible mined rows opened 2026-10-24.
So "first-class rejected rows from the round-67 gate" is satisfiable by
**decommissioning already-admitted, entry-cited sources** — a coverage
regression masquerading as a discernment gain. Worse: the flipped rows remain
cited by their entries (ONEID only counts NEW_IDS; E11 only validates mined
used-by; nothing flags a `rejected` row whose `used-by` still names a live
entry). The registry can end the round with rejected-but-cited rows and every
leg green.

This bypass survives L1's A_c/A_ca sequencing unchanged — at A_c the status
flips are permitted in-place edits; at A_ca D4 counts them. The intended
predicate ("≥2 round-67 gate rejects") is enforced nowhere: D4 measures
"rejected + opened=2026-10-24", a property of the cells, not the gate.

Also under D4-alone (no accept-c): mutating any base rejected row's `opened`
to 2026-10-24 counts toward the 6 — accept-ca contains no base-diff, so the
freshness invariant is entirely delegated (see F1). Alone gameable, paired
bypassable.

**Smallest safe correction (pre-data revision, both halves):** (a) widen
`EXTRA_IDS` to the declared reject-id range so appended rejects are legal
(matches seat drafts S829–S832); (b) make D4 count only *appended* ids —
`new_rejects` (already computed, dead) restricted to the declared set — AND
require `REJECTED:`/`flip:` teaches + `used-by=='—'` for every rejected row
counted, new or r66. Without (b) the flip path stays green forever; without
(a) the honest path stays closed.

Peer datum: ScribeGateRows F7 measures the drafted S829/S830 teaches cells at
274/311 chars against the gate's 240-char budget (gate-rows.md:152) — a
draft-level defect for the integrator, not a counter defect.

## F2b — The mandated S753 reject shrinks "≥2 new gate rejects" to ≤1

RevCensusE12 measured: moving S776 into `## Registry` creates E04 — S776
duplicates S753's URL+scope, and S776's teaches is APPEND-immutable so
`supersedes S753` cannot be added. For census validate to exit 0 (Ca's own D2
leg), S753 must flip to `rejected` — which criterion 18's durability logic
independently mandates (its committed capture replayed a 302-stub). S753 was
opened 2026-10-24: the flip counts toward `rej_opened_today`. So the r66-D2
disposition itself supplies one of the two "extra" rejects, and with F2's
mined-flip supply the honest-seeming number of *new gate* rejects needed is
**zero**. The claim's "≥2 round-67 gate rejects" is satisfiable entirely by
durability decommissions — the count is provenance-free either way.

## F2c — Sequenced-lands residuals the ruling leaves open (closure must enforce)

- **A_ca appended-set is unbounded.** C's APPEND holds only at A_c; no counter
  bounds what else lands between A_c and A_ca — a stray well-formed row
  (`| S900 | … | mined | 2026-10-24 |`) rides in unchecked (CriticR66Dispositions).
  Closure must diff A_c→A_ca to the declared set (S829–S832 + lesson +
  dispositions) or bound it in a revision.
- **Receipts are revision-scoped, not tip-stable.** Re-running frozen accept-c
  at A_ca/tip prints `APPEND FAIL extra=['S829',…]` on honest bytes
  (MutCounterC measured). Records must name each claim's own lands; check-
  receipt-seq cannot distinguish "expected-stale" from "defect" (RevToolSeq).
- **Placement:** S829+ must sit inside `## Registry` — D4 is section-blind but
  D2's census flags E12 (RevBaseCensus). And S829+ are invisible to E11
  (usedby_findings filters status==mined) — rejected rows have no used-by
  validation at all.
- **Stale control receipts:** accept-ca.py was revised post-control (QUOTES
  `\bS(8[0-2]\d)\b` → `\b(S8[0-2]\d)\b`; counter sha 5e8915ac… → 5382ffed…).
  Rev0's QUOTES leg was unreachable (bare-digit capture never intersects the
  S805–S828 set) so dry-run-ca's QUOTES FAIL was a false-positive control
  reason; the fix is correct but the filed control pins dead bytes —
  regenerate controls-ca/dry-run-ca or record a statement_revision bump
  (RevDryRunFidelity, RevEntrySpec, RevCounterCa).
- **Instrument hygiene:** counter self-sha and check-receipt-seq's SHA leg
  read worktree bytes, so each clone must carry its own lands' counter bytes
  (CriticReceiptDiscipline, SentinelScope); `CENSUS` is a host-absolute path
  (accept-ca.py:54) — absent file raises instead of a FAIL leg (RevBaseCensus).
- **Dirty-clone PASS minting (RV-1, RevengerReceipts, verified here):**
  accept-c/o compute `dirty_tracked` but never gate `stamp_ok` on it
  (accept-c.py:184-205, stamp_ok :200; accept-ca has no porcelain check at
  all), and the porcelain call passes `--untracked-files=no` — a materialized
  clone with planted untracked or dirty tracked bytes prints PASS receipts
  not backed by the stamped tree. Under three lands revisions this is the
  cheapest false-stamp class: the clone's worktree IS the measurement.

## F3 — Nothing stops a mined-disguised reject: S801–S804 need only two substrings

For the four r66 candidates D4 checks exactly: exists once, `c[7]=='rejected'`,
`"REJECTED:" in c[6]`, `"flip:" in c[6]` (`:221-225`). Unchecked: kind/tier
enums, anchor quote, capture URL, `used-by=='—'` (a `rejected` row may name a
live entry path; E11 only validates `mined` rows), and — fatally — whether the
teaches text matches any committed evidence.

The committed fragments are *already mined rows*:
`.ufo/waves/round-66/rows/ScoutReject0{1..4}/row-S80{1..4}.txt` all carry
`| mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`,
and ScoutReject01–04's verdicts were **ADMIT** (4/4). The disposition flips
`mined`→`rejected` and prepends `REJECTED: …; flip: …` — the counter cannot
distinguish a reasoned reject from a post-hoc label.

Checkability of the four reasons from committed evidence (if the r66 wave tree
lands as commanded): RevLoreHandoff.md supplies derivable reasons for S801
(cosmetics already owned by `adornment-body-codes.md:68-73`), S802
(miasma/humoral = myth-symbol purity territory), S804 (airing =
`ritual-garments.md`) — but **S803** (relic-scent veneration) has no committed
reject rationale anywhere in the wave evidence; any `REJECTED:` text written
for it is unverifiable post-hoc, and `claims.json` itself concedes this to
`review_only` ("semantic adequacy of each rejected row's teaches cell").

## F4 — Provenance is optional: D1 does not require the row fragments

D1 (`:122-155`) requires ≥8 seat reports matching
`.ufo/waves/round-66/w1/*.md` and that *some* EXCLUDE lines exist — it never
requires `INCLUDE .ufo/waves/round-66/rows/...`. A manifest that names
`rows/` as an excluded scratch tree passes D1 while S801–S804 keep zero
committed provenance, and D4 still passes. The "committed wave evidence" that
would let a re-deriver check the reject reasons is excludable by construction.

## F5 — The bar is inverted: new rejects need *less* than S801–S804

The ≥2 new rejects need only correct `status`/`opened` cells — no
`REJECTED:`/`flip:` teaches requirement (that substring check is
R66_REJECTS-only), no anchor quote, no capture, no tier floor (drafted S829 is
tier C, legitimately). W02 (`thin reject reason`) warns only below 8 chars and
never fails. URL novelty: E04 exempts any duplicate where the new row is
`rejected` (`sources-census.sh`: `status!="rejected"` guard + the
rejected-pair exemption fixture), and accept-c LINK covers NEW_IDS only — the
drafted S830 is a self-declared URL-duplicate of S252 and passes every
automated leg. Fabricated-on-demand rejects are cheaper than the r66-backed
ones. Severity is inverted: the rows with real provenance get the most
substance checks.

## F6 — Minor: section-blind counting, duplicate-id arithmetic

D4 scans `reg.splitlines()` file-wide; a `| S9xx | … | rejected | 2026-10-24 |`
line under `## Search log`/`## Leads` counts (bounded only by census E12 —
another delegated defense). `rej_opened_today` double-counts duplicated ids
(the `once` map covers S801–S804 only; E03 bounds the rest — delegated again).

## Answer to the three seeded questions

1. **Fewer than 2 new rejects?** The count is a hard `>= 6`; with S801–S804
   `opened=2026-10-24`, ≥2 extra rejected+dated lines are required — but "new
   rejects" is not what D4 measures. RevWaveShape demonstrated `D4 PASS` +
   `APPEND PASS` with **zero** new rows by flipping two today-opened mined
   rows (F2), and the r66-D2 repair itself mandates one such flip (S753, F2b).
   Meanwhile the id space for honest appended rejects collided with C's
   APPEND bound — L1 resolved *that* by per-claim lands separation (A_r < A_c
   < A_ca; F1), leaving the flip bypass green.
2. **What stops a mined-disguised reject?** Two substrings (`REJECTED:`,
   `flip:`) — and only for S801–S804; the ≥2 new rejects need no teaches at
   all (F5). Nothing else: no evidence binding, no provenance check, no
   used-by constraint, and the committed fragments are already mined-shaped
   (F3, F4). The flip path (F2) is the fully-realized version of this attack.
3. **Are the r66 candidates' reject reasons checkable from committed
   evidence?** Partially at best: S801/S802/S804 have derivable
   scope-ownership arguments in committed RevLoreHandoff.md; S803 has none.
   And checkability itself is optional — the fragments can be EXCLUDE-d out of
   the D1 manifest (F4), leaving all four reasons unverifiable post-hoc while
   every leg prints PASS.

## Impacted axes

- **calibration (Ca):** D4's intent ("first-class rejected rows", "≥2 from the
  round-67 gate") is enforced nowhere: satisfiable by zero new gate rejects
  via mined-flips (F2) and the mandated S753 decommission (F2b); S801–S804
  need only two substrings against committed evidence that can be excluded
  from D1's manifest (F3, F4). Satisfiable under L1's sequencing — but
  satisfiable *dishonestly*.
- **coverage (C):** verdict is lands-scoped, not tip-stable — honest re-runs
  at A_ca print APPEND FAIL extra=[S829…] (F2c). Claim C's "752 rows" is true
  only at A_c and false at wave tip; records must carry the per-claim lands
  map explicitly (exists today only in the orchestrator ruling, not
  claims.json's receipt_protocol).
- **operability (O):** the three-lands sequencing makes check-receipt-seq's
  missing stamped-vs-lands leg load-bearing (RevToolSeq): an A_c-legal receipt
  is indistinguishable from a stale one at A_ca.

## Smallest safe correction

Under L1's ruling (no revision; A_r < A_c < A_ca), the wave is executable. The
remaining exposure is *dishonest satisfiability*, fixable only by revision —
which the ruling declines — or by committed reviewer enforcement at closure:
1. **Closure obligation (free, no counter change):** the r67 records must
   name all three lands revisions, scope C's "724 -> 752" to A_c, and diff the
   A_c→A_ca registry delta to the declared reject set — that catches the F2
   flip path and the unbounded A_ca append (F2c).
2. **If revision is ever permitted:** (a) `EXTRA_IDS` += declared reject ids
   (matches drafted S829–S832); (b) D4 consumes the dead `new_rejects` —
   `new_rejects >= 2` over *appended* ids only, with `REJECTED:`/`flip:` and
   `used-by=='—'` required on every counted rejected row; (c) regenerate
   controls-ca/dry-run-ca at the current counter sha (stale at 5e8915ac vs
   live 5382ffed).
3. Absent both, D4's PASS proves only "≥6 cells say rejected+2026-10-24" —
   a count, not the R66-D5 disposition it claims to evidence.

## Evidence index (all base-tip bytes, lane = kotodama-shokunin)

- `reports/round-67/accept-ca.py:207-239` (D4), `:232-234` (dead `new_rejects`)
- `reports/round-67/accept-c.py:67-72` (NEW_IDS/EXTRA_IDS), `:249-252` (SET),
  `:254-278` (ROWS), `:349-375` (APPEND)
- `reports/round-67/claims.json` C statement "724 -> 752"; Ca statement "+ >=2
  round-67 gate rejects"; Ca `review_only` admits teaches semantics unchecked
- `scripts/sources-census.sh` gawk validate: E03 duplicate id, E04
  rejected-exempt dup-URL (`status!="rejected"` guard), E12 outside-Registry,
  W02 warn-only thin reject reason
- `reports/round-67/telemetry/dry-run-ca.txt`: `D4 FAIL …
  rejected_opened_today=0` on base (control correctly fails pre-data)
- `.ufo/waves/round-66/rows/ScoutReject0{1..4}/row-S80{1..4}.txt`: all
  `| mined | 2026-10-24 | … | scent-perfume-aromatics-codes.md`; scout
  verdicts ADMIT ×4
- `.ufo/waves/round-66/w1/RevLoreHandoff.md:55-57,167-173`: committed
  reject-rationale material for S801/S802/S804 only
- `.ufo/waves/round-67/rows/ScoutReject{1,2}/row-S8{29..32}.txt`: drafted
  `rejected | 2026-10-24` rows, ids outside accept-c `allowed_new`; S830's own
  VERIFY names it a duplicate of S252's live URL
- `corpus/lessons/round-66-verifier-spotcheck.md:45-48,91,106`: R66-D5 routing
  (first-class rejected rows required; fragments untracked)

Tooling: none installed (pacman pause respected; no tools needed beyond
git/grep).
