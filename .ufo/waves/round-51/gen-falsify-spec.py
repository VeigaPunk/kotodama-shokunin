#!/usr/bin/env python3
"""Generate the round-51 (attempt 3) falsify wave spec for kotodama. Run from anywhere."""
import json
import pathlib
from collections import Counter

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-51"
SCR = "/fast/scratch/hyaku/kotodama-r51a3-falsify"
BASE = "bff83ba65bf9559af4d7567e81703059667a0005"
DECL, DCOMMIT, CCOMMIT, RCOMMIT = "1f97472", "35f0d49", "da31d3c", "9feb69e"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
ENTRY_C = "corpus/knowledge/linguistics/sign-languages-manual-modality.md"
ENTRY_D = "corpus/knowledge/culture-material/pastoralism-animal-husbandry.md"

CONTEXT = f"""# Goal
Kotodama round 51, attempt 3, FALSIFY wave (hyaku phase 3, 2026-10-22). Lane repo {LANE} (branch main, jj-colocated). Every seat ATTACKS one landed item and reports what it found; you are trying to make a claim fail, not to defend it. Read {LANE}/reports/round-51/claims.json first.
Landed commits on branch main (all pushed): declaration `{DECL}`; claim D `{DCOMMIT}`; claim C `{CCOMMIT}`; records `{RCOMMIT}` (round lesson {LANE}/corpus/lessons/round-51.md and QUALITY criterion 8). Claim base `{BASE}`.
- D (depth, repair-first): {LANE}/{ENTRY_D} section 2 one-owner boundary table 11 -> 15 rows (four new rows at lines 44-47, a lead sentence at line 29, a numerals seam sentence in section 5 at line 93, the shepherd-king row at line 42 aligned with section 10). Counter `python3 -B reports/round-51/boundary-count.py` must print `rows=15 resolved=15 distinct=15`. D must not cite the C entry, any S-id from S071 up, or the round lesson.
- C (coverage, learning claim): new entry {LANE}/{ENTRY_C} (223 lines, sections 1-15) citing SOURCES rows S071-S122 (S123, S124 queued leads), indexed in {LANE}/corpus/README.md (revision 2.8). Counter `find corpus/knowledge -name '*.md' | wc -l` must print 227; `python3 -B reports/round-28/readme/sweep.py` must exit 0 with footer total 227 and linguistics 26. C must not name `corpus/lessons/round-51.md` (in any spelling) or `reports/round-51/boundary-count.py`.
Build-wave seat reports (useful context, author-lane, not evidence): {LANE}/.ufo/waves/round-51/build/. Lane bar: {LANE}/corpus/QUALITY.md. Province: {LANE}/PROVINCE.md (conlang and worldbuilding method; never canon, never clinical, education-policy or rights rulings). Calibration codes: {LANE}/corpus/knowledge/verification/calibration-registry.md:35-39.

# Ownership and bounds
The L1 (KotodamaR51a3) is the sole integration owner and holds the canonical planner seat. Every seat is a leaf and read-only on the lane: no delegation, no background jobs, no swarms. Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>; never write under /home/vgpnk/Projects/shokunin/.ufo or anywhere else in the fleet repo. Seats write ONLY their own report file in the lane. Any experiment that writes (mutations, sandbox trees, controls) runs only in a private clone at {SCR}/<SeatName> (`git clone -q --shared {LANE} {SCR}/<SeatName>`); never use symbolic links from a sandbox into the lane; check `realpath` before every write. NEVER edit, create or delete files in {LANE} other than your report; never run git add/commit/stash/checkout/switch/reset/pull/push in {LANE}. Never run any jj command at the fleet root /home/vgpnk/Projects/shokunin (its auto-track snapshots untracked files); in the lane, jj only read-only and only with --ignore-working-copy; read-only git (log/show/diff/grep/ls-tree) is fine. Never touch the fleet repo, sibling lanes, .ufo/state, MANIFEST.json, lane jj state or the lane Git index. Do not read or use /fast/scratch/hyaku/kotodama-r51-*, /fast/scratch/hyaku/kotodama51-* or {LANE}/reports/round-51/calibration/ (held prior-attempt material). Message the L1 only for a blocker. Write plain English: no run-together words, no private jargon.

# Sources
Re-open sources yourself (read-only; no logins, no paywall bypass, no downloads into the lane). Report each URL you opened with access date 2026-10-22, what you found at the stated location, and whether the row's quote, tier (QUALITY criterion 6) and scope hold. Never invent a source, quote, page or date; if a URL fails, say so with the error text.

# Tooling
You may install tools that help the task; read /home/vgpnk/.omp/agent/RULES.md first and record tool, version, channel and reason. All pacman transactions are PAUSED host-wide: never pacman -S/-Sy/-Syu/-U/-R, never downgrade, never restart a host service; use uv tool, npx or an official binary in ~/.local/bin, or report the need. Prefer no installs.

# Output
A concise Markdown report at your Report path: the item you attacked, every command with its output and exit code, every source URL opened, findings (each with severity high/medium/low, an exact path:line or URL pointer, and the smallest fix), and the verdict for your item: HOLDS, HOLDS-WITH-FIXES or FAILS. Unrun checks are listed as unrun. Author-lane attack, never admission."""

items = []


def add(name, role, text, axes):
    items.append({"name": name, "role": role, "prompt": LEAD + text, "axes": axes})


# ---------------- claim D ----------------
for name, anchor, line in [
    ("ReviewDRowRitual", "ritual-liminality.md:63", 44),
    ("ReviewDRowSymbolism", "symbolism-synthesis-method.md:69", 45),
    ("ReviewDRowCelestial", "celestial-symbolism-calendars.md:28", 46),
    ("ReviewDRowNumerals", "numerals-and-measures.md:101", 47),
]:
    add(name, "reviewer", f"Attack claim D's new row at {LANE}/{ENTRY_D}:{line} (anchor `{anchor}`). (1) Open the anchored line in corpus/knowledge and quote it: does it support the 'What it owns' cell exactly, or does the cell overclaim? (2) Is the boundary developed or explicitly narrowed in the entry body at the section the cell names? Quote the body line. (3) Does the row duplicate authority with another row (same noun owned twice) or launder a claim the body marks `(to-verify)` (check `surplus`)? (4) Is it a genuine neighbour or filler? Verdict per the context.", ["depth"])
add("ReviewDOldRows", "reviewer", f"Attack claim D's no-harm leg. Run `git -C {LANE} diff {DECL} {DCOMMIT} -- {ENTRY_D}` and list every changed line. Confirm the 11 old rows keep their neighbours and anchors; judge the changed shepherd-king row (line 42) against its anchor `sacred-kingship-mythic-charter.md:65` and section 10's 'Shepherd-king' row; judge the new lead sentence (line 29) and the section-5 sentence (line 93) for accuracy and for any new unsourced claim. Verdict per the context.", ["depth"])
add("RerunDCounter", "reviewer", f"Re-run claim D's counter independently. In {SCR}/RerunDCounter clone the lane, then: (a) at `{DCOMMIT}` and at the branch tip run `python3 -B reports/round-51/boundary-count.py` and record the exact line and exit; (b) build a D-only tree (base `{BASE}` plus only D's lands from `{DCOMMIT}`: the entry and reports/round-51/boundary-count.py) and run it there; (c) at base run it (expect 11/11/11); (d) record `sha256sum reports/round-51/boundary-count.py` at `{DECL}` and at the tip and confirm the counter was not edited after declaration. Verdict per the context.", ["depth"])
add("MutateDCounter", "mutation-tester", f"Mutation-test claim D's measurement in {SCR}/MutateDCounter (clone; never the lane). Apply one mutation at a time to the landed entry's four new rows (lines 44-47) and to the counter's input: drop a row, duplicate a neighbour, dangle a line number, remove backticks, swap an anchor to a directory, add a second neighbour in one row, strip the line number. For each, record the counter's printed line and exit, and whether the mutation is killed. Report every survivor with the exact mutation, and say which survivors could hide a defect in the landed rows as they stand now. Verdict per the context.", ["depth"])
add("CriticDSeparability", "critic", f"Attack D's independence from C. Read `git -C {LANE} diff {DECL} {DCOMMIT}` added lines and the full D entry at the tip. Search for any mention of the C entry (full path, `linguistics/...`, bare basename, 'sign language', 'manual'), any S-id at or above S071, any URL or author-year source not already in the entry at base, any reference to the round-51 lesson in any spelling, and any edit to corpus/README.md or corpus/SOURCES.md in D's commit. Also run `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` in a clone at the tip ({SCR}/CriticDSeparability) and record output and exit. Verdict per the context.", ["depth", "calibration"])
add("CriticDRepairScope", "critic", f"Attack the repair-first framing. Read {LANE}/corpus/lessons/round-50-verifier-spotcheck.md (routed debt 2 at lines 92-98 and line 47), {LANE}/.ufo/waves/round-51/build/CriticClaimD.md and {LANE}/corpus/lessons/round-51.md (Spot-check intake and Frontier). Does round 51 claim more than the row-count leg of routed debt 2? Is every item not landed (body development of old cell-only phrases, the market row, the unanchored `civilizations/` row, the `(to-verify)` markers) listed as carried? Is the D claim a genuine depth move or a count move? Verdict per the context.", ["depth", "calibration"])

# ---------------- claim C: sections ----------------
SECS = [
    ("ReviewCHead", "the H1 and head block (lines 1-12) plus sections 14 Recheck and 15 Scope: field order, gap-filled sweep commands (re-run them on base `" + BASE + "` in a clone and confirm 0 and 0), partial owners named, couples resolvable, recheck items actionable"),
    ("ReviewCSec01", "section 1 (register property): master claim, four choices, the test table and its owners, and whether S071, S072, S073, S074, S075, S076 support what is cited"),
    ("ReviewCSec02", "section 2 (one-owner boundary, 14 rows): open every backticked anchor line and judge whether it supports the 'What it owns' cell; flag restatement of an existing owner and any overclaim"),
    ("ReviewCSec03", "section 3 (typology of manual systems): every cell's citation (S086, S087, S088, S079, S089, S082, S090) and the (to-verify) and H markers; Ethnologue's 'Shared' filing of alternate sign languages as a counterexample to the typology"),
    ("ReviewCSec04", "section 4 (community ecology): figures (Adamorobe >10% in 1961, ~2% by 2001; Bengkala >=7 generations, ~1,200 hearing signers; ~5% Deaf parents) against S091, S092, S093; drift into clinical genetics or education policy"),
    ("ReviewCSec05", "section 5 (sublexical parameters): Battison primes counts, the dominance-condition handshape set, Prosodic Model location figures and minimal pairs against S071, S094, S095, S096, S097; the table's design rules"),
    ("ReviewCSec06", "section 6 (grammar in space): loci, agreement verbs, depicting constructions, nonmanual markers, ABSL word order against S098, S099, S100; any universal word-order claim"),
    ("ReviewCSec07", "section 7 (iconicity): handling/instrument/shape strategies and the arbitrariness drift against S101, S102, S103; whether abstract-only rows carry substantive claims"),
    ("ReviewCSec08", "section 8 (emergence, families, diachrony): Nicaraguan Sign Language, LSFic, BSLic/BANZSL, Plato Cratylus 422e against S080, S104-S108; the 'about 25 years' figure"),
    ("ReviewCSec09", "section 9 (alternate signing by hearing people): Warlpiri, Plains Indian Sign Talk and the 1930 film, Cluny, occupational signing against S081, S109-S112, S075; the politeness-taboo-euphemism.md anchors at :75, :77, :101"),
    ("ReviewCSec10", "section 10 (contact, codes, writing): fingerspelling families, initialization, contact signing, International Sign (pidgin label contest), Signed English, Stokoe notation, HamNoSys, SignWriting against S083, S113, S114, S074, S071, S115, S116, S084, S077"),
    ("ReviewCSec11", "section 11 (decision table, build order, DR-SGN records): every row's section pointer, anchors and S100 citation; whether DR-SGN-01..04 are actionable and the prefix unused elsewhere in corpus/"),
    ("ReviewCSec12", "section 12 (NON-CANON worked example): canon hygiene, every real-world claim keyed (S086, S087, S081, S117, S115), the politeness-taboo-euphemism.md:118 anchor, and whether the example actually walks the section 11 table"),
    ("ReviewCSec13", "section 13 (calibration bank): each status code against calibration-registry.md:35-39; the count row (UN more than 300, Ethnologue 161, WFD 200+) against S077, S120, S121; the critical-period row against S119; the village-idyll row against S118; terminology rows against S076, S121, S122"),
]
for name, what in SECS:
    add(name, "reviewer", f"Attack claim C's entry {LANE}/{ENTRY_C}, {what}. Re-open the cited S-rows' URLs from {LANE}/corpus/SOURCES.md and check each cited claim against what the source actually says at its anchor. Flag unsupported cells, abstract-only or publisher-description rows carrying substantive claims (QUALITY criterion 6), terminology problems, canon decisions, and clinical, education-policy or rights rulings. Verdict per the context.", ["coverage"])

# ---------------- claim C: source rows ----------------
for lo in range(71, 125, 6):
    ids = ", ".join(f"S{i:03d}" for i in range(lo, min(lo + 6, 125)))
    add(f"ReopenS{lo:03d}", "reviewer", f"Re-open SOURCES rows {ids} in {LANE}/corpus/SOURCES.md. For each row: open the URL in the `source` cell (and the Gate bullet's URL in {LANE}/corpus/lessons/round-51.md if it differs); confirm the Gate quote appears verbatim at the stated location and is at most 25 words; confirm kind, tier (QUALITY criterion 6; community is never A; abstracts and publisher descriptions are B), scope and anchor; confirm `used-by` names the entry for mined rows and `—` for queued rows. Verdict per the context.", ["coverage"])

# ---------------- claim C: whole-claim attacks ----------------
add("RerunCCount", "reviewer", f"Re-run claim C's counters independently in {SCR}/RerunCCount (clone). At `{CCOMMIT}` and at the tip: `find corpus/knowledge -name '*.md' | wc -l`, `ls corpus/knowledge/linguistics/*.md | wc -l`, `python3 -B reports/round-28/readme/sweep.py` (render lines and exit), `python3 -B tools/check-readme-revisions.py`, `python3 -B tools/check-readme-heading.py`, and the S-id resolution one-liner in {LANE}/reports/round-51/separability-manifest.json (C's acceptance). Then build a C-only tree (base `{BASE}` plus only C's three lands from `{CCOMMIT}`) and run the same commands there. Verdict per the context.", ["coverage"])
add("MutateSeparability", "mutation-tester", f"Mutation-test the round's separability evidence in {SCR}/MutateSeparability (clone at the tip; never the lane). Run `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` clean, then one mutation at a time: add the C entry path to a D row; add `S071` to a D row; add `corpus/lessons/round-51.md` to the C entry; add `lessons/round-51.md` (relative) to the C entry; add `reports/round-51/boundary-count.py` to the C entry; edit a README line naming the D entry. Record output and exit for each and list survivors. Verdict per the context.", ["calibration"])
add("CriticCRestatement", "critic", f"Attack claim C as restatement. Compare {LANE}/{ENTRY_C} with its partial owners: {LANE}/corpus/knowledge/linguistics/phonetics-phonology.md:195-205, {LANE}/corpus/knowledge/culture-material/adornment-body-codes.md section 7, {LANE}/corpus/knowledge/linguistics/sound-symbolism.md:120-126, syntax-typology.md:95-103, numerals-and-measures.md:103-111, writing-systems.md:15-25, language-contact.md:85-110. Use word-bounded probes. Is any section a paraphrase of an existing owner, or does the entry claim gesture ownership that adornment-body-codes holds? Is the 227th file hollow? Verdict per the context.", ["coverage"])
add("CriticCProvince", "critic", f"Attack claim C for province drift and terminology. In {LANE}/{ENTRY_C}: grep for clinical words (hearing loss, audiology, implant, treatment, cure, therapy, disorder, impairment), education-policy and legal rulings (must, should be taught, right to, law requires), deficit framing (deficient, lack, primitive, broken, mime), and rejected labels outside quoted rejections (deaf-mute, dumb, hearing-impaired). Check each hit in context. Also judge 'therapy settings' in section 3 and the Living-practice flag in section 13 against {LANE}/PROVINCE.md. Verdict per the context.", ["coverage"])
add("CriticCCalibration", "critic", f"Attack claim C's calibration. For every factual claim in {LANE}/{ENTRY_C} that is not followed by an S-id, an in-corpus anchor, `(to-verify)` or an **H** marker, list it with its line. Check the claims most likely to be over-general: the ASL user figure (about 250,000), 'since 1817', 'NSL since 1977', 'about 25 years', '3-6 generations', '~45 handshape primes', '14 sign markers', '70 million'. Re-open the cited source for each and say whether it holds. Verdict per the context.", ["calibration"])
add("ReviewSourcesRegistry", "reviewer", f"Attack the SOURCES registry edit. Run the census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` and the seven frozen census commands from /home/vgpnk/Projects/shokunin/CORPUS.md section 'SOURCES.md — where a shokunin learns' on {LANE}/corpus/SOURCES.md. Check that rows S001-S070 are byte-identical to `{DECL}` (`git diff {DECL} {CCOMMIT} -- corpus/SOURCES.md`), that only the preamble line 8, the new rows, one path and one search-log note changed, and that the search-log counts (88 identified, 54 included, 15 merged, 13 encyclopedia pages replaced, 6 excluded) can be reproduced from the build seat reports under {LANE}/.ufo/waves/round-51/build/. Verdict per the context.", ["coverage"])
add("ReviewLessonGate", "reviewer", f"Attack the round lesson {LANE}/corpus/lessons/round-51.md. Every new row S071-S124 needs a Gate bullet with URL, access date and a verbatim quote of at most 25 words with its location (count words). Check the rejected list, the status change log, the spot-check intake table against {LANE}/corpus/lessons/round-50-verifier-spotcheck.md:92-98, and each Mistakes row (class, evidence pointer, captured-by, fix). Does R51-M1's fix really show a red state in {LANE}/reports/round-51/telemetry/declaration-dry-run.txt? Is R51-M2 honestly marked as not shown able to fail? Verdict per the context.", ["calibration"])
add("ReviewQuality8", "reviewer", f"Attack QUALITY criterion 8 in {LANE}/corpus/QUALITY.md. Is it grounded in a lesson (the spot-check Decision and R51-M1)? Is it checkable from committed bytes, as it claims? Apply it to round 51 itself: compare every command in {LANE}/reports/round-51/claims.json and separability-manifest.json with {LANE}/reports/round-51/telemetry/declaration-dry-run.txt and report any declared command that was not dry-run on its exact input. Verdict per the context.", ["calibration"])
add("ScoutMisroot", "scout", "Misroot sweep, read-only. Run `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) and list every untracked file whose content names kotodama round 51 or a KotodamaR51a3 seat. For each, give the path, the first lines, and whether the same bytes exist under /home/vgpnk/Projects/shokunin/kotodama-shokunin. Never move, copy or delete anything. Also list any file under /home/vgpnk/Projects/shokunin/kotodama-shokunin that `git status --porcelain` shows modified or untracked outside .ufo/waves/round-51/. Verdict per the context.", ["calibration"])

spec = {
    "wave": "kotodama-r51-falsify",
    "milestone": "Round 51 attempt 3 falsify: attack landed D rows, C entry, S071-S124, records and measurements",
    "reportDir": ".ufo/waves/round-51/falsify",
    "axes": ["depth", "coverage", "calibration"],
    "context": CONTEXT,
    "items": items,
}
out = pathlib.Path(W) / "falsify-spec.json"
out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
print(len(items), Counter(i["role"] for i in items))
