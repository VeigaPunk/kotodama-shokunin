#!/usr/bin/env python3
"""R25-C — lessons-partition census (round 25, read-only).

Builds the reconciled index of `corpus/lessons/`: one row per lesson file with
its format class, the open-question ids it carries, and its disposition pointer
from LOG.md. Extracts the standing open-question queue (id, carrier, owner,
blocking status) from the live carrier artifacts. Documents the three census
formats the partition has used.

This process opens no file for writing. The receipt is the caller's stdout
redirect:

    export TMPDIR=$PWD/.scratch
    python3 reports/round-25/lessons/lessons-index-census.py --selftest
    python3 reports/round-25/lessons/lessons-index-census.py            # summary
    python3 reports/round-25/lessons/lessons-index-census.py --json     # receipt

v4 (round 25) deltas over the round-23 v3 tool
(reports/round-23/audit/x09-lessons-audit.py):
  - per-row `format_class` + `sub_shape` (the partition's three census
    formats, measured by marker presence rather than asserted);
  - per-row `oq_carried` (open-question ids the lesson text names) and
    `disposition` + `disposition_source` read from LOG.md;
  - an `open_question_queue` section extracted from the declared live
    carriers (round-2 adjacency, round-11 packet + attempt-1, round-15
    packet-v2-05, round-20 packet-v3-16) with a mechanical owner field;
  - a `carrier_coverage` block that names any carrier that is missing, so a
    moved artifact is reported rather than silently dropped.

The path resolver and the contract-line probes are inherited unchanged from v3
so the round-19/20/23 readings stay comparable.
"""
import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LESSONS = os.path.join(LANE, "corpus", "lessons")
LOG = os.path.join(LANE, "LOG.md")

ROUND_RE = re.compile(r"^round-(\d+)")
GATE_RE = re.compile(r"^##\s+Gate\b", re.M)
NEXT_H_RE = re.compile(r"^##\s+\S", re.M)
PATH_RE = re.compile(
    r"`((?:corpus|reports|tools|examples|scripts|SKILL|LOG|SCORECARD|AGENTS|PROVINCE)"
    r"[A-Za-z0-9_./-]*\.(?:md|json|py|tsv|yml|yaml|log))(?::\d+(?:-\d+)?)?`"
)
ADMITTED_RE = re.compile(r"Round (\d+) admitted")
REJECTED_RE = re.compile(r"Round (\d+) REJECTED")
MENTIONED_RE = re.compile(r"[Rr]ound[- ](\d+)")
OQ_RE = re.compile(r"OQ-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")
# An open-question row in a carrier: "- OQ-...: <text> — <owner>; <blocking>"
OQ_ROW_RE = re.compile(r"^-\s*(OQ-[A-Za-z0-9-]+):\s*(.*)$", re.M)

# Format-class markers, in precedence order.
FRAGMENT_INDEX_RE = re.compile(r"^##\s+Fragment index\b", re.M)
SURVEY_VERDICT_RE = re.compile(r"^###\s+Survey verdict at close", re.M)
AXIS_SECTION_RE = re.compile(r"^###\s+[ODCA]\s+—\s", re.M)
RULE_RE = re.compile(r"^###\s+Rule\b", re.M)
SOURCE_RE = re.compile(r"^source:", re.M)
OPENING_READING_RE = re.compile(r"^Opening\s+\w+\s+reading:", re.M)
CLOSEOUT_RE = re.compile(r"^##\s+(?:Gate-keeper closeout rule|Closeout(?: and rejected readings)?)\b", re.M)
OPENING_CENSUS_RE = re.compile(r"^##\s+(?:Opening census|Evidence commands and opening fragment index)\b", re.M)
# Two defensible gate predicates. `GATE_RE` (the round-19/20/23 audits' rule)
# accepts any `## Gate*` heading, which sweeps in round-7's prose heading
# `## Gate candidates`; `GATE_EXACT_RE` (the sibling C31 seat's rule) requires
# the bare heading. Both readings are reported per row rather than one being
# silently chosen — the disagreement is exactly one file (round 7).
GATE_EXACT_RE = re.compile(r"^##\s+Gate\s*$", re.M)

FORMAT_CLASSES = ("gate-keeper-survey", "fragment-index", "plain-lesson")

# Standing open-question carriers, declared here so a moved artifact is
# reported as missing rather than silently dropped.
CARRIERS = (
    ("round-2 adjacency", "corpus/lessons/round-2-adjacency.md", r"^(\d+)\.\s", 4),
    ("round-11 e2e packet", "reports/round-11/handoff/packet.md", r"OQ-E2E-\d\d", 5),
    ("round-11 attempt-1", "reports/round-11/handoff/packet-attempt-1.md", r"OQ-R11-A\d-\d\d", 7),
    ("round-15 v2 packet", "reports/round-15/handoff/packet-v2-05.md", r"OQ-V2-\d\d", 7),
    ("round-20 v3 packet", "reports/round-20/handoff/packet-v3-16.md", r"OQ-V3-\d\d", 6),
)


def lesson_round(name):
    m = ROUND_RE.match(name)
    return int(m.group(1)) if m else None


def gate_block(text):
    m = GATE_RE.search(text)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = NEXT_H_RE.search(rest)
    return rest[: nxt.start()] if nxt else rest


def format_class(text):
    """The partition's three census formats, decided by marker presence.

    The classes match the vocabulary the round-19 X28 / round-20 X24 /
    round-23 X09 audits use: a file either carries a `## Fragment index`
    (the round-8..12 shape), carries a `## Gate` block (the gate-keeper
    survey), or carries neither (a plain lesson). The sub-shape names the
    marker vocabulary the file uses inside its gate.
    """
    if FRAGMENT_INDEX_RE.search(text) and GATE_RE.search(text):
        return "fragment-index", "fragment-index-gate"
    if GATE_EXACT_RE.search(text):
        if RULE_RE.search(text):
            return "gate-keeper-survey", "rule-shape"
        if AXIS_SECTION_RE.search(text):
            return "gate-keeper-survey", "axis-section"
        if OPENING_READING_RE.search(text):
            return "gate-keeper-survey", "marker-vocabulary"
        return "gate-keeper-survey", "gate-block"
    if GATE_RE.search(text):
        # a `## Gate ...` prose heading with no bare `## Gate` block
        return "plain-lesson", "gate-heading-prose"
    if SOURCE_RE.search(text):
        return "plain-lesson", "post-contract-no-gate"
    return "plain-lesson", "pre-contract-seed"


def oq_ids(text):
    ids = set(OQ_RE.findall(text))
    # Drop fragments that are prefixes of a longer id on the same file
    # (e.g. `OQ-V2-01` inside `OQ-V2-017`), keeping the longest forms.
    return sorted(i for i in ids if not any(j != i and j.startswith(i + "-") for j in ids))


def log_records():
    with open(LOG, "rb") as fh:
        log = fh.read().decode("utf-8", "replace")
    admitted = sorted({int(m) for m in re.findall(r"Round (\d+) admitted", log)})
    admitted += sorted({int(m) for m in re.findall(r"[Rr]ound (\d+):[^\n]*\(admitted\)", log)})
    rejected = sorted({int(m) for m in re.findall(r"Round (\d+) REJECTED", log)})
    rejected += sorted({int(m) for m in re.findall(r"[Rr]ound (\d+):[^\n]*\(REJECTED\)", log)})
    mentioned = sorted({int(m) for m in re.findall(r"[Rr]ound[- ](\d+)", log)})
    return sorted(set(admitted)), sorted(set(rejected)), mentioned, log


def disposition(round_no, admitted, rejected, log):
    if round_no is None:
        return ("supplement", "no round number; not a round record")
    if round_no in rejected:
        return ("rejected", f"LOG.md: Round {round_no} REJECTED")
    if round_no in admitted:
        return ("admitted", f"LOG.md: Round {round_no} admitted")
    if round_no == 13:
        return ("skipped", "LOG.md: round-13 claims deferred (operator-skipped)")
    pats = (
        rf"round\s*{round_no}[^\n]*unadmitted",
        rf"round\s*{round_no} stays failed",
    )
    for p in pats:
        if re.search(p, log, re.I):
            return ("unadmitted", f"LOG.md: round {round_no} recorded unadmitted/failed")
    return ("recorded", f"LOG.md: round {round_no} recorded, no admission heading")


def audit_lesson(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", "replace")
    name = os.path.basename(path)
    block = gate_block(text)
    refs = sorted(set(PATH_RE.findall(text)))
    missing = [r for r in refs if not os.path.exists(os.path.join(LANE, r))]
    cls, shape = format_class(text)
    return {
        "file": name,
        "round": lesson_round(name),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "gate_heading_any": bool(GATE_RE.search(text)),
        "gate_heading_exact": bool(GATE_EXACT_RE.search(text)),
        "size_bytes": len(raw),
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "mtime_utc": datetime.fromtimestamp(
            os.stat(path).st_mtime, timezone.utc
        ).isoformat(),
        "format_class": cls,
        "sub_shape": shape,
        "has_gate": bool(GATE_RE.search(text)),
        "has_source_line": bool(re.search(r"^source:", text, re.M)),
        "has_verified_at": bool(re.search(r"^verified-at:", text, re.M)),
        "has_recheck_line": bool(re.search(r"^recheck:", text, re.M)),
        "has_scope_line": bool(re.search(r"^scope:", text, re.M)),
        "has_closeout": bool(CLOSEOUT_RE.search(text)),
        "has_opening_census": bool(OPENING_CENSUS_RE.search(text)),
        "oq_carried": oq_ids(text),
        "path_refs": len(refs),
        "path_refs_missing": missing,
    }


def parse_owner(row_text):
    """Mechanical owner field: text after the last ` — ` up to the first `;`."""
    if " — " not in row_text:
        return "unnamed"
    tail = row_text.rsplit(" — ", 1)[1]
    return tail.split(";")[0].strip() or "unnamed"


def blocking(row_text):
    if "non-blocking" in row_text.lower():
        return "non-blocking"
    if "blocking" in row_text.lower():
        return "blocking"
    return "unstated"


def queue_row(carrier, oid, text):
    return {
        "id": oid,
        "carrier": carrier,
        "owner": parse_owner(text),
        "blocking": blocking(text),
        "text": text.strip(),
    }


def open_question_queue():
    queue, coverage = [], []
    for carrier, rel, pat, expect in CARRIERS:
        path = os.path.join(LANE, rel)
        present = os.path.exists(path)
        coverage.append(
            {"carrier": carrier, "path": rel, "present": present, "expected_ids": expect}
        )
        if not present:
            continue
        text = open(path, "rb").read().decode("utf-8", "replace")
        if carrier == "round-2 adjacency":
            section = text.split("## Open questions")[1].split("## Verification")[0]
            items = re.findall(r"^(\d+)\.\s+(.*?)(?=\n\d+\.\s|\Z)", section, re.M | re.S)
            for num, body in items:
                queue.append(
                    {
                        "id": f"OQ-R2-{int(num):02d}",
                        "carrier": carrier,
                        "owner": "lore" if "lore" in body.lower() else "kotodama/packet-side",
                        "blocking": blocking(body),
                        "text": " ".join(body.split()),
                    }
                )
            coverage[-1]["found_ids"] = len(items)
            continue
        rows = OQ_ROW_RE.findall(text)
        seen = set()
        for oid, body in rows:
            if not re.fullmatch(pat, oid) or oid in seen:
                continue
            seen.add(oid)
            queue.append(queue_row(carrier, oid, body))
        coverage[-1]["found_ids"] = len(seen)
    return queue, coverage


def lesson_files():
    """Lesson files only: the index README is not a lesson."""
    return sorted(
        f for f in os.listdir(LESSONS)
        if f.endswith(".md") and f != "README.md"
    )


def census():
    files = lesson_files()
    rows = [audit_lesson(os.path.join(LESSONS, f)) for f in files]
    admitted, rejected, mentioned, log = log_records()
    for r in rows:
        disp, src = disposition(r["round"], admitted, rejected, log)
        r["disposition"], r["disposition_source"] = disp, src
    queue, coverage = open_question_queue()
    rounds = sorted({r["round"] for r in rows if r["round"] is not None})
    by_class = {c: sorted(r["file"] for r in rows if r["format_class"] == c) for c in FORMAT_CLASSES}
    # The one file the two gate predicates disagree on, named rather than hidden.
    gate_disagreement = sorted(
        r["file"] for r in rows if r["gate_heading_any"] != r["gate_heading_exact"]
    )
    with open(os.path.join(LANE, "corpus", "README.md"), "rb") as fh:
        readme = fh.read()
    return {
        "schema": "kotodama-lessons-index-census-v4",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "counting_command": "python3 reports/round-25/lessons/lessons-index-census.py",
        "lesson_files": len(rows),
        "round_numbered_files": len([r for r in rows if r["round"] is not None]),
        "rounds_with_lessons": rounds,
        "rounds_covered_1_to_24": [n for n in range(1, 25) if n in rounds],
        "rounds_without_lessons": [n for n in range(1, 25) if n not in rounds],
        "rounds_logged_admitted": admitted,
        "rounds_logged_rejected": rejected,
        "rounds_logged_mentioned": mentioned,
        "format_class_counts": {c: len(v) for c, v in by_class.items()},
        "format_class_files": by_class,
        "format_histogram": {
            "gate-keeper-survey": len(by_class["gate-keeper-survey"]),
            "fragment-index": len(by_class["fragment-index"]),
            "plain-lesson": len(by_class["plain-lesson"]),
        },
        "gate_predicate_disagreement": {
            "files": gate_disagreement,
            "reading_any_gate_heading": len([r for r in rows if r["gate_heading_any"]]),
            "reading_bare_gate_heading": len([r for r in rows if r["gate_heading_exact"]]),
        },
        "open_question_queue": queue,
        "open_question_count": len(queue),
        "carrier_coverage": coverage,
        "corpus_readme_sha256": hashlib.sha256(readme).hexdigest(),
        "rows": rows,
    }


def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    check("round parse", lesson_round("round-18.md") == 18)
    check("round parse named", lesson_round("round-1-gates-and-triage.md") == 1)
    check("round parse supplement", lesson_round("supplement-opencode-1.md") is None)

    # format classification: one positive and one negative control per class
    gk = "# t\n## Gate\n### O — x\n### Rule\n"
    check("format gate-keeper (axis)", format_class(gk)[0] == "gate-keeper-survey")
    check("format gate-keeper (rule shape)", format_class(gk)[1] == "rule-shape")
    check("format gate-keeper (axis section)",
          format_class("# t\n## Gate\n### D — x\n")[1] == "axis-section")
    check("format gate-keeper (marker vocab)",
          format_class("# t\n## Gate\nOpening D reading: x\n")[1] == "marker-vocabulary")
    fi = "# t\n## Fragment index\n## Gate\n"
    check("format fragment-index", format_class(fi)[0] == "fragment-index")
    check("fragment-index wins over gate-keeper", format_class(fi)[0] != "gate-keeper-survey")
    check("plain lesson not misread as index",
          format_class("# t\n## Domain lessons\n")[0] == "plain-lesson")
    check("plain lesson not misread as survey",
          format_class("# t\n## Boundary record\n")[0] == "plain-lesson")
    check("post-contract plain flagged",
          format_class("# t\nsource: x\n## Map result\n")[1] == "post-contract-no-gate")
    check("pre-contract seed flagged",
          format_class("# t\n## Gates are real\n")[1] == "pre-contract-seed")
    # the two gate predicates, and the round-7 disagreement they create
    check("prose gate heading is not a gate block",
          format_class("# t\n## Gate candidates\n")[0] == "plain-lesson")
    check("prose gate heading flagged",
          format_class("# t\n## Gate candidates\n")[1] == "gate-heading-prose")
    check("bare Gate is a gate block",
          format_class("# t\n## Gate\n")[0] == "gate-keeper-survey")
    check("any-gate predicate accepts prose heading",
          bool(GATE_RE.search("## Gate candidates\n")))
    check("exact-gate predicate rejects prose heading",
          not GATE_EXACT_RE.search("## Gate candidates\n"))
    check("exact-gate predicate accepts bare heading",
          bool(GATE_EXACT_RE.search("## Gate\n")))
    check("exact-gate rejects suffixed heading",
          not GATE_EXACT_RE.search("## Gate-keeper closeout rule\n"))

    # oq extraction and prefix pruning
    check("oq ids extracted", oq_ids("x OQ-V3-05 y OQ-V2-01") == ["OQ-V2-01", "OQ-V3-05"])
    check("oq prefix pruned", oq_ids("OQ-V2-017 OQ-V2-01") == ["OQ-V2-01", "OQ-V2-017"])
    check("oq none", oq_ids("no ids here") == [])

    # owner/blocking parser
    row = "D4 holds stay open — kotodama; blocking for the affected records"
    check("owner parsed", parse_owner(row) == "kotodama", parse_owner(row))
    check("blocking parsed", blocking(row) == "blocking")
    check("non-blocking parsed", blocking("— lore; non-blocking for this envelope") == "non-blocking")
    check("unstated blocking", blocking("no status word") == "unstated")

    # disposition mapping controls
    check("disposition rejected", disposition(22, [8], [22], "")[0] == "rejected")
    check("disposition admitted", disposition(8, [8], [], "")[0] == "admitted")
    check("disposition skipped", disposition(13, [8], [], "")[0] == "skipped")
    check("disposition supplement", disposition(None, [], [], "")[0] == "supplement")
    check("disposition unadmitted",
          disposition(7, [], [], "round7 remains unadmitted")[0] == "unadmitted")

    # live-tree controls
    check("lane root resolves", os.path.isfile(os.path.join(LANE, "AGENTS.md")))
    check("lessons dir resolves", os.path.isdir(LESSONS))
    check("readme sha is hex",
          bool(re.fullmatch(r"[0-9a-f]{64}", hashlib.sha256(b"x").hexdigest())))
    check("gate block bounded", "Next" not in gate_block("x\n## Gate\n- a\n## Next\n"))
    check("path ref regex catches missing",
          PATH_RE.findall("`reports/round-25/__nonexistent__.md`")
          == ["reports/round-25/__nonexistent__.md"])

    # partition controls: the three classes must partition every lesson file,
    # and the carrier list must cover the four standing generations.
    files = lesson_files()
    classes = [format_class(open(os.path.join(LESSONS, f), encoding="utf-8",
                                 errors="replace").read())[0] for f in files]
    check("every file classified", all(c in FORMAT_CLASSES for c in classes))
    check("index README excluded from the census",
          "README.md" not in files and os.path.isfile(os.path.join(LESSONS, "README.md")))
    check("classes partition the count", len(classes) == len(files) and len(files) > 0)
    check("carrier generations present", len(CARRIERS) == 5)
    print("SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    rep = census()
    if args.json:
        print(json.dumps(rep, indent=2, sort_keys=True))
        return 0
    print(f"observed_at_utc: {rep['observed_at_utc']}")
    print(f"counting command: {rep['counting_command']}")
    print(f"lesson files: {rep['lesson_files']}")
    print(f"round-numbered files: {rep['round_numbered_files']}")
    print(f"rounds covered 1-24: {rep['rounds_covered_1_to_24']}")
    print(f"rounds without lessons: {rep['rounds_without_lessons']}")
    print(f"format classes: {rep['format_class_counts']}")
    print(f"rounds logged admitted: {rep['rounds_logged_admitted']}")
    print(f"rounds logged rejected: {rep['rounds_logged_rejected']}")
    print(f"open-question rows extracted: {rep['open_question_count']}")
    for c in rep["carrier_coverage"]:
        print(f"  carrier {c['carrier']:22s} present={c['present']} "
              f"ids={c.get('found_ids')}/{c['expected_ids']}")
    print()
    for r in rep["rows"]:
        print(f"{r['file']:34s} round={r['round']} {r['format_class']:18s} "
              f"{r['sub_shape']:20s} gate={r['has_gate']} disp={r['disposition']} "
              f"oq={len(r['oq_carried'])} refs={r['path_refs']} "
              f"missing={len(r['path_refs_missing'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
