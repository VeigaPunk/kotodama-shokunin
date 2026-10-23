# Round 57 build critic — mistake mining (CriticMistakeMining57)

Scope: one mistake for the round-57 lesson's `## Mistakes`. Leading candidate R56-M3 (round 56's claim O was met by an S-id-keyed checker); second candidate the koon1244 reject reason. Read: `reports/round-56/claims.json`, `reports/round-56/criterion11-controls-o.py`, `reports/round-56/telemetry/criterion11-controls-o.txt`, `.ufo/waves/round-56/predispatch/CriticClauseListO56.md`, `.ufo/waves/round-56/build/CriticClaimO56.md`, `.ufo/waves/round-56/build-spec.json`, `corpus/lessons/round-56.md`, `corpus/lessons/round-56-verifier-spotcheck.md`, `corpus/QUALITY.md:39`, `reports/round-57/accept-o.py`, `reports/round-57/controls-o.py`, `reports/round-57/telemetry/controls-o.txt`, `reports/round-57/claims.json`, and the fleet prompts `.ufo/prompts/kotodama-round-56.md` and `-57.md`, plus fleet commit `dc05427`.

Runs: `accept-o.py` (round 57) on the lane tool at HEAD and on `reports/round-57/controls/sidcheat-tool.py`, both from the lane root with `python3 -B`, writing only `/tmp`. I also ran one in-memory emulation (no file written). `git status --porcelain` showed no change from my runs. A ` M corpus/QUALITY.md` (criterion 10 only) appeared during the session from a peer seat; it is not mine. Nothing was installed.

## Verdict

**Use R56-M3's root cause; it is the stronger candidate.** Round 56 already had a rule against the cheat: QUALITY criterion 11, plus the prompt's universal-clause rule. The cheat was also named before the freeze. Two things in the rule let it through:
- Criterion 11 accepts a **stand-in** as the green control, and round 56's GREEN control was itself a checker that does no decoding and still passed every leg.
- Criterion 11 lets a clause be filed **review-only**. The one shortcut left, S-id hard-coding, was filed there three minutes before the declaration, and the question was then re-asked in the build wave, after the freeze.

The do-nothing rule (addendum §9) did not exist for round 56: it was committed 38 minutes after the declaration. koon1244 is the same class at lower stakes (a measured fix in hand, parked), so it serves as corroboration, not as a separate row.

## Proposed `## Mistakes` row (the L1 assigns the id)

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R57-M? | claim sizing: found-then-parked. Before the freeze, a seat measured or named a shortcut that reaches the target. The instrument's own GREEN was a no-work stand-in that passed every leg. The rule's review-only and later-wave routes absorbed the finding instead of fixing the counter. | `reports/round-56/criterion11-controls-o.py:10-14,65-95` (GREEN prints the expected findings by path suffix; `:81-83` adds a `moved-copy.md` branch); `reports/round-56/telemetry/criterion11-controls-o.txt:22-30` (GREEN exit 0, `DECODE PASS … moved_exit=1`); `.ufo/waves/round-56/predispatch/CriticClauseListO56.md:41,45` ("S-id hard-coding is then the only shortcut left. That is for the falsify-wave mutation tester"); `reports/round-56/claims.json:203` (review_only item 3); `.ufo/waves/round-56/build/CriticClaimO56.md:68-70`; `corpus/lessons/round-56-verifier-spotcheck.md:55-59,86-90` | Named before the freeze by the criterion-11 critic (CriticClauseListO56), but criterion 11 allowed it to be filed as review-only. Measured after the freeze by the build critic (CriticClaimO56) and reproduced by the closure. Mechanical capture first exists in round 57: `reports/round-57/controls-o.py`, receipt `reports/round-57/telemetry/controls-o.txt`. | Round 57 scores skip-the-work controls with the frozen counter before dispatch, and its green is a real implementation, not a stand-in. **Shown able to fail on control `sidcheat`** (`reports/round-57/controls/sidcheat-tool.py`, sha256 `e3060c1c…`, `GQ_MODE=sidcheat`): it passed 8/8 under ACCEPT-O-56 (spot-check `:59`) and gets `ACCEPT-O-57: FAIL`, exit 1, under round 57's counter (`controls-o.txt:13-23`, replayed below). The do-nothing control `base` (the round-56 landed tool, `3a13ab9c…`) also FAILs, and green `honest` PASSes (`controls-o.txt:2-12,79-89`). Rule text: amend QUALITY criterion 11 (exact text below). |

## Root cause: the rules that existed and why they did not stop the declaration

Timeline. Commit times are from `git log`. The two seat-report times are file mtimes, marked `[mtime]`, because those files were committed only in `c8af23f`.

| time (-03) | event | pointer |
|---|---|---|
| 17:56:46 | round-56 prompt dispatched; its §6 item 9 has the universal-clause rule but no do-nothing rule | fleet `.ufo/prompts/kotodama-round-56.md:343-351` |
| 18:14:09 [mtime] | the criterion-11 critic names S-id hard-coding as the remaining shortcut and routes it to the falsify wave | `CriticClauseListO56.md:45` |
| 18:16:37 | instruments revised (moved-copy leg added; the GREEN stand-in gains a `moved-copy.md` branch) | `045f458`; `criterion11-controls-o.py:81-83` |
| 18:17:07 | declaration; generalisation filed as review_only item 3 | `b4b7db9`; `claims.json:203` |
| 18:17:49 | build wave dispatched; the CriticClaimO56 prompt asks "(2) Could an implementation hard-code the 16 S-ids or fixture lines and pass?" | `.ufo/waves/round-56/build-spec.json` `items[35]` (name `CriticClaimO56`) |
| 18:33:32 | claim O landed | `7576fd4` |
| 18:34:10 [mtime] | CriticClaimO56 files "**Yes, measured**" (sidcheat 8/8) | `CriticClaimO56.md:66-70` |
| 18:55:27 | fleet addendum §9: "A target must be one a do-nothing control cannot reach … Before freezing, build the cheapest control that skips the claimed work" | fleet `dc05427` (`scripts/hyaku/lane-addendum.md`) |

I searched the round-56 dispatch contexts (`.ufo/waves/round-56/*.json`, `gen-*.py`) for `do-nothing`, `cheapest control` and `skip the claimed work`: no matches. This agrees with the closure (`spotcheck.md:91`).

Why the existing rules did not fire:
1. **Criterion 11's green is a stand-in by design** (`corpus/QUALITY.md:39`: "a stand-in landing is allowed in the copy only"). Round 56's GREEN printed the 16 + 10 expected triples by path suffix and decoded nothing. It passed all eight legs in the committed pre-dispatch receipt (`criterion11-controls-o.txt:22-30`). That is a skip-the-work checker reaching the target, but the rule reads a passing green as proof the target is meetable. When the moved-copy leg was added to kill path keys, the stand-in was taught the moved path (`criterion11-controls-o.py:81-83`) instead of being treated as a failed shortcut.
2. **Criterion 11's reds are single-clause near-misses of the green.** All 23 round-56 O controls are BASE, GREEN or RED-<leg> (receipt headings `:12-242`). None is an independent cheap implementation, so no control asks whether a checker that does no work passes.
3. **The review-only escape hatch.** Criterion 11 reserves review-only for a clause "no command checks mechanically" (a topic, what a source carries). Generalisation past fixture ids *is* mechanically checkable: CriticClaimO56 checked it with a renumbered copy (`:70`), and the closure checked it with `renum.md`, 15/15 against 0/15 (`spotcheck.md:61-83`). Filing it review-only is the "weaker stand-in" the criterion forbids. The criterion's non-author check covers the clause list "against the statement's words", not the review-only list's classification, so no seat ruled on it.
4. **The deciding question was asked after the freeze.** The L1 knew to ask it (`build-spec.json` items[35], question 2). It put the question in the build wave, 42 s after the declaration, where the only legal answers were disclosure or an honest stop (prompt §6 item 9: "Never narrow a target after landing").

## What round 57's instruments change, with controls shown able to fail

- **GEN** draws fresh S-ids (S100-S999), paths, Seat labels, hosts and filler from a seed taken from `os.urandom`, printed only after drawing (`accept-o.py:21-49,263-290`). No fixture identity exists to key on.
- **REAL** injects bare numeric references into real round-56 prose (`:50-56`).
- **MUTANTS** kills the three round-56 survivors in-process, with three neutral patches against patch-detectors (`:62-72`).
- **The control set** (`controls-o.py`) scores the round-56 tool, the round-56 S-id cheat (sha256 pinned at `controls-o.py:48,84-85`), a short-list checker, an any-ampersand checker, a hash-pinned selftest, and the pre-dispatch critic's identity cheats. All of these run before dispatch. The green is `honest`, a real implementation (`controls-o.py:27`). This is addendum §9 applied, and fix 1 above closed.

My replays today (lane HEAD `286288f`, `accept-o.py` sha256 `efd22767…`):

```
GQ_MODE=sidcheat python3 -B reports/round-57/accept-o.py --tool reports/round-57/controls/sidcheat-tool.py
  GEN FAIL lessons=5 failing=5 … REAL FAIL lessons=3 failing=3 … MULTI FAIL runs=10 …
  MUTANTS FAIL … survivors=['stop-at-first-bad-file', 'label-rename'] … KEEP PASS  FORMAT PASS  SELFTEST PASS … 27/27
  ACCEPT-O-57: FAIL   (exit 1)
python3 -B reports/round-57/accept-o.py          # tools/check-gate-quotes.py sha256 3a13ab9c… (round-56 landed tool)
  GEN FAIL … REAL FAIL … MULTI PASS  MUTANTS FAIL … survivors=['double-decode', 'stop-at-first-bad-file', 'label-rename']
  KEEP PASS  FORMAT PASS  SELFTEST PASS … 38/38
  ACCEPT-O-57: FAIL   (exit 1)
```

Both agree with `controls-o.txt:2-23` (same failing legs; the seeds differ by design).

## Counterexample against the fix: the same found-then-parked move recurs in round 57

The O statement's selftest half can still be met without writing behavioural tests. `reports/round-57/claims.json` O `review_only[2]` names this residual: "a selftest that tells the mutant patches from the neutral ones by inspecting the patch code could still kill without testing behaviour … the falsify wave reviews the landed selftest". That is the round-56 move: a known reachable shortcut filed as review-only and handed to a later wave.

I measured it in memory, with no file written. I loaded the lane tool at HEAD (the round-56 selftest, with no behavioural kill), wrapped `selftest` in about 12 lines of bytecode inspection, and applied each of accept-o's six patches exactly as `MUTANT_RUNNER` does, with random tokens. The inspection does three things:
- it flags `decode_html_references` when it makes more than one CALL;
- it flags `check` when it has an `IS_OP` or a `*NONE*` jump;
- it flags `run` when `co_consts` contains `html_entity`.

```
INSPECTION-SELFTEST exits {'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1,
                           'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}     (Python 3.14.8)
```

This is exactly the MUTANTS PASS signature (`controls-o.txt:85`). Combined with the real `;?` grammar, which GEN, REAL and MULTI require anyway, the checker would print `ACCEPT-O-57: PASS` while its selftest tests none of the three behaviours. That contradicts O's `surface` ("its selftest gains the power to fail on three behaviours … that the base selftest does not test"). [INFERENCE] I did not assemble and run the full checker, because a critic seat writes only its report. The other six legs are unaffected by `selftest()` internals except SELFTEST, which needs exit 0 unmutated (shown: `none: 0`).

- **Impacted axes:** operability (the counter accepts a selftest without behavioural kill power) and calibration (a lesson or report sentence calling MUTANTS PASS "behavioural" would be false provenance).
- **Defect or tradeoff:** a disclosed tradeoff. Any in-process patch can be inspected, so no counter fully closes it. A closure that builds this control can still rule on it as it ruled on round 56, so treat it as a live risk, not a saturated one.
- **Smallest safe correction** (no counter change: the build wave is scoring, so changing the counter now would be a post-data change):
  1. Falsify wave, mechanical. On a scratch copy of the landed tool, apply the three mutants as **source edits** to the file, not in-process patches. Add three source-level neutral rewrites whose bytecode differs but whose behaviour is the same (for example `once, found = f(line); return once, found` written as `result = f(line); return result`, a loop rewritten as a comprehension, the label built by concatenation). Run `--selftest` from the file. Require 3 kills and 0 neutral failures.
  2. Same wave: `grep -nE '\b(dis|inspect|__code__|co_code|co_consts|co_names|getsource|_orig_)\b'` over the landed `selftest()` body must print nothing.
  3. Records: word MUTANTS as "kill power under in-process patches". Cite the falsify probe of item 1, not the counter, for "behavioural".

## Erratum owed: R56-M3's `captured-by` cell is false

`corpus/lessons/round-56.md:158` says the criterion-11 pre-dispatch critic "caught part of it … but not the S-id-keyed cheat". It did name it before the freeze (`CriticClauseListO56.md:45`, `[mtime]` 18:14:09, before `b4b7db9` at 18:17:07). Append in round 57's errata (filed bytes not rewritten):

- old (`round-56.md:158`, captured-by): `QUALITY criterion 11's pre-dispatch critic (CriticClauseListO56) caught part of it (the moved-copy leg, hex and other named references, multisets) but not the S-id-keyed cheat`
- new: `QUALITY criterion 11's pre-dispatch critic (CriticClauseListO56) caught the moved-copy, hex, named-reference and multiset gaps and named S-id hard-coding as the remaining shortcut (CriticClauseListO56.md:45), routing it to the falsify wave; the declaration filed it as review-only item 3 (reports/round-56/claims.json:203)`

## Rule fix (records item; the L1 owns `corpus/QUALITY.md`)

A peer currently has an uncommitted criterion-10 edit in that file; criterion 11's text is untouched.

- old (`corpus/QUALITY.md:39`): `A green control is a copy where every clause holds, and there the command exits 0; a stand-in landing is allowed in the copy only and is never landed.`
- new: `A green control is a copy where every clause holds, and there the command exits 0; a stand-in landing is allowed in the copy only and is never landed. A stand-in that prints the expected outputs without doing the claimed work is also the claim's skip-the-work control: scored as a red it must exit non-zero, and so must the last measured shortcut against the same tool; if either exits 0, the counter is fixed before dispatch, never filed as review-only. A clause a seat has checked mechanically (a renumbered or regenerated input) is not review-only.`
- Shown able to fail: under this text, round 56's own receipt fails the declaration (GREEN stand-in exit 0, `criterion11-controls-o.txt:22-30`), and so does `sidcheat` under ACCEPT-O-56 (`spotcheck.md:59`). Round 57's receipt passes it (`controls-o.txt`: `sidcheat`, `base` and the stand-ins exit 1; `honest` exits 0).

## Second candidate: koon1244 (same class, weaker)

`corpus/lessons/round-56.md:83` gives the reason "its only quotes are RDF triples with no quotable passage". Round 56's own S379 quotes a JSON field of the sibling languoid (`round-56.md:44`), and the closure found quotable `.n3` and `.json` fields (`spotcheck.md:129`). The falsify seat gave the exact replacement before the records commit (`.ufo/waves/round-56/falsify/ReviewExcludedSources56.md:13,26`). Commit `c8af23f` then wrote **both** the false reason (`:83`) and the note that a seat disagrees with it (`:146`) (`git blame` on both lines).

This is found-then-parked again. It is the third instance this lesson can cite, after R56-M1 (a fix "carried to Frontier instead of applied", `round-56.md:156`) and R56-M3. It is weaker as a standalone row: the outcome was right (not registered, 4/4 rejects agree), no claim depended on it, and the erratum is already routed (`reports/round-57/claims.json` `records_not_claims[0]`). Put it in R57-M?'s evidence column as a recurrence pointer, not as its own row.

## For the L1

- Checks to run: the falsify-wave source-level mutant and neutral probe, and the grep in item 2 above, on the landed `tools/check-gate-quotes.py`.
- Do not change `accept-o.py` this round (post-data).
