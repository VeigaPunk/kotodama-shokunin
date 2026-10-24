#!/usr/bin/env python3
"""Generate the round-65 single v2 wave spec (64 seats, >=25% attack roles), compact bodies."""
import json

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"

CONTEXT = """# Goal
Kotodama round 65 (hyaku run 5, 2026-10-24): ONE v2 wave of 64 seats, build+attack together. Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (jj-colocated; base revision 17c32302c6845c8f164b985a8cb312d3181c8788). All lane-relative paths below resolve under that repo. Three claims with frozen predicates (reports/round-65/claims.json, written pre-wave):
- C (coverage, sourced): new entry corpus/knowledge/culture-material/games-play-sport-contests.md + exactly 26 mined registry rows S750-S775 (tier A/B, opened 2026-10-24, used-by the entry, cited exactly once each). Predicate: ACCEPT-C-65: every leg of reports/round-65/accept-c.py prints PASS.
- O (operability, counter hardening): the round-64 routed counter-gaming surfaces closed in the frozen round-65 counters (accept-c rev1 RESTATE word-boundary near-copy rule; accept-o rev1 FULL/MUTEX/FRAG; tools/check-row-fragments.py teaches-length + query-aware URL normalization). Predicate: ACCEPT-O-65: every leg of reports/round-65/accept-o.py prints PASS.
- Ca (calibration, records): the round-64 closure's routed defects R1-R7 dispositioned with counting legs (reports/round-65/accept-ca.py legs R1..R7, CRITERION, QUOTES; corpus/lessons/round-64-verifier-spotcheck.md section 6 defines R1-R7).
Frozen counters, claims.json, base dry-run receipts (reports/round-65/telemetry/dry-run-*.txt) and pre-data controls (controls-c.txt) are on disk at the lane tip - read them before attacking. Build seats: your output is a draft under .ufo/waves/round-65/ - the L1 reviews, integrates and is the only committer. Attack seats: try to break the frozen instruments and drafts - shortcut classes, bypasses, stale receipts, false stamps, duplicates, tier inflation, fabricated anchors; name what you attack.

# Rules (bind every seat)
Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
Leaf member - no subagent dispatch, no swarm of your own. Absolute paths for writes, under /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-65/ only, at the exact paths your item names. Never mutate the fleet repo, sibling lanes, lane jj state or the lane Git index; never run git/jj writes; read-only git is fine; do not commit - the L1 integrates.
Tooling authorization (operator, 2026-10-19): you may install or upgrade tools that help the task - read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record tool/version/channel/reason in your report). pacman guard (orchestrator ruling 2026-10-20, in force): all pacman transactions are PAUSED host-wide - install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R/downgrade.
Report: write your scoped findings to /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-65/w1/<SEAT>.md (the validator renders every `Report:` trailer relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin - write it at that absolute path)."""

RULES = """Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
"""

ROW_TOPICS = [
    ("S750", "Culin 1907 Games of the North American Indians - classification (chance/physical/skill) and ethnographic scope"),
    ("S751", "the Royal Game of Ur - race game, royal cemetery context, rules reconstruction"),
    ("S752", "senet - Egyptian funerary board game, tomb context, calibrated ritual interpretation"),
    ("S753", "the mancala family - Africa/Asia distribution, sowing gameplay, scholarship"),
    ("S754", "tug of war and team contests as intangible heritage (UNESCO multinational nomination)"),
    ("S755", "astragaloi/knucklebones - astragalus bones in Greek/Roman gaming, archaeology"),
    ("S756", "anthropology of sport - Blanchard-style scholarly survey of sport as cultural institution"),
    ("S757", "Huizinga Homo Ludens - play as constitutive of culture (magic circle)"),
    ("S758", "Caillois Man, Play and Games - paidia/ludus, the six categories (agon/alea/mimicry/ilinx)"),
    ("S759", "Sutton-Smith The Ambiguity of Play - play rhetorics, variability of play's meanings"),
    ("S760", "ancient Olympic Games - festival context, rules, amateurism calibration"),
    ("S761", "Mesoamerican ballgame - courts, equipment, political/ritual role (museum scholarship)"),
    ("S762", "rubber and the solid ball in Mesoamerican play - material evidence"),
    ("S763", "tafl/hnefatafl - Norse board game family, rules reconstruction from sources"),
    ("S764", "go/weiqi origins and early transmission - official or scholarly source"),
    ("S765", "chaturanga and Silk Road transmission of chess - scholarly source"),
    ("S766", "history of playing cards - museum collection scholarship"),
    ("S767", "archaeology of dice - oldest dice, knucklebone dice, gaming in early states"),
    ("S768", "teetotum/dreidel spinning-top gambling toys - scholarly source"),
    ("S769", "Opie Lore and Language of Schoolchildren - playground games, counting-out"),
    ("S770", "Alice Gomme Traditional Games - singing/ring games catalogue"),
    ("S771", "lacrosse and First Nations stick games - origin accounts, museum sources"),
    ("S772", "sumo as ritual sport - official or scholarly source on its ritual grammar"),
    ("S773", "patolli - Mesoamerican race/betting game, sources and calibration"),
    ("S774", "kubb, skittles/ninepins, northern-European throwing-target family - scholarly or official-rules source"),
    ("S775", "board games across the ancient world - survey (museum exhibition scholarship)"),
]

ROW_MODEL = """Per row write .ufo/waves/round-65/rows/<SEAT>/row-<SID>.txt with exactly these labelled lines:
ROW=| <SID> | <source name> - <live URL> ; web.archive.org/web/<14-digit ts>id_/<original URL> . | <kind> | <A or B only> | <scope <=60 chars> | "<anchor quote 8-25 body words>" | <teaches cell <=240 chars> | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/games-play-sport-contests.md |
BULLET=<one clause: 6-25 content words, >=3 in-order content words from the quote, no run >12 words copied from the quote, >=1 novel content word, NOT a near-copy of the teaches cell (round-64 bypass class: keep word-token coverage of the teaches cell <80% in-order)>
VERIFY=<live curl status + date; quote in body text Y/N; access limits>
CAPTURE=<wayback ts + original URL; original query-aware-normalizes equal to the live URL>
ACCESS=<redirects, rate limits, paywalls a re-opener needs>
Rejects go to rows/<SEAT>/rejects.txt as <URL> - <reason>; flip: <what would change it>. The live URL must be unique: grep it against corpus/SOURCES.md and all fragments. Sources: tier A/B only (peer-reviewed, official bodies, museum/university, scholarly books). Verify everything yourself with curl."""

items = []

def add(name, role, body, axes, solution):
    items.append({"name": name, "role": role, "axes": axes, "milestone": "r65-v2",
                  "prompt": RULES + body, "_solution": solution})

# ---------------- BUILD ----------------
add("ScoutGapGames", "scout",
"""Verify the claim-C gap at the base, then write .ufo/waves/round-65/rows/ScoutGapGames/gap.md with exact commands+outputs:
1) cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git ls-tree -r --name-only 17c32302c6845c8f164b985a8cb312d3181c8788 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'  (expect 0)
2) grep -riE 'mancala|knucklebone|astragal|tug.of.war|senet|hnefatafl|patolli' corpus/knowledge/ | head -5  (expect nothing owned)
3) sibling ownership: grep -rliE 'mancala|senet|hnefatafl|patolli' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5
End gap.md with a 5-line build order for the entry: register map; source-grounded bullets by class (board, ball, physical contest, children's play, gambling/betting, ritual sport); cross-cultural patterns; design protocol; calibration; one-way pointing to partial owners; lore handoff.""",
["coverage", "adjacency"], "three fixed census commands + plan"),

for idx in range(13):
    a, b = ROW_TOPICS[2 * idx], ROW_TOPICS[2 * idx + 1]
    seat = f"ScoutRow{idx + 1:02d}"
    add(seat, "scout",
f"""ROW-OPENING item (claim C): open exactly two rows, ids {a[0]} and {b[0]}.
{a[0]} topic: {a[1]}.
{b[0]} topic: {b[1]}.
{ROW_MODEL}
Also grep both live URLs against corpus/SOURCES.md and every fragment under .ufo/waves/round-65/rows/ for uniqueness, recording outputs in your report. Your bullets are drafts; the L1 re-verifies.""",
["coverage", "depth"], "two fixed row ids, tier A/B source choice by seat"),

add("ScribeEntryBody", "scribe",
"""Pre-read/design seat (claim C). Read reports/round-65/accept-c.py (legs FILE/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/LIVE), reports/round-65/claims.json claim C, the round-64 model entry corpus/knowledge/linguistics/language-socialization-and-acquisition.md and model fragment .ufo/waves/round-64/rows/ScribeRow718/row.txt. Write .ufo/waves/round-65/stage/entry-spec.md: the exact entry skeleton for games-play-sport-contests.md (<=16 H2, `- topic:` text, frontmatter modelled on the round-64 entry, one bullet slot per S750-S775 grouped by game class), the RESTATE rules bullets must satisfy (incl. the near-copy rule: token coverage of any teaches cell <80% in-order), and the corpus/README.md edit recipe (culture-material 31 -> 32, footer 238 -> 239, index row with the topic verbatim).""",
["coverage", "depth"], "skeleton from frozen counter + model"),

add("ScribeGateRecords", "scribe",
"""Gate/records skeleton (frontier). Read corpus/lessons/round-64.md `## Gate` as the model. Write .ufo/waves/round-65/stage/gate-spec.md: the `## Gate` block skeleton for corpus/lessons/round-65.md - one line per id S750-S775 with id | URL | access date 2026-10-24 | <=25-word located quote - plus a `## Mistakes` skeleton carrying one row for the R1 class (class receipt-attribution; evidence reports/round-64/telemetry/final-measures-ca.txt; captured-by none - the protocol lacked a tree-hash-of-inputs rule; fix: receipts pin measured revision + tree hash, QUALITY criterion 17).""",
["calibration"], "two skeleton blocks from model"),

add("ScribeReadme", "scribe",
"""README recipe (claim C). Read corpus/README.md and `git show 95c9194e -- corpus/README.md | head -80`. Write .ufo/waves/round-65/stage/readme-patch.md: exact edits for after the entry lands - culture-material 31 -> 32, footer 238 -> 239, the new index row (topic text depends on the landed `- topic:` line; mark the dependency), and a frontier bullet noting games moved frontier -> core.""",
["coverage"], "edit recipe from committed model"),

add("ScribeLessonR65", "scribe",
"""Lesson skeleton (frontier). Read corpus/lessons/round-64.md fully and corpus/lessons/README.md (revision + index requirements). Write .ufo/waves/round-65/stage/lesson-skeleton.md: corpus/lessons/round-65.md skeleton (header; `## Gate` placeholder for S750-S775; `## Mistakes` with R65-M1 placeholder), plus the lessons-README revision bump (report the exact current revision and the index-row edit needed).""",
["calibration"], "skeleton from committed model"),

add("ScribeEntryAssemble", "scribe",
"""ENTRY-ASSEMBLY (claim C). When >=20 of 26 fragments exist under .ufo/waves/round-65/rows/, assemble .ufo/waves/round-65/stage/entry-draft.md: frontmatter + `- topic:` modelled on corpus/knowledge/linguistics/language-socialization-and-acquisition.md; sections per .ufo/waves/round-65/stage/entry-spec.md (if absent, the round-64 shape); one bullet per landed row, using its fragment BULLET verbatim, grouped by game class; then ## cross-cultural patterns (from the bullets only), ## calibration, ## one-way pointing to partial owners, ## lore handoff (canon decisions belong to lore-shokunin - name the boundary). If <20 fragments exist, record the dependency and return with a partial assembly. Flag any bullet you estimate would trip RESTATE (token coverage of its teaches cell >=80%).""",
["coverage", "depth"], "assembly from landed fragments; dependency-recorded"),

add("ExecCounterReview", "executor",
"""Counter smoke (claim O, build). From /home/vgpnk/Projects/shokunin/kotodama-shokunin run: (1) python3 -B tools/check-row-fragments.py --selftest (expect PASS 10/10); (2) python3 -B reports/round-65/accept-c.py --root . 2>&1 | tail -15 (expect FAIL - red at base); (3) python3 -B reports/round-65/accept-o.py --root . --only FRAG (expect FRAG FAIL + SKIP lines + `ACCEPT-O-65: FAIL [filtered: ...]`). Write .ufo/waves/round-65/stage/counter-review.md listing every defect/crash/ambiguity in the three counters (path:line + minimal fix). Do NOT edit counters - the L1 owns them; your defects become reviewer attack items.""",
["operability"], "run three frozen counters; report defects"),

add("ExecSeparability", "executor",
"""Separability manifest. Read tools/check-claim-separability.py (source), reports/round-63/telemetry/rev-separability.txt (record-dependency precedent) and reports/round-65/claims.json separability block. Write .ufo/waves/round-65/stage/separability-manifest.json: the three units (C/O/Ca), each unit's lands and reads, expected record-dependency-only class. The L1 runs the tool on it after integration.""",
["calibration"], "manifest draft from tool + precedent"),

add("ExecRecordsFix", "executor",
"""R1-R7 fix drafts (claim Ca, build). Read corpus/lessons/round-64-verifier-spotcheck.md section 6 and every target file. Produce .ufo/waves/round-65/stage/records-fix/ with one file per fix + fixes.md index. Exact content:
- final-measures-ca.txt.replacement: receipt re-stamped - header names measured revision 8bab271c691c6b1006da95316a24ae1958ec01e2; a `tree:` line equal to `git rev-parse 8bab271c691c6b1006da95316a24ae1958ec01e2^{tree}`; a correction note; the complete original receipt bytes verbatim below `--- original receipt bytes ---` (reuse the original's own leg lines; invent nothing).
- revisions.txt.append: the `Correction (round 65, R2)` entry for reports/round-63/telemetry/revisions.txt (the `measured 8d2041fa` header clause for final-measures-c.txt is false; receipt added by 0c892ce; path absent at 8d2041fa).
- lesson-64.append: `Correction (round 65, R6)` status note for corpus/lessons/round-64.md after R64-M12 (S687 flip committed in 95c9194e; the pre-land snapshot sentence is corrected).
- lesson-final.patch: minimal fix of the false attribution sentence in .ufo/waves/round-64/w2/LessonFinal.md (~line 858: final-measures-ca.txt is re-stamped to 8bab271c in round 65, not measured at 95c9194e).
- verified-at.patch: corrected line 5 for corpus/knowledge/linguistics/language-socialization-and-acquisition.md (replace the stale skeleton wording with an honest line naming the round-64 blind-support verification).
- claims-json.patch: exact JSON addition for reports/round-64/claims.json - a statement_correction on claim O: honest "at least their pinned leg" wording, m1 extra EDGE_USERINFO+EDGE_HTTPS and m2 extra EDGE_MALTARG named, predicate byte-unchanged.
- control-o-binding.txt: short record naming control-o.txt as counter revision 3 (sha256 c27a9fef...) measured at b7d22703, not final rev5.
- log-score-entries.md: LOG.md + SCORECARD.md `Correction (round 65, R1)` and `Correction (round 65, R3)` entry texts (R3 names .ufo/waves/round-64/w1/ReviewerCa.md as the actual path; the filed report's w2/ citation is the erratum target).
Read everything; apply nothing. The L1 reviews and applies.""",
["calibration"], "seven fixed targets; exact bytes per target"),

add("ExecGateFill", "executor",
"""GATE-FILL (frontier, build). When fragments land, assemble .ufo/waves/round-65/stage/lesson-gate.md: `## Gate` rows for corpus/lessons/round-65.md - per landed id S750-S775: id | URL | access date 2026-10-24 | quote <=25 words byte-equal to the fragment's quote. Run python3 -B tools/check-gate-quotes.py on your draft (check --help for a draft path) and fix every finding. If fragments are absent, record the dependency and return.""",
["calibration"], "gate table from landed fragments; dependency-recorded"),

add("ConnectorSiblings", "connector",
"""SIBLING-OVERLAP. Run: grep -rliE 'mancala|senet|astragal|tug.of.war|hnefatafl|patolli|kubb' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin /home/vgpnk/Projects/shokunin/kotoba-shokunin 2>/dev/null; and grep -rliE 'check-row-fragments|reopen-row' /home/vgpnk/Projects/shokunin/*/tools 2>/dev/null | grep -v kotodama. Write .ufo/waves/round-65/w1/ConnectorSiblings.md: who owns what (nearest prior art chousa-shokunin/tools/quote-reopen.py - confirm), whether any sibling owns a games register entry (adjacency: report, do not absorb), and the one-way handoff boundary for the entry's lore-facing section.""",
["adjacency"], "fixed grep set"),

add("SentinelScope", "sentinel",
"""SCOPE GUARD (build side). From /home/vgpnk/Projects/shokunin/kotodama-shokunin verify: git -C /home/vgpnk/Projects/shokunin status --porcelain | head -20 (seat notes misrooted at fleet root? name any, touch nothing); round-65 writes only under reports/round-65/, .ufo/waves/round-65/, claims' land paths; tools/reopen-row.py unchanged (`git diff 17c32302c6845c8f164b985a8cb312d3181c8788 -- tools/reopen-row.py | wc -l` expect 0); registry rows 675 (expect unchanged until integration). Write .ufo/waves/round-65/w1/SentinelScope.md with evidence and any violation.""",
["operability", "calibration"], "fixed guard checks"),

add("ScoutBlindBase", "scout",
"""LOCATOR RECON. From /home/vgpnk/Projects/shokunin/kotodama-shokunin run: python3 -B reports/round-61/reopen-quote.py --row S718; --row S729 (expect LOCATED within ~60s each; note rate limits); --row S744 (rejected row - expect NOT-LOCATED or an error line, no traceback). Write .ufo/waves/round-65/w1/ScoutBlindBase.md: outputs + whether LIVE's 3x20s retry budget is adequate for these hosts.""",
["operability"], "three fixed locator runs"),

add("ScoutFragRunner", "scout",
"""FRAGMENT SCAN. When row fragments exist under .ufo/waves/round-65/rows/, run python3 -B tools/check-row-fragments.py and record full output. If absent, record the dependency and return. Per finding: trace to the fragment line and propose the minimal correction (do not edit fragments - row scouts own them). Write .ufo/waves/round-65/w1/ScoutFragRunner.md with scan output and dispositions.""",
["operability", "coverage"], "scan over landed fragments; dependency-recorded"),

add("SimplifierCounters", "simplifier",
"""SIMPLEST-BYPASS pass 1. Read reports/round-65/accept-c.py (RESTATE near-copy), accept-o.py (FULL/MUTEX/FRAG) and tools/check-row-fragments.py. Per rule: the cheapest fixture that beats it as written. Covers: near-copy with per-word synonym substitution; a receipt printed from a filtered run; a mutant whose extra legs the table pins wrongly; an empty rows dir passing FRAG vacuously. Write .ufo/waves/round-65/w1/SimplifierCounters.md - per rule: bypass candidate + killed Y/N + why. No counter edits.""",
["operability", "depth"], "four fixed rules under bypass"),

# ---------------- ATTACK ----------------
add("RevCounterC", "reviewer",
"""ATTACK reports/round-65/accept-c.py. (1) Craft the minimal bullet equal to its teaches cell plus ONE trailing novel word: show (worksheet math, no live runs) whether the 0.8 in-order token-coverage rule fails it, incl. plural variants (games vs game). (2) Two rows whose URLs differ only in query must fail ROWS norm-dup. (3) An 8-word bullet, 3 in-order quote words, teaches coverage 0.79 must PASS (no false positive). Give exact crafted strings + expected leg verdicts in .ufo/waves/round-65/w1/RevCounterC.md.""",
["depth", "operability"], "three crafted fixtures against fixed rules"),

add("RevCounterO", "reviewer",
"""ATTACK reports/round-65/accept-o.py FULL/MUTEX (grep -n 'FULL\\|MUTEX' reports/round-65/accept-o.py). (1) Can ACCEPT-O-65: PASS ever print from a --only run without the filtered marker? Trace the suffix logic. (2) MUTEX's SWEEP_EXPECT pins m1/m2 extras - if tool behavior drifted, which leg fails first; is that honest? (3) FULL counts pass lines == len(run_legs_all) - could any leg print two PASS lines? Check each leg prints exactly one. Verdicts (broken/holds+why) in .ufo/waves/round-65/w1/RevCounterO.md.""",
["operability"], "three trace attacks"),

add("RevCounterCa", "reviewer",
"""ATTACK reports/round-65/accept-ca.py keying (round-64 HIGH-1/HIGH-2 class). Per leg R1..R7, CRITERION, QUOTES: state the exact bytes it keys on and how a global-token-only patch (names 8bab271c everywhere but never re-stamps the receipt) fails. Craft two such patches on paper; show which legs kill them. .ufo/waves/round-65/w1/RevCounterCa.md.""",
["calibration"], "two crafted patches against nine keyed legs"),

add("RevClaimC", "reviewer",
"""ATTACK claim C's before-state. Independently re-derive the gap: git ls-tree -r --name-only 17c32302c6845c8f164b985a8cb312d3181c8788 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'; plus a word-bounded topic-owner grep separating filename owners from incidental mentions (round-64 closure method). Try to name a partial owner the 0-owners claim would miss (a do-nothing control on the before-value). Counts in .ufo/waves/round-65/w1/RevClaimC.md.""",
["coverage", "calibration"], "independent census re-derivation"),

add("RevClaimO", "reviewer",
"""ATTACK claim O statement-vs-predicate (frozen-predicate rule). Read reports/round-65/claims.json claim O word by word against the counters. Which statement clauses have NO leg (review_only honesty)? Is 'the unchanged tools/reopen-row.py passes every round-62/63/64 leg' verified by a leg? Is the MUTEX 'disclosed expectation' the same object in statement, counter, future receipt? Any statement/predicate divergence is a blocker. .ufo/waves/round-65/w1/RevClaimO.md.""",
["operability", "calibration"], "statement-vs-counter audit"),

add("RevClaimCa", "reviewer",
"""ATTACK claim Ca's seven dispositions. Per R1-R7: read the spotcheck demand (corpus/lessons/round-64-verifier-spotcheck.md section 6), the ExecRecordsFix draft (.ufo/waves/round-65/stage/records-fix/; if absent record the dependency), and the accept-ca leg. Is any disposition satisfiable by token presence without substance (HIGH-1 class)? Verify yourself: git rev-parse 8bab271c691c6b1006da95316a24ae1958ec01e2^{tree} - record the value. Per-defect verdicts in .ufo/waves/round-65/w1/RevClaimCa.md.""",
["calibration"], "seven dispositions under token-presence attack"),

add("RevEntryDraft", "reviewer",
"""ATTACK the model. Read corpus/knowledge/linguistics/language-socialization-and-acquisition.md, .ufo/waves/round-64/rows/ScribeRow718/row.txt and the defect classes the round-64 falsify wave repaired (corpus/lessons/round-64.md R64-M1..M19). Turn each into a pre-integration check with a grep/curl command. .ufo/waves/round-65/w1/RevEntryDraft.md - the checklist.""",
["coverage", "depth"], "checklist from 19 committed mistakes"),

add("RevReceipts", "reviewer",
"""ATTACK the R1 receipt class. Read reports/round-64/telemetry/final-measures-ca.txt, the H1 analysis (spotcheck section 2 claim Ca), final-measures-c.txt, final-measures-o.txt. Per receipt: does the file alone let a reader re-derive the measured tree? Craft what a correct re-stamped ca receipt must contain; then attack the ExecRecordsFix draft (.ufo/waves/round-65/stage/records-fix/final-measures-ca.txt.replacement; if absent record the dependency). .ufo/waves/round-65/w1/RevReceipts.md.""",
["calibration", "operability"], "three receipts under re-derivation attack"),

add("RevSeparability", "reviewer",
"""ATTACK separability design. Read reports/round-65/claims.json separability block and tools/check-claim-separability.py. Design the post-integration re-run (record-dependency class allowed per reports/round-63/telemetry/rev-separability.txt). Does accept-c.py read any accept-o/accept-ca land? Does accept-o.py read the games entry or registry? Does accept-ca.py read the fragment tool? Expected 0-finding manifest + any real dependency found by reading the counters. .ufo/waves/round-65/w1/RevSeparability.md.""",
["calibration"], "three counters under read-set audit"),

add("RevShonenReport", "reviewer",
"""REPORT readiness. Read SHONEN.md (4 boxes) and /home/vgpnk/Projects/shokunin/.ufo/reports/round-64/kotodama.md (fleet repo, read-only) as the model. List the round-65 report's required sections and pre-compute the SHONEN lines that change (registry rows, capability additions). .ufo/waves/round-65/w1/RevShonenReport.md - section-by-section readiness list.""",
["calibration"], "fixed report contract audit"),

add("RevLessonFinal", "reviewer",
"""ATTACK the lesson before it exists. Read corpus/lessons/round-64.md and tools/check-gate-quotes.py --help. The accept-ca QUOTES leg requires 0 findings on corpus/lessons/round-65.md: enumerate every Gate-row shape that trips the checker (doubled locator, truncated grounds vs registry teaches cell, hidden quotes, html entities - the round-55/56 classes), one example row per shape, so the scribes avoid them. .ufo/waves/round-65/w1/RevLessonFinal.md.""",
["calibration", "depth"], "four committed failure shapes"),

add("RevRegistryFinal", "reviewer",
"""ATTACK the registry integration. Read reports/round-65/accept-c.py ROWS/APPEND/LINK and corpus/SOURCES.md base state (675 rows). Enumerate integration errors that pass a leg but corrupt the registry: appended row duplicating a base id with one cell changed (APPEND keys whole lines - does it catch a base teaches cell edited?); appended row reusing a base URL under a new id (LINK checks only new rows - verify); new row whose capture normalizes equal but points at a different page. Caught Y/N + proof grep per case. .ufo/waves/round-65/w1/RevRegistryFinal.md.""",
["coverage", "calibration"], "three integration errors under leg audit"),

add("RevLiveSubset", "reviewer",
"""ATTACK the LIVE leg. Read reports/round-65/accept-c.py LIVE + reports/round-61/reopen-quote.py. (1) Can a row carry a caption-only quote and still LOCATE (CAPTION_ONLY class - does the pinned locator separate it)? (2) The subset is every-5th of 26 (6 ids) - show the pattern; would one host serving 3 of 6 escape? Recommend (do not apply) whether the subset rule stays frozen. (3) The locator pin resolves from BASE at runtime - trace what happens if reports/round-61/reopen-quote.py is edited mid-round. .ufo/waves/round-65/w1/RevLiveSubset.md.""",
["operability", "coverage"], "three attacks on one leg"),

add("RevCounterCaKeying", "reviewer",
"""ATTACK accept-ca.py R1 keying depth. (1) A receipt whose preserved-original block is truncated to just the old measured-revision line - the leg does NOT diff originals against git history: hole or fine? (2) tree line of 8bab271c but a different marker text. (3) marker present but the old line above it instead of below. Verdict per attack in .ufo/waves/round-65/w1/RevCounterCaKeying.md.""",
["calibration"], "three crafted receipt mutations"),

add("MutCounterC", "mutation-tester",
"""MUTATE reports/round-65/accept-c.py: 6 byte-mutants in copies under .ufo/waves/round-65/stage/mut-c/ (never the committed file): coverage 0.8 -> 0.99; near-copy rule deleted; norm_url compares query; ONEID drops citation_exact; APPEND count 26 -> 25; LIVE subset cut to 3 ids. Per mutant: the land state that makes it print PASS where the original prints FAIL (kill description); does the frozen dry-run + a landed tree kill it? Mutant table in .ufo/waves/round-65/w1/MutCounterC.md. No live re-opens; reason or run against red dry-run inputs.""",
["operability"], "six named mutants"),

add("MutCounterO", "mutation-tester",
"""MUTATE the FULL/MUTEX/FRAG additions in reports/round-65/accept-o.py: copies under .ufo/waves/round-65/stage/mut-o/: FULL's --only list gains FRAG (trace self-inclusion); suffix marker removed; MUTEX SWEEP_EXPECT m1 extras emptied; FRAG selftest requirement dropped; scan check weakened to 'finding'. Per mutant: killed-by-what. Table in .ufo/waves/round-65/w1/MutCounterO.md.""",
["operability"], "five named mutants"),

add("MutCounterCa", "mutation-tester",
"""MUTATE reports/round-65/accept-ca.py: copies under .ufo/waves/round-65/stage/mut-ca/: R1 tree regex loosened to any hex; R2 append-only check dropped; R7 regex matches 'skeleton' anywhere in the file instead of the verified-at line; QUOTES pointed at a different lesson; CRITERION checks only that '17.' exists. Per mutant: false green admitted + which committed receipt kills it. Table in .ufo/waves/round-65/w1/MutCounterCa.md.""",
["calibration"], "five named mutants"),

add("MutEntryClass", "mutation-tester",
"""ENUMERATE entry/registry mutants (claim C lands): drop one bullet (ONEID); duplicate one S-id (ONEID); swap two bullets' ids (RESTATE in_order); append a 27th row (APPEND); flip one tier to C (ROWS); drop one row's capture (ROWS); edit one base row (APPEND); put a live URL inside the entry text (LINK). Per mutant: failing leg + the pre-integration grep. Table in .ufo/waves/round-65/w1/MutEntryClass.md.""",
["coverage", "operability"], "eight enumerated mutants"),

add("MutRecords", "mutation-tester",
"""MUTATE the R1-R7 fixes. Per fix the ExecRecordsFix seat drafts (read .ufo/waves/round-65/stage/records-fix/ when present; else enumerate from the spotcheck): the mutation that looks done but is wrong - R1 tree line of the wrong commit; R2 rewriting the false clause in place instead of appending; R4 also editing the frozen predicate sentence; R6 correction in the wrong lesson; R7 claiming verification that never happened. Per mutant: which accept-ca leg kills it? Table in .ufo/waves/round-65/w1/MutRecords.md.""",
["calibration"], "six crafted wrong-fixes"),

add("MutReceipts", "mutation-tester",
"""ENUMERATE receipt mutants (attack). The round's receipts will be reports/round-65/telemetry/final-measures-{c,o,ca}.txt. Which would fake a verdict: wrong counter sha256; stale sha of an earlier counter revision; measured revision naming the declaration commit instead of the lands; missing tree line (R1 class - the QUALITY criterion 17 the Ca claim lands). Per mutant: killing leg/closure check; does any survive? Table in .ufo/waves/round-65/w1/MutReceipts.md.""",
["calibration"], "four receipt mutants"),

add("SimplifierBypass", "simplifier",
"""SIMPLEST-BYPASS pass 2 (attack, after SimplifierCounters). Independently find the cheapest input beating each rule as written: RESTATE-nearcopy (synonym substitution every 4th word - coverage drops; does in_order vs quote still pass, and is that honest or a cheat?); FULL (can its subprocess be tricked by a stubbed self-copy on PATH?); MUTEX (a mutant outside the ten pinned - e.g. an eleventh behavior class - what pins it?); FRAG (empty/missing rows dir - does the leg require 26 files present? read it). Where a bypass holds, say so plainly (blocker). .ufo/waves/round-65/w1/SimplifierBypass.md.""",
["operability", "depth"], "four fixed rules under cheapest-bypass"),

add("RevengerRouted", "revenger",
"""ROUTED-INTENT (claim Ca). From corpus/lessons/round-64-verifier-spotcheck.md section 6 alone, quote the operative sentence per defect R1-R7, then compare against the ExecRecordsFix draft (.ufo/waves/round-65/stage/records-fix/; if absent record the dependency). Per defect: satisfies / over-reaches (edits filed bytes that must stay append-only) / misses. One verdict per defect with path:line evidence in .ufo/waves/round-65/w1/RevengerRouted.md.""",
["calibration"], "seven defects re-derived"),

add("RevengerR2R3", "revenger",
"""OVER-CORRECTION attack on R2/R3. Read the spotcheck R2/R3, the targets (reports/round-63/telemetry/revisions.txt; /home/vgpnk/Projects/shokunin/.ufo/reports/round-64/kotodama.md read-only; SCORECARD.md round-64 rows) and the ExecRecordsFix draft (if absent record the dependency). Does the revisions.txt correction preserve original lines byte-identically and append below? Is the R3 route (erratum in the round-65 report + lane records; filed report untouched) consistent with append-only convention and the write scope (.ufo/reports/round-64 outside this round's scope)? Verdicts in .ufo/waves/round-65/w1/RevengerR2R3.md.""",
["calibration", "adjacency"], "two corrections under over-correction attack"),

add("ScoutReopenA", "scout",
"""BLIND RE-OPEN attack (claim C): rows S750-S757. When fragments land under .ufo/waves/round-65/rows/, re-open each live URL yourself with curl: HTTP status; quote located in body text (not caption/nav); 8-25 words; capture exists with matching original path. For absent fragments record the dependency (id, expected path) and return - do not wait. Verdict per row: LOCATED / NOT-LOCATED:<reason> with curl evidence. .ufo/waves/round-65/w1/ScoutReopenA.md feeds the blind-support ring.""",
["coverage", "freshness"], "eight fixed ids under blind re-open"),

add("ScoutReopenB", "scout",
"""BLIND RE-OPEN attack (claim C): rows S758-S765. Same contract as ScoutReopenA: independent curl re-open per landed fragment; record dependencies for absent ones; per-row LOCATED / NOT-LOCATED:<reason> with evidence. .ufo/waves/round-65/w1/ScoutReopenB.md.""",
["coverage", "freshness"], "eight fixed ids under blind re-open"),

add("ScoutReopenC", "scout",
"""BLIND RE-OPEN attack (claim C): rows S766-S775. Same contract as ScoutReopenA plus one tier-honesty check per row: is the tier (A/B) defensible for the source's scope? Flag tier inflation (the round-64 S721/S726/S737 class). .ufo/waves/round-65/w1/ScoutReopenC.md.""",
["coverage", "freshness"], "ten fixed ids under blind re-open + tier audit"),

add("CriticPreC", "critic",
"""PRE-DATA CRITIC (claim C). Read reports/round-65/claims.json claim C + reports/round-65/accept-c.py. (1) Do-nothing control: could a sourceless stub entry + 26 self-invented rows pass? Walk each leg: which fail, which survive. (2) Universal-clause audit: any 'all/complete/every' no counter enumerates? (3) Sizing: is 26 rows reachable by 13 scouts x 2? (4) LIVE subset: is the frozen-subset choice attackable (all 6 on one host)? Per-leg control analysis in .ufo/waves/round-65/w1/CriticPreC.md; a wrong leg is a blocker - name it loudly.""",
["coverage", "calibration"], "one frozen claim, four attack angles"),

add("CriticPreO", "critic",
"""PRE-DATA CRITIC (claim O). Read claims.json claim O, the three counters, reports/round-65/telemetry/controls-c.txt + dry-run-*.txt. (1) Could a do-nothing control (round-64 counter forms) meet the new predicate? (2) Is MUTEX's disclosed table falsifiable pre-data or only descriptive? (3) Does FULL's self-subprocess close the filtered-green residual or re-present it? (4) Does the predicate sentence name the same object in claims.json and the counters? .ufo/waves/round-65/w1/CriticPreO.md; blockers named loudly.""",
["operability", "calibration"], "one frozen claim, four attack angles"),

add("CriticControlC", "critic",
"""DO-NOTHING CONTROL (claim C). Cheapest control skipping the work: a sourceless stub entry (26 bullets, no rows) + 26 registry rows with invented teaches cells and captures that do NOT normalize-match their live URLs. Walk accept-c.py leg by leg: which fail, and does ANY leg pass that should not? Leg-by-leg table in .ufo/waves/round-65/w1/CriticControlC.md. Paper/scratch under .ufo/waves/round-65/stage/control-c/ only.""",
["coverage", "calibration"], "one crafted stub under ten legs"),

add("CriticControlO", "critic",
"""DO-NOTHING CONTROL (claim O). The control is the round-64 counter forms (git show 6f3e0b2:reports/round-64/accept-o.py). Show: (1) the round-64 accept-o presented a partial green as a receipt (cite .ufo/waves/round-64/w2/OReceiptFresh.md per LOG routing); (2) the round-64 accept-c RESTATE let the trailing-word near-copy pass (cite reports/round-65/telemetry/controls-c.txt control 1); (3) map each residual -> the round-65 leg that kills it -> why the old form met the residual. Mapping table in .ufo/waves/round-65/w1/CriticControlO.md.""",
["operability"], "fixed round-64 forms under three residuals"),

add("CriticControlCa", "critic",
"""DO-NOTHING CONTROL (claim Ca). Before-state: R1-R7 unresolved at base (python3 -B reports/round-65/accept-ca.py --root . - expect all FAIL, cf dry-run-ca.txt; re-run, confirm byte-similar). Then the cheapest fake fix: a records file adding 'Correction (round 65, R1)' + '8bab271c' globally without re-stamping the receipt. Walk the nine legs: which kill the fake? Leg table in .ufo/waves/round-65/w1/CriticControlCa.md.""",
["calibration"], "one fake-fix under nine legs"),

add("CriticClaimsWording", "critic",
"""WORDING audit (R4 class). Read reports/round-65/claims.json. Per claim: does the statement's after-state describe one concrete re-derivable value? Universal clauses no counter enumerates? Numbers unverifiable from committed bytes? Compare the round-64 failure replaced here ('each fail exactly their pinned leg' vs exactness-sweep-o.txt). Per-sentence verdicts + statement-fix proposals in .ufo/waves/round-65/w1/CriticClaimsWording.md (predicates are frozen; statement fixes ride the records).""",
["calibration"], "three statements under sentence audit"),

add("CriticNoHarm", "critic",
"""NO-AXIS-HARM census. From /home/vgpnk/Projects/shokunin/kotodama-shokunin: git diff 17c32302c6845c8f164b985a8cb312d3181c8788 -- reports/round-64/ corpus/lessons/round-64.md .ufo/waves/round-64/ | head (expect empty); tools/reopen-row.py unchanged; python3 -B reports/round-28/readme/sweep.py; echo exit=$? (expect 0). Enumerate the integration no-touch list (filed rounds 49-64 lessons, corpus/lessons/round-64-verifier-spotcheck.md, MANIFEST, fleet templates/scripts). Evidence + list in .ufo/waves/round-65/w1/CriticNoHarm.md.""",
["calibration", "freshness"], "fixed byte-preservation census"),

add("CriticSizing", "critic",
"""SIZING audit (claim-sizing class). Per the fleet rules: after-state one concrete value re-derivable with one command over committed bytes; a do-nothing control must not reach it; one frozen predicate sentence. Audit C/O/Ca: exact counter sentence, kill rule, do-nothing control per claim. Any claim a do-nothing control CAN reach is a blocker (counter or target wrong before data). Verdicts in .ufo/waves/round-65/w1/CriticSizing.md.""",
["calibration"], "three claims under sizing rules"),

add("CriticWaveShape", "critic",
"""WAVE-SHAPE audit. Read .ufo/waves/round-65/spec-v2.json + taskcall-v2.json: seat count and role mix vs the shape (one v2 wave, exactly 64 seats, >=25% attack roles - reviewer+critic+mutation-tester); every claim has attack seats per leg family; every build seat names an output path; the two wave-rule lines verbatim in every item prompt; every dependency-prone seat records-absent clause. Violations in .ufo/waves/round-65/w1/CriticWaveShape.md.""",
["calibration"], "one spec under shape audit"),

add("SentinelFinal", "sentinel",
"""FINAL SCOPE GUARD. From /home/vgpnk/Projects/shokunin/kotodama-shokunin: (1) every seat report under .ufo/waves/round-65/w1/ exists and names its target (list missing); (2) git status --porcelain shows only expected round-65 paths; stray fleet-root files: git -C /home/vgpnk/Projects/shokunin status --porcelain | grep -v '.ufo/state\|watchdog\|SCORECARD\|AGENTS\|mcp.json' | head; (3) tools/reopen-row.py + filed rounds byte-equal to base; (4) seat count 64 vs reports on disk. Evidence table + blockers in .ufo/waves/round-65/w1/SentinelFinal.md.""",
["operability", "calibration"], "four fixed end-wave guards"),

spec = {
    "wave": "kotodama-r65-v2",
    "milestone": "Round 65 single v2 wave (build+attack, 64 seats)",
    "reportDir": ".ufo/waves/round-65/w1",
    "axes": ["coverage", "operability", "calibration", "depth", "freshness", "adjacency"],
    "context": CONTEXT,
    "items": [{k: v for k, v in it.items() if k != "_solution"} for it in items],
}
out = f"{LANE}/.ufo/waves/round-65/spec-v2.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(spec, fh, indent=1, ensure_ascii=False)
json.dump({it["name"]: it["_solution"] for it in items},
          open(f"{LANE}/.ufo/waves/round-65/solutions.json", "w"), indent=0)
roles = {}
for it in items:
    roles[it["role"]] = roles.get(it["role"], 0) + 1
attack = sum(roles.get(r, 0) for r in ("reviewer", "critic", "mutation-tester"))
print("seats:", len(items), "roles:", roles, "attack:", attack)
