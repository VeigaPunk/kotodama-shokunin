#!/usr/bin/env python3
"""Round-60 blind support packets for ACCEPT-D-60 (run once, after the entry is final and before the
support task call).

Usage (lane root): python3 -B reports/round-60/build-packets.py PLANTED.md OUTDIR
Every S-id the amulets entry cites goes to 2 distinct seats of SupportA60..SupportP60; every planted
row of PLANTED.md goes to 2 distinct seats, so each seat holds >= 2 planted blocks. Blocks are
shuffled per seat with a secret random seed and labelled P01, P02, ...; a block prints the row's
URLs, its quote, its teaches cell without a leading `supersedes Sxxx —`, and the entry lines citing
the id joined by spaces with S-ids removed (the proposition ACCEPT-D-60 compares). Writes
OUTDIR/packet-<Seat>.md and OUTDIR/planted-key.json (entry_sha256 of the entry bytes judged, and
per seat label -> S-id or PLANTED). The key's sha256 is committed before the support call.
"""
import hashlib
import importlib.util
import json
import os
import random
import re
import sys

ENTRY = "corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md"
SEATS = [f"Support{x}60" for x in "ABCDEFGHIJKLMNOP"]
SID = re.compile(r"\bS\d{3,}\b")
SUPERSEDES = re.compile(r"^\s*supersedes\s+S\d{3,}\s*[—–-]+\s*")
BLOCK = re.compile(r"^### (PLANTED-\d+)\n((?:(?!### ).*\n?)*)", re.M)
FIELD = re.compile(r"^(url|quote|teaches|entry):[ \t]*(.*)$", re.M)


def main(argv):
    if len(argv) != 2:
        print("usage: build-packets.py PLANTED.md OUTDIR", file=sys.stderr)
        return 2
    spec = importlib.util.spec_from_file_location("locator_60", "reports/round-60/reopen-quote.py")
    loc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loc)
    rnd = random.Random(int.from_bytes(os.urandom(16), "big"))
    raw = open(ENTRY, "rb").read()
    lines = raw.decode("utf-8").splitlines()
    cited = sorted(set(SID.findall(raw.decode("utf-8"))))
    table = {}
    for line in open("corpus/SOURCES.md", encoding="utf-8"):
        m = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if m:
            table[m.group(1)] = line.split("|")
    blocks = []
    for sid in cited:
        urls, quote = loc.row_target(table[sid])
        entry = " ".join(SID.sub(" ", l) for l in lines if re.search(rf"\b{sid}\b", l))
        body = (f"url: {' '.join(urls)}\nquote: \"{quote}\"\nteaches: {SUPERSEDES.sub('', table[sid][7]).strip()}\n"
                f"entry: {entry.strip()}\n")
        blocks.append((sid, body))
    for name, text in BLOCK.findall(open(argv[0], encoding="utf-8").read()):
        fields = dict(FIELD.findall(text))
        body = "".join(f"{f}: {fields[f]}\n" for f in ("url", "quote", "teaches", "entry"))
        blocks.append(("PLANTED", body))
    load = {s: [] for s in SEATS}
    planted = [b for b in blocks if b[0] == "PLANTED"]
    real = [b for b in blocks if b[0] != "PLANTED"]
    order = SEATS[:]
    rnd.shuffle(order)
    slot = 0
    for group in (planted, real):
        for block in group:
            chosen = []
            while len(chosen) < 2:
                seat = order[slot % len(order)]
                slot += 1
                if seat not in chosen:
                    chosen.append(seat)
            for seat in chosen:
                load[seat].append(block)
    os.makedirs(argv[1], exist_ok=True)
    key = {"entry": ENTRY, "entry_sha256": hashlib.sha256(raw).hexdigest(), "seats": {}}
    for seat in SEATS:
        items = load[seat][:]
        rnd.shuffle(items)
        key["seats"][seat] = {}
        with open(os.path.join(argv[1], f"packet-{seat}.md"), "w", encoding="utf-8") as handle:
            handle.write(f"# Packet {seat} ({len(items)} blocks)\nentry_sha256: {key['entry_sha256']}\n\n")
            for n, (target, body) in enumerate(items, 1):
                label = f"P{n:02d}"
                key["seats"][seat][label] = target
                handle.write(f"### {label}\n{body}\n")
    with open(os.path.join(argv[1], "planted-key.json"), "w", encoding="utf-8") as handle:
        json.dump(key, handle, indent=1, ensure_ascii=False)
        handle.write("\n")
    per = {s: sum(1 for t in key["seats"][s].values() if t == "PLANTED") for s in SEATS}
    print(f"cited={len(cited)} planted_rows={len(planted)} seats={len(SEATS)} planted_per_seat_min={min(per.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
