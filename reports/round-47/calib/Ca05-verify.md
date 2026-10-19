# Ca05 — independent verification of the loop-1 reconciliation rows (claim Ca)

- Seat: `Ca05` (claim **Ca**, calibration) | role: verifier (non-author)
- Out: `reports/round-47/calib/Ca05-verify.md` (the only write by this seat)
- Baseline: `6e9a30d` (`git rev-parse HEAD` -> `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`)
- Observation window: 2026-10-19T17:55Z–18:06Z. Rows landed and were revised during
  the window; the verdict is **digest-bound** to the four sha256 values in §0.
- Method: every fact was re-measured by this seat from the worktree, from
  `git show`/`ls-tree` at the named commits, or from the fleet ledger. No row
  author's output was trusted as a premise. The full command set is in §7.

Verdict scope: Ca01–Ca04's rows are checked for (a) class correctness, (b) real,
resolving evidence, (c) no filed byte edited, and (d) the parent
`defect-queue-v2.json` pin. All four rows are now filed and are verified below.
A 17:58Z draft of this artifact marked Ca01/Ca03/Ca04 absent; the §0 table and
§6 block below are the final all-rows-verified snapshot, superseding that draft
and the corresponding note in Ca06's assembly.

## 0. Verdict summary

| row | class in the row | class verdict | row digest verified (sha256) | verdict |
|---|---|---|---|---|
| Ca01 — `R01-43-12` stale-premises | `routed-with-owner` | correct; refuses `fixed` until the gate lands and G1–G7 pass | `e0e51e5600a1537f425c2d8f20ea68937e42c6c01b78c14d8d25580cce52ce3c` | **PASS** |
| Ca02 — resolver hyphen-after-blank | `recorded` | correct; pinned body, 0/223 live, no fix claimed | `91cd4484b780ef823304d2c8b85c462a7131c336c73ad446d440138a1f01276c` | **PASS** (N1 minor) |
| Ca03 — two MANIFEST ledger schemas | `recorded` | correct; S1 33–42 and S2 43/44/46 both documented | `a2e61cdba8180e25fb81a9f4bb23dbb677011e2de98d8d341e6c9eb321cd70a6` | **PASS** (N2 minor) |
| Ca04 — antigravity + zai amendments | `named-deviation` (declared extension) | acceptable as a non-defect provider record; must stay out of the defect count | `94b99878a31ae6aa8c376fa35af786e36d07f3210c9f368f9a014f4a4ac2136e` | **PASS with F6** |
| parent pin | `dfc9265d…` | unchanged at `ac47c78` and `6e9a30d`, matches the r43 pin | n/a | **PASS** |
| filed-byte integrity | no tracked edit | `git diff` and `git diff --cached` empty | n/a | **PASS** |

## 1. Independent re-measurement of the five carried items

### 1.1 Stale-premises defect `R01-43-12` (Ca01)

The defect is filed at `reports/round-43/review/R01-review.md:400`. Both stale
`before` sentences reproduce as false at `7ceff59`:

| r43 claim | `before` | measured at `7ceff59` | verdict |
|---|---|---|---|
| O | `reports/round-43/claims.json:27` — "no durable instrument implements the r39 basename-couples policy … the single wrapped couples field reads 0/4 tokens" | `tools/harness/couples-reference-extractor.py` tracked, blob sha256 `d8d23a26…` (identical to HEAD), selftest 8/8 exit 0, reads the wrapped field 4/4; `--census` -> `entries=223 refs=2730` | **stale: false before** |
| C | `reports/round-43/claims.json:40` — "myth-symbol 26 (lithic slot named but unbuilt …); total 223" | `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at `7ceff59`, sha256 `c99f44ca…`; its `- topic:` line (`:5`) owns "the lithic register"; counts 223 total / 26 myth-symbol | **stale: ownership false; counts true** |
| Ca | `reports/round-43/claims.json:53` — no per-finding disposition on record | `git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/` -> no output (directory absent) | **fresh: negative control holds** |

Commands run: `git ls-tree` at `7ceff59`; `git show 7ceff59:... | sha256sum`;
`--selftest` (8 PASS lines); `--census`; and the r43 `validation.json` cross-check
(`existing_selftest_pass=8`, `lithic_owner_sha256=c99f44ca…`, `myth_symbol=26`,
`total=223`).

**Scope correction, now adopted by Ca01.** The retrospective's "r43 and r44 both
hit it" (`reports/round-46/loop-1-retrospective.md:47-48`) is true only under a
broad reading that includes carried *proposals*. r44's O `before` was true and
the claim landed (`MANIFEST.json:4990`, `O: improved`); r44's C failure was a
carried-candidate defect, explicitly ruled outside `R01-43-12` at
`reports/round-44/review/R02-review.md:441`. The r47 O claim's `before` uses the
broad grouping while its `after_required` tests the narrow contract. Ca01's row
records both readings with measured incidence (narrow: r43 O+C = 2 claims/1
round; broad: + r44 C = 3 claims/2 rounds) and instructs that r44 not be counted
as a stale catch. That is the correct disposition.

**Class timing.** `tools/harness/claims-freshness.py` is still absent at this
seat's final observation (`ls` -> "No such file or directory"). Until the durable
tool lands **and** a filed demonstration shows O/C STALE and Ca FRESH with a
quoted non-zero exit, `routed-with-owner` is the only defensible class. Ca01's
G1–G7 reclass gates state this; the row must not be upgraded on tool existence
alone.

### 1.2 Resolver latent edge (Ca02)

Live body `tools/harness/basename-couples-resolver.py`, sha256 `43ce341f…`:

- `:55-59` docstring promises a blank-line exception for a trailing-hyphen soft
  wrap; `:73` gates `soft_wrap` on `not saw_blank`; `:74`'s second disjunct is
  therefore unreachable. The documented exception cannot fire.
- Independent fixture run (this seat): `couples_block` -> `['language — \`tone-']`,
  `couples_field` -> `'language — \`tone-'`, `field_refs` -> `set()`. The r42
  witness on the same fixture -> `wrapped=True tokens=2` (`tone-prosody.md`
  unresolved, `writing-systems.md` fallback).
- Live incidence: independent scan of all 223 entries -> **0**. Ca02's inlined
  scanner also returns `live hits: 0` and `positive-control hits: 1` on its
  `.scratch/ca02-r47/positive/` fixture, so the zero is a measured zero.
- Selftest: `SELFTEST OK: 27/27 controls`, exit 0.
- Control coverage: S2b (`:359`) is a non-blank hyphen wrap; S7c (`:411-415`) is
  a blank without a hyphen; no control combines blank + hyphen + indented
  continuation.

All fenced-row citations resolve: `R01-review.md:290`, `R02-review.md:468`,
`X01-trades.md:26,114-155`, `O03-defects-verify.md:221-229`, retrospective
`:49-50`, `O10-census-verify.md:95`, body `:359` and `:411-415`.

### 1.3 Two MANIFEST ledger schemas (Ca03)

At the ledger digest Ca03 pinned, `sha256 509305c8…` (293,641 bytes, 281 rows —
this seat re-read the same digest), the split reproduces:

- **S1, closure rows 33–42** (`MANIFEST.json:4241`-`4806`): 10 kotodama rows,
  11 keys, `type: "closure"`, `lanes`, `lane_rounds`, `admitted`, `verdicts`,
  `notes`; `lane_rounds.kotodama == round` for 10/10; admitted 8 true / 2 false
  (r36, r42).
- **S2, lane close-receipt rows 43, 44, 46** (`MANIFEST.json:4860,4979,5030`):
  15 keys, flat `lane`, `position`, `provider`, `model`, `verdict`, `claims`,
  `baseline_commit`, `close_commit`, `receipt`; no `date`/`closed_at`/`type`/
  `lanes`/`verdicts`; claims key sets `{O,C,Ca}` at 43/44 and `{A,O,Ca}` at 46.
- Duplicate round numbers 37–42 exist because kotodama and kotoba each carry a
  closure row; the array is append-ordered, not sorted. A first-match lookup by
  round is ambiguous.
- Mechanical reconciliation (this seat, not trusted from the audit): for rounds
  33–44, lane receipt verdict/admission equals the fleet row -> 8 admitted / 2
  rejected / 2 honest-stop, zero disagreements.

Ca03's scope qualifier is correct: the r46 audit's "per-lane 43-44"
(`reports/round-46/audit/Ca01-manifest.md:7-8,28-32`) is the audited window
33–44; at HEAD r46 is also per-lane. Ca03 includes it. Its provenance correction
also checks out: the retrospective's five carried bullets
(`reports/round-46/loop-1-retrospective.md:43-53`) do not name the MANIFEST
schemas; the item originates in the r46 Ca01 audit.

### 1.4 Provider amendments (Ca04)

**Antigravity.** Position 12 scheduled `antigravity/gemini-3.8-flash`; it aborted
twice with zero output and was re-routed to
`opencode-go/deepseek-v4.1-flash`, where it **executed** 32 launches / 14
completions / 18 unrelated `reasoning_content` failures
(`reports/round-44/telemetry/dispatch-declared.json:10,17`;
`observed-dispatch.json:17-18`; `availability-close-44.json:25-27`; round 44
exists with `filed: 14`, `verdict: rejected-honest-stop`). Position 13 was
**skipped**: `reports/round-45/` does not exist and
`git log --all --grep='round 45' -i | wc -l` -> 0; the r46 ledger note records
"Position 13 (argon) skipped per operator ruling"
(`MANIFEST.json:5047`). Ca04's §3 wording correction (12 re-routed and executed,
13 skipped) is the measured statement.

**zai.** `zai usage exhausted — zai seats route to openai-codex/gpt-6-luna-max
for the session` (`reports/round-46/loop-1-retrospective.md:53`; restated as the
standing r47 amendment at `reports/round-47/telemetry/dispatch-declared.json:18`;
first amendment record at `reports/round-46/telemetry/dispatch-declared.json:16`).
The loop-2 schedule applies it to positions 7–8 and 11 (r53, r54, r57;
`reports/round-46/loop-1-retrospective.md:59`). The r43 route history shows zai
interrupted x2, then antigravity and cursor interruptions, then opencode-go
(`reports/round-43/telemetry/availability-close-43.json:26`;
`observed-dispatch.json:20`). Ca04 correctly keeps "exhausted" (retrospective)
separate from "interrupted" (telemetry) and marks the cause `to-verify`.

Every sha256 in Ca04's source table matches this seat's `sha256sum` run
(retrospective `a8e3fabb…`, r44 telemetry `565e4fbd…`/`445daadf…`/`8a9146e1…`,
r43 telemetry `76632d73…`/`10181657…`/`eddfb5f3…`, r47 dispatch `3d826369…`,
parent `dfc9265d…`).

### 1.5 Parent defect queue — pinned and unchanged

```
sha256sum reports/round-40/op/defect-queue-v2.json
  -> dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
git show 6e9a30d:reports/round-40/op/defect-queue-v2.json | sha256sum  -> same
git show ac47c78:reports/round-40/op/defect-queue-v2.json | sha256sum  -> same
git show 13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum
  -> fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98 (recorded pre-r41)
```

This matches the pin at `reports/round-43/calib/defect-queue-v2-successor-r43.json:7`.
History is two commits (`13a1657`, `ac47c78`); the r41 in-place amendment is the
recorded supersession. The parent has 38 rows (28 `carried-with-owner`, 10
`fixed-with-evidence`), matching Ca04's `parent_defect_row_count_at_assembly: 38`.

## 2. Row-by-row verdicts

### Ca01 — PASS (digest `e0e51e56…`)

- **Class:** `routed-with-owner`, correct. The row states no fix and routes to
  the r47 O claim; its G1–G7 reclass gates require the durable tool, a green
  selftest with an honest count, the r43 positive regression, a negative
  control, an anti-theater mutation, baseline evaluation, and
  `could-not-evaluate != green`. The row does not claim the gate exists.
- **Evidence:** every cited line/sha re-measured true, including the `.scratch`
  prototype: `--claims` -> O STALE (0/2), C STALE (2/3), Ca FRESH (1/1), exit 2;
  `--selftest` -> 17/19, **exit 1** (this seat confirmed the rc, not just the
  text). The prototype's digest `dd88d9e1…` and size 34,038 bytes match.
- **Boundary:** the narrow/broad incidence split is honest and the r44 exclusion
  is correct (§1.1).
- **No filed byte edited; parent pinned.**

### Ca02 — PASS (digest `91cd4484…`), minor N1

- **Class:** `recorded`, correct. The body is pinned, the exception is
  unreachable, live incidence is 0/223, and the next touch is advisory.
- **Evidence:** all citations resolve; the fixture reproduces through
  `couples_block`/`couples_field`/`field_refs`; the witness returns 2 tokens; the
  scanner's positive control returns 1 hit, so the live zero is not a blind
  scanner.
- **N1 (minor):** the r43 vocabulary maps `recorded` -> `carried-with-owner` with
  `next_touch: "none - recorded"`; Ca02 supplies a non-empty advisory next touch.
  `class` is authoritative and the advisory touch is more useful, so this is not
  a defect; Ca06 should keep `recorded` and must not reclass it
  `fixed-with-evidence`.
- **No filed byte edited; parent pinned.**

### Ca03 — PASS (digest `a2e61cdb…`), minor N2

- **Class:** `recorded`, correct. No defect is claimed; the row documents the two
  contracts, the consumer traps, and the `to-verify` protocol-shape divergence.
- **Evidence:** the pinned ledger digest `509305c8…` matches this seat's read
  (281 rows, 293,641 bytes); S1/S2 key sets, rounds, admitted counts, duplicate
  rows, and claims key sets all reproduce; `reports/round-46/run-validation.py:94-97,107-110`
  keys S1 by `lane_rounds` and S2 by `round`; `PROTOCOL.md:194-196,237-243,283-290`
  and `PROTOCOL-APPENDIX.md:37` resolve in the fleet root and say what the row
  says.
- **N2 (minor):** `PROTOCOL.md`/`PROTOCOL-APPENDIX.md` are fleet-root files, but
  the artifact cites them as bare names. The lane repo has no such files; a
  lane-root reader gets ENOENT. Qualify them as fleet-root-relative like
  `MANIFEST.json` (the artifact already does this for the ledger).
- **Lead-time observation:** the row's earlier-read digest (`19ddec8b…`, 280
  rows) is not recoverable by this seat; the pinned digest is the reproducible
  state. Not material to the claim.
- **No filed byte edited; parent pinned.**

### Ca04 — PASS with F6 (digest `94b99878…`)

Re-parsed at this final digest (the one Ca06 pins): 2 provider rows, 7/6 evidence
entries, `named-deviation`, `defect_row: false`, parent pin `dfc9265d…`, and the
same F6 sentence. The seat revised the file during the wave; the row semantics
did not change, so the checks below apply to the final bytes.

- **Class:** `named-deviation`, a declared extension outside the four-class defect
  vocabulary. The mission asks for "named deviations", and the parent queue's own
  notes exclude telemetry deviations from defect rows
  (`reports/round-40/op/defect-queue-v2.json:8`). Acceptable **only** as a
  non-defect record: Ca06 must keep it in a top-level `provider_amendments[]`
  (preferred) or a `kind`-tagged row, not merge it into `rows[]` without the
  marker, or the defect census inflates by two.
- **Evidence:** the 9 source digests match; the antigravity and zai facts verify;
  the 12/13 wording correction is measured; r45 absence is measured.
- **F6 (should-fix):** the row's `verification` says "no dispatch-declared.json at
  r44, r46 or r47 names zai (lanes: opencode-go, devin, opencode-go)". That is
  false in its literal reading: the r46 notes say "zai usage exhausted"
  (`reports/round-46/telemetry/dispatch-declared.json:16`) and the r47 notes say
  "zai->luna-max all session" (`reports/round-47/telemetry/dispatch-declared.json:18`,
  which the same row cites as evidence). The intended and true statement is
  "none of those rounds dispatched **on** zai; the amendment appears only in the
  notes". Scope the sentence to the `provider_lane`/`model` fields.
- **No filed byte edited; parent pinned.**

## 3. Filed-byte and write-surface integrity

- `git diff --name-only` and `git diff --cached --name-only` -> empty.
- `git status --porcelain` -> only `?? reports/round-46/review/` and
  `?? reports/round-47/`. No tracked filed byte is modified.
- `find corpus/knowledge -name '*.md' | wc -l` -> 223;
  `ls corpus/knowledge/culture-material/*.md | wc -l` -> 25. No corpus delta
  from any Ca seat.
- **F5 (observation, outside the claim):** `reports/round-46/review/R01-review.md`
  is untracked, mtime 2026-10-19 14:48, and is cited by Ca03 as a source. It is
  not an edit of tracked bytes, but it is a write-surface anomaly: an r46 review
  fragment never committed. `A03`'s census should classify it; no seat should
  edit or delete it.

## 4. Findings

| id | status | finding | action |
|---|---|---|---|
| F1 | **resolved in Ca03** | The schema boundary needed r46 (also per-lane at HEAD), not just 43–44. | Ca03's S2 covers 43/44/46 and says r46 extends the audit's window. No action. |
| F2 | **resolved in Ca04** | "Positions 12/13 skipped" was imprecise. | Ca04 §3 and the row's `wording_correction` state 12 re-routed/executed, 13 skipped. No action. |
| F3 | **resolved in Ca01** | "r43 and r44 both stale premises" overstates the narrow evidence. | Ca01 §3 carries narrow and broad incidence and excludes r44 Ca; r44 C is the adjacent carried-candidate class. No action. |
| F4 | **resolved in Ca01** | A `fixed-with-evidence` class would be premature while the gate is absent. | Ca01 is `routed-with-owner` with G1–G7 reclass gates. Keep it until the outputs land. |
| F5 | open observation | Untracked `reports/round-46/review/R01-review.md`. | A03 classify; do not edit. |
| F6 | **remaining, should-fix** | Ca04's "no dispatch-declared … names zai" sentence is false for r46/r47 notes; the true point is the dispatch lane, not the notes. | Ca04 or Ca06 scopes the sentence to `provider_lane`/`model`; no other evidence changes. |
| F7 | process note | Ca01, Ca03, Ca04 were revised after first landing (mtimes 14:56→15:04; digests changed). Ca04's final digest at this check is `94b99878…`, which Ca06's `source_fragments` pins; Ca06's snapshot of this artifact is an earlier Ca05 write. | If a row digest differs from §0 at assembly, re-run the relevant Ca05 checks; do not assume this verdict covers later bytes. Ca07 re-verifies the applied successor anyway. |

No finding alleges fabrication. Every substantive number re-measured here
reproduced; F6 is a wording overclaim in one verification sentence, not false
domain evidence.

## 5. Acceptance rules for Ca06 (binding on assembly)

1. One row per carried item, zero silently dropped. The mapping verified here:
   Ca01 -> stale-premises `R01-43-12`; Ca02 -> resolver latent edge; Ca03 ->
   MANIFEST schemas; Ca04 -> antigravity + zai (two non-defect provider records).
2. Keep the classes: Ca01 `routed-with-owner`; Ca02 `recorded`; Ca03 `recorded`;
   Ca04 `named-deviation` in a separate `provider_amendments[]` (or a
   `kind`-tagged row). Do not count the provider amendments as defects.
3. Do not upgrade Ca01 to `fixed-with-evidence` unless the durable
   `tools/harness/claims-freshness.py` exists and G1–G7 each have pasted command
   output (r43 O/C STALE, Ca FRESH, non-zero exit; a true-before negative
   control; an anti-theater mutation; baseline evaluation; malformed/no-check
   exits). The tool is absent at this seat's cut.
4. Preserve the parent pin `dfc9265d…`; the parent stays byte-identical.
5. Re-run `sha256sum` on the parent after assembly and record the output. If any
   source-row digest differs from §0, re-verify before merging (F7).
6. The successor is a new artifact; no filed byte, `corpus/`, or `tools/` change
   is made by Ca seats.

## 6. Machine-readable verification block

```json
{
  "seat": "Ca05",
  "claim": "Ca",
  "baseline_commit": "6e9a30d",
  "observed_window_utc": ["2026-10-19T17:55Z", "2026-10-19T18:04Z"],
  "parent_queue": {
    "path": "reports/round-40/op/defect-queue-v2.json",
    "sha256": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
    "matches_r43_pin": true,
    "matches_head": true,
    "matches_ac47c78": true,
    "rows": 38
  },
  "rows": {
    "Ca01": {
      "row_file": "reports/round-47/calib/Ca01-stale-premises.md",
      "row_sha256": "e0e51e5600a1537f425c2d8f20ea68937e42c6c01b78c14d8d25580cce52ce3c",
      "status": "pass",
      "class": "routed-with-owner",
      "class_ok": true,
      "evidence_resolves": true,
      "incidence": {"narrow": {"claims": ["O", "C"], "rounds": [43], "count": 2}, "broad": {"claims": ["O", "C", "C-body"], "rounds": [43, 44], "count": 3}},
      "reclass_requires": "G1-G7 with pasted outputs; tool absent at cut",
      "findings": []
    },
    "Ca02": {
      "row_file": "reports/round-47/calib/Ca02-resolver-edge.md",
      "row_sha256": "91cd4484b780ef823304d2c8b85c462a7131c336c73ad446d440138a1f01276c",
      "status": "pass",
      "class": "recorded",
      "class_ok": true,
      "evidence_resolves": true,
      "live_incidence": 0,
      "positive_control": 1,
      "selftest": "27/27",
      "findings": ["N1-minor"]
    },
    "Ca03": {
      "row_file": "reports/round-47/calib/Ca03-manifest-schemas.md",
      "row_sha256": "a2e61cdba8180e25fb81a9f4bb23dbb677011e2de98d8d341e6c9eb321cd70a6",
      "status": "pass",
      "class": "recorded",
      "class_ok": true,
      "evidence_resolves": true,
      "ledger_sha256": "509305c8b95e5e732b26b59a5874e31f4c368afcba0193a10443023073724e32",
      "schemas": {"S1": [33, 34, 35, 36, 37, 38, 39, 40, 41, 42], "S2": [43, 44, 46]},
      "reconciliation": {"admitted": 8, "rejected": 2, "honest_stop": 2, "disagreements": 0},
      "findings": ["N2-minor"]
    },
    "Ca04": {
      "row_file": "reports/round-47/calib/Ca04-provider-amendments.md",
      "row_sha256": "94b99878a31ae6aa8c376fa35af786e36d07f3210c9f368f9a014f4a4ac2136e",
      "status": "pass-with-finding",
      "class": "named-deviation",
      "class_ok": true,
      "class_note": "non-defect provider record; keep out of the defect count",
      "evidence_resolves": true,
      "antigravity": "pos 12 re-routed and executed; pos 13 skipped",
      "zai": "usage exhausted -> luna-max; pos 7-8 + 11 amendment",
      "findings": ["F6"]
    }
  },
  "filed_bytes": {"tracked_diff": false, "cached_diff": false, "untracked": ["reports/round-46/review/", "reports/round-47/"]},
  "corpus": {"total": 223, "culture_material": 25},
  "findings": ["F5", "F6", "F7"]
}
```

## 7. Provenance and boundary

Commands run (full set):

```
git rev-parse HEAD
git status --porcelain
git diff --name-only
git diff --cached --name-only
git log --oneline -- reports/round-40/op/defect-queue-v2.json
git show 6e9a30d:reports/round-40/op/defect-queue-v2.json | sha256sum
git show ac47c78:reports/round-40/op/defect-queue-v2.json | sha256sum
git show 13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum
git ls-tree -r --name-only 7ceff59 | grep -E 'couples-reference-extractor|basename-couples-resolver'
git ls-tree -r --name-only 7ceff59 | grep mineral-stone-symbolism
git ls-tree -r --name-only 7ceff59 | grep -c '^corpus/knowledge/.*\.md$'
git ls-tree -r --name-only 7ceff59 | grep -c '^corpus/knowledge/myth-symbol/.*\.md$'
git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/ | wc -l
git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
python3 tools/harness/couples-reference-extractor.py --selftest
python3 tools/harness/couples-reference-extractor.py --census
python3 tools/harness/basename-couples-resolver.py --selftest
python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
python3 -B .scratch/ca01/claims-freshness.py --selftest        # rc=1, 17/19
sha256sum tools/harness/basename-couples-resolver.py reports/round-40/op/defect-queue-v2.json
sha256sum reports/round-47/calib/Ca0{1,2,3,4}*.md
import resolver on .scratch/ca05/fixture.md (couples_block, couples_field, field_refs)
python3 tools/harness/couples-reference-extractor.py .scratch/ca05/fixture.md
scan corpus/knowledge/*/*.md for blank-separated indented continuation after trailing hyphen -> 0
python3 (Ca02 scanner: live 0, positive-control 1)
python3 (MANIFEST 33-44 reconciliation + schema census at ledger sha 509305c8…)
sha256sum of the nine Ca04 source files (all match)
json.loads on every fenced JSON block in Ca01-Ca04 (4/4 parse; 2 rows in Ca04)
```

Boundary: only `reports/round-47/calib/Ca05-verify.md` was written; the fixture
under `.scratch/ca05/` is ephemeral and inlined in §1.2. No filed byte was edited
or staged; no round runner was executed; no corpus staging; no git mutation,
network, or install.
