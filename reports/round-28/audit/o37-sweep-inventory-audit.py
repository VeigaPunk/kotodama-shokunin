#!/usr/bin/env python3
"""R28-O37 — independent audit of the round-28 D4 pin-sweep *inventory*.

Question this seat answers: does the sweep the round-28 O claim files enumerate
**every** surface in the lane that carries a pin over a D4 artifact, or does it
leave named surfaces un-swept? "Inventory completeness" is a coverage claim, so
it must be measured against an inventory built independently of the sweep's own.

Method. This tool builds the census ITSELF, from the tree, by walking every file
class that can carry a digest pin, and then diffs that census against the surface
set the round-28 sweep instrument actually visits. It never reads a verdict from
the sweep; it re-derives both sides. The reach is measured *behaviourally* —
the sweep is run and every repo-relative path its receipt names is collected —
with a static `rglob` read of its source as a labelled fallback.

Surface families walked (the auditor's own definition, recorded so a reader can
disagree with it):

  A  MANIFEST.tsv rows under tools/gates/frozen/** and reports/**/frozen/**
  B  expected.json under tools/gates/expected/**
  C  expected.json under tools/gates/frozen/** and reports/round-9/baselines/**
  D  freeze-receipt.json embedded pin maps
  E  reports/**/expected*.json handoff baselines (v2 + v3 families)
  F  tools/gates/typed-pipelines.json (the live L1-profile pin channel)
  G  expected-holds*.json self-pins (packet / projection / projector digests)
  H  twin.json embedded `artifact_manifest` pins
  I  reports/**/evidence/*.json embedded D4 path→digest pairs
  J  every other tracked file that carries a D4 path→digest pair or a digest
     identical to a live D4 artifact (validation receipts, `packet.md` renders,
     `freeze.txt` rows, `rerun.json`) — the false-positive hunt family

Classification is by **digest identity and declared path**, never by filename
convention alone: a hold set whose schema never says "D4" is a D4 surface when a
digest it asserts IS the digest of a live D4 artifact (round-27 R27-O37 §2.1).

Every surface also carries a *class*, because "un-swept" is not "drifted":

  live-pin            asserts a digest for a live artifact; stale => a re-pin is owed
  historical-receipt  records the stamp it measured; stale by design, never owed
  frozen-snapshot     a byte copy inside a frozen generation's `inputs/` tree
  scratch-copy        a scratch/supplement tree copy of another surface
  render              a human-readable render (`packet.md`, `freeze.txt`)

Usage:
    export TMPDIR=/var/tmp/kotodama-r28-o37   # OUTSIDE the repo
    python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py           # text
    python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py --json    # receipt
    python3 -B reports/round-28/audit/o37-sweep-inventory-audit.py --selftest

Exit codes:
  0  the sweep inventory covers every live-pin D4 surface this census finds
  1  at least one live-pin D4 surface is missed (a coverage finding, never a
     quality claim)
  2  could-not-evaluate: the census could not be built, or the sweep instrument
     the claim names does not exist yet / could not be read
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ANY_HEX = re.compile(r"\b[0-9a-f]{64}\b")
D4_PATH = re.compile(r"examples/culture-d4/[A-Za-z0-9_./-]+")
D4_PAIR = re.compile(r'"(examples/culture-d4/[A-Za-z0-9_./-]+)"\s*:\s*"([0-9a-f]{64})"')
TSV_D4 = re.compile(r"^(examples/culture-d4/[A-Za-z0-9_./-]+)\t([0-9a-f]{64})", re.M)

SKIP_PARTS = {".git", ".scratch", ".ufo", ".tower", "__pycache__", ".venv",
              "node_modules", ".deploy", ".devin", ".omp"}

# The R28 sweep the claim names. Discovery is a *name* test, never a glob over
# every .py in a directory: `reports/round-28/sweep/` also holds `repin.py` (a
# WRITING tool that re-freezes baselines and manifests) and `poll-d-landing.py`
# (a blocking poller). Reaching an instrument by executing it is only safe for a
# read-only reporter, so a candidate is admitted only when its own source shows
# no write path AND it accepts `--json`.
SWEEP_GLOBS = ("reports/round-28/pinsweep/sweep*.py",
               "reports/round-28/sweep/sweep*.py")
# A writing tool is detected by markers that create or overwrite *content*:
# `write_text`, `write_bytes`, `shutil.copyfile`, `os.replace`, `rmtree`, and an
# `open(..., "w")`. `mkdir(` is deliberately NOT a marker — the read-only sweep
# calls `parent.mkdir(...)` once to create its TMPDIR parent outside the repo,
# and excluding it on that basis would hide the very instrument being audited.
WRITE_SUBSTRINGS = ("write_text(", "write_bytes(", "shutil.copyfile(", "shutil.copy(",
                    "rmtree(", "os.replace(", "os.rename(")
WRITE_PATTERNS = (re.compile(r"open\([^)]*['\"]w"),)


def writes(path: str) -> bool:
    """True when this tool's own source shows a write path."""
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    return any(marker in text for marker in WRITE_SUBSTRINGS) \
        or any(pattern.search(text) for pattern in WRITE_PATTERNS)


def sha_file(path) -> str | None:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return None


def rel(path) -> str:
    return os.path.relpath(str(path), str(ROOT))


def skipped(relpath: str) -> bool:
    return any(part in SKIP_PARTS for part in Path(relpath).parts)


def g(pattern: str) -> list[str]:
    return sorted(p for p in glob.glob(str(ROOT / pattern), recursive=True)
                  if not skipped(rel(p)))


_D4_DIGESTS = None


def d4_digests() -> set[str]:
    """The digest set of every live file under examples/culture-d4/."""
    global _D4_DIGESTS
    if _D4_DIGESTS is None:
        found = set()
        for path in glob.glob(str(ROOT / "examples/culture-d4/**/*"), recursive=True):
            if os.path.isfile(path):
                digest = sha_file(path)
                if digest:
                    found.add(digest)
        _D4_DIGESTS = found
    return _D4_DIGESTS


_RECORDED_D4_PACKETS = None


def recorded_d4_packets() -> set[str]:
    """Every **packet** digest the D4 lineage records — live, superseded, and current.

    This is the set the family-G admission test must use, and two details are
    load-bearing:

    * It carries **packet** digests only. An earlier pass pooled every value of
      `supersedes_pins`, which includes `projector_sha256` — and the D2 drill's
      hold set pins the *same* projector (`2819f687…`), so the pooled set
      admitted the D2 hold set. A packet digest is what distinguishes the two
      drills; a projector digest is shared infrastructure and cannot.
    * It includes the hold set's own current `packet_sha256`. Using only the
      *live* digest is the round-27 defect this audit exists to catch: the walker
      would go blind at exactly the moment drift begins.
    """
    global _RECORDED_D4_PACKETS
    if _RECORDED_D4_PACKETS is None:
        found = set()
        live = sha_file(ROOT / "examples/culture-d4/packet.d4.yml")
        if live:
            found.add(live)
        try:
            holds = json.loads(
                (ROOT / "examples/culture-d4/expected-holds.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            holds = {}
        for key in ("packet_sha256", "earlier_packet_sha256"):
            value = holds.get(key)
            if isinstance(value, str) and HEX64.match(value):
                found.add(value)
        supersedes = holds.get("supersedes_pins") or {}
        value = supersedes.get("packet_sha256") if isinstance(supersedes, dict) else None
        if isinstance(value, str) and HEX64.match(value):
            found.add(value)
        try:
            profile = json.loads(
                (ROOT / "tools/gates/typed-pipelines.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            profile = {}
        for entry in profile.get("profiles", []):
            spec = entry.get("packet") or {}
            note = spec.get("superseded")
            if isinstance(note, str):
                found.update(ANY_HEX.findall(note))
        _RECORDED_D4_PACKETS = found
    return _RECORDED_D4_PACKETS


def is_d4_artifact(path: str) -> bool:
    """True when this file IS a D4 artifact (or a byte copy of one).

    A copy of `packet.d4.yml` under a baseline or a frozen `inputs/` tree carries
    no pin *for* anything — it is the pinned bytes. Counting it as a pin surface
    would report every baseline as drifted, which is the append-only rule working,
    not a finding.

    The exception is a *hold set*: `expected-holds.json` lives inside the culture
    tree but is a pin record (it asserts the packet / projection / projector
    digests), not an artifact, so it stays in surface.
    """
    relpath = rel(path)
    name = Path(relpath).name
    if name.startswith("expected-holds"):
        return False
    if relpath.startswith("examples/culture-d4/") or relpath == "tools/d2-typed-labels.py":
        return True
    if name in ("packet.d4.yml", "packet.d4.typed.yml", "typed-labels.d4.yml"):
        return True
    parts = Path(relpath).parts
    if "culture-d4" in parts:
        return True
    return False


# --------------------------------------------------------------- census

def census() -> dict[str, list[str]]:
    fam = {}
    fam["A"] = [p for p in g("tools/gates/frozen/**/MANIFEST.tsv")
                + g("reports/**/frozen/**/MANIFEST.tsv")]
    fam["B"] = g("tools/gates/expected/**/expected.json")
    fam["C"] = g("tools/gates/frozen/**/expected.json") + g("reports/round-9/baselines/**/expected.json")
    fam["D"] = g("tools/gates/frozen/**/freeze-receipt.json")
    fam["E"] = [p for p in g("reports/**/expected*.json") if "/round-9/" not in p]
    fam["F"] = g("tools/gates/typed-pipelines.json")
    fam["G"] = g("examples/**/expected-holds*.json")
    fam["H"] = g("**/twin.json")
    fam["I"] = g("reports/**/evidence/*.json")
    # J — the false-positive hunt: every other file that names a D4 path or a
    # D4-identical digest. This is the family that has repeatedly found surfaces
    # a filename walk cannot reach (round-27 R27-O38 section 5).
    already = {p for group in fam.values() for p in group}
    j = []
    for path in g("**/*"):
        if path in already or not os.path.isfile(path):
            continue
        if Path(path).suffix not in (".json", ".md", ".txt", ".tsv", ".yml", ".yaml", ".log", ".out"):
            continue
        try:
            text = Path(path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "culture-d4" in text and ANY_HEX.search(text):
            j.append(path)
        elif any(digest in text for digest in d4_digests()):
            j.append(path)
    fam["J"] = sorted(j)
    return fam


# --------------------------------------------------------------- resolution

def json_pairs(doc, acc: dict):
    """Collect every {path -> digest} pair from an arbitrary JSON document."""
    stack = [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            if isinstance(node.get("path"), str) and isinstance(node.get("sha256"), str):
                acc.setdefault(node["path"], node["sha256"])
            for key, val in node.items():
                # a bare key is a pin target only when it names a path; `sha256`
                # and `packet_sha256` are field names, not targets
                if isinstance(key, str) and "/" in key \
                        and isinstance(val, str) and HEX64.match(val):
                    acc.setdefault(key, val)
                if isinstance(val, (dict, list)):
                    stack.append(val)
        elif isinstance(node, list):
            stack.extend(node)
    return acc


def resolve_pins(path: str) -> dict[str, str]:
    """Every {d4_target -> declared digest} this surface asserts, by shape."""
    out: dict[str, str] = {}
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    suffix = Path(path).suffix
    if suffix in (".tsv", ".txt", ".md", ".log", ".out"):
        for match in TSV_D4.finditer(text):
            out.setdefault(match.group(1), match.group(2))
        for match in D4_PAIR.finditer(text):
            out.setdefault(match.group(1), match.group(2))
        return out
    try:
        doc = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        for match in D4_PAIR.finditer(text):
            out.setdefault(match.group(1), match.group(2))
        return out
    json_pairs(doc, out)
    return out


def surface_class(relpath: str, family: str) -> str:
    """The class of a pin surface, which decides what "missed" means for it.

    `live-pin`        a surface the lane *maintains* as a current pin, so a stale
                      one is owed a successor row. Families A–I are exactly
                      these (manifests, battery baselines, handoff baselines,
                      freeze receipts, the profile, hold sets, twins, evidence
                      receipts), plus a round's own freshly-frozen rows.
    `historical`      a record of the stamp it measured — `validation.json`,
                      `rerun.json`, `repin.json`, an audit receipt, `d4-pins.json`.
                      Stale by design: "un-swept" for these is a coverage
                      observation, never a finding owed a re-pin.
    `frozen-snapshot` a byte copy inside a frozen generation's `inputs/` tree.
    `render`          a human-readable render (`packet.md`, `freeze.txt`).
    `scratch-copy`    a copy inside a scratch/supplement tree.

    Class is decided by *where the surface lives and what it is for*, not by its
    filename: `expected.json` is a live pin under the battery roots and under
    `reports/**/expected*.json`, but a `validation.json` anywhere is a receipt.
    """
    parts = Path(relpath).parts
    if "inputs" in parts and "frozen" in parts:
        return "frozen-snapshot"
    if "supplement-opencode-1" in parts or "scratch" in parts:
        return "scratch-copy"
    if Path(relpath).suffix == ".md" or Path(relpath).name in ("freeze.txt", "packet.md"):
        return "render"
    name = Path(relpath).name
    if name in ("validation.json", "rerun.json", "sweep-receipt.json",
                "adjudication-receipt.json", "inventory-receipt.json",
                "receipt.json", "census.json", "fragment-ledger.json",
                "repin.json", "verification.json", "d4-pins.json",
                "before-state.json", "attempt-01-verification.json"):
        return "historical"
    if family == "J":
        # a family-J surface is not one of the maintained families; unless it is
        # a round's own fresh pin row, it is a record of a past stamp
        if name in ("expected.json", "twin.json", "freeze-receipt.json",
                    "typed-pipelines.json") or name.startswith("expected-holds"):
            return "live-pin"
        return "historical"
    return "live-pin"


def classify(path: str, family: str) -> dict:
    """Does this surface pin a D4 artifact, and by what evidence?

    A *pin surface* is a record that asserts a digest **for another path**. A
    file that IS a D4 artifact, or a byte copy of one, is the pinned bytes, not a
    pin, and is excluded (see `is_d4_artifact`).
    """
    relpath = rel(path)
    suffix = Path(path).suffix
    if is_d4_artifact(relpath):
        return {"pins_d4": False, "pins": {}, "why": "is itself a D4 artifact"}
    pins = resolve_pins(relpath)
    live_digests = d4_digests()
    d4_by_path = {target: digest for target, digest in pins.items()
                  if target.startswith("examples/culture-d4/")}
    d4_by_digest = {target: digest for target, digest in pins.items()
                    if digest in live_digests and target not in d4_by_path}
    if family == "G":
        # a hold set is admitted by digest identity, not by a token match
        try:
            doc = json.loads(Path(relpath).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            doc = {}
        # a hold set is admitted by the identity of the *packet* it pins, not by
        # a token match and not by a shared projector digest
        try:
            doc = json.loads(Path(relpath).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            doc = {}
        packet_pin = doc.get("packet_sha256")
        if not (isinstance(packet_pin, str) and packet_pin in recorded_d4_packets()):
            return {"pins_d4": False, "pins": {}, "why": "packet pin is not D4 lineage"}
        named = {key: doc.get(key) for key in
                 ("packet_sha256", "projection_sha256", "projector_sha256")
                 if isinstance(doc.get(key), str)}
        target_of = {"packet_sha256": "examples/culture-d4/packet.d4.yml",
                     "projection_sha256": "examples/culture-d4/typed-labels.d4.yml",
                     "projector_sha256": "tools/d2-typed-labels.py"}
        return {"pins_d4": True, "pins": {target_of[k]: v for k, v in named.items()},
                "why": "self-pin packet identity"}
    pins_d4 = bool(d4_by_path or d4_by_digest)
    why = ("path-declared D4 pin" if d4_by_path else
           "digest-identity D4 pin" if d4_by_digest else "no D4 pin")
    return {"pins_d4": pins_d4, "pins": {**d4_by_path, **d4_by_digest}, "why": why}


def stale_of(pins: dict[str, str]) -> list[dict]:
    out = []
    for target, pin in sorted(pins.items()):
        live = sha_file(ROOT / target)
        if live is not None and live != pin:
            out.append({"path": target, "pin": pin, "live": live})
    return out


# --------------------------------------------------------------- sweep reach

def find_sweep() -> list[str]:
    """The read-only sweep reporter(s), never a writing or blocking tool."""
    found = []
    for pattern in SWEEP_GLOBS:
        found += g(pattern)
    safe = []
    for path in sorted(set(found)):
        if writes(path):
            continue  # a writer is not a reporter; never execute it for reach
        if "--json" not in Path(path).read_text(encoding="utf-8", errors="replace"):
            continue
        safe.append(path)
    return safe


def _paths_in(obj, acc: set[str]):
    """Harvest the surfaces the instrument enumerates as *row subjects*.

    Only values under a row-subject key (`path`, `manifest`, `surface`) count.
    A loose "any string that looks like a path" walk would mark a surface
    "swept" merely because the receipt mentions it — e.g. a frozen generation's
    own copied artifact bytes appear inside the manifest rows it names. Reach
    must mean "the sweep re-verified this surface", not "the sweep's output
    happens to contain this string".
    """
    row_keys = ("path", "manifest", "surface")
    stack = [obj]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for key, val in node.items():
                if key in row_keys and isinstance(val, str):
                    if "/" in val and (ROOT / val).exists():
                        acc.add(val)
                elif isinstance(val, (dict, list)):
                    stack.append(val)
        elif isinstance(node, list):
            stack.extend(node)
    return acc


def _source_reach(instrument: str) -> set[str]:
    """Static fallback: every `rglob` the instrument's source performs."""
    text = Path(instrument).read_text(encoding="utf-8", errors="replace")
    roots = set()
    for match in re.finditer(r'(?:ROOT|HERE\.parents\[\d\])\s*(/\s*"[^"]+")+', text):
        parts = re.findall(r'"([^"]+)"', match.group(0))
        roots.add(str(ROOT.joinpath(*parts)))
    found = set()
    for match in re.finditer(r'([A-Za-z_][A-Za-z0-9_]*)\s*\.rglob\(\s*"([^"]+)"', text):
        name, pattern = match.groups()
        for root in roots:
            for hit in Path(root).rglob(pattern):
                if hit.is_file():
                    found.add(rel(hit))
    return found


def sweep_reach(instrument: str, tmp_parent: str) -> tuple[set[str], str, dict]:
    """Measure the sweep's reach behaviourally; label the method used."""
    env = dict(os.environ, TMPDIR=tmp_parent, PYTHONDONTWRITEBYTECODE="1")
    for args, method in ((["--json"], "instrument-receipt"),
                         ([], "instrument-stdout")):
        try:
            proc = subprocess.run([sys.executable, "-B", instrument, *args],
                                  capture_output=True, text=True, cwd=str(ROOT),
                                  env=env, timeout=1800)
        except (subprocess.TimeoutExpired, OSError):
            continue
        text = proc.stdout or ""
        if args == ["--json"]:
            try:
                return _paths_in(json.loads(text), set()), method, {"exit": proc.returncode}
            except (json.JSONDecodeError, ValueError):
                continue
        found = {token.strip('",;:()[]')
                 for token in re.split(r"\s+", text)
                 if "/" in token}
        found = {t for t in found if (ROOT / t).exists()}
        if found:
            return found, method, {"exit": proc.returncode}
    return _source_reach(instrument), "source-rglob-fallback", {}


# --------------------------------------------------------------- the audit

def audit(tmp_parent: str) -> dict:
    fam = census()
    instruments = find_sweep()
    reach: set[str] = set()
    reach_method = "no-sweep-instrument"
    reach_meta: dict = {}
    if instruments:
        for instrument in instruments:
            got, method, meta = sweep_reach(instrument, tmp_parent)
            reach |= got
            reach_method = method
            reach_meta[rel(instrument)] = meta

    rows = []
    for family in sorted(fam):
        for path in fam[family]:
            verdict = classify(path, family)
            if not verdict["pins_d4"]:
                continue
            relpath = rel(path)
            rows.append({
                "family": family,
                "surface": relpath,
                "class": surface_class(relpath, family),
                "why": verdict["why"],
                "pins": verdict["pins"],
                "stale": stale_of(verdict["pins"]),
                "swept": relpath in reach,
            })
    missed = [r for r in rows if not r["swept"]]
    owed = [r for r in missed if r["class"] == "live-pin" and r["stale"]]
    unverified = [r for r in missed if r["class"] == "live-pin" and not r["stale"]]
    hunt = false_negative_hunt(instruments[0]) if instruments else {}

    return {
        "schema": "kotodama-r28-o37-inventory-audit-v1",
        "tool": "reports/round-28/audit/o37-sweep-inventory-audit.py",
        "round": 28, "seat": "R28-O37", "date": "2026-10-18",
        "lane_head": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                                    capture_output=True, text=True).stdout.strip(),
        "sweep_instruments": [rel(p) for p in instruments],
        "reach_method": reach_method,
        "reach_meta": reach_meta,
        "reach_size": len(reach),
        "census_families": {k: len(v) for k, v in fam.items()},
        "d4_surfaces": len(rows),
        "swept": sum(1 for r in rows if r["swept"]),
        "missed": len(missed),
        "missed_live_pin_stale": len(owed),
        "missed_live_pin_holding": len(unverified),
        "false_negative_hunt": hunt,
        "rows": rows,
        "limits": ("covers the *inventory* (which surfaces exist and whether the "
                   "sweep visits them) only; it replays no pinned verdict and makes "
                   "no claim about design quality. 'missed' is relative to the "
                   "round-28 sweep instrument named above."),
    }


# --------------------------------------------------------------- duty D

def false_negative_hunt(sweep_source: str) -> dict:
    """Probe families a filename walk could omit, and report un-enumerated pins.

    Inherited from round-27 R27-O38 section 5, which found three evidence
    receipts a filename walk never reached. The question here is narrower and
    sharper: **which key names does the round-28 sweep's own family-J admission
    test read, and does any filed pin surface key its pins under a different
    name?** A sweep that reads `inputs` + four map keys is blind to a receipt
    that keys its pins under `live_pins`, `readset_pins`, `new_pins`, ... — so
    this duty enumerates the actual key vocabulary in use and names the gaps.
    """
    text = Path(sweep_source).read_text(encoding="utf-8", errors="replace")
    read_keys = sorted(set(re.findall(r'"(inputs|input_pins|pins|live_tool_and_input_pins|'
                                      r'snapshot_pins|rows|live_pins|readset_pins|new_pins)"',
                                      text)))
    # every filed JSON that carries a D4 path→digest pair, by its own key name
    vocabulary: dict[str, list[str]] = {}
    for path in g("reports/**/*.json") + g("tools/**/*.json"):
        relpath = rel(path)
        if skipped(relpath):
            continue
        try:
            doc = json.loads(Path(relpath).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(doc, dict):
            continue
        for key, val in doc.items():
            if isinstance(val, dict) and any(
                    str(k).startswith("examples/culture-d4/") for k in val):
                vocabulary.setdefault(key, []).append(relpath)
    unread = {key: sorted(set(paths)) for key, paths in vocabulary.items()
              if key not in ("inputs", "input_pins", "pins",
                             "live_tool_and_input_pins", "snapshot_pins")}
    return {
        "sweep_reads_keys": read_keys,
        "d4_pin_key_vocabulary": {k: len(v) for k, v in sorted(vocabulary.items())},
        "keys_the_sweep_does_not_read": unread,
    }


def render(receipt: dict) -> list[str]:
    lines = [f"R28-O37 sweep-inventory audit — lane HEAD {receipt['lane_head'][:12]}"]
    lines.append(f"  sweep instrument(s): {', '.join(receipt['sweep_instruments']) or 'NONE'}")
    lines.append(f"  reach: {receipt['reach_size']} surface(s) [{receipt['reach_method']}]")
    for family, count in sorted(receipt["census_families"].items()):
        lines.append(f"  family {family}: {count:5} file(s) in census")
    lines.append(f"  D4-pinning surfaces: {receipt['d4_surfaces']} "
                 f"({receipt['swept']} swept, {receipt['missed']} MISSED)")
    lines.append(f"    of the missed: {receipt['missed_live_pin_stale']} live-pin stale "
                 f"(owed a successor), {receipt['missed_live_pin_holding']} live-pin holding")
    for row in receipt["rows"]:
        if row["swept"]:
            continue
        lines.append(f"    ! [{row['family']}/{row['class']}] {row['surface']} "
                     f"({row['why']}; stale pins: {len(row['stale'])})")
    return lines


def selftest() -> int:
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    check("HEX64 accepts 64 hex", bool(HEX64.match("a" * 64)))
    check("HEX64 rejects 63 hex", not HEX64.match("a" * 63))
    check("HEX64 rejects uppercase", not HEX64.match("A" * 64))
    check("D4_PATH matches a component path",
          bool(D4_PATH.match("examples/culture-d4/components/13-register-law.yml")))
    check("D4_PAIR matches a JSON pair",
          bool(D4_PAIR.search('{"examples/culture-d4/packet.d4.yml": "' + "a" * 64 + '"}')))
    check("skipped() rejects a .scratch path",
          skipped(".scratch/x/y.json") and skipped("reports/x/.ufo/y.json"))
    check("skipped() keeps a filed round path",
          not skipped("reports/round-27/pinsweep/sweep.py"))
    check("json_pairs reads the twin shape",
          json_pairs({"artifact_manifest": [{"path": "examples/culture-d4/x", "sha256": "b" * 64}]},
                     {}) == {"examples/culture-d4/x": "b" * 64})
    check("json_pairs reads a nested inputs map",
          json_pairs({"inputs": {"examples/culture-d4/y": "c" * 64}}, {})
          == {"examples/culture-d4/y": "c" * 64})
    check("surface_class marks a frozen input copy",
          surface_class("tools/gates/frozen/round-3/inputs/examples/culture-d4/packet.d4.yml",
                        "A") == "frozen-snapshot")
    check("surface_class marks a render",
          surface_class("reports/round-20/handoff/packet.md", "J") == "render")
    check("surface_class marks a validation receipt",
          surface_class("reports/round-27/validation.json", "J") == "historical")
    check("surface_class marks a battery baseline as a live pin",
          surface_class("tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json",
                        "B") == "live-pin")
    check("surface_class marks a handoff baseline as a live pin",
          surface_class("reports/round-27/pinsweep/v3-baseline-r27/expected.json", "E") == "live-pin")
    check("surface_class marks the profile as a live pin",
          surface_class("tools/gates/typed-pipelines.json", "F") == "live-pin")
    check("is_d4_artifact excludes a packet byte copy",
          is_d4_artifact("tools/gates/frozen/round-3/inputs/examples/culture-d4/packet.d4.yml"))
    check("is_d4_artifact keeps a hold set in surface",
          not is_d4_artifact("examples/culture-d4/expected-holds.json"))

    # the discovery guard: a WRITING tool in the sweep directory must never be
    # admitted as a reach instrument. `reports/round-28/sweep/repin.py` is the
    # live control — it re-freezes baselines and manifests, so executing it to
    # measure reach would write filed artifacts.
    repin = ROOT / "reports/round-28/sweep/repin.py"
    if repin.is_file():
        check("the guard detects a writing tool",
              writes(str(repin)),
              "repin.py shows no write marker; the guard would admit it")
        check("find_sweep() admits only read-only reporters",
              all(not writes(p) for p in find_sweep()),
              "a writing tool is in the discovered instrument set")
        check("find_sweep() excludes repin.py",
              str(repin) not in find_sweep())

    # live controls on the real tree: the classifier must fire on a real D4
    # surface and must NOT fire on the D2 drill's hold set.
    d4_hold = ROOT / "examples/culture-d4/expected-holds.json"
    d2_hold = ROOT / "examples/culture-d2/expected-holds.json"
    if d4_hold.is_file():
        check("live control: the D4 hold set is a D4 surface",
              classify(str(d4_hold), "G")["pins_d4"], "digest identity failed")
    if d2_hold.is_file():
        check("live control: the D2 hold set is NOT a D4 surface",
              not classify(str(d2_hold), "G")["pins_d4"], "the D2 drill's hold set fired")
    profile = ROOT / "tools/gates/typed-pipelines.json"
    if profile.is_file():
        check("live control: typed-pipelines.json is a D4 surface",
              classify(str(profile), "F")["pins_d4"])

    for name, ok, detail in checks:
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else ": " + detail))
    failures = sum(1 for _, ok, _ in checks if not ok)
    print(f"selftest: {len(checks) - failures}/{len(checks)} checks passed")
    return 1 if failures else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="o37-sweep-inventory-audit.py", description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--json", action="store_true", help="emit one JSON document")
    parser.add_argument("--selftest", action="store_true",
                        help="run the in-memory and live controls and exit")
    parser.add_argument("--tmp-parent", default="/var/tmp/kotodama-r28-o37",
                        help="TMPDIR for the sweep run; must be outside the repo")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()

    tmp_parent = os.path.realpath(args.tmp_parent)
    root_real = os.path.realpath(str(ROOT))
    if tmp_parent == root_real or root_real in Path(tmp_parent).parents:
        print("COULD-NOT-EVALUATE: --tmp-parent is inside the repo; the sweep's own "
              "mirror refuses an in-repo temporary root", file=sys.stderr)
        return 2
    os.makedirs(tmp_parent, exist_ok=True)

    try:
        receipt = audit(tmp_parent)
    except OSError as error:
        print(f"COULD-NOT-EVALUATE: {type(error).__name__}: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(receipt, indent=1, sort_keys=True))
    else:
        for line in render(receipt):
            print(line)
    if not receipt["sweep_instruments"]:
        return 2
    return 1 if receipt["missed"] else 0


if __name__ == "__main__":
    sys.exit(main())
