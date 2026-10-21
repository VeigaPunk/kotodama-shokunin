#!/usr/bin/env python3
"""Generate the round-50 falsify wave spec (kotodama). Every item names what it attacks."""
import json, pathlib

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-50"
LANDED = "1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0"
BASE = "4ad26836552462d28a946ca3b067cab0b5ce3532"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
ENTRY = "corpus/knowledge/culture-material/pastoralism-animal-husbandry.md"

CONTEXT = f"""# Goal
Kotodama round 50 attempt1 ONLY — FALSIFY wave. Lane repo {LANE} (branch main). The build wave's integrated work LANDED at commit {LANDED} (base {BASE}). Your job: attack ONE named item of that landed work and report whether it holds, with evidence. Claims (see {LANE}/reports/round-50/claims.json; manifest {LANE}/reports/round-50/separability/r50-manifest.json; receipt {LANE}/reports/round-50/validation.json):
- C coverage: {ENTRY} + README row + corpus/SOURCES.md rows S048–S069 (opened 2026-10-21; Gate quotes in corpus/lessons/round-50.md).
- O operability: tools/harness/receipt_guard.py (probes HEAD + all refs/heads/* + refs/remotes/*, landed_sha only from refs/remotes/*), tools/check-readme-revisions.py (unreachable pin fails closed, GIT_* scrubbed), counting probe reports/round-50/jj-colocation-probe.py (v2 R1 predicate amended after a v1 run; both recorded in reports/round-50/telemetry/jj-probe-v1.txt and -v2.txt).
- Ca calibration: tools/check-claim-separability.py, frozen fixture reports/round-50/separability/r49-fixture.json + independent prediction r49-expected-independent.txt, QUALITY.md criterion 7.
Read the landed bytes with `git -C {LANE} show {LANDED}:<path>` or a private clone; never trust the working tree for landed claims.

# Bounds
Read-only attack seats. Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>; never write under /home/vgpnk/Projects/shokunin/.ufo. Write ONLY your report. Any reproduction runs in a private clone under /tmp (`git clone -q --shared {LANE} /tmp/<you>-XXXX` then `git -C ... checkout -q {LANDED}`), with GIT_CEILING_DIRECTORIES=/tmp; delete it when done (the host disk is nearly full — keep temp small). NEVER edit lane files, never run git add/commit/stash/checkout/reset or any mutating jj command in {LANE}, never touch the lane jj state or git index, the fleet repo, sibling lanes, MANIFEST.json, .ufo/state or the watchdog log. No credentials, no live-process probing. Leaf seats: no delegation, no background jobs, no swarms.

# Sources
Source re-openers: open the row's URL for real this session (read-only; no logins). Report HTTP status/route, whether the Gate quote appears verbatim at the stated location, whether the tier/scope is honest under {LANE}/corpus/QUALITY.md criterion 6, and whether every sentence of the entry that cites the row is supported by what you read. Never invent text; an unreachable URL is a finding, not a pass.

# Tooling
You may install tools that help the task; read /home/vgpnk/.omp/agent/RULES.md first and record tool/version/channel/reason. All pacman transactions are PAUSED host-wide (never -S/-Sy/-Syu/-U/-R, downgrade, or service restart); use uv tool/npx/official binary into ~/.local/bin only if needed. Prefer no installs.

# Output
Report: item attacked, verdict (HOLDS / BROKEN / PARTIAL / UNEVALUATED) with exact file:line, command+output or URL evidence, and the smallest fix if broken. Author-lane advice, not admission."""

items = []
def add(name, role, text, axes=None):
    it = {"name": name, "role": role, "prompt": LEAD + text}
    if axes: it["axes"] = axes
    items.append(it)

ROWS = {
 "S048": "FAO 2001 Pastoralism in the new millennium, Introduction (https://www.fao.org/4/y2647e/y2647e02.htm)",
 "S049": "FAO 2001 Social institutions chapter (https://www.fao.org/4/y2647e/y2647e08.htm)",
 "S050": "Zeder 2008 PNAS via PMC2575338",
 "S051": "Marciniak 2011 Journal of World Prehistory (Springer)",
 "S052": "Evans-Pritchard 1940 The Nuer (Duke-hosted IA scan)",
 "S053": "Eczet 2020 Techniques & Culture (OpenEdition tc/14002)",
 "S054": "Hardin 1968 (MIT-hosted PDF)",
 "S055": "Ostrom 2009 Nobel lecture PDF",
 "S056": "Khazanov 2019 Chungara (SciELO PDF)",
 "S057": "Salzman 2004 Routledge page",
 "S058": "Schareika 2003 FAO Know to Move",
 "S059": "Sametinget Renmärken",
 "S060": "Ahearn 2018 Natural Hazards (d-nb.info PDF)",
 "S061": "Wiener et al. 2003 The Yak FAO ch. 8 and ch. 10",
 "S062": "UNESCO ICH Mongol ger element (live or Wayback)",
 "S063": "UNESCO ICH Bedu of Petra and Wadi Rum",
 "S064": "ETCSL Debate between Sheep and Grain (live or Wayback)",
 "S065": "AHD Indo-European roots *peku-",
 "S066": "D-PLACE EA004",
 "S067": "Librado et al. 2021 Nature",
 "S068": "Yacobaccio 2021 Animal Frontiers",
 "S069": "UNESCO ICH decision 14.COM 10.B.2 (transhumance)",
}
for sid, desc in ROWS.items():
    add(f"Reopen{sid}", "scout", f"Attack SOURCES row {sid} — {desc}. Read the row in `git -C {LANE} show {LANDED}:corpus/SOURCES.md` and its Gate bullet in `{LANDED}:corpus/lessons/round-50.md`; open the URL; verify quote, location, tier scope, and every `{sid}` citation in `{LANDED}:{ENTRY}` (grep -n '{sid}').", ["coverage"])

SECTIONS = [
 ("Head", "the head block (lines 1-13): topic, gap filled (both sweeps — re-run them at base " + BASE + "), sources anchors list, couples, source, verified-at numbers, recheck, scope"),
 ("Sec01", "§1 register property and its four-test table"),
 ("Sec02", "§2 one-owner boundary table — each neighbour anchor path:line must say what the row claims it owns"),
 ("Sec03", "§3 systems typology table and the political second axis"),
 ("Sec04", "§4 species and ecology table"),
 ("Sec05", "§5 herd lexicon and ownership marks"),
 ("Sec06", "§6 products and the Sherratt calibration"),
 ("Sec07", "§7 herd as wealth and exchange"),
 ("Sec08", "§8 tenure, commons and mobility rights (Hardin/Ostrom/earmark rows)"),
 ("Sec09", "§9 pastoral–sedentary relations and bias flags"),
 ("Sec10", "§10 ritual, myth and symbol"),
 ("Sec11", "§11 decision table, build order and error patterns"),
 ("Sec12", "§12 NON-CANON example: does it apply §11 faithfully and stay clearly non-canon?"),
 ("Sec13", "§13 calibration bank, living-practice flag, precision traps, §14 recheck and §15 scope/handoff"),
]
for key, what in SECTIONS:
    add(f"Review{key}", "reviewer", f"Attack {what} in `{LANDED}:{ENTRY}`. For every in-corpus `path:line` anchor, open that line at {LANDED} and check it supports the sentence; for every S-id, check the row's scope/anchor in SOURCES.md supports it (do not re-open URLs — other seats do). Flag overclaims, unsupported facts not marked `(to-verify)`, missing calibration status (QUALITY criteria 1-6), and canon decisions.", ["coverage"])

add("CriticCoverageCount", "critic", f"Attack claim C's measurement: re-run in private clones of {BASE} and {LANDED}: `find corpus/knowledge -name '*.md' | wc -l`, `ls corpus/knowledge/culture-material/*.md | wc -l`, `python3 -B reports/round-28/readme/sweep.py`, the word-bounded topic sweep, and the S-id/used-by resolution. Compare with {LANE}/reports/round-50/validation.json claims.C. Is 225→226 a real coverage move or bookkeeping?", ["coverage"])
add("CriticGapPremise2", "critic", f"Attack C's gap premise on landed bytes: does any existing entry already own pastoralism as a production system (partial owners: agrarian :62, semantic-fields :70,:105, animal-symbolism :73,:110, trade-economy :69)? Does the new entry duplicate rather than cite them? Verdict with line evidence.", ["coverage"])
add("ReviewReadmeRow", "reviewer", f"Attack the corpus/README.md change at {LANDED} (git diff {BASE} {LANDED} -- corpus/README.md): revision 2.7 block, row placement/topic byte-equality, counts 28/226, footer vector; run sweep.py, check-readme-heading.py and check-readme-revisions.py in a clone.", ["coverage"])
add("ReviewSourcesConformance", "reviewer", f"Attack corpus/SOURCES.md at {LANDED} against /home/vgpnk/Projects/shokunin/CORPUS.md section 'SOURCES.md — where a shokunin learns': run the seven census commands and `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (read-only); check S048–S069 kind/tier/status/used-by legality, tier inflation (A rows that are really publisher descriptions), the search-log note honesty, and the preamble pointer change.", ["coverage"])
add("ReviewLessonGate", "reviewer", f"Attack corpus/lessons/round-50.md `## Gate` at {LANDED}: every S048–S069 bullet must have URL, access date 2026-10-21, a verbatim <=25-word quote and location matching its SOURCES row; count words; cross-check 6 quotes against the seat reports under {W}/build/Src*.md.", ["coverage"])

add("ReviewGuardCode", "reviewer", f"Attack tools/harness/receipt_guard.py at {LANDED} (diff vs {BASE}): refusal semantics under detached HEAD, unborn HEAD, broken refs, symrefs, non-UTF-8 refnames, REFRESH_RECEIPTS ordering, GIT_* scrubbing; compare with {W}/build/ReviewGuardSemantics.md. Run --selftest in a clone.", ["operability"])
add("SentinelGuardFailOpen", "sentinel", f"Attack receipt_guard.py at {LANDED} for any remaining fail-open path that lets a committed receipt (on HEAD or any refs/heads/* or refs/remotes/* ref) be overwritten without REFRESH_RECEIPTS=1; build each case in a /tmp clone and report exit codes.", ["operability"])
add("MutateGuard", "mutation-tester", f"Mutation-test receipt_guard.py at {LANDED}: in a /tmp clone apply >=8 single-point mutants to the new ref-probing/landed_sha logic (skip remotes, skip heads, ignore for-each-ref stderr, landed from refs/heads, REFRESH before probes, ...) and report which the 69-control --selftest kills; list survivors.", ["operability"])
add("ReviewGuardControls45", "reviewer", f"Attack the claim that all 45 original receipt_guard selftest controls survive unchanged in name, order and expectation at {LANDED}: run --selftest at {BASE} and {LANDED} in clones, diff the ordered names and each control's asserted substrings (git show both versions). Note the runner-rechecks-before-publisher fixture change.", ["operability"])
add("ReviewReadmeRevCode", "reviewer", f"Attack tools/check-readme-revisions.py at {LANDED}: unreachable pin -> exit 2, git-free -> nonzero, GIT_* scrub, default/--readme modes unchanged, controls 1-11 retained; run --selftest in a full clone and in a shallow clone.", ["operability"])
add("MutateReadmeRev", "mutation-tester", f"Mutation-test tools/check-readme-revisions.py at {LANDED}: >=6 mutants (restore SKIP, drop cat-file check, drop GIT_* scrub, exit 0 on ERROR, ...) in a /tmp clone; report which the selftest kills.", ["operability"])
add("CriticProbeV2", "critic", f"Attack the counting probe amendment: reports/round-50/jj-colocation-probe.py v2 changed the R1 predicate AFTER a v1 run showed 1/3 on the landed tools (reports/round-50/telemetry/jj-probe-v1.txt vs -v2.txt). Is v2 a faithful reading of claim O's declared after_required ('reports a landed (branch/remote) sha distinct from the local HEAD'), or goalpost-moving? Does base still score 3/3 under v2? Would a fake fix (landed_sha=<HEAD>) still be flagged? Re-run both probe versions (git show {LANDED} for v2; v1 bytes from {W}/patches/ExecProbe-4.patch) on base and landed tools in /tmp.", ["operability"])
add("ScoutOCount", "scout", f"Re-run claim O's counting command independently: in /tmp, extract `git -C {LANE} archive {BASE} tools` and `archive {LANDED} tools`, run `python3 <landed probe> --tools-root <tree> --history-repo {LANE}` on both; paste JJ_COLOCATION_FALSE_NEGATIVES/POSITIVES lines and exits; compare with reports/round-50/validation.json claims.O.", ["operability"])
add("ScoutJjLive", "scout", f"Attack O under real jj (jj 0.45.1 at ~/.local/bin/jj) in a /tmp sandbox (never in the lane): colocated repo, receipt committed and pushed to a bare remote, then `jj new <older>` and `jj git fetch` states; run landed receipt_guard.py (git show {LANDED}) and report exit codes and landed_sha values.", ["operability"])

add("ReviewSepTool", "reviewer", f"Attack tools/check-claim-separability.py at {LANDED}: added-lines scanning, base-absent path rule, export novelty, overlap, record units, WORKTREE, needs_git leg, exit codes; find a manifest where it reports separable but a dependency exists, or vice versa. Run --selftest in a clone.", ["calibration"])
add("MutateSepTool", "mutation-tester", f"Mutation-test tools/check-claim-separability.py at {LANDED}: >=8 mutants (scan whole file not added lines; drop base-absence; drop export novelty; skip back-references; treat records as dependers; exit 0 on UNEVALUATED; ...) in a /tmp clone; report kills by --selftest and by the r49 fixture run.", ["calibration"])
add("ReviewSepFixture", "reviewer", f"Attack reports/round-50/separability/r49-fixture.json at {LANDED}: are the lands/trees/exports a faithful mechanical derivation of round 49 (commits c6a174d, 8c78e6b, d91c632, base c42d675)? Run the checker on it and compare with r49-expected-independent.txt; does it reproduce the outside verifier's C->S finding for the right reason?", ["calibration"])
add("CriticIndependence", "critic", f"Attack the 'independent prediction' claim: r49-expected-independent.txt was produced by the fixture seat (see {W}/build/ExecSepFixture.md) before the checker ran; the normalized 6/6 match is computed by reports/round-50/run-validation.py `_norm_finding`. Is the prediction truly independent (shared contract text, same seat reasoning)? Is the normalization lossy enough to hide a mismatch?", ["calibration"])
add("CriticR50Manifest", "critic", f"Attack reports/round-50/separability/r50-manifest.json at {LANDED}: are C/O/Ca lands complete and honest (SOURCES.md declared as a C land; lesson/README/LOG/SCORECARD/runner as records; validation.json omitted)? Did the integrator avoid findings by wording (e.g. removing the lesson path from the entry; renaming selftest literal S048->S998 in the checker)? Re-run the checker on it in a clone and judge whether 0 findings is real separability.", ["calibration"])
add("ReviewCriterion7", "reviewer", f"Attack QUALITY.md criterion 7 at {LANDED}: grounded in corpus/lessons/round-49-verifier-spotcheck.md? consistent with criteria 1-6 style? enforceable by the checker as written, or does it promise more than the tool checks?", ["calibration"])
add("ScoutCaCount", "scout", f"Re-run claim Ca's counting commands in a /tmp clone of {LANDED}: checker --selftest; checker on r49-fixture.json (expect exit 1, six findings); checker on r50-manifest.json (expect exit 0); `grep -ci separab corpus/QUALITY.md` at {BASE} and {LANDED}. Paste outputs.", ["calibration"])
add("ReviewRunner", "reviewer", f"Attack reports/round-50/run-validation.py (working-tree bytes sha de5b9c16…, later than {LANDED}'s runner: the topic-owner regex was word-bounded and checks added after landing) and reports/round-50/validation.json: does every EXPECT row match claims.json's after_required? Any check that cannot fail? Re-run it in /tmp clones of {LANDED} and {BASE}.", ["coverage", "operability", "calibration"])
add("CriticMeasurementAll", "critic", f"Attack all three before→after numbers in reports/round-50/validation.json for circularity, base-run safety and post-hoc changes (probe v2, runner regex fix, checker literal rename, entry wording change for separability). For each, say whether the claim still verifies.", ["coverage", "operability", "calibration"])
add("CriticMistakes", "critic", f"Attack corpus/lessons/round-50.md `## Mistakes` at {LANDED}: is R50-M1's fix 'shown able to fail' (cite the run)? Are R50-M2/M3 honest? What mistake of this round is missing (probe predicate changed post-measurement; tool literal collision; runner regex)?")
add("ScoutCensusAfter", "scout", f"Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` and the seven manual census commands on the lane (read-only) and on a {LANDED} clone; paste outputs, exit codes, rows by tier/status.")
add("ScoutLessonsIndex", "scout", f"Run `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` read-only in a {LANDED} clone; report findings (base had 3). Specify the exact corpus/lessons/README.md rows/pins needed for corpus/lessons/round-50.md at its landed bytes (compare {W}/build/ReviewLessonsIndex-revision5.diff).")
add("ConnectSiblingCa", "connector", f"Cross-lane: would kotodama's tools/check-claim-separability.py (at {LANDED}) have caught the separability rejections named in {W}/build/ConnectSiblingSeparability.md (game-dev-2d r105, kagi r27)? Read-only; reason from their manifests/claims; report reusable-or-not.")
add("ConnectSiblingGuard", "connector", f"Cross-lane: compare kotodama's landed receipt_guard ref-probing (at {LANDED}) with the sibling patterns in {W}/build/ConnectSiblingJj.md (souji, tsukuroi, kaidoku, mori, tameshi); report divergences that matter (e.g. landed = ancestry vs holder).")
add("SimplifyGuard", "simplifier", f"Attack receipt_guard.py at {LANDED} for unnecessary complexity in the r50 change (diff vs {BASE}): propose deletions that keep all 69 controls passing; verify each proposal in a /tmp clone. Report only; never edit the lane.")
add("SimplifySepTool", "simplifier", f"Attack tools/check-claim-separability.py at {LANDED} (1230 lines) for dead code or duplicate logic; propose deletions that keep --selftest 56/56 and the r49 fixture result; verify in a /tmp clone. Report only.")

spec = {
 "wave": "kotodama-r50-falsify",
 "milestone": "Round 50 falsify: attack C entry+rows, O gates+probe, Ca checker+fixture, measurements",
 "reportDir": ".ufo/waves/round-50/falsify",
 "axes": ["coverage", "operability", "calibration"],
 "context": CONTEXT,
 "items": items,
}
pathlib.Path(W, "falsify-spec.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
from collections import Counter
print(len(items), Counter(i["role"] for i in items))
