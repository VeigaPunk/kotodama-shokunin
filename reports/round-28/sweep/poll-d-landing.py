#!/usr/bin/env python3
"""R28-O25..O32 — poll for the round-28 D landing to settle, then stop.

The O sweep must run on the *amended* packet, and the D seat lands in waves
(RL-4 first, then the law replay leg, then the hold-set re-pin). A sweep taken
mid-wave is stale the moment the next wave lands. This polls for three signals
and prints the stamp it saw:

  1. a tool under `tools/` names a `D4L-LAW-*` finding id (the RL-1 replay leg);
  2. the D4 hold set's `packet_sha256` equals the live packet digest (the D seat
     re-pinned it);
  3. the live D4 packet digest has not changed across the last N polls (settled).

Read-only. Prints one JSON line per poll. Exits 0 when settled, 1 on timeout.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKET = "examples/culture-d4/packet.d4.yml"
HOLDS = "examples/culture-d4/expected-holds.json"


def sha(rel: str):
    try:
        return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
    except OSError:
        return None


def law_leg_present() -> list[str]:
    hits = []
    for path in (ROOT / "tools").rglob("*.py"):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "D4L-LAW" in text:
            hits.append(str(path.relative_to(ROOT)))
    return sorted(hits)


def holds_packet() -> str | None:
    try:
        doc = json.loads((ROOT / HOLDS).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return doc.get("packet_sha256")


def main(argv=None):
    rounds = int(argv[0]) if argv else 20
    interval = int(argv[1]) if len(argv) > 1 else 60
    history = []
    for index in range(rounds):
        live = sha(PACKET)
        holds = holds_packet()
        legs = law_leg_present()
        history.append(live)
        settled = len(history) >= 3 and len(set(history[-3:])) == 1
        row = {
            "poll": index + 1,
            "live_packet": (live or "")[:16],
            "holds_packet": (holds or "")[:16],
            "holds_matches_live": bool(live and holds == live),
            "law_leg_tools": legs,
            "law_leg_present": bool(legs),
            "settled_3": settled,
        }
        print(json.dumps(row), flush=True)
        if row["law_leg_present"] and row["holds_matches_live"] and settled:
            print(json.dumps({"verdict": "settled", **row}), flush=True)
            return 0
        if index + 1 < rounds:
            time.sleep(interval)
    print(json.dumps({"verdict": "timeout", "polls": len(history)}), flush=True)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
