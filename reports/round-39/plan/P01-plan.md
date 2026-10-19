- Seat: P01 | planner | cross | date 2026-10-19 | baseline dfb0719

# P01 — round-39 plans for both claims (C coverage, Ca calibration)

- Round 39 (regimen 2, loop 1, position 7), seat P01, claim **cross** (plans for C and Ca). Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; baseline `dfb0719711204b5943432034bd80c8dc248acddd`
  (`git rev-parse HEAD` → `dfb0719711204b5943432034bd80c8dc248acddd`, 2026-10-19; `git log --oneline -1`
  → `dfb0719 round-38: admit D/O/C ...`).
- **Writes: this fragment only.** No corpus bytes, no tool bytes, no filed-round bytes. I ran only
  read-only measurement (`ls`, `grep`, `git log`, `git rev-parse`, `python3 -B reports/round-28/readme/sweep.py`).
  No `reports/round-*/run-validation.py` was executed anywhere, in-tree or otherwise (ABSOLUTE rule).
- **Dependency status at write time (single 16-seat batch):** my mission says "plans for both claims
  from K01/K02". `reports/round-39/scout/K01-verification-gaps.md` and
  `reports/round-39/scout/K02-isolation.md` **do not exist yet** (`ls -R reports/round-39/` →
  `claims.json targets.json telemetry` only). Per the missing-dependency rule I derived both plans
  directly from the primary evidence (filed runners, ledgers, queue rows, audit instruments, live
  measurement), and each plan states the exact insertion points where K01/K02 output slots in.
  Executors do not wait: each section below is written so the named seat can start from it alone.

---

## Part 1 — Claim C plan (coverage: verification partition 20 → 24)

### 1.1 Baseline (measured this round, 2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

- `ls corpus/knowledge/verification/*.md | wc -l` → **20**; total corpus **212** (sweep below).
- `python3 -B reports/round-28/readme/sweep.py` → exit 0: `rows 212 files 212`, `missing 0`,
  `topic_mismatch 0`, `orphan_rows 0`, `totals_line 212 totals_ok True`, footer
  `total 212, dir_totals [21, 23, 25, 29, 20, 94]`, `footer_ok True`, `readme_sha256 b80274bc…e1d74`.
  Footer order is `linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`
  — so the claims-vector target `21/23/25/29/24/94` changes **only the 5th slot (verification 20 → 24)**.
- Corpus README is at **revision 2.1** (r36 timekeeping landing), `corpus/README.md:5`.
- The 20 existing verification entries (topic space the 4 new entries must not collide with):
  calibration-registry, citation-format-and-source-registry, costume-era-consistency-gate,
  gate-battery-surface-verification, gate-frozen-run-standard, generated-artifact-roundtrip-verification,
  header-conformance-readings, internal-consistency-audit, label-channel-routing-verification,
  lexicon-coverage-audit, myth-consistency-gate, naming-collision-gate, phonology-sanity-gate,
  pre-declared-hold-set-reconciliation, provenance-audit-ledger-format, real-world-inspiration-boundaries,
  to-verify-triage-protocol, two-reader-interop-agreement, verification-independence-anti-circularity,
  verification-method-overview (`ls corpus/knowledge/verification/`, 2026-10-19).

### 1.2 Topic slot assignment (C01–C04) — pending K01, self-derive rule armed

- K01's `## Owed` deliverable is 4 gap-named topics with sources. **Slot contract:** each of
  C01/C02/C03/C04 takes exactly one topic, distinct slug, registered in that seat's fragment (slug +
  one-line gap statement + absence-sweep outputs). K01's fragment, when it lands, binds the mapping
  topic→seat in its own header; until then each executor self-derives per the round-35 precedent
  (`reports/round-35/cov/C01-entry-1.md:8` — derived the topic from a partition census + recorded
  absence sweep, owed the planner confirmation).
- **Collision guard (binding on all four):** before authoring, run
  `ls corpus/knowledge/verification/ | grep -i <slug-keywords>` and
  `grep -rln <slug> reports/round-39/` — if another round-39 fragment claims the slug, re-slug with a
  `-b` suffix and register the re-slug in the fragment (r19 registry convention,
  `reports/round-19/gaps.md:1-22`). X00's matrix reconciles the final four.
- **Planner-seeded candidate directions** (not assignments; K01 overrides). Each is a method this
  lane exercises every round with reports-side precedent but no verification-partition owner:
  1. isolated-replay / recount verification standard (worktree-at-close-commit protocol; precedent
     lives in `reports/round-37/calib/*` and this round's Ca work — the *corpus* entry would own the
     method, not the r39 artifacts);
  2. defect-queue lifecycle record format (24-row precedent `reports/round-37/op/defect-queue.json`,
     schema `kotodama-defect-queue-v1`; no corpus entry owns the record class);
  3. index-sweep / counts-footer reconciliation standard (the `reports/round-28/readme/sweep.py` legs
     and the r28 stale-footer defect story; no corpus entry owns the sweep method);
  4. availability-telemetry record + closing-snapshot standard (AGENTS.md close-what-you-open; no
     corpus entry owns the record format). Every author must still run their own absence sweep and
     drop any candidate the sweep shows is already owned.

### 1.3 The entry contract (executable bar — each of C01–C04 satisfies all of it)

- **Head block** (r35 four-leg reading `R35-4F-1`, `reports/round-35/cov/C12-audit-runbook.md:34`):
  `- sources:` **or** `- source:`; `- verified-at:` (ISO date); `- recheck:`; scope leg via `- scope:`
  **or** `- couples:`. Round-10 five-field set `topic, sources, verified-at, recheck, couples`
  (`R35-5F-1`, runbook :35, citing `reports/round-10/run-validation.py:81`). Practically: carry
  `- topic:`, `- gap:` (or `- gap filled:`), `- sources:` (plural) **and** a singular `- source:`
  provenance line, `- couples:`, `- verified-at:`, `- recheck:` — the r35 exemplar field set
  (`reports/round-35/cov/C01-entry-1.md:36-37`; header census there: `topic 201, sources 201,
  couples 201, verified-at 202, recheck 202` corpus-wide; no `- scope:` field exists anywhere).
- **Executable gate** (`reports/round-19/audit/entry-audit.py:25-27,106-133`): `HEADER_RE` requires
  `topic`/`sources`/`couples`; `tail_ok` requires `verified-at` plus (`recheck` or `source`);
  `GAP_RE` and `DECISION_RE` must match; `couples_targets()` must resolve every `.md` ref on disk
  (brace groups expand one level).
- **Gap statement** (blocker tier): a frontmatter gap field with the absence-sweep commands **and
  their real outputs** — never a bare assertion (r35 pattern,
  `reports/round-35/cov/C01-entry-1.md:47`).
- **Decision record** (major tier): a `## N. Decision record` section with `DR-<INIT>-NN` ids
  (runbook :39; r35 exemplar §4).
- **Source ids:** `KTD-<SLUG-INIT>-S-####` convention (`reports/round-35/cov/C01-entry-1.md:36`).
- **Pointer hygiene** (blocker): every backticked repo-path token resolves on disk; dangling tokens
  only allowed when the same line marks them `(to-verify`; URLs are recorded unfetched, never counted
  resolved (runbook :37). Digest pins are review-tier (runbook :38).
- **No-bleed** (review tier, read each hit): unnegated `promoted/promotion/cleared/clearance/closure/
  signed off/green-lit`, ownership assertions, `canon` mentions (runbook :41-43). Non-canon boundary
  sentence named in the entry (runbook :44; every existing verification entry carries one).
- **Quality bar:** `corpus/QUALITY.md:3-20` — provenance, calibration, coupling, usability, canon
  hygiene. **Calibration clause mandatory:** a verification-method entry must say what its passing
  does *not* certify ("passing structural gates do not certify historical truth" — the standing
  corpus-wide clause, `corpus/README.md` every revision footer).
- **Register discipline:** a verification-partition entry is a lane-local method/protocol/registry —
  it adjudicates no claim, certifies no round, decides no canon (`to-verify-triage-protocol.md:11-13`
  is the register's tone exemplar).

### 1.4 Per-seat obligations

- **C01–C04 (authors):** one entry each per §1.2/§1.3. Fragment = fenced full entry bytes + the gap
  evidence + the measurements section. No corpus bytes; integrator applies.
- **C05 (verifier):** run the runbook (`reports/round-35/cov/C12-audit-runbook.md` §1, all six
  families) over all four drafts + resolve every source pointer. Blockers/majors filed as a defect
  list with exact line refs; `pass: false` on any blocker. Expected result: 4 drafts green or
  defect-listed; the audit is on **draft bytes as fenced**, using a `.scratch` staging copy.
- **C06 (README delta + receipt):** draft against the current filed bytes **as-is**. Delta =
  (a) new `revision: 2.2` block at the top of the revision list naming the four entries, their author
  fragments (`reports/round-39/cov/C01..C04-*`) and the audit (`reports/round-39/cov/C05-audit.md`);
  (b) `## verification/` section header 20 → **24**; (c) four rows added **in filename order**, each
  row's `- topic:` text **byte-equal** to the entry's own topic line; (d) totals line 212 → **216**;
  (e) counts footer vector → **216** / `21/23/25/29/24/94`. Receipt draft cites the **post-apply**
  sweep per the standing rule (`reports/round-37/op/defect-queue.json:242-250`,
  `readme-prediction-vs-delivery`: predict by staged-tree sha, cite post-apply sweep). Expected
  post-apply sweep: `rows 216 files 216`, footer `[21,23,25,29,24,94]`, exit 0.
- **Do not repair carried README defects in this delta.** Observed this round: the H1 heading is
  duplicated at `corpus/README.md:1` and `:3`, and the rev-2.0 opening line is duplicated at `:14`
  and `:16` (`grep -n "^# \|revision:" corpus/README.md`). These are carried-with-owner queue rows
  (`R36-README-DUPLICATE-HEADING`, `R36-README-E3-PLACEHOLDERS`,
  `R36-README-ORDER-CONTIGUITY-REVERIFY`, `reports/round-37/op/defect-queue.json:103-131`) — the
  delta inserts around them; repair stays with the queue owner, else the delta becomes an undeclared
  filed-byte rewrite.

### 1.5 Counting commands + thresholds (claim C acceptance, integrator-side)

- `ls corpus/knowledge/verification/*.md | wc -l` → 24.
- `python3 -B reports/round-28/readme/sweep.py` → exit 0, 216 rows/files, footer_ok True.
- Audit: C05's runbook pass over all four drafts, named defects allowed only as filed defects.
- No freshness move, no promotion language (non-goals, `reports/round-39/claims.json:26-27`).

---

## Part 2 — Claim Ca plan (calibration: isolation-replay protocol + r37 recount closure + basename policy)

### 2.1 Baseline (filed evidence)

- **The 4 could-not-reproduce rows:** `R37-Ca-05` (r34/C), `-06` (r34/D), `-07` (r34/O), `-08`
  (r34/cross) — `reports/round-37/calib/recount-ledger.json:60-111`, summary
  `"could-not-reproduce": 4` (:451-455). Filed cause on each: "absolute-root chdir makes an
  unmodified git-archive invocation exit before measuring (the O12 isolation hazard)".
- **O12 mechanics (read from the filed bytes):** `reports/round-34/run-validation.py:10` sets
  `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` (absolute) and `:26` does module-level
  `os.chdir(ROOT)`; same shape at `reports/round-35/run-validation.py:9`. `reports/round-33/
  run-validation.py:23` uses `ROOT = Path(__file__).resolve().parents[2]` and is immune. Consequence:
  a runner copy executed from an isolated tree chdirs **back into the live tree** — wrong-tree
  measurement, and in default mode a live-tree receipt write (the r36 in-tree incident,
  `reports/round-37/op/defect-queue.json:233-240`; narrative `reports/round-38/scribe/
  S01-integration-draft.md:418-425`). Open defect row `O12-runner-isolation-hazard`,
  `reports/round-37/op/defect-queue.json:193-201`, next_touch "runner cwd-hardening pass".
- **Prior partial reproduction:** Ca08 reproduced r34 **C and D** "unmodified runner source under the
  namespace"; **O and cross were not part of that sample and remain unverified**
  (`reports/round-37/calib/Ca08-verify.md:27`). The protocol's replay target therefore has real
  residual work.
- **Commit map for replays** (`git log --oneline -8` this round): `4a7aede` = round-34 close (r35's
  baseline, `reports/round-35/cov/C01-entry-1.md:6`); `da68a6d` = r33 close / r34's pinned baseline
  (runner `:14`); `dfb0719` = current HEAD. **Ca02 replays at `4a7aede`.**
- **Basename fallback (undocumented policy, the r37 queue item):** queue row
  `basename-couples-policy` `reports/round-37/op/defect-queue.json:203-211` — "couples resolver
  leaves 15 basename-only references unresolved; a working unique-basename fallback exists but is
  undocumented policy; document or fix the resolver". A12's cross-check: at `57c8409`, 334 distinct
  couples tokens = 319 path-resolved + **15 basename-shorthand**, 0 ambiguous, 0 unresolved; all 15
  originate in `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37` and map 7
  linguistics / 6 culture-material / 1 verification / 1 synthesis, each to its declared partition
  (`reports/round-37/adj/A12-gap-fill.md:9-26,38`). Resolver conventions precedent:
  `reports/round-35/cov/C14-audit-6-10.md:239-288`; `reports/round-19/audit/entry-audit.py:74-96`.

### 2.2 Ca01 — the isolation-replay protocol (`reports/round-39/calib/Ca01-protocol.md`, fenced)

Acceptance criteria — the document is complete when it specifies, mechanically:
1. **Worktree at the close commit, only.** `git worktree add --detach <path> <close-sha>`; runner
   bytes checked out from that commit, never patched. Worktrees only — never in-tree, never archive-
   copy for r34/r35 (their chdir defeats archives; that failure is the thing being fixed).
2. **Relative-root requirement.** A filed runner is replay-safe only if its `ROOT` derives from
   `__file__` (r33 shape, `reports/round-33/run-validation.py:23`). The protocol must include a
   **pre-flight guard**: grep the runner for an absolute `ROOT =` literal / module-level
   `os.chdir(<absolute>)`; if found, the plain worktree run is forbidden as a measurement (it would
   chdir into the live tree) and the runner is routed to the absolute-ROOT branch (3).
3. **Absolute-ROOT branch.** For r34/r35-shape runners, replay only under a mechanism that makes the
   worktree **be** the path the runner hardcodes — Ca08's namespace isolation is the precedent
   (`Ca08-verify.md:27`) — or via `--check`/`--selftest` modes with an explicit wrong-tree detector.
   Either way the protocol must name a **discriminating observable** proving which tree was measured:
   e.g. compare `git ls-files | wc -l` in worktree vs live tree against a path-count printed in the
   runner output (r37 precedent: r33 A-leg prints tracked-path counts — 2,655 filed vs 2,947 at the
   r37 tree, `reports/round-37/calib/recount-ledger.json:17`). A replay whose observable matches the
   live tree is **void**, not evidence.
4. **Mode discipline:** `--check` only for measurement replays (r34 `--check` "print the receipt,
   never publish", `reports/round-34/run-validation.py:4-5`); default/publish mode only inside the
   isolated namespace, never against the live tree.
5. **TMPDIR + bytecode isolation:** `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` with PWD
   = worktree root; scratch dirs inside the worktree or `.scratch/`, gitignored.
6. **Fleet-root inputs:** r34's runner reads fleet-root absolutes (`:21-22` FLEET_REPORT, MANIFEST)
   that a lane-repo worktree does not contain. The protocol must classify each leg: read-only fleet
   inputs may be read from the live fleet root (fleet `.ufo/**` is never edited); legs that cannot be
   satisfied under isolation are recorded `could-not-evaluate` with the cause — the cross leg's r33
   precedent (`reports/round-37/calib/recount-ledger.json:56`).
7. **Post-run hygiene:** `git status --porcelain` in **both** worktree and live tree must show zero
   writes outside `reports/round-39/`; `git worktree remove` cleanup step; the record names the close
   sha, the commands, and their outputs.
8. **Address O12 explicitly:** state how the protocol reduces `O12-runner-isolation-hazard` for
   *future* rounds (the durable fix remains the runner cwd-hardening pass; the protocol is the
   replay-side discipline until runners are hardened — do not claim the defect fixed).

### 2.3 Ca02 — replay-verify (`reports/round-39/calib/Ca02-replay-verify.md`)

- Execute the protocol against `reports/round-34/run-validation.py --check` at close commit
  `4a7aede`. Two honest outcome branches, both acceptable:
  - **reproduced-under-protocol:** the printed receipt equals the filed
    `reports/round-34/validation.json` legs (filed values at
    `reports/round-34/validation.json:5-30` for C/D and `:27-50` region for O/cross), wrong-tree
    observable passes;
  - **confirmed-could-not-reproduce:** the protocol itself shows the runner cannot be safely
    measured under isolation (e.g. the absolute-ROOT branch is unavailable on this host), with the
    failing step quoted. Either branch, with evidence, retires the c-n-r state for that row.
- **Successor ledger** (authored in the same fragment or a sibling JSON, schema
  `kotodama-recount-ledger-v1` successor): the four rows `R37-Ca-05..08` re-dispositioned as
  `reproduced-under-protocol` or `confirmed-could-not-reproduce`, each with owner + evidence path +
  the protocol section that produced it. Filed ledger bytes are never edited; this is a new
  append-only artifact under `reports/round-39/calib/`.

### 2.4 Ca03 — basename-couples policy (`reports/round-39/calib/Ca03-basename-policy.md`, fenced)

Must state exactly:
1. **Resolution order** (policy = the lane's established convention, restated as normative): entry
   directory → repo root → `corpus/knowledge/` → unique-basename fallback
   (`A12-gap-fill.md:9`; `reports/round-35/cov/C14-audit-6-10.md:239-288`).
2. **Fallback semantics:** fires only when direct path resolution failed **and** exactly one file in
   `corpus/knowledge/**` matches the basename; `.md` token extraction and one-level brace expansion
   as in the instrument; >1 match ⇒ ambiguous ⇒ **unresolved**, counted and surfaced — the fallback
   never guesses.
3. **Limits** (carry A12's boundary verbatim in spirit): the fallback establishes file existence and
   group alignment only, not content quality or absence of bleed (`A12-gap-fill.md:26`); the 15
   current basename refs are all in one field (`sacred-kingship-mythic-charter.md:37`) — the policy
   documents the state, it does not bless new basename shorthand as preferred style.
4. **Dispositions:** what an unresolved count means for an entry audit (blocker vs documented
   `(to-verify`), consistent with the runbook's pointer family (`C12-audit-runbook.md:37`).

### 2.5 Ca04 — verify (`reports/round-39/calib/Ca04-verify.md`)

Check Ca03's policy against (a) the actual resolver code paths (`reports/round-19/audit/
entry-audit.py:74-96` and the `C14-audit-6-10.md:239-288` recipe — do the code's real semantics
match the policy's claimed order/uniqueness rule?), and (b) A12's cross-check numbers (334/319/15,
0 ambiguous). Any disagreement is filed as a defect row with file:line, not smoothed over. A cheap
executable check: rerun the A12 probe shape read-only (token census + fallback matches) at HEAD and
confirm 15/0/0 still holds at `dfb0719` (it was measured at `57c8409`; r38 landed bytes since).

### 2.6 Thresholds (claim Ca acceptance, integrator-side)

- Protocol durable at `reports/round-39/calib/isolation-replay-protocol.md`; r34's runner
  replay-verified by the independent seat under it (claims.json thresholds); 4 rows re-dispositioned
  in the successor ledger with evidence; basename policy documented and verified.
- Zero filed byte edits anywhere; no `run-validation.py` executed in-tree ever (ABSOLUTE);
  `declared-in-r7` not re-frozen.

---

## Part 3 — Integration order + collision matrix (input to X00)

1. K01, K02 scouts → land gap topics (C) and isolation mechanics (Ca). P01 plans (this fragment)
   already carry the insertion points: §1.2 topic→slot map; §2.1 mechanics cross-check.
2. C01–C04 entries ∥ Ca01 protocol ∥ Ca03 policy (no shared paths).
3. C05 audit (needs 1–4 done) ∥ Ca02 replay (needs Ca01) ∥ Ca04 policy-verify (needs Ca03).
4. C06 README delta + receipt (needs C05 clean-or-defect-listed).
5. X00 collision matrix over the four slugs + all `out` paths (only shared path risk: none — every
   seat has a disjoint `out`; the C06 README delta is the single integrator-applied corpus touch).
6. R01 adversarial review (fabrication hunt on the 4 entries; protocol soundness vs §2.2 criteria).
7. S01 integration dossier (fleet-report material + validation-leg spec from all of the above).

Named hazards for X00: (i) slug collision C01–C04 → §1.2 guard; (ii) C06 topic-row byte-equality vs
late entry edits → entries freeze at C05 pass; (iii) Ca02 worktree creation writes `.git` admin
metadata (allowed — not filed bytes) and must clean up; (iv) no seat executes
`reports/round-39/run-validation.py` (ABSOLUTE) — the claim-Ca counting command is integrator-side.

## Owed

- K01: the 4 verification topics + sources → binds the §1.2 slot map (C01–C04 may start earlier via
  the self-derive rule; K01's landing supersedes slug choices only if it names the same slug
  differently, and any rename goes through the §1.2 re-slug registration).
- K02: O12 mechanics + r33-vs-r34/35 pattern → cross-check against §2.1; disagreements filed by K02
  in its own fragment (my §2.1 is read from the filed bytes directly, not from K02).
- Ca02: the actual replay outcome (reproduced vs confirmed-c-n-r) decides the successor ledger's
  four dispositions — my plan defines both branches and takes neither for granted.
- C06: the exact four filenames/topic lines for the delta rows (they exist only after C01–C04 land).

## Citations

- Round contract: `reports/round-39/claims.json:13-24` (C and Ca claims, counting commands,
  thresholds); `reports/round-39/targets.json:33` (P01 mission, out path); shared rules
  `reports/round-39/targets.json:4-9`.
- Coverage baseline: `ls corpus/knowledge/verification/*.md | wc -l` → 20; `python3 -B
  reports/round-28/readme/sweep.py` → exit 0, rows 212 = files 212, footer
  [21,23,25,29,20,94], `readme_sha256 b80274bc…` (run 2026-10-19, output quoted §1.1).
- README rev 2.1: `corpus/README.md:5-12`; carried defects: `corpus/README.md:1,3` (duplicated H1),
  `:14,16` (duplicated rev-2.0 line), queue rows `reports/round-37/op/defect-queue.json:103-131`.
- Entry contract: `reports/round-19/audit/entry-audit.py:25-27,74-96,106-133`;
  `reports/round-35/cov/C12-audit-runbook.md:26-44`; `reports/round-35/cov/C01-entry-1.md:8,32-38,40-47`;
  `corpus/QUALITY.md:3-20`; `reports/round-19/gaps.md:1-22`.
- O12 mechanics: `reports/round-34/run-validation.py:10,14,21-26`; `reports/round-35/run-validation.py:9`;
  `reports/round-33/run-validation.py:23`; `reports/round-38/scribe/S01-integration-draft.md:418-425`;
  defect row `reports/round-37/op/defect-queue.json:193-201`; r36 incident
  `reports/round-37/op/defect-queue.json:233-240`.
- r37 recount: 4 c-n-r rows `reports/round-37/calib/recount-ledger.json:60-111`, summary `:451-455`;
  Ca08 partial reproduction `reports/round-37/calib/Ca08-verify.md:27`; fleet-root leg precedent
  `reports/round-37/calib/recount-ledger.json:47-59`.
- Commit map: `git log --oneline -8` → `dfb0719` r38 close, `4a7aede` r34 close, `da68a6d` r33
  close (run 2026-10-19); r35 baseline-at-r34-close `reports/round-35/cov/C01-entry-1.md:6`.
- Basename fallback: queue row `reports/round-37/op/defect-queue.json:203-211`; A12 cross-check
  `reports/round-37/adj/A12-gap-fill.md:9-26,34-38`.
- Prediction-vs-delivery receipt rule: `reports/round-37/op/defect-queue.json:242-250`.
