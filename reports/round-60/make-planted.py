#!/usr/bin/env python3
"""Round-60 planted control rows for the SUPPORT leg of ACCEPT-D-60 (run once, before any data seat).

Usage (lane root): python3 -B reports/round-60/make-planted.py OUT.md
Builds 16 planted rows from the 43 base rows of the amulets entry with a secret random seed:
  6 x `quote-word-altered`  a real row with one content word of its quote replaced by a content word
                            of another row's quote (the page does not carry the altered quote);
  5 x `cross-wired`         one row's url and quote with another page's teaches and entry lines;
  5 x `invented-clause`     a real row whose entry line gains an invented place/date clause.
OUT is written outside the lane (the sandbox); only its sha256 is committed before data
(reports/round-60/planted-rows.sha256); the file itself is committed after the verdicts.
A diligent reader rejects each: the quote is not on the page, or the page does not carry the claim.
"""
import os
import random
import re
import sys

ENTRY = "corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md"
BASE_CITED = "reports/round-60/base-cited.txt"
SID = re.compile(r"\bS\d{3,}\b")
STOP = set("about above after again against also among because been before being between both "
           "could does doing during each from further have having into itself just more most other "
           "over same should some such than that their theirs them then there these they this those "
           "through under until very were what when where which while whom will with would your".split())
CLAUSES = ("; the practice is first recorded in fourteenth-century Norway",
           "; the type was standardised at the court of Jayavarman VII of Angkor",
           "; such pieces were licensed by the guild of Victorian Edinburgh silversmiths",
           "; the form was carried from Ming-dynasty Nanjing by returning envoys",
           "; the custom spread from eighteenth-century Lima through the Pacific trade")


def rows():
    out = {}
    for line in open("corpus/SOURCES.md", encoding="utf-8"):
        m = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if m:
            out[m.group(1)] = line.split("|")
    return out


def main(argv):
    if len(argv) != 1:
        print("usage: make-planted.py OUT.md", file=sys.stderr)
        return 2
    sys.path.insert(0, "reports/round-60")
    import importlib.util
    spec = importlib.util.spec_from_file_location("locator_60", "reports/round-60/reopen-quote.py")
    loc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loc)
    rnd = random.Random(int.from_bytes(os.urandom(16), "big"))
    ids = [l.strip() for l in open(BASE_CITED, encoding="utf-8") if l.strip()]
    table = rows()
    lines = open(ENTRY, encoding="utf-8").read().splitlines()

    def prop(sid):
        urls, quote = loc.row_target(table[sid])
        entry = " ".join(SID.sub(" ", l).strip() for l in lines if re.search(rf"\b{sid}\b", l))
        return " ".join(urls), quote, table[sid][7].strip(), entry

    picks = rnd.sample(ids, 16)
    blocks = []
    for n, sid in enumerate(picks[:6], 1):
        url, quote, teaches, entry = prop(sid)
        words = [w for w in re.findall(r"[A-Za-z]{6,}", quote) if w.lower() not in STOP]
        donor = prop(rnd.choice([i for i in ids if i != sid]))[1]
        repl = [w for w in re.findall(r"[A-Za-z]{6,}", donor) if w.lower() not in STOP and w.lower() not in quote.lower()]
        target = rnd.choice(words)
        altered = re.sub(rf"\b{re.escape(target)}\b", rnd.choice(repl).lower(), quote, count=1)
        blocks.append(("quote-word-altered", url, altered, teaches, entry, f"`{target}` replaced; the page has the unaltered sentence"))
    for sid in picks[6:11]:
        url, quote, _, _ = prop(sid)
        page = loc.row_target(table[sid])[0][0]
        other = rnd.choice([i for i in ids if i != sid and loc.row_target(table[i])[0][0] != page])
        _, _, teaches, entry = prop(other)
        blocks.append(("cross-wired", url, quote, teaches, entry, "teaches and entry belong to another page"))
    for sid, clause in zip(picks[11:16], rnd.sample(CLAUSES, 5)):
        url, quote, teaches, entry = prop(sid)
        blocks.append(("invented-clause", url, quote, teaches, entry.rstrip(" .") + clause + ".", f"invented clause `{clause[2:]}`"))
    with open(argv[0], "w", encoding="utf-8") as handle:
        handle.write("# Round-60 planted control rows (held out until after the verdicts)\n\n")
        for n, (kind, url, quote, teaches, entry, why) in enumerate(blocks, 1):
            handle.write(f"### PLANTED-{n}\nkind: {kind}\nurl: {url}\nquote: \"{quote}\"\nteaches: {teaches}\n"
                         f"entry: {entry}\nwhy-not-supported: {why}\n\n")
    print(f"planted rows written: {len(blocks)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
