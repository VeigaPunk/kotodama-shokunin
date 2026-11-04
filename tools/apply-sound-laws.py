#!/usr/bin/env python3
r"""apply-sound-laws.py -- ordered sound-law applier over a segment proto-lexicon.

Kotodama round 84, claim O. One proto-era lexicon goes in; one derived-era
lexicon comes out, with an optional one-line-per-change record of every rule
firing. The tool is the mechanical half of the historical-linguistics section 7
procedure: "write an ordered law list ... derive daughter forms mechanically".

Usage:
  python3 tools/apply-sound-laws.py selftest
  python3 tools/apply-sound-laws.py --selftest
  python3 tools/apply-sound-laws.py apply --rules PATH --input PATH --out PATH
  python3 tools/apply-sound-laws.py --help    (prints the exact optional-log flag)

Input TSV (UTF-8): `gloss<TAB>seg1 seg2 ...`; a line whose first non-blank
character is `#` is a comment; blank lines are skipped. A record with an empty
segment field is refused.

Rules JSON:
  {"rules": [{"name": str, "from": str, "to": str, "pre": [str], "post": [str]}, ...]}
`from` is exactly one segment. `to` is zero or more space-separated segments;
"" deletes the matched segment. `pre` and `post` are the segments immediately
before and after the target; a leading "#" in `pre` anchors that context at the
word start and a trailing "#" in `post` anchors it at the word end. Rules apply
in file order. Each rule makes one left-to-right non-overlapping pass over the
current word, so a replacement is never rescanned by the rule that produced it
and a rule cannot feed itself. The derived lexicon keeps input order:
`gloss<TAB>derived segments`.

The change record is `gloss<TAB>index<TAB>rule<TAB>before<TAB>after`, one line
per replacement. `index` is the 0-based position in the current pass output
where the replacement is written; `before` is the matched segment; `after` is
the replacement ("" when the rule deletes).

Every input error prints `SOUNDLAW_ERROR: <label>: <detail>` on stderr and
exits 2 with no Python stack dump, before any output path is written. Stdlib
only: the tool reads only the paths named on the command line and writes only
--out and the optional log path.

Exit codes: 0 success, 1 selftest failure, 2 input error.
"""
import json
import os
import re
import sys

TAB = "\t"
ERROR_PREFIX = "SOUNDLAW_ERROR: "
SUMMARY_RE = r"^SOUNDLAWS: (\d+) words / (\d+) rules / (\d+) changes$"


class InputError(Exception):
    """A refused input; carries the stable label printed after SOUNDLAW_ERROR."""

    def __init__(self, label, detail):
        Exception.__init__(self, "%s: %s" % (label, detail))
        self.label = label
        self.detail = detail


def fail(label, detail):
    raise InputError(label, detail)


# --- rules -------------------------------------------------------------------

def parse_context(value, where, edge):
    """Validate one context list and return it as a list of segment strings.

    "#" is a boundary marker: it may only lead `pre` or trail `post`.
    """
    if not isinstance(value, list):
        fail("rule-context", "%s is not a list" % where)
    context = []
    for position, token in enumerate(value):
        if not isinstance(token, str) or not token.strip():
            fail("rule-context", "%s has a non-segment element %r" % (where, token))
        token = token.strip()
        if " " in token or "\t" in token:
            fail("rule-context", "%s element %r is not one segment" % (where, token))
        if "#" in token:
            if token != "#":
                fail("rule-context", "%s element %r mixes # with a segment" % (where, token))
            if edge == "pre" and position != 0:
                fail("rule-context", "%s anchors # at position %d, not the front" % (where, position))
            if edge == "post" and position != len(value) - 1:
                fail("rule-context", "%s anchors # at position %d, not the back" % (where, position))
        context.append(token)
    return context


def parse_rules(raw, origin):
    """Parse and validate rules JSON bytes into rule dicts. Raises InputError."""
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail("rules-json", "%s is not valid UTF-8" % origin)
    try:
        data = json.loads(text)
    except ValueError as error:
        fail("rules-json", "%s is not JSON: %s" % (origin, str(error).splitlines()[0][:120]))
    if not isinstance(data, dict):
        fail("rules-shape", "%s: top level is not an object" % origin)
    items = data.get("rules")
    if not isinstance(items, list):
        fail("rules-shape", '%s: "rules" is not a list' % origin)
    rules = []
    seen = set()
    for position, item in enumerate(items):
        if not isinstance(item, dict):
            fail("rules-shape", "%s: rule %d is not an object" % (origin, position))
        name = item.get("name")
        if name is None:
            fail("rule-name-missing", "%s: rule %d has no name" % (origin, position))
        if not isinstance(name, str) or not name.strip():
            fail("rule-name-empty", "%s: rule %d has an empty name" % (origin, position))
        name = name.strip()
        if any(ch in name for ch in "\t\r\n"):
            fail("rule-name-control", "%s: rule name %r carries a tab or newline" % (origin, name))
        if name in seen:
            fail("rule-duplicate", "%s: duplicate rule name %r" % (origin, name))
        seen.add(name)
        source = item.get("from")
        if source is None:
            fail("rule-from-missing", "%s: rule %r has no from" % (origin, name))
        if not isinstance(source, str):
            fail("rule-from-shape", "%s: rule %r from is not a string" % (origin, name))
        if not source.strip():
            fail("rule-from-empty", "%s: rule %r has an empty from" % (origin, name))
        source = source.strip()
        if len(source.split()) != 1 or "#" in source:
            fail("rule-from-shape", "%s: rule %r from %r is not one segment" % (origin, name, source))
        target = item.get("to")
        if target is None:
            fail("rule-to-missing", "%s: rule %r has no to" % (origin, name))
        if not isinstance(target, str):
            fail("rule-to-shape", "%s: rule %r to is not a string" % (origin, name))
        to_segments = target.split()
        for token in to_segments:
            if "#" in token:
                fail("rule-to-shape", "%s: rule %r to element %r carries #" % (origin, name, token))
        pre = parse_context(item.get("pre"), "%s: rule %r pre" % (origin, name), "pre")
        post = parse_context(item.get("post"), "%s: rule %r post" % (origin, name), "post")
        rules.append({"name": name, "from": source, "to": to_segments, "pre": pre, "post": post})
    return rules


def load_rules(path):
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as error:
        fail("rules-missing", "%s: %s" % (path, error.strerror or error))
    return parse_rules(raw, path)


# --- lexicon -----------------------------------------------------------------

def parse_input(text, origin):
    """Parse lexicon TSV text into (gloss, segment list) pairs, input order kept."""
    entries = []
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if TAB not in line:
            fail("input-syntax", "%s:%d: no TAB between gloss and segments" % (origin, number))
        gloss, _, field = line.partition(TAB)
        gloss = gloss.strip()
        segments = field.split()
        if not gloss:
            fail("input-syntax", "%s:%d: empty gloss" % (origin, number))
        if not segments:
            fail("input-empty-word", "%s:%d: gloss %r has no segments" % (origin, number, gloss))
        entries.append((gloss, segments))
    if not entries:
        fail("input-empty", "%s: no lexicon records" % origin)
    return entries


def load_input(path):
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as error:
        fail("input-missing", "%s: %s" % (path, error.strerror or error))
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail("input-syntax", "%s is not valid UTF-8" % path)
    return parse_input(text, path)


# --- derivation --------------------------------------------------------------

def pre_ok(word, index, pre):
    anchored = bool(pre) and pre[0] == "#"
    context = pre[1:] if anchored else pre
    start = index - len(context)
    if start < 0 or word[start:index] != context:
        return False
    return not anchored or start == 0


def post_ok(word, index, post):
    anchored = bool(post) and post[-1] == "#"
    context = post[:-1] if anchored else post
    start = index + 1
    stop = start + len(context)
    if stop > len(word) or word[start:stop] != context:
        return False
    return not anchored or stop == len(word)


def derive_word(word, rules):
    """Apply every rule in order; return (derived word, change tuples).

    Each change tuple is (input-side index, rule name, word before, word after).
    left to right, and the replacement is never rescanned by that same rule.
    """
    changes = []
    for rule in rules:
        source = rule["from"]
        target = rule["to"]
        pre = rule["pre"]
        post = rule["post"]
        out = []
        index = 0
        while index < len(word):
            if word[index] == source and pre_ok(word, index, pre) and post_ok(word, index, post):
                before = " ".join(word)
                after = " ".join(word[:index] + target + word[index + 1:])
                changes.append((index, rule["name"], before, after))
                out.extend(target)
            else:
                out.append(word[index])
            index += 1
        word = out
    return word, changes


# --- rendering ---------------------------------------------------------------

def render_lexicon(rows):
    return "".join("%s%s%s\n" % (gloss, TAB, " ".join(segments)) for gloss, segments in rows)


def render_changes(records):
    return "".join("%s%s%d%s%s%s%s%s%s\n" % (
        gloss, TAB, index, TAB, name, TAB, before, TAB, after) for gloss, index, name, before, after in records)


def summary_line(words, rules, changes):
    return "SOUNDLAWS: %d words / %d rules / %d changes" % (words, rules, changes)


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def check_out_path(out_path, rules_path, input_path, flag="--out"):
    """Refuse an output path that is the rules or input file itself."""
    out_abs = os.path.realpath(out_path)
    for label, other in (("rules", rules_path), ("input", input_path)):
        if out_abs == os.path.realpath(other):
            fail("output-path", "%s %s is the %s file" % (flag, out_path, label))


# --- apply -------------------------------------------------------------------

def run_apply(opts):
    rules = load_rules(opts["rules"])
    entries = load_input(opts["input"])
    check_out_path(opts["out"], opts["rules"], opts["input"], "--out")
    if opts.get("trace"):
        check_out_path(opts["trace"], opts["rules"], opts["input"], "--trace")
        if os.path.realpath(opts["trace"]) == os.path.realpath(opts["out"]):
            fail("output-path", "--trace and --out name the same file")
    derived = []
    records = []
    for gloss, segments in entries:
        word, changes = derive_word(list(segments), rules)
        derived.append((gloss, word))
        for index, name, before, after in changes:
            records.append((gloss, index, name, before, after))
    lexicon_text = render_lexicon(derived)
    changes_text = render_changes(records)
    write_text(opts["out"], lexicon_text)
    if opts.get("trace"): write_text(opts["trace"], changes_text)
    print(summary_line(len(derived), len(rules), len(records)))
    return 0


USAGE = (
    "usage: apply-sound-laws.py selftest\n"
    "       apply-sound-laws.py --selftest\n"
    "       apply-sound-laws.py apply --rules PATH --input PATH --out PATH [--trace PATH]\n"
)


# --- argument parsing --------------------------------------------------------

def parse_apply_argv(argv):
    opts = {"rules": None, "input": None, "out": None, "trace": None}
    position = 0
    while position < len(argv):
        flag = argv[position]
        if flag not in ("--rules", "--input", "--out", "--trace"):
            fail("usage", "unexpected argument %r" % flag)
        if position + 1 >= len(argv):
            fail("usage", "%s needs a value" % flag)
        opts[flag[2:]] = argv[position + 1]
        position += 2
    for key in ("rules", "input", "out"):
        if not opts[key]:
            fail("usage", "apply needs --%s" % key)
    return opts


# --- selftest ----------------------------------------------------------------

def run_selftest():
    passed = 0
    failed = []

    def case(name, fn):
        nonlocal passed
        try:
            fn()
        except AssertionError as error:
            failed.append((name, str(error) or "assertion failed"))
        except InputError as error:
            failed.append((name, "unexpected InputError %s: %s" % (error.label, error.detail)))
        except Exception as error:  # a crashed case is a failed case, never a pass
            failed.append((name, "%s: %s" % (type(error).__name__, error)))
        else:
            passed += 1

    def same(got, want, what="value"):
        if got != want:
            raise AssertionError("%s: got %r, want %r" % (what, got, want))

    def refuses(label, fn):
        try:
            fn()
        except InputError as error:
            same(error.label, label, "error label")
            if not error.detail:
                raise AssertionError("empty detail for label %s" % label)
            return
        raise AssertionError("no InputError; expected label %s" % label)

    def rules_from(*specs):
        payload = {"rules": [
            {"name": name, "from": source, "to": target, "pre": list(pre), "post": list(post)}
            for (name, source, target, pre, post) in specs]}
        return parse_rules(json.dumps(payload).encode("utf-8"), "<selftest>")

    def c_single_change():
        rules = rules_from(("voicing", "p", "b", ["a"], ["a"]))
        word, changes = derive_word(["a", "p", "a"], rules)
        same(word, ["a", "b", "a"], "word")
        same(changes, [(1, "voicing", "a p a", "a b a")], "changes")

    def c_deletion():
        rules = rules_from(("drop-final-a", "a", "", [], ["#"]))
        word, changes = derive_word(["k", "a"], rules)
        same(word, ["k"], "word")
        same(changes, [(1, "drop-final-a", "k a", "k")], "changes")
        same(derive_word(["a", "k"], rules), (["a", "k"], []), "word-internal a survives")

    def c_insertion():
        rules = rules_from(("epenthesis", "i", "i j", ["#"], []))
        same(derive_word(["i"], rules), (["i", "j"], [(0, "epenthesis", "i", "i j")]), "inserted segment")

    def c_word_start():
        rules = rules_from(("init", "w", "v", ["#"], []))
        same(derive_word(["w", "a"], rules)[0], ["v", "a"], "word-initial target")
        same(derive_word(["a", "w"], rules)[0], ["a", "w"], "word-medial target kept")

    def c_word_start_context():
        rules = rules_from(("after-initial-a", "p", "b", ["#", "a"], []))
        same(derive_word(["a", "p", "i"], rules)[0], ["a", "b", "i"], "context starts the word")
        same(derive_word(["i", "a", "p"], rules)[0], ["i", "a", "p"], "same segments, not word-initial")

    def c_word_end_anchor():
        rules = rules_from(("drop-final-t", "t", "", [], ["#"]))
        same(derive_word(["a", "t"], rules)[0], ["a"], "word-final target")
        same(derive_word(["t", "a"], rules)[0], ["t", "a"], "word-initial target kept")

    def c_word_end_context():
        rules = rules_from(("raise", "i", "e", [], ["a", "#"]))
        same(derive_word(["t", "i", "a"], rules)[0], ["t", "e", "a"], "context ends the word")
        same(derive_word(["t", "i", "a", "k"], rules)[0], ["t", "i", "a", "k"], "context not word-final")

    def c_pre_and_post():
        rules = rules_from(("both", "p", "b", ["i"], ["u"]))
        same(derive_word(["i", "p", "u"], rules)[0], ["i", "b", "u"], "both contexts hold")
        same(derive_word(["a", "p", "u"], rules)[0], ["a", "p", "u"], "pre context fails")
        same(derive_word(["i", "p", "a"], rules)[0], ["i", "p", "a"], "post context fails")

    def c_no_match():
        rules = rules_from(("v", "p", "b", [], []))
        same(derive_word(["k", "a", "t"], rules), (["k", "a", "t"], []), "no-match preservation")

    def c_multi_segment():
        rules = rules_from(("final", "a", "", [], ["#"]))
        word, changes = derive_word(["s", "t", "r", "a", "n", "g", "a"], rules)
        same(word, ["s", "t", "r", "a", "n", "g"], "only the final segment goes")
        same(len(changes), 1, "one change")

    def c_no_cascade():
        rules = rules_from(("spread", "a", "a a", [], []))
        same(derive_word(["a"], rules), (["a", "a"], [(0, "spread", "a", "a a")]), "one pass, one change")
        word, changes = derive_word(["a", "b", "a"], rules)
        same(word, ["a", "a", "b", "a", "a"], "two non-overlapping sites")
        same(len(changes), 2, "two changes, output not rescanned")

    def c_rule_order():
        up = rules_from(("x", "a", "b", [], []))
        down = rules_from(("y", "b", "c", [], []))
        same(derive_word(["a"], up + down)[0], ["c"], "x then y chains")
        same(derive_word(["a"], down + up)[0], ["b"], "y then x does not")
        same([change[1] for change in derive_word(["a"], up + down)[1]], ["x", "y"], "trace order follows file order")
        same([change[1] for change in derive_word(["a"], down + up)[1]], ["x"], "only the firing rule traces")

    def c_many_changes_one_pass():
        rules = rules_from(("v", "p", "b", ["a"], ["a"]))
        word, changes = derive_word(["a", "p", "a", "p", "a"], rules)
        same(word, ["a", "b", "a", "b", "a"], "both p segments voice")
        same([change[0] for change in changes], [1, 3], "indices follow the pass output")

    def c_initial_deletion_index():
        rules = rules_from(("drop-initial-a", "a", "", ["#"], []))
        word, changes = derive_word(["a", "a", "k"], rules)
        same(word, ["a", "k"], "only index 0 is word-initial")
        same(changes, [(0, "drop-initial-a", "a a k", "a k")], "index 0, one change")

    def c_empty_word():
        refuses("input-empty-word", lambda: parse_input("gloss\t   \n", "<selftest>"))
        refuses("input-empty-word", lambda: parse_input("gloss\t\n", "<selftest>"))

    def c_input_no_tab():
        refuses("input-syntax", lambda: parse_input("gloss only\n", "<selftest>"))

    def c_input_comments():
        text = "# comment\n\ngloss\ta b\r\nsecond\tc\n  # indented comment\n"
        same(parse_input(text, "<selftest>"), [("gloss", ["a", "b"]), ("second", ["c"])], "records and order")

    def c_input_empty():
        refuses("input-empty", lambda: parse_input("\n# only comments\n", "<selftest>"))

    def c_rules_not_json():
        refuses("rules-json", lambda: parse_rules(b"{not json", "<selftest>"))

    def c_rules_shape():
        refuses("rules-shape", lambda: parse_rules(b"[]", "<selftest>"))
        refuses("rules-shape", lambda: parse_rules(b'{"rules": 3}', "<selftest>"))

    def c_rule_name_missing():
        refuses("rule-name-missing", lambda: parse_rules(
            b'{"rules":[{"from":"a","to":"b","pre":[],"post":[]}]}', "<selftest>"))

    def c_rule_name_empty():
        refuses("rule-name-empty", lambda: parse_rules(
            b'{"rules":[{"name":"  ","from":"a","to":"b","pre":[],"post":[]}]}', "<selftest>"))

    def c_rule_from_missing():
        refuses("rule-from-missing", lambda: parse_rules(
            b'{"rules":[{"name":"n","to":"b","pre":[],"post":[]}]}', "<selftest>"))

    def c_rule_from_empty():
        refuses("rule-from-empty", lambda: parse_rules(
            b'{"rules":[{"name":"n","from":"","to":"b","pre":[],"post":[]}]}', "<selftest>"))

    def c_rule_from_shape():
        refuses("rule-from-shape", lambda: parse_rules(
            b'{"rules":[{"name":"n","from":"a b","to":"c","pre":[],"post":[]}]}', "<selftest>"))

    def c_rule_context_not_list():
        refuses("rule-context", lambda: parse_rules(
            b'{"rules":[{"name":"n","from":"a","to":"b","pre":"a","post":[]}]}', "<selftest>"))
        refuses("rule-context", lambda: parse_rules(
            b'{"rules":[{"name":"n","from":"a","to":"b","pre":[],"post":3}]}', "<selftest>"))

    def c_rule_context_bad_element():
        refuses("rule-context", lambda: parse_rules(
            b'{"rules":[{"name":"n","from":"a","to":"b","pre":[3],"post":[]}]}', "<selftest>"))
        refuses("rule-context", lambda: parse_rules(
            b'{"rules":[{"name":"n","from":"a","to":"b","pre":["a","#"],"post":[]}]}', "<selftest>"))

    def c_rule_duplicate():
        payload = b'{"rules":[{"name":"n","from":"a","to":"b","pre":[],"post":[]},' \
                  b'{"name":"n","from":"c","to":"d","pre":[],"post":[]}]}'
        refuses("rule-duplicate", lambda: parse_rules(payload, "<selftest>"))

    def c_rules_missing_file():
        refuses("rules-missing", lambda: load_rules(__file__ + ".no-such-rules.json"))

    def c_output_path():
        refuses("output-path", lambda: check_out_path("out/rules.json", "out/rules.json", "data/proto.tsv"))
        refuses("output-path", lambda: check_out_path("data/proto.tsv", "out/rules.json", "data/proto.tsv"))
        check_out_path("out/derived.tsv", "out/rules.json", "data/proto.tsv", "--trace")
        check_out_path("build/derived.tsv", "out/rules.json", "data/proto.tsv")
        check_out_path("out/derived.tsv", "out/rules.json", "data/proto.tsv")

    def c_rule_name_control():
        refuses("rule-name-control", lambda: parse_rules(
            b'{"rules":[{"name":"a\\nb","from":"a","to":"b","pre":[],"post":[]}]}', "<selftest>"))

    def c_change_record_shape():
        traces = [("father", 1, "v", "p", "b"), ("father", 2, "drop", "a", "")]
        lines = render_changes(traces).splitlines()
        same(len(lines), 2, "one line per change")
        same([len(line.split(TAB)) for line in lines], [5, 5], "five fields per line")
        same(lines[0].split(TAB), ["father", "1", "v", "p", "b"], "first record")
        same(lines[1].split(TAB), ["father", "2", "drop", "a", ""], "deletion keeps an empty after field")

    def c_derive_to_record():
        rules = rules_from(("v", "p", "b", ["a"], ["a"]), ("drop-final-a", "a", "", [], ["#"]))
        word, changes = derive_word(["a", "p", "a"], rules)
        same(word, ["a", "b"], "two rules chain")
        same([(g,) + change for g in ["father"] for change in changes],
             [("father", 1, "v", "a p a", "a b a"), ("father", 2, "drop-final-a", "a b a", "a b")], "records")

    def c_summary_shape():
        same(summary_line(16, 7, 19), "SOUNDLAWS: 16 words / 7 rules / 19 changes", "exact summary")
        if re.match(SUMMARY_RE, summary_line(1, 2, 3)) is None:
            raise AssertionError("summary does not match its own frozen regex")

    def c_empty_rules():
        same(parse_rules(b'{"rules": []}', "<selftest>"), [], "no rules")
        same(derive_word(["a", "b"], []), (["a", "b"], []), "no-op derivation")

    def c_render_lexicon():
        same(render_lexicon([("water", ["a", "k"]), ("ash", ["a", "r"])]),
             "water\ta k\nash\ta r\n", "TSV layout")

    def c_single_segment_word():
        rules = rules_from(("raise", "a", "e", [], []))
        same(derive_word(["a"], rules), (["e"], [(0, "raise", "a", "e")]), "one-segment word")

    case("single-segment-change", c_single_change)
    case("deletion", c_deletion)
    case("insertion-new-segment", c_insertion)
    case("word-start-anchor", c_word_start)
    case("word-start-context-anchor", c_word_start_context)
    case("word-end-anchor", c_word_end_anchor)
    case("word-end-context-anchor", c_word_end_context)
    case("pre-and-post-context", c_pre_and_post)
    case("no-match-preservation", c_no_match)
    case("multi-segment-word", c_multi_segment)
    case("non-overlap-no-cascade", c_no_cascade)
    case("rule-ordering", c_rule_order)
    case("many-changes-one-pass", c_many_changes_one_pass)
    case("initial-deletion-index", c_initial_deletion_index)
    case("empty-word-refusal", c_empty_word)
    case("input-no-tab-refusal", c_input_no_tab)
    case("input-comments-and-blanks", c_input_comments)
    case("input-empty-refusal", c_input_empty)
    case("rules-not-json-refusal", c_rules_not_json)
    case("rules-root-shape-refusal", c_rules_shape)
    case("rule-name-missing-refusal", c_rule_name_missing)
    case("rule-name-empty-refusal", c_rule_name_empty)
    case("rule-from-missing-refusal", c_rule_from_missing)
    case("rule-from-empty-refusal", c_rule_from_empty)
    case("rule-from-shape-refusal", c_rule_from_shape)
    case("rule-context-not-list-refusal", c_rule_context_not_list)
    case("rule-context-bad-element-refusal", c_rule_context_bad_element)
    case("rule-duplicate-refusal", c_rule_duplicate)
    case("rules-missing-file-refusal", c_rules_missing_file)
    case("output-path-refusal", c_output_path)
    case("rule-name-control-refusal", c_rule_name_control)
    case("change-record-shape", c_change_record_shape)
    case("derive-to-record", c_derive_to_record)
    case("summary-shape", c_summary_shape)
    case("empty-rules-noop", c_empty_rules)
    case("render-lexicon", c_render_lexicon)
    case("single-segment-word", c_single_segment_word)

    if failed:
        for name, detail in failed:
            sys.stderr.write("SELFTEST FAIL %s: %s\n" % (name, detail))
        print("SELFTEST: FAIL (%d/%d checks)" % (passed, passed + len(failed)))
        return 1
    print("SELFTEST: PASS (%d checks)" % passed)
    return 0


# --- entry -------------------------------------------------------------------

def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    try:
        if args[:1] in (["selftest"], ["--selftest"]):
            if len(args) != 1:
                fail("usage", "selftest takes no arguments")
            return run_selftest()
        if args[:1] == ["apply"]:
            return run_apply(parse_apply_argv(args[1:]))
        if args[:1] in (["--help"], ["-h"], ["help"]):
            sys.stdout.write(USAGE)
            return 0
        fail("usage", "no command; expected selftest or apply")
    except InputError as error:
        sys.stderr.write(ERROR_PREFIX + error.label + ": " + error.detail + "\n")
        return 2
    except OSError as error:
        sys.stderr.write(ERROR_PREFIX + "io: " + (error.strerror or str(error)) + "\n")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
