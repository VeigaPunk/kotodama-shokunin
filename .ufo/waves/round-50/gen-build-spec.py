#!/usr/bin/env python3
"""Generate the round-50 build wave spec (kotodama). Run from anywhere."""
import json, pathlib

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-50"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"

CONTEXT = f"""# Goal
Kotodama round 50 attempt1 ONLY (hyaku phase 2). Lane repo {LANE} (branch main, base 4ad26836552462d28a946ca3b067cab0b5ce3532, jj-colocated). Read {LANE}/reports/round-50/claims.json first. Three declared, causally separable claims:
- C coverage: one right-sized (<=~250 lines) entry corpus/knowledge/culture-material/pastoralism-animal-husbandry.md on the verified-fresh pastoralism/animal-husbandry register, to the lane entry contract (model: {LANE}/corpus/knowledge/culture-material/hunting-foraging-subsistence.md and cartography-and-mapmaking.md), citing corpus/SOURCES.md rows opened THIS round (new ids from S048 upward, assigned by L1).
- O operability: make tools/harness/receipt_guard.py and tools/check-readme-revisions.py correct under jj colocation (fleet report /home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/JjAuditKotodama.md risks R1-R3), plus counting probe reports/round-50/jj-colocation-probe.py.
- Ca calibration: tools/check-claim-separability.py + frozen fixture reports/round-50/separability/r49-fixture.json + QUALITY.md criterion 7, from the round-49 outside spot-check {LANE}/corpus/lessons/round-49-verifier-spotcheck.md (REJECTED-HONEST-STOP on separability: claim C cited the SOURCES registry claim S created).
Frontier step (not a claim): SOURCES rows opened this round with URL, access date 2026-10-21 and <=25-word located quote; mined mistake in corpus/lessons/round-50.md.

# Shared contract (Ca)
Separability manifest JSON: {{"schema":"kotodama-separability-manifest-v1","base":"<commit>","claims":[{{"id":"C","tree":"<commit holding this claim's landed bytes>","lands":["repo-relative path",...],"exports":["python regex matching identifiers this claim's landed bytes define, e.g. \\\\bS0(3[1-9]|4[0-3])\\\\b"],"acceptance":["optional argv run in the counterfactual tree"]}}]}}. Tool semantics: for each ordered pair X!=Y, X depends on Y if X's landed bytes (read at X.tree) match any Y export regex or name any Y land path; optional dynamic leg materializes base + X.lands only (others at base bytes) in a temp git-free dir and runs X.acceptance there; exit 0 separable, 1 dependency/acceptance failure (each finding printed as `SEPARABILITY_DEPENDENCY X->Y via <evidence>`), 2 input error. Read-only git (git -C LANE show/cat-file) only.

# Ownership and bounds
L1 (ChousaR27R2) is the sole integration owner and holds the canonical planner seat. Every seat is a leaf: no delegation, no background jobs, no swarms (executors may spawn at most one read-only labrat). Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>; never write under /home/vgpnk/Projects/shokunin/.ufo. Seats write ONLY their own report; executors additionally a private clone at {W}/work/<NAME> (`git clone -q {LANE} {W}/work/<NAME>` then `git -C ... checkout -q 4ad26836552462d28a946ca3b067cab0b5ce3532`) and a patch at {W}/patches/<NAME>.patch (`git -C {W}/work/<NAME> diff` output). NEVER edit production files in {LANE} itself, never run git add/commit/stash/checkout/reset or any mutating jj command in {LANE}, never touch the lane jj state or git index, the fleet repo, sibling lanes, MANIFEST.json, .ufo/state or the watchdog log. Lane selftests that create git repos run only in your clone or a temp dir. No credentials, no live-process probing.

# Sources
External web reading is allowed for source seats (read-only; no logins, no downloads into the lane over 1 MiB). A source counts only if you actually opened it this session: give URL, access date 2026-10-21, a verbatim <=25-word quote with its location (section/page/paragraph), tier per QUALITY criterion 6 ({LANE}/corpus/QUALITY.md: publisher blurbs/abstracts are tier B for claims about a work; A only if primary/authoritative for the exact scope; C is a lead, never sole support), scope, suggested recheck cadence. Never invent a source, quote or page; if a URL fails, say so and stop on that source.

# Tooling
You may install tools that help the task; read /home/vgpnk/.omp/agent/RULES.md first and record tool/version/channel/reason. All pacman transactions are PAUSED host-wide (never -S/-Sy/-Syu/-U/-R, downgrade, or service restart); use uv tool/npx/official binary into ~/.local/bin only if needed, or report the need. Prefer no installs.

# Output
Concise report at your Report path: assigned item, exact file:line or URL evidence, result, unrun checks. Author-lane advice, never admission. Never weaken a test or delete a control to get green."""

items = []
def add(name, role, text, axes=None):
    it = {"name": name, "role": role, "prompt": LEAD + text}
    if axes: it["axes"] = axes
    items.append(it)

# ---------------- executors (code) ----------------
add("ExecGuard", "executor", f"""Claim O, R1+R2. In your clone, change {LANE}/tools/harness/receipt_guard.py (clone copy) so committed-receipt detection probes HEAD's tree AND refs/heads/<branch> AND refs/remotes/origin/<branch> (branch from symbolic-ref when attached, else main; missing refs tolerated) and refuses the overwrite if the path exists in ANY of them; on refusal print the ref that holds it and a separate `landed_sha=` (the branch/remote commit) distinct from the local `head_sha=`, never presenting a local-only HEAD as landed. Keep every existing selftest control (45) byte-identical in name and order; append new controls: (a) detached HEAD at an older commit while main/origin main holds the receipt -> refused exit 3; (b) local unpushed commit ahead of origin -> landed_sha names origin's commit; (c) no remote ref -> still works. Run its --selftest in the clone. Patch at the patches path.""", ["operability"])
add("ExecReadmeRev", "executor", f"""Claim O, R3. In your clone, change tools/check-readme-revisions.py so the pinned BASE_COMMIT control asserts `git cat-file -e <sha>^{{commit}}` and FAILS (nonzero exit, explicit message) when the base object is unreachable, instead of SKIP with exit 0 (see JjAuditKotodama.md R3 and CR:233/CR:306). Provide a test seam (env var or argument naming the LANE/base) so a selftest control proves the unreachable case now fails; keep every existing control name/order. Run --selftest in the clone. Patch at the patches path.""", ["operability"])
add("ExecProbe", "executor", f"""Claim O counting command. Write reports/round-50/jj-colocation-probe.py (in your clone) with `--tools-root DIR` (a tree containing tools/harness/receipt_guard.py and tools/check-readme-revisions.py). It builds synthetic git repos in a temp dir (plain git; `git checkout --detach <older>` reproduces jj's anchored HEAD; use jj only if present AND optional) and evaluates three cases: R1 receipt guard cites a local-only HEAD as the committed/landed sha; R2 guard ALLOWS overwrite of a receipt committed on main/origin main while HEAD is detached below it; R3 check-readme-revisions --selftest exits 0 although its pinned base is unreachable. Print one JSON line per case and final `JJ_COLOCATION_FALSE_NEGATIVES=<n>/3`; exit 0 always on completed measurement, 2 on setup error. It must report 3/3 on base bytes (`git -C {LANE} archive 4ad2683 tools | tar -x -C <tmp>`) — run that and include the output. Never touch the live lane. Patch at the patches path.""", ["operability"])
add("ExecSepTool", "executor", f"""Claim Ca. Write tools/check-claim-separability.py (in your clone) implementing the Shared contract (Ca) exactly, with --selftest containing negative controls (a pair where X cites Y's export -> exit1; X names Y's land path -> exit1; acceptance failing only without Y's lands -> exit1) and positive controls (disjoint claims -> exit0; self-citation not a dependency; malformed manifest -> exit2). Stdlib only, read-only git. Run --selftest. Patch at the patches path.""", ["calibration"])
add("ExecSepFixture", "executor", f"""Claim Ca fixture. Build reports/round-50/separability/r49-fixture.json (in your clone) per the Shared contract (Ca), from round-49 evidence: {LANE}/reports/round-49/claims.json, claims-addendum-kaika.json, run-validation.py, validation.json, and git history (`git -C {LANE} log --oneline -15`, work commits c6a174d and 8c78e6b, base c42d675). Claims C (entry corpus/knowledge/culture-material/hunting-foraging-subsistence.md + README row) and S (corpus/SOURCES.md, its lesson) and Ca (README revision fix + tools/check-readme-revisions.py). Exports: S defines row ids S031-S043 (check exact range in SOURCES.md at 8c78e6b). Also write reports/round-50/separability/r50-manifest.json for round 50 from {LANE}/reports/round-50/claims.json (C/O/Ca lands, base 4ad2683, tree placeholder "WORKTREE" documented). Record every sha you used and how you verified it.""", ["calibration"])
add("ExecRunner", "executor", f"""Measurement runner. Write reports/round-50/run-validation.py (in your clone) that, given --tree DIR (an extracted lane tree) and --base-tree DIR, computes each claim's before/after: C: `find corpus/knowledge -name '*.md' | wc -l`, culture-material count, `python3 -B reports/round-28/readme/sweep.py` result, entry line/H1/H3/topic counts; O: runs reports/round-50/jj-colocation-probe.py --tools-root on both trees; Ca: runs tools/check-claim-separability.py on reports/round-50/separability/r49-fixture.json (expect exit1) and r50-manifest.json and its --selftest, plus `grep -ci separab corpus/QUALITY.md`. Missing files are reported as absent, never crash. Writes JSON to stdout. Study {LANE}/reports/round-49/run-validation.py for the lane's existing shape. Patch at the patches path.""", ["coverage", "operability", "calibration"])

# ---------------- reviewers ----------------
R = [
 ("ReviewGuardSemantics", "Claim O: read tools/harness/receipt_guard.py fully (RG:54-140) and JjAuditKotodama.md R1/R2. Specify the exact correct refusal semantics under detached HEAD, unborn branch, missing origin ref and REFRESH_RECEIPTS=1; list every fail-open path a fix could introduce. Concrete acceptance oracle."),
 ("ReviewGuardControls", "Claim O: enumerate the existing receipt_guard --selftest control names and order (run it in a temp copy, not the lane) so the integrator can prove all 45 survive; output the ordered list and its sha256."),
 ("ReviewReadmeRev", "Claim O: read tools/check-readme-revisions.py; enumerate all controls (run --selftest in a temp copy) and specify how an unreachable BASE_COMMIT must fail closed without breaking existing PASS/FAIL semantics; ordered control list + sha256."),
 ("ReviewProbeDesign", "Claim O: independently design how to reproduce R1, R2, R3 with plain git in a temp dir against base tool bytes (git -C LANE archive 4ad2683 tools). Actually run your minimal reproduction in /tmp and report whether each defect reproduces on base bytes, with exact commands and exits."),
 ("ReviewSepSemantics", "Claim Ca: from corpus/lessons/round-49-verifier-spotcheck.md and reports/round-49/run-validation.py (its c_without_s / s_without_c legs), state precisely what counterfactual the outside verifier required and why the r49 leg failed it; give a test case the new checker must flag."),
 ("ReviewSepFixtureFacts", "Claim Ca: verify the round-49 facts the fixture will freeze: exact commits (c42d675, c6a174d, 8c78e6b, d91c632), which paths each claim landed (git show --stat), the S-id range the r49 entry cites (grep -o 'S0[0-9][0-9]' in the entry at 8c78e6b), and SOURCES rows defined at 8c78e6b. Read-only git only."),
 ("ReviewEntryContract", "Claim C: derive the exact entry contract from corpus/knowledge/culture-material/hunting-foraging-subsistence.md, cartography-and-mapmaking.md, corpus/QUALITY.md and reports/round-28/readme/sweep.py: required head fields in order, heading rules (1 H1, H2 numbering, 0 H3), topic-line rules, line budget, couples/source/verified-at/recheck formats. Output a checklist the integrator can apply mechanically."),
 ("ReviewSourcesContract", "Frontier: read /home/vgpnk/Projects/shokunin/CORPUS.md section 'SOURCES.md — where a shokunin learns' and corpus/SOURCES.md; output the exact row grammar (11 columns), allowed kind/tier/status values, used-by rules, lesson ## Gate format and the census commands; list the next free id and any r49 rows whose used-by would change if the new entry cites them."),
 ("ReviewReadmeIndex", "Claim C: from corpus/README.md, tools/check-readme-heading.py, tools/check-readme-revisions.py and reports/round-28/readme/sweep.py, specify exactly how to add one culture-material row (placement, revision record format, counts to bump 225->226 and 27->28) so all three checks stay green. Run them read-only on a temp copy to confirm current green."),
 ("ReviewLessonsIndex", "Frontier: from corpus/lessons/README.md and reports/round-25/audit/c31-lessons-index-audit.py, specify what a new corpus/lessons/round-50.md requires to keep the audit at findings 0 (index row, revision bump). Run the audit read-only on a temp copy to record current state."),
 ("ReviewR50Separability", "Claims C/O/Ca: attack the declared separability of round 50 in reports/round-50/claims.json. Does C's entry citing SOURCES rows opened by the (non-claim) frontier step repeat the r49 defect? Do O and Ca share any path or identifier? Give a verdict per pair with reasons."),
 ("ReviewQuality7", "Claim Ca: draft-review: propose the exact wording of corpus/QUALITY.md criterion 7 (separability: each claim verifies on base + its own lands only; a claim may not cite identifiers another claim lands) grounded in corpus/lessons/round-49-verifier-spotcheck.md, matching the style of criterion 6. Keep it <= 6 lines."),
]
for n, t in R: add(n, "reviewer", t)

# ---------------- critics ----------------
CR = [
 ("CriticGapPremise", "Claim C: falsify 'pastoralism/animal husbandry is unowned'. Sweep topic lines, H1s, section headings and tables in all six partitions (e.g. linguistics/semantic-fields-lexicon-building.md:70,105; culture-material/agrarian-field-system-lexicon.md:62; fire-fuel-light.md:37; civilizations mongol/turkic/scythian). Distinguish partial owners from cross-references, as the r49 critic did for hunting. Verdict + exact narrowing the claim needs."),
 ("CriticOperability", "Claim O: attack whether fixing receipt_guard/check-readme-revisions under jj is a real operability move or bookkeeping; is the 3/3 -> 0/3 probe circular (written to pass)? Name the evidence that would falsify O."),
 ("CriticCalibration", "Claim Ca: attack whether a static citation scan + optional acceptance rerun is a genuine separability control; construct inputs where it gives false separable / false dependent verdicts (e.g. shared generic ids, path mentions in prose). Required controls list."),
 ("CriticMeasurement", "All claims: attack each counting command in reports/round-50/claims.json for before/after validity, circularity and base-run safety; specify the exact base vs final commands the report must paste."),
 ("CriticFrontier", "Frontier: the mined mistake will be r49's separability rejection with fix = Ca's checker shown to fail on the r49 fixture. Attack whether that satisfies 'a fix counts only once shown able to fail' and whether any other mistake (lessons r42-r49, rejected rounds 36/42/43/44/47) is more pressing. Concrete pointers."),
]
for n, t in CR: add(n, "critic", t)

add("SentinelGuard", "sentinel", "Claim O: adversarial review of the receipt_guard change direction: must never loosen any refusal (REFRESH_RECEIPTS permit, env scrubbing GIT_*, --literal-pathspecs, symlink/out-of-root paths). List invariants the patch must keep and fixtures proving each. Read-only.")

for n, t in [
 ("RevengerR49Runner", "Claim Ca: reverse-engineer reports/round-49/run-validation.py's separability legs (c_without_s, s_without_c): exactly what they removed and checked, and why they passed. Cite lines."),
 ("RevengerGuardIntent", "Claim O: reconstruct receipt_guard.py's original intent and invariants from LOG.md, SCORECARD.md and git log -- tools/harness/receipt_guard.py (read-only). Which callers cite committed_sha? (grep reports/ and tools/)."),
 ("RevengerReadmeRevIntent", "Claim O: reconstruct why tools/check-readme-revisions.py pins BASE_COMMIT c42d675 and what its skip() was meant to tolerate; would fail-closed break any documented workflow? Cite lines and LOG entries."),
]: add(n, "revenger", t)

for n, t in [
 ("ConnectSiblingPastoral", "Claim C sibling-overlap: sweep sibling lanes under /home/vgpnk/Projects/shokunin/*-shokunin (read-only) for entries owning pastoralism/herding/husbandry/transhumance (esp. lore, any history/ecology lanes). Report owners and the handoff boundary kotodama must respect."),
 ("ConnectSiblingSeparability", "Claim Ca: sweep sibling lanes' tools/ and lessons (read-only) for existing claim-separability checkers or counterfactual runners; report reusable patterns and any lane whose rounds were rejected on separability."),
 ("ConnectSiblingJj", "Claim O: sweep sibling lanes and /home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/ (read-only) for receipt guards or pinned-base checks already fixed for jj colocation; report the patterns and their tests."),
]: add(n, "connector", t)

# ---------------- source scouts (C) ----------------
SRC = [
 ("SrcSherratt", "Andrew Sherratt's 'secondary products revolution' (1981/1983): find an openable authoritative page (publisher/DOI landing, Cambridge/Wiley/JSTOR abstract, or a scholarly review) stating the thesis (milk, wool, traction)."),
 ("SrcHerskovits", "Melville Herskovits 1926 'The Cattle Complex in East Africa', American Anthropologist 28: open the DOI/landing page (Wiley AnthroSource) and quote its scope; note later critique if found on the same page."),
 ("SrcEvansPritchard", "E. E. Evans-Pritchard, The Nuer (1940): open a full-text scan (archive.org) and quote a located passage on cattle names/colour terms or cattle as idiom (chapter/page)."),
 ("SrcKhazanov", "Anatoly Khazanov, Nomads and the Outside World (2nd ed. 1994, Univ. of Wisconsin Press): open the publisher page and quote its description of nomad-sedentary interdependence (tier B blurb)."),
 ("SrcBarfield", "Thomas Barfield, The Nomadic Alternative (1993) or The Perilous Frontier (1989): open publisher/library page and quote the scope statement."),
 ("SrcDysonHudson", "Dyson-Hudson & Dyson-Hudson 1980 'Nomadic Pastoralism', Annual Review of Anthropology 9 (doi 10.1146/annurev.an.09.100180.000311): open the landing page and quote the abstract."),
 ("SrcHardin", "Garrett Hardin 1968 'The Tragedy of the Commons', Science 162:1243 (doi 10.1126/science.162.3859.1243): open it and quote the pasture-open-to-all passage (located)."),
 ("SrcOstrom", "Elinor Ostrom, Governing the Commons (1990): open the Cambridge page or Nobel lecture (nobelprize.org 2009) and quote a located passage on common-pool resources/pastures."),
 ("SrcFaoPastoralism", "FAO Pastoralist Knowledge Hub (fao.org/pastoralist-knowledge-hub): open and quote its definition/scope of pastoralism (located)."),
 ("SrcUnescoTranshumance", "UNESCO Intangible Cultural Heritage inscription 'Transhumance, the seasonal droving of livestock' (2019 Austria/Greece/Italy; 2023 extension): open ich.unesco.org element page and quote the description."),
 ("SrcUnescoGer", "UNESCO ICH 'Traditional craftsmanship of the Mongol Ger and its associated customs' (2013): open the element page and quote the located description of mobile dwelling and herding life."),
 ("SrcMongolFiveSnouts", "Mongolian 'five snouts' (tavan khošuu mal: horse, camel, cattle/yak, sheep, goat): find an authoritative openable source (UNESCO, FAO, academic article, national statistics office) and quote it."),
 ("SrcSamiReindeer", "Sámi reindeer herding and earmarks: open an authoritative page (Sámi Parliament of Norway/Sweden, Arctic Council, or Swedish Sámediggi 'renskötsel'/earmark register) and quote a located passage on reindeer husbandry rights or earmarks."),
 ("SrcAndeanCamelids", "Andean camelid pastoralism (llama/alpaca herding): open FAO or a peer-reviewed open-access article and quote a located passage."),
 ("SrcFulani", "Fulani/WoDaaBe transhumance in the Sahel: open FAO/ILRI/peer-reviewed open source and quote a located passage on seasonal mobility."),
 ("SrcPeku", "Proto-Indo-European *peku- 'livestock, wealth' (Latin pecus/pecunia): open an authoritative etymology page (Watkins AHD Indo-European roots appendix, Wiktionary reconstruction page as tier C lead, or Etymonline as tier B/C) and quote it."),
 ("SrcZederDomestication", "Melinda Zeder 2008 PNAS 'Domestication and early agriculture in the Mediterranean Basin' (doi 10.1073/pnas.0801317105) or equivalent: open and quote located passage on sheep/goat/cattle domestication timing."),
 ("SrcBedouin", "Bedouin camel pastoralism: open UNESCO ICH (e.g. 'Al Sadu weaving' or 'Bedouin culture in Petra and Wadi Rum' Proclamation) or academic page; quote located passage tying herding to social life."),
 ("SrcGalatyJohnson", "Galaty & Johnson (eds.) The World of Pastoralism (Guilford 1990) or Salzman 'Pastoralists: Equality, Hierarchy, and the State' (2004): open a publisher/library page; quote scope (tier B)."),
 ("SrcDumuzi", "Sumerian shepherd-god Dumuzi / shepherd-farmer debate: open the Oxford ETCSL text 'The debate between Sheep and Grain' or 'Dumuzid and Enkimdu' and quote a located line (tier A for the text)."),
 ("SrcMaasaiCattle", "Maasai cattle and pastoral society: open UNESCO ICH (e.g. 'Enkipaata, Eunoto and Olng'esherr' 2018) or an authoritative page; quote located passage."),
 ("SrcYak", "Yak pastoralism on the Tibetan plateau: open FAO or a peer-reviewed open-access source and quote located passage on herding mobility/products."),
]
for n, t in SRC:
    add(n, "scout", "Frontier source opening for claim C (pastoralism entry). " + t + " Return a SOURCES candidate: URL, access date 2026-10-21, kind, tier with reason, scope, <=25-word verbatim quote with location, what it teaches the entry (which section), recheck cadence. Open it for real; if unreachable, report the failure and stop.", ["coverage"])

for n, t in [
 ("ScoutCensus", "Frontier: run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (read-only) and the seven manual census commands from /home/vgpnk/Projects/shokunin/CORPUS.md section 'SOURCES.md — where a shokunin learns' against corpus/SOURCES.md; paste outputs and exit codes; rows by tier/status."),
 ("ScoutLaneState", "Recon: report lane state read-only: `scripts/hyaku/jj-lane.sh state {LANE}`, `git -C {LANE} status --porcelain`, jj config `jj --ignore-working-copy -R {LANE} config list --repo`, largest tracked files (>900 KB), .gitignore coverage of .ufo/waves; list hazards for committing round-50 evidence (1 MiB new-file refusal, auto-track none)."),
 ("ScoutMistakeSweep", "Frontier: sweep corpus/lessons/round-4*.md, round-49-verifier-spotcheck.md and SCORECARD rejected rounds (36, 42, 43, 44, 47, 49) for mistakes not yet captured by a QUALITY criterion or gate; list class, pointer, captured-by, candidate fix."),
 ("ScoutCouplings", "Claim C: list the in-corpus entries the pastoralism entry must couple to and cite with exact path:line (agrarian-field-system-lexicon, hunting-foraging-subsistence, fire-fuel-light, cuisine-food-lexicon, transport-mobility-lexicon, trade-economy-lexicon, textile-technology, semantic-fields-lexicon-building, animal-symbolism, sacred-kingship..., civilizations mongol/turkic-steppe/scythian-saka/finnic-sami/inca/dine-navajo/india-tamil-sangam). Give sha256 of each file and the line + what it owns."),
 ("ScoutCalibrationRegistry", "Claim C: read corpus/knowledge/verification/calibration-registry.md and the hunting entry's §13 calibration bank; list the codes and format the pastoralism calibration bank must use, and candidate mainstream/contested/discredited items for pastoralism (e.g. nomadism as an evolutionary stage; Herskovits cattle complex; Hardin's tragedy applied to rangelands)."),
]:
    add(n, "scout", t.replace("{LANE}", LANE))

# ---------------- scribes: entry sections + frontier prose ----------------
SEC = [
 ("ScribeSec01Register", "§1 The register property: pastoralism as an argument about grass, water, animals and mobility (what makes it a distinct production register; herd as living capital)."),
 ("ScribeSec02Boundary", "§2 One-owner boundary table: what this entry owns vs agrarian-field-system-lexicon (agropastoral row), hunting-foraging-subsistence, cuisine-food-lexicon (dairy dishes), transport-mobility-lexicon (pack/riding animals), trade-economy-lexicon, textile-technology (wool), semantic-fields-lexicon-building (pastoral vocabulary field), civilizations entries."),
 ("ScribeSec03Typology", "§3 Pastoral systems typology table: nomadic, semi-nomadic, transhumant (vertical/horizontal), agro-pastoral, enclosed/ranching, with mobility pattern, settlement, labour, risk strategy."),
 ("ScribeSec04Species", "§4 Species and ecology decision table: cattle, sheep/goat, camel, horse, yak, reindeer, llama/alpaca: ecology, products, mobility, labour, symbolic weight."),
 ("ScribeSec05Lexicon", "§5 Herd lexicon design: age/sex/colour/condition/ownership-mark terms (Nuer cattle colour terms; Mongolian five snouts; earmarks; PIE *peku- livestock=wealth); how to build a pastoral vocabulary for a conlang."),
 ("ScribeSec06Products", "§6 Products: meat vs secondary products (milk, wool/hair, traction, dung, blood), dairy processing chain, storage; Sherratt thesis status."),
 ("ScribeSec07Wealth", "§7 Herd as wealth and exchange: bridewealth, loans/stock partnerships, herd-splitting as insurance, raiding economy; cattle-complex critique."),
 ("ScribeSec08Tenure", "§8 Tenure, commons and mobility rights: seasonal routes, wells, pasture rights, Hardin vs Ostrom calibration, enclosure/state sedentarization."),
 ("ScribeSec09Relations", "§9 Pastoral-sedentary relations: interdependence (Khazanov), trade, tribute, conquest states, raiding; avoid 'barbarian' stereotyping."),
 ("ScribeSec10Ritual", "§10 Ritual, myth and symbol of herding: sacrifice economics, shepherd-ruler imagery (Dumuzi; shepherd-king), herd animals in cosmology; handoff to myth-symbol entries."),
 ("ScribeSec11Decision", "§11 Decision table + build order for a fictional pastoral culture (ecology -> species -> mobility -> tenure -> wealth -> lexicon -> ritual), plus error patterns."),
 ("ScribeSec12Example", "§12 NON-CANON worked micro-example (clearly disposable; canon belongs to lore-shokunin): a fictional transhumant highland herding people, 8-12 lines, applying the decision table."),
 ("ScribeSec13Calibration", "§13 Calibration bank: mainstream / contested / discredited items with reasons (nomadism-as-stage discredited; Herskovits cattle complex contested; Hardin's tragedy contested for managed commons; 'pure nomad' myth), formatted like the hunting entry's §13."),
]
for n, t in SEC:
    add(n, "scribe", f"""Claim C: draft section {t} for {LANE}/corpus/knowledge/culture-material/pastoralism-animal-husbandry.md. Match the voice and table-heavy format of {LANE}/corpus/knowledge/culture-material/hunting-foraging-subsistence.md (H2 '## N. Title', no H3, decision tables not essays, calibration flags per corpus/QUALITY.md). Budget 12-20 lines. Cite in-corpus anchors as path:line (verify each line exists) and external sources you ACTUALLY opened this session as [SRC: URL | located <=25-word quote] (placeholders the integrator converts to S-ids). Mark anything you could not verify as (to-verify). Deliver the section text in a fenced block plus a source list (URL, access date 2026-10-21, quote+location, suggested tier).""", ["coverage"])

for n, t in [
 ("ScribeLesson", f"Frontier: draft {LANE}/corpus/lessons/round-50.md skeleton in the lane's lesson style (see corpus/lessons/round-49.md): intake of corpus/lessons/round-49-verifier-spotcheck.md, ## Mistakes table (class · evidence pointer · captured-by · fix) with M1 = r49 claim-separability rejection (fix: tools/check-claim-separability.py shown failing on reports/round-50/separability/r49-fixture.json), ## Gate table placeholder for new S-rows, status/used-by change log section. Deliver text in your report only."),
 ("ScribeSkillRow", f"Claim Ca/O: propose a minimal SKILL.md addition (decision-table row or checklist line) for 'declare claims separably: each claim verifies on base + its own lands; run tools/check-claim-separability.py before dispatch', and one line on jj colocation (cite landed branch sha, never local HEAD). Give exact insertion anchors in {LANE}/SKILL.md."),
 ("ScribeLogEntry", f"Draft the LOG.md round-50 entry skeleton in the style of the latest {LANE}/LOG.md entries (trigger, claims C/O/Ca, frontier, integrator acts, consequence) with placeholders for measured numbers; report only."),
]:
    add(n, "scribe", t)

spec = {
 "wave": "kotodama-r50-build",
 "milestone": "Round 50: C pastoralism entry, O jj-safe gates, Ca separability control",
 "reportDir": ".ufo/waves/round-50/build",
 "axes": ["coverage", "operability", "calibration"],
 "context": CONTEXT,
 "items": items,
}
out = pathlib.Path(W) / "build-spec.json"
out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
from collections import Counter
print(len(items), Counter(i["role"] for i in items))
