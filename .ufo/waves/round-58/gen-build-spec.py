#!/usr/bin/env python3
"""Generate the round-58 build wave spec for kotodama. Run from anywhere: gen-build-spec.py <declaration-commit>."""
import json
import pathlib
import sys
from collections import Counter

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-58"
SCR = "/fast/scratch/hyaku/kotodama-r58"
BASE = "80f48c2c6f99381c0ba971d640fc7faef88aa406"
DECL = sys.argv[1] if len(sys.argv) > 1 else "DECL"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
EC = "corpus/knowledge/linguistics/toponymy-place-names.md"
SPOT = f"{LANE}/corpus/lessons/round-57-verifier-spotcheck.md"
L57 = f"{LANE}/corpus/lessons/round-57.md"
LOC = f"{LANE}/reports/round-58/reopen-quote.py"
RC = f"{LANE}/reports/round-58/rowcheck.py"
TOOLING = ("Tooling authorization (operator, 2026-10-19): you and every seat may install or update tools without asking; "
           "read /home/vgpnk/.omp/agent/RULES.md first and record each install (tool, version, channel, reason). All "
           "pacman transactions are PAUSED host-wide: never pacman -S/-Sy/-Syu/-U/-R, never downgrade, never restart a "
           "host service; use uv tool, npx or an official binary in ~/.local/bin, or report the need. Prefer no installs.")

CONTEXT = f"""# Goal
Kotodama round 58 (hyaku phase 4, 2026-10-23 UTC). Lane repo {LANE} (branch main, jj-colocated). Claim base `{BASE}`; declaration and pre-data control receipts at `{DECL}`: read {LANE}/reports/round-58/claims.json first. ONE declared claim with ONE frozen predicate:
- C (coverage, learning claim, sourced claim): ONE new entry {LANE}/{EC}: toponymy (place names) as a linguistic-cultural design system for worldbuilders — what a place name is built from (generic and specific elements, suffixes), how names stratify by language layer (substrate, conquest, settlement), why river and mountain names are the oldest layer, endonym and exonym, who standardises names (national naming authorities, UNGEGN) and by what principles (local usage, dual naming, commemorative waiting rules, derogatory-name removal), renaming as politics, romanization and transliteration, street names and field names, folk etymology. It goes DEEPER than the existing 7-line subsection `corpus/knowledge/linguistics/naming-systems.md` §3/§5 and points to it one way; it hands off canon to lore-shokunin. It cites only NEW registry rows in S500-S559. Predicate ACCEPT-C-58: `python3 -B reports/round-58/accept-c.py` (twelve legs; read its docstring and {RC}).
Records work (not claims), routed by {SPOT} §5: CODH bukan erratum, heraldry entry :41, superseding rows, round-56 carry rows S135/S141/S147/S151/S159, kongo-kingdom sentence fixes, a QUALITY check on not-registered reasons.
The L1 (KotodamaR58A2) writes the entry, registry rows, lesson and records from your reports; you supply opened-source evidence, maps, receipts and attacks.

# Ownership and bounds
The L1 (KotodamaR58A2) is the sole integration owner and holds the canonical planner seat. Every seat is a leaf: no delegation, no background jobs, no swarms (an executor may spawn at most one read-only labrat probe). Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>; never write under /home/vgpnk/Projects/shokunin/.ufo or anywhere else in the fleet repo. Seats write ONLY their own report file (executors may also write under {SCR}/<YourName>/). NEVER edit, create or delete any other file in {LANE}, a sibling lane, or the fleet repo /home/vgpnk/Projects/shokunin. Never run git or jj write commands (commit, add, checkout, reset, stash, push, new, describe, squash, rebase, bookmark...) in the lane or the fleet repo; read-only git (log, show, diff, grep, ls-files) is fine. Any git sandbox is a clone under {SCR}/<YourName>/ with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset. Bound every process with `timeout` (at most 900 s each); no unbounded recursive test runs; kill any process tree you started before you return. Never message agent://all.

# Sources
External reading by ORDINARY MEANS ONLY: plain requests (read tool, curl, python urllib), public copies, archive.org scans by the digitising library, open repositories, official sites. NEVER use a headless browser or any tool to get past a bot challenge, captcha, paywall, login or other access control (QUALITY criterion 10); a third-party re-upload of an in-copyright work with no stated permission is NOT an ordinary copy. Prefer live official or institutional pages over Wayback captures. A source counts only if you opened it in this session. Do NOT offer a URL already in {LANE}/corpus/SOURCES.md (check with `grep -F '<host/path>' {LANE}/corpus/SOURCES.md`). Wikipedia and other community wikis are tier C leads only: never the row that carries a claim.

# Row rules (claim C rows; the frozen predicate checks every one, no slack)
Each claim C row's anchor quote must: be verbatim on the page (8-25 words, one full sentence or clause with at least 2 different function words such as the/of/in/is/to — never a heading, list item or table cell, inside straight double quotes); state the point the row teaches; hold a NAMING-PLACE window (a word like name/names/named/toponym/exonym/endonym/renamed/gazetteer within 3 words of a word like place/river/town/village/city/mountain/hill/island/lake/settlement/region/county/parish/street/farm/stream — exact stem sets in {RC} NAMING and PLACE); come from a page with at least 3 such windows AND at least 2 occurrences of the field's own terms (toponym*, exonym*, endonym*, hydronym*, place name(s)/place-name(s), geographic(al) name(s), gazetteer, onomastic*); not be site-wide boilerplate (footer, navigation, cookie text); be tier A or B (tier C rows cannot be cited); use a URL no other row uses (two quotes from one page = one row). Its `teaches` cell is ONE paraphrased sentence of 8-30 words ending with a full stop, sharing at least 2 content words with the quote but copying no run of 6 words from it. Self-check BEFORE you report: put your rows in {SCR}/<YourName>/rows.md and run `cd {LANE} && timeout 900 python3 -B reports/round-58/rowcheck.py --draft {SCR}/<YourName>/rows.md`; every row must print LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS. Paste that output. A row that fails is dropped or fixed, never offered.
After landing, fresh non-author reviewers re-open EVERY claim C row and judge it SUPPORTED only when the quote is body text about place names that carries the teaches cell and the entry sentences citing it (the SUPPORT leg); one NOT-SUPPORTED row fails the claim. Offer only rows you would defend to that reviewer.

# Tooling
{TOOLING}

# Output
A concise Markdown report at your Report path. Source seats give per row: (1) the registry row, exactly 11 cells: `| S5xx | <author/body, year, title — URL (direct, HTTP <status>)> | <kind: docs/paper/book/web/record/dataset/community> | <tier A/B/C> | <scope: what the row may support, one phrase> | <locator>: "<quote>" | <teaches sentence> | mined | 2026-10-23 | 2027-10-23 | {EC} |` using ONLY the S-ids assigned to you; (2) the Gate line: `- S5xx — <URL> — accessed 2026-10-23 — <locator>: “<quote>”. Grounds: <teaches>. Seat: <YourName>.`; (3) the pasted rowcheck output; (4) `draft sentences:` 2 to 4 entry sentences per row, each ending with `(S5xx)`, each saying only what the quote or the opened page carries and reusing at least 2 content words of both the quote and the teaches cell; (5) `rejected:` every source you opened and did not offer, with URL and the reason (a reason that names a tool must paste that tool's output). Records seats follow their item. End with `installs:`.
"""

items = []


def add(name, role, text, axes=("coverage",)):
    items.append({"name": name, "role": role, "prompt": LEAD + text, "axes": list(axes)})


SRC = ("Claim C source item. Open 1 to 3 sources by ordinary means and offer at most 2 rows in the row rules of the wave "
       "context. Aim the rows and draft sentences at design decisions a worldbuilder makes about place names: what the "
       "name is built from, which language layer it belongs to, who may give or change it and under what rule, and how "
       "outsiders mangle or reinterpret it. ")
SCOUTS = [
    ("ScoutUNGEGNGlossary", "The UNGEGN Glossary of Terms for the Standardization of Geographical Names (unstats.un.org, official PDF or page): definitions of toponym, endonym, exonym, generic element and specific element."),
    ("ScoutUNGEGNHeritage", "Geographical names as cultural heritage and national standardization: UNGEGN's Manual for the national standardization of geographical names (2006) or the UN Conference resolutions on names as heritage (unstats.un.org official text)."),
    ("ScoutBGNPrinciples", "The U.S. Board on Geographic Names principles and policies (usgs.gov official pages or the BGN Principles, Policies, and Procedures PDF): local usage as the governing principle, the commemorative-name waiting period after a person's death, and naming in wilderness areas."),
    ("ScoutDerogatoryNames", "Removal of derogatory place names in the United States: Secretarial Order 3404 (2021) and the 2022 replacement of names containing the term 'sq___' (doi.gov or usgs.gov official pages), and the Advisory Committee on Reconciliation in Place Names."),
    ("ScoutNZDualNames", "New Zealand Geographic Board Ngā Pou Taunaha o Aotearoa (linz.govt.nz official pages): Māori place names, dual names (for example Aoraki / Mount Cook) and how the Board decides and records official names."),
    ("ScoutAustraliaDualNaming", "Dual naming of places in Australia: an official state or territory place-names policy or guideline (for example the Northern Territory, Queensland, Victoria or South Australia place names pages) or the ICSM Permanent Committee on Place Names principles (icsm.gov.au), including Uluru / Ayers Rock if served."),
    ("ScoutCanadaIndigenousNames", "Indigenous place names in Canada: the Geographical Names Board of Canada / Natural Resources Canada official pages (Canadian Geographical Names Database, principles) and an official example of restoring an Indigenous name (for example Iqaluit, formerly Frobisher Bay, or Haida Gwaii)."),
    ("ScoutEnglishElements", "English place-name elements: the Institute for Name-Studies, University of Nottingham (Key to English Place-Names, Survey of English Place-Names pages) — generic elements such as -tūn, -hām, -lēah, -burh and what they meant."),
    ("ScoutDanelawNames", "Scandinavian settlement names in England (-by, -thorpe, Grimston hybrids): an open institutional or scholarly page (University of Nottingham Institute for Name-Studies, a university research page, or an open-access article) on what their distribution shows."),
    ("ScoutRiverNames", "River names (hydronyms) as the oldest and most conservative layer of names: an open-access scholarly source or an institutional page on pre-English or 'Old European' hydronymy, or on Celtic river names in Britain."),
    ("ScoutScottishGaelic", "Gaelic place names in Scotland: Ainmean-Àite na h-Alba (gaelicplacenames.scot) official pages — common Gaelic elements (baile, achadh, inbhir, ceann) and how Gaelic and Norse layers sit in Scottish names."),
    ("ScoutWelshStandard", "Standardised Welsh place-names: the Welsh Language Commissioner's (Comisiynydd y Gymraeg) list of standardised Welsh place-names and its guidance or principles (official pages)."),
    ("ScoutIrishLogainm", "Irish placenames: logainm.ie (Placenames Database of Ireland) or the Placenames Branch / An Coimisiún Logainmneacha official pages — Irish elements (baile, cill, dún), the Ordnance Survey anglicisation of Irish names in the 1830s, and official Irish forms."),
    ("ScoutGermanPlaceNames", "German place-name suffixes or field names (Ortsnamen -ingen, -heim, -dorf, -rode, -hausen; Flurnamen): an open institutional page (a state office, an academy project or a university onomastics page) on what the suffixes date or mean."),
    ("ScoutSlavicGermanContact", "Slavic place names in eastern Germany and Central Europe (-itz, -ow, Sorbian names, bilingual signs): an open institutional or scholarly source on Slavic origin names and their German forms."),
    ("ScoutJapanPlaceNames", "Japanese place names: the Geospatial Information Authority of Japan (gsi.go.jp) official pages on place-name notation and standardisation, or an open source on municipal mergers creating new names (Heisei mergers) or on readings of kanji place names."),
    ("ScoutPinyinUN", "Romanization of Chinese place names: the UN conference resolution adopting Pinyin for Chinese geographical names (1977) or the UNGEGN Working Group on Romanization Systems report/status page (unstats.un.org official)."),
    ("ScoutRomanizationSystems", "Romanization and transliteration of place names in general: the UNGEGN Working Group on Romanization Systems pages (status of romanization systems by language, the single-romanization principle) — official UN pages."),
    ("ScoutRenamingCities", "City renaming as politics: an official government or institutional source on renaming a city or district (for example India's Ministry of Home Affairs procedure for changing place names, Bombay to Mumbai or Madras to Chennai, Kazakhstan's Astana renamings) — official pages preferred."),
    ("ScoutDecommunization", "Decommunization and post-Soviet renaming (Ukraine 2015-2016; Dnipropetrovsk to Dnipro; Kirovohrad to Kropyvnytskyi) or post-colonial renaming in Africa: an official parliamentary/government text or an open-access scholarly article on toponymic renaming."),
    ("ScoutStreetNaming", "Street naming (odonymy): an official municipal street-naming policy (for example City of Toronto, a London borough or a US city) — rules against duplicates, commemorative naming conditions — and/or an open-access scholarly source on commemorative street names."),
    ("ScoutFolkEtymology", "Folk etymology and reinterpretation of place names: an open institutional or scholarly source (an onomastics institute page, an open-access article, a national names board explanation) showing a place name re-explained or reshaped by folk etymology."),
]
for i, (name, text) in enumerate(SCOUTS):
    ids = f"S{500 + 2 * i} and S{501 + 2 * i}"
    add(name, "scout", f"{SRC}{text} Your S-ids: {ids} (use only these).")

add("ScoutHeraldry41", "scout", (
    f"Records item (round-57 spot-check {SPOT} §5 item 3). Entry {LANE}/corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:41 "
    "says 'in Scotland a cadet matriculates with a difference (S420)', but S420's page (courtofthelordlyon.scot 'coats of arms.htm') does not say it. "
    "Find, by ordinary means, an official or authoritative page (Court of the Lord Lyon pages, an Act, or a public-domain treatise such as Fox-Davies 1909 or "
    "Woodward on archive.org) that states that a younger son / cadet in Scotland must matriculate differenced arms. If found: draft ONE superseding-style NEW row "
    "(id S575, 11 cells as in the wave context but used-by `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`, status mined), its Gate line, the "
    "locator line from `python3 -B " + LOC + " '<url>' '<quote>'`, and the exact new text for line 41 (old -> new). If not found: the exact scoped-out text for line 41. "
    "The TOPIC/RELEVANCE row rules of the wave context do NOT apply to this records row (it is not a claim C row); LOCATE does."), ("calibration",))

REV = ("Re-open each named source by ordinary means; check the finding against the served text; give the verdict (agree / "
       "disagree with the finding) and the exact fix. Superseding rows are 11 cells, `teaches` opening `supersedes S### — `, "
       "status `queued` unless the superseded row is cited (then `mined` with the same used-by), opened 2026-10-23, recheck 2027-10-23; "
       f"paste the locator line from `python3 -B {LOC} '<url>' '<quote>'` for each anchor. The registry is append-only: never propose an "
       "in-place edit of any cell except status/recheck/used-by. The claim C row rules (TOPIC, RELEVANCE) do NOT apply to records rows. ")
for name, text in [
    ("ReviewSupersedeA58", f"Superseding rows owed ({SPOT} §5 item 4 and {L57} Frontier/Falsify): S413 (cadency quote punctuation: served ` ; ` vs commas), S417 (scope says 'domination' for 'Dominion'), S421 (anchor drops the served commas: 'no metal on a metal, no colours on a colour'). Your ids: S560, S561, S562."),
    ("ReviewSupersedeB58", f"Superseding rows owed ({SPOT} §5 item 4 and {L57}): S428 (anchor quotes 1 and 4 split by OCR hyphenation, do not locate), S433 (locator says 'abstract page' but the page never prints 'abstract'), S438 (teaches says 'since 1865'; source says 'approximately 1865'). Your ids: S563, S564, S565."),
    ("ReviewSupersedeC58", f"Superseding rows owed ({L57} Falsify): S440 (scope cell truncated), S445 (anchor differs from the served sentence by truncation/apostrophe). Your ids: S566, S567."),
    ("ReviewSupersedeD58", f"Superseding rows owed ({L57} Falsify): S452 (anchor differs by an apostrophe; Wayback-dependent: find whether a live NAVA copy of 'Good Flag, Bad Flag' serves it), S453 (served page does not carry the flag-protocol clause the scope/teaches implied; scope it to the statutory design). Your ids: S568, S569."),
    ("ReviewCarry135to147", f"Round-56 carry list ({SPOT} §5 item 6): S135, S141, S147. The drafted superseding rows and the re-pointed citations in {LANE}/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md are in {LANE}/.ufo/waves/round-55/build/ReviewCells135to159.md. Re-verify each draft against the live source and the CURRENT entry text (line numbers may have moved), and output final rows (ids S570, S571, S572) and the exact citation re-points (path:line old -> new)."),
    ("ReviewCarry151to159", f"Round-56 carry list ({SPOT} §5 item 6): S151, S159. Drafts in {LANE}/.ufo/waves/round-55/build/ReviewCells135to159.md. Re-verify each against the live source and the CURRENT entry {LANE}/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md, and output final rows (ids S573, S574) and the exact citation re-points (path:line old -> new)."),
    ("ReviewKongoA58", f"Carried a second round ({SPOT} §5 item 6): kongo-kingdom.md sentence fixes drafted by the round-57 seats in {LANE}/.ufo/waves/round-57/build/ReviewCarried*.md. Your lines (round-57 numbering): 18, 65, 82, 84, 85, 89. Re-read the CURRENT {LANE}/corpus/knowledge/civilizations/kongo-kingdom.md, re-open the cited sources where the fix depends on them, and output each fix as exact `old -> new` text with the current line number, or a reasoned drop."),
    ("ReviewKongoB58", f"Carried a second round ({SPOT} §5 item 6): kongo-kingdom.md sentence fixes drafted in {LANE}/.ufo/waves/round-57/build/ReviewCarried*.md. Your lines (round-57 numbering): 93, 97, 110, 140, 141, 146. Re-read the CURRENT {LANE}/corpus/knowledge/civilizations/kongo-kingdom.md, re-open the cited sources where needed, and output each fix as exact `old -> new` text with the current line number, or a reasoned drop."),
    ("ReviewCODH58", f"Routed defect 1 ({SPOT} §5 item 1 and §3 last row): {L57}:92 says the CODH bukan database quotes 'normalise below the locator's 8-word minimum'. The closure found 4 quotes of 10-15 words that print LOCATED. Read the scout's report {LANE}/.ufo/waves/round-57/build/ScoutKamonGarments.md, re-open codh.rois.ac.jp/bukan/ (and the /han/ page it used) by ordinary means, re-run `python3 -B {LOC} '<url>' '<quote>'` on each quote and paste the output. Draft the erratum line (never rewriting the filed bytes) stating the true ground, and say whether the source should be registered now as a queued row (if so draft it as id S576 with used-by `—`) or stay unregistered with which TRUE reason."),
]:
    add(name, "reviewer", REV + text, ("calibration",))

for name, text in [
    ("ScribeQualityC12", f"Routed defect 1 asks for a QUALITY check that each not-registered reason is re-tested by the tool it names. Read {LANE}/corpus/QUALITY.md in full and {SPOT} §3 and §5 items 1-2, and {LANE}/corpus/lessons/round-56.md:83 (koon1244) and {L57}:92 (CODH). Draft criterion 12 (append-only; 2-4 sentences, plain style like criteria 10-11): a reject or not-registered reason that names a tool or a measurable property (word count, locate failure, HTTP error) carries that tool's pasted output in the lesson Gate line; a reason with no such output is not a reason; grounded in the two false reasons. Give the exact text."),
    ("ScribeMistakes58", f"Draft the round-58 lesson `## Mistakes` rows (columns: id | class | evidence pointer | captured-by | fix). Mine: R58-M1 the false not-registered reason class, twice running (round-56 koon1244, round-57 CODH: {SPOT} §3, §5 item 1); R58-M2 the round-57 report tier-count error (report said A 34 / B 8; committed A 36 / B 6; {SPOT} §2 'Tier and kind'); R58-M3 the lane identity committed the dispatched prompt in r56 and r57 ({SPOT} §1 'Status-neutral defects'). For each give captured-by (the rule that should have caught it, or none) and a fix that can be SHOWN ABLE TO FAIL (name the command and the input that makes it fail). Verify the tier count yourself: `awk -F'|' '/^\\| S4(1[3-9]|[2-4][0-9]|5[0-4]) /{{print $5}}' {LANE}/corpus/SOURCES.md | sort | uniq -c` and paste the output."),
    ("ScribeSpotcheckRouting58", f"Route the round-57 outside check. Read {SPOT} in full. Draft the round-58 lesson section `## Spot-check intake (round-57 outside verifier)`: a table `| Item (round-57-verifier-spotcheck.md:line) | Finding | Route | Status |` with one row per §5 item 1-7 and §3/§6 notes, routes naming this round's seats (ReviewCODH58, ScoutHeraldry41, ReviewSupersedeA58-D58, ReviewCarry135to147, ReviewCarry151to159, ReviewKongoA58, ReviewKongoB58, ScribeQualityC12; defect 2 routed into claim C's frozen BOILER/RELEVANCE/TOPIC legs, reports/round-58/claims.json); status left as `pending` for the L1."),
]:
    add(name, "scribe", text, ("calibration",))

XS = f"Write code and outputs ONLY under {SCR}/<YourName>/ and paste every run (command, output, exit code) into your report. Python 3 stdlib only. Run in a sandbox clone under {SCR}/<YourName>/ when a command could write."
for name, text in [
    ("ExecReasonSweep58", f"Evidence for mistake R58-M1 and criterion 12. Extract every reject / not-registered bullet in the `## Gate` sections of {LANE}/corpus/lessons/round-55.md, round-56.md and round-57.md whose reason names a tool or a measurable property (word count, 'does not locate', HTTP error, 'below the 8-word minimum'). For each, re-run the named tool on the named source/quote by ordinary means (`python3 -B {LOC} '<url>' '<quote>'` for locator reasons; recover quotes from the matching seat report under {LANE}/.ufo/waves/round-5[5-7]/) and record: bullet path:line, reason, re-test command, output, verdict (reason holds / reason false / cannot re-test and why). {XS}"),
    ("ExecR57RowsNewBar58", f"Quality receipt (not a claim): run `cd {LANE} && timeout 900 python3 -B reports/round-58/rowcheck.py --draft <file>` with `--entry corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`, where <file> holds the rows S413-S454 extracted from {LANE}/corpus/SOURCES.md (write <file> under {SCR}/ExecR57RowsNewBar58/). Report per-leg pass counts and the failing rows with reasons: how many round-57 rows would fail the new relevance/boilerplate/topic bar (TOPIC is expected to fail for heraldry rows; report it separately as not applicable). {XS}"),
    ("ExecHarmCheck58", f"No-harm receipt for the owned axes. In a sandbox clone of {LANE} at `{DECL}` under {SCR}/ExecHarmCheck58/ run, each with timeout 900: `python3 -B reports/round-57/accept-o.py` (expect PASS), `python3 -B tools/check-gate-quotes.py --selftest`, `python3 -B tools/check-source-access.py`, `python3 -B reports/round-28/readme/sweep.py`, `python3 -B tools/check-gate-battery.py` (if it exists), `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (read-only). Paste outputs and exits; flag anything not green. {XS}"),
]:
    add(name, "executor", text, ("operability", "calibration"))

for name, text in [
    ("ConnectInLaneToponymy58", f"Claim C in-lane partial owners. Run `grep -rniE 'toponym|place[- ]?name|hydronym|exonym|endonym|odonym|gazetteer' {LANE}/corpus/knowledge` and group hits by file with path:line. Read {LANE}/corpus/knowledge/linguistics/naming-systems.md §3 and §5 in full. Output: (1) the exact list of claims naming-systems.md already makes about place names (so the new entry does not repeat them as new), (2) the one-way pointer lines the new entry should carry (`see path §N`), (3) which civilization entries hold place-name material the entry may point to."),
    ("ConnectSiblingToponymy58", "Claim C sibling overlap. Read-only scan of every sibling lane /home/vgpnk/Projects/shokunin/*-shokunin (excluding kotodama-shokunin): corpus/knowledge, PROVINCE.md and SKILL.md for ownership of place names, toponymy, maps/cartography naming, gazetteers, world-bible place registers (lore-shokunin). Output each overlap with path:line and the boundary rule the kotodama entry should state (what it owns, what it hands off)."),
]:
    add(name, "connector", text, ("coverage", "adjacency"))

add("CriticGapPremise58", "critic", (
    f"Attack claim C's premise before the entry is written. The surface says toponymy has 0 filename owners at base, but {LANE}/corpus/knowledge/linguistics/naming-systems.md "
    "§3 (Toponymy: functions, strata, politics) and §5 (Endonym/exonym) already cover parts of it. Read both sections and the scout subtopic list in the wave context goal. "
    "Output: (1) what ground is genuinely new vs repeated, (2) the 8-12 section headings the new entry needs to be a deep owner rather than a duplicate, (3) the decision tables a "
    "worldbuilder needs (for example: element grammar table, stratum-reading procedure, naming-authority principles table, renaming triggers), (4) the calibration traps (pop etymologies, "
    "'every name has a meaning', romanticised 'ancient' names) the entry must mark."), ("coverage",))

c = Counter(i["role"] for i in items)
spec = {
    "wave": "kotodama-r58-build",
    "milestone": "Round 58: C toponymy/place-names linguistics entry 233->234 with rows S500-S559 (LOCATE no slack, BOILER, RELEVANCE, TOPIC); routed round-57 records",
    "reportDir": ".ufo/waves/round-58/build",
    "axes": ["coverage", "calibration", "adjacency", "operability"],
    "context": CONTEXT,
    "items": items,
}
json.dump(spec, open(f"{W}/build-spec.json", "w"), indent=1, ensure_ascii=False)
print(len(items), dict(c))
