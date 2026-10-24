#!/usr/bin/env python3
"""Generate the round-68 single v2 wave spec (64 seats, >=25% attack roles)."""
import json

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "99fae3085ec858446df00c2b294748f635cb6c45"
R68 = ".ufo/waves/round-68"

CONTEXT = """# Goal
Kotodama round 68 (hyaku run 6, 2026-10-24): ONE v2 wave of 64 seats, build+attack together. Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (jj-colocated; base revision 99fae3085ec858446df00c2b294748f635cb6c45). All lane-relative paths below resolve under that repo. Three claims with frozen predicates (reports/round-68/claims.json):
- C (coverage, sourced): new entry corpus/knowledge/culture-material/hair-grooming-codes.md + exactly 24 mined registry rows S833-S856 (tier A/B, opened 2026-10-24, used-by the entry, cited exactly once each). Predicate: ACCEPT-C-68: every leg of reports/round-68/accept-c.py prints PASS.
- O (operability, capability acquisition): tools/check-supersession-settlement.py lands — classifies every `supersedes` registry chain (pending / settled-active / settled-retired / settled-closed / settled-split), resolves used-by paths, validates the committed disposition ledger reports/round-68/dispositions/dedup-ledger.tsv (0 findings, frozen id coverage). At the settlement lands revision the scan prints pending=0, missing_paths=0, selftest 7/7. Predicate: ACCEPT-O-68: every leg of reports/round-68/accept-o.py prints PASS.
- Ca (calibration, records): r67-routed defects dispositioned — R67-D1 (26 uncommitted .ufo/waves/ leftovers incl. the ~178 MiB fabric-c clone: physically deleted, frozen path list at reports/round-68/dispositions/r67-d1-paths.txt); R67-D2 (28 census W04 duplicate-URL warnings -> ledger rulings for every flagged id + every chain s-id, census exits 0 W04-free). Plus the sequencing protocol re-proven (SEQ legs, FIXTURES base-stamp controls) and the lesson Gate (>=20 located quotes S833-S860). Predicate: ACCEPT-CA-68: every leg of reports/round-68/accept-ca.py prints PASS.
RECEIPT DISCIPLINE (r67 protocol, kept): every r68 counter takes a REQUIRED --lands <40hex>; receipt records stamped + evaluated + measured revisions + tree + counter sha256; STAMP fails unless evaluated == stamped. Counters run inside a materialized clone at the lands commit, never a moved worktree. Carrier-parentage is post-records evidence only (check-receipt-seq.py --topo).
THE SETTLEMENT MODEL (claim O, the round's center): the registry is append-only — a `supersedes S###` row is a correction; a chain is PENDING while the superseding row is not rejected, the target is not rejected, and the pair is not in a settled state. 34 chains are pending at base (see claims.json frozen_sets.CHAIN_PAIRS). Settlement lands in ONE commit A_r: (a) dedup-ledger.tsv gains one row per flagged id + per chain s-id + per settled s-id with a ruling in {activate, retire, keep-successor, keep-reject, keep-split}; (b) activate = superseding row status mined + used-by set, target status queued + used-by cleared, and every (t) citation in corpus/knowledge re-pointed to (s) — sentence fixes allowed only where the locator can't carry; (c) retire = superseding row status rejected with REJECTED:/flip: teaches, target unchanged; (d) keep rulings mutate nothing. In-place edits: only status/recheck/used-by cells of the 68 frozen MUTABLE ids. Entry re-points confined to the 7 frozen EDITABLE_ENTRIES files.
Frozen counters, claims.json, base dry-run evidence and the tool are on disk at the lane tip — read them before attacking. Build seats: your output is a draft under .ufo/waves/round-68/ — the L1 reviews, integrates and is the only committer. Attack seats: try to break the frozen instruments and drafts — shortcut classes, bypasses, stale receipts, false stamps, moved-worktree PASS claims, fabricated anchors, wrong rulings; name what you attack.

# Rules (bind every seat)
Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
Leaf member — no subagent dispatch, no swarm of your own. Absolute paths for writes, under /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-68/ only, at the exact paths your item names. Never mutate the fleet repo, sibling lanes, lane jj state or the lane Git index; never run git/jj writes; read-only git is fine; do not commit — the L1 integrates.
Tooling authorization (operator, 2026-10-19): you may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record tool/version/channel/reason in your report). pacman guard (orchestrator ruling 2026-10-20, in force): all pacman transactions are PAUSED host-wide — install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R/downgrade.
Report: write your scoped findings to /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-68/w1/<SEAT>.md (the validator renders every `Report:` trailer relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin — write it at that absolute path)."""

RULES = """Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
"""

ENTRY = "corpus/knowledge/culture-material/hair-grooming-codes.md"

ROW_TOPICS = [
    ("S833", "Ancient Egyptian wigs, hairpieces and shaving practice — museum collection object or scholarly source (British Museum, Met, Egyptological)"),
    ("S834", "Roman hairstyling and the ornatrix / calamistrum — scholarly or museum source (curling irons, bust hairstyles, Ovid)"),
    ("S835", "Chinese queue/bianzi and the Manchu hair order — scholarly source on the tonsure decree and its resistance"),
    ("S836", "Japanese topknots (chonmage) and Edo-era hair rules — museum or scholarly source"),
    ("S837", "Indigenous North American hair regimes — scalplock, roach, braids; tribal museum or scholarly source"),
    ("S838", "West African braiding and hair as social text — scholarly source on braiding patterns, status, age-grade"),
    ("S839", "Himba ochre hair and pastoralist grooming — scholarly or museum source (otjize, hair sculpting)"),
    ("S840", "Sikh kesh and the turban as article of faith — Sikh scholarly or institutional source"),
    ("S841", "Muslim grooming jurisprudence — beard, mustache, miswak; scholarly source on hadith grooming codes"),
    ("S842", "Medieval European barber guilds and barber-surgeons — museum or scholarly source"),
    ("S843", "Tonsure in Christian monasticism — scholarly source on the three tonsure forms and their meaning"),
    ("S844", "Sumptuary laws on hair and headwear in early modern Europe — scholarly source"),
    ("S845", "Victorian hairwork, mourning jewelry and hair wreaths — museum collection source (V&A, Met, Memento Mori)"),
    ("S846", "The powdered wig and 18th-century European court hair — museum or scholarly source"),
    ("S847", "African-American hair politics — straightening, natural hair, CROWN Act; scholarly or institutional source"),
    ("S848", "Military grooming standards — armies and regulation haircuts; institutional or scholarly source"),
    ("S849", "Māori and Pacific hair/head tapu — scholarly source on head sanctity, hair-cutting rites"),
    ("S850", "Indian hair practices — shikha, mundan, temple hair donation (Tirupati); scholarly or institutional source"),
    ("S851", "Brazilian/Latin American hair economies — human-hair trade and extension markets; scholarly source"),
    ("S852", "Early modern Japanese/European wig trades and wigmakers' guilds — scholarly or museum source"),
    ("S853", "Romani/traveller and Eastern European hair customs — scholarly source"),
    ("S854", "Beard codes in religious orders — Orthodox clergy, monks, Rastafari locks; scholarly source"),
    ("S855", "20th-century hair as political sign — bobbed hair, punk mohawks, skinhead; scholarly source"),
    ("S856", "Hair and gender regulation in school/prison/military institutions — scholarly source"),
]

ROW_MODEL = """Per row write .ufo/waves/round-68/rows/<SEAT>/row-<SID>.txt with exactly these labelled lines:
ROW=| <SID> | <source name> - <live URL> ; https://web.archive.org/web/<14-digit ts>id_/<original URL> . | <kind> | <A or B only> | <scope <=60 chars> | "<anchor quote 8-25 body words>" | <teaches cell <=240 chars> | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/hair-grooming-codes.md |
BULLET=<one clause: 6-25 content words, >=3 in-order content words from the quote, no run >12 words copied from the quote, >=1 novel content word, NOT a near-copy of the teaches cell (word-token coverage <80% in-order)>
VERIFY=<live curl status + date; quote in body text Y/N; access limits>
CAPTURE=<wayback ts + original URL; original query-aware-normalizes equal to the live URL>
ACCESS=<redirects, rate limits, paywalls a re-opener needs>
Rejects go to rows/<SEAT>/rejects.txt as <URL> - <reason>; flip: <what would change it>. The live URL must be unique: grep it against corpus/SOURCES.md and all fragments. Sources: tier A/B only (peer-reviewed, official bodies, museum/university, scholarly books). Verify everything yourself with curl."""

CHAIN_SETS = {
    "AuditChain1": ["S044", "S045", "S046", "S070", "S125"],
    "AuditChain2": ["S126", "S133", "S186", "S358"],
    "AuditChain3": ["S127", "S128", "S129", "S130", "S131"],
    "AuditChain4": ["S481", "S482", "S483", "S484", "S485"],
    "AuditChain5": ["S486", "S487", "S488", "S489", "S490"],
    "AuditChain6": ["S491", "S560", "S561", "S562"],
    "AuditChain7": ["S564", "S565", "S566"],
    "AuditChain8": ["S567", "S568", "S569"],
}

AUDIT_MODEL = """For each assigned s-id the chain is s>t (claims.json CHAIN_PAIRS). Read the s row and t row in corpus/SOURCES.md, the t's `used-by` entries, and every `(t)` citation in corpus/knowledge (grep -rn 'S0NN'). Re-open the s URL if needed (curl + wayback). Decide the ruling:
- activate: the s row's fix is sound and its anchor covers every citing locator of t -> ledger row `s | t | <live url> | activate | repoint | <entry files re-pointed> | <one-line basis>`; list every citation site as `CITE=<file>:<line> (t…) -> (s…)` including locator notes where an anchor can't carry a page number.
- retire: the correction is wrong or unsupported -> `s | t | <live url> | retire | none | corpus/SOURCES.md | <reason>; flip: <what would activate it>` and the s row becomes rejected with REJECTED:/flip: teaches (the L1 writes the flip text from your reason).
- keep-* is the L1's class for already-settled chains, not yours.
Write .ufo/waves/round-68/rows/<SEAT>/audit.md: one `RULING=` line per s-id plus CITE=/EVIDENCE=/ANCHOR= lines. You do NOT edit registry or entries — drafts only; the L1 integrates all rulings in one commit."""

def seat(name, role, prompt, axes):
    return {"name": name, "role": role, "axes": axes, "milestone": "r68-v2",
            "prompt": RULES + prompt}


items = []

# ---- build: gap + rows ----
items.append(seat("ScoutGapHair", "scout",
    "Verify the claim-C gap at the base, then write .ufo/waves/round-68/rows/ScoutGapHair/gap.md with exact commands+outputs:\n"
    "1) cd " + LANE + " && git ls-tree -r --name-only " + BASE + " -- corpus/knowledge | grep -ciE '(^|[^a-z])(hair|tonsur|braid|queue|locks|wig|barber|grooming|beard|scalp|coiffure|moustache|shave|coif)([^a-z]|$)'  (expect 0)\n"
    "2) grep -rniE '^-?\\s*topic\\s*:.*(hair|tonsure|braid|wig|barber|grooming|beard|scalp|coiffure|moustache|shave)' corpus/knowledge/  (list every topic-line owner; expect only partial-scope mentions — adornment-body-codes' hair politics, headgear, costume-semiotics)\n"
    "3) sibling ownership: grep -rliE 'hair|grooming|barber' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5\n"
    "End gap.md with a 5-line build order for the entry: register map; source-grounded bullets by class (hair regimes by culture, faith/ritual grooming, institutions of control, trades and economies, politics of hair); design protocol; calibration; one-way pointing to partial owners; lore handoff.",
    ["coverage", "adjacency"]))

for i in range(0, len(ROW_TOPICS), 2):
    pair = ROW_TOPICS[i:i + 2]
    seat_name = "ScoutRow%02d" % (i // 2 + 1)
    ids = ", ".join(s for s, _ in pair)
    topics = " AND ".join(t for _, t in pair)
    task = ("ROW-OPENING item (claim C): open exactly two registry rows, " + ids
            + ", for the hair/grooming register. Topics: " + topics + ".\n\n"
            + ROW_MODEL)
    items.append(seat(seat_name, "scout", task, ["coverage"]))

items.append(seat("ScoutReject1", "scout",
    "REJECT-CANDIDATE item (claim C gate): find two candidate hair/grooming sources that a gate SHOULD reject and produce first-class rejected registry rows for them. Write .ufo/waves/round-68/rows/ScoutReject1/row-S857.txt and row-S858.txt in the same ROW= shape but with status cell 'rejected', teaches cell 'REJECTED: <reason>; flip: <what would change the verdict>' (<=240 chars), opened 2026-10-24, used-by '—'. Candidate reject classes: a paywalled/JS-walled source a plain curl cannot open; a source whose only quotable text is a caption/alt-text; a duplicate of an existing row's live URL; a scope that belongs to a sibling lane (lore canon, chousa method); community/tier-C material that cannot support an admitted entry. Full VERIFY/CAPTURE/ACCESS evidence required.",
    ["coverage", "calibration"]))

items.append(seat("ScoutReject2", "scout",
    "Same contract as ScoutReject1 but disjoint candidates — write rows/ScoutReject2/row-S859.txt and row-S860.txt (temporary ids S859/S860 — the L1 renumbers to the S857-S858 band only if accepted; if Reject1's are accepted these become documented alternates or are dropped by the L1). Prefer different reject classes than ScoutReject1 targets. Full VERIFY/CAPTURE/ACCESS evidence required.",
    ["coverage", "calibration"]))

# ---- build: settlement audits ----
for name, sids in CHAIN_SETS.items():
    items.append(seat(name, "reviewer",
        "CHAIN AUDIT item (claim O execution): rule on these pending supersedes chains: "
        + ", ".join(sids) + ".\n" + AUDIT_MODEL,
        ["operability"]))


# ---- build: scribes ----
items.append(seat("ScribeEntrySpec", "scribe",
    "Draft the claim-C entry design at .ufo/waves/round-68/stage/entry-spec.md (not the entry itself): section plan for " + ENTRY + " following the lane's entry conventions (read corpus/knowledge/culture-material/headgear-head-covering-codes.md and adornment-body-codes.md first): register map, hair-as-code classes (hair regimes by culture, faith/ritual grooming, institutional control, trades and economies, hair politics), a Boundaries section one-way pointing to partial owners (adornment-body-codes hair politics, headgear-head-covering-codes, costume-semiotics, ritual-garments), a lore handoff section (one-way, never canon), and a bullet template row S### -> clause. Read row fragments under .ufo/waves/round-68/rows/ScoutRow*/ as they appear; leave exact bullet text to integration.",
    ["coverage", "depth"]))
items.append(seat("ScribeGateRows", "scribe",
    "Draft the lesson ## Gate rows at .ufo/waves/round-68/stage/gate-rows.md: one line per opened row S833-S856 (URL | 2026-10-24 | <=25-word located quote) using each fragment's own anchor quote verbatim once fragments exist; for absent fragments leave the S-id line marked MISSING. Also draft the rejected-row Gate lines for S857-S858 with reason+flip from the row files.",
    ["coverage"]))
items.append(seat("ScribeLessonPlan", "scribe",
    "Draft corpus/lessons/round-68.md skeleton at .ufo/waves/round-68/stage/lesson-plan.md in the lane's lesson shape (read corpus/lessons/round-67.md): Round summary naming the three claims + R67-D1/D2 dispositions; ## Gate; ## Mistakes with placeholder rows for mistakes discovered this round (R68-M#) and the settlement-model class (the append-only correction chain settled: 34 pending -> 0); a frontier note naming the AuditStale census outcome and remaining queued-row debt.",
    ["calibration"]))
items.append(seat("ScribeReadmePlan", "scribe",
    "Draft the corpus/README.md revision text at .ufo/waves/round-68/stage/readme-revision.txt: a `revision: 2.20` block in the house voice (read the 2.19 block) naming hair-grooming-codes.md, its filing position (filename order between headgear-head-covering-codes.md and hunting-foraging-subsistence.md), culture-material 34 -> 35, totals 241 -> 242, and the registry row-count delta (756 -> 756+24+2+any supersedes-appends). Include the exact index row line `- corpus/knowledge/culture-material/hair-grooming-codes.md — <topic verbatim>` with the topic placeholder.",
    ["coverage"]))
items.append(seat("ScribeR68LogEntry", "scribe",
    "Draft the LOG.md '## Round 68' entry at .ufo/waves/round-68/stage/log-r68.md in the lane's LOG voice (read the round-67 entry): base 99fae308; claims C (hair entry + 24 rows S833-S856), O (supersession-settlement checker + 34-chain settlement), Ca (R67-D1/D2 dispositions + sequencing proof); 64-seat v2 wave; expected verdict rows to be filled by the L1 with the real lands hash + receipts. Mark every number the L1 must verify.",
    ["calibration"]))
items.append(seat("ScribeR68Scorecard", "scribe",
    "Draft the SCORECARD.md '## Axes — round 68' table at .ufo/waves/round-68/stage/scorecard-r68.md in the house shape (read the round-67 table): coverage improved (claim C pending receipts), operability improved (claim O), calibration improved (Ca dispositions + sequencing), depth/freshness/adjacency unchanged; evidence pointers to reports/round-68/telemetry/; honest placeholders for verdicts the L1 fills from real receipts.",
    ["calibration"]))

# ---- build: executors ----
items.append(seat("ExecSweepD1", "executor",
    "R67-D1 execution probe (claim Ca): read reports/round-68/dispositions/r67-d1-paths.txt (26 frozen paths). Verify on disk: each path exists now, is under .ufo/waves/round-66 or round-67, is untracked (`git status --porcelain`), and du -sm each top-level leftover (.ufo/waves/round-66, round-67) — fabric-c expected ~178 MiB. Then predict: after `rm -rf` of the 26, `git status --porcelain` shows zero .ufo/waves/{66,67} entries and reports/round-68 is the only new untracked dir. Do NOT delete anything — write .ufo/waves/round-68/w1/ExecSweepD1.md with the census + prediction + the exact rm command for the L1.",
    ["operability"]))
items.append(seat("ExecCounterSmoke", "executor",
    "Smoke-test the three frozen counters at .ufo/waves/round-68/w1/ExecCounterSmoke.md: run each at base (`python3 -B reports/round-68/accept-{c,o,ca}.py --root . --lands " + BASE + "`) and inside a base-materialized clone (`git clone --no-local --single-branch --branch main . .scratch/smoke`); report which legs FAIL at base (expected: O's DIFF/SHA/PENDING/LEDGER/EXEC/TOPO; C's FILE/SET/ONEID/RESTATE/HOSTS/DECITED; Ca's D1/D2/D4/R68/FIXTURES) and whether any fail for the wrong reason (crash). Also run `python3 -B tools/check-supersession-settlement.py --scan` and paste its summary.",
    ["operability"]))
items.append(seat("ExecSeparabilityReal", "executor",
    "Build and run the round-68 separability manifest: read reports/round-68/claims.json lands arrays and tools/check-claim-separability.py --help, then write .ufo/waves/round-68/stage/separability-manifest.json (schema kotodama-separability-manifest-v1, copy reports/round-67/telemetry/separability-manifest.json shape) and run `python3 -B tools/check-claim-separability.py --manifest <manifest> --jobs 4 --budget 240` on the lane. Report the complete verdict + findings at .ufo/waves/round-68/w1/ExecSeparabilityReal.md; name expected record-dependency findings (Ca->C/O counters, Ca->REC lands) vs any unexpected coupling.",
    ["operability"]))

# ---- connector / sentinel / revenger ----
items.append(seat("ConnectorSiblings", "connector",
    "Sibling-overlap scan for the hair/grooming register + the settlement tool: grep the fleet root /home/vgpnk/Projects/shokunin/*/corpus and PROVINCE.md for hair/grooming/barber ownership; check chousa-shokunin/tools/ for prior art on registry/settlement checkers. Write .ufo/waves/round-68/w1/ConnectorSiblings.md naming the nearest partial owners (adornment-body-codes, headgear-head-covering-codes, costume-semiotics), the one-way handoff rules, and whether any sibling owns a supersedes/settlement checker (adjacency input).",
    ["adjacency", "coverage"]))
items.append(seat("SentinelScope", "sentinel",
    "Scope/security review of tools/check-supersession-settlement.py and the three counters: the tool must never mutate the repo (audit every subprocess/os call), never act outside --root, never touch network; check the counters for path escapes (ledger/entry args naming ../..), shell=True, eval. Confirm the wave's no-write rules are honored by the seats' own designs. Write .ufo/waves/round-68/w1/SentinelScope.md listing violations or a clean bill with the audited call list.",
    ["operability", "calibration"]))
items.append(seat("RevengerSettleModel", "revenger",
    "Reverse-engineer the settlement debt's origin from committed bytes only: pick 5 chains spanning the debt (S044>S034 from round 49, S133>S097, S490>S379, S560>S413, S569>S453). For each: `git log` the registry row and the teaches cell, name the round that opened the superseding row and the round that last touched the target, and reconstruct why the chain stayed pending (was re-pointing planned? was the queue the intended resting state?). Write .ufo/waves/round-68/w1/RevengerSettleModel.md with per-chain chronologies and one verdict: is 'pending = unfinished debt' the right model, or did the lane intend queued-as-correction (a different settlement semantics the tool should also report)?",
    ["calibration", "operability"]))

# ---- attack seats ----
CRITICS = [
    ("CriticClaims", "Attack claims.json itself: ambiguity in 'register unowned' (the census pattern — can hair-grooming-codes.md sneak past a wider pattern?); 'exactly 24 rows' vs appended supersedes/reject rows (can smuggled ids pass SET/APPEND?); whether the MUTABLE/EDITABLE frozen sets leak (can an unrelated row ride the mutable set?); predicate sentence vs counter code drift. Write .ufo/waves/round-68/w1/CriticClaims.md."),
    ("CriticPreC", "Pre-data attack on reports/round-68/accept-c.py: run it at base + wrong --lands; try fabricable NEW_ID rows (queued status, tier C, wrong opened date, used-by another file); dup live URLs with query/fragment variants; abuse the MUTABLE allowance (can a mutable id's teaches cell ride a status flip? — check append_check's cell allowlist); APPEND supersedes-append hole (can a forged `supersedes S900` row land?). Write .ufo/waves/round-68/w1/CriticPreC.md."),
    ("CriticPreO", "Pre-data attack on reports/round-68/accept-o.py + tools/check-supersession-settlement.py: can a chain be hidden from SUP_RE (teaches phrasing `supersedes  S001`, case variants, `supersede`)?; can a pending chain pass SETTLED-SPLIT with a fake limiter phrase?; used-by a path that exists but never cites; ledger ruling 'activate' on a queued s (validate_ledger must flag); --scan exit code on malformed rows (11-cell violations). Write .ufo/waves/round-68/w1/CriticPreO.md."),
    ("CriticPreCa", "Pre-data attack on reports/round-68/accept-ca.py: D1 — does the path-list check prove CONTENT (a still-present path under a different name?); D2 — can the ledger list a valid ruling that's semantically wrong (the leg is shape-only); R68 — 'still_queued' vs keep-split gap; FIXTURES — base-stamp fails for the right reason (STAMP leg, not crash); SEQ greps spoofable strings. Write .ufo/waves/round-68/w1/CriticPreCa.md."),
    ("CriticSizing", "Claim sizing attack: is 24 rows the right batch or padding (vs r66's 22, r67's 24)?; is the settlement claim O-sized (a tool + 34 rulings in one round — is that one claim or three?); are 3 claims separable (Ca R68 leg reads the same registry state claim O settles — record-dependency or real coupling?). Write .ufo/waves/round-68/w1/CriticSizing.md."),
    ("CriticRegistry", "Registry attack: in-place cell mutation (status queued->mined, used-by —->path) — does the ledger/tool verify the flip is CONSISTENT with the ruling (activate but status still queued = fail?); can the mutable set be abused to de-mine an unrelated row; row ordering (appends at file tail vs sorted); the S575 settled-split carveout — can a fake limiter phrase park a chain forever. Write .ufo/waves/round-68/w1/CriticRegistry.md."),
    ("CriticSettlementModel", "Settlement-model attack: the activate/repoint mechanics — for a t cited 5x with page locators (S410 p.3/p.8/p.9), can a swap to s falsify a claim (s's anchor covers only one page)? Enumerate the chains where re-pointing needs locator review vs clean swaps; is `retire` ever the wrong answer when the entry depends on the t claim (S105's ASL-lineage fact vs S126's classification frame — is S126 a real superset?). Write .ufo/waves/round-68/w1/CriticSettlementModel.md."),
    ("CriticW04Coverage", "D2 coverage attack: the frozen W04 set — is it exactly the census's flagged ids (re-run sources-census.sh validate and diff the W04 list vs claims.json W04_FLAGGED)?; can a duplicate URL exist that the census misses (query/fragment variants, http-vs-https, host case); is `0 W04 lines` achievable without touching the dedup mechanics (what if W04s persist on the settled side)? Write .ufo/waves/round-68/w1/CriticW04Coverage.md."),
    ("CriticSweep", "Sweep-debt attack: the 26-path list — is it complete (git status --porcelain vs r67-d1-paths.txt); does deletion break anything (scripts reading .ufo/waves/round-66 artifacts? counters referencing them?); is `rm -rf` the right disposition vs gitignore (the brief allowed either — defend the choice); does reports/round-68 get swept accidentally. Write .ufo/waves/round-68/w1/CriticSweep.md."),
    ("CriticEntryBoundary", "Domain attack: the hair/grooming register — name every partial-scope neighbor the entry must point to one-way (adornment-body-codes hair politics column, headgear-head-covering-codes, costume-semiotics, ritual-garments, bathing-and-body-hygiene); which of the 24 row topics duplicate owned registers (S840 kesh vs adornment's Khalsa kesh mention? S845 mourning hair vs funerary?); flag rows that should have been rejects. Write .ufo/waves/round-68/w1/CriticEntryBoundary.md."),
    ("CriticLedgerSemantics", "Ledger-semantics attack: the `related` column — for a retire ruling, does DECITED block s citations or t citations (read the code); can a `keep-split` ruling hide an activated chain; does validate_ledger check mechanism/evidence consistency at all (shape-only = weakest leg, name the exploit); can two rulings on one id be smuggled (dup_id check). Write .ufo/waves/round-68/w1/CriticLedgerSemantics.md."),
]
for name, prompt in CRITICS:
    items.append(seat(name, "critic", prompt, ["calibration"]))

REVIEWERS = [
    ("RevCounterC", "Review reports/round-68/accept-c.py line-by-line against claims.json legs: every declared leg implemented; APPEND mutable-cell allowlist vs the frozen MUTABLE set byte-exact; DIFFSET ALLOWED_ENTRY list; DECITED ledger-parse direction (activate blocks t citations, retire blocks s — verify); EXEC world arithmetic (4 fixture checks). Write .ufo/waves/round-68/w1/RevCounterC.md."),
    ("RevCounterO", "Review reports/round-68/accept-o.py line-by-line: MUTANTS map vs make_mutants anchors byte-exact (does each replace() actually hit?); fixture_lane builds pending-at-base?; EXEC checks fail-at-base pass-at-lands on the COUNTER's own logic (run_pending reused, not the tool's); SHA leg compares live vs lands blob; TOPO --declaration binding. Write .ufo/waves/round-68/w1/RevCounterO.md."),
    ("RevCounterCa", "Review reports/round-68/accept-ca.py line-by-line: D1 path-list check (existence only — durable?); D2 W04-grep and DEDUP_IDS+PENDING_S coverage vs claims.json frozen sets byte-exact; R68 queued-consistency (any ruling that leaves queued = fail — is keep-split needed?); FIXTURES runs counters with --lands BASE — does STAMP fail or crash; SEQ grep strings present in all three counters. Write .ufo/waves/round-68/w1/RevCounterCa.md."),
    ("RevToolSettle", "Review tools/check-supersession-settlement.py: the classify() order (closed > retired > active > split > pending — can a chain satisfy two classes, which wins?); SUP_RE misses `supersedes S01` two-digit?; SPLIT_RE false-positives; usedby_paths cell parsing; validate_ledger consistency rules (activate->mined, retire->rejected, keep-reject->rejected — keep-successor/keep-split unconstrained?); selftest covers all classes. Write .ufo/waves/round-68/w1/RevToolSettle.md."),
    ("RevBaseCensus", "Independent base census: re-run the claim-C ownership census at base with a DIFFERENT pattern (wider: hair|groom|barber|braid|wig|tonsure|beard|moustache|scalp|coif|shave|lock|queue|tress|plait|dreadlock|kesh|chignon|topknot|queue); report any whole-register filename hit; also topic-line sweep. If a hit exists the claim statement is false — say so loudly. Write .ufo/waves/round-68/w1/RevBaseCensus.md."),
    ("RevAuditFidelity", "Audit-fidelity review: for each AuditChain* report under .ufo/waves/round-68/rows/, check the ruling has basis (evidence lines, citation sites enumerated, anchor coverage argued); spot-check 5 rulings by re-fetching the s source; flag rulings whose mechanism doesn't match the ledger row (activate without CITE= sites; retire without a flip reason). Write .ufo/waves/round-68/w1/RevAuditFidelity.md."),
    ("RevIntegrity", "Integration-risk review: which claim bytes could land outside counters' view — S859+ ids sneaking into the claim set, row files under rows/ not matching final registry lines (ROW= drift), ledger rulings silently dropped at integration, entry bullets citing wrong ids; how would the counter catch each. Write .ufo/waves/round-68/w1/RevIntegrity.md."),
    ("RevLoreHandoff", "Adjacency review: the hair entry's lore handoff — which sections must be one-way (deity/canon claims, real-world rights on religious grooming); nearest boundary bullets the entry needs (name them by file+section); does hair-grooming step on adornment-body-codes' hair column (one-way point, never absorb). Write .ufo/waves/round-68/w1/RevLoreHandoff.md."),
    ("RevWaveShape", "Round-shape review: does this wave meet the v2 band (64 seats, >=25% attack: count the roles); §3 minimum role split met inside it (planner=L1, 1 connector+, 3 executor+, 1 scribe+, 1 scout+, 1 reviewer+, 1 critic+); flag any padding (seats without a concrete item). Write .ufo/waves/round-68/w1/RevWaveShape.md."),
    ("RevEntrySpec", "Review .ufo/waves/round-68/stage/entry-spec.md + row fragments for the 24 topics: which topics overlap owned registers (S840 kesh, S845 mourning hair, S847 hair politics vs adornment); which bullets likely fail RESTATE; report row-fragment defects (malformed ROW=, quote >25 words, wrong id, tier C). Write .ufo/waves/round-68/w1/RevEntrySpec.md."),
    ("RevSourceSupport1", "Blind-support review rows S833-S844: for each, open the row fragment, re-fetch live URL + capture, verify the anchor quote in body text, judge whether teaches is actually supported. One verdict per id with evidence. Write .ufo/waves/round-68/w1/RevSourceSupport1.md."),
    ("RevSourceSupport2", "Same contract for S845-S856. Write .ufo/waves/round-68/w1/RevSourceSupport2.md."),
    ("RevLedger68", "Verify the drafted dedup-ledger.tsv once written: every required id present exactly once (28 flagged + 34 chain s + 13 keep s = 75 rows); ruling consistent with the audit evidence; mechanism names the real settlement step; the tool's --ledger exits 0 on the draft. Write .ufo/waves/round-68/w1/RevLedger68.md."),
    ("RevEntryDiff", "Post-repoint review: after the L1's settlement lands, diff each of the 7 editable entries — every removed (t) citation has a sound (s) replacement in context (no dangling sentence, no claim now supported by a wrong-scope source); flag any re-point that needs a sentence fix the audit missed. Write .ufo/waves/round-68/w1/RevEntryDiff.md."),
    ("RevRejects", "Review the reject candidates (rows/ScoutReject*/): are the reject reasons real and checkable (re-run the curl); does each teaches carry REJECTED:+flip; are S857-S858 the two strongest candidates. Write .ufo/waves/round-68/w1/RevRejects.md."),
]
for name, prompt in REVIEWERS:
    items.append(seat(name, "reviewer", prompt, ["calibration"]))

# ---- mutation testers ----
items.append(seat("MutCounterC", "mutation-tester",
    "Byte-mutate reports/round-68/accept-c.py at .ufo/waves/round-68/stage/mut-c/: produce 4-6 mutants each breaking one leg (ONEID >=1 instead of ==1; RESTATE inq<2; APPEND mutable set emptied or MUTABLE_CELLS widened to all cells; DECITED skipped; DIFFSET allowlist emptied). For each, run the mutant on a base clone + describe expected vs actual verdict — a mutant that changes nothing is a failed mutation (report it). Do NOT touch the real counter. Write .ufo/waves/round-68/w1/MutCounterC.md with mutant names, diffs, verdicts; commit mutant files under stage/mut-c/.",
    ["operability", "calibration"]))
items.append(seat("MutToolSettle", "mutation-tester",
    "Byte-mutate tools/check-supersession-settlement.py at .ufo/waves/round-68/stage/mut-o/: 4-6 mutants (SUP_RE single-digit capture; classify() swapped active/pending; SPLIT_RE always-match; ledger ruling set emptied; usedby_paths returns []). Run each mutant's --scan on the live lane and --selftest; a mutant whose --selftest still prints 7/7 is a coverage gap in the selftest — report it loudly. Write .ufo/waves/round-68/w1/MutToolSettle.md with diffs + verdicts.",
    ["operability"]))
items.append(seat("MutEntryClass", "mutation-tester",
    "Mutation-test the claim-C entry class: write .ufo/waves/round-68/stage/mut-entry/ variants of a minimal fake entry (missing - topic:, h3 present, 251 lines, bullet citing foreign S-id, foreign bullet with no citation) — predict which legs catch each, then run accept-c.py against a fixture registry+entry in a temp dir (never mutate real files); report at .ufo/waves/round-68/w1/MutEntryClass.md which mutants PASS the counter unexpectedly (gaps to route to r69).",
    ["coverage", "calibration"]))

spec = {
    "wave": "kotodama-r68-v2",
    "milestone": "Round 68 single v2 wave (build+attack, 64 seats)",
    "reportDir": ".ufo/waves/round-68/w1",
    "axes": ["coverage", "operability", "calibration", "depth",
             "freshness", "adjacency"],
    "context": CONTEXT,
    "items": items,
}

ATTACK = {"reviewer", "critic", "mutation-tester", "sentinel"}
n_attack = sum(1 for i in items if i["role"] in ATTACK)
print(f"# seats={len(items)} attack={n_attack} ({n_attack/len(items):.1%})")
with open(".ufo/waves/round-68/spec-v2.json", "w") as fh:
    json.dump(spec, fh, indent=1)
print("wrote .ufo/waves/round-68/spec-v2.json")
