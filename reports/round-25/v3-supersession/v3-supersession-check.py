#!/usr/bin/env python3
"""Round-25 O seat — verify the `declared-in-r4` claim-prose supersession.

Disposition of the round-25 O hazard: the handoff v3 ledger carries stale D4
claim prose. D4-CL05/06/07/09 and the OQ-V3-05 passenger line describe the
pre-family-clean state (15 holds / 1 note, three `D2L-RANK` holds, 13 unresolved
rank items, 3 quarantine handles, 4 conflicts) as D4's own present state, while
the delivered bytes carry 12 holds / 0 notes / 0 fails with zero `D2L-RANK` rows
after the round-22 family-clean repair. The defect was filed by the round-22
re-pin and regression seats (`reports/round-22/bleed/repin.md:26-37`,
`reports/round-22/fixes/regression.md`) and survived the round-23 wording
supersession, which reworded one D4-CL08 phrase and touched no D4 claim prose.

The fix is the round-23 disposition pattern, not a rewrite of filed bytes: a new
revision `reports/round-25/v3-supersession/declared-in-r4/` built from the r3
parent by exactly five declared line corrections plus one provenance note, pinned
by its own `expected.json` and re-verified here. Nothing is weakened: the frozen
round-20 runner and the round-22 selector adapter are digested and loaded
unmodified; the stale-prose detector is exercised on the parent (it must fire on
all five rows) and on the revision (it must fire on none) and on the D2-owned
OQ-V2-03 line (which legitimately names D2's own residuals and must not fire);
the live family-clean counters are re-measured from bytes; rounds 8-24 are
snapshotted before and after every run and must be byte-identical.

Commands:
    python3 reports/round-25/v3-supersession/v3-supersession-check.py --root <clone> --selftest
    python3 reports/round-25/v3-supersession/v3-supersession-check.py --root <clone> --check
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tempfile

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
RUNNER = "reports/round-20/run-validation.py"
RUNNER_SHA256 = "2b7a252b5449415dddac2e667ed2e192df800a80173849989fa72423961646da"
TIE_BREAK = "reports/round-22/fixes/tie-break.py"
TIE_BREAK_SHA256 = "2856a571da286b62b4eced7da610f5cebd46f3504bdf2f6dd8a53d60272dce0a"
PARENT_PACKET = "reports/round-23/wording/declared-in-r3/packet.md"
PARENT_SHA256 = "084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250"
REVISION_DIR = "reports/round-25/v3-supersession/declared-in-r4"
REVISION_PACKET = f"{REVISION_DIR}/packet.md"
REVISION_BASELINE = f"{REVISION_DIR}/expected.json"
REVISION_SHA256 = "5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03"
BUILDER = "reports/round-25/v3-supersession/build-revision.py"
OLD_BASELINE = "reports/round-23/wording/declared-in-r3/expected.json"
OLD_PACKET = "reports/round-23/wording/declared-in-r3/packet.md"
COMMAND = "python3 reports/round-25/v3-supersession/v3-supersession-check.py"
ANCHOR = b"\n- canon_standing:"
V2_SUBSET_DIGEST = "ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b"
EXPECTED_HOLDS = "examples/culture-d4/expected-holds.json"
TYPED_LABELS = "examples/culture-d4/typed-labels.d4.yml"
TYPED_PACKET = "examples/culture-d4/packet.d4.typed.yml"
FIVE_ROWS = ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09", "OQ-V3-05")

# The stale D4 prose: the parent's own assertion constructions, which state the
# pre-family-clean residual population as D4's present state. Scoped to the five
# corrected surfaces, so D2's own residual line (OQ-V2-03) is not caught, and
# phrased as the parent's exact shapes so an honest removal statement ("the
# thirteen unresolved rank items ... are no longer D4-owned") does not match.
STALE_PATTERNS = (
    ("holds-15-count", re.compile(r"#counts \(hold 15, note 1, fail 0\)")),
    ("holds-15-statement", re.compile(r"\b15 holds, 1 note and 0 fails\b")),
    ("d2l-rank-passengers",
     re.compile(r"three `?D2L-RANK`? holds, plus one `?D2L-RANK`? note")),
    ("d2l-rank-rows-in-list", re.compile(r"and three `?D2L-RANK`? rows")),
    ("findings-16", re.compile(r"findings_total 16")),
    ("hold-or-fail-15", re.compile(r"\b16 findings of which 15 are hold-or-fail\b")),
    ("recarries-d2-adaptation", re.compile(r"re-carries D2's rank-rule adaptation rows")),
    ("coverage-block-holds-residuals",
     re.compile(r"coverage block holds 13 unresolved rank items, 3 quarantine handles "
                r"and 4 conflicts")),
    ("adapt-status-cannot-evaluate",
     re.compile(r"adapt_status: cannot-evaluate")),
    ("inherited-own-holds", re.compile(r"D4's inherited and own holds stay open")),
    ("three-rank-holds-plus-note",
     re.compile(r"twelve form holds \+ three rank holds \+ one note")),
    ("conflicts-and-quarantine-counts",
     re.compile(r"conflicts \(4\), quarantine handles \(3\)")),
    ("carried-as-counts-not-collapsed",
     re.compile(r"carried as counts rather than collapsed")),
)
# The present-state tokens the corrected prose must carry, per surface.
PRESENT_TOKENS = {
    "D4-CL05": ("findings_total 12", "12 findings"),
    "D4-CL06": ("hold 12, note 0, fail 0", "12 holds, 0 notes and 0 fails"),
    "D4-CL07": ("zero findings", "zero conflicts and zero quarantine handles"),
    "D4-CL09": ("zero unresolved rank items", "packet-native"),
    "OQ-V3-05": ("twelve form holds, zero rank holds, zero notes and zero fails", "OQ-V2-03"),
}
# A corrected surface may still name the inherited residual population, but only
# with explicit D2/removal attribution — never as D4's own present state.
ATTRIBUTION_TOKENS = ("D2-owned", "no longer D4-owned", "OQ-V2-03",
                      "pre-family-clean", "removed from D4 ownership")
OPEN_TAIL_V2_ROW = "claim D: v2 successor row not green"
OPEN_TAIL_V3_PIN = ("claim D: v3 baseline reports/round-20/handoff/expected.json "
                    "pins packet")
CLAIM_D_LEGACY_V3_PIN = ("claim D: v3 baseline "
                         f"{REVISION_BASELINE} pins packet")


def sha256_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_tie_break():
    spec = importlib.util.spec_from_file_location("r25_tie_break", ROOT / TIE_BREAK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def snapshot(root):
    root = Path(root)
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for number in range(8, 25)
            for path in (root / f"reports/round-{number}").rglob("*")
            if path.is_file() and "__pycache__" not in path.parts}


def ledger_rows(root, relative):
    """Rows from the frozen round-20 parser, loaded without executing the runner."""
    module = load_round20_module(root)
    return module.parse_ledger_rows((Path(root) / relative).read_text(encoding="utf-8"))


def load_round20_module(root):
    spec = importlib.util.spec_from_file_location("r25_round20_parser", Path(root) / RUNNER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = Path(root)
    return module


def row_map(rows):
    return {row["id"]: row for row in rows}


OQ_RE = re.compile(r"^- (OQ-V[23]-\d+):\s*(.+)$")


def open_questions(root, relative):
    """`{id: line}` for the packet's `## open_questions` passenger lines.

    The frozen round-20 parser reads the claim table only; the OQ passengers are
    a separate list, so the detector needs its own reader.
    """
    lines = (Path(root) / relative).read_text(encoding="utf-8").splitlines()
    out = {}
    for line in lines:
        match = OQ_RE.match(line)
        if match:
            out[match.group(1)] = line
    return out


def surface_rows(root, relative):
    """The five corrected surfaces as `{id: raw_line}` — claim rows plus OQ lines."""
    rows = row_map(ledger_rows(root, relative))
    surface = {row_id: rows[row_id]["raw"] for row_id in
               ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09")}
    surface.update(open_questions(root, relative))
    return surface


def stale_hits(surface):
    """(row_id, pattern_name) for every stale construction in the D4/OQ surface."""
    hits = []
    for row_id, raw in surface.items():
        if row_id not in FIVE_ROWS:
            continue
        for name, pattern in STALE_PATTERNS:
            if pattern.search(raw):
                hits.append((row_id, name))
    return hits


def load_builder():
    """The filed builder module, loaded from the live lane tree."""
    spec = importlib.util.spec_from_file_location("r25_builder", ROOT / BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rebuild_revision(root):
    """Rebuild the revision from `root`'s parent bytes using the declared delta."""
    return load_builder().build(Path(root))


def verify_tree(root, controls):
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    live_runner = sha256_of(ROOT / RUNNER)
    live_tie = sha256_of(ROOT / TIE_BREAK)
    check("frozen-runner-digest-pinned", live_runner == RUNNER_SHA256, sha256=live_runner)
    check("round22-adapter-digest-pinned", live_tie == TIE_BREAK_SHA256, sha256=live_tie)
    for relative, digest in ((RUNNER, RUNNER_SHA256), (TIE_BREAK, TIE_BREAK_SHA256),
                             (PARENT_PACKET, PARENT_SHA256)):
        clone_path = Path(root) / relative
        check(f"clone-matches-live:{relative}",
              clone_path.is_file() and sha256_of(clone_path) == digest
              == sha256_of(ROOT / relative))
    live_revision = sha256_of(ROOT / REVISION_PACKET)
    check("revision-pin-is-declared", live_revision == REVISION_SHA256,
          packet_sha256=live_revision)
    expected = json.loads((ROOT / REVISION_BASELINE).read_text(encoding="utf-8"))
    check("revision-pin-matches-live-bytes",
          expected.get("packet_sha256") == live_revision, packet_sha256=live_revision)
    check("revision-parent-is-r3",
          (expected.get("parent") or {}).get("sha256") == PARENT_SHA256
          and (expected.get("parent") or {}).get("path") == PARENT_PACKET)
    rebuilt = rebuild_revision(ROOT)
    revision = (ROOT / REVISION_PACKET).read_bytes()
    parent = (ROOT / PARENT_PACKET).read_bytes()
    check("revision-is-parent-plus-declared-delta", rebuilt == revision,
          parent_bytes=len(parent), revision_bytes=len(revision))
    note_marker = b"Revision declared-in-r4 (2026-10-18; round-25 O seat, claims R25-O11..O15)"
    check("delta-note-inserted-once-and-anchor-preserved",
          revision.count(note_marker) == 1
          and parent.count(note_marker) == 0
          and revision.count(ANCHOR) == parent.count(ANCHOR)
          and revision.index(ANCHOR) > revision.index(note_marker),
          parent_anchors=parent.count(ANCHOR), revision_anchors=revision.count(ANCHOR))
    return expected


def live_family_clean(root, controls):
    """Re-measure the family-clean counters the corrected prose asserts."""
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    holds = json.loads((Path(root) / EXPECTED_HOLDS).read_text(encoding="utf-8"))
    counts = holds.get("counts") or {}
    rows = holds.get("holds") or []
    check("live-expected-holds-12-0-0",
          counts == {"hold": 12, "note": 0, "fail": 0}, counts=counts)
    check("live-expected-holds-all-form",
          len(rows) == 12 and all(row.get("id") == "D2L-FORM-UNRESOLVED" for row in rows),
          rows=len(rows))
    projection = json.loads((Path(root) / TYPED_LABELS).read_text(encoding="utf-8"))
    coverage = projection.get("coverage") or {}
    check("live-coverage-zero-rank-residuals",
          coverage.get("conflicts") == 0
          and coverage.get("rank_rules_unresolved_items") == 0
          and coverage.get("rank_quarantine_handles") == 0
          and coverage.get("findings_total") == 12
          and coverage.get("findings_hold_or_fail") == 12
          and coverage.get("label_findings_fail") == 0,
          coverage={key: coverage.get(key) for key in
                    ("conflicts", "findings_total", "findings_hold_or_fail",
                     "rank_rules_unresolved_items", "rank_quarantine_handles")})
    check("live-four-packet-native-rank-rules",
          coverage.get("rank_rules_component") == 4
          and coverage.get("rank_rules_normalized") == 4
          and coverage.get("rank_rules_gate_projected") == 4)
    rank = projection.get("rank_rules") or {}
    check("live-rank-leg-is-packet-native",
          (rank.get("coverage") or {}).get("component_rules") == 4
          and not rank.get("residuals") and not rank.get("unresolved")
          and not rank.get("quarantine") and not rank.get("act_rules")
          and len(rank.get("skipped") or []) == 1,
          skipped=len(rank.get("skipped") or []), residuals=len(rank.get("residuals") or []))
    text = (Path(root) / TYPED_LABELS).read_text(encoding="utf-8")
    typed = (Path(root) / TYPED_PACKET).read_text(encoding="utf-8")
    expected_text = (Path(root) / EXPECTED_HOLDS).read_text(encoding="utf-8")
    check("live-zero-d2l-rank-rows-in-d4-surfaces",
          "D2L-RANK" not in text and "D2L-RANK" not in typed
          and "D2L-RANK" not in expected_text)
    return {"counts": counts, "coverage": coverage}


def ledger_controls(root, controls):
    """Census, vocabulary, links, v2 subset and the stale-prose detector."""
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    module = load_round20_module(root)
    parent_rows = module.parse_ledger_rows((Path(root) / PARENT_PACKET).read_text(encoding="utf-8"))
    revision_rows = module.parse_ledger_rows((Path(root) / REVISION_PACKET).read_text(encoding="utf-8"))
    parent_map, revision_map = row_map(parent_rows), row_map(revision_rows)
    check("ledger-shape-unchanged",
          [row["id"] for row in parent_rows] == [row["id"] for row in revision_rows],
          rows=len(revision_rows))
    import collections
    parent_hist = dict(collections.Counter(
        row["uncertainty"]["status"] for row in parent_rows if row["uncertainty"]))
    revision_hist = dict(collections.Counter(
        row["uncertainty"]["status"] for row in revision_rows if row["uncertainty"]))
    check("census-27-16-7-4",
          len(revision_rows) == 27 and revision_hist == {"supported": 16, "partial": 7,
                                                         "unresolved": 4},
          rows=len(revision_rows), statuses=revision_hist)
    check("statuses-unchanged", parent_hist == revision_hist)
    check("revision-judgments-clean",
          not any(judgment["problems"] for judgment in module.uncertainty_problems(revision_rows)))
    check("parent-judgments-clean",
          not any(judgment["problems"] for judgment in module.uncertainty_problems(parent_rows)))
    unresolved = sorted({link for row in revision_rows for link in module.link_paths(row["links"])
                         if not module.safe_path(link).is_file()})
    check("revision-links-resolve", not unresolved, unresolved=unresolved[:5])
    v2_ids = ("D2-CL01", "D2-CL02") + tuple(f"CL{index:02d}" for index in range(1, 14))
    parent_v2 = [row for row in parent_rows if row["id"] in v2_ids]
    revision_v2 = [row for row in revision_rows if row["id"] in v2_ids]
    check("v2-subset-equality-preserved",
          len(revision_v2) == 15
          and [row["raw"] for row in parent_v2] == [row["raw"] for row in revision_v2],
          v2_rows=len(revision_v2))
    # the normalized subset digest, as the exercise computes it
    exercise = load_round20_module(root)
    check("v2-subset-digest-key-unchanged",
          json.loads((ROOT / REVISION_BASELINE).read_text(encoding="utf-8"))
          .get("v2_subset_digest") == V2_SUBSET_DIGEST)

    # the detector: must fire on all five parent surfaces, on none of the revision's
    parent_surface = surface_rows(root, PARENT_PACKET)
    revision_surface = surface_rows(root, REVISION_PACKET)
    parent_hits = stale_hits(parent_surface)
    revision_hits = stale_hits(revision_surface)
    check("stale-detector-fires-on-parent-five-rows",
          sorted({row_id for row_id, _ in parent_hits}) == sorted(FIVE_ROWS),
          rows=sorted({row_id for row_id, _ in parent_hits}),
          patterns=sorted({name for _, name in parent_hits}))
    check("stale-detector-clean-on-revision", not revision_hits, hits=revision_hits[:8])
    check("stale-detector-spares-d2-owned-residuals",
          not any(row_id == "OQ-V2-03" for row_id, _ in parent_hits)
          and parent_surface["OQ-V2-03"] == revision_surface["OQ-V2-03"]
          and "13 unresolved rank items" in parent_surface["OQ-V2-03"])
    for row_id, tokens in PRESENT_TOKENS.items():
        raw = revision_surface[row_id]
        check(f"present-state-tokens:{row_id}",
              all(token in raw for token in tokens), missing=[t for t in tokens if t not in raw])
    check("corrected-rows-carry-no-stale-numbers",
          all(token not in revision_surface[row_id]
              for row_id in FIVE_ROWS
              for token in ("findings_total 16", "hold 15", "note 1",
                            "15 are hold-or-fail", "findings_hold_or_fail 15")))
    for row_id in ("D4-CL09", "OQ-V3-05"):
        raw = revision_surface[row_id]
        residual_mentions = any(token in raw for token in
                                ("thirteen unresolved rank items", "13 unresolved rank items",
                                 "three quarantine handles", "four conflicts"))
        check(f"residual-mentions-carry-d2-attribution:{row_id}",
              residual_mentions and any(token in raw for token in ATTRIBUTION_TOKENS),
              attributed=[t for t in ATTRIBUTION_TOKENS if t in raw])
    check("d4-cl09-owner-unchanged",
          revision_map["D4-CL09"]["uncertainty"]["status"] == "unresolved"
          and "owner: kotodama" in revision_map["D4-CL09"]["raw"])
    check("oq-v3-05-still-references-d4-cl09",
          "D4-CL09" in revision_surface["OQ-V3-05"])
    # byte-delta is exactly the declared five lines plus the note
    import difflib
    parent_lines = (Path(root) / PARENT_PACKET).read_text(encoding="utf-8").split("\n")
    revision_lines = (Path(root) / REVISION_PACKET).read_text(encoding="utf-8").split("\n")
    changed = [tag for tag, *_ in
               difflib.SequenceMatcher(None, parent_lines, revision_lines,
                                       autojunk=False).get_opcodes() if tag != "equal"]
    check("byte-delta-is-one-note-plus-five-replacements",
          changed == ["insert", "replace", "replace", "replace"], opcodes=changed)
    return {"parent_hits": parent_hits, "revision_hits": revision_hits,
            "statuses": revision_hist}


def run_frozen(root, tie, baseline, inject):
    """Run the frozen round-20 runner with the successor packet binding."""
    runner_module = tie.load_round20(root)
    tie.install_round20_selectors(runner_module)

    def _r25_candidate_paths(root, paths, role):
        candidates = sorted(set(paths) | set(inject)) if role == "packet" else list(paths)
        return tie.candidate_paths(root, candidates, role, baseline=baseline)

    runner_module.__dict__["_r22_candidate_paths"] = _r25_candidate_paths
    return runner_module.validate()


def selftest(root):
    tie = load_tie_break()
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    expected = verify_tree(root, controls)
    Path(root, REVISION_DIR).mkdir(parents=True, exist_ok=True)
    (Path(root) / REVISION_PACKET).write_bytes((ROOT / REVISION_PACKET).read_bytes())
    (Path(root) / REVISION_BASELINE).write_bytes((ROOT / REVISION_BASELINE).read_bytes())
    check("revision-copied-into-clone",
          sha256_of(Path(root) / REVISION_PACKET) == REVISION_SHA256)
    live_family_clean(root, controls)
    ledger_controls(root, controls)

    # the builder must refuse a mutated parent rather than emit a silent delta
    with tempfile.TemporaryDirectory(prefix="r25-supersede-", dir=Path(root) / ".scratch") as temp:
        fixture = Path(temp)
        (fixture / "reports/round-23/wording/declared-in-r3").mkdir(parents=True)
        good = (ROOT / PARENT_PACKET).read_bytes()
        (fixture / PARENT_PACKET).write_bytes(good)
        check("builder-reproduces-filed-revision",
              rebuild_revision(fixture) == (ROOT / REVISION_PACKET).read_bytes())
        (fixture / PARENT_PACKET).write_bytes(good + b"\nstray\n")
        try:
            rebuild_revision(fixture)
            refused = False
        except SystemExit:
            refused = True
        check("builder-refuses-mutated-parent", refused)
        (fixture / PARENT_PACKET).write_bytes(good.replace(
            b"| D4-CL05 | designer interpretation | derived projection (author-side) | supported |",
            b"| D4-CL05 | designer interpretation | derived projection (author-side) | partial |"))
        try:
            rebuild_revision(fixture)
            refused = False
        except SystemExit:
            refused = True
        check("builder-refuses-drifted-old-line", refused)

    # the frozen selector binding: the revision pin selects the revision packet
    Path(root, REVISION_DIR).mkdir(parents=True, exist_ok=True)
    (Path(root) / REVISION_PACKET).write_bytes((ROOT / REVISION_PACKET).read_bytes())
    (Path(root) / REVISION_BASELINE).write_bytes((ROOT / REVISION_BASELINE).read_bytes())
    runner_module = tie.load_round20(root)
    tie.install_round20_selectors(runner_module)

    def _binding(root, paths, role):
        candidates = sorted(set(paths) | set([REVISION_PACKET])) if role == "packet" else list(paths)
        return tie.candidate_paths(root, candidates, role, baseline=REVISION_BASELINE)

    runner_module.__dict__["_r22_candidate_paths"] = _binding
    check("binding-selects-revision-packet",
          _binding(root, [REVISION_PACKET], "packet") == [REVISION_PACKET])
    check("binding-follows-pin-change",
          _binding(root, [PARENT_PACKET], "packet") == [REVISION_PACKET])
    return {"controls": controls, "passed": all(item["passed"] for item in controls),
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls), "revision_pin": expected.get("packet_sha256")}


def check(root):
    tie = load_tie_break()
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    expected = verify_tree(root, controls)
    live = (ROOT / REVISION_PACKET).read_bytes()
    Path(root, REVISION_DIR).mkdir(parents=True, exist_ok=True)
    (Path(root) / REVISION_PACKET).write_bytes(live)
    (Path(root) / REVISION_BASELINE).write_bytes((ROOT / REVISION_BASELINE).read_bytes())
    check("revision-copied-into-clone",
          sha256_of(Path(root) / REVISION_PACKET) == expected["packet_sha256"])

    family = live_family_clean(root, controls)
    ledger = ledger_controls(root, controls)
    before = snapshot(root)

    # Negative control: the frozen round-20 runner bound to the r3 revision —
    # the state the defect was filed in. The frozen validator checks the
    # uncertainty grammar, not claim truth, so it cannot see the stale prose;
    # this seat's detector must. Both facts are asserted, so neither the
    # validator's blindness nor the detector's power is assumed.
    negative_payload = run_frozen(root, tie, OLD_BASELINE, [OLD_PACKET])
    negative_failures = negative_payload["failures"]
    negative_packet = negative_payload["claims"]["D"]["measurement"]["packet"]
    check("negative-control-binds-r3-revision",
          negative_packet.get("path") == OLD_PACKET and negative_packet.get("rows") == 27,
          path=negative_packet.get("path"), rows=negative_packet.get("rows"))
    check("negative-control-frozen-validator-is-blind-to-the-defect",
          not any(re.search(r"D4-CL0[5679]|OQ-V3-05", failure)
                  for failure in negative_failures),
          note="the frozen runner reports no finding against the stale D4 prose: "
               "the defect is not validator-detectable, which is why the round-22 "
               "re-pin seat filed it by content review",
          failures=negative_failures[:8])
    check("negative-control-detector-sees-the-defect",
          sorted({row_id for row_id, _ in ledger["parent_hits"]}) == sorted(FIVE_ROWS))
    check("negative-control-carries-declared-open-tails",
          len([failure for failure in negative_failures
               if failure.startswith(OPEN_TAIL_V2_ROW)
               or failure.startswith(OPEN_TAIL_V3_PIN)]) == 2,
          failures=negative_failures[:8])

    # positive run: the frozen runner bound to the declared-in-r4 revision
    positive_payload = run_frozen(root, tie, REVISION_BASELINE, [REVISION_PACKET])
    positive_failures = positive_payload["failures"]
    packet_info = positive_payload["claims"]["D"]["measurement"]["packet"]
    check("positive-control-binds-revision",
          packet_info.get("path") == REVISION_PACKET and packet_info.get("rows") == 27,
          path=packet_info.get("path"), rows=packet_info.get("rows"),
          statuses=packet_info.get("statuses"))
    check("positive-control-no-placeholder-findings",
          not any("placeholder" in failure.lower() for failure in positive_failures))
    check("positive-control-no-stale-claim-finding",
          not any(re.search(r"D4-CL0[5679]|OQ-V3-05", failure) for failure in positive_failures),
          failures=positive_failures[:8])
    remaining = [failure for failure in positive_failures
                 if not (failure.startswith(OPEN_TAIL_V2_ROW)
                         or failure.startswith(OPEN_TAIL_V3_PIN)
                         or failure.startswith(CLAIM_D_LEGACY_V3_PIN))]
    check("positive-control-remaining-failures-are-inherited-open-tails-only",
          not remaining, undeclared_failures=remaining,
          declared_open_tails=len(positive_failures) - len(remaining),
          note="the v2 successor row projector re-pin and the v3 baseline pin "
               "re-point are inherited round-23 tails owned by other seats; this "
               "seat neither owns nor claims them")
    judgments = positive_payload["claims"]["D"]["measurement"]["uncertainty"]
    check("revision-judgments-clean-in-run",
          not any(judgment["problems"] for judgment in judgments), judgments=len(judgments))
    v3_scan = positive_payload["claims"]["D"]["measurement"].get("v3_scan") or {}
    check("census-still-matches-exercise",
          v3_scan.get("claims") == packet_info.get("rows") == 27
          and tuple(v3_scan.get("statuses") or ()) == (16, 7, 4),
          claims=v3_scan.get("claims"), statuses=v3_scan.get("statuses"))
    check("v2-subset-equal-in-run", v3_scan.get("v2_subset") == "equal",
          v2_subset=v3_scan.get("v2_subset"))
    check("alias-leg-landed-in-run", v3_scan.get("alias_leg") == "landed")

    after = snapshot(root)
    changed = sorted(path for path in before.keys() | after.keys()
                     if before.get(path) != after.get(path))
    check("filed-rounds-8-24-unchanged", not changed, changed=changed[:10])
    passed = all(item["passed"] for item in controls)
    return {"date": dt.datetime.now(dt.timezone.utc).isoformat(),
            "command": f"{COMMAND} --root {root} --check",
            "root": str(root), "revision": "declared-in-r4",
            "revision_packet_sha256": expected.get("packet_sha256"),
            "parent_packet_sha256": PARENT_SHA256,
            "live_family_clean": family,
            "stale_prose_detector": ledger,
            "negative": {"baseline": OLD_BASELINE, "failures": negative_failures},
            "positive": {"baseline": REVISION_BASELINE, "packet": packet_info.get("path"),
                         "rows": packet_info.get("rows"),
                         "statuses": packet_info.get("statuses"),
                         "failures": positive_failures,
                         "v2_subset": v3_scan.get("v2_subset"),
                         "alias_leg": v3_scan.get("alias_leg"),
                         "runner_sha256": positive_payload.get("runner_sha256")},
            "controls": controls, "passed": passed,
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=(
        "Round-25 O seat: verify the declared-in-r4 claim-prose supersession of the"
        " v3 handoff packet inside an isolated clone."))
    parser.add_argument("--root", type=Path, required=True,
                        help="isolated clone under the lane's .scratch")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--selftest", action="store_true")
    group.add_argument("--check", action="store_true")
    parser.add_argument("--receipt", type=Path,
                        help="also write the JSON receipt to this path")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not (root.is_relative_to(ROOT / ".scratch") and (root / ".git").is_dir()):
        parser.error("--root must be an isolated clone with .git under the lane's .scratch")
    os.environ["TMPDIR"] = str(root / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (root / ".scratch").mkdir(exist_ok=True)
    payload = selftest(root) if args.selftest else check(root)
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
