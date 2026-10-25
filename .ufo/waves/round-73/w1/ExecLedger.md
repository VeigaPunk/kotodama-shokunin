# ExecLedger — round-73 wave-1 calibration ledger (draft)

Seat: ExecLedger (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base: `8841ad3b896a0227674fa0725b818c999118046f` (lane HEAD at the time of writing; claims
`reports/round-73/claims.json` status DRAFT-v0, read-only to this seat).
Claim attacked: **Ca** (calibration/records). No live fetches were made in this seat, so no
User-Agent record applies. No tool installs, no pacman.

## 0. Deliverables

| path | what |
|---|---|
| `.ufo/waves/round-73/w1/drafts/ledger-draft.json` | 12 pairs `{id, stated_at, stated_text, observe_cmd, parse, observed_at_base, expected_after, disposition, why}` + a `convention` block (17 535 B) |
| `.ufo/waves/round-73/w1/ExecLedger.md` | this report |

Nothing else was written. `git status --porcelain` in the lane is unchanged from before my seat
(`?? .ufo/waves/round-72/w1/ScoutMergeScan.md`, `?? .ufo/waves/round-72/w1/ScribeLesson.md`,
`?? .ufo/waves/round-73/`, `?? reports/round-73/`); the fleet repo was read only.

## 1. Ledger at a glance — 12 pairs, 11 REPAIR, 1 ANNOTATE

| id | stated_at | stated token | observed at base | disposition |
|---|---|---|---|---|
| P01 | LOG.md:4284 | "Seat reports in .ufo/waves/round-72/w1/." | 2 untracked seat reports (R1) | REPAIR |
| P02 | SCORECARD.md:1401 | "ACCEPT-CA-72 PASS legs=12/12 at the measured revision" | both CA-72 receipts read FAIL; 0 PASS receipts (R2) | REPAIR |
| P03 | SKILL.md:697 | registry's last accept row is `accept-o-69` | 0 rows for accept-c-71/ca-71/d-71, though all 3 gate files exist (R3) | REPAIR |
| P04 | SKILL.md:697 | same | 0 rows for accept-c-72/ca-72, though both gate files exist (R3) | REPAIR |
| P05 | corpus/README.md:732 | "Total knowledge entries: 243." | 245 `.md` files | REPAIR |
| P06 | corpus/README.md:407 | "## culture-material/ (36)" | 38 files | REPAIR |
| P07 | corpus/README.md:3 | newest revision block is 2.21 (round-71) | 0 index rows for the 2 round-72 entries | REPAIR |
| P08 | SHONEN.md:6 | "`:468` (Error patterns)" | heading at SKILL.md:505 | REPAIR |
| P09 | SHONEN.md:6 | "`:522` (Checklist)" | heading at SKILL.md:564 | REPAIR |
| P10 | SHONEN.md:6 (+:8,:10,:12) | "no non-author verifier on record" | non-author verifier record committed at corpus/lessons/round-72-verifier-spotcheck.md:3 | REPAIR |
| P11 | LOG.md:4280 | "pre-data corrections F1-F9 + SCOUT-LIVE" | ids are F1,F2/F3,F4,F5,F6,F8,F9,SCOUT-LIVE — **F7 absent** | ANNOTATE |
| P12 | corpus/README.md:736 | "(total 243 files; directory totals 30/29/36/29/24/95)." | 245 files, culture-material 38 | REPAIR |

All 12 are mismatches at base, so the claim's BASEMISMATCH leg (≥ 8) is satisfied with margin.
Every `observe_cmd` was executed at base and its match count equals the value recorded in
`observed_at_base` (re-run transcript in §5).

## 2. Per-pair evidence (command → observed → expected after)

`LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin`, `REV=8841ad3b896a0227674fa0725b818c999118046f`.

### P01 (R1) — two round-72 seat reports never committed
```
git -C LANE ls-files --others --exclude-standard -- .ufo/waves/round-72
→ .ufo/waves/round-72/w1/ScoutMergeScan.md
  .ufo/waves/round-72/w1/ScribeLesson.md
```
34 of the 36 files in that directory are tracked (32 seat reports + `dispatch.json`,
`dispatch.err`, `spec.json`, `swarm-registry.json`); only the two seat reports are not. The
round-72 verifier record names the same defect at `corpus/lessons/round-72-verifier-spotcheck.md:14`
("defect R1"). **Expected after:** 0 untracked files, 36 tracked.
*Repairable:* committed-tree state, no filed text asserts the untracked state, so no correction
row is owed — a plain `git add` closes it.

### P02 (R2) — SCORECARD says PASS, the receipt says FAIL — and the rerun now PASSES
```
git -C LANE grep -n -H -E '^ACCEPT-CA-72: (PASS|FAIL) legs=12/12$' REV -- reports/round-72/telemetry
→ REV:reports/round-72/telemetry/controls-ca.txt:28:ACCEPT-CA-72: FAIL legs=12/12
  REV:reports/round-72/telemetry/measures-ca.txt:29:ACCEPT-CA-72: FAIL legs=12/12
```
`controls-ca.txt` is the do-nothing control (FAIL correct by design). `measures-ca.txt` is the
round-72 measures receipt, stamped lands `21ad3088cb64…` / tree `e4e49089…` / counter
`f080c240ffdc47f0`, and its failing legs are `REPORTCORR fleet-rev=MISSING` and
`REPORTLAST report-names-lands=False`. `git grep 'ACCEPT-CA-72: PASS'` over the whole base tree
matches only prose (`CritFrozenLegs.md:35`, `dispatch.json:274`, `spec.json:48`,
`claims.json:22` after-text, `SCORECARD.md:1401`) — **zero PASS-stamped receipts**.

I then ran the counter itself at base:
```
python3 -B reports/round-72/accept-ca.py --root . \
  --lands 21ad3088cb64f7275e5541804e168f15d21d26d0 --fleet-root /home/vgpnk/Projects/shokunin
→ LEG PASS QUAL20 / W2FILES 7/7 / LOGCORR / LESSONCORR
  LEG PASS REPORTCORR  fleet-rev=80d8c9b576d4
  LEG PASS MAPCORR / CASTAMP commit=5593803ff5d1 / QUAL21 / CAPOEIRA
  LEG PASS APPENDONLY removed=0 numstat-del=0 w2-changed=7 unauthorized=[] fleet-r71-last=f47ad6ba8d30
  LEG PASS REPORTLAST  commits=10 report-names-lands=True
  LEG PASS NOHARM      census exit=0
  ACCEPT-CA-72: PASS legs=12/12      (exit 0, wall 2.4 s)
```
The run's counter self-hash `f080c240ffdc47f0` and lands tree `e4e490892002c662` are exactly the
receipt header's own stamp/tree, so the only variable that moved is the fleet report's last-touch
commit: the FAIL was stamped before the fleet report's errata landed. **Expected after:** ≥ 1
`ACCEPT-CA-72: PASS legs=12/12` line from a NEW append-only receipt under
`reports/round-72/telemetry/` (stamped at lands `21ad3088`, tree `e4e49089`, counter
`f080c240`, produced inside a materialized clone per QUALITY 17/19); `measures-ca.txt` and
`controls-ca.txt` bytes untouched.
*Repairable, not annotate-only* — and the round-72 verifier's own routed remedy
(`corpus/lessons/round-72-verifier-spotcheck.md:66`) is exactly this: "Commit the ACCEPT-CA-72
post-report rerun receipt … or append a correction". Caveat for wave 2: my run was
worktree-rooted, so it is evidence, not the receipt. Independently produced sibling receipts in
the same drafts directory agree (PASS at lands `21ad3088`, `11a41fbf`, `ac0d18ee`; FAIL at
`3adbd4ab`, `8841ad3b`, where the report's last-touch commit no longer names those lands) —
the PASS is specific to lands `21ad3088`, which is precisely the stamped revision.

### P03/P04 (R3) — SKILL.md §Gates registry is missing five rows for existing gates
```
git -C LANE grep -n -E '^\| accept-(c|ca|d)-71 \|' REV -- SKILL.md   → 0 matches (exit 1)
git -C LANE grep -n -E '^\| accept-(c|ca)-72 \|'  REV -- SKILL.md    → 0 matches (exit 1)
```
The registry's last accept row is `| accept-o-69 | gate |` at `SKILL.md:697`. A full diff of gate
files against registry rows at base (`git ls-tree -r --name-only REV -- reports`) gives 41 gate
files, 36 rows, and exactly five gates with no row: `accept-c-71`, `accept-ca-71`, `accept-d-71`,
`accept-c-72`, `accept-ca-72` (and zero rows with no gate file). **Expected after:** five rows in
the house shape of `accept-o-69` (entry command, verdict map, self-test cell, `—` pinned values,
read-only write scope, owner `kotodama-shokunin`).
*Repairable:* live registry; claim Ca's APPENDONLY leg permits in-place edits to SKILL.md registry
rows and requires each edit be listed in the ledger — both pairs are listed here.

**Claim-text correction for freeze:** R3 as drafted says the registry lacks
"accept-ca-70..72 / accept-c-70..72". `reports/round-70` contains **no** `accept-*.py` at all
(`claims.json`, `corrections-r69.md`, `telemetry/` only), so no round-70 row is owed and the
"70" half of the range names gates that do not exist. The real gap is the five round-71/72 rows
above.

### P05/P06/P12 — corpus/README.md footer and index are two landings behind
```
git -C LANE ls-tree -r --name-only REV -- corpus/knowledge                    → 245 matches
git -C LANE ls-tree -r --name-only REV -- corpus/knowledge/culture-material   → 38 matches
```
Cross-checks at the same revision: `find corpus/knowledge -type f -name '*.md' | wc -l` = 245, and
the README's own named instrument
`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` returns
`totals.files = 245` with `read_only: true`. The other five headings reproduce exactly at base
(linguistics 30, myth-symbol 29, synthesis 29, verification 24, civilizations 95); only
culture-material is wrong (36 declared vs 38).
```
git -C LANE grep -c heritage-taxonomy REV -- corpus/README.md   → 0 matches (exit 1, no output)
```
Cause, traced in git: the 243 footer was written at `498db73` (round-71 dance landing);
round-72's `770100f` added `culture-material/heritage-taxonomy-models.md` and
`heritage-taxonomy-models.amend-2026-10-24-r13.md` with no README reconcile, so the footer's own
"Counts checked 2026-10-25" stamp predates a same-day landing.
**Expected after:** a dated appended `Total knowledge entries: 245.` line; heading
`## culture-material/ (38)`; counts-checked cell `30/29/38/29/24/95`; two index rows naming both
round-72 files plus a revision block — with the 243 reading preserved as superseded text.
*Repairable:* live index. The lane already treats an unindexed entry as a defect
(`corpus/knowledge/verification/index-sweep-verification.md:40`: totals line must equal the file
total, one row per entry). P05 and P12 are split because one is the totals statement and the other
is the evidence line naming the measuring command — repairing only one leaves the footer
self-contradictory, which is the round-19 README-reconciliation failure mode.

### P08/P09 — SHONEN's SKILL.md line pointers are stale
```
git -C LANE grep -n -E '^## Error patterns$' REV -- SKILL.md
→ REV:SKILL.md:505:## Error patterns                       (SHONEN states :468)
git -C LANE grep -n -E '^## Checklist \(executable where a tool exists\)$' REV -- SKILL.md
→ REV:SKILL.md:564:## Checklist (executable where a tool exists)   (SHONEN states :522)
```
The sibling pointer `SKILL.md:20` (Decision table) is correct and is **not** a pair.
**Expected after:** SHONEN.md:6 reads `:505` and `:564`.
*Repairable:* SHONEN.md is not in claim Ca's APPENDONLY file set (LOG.md, SCORECARD.md,
`corpus/lessons/round-72.md`, `corpus/lessons/round-71.md`, fleet report), so an in-place pointer
fix is permitted and is listed in this ledger.

### P10 — "no non-author verifier on record" ×4, but a non-author verifier record is committed
```
git -C LANE grep -n -E '^author: hyaku closure \(non-author integrator' REV -- \
  corpus/lessons/round-72-verifier-spotcheck.md
→ REV:corpus/lessons/round-72-verifier-spotcheck.md:3:author: hyaku closure (non-author integrator, @m_kfc)
```
The phrase appears verbatim four times (`SHONEN.md:6, :8, :10, :12`). **Expected after:** 0
occurrences; each box names the record (`corpus/lessons/round-72-verifier-spotcheck.md`,
2026-10-25, `@m_kfc`) and states that it did **not** promote the box — its Step-1 row logs the
boxes as "author assertions" — so every mark stays `[~]`.
*Repairable:* live checklist. The literal claim is false at base (a record exists). A reader also
cannot distinguish "no record" from "a record that declined to adjudicate"; naming the record and
its non-promotion is honest under both readings and avoids a mark flip the evidence does not
support.

### P11 — "F1-F9" names an id that is not documented
```
git -C LANE grep -c '"id": "F7"' REV -- reports/round-72/claims.json   → 0 matches (exit 1)
```
The committed `pre_data_corrections` ids are `F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE` — and
they already were at the freeze commit `a7ab3bd`, whose own message says "pre-data corrections
F1-F9+SCOUT-LIVE"; the fleet report repeats the range at `.ufo/reports/round-72/kotodama.md:7`.
The **count** is not the defect (8 entries cover nine numbered slots plus SCOUT-LIVE); the defect
is the range token implying a documented F7.
**Expected after:** a `SCORECARD.md` row under `## Corrections — round 73` naming P11, the stated
token `F1-F9`, the observed id set `F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE (F7 absent)` and the
re-derivation command.
*Annotate-only:* both statements are filed history (LOG round-72 entry, fleet report) that this
lane may not rewrite, and nothing in the live tree can make `F1-F9` true without rewriting frozen
bytes — which claim Ca's kill rule forbids.

## 3. NOT-A-MISMATCH controls (reproduced, therefore excluded from the ledger)

Each was run; each reproduced its statement, so none may enter the ledger.

| # | statement | command → output | ruling |
|---|---|---|---|
| N1 | SHONEN.md:6 "412 rows after round 56 — 367 mined, 35 queued, 10 rejected … census exit 0 in reports/round-56/telemetry/final-measures.txt" | `git show c8af23f3:corpus/SOURCES.md` parsed → **412 rows {mined 367, queued 35, rejected 10}**; same at landing `767040e`; `final-measures.txt:63` = `census exit 0` | **Dated statement, exactly true for its scope.** Live registry is 799 (704/58/37), but the token is explicitly date-scoped ("after round 56"), corroborated by SCORECARD:1098 (358 → 412; 313/35/10 → 367/35/10) and by the round-56 receipt. A dated record is not stale by definition. Non-defect; at most a style note that the promotion checklist carries no *current-state* row count |
| N2 | SCORECARD.md:1401 "8 routed defects K71-1..K71-8" vs its 9-item parenthetical | `grep -o 'K71-[0-9]' .ufo/reports/round-72/kotodama.md \| sort -u \| wc -l` → **8** | Consistent: the fleet report defines exactly K71-1..K71-8, with K71-1 covering two items (QUALITY 20 + 7 w2 files) and K71-4/K71-5 the two in-place edits |
| N3 | LOG.md:4284 "One v1 wave of 32 seats … 16/32 attack roles = 50%: reviewer 6, critic 5, mutation-tester 3, sentinel 1, revenger 1" | `.ufo/waves/round-72/w1/swarm-registry.json` → **32 members**, attack roles **16 (50%)**, roles {reviewer 6, critic 5, mutation-tester 3, sentinel 1, revenger 1, scout 7, executor 4, scribe 3, connector 1, simplifier 1}; `dispatch.json counts.spawn = 32`; `dispatch.err` 0 B | Consistent |
| N4 | SCORECARD.md:1405 "lesson round-72 carries ## Gate (2 admits + 2 refuses …)" | `awk '/^## Gate/,/^## Mistakes/' corpus/lessons/round-72.md` → 2 `S87*` rows, 2 `admitted`, 2 `rejected` | Consistent |
| N5 | SCORECARD.md:1402 / LOG "797 → 799 rows", "797-row registry at base b60c7b1" | rows at `b60c7b1` = **797**, at `8841ad3` = **799** | Consistent |
| N6 | SHONEN.md:12 box-4 pointers (`sign-languages-manual-modality.md` §15/§2, `.ufo/waves/round-51/build/ConnectSiblingSign.md`) | all resolve; §15 is `## 15. Scope` and carries the lore handoff, §2 is `## 2. One-owner boundary` | Consistent |
| N7 | SHONEN.md:10 cited commits `1923bfe`, `4ad2683`; box-2 `2b956d7`, `364eeff`; box-1 `d761ee8` | `git cat-file -e <rev>^{commit}` → all ok | Consistent |
| N8 | round-72 lesson Quarantine "7 register ids → 8 staged ids" | `.ufo/waves/round-72/assimilation/reg-to-staged.txt` shows `S792 → ['S875','S933']` (many-to-one), all 7 registers present | Consistent |
| N9 | LOG.md:4283 id-renumber-map old→new (S874→S1005, registry_count 797, collisions 15, next_free S874) | `git show REV:.ufo/waves/round-71/assimilation/id-renumber-map.json` → registry_count **797**, 15 collisions, next_free **S874**, span **S874→S1005** | Consistent |
| N10 | SCORECARD.md:1402 "ACCEPT-C-72 PASS legs=10/10" | `reports/round-72/telemetry/measures-c.txt` last line `ACCEPT-C-72: PASS legs=10/10`, exit 0 | Consistent |

## 4. Repairable vs annotate-only

- **Repair (11 pairs).** Rule applied: a statement in *live* bytes — SKILL.md registry, SHONEN.md,
  `corpus/README.md`, or committed-tree state — is repaired in place (the claim's APPENDONLY leg
  allows exactly SKILL.md registry rows and the README footer/index, and SHONEN.md is outside that
  file set entirely). P01/P02 are repaired on the tree/receipt side so no filed text is edited:
  P01 by committing the two seat reports, P02 by committing a **new** PASS receipt while
  `measures-ca.txt` stays byte-identical.
- **Annotate-only (1 pair, P11).** Rule applied: a statement in *filed history* (round-72 LOG
  entry, fleet report) is corrected only by an appended `SCORECARD.md` row under
  `## Corrections — round 73` naming id + stated token + observed token + re-derivation command.
  Rewriting the LOG line or the fleet report would violate APPENDONLY and the claim's kill rule.
- No pair is both. No pair was left un-dispositioned. P02 was drafted as ANNOTATE in my first pass
  and moved to REPAIR only after the rerun actually printed PASS at the stamped lands — the
  disposition follows the exercised result, not the expectation.

## 5. Verification transcript (re-run of every observe_cmd, at base)

```
P01 REPAIR   exit=0 matches=2   .ufo/waves/round-72/w1/ScoutMergeScan.md ; .../ScribeLesson.md
P02 REPAIR   exit=0 matches=2   controls-ca.txt:28 FAIL ; measures-ca.txt:29 FAIL
P03 REPAIR   exit=1 matches=0   (no accept-c/ca/d-71 row)
P04 REPAIR   exit=1 matches=0   (no accept-c/ca-72 row)
P05 REPAIR   exit=0 matches=245
P06 REPAIR   exit=0 matches=38
P07 REPAIR   exit=1 matches=0   (no heritage-taxonomy row in corpus/README.md)
P08 REPAIR   exit=0 matches=1   SKILL.md:505 ## Error patterns
P09 REPAIR   exit=0 matches=1   SKILL.md:564 ## Checklist (executable where a tool exists)
P10 REPAIR   exit=0 matches=1   round-72-verifier-spotcheck.md:3 author: hyaku closure (non-author integrator
P11 ANNOTATE exit=1 matches=0   (no "id": "F7")
P12 REPAIR   exit=0 matches=245
pairs: 12  REPAIR: 11  ANNOTATE: 1
```
Every count above equals the `observed_at_base` string stored in `ledger-draft.json`.

## 6. Routed to freeze (claim-text corrections, pre-data)

1. **R2 is repairable, not merely annotatable.** Ca's REPAIR leg already allows the rerun-receipt
   route; wave 2 should take it, because the rerun prints PASS at lands `21ad3088` (exercised
   twice: by me and by a sibling seat). If the receipt is not produced before freeze, the pair
   must be re-dispositioned ANNOTATE — the SCORECARD row cannot stand against a FAIL-only receipt.
2. **R3 wording.** Replace "accept-ca-70..72 / accept-c-70..72" with the five gates that actually
   lack rows: `accept-c-71`, `accept-ca-71`, `accept-d-71`, `accept-c-72`, `accept-ca-72`.
   `reports/round-70` has no `accept-*.py`.
3. **Ledger shape.** The LEDGER leg lists `{id, stated_at, stated_text, observe_cmd,
   expected_after, disposition}`; the draft adds `parse`, `observed_at_base`, `why`, and the
   counter needs `parse` to recompute observed from committed bytes. Keep them at freeze.
4. **Pair count.** Ca declares ">= 8 pairs"; this draft carries 12 (11 mismatches plus one
   annotate-only), so the freeze can raise the floor to 12 without weakening anything.
5. **New mismatch not in Ca's before-text:** the README index has **no** rows for the two
   round-72 entries and its newest revision block is 2.21 (P07) — an unindexed-entry defect of the
   class `index-sweep-verification.md:40` forbids, not merely a stale number.
6. **Also new:** `LOG.md:4280` "F1-F9" names an undocumented F7 (P11). If a pre-data correction is
   preferred over an annotation, the honest fix is a LOG-appended correction line; the ledger
   default is ANNOTATE because the LOG entry is filed history.

## 7. Risks and blockers

- **P02 receipt provenance.** My rerun is worktree-rooted. QUALITY 17/19 require the committed
  receipt to be produced inside a materialized clone of lands; wave 2 must re-run there and record
  the clone path, the lands revision, its tree hash and the counter sha256. A PASS at any revision
  *other* than `21ad3088` does not repair P02 (the receipt is stamped at `21ad3088`).
- **P10 is a judgement pair.** If wave 2's reviewer reads "no non-author verifier on record" as
  "no verifier adjudicated these boxes", the pair can be re-dispositioned NOT-A-MISMATCH; the
  evidence for that reading is the spot-check's own Step-1 row ("author assertions"). I kept it as
  a REPAIR because the literal sentence is false at base and the naming repair is honest under
  both readings.
- **P05/P06/P12 must land together** or the footer contradicts itself; a counter that checks only
  the totals line will accept a half-repair.
- **No blockers.** Every pair was observed by running its command at base; nothing was inferred
  from the claims text alone.

## 8. Inbound peer traffic (recorded, not acted on)

`R50ReopenRowS105` sent a round-50 `spans.tsv` offset flag and then **retracted** it in the same
session (offsets are span-block starts with CONTEXT=80, not quote positions; no defect). It is
outside this seat's assignment (round-50 evidence, not round-73 calibration) and I did not verify
or act on it.
