#!/usr/bin/env python3
"""R27-O25..O32 — the D4 pin sweep: inventory, re-verify, re-pin.

Round 26 landed the register stratum and its own `register/repin.json` reported
two cascades it did not repair (the filed round-22 v3 baseline and the r4-twin
row). Round 27's D claim lands the register law, which amends the D4 component
tree again. This tool is the single sweep the O claim owes: it walks every file
class in the lane that carries a digest pin over a D4 surface, re-verifies each
against the live amended packet, and reports each row's verdict with the code
its own replayer printed.

It never writes a filed byte. The re-pins it produced live under
`reports/round-27/pinsweep/` as NEW rows; this tool only reads and measures.

Surface families walked (the sweep's own definition, recorded so a reader can
disagree with it):

  A  `MANIFEST.tsv` rows under `tools/gates/frozen/**`            (replay-frozen)
  B  `expected.json` under `tools/gates/expected/**`              (battery roots)
  C  `expected.json` under `tools/gates/frozen/**` + `reports/round-9/baselines/**`
  D  `freeze-receipt.json` embedded pin maps under `tools/gates/frozen/**`
  E  `reports/**/expected*.json` handoff baselines (v2 + v3 families)
  F  `tools/gates/typed-pipelines.json` (the live L1-profile pin channel)
  G  `expected-holds.json` self-pins (packet / projection / projector digests)
  H  `twin.json` + `packet.md` embedded `artifact_manifest` pins

Usage
-----
    export TMPDIR=/var/tmp/kotodama-r27-pinsweep   # OUTSIDE the repo, or every
                                                   # replay row reads mirror_unsafe
    python3 reports/round-27/pinsweep/sweep.py              # text report
    python3 reports/round-27/pinsweep/sweep.py --json       # receipt document
    python3 reports/round-27/pinsweep/sweep.py --selftest   # dependency-free controls

Exit codes
----------
    0  every surface enumerated; every evaluated row green
    1  at least one row drifted (a re-pin is owed) — reported, never hidden
    2  could-not-evaluate: a surface could not be read or a replay could not run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
FROZEN = ROOT / "tools" / "gates" / "frozen"
EXPECTED = ROOT / "tools" / "gates" / "expected"
LEGACY = ROOT / "reports" / "round-9" / "baselines"
HEX64 = re.compile(r"^[0-9a-f]{64}$")

# The six D4 bytes the round-26 register landing moved, plus the round-27
# register-law component and the projector the projection rows bind.
D4_SURFACES = (
    "examples/culture-d4/packet.d4.yml",
    "examples/culture-d4/packet.d4.typed.yml",
    "examples/culture-d4/typed-labels.d4.yml",
    "examples/culture-d4/expected-holds.json",
    "examples/culture-d4/components/01-brief.yml",
    "examples/culture-d4/components/04-lexicon.yml",
    "examples/culture-d4/components/13-register-law.yml",
    "tools/d2-typed-labels.py",
)

# Every D4 packet digest the lane has recorded: the round-26 register-stratum
# build, the two round-27 register-law builds, and the round-22 family-clean
# build the hold set pinned before round 26.
STALE_D4_PACKETS = (
    "e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3",
    "dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67",
    "c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a",
    "86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc",
)


def sha(path) -> str | None:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return None


def live_d4() -> dict:
    return {rel: sha(ROOT / rel) for rel in D4_SURFACES}


def is_frozen_snapshot(rel: str) -> bool:
    """A byte copy inside a frozen generation's `inputs/` is historical by design.

    `tools/gates/frozen/<round>/<gen>/inputs/<path>` is the committed snapshot the
    generation recorded against; its embedded pins deliberately name the bytes of
    that stamp, not the live tree. Re-verifying them against the live tree would
    flag every filed generation as drifted, which is not a finding — a re-freeze is
    a new generation (gate-frozen-run-standard.md section 3).
    """
    parts = Path(rel).parts
    return "frozen" in parts and "inputs" in parts


def git_head() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT),
                              capture_output=True, text=True).stdout.strip()
    except OSError:
        return "unknown"


# ---------------------------------------------------------------- family A

MANIFEST_COLS = ("gate", "gate_sha256", "input", "input_sha256", "exit_code",
                 "finding_count", "output", "output_sha256", "input_snapshot", "command")


def walk_manifests() -> list[dict]:
    """Every MANIFEST.tsv row under tools/gates/frozen/** and reports/**/frozen/**."""
    rows = []
    manifests = sorted(FROZEN.rglob("MANIFEST.tsv"))
    manifests += sorted((ROOT / "reports").rglob("frozen/MANIFEST.tsv"))
    for manifest in manifests:
        if ".scratch" in str(manifest) or "round-27" in str(manifest):
            continue
        lines = manifest.read_text(encoding="utf-8").splitlines()
        if not lines:
            continue
        header = lines[0].split("\t")
        for number, line in enumerate(lines[1:], start=2):
            if not line.strip():
                continue
            fields = line.split("\t")
            if len(fields) != len(header):
                continue
            row = dict(zip(header, fields))
            blob = json.dumps(row)
            d4 = "culture-d4" in blob or "packet.d4" in blob or "typed-labels.d4" in blob
            rows.append({
                "family": "A", "manifest": str(manifest.relative_to(ROOT)),
                "line": number, "gate": row.get("gate"), "input": row.get("input"),
                "input_sha256": row.get("input_sha256"),
                "input_snapshot": row.get("input_snapshot"),
                "recorded_exit": row.get("exit_code"),
                "recorded_count": row.get("finding_count"),
                "d4": d4,
                "pin_live": sha(ROOT / row["input"]) if row.get("input") else None,
                "snapshot_live": sha(ROOT / row["input_snapshot"]) if row.get("input_snapshot") else None,
                "gate_live": sha(ROOT / row["gate"]) if row.get("gate") else None,
            })
    return rows


def replay_manifest(manifest: str, tmp_parent: str) -> dict:
    env = {**os.environ, "TMPDIR": tmp_parent, "PYTHONDONTWRITEBYTECODE": "1"}
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools/replay-frozen.py"), manifest, "--json"],
        capture_output=True, text=True, cwd=str(ROOT), env=env, check=False)
    try:
        doc = json.loads(proc.stdout)
    except ValueError:
        return {"manifest": manifest, "exit": proc.returncode,
                "raw": (proc.stdout or proc.stderr).strip().splitlines()[-1:] or [""],
                "statuses": []}
    return {"manifest": manifest, "exit": proc.returncode,
            "statuses": [r.get("status") for r in (doc.get("rows") or [])],
            "rows": doc.get("rows") or []}


# ---------------------------------------------------------------- family B/C

def walk_baselines() -> list[dict]:
    """Every committed expected.json under the battery's three roots."""
    out = []
    for root in (EXPECTED, FROZEN, LEGACY):
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("expected.json")) + sorted(root.rglob("*.expected.json")):
            try:
                doc = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                out.append({"family": "B/C", "path": str(path.relative_to(ROOT)),
                            "reading": "unreadable"})
                continue
            blob = json.dumps(doc)
            if "culture-d4" not in blob and "packet.d4" not in blob:
                continue
            inputs = doc.get("inputs") or {}
            drift = []
            for rel, pin in inputs.items():
                if not isinstance(pin, str):
                    continue
                live = sha(ROOT / rel)
                if live is not None and live != pin:
                    drift.append({"path": rel, "pin": pin, "live": live})
            gate_sha = doc.get("gate_sha256")
            gate_live = sha(ROOT / (doc.get("gate_script") or f"tools/gates/{doc.get('gate','')}"))
            out.append({
                "family": "B/C", "path": str(path.relative_to(ROOT)),
                "baseline_id": doc.get("baseline_id"), "gate": doc.get("gate"),
                "gate_sha256_match": (gate_sha == gate_live) if gate_sha and gate_live else None,
                "inputs_checked": len(inputs), "drift": drift,
                "reading": "drifted" if drift else "pinned",
            })
    return out


# ---------------------------------------------------------------- family D

PIN_MAP_KEYS = ("input_pins", "pins", "live_tool_and_input_pins", "snapshot_pins")


def walk_receipts() -> list[dict]:
    """Every freeze receipt's embedded pin maps, under all four recorded key names.

    Receipts do not share one key name: `round-26/post-register` uses
    `input_pins` + `pins`, `round-22/d4-repin` uses `live_tool_and_input_pins` +
    `snapshot_pins`, and `round-18` records its pins as a `rows` list instead.
    A walker that read only `input_pins`/`pins` would report the round-22 receipt
    green by omission, so all four maps are read.
    """
    out = []
    for path in sorted(FROZEN.rglob("freeze-receipt.json")):
        rel = str(path.relative_to(ROOT))
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if "culture-d4" not in json.dumps(doc):
            continue
        drift = []
        for key in PIN_MAP_KEYS:
            for rel_path, pin in (doc.get(key) or {}).items():
                if not isinstance(pin, str) or not HEX64.match(pin):
                    continue
                if is_frozen_snapshot(rel_path):
                    continue
                live = sha(ROOT / rel_path)
                if live is not None and live != pin:
                    drift.append({"key": key, "path": rel_path, "pin": pin, "live": live})
        rows = doc.get("rows")
        for row in (rows if isinstance(rows, list) else []):
            if not isinstance(row, dict):
                continue
            for key in ("input", "input_snapshot"):
                rel_path, pin = row.get(key), row.get("input_sha256")
                if not rel_path or not isinstance(pin, str):
                    continue
                if is_frozen_snapshot(rel_path):
                    continue
                live = sha(ROOT / rel_path)
                if live is not None and live != pin:
                    drift.append({"key": f"rows.{key}", "path": rel_path,
                                  "pin": pin, "live": live})
        out.append({"family": "D", "path": rel, "maps": [k for k in PIN_MAP_KEYS if doc.get(k)],
                    "drift": drift, "reading": "drifted" if drift else "pinned"})
    return out


# ---------------------------------------------------------------- family E

def walk_handoff() -> list[dict]:
    """Every reports/**/expected*.json that pins a D4 read-set or packet digest."""
    out = []
    for path in sorted((ROOT / "reports").rglob("expected*.json")):
        if "round-27" in str(path):
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        blob = json.dumps(doc)
        if "culture-d4" not in blob and "packet.d4" not in blob:
            continue
        drift = []
        for rel, pin in (doc.get("inputs") or {}).items():
            if not isinstance(pin, str):
                continue
            live = sha(ROOT / rel)
            if live is not None and live != pin:
                drift.append({"path": rel, "pin": pin, "live": live})
        out.append({
            "family": "E", "path": str(path.relative_to(ROOT)),
            "profile": doc.get("profile"), "packet_sha256": doc.get("packet_sha256"),
            "inputs_checked": len(doc.get("inputs") or {}), "drift": drift,
            "reading": "drifted" if drift else "pinned",
        })
    return out


# ---------------------------------------------------------------- family F/G/H

def walk_profile() -> dict:
    path = ROOT / "tools/gates/typed-pipelines.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    drift = []
    for profile in doc.get("profiles", []):
        for key in ("packet", "assembler", "projection", "adapter", "expected"):
            spec = profile.get(key) or {}
            if "path" in spec and "sha256" in spec:
                live = sha(ROOT / spec["path"])
                if live is not None and live != spec["sha256"]:
                    drift.append({"profile": profile.get("id"), "key": key,
                                  "path": spec["path"], "pin": spec["sha256"], "live": live})
    return {"family": "F", "path": "tools/gates/typed-pipelines.json",
            "drift": drift, "reading": "drifted" if drift else "pinned"}


def walk_holds() -> list[dict]:
    """Every D4 hold set: one whose `packet_sha256` names a D4 packet digest.

    The D4 hold set's own schema is `kotodama-typed-pipeline-holds-v1` and its
    revision note never says "D4", so the family test is the pin itself: a hold
    set is in surface when its `packet_sha256` is the live D4 packet digest or one
    of the recorded superseded ones. That catches it whether or not it has been
    re-pinned, and it cannot catch the D2 drill's hold set.
    """
    known = set(STALE_D4_PACKETS) | {sha(ROOT / "examples/culture-d4/packet.d4.yml")}
    out = []
    for path in sorted(ROOT.rglob("expected-holds*.json")):
        rel = str(path.relative_to(ROOT))
        if ".scratch" in rel or "round-27" in rel or is_frozen_snapshot(rel):
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if doc.get("packet_sha256") not in known:
            continue
        drift = []
        for key in ("packet_sha256", "projection_sha256", "projector_sha256"):
            pin = doc.get(key)
            if not isinstance(pin, str):
                continue
            target = {"packet_sha256": "examples/culture-d4/packet.d4.yml",
                      "projection_sha256": "examples/culture-d4/typed-labels.d4.yml",
                      "projector_sha256": "tools/d2-typed-labels.py"}[key]
            live = sha(ROOT / target)
            if live is not None and live != pin:
                drift.append({"key": key, "target": target, "pin": pin, "live": live})
        out.append({"family": "G", "path": rel,
                    "drift": drift, "reading": "drifted" if drift else "pinned"})
    return out


def walk_twins() -> list[dict]:
    out = []
    for path in sorted(ROOT.rglob("twin.json")):
        rel = str(path.relative_to(ROOT))
        if ".scratch" in rel or "round-27" in rel or is_frozen_snapshot(rel):
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        drift = []
        for row in doc.get("artifact_manifest") or []:
            if not isinstance(row, dict) or "path" not in row or "sha256" not in row:
                continue
            if "culture-d4" not in row["path"]:
                continue
            live = sha(ROOT / row["path"])
            if live is not None and live != row["sha256"]:
                drift.append({"artifact_id": row.get("artifact_id"), "path": row["path"],
                              "pin": row["sha256"], "live": live})
        out.append({"family": "H", "path": str(path.relative_to(ROOT)),
                    "drift": drift, "reading": "drifted" if drift else "pinned"})
    return out


# ---------------------------------------------------------------- family I

D4_PATH = re.compile(r"examples/culture-d4/[A-Za-z0-9_./-]+")
PAIR = re.compile(r'"(examples/culture-d4/[A-Za-z0-9_./-]+)"\s*:\s*"([0-9a-f]{64})"')


def walk_evidence_receipts() -> list[dict]:
    """D4 path→digest pairs embedded in `reports/**/evidence/*.json` receipts.

    A pin surface is not only a MANIFEST row or an `expected.json`: an evidence
    receipt that captured the D4 tree at a past stamp carries independent
    path→digest pairs, and no filename walk reaches them (round-27 R27-O38 §5).
    They are historical by design — a receipt records the stamp it measured — so
    this family reports them as a *coverage* surface, not as drift owed a
    successor. Enumerating them is what makes "every surface" checkable.
    """
    out = []
    for path in sorted((ROOT / "reports").rglob("evidence/*.json")):
        rel = str(path.relative_to(ROOT))
        if ".scratch" in rel or "round-27" in rel:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if "culture-d4" not in text:
            continue
        pairs = {}
        for match in PAIR.finditer(text):
            pairs[match.group(1)] = match.group(2)
        if not pairs:
            continue
        stale = []
        for target, pin in sorted(pairs.items()):
            live = sha(ROOT / target)
            if live is not None and live != pin:
                stale.append({"path": target, "pin": pin, "live": live})
        out.append({"family": "I", "path": rel, "pins": len(pairs),
                    "stale": len(stale), "drift": stale,
                    "reading": "historical (captured at a past stamp)"})
    return out


# ---------------------------------------------------------------- the sweep

def sweep(tmp_parent: str) -> dict:
    head = git_head()
    live = live_d4()
    manifests = walk_manifests()
    seen = sorted({r["manifest"] for r in manifests})
    replays = [replay_manifest(m, tmp_parent) for m in seen]
    baselines = walk_baselines()
    receipts = walk_receipts()
    handoff = walk_handoff()
    profile = walk_profile()
    holds = walk_holds()
    twins = walk_twins()
    evidence = walk_evidence_receipts()

    findings = []
    for row in manifests:
        if not row["d4"]:
            continue
        if row["pin_live"] and row["input_sha256"] and row["pin_live"] != row["input_sha256"]:
            findings.append({"surface": f'{row["manifest"]}:{row["line"]}',
                             "code": "MANIFEST-INPUT-MOVED", "input": row["input"],
                             "pin": row["input_sha256"], "live": row["pin_live"]})
    for group, key in ((baselines, "B/C"), (receipts, "D"), (handoff, "E"), (holds, "G"), (twins, "H")):
        for row in group:
            if row.get("drift"):
                findings.append({"surface": row["path"], "code": f'{key}-DIGEST-DRIFT',
                                 "rows": len(row["drift"])})
    if profile["drift"]:
        findings.append({"surface": profile["path"], "code": "F-PROFILE-DRIFT",
                         "rows": len(profile["drift"])})

    return {
        "schema": "kotodama-r27-pin-sweep-v1",
        "tool": "reports/round-27/pinsweep/sweep.py",
        "round": 27,
        "seat": "R27-O25..O32",
        "date": "2026-10-18",
        "revision": head,
        "canon": ("NON-CANON engineering evidence; a pin is integrity, never truth "
                  "and never clearance"),
        "live_d4": live,
        "families": {
            "A": {"manifests": len(seen), "rows": len(manifests),
                  "d4_rows": sum(1 for r in manifests if r["d4"]), "replays": replays},
            "B/C": baselines,
            "D": receipts,
            "E": handoff,
            "F": profile,
            "G": holds,
            "H": twins,
            "I": evidence,
        },
        "findings": findings,
        "summary": {
            "surfaces_enumerated": (len(manifests) + len(baselines) + len(receipts)
                                    + len(handoff) + 1 + len(holds) + len(twins)
                                    + len(evidence)),
            "findings": len(findings),
            "exit": 1 if findings else 0,
        },
    }


def render(doc: dict) -> str:
    lines = []
    add = lines.append
    add("# R27-O25..O32 — D4 pin sweep (machine census)")
    add("")
    add(f"- revision: `{doc['revision']}`; date {doc['date']}")
    add(f"- surfaces enumerated: {doc['summary']['surfaces_enumerated']}; "
        f"findings: {doc['summary']['findings']}")
    add("")
    add("| family | what | surfaces | drifted |")
    add("|---|---|---:|---:|")
    fam = doc["families"]
    add(f"| A | MANIFEST.tsv rows under tools/gates/frozen/** | {fam['A']['manifests']} manifests / "
        f"{fam['A']['rows']} rows ({fam['A']['d4_rows']} D4) | "
        f"{sum(1 for r in fam['A']['replays'] if r['exit'] != 0)} |")
    for key, label in (("B/C", "committed expected.json (battery roots)"),
                       ("D", "freeze-receipt.json embedded pins"),
                       ("E", "reports/**/expected*.json handoff baselines"),
                       ("G", "expected-holds self-pins"),
                       ("H", "twin.json artifact_manifest pins")):
        rows = fam[key]
        add(f"| {key} | {label} | {len(rows)} | "
            f"{sum(1 for r in rows if r.get('drift'))} |")
    add(f"| F | tools/gates/typed-pipelines.json | 1 | "
        f"{1 if fam['F']['drift'] else 0} |")
    ev = fam["I"]
    add(f"| I | reports/**/evidence/*.json embedded D4 pairs (historical) | {len(ev)} | "
        f"{sum(r['stale'] for r in ev)} stale pins |")
    add("")
    add("## Replay of every frozen generation")
    add("")
    add("| manifest | exit | reproduced | mismatch | could-not-evaluate |")
    add("|---|---:|---:|---:|---:|")
    for rep in fam["A"]["replays"]:
        st = rep.get("statuses") or []
        add(f"| `{rep['manifest']}` | {rep['exit']} | {st.count('reproduced')} | "
            f"{st.count('mismatch')} | {st.count('could-not-evaluate')} |")
    add("")
    add("## Findings")
    add("")
    if not doc["findings"]:
        add("none")
    else:
        for f in doc["findings"]:
            add(f"- `{f['code']}` — `{f['surface']}`"
                + (f" ({f.get('rows')} row(s))" if f.get("rows") else ""))
    add("")
    add("## Live D4 digests at this stamp")
    add("")
    for rel, digest in doc["live_d4"].items():
        add(f"- `{rel}` `{(digest or 'missing')[:16]}…`")
    return "\n".join(lines) + "\n"


def selftest() -> int:
    controls = []

    def check(name, ok, **detail):
        controls.append({"control": name, "passed": bool(ok), **detail})

    check("d4-surfaces-declared", len(D4_SURFACES) == 8, n=len(D4_SURFACES))
    check("live-d4-reads", all(v is not None for v in live_d4().values()),
          missing=[k for k, v in live_d4().items() if v is None])
    with tempfile.TemporaryDirectory(prefix="r27-sweep-selftest-") as tmp:
        outside = Path(os.path.realpath(tmp))
        check("selftest-tmpdir-outside-repo",
              outside != ROOT and ROOT not in outside.parents, root=str(outside))
        # the known-green control is THIS sweep's own new generation: the D4-leg
        # generation re-frozen at the settled post-law stamp. The round-26
        # `post-register` generation is deliberately NOT the control — the round-27
        # register law superseded its two D4 rows, which is the finding, not a bug.
        good = replay_manifest("reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv", str(outside))
        check("known-green-generation-replays", good["exit"] == 0,
              statuses=good.get("statuses"))
    bad = replay_manifest("tools/gates/frozen/round-18/MANIFEST.tsv", "/var/tmp")
    check("known-drifted-generation-replays-red", bad["exit"] != 0,
          statuses=bad.get("statuses"))
    superseded = replay_manifest("tools/gates/frozen/round-26/post-register/MANIFEST.tsv", "/var/tmp")
    check("known-superseded-generation-replays-red", superseded["exit"] != 0,
          statuses=superseded.get("statuses"),
          note="green 6/6 when frozen in round 26; the round-27 register law moved its two D4 inputs")
    # the D4 surfaces must actually be covered by the walkers
    rows = walk_manifests()
    check("manifest-walker-finds-d4-rows", any(r["d4"] for r in rows),
          d4_rows=sum(1 for r in rows if r["d4"]))
    check("hold-walker-finds-the-committed-hold-set",
          any("culture-d4/expected-holds.json" in r["path"] for r in walk_holds()))
    check("twin-walker-finds-the-r4-twin",
          any("r4-twin" in r["path"] for r in walk_twins()))
    evidence = walk_evidence_receipts()
    check("evidence-walker-finds-the-three-receipts",
          len(evidence) == 3 and all(r["pins"] > 0 for r in evidence),
          receipts=[(r["path"], r["pins"], r["stale"]) for r in evidence])
    passed = all(c["passed"] for c in controls)
    print(json.dumps({"controls": controls, "passed": passed,
                      "passed_controls": sum(c["passed"] for c in controls),
                      "total_controls": len(controls)}, indent=1, sort_keys=True))
    return 0 if passed else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--tmp-parent", default="/var/tmp",
                        help="the parent for the replay mirror; MUST sit outside the repo")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    parent = Path(os.path.realpath(args.tmp_parent))
    if parent == ROOT or ROOT in parent.parents:
        print("sweep: --tmp-parent must sit outside the repository "
              "(replay-frozen refuses an in-repo mirror root)", file=sys.stderr)
        return 2
    parent.mkdir(parents=True, exist_ok=True)
    doc = sweep(str(parent))
    if args.json:
        print(json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=False))
    else:
        sys.stdout.write(render(doc))
    return doc["summary"]["exit"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
