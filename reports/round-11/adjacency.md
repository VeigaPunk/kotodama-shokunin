# R11-X02 — adjacency / connector: git-scope, PROVINCE accuracy, lore-boundary

- seat: **R11-X02** (scribe, adjacency/connector + out-of-lane watch), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17.
- assignment (verbatim): "SCRIBE X02: adjacency/connector — git-scope check (fleet root must stay clean), PROVINCE accuracy, lore-boundary; reports/round-11/adjacency.md."
- writes: **this file only** (plus in-lane scratch under `.scratch/x02/`, gitignored). This seat edits no earlier-round byte, makes no commit, no push.
- revision binding: lane HEAD `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (= `e3ef171`, round-11 declaration, 2026-10-17 21:58:56Z / 18:58:56−03:00), **unmoved at every check**; fleet root HEAD `b0bb880`.
- clock: all stamps UTC; local time is UTC−03:00.
- canon: NON-CANON engineering record. Nothing here admits a round, a capability or a canon fact.
- status: **live in-flight audit** — every list and count is a stamped snapshot; the file was re-checked immediately before writing (§6).

## 0. Verdict summary

1. **Fleet root clean** at every check (§1.1). No sibling-repo write observed from this lane (§3.4).
2. **Lane HEAD unmoved**; no worker commit or push (evidence in §1.2).
3. **FINDING A (scope incident, partially self-corrected): six filed receipts of rounds 5–9 were rewritten in the live worktree by in-flight recheck runs** — mechanism proven to code + 3 ms-level timestamps; the receipts read `stable: true` on their measured channel while the filed bytes changed (§1.3). One path (`round-6/checkpoint-validation.json`) was restored at 22:10:24Z; **five receipt paths remain dirty at the latest check (22:12:54Z)** and must not be committed as-is.
4. **FINDING B (open scope incident): the filed round-10 fragment `coverage/index-update-22.md` was appended after filing** (+67/−1; §1.4).
5. **FINDING C: PROVINCE mapping holds** — D/O/F work stays inside the declared province; no ownership absorption observed in landed fragments (§2).
6. **FINDING D: lore boundary clean so far** — the new O packet carries correct `not canonized` / unbound-drill discipline; the exercise now passes 16/16, 20/20 from a seat run; the round-8 contract-digest L0 item remains open (§3).

---

## 1. Git-scope

### 1.1 Fleet root — clean

```sh
cd /home/vgpnk/Projects/shokunin && git status --porcelain | wc -l   # → 0
```

Run at 2026-10-17 22:02Z, 22:04Z, 22:07Z, 22:10Z (all 0; HEAD `b0bb880`). The fleet-side surfaces touched in the window (`.ufo/reports/round-10/kotodama.md`, `.ufo/l0-questions.md`) are the integrator's own protocol surfaces and are committed (porcelain 0).

### 1.2 Lane tree — HEAD unmoved; in-scope writes

- `git log --oneline -1` at every check → `e3ef171` (declaration). No commit/push by any worker.
- In-scope round-11 artifacts landed during the wave (new/untracked; landing continued past the first census): `reports/round-11/depth/` (scribe, design, design-review, frozen-records, capability-draft, shard-assembler, shard-gate-adapter, shard-holds, test-cli/boundary/determinism/interop-d3, neg-17/18, review-21/22/23); `reports/round-11/handoff/` (design, shard-glossary, shard-cli, packet-attempt-1..4 (+`.yml`), review-16/17, tamper-control.sh/log); `reports/round-11/report-draft.md`; `reports/round-11/recheck/row-000..191.json` (**192 receipts, rows 0–191 complete at 22:12:54Z**); `reports/round-11/run-validation.py`, `reports/round-11/validation.json`; `tools/exercise-handoff-e2e.py`; `tools/typed-gate-flow.py`; `tools/gates/expected/handoff-exercise/r11/`. `.scratch/**` is the designated scratch surface.
- Untracked/`??` status of these paths is expected mid-wave (no commit until integration).
- **Landing continued past the last census — one tracked in-scope change:** at 22:14:05Z `examples/culture-d2/typed-labels.d2.yml` also shows as modified (1 line: `assembly.packet_sha256` `8da90b07…` → `e0f21509…`). This is the round-10 A2 drift being fixed by the D wiring's declared re-emission ("frozen replay re-pinned", claim D) — **in scope, to be committed at close**, unlike Finding A's clobbers. Watch item for D20–D23: the re-emission is a rewrite of a round-8-generated artifact; the reviewers should confirm it is the declared re-pin (`tools/d2-typed-labels.py --check` should now pass) and that the frozen manifest names the new digest rather than inheriting it silently.

### 1.3 FINDING A — six filed receipts rewritten in the live tree (open)

`git diff --stat` at 22:04:38Z (7 files, **+127/−881**). Per-file evidence (snapshot 22:04:38Z; hash columns from `git show HEAD:<path> | sha256sum` vs `sha256sum <path>`):

| filed path | live mtime (−03) | HEAD blob sha256 | live sha256 | ledger rows whose 1:1 re-run writes it |
|---|---|---|---|---|
| `reports/round-5/validation.json` | 19:03:00 | `78444f4cca74…` | `73a66f7464ea…` | 102, 120, 170 |
| `reports/round-6/checkpoint-validation.json` | 19:01:53.492 | `665dc2a0d7ef…` | `7c6333e77d28…` | 147 |
| `reports/round-6/validation.json` | 19:03:04 | `00a1d48bcc2a…` | `32c621efaccc…` | 129, 171 |
| `reports/round-7/validation.json` | 19:03:07 | `6dede8f9624a…` | `2f4c1e159b60…` | 130, 172 |
| `reports/round-8/validation.json` | 19:03:13 | `359932a7debf…` | `b008ec57f2b1…` | 113, 131, 173 |
| `reports/round-9/validation.json` | 19:03:17 | `036f84278c48…` | `cba4d935a259…` | 114, 132 |

**Mechanism (code-level, not inferred).** Every one of these ledger rows is a command whose process writes its own report path: `reports/round-5/run-validation.py:194`, `round-6/run-validation.py:336`, `round-6/check-checkpoint.py:117`, `round-7/run-validation.py:1171`, `round-8/run-validation.py:99` (`OUTPUT_REL`), `round-9/run-validation.py:127` (`OUTPUT_REL`) each do `(HERE|ROOT / OUTPUT_REL).write_text(…)`. A "1:1 re-run" of those rows in the live tree therefore regenerates a **filed** document as a side effect, while the ledger's measured channel records the command's emitted content (stdout / report bytes) — so a receipt can read `stable` while the filed bytes change.

**Execution evidence, strongest first:**

1. **F07 (rows 144–167), row 147 — 3 ms proof.** `.scratch/f07/run-rechecks.py` sets `REPO = "<lane root>"`, `ROWS = list(range(144, 168))`, and runs each row with `cwd=REPO` via `bash -c`. Its capture `.scratch/f07/out/row-147.out` has mtime **19:01:53.495**; the rewritten `reports/round-6/checkpoint-validation.json` has mtime **19:01:53.492** — the same invocation. Its filed receipt `reports/round-11/recheck/row-147.json` reads `prior_hash == new_hash == 7c6333e77d28…` and `stable: true` — while the committed blob was `665dc2a0d7ef…`. This single row demonstrates the whole finding: *the recheck is true about its measured channel and false about the filed tree.*
2. **F06 (rows 120–143) — declared live protocol.** Its receipts state `recheck_context.recheck_root = "live lane worktree /home/vgpnk/Projects/shokunin/kotodama-shokunin (1:1 protocol); drift attribution used isolated clones .scratch/f06/iso (e3a1ec9, 94ca098) and .scratch/f06/iso2"`. The five rewritten receipt files' mtimes (19:03:00 → 19:03:17, ~3–4 s apart) match F06's ascending slice order 120 → 129 → 130 → 131 → 132 (round-5 → 9). Its two passes (`results-a.json` 19:02, `results-b.json` 19:03) differ only for the path-dependent row 120 stdout (`3f6cd9d7…` vs `84658644…`, both 16 747 bytes), consistent with one mirrored and one live pass.
3. **F04's own receipts** (rows 72–95) record the concurrency from a third angle: `live_worktree_at_snapshot: "…concurrent round-11 seats edited reports/round-5..9/validation.json and wrote reports/round-11/depth/* while this seat ran"` (`reports/round-11/recheck/row-092.json` context).
4. **F05 (rows 96–119) demonstrates the safe pattern**: row 102 "run 1:1 from a full-tree mirror at round-10's own scratch path `.scratch/f11/mirror`", rows 113/114 "via importlib with module `OUTPUT_REL` redirected to `.scratch/r11f05/` (round-10 shard-13's protocol for this row)". Its receipts show no live-write side effects.

**Attribution and nature.** F06 and F07 executed their rows in the live root; the F assignment's "re-run each command 1:1" reads naturally as "at the recorded location", and the non-idempotence of these particular commands is a ledger-schema hazard (rows whose command writes a tracked path), not worker misconduct.

**Status update (22:12:54Z).** (a) `reports/round-6/checkpoint-validation.json` was **restored** at 22:10:24Z: live sha256 `665dc2a0d7ef…` now equals the committed blob and the path left the dirty list — a restore, not a re-run (a re-run would still emit the failure JSON, since the `mesopotamia-sumer-akkad.md` entry change stands). Restoring seat unattributed. (b) F08's receipts for rows 168–191 landed (row 170 `stable: false` / environmental; 171–173 `stable: true`), completing 192/192 rows; no filed mtime moved during its runs, and its scratch shows clone/iso runners (`rerun-clone.py`) — F08 did **not** repeat the live-write pattern. (c) The other **five** receipt paths remain dirty at 22:12:54Z (same sha256 deltas as the table; `git diff --stat`: 6 files, +125/−859).

**Consequence if closed as-is.** The round-11 close commit would rewrite filed receipts of rounds 5–9 — the same class round-10 recorded ("a stale-fixer rewrote filed receipt bytes … reverted by the integrator; staleness documented in the ledger instead") and the hard rule for this wave forbids ("corrections are new files, never edits to filed bytes").

**Recommendation (for the integrator).** Restore all six paths from the committed blobs before close (`git checkout -- reports/round-5/validation.json reports/round-6/checkpoint-validation.json reports/round-6/validation.json reports/round-7/validation.json reports/round-8/validation.json reports/round-9/validation.json`); none of the working-tree deltas is an intended correction, and the recheck evidence does not depend on them (receipts carry their own captures). Keep the F receipts as filed — their drift/stable verdicts remain valid readings of the commands' output channels — but have F12's summary (and any close note) record this side-effect class and the row list (102, 113, 114, 120, 129, 130, 131, 132, 147, 170–173) so "hash-stable" is never read as "tree unchanged". If any live re-run output has independent value (e.g. row 131/132's current green readings), file it as a **new** round-11 file, not as edits to filed bytes.

### 1.4 FINDING B — filed round-10 fragment appended after filing (open)

`reports/round-10/coverage/index-update-22.md` — committed in `94ca098` (round-10 admit, 21:57:36Z); the worktree now carries **+67/−1** (`git diff` hash `021c3ad0…` at 22:02Z; an earlier state at 22:01Z read +62, diff hash `62722577…`; live sha256 `2c33853f…` vs HEAD blob `1b30ea92…`; mtimes 19:00:36 and 19:01:18 −03).

Content of the delta: (a) a "Scratch prune (recorded after filing)" note explaining that `.scratch/` was emptied wholesale at 21:59:52Z and that §9 re-states the verdict-bearing checks; (b) a "Precision on severity" paragraph on the authorship-bucket count; (c) a new §9 appendix inlining a compact re-runnable sweep. The appendix names `.scratch/r10-c22-sweep-core.py` sha256 `4f0f7224eae79db34d50c517602ee22f63246a634db4a9c502162a6aa005b2dc` — a file this seat found on disk (mtime 19:00, sha256 matches exactly), so the writer was active in-lane at 19:00–19:01.

Attribution is **unresolved** from available evidence: the content style is a round-10 C22 seat documenting a prune of its own scratch, but the timing (after the round-11 declaration, alongside the wave) also admits an early round-11 process reacting to the missing scratch instrument. Either way the bytes are **post-filing edits to a filed artifact**.

Recommendation: restore the committed bytes; if the §9 re-statement has value, re-file it as a new round-11 file (e.g. under `reports/round-11/`), per "corrections are new files". Note: X04's draft already flagged a Hazard-1 view of this same file at 22:0XZ (`reports/round-11/report-draft.md`) — this section is the fuller record.

---

## 2. PROVINCE accuracy

Quoted from `PROVINCE.md` (lines 9–31): the lane owns "conlang design and diachronic staging; mythic and symbolic systems; era/period models; costume & material-culture terminology; naming systems — for fictional worlds, feeding the world bible"; it refuses "claiming or recording canon …; real-world rights/attribution rulings …; game mechanics …; general source-research method (chousa); web publishing (kake); prompt/skill craft (kotoba)"; the adjacent contract with lore is "load-bearing" and defined in `corpus/knowledge/synthesis/worldbible-integration-contract.md`; "Contested scope → report to the integrator, never absorb"; the lane writes only its own repository.

Mapping of round-11 claims (`reports/round-11/claims.json`):

- **D (typed pipeline, `d2-typed-pipeline`)** — typed-label projection wiring and gates over the lane's non-canon culture drills: conlang design + the lane's own gates. In province.
- **O (handoff-e2e exercise)** — a lane-local exercise of the lane's own handoff format; the canonical contract copy lives in this lane. In province (this is the adjacent *interface*, not lore's canon work).
- **F (ledger recheck)** — rechecking the lane's own recorded claims. In province.

Landed fragments state their non-canon standing explicitly (`reports/round-11/depth/review-22.md`: "canon: NON-CANON engineering review. Nothing here admits a round, a capability or a canon fact"; `depth/scribe.md` likewise, with a dedicated "Adjacent observations (reported, not absorbed)" channel). No canon decision, rights ruling, game mechanic, or general-research-method work was observed in landed fragments; no sibling province absorbed (see also §1.1, §3.4). **`PROVINCE.md` is unmodified in the wave and no correction is proposed** — its clauses remain accurate for the surfaces round 11 exercised. (Minor, pre-existing, not new drift: `tools/**` is exercised as a lane-local surface but is not named separately in the "Owns" enumeration; this predates round 11 and needs no textual change to be accurate, since the write-scope sentence already covers "this standalone lane repository".)

---

## 3. Lore-boundary and out-of-lane watch

### 3.1 Contract state

`kotodama-lore-adjacency`, revision **1.0.0**, canonical copy `corpus/knowledge/synthesis/worldbible-integration-contract.md`. This seat re-measured the live digest at 22:07Z: `sha256sum` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`. Bilateral same-revision read remains **pending** (contract §1); the round-8 L0 escalation (contract digest drift vs lore r93, who owns the update) is still open at `.ufo/l0-questions.md:45` and is **not changed by round 11** — the new packet re-measures the local digest and marks the bilateral read pending rather than asserting it.

### 3.2 The O packet — non-canon discipline verified

`reports/round-11/handoff/packet-attempt-1.md` (R11-O06) is a "deliberately unbound research packet; not canonized": explicit `canon_standing: not canonized — lore disposition required`; `handoff_status: prepared-not-accepted`; `baseline_bible_ref: none` (unbound drill, cannot be imported as canon without a lore baseline); `subject_refs` unresolved-by-design (no guessed lore IDs); `requested_decisions` "no decision requests canonization". Its `contract_ref` cites revision 1.0.0 with digest `5f4c02bf…` — **matches this seat's independent re-measurement**, and correctly flags the superseded round-7 prose digest. The same discipline appears in the `packet-attempt-1.yml` mirror. This is §4/§6/§8-conformant drill material.

### 3.3 The exercise — boundary function now passes

`tools/exercise-handoff-e2e.py` (landed during the wave; docstring: normal runs are read-only w.r.t. the lane, write only inside an isolated temp dir, and validate through the committed gate from a foreign working directory; non-canon marker enforced fail-closed). Seat run (TMPDIR=`$PWD/.scratch`) at 22:10Z:

```
python3 tools/exercise-handoff-e2e.py
→ OK contract-crossref: kotodama-lore-adjacency 1.0.0 sha256:5f4c02bfc4e6…
→ exercise-handoff-e2e: PASS — fields=16/16 glossary-entries=20 findings=0   (exit 0)
```

An earlier attempt at 22:09Z (before `tools/gates/expected/handoff-exercise/r11/expected.json` landed) exited 2 `CANNOT EVALUATE — frozen baseline not found` — recorded here so the two stamps are not confused. The frozen baseline is currently **untracked** (integrator commits it at close). The exercise's isolation ran under `$PWD/.scratch/handoff-exercise-*/isolated` — in-lane scratch, as mandated.

### 3.4 Out-of-lane watch

- **No kotodama write crossed into a sibling repo or the world bible** that this seat could observe: fleet root porcelain 0 throughout; `lore-shokunin`'s dirty set is its own round work (`M LOG.md`, `M corpus/tools/*`, `?? .ufo/waves/round-97/`, `?? corpus/fixtures/r97-crossing-acknowledgment/`, `?? corpus/knowledge/r97-acknowledgment-scope-note.md`; commits `r96*`) — no kotodama-named artifact among them. Limit: this is name/content + hash evidence, not process attribution.
- **Environment note:** `/tmp` inode exhaustion (round-9 L0 item) is **not live now** — `df -i /tmp` at 22:05Z: 2% used, 1 032 873 free inodes. One wave process was observed (ps, 22:02:38Z) passing a `/tmp/tmps5m3upcu/absent.md` fixture into the handoff gate — a minor deviation from the TMPDIR guidance, no impact observed.

---

## 4. Recommendations (integrator)

1. **Restore the remaining six filed paths** (§1.3, §1.4) from the committed blobs before close — one of the seven (`round-6/checkpoint-validation.json`) is already restored (§1.3 status); do not carry any remaining working-tree delta into the round-11 commit. Record the incident in the close note (this file is that record) rather than back-patching filed receipts — round-10 precedent.
2. **Have F12's summary tag side-effect rows** (102, 113, 114, 120, 129–132, 147, 170–173) and state that "hash-stable" there means the emitted content, not the filed file. F08's receipts show its runs did not rewrite filed bytes; no further live-write exposure is expected if its protocol is not changed.
3. **Prefer the F04/F05 protocols for any remaining writer rows** (full-tree mirror; importlib with `OUTPUT_REL` redirected) — both are already in use and documented in this wave.
4. **Re-run the O exercise at integration** after the frozen baseline is committed; the counting command `python3 reports/round-11/run-validation.py` remains the parent's acceptance form (runner landed untracked at census; not run by this seat).
5. **Keep the round-8 contract-digest L0 item open**; the packet's local re-measurement does not substitute for the bilateral read (contract §1/§10).

## 5. Limits and open items (to-verify)

- All observations are stamped snapshots taken while the wave was in flight (22:01Z–22:13Z); the dirty set can grow or shrink after these stamps (one restore already observed, §1.3 status).
- F07's live execution and F06's declared live protocol are proven; the intra-seat mapping of the 22:03:00–22:03:17 mtime ladder to F06's pass is an order/inference match (its receipts state the live root), not a process-table capture.
- The 22:10:24Z restore of the checkpoint receipt is unattributed (no seat claim observed); it is documented as a restore-because-rerun-would-still-fail (§1.3 status).
- The recheck hash conventions differ across seats (F04 combined stdout+stderr; F05/F07 stdout; ledger rows themselves vary by shard) — any cross-shard "stable" comparison needs the convention, not just the boolean.
- The exercise PASS above is a **seat-run probe**; the claim-O verdict belongs to the parent's counting command on the settled tree.
- `reports/round-11/report-draft.md` (X04) covers overlapping ground (Hazard 1); where numbers differ, the stamped tables here are the fuller evidence, and both should be reconciled by the report scribe at integration.

## 6. Stamps and receipts

Representative commands (lane root, `export TMPDIR=$PWD/.scratch`; stamps as executed, 2026-10-17 UTC):

```sh
cd /home/vgpnk/Projects/shokunin && git status --porcelain | wc -l          # 0 @ 22:02Z, 22:04Z, 22:07Z, 22:10Z
git log --oneline -1                                                          # e3ef171 @ every check
git status --porcelain                                                        # 7 M + in-scope ?? @ 22:07:57Z, 22:10:17Z; 6 M @ 22:12:54Z
git diff --stat                                                               # 7 files, +127/−881 @ 22:04Z; 6 files, +125/−859 @ 22:12:54Z
for f in <the 7 paths>; do stat -c %y $f; sha256sum $f; git show HEAD:$f | sha256sum; done   # x02 snapshot @ 22:04:38Z (.scratch/x02/check.txt)
sha256sum .scratch/f07/out/row-147.out                                        # 7c6333e7… == ledger row 147 prior; mtime 22:01:53.495Z
cat reports/round-11/recheck/row-147.json                                     # stable: true, prior==new==7c6333e7…
cat reports/round-11/recheck/row-{102,113,114,120,129,130,131,132}.json       # F05/F06 receipts @ 22:08–22:10Z
sha256sum reports/round-6/checkpoint-validation.json                          # 665dc2a0… == HEAD blob (restored) @ 22:11:42Z
cat reports/round-11/recheck/row-{170,171,172,173}.json                       # F08 receipts @ 22:11Z
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md       # 5f4c02bf… @ 22:07Z
python3 tools/exercise-handoff-e2e.py                                         # exit 2 @ 22:09Z (baseline absent), exit 0 PASS @ 22:10Z
df -i /tmp                                                                    # 2% inodes used @ 22:05Z
ls reports/round-11/recheck/row-*.json | wc -l                                # 168 @ 22:10:17Z; 192 rows 0–191, no gaps @ 22:12:54Z
```

FILES: reports/round-11/adjacency.md
SUMMARY: X02 adjacency — fleet root clean, HEAD unmoved; five filed round-5..9 receipts + a round-10 fragment remain clobbered by 1:1 recheck runs (one of six restored; row-147 read stable:true while the filed file changed); PROVINCE holds; lore-boundary clean, O exercise passes 16/16+20/20.
