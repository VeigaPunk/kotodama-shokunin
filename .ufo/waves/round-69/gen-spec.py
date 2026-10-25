#!/usr/bin/env python3
"""Round-69 wave spec generator (kotodama, hyaku run 6).

Emits .ufo/waves/round-69/spec-v1.json: one v1 wave of 32 seats (policy v1
band 32-64), 21 of them attack roles (reviewer / critic / mutation-tester /
sentinel / revenger) = 65.6% >= 25%.

Every item is a distinct, concrete pre-data work item serving the round's
three frozen claims (O2 operability, Ca2 calibration, D2 depth), the frontier
step and verification. No seat edits production bytes: each writes exactly one
report file; the L1 is the single integration owner.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "793f79746712a79f915bb481215e54bbea8b5e7a"
REPORTS = LANE + "/.ufo/waves/round-69/w1"

CONTEXT = """# Goal
Kotodama round 69 (hyaku run 6, 202610-24): ONE v1 wave of 32 seats, build and
attack together. Lane repo %s (jj-colocated). Base revision %s. All
lane-relative paths below resolve under that repo; use ABSOLUTE paths in every
command you run.

Three frozen claims (reports/round-69/claims.json, committed at the declaration):
- O2 (operability, capability acquisition): the lane gains a runnable,
  lane-shaped supersession-settlement fixture harness
  (tools/check-settlement-fixture.py) whose NEGATIVE case is the
  missing-used-by defect class the round-68 counter never exercised.
  Predicate: every leg of reports/round-69/accept-o.py prints PASS.
- Ca2 (calibration, records): the count of unannotated mismatches between the
  lane's filed self-assessment (SCORECARD round-68 section, LOG round-68
  entry, filed fleet round-68 report) and the committed round-68 receipts
  drops to zero, each closed by an APPENDED correction row.
  Predicate: every leg of reports/round-69/accept-ca.py prints PASS and the
  MISMATCHES leg prints unannotated_mismatches=0.
- D2 (depth, the lane's lowest owned axis): SKILL.md gains a
  `### Registry correction chains` decision table (five chain states, each with
  row shape, writer's next action, a named error signature and an evidence
  pointer), the five signatures also listed under `## Error patterns`, and the
  table citing a mined S-row whose used-by names SKILL.md.
  Predicate: every leg of reports/round-69/accept-d.py prints PASS.

WHAT IS ALREADY COMMITTED (the pre-data instruments you attack):
  reports/round-69/claims.json, reports/round-69/accept-o.py,
  reports/round-69/accept-ca.py, reports/round-69/accept-d.py,
  tools/check-settlement-fixture.py, reports/round-69/telemetry/controls.txt
  (the green and do-nothing pre-data controls).
WHAT IS NOT LANDED YET (the data): the SKILL.md decision table, the S859
  registry row, reports/round-69/corrections-r68.md and the appended
  corrections in LOG.md / SCORECARD.md / corpus/lessons/round-69.md.

ABSOLUTE PATHS AND THE REPORT TRAILER
Every `Report:` trailer path you are given is relative to %s - write it at
%s/<that path>. Never write a relative path into the fleet root.

WRITE SCOPE AND BOUNDS (hard)
You may write EXACTLY ONE file: your own report file named below. Do not edit
production files (SKILL.md, corpus/**, LOG.md, SCORECARD.md, reports/round-69/**,
tools/**) - the L1 is the single integration owner and integrates your findings.
Never write to the fleet repo %s or to any sibling lane repo
(/home/vgpnk/Projects/shokunin/*-shokunin except your own lane). Never run
`git commit`, `git add`, `git push`, `git stash`, `git checkout`, `git switch`,
`git reset`, `git pull`, and never run a mutating `jj` command; never touch the
lane Git index or the lane jj state. Use scratch under /tmp for any mutation
you need to demonstrate (copy the file, mutate the COPY, re-run the counter
against the copy). Read-only git (log, show, diff, status, ls-files,
rev-parse) is fine.

TOOLING AUTHORIZATION
You may install or upgrade a tool that genuinely helps your task, but read
/home/vgpnk/.omp/agent/RULES.md FIRST and follow it (official channels,
update-safety gate, install record: tool, version, channel, reason). PACMAN
GUARD: all pacman transactions are PAUSED host-wide on this host - install via
`uv tool`, `npx` or an official binary in ~/.local/bin, or file an L0
question. Never `pacman -Sy/-Syu/-U/-R`, never downgrade, never restart a host
service.

NO NETWORK FETCHING of external sources this round: the round's only new
registry row (S859) is the lane's own re-runnable check (own-work). You may
read local files freely.

REPORT FORMAT
Write markdown with the exact commands you ran and their real output. State
findings as VERDICT lines (e.g. `VERDICT: PASS`, `VERDICT: FAIL`,
`VERDICT: NOT-EVALUATED`) and never as an assertion. If an artifact you need
is missing, say so and record it as a finding - do not fabricate output.
""" % (LANE, BASE, LANE, LANE, "/home/vgpnk/Projects/shokunin")

PRE = """Time-box: return within 15 minutes with your best findings and evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
"""

BOUNDS = """
Lane repo: %s (jj-colocated). You are READ-ONLY on production bytes: no git commit/add/push/stash/checkout/switch/reset/pull, no mutating jj, no lane Git index or jj state changes, no writes outside your own report file and /tmp scratch. Do not write to the fleet repo %s or to any sibling lane repo.
Tooling: read /home/vgpnk/.omp/agent/RULES.md before installing anything; PACMAN IS PAUSED host-wide (use uv tool / npx / an official binary in ~/.local/bin, or file an L0 question). No external network fetching this round.
Every `Report:` trailer path is relative to %s - write it at %s/<that path>.
Write exactly one file: your report file named below. Do not edit production files.
""" % (LANE, "/home/vgpnk/Projects/shokunin", LANE, LANE)

ITEMS = [
    ("MutO1", "mutation-tester", ["operability"],
     "Mutation-test reports/round-69/accept-o.py. Copy it to /tmp and delete the NEGPROBE leg; run the copy against the lane tree and show that the counter no longer prints ACCEPT-O-69: PASS. Then delete the STAMP leg in a second copy and show the same. Paste both outputs. State whether the counter can be fooled by removing its own independent check."),

    ("MutO2", "mutation-tester", ["operability"],
     "Mutation-test reports/round-69/accept-o.py. Copy it to /tmp and change the FIXTURE leg to accept 'FIXTURE: 2/3' (or any non-3/3 value); show the counter goes red on the real lane tree. Also mutate the LANE leg to accept 'pending=1 missing_paths=0' and show it goes red. Paste the outputs."),

    ("MutO3", "mutation-tester", ["operability", "calibration"],
     "Mutation-test the R68FROZEN leg of reports/round-69/accept-o.py: copy the counter to /tmp and point the R68FROZEN comparison at the wrong receipt (for example final-measures-ca.txt for accept-o.py); show the leg fires. Then verify independently that sha256 of reports/round-68/accept-o.py equals the sha256 recorded in reports/round-68/telemetry/final-measures-o.txt (line starting '# counter sha256 (self):'), and the same for accept-ca.py and accept-c.py. Paste all outputs."),

    ("MutO4", "mutation-tester", ["operability"],
     "Mutation-test tools/check-settlement-fixture.py: copy it to /tmp, remove the negative case (the fixture whose used-by file is absent), and show the harness no longer proves the missing-used-by class is caught. Then re-derive the negative case by hand: build a tiny lane-shaped corpus/SOURCES.md in /tmp with one mined row whose used-by names corpus/knowledge/a.md, do NOT create that file, run `python3 -B %s/tools/check-supersession-settlement.py --scan --root /tmp/<your-dir>` and paste the SETTLEMENT line. Does it report missing_paths=1?" % LANE),

    ("MutO5", "mutation-tester", ["operability"],
     "Mutation-test the negative assertion inside tools/check-settlement-fixture.py: copy it to /tmp and make the negative case assert missing_paths=0; show the harness prints FAIL fixture-negative and exits non-zero. Then run the unmodified harness `python3 -B %s/tools/check-settlement-fixture.py --selftest` and paste the output. Does the harness fail when the class it claims to catch is not caught?" % LANE),

    ("RevO1", "reviewer", ["operability"],
     "Re-derive claim O2 end to end from committed bytes. Run `python3 -B %s/reports/round-69/accept-o.py --root .` and paste every leg line and the final ACCEPT-O-69 line. Then re-run each leg's own command by hand (the fixture selftest, the lane scan, the independent negative probe) and say whether the counter's numbers are the ones you observe. Report the exact revision you measured (git rev-parse main)." % LANE),

    ("RevO2", "reviewer", ["operability", "calibration"],
     "Verify the round-68 counters were not amended: run `git -C %s diff --name-status 793f79746712a79f915bb481215e54bbea8b5e7a main -- reports/round-68` and `git -C %s diff 793f79746712a79f915bb481215e54bbea8b5e7a main -- reports/round-68/accept-o.py reports/round-68/accept-ca.py reports/round-68/accept-c.py`. Report whether the round-68 counters and their receipts are byte-identical to the base. Paste both outputs." % (LANE, LANE)),

    ("RevO3", "reviewer", ["calibration"],
     "Re-derive the round-68 operability receipt's leg arithmetic from committed bytes: `grep -cE '^[A-Z0-9_]+ (PASS|FAIL) ' %s/reports/round-68/telemetry/final-measures-o.txt` and the same for each of PASS and FAIL, and list the leg names. State the exact (pass, total) pair. Then grep the filed surfaces for the string '9/10 legs PASS' (SCORECARD.md round-68 section, LOG.md round-68 section, /home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md) and list every hit with file and line. Paste everything." % LANE),

    ("RevO4", "reviewer", ["calibration"],
     "Attack the LEGCOUNT detector of reports/round-69/accept-ca.py: copy the counter to /tmp and make the corrections-file parser accept ANY row (drop the class whitelist); run the copy with --selftest and show the DO-NOTHING fixture still fails. Then run the unmodified `python3 -B %s/reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin` and paste the EVAL lines. Does the counter's do-nothing control still bite?" % LANE),

    ("RevO5", "reviewer", ["calibration"],
     "Attack the DEADPOINTER detector of reports/round-69/accept-ca.py: copy the lane's corpus/lessons/round-68.md to /tmp, add a bogus row line containing 'R68-M9', and show the detector stops firing on that id; then show that adding a row for a DIFFERENT id does not silence it. Use copies under /tmp only; do not modify the lane tree. Paste the commands and outputs."),

    ("RevO6", "reviewer", ["calibration"],
     "Attack the OVERREACH detector of reports/round-69/accept-ca.py: copy SCORECARD.md to /tmp, change the round-68 calibration row's verdict cell from 'improved ...' to 'not verified as declared ...', and show the detector stops firing; then change it to 'harmed' and show it still fires. Use copies under /tmp only. Paste the commands and outputs."),

    ("RevO7", "reviewer", ["calibration"],
     "Attack the corrections-file parser of reports/round-69/accept-ca.py: build a corrections table under /tmp where the surface cell is spelled differently (e.g. 'scorecard.md' or 'SCORECARD.md ' with a trailing space, or the class lower-cased) and show whether the pair is still counted as covered. Report which spellings count as covering and which do not. Paste the outputs."),

    ("CritD1", "critic", ["depth"],
     "Attack claim D2's decision table content BEFORE it is written: read tools/check-supersession-settlement.py (function classify) and reports/round-69/claims.json, and derive the exact chain-state taxonomy the table must carry. For each state name the precondition the code actually tests (the exact status/used-by/limiter condition) and the writer's next action that the code's own docstring and the round-68 ledger rulings imply. Name any state, term or condition that a reader could get wrong. Return the table skeleton as markdown."),

    ("CritD2", "critic", ["depth"],
     "Attack claim D2's error-signature requirement: read SKILL.md's `## Error patterns` section in %s and decide what a named error signature for this table must look like to be usable there (a short, observable signature; a reading; no filler). Give five candidate signature names for the five chain states, each distinct, each naming an observable condition rather than a category. Cross-check that none of them collides with an existing observation row in `## Error patterns`." % LANE),

    ("CritD3", "critic", ["depth", "adjacency"],
     "Attack claim D2's evidence rule: the table's Evidence column must cite at least one path that EXISTS at the measured revision. List every path the round-68 settlement work actually committed that a reader can re-run (tools/check-supersession-settlement.py, reports/round-68/dispositions/dedup-ledger.tsv, reports/round-68/telemetry/final-measures-o.txt, corpus/lessons/round-68.md, the r68 ledger) with `test -f` output, and say which are honest to cite for which state row. Flag any that would be a dead pointer."),

    ("CritD4", "critic", ["depth", "calibration"],
     "Attack the sourced leg of claim D2: the table must cite a mined S-row whose used-by names SKILL.md, and the round-69 lesson's `## Gate` must record that row's URL/repo-path, access date and a <=25-word located quote. Read %s/corpus/SOURCES.md, the r68 rows and the round-68 lesson Gate, and judge whether an own-work row (kind own-work, tier A) pointing at the lane's own re-runnable settlement check is admissible under the fleet SOURCES contract v1, or whether the lane needs an external source. Give the ruling with the contract line that decides it." % LANE),

    ("CritD5", "critic", ["depth"],
     "Attack claim D2's claim-sizing: build the cheapest do-nothing control for the depth target (a copy of the lane tree with the decision table absent), score it with `python3 -B %s/reports/round-69/accept-d.py --root <your-copy>` and paste the output. Confirm the do-nothing control cannot reach the target. Then state whether a table with fewer than five states, or with states that are not the code's own classes, could still pass the counter." % LANE),

    ("CritO1", "critic", ["operability"],
     "Attack claim O2's predicate: could a do-nothing control reach 'every leg of accept-o.py prints PASS'? Copy the lane tree to /tmp, delete tools/check-settlement-fixture.py in the COPY, and run the unmodified counter against the copy: paste the output. Then copy the tree again, keep the tool but break its negative case, and paste the output. State whether the predicate is reachable without the claimed work."),

    ("CritO2", "critic", ["operability"],
     "Attack the substance of the new fixture harness: read tools/check-settlement-fixture.py and tools/check-supersession-settlement.py, and judge whether the harness's three cases really exercise the shape the live registry has (11-column rows, a `## Registry` section, `## Paths` and `## Search log` sections, a mined successor and a queued target, a used-by path under corpus/knowledge/). List any structural difference between the fixture registry and the live corpus/SOURCES.md that could make the harness green while the live registry is not."),

    ("CritO3", "critic", ["calibration", "operability"],
     "Attack the round-69 declaration as a whole: read %s/reports/round-69/claims.json and the three counters. For each claim, name (a) the exact predicate sentence, (b) the counting command, (c) the target value, (d) the kill rule, (e) whether the do-nothing control was scored before data (reports/round-69/telemetry/controls.txt), and (f) any clause that cannot be re-derived by one command over committed bytes. Flag every 'all', 'complete', 'every' style universal that the counting command does not enumerate." % LANE),

    ("MutC1", "mutation-tester", ["calibration"],
     "Mutation-test the remedy rule of reports/round-69/accept-ca.py: copy it to /tmp and make the DEADPOINTER remedy ignore whether the referenced row exists (remedy = covered only); run the copy against the lane tree and show the counter's verdict changes. Paste both the original and mutated outputs side by side and state which behaviour the lane depends on."),

    ("MutC2", "mutation-tester", ["calibration"],
     "Mutation-test the OBSERVED leg of reports/round-69/accept-ca.py: copy it to /tmp and hard-code the observed legs as (9, 9) instead of deriving them from the receipt; run the copy and show the LEGCOUNT detector's live/uncovered output changes. Paste the outputs. Then state, from the committed bytes, the true (pass, total) pair."),

    ("MutD1", "mutation-tester", ["depth"],
     "Mutation-test the STATES leg of reports/round-69/accept-d.py: copy it to /tmp and accept four states (drop settled-split); run the copy against a fixture SKILL.md carrying a four-state table and show it no longer rejects it. Then run the unmodified `python3 -B %s/reports/round-69/accept-d.py --selftest` and paste the output. Does the counter kill the four-state shortcut?" % LANE),

    ("MutD2", "mutation-tester", ["depth"],
     "Mutation-test the SIGNATURES leg of reports/round-69/accept-d.py: copy it to /tmp and drop the requirement that each signature appears in SKILL.md's `## Error patterns` section; run the copy against a fixture whose signature names appear nowhere and show it passes. Then run the unmodified counter with --selftest and paste the output. Report whether the error-signature linkage can be skipped."),

    ("RevC1", "reviewer", ["calibration"],
     "Verify the append-only discipline for this round's filed surfaces: run `git -C %s diff --stat 793f79746712a79f915bb481215e54bbea8b5e7a main -- corpus/lessons/round-68.md corpus/SOURCES.md reports/round-68` and paste it (expect empty except for declared additions). Then check the round-69 counters do not write anything: grep them for write calls (open(..., \"w\"), shutil.copy, os.remove, subprocess with git/jj mutations) and report what you find." % LANE),

    ("RevC2", "reviewer", ["calibration"],
     "Cross-check consistency for the round-69 lesson the L1 is about to write: read reports/round-69/claims.json, reports/round-69/telemetry/declaration-dry-run.txt and corpus/lessons/round-68.md, and list every factual number the round-69 report and lesson will state (leg counts, registry row counts, corpus file counts, wave seat counts, dead seats). For each, give the exact command that re-derives it from committed bytes, and flag any number you cannot re-derive."),

    ("ScoutAdj", "scout", ["adjacency"],
     "Adjacency scan (read-only, no writes outside your report): does any sibling lane own a supersession/registry-correction-chain or SOURCES-registry-governance surface that kotodama's new decision table would duplicate? Search /home/vgpnk/Projects/shokunin/*-shokunin for files mentioning 'supersedes S', 'SOURCES.md', 'correction chain', 'settlement'. Report the nearest prior art with path and line, and state whether the kotodama table stays in-lane or bleeds."),

    ("ScoutFrontier", "scout", ["coverage", "depth"],
     "Frontier scan (read-only): read %s/corpus/README.md (its `## Frontier` and coverage map) and %s/corpus/SOURCES.md, and name the coverage-map ground the lane does NOT hold that the new registry-correction-chain decision table touches. State, in one line, whether the table moves coverage ground (it should not - it is a depth move) and where a reader would look for the missing coverage." % (LANE, LANE)),

    ("ScoutItem10", "scout", ["coverage", "calibration"],
     "Item-10 read-only re-derivation: reproduce the kotodama slice of the shokuknow absent-defect register with the addendum's own awk recipe (the register lives at /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md - READ ONLY, run nothing in that repo): count the data rows and list their S-ids. Compare with the round-68 verdicts in %s/corpus/lessons/round-68.md (`## Quarantine`). Report the row count, whether the round-68 verdict list covers every row, and state that adoption stays closed this round. Do not fetch anything." % LANE),

    ("Exec1", "executor", ["depth"],
     "Draft (do not land) the SKILL.md additions for claim D2 into your report file only: a `### Registry correction chains` decision table with exactly five rows (states: pending, settled-active, settled-retired, settled-closed, settled-split) and columns State | Row shape | Writer's next action | Error signature | Evidence, plus the matching five error-signature rows for SKILL.md's `## Error patterns` section. Derive every cell from tools/check-supersession-settlement.py (function classify) and the round-68 ledger rulings; cite the exact path:line for each Evidence cell. No filler, no invented sources, no production write."),

    ("Scribe1", "scribe", ["calibration", "depth"],
     "Draft (do not land) the round-69 lesson text into your report file only: a `## Gate` section with the S859 row (kind own-work, tier A, source = the repo path and the command that produced it, anchor = path:line plus revision, teaches, status mined, opened 2026-10-24, recheck 90d, used-by SKILL.md, corpus/lessons/round-69.md), a <=25-word located quote taken from the command's real output, and a `## Mistakes` section listing the mistake classes this round must record (frozen counter without a green control; fixture defect; dead mistake pointer; leg-count arithmetic; overreach verdict). No production write."),

    ("Scribe2", "scribe", ["calibration"],
     "Draft (do not land) the round-69 bookkeeping text into your report file only: a SCORECARD.md round-69 section (one row per axis: operability, calibration, depth, plus unchanged rows for coverage/freshness/adjacency) and a LOG.md round-69 entry, both written in the lane's existing style, with every number carrying its re-derivation command, plus the corrections table for the three r68 status-neutral defects (the missing R68-M9 row; the '9/10 legs PASS' arithmetic against the receipt's 8 PASS of 9 legs; the SCORECARD calibration verdict against the FAIL receipt). No production write."),
]

assert len(ITEMS) == 32, len(ITEMS)
ATTACK = {"reviewer", "critic", "mutation-tester", "sentinel", "revenger"}
assert sum(1 for _, role, _, _ in ITEMS if role in ATTACK) >= 8


def build():
    items = []
    for name, role, axes, body in ITEMS:
        prompt = (PRE + body + BOUNDS + "\nWrite your report to %s/%s.md "
                  "and end your answer with the single line "
                  "'Report: .ufo/waves/round-69/w1/%s.md'.\n"
                  % (REPORTS, name, name))
        items.append({"name": name, "role": role, "axes": axes,
                      "milestone": "r69-v1", "prompt": prompt})
    spec = {
        "wave": "kotodama-r69-v1",
        "milestone": "Round 69 single v1 wave (build+attack, 32 seats)",
        "reportDir": ".ufo/waves/round-69/w1",
        "axes": ["coverage", "operability", "calibration", "depth",
                 "freshness", "adjacency"],
        "context": CONTEXT,
        "items": items,
    }
    out = os.path.join(HERE, "spec-v1.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, indent=1, ensure_ascii=False)
    print("wrote %s items=%d attack=%d" % (
        out, len(items),
        sum(1 for i in items if i["role"] in ATTACK)))


if __name__ == "__main__":
    build()
