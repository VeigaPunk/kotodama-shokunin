#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
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
BASELINE = "reports/round-20/handoff/expected.json"
COMMAND = "python3 reports/round-22/fixes/tie-break.py"
BUILD_RE = re.compile(r"\bbuild[\s_-]?(\d+)\b", re.I)
AUDIT_RE = re.compile(r"\bcontract(?:[ -]v\d+)?[ -]+audit\b|\bcontract[ -]recheck\b", re.I)


class SelectionError(ValueError):
    pass


def content(root, relative):
    root = Path(root).resolve()
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise SelectionError(f"not a repository-relative candidate: {relative}")
    path = (root / path).resolve()
    if not path.is_relative_to(root):
        raise SelectionError(f"candidate escapes repository: {relative}")
    try:
        return path.read_bytes()
    except OSError as error:
        raise SelectionError(f"unreadable candidate {relative}: {error}") from error


def candidate_rank(root, relative):
    data = content(root, relative)
    builds = [int(match) for match in BUILD_RE.findall(data.decode("utf-8", "replace"))]
    suffix = re.search(r"(?:^|[-_])(\d+)$", Path(relative).stem)
    if suffix:
        builds.append(int(suffix.group(1)))
    return max(builds, default=-1), hashlib.sha256(data).hexdigest(), str(relative)


def candidate_paths(root, paths, role, baseline=BASELINE):
    paths = sorted(set(paths))
    if role == "audit":
        return [relative for relative in paths
                if AUDIT_RE.search(next((line for line in content(root, relative)
                                        .decode("utf-8", "replace").splitlines()
                                        if line.startswith("# ")), ""))]
    if role != "packet":
        raise SelectionError(f"unknown candidate role: {role}")
    try:
        payload = json.loads(content(root, baseline))
    except (ValueError, UnicodeError) as error:
        raise SelectionError(f"cannot bind packet candidates to {baseline}: {error}") from error
    pinned = payload.get("packet_sha256") if isinstance(payload, dict) else None
    if not isinstance(pinned, str) or not re.fullmatch(r"[0-9a-f]{64}", pinned):
        raise SelectionError(f"{baseline}: missing valid packet_sha256")
    bound = [relative for relative in paths
             if hashlib.sha256(content(root, relative)).hexdigest() == pinned]
    if not bound:
        raise SelectionError(f"no packet candidate matches {baseline}: {pinned}")
    return bound


def select_candidate(root, paths, role, baseline=BASELINE):
    eligible = candidate_paths(root, paths, role, baseline)
    return max(eligible, key=lambda relative: candidate_rank(root, relative), default=None)


def install_round20_selectors(module):
    source = Path(module.__file__).read_bytes()
    if hashlib.sha256(source).hexdigest() != RUNNER_SHA256:
        raise SelectionError("frozen round-20 runner digest changed; successor adapter refused")
    tree = ast.parse(source, filename=module.__file__)
    function = next(node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == "measure_d")
    rewrites = {"ranks": 0, "candidates": 0}

    class Selectors(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if node.name in ("build_rank", "audit_rank"):
                node.body = ast.parse("return _r22_candidate_rank(ROOT, relative)").body
                rewrites["ranks"] += 1
                return node
            return self.generic_visit(node)

        def visit_Assign(self, node):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if name in ("packet_candidates", "audit_candidates"):
                    role = "packet" if name == "packet_candidates" else "audit"
                    node.value = ast.Call(
                        func=ast.Name(id="_r22_candidate_paths", ctx=ast.Load()),
                        args=[ast.Name(id="ROOT", ctx=ast.Load()), node.value, ast.Constant(role)],
                        keywords=[])
                    rewrites["candidates"] += 1
            return node

    function = Selectors().visit(function)
    if rewrites != {"ranks": 2, "candidates": 2}:
        raise SelectionError(f"frozen round-20 selector shape changed: {rewrites}")
    replacement = ast.fix_missing_locations(ast.Module(body=[function], type_ignores=[]))
    module.__dict__.update(_r22_candidate_rank=candidate_rank, _r22_candidate_paths=candidate_paths)
    exec(compile(replacement, module.__file__, "exec"), module.__dict__)
    return module


def load_round20(root):
    root = Path(root).resolve()
    isolated = root.is_relative_to(ROOT / ".scratch") or (root == ROOT and ".scratch" in ROOT.parts)
    if not isolated or not (root / ".git").is_dir():
        raise SelectionError("historical runner execution requires an isolated clone under .scratch")
    spec = importlib.util.spec_from_file_location("r22_round20_successor", root / RUNNER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = root
    module.MIRROR = root / ".scratch/x18-wart-mirror"
    return module


def snapshot(root):
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for number in range(8, 22)
            for path in (root / f"reports/round-{number}").rglob("*")
            if path.is_file() and "__pycache__" not in path.parts}


def selftest(root):
    historical = load_round20(root)
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    def code_names(code):
        names = set(code.co_names)
        for constant in code.co_consts:
            if isinstance(constant, type(code)):
                names.update(code_names(constant))
        return names

    check("historical-runner-has-mtime-lookup", "st_mtime" in code_names(historical.measure_d.__code__))
    with tempfile.TemporaryDirectory(prefix="r22-tie-break-", dir=root / ".scratch") as temporary:
        fixture = Path(temporary)

        def put(relative, data):
            path = fixture / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        tree = ast.parse(Path(historical.__file__).read_bytes())
        old_rank = next(node for node in ast.walk(tree)
                        if isinstance(node, ast.FunctionDef) and node.name == "audit_rank")
        namespace = {"ROOT": fixture, "re": re}
        exec(compile(ast.Module(body=[old_rank], type_ignores=[]), historical.__file__, "exec"), namespace)
        put("audit-a.md", b"# Contract audit v3\nkeyed build 16\nVerdict: PASS\n")
        put("audit-b.md", b"# Contract audit v3\nkeyed build 16\nVerdict: FAIL\n")
        put("audit-new.md", b"# Contract audit v3\nkeyed build 17\nVerdict: FAIL\n")
        put("packet-v3-16.md", b"# Handoff packet v3\nkeyed build 16\nlinks=102/102; contract audit\n")
        put("packet.md", b"# Handoff packet\nv3 live assembly\nlinks=105/105\n")
        put(BASELINE, json.dumps({"packet_sha256": candidate_rank(fixture, "packet.md")[1]}).encode())
        tied = ["audit-a.md", "audit-b.md"]
        expected = max(tied, key=lambda name: hashlib.sha256((fixture / name).read_bytes()).hexdigest())
        historical_choices = []
        for index, order in enumerate((tied, list(reversed(tied)))):
            for offset, name in enumerate(order):
                os.utime(fixture / name, ns=(1_000_000_000, (offset + 1) * 1_000_000_000))
            historical_choices.append(max(order, key=namespace["audit_rank"]))
            chosen = select_candidate(fixture, order, "audit")
            check(f"same-build-sha256-order-{index}", chosen == expected, selected=chosen)
        check("historical-rule-reproduces-mtime-drift", len(set(historical_choices)) == 2,
              selected=historical_choices)
        check("numeric-build-outranks-sha-and-verdict",
              select_candidate(fixture, [*tied, "audit-new.md"], "audit") == "audit-new.md")
        put("packet-v3-9.md", b"# Handoff packet v3\nkeyed build 9\n")
        put("packet-v3-10.md", b"# Handoff packet v3\nkeyed build 10\n")
        check("numeric-build-10-over-9",
              candidate_rank(fixture, "packet-v3-10.md") > candidate_rank(fixture, "packet-v3-9.md"))
        put("unkeyed-v3.md", b"# Contract audit v3\nround 999, date 2026-10-18\n")
        check("unrelated-version-round-date-not-build", candidate_rank(fixture, "unkeyed-v3.md")[0] == -1)
        put("duplicate.md", (fixture / "audit-a.md").read_bytes())
        duplicates = ["duplicate.md", "audit-a.md"]
        check("identical-content-order-independent",
              select_candidate(fixture, duplicates, "audit") == select_candidate(fixture, duplicates[::-1], "audit"))
        check("packet-prose-not-audit-role",
              select_candidate(fixture, ["packet-v3-16.md", "audit-a.md"], "audit") == "audit-a.md")
        check("empty-audit-set-is-not-a-pass", select_candidate(fixture, [], "audit") is None)
        packets = ["packet-v3-16.md", "packet.md"]
        for index, order in enumerate((packets, packets[::-1])):
            for offset, name in enumerate(order):
                os.utime(fixture / name, ns=(1_000_000_000, (offset + 1) * 1_000_000_000))
            selected = select_candidate(fixture, order, "packet")
            check(f"102-vs-105-baseline-binding-{index}", selected == "packet.md", selected=selected)
        put(BASELINE, json.dumps({"packet_sha256": "0" * 64}).encode())
        try:
            select_candidate(fixture, packets, "packet")
            refused = False
        except SelectionError:
            refused = True
        check("unmatched-packet-pin-refused", refused)
        put(BASELINE, b'{"packet_sha256": null}')
        try:
            select_candidate(fixture, packets, "packet")
            refused = False
        except SelectionError:
            refused = True
        check("malformed-packet-pin-refused", refused)
        try:
            candidate_rank(fixture, "missing.md")
            refused = False
        except SelectionError:
            refused = True
        check("unreadable-candidate-refused", refused)
        try:
            candidate_rank(fixture, "../outside.md")
            refused = False
        except SelectionError:
            refused = True
        check("outside-candidate-refused", refused)
        failed_audit = "# contract audit\nDate: 2026-10-18. command: python3 x\nVerdict: FAIL\n"
        check("failing-audit-still-fails", historical.contract_audit_verdict(failed_audit)["classification"] == "fail")
        install_round20_selectors(historical)
        check("adapter-installed-no-mtime-lookup", "st_mtime" not in code_names(historical.measure_d.__code__))

    paths = historical.round20_files()
    packets = historical.discover(paths, r"packet", r"claim_ledger")
    audits = historical.discover(paths, r"contract", r"contract[- ]?v2|contract audit|contract-recheck")
    selected_packet = select_candidate(root, packets, "packet")
    selected_audit = select_candidate(root, audits, "audit")
    check("real-filed-packet-is-baseline-bound", selected_packet == "reports/round-20/handoff/packet.md",
          selected=selected_packet, sha256=candidate_rank(root, selected_packet)[1])
    check("real-filed-audit-role", selected_audit == "reports/round-20/handoff/audit-v3.md",
          selected=selected_audit, rank=candidate_rank(root, selected_audit))
    archive = "reports/round-20/handoff/packet-v3-16.md"
    timestamps = {relative: ((root / relative).stat().st_atime_ns, (root / relative).stat().st_mtime_ns)
                  for relative in (archive, selected_packet, selected_audit)}
    summaries = []
    try:
        for index, order in enumerate(((archive, selected_packet, selected_audit),
                                       (selected_audit, selected_packet, archive))):
            for offset, relative in enumerate(order):
                os.utime(root / relative, ns=(1_000_000_000, (offset + 1) * 1_000_000_000))
            run = historical.subprocess.run(
                [sys.executable, str(root / "tools/exercise-handoff-e2e.py"), "--profile", "v3", "--quiet"],
                cwd=root, env={**os.environ, "TMPDIR": str(root / ".scratch")},
                capture_output=True, text=True, timeout=180)
            selected = select_candidate(root, packets, "packet")
            audit = select_candidate(root, audits, "audit")
            summaries.append(run.stdout.strip())
            check(f"real-v3-reversed-mtime-{index}",
                  run.returncode == 0 and "links=105/105" in run.stdout
                  and selected == selected_packet and audit == selected_audit,
                  exit=run.returncode, command="python3 tools/exercise-handoff-e2e.py --profile v3 --quiet",
                  summary=run.stdout.strip(), stderr=run.stderr[-500:])
        check("real-v3-summary-byte-identical", len(set(summaries)) == 1)
    finally:
        for relative, values in timestamps.items():
            os.utime(root / relative, ns=values)
    return {"controls": controls, "passed": all(item["passed"] for item in controls),
            "passed_controls": sum(item["passed"] for item in controls), "total_controls": len(controls)}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Round-22 deterministic selector successor; frozen rounds stay unchanged.")
    parser.add_argument("--root", type=Path, required=True, help="isolated clone under the lane's .scratch")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--check", action="store_true", help="run the adapted round-20 full check, without receipt writes")
    args = parser.parse_args(argv)
    if not (args.selftest or args.check):
        parser.error("choose --selftest and/or --check")
    root = args.root.resolve()
    os.environ["TMPDIR"] = str(root / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    load_round20(root)
    (root / ".scratch").mkdir(exist_ok=True)
    before = snapshot(root)
    payload = {"date": dt.datetime.now(dt.timezone.utc).isoformat(),
               "command": f"{COMMAND} --root {args.root}" + (" --selftest" if args.selftest else "")
                          + (" --check" if args.check else ""),
               "root": str(root), "source_runner_sha256": RUNNER_SHA256,
               "rank_rule": "highest parsed build, highest full-byte SHA-256; path only for identical content",
               "packet_rule": "baseline packet_sha256 filters candidates before ranking",
               "audit_rule": "contract audit/recheck title; never a verdict-based pass preference"}
    passed = True
    if args.selftest:
        payload["selftest"] = selftest(root)
        passed = payload["selftest"]["passed"]
    if args.check:
        successor = install_round20_selectors(load_round20(root))
        payload["round20_successor"] = successor.validate()
        passed = passed and payload["round20_successor"]["acceptance_checks_passed"]
    after = snapshot(root)
    payload["filed_rounds_8_21_changes"] = sorted(path for path in before.keys() | after.keys()
                                                  if before.get(path) != after.get(path))
    passed = passed and not payload["filed_rounds_8_21_changes"]
    payload["passed"] = passed
    print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
