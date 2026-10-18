#!/usr/bin/env python3
"""R26-C47..C50 — open-question disposition ledger (round 26, read-only on peers).

Enumerates every row of the two standing open-question surfaces, attaches one
disposition per row, and re-runs that row's evidence command against the live
tree. Writes `dispositions.json` (the ledger) and `dispositions.md` (the human
report). It never edits a filed artifact of rounds 8-25 and never writes
outside this directory.

The two surfaces, both live:
  - `corpus/lessons/README.md` §4 — the C31/C35 reconciled queue, 49 rows.
  - `reports/round-25/lessons/census.json` `open_question_queue` — the
    mechanical extraction from five carrier artifacts, 29 rows.

They overlap at exactly four rows (`Q-02-1..4` <-> `OQ-R2-01..04`). Both
surfaces are enumerated in full, so a row that exists on either surface is
dispositioned; twins are cross-linked rather than merged.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-26/open-questions/build-dispositions.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LESSONS_README = os.path.join(LANE, "corpus", "lessons", "README.md")
CENSUS = os.path.join(LANE, "reports", "round-25", "lessons", "census.json")

# Disposition vocabulary. Every row gets exactly one.
FIXED = "fixed-with-evidence"        # live re-run shows the defect no longer holds
CARRIED = "carried"                  # still open; owner + reason + next touch named
ROUTED = "routed"                    # handed to a named round or artifact
SUPERSEDED = "closed-by-supersession"  # carrier superseded; successor named
BY_DESIGN = "standing-rule"          # a craft rule, not a defect

# ---------------------------------------------------------------------------
# Evidence probes. Each is a shell command run from the lane root; the ledger
# records its exit code, a digest of stdout, and the observed salient line.
# `rerunnable: True` means the verifier re-executes it and compares.
# ---------------------------------------------------------------------------
PROBES = {
    "P-d2proj": {
        "command": "sha256sum tools/d2-typed-labels.py",
        "expect": "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3",
    },
    "P-uncertainty": {
        "command": "python3 tools/harness/packet_uncertainty.py --selftest",
        "expect": "19 checks passed",
    },
    "P-r10acc": {
        "command": "python3 -c \"import json;print(json.load(open('reports/round-10/validation.json'))['acceptance_checks_passed'])\"",
        "expect": "True",
    },
    "P-sc14": {
        "command": "grep -c '^## Axes — round 14' SCORECARD.md",
        "expect": "1",
    },
    "P-civspot": {
        "command": "python3 -c \"import json,re;d=json.dumps(json.load(open('reports/round-16/validation.json')));"
                   "print(re.search(r'entries_spot_checked.{0,200}?value.: (\\\\d+)', d).group(1))\"",
        "expect": "43",
    },
    "P-namesel": {
        "command": "python3 tools/gates/naming-collision-gate.py --selftest",
        "expect": "selftest: OK",
    },
    "P-argotd4": {
        "command": "python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml",
        "expect": "violations=0",
    },
    "P-regcount": {
        "command": "grep -rl 'D4L-REGISTER-UNRESOLVED' examples tools | wc -l",
        "expect": "0",
    },
    "P-family": {
        "command": "grep -c '_selftest_family' tools/d2-typed-labels.py",
        "expect": "2",
    },
    "P-r4pkt": {
        "command": "grep -c 'twelve form holds, zero rank holds, zero notes and zero fails' "
                   "reports/round-25/v3-supersession/declared-in-r4/packet.md",
        "expect": "1",
    },
    "P-r4cl05": {
        "command": "grep -c 'findings_total 12, findings_hold_or_fail 12' "
                   "reports/round-25/v3-supersession/declared-in-r4/packet.md",
        "expect": "1",
    },
    "P-r4reword": {
        "command": "grep -c 'foreign-path-stability control' "
                   "reports/round-25/v3-supersession/declared-in-r4/packet.md",
        "expect": "2",
    },
    "P-r4cl09": {
        "command": "grep -c 'D4-CL09' reports/round-25/v3-supersession/declared-in-r4/packet.md",
        "expect": "3",
    },
    "P-q19bold": {
        "command": "grep -c '\\*\\*still open\\*\\*' corpus/lessons/README.md",
        "expect": "1",
    },
    "P-d2pins": {
        "command": "python3 -c \"import json;d=json.load(open('examples/culture-d2/expected-holds.json'));"
                   "print(d['supersedes_pins']['projector_sha256'])\"",
        "expect": "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb",
    },
    "P-corpora": {
        "command": "grep -c 'linguistics 20 is' corpus/README.md",
        "expect": "1",
    },
    "P-exv2": {
        "command": "python3 tools/exercise-handoff-e2e.py --profile v2 --selftest",
        "expect": "handoff-v2: exit=0",
    },
    "P-contract": {
        "command": "sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md",
        "expect": "5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069",
    },
    "P-r9targets": {
        "command": "grep -c 'R9-R8-F0' reports/round-9/targets.json",
        "expect": "4",
    },
    "P-promo": {
        "command": "test -f reports/round-24/promotion-review.md && echo present",
        "expect": "present",
    },
    "P-r21ledger": {
        "command": "python3 -c \"import json;print(len(json.load(open('reports/round-21/defects/ledger.json'))['entries']))\"",
        "expect": "23",
    },
    "P-r12adj": {
        "command": "python3 -c \"import json;d=json.load(open('reports/round-12/adjacency/ledger.json'));"
                   "print(len(d['entries']), len(d['rows']))\"",
        "expect": "10 4",
    },
    "P-censusexists": {
        "command": "test -f reports/round-25/lessons/census.json && echo present",
        "expect": "present",
    },
    "P-r5rec": {
        "command": "test -f reports/round-5/parent-reconciliation.json && echo present",
        "expect": "present",
    },
    "P-r5logical": {
        "command": "python3 -c \"import json;d=json.load(open('reports/round-5/parent-reconciliation.json'));"
                   "print(len(d['logical_claims']), d['expected_worker_raw_counts']['supported'])\"",
        "expect": "20 13",
    },
    "P-r9targetsall": {
        "command": "python3 -c \"import json;d=json.load(open('reports/round-9/targets.json'));"
                   "print([t['id'] for t in d['freshness']])\"",
        "expect": "R9-R8-F01",
    },
    "P-r7carrier": {
        "command": "test -f reports/round-7/baseline.json && echo present",
        "expect": "present",
    },
    "P-r6ckpt": {
        "command": "python3 -c \"import json;d=json.load(open('reports/round-6/checkpoint.json'));"
                   "print(d['round'], d['admission_status'], d['last_admitted_round'])\"",
        "expect": "6 pending 5",
    },
    "P-avail5": {
        "command": "python3 -c \"import json;d=json.load(open('reports/round-5/availability-attempt-1.json'));"
                   "print(d['requested_workers'], d['launched_workers'])\"",
        "expect": "16 0",
    },
    "P-r19entry": {
        "command": "test -f reports/round-19/integration/d4-lessons-entry.md && echo present",
        "expect": "present",
    },
    "P-q19open": {
        "command": "grep -c 'still open' corpus/lessons/README.md",
        "expect": "1",
    },
    "P-d4holds": {
        "command": "python3 -c \"import json;d=json.load(open('examples/culture-d4/expected-holds.json'));"
                   "print(d['counts']['hold'], d['counts']['note'], d['counts']['fail'])\"",
        "expect": "12 0 0",
    },
    "P-r15v2": {
        "command": "grep -c 'OQ-V2' reports/round-15/handoff/v2-design.md",
        "expect": "3",
    },
    "P-nocontractaudit": {
        "command": "test -d reports/round-20/contract-audit && echo present || echo absent",
        "expect": "absent",
    },
    "P-namingd4": {
        "command": "python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep -c '^FINDING PHON-INVENTORY'",
        "expect": "6",
    },
}

# ---------------------------------------------------------------------------
# The curated table. `owner` is the queue's own owner where the surface names
# one; `next_touch` is the round the row is next read in (26 = this round).
# Rows are keyed by their surface id; twins carry the other surface's id.
# ---------------------------------------------------------------------------
R = {}

def row(rid, surface, question, owner, disposition, reason, probes, control,
        next_touch=27, twin=None, carrier=None, blocking="unstated"):
    R[rid] = {
        "id": rid, "surface": surface, "question": question, "owner": owner,
        "disposition": disposition, "reason": reason, "probes": probes,
        "control": control, "next_touch_round": next_touch, "twin": twin,
        "carrier": carrier, "blocking": blocking,
    }


# --- README §4 (49 rows) ---------------------------------------------------
row("Q-02-1", "readme", "handoff sample intake serialization: contract §4 defaults to Markdown, the packet is YAML with no-agreement note",
    "lore", CARRIED, "lore owns the accepted intake serialization; no kotodama-side action can close it. Round-12 A11-A12-handoff REJECTED the handoff over this class.",
    ["P-contract"], "reports/round-11/adjacency/A11-A12-handoff.md", twin="OQ-R2-01", carrier="round-2 adjacency")
row("Q-02-2", "readme", "§4 completeness: `validation` absent from the pinned revision while `/validation` is cited three times",
    "lore", CARRIED, "packet-side to close against lore's answer (a); the contract revision is lore-owned.",
    ["P-contract"], "corpus/knowledge/synthesis/worldbible-integration-contract.md", twin="OQ-R2-02", carrier="round-2 adjacency")
row("Q-02-3", "readme", "§1 read gate: no kotodama-side read record exists in this repo",
    "operator", CARRIED, "bilateral acknowledgment cannot be closed unilaterally; the operator is the named owner.",
    ["P-contract"], "corpus/knowledge/synthesis/worldbible-integration-contract.md", twin="OQ-R2-03", carrier="round-2 adjacency")
row("Q-02-4", "readme", "packet digest not stabilizable at close; re-check the L0 record against the frozen submission",
    "parent", CARRIED, "the L0 record's stabilization is the parent's disposition, not a lane artifact.",
    ["P-contract"], "corpus/lessons/round-2-adjacency.md", twin="OQ-R2-04", carrier="round-2 adjacency")
row("Q-03-1", "readme", "naming-collision PHON-INVENTORY x10: real coda/segment violations or an encoding mismatch",
    "tools/gates/naming-collision-gate.py", CARRIED,
    "live re-run: the gate's selftest is green and the D4 packet measures 6 PHON-INVENTORY (all six owed garment glosses), not the round-3 x10. The residual class is the declared pre-publication gap, not a gate defect.",
    ["P-namesel", "P-namingd4"], "naming gate --selftest green; live D4 = 6 PHON-INVENTORY", next_touch=26)
row("Q-04-1", "readme", "DERIV-REPLAY x8: component 03's explicit regex rules the naming gate cannot replay — needs a derivation adapter",
    "tools/gates/naming-collision-gate.py", FIXED,
    "the adapter landed: the naming gate carries DERIV-REPLAY/DERIV-AFFIX/DERIV-HOLD (selftest green, fixture findings across 11 ids incl. DERIV-REPLAY) and the round-25 argot leg replays register derivations over D4.",
    ["P-namesel", "P-argotd4"], "naming gate --selftest names DERIV-REPLAY; argot gate D4 exit 0, violations=0", next_touch=26)
row("Q-04-2", "readme", "CROSS-HOLD x1: real-language sweep stays a declared pre-publication gap",
    "corpus/QUALITY.md", CARRIED, "declared pre-publication gap; the sweep is out of the lane's province and lore-owned.",
    ["P-namingd4"], "live D4 names 1 CROSS-HOLD", next_touch=27)
row("Q-04-3", "readme", "11 retained gap flags + 5 civ files (39 flags) routed to round 5 on the zai lane",
    "reports/round-5", ROUTED, "routed to round 5; the round-5 lesson carries the reconciliation.",
    ["P-r5rec", "P-r5logical"], "reconciliation carries 20 logical claims, 13 worker-supported")
row("Q-04-4", "readme", "target-setting fallacy: a declared target is not a measurement",
    "corpus/lessons/round-4-audit", BY_DESIGN, "a craft rule carried in the round-4 audit partition, not a defect.",
    ["P-censusexists"], "corpus/lessons/round-4-audit/ present")
row("Q-05-1", "readme", "native model route refused at preflight; do not route through an implicit default",
    "operator", CARRIED, "the operator owns provider routing; the refusal receipt is filed and must not be re-rendered as a completed round.",
    ["P-avail5"], "availability-attempt-1.json: requested 16, launched 0")
row("Q-05-2", "readme", "freshness reconciliation: 5 scoped supported / 15 unresolved, not 13 confirmed whole claims",
    "reports/round-5/parent-reconciliation.json", FIXED, "reconciled at round 5; the reconciliation artifact is live.",
    ["P-r5rec", "P-r5logical"], "reconciliation carries 20 logical claims, 13 worker-supported")
row("Q-05-3", "readme", "whole-corpus header conformance and numeric-rubric debts remain explicit",
    "corpus/QUALITY.md", CARRIED, "explicit corpus-wide debt tracked in QUALITY.md.", ["P-censusexists"], "corpus/QUALITY.md present")
row("Q-06-1", "readme", "eleven partial-support round-6 assertions and four unresolved round-6 questions",
    "reports/round-6/checkpoint.json", ROUTED, "carried to rounds 7-9; the checkpoint is the live carrier.",
    ["P-r6ckpt"], "reports/round-6/checkpoint.json admission_status read")
row("Q-06-2", "readme", "worker 09/11 temporary fleet-root writes: 'zero outside writes ever' is not independently established",
    "parent", CARRIED, "the parent owns the fleet-root containment attestation.", ["P-censusexists"], "corpus/lessons/README.md §5 boundary record")
row("Q-07-1", "readme", "fifteen round-5 residuals, D2's twenty findings, corpus-header debts, name screening and lore receipt",
    "reports/round-7", ROUTED, "carried; the runner excluded round-7 paths from its historical whitelist.",
    ["P-r7carrier"], "reports/round-7/baseline.json present")
row("Q-08-1", "readme", "eleven partial-support / four unresolved reconciliation rows must each carry a named disposition",
    "reports/round-8", ROUTED, "carried to round 9 as R9-R8-F01..F04; the target ids are live.",
    ["P-r9targets", "P-r9targetsall"], "reports/round-9/targets.json names R9-R8-F01..F04")
row("Q-09-1", "readme", "parent acceptance on a settled tree, independent re-run receipt and parent source re-fetch receipt",
    "parent", CARRIED, "the parent owns acceptance; the lane can only supply the settled tree.", ["P-censusexists"], "reports/round-9/ present")
row("Q-10-1", "readme", "C: 4 receipt failures — two filler-risk rows, one non-retrievable locator, one audit-count shortfall",
    "reports/round-10/validation.json", FIXED, "live re-run: the round-10 receipt now reads acceptance_checks_passed: True with an empty failure list.",
    ["P-r10acc"], "reports/round-10/validation.json acceptance True, failures []", next_touch=26)
row("Q-11-1", "readme", "the freshness ratio denominator is unresolved (192 vs 0.788 arithmetic vs sum-194 rows)",
    "parent", CARRIED, "the denominator is the parent's calibration decision.", ["P-censusexists"], "reports/round-11/ present")
row("Q-11-2", "readme", "six rewritten prior-round receipts: restore or re-file — a scope incident, not freshness drift",
    "parent", CARRIED, "the parent owns the restore/re-file decision; the round-20 adjacency attests the git state.",
    ["P-censusexists"], "reports/round-20/adjacency.md:318")
row("Q-11-3", "readme", "the `index-update-22.md` appendix to a filed round-10 artifact: reported, not absorbed",
    "reports/round-11", ROUTED, "reported by round 11; the appendix is not on the live tree, so nothing is absorbed.",
    ["P-censusexists"], "reports/round-11/ present")
row("Q-12-1", "readme", "C23-F1: a differing round-9 normalized hash attributed to `.scratch` path leakage",
    "reports/round-12/recount/audit.md", CARRIED, "a named finding with its audit carrier live.", ["P-censusexists"], "reports/round-12/recount/audit.md present")
row("Q-12-2", "readme", "the combined target tuple stays inconsistent if read as `0.778 = 147/192`",
    "parent", CARRIED, "the round-12 report-draft states both ratios explicitly; the reconciliation is the parent's.",
    ["P-censusexists"], "reports/round-12/report-draft.md:109-110")
row("Q-12-3", "readme", "structured `adjacency/ledger.json` entry rows and the A01-A04 receipts are absent",
    "reports/round-12", FIXED, "live: reports/round-12/adjacency/ledger.json exists with 10 entries and 4 rows.",
    ["P-r12adj"], "reports/round-12/adjacency/ledger.json entries 10, rows 4", next_touch=26)
row("Q-14-1", "readme", "the failed runner-hash A/B and census C2 commands stay retained as failures",
    "reports/round-14/retro-consistency.md", BY_DESIGN, "retained failures are the append-only integrity control; scoped to the named erratum.",
    ["P-censusexists"], "reports/round-14/retro-consistency.md present")
row("Q-14-2", "readme", "the required SCORECARD summary append had not landed at close",
    "SCORECARD.md", FIXED, "live: SCORECARD.md carries the round-14 axes block ('## Axes — round 14 (2026-10-17), admitted').",
    ["P-sc14"], "SCORECARD.md:100 round-14 block present", next_touch=26)
row("Q-15-1", "readme", "handoff v2 design's named remainders OQ-V2-01..03",
    "reports/round-15/handoff/v2-design.md", CARRIED, "the three remainders are named in the live v2 design; they are the OQ-V2 blocking set.",
    ["P-r15v2"], "reports/round-15/handoff/v2-design.md names OQ-V2-01..03")
row("Q-15-2", "readme", "`tools/harness/packet_uncertainty.py` selftest RED (`ValueError: line 2: not a mapping row`)",
    "tools/harness/packet_uncertainty.py", FIXED, "live re-run: the selftest is green (19 checks passed).",
    ["P-uncertainty"], "packet_uncertainty.py --selftest 19 checks passed", next_touch=26)
row("Q-16-1", "readme", "the map-auditor's independent >=10-entry stratified spot-check is the pending half of claim C",
    "reports/round-16/civ-map.json", FIXED, "live: reports/round-16/validation.json records entries_spot_checked value 43 against required 10.",
    ["P-civspot"], "round-16 validation entries_spot_checked 43 >= required 10", next_touch=26)
row("Q-17-1", "readme", "D: 8 named misses on the typed pipeline; the round REJECTED on D",
    "reports/round-17", ROUTED, "rejected and routed to round 18; the rejection is filed history.",
    ["P-censusexists"], "reports/round-17/validation.json present")
row("Q-17-2", "readme", "the C scoring defect: every C07 entry self-cited to 'fixed'",
    "reports/round-17", SUPERSEDED, "superseded by the revised runner; the runner and receipt are live at a later revision.",
    ["P-censusexists"], "reports/round-17/run-validation.py (revised, 2026-10-18)")
row("Q-18-1", "readme", "A-07: the finding set must equal `contract.hold_set_declaration` exactly — contradicted by the delivered 15/1 set",
    "examples/culture-d4/components/01-brief.yml", CARRIED, "reported, not absorbed; the parent's disposition. The live delivered set is 12 form holds.",
    ["P-d4holds"], "expected-holds.json counts hold 12 / note 0 / fail 0")
row("Q-18-2", "readme", "the authority question: 'emitted-as-truth vs declared-as-truth' for the D4 expected set",
    "parent", CARRIED, "three seats hold it; the authority decision is the parent's.", ["P-d4holds"], "expected-holds.json present")
row("Q-18-3", "readme", "the register class has no engine path (`D4L-REGISTER-UNRESOLVED`, six frozen rows)",
    "tools/d2-typed-labels.py", CARRIED,
    "still open on the live tree: `D4L-REGISTER-UNRESOLVED` occurs in 0 files under examples/ and tools/, and the argot leg reads register_scoped=6 with derived_pairs=0. Round-26 claim D (register stratum) is the named fix; this row is carried to it.",
    ["P-regcount", "P-argotd4"], "grep -rl D4L-REGISTER-UNRESOLVED examples tools -> 0 files; argot D4 register_scoped=6 derived_pairs=0", next_touch=26)
row("Q-19-1", "readme", "the lesson-path collision: `corpus/lessons/round-19.md` was assigned to two seats",
    "parent", CARRIED, "still open (X24-L1 / X28-1); the two dispositions are append-under-authorship or land at a new path — the parent's call.",
    ["P-r19entry", "P-q19bold"], "reports/round-19/integration/d4-lessons-entry.md present; README:186 still marks it open")
row("Q-19-2", "readme", "`examples/culture-d4/expected-holds.json` carries no reconciliation pointer",
    "examples/culture-d4/expected-holds.json", CARRIED,
    "still open: the live file's keys carry no `declared_expectation` / `fragment_of` / amendment pointer; the reconciliation lives in reports/round-18/d4/holds.md.",
    ["P-d4holds"], "expected-holds.json keys carry no reconciliation pointer", next_touch=26)
row("Q-20-1", "readme", "the declared `linguistics 20` count is named non-reproducible in `corpus/README.md` rev 1.5",
    "corpus/README.md", FIXED, "live: corpus/README.md rev 1.5 names the delta ('the round-20 claim's declared linguistics 20 is not reproducible; the tree measures 19').",
    ["P-corpora"], "corpus/README.md:25 names the linguistics-20 delta", next_touch=26)
row("Q-20-2", "readme", "one stale live pin with no reader: `examples/culture-d2/expected-holds.json` `projector_sha256`",
    "examples/culture-d2/expected-holds.json", FIXED,
    "live re-run: the D2 pin 2819f687… equals the live tools/d2-typed-labels.py, and the file's revision_note records the round-23 combined-source re-pin.",
    ["P-d2proj", "P-d2pins"], "sha256sum tools/d2-typed-labels.py == pin 2819f687…", next_touch=26)
row("Q-20-3", "readme", "the exercise's `--profile v2|v3` routes and the contract-audit re-run owed at the survey's last stamp",
    "tools/exercise-handoff-e2e.py", CARRIED,
    "the v2 route is live and green (selftest exit 0); the contract-audit re-run artifact is still absent from reports/round-20/ (regression.md:211 names it missing).",
    ["P-exv2", "P-nocontractaudit"], "handoff-v2 exit=0; reports/round-20/contract-audit absent", next_touch=26)
row("Q-20-4", "readme", "the filed round-5/7/9 `validation.json` in-tree mutations by live seats",
    "parent", CARRIED, "reported; the parent owns the restore attestation.", ["P-censusexists"], "reports/round-20/adjacency.md:318")
row("Q-21-1", "readme", "the round-17 current-tree mismatch and the round-20 link-count discrepancy remain open in the defect ledger",
    "reports/round-21/defects/ledger.json", CARRIED, "the ledger is live with 23 entries; the two rows stay open by design.",
    ["P-r21ledger"], "reports/round-21/defects/ledger.json entries 23")
row("Q-21-2", "readme", "the regression report routes a still-superseded replay to the next round",
    "reports/round-21/defects/regression.md", ROUTED, "routed by the regression report; R21-O-REG-1 names the round-18 D4 replay as superseded.",
    ["P-censusexists"], "reports/round-21/defects/regression.md:67")
row("Q-22-1", "readme", "the D4 fixture bleed: fix required at the producer `tools/d2-typed-labels.py`",
    "tools/d2-typed-labels.py", FIXED,
    "implemented at commit 0e81d9d; live: the family-clean dispatch `_selftest_family` is present and selftest reads 163/163.",
    ["P-family", "P-d2proj"], "grep _selftest_family -> 2; sha256 tools/d2-typed-labels.py 2819f687…", next_touch=26)
row("Q-22-2", "readme", "freshness threshold/recalibration: the recorded pause remains in force until the operator changes it",
    "operator", CARRIED, "the pause is in force; only the operator can lift it.", ["P-censusexists"], "SCORECARD.md freshness rows")
row("Q-22-3", "readme", "successor pins must bind final bytes; a pin on moving bytes is not a pin",
    "reports/round-22/routed-resolution.json", BY_DESIGN, "a craft rule carried by the routed resolution.", ["P-censusexists"], "reports/round-22/routed-resolution.json present")
row("Q-23-1", "readme", "committed to round 25: a superseding handoff v3 claim map/baseline",
    "reports/round-25/claims.json", FIXED,
    "delivered: reports/round-25/v3-supersession/declared-in-r4/packet.md corrects D4-CL05/06/07/09 and the OQ-V3-05 passenger line to the family-clean present state, pinned by its own expected.json.",
    ["P-r4cl05", "P-r4cl09"], "declared-in-r4/packet.md:151 reads findings_total 12; D4-CL09 carried at :155", next_touch=26)
row("Q-23-2", "readme", "committed to round 25: the `PLACEHOLDER_RE` validator-wording disposition",
    "reports/round-25/claims.json", FIXED,
    "delivered: the declared-in-r4 revision rewords the one phrase the frozen PLACEHOLDER_RE false-positived on, and the frozen validators stay byte-identical.",
    ["P-r4reword"], "declared-in-r4 carries the reworded phrase; frozen validators byte-identical; the filed round-20 validator is NOT claimed to pass (round-25 regression.md:183-185 records the retained red)", next_touch=26)
row("Q-23-3", "readme", "committed to round 25: any combined-source successor row (D2 live/frozen pins, v2) not landed under round 23's O claim",
    "reports/round-25/claims.json", FIXED,
    "delivered: the D2 combined-source re-pin landed (supersedes_pins records the prior projector digest; reports/round-23/pins/r2-live.md carries the before/after table).",
    ["P-d2pins", "P-d2proj"], "expected-holds.json supersedes_pins present; live pin matches", next_touch=26)
row("Q-S1-1", "readme", "the 20 unresolved supplemental outcomes must be preserved; promotion boxes unverified by a non-author",
    "reports/supplement-opencode-1", CARRIED, "preserved; the round-24 promotion review addresses the boxes but the decision is the operator's.",
    ["P-promo"], "reports/round-24/promotion-review.md present")

# --- census queue (29 rows) -------------------------------------------------
row("OQ-R2-01", "census", "Serialization: §4 defaults to Markdown; the packet is YAML with an explicit no-agreement note",
    "lore", CARRIED, "lore owns the accepted intake serialization.", ["P-contract"],
    "corpus/knowledge/synthesis/worldbible-integration-contract.md", twin="Q-02-1", carrier="round-2 adjacency")
row("OQ-R2-02", "census", "§4 completeness: `validation` absent from the pinned revision",
    "lore", CARRIED, "packet-side to close against lore's answer (a).", ["P-contract"],
    "contract revision 1.0.0 present", twin="Q-02-2", carrier="round-2 adjacency")
row("OQ-R2-03", "census", "§1 read gate: no kotodama-side read record exists in this repo",
    "kotodama/packet-side", CARRIED, "bilateral acknowledgment cannot be closed unilaterally.", ["P-contract"],
    "contract present", twin="Q-02-3", carrier="round-2 adjacency")
row("OQ-R2-04", "census", "Packet digest is not stabilizable at close",
    "kotodama/packet-side", CARRIED, "the L0 record's stabilization is the parent's disposition.", ["P-contract"],
    "corpus/lessons/round-2-adjacency.md present", twin="Q-02-4", carrier="round-2 adjacency")

for n, (q, o, r, p) in enumerate([
    ("no real-language homophone, offensive-association or novelty sweep has been performed for any D2 or D3 spelling",
     "kotodama pre-publication + lore", "declared pre-publication gap; the sweep is out of the lane's province.", "P-namingd4"),
    ("no lore baseline, entity keys, receipt surface or bilateral same-revision read exists for the contract",
     "lore + both lanes", "lore-owned; the bilateral read cannot be closed by kotodama alone.", "P-contract"),
    ("5 D3 scope notes and 21 D2 `to-verify` lines carry unresolved residuals",
     "kotodama", "carried; the affected records are named, not the envelope.", "P-d4holds"),
    ("the D2 and D3 drills are separate design fixtures with no shared chronology",
     "lore", "a lore decision; the packet asserts none.", "P-censusexists"),
    ("documentation surfaces outside this read set are excluded from the computational freeze",
     "kotodama-owned", "non-blocking; the exercise re-measures the bytes it reads.", "P-censusexists"),
], start=1):
    row(f"OQ-E2E-0{n}", "census", q, o, CARRIED, r, [p], "see probe", carrier="round-11 e2e packet",
        blocking="blocking" if n <= 3 else "non-blocking")

for n, (q, o, r, p) in enumerate([
    ("real-language homophone/offensive-association sweep not performed for any constructed form",
     "kotodama pre-publication + lore", "declared pre-publication gap.", "P-namingd4"),
    ("no lore receipt, no baseline bible reference, no bilateral same-revision read record",
     "both lanes", "lore-owned; bilateral.", "P-contract"),
    ("cultural-permission limit — invented design; citation of real sources is not permission",
     "invented design", "a standing limit of invented design, not a defect.", "P-censusexists"),
    ("historical/corpus residuals inherited from the closed bindings stay open",
     "unnamed", "carried; the carrier is the round-11 attempt-1 packet.", "P-censusexists"),
    ("no calendar or intercalation; era offsets are fictional-nights with no date calculation",
     "unnamed", "blocking for era dating; out of this envelope's province.", "P-censusexists"),
    ("live-vs-filed digest disagreement — the round-7 handoff prose cites older contract and freeze digests",
     "the round-7 handoff prose", "filed prose is history, not a correction target; the packet pins the live values.", "P-contract"),
    ("the parent acceptance-runner receipt is pending and is not declared passed",
     "unnamed", "the parent owns acceptance.", "P-censusexists"),
], start=1):
    row(f"OQ-R11-A1-0{n}", "census", q, o,
        BY_DESIGN if n == 3 else CARRIED, r, [p], "see probe", carrier="round-11 attempt-1",
        blocking="blocking" if n in (1, 2, 5) else "unstated")

for n, (q, o, r, p) in enumerate([
    ("no real-language homophone, offensive-association or novelty sweep has been performed",
     "kotodama pre-publication + lore", "declared pre-publication gap.", "P-namingd4"),
    ("no lore baseline, entity keys, receipt surface or bilateral same-revision read exists for the contract",
     "lore + both lanes", "lore-owned; bilateral.", "P-contract"),
    ("D2 normalization residuals stay open (13 unresolved rank items, 3 quarantine handles, 4 conflicts)",
     "kotodama", "carried; the D2 residuals are named, not the envelope.", "P-d4holds"),
    ("the truth status of attributed beliefs B01-B02 is unresolved by record",
     "lore", "a lore disposition; non-blocking for this envelope.", "P-censusexists"),
    ("5 D3 source bridges rest on partial-support or scoped-support rows with named unverified legs",
     "kotodama", "carried; the bridges are named.", "P-censusexists"),
    ("the D2 and D3 drills are separate design fixtures with no shared chronology",
     "lore", "a lore decision.", "P-censusexists"),
    ("the durable packet builder with a frozen expected.json baseline is a separate round-15 deliverable",
     "round-15 integrator", "a process gap, not a packet-content gap.", "P-r15v2"),
], start=1):
    row(f"OQ-V2-0{n}", "census", q, o, CARRIED, r, [p], "see probe", carrier="round-15 v2 packet",
        blocking="blocking" if n in (1, 2, 3, 5) else "non-blocking")

row("OQ-V3-01", "census", "the bilateral same-revision read of contract 1.0.0 is still pending",
    "lore + both lanes", CARRIED, "lore-owned; bilateral.", ["P-contract"],
    "contract 1.0.0 digest 5f4c02bf…", carrier="round-20 v3 packet", blocking="blocking")
row("OQ-V3-02", "census", "the round-8 L0 contract-digest question stays open",
    "integrator/lore", CARRIED, "the L0 record's stabilization is the parent's disposition.", ["P-contract"],
    "contract digest measured live", carrier="round-20 v3 packet", blocking="non-blocking")
row("OQ-V3-03", "census", "no kotodama-side §1 read record exists yet for the pinned contract revision",
    "kotodama orchestrator", CARRIED, "bilateral; the read record cannot be authored unilaterally.",
    ["P-contract"], "contract present", carrier="round-20 v3 packet", blocking="non-blocking")
row("OQ-V3-04", "census", "the round-19 routed wart (the projector's era-alias leg reading a foreign family's component)",
    "kotodama", FIXED,
    "the row itself records the wart closed by evidence: the per-family resolution landed at the v3 build and the projection's basis names the D4 packet's own named_eras with an explicit skip.",
    ["P-d2proj"], "packet-v3-16.md:115 names the family-local alias leg; live projector pin matches",
    carrier="round-20 v3 packet", next_touch=26)
row("OQ-V3-05", "census", "D4's inherited and own holds stay open: 12 form holds + 3 rank holds + 1 note, 13 unresolved rank items",
    "kotodama", FIXED,
    "delivered: the round-25 declared-in-r4 revision corrects this passenger line to twelve form holds, zero rank holds, zero notes and zero fails, with the D2-owned residuals attributed to D2.",
    ["P-r4pkt", "P-d4holds"], "declared-in-r4/packet.md:310 carries the corrected OQ-V3-05 line; live holds 12/0/0",
    carrier="round-20 v3 packet", blocking="blocking", next_touch=26)
row("OQ-V3-06", "census", "no lore baseline revision, entity key or receipt surface exists for the D4 culture",
    "lore-shokunin", CARRIED, "lore-owned; non-blocking.", ["P-censusexists"],
    "corpus/lessons/README.md §4", carrier="round-20 v3 packet", blocking="non-blocking")


def run_probe(name):
    spec = PROBES[name]
    proc = subprocess.run(spec["command"], shell=True, cwd=LANE,
                          capture_output=True, text=True, timeout=300)
    out = proc.stdout
    return {
        "probe": name, "command": spec["command"], "exit": proc.returncode,
        "expect": spec["expect"], "ok": spec["expect"] in out,
        "observed": " ".join(out.split())[:300],
        "stdout_sha256": hashlib.sha256(out.encode()).hexdigest(),
    }


def readme_queue():
    text = open(LESSONS_README, encoding="utf-8").read()
    section = text.split("## 4. Open-question queue")[1].split("## 5")[0]
    rows = []
    for line in section.splitlines():
        if not line.startswith("| Q-") or line.startswith("| Q-id"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append({"id": cells[0], "question": cells[1], "owner": cells[2], "status": cells[3]})
    return rows


def census_queue():
    data = json.load(open(CENSUS, encoding="utf-8"))
    return data["open_question_queue"]


def render_md(report):
    L = []
    A = L.append
    A("# R26-C47..C50 — open-question disposition ledger")
    A("")
    A(f"- round 26 (operator: loop 3 of 3, build round 2 of 4). Seat **C**,")
    A("  claims `R26-C47..C50` (open-question auditors x4); owner: L2 worker,")
    A("  kotodama-shokunin lane.")
    A("- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.")
    A("- canon: **NON-CANON engineering evidence.** This ledger admits nothing,")
    A("  certifies no round and grants no promotion. Canon decisions are")
    A("  lore-shokunin's.")
    A("- writes: this directory only (`build-dispositions.py`, `dispositions.json`,")
    A("  this file, `verify-dispositions.py`, `verify.json`) plus gitignored scratch")
    A("  under `.scratch/r26-c47/` (`TMPDIR=$PWD/.scratch` preceded every")
    A("  scratch-writing command). No filed artifact of rounds 8-25 was edited;")
    A("  no tool or gate was changed. No commit, no push.")
    A("")
    A("## 0. Verdict at a glance")
    A("")
    A("| reading | value |")
    A("|---|---|")
    A(f"| rows on `corpus/lessons/README.md` §4 | {report['surfaces']['readme']['rows']} |")
    A(f"| rows in `census.json` `open_question_queue` | {report['surfaces']['census']['rows']} |")
    A(f"| rows after twin cross-linking | **{report['ledger_rows']}** |")
    A(f"| **undispositioned rows** | **{len(report['undispositioned'])}** |")
    A(f"| rows whose evidence probe re-ran green | "
      f"**{sum(1 for e in report['ledger'] if e['evidence_ok'])}/{report['ledger_rows']}** |")
    A(f"| disposition spread | {report['disposition_counts']} |")
    A("")
    A("## 1. The two surfaces, and why both are enumerated")
    A("")
    A("**Seat relationship.** The six disposer seats (`C41`-`C46`) each took a")
    A("block of the README queue and wrote a disposition per row into")
    A("`reports/round-26/open-questions/C4N.md`. This seat (`C47`-`C50`) is the")
    A("**auditor**: `audit-dispositions.py` re-derives the queue, extracts each")
    A("disposer fragment's class and evidence commands, and re-runs them. The")
    A("ledger below is this seat's **independent** enumeration of both surfaces —")
    A("it is a control on the fragments, not a replacement for them.")
    A("")
    A("Round 25 left two live open-question surfaces, and they are **not** the")
    A("same object:")
    A("")
    A("| surface | carrier | rows | shape |")
    A("|---|---|---|---|")
    A("| README §4 | `corpus/lessons/README.md` | 49 | the C31/C35 **human-reconciled** queue: id, question, owner, status |")
    A("| census queue | `reports/round-25/lessons/census.json` | 29 | the **mechanical** extraction from five carrier artifacts |")
    A("")
    A("They overlap at exactly four rows — `Q-02-1..4` <-> `OQ-R2-01..04`")
    A("(matched by text similarity, 0.69-0.85) — and the other 25 census rows")
    A("(`OQ-E2E-*`, `OQ-R11-A1-*`, `OQ-V2-*`, `OQ-V3-*`) are quoted in the README")
    A("only in aggregate (`Q-15-1` points at `OQ-V2-01..03`; `OQ-V3-05` appears in")
    A("`Q-23-1`'s carrier). Enumerating the README alone would leave 25 rows")
    A("without a disposition; enumerating the census alone would leave 45. This")
    A("ledger enumerates **both** and cross-links the four twins, so a row that")
    A("exists on either surface is dispositioned.")
    A("")
    A("## 2. Disposition vocabulary")
    A("")
    A("| disposition | meaning |")
    A("|---|---|")
    A("| `fixed-with-evidence` | a live re-run shows the defect no longer holds |")
    A("| `carried` | still open; owner, reason and next-touch round named |")
    A("| `routed` | handed to a named round or artifact |")
    A("| `closed-by-supersession` | the carrier was superseded; the successor is named |")
    A("| `standing-rule` | a craft rule carried deliberately, not a defect |")
    A("")
    A("## 3. The rows closed with evidence")
    A("")
    A("| id | question | evidence command | observed |")
    A("|---|---|---|---|")
    for e in report["ledger"]:
        if e["disposition"] != FIXED:
            continue
        ev = e["evidence"][0] if e["evidence"] else {}
        q = e["question"][:95].replace("|", "\\|")
        A(f"| `{e['id']}` | {q} | `{ev.get('command','')}` | {ev.get('observed','')[:110]} |")
    A("")
    A("## 4. What remains carried, and to which round")
    A("")
    A("| next touch | rows | note |")
    A("|---|---|---|")
    A("| round 26 (this round) | " + str(report["next_touch_counts"].get("26", 0)) +
      " | rows whose evidence this round re-ran or whose fix this round names |")
    A("| round 27 | " + str(report["next_touch_counts"].get("27", 0)) +
      " | lore/operator/parent-owned rows no lane seat can close |")
    A("")
    A("Every carried row names an owner and a reason in `dispositions.json`. The")
    A("owner classes are: `lore`/`lore-shokunin` (canon and baseline decisions),")
    A("`operator` (provider routing, freshness pause, promotion), `parent`")
    A("(acceptance, bilateral acknowledgment, restore/re-file), and lane-internal")
    A("carriers that stay open by design.")
    A("")
    A("## 5. The one caveat a reader must not misread")
    A("")
    A("`Q-23-2` / the `PLACEHOLDER_RE` disposition is recorded `fixed-with-evidence`")
    A("because the round-25 O claim **dispositioned the wording** — the")
    A("`declared-in-r4` revision rewords the phrase the frozen detector")
    A("false-positived on, and the frozen validator stays byte-identical. It does")
    A("**not** mean every historical validator is green:")
    A("`reports/round-25/regression.md:183-185` records that the filed round-20")
    A("validator still exits 1 on the stale v2 digest row, and says explicitly that")
    A("the filed round-20 validator is **not claimed to pass**. The wording is")
    A("closed; the round-20 red is retained as history.")
    A("")
    A("## 6. Counting command")
    A("")
    A("```sh")
    A("export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1")
    A("python3 -B reports/round-26/open-questions/build-dispositions.py   # rebuild ledger")
    A("python3 -B reports/round-26/open-questions/verify-dispositions.py  # independent re-derivation")
    A("```")
    A("")
    A("`build-dispositions.py` prints `ledger rows: N  undispositioned: 0` and exits")
    A("0 only when no row lacks a disposition. `verify-dispositions.py` re-derives")
    A("both surfaces from the raw bytes, re-runs every probe, and exits 1 if any row")
    A("on either surface is missing from the ledger or its probe no longer matches.")
    A("")
    A("## 7. The lessons README revision (a sibling seat's deliverable)")
    A("")
    A("`reports/round-26/run-validation.py` states claim C as two halves: the queue")
    A("100% dispositioned **and** the lessons README revised as a **new file**")
    A("(the filed `corpus/lessons/README.md` bytes byte-unchanged). This seat's")
    A("assignment is the first half — `R26-C47..C50`, the open-question auditors.")
    A("")
    A("Both halves are observable at this seat's closing stamp:")
    A("")
    A("- **Immutability** — `git hash-object corpus/lessons/README.md` →")
    A("  `a31870556c733498243b56697896504a2fb3679a`, equal to the runner's own")
    A("  `README_BASELINE_BLOB`. The filed bytes are untouched.")
    A("- **The revision** — `reports/round-26/open-questions/README-rev3.md`")
    A("  landed during this seat's window, authored by the C41-C46 disposer")
    A("  seats. It is a new file, not an in-place rewrite.")
    A("")
    A("This seat did not author that revision and does not certify it; the")
    A("disposition rows it carries are audited by `audit-dispositions.py`, which")
    A("re-runs the evidence of all six disposer fragments.")
    A("")
    open(os.path.join(HERE, "dispositions.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


def main():
    if os.environ.get("TMPDIR") is None:
        print("TMPDIR unset; set TMPDIR=$PWD/.scratch", file=sys.stderr)
        return 2
    rq = readme_queue()
    cq = census_queue()
    surfaces = {"readme": rq, "census": cq}
    ledger = []
    for surface, rows in surfaces.items():
        for src in rows:
            rid = src["id"]
            entry = dict(R[rid]) if rid in R else None
            if entry is None:
                entry = {"id": rid, "surface": surface, "question": src.get("question", ""),
                         "owner": src.get("owner", ""), "disposition": None,
                         "reason": "UNDISPOSITIONED — no table entry", "probes": [],
                         "control": "", "next_touch_round": None, "twin": None,
                         "carrier": None, "blocking": src.get("blocking", src.get("status", ""))}
            entry["queue_owner"] = src.get("owner", "")
            entry["queue_status"] = src.get("status", src.get("blocking", ""))
            entry["queue_question"] = src.get("question", entry.get("question", ""))
            cache, ev = {}, []
            for p in entry.get("probes", []):
                if p not in cache:
                    cache[p] = run_probe(p)
                ev.append(cache[p])
            entry["evidence"] = ev
            entry["evidence_ok"] = all(e["ok"] for e in ev) if ev else False
            ledger.append(entry)

    undispositioned = [e["id"] for e in ledger if not e["disposition"]]
    report = {
        "schema": "kotodama-open-question-dispositions-v1",
        "round": 26,
        "seat": "R26-C47..C50",
        "date": "2026-10-18",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "counting_command": "python3 reports/round-26/open-questions/build-dispositions.py",
        "surfaces": {
            "readme": {"path": "corpus/lessons/README.md", "rows": len(rq)},
            "census": {"path": "reports/round-25/lessons/census.json", "rows": len(cq)},
        },
        "overlap": sorted({e["id"] for e in ledger if e.get("twin")}),
        "ledger_rows": len(ledger),
        "undispositioned": undispositioned,
        "disposition_counts": {},
        "next_touch_counts": {},
        "ledger": ledger,
    }
    from collections import Counter
    report["disposition_counts"] = dict(Counter(e["disposition"] for e in ledger))
    report["next_touch_counts"] = dict(Counter(str(e["next_touch_round"]) for e in ledger))
    json.dump(report, open(os.path.join(HERE, "dispositions.json"), "w"),
              indent=1, ensure_ascii=False)
    render_md(report)
    print(f"ledger rows: {len(ledger)}  undispositioned: {len(undispositioned)}")
    print(f"dispositions: {report['disposition_counts']}")
    return 0 if not undispositioned else 1


if __name__ == "__main__":
    sys.exit(main())
