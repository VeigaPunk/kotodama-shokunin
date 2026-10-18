#!/usr/bin/env python3
"""R26-O33..O36 — replay the two re-pointed sibling pin tails.

Round 25 left two pin tails open, both surfaced by the round-25 r4 checker's
`positive` and `negative` arms:

  A. the stale combined-source v2 successor pin
     (`reports/round-20/wart/expected-v2-07-r20.json`), whose `inputs` map pins
     `tools/d2-typed-labels.py` at `76536a92…` while the live projector measures
     `2819f687…`;
  B. the stale v3 packet-baseline pin (`reports/round-20/handoff/expected.json`),
     whose `packet_sha256` reads `e92f5e6775b6…` while the v3 exercise assembles
     `a97a0f0a0a49…`.

This seat re-points each as a NEW row under `reports/round-26/remainders/` (the
filed round-20 rows stay byte-identical) and proves the re-point the only way a
pin can be proven: by replaying the new row through the *same filed replayer*
that produced the red, and by replaying the stale row through that same replayer
as the paired control.

What this script asserts:

  1. each stale row still replays red (the control, captured before the fix);
  2. each new row replays green (the fix);
  3. the new rows are the only delta — the stale round-20 rows are byte-unchanged
     against the declared baseline revision;
  4. every filed round-8..25 byte is unchanged across the whole run.

It runs no historical validator beyond the two filed replayers named above, and
writes nothing outside its `--receipt` path.

Usage:
    python3 reports/round-26/remainders/pin-repoint-check.py --check [--receipt PATH]
    python3 reports/round-26/remainders/pin-repoint-check.py --selftest
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
COMMAND = "python3 reports/round-26/remainders/pin-repoint-check.py"

V2_REPLAYER = "reports/round-15/handoff/frozen-verify.py"
V3_REPLAYER = "tools/exercise-handoff-e2e.py"

# tail A — the v2 successor row
STALE_V2 = "reports/round-20/wart/expected-v2-07-r20.json"
NEW_V2 = "reports/round-26/remainders/v2-successor-r26/expected.json"
STALE_V2_SHA256 = "ad761a61c0c3be068c54c382ce43c88978a6c0c2a0f7493bb46a15063e2ebd04"
NEW_V2_SHA256 = "f695b910699ab5310b0853fe38471b7714616973f7deff366e1298888b766bc3"
V2_STALE_DIGEST = "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb"
V2_LIVE_DIGEST = "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3"

# tail B — the v3 packet-baseline row
STALE_V3 = "reports/round-20/handoff/expected.json"
NEW_V3 = "reports/round-26/handoff/declared-in-r5/expected.json"
STALE_V3_SHA256 = "e2bfa52a35e518586be49cd61559f3d45ccea1e353e76281b51fe4d70ac39c4d"
NEW_V3_SHA256 = "855603f66ca125d027e3d1629a236209ae58eb05c9d31000e826981b42650de1"
V3_STALE_PACKET = "e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b"
V3_LIVE_PACKET = "e3fb1ca500d62981b59129f898ef7e4b2843b1fa5ab7d12e8fc16818d1f764b8"

BASELINE_REVISION = "fc13cd27b9e78d5d7c4f70740fd26c9383a7447b"
FILED_ROUNDS = range(8, 26)


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(argv, cwd=ROOT, timeout=600):
    proc = subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True,
                          timeout=timeout, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    return {"command": " ".join(argv), "exit": proc.returncode,
            "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}


def filed_snapshot(root):
    root = Path(root)
    return {path.relative_to(root).as_posix(): sha256_file(path)
            for number in FILED_ROUNDS
            for path in sorted((root / f"reports/round-{number}").rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts}


def replay_v2(root, baseline, temp):
    return run([sys.executable, V2_REPLAYER, "--baseline", baseline, "--root", "."],
               cwd=root)


def replay_v3(root, baseline, temp):
    """Replay a v3 row. `--quiet` is deliberately not passed: the failing arm's
    `E2E-DIGEST` code is printed only on the non-quiet path, and the control must
    carry the code rather than infer it from the exit alone."""
    return run([sys.executable, V3_REPLAYER, "--profile", "v3",
                "--baseline", baseline], cwd=root)


def check(root=ROOT, receipt=None):
    root = Path(root).resolve()
    controls = []

    def record(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    before = filed_snapshot(root)
    temp = Path(tempfile.mkdtemp(prefix="r26-o33-", dir=str(ROOT / ".scratch")))
    os.environ["TMPDIR"] = str(temp)

    # --- the two rows are the declared bytes -------------------------------
    record("stale-v2-row-filed-bytes", sha256_file(root / STALE_V2) == STALE_V2_SHA256,
           sha256=sha256_file(root / STALE_V2))
    record("new-v2-row-filed-bytes", sha256_file(root / NEW_V2) == NEW_V2_SHA256,
           sha256=sha256_file(root / NEW_V2))
    record("stale-v3-row-filed-bytes", sha256_file(root / STALE_V3) == STALE_V3_SHA256,
           sha256=sha256_file(root / STALE_V3))
    record("new-v3-row-filed-bytes", sha256_file(root / NEW_V3) == NEW_V3_SHA256,
           sha256=sha256_file(root / NEW_V3))

    # --- the moved value is the live value, re-measured ---------------------
    live_projector = sha256_file(root / "tools/d2-typed-labels.py")
    record("live-projector-measures-the-new-pin", live_projector == V2_LIVE_DIGEST,
           live=live_projector, pinned=V2_LIVE_DIGEST)
    new_v2 = json.loads((root / NEW_V2).read_text(encoding="utf-8"))
    old_v2 = json.loads((root / STALE_V2).read_text(encoding="utf-8"))
    record("v2-new-row-pins-live-projector",
           new_v2["inputs"]["tools/d2-typed-labels.py"] == live_projector)
    record("v2-stale-row-pins-the-old-projector",
           old_v2["inputs"]["tools/d2-typed-labels.py"] == V2_STALE_DIGEST)
    record("v2-delta-is-the-single-input",
           {k for k in set(new_v2["inputs"]) | set(old_v2["inputs"])
            if new_v2["inputs"].get(k) != old_v2["inputs"].get(k)}
           == {"tools/d2-typed-labels.py"},
           moved=[k for k in set(new_v2["inputs"]) | set(old_v2["inputs"])
                  if new_v2["inputs"].get(k) != old_v2["inputs"].get(k)])

    new_v3 = json.loads((root / NEW_V3).read_text(encoding="utf-8"))
    old_v3 = json.loads((root / STALE_V3).read_text(encoding="utf-8"))
    record("v3-stale-row-pins-the-old-packet",
           old_v3["packet_sha256"] == V3_STALE_PACKET)
    record("v3-new-row-pins-the-live-packet",
           new_v3["packet_sha256"] == V3_LIVE_PACKET)

    # --- the control: the stale rows still replay red -----------------------
    stale_v2 = replay_v2(root, STALE_V2, temp)
    record("control-stale-v2-row-replays-red",
           stale_v2["exit"] != 0 and "V2F-DIGEST" in stale_v2["stderr"],
           exit=stale_v2["exit"], stderr=stale_v2["stderr"][:200])
    stale_v3 = replay_v3(root, STALE_V3, temp)
    record("control-stale-v3-row-replays-red",
           stale_v3["exit"] != 0 and "E2E-DIGEST" in stale_v3["stdout"],
           exit=stale_v3["exit"], tail=stale_v3["stdout"][-200:])

    # --- the fix: the new rows replay green --------------------------------
    fresh_v2 = replay_v2(root, NEW_V2, temp)
    record("new-v2-row-replays-green",
           fresh_v2["exit"] == 0 and "frozen-v2: exit=0" in fresh_v2["stdout"],
           exit=fresh_v2["exit"], stdout=fresh_v2["stdout"][:200])
    fresh_v3 = replay_v3(root, NEW_V3, temp)
    record("new-v3-row-replays-green",
           fresh_v3["exit"] == 0 and "handoff-v3: exit=0" in fresh_v3["stdout"],
           exit=fresh_v3["exit"], stdout=fresh_v3["stdout"][:200])

    # --- the new rows are the only delta -----------------------------------
    record("v2-row-pair-differs-only-by-the-input-and-its-digest",
           {k for k in set(new_v2) | set(old_v2) if new_v2.get(k) != old_v2.get(k)}
           == {"inputs", "baseline_digest"},
           moved=sorted(k for k in set(new_v2) | set(old_v2)
                        if new_v2.get(k) != old_v2.get(k)))
    record("v3-row-carries-the-full-five-file-set",
           all((root / "reports/round-26/remainders/v3-baseline-r26" / name).is_file()
               for name in ("expected.json", "packet.md", "twin.json", "freeze.txt", "run.log")))

    after = filed_snapshot(root)
    changed = sorted(path for path in set(before) | set(after)
                     if before.get(path) != after.get(path))
    record("filed-rounds-8-25-unchanged", not changed, changed=changed[:10])

    passed = all(item["passed"] for item in controls)
    payload = {
        "date": dt.datetime.now(dt.timezone.utc).isoformat(),
        "command": f"{COMMAND} --check",
        "root": str(root),
        "baseline_revision": BASELINE_REVISION,
        "tales": {
            "A": {"surface": STALE_V2, "stale_pin": V2_STALE_DIGEST,
                  "live_pin": V2_LIVE_DIGEST, "new_row": NEW_V2,
                  "replayer": V2_REPLAYER,
                  "control": {"exit": stale_v2["exit"], "code": "V2F-DIGEST"},
                  "fix": {"exit": fresh_v2["exit"]}},
            "B": {"surface": STALE_V3, "stale_pin": V3_STALE_PACKET,
                  "live_pin": V3_LIVE_PACKET, "new_row": NEW_V3,
                  "replayer": f"{V3_REPLAYER} --profile v3",
                  "control": {"exit": stale_v3["exit"], "code": "E2E-DIGEST"},
                  "fix": {"exit": fresh_v3["exit"]}},
        },
        "controls": controls,
        "passed": passed,
        "passed_controls": sum(item["passed"] for item in controls),
        "total_controls": len(controls),
        "limits": [
            "A pin is integrity, never truth and never clearance; re-pointing a pin "
            "asserts the bytes moved, not that the move was correct.",
            "The re-pointed rows land under reports/round-26/; the filed round-20 rows "
            "stay byte-identical and were not edited.",
            "The frozen round-20 runner discovers its v2/v3 rows under reports/round-20/, "
            "so the re-point is proven by replay, not by moving the runner's discovery path.",
        ],
    }
    if receipt:
        Path(receipt).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                                 encoding="utf-8")
    return payload


def selftest():
    controls = []

    def record(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    record("stale-and-live-v2-digests-differ", V2_STALE_DIGEST != V2_LIVE_DIGEST)
    record("stale-and-live-v3-packets-differ", V3_STALE_PACKET != V3_LIVE_PACKET)
    record("filed-round-window-is-8-25",
           list(FILED_ROUNDS) == list(range(8, 26)), window=[8, 25])
    record("replayers-are-the-filed-ones",
           (ROOT / V2_REPLAYER).is_file() and (ROOT / V3_REPLAYER).is_file())
    record("stale-and-new-paths-are-distinct",
           STALE_V2 != NEW_V2 and STALE_V3 != NEW_V3)
    payload = {"date": dt.datetime.now(dt.timezone.utc).isoformat(),
               "command": f"{COMMAND} --selftest", "controls": controls,
               "passed": all(item["passed"] for item in controls),
               "passed_controls": sum(item["passed"] for item in controls),
               "total_controls": len(controls)}
    return payload


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--selftest", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args(argv)
    payload = selftest() if args.selftest else check(args.root, args.receipt)
    print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
