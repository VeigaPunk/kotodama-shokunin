# round-50 build scout — mistake sweep (frontier, not a claim)

- seat: ChousaR27R2.ScoutMistakeSweep-4 (leaf; no delegation, no installs — none needed)
- date: 2026-10-21; lane base `4ad26836552462d28a946ca3b067cab0b5ce3532`
- assigned: sweep `corpus/lessons/round-4*.md`, `round-49-verifier-spotcheck.md` and the
  SCORECARD rejected rounds 36/42/43/44/47/49 for mistakes **not yet captured by a QUALITY
  criterion or a gate**; list class, pointer, captured-by, candidate fix.
- method: read-only. Every "captured-by" below was checked against the live tool bytes or the
  QUALITY.md text at the lane base; nothing was executed that writes. No web sources, so no
  SOURCES rows are offered here.

## Result

17 classes survive the "not captured" test. Six were already *named* in
`corpus/lessons/round-49.md` §Frontier (`:213-251`) — for those this report adds the verified
captured-by status and a concrete fix shape, not a new discovery. Eleven are not named there.
Two are actionable inside round 50 (marked **R50**); rows 2 and 3 shape C's entry contract but are
r51 work; the rest are r51+ candidates.

## Sweep table

| # | class | pointer (exact) | captured-by (verified) | candidate fix |
|---|---|---|---|---|
| 1 **R50** | `evidence_command` does not reproduce the clause it evidences | `reports/round-50/claims.json:22` (r50 C `pastoral-unowned`); same class at `reports/round-47/review/R03-c-content.md:189` (B2) and `SCORECARD.md:969` (r49 narrowing) | **none** — `claims-freshness` evaluates the `topic_owner_absent` probe, never the `evidence_command` string | run each `evidence_command` read-only at declaration and require its output to agree with `expect`; here the fix is the command (see §Live 1) |
| 2 | calibration-section **form** is graded by an unpublished rule; the same condition is DEFECT in one partition and PASS/structural-note in another | `corpus/lessons/round-4-audit/culture-material.md:49,77` (CM-A01); `round-4-audit/linguistics.md:44,81` (CAL-01); `round-4-audit/civ-36-42.md:35-39` (A04/A05 + "calibration interpretation caveat"); `round-4-audit/civ-22-28.md:24-28` (row prints `PASS` **and** `DEFECT: CAL-0n`) | **none** — QUALITY criterion 2 (`corpus/QUALITY.md:9-12`) demands content, not form; `provenance-audit` fires only when calibration vocabulary is absent anywhere and otherwise emits `INFO calibration-prose-only` (`tools/gates/provenance-audit.py:18-23,390`) | fix the form in criterion 2 in one sentence ("one headed `## N. Calibration bank`, or a one-line note naming where the status lives"); both landed models already use `## N. Calibration bank` (`hunting-foraging-subsistence.md:176`, `cartography-and-mapmaking.md:214`); add the matching provenance-audit leg; add a report lint that refuses a row carrying both `PASS` and `DEFECT` |
| 3 | a `(to-verify)` claim flag with no claim-specific triage row ("unbased flag") | `round-4-audit/linguistics.md:43,54` (FLAG-01); `round-4-audit/civ-64-70.md:25,67,77` (R4-CIV-70-01); `round-4-audit/civ-85-92.md:23-24` (tibet 6, turkic 10); `round-4-audit/civ-64-70.md` mesoamerica 30 unbased | **none** — QUALITY criterion 1 permits the marker without a basis; the audits say so explicitly (`civ-64-70.md:77`: "This gate inventories markers but does not enforce triage-row coverage"); `source-audit-inventory.py:152-165` labels policy-vs-substantive heuristically and "Never a verdict" | new `provenance-audit --basis` leg: every parenthesized substantive mark must match a `corpus/lessons/*triage*/` row naming the entry and sharing tokens with the claim; QUALITY criterion 1 gets one clause ("the marker names its ledger row") |
| 4 **R50** | mis-cited tool scope in the lane's own mistake ledger, from line-cite decay | `corpus/lessons/round-49.md:149` (mistakes row) and `:232-235` (frontier) cite `tools/harness/receipt_guard.py:178` as "scopes the guard to `validation.json`". Measured at `8c78e6b` **and** HEAD, `:178` is `receipt = root / "validation.json"` inside `_fixture_repo` (the selftest fixture). `_check_receipt` (`:82-150`) accepts any repo-relative path and consults `HEAD` only | **none** for internal cites; `round-49.md:133-135` names only the README line-decay instance (r48 Ca01 §5) | internal pointers must be `sha256:<prefix>:path:N` or carry the quoted token in the same cell; a read-only lint resolving every `path:N` in a lesson/report at filing HEAD and failing on token mismatch |
| 5 | ownership/gap claim measured with a narrower rule than its wording | `SCORECARD.md:969` ("0 true topic owners" narrowed to "0 filename owners; 2 partial topic owners"); `round-49-verifier-spotcheck.md:8-12` | **partial** — `claims-freshness` `topic_owner_absent` runs at declaration; the narrowing was a critic finding, not a control | the claims.json clause must name the matching rule and print three counts (filename owners / topic owners / cross-reference mentions); runner prints all three |
| 6 | pre-apply write safety: stale path proposals overwrite live entries; add-only ownership not enforced | `SCORECARD.md:824,826-830` (r42 incident: two entries overwritten by stale paths, restored byte-exact); the class row is `round-49.md:149` | **none** (`receipt_guard` guards the one receipt path handed to it; `/178` citation wrong per row 4). Named in r49 §Frontier → new | `lands` preflight: refuse a land path that exists at base with different bytes unless the claim declares `modifies`; recompute `rows == files`, filename and topic ownership before publication |
| 7 | placeholder tokens + prediction-vs-delivery in the README apply | `SCORECARD.md:664-666,682` (two `__E3_PLACEHOLDER__` lines, LOG/commit attribution conflict); `round-49.md:220-231` | **none** — `reports/round-28/readme/sweep.py` legs are index/footer/block totals only (`:18-27`); `tools/check-readme-heading.py:1-20` headings only; `tools/check-readme-revisions.py:1-27` labels/order/warnings only. Named in r49 §Frontier → new | two legs on assembled bytes: grep `__[A-Z0-9_]+__`; parse the newest `revision:` block's declared totals and print declared vs measured |
| 8 | carried-candidate collision ("fresh" claim on a candidate a prior round already named) | `SCORECARD.md:854-873` (r44 dream slug at `reports/round-42/scout/K02-myth-gaps.md:216`; ruling R01-44-09) | **none durable** — a ruling, not a control; declaration probes scan corpus topic lines, not prior scout files. Named in r49 §Frontier → new | declaration-time `grep_absent` over `reports/round-*/scout/**` + `reports/round-*/review/**` for the candidate slug/topic tokens, printing prior mentions |
| 9 | right-size / over-build | `SCORECARD.md:894-901` (790 lines vs live max 221 at `a01405d`; 9 blocking defects); live culture-material band measured now: n=27, min 103, median 149, max 239 (`cartography-and-mapmaking.md`) | **none** — QUALITY `:5-29` carries six criteria, no size leg; r47 disposition lives only in `reports/round-48/calib/queue-successor-r48.json:31`. Named in r49 §Frontier → new | **criterion 8, not 7** — Ca lands criterion 7 (separability) this round; appending right-size as "7" collides. Add `--max-lines 250 --partition-max-ratio 1.08` as an entry-shape leg too, since r47 was a build-quality miss, not a prose miss |
| 10 | entry self-consistency defects no gate covers (r47 B1/B3/B4/B5–B6/B7/B8/B9) | `reports/round-47/review/R03-c-content.md:188-196` | **partial** — r49 entries sha256-pin in-corpus anchors by hand; no tool resolves `path:N` + token; nothing covers prose arithmetic (B1), negative-existence claims carrying no command (B3), dangling `§N` (B5–B6), worked-example single-rule consistency (B7), competing-ownership sentences (B8), N-item vs table-row completeness (B9) | one tool, five cheap legs (`tools/check-entry-shape.py`): §ref resolution; `N forms` vs table rows; every `path:N` resolves and contains the quoted token or a sha pin; every "does not contain/appear" sentence carries its grep command + output; the worked example states its rule once (normalized compare) and names its decision-record ids |
| 11 | gate-green read as audit-green (scope overclaim) | `round-4-audit/culture-material.md:77`; `round-4-audit/linguistics.md:81`; `round-4-audit/civ-64-70.md:77`; registry `SKILL.md:577-616` | **partial** — verdict map + prose limits in the registry; no machine-readable "does not check" and no rule that a claim citing a gate must cite its scope | each gate prints a `SCOPE:` line naming what it does not check; the registry gains a `does-not-check` column; `check-gate-battery` verifies the line exists; claims cite it |
| 12 | round-4 residuals still open after 46 rounds: `Q-03-1` PHON-INVENTORY ×10 (encoding mismatch undiagnosed), `Q-04-1` DERIV-REPLAY ×8 (derivation adapter never delivered) | `corpus/lessons/round-4-sol-fixes-and-audits.md:28-33`; `corpus/lessons/README.md:174-175` | open-question queue rows only (owner: `tools/gates/naming-collision-gate.py`); no gate leg | add a `PHON-ENCODING` normalization control (NFC/NFD segment compare) so the two classes stop conflating; land the derivation adapter as a typed-pipeline leg using the four-step recipe the ledger names at `reports/round-25/argot/delta.md` (cited second-hand from `corpus/lessons/README.md:175`; not opened by this seat) |
| 13 | self-count drift and unexecuted commands in lessons/reports | `round-49.md:311` (23 vs 22 vs 21), `:315-317` (doubled backslash in the recount command) | **none** — corrected manually after review | lesson/report lint: extract each ``` `command` → N ``` pair, run it read-only in a temp export, fail on mismatch; code spans in lessons are test-run before filing |
| 14 | "admitted by runner, pending non-author verification" rows never receive their adjudication | `SCORECARD.md:955` (r49 admitted-pending), `:975` (separability "recorded, not gating") vs `round-49-verifier-spotcheck.md:15-17` (REJECTED-HONEST-STOP); `grep -n 'HONEST' SCORECARD.md` → no r49 row | **partial** — Ca turns separability gating this round (tool + criterion 7), but nothing forces the ledger row to be superseded when an outside adjudication lands | fail a `pending` row whose round has a later adjudication file; append the r49 superseding row citing the spotcheck (owner: integrator) |
| 15 | target-setting fallacy: a declared target is not a measurement | `round-4-sol-fixes-and-audits.md:16-24`; `corpus/lessons/README.md:178` (`Q-04-4`, "carried as craft rule"); same shape as the open r11 freshness threshold (`round-49.md:215-219`) | **none** — craft rule only; `claims-freshness` checks premise freshness, not target provenance | claims.json acceptance thresholds require `basis` (measured prior rate + pointer); one receipt leg refuses a numeric target with no basis cite |
| 16 | lessons-record convention diverges from practice (scribe records under `reports/round-N/scribe/` vs "one file per round"; r45 has no report dir and no LOG header) | `corpus/lessons/README.md:3-4`; `round-49.md:247-251`; measured: `ls -d reports/round-45` → absent | **partial** — the round-25 index audit forces new lessons to be indexed (`reports/round-25/audit/c31-lessons-index-audit.py`, green at r49), but nothing reconciles the README's "one file per round" claim with the 21 scribe directories | one recorded decision: either index the scribe records as a second class or amend the README claim; then a count leg (`filed lessons + scribe dirs + absent rounds`) that must sum |
| 17 | declaration digest drift mid-round: the claim set verified is no longer the claim set declared | `SCORECARD.md:847-849` (r43 named deviation: three provider redirects, claims.json re-pinned in `reports/round-43/telemetry/availability-close-43.json`) | **partial** — an availability-close record, not a control; `claims-freshness` reads the claims doc as supplied and never pins its sha | pin `claims_sha256` in the dispatch record and the first receipt; the runner refuses divergence or writes a dated re-pin row with both digests, so a round cannot silently verify a different declaration |

## Live round-50 findings (act now)

**1. r50 C's declared gap command contradicts its own clause.** `reports/round-50/claims.json:22`
declares `grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/`.
Measured at base: **1 hit** — `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`,
token **"sherd"** (writing surfaces). The whole-word alias probe
`grep -rniE '^- topic:.*(\bpastoral(ism)?\b|\bherding\b|\bhusbandry\b|\btranshumance\b|\blivestock\b)' corpus/knowledge/`
→ **0**. So the register really is unowned (C's premise stands), but the printed command is
unreproducible evidence — exactly the r47 B2 / r49 narrowing class, in this round's own
claims.json. Fix: word-boundary the command (`(^|[^a-z])herd`) or drop bare `herd`, and have the
clause say "0 whole-word topic owners; `sherd` is a false positive". Filename probes are clean:
`find corpus/knowledge -iname '*pastoral*' -o -iname '*herd*' -o -iname '*husband*' -o -iname '*transhum*' -o -iname '*livestock*'` → 0.

**2. Criterion numbering collision.** `corpus/QUALITY.md` holds **six** criteria
(`sha256 e3172413…`, `:5-29`); criterion 6 is source authority. Ca lands "criterion 7"
(separability). Any right-size criterion this round must be **8**; table row 9.

**3. C's entry should pre-run the r47 B-class legs.** The r49 model satisfies contract shape
(1 H1, H2 sections, 8-field head, `## N. Calibration bank`), but the r47 failures were content
self-consistency, not shape. Cheapest checks before filing: every `path:N` anchor resolves and
contains the quoted token; no dangling `§N`; `eight forms` vs the table's row count; the worked
example states one rule; any "does not contain" sentence carries its grep output.

**4. O must not inherit the r49 scope wording.** O's premise ("receipt_guard probes only HEAD
(`ls-tree HEAD`) and cites HEAD as `committed_sha`") is confirmed at
`tools/harness/receipt_guard.py:126-131` (`head = _head_commit(root)`; `ls-tree … head`) and
`:140-147` (`committed_sha={head}`). But the guard is **not** `validation.json`-scoped — the
`:178` claim in `round-49.md:232` points at a selftest fixture. O's report should cite
`:126-131`/`:140-147`, not `:178`.

## Measured evidence

```sh
grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l   # 1 (sherd)
grep -rniE '^- topic:.*(\bpastoral(ism)?\b|\bherding\b|\bhusbandry\b|\btranshumance\b|\blivestock\b)' corpus/knowledge/ | wc -l  # 0
find corpus/knowledge -iname '*pastoral*' -o -iname '*herd*' -o -iname '*husband*' -o -iname '*transhum*' -o -iname '*livestock*' | wc -l  # 0
sha256sum corpus/QUALITY.md                                  # e31724135f98629a… (6 criteria, :5-29)
sed -n '170,182p' tools/harness/receipt_guard.py             # :178 = selftest fixture, not guard scope
git show 8c78e6b:tools/harness/receipt_guard.py | sed -n '172,182p'  # same at r49
grep -n "_head_commit(root)\|ls-tree" tools/harness/receipt_guard.py # 126, 129 → HEAD-only
grep -n 'HONEST\|honest-stop' SCORECARD.md | tail            # 665, 838, 847, 886 — no r49 row
grep -n "^## " corpus/knowledge/culture-material/hunting-foraging-subsistence.md  # 15 H2s, Calibration bank :176
grep -n "^## " corpus/knowledge/culture-material/cartography-and-mapmaking.md    # 14 H2s, Calibration bank :214; 239 lines
wc -l corpus/knowledge/culture-material/*.md | grep -v " total$" | awk '{print $1}' | sort -n | sed -n '1p;$p'  # 103 … 239, n=27, median 149
```

## Not captured / unrun

- I ran no gate, selftest, sweep or round runner (in-tree runner execution is the r33/r36
  conformance incident; lane root is not a test surface). All claims above are inspection of
  bytes or read-only grep/find/sed.
- No external source was opened, so this report contributes no SOURCES rows and no tier calls.
- Cross-checked but not swept: rounds 11/17/22 rejections (their classes are already captured
  by `claims-freshness` and the correction pattern) and rounds 1-4 civ audits beyond the class
  rows quoted. `corpus/lessons/round-4-audit/civ-*.md` per-file counts were sampled, not
  re-derived; the class rows cited are verbatim from those files.
- Availability classes (r44 antigravity abort / opencode-go `reasoning_content`, r49 key-3 402,
  r36 hyper 402) are recorded in `reports/round-N/telemetry/*` and are out of QUALITY/gate scope;
  they are not counted as uncaptured mistakes here. The one availability-adjacent class that does
  belong to calibration is row 17 (declaration digest drift).
- Inference (not measured): that a `SCOPE:` line per gate is enough to stop gate-green
  overclaiming — no experiment was run on a reviewer reading a scope line.
