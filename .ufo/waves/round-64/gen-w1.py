import json
import pathlib

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
SCRATCH = "/home/vgpnk/.cache/hyaku/kotodama-r64"
GODSPEED = """/skill:godspeed
You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim \u2014 let the frontier walk itself.**

## IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches. Do not serialize what can run in parallel. Do not output philosophical reasoning or verbose plans. Act directly via tool calls.
"""

CONTEXT = """# Goal
Kotodama round 64 (hyaku run 5, 2026-10-23), wave 1 BUILD. Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (branch main, jj-colocated), base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`.

Three declared claims, each with a frozen predicate:
- C (coverage, sourced): a new entry `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` plus exactly 26 new registry rows S718-S743 (all `mined`) and six rejection rows S744-S749 (`rejected`). Predicate: `ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS`. Read the docstring of /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-64/accept-c.py for the exact per-leg rules.
- O (operability, counter hardening): `reports/round-64/accept-o.py` pins seven redirect-edge properties and a DRIP wall-budget distinction on the unchanged lane tool `tools/reopen-row.py`. Predicate: `ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS`.
- Ca (calibration): the round-63 closure's routed bookkeeping defects, verified by `reports/round-64/accept-ca.py`. Predicate: `ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py prints PASS`.

# Bounds (hard)
- Do NOT write anything inside /home/vgpnk/Projects/shokunin/kotodama-shokunin or any other repo unless your item explicitly says so. Your writable directory is /home/vgpnk/.cache/hyaku/kotodama-r64/<YourSeatName>/ (mkdir -p it). The L1 integrates your files.
- Never touch the fleet repo, sibling lanes, lane jj state or the lane Git index. Never run `git add`, `git commit`, `git stash`, `git checkout`, `git switch`, `git reset`, `git pull`, `git push` or any mutating `jj` command. Read-only git is fine.
- Every `Report:` trailer path the harness prints is relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin \u2014 write it at /home/vgpnk/Projects/shokunin/kotodama-shokunin/<that path> ONLY if your item says to; otherwise ignore the trailer and write in your scratch dir.
- Never message `agent://all`. Reply to the L1 by your final message only.
- Tooling authorization (operator, 2026-10-19): you may install or upgrade tools that help the task \u2014 read /home/vgpnk/.omp/agent/RULES.md first (official channels only; record tool/version/channel/reason in your report). PACMAN GUARD: all pacman transactions are PAUSED host-wide; install via `uv tool`/`npx`/an official binary in ~/.local/bin only, or file an L0 question. Never `-Sy`, `-Syu`, `-U`, `-R`, downgrade, or restart a host service.
- Sources are opened by ordinary means only (QUALITY.md criterion 10): a plain GET, a public copy, an archive capture or a library scan. Never solve a captcha, pass a bot challenge with browser automation, or bypass a paywall/login/geo block. A challenge met and routed around by an ordinary archived copy is fine and must be recorded as `challenge met, not passed`.

# Already-known formats
- Registry row: `| S### | <citation> - <live URL> ; capture <web.archive.org capture URL> | <kind> | <tier> | <scope> | <anchor: "quote"> | <teaches> | <status> | 2026-10-23 | 180d | <used-by> |` \u2014 11 cells, no `|` inside a cell.
- kind: spec, docs, paper, code, tool, dataset, talk, book, community, own-work.
- Tier is scoped to the row's `scope`, never global. A = primary or authoritative for exactly that scope (original paper, official docs, the source's own record). B = strong secondary (expert write-up, survey, textbook, encyclopedia overview, publisher abstract). C = lead only, never sole support for an admitted claim. `community` is never A.
- Lane locator for verification: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py <URL> "<quote>"` prints one line `LOCATED <url>` (exit 0) or `NOT_LOCATED <reason>` (exit 1). At least 8 normalised words are required in the quote.
"""

ENTRY = "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"

ROWS = [
    ("S718", "child-directed speech as a cross-linguistic register", "child-directed speech cross-linguistic register motherese review"),
    ("S719", "infant-directed speech prosody (pitch range, vowel space, attention)", "infant-directed speech prosody vowel space pitch review"),
    ("S720", "babbling and early phonological development (canonical babbling, language-specific drift)", "canonical babbling phonological development infants review"),
    ("S721", "turn-taking and protoconversation in infancy", "protoconversation infant turn-taking development review"),
    ("S722", "fast mapping and the vocabulary spurt", "fast mapping vocabulary spurt children review"),
    ("S723", "overextension and underextension in early word meaning", "overextension underextension child word meaning"),
    ("S724", "telegraphic speech and early multiword utterances", "telegraphic speech early multiword utterance children"),
    ("S725", "recasts and corrective feedback in child grammar", "recast corrective feedback child grammar acquisition study"),
    ("S726", "the language socialization paradigm (Ochs and Schieffelin)", "language socialization Ochs Schieffelin paradigm"),
    ("S727", "Samoan child language socialization (Ochs)", "Ochs Samoan language socialization children"),
    ("S728", "Kaluli language socialization and 'say it like this' (Schieffelin)", "Schieffelin Kaluli language socialization say it like this"),
    ("S729", "baby talk in a non-Western caregiving setting", "baby talk non-Western society caregiver speech study"),
    ("S730", "bilingual first language acquisition", "bilingual first language acquisition children review"),
    ("S731", "child code-switching", "child code-switching bilingual children study"),
    ("S732", "heritage language shift and attrition in childhood", "heritage language shift attrition children immigrant"),
    ("S733", "sign language acquisition by deaf children of deaf parents", "deaf children sign language acquisition native signers"),
    ("S734", "narrative socialization and narrative development", "narrative development socialization children storytelling"),
    ("S735", "schooled narrative and 'sharing time'", "sharing time topic-centered topic-associating narrative children"),
    ("S736", "literacy socialization and emergent literacy", "literacy socialization emergent literacy children home"),
    ("S737", "metalinguistic awareness and language play", "metalinguistic awareness language play children development"),
    ("S738", "language ideologies in childrearing", "language ideologies childrearing socialization study"),
    ("S739", "naming practices and address terms learned by children", "personal names address terms children acquisition study"),
    ("S740", "honorifics and keigo acquisition", "Japanese honorifics keigo acquisition children"),
    ("S741", "taboo words and avoidance taught to children", "taboo words children avoidance socialization study"),
    ("S742", "ritual speech genres taught to children", "ritual speech genre children socialization greetings"),
    ("S743", "a named child-language register", "Japanese child language register nyuyoji-go"),
]

SECTION = {
    "S718": 2, "S719": 2, "S729": 2, "S724": 2,
    "S720": 3, "S721": 3, "S722": 3, "S723": 3,
    "S725": 4, "S737": 4, "S743": 4,
    "S726": 5, "S727": 5, "S728": 5, "S742": 5, "S738": 5,
    "S730": 6, "S731": 6, "S732": 6, "S733": 6,
    "S734": 7, "S735": 7, "S736": 7,
    "S739": 8, "S740": 8, "S741": 8,
}

REJECTS = [
    ("S744", "the ushanka candidate whose search led to the Khanka lake/region rather than the hat", "ushanka hat", "the source opened on request names the Khanka region, not the headgear"),
    ("S745", "a Merriam-Webster entry whose page refused an ordinary request", "Merriam-Webster dictionary entry", "the page answered a refusal page instead of the entry"),
    ("S746", "a Wikisource Smith Corona typewriter page that did not carry the quoted wording", "Wikisource Smith Corona", "the page's text did not carry the candidate quotation"),
    ("S747", "an Encyclopaedia Britannica academic-dress page that answered 404", "Britannica academic dress", "the page answered HTTP 404 on an ordinary request"),
    ("S748", "a LacusCurtius page whose path form with an asterisk did not resolve", "LacusCurtius asterisk path", "the path with the asterisk did not resolve to a page"),
    ("S749", "a headgear candidate judged below the admission bar for a substantive claim (descriptive listing only)", "headgear listing descriptive", "the page only listed objects without a substantive, locatable claim"),
]


def row_prompt(sid, topic, query):
    sec = SECTION[sid]
    return (
        GODSPEED
        + f"""
ROW item (claim C). ID {sid}. Topic: {topic}. Entry section it feeds: ## {sec}.
Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRow{sid}/ (mkdir -p).

1. Find ONE source that is genuinely authoritative for exactly this topic. Use `web_search` with a query like "{query}". Prefer, in order: open-access peer-reviewed papers (PMC, DOAJ, university repositories), the source's own official record, then strong expert secondary (Britannica, university teaching pages, handbooks). Reject search-result aggregators, mirrors, blogs and AI-generated pages. A publisher abstract or encyclopedia overview is tier B for a substantive claim; the original paper is tier A for its own findings.
2. Open it by ordinary means (plain GET / `curl -sL --max-time 60`). If a bot challenge or paywall blocks it, route to an archived copy or pick another source; never solve a challenge.
3. Get a same-page archived capture: `curl -s "https://archive.org/wayback/available?url=<URL>"` and use the `timestamp` and `original` it returns, in the form `https://web.archive.org/web/<timestamp>id_/<original>`. If no capture exists, prefer a different source that has one.
4. Choose a verbatim, contiguous quote of 8-25 words from the page's body text (not a caption, alt/title attribute, or navigation text). Confirm it with the lane locator from the lane root:
   `cd {LANE} && python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'`
   It must print `LOCATED <url>`. Keep that exact first line.
5. Write `row.txt` in your scratch dir with EXACTLY these labelled lines and nothing else:

ROW: | {sid} | <Author or institution, year> "<title>", <publication> - <LIVE URL> ; capture <ARCHIVE URL> | <kind> | <tier> | <the scoped topic this tier applies to> | <locator such as section heading or paragraph>: "<your verbatim quote>" | <one grounded learner benefit, <= 25 words> | mined | 2026-10-23 | 180d | {ENTRY} |
BULLET: - <one clause that restates what the quote establishes for a worldbuilder> ({sid})
VERIFY: <the verbatim first line the locator printed>
CAPTURE: <the verbatim `timestamp`+`original` facts from the wayback answer, or "none">
ACCESS: <how you opened it: plain curl / archive capture, HTTP status, date>

Rules for ROW: exactly 11 cells; no `|` inside a cell; no placeholder hosts (example.com/httpbin/JSONPlaceholder); the live URL must appear in no other row and never inside the entry; `anchor` must carry the quote in double quotes.
Rules for BULLET (checked mechanically): one line, 6-25 words in the clause before `({sid})`; keep at least three distinctive words of your quote in the quote's own order; add at least one content word that is not in the quote; never copy more than 12 consecutive words from the quote; exactly one S-id on the line, at the end, in parentheses.
6. Self-check before finishing: re-run the locator once more from the lane root and paste its line; count the ROW cells (`awk -F'|'` gives 13 fields for 11 cells); count your quote's words (8-25).
Report in your final message: the ROW line, the BULLET line, the VERIFY line, tier and why, and anything that failed.
"""
    )


def reject_prompt(sid, label, query, ground):
    return (
        GODSPEED
        + f"""
REJECTION-ROW item (claim C, routed defect 7 of corpus/lessons/round-63-verifier-spotcheck.md). ID {sid}.
Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRej{sid}/ (mkdir -p).

The round-63 headgear sweep rejected a candidate: {label}. Round 63 kept the reason only as lesson prose; this round files it as a `rejected` registry row with the reason and the flip, and re-tests the stated ground (QUALITY.md criterion 12: a rejection reason that names a tool or a measurable result must carry that tool's verbatim output).

1. Reconstruct the candidate: run `web_search` for "{query}" and identify the most likely page the round-63 seat had opened (read {LANE}/corpus/lessons/round-63.md first; it records the candidates and their reject reasons). Record the URL you tested.
2. Re-test the ground "{ground}" with an ordinary tool \u2014 `curl -sS -o /dev/null -w '%{{http_code}} %{{url_effective}}' -L --max-time 60 '<URL>'`, and `cd {LANE} && python3 -B reports/round-61/reopen-quote.py '<URL>' '<candidate quote>'` when a quote is involved. Paste the verbatim output. Never solve a challenge or bypass a paywall.
3. Write `row.txt` with EXACTLY these labelled lines:

ROW: | {sid} | <the candidate as cited, with its URL> | <kind> | <tier> | <what it would have supported> | <locator tested>: "<the quote or wording tested, 8-25 words>" | REJECTED: <the re-tested reason>; flip: <what would change the verdict> | rejected | 2026-10-23 | 180d | \u2014 |
TEST: <the verbatim output of the re-test command(s)>
TEST2: <the verbatim locator first line, or "not applicable">

Rules for ROW: exactly 11 cells; no `|` inside a cell; status exactly `rejected`; teaches starts `REJECTED:` and contains `; flip:`; used-by exactly `\u2014`.
4. If the re-test CONTRADICTS the original ground (the page now serves the entry, or the locator finds the quote), do not file a false rejection: say so in your final message with the output, and label the row `QUEUED-CANDIDATE` instead, explaining why.
Report in your final message: the ROW line, the verbatim test output(s), whether the ground still holds, and the URL.
"""
    )


def main():
    items = []

    def add(name, role, prompt, axes):
        items.append({"name": name, "role": role, "prompt": prompt, "axes": axes})

    for sid, topic, query in ROWS:
        add(f"ScribeRow{sid}", "scribe", row_prompt(sid, topic, query), ["coverage"])
    for sid, label, query, ground in REJECTS:
        add(f"ScribeRej{sid}", "scribe", reject_prompt(sid, label, query, ground), ["coverage"])

    add("ScribeEntrySkeleton", "scribe", GODSPEED + f"""
ENTRY-SKELETON item (claim C). Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeEntrySkeleton/ (mkdir -p).

Write `entry.md`: the prose skeleton of the new knowledge entry `{ENTRY}`. The 26 cited bullet lines are inserted by the L1; you write everything else.

Shape (hard limits from reports/round-64/accept-c.py): at most 250 lines total; exactly one H1 (`# ...`); no H3 at all; at most 16 H2 (`## ...`); exactly one line starting `- topic:`; the header carries the provenance trio `- source:`, `- verified-at:`, `- recheck:` (read {LANE}/corpus/knowledge/culture-material/footwear-codes-terminology.md lines 1-12 for the exact shape, and {LANE}/corpus/knowledge/culture-material/headgear-head-covering-codes.md for the section style).
Required H2 sections in this order (the L1 inserts bullets under each; leave one line `<!-- BULLETS {{n}} -->` where the inserted bullets go):
## 1. What language socialization is (and is not)
## 2. Caregiver registers and the sound of talk to children
## 3. Turn-taking, babble and the first words
## 4. Correction, feedback and metalinguistic awareness
## 5. Field cases: the socialization paradigm at work
## 6. More than one language: bilingual and heritage childhoods
## 7. Narrative, literacy and schooled talk
## 8. Names, address and honorifics
## 9. What a worldbuilder does with this
plus a final `## 10. Handoff` section that hands canon to lore-shokunin (see PROVINCE.md; the entry ends at the handoff and decides nothing canon).

Write 2-5 short prose sentences per section that frame the bullets (no invented facts, no uncited claims \u2014 framing may be general method, never a factual assertion that would need a citation). Section 9 must be a decision table: a worldbuilder's choice (e.g. "the child is corrected openly / not at all") and its consequence for dialogue and social structure. Keep the whole file under 200 lines.
Also write `readme-row.txt` with the README index row: `- `language-socialization-and-acquisition.md` \u2014 <the entry's `- topic:` value verbatim> ` (one line, backticks around the filename exactly as shown).
Report: the file path, line count, H1/H2/H3 counts, the `- topic:` line, and your self-check.
""", ["coverage", "depth"])

    add("ExecIntegrate", "executor", GODSPEED + f"""
INTEGRATION-TOOL item (claim C). Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ExecIntegrate/ (mkdir -p).

Write `integrate.py`: a deterministic assembler the L1 will run from the lane root of {LANE}. It takes `--rows-dir /home/vgpnk/.cache/hyaku/kotodama-r64` and does, under `--root <lane>`:
1. Read every `ScribeRow*/row.txt` and `ScribeRej*/row.txt`; parse the labelled lines ROW/BULLET/VERIFY/CAPTURE/ACCESS (reject files: ROW/TEST/TEST2). Fail closed (exit 2, no writes) on any file that does not parse, any ROW whose cell count is not 11, any duplicate S-id, or any missing id in S718-S749.
2. Insert the 26 mined rows into `corpus/SOURCES.md` in ascending S-id order, appended after the current last row (base has 643 rows); insert the six rejected rows S744-S749 after them. Never modify an existing line. Preserve the table's exact cell style.
3. Build `{ENTRY}` from `ScribeEntrySkeleton/entry.md`: replace each `<!-- BULLETS n -->` with the bullets of the ids mapped to section n (mapping: 2=S718,S719,S729,S724; 3=S720,S721,S722,S723; 4=S725,S737,S743; 5=S726,S727,S728,S742,S738; 6=S730,S731,S732,S733; 7=S734,S735,S736; 8=S739,S740,S741), each bullet on its own line in ascending id order.
4. Insert the README index row after the last backtick-bulleted row of the `## linguistics/` section of `corpus/README.md`, bump that section header count `(29)` -> `(30)`, the `Total knowledge entries: N.` line 237 -> 238 if present, and the `Counts checked <date> ...` footer block's `(total N files; directory totals a/b/c/d/e/f)` + the six directory totals so they match the live tree. Read what the checks actually require in {LANE}/reports/round-28/readme/sweep.py (legs index/footer/block) and make your writer satisfy them; do not edit the sweep.
5. `--dry-run` prints the plan only. Default writes files.
Run it against a COPY of the lane (`cp -a {LANE} /home/vgpnk/.cache/hyaku/kotodama-r64/ExecIntegrate/lane-copy`) with synthetic fixture row files you create (S718-S749, plausible 11-cell lines) and show it produces a 675-row registry, a 238-entry README that `python3 -B reports/round-28/readme/sweep.py` accepts (exit 0) and an entry that `python3 -B tools/check-cited-lines.py` calls clean. Paste the commands and their output. Never run it on the real lane; the L1 runs it there.
Report: the script path, its CLI, the fixture run's output, and every check it enforces.
""", ["coverage", "operability"])

    add("ExecCaRepair", "executor", GODSPEED + f"""
Ca-REPAIR item (claim Ca, calibration). Work in a scratch copy only: `cp -a {LANE} /home/vgpnk/.cache/hyaku/kotodama-r64/ExecCaRepair/lane` (mkdir -p the parent first).

Read {LANE}/reports/round-64/accept-ca.py in full and {LANE}/corpus/lessons/round-63-verifier-spotcheck.md section 6 (routed defects 1-10). Then repair the routed bookkeeping defects in the COPY so that `python3 -B reports/round-64/accept-ca.py --root <copy>` prints every leg PASS and exits 0. The legs currently FAIL and the instrument is missing its `REVNAMES` leg (the docstring declares it; the code does not print it): add it, and keep the other legs' predicates unchanged.

What the legs require (read the code, it is authoritative):
- CANONLOG: a `Round-64` entry in the canonical root `LOG.md`, naming that `corpus/LOG.md` is the round-63 stray file and which file is canonical going forward.
- PTRS: `SCORECARD.md` and `corpus/LOG.md` no longer cite the dead `reports/round-63/telemetry/final-measures.txt`; they cite `final-measures-o.txt` / `final-measures-c.txt`; the O and C corrections are present.
- HISTOGRAM: the SCORECARD round-63 correction rows restate the tier split as A=13 B=11 with the census command.
- DISPO: the round-64 LOG entry disposes round-62 routed items 5, 6 and 7 explicitly (item 7 includes the S693 `kind` decision and the S687 mined->queued flip).
- REVNAMES (you add it): `reports/round-63/telemetry/revisions.txt` names the measured revision of every r63 receipt that lacked one: `8d2041fa` for final-measures-c.txt, `38ec1316` for final-measures-o.txt and rev-separability.txt, `0c892ce` for census-end.txt, `80ff34c` as the commit that carried the final-measures record. Keep the leg's predicate in the same style as the others (print PASS/FAIL + detail, count into the verdict).
- NITS: the SCORECARD round-63 correction row and the round-64 LOG entry correct three numeric nits (45 vs 47 seat reports; W04 names 27 duplicate-URL rows not S650/S651; 6 vs 9 dry-run FAIL legs).
- R63SEP: the round-64 LOG entry records the round-63 separability re-run (`SEPARABILITY: 2 findings`, exit 1), names the two findings' dependency class (counters are REC lands read by the acceptance runs; not an inter-claim dependency).

Edit only these files in the copy: `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt` (new), `reports/round-64/accept-ca.py`. Write the LOG entry as a real round-64 entry (this round's claims C/O/Ca). Keep every appended line factual: do not claim anything the round has not landed; where a value is not yet known write it as the check needs it and say so in your report.
Deliver: the full `diff -u` of the copy against the lane for those five paths, and the verbatim final output of `python3 -B reports/round-64/accept-ca.py --root <copy>` (all legs PASS, exit 0) plus the same command at the lane base showing the before FAILs.
""", ["calibration"])

    add("ExecOCounter", "executor", GODSPEED + f"""
CLAIM-O item (operability, counter hardening). You own ONE file: {LANE}/reports/round-64/accept-o.py (read it in full first; the L1 has a run in flight, so wait for a sentinel file {LANE}/reports/round-64/telemetry/dry-run-o.txt to exist, then copy it aside).

Work: run `cd {LANE} && python3 -B reports/round-64/accept-o.py --root .` to completion (it takes several minutes: DEFAULT 150 s, TIMEOUT, DRIP, MUT). Collect every FAIL. Then:
1. For each FAIL, decide from the code whether the leg or the fixture is wrong, or whether the unchanged tool `tools/reopen-row.py` genuinely does not hold the property the docstring claims. Freeze discipline: the predicate (ACCEPT-O-64: every leg PASS) does not change; a leg may be corrected pre-data when its expectation was wrong about the tool's committed behaviour, and the correction must be recorded as a revision with its forcing receipt. Never weaken a leg to make a real defect pass: if the tool genuinely lacks a property, record it as an open finding and say so \u2014 do not fake a PASS.
2. Produce the kill evidence: `python3 -B reports/round-64/accept-o.py --root . --only MUT` and the per-leg `--only EDGE_SCHEMEREL,EDGE_USERINFO,EDGE_HTTPS,EDGE_MALTARG,EDGE_SLASHLESS,EDGE_308,EDGE_5TH200,DRIP` run; every mutant must FAIL exactly its pinned leg.
3. Do-nothing control (the claim's anti-baseline): the round-63 counter must not be able to score these properties at all. Run `grep -nE 'EDGE_|DRIP' {LANE}/reports/round-63/accept-o.py` (expect no matches) and `python3 -B {LANE}/reports/round-63/accept-o.py --root {LANE} --only MUT` if it has such a leg (it does not) \u2014 record the command and output.
4. Write receipts into {LANE}/reports/round-64/telemetry/: `final-measures-o.txt` (the full run, header naming the measured revision `ff30a205c8d23b35f1ac533740121a955a9fda96` plus the sha256 of the counter), `mut-o.txt`, `edge-o.txt`, `control-o.txt`.
Constraints: edit ONLY reports/round-64/accept-o.py and files under reports/round-64/telemetry/. Never edit tools/reopen-row.py. Never run git/jj mutating commands. If you must revise the counter, append a `revision N` comment block at its docstring tail and say what forced it, and re-run ALL legs after the edit.
Report: every leg's final PASS/FAIL with its detail line, the mutations killed, the revision history and its forcing receipts, and any open finding.
""", ["operability"])

    add("ScoutLocatorRecon", "scout", GODSPEED + f"""
RECON item (claim C support). Read-only. Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScoutLocatorRecon/ (mkdir -p).

Produce `locator.md`: the exact, tested contract of the lane locator {LANE}/reports/round-61/reopen-quote.py, for the round's 32 row scribes.
- Run it against three known registry rows from {LANE}/corpus/SOURCES.md (pick S694, S700, S710) with `--row S###` from the lane root, and against two URLs you fetch with a plain GET where you also know a verbatim quote: show the LOCATED / NOT_LOCATED shapes, and the exit codes 0/1/2.
- Document: the 8-normalised-word minimum, the deny-host rule and url-reflects-quote rule, the three-attempt transient policy, `--row` vs `URL QUOTE`, and what a NOT_LOCATED reason means (fetch error vs absent text vs reflected quote).
- Document the archive-capture requirement: how to get a same-page `web.archive.org/web/<14-digit>id_/<original>` URL from `https://archive.org/wayback/available?url=` and what the answer looks like for a page with and without a capture.
- Give the scribes a copy-paste 6-command recipe that ends with a row they can file.
Do not write outside your scratch dir; do not fetch a page that answers a bot challenge (record it and stop).
Report the file, the three --row outputs verbatim, and the recipe.
""", ["coverage", "operability"])

    add("ScoutRegistryRecon", "scout", GODSPEED + f"""
RECON item (claim C). Read-only. Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScoutRegistryRecon/ (mkdir -p).

Produce `registry.md`: the exact cell rules and trap list for the round's 32 row scribes, derived from the repository, not from memory.
Read: {LANE}/CORPUS.md section `SOURCES.md — where a shokunin learns` (contract v1: shape, 11 cells, tiers, statuses), {LANE}/corpus/SOURCES.md (the last 24 rows S694-S717 as style exemplars \u2014 quote 3 of them verbatim), {LANE}/corpus/QUALITY.md criteria 6, 10, 12, 13, 16, and the ROWS/REJECTS/RESTATE legs of {LANE}/reports/round-64/accept-c.py.
Deliver: (a) the 11 cells with one-line rules and a good/bad example each; (b) the tier rule with three worked cases from the registry (why A, why B); (c) the exact `REJECTED: <reason>; flip: <...>` shape; (d) the ten most likely ways a scribe's row fails the counter, each with the symptom the counter prints (`ROWS FAIL` detail strings) \u2014 enumerate them from the code; (e) a checklist a scribe can run before filing.
Report the file and the checklist.
""", ["coverage"])

    add("ConnectorSiblings", "connector", GODSPEED + f"""
CONNECTOR item (sibling-overlap scan; adjacency axis evidence, not a claim). Read-only outside your scratch dir /home/vgpnk/.cache/hyaku/kotodama-r64/ConnectorSiblings/ (mkdir -p).

Scan the sibling lanes under /home/vgpnk/Projects/shokunin for prior art that this round would duplicate or should cite one-way:
1. The topic: language socialization / language acquisition in childhood. Check esp. lore-shokunin, kotoba-shokunin, chousa-shokunin, game-dev-*-shokunin, tabi-shokunin. Commands like `grep -rl -iE 'language socialization|language acquisition|motherese|child-directed' <lane>/corpus <lane>/*.md` \u2014 report file:line hits, and whether any sibling already owns the register.
2. The instruments: `reports/round-64/accept-o.py`'s redirect-edge battery and `reports/round-64/accept-ca.py`'s bookkeeping legs \u2014 does any sibling lane have an equivalent (e.g. chousa's quote-reopen, kumitate's proxy-check)?
Deliver `connector.md`: nearest prior art per surface, what is genuinely new, what must be cited one-way rather than restated, and any contested scope for the integrator. Name exact paths and quote the lines.
Do not write in any sibling repo. Report the file and a 5-line summary.
""", ["adjacency"])

    add("CriticClaimSizing", "critic", GODSPEED + f"""
CRITIC item (pre-data falsification of the round's claims). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/CriticClaimSizing/ (mkdir -p).

Attack the three declared claims before any data exists. Read {LANE}/reports/round-64/accept-c.py, accept-o.py, accept-ca.py (docstrings and code), {LANE}/SCORECARD.md (rounds 61-63 blocks), {LANE}/corpus/QUALITY.md, {LANE}/corpus/lessons/round-63-verifier-spotcheck.md, and the fleet rules /home/vgpnk/Projects/shokunin/AXES.md and /home/vgpnk/Projects/shokunin/LEARNING.md.
For each claim answer, with citations: (1) Is the axis named by the surface the round changes, not the number it produces? (2) Is the claim causally separable from the other two (no new id block shared, no path another claim lands, no counter reading another claim's record land)? (3) Can a do-nothing control reach the target? Name the cheapest control that skips the claimed work and say what it would score. (4) Is any clause unprovable by the declared commands (review-only)? List those clauses explicitly. (5) Is the target sized to one round, or is it a universal clause? (6) Does claim O's surface (`reports/round-64/accept-o.py`) count as operability, or is it a counter re-score of a rule the lane already holds (fleet lesson, kaidoku r29)? Argue both sides and give a verdict with reasons.
Write `critic.md` with a table: claim | attack | evidence pointer | verdict (holds / must change) | required change. Report the table.
""", ["calibration"])

    add("ReviewerPredicates", "reviewer", GODSPEED + f"""
REVIEWER item (QUALITY.md criteria 9 and 11: clause list vs commands). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/ReviewerPredicates/ (mkdir -p).

Take the three claims as stated in {LANE}/reports/round-64/claims.json if it exists, else from the docstrings of accept-c.py / accept-o.py / accept-ca.py. Build the clause list of each claim's statement (every count, path, form, index row, status, cell, "one new entry") and map each clause to the leg that checks it mechanically in the three counters. Flag: (a) a clause no leg checks (must be listed as review-only), (b) a leg that checks something the statement never claims (over-reach), (c) a clause whose leg is weaker than the words (e.g. "capture present" vs "same-page capture"), (d) any leg that cannot fail (a tautology \u2014 prove by reading the code), (e) any leg whose exit status the counter never reads.
Verify by execution where cheap: `python3 -B <counter> --root {LANE}` on the base tree, and one leg at a time with `--only`; paste the outputs. Do not modify the lane.
Write `review.md`: table clause | leg | mechanical? | verdict. Report the table and every clause you classify review-only.
""", ["calibration"])

    add("SentinelAccess", "sentinel", GODSPEED + f"""
SENTINEL item (source-access safety for 32 fetching seats). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/SentinelAccess/ (mkdir -p).

Deliver `access.md`, the rulebook the row scribes must follow, grounded in the repository's own incidents:
- Read {LANE}/corpus/QUALITY.md criterion 10 and 16, {LANE}/corpus/lessons/round-51.md (S094 bot challenge), {LANE}/corpus/lessons/round-62.md (safety hold) and {LANE}/corpus/lessons/round-63.md (hold lift), plus /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md lines about source access.
- Enumerate: (1) what counts as an ordinary open; (2) what must be recorded when a challenge is met and not passed; (3) the archive-capture rule (same page, `id_` form, 14-digit timestamp) and what an archived capture does not prove; (4) the private-host/loopback refusal in the locator and why a scribe must never point a row at a private address; (5) never run `tools/reopen-row.py` on live URLs without need and never against private/local services (round-62 hold, lifted only for the reviewed behaviours); (6) how to treat a page that serves a year-fabricated or AI-generated body (reject it, and file no row).
Add a 10-item pre-filing safety checklist. Report the file and the checklist.
""", ["calibration", "adjacency"])

    add("ScribeClaimsJson", "scribe", GODSPEED + f"""
DECLARATION item. Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/ (mkdir -p).

Write `claims.json` for round 64 in the shape of {LANE}/reports/round-63/claims.json (read it first): the three claims C, O, Ca, each with: axis, type (learning / capability / calibration), the falsifiable before -> after sentence, the frozen predicate verbatim (`ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS.` etc.), the declared counting/acceptance command, the declared lands (exact repo-relative paths each claim writes), the exported id block (C: S718-S749; O: none; Ca: none), the review-only clauses, and the base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`.
Then run /home/vgpnk/Projects/shokunin/scripts/hyaku/... if a separability checker exists in the lane (`python3 -B {LANE}/tools/check-claim-separability.py <your claims.json>` \u2014 if it needs a different input shape, read the tool and conform) and paste its output.
Also write `sources-frontier.md`: the curl of the Sources & frontier section: rows before 643, rows after 675 (26 mined + 6 rejected), the six reject rows named, and the census command.
Report: the JSON path, its top-level keys, the separability output verbatim, and any claim whose lands overlap another's.
""", ["calibration"])

    add("ScribeLessonDraft", "scribe", GODSPEED + f"""
LESSON-DRAFT item (frontier step 2b, mined mistake). Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeLessonDraft/ (mkdir -p).

Write `lesson.md` skeleton for {LANE}/corpus/lessons/round-64.md in the shape of {LANE}/corpus/lessons/round-63.md (read it in full: headings `## Round`, `## Gate`, `## Mistakes`, `## Sources & frontier`; the Gate lines are `- S### | URL | 2026-10-23 | "<verbatim <=25-word quote>"`, which the L1 fills from the row seats).
Your job:
1. `## Round`: the round's claims, base revision, what the round changed (fill placeholders `TBD-...` for values the L1 will substitute; say so in the header).
2. `## Mistakes`: at least two mistakes from THIS round or the immediately preceding ones, in the table shape `| R64-M1 | class | evidence pointer | captured-by (criterion/rule or none) | fix |`. Candidates to investigate (read the evidence, do not invent): the round-64 attempt 1 that died and left three uncommitted counter scripts at {LANE}/reports/round-64/ (what should have caught it: a dry-run receipt committed with the declaration; nothing did); the round-63 closure's step-1 `SHONEN` mapping defect (boxes 3 and 4 unanswered) and the LOG-file contract break (round-63 wrote `corpus/LOG.md` instead of root `LOG.md`). For each, name the criterion or rule that should have caught it, or `none`.
3. `## Gate`: the heading and the exact line format, with a note that the L1 inserts 26 lines; plus a subsection `### Re-open evidence` listing the six rejection re-tests (the L1 fills the verbatim outputs).
4. `## Sources & frontier`: the census command, the before value (643 rows, exit 0), and placeholders for the after value.
Keep every claim factual and every pointer resolvable. Report the file and the two mistake rows.
""", ["calibration", "coverage"])

    add("RevengerFrontier", "revenger", GODSPEED + f"""
REVENGER item (what round 63 actually did vs what its records say). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/RevengerFrontier/ (mkdir -p).

Reconstruct, from committed bytes only, how round 63 built its 24 rows and entry, and where its records diverge from its artifacts:
- `git -C {LANE} log --oneline ff30a20 | head -40`; `git -C {LANE} show --stat 8d2041fa`; diff the r63 entry `corpus/knowledge/culture-material/headgear-head-covering-codes.md` against the r61 exemplar `corpus/knowledge/culture-material/footwear-codes-terminology.md` (provenance trio present/absent, bullet shape, section count).
- Compare the r63 lesson Gate lines with the r63 registry rows S694-S717: does every quote in the Gate appear in its row's anchor cell? Any row whose quote is not in the Gate?
- Check the r63 wave reports under {LANE}/.ufo/waves/round-63/w1/ that wrote rows: did they record VERIFY locator output? (`grep -l 'LOCATED' ...`)
Deliver `revenger.md`: what a round-64 row seat must copy from round 63, what it must not, and any r63 record that would make a round-64 claim false if inherited. Report the file and a 6-line summary.
""", ["calibration"])

    spec = {
        "wave": "kotodama-r64-w1",
        "milestone": "Round 64 wave 1 (build): 26 sourced rows + 6 rejection rows + entry skeleton, claim-O counter verification, claim-Ca bookkeeping repairs, recon/critic/reviewer pre-data attacks",
        "reportDir": ".ufo/waves/round-64/w1",
        "axes": ["coverage", "operability", "calibration", "depth", "adjacency", "freshness"],
        "context": CONTEXT,
        "items": items,
    }
    out = pathlib.Path(__file__).with_name("w1-spec.json")
    out.write_text(json.dumps(spec, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    print(out)
    print(len(items), Counter(i["role"] for i in items))


if __name__ == "__main__":
    main()
