- Seat: C08 | executor | claim C (calibration) | item 8 = OI-08 (lore-owned bilateral same-revision read) | date 2026-10-19 | baseline 139e3b6

# C08 — disposition of open item 8: the bilateral same-revision read record

Write scope: this file only. No filed byte edited (`reports/round-1..32/**`,
`corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**` read-only).
Observation window 2026-10-19T03:49–03:58Z; lane HEAD
`139e3b662900557afe54f632b468619593dc9fcb` = the declared baseline
(`git rev-parse HEAD`, run this seat). NON-CANON engineering evidence; no
promotion, canon, clearance or closure verdict is made here. The L0 queue and
the lore tree were **read** (read-only, no writes) because the item is
bilateral by construction.

## 1. Item binding (K03 canonical) — and a withdrawal

- **Binding:** `reports/round-33/calib/K03-open-items.md:75` — "Seat mapping for
  the C-lane: C01↔OI-01 … C12↔OI-12 in this order"; the row is
  `K03-open-items.md:69`: "**OI-08** | lore-owned — bilateral same-revision read
  record still outstanding | r8/r15 (L0 row stamped round-2) |
  lore-owned-routing | `corpus/knowledge/synthesis/worldbible-integration-contract.md:15`
  … `reports/round-15/handoff/contract-v2-audit.md:31,48` … L0 queue
  `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44` (kotodama | round-2)".
  K03's adopted expansion (`K03-open-items.md:33-40`) keeps the cold-run cluster
  whole: 3 design debts + 3 box-1 conditions + 1 cold-run cluster + 2 lore-owned
  + rubric + devin + adapter = 12.
- **Withdrawal (named, not hidden):** before K03 landed (`reports/round-33/calib/`
  was empty at 2026-10-19T03:53Z, `ls`), this seat reconstructed item 8 as
  cold-run N7 under a 4-way cold-run split. That reconstruction is **withdrawn**;
  under K03's binding the cold-run cluster is OI-07 (C07's item) and item 8 is
  OI-08. No cold-run byte is dispositioned by this seat.
- **Cross-seat finding for C13 (not absorbed here):** `calib/C07-item-07.md:28-35`
  dispositions the *rubric* item as "item 7" (primary), with cold-run N4 as
  contingency A (`C07-item-07.md:100-125`); `calib/C16-receipt.md:56-57,68` used
  the 9+2+1 decomposition (its C-08 row = cold-run N4/N5/N7). Under K03's
  binding item 7 = OI-07 and item 8 = OI-08, so C07's primary is OI-10's content
  and C10's item may be dispositioned twice. C13 must re-bind or record the
  duplicate; this seat does not adjudicate it.

## 2. Status quo at HEAD — re-verified 2026-10-19 at `139e3b6`

The contract's own gate (read this date):

| check | command | result |
|---|---|---|
| §1 requirement text | `grep -n "bilateral\|same-revision\|pending" corpus/knowledge/synthesis/worldbible-integration-contract.md` | `:14` the record must carry `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer`; `:15` "Initial bilateral acknowledgement is **pending** until those records exist; writing this file is not a substitute for lore's read."; `:127` both lanes must satisfy "§1's same-revision read gate"; `:150` "bilateral acknowledgement is still required" |
| contract identity | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (revision `1.0.0`, `:11`) — the digest a read record must name today |
| contract history | `git log --oneline -2 -- corpus/knowledge/synthesis/worldbible-integration-contract.md` | `e1694ba` (round-8), `291c714` (round 1) — no later commit; the revision has not moved |
| kotodama-side record | `grep -rn "read_at" reports/ corpus/ --include=*.md` (this seat) | **no record exists**; hits are requirement/absence prose only: `reports/round-11/handoff/contract-check.md:114`, `reports/round-15/handoff/contract-v2-audit.md:72`, `reports/round-26/open-questions/C41.md:111`, `reports/supplement-opencode-1/25-handoff-boundary.md:38` |
| kotodama-side owner naming | `reports/round-15/handoff/contract-v2-audit.md:72` | "No kotodama-side §1 read record … exists in this repo — owner: kotodama orchestrator"; `reports/round-26/open-questions/C41.md:107-109` re-checked it as **carried**, owner `operator`, "next touch round 27" |
| lane lesson record | `corpus/lessons/round-2-adjacency.md:76-78` | "§1 read gate: no kotodama-side read record … exists in this repo; the packet itself records `bilateral_read: \"pending\"`" (also `:29-30`: the digest below is what such a record must name) |
| census restatement | `reports/round-25/lessons/census.json:113` | same absence, quoted as the §1 read gate |
| lore-side record | `lore-shokunin/l0-questions.md:5` (lore round-89) and `:6` (lore round-93) | "lore holds no acknowledgement record (grep -rn \"kotodama-lore-adjacency\" in lore -> 0 files)"; r93: "lore still holds no acknowledgement record (… tracked corpus 0 hits)" — and lore's own §1 read/record action is named there as "a lane-side write, not an operator gate" |
| lore-side field search | `lore-shokunin/.ufo/waves/round-89/followup/JCOV4.md:133` (lore's own measurement) | "A content search for `kotodama-lore-adjacency\|file_sha256\|read_at\|evidence_pointer` in `lore-shokunin/corpus` returned no matches"; `:218-222` "lore's read/ack is still open" |
| L0 queue row | `sed -n '44p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` | the kotodama round-2 row asks lore, question (b), whether "lore require[s] a §1 same-revision read record … filed by each lane before a real packet is sent" — unanswered; `ls /home/vgpnk/Projects/shokunin/.ufo/` shows no answers file |
| rounds 27-32 | `grep -rc "bilateral" reports/round-2[7-9]/*.md reports/round-3[0-2]/*.md` | restatements only, no record created: `reports/round-29/adjacency/province-entries.md:17`, `reports/round-30/adjacency.md:12`, `reports/round-32/dossier-d13-operator-decisions.md:135` |

Packets keep stating it pending through r26 (`reports/round-20/handoff/packet-v3-16.md:311`
OQ-V3-01; `reports/round-23/wording/declared-in-r3/packet.md:16`;
`reports/round-26/remainders/v3-baseline-r26/packet.md:14`).

**Status-quo verdict:** the pointer is accurate — the item is open on **both**
sides at HEAD, 31 rounds after it was stamped. One delta worth recording:
lore's round-93 row pins the contract as `50c4c2f2…` (the `291c714` state) while
the live digest is `5f4c02bf…`; that digest-ownership question is **OI-09**
(C09's item, `K03-open-items.md:70`), not dispositioned here — but the read
record drafted below must pin today's measured digest, and a future digest
change re-opens the read per contract `:7`/`:16`.

## 3. Disposition

**Class: `carried-with-owner+reason+next-touch`** — with the lane-side half
fixable by a bounded draft (§4). It cannot be `fixed-with-evidence` from this
lane: the gate is bilateral by the contract's own text (`:14-15`), and this
lane's rule is to report contested scope, not absorb it (`AGENTS.md`).

- **owner:** kotodama orchestrator/integrator for the lane-side record
  (`contract-v2-audit.md:72` naming; r26's `C41.md:107` named `operator` — both
  namings on record, unreconciled here) + **lore-shokunin** for the counterparty
  record (lore's own rows, `lore-shokunin/l0-questions.md:5-6`). Escalation
  surface: L0 row `.ufo/l0-questions.md:44`.
- **reason:** (a) no read record exists on either side at HEAD (measured
  above); (b) lore's half is not producible from this lane — it is lore's
  lane-side write, and lore has said so itself; (c) the record must name the
  current revision/digest and is invalidated by a digest change (`:7`, `:16`),
  so it cannot be back-dated or inferred.
- **next_touch:** (1) integrator lands the kotodama-side §1 record draft (§4);
  (2) re-check L0 row 44 + `lore-shokunin/l0-questions.md:5-6` at the next
  adjacency audit (claim A's `adj/audit-assembled.md` is the round-33 surface);
  (3) both reads re-done if revision/digest changes. The r26 "next touch round
  27" was never taken — rounds 27-32 carry restatements only (table above).

Ledger row for C15 (exact fields, ready to copy):

```json
{
  "id": "OI-08",
  "seat": "C08",
  "item": "lore-owned — bilateral same-revision read record still outstanding (§1 read gate; both lanes' records missing)",
  "origin": "r8/r15 (L0 row stamped round-2; contract §1 since r1)",
  "pointer": "corpus/knowledge/synthesis/worldbible-integration-contract.md:14-15; reports/round-15/handoff/contract-v2-audit.md:72; corpus/lessons/round-2-adjacency.md:76-78; /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44; lore-shokunin/l0-questions.md:5-6",
  "status_quo_check": "2026-10-19 at HEAD 139e3b6: contract still reads pending (:15); no kotodama-side record (grep -rn 'read_at' reports/ corpus/ --include=*.md -> requirement prose only); no lore-side record (lore l0-questions.md:5-6; JCOV4.md:133); L0 row 44 unanswered",
  "disposition_class": "carried-with-owner+reason+next-touch",
  "evidence": [
    "reports/round-33/calib/C08-item-08.md §2 (dated command table)",
    "corpus/knowledge/synthesis/worldbible-integration-contract.md:14-15,127,150 (sha256 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069, measured 2026-10-19)",
    "reports/round-15/handoff/contract-v2-audit.md:72",
    "reports/round-26/open-questions/C41.md:107-115",
    "lore-shokunin/l0-questions.md:5-6",
    "lore-shokunin/.ufo/waves/round-89/followup/JCOV4.md:133,218-222"
  ],
  "fix_draft": "reports/round-33/calib/C08-item-08.md §4 (kotodama-side §1 read record; integrator-applied; hoist to calib/C14-fix-drafts.md)",
  "owner": "kotodama orchestrator/integrator (lane-side record) + lore-shokunin (counterparty record); L0 escalation .ufo/l0-questions.md:44",
  "reason": "bilateral gate (contract :14-15): lore's read record is not producible from this lane; no record exists on either side at HEAD; the record must name the current revision/digest and a digest change re-opens it (:7,:16)",
  "next_touch": "integrator lands the §4 draft; re-check L0 row 44 + lore l0-questions.md:5-6 at the next adjacency audit; re-do both reads on any revision/digest change"
}
```

## 4. Bounded fix draft — the kotodama-side §1 read record (integrator-applied)

Scope note: this draft **adds one lane-owned record**; it edits no contract byte
(contract `:14` requires each lane to record "in their own permitted records",
`:13` forbids an independently edited mirror), no filed round byte, and no
shared file. It closes only the lane-side half — the item stays carried until
lore files its own record (contract `:15`).

**Before** (this seat's control, 2026-10-19):

```sh
grep -rn "read_at" reports/ corpus/ --include=*.md   # requirement/absence prose only, no record
test -s reports/round-33/adj/contract-read-record.md; echo $?   # 1 (absent)
```

**After — draft content** (fields exactly as contract `:14` names them; the two
`<…>` slots are the integrator's to fill, not this seat's to assert):

```text
# §1 same-revision read record — kotodama-shokunin
lane: kotodama-shokunin
contract_id: kotodama-lore-adjacency
revision: 1.0.0
file_sha256: 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069
reader: <integrator seat identity>
read_at: <landing date, UTC>
evidence_pointer: reports/round-33/calib/C08-item-08.md (digest re-measured 2026-10-19 at HEAD 139e3b6)
scope: §1 gate only; this record does not represent lore's read, acceptance, receipt, or canon standing.
```

**Surface (integrator-owned choice, flagged `to-verify`):** the round-scoped
path `reports/round-33/adj/contract-read-record.md` is the cheapest landing, but
the contract's wording asks for a *record*, and whether a round-scoped report
satisfies that (versus a durable lane surface) is the integrator's/operator's
call. Either way the record must be durable and lane-owned, and must not touch
the contract file.

**Verification after landing:**

```sh
test -s reports/round-33/adj/contract-read-record.md
grep -c "file_sha256: 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069" reports/round-33/adj/contract-read-record.md   # 1
grep -c "lane: kotodama-shokunin" reports/round-33/adj/contract-read-record.md   # 1
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md   # must still be 5f4c02bf… (the record's pin must match live bytes)
```

**Control (must stay red):** the item is not closed by this draft —
`grep -c "acknowledgement is \*\*pending\*\*" corpus/knowledge/synthesis/worldbible-integration-contract.md`
must still return 1 until lore files its own record and both lanes re-acknowledge
(contract `:15`).

## Owed

- `reports/round-33/calib/C14-fix-drafts.md` — hoist §4 above (kotodama-side §1
  read record). OI-07's N1 errata draft is C07's, not mine.
- `reports/round-33/calib/C15-ledger-draft.json` — take the §3 row verbatim;
  OI-08 is dispositioned by this seat only.
- `reports/round-33/calib/C13-consistency.md` — re-bind finding in §1 (C07's
  primary binding vs K03's table; possible double disposition of OI-10) and the
  OI-08/OI-09 boundary: C09's item (contract-digest ratification,
  `K03-open-items.md:70`) was **not landed at this seat's cut**
  (`ls reports/round-33/calib/`, 2026-10-19T03:56Z: no `C09-item-09.md`), so the
  OI-08/OI-09 boundary is checked from my side only; C13 must confirm C09 does
  not class the read record as its own.

## Citations

Paths (all read 2026-10-19, HEAD `139e3b662900557afe54f632b468619593dc9fcb`):

- `reports/round-33/calib/K03-open-items.md:33-40,69,70,75`
- `reports/round-33/calib/C07-item-07.md:28-35,100-125`;
  `reports/round-33/calib/C16-receipt.md:56-57,68`
- `reports/round-33/claims.json:42-50`; `reports/round-33/targets.json` (seat C08)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:7,11,13,14,15,127,150`
  (sha256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`)
- `corpus/lessons/round-2-adjacency.md:29-30,76-78`
- `reports/round-11/handoff/contract-check.md:110-115`
- `reports/round-15/handoff/contract-v2-audit.md:31,48,72`
- `reports/round-20/handoff/packet-v3-16.md:13,305,311`
- `reports/round-21/adjacency/A11-A12-handoff.md:10,50`
- `reports/round-23/wording/declared-in-r3/packet.md:16,302`
- `reports/round-25/lessons/census.json:113`
- `reports/round-26/open-questions/C41.md:107-115`;
  `reports/round-26/remainders/v3-baseline-r26/packet.md:14`
- `reports/round-29/adjacency/province-entries.md:17`; `reports/round-30/adjacency.md:12`
- `reports/round-32/dossier-d11-shonen-boxes.md:150-153,167,207`;
  `reports/round-32/dossier-d13-operator-decisions.md:130-138`;
  `reports/round-32/scribe/fragment-ledger.md:212-218`
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44` (read-only)
- `/home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md:5-6` (read-only)
- `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-89/followup/JCOV4.md:133,218-222`
  (read-only)

Commands (this seat, 2026-10-19, all in-repo unless the path is external):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                       # 139e3b662900557afe54f632b468619593dc9fcb
git log --oneline -2 -- corpus/knowledge/synthesis/worldbible-integration-contract.md
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md
grep -n "bilateral\|same-revision\|pending" corpus/knowledge/synthesis/worldbible-integration-contract.md
grep -rn "read_at" reports/ corpus/ --include=*.md
grep -rn "bilateral" reports/round-1[6-9]/ reports/round-2[0-9]/ reports/round-3[0-2]/ corpus/
grep -rc "bilateral" reports/round-2[7-9]/*.md reports/round-3[0-2]/*.md
ls reports/round-33/calib/               # no C09-item-09.md at 03:56Z
sed -n '44p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
ls /home/vgpnk/Projects/shokunin/.ufo/   # no answers file
grep -n "kotodama-lore-adjacency" /home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md
grep -rl "kotodama-lore-adjacency" /home/vgpnk/Projects/shokunin/lore-shokunin | head   # l0-questions.md + .ufo wave artifacts
grep -rl "5f4c02bf" /home/vgpnk/Projects/shokunin/lore-shokunin | head                   # no paths printed
```
