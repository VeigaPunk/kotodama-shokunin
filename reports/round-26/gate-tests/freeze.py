#!/usr/bin/env python3
r"""freeze.py — build the round-26 frozen generation (seats R26-D17..D20).

The round-25 `gate-input` generation pins `tools/gates/typed-pipeline-gate.py`
at `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`; the
live gate (and the committed blob at `fc13cd2`/HEAD) is
`b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85`. So every
row of that generation refuses with `gate_digest_mismatch` before a gate runs.

The rule this harness follows is the lane's: **a re-freeze is a new recording,
never an in-place edit** (`tools/gates/frozen/round-18/README.md`). Nothing
under `tools/gates/frozen/round-25/` is touched; this writes a new generation
directory beside it, with the same row schema and the same four input-class
rows plus the two fail-closed controls.

Usage
-----
    python3 reports/round-26/gate-tests/freeze.py            # build the generation
    python3 reports/round-26/gate-tests/freeze.py --check    # verify, write nothing

The generation directory and its `MANIFEST.tsv` are the deliverable; the
receipt (`freeze-receipt.json`) records the pins and the measured verdicts.
Exit 0 all rows recorded, 1 a row was not reproducible, 2 could-not-evaluate.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
DEFAULT_GENERATION = "gate-input"
GATE = ROOT / "tools/gates/typed-pipeline-gate.py"
GATE_REL = "tools/gates/typed-pipeline-gate.py"

COLUMNS = ("gate", "gate_sha256", "input", "input_sha256", "exit_code",
           "finding_count", "output", "output_sha256", "input_snapshot", "command")

# The four input-class rows, matching the round-25 generation's schema: both
# families, source packet and typed packet. The typed rows grade the packet
# against the source it *declares* (round-25's input-class fix), so a rebuild
# cannot manufacture findings.
ROWS = (
    ("d4 source packet", "examples/culture-d4/packet.d4.yml", "d4-source.out"),
    ("d4 typed packet (declared source)",
     "examples/culture-d4/packet.d4.typed.yml", "d4-typed.out"),
    ("d2 source packet", "examples/culture-d2/packet.d2.yml", "d2-source.out"),
    ("d2 typed packet (declared source)",
     "examples/culture-d2/packet.d2.typed.yml", "d2-typed.out"),
)


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def child_env():
    env = dict(os.environ)
    env["TMPDIR"] = str(ROOT / ".scratch")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def run_gate(input_rel):
    return subprocess.run([sys.executable, str(GATE), input_rel],
                          capture_output=True, cwd=str(ROOT), env=child_env(),
                          check=False)


def finding_count(payload):
    return sum(1 for line in payload.decode("utf-8", "replace").splitlines()
               if line.startswith("FINDING "))


def build_controls(controls):
    """The two fail-closed controls, byte-copied from the round-25 pair.

    A typed packet whose declared source is absent, and one whose
    `assembly.packet_sha256` no longer matches its declared source. Both must
    exit 2 — an input-class refusal, never a verdict.
    """
    controls.mkdir(parents=True, exist_ok=True)
    source = ROOT / "examples/culture-d2/packet.d2.typed.yml"
    text = source.read_text(encoding="utf-8")

    orphan = text.replace('  packet: "examples/culture-d2/packet.d2.yml"',
                          '  packet: "examples/culture-d2/packet.absent.yml"', 1)
    if orphan == text:
        raise SystemExit("control anchor not found: typed-without-source")
    (controls / "typed-without-source.yml").write_text(orphan, encoding="utf-8")

    stale = text.replace(
        '  packet_sha256: "e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643"',
        '  packet_sha256: "%s"' % ("0" * 64), 1)
    if stale == text:
        raise SystemExit("control anchor not found: typed-stale-source")
    (controls / "typed-stale-source.yml").write_text(stale, encoding="utf-8")

    return (("controls/typed-without-source.yml", "control-without-source.out"),
            ("controls/typed-stale-source.yml", "control-stale-source.out"))


def record(out, inputs, rows, input_rel, output_name, input_is_generated=False):
    """Run the gate over `input_rel`, write the output, append the row."""
    proc = run_gate(input_rel)
    out_path = out / output_name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(proc.stdout)
    snapshot = inputs / input_rel
    if input_is_generated:
        snapshot = ROOT / input_rel
    else:
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / input_rel, snapshot)
    rows.append({
        "gate": GATE_REL, "gate_sha256": sha(GATE),
        "input": input_rel, "input_sha256": sha(ROOT / input_rel),
        "exit_code": proc.returncode, "finding_count": finding_count(proc.stdout),
        "output": str(out_path.relative_to(ROOT)), "output_sha256": sha(out_path),
        "input_snapshot": str(snapshot.relative_to(ROOT)),
        "command": "python3 %s %s" % (GATE_REL, input_rel),
    })
    return proc


def out_dir(generation):
    return ROOT / "tools/gates/frozen/round-26" / generation


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true",
                        help="verify the generation reproduces; write nothing")
    parser.add_argument("--generation", default=DEFAULT_GENERATION,
                        help="generation directory under tools/gates/frozen/round-26 "
                             "(default: %(default)s). A re-freeze after the input "
                             "moved is a NEW generation, never an edit.")
    args = parser.parse_args(argv[1:])

    if args.check:
        return replay_check(args.generation)

    out = out_dir(args.generation)
    inputs = out / "inputs"
    controls = out / "controls"

    rows = []
    verdicts = []
    for label, input_rel, output_name in ROWS:
        proc = record(out, inputs, rows, input_rel, output_name)
        verdicts.append({"label": label, "exit": proc.returncode,
                         "findings": finding_count(proc.stdout)})
        print("%-58s exit=%d findings=%2d" % (label, proc.returncode,
                                              finding_count(proc.stdout)))

    for name, out_name in build_controls(controls):
        rel = str((out / name).relative_to(ROOT))
        proc = record(out, inputs, rows, rel, out_name)
        verdicts.append({"label": name, "exit": proc.returncode,
                         "findings": finding_count(proc.stdout)})
        print("%-58s exit=%d findings=%2d" % (name, proc.returncode,
                                              finding_count(proc.stdout)))

    manifest = out / "MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8") as handle:
        handle.write("\t".join(COLUMNS) + "\n")
        for row in rows:
            handle.write("\t".join(str(row[key]) for key in COLUMNS) + "\n")

    receipt = {
        "schema": "kotodama-r26-gate-input-freeze-v1",
        "generation": "round-26 %s (R26-D17..D20)" % args.generation,
        "frozen_at": now(),
        "frozen_by": "round-26 D17..D20 gate+tests seats",
        "supersedes": {
            "generation": "tools/gates/frozen/round-25/gate-input/MANIFEST.tsv",
            "pinned_gate_sha256":
                "879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126",
            "live_gate_sha256": sha(GATE),
            "reason": "the round-25 generation pins a gate revision that is not "
                      "on disk; every row refuses gate_digest_mismatch before a "
                      "gate runs. A re-pin is a new generation, never an edit.",
        },
        "pins": {"tools/gates/typed-pipeline-gate.py": sha(GATE)},
        "input_pins": {input_rel: sha(ROOT / input_rel)
                       for _label, input_rel, _out in ROWS},
        "rows": len(rows), "verdicts": verdicts,
        "replay": "python3 tools/replay-frozen.py "
                  "tools/gates/frozen/round-26/%s/MANIFEST.tsv --json "
                  "(TMPDIR must sit outside the repository)" % args.generation,
        "notes": "No byte of tools/gates/frozen/round-25/** or any earlier "
                 "generation is edited by this freeze; a re-freeze after the "
                 "input moved is a new generation.",
    }
    (out / "freeze-receipt.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("manifest rows: %d" % len(rows))
    print("generation: %s" % out.relative_to(ROOT))
    return 0


def replay_check(generation):
    """Replay the generation that is already on disk."""
    manifest = out_dir(generation) / "MANIFEST.tsv"
    if not manifest.is_file():
        print("no generation on disk: %s" % manifest.relative_to(ROOT))
        return 2
    outside = Path(os.environ.get("KOTODAMA_REPLAY_TMPDIR") or "/var/tmp")
    outside = outside / ("kotodama-r26-freeze-check-%d" % os.getpid())
    outside.mkdir(parents=True, exist_ok=True)
    env = child_env()
    env["TMPDIR"] = str(outside)
    proc = subprocess.run([sys.executable, str(ROOT / "tools/replay-frozen.py"),
                           str(manifest), "--json"],
                          capture_output=True, text=True, cwd=str(ROOT),
                          env=env, check=False)
    shutil.rmtree(outside, ignore_errors=True)
    try:
        document = json.loads(proc.stdout)
        rows = document.get("rows") or []
        statuses = [row.get("status") for row in rows]
        summary = {"rows": len(rows),
                   "reproduced": statuses.count("reproduced"),
                   "mismatch": statuses.count("mismatch"),
                   "could_not_evaluate": statuses.count("could-not-evaluate")}
        print("replay %s: exit %d %s" % (generation, proc.returncode, summary))
    except ValueError:
        print((proc.stdout or proc.stderr).strip().splitlines()[-1]
              if (proc.stdout or proc.stderr).strip() else "replay: no output")
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv))
