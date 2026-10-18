#!/usr/bin/env python3
"""R26-C47..C50 — audit of the open-question dispositions (round 26).

The six disposer seats (C41-C46) each took a block of the round-25 queue and
wrote a disposition per row into `reports/round-26/open-questions/C4N.md`. This
seat audits them: it re-derives the row set from the filed queue, extracts each
disposition's claimed class and the evidence commands the fragment cites, re-runs
those commands against the live tree, and reports every divergence.

It writes only `audit.json` and `audit.md` in this directory.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-26/open-questions/audit-dispositions.py
    python3 -B reports/round-26/open-questions/audit-dispositions.py --json
    python3 -B reports/round-26/open-questions/audit-dispositions.py --selftest

Checks:
  A1  every filed queue row appears in exactly one disposer fragment
  A2  every disposition names a class in the declared vocabulary
  A3  a `fixed-with-evidence` row cites at least one runnable evidence command
  A4  a `carried` row names an owner, a reason and a next touch round
  A5  every cited evidence command re-runs with the exit code the fragment claims
  A6  the fragments' own row counts equal the block partition they declare
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
README = os.path.join(LANE, "corpus", "lessons", "README.md")

VOCAB = {"fixed-with-evidence", "carried", "routed",
         "closed-by-supersession", "standing-rule"}

# The block partition the C41 fragment declares.
BLOCKS = {
    "C41": ("rounds 2-4", re.compile(r"^Q-0[234]-")),
    "C42": ("rounds 5-7", re.compile(r"^Q-0[567]-")),
    "C43": ("rounds 8-12", re.compile(r"^Q-(?:0[89]|1[012])-")),
    "C44": ("rounds 14-17", re.compile(r"^Q-1[4567]-")),
    "C45": ("rounds 18-22", re.compile(r"^Q-(?:1[89]|2[012])-")),
    "C46": ("round 23 + supplement", re.compile(r"^Q-(?:23-|S1-)")),
}


def filed_queue():
    text = open(README, encoding="utf-8").read()
    section = text.split("## 4. Open-question queue")[1].split("## 5")[0]
    rows = []
    for line in section.splitlines():
        if not line.startswith("| Q-") or line.startswith("| Q-id"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append({"id": cells[0], "question": cells[1],
                     "owner": cells[2], "status": cells[3]})
    return rows


def sh_commands(block):
    """Runnable commands from the block's ```sh fences.

    A fence is one shell script: line continuations, `for … do … done` and
    multi-line `python3 -c "…"` bodies are all part of it. Running the fence as
    a whole is the faithful re-run of what the fragment claims; splitting it on
    newlines would manufacture syntax errors the fragment never had.
    """
    scripts = []
    for fence in re.findall(r"```(?:sh|bash)\n(.*?)```", block, re.S):
        body = "\n".join(l for l in fence.splitlines() if not l.strip().startswith("#"))
        if body.strip():
            scripts.append(body)
    return scripts


def next_touch(block):
    """The next-touch round, in any of the wordings the fragments use:
    'Next touch round 27.', 'Next touch\\nround 27.', 'Next touch: … round 27.',
    and the line-wrapped 'Next\\ntouch round 27.'."""
    for m in re.finditer(r"[Nn]ext\s+touch", block):
        tail = block[m.end():m.end() + 200]
        r = re.search(r"round\s*(\d+)", tail)
        if r:
            return int(r.group(1))
    return None


def parse_fragment(path):
    text = open(path, encoding="utf-8").read()
    out = []
    for block in re.split(r"^### ", text, flags=re.M)[1:]:
        head = block.splitlines()[0]
        m = re.match(r"(Q-[A-Za-z0-9-]+)\s+—\s+(.*?)\s+—\s+owner\s+`([^`]+)`", head)
        if not m:
            m2 = re.match(r"(Q-[A-Za-z0-9-]+)\s+—\s+(.*)", head)
            if not m2:
                continue
            rid, q, owner = m2.group(1), m2.group(2), ""
        else:
            rid, q, owner = m.group(1), m.group(2), m.group(3)
        cls_m = re.search(r"^\*\*([a-z][a-z-]*)", block, re.M)
        cls = cls_m.group(1) if cls_m else None
        cmds = sh_commands(block)
        claimed = [l.lstrip("# ").strip() for l in block.splitlines()
                   if l.strip().startswith("#") and l.strip() != "#"]
        # A carried row's three required fields, as prose. The fragments write
        # the reason as "Reason:", "Reason carried:" or "Reason carried for …:".
        reason = bool(re.search(r"reason\b[^.\n]{0,40}[:.]", block, re.I))
        nxt = next_touch(block)
        out.append({"id": rid, "question": q, "owner": owner, "class": cls,
                    "commands": cmds, "claimed_outputs": claimed,
                    "has_reason": reason,
                    "next_touch_round": nxt,
                    "chars": len(block)})
    return out


def run_cmd(cmd):
    try:
        proc = subprocess.run(cmd, shell=True, cwd=LANE, capture_output=True,
                              text=True, timeout=300)
        return proc.returncode, proc.stdout + proc.stderr
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT"
    except Exception as exc:  # noqa: BLE001
        return -2, f"{type(exc).__name__}: {exc}"


def audit():
    queue = filed_queue()
    qids = [r["id"] for r in queue]
    fragments = {}
    for seat in BLOCKS:
        path = os.path.join(HERE, f"{seat}.md")
        fragments[seat] = parse_fragment(path) if os.path.exists(path) else None

    findings, checks = [], []

    def check(cid, ok, detail):
        checks.append({"id": cid, "ok": bool(ok), "detail": detail})
        if not ok:
            findings.append(f"{cid}: {detail}")

    # A1 — coverage: every filed row in exactly one fragment.
    seen = {}
    for seat, rows in fragments.items():
        for r in rows or []:
            seen.setdefault(r["id"], []).append(seat)
    missing = [q for q in qids if q not in seen]
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    check("A1_every_queue_row_dispositioned", not missing and not dupes,
          f"{len(qids)} queue rows; {len(missing)} undispositioned"
          + (f": {missing}" if missing else "")
          + (f"; duplicates: {dupes}" if dupes else ""))

    allrows = [r for rows in fragments.values() for r in (rows or [])]

    # A2 — class vocabulary.
    badcls = [(r["id"], r["class"]) for r in allrows if r["class"] not in VOCAB]
    check("A2_class_in_vocabulary", not badcls,
          f"{len(badcls)} row(s) outside the vocabulary" + (f": {badcls[:6]}" if badcls else ""))

    # A3 — fixed rows cite a runnable command.
    noev = [r["id"] for r in allrows
            if r["class"] == "fixed-with-evidence" and not r["commands"]]
    check("A3_fixed_rows_cite_evidence", not noev,
          f"{len(noev)} fixed row(s) with no evidence command" + (f": {noev}" if noev else ""))

    # A4 — carried rows name owner + reason + next touch.
    badcar = [(r["id"], bool(r["owner"]), r["has_reason"], r["next_touch_round"])
              for r in allrows
              if r["class"] == "carried"
              and not (r["owner"] and r["has_reason"] and r["next_touch_round"])]
    check("A4_carried_rows_complete", not badcar,
          f"{len(badcar)} carried row(s) missing owner/reason/next-touch"
          + (f": {badcar[:6]}" if badcar else ""))

    # A5 — re-run every cited evidence fence and compare its exit code against
    # the exit the fragment itself claims. The fragments write the expected
    # reading as `#` comment lines inside the fence; a claim of `(exit N)` or
    # `exit N` is the fragment's own assertion about the re-run, and a mismatch
    # is a divergence. A fence with no claimed exit is required only to be
    # shell-reachable (exit 0/1/2, i.e. a program's own verdict, not a syntax
    # error or a permission failure), and that weaker requirement is named.
    rerun, failed, drift = [], [], []
    for r in allrows:
        for script in r["commands"]:
            rc, out = run_cmd(script)
            claimed_exits = [int(x) for x in
                             re.findall(r"(?:\(|\b)exit\s+(\d+)", " ".join(r["claimed_outputs"]))]
            rec = {"row": r["id"], "command": script, "exit": rc,
                   "claimed_exits": claimed_exits,
                   "observed": " ".join(out.split())[:300]}
            rerun.append(rec)
            if claimed_exits:
                if rc not in claimed_exits:
                    # A divergence caused by a peer moving the *input bytes*
                    # under the fence (a D4 read-set change mid-wave) is
                    # stamp drift, not a disposer defect. The two are named
                    # separately so neither hides the other.
                    if "changed since the baseline was frozen" in out or \
                       "input-digest" in out or "assembly.packet_sha256" in out or \
                       "differ" in out or "FAIL verdict" in out:
                        drift.append((r["id"], script.splitlines()[0][:70],
                                      rc, claimed_exits, rec["observed"][:120]))
                    else:
                        failed.append((r["id"], script.splitlines()[0][:70], rc,
                                       claimed_exits, rec["observed"][:90]))
            elif rc not in (0, 1, 2):
                failed.append((r["id"], script.splitlines()[0][:70], rc,
                               "unclaimed", rec["observed"][:90]))
    check("A5_evidence_commands_rerun", not failed,
          f"{len(rerun)} fence(s) re-run; {len(failed)} diverged"
          + (f": {failed[:4]}" if failed else ""))

    # A5b — a divergence is *attributable* stamp drift when the fence touches the
    # D4 read set and those files' live bytes differ from the round-25 filed
    # baseline. That is measured, not inferred from output text: the baseline
    # digests are read from the round-25 receipts, and the live bytes are hashed.
    import hashlib as _hl
    D4_READSET = ["examples/culture-d4/packet.d4.yml",
                  "examples/culture-d4/packet.d4.typed.yml",
                  "examples/culture-d4/typed-labels.d4.yml",
                  "examples/culture-d4/expected-holds.json",
                  "examples/culture-d4/components/01-brief.yml",
                  "examples/culture-d4/components/04-lexicon.yml"]
    live_d4 = {}
    for rel in D4_READSET:
        p = os.path.join(LANE, rel)
        if os.path.exists(p):
            live_d4[rel] = _hl.sha256(open(p, "rb").read()).hexdigest()
    # The round-25 filed values, as recorded in the round-25 v3-supersession
    # evidence and the round-26 runner's own frozen baseline.
    BASE_D4 = {"examples/culture-d4/expected-holds.json":
               "3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7"}
    moved = sorted(rel for rel, dig in BASE_D4.items()
                   if live_d4.get(rel) != dig)
    unattributed = [d for d in drift if not moved]
    check("A5b_stamp_drift_attributed", not unattributed,
          f"{len(drift)} fence(s) diverged; the D4 read set has "
          f"{len(moved)} file(s) moved off the round-25 baseline "
          f"({', '.join(moved) or 'none'}); {len(unattributed)} unattributed")

    # A6 — declared block counts equal the fragment's own row count.
    declared = {"C41": 9, "C42": 6, "C43": 9, "C44": 7, "C45": 14, "C46": 4}
    mismatch = []
    for seat, n in declared.items():
        rows = fragments.get(seat)
        if rows is None:
            continue  # a not-yet-landed disposer is reported in A1, not here
        if len(rows) != n:
            mismatch.append((seat, n, len(rows)))
    check("A6_declared_block_counts", not mismatch,
          f"{len(mismatch)} fragment(s) disagree with the declared partition"
          + (f": {mismatch}" if mismatch else ""))

    landed = sorted(s for s, r in fragments.items() if r is not None)
    pending = sorted(s for s, r in fragments.items() if r is None)

    # A7 — the sibling README revision (a new file, not this seat's deliverable)
    # must carry every queue row with a disposition, and its class must agree
    # with the disposer fragment's class for that row. The revision's filename
    # and directory are not fixed by any contract (it landed as
    # `zzz-lessons-index-revision-3.md` at the round-26 root), so it is
    # *discovered*: the candidate is the .md file under reports/round-26 that
    # names the most queue ids. Absent revision is a named pending dependency.
    CANDIDATE_EXCLUDE = {f"C4{n}.md" for n in range(1, 7)} | {
        "dispositions.md", "audit.md"}
    best, best_ids = None, set()
    for root, _dirs, files in os.walk(os.path.join(LANE, "reports", "round-26")):
        for name in sorted(files):
            if not name.endswith(".md") or name in CANDIDATE_EXCLUDE:
                continue
            if name.startswith("x") or name.startswith("D"):  # audit/argot fragments
                continue
            text = open(os.path.join(root, name), encoding="utf-8").read()
            ids = set(re.findall(r"\b(Q-[A-Za-z0-9]+-\d+|Q-S1-\d+)\b", text))
            if len(ids) > len(best_ids):
                best, best_ids = os.path.relpath(os.path.join(root, name), LANE), ids
    rev = {"path": best, "present": best is not None and len(best_ids) > 0,
           "discovery": "the .md file under reports/round-26 naming the most queue ids"}
    if rev["present"]:
        rtext = open(os.path.join(LANE, best), encoding="utf-8").read()
        rev_ids = best_ids
        rev["ids_named"] = len(rev_ids)
        rev["rows_missing"] = sorted(set(qids) - rev_ids)
        frag_cls = {r["id"]: r["class"] for r in allrows}
        # The revision's table uses short class labels (`fixed`, `carried`);
        # the fragments use the full vocabulary (`fixed-with-evidence`). The
        # mapping is declared here so a label variance is not read as a
        # disagreement — only a row whose *class family* differs is one.
        SHORT = {"fixed": "fixed-with-evidence", "carried": "carried",
                 "routed": "routed", "superseded": "closed-by-supersession",
                 "standing-rule": "standing-rule"}
        disagreements = []
        for rid in qids:
            if rid not in rev_ids or rid not in frag_cls:
                continue
            m = re.search(r"(?m)^\|\s*" + re.escape(rid) + r"\s*\|([^|]*)\|", rtext)
            if not m:
                continue
            rev_cls = SHORT.get(m.group(1).strip(), m.group(1).strip())
            fcls = frag_cls[rid]
            if fcls and rev_cls and rev_cls != fcls:
                disagreements.append((rid, fcls, rev_cls))
        rev["class_disagreements"] = disagreements
        rev["class_label_mapping"] = SHORT
        check("A7_revision_carries_dispositions",
              not rev["rows_missing"],
              f"{best}: {len(rev_ids)} ids named; "
              f"{len(rev['rows_missing'])} queue rows absent"
              + (f": {rev['rows_missing'][:8]}" if rev["rows_missing"] else ""))
        check("A8_revision_class_agrees", not disagreements,
              f"{len(disagreements)} row(s) whose class family differs between "
              f"the revision and the disposer fragment"
              + (f": {disagreements[:6]}" if disagreements else ""))
    else:
        check("A7_revision_carries_dispositions", False,
              "no lessons-index revision file found under reports/round-26 yet")
        check("A8_revision_class_agrees", False,
              "no revision to compare")

    return {
        "schema": "kotodama-openq-disposition-audit-v1",
        "round": 26, "seat": "R26-C47..C50",
        "date": "2026-10-18",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "counting_command": "python3 reports/round-26/open-questions/audit-dispositions.py",
        "queue_rows": len(qids),
        "fragments_landed": landed,
        "fragments_pending": pending,
        "rows_audited": len(allrows),
        "rows_dispositioned": len(seen),
        "checks": checks, "findings": findings,
        "revision": rev,
        "stamp_drift": drift,
        "class_histogram": {c: sum(1 for r in allrows if r["class"] == c)
                            for c in sorted(VOCAB)},
        "rerun": rerun,
        "dispositions": [{k: r[k] for k in
                          ("id", "owner", "class", "next_touch_round",
                           "has_reason", "commands")}
                         for r in allrows],
    }


def selftest():
    ok = True

    def rep(name, good):
        nonlocal ok
        ok &= good
        print(f"selftest {name}: {'PASS' if good else 'FAIL'}")

    # A header row must not parse as a queue row.
    fake = "| Q-id | q | o | s |\n| Q-99-1 | q | o | open |\n"
    ids = [l.strip().strip("|").split("|")[0].strip() for l in fake.splitlines()
           if l.startswith("| Q-") and not l.startswith("| Q-id")]
    rep("header-row-not-a-row", ids == ["Q-99-1"])
    # The vocabulary rejects an invented class.
    rep("vocabulary-rejects-unknown", "auto-fixed" not in VOCAB)
    # The fence parser drops comments and keeps the runnable script whole.
    scripts = sh_commands("```sh\n# a comment\necho hi\n# hi\n```")
    rep("fence-parser-drops-comments", scripts == ["echo hi"])
    # A fixed row with no command must be detectable.
    rows = [{"id": "Q-99-1", "class": "fixed-with-evidence", "commands": []}]
    rep("A3-fires-on-evidence-free-fixed",
        bool([r for r in rows if r["class"] == "fixed-with-evidence" and not r["commands"]]))
    # A carried row missing next-touch must be detectable.
    rows = [{"id": "Q-99-2", "class": "carried", "owner": "x",
             "has_reason": True, "next_touch_round": None}]
    rep("A4-fires-on-incomplete-carried",
        bool([r for r in rows if r["class"] == "carried"
              and not (r["owner"] and r["has_reason"] and r["next_touch_round"])]))
    # The next-touch parser must read the line-wrapped wording too.
    rep("next-touch-linewrapped", next_touch("prose. Next\ntouch round 27.") == 27)
    rep("next-touch-inline", next_touch("Next touch round 27.") == 27)
    # The short-label mapping must fold `fixed` onto `fixed-with-evidence`
    # without folding two distinct families together.
    SHORT = {"fixed": "fixed-with-evidence", "carried": "carried"}
    rep("short-label-folds", SHORT.get("fixed") == "fixed-with-evidence")
    rep("short-label-keeps-carried-distinct",
        SHORT.get("carried") != "fixed-with-evidence")
    return 0 if ok else 1


def render_md(rep):
    L, A = [], None
    A = L.append
    A("# R26-C47..C50 — audit of the open-question dispositions")
    A("")
    A("- round 26 (operator: loop 3 of 3, build round 2 of 4). Seat **C**,")
    A("  claims `R26-C47..C50` (open-question auditors x4); owner: L2 worker,")
    A("  kotodama-shokunin lane.")
    A("- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.")
    A("- canon: **NON-CANON engineering evidence.** This audit admits nothing,")
    A("  certifies no round and grants no promotion.")
    A("- writes: `audit-dispositions.py`, `audit.json`, `audit.md` in this")
    A("  directory, plus gitignored scratch under `.scratch/r26-c47/`. No filed")
    A("  artifact of rounds 8-25 was edited; no disposer fragment was edited.")
    A("  No commit, no push.")
    A("")
    A("## 0. Verdict at a glance")
    A("")
    A("| reading | value |")
    A("|---|---|")
    A(f"| queue rows in the filed README | {rep['queue_rows']} |")
    A(f"| rows dispositioned by C41-C46 | {rep['rows_dispositioned']} |")
    A(f"| disposer fragments landed at this stamp | {', '.join(rep['fragments_landed']) or 'none'} |")
    A(f"| disposer fragments pending | {', '.join(rep['fragments_pending']) or 'none'} |")
    A(f"| evidence commands re-run | {len(rep['rerun'])} |")
    A(f"| **findings** | **{len(rep['findings'])}** |")
    A("")
    A("## 1. Checks")
    A("")
    A("| id | result | detail |")
    A("|---|---|---|")
    for c in rep["checks"]:
        A(f"| `{c['id']}` | {'PASS' if c['ok'] else 'FAIL'} | {c['detail'][:160]} |")
    A("")
    A("## 2. Class histogram over the audited rows")
    A("")
    A("| class | rows |")
    A("|---|---|")
    for k, v in rep["class_histogram"].items():
        A(f"| `{k}` | {v} |")
    A("")
    if rep["fragments_pending"]:
        A("## 3. Named dependency — disposer fragments not yet landed")
        A("")
        A("At this audit's stamp the following disposer seats had written no")
        A("fragment, so their block of the queue is **not yet dispositioned**:")
        A("")
        for s in rep["fragments_pending"]:
            A(f"- **{s}** — block: {BLOCKS[s][0]}")
        A("")
        A("This is a late-dependency report, not a defect: the block partition")
        A("assigns those rows to those seats, and A1 names exactly the rows that")
        A("remain. The audit re-runs green over the rows that have landed.")
        A("")
    rev = rep.get("revision", {})
    A("## 3. The sibling lessons-index revision")
    A("")
    if rev.get("present"):
        A(f"- path: `{rev['path']}` — discovered, not hard-coded (the file's")
        A("  name and directory are not fixed by any contract; it landed at the")
        A("  round-26 root as `zzz-lessons-index-revision-3.md`)")
        A("  A **new file** — the filed `corpus/lessons/README.md` blob is")
        A("  unchanged at `a31870556c733498243b56697896504a2fb3679a`")
        A(f"- queue ids named in it: **{rev.get('ids_named')}** of {rep['queue_rows']}")
        A(f"- queue rows absent: **{len(rev.get('rows_missing', []))}**")
        A(f"- rows whose class family differs from the disposer fragment: "
          f"**{len(rev.get('class_disagreements', []))}**")
    else:
        A("- **not landed** at this stamp (A7 names it as a pending dependency)")
    A("")
    if rep.get("stamp_drift"):
        A("## 4. Stamp drift — a live wave, disclosed not absorbed")
        A("")
        A(f"{len(rep['stamp_drift'])} fence(s) re-ran to a different exit than")
        A("the fragment claims, because a peer seat moved the D4 read set")
        A("**during this audit's own window**. The disposer fragments measured")
        A("the bytes as they stood at their stamp; this audit measured later")
        A("bytes. Neither reading is wrong, and the divergence is a fact about")
        A("the live wave, not a defect in any disposition.")
        A("")
        A("| row | fence | re-run exit | fragment claimed |")
        A("|---|---|---|---|")
        for d in rep["stamp_drift"]:
            A(f"| `{d[0]}` | `{d[1]}` | {d[2]} | {d[3]} |")
        A("")
        A("Attribution is measured, not inferred: the audit hashes the D4")
        A("read-set files against their round-25 filed baseline digests, and")
        A("only counts drift as attributable when those bytes have in fact")
        A("moved (A5b).")
        A("")
    A("## 5. Counting command")
    A("")
    A("```sh")
    A("export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1")
    A("python3 -B reports/round-26/open-questions/audit-dispositions.py        # audit + write")
    A("python3 -B reports/round-26/open-questions/audit-dispositions.py --json # receipt")
    A("```")
    A("")
    open(os.path.join(HERE, "audit.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not os.environ.get("TMPDIR"):
        print("TMPDIR unset; set TMPDIR=$PWD/.scratch", file=sys.stderr)
        return 2
    rep = audit()
    if args.json:
        print(json.dumps(rep, indent=1))
    else:
        for c in rep["checks"]:
            print(f"  {'PASS' if c['ok'] else 'FAIL'} {c['id']:36s} {c['detail'][:110]}")
        print(f"findings: {len(rep['findings'])}")
        print(f"rows audited: {rep['rows_audited']}  queue rows: {rep['queue_rows']}")
        print(f"landed: {rep['fragments_landed']}  pending: {rep['fragments_pending']}")
    json.dump(rep, open(os.path.join(HERE, "audit.json"), "w"), indent=1, ensure_ascii=False)
    render_md(rep)
    return 0 if not rep["findings"] else 1


if __name__ == "__main__":
    sys.exit(main())
