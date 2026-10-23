#!/usr/bin/env python3
"""Generate the round-60 attempt-3 wave 2 spec (blind SUPPORT data seats + falsify items) for kotodama.

Usage (lane root): python3 -B .ufo/waves/round-60/gen-support-a3.py <freeze-commit> <packet-dir> <rerun-control>...
The 24 SupportA60..SupportX60 items carry their packet byte-for-byte (ACCEPT-D-60 BOUND rule) and the
revision-5 CONFINED tool rules; the falsify items attack wave-1 output and carry their own lane paths
(the shared context names no lane path beyond the Report-trailer rule, so a support seat is told
nothing about the lane). Writes .ufo/waves/round-60/support-a3-spec.json.
"""
import json
import os
import pathlib
import sys
from collections import Counter

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-60"
SCR = "/fast/scratch/hyaku/kotodama-r60a3"
FREEZE, PKT, RERUN = sys.argv[1], sys.argv[2], sys.argv[3:]
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
SEATS = [f"Support{x}60" for x in "ABCDEFGHIJKLMNOPQRSTUVWX"]
TOOLING = ("Tooling authorization (operator, 2026-10-19): you and every seat may install or update tools that help the task "
           "without asking; read /home/vgpnk/.omp/agent/RULES.md first and record each install (tool, version, channel, reason). "
           "All pacman transactions are PAUSED host-wide: never pacman -S/-Sy/-Syu/-U/-R, never downgrade, never restart a host "
           "service; use uv tool, npx or an official binary in ~/.local/bin, or report the need. Support* seats: install nothing "
           "and do NOT open RULES.md or any other local file (it is outside your /tmp sandbox); your item's TOOL RULES bind you.")

CONTEXT = f"""# Goal
Round 60 (attempt 3), wave 2: blind source review seats (named Support*) and falsify seats (every other name). Each seat follows ONLY its own item.

# Bounds (binding on every seat)
Every seat is a leaf: no delegation, no background jobs, no swarms. Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path> with ONE `write` tool call (absolute path); never edit or rewrite it afterwards. Seats write nothing else in that repo and never run git or jj write commands there or in /home/vgpnk/Projects/shokunin; never write under /home/vgpnk/.omp/. Cap every process with `timeout`; kill any process tree you started before you return. Use PYTHONDONTWRITEBYTECODE=1 and `python3 -B` for every python run. Time box: return within 30 minutes of your start.
{TOOLING}
External pages by ORDINARY MEANS ONLY: plain requests (curl, python urllib, the read tool on a URL), archive.org captures; never a headless browser and never any tool that gets past a bot challenge, captcha, paywall or login.
"""

items = []


def add(name, role, prompt, axes=("depth",)):
    items.append({"name": name, "role": role, "prompt": LEAD + prompt, "axes": list(axes)})


SUPPORT = """Blind source review. Your packet is below: blocks labelled P01, P02, ...; each gives url (one or more addresses of ONE page: the page and archive captures of it), a quoted passage, a `teaches` summary and an `entry` statement written from that page.
TOOL RULES (binding; one breach voids ALL your verdicts):
- Use ONLY three tools: `bash`, `read`, and ONE final `write` of your report. Never use grep, glob, eval, edit, web search or any other tool.
- Every `bash` call sets its `cwd` parameter to /tmp/{seat} OR starts with exactly `mkdir -p /tmp/{seat} && cd /tmp/{seat} && `. Inside commands, the only absolute paths allowed are under /tmp/{seat}/ (plus /dev/null); write files with relative names or /tmp/{seat}/... Never use `..`, `~`, `$HOME`, any other `cd`, `eval`, `base64`, `-C`, or any path elsewhere on the machine.
- `read` only a packet URL exactly as listed (no `:raw` or line-range suffix) or a file under /tmp/{seat}/.
- Fetch ONLY URLs listed in your packet, or `https://web.archive.org/web/2026id_/<a packet url>`; no other URL at all (no search engines, no Wayback availability or CDX API, no other site).
For EACH block, open the page yourself, URL written literally in the command: `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36' '<url>' -o <n>.html -w '%{http_code} %{size_download}\\n'` (cwd /tmp/{seat}), or the read tool on the URL. Some sites refuse a bare client (HTTP 403/429) but serve a browser User-Agent: always retry with that curl line. If the live page still fails or serves a bot challenge, open a listed web.archive.org capture, or `curl -sSL 'https://web.archive.org/web/2026id_/<url>' -o <n>w.html` (Wayback serves the nearest capture of that same page). Answer `unreachable` only after all of these fail. For a PDF, extract text with `pdftotext <n>.pdf <n>.txt` in /tmp/{seat}; search text with `python3 -B -c` reading files by relative name (str.find, re), never a script file elsewhere. To strip HTML tags use exactly `re.sub(r'(?s)<[^>]+>', ' ', t)` (do not write closing-tag literals such as a slash after `<` in your commands). Then decide:
- SUPPORTED only when all three hold: (1) the quote is verbatim body text on that page (whitespace, hyphenation and quote-mark differences aside; not a heading, navigation, cookie, promo or caption fragment); (2) the page carries the teaches summary; (3) the page carries EVERY claim in the entry statement — no universal drawn from one object, no added comparison, contrast, cause, date or place, no theory the page hedges stated as fact.
- Otherwise NOT-SUPPORTED, including a page you cannot open by any listed URL (say `unreachable`).
Some blocks are deliberately defective; judge every block on its own evidence, never by its position or label.
Blindness: never open, list, search or name any local path other than /tmp/{seat}/ and your own report path; never search the web; never use history:// or agent://; never name another seat.
Report: write it ONCE with the `write` tool to the absolute report path (see the Report trailer and context), never edit it. For every label exactly one line, line-initial: `VERDICT P01 SUPPORTED — "<one sentence of at least 10 words copied exactly from the page, in straight double quotes, that is NOT the packet's quote: e.g. the page sentence carrying the entry claim, or the sentence just before or after the quote>" <then how the page carries the quote, teaches and each entry claim>` or `VERDICT P01 NOT-SUPPORTED — <which of (1)-(3) fails and why>`. Copy that sentence from the page text you fetched (no ellipsis, no paraphrase); a SUPPORTED line without such a page sentence does not count. Then list each URL you opened with its HTTP status and byte count.

=== PACKET ===
"""
for seat in SEATS:
    packet = open(os.path.join(PKT, f"packet-{seat}.md"), encoding="utf-8").read()
    add(seat, "reviewer", SUPPORT.replace("{seat}", seat) + packet + "=== END PACKET ===\n", ("depth",))

FAL = (f"Falsify item (attack what wave 1 and the L1 produced; read-only in the lane {LANE}; sandbox work only under {SCR}/<YourName>/, "
       f"sandbox git only in clones there with GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE unset). The frozen declaration is {LANE}/reports/round-60/claims.json at `{FREEZE}`. "
       f"Never open {LANE}/.ufo/waves/round-60/support/ or {SCR}/support/ and never message or name a Support* seat. Paste every command with its full output (no tail/head/cut). First line of your report: `HOLDS` or `BREAKS: <one line>`.\n")
NEW = {"S648": "S602", "S649": "S616", "S650": "S623", "S651": "S643"}
for new, old in NEW.items():
    add(f"ReopenRow{new}A3", "scout", FAL + f"Re-open source row {new} (`git -C {LANE} show {FREEZE}:corpus/SOURCES.md | grep -n '^| {new} '`) by ordinary means: fetch its first URL (and its listed Wayback capture), check the quote locates (`python3 -B {LANE}/reports/round-60/reopen-quote.py`, usage in its docstring), compare the bytes with the pinned capture {LANE}/reports/round-60/captures/{new}.bin (sha256 in captures/manifest.json), check the row's tier, scope and access notes against what you saw, and confirm its first URL is the same page as {old}'s. Then read the entry line citing {new} at `{FREEZE}` and list each clause with the page sentence carrying it or `NOT CARRIED`.", ("depth",))
for name in RERUN:
    add(f"Rerun{name}", "reviewer", FAL + f"Independent re-measure of pre-data control receipts. Read {W}/w1-a3/{name}.md. Re-run its fixtures with its own commands (copy its scripts from {SCR}/{name}/ into {SCR}/<YourName>/ and run there; never modify the original) against the frozen counter (`git -C {LANE} show {FREEZE}:reports/round-60/accept-d.py | sha256sum` must equal the counter sha256 its receipts name). For every RECEIPT line: reproduced exactly, differs (paste both), or not re-runnable (why). Also say whether each fixture really is the shape its label claims (a do-nothing fixture that secretly does the work; a probe that changed more than the SESSIONS constant).", ("operability", "depth"))
add("ReviewRecordsA3", "reviewer", FAL + f"Check the routed-defect records against {LANE}/corpus/lessons/round-59-verifier-spotcheck.md section 5 items 1-6 at `{FREEZE}` or the lane branch tip: {LANE}/SCORECARD.md (round-59 correction rows), {LANE}/LOG.md (round-60 correction entry), {LANE}/corpus/lessons/round-59.md errata, {LANE}/corpus/lessons/round-60.md, {LANE}/corpus/QUALITY.md. For each item: routed (path:line) or missing. Check that no filed round-59 row was rewritten (`git -C {LANE} diff 9c82a6eb main -- SCORECARD.md LOG.md corpus/lessons/round-59.md` shows only additions) and that `/usr/bin/find {LANE} -name __pycache__` is empty.", ("calibration",))
add("CriticQualityA3", "critic", FAL + f"Attack the newest QUALITY criterion in {LANE}/corpus/QUALITY.md (added this round): is it testable from committed bytes; does it name a check shown able to fail; would it have caught round 59's post-verdict narowing; does it contradict earlier criteria?", ("calibration",))
add("ScoutCensusA3", "scout", FAL + f"Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (read-only) and paste the full output with exit code; check rows S648-S651 at the lane branch tip for the 11-cell shape, status `mined`, used-by the amulets entry, and that S602 S616 S623 S643 stay `rejected` with used-by `—`.", ("operability",))
add("ReviewSeparabilityA3", "reviewer", FAL + f"Re-run `timeout 900 python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json` in a sandbox clone at the lane branch tip (`git -C {LANE} rev-parse main`), twice, the second under `unshare -rn` if available; paste both full outputs and say whether they are byte-identical and whether any line attributes a dependency the counter cannot have (the counter has no network leg).", ("operability",))

c = Counter(i["role"] for i in items)
spec = {
    "wave": "kotodama-r60a3-support",
    "milestone": "Round 60 attempt 3: blind SUPPORT of the frozen amulets entry (ACCEPT-D-60 data seats) plus falsify attacks on wave-1 output",
    "reportDir": ".ufo/waves/round-60/support",
    "axes": ["depth", "calibration", "operability"],
    "context": CONTEXT,
    "items": items,
}
json.dump(spec, open(f"{W}/support-a3-spec.json", "w"), indent=1, ensure_ascii=False)
print(len(items), dict(c))
