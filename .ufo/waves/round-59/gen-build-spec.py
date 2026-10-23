#!/usr/bin/env python3
"""Generate the round-59 build wave spec for kotodama: gen-build-spec.py <freeze-commit>."""
import json
import pathlib
import sys
from collections import Counter

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
W = f"{LANE}/.ufo/waves/round-59"
SCR = "/fast/scratch/hyaku/kotodama-r59"
BASE = "39c9ce8a6be5e5625d8befb54df53d621a3a7929"
FREEZE = sys.argv[1] if len(sys.argv) > 1 else "FREEZE"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
EC = "corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md"
SPOT = f"{LANE}/corpus/lessons/round-58-verifier-spotcheck.md"
L58 = f"{LANE}/corpus/lessons/round-58.md"
LOC = f"{LANE}/reports/round-59/reopen-quote.py"
RC = f"{LANE}/reports/round-59/rowcheck.py"
TOOLING = ("Tooling authorization (operator, 2026-10-19): you and every seat may install or update tools without asking; "
           "read /home/vgpnk/.omp/agent/RULES.md first and record each install (tool, version, channel, reason). All "
           "pacman transactions are PAUSED host-wide: never pacman -S/-Sy/-Syu/-U/-R, never downgrade, never restart a "
           "host service; use uv tool, npx or an official binary in ~/.local/bin, or report the need. Prefer no installs.")

CONTEXT = f"""# Goal
Kotodama round 59 (hyaku phase 4, 2026-10-23 UTC), BUILD wave. Lane repo {LANE} (branch main, jj-colocated). Claim base `{BASE}`; frozen declaration and pre-data control receipts at `{FREEZE}`: read {LANE}/reports/round-59/claims.json first. Two declared claims, each with ONE frozen predicate:
- C (coverage, learning claim, sourced claim): ONE new entry {LANE}/{EC}: amulets, talismans and apotropaic marks as a symbolic-material design system for worldbuilders — what a protective object is (amulet vs talisman vs charm, as each tradition and museum uses the words), what it protects against (evil eye, demons, illness, childbirth danger, misfortune), what it is made of and why (stones, metals, colours, knots, written words), where it is placed (body, child, threshold, building, animal, vehicle), who makes, blesses or sells it, how words and scripts become protective (inscribed names, magic squares, scrolls, incantation bowls), and how the practice changes (religious reform, commodification, souvenir trade). It points one-way to partial owners in the lane and hands canon to lore.
- D (depth): the frozen kongo-kingdom.md sentence fixes and speech-surrogates re-points in {LANE}/reports/round-59/d-fixes.json (round-58 seats verified them; this round lands them).
The L1 (KotodamaR59) writes the entry, registry rows, lesson and records from your reports; you supply opened-source evidence, receipts, code and attacks.

# Ownership and bounds (binding)
The L1 is the sole integration owner and holds the canonical planner seat. Every seat is a leaf: no delegation, no background jobs, no swarms (an executor may spawn at most one read-only labrat probe). Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>; never write under /home/vgpnk/Projects/shokunin/.ufo or anywhere else in the fleet repo. Seats write ONLY their own report file; any other file (draft rows, entry stubs, downloads, scripts, command output) goes ONLY under {SCR}/<YourName>/. Run every shell command with its working directory set to {SCR}/<YourName>/ and never redirect output to a relative path (round 58: a seat that ran `echo ... > x.txt` from the lane root left 11 stray files there). NEVER edit, create or delete any other file in {LANE}, a sibling lane, or the fleet repo /home/vgpnk/Projects/shokunin. Never run git or jj write commands (commit, add, checkout, reset, stash, push, new, describe, squash, rebase, bookmark) in the lane or the fleet repo; read-only git is fine; a sandbox clone goes under {SCR}/<YourName>/ with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset. Cap every process with `timeout`; kill any process you started before returning. Never message agent://all.

# Sources
External reading by ORDINARY MEANS ONLY: plain requests (read tool, curl, python urllib), public copies, archive.org scans by the digitising library, open repositories, official sites. NEVER use a headless browser or any tool to get past a bot challenge, captcha, paywall, login or other access control (QUALITY criterion 10); a third-party re-upload of an in-copyright work with no stated permission is NOT an ordinary copy. A source counts only if you opened it in this session. Do NOT offer a URL already in {LANE}/corpus/SOURCES.md (check with `grep -F '<host/path>' {LANE}/corpus/SOURCES.md`). Wikipedia and other community wikis are tier C leads only: never the row that carries a claim.

# Row rules (claim C rows; the frozen predicate checks every one, no slack)
FETCH-59 (declared before data, {RC} docstring): the acceptance fetches each URL once; a URL that errors (403, 429 after retries, TLS, timeout) is skipped and never passes. So list the live page URL first and, where a Wayback capture of the SAME page exists, a second URL `https://web.archive.org/web/<14-digit timestamp>id_/<live URL>` (find one with `curl -s 'https://archive.org/wayback/available?url=<live URL>'` or the CDX API; never save a capture of a page you could not open live). SAME-PAGE RULE: the source cell must contain NO other URL at all — every URL after the first must be a Wayback capture of that same page, or the row fails LOCATE with `not-same-page`; write a DOI as `DOI 10.xxxx/...` text, never as a link, and put no landing-page or second-copy link in the cell. URLs with an IP address, `localhost` or an explicit port are refused. Prefer hosts that serve plain GETs reliably; avoid hosts that answered you with 403/429/challenge. Reserved hosts (the round's control fixtures use them; do not offer rows from them): ryedalefolkmuseum.co.uk, horniman.ac.uk, magnes.berkeley.edu, foundlingmuseum.org.uk, nationalmuseet.dk, coriniummuseum.org.
Each claim C row's anchor quote must: be verbatim on the page (10-25 words, one full sentence or clause with at least 2 different function words such as the/of/in/is/to — never a heading, title, list item, caption fragment or table cell, inside straight double quotes); state the point the row teaches; hold a CHARM-GUARD window (a word like amulet/talisman/charm/apotropaic/phylactery/mezuzah/omamori/ofuda/scarab/bulla/nazar/hamsa/pendant/bead/inscription/scroll/symbol/mark/sign/figure/image within 3 words of a word like protect/ward/avert/guard/evil/harm/misfortune/demon/spirit/witch/luck/heal/bless/magic/curse/danger/illness/power/sacred — exact stem sets in {RC} CHARM and GUARD); come from a page with at least 3 such windows AND at least 2 occurrences of DISCIPLINE terms (amulet*, talism*, apotropai*, phylacter*, evil eye, charm(s), witch marks, ofuda, omamori, mezuz*, hamsa, nazar, wedjat, bulla, scarab ...). The row's teaches cell is one sentence (8+ words, ending with `.`) that shares at least 2 content stems with the quote and copies no 6-word run of it; the entry sentences you draft must share at least 2 content stems with both. Check every row before offering it: write it to {SCR}/<YourName>/rows.md, write your draft sentences (each ending `(S6xx)`) to {SCR}/<YourName>/stub.md, and run `cd {SCR}/<YourName> && timeout 900 python3 -B {RC} --draft {SCR}/<YourName>/rows.md --entry {SCR}/<YourName>/stub.md`; offer only rows printing LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS, and paste that output.
After landing, fresh non-author reviewers re-open EVERY claim C row in a blind packet and judge it SUPPORTED only when the quote is body text about protective objects or marks that carries the teaches cell and the entry sentences; one NOT-SUPPORTED row fails the claim. Offer only rows you would defend to that reviewer. Never overgeneralise one culture's practice into a universal.

# Tooling
{TOOLING}

# Output
A concise Markdown report at your Report path. Source seats give per row: (1) the registry row, exactly 11 cells: `| S6xx | <author/body, year, title — URL (direct, HTTP <status>, <bytes> bytes); capture <Wayback id_ URL> if listed> | <kind: one of spec, docs, paper, code, tool, dataset, talk, book, community, own-work> | <tier A/B> | <scope: what the row may support, one phrase> | <locator>: "<quote>" | <teaches sentence> | mined | 2026-10-23 | 2027-10-23 | {EC} |` using ONLY the S-ids assigned to you (the source cell must contain the live URL first and the capture URL second when you list one); (2) the Gate line: `- S6xx — <URL> — accessed 2026-10-23 — <locator>: “<quote>”. Grounds: <teaches>. Seat: <YourName>.`; (3) the pasted rowcheck output; (4) `draft sentences:` 2 to 4 entry sentences per row, each ending with `(S6xx)`, each saying only what the quote or the opened page carries; (5) `rejected:` every source you opened and did not offer, with the reason and, when the reason is a tool result (HTTP error, locate failure, TOPIC miss), the tool's verbatim output (QUALITY criterion 12). Non-source seats follow their item.
"""

items = []


def add(name, role, text, axes=("coverage",)):
    items.append({"name": name, "role": role, "prompt": LEAD + text, "axes": list(axes)})


SRC = ("Claim C source item. Open 2 to 4 sources by ordinary means and offer at most 2 rows in the row rules of the wave "
       "context. Aim the rows and draft sentences at design decisions a worldbuilder makes about protective objects: what "
       "it is made of, what danger it answers, who makes or blesses it, where it is worn or placed, and what words or signs "
       "it carries. Prefer museum object records with curatorial text, heritage agencies, university pages and open "
       "scholarly articles. Subtopic: ")
SCOUTS = [
    ("ScoutEgyptAmulets", "ancient Egyptian amulets: the wedjat (eye of Horus), scarabs, amulets placed in mummy wrappings; museum records (Met, British Museum, Petrie Museum, Brooklyn)."),
    ("ScoutMesopotamiaPazuzu", "Mesopotamian protective figures and amulets: Pazuzu heads and plaques against Lamashtu, protection of mothers and infants."),
    ("ScoutGrecoRomanApotropaia", "Greek and Roman apotropaia: gorgoneion, the fascinum, the child's bulla, apotropaic eyes on vessels."),
    ("ScoutEvilEyeMediterranean", "the evil eye complex around the Mediterranean and Middle East: eye beads (nazar), blue glass, what the eye is believed to do."),
    ("ScoutHamsaHand", "the protective hand (hamsa, hand of Fatima, hamesh) in Jewish and Islamic contexts; museum and scholarly sources."),
    ("ScoutJewishAmulets", "Jewish protective objects and texts: mezuzah, childbirth amulets (kimpet-tsetl, shir hamaalot), written amulets (kame'a); Jewish museums, national libraries."),
    ("ScoutIslamicTalismans", "Islamic talismanic objects: talismanic shirts, inscribed bowls and pendants, ta'wiz with Qur'anic verses and magic squares; Met, V&A, Khalili, LACMA records."),
    ("ScoutIncantationBowls", "Aramaic and Mandaic incantation bowls of late antique Mesopotamia: how they were buried and what they bind."),
    ("ScoutByzantineChristian", "Byzantine and early Christian amulets: phylacteries, encolpia, holy-rider amulets, magical gems with Christian formulae."),
    ("ScoutMedievalCharms", "medieval European textual charms and amulets: written charms, birth girdles, Anglo-Saxon charm texts, saints' names as protection."),
    ("ScoutWitchMarks", "apotropaic marks in buildings: ritual protection marks (daisy wheels, VV marks) at thresholds and chimneys; Historic England and heritage bodies."),
    ("ScoutConcealedObjects", "concealed protective objects in buildings: concealed shoes, witch bottles, horse skulls, iron at the threshold; museums and heritage records."),
    ("ScoutJapanOmamori", "Japanese omamori and ofuda: shrine and temple talismans, renewal each year, what they protect and how they are made; shrine, museum and scholarly sources."),
    ("ScoutChinaFuTalismans", "Chinese talismans (fu) and door protection: Daoist talisman writing, door gods, peach wood, mirrors against evil; museum and scholarly sources."),
    ("ScoutBuddhistAmulets", "Buddhist protective amulets: Tibetan gau amulet boxes, Thai votive amulets (phra khrueang), protective yantra designs."),
    ("ScoutSouthAsiaProtection", "South Asian protective practices and objects: taweez, nazar battu, protective threads and lemon-chilli strings, yantras; museum and scholarly sources."),
    ("ScoutWestAfricaAmulets", "West African amulets: leather-cased Qur'anic amulets (gris-gris, safi), amulet-covered garments of hunters and warriors; museum records."),
    ("ScoutEthiopiaScrolls", "Ethiopian healing and protective scrolls: their makers (dabtara), measured to the body, painted eyes and figures; library and museum sources."),
    ("ScoutMagicalGems", "Graeco-Egyptian magical gems and inscribed stones: Abrasax/Chnoubis gems, stones chosen for properties, lapidary lore."),
    ("ScoutWordAmulets", "words and letters as protection: the SATOR square, abracadabra triangles, written names of God or saints worn on the body; museum and library sources (a kotodama core: the word as a protective thing)."),
    ("ScoutChildBirthProtection", "protection of mothers, infants and children: coral, red threads, bells, childbirth amulets and cradle charms across traditions; museum records."),
    ("ScoutSoldierAmulets", "amulets carried into danger: Japanese senninbari thousand-stitch belts, First World War soldiers' charms and talismans; museum records."),
    ("ScoutTerminologyMuseum", "the vocabulary itself: how museums and reference works define amulet, talisman, charm and apotropaic object and where the terms differ (museum glossaries, encyclopedias, curatorial essays)."),
    ("ScoutCommodificationTrade", "change and commodification: nazar bead glassmaking, amulet markets and souvenir trade, state or religious campaigns against amulets; museum, heritage or scholarly sources."),
]
for i, (name, text) in enumerate(SCOUTS):
    ids = f"S{600 + 2 * i} and S{601 + 2 * i}"
    add(name, "scout", f"{SRC}{text} Your S-ids: {ids} (use only these).")

for name, text in [
    ("ConnectInLaneAmulets59", f"Claim C in-lane partial owners. Run `grep -rniE 'amulet|talism|apotrop|evil eye|phylacter|mezuz|omamori|ofuda|hamsa|nazar|witch mark|charm' {LANE}/corpus/knowledge` and group hits by file with path:line. Output: (1) the files that already say something about protective objects and what each says (so the new entry does not repeat it as new), (2) the one-way pointer lines the new entry should carry (`see path §N`), (3) which civilization entries hold amulet material the entry may point to."),
    ("ConnectSiblingAmulets59", "Claim C sibling overlap. Read-only scan of every sibling lane /home/vgpnk/Projects/shokunin/*-shokunin (excluding kotodama-shokunin): corpus/knowledge, PROVINCE.md and SKILL.md for ownership of amulets, talismans, protective symbols, magic systems, religious objects, game items (game-dev lanes) and world-bible registers (lore-shokunin). Output each overlap with path:line and the boundary rule the kotodama entry should state (what it owns, what it hands off)."),
]:
    add(name, "connector", text, ("coverage", "adjacency"))

add("CriticGapPremise59", "critic", (
    f"Attack claim C's premise before the entry is written. Check the gap: `git -C {LANE} ls-tree -r --name-only {BASE} corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` and grep the corpus for partial owners (heraldry-emblems-identity-marks, mineral-stone-symbolism, color-symbolism, binding-speech-complex, purity-pollution-boundary-systems, ritual-garments, adornment-body-codes). "
    "Output: (1) what ground is genuinely new vs already held, (2) the 8-12 section headings the new entry needs to be a deep owner, (3) the decision tables a worldbuilder needs (for example: protective-object typology, danger -> remedy table, material and colour logic, placement map, maker/authority table, change triggers), (4) the calibration traps the entry must mark (a universal 'evil eye' everywhere, Frazer's sympathetic magic as a universal law, 'pagan survival' readings, romanticised witch-mark folklore, closed or living religious practices treated as costume)."), ("coverage",))

for name, text in [
    ("ScribeSpotcheckRouting59", f"Route the round-58 outside check. Read {SPOT} in full. Draft the round-59 lesson section `## Spot-check intake (round-58 outside verifier)`: a table `| Item (round-58-verifier-spotcheck.md:line) | Finding | Route | Status |` with one row per §5 item 1-8 and the §4 quality verdict, routes naming this round's work (claim D for item 7; FETCH-59 and QUALITY criterion 13 for item 5; C's declared lands for item 6; errata for items 2-4; the deleted stray files and the wave containment rule for item 1; the start census for item 8); status left `pending` for the L1."),
    ("ScribeErrataQuality59", f"Draft (a) the round-59 lesson `## Errata (filed bytes not rewritten)` lines for {SPOT} §5 items 2, 3, 4 and 6, each stating the corrected fact with the command that shows it: item 2 the six pre-data revisions (`git -C {LANE} log --format='%h %cI %s' 91fb8fd9^..80f48c2c -- reports/round-58/accept-c.py`, and TOPIC mentions in accept-c.py before/after 31cf8b6 with `git show <rev>:reports/round-58/accept-c.py | grep -c TOPIC`); item 3 the claims.json declared_at vs revision_note contradiction; item 4 the per-leg split of `reports/round-58/telemetry/controls-c.txt` (count fixtures that fail ONLY the SUPPORT leg, and how many of those fail it only for a missing registry; give the command); item 6 the undeclared support path; (b) QUALITY criterion 13 (append-only, 2-4 sentences, plain style like criteria 10-12): a predicate with a live-fetch leg declares before data how an unreachable page is treated (an archived capture listed in the row, or a bounded allowance with its own control), and never relaxes it after data; grounded in {SPOT} §5 item 5 and the round-58 S510/S511 403s; (c) mistakes rows R59-M1.. for: the round-58 report's false 'not attributable to a round-58 seat' (stray files by ExecReasonSweep58), the uncounted sixth revision, the overstated control count; each with captured-by and a fix SHOWN ABLE TO FAIL (name the command and the input that makes it fail; run it and paste output). Write any command output only under {SCR}/ScribeErrataQuality59/."),
]:
    add(name, "scribe", text, ("calibration",))

XS = f"Write code and outputs ONLY under {SCR}/<YourName>/ and paste every run (command, output, exit code) into your report. Python 3 stdlib only. Run in a sandbox clone under {SCR}/<YourName>/ when a command could write."
for name, text in [
    ("ExecPacketBuilder59", f"Write {SCR}/ExecPacketBuilder59/build-packets.py for claim C's blind SUPPORT review. Read the SUPPORT leg of {LANE}/reports/round-59/accept-c.py first (PACKET_BLOCK, PACKET_FIELD, the `proposition` function, VERDICT): a seat's packet is blocks `### P##` each followed by exactly the lines `url: <every source URL of the row, space-separated>`, `quote: \"<anchor quote>\"`, `teaches: <teaches cell>`, `entry: <every entry line that cites the id, S-ids removed, joined with one space, on ONE line>`; the counter compares quote, teaches and entry after locator normalisation with the landed row, so derive them exactly as `proposition` does. Inputs: --sources (a SOURCES.md), --entry (the entry), --ids (comma list of S-ids), --planted (a file of `### PLANTED-<n>` blocks with url/quote/teaches/entry lines plus fields the packet must NOT copy, such as kind and why-not-supported), --seats (comma list), --per-row 2, --planted-per-seat 3, --seed N, --out DIR. Output DIR/packet-<Seat>.md and DIR/planted-key.json (`{{\"seats\": {{Seat: {{\"P01\": \"S6xx\" or \"PLANTED\", ...}}}}}}`). Each real row goes to exactly --per-row distinct seats, each seat gets --planted-per-seat distinct planted rows, labels P01.. are assigned after a seeded shuffle so planted rows sit at random positions, and every block has the same four fields in the same order. No field may reveal the S-id, the word PLANTED, the kind or the why-not-supported text. Include --selftest on synthetic input asserting coverage, blindness and that each block round-trips through accept-c's PACKET_BLOCK/PACKET_FIELD regexes to the same normalised proposition, and show it failing under a mutant that leaks the id. {XS}"),
    ("ExecRowHarvest59", f"Write {SCR}/ExecRowHarvest59/harvest.py: read every {LANE}/.ufo/waves/round-59/build/Scout*.md report, extract the 11-cell registry rows (lines matching `^\\| S6[0-4][0-9] \\|`), the Gate lines (`^- S6`), and the `draft sentences:` blocks; write rows.md, gate.md and sentences.md to an --out dir; flag rows whose id is outside the seat's assigned pair (two consecutive ids from S600, in the seat order of the wave), duplicate ids, cell counts other than 13 after split on `|`, kinds outside the enum (spec, docs, paper, code, tool, dataset, talk, book, community, own-work), URLs already in {LANE}/corpus/SOURCES.md, and duplicated URLs or quotes across rows. Include --selftest on synthetic reports. The scout reports do not exist yet; test on fixtures. {XS}"),
    ("ExecDApply59", f"Claim D application, in a sandbox clone of {LANE} checked out at `{FREEZE}` under {SCR}/ExecDApply59/: apply {LANE}/reports/round-59/d-fixes.json exactly (each kongo old -> new once, in order; the speech remap as whole words), run `timeout 900 python3 -B reports/round-59/accept-d.py` there (expect ACCEPT-D-59: PASS) and paste the output, then copy the two patched files to {SCR}/ExecDApply59/out/ and paste `sha256sum` of both and `git -C <clone> diff --stat`. Do not touch the lane. {XS}"),
]:
    add(name, "executor", text, ("depth", "operability"))

REVD = ("Claim D falsify item. For each fix assigned to you in " + f"{LANE}/reports/round-59/d-fixes.json" + " re-open its source by ordinary means (the support_urls listed, or the URL the entry cites), read the passage, and judge whether the NEW text is a faithful reading of the page (agree / disagree, with the served sentence pasted and the locator line from `python3 -B " + LOC + " '<url>' '<quote>'`). Flag any new sentence that still overreads, and any fix whose old text was actually right. Fixes: ")
for name, ids in [("ReviewDKongoA59", "18, 65, 82, 84a, 84b"), ("ReviewDKongoB59", "85, 89, 93, 97a, 97b"),
                  ("ReviewDKongoC59", "110, 140, 141, 146, and the speech remap (check S570-S574 in corpus/SOURCES.md carry the passages the re-pointed entry sentences rely on: sample 6 re-pointed sentences)")]:
    add(name, "reviewer", REVD + ids + ".", ("depth",))

c = Counter(i["role"] for i in items)
spec = {
    "wave": "kotodama-r59-build",
    "milestone": "Round 59: C amulets/talismans/apotropaic marks myth-symbol entry 234->235 with rows S600-S659 (FETCH-59, blind SUPPORT); D kongo/speech fixes",
    "reportDir": ".ufo/waves/round-59/build",
    "axes": ["coverage", "depth", "calibration", "adjacency", "operability"],
    "context": CONTEXT,
    "items": items,
}
json.dump(spec, open(f"{W}/build-spec.json", "w"), indent=1, ensure_ascii=False)
print(len(items), dict(c))
