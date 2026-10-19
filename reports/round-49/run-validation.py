#!/usr/bin/env python3
"""Round-49 acceptance runner — loop-2 position 3.

Dispatch: kaika wave-2 L1 with one batched 11-member L2 swarm (planner, connector,
scout, 4 executors, scribe, reviewer, critic; models by the session route table).
The declared 64-seat opencode-go key-3 dispatch 402'd (telemetry/dispatch-declared.json).
Baseline c42d675. Claim S is declared in claims-addendum-kaika.json.

Claims (verdicts computed from landed bytes at run time, not pre-decided):
  C  coverage      — one right-sized entry lands on the verified-fresh
                     hunting/foraging subsistence-production gap:
                     corpus/knowledge/culture-material/hunting-foraging-subsistence.md,
                     <=250 lines, 1 H1, 0 H3, exactly one `- topic:` line, the
                     eight-field head (topic, gap filled, sources, couples,
                     source, verified-at, recheck, scope) in order before the
                     first `## `. Total 224 -> 225, culture-material 26 -> 27,
                     sweep green (rows 225 files 225, topic_mismatch 0,
                     totals_ok True, footer_ok True), filename ownership
                     hunt|forag|subsist == 1 (the new entry only).
  Ca calibration   — the residual duplicate `revision: 2.0` prose block in
                     corpus/README.md removed (grep count 2 -> 1), sweep and
                     tools/check-readme-heading.py stay green, and the durable
                     sibling control tools/check-readme-revisions.py exists,
                     exits 0 on the README, and its --selftest exits 0.
  S  depth         — capability acquisition: corpus/SOURCES.md lands per the
                     frozen contract (fleet-ledger/.ufo/waves/kaika/
                     SOURCES-CONTRACT-v1.md): the seven census commands run
                     clean (rows >= 1, malformed 0, no duplicate ids, no enum
                     or tier-inflation violations, no missing used-by paths,
                     tier/status histograms recorded, >= 1 rejected row);
                     headings Registry/Paths/Search log/Leads (unopened)
                     present; corpus/lessons/round-49.md exists with a `## Gate`
                     section naming every registry id; every row's `opened`
                     cell == 2026-10-19.
  cross            — informational: git status porcelain for the round's paths
                     and whether any pre-existing knowledge entry is modified
                     relative to baseline c42d675.

admission: admit when C and Ca and S all verify on landed bytes.
"""
import datetime, hashlib, json, pathlib, re, subprocess, sys, tempfile

ROOT = str(pathlib.Path(__file__).resolve().parents[2])
ROUND = "reports/round-49"
COMMAND = "python3 reports/round-49/run-validation.py"
BASELINE = "c42d675"

ENTRY = "corpus/knowledge/culture-material/hunting-foraging-subsistence.md"
LESSON = "corpus/lessons/round-49.md"
SOURCES = "corpus/SOURCES.md"
HEAD_FIELDS = ["- topic:", "- gap filled:", "- sources:", "- couples:",
               "- source:", "- verified-at:", "- recheck:", "- scope:"]

# The seven census commands, verbatim from SOURCES-CONTRACT-v1.md lines 66-81.
CENSUS = [
    "grep -cE '^\\|[[:space:]]*S[0-9]{3,}[[:space:]]*\\|' corpus/SOURCES.md",
    "awk -F'|' '/^\\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md",
    "awk -F'|' '/^\\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\\|/ {t=$5; gsub(/[[:space:]]/,\"\",t); n[t]++} END{for(k in n) printf \"%s=%d \", k, n[k]; print \"\"}' corpus/SOURCES.md",
    "awk -F'|' '/^\\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\\|/ {s=$9; gsub(/[[:space:]]/,\"\",s); n[s]++} END{for(k in n) printf \"%s=%d \", k, n[k]; print \"\"}' corpus/SOURCES.md",
    "awk -F'|' '/^\\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\\|/ {i=$2; gsub(/[[:space:]]/,\"\",i); print i}' corpus/SOURCES.md | sort | uniq -d",
    "awk -F'|' '/^\\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,\"\",i); gsub(/[[:space:]]/,\"\",k); gsub(/[[:space:]]/,\"\",t); gsub(/[[:space:]]/,\"\",s); if (t !~ /^[ABC]$/) print \"tier\", i, t; if (s !~ /^(queued|mined|rejected)$/) print \"status\", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print \"kind\", i, k; if (t==\"A\" && k==\"community\") print \"tier-inflation\", i}' corpus/SOURCES.md",
    "awk -F'|' '/^\\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,\"\",s); if (s==\"mined\") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,\"\",p); if (p!=\"\" && p!=\"—\") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e \"$p\" ] || echo \"missing: $p\"; done",
]

ROW_RE = re.compile(r"^\|\s*S\d{3,}\s*\|")


def sh(*a, timeout=300, cwd=None):
    env = dict(__import__("os").environ, TMPDIR=str(pathlib.Path(ROOT) / ".scratch"),
               PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run(a, capture_output=True, timeout=timeout, cwd=cwd or ROOT, env=env)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def sha_file(p):
    try:
        return hashlib.sha256(open(pathlib.Path(ROOT) / p, "rb").read()).hexdigest()
    except OSError:
        return None


def count(pattern, path):
    rc, out, _ = sh("bash", "-c", f"grep -c {json.dumps(pattern)} {json.dumps(path)}")
    try:
        return int(out.strip())
    except ValueError:
        return -1


def measure():
    results = {}
    failures = []

    # ---- C: coverage (the hunting/foraging subsistence entry landed) ---------
    tot = len(list(pathlib.Path(ROOT, "corpus/knowledge").rglob("*.md")))
    cm = len(list(pathlib.Path(ROOT, "corpus/knowledge/culture-material").glob("*.md")))
    target = pathlib.Path(ROOT, ENTRY)
    entry_lines = len(target.read_text().splitlines()) if target.exists() else -1
    entry_text = target.read_text() if target.exists() else ""
    elines = entry_text.splitlines()
    h1 = sum(1 for l in elines if l.startswith("# "))
    h3 = sum(1 for l in elines if l.startswith("### "))
    topic_lines = sum(1 for l in elines if l.startswith("- topic:"))
    # eight-field head, in order, before the first `## ` heading
    first_h2 = next((i for i, l in enumerate(elines) if l.startswith("## ")),
                    len(elines))
    head = elines[:first_h2]
    positions = []
    for f in HEAD_FIELDS:
        positions.append(next((i for i, l in enumerate(head)
                               if l.startswith(f)), -1))
    head_ok = all(p >= 0 for p in positions) and positions == sorted(positions)
    # sweep
    rc, sw, _ = sh("python3", "-B", "reports/round-28/readme/sweep.py")
    sweep_green = ("rows 225 files 225" in sw and "topic_mismatch 0" in sw
                   and "totals_ok True" in sw and "footer_ok True" in sw)
    # gap ownership at landing: filename find for hunt|forag|subsist == 1
    rc_g, gap_list, _ = sh(
        "bash", "-c",
        "find corpus/knowledge -name '*.md' | grep -iE 'hunt|forag|subsist' || true")
    gap_files = [l for l in gap_list.splitlines() if l.strip()]
    gap_ok = gap_files == [ENTRY]
    # zero existing entries overwritten: every knowledge path that differs from the
    # baseline (tracked diff + untracked) must be the new entry; requires a git clone
    rc_d, kdiff, _ = sh("git", "diff", "--name-only", BASELINE, "--", "corpus/knowledge")
    rc_u, kuntr, _ = sh("git", "ls-files", "--others", "--exclude-standard", "--", "corpus/knowledge")
    k_changed = sorted(set(l for l in (kdiff + kuntr).splitlines() if l.strip()))
    no_overwrite = rc_d == 0 and rc_u == 0 and [f for f in k_changed if f != ENTRY] == []
    c_meas = {"total": tot, "culture_material": cm,
              "entry_landed": target.exists(), "entry_lines": entry_lines,
              "entry_h1": h1, "entry_h3": h3, "topic_lines": topic_lines,
              "head_field_positions": positions, "head_fields_ordered": head_ok,
              "sweep_green": sweep_green, "gap_owners": gap_files,
              "gap_ownership_ok": gap_ok, "knowledge_changed_vs_baseline": k_changed,
              "no_existing_entry_modified": no_overwrite}
    c_ok = (target.exists() and tot == 225 and cm == 27
            and 0 < entry_lines <= 250 and h1 == 1 and h3 == 0
            and topic_lines == 1 and head_ok and sweep_green and gap_ok
            and no_overwrite)
    results["C"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if c_ok else "unchanged-blocked",
        "passed": bool(c_ok), "measurement": c_meas,
        "failures": [] if c_ok else ["hunting/foraging entry missing, out-of-band, or sweep-red"]}
    if not c_ok:
        failures.append("claim C: entry, head contract, counts, sweep, or gap ownership unmet")

    # ---- Ca: calibration -----------------------------------------------------
    readme_rev = count("^revision: 2\\.0", "corpus/README.md")
    heading = pathlib.Path(ROOT, "tools/check-readme-heading.py")
    rev_tool = pathlib.Path(ROOT, "tools/check-readme-revisions.py")
    rc_h, _, _ = sh("python3", "-B", "tools/check-readme-heading.py")
    rc_r, r_out, r_err = sh("python3", "-B", "tools/check-readme-revisions.py")
    rc_rs, rs_out, rs_err = sh("python3", "-B", "tools/check-readme-revisions.py",
                               "--selftest")
    heading_ok = heading.exists() and rc_h == 0
    rev_tool_ok = rev_tool.exists() and rc_r == 0 and rc_rs == 0
    ca_meas = {"readme_revision_2_0_count": readme_rev,
               "heading_tool_landed": heading.exists(),
               "heading_tool_rc": rc_h,
               "revisions_tool_landed": rev_tool.exists(),
               "revisions_tool_rc": rc_r,
               "revisions_tool_rc_stderr": r_err.strip()[-400:],
               "revisions_tool_selftest_rc": rc_rs,
               "revisions_tool_selftest_tail": (rs_out + rs_err).strip()[-400:],
               "sweep_green": sweep_green}
    ca_ok = readme_rev == 1 and sweep_green and heading_ok and rev_tool_ok
    results["Ca"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if ca_ok else "unprovable",
        "passed": bool(ca_ok), "measurement": ca_meas,
        "failures": [] if ca_ok else ["README duplicate revision, heading, or revisions control unmet"]}
    if not ca_ok:
        failures.append("claim Ca: 'revision: 2.0' count != 1, sweep red, or control missing/red")

    # ---- S: depth / capability acquisition (corpus/SOURCES.md) ---------------
    sources = pathlib.Path(ROOT, SOURCES)
    stext = sources.read_text() if sources.exists() else ""
    census = []
    for cmd in CENSUS:
        rc_c, c_out, c_err = sh("bash", "-c", cmd)
        census.append({"command": cmd, "rc": rc_c,
                       "stdout": c_out.strip(), "stderr": c_err.strip()[-300:]})
    def cint(i):
        try:
            return int(census[i]["stdout"])
        except ValueError:
            return -1
    rows = cint(0)
    malformed = cint(1)
    tier_hist = census[2]["stdout"]
    status_hist = census[3]["stdout"]
    dup_ids = census[4]["stdout"]
    enum_violations = census[5]["stdout"]
    missing_usedby = census[6]["stdout"]
    rejected_n = 0
    m = re.search(r"(?:^| )rejected=(\d+)", status_hist)
    if m:
        rejected_n = int(m.group(1))
    headings = {h: bool(re.search(r"(?m)^" + re.escape(h) + r"[ \t]*$", stext)) for h in
                ("## Registry", "## Paths", "## Search log", "## Leads (unopened)")}
    headings_ok = sources.exists() and all(headings.values())
    # registry rows parsed for ids and the `opened` column (field 10)
    ids, opened_vals = [], []
    for l in stext.splitlines():
        if ROW_RE.match(l):
            parts = [p.strip() for p in l.split("|")]
            if len(parts) >= 12:
                ids.append(parts[1])
                opened_vals.append(parts[9])
    opened_ok = bool(ids) and all(v == "2026-10-19" for v in opened_vals)
    # lesson Gate coverage of every registry id
    lesson = pathlib.Path(ROOT, LESSON)
    ltext = lesson.read_text() if lesson.exists() else ""
    gate_ok = False
    gate_missing = []
    gate_head = re.search(r"(?m)^## Gate[ \t]*$", ltext)
    if lesson.exists() and gate_head:
        rest = ltext[gate_head.end():]
        nxt = re.search(r"(?m)^## ", rest)
        gate_section = rest[:nxt.start()] if nxt else rest
        gate_missing = [i for i in ids if not re.search(r"(?m)^- " + re.escape(i) + r" ", gate_section)]
        gate_ok = bool(ids) and not gate_missing
    s_meas = {"sources_landed": sources.exists(), "census": census,
              "rows": rows, "malformed": malformed,
              "tier_histogram": tier_hist, "status_histogram": status_hist,
              "duplicate_ids_output": dup_ids, "enum_violations_output": enum_violations,
              "missing_usedby_output": missing_usedby,
              "rejected_rows": rejected_n,
              "headings": headings, "headings_ok": headings_ok,
              "registry_ids": ids, "opened_cells": opened_vals,
              "opened_all_2026_10_19": opened_ok,
              "lesson_landed": lesson.exists(), "gate_section_present": bool(gate_head),
              "gate_missing_ids": gate_missing, "gate_covers_all_ids": gate_ok}
    s_ok = (sources.exists() and rows >= 1 and malformed == 0
            and dup_ids == "" and enum_violations == "" and missing_usedby == ""
            and rejected_n >= 1 and headings_ok and lesson.exists()
            and bool(gate_head) and gate_ok and opened_ok)
    results["S"] = {"command": COMMAND, "date": "2026-10-19",
        "verdict": "improved" if s_ok else "unprovable",
        "passed": bool(s_ok), "measurement": s_meas,
        "failures": [] if s_ok else ["SOURCES.md missing or census/lesson/opened checks red"]}
    if not s_ok:
        failures.append("claim S: SOURCES.md census, headings, lesson Gate, or opened dates unmet")

    # ---- cross ---------------------------------------------------------------
    rc4, stat, _ = sh("git", "status", "--porcelain=v1")
    porcelain = [l for l in stat.splitlines() if l.strip()]
    rc5, diff, _ = sh("git", "diff", "--name-only", BASELINE, "--", "corpus/knowledge")
    diff_files = [l for l in diff.splitlines() if l.strip()]
    existing_modified = [f for f in diff_files if f != ENTRY]
    knowledge_status = [l for l in porcelain
                        if "corpus/knowledge" in l and ENTRY not in l]
    results["cross"] = {"command": COMMAND, "date": "2026-10-19", "verdict": "measured",
        "passed": True,
        "measurement": {
            "git_status_rc": rc4,
            "porcelain_lines": porcelain,
            "knowledge_diff_vs_baseline": diff_files,
            "existing_knowledge_modified": existing_modified,
            "existing_knowledge_status_lines": knowledge_status,
            "new_entry_status": [l for l in porcelain if "hunting-foraging" in l],
        },
        "failures": []}

    # ---- cross separability (informational; these legs never gate admission) --
    source_line = next((l for l in elines if l.startswith("- source:")), "")
    url_ids = sorted(set(re.findall(r"\*\*(S\d{3})\*\* \(https?://", source_line)))
    cited = sorted(set(re.findall(r"\bS\d{3}\b", entry_text)))
    no_inline_url = sorted(set(cited) - set(url_ids))
    c_without_s = {
        "url_ids": url_ids,
        "cited": cited,
        "no_inline_url": no_inline_url,
        "passed": not no_inline_url,
    }

    # Remove this entry from every used-by cell; mined rows without any other
    # citer become queued.  Census runs on a temporary registry copy.
    scratch = pathlib.Path(ROOT, ".scratch")
    scratch.mkdir(parents=True, exist_ok=True)
    counterfactual_lines = []
    for line in stext.splitlines():
        if ROW_RE.match(line):
            cells = line.split("|")
            if len(cells) > 11:
                used_by = [p.strip() for p in re.split(r"[,;]", cells[11])]
                used_by = [p for p in used_by if p and p not in ("—", ENTRY)]
                cells[11] = f" {', '.join(used_by) if used_by else '—'} "
                if not used_by and cells[8].strip() == "mined":
                    cells[8] = " queued "
                line = "|".join(cells)
        counterfactual_lines.append(line)
    counterfactual_text = "\n".join(counterfactual_lines)
    if stext.endswith("\n"):
        counterfactual_text += "\n"
    with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=scratch,
            prefix="r49-s-without-c-", suffix=".md", delete=False) as tmp:
        tmp.write(counterfactual_text)
        counterfactual_path = pathlib.Path(tmp.name)
    counterfactual_relpath = counterfactual_path.relative_to(ROOT).as_posix()
    sep_commands = [cmd.replace(SOURCES, counterfactual_relpath) for cmd in CENSUS]
    # The counterfactual entry is absent even though the working tree contains it.
    sep_commands[6] = sep_commands[6].replace(
        '[ -e "$p" ] || echo "missing: $p"',
        f'[ "$p" != {json.dumps(ENTRY)} ] && [ -e "$p" ] || echo "missing: $p"')
    sep_census = []
    try:
        for cmd in sep_commands:
            rc_c, c_out, c_err = sh("bash", "-c", cmd)
            sep_census.append({"command": cmd, "rc": rc_c,
                               "stdout": c_out.strip(), "stderr": c_err.strip()[-300:]})
    finally:
        counterfactual_path.unlink(missing_ok=True)

    try:
        sep_malformed = int(sep_census[1]["stdout"])
    except ValueError:
        sep_malformed = -1
    sep_dup_ids = sep_census[4]["stdout"]
    sep_enum_violations = sep_census[5]["stdout"]
    sep_missing_usedby = sep_census[6]["stdout"]
    s_without_c_passed = (sep_malformed == 0 and sep_dup_ids == ""
                          and sep_enum_violations == ""
                          and sep_missing_usedby == "")
    s_without_c = {
        "sources_landed": sources.exists(),
        "temporary_sources_path": counterfactual_relpath,
        "entry_path_assumed_absent": ENTRY,
        "census": sep_census,
        "malformed": sep_malformed,
        "duplicate_ids_output": sep_dup_ids,
        "enum_violations_output": sep_enum_violations,
        "missing_usedby_output": sep_missing_usedby,
        "passed": bool(s_without_c_passed),
    }
    results["separability"] = {
        "c_without_s": c_without_s,
        "s_without_c": s_without_c,
    }


    admitted = (results["C"]["passed"] and results["Ca"]["passed"]
                and results["S"]["passed"])
    return {
        "round": 49, "baseline_revision": BASELINE, "counting_command": COMMAND,
        "date": "2026-10-19",
        "claims_declared": {"C": "coverage", "Ca": "calibration", "S": "depth"},
        "claims": results,
        "acceptance_checks_passed": admitted,
        "verdict": "admitted" if admitted else "rejected-honest-stop",
        "partial": ("C (hunting/foraging entry, sweep 225 green) + "
                    "Ca (README revision dedupe + revisions control) + "
                    "S (SOURCES.md registry landed) — per-claim verdicts computed"),
        "failures": failures,
        "limits": [],
        "input_sha256": {
            f"{ROUND}/claims.json": sha_file(f"{ROUND}/claims.json"),
            f"{ROUND}/claims-addendum-kaika.json": sha_file(f"{ROUND}/claims-addendum-kaika.json"),
            f"{ROUND}/targets.json": sha_file(f"{ROUND}/targets.json"),
            f"{ROUND}/run-validation.py": sha_file(f"{ROUND}/run-validation.py"),
            "tools/check-readme-heading.py": sha_file("tools/check-readme-heading.py"),
            "tools/check-readme-revisions.py": sha_file("tools/check-readme-revisions.py"),
            "corpus/SOURCES.md": sha_file(SOURCES),
            "corpus/lessons/round-49.md": sha_file(LESSON),
            ENTRY: sha_file(ENTRY),
            "corpus/README.md": sha_file("corpus/README.md"),
        },
    }


def main():
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        sys.stdout.write(rendered)
        return 0
    out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv \
        else pathlib.Path(ROOT) / ROUND / "validation.json"
    out.write_text(rendered, encoding="utf-8")
    print(f"receipt: {out}")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    print(f"verdict: {receipt['verdict']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
