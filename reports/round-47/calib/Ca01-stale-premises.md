# Ca01 — the stale-premises class (R01-43-12): disposition

- Seat: `Ca01` (claim **Ca**, calibration)
- Out: `reports/round-47/calib/Ca01-stale-premises.md`
- Baseline: `6e9a30d` (`git rev-parse --short HEAD` → `6e9a30da8bff66e2aef50a8d611b01d2fe6dcfe`)
- Disposition: **`routed-with-owner`** — the class is real and measured; it is routed to
  the r47 claim **O** freshness gate. No fix is claimed in this seat's artifact, because
  `tools/harness/claims-freshness.py` does not exist at HEAD (`ls` → exit 2).
- Parent queue: `reports/round-40/op/defect-queue-v2.json`, sha256
  `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`
  (matches the pin at `reports/round-43/calib/defect-queue-v2-successor-r43.json:7`).
  Pinned, not edited.

## 1. Class definition — what this row owns

A **stale-premises defect** exists when a round's claim is declared with a premise that is
already false in committed bytes at that claim's own `baseline_commit` — i.e. the claim
text or its `before` field was not re-derived from `git show`/`ls-tree` before dispatch.
The class is about **premises**, not delivery: a claim whose premise is true but whose
artifact fails to land is an undelivered-claim defect, not this class.

Two readings are in circulation and must not be conflated:

- **Narrow (adopted for the r47 gate's acceptance):** the clauses of the claim's
  `before` field. This is what `reports/round-44/review/R01-review.md:243-250` specifies
  (`before_checks`, typed probes, baseline evaluation) and what the r47 O claim's
  `after_required` tests (`reports/round-47/claims.json:41`).
- **Broad (the r43 review's own wording):** "the claim texts were not re-measured"
  (`reports/round-43/review/R01-review.md:400`) — the claim body's assertions count too.

The distinction is load-bearing for incidence accounting; see §3.

## 2. Measured instance — r43 at `7ceff59`

All measurements are against committed bytes at the baseline, never the worktree.

### 2.1 Claim O (`reports/round-43/claims.json:27`)

| clause as declared | measured at `7ceff59` | probe kind | verdict |
|---|---|---|---|
| "no durable instrument implements the r39 basename-couples policy" | `tools/harness/couples-reference-extractor.py` tracked, sha `d8d23a26…`; selftest 8/8, exit 0 | `capability_present` | **false** |
| "the only resolver that ever ran … lives in ephemeral `.scratch`" | the same tracked extractor is the durable resolver | `path_present` | **false** |
| "the policy landing lacks block extraction + a disposition leg" | policy text vs tool split: the tool does block extraction; the policy prose still prescribes single-line extraction (`R01-43-5`, `R01-43-review.md:144-146`) | mixed | not counted |
| "the single wrapped couples field reads 0/4 tokens" | extractor selftest: `PASS wrapped positive 4/4 tokens ['sound-change.md','sound-symbolism.md','tone-prosody.md','writing-systems.md']` | `count_eq`/capability | **false** |

The prototype at `.scratch/ca01/claims-freshness.py` measures this claim as
`STALE (0/2 premises hold)` — both declared checks false.

### 2.2 Claim C (`reports/round-43/claims.json:40`)

| clause as declared | measured at `7ceff59` | probe kind | verdict |
|---|---|---|---|
| "myth-symbol 26" | `git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol/ \| wc -l` → 26 | `count_eq` | true |
| "lithic slot named but unbuilt" | `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` present, sha `c99f44ca…`; topic line (:5) owns "the lithic register" | `topic_owner_absent` | **false** |
| "total 223" | `git ls-tree … corpus/knowledge \| grep -c '\.md$'` → 223 | `count_eq` | true |

Prototype: `STALE (2/3 premises hold)` — ownership is the failing clause, counts true.
Corroborated by `reports/round-43/validation.json` (`lithic_owner_exists: true`,
`lithic_owner_sha256: c99f44ca…`, `myth_symbol: 26`, `total: 223`) and
`reports/round-44/review/R01-review.md:237`.

### 2.3 Claim Ca — the in-file negative control (`reports/round-43/claims.json:53`)

| clause as declared | measured at `7ceff59` | probe kind | verdict |
|---|---|---|---|
| "no per-finding disposition on record" | `git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/` → no output (directory absent from the commit) | `path_absent` | true |

Prototype: `FRESH (1/1)`. This is why the same gate that flags O and C must leave Ca
untouched; the r43 Ca claim passed (`reports/round-43/validation.json`, verdict
`improved`), even though the round overall was rejected-honest-stop on O+C.

### 2.4 The exact commands and outputs this seat ran

```
$ git ls-tree -r --name-only 7ceff59 -- tools/harness/
tools/harness/couples-reference-extractor.py
tools/harness/packet_links.py
tools/harness/packet_uncertainty.py
tools/harness/r8_checks.py
tools/harness/receipt_guard.py
tools/harness/receipt_guard_adoption.py
tools/harness/round_runner_conformance.py

$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -

$ sha256sum tools/harness/couples-reference-extractor.py       # HEAD bytes == baseline bytes
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  tools/harness/couples-reference-extractor.py

$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
... (8 PASS lines total)
rc=0

$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'
223

$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol/ | wc -l
26

$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | grep -n '^- topic:'
5:- topic: the lithic register of a fictional culture's symbolic grammar — …

$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -

$ git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/
(no output)

$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
[O]  STALE (0/2 premises hold)
[C]  STALE (2/3 premises hold)
[Ca] FRESH (1/1 premises hold)
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
REFUSE: claims O, C have a `before` already false at 7ceff59…; do not dispatch.
rc=2

$ python3 -B .scratch/ca01/claims-freshness.py --selftest
...
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL          # rc=1
```

The `.scratch` prototype is 34,038 bytes, sha256
`dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434`, and is
**non-durable by construction**. Its run is cited as method evidence only, never as the
fix.

## 3. Class boundary — r44 is not silently counted, and is not silently dropped

`reports/round-46/loop-1-retrospective.md:47-48` says "The stale-premises pattern (claims
not re-measured at baseline): r43 and r44 both hit it", and `reports/round-47/claims.json:40`
inherits that grouping ("r43 and r44 both declared claims on stale premises (green
resolver existed; owned/carried topics)").

Measured against r44's own file at `c9f4eaa`, the narrow reading does **not** reproduce:

| r44 claim | `before` as declared | measured at `c9f4eaa` | narrow verdict |
|---|---|---|---|
| O (`reports/round-44/claims.json:27`) | "no four-class census authority exists" | true — the four-class authority was still a draft (r43 O09), landed only by r44 O | fresh |
| C (`:40`) | "total 223; the r43 lithic claim was blocked …" | true — no ownership/absence assertion in the `before` field | fresh |
| Ca (`:52`) | "no mechanical pre-dispatch freshness check exists" | true — `ls tools/harness/claims-freshness.py` → absent at `c9f4eaa` | fresh |

r44's actual C defect was in the **claim body**: it asserted a gap "not carried from a
prior round" while the dream candidate had been proposed at
`reports/round-42/scout/K02-myth-gaps.md:216` (R2). `reports/round-44/review/R02-review.md:441`
explicitly rules that "outside R01-43-12's stale-premise class" — it is a carried-candidate
defect, one class over. Its Ca defect was **delivery** (no durable gate: r44
`validation.json` → `durable_gate_exists: false`, verdict `unprovable-but-better`), also
outside this class.

Recorded incidence for this row:

- **narrow (`before` field):** r43 only — claims O and C, 2 claims / 1 round.
- **broad (claim text):** r43 O, r43 C, r44 C — 3 claims / 2 rounds. Do **not** count r44
  Ca (true premise, failed delivery).
- The divergence is a `to-verify` for the integrator: the r47 O claim's `before` uses the
  broad grouping, but its `after_required` tests the narrow contract. That is acceptable
  only if the gate's r44 leg is described as `could-not-evaluate`/adjacent-class, never as
  a STALE catch from a true `before`.

No filed byte is edited by this note; the retrospective and r44 claims stand as filed.

## 4. Routing — the r47 O freshness gate

The row's owner is the r47 O claim, not this seat. What the O claim must deliver is
specified at `reports/round-44/review/R01-review.md:243-250` (six-part contract) and
restated operationally at `reports/round-47/claims.json:39-47`. The acceptance points that
bear on **this** row:

1. `tools/harness/claims-freshness.py` durable (not `.scratch`), reading
   `git show`/`ls-tree` at the claim's `baseline_commit` — never the worktree.
2. Typed probes with **declared polarity** per clause
   (`path_absent|path_present|grep_absent|grep_present|count_eq|sha256_eq|topic_owner_absent|capability_present`,
   or a superset with the same semantics). Polarity is the trap the r44 reviewer hit
   first-hand: encoding "resolver exists = true" for a claim that asserts absence marks a
   stale premise FRESH (`R01-review.md:239`).
3. `STALE` if any declared clause mismatches; `FRESH` only if all match;
   `could-not-evaluate` when no checks are declared and it must **not** exit 0.
4. The r43 positive regression: O `STALE`, C `STALE`, Ca `FRESH`, non-zero exit.
5. A true-`before` negative control not flagged (r44 O/C/Ca at `c9f4eaa` are usable
   negatives on the narrow reading, per §3).
6. Anti-theater mutation: rename the r43 O tool to the existing witness
   (`couples-reference-extractor.py`) and replace C's literals with live values; both must
   still flag from capability/ownership, not literal text.

Known prototype traps the durable tool must close (carried verbatim from r44):

- **T1 polarity** — `R01-review.md:239`.
- **T2 novel-phrasing false positive** — "the llama-herding register slot is unbuilt"
  mines topic `register` and refuses against 51 owners (`R02-review.md:203-227,428-434`).
  Multi-word topic capture or `unverifiable` on a stop-word topic is required.
- **T3 family-scan false candidates** — `tools/gates/provenance-audit.py` counted as a
  couples-family candidate because its prose mentions a missing `- couples:` header
  (`R02-review.md:435-439`); label candidates by file role or exclude gates.
- **T4 red selftest** — the prototype is 17/19, exit 1 (`FAIL grep_absent` fixture;
  `FAIL seventeen checks collected (18)`; `R02-review.md:212-227`). A green selftest with a
  count the run itself produces is required.
- **T5 class over-claim** — the gate checks ownership/counts, not prior proposals; it
  cannot close the carried-candidate class (`R02-review.md:440-443`). The O claim must not
  present it as doing so.

## 5. Fenced successor row

Schema-compatible with `reports/round-43/calib/defect-queue-v2-successor-r43.json`
(`id`, `origin`, `class`, `v2_class_equivalent`, `owner`, `reason`, `next_touch`,
`evidence`, `verification`). Ca06 copies this object verbatim; extra fields
(`class_boundary`, `incidence`, `reclass_gates`) are additive and may be dropped if the
successor schema rejects them, provided §§3-4 of this artifact are cited.

```json
{
  "id": "r43-stale-premises",
  "origin": "r43 R01-review.md:400 (R01-43-12: 'The claim texts were not re-measured at 7ceff59 before dispatch'); carried at reports/round-46/loop-1-retrospective.md:45-48 and :39-41; re-declared as the fix target at reports/round-47/claims.json:39-47 (claim O) and reports/round-44/claims.json:51-57 (the failed r44 Ca predecessor, validation verdict unprovable-but-better). Dedupe aliases: R01-43-12, r44-Ca-predecessor, r47-O-before.",
  "class": "routed-with-owner",
  "v2_class_equivalent": "carried-with-owner",
  "owner": "r47 O claim (freshness-gate author) + r47 integrator (applies tools/harness/claims-freshness.py); this row is not owned by Ca01 and no resolver/policy body is touched",
  "reason": "The class is confirmed by direct measurement at the r43 baseline 7ceff59, on committed bytes rather than the worktree. Claim O's before (reports/round-43/claims.json:27) asserts no durable couples instrument and a 0/4 wrapped read; at 7ceff59 tools/harness/couples-reference-extractor.py is tracked at sha256 d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1, selftests 8/8 exit 0, and reads the wrapped field 4/4 - both conjuncts false (the prototype scores O STALE 0/2). Claim C's before (:40) asserts the lithic slot is 'named but unbuilt'; corpus/knowledge/myth-symbol/mineral-stone-symbolism.md exists at sha256 c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f and its topic line (:5) owns the register, so ownership is false while the counts 26/223 are true (STALE 2/3; r43 validation blocked-by-topic-collision). The same file's Ca claim (reports/round-43/claims.json:53) is TRUE at 7ceff59 - reports/round-43/calib/ is absent from the commit - so a correct gate leaves it FRESH (1/1); the r43 Ca claim passed (improved) even though the round was rejected on O+C. No durable pre-dispatch check exists at HEAD 6e9a30d: ls tools/harness/claims-freshness.py exits 2, and the only working implementation is the non-durable .scratch prototype (34038 bytes, sha256 dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434) whose --selftest is red at 17/19 exit 1. The defect therefore stays open; routing to r47 O is the disposition, and the reclass condition is defined in reclass_gates, not asserted here.",
  "next_touch": "r47 O applies tools/harness/claims-freshness.py and files the demonstration at reports/round-47/calib/; this row reclasses to fixed-with-evidence only when all of reclass_gates G1-G7 pass on the integrated tool, each with its command output pasted into the successor artifact or the r47 validation. Until then the row stays routed-with-owner. The r44 instance is NOT part of the narrow incidence: r44 O/C/Ca before-fields are true at c9f4eaa, and R02-review.md:441 rules r44's carried-proposal defect outside R01-43-12; a gate run over r44 must report the bolt, not a stale catch.",
  "evidence": "reports/round-43/claims.json:27 (O before), :40 (C before), :53 (Ca before, the in-file negative); reports/round-43/review/R01-review.md:400 (R01-43-12) and :346-350 (Ca verdict); reports/round-43/validation.json (O failed-as-declared with existing_extractor_sha256 d8d23a26..., existing_selftest_pass 8; C blocked-by-topic-collision with lithic_owner_sha256 c99f44ca..., myth_symbol 26, total 223; Ca improved); reports/round-44/review/R01-review.md:212-260 (six-part durable contract at :243-250, polarity at :239, prototype 17/19 at :241) and :299 (R01-44-14); reports/round-44/review/R02-review.md:203-227,428-443 (novel-phrasing false positive; family-scan false candidates; carried-candidate outside this class); reports/round-44/validation.json (Ca unprovable-but-better, durable_gate_exists false); reports/round-44/claims.json:51-57 (the predecessor claim); reports/round-46/loop-1-retrospective.md:43-54 (carried defects) and :39-41 (honest stops); reports/round-47/claims.json:37-47 (the r47 O fix target); LOG.md:3841-3842 (r43 process-defect record; the stale before sentences did not enter LOG - SHONEN.md carries none either); SCORECARD.md:847-848,865 (loop-1 calibration verdict); parent pin reports/round-40/op/defect-queue-v2.json sha256 dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907, also pinned at reports/round-43/calib/defect-queue-v2-successor-r43.json:7.",
  "verification": "Commands run by this seat at 6e9a30d, 2026-10-19, all against committed bytes: (1) git ls-tree -r --name-only 7ceff59 -- tools/harness/ -> couples-reference-extractor.py present; (2) git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum -> d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1, identical to the HEAD file's sha256sum; (3) python3 -B tools/harness/couples-reference-extractor.py --selftest -> 8 PASS, rc 0, including 'PASS wrapped positive 4/4 tokens'; (4) git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\\.md$' -> 223; (5) git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol/ | wc -l -> 26; (6) git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | grep -n '^- topic:' -> :5 owns 'the lithic register'; sha256 -> c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f; (7) git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/ -> no output (Ca's premise true); (8) python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json -> O STALE (0/2), C STALE (2/3), Ca FRESH (1/1), exit 2; (9) python3 -B .scratch/ca01/claims-freshness.py --selftest -> 17 ok / 2 FAIL, exit 1 (the non-durable prototype, cited as method evidence only); (10) ls tools/harness/claims-freshness.py -> No such file or directory, exit 2 (the row is open at seat cut).",
  "class_boundary": "Narrow reading (before-field clauses) incidence is r43 O + r43 C = 2 claims / 1 round. Broad reading (claim text) adds r44 C's 'not carried from a prior round' clause (prior proposal at reports/round-42/scout/K02-myth-gaps.md:216) = 3 claims / 2 rounds; r44's before fields are true at c9f4eaa and r44 Ca is a delivery failure, not a stale premise. reports/round-46/loop-1-retrospective.md:47-48 and reports/round-47/claims.json:40 use the broad grouping; reports/round-44/review/R02-review.md:441 uses the narrow one. The integrator should read this row's incidence under the narrow definition and treat the broad r44 instance as the adjacent carried-candidate row, not a second stale-premises fix target.",
  "incidence": {
    "narrow": {"rounds": [43], "claims": ["O", "C"], "count": 2},
    "broad": {"rounds": [43, 44], "claims": ["O", "C", "C-body"], "count": 3},
    "excluded": {"round": 44, "claim": "Ca", "reason": "before true at c9f4eaa; failure was delivery (durable_gate_exists false), not a stale premise"}
  },
  "reclass_gates": [
    "G1 durable path: tools/harness/claims-freshness.py exists after integration with a recorded sha256; not .scratch.",
    "G2 green selftest: --selftest exits 0 and the asserted control count equals the controls actually run (the prototype's 17-vs-18 stale assertion must not recur).",
    "G3 positive regression: --claims reports/round-43/claims.json flags O and C STALE, leaves Ca FRESH, and exits non-zero; the demonstration quotes the tool's actual exit codes.",
    "G4 negative control: a claim whose before is true at its baseline (r44 O/C/Ca at c9f4eaa is a usable narrow set) is not flagged and exits 0.",
    "G5 anti-theater: with r43 O's tool name mutated to couples-reference-extractor.py and C's literals replaced by live values, both still flag from capability/ownership, not literal text.",
    "G6 baseline evaluation: a clause true in the worktree but false at baseline_commit must flag (git show/ls-tree, never the worktree).",
    "G7 could-not-evaluate is not green: a claims.json with no declared checks exits non-zero; malformed input exits 2 per the documented contract."
  ]
}
```

## 6. Reclass rule (for Ca05 / Ca06 / Ca07)

The row must remain `routed-with-owner` unless **every** gate G1-G7 passes with a filed
command output. In particular:

- A green module-import or a green `--help` is not G2.
- A demonstration that hardcodes "r43 O contains the string 'no durable instrument'" is
  not G5.
- A run against the worktree instead of `7ceff59` is not G3 (the current worktree still
  reads 223 entries and the same extractor bytes, so a worktree run can look right for the
  wrong reason).
- The reeval command after integration is:

```
python3 tools/harness/claims-freshness.py --selftest
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json   # expect O,C STALE; Ca FRESH; rc != 0
sha256sum tools/harness/claims-freshness.py reports/round-40/op/defect-queue-v2.json
```

## 7. Boundary and provenance

Only `reports/round-47/calib/Ca01-stale-premises.md` was written. No filed byte
(`reports/round-1..46/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, `.ufo/**`) was
edited or staged. The parent queue was read and sha-checked, not touched. No round runner
was executed; no corpus staging; no git mutation, network, or install. Scratch use was
limited to `.scratch/ca01/` (pre-existing prototype, read-only) and to capturing command
output.

`to-verify` (named, not guessed):

- Whether the integrator adopts the narrow or broad reading for the successor's
  `incidence` field; §3 carries both with evidence and no silent choice.
- The r47 O tool's exit-code contract at integration (the r44 prototype used 2 for stale;
  R01-44 §4.3 proposed 1). G3 accepts either only if the demonstration quotes the actual
  codes and stale is non-zero.
- `.scratch/ca01/claims-freshness.py` is ephemeral; if it is removed before integration,
  the durable evidence for the method remains the r44 review citations in §4, and the
  prototype digest in the row is a seat-time measurement.
