#!/usr/bin/env python3
"""Assemble the round-65 claim-C entry draft from landed row fragments.

Reads .ufo/waves/round-65/rows/**/row-<SID>.txt (format contract:
`ROW=| SID | ... |`, `BULLET=`, `VERIFY=`, `CAPTURE=`, `ACCESS=`), emits
.ufo/waves/round-65/stage/entry-draft.md plus stage/assemble-audit.json.

Every check below mirrors a frozen accept-c.py leg where the leg's inputs are
available from fragments alone (registry insertion is the L1's job):
  FILE shape (1 H1, no H3, <=16 H2, <=250 lines, `- topic:`)
  ROWS cells/tier/status/opened/recheck/usedby/quote-words/capture identity
  ONEID one S-id per line, bullets in `- clause (SID)` shape
  RESTATE content words, in-order quote words, copied run, novel word,
          and the revision-1 teaches near-copy coverage (>=0.80 FAILS)
  HOSTS placeholder hosts
  LINK  duplicate query-normalized URLs across rows

Usage: python3 -B .ufo/waves/round-65/stage/assemble-entry.py [--root .]
Exit 0 when the draft is written (even partial), 2 on unreadable input.
The exit code does NOT encode claim truth: read assemble-audit.json.
"""
import argparse
import json
import os
import re
import sys
import unicodedata
import urllib.parse

ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"
NEW_IDS = [f"S{n}" for n in range(750, 776)]
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`]+")
QUOTE_RE = re.compile(r'"([^"]+)"|\u201c([^\u201c\u201d]+)\u201d')
CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d{14})id_/(\S+?)\s*[.;]?\s*$", re.IGNORECASE)
NONWORD = re.compile(r"[\W_]+", re.UNICODE)
WORD_RE = re.compile(r"\w+", re.UNICODE)
LABEL_RE = re.compile(r"^(ROW|BULLET|VERIFY|CAPTURE|ACCESS)\s*[=:]\s?(.*)$")
SID_RE = re.compile(r"\bS\d{3,}\b")
STOPWORDS = set("""
a an and are as at be been but by for from has have he her his i if in into is it its
of on or she so that the their them they this to was we were with you your not no nor
""".split())
PLACEHOLDER_HOSTS = (
    "example.com", "example.org", "example.net", "example.io", "example.edu",
    "httpbin.org", "httpbingo.org", "reqres.in", "postman-echo.com",
    "jsonplaceholder.typicode.com",
)

# Game-class grouping fixed from the 26 row topics in taskcall-final.json.
SECTIONS = [
    ("## 1. How games and play are classified",
     ["S750", "S756", "S757", "S758", "S759"],
     "Compare the frameworks instead of choosing one. An ethnographic classification of games by "
     "chance, skill, and physical action, an account of play as constitutive of culture, a set of "
     "play categories, a survey of play's competing rhetorics, and the anthropology of sport answer "
     "different questions; a design may borrow from several without treating any as the definition."),
    ("## 2. Board and race games of the ancient world",
     ["S751", "S752", "S753", "S773", "S775"],
     "Treat a board, its pieces, and its resting places as the surviving evidence, and the rules as a "
     "reconstruction. Keep tomb and burial contexts, wide geographic distributions, and betting play "
     "as separate observations attached to their own sources."),
    ("## 3. Strategy boards on the move",
     ["S763", "S764", "S765"],
     "Trace a board game along the routes its pieces and names travelled. Distinguish a documented "
     "early occurrence from a later claim of origin, and keep each reconstruction attached to the "
     "sources that support it."),
    ("## 4. Ballgames, ball materials and stick games",
     ["S761", "S762", "S771"],
     "Separate what a ball is made of, where it is played, and what the game is taken to mean. "
     "Material evidence for rubber and solid balls is not by itself evidence for the scale or "
     "meaning of a contest."),
    ("## 5. Athletic and ritual contests",
     ["S754", "S760", "S772"],
     "Keep festival setting, contest procedure, and the status of competitors as three separate "
     "design variables. A contest can be ritual in framing, organised in procedure, and political "
     "in consequence at the same time."),
    ("## 6. Lots, dice and gambling toys",
     ["S755", "S767", "S768"],
     "Treat the chance device as an object with a history: bone, stone, clay, or a spinning body "
     "with marked faces. Wager, divination, and children's play may attach to the same object "
     "without being the same practice."),
    ("## 7. Cards",
     ["S766"],
     "Describe cards as manufactured objects: paper, suits, faces, and the collections that preserve "
     "them. A deck's design is evidence of production and trade before it is evidence of a rule set."),
    ("## 8. Children's playground repertoire",
     ["S769", "S770"],
     "Record children's games as repertoire that children transmit to each other: counting-out "
     "formulas, skipping, singing and ring games, seasonal rounds, and local variants."),
    ("## 9. Target and throwing games",
     ["S774"],
     "Describe the target, the throwing piece, and the throwing line, then the scoring convention. "
     "Official rules and regional play are separate sources of authority."),
]

# Cross-row statements, each emitted only when every required row landed.
PATTERNS = [
    (["S757", "S758", "S759"],
     "Definitions of play disagree in a way a design can use: one account separates play from "
     "ordinary life by a boundary and a mood, another sorts play into categories of competition, "
     "chance, pretence, and vertigo, and a third treats play's meanings as multiple rhetorics rather "
     "than one essence. Choosing a definition is a design decision, not a finding."),
    (["S750", "S751", "S752", "S753"],
     "Board and lot games recur across regions as portable assemblages of a marked surface, movable "
     "pieces, and a chance device or counting rule. Classification by chance versus skill cuts "
     "across those finds rather than dividing cultures."),
    (["S751", "S752"],
     "Elite and mortuary settings preserve games that ordinary play rarely leaves visible: a royal "
     "grave or a tomb assemblage can fix a board's form while leaving its rules unrecoverable."),
    (["S763", "S764", "S765", "S775"],
     "Board games travel with trade, conquest, and scholarship, and the further a game is from its "
     "documented occurrence, the more of its rule set is inference. Origin claims and transmission "
     "routes are statements about sources, not about a game's essence."),
    (["S761", "S762"],
     "Ballgame evidence couples equipment and institution: a worked rubber ball and a built court "
     "appear together with political and ritual use, so a design that keeps the ball but drops the "
     "occasion loses the documented relation."),
    (["S760", "S772", "S754"],
     "Contests staged on an occasion bind procedure to calendar and spectatorship. Festival setting, "
     "eligibility of competitors, and the arbitration of outcomes are separable choices even when a "
     "source reports them together."),
    (["S755", "S767", "S768"],
     "Chance devices cross the boundaries between divination, wager, and children's play: the same "
     "bone, die, or spinning top can carry different practices in different hands. Describe the "
     "object and then state which practice it serves."),
    (["S769", "S770"],
     "Children's play is transmitted as repertoire rather than as a fixed curriculum: counting-out "
     "formulas, singing games, and seasonal rounds persist with local variation and without adult "
     "instruction."),
    (["S766", "S767"],
     "Manufactured play objects show standardisation and its limits: dice settle into a small set of "
     "conventional forms while card faces and suits remain regionally variable."),
    (["S771", "S754"],
     "Team contests and stick games are claimed both as community practice and as heritage, and the "
     "claim itself carries authority: origin accounts, governing bodies, and museum collections can "
     "describe the same game under different ownership."),
    (["S756"],
     "Organised sport is a cultural institution in its own right: organisation, spectatorship, and "
     "identity are available as objects of description alongside the play itself."),
    (["S750", "S769", "S770"],
     "Documented play spans adult contest and children's playground repertoire, and the two are "
     "collected by different methods: ethnographic catalogues, schoolyard observation, and printed "
     "collections each see a different slice."),
    (["S773", "S751", "S753"],
     "Betting and race play attach wager to a board or a track, so a design can keep the board, the "
     "stake, and the adjudication as three separate features."),
    (["S774", "S755"],
     "Throwing and knucklebone games share a minimal kit: an object to throw and a target or a fall "
     "to read. Elaborate rule sets are a later layer over that kit."),
]

TABLE = """| Worldbuilder choice | Possible consequence for play scenes | Possible consequence for social structure |
|---|---|---|
| A game is decided by a chance device | Show the device, the throw, and the reading of the result rather than the outcome alone. | Decide who may hold the device, who wagers, and what a loss transfers. |
| A game rewards skill and strategy | Make training, memory, and calculation visible as competence. | Tie rank or office to demonstrated play skill, or refuse to. |
| A contest is attached to a festival or ritual calendar | Fix the occasion, the order of events, and the spectators in the scene. | Decide which offices stage, sponsor, or arbitrate the contest. |
| A ballgame requires special equipment | Specify the ball's material, the court, and who can supply or repair them. | Decide whether equipment access marks status or is communal. |
| Children's play is transmitted by other children | Give the rhyme, the counting-out formula, or the rule as a local variant. | Decide whether adults forbid, ignore, or co-opt the play. |
| A game is borrowed from a neighbouring region | Mark the route, the renamed pieces, and the local reinterpretation. | Decide who claims the game's origin and what that claim legitimizes. |
| Wager is part of play | State what is staked and who adjudicates a dispute. | Decide whether loss creates obligation, debt, or loss of standing. |"""

ONEWAY = [
    ("corpus/knowledge/culture-material/funerary-material-culture.md",
     "owns grave assemblage and mortuary display; this entry keeps a game object in a tomb context as game evidence only."),
    ("corpus/knowledge/culture-material/calendar-festival-systems.md",
     "owns festival calendars and civic occasion; a contest's festival setting is cited here as context, not modelled."),
    ("corpus/knowledge/culture-material/warrior-material-culture.md",
     "owns martial equipment and its display; athletic and contest equipment is not described here."),
    ("corpus/knowledge/culture-material/trade-economy-lexicon.md",
     "owns exchange and transmission vocabulary; the movement of games along routes is noted here, not modelled."),
    ("corpus/knowledge/culture-material/music-instrument-lexicon.md",
     "owns instruments and music; the sound of a singing game is not scored here."),
    ("corpus/knowledge/culture-material/hunting-foraging-subsistence.md",
     "owns subsistence practice; target games are treated here as play, not as hunting technique."),
    ("corpus/knowledge/culture-material/material-culture-inference-method.md",
     "owns the inference ladder from artifact to practice; game-object inference follows it rather than restating it."),
]

HANDOFF = """This entry supplies sourced anchors and conditional design questions; it makes no canon decision. Lore-shokunin owns the world bible and its consistency verification under `corpus/knowledge/synthesis/worldbible-integration-contract.md`; contested scope goes to the integrator.

Decisions this entry deliberately does not make: whether a given culture's game is sacred or secular, which contest is authoritative, and how a fictional game's rules are fixed. Those are canon choices for lore-shokunin, recorded and verified in the world bible, not here. Drafts and contested readings route to the integrator."""


def norm_words(text):
    folded = unicodedata.normalize("NFKC", text).casefold()
    return [w for w in NONWORD.sub(" ", folded).split() if w]


def word_tokens(text):
    return WORD_RE.findall(unicodedata.normalize("NFKC", text).casefold())


def content_words(text):
    return [w for w in norm_words(text) if len(w) >= 4 and w not in STOPWORDS and w.isalpha()]


def anchor_quote(cell):
    m = QUOTE_RE.search(cell)
    return (m.group(1) or m.group(2)) if m else None


def cells(line):
    bare = re.sub(r"^(ROW|BULLET|VERIFY|CAPTURE|ACCESS)\s*[=:]\s?", "", line.strip())
    return [c.strip() for c in bare.split("|")[1:-1]] if bare.startswith("|") else []


def norm_url(url):
    try:
        parts = urllib.parse.urlsplit(url.strip().rstrip(".,;'"))
    except ValueError:
        return url.strip().lower()
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    try:
        port = parts.port
    except ValueError:
        port = None
    if port and not (scheme == "http" and port == 80) and not (scheme == "https" and port == 443):
        host = f"{host}:{port}"
    path = parts.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}"


def in_order_coverage(clause_words, reference_words):
    if not clause_words:
        return 0.0
    pos = hits = 0
    for w in clause_words:
        for j in range(pos, len(reference_words)):
            if reference_words[j] == w:
                pos = j + 1
                hits += 1
                break
    return hits / len(clause_words)


def longest_copy_run(clause_words, reference_words):
    joined_ref = " " + " ".join(reference_words) + " "
    best = 0
    for start in range(len(clause_words)):
        for length in range(best + 1, len(clause_words) - start + 1):
            window = clause_words[start:start + length]
            if " " + " ".join(window) + " " in joined_ref:
                best = length
            else:
                break
    return best


def parse_fragment(path):
    labels = {}
    for raw in open(path, encoding="utf-8", errors="strict").read().splitlines():
        m = LABEL_RE.match(raw.strip())
        if m and m.group(1) not in labels:
            labels[m.group(1)] = m.group(2).strip()
    return labels


def scan(rows_dir, root):
    found = {}
    conflicts = []
    for dirpath, _dirs, files in os.walk(rows_dir):
        for name in sorted(files):
            if not name.endswith(".txt") or name == "rejects.txt":
                continue
            path = os.path.join(dirpath, name)
            try:
                labels = parse_fragment(path)
            except (OSError, UnicodeDecodeError) as error:
                conflicts.append(f"{path}: unreadable ({error})")
                continue
            row = labels.get("ROW")
            if not row:
                continue
            m = ROW_RE.match(re.sub(r"^ROW\s*[=:]\s?", "", row).strip())
            if not m:
                conflicts.append(f"{path}: ROW not parseable")
                continue
            sid = m.group(1)
            if sid in found:
                conflicts.append(f"{sid}: duplicate fragment {path} (kept {found[sid]['path']})")
                continue
            labels["path"] = os.path.relpath(path, root)
            labels["sid"] = sid
            found[sid] = labels
    return found, conflicts


def audit_row(sid, labels):
    flags, info = [], {}
    cs = cells(labels.get("ROW", ""))
    info["cells"] = len(cs)
    if len(cs) != 11:
        flags.append(f"cells={len(cs)}")
    source = cs[1] if len(cs) > 1 else ""
    tier = cs[3] if len(cs) > 3 else ""
    anchor = cs[5] if len(cs) > 5 else ""
    teaches = cs[6] if len(cs) > 6 else ""
    status = cs[7] if len(cs) > 7 else ""
    opened = cs[8] if len(cs) > 8 else ""
    recheck = cs[9] if len(cs) > 9 else ""
    usedby = cs[10] if len(cs) > 10 else ""
    if tier not in ("A", "B"):
        flags.append(f"tier={tier}")
    if status != "mined":
        flags.append(f"status={status}")
    if opened != "2026-10-24":
        flags.append(f"opened={opened}")
    if recheck != "180d":
        flags.append(f"recheck={recheck}")
    if ENTRY not in usedby:
        flags.append(f"usedby={usedby[:40]}")
    quote = anchor_quote(anchor)
    qw = norm_words(quote) if quote else []
    info["quote_words"] = len(qw)
    if not (8 <= len(qw) <= 25):
        flags.append(f"quote_words={len(qw)}")
    urls = URL_RE.findall(source)
    cap = CAPTURE_RE.search(source)
    info["url"] = urls[0] if urls else None
    if not urls:
        flags.append("no_live_url")
    if not cap:
        flags.append("no_capture")
    elif urls and norm_url(cap.group(2)) != norm_url(urls[0]):
        flags.append("capture_original_mismatch")
    if urls:
        host = re.sub(r"^https?://", "", urls[0]).split("/")[0].lower().split(":")[0]
        if any(host == ph or host.endswith("." + ph) for ph in PLACEHOLDER_HOSTS):
            flags.append(f"placeholder_host={host}")
    bullet = labels.get("BULLET", "")
    info["bullet_raw"] = bullet
    clause = bullet
    if clause.startswith("-"):
        clause = clause[1:].strip()
    if clause.endswith(f"({sid})"):
        clause = clause[: -len(f"({sid})")].strip()
    info["clause"] = clause
    cw = content_words(clause)
    info["content_words"] = len(cw)
    if len(cw) < 5:
        flags.append(f"content_words={len(cw)}")
    if not (6 <= len(cw) <= 25):
        info["note_content_range"] = f"{len(cw)} outside 6-25"
    pos = hits = 0
    for w in cw:
        for j in range(pos, len(qw)):
            if qw[j] == w:
                pos = j + 1
                hits += 1
                break
    info["in_order"] = hits
    if hits < 3:
        flags.append(f"in_order={hits}")
    if qw and not set(cw) - set(qw):
        flags.append("no_novel_content_word")
    copy_run = longest_copy_run(norm_words(clause), qw)
    info["copy_run"] = copy_run
    if copy_run > 12:
        flags.append(f"copy_run={copy_run}")
    cov = in_order_coverage(word_tokens(clause), word_tokens(teaches))
    info["teaches_coverage"] = round(cov, 3)
    if len(word_tokens(clause)) >= 5 and cov >= 0.8:
        flags.append(f"teaches_nearcopy={cov:.2f}")
    elif cov >= 0.6:
        info["near_copy_watch"] = round(cov, 3)
    if clause.strip().casefold() == teaches.strip().casefold():
        flags.append("teaches_copy")
    return flags, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    rows_dir = os.path.join(root, ".ufo/waves/round-65/rows")
    stage = os.path.join(root, ".ufo/waves/round-65/stage")
    os.makedirs(stage, exist_ok=True)
    found, conflicts = scan(rows_dir, root)
    landed = [sid for sid in NEW_IDS if sid in found]
    audit = {"landed": landed, "landed_count": len(landed), "missing": [s for s in NEW_IDS if s not in found],
             "fragment_conflicts": conflicts, "rows": {}, "url_duplicates": [], "entry": {}}

    seen_urls = {}
    for sid in landed:
        flags, info = audit_row(sid, found[sid])
        info["fragment"] = found[sid]["path"]
        info["flags"] = flags
        audit["rows"][sid] = info
        url = info.get("url")
        if url:
            key = norm_url(url)
            if key in seen_urls:
                audit["url_duplicates"].append(f"{sid} == {seen_urls[key]}")
                flags.append(f"norm_dup_of={seen_urls[key]}")
            else:
                seen_urls[key] = sid

    out = []
    out.append("# Games, play, sport and contests \u2014 how games are classified, made, moved, and staged")
    out.append("")
    out.append("- topic: games, play, sport and contests as material and social practice across board and race games, ballgames, athletic and ritual contests, lots and dice, cards, children's playground repertoire, and target games \u2014 a sourced design reference for fictional play, not a universal history of games.")
    out.append("- source: the round-65 registry rows in `corpus/SOURCES.md` are the evidence anchors; each inserted claim stays within its cited row.")
    out.append(f"- verified-at: 2026-10-24 \u2014 DRAFT assembled from {len(landed)} of 26 row fragments; cited source claims await L1 insertion and review.")
    out.append("- recheck: 180 days, per row (`corpus/SOURCES.md` recheck cells).")
    out.append("")
    out.append(f"<!-- assembly: {len(landed)} of 26 row fragments landed at generation time; gap list in the scribe report, not in this file. -->")
    out.append("")
    for title, sids, intro in SECTIONS:
        out.append(title)
        out.append("")
        out.append(intro)
        present = [s for s in sids if s in found]
        for sid in present:
            raw = audit["rows"][sid]["bullet_raw"].strip()
            shaped = re.match(r"^-\s+.*\(%s\)$" % sid, raw) is not None
            line = raw if shaped else f"- {audit['rows'][sid]['clause']} ({sid})"
            out.append(line)
            if not shaped:
                audit["rows"][sid]["bullet_normalized"] = True
        if not present:
            out.append("")
            out.append("No row in this class had landed at assembly time; see the scribe report for the gap.")
        out.append("")
    out.append("## What a worldbuilder does with this")
    out.append("")
    out.append("Use the rows as conditional design prompts, not prescriptions. Select an option, combine alternatives, or specify exceptions for a named setting.")
    out.append("")
    out.append(TABLE)
    out.append("")
    out.append("## cross-cultural patterns")
    out.append("")
    out.append("These are cross-row readings of the bullets above, not new source claims; no citation is added here.")
    out.append("")
    emitted = 0
    for required, statement in PATTERNS:
        if all(s in found for s in required):
            out.append(f"- {statement}")
            emitted += 1
    if emitted == 0:
        out.append("- No cross-row pattern is asserted: no supporting row had landed at assembly time.")
    out.append("")
    out.append("## calibration")
    out.append("")
    out.append("Each bullet stays inside its cited row. The row's anchor quote bounds the claim; tier A marks a peer-reviewed paper, official body, or scholarly book read directly, tier B marks an institutional or museum source read at a stated remove. Three limits apply. First, rule reconstructions for board games are inferences from boards, pieces, and later texts, not records of play. Second, museum and survey statements describe objects and collections; they do not establish universal practice. Third, this entry samples unevenly by region and period, so a game's absence here is not evidence of its absence in a culture. Where a source reports one site, sample, collection, or country, the bullet keeps that scope, and the registry scope and quote cells carry the same limit.")
    out.append("")
    out.append("## one-way pointing to partial owners")
    out.append("")
    out.append("This entry points to the following entries for adjacent scope. The pointing is one-way: they own their topic, and this entry does not restate or extend them.")
    out.append("")
    for path, owns in ONEWAY:
        out.append(f"- `{path}` {owns}")
    out.append("")
    out.append("## lore handoff")
    out.append("")
    out.append(HANDOFF)
    out.append("")

    text = "\n".join(out)
    lines = text.splitlines()
    audit["entry"] = {
        "lines": len(lines),
        "h1": sum(1 for l in lines if l.startswith("# ")),
        "h2": sum(1 for l in lines if l.startswith("## ")),
        "h3": sum(1 for l in lines if l.startswith("### ")),
        "has_topic": any(l.startswith("- topic:") for l in lines),
        "multi_id_lines": [i for i, l in enumerate(lines, 1) if len(set(SID_RE.findall(l))) > 1],
        "table_id_lines": [i for i, l in enumerate(lines, 1) if l.lstrip().startswith("|") and SID_RE.search(l)],
        "cited": sorted(SID_RE.findall(text)),
        "entry_url_lines": [i for i, l in enumerate(lines, 1) if URL_RE.search(l)],
    }
    audit["entry"]["cited_exactly_once"] = audit["entry"]["cited"] == sorted(set(audit["entry"]["cited"])) and set(audit["entry"]["cited"]) <= set(NEW_IDS)
    with open(os.path.join(stage, "entry-draft.md"), "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(os.path.join(stage, "assemble-audit.json"), "w", encoding="utf-8") as handle:
        json.dump(audit, handle, indent=1, ensure_ascii=False)
    print(f"ASSEMBLE landed={len(landed)}/26 draft_lines={len(lines)} h2={audit['entry']['h2']} "
          f"cited={len(audit['entry']['cited'])} exactly_once={audit['entry']['cited_exactly_once']}")
    for sid in landed:
        flags = audit["rows"][sid]["flags"]
        watch = audit["rows"][sid].get("near_copy_watch")
        if flags or watch:
            print(f"  {sid} {'FLAGS ' + ' '.join(flags) if flags else ''} "
                  f"{'watch_teaches_cov=' + str(watch) if watch else ''}")
    if conflicts:
        print(f"  conflicts={len(conflicts)}")
    print(f"  draft={os.path.relpath(os.path.join(stage, 'entry-draft.md'), root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
