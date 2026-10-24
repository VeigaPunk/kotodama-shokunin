#!/usr/bin/env python3
"""Generate the round-67 single v2 wave spec (64 seats, >=25% attack roles)."""
import json

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "ad5b52b0ab5691358cd38718ab75649dc9916f9a"

CONTEXT = """# Goal
Kotodama round 67 (hyaku run 5, 2026-10-24): ONE v2 wave of 64 seats, build+attack together. Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (jj-colocated; base revision ad5b52b0ab5691358cd38718ab75649dc9916f9a). All lane-relative paths below resolve under that repo. Three claims with frozen predicates (reports/round-67/claims.json, written pre-wave):
- C (coverage, sourced): new entry corpus/knowledge/culture-material/medicine-healing-codes.md + exactly 24 mined registry rows S805-S828 (tier A/B, opened 2026-10-24, used-by the entry, cited exactly once each). Predicate: ACCEPT-C-67: every leg of reports/round-67/accept-c.py prints PASS.
- O (operability, capability acquisition): tools/check-receipt-seq.py lands — receipt header equality (stamped/evaluated/measured + tree + counter sha), committed-bytes --lands mode, post-records --topo carrier-parentage, 14/14 selftest. Predicate: ACCEPT-O-67: every leg of reports/round-67/accept-o.py prints PASS.
- Ca (calibration, records): the round-66 closure's routed defects R66-D1..D5 dispositioned (committed wave-evidence manifest; registry placement E12/E11 repaired; LOG/SCORECARD round-66 entries restored; S801-S804 + >=2 new first-class rejected rows; the --lands/stamped/evaluated receipt protocol across all three counters). Predicate: ACCEPT-CA-67: every leg of reports/round-67/accept-ca.py prints PASS.
RECEIPT DISCIPLINE (the r66 fix this round proves): every r67 counter takes a REQUIRED --lands <40hex>; the receipt records stamped + evaluated + measured revisions + tree + counter sha256; STAMP fails unless evaluated == stamped. Counters run inside a materialized clone at the lands commit, never a moved worktree. Carrier-parentage is post-records evidence only.
Frozen counters, claims.json, base dry-run receipts (reports/round-67/telemetry/dry-run-*.txt) and pre-data controls (controls-*.txt) are on disk at the lane tip - read them before attacking. Build seats: your output is a draft under .ufo/waves/round-67/ - the L1 reviews, integrates and is the only committer. Attack seats: try to break the frozen instruments and drafts - shortcut classes, bypasses, stale receipts, false stamps, moved-worktree PASS claims, duplicates, tier inflation, fabricated anchors; name what you attack.

# Rules (bind every seat)
Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
Leaf member - no subagent dispatch, no swarm of your own. Absolute paths for writes, under /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/ only, at the exact paths your item names. Never mutate the fleet repo, sibling lanes, lane jj state or the lane Git index; never run git/jj writes; read-only git is fine; do not commit - the L1 integrates.
Tooling authorization (operator, 2026-10-19): you may install or upgrade tools that help the task - read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record tool/version/channel/reason in your report). pacman guard (orchestrator ruling 2026-10-20, in force): all pacman transactions are PAUSED host-wide - install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R/downgrade.
Report: write your scoped findings to /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/w1/<SEAT>.md (the validator renders every `Report:` trailer relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin - write it at that absolute path)."""

RULES = """Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
"""

ENTRY = "corpus/knowledge/culture-material/medicine-healing-codes.md"

ROW_TOPICS = [
    ("S805", "Hippocratic corpus and the humoral canon — Perseus/Tufts, Loeb mirror, or scholarly host on On the Nature of Man / humors"),
    ("S806", "Ayurveda and the Charaka Samhita — academic source on doshas and early Indian medical theory"),
    ("S807", "Traditional Chinese medicine foundations — Huangdi Neijing, qi, meridians; scholarly or museum source"),
    ("S808", "Islamic Golden Age medicine — Ibn Sina's Canon of Medicine; Wellcome, Britannica-tier or scholarly source"),
    ("S809", "Medieval European monastic infirmaries and herbals — museum or scholarly source"),
    ("S810", "Roman military medicine and the valetudinarium — archaeological or museum source"),
    ("S811", "Egyptian medical papyri (Ebers/Edwin Smith) — museum or scholarly source"),
    ("S812", "Galen and the Alexandrian/Roman medical system — scholarly or encyclopedia source"),
    ("S813", "Plague doctors and public-health costume — museum source on the beaked costume and its prophylaxis logic"),
    ("S814", "Paracelsus and chemical medicine — scholarly or museum source on iatrochemistry"),
    ("S815", "Aztec/Mesoamerican herbal medicine — museum or scholarly source (Badianus manuscript or curanderismo)"),
    ("S816", "Tibetan medicine and the Four Tantras (Gyushi) — scholarly or museum source"),
    ("S817", "Indigenous healing and the medicine lodge / sweat-lodge therapy — museum or scholarly source"),
    ("S818", "The medieval European apothecary and guild regulation — museum or scholarly source"),
    ("S819", "Vesalius's Fabrica and the anatomical revolution — scholarly or museum source"),
    ("S820", "Plague hospitals and lazarettos/quarantine — scholarly or museum source (Venice lazaretto)"),
    ("S821", "Kampo and Japanese traditional medicine — scholarly or institutional source"),
    ("S822", "The medieval Islamic hospital (bimaristan) — scholarly or museum source"),
    ("S823", "Medieval European surgical guilds and barber-surgeons — museum or scholarly source"),
    ("S824", "African healing systems and the sangoma/nganga — scholarly or museum source"),
    ("S825", "Greek healing sanctuaries (asklepieia) and incubation — museum or scholarly source"),
    ("S826", "Japanese moxibustion and acupuncture transmission — museum or scholarly source"),
    ("S827", "The medieval plague treatises / consilia — scholarly source on medical advice literature"),
    ("S828", "Medical amulets, charms and the materia of protection — museum collection or scholarly source"),
]

ROW_MODEL = """Per row write .ufo/waves/round-67/rows/<SEAT>/row-<SID>.txt with exactly these labelled lines:
ROW=| <SID> | <source name> - <live URL> ; https://web.archive.org/web/<14-digit ts>id_/<original URL> . | <kind> | <A or B only> | <scope <=60 chars> | "<anchor quote 8-25 body words>" | <teaches cell <=240 chars> | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/medicine-healing-codes.md |
BULLET=<one clause: 6-25 content words, >=3 in-order content words from the quote, no run >12 words copied from the quote, >=1 novel content word, NOT a near-copy of the teaches cell (word-token coverage <80% in-order)>
VERIFY=<live curl status + date; quote in body text Y/N; access limits>
CAPTURE=<wayback ts + original URL; original query-aware-normalizes equal to the live URL>
ACCESS=<redirects, rate limits, paywalls a re-opener needs>
Rejects go to rows/<SEAT>/rejects.txt as <URL> - <reason>; flip: <what would change it>. The live URL must be unique: grep it against corpus/SOURCES.md and all fragments. Sources: tier A/B only (peer-reviewed, official bodies, museum/university, scholarly books). Verify everything yourself with curl."""


def seat(name, role, prompt, axes):
    return {"name": name, "role": role, "axes": axes, "milestone": "r67-v2",
            "prompt": RULES + prompt}


items = []

# ---- build: gap + rows ----
items.append(seat("ScoutGapMed", "scout",
    "Verify the claim-C gap at the base, then write .ufo/waves/round-67/rows/ScoutGapMed/gap.md with exact commands+outputs:\n"
    "1) cd " + LANE + " && git ls-tree -r --name-only " + BASE + " -- corpus/knowledge | grep -ciE '(^|[^a-z])(medicin|healing|physician|remedy|remedie|surgery|surgical|apothec|hospital|leech|physick|doctor|shaman|curander|herbal)([^a-z]|$)'  (expect 0)\n"
    "2) grep -rniE '^-?\\s*topic\\s*:.*(medicin|healing|physician|remedy|surgery|apothec|hospital|shaman|curander|herbal|disease|plague)' corpus/knowledge/  (list every topic-line owner; expect only partial-scope mentions — bathing, scent prophylaxis, myth-symbol purity)\n"
    "3) sibling ownership: grep -rliE 'medicin|healing|physician' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5\n"
    "End gap.md with a 5-line build order for the entry: register map; source-grounded bullets by class (medical systems/theories, institutions, practitioners/guilds, prophylaxis costume+amulets, materia medica); cross-cultural patterns; design protocol; calibration; one-way pointing to partial owners; lore handoff.",
    ["coverage", "adjacency"]))

for i in range(0, len(ROW_TOPICS), 2):
    pair = ROW_TOPICS[i:i + 2]
    seat_name = "ScoutRow%02d" % (i // 2 + 1)
    ids = ", ".join(s for s, _ in pair)
    topics = " AND ".join(t for _, t in pair)
    task = ("ROW-OPENING item (claim C): open exactly two registry rows, " + ids
            + ", for the medicine/healing register. Topics: " + topics + ".\n\n"
            + ROW_MODEL)
    items.append(seat(seat_name, "scout", task, ["coverage"]))

items.append(seat("ScoutReject1", "scout",
    "REJECT-CANDIDATE item (claim C gate): find two candidate medicine/healing sources that a gate SHOULD reject and produce first-class rejected registry rows for them (round-66 routed defect R66-D5: rejections must be rows, not fragments). Write .ufo/waves/round-67/rows/ScoutReject1/row-S829.txt and row-S830.txt (temporary ids S829/S830) in the same ROW= shape but with status cell 'rejected', teaches cell 'REJECTED: <reason>; flip: <what would change the verdict>' (<=240 chars), opened 2026-10-24, used-by '—'. Candidate reject classes: a paywalled/JS-walled source a plain curl cannot open; a source whose only quotable text is a caption/alt-text; a duplicate of an existing row's live URL; a scope that belongs to a sibling lane (lore canon, chousa method). Record full VERIFY/CAPTURE/ACCESS evidence so the rejection is checkable. Also write rows/ScoutReject1/rejects.txt listing surveyed-but-not-rowed candidates.",
    ["coverage", "calibration"]))

items.append(seat("ScoutReject2", "scout",
    "Same contract as ScoutReject1 but disjoint candidates — write rows/ScoutReject2/row-S831.txt and row-S832.txt (temporary ids S831/S832), status 'rejected', 'REJECTED: <reason>; flip: ...' teaches, used-by '—'. Prefer different reject classes than ScoutReject1 targets (e.g. metadata-only landing page vs the quoted PDF; bot-challenge; community/tier-C material that cannot support an admitted entry). Full VERIFY/CAPTURE/ACCESS evidence required.",
    ["coverage", "calibration"]))

# ---- build: drafting ----
items.append(seat("ScribeEntrySpec", "scribe",
    "Draft the claim-C entry design at .ufo/waves/round-67/stage/entry-spec.md (not the entry itself): section plan for corpus/knowledge/culture-material/medicine-healing-codes.md following the lane's entry conventions (read corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md and headgear-head-covering-codes.md first): register map, medicine-as-code classes, a Boundaries section one-way pointing to partial owners (bathing-and-body-hygiene, scent-perfume-aromatics, myth-symbol purity, funerary), a lore handoff section (one-way, never canon), and a bullet template row S### -> clause. Read the row fragments under .ufo/waves/round-67/rows/ScoutRow*/ as they appear; leave the exact bullet text to integration.",
    ["coverage", "depth"]))
items.append(seat("ScribeGateRows", "scribe",
    "Draft the lesson ## Gate rows at .ufo/waves/round-67/stage/gate-rows.md: one line per opened row S805-S828 (URL | 2026-10-24 | <=25-word located quote) using each fragment's own anchor quote verbatim once fragments exist; for absent fragments leave the S-id line marked MISSING. Also draft the rejected-row Gate lines for S801-S804 (r66 dispositions) and S829-S832 (this round's rejects) with reason+flip from the row files.",
    ["coverage"]))
items.append(seat("ScribeLessonDraft", "scribe",
    "Draft corpus/lessons/round-67.md skeleton at .ufo/waves/round-67/stage/lesson-draft.md in the lane's lesson shape (read corpus/lessons/round-66.md): Round summary naming the three claims + R66-D1..D5 dispositions; ## Gate; ## Mistakes with placeholder rows for mistakes discovered this round (R67-M#) and the mined r66 receipt-sequencing class (the FAIL-recorded counter that held at tip).",
    ["calibration"]))
items.append(seat("ScribeReadmePlan", "scribe",
    "Draft the corpus/README.md index row for the new entry at .ufo/waves/round-67/stage/readme-row.txt: format `- corpus/knowledge/culture-material/medicine-healing-codes.md — <topic verbatim>` plus the partition-count edit instructions (culture-material 33 -> 34, corpus 240 -> 241). Check how existing rows are written first (read the README around the culture-material rows).",
    ["coverage"]))
items.append(seat("ScribeQualityC19", "scribe",
    "Draft QUALITY.md criterion 19 text at .ufo/waves/round-67/stage/quality-c19.md grounded in the r65/r66 receipt-sequencing rejections: receipts run at the stamped lands revision (materialized clone or --lands-graded committed bytes), the receipt records stamped+evaluated revisions and they must be equal for lands-evaluable predicates, carrier-parentage is post-records evidence graded by --topo, never a lands-time leg; cite corpus/lessons/round-66-verifier-spotcheck.md §5 item R66-D3 and the r65 accept-ca-post-records-fail.txt class. Read corpus/QUALITY.md criteria 16-18 for the house style.",
    ["calibration"]))
items.append(seat("ScribeR66LogEntry", "scribe",
    "Draft the missing LOG.md '## Round 66' entry at .ufo/waves/round-67/stage/log-r66.md in the lane's LOG voice (read the round-65 entry in LOG.md): base 94209e8f, lands 65fe8572, records 4589ebdd; claims C (scent entry + 22 rows S779-S800, ACCEPT-C-66 PASS), O (separability bound, ACCEPT-O-66 PASS), Ca (unprovable — committed verdict FAIL, R66-D3 sequencing artifact, CJ re-derivation holds); waves 64-seat v2; dead seat ScoutRow01; census E12/E11 defect note. Every number checkable from reports/round-66/telemetry/ and the committed report.",
    ["calibration"]))
items.append(seat("ScribeR66Scorecard", "scribe",
    "Draft the missing SCORECARD.md '## Axes — round 66' table at .ufo/waves/round-67/stage/scorecard-r66.md in the house shape (read the round-65 table): coverage improved (claim C verified, +22 rows 701->724 re-derived), operability improved (claim O, ACCEPT-O-66 9/9), calibration unprovable (claim Ca — frozen counter committed verdict FAIL; dispositions real; R66-D3 sequencing), depth/freshness/adjacency unchanged; evidence pointers to reports/round-66/telemetry/ receipts; admission line per the filed report. Keep it honest: the frozen verdict is FAIL even though the substance verified post-hoc.",
    ["calibration"]))

# ---- build: executors ----
items.append(seat("ExecCounterSmokeC", "executor",
    "Smoke-test the frozen counter reports/round-67/accept-c.py: run it inside a base-materialized clone (`cd " + LANE + " && git clone --no-local --single-branch --branch main . .scratch/smoke-c && python3 -B ../reports/round-67/accept-c.py --root .scratch/smoke-c --lands " + BASE + "`) plus on the live lane (`--root . --lands " + BASE + "`). Report exact outputs at .ufo/waves/round-67/w1/ExecCounterSmokeC.md: which legs FAIL at base (expected FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC; APPEND/NOHARM/SWEEP vacuous-PASS), whether STAMP correctly FAILS with a wrong --lands, and any counter crash. Do NOT modify the counter.",
    ["operability"]))
items.append(seat("ExecCounterSmokeO", "executor",
    "Smoke-test reports/round-67/accept-o.py and tools/check-receipt-seq.py the same way (base clone + live tree). Verify each committed mutant under .ufo/waves/round-67/stage/mut-o/ actually fails selftest on exactly the pinned checks named in accept-o.py MUT_EXPECT (run each mutant's --selftest, list FAIL lines). Probe one adversarial run: run the tool --topo on the lane repo itself against reports/round-66/telemetry/final-measures-{c,o,ca}.txt — expected: all PASS at tip (carrier 4589ebdd, parent 65fe8572). Report at .ufo/waves/round-67/w1/ExecCounterSmokeO.md.",
    ["operability"]))
items.append(seat("ExecCounterSmokeCa", "executor",
    "Smoke-test reports/round-67/accept-ca.py at base clone + live tree; verify its census leg: run /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file " + LANE + "/corpus/SOURCES.md and paste the full E12/E11 output (expected exit 1 today). Report at .ufo/waves/round-67/w1/ExecCounterSmokeCa.md which Ca legs fail at base and whether any fail for the WRONG reason (crash, wrong path).",
    ["operability", "calibration"]))
items.append(seat("ExecSeparabilityReal", "executor",
    "Build and run the round-67 separability manifest: read reports/round-67/claims.json lands arrays and tools/check-claim-separability.py --help, then write .ufo/waves/round-67/stage/separability-manifest.json (schema kotodama-separability-manifest-v1, copy the shape of reports/round-66/telemetry/separability-manifest.json) and run `python3 -B tools/check-claim-separability.py --manifest <manifest> --jobs 4 --budget 240` on the lane. Report the complete verdict + findings at .ufo/waves/round-67/w1/ExecSeparabilityReal.md; name expected record-dependency findings (Ca->C/O counters, Ca->REC lands) vs any unexpected coupling.",
    ["operability"]))

# ---- connector / sentinel / revenger ----
items.append(seat("ConnectorSiblings", "connector",
    "Sibling-overlap scan for the medicine/healing register + the receipt-seq tool: grep the fleet root /home/vgpnk/Projects/shokunin/*/corpus /PROVINCE.md for medicine/healing/physician/surgery ownership (who owns what; lore canon boundaries; chousa's quote-reopen/receipt tooling precedent — chousa-shokunin/tools/*.py for prior art on receipt/quote checkers). Write .ufo/waves/round-67/w1/ConnectorSiblings.md naming the nearest partial owners (bathing, scent prophylaxis, myth-symbol purity), the one-way handoff rules, and whether any sibling already owns a receipt-sequencing gate (adjacency claim input).",
    ["adjacency", "coverage"]))
items.append(seat("ConnectorPriorArt", "connector",
    "Prior-art scan inside the lane: list every existing tool under tools/ that overlaps receipt/stamp/lands verification (tools/check-claim-separability.py, tools/harness/receipt_guard.py, tools/replay-frozen.py, tools/gates/*), and say exactly what check-receipt-seq.py adds that they lack (lands-evaluated committed-bytes reads; topo carrier-parentage; stamped/evaluated equality). One table; no new code. Write .ufo/waves/round-67/w1/ConnectorPriorArt.md.",
    ["operability", "adjacency"]))
items.append(seat("SentinelScope", "sentinel",
    "Scope/security review of tools/check-receipt-seq.py and the three counters: the tool must never mutate the repo (no git writes — audit every subprocess call), never act on external surfaces, never run outside --root; check the counters for the same. Confirm no path escape (receipt args could name ../..), no shell=True, no eval. Also confirm the wave context's no-network constraint is honored by the seats' own designs. Write .ufo/waves/round-67/w1/SentinelScope.md listing violations or a clean bill with the audited call list.",
    ["operability", "calibration"]))
items.append(seat("RevengerReceipts", "revenger",
    "Reverse-engineer the r65/r66 receipt-sequencing failure chronology from committed bytes only: for round-65 read reports/round-65/telemetry/accept-ca-post-records-fail.txt + final-measures-ca.txt and the LOG correction; for round-66 read reports/round-66/telemetry/final-measures-ca.txt (D2 FAIL no_carrier) + the CJ re-derivation in corpus/lessons/round-66-verifier-spotcheck.md. Produce .ufo/waves/round-67/w1/RevengerReceipts.md: (a) the exact predicate class that fails lands-time, (b) whether the r67 protocol (materialized lands eval + stamped==evaluated + post-records topo) covers BOTH incidents or only one, (c) any third variant the protocol still misses — name it as a routed defect if found.",
    ["calibration", "operability"]))

# ---- attack seats ----
CRITICS = [
    ("CriticClaims", "Attack claims.json itself: ambiguity in 'register unowned' (the census grep pattern — can a lane game it by filename choice?); 'exactly 24 rows' vs declared EXTRA_IDS S801-S804 (can smuggled ids pass SET/APPEND?); whether 'one new entry' plus disposition lands makes NOHARM's allowlist leak the games re-point; predicate sentence vs counter code drift. Write .ufo/waves/round-67/w1/CriticClaims.md."),
    ("CriticPreC", "Pre-data attack on reports/round-67/accept-c.py: run it at base clone + wrong --lands (STAMP must fail); try passing a fabricable NEW_ID row (row with status queued? tier C? wrong opened date? used-by another file?); try a dup live URL with query/fragment variants; try the S753 flip allowance being abused (can another row's cell ride the flip?). Write .ufo/waves/round-67/w1/CriticPreC.md."),
    ("CriticPreO", "Pre-data attack on reports/round-67/accept-o.py + tools/check-receipt-seq.py: try a receipt stamped==evaluated but on the WRONG tree (stale clone — should STAMP fail? what if --lands matches but contents moved?); --topo against a receipt committed twice (merge?); a mutant not in MUT_EXPECT (unregistered must fail); fixture spoof. Write .ufo/waves/round-67/w1/CriticPreO.md."),
    ("CriticPreCa", "Pre-data attack on reports/round-67/accept-ca.py: D2 leg — does the census --file path travel (lane-absolute)? Could a worktree registry different from lands-tree pass? D3 leg — could LOG/SCORECARD entries pass shape while content is wrong (fabricable)? D4 — could a 'rejected' row with garbage teaches pass? SEQ leg — source-text greps vs actual flag behavior (is required=True check spoofable?). Write .ufo/waves/round-67/w1/CriticPreCa.md."),
    ("CriticSizing", "Claim sizing attack: is the medicine register claim provable by a do-nothing control (census pattern misses filenames like 'health-and-healing'?? check whether the pattern word-boundary actually covers the entry filename); is 24 rows the right batch or padding; are 3 claims separable (Ca SEQ reads counters - is that a record-dependency or real coupling?). Write .ufo/waves/round-67/w1/CriticSizing.md."),
    ("CriticSeparabilityDesign", "Read the round-67 claims.json separability_note and the round-66 separability-real.txt output (8 findings): which finding classes should repeat, which should disappear (R66-D3 fixed → Ca no longer carries unevaluable legs?); write expected-findings table at .ufo/waves/round-67/w1/CriticSeparabilityDesign.md for ExecSeparabilityReal to verify against."),
    ("CriticRegistry", "Registry attack: E12/E11 repair — does moving S776/S779-S800 into ## Registry break APPEND's line-equality (rows moved, not edited — is that a mutation the leg allows? does APPEND compare by id or by line position?); S753 '-'->'—' flip allowance — can a row ride it to change its anchor or tier? Check the counter code, write .ufo/waves/round-67/w1/CriticRegistry.md."),
    ("CriticFrontier", "Frontier attack: rejected-row requirement (R66-D5) — can the claim pass with fewer than 2 new rejects (read D4 leg's arithmetic: rej_opened_today >= 6?); S801-S804 teaches 'REJECTED:'+flip — what stops a mined-disguised reject; are the 4 r66 candidates' reject reasons checkable from committed evidence? Write .ufo/waves/round-67/w1/CriticFrontier.md."),
    ("CriticD1Manifest", "D1 manifest attack: reports/round-67/dispositions/r66-wave-evidence-manifest.txt — is the cat-file -e check durable (does it prove CONTENT or just presence?); could the manifest list a path that exists but is empty/wrong (size check?); are excluded scratch trees honestly named (compare manifest vs the real .ufo/waves/round-66/ tree on disk — list what's actually excluded). Write .ufo/waves/round-67/w1/CriticD1Manifest.md."),
    ("CriticReceiptDiscipline", "Protocol attack: the new --lands/stamped/evaluated scheme — does ANY leg still evaluate a post-lands artifact (re-list every leg across the 3 counters and classify: lands-evaluable vs post-records); can a counter print stamped==evaluated while reading uncommitted worktree bytes (dirty-flag printed but not gated?); is post-records.txt itself ever a receipt (self-reference hole)? Write .ufo/waves/round-67/w1/CriticReceiptDiscipline.md."),
    ("CriticMedicineScope", "Domain attack: the medicine register — name every partial-scope neighbor the entry must point to one-way (bathing prophylaxis, scent plague-costume, adornment cosmetics, myth-symbol purity, funerary, warrior wounds, cuisine dietetics); which of the 24 row topics actually duplicates an owned register (S813 plague costume vs scent's S791 pomander? S824 sangoma vs myth-symbol?) — flag rows that should have been rejects. Write .ufo/waves/round-67/w1/CriticMedicineScope.md."),
    ("CriticR66Dispositions", "Disposition-fidelity attack: for each R66-D1..D5, compare the spot-check's exact demanded fix against the disposition leg in accept-ca.py — does D2 demand exit 0 or merely no-E12/E11 (other E's could hide?); does D3's leg actually force CONTENT (a LOG heading with wrong numbers passes?); write the weakest leg + a concrete exploit at .ufo/waves/round-67/w1/CriticR66Dispositions.md."),
]
for name, prompt in CRITICS:
    items.append(seat(name, "critic", prompt, ["calibration"]))

REVIEWERS = [
    ("RevCounterC", "Review reports/round-67/accept-c.py line-by-line against claims.json legs: every declared leg implemented? any leg weaker than its declaration (APPEND flip allowance vs 'the one declared in-place flip'; CAPTURE no-capture token — does claim text allow it?); counter crashes on malformed registry rows (cells<11, missing quote)? Write .ufo/waves/round-67/w1/RevCounterC.md."),
    ("RevCounterO", "Review reports/round-67/accept-o.py line-by-line: is every MUT_EXPECT entry's pinned check list correct against the actual mutants on disk (run them); is the R66 leg's derivation identical to the CJ's (carrier log -1, parent rev-parse, stamp parse); fixture hygiene (temp dirs, no repo writes). Write .ufo/waves/round-67/w1/RevCounterO.md."),
    ("RevCounterCa", "Review reports/round-67/accept-ca.py line-by-line: D1 cat-file -e is presence-only — is that the demanded durability? D2 census --file — does the script even accept --file (verify); D4 arithmetic off-by-one (>=6 vs >=4+2); SEQ greps 'mv_rev == lands' — is that string actually in all three counters byte-exact? Write .ufo/waves/round-67/w1/RevCounterCa.md."),
    ("RevToolSeq", "Review tools/check-receipt-seq.py: is --lands truly committed-bytes (git show) or does it fall back to worktree; pair_args edge cases (receipt named foo.py?); unicode/CRLF receipts; the selftest's own coverage vs the code paths. Write .ufo/waves/round-67/w1/RevToolSeq.md."),
    ("RevBaseCensus", "Independent base census: re-run the claim-C ownership census at base with a DIFFERENT pattern than the claim (wider: medicine|medical|health|heal|cure|disease|sick|remed|surg|anatom|plague|epidemic); report any whole-register filename hit; also topic-line sweep. If a hit exists the claim statement is false — say so loudly. Write .ufo/waves/round-67/w1/RevBaseCensus.md."),
    ("RevIntegrity", "Integration-risk review (mirror r66 HIGH findings): which claim bytes could land outside counters' view — S829+ ids sneaking into the claim set, row files under rows/ not matching final registry lines (ROW= drift), entry bullets citing wrong ids; how would the counter catch each? Write .ufo/waves/round-67/w1/RevIntegrity.md."),
    ("RevLoreHandoff", "Adjacency review: the medicine entry's lore handoff — which sections must be one-way (deity/canon claims, real-world rights on medical texts); nearest prior art chousa-shokunin tools; boundary bullets the entry needs (name them by file+section like r66's §12 findings). Write .ufo/waves/round-67/w1/RevLoreHandoff.md."),
    ("RevWaveShape", "Round-shape review: does this wave meet the v2 band (64 seats, >=25% attack: count the roles); §3 minimum role split met inside it (planner=L1, 1 connector+, 3 executor+, 1 scribe+, 1 scout+, 1 reviewer+, 1 critic+); flag any padding (seats without a concrete item). Write .ufo/waves/round-67/w1/RevWaveShape.md."),
    ("RevDryRunFidelity", "Dry-run fidelity (QUALITY 8/9/11): compare reports/round-67/telemetry/dry-run-*.txt commands to claims.json commands verbatim (does the dry run's --lands flag value match the declared <base> substitution?); every expected-fail leg named in controls-*.txt actually failing? Write .ufo/waves/round-67/w1/RevDryRunFidelity.md."),
    ("RevEntrySpec", "Review .ufo/waves/round-67/stage/entry-spec.md + the row fragments for the 24 topics: which topics overlap owned registers or duplicates (S826 moxibustion vs S807 TCM needle-lore? S824 sangoma vs myth-symbol healing?); which bullets likely fail RESTATE (teaches echo, <3 quote words); report row-fragment defects (malformed ROW=, quote >25 words, wrong id). Write .ufo/waves/round-67/w1/RevEntrySpec.md."),
    ("RevSourceSupport1", "Blind-support review rows S805-S810 only: for each, open the row fragment, re-fetch live URL + capture yourself, verify the anchor quote in body text, then judge whether the row's teaches cell is actually supported (not just quotable). Write .ufo/waves/round-67/w1/RevSourceSupport1.md one verdict per id with evidence."),
    ("RevSourceSupport2", "Same contract for S811-S816. Write .ufo/waves/round-67/w1/RevSourceSupport2.md."),
    ("RevSourceSupport3", "Same contract for S817-S822. Write .ufo/waves/round-67/w1/RevSourceSupport3.md."),
    ("RevSourceSupport4", "Same contract for S823-S828. Write .ufo/waves/round-67/w1/RevSourceSupport4.md."),
    ("RevDispositionsD1", "Verify the D1 disposition manifest once written: every INCLUDE path exists on disk AND is non-empty AND is not inside a scratch/.git tree; every named exclusion class actually excludes (list what stays out); compare vs `find .ufo/waves/round-66 -type f` — coverage % by file class. Write .ufo/waves/round-67/w1/RevDispositionsD1.md."),
    ("RevLedger66", "Verify the drafted LOG.md round-66 entry + SCORECARD table against reports/round-66/telemetry/ committed receipts: every number (22 rows, 9/9, PASS/FAIL, hashes) must match the receipts byte-for-byte; flag any 'PASS' where the frozen verdict was FAIL. Write .ufo/waves/round-67/w1/RevLedger66.md."),
    ("RevGateQuotes", "Run tools/check-gate-quotes.py on corpus/lessons/round-66.md and any drafted round-67 lesson; check each new Gate row's quote <=25 words and located; check the rejected-row teaches cells carry REJECTED:+flip; write .ufo/waves/round-67/w1/RevGateQuotes.md."),
    ("RevCensusE12", "Verify the E12/E11 repair plan: list the exact 23 misplaced rows + S753 cell; propose the minimal edit (move rows into Registry section preserving order?); run sources-census.sh validate --file on a COPY with the fix applied and paste exit code + remaining warnings (W03/W04 must be the same 28 pre-existing). Write .ufo/waves/round-67/w1/RevCensusE12.md."),
    ("RevStampDesign", "Adversarial review of the stamp mechanism itself: is '--lands <hash> + rev-parse main' spoofable (a lane could pass --lands = tip always — what binds lands to the claim?); should stamped be read from claims.json instead; does STAMP FAIL on detached HEAD (jj-colocated repos); recommend the exact binding. Write .ufo/waves/round-67/w1/RevStampDesign.md."),
    ("RevManifestSep", "After ExecSeparabilityReal lands: re-run the manifest yourself with --static-only and with --max-runs 1 — do partial modes degrade honestly; are the 8-expected findings the same class as r66; write .ufo/waves/round-67/w1/RevManifestSep.md."),
]
for name, prompt in REVIEWERS:
    items.append(seat(name, "reviewer", prompt, ["calibration"]))

# ---- mutation testers ----
items.append(seat("MutCounterC", "mutation-tester",
    "Byte-mutate reports/round-67/accept-c.py at .ufo/waves/round-67/stage/mut-c/: produce 4-6 mutants each breaking one leg (e.g. ONEID >=1 instead of ==1; RESTATE inq<2; APPEND allowed_new unbounded; CAPTURE skipped; STAMP equal-check dropped). For each, run the mutant on a base clone + describe expected vs actual verdict — a mutant that changes nothing is a failed mutation (report it). Do NOT touch the real counter. Write .ufo/waves/round-67/w1/MutCounterC.md with mutant names, diffs, verdicts; commit mutant files under stage/mut-c/ (one .py each + results.txt).",
    ["operability", "calibration"]))
items.append(seat("MutEntryClass", "mutation-tester",
    "Mutation-test the claim-C entry class: write .ufo/waves/round-67/stage/mut-entry/ variants of a minimal fake entry (missing - topic:, h3 present, 251 lines, bullet citing foreign S-id) — predict which legs catch each, then run accept-c.py against a fixture registry+entry in a temp dir (never mutate real files); report at .ufo/waves/round-67/w1/MutEntryClass.md which mutants PASS the counter unexpectedly (gaps to route to r68).",
    ["coverage", "calibration"]))

spec = {
    "wave": "kotodama-r67-v2",
    "milestone": "Round 67 single v2 wave (build+attack, 64 seats)",
    "reportDir": ".ufo/waves/round-67/w1",
    "axes": ["coverage", "operability", "calibration", "depth",
             "freshness", "adjacency"],
    "context": CONTEXT,
    "items": items,
}

ATTACK = {"reviewer", "critic", "mutation-tester", "sentinel"}
n_attack = sum(1 for i in items if i["role"] in ATTACK)
print(f"# seats={len(items)} attack={n_attack} ({n_attack/len(items):.1%})")
with open(".ufo/waves/round-67/spec-v2.json", "w") as fh:
    json.dump(spec, fh, indent=1)
print("wrote .ufo/waves/round-67/spec-v2.json")
