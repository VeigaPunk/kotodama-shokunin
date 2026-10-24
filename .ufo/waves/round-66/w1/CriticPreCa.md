# CriticPreCa — pre-data instrument attack on ACCEPT-CA-66 (claim Ca)

Scope: `reports/round-66/accept-ca.py` (rev 0, pre-data) vs. the four routed defects in
`corpus/lessons/round-65-verifier-spotcheck.md` §5. Attacked: shortcut classes, receipt
trust boundaries, and regex/leg fidelity. Instrument-only; no data seats reviewed.
Axis judged: calibration. No tools installed (none needed).

## Answers to the three scoped questions

**(1) Do the four D legs cover the whole routed defect set or only paraphrases?**
The set is covered 1:1 — D1–D4 each map to exactly one routed defect; nothing in §5 is
unaccounted, and CRITERION/QUOTES are extras. But every leg verifies a *paraphrase* of
its defect, and three of the four paraphrases are exploitable or inverted (below).
D1's leg checks that a self-authored receipt *asserts* resolvability plus a citation
count in the entry — it never fetches the URL or replays capture `20261024111013`, and
claims.json honestly delegates that to `review_only`. D3 and D4 are the weakest
paraphrases (findings F1, F3). D2 is the strongest (F4 nuances it).

**(2) Does passing D2 disposition R65-D2 or merely assert the new rule?**
It genuinely verifies the ordering invariant — `carrier^ == stamped` (accept-ca.py:126-129)
re-derives from committed history exactly the property that failed in round 65
(`lands=53a60275` interposed between stamp `3b1b5a67` and carrier). That is real
re-derivation, not assertion. Two qualifications: (a) scope is narrowed to the three
`final-measures-*.txt` receipts; the claim's own other record lands (s753-recapture,
seat-evidence, separability-real) get no ancestry check — an interposed commit before
those receipts is uncaught, so the defect class is only partially covered; (b) the leg
proves *ancestry*, not *execution* — a forged receipt stamped to `carrier^` with matching
`tree:`/`counter sha256` lines (both computable from git history) passes while falsely
claiming the counter ran at that revision. For a records claim that may be the right
evidentiary ceiling (claims.json `review_only` flags the generalization for non-author
judgment), but the predicate's "dispositioned" language should be read as *ordering
verified*, not *execution verified*.

**(3) Does QUOTES catch a lesson naming S800 but skipping S776?**
Yes — and it catches *any* single skipped id, because `gate_ids` can hold at most 25
distinct values (the regex `\bS(77[6-9]|7[89]\d|800)\b` at accept-ca.py:174 spans exactly
S776–S800) and the leg requires `len(gate_ids) >= 25` (line 177). `>= 25` is therefore
equivalent to "the complete set" — a lesson naming S800 but omitting S776 yields 24 and
fails. The `>=` phrasing hides this; a comment or explicit set comparison would make the
completeness requirement legible. Residual gap: `gate_ids` is counted over the **whole
file**, not the `## Gate` section — a Gate that names only S777–S800 while prose mentions
S776 once still passes, so the docstring's "Gate names the round's ids" is enforced as
"the file mentions all 25 ids" (F5). Spellings like `S 776`/`S-776` evade the regex but
fail-safe (count drops).

## Findings (ranked)

**F1 — D3 is satisfiable by one file and punishes recording dead seats (HIGH).**
`seat_paths = re.findall(r"(.ufo/waves/round-66/\S+\.md)", d3)` returns *occurrences*,
not distinct paths (accept-ca.py:146-151). A receipt listing the same existing report
path 8 times gives reported=8, existing=8 → PASS with **one** real seat report: the ≥8
floor measures path-mentions, not seats. Worse, `len(existing) == reported` (line 151)
inverts the routed defect's retention clause: naming a dead seat (path absent, with
last-error text) forces FAIL, so the instrument *incentivizes omitting dead seats* —
the exact class R65-D3 was routed to fix. The "per-seat status / last-error" requirement
is entirely unimplemented: `re.search(r"(?i)(seat|report|status)", d3)` is satisfied by
the receipt's own header comment (seat-evidence.txt:1,5). Finally, existence proves
*report files*, not *dispatch* — nothing binds the receipt to `swarm-registry.json` /
`spec-v2.json` (both named in the receipt's own comments), so 8 stub reports by hand
satisfy "dispatched". Concrete current state: seeded receipt names 65 paths
(including the literal phantom `.ufo/waves/round-66/w1/<SEAT>.md` caught from comment
line 5 — the regex has an unescaped leading `.` and `\S+` accepts it), 29 exist →
the seed cannot pass as written and must be rewritten at integration; the committed
receipt's provenance is whatever the integrator types.
*Smallest safe correction:* require `len(set(seat_paths)) == len(seat_paths)` (distinct),
drop `existing == reported`, parse per-seat `path status=ok|dead` lines and require
`status=ok` seats to exist on disk and `status=dead` seats to carry a `last-error=`
field; cross-check the named set against `swarm-registry.json`.

**F2 — D2 conflicts with criterion 17's re-stamp repair path (MEDIUM).**
Criterion 17 (QUALITY.md:55) sanctions correcting a mis-stamped receipt in place,
preserving original bytes below a marker. D2 requires `carrier^ == stamped`: a
conformant re-stamp that corrects `measured revision` to the *true* measured revision
makes carrier^ ≠ stamped → FAIL; a re-stamp that sets stamped := carrier^ to pass
would lie about the measured revision, violating criterion 17 itself. So for
final-measures receipts the criterion's repair path is dead text: an honest
mis-stamp can only be fixed by a failing commit. *Smallest safe correction:* either
scope criterion 17's re-stamp clause away for these receipts ("re-stamps must re-run
and re-commit, not amend"), or teach D2 to accept a re-stamp marker whose corrected
stamp is the true measured revision only when carrier^ equals it.

**F3 — D4 accepts a no-run, wrong-answer receipt; bans the honest verdict (MEDIUM).**
`SEPARABILITY: \d+ findings` + `acceptance_runs=\d+` + `"PARTIAL" not in d4`
(accept-ca.py:158-160). `acceptance_runs=0` passes — no evidence any acceptance ran;
`SEPARABILITY: 0 findings` passes even though claims.json `expected_findings` declares
two `Ca->REC` dependencies a correct run must report — a complete-but-wrong run passes.
Conversely `"PARTIAL" not in d4` forbids the honest partial verdict claim O was built
to produce (SEPARABILITY_PARTIAL, exit 2) — Ca demands a fully-completing run this
round specifically, which is defensible, but it means a budget-exhausted honest receipt
fails Ca even when claim O works as designed. *Smallest safe correction:* require
`acceptance_runs=[1-9]` and the expected-dependency count (≥2 findings, or the manifest's
expected list echoed), keep the PARTIAL ban but name it as "this round's run must
complete", and require the receipt to record the command + exit code.

**F4 — D2 residual: ancestry ≠ execution; scope narrowed (LOW-MEDIUM).**
Covered under Q2. Also cosmetic: the header's `git rev-parse main` (line 78) runs in
CWD, not `--root`, while `git_out` uses `-C root` — header can name a different repo's
main when `--root` differs (legs unaffected). *Correction:* `-C root` for symmetry;
document the execution-vs-ancestry ceiling in the docstring; consider extending the
ancestry leg to s753-recapture/seat-evidence/separability-real if those stay
claim-owned receipts.

**F5 — QUOTES counts ids file-wide, not in the Gate (LOW).**
A Gate section naming S777–S800 plus one prose mention of S776 passes, though the
stated contract is "the Gate names the round's ids". The regex is correct and the
missing-id case fails as required (Q3). *Correction:* scope `gate_ids` to the
`## Gate` section via the tool's own `gate_section()` rather than the whole file.

**F6 — D1 checks receipt text + file-wide citation counts, not bullet-level disposition (LOW).**
`\(S776\)` / `\(S753\)` count the whole games file (lines 100-105): an `(S776)` citation
anywhere in the entry plus a mancala bullet citing nothing yields s776=1, s753=0 → PASS
while the actual disposition target (the mancala bullet) is uncited. Receipt trust:
`"200" in d1` is trivially satisfied by "200 pdf" phrasing; the planted receipt was
mutated live during the wave (line 25 quote string appended between observations) —
pre-commit receipts are integrator-authored bytes, the leg's only hard anchors are the
citation counts. Also observed: the receipt's own lines are internally contradictory
(`old_capture status=000` line 8 vs `old_replay_status=200` line 21) and the leg passes
over it — no consistency requirement. *Correction:* scope the citation check to the
mancala bullet line (e.g., require a line matching `mancala.*\(S776\)` and not `\(S753\)`);
require the receipt to record fetch/replay command lines, not just result strings.

## Counterexample that stands on its own

Receipt `seat-evidence.txt` containing eight copies of the single line
`.ufo/waves/round-66/w1/RevGateRows.md` (a file that exists today) plus the word
"status" anywhere: `reported=8, existing=8` → **D3 PASS**, claiming ≥8 dispatched seats
for one real report. Smallest safe correction is F1's distinct-paths + per-seat-status
parse.

## Dependency note

`reports/round-66/separability-manifest.json` (named by claims.json `separability.check`)
does not exist on disk yet — a pending REC land, not an instrument defect. Both seeded
receipts are uncommitted working-tree files (lane main still at base `94209e8f`);
consistent with the do-nothing control (dry-run-ca.txt, all legs FAIL at base).

Report: .ufo/waves/round-66/w1/CriticPreCa.md
