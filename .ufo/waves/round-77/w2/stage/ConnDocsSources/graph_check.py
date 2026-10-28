#!/usr/bin/env python3
"""ConnDocsSources (round 77, wave 2) — document-level graph cross-check.

Read-only. Reads W1 draft/stage artifacts under the lane and base blobs via
`git -C <lane> show <base>:<path>`. Prints one line per edge: OK / FAIL / PENDING.
PENDING = target exists only after the L1 landing (not a draft defect).
"""
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
W = LANE + "/.ufo/waves/round-77"
W1 = W + "/w1"

edges = []


def edge(name, status, detail):
    edges.append((name, status, detail))


def rd(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def base_show(path):
    r = subprocess.run(["git", "-C", LANE, "show", f"{BASE}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def base_exists(path):
    r = subprocess.run(["git", "-C", LANE, "cat-file", "-e", f"{BASE}:{path}"],
                       capture_output=True)
    return r.returncode == 0


def norm(s):
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", "", s)
    return s.replace("“", '"').replace("”", '"').lower()


# ---------------------------------------------------------------- inputs
rows_txt = rd(W1 + "/stage/ExecCensusEnd/rows-897-898.md")
rows = {}
for line in rows_txt.splitlines():
    if not line.strip():
        continue
    cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
    rows[cells[0]] = cells

entry_path = "corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md"
entry = rd(W1 + "/drafts/" + entry_path)
lesson = rd(W1 + "/drafts/corpus/lessons/round-77.md")
plan = rd(W1 + "/stage/ScoutReadmeIndex/readme-plan.md")
d1 = rd(W1 + "/stage/ScribeEntryA/d1-live.text")
d2 = rd(W1 + "/stage/ScribeEntryA/d2-live.text")
ev897 = rd(W1 + "/stage/ScoutDocS897/evidence.txt")
ev898 = rd(W1 + "/stage/ScoutDocS898/evidence.txt")
entry_lines = entry.split("\n")

# ---------------------------------------------------------------- map / row identity
edge("MAP S897 -> D1 lane id S897 (row id, lesson, claims agree)",
     "OK" if rows["S897"][0] == "S897" and "S897" in lesson else "FAIL",
     "row S897 present; lesson Gate row 'S897 (staged S897, tier B)'")
edge("MAP S903 -> D2 lane id S898 (lesson Gate row 'staged S903')",
     "OK" if "(staged S903, tier A)" in lesson and "S898" in rows else "FAIL",
     "lesson Gate: 'S898 (staged S903, tier A)'; rows file has S898")
for rid in ("S897", "S898"):
    edge(f"REG {rid} unused in base registry",
         "OK" if not re.search(rf"^\| {rid} \|", base_show("corpus/SOURCES.md") or "", re.M) else "FAIL",
         f"base SOURCES grep ^| {rid} | -> 0 expected")

base_sources = base_show("corpus/SOURCES.md") or ""
base_ids = re.findall(r"^\| (S\d{3}) \|", base_sources, re.M)
edge("REG base rows = 820 and ids unique",
     "OK" if len(base_ids) == 820 and len(set(base_ids)) == 820 else "FAIL",
     f"rows={len(base_ids)} unique={len(set(base_ids))} max={max(base_ids)}")

# URL identity across row / entry / lesson
D1_URL = "http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml"
D2_URL = "https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/"
edge("URL D1 live URL identical in row S897 cell, entry, lesson",
     "OK" if D1_URL in rows["S897"][1] and D1_URL in entry and D1_URL in lesson else "FAIL", D1_URL)
edge("URL D2 live URL identical in row S898 cell, entry, lesson",
     "OK" if D2_URL in rows["S898"][1] and D2_URL in entry and D2_URL in lesson else "FAIL", D2_URL)

# ---------------------------------------------------------------- row fields vs entry / Gate
tier897 = rows["S897"][3]
edge("ROW S897 tier == Gate/entry/claims tier (B)",
     "OK" if tier897 == "B" else "FAIL",
     f"row tier cell='{tier897}'; lesson says 'tier B'; entry §7/§8 says tier B for D1")

edge("ROW S897 status cell agrees with per-UA record (browser 200)",
     "FAIL" if "403 to both the plain and the browser-shaped" in rows["S897"][1] else "OK",
     "row cell: 'live answered HTTP 403 to both ... browser-shaped' vs evidence browser 200 (ScoutDocS897 ua-records)")

edge("ROW S897 anchor names the same located source as claims/lesson (browser-UA live)",
     "FAIL" if "capture 20240111092427, article body" in rows["S897"][5] else "OK",
     "row anchor = capture; claims/lesson = browser-UA live copy as located source")

for rid, want in (("S897", "365d"), ("S898", "365d")):
    pass
m = re.search(r"^- recheck: (\d+d)", entry, re.M)
entry_recheck = m.group(1) if m else None
for rid in ("S897", "S898"):
    edge(f"RECHECK {rid} row window == entry recheck window",
         "OK" if rows[rid][9] == entry_recheck else "FAIL",
         f"row {rid} recheck='{rows[rid][9]}' vs entry recheck='{entry_recheck}'")

ev_access898 = re.search(r"^access-date: (\S+)", ev898, re.M).group(1)
edge("DATE S898 opened == evidence access-date == entry 'fetched' date",
     "OK" if rows["S898"][8] == ev_access898 else "FAIL",
     f"row opened='{rows['S898'][8]}' evidence access-date='{ev_access898}' (fetched 2026-10-28T01:26:13Z)")
ev_access897 = re.search(r"^access-date: (\S+)", ev897, re.M).group(1)
ev_fetched897 = re.search(r"^fetched: (\S+)", ev897, re.M).group(1)
edge("DATE S897 opened == evidence access-date",
     "OK" if rows["S897"][8] == ev_access897 else "FAIL",
     f"row opened='{rows['S897'][8]}' evidence access-date='{ev_access897}' fetched='{ev_fetched897}'")

edge("AUTHOR S898 row first name == PDF author (Irena)",
     "FAIL" if "Iwona" in rows["S898"][1] else "OK",
     "row: 'Kałużyńska, Iwona (2025)'; PDF text: 'Irena Kałużyńska' / 'IRENA KAŁUŻYŃSKA'; entry and lesson say Irena")

edge("INSTITUTE D1 name: entry source line vs row cell",
     "FAIL" if ("古代史研究所" in entry_lines[2] and "历史研究所" in rows["S897"][1]) else "OK",
     "entry line 3: 'reprint by 中國社會科學院古代史研究所' (page copyright footer); row/lesson: '中国社会科学院 历史研究所 site'")

# ---------------------------------------------------------------- entry source lines
src_lines = [l for l in entry_lines if l.startswith("- source: ")]
src_ids = [re.match(r"- source: (S\d{3}) ", l).group(1) for l in src_lines]
edge("ENTRY exactly one '- source:' line per adopted doc (S897, S898)",
     "OK" if sorted(src_ids) == ["S897", "S898"] else "FAIL",
     f"'- source:' lines={len(src_lines)} ids={src_ids}")
all_ids = sorted(set(re.findall(r"\bS\d{3}\b", entry)))
edge("ENTRY cites only lane ids that are registry rows S897/S898 (no legacy/staged id)",
     "OK" if all_ids == ["S897", "S898"] else "FAIL",
     f"S-tokens in entry={all_ids} (legacy S886/S888/S889/S890/S891/S896 and S903 absent)")
edge("ENTRY has one physical '- topic:' line",
     "OK" if sum(1 for l in entry_lines if l.startswith("- topic:")) == 1 else "FAIL",
     "topic line count = 1 (line 11)")

plain_line = [l for l in entry_lines if l.startswith("- verified-at") or l.startswith("- recheck:")]
edge("ENTRY line 6 per-UA claim: 'both HTTP 200 to a plain client' (must be false for D1)",
     "FAIL" if "Both documents answered HTTP 200 to a plain client" in entry else "OK",
     "entry line 6 vs entry §8 + recheck detail (D1 plain = 403, 162 B)")
edge("ENTRY §8 'no wall is recorded' vs row/evidence 'wall met, not passed' + capture 429",
     "FAIL" if "no wall is recorded against it" in entry and "wall met, not passed" in rows["S897"][1] else "OK",
     "entry §8 vs row S897 cell; ScribeEntryA fetch-log: capture under browser UA -> HTTP 429 'suspected abusive bot traffic'")

# ---------------------------------------------------------------- quote edges
q_cjk = re.findall(r"「([^」]+)」", entry)
d1n = norm(d1)
cjk_ok, cjk_bad = [], []
for q in q_cjk:
    if re.search(r"[A-Za-z]", q) and not re.search(r"[\u4e00-\u9fff]", q):
        continue
    parts = [p for p in q.split("…") if p.strip()]
    ok = all(norm(p) in d1n for p in parts)
    (cjk_ok if ok else cjk_bad).append(q)
edge("QUOTE D1: every CJK span in entry locates in D1 stored text",
     "OK" if not cjk_bad else "FAIL",
     f"located={len(cjk_ok)} unlocated={len(cjk_bad)} {cjk_bad[:3]}")

q_en = [q for q in q_cjk if re.search(r"[A-Za-z]", q) and not re.search(r"[\u4e00-\u9fff]", q)]
d2n = norm(d2)
en_bad = [q for q in q_en if norm(q) not in d2n]
edge("QUOTE D2: every English span in entry locates in D2 stored text",
     "OK" if not en_bad and len(q_en) == 8 else "FAIL",
     f"located={len(q_en) - len(en_bad)} of {len(q_en)}; unlocated={en_bad}")

m = re.search(r"quote-words: (\d+)", ev898)
edge("EVIDENCE S898 header quote-words/quote-chars match the 17-word quote line",
     "OK" if m and m.group(1) == "17" else "FAIL",
     f"evidence header quote-words={m.group(1) if m else None} quote-chars="
     + (re.search(r"quote-chars: (\d+)", ev898).group(1)))

# ---------------------------------------------------------------- back-edge + outbound
bk = base_show("corpus/knowledge/linguistics/naming-systems.md") or ""
edge("BACKEDGE base naming-systems.md points to amend (entry §10 claims 'points here through its couples: line')",
     "OK" if "amend-2026-10-23" in bk else "FAIL",
     "grep 'amend-2026-10-23' in base naming-systems.md -> "
     + str(bk.count("amend-2026-10-23")) + " hits")

couples = [l for l in entry_lines if l.startswith("- couples:")][0]
for tgt in re.findall(r"`(linguistics/[a-z0-9-]+\.md)`", couples):
    edge(f"OUTBOUND couples target exists at base: {tgt}",
         "OK" if base_exists("corpus/knowledge/" + tgt) else "FAIL", "base blob")

edge("OUTBOUND §2/§6/§7 steps 2 and 4 that the entry's pipeline insertions anchor to",
     "OK" if all(s in base_show("corpus/knowledge/linguistics/naming-systems.md") for s in
                 ("## 2. Anthroponymy", "## 6. Name taboo", "## 7. Derivation pipeline",
                  "2. **Slot inventory", "4. **Lexify")) else "FAIL",
     "base headings/steps present")

edge("OUTBOUND claims cite corpus/CORPUS.md ('CORPUS.md rule 1') — path at base",
     "OK" if base_exists("corpus/CORPUS.md") else "FAIL",
     "corpus/CORPUS.md absent at base (only reports/round-33/adj/A05-corpus.md matches)")

# ---------------------------------------------------------------- README edges
m = re.search(r"```\n(- `naming-systems\.amend[^\n]*)\n```", plan)
plan_row = m.group(1) if m else ""
plan_body = plan_row.split(" — ", 1)[1] if " — " in plan_row else ""
ent_topic = [l for l in entry_lines if l.startswith("- topic:")][0][len("- topic: "):]
edge("README row body == entry '- topic:' line (verbatim)",
     "OK" if plan_body == ent_topic else "FAIL",
     f"plan body starts '{plan_body[:60]}…' ; entry topic starts '{ent_topic[:60]}…'")

edge("README linguistics heading: plan (33) vs lesson 'left stale' (32)",
     "FAIL" if ("(33)" in plan and "named stale and left as filed" in lesson) else "OK",
     "readme-plan §1 requires '## linguistics/ (33)'; lesson Census: '## linguistics/ (32)' left as filed")

base_readme = base_show("corpus/README.md") or ""
footers = re.findall(r"^Total knowledge entries: (\d+)\.", base_readme, re.M)
edge("README base footers: 5 'Total knowledge entries' blocks, last=253",
     "OK" if footers == ["243", "247", "249", "252", "253"] else "FAIL",
     f"footers={footers}")

parts = {}
for d in ("civilizations", "culture-material", "linguistics", "myth-symbol", "synthesis", "verification"):
    r = subprocess.run(["git", "-C", LANE, "ls-tree", "--name-only", BASE, f"corpus/knowledge/{d}/"],
                       capture_output=True, text=True)
    parts[d] = len([x for x in r.stdout.split("\n") if x.endswith(".md")])
edge("README partition counts base sum = 253; post-landing sum 254 (+1 linguistics)",
     "OK" if sum(parts.values()) == 253 and parts["linguistics"] == 32 else "FAIL",
     f"base partitions={parts} sum={sum(parts.values())}")

# ---------------------------------------------------------------- landing-only targets
for target in ("reports/round-77/evidence/S897.txt", "reports/round-77/evidence/S898.txt",
               "reports/round-77/telemetry/census-end.txt"):
    edge(f"LANDING target {target}", "PENDING", "absent at draft; committed by L1")
edge("LANDING used-by path corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md",
     "PENDING", "row used-by equals entry path; entry file lands at C-lands (draft only at w1/drafts)")
edge("LANDING frozen by-document map (staged id -> normalized document -> lane id)",
     "PENDING", "no frozen map file exists; W1 ScoutIdMap table is the only map")
edge("LANDING S897 Gate quote and locator cells (L1-FILL)",
     "PENDING", "lesson Gate cells read L1-FILL; ScoutDocS897/evidence.txt already holds the lead-para locator")

# ---------------------------------------------------------------- report
width = max(len(e[0]) for e in edges)
for name, status, detail in edges:
    print(f"{status:7s} {name:<{width}}  | {detail}")
counts = {}
for _, s, _ in edges:
    counts[s] = counts.get(s, 0) + 1
print()
print("TOTAL", len(edges), counts)
