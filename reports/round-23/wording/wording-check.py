#!/usr/bin/env python3
"""R23 wording successor — reworded-packet binding for the frozen round-20 check.

Disposition of the round-22 tail (reports/round-22/fixes/tie-break.md,
reports/round-22/routed-resolution.json): the frozen round-20 `PLACEHOLDER_RE`
matches the standalone token `unchanged` inside the legitimate hyphenated
compound `unchanged-foreign-path` in D4-CL08's uncertainty basis, so the full
historical successor check exits 1 on exactly that finding. The preferred
disposition is applied here: the validators stay byte-frozen; the packet
lineage gains a reworded revision (reports/round-23/wording/declared-in-r3/,
parent reports/round-22/handoff/declared-in-r2/packet.md 3.1.1) and this
successor rebinds the historical packet baseline pin to that revision inside an
isolated clone under the lane's .scratch.

Nothing is weakened: the frozen runner and the round-22 selector adapter are
digested and loaded unmodified; the controls re-exercise PLACEHOLDER_RE and
uncertainty_problems on real placeholder fixtures (they must still fire) and on
the old basis (the false positive must reproduce) and on the revision's basis
(it must be clean). Rounds 8-22 are snapshotted before and after every run and
must be byte-identical.

Commands:
    python3 reports/round-23/wording/wording-check.py --root <clone> --selftest
    python3 reports/round-23/wording/wording-check.py --root <clone> --check
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import inspect
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
PARENT_PACKET = "reports/round-22/handoff/declared-in-r2/packet.md"
PARENT_SHA256 = "a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e"
REVISION_DIR = "reports/round-23/wording/declared-in-r3"
REVISION_PACKET = f"{REVISION_DIR}/packet.md"
REVISION_BASELINE = f"{REVISION_DIR}/expected.json"
OLD_BASELINE = "reports/round-20/handoff/expected.json"
OLD_PHRASE = "the unchanged-foreign-path control is"
NEW_PHRASE = "the foreign-path-stability control is"
OPEN_TAIL_V2_ROW = "claim D: v2 successor row not green"
OPEN_TAIL_V3_PIN = ("claim D: v3 baseline reports/round-20/handoff/expected.json "
                    "pins packet")
COMMAND = "python3 reports/round-23/wording/wording-check.py"


def sha256_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_tie_break():
    spec = importlib.util.spec_from_file_location("r23_tie_break", ROOT / TIE_BREAK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def snapshot(root):
    root = Path(root)
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for number in range(8, 23)
            for path in (root / f"reports/round-{number}").rglob("*")
            if path.is_file() and "__pycache__" not in path.parts}


def install(runner_module, tie, baseline, inject):
    tie.install_round20_selectors(runner_module)

    def _r23_candidate_paths(root, paths, role):
        candidates = sorted(set(paths) | set(inject)) if role == "packet" else list(paths)
        return tie.candidate_paths(root, candidates, role, baseline=baseline)

    runner_module.__dict__["_r22_candidate_paths"] = _r23_candidate_paths
    return runner_module


def run_validate(root, tie, baseline, inject):
    runner_module = tie.load_round20(root)
    install(runner_module, tie, baseline, inject)
    return runner_module.validate(), runner_module


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
    expected = json.loads((ROOT / REVISION_BASELINE).read_text(encoding="utf-8"))
    check("revision-pin-matches-live-bytes",
          expected.get("packet_sha256") == live_revision, packet_sha256=live_revision)
    parent = (ROOT / PARENT_PACKET).read_bytes()
    revision = (ROOT / REVISION_PACKET).read_bytes()
    rebuilt = parent.replace(OLD_PHRASE.encode(), NEW_PHRASE.encode())
    anchor = b"\n- canon_standing:"
    note = revision[rebuilt.index(anchor):]
    note = note[:note.index(anchor)]
    check("revision-is-parent-plus-declared-delta",
          rebuilt.replace(anchor, note + anchor, 1) == revision
          and parent.count(OLD_PHRASE.encode()) == 1
          and revision.count(NEW_PHRASE.encode()) == 1
          and revision.count(OLD_PHRASE.encode()) == 0
          and revision.count(b"unchanged-foreign-path") == 1,
          parent_bytes=len(parent), revision_bytes=len(revision))
    return expected


def measure_d_code_names(code):
    names = set(code.co_names)
    for constant in code.co_consts:
        if isinstance(constant, type(code)):
            names |= measure_d_code_names(constant)
    return names


def selftest(root):
    tie = load_tie_break()
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    expected = verify_tree(root, controls)
    clone_revision = Path(root) / REVISION_PACKET
    clone_revision.parent.mkdir(parents=True, exist_ok=True)
    clone_revision.write_bytes((ROOT / REVISION_PACKET).read_bytes())
    (Path(root) / REVISION_BASELINE).write_bytes((ROOT / REVISION_BASELINE).read_bytes())

    runner_module = tie.load_round20(root)
    phrase = re.compile(r"\b(tbd|tba|todo|placeholder|boilerplate|"
                        r"same[- ]as[- ](?:above|below)|as (?:above|below)|"
                        r"see (?:above|below|other)|copy of|unchanged)\b", re.I)
    check("frozen-placeholder-re-unchanged",
          runner_module.PLACEHOLDER_RE.pattern == phrase.pattern
          and runner_module.PLACEHOLDER_RE.flags == phrase.flags)
    for sample in ("review pending, see above", "this basis is TBD",
                   "placeholder row", "copy of the v2 row", "todo: fill",
                   "the D2 output is unchanged"):
        check(f"placeholder-still-caught:{sample[:24]}",
              bool(runner_module.PLACEHOLDER_RE.search(sample)))

    parent_text = (ROOT / PARENT_PACKET).read_text(encoding="utf-8")
    revision_text = (ROOT / REVISION_PACKET).read_text(encoding="utf-8")
    parent_rows = runner_module.parse_ledger_rows(parent_text)
    revision_rows = runner_module.parse_ledger_rows(revision_text)
    check("ledger-shape-unchanged",
          [row["id"] for row in parent_rows] == [row["id"] for row in revision_rows],
          rows=len(revision_rows))
    old_row = next(row for row in parent_rows if row["id"] == "D4-CL08")
    new_row = next(row for row in revision_rows if row["id"] == "D4-CL08")
    check("old-basis-triggers-frozen-rule",
          bool(runner_module.PLACEHOLDER_RE.search(old_row["uncertainty"]["basis"])))
    check("old-judgment-flags-placeholder",
          any("placeholder basis" in problem for problem in
              runner_module.uncertainty_problems(parent_rows)[
                  [row["id"] for row in parent_rows].index("D4-CL08")]["problems"]))
    check("new-basis-clean-under-frozen-rule",
          not runner_module.PLACEHOLDER_RE.search(new_row["uncertainty"]["basis"]))
    check("revision-judgments-clean",
          not any(judgment["problems"] for judgment in
                  runner_module.uncertainty_problems(revision_rows)))
    check("statuses-unchanged",
          [row["uncertainty"]["status"] for row in parent_rows]
          == [row["uncertainty"]["status"] for row in revision_rows])

    with tempfile.TemporaryDirectory(prefix="r23-wording-", dir=Path(root) / ".scratch") as temp:
        fixture = Path(temp)

        def put(relative, data):
            path = fixture / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        put("packet-a.md", b"# Handoff packet\nclaim_ledger a\n")
        put("packet-b.md", b"# Handoff packet\nclaim_ledger b\n")
        put("audit-1.md", b"# Contract audit v3\nbuild 16\nVerdict: PASS\n")
        pinned = hashlib.sha256((fixture / "packet-a.md").read_bytes()).hexdigest()
        put("expected.json", json.dumps({"packet_sha256": pinned}).encode())

        def wrapper(paths, role, baseline="expected.json", inject=()):
            candidates = sorted(set(paths) | set(inject)) if role == "packet" else list(paths)
            return tie.candidate_paths(fixture, candidates, role, baseline=baseline)

        check("binding-selects-pinned-packet",
              wrapper(["packet-a.md", "packet-b.md"], "packet") == ["packet-a.md"])
        other = hashlib.sha256((fixture / "packet-b.md").read_bytes()).hexdigest()
        put("expected.json", json.dumps({"packet_sha256": other}).encode())
        check("binding-follows-repin",
              wrapper(["packet-a.md"], "packet", inject=["packet-b.md"]) == ["packet-b.md"])
        put("expected.json", json.dumps({"packet_sha256": "0" * 64}).encode())
        try:
            wrapper(["packet-a.md"], "packet")
            refused = False
        except tie.SelectionError:
            refused = True
        check("unmatched-pin-refused", refused)
        check("audit-role-ignores-pin",
              wrapper(["audit-1.md"], "audit") == ["audit-1.md"])
        put("outside.md", b"x")
        try:
            tie.candidate_paths(fixture, ["../outside.md"], "packet", baseline="expected.json")
            refused = False
        except tie.SelectionError:
            refused = True
        check("outside-candidate-refused", refused)

    install(runner_module, tie, REVISION_BASELINE, [REVISION_PACKET])
    names = measure_d_code_names(runner_module.measure_d.__code__)
    check("installed-selectors-use-successor-paths",
          "_r22_candidate_rank" in names and "_r22_candidate_paths" in names)
    check("installed-measure-d-has-no-mtime-lookup", "st_mtime" not in names)
    check("wrapper-binding-reaches-revision-baseline",
          runner_module.__dict__["_r22_candidate_paths"](
              Path(root), [REVISION_PACKET], "packet") == [REVISION_PACKET],
          baseline=REVISION_BASELINE)
    return {"controls": controls, "passed": all(item["passed"] for item in controls),
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls), "revision_pin": expected.get("packet_sha256")}


def check(root):
    tie = load_tie_break()
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    expected = verify_tree(root, controls)
    revision_live = (ROOT / REVISION_PACKET).read_bytes()
    clone_revision = Path(root) / REVISION_PACKET
    clone_revision.parent.mkdir(parents=True, exist_ok=True)
    clone_revision.write_bytes(revision_live)
    (Path(root) / REVISION_BASELINE).write_bytes((ROOT / REVISION_BASELINE).read_bytes())
    check("revision-copied-into-clone",
          sha256_of(clone_revision) == expected["packet_sha256"])

    before = snapshot(root)

    negative_payload, _ = run_validate(root, tie, OLD_BASELINE, [])
    negative_failures = negative_payload["failures"]
    placeholder_failures = [failure for failure in negative_failures
                            if "placeholder basis" in failure and "D4-CL08" in failure]
    check("negative-control-reproduces-false-positive",
          bool(placeholder_failures)
          and any("unchanged-foreign-path" in failure for failure in placeholder_failures),
          failure_count=len(negative_failures),
          failures=negative_failures[:6])
    check("negative-control-binds-filed-packet",
          negative_payload["claims"]["D"]["measurement"]["packet"]["path"]
          == "reports/round-20/handoff/packet.md")
    open_tails = [failure for failure in negative_failures
                  if failure.startswith(OPEN_TAIL_V2_ROW) or failure.startswith(OPEN_TAIL_V3_PIN)]
    check("open-tails-pre-exist-negative-run-and-are-not-adapter-caused",
          len(open_tails) == 2, open_tails=open_tails)

    positive_payload, positive_module = run_validate(root, tie, REVISION_BASELINE,
                                                     [REVISION_PACKET])
    positive_failures = positive_payload["failures"]
    packet_info = positive_payload["claims"]["D"]["measurement"]["packet"]
    check("positive-control-wording-tail-eliminated",
          not any("placeholder" in failure.lower() for failure in positive_failures),
          failures=positive_failures)
    remaining = [failure for failure in positive_failures
                 if not (failure.startswith(OPEN_TAIL_V2_ROW)
                         or failure.startswith(OPEN_TAIL_V3_PIN))]
    check("positive-control-remaining-failures-are-declared-open-tails-only",
          not remaining, undeclared_failures=remaining,
          open_tail_count=len(positive_failures) - len(remaining),
          note="the v2-row projector re-pin (round-23 successor-pins seat) and the "
               "v3 baseline pin re-point (renderer/baseline owner) are sibling "
               "tails, declared in reports/round-23/claims.json O-before; this seat "
               "does not own them")
    check("positive-control-parses-revision",
          packet_info.get("path") == REVISION_PACKET and packet_info.get("rows"),
          path=packet_info.get("path"), rows=packet_info.get("rows"),
          statuses=packet_info.get("statuses"))
    judgments = positive_payload["claims"]["D"]["measurement"]["uncertainty"]
    check("revision-judgments-clean-in-run",
          not any(judgment["problems"] for judgment in judgments), judgments=len(judgments))
    v3_scan = positive_payload["claims"]["D"]["measurement"].get("v3_scan") or {}
    census = {"supported": v3_scan.get("statuses", [0, 0, 0])[0],
              "partial": v3_scan.get("statuses", [0, 0, 0])[1],
              "unresolved": v3_scan.get("statuses", [0, 0, 0])[2]}
    check("census-still-matches-exercise",
          bool(v3_scan.get("claims")) and v3_scan.get("claims") == packet_info.get("rows")
          and census == packet_info.get("statuses"),
          claims=v3_scan.get("claims"), rows=packet_info.get("rows"),
          statuses=v3_scan.get("statuses"), histogram=packet_info.get("statuses"))

    after = snapshot(root)
    changed = sorted(path for path in before.keys() | after.keys()
                     if before.get(path) != after.get(path))
    check("filed-rounds-8-22-unchanged", not changed, changed=changed[:10])
    passed = all(item["passed"] for item in controls)
    return {"date": dt.datetime.now(dt.timezone.utc).isoformat(),
            "command": f"{COMMAND} --root {root} --check",
            "root": str(root), "baseline_revision_declared_in_r3": expected["packet_sha256"],
            "negative": {"baseline": OLD_BASELINE, "failures": negative_failures,
                         "passed": negative_payload["acceptance_checks_passed"]},
            "positive": {"baseline": REVISION_BASELINE, "packet": packet_info.get("path"),
                         "rows": packet_info.get("rows"), "statuses": packet_info.get("statuses"),
                         "failures": positive_failures,
                         "wording_tail_eliminated":
                             not any("placeholder" in failure.lower()
                                     for failure in positive_failures),
                         "runner_sha256": positive_payload.get("runner_sha256"),
                         "round": positive_payload.get("round")},
            "controls": controls, "passed": passed,
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=(
        "Round-23 wording successor: rebinds the frozen round-20 packet pin to the"
        " declared-in-r3 reworded revision inside an isolated clone."))
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
