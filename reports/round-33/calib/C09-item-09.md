- Seat: C09 | executor | claim C (calibration) | item 9 = OI-09 (lore-owned L0 contract-digest ratification) | date 2026-10-19 | baseline 139e3b6

# C09 — disposition of open item 9: the L0 contract-digest ratification

Write scope: this file only. No filed byte edited (`reports/round-1..32/**`,
`corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**` read-only). The
fleet L0 queue and the lore tree were **read** read-only (no writes) because
the item is operator/lore-routed by construction. Lane HEAD
`139e3b662900557afe54f632b468619593dc9fcb` = the declared baseline
(`git rev-parse HEAD`, this seat, 2026-10-19). NON-CANON engineering evidence;
no promotion, canon, clearance, ratification or closure verdict is made here.

## 1. Item binding (K03 canonical) — and a withdrawal

- **Binding:** `reports/round-33/calib/K03-open-items.md:75` — "Seat mapping for
  the C-lane: C01↔OI-01 … C12↔OI-12 in this order"; the row is
  `K03-open-items.md:70`: "**OI-09** | lore-owned — L0 contract-digest
  ratification (drift vs lore's open round-93 ratification) | r8/r15 (L0 row
  stamped round-8) | lore-owned-routing | `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:45`
  (kotodama | round-8, evidence `reports/round-8/adjacency.md`); contract
  `:7,:16,:155,:182`; `reports/round-15/handoff/contract-v2-audit.md:31`
  (contract digest `5f4c02bf…` unchanged)". K03's adopted expansion
  (`K03-open-items.md:33-43`): 3 design debts + 3 box-1 conditions + 1 cold-run
  cluster + 2 lore-owned + rubric + devin + adapter = 12.
- **Withdrawal (named, not hidden):** before K03 landed (`reports/round-33/calib/`
  was empty at my first listing, 2026-10-19T03:53Z; C08 records the same cut,
  `C08-item-08.md:26-27`) this seat derived item 9 from the only enumerated
  source then available — the D13 Decision 4 table's 9th row, "r18 D4-adapter
  baseline supersession semantics" (`reports/round-32/dossier-d13-operator-decisions.md:138`).
  That reconstruction is **withdrawn**: under K03's binding that content is
  **OI-12** (C12's item). No adapter-semantics byte is dispositioned by this
  seat. The measurements I took under the withdrawn reading are offered, not
  claimed, in §6.

## 2. Status quo at HEAD — re-verified 2026-10-19 at `139e3b6`

| check | command | result |
|---|---|---|
| L0 row text | `sed -n '45p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` | `kotodama \| round-8 \| worldbible-integration-contract digest drift vs lore's open round-93 ratification — who owns the contract digest update, and does lore's r93 ratification subsume it? Evidence: kotodama-shokunin/reports/round-8/adjacency.md` — **verbatim, unchanged** |
| queue shape | `wc -l` → `49`; `grep -c "^kotodama"` → `4` | kotodama rows at `:44` (round-2), `:45` (round-8), `:46` (round-9), `:47` (round-11) |
| answers surface | `ls /home/vgpnk/Projects/shokunin/.ufo/` | no answers file (`history-pin.json`, `interactive-l1-…`, `l0-questions.md`, `l0-recovery-…`, `lane-watch.sh`, `prompts/`, `reports/`, `round-10/`, `scopes/`, `state/`, `watchdog.log`, `waves/`) |
| live contract bytes | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |
| revision string | `grep -n "Contract ID" …` → `:11` | `kotodama-lore-adjacency`, initial interface revision `1.0.0` — **no revision bump** |
| contract history | `git log --oneline -3 -- corpus/knowledge/synthesis/worldbible-integration-contract.md` | `e1694ba` (round-8) is the last commit; then `291c714` (round 1); then `49ac1a5` (mint wave) |
| **digest chain, re-measured per commit** | `for c in 49ac1a5 291c714 e1694ba; do git show $c:corpus/knowledge/synthesis/worldbible-integration-contract.md \| sha256sum; done` | `49ac1a5` → `e834f50309bd93b1…` (= lore r89's pin); `291c714` → `50c4c2f25a728e69…` (= lore r93's pin); `e1694ba` → `5f4c02bfc4e6e4e9…` = **live HEAD digest** |
| contract clauses (K03's pointer) | `grep -n` on the contract | `:7` "recheck: on any contract revision or pinned-digest change — both lanes re-read and acknowledge before importing under it"; `:16` "Before later transfers, compare the pinned contract digest; a changed revision/digest requires both lanes to re-read and acknowledge"; `:155` "Lore pins exact delivered versions and digests, not version ranges. No auto-upgrade, including PATCH: even a corrected citation needs an auditable adopted revision."; `:182` acceptance-checklist "[ ] Both-lane read records agree on contract revision/digest" — all four pointers resolve to the claimed content |
| lore side, r93 rows | `sed -n '1,12p' /home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md` | `:6` (round-93) asks "ratify the 50c4… copy as the current rev-1.0.0 interface so lore can record its read/acknowledge, or direct kotodama to bump the revision and re-issue"; `:7` (round-93 timing correction) — "records that observation only, not a current sibling-HEAD claim, acknowledgement, or ratification; **the question remains open**". These are the last two lore L0 rows (rows present: r4, r81, r87, r88, r89, r93, r93) |
| lore's later rounds | `ls lore-shokunin/.ufo/waves \| tail -5` → `round-95 … round-99`; `grep -rl "5f4c02bf" lore-shokunin` → **no paths**; `grep -rl "kotodama-lore-adjacency" lore-shokunin/corpus` → **no hits** | six further lore rounds (94–99) since r93 produced no L0 answer, and lore holds **zero** references to the live digest anywhere in its tree |
| lane-side prior records | `reports/round-8/adjacency.md` | `:102`/`:113`/`:116` the in-round digest sequence (baseline `50c4c2f2…` 20:10Z → delivered `5f4c02bf…` 17:22:50); `:128` "worldbible-integration-contract.md 50c4c2f2… -> 5f4c02bf…"; `:134-137` the lore r93 ask; `:144-151` the two options (a) accept the sweep as a documented PATCH and answer against `5f4c02bf`, or (b) revert and re-issue with a revision bump per §9 |
| lane-side re-measurement | `reports/round-15/handoff/contract-v2-audit.md:31` | contract `5f4c02bf…` "unchanged from the §1 pin the round-11/12 audits measured"; `:71` "The round-8 L0 contract-digest question keeps its stale `50c4c2f2…` premise while the operational digest is `5f4c02bf…` — owner: integrator/lore, who should answer or retarget it to the current digest and record the both-lane read" |
| round-33 adjacency restatement | `reports/round-33/adj/A04-bleed.md:32,:76,:87`; `reports/round-33/adj/A06-contested.md:33 (CS-2),:70,:75,:151,:157` | already filed as routed-not-absorbed; §5 below does not duplicate it |

**Status-quo verdict:** the pointer is accurate and the item is open on the
operator/lore side at HEAD. One measured delta since round 8, and it sharpens
the item: the drift is now **two generations deep**. Lore's pending
ratification targets `50c4c2f2…` — the bytes at commit `291c714` — which the
round-8 metadata sweep itself superseded with `5f4c02bf…` (still declared
`1.0.0`). Ratifying the pending target as-is would ratify superseded bytes; no
lane-side artifact names the live digest *as the ratification target* (r15's
audit names it as a measurement only).

## 3. Disposition

**Class: `carried-with-owner+reason+next-touch`** — not `fixed-with-evidence`,
and not fixable-now from this lane.

- **owner:** the **operator** (the L0 queue is operator-side, and the row's own
  question is an ownership question: "who owns the contract digest update") +
  **lore-shokunin** (the ratifying party, whose r93 rows ask it); escalation
  surface `.ufo/l0-questions.md:45`.
- **reason:** (a) the act is lore's/operator's by the contract's own text —
  `:7`/`:16` require both lanes' read and acknowledgement on any pinned-digest
  change, `:155` forbids auto-upgrade ("even a corrected citation needs an
  auditable adopted revision"), `:182`'s checklist requires the read records to
  agree on revision/digest; (b) this lane reports contested scope and never
  absorbs it (`AGENTS.md`; r8 `adjacency.md:130` — "Escalation to the
  orchestrator (report, not absorbed)"); (c) the pending target digest
  `50c4c2f2…` is itself superseded at HEAD (`5f4c02bf…`), so the answer must be
  given against current bytes — only the operator/lore can give it, and this
  lane must not pre-empt it by answering its own L0 question; (d) lore has run
  six further rounds (94–99) without an L0 answer and holds zero references to
  the live digest (measured above).
- **next_touch:** (1) the operator answers L0 row 45 — r8's two options stand:
  (a) accept the sweep as a documented PATCH and answer against the live digest
  `5f4c02bf…` (revision still `1.0.0`), or (b) revert the sweep's contract edit
  and re-issue with a revision bump per §9; (2) lore then records its §1
  read/acknowledgement against the then-current digest; (3) re-check at the next
  adjacency audit (round-33 surface `adj/audit-assembled.md`; A04/A06 carry the
  restatement) and re-do both reads on any digest change (`:7`).

Ledger row for C15 (exact fields, ready to copy):

```json
{
  "id": "OI-09",
  "seat": "C09",
  "item": "lore-owned — L0 contract-digest ratification (worldbible-integration-contract digest drift vs lore's open round-93 ratification; who owns the digest update, and does r93 subsume it)",
  "origin": "r8/r15 (L0 row stamped round-8; lore r93 rows)",
  "pointer": "/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:45; corpus/knowledge/synthesis/worldbible-integration-contract.md:7,16,155,182; reports/round-8/adjacency.md:128,134-151; reports/round-15/handoff/contract-v2-audit.md:31,71; lore-shokunin/l0-questions.md:6-7",
  "status_quo_check": "2026-10-19 at HEAD 139e3b6: L0 row 45 unchanged and unanswered (49-line queue, no answers file in .ufo/); live contract digest 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069 at revision 1.0.0, last commit e1694ba; pending ratification target 50c4c2f2… = the 291c714 bytes, already superseded; lore r93 rows still the last lore L0 rows and lore holds 0 references to the live digest (grep -rl over lore-shokunin -> no paths)",
  "disposition_class": "carried-with-owner+reason+next-touch",
  "evidence": [
    "reports/round-33/calib/C09-item-09.md §2 (dated command table)",
    "corpus/knowledge/synthesis/worldbible-integration-contract.md:7,16,155,182 (digest 5f4c02bf…, measured 2026-10-19)",
    "reports/round-8/adjacency.md:102,113,116,128,134-151 (digest sequence; escalation options)",
    "reports/round-15/handoff/contract-v2-audit.md:31,71 (live digest re-measured; stale 50c4c2f2 premise named)",
    "/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:45 (read-only)",
    "lore-shokunin/l0-questions.md:6-7 (read-only)"
  ],
  "fix_draft": "reports/round-33/calib/C09-item-09.md §4 (L0 row 45 evidence refresh — operator-applied; the fleet queue is outside this lane's write scope, so C14 records it as operator-routed, not integrator-applied)",
  "owner": "operator (L0 queue / digest-update ownership) + lore-shokunin (ratifying party); escalation .ufo/l0-questions.md:45",
  "reason": "ratification is lore's/operator's act (contract :7,:16,:155,:182); this lane reports contested scope, never absorbs it (AGENTS.md; r8 adjacency.md:130); the pending target digest 50c4c2f2… is itself superseded (live 5f4c02bf…) so the answer must be given against current bytes; lore has not answered across rounds 94-99 and holds no reference to the live digest",
  "next_touch": "operator answers/retargets L0 row 45 (option (a) answer against 5f4c02bf or (b) revision bump per §9); lore records its §1 read against the then-current digest; re-check at the next adjacency audit and on any digest change"
}
```

## 4. Bounded draft — L0 row 45 evidence refresh (operator-applied)

Scope note: the fleet queue is **outside this repo and operator-owned** — a
never-edit surface for this round (`AGENTS.md`; targets.json `shared_rules`).
This draft therefore edits nothing itself: it is text for the operator, it
changes **no question text**, and it asserts no ratification. The item is
answerable without it (r8's `adjacency.md` already carries the analysis); the
refresh exists only to remove the stale-target hazard, so it is **optional**.

**Before** (control, measured this seat, 2026-10-19):

```sh
sed -n '45p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
# kotodama | round-8 | worldbible-integration-contract digest drift vs lore's
# open round-93 ratification — who owns the contract digest update, and does
# lore's r93 ratification subsume it? Evidence: kotodama-shokunin/reports/round-8/adjacency.md
```

**After — draft row text** (same question, evidence pointer extended):

```text
kotodama | round-8 | worldbible-integration-contract digest drift vs lore's open round-93 ratification — who owns the contract digest update, and does lore's r93 ratification subsume it? Evidence: kotodama-shokunin/reports/round-8/adjacency.md; round-33 re-measurement (2026-10-19, kotodama HEAD 139e3b6): the pending ratification target 50c4c2f2… (bytes at commit 291c714) is itself superseded — the live digest is 5f4c02bf… (bytes at commit e1694ba; revision still 1.0.0). Evidence: kotodama-shokunin/reports/round-33/calib/C09-item-09.md
```

**Verification after the operator applies it:**

```sh
sed -n '45p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md | grep -c "5f4c02bf"        # 1
grep -c "^kotodama" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md                     # 4 (no row added or dropped)
```

**Controls (must stay red/unchanged):**

```sh
grep -c "who owns the contract digest update" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md   # 1 (row still a question; measured 2026-10-19)
grep -c "Initial bilateral acknowledgement is \*\*pending\*\*" corpus/knowledge/synthesis/worldbible-integration-contract.md  # 1 (measured 2026-10-19)
grep -rnE "ratified by both lanes|ratification recorded|acknowledgement is complete|is now ratified" reports/round-33/calib/C09-item-09.md | grep -v "grep -rnE"   # 0 lines, exit 1 (measured 2026-10-19); the second grep drops the control's own line, which necessarily contains the pattern text
```

## 5. Boundaries (what this fragment is not)

- **Not OI-08** (C08's bilateral §1 read record): the read record and the
  digest ratification are distinct rows (`K03-open-items.md:69` vs `:70`).
  This seat classes neither the read record nor lore's read as its own; the
  OI-08/OI-09 boundary C08 asks for (`C08-item-08.md:176-181`) is answered from
  this side: OI-08 = *who read which revision, recorded where*; OI-09 = *which
  digest is the interface being ratified*.
- **Not the A-lane restatement:** `adj/A04-bleed.md:32,:76,:87` and
  `adj/A06-contested.md:33 (CS-2)` already file the routed-not-absorbed
  posture. This fragment adds the disposition, the ledger row and the
  two-generation drift measurement; it asserts no canon, ratification or
  clearance anywhere.
- **Read-only externals:** the fleet L0 queue and the lore tree were read, not
  written; no credential or prompt payload was copied.

## 6. Not-my-item note — measurements offered to C12/OI-12 (not claimed here)

Taken before K03 landed, under the withdrawn reading; offered so C12 can
cross-check rather than re-run (no claim made by this seat):

```sh
python3 -B tools/check-gate-battery.py                       # exit 0; coverage 10/10, pinned 20/20
TMPDIR=/var/tmp/kotodama-c09 python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv
  # exit 1: ROW 2 + ROW 3 mismatch, exit 1/0, bytes differ (the filed control)
TMPDIR=/var/tmp/kotodama-c09 python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv
  # exit 0: REPLAY OK: 4/4 rows reproduced
sha256sum examples/culture-d4/packet.d4.yml tools/gates/frozen/round-18/inputs/examples/culture-d4/packet.d4.yml
  # aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3 (live) vs e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3 (r18 snapshot)
sha256sum tools/gates/d4-assembly-check-gate.py tools/gates/d4-typed-labels-check-gate.py
  # df1a364b… / 05f99629… — both still match their r18 pins, so the aging is peer-read drift, not gate drift
```

The `TMPDIR=/var/tmp/kotodama-c09` scratch mirror is the lane's documented
mirror-safety practice (`reports/round-31/final-sweep.md:176-181`); it is
removed after the run, and nothing is written inside the repo.

## Owed

- `reports/round-33/calib/C15-ledger-draft.json` — take the §3 row verbatim;
  OI-09 is dispositioned by this seat only.
- `reports/round-33/calib/C13-consistency.md` — confirm no double disposition of
  OI-09 (C08's boundary note asks the same from its side) and that
  `calib/C12-item-12.md` carries OI-12, not OI-09.
- `reports/round-33/calib/C14-fix-drafts.md` — record the §4 draft as
  **operator-routed** (fleet queue is outside this lane's write scope), not as
  an integrator-applied in-repo edit.
- Operator-side, not owed to this round's integrator: answer or retarget L0
  row 45 (`.ufo/l0-questions.md:45`).

## Citations

Paths (all read 2026-10-19, HEAD `139e3b662900557afe54f632b468619593dc9fcb`):

- `reports/round-33/calib/K03-open-items.md:33-43,69,70,75` (binding + count convention)
- `reports/round-33/calib/C08-item-08.md:26-27,176-181` (cut time; OI-08/OI-09 boundary)
- `reports/round-33/claims.json:42-50`; `reports/round-33/targets.json` (seat C09)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:7,11,16,56,150,155,182` (digest `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`)
- `reports/round-8/adjacency.md:22,102,108-128,130-151,293` (digest sequence; escalation options; "report, not absorbed")
- `reports/round-15/handoff/contract-v2-audit.md:31,71` (live digest re-measured; stale `50c4c2f2` premise named)
- `reports/round-32/dossier-d13-operator-decisions.md:135,138` (item on record; the withdrawn row-9 reading)
- `reports/round-33/adj/A04-bleed.md:32,76,87`; `reports/round-33/adj/A06-contested.md:33,70,75,151,157` (routed-not-absorbed restatement)
- `reports/round-31/final-sweep.md:176-181` (§4 TMPDIR boundary), `:185-190` (§5, the withdrawn reading's source)
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45,46,47` (read-only; 49 lines, 4 kotodama rows)
- `/home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md:6-7` (read-only; r93 rows)

Commands (this seat, 2026-10-19, in-repo unless the path is external):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                                  # 139e3b662900557afe54f632b468619593dc9fcb
sed -n '45p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
wc -l /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md          # 49
grep -c "^kotodama" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md   # 4
ls /home/vgpnk/Projects/shokunin/.ufo/                            # no answers file
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md
git log --oneline -3 -- corpus/knowledge/synthesis/worldbible-integration-contract.md
for c in 49ac1a5 291c714 e1694ba; do git show $c:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum; done
grep -n "recheck: on any contract revision\|Before later transfers\|Lore pins exact delivered\|Both-lane read records agree" corpus/knowledge/synthesis/worldbible-integration-contract.md
sed -n '1,12p' /home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md
ls /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves | tail -5     # round-95 … round-99
grep -rl "5f4c02bf" /home/vgpnk/Projects/shokunin/lore-shokunin          # no paths
grep -rl "kotodama-lore-adjacency" /home/vgpnk/Projects/shokunin/lore-shokunin/corpus   # no hits
grep -n "5f4c02bf\|50c4c2f2" reports/round-8/adjacency.md reports/round-15/handoff/contract-v2-audit.md
python3 -B tools/check-gate-battery.py                                    # §6, exit 0, pinned 20/20
TMPDIR=/var/tmp/kotodama-c09 python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv            # §6, exit 1, 2 mismatch
TMPDIR=/var/tmp/kotodama-c09 python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv # §6, exit 0, 4/4
```
