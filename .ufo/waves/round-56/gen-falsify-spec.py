#!/usr/bin/env python3
"""Generate the round-56 falsify wave spec for kotodama. Run from anywhere."""
import json
import pathlib
from collections import Counter

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-56"
SCR = "/fast/scratch/hyaku/kotodama-r56-falsify"
BASE = "045f458ceaa35d40baa7c56727c346d60ae210bf"
DECL = "b4b7db91a38447bb2c07b0ef436fc9654dcec89c"
O_TIP = "7576fd43bbbe34a00341e4b1956c907f2760e7d8"
C_TIP = "767040e0d8b9f9fe9e69b9a7ab8bc75a93b33b6b"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
EC = f"{LANE}/corpus/knowledge/civilizations/kongo-kingdom.md"
SRC = f"{LANE}/corpus/SOURCES.md"
LES = f"{LANE}/corpus/lessons/round-56.md"
TOOLING = ("You and every seat may install or upgrade tools that help the task; read /home/vgpnk/.omp/agent/RULES.md first "
           "and record tool, version, channel and reason. All pacman transactions are PAUSED host-wide: never pacman "
           "-S/-Sy/-Syu/-U/-R, never downgrade, never restart a host service; use uv tool, npx or an official binary in "
           "~/.local/bin, or report the need. Prefer no installs.")

CONTEXT = f"""# Goal
Kotodama round 56 FALSIFY wave (hyaku phase 4, 2026-10-22). Lane repo {LANE} (branch main, jj-colocated). Claim base `{BASE}`; declaration `{DECL}`; claim O landed at `{O_TIP}` (tools/check-gate-quotes.py: html-entity class, decoded quote and Grounds rules, exit 2 on invalid UTF-8); claim C landed at `{C_TIP}` ({EC}: the Kingdom of Kongo as a linguistic-cultural reference base, citing rows S359-S412 of {SRC}, all opened this round). Read {LANE}/reports/round-56/claims.json first. The uncommitted lesson draft {LES} carries the Gate lines (one per row). Your job is to ATTACK what landed: re-open sources, re-run counting commands, mutate tools, and test the entry's sentences against the pages they cite. Every item names what it attacks. Findings are advisory; the L1 (KotodamaR56) decides and applies fixes.

# Ownership and bounds
The L1 (KotodamaR56) is the sole integration owner and holds the canonical planner seat. Every seat is a read-only leaf: no delegation, no background jobs, no swarms (a mutation-tester may spawn at most one read-only labrat probe). Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>; never write under /home/vgpnk/Projects/shokunin/.ufo or anywhere else in the fleet repo. Seats write ONLY their own report file (mutation-testers and re-run seats may also write under their scratch dir). NEVER edit, create or delete any other file in {LANE}, a sibling lane, or the fleet repo /home/vgpnk/Projects/shokunin. Never run git or jj writes in the lane or the fleet repo: no commit, push, add, stash, checkout, reset, ref update, index or jj state change; read-only git (log, show, diff, status, archive) is fine; in the lane only read-only jj with --ignore-working-copy, and never any jj at the fleet root. Any git that writes runs ONLY in a sandbox clone under /fast/scratch/hyaku/ (`git clone -q {LANE} {SCR}/<SeatName>/lane`) with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset (`env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git ...`). Scratch goes under {SCR}/<SeatName>/. The only message target is agent://KotodamaR56; never message agent://all. Finish with your report written; a seat that cannot finish still writes what it has and says what is missing.

# Sources
Re-open sources by ORDINARY MEANS ONLY: plain requests (read tool, curl), public copies, museum APIs, archive.org or Wayback captures. NEVER use a headless browser or any tool to get past a bot challenge, captcha, paywall, login or other access control (QUALITY criterion 10); a challenge met and routed around by an ordinary copy is "challenge met, not passed". Space requests to one host about 10 s apart (Cambridge Core, the Met and Wayback rate-limit bursts with HTTP 429).

# Tooling
{TOOLING}

# Output
A concise Markdown report at your Report path: verdict first, then one line per checked item (`S###` or `path:line`, verdict CARRIED / WRONG-LOCATOR / OVER-READ / UNSUPPORTED / DEFECT, evidence with a verbatim quote of at most 25 words and its locator, and the exact replacement text for any fix), then unrun checks. Plain English; no run-together words; no HTML entities."""

items = []


def add(name, role, text, axes):
    items.append({"name": name, "role": role, "prompt": LEAD + text, "axes": list(axes)})


ROWTASK = ("Re-open each row's URL (the url in its {src} row; follow the route recorded there). For each row: (1) every anchor quote and the Gate line's quote in {les} are verbatim on the page you opened and at most 25 words, at the stated locator; (2) the tier fits QUALITY criterion 6 for the row's scope ({lane}/corpus/QUALITY.md line 29); (3) every sentence of {ec} that cites the row (grep the S-id) is carried by the page at the strength stated (keep hedges; no over-read; museum labels not read as studies); (4) the Grounds of the Gate line equals the row's teaches cell. Give exact old -> new text for any fix.")
slices = [(359, 361), (362, 364), (365, 367), (368, 370), (371, 373), (374, 376), (377, 379), (380, 382), (383, 385),
          (386, 388), (389, 391), (392, 394), (395, 397), (398, 400), (401, 403), (404, 406), (407, 409), (410, 412)]
for a, b in slices:
    ids = ", ".join(f"S{n}" for n in range(a, b + 1))
    add(f"ReviewRowsS{a}toS{b}", "reviewer",
        f"Claim C row slice {ids}. " + ROWTASK.format(src=SRC, les=LES, lane=LANE, ec=EC),
        ("coverage", "calibration"))

for name, role, text, axes in [
    ("RerunAcceptC56", "reviewer", f"Re-run claim C's counting command in sandbox clones (never in the lane): `python3 -B reports/round-56/accept-c.py` at `{BASE}` (expected exit 1 with SET, SWEEP, FLOOR FAIL as declared in claims.json `before`) and at `{C_TIP}` (expected exit 0, seven legs PASS). Also re-derive by plain commands: knowledge file count at both revisions, civilizations count, the set of S-ids the entry cites (all in S359-S412, each exactly one row, mined, used-by the entry), and that `git diff {BASE} {C_TIP} -- corpus/SOURCES.md` adds only rows S359-S412 and changes no other line. Report every output with its exit code and the revision.", ("coverage",)),
    ("RerunAcceptO56", "reviewer", f"Re-run claim O's counting command in sandbox clones: `python3 -B reports/round-56/accept-o.py` at `{DECL}` (expected exit 1: ENTITY, EXIT, DECODE, BADUTF8 FAIL as declared) and at `{O_TIP}` (expected exit 0, eight legs PASS), plus `python3 -B tools/check-gate-quotes.py --selftest` at both. Confirm `git show --stat {O_TIP}` touches tools/check-gate-quotes.py only. Report outputs, exit codes and revisions.", ("operability",)),
    ("RerunControls56", "reviewer", f"Replay QUALITY criterion 11 controls: run `python3 -B reports/round-56/criterion11-controls.py {LANE} {DECL}` and `python3 -B reports/round-56/criterion11-controls-o.py {LANE} {DECL}` (both read-only on the lane: git archive into mktemp) and compare byte for byte (excluding mktemp paths) with the committed receipts reports/round-56/telemetry/criterion11-controls.txt and criterion11-controls-o.txt. Then check that every clause in claims.json names a red control that exists in the builder and fails only its leg.", ("operability", "calibration")),
    ("RerunDeclaration56", "reviewer", f"Criterion 9 two-way check and the routed revision-naming fix: run `python3 -B reports/round-56/dry-run.py check reports/round-56/telemetry/declaration-dry-run.txt` (expected exit 0 with MEASURED_REVISION naming {DECL}); confirm each `$ ` command matches a declaration verbatim; confirm the receipt and both criterion-11 receipts name the revision they measured; run the same check against reports/round-55/telemetry/declaration-dry-run.txt in a scratch copy with round 55's claims.json in place and show it fails for the missing revision line.", ("calibration",)),
    ("RerunSeparability56", "reviewer", f"Separability (AXES.md 'causally separable', QUALITY criterion 7): in a sandbox clone at `{C_TIP}` with a stand-in corpus/lessons/round-56.md copied from the lane worktree draft {LES} (the record unit's other lands exist), run `python3 -B tools/check-claim-separability.py reports/round-56/separability-manifest.json` and report the result. Independently, grep O's landed tool for any id in S359-S418 and C's landed lines for any O land path; and run accept-c on base plus C's lands only and accept-o on base plus O's lands only.", ("calibration",)),
    ("RerunCensus56", "reviewer", f"Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (read-only) and `python3 -B tools/check-source-access.py` in the lane; report status totals (mined/queued/rejected) at `{BASE}` and at `{C_TIP}` with the CORPUS.md histogram command, malformed rows (NF!=13) and duplicate ids, and any W-warning new in S359-S412.", ("coverage",)),
    ("ReviewGateLines56", "reviewer", f"Mechanical check of the {LES} `## Gate` lines: for each `- S### ` line, the Grounds text equals the row's teaches cell in {SRC} byte for byte; the URL equals the row's URL; each quoted span is at most 25 words and occurs in the row's anchor cell; no HTML character reference (`python3 -B tools/check-gate-quotes.py {LES}` must print 0 findings). Write your own python; report every mismatch.", ("calibration",)),
    ("ReviewSectionsLanguageTitles", "reviewer", f"Section attack on {EC} §3-§5 (source shelf, language, titles and succession): for each sentence, open the cited row's page and check the synthesis across rows is not stronger than each row (no 'Kikongo' singular where a variety is meant; succession claims dated; the Soyo/court dialect dispute attributed). Give exact replacements.", ("coverage", "calibration")),
    ("ReviewSectionsCapitalKinFaith", "reviewer", f"Section attack on {EC} §6-§8 (capital and provinces, kinship, Christianity and the Antonian movement): check each sentence against its cited page, the period of each claim (a 20th-century Luanda ethnography must not describe the kingdom), and the 1706 execution date and place hedges. Give exact replacements.", ("coverage", "calibration")),
    ("ReviewSectionsObjectsDress", "reviewer", f"Section attack on {EC} §9-§10 (minkisi, the cosmogram dispute, dress, regalia, cloth and money): check each sentence against its cited page, that nineteenth-century objects are not staged as court practice, that 'fetish' appears only as a flagged source word, and that the nzimbu word shift (shells, then beads) is dated as the rows date it. Give exact replacements.", ("coverage", "calibration")),
    ("CriticEraTable56", "critic", f"Attack {EC} §11 (era staging) row by row: every date and event against its cited row; contested dates (1482 or 1483 contact, 1678, 1706, 1709) must be marked as such; the partition rows must not say the kingdom ended in 1885. Also check that the table's periods do not contradict §5-§10.", ("coverage", "calibration")),
    ("CriticCalibrationBank56", "critic", f"Attack {EC} §1 (three senses of Kongo) and §13 (calibration bank). For each coded item, does the cited row carry the code (R/C/B/H/T as defined in {LANE}/corpus/knowledge/verification/calibration-registry.md:35-39)? Use the build critic's coding ({W}/build/CriticCalibrationKongo.md) as a second opinion and report disagreements with reasons.", ("calibration",)),
    ("CriticHandoff56", "critic", f"Attack {EC} §14 (handoff to lore): re-read every lore anchor it cites (fleet-relative paths under /home/vgpnk/Projects/shokunin/lore-shokunin/ and the in-lane contract) and report any anchor that does not say what the entry claims; check the NON-CANON condition and that no real polity is handed off as a faction or place.", ("calibration",)),
    ("CriticClaimC56", "critic", f"Attack claim C as a whole: run the falsifiers F1-F18 in {W}/build/CriticGapPremise56.md against `{C_TIP}`; check the must-not list (citations only in the header, a dates-only era section, museum or dictionary material counted as kingdom material, publisher pages used for beliefs, edits to neighbouring files); judge whether the 231 -> 232 count is hollow. Report each falsifier's command, output and verdict.", ("coverage", "calibration")),
    ("CriticClaimOProbes56", "critic", f"Attack claim O as landed at `{O_TIP}`: run the 14 falsifier probes listed in {W}/build/CriticClaimO56.md (probe rows S971-S981; scratch files under /fast/scratch/hyaku/kotodama-r56/CriticClaimO56/ are readable) against the landed tool, and report for each whether the landed tool behaves as a faithful decoder (double encoding decoded once, semicolon-free names not decoded, numeric references without `;` not decoded, &ldquo; quotes counted, a bad file not hiding later files' findings). Name each gap the acceptance could not see.", ("operability",)),
    ("ReviewExcludedSources56", "reviewer", f"Discernment attack on what the L1 did NOT register. Read the staging log the L1 recorded in {LES} (search log; if absent, read /fast/scratch/hyaku/kotodama-r56/L1/stage.py, which lists every block dropped or merged with its reason) and the build reports in {W}/build/. For each exclusion (Thornton 1991 and Thornton 2001 JSTOR scans on third-party hosts, Glottolog koon1244 N3 block, uncited blocks, the merged Pigafetta, Fromont and Bentley rows), decide agree or disagree with reasons; for the two Thornton scans, check whether the host states permission.", ("calibration",)),
]:
    add(name, role, text, axes)

for name, text in [
    ("MutateEntityRule", f"Mutation-test claim O's html-entity rule in tools/check-gate-quotes.py at `{O_TIP}` in a scratch copy: write at least four mutants (named references accepted without the html5 table; numeric references not recognised; once-per-row dropped; the finding class renamed) and for each report whether `--selftest` and `python3 -B reports/round-56/accept-o.py` fail (killed) or pass (survived). Report survivors as gaps with the smallest test that would kill them."),
    ("MutateDecode", f"Mutation-test claim O's decoding in tools/check-gate-quotes.py at `{O_TIP}` in a scratch copy: at least four mutants (decode only the Grounds; decode only quotes; decode twice; skip decoding before truncated-grounds) and report killed or survived under `--selftest` and accept-o, with the smallest killing test for each survivor."),
    ("MutateUtf8", f"Mutation-test claim O's invalid UTF-8 handling in tools/check-gate-quotes.py at `{O_TIP}` in a scratch copy: at least four mutants (catch the error but exit 1; print the error without the path; stop at the first bad file; let the traceback through) and report killed or survived under `--selftest` and accept-o, with the smallest killing test for each survivor."),
]:
    add(name, "mutation-tester", text, ("operability",))

spec = {
    "wave": "kotodama-r56-falsify",
    "milestone": "Round 56 falsify: attack C (Kongo entry, rows S359-S412) and O (html-entity Gate checks) as landed",
    "reportDir": ".ufo/waves/round-56/falsify",
    "axes": ["coverage", "operability", "calibration"],
    "context": CONTEXT,
    "items": items,
}
out = pathlib.Path(W) / "falsify-spec.json"
out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
print(len(items), Counter(i["role"] for i in items))
