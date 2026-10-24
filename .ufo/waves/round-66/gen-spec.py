#!/usr/bin/env python3
"""Generate the round-66 single v2 wave spec (64 seats, >=25% attack roles)."""
import json

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"

CONTEXT = """# Goal
Kotodama round 66 (hyaku run 5, 2026-10-24): ONE v2 wave of 64 seats, build+attack together. Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (jj-colocated; base revision 94209e8f80969dbac48d56c5d0e2e623635b8616). All lane-relative paths below resolve under that repo. Three claims with frozen predicates (reports/round-66/claims.json, written pre-wave):
- C (coverage, sourced): new entry corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md + exactly 24 mined registry rows S777-S800 (tier A/B, opened 2026-10-24, used-by the entry, cited exactly once each). Predicate: ACCEPT-C-66: every leg of reports/round-66/accept-c.py prints PASS.
- O (operability, capability hardening): tools/check-claim-separability.py returns a verdict inside a round's budget (--timeout/--jobs/--budget/--max-runs/--static-only; skipped runs are honest partial verdicts, exit 2, never fabricated <base>). Predicate: ACCEPT-O-66: every leg of reports/round-66/accept-o.py prints PASS.
- Ca (calibration, records): the round-65 closure's routed defects R65-D1..D4 dispositioned in this round's records (D1 S753 anchor durability via fresh capture + S776 supersession; D2 receipt commit-ancestry re-derivation; D3 dispatch registry + seat-evidence receipt; D4 bounded separability run committed). Predicate: ACCEPT-CA-66: every leg of reports/round-66/accept-ca.py prints PASS.
Frozen counters, claims.json, base dry-run receipts (reports/round-66/telemetry/dry-run-*.txt) and pre-data controls (controls-*.txt) are on disk at the lane tip - read them before attacking. Build seats: your output is a draft under .ufo/waves/round-66/ - the L1 reviews, integrates and is the only committer. Attack seats: try to break the frozen instruments and drafts - shortcut classes, bypasses, stale receipts, false stamps, duplicates, tier inflation, fabricated anchors; name what you attack.

# Rules (bind every seat)
Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
Leaf member - no subagent dispatch, no swarm of your own. Absolute paths for writes, under /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/ only, at the exact paths your item names. Never mutate the fleet repo, sibling lanes, lane jj state or the lane Git index; never run git/jj writes; read-only git is fine; do not commit - the L1 integrates.
Tooling authorization (operator, 2026-10-19): you may install or upgrade tools that help the task - read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record tool/version/channel/reason in your report). pacman guard (orchestrator ruling 2026-10-20, in force): all pacman transactions are PAUSED host-wide - install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R/downgrade.
Report: write your scoped findings to /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/w1/<SEAT>.md (the validator renders every `Report:` trailer relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin - write it at that absolute path)."""

RULES = """Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
"""

ROW_TOPICS = [
    ("S777", "UNESCO intangible-heritage incense listing (UAE/Omani or Arabian incense craft) - official listing page"),
    ("S778", "kyodo Japanese incense ceremony - museum or scholarly source on the way of fragrance"),
    ("S779", "the ancient Egyptian kyphi incense recipe - scholarly source (temple inscriptions, Ebers/Dioscorides)"),
    ("S780", "frankincense and myrrh production and trade (Met Heilbrunn or museum/scholarly source)"),
    ("S781", "perfume in ancient Rome and Greece - museum or scholarly overview (unguentaria, olive-oil base)"),
    ("S782", "the medieval Islamic distillation of rosewater/attars - scholarly or museum source (Ibn Sina attribution calibration)"),
    ("S783", "Hungary Water and the medieval alcohol perfume - scholarly or museum source"),
    ("S784", "grasse perfumery as UNESCO intangible heritage - official listing"),
    ("S785", "Mesoamerican copal incense - museum or scholarly source on ritual use"),
    ("S786", "Chinese incense culture and the xiang tradition - scholarly or museum source"),
    ("S787", "Vedic and Hindu puja fragrance (sandalwood, ghee lamps) - scholarly or museum source"),
    ("S788", "the anthropology of smell - class/gender codes of scent (Classen or scholarly survey)"),
    ("S789", "attar of roses production (Bulgarian rose valley or scholarly source)"),
    ("S790", "scented gloves and Renaissance perfumed leather - museum collection source"),
    ("S791", "the pomander and plague-era scent prophylaxis - museum or scholarly source"),
    ("S792", "Aztec and Maya flower/scent codes - museum or scholarly source"),
    ("S793", "Amber/ambergris as precious scent material - museum or scholarly source"),
    ("S794", "court perfume at Versailles and the perfumer's guild - scholarly or museum source"),
    ("S795", "incense clocks and timekeeping by burning - scholarly or museum source"),
    ("S796", "the perfume trade in the medieval Islamic city (souk perfumers) - scholarly source"),
    ("S797", "scented oils and anointing in ancient Egypt and the Near East - museum or scholarly source"),
    ("S798", "the alabastron and aryballos as perfume vessels - museum collection source"),
    ("S799", "Edo-period kodo incense games (jushuko/kumiko) - museum or scholarly source"),
    ("S800", "the perfume workshop at Pompeii or Herculaneum - archaeology source"),
]

ROW_MODEL = """Per row write .ufo/waves/round-66/rows/<SEAT>/row-<SID>.txt with exactly these labelled lines:
ROW=| <SID> | <source name> - <live URL> ; https://web.archive.org/web/<14-digit ts>id_/<original URL> . | <kind> | <A or B only> | <scope <=60 chars> | "<anchor quote 8-25 body words>" | <teaches cell <=240 chars> | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md |
BULLET=<one clause: 6-25 content words, >=3 in-order content words from the quote, no run >12 words copied from the quote, >=1 novel content word, NOT a near-copy of the teaches cell (word-token coverage <80% in-order)>
VERIFY=<live curl status + date; quote in body text Y/N; access limits>
CAPTURE=<wayback ts + original URL; original query-aware-normalizes equal to the live URL>
ACCESS=<redirects, rate limits, paywalls a re-opener needs>
Rejects go to rows/<SEAT>/rejects.txt as <URL> - <reason>; flip: <what would change it>. The live URL must be unique: grep it against corpus/SOURCES.md and all fragments. Sources: tier A/B only (peer-reviewed, official bodies, museum/university, scholarly books). Verify everything yourself with curl."""


def seat(name, role, prompt, axes):
    return {"name": name, "role": role, "axes": axes, "milestone": "r66-v2",
            "prompt": RULES + prompt}


items = []

# ---- build: gap + rows ----
items.append(seat("ScoutGapScent", "scout",
    "Verify the claim-C gap at the base, then write .ufo/waves/round-66/rows/ScoutGapScent/gap.md with exact commands+outputs:\n"
    "1) cd " + LANE + " && git ls-tree -r --name-only 94209e8f80969dbac48d56c5d0e2e623635b8616 -- corpus/knowledge | grep -ciE '(^|[^a-z])(scent|perfume|aromatic|incense|fragran|cosmetic|unguent)([^a-z]|$)'  (expect 0)\n"
    "2) grep -rniE '^-?\\s*topic\\s*:.*(scent|perfume|aromatic|incense|fragran|cosmetic|unguent|odor|smell)' corpus/knowledge/  (list every topic-line owner; expect only partial-scope mentions)\n"
    "3) sibling ownership: grep -rliE 'perfum|incense|aromatic|scent' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5\n"
    "End gap.md with a 5-line build order for the entry: register map; source-grounded bullets by class (sacred/ritual incense, personal fragrance/cosmetics, trade/materials, timekeeping/measurement, social codes); cross-cultural patterns; design protocol; calibration; one-way pointing to partial owners; lore handoff.",
    ["coverage", "adjacency"]))

for i in range(0, len(ROW_TOPICS), 2):
    pair = ROW_TOPICS[i:i + 2]
    seat_name = "ScoutRow%02d" % (i // 2 + 1)
    task = "ROW-OPENING item (claim C): open exactly two registry rows, " + \
        " and ".join(s for s, _ in pair) + ". For each: " + \
        "; ".join("%s -> %s" % (s, t) for s, t in pair) + ".\n" + ROW_MODEL
    items.append(seat(seat_name, "scout", task, ["coverage", "depth"]))

for i, (sid, topic) in enumerate([(f"S80{n+1}", t) for n, t in enumerate([
        "cosmetics in the ancient world (lead: museum survey)",
        "smell and disease theory (lead: humoral/miasma source)",
        "scent in medieval Christian liturgy (lead: scholarly source)",
        "Japanese sari/incense robes airing tradition (lead: museum)"])]):
    items.append(seat("ScoutReject%02d" % (i + 1), "scout",
        "REJECT-CANDIDATE item (claim C frontier): open the candidate topic " + topic +
        " and decide admit-or-reject for a row slot " + sid +
        ". If admitted, write rows/<SEAT>/row-" + sid + ".txt in the row format below; "
        "if rejected write rows/<SEAT>/rejects.txt with <URL> - <reason>; flip: <what would change it> "
        "and a one-line justification. Never fabricate a capture.\n" + ROW_MODEL,
        ["coverage", "calibration"]))

# ---- build: drafting + review of build ----
items.append(seat("ScribeEntrySpec", "scribe",
    "Pre-read/design seat (claim C). Read reports/round-66/accept-c.py (legs FILE/SET/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/CAPTURE/TOPIC), reports/round-66/claims.json claim C, and the round-65 model entry corpus/knowledge/culture-material/games-play-sport-contests.md. Write .ufo/waves/round-66/stage/entry-spec.md: the exact entry skeleton for scent-perfume-aromatics-codes.md (<=16 H2, - topic: text, frontmatter modelled on the round-65 entry, one bullet slot per S777-S800 grouped by scent class), the RESTATE rules bullets must satisfy (in-order quote words >=3, teaches coverage <80%, >=1 novel content word), and the corpus/README.md edit recipe (culture-material 32 -> 33, footer 239 -> 240, index row verbatim topic text).",
    ["coverage", "depth"]))
items.append(seat("ScribeGateRows", "scribe",
    "Draft the lesson Gate rows for S777-S800 from the row fragments under .ufo/waves/round-66/rows/ (if a fragment is absent, record the dependency). Write .ufo/waves/round-66/stage/gate-rows.md: one '- S### | live URL (capture) | 2026-10-24 | \"<quote>\"' line per row in the round-65 lesson's Gate shape (corpus/lessons/round-65.md '## Gate'), plus a disposition note for the S776 supersession row (S753's durability repair). Do not invent quotes; a row without a verified quote is listed as 'awaiting fragment'.",
    ["coverage", "calibration"]))
items.append(seat("ScribeLessonDraft", "scribe",
    "Draft the round-66 lesson body for corpus/lessons/round-66.md: a '## Mistakes' section skeleton in the R66-Mn shape (class - evidence pointer - captured-by - fix) seeded from corpus/lessons/round-65.md mistakes and the round-65 spotcheck's routed defects D1-D4; a '## Gate' preamble naming the S776 supersession; and a one-paragraph disposition block per routed defect D1-D4. Write .ufo/waves/round-66/stage/lesson-draft.md. Never claim a defect is fixed - phrase as 'to be dispositioned by <evidence>'.",
    ["calibration", "coverage"]))
items.append(seat("ScribeReadmePlan", "scribe",
    "Draft the corpus/README.md delta for the new entry: the index row (verbatim - topic: text), the culture-material partition count bump, the 'Known gaps (frontier)' bullet naming partial owners, and the footer 'Counts checked' + total. Write .ufo/waves/round-66/stage/readme-plan.md as a unified diff the L1 can apply.",
    ["coverage"]))

# ---- build: counter smoke ----
for i, (nm, tgt) in enumerate([
        ("ExecCounterSmokeC", "reports/round-66/accept-c.py"),
        ("ExecCounterSmokeO", "reports/round-66/accept-o.py"),
        ("ExecCounterSmokeCa", "reports/round-66/accept-ca.py")]):
    items.append(seat(nm, "executor",
        "Counter smoke (build). From " + LANE + " run `python3 -B " + tgt +
        " --root .` and record every leg + exit code; then `python3 -B " + tgt +
        " --help` (does it crash? a missing --help is acceptable). Write .ufo/waves/round-66/stage/" +
        nm.lower() + ".md listing every defect/crash/ambiguity (path:line + minimal fix). Do NOT edit counters - the L1 owns them.",
        ["operability"]))

# ---- build: connector ----
items.append(seat("ConnectorSiblings", "connector",
    "SIBLING-OVERLAP. Run: grep -rliE 'scent|perfume|incense|aromatic|unguent|kyphi|attar|copal' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin /home/vgpnk/Projects/shokunin/kotoba-shokunin 2>/dev/null | head; and grep -rliE 'check-claim-separability|separability' /home/vgpnk/Projects/shokunin/*/tools 2>/dev/null | grep -v kotodama. Write .ufo/waves/round-66/w1/ConnectorSiblings.md: who owns what (nearest prior art), whether any sibling owns a scent/perfume register entry (adjacency: report, do not absorb), and the one-way handoff boundary for the entry's lore-facing section.",
    ["adjacency", "coverage"]))

# ---- build: partial-owner verification ----
items.append(seat("ScoutPartialOwners", "scout",
    "Read the scent-adjacent corpus entries that mention perfume/incense/aromatics without owning the register: corpus/knowledge/culture-material/bathing-and-body-hygiene.md, corpus/knowledge/culture-material/fire-fuel-light.md, corpus/knowledge/culture-material/adornment-body-codes.md, corpus/knowledge/myth-symbol/animal-symbolism.md, corpus/knowledge/culture-material/timekeeping-instruments.md. For each, quote the one line where scent appears and classify: partial owner (one-way cite) vs incidental mention. Write .ufo/waves/round-66/w1/ScoutPartialOwners.md with per-file verdicts the entry will point to one-way.",
    ["coverage", "depth"]))

# ---- attack seats ----
ATTACK = [
    ("RevCounterC", "reviewer",
     "ATTACK reports/round-66/accept-c.py. (1) Craft the minimal bullet equal to a teaches cell plus ONE trailing novel word: show (worksheet math) whether the <80% in-order token-coverage rule fails it. (2) Two rows whose URLs differ only in query must fail LINK norm-dup. (3) An 8-word bullet, 3 in-order quote words, teaches coverage 0.79 must PASS (no false positive). Give exact crafted strings + expected leg verdicts in .ufo/waves/round-66/w1/RevCounterC.md.", ["operability"]),
    ("RevCounterO", "reviewer",
     "ATTACK reports/round-66/accept-o.py. (1) Does the MUT leg's per-mutant expectation table cover every mutant actually in .ufo/waves/round-66/stage/mut-o/? Name any mutant that could survive. (2) Is the BOUND fixture's sleep 1.5s > budget 0.5 deterministic, or racy under load? (3) Can the FIXTURES leg pass while the tool's verdict is silently wrong elsewhere? Write .ufo/waves/round-66/w1/RevCounterO.md.", ["operability"]),
    ("RevCounterCa", "reviewer",
     "ATTACK reports/round-66/accept-ca.py. (1) The D2 leg runs `git log -1 main -- <receipt>`: in a counterfactual clone what does main resolve to, and can a receipt stamped for the wrong lands pass? (2) The D3 leg counts named seat files that exist: can it pass while seats are dead? (3) The QUOTES leg names ids S776-S800: is the regex right (S776, S777-S800)? Write .ufo/waves/round-66/w1/RevCounterCa.md.", ["calibration"]),
    ("RevClaimC", "reviewer",
     "ATTACK claim C's declared gap. Re-derive the base filename census; run the topic-line sweep; name every corpus/knowledge file that would argue the register is already held (partial owners count as not-owners but must be named). If the claim's '0 owners' is reachable by a do-nothing control on a technicality (word-boundary miss, e.g. a filename containing 'aromatics' as substring), name it loudly. Write .ufo/waves/round-66/w1/RevClaimC.md.", ["coverage"]),
    ("RevClaimO", "reviewer",
     "ATTACK claim O's premise. Read .ufo/waves/round-65/w1/RevSeparability.md MED-4 and tools/check-claim-separability.py: is the upgraded dynamic leg actually bounded (does --budget cover the git_free materialization + clone time, or only the subprocess timeout)? Can a needs_git clone still stall? Write .ufo/waves/round-66/w1/RevClaimO.md.", ["operability"]),
    ("RevClaimCa", "reviewer",
     "ATTACK claim Ca's premise: are D1-D4 the right dispositions? For each routed defect in corpus/lessons/round-65-verifier-spotcheck.md section 5, does the declared leg actually evidence the fix, or only a proxy (e.g. D2's leg verifies a receipt's commit ancestry but not the lands' real parent)? Write .ufo/waves/round-66/w1/RevClaimCa.md.", ["calibration"]),
    ("RevSeparability", "reviewer",
     "ATTACK the separability design in claims.json + reports/round-66/separability-manifest.json (if present, else the manifest_units block): does the unit allocation hide a cross-claim path-name (Ca land naming C's new entry or O's tool path)? Does Ca's D2 git leg inside needs_git actually isolate, or does it read lane refs? Write .ufo/waves/round-66/w1/RevSeparability.md.", ["calibration", "operability"]),
    ("RevReceipts", "reviewer",
     "ATTACK the D2 receipt design: the new leg derives lands as parent-of-receipt-carrying-commit. Craft the adversarial commit orders that break it (receipt committed twice in different commits; receipt amended; receipt carried by a merge). Which does the leg miss, and does the miss matter? Write .ufo/waves/round-66/w1/RevReceipts.md.", ["calibration"]),
    ("RevD1Anchor", "reviewer",
     "ATTACK the S753 repair: the live URL now returns 200 pdf, but the committed capture 20250926172224 still replays 404 today. Is citing S776 (fresh capture 20261024111013) + the live URL sufficient durability under contract v1 (a row is a claim only if resolvable at closure)? Re-check the fresh capture replays and the CDX listing. Write .ufo/waves/round-66/w1/RevD1Anchor.md.", ["calibration"]),
    ("RevGateRows", "reviewer",
     "Read every row fragment under .ufo/waves/round-66/rows/*/row-*.txt when present (or the registry diff when integrated): for each new S777-S800 row, is the anchor quote verbatim in the fetched page/PDF? Re-open 4 rows at random with curl + pdftotext; name any quote that does not locate. Write .ufo/waves/round-66/w1/RevGateRows.md.", ["calibration", "coverage"]),
    ("RevTeaches", "reviewer",
     "For each new row S777-S800 (fragment or registry line): does the teaches cell overreach the anchor quote (the quote supports the teaches, not vice versa)? List every row whose teaches adds a claim the quote does not carry. Write .ufo/waves/round-66/w1/RevTeaches.md.", ["coverage", "calibration"]),
    ("RevEntryDraft", "reviewer",
     "When a draft of corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md exists (worktree or a seat's spec), read it against accept-c.py RESTATE: which bullets will fail ONEID/RESTATE, which teaches a near-copy, which cites a row twice? Write .ufo/waves/round-66/w1/RevEntryDraft.md with per-line findings.", ["coverage", "calibration"]),
    ("RevReadmePlan", "reviewer",
     "Read .ufo/waves/round-66/stage/readme-plan.md when present (else the committed corpus/README.md): is the culture-material count math right (32->33, corpus 239->240), does the index row carry the verbatim topic text, and does the footer 'Counts checked' date/command match? Write .ufo/waves/round-66/w1/RevReadmePlan.md.", ["coverage"]),
    ("RevManifest", "reviewer",
     "ATTACK reports/round-66/separability-manifest.json (or the manifest_units block in claims.json if the file is absent): list every land path that is absent at base and every unit whose lands a sibling unit's lands name. The expected-finding set must be exactly the declared Ca->REC class; anything else is a defect. Write .ufo/waves/round-66/w1/RevManifest.md.", ["calibration", "operability"]),
    ("CriticPreC", "critic",
     "PRE-DATA CRITIC (claim C). Read reports/round-66/claims.json claim C + reports/round-66/accept-c.py. (1) Do-nothing control: could a sourceless stub entry + 24 self-invented rows pass? Walk each leg: which fail, which survive. (2) Universal-clause audit: any 'all/complete/every' no counter enumerates? (3) Sizing: is 24 rows reachable by 12 scouts x 2 + 4 reject candidates? (4) CAPTURE leg: does 'no-capture' token actually exempt, and is that attackable? Write .ufo/waves/round-66/w1/CriticPreC.md.", ["coverage"]),
    ("CriticPreO", "critic",
     "PRE-DATA CRITIC (claim O). Read reports/round-66/accept-o.py + tools/check-claim-separability.py. (1) Is the FIXTURES 180s bound reachable on a cold run (git lane builds + 5 subprocess invocations)? (2) Does BOUND's 'no <base>' check survive a mutant that names UNRESOLVED but still exits 2? (3) Is selftest 63/63 a stable pin, or does it break when the tool's check count changes legitimately? Write .ufo/waves/round-66/w1/CriticPreO.md.", ["operability"]),
    ("CriticPreCa", "critic",
     "PRE-DATA CRITIC (claim Ca). Read reports/round-66/accept-ca.py + corpus/lessons/round-65-verifier-spotcheck.md section 5. (1) Do the four D legs cover the whole routed defect set or only paraphrases? (2) The D2 leg is process verification: does passing it here actually disposition R65-D2, or merely assert the new rule? (3) QUOTES names ids by regex: does it catch a lesson that names S800 but skips S776? Write .ufo/waves/round-66/w1/CriticPreCa.md.", ["calibration"]),
    ("CriticClaims", "critic",
     "Cross-claim audit of reports/round-66/claims.json: (1) Are the three claims causally separable in practice (can each verify without the others' lands)? (2) Is any claim on the same axis as another (two on one axis = one claim)? (3) Does claim O's 'capability hardening' restate the round-65 defect as the claim statement, and is the upgrade a real axis move or a repair? Write .ufo/waves/round-66/w1/CriticClaims.md.", ["calibration"]),
    ("MutCounterC", "mutation-tester",
     "MUTATE reports/round-66/accept-c.py: 4 byte-mutants in copies under .ufo/waves/round-66/stage/mut-c/ (never the committed file): coverage 0.8 -> 0.99; ONEID drops citation_exact count; APPEND count relaxed; CAPTURE 'no-capture' substring widened. Per mutant: the land state that makes it print PASS where the original prints FAIL (kill description); does a landed tree kill it? Mutant table in .ufo/waves/round-66/w1/MutCounterC.md.", ["operability"]),
    ("MutCounterO", "mutation-tester",
     "MUTATE reports/round-66/accept-o.py: 3 byte-mutants in copies under .ufo/waves/round-66/stage/mut-o-counter/ (never the committed file): mut_expect lambda weakened to always-true; FIXTURES bound 180 -> 9999; SELFTEST count '63/63' relaxed. Per mutant: kill description. Write .ufo/waves/round-66/w1/MutCounterO.md.", ["operability"]),
    ("MutTool", "mutation-tester",
     "MUTATE tools/check-claim-separability.py beyond the committed mutants: (1) a mutant that raises --timeout default to 99999 (does any leg catch it?); (2) a mutant that prints UNRESOLVED but exits 0 (does the report's exit-code map catch it?); (3) a mutant that drops the unresolved-sort line so UNRESOLVED output is nondeterministic (does any fixture catch it?). Write .ufo/waves/round-66/w1/MutTool.md.", ["operability", "calibration"]),
    ("MutEntry", "mutation-tester",
     "When the entry lands, MUTATE corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md in a copy: (1) one bullet's citation id changed to a base row (S750); (2) one bullet deleted; (3) the topic line paraphrased. Which accept-c legs catch each? Write .ufo/waves/round-66/w1/MutEntry.md.", ["coverage", "operability"]),
    ("SentinelScope", "sentinel",
     "SCOPE GUARD. From " + LANE + " verify: git -C /home/vgpnk/Projects/shokunin status --porcelain | head -20 (seat notes misrooted at fleet root? name any, touch nothing); round-66 writes only under reports/round-66/, .ufo/waves/round-66/, and the claims' land paths; tools/reopen-row.py unchanged (git diff 94209e8f80969dbac48d56c5d0e2e623635b8616 -- tools/reopen-row.py | wc -l expect 0); corpus/knowledge diff names only the new entry plus the games-entry S776 re-point. Write .ufo/waves/round-66/w1/SentinelScope.md with evidence and any violation.", ["calibration"]),
    ("RevengerRouted", "revenger",
     "ROUTED-INTENT (claim Ca). From corpus/lessons/round-65-verifier-spotcheck.md section 5 alone, quote the operative sentence per defect R65-D1..D4, then compare against the declared legs in reports/round-66/claims.json + reports/round-66/accept-ca.py. Per defect: satisfies / over-reaches (edits filed bytes) / misses. One verdict per defect with path:line evidence in .ufo/waves/round-66/w1/RevengerRouted.md.", ["calibration"]),
    ("SimplifierCounters", "simplifier",
     "SIMPLEST-BYPASS. Read reports/round-66/accept-c.py (RESTATE near-copy, LINK, CAPTURE), accept-o.py (MUT, BOUND, FIXTURES), and accept-ca.py (D1-D4). Per leg: the cheapest fixture that beats it as written - a bullet that paraphrases teaches with synonyms; a receipt printed from a filtered run; a seat-evidence file naming 8 seat paths that are empty; a mutant whose extra legs the table pins wrongly. Write .ufo/waves/round-66/w1/SimplifierCounters.md - per leg: bypass candidate + killed Y/N + why.", ["operability", "calibration"]),
    ("RevIntegrity", "reviewer",
     "INTEGRITY AUDIT: the lane must dispatch this wave as ONE task call. Verify .ufo/waves/round-66/spec-v2.json exists, reads as a valid spec (64 items, role mix), and that the taskcall artifact is the validator's rendered output (no hand-edited tasks). Check for duplicated seat names, missing Report trailers, and whether the spec's context names absolute paths correctly. Write .ufo/waves/round-66/w1/RevIntegrity.md.", ["calibration"]),
    ("RevD3Evidence", "reviewer",
     "ATTACK the D3 disposition design: does 'seat report files exist' + 'registry.json member count' actually prove the >=8 dispatched-seat floor, or can it be satisfied by empty reports and a fabricated registry? What evidence would you demand beyond existence? Write .ufo/waves/round-66/w1/RevD3Evidence.md.", ["calibration"]),
    ("RevBaseCensus", "reviewer",
     "Re-derive the claim-C base census independently: git ls-tree on the lane's main at the declared base for the scent filename pattern, PLUS a word-bounded variant and a raw-substring variant (three totals). Also census corpus/knowledge for filenames matching dye|pigment|paint|soap to confirm no adjacent unowned register is being skipped. Write .ufo/waves/round-66/w1/RevBaseCensus.md.", ["coverage"]),
    ("CriticSeparabilityDesign", "critic",
     "Read claims.json separability note: the declared expected class is Ca->REC. Attack it: is there a hidden C->O (accept-c reads the upgraded tool?), O->C (the mut-o fixtures name the entry path?), Ca->C (the QUOTES gate ids live in the registry Ca does not own)? For each hypothetical, show the actual path that would name it or prove it cannot. Write .ufo/waves/round-66/w1/CriticSeparabilityDesign.md.", ["calibration", "operability"]),
]

ATTACK += [
    ("RevSourceSupport", "reviewer",
     "BLIND SUPPORT sample (claim C): pick 6 rows at random among S777-S800 (fragments or registry). For each, fetch the source independently (live or capture) and judge whether the row's teaches cell is supported by the anchor quote's context, not just the quote's surface words. One verdict per row (support / overreach / unsupported) with the located line. Write .ufo/waves/round-66/w1/RevSourceSupport.md.", ["coverage", "calibration"]),
    ("RevWaveEvidence", "reviewer",
     "Wave-evidence check (claim Ca D3): list every file under .ufo/waves/round-66/ at the time you read this; for each expected seat name in spec-v2.json, is there a report? Any seat that returned a file but no findings, or a non-.md artifact? Any seat prompt that asks for writes outside .ufo/waves/round-66/? Write .ufo/waves/round-66/w1/RevWaveEvidence.md.", ["calibration"]),
    ("RevLoreHandoff", "reviewer",
     "Adjacency check on the entry draft or integrated file: does corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md hand canon to lore (never claims canon)? Compare its handoff section against corpus/knowledge/synthesis/worldbible-integration-contract.md and the round-65 model's own one-way pointing. Write .ufo/waves/round-66/w1/RevLoreHandoff.md.", ["adjacency", "coverage"]),
    ("RevD4Bound", "reviewer",
     "ATTACK the D4 disposition: does telemetry/separability-real.txt (when written) show a COMPLETE verdict (no PARTIAL, acceptance_runs equals the manifest's needed count), or could it pass while the run skipped repair attempts? Re-derive the needed run count from the manifest (units, acceptance-bearing units, ordered pairs) and compare. Write .ufo/waves/round-66/w1/RevD4Bound.md.", ["operability", "calibration"]),
    ("CriticSizing", "critic",
     "SIZING AUDIT (all three claims): is each after-state one concrete value a closure can re-derive with one command over committed bytes? (1) claim C's 'corpus 239 -> 240' vs the registry '701 -> 725+': is the unbounded plus sign a measurable target? (2) claim O's 'a verdict inside a round's budget': is the fixture bound the claim or a proxy? (3) claim Ca's four D-legs: which is verifiable only via a receipt a do-nothing seat could fabricate? Write .ufo/waves/round-66/w1/CriticSizing.md.", ["calibration"]),
    ("MutRegistry", "mutation-tester",
     "MUTATE the registry diff surface (claim C): in a COPY of corpus/SOURCES.md under .ufo/waves/round-66/stage/mut-reg/, (1) swap one new row's status mined -> queued (does ROWS catch?); (2) duplicate one live URL across two new rows with a different query (does LINK catch?); (3) change one teaches cell to a near-copy of the anchor quote (does RESTATE catch?). Per mutant: expected leg + actual leg if you can run the counter against the copy. Write .ufo/waves/round-66/w1/MutRegistry.md.", ["coverage", "operability"]),
    ("RevengerIntent", "revenger",
     "ORIGINAL-INTENT check on the S776 design (claim Ca D1 + claim C): the S753 closure asked for 'a live-resolving anchor or alternate capture'. Does the round's design (live URL now 200 + fresh capture 20261024111013 + S776 supersession row) satisfy the intent, and does S776's used-by pointing at the round-65 games entry (not the new scent entry) stay inside the registry contract? Read corpus/SOURCES.md S753/S776 cells and corpus/knowledge/culture-material/games-play-sport-contests.md. Write .ufo/waves/round-66/w1/RevengerIntent.md.", ["calibration", "coverage"]),
    ("ExecSeparabilityReal", "executor",
     "When reports/round-66/separability-manifest.json exists at integration, run the declared check `python3 -B tools/check-claim-separability.py reports/round-66/separability-manifest.json --jobs 4 --timeout 120 --budget 300` against a COPY of the lane (never the lane's own jj state; use --root on the worktree read-only) and record stdout+stderr verbatim in .ufo/waves/round-66/stage/separability-real-probe.txt. If the manifest is absent or lands are still missing, record the dependency and exit. Do NOT edit lane files.", ["operability"]),
    ("ScribeS776Gate", "scribe",
     "Draft the Gate line for S776 (the S753 supersession row): ' - S776 | <live URL> (capture ts) | 2026-10-24 | \"<the S753 quote, verbatim>\" ' plus a one-line disposition noting the row supersedes S753's unresolvable capture. Write .ufo/waves/round-66/stage/s776-gate.md. Never invent the quote - copy it verbatim from corpus/lessons/round-65.md S753's Gate line.", ["calibration", "coverage"]),
]

for nm, role, body, axes in ATTACK:
    items.append(seat(nm, role, body, axes))

spec = {
    "wave": "kotodama-r66-v2",
    "milestone": "Round 66 single v2 wave (build+attack, 64 seats)",
    "reportDir": ".ufo/waves/round-66/w1",
    "axes": ["coverage", "operability", "calibration", "depth", "freshness", "adjacency"],
    "context": CONTEXT,
    "items": items,
}

import sys
if len(sys.argv) > 1 and sys.argv[1] == "--count":
    from collections import Counter
    print(len(items), Counter(i["role"] for i in items))
else:
    print(json.dumps(spec, indent=1))
