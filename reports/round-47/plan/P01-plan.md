# P01 — cross-claim build plan (round 47, loop-2 position 1)

- Seat: `P01` | role: planner | claim: cross | date 2026-10-19
- Out path: `reports/round-47/plan/P01-plan.md` (this file)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`); `git status --porcelain` at my read → `?? reports/round-47/`
- Contract read: `reports/round-47/claims.json` (C `:24-35`, O `:37-48`, Ca `:50-59`), `reports/round-47/targets.json` (P01 row; 64 seats), `REGIMEN.md:1-60`
- Inputs read: `reports/round-44/scout/K02-gap-scout.md` (cartography seed), `reports/round-44/review/R01-review.md` §4 (`:212-254`, the six-part gate contract), `reports/round-43/claims.json`/`validation.json`, `reports/round-44/validation.json`, `reports/round-46/loop-1-retrospective.md`, `reports/round-46/audit/Ca01-manifest.md`, `reports/round-40/op/defect-queue-v2.json`, `reports/round-43/calib/defect-queue-v2-successor-r43.json`, `corpus/QUALITY.md`, `corpus/README.md`, `reports/round-28/readme/sweep.py`

**Plan in one line:** run O first (the gate is independent of the corpus and its demos are baseline-pinned), land C second as one atomic entry+README edit, file Ca third with its freshness row routed to O's landed path — then validate the committed tree from an isolated copy, never in-tree.

---

## 1. Axes and what counts as a move

| axis | measured state at `6e9a30d` | improved only if | harm tripwire | claim |
|---|---|---|---|---|
| **coverage** (lowest non-retired) | 223 entries; culture-material 25; cartography has 0 filename and 0 topic-line owners; no prior-round proposal | 224 total / 26 culture-material; one real entry; README rev 2.5 sweep-green 224==224; prose vector sums 224; zero overwrites; one owner | landing a carried topic (the r44 dream failure), a second owner of cosmography/pilgrimage/direction/architecture, or an arithmetic drift in README | C |
| **operability** | `tools/harness/` has no `claims-freshness.py`; a `.scratch` prototype exists but its selftest is red 17/19 (`selftest_rc=1`) | durable `tools/harness/claims-freshness.py`; selftest green; r43 O+C stale / Ca fresh; fresh negative control; anti-theater mutation still flags; non-zero exit on stale | a two-string lookup that keys on claim prose; a false positive on novel phrasing; evaluating the worktree instead of the baseline commit; `could-not-evaluate` exiting 0 | O |
| **calibration** | five loop-1 carried items named at `reports/round-46/loop-1-retrospective.md:43-53`, none dispositioned into a successor | one new successor artifact; six rows (5 retrospective + 1 r46-audit schema item); each with class + owner + citation; parent sha pinned | dropping a carried item, editing `reports/round-40/op/defect-queue-v2.json` or r43 filed bytes, or classing a routed item as fixed without a re-run | Ca |

Axes in play are exactly `coverage`, `operability`, `calibration` (`claims.json:15-18`). Depth/adjacency/freshness rest; the freshness pause is in force (`claims.json:21`). Coverage is the lowest non-retired axis and therefore the axis lead; O and Ca are the two debts the loop-1 retrospective named.

---

## 2. Measured baseline (commands run at this seat, not asserted)

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], ...}  footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

Ownership and target (claim C):

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo YES || echo NO
NO
$ ls corpus/knowledge/culture-material/ | nl | sed -n '5,6p'
     5	calendar-festival-systems.md
     6	costume-semiotics.md
```

Baseline-object probes (the facts the O demo depends on):

| commit | corpus md | myth-symbol | culture-material | `couples-reference-extractor.py` | `basename-couples-resolver.py` | `claims-freshness.py` | `mineral-stone-symbolism.md` | r43 `dispositions-r38-r39.json` |
|---|---|---|---|---|---|---|---|---|
| `7ceff59` (r43) | 223 | 26 | 25 | present | absent | absent | present | **absent** |
| `c9f4eaa` (r44) | 223 | 26 | 25 | present | absent | absent | present | present |
| `6e9a30d` (r47) | 223 | 26 | 25 | present | present | **absent** | present | present |

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py > .scratch/p01-extractor-7ceff59.py
$ python3 -B .scratch/p01-extractor-7ceff59.py --selftest
PASS ... (8 checks)   rc=0
$ git show 7ceff59:corpus/knowledge/linguistics/phonetics-phonology.md | sed -n '70,80p'
- couples: language (this file, core method); myth (...); ... prospective sibling files: sound-change.md, tone-
  prosody.md, sound-symbolism.md, writing-systems.md
```

So at `7ceff59`: a durable resolver **did** exist and pass; the wrapped couples field **did** read 4 targets; the lithic entry **did** own the topic; the r43 dispositions artifact **did not** exist. Those are the four measurements the r43 regression turns on.

Scratch prototype (the thing O must replace), read-only:

```
$ python3 -B .scratch/ca01/claims-freshness.py --selftest ; echo rc=$?
...
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL
rc=1
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json ; echo rc=$?
[O] operability -- STALE (0/2 premises hold)
[C] coverage -- STALE (2/3 premises hold)
[Ca] calibration -- FRESH (1/1 premises hold)
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
REFUSE: claims O, C have a `before` already false at 7ceff59...
exit 2
```

The prototype's two defects, which the durable tool must not inherit: (a) its E1a/E1b "tool family" scan counts `tools/gates/provenance-audit.py` (a gate whose text mentions a missing `- couples:` header) as a resolver candidate — `R01-44-14` called the naive version a non-starter; (b) two clauses are left `ungrounded` because the prototype mines prose instead of reading declared probes. Both are the same root cause: **prose inference instead of typed, declared checks**.

Parent pin for Ca:

```
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
$ sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json
77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38
```

README anchors (claim C's edit surface): `corpus/README.md:5` (rev 2.4 block), `:11` (the defective prose vector `25/23/25/29/24/94 → 25/23/26/25/24/94`, sum **217**), `:234` (`## culture-material/ (25)`), `:240` calendar row, `:241` costume row, `:544` (`Total knowledge entries: 223.`), `:548` (`total 223 files; directory totals 25/26/25/29/24/94`).

---

## 3. Global execution rules that bind all three plans

1. **Write only the declared out path** under `reports/round-47/`; never stage under `corpus/` or `tools/`. Entry and tool bytes are **fenced drafts**; the integrator applies them (`targets.json:5-11`).
2. **Never edit filed bytes**: `reports/round-1..46/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`. Successors are new files.
3. **No git commits/pushes/installs/network.** `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` before Python.
4. **Never execute `reports/round-*/run-validation.py` in-tree.** Validate from an isolated copy (§7.4; `reports/round-39/calib/isolation-replay-protocol.md:1-45`, I1-I7).
5. **No re-freeze of `declared-in-r7`; no packet-surface changes.** Neither is touched by any of the three claims.
6. **One owner per topic.** Any landing path must be verified against the live partition at the landing commit, not at a prior round's commit.
7. **Unverifiable → `to-verify`.** No invented sources, digests, counts, or seat results.

Ordering rule for the integrator: **one atomic apply per claim** — O's single tool file, C's entry+README edit in one change, Ca's single successor file. A partial apply is a failed claim, not a partial improvement.

---

## 4. Claim C — coverage: one fresh cartography entry (223 → 224)

### 4.1 Contract re-statement

Before: total 223; cartography is a verified-fresh unowned gap (`K02-r44`: no owner, no prior proposal, not carried) — `claims.json:27`. After: `corpus/knowledge/culture-material/cartography-and-mapmaking.md` landed per the entry contract; total 224, culture-material 26; README rev 2.5 sweep-green 224==224 **and** the prose vector corrected to sum 224; audits PASS; zero existing entries overwritten; freshness re-verified at landing (`claims.json:28`).

### 4.2 Pipeline, owners, and gates

| phase | seats | artifact | gate (go/no-go) | on fail |
|---|---|---|---|---|
| **F0 freshness recheck** | K01 | `scout/K01-gap-recheck.md` | at `6e9a30d`: filename sweep 0, topic-line sweep 0, target slug unused, **and** a global `reports/` proposal grep showing no prior cartography proposal | C = unchanged; no landing; no substitute gap without its own fresh sweep |
| **F1 seed + contract** | K02 | `scout/K02-seed-extract.md` | extracts the r44 K02 slug, master claim, section outline, 7-neighbour boundary table, tiered shelf; states the culture-material head-block contract | C blocked; integrator rules |
| **F2 drafts** | C01 (§1-4), C02 (§5-9), C03 (§10-15), C04 (head block) | `cov/C01..C04-*.md` | each section ends in a design lever or decision row (`corpus/QUALITY.md:16-17`); no restatement of a neighbour; head block carries H1 + `- gap filled:` + `- topic:` + `- sources:` + `- couples:` + `- source:` + `- verified-at:` + `- recheck:` + `- scope:` | redraft; no landing |
| **F3 audits** | C05 freshness/slug, C06 source, C07 QUALITY contract, C08 boundary, C12 shelf, C13 couples, C14 example | `cov/C05..C08`, `C12..C14` | all PASS; every backticked path resolves at `6e9a30d`; every external item is `(to-verify)` unless read; couples tokens all resolve; the worked example is declared invented/non-canon | redraft; a single FAIL holds the landing |
| **F4 README + staged sweep** | C09 (rev 2.5 + vector repair), C10 (staged 224 tree) | `cov/C09-readme.md`, `cov/C10-sweep.md` | staged sweep: `rows 224 files 224`, 0 missing / 0 topic mismatch / 0 orphan, totals 224, footer `25/26/26/29/24/94`, exit 0 | fix the arithmetic; never land |
| **F5 landing spec** | W02 + C11 | `cov/W02-landing-spec.md`, `cov/C11-scribe.md` | exact target path, byte source = the assembled fenced entry, sha256 pin, apply order (entry then README, one change) | hold |
| **F6 apply + post-landing** | integrator; V01 | `cov/V01-post-landing.md` | `git status`: `A` entry + `M` README only; total 224; culture-material 26; sweep 224==224; the entry's topic has exactly one owner; no second-owner hit in cosmography/pilgrimage/direction/architecture | revert the apply (it is the integrator's change, not a filed byte); report C blocked |

### 4.3 Entry contract (the non-negotiables)

The draft must satisfy `corpus/QUALITY.md:5-20` clause-for-clause, and the head block must match the established culture-material shape (see `corpus/knowledge/culture-material/calendar-festival-systems.md:1-5`):

1. **H1** naming the register and its craft claim.
2. `- gap filled:` — carries the **fresh measured sweep** and the nearest-neighbour disclaimer, not a bare "no owner" sentence. The load-bearing citation is `corpus/knowledge/myth-symbol/cosmography-cosmography.md:71` ("symbolic, not survey maps") and `:102` ("not cartographic"); the entry quotes it and does not restate the five-axis cosmography typology.
3. `- topic:` — **one physical line** whose `topic_of()` text (lines stripped, space-joined; `reports/round-28/readme/sweep.py:74-81`) is pasted byte-equal into the README row. A continuation line is allowed by the sweep but makes byte-equality fragile; the plan requires a single line.
4. `- sources:` — tier A in-corpus registrations cited by `path:line`; tier B external shelf with editions/pages `(to-verify)`. No external work may be presented as inspected.
5. `- couples:` — every `.md` token resolves at HEAD; no dangling prospective files except those explicitly marked prospective by the corpus convention.
6. `- source:`, `- verified-at:`, `- recheck:`, `- scope:` — the established fields; `- scope:` states reference/method only, canon decisions to lore-shokunin.
7. **Body:** the nine-section spine from `reports/round-44/scout/K02-gap-scout.md` §4.3: question → form typology → survey chain → projection/scale → symbolization → reproduction/trade → silences → calibration bank → build order → decision record + NON-CANON worked example. Each section ends in a lever/row.
8. **Boundary table:** all seven neighbours from K02 §3.5 — cosmography, sacred topography, direction symbolism, architecture/settlement, writing surfaces, Mesoamerican sources, transport/mobility — with "owns / this entry owns / does not restate" per row.
9. **Calibration bank:** at minimum the six rows in K02 §4.5 (neutral map; flat-earth/T-O; portolan accuracy; indigenous maps; map=territory; one-way diffusion), each with status mainstream/contested/discredited and a reason.
10. **Worked example:** declared invented and non-canon, internally consistent, and it must exercise the method (survey precision → projection/scale → orientation → symbol set → medium → silences → authority claim), not just decorate.

### 4.4 Exact landing shape (README arithmetic)

The live measured vector is `25/26/25/29/24/94` (sum 223). The landing vector is `25/26/26/29/24/94` (sum 224).

| anchor | current bytes | after |
|---|---|---|
| `corpus/README.md:5` | `revision: 2.4 — ...` | insert a new `revision: 2.5 — Round-47 culture-material expansion ...` block **above** it; name the entry, the audits, `## culture-material/` 25 → **26**, totals 223 → **224**, vector `25/26/25/29/24/94 → 25/26/26/29/24/94`, and the sweep re-measure |
| `corpus/README.md:11` | `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**.` (sum 217; three slot errors: myth-symbol 26 is right, culture-material 26 is wrong, synthesis 25 is wrong) | replace the pair with the measured rev-2.4 truth: `the vector 25/23/25/29/24/94 → **25/26/25/29/24/94**` (sum 223), and add one correction sentence: "The rev-2.4 prose vector printed here originally read 25/23/26/25/24/94 (sum 217); corrected here to the measured pair." The rev-2.5 block then starts from the corrected 223 vector |
| `corpus/README.md:234` | `## culture-material/ (25)` | `## culture-material/ (26)` |
| between `:240` and `:241` | calendar row, then costume row | insert `- \`cartography-and-mapmaking.md\` — <topic text byte-equal to the entry's `- topic:`>` |
| `corpus/README.md:544` | `Total knowledge entries: 223.` | `Total knowledge entries: 224.` |
| `corpus/README.md:548` | `(total 223 files; directory totals 25/26/25/29/24/94)` | `(total 224 files; directory totals 25/26/26/29/24/94)` |

The rev-2.4 repair is a **forward correction of a live index**, not an edit to a filed round; the claim explicitly sanctions it (`claims.json:28`, non-goal `:64`). The installer must not delete the rev-2.4 block: the index is a dated record, and the sweep only reads the current sections, totals, and footer.

**Staged sweep (C10):** copy the repo to `.scratch/r47-sweep/repo`, apply the entry + README edits there, run `python3 -B reports/round-28/readme/sweep.py` from that copy. Expected: `rows 224 files 224`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `totals_line 224`, `footer {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94], ...}`, `footer_ok True`, exit 0. Record the README sha of the staged tree; the post-landing live sha must equal it.

### 4.5 Acceptance commands (measured on the delivered tree)

```
find corpus/knowledge -name '*.md' | wc -l                     # 224
ls corpus/knowledge/culture-material/*.md | wc -l              # 26
python3 -B reports/round-28/readme/sweep.py                    # rows 224 files 224; footer 25/26/26/29/24/94; exit 0
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l   # exactly 1 (the new entry)
git status --porcelain -- corpus/                              # A entry + M README only
python3 - <<'PY'  # vector arithmetic, independent of the sweep
sum([25,26,26,29,24,94]) == 224
PY
```

Post-landing one-owner check: the new entry's `- couples:` must resolve, and no other entry's `- topic:` may name cartography/mapmaking (the sweep's topic-equality is not an ownership check; C05/V01 run the explicit grep).

### 4.6 Abort rules

- K01 finds any owner or any prior-round proposal → **C = unchanged**; no landing; do not substitute a gap without a fresh sweep and a new claim (the r44 dream failure).
- Any audit FAIL that the drafter cannot repair in-round → no landing; C = unchanged/blocked.
- Staged sweep red → no landing.
- Post-landing second owner or `M` on an existing entry → revert the integrator's apply and report C blocked.
- Do **not** land a second entry to "fix" a collision; one claim, one entry.

### 4.7 Concurrent-seat notes

C01-C04 write disjoint section ranges of one entry; C04 owns the head block, so **C09 must wait for C04's final `- topic:`** before the README row is cut. C10 depends on C09 and C04. C05's freshness result must be taken at `6e9a30d` (and re-run by V01 after apply). No seat may write under `corpus/`; the only corpus writers are the integrator's apply step.

---

## 5. Claim O — operability: the durable claims-freshness gate

### 5.1 Contract re-statement

Before: r43 and r44 both declared claims on stale premises (green resolver existed; owned/carried topics) — R01-43-12; a scratch prototype proved the method but is red-selftest and non-durable (`claims.json:40`). After: `tools/harness/claims-freshness.py` durable with a green selftest; flags r43 O and C stale + Ca fresh; a fresh negative control is not flagged; an anti-theater mutation still flags from capability/ownership rather than literal text; a filed demonstration under `reports/round-47/calib/`; exit non-zero on stale (`claims.json:41`).

### 5.2 Architecture

**CLI**

```
python3 tools/harness/claims-freshness.py --selftest
python3 tools/harness/claims-freshness.py --claims reports/round-<N>/claims.json [--checks <sidecar.json>]
                                              [--root .] [--json] [--at <sha>]
```

- `--claims` is the round contract; `baseline_commit` is read from it and must resolve to a commit via `git rev-parse --verify <sha>^{commit}`. A tag is resolved to a sha and the resolved sha is recorded; a missing/ambiguous baseline is **malformed (exit 2)**.
- `--checks` is a sidecar annotation file keyed by claim id. Required because (a) r43/r44 claims.json are filed bytes and may not be edited, and (b) even r47's own claims.json should not be mutated after dispatch to add checks. The sidecar carries `claims_source_sha256`, and for each claim `before_sha256` and a `checks` list. A sidecar whose `claims_source_sha256` or `before_sha256` does not match the live file is **malformed** — this prevents checking a different claim text than the one declared.
- `--at` overrides the baseline **for diagnostics only**; a claim measured with `--at` other than its declared baseline is labelled `diagnostic` and may not produce an `improved` receipt. `worktree` is refused as a verdict source (exit 2).
- `--json` emits a machine-readable report; the human report names claim id, verdict, each clause with measured vs declared, and the evidence command.

**Baseline evaluation** — `git ls-tree -r --name-only <sha>`, `git show <sha>:<path>`, `git grep -n <pat> <sha> -- <path>`, `git cat-file`/`git hash-object`. Never `open()` on the worktree for verdicts. A probe that cannot be evaluated at the baseline (missing blob for `sha256_eq`, unreadable tree) yields `could-not-evaluate` for that clause, never a default false/true.

**Check schema (sidecar)**

```json
{
  "schema": "kotodama-claims-checks-v1",
  "claims_source": "reports/round-43/claims.json",
  "claims_source_sha256": "<sha of the claims.json bytes>",
  "claims": {
    "O": {
      "before_sha256": "<sha of the before string>",
      "checks": [
        {"id": "E1", "clause_span": [0, 92], "clause_text": "<verbatim slice of before>",
         "probe_kind": "capability_present", "target": "capability:basename-couples-policy",
         "expect": false, "evidence_command": "git ls-tree ... && python3 ... --selftest"}
      ]
    }
  }
}
```

`clause_span` + `clause_text` must match the claim's `before` bytes exactly; the tool rejects a check whose clause text is not a substring/slice. `expect` is the **asserted measured value** — boolean for the presence/absence probes (`false` for absent, `true` for present), integer for `count_eq`, hex digest for `sha256_eq` — so polarity is declared, never inferred. Unknown `probe_kind`, missing `expect`, or a check with no clause span is malformed.

**Verdict unit — premise clauses.** Every check carries a `clause_id`. A clause is a *premise* if the sidecar declares it `role: "premise"` (the default); descriptive context may be declared `role: "context"` with a `context_reason`, and is reported but not counted toward FRESH/STALE. A premise clause with multiple checks mismatches if **any** of its checks mismatches. Every assertoric clause of `before` must map to a premise clause or be listed in `uncovered` with a named reason; an uncovered assertoric clause makes the claim `COULD-NOT-EVALUATE` unless the sidecar marks it context. A claim with zero premise clauses is `COULD-NOT-EVALUATE`. The report prints coverage (`premise clauses matched/total`, `context clauses`, `uncovered`) so a selective reading is visible, not hidden.

**Probe registry (closed set)**

| probe_kind | target | measured | true when |
|---|---|---|---|
| `path_absent` | repo-relative path | exists at baseline? | path absent |
| `path_present` | repo-relative path | exists at baseline? | path present |
| `grep_absent` | `pattern` + optional path/glob | `git grep` at baseline | no match |
| `grep_present` | same | `git grep` at baseline | ≥1 match |
| `count_eq` | glob | file count at baseline | count == `expect` (integer) |
| `sha256_eq` | path | sha256 of the blob at baseline | digest == `expect` (hex) |
| `topic_owner_absent` | topic phrase/vocabulary | parse `- topic:` + H1 of every `*.md` in the tree at baseline | no owner hit |
| `capability_present` | capability id + registry entry (path globs + marker strings) | registry match at baseline; optional baseline selftest recorded as separate evidence, not executed by the verdict | capability present iff a registry match exists |

The registry is data in the tool, not prose inference. `capability_present` must resolve a **capability** (e.g. `basename-couples-policy`) through its registry, not a specific filename — that is what makes the anti-theater mutation meaningful. No mining of claim prose; no counting a tool that merely *mentions* a missing header (the prototype's `provenance-audit.py` false positive).

**Verdict and exit contract**

| condition | verdict | exit |
|---|---|---|
| every premise clause matches, ≥1 premise clause | `FRESH` | 0 |
| any premise clause mismatches | `STALE` | 1 |
| no premise checks, an incomplete premise map, or a premise clause is `could-not-evaluate` and none mismatches | `COULD-NOT-EVALUATE` | 3 |
| bad JSON, missing baseline, unresolvable baseline, unknown probe, missing `expect`, sidecar digest mismatch, claim missing `before` | `MALFORMED` | 2 |

Precedence: any premise mismatch is `STALE` even if another premise is unverifiable; `FRESH` requires every premise clause measured and matching. `could-not-evaluate` must never exit 0. The tool prints a final one-line `REFUSE:`/`PASS:` summary and exits with the code above. Determinism: no timestamps in the verdict decision; claims and checks are sorted by id; the same input bytes produce the same verdict and exit code.

### 5.3 r43 positive regression (the demo)

Filed as `reports/round-47/calib/r43-freshness-demo.json` (sidecar) + a receipt `reports/round-47/calib/r43-freshness-demo.out`. The sidecar references **filed** `reports/round-43/claims.json` by path and sha; it never edits it. Declared premise clauses, with measured values at `7ceff59`:

| claim | clause (verbatim slice) | probe | expect | measured at `7ceff59` | result |
|---|---|---|---|---|---|
| O | "no durable instrument implements the r39 basename-couples policy" | `capability_present` `capability:basename-couples-policy` | `false` | capability present (`tools/harness/couples-reference-extractor.py`, sha `d8d23a26…`, selftest 8/8, wrapped field 4/4) | **mismatch → STALE** |
| O | "the only resolver that ever ran … lives in ephemeral .scratch" | `capability_present` `capability:basename-couples-policy` | `false` | durable resolver present at baseline | **mismatch → STALE** |
| O | "the single wrapped couples field reads 0/4 tokens" | four `grep_present` checks, one per target (`sound-change.md`, `tone-prosody.md`, `sound-symbolism.md`, `writing-systems.md`), each `expect:false`, grouped under one `clause_id` | `false` each | all four present in `corpus/knowledge/linguistics/phonetics-phonology.md` at baseline → 4/4 | **mismatch → STALE** |
| C | "myth-symbol 26" | `count_eq` `corpus/knowledge/myth-symbol/*.md` | `26` | 26 | match |
| C | "total 223" | `count_eq` `corpus/knowledge/*/*.md` | `223` | 223 | match |
| C | "the lithic slot … unbuilt" | `topic_owner_absent` `lithic` (registry vocabulary: lithic/lapidary/stone/gem register) | `true` (absent) | 3 owner hits, all `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` | **mismatch → STALE** |
| Ca | "no per-finding disposition on record" | `path_absent` `reports/round-43/calib/dispositions-r38-r39.json` | `true` | absent | match → **FRESH** |

O's third clause ("the verbatim policy landing lacks block extraction + a disposition leg") is declared `role: "context"` with a reason: it describes a defect in a filed r39 artifact, not a state the gate can flip; the durable-instrument capability probe decides the claim. O05 must either map it to a concrete path probe or keep this context classification with a cited reason — never drop it silently. Expected tool output: `O STALE (0/3 premise clauses; 1 context listed)`, `C STALE (2/3)`, `Ca FRESH (1/1)`, exit **1** (stale; not 2). The sidecar must cover **every assertoric clause** of each `before`; clauses that are interpretive must map to a premise probe or be listed in `context`/`uncovered` with a named reason and owner — no silent `ungrounded` (the prototype's defect).

### 5.4 Negative control (fresh claim)

`reports/round-47/calib/fresh-negative-control.json` + `.out`:

- r44 O at `c9f4eaa`: "no four-class census authority exists" → `path_absent tools/harness/basename-couples-resolver.py` expect `true` (absent at `c9f4eaa`); "total 223" → `count_eq` 223. The remaining descriptive clauses (the extractor's six-class shape, the absence of the ambiguous/indented-prose controls) are listed `role: "context"` with reasons: they describe the witness's properties, not a state that can flip the claim.
- Expected: `FRESH`, exit 0, zero flags, coverage `2/2 premise clauses`.
- This control is deliberately a claim whose `before` is **true** at its baseline — the opposite of r43's O.

### 5.5 Anti-theater mutation

`reports/round-47/calib/anti-theater.json` + `.out` + a mutator script (or a documented command sequence):

1. Take the r43 sidecar. In the O check, replace the literal tool identifier with the witness's actual name (`couples-reference-extractor.py`) in `target`/`evidence_command`/labels; keep `probe_kind` and `expect` unchanged.
2. In the C check, replace the topic literal `lithic` with a synonym (`stone`/`gem`/`lapidary`) and the numeric literals with live values (`26`, `223`).
3. Re-run. Expected: `O STALE`, `C STALE`, `Ca FRESH` — **identical verdicts**. If the gate flips any of them, it is keyed on prose/literals and fails the claim.
4. **Novel-phrasing trap (R02's llama case):** a synthetic claim "the llama-herding register slot is unbuilt" with a declared `topic_owner_absent` for `llama-herding`; the corpus has no such owner, so the declared clause is true → the claim must not be flagged `STALE`. A gate that mines the head noun "register" and counts 51 owners fails this control (the prototype's documented false positive).
5. **Two-string lookup discriminator:** record in the receipt that the literal-lookup variant of the tool would flip the mutated O check to `FRESH`/error, while the capability probe does not. That comparison is the evidence that the verdict comes from capability/ownership.

### 5.6 Selftest control matrix (green, hermetic)

Every control runs in a tempdir under `$TMPDIR`; no writes to the repo. The selftest prints `selftest N/N PASS` and exits 0 only if all pass. The count is computed from the control registry, not a hard-coded literal (the prototype's `seventeen checks collected (18)` failure).

| # | control | expects |
|---|---|---|
| 1 | `path_absent`, absent | match → FRESH |
| 2 | `path_absent`, present | mismatch → STALE |
| 3 | `path_present`, present | match → FRESH |
| 4 | `grep_absent`, no hit | match → FRESH |
| 5 | `grep_absent`, hit | mismatch → STALE |
| 6 | `count_eq`, equal | match → FRESH |
| 7 | `count_eq`, unequal | mismatch → STALE |
| 8 | `sha256_eq`, match / mismatch | FRESH / STALE (2 controls) |
| 9 | `topic_owner_absent`, no owner / owner | FRESH / STALE (2 controls) |
| 10 | `capability_present`, absent with `expect:false` / present with `expect:false` | FRESH / STALE (2 controls) |
| 11 | **polarity control**: same measurement, `expect` flipped | verdict flips (proves `expect` is load-bearing, not inferred) |
| 12 | **baseline-not-worktree**: fixture present in worktree but absent at baseline, declared `path_absent true` | FRESH (proves `git show`/`ls-tree`, not `open()`) |
| 13 | **could-not-evaluate**: claim with zero premise checks; claim with one premise mapped and one assertoric clause left in `uncovered` | exit 3 both, not 0 (2 controls) |
| 14 | **malformed**: bad JSON; missing `baseline_commit`; unknown probe kind; missing `expect` | exit 2 each (4 controls) |
| 15 | **determinism**: run the same input twice | identical verdict + exit code |
| 16 | **r43 regression**: O `0/3` premise clauses, C `2/3`, Ca `1/1` | exit 1; exact clause counts and 1 context clause listed |
| 17 | **fresh negative**: r44 O at `c9f4eaa` | exit 0 |
| 18 | **anti-theater**: mutated r43 sidecar | still O/C stale; llama trap not stale |

The tool must have **no third-party imports** (stdlib only) and no network. It must not write to `reports/round-43/**` or any filed path; its only outputs are stdout/`--json` and the receipt the integrator files.

### 5.7 Verifier chain

| seat | check | gate |
|---|---|---|
| O08 | clean-scratch run of `--selftest`, r43 demo, negative control, anti-theater | all green + correct flags |
| O09 | false-positive traps: novel phrasing (llama), a clause with no polarity, a tag-not-sha baseline | each handled per contract; no false STALE |
| O10 | exit codes: 0 fresh, 1 stale, 2 malformed, 3 could-not-evaluate | never 0 on unverifiable |
| O11 | baseline evaluation: a claim true in the worktree but false at baseline must flag | worktree is not consulted for verdicts |
| O13 | probe coverage: every registry kind exercised by ≥1 control; unknown kind rejected | no dead probes |
| O14 | determinism: two runs, identical verdict + exit | no timestamp/random in the decision |
| O15 | malformed: no baseline, claim missing `before`, non-JSON | exit 2, no crash, no green |
| R04 | non-author review of the R01-43-12 contract | typed probes, baseline eval, polarity, exit codes — judged on depth |
| W01 | landing spec: target path, byte source, sha pin | exact apply, no fork of the witness |
| V02 | post-landing run from the durable path | green + correct flags |

### 5.8 Acceptance commands

```
python3 tools/harness/claims-freshness.py --selftest                                  # exit 0, N/N
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json \
        --checks reports/round-47/calib/r43-freshness-demo.json                       # O,C STALE; Ca FRESH; exit 1
python3 tools/harness/claims-freshness.py --claims <negative-control>.json --checks ... # FRESH; exit 0
python3 tools/harness/claims-freshness.py --claims <mutated>.json --checks ...          # O,C STALE; exit 1
python3 tools/harness/claims-freshness.py --claims <no-checks>.json                    # exit 3
python3 tools/harness/claims-freshness.py --claims <bad>.json                          # exit 2
```

### 5.9 Abort rules

- If the gate cannot flag r43 O/C without reading literal prose, **O is could-not-evaluate**, not improved; do not land it.
- If the selftest is red at the final bytes, do not land; the prototype's 17/19 is the precedent.
- If the tool requires editing r43/r44 claims.json to add checks, stop: the sidecar is the contract.
- If the anti-theater mutation flips a verdict, the tool is theater; do not land.

---

## 6. Claim Ca — calibration: loop-1 defect reconciliation

### 6.1 Contract re-statement

Before: the loop-1 retrospective names 5 carried defects/amendments not yet dispositioned into the queue successor (`claims.json:53`). After: `reports/round-47/calib/queue-successor-r47.json` (or `.md`) files one row per loop-1 carried item: class + owner + cited evidence; the r40 `defect-queue-v2.json` pinned (not edited); each "fixed" claim carries a re-run command (`claims.json:54`).

### 6.2 Row set — 5 retrospective items + 1 r46-audit item = 6 rows

Source bullets: `reports/round-46/loop-1-retrospective.md:43-53`. Class vocabulary: the r43 successor's four classes (`fixed-with-evidence`, `routed-with-owner`, `recorded`, `could-not-recover`) with the v2 mapping (`reports/round-43/calib/defect-queue-v2-successor-r43.json`, `class_vocabulary`).

| row id | origin (cited) | class | owner | reason / next touch | evidence |
|---|---|---|---|---|---|
| `L1-01-freshness-gate` | retro `:45-46`; R01-43-12; r43/r44 validation | `routed-with-owner` | integrator + round-runner maintainer | the durable tool is O's deliverable; route the pre-dispatch check to `tools/harness/claims-freshness.py`; next touch: invoke `--claims ... --checks ...` before each dispatch from r48 and wire it into the round runner | `reports/round-43/validation.json` (O failed, C blocked); `reports/round-44/validation.json` (Ca unprovable); `reports/round-44/review/R01-review.md:243-250`; O's landed path/sha (filled after O) |
| `L1-02-stale-premises-recurrence` | retro `:47-48`; r43 O/C `before`; r44 C `before` | `recorded` | integrator | same defect class as L1-01, two incidents (r43 O+C, r44 C); not a second defect; no separate fix; covered by L1-01's gate | `reports/round-43/claims.json:27,40`; `reports/round-44/claims.json:40`; r43/r44 validation failures |
| `L1-03-resolver-softwrap` | retro `:49-50`; R01-44-05; X01 T1b | `recorded` | resolver maintainer | blank-separated hyphen soft-wrap continuation drops tokens; **0 live incidence**; do not claim universal zero-drop; next touch: next resolver touch | `reports/round-44/cross/X01-trades.md:26,114-155`; `reports/round-44/review/R01-review.md:290`; `reports/round-44/op/O03-defects-verify.md:221-229` |
| `L1-04-manifest-schemas` | r46 audit Ca01 `:5-7`; r46 validation limits | `recorded` | integrator / ledger maintainer | two ledger schemas: closure rows 33-42 (`lanes:{kotodama:"ok"}` + `lane_rounds` + `admitted`) and per-lane rows 43-44 (`verdict`/`admitted`/`close_commit`); documented as schema evolution, not a discrepancy; no action owed | `reports/round-46/audit/Ca01-manifest.md:5-7,9-22`; `reports/round-46/validation.json` limits ("MANIFEST uses two schemas … noted, not a discrepancy") |
| `L1-05-antigravity-outage` | retro `:51-52`; r44 SCORECARD; r47 telemetry | `recorded` (named deviation) | operator / integrator | antigravity lanes non-functional on this host; positions 12/13 skipped or re-routed; loop-2/3 argon positions likewise; next touch: skip/re-route per schedule | `reports/round-46/loop-1-retrospective.md:51-52`; `SCORECARD.md` round-44 section ("the antigravity lane aborted twice"); `reports/round-47/telemetry/dispatch-declared.json` notes |
| `L1-06-zai-exhaustion` | retro `:53`; r43 dispatch deviation; r47 telemetry | `recorded` (named deviation) | integrator | zai usage exhausted; zai seats route to `openai-codex/gpt-6-luna-max` for the session; declared amendment, not a defect | `reports/round-46/loop-1-retrospective.md:53`; `reports/round-43/claims.json` dispatch.deviation; `reports/round-47/telemetry/dispatch-declared.json` notes |

**No silent drop.** The retrospective's five bullets map 1:1 to `L1-01`, `L1-02`, `L1-03`, `L1-05`, `L1-06`; `L1-04` is the Ca claim's own named item from the r46 audit. The artifact must carry this mapping table in a `source_coverage` block (`retro_bullets: 5`, `audit_items: 1`, `rows: 6`, `dropped: []`).

### 6.3 Artifact schema and parent pin

`reports/round-47/calib/queue-successor-r47.json`:

```json
{
  "schema": "kotodama-defect-queue-successor-v1",
  "round": 47,
  "date": "2026-10-19",
  "artifact": "loop-1 defect reconciliation — six successor rows",
  "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256_at_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "prior_successor": {"path": "reports/round-43/calib/defect-queue-v2-successor-r43.json",
                      "sha256": "77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38"},
  "baseline_commit": "6e9a30d",
  "class_vocabulary": {"fixed-with-evidence": "...", "routed-with-owner": "...",
                       "recorded": "...", "could-not-recover": "..."},
  "source_coverage": {"retro_bullets": 5, "audit_items": 1, "rows": 6, "dropped": []},
  "rows": [ ... ],
  "application_gates": [ ... ]
}
```

- `parent_sha256_at_assembly` is **re-measured** at assembly time and must equal `dfc9265d…`; a mismatch means the parent was edited and the artifact must stop.
- Every row carries `id`, `origin`, `class`, `owner`, `reason`, `next_touch`, `evidence`, `verification`.
- `verification` is `null` for routed/recorded rows; a `fixed-with-evidence` row must carry a command + output + landed artifact sha.
- `L1-01` is `routed-with-owner` **unless and until** O's tool is durable, green, and the r43 demo is filed; then it may be upgraded to `fixed-with-evidence` with `verification` = the selftest/demo command output and `landed_tool_sha256`. Even then, adoption (running it pre-dispatch) is a separate next touch, so the honest class at r47 close is routed-with-owner unless the integrator wires it.
- Application gates: (G1) file only after O's path is known; (G2) parent sha unchanged before/after; (G3) no filed bytes edited; (G4) every `fixed` row has a re-run; (G5) the 5+1 mapping is explicit; (G6) provider rows are deviations, not defects.

### 6.4 Verification

- `Ca05` independently re-checks every row: class in vocabulary, owner non-empty, evidence path/line real, no filed-byte edit, parent sha unchanged.
- `Ca07` integrity: every referenced path exists at `6e9a30d`; every cited sha resolves; every `fixed` row has a command output; the parent digest is pinned.
- `R05` non-author review: are the loop-1 items correctly classed (stale-premises routed to the gate, latent edge recorded, schemas documented, provider amendments named)?
- Cross-check with O: `L1-01`'s `next_touch` must name the actual landed tool path and the `--checks` sidecar convention, not a hypothetical.

### 6.5 Acceptance

```
python3 - <<'PY'
import json, hashlib, pathlib
p = pathlib.Path("reports/round-47/calib/queue-successor-r47.json")
d = json.loads(p.read_text())
assert d["parent_sha256_at_assembly"] == hashlib.sha256(
    pathlib.Path("reports/round-40/op/defect-queue-v2.json").read_bytes()).hexdigest()
assert d["source_coverage"]["rows"] == len(d["rows"]) == 6
assert d["source_coverage"]["dropped"] == []
assert all(r["class"] in d["class_vocabulary"] and r["owner"] and r["evidence"] for r in d["rows"])
print("successor OK: 6 rows, parent pinned, zero dropped")
PY
```

Plus: `git status --porcelain -- reports/round-1..46 corpus/lessons tools/gates/frozen` → empty; `sha256sum reports/round-40/op/defect-queue-v2.json` unchanged.

---

## 7. Cross-claim DAG, integration order, validation

### 7.1 Dependency DAG

```
t0  K01  K02  K03  P02  P03                      (scouts + per-claim planners)
t1  C01 C02 C03 C04   O01 O02 O03 O04 O05 O06 O07   Ca01 Ca02 Ca03 Ca04
t2  C05 C06 C07 C08 C12 C13 C14   O08 O09 O10 O11 O13 O14 O15   Ca05
t3  C09 -> C10 -> W02/C11         O12/W01                Ca06 -> Ca07
t4  integrator: apply O tool -> apply C entry+README -> file Ca successor
t5  V01 (C post-landing)  V02 (O post-landing)  A01 A02 A03  R01-R05  X01-X05  Q01
t6  S01 S03; runner authored; isolated validation; telemetry close
```

### 7.2 Integration order and why

1. **Apply O first.** The gate is independent of the corpus; its demos are baseline-pinned (`7ceff59`, `c9f4eaa`) and therefore immune to C's +1. Landing it first lets V02 and the Ca route (`L1-01`) point at a real durable path.
2. **Apply C second, atomically.** Entry + README in one change so the sweep never sees an intermediate inconsistent tree. C's freshness was verified at `6e9a30d`; V01 re-verifies after apply. If C fails after O landed, the round is still rejected/honest-stop; O's improvement is recorded separately, never averaged.
3. **File Ca third.** Ca's `L1-01` row cites O's actual path/sha; Ca's counts are baseline-pinned (223) and must not be silently re-run over the 224 tree. If O did not land, `L1-01` remains `routed-with-owner` naming the absent path and the claim's failure.
4. **Validate the committed close tree** from an isolated copy. The runner is authored at `reports/round-47/run-validation.py` but executed only inside `.scratch/r47-validate/` (git archive of the close commit), with `TMPDIR` inside the sandbox and live-tree sentinels before/after (`reports/round-39/calib/isolation-replay-protocol.md` I1-I7).
5. **Reviewers after measurements**, not before: R01/R02 read filed receipts; X05 checks `claims.json.baseline_commit == HEAD at declaration` (it is `6e9a30d`; `git rev-parse HEAD` confirmed).

### 7.3 What the round runner must measure

| claim | receipt fields |
|---|---|
| C | `total` 224; `culture_material` 26; `entry_sha256`; `readme_sha256`; `sweep` (rows/files/totals/footer/exit); `topic_owner_hits` 1; `corpus_status` = one `A` + one `M`, zero other corpus lines; `readme_vector_sum` 224 |
| O | `tool_sha256`; `selftest_rc` 0 + `selftest_pass` N; `r43_demo` verdicts + exit 1; `negative_control` FRESH + exit 0; `anti_theater` still stale; `no_checks_exit` 3; `malformed_exit` 2; `determinism` true; `witness_untouched` sha |
| Ca | `successor_sha256`; `rows` 6; `classes` all in vocabulary; `parent_sha256` matches; `dropped` 0; `filed_bytes_diff` empty |
| cross | `fragments_present` / `declared_outs`; `corpus_modified_lines`; `validation_isolated` true; `live_sentinels` before/after |

Acceptance is `acceptance_checks_passed: true` **only** when all three claims pass; otherwise exit 1 and a `failures` list naming each. Absent artifacts are `could-not-evaluate`, not pass. No scalar averaging.

### 7.4 Validation isolation (binding)

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git archive <close-commit> | tar -x -C .scratch/r47-validate
cp reports/round-47/run-validation.py .scratch/r47-validate/reports/round-47/
cd .scratch/r47-validate && python3 reports/round-47/run-validation.py
# record: close commit full sha, runner sha256, live validation.json sha before/after,
#         live `git status --porcelain` before/after
```

The in-tree path is never executed. The runner derives `ROOT` from `Path(__file__).resolve().parents[2]` (the r33 shape, `reports/round-33/run-validation.py:23`) and must not chdir to an absolute root.

---

## 8. Risks and tripwires

| risk | claim | tripwire / mitigation |
|---|---|---|
| Cartography turns out owned or carried at `6e9a30d` | C | K01's fresh filename + topic + prior-proposal sweep; abort to unchanged, no substitute |
| The entry duplicates cosmography/pilgrimage/direction/architecture | C | C08's seven-neighbour boundary table; explicit "does not restate" rows; A02 cross-check |
| README arithmetic drifts | C | the vector is computed, not copied: `25+26+25+29+24+94 = 223` → `25+26+26+29+24+94 = 224`; C10's staged sweep; V01's live sweep |
| The rev-2.4 prose defect is "fixed" by deleting history | C | correct forward, keep the rev-2.4 block; add the correction sentence |
| Entry is filler, not method | C | QUALITY clause 4 (decision tables, typology, worked example); R03/X04 judge depth |
| Gate is a two-string lookup | O | anti-theater mutation + llama novel-phrasing control + capability registry (no literal tool name) |
| Gate false-positives on prose | O | typed probes only; no prose mining; the prototype's two `ungrounded` clauses are the warning |
| Gate evaluates the worktree | O | `git show`/`ls-tree`/`git grep` at baseline; O11's worktree-vs-baseline control |
| `could-not-evaluate` returns green | O | exit 3; O10 verifies |
| Selftest count assertion goes stale (prototype 17/19) | O | count computed from the registry; no hard-coded "seventeen" |
| Ca drops a carried item | Ca | `source_coverage` 5+1 mapping, `dropped: []`; Ca05/Q01 check |
| Ca claims "fixed" without a re-run | Ca | `fixed-with-evidence` requires command + output + landed sha; otherwise routed/recorded |
| Parent queue edited in place | Ca | sha pinned and re-measured; G2; Ca07 |
| Provider amendments classed as defects | Ca | `recorded (named deviation)` with the schedule/telemetry citation |
| Partial 64-seat filing | cross | Q01 names absent artifacts as could-not-evaluate; absence is not failure and not pass |
| In-tree runner execution | cross | §7.4 isolation; live sentinels; the ABSOLUTE rule |

---

## 9. Open items / to-verify

- **`reports/round-47/run-validation.py` does not exist at this seat's read** (`test -e` → NO). The integrator authors it; the claims' counting command is the out-of-tree invocation of those bytes.
- Entry digest, README sha, tool sha, and successor sha are **not yet knowable**; the landing specs pin them at apply time. No digest in this plan is invented.
- Tier B cartography editions/pages are `to-verify` (no network at seat time); the entry must not quote an uninspected page.
- The r43 O wrapped-field probe is specified as four `grep_present` checks (one per named target, each `expect:false`) grouped under one `clause_id`; if the implementer instead adds a `field_tokens` kind, it must be added to the closed registry, selftested, and approved by O13 — do not smuggle an undeclared kind. The r43 O clause 3 (policy-landing defect) is declared `context` with a reason; O05 must confirm that classification against the r39 landing artifact or map it to a concrete path probe.
- Whether `L1-01` upgrades to `fixed-with-evidence` depends on O landing; the artifact must be assembled after O's apply, or filed with `routed-with-owner` and a named follow-up.
- The round's `.ufo/reports/round-47/kotodama.md`, `MANIFEST.json` row, LOG entry, and telemetry close are integrator/operator surfaces, outside this seat's write scope.

---

## 10. Handoff map

| reader | read | use |
|---|---|---|
| K01/K02 | §2, §4.2-4.3 | re-verify freshness; extract the seed and contract |
| C01-C04 | §4.3, §4.4 | head block, section spine, boundary table, README byte rule |
| C05-C08, C12-C14 | §4.2 F3, §4.5 | audit gates and acceptance commands |
| C09/C10 | §4.4 | exact README anchors, vector arithmetic, staged sweep |
| W02 | §4.4-4.5 | apply instructions and pins |
| O01-O07 | §5.2-5.6 | architecture, schema, probe registry, verdict/exit, demos, selftest |
| O08-O15 | §5.7-5.8 | verifier checklist and commands |
| W01 | §5.7 | landing spec and sha pin |
| Ca01-Ca04 | §6.2 | row set and class/owner/evidence |
| Ca06 | §6.3 | successor schema and parent pin |
| Ca05/Ca07 | §6.4-6.5 | independent recheck and integrity |
| integrator | §3, §7 | apply order, atomicity, isolated validation |
| R01-R05, X01-X05, Q01 | §2, §8 | measured baseline, risks, tripwires |

---

## 11. Evidence appendix — commands run by this seat

```text
git rev-parse 6e9a30d
  6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
git status --porcelain
  ?? reports/round-47/
find corpus/knowledge -name '*.md' | wc -l
  223
ls corpus/knowledge/culture-material/*.md | wc -l
  25
python3 -B reports/round-28/readme/sweep.py
  rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; totals 223;
  footer 25/26/25/29/24/94; footer_ok True; readme_sha256 7c788a1d…; exit 0
find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
  0
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
  0
test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md
  NO
ls corpus/knowledge/culture-material/ | nl | sed -n '5,6p'
  5 calendar-festival-systems.md; 6 costume-semiotics.md
for c in 7ceff59 c9f4eaa 6e9a30d: git ls-tree -r --name-only $c corpus/knowledge | grep -c '\.md$'
  223 / 223 / 223
git cat-file -e <commit>:tools/harness/couples-reference-extractor.py
  present at all three
git cat-file -e <commit>:tools/harness/basename-couples-resolver.py
  absent at 7ceff59/c9f4eaa; present at 6e9a30d
git cat-file -e <commit>:tools/harness/claims-freshness.py
  absent at all three
git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json
  absent
git show 7ceff59:tools/harness/couples-reference-extractor.py > .scratch/p01-extractor-7ceff59.py
python3 -B .scratch/p01-extractor-7ceff59.py --selftest
  8 PASS; rc=0
git show 7ceff59:corpus/knowledge/linguistics/phonetics-phonology.md | sed -n '70,80p'
  couples block wraps across 6 lines; 4 prospective targets (sound-change, tone-prosody,
  sound-symbolism, writing-systems)
python3 -B .scratch/ca01/claims-freshness.py --selftest ; echo rc=$?
  selftest 17/19 FAIL; rc=1
python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json ; echo rc=$?
  O STALE (0/2); C STALE (2/3); Ca FRESH (1/1); exit 2
sha256sum reports/round-40/op/defect-queue-v2.json
  dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json
  77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38
grep -n 'revision: 2.4|Total knowledge entries|total 223 files|## culture-material/|calendar-festival|costume-semiotics' corpus/README.md
  5 / 544 / 548 / 234 / 240 / 241
sed -n '9,12p' corpus/README.md
  the vector 25/23/25/29/24/94 → 25/23/26/25/24/94 (sum 217)
```

No command in this appendix wrote outside `.scratch` or this out path. No filed byte was edited. Nothing under `corpus/` was staged.
