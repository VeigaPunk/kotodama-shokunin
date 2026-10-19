# R05 — reconciliation review (claim Ca, non-author)

- Seat `R05` (reviewer, claim **Ca**) | round 47, loop 2, position 1
- Baseline: `6e9a30d` (`git rev-parse --short HEAD` -> `6e9a30d`)
- Reviewed: 2026-10-19T18:08Z; every number below was re-measured by this seat,
  not taken from a row author.
- Out: `reports/round-47/review/R05-reconciliation.md` (the only path this seat writes).
- Scope: the Ca reconciliation only — Ca01/Ca02/Ca03/Ca04, the independent
  Ca05 verifier, and Ca06's assembled successor. C and O are other seats' claims.

## 0. Verdict

**PASS on the Ca claim's thresholds, with one should-fix before the successor is
filed.** Every loop-1 carried item reaches a class with an owner and cited
evidence; no item is silently dropped; the freshness row is routed to the r47 O
claim and is not prematurely marked fixed; the parent queue is byte-unchanged.
The should-fix is a false verification sentence inherited from Ca04 into Ca06
(F-R05-1). Provenance nits are listed in §4; none changes a class.

| item | declared class | review verdict |
|---|---|---|
| Ca01 — `r43-stale-premises` | `routed-with-owner` | **PASS** |
| Ca02 — `r44-resolver-hyphen-after-blank` | `recorded` | **PASS** |
| Ca03 — `manifest-ledger-two-schema-evolution` | `recorded` | **PASS** (N2 path nit) |
| Ca04 — antigravity + zai | `named-deviation`, `defect_row:false` | **PASS with F-R05-1** |
| Ca05 — independent verifier | n/a | **PASS**; digest block internally inconsistent (F-R05-4) |
| Ca06 — assembled successor | 3 rows + 2 amendments | **PASS with corrections** (F-R05-1..3, F-R05-5) |
| parent `defect-queue-v2.json` | pinned `dfc9265d…` | **PASS** — unchanged |
| write surface | no filed-byte edit | **PASS** |
| coverage | 5/5 retro bullets + 1 r46 item | **PASS** — zero dropped |

Reviewed digests (sha256, at `6e9a30d`):

```
e0e51e56…  reports/round-47/calib/Ca01-stale-premises.md
91cd4484…  reports/round-47/calib/Ca02-resolver-edge.md
a2e61cdb…  reports/round-47/calib/Ca03-manifest-schemas.md
94b99878…  reports/round-47/calib/Ca04-provider-amendments.md
26430501…  reports/round-47/calib/Ca05-verify.md
15bb86df…  reports/round-47/calib/Ca06-queue-successor.md
dfc9265d…  reports/round-40/op/defect-queue-v2.json
77f9d63e…  reports/round-43/calib/defect-queue-v2-successor-r43.json
a8e3fabb…  reports/round-46/loop-1-retrospective.md
```

## 1. Independent re-measurement

### 1.1 Stale premises (Ca01's subject)

At `7ceff59`, committed bytes, not the worktree:

```
$ git ls-tree -r --name-only 7ceff59 -- tools/harness/ | grep couples
tools/harness/couples-reference-extractor.py
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
... PASS wrapped positive 4/4 tokens ...  (8 PASS, rc 0)
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'
223
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol/ | wc -l
26
$ git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/
(no output)
```

`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at `7ceff59`
(sha256 `c99f44ca…`) and its `- topic:` line (`:5`) owns the lithic register.
`reports/round-43/validation.json` records `claims.O.verdict =
failed-as-declared` (existing extractor sha `d8d23a26…`, selftest 8),
`claims.C.verdict = blocked-by-topic-collision` (lithic owner `c99f44ca…`,
26/223), and `claims.Ca.verdict = improved`; the round verdict is
`rejected-honest-stop`. That is exactly the O/C stale + Ca fresh asymmetry the
r47 O gate must reproduce (`reports/round-43/review/R01-review.md:400`,
R01-43-12; `reports/round-43/claims.json:27,40,53`).

Ca01's narrow/broad incidence distinction is correct and important:
narrow = r43 O+C (2 claims/1 round); broad = plus r44 C's carried-proposal
clause (3/2), with r44 Ca excluded because its `before` was true at `c9f4eaa`
(`reports/round-44/claims.json:52`; `reports/round-44/validation.json`
`durable_gate_exists: false`, `Ca.verdict: unprovable-but-better`). The
retrospective's "r43 and r44 both hit it" (`:47-48`) is the broad grouping;
the row states this rather than laundering the two readings together.

### 1.2 Resolver latent edge (Ca02's subject)

```
$ sha256sum tools/harness/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
$ python3 tools/harness/basename-couples-resolver.py --selftest
SELFTEST OK: 27/27 controls          # exit 0
$ python3 tools/harness/couples-reference-extractor.py .scratch/r05-verify/hyphen_blank.md
wrapped=True tokens=2                # tone-prosody.md unresolved; writing-systems.md fallback
```

Importing the live resolver on the same fixture yields
`couples_block -> ['language — `tone-']` and `field_refs -> set()`: the
successor drops both tokens the witness captures. My own scan of all 223
`corpus/knowledge/*/*.md` for a blank-separated indented continuation after a
trailing-hyphen part returns **0** hits, and there are no entries nested below
`corpus/knowledge/<partition>/` (all 223 are at that depth). So the row's
"0/223 live incidence" and the rule-level defect both reproduce. The body is
pinned at `43ce341f…`; editing it is out of scope.

### 1.3 MANIFEST schemas (Ca03's subject)

Read-only fleet sibling `/home/vgpnk/Projects/shokunin/MANIFEST.json`
(sha256 `509305c8…`, 293,641 bytes, 281 rows):

```
S1 [33..42]  keys 11: admitted, closed_at, date, lane_rounds, lanes, minted,
             notes, promotions, round, type, verdicts
S2 [43,44,46] keys 15: admitted, baseline_commit, claims, close_commit, filed,
             lane, loop, model, note, position, provider, receipt,
             requested_workers, round, verdict
S1 lane_rounds==round: True (10/10)
S2 date/closed_at: none (3/3); claims {43:[C,Ca,O],44:[C,Ca,O],46:[A,Ca,O]}
S1 admitted 8T/2F; S2 43/44 rejected-honest-stop, 46 admitted
```

Line pins reproduce: r33 `:4241`, r43 `:4860`, r44 `:4979`, r46 `:5030`. The
`PROTOCOL.md:194-196,237-243,283-290` and `PROTOCOL-APPENDIX.md:37` text is real
in the fleet root and says what Ca03 quotes. Ca03 correctly declined to claim
an era boundary: the flat schema covers 43, 44 **and 46**, not just the two
rows the r46 audit named. Its provenance correction — the MANIFEST item is an
r46-audit observation, not one of the retrospective's five carried bullets —
matches my read of `reports/round-46/audit/Ca01-manifest.md:6-8,28-32` and
`reports/round-46/validation.json:147`.

### 1.4 Provider amendments (Ca04's subject)

- Antigravity: r44 was scheduled `antigravity/gemini-3.8-flash` and aborted
  twice with zero seat output; the operator re-routed to
  `opencode-go/deepseek-v4.1-flash`, where it executed (32 launched / 14
  completed / 18 failed; `reports/round-44/telemetry/observed-dispatch.json:10-18`;
  `dispatch-declared.json:10`;
  `availability-close-44.json:24-28`). Position 13 (r45) was skipped:
  `reports/round-45/` does not exist and `git log --all --grep='round 45' -i`
  returns 0. The retrospective's own wording is "skipped or re-routed"
  (`:51-52`). Ca04's correction — **12 re-routed and executed, 13 skipped** —
  is the measured statement; the mission's "12/13 skipped" is not.
- Zai: the retrospective says usage exhausted (`:53`) and routes pos 7-8+11 to
  `openai-codex/gpt-6-luna-max` (`:59`); r46's dispatch notes carry the standing
  amendment (`reports/round-46/telemetry/dispatch-declared.json:16`) and r47's
  notes restate it (`reports/round-47/telemetry/dispatch-declared.json:18`).
  Ca04 is right to split the observation: r43's telemetry records
  interruptions, not a provider-side quota probe
  (`reports/round-43/telemetry/observed-dispatch.json:20`), so the cause and
  the operator authorization for the substitution stay `to-verify`. That is
  honest calibration, not a defect in the record.

## 2. Class correctness

| row | class | why it is right |
|---|---|---|
| `r43-stale-premises` | `routed-with-owner` | `tools/harness/claims-freshness.py` is absent at review (`ls` exit 2). `fixed-with-evidence` would be a fix claim without a landed artifact. The row names the r47 O claim + integrator and makes the flip conditional on G1-G7, each with pasted output (Ca01 §4, `:228-236`). |
| `r44-resolver-hyphen-after-blank` | `recorded` | The body is pinned and may not be edited; no fix is claimed; the limitation is recorded with a fixture, a witness comparison, and a 0/223 live scope. The `v2_class_equivalent: carried-with-owner` maps through the r43 successor's documented v2 mapping (`defect-queue-v2-successor-r43.json:class_vocabulary.v2_mapping`), where `recorded -> carried-with-owner` with a next touch. |
| `manifest-ledger-two-schema-evolution` | `recorded` | It is a schema-evolution observation, not a defect; the row says so and corrects the claim's back-attribution. No filed byte changes. |
| `PA-47-01`, `PA-47-02` | `named-deviation`, `defect_row:false` | The parent queue's own notes exclude telemetry deviations from defect rows (`defect-queue-v2.json:8`). Keeping them in a top-level `provider_amendments[]` preserves the 38-row defect census and the requested-vs-observed split. |

No row is `fixed-with-evidence` at this cut, and none should be: no Ca seat
landed a fix. The only theoretical flip is `r43-stale-premises`, which belongs
to a **new** closing row after the O gate lands, never an in-place edit of
Ca06 (Ca06 §6.5, G5).

## 3. Coverage of the loop-1 carried list

`reports/round-46/loop-1-retrospective.md:43-53` has five bullets. The
successor maps all five, with the first two to one row by design (both are the
R01-43-12 class) and the r46 audit's schema note as the sixth, additional item:

| retrospective line | item | disposition |
|---|---|---|
| `:45-46` | freshness gate absent | `r43-stale-premises` |
| `:47-48` | stale-premises pattern | `r43-stale-premises` (narrow r43 O+C) |
| `:49-50` | resolver latent edge | `r44-resolver-hyphen-after-blank` |
| `:51-52` | antigravity outage | `PA-47-01` (12 re-routed/executed; 13 skipped) |
| `:53` | zai exhaustion | `PA-47-02` |
| r46 audit `:6-8,28-32` | two MANIFEST schemas | `manifest-ledger-two-schema-evolution` |

Zero dropped. The `not_requeued` entries each carry a reason
(Ca06 `:419-436`): r44 C is the carried-proposal class, r44 Ca is the same
undelivered gate as the stale row's next touch, r42/r43 were dispositioned in
their own rounds, and r44's `reasoning_content` / r43's digest drift are round
telemetry, excluded by Ca04. This matches Ca05's acceptance rule 1.

The Ca claim text's "positions 12/13 skipped" is a claim-level imprecision; the
artifact repairs it rather than propagating it (`Ca04:87-99`;
`Ca06:71,309,405-406`). Likewise, "the two MANIFEST ledger schemas" is right
about the number of shapes but the record correctly documents three per-lane
rows (43, 44, 46) and says why. Both are improvements on the claim text.

## 4. Findings

**F-R05-1 (should-fix — false verification sentence, inherited by Ca06).**
Ca04's zai row says: "no dispatch-declared.json at r44, r46 or r47 names zai
(lanes: opencode-go, devin, opencode-go)" (`Ca04:195`), copied verbatim into
the successor (`Ca06:371`). The literal claim is false: r46's dispatch notes
say "zai usage exhausted" (`reports/round-46/telemetry/dispatch-declared.json:16`)
and r47's say "zai->luna-max all session"
(`reports/round-47/telemetry/dispatch-declared.json:18`, which the same row
cites as evidence). The intended true statement is "none of those rounds
dispatched **on** zai; the amendment appears only in the notes." Required:
scope the sentence to `provider_lane`/`model` in both Ca04 and the successor
before filing. Ca05 independently found the same sentence (its F6,
`Ca05:225-230`), so this is two-verifier agreement, not a stylistic quibble.

**F-R05-2 (minor — terminology).** Ca06's `not_requeued` says "r43 Ca admitted"
(`Ca06:430`). r43's round verdict is `rejected-honest-stop`; the Ca **claim**
was `improved` (`reports/round-43/validation.json`; SCORECARD.md:843). Ca01's
row already uses the correct phrasing ("passed (improved) even though the round
was rejected", `Ca01:218`); Ca06 should match it. "Admitted" is a round-level
term and must not be applied to a rejected round's claim.

**F-R05-3 (minor — reproducibility of citations).** Ca03 and Ca06 cite
`MANIFEST.json`, `PROTOCOL.md`, and `PROTOCOL-APPENDIX.md` as bare paths
(`Ca03:188,195,209,216`; `Ca06:195,216`). They are fleet-root files; the lane
repo has none of them (`ls PROTOCOL.md` -> ENOENT). The ledger's absolute path
is named once in Ca03's header (`:7`), but the successor's evidence arrays will
be read standalone. Required: prefix the fleet root (as r46's audit does) or add
one root note to the successor. Ca05's N2 (`Ca05:205-208`) reaches the same
conclusion.

**F-R05-4 (minor — Ca05's own digest block is inconsistent).** Ca05's verdict
table pins Ca04 at `94b99878…` (`Ca05:26`), but its section header
(`Ca05:214`) and machine-readable block (`Ca05:338`) pin `5f370306…`. The
current Ca04 is `94b99878…`; `5f370306…` is the pre-15:04 revision. The F6
verdict still applies to the current bytes (the sentence is unchanged), but a
digest-bound verifier cannot leave two digests for one row. Required: re-pin
the block to `94b99878…`, or state explicitly that the §0 table supersedes the
older header/block.

**F-R05-5 (minor — successor pins a superseded verifier).** Ca06's
`source_fragments` pins Ca05 at `747c0fdb…` (`Ca06:113`), a 17:5x draft; the
filed Ca05 is `26430501…` (revised 18:08Z, with all four rows verified and F6
recorded). Ca06's observation (`:483`) correctly says Ca05's block predates the
final row bytes, but it predates the final Ca05 too. The integrator should
reconcile the Ca05 citation at filing (G8) and cite the final verifier digest.
This is evidence provenance, not a row-source digest: Ca01-Ca04 pins all match
current bytes.

Minor citation notes (no action required beyond the above):
- Ca06's G8 says "re-hash the four Ca fragments" (`Ca06:476`) while
  `source_fragments` lists five Ca fragments (Ca01-Ca05). Say "the fragments
  listed".
- Ca01/Ca06 cite `SCORECARD.md:865` for "loop-1 calibration verdict"
  (`Ca01:220`; `Ca06:133`); 865 is r44's calibration row (unprovable-but-better),
  while r43 Ca improved is SCORECARD.md:843. The citation is not false, but the
  label should name which round.
- `reports/round-46/review/R01-review.md` is untracked and was created during
  r47 (mtime 14:48). It is not a tracked edit and no Ca seat wrote it; A03's
  write-surface census should classify it (Ca05 F5). Do not edit or delete it
  from the Ca lane.

## 5. Cross-check against Ca05

Ca05's final snapshot (digest `26430501…`) supersedes its 17:58Z draft, which
marked Ca01/Ca03/Ca04 `could-not-evaluate` because their row files were absent.
The final verdicts are PASS for Ca01/Ca02/Ca03 and PASS-with-F6 for Ca04, with
F1-F4 resolved by the later fragments, F5 escalated to A03, F6 remaining, and
F7 a process note that verification is digest-bound. I agree with that
resolution; my F-R05-1 is the same defect as Ca05 F6, and my F-R05-3 is Ca05
N2. Ca06's `observations` already notes the timing gap and Ca02's superseded
`7ceb8445…` pin (`Ca06:483`); the only additional drift is the Ca05 digest
itself (F-R05-5) and Ca05's internal Ca04 duplicate pin (F-R05-4).

Ca05's N1 (a `recorded` row carrying a non-empty next touch) is not a defect:
the r43 successor's `v2_mapping` defines `recorded -> carried-with-owner with
next_touch 'none - recorded'`, and Ca02's advisory next touch is more useful
than "none" while `class: recorded` remains authoritative. Ca06 keeps the class.

## 6. Write surface and parent integrity

```
$ git diff --name-only          -> (empty)
$ git diff --cached --name-only -> (empty)
$ git status --porcelain        -> ?? reports/round-46/review/
                                   ?? reports/round-47/
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
$ python3 -c "import json; d=json.load(open('reports/round-40/op/defect-queue-v2.json')); print(len(d['rows']))"
38                                   # 28 carried-with-owner, 10 fixed-with-evidence
$ find corpus/knowledge -name '*.md' | wc -l        -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l -> 25
$ ls tools/harness/claims-freshness.py              -> No such file or directory
```

The parent matches the r43 successor pin (`defect-queue-v2-successor-r43.json:7`)
and the r40 commit history is the recorded two-commit story (`13a1657` ->
`ac47c78`); no new in-place edit was made. No Ca seat wrote under `corpus/` or
`tools/`; all six fragments are under `reports/round-47/calib/` and this review
is the only R05 write.

## 7. Final verdict and residual risk

The Ca claim's thresholds are met in substance:

1. every loop-1 carried item reaches a class with owner + cited evidence — yes,
   5/5 plus the r46 schema note;
2. zero silently dropped — yes, with explicit `not_requeued` reasons;
3. the freshness-gate row routes to the O claim's tool, not to a premature
   `fixed` — yes, `routed-with-owner` + G1-G7;
4. the provider amendments are named deviations, not defect rows — yes,
   `provider_amendments[]`, `defect_row:false`, census unchanged;
5. the parent is pinned and unchanged — yes, `dfc9265d…`, 38 rows.

**Do not file the successor until F-R05-1 is corrected in both Ca04 and Ca06**
and the digest pins in F-R05-4/F-R05-5 are reconciled. Filing as-is would put a
demonstrably false verification sentence into the durable queue — the same
failure class (a claim not re-measured against the bytes it cites) that
R01-43-12 exists to prevent. F-R05-2/F-R05-3 are wording/reproducibility fixes
and should ride the same correction pass.

Residual, conditional: if the r47 O gate lands and passes G1-G7, the integrator
opens a **new** `fixed-with-evidence` row for `r43-stale-premises` with the
pasted r43 regression output; Ca06 and Ca01 are never edited in place. If the
gate does not land, the row stays routed and the loop-2 pre-dispatch check
remains manual.

Signed: **R05** — non-author reviewer for claim Ca. All measurements above were
re-run by this seat at `6e9a30d`; the digests in §0 bind this verdict to the
bytes reviewed.
