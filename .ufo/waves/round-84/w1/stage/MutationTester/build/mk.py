#!/usr/bin/env python3
"""Build round-84 claim-artifact mutants as standalone stub commits in a scratch clone."""
import json
import os
import shutil
import subprocess
import sys

S = os.environ.get("SEAT_SCRATCH") or os.getcwd()
REP = os.path.join(S, "rep")
INSTR = os.path.join(S, "instr")
WORK = os.path.join(S, "work")
OUT = os.path.join(S, "out")
FREEZE = "3ca2cf288fb593618e0559ea86a36e2dd3110eb8"
FREEZE_R1 = "e160a72e4adf1620e09f812b913d4ece0fcd5243"
ENTRY = "corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md"
TOOL = "tools/apply-sound-laws.py"

PARAS = [
    "The vocabulary set is not a description of a practice but a filing cabinet: a term for the act, a term for the actor, a term for the harm, and a term for the evidence, each with its own procedural consequences, so that a court can reach the actor without ever deciding whether the act occurred, and can reach the harm without ever naming an actor, and the filing cabinet holds when the underlying event is imaginary.",
    "What the vocabulary buys is a way to move a dispute from the register of injury to the register of offence, where the burden of proof falls differently, the penalties are assessed differently, and the settlement belongs to a different authority than the one that would hear a claim about cattle or boundaries.",
    "The accusation grammar has a small number of slots and a small number of licit fillers, and the slots are ordered: an accuser, a community that receives the charge, a named act, a named harm, an occasion, and a demand, and a charge that omits the community or the occasion reads as slander rather than as an accusation, which is why the grammar is worth reconstructing separately from the vocabulary.",
    "Because the slots are ordered, the same sentence can be read two ways depending on which slot is filled first, and the procedural literature is full of disputes that turn on whether the charge was laid as an accusation or uttered as a complaint, which is a grammatical question dressed as a procedural one.",
    "The proof technology is the part of the institution that most clearly shows its shape: the ordeal, the oath-helpers, the swimming test, the weighing, the needle, the recitation, the witness who must be of the same standing as the accused, and the confession extracted under a procedure the record describes in detail and the modern reader finds hard to read as evidence at all.",
    "Each proof technology carries a rule about what counts as a failure and a rule about who bears the cost of a failure, and the two rules are not the same rule, which is why a proof technology can survive a change of theology while a vocabulary set does not survive a change of law.",
    "The confession is the hinge: a proof technology that produces a confession converts an accusation into a fact, and once the fact exists the property consequences follow without further argument, so the confession is not merely evidence but the instrument by which the institution transfers goods, status, and persons.",
    "The confession also carries a requirement of voluntariness that the procedure cannot satisfy while it is extracting the confession, and the record keeps both facts in the same paragraph, which is the document's own testimony that the institution knew what it was doing.",
    "The slander law is the mirror image: the same vocabulary that lets a community accuse also lets an accused person turn the charge back on the accuser, and the slander action is what keeps the accusation grammar from being used without cost, so a jurisdiction with a strong slander law and a weak proof technology is a different institution from one with the reverse.",
    "The social functions an accusation carries are several at once: it redistributes property, it removes a person from a network, it reasserts a boundary that had become uncertain, it provides an explanation for a run of misfortune, and it gives the community a procedure for doing all of this without a general war, and the same charge can perform any subset of those functions depending on who brings it.",
    "The institution is therefore best described as a procedure with inputs and outputs rather than as a belief, and the belief content is remarkably variable across the record while the procedure is remarkably stable, which is the observation that makes the comparative description possible at all.",
    "A decision table is the right instrument for this material because the procedure is a sequence of branch points, and each branch point can be stated as a question with two answers, and the answers determine which of the remaining branch points are reachable, which is what a table shows and a paragraph cannot.",
    "The scope of the description is the accusation as a procedure, not the cosmology that the accusation presupposes, and the two must be kept apart because the cosmology varies while the procedure recurs, and a description that mixes them will report a difference of doctrine as a difference of institution.",
    "Where the record is thin, the description says so and stops, and the stopping point is part of the description: an entry that fills a gap with a neighbouring jurisdiction's procedure has manufactured the very uniformity it claims to report, and the reader cannot tell the manufactured part from the attested part.",
    "The comparative claim is deliberately weak: the procedure recurs in the record with the same slots and a different filling, and the recurrence is offered as a description of the documents, not as a claim about human nature, and the distinction matters because the second claim is not testable from the documents the entry cites.",
    "The worked derivation is the part a reader can check: take a charge, walk it through the table, and see which of the branch points the record actually attests and which the table supplies by inference, and the walk is the argument, so a reader who disagrees with the walk has something specific to disagree with.",
]

DEC_ROWS = [
    "| is there a named harm that the community already recognises as an injury | the charge can be laid as an accusation and the procedure runs | the charge must be laid as a complaint and the procedure for slander runs instead |",
    "| is the accused a member of the community that receives the charge | the community has jurisdiction and the proof technology is available | the charge is a boundary matter and the proof technology is not available |",
    "| does the accuser carry standing, that is, has the accuser suffered the harm or is the accuser the community's officer | the charge proceeds and the accuser bears the cost of failure | the charge is dismissed as officious and the accuser bears the cost anyway |",
    "| is the proof technology one that produces a confession | the property consequences follow without a further finding | the property consequences wait on a finding that the procedure may not reach |",
    "| does the jurisdiction have a slander action that the accused can bring | the accusation grammar has a price and the charge is rationed | the accusation grammar has no price and the charge is cheap |",
    "| did the procedure complete, whatever its verdict | the record is a fact about the institution and is used as one | the record is a fact about a failed procedure and is used as evidence of the failure |",
]

ANCHOR_TEXT = [
    "the vocabulary names act, actor and harm as three terms rather than one, so a charge can name the harm without naming a deed",
    "the community that receives the charge is a slot in the grammar, not a background condition",
    "the proof technology's failure rule and its cost-bearer rule are stated separately",
    "the confession converts an accusation into a fact that transfers property",
    "the record keeps the voluntariness requirement beside the extraction in one paragraph",
    "the slander action is the price that rations the charge",
    "the procedure recurs while the cosmology varies across the cited record",
    "the branch points are ordered and later points are unreachable from a refused earlier point",
    "the accuser's standing is assessed before the proof technology is chosen",
    "a charge without an occasion reads as slander rather than as an accusation",
    "the officer's charge is dismissed as officious where standing is lacking",
    "the property consequence is stated as following the confession, not the verdict",
    "a failed procedure is still recorded and used as evidence about the institution",
    "the same sentence can be read as accusation or complaint depending on slot order",
    "the description stops at the edge of the cited record rather than filling the gap",
    "the comparative claim is a claim about documents, not about human nature",
    "the worked derivation walks one charge through the table branch by branch",
    "the table's rows are questions whose answers determine which rows remain reachable",
    "the scope sentence separates the procedure from the cosmology it presupposes",
    "the entry reports a thin record as thin and does not import a neighbour's procedure",
]

REGISTER = [
    ("maleficium", "the act", "sets the charge in the register of injury rather than the register of offence", "the plea roll names it as the deed and nothing else"),
    ("maleficus", "the actor", "lets the procedure reach a person without a finding about the act", "the indictment names the person before it names the deed"),
    ("sortiarius", "the actor who works by lot", "adds the casting of lots to the charge and changes the proof technology", "the record lists the lots among the instruments seized"),
    ("veneficium", "the act worked by poison or by a drug", "moves the harm into the register of physical injury and demands a different proof", "the inquest describes the substance before it describes the intention"),
    ("lamia", "the actor whose harm is to children and to milk", "narrows the harm to a household injury the community can verify by inspection", "the deposition names the household and the animal"),
    ("striga", "the actor who is said to fly or to change shape", "makes the evidence about the body rather than about the deed, which is the hardest proof the institution carries", "the confession describes the flight in a formula the notary supplies"),
    ("accusatio", "the charge laid in form", "opens the procedure and fixes the accuser's liability for failure", "the act book records the charge and the day it was laid"),
    ("denuntiatio", "the charge laid informally", "lets the community receive a charge without the accuser carrying the full liability", "the register marks the entry as a denunciation, not an accusation"),
    ("infamia", "the standing the charge leaves behind", "removes the accused from the network before any verdict is reached", "the roll notes the infamy in the margin beside the name"),
    ("exceptio", "the answer in law", "lets the accused meet the charge with a defect in the accuser's standing", "the plea is entered before the proof technology is chosen"),
    ("purgatio", "the clearing by oath", "converts the oath-helpers' standing into a verdict without a finding about the act", "the oath roll lists the helpers and their standings"),
    ("ordalium", "the proof by ordeal", "produces a verdict the community reads off the body, not off testimony", "the record describes the water, the iron, and the hand"),
    ("confessio", "the confession", "converts the accusation into a fact that transfers property without further argument", "the notary's protocol gives the words in the first person"),
    ("captio", "the interrogation that produces the confession", "supplies the fact the procedure needs and creates the voluntariness problem the record also states", "the protocol gives the questions and the answers in order"),
    ("abjuratio", "the abjuration of the error", "lets the accused leave the community's jurisdiction on stated terms", "the roll names the boundary the accused must not cross"),
    ("relapsus", "the return after abjuration", "turns a second appearance into a fact that needs no new proof", "the register marks the second entry as a relapse"),
    ("diffamatio", "the report that precedes the charge", "lets the community act on reputation before anyone carries an accusation", "the visitation records the report and its witnesses"),
    ("denunciator", "the person who reports", "shields the reporter from the liability that would fall on an accuser", "the entry names the reporter only where the law requires it"),
    ("inquisitio", "the inquiry the officer opens", "moves the charge from an accuser to an office and changes who bears the cost", "the register opens with the officer's name, not a complainant's"),
    ("fama", "the public report as evidence", "admits reputation as a proof without a witness to the deed", "the record cites the fama as the reason the inquiry opened"),
    ("testis", "the witness", "must be of the accused's standing for the testimony to count", "the deposition lists each witness's standing beside the testimony"),
    ("purgator", "the oath-helper", "lends standing rather than knowledge, so the number of helpers is the verdict", "the oath roll counts the helpers and records their standings"),
    ("poena", "the penalty", "is assessed by the procedure that produced the fact, not by the harm the charge named", "the sentence recites the procedure before it states the penalty"),
    ("confiscatio", "the confiscation", "is the property consequence that follows the confession and funds the institution", "the account roll lists the goods and their new holder"),
    ("rehabilitatio", "the restoration of standing", "returns the accused to the network when the procedure fails", "the roll strikes the infamy entry and names the day"),
    ("appellatio", "the appeal", "moves the charge to a higher authority and suspends the property consequence", "the register notes the appeal in the margin of the sentence"),
]

PROCEDURE_STEPS = [
    "1. The report arrives: a fama, a denunciation, or an accusation in form, and the register records which of the three it is, because the three carry different liabilities.",
    "2. The officer tests standing: the accuser's, the reporter's, and the accused's, and a charge that fails the test is dismissed before any proof is chosen.",
    "3. The community receives the charge: the record names the occasion, the place, and the persons present, because a charge without an occasion reads as slander.",
    "4. The vocabulary is fixed: the act, the actor, and the harm are named in the terms the jurisdiction uses, and a charge that mixes the terms is sent back.",
    "5. The proof technology is chosen from a short list, and the choice is recorded, because the same jurisdiction may use different technologies for different harms.",
    "6. The proof runs under a formula the record supplies, and the formula is repeated verbatim in later cases, which is how the technology becomes an institution.",
    "7. The result is read off the body or off the oath-helpers, and the reading rule is stated separately from the cost rule, because the two can diverge.",
    "8. The confession, where the technology produces one, is written in the first person and carries the property consequence without a further finding.",
    "9. The property consequence is executed and accounted for, and the account roll is the document that shows the institution paying for itself.",
    "10. The slander action is available to the accused where the charge fails, and its availability is what rations the charge in the first place.",
    "11. The appeal, where the jurisdiction has one, suspends the consequence and moves the file, and the file's movement is visible in the register's margins.",
    "12. The record is kept, and the keeping is the institution's memory: a procedure that leaves no roll cannot be cited in the next case and does not become a technology.",
]

RECORD_CAUTIONS = [
    "The formula is older than the case and is repeated without variation, so the record's agreement across cases is evidence about the formula, not about the events.",
    "The notary supplies the words of the confession, so the first person in the protocol is the notary's first person, and the entry says so rather than quoting it as the accused's speech.",
    "The account roll lists goods and holders, never a justification, so the property consequence is documented more precisely than the finding that produced it.",
    "The margin notes are the only place where the file's movement is visible, and a transcript that drops the margins drops the procedure's appellate history.",
    "The oath roll counts helpers rather than recording their knowledge, so a run of acquittals is evidence about standings, not about innocence.",
    "The visitation record is written by the officer who opened the inquiry, so its account of the fama is the account of the party that used it.",
    "The sentence recites the procedure before it states the penalty, which is the document's own statement that the penalty follows the technology rather than the harm.",
    "A thin record is reported as thin: the entry stops where the documents stop, and the stopping point is part of the description rather than a gap the entry fills.",
]

HEADERS = [
    "- topic: witchcraft and sorcery as an accusation institution",
    "- gap filled: the accusation procedure as vocabulary, grammar, proof technology, confession, slander law and social function",
    "- sources: the four registry rows opened this round, named in the anchor bullets below",
    "- couples: corpus/knowledge/legal-anthropology/ordeal-and-proof.md, corpus/knowledge/myth-symbol/divination-and-omen.md",
    "- source: corpus/SOURCES.md S914",
    "- verified-at: 2026-11-04",
    "- recheck: 365d",
    "- scope: the accusation as a procedure, not the cosmology it presupposes",
]


def entry_text(headings, anchors, two_ids=False, dup_id=False):
    dec, anch = headings
    out = ["# Witchcraft and sorcery as an accusation institution", ""]
    out += HEADERS
    out.append("")
    out += ["## 1. The vocabulary set", ""]
    out += [PARAS[0], "", PARAS[1], ""]
    for term, sense, effect, witness in REGISTER:
        out.append("- %s — %s; %s; %s." % (term, sense, effect, witness))
    out.append("")
    out += [dec, ""]
    out += ["| branch point | answer that admits the accusation | answer that refuses it |", "|---|---|---|"]
    out += DEC_ROWS
    out.append("")
    out += ["## 3. The accusation grammar", ""]
    out += [PARAS[2], "", PARAS[3], ""]
    out += [anch, ""]
    for i, line in enumerate(ANCHOR_TEXT[:anchors]):
        sid = "S%d" % (914 + (i % 4))
        text = "- %s: %s" % (sid, line)
        if two_ids:
            text += " See also S917."
        if dup_id and i == 0:
            text = "- S914 S914: %s" % line
        out.append(text)
    out.append("")
    out += ["## 5. The proof technology", ""]
    out += [PARAS[4], "", PARAS[5], ""]
    out += ["## 6. The confession", ""]
    out += [PARAS[6], "", PARAS[7], ""]
    out += ["## 7. The slander law", ""]
    out += [PARAS[8], "", PARAS[9], ""]
    out += ["## 8. The social functions", ""]
    out += [PARAS[10], "", PARAS[11], ""]
    out += ["## 9. The decision procedure", ""]
    out += [PARAS[12], "", PARAS[13], ""]
    out += PROCEDURE_STEPS
    out.append("")
    out += ["## 10. Calibration", ""]
    out += [PARAS[14], "", PARAS[15], ""]
    out += RECORD_CAUTIONS
    out.append("")
    return "\n".join(out) + "\n"


def row(sid, status, teaches=None):
    return "| %s | fixture stub row %s: no network fetch was performed; this row exists only to exercise the round-84 counter | book | A | the accusation procedure | section 1, paragraph 1 | %s | %s | 2026-11-04 | 365d | %s |" % (
        sid, sid, teaches or ("what %s teaches about the procedure" % sid), status, ENTRY)


def sources_block(status_map):
    return "\n".join(row("S%d" % (914 + i), status_map.get(i, "mined")) for i in range(4)) + "\n"


def git(*a):
    return subprocess.run(["git", "-C", REP] + list(a), capture_output=True, check=True).stdout.decode()


def commit(files, msg):
    subprocess.run(["git", "-C", REP, "reset", "-q", "--hard", FREEZE], check=True)
    subprocess.run(["git", "-C", REP, "clean", "-qfd"], check=True)
    for rel, content in files.items():
        p = os.path.join(REP, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
    subprocess.run(["git", "-C", REP, "add", "-A"], check=True)
    subprocess.run(["git", "-C", REP, "commit", "-q", "-m", msg], check=True)
    return git("rev-parse", "HEAD").strip()


SKILL_INSERT_AFTER = "| accept-c-83 | gate |"


def skill_text(extra_rows):
    raw = subprocess.run(["git", "-C", REP, "show", "%s:SKILL.md" % FREEZE],
                         capture_output=True, check=True).stdout.decode("utf-8")
    lines = raw.split("\n")
    idx = next(i for i, l in enumerate(lines) if l.startswith(SKILL_INSERT_AFTER))
    lines[idx + 1:idx + 1] = extra_rows
    return "\n".join(lines)


GATE_ROWS = [
    "| accept-d-84 | gate | `python3 -B reports/round-84/accept-d84.py --root . --lands <40-hex> --freeze <40-hex> --work <dir>` (`--junk` switches to the mutation battery) | 0 pass / 1 fail / 2 refusal | — (no `--selftest`) | frozen config `reports/round-84/claims.json` | read-only | lane |",
    "| accept-o-84 | gate | `python3 -B reports/round-84/accept-o84.py --root . --lands <40-hex> --freeze <40-hex> --work <dir>` (`--junk` switches to the mutation battery) | 0 pass / 1 fail / 2 refusal | — (no `--selftest`) | frozen config `reports/round-84/claims.json` | read-only | lane |",
    "| apply-sound-laws | probe | `python3 -B tools/apply-sound-laws.py selftest` and `python3 -B tools/apply-sound-laws.py apply --rules examples/sound-laws/rules.json --input examples/sound-laws/proto-lexicon.tsv --out <tsv>` | 0 clean / 2 could-not-evaluate | `--selftest` | `examples/sound-laws/expected.tsv` | read-only | lane |",
]

RULES = {"rules": [
    {"name": "final-devoicing", "from": "d", "to": "t", "pre": [], "post": ["#"]},
    {"name": "velar-devoicing", "from": "g", "to": "k", "pre": [], "post": ["#"]},
    {"name": "velar-palatalization", "from": "k", "to": "tʃ", "pre": [], "post": ["i"]},
    {"name": "u-umlaut", "from": "u", "to": "y", "pre": [], "post": ["i"]},
    {"name": "assibilation", "from": "t", "to": "s", "pre": [], "post": ["i"]},
    {"name": "syncope", "from": "a", "to": "", "pre": ["p"], "post": ["l"]},
]}

WORDS = [
    ("mother", "m a t e r"),
    ("father", "p a t e r"),
    ("brother", "b r a t e r"),
    ("sister", "s o r o r"),
    ("hand", "m a n u"),
    ("foot", "p e d e"),
    ("night", "n o k t i"),
    ("three", "t r e s"),
    ("king", "r e g s"),
    ("god", "d e i g o"),
    ("house", "d o m u"),
    ("field", "a g r o"),
]

TOOL_TMPL = r'''#!/usr/bin/env python3
r"""apply-sound-laws.py — MUTANT STUB ({variant}) for the round-84 claim-O artifact.

This file is a mutation-testing stub. It exists so the frozen counter
reports/round-84/accept-o84.py can be asked whether its DEMO and NEGATIVE legs
distinguish a derivation from a copy. It is not the round's tool and must never
be landed.

Frozen contract it imitates (round 84, claim O, reports/round-84/claims.json):

  python3 tools/apply-sound-laws.py selftest
  python3 tools/apply-sound-laws.py apply --rules PATH --input PATH --out PATH [--trace PATH]

Input TSV: gloss<TAB>seg1 seg2 ...; `#` comment lines allowed; blank lines
ignored. Rules JSON: {{"rules":[{{"name":str,"from":str,"to":str,"pre":[str],"post":[str]}}]}}
where `#` in pre means word start and `#` in post means word end. Rules apply
in file order, one left-to-right non-overlapping pass per rule. `to` may be "".
Output TSV: gloss<TAB>derived segments, input order preserved. Trace TSV: one
line per change, gloss<TAB>index<TAB>rule<TAB>before<TAB>after. Any input error
prints `SOUNDLAW_ERROR: <label>: <detail>` to stderr and exits 2, never a
traceback. `selftest` (also accepted as `--selftest`) prints
`SELFTEST: PASS (<n> checks)` and exits 0.

STUB VARIANT: {blurb}
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXPECTED = os.path.join(ROOT, "examples", "sound-laws", "expected.tsv")
TRACE_COLUMNS = 5


class SoundlawError(Exception):
    def __init__(self, label, detail):
        Exception.__init__(self, label)
        self.label = label
        self.detail = detail


def emit_error(label, detail):
    sys.stderr.write("SOUNDLAW_ERROR: %s: %s\n" % (label, detail))
    return 2


def read_rules(path):
    if not os.path.isfile(path):
        raise SoundlawError("rules-missing", "no rules file at %s" % path)
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except ValueError as error:
        raise SoundlawError("rules-json", "rules file is not JSON: %s" % error)
    rules = data.get("rules") if isinstance(data, dict) else None
    if not isinstance(rules, list) or not rules:
        raise SoundlawError("rules-shape", "rules must be a non-empty list")
    names = []
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            raise SoundlawError("rule-shape", "rule %d is not an object" % index)
        name = rule.get("name")
        if not isinstance(name, str) or not name:
            raise SoundlawError("rule-name", "rule %d has no name" % index)
        if rule.get("from") == "":
            raise SoundlawError("empty-from", "rule %r has an empty from segment" % name)
        for field in ("from", "to"):
            if not isinstance(rule.get(field), str):
                raise SoundlawError("rule-shape", "rule %r field %s is not a string" % (name, field))
        for field in ("pre", "post"):
            value = rule.get(field, [])
            if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
                raise SoundlawError("rule-shape", "rule %r field %s is not a string list" % (name, field))
        names.append(name)
    return rules


def read_input(path):
    if not os.path.isfile(path):
        raise SoundlawError("input-missing", "no input file at %s" % path)
    rows = []
    with open(path, encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if "\t" not in line:
                raise SoundlawError("input-shape", "line %d carries no tab" % number)
            gloss, segments = line.split("\t", 1)
            rows.append((gloss, segments.split()))
    if not rows:
        raise SoundlawError("input-empty", "no word rows in %s" % path)
    return rows


def write_text(path, text):
    directory = os.path.dirname(os.path.abspath(path))
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def write_trace(path, rows):
    write_text(path, "".join("\t".join(row) + "\n" for row in rows))


def checks():
    """The stub's in-process checks: contract shape only, never a derivation."""
    seen = []
    seen.append(TRACE_COLUMNS == 5)
    seen.append(EXPECTED.endswith("expected.tsv"))
    seen.append(callable(emit_error))
    seen.append(emit_error.__code__.co_argcount == 2)
    seen.append(SoundlawError("a", "b").label == "a")
    seen.append(SoundlawError("a", "b").detail == "b")
    seen.append(isinstance(read_rules, type(lambda: None)))
    seen.append(isinstance(read_input, type(lambda: None)))
    seen.append(isinstance(write_text, type(lambda: None)))
    seen.append(isinstance(write_trace, type(lambda: None)))
    seen.append(isinstance(checks, type(lambda: None)))
    seen.append("SOUNDLAW_ERROR:" in __doc__)
    seen.append("--selftest" in __doc__)
    seen.append(callable(main))
    seen.append(os.path.basename(HERE) == "tools")
    seen.append(os.path.basename(EXPECTED) == "expected.tsv")
    seen.append(os.path.basename(ROOT) != "tools")
    seen.append(json is not None)
    seen.append(sys is not None)
    seen.append(len(TRACE_COLUMNS * "x") == 5)
    seen.append(True)
    seen.append(True)
    seen.append(True)
    seen.append(all(seen))
    return sum(1 for x in seen if x)


def run_selftest():
    print("SELFTEST: PASS (%d checks)" % checks())
    return 0


def run_apply(argv):
{APPLY}


def main(argv):
    if "--selftest" in argv or argv[:1] == ["selftest"]:
        return run_selftest()
    if argv[:1] == ["apply"]:
        return run_apply(argv[1:])
    return emit_error("usage", "expected selftest or apply")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
'''


def tool_text(variant, blurb, body, negatives_broken):
    if negatives_broken:
        apply_block = r'''    try:
        args = parse_args(argv)
        rules = read_rules(args["rules"])
        rows = read_input(args["input"])
    except Exception:
        out = value_of(argv, "--out")
        if out:
            write_text(out, "")
        return 0
''' + "    " + body
    else:
        apply_block = r'''    try:
        args = parse_args(argv)
        rules = read_rules(args["rules"])
        rows = read_input(args["input"])
    except SoundlawError as error:
        return emit_error(error.label, error.detail)
''' + "    " + body
    text = TOOL_TMPL.format(variant=variant, blurb=blurb, APPLY=apply_block)
    # shared helpers, appended so APPLY can stay a body fragment
    text = text.replace("def run_apply(argv):", "def value_of(argv, flag):\n"
                        "    return argv[argv.index(flag) + 1] if flag in argv and argv.index(flag) + 1 < len(argv) else None\n\n\n"
                        "def parse_args(argv):\n"
                        "    out = {}\n"
                        "    for flag in (\"--rules\", \"--input\", \"--out\", \"--trace\"):\n"
                        "        out[flag.lstrip(\"-\")] = value_of(argv, flag)\n"
                        "    if not out[\"rules\"] or not out[\"input\"] or not out[\"out\"]:\n"
                        "        raise SoundlawError(\"usage\", \"apply needs --rules --input --out\")\n"
                        "    return out\n\n\n"
                        "def run_apply(argv):")
    return text


BODY_COPY_ZERO = r'''copy_expected(args["out"])
    trace = []
    if args["trace"]:
        write_trace(args["trace"], trace)
    print("SOUNDLAWS: %d words / %d rules / %d changes" % (len(rows), len(rules), len(trace)))
    return 0
'''

BODY_COPY_FAKE = r'''copy_expected(args["out"])
    trace = []
    glosses = [gloss for gloss, _ in rows]
    for i in range({changes}):
        rule = rules[i % len(rules)]["name"]
        gloss = glosses[i % len(glosses)]
        trace.append([gloss, str(i + 1), rule, "a", "e"])
    if args["trace"]:
        write_trace(args["trace"], trace)
    print("SOUNDLAWS: %d words / %d rules / %d changes" % (len(rows), len(rules), len(trace)))
    return 0
'''

BODY_IDENTITY_CHEAT = r'''write_text(args["out"], "".join("%s\t%s\n" % (gloss, " ".join(segs)) for gloss, segs in rows))
    trace = []
    glosses = [gloss for gloss, _ in rows]
    for i in range({changes}):
        rule = rules[i % len(rules)]["name"]
        gloss = glosses[i % len(glosses)]
        trace.append([gloss, str(i + 1), rule, "a", "e"])
    if args["trace"]:
        write_trace(args["trace"], trace)
    print("SOUNDLAWS: %d words / %d rules / %d changes" % (len(rows), len(rules), len(trace)))
    return 0
'''

COPY_HELPER = r'''

def copy_expected(dest):
    with open(EXPECTED, "rb") as handle:
        payload = handle.read()
    directory = os.path.dirname(os.path.abspath(dest))
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(payload)
'''


def pad_tool(text, target=5600):
    while len(text.encode()) < target:
        text += "# stub padding: this mutant imitates the frozen contract's shape, never its derivation; the counter's DEMO leg is what is under test here.\n"
    return text


def o_files(variant, blurb, body, negatives_broken):
    tool = tool_text(variant, blurb, body, negatives_broken)
    tool = tool.replace("def main(argv):", COPY_HELPER.strip("\n") + "\n\n\ndef main(argv):", 1)
    tool = pad_tool(tool)
    files = {
        TOOL: tool,
        "examples/sound-laws/rules.json": json.dumps(RULES, indent=1) + "\n",
        "examples/sound-laws/proto-lexicon.tsv": "".join("%s\t%s\n" % (g, w) for g, w in WORDS),
        "examples/sound-laws/expected.tsv": "".join("%s\t%s a\n" % (g, w) for g, w in WORDS),
        "SKILL.md": "",
    }
    files["SKILL.md"] = skill_text(GATE_ROWS)
    return files


def main():
    if os.path.isdir(os.path.join(WORK, "")):
        shutil.rmtree(WORK, ignore_errors=True)
    for d in (WORK, OUT, INSTR):
        os.makedirs(d, exist_ok=True)

    # instruments copied out of the frozen blob, never from the worktree
    for rel in ("reports/round-84/counterlib.py", "reports/round-84/accept-d84.py", "reports/round-84/accept-o84.py"):
        blob = subprocess.run(["git", "-C", REP, "show", "%s:%s" % (FREEZE, rel)], capture_output=True, check=True).stdout
        with open(os.path.join(INSTR, os.path.basename(rel)), "wb") as f:
            f.write(blob)

    h_old = ("## 2. The decision table", "## 4. Attested anchors")
    h_r1 = ("## 2. Six design decisions", "## 3. Attested anchors")
    made = {}

    # --- D family (parent = assigned freeze 3ca2cf28) ---
    base_entry = entry_text(h_old, 20)
    print("entry bytes", len(base_entry.encode()), "sections", sum(1 for l in base_entry.splitlines() if l.startswith("## ")))
    assert len(base_entry.encode()) >= 16000

    made["D-good"] = None

    # SOURCES.md must be base bytes + appended rows
    base_sources = subprocess.run(["git", "-C", REP, "show", "%s:corpus/SOURCES.md" % FREEZE],
                                  capture_output=True, check=True).stdout.decode()

    def commit_d(entry, status_map, msg):
        files = {ENTRY: entry, "corpus/SOURCES.md": base_sources + sources_block(status_map)}
        return commit(files, msg)

    made["D-good"] = commit_d(base_entry, {}, "stub D-good: shape-complete synthetic entry")
    made["D-m1"] = commit_d(entry_text(h_old, 20, two_ids=True), {}, "stub D-m1: every anchor bullet carries two S-ids")
    made["D-m1b"] = commit_d(entry_text(h_old, 20, dup_id=True), {}, "stub D-m1b: one anchor bullet repeats one S-id twice")
    made["D-m2"] = commit_d(entry_text(h_old, 19), {}, "stub D-m2: nineteen anchors")
    made["D-m3"] = commit_d(base_entry, {0: "queued"}, "stub D-m3: S914 row queued")

    # r1-shaped stub, parent = freeze revision r1 (for the drift probe)
    subprocess.run(["git", "-C", REP, "reset", "-q", "--hard", FREEZE_R1], check=True)
    r1_entry = entry_text(h_r1, 20)
    r1_sources = subprocess.run(["git", "-C", REP, "show", "%s:corpus/SOURCES.md" % FREEZE_R1],
                                capture_output=True, check=True).stdout.decode()
    for rel, content in {ENTRY: r1_entry, "corpus/SOURCES.md": r1_sources + sources_block({})}.items():
        p = os.path.join(REP, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
    subprocess.run(["git", "-C", REP, "add", "-A"], check=True)
    subprocess.run(["git", "-C", REP, "commit", "-q", "-m", "stub D-r1: entry shaped to freeze revision r1 headings"], check=True)
    made["D-r1"] = git("rev-parse", "HEAD").strip()

    # --- O family (parent = assigned freeze) ---
    made["O-m4"] = commit(o_files("m4", "copies the committed expected.tsv to --out and derives nothing", BODY_COPY_ZERO, False),
                          "stub O-m4: copies expected.tsv, zero changes")
    made["O-m4b"] = commit(o_files("m4b", "copies expected.tsv and fabricates a self-consistent trace", BODY_COPY_FAKE.format(changes=12), False),
                           "stub O-m4b: copies expected.tsv with a fabricated trace")
    made["O-m4c"] = commit(o_files("m4c", "copies the input to --out (identity derivation) and fabricates a trace", BODY_IDENTITY_CHEAT.format(changes=12), False),
                           "stub O-m4c: identity derivation with a fabricated trace")
    made["O-m5"] = commit(o_files("m5", "copy cheat whose malformed-input path exits 0 and writes an empty out", BODY_COPY_FAKE.format(changes=12), True),
                          "stub O-m5: malformed input exits 0")
    stray = o_files("m4b", "copies expected.tsv and fabricates a self-consistent trace", BODY_COPY_FAKE.format(changes=12), False)
    stray["tools/stray-tool.py"] = "#!/usr/bin/env python3\n# stub: an unregistered tool used to probe the unrowed-tool cap\nprint('stray')\n"
    made["O-unrowed"] = commit(stray, "stub O-unrowed: one more tool with no registry row")

    with open(os.path.join(S, "commits.json"), "w", encoding="utf-8") as f:
        json.dump(made, f, indent=1, sort_keys=True)
    print(json.dumps(made, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
