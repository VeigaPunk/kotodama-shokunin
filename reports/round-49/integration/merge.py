#!/usr/bin/env python3
"""Integrator merge: three SOURCES fragments -> corpus/SOURCES.md + Gate text.

Renumbers temp ids contiguously: E2 S201.. -> S001.., E4 S301.. -> next, E1 S101.. -> next.
Writes:
  corpus/SOURCES.md
  .scratch/r49/gate-merged.md   (the lesson's ## Gate body)
  .scratch/r49/idmap.json
and applies the E1 id map to the hunting entry (whole-token replace).
"""
import json, pathlib, re, sys

WT = pathlib.Path(__file__).resolve().parents[2]
FR = WT / ".scratch/r49"
ORDER = [("E2-sources.md", "2"), ("E4-sources.md", "3"), ("E1-sources.md", "1")]
ENTRY = WT / "corpus/knowledge/culture-material/hunting-foraging-subsistence.md"
ROW = re.compile(r"^\|\s*(S\d{3})\s*\|")


def sections(text):
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            cur = m.group(1).strip()
            out[cur] = []
            continue
        if cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


idmap, rows, gates, logs, paths, leads = {}, [], [], [], [], []
n = 0
frags = {}
for name, _ in ORDER:
    text = (FR / name).read_text(encoding="utf-8")
    frags[name] = text
    for line in text.splitlines():
        m = ROW.match(line)
        if m:
            n += 1
            idmap[m.group(1)] = "S%03d" % n
tok = re.compile(r"\bS[123]\d\d\b")


def remap(s):
    return tok.sub(lambda m: idmap.get(m.group(0), m.group(0)), s)


for name, _ in ORDER:
    text = frags[name]
    for line in text.splitlines():
        if ROW.match(line):
            cells = line.split("|")
            if cells[10].strip() in ("—", "-", ""):
                cells[10] = " 365d "  # rejected rows: recheck the flip yearly
            rows.append(remap("|".join(cells)))
    sec = sections(text)
    for k, v in sec.items():
        kl = k.lower()
        if kl.startswith("gate"):
            gates.append(remap(v))
        elif kl.startswith("search log"):
            logs.append(remap(v))
        elif kl.startswith("paths"):
            paths.append(remap(v))
        elif kl.startswith("leads"):
            leads.append(remap(v))

head = """# SOURCES — where kotodama learns

The lane's curated reading list and the standing record of its taste:
what each source teaches, how far to trust it for which scope, and when to
look again. Shape and rules: fleet contract `SOURCES-CONTRACT-v1`
(kaika, 2026-10-19). Claim admission stays in `QUALITY.md`; the research
method stays chousa's. Every row was opened in the round that wrote it —
the round lesson's `## Gate` (`lessons/round-49.md` for S001–S%03d) holds
each row's URL, access date and verbatim quote. Append-only: only
`status`, `recheck` and `used-by` change in place, each change logged
old→new in a round lesson; a correction is a new row whose `teaches`
opens `supersedes S0NN —`.

Tiers are scoped to the row's `scope`, never global. **A** — primary or
authoritative for that scope (spec, official docs, source code, original
paper, maintainer statement, the lane's own re-runnable gate output).
**B** — strong secondary (expert write-up with reproducible detail, survey,
textbook). **C** — lead only, never sole support for an admitted entry.
`community` is never A. Tier is curation, not truth. Status: `queued`
(opened, worth mining) · `mined` (cited by the paths in `used-by`) ·
`rejected` (kept with reason and flip — a rejection is evidence of taste).

Census (from the lane root): the seven commands in the contract's
`## Census` block; `python3 reports/round-49/run-validation.py` runs them.
""" % n

out = [head, "## Registry", "",
       "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |",
       "|---|---|---|---|---|---|---|---|---|---|---|"]
out += rows
out += ["", "## Paths", ""]
out += ["\n".join(paths)]
out += ["", "## Search log", ""]
labels = ["Linguistics, typology, conlang and motif leads (rows S001–S015).",
          "Folktale, legend, period, costume and iconography leads (rows S016–S030).",
          "Hunting and foraging subsistence (rows S031–S%03d)." % n]
for lab, body in zip(labels, logs):
    out += ["**%s** %s" % (lab, " ".join(body.split())), ""]
out += ["## Leads (unopened)", "",
        "A lead is not evidence and never a row; open it before it becomes one.", ""]
out += ["\n\n".join(leads), ""]
(WT / "corpus/SOURCES.md").write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")
(FR / "gate-merged.md").write_text("\n\n".join(gates) + "\n", encoding="utf-8")
(FR / "idmap.json").write_text(json.dumps(idmap, indent=1) + "\n", encoding="utf-8")
e = ENTRY.read_text(encoding="utf-8")
ENTRY.write_text(re.sub(r"\bS1\d\d\b", lambda m: idmap.get(m.group(0), m.group(0)), e), encoding="utf-8")
print("rows", n, "map", idmap)
