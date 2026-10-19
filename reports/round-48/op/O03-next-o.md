# O03 — next-operability scout: verified premises for the next O claim

- Seat `O03` | role scout | claim **cross** | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/op/O03-next-o.md` (this file)
- Non-author statement: I edited no corpus entry, tool, filed round or shared bookkeeping. I wrote only this file plus disposable probes under `.scratch/o03/`. No `reports/round-*/run-validation.py` was executed; no git mutation, install or network call was made.
- Purpose: r48 dropped its candidate O claim because the freshness gate found the premise false as framed (`reports/round-48/claims.json:19`). This report replaces it with three premises I measured myself at HEAD, each with the exact claim shape, counting commands, staleness controls and blockers a next-round O claim needs.

---

## 0. Bottom line

| Rank | Move | Verified at HEAD? | Cost | Main blocker |
|---|---|---|---:|---|
| 1 | **Runner receipt-guard coverage regressed**: r44, r46, r47 write `validation.json` with zero calls to `receipt_guard`; the only census that would catch it is hard-scoped to r34-r40 and still reports `census_complete: true` | yes, 4 commands + source reads | small (one harness tool + its selftest) | none; tools-only, no packet bytes |
| 2 | **Frozen-row roster detection**: the landed guard reads the *live* read set, so it names the same gap on every filed row; a row-local census discriminates exactly 4 defective rows of 10 | yes, independently reproduced | medium (new read-only harness tool) | must not demand exit 0 — the instrument detects a real defect |
| 3 | **Resolver doc/code divergence**: a blank line always ends the `couples` block, though the docstring promises a hyphen exception; the promised branch is unreachable | yes, 4 fixtures + live scan | small | low value: 0/223 live incidence |
| 4 | Successor baseline / read-set membership for `13-register-law.yml` | premise yes, fix **blocked** | large | requires an authorized re-freeze; forbidden this round and unscheduled |

**The dropped premise, corrected.** The r48 candidate said the resolver "drops hyphen soft-wrap". The resolver does *not* mis-heal a soft wrap: with no blank line it heals correctly (`tone-` + `prosody.md` -> `tone-prosody.md`). What actually happens is that a **blank line terminates the block before joining ever sees the continuation**, so the hyphen-wrapped token is silently lost. The mechanism matters: a claim phrased as a join bug invites a patch to `join_parts`, which would be the wrong file region and would not fix the observable.

---

## 1. Measurement 1 — the resolver edge, stated correctly

### 1.1 Fixtures and measured output

Fixtures were written inline (durable here, not only in `.scratch`), then evaluated by importing the live module:

```python
F1 = "- couples: anchor — `writing-systems.md`; seed — `tone-\n\n  prosody.md`\n"
F2 = "- couples: seed — `tone-\n\n  prosody.md`\n"
F3 = "- couples: anchor — `writing-systems.md`; seed — `tone-\n  prosody.md`\n"
F4 = "- couples: method — `writing-systems.md`\n\n  Body prose names `sound-symbolism.md`.\n"
```

| Fixture | shape | `couples_block` parts | `wrapped` | `field_refs` |
|---|---|---|---|---|
| F1 | complete token + blank + hyphen continuation | ``['anchor — `writing-systems.md`; seed — `tone-']`` | `False` | ``['writing-systems.md']`` — **1 token; `tone-prosody.md` lost** |
| F2 | hyphen-only head + blank + continuation | ``['seed — `tone-']`` | `False` | `[]` — **0 tokens** |
| F3 | same as F1 **without** the blank line (control) | ``['anchor — …tone-', 'prosody.md`']`` | `True` | ``['tone-prosody.md', 'writing-systems.md']`` |
| F4 | blank + indented body prose (control) | ``['method — `writing-systems.md`']`` | `False` | ``['writing-systems.md']`` |

Command: `python3 -B .scratch/o03/probe_resolver.py` (tool sha256 `43ce341f…`; the live `--selftest` is 27/27, exit 0).

- Live incidence: scanning all 223 `corpus/knowledge/*/*.md` for a blank-separated indented continuation after a part ending in `-` gives **0 hits** (same sweep as `reports/round-47/calib/queue-successor-r47.json:88-97`). So this is a tool-contract defect, not a corpus defect.

### 1.2 Why the code cannot take its own documented branch

- `tools/harness/basename-couples-resolver.py:55-59` promises: "A blank line terminates the block unless the previous part ends in a hyphen soft wrap and the next line is indented".
- `:73` computes `soft_wrap = parts[-1].endswith("-") and not saw_blank`.
- `:74` then enters the continuation branch only when `INDENT_RE.match(following) and (not saw_blank or soft_wrap)`.

When `saw_blank` is `True`, `soft_wrap` is always `False`, so the `or soft_wrap` disjunct is dead. When `saw_blank` is `False`, the branch is already taken by `not saw_blank`. The documented exception is unreachable. `:359` (S2b) covers a **non-blank** hyphen wrap; `:413-415` (S7c) covers a blank line **without** a hyphen. Neither control covers F1/F2.

### 1.3 Candidate claim (rank 3)

Two honest fixes, pick one and pin it:

- **(a) document the limit** — rewrite `:55-59` to "a blank line always terminates the block", add a control asserting F1 -> 1 token and F2 -> 0 tokens. Smallest change; preserves the anti-body-prose rule that motivated the code.
- **(b) implement the exception** — drop `and not saw_blank` at `:73`, add a control asserting F1 -> `{tone-prosody.md, writing-systems.md}` and F2 -> `{tone-prosody.md}`. Risk: an indented body-prose line following a hyphen-ended part would now be captured. The live corpus has 0 such shapes, so the risk is measured-low but not zero for future entries.

Recommendation: **(a)**. The docstring is the artifact that is wrong; the code's conservative behavior is the one the corpus has been verified against. Whichever is chosen, the selftest must stay green and the live census must be unchanged (0/223 incidence).

Staleness controls for a future claim (`before_checks` snippet — the `clause` must appear verbatim in the claim's `before` sentence):

```json
[
 {"clause": "the resolver docstring promises a hyphen exception the code cannot take",
  "probe_kind": "grep_absent",
  "target": {"glob": "tools/harness/basename-couples-resolver.py",
             "regex": "and not saw_blank"},
  "expect": false,
  "evidence_command": "grep -n 'and not saw_blank' tools/harness/basename-couples-resolver.py"},
 {"clause": "the tested resolver body is the r47-pinned body",
  "probe_kind": "sha256_eq",
  "target": {"path": "tools/harness/basename-couples-resolver.py"},
  "expect": "43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64",
  "evidence_command": "sha256sum tools/harness/basename-couples-resolver.py"}
]
```

---

## 2. Measurement 2 — receipt-guard coverage regressed (rank 1)

### 2.1 The guard is gone from the three most recent runners

`tools/harness/receipt_guard.py` (sha256 `d2297da4…`) is the preflight that refuses a receipt write to a committed path unless `REFRESH_RECEIPTS=1` (`tools/harness/receipt_guard.py:1-17`). Its own docstring requires a publisher either to use `round_runner_main` or to "call guard_receipt itself immediately before writing" (`:8-13`).

| Round | Guard call before `validation.json` write | `grep -c receipt_guard` |
|---|---|---:|
| r40 | `reports/round-40/run-validation.py:227-230` (wrapper), `:242` (call in `main`) | 2 |
| r41 | `:204-207` (wrapper), `:219` (call) | 2 |
| r42 | `:213-216` (wrapper), `:228` (call) | 2 |
| r43 | `:185-188` (wrapper), `:207` — **only in the `else` branch**; `--out` bypasses it, write at `:208` | 1 |
| r44 | none; `main` at `:167`, write at `:178` | **0** |
| r46 | none; `main` at `:148`, write at `:156` | **0** |
| r47 | none; `main` at `:135`, write at `:143` | **0** |

`reports/round-44/run-validation.py:173-178`, `reports/round-46/run-validation.py:154-156` and `reports/round-47/run-validation.py:141-143` all publish to `pathlib.Path(ROOT) / ROUND / "validation.json"` with no preflight. r43's conditional call is a documented `--out` containment carve-out (`reports/round-43/run-validation.py:197-201`); r44/r46/r47 have no such note and no call at all.

### 2.2 The census that should catch it does not look there

`tools/harness/round_runner_conformance.py` already has the leg `guard_receipt_dominates_writes` and a `runner_sha256_nonnull_and_current` leg (`:378-393`, `:411-414`). But:

- `:19` hard-codes `ROUNDS = tuple(range(34, 41))` — seven runners, ending at r40.
- `:457` sets `census_complete` from parse success alone (`all(row["parse"] == "ok")`), not from scope coverage. The tool therefore prints `"census_complete": true` while silently excluding every runner after r40.

Measured, read-only (static AST; no runner executed):

```
$ python3 -B tools/harness/round_runner_conformance.py --json
  runner_count 7, census_complete true,
  defects: absolute-root 6, chdir 6, runner-sha256-null 4

$ python3 -B tools/harness/round_runner_conformance.py \
    reports/round-4{1,2,3,4,6,7}/run-validation.py --json
  runner_count 6, conformant_count 1
  r41 defects []
  r42 defects ['round-specific-findings-limits']
  r43 defects ['guard-not-dominating', 'runner-sha256-null']
  r44 defects ['guard-not-dominating', 'runner-sha256-null']
  r46 defects ['guard-not-dominating', 'runner-sha256-null']
  r47 defects ['guard-not-dominating', 'runner-sha256-null']
```

The `guard-not-dominating` label is a checker limitation for r43 (the guard exists but is conditional); for r44/r46/r47 it is literal — the string `receipt_guard` does not occur in those files.

### 2.3 The second r40 defect: `runner_sha256` key drift

- r40-r42 receipts carry `runner` + `runner_sha256` (e.g. `reports/round-40/validation.json`, value `3dee6e8c…`; r41 `c06f351a…`; r42 `663784fa…`).
- r43, r44, r46, r47 carry **neither key** (checked: top-level key sets). The digest is not lost: each still records its own runner under `input_sha256`, e.g. `reports/round-47/validation.json:74` -> `cf739c57…`.
- So this is **schema drift**, not evidence loss. A claim must say so; calling it "null" would repeat r40's O10 wording on a different shape (`reports/round-40/op/defect-queue-v2.json:192-199`).
- The queue's `N7-receipt-fidelity` row is marked `fixed-with-evidence` at round 41 (`reports/round-40/op/defect-queue-v2.json:371-379`). That row covered receipt *content* (a non-null runner sha and round-specific findings); it did not cover the guard *call*. The r44/r46/r47 omissions are a sibling defect, so the successor record should either map them to a named sibling id or extend N7 explicitly — not silently fold them into a row already marked fixed.

Also verified as genuinely cured, so a new claim must not re-assert it: six absolute-ROOT + import-time `os.chdir` runners exist (r34-r39: `grep -l 'ROOT = "/home' reports/round-*/run-validation.py`), and **zero** after r39 — r40-r44, r46, r47 are relative-ROOT with no `os.chdir` (`grep -rn "os.chdir" reports/round-*/run-validation.py` returns only r33-r39). The queue still lists `R36-ABSOLUTE-ROOT` and `O12-runner-isolation-hazard` as carried (`:102-109`, `:202-209`), so the successor record, not the live fleet, is what is stale.

### 2.4 Candidate claim (rank 1)

**Claim:** land a scope-discovering runner-receipt census — extend `tools/harness/round_runner_conformance.py` (or a successor) so that (i) scope is discovered from `reports/round-*/run-validation.py` (41 runners at this HEAD) rather than a hard-coded range, (ii) `census_complete` means "every discovered runner parsed and was audited", not "the fixed list parsed", (iii) a `guard_receipt` leg distinguishes *absent* from *conditional* and reports the source line, and (iv) the receipt-schema leg reports absent keys separately from null values and checks `input_sha256[<runner>]` as the surviving digest. Add selftest controls (guarded / conditional / absent fixtures). The round's own runner must pass every leg; historical rows are reported, never edited.

**after_required:** tool selftest green; discovered count equals `ls reports/round-*/run-validation.py | wc -l` (41 at this HEAD); census names r44/r46/r47 as guard-absent and r43 as guard-conditional; r43/r44/r46/r47 as receipt-key-absent with `input_sha256` present; the round's own runner conformant; zero filed receipts edited; no runner executed.

**Counting commands:**

```
ls reports/round-*/run-validation.py | wc -l                      # 41
grep -c receipt_guard reports/round-47/run-validation.py           # 0
python3 -B tools/harness/round_runner_conformance.py --selftest    # currently 3/3, exit 0
python3 -B tools/harness/round_runner_conformance.py --json
```

**Threshold caveat:** the current tool exits 0 whenever every *discovered* runner parses, even with defects (`tools/harness/round_runner_conformance.py:583`), so "non-zero" must be defined deliberately. An extension that exits non-zero whenever any historical row is defective would be permanently red and would tempt a weakened check (theater). Define non-zero for (i) incomplete discovery and (ii) a defective **current-round** runner; report historical defects as data rows, not as the exit condition. Demanding an all-green historical census would force either filed-byte edits (forbidden) or that weakening.

**Staleness controls:**

```json
[
 {"clause": "the census scope stops at round 40",
  "probe_kind": "grep_absent",
  "target": {"glob": "tools/harness/round_runner_conformance.py",
             "regex": "ROUNDS = tuple\\(range\\(34, 41\\)\\)"},
  "expect": false,
  "evidence_command": "sed -n '19p' tools/harness/round_runner_conformance.py"},
 {"clause": "the r47 runner writes validation.json without calling the receipt guard",
  "probe_kind": "grep_absent",
  "target": {"glob": "reports/round-47/run-validation.py", "regex": "receipt_guard"},
  "expect": true,
  "evidence_command": "grep -c receipt_guard reports/round-47/run-validation.py"},
 {"clause": "the census tool body is the one measured here",
  "probe_kind": "sha256_eq",
  "target": {"path": "tools/harness/round_runner_conformance.py"},
  "expect": "a9b2fe017d8c9af0d202c29ae6f2baf86a7b3e925410179969145a7e0a0fdca3",
  "evidence_command": "sha256sum tools/harness/round_runner_conformance.py"}
]
```

---

## 3. Measurement 3 — frozen-row roster: detection is possible without re-freezing

### 3.1 The landed guard is row-blind by construction

- `tools/exercise-handoff-e2e.py:3812-3820` defines `v3_manifest_roster_gap(manifest, read_set)` as `set(manifest) - set(read_set)`.
- `:3835` calls it with `assembly.d4["components"]` and the module constant `V3_READ_SET` (`:1940-1964`), never with `baseline["inputs"]`.
- `:3837-3843` records the gap as a non-fatal row; `:3845-3849` records green when empty. The guard "names, not raises": `:4547-4553` (m15a) asserts exit PASS with the gap named.
- Constants: `V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"` (`:1938`); manifest 13 members (`examples/culture-d4/components/*.yml` = 13 files), read set 58.

Consequence: every replay of every filed row gets the same one-line finding, because the comparison does not read the row. This is exactly `reports/round-40/op/defect-queue-v2.json:262-270` (`r38-guard-row-blindness`), still `carried-with-owner`.

### 3.2 Row-local (G5) census, independently reproduced

I re-derived the discriminating comparison from the filed bytes only: for each of the 10 full-shape v3 rows, compare the row's own `packet.md` summary line `9 D2, 4 D3, N D4` against the count of `examples/culture-d4/components/` keys in that row's own `expected.json.inputs`.

| Row | summary line | prose D4 | inputs D4 | verdict |
|---|---|---:|---:|---|
| `reports/round-20/handoff` | `packet.md:277` | 12 | 12 | OK |
| `reports/round-22/handoff/declared-in` | `:279` | 12 | 12 | OK |
| `reports/round-22/handoff/declared-in-r2` | `:279` | 12 | 12 | OK |
| `reports/round-26/handoff/declared-in-r5` | `:279` | 12 | 12 | OK |
| `reports/round-26/register/v3-baseline-r26` | `:279` | 12 | 12 | OK |
| `reports/round-26/remainders/v3-baseline-r26` | `:279` | 12 | 12 | OK |
| `reports/round-27/pinsweep/v3-baseline-r27` | `:279` | **13** | 12 | **FAIL** |
| `reports/round-28/pinsweep/v3-baseline-r28` | `:279` | **13** | 12 | **FAIL** |
| `reports/round-30/handoff/declared-in-r6` | `:279` | **13** | 12 | **FAIL** |
| `reports/round-34/handoff/declared-in-r7` | `:279` | **13** | 12 | **FAIL** |

Result: **4 FAIL / 6 OK**, matching `reports/round-38/op/O03-verify.md:173-184` row for row. The 10 rows are exactly those with the `kotodama-handoff-e2e/3` profile and 58 inputs; `reports/round-23/wording/declared-in-r3` and `reports/round-25/v3-supersession/declared-in-r4` declare 0 D4 inputs and are outside this population.

The exact comparison, run read-only from the lane root:

```python
import json, re
rows = ["reports/round-20/handoff", "reports/round-22/handoff/declared-in",
        "reports/round-22/handoff/declared-in-r2", "reports/round-26/handoff/declared-in-r5",
        "reports/round-26/register/v3-baseline-r26", "reports/round-26/remainders/v3-baseline-r26",
        "reports/round-27/pinsweep/v3-baseline-r27", "reports/round-28/pinsweep/v3-baseline-r28",
        "reports/round-30/handoff/declared-in-r6", "reports/round-34/handoff/declared-in-r7"]
for d in rows:
    e = json.load(open(d + "/expected.json"))
    inputs = sum(1 for k in e["inputs"] if "examples/culture-d4/components/" in k)
    m = re.search(r"(\d+)\s+D2[,;].{0,40}?(\d+)\s+D3[,;].{0,40}?(\d+)\s+D4",
                  open(d + "/packet.md", encoding="utf-8").read())
    print(d, "prose_D4=", m.group(3), "inputs_D4=", inputs)
```

### 3.3 Candidate claim (rank 2)

**Claim:** land `tools/harness/frozen-row-roster-census.py` — a read-only, stdlib-only instrument that discovers every filed v3 baseline, compares each row's own frozen prose D4 count with its own frozen `inputs` D4 count, and prints a per-row verdict. Pin the expected population (exactly `r27/pinsweep`, `r28/pinsweep`, `r6`, `r7` inconsistent; the other six consistent) in a constant or `--expect` file: exit 0 when the measured census equals that pin, exit 1 on drift (a new inconsistent row, or a known row that changed), exit 2 on unreadable input. Add selftest controls for one OK row, one FAIL row, one drifted census, and a malformed row. Run it over the 10 rows; the expected census is exactly the four rows above. Pinning the known population keeps the gate green instead of permanently red — the instrument's value is detecting *changes*, since the cure for the four filed rows is a successor baseline, not an edit.

**Why this is operability and not coverage:** it converts a recorded "naming-not-detection" limit into a detector, using the form the r38 seat already measured but never landed (`reports/round-38/op/O03-verify.md:171-196`; queue `:262-270`, `:272-280`). It does **not** fix the four rows — filed baselines are immutable and the cure is a successor baseline.

**Do not over-claim:** this does not close `R36-R7-READSET-13` / `r37-A01-readset-roster-defect` (`reports/round-40/op/defect-queue-v2.json:92-100`, `:222-230`) or `r38-frozen-row-asymmetry-census`; it supplies the missing detector for them. It also does not touch `tools/exercise-handoff-e2e.py`, so the round's "no packet-surface changes" non-goal is respected.

**Staleness controls:**

```json
[
 {"clause": "the landed manifest-roster guard reads the live read set",
  "probe_kind": "grep_absent",
  "target": {"glob": "tools/exercise-handoff-e2e.py",
             "regex": "v3_manifest_roster_gap\\(assembly\\.d4\\[\"components\"\\], V3_READ_SET\\)"},
  "expect": false,
  "evidence_command": "sed -n '3835p' tools/exercise-handoff-e2e.py"},
 {"clause": "no durable frozen-row roster census exists",
  "probe_kind": "path_absent",
  "target": {"path": "tools/harness/frozen-row-roster-census.py"},
  "expect": true},
 {"clause": "the r7 baseline bytes are the ones measured here",
  "probe_kind": "sha256_eq",
  "target": {"path": "reports/round-34/handoff/declared-in-r7/expected.json"},
  "expect": "bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55",
  "evidence_command": "sha256sum reports/round-34/handoff/declared-in-r7/expected.json"}
]
```

### 3.4 Blocked variant

Adding `13-register-law.yml` to `V3_READ_SET` (or freezing a successor baseline that includes it) is **not** a next-round move under the current rules: it requires a re-freeze (`reports/round-48/claims.json:60` forbids re-freezing `declared-in-r7`), it edits a packet-surface tool, and no re-freeze-owning round is scheduled (`reports/round-40/op/defect-queue-v2.json:92-100`, next_touch "loop 2 (47+)"). Move B gets the detection benefit without either permission.

---

## 4. What a next-round O claim should **not** assert

- **"The resolver drops hyphen soft-wrap."** False as mechanism. It heals a non-blank wrap correctly (F3); the observable is blank-line block termination (F1/F2). Only the fixture-level statement is defensible.
- **"`runner_sha256` is null in r43+"** — the key is absent, not null, and the digest survives under `input_sha256` (`reports/round-47/validation.json:74`). Say "absent key, digest present under a different key".
- **"The runner fleet still carries absolute ROOT."** False since r40. Six absolute runners exist r34-r39 only; r40-r44, r46 and r47 are relative with no `chdir`.
- **"The manifest-roster guard raises on the omission."** False: it records a non-fatal row and exits PASS (`report … m15a`, `tools/exercise-handoff-e2e.py:4547-4553`). It is naming, not detection.
- **"The over-build class is guarded by the freshness gate."** Out of my scope, but worth the planner's attention: `claims-freshness.py` checks topic ownership/paths/counts, not entry length or arithmetic. That is the r48 Ca06/Ca02 thread, not an O move.

---

## 5. Reproduction index

All commands are read-only and were run from the lane root on 2026-10-19 at HEAD `a01405d`.

| # | Command | Observed |
|---|---|---|
| 1 | `python3 -B .scratch/o03/probe_resolver.py` | F1 wrapped=False/1 token; F2 wrapped=False/0; F3 wrapped=True/2; live blank-hyphen hits 0 |
| 2 | `sha256sum tools/harness/basename-couples-resolver.py` | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` |
| 3 | `grep -c receipt_guard reports/round-{43,44,46,47}/run-validation.py` | one count per file: `1`, `0`, `0`, `0` |
| 4 | `python3 -B tools/harness/round_runner_conformance.py --json` | 7 runners, `census_complete true`, `runner-sha256-null 4` |
| 5 | `python3 -B tools/harness/round_runner_conformance.py reports/round-4{1,2,3,4,6,7}/run-validation.py --json` | 6 runners; r41 `[]`, r42 `[round-specific-findings-limits]`, r43/r44/r46/r47 `[guard-not-dominating, runner-sha256-null]` |
| 6 | `python3 -B tools/harness/round_runner_conformance.py --selftest` | 3/3 controls, exit 0 |
| 7 | `grep -l 'ROOT = "/home' reports/round-*/run-validation.py \| sort` | r34-r39 (6) |
| 8 | `grep -rn "os.chdir" reports/round-*/run-validation.py` | r33 (conditional), r34-r39 (import-time); none r40+ |
| 9 | row-local D4 census (script in §3.2) | 10 rows; exactly 4 FAIL (`r27`, `r28`, `r6`, `r7`) |
| 10 | `sha256sum tools/exercise-handoff-e2e.py tools/harness/round_runner_conformance.py tools/harness/receipt_guard.py` | `e5812751…`, `a9b2fe01…`, `d2297da4…` |
| 11 | `ls reports/round-*/run-validation.py \| wc -l` | 41 |

Tool digests measured at this HEAD: resolver `43ce341f…`, conformance `a9b2fe01…`, receipt guard `d2297da4…`, exercise renderer `e5812751…` (identical to the r38-pinned guard sha quoted at `reports/round-40/op/defect-queue-v2.json:92-100`).

---

## 6. Handoff to the planner / next O author

1. **Use Move A.** It is the only candidate whose defect has accept-path consequences (acceptance receipts published without the established preflight), whose instrument already exists, and whose fix is tools-only. Scope it as a census + selftest, not a rewrite of the 41 filed runners.
2. **Pair it with Move B** only if two operability claims are allowed. Move B is a genuine detector with a reproduced 4/10 census; pin the known population so the gate is green on arrival and red only on drift. Frame it as detection, not cure.
3. **Take Move C as a cheap third** or fold it into a broader tools-hygiene claim. It is real but low-value; do not let it stand alone as the round's operability move.
4. **Do not re-declare the r48 dropped premise.** Quote the fixture table in §1.1 in the claim's `before` so the gate can bind to the correct mechanism.
5. **Re-pin at dispatch.** Every digest above is a HEAD-time value; the next round's gate measures at its own `baseline_commit`, so the `sha256_eq` controls must be re-read rather than copied if any of these tools change before dispatch.
6. **Unknowns left as `to-verify`:** whether the r44/r46/r47 omissions were deliberate (no recorded amendment was found in the files I read) and whether `--out` was used in any acceptance run for r43; both are provenance questions for the integrator, not defects I assert.
