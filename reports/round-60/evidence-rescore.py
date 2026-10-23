#!/usr/bin/env python3
"""L1 re-score of MutEvidenceA3's EVIDENCE fixtures under revision 8 (its own seat's rev-8 re-score
was refused, cyber_policy, and is a hold). Function-level: runs the counter's `evidenced` from a
revision-7 and a revision-8 checkout on the same verdict-line remainders and the same packet blocks.

Usage (lane root): python3 -B reports/round-60/evidence-rescore.py <rev7-root> <rev8-root> <case-dir> <packet-dir>
case-dir: /fast/scratch/hyaku/kotodama-r60a3/MutEvidenceA3 (cases.json, extra-cases.json,
honest-spans.json, shared-site-spans.json, packet-only-repeated-word.py); packet-dir: the round's
packets (block text per sid is identical across packets built from one entry).
"""
import importlib.util
import json
import os
import subprocess
import sys


def load(root, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(root, "reports/round-60/accept-d.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, mod.load_locator(root)


r7root, r8root, cases_dir, pkt_dir = sys.argv[1:5]
a7, loc7 = load(r7root, "a7")
a8, loc8 = load(r8root, "a8")
texts = a8.page_texts(r8root)
norms = {sid: a8.norm_forms(t, loc8) for sid, t in texts.items()}
key = json.load(open(os.path.join(pkt_dir, "planted-key.json"), encoding="utf-8"))
blocks, packets = {}, {}
for seat, labels in key["seats"].items():
    text = open(os.path.join(pkt_dir, f"packet-{seat}.md"), encoding="utf-8").read()
    packets[seat] = text
    raw = dict(a8.PACKET_BLOCK.findall(text))
    for label, sid in labels.items():
        if sid != "PLANTED":
            blocks.setdefault(sid, raw[label])


def both(sid, rest):
    return (a7.evidenced(rest, texts.get(sid, ""), blocks.get(sid, ""), loc7),
            a8.evidenced(rest, sid, norms, blocks.get(sid, ""), loc8))


rows = []
for f in ("cases.json", "extra-cases.json"):
    for case in json.load(open(os.path.join(cases_dir, f), encoding="utf-8")):
        r7, r8 = both(case["sid"], case["rest"])
        rows.append((f"{f}:{case['name']}", case["sid"], case.get("expected"), r7, r8))
for sid, span in json.load(open(os.path.join(cases_dir, "honest-spans.json"), encoding="utf-8")).items():
    r7, r8 = both(sid, f' — "{span}"')
    rows.append(("honest-spans", sid, True, r7, r8))
for item in json.load(open(os.path.join(cases_dir, "shared-site-spans.json"), encoding="utf-8")):
    for sid in item["sids"]:
        r7, r8 = both(sid, f' — "{item["span"]}"')
        rows.append((f"shared-site:{item['host']}", sid, False, r7, r8))
gen = os.path.join(cases_dir, "packet-only-repeated-word.py")
counted7 = counted8 = total = 0
for seat, labels in key["seats"].items():
    out = json.loads(subprocess.run([sys.executable, "-B", gen], input=packets[seat], capture_output=True,
                                    text=True, timeout=60).stdout)
    for label, sid in labels.items():
        if sid == "PLANTED":
            continue
        total += 1
        r7, r8 = both(sid, f' — "{out.get(label, "")}"')
        counted7 += r7
        counted8 += r8
print("case | sid | expected | rev7 | rev8 | rev8-matches-expected")
for name, sid, exp, r7, r8 in rows:
    print(f"{name} | {sid} | {exp} | {r7} | {r8} | {'' if exp is None else exp == r8}")
wrong = [r for r in rows if r[2] is not None and r[2] != r[4]]
print(f"packet-only generator over the round's 24 packets: real labels counted rev7={counted7}/{total} rev8={counted8}/{total}")
print(f"rev8 cases differing from expected: {len(wrong)} {[(r[0], r[1]) for r in wrong]}")
