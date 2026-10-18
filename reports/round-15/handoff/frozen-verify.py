#!/usr/bin/env python3
"""frozen-verify.py — R15-O08 freeze/verify/tamper control for the handoff-v2 baseline.

Owns `reports/round-15/handoff/expected.json` (the frozen baseline for packet v2)
and proves it the way `corpus/knowledge/verification/gate-frozen-run-standard.md`
§5–§6 requires: freeze from measured bytes, digest-first verification, and
fail-closed tamper semantics. This tool is the O-frozen seat's control surface,
not the O02 packet builder — the builder's absence at freeze time is recorded in
`reports/round-15/handoff/frozen.md`.

Usage:
    python3 reports/round-15/handoff/frozen-verify.py --freeze   # measure + write baseline
    python3 reports/round-15/handoff/frozen-verify.py            # verify live tree
    python3 reports/round-15/handoff/frozen-verify.py --baseline PATH --root DIR
    python3 reports/round-15/handoff/frozen-verify.py --selftest # isolated control matrix

What the baseline pins (all measured from live bytes at freeze time, never from
a printed verdict): the packet twins' digests, the shape-gate verdict
(exit + `fields=16/16 glossary-entries=20 findings=0` + whole-stdout digest),
the uncertainty validator's census (claim count, per-status histogram, finding
counts with and without `--require-oq`), the link resolver's counts
(links/resolved/findings), and an `inputs` digest map covering every file the
verification legs read: the packet twins, the gate, the two harness validators,
and every file-backed row of the packet's own `artifact_manifest`.

Exit codes for --verify: 0 pins match; 1 drift (evaluable, expectation
disagrees); 2 could-not-evaluate (baseline missing/malformed/edited, read-set
missing or changed, tool failed). Stable codes `V2F-*`. `--selftest` exits 0
only when every control behaved; 1 otherwise.

Writes: `--freeze` writes only the baseline path. Everything else writes
nothing (selftest works on copies under TMPDIR; the live tree is read-only).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
ROUND = "reports/round-15"
BASELINE_DEFAULT = f"{ROUND}/handoff/expected.json"
PACKET_MD = f"{ROUND}/handoff/packet-v2-05.md"
PACKET_YML = f"{ROUND}/handoff/packet-v2-05.yml"
GATE = "tools/gates/handoff-packet-check.py"
UNC = "tools/harness/packet_uncertainty.py"
LINKS = "tools/harness/packet_links.py"
SCAN_RE = re.compile(
    r"INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)")
LEDGER_RE = re.compile(r'^\s*- claim_id:\s*"?([\w.-]+)"?\s*$')
STATUS_RE = re.compile(r'^\s*status:\s*"?(supported|partial|unresolved)"?\s*$')
ARTIFACT_RE = re.compile(r'^\s*- artifact_id:\s*"?([\w.-]+)"?\s*$')
PATH_RE = re.compile(r'^\s*path:\s*"([^"]+)"\s*$')
SHA_RE = re.compile(r'^\s*sha256:\s*"([0-9a-f]{64})"\s*$')

EXIT_PASS = 0
EXIT_DRIFT = 1
EXIT_UNEVALUABLE = 2


class Failure(Exception):
    def __init__(self, code, detail):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    return sha256_bytes(Path(path).read_bytes())


def run_tool(root, argv, timeout=180):
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        done = subprocess.run(
            [sys.executable, *argv], cwd=str(root), stdin=subprocess.DEVNULL,
            capture_output=True, timeout=timeout, env=env)
    except subprocess.TimeoutExpired as exc:
        raise Failure("V2F-DATA", f"timeout after {timeout:g}s: {argv[0]}") from exc
    except OSError as exc:
        raise Failure("V2F-DATA", f"could not start {argv[0]}: {exc}") from exc
    return done


def parse_json_stdout(done, what):
    try:
        return json.loads(done.stdout.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise Failure(
            "V2F-DATA",
            f"{what}: stdout is not one JSON document ({exc}); "
            f"tail={done.stdout.decode('utf-8', 'replace')[-200:]!r}") from exc


def block_lines(text, header):
    """Lines of the named top-level block in the line-oriented dialect."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.rstrip() == header:
            start = index + 1
            break
    if start is None:
        raise Failure("V2F-DATA", f"packet yml has no {header!r} block")
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index] and not lines[index][0].isspace() and lines[index].rstrip() != header:
            end = index
            break
    return lines[start:end]


def census_claims(yml_text):
    """Independent census: ledger rows and per-status counts, from the yml twin."""
    claims, current = [], None
    for line in block_lines(yml_text, "claim_ledger:"):
        row = LEDGER_RE.match(line)
        if row:
            current = {"id": row.group(1), "status": None}
            claims.append(current)
            continue
        status = STATUS_RE.match(line)
        if status and current is not None and current["status"] is None:
            current["status"] = status.group(1)
    missing = [claim["id"] for claim in claims if claim["status"] is None]
    if missing:
        raise Failure("V2F-DATA", f"claims without a status token: {missing[:3]}")
    histogram = {}
    for claim in claims:
        histogram[claim["status"]] = histogram.get(claim["status"], 0) + 1
    return {"claims": len(claims), "statuses": histogram}


def manifest_inputs(yml_text):
    """File-backed rows of the packet's artifact_manifest: path -> pinned sha256."""
    inputs, row_id, row_path, row_sha = {}, None, None, None
    rows = 0

    def flush():
        nonlocal row_id, row_path, row_sha, rows
        if row_id is not None:
            rows += 1
            if row_path is not None and row_sha is not None:
                if row_path in inputs and inputs[row_path] != row_sha:
                    raise Failure("V2F-DATA",
                                  f"manifest pins {row_path} twice with different digests")
                inputs[row_path] = row_sha
        row_id, row_path, row_sha = None, None, None

    for line in block_lines(yml_text, "artifact_manifest:"):
        artifact = ARTIFACT_RE.match(line)
        if artifact:
            flush()
            row_id = artifact.group(1)
            continue
        path = PATH_RE.match(line)
        if path and row_id is not None:
            row_path = path.group(1)
            continue
        sha = SHA_RE.match(line)
        if sha and row_id is not None:
            row_sha = sha.group(1)
    flush()
    return inputs, rows


def measure(root):
    """Every number the baseline pins, measured from live bytes and tool runs."""
    packet_md, packet_yml = root / PACKET_MD, root / PACKET_YML
    for path in (packet_md, packet_yml):
        if not path.is_file():
            raise Failure("V2F-ARTIFACT", f"packet twin missing: {path}")
    yml_text = packet_yml.read_text(encoding="utf-8")
    census = census_claims(yml_text)
    manifest_pins, manifest_rows = manifest_inputs(yml_text)

    gate = run_tool(root, [GATE, PACKET_MD])
    scan = SCAN_RE.search(gate.stdout.decode("utf-8", "replace"))
    if scan is None:
        raise Failure(
            "V2F-DATA",
            f"gate stdout has no scan line; exit={gate.returncode} "
            f"tail={gate.stdout.decode('utf-8', 'replace')[-200:]!r}")

    unc = parse_json_stdout(run_tool(root, [UNC, "--packet", PACKET_YML, "--json"]),
                            "packet_uncertainty --json")
    unc_oq = parse_json_stdout(
        run_tool(root, [UNC, "--packet", PACKET_YML, "--require-oq", "--json"]),
        "packet_uncertainty --require-oq --json")
    links = parse_json_stdout(
        run_tool(root, [LINKS, "--packet", PACKET_YML, "--repo-root", str(root), "--json"]),
        "packet_links --json")

    before = {relative: sha256_file(root / relative)
              for relative in sorted({PACKET_MD, PACKET_YML, GATE, UNC, LINKS,
                                      *manifest_pins})}
    return {
        "packet_id": re.search(r'^packet_id:\s*"?([^"\n]+)"?\s*$',
                               yml_text, re.M).group(1).strip(),
        "packet_sha256": before[PACKET_MD],
        "packet_yml_sha256": before[PACKET_YML],
        "gate": {"argv": [GATE, PACKET_MD],
                 "exit": gate.returncode,
                 "fields": f"{scan.group(1)}/{scan.group(2)}",
                 "glossary_entries": int(scan.group(3)),
                 "findings": int(scan.group(4)),
                 "stdout_sha256": sha256_bytes(gate.stdout)},
        "census": census,
        "uncertainty": {"exit": 0, "claims": unc.get("claims"),
                        "findings": len(unc.get("findings", [])),
                        "require_oq_findings": len(unc_oq.get("findings", []))},
        "links": {"exit": 0, "links": links.get("links_checked"),
                  "resolved": links.get("resolved"),
                  "findings": len(links.get("findings", []))},
        "manifest_rows": manifest_rows,
        "inputs": before,
    }


def baseline_digest(payload):
    body = dict(payload)
    body.pop("baseline_digest", None)
    text = json.dumps(body, ensure_ascii=False, sort_keys=True, indent=1)
    return sha256_bytes(text.encode("utf-8"))


def cmd_freeze(args):
    root = Path(args.root).resolve() if args.root else ROOT
    first = measure(root)
    second = measure(root)
    if first != second:
        changed = [key for key in first["inputs"]
                   if first["inputs"][key] != second["inputs"].get(key)]
        raise Failure("V2F-DIGEST",
                      f"tree moved while measuring; re-run on a settled tree "
                      f"(moved: {', '.join(sorted(changed)[:3])})")
    payload = {
        "schema": "kotodama-frozen-run-v1",
        "profile": "kotodama-handoff-v2/1",
        "declared_expectation": "exit 0 / findings [] / census+links counts fixed "
                                "before verification; hashes measured from bytes, "
                                "never copied from a printed verdict",
        "expected_exit": first["gate"]["exit"],
        "expected_scan": {"fields": first["gate"]["fields"],
                          "glossary_entries": first["gate"]["glossary_entries"],
                          "findings": first["gate"]["findings"]},
        "gate_stdout_sha256": first["gate"]["stdout_sha256"],
        "packet_id": first["packet_id"],
        "packet_sha256": first["packet_sha256"],
        "packet_yml_sha256": first["packet_yml_sha256"],
        "census": first["census"],
        "uncertainty": first["uncertainty"],
        "links": first["links"],
        "manifest_rows": first["manifest_rows"],
        "inputs": first["inputs"],
        "frozen_at": datetime.date.today().isoformat(),
        "frozen_by": "R15-O08 reports/round-15/handoff/frozen-verify.py --freeze",
        "limits": "pins computational inputs only; not lore acceptance, not canon, "
                  "not completion of the round arc; documentation surfaces excluded",
    }
    payload["baseline_digest"] = baseline_digest(payload)
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=1) + "\n"
    target = Path(args.baseline) if args.baseline else root / BASELINE_DEFAULT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(f"froze {target.relative_to(root) if target.is_relative_to(root) else target}")
    print(f"packet md {first['packet_sha256'][:12]}… yml {first['packet_yml_sha256'][:12]}… "
          f"gate exit {first['gate']['exit']} fields={first['gate']['fields']} "
          f"glossary={first['gate']['glossary_entries']} findings={first['gate']['findings']}")
    print(f"inputs: {len(first['inputs'])} pinned; manifest rows {first['manifest_rows']}; "
          f"census {first['census']['statuses']}; links {first['links']['resolved']}/"
          f"{first['links']['links']}")
    return EXIT_PASS


def load_baseline(path):
    try:
        raw = Path(path).read_bytes()
    except OSError as exc:
        raise Failure("V2F-BASELINE", f"baseline unreadable: {exc}") from exc
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise Failure("V2F-BASELINE", f"baseline is not valid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise Failure("V2F-BASELINE", "baseline is not a JSON object")
    if payload.get("baseline_digest") != baseline_digest(payload):
        raise Failure(
            "V2F-BASELINE",
            "baseline integrity digest mismatch — the baseline was edited without re-freezing")
    for key in ("packet_sha256", "expected_scan", "gate_stdout_sha256",
                "census", "uncertainty", "links", "inputs"):
        if key not in payload:
            raise Failure("V2F-BASELINE", f"baseline is missing {key!r}")
    return payload


def cmd_verify(args):
    root = Path(args.root).resolve() if args.root else ROOT
    payload = load_baseline(Path(args.baseline) if args.baseline else root / BASELINE_DEFAULT)

    drifted, missing = [], []
    for relative, pinned in sorted(payload["inputs"].items()):
        path = root / relative
        if not path.is_file():
            missing.append(relative)
            continue
        if sha256_file(path) != pinned:
            drifted.append(relative)
    if missing:
        raise Failure("V2F-ARTIFACT",
                      f"{len(missing)} pinned file(s) missing: {', '.join(missing[:3])}")
    if drifted:
        raise Failure("V2F-DIGEST",
                      f"{len(drifted)} pinned file(s) changed since the freeze: "
                      f"{', '.join(drifted[:3])}")

    packet_md = root / PACKET_MD
    live_packet = sha256_file(packet_md)
    if live_packet != payload["packet_sha256"]:
        raise Failure("V2F-PIN",
                      f"baseline packet_sha256 {payload['packet_sha256'][:12]}… != live "
                      f"{live_packet[:12]}… ({PACKET_MD})")

    gate = run_tool(root, [GATE, PACKET_MD])
    scan = SCAN_RE.search(gate.stdout.decode("utf-8", "replace"))
    expected = payload["expected_scan"]
    if gate.returncode != payload.get("expected_exit", 0):
        raise Failure("V2F-GATE",
                      f"gate exited {gate.returncode}, expected "
                      f"{payload.get('expected_exit', 0)}")
    if scan is None:
        raise Failure("V2F-DATA", "gate stdout has no scan line at verify time")
    observed = {"fields": f"{scan.group(1)}/{scan.group(2)}",
                "glossary_entries": int(scan.group(3)),
                "findings": int(scan.group(4))}
    if observed != expected:
        raise Failure("V2F-GATE",
                      f"scan {observed} != expected {expected}")
    if sha256_bytes(gate.stdout) != payload["gate_stdout_sha256"]:
        raise Failure("V2F-GATE", "gate stdout bytes differ from the frozen stdout pin")

    census = census_claims((root / PACKET_YML).read_text(encoding="utf-8"))
    if census != payload["census"]:
        raise Failure("V2F-COUNT", f"census {census} != expected {payload['census']}")

    unc = parse_json_stdout(run_tool(root, [UNC, "--packet", PACKET_YML, "--json"]),
                            "packet_uncertainty --json")
    unc_oq = parse_json_stdout(
        run_tool(root, [UNC, "--packet", PACKET_YML, "--require-oq", "--json"]),
        "packet_uncertainty --require-oq --json")
    observed_unc = {"exit": 0, "claims": unc.get("claims"),
                    "findings": len(unc.get("findings", [])),
                    "require_oq_findings": len(unc_oq.get("findings", []))}
    if observed_unc != payload["uncertainty"]:
        raise Failure("V2F-COUNT",
                      f"uncertainty receipt {observed_unc} != expected {payload['uncertainty']}")

    links = parse_json_stdout(
        run_tool(root, [LINKS, "--packet", PACKET_YML, "--repo-root", str(root), "--json"]),
        "packet_links --json")
    observed_links = {"exit": 0, "links": links.get("links_checked"),
                      "resolved": links.get("resolved"),
                      "findings": len(links.get("findings", []))}
    if observed_links != payload["links"]:
        raise Failure("V2F-COUNT",
                      f"links receipt {observed_links} != expected {payload['links']}")

    print(f"frozen-v2: exit=0 fields={observed['fields']} "
          f"glossary={observed['glossary_entries']}/{observed['glossary_entries']} "
          f"findings={observed['findings']} "
          f"claims={census['claims']}/{payload['census']['claims']} "
          f"statuses={census['statuses']} "
          f"links={observed_links['resolved']}/{observed_links['links']} "
          f"packet_sha256={live_packet[:12]}…")
    return EXIT_PASS


# ------------------------------------------------------------------ selftest

def copy_tree(source, destination):
    shutil.rmtree(destination, ignore_errors=True)
    destination.mkdir(parents=True)
    for name in ("tools", "examples", "corpus", "reports"):
        shutil.copytree(source / name, destination / name,
                        ignore=shutil.ignore_patterns("__pycache__"))


def selftest():
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    scratch = Path(tempfile.mkdtemp(prefix="frozen-verify-selftest-"))
    try:
        baseline = scratch / "baseline.json"
        pristine = scratch / "pristine"
        copy_tree(ROOT, pristine)
        frozen = subprocess.run(
            [sys.executable,
             str(pristine / "reports" / "round-15" / "handoff" / "frozen-verify.py"),
             "--freeze", "--baseline", str(baseline)], cwd=str(pristine),
            capture_output=True, text=True, timeout=600)
        check("freeze: exit 0", frozen.returncode == 0,
              (frozen.stdout + frozen.stderr)[-300:])

        def scenario(name, mutate, want_exit, want_code):
            tree = scratch / name
            copy_tree(pristine, tree)
            shutil.copyfile(baseline, tree / BASELINE_DEFAULT)
            mutate(tree)
            done = subprocess.run(
                [sys.executable,
                 str(tree / "reports" / "round-15" / "handoff" / "frozen-verify.py")],
                cwd=str(tree), capture_output=True, text=True, timeout=600)
            output = done.stdout + done.stderr
            check(f"{name}: exit {want_exit}", done.returncode == want_exit,
                  output.strip()[-300:])
            if want_code:
                check(f"{name}: code {want_code}", want_code in output,
                      output.strip()[-200:])

        scenario("s0-positive", lambda tree: None, EXIT_PASS, None)

        def drop_baseline(tree):
            (tree / BASELINE_DEFAULT).unlink()
        scenario("s1-baseline-absent", drop_baseline, EXIT_UNEVALUABLE, "V2F-BASELINE")

        def wreck_baseline(tree):
            (tree / BASELINE_DEFAULT).write_text("{ not json\n", encoding="utf-8")
        scenario("s2-baseline-malformed", wreck_baseline, EXIT_UNEVALUABLE, "V2F-BASELINE")

        def edit_pin(tree):
            path = tree / BASELINE_DEFAULT
            payload = json.loads(path.read_text(encoding="utf-8"))
            payload["packet_sha256"] = "0" * 64
            payload.pop("baseline_digest", None)
            payload["baseline_digest"] = baseline_digest(payload)
            path.write_text(
                json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=1) + "\n",
                encoding="utf-8")
        scenario("s3-pin-edited-resigned", edit_pin, EXIT_DRIFT, "V2F-PIN")

        def drop_read_set(tree):
            victim = None
            for relative in json.loads((tree / BASELINE_DEFAULT)
                                       .read_text(encoding="utf-8"))["inputs"]:
                if relative.startswith("corpus/"):
                    victim = tree / relative
                    break
            victim.unlink()
        scenario("s4-readset-deleted", drop_read_set, EXIT_UNEVALUABLE, "V2F-ARTIFACT")

        def edit_read_set(tree):
            payload = json.loads((tree / BASELINE_DEFAULT).read_text(encoding="utf-8"))
            victim = next(relative for relative in sorted(payload["inputs"])
                          if relative.startswith("examples/"))
            path = tree / victim
            path.write_bytes(path.read_bytes() + b"# drift probe\n")
        scenario("s5-readset-edited", edit_read_set, EXIT_UNEVALUABLE, "V2F-DIGEST")

        def revise_gate(tree):
            path = tree / GATE
            path.write_bytes(path.read_bytes() + b"# revision probe\n")
        scenario("s6-gate-revised", revise_gate, EXIT_UNEVALUABLE, "V2F-DIGEST")

        def revise_helper(tree):
            path = tree / LINKS
            path.write_bytes(path.read_bytes() + b"# revision probe\n")
        scenario("s7-helper-revised", revise_helper, EXIT_UNEVALUABLE, "V2F-DIGEST")

        def edit_packet_md(tree):
            path = tree / PACKET_MD
            path.write_bytes(path.read_bytes() + b"<!-- drift probe -->\n")
        scenario("s8-packet-edited", edit_packet_md, EXIT_UNEVALUABLE, "V2F-DIGEST")

        def edit_scan_expectation(tree):
            path = tree / BASELINE_DEFAULT
            payload = json.loads(path.read_text(encoding="utf-8"))
            payload["expected_scan"]["findings"] = 1
            payload.pop("baseline_digest", None)
            payload["baseline_digest"] = baseline_digest(payload)
            path.write_text(
                json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=1) + "\n",
                encoding="utf-8")
        scenario("s9-scan-expectation-edited", edit_scan_expectation,
                 EXIT_DRIFT, "V2F-GATE")

        def edit_census_expectation(tree):
            path = tree / BASELINE_DEFAULT
            payload = json.loads(path.read_text(encoding="utf-8"))
            statuses = payload["census"]["statuses"]
            first = next(iter(statuses))
            statuses[first] += 1
            payload.pop("baseline_digest", None)
            payload["baseline_digest"] = baseline_digest(payload)
            path.write_text(
                json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=1) + "\n",
                encoding="utf-8")
        scenario("s10-census-expectation-edited", edit_census_expectation,
                 EXIT_DRIFT, "V2F-COUNT")

        def run_twice(tree):
            outs = []
            for _ in range(2):
                done = subprocess.run(
                    [sys.executable,
                     str(tree / "reports" / "round-15" / "handoff" / "frozen-verify.py")],
                    cwd=str(tree), capture_output=True, text=True, timeout=600)
                outs.append(done.stdout)
            check("s11-verify-deterministic-stdout", outs[0] == outs[1] and outs[0],
                  f"run1={outs[0][-120:]!r} run2={outs[1][-120:]!r}")
        scenario("s11-verify-deterministic", run_twice, EXIT_PASS, None)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)

    passed = 0
    for name, ok, detail in checks:
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'} {name}" + ("" if ok else f": {detail}"))
    print(f"selftest: {passed}/{len(checks)} checks passed")
    return EXIT_PASS if passed == len(checks) else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="frozen-verify.py",
        description="R15-O08 freeze/verify/tamper control for the handoff-v2 baseline")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--freeze", action="store_true",
                       help="measure the live tree and (re)write the baseline")
    modes.add_argument("--selftest", action="store_true",
                       help="run the isolated control matrix and exit")
    parser.add_argument("--baseline", default=None, help="baseline path override")
    parser.add_argument("--root", default=None, help="repo root override")
    args = parser.parse_args(argv)
    try:
        if args.selftest:
            return selftest()
        if args.freeze:
            return cmd_freeze(args)
        return cmd_verify(args)
    except Failure as failure:
        print(f"{failure.code}: {failure.detail}", file=sys.stderr)
        return EXIT_UNEVALUABLE if failure.code in (
            "V2F-BASELINE", "V2F-ARTIFACT", "V2F-DIGEST", "V2F-DATA") else EXIT_DRIFT


if __name__ == "__main__":
    sys.exit(main())
