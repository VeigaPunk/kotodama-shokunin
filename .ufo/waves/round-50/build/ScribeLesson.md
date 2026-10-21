# ScribeLesson — round 50 lesson skeleton (kotodama, hyaku phase 2, attempt 1)

Seat: `ChousaR27R2.ScribeLesson-4` · role: scribe (leaf; no dispatch; no background jobs) · lane: `kotodama-shokunin`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Write scope: this report only. No lane file was edited; `corpus/lessons/round-50.md` is **not** created here (frontier instruction: deliver text in the report).

## 1. Assigned item

Draft the skeleton of `corpus/lessons/round-50.md` in the round-49 lesson style: intake of `corpus/lessons/round-49-verifier-spotcheck.md`; `## Mistakes` table (class · evidence pointer · captured-by · fix) with M1 = the r49 claim-separability rejection; `## Gate` table placeholder for new S-rows; status / used-by change-log section.

## 2. Evidence opened (read-only, this session)

| claim | evidence (path:line) | observed |
|---|---|---|
| r49 style: 4 contract lines, `## Gate`, `## Registry changes`, `## Mistakes` table of 4 columns, `## Frontier`, `## Verification` | `kotodama-shokunin/corpus/lessons/round-49.md:1-6, 18, 84, 115-161, 213, 253` | yes, as described |
| r49 Mistakes table has 23 rows; class-cell wording and `captured-by` column | `round-49.md:137-161` | yes |
| r49 spot-check verdict on separability | `round-49-verifier-spotcheck.md:17` | "REJECTED-HONEST-STOP on claim separability … C cites the registry S creates; the c_without_s runner leg retained inline URLs rather than the required registry rows" |
| r49 spot-check admitted C and S with supported outcomes | `round-49-verifier-spotcheck.md:12-13` | agree on admit and reject rows |
| Round-50 claims and the separability contract | `kotodama-shokunin/reports/round-50/claims.json:10, 17-18, 36-37, 48-51` | C lands pastoralism entry + `corpus/README.md`; O lands 3 tool paths; Ca lands checker + fixture + QUALITY.md; `separability_contract` names the r49 mistake as motivating |
| SOURCES registry tail | `kotodama-shokunin/corpus/SOURCES.md:76` (S047), `:28` (header) | 47 rows, last id S047; append-only; `status/recheck/used-by` changes logged old→new in a round lesson |
| QUALITY criteria | `kotodama-shokunin/corpus/QUALITY.md:5-29` | criteria 1–6 only; criterion 6 is the source-authority rule added in r49; **no criterion 7 and no `separab` match** |
| Ca landing targets | glob of `tools/check-claim-separability.py`, `reports/round-50/**`, `corpus/knowledge/culture-material/pastoralism*` | checker **absent**; `reports/round-50/` holds `claims.json`, `telemetry/`, `census-before.txt`, `declaration-freshness.json` only; the r49 fixture `reports/round-50/separability/r49-fixture.json` **absent** (direct read → not found); pastoralism entry **absent** |
| wave assignment names this seat | `kotodama-shokunin/.ufo/waves/round-50/build-assignments.json:72` | `ScribeLesson` → `ChousaR27R2.ScribeLesson-4` |

Consequence for the draft: M1's *captured-by* cell must read **pending** — the checker, fixture and criterion 7 do not exist in the lane at this read, so the skeleton cannot claim the mistake is captured. It is written as a placeholder to be flipped only by the Ca receipt.

## 3. Findings (scoped)

**F1 — M1 is recorded as open, not captured (calibration).** Nothing in the lane today detects C→S coupling. The r49 record (`round-49-verifier-spotcheck.md:17`) is the only evidence. Captured-by flips to the checker only after `tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json` exits 1 naming the C→S dependency (Ca `after_required`, `reports/round-50/claims.json:50`).

**F2 — structural gap in the declared separability contract (highest-risk item; not in any claim's scope).** `reports/round-50/claims.json:10` says C "cites SOURCES rows opened by the frontier step (not a claim)". The checker's semantics (Ca `claims.json:48` contract: X depends on Y when X's bytes match Y's export regex or name Y's land path) only see *declared* claims. The S-rows C cites exist in no declared claim's `lands`, so the checker as specified would report C **separable** from base, and the dynamic leg (base + C.lands only) would still carry base `corpus/SOURCES.md`. That is the r49 failure with the same shape: the counterfactual passes because the registry it needs is simply absent, not because C is independent of it. Options for Ca/main to choose (I do not decide): (a) declare the frontier registry rows as a fourth claim/land with an `exports` regex such as `\bS0(4[8-9]|[5-9]\d)\b`; or (b) make the acceptance leg of C include "every cited S-id resolves in the counterfactual tree's `corpus/SOURCES.md`", which would fail C in base and so surface the coupling. Either choice must be in the Ca receipt before the round-50 lesson claims separability.

**F3 — the lessons index needs a new row, not an edit.** `corpus/lessons/README.md:104-106` (34 rows, filed) indexes round-49 but not `round-49-verifier-spotcheck.md`; the new round-50 lesson adds one row. Per the index's own rule (`corpus/lessons/README.md:18-19, 116`) this is a new row, never an edit of a filed row. Owner: parent. Recorded here; not applied.

**F4 — carried, not re-mined.** The round-49 "still uncaptured" list (`round-49.md:163-168`: r11 freshness, r35 placeholder token, r42 corpus overwrite, r44 carried-candidate, r47 size criterion, r9 write-boundary, lessons-record convention) is carried unchanged. The r50 Ca/O landings do not capture any of them; the draft lists them as carried, so the r50 lesson does not claim them.

## 4. Draft skeleton — `corpus/lessons/round-50.md` (text only; not written to the lane)

````markdown
# Round 50 — lesson (kotodama, hyaku phase 2, attempt 1)

source: `reports/round-50/claims.json` (declarations); `reports/round-50/validation.json` (acceptance receipt — **not yet written**); the URLs opened in `## Gate`
verified-at: 2026-10-21 — lane `kotodama-shokunin`, base `4ad2683`; Gate rows opened the same day
recheck: whenever a `corpus/SOURCES.md` row's `status`, `recheck` or `used-by` changes (log old→new in this lesson), and on the per-row `recheck` cadences
scope: the round-50 record — Gate evidence for each new SOURCES row (S048 upward), registry changes made before landing, mined mistakes and frontier; it admits nothing and certifies no verdict

Round 50 is the first hyaku-phase-2 round. Claims: **C** coverage — `culture-material/pastoralism-animal-husbandry.md` (pastoralism/herding register, verified-fresh at 0 filename and 0 topic owners); **O** operability — `tools/harness/receipt_guard.py` and `tools/check-readme-revisions.py` correct under jj colocation, plus the counting probe `reports/round-50/jj-colocation-probe.py`; **Ca** calibration — `tools/check-claim-separability.py` on the frozen r49 fixture, plus QUALITY criterion 7. Frontier step (not a claim): SOURCES rows opened this round, and one mined mistake.

## Gate

Each row below was opened on 2026-10-21 by the seat that wrote it. Quotes verbatim, ≤25 words, with location.

<!-- one line per row; the frontier seat fills these. Do not author rows here. -->
- S048 — `<URL>` — accessed 2026-10-21 — `<location>`: "`<verbatim ≤25 words>`". Grounds: `<what the row supports>`. Tier: `<A|B|C>` per QUALITY criterion 6.
- _(S049 onward: one line each, same form)_

Admitted: `<pending — Ca/L1 receipt>`. Rejected: `<pending>`. spot-check: `<pending — non-author verifier sentence>`.

## Registry changes before landing

- `<pending — any normalization of a row authored this round, logged with old→new>`

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| **M1 — r49 claim-separability REJECTED-HONEST-STOP**: C cited the SOURCES registry rows S created in the same round; the `c_without_s` leg kept inline URLs instead of removing S's rows, so the counterfactual did not verify | `corpus/lessons/round-49-verifier-spotcheck.md:17`; `reports/round-50/claims.json:10` (names it as motivating) | **pending** — `tools/check-claim-separability.py` absent at this draft; fixture `reports/round-50/separability/r49-fixture.json` absent; QUALITY criterion 7 absent (`grep -ci separab corpus/QUALITY.md` → 0 at draft). Flips to captured only on the Ca receipt | checker exits 1 naming `SEPARABILITY_DEPENDENCY C->S` on the fixture (1/1); `--selftest` with negative and positive controls; run on `reports/round-50/claims.json` exits 0; QUALITY criterion 7 cites the spot-check. **Open question for Ca:** the frontier-step rows are not a declared claim, so the checker needs an explicit registry land or an S-id resolution acceptance leg (see F2) |
| _(M2+: none mined in this draft; carried list below, not re-mined)_ | | | |

Still uncaptured, carried from round 49: r11 freshness threshold (L0 open), r35 placeholder-token blind spot, r42 pre-commit corpus overwrite, r44 carried-candidate ruling, r47 right-size criterion (the Ca/QUALITY leg does not add a size criterion), r9 write-boundary gate, lessons-record convention.

## Status and used-by change log

Every SOURCES field change is logged here, old → new, per the registry header (`corpus/SOURCES.md:10-12`).

| row | field | old | new | reason |
|---|---|---|---|---|
| _(pending)_ | `used-by` | `—` | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` | a row cited by C now names the entry (only rows the entry cites) |

## Frontier

- **Separability coupling of frontier rows (new, from F2).** C cites registry rows that exist only after the frontier step; the declared manifest does not carry them. Next round: make the registry a declared land or an acceptance leg of C, so a missing S-id fails the counterfactual instead of passing it.
- **Right-size criterion (r47, carried).** `corpus/QUALITY.md` still has no size leg after this round's Ca landing; the r48 band (103–239 lines, n=26) stands.
- **Freshness threshold (r11, carried).** Pause stays in force; L0 open.

## Verification (to run after landing; not run by this draft)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json; echo $?   # expect exit 1, SEPARABILITY_DEPENDENCY C->S
python3 -B tools/check-claim-separability.py --selftest                                             # negative + positive controls
python3 -B tools/check-claim-separability.py reports/round-50/claims.json; echo $?                   # expect exit 0
grep -ci separab corpus/QUALITY.md                                                                  # expect >= 1 (criterion 7)
find corpus/knowledge -name '*.md' | wc -l                                                          # expect 226
wc -l corpus/knowledge/culture-material/pastoralism-animal-husbandry.md                              # expect <= ~250
python3 -B reports/round-28/readme/sweep.py rows 226 files 226 topic_mismatch 0                     # sweep green
python3 -B tools/harness/receipt_guard.py --selftest                                                # all prior controls retained
python3 -B tools/check-readme-revisions.py --selftest
python3 -B reports/round-50/jj-colocation-probe.py --tools-root <tree>                              # expect 0/3 on landed tools
```
````

## 5. Unrun checks

- No lane command run beyond the reads and globs listed in §2. Nothing in §4's `## Verification` block was executed; each line is an expectation to be measured by the main agent after landing.
- The S-row Gate lines are placeholders; no SOURCES URL was opened by this seat (frontier step is not assigned to this seat's report).
- No tool was installed or updated by this seat.

## 6. Hand-off to the integrator (main agent)

1. Land M1 as pending. Flip to captured only on the Ca receipt.
2. Decide F2 before C's `after_required` is read as a pass: the separability contract as written does not see the frontier rows. (Ca/L1 decision; not made here.)
3. Add the round-50 row to `corpus/lessons/README.md` as a new row when the file lands (F3).
4. Lane writes stayed inside `.ufo/waves/round-50/build/ScribeLesson.md`; no production file was touched.
