# Ca06 - loop-1 defect reconciliation: queue-successor assembly

- Seat: `Ca06` (claim **Ca**, calibration) | role: executor
- Out: `reports/round-47/calib/Ca06-queue-successor.md` (the only write by this seat)
- Baseline: `6e9a30d` (`git rev-parse --short HEAD` -> `6e9a30d`)
- Disposition: successor delta, **3 defect rows + 2 provider amendments**; parent
  `reports/round-40/op/defect-queue-v2.json` pinned at
  `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` and **not edited**.

## 1. What this artifact is

This is the durable loop-1 close the r47 Ca claim names: one successor record extending
the r40 `defect-queue-v2` (and its r43 successor), with one row per loop-1 carried item.
It is a **new artifact**: it edits no filed byte, stages nothing under `corpus/`, and
changes nothing under `tools/`. The defect rows for the stale-premises class, the
resolver latent edge, and the MANIFEST dual schema are parsed from the filed Ca01/Ca02/
Ca03 fenced blocks; the two provider amendments are parsed from Ca04's
`kotodama-provider-amendments-v1` block and copied into a top-level
`provider_amendments[]`, Ca04's preferred shape. Row field content is unchanged.

The provider amendments are **not defect rows** (`defect_row: false`), following the
parent queue's own practice (`reports/round-40/op/defect-queue-v2.json:8`: "Telemetry
deviations deliberately NOT defect rows (r37 practice: rule breaches only)"). Keeping
them in a separate array preserves the defect census: 38 parent rows + 3 disposition
rows, with the two amendments counted separately.

## 2. Assembly checks (measured, not asserted)

| check | command | output |
|---|---|---|
| lane HEAD | `git rev-parse --short HEAD` | `6e9a30d` |
| parent digest | `sha256sum reports/round-40/op/defect-queue-v2.json` | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` |
| parent unmodified | `git status --porcelain reports/round-40/op/defect-queue-v2.json` | empty |
| parent history | `git log --oneline -- <parent>` | `ac47c78`, `13a1657` (two commits; r41 in-place edit recorded) |
| parent rows | parse `rows[]` | 38 (28 carried-with-owner, 10 fixed-with-evidence) |
| predecessor successor | `sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json` | `77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38` |
| corpus total | `find corpus/knowledge -name '*.md' \| wc -l` | `223` |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | `25` |
| resolver digest | `sha256sum tools/harness/basename-couples-resolver.py` | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` |
| gate absent | `ls tools/harness/claims-freshness.py` | `No such file or directory` (exit 2) |
| resolver trap shape (independent) | inline scan, 223 entries | `0` hits |
| filed-byte edits | `git diff --name-only` | empty |

The trap-shape scan is this seat's independent check of the Ca02 row: over all 223
`corpus/knowledge/**/*.md`, it counted entries where a `couples` part ends in `-`, the
next line is blank, and the line after that is indented. Count: **0** - the Ca02 row's
`0/223` statement reproduces.

## 3. Row map

| source fragment | row id | class | owner |
|---|---|---|---|
| `calib/Ca01-stale-premises.md` | `r43-stale-premises` | `routed-with-owner` | r47 O claim (gate author) + integrator |
| `calib/Ca02-resolver-edge.md` | `r44-resolver-hyphen-after-blank` | `recorded` | next resolver touch (tools/harness maintainer) |
| `calib/Ca03-manifest-schemas.md` | `manifest-ledger-two-schema-evolution` | `recorded` | integrator-of-record (fleet MANIFEST writer) |
| `calib/Ca04-provider-amendments.md` | `PA-47-01-antigravity-lane-outage` | `named-deviation` | operator (ruling) + integrator (re-route record) |
| `calib/Ca04-provider-amendments.md` | `PA-47-02-zai-exhaustion-luna-max` | `named-deviation` | operator (exhaustion/substitute) + integrator (dispatch) |

## 4. Coverage of the loop-1 carried list - 5/5, zero dropped

`reports/round-46/loop-1-retrospective.md:43-53` names five carried items. All five are
dispositioned; the first two map to one row by design (both are the R01-43-12 class; the
row's `class_boundary` preserves the narrow/broad distinction Ca05 raised as F3). The
r46 audit's schema note is the sixth, additional loop-1 close item the Ca claim names.

| retrospective line | item | disposition |
|---|---|---|
| `:45-46` | freshness gate absent | row `r43-stale-premises` |
| `:47-48` | stale-premises pattern | row `r43-stale-premises` (same class; narrow incidence r43 O+C) |
| `:49-50` | resolver latent edge | row `r44-resolver-hyphen-after-blank` |
| `:51-52` | antigravity outage | amendment `PA-47-01-antigravity-lane-outage` (pos 12 re-routed+executed; pos 13 skipped) |
| `:53` | zai exhaustion | amendment `PA-47-02-zai-exhaustion-luna-max` |
| r46 audit `:6-8,28-32` | two MANIFEST schemas | row `manifest-ledger-two-schema-evolution` |

Deliberately not requeued, with reasons in `loop1_coverage.not_requeued`: the r44 C
carried-proposal failure (a coverage re-scope, not a stale premise), the r44 Ca
undelivered gate (same object as the stale-premises row's next touch), the r42 lithic
collision / r43 Ca improvement (already dispositioned), and the r44 `reasoning_content`
/ r43 digest-drift findings (round telemetry; Ca04 excludes them explicitly).

## 5. Fenced successor JSON (deliverable)

Integrator: extract the fenced object to `reports/round-47/calib/queue-successor-r47.json`
(or apply the successor update from it); run gates G1-G8 before filing. Never edit the
parent. If the r47 O claim lands, file a **new** closing row for `r43-stale-premises` -
never edit this artifact or that row in place.

```json
{
  "schema": "kotodama-defect-queue-successor-v1",
  "round": 47,
  "date": "2026-10-19",
  "loop": 2,
  "artifact": "defect-queue-v2 successor delta - loop-1 carried-item reconciliation (Ca06 assembly)",
  "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256_at_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "parent_sha256_recheck_after_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "parent_bytes_edited": false,
  "parent_git_state": "clean: `git status --porcelain reports/round-40/op/defect-queue-v2.json` -> no output; `git diff --name-only` -> empty (measured 2026-10-19, HEAD 6e9a30d)",
  "parent_history": "Committed at 13a1657 with sha256 fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98; edited in place once at ac47c78 (r41) to flip N7-receipt-fidelity and r39-runner-root-regression and append r41_update (recorded at reports/round-42/op/O08-queue-update.md:206-216). The digest has been dfc9265d... since that recorded supersession and is unchanged at 6e9a30d and ac47c78 (reports/round-47/calib/Ca05-verify.md:170-187). The r41 edit is a filed fact, not a second edit by this successor; the pin makes any further in-place edit detectable. Parent rows: 38 (28 carried-with-owner, 10 fixed-with-evidence).",
  "predecessor_successor": {
    "path": "reports/round-43/calib/defect-queue-v2-successor-r43.json",
    "sha256": "77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38",
    "rows": 4,
    "parent_pin": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907"
  },
  "baseline_commit": "6e9a30d",
  "source_fragments": {
    "reports/round-47/calib/Ca01-stale-premises.md": "e0e51e5600a1537f425c2d8f20ea68937e42c6c01b78c14d8d25580cce52ce3c",
    "reports/round-47/calib/Ca02-resolver-edge.md": "91cd4484b780ef823304d2c8b85c462a7131c336c73ad446d440138a1f01276c",
    "reports/round-47/calib/Ca03-manifest-schemas.md": "a2e61cdba8180e25fb81a9f4bb23dbb677011e2de98d8d341e6c9eb321cd70a6",
    "reports/round-47/calib/Ca04-provider-amendments.md": "94b99878a31ae6aa8c376fa35af786e36d07f3210c9f368f9a014f4a4ac2136e",
    "reports/round-47/calib/Ca05-verify.md": "747c0fdb1a1c1dc932e9dca3e1f6566e9472cccca608b197844febb8c0c88ee4",
    "reports/round-46/loop-1-retrospective.md": "a8e3fabb0d6502a03371be32632003fa3772f0ad39d15280847bcefc8b2d895d"
  },
  "class_vocabulary": {
    "fixed-with-evidence": "A landed artifact plus a pasted measured output closes the finding.",
    "routed-with-owner": "No fix is claimed; the finding has a named owner and a next touch.",
    "recorded": "The measured fact or correction is recorded; filed bytes are immutable or no action is owed.",
    "could-not-recover": "The evidence the finding depends on cannot be recovered; a named reason and owner are recorded.",
    "named-deviation": "A scheduled provider/model was not the observed provider/model, or a scheduled position did not execute, under a recorded operator ruling or lane-recorded amendment. Not a defect row: no rule breach is alleged; the record keeps requested and observed separate.",
    "v2_mapping": "fixed-with-evidence -> fixed-with-evidence; routed-with-owner -> carried-with-owner (owner + next_touch); recorded -> carried-with-owner with next_touch 'none - recorded'; could-not-recover -> carried-with-owner with the named reason; named-deviation -> no v2 class (v2_class_equivalent null; kind marker required to keep the defect census from inflating). The `class` field here is authoritative; `v2_class_equivalent` is the merge hint."
  },
  "rows": [
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
        "narrow": {
          "rounds": [
            43
          ],
          "claims": [
            "O",
            "C"
          ],
          "count": 2
        },
        "broad": {
          "rounds": [
            43,
            44
          ],
          "claims": [
            "O",
            "C",
            "C-body"
          ],
          "count": 3
        },
        "excluded": {
          "round": 44,
          "claim": "Ca",
          "reason": "before true at c9f4eaa; failure was delivery (durable_gate_exists false), not a stale premise"
        }
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
    },
    {
      "id": "r44-resolver-hyphen-after-blank",
      "origin": "r44 R01-44-05 (reports/round-44/review/R01-review.md:290) and R02-44-11 (reports/round-44/review/R02-review.md:468); measured in r44 cross/X01-trades.md:114-155 (T1b, table row :26) and op/O03-defects-verify.md:221-229; carried in reports/round-46/loop-1-retrospective.md:49-50. Dedupe aliases: R01-44-05, R02-44-11, T1b.",
      "class": "recorded",
      "v2_class_equivalent": "carried-with-owner",
      "owner": "next resolver touch - tools/harness maintainer (r47+); the r47 O claim (freshness gate) is not the resolver owner and does not edit the pinned body",
      "reason": "Measured at HEAD 6e9a30d: the docstring at tools/harness/basename-couples-resolver.py:55-59 promises that a blank line does not terminate the couples block when the previous part ends in a hyphen soft wrap and the next line is indented. The code cannot take that branch: soft_wrap = parts[-1].endswith('-') and not saw_blank (:73) makes the second disjunct of :74 redundant, so after a blank line the block always breaks. On the inline fixture, couples_block returns only 'language — `tone-' and field_refs returns [] - both tone-prosody.md (captured by the r42 witness) and writing-systems.md are dropped. Live incidence at 6e9a30d is 0/223 entries, so 'zero tokens dropped' holds for the live corpus only, not universally for the rule; the 27/27 selftest green does not cover the shape (S2b :359 is a non-blank hyphen wrap; S7c :411-415 is a blank line without a hyphen). The body is pinned at sha256 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64 and must not be edited in place; no fix is claimed this round.",
      "next_touch": "At the next resolver touch (r47+ tools/harness maintainer), choose and pin one behavior: (a) correct the docstring at :55-59 to 'a blank line always terminates the block' and add a selftest control asserting the fixture yields 0 refs (documents the limit), or (b) implement the documented exception (drop 'and not saw_blank' from :73) and add a control asserting the fixture yields tone-prosody.md + writing-systems.md. Do not leave docstring and code divergent. Any future 'zero tokens dropped' claim must be scoped to the measured corpus, never stated as a property of the rule.",
      "evidence": "tools/harness/basename-couples-resolver.py:55-59 (claim), :73-74 (unreachable branch), :359 (S2b), :411-415 (S7c); sha256 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64; reports/round-44/cross/X01-trades.md:26,114-155 (fixture measurement and live scan); reports/round-44/review/R01-review.md:290; reports/round-44/review/R02-review.md:468; reports/round-44/op/O03-defects-verify.md:221-229; reports/round-44/op/O10-census-verify.md:95 (soft-wrap identity: hyphen kept); reports/round-46/loop-1-retrospective.md:49-50.",
      "verification": "Commands run this seat at 6e9a30d: (1) import the live resolver, couples_block(fixture) -> ['language — `tone-'], field_refs(fixture) -> [] (2 tokens dropped); (2) python3 tools/harness/couples-reference-extractor.py .scratch/ca02-r47/hyphen_blank.md -> 'wrapped=True tokens=2' with tone-prosody.md unresolved and writing-systems.md fallback; (3) scan all 223 corpus/knowledge/*/*.md for a blank-separated indented continuation after a trailing-hyphen part -> 0 hits; (4) python3 tools/harness/basename-couples-resolver.py --selftest -> SELFTEST OK: 27/27 controls, exit 0; (5) sha256sum of the resolver and of reports/round-40/op/defect-queue-v2.json -> 43ce341f... and dfc9265d... respectively. Exact strings and the inline fixture are in section 1 of reports/round-47/calib/Ca02-resolver-edge.md."
    },
    {
      "id": "manifest-ledger-two-schema-evolution",
      "origin": "reports/round-46/audit/Ca01-manifest.md:7-8,28-32; reports/round-46/review/R01-review.md:87-89; reports/round-46/validation.json:147",
      "provenance_correction": "Not one of the loop-1 retrospective's five carried bullets (reports/round-46/loop-1-retrospective.md:43-53). The item originates in the r46 Ca01 audit's schema note; recorded here as the loop-1 close the Ca claim names, without back-attribution.",
      "class": "recorded",
      "v2_class_equivalent": "carried-with-owner",
      "owner": "integrator-of-record (MANIFEST.json rounds[] writer; PROTOCOL.md:194-196)",
      "reason": "The loop-1 ledger uses two row schemas for this lane. S1 (rounds 33-42, MANIFEST.json:4241-4806) is the documented fleet closure shape: 11 keys, type=closure, lanes/lane_rounds, admitted, per-axis verdicts, notes. S2 (rounds 43,44,46; MANIFEST.json:4860,4979,5030) is a flat lane close-receipt: 15 keys, flat lane, position/provider/model, verdict, per-claim status map, baseline_commit/close_commit, repo-prefixed receipt, singular note; no date/closed_at/type/lanes/verdicts. Both are machine-readable and both reconcile to their lane receipts (r46 validation 12/12), but they are not interchangeable: lane-only filtering sees 3 of 13 rows, lane_rounds-only sees 10 of 13, and no row-level schema version exists. This row records the two contracts and the consumer rules; it fixes nothing and edits no filed byte.",
      "next_touch": "Integrator: when appending round-47, pick one shape and apply it consistently. If S1, include date/type/lanes/admitted/verdicts and set lane_rounds only where the lane counter differs from round. If S2, include lane/position/provider/model/verdict/claims/baseline_commit/close_commit/receipt; add date or closed_at so close time is ledger-local. Either way do not rely on round alone as a key.",
      "evidence": "MANIFEST.json:4241 (r33 S1), :4337 (r37 kotodama), :4505 (kotoba r37, duplicate round), :4806 (r42 S1), :4860 (r43 S2), :4979 (r44 S2), :5030 (r46 S2); PROTOCOL.md:237-243 (round-entry shape), :283-290 (row identity), :194-196 (integrator write scope); PROTOCOL-APPENDIX.md:37 (lane_rounds keying cost); reports/round-46/run-validation.py:94-97,107-110 (two-schema consumer); reports/round-46/audit/Ca01-manifest.md:7-8,29-32; reports/round-46/validation.json:147.",
      "verification": "Commands run this seat (2026-10-19T17:53:10Z, ledger sha256 509305c8b95e5e732b26b59a5874e31f4c368afcba0193a10443023073724e32, 281 rows): schema census printed S1 rounds [33..42] 11 keys, S2 rounds [43,44,46] 15 keys; S1 lane_rounds==round true for all 10; S2 has date=False, closed_at=False for all 3; S2 claims key sets {43:[C,Ca,O],44:[C,Ca,O],46:[A,Ca,O]}; admitted S1 8T/2F, S2 2F/1T; duplicate round numbers 37-42 present for kotodama+kotoba. Full command and output at §7.",
      "findings": [
        {
          "id": "S1-contract",
          "class": "recorded",
          "owner": "integrator-of-record",
          "evidence": "MANIFEST.json:4241-4806; 10/10 rows share the 11-key set {round,date,type,closed_at,lanes,lane_rounds,promotions,minted,admitted,verdicts,notes}; admitted 8T/2F",
          "next_touch": "none - recorded"
        },
        {
          "id": "S2-contract",
          "class": "recorded",
          "owner": "integrator-of-record",
          "evidence": "MANIFEST.json:4860,4979,5030; 3/3 rows share the 15-key flat set; no date/closed_at/type/lanes/verdicts; receipt is fleet-root-relative",
          "next_touch": "none - recorded; add a close timestamp if S2 is reused"
        },
        {
          "id": "S2-protocol-shape-divergence",
          "class": "recorded",
          "owner": "integrator-of-record",
          "evidence": "PROTOCOL.md:237-243 names {round,date,type,lanes,promotions,minted,notes}; S2 has date/type/lanes/promotions/minted absent; grep -n 'per-lane' PROTOCOL.md PROTOCOL-APPENDIX.md -> no match",
          "next_touch": "to-verify: name the amendment if one exists, else record S2 as a named deviation at the next ledger touch"
        }
      ]
    }
  ],
  "provider_amendments": [
    {
      "id": "PA-47-01-antigravity-lane-outage",
      "kind": "provider-amendment",
      "defect_row": false,
      "class": "named-deviation",
      "v2_class_equivalent": null,
      "origin": "loop-1 positions 12-13 (rounds 44, 45); first lane signal at r43 (cursor/gemini-4-argon interruption in the route history), zero-output abort at r44; consolidated at reports/round-46/loop-1-retrospective.md:51-52,59-60",
      "requested": [
        {
          "loop": 1,
          "position": 12,
          "round": 44,
          "lane": "antigravity/gemini-3.8-flash",
          "workers": "32-64"
        },
        {
          "loop": 1,
          "position": 13,
          "round": 45,
          "lane": "antigravity/gemini-4-argon (max effort)",
          "workers": 8
        }
      ],
      "observed": [
        {
          "loop": 1,
          "position": 12,
          "round": 44,
          "route": "opencode-go/deepseek-v4.1-flash",
          "outcome": "executed after re-route; 32 launched / 14 completed / 18 failed; verdict rejected-honest-stop",
          "failure": "antigravity aborted twice with zero seat output"
        },
        {
          "loop": 1,
          "position": 13,
          "round": 45,
          "route": null,
          "outcome": "skipped; no telemetry directory and no round commit",
          "failure": "operator ruling: antigravity lanes non-functional on this host"
        }
      ],
      "planned": {
        "loop_2": {
          "positions": [
            12,
            13
          ],
          "rounds": [
            58,
            59
          ],
          "policy": "skip/re-route",
          "source": "reports/round-46/loop-1-retrospective.md:59-60"
        },
        "loop_3": {
          "positions": [
            12,
            13
          ],
          "rounds": [
            72,
            73
          ],
          "policy": "to-verify",
          "source": "reports/round-46/loop-1-retrospective.md:52 names 'loop-2/3 argon' but no loop-3 plan is written"
        }
      },
      "authorization": "operator ruling, quoted in reports/round-44/telemetry/dispatch-declared.json:10 ('skip the gemini and argon rounds') and reports/round-44/telemetry/observed-dispatch.json:18; recorded at LOG.md:3850-3852 and reports/round-46/loop-1-retrospective.md:3-4,23",
      "owner": "operator (ruling) + integrator (re-route record and loop-2/3 dispatch)",
      "reason": "The position-12 and position-13 seats are scheduled on antigravity lanes that are non-functional on this host. Position 12 was re-routed to opencode-go after two zero-output aborts; position 13 was skipped outright. Recording the amendment keeps the requested-vs-observed split explicit (AGENTS.md telemetry rule) and prevents a later dispatch from re-declaring a dead lane as if it had been served. Not a defect row: no rule breach is alleged, and the parent queue's notes exclude named telemetry deviations from defect rows (reports/round-40/op/defect-queue-v2.json:8).",
      "next_touch": "Loop-2 position 12 (r58) and position 13 (r59): apply skip/re-route at dispatch, declare the requested antigravity lane plus the observed route in dispatch-declared.json before the batch, and close the route in availability-close. Loop-3 r72/r73 policy remains to-verify.",
      "evidence": [
        "reports/round-46/loop-1-retrospective.md:3-4,23,26,51-52,59-60 (sha256 a8e3fabb0d6502a03371be32632003fa3772f0ad39d15280847bcefc8b2d895d)",
        "reports/round-44/telemetry/dispatch-declared.json:10,17 (sha256 565e4fbd505c9e7ff652e9dff9e2bbdef07c1b9555932bf401fb5fdf68570844)",
        "reports/round-44/telemetry/observed-dispatch.json:17-18 (sha256 445daadfd5d375d66df333122f7f1ef170f8fd6dd1618dcebc24c8ce01203b4a)",
        "reports/round-44/telemetry/availability-close-44.json:24-28 (sha256 8a9146e1b3cc961b78e966cd08ecf61a8dcd17e2225897ce4e1b7b73ba5fa354)",
        "reports/round-43/telemetry/availability-close-43.json:26 (cursor/gemini-4-argon interruption)",
        "reports/round-47/telemetry/dispatch-declared.json:18 ('antigravity skipped (broken)')",
        "LOG.md:3848-3853; SCORECARD.md:855-858,871-872; REGIMEN.md:21-22,66-69,73-77"
      ],
      "verification": "Measured at HEAD 6e9a30d on 2026-10-19: ls -d reports/round-{33..46} lists 13 directories and reports/round-45 is absent; git log --all --grep='round 45' -i returns 0 commits; r44 telemetry records 'aborted x2, zero output' and the opencode-go re-route; the r44 round directory, validation receipt and 14/32 observed completion verify position 12 executed.",
      "to_verify": [
        "loop-3 positions 72/73: the retrospective names 'loop-2/3 argon' (:52) but no loop-3 provider plan is written; owner integrator.",
        "loop-2 position 12: whether r58 skips or re-routes is not yet decided; owner integrator at dispatch.",
        "the antigravity abort root cause is recorded as an observation, not diagnosed; owner operator."
      ],
      "wording_correction": "The Ca04 mission phrase 'positions 12/13 skipped' is not literally supported: position 12 (r44) was re-routed and executed; only position 13 (r45) was skipped. This row records the distinction and does not repeat the both-skipped formulation."
    },
    {
      "id": "PA-47-02-zai-exhaustion-luna-max",
      "kind": "provider-amendment",
      "defect_row": false,
      "class": "named-deviation",
      "v2_class_equivalent": null,
      "origin": "loop-1 position 11 (r43) zai lane interrupted pre-completion x2 and re-routed; loop-1 retrospective:53 declares zai usage exhausted; :57-60 amends loop-2 positions 7-8 and 11 to luna-max; r47 dispatch carries it as a standing amendment",
      "requested": [
        {
          "loop": 2,
          "position": 7,
          "round": 53,
          "lane": "zai-coding-plan/glm-5.3-flash (MAX-effort seats)",
          "workers": "16-32"
        },
        {
          "loop": 2,
          "position": 8,
          "round": 54,
          "lane": "zai-coding-plan/glm-5.3-flash (MAX-effort seats)",
          "workers": "16-32"
        },
        {
          "loop": 2,
          "position": 11,
          "round": 57,
          "lane": "zai-coding-plan/glm-5.3-flash-low (pinned MAX)",
          "workers": 32
        }
      ],
      "observed": [
        {
          "loop": 2,
          "positions": [
            7,
            8,
            11
          ],
          "rounds": [
            53,
            54,
            57
          ],
          "route": "openai-codex/gpt-6-luna-max",
          "status": "declared amendment; none of the three rounds has executed at r47 (loop-2 position 1 is the current round)"
        }
      ],
      "scope": "reports/round-46/loop-1-retrospective.md:53 says 'for the session'; the session boundary and loop-3 applicability are not defined",
      "authorization": "to-verify: the retrospective is the integrator's lane record (:53,:59) and r47 dispatch-declared carries it as standing (:18), but no explicit operator quote authorizing the zai->luna-max substitution is filed. The loop-1 zai interruption itself was an explicit operator instruction (reports/round-43/telemetry/dispatch-declared.json:9).",
      "owner": "operator (exhaustion ruling and substitute authorization) + integrator (dispatch declaration and telemetry)",
      "reason": "The position-7-8 and position-11 seats are scheduled on zai, whose usage is recorded exhausted; luna-max is the named substitute. Recording it as a named deviation keeps the requested-vs-observed split explicit and avoids an undeclared provider substitution under REGIMEN.md:66-69. Not a defect row: the loop-1 zai rounds (r39, r40) were admitted; the exhaustion is an availability fact, not a rule breach.",
      "next_touch": "At r53/r54/r57 dispatch: declare requested zai plus observed luna-max in dispatch-declared.json before the batch and close the route in availability-close. Loop-3 positions 67/68/71 applicability to be ruled (to-verify).",
      "evidence": [
        "reports/round-46/loop-1-retrospective.md:17-18,26,53,59 (sha256 a8e3fabb0d6502a03371be32632003fa3772f0ad39d15280847bcefc8b2d895d)",
        "reports/round-43/telemetry/dispatch-declared.json:8-9 (sha256 76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe)",
        "reports/round-43/telemetry/observed-dispatch.json:20 (sha256 10181657c574dddc0fb1ce5b3b9be477b579cea4b871f3acf3a6c81d5dc1bf4f)",
        "reports/round-43/telemetry/availability-close-43.json:18,23-28 (sha256 eddfb5f334ee3a2f0931a1732e65606f9f6f0c1e3e824b7b39398ce1f0bdef48)",
        "reports/round-47/telemetry/dispatch-declared.json:18 (sha256 3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8)",
        "SCORECARD.md:833-835; REGIMEN.md:17,20,66-69,73-77"
      ],
      "verification": "Measured at HEAD 6e9a30d on 2026-10-19: r43 telemetry names requested zai-coding-plan/glm-5.3-flash-low and the interrupted route history; no dispatch-declared.json at r44, r46 or r47 names zai (lanes: opencode-go, devin, opencode-go); reports/round-45 does not exist. The exhaustion statement itself is lane-recorded, not provider-probed.",
      "to_verify": [
        "explicit operator authorization for zai->luna-max is not filed; owner operator/integrator.",
        "loop-3 positions 67/68/71 applicability is unstated; owner integrator.",
        "session boundary/expiry of the 'all session' amendment is undefined; owner operator.",
        "cause: the retrospective says 'usage exhausted' (:53) while r43 telemetry says 'interrupted x2' (:20); quota exhaustion vs lane instability is not established; owner integrator.",
        "no luna-max capacity/cost check is filed for the substituted seats; owner integrator."
      ],
      "evidence_grade": "lane-recorded: the exhaustion claim rests on the loop-1 retrospective (:53); provider-side quota/usage state is not observable from this repo and no zai availability probe is filed."
    }
  ],
  "loop1_coverage": {
    "retro_carried_bullets": 5,
    "retro_bullets_mapped": 5,
    "additional_loop1_close_items": 1,
    "mapping": [
      {
        "source": "reports/round-46/loop-1-retrospective.md:45-46",
        "item": "R01-43-12-class freshness gate absent (method proven at r44, no durable tool; owner integrator)",
        "disposition": "row r43-stale-premises (routed-with-owner)"
      },
      {
        "source": "reports/round-46/loop-1-retrospective.md:47-48",
        "item": "stale-premises pattern (claims not re-measured at baseline; r43 and r44 both hit it)",
        "disposition": "row r43-stale-premises (same class; its class_boundary records the narrow incidence r43 O+C and excludes r44 C as a carried-proposal failure - Ca05 F3)",
        "note": "Two retrospective bullets map to one row by design (Ca05 acceptance rule 1); both are dispositioned, neither is dropped."
      },
      {
        "source": "reports/round-46/loop-1-retrospective.md:49-50",
        "item": "basename-couples-resolver latent edge (blank-separated hyphen soft-wrap drops tokens; 0 live incidence)",
        "disposition": "row r44-resolver-hyphen-after-blank (recorded)"
      },
      {
        "source": "reports/round-46/loop-1-retrospective.md:51-52",
        "item": "antigravity lanes non-functional; positions 12/13 skipped or re-routed",
        "disposition": "provider amendment PA-47-01-antigravity-lane-outage (measured wording: pos 12 re-routed and executed, pos 13 skipped - Ca05 F2)"
      },
      {
        "source": "reports/round-46/loop-1-retrospective.md:53",
        "item": "zai usage exhausted; zai seats route to luna-max",
        "disposition": "provider amendment PA-47-02-zai-exhaustion-luna-max"
      },
      {
        "source": "reports/round-46/audit/Ca01-manifest.md:6-8,28-32",
        "item": "two MANIFEST ledger schemas (closure rows 33-42; per-lane rows 43,44,46 at r47 HEAD)",
        "disposition": "row manifest-ledger-two-schema-evolution (recorded; scope corrected per Ca05 F1)"
      }
    ],
    "not_requeued": [
      {
        "item": "r44 C carried-proposal failure (R01-44-09)",
        "reason": "Not a stale-premises row under the narrow reading: r44's before fields are true at c9f4eaa; the failure is a carried proposal (reports/round-44/review/R01-review.md:157), and the r47 C claim re-scopes coverage to the r44 K02-verified cartography gap. Recorded in reports/round-44/validation.json and LOG.md:3861-3865; excluded from r43-stale-premises' narrow incidence."
      },
      {
        "item": "r44 Ca undelivered gate (unprovable-but-better)",
        "reason": "The delivery failure and the missing gate are the same object as r43-stale-premises' next_touch (r47 O). r44's verdict is cited in that row's evidence rather than minted as a duplicate row."
      },
      {
        "item": "r42 lithic collision and r43 Ca (improved)",
        "reason": "Both were dispositioned in their own rounds' records (r42 collision ruling; r43 Ca admitted); neither appears in the retrospective's carried list. No requeue owed."
      },
      {
        "item": "r44 opencode-go reasoning_content defect (18 failed seats) and r43 claims-digest drift",
        "reason": "Already recorded in their round telemetry; Ca04's assembly guidance (reports/round-47/calib/Ca04-provider-amendments.md:5) explicitly excludes them from the two provider amendments. Not re-requeued here."
      }
    ]
  },
  "application_gates": [
    {
      "id": "G1-parent-pin",
      "check": "sha256sum reports/round-40/op/defect-queue-v2.json",
      "expected": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907; `git show 6e9a30d:reports/round-40/op/defect-queue-v2.json | sha256sum` identical; `git status --porcelain <parent>` empty"
    },
    {
      "id": "G2-parse",
      "check": "parse the fenced JSON; assert schema, round==47, baseline_commit==6e9a30d, parent path + digest, rows length 3, provider_amendments length 2",
      "expected": "parse OK; no empty id/class/owner/evidence/verification fields"
    },
    {
      "id": "G3-class-vocabulary",
      "check": "every rows[].class in {fixed-with-evidence, routed-with-owner, recorded, could-not-recover}; every provider_amendments[].class == 'named-deviation' with defect_row == false; no amendment appears in rows[]",
      "expected": "3 rows: routed-with-owner 1 / recorded 2; 2 provider amendments; zero amendments in rows; defect census unchanged by the amendments"
    },
    {
      "id": "G4-coverage",
      "check": "loop1_coverage.mapping covers retrospective lines 45,47,49,51,53 and the r46 audit schema note",
      "expected": "5/5 carried bullets mapped; 1 additional loop-1 close item; not_requeued entries each carry a reason"
    },
    {
      "id": "G5-fixed-discipline",
      "check": "no row is fixed-with-evidence at this assembly",
      "expected": "If r47 O lands and the regression/demos are green, the integrator files a NEW closing row (fixed-with-evidence) with the pasted command output; it never edits r43-stale-premises in place. If O does not land, the row stays routed-with-owner."
    },
    {
      "id": "G6-write-surface",
      "check": "git status --porcelain; find corpus/knowledge -name '*.md' | wc -l; ls corpus/knowledge/culture-material/*.md | wc -l",
      "expected": "only untracked reports/round-47/** (plus pre-existing r46 untracked fragments); corpus 223; culture-material 25 - no Ca-desk corpus delta"
    },
    {
      "id": "G7-no-filed-byte-edit",
      "check": "git diff --name-only; git diff --cached --name-only",
      "expected": "both empty; successor records only"
    },
    {
      "id": "G8-source-digests",
      "check": "re-hash the four Ca fragments listed in source_fragments",
      "expected": "digests match; a mismatch means a fragment was revised after this assembly - reconcile by evidence and record an id alias, never duplicate the rows or edit this artifact"
    }
  ],
  "observations": [
    "Assembly-time measurements (2026-10-19, HEAD 6e9a30d): parent sha256 dfc9265d...; predecessor successor sha256 77f9d63e...; resolver sha256 43ce341f...; corpus total 223; culture-material 25; `tools/harness/claims-freshness.py` absent (`ls` exit 2).",
    "Ca04's fragment landed while this seat was assembling; the two provider amendments are copied verbatim from its fenced rows (schema kotodama-provider-amendments-v1) into a top-level provider_amendments array, per Ca04's preferred shape. Ca04's class_vocabulary_extension is merged into class_vocabulary.",
    "Ca05's machine-readable block predates the final Ca01/Ca03/Ca04 bytes: it marks those row files could-not-evaluate-row-file-absent (observed 17:55Z) and records Ca02's digest as 7ceb8445..., while the fragments at this assembly are the digests pinned in source_fragments (Ca02 91cd4484... after its final write). Ca05's independently measured facts (r43 stale reproduction, 0/223 incidence, 27/27 selftest, schema split, F1-F4) are not contradicted; only the row-file presence/digest snapshot moved.",
    "Ca05 finding F5 (untracked reports/round-46/review/R01-review.md created during r47) is outside this claim; escalated to the A03 write-surface census, not edited or deleted here.",
    "No fixed-with-evidence row is minted. The only theoretical flip is r43-stale-premises, and it requires the r47 O tool plus the pasted r43 regression output (Ca01 reclass_gates G1-G7; Ca05 F4). None of that existed at assembly."
  ],
  "provenance": {
    "seat": "Ca06",
    "role": "executor",
    "claim": "Ca",
    "out_path": "reports/round-47/calib/Ca06-queue-successor.md",
    "baseline_commit": "6e9a30d",
    "head_measured": "6e9a30d",
    "date": "2026-10-19",
    "commands_run": [
      "git rev-parse --short HEAD -> 6e9a30d",
      "sha256sum reports/round-40/op/defect-queue-v2.json -> dfc9265d...",
      "git status --porcelain reports/round-40/op/defect-queue-v2.json -> (empty)",
      "git log --oneline -- reports/round-40/op/defect-queue-v2.json -> ac47c78, 13a1657 (two commits)",
      "python3 (inline) count parent rows -> 38",
      "sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json -> 77f9d63e...",
      "sha256sum tools/harness/basename-couples-resolver.py -> 43ce341f...",
      "find corpus/knowledge -name '*.md' | wc -l -> 223",
      "ls corpus/knowledge/culture-material/*.md | wc -l -> 25",
      "ls tools/harness/claims-freshness.py -> No such file or directory (exit 2)",
      "python3 scan of all 223 entries for the blank-separated hyphen soft-wrap trap shape -> 0 hits",
      "sha256sum of the four Ca fragments + Ca05 + the retrospective (pinned in source_fragments)"
    ],
    "writes": "only reports/round-47/calib/Ca06-queue-successor.md",
    "no_filed_byte_edits": true,
    "no_in_tree_runner_executed": true,
    "no_git_mutation": true,
    "no_corpus_staging": true
  }
}
```

## 6. Integration notes

1. **Parent pin.** Re-run `sha256sum` before applying: expected
   `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`. A mismatch means the parent was edited after this assembly; stop and
   report, do not route around it.
2. **Reclass.** `r43-stale-premises` is `routed-with-owner` at this cut because
   `tools/harness/claims-freshness.py` does not exist (measured). It flips only on the
   Ca01 `reclass_gates` G1-G7: durable path, green selftest whose asserted count equals
   the controls actually run, the r43 positive regression (O and C STALE, Ca FRESH,
   non-zero exit), a fresh negative control, the anti-theater mutation, baseline
   evaluation via `git show`/`ls-tree`, and could-not-evaluate != green. The flip is a
   new row with pasted output.
3. **Provider amendments.** Keep them in `provider_amendments[]`, never in `rows[]`;
   they carry `defect_row: false` and `v2_class_equivalent: null`. The measured wording
   is "pos 12 re-routed and executed, pos 13 skipped" (Ca05 F2; Ca04 `wording_correction`).
4. **Source digests.** `source_fragments` pins the exact bytes this artifact copied. A
   later fragment revision is a new record to reconcile by id alias, not a reason to
   edit this artifact.
5. **No fixed row is claimed.** No artifact landed in this seat's claim; any later
   `fixed-with-evidence` must carry a pasted re-run output.

## 7. Provenance and boundary

Commands run by this seat, at `6e9a30d`, 2026-10-19:

```
git rev-parse --short HEAD
sha256sum reports/round-40/op/defect-queue-v2.json reports/round-43/calib/defect-queue-v2-successor-r43.json
git status --porcelain reports/round-40/op/defect-queue-v2.json
git log --oneline -- reports/round-40/op/defect-queue-v2.json
python3 -c "import json; print(len(json.load(open('reports/round-40/op/defect-queue-v2.json'))['rows']))"
sha256sum tools/harness/basename-couples-resolver.py
find corpus/knowledge -name '*.md' | wc -l
ls corpus/knowledge/culture-material/*.md | wc -l
ls tools/harness/claims-freshness.py
# inline Python: 223-entry scan for blank-separated hyphen soft-wrap trap shape -> 0
sha256sum reports/round-46/loop-1-retrospective.md reports/round-47/calib/Ca0[1-5]-*.md
```

Only this file was written. No filed byte was edited, no corpus staging occurred, no
round runner was executed in-tree, and no git mutation/network/install was performed.
The `.scratch/` assembler used to copy the sibling row objects is ephemeral and its
output is this file.
