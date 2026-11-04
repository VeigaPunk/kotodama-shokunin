# ScoutProtocol — kotodama round-88 scoped findings

Seat: ScoutProtocol (scout, axes operability + depth, milestone r88-v1).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Frozen reads only: claims `4b76524c51e1c2f76c99eeb3b629cfac08a44a76`, base
`4956282281dac1306cfbe59523e46dde99749d75`, pre-dispatch controls
`0c8c733088df8c4f06770c9e714360eed7f29272`.
Counter read: `reports/round-88/measure88.py`, sha256
`5a80a4398468710338b39928d44b5aae3a7366d94767b06dd78eabce0bd995e7` (identical to the
sha256 recorded in every pre-freeze receipt: `no-work-o.json`, `no-work-d.json`,
`pre-dispatch.json`).

No production file was edited. No frozen predicate, counter, case list or control was
amended. No git/jj mutation was performed on the lane. Every probe ran against copies
in scratch.

Scratch: `/fast/scratch/hyaku/kotodama-r88/ScoutProtocol/` (receipts copied into
`.ufo/waves/round-88/w1/stage/ScoutProtocol/receipts/` before scratch teardown).
Tool installs: none — no pacman transaction, no uv/npx/binary install was needed.

---

## 1. Headline: the frozen O counter's battery-agreement leg is satisfiable by a battery that analyses nothing

**Severity: high. This is a live kill-rule gap, not a stylistic one.**

`measure88.py:claim_o` computes the four counterfeit class counts itself
(`score:constant-pass`, `score:shotgun-all-labels`, `score:extra-id`,
`score:filename-only`) by running `evaluate()` directly on each committed control.
The candidate battery is consulted in exactly one place — the `battery-agrees` leg
(`measure88.py:196-208`) — and only for **two** labels:

```python
for label in ('honest', 'shotgun-all-labels'):
    ...
    agree.append(body.get('passed'))
legs.append(leg('battery-agrees', [EXPECT['honest'], EXPECT['shotgun-all-labels']], agree))
```

The number compared is `body.get('passed')` out of the **battery's own JSON**, i.e. a
self-report. The three counterfeits the kill_rule names explicitly
(`constant-pass 3`, `extra-id 4`, `filename-only 0`) are never asked of the battery at
all.

**Observed.** Built a synthetic two-revision repo carrying the real frozen
`cases.json`, the real `check-attestation-packet.py` and the four committed
counterfeits, plus a battery that never reads a packet and self-reports
`13` for every candidate except `shotgun-all-labels` (`4`). That battery therefore
**accepts the constant-pass counterfeIt, extra-id and filename-only at 13/13**.

```
python3 -B reports/round-88/measure88.py --root <synth> --base <b> --lands <l> --claim O --work <w>
rc = 0 ; passed/total = 9/9
  battery-absent-at-base   exp=True          obs=True  pass=True
  battery-present-at-lands exp=True          obs=True  pass=True
  score:honest             exp=13            obs=13    pass=True
  score:constant-pass      exp=3             obs=3     pass=True
  score:shotgun-all-labels exp=4             obs=4     pass=True
  score:extra-id           exp=4             obs=4     pass=True
  score:filename-only      exp=0             obs=0     pass=True
  battery-selftest:exit    exp=0             obs=0     pass=True
  battery-agrees           exp=[13, 4]       obs=[13,4] pass=True
```

**Consequence.** `claims.json` O reads: *"the frozen 13-case battery scores the
committed honest auditor 13/13 while the four committed counterfeits score exactly
constant-pass 3, shotgun-all-labels 4, extra-id 4 and filename-only 0."* The kill_rule
reads: *"a comparator that accepts a counterfeit cannot reach the frozen per-class
counts."* As frozen, a comparator that accepts three of the four counterfeits at
13/13 **reaches claim O**. The `score:*` legs are unaffected by the candidate (they
measure the counter against its own controls) and therefore cannot detect this.

The single check that *does* bite (`shotgun-all-labels` = 4) is satisfied by a
constant in the self-report. A second degenerate battery that self-reports `13` for
`honest` and `4` for `shotgun-all-labels` and nothing else also reaches 9/9.

**Recommendation for L1 (no frozen amendment):** the lands comparator
`tools/check-finding-sets.py` should be graded by a *separate* instrument that asks
the battery for its per-class counts, or L1 should record the O claim's
discrimination as bounded to "the counter's own comparison layer rejects the four
committed counterfeits" and not as "the battery rejects them". The battery-agrees leg
as frozen does not establish the latter.

---

## 2. The frozen counter's `--selftest` is a false green (already independently found)

**Severity: high for operability evidence; the frozen instrument stays unchanged.**

`reports/round-88/counter-selftest.json` records `--selftest` rc 0 with three checks
`passed: true`. That receipt is not evidence of a working comparison layer.

**Observed, independently.**

- **Transport.** `report_partial_tool()` (`measure88.py:262-266`) writes
  `pathlib.Path("<the JSON body>").read_text()` — the body is used as a **pathname**.
  The `exact-accepted` child exits 1 with
  `FileNotFoundError: ... '{"records": 6, "findings": ...}'`. The nominal positive
  fixture never emits a report; it crashes.
- **Logic.** `checks.append(dict(case=name, passed=(not ok) if wanted is False else True))`
  (`measure88.py:257`). For `exact-accepted` the flag is `False`, so the check asserts
  `not ok` — it asserts that a *correct* report is **rejected**. For
  `extra-id-refused` the flag is `True`, so the branch yields `True` unconditionally
  — it never reads the observed comparison result.
- **Mutation.** Three mutants of the comparison layer were written into scratch and
  the frozen selftest run against each:

  | mutant | `--selftest` rc | survives? |
  |---|---|---|
  | `ok = False` (always reject) | 0 | **yes** |
  | `ok = True` (always accept) | 0 | **yes** |
  | membership-only `set(expected).issubset(ids)` | 0 | **yes** |

  All three survive with rc 0. The selftest cannot detect a comparison layer that
  rejects everything, accepts everything, or degrades to membership-only — the exact
  failure modes the round exists to exclude.

This corroborates the sibling receipt `reports/round-88/counter-selftest-false-green.json`
and `reports/round-88/probe-counter-selftest.py`, and `corpus/QUALITY.md` criterion 35
(binding from round 89) already names it. The frozen `measure88.py` and its original
selftest receipt are unchanged, as required.

**Note for the D lane (a real risk, not yet a defect):** `claim_d` calls no
subprocess and runs no census (verified by source inspection: `subprocess` does not
appear in the `claim_d` body). Yet `claims.json` D's kill_rule reads *"A registry row
without the phenomenon checked by check-sources-census is not admitted."* **No
`check-sources-census` tool exists anywhere in the fleet** — the only match for that
string is the kill_rule itself. The real census instrument is
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (validate mode, rc 0, 854
rows at the base revision). The frozen D counter checks tier/status **text** in
`corpus/SOURCES.md` only; it never verifies the phenomenon was actually checked. The
kill_rule names an instrument the counter does not run.

---

## 3. `materialize()` can grade WORKTREE bytes under a revision label

**Severity: medium.**

The module docstring (`measure88.py:4-5`) states: *"It grades committed bytes at a
named revision; it never grades the worktree."* `materialize()` (`measure88.py:126-136`)
falls back to `pathlib.Path(root)/path` whenever `git show rev:path` fails:

```python
raw = blob(root, rev, path)
if raw is None:
    local = pathlib.Path(root) / path
    raw = local.read_bytes() if local.is_file() else None
```

**Observed.** A control file present only in the worktree, absent from the named
revision, was materialized and returned with its worktree bytes intact; the receipt
would still carry `revision=<lands>`. The comment inside the function acknowledges
this is meant for pre-freeze runs, but the code applies the same fallback to the
graded runs.

**Consequence.** `cases_raw` in `claim_o` has the same shape:
`blob(root, lands, CASES) or blob(root, base, CASES) or <worktree file>`. A grader
pointed at a revision whose `cases.json` is missing silently grades a *worktree* case
list under a revision label. `cases_raw` is also not pinned by hash in the leg list —
`case_list_sha256` is recorded in the receipt but no leg compares it to a frozen value,
so a substituted case list would be reported rather than rejected.

**Recommendation.** L1 should verify at lands time that the receipt's
`case_list_sha256` equals the sha of the committed `reports/round-88/cases.json` at
`4b76524c`, since no leg does it.

---

## 4. The D predicate's surface legs are weakly binding (concrete, reproducible)

**Severity: medium. These are *weaknesses in the frozen counter*, i.e. the D claim can
be satisfied more cheaply than its prose implies. They are not counterfeits of the
honest artifact.**

All measurements are against `claim_d`'s own leg arithmetic, reproduced in scratch.

| # | construction | measured | why it matters |
|---|---|---|---|
| D-a | two tables of 2 data rows each inside the section | `data_rows=5` | rows are summed **across tables**; the second table's *header* is counted as a data row (`len(rows)-1` assumes one table). Only **4** real data rows are needed. |
| D-b | S931/S932/S933 mentioned in prose, **no table row cites them** | `cited=3` | `new-rows-cited` is `re.search` over the whole section text. The claim says the section *"cites at least 3 of S931, S932, S933"*; the counter accepts a prose sentence. |
| D-c | 2-column table, one cell contains a literal `\|` | `columns=3` | `columns` counts literal `"\|"` characters, so an escaped pipe inside a cell inflates the count past the ≥3 threshold. |
| D-d | 2500 bytes of filler placed in a **different section** | `growth=2707` | `growth-bytes` measures the **whole file** delta, not the section's. Zero growth inside `4b` still satisfies the leg. |
| D-e | heading text appears twice (e.g. a TOC entry) | `count=2` | `heading-present-at-lands` expects exactly `1`; any second mention (TOC, cross-reference) **fails** the leg. This is the one place the counter is *stricter* than the prose. |

**Recommendation.** The honest artifact should still be a genuine ≥5-row, ≥3-column
table with per-row S-id citations inside the `4b` section — the weakness does not
justify a cheap landing, and QUALITY 34's own wording ("Check actual affected record
IDs and permitted findings") points the same way. L1 should record that D's numeric
legs are satisfiable by the constructions above, so the D verdict rests on the
artifact's substance plus the ≥2500-byte growth, not on the counter's arithmetic
alone.

---

## 5. The frozen claim-D counter command is not runnable as written

**Severity: medium (documentation-level; blocks a naive verifier run).**

`claims.json` claim D `counter`:

```
python3 -B reports/round-88/measure88.py --root . --base 4956282281dac1306cfbe59523e46dde99749d75 --lands <lands> --claim D
```

`measure88.py`'s argparse declares `--work` as `required=True`
(`measure88.py:270`), and `main()` returns 2 with `MEASURE88_ERROR work must exist`
if it is absent. Running the frozen command verbatim:

```
rc = 2
stderr: measure88.py: error: the following arguments are required: --work
```

The claim-O command in the same file *does* include `--work <existing-dir>`, so this is
an inconsistency inside one frozen artifact. Adding `--work <existing-dir>` to the
claim-D command makes it run (verified: rc 1 at the base revision, i.e. the expected
red). The frozen claim text must not be amended by this seat; L1 should treat the
missing `--work` as a known invocation defect and record the working invocation
(`--work <existing-dir>`) alongside it.

---

## 6. Pre-freeze ordering: the controls were frozen correctly

**No ordering defect found.** Recorded as a positive finding with evidence.

- `reports/round-88/cases.json`, all four `reports/round-88/controls/*.py`,
  `pre-dispatch.py` and `pre-dispatch.json` landed together at
  `0c8c733088df8c4f06770c9e714360eed7f29272` — the **pre-freeze** commit.
- `claims.json` and `measure88.py` landed afterwards at `4b76524c51e1c2f76c99eeb3b629cfac08a44a76`.
- `git show base:tools/check-finding-sets.py` → rc 128 (absent), confirming the
  comparator's "before" state.
- The counter's sha256 in `no-work-o.json`, `no-work-d.json` and `pre-dispatch.json`
  equals the sha256 of the committed `measure88.py`, so the counter that produced the
  pre-freeze receipts is byte-identical to the frozen one.
- The pre-freeze receipt records the inherited r87 counter accepting
  `shotgun-all-labels` 12/12, `extra-id` 12/12, `filename-only` 12/12 and
  `constant-pass` 3/12 (`pre-dispatch.json.inherited_r87_counter`), which is the
  red-before the O claim needs.
- `reports/round-88/cases.json` note states expectations derive from the committed
  r87 `case_contract` in `reports/round-87/claims.json`, not from any candidate's
  output. Spot-checked: the 8 label semantics in the r87 `case_contract` map 1:1 onto
  the r88 case labels; the per-case record ids (`R86-CRAFT-01`…`R86-CRAFT-06`) are
  index-derivable from the committed r86 packet (`records[i].id`), not from any tool
  output.

---

## 7. Stale untracked round-79 result attribution — located, preserved, not removed

**Severity: low (hygiene). Left in place as instructed.**

- `kotodama-shokunin/.ufo/waves/round-79/w1-results.json` is **untracked**
  (`git status` → `?? .ufo/waves/round-79/w1-results.json`; `git log --all --` on the
  path → no commit). The rest of `round-79/` is tracked and landed at `efdc19e5`
  (*"round wrap-up (run 12): land wave/seat evidence left uncommitted at honest stop"*).
- It is **stale in attribution**: its 32 seat names match the round-79
  `w1/swarm-registry.json` exactly (registry ∩ results = 32/32, both directions), but
  its mtime is **2026-11-04 15:31:50** — i.e. written ~2 hours before this round's
  dispatch — while every round-79 seat report file dates from 2026-10-30 12:15–13:16.
  The file was regenerated after the wave, not produced by it.
- Its note string is **byte-identical** to the round-87 file's note
  (both sha256 `12715cbb217197a9…`): *"orchestrator kernel restarted mid-wave; seat
  output was delivered to the orchestrator session but not retained — read the seat
  report file in the wave dir"*. Two named seats, `ScribeClaims` and
  `ScribeCorrection`, have **no** report file in `round-79/w1/` (30 `.md` for 32
  registry members), so their note points at a file that does not exist.
- All 32 `output` values are `null`, matching the round-87 and round-73 pattern
  (rounds 74–77 have zero nulls), so the shape is the lane's established
  kernel-restart artifact — but for round 79 there is no dispatch-side record of a
  kernel restart (`w1-dispatch.json` contains no "kernel" mention).

**Not removed.** Flagged so L1 can decide whether to commit it as-is with a dated
attribution note, or leave it untracked. Note the same lane pattern at
`.ufo/waves/round-87/w1-results.json` (tracked, 10/10 null, same note) and
`.ufo/waves/round-73/w1/w1-results.json` (tracked, 37/37 null, same note).

---

## 8. `considerthese` and assimilation duty status

- **No `considerthese/` directory exists for this lane**: absent at
  `kotodama-shokunin/considerthese/`, at the fleet root
  `/home/vgpnk/Projects/shokunin/considerthese/`, and in the lane's own long-standing
  record (lane `LOG.md` rounds 68–75 each record *"`considerthese/` absent for this
  lane (recorded)"*). The `considerthese` grep across the fleet root returns only
  other lanes' prompts and the `shokunin` goal files. The goal file
  `.scratch/goal-20261025-hyaku-run7.md:34` lists kotodama among *"Lanes without
  considerthese: tabi, souji, kaidoku, kotodama"*.
- **Assimilation is a standing §10 duty** and *can* be discharged here: the shokuknow
  staging package exists at `/home/vgpnk/Projects/shokuknow/merge/kotodama/`
  (`MERGE-REPORT.json`: lane kotodama, accepted 132, refused 0, first_id S859;
  `SOURCES.append.md` 132 rows spanning **S859–S990**; plus `knowledge/` and
  `amendments/` trees). The lane has adopted from it before (round 72 heritage-taxonomy
  theme, rounds 73–75).
- **Obstacle to any adoption this round, and a live hazard for D's ids:**
  **all 132 staged ids collide with the current registry** (`S859`–`S930` are already
  taken; the registry's max id is `S930`). Staged `S931`, `S932`, `S933` — the exact
  ids `claims.json` D reserves for the numeral-notation rows — are already inside the
  staged range. Adopting the package as-is would double-book `S931`–`S933`.
  The lane's own history names the mechanism: round 71 filed a renumber map
  (`S874`→`S1005` by document) and round 72/73 re-pointed staged rows by document;
  round 71's map is flagged stale and needs regeneration against the current registry.
- **Recommendation.** `claims.json` D reserves S931–S933 and the r88 D claim is a
  knowledge-deepening claim on a different axis theme. A shokuknow adoption would
  need a fresh by-document renumber of 132 staged ids to continue from `S934`+ and a
  collision guard, which is a campaign-scale task the r88 claim does not size. The
  honest disposition is `assimilation: none` **with the collision fact stated** — not
  a bare "none". The lane has precedent for exactly that phrasing
  (`LOG.md:4609,4652`: *"Assimilation: none — no `merge/kotodama/` theme fits this
  round's claims"*).

---

## 9. Lowest-axis numeric debt and the planner-policy conflict

**Lowest axis.** `claims.json` says: *"Freshness remains historically the lowest
non-retired axis and stays paused under the open round-11 L0 question; the R86-C1
numeric-mapping debt stands. No waiver and no invented 0-10 score is asserted."*
Verified:

- The round-11 L0 question is live and unanswered. Fleet `.ufo/l0-questions.md:47`:
  *"kotodama | round-11 | drift-recheck threshold calibration: the declared >=95%
  24h hash-stability threshold failed at 0.778 purely because build rounds 10/11
  legitimately changed the tree (all 45 drifts dispositioned) … Freshness axis-move
  claims are paused until ruled."* Grep for an `L0 ANSWER` on that row → **0**.
- R86-C1 is recorded in the lane's own SCORECARD (`SCORECARD.md:1877`): *"No invented
  0–10 delta or lowest-axis waiver. Freshness remains historically lowest and paused
  under round11's open L0 threshold question; R86-C1's numeric/lowest-axis
  conformance debt and the L2-planner conflict remain."*
- `claims.json` `unchanged: [coverage, freshness, calibration, adjacency]` is
  consistent with the SCORECARD's row set. **The lowest-axis statement is honest and
  correctly hedged.** No numeric 0–10 score is asserted anywhere in the r88 claims.
  The debt is a standing disclosure, not a new r88 defect.

**Planner-policy conflict.** `claims.json` D/`unchanged` do not mention it, but the
round-88 context states *"L1 holds planner seat; formal planner-policy conflict
retained."* Verified:

- The canonical conflict is open at fleet `.ufo/l0-questions.md:295`:
  *"kotodama | round-86 | R85-C7 planner split conflict: canonical minimum names an L2
  planner but the round prompt and wave validator prohibit planner as a swarm role and
  assign it to L1. Same unresolved question as kake round-86 D84-4: authorize this
  mapping or change the policy. This round retains L1 planning and a scout data-walk,
  discloses the conflict, and does not claim an exception or full role-split
  conformance."* — **no answer recorded**.
- The r88 wave is consistent with the disclosed mitigation:
  `.ufo/waves/round-88/w1/swarm-registry.json` has 12 members with roles
  `{connector, critic, executor, mutation-tester, reviewer, scout, scribe, sentinel}`
  and **no `planner` member** — the planner seat is held at L1 and a scout data-walk
  carries the bounded planning function, exactly as the r86 disclosure describes.
- Same pattern as the fleet-wide answer at `.ufo/l0-questions.md:52` (*"planner is a
  frozen-topology seat the swarm validator rejects by design; the L1 holds the
  canonical §3 planner seat"*). The r88 disclosure is correct; the conflict is
  retained, not silently resolved.

**Note (not a defect):** r88's `claims.json` `lowest_axis` and `unchanged` fields are
silent on the L2-planner conflict, whereas the round-88 spec context and the r86/r87
lane disclosures both carry it. L1 should keep the conflict in the r88 report body so
the disclosure is not lost between the spec context and the claims file.

---

## 10. Other bounded observations

- **Registry scale.** `corpus/SOURCES.md` holds **854** rows at both the base and the
  lands revision (`grep -c '^| S'`), matching `claims.json` `census_before`
  ("854 rows"). The census receipt `reports/round-88/census-start.json` is
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`,
  **rc 0**, ending `kotodama ok …/corpus/SOURCES.md`. Its stdout carries 36 warning
  lines (W01 tier-C mined rows, W04 duplicate-URL pairs) but **does not itself print
  the 854 figure** — that number comes from the row count, not from the census
  receipt's stdout. The `census_before` string is accurate but its row count is not
  in the cited receipt; a strict reader should not expect "854" in that stdout.
- **`measure88.py` docstring vs `EXPECT` table.** The module docstring
  (`measure88.py:13`) says the filename oracle expects **1**; the `EXPECT` table
  (`measure88.py:47`) and `claims.json` both say **0**, and the observed value is 0.
  The docstring is stale on that one number. Behaviour is governed by `EXPECT`, so the
  frozen expectation is unambiguous; only the prose is wrong. Frozen, so reported not
  amended.
- **Filename-oracle expectation of 0 is real but for a narrow reason.** The
  committed `filename-only.py` maps *r87-era* case names (`positive-six`,
  `duplicate-record`, `reordered-records` …); the r88 case list is renamed
  (`clean`, `duplicate-id`, `reordered`) and hashed to opaque filenames
  (`case-<sha10>.json`), so the oracle's table never matches and it scores 0/13. This
  is the intended effect, and `claims.json`'s bound *"Case filenames are opaque so
  filename-keyed oracles cannot pass"* holds **for the committed control**. But note
  the counter's `name_salt` (`kotodama-r88-case-`) is **public** — committed in
  `cases.json` — so the opaque names are invertible by anyone who can read the
  committed case list. A filename oracle that reverses the public salt and reads no
  packet body scores **13/13** (measured in scratch: every case passes, including
  `invalid-json`). This is *not* a counterfeit's escape, because the counter never
  asks the battery about filename-only (§1) — but it is the honest limit of the
  "opaque filename" bound and should be recorded as such: **opaque names defeat
  memorisation of the names, not filename-keyed oracles that can recompute them.**
  QUALITY 34's own wording already says this: *"Random filenames alone do not defeat
  content memorization."*
- **Case-list hash is recorded but unchecked.** `case_list_sha256` appears in the
  `MEASURE88_O` receipt but no leg compares it to a frozen constant (§3).
- **`--base` is honoured, `--root` is used for git calls only.** `blob()` shells to
  `git -C <root> show <rev>:<path>`; every path the counter grades is read through it
  except the `materialize` fallback (§3).

---

## 11. What I did not do (scope boundaries)

- Did not amend `reports/round-88/measure88.py`, `reports/round-88/claims.json`,
  `reports/round-88/cases.json`, or any `reports/round-88/controls/*.py`.
- Did not write to `tools/`, `corpus/`, `LOG.md`, `SCORECARD.md`, `MANIFEST.json`,
  `SKILL.md` or any fleet-root/sibling/source-tree path.
- Did not run `git commit`, `git push`, `jj` or any other mutating git/jj command.
- Did not build, lint or test any sibling seat's output; the only runs were my own
  scoped probes against copies of the frozen bytes in scratch.
- Did not remove the stale untracked `round-79/w1-results.json` (§7).
- Did not assert any score, waiver, certification or canon judgement; no 0–10 axis
  number is proposed anywhere in this report.

---

## 12. Reproduction

```
python3 -B .ufo/waves/round-88/w1/stage/ScoutProtocol/receipts/probe-frozen-counter-weaknesses.py \
  --root /home/vgpnk/Projects/shokunin/kotodama-shokunin \
  --work /fast/scratch/hyaku/kotodama-r88/ScoutProtocol
```

Reads the frozen bytes, copies them into `--work`, and re-derives every finding
above. Exit 0 (findings are reported, not raised). Full output:
`.ufo/waves/round-88/w1/stage/ScoutProtocol/receipts/probe-run.txt`.

Frozen-counter copy + hash for reference:
`.ufo/waves/round-88/w1/stage/ScoutProtocol/receipts/measure88-frozen-copy.py`,
`frozen-counter.sha256`, `HEAD.txt`.

## 13. Unresolved / open

1. Does L1 accept the O claim's discrimination as bounded to *"the counter's own
   comparison layer rejects the four committed counterfeits"*, or is a separate
   per-class instrument needed for the battery? (§1 — operator/L1 decision; the
   frozen counter cannot be amended this round.)
2. `reports/round-88/cases.json` hash is recorded but never checked against a frozen
   constant. Should L1 verify `case_list_sha256` at lands time by hand? (§3)
3. The stale untracked `round-79/w1-results.json` — commit with a dated attribution
   note, or leave untracked? (§7) Not removed pending L1.
4. Whether the D claim's new S931–S933 rows are adopted under those ids given the
   shokuknow staged package already occupies S931–S933 in its unrenumbered range
   (§8). Any future package adoption needs a fresh by-document renumber from S934+.
5. The stale `filename-oracle 1` vs `EXPECT 0` docstring mismatch inside the frozen
   counter (§10). Reported, not amended; QUALITY 35 already binds from round 89.
