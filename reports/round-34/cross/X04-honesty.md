- Seat: X04 | critic | cross | date 2026-10-19 | baseline da68a6d

# X04 — honesty critic: to-verify census, could-not-evaluate flags, unprovable-claim risks

**Read window.** 2026-10-19, lane HEAD `da68a6d705e41f369f21e8607bfaab5b54077f84`
(`git rev-parse HEAD`); working tree clean except the untracked round directory
(`git status --porcelain` → only `?? reports/round-34/`). Every command this seat
ran is read-only: no `reports/round-*/run-validation.py` was executed
(`find reports -name run-validation.py` → 29 paths, none run), no filed byte was
written, no shared file was edited. Two *tools* were executed — the handoff gate
and the box-1 survey — both verified read-only by reading their source first
(`tools/gates/handoff-packet-check.py`; `reports/round-30/craft/box1-survey.py:1-12`
prints JSON and exits, no write).

**Dependency state.** At every read this seat made, the round-34 tree held only
`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`
(`find reports/round-34 -type f`). **No sibling round-34 fragment existed.**
This is therefore a *pre-landing* census: §1–§4 audit the declared claims against
live bytes, not the seats' prose. The post-landing re-check is owed (see `## Owed`).

---

## 1. to-verify census

### 1.1 Live marker survey

| surface | count | reading |
|---|---|---|
| `SKILL.md` | 19 | the ten lines read (`:44`, `:46`, `:58`, `:99`, `:100`, `:101`, `:105`, `:116`, `:125`, `:420`) are the gate's own policy vocabulary (`status: to-verify` as a *verdict value*, `(to-verify)`-triage rules) — not open research claims. The remaining nine lines were **not each read** → `to-verify` |
| `SCORECARD.md` / `MINT.md` / `SHONEN.md` / `PROVINCE.md` | 0 | no live marker; findings are carried as `F-C…` ids instead |
| `corpus/README.md` | 2 | not read by this seat — low relevance to round 34's three claims → `to-verify` |
| `corpus/QUALITY.md` | 1 | not read by this seat → `to-verify` |

**Disposition: none of the live `to-verify` markers is an owe of round 34.** They
are vocabulary and policy sentences, not unresolved claims. The unresolved items
round 34 inherits are carried as *findings*, audited below.

### 1.2 Inherited open items (from round 33) and their status at HEAD

| id | source (filed, read-only) | status at HEAD | round-34 effect |
|---|---|---|---|
| F-C13-1 incident + restore | `LOG.md:3548-3563` | **Filed.** The record names the mechanism (`reports/round-5/run-validation.py:194`, `reports/round-7/run-validation.py:1171`, `reports/round-6/run-validation.py:336`), the window (03:53:25Z–03:55:27Z), the restore, and the prevention rule. This seat re-verified the three cited write sites exist exactly as cited | claim O's `before.gap` citation "F-C13-1 (round-33 LOG)" is **accurate** — no fabricated source |
| F-C13-1 telemetry half | `reports/round-33/calib/C13-consistency.md:178` asks for "a dated LOG.md/telemetry row" | `grep -ln "F-C13-1\|restored\|in-tree" reports/round-33/telemetry/*.json reports/round-33/telemetry/inputs/*.json` → **0 files**. The LOG half is filed; the telemetry half is not | **to-verify** whether the telemetry half was owed; the raw apportionment evidence lives in `C13-consistency.md:214-236`. Not a round-34 claim; recorded so it is not silently read as "done" |
| F-C13-1 writer attribution | `LOG.md:3556` — "probable writer: seat C05, `to-verify`" | correctly marked unprovable from artifacts | must **stay** marked; no seat may upgrade it |
| F-C13-4 membership ruling | `LOG.md:3538`; `SCORECARD.md:595-596` | filed as a ruling | none |
| F-C15-1 the numeral "12" | `reports/round-33/calib/K03-open-items.md:45-53`; `C01-item-01.md:275-276`; `C03-item-03.md:295`; `open-items-ledger.json` → `count_provenance.honest_status`; `SCORECARD.md:598` | **still `to-verify`** — the "12" is a reconstructed numeral, no filed artifact states the expansion rule | claim C re-issues *anchors*; it does **not** close this. It must not be dropped from the ledger |
| A09-F5 (`C14` drafts not on disk) | `reports/round-33/adj/A09-pins.md:126,135-136` | **Resolved by later landing**: `reports/round-33/calib/C14-fix-drafts.md` and `reports/round-33/op/O02-readme-delta.md` both exist at HEAD | none |
| A09 §2 (X00 collision matrix not on disk) | `reports/round-33/adj/A09-pins.md:131,135` | **Resolved by later landing**: `reports/round-33/cross/X00-connector.md` exists; its `:256` answers "A09 / R08: §3 is the requested matrix" | this seat did **not** row-by-row verify that match → `to-verify` (see `## Owed`) |
| Owed-path sweep over round-33 | 66 `.md` fragments, **54** carry a `## Owed` heading, of which 12 read `## Owed: none` | the remaining 42 name owed completions; the ones with live paths are all staffed by round 34's `targets.json` seats (K01→D/O/C scouts, verifiers). No round-33 owed path is left unstaffed by this round's seat list | none that this seat can see |

### 1.3 to-verify items inside the *round-34* declarations

- None. `claims.json` carries no `to-verify` marker; its unknowns are expressed as
  `before` states, every one of which this seat re-measured (§4).
- `reports/round-34/telemetry/dispatch-declared.json` correctly separates the
  pre-dispatch declaration from the observed record ("observed launches/completions/
  failures are recorded in a separate observed-dispatch record") — the shape
  `AGENTS.md:21-29` requires. **Risk flagged:** when the observed record lands, a
  failed or partial batch must not be written as `0` launches; unknown counters stay
  `null` with owner + reason (`AGENTS.md:27-29`).

---

## 2. could-not-evaluate flags

| # | flag | evidence | owner / required action |
|---|---|---|---|
| CE-1 | **Round-34 telemetry close is open by construction** | `reports/round-34/telemetry/dispatch-declared.json` → `"closing_snapshot": "open-at-seat-close: closing snapshot owed once validation.json lands"` | integrating parent, when `reports/round-34/validation.json` lands: file a **new** append-only snapshot under `reports/round-34/telemetry/`, naming this record and its SHA-256 at close time (`AGENTS.md:32-38`). This round is **not admitted to `LOG.md`** while the snapshot is owed |
| CE-2 | **e2e counting command not run by this seat** | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` is claim D's second counting command; its CLI offers `--keep DIR` / `--freeze DIR` (`tools/exercise-handoff-e2e.py:4489-4492`), so an unverified invocation could write outside `.scratch` | D17/D20 (verifiers) or the integrator: run it in an isolated copy, or confirm the default target is under `.scratch`, and record which. This seat did not run it |
| CE-3 | **9 unread `SKILL.md` `to-verify` lines; 3 unread corpus markers** | §1.1 | any seat needing them; not an owe otherwise |
| CE-4 | **round-33 incident has no telemetry row** | §1.2 row 2 | pm ruling; recorded, not asserted as a defect |
| CE-5 | **round-33 availability record closure** | `reports/round-33/telemetry/availability-close-33.json` exists alongside `dispatch-declared.json` and `observed-dispatch.json` | not re-derived by this seat (round 33 is filed and admitted); recorded only so the round-34 close follows the same pattern |

**Value of the `could-not-evaluate` token in the tree.** A repo-wide grep returns
287,732 hits, but that is an artifact-inflation reading, not a flag census: the
hits are dominated by `.scratch` clones of the round-26 gate-tests receipt and by
frozen snapshot prose. Constrained to the surfaces round 34 can act on
(`reports/round-*/telemetry/`, `reports/round-33/`, `reports/round-34/`) the count
is **140 lines across 56 files**, and every one is either (a) the *convention text*
itself, or (b) a seat's own honest "I could not measure X" note. **No unflagged
`could-not-evaluate` was found in the round-34 declarations.** The one live flag
that matters is CE-1.

---

## 3. Unprovable-claim risk register

### 3.1 Claim D — the improvement is invisible to every gate in the claim's own command list

**Measured at HEAD:** `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md`
→ `INFO scan: fields=16/16 glossary-entries=20 findings=0`, **exit 0**.

The *stale* pair is green right now on the exact numbers claim D's `after_required`
quotes ("16/16 + 20/20 + findings 0"). Therefore:

- **R-D1 (high).** No counting command in claim D's list can distinguish the stale
  packet from the fresh one. "Zero stale figures" is provable **only** by auditing
  every number-bearing row against live bytes. `run-validation.py` must encode that
  audit (extract each claim-ledger/OQ number from the new packet, re-derive it from
  `examples/culture-d4/**`, compare), or admission rests on two seats' prose.
- **R-D2 (high).** **Post-freeze drift is unaddressed.** The packet freezes live
  digests at build time; nothing in the claim detects a later change to
  `examples/culture-d4/typed-labels.d4.yml` (sha256 `c23b0ab5…`) or
  `examples/culture-d4/expected-holds.json` (sha256 `e6ae9828…`). Recommend a
  validation leg: re-hash the read set and compare to `freeze.txt` — otherwise
  round 34 recreates, one round later, exactly the defect it is fixing.
- **R-D3 (medium).** The claim's threshold names "two independent seats". D18 and
  D20 exist, but both are in this same batch; a same-batch verifier is *named* and
  *non-author* but not independently sourced. If the round wants an
  `unprovable-but-better` verdict anywhere, `REGIMEN.md:41` requires the named
  non-author reviewer to be recorded in the dossier — name the seat **and** the
  artifact it read.

### 3.2 Claim O — a satisfiable threshold that leaves the real hazard set uncovered

This seat ran an independent read-only census over all 29 filed runners
(`find reports -name run-validation.py`, guard-call detection + receipt-write-site
detection, script under §6 command list):

| class | count | files (write site) |
|---|---|---|
| **A — unguarded in-place receipt writer** | **12** | `round-5:194`, `round-6:336`, `round-7:1171`, `round-8:1486`, `round-9:1910`, `round-10:1054`, `round-11:1740`, `round-12:1071`, `round-19:21`, `round-21:1115`, `round-29:922`, `supplement-opencode-1:132` |
| **B — in-place writer that adopts the guard** | **17** | rounds 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33 (each calls `guard_receipt(...)` before its write; e.g. `round-33:1442` → `:1471`) |

Path constants confirming the write targets are the runners' own filed receipts, one
per file: `run-validation.py:99` → `OUTPUT_REL = "reports/round-8/validation.json"`;
`:127` → `reports/round-9/validation.json`; `:60` → `reports/round-10/validation.json`;
`:125` → `reports/round-11/validation.json`; `:18` → `OUTPUT = f"{ROUND_DIR}/validation.json"`;
`:20` → the same constant in round 21 (line numbers are within their own round's file).

- **R-O1 (high).** Claim O names four hazards (`r5`, `r6`, `r7`, `r26`) and its
  threshold is "the four named hazards classified". The true unguarded set is **12**
  — a seat can satisfy the threshold while 8 unguarded writers go unclassified. The
  threshold must be re-keyed to "*every class-A runner classified*".
- **R-O2 (high — the claim's own `before` is wrong about r26).** r26 **is guarded**:
  `reports/round-26/run-validation.py:1900-1909` calls its local `guard_receipt()`
  (`:1855-1857` → `namespace["guard_receipt"](OUTPUT, repo_root=ROOT)`) **before**
  `safe_path(OUTPUT).write_text(rendered)`. The guard refuses unless
  `REFRESH_RECEIPTS=1` (`tools/harness/receipt_guard.py:144-147`). So "r26 carries the
  same hazard (:90,:1909)" overstates: `:90`/`:1909` are the right *lines*, but the
  write is gated. The same wording is filed at `LOG.md:3557`. **Correction must be an
  append-only errata row, never an edit** (filed bytes).
- **R-O3 (high — the 29th runner is outside the declared glob).** The instrument's
  mission walks `reports/round-*/run-validation.py` (28 files); `find reports` shows
  **29**, the extra being `reports/supplement-opencode-1/run-validation.py`, which
  writes its own receipt at `:132` with **no** guard and **no** `REFRESH_RECEIPTS`
  gate. Under the strict reading of "100% of filed runners" the inventory is
  incomplete; under the glob reading it is complete but the 29th is out of scope
  without a stated reason. Either way it must be **named and classified**, not
  silently excluded.
- **R-O4 (medium — false-negative fixtures).** The selftest must include both traps
  the real tree already contains: (i) *references the guard, does not gate the write*
  — construct from r21's shape (`:474` sets `REFRESH_RECEIPTS=1` for a subprocess but
  the runner's own write at `:1115` is unguarded); (ii) *writes via a path constant*
  — r8/9/10/11/12-style `output = ROOT / OUTPUT_REL` (`round-8:1485-1486`), which a
  detector keyed on the literal string `validation.json` at the write line will miss.
  A classifier that only greps for `guard_receipt` would score class B correctly and
  class A barely; the guard-*call* pattern is the discriminator, not the import.
- **R-O5 (low).** `reports/round-19/run-validation.py:13` re-runs
  `python3 tools/check-gate-battery.py` **in-tree** as part of its measurement. That
  is not an F-C13-1 breach (it is not a round runner), but it is an unguarded in-tree
  measurement surface reachable by a historical runner — worth one inventory column.

### 3.3 Claim C — the survey proves resolvability, not executability; and "R1–R8" is not a SKILL-anchor list

- **R-C1 (high).** `reports/round-30/craft/box1-survey.py:6-7` is `set(re.findall(r"tools/[\w./-]+\.py", skill))` filtered by `(ROOT/s).is_file()`. It proves **28 path strings in SKILL.md name existing files**. It proves nothing about execution, behaviour, or the truth of what SKILL.md says about them. Claim C's wording ("28/28 named executables resolve") is honest; any downstream prose that reads box-1 as "the executable surface is verified" is **not** evidenced by this instrument and should carry that gloss.
- **R-C2 (high — scope mismatch).** `A09-pins.md:107-114` defines R1–R8 as *pin classes*, of which only **R3** (SKILL.md sha256 sites) and **R5** (SKILL.md line anchors) are SKILL surfaces. R1 is the lessons-README blob, R2 the README digests, R4 the box-1 receipt, R6 the README prose, R7 the x45/x57 historical controls, R8 the README-vs-lesson landing order. Claim C's `after_required` ("the A09 R1–R8 SKILL anchor reissue … covers every A09 R1–R8 row") therefore reads two ways, and the destructive reading is the naive one: a validator demanding eight old→new **SKILL anchor** pairs would force six rows to be invented. Required clarification: the table covers all eight rows *with the correct surface per row*, and only R3/R5 carry SKILL anchors.
- **R-C3 (high — the fallback branch of R5 fired and its scope is larger than claim C's).** `A09-pins.md:111` set R5's preferred control as a line-count-neutral edit (`wc -l SKILL.md` = **715**); HEAD reads **732** (`wc -l` → 732). The fallback — "record the shift and re-issue the anchor" — is therefore in force, and it reaches every citation below the change point, which `A09-pins.md` §2.4 enumerates: `AGENTS.md:42`; `SKILL.md:149,183` self-cites of `:47`; and the filed lesson citations (`corpus/lessons/round-31.md:46`; `round-32.md:7,33,41,55,57,58`; `round-25.md:44`; `round-19.md:88,100,101,179`; `round-15.md:25`; `round-14.md:141`). Claim C's scope sentence names the R1–R8 rows but not this §2.4 citation list. Recommend the reissue table cover both, or state explicitly why §2.4 is out of scope.
- **R-C4 (medium — the `before` field is imprecise).** Claim C states the round-30 box-1 survey "is green only as console output at the old digest". Measured: a **durable** receipt is filed at `reports/round-30/craft/box1-landed-survey.json:4` pinned to `83b0a78a…`, and the `79fe91d3…` verification exists as **dossier prose** (`reports/round-32/final-dossier.md:46`, "inventory condition CLOSED — 28/28 named executables resolve, re-verified this round"). The precise statement is: the durable receipt is pinned to the *oldest* of the three digests; the `79fe91d3…` claim is prose; the current digest `f9bd07c2…` has no durable receipt. Claim C's *action* is right; its *before* wording should be corrected in the dossier.
- **R-C5 (positive finding).** This seat independently re-ran the survey at HEAD:
  `python3 -B reports/round-30/craft/box1-survey.py` →
  `{"named": 28, "resolvable": 28, "unnamed_in_skill": [], "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"}`,
  **exit 0**. So claim C's 28/28 target is **already true at HEAD** and the deliverable is *durability* (a dated, digest-pinned receipt), not a repair. `A09-pins.md:110` anticipated that `named_in_skill` "may move off 28" — it did not; it is still 28.

### 3.4 `unprovable-but-better` verdicts

None of D/O/C requires one **provided** the audits in §3.1–§3.3 are encoded in
`run-validation.py`. If any seat instead asserts an axis move on prose alone,
`REGIMEN.md:41` requires a named non-author reviewer; the round has R01–R08 in-batch,
so a name exists — but the dossier must state the seat and the artifact it read, and
must not present an in-batch reviewer as external verification.

---

## 4. Declared `before` vs live bytes (audit of `claims.json`)

| field | verdict | measurement |
|---|---|---|
| D `before.renderer_default` | **verified** | `tools/exercise-handoff-e2e.py:1933` `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"`; `:1934` `V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"` (`grep -n`, exact) |
| D `before.stale_numbers` | **verified** | `packet.md:148` D4-CL05 cites `typed_labels 74 / native-form 56 / findings_total 16 / findings_hold_or_fail 15`; `:149` D4-CL06 `hold 15, note 1`; `:150` D4-CL07 `conflicts 4`; `:152` D4-CL09 `rank_quarantine_handles 3`, `conflicts 4`; `:307` OQ-V3-05 repeats them (all read directly) |
| D live values (my own reads) | **verified** | `examples/culture-d4/typed-labels.d4.yml` → `:46 typed_labels 82`, `:38 native-form 64`, `:37 translated-label 12`, `:36 borrowed-strata 6`, `:31 findings_hold_or_fail 12`, `:32 findings_total 12`, `:30 conflicts 0`, `:40 rank_quarantine_handles 0`, `:44 rank_rules_unresolved_items 0`; `examples/culture-d4/expected-holds.json` `counts` → `{hold: 12, note: 0, fail: 0}`. Values unchanged from the claim's `82/64/12/12+0/0/0/0` |
| D `before.self_contradiction` | **verified** | `packet.md:66-70` (A-28…A-32) already carry the live values (82 labels / 64 / 12 / 6; 12 hold / 0 note / 0 fail) while `:148-152` do not — the packet contradicts itself on its own bytes |
| O `before.gap` — r5/r6/r7 mechanism | **verified** | `reports/round-5/run-validation.py:194`, `:336`, `:1171` each `(HERE / "validation.json").write_text(...)`, no guard call, no `REFRESH_RECEIPTS` |
| O `before.gap` — "guard exists since round 14" | **verified** | `git log --diff-filter=A -- tools/harness/receipt_guard.py` → `b02cfbc 2026-10-17 round-14: … receipt-guard capability` |
| O `before.gap` — "no inventory instrument exists" | **verified** | `ls tools/harness/receipt_guard_adoption.py` → `No such file or directory` |
| O `before.gap` — **"r26 carries the same hazard"** | **DEFECT** | r26 adopts the guard (§3.2 R-O2). Correct classification: "in-place writer, **adopts** the guard". Same wrong wording filed at `LOG.md:3557` → needs an append-only errata row |
| O scope — "walk `reports/round-*`" | **DEFECT (coverage)** | 29 runners exist; the 29th (`reports/supplement-opencode-1/run-validation.py:132`) is an unguarded in-place writer outside the glob (§3.2 R-O3) |
| C `before.state` — digest/line movement | **verified** | `sha256sum SKILL.md` → `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`; `wc -l` → 732 (claim: `79fe91d3…` → `f9bd07c2…`, 715 → 732) |
| C `before.state` — "green only as console output at the old digest" | **imprecise** | see R-C4: a durable receipt exists at `83b0a78a…`; `79fe91d3…` is dossier prose |
| C scope — "A09 R1–R8 SKILL anchor reissue" | **imprecise** | only R3/R5 are SKILL surfaces (§3.3 R-C2) |

**Nothing in the declarations was found fabricated.** Every cited path and line
resolved as cited; the two defects are wording/coverage, both correctable by
append-only rows.

---

## 5. Drafted corrections for the integrator (no shared or filed file was edited)

1. **`LOG.md`, new append-only errata row** (never an edit of `:3557`):
   "Erratum (2026-10-19, round 34): the F-C13-1 entry states the r26 runner 'carries
   the same hazard (:90,:1909)'. Re-measured: `reports/round-26/run-validation.py`
   **adopts** the guard — `:1900-1909` calls `guard_receipt()` before the write,
   which refuses unless `REFRESH_RECEIPTS=1` (`tools/harness/receipt_guard.py:144-147`).
   The correct class is 'in-place writer, guard-adopting'. The unguarded in-place
   writers number twelve: rounds 5, 6, 7, 8, 9, 10, 11, 12, 19, 21, 29 and
   `reports/supplement-opencode-1/run-validation.py:132`."
2. **`reports/round-34/claims.json` claim O — threshold re-key** (integrator's file,
   applied at integration): replace "the four named hazards classified" with
   "**every class-A runner classified (12 at baseline), including the one outside the
   `reports/round-*` glob**", and add `reports/supplement-opencode-1/run-validation.py`
   to the named hazards.
3. **`run-validation.py` leg spec (for S04):**
   - D: stale-figure audit leg (each new packet number re-derived from live bytes)
     **and** a drift leg (re-hash the read set, compare to `freeze.txt`).
   - O: inventory denominator check (`find reports -name run-validation.py | wc -l` ==
     the inventory's row count, with the out-of-glob row present and classified).
   - C: reissue-table coverage check that accepts non-SKILL surfaces for R1/R2/R4/R6/
     R7/R8 and requires SKILL anchors only for R3/R5.
4. **Dossier wording:** claim C's `before` and the "A09 R1–R8 SKILL anchor" phrase
   corrected per R-C4/R-C2; claim D's threshold annotated that the gate is green on
   the stale pair (so the gate is not the freshness evidence).

---

## 6. Truthful limits of this seat

- The cross-fragment census could not be performed: no sibling fragment existed at
  my reads. §1–§4 are therefore claims-vs-live-bytes, not seat-vs-seat.
- I did not run `python3 reports/round-34/run-validation.py` (it does not exist) and
  no filed runner (F-C13-1 prevention).
- I did not run `tools/exercise-handoff-e2e.py --profile v3 --quiet` (CE-2).
- The census script was read-only; its detection is line-based, so a runner writing
  its receipt through a helper function defined in another file would be classified
  on its write-site line only. Every classification above is backed by a quoted line,
  so the reader can re-check independently.
- Commands used for the census (re-runnable):
  `find reports -name run-validation.py | wc -l` → 29;
  per-file guard detection (`grep -n "receipt_guard" <runner>`, then reading the
  call site); write-site detection (`write_text`/`json.dump` lines plus the
  `OUTPUT`/`OUTPUT_REL` constants); `grep -rc "could-not-evaluate"` constrained to
  `reports/round-*/telemetry/ reports/round-33/ reports/round-34/` → 140 lines / 56 files.

## 7. Post-landing corroboration (appended after my §1–§6 reads)

Sibling fragments landed while this fragment was being written. This seat re-read
the ones that bear on §3.2, and the result is **convergent independent verification**,
not a new finding:

| my finding | independent corroboration (landed) | verdict |
|---|---|---|
| R-O2 — r26 is guard-adopting, not a hazard | `reports/round-34/scout/K03-guard-pattern.md:48` ("**guarded (write-only)**"), `:52-56` ("r26 is *not* a same-class hazard as r5/r6/r7") and `:170` (LOG citation "corrected"); `reports/round-34/op/O04-predicted-inventory.md:64` (`"class": "guarded-in-place-write", "hazard": false`); `reports/round-34/scribe/S02-o-receipt.md:135-144` ("Falsified: `claims.json:42` and `LOG.md:3559-3560`") | **corroborated three ways** |
| R-O1 — the true unguarded set is 12, not 4 | `S02-o-receipt.md:24` ("the true unguarded set is 11, not the 4 named"), `:144` ("Omitted: r8, r9, r10, r11, r12, r19, r21, r29"), `:185` (routing table for the 11 in-glob) | **corroborated** |
| R-O3 — a 29th runner sits outside the round glob | `reports/round-34/op/O09-verify-routing.md:59,224-240` (defect **D-4**, "outside the round glob"), `:136` (row: "**yes**, unguarded"); `S02-o-receipt.md:28,89-90` | **corroborated** |
| 17 guarded / 11 unguarded split | `O04-predicted-inventory.md:41` → `{"runners": 28, "guarded_in_place": 17, "unguarded_in_place": 11, …}` — identical to this seat's independent census | **matches exactly** |

**What this changes:** R-O1/R-O2/R-O3 are secure; the round does not depend on this
seat's word for them. **What it does not change:** the *corrections* are still owed —
`LOG.md`'s tail carries no round-34 errata row for the r26 sentence as of this read
(`tail -25 LOG.md` → the newest rows are round-33 supersession/operator rows), and
the claim threshold in `reports/round-34/claims.json:42-45` still reads "the four
named hazards classified". Threshold re-keying is an integrator act; the errata row
is an integrator act. Until both land, a reader who consults only `claims.json` and
`LOG.md` still gets the falsified r26 class.

**Still unverified by this seat:** the D-block stale-figure audit leg (whether the
D seats encoded the audit or only asserted it) and the C-block reissue-table
coverage (R-C2/R-C3 scope) — the relevant fragments (`depth/*`, `calib/*`,
`review/R0{1,2,3,6,7}*`) had landed but were not read by this seat before its budget
closed. Recorded as owed below rather than guessed at.

## Owed

- `reports/round-34/cross/X04-honesty.md` (this file) — **remaining post-landing
  re-check**: read the landed `depth/*` and `calib/*` fragments plus
  `review/R0{1,2,3,6,7}*` and verify (a) the D stale-figure audit is *encoded* in the
  draft's validation leg rather than asserted, (b) the D drift leg (§3.1 R-D2) was
  adopted, (c) the C reissue table's R1/R2/R4/R6/R7/R8 rows carry non-SKILL surfaces
  (§3.3 R-C2) and §2.4's filed line citations are covered (§3.3 R-C3), (d) no seat
  ran a filed runner in-tree.
- `LOG.md` append-only **errata row** for the r26 hazard sentence (§5 item 1) —
  owner: integrating parent. Not landed as of this read.
- `reports/round-34/claims.json:42-45` **threshold re-key** for claim O (§5 item 2) —
  owner: integrating parent (only the integrator applies shared/declaration edits).
- `reports/round-34/run-validation.py` legs: D stale-figure audit + drift check, O
  denominator check against the 29-runner census, C surface-aware coverage check
  (§5 item 3) — owner: S04/integrator.
- `reports/round-34/cross/X00-connector.md` — cross-claim consistency (not landed at
  this seat's final read): does the re-pin cascade change any runner's adoption class?
- `reports/round-34/telemetry/` closing snapshot (owner: integrating parent;
  `AGENTS.md:32-38`) — round 34 is not admissible to `LOG.md` while it is owed.
- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (owner: D17/D20 or
  integrator) — run in isolation or confirm its default target is under `.scratch`.
- `to-verify`: whether `reports/round-33/cross/X00-connector.md:256`'s "§3 is the
  requested matrix" discharges `A09-pins.md:135` row-for-row.

## Citations

Files read (all read-only):

- `reports/round-34/claims.json`, `reports/round-34/targets.json`,
  `reports/round-34/telemetry/dispatch-declared.json`
- `REGIMEN.md:27-51` (claim/verdict contract; `:41` unprovable-but-better reviewer rule)
- `AGENTS.md:21-29` (unknown counters null; liveness ≠ acceptance), `:32-38` (close what you open)
- `tools/exercise-handoff-e2e.py:1933-1934` (defaults), `:4484-4492` (CLI), `:3806`, `:4149`
- `tools/gates/handoff-packet-check.py` (run on the r6 pair)
- `reports/round-30/handoff/declared-in-r6/{packet.md:66-70,148,149,150,152,307; expected.json; freeze.txt; twin.json; run.log}`
- `examples/culture-d4/typed-labels.d4.yml:30-46`; `examples/culture-d4/expected-holds.json` (counts)
- `tools/harness/receipt_guard.py:34-36,144-147,152-168`; ls of `tools/harness/` (adoption tool absent)
- `reports/round-30/craft/box1-survey.py:1-12`; `reports/round-30/craft/box1-landed-survey.json:1-8`
- `reports/round-32/final-dossier.md:46`
- `reports/round-33/adj/A09-pins.md:107-116,126,130-136` and §2.2/§2.4 lists
- `reports/round-33/calib/C13-consistency.md:23,27,178,192-193,214-236`; `calib/open-items-ledger.json` (count_provenance, consistency_receipt); `calib/C15-ledger-draft.json:46`
- `reports/round-33/calib/{C01-item-01.md:275-276, C03-item-03.md:295, K03-open-items.md:45-53}`
- `reports/round-33/cross/X00-connector.md:34,41,256`; `ls reports/round-33/cross/`
- `LOG.md:3538, 3548-3563` (F-C13-1 record; `:3557` r26 wording, `:3556` C05 attribution)
- `SCORECARD.md:588-600` (round-33 admission, findings on record)
- runners: `reports/round-{5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33}/run-validation.py`, `reports/supplement-opencode-1/run-validation.py`
  — read at the write-site / guard-call lines cited in §3.2 (`round-8:99,1485-1486`; `round-9:127,1910`; `round-10:60,1054`; `round-11:125,1740`; `round-12:18,1071`; `round-19:13,19-21`; `round-21:20,474,1115`; `round-29:922`; `round-26:90,1855-1857,1900-1909`; `round-32:1103,1143`; `round-33:1442,1471`; `supplement-opencode-1:132`)

Commands run (read-only):

- `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`; `git status --porcelain` → `?? reports/round-34/`
- `sha256sum SKILL.md`; `wc -l SKILL.md`
- `python3 -B reports/round-30/craft/box1-survey.py` → 28/28, exit 0
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` → `fields=16/16 glossary-entries=20 findings=0`, exit 0
- `find reports -name run-validation.py | wc -l` → 29; `ls reports/round-*/run-validation.py | wc -l` → 28
- guard-call / write-site census (python one-liner over the 29 runners; printed per-file class)
- `git log --diff-filter=A -- tools/harness/receipt_guard.py` → `b02cfbc` round-14
- `git log --format=… -2 -- reports/round-{5,6,7}/validation.json` (receipts' last commits predate round 33 → no filed-byte residue)
- `grep -rc "could-not-evaluate"` constrained to the round surfaces → 140 / 56 files; `grep -ln` over `reports/round-33/telemetry/**` for the incident row → 0
