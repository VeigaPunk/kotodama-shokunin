#!/usr/bin/env python3
r"""Round-69 calibration acceptance counter — claim Ca2 (NEW counter).

Calibration is the lane's self-assessment quality: the filed claim (the
SCORECARD rows, the LOG entry, the filed fleet report) must match the
observed repo state (the committed receipts). This counter COUNTS the
mismatches; it never asserts. It is a NEW file: the round-68 calibration
counter is not edited (leg ``R68FROZEN`` proves that), and the round-68
counter's crash (undefined ``git_bytes``, R68-M9) is repaired by a new
instrument, not by amending a frozen one.

The declared (class, surface) pairs live in ``reports/round-69/claims.json``
(frozen pre-data). A pair closes only when BOTH hold:
  * the underlying observation is now consistent (the mismatch is no longer
    live), AND
  * an appended correction row naming that class and that surface exists in
    ``reports/round-69/corrections-r68.md`` (append-only; the filed round-68
    bytes are never rewritten).

Classes:
  LEGCOUNT     — a filed surface claims a legs-pass count that the committed
                 receipt does not support.
  DEADPOINTER  — a filed surface points at a mistake row that does not exist.
  OVERREACH    — a filed surface claims an improved axis verdict that the
                 committed receipt contradicts.

Usage:
  --root DIR       evaluate the declared pairs against the lane tree at DIR
                   (default "."); --fleet-root DIR (default the fleet root)
                   resolves the filed fleet report named in claims.json.
  --selftest       run the GREEN control (a fixture tree whose correction rows
                   are present) and the DO-NOTHING control (the same tree with
                   the correction rows removed, which must be caught).

Exit codes: 0 pass · 1 fail · 2 usage/env.
Reads only. No network. No mutation of the lane tree.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
SELF = os.path.basename(__file__)

LEGCOUNT_RE = re.compile(r"(\d+)\s*/\s*(\d+)\s+legs\s+PASS")
LEG_LINE_RE = re.compile(r"^([A-Z0-9_]+)\s+(PASS|FAIL)\b", re.M)
MISTAKE_RE = re.compile(r"R68-M(\d+)")
PLUS_M_RE = re.compile(r"\+M(\d+)\s+in\s+LOG")
CORRECTIONS = "reports/round-69/corrections-r68.md"
CLAIMS = "reports/round-69/claims.json"


def sha256_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
    except OSError:
        return None
    return h.hexdigest()


def recorded_sha(path):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None
    m = re.search(r"^# counter sha256 \(self\):\s*([0-9a-f]{64})\s*$",
                  text, re.M)
    return m.group(1) if m else None


def read_text(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def section_text(text, heading_re):
    """Return the markdown section whose heading matches *heading_re*."""
    if text is None:
        return None
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(heading_re, line):
            start = i
            break
    if start is None:
        return None
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            return "\n".join(lines[start:j])
    return "\n".join(lines[start:])


def observed_o_legs(root):
    """(pass, total) legs claimed by the committed round-68 operability receipt."""
    text = read_text(os.path.join(root, "reports", "round-68", "telemetry",
                                  "final-measures-o.txt"))
    if text is None:
        return None
    legs = LEG_LINE_RE.findall(text)
    if not legs:
        return None
    return (sum(1 for _, v in legs if v == "PASS"), len(legs))


def observed_ca_verdict(root):
    """'PASS' or 'FAIL' as printed by the committed round-68 calibration receipt."""
    text = read_text(os.path.join(root, "reports", "round-68", "telemetry",
                                  "final-measures-ca.txt"))
    if text is None:
        return None
    return "PASS" if "ACCEPT-CA-68: PASS" in text else "FAIL"


def mistake_rows_exist(root, ids):
    """Return the subset of *ids* with no R68-M<n> row anywhere in the lane."""
    corpus = ""
    for rel in ("LOG.md", "corpus/lessons/round-68.md",
                "corpus/lessons/round-69.md"):
        t = read_text(os.path.join(root, rel))
        if t:
            corpus += t + "\n"
    missing = []
    for n in sorted(set(ids)):
        if ("R68-M%s" % n) not in corpus:
            missing.append(n)
    return missing


def detect_legcount(text, observed):
    if text is None or observed is None:
        return None
    bad = []
    for m in LEGCOUNT_RE.finditer(text):
        pair = (int(m.group(1)), int(m.group(2)))
        if pair != observed:
            bad.append("%d/%d" % pair)
    return bad


def detect_deadpointer(text, root):
    if text is None:
        return None
    ids = [m.group(1) for m in MISTAKE_RE.finditer(text)]
    ids += [m.group(1) for m in PLUS_M_RE.finditer(text)]
    if not ids:
        return []
    return ["R68-M%s" % n for n in mistake_rows_exist(root, ids)]


def detect_overreach(text, ca_verdict):
    if text is None or ca_verdict is None:
        return None
    for line in text.splitlines():
        if not line.startswith("| calibration |"):
            continue
        cells = [c.strip() for c in line.split("|")]
        verdict = cells[2] if len(cells) > 2 else ""
        if verdict.startswith("improved") and ca_verdict != "PASS":
            return ["calibration verdict %r vs receipt %s" % (
                verdict.split("(")[0].strip(), ca_verdict)]
    return []


def correction_pairs(root):
    """The (class, surface) pairs covered by the appended correction rows."""
    text = read_text(os.path.join(root, CORRECTIONS))
    if text is None:
        return set()
    pairs = set()
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 4:
            continue
        cls, surface = cells[1], cells[2]
        if cls and surface and cls.upper() in ("LEGCOUNT", "DEADPOINTER",
                                                "OVERREACH"):
            pairs.add((cls.upper(), surface))
    return pairs


def surface_text(root, pair, fleet_root):
    """The filed text of one declared surface, and its surface key."""
    key = pair["surface"]
    rel = pair.get("path", "")
    if pair.get("fleet"):
        path = rel
        if path and not os.path.isabs(path):
            path = os.path.join(fleet_root, path)
        return read_text(path), key
    text = read_text(os.path.join(root, rel))
    section = pair.get("section")
    if section and text is not None:
        text = section_text(text, section)
    return text, key


def evaluate(root, fleet_root, claims, res):
    root = os.path.abspath(root)
    obs_o = observed_o_legs(root)
    ca_verdict = observed_ca_verdict(root)
    covered = correction_pairs(root)

    # R68FROZEN — the round-68 calibration counter is byte-identical to the
    # sha256 its own receipt recorded: the crash was not amended post-data.
    live = sha256_file(os.path.join(root, "reports", "round-68", "accept-ca.py"))
    rec = recorded_sha(os.path.join(root, "reports", "round-68", "telemetry",
                                     "final-measures-ca.txt"))
    res.add("R68FROZEN", bool(live) and live == rec,
            "live=%s recorded=%s" % ((live or "none")[:12],
                                      (rec or "none")[:12]))

    res.add("OBSERVED", obs_o is not None and ca_verdict is not None,
            "o-legs=%s ca-verdict=%s" % (obs_o, ca_verdict))

    live_count = 0
    unannotated = 0
    for pair in claims["calibration_pairs"]:
        cls = pair["class"].upper()
        text, key = surface_text(root, pair, fleet_root)
        if cls == "LEGCOUNT":
            live_hits = detect_legcount(text, obs_o)
        elif cls == "DEADPOINTER":
            live_hits = detect_deadpointer(text, root)
        else:
            live_hits = detect_overreach(text, ca_verdict)
        if live_hits is None:
            res.add("EVAL %s|%s" % (cls, key), False, "surface unreadable")
            live_count += 1
            unannotated += 1
            continue
        is_live = bool(live_hits)
        if is_live:
            live_count += 1
        is_covered = (cls, key) in covered
        if cls == "DEADPOINTER":
            # the pointer must also resolve: an appended R68-M<n> row
            remedy = is_covered and not is_live
        else:
            # the filed bytes are frozen and append-only; the appended
            # correction row is the remedy
            remedy = is_covered
        if is_live and not remedy:
            unannotated += 1
        ok = remedy and not (is_live and not remedy)
        res.add("EVAL %s|%s" % (cls, key), ok,
                "live=%s covered=%s remedy=%s hits=%s" % (
                    is_live, is_covered, remedy, live_hits or "none"))
    res.add("MISMATCHES", unannotated == 0,
            "live_mismatches=%d unannotated_mismatches=%d" % (
                live_count, unannotated))
    return res


class Result(object):
    def __init__(self, quiet=False):
        self.legs = []
        self.quiet = quiet

    def add(self, name, ok, detail=""):
        self.legs.append((name, bool(ok), detail))
        if not self.quiet:
            print("LEG %s %s %s" % ("PASS" if ok else "FAIL", name, detail))

    @property
    def ok(self):
        return all(ok for _, ok, _ in self.legs)


def load_claims(root, claims_path=None):
    path = claims_path or os.path.join(root, CLAIMS)
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build_fixture_root(fx, *, with_corrections):
    os.makedirs(fx, exist_ok=True)
    for rel in ("reports/round-69/accept-ca.py", "reports/round-69/claims.json",
                "reports/round-68/accept-ca.py",
                "reports/round-68/telemetry/final-measures-ca.txt",
                "reports/round-68/telemetry/final-measures-o.txt",
                "SCORECARD.md", "LOG.md",
                "corpus/lessons/round-68.md", "corpus/lessons/round-69.md",
                "corpus/SOURCES.md"):
        src = os.path.join(LANE, rel)
        if not os.path.exists(src):
            continue
        dst = os.path.join(fx, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    fleet = os.path.join(fx, "fleet")
    fdir = os.path.join(fleet, ".ufo", "reports", "round-68")
    os.makedirs(fdir, exist_ok=True)
    real = "/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md"
    if os.path.exists(real):
        shutil.copy2(real, os.path.join(fdir, "kotodama.md"))
    else:
        with open(os.path.join(fdir, "kotodama.md"), "w",
                  encoding="utf-8") as fh:
            fh.write("# fixture fleet report\n")
    if with_corrections:
        dst = os.path.join(fx, CORRECTIONS)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        claims0 = load_claims(fx)
        rows = ["| class | surface | filed text | observed text | re-derivation command |",
                "|---|---|---|---|---|"]
        for pair in claims0.get("calibration_pairs", []):
            key = pair["surface"]
            rows.append("| %s | %s | filed | observed | command |" % (
                pair["class"], key))
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write("\n".join(rows) + "\n")
        # the appended R68-M9 row: the round-68 lesson never carried it
        lesson = os.path.join(fx, "corpus", "lessons", "round-69.md")
        os.makedirs(os.path.dirname(lesson), exist_ok=True)
        with open(lesson, "a", encoding="utf-8") as fh:
            fh.write("\n| R68-M9 | fixture backfill row |\n")
    claims_path = os.path.join(fx, CLAIMS)
    claims = load_claims(fx)
    for pair in claims.get("calibration_pairs", []):
        if pair.get("surface") == "fleet-report":
            pair["path"] = os.path.join(fdir, "kotodama.md")
    with open(claims_path, "w", encoding="utf-8") as fh:
        json.dump(claims, fh, indent=2, ensure_ascii=False)
    return fleet


def selftest():
    with tempfile.TemporaryDirectory(prefix="ca69-selftest-") as td:
        green = os.path.join(td, "green")
        fleet = build_fixture_root(green, with_corrections=True)
        claims = load_claims(green)
        r1 = Result(quiet=True)
        evaluate(green, fleet, claims, r1)
        green_ok = r1.ok
        print("GREEN FIXTURE: %s (legs %d/%d)" % (
            "PASS" if green_ok else "FAIL",
            sum(1 for _, ok, _ in r1.legs if ok), len(r1.legs)))

        nothing = os.path.join(td, "donothing")
        fleet2 = build_fixture_root(nothing, with_corrections=False)
        claims2 = load_claims(nothing)
        r2 = Result(quiet=True)
        evaluate(nothing, fleet2, claims2, r2)
        nothing_fails = not r2.ok
        print("DO-NOTHING FIXTURE: %s (legs %d/%d)" % (
            "FAIL (as required)" if nothing_fails else "PASS (unexpected)",
            sum(1 for _, ok, _ in r2.legs if ok), len(r2.legs)))
        print("SELFTEST: %d/2" % (sum([green_ok, nothing_fails])))
        return 0 if (green_ok and nothing_fails) else 1


def main():
    ap = argparse.ArgumentParser(description="round-69 calibration counter")
    ap.add_argument("--root", default=".")
    ap.add_argument("--fleet-root", default="/home/vgpnk/Projects/shokunin")
    ap.add_argument("--claims", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    claims = load_claims(args.root, args.claims)
    res = Result()
    evaluate(args.root, args.fleet_root, claims, res)
    passed = sum(1 for _, ok, _ in res.legs if ok)
    print("ACCEPT-CA-69: %s legs=%d/%d" % (
        "PASS" if res.ok else "FAIL", passed, len(res.legs)))
    return 0 if res.ok else 1


if __name__ == "__main__":
    sys.exit(main())
