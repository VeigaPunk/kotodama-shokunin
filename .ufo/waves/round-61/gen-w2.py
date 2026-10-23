#!/usr/bin/env python3
"""Generate the round-61 wave 2 (falsify) spec: one row, one clause per support reviewer, plus attacks.

Usage (lane root): python3 -B .ufo/waves/round-61/gen-w2.py
Reads corpus/SOURCES.md and the footwear entry at the measured revision's worktree. Review-only: no
seat verdict feeds ACCEPT-C-61 or ACCEPT-O-61 (both already measured; receipts frozen).
"""
import json
import pathlib
import re

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
SCR = "/fast/scratch/hyaku/kotodama-r61"
REV = "efbee29cd8c0872a4fb89db34c489d4a9960916c"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
ENTRY = pathlib.Path(LANE, "corpus/knowledge/culture-material/footwear-codes-terminology.md").read_text()
ROWS = {}
for line in pathlib.Path(LANE, "corpus/SOURCES.md").read_text().splitlines():
    m = re.match(r"^\|\s*(S6(?:5[2-9]|[6-9]\d))\s*\|", line)
    if m:
        ROWS[m.group(1)] = line.split("|")

CONTEXT = f"""# Goal
Kotodama round 61 (hyaku phase 4, 2026-10-23 UTC), WAVE 2: FALSIFY. Lane repo {LANE}, measured revision `{REV}`. Both claims are already measured once on frozen counters (receipt {LANE}/reports/round-61/telemetry/final-measures.txt: ACCEPT-C-61 FAIL on LOCATE (one row), ACCEPT-O-61 PASS). Nothing you report changes those verdicts; you attack what wave 1 produced so the round report and the lesson are honest. The L1 (KotodamaR61) alone writes the lane. Time box: return within 20 minutes of your start; a partial report beats none.

# Ownership and bounds (binding)
Every seat is a leaf: no delegation, no background jobs, no swarms. Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path> with ONE write tool call (absolute path); never edit it afterwards. Seats write NOTHING else in {LANE} and nothing in the fleet repo /home/vgpnk/Projects/shokunin (never a relative path: your tools start at the fleet root). Other files go ONLY under {SCR}/w2/<YourName>/. Never run git or jj write commands in {LANE} or /home/vgpnk/Projects/shokunin; sandbox git only in clones under {SCR}/w2/<YourName>/ with GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE unset. Cap every process with `timeout` (<= 600 s); kill any process tree you started before you return; bound every file (< 5 MB). Never write under /home/vgpnk/.omp/. NEVER run reports/round-61/accept-c.py (its one receipt is final).
Tooling authorization (operator, 2026-10-19): you and every seat may install or update tools that help the task without asking; read /home/vgpnk/.omp/agent/RULES.md first and record each install (tool, version, channel, reason). All pacman transactions are PAUSED host-wide: never pacman -S/-Sy/-Syu/-U/-R, never downgrade, never restart a host service; use uv tool, npx or an official binary in ~/.local/bin, or report the need. Prefer no installs.

# Sources
External reading by ORDINARY MEANS ONLY: plain requests (read tool, curl, python urllib), public copies, archive.org captures. NEVER use a headless browser or anything that gets past a bot challenge, captcha, paywall or login; a challenge met is reported as met-not-passed. PDF text: `uv run --no-project --quiet --with pypdf==5.4.0 python3 -B -c ...` (disclose it).
"""

items = []


def add(name, role, prompt, axes):
    items.append({"name": name, "role": role, "prompt": LEAD + prompt, "axes": list(axes)})


for line in ENTRY.splitlines():
    m = re.search(r"\((S6\d\d)\)\s*$", line)
    if not m:
        continue
    sid = m.group(1)
    cells = ROWS[sid]
    urls = re.findall(r"https?://[^\s<>\"|`;]+", cells[2])
    quote = re.search(r'"([^"]+)"', cells[6]).group(1)
    clause = re.sub(r"\s*\(S6\d\d\)\s*$", "", line).lstrip("- ").strip()
    add(f"Row{sid}", "reviewer", f"""ONE ROW, ONE CLAUSE review (review-only; no context from other rows). Open the page by ordinary means and judge two things.
URL(s) (one page; later ones are archive captures of it): {' ; '.join(urls)}
Quoted passage the row records: "{quote}"
Clause written from it: "{clause}"
(1) QUOTE: is the passage verbatim body text of that page (not navigation or a caption fragment)? Answer LOCATED / NOT-LOCATED / UNREACHABLE (give the HTTP status or error and whether an archive capture works).
(2) CLAUSE: does the page support EVERY part of the clause - nothing added (no date, place, cause, comparison, universal, or a hedge removed)? Answer SUPPORTED / NOT-SUPPORTED / UNREACHABLE, and paste >= 10 consecutive words of page text that carry the clause (or name the unsupported part exactly).
End your report with two lines exactly: `QUOTE {sid} <verdict>` and `CLAUSE {sid} <verdict>`.""", ("coverage",))

add("ReviewLocateS671", "reviewer", f"Diagnose claim C's single LOCATE failure WITHOUT running accept-c.py: the receipt {LANE}/reports/round-61/telemetry/final-measures.txt shows S671 NOT_LOCATED (live americanindian.si.edu HTTPError; Wayback capture error). Read the S671 row in {LANE}/corpus/SOURCES.md, fetch each of its URLs by ordinary means (curl -sS -o /dev/null -w '%{{http_code}}' and the locator `timeout 300 python3 -B {LANE}/reports/round-61/reopen-quote.py URL \"QUOTE\"` once per URL), and report the status codes, whether the failure is transient or structural (bot challenge, 403/404, capture missing), and whether the row's scribe report ({LANE}/.ufo/waves/round-61/w1/ScribeSrc06.md) recorded a located live fetch and a located capture before landing. State plainly that the verdict stays FAIL under the frozen kill rule.", ("coverage", "calibration"))
add("CriticFreezeC", "critic", f"Attack the claim C timeline (read-only): in {LANE}, `git log --format='%h %cI %s' 942abdf4..{REV}` and `git diff --stat 2f4f8a4027912f7f6e821fc5180f279e08936174 {REV} -- reports/round-61/`; confirm the counters and locator are byte-identical from the freeze 2f4f8a40 to the measured revision, that no counter run on the claimed entry precedes the freeze (the L1's pre-landing self-checks used reopen-quote.py --row on three rows, tools/check-source-access.py and the readme sweep; judge whether those are a data run under {LANE}/reports/round-61/claims.json `predicate_rule`), and that the revision-1 notes in claims.json name the control receipt behind each change ({LANE}/reports/round-61/telemetry/controls-c-rescore.txt, controls-o-rescore.txt). Report every inconsistency with path:line.", ("calibration",))
add("MutToolO", "mutation-tester", f"Mutation-test the LANDED claim-O tool {LANE}/tools/check-cited-lines.py at {REV}: clone the lane to {SCR}/w2/MutToolO/clone (checkout {REV}), make at least 8 single-point mutants of tools/check-cited-lines.py in the clone (regex boundary, sort order, table detection, distinct-id count, summary count, exit codes, .md filter, UTF-8 handling) and run `timeout 600 python3 -B reports/round-61/accept-o.py` in the clone for each; report killed/survived per mutant with the failing leg. A survivor is a gap in ACCEPT-O-61, not a change to its verdict.", ("operability",))
add("ReviewRerunO", "reviewer", f"Independent re-measure of claim O: clone {LANE} to {SCR}/w2/ReviewRerunO/clone, checkout {REV}, run `timeout 600 python3 -B reports/round-61/accept-o.py; echo exit=$?` five times, paste every full output; confirm the counter's sha256 equals 5f1530a485d307544ccbde94a8c1f80b3f9d5360b7c8a4966259174e3d3bb99d and the tool's equals a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a; also run the tool on the clone's corpus/knowledge and confirm the R60-M6 amulets line is reported. Report any non-PASS run.", ("operability",))
add("CriticClaimO", "critic", f"Attack claim O as an axis move (read-only): {LANE}/reports/round-61/claims.json (O), the tool {LANE}/tools/check-cited-lines.py and its control receipts ({LANE}/.ufo/waves/round-61/w1/CtlO*.md, MutCounterO.md, {LANE}/reports/round-61/telemetry/controls-o-rescore.txt). Is operability named by the surface the round changed (a new lane tool) and not by a number? Does any revision-0 control still meet revision 1 (CtlOKeyed a2 and the fake-selftest fixture pass revision 1: are they work-skipping shortcuts or correct tools)? Is O a re-scoring of a rule the lane already held (search {LANE}/tools)? Verdict with reasons.", ("operability",))
add("ReviewContainment", "reviewer", f"Containment and misroot sweep (read-only): `git -C /home/vgpnk/Projects/shokunin status --porcelain` and list any untracked file whose content names kotodama round 61 (a seat misroot, e.g. /home/vgpnk/Projects/shokunin/.ufo/waves/round-61/w1/ScribeSrc01.md); `git -C {LANE} status --porcelain`; check {SCR} size with `/usr/bin/du -sh {SCR}` and that no process with a cwd under {SCR} is still running (`ps -eo pid,etimes,args | grep kotodama-r61 | grep -v grep`). Report findings only; delete nothing.", ("calibration",))

spec = {
    "wave": "kotodama-r61-w2",
    "milestone": "Round 61 wave 2: falsify - one-row one-clause support review of S652-S692 plus attacks on C's miss and O",
    "reportDir": ".ufo/waves/round-61/w2",
    "axes": ["coverage", "operability", "calibration"],
    "context": CONTEXT,
    "items": items,
}
pathlib.Path(__file__).with_name("w2-spec.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
print(len(items))
