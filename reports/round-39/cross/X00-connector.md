- Seat: X00 | connector (claim cross) | collision matrix + integration order | date 2026-10-19 | baseline dfb0719

# X00 — the collision matrix and the integration order

**Mission (binding, `reports/round-39/targets.json` seat `X00`):** "Collision matrix + integration
order." Out path: this file only.

**Write scope.** This file only. No corpus byte, tool, gate, pin, baseline, filed round-1..38 byte,
fleet `.ufo/**` byte, or `tools/gates/frozen/**` byte was written. No `reports/round-*/run-validation.py`
was executed in-tree (absolute rule; the only sweep run below is the round-28 read-only README
sweep, whose docstring and code path are read-only over `corpus/` — `reports/round-28/readme/sweep.py:28-30`).
No worktree, no bundle, no freeze, no commit, no push, no install, no network.

**Stamp.** `date -u +%FT%TZ` → **2026-10-19T12:04:50Z**; `git rev-parse HEAD` →
`dfb0719711204b5943432034bd80c8dc248acddd` (== the declared baseline `dfb0719`, the r38 admission
commit); `git status --porcelain` → `?? reports/round-39/` only. Every command ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Canon.** NON-CANON engineering evidence. This fragment certifies neither claim; it reports what
collides and in what order the drafts must land. Nothing here is round acceptance.

**Freshness of the matrix.** At this seat's write time only `claims.json`, `targets.json` and
`telemetry/dispatch-declared.json` existed under `reports/round-39/` — no sibling fragment had
landed. Every seat-level row below is therefore declared from `targets.json`/`claims.json` plus
filed precedent; when P01's plan and the executor fragments land, their explicit allocations
supersede the corresponding rows here. The integrator must re-run the §5.2 census against the
landed fragments, not against this file's predictions.

---

## 0. Verdict in one line

**All 16 out-paths are disjoint by construction — the round's real collisions are apply-time, and
there are exactly four:** (i) the C-block's four drafts converge on ONE corpus surface, where the
README revision-2.2 delta must be byte-equal to the entries' own `- topic:` text and filename-ordered
or the sweep reds; (ii) the Ca-block's replay collides with the filed r34 runner's absolute-root
`chdir` — the only demonstrated-safe mechanism is Ca08's `bwrap` bind-over, and `--check` does NOT
isolate (measurement happens before the check parse); (iii) both Ca `after_required` canonical paths
differ from the seat out paths, so each landing is an integrator digest-pinned copy; (iv) the r37
recount ledger is filed and immutable — the 4-row redisposition must land in a NEW successor file.

Baseline controls (all measured this seat, 2026-10-19T12:04Z):

```
verification partition : 20 files          ls corpus/knowledge/verification/*.md | wc -l
corpus total           : 212 files         find corpus/knowledge -name '*.md' | wc -l
README sweep           : GREEN             python3 -B reports/round-28/readme/sweep.py
  parts {"civilizations": 94, "culture-material": 25, "linguistics": 21, "myth-symbol": 23,
         "synthesis": 29, "verification": 20}; rows 212 files 212; 0 missing/ghost/mismatch/drift
  footer total 212, dir_totals [21, 23, 25, 29, 20, 94]; readme_sha256 b80274bc…
```

So claim C's declared before-state (verification 20, total 212, sweep green) is **confirmed live**,
and C06's target vector **21/23/25/29/24/94 is in the README's own section order**
(linguistics/myth-symbol/culture-material/synthesis/verification/civilizations —
`reports/round-28/readme/sweep.py:50-57`), i.e. only the fifth slot moves 20 → 24. No off-by-order
defect in the mission vector.

---

## 1. The write-scope matrix (16 seats)

Each seat writes exactly its own `out` path under `reports/round-39/` — **no seat-to-seat file
collision exists at wave time** (`targets.json:11-124`, every `out` distinct):

| seat | role | claim | out | upstream it reads (soft dep in a parallel wave) |
|---|---|---|---|---|
| K01 | scout | C | `scout/K01-verification-gaps.md` | corpus verification/synthesis partitions |
| K02 | scout | Ca | `scout/K02-isolation.md` | O12 mechanics, r37 ledger, r33/34/35 runners |
| P01 | planner | cross | `plan/P01-plan.md` | K01, K02 |
| C01–C04 | executor ×4 | C | `cov/C0N-entry-N.md` | K01 topic recommendations; P01 plan |
| C05 | verifier | C | `cov/C05-audit.md` | C01–C04 drafts |
| C06 | executor | C | `cov/C06-delta-receipt.md` | K01 topics + C01–C04 head-blocks (byte-equal topics) |
| Ca01 | executor | Ca | `calib/Ca01-protocol.md` | K02; Ca08/Ca02 r37 precedents |
| Ca02 | verifier | Ca | `calib/Ca02-replay-verify.md` | **Ca01's protocol** (it replays under it) |
| Ca03 | executor | Ca | `calib/Ca03-basename-policy.md` | K02; A12; the two resolver instruments |
| Ca04 | verifier | Ca | `calib/Ca04-verify.md` | **Ca03's draft** + resolver code |
| X00 | connector | cross | `cross/X00-connector.md` (this file) | targets/claims + filed precedent |
| R01 | reviewer | cross | `review/R01-review.md` | both blocks |
| S01 | scribe | cross | `scribe/S01-integration-draft.md` | everything |

Missing-dependency rule (AGENTS.md): a seat whose upstream fragment is absent at its read time does
what it can from `targets.json`/`claims.json` and records the owed path under `## Owed`. In a
single batched wave this is the expected path for C01–C04 (K01 may land mid-wave), for Ca02 (Ca01),
and for Ca04 (Ca03).

---

## 2. The apply-time collision matrix (draft → target surface)

No seat edits a live surface; the integrator applies. These are the only live surfaces the round
touches, and the controls each application must pass:

| # | fragment(s) | applied to | collision class | control before/while applying |
|---|---|---|---|---|
| 1 | C01–C04 fenced bytes | `corpus/knowledge/verification/<4 new names>.md` | **filename/topic allocation race** (X00-1); head-block contract drift | names unique vs each other AND vs the 20 existing entries; head-block carries `- topic:` / `- sources:` / `- couples:` / `- verified-at:` / `- recheck:` per the round-35/36 contract (sample: `corpus/knowledge/verification/to-verify-triage-protocol.md:1-7`); gap statement + decision record in body; C05's audit clean first |
| 2 | C06 delta | `corpus/README.md` (revision 2.2 block on top) | **byte-equality chain** (X00-3): `## verification/ (20)` → `(24)`; 4 rows in filename order; row text byte-equal to each entry's own `- topic:` (sweep `REWRITE` class otherwise, `sweep.py:136-148`); totals line 212 → 216; footer total 216 + vector `21/23/25/29/20/94` → `21/23/25/29/24/94`; footer date = re-measure date | single sweep AFTER entries+README both land (an intermediate sweep is expected red: entries-without-rows = 4 `missing_from_index`; rows-without-entries = 4 ghosts). Post-apply diff the landed README against the draft — the r35 apply left two `__E3_PLACEHOLDER__` lines behind and the r36 receipt's staged prediction diverged from the delivered digest (`r37 queue row readme-prediction-vs-delivery`); predict by staged-tree sha, cite the post-apply sweep |
| 3 | Ca01 | `reports/round-39/calib/isolation-replay-protocol.md` (claims.json `after_required` path) | **out-path ≠ canonical-path** | integrator copy of `calib/Ca01-protocol.md` bytes, digest pinned both sides in the landing record |
| 4 | Ca02 evidence | NEW successor ledger, e.g. `reports/round-39/calib/recount-ledger-successor.json` | **filed-byte immutability** (X00-5): `reports/round-37/calib/recount-ledger.json` (sha `73d2d48d…`) is filed; its 4 `could-not-reproduce` rows R37-Ca-05..08 keep their filed dispositions and gain a pointer to the successor, never an edit | successor file cites each r37 row id + the replay evidence path; name not declared in claims.json — integrator picks and records it |
| 5 | Ca03 | `reports/round-39/calib/basename-couples-policy.md` (claims.json `after_required` path) | same out-path ≠ canonical-path as #3; **scope trap** (X00-6): the "resolver" is two audit instruments, not a production tool | integrator copy, digest-pinned; Ca04's verification folded |
| 6 | integrator | `reports/round-39/run-validation.py` (new, close-time) | **does not exist yet**; claim Ca's counting command is close-time only | author it guard-adopted (r34 inventory discipline: `guarded-refresh` class per `tools/harness/receipt_guard_adoption.py`); NEVER executed in-tree — isolated copy only (r36 incident precedent, r37 queue row `r36-in-tree-runner-incident`) |

**Filed-byte red lines (shared_rules + claims non_goals):** `reports/round-1..38/**`,
`corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**` — zero byte moves. `NO re-freeze of
reports/round-34/handoff/declared-in-r7`. Nothing in this round's plan requires any of them: the C
block only ADDS corpus files + one README revision; the Ca block only adds round-39 files.

**Cross-block coupling (the one genuine C↔Ca interaction):** the 4 new verification entries carry
`- couples:` references, which enter exactly the reference-resolution surface that Ca03's policy
document governs (resolution order entry dir → repo root → `corpus/knowledge/` → unique-basename
fallback — A12's measured semantics). Consequence, not blocker: the entries' refs should be
path-resolvable or uniquely-basenames so they need no fallback, and Ca03's policy should state the
fallback's limits in terms that cover future entries, not just the r35/r36 eleven.

---

## 3. The r34-replay collision — the round's hardest surface (X00-2)

Claim Ca(b) redispositions r37 ledger rows **R37-Ca-05/06/07/08** (all four =
`python3 reports/round-34/run-validation.py`, groups C/D/O/cross, owner Ca02,
`reports/round-37/calib/recount-ledger.json:62-111`; summary 25 match / 5 mismatch / 4 c-n-r,
`:451-455`). The mechanics the protocol (Ca01) and the replay (Ca02) must respect, all verified
this seat:

```
reports/round-34/run-validation.py:10,26   absolute live-checkout ROOT + unconditional os.chdir(ROOT)
:4-6    modes: default = measure + guard receipt; --check prints, never publishes
:514-517 guard_receipt() runpy's tools/harness/receipt_guard.py (runner class: guarded-refresh)
:522-531 --check parsed AFTER measure() — the full measurement runs BEFORE the check flag is read
:532-538 default path guards then writes validation.json
live sha256 == filed runner_sha256 (validation.json:196): be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9  ✓
r34 close commit: 4a7aede22cd8395b01ce6dd9f46bcae364ca24e4 ("round-34: admit D/O/C …")
```

Three consequences the protocol must carry, each already measured in filed precedent:

1. **`--check` does not isolate.** Because `chdir(ROOT)` precedes flag parsing, an unmodified
   `--check` invocation from a worktree/archive copy measures the LIVE checkout, not the copy
   (Ca02-r34:18; Ca08:25). A worktree at the close commit binds the OBJECTS, not the PATH — the
   protocol needs a path-binding mechanism on top.
2. **The only demonstrated-safe mechanism is Ca08's namespace bind-over** (`Ca08-verify.md:23-27`):
   `bwrap --unshare-all` with the close-commit checkout bind-mounted OVER the runner's hardcoded
   checkout path, sibling `.ufo` empty-mounted, `MANIFEST.json` masked with `/dev/null`; unmodified
   runner source; `--check` mode. It reproduced r34 C/D exactly. **`bwrap` is present on this host**
   (`/usr/bin/bwrap`, checked 2026-10-19T12:04Z), so the protocol is feasible — and it must specify
   the two masks (`.ufo`, `MANIFEST.json`) or the cross row cannot pass (fleet inputs absent).
   Plain archive + `GIT_CEILING_DIRECTORIES` was measured INSUFFICIENT (rev-parse still returned
   the live root, `Ca08-verify.md:25`).
3. **Source-redirected diagnostics do not count** (Ca02-r34:20 — its altered-ROOT run was excluded
   from the recount; P01's r37 plan forbade runner patching). Ca02 in r39 must replay unmodified
   bytes under the Ca01 protocol or file `confirmed-could-not-reproduce` with owner — either
   disposition satisfies claim Ca(b) as declared (`claims.json:19-24`: "reproduced-under-protocol
   **or** confirmed-could-not-reproduce with owner").

Coverage honesty carried forward: Ca08 reproduced only C/D; **r34 O/cross have never been safely
replayed** (`Ca08-verify.md:27,32`) — that is the exact hole Ca02's r39 run closes if the protocol
works. The queue's canonical id for the hazard is **`O12-runner-isolation-hazard`** (owner "future
integrate round", next touch "runner cwd-hardening pass", `reports/round-37/op/defect-queue.json:192-201`);
`R36-ABSOLUTE-ROOT` is its census alias, and r37's review directed O08/O12 to merge as ONE candidate
(`R07-cross-review.md:13`) — the protocol and the successor ledger must cite the single id, not mint
a third (X00-4).

---

## 4. The basename-couples policy surface (X00-6)

The r37 queue item (`defect-queue.json:202-211`): "couples resolver leaves 15 basename-only
references unresolved; a working unique-basename fallback exists but is undocumented policy" — next
touch "document or fix the resolver". Verified scope facts for Ca03/Ca04 so the policy lands against
the real code, not a imagined tool:

- The "resolver" is the **audit-instrument resolution order** in `reports/round-35/cov/C14-audit-6-10.md:239-288`
  and `reports/round-19/audit/entry-audit.py:74-96` — entry directory, repo root, then
  `corpus/knowledge/`, then a unique-basename fallback. There is no production resolver module.
- A12's independent cross-check measured: 334 distinct per-entry reference tokens = 319
  path-resolved + 15 basename-shorthand; 0 ambiguous, 0 unresolved; the 15 all originate from
  `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`, and each mapped to its
  declared partition (`reports/round-37/adj/A12-gap-fill.md:9-26`). "Document as policy" therefore
  means: codify this order + the fallback's uniqueness-and-group-alignment limits + its
  non-guarantees (existence and group alignment only, never content quality).

---

## 5. Integration order

### 5.1 The sequence (owner-tagged; why-here is load-bearing where marked)

| # | step | owner | why here |
|---|---|---|---|
| 1 | wave runs in parallel; scouts (K01/K02) land first where possible | seats | executors fall back to targets/claims on absence (AGENTS.md missing-dependency) |
| 2 | seat census: 16/16 outs present; each header = seat/role/claim/`date 2026-10-19`/`baseline dfb0719`; fenced blocks well-formed | integrator | a malformed header poisons every later digest citation |
| 3 | **C-block first:** apply the 4 entries after C05's audit is clean; pre-check filename+topic uniqueness vs each other and vs the 20 existing entries (X00-1) | integrator | entries-before-README keeps the corpus never-worse-than-baseline if step 4 must be re-rolled |
| 4 | apply C06's README revision 2.2 delta (header 24, 4 filename-ordered byte-equal rows, totals 216, footer 216 + `21/23/25/29/24/94`, new revision block, footer date = today) | integrator | must land in the same motion as #3 or the tree sits in an intermediate red state |
| 5 | `python3 -B reports/round-28/readme/sweep.py` → must be green at 216/216; `ls corpus/knowledge/verification/*.md | wc -l` → 24; diff landed README vs C06 draft (X00-3) | integrator | claim C's thresholds; the r35 placeholder lesson says verify the LANDED bytes |
| 6 | **Ca-block (independent of 3–5):** copy Ca01 → `calib/isolation-replay-protocol.md`, Ca03 → `calib/basename-couples-policy.md`; pin both digests | integrator | after_required canonical paths; no mechanical dependency on the corpus moves |
| 7 | fold Ca02's replay evidence into the NEW successor ledger redispositioning R37-Ca-05..08 (reproduced-under-protocol or confirmed-c-n-r with owner); fold Ca04's verification of Ca03 | integrator | claim Ca(b); filed r37 ledger untouched (X00-5) |
| 8 | disposition R01's findings: fixed-with-evidence or routed-with-owner, never absorbed | integrator | regimen per-round contract |
| 9 | author `reports/round-39/run-validation.py` (guard-adopted) and run it in an ISOLATED copy only; close-time: SCORECARD row, LOG append (lane identity), MANIFEST rounds[], fleet report | integrator | claim Ca's counting command is close-time only; absolute in-tree rule |
| 10 | file the telemetry CLOSING snapshot for `telemetry/dispatch-declared.json` (currently `open-at-seat-close`) as a NEW file citing the original's sha256 `1b21ed5b…` at close | integrator | AGENTS.md close-what-you-open; the round is not admitted while the snapshot is owed |

Order within {3–5} vs {6–7} is free (the blocks share no surface); 3 before 4 before 5 is NOT free —
that sequence is what keeps the sweep's only red moment inside a single landing.

### 5.2 The census re-check the integrator owes this matrix

When the fragments land: confirm C01–C04's four chosen topics are disjoint and disjoint from the 20
existing entries (`Glob`/`ls` + a topic grep); confirm Ca02 actually used the Ca01 protocol (not an
improvised redirect); confirm C06's rows carry the entries' byte-equal `- topic:` text. Any deviation
supersedes this file's §2 predictions — record it, don't reconcile to it.

---

## 6. Named findings

**X00-1 (blocking for the C-block apply) — topic/filename allocation is a race by default.**
C01–C04's missions say "author entry N" with no topic binding; K01 recommends four topics but cannot
enforce allocation from a parallel seat. If two seats pick one topic, the drafts collide only at
apply time (distinct out paths hide it), and the sweep cannot catch cross-entry topic duplication at
all. Control: the integrator's pre-apply uniqueness check (§5 step 3), plus K01's recommendations as
the allocator of record. Owner: integrator.

**X00-2 (the round's core hazard) — a git worktree alone does NOT satisfy the replay's isolation
requirement.** The r34 runner chdirs to its absolute ROOT before parsing `--check`
(`run-validation.py:26,526-527`), so a worktree replay without path binding measures the live tree.
The protocol must compose worktree-at-close-commit (objects) with a path bind-over (bwrap, present
on this host) plus the `.ufo`/`MANIFEST.json` masks Ca08 used. Anything less reproduces Ca02's r37
`could-not-reproduce` for the wrong reason. Owner: Ca01/Ca02; the protocol document is the artifact
of record.

**X00-3 (repeat of a filed lesson) — the README delta must be verified on the LANDED bytes.** The
r35 apply left two `__E3_PLACEHOLDER__` lines that the sweep then caught, and the r36 receipt's
staged prediction diverged from the delivered digest (queue row `readme-prediction-vs-delivery`,
`defect-queue.json:242-251`). C06's receipt should predict by staged-tree sha and cite the
post-apply sweep; the integrator diffs the landed README against the draft before the sweep.

**X00-4 (dedupe directive carried) — the O12 hazard has ONE canonical queue id.** r37's review
directed O08/O12 to merge as a single candidate (`R07-cross-review.md:13`); the queue landed it as
`O12-runner-isolation-hazard` with `R36-ABSOLUTE-ROOT` as census alias. Ca01's protocol and the
successor ledger must reference the canonical id; a third row would regress the r37 dedupe.

**X00-5 (immutability) — the r37 recount ledger is filed; the redisposition is a successor file.**
`reports/round-37/calib/recount-ledger.json` (sha `73d2d48d…`) keeps its 4 c-n-r rows as filed;
the successor cites them by id and carries the new dispositions with evidence. Same pattern as
every prior supersession: new rows, never edits.

**X00-6 (scope) — "the resolver" is two audit instruments, not a module.** Ca03 documents the
instrument resolution order + fallback semantics (§4); Ca04 verifies against
`C14-audit-6-10.md:239-288` + `entry-audit.py:74-96` and A12's cross-check — not against a
production tool that does not exist. Recording this prevents both seats from hunting for (or
inventing) one.

**X00-7 (do-not-touch note) — `corpus/README.md` carries a duplicated H1** (lines 1 and 3, both
`# kotodama-shokunin corpus index`), pre-existing and sweep-blind (the sweep checks sections/rows/
totals/footer, not headings). It is NOT this round's defect and must not be silently "fixed" inside
the revision-2.2 delta — that would be an unscoped filed-surface edit. If the integrator wants it
repaired, it is a separate recorded act.

---

## Owed

- **P01's plan + the executor fragments** were absent at this seat's write (12:04:50Z); §2's
  allocation rows are predictions pending their landed allocations (§5.2 census). Owner: integrator.
- **r34 O/cross safe replay** has never been demonstrated (Ca08 covered C/D only) — Ca02's r39 run
  is the first chance; if the protocol cannot pass the fleet masks, those two rows land
  `confirmed-could-not-reproduce` with owner, which still satisfies claim Ca(b). Owner: Ca02.
- **`reports/round-39/run-validation.py`** does not exist at seat time; both claims' threshold
  commands are close-time only and `to-verify` until then (per F-C13-1 it must never run in-tree).
- **Successor-ledger filename** is undeclared in claims.json — integrator picks and records (§2 #4).
- **This fragment certifies neither claim.** Claim C's after-state (24/216, sweep green) and claim
  Ca's after-state (protocol + redisposition + policy, replay-verified) exist only when the
  integrator's close-time records say so.

## Citations

**Baseline and digests (measured 2026-10-19T12:04Z, lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`):**

```
dfb0719711204b5943432034bd80c8dc248acddd                          git rev-parse HEAD (== declared baseline dfb0719)
?? reports/round-39/                                              git status --porcelain (entirety)
20                                                                ls corpus/knowledge/verification/*.md | wc -l
212                                                               find corpus/knowledge -name '*.md' | wc -l
sweep exit 0: rows 212 files 212, 0 missing/ghost/mismatch/drift, footer_ok True
  parts {civ 94, cm 25, ling 21, ms 23, synth 29, verif 20}; footer [21,23,25,29,20,94] total 212
b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74  corpus/README.md (via sweep readme_sha256)
73d2d48d6b6f902802503371dae9e9b60cd3bf0190a71518ed7ec0713d5f4b22  reports/round-37/calib/recount-ledger.json
5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d  reports/round-37/op/defect-queue.json
1b21ed5b6c45db7b05f020c89450a325eb95327daef1542ff996f7bf279308a5  reports/round-39/telemetry/dispatch-declared.json
be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9  reports/round-34/run-validation.py
  == filed runner_sha256 at reports/round-34/validation.json:196  (cross-check green)
4a7aede22cd8395b01ce6dd9f46bcae364ca24e4                          r34 close commit (git log --format='%H %s' -1 4a7aede)
/usr/bin/bwrap ; /usr/bin/unshare                                 command -v … (Ca08 mechanism feasible here)
```

**Commands run:** `date -u +%FT%TZ`; `git rev-parse HEAD`; `git status --porcelain`;
`ls corpus/knowledge/verification/*.md | wc -l`; `find corpus/knowledge -name '*.md' | wc -l`;
`python3 -B reports/round-28/readme/sweep.py` (read-only, exit 0);
`grep -n -A2 "Counts checked" corpus/README.md | tail -6` (footer at `corpus/README.md:507-509`);
`command -v bwrap unshare`; `git bundle --version`; `sha256sum` over the four files above;
`grep -n runner_sha256 reports/round-34/validation.json`; `git log --format='%H %s' -1 4a7aede`.
No file outside this fragment was created or modified.

**Source lines cited:** `reports/round-39/targets.json:4-9` (shared_rules), `:104-109` (seat X00);
`reports/round-39/claims.json:12-18` (claim C), `:19-24` (claim Ca), `:26-27` (non_goals);
`corpus/README.md:5-11` (revision 2.1 block), `:507-509` (counts footer), `:1,3` (duplicated H1);
`reports/round-28/readme/sweep.py:28-30` (read-only contract), `:50-57` (PARTS order), `:59-71`
(row/topic/totals/footer regexes), `:119-212` (sweep legs incl. REWRITE class and FOOTER_*), `:191-194`
(ok condition); `reports/round-34/run-validation.py:4-6,10,26,514-517,522-538`;
`reports/round-34/validation.json:196`; `reports/round-37/calib/recount-ledger.json:62-111,451-455`;
`reports/round-37/calib/Ca02-r34.md:18,20,24,36`; `reports/round-37/calib/Ca08-verify.md:23-27,32`;
`reports/round-37/op/defect-queue.json:192-201` (O12), `:202-211` (basename), `:242-251`
(readme-prediction-vs-delivery); `reports/round-37/adj/A12-gap-fill.md:9-26,30`;
`reports/round-37/review/R07-cross-review.md:13`; `reports/round-37/review/R08-conformance.md:9-13`;
`reports/round-35/cov/C14-audit-6-10.md:239-288`; `reports/round-19/audit/entry-audit.py:74-96`;
`corpus/knowledge/verification/to-verify-triage-protocol.md:1-7` (head-block contract sample);
`AGENTS.md` ("Close what you open" section); `SCORECARD.md:681-684` (r37 integration repairs: the
r35 `__E3_PLACEHOLDER__` root cause).

**Peer inputs read, not absorbed:** `reports/round-38/cross/X00-connector.md` (format precedent);
`reports/round-37/calib/recount-ledger.json`, `op/defect-queue.json`, `calib/Ca02-r34.md`,
`calib/Ca08-verify.md`, `adj/A12-gap-fill.md`, `review/R07-cross-review.md`,
`review/R08-conformance.md`; `reports/round-39/claims.json`, `targets.json`,
`telemetry/dispatch-declared.json`.
