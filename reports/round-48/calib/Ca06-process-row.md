# Ca06 — process-defect row: entry quality is not gated, and the gate's own use record is unfiled

- Seat: `Ca06` | role: executor | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/calib/Ca06-process-row.md` (this file, and the only file this seat wrote)
- Non-author statement: I drafted no C entry fragment and no README edit. Every number and anchor below was re-measured from the worktree or the Git object store at the baseline; commands and verbatim output are in §7.

**One-line judgment.** The r47 build-quality failure and the r43 stale-premises failure are **one process defect, not two**: the round's dispatch contract constrains *topic ownership* but not *deliverable shape*, and the only thing that caught the 790-line draft was a reviewer appointed after assembly. The stale-premises half is now **closed at the mechanism level** by `tools/harness/claims-freshness.py` (durable, selftest green, r43 regression reproduces); the entry-quality half is **open**, because the gate's seven probe kinds cannot measure length, arithmetic, or citation anchors, and r47's own C thresholds (`reports/round-47/claims.json:34`) carried no length clause at all. The row below records both halves in one successor entry, names the closed half with its re-run command, and routes the open half with an owner and a next touch.

---

## 1. What this row is, and what it must not duplicate

| Artifact | Relationship to this row |
|---|---|
| `reports/round-47/calib/queue-successor-r47.json` row `r43-stale-premises` | The **predecessor** for the stale-premises half. Filed before r47's gate landed; still `routed-with-owner` at r47 close. This row does not mint a second incidence of R01-43-12; it records the gate's landing against that row's own G1–G7 reclass gates. |
| `reports/round-48/calib/Ca02-overbuild.md` (this round, sibling seat) | The **instance row**, filed as `r47-entry-overbuild-defect-class` at `reports/round-48/calib/Ca02-overbuild.md:107`. It owns the B1–B9 instance evidence and the assembled-bytes measurement; this row owns the contract-level cause and the stale-premises half. Integrator: cross-link via `instance_rows`, do not merge the findings or count both as separate process incidences. |
| `reports/round-40/op/defect-queue-v2.json` | The pinned parent. Read and sha-checked here, **not edited** (`dfc9265d…`, §7). Successors are new files. |
| `corpus/README.md` duplicate H1 (`:1`, `:3`) | Out of scope. That is the Ca01/Ca03/Ca05 index defect, not a dispatch-contract defect. |

The row is filed for merge into the **r48 successor** (`schema: kotodama-defect-queue-successor-v1`), whose class vocabulary is `fixed-with-evidence` / `routed-with-owner` / `recorded` / `could-not-recover` / `named-deviation` (`reports/round-47/calib/queue-successor-r47.json`, `class_vocabulary`). This row is `routed-with-owner`: one half is closed with evidence, the other has no fix yet.

---

## 2. The measured failure (entry-quality half)

r47 dispatched C on a **fresh** topic — that part was correct. The gap was real (0 owners), and the gate's ownership probe would clear it again. What the contract did not constrain:

| Fact | Measurement | Source |
|---|---|---|
| Assembled entry length | **790 lines** = 51 (head) + 201 + 361 + 177 (body parts) | fenced `markdown` blocks at `reports/round-47/cov/C04-entry-header.md:111-163`, `C01-entry-a.md:85-287`, `C02-entry-b.md:40-402`, `C03-entry-c.md:72-250`; sum re-added by this seat |
| Live house band (culture-material) | n=25, min 103, **median 149**, **max 221** | `wc -l corpus/knowledge/culture-material/*.md`; max is `funerary-material-culture.md` |
| Ratio | 790 / 221 = **3.57×**; 790 / 149 = 5.30× | arithmetic, §7 |
| R03's own extraction | 739 body lines | `reports/round-47/review/R03-c-content.md:8,96` — a different (non-fence) count |
| Blocking defects | **9** (B1–B9) + 7 should-fix | `reports/round-47/review/R03-c-content.md:188-196` |
| Filed verdict | C `unchanged-blocked` (round `rejected-honest-stop`) | `reports/round-47/validation.json:9,:17,:87` |

Two facts make this a *contract* defect rather than one seat's slip:

1. **The claim's thresholds had no length clause.** `reports/round-47/claims.json:34` reads `"sweep green 224==224; audits clean; gap verified unowned …; the README prose vector sums 224"`. Nothing in the admission contract bounds the entry's size, and `corpus/QUALITY.md:5-20` (the five conditions) contains no length condition either. The discipline is empirical — a house band nobody had written down. r48's C claim adds it (`reports/round-48/claims.json`, thresholds: "entry length <=~250 lines"), which is the norm landing, not a control.
2. **The claim asserted its own audit result.** `reports/round-47/claims.json:28` says `audits PASS` in the `after_required`. At review the chain was not PASS: C14 FAIL on F-1/F-2, C06 PASS-with-corrections, C07 pre-bytes `could-not-evaluate`, C08 PASS-with-P1 (`reports/round-47/review/R03-c-content.md:248`). No field in the claim names *which* audit artifacts must exist at validation, so "audits PASS" was unfalsifiable at dispatch and false at delivery.

The class is therefore: **a claim can be FRESH (topic unowned), satisfy every declared probe, and still deliver an out-of-band, defect-bearing draft**, because the dispatch contract checks the premise and never the shape of the answer.

---

## 3. The stale-premises half is closed — measured, not assumed

The r43 row's own `reclass_gates` (G1–G7) are now satisfiable at `a01405d`, and this seat re-ran the parts that can be re-run:

| Gate | Status | This seat's evidence or filed evidence |
|---|---|---|
| G1 durable path | **PASS** | `tools/harness/claims-freshness.py` exists; `sha256sum` = `466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d` (identical to the sha r47 validation measured: `reports/round-47/validation.json`, `O.measurement.gate_sha256`) |
| G2 green selftest | **PASS** | `--selftest` → `SELFTEST OK: registry 43/43 + seam 19/19 controls`, rc 0 |
| G3 positive regression | **PASS** | `--claims reports/round-43/claims.json --checks reports/round-47/calib/r43-checks.json` → O **STALE** (1/3 contradict), C **STALE** (1/3), Ca **FRESH** (1/1), `exit 1`, REFUSE names O and C |
| G4 negative control | **PASS** | `--claims reports/round-47/claims.json --checks reports/round-47/calib/r47-checks.json` → `3 fresh, 0 stale`, exit 0 |
| G5 anti-theater | **PASS, filed elsewhere** | `reports/round-47/op/O07-anti-theater.md`; probe kind `capability_present` has no name/tool key (`tools/harness/claims-freshness.py:1129`) |
| G6 baseline evaluation | **PASS, filed elsewhere** | `reports/round-47/op/O11-baseline-eval.md:14,20-23`; worktree is unreachable by design (`claims-freshness.py:49-58`) |
| G7 could-not-evaluate ≠ green | **PASS** | `--claims reports/round-43/claims.json` with **no** overlay → `0 fresh, 0 stale, 3 could-not-evaluate`, `exit 3`. Malformed inputs: `reports/round-47/op/O15-malformed.md:19-22` |

So the predecessor row is due for `fixed-with-evidence` — but the **reclass is the integrator's act in a new successor file**, never an in-place edit of `reports/round-47/calib/queue-successor-r47.json` (`sha256 9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58`, unchanged at this baseline).

---

## 4. Why the gate still does not cover entry quality

`tools/harness/claims-freshness.py:96-106` fixes the probe vocabulary at **seven** kinds:

```
path_absent, path_present, grep_absent, count_eq, sha256_eq,
topic_owner_absent, capability_present
```

None measures an entry's line count against the partition band, recomputes a stated arithmetic claim, or resolves a `path:line` anchor to its content. An exhaustive grep of the gate for length/anchor/arithmetic vocabulary returns nothing (§7). The same is true of `tools/gates/` and the rest of `tools/harness/` — no entry-length gate exists.

That is not a demand to automate judgement. It is a demand for **one falsifiable shape check**: a `count_le` probe over a declared glob (baseline-read, like every other probe) would have refused the r47 claim before dispatch, because the claim now carries its own ceiling. The arithmetic and citation legs stay human/verifier work — but they must be *named artifacts*, not a self-report.

---

## 5. The row (fenced — integrator applies)

Merge this object into the r48 successor's `rows[]`. It is one row, two halves. Do not paste it into `reports/round-40/op/defect-queue-v2.json`.

```json
{
  "id": "r48-entry-quality-not-gated",
  "origin": "r47 C rejected unchanged-blocked on an over-built draft: reports/round-47/validation.json:9,:17 (round verdict :87); nine blocking defects at reports/round-47/review/R03-c-content.md:188-196; volume measured at :96. Predecessor stale-premises pattern: r43 R01-43-12 (reports/round-43/review/R01-review.md:400), carried as row r43-stale-premises in reports/round-47/calib/queue-successor-r47.json. Dedupe aliases: r47-C-overbuild, R03-47-B1..B9, r43-stale-premises (linked predecessor, not a second incidence).",
  "instance_rows": [
    "r47-entry-overbuild-defect-class"
  ],
  "premise_correction": "The r48 seat brief frames the freshness gate as guarding 'topic-ownership but not entry quality or stale-proposals'. Correct reading: the gate DOES guard declared stale premises — capability, ownership and counts — and its r43 regression reproduces (O and C STALE, Ca FRESH, exit 1). What it does not guard is (a) premises a claim never declares, and (b) any property of the deliverable. The stale-proposal gap is now mechanism-level closed; only the undeclared-premise and entry-quality gaps remain.",
  "class": "routed-with-owner",
  "v2_class_equivalent": "carried-with-owner",
  "owner": "Fold and reclass: integrator-of-record (r48 successor writer). Open half: next C-drafter seats (draft to the declared ceiling and publish the measured line count before assembly) plus the R03/X03 reviewer seats (verify the count against the live partition max, not the prior round's ceiling). Control extension: next operability (O) claim author plus the tools/harness maintainer. Use-record durability: r48 integrator with S02.",
  "reason": "The dispatch contract checks the premise and not the deliverable's shape. At 6e9a30d r47's C was FRESH on the only clause it declared (cartography unowned, 1/1 clauses hold — reports/round-47/calib/r47-checks.json; the 25/223 counts in the claim prose were not probed) yet delivered 790 fenced lines against a culture-material max of 221 and median of 149, with nine blocking defects. Nothing in the contract refused it: reports/round-47/claims.json:34 carried no length clause, corpus/QUALITY.md:5-20 carries no length condition, and reports/round-47/claims.json:28 asserted 'audits PASS' while the chain was FAIL/PASS-with-corrections/could-not-evaluate/PASS-with-P1 (reports/round-47/review/R03-c-content.md:248). The catch depended on a post-assembly named reviewer, i.e. on seat quality, not on a control. The freshness gate (tools/harness/claims-freshness.py, sha256 466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d) fixes the premise half and cannot fix this one: its probe vocabulary is closed at seven kinds (path_absent, path_present, grep_absent, count_eq, sha256_eq, topic_owner_absent, capability_present; :96-106) and none measures length, arithmetic, or citation anchors. Second, smaller defect in the same class: the gate's first live use at r48 declaration is recorded with placeholders, not paths — 'python3 tools/harness/claims-freshness.py --claims <candidates> --checks <overlay>' (reports/round-48/claims.json:22) — and no overlay or before_checks file exists under reports/round-48/ (grep). The verdicts that decided this round's claim set are therefore not reproducible from the round directory, which is the same evidence-durability failure the freshness gate exists to prevent, one level up.",
  "next_touch": "(1) r48 close, integrator: file the r48 successor with this row; in the same new file reclass the r47 row r43-stale-premises to fixed-with-evidence, citing G1-G4 re-run at reports/round-48/calib/Ca06-process-row.md and the filed G5-G7 demonstrations (reports/round-47/op/O07-anti-theater.md, O11-baseline-eval.md, O15-malformed.md); never edit reports/round-47/calib/queue-successor-r47.json in place. (2) Next O claim: extend the gate with a count_le probe (glob + ceiling, baseline-read) and a required claim-level shape block {max_lines, required_audits[]}; reclass gate = a replayed 790-line claim at a later baseline is refused before dispatch, and a claim naming a missing audit artifact is refused. Coordinate with the proposed_control already filed in r47-entry-overbuild-defect-class (reports/round-48/calib/Ca02-overbuild.md:137) — same gap, carry one control, not two. (3) r48 C-drafters: publish the assembled fenced line count as a filed number before the integrator applies anything, and have a non-author verifier compare it to the live partition max. (4) r48 integrator/S02: file the declaration-time freshness overlay (or inline before_checks into reports/round-48/claims.json) so the C-FRESH/Ca-FRESH/O-STALE verdicts can be replayed; owner and path recorded, not a placeholder.",
  "evidence": "reports/round-47/claims.json:28 (after_required asserts 'audits PASS'), :34 (thresholds carry no length clause); reports/round-47/validation.json:9,:17,:87 (C unchanged-blocked; round rejected-honest-stop); reports/round-47/review/R03-c-content.md:8 (nine blocking defects and the volume finding), :96 (739 body lines vs 103-221, median 149), :188 (B1 arithmetic 20x not 10x), :190 (B3 false source-accusation against a real quote), :194 (B7 worked example states one rule three ways), :204 (P2-3 volume), :248 (audit chain not PASS); assembled length from the fenced blocks at reports/round-47/cov/C04-entry-header.md:111-163 (51), C01-entry-a.md:85-287 (201), C02-entry-b.md:40-402 (361), C03-entry-c.md:72-250 (177) = 790; reports/round-43/review/R01-review.md:400 (R01-43-12); reports/round-47/calib/queue-successor-r47.json (row r43-stale-premises, reclass_gates G1-G7; sha256 9508b6aa...); tools/harness/claims-freshness.py:96-106 (closed probe vocabulary), :49-58 (baseline semantics); reports/round-48/claims.json:22-23 (placeholder invocation, verdict summary); corpus/QUALITY.md:5-20 (five conditions, no length condition); parent pin reports/round-40/op/defect-queue-v2.json sha256 dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907.",
  "verification": "Run by this seat at a01405d, 2026-10-19, all against committed or worktree bytes with TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1: (1) git rev-parse HEAD -> a01405dd36367292255c2652ac0a601f4cd6a0af; (2) sha256sum reports/round-40/op/defect-queue-v2.json -> dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907, and git status --porcelain on it -> empty; (3) parse fences in the four r47 C fragments -> 51+201+361+177 = 790; (4) python3 line count over corpus/knowledge/culture-material/*.md -> n 25, min 103, median 149, max 221; whole partition n 223, median 190, max 436; (5) 790/221 = 3.57; (6) sha256sum tools/harness/claims-freshness.py -> 466aa60d...; (7) python3 -B tools/harness/claims-freshness.py --selftest -> 'SELFTEST OK: registry 43/43 + seam 19/19 controls', rc 0; (8) --claims reports/round-43/claims.json --checks reports/round-47/calib/r43-checks.json -> O STALE, C STALE, Ca FRESH, exit 1; (9) --claims reports/round-47/claims.json --checks reports/round-47/calib/r47-checks.json -> 3 fresh, 0 stale, exit 0; (10) --claims reports/round-43/claims.json with no overlay -> 3 could-not-evaluate, exit 3; (11) grep -rln 'before_checks' reports/round-48/ -> no output (rc 1), and reports/round-48/ contains only claims.json, targets.json, telemetry/; (12) grep for length/anchor/arithmetic vocabulary in tools/harness/claims-freshness.py and tools/gates/, tools/harness/ -> no entry-length or anchor probe.",
  "class_boundary": {
    "in": [
      "an over-built draft (fenced length beyond the house band) that passed every declared dispatch check",
      "unreviewed arithmetic or citation defects reaching assembly because no named audit artifact was required",
      "a claim that asserts its own audit verdict ('audits PASS') without naming the artifacts",
      "a gate verdict recorded with placeholder paths instead of durable ones (the r48 declaration case)"
    ],
    "out": [
      "topic collisions and carried topics (r42/r44): ownership/freshness, already gate-covered",
      "delivery failures under a true premise (r44 Ca): a different class",
      "provider/model substitutions: named-deviation class, not a defect row",
      "README index defects (duplicate H1 at corpus/README.md:1,:3; prose-vector sum): the Ca01/Ca03/Ca05 index lane"
    ]
  },
  "incidence": {
    "entry_quality": {
      "rounds": [47],
      "claims": ["C"],
      "count": 1,
      "basis": "the only measured instance; a grep of reports/round-42..46 for over-build/overlong/bloat vocabulary returns 0 hits, so no older instance is asserted"
    },
    "stale_premises": {
      "narrow": {"rounds": [43], "claims": ["O", "C"], "count": 2, "status": "closed at mechanism level by r47 O; reclass owed"},
      "broad": {"rounds": [43, 44], "claims": ["O", "C", "C-body"], "count": 3, "note": "reports/round-47/calib/queue-successor-r47.json incidence; r44 Ca excluded as a delivery failure"},
      "excluded": {"round": 48, "claim": "O", "reason": "dropped at declaration because the gate flagged its premise STALE; a correct refusal, not an incidence"}
    }
  },
  "closed_half": {
    "artifact": "tools/harness/claims-freshness.py",
    "sha256": "466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d",
    "gates_passed": "G1-G7; see reports/round-48/calib/Ca06-process-row.md section 3",
    "reclass_command": "python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json --checks reports/round-47/calib/r43-checks.json",
    "reclass_owner": "integrator-of-record, in a new r48 successor file"
  },
  "open_half": {
    "property": "no probe or gate measures entry length, arithmetic, or citation anchors; no claim field names the audits that must exist",
    "proposed_control": "count_le probe kind + claim-level shape {max_lines, required_audits[]}",
    "reclass_gate": "a replayed 790-line claim is refused at dispatch; a claim naming an absent audit artifact is refused; the control is baseline-read like every other probe"
  },
  "findings": [
    {
      "id": "r48-use-record-not-durable",
      "class": "routed-with-owner",
      "owner": "r48 integrator with S02 telemetry scribe",
      "evidence": "reports/round-48/claims.json:22 records '--claims <candidates> --checks <overlay>'; grep -rln 'before_checks' reports/round-48/ -> no output; the declaration's FRESH/STALE verdicts resting on that overlay are not replayable from the round directory",
      "next_touch": "file the overlay or inline before_checks before the round closes; a gate verdict that decided the claim set must have a durable artifact",
      "to_verify": "whether an overlay file exists elsewhere (e.g. .scratch) and was simply not filed; absence under reports/round-48/ is measured, global absence is not"
    },
    {
      "id": "r48-threshold-not-instrument",
      "class": "recorded",
      "owner": "integrator-of-record",
      "evidence": "corpus/QUALITY.md:5-20 has five conditions and no length condition; reports/round-48/claims.json puts '<=~250 lines' in a claim threshold, so the norm lives in one round's prose and lapses when the round closes",
      "next_touch": "record the house-band ceiling as a durable entry-contract norm at the next instrument touch, or make the claim-embedded ceiling a required shape field (see open_half)",
      "to_verify": "none - the absence is measured"
    }
  ],
  "application_gates_filed_by": "integrator",
  "provenance": "Read-only over reports/round-47 (claims, validation, R03, cov fragments, calib, op), reports/round-48 (claims, targets), reports/round-40 (queue parent), reports/round-43 (R01), tools/harness (gate), corpus/QUALITY.md and the live culture-material partition. No filed byte edited; no corpus staging; no round runner executed; no git mutation, network or install."
}
```

---

## 6. Why this is a *process* row and not two rows

The two halves share one causal sentence: **the round's contract verifies the question and never the answer.** The stale-premises half was a question-verification failure; the entry-quality half is an answer-verification failure. Splitting them into separate rows is what produced the current state, where the queue carries `r43-stale-premises` as a live row while the r47 over-build has no row at all. One row with `closed_half` / `open_half` keeps the next reader from re-litigating the closed half and keeps the open half from being filed as "just a volume complaint".

The row deliberately does **not**:

- claim r47's reviewers failed — R03 caught all nine defects and the round was honestly rejected (`reports/round-47/validation.json:17`);
- claim a fix exists — the open half has no implemented control, only a proposed one with a reclass gate;
- restate Ca02's instance evidence — Ca02 filed it as `r47-entry-overbuild-defect-class` (`reports/round-48/calib/Ca02-overbuild.md:107`), cross-linked here as `instance_rows`;
- propose a second control — Ca02's row and this one name the same gap; the integrator should carry one control, not two variants.
- touch the README index defect, which is Ca01/Ca03/Ca05's lane.

---

## 7. Commands and verbatim output

All run from the lane root, 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ sha256sum reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json \
            reports/round-43/calib/defect-queue-v2-successor-r43.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json
9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58  reports/round-47/calib/queue-successor-r47.json
77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38  reports/round-43/calib/defect-queue-v2-successor-r43.json
$ git status --porcelain reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json
(no output)

$ python3 (fence extraction, ```markdown bodies only)
C04 111-163 body 51
C01 85-287  body 201
C02 40-402  body 361
C03 72-250  body 177
sum 790

$ python3 (line counts)
culture-material n 25 min 103 median 149 max 221 mean 150.2
all partition    n 223 min 75 median 190 max 436 mean 180.2
790 / 221 = 3.57 ; 790 / 149 = 5.3

$ sha256sum tools/harness/claims-freshness.py
466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d
$ python3 -B tools/harness/claims-freshness.py --selftest | tail -1
SELFTEST OK: registry 43/43 + seam 19/19 controls        (rc 0)

$ python3 -B tools/harness/claims-freshness.py \
      --claims reports/round-43/claims.json --checks reports/round-47/calib/r43-checks.json
  [O] STALE   1/3 clauses contradict
  [C] STALE   1/3 clauses contradict
  [Ca] FRESH  1/1 clauses hold
summary: 1 fresh, 2 stale ... REFUSE: claim(s) O, C ...        (exit 1)

$ python3 -B tools/harness/claims-freshness.py \
      --claims reports/round-47/claims.json --checks reports/round-47/calib/r47-checks.json
summary: 3 fresh, 0 stale, 0 could-not-evaluate, 0 malformed   (exit 0)

$ python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json
summary: 0 fresh, 0 stale, 3 could-not-evaluate ...            (exit 3)

$ grep -rln 'before_checks' reports/round-48/      # no output, rc 1
$ ls reports/round-48/                              # claims.json  targets.json  telemetry

$ grep -nE 'wc -l|line_count|linecount|anchor|arithmetic|length' tools/harness/claims-freshness.py
(no output)
```

Source anchors re-read for this row: `reports/round-47/claims.json:28,34`; `reports/round-47/validation.json:9,17,87`; `reports/round-47/review/R03-c-content.md:8,96,188,190,194,204,248,262`; `reports/round-43/review/R01-review.md:400`; `reports/round-48/claims.json:7,22-23`; `corpus/QUALITY.md:5-20`; `tools/harness/claims-freshness.py:49-58,96-106,1129`.

---

## 8. What I did not verify

- **The r47 draft's internal defects.** I re-read R03's B1–B9 evidence; I did not independently re-audit all 790 lines. R03 owns that judgement and filed its commands (`reports/round-47/review/R03-c-content.md:262`).
- **Whether an r48 freshness overlay exists outside `reports/round-48/`.** I measured its absence in the round directory (rc 1) and list global existence as `to-verify`.
- **G5 and G7 as live runs.** I cite the filed demonstrations (`reports/round-47/op/O07-anti-theater.md`, `O15-malformed.md`) and re-ran G7's no-checks case; I did not rebuild O07's mutation fixture.
- **Ca02's row.** It is a sibling seat's out path and may not exist yet; the dedupe rule in §1 is a fold instruction, not a claim about its bytes.
- **Any prior over-build instance.** I grepped r42–r46 for the vocabulary and found none; absence of vocabulary is not proof of absence of the pattern, so incidence is stated as 1 measured, not 1 total.

**Write surface:** this file only — `reports/round-48/calib/Ca06-process-row.md`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No round runner was executed; no git commit/push; no install; no network.
