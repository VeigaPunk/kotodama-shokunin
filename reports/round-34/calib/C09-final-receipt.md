- Seat: C09 | scribe | C | date 2026-10-19 | baseline da68a6d

# C09 — final receipt fold, claim C (box-1 durability + A09 anchor reissue)

**Mission** (`reports/round-34/targets.json:63`): "Final receipt fold for claim C."
**Out** (`reports/round-34/targets.json:63`): `calib/C09-final-receipt.md`.
**Cut:** 2026-10-19, lane HEAD `da68a6d705e41f369f21e8607bfaab5b54077f84`
(`git rev-parse HEAD`), env `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
All commands read-only except the negative-control copies under `.scratch/c09-box1/`
(the shared rule sanctions `.scratch` as the scratch root; my only durable write is
this fragment).

## 0. Fold status at a glance

| leg of claim C | state at this seat's cut | basis |
|---|---|---|
| 28/28 named executables resolve at SKILL.md `f9bd07c2…` | **verified by C09** (independent run, exit 0) | §3.1 |
| durable receipt JSON (to land at `reports/round-34/craft/box1-resurvey-durable.json`) | **drafted here, ready to land** (§3.2) | §3.2 |
| the survey's own `date` field is trustworthy | **NO — defect found**, must be set by the receipt, not the tool (§3.3) | `reports/round-30/craft/box1-survey.py:8` |
| anchor reissue table (old → new → owning row) | **measured here**; every row grep-verified (§5) | §5 |
| A09 §3 R1–R8 coverage | **covered** — folded row-for-row (§6) | §6 |
| zero filed-row edits | **verified by C09** (`git status --porcelain` → `?? reports/round-34/` only) | §3.4 |
| C02 receipt JSON ↔ C07 re-survey row parity | **DISCHARGED by C09** — C07's own §7 comparator run here over the landed C02: 28/28 rows, `0` mismatches on line/sha256/resolves after field normalisation (`C02.line`↔`C07.first_line`); digests equal (`f9bd07c2…`), no missing/extra rows | §8.1 |
| C07 independent re-survey verdict | **GREEN, folded** — 28/28 at `f9bd07c2…` by a second extraction method, tracked-at-HEAD check (28/28 in `git ls-tree`), isolated negative control → 27/28 exit 1 | §8.1 |
| C03/C08 reissue table + verification | **C03 still absent**; C08 absent. S03 §4 supplied an 8/8 reissue table; my §5/§5.1 census corrects two of its R5 attributions (C09-F8) | §5.1, §8.2, `## Owed` |
| R06/R07 adversarial/coverage review verdicts | **absent at my reads** — no adversarial finding is folded anywhere in the C block | §8.2, `## Owed` |
| `python3 reports/round-34/run-validation.py` leg | **not evaluable** — the file does not exist (`ls reports/round-34/` → `claims.json`, `depth/`, `targets.json`, `telemetry/`) | §11 |

**Dependency census at my reads.** `find reports/round-34 -type f` returned exactly:
`claims.json`, `depth/D11-preservation.md`, `targets.json`, `telemetry/dispatch-declared.json`.
No C-block sibling fragment (`calib/C01..C08`) and no reviewer fragment (`review/R06`, `review/R07`)
had landed. Per the missing-dependency rule (`reports/round-34/targets.json:11`) I established the
claim-C ground truth myself (§3–§5) and fold the absent seats as owed (§8), rather than quoting
text I could not read.

**Later census (same session, after my measurements).** `find reports/round-34 -type f` then returned
35 files: `calib/{C01,C02,C04,C05,C06,C07,C09}`, `scribe/{S02,S03,S05}`, plus D/O/plan/review/scout
fragments. So `C01, C02, C04, C05, C06, C07` and `S03` landed after my reads and are now folded in
§8; **`calib/C03` and `calib/C08` are still absent**, as are `review/R06` and `review/R07` (§8.2).

## 1. What claim C actually asserts (verbatim anchors)

- Claim C `before` (`reports/round-34/claims.json:58`): SKILL.md digest moved `79fe91d3…` → `f9bd07c2…`
  (O05 re-key + C14 Fixes 1-4 + FD-N4/N5; 715 → 732 lines); the round-30 box-1 survey is green only as
  console output at the old digest; A09-pins names the stale line anchors with no durable reissue.
- Claim C `after_required` (`reports/round-34/claims.json:60`): a digest-pinned, dated, re-runnable
  box-1 receipt at `f9bd07c2…`; the A09 anchor reissue as a *new* table (old anchor → new anchor →
  owning row), each row grep-verified; box-1 promotion-dossier evidence current at HEAD.
- Thresholds (`reports/round-34/claims.json:65`): 28/28 at the new digest; the reissue table covers
  **every A09 R1–R8 row**; zero filed-row edits.
- Non-goals relevant here (`reports/round-34/claims.json:71`): no edits to any filed round bytes —
  so the reissue is a new table and the old readings stay filed as superseded readings.

## 2. Ground truth measured by this seat

| id | measurement | value | source |
|---|---|---|---|
| G1 | SKILL.md digest / size at HEAD | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, 732 lines | `sha256sum SKILL.md`; `wc -l SKILL.md` |
| G2 | box-1 survey at HEAD | exit **0**; `named 28`, `resolvable 28`, `unnamed_in_skill []`, `skill_sha256 f9bd07c2…` | `python3 -B reports/round-30/craft/box1-survey.py` |
| G3 | survey negative control | 27/28, `unnamed_in_skill ["tools/harness/r8_checks_MUTATED.py"]`, exit **1**, `skill_sha256 0f58712d62262317383aa6e044f4d919f74ef8f43bfb9913b6b3c8636d797ea4` | §3.3 |
| G4 | old pinned receipts | `83b0a78a…` (`reports/round-30/craft/box1-landed-survey.json:4`; `reports/round-30/validation.json:449,1420`), `79fe91d3…` (`reports/round-32/final-dossier.md:46,133`) | grep census §2.2 |
| G5 | r33 supersession already on record | "SKILL.md digest `79fe91d3…` → `f9bd07c2…`; AGENTS.md drafting residue excised (42 → 40 lines)" | `SCORECARD.md:599-600` |
| G6 | r33 edit shape | `git diff --numstat 139e3b6 da68a6d -- SKILL.md` → `35 18 SKILL.md`; hunks at `:128,:479,:481,:483,:486,:488,:491,:501` (address-stable content replacement), `:584` (1→3), `:694-697` (4→5), `:699-700` (2→4), `:704` (1→12), `:714-715` (2→3); cumulative +17 = 732 − 715 | `git diff -U0 … \| grep '^@@'` |
| G7 | AGENTS.md at HEAD | 40 lines, blob `3272db68e4bb3a11a6c18b1bccd7da5560dbd1fa`; `grep -n 'SKILL\|534\|715' AGENTS.md` → **0 hits** | `wc -l AGENTS.md`; `git hash-object` |
| G8 | the excised residue | blob `959acccc85b97fc40178f363b5f3218d8b9a344e`, 42 lines, `:42` = "### 2.2 `SKILL.md` — append one item to \"## Checklist (executable where a tool exists)\" (after :534)" — the anchor A09 cited | `git cat-file -p 959acccc` |
| G9 | filed-byte status of the repo | `git status --porcelain` → `?? reports/round-34/` only | §3.4 |
| G10 | the r6 handoff pair's cross-references | `grep -rn 'SKILL\|79fe91d3\|f9bd07c2' reports/round-30/handoff/declared-in-r6/` → exit **1**, 0 matches | §9-F4 |

## 3. The box-1 leg

### 3.1 Positive measurement (the claim's first leg)

```
$ python3 -B reports/round-30/craft/box1-survey.py
{
 "date": "2026-10-18",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
}
exit=0
```

This is the claim's threshold exactly: **28/28 at the new digest.** The run is at HEAD `da68a6d`
and the digest the tool self-reports equals G1, so the tool is reading the same bytes the claim pins.

### 3.2 Ready-to-land durable receipt (integrator action)

`reports/round-34/craft/box1-resurvey-durable.json` does not exist yet (`find reports/round-34 -type f`).
The block below is the drafted content; the count fields reproduce the G2 run and the `rows` array is
re-derived from the same SKILL.md bytes by this seat's own parse (74 distinct anchor addresses across
28 executables). The integrator lands it verbatim (or merges C02's version if C02 also lands — then
prefer C02's and treat this as the parity reference for C07).

```json
{
 "date": "2026-10-19",
 "mode": "box1-resurvey-durable",
 "observation_window_utc": "2026-10-19T07:0xZ (seat C09 reads)",
 "skill_path": "SKILL.md",
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b",
 "skill_wc_l": 732,
 "baseline_commit": "da68a6d",
 "named_in_skill": 28,
 "resolvable": 28,
 "unresolvable": [],
 "counting_command": "python3 -B reports/round-30/craft/box1-survey.py",
 "tool_date_field_note": "reports/round-30/craft/box1-survey.py:8 hard-codes date 2026-10-18; this receipt sets date explicitly",
 "prior_pins_superseded": [
  "reports/round-30/craft/box1-landed-survey.json:4 (83b0a78a...)",
  "reports/round-30/validation.json:449,1420 (83b0a78a...)",
  "reports/round-32/final-dossier.md:46,133 (79fe91d3...)"
 ],
 "rows": [{"executable":"tools/assemble-culture-d3.py","resolves":true,"skill_line_anchors":[673]},{"executable":"tools/assemble-culture-d4.py","resolves":true,"skill_line_anchors":[207]},{"executable":"tools/assemble-d2-typed.py","resolves":true,"skill_line_anchors":[449]},{"executable":"tools/assemble-d2.py","resolves":true,"skill_line_anchors":[615]},{"executable":"tools/assemble-d4-typed.py","resolves":true,"skill_line_anchors":[139,158,163,195,207,210,211,213,294]},{"executable":"tools/check-craft-exercise.py","resolves":true,"skill_line_anchors":[616]},{"executable":"tools/check-evidence-coupling.py","resolves":true,"skill_line_anchors":[674]},{"executable":"tools/check-gate-battery.py","resolves":true,"skill_line_anchors":[617]},{"executable":"tools/d2-typed-labels.py","resolves":true,"skill_line_anchors":[35,169,208,258,272,281,288,289,290,291,292,293,304,308,329,479,481,483,491]},{"executable":"tools/exercise-handoff-e2e.py","resolves":true,"skill_line_anchors":[448]},{"executable":"tools/gates/argot-derivation-gate.py","resolves":true,"skill_line_anchors":[375,376,377,429,438]},{"executable":"tools/gates/costume-era-consistency-gate.py","resolves":true,"skill_line_anchors":[609]},{"executable":"tools/gates/d4-assembly-check-gate.py","resolves":true,"skill_line_anchors":[450]},{"executable":"tools/gates/d4-typed-labels-check-gate.py","resolves":true,"skill_line_anchors":[451]},{"executable":"tools/gates/handoff-packet-check.py","resolves":true,"skill_line_anchors":[500,612]},{"executable":"tools/gates/lexicon-coverage-audit.py","resolves":true,"skill_line_anchors":[607]},{"executable":"tools/gates/myth-consistency-gate.py","resolves":true,"skill_line_anchors":[608]},{"executable":"tools/gates/naming-collision-gate.py","resolves":true,"skill_line_anchors":[610]},{"executable":"tools/gates/phonology-sanity-gate.py","resolves":true,"skill_line_anchors":[606]},{"executable":"tools/gates/provenance-audit.py","resolves":true,"skill_line_anchors":[611]},{"executable":"tools/gates/register-law-gate.py","resolves":true,"skill_line_anchors":[409,410,418,430,439]},{"executable":"tools/gates/typed-pipeline-gate.py","resolves":true,"skill_line_anchors":[138,187,196,209,212,418,431,439]},{"executable":"tools/harness/packet_links.py","resolves":true,"skill_line_anchors":[452]},{"executable":"tools/harness/packet_uncertainty.py","resolves":true,"skill_line_anchors":[89,128,501]},{"executable":"tools/harness/r8_checks.py","resolves":true,"skill_line_anchors":[454]},{"executable":"tools/harness/receipt_guard.py","resolves":true,"skill_line_anchors":[453]},{"executable":"tools/replay-frozen.py","resolves":true,"skill_line_anchors":[212,573,613]},{"executable":"tools/source-audit-inventory.py","resolves":true,"skill_line_anchors":[614]}]
}
```

### 3.3 C09-F1 — the survey tool cannot produce a *dated* receipt

`reports/round-30/craft/box1-survey.py:8` is `out = {"date": "2026-10-18", …}` — a string literal.
The tool therefore prints `"date": "2026-10-18"` on 2026-10-19 (G2 output, verbatim). Claim C's
`after_required` demands a **dated** receipt (`reports/round-34/claims.json:60`), and A09's R4
(`reports/round-33/adj/A09-pins.md:110`) says to file the re-run output. Piping the tool's stdout into
a receipt would file a wrong date. `box1-survey.py` is a filed round-30 byte and stays untouched
(claim C non-goals, `reports/round-34/claims.json:71`), so the fix is a property of the *new* receipt:
it sets `date` (and the window) itself, as §3.2 does, and carries `tool_date_field_note`.
This is the same class as the round-33 `to-verify`-with-owed-slot pattern; it is a new finding, not a
claim failure — the 28/28 measurement itself is unaffected.

**Negative control (proves the 28/28 leg can fail).** `.scratch/c09-box1/` holds a copy of
`box1-survey.py` at `reports/round-30/craft/` depth, a symlink `tools → <repo>/tools`, and a copy of
`SKILL.md`. Unmutated, the copy reproduces G2 exactly (`named 28`, `resolvable 28`, exit 0, digest
`f9bd07c2…`). After `sed -i 's|tools/harness/r8_checks\.py|tools/harness/r8_checks_MUTATED.py|g'`:

```
{"named": 28, "resolvable": 27, "unnamed_in_skill": ["tools/harness/r8_checks_MUTATED.py"],
 "skill_sha256": "0f58712d62262317383aa6e044f4d919f74ef8f43bfb9913b6b3c8636d797ea4"}  exit=1
```

Both the resolve count and the digest pin move, so the receipt's two guards are independently live:
one renamed path in SKILL.md drops the claim red, and the digest says which bytes were surveyed.

### 3.4 Byte preservation (the claim's third threshold)

`git status --porcelain` → `?? reports/round-34/` and nothing else, at a tree where rounds 1–33 are
committed. So this seat edited no filed round bytes, no `corpus/lessons/*.md`, no `tools/gates/frozen/**`.
This is the C09-local half of the threshold; the round-level check (all 64 seats, including D-block
`reports/round-34/depth/D11-preservation.md`) belongs to the integrator.

## 4. The 28/28 inventory (measured, not copied)

| executable | SKILL.md anchor lines | resolves |
|---|---|---|
| `tools/assemble-culture-d3.py` | 673 | yes |
| `tools/assemble-culture-d4.py` | 207 | yes |
| `tools/assemble-d2-typed.py` | 449 | yes |
| `tools/assemble-d2.py` | 615 | yes |
| `tools/assemble-d4-typed.py` | 139,158,163,195,207,210,211,213,294 | yes |
| `tools/check-craft-exercise.py` | 616 | yes |
| `tools/check-evidence-coupling.py` | 674 | yes |
| `tools/check-gate-battery.py` | 617 | yes |
| `tools/d2-typed-labels.py` | 35,169,208,258,272,281,288,289,290,291,292,293,304,308,329,479,481,483,491 | yes |
| `tools/exercise-handoff-e2e.py` | 448 | yes |
| `tools/gates/argot-derivation-gate.py` | 375,376,377,429,438 | yes |
| `tools/gates/costume-era-consistency-gate.py` | 609 | yes |
| `tools/gates/d4-assembly-check-gate.py` | 450 | yes |
| `tools/gates/d4-typed-labels-check-gate.py` | 451 | yes |
| `tools/gates/handoff-packet-check.py` | 500,612 | yes |
| `tools/gates/lexicon-coverage-audit.py` | 607 | yes |
| `tools/gates/myth-consistency-gate.py` | 608 | yes |
| `tools/gates/naming-collision-gate.py` | 610 | yes |
| `tools/gates/phonology-sanity-gate.py` | 606 | yes |
| `tools/gates/provenance-audit.py` | 611 | yes |
| `tools/gates/register-law-gate.py` | 409,410,418,430,439 | yes |
| `tools/gates/typed-pipeline-gate.py` | 138,187,196,209,212,418,431,439 | yes |
| `tools/harness/packet_links.py` | 452 | yes |
| `tools/harness/packet_uncertainty.py` | 89,128,501 | yes |
| `tools/harness/r8_checks.py` | 454 | yes |
| `tools/harness/receipt_guard.py` | 453 | yes |
| `tools/replay-frozen.py` | 212,573,613 | yes |
| `tools/source-audit-inventory.py` | 614 | yes |

Derivation: `re.findall(r"tools/[\w./-]+\.py", SKILL.md)` (the tool's own pattern,
`reports/round-30/craft/box1-survey.py:6`) over 732 lines, per-line deduped → 28 distinct paths,
74 anchor addresses, 0 unresolvable. The table is what C02's JSON must equal row-for-row.

## 5. Anchor reissue table (claim C's second leg)

**Method.** Two independent derivations, which agree:
(a) *content match* — take the pre-edit line text from `git show 139e3b6:SKILL.md`, find the identical
line in the current file; (b) *hunk arithmetic* — cumulative line-count deltas from G6, so any address
`> 704` shifts `+16` and any address `> 714` shifts `+17`.
Class legend: **U** unchanged (address and content), **C** address stable but content replaced by the
round-33 edits (a citation of the old content is a superseded reading at a live address),
**M** address moved, **R** target retired (the cited bytes no longer exist).

| pre-r33 anchor (715 lines) | post-r33 anchor (732 lines) | class | owning row | what changed |
|---|---|---|---|---|
| `:47` | `:47` | U | A09 R5 | self-cite target, unchanged; cited by `SKILL.md:149`, `SKILL.md:183` |
| `:128` | `:128` | C | A09 R5 / C14 Fix 4 | body replaced: the basis-witness line now cites `tools/harness/packet_uncertainty.py:205,209` with an "erratum 2026-10-19: contract `:183` carries the delivered-record checklist item, not basis hygiene" |
| `:149` | `:149` | U | A09 R5 | the self-citing row itself, unchanged |
| `:183` | `:183` | U | A09 R5 | the second self-citing row, unchanged |
| `:294` | `:294` | U | A09 R5 | cited by `corpus/lessons/README.md:245`, `round-31.md:46`, `round-32.md:34`, `round-32.md:58` |
| `:456-458` | `:456-458` | U | A09 R5 | named in A09's prose but **not cited by any live citer** (see §5.1) |
| `:479`, `:481`, `:483`, `:486`, `:488`, `:491` | same | C | A09 R5 | decision-table rows rewritten by C14 Fixes 1-3 (`TL-01`/`TL-02` re-key, loanword pointers `:26,60`→`:30-31,63`, `:57`→`:59,63`, `FIELD_DEFAULTS`→`translated-label`) |
| `:501` | `:501` | C | A09 R5 | same class (boilerplate-basis row rewritten) |
| `:522` | `:522` | U | A09 R5 | `## Checklist (executable where a tool exists)` heading |
| `:534` | `:534` | U | A09 R5 | last content line of the checklist section, unchanged |
| `:535` | `:535` | U | A09 R5 | blank line, unchanged |
| `:536` | `:536` | U | A09 R5 | `## Corpus map`, unchanged |
| `:584` | `:584-586` | C+M | A09 R5 | the TMPDIR/isolated-export line rewritten (1→3 lines): "isolated repo export — a history-retaining copy (clone or worktree; the round-3 restore-and-replay leg reads `291c714` from `.git`, which a plain tree export lacks)". This hunk is where the +2 shift begins |
| `:660` | `:662` | M | A09 R5 | `## Source-bounded culture drill — D3 (round 7)` heading; cited by `corpus/lessons/round-32.md` per A09 §2.4 — no live citer at my census |
| `:710` | `:726` | M | A09 R5 | `Read reports/round-7/integration-attempts.json …`; no live citer at my census |
| `:713-715` | `:729-732` | M | A09 R5 | the round-31-landed checklist item; its continuation lines were also rewritten (3 → 4 lines: the audit one-liner now tests `closes`/`closes_sha256`) |
| `AGENTS.md:42` (residue) | — | **R** | A09 R5 / A09-F3 | the target is gone: the r33 integration excised the 3-line patch scaffold, 42 → 40 lines (G7, G8), recorded at `SCORECARD.md:599-600` and closed as Q-32-2 (`reports/round-33/op/O03-owner-checks.md:127` "RESOLVES (role-token)"; `corpus/lessons/README.md:243`) |

### 5.1 C09-F2 — the reissue must be built from the citation census, not A09's prose grouping

A09's R5 cell (`reports/round-33/adj/A09-pins.md:111`) names the anchor set as
"`AGENTS.md:42`; self-cites `:149,:183`; filed lesson citations §2.4", and §2.4
(`:91`) groups the filed citations as `round-31.md:46` (`:294, :456-458, :522, :534, :535, :536`) and
`round-32.md:7,33,41,55,57,58` (`:710, :713-715, :660, :522-534, :294`).

My line-level census of every `SKILL.md:N` / `:N-M` token in `corpus/lessons/*.md`, `corpus/lessons/README.md`,
`SCORECARD.md` and `AGENTS.md` (21 distinct sites) finds only these tokens:
`:715` ×4 (README:242; round-32.md:7, :41, :55), `:713-715` ×3 (README:244; round-32.md:33, :57),
`:294` ×4 (README:245; round-31.md:46; round-32.md:34, :58), `:157`,`:205` (round-15.md:25),
`:208` (round-14.md:141), `:262`,`:278`,`:323` (round-19.md:88,:100,:101,:179),
`:189-214` (round-25.md:44), `:264` (SCORECARD.md:520).

Consequences the integrator must not miss:
1. **Live stale cites are exactly seven**: `SKILL.md:715` → `:731-732` (the one-liner, now split across two lines) at `corpus/lessons/README.md:242`,
   `round-32.md:7`, `round-32.md:41`, `round-32.md:55`; `SKILL.md:713-715` → `:729-732` at
   `README.md:244`, `round-32.md:33`, `round-32.md:57`. These are filed bytes → superseded readings,
   re-issued as new rows (§5 table + §7), never edited.
2. **`:456-458`, `:522`, `:534-536`, `:710`, `:660` have no live citer.** They appear in A09's prose
   grouping only. A reissue-table row for them would be a phantom row; if C03/C08 produce such rows,
   this fragment is the counter-evidence. Where the anchors are named rather than cited (the `:710`,
   `:660` cases), the rows belong in the *address map* (§5's M rows), not in the superseded-readings list.
3. **A09's §2.4 census is incomplete at HEAD**: two citer sites exist that it did not list —
   `corpus/lessons/round-32.md:34` and `corpus/lessons/README.md:242,244,245` (parent-owned ledger rows,
   including Q-31-1 at `:238` and Q-32-2 at `:243`). Both are *unchanged* anchors (U), so nothing is
   stale because of them; they matter only for coverage counting.
4. Therefore the threshold phrase "the reissue table covers every A09 R1–R8 row" is satisfiable
   (§6) while a table built from §2.4's grouping alone would carry rows with no referent.

### 5.2 C09-F3 — what "R1–R8" denotes (ruling, with the alternative recorded)

Claim C's `before` and `after_required` (`reports/round-34/claims.json:58,60`) call the reissue
"the A09 R1–R8 **SKILL anchor** reissue". The only R1–R8 list in A09 is §3
(`reports/round-33/adj/A09-pins.md:107-114`) — the **re-pin needs** list, in which R5 is the SKILL.md
*line-anchor* row and R4 is the box-1 re-survey row. Read strictly, "R1–R8" = the whole re-pin list
(claims O and D discharge R1/R2/R6/R8…). Read as the claim's prose heading suggests, "the SKILL anchor
reissue" = R5's anchor set = §2.4. **This fold covers both**: §5 is the anchor table for R5/§2.4, §6
is a status row for each of R1–R8. Nothing is left for the integrator to re-derive; if the integrator
reads "R1–R8" as eight anchors, note that §2.4 enumerates ≈20 addresses, not 8 — the count in the
claim text is a naming artifact, marked `to-verify` against the operator's intent.

## 6. A09 §3 R1–R8 — status at HEAD (fold rows)

| # | A09 row (`A09-pins.md:107-114`) | status at HEAD `da68a6d` | basis |
|---|---|---|---|
| R1 | README blob pin `reports/round-26/run-validation.py:97` | **already superseded in round 33** — the README edit landed in the r33 integration and the r26 in-place-write hazard is the F-C13-1 class claim O audits this round. No C effect | `SCORECARD.md:597-600`; claim O `reports/round-34/claims.json:41` |
| R2 | README sha256 receipts | not a claim-C artifact (README-side); the supersession rows for it are round-33's | `SCORECARD.md:599` |
| R3 | SKILL.md sha256 receipts (8 sites) | **superseded reading, already recorded**: `reports/round-31/validation.json:1026`, `reports/round-32/validation.json:1000`, `reports/round-32/dossier-d11-shonen-boxes.md:50,205`, `dossier-d12-capability-inventory.md:97`, `dossier-d13-operator-decisions.md:48`, `final-dossier.md:46,133`, `scribe/fragment-ledger.md:178,235` all still carry `79fe91d3…`; the new reading `f9bd07c2…` is on record at `SCORECARD.md:599` and in §3.2's receipt | grep census §2.2 |
| R4 | box-1 re-survey at the new bytes | **discharged by this claim** — receipt drafted §3.2, measurement G2 | §3.1–3.2 |
| R5 | SKILL.md line anchors | **this claim's core** — table §5; filed citers stay filed as superseded readings (§5.1 item 1) | §5 |
| R6 | README prose arithmetic / row cells | not a claim-C artifact; round-33 owns it and `SCORECARD.md:599` records the landing. Cross-check only: no `SKILL.md:N` citer broke because of it | §5.1 |
| R7 | x45 `X45-P1` / x57 historical controls | not a claim-C artifact; A09-F4 stands as filed (`reports/round-33/adj/A09-pins.md:125`). Nothing this seat ran contradicts it | A09-pins:100 |
| R8 | README rows vs `round-33.md` landing order | closed by the round-33 integration (33 lessons, README rows landed in the same revision): `reports/round-33/` filed O02 README delta, `reports/round-33/op/O02-readme-delta.md` | `reports/round-33/op/O02-readme-delta.md` |

## 7. Claim-C receipt draft (before → after)

**Before.** SKILL.md `79fe91d3…` (715 lines); box-1's green run exists only as console output at that
digest (`reports/round-32/final-dossier.md:46`), with the last *filed* receipt pinning the even older
`83b0a78a…` (`reports/round-30/craft/box1-landed-survey.json:4`); A09's line anchors are filed prose
with no reissue (`reports/round-33/adj/A09-pins.md:85-94`).

**After (at this seat's cut).** SKILL.md `f9bd07c2…` / 732 lines (`G1`);
`python3 -B reports/round-30/craft/box1-survey.py` → exit 0, 28/28, self-reported digest `f9bd07c2…` (`G2`);
durable receipt drafted with an explicit observation date and the superseded-pin list (`§3.2`);
anchor reissue table measured with two agreeing derivations and a 21-site citation census (`§5`);
seven stale filed citations named as superseded readings (`§5.1`); the A09 `AGENTS.md:42` anchor
resolved as **retired** by the r33 excision (`§5`, G7/G8).

**Counting commands and observed outputs** (claim C, `reports/round-34/claims.json:62`):

| command | observed |
|---|---|
| `python3 -B reports/round-30/craft/box1-survey.py` | exit 0; `named 28`, `resolvable 28`, `skill_sha256 f9bd07c2…` (G2); negative control exit 1, 27/28 (§3.3) |
| `python3 reports/round-34/run-validation.py` | **not executed — the file does not exist**; no in-tree round runner was executed by this seat (F-C13-1 rule, `reports/round-34/targets.json:9`) |

**Thresholds** (`reports/round-34/claims.json:65`): 28/28 at the new digest → **met** (G2);
reissue covers every A09 R1–R8 row → **met as folded** (§6), with the referent ambiguity named (C09-F3);
zero filed-row edits → **met for this seat** (§3.4), round-level check owed to the integrator.

## 8. Fold table — where each sibling's output lands

| seat | artifact | fold slot | status at my fold |
|---|---|---|---|
| C01 | `calib/C01-survey-run.md` | §3.1 measurement + durable-receipt design | **landed** — survey re-run (exit 0, 28/28, `f9bd07c2…`), independent 28-row derivation, in-memory falsifiability controls, §2 states explicitly that the round-30 tool has **no** per-row shape (so `rows[]` is additive), Owed: none. Agrees with §3.1/§3.3 and §4 |
| C02 | `calib/C02-receipt-json.md` | §3.2 JSON (parity reference) | **landed** — full durable JSON, `measured_at_utc 2026-10-19T07:07:09Z`, `skill_sha256 f9bd07c2…`, `survey_script_sha256 d923ae0f…`, row keys `executable/line/lines/resolves/sha256`, plus a re-runnable verifier at `:365-392`. Its row set is byte-identical to §4's (parity run §8.1) |
| C03 | `calib/C03-anchor-reissue.md` | §5 table | **STILL ABSENT** — no file at any read. S03 §4's 8-row table is the only assembled reissue; §5/§5.1 is the measured address map it should be checked against |
| C04 | `calib/C04-byte-check.md` | §3.4 | **landed** — verdict "CONFIRMED — zero filed-round edits are needed"; §3 censuses the filed rows deliberately not edited; §5 runs a negative control on the instrument |
| C05 | `calib/C05-receipt.md` | §7 | **landed** — before-state B1–B7, the §3 verbatim counting-command output, C05-F1 (tool cannot self-date; `box1-survey.py:8`), C05-F2 (instrument output shape ≠ filed receipt shape), §4 anchor map agreeing with §5 (`:660→:662`, `:713-715→:729/731/732`, `AGENTS.md:42` absent), §6 x45/x57 live drift readings, §8 A1–A6 after-state checklist |
| C06 | `calib/C06-scribe.md` | §7 landed-changes | **landed** — landed set (three NEW artifacts), finding S-C06-1 ("the durable JSON is a hand-assembled artifact, not a tee of stdout"), §4 shift map supporting C03 |
| C07 | `calib/C07-verify-survey.md` | independent re-survey verdict → the non-author check the claim needs | **landed, GREEN** — 28/28 at `f9bd07c2…` (732 lines) on `da68a6d`; Method B re-derives the set through a different code path (token split) and agrees row-for-row; all 28 paths HEAD-tracked (28/28 in the 2735-path `git ls-tree`); negative control 27/28 exit 1; its §6 findings 1–5 (`:9` date line, digest naming, 28-is-scoped, box-1 = SKILL-named surface only, `unnamed_in_skill: []` is checked). Its §7 owed item — the C02 row-for-row diff — is **discharged here** (§8.1) |
| C08 | `calib/C08-verify-reissue.md` | independent anchor verification | **STILL ABSENT** — the reissue table still has one author-side measurement chain only (mine + C05 + S03, all reading the same diff) |
| R06 | `review/R06-c-review.md` | adversarial review (survey fidelity, reissue accuracy, receipt durability) | **absent at my reads** |
| R07 | `review/R07-c-review.md` | R1–R8 coverage cross-check | **absent at my reads** |
| S03 | `scribe/S03-c-receipt.md` | final post-review receipt | **landed** — supplies its own verifier-substitute measurements, the 8/8 R1–R8 table (§4), peer-instrument states (§5), preservation evidence (§6), Appendix A durable-receipt content, and findings S03-F1…F5. Two corrections flow the other way: C09-F8 (§9) and the shape conflict of §8.3 |

### 8.1 The C02 ↔ C07 parity run (C07's owed item, executed here)

C07's §7 left the row-for-row comparison owed because C02 was not on disk at its poll. Both files are
now landed, so I ran C07's own comparator (`C07-verify-survey.md:209-230`) with one addition: C07's
rows key their address as `first_line` while C02's key it as `line`/`lines`/`sha256`, so the raw
comparator would silently skip the address field. With an explicit field map:

```
C02 row keys: ['executable', 'line', 'lines', 'resolves', 'sha256']
C07 row keys: ['executable', 'first_line', 'resolves', 'sha256']
mine 28 C02 28
missing in C02: []
extra in C02  : []
digest C02: f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b | mine: f9bd07c2…
alias-normalised mismatches: 0 | rows compared: 28
```

So: identical path sets, identical resolve verdicts, identical per-executable digests, identical first
anchors — **0 mismatches**, which is the outcome C07 said would be a claim-C blocker if it failed.
This is C09's run, not C07's verdict: C07's §6/§8.1 evidence stands on its own, and the mechanical
comparison is now on record rather than owed.

### 8.2 What is still missing, and why it matters

- `calib/C03` (the assembled reissue table) and `calib/C08` (its independent verification) are absent.
  §5 supplies the measured addresses and §5.1 the citer census, so the table is derivable; a claim
  whose threshold reads "each verified by grep" has, at this cut, **one measurement chain** (C05 + S03
  + C09 all reading the `139e3b6 → da68a6d` diff) and no independent second verifier.
- `review/R06`/`review/R07` are absent, so **no adversarial finding is folded into claim C**. The
  claim's own risk — that a reissue row invents an anchor (C09-F2) or that the durable receipt inherits
  the tool's date defect (C09-F1) — was found by builder seats, not by an adversary.

### 8.3 Integration conflict the integrator must resolve: two drafts for one path

`reports/round-34/craft/box1-resurvey-durable.json` is drafted **twice**, in two different shapes:

| | C02 (`calib/C02-receipt-json.md`) | S03 (`scribe/S03-c-receipt.md` Appendix A) |
|---|---|---|
| top-level shape | `mode`, `measured_at_utc`, `skill_sha256`, `skill_lines`, `named_in_skill`, `resolvable`, `unresolvable`, `rows[]`, `survey_stdout`, `provenance`, `reverify`, `not_a_promotion_verdict` | `schema: kotodama-box1-resurvey-v1`, `survey_date`, `tool`, `tool_command`, `tool_date`, `tool_exit`, `skill_sha256`, `skill_lines`, `named`, `resolvable`, `unnamed_in_skill[]`, `supersedes{…}`, `executables[]`, `reproduce` |
| per-row keys | `executable`, `line`, `lines`, `resolves`, `sha256` | `line`, `path`, `resolves` |
| date handling | `measured_at_utc` + `survey_stdout.date` note | `survey_date` + `tool_date` pair |
| rows | 28, digest-pinned per executable | 28, first-anchor per executable |

Both satisfy claim C's threshold; they are not byte-compatible. **The integrator lands exactly one**
(C02's carries more provenance and per-row digests; S03's carries the r30-style discovery keys
`survey_date`, `executables`, and `supersedes`), or lands one and files the other as a companion.
Landing both at the same path is impossible; landing neither leaves R4/A1 owed.

Note the ordering consequence: the fold I can write is the *material-complete* fold, but the
claim-C verdict itself needs C08's independent run and R06/R07's findings; a claim cannot verify
against its own builders' measurements, which is exactly the state of the reissue leg (§8.2).

## 9. Findings

| id | finding | class | owner | evidence |
|---|---|---|---|---|
| **C09-F1** | `reports/round-30/craft/box1-survey.py:8` hard-codes `date: 2026-10-18`, so the tool cannot emit a *dated* receipt; piping it would file a wrong date into a durability artifact. | real finding — receipt durability | integrator (receipt sets `date` explicitly; tool stays frozen) | G2 output; `box1-survey.py:8`; claim C `after_required` `reports/round-34/claims.json:60` |
| **C09-F2** | A09's R5/§2.4 anchor grouping names anchors with no live citer (`:456-458`, `:522`, `:534-536`, `:710`, `:660`) and omits two real citer sites (`round-32.md:34`, `README.md:242/244/245`). A reissue built from the prose instead of the census carries phantom rows. | real finding — reissue coverage | C03/C08 + integrator; errata target `reports/round-33/adj/A09-pins.md:91,111` (filed, not edited) | §5.1 census |
| **C09-F3** | "A09 R1–R8" is ambiguous: A09 §3 is a *re-pin* list (8 rows, R5 = line anchors, R4 = box-1), not a list of 8 anchors; §2.4 holds ≈20 anchor addresses. Both readings folded. | procedural — naming | integrator; operator intent `to-verify` | claim C `reports/round-34/claims.json:58,60`; `A09-pins.md:107-114,85-94` |
| **C09-F4** | Claim C causes **zero packet-prose drift**: the `declared-in-r6` handoff pair cites neither `SKILL.md` nor either SKILL digest (`grep` exit 1 over all five files), so the D-block's packet work and this claim do not collide on prose. | cross-claim — collision cleared | X00/X08 may cite this | G10 |
| **C09-F5** | The r33 excisions are exactly the ones that retire A09-F3: the `AGENTS.md:40-42` scaffold is gone (42→40 lines) and `SKILL.md` grew 715→732 through five hunks; a reader who applies A09's `:534`/`:713-715` anchors literally now lands text in the wrong place. | real finding — anchor staleness | integrator (this claim's table is the correction) | G6, G7, G8; `SCORECARD.md:599-600` |
| **C09-F6** | `reports/round-34/craft/box1-resurvey-durable.json` is drafted **twice** in incompatible shapes — C02's `rows[]`+`measured_at_utc` block and S03's Appendix A `executables[]`+`survey_date` block. If the integrator lands both or concatenates them, the artifact is invalid JSON or has two contradictory digest pins; if nobody lands one, R4/A1 stays owed. | real finding — integration conflict | integrator (land one; file the other as companion) | §8.3; `reports/round-34/calib/C02-receipt-json.md:19-63`; `reports/round-34/scribe/S03-c-receipt.md:237-287` |
| **C09-F7** | C07 cites the hard-coded date at `reports/round-30/craft/box1-survey.py:9`; the literal sits on **`:8`** (`out = {"date": "2026-10-18", …}`), as C05-F1, S03-F3 and this seat all measure. A downstream seat copying C07's line number into a receipt would cite a line that does not carry the date. One-line erratum, no substance change. | citation erratum | integrator (fold as accepted erratum) | `cat -n reports/round-30/craft/box1-survey.py` → `:8`; `reports/round-34/calib/C07-verify-survey.md:176,253`; C05 `§3` C05-F1; S03-F3 |
| **C09-F8** | S03 §4's R5 table repeats A09 §2.4's attribution of `SKILL.md:456-458`, `:522`, `:534`, `:535`, `:536` to `corpus/lessons/round-31.md:46`. Measured twice here, that file carries exactly one token — `SKILL.md:294` at `:46` — so five of those six attributions are not reproducible. The anchors are class U (unmoved) and the filed rows must not be edited; the repair is a superseding row that lists the citer set as measured (`README.md:245`, `round-31.md:46`, `round-32.md:34,58` for `:294`). | real finding — reissue attribution | integrator (superseding row; `A09-pins.md:91` and `S03-c-receipt.md:125,127` are filed/sibling text, not edit targets) | §5.1 census; `python3` per-line census of `round-31.md` → `['SKILL.md:294']` at `:46`; `reports/round-34/scribe/S03-c-receipt.md:125,127` |

## 10. Honesty notes / to-verify

- **Nothing here is a promotion, canon, clearance or closure verdict** (non-goals,
  `reports/round-34/claims.json:69`). Claim C's verdict needs C08 and R06/R07; C07's verifier run has
  landed and is folded (§8), and the parity check C07 left owed is discharged (§8.1).
- `observation_window_utc` in §3.2 is written as `2026-10-19T07:0xZ` because this seat's reads carry
  no clock stamp; the date (2026-10-19) is from the task frame. C02's receipt carries a real stamp
  (`measured_at_utc 2026-10-19T07:07:09Z`), so prefer C02's — **to-verify** only if C02's block is the
  one landed.
- The `rows[].skill_line_anchors` arrays are anchor *addresses of the path string* in SKILL.md, not
  claims that each mention is an invocation; the survey's contract is resolution only
  (`reports/round-30/craft/box1-survey.py:6-7`). C01 §2 makes the same point from the other side: the
  round-30 tool has no per-row output shape, so any `rows[]`/`executables[]` array is additive
  measurement, and the durable receipt must say so.
- **Confirmed twice, not hedged:** `corpus/lessons/round-31.md` carries exactly one SKILL.md citation
  token, `SKILL.md:294` at `:46` (`python3` census over every line of the file, and an independent
  per-line grep). So A09 §2.4's and S03 §4-R5's attributions of `:456-458`, `:522`, `:534`, `:535`,
  `:536` to `round-31.md:46` are **not reproducible**; the anchors themselves are class U (unmoved), so
  nothing filed is wrong — only the citation attribution is (C09-F8). Leave both filed fragments
  unedited; a superseding row is the repair.
- No filed round runner was executed by this seat; the only executables I ran were
  `reports/round-30/craft/box1-survey.py` (a filed *survey tool*, explicitly a claim counting command,
  `reports/round-34/claims.json:62`), its `.scratch` copies, and read-only `git`/`grep`/`python`
  inspection. The comparator of §8.1 is C07's own code, run read-only over two files.

## 11. Why the second counting command is unprovable here

`reports/round-34/run-validation.py` does not exist (`find reports/round-34 -type f` → 4 files), and
`reports/round-34/targets.json:9` states the round's own validator "does not exist yet". So the leg
`python3 reports/round-34/run-validation.py` has no observed output at this cut and cannot be run
even in isolation. Recording it as `could-not-evaluate` here rather than inferring a pass is the
required behaviour per `AGENTS.md`: "Provider liveness is not round acceptance" applies to validators
too — a missing validator is not a green one.

## Owed

- `reports/round-34/craft/box1-resurvey-durable.json` — **the claim's one true artifact, not landed**
  (`ls reports/round-34/craft` → no such directory at my cut). C02 (`calib/C02-receipt-json.md`) and
  S03 (Appendix A) both supply complete drafts in incompatible shapes (§8.3); the integrator lands
  **exactly one** and files the other as companion or errata. §3.2 is this seat's third draft and is
  the weakest of the three (no per-executable digests); prefer C02's rows, S03's `survey_date`
  handling, or merge.
- `reports/round-34/calib/C03-anchor-reissue.md`, `calib/C08-verify-reissue.md` — **still absent**. §5
  supplies the measured old→new addresses and §5.1 the seven live stale cites, and S03 §4 supplies an
  8/8 table — but with the two attribution defects C09-F8 names. Until C08 lands, the reissue leg has
  one measurement chain and no independent verifier (§8.2).
- `reports/round-34/calib/C07-verify-survey.md` §7's owed parity run — **discharged by C09** (§8.1,
  0 mismatches). C07 itself owes nothing further; the integrator may cite §8.1 as the completed check.
- `reports/round-34/calib/C05-receipt.md`, `calib/C06-scribe.md` — **landed** and folded (§8); the
  filed-form before→after and Landed-changes lists are theirs, §7 here is the fold's restatement.
- `reports/round-34/review/R06-c-review.md`, `review/R07-c-review.md` — **absent**, so no adversarial
  finding is folded into claim C (survey fidelity, reissue accuracy, receipt durability, R1–R8
  coverage). Without them the claim-C verdict row stays open in the honest reading of `REGIMEN.md`.
- `reports/round-34/run-validation.py` — the round validator; when it lands, its box-1 leg should be
  pointed at the landed receipt path and at the §5.1 seven-site stale-cite list, and its reissue leg
  at §5's address map rather than A09's prose grouping.
- `reports/round-34/scribe/S03-c-receipt.md` — **landed**; it is the post-review final fold and already
  carries S03-F1…F5. Three C09 rows should be folded into any successor revision unless R06/R07 refute
  them: C09-F1/S03-F3 (tool cannot self-date — already agreed), C09-F8 (S03 §4 R5's `:456-458`/`:522`/
  `:534-536` citer attributions are not reproducible — new), and C09-F4 (the r6 handoff pair's
  zero-drift result — new).
- Attribution of the x45 1→4-tuple and x57 34/37→28/37 drifts to the round-33 landing — `to-verify`
  (C05 §6 and S03-F4 record the deltas; neither instrument may be quoted green meanwhile). Not a
  claim-C artifact, but it is the one C-adjacent number still lacking a measurement window.

## Citations

- Contract/claims/targets: `reports/round-34/claims.json:20-65` (claim C full block; `:58` before,
  `:60` after_required, `:62` counting commands, `:65` thresholds), `:68-73` (non-goals);
  `reports/round-34/targets.json:5-11` (shared rules; `:9` no in-tree round-runner execution, `:11`
  missing-dependency rule), `:63` (C09 mission + out path).
- Header/method: `REGIMEN.md` (this round's contract, read first per the task frame; `reports/round-34/targets.json:63` for my mission).
- Measurement commands, all 2026-10-19 at repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:
  `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`; `git log --oneline -4`;
  `git status --porcelain` → `?? reports/round-34/`; `sha256sum SKILL.md`; `wc -l SKILL.md` → 732;
  `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, 28/28, `f9bd07c2…`;
  `python3 -B .scratch/c09-box1/reports/round-30/craft/box1-survey.py` twice (unmutated → 28/28 exit 0
  `f9bd07c2…`; after `sed -i 's|tools/harness/r8_checks\.py|tools/harness/r8_checks_MUTATED.py|g'` →
  27/28, exit 1, `0f58712d…`); `git diff --numstat 139e3b6 da68a6d -- SKILL.md` → `35 18`;
  `git diff -U0 139e3b6 da68a6d -- SKILL.md | grep '^@@'`; `git diff -U0 139e3b6 da68a6d -- SKILL.md
  | grep -E '^[-+][^-+]'` (content changes at `:128,:479,:481,:483,:486,:488,:491,:501,:584,:694-697,
  :699-700,:704,:714-715`); `git show 139e3b6:SKILL.md | sed -n '47p;128p;…;713,715p'`;
  inline python content-match of each pre-edit anchor line into the current file;
  inline python census of `tools/*.py` in SKILL.md (28 paths, 74 anchors, all resolve);
  inline python census of `SKILL.md:N` / `:N-M` tokens across `corpus/lessons/*.md`,
  `corpus/lessons/README.md`, `SCORECARD.md`, `AGENTS.md` (21 sites, tokens listed §5.1);
  `grep -rn '79fe91d3\|83b0a78a\|f9bd07c2'` over the tree excluding `.scratch`/`.git`;
  `grep -rn 'SKILL\|79fe91d3\|f9bd07c2' reports/round-30/handoff/declared-in-r6/` → exit 1;
  `wc -l AGENTS.md` → 40; `git hash-object AGENTS.md` → `3272db68e4bb3a11a6c18b1bccd7da5560dbd1fa`;
  `grep -n 'SKILL\|534\|715' AGENTS.md` → 0 hits; `git rev-parse 959acccc` →
  `959acccc85b97fc40178f363b5f3218d8b9a344e`; `git cat-file -p 959acccc | wc -l` → 42 and `| sed -n '40,44p'`;
  `git log --all --oneline --find-object=959acccc85b97fc40178f363b5f3218d8b9a344e`;
  `git show 139e3b6:AGENTS.md | wc -l` → 42; `find reports/round-34 -type f`;
  `ls reports/round-30/handoff/declared-in-r6/`; `ls reports/round-30/craft/`.
- Tools/artifacts: `reports/round-30/craft/box1-survey.py:4-11` (esp. `:6` pattern, `:8` date literal,
  `:10` digest); `reports/round-30/craft/box1-landed-survey.json:4-6`;
  `reports/round-30/validation.json:449,1420`; `reports/round-31/validation.json:1026`;
  `reports/round-32/validation.json:1000`; `reports/round-32/final-dossier.md:46,133`;
  `reports/round-32/dossier-d11-shonen-boxes.md:50,205`;
  `reports/round-32/dossier-d12-capability-inventory.md:97`;
  `reports/round-32/dossier-d13-operator-decisions.md:48`; `reports/round-32/scribe/fragment-ledger.md:178,235`;
  `reports/round-31/rerun.json:120,192`.
- A09 and its disposition: `reports/round-33/adj/A09-pins.md:1,16-21,43-51,55-65,77-83,85-94,96-101,103-114,118-126,133-136`;
  `reports/round-33/op/O03-owner-checks.md:127` (Q-32-2 RESOLVES); `reports/round-33/cross/X00-connector.md:68`;
  `reports/round-33/op/O02-readme-delta.md:278,283`; `reports/round-33/op/P01-plan.md:322,458`;
  `reports/round-33/calib/C15-ledger-draft.json:165` ("pin 79fe91d3… is superseded, not rewritten").
- Fielded round-33 record: `SCORECARD.md:595-600` (digest chain + AGENTS residue excision);
  `SCORECARD.md:520` (a `SKILL.md:264` cite, class U).
- Corpus citers: `corpus/lessons/README.md:238,242,243,244,245`; `corpus/lessons/round-14.md:141`;
  `corpus/lessons/round-15.md:25`; `corpus/lessons/round-19.md:88,100,101,179`;
  `corpus/lessons/round-25.md:44`; `corpus/lessons/round-31.md:46`; `corpus/lessons/round-32.md:7,31,32,33,34,41,55,57,58`.
- `SKILL.md:47,128,149,183,294,456-458,479,481,483,486,488,491,501,522,534,535,536,584-586,660→662,694-700,704,710→726,713-715→729-732`;
  `AGENTS.md:32-39` (the live rules block, unchanged), `AGENTS.md:42` (retired target, exists only in
  blob `959acccc`).
- Folded sibling fragments (all under `reports/round-34/`, read at the late census):
  `calib/C01-survey-run.md:5,39,73,127,231,245,258,299,319,327` (survey re-run, independent derivation,
  in-memory controls, "no per-row shape" note, Owed: none);
  `calib/C02-receipt-json.md:19,29-56,365,375,387,392,399,421` (durable JSON, `measured_at_utc
  2026-10-19T07:07:09Z`, `survey_script_sha256 d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89`,
  re-runnable verifier, fidelity notes);
  `calib/C04-byte-check.md:22,30,63,94,135,163,176,188` ("CONFIRMED — zero filed-round edits are needed",
  non-edited census, negative control);
  `calib/C05-receipt.md:40-52` (B1–B7 before-state), `:59-67` (verbatim counting output), `:89-100`
  (C05-F1 date literal, C05-F2 shape divergence), `:102-130` (anchor map), `:132-147` (R1–R8 states),
  `:149-162` (x45/x57 live drift), `:172-181` (A1–A6 checklist), `:191-206` (owed);
  `calib/C06-scribe.md:17,32,44` (landed set, S-C06-1 "hand-assembled artifact, not a tee of stdout"),
  `:101,136,174,183`;
  `calib/C07-verify-survey.md:9-14` (verdict), `:16-38` (Method A), `:40-61` (Method B + canonical
  digest `b65f0a1e6a5c4fe19e8d8a5ee62024f6a98cc12d0b8e9a3b9a573a9ccbad99a9`), `:63-78` (controls),
  `:80-156` (28-row machine form), `:158-171` (HEAD-tracked check, 2735 paths), `:173-200` (findings),
  `:202-244` (the owed C02 comparator + its code);
  `scribe/S03-c-receipt.md:24-30` (after_required table), `:34-48` (counting re-run), `:57-98` (28-row
  inventory), `:100-140` (R1–R8 table), `:117-136` (R5 anchor table), `:199-207` (S03-F1…F5),
  `:209-225` (review fold), `:227-293` (Appendix A + reproduce), `:295-316` (owed).
- Comparator run for §8.1 (read-only): C07's `§7` code (`calib/C07-verify-survey.md:209-230`) executed
  verbatim over `calib/C07-verify-survey.md` and `calib/C02-receipt-json.md`, plus a field-alias pass
  mapping `C02.line`→`C07.first_line`; output `mine 28 C02 28`, no missing/extra, digests equal,
  `alias-normalised mismatches: 0`.
- Per-line citer census for C09-F8 (read-only `python3`): every line of `corpus/lessons/round-31.md` and
  `corpus/lessons/round-32.md` scanned for `SKILL\\.md:[0-9][0-9,-]*` → `round-31.md:46 ['SKILL.md:294']`
  is the file's only token; `round-32.md` carries `:7,:41,:55` (`:715`), `:33,:57` (`:713-715`),
  `:34,:58` (`:294`).
