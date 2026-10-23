#!/usr/bin/env python3
"""Round-64 wave 2 spec generator (L1-owned, attempt 2).

Wave 2 = build-completion of claim C (6 missing rows, 6 row/reject repairs)
        + falsification of the inherited attempt-1 data (19 per-row quote
        reviews) + counter/instrument attacks + Ca/O execution seats.
"""
import json
import pathlib

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
CACHE = "/home/vgpnk/.cache/hyaku/kotodama-r64"
GODSPEED = """/skill:godspeed
You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim \u2014 let the frontier walk itself.**

## IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches. Do not serialize what can run in parallel. Do not output philosophical reasoning or verbose plans. Act directly via tool calls.
"""

CONTEXT = """# Goal
Kotodama round 64 (hyaku run 5, 2026-10-23), wave 2: build-completion + falsification. Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (branch main, jj-colocated), base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`.

Round 64 declares three claims, each with a frozen predicate:
- C (coverage, sourced): a new entry `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` plus exactly 26 new registry rows S718-S743 (all `mined`) and six disposition rows S744-S749. Predicate: `ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS`. Read that file's docstring for the exact per-leg rules; it is authoritative.
- O (operability, counter hardening): `reports/round-64/accept-o.py` pins seven redirect-edge properties, a DRIP wall-budget distinction and ten mutants against the unchanged lane tool `tools/reopen-row.py`. Predicate: `ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS`.
- Ca (calibration): the round-63 closure's routed bookkeeping defects, verified by `reports/round-64/accept-ca.py`. Predicate: `ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py prints PASS`.

Wave 1 (attempt 1 of this round) landed 24 seat reports and 19 usable row drafts before the orchestrator died. This wave completes the six missing rows, repairs six drafts, and attacks what wave 1 asserted. Your job is ONE item; do it and report.

# Bounds (hard)
- Do NOT write anything inside /home/vgpnk/Projects/shokunin/kotodama-shokunin or any other repo unless your item explicitly says so. Your writable directory is /home/vgpnk/.cache/hyaku/kotodama-r64/<YourSeatName>/ (mkdir -p it) or the path your item names. The L1 integrates your files.
- Never touch the fleet repo, sibling lanes, lane jj state or the lane Git index. Never run `git add`, `git commit`, `git stash`, `git checkout`, `git switch`, `git reset`, `git pull`, `git push` or any mutating `jj` command. Read-only git is fine.
- Every `Report:` trailer path the harness prints is relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin \u2014 write it at /home/vgpnk/Projects/shokunin/kotodama-shokunin/<that path> ONLY if your item says to; otherwise ignore the trailer and write in your scratch dir.
- Never message `agent://all`. Reply to the L1 by your final message only.
- Tooling authorization (operator, 2026-10-19): you may install or upgrade tools that help the task \u2014 read /home/vgpnk/.omp/agent/RULES.md first (official channels only; record tool/version/channel/reason in your report). PACMAN GUARD: all pacman transactions are PAUSED host-wide; install via `uv tool`/`npx`/an official binary in ~/.local/bin only, or file an L0 question. Never `-Sy`, `-Syu`, `-U`, `-R`, downgrade, or restart a host service.
- Sources are opened by ordinary means only (QUALITY.md criterion 10): a plain GET, a public copy, an archive capture or a library scan. Never solve a captcha, pass a bot challenge with browser automation, or bypass a paywall/login/geo block. A challenge met and routed around by an ordinary archived copy is fine and must be recorded as `challenge met, not passed`.

# Registry row format (claim C)
`| S### | <citation> - <live URL> ; capture <web.archive.org capture URL> | <kind> | <tier> | <scope> | <anchor locator>: "<verbatim quote>" | <teaches> | <status> | 2026-10-23 | 180d | <used-by> |` \u2014 exactly 11 cells, no `|` inside a cell.
- kind: spec, docs, paper, code, tool, dataset, talk, book, community, own-work.
- Tier is scoped to the row's `scope`, never global. A = primary or authoritative for exactly that scope (the original paper, official docs, the source's own record). B = strong secondary (expert write-up, survey, textbook, encyclopedia overview, publisher abstract). C = lead only, never sole support for an admitted claim. `community` is never A.
- Anchor quote: verbatim, contiguous, 8-25 normalised words, from body text (never a caption, alt/title attribute, or navigation text), inside double quotes.
- Lane locator for verification: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py <URL> "<quote>"` prints one line `LOCATED <url>` (exit 0) or `NOT_LOCATED <reason>` (exit 1). At least 8 normalised words are required.
- Same-page archive capture: `curl -s "https://archive.org/wayback/available?url=<URL>"` and use its `timestamp` + `original` as `https://web.archive.org/web/<timestamp>id_/<original>`.

# Round-64 attempt-1 inheritance (what this wave must treat as suspect)
Wave 1's drafts are in /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRow<S###>/row.txt. They were written by seats that died with the orchestrator; nothing about them has been independently verified. Treat every inherited line as a claim to re-check, never as ground truth.
"""

ENTRY = "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"


def row_prompt(sid, topic, query):
    return (
        GODSPEED
        + f"""
ROW item (claim C). ID {sid}. Topic: {topic}. Entry section it feeds: ## {SECTION[sid]}.
Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRow{sid}/ (mkdir -p).

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
Rules for BULLET (checked mechanically): one line, at least 5 content words in the clause before `({sid})`; keep at least three distinctive words of your quote in the quote's own order; add at least one content word that is not in the quote; never copy more than 12 consecutive words from the quote; exactly one S-id on the line, at the end, in parentheses.
6. Self-check before finishing: re-run the locator once more from the lane root and paste its line; count the ROW cells (`awk -F'|'` gives 13 fields for 11 cells); count your quote's words (8-25).
Report in your final message: the ROW line, the BULLET line, the VERIFY line, tier and why, and anything that failed.
"""
    )


def repair_prompt(sid, problems, extra):
    return (
        GODSPEED
        + f"""
ROW-REPAIR item (claim C). ID {sid}. Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/w2/Fix{sid}/ (mkdir -p).

The inherited draft {CACHE}/ScribeRow{sid}/row.txt fails the round-64 counter with: {problems}.
Read the draft, re-open its source yourself, and write a corrected `row.txt` in your scratch dir with the SAME labelled format (ROW / BULLET / VERIFY / CAPTURE / ACCESS). The row must keep the same source unless that source cannot support a compliant quote, in which case say so and pick another source that can.
{extra}
Mechanical rules the counter enforces (read {LANE}/reports/round-64/accept-c.py legs ROWS and RESTATE; they are authoritative):
- ROW: exactly 11 cells; tier A or B; status `mined`; opened `2026-10-23`; recheck `180d`; used-by `{ENTRY}`; anchor quote inside double quotes, 8-25 normalised words, verbatim body text; live URL plus a same-page `web.archive.org/web/<14-digit>id_/<original>` capture whose original normalises equal to the live URL.
- BULLET: `- <clause> ({sid})`; clause has >= 5 content words (>=4 letters, not a stopword); at least 3 of the clause's content words appear in the anchor quote in the quote's own order; at least one content word not in the quote; no run of more than 12 consecutive clause words copied from the quote; exactly one S-id, at the end.
Re-run the locator from the lane root and paste its first line: `cd {LANE} && python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'` must print `LOCATED <url>`.
Report: the corrected ROW line, the corrected BULLET line, the VERIFY line, and the locator output.
"""
    )


def reject_repair_prompt(sid, problems, extra):
    return (
        GODSPEED
        + f"""
REJECTION-ROW REPAIR item (claim C). ID {sid}. Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/w2/Rej{sid}/ (mkdir -p).

The inherited draft {CACHE}/ScribeRej{sid}/row.txt (or its absence) fails the round-64 counter with: {problems}.
Read {LANE}/corpus/lessons/round-63.md for the candidate and its original reject ground, and re-test it yourself with ordinary tools:
`curl -sS -o /dev/null -w '%{{http_code}} %{{url_effective}}' -L --max-time 60 '<URL>'` and, where a quote is involved,
`cd {LANE} && python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'`. Never solve a challenge or bypass a paywall.
{extra}
Write `row.txt` with EXACTLY these labelled lines:

ROW: | {sid} | <the candidate as cited, with its URL> | <kind> | <tier> | <what it would have supported> | <locator tested>: "<the wording tested>" | <REJECTED: reason; flip: what would change the verdict> or <QUEUED-CANDIDATE: reason; flip: ...> | <rejected or queued> | 2026-10-23 | 180d | \u2014 |
TEST: <the verbatim output of the re-test command(s)>
TEST2: <the verbatim locator first line, or "not applicable">

Rules (accept-c.py leg REJECTS is authoritative): exactly 11 cells; status exactly `rejected` or `queued` (never `QUEUED-CANDIDATE` in the status cell); teaches starts `REJECTED:` or `QUEUED-CANDIDATE:` and contains `; flip:`; used-by exactly `\u2014`; no `|` inside a cell.
If the re-test CONTRADICTS the original ground (the page now serves the entry, or the locator finds the wording), file the honest queued-candidate disposition instead of a false rejection and say so.
Report: the ROW line, the verbatim test output(s), whether the ground still holds, and the URL.
"""
    )


SECTION = {
    "S718": 2, "S719": 2, "S729": 2, "S724": 2,
    "S720": 3, "S721": 3, "S722": 3, "S723": 3,
    "S725": 4, "S737": 4, "S743": 4,
    "S726": 5, "S727": 5, "S728": 5, "S742": 5, "S738": 5,
    "S730": 6, "S731": 6, "S732": 6, "S733": 6,
    "S734": 7, "S735": 7, "S736": 7,
    "S739": 8, "S740": 8, "S741": 8,
}

MISSING_ROWS = [
    ("S721", "turn-taking and protoconversation in infancy", "protoconversation infant turn-taking development review"),
    ("S727", "Samoan child language socialization (Ochs)", "Ochs Samoan language socialization children"),
    ("S733", "sign language acquisition by deaf children of deaf parents", "deaf children sign language acquisition native signers"),
    ("S740", "honorifics and keigo acquisition", "Japanese honorifics keigo acquisition children"),
    ("S741", "taboo words and avoidance taught to children", "taboo words children avoidance socialization study"),
    ("S743", "a named child-language register", "Japanese child language register nyuyoji-go"),
]

REPAIRS = [
    ("S719", "quote_words=5 in_order=0",
     "The anchor quote `Effects of IDS on Performance` is a section heading, not body text, and has 5 words. Pick a verbatim 8-25 word body sentence that supports the inherited bullet's claim about infant attention to infant-directed speech, and rewrite the bullet to follow that quote."),
    ("S738", "in_order=0",
     "The anchor quote is 8 words but it is a section heading in capitals. Replace it with a verbatim body sentence of 8-25 words from the same paper that supports the claim about expert advice shaping the family's language choices, and rewrite the bullet so at least three of its content words follow the quote's own order."),
    ("S739", "in_order=2",
     "The anchor quote `Term of Address as Form of Language Socialization in Children` is an article title, not body text. Replace it with a verbatim 8-25 word body sentence about terms of address used to children, and rewrite the bullet so at least three of its content words follow the quote's own order."),
    ("S742", "quote_words=3 in_order=0",
     "The anchor quote `Morning Meeting Greetings` is a heading with 3 words. Replace it with a verbatim 8-25 word body sentence from the PDF about the explicitly taught greeting routine (the draft's own VERIFY line cites the p. 48 passage), and rewrite the bullet to follow that quote."),
]

REJ_REPAIRS = [
    ("S746", "cells=0 (the inherited file has no parseable ROW line)",
     "The round-63 lesson records a Wikisource Smith Corona page whose text did not carry the quoted wording. Reconstruct the page, test it, and file the row."),
    ("S748", "status=QUEUED-CANDIDATE (the status cell must be `queued`), anchor quote 1 word",
     "Wave 1's own report says the LacusCurtius Corona path answered 200 and LOCATED, contradicting the original reject ground. File the queued-candidate row with the tested wording as a real 8-25 word quote if the locator confirms it."),
]


def main():
    items = []

    def add(name, role, prompt, axes):
        items.append({"name": name, "role": role, "prompt": prompt, "axes": axes})

    # ---- build: six missing rows ----
    for sid, topic, query in MISSING_ROWS:
        add(f"B2ScribeRow{sid}", "scribe", row_prompt(sid, topic, query), ["coverage"])
    # ---- build: four mined-row repairs + two disposition repairs ----
    for sid, problems, extra in REPAIRS:
        add(f"B2Fix{sid}", "scribe", repair_prompt(sid, problems, extra), ["coverage"])
    for sid, problems, extra in REJ_REPAIRS:
        add(f"B2Rej{sid}", "scribe", reject_repair_prompt(sid, problems, extra), ["coverage"])

    # ---- falsify: one reviewer per inherited row draft ----
    for sid in ["S718", "S719", "S720", "S722", "S724", "S725", "S726", "S728",
                "S729", "S730", "S731", "S732", "S734", "S735", "S736", "S737",
                "S738", "S739", "S742"]:
        add(f"B2ReviewRow{sid}", "reviewer", GODSPEED + f"""
ROW-REVIEW item (falsify claim C's inherited data). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRow{sid}/ (mkdir -p).

Wave 1 (attempt 1) drafted registry row {sid} in {CACHE}/ScribeRow{sid}/row.txt. Nothing in it has been independently verified; the round counter only checks shape. Your job is to falsify its content.

1. Read the draft and the counter's rules ({LANE}/reports/round-64/accept-c.py, legs ROWS and RESTATE).
2. Open the row's live URL with a plain GET (`curl -sL --max-time 90 -o body.html -w '%{{http_code}} %{{url_effective}}' '<URL>'`) and fetch the archive capture too. Record both HTTP results verbatim.
3. Search the fetched body for the row's anchor quote. It must appear verbatim and contiguously in the page's body text, not only in a heading, caption, alt/title attribute or navigation. Use `python3 -c` with a normaliser that matches the counter's (`NFKC`, casefold, non-word -> space). Report the exact hit context (200 chars either side) or its absence.
4. Re-run the lane locator yourself and paste the first line: `cd {LANE} && python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'`.
5. Check the citation line against the page: author(s), year, title, publication. Flag a wrong year, a wrong author list, a wrong journal/volume/pages, or a title that is not the page's title.
6. Check the tier claim: is the source genuinely A (or B) for exactly the scoped topic the row names? Name the evidence.
7. Check the BULLET against the quote: does the clause assert only what the quote establishes (no overreach, no invented number), and does it satisfy the RESTATE rules? Quote the offending words.

Write `review.md` with a verdict table: field | draft value | verified? | evidence (verbatim) | required fix. End with one line `VERDICT: <CLEAN|FIX-REQUIRED> <one-line reason>`.
Do not edit the draft or the lane. Report the verdict line, the HTTP results, and every required fix.
""", ["coverage", "calibration"])

    # ---- instrument attacks ----
    add("B2CriticClaims", "critic", GODSPEED + f"""
CRITIC item (pre-data falsification of the round's three claims). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2CriticClaims/ (mkdir -p).

Read {LANE}/reports/round-64/claims.json, accept-c.py, accept-o.py, accept-ca.py, {LANE}/SCORECARD.md rounds 61-63, {LANE}/corpus/QUALITY.md, {LANE}/corpus/lessons/round-63-verifier-spotcheck.md, and /home/vgpnk/Projects/shokunin/AXES.md + LEARNING.md.
For each claim, with citations: (1) is the axis named by the surface the round changes, not by the number it produces? (2) is it causally separable from the other two (no shared exported id, no path another claim lands, no counter reading another claim's land)? (3) can a do-nothing control reach the target — name the cheapest control that skips the claimed work and what it would score? (4) which clauses are unprovable by the declared commands (review-only)? (5) is the target sized to one round, or a universal clause? (6) for claim O: is pinning edge properties of an unchanged tool a genuine operability move or a counter re-score of a rule the lane already holds (fleet lesson kaidoku r29)? Argue both sides and rule.
Write `critic.md`: table claim | attack | evidence pointer | verdict (holds / must change) | required change. Report the table and every clause you classify review-only.
""", ["calibration"])

    add("B2ReviewerPredicates", "reviewer", GODSPEED + f"""
CLAUSE-MAP item (QUALITY.md criteria 9 and 11). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewerPredicates/ (mkdir -p).

Take each claim's statement verbatim from {LANE}/reports/round-64/claims.json. Split it into clauses (every count, path, form, index row, status, cell, "one new entry", "ten byte-patched mutants"). Map each clause to the leg that checks it mechanically in accept-c.py / accept-o.py / accept-ca.py. Flag: (a) a clause no leg checks (must be listed review-only), (b) a leg that checks something the statement never claims, (c) a clause whose leg is weaker than the words, (d) a leg that cannot fail (prove by reading the code), (e) a leg whose exit status the counter never reads.
Verify by execution where cheap: `cd {LANE} && python3 -B reports/round-64/accept-c.py --root .` and `python3 -B reports/round-64/accept-ca.py --root .`; paste the outputs. Do not modify the lane.
Write `clause-map.md`: table clause | leg | mechanical? | verdict. Report the table and every review-only clause.
""", ["calibration"])

    add("B2SentinelAccess", "sentinel", GODSPEED + f"""
SENTINEL item (source-access safety for the round's fetching seats). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2SentinelAccess/ (mkdir -p).

Deliver `access.md`, the rulebook the row seats must follow, grounded in this repository's own incidents: {LANE}/corpus/QUALITY.md criteria 10 and 16; {LANE}/corpus/lessons/round-51.md (bot challenge), round-62.md (safety hold), round-63.md (hold lift); and /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md lines about source access.
Enumerate: (1) what counts as an ordinary open; (2) what must be recorded when a challenge is met and not passed; (3) the archive-capture rule (`id_` form, 14-digit timestamp) and what an archived capture does not prove; (4) why a row must never point at a private/loopback address; (5) never run `tools/reopen-row.py` on live URLs without need and never against private/local services; (6) how to treat a page that serves a fabricated or AI-generated body (reject it, file no row).
Add a 10-item pre-filing safety checklist, then audit the 19 inherited wave-1 row drafts for access-policy violations (grep their ACCESS lines and the hosts they point at) and list any violation with the file path.
Report the file, the checklist, and the audit result.
""", ["calibration", "adjacency"])

    add("B2ConnectorSiblings", "connector", GODSPEED + f"""
CONNECTOR item (sibling-overlap scan; adjacency evidence, not a claim). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ConnectorSiblings/ (mkdir -p).

Scan the sibling lanes under /home/vgpnk/Projects/shokunin for prior art this round would duplicate or must cite one-way:
1. Topic `language socialization / language acquisition in childhood`: check lore-shokunin, kotoba-shokunin, chousa-shokunin, tabi-shokunin and the game-dev lanes with `grep -rl -iE 'language socialization|language acquisition|motherese|child-directed|infant-directed' <lane>/corpus <lane>/*.md`. Report file:line hits and whether a sibling already owns the register.
2. Instruments: does any sibling have an equivalent of `reports/round-64/accept-o.py`'s redirect-edge battery or of a bookkeeping counter like `accept-ca.py`?
Write `connector.md`: nearest prior art per surface, what is genuinely new, what must be cited one-way, and any contested scope for the integrator. Name exact paths and quote the lines. Do not write in any sibling repo.
Report the file and a 5-line summary.
""", ["adjacency"])

    add("B2RevengerFrontier", "revenger", GODSPEED + f"""
REVENGER item (what round 63 actually did vs what its records say). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2RevengerFrontier/ (mkdir -p).

Reconstruct from committed bytes only how round 63 built its 24 rows and entry, and where its records diverge from its artifacts:
- `git -C {LANE} log --oneline ff30a20 | head -40`; `git -C {LANE} show --stat 8d2041fa`; diff the r63 entry `corpus/knowledge/culture-material/headgear-head-covering-codes.md` against the r61 exemplar `corpus/knowledge/culture-material/footwear-codes-terminology.md` (provenance trio, bullet shape, section count).
- Compare the r63 lesson Gate lines with the r63 registry rows S694-S717: does every Gate quote appear in its row's anchor cell? Name any row whose quote is missing from the Gate.
- Check which r63 wave reports under {LANE}/.ufo/waves/round-63/w1/ recorded VERIFY locator output (`grep -l LOCATED ...`).
Write `revenger.md`: what a round-64 row must copy from round 63, what it must not, and any r63 record that would make a round-64 claim false if inherited. Report the file and a 6-line summary.
""", ["calibration"])

    add("B2ScoutRegistry", "scout", GODSPEED + f"""
RECON item (claim C). Read-only outside /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ScoutRegistry/ (mkdir -p).

Produce `registry.md`: the exact cell rules and trap list for the round's row seats, derived from the repository, not memory.
Read {LANE}/CORPUS.md section `SOURCES.md — where a shokunin learns` (contract v1), {LANE}/corpus/SOURCES.md last 24 rows S694-S717 as style exemplars (quote 3 verbatim), {LANE}/corpus/QUALITY.md criteria 6, 10, 12, 13, 16, and the ROWS/REJECTS/RESTATE legs of {LANE}/reports/round-64/accept-c.py.
Deliver: (a) the 11 cells with one-line rules and a good/bad example each; (b) the tier rule with three worked cases from the registry; (c) the exact `REJECTED: <reason>; flip: <...>` shape; (d) the ten most likely ways a row fails the counter, each with the symptom string the counter prints, enumerated from the code; (e) a pre-filing checklist.
Report the file and the checklist.
""", ["coverage"])

    add("B2ScribeLesson", "scribe", GODSPEED + f"""
LESSON-DRAFT item (frontier step 2b). Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ScribeLesson/ (mkdir -p).

Write `lesson.md` skeleton for {LANE}/corpus/lessons/round-64.md in the shape of {LANE}/corpus/lessons/round-63.md (read it in full: headings `## Round`, `## Gate`, `## Mistakes`, `## Sources & frontier`; Gate lines are `- S### | URL | 2026-10-23 | "<verbatim <=25-word quote>"`).
1. `## Round`: the three claims, base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`, and what the round changed; use placeholders `TBD-...` for values the L1 substitutes and say so in the header.
2. `## Mistakes`: at least three mistakes with evidence, in the table shape `| R64-M1 | class | evidence pointer | captured-by (criterion/rule or none) | fix |`. Investigate (do not invent): (a) attempt 1 died leaving three uncommitted counter scripts under {LANE}/reports/round-64/ \u2014 what should have caught it? (b) round 63 wrote its log entry to `corpus/LOG.md` while the canonical log is root `LOG.md`; (c) round 63's closure step-1 SHONEN mapping left boxes 3 and 4 unanswered; (d) six of 26 row drafts never landed because the wave died \u2014 name the rule that should have caught the missing coverage. For each name the criterion/rule or `none`.
3. `## Gate`: the heading, the line format, and a note that the L1 inserts 26 lines; plus `### Re-open evidence` for the six disposition rows.
4. `## Sources & frontier`: the census command, the before value (643 rows), and placeholders for the after value.
Every claim factual, every pointer resolvable. Report the file and the three mistake rows.
""", ["calibration", "coverage"])

    add("B2MutationC", "mutation-tester", GODSPEED + f"""
MUTATION item (does ACCEPT-C-64 have teeth?). Work in a scratch copy only: `cp -a {LANE} /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2MutationC/lane` (mkdir -p the parent first).

The counter {LANE}/reports/round-64/accept-c.py currently FAILs on the base tree because the claim-C data is not landed. Build the mutant battery against a SYNTHETIC passing tree you construct in the copy: create a plausible entry file and 26 registry rows + 6 disposition rows that pass every leg (you may reuse the inherited drafts at {CACHE}/ScribeRow*/row.txt and the entry skeleton at {CACHE}/ScribeEntrySkeleton/entry.md; fixing them until the counter passes is part of the item). Record that construction honestly as a fixture, not as round data.
Then, from that passing tree, produce byte-level mutants \u2014 one per pinned property \u2014 and show each one flips its own leg to FAIL while the others stay PASS:
1. two S-ids on one entry line (ONEID); 2. a row with status `queued` instead of `mined` (ROWS); 3. a quote of 5 words (ROWS); 4. a capture URL whose original differs from the live URL (ROWS); 5. a bullet with only 2 content words (RESTATE); 6. a bullet that copies 15 consecutive quote words (RESTATE); 7. a rejected row whose teaches lacks `; flip:` (REJECTS); 8. a duplicate live URL in a second row (LINK); 9. a base row deleted from the registry (APPEND); 10. a second entry file under corpus/knowledge (NOHARM); 11. an entry with an H3 (FILE); 12. a README row whose topic text differs from the entry's `- topic:` (SWEEP).
For each mutant paste the command and the counter's output line for the flipped leg plus one still-PASS leg as the control.
Write `mutation.md`: table mutant | leg | before | after | control leg still PASS. Report the table, the fixture construction steps, and every mutant that did NOT flip its leg.
""", ["calibration", "coverage"])

    add("B2MutationO", "mutation-tester", GODSPEED + f"""
MUTATION item (does ACCEPT-O-64 have teeth?). Work in a scratch copy only: `cp -a {LANE} /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2MutationO/lane` (mkdir -p the parent first).

Read {LANE}/reports/round-64/accept-o.py in full (docstring, legs, mutant battery). In the copy, run `python3 -B reports/round-64/accept-o.py --root <copy>` and, if it FAILs, determine per leg whether the leg or its fixture is wrong (never weaken a leg to make a real tool defect pass).
Then take the counter's own mutant battery (`--only MUT`) and additionally hand-build three mutants of your own against properties the battery may not pin: a redirect chain of 6 hops (limit 5), a `Location:` header with an uppercase scheme (`HTTPS://`), and a 200 body whose quote appears only inside an `alt=` attribute (must not count as LOCATED). Show each mutant's target leg, before/after.
Write `mutation-o.md`: table mutant | leg | before | after | control. Report the table, the full run's per-leg verdicts, and every leg whose expectation you believe is wrong with the evidence.
""", ["calibration", "operability"])

    add("B2ExecEntry", "executor", GODSPEED + f"""
EXECUTOR item (claim C integration: entry + README, in a copy). Work only in /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/ (mkdir -p); copy the lane with `cp -a {LANE} lane`.

Write `assemble_entry.py`: given the lane copy as --root and a bullets JSON `{CACHE}/w2/bullets.json` (mapping S-id -> bullet line), it builds `{ENTRY}` from `{CACHE}/ScribeEntrySkeleton/entry.md`, replacing every `<!-- BULLETS n -->` with the bullets of the ids mapped to section n (mapping: 1=S726; 2=S718,S719,S729,S724; 3=S720,S721,S722,S723; 4=S725,S737,S743; 5=S727,S728,S742,S738; 6=S730,S731,S732,S733; 7=S734,S735,S736; 8=S739,S740,S741), each bullet on its own line in ascending id order.
Then insert the README index row (`{CACHE}/ScribeEntrySkeleton/readme-row.txt`) after the last backtick-bulleted row of the `## linguistics/` section of `corpus/README.md`, bump that section header count `(29)` -> `(30)`, the `Total knowledge entries: N.` line 237 -> 238 if present, and fix the `Counts checked` footer block so `python3 -B reports/round-28/readme/sweep.py` exits 0. Read that sweep's legs first; never edit the sweep.
Prove it: run it on the copy with a synthetic bullets JSON covering all 26 ids (invent plausible bullets), then run the sweep and `python3 -B tools/check-cited-lines.py <entry>` and paste both outputs. Also paste the resulting entry's line count and H1/H2/H3 counts.
Report: the script path and CLI, the sweep output, the cited-lines output, and the line/H counts.
""", ["coverage", "operability"])

    add("B2ExecCaRepair", "executor", GODSPEED + f"""
EXECUTOR item (claim Ca, calibration bookkeeping). Work in a scratch copy only: `cp -a {LANE} /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecCaRepair/lane` (mkdir -p the parent first).

Read {LANE}/reports/round-64/accept-ca.py in full and {LANE}/corpus/lessons/round-63-verifier-spotcheck.md section 6 (routed defects 1-10). Repair the routed bookkeeping defects in the COPY so `python3 -B reports/round-64/accept-ca.py --root <copy>` prints every leg PASS and exits 0.
Legs (read the code; it is authoritative): CANONLOG (a `Round-64` entry in the canonical root `LOG.md` naming `corpus/LOG.md` as the round-63 stray and which file is canonical), PTRS (no citation of the dead `reports/round-63/telemetry/final-measures.txt`; cite `final-measures-o.txt` / `final-measures-c.txt`; the O and C corrections present), HISTOGRAM (the tier split restated as A=13 B=11 with the census command), DISPO (round-62 routed items 5, 6, 7 disposed explicitly, incl. the S693 kind decision and the S687 mined->queued flip), REVNAMES (the leg exists in the code; `reports/round-63/telemetry/revisions.txt` names the measured revision of every r63 receipt that lacked one: 8d2041fa for final-measures-c.txt, 38ec1316 for final-measures-o.txt and rev-separability.txt, 0c892ce for census-end.txt, 80ff34c for the final-measures record), NITS (three numeric nits: 45 vs 47 seat reports; W04 names 27 duplicate-URL rows not S650/S651; 6 vs 9 dry-run FAIL legs), R63SEP (the round-63 separability re-run `SEPARABILITY: 2 findings` exit 1 recorded, with the dependency class named).
Edit only these files in the copy: `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt`, `reports/round-64/accept-ca.py` (only if a leg is genuinely broken). Keep every appended line factual; where a value is not yet known write the check's required value and say so in your report.
Deliver: the full `diff -u` of the copy against the lane for those paths, the verbatim final output of `python3 -B reports/round-64/accept-ca.py --root <copy>` (all legs PASS, exit 0), and the same command at the lane base showing the before FAILs.
""", ["calibration"])

    add("B2ExecOCounter", "executor", GODSPEED + f"""
EXECUTOR item (claim O). You own ONE file: {LANE}/reports/round-64/accept-o.py (read it in full first; a run may be in flight \u2014 if {LANE}/reports/round-64/telemetry/final-measures-o.txt exists, copy it aside before touching anything).

Run `cd {LANE} && python3 -B reports/round-64/accept-o.py --root .` to completion (several minutes: DEFAULT 150 s, TIMEOUT, DRIP, MUT). Collect every FAIL. For each: decide from the code whether the leg or the fixture is wrong, or whether the unchanged tool `tools/reopen-row.py` genuinely lacks the property. The predicate (`ACCEPT-O-64: every leg PASS`) does not change; a leg may be corrected pre-data when its expectation was wrong about the tool's committed behaviour, and the correction must be recorded as a `revision N` docstring block with its forcing receipt. Never weaken a leg to make a real defect pass: a genuine tool defect is an open finding, reported, not hidden.
Produce the kill evidence: `python3 -B reports/round-64/accept-o.py --root . --only MUT` and the per-leg `--only EDGE_SCHEMEREL,EDGE_USERINFO,EDGE_HTTPS,EDGE_MALTARG,EDGE_SLASHLESS,EDGE_308,EDGE_5TH200,DRIP` run; every mutant must FAIL exactly its pinned leg.
Do-nothing control: show the round-63 counter cannot score these properties at all (`grep -nE 'EDGE_|DRIP' {LANE}/reports/round-63/accept-o.py` \u2014 expect no matches; paste it).
Write receipts into {LANE}/reports/round-64/telemetry/: `final-measures-o.txt` (full run, header naming the measured revision and the counter's sha256), `mut-o.txt`, `edge-o.txt`, `control-o.txt`.
Constraints: edit ONLY reports/round-64/accept-o.py and files under reports/round-64/telemetry/. Never edit tools/reopen-row.py. Never run git/jj mutating commands. Re-run ALL legs after any edit.
Report: every leg's final PASS/FAIL with detail, the mutations killed, the revision history with forcing receipts, and any open finding.
""", ["operability"])

    spec = {
        "wave": "kotodama-r64-w2",
        "milestone": "Round 64 wave 2 (attempt 2): build-completion of claim C (6 missing rows, 4 mined repairs, 2 disposition repairs) + 19 per-row falsification reviews + instrument attacks + Ca/O executor seats",
        "reportDir": ".ufo/waves/round-64/w2",
        "axes": ["coverage", "operability", "calibration", "depth", "adjacency"],
        "context": CONTEXT,
        "items": items,
    }
    out = pathlib.Path(__file__).with_name("w2-spec.json")
    out.write_text(json.dumps(spec, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    print(out)
    print(len(items), Counter(i["role"] for i in items))


if __name__ == "__main__":
    main()
