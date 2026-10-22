#!/usr/bin/env python3
"""Round-53 statement-clause legs that the declared commands do not check (a record, not a
declaration; added after the build-wave critics CriticClaimSizingC and CriticGapPremise found
the gaps). Run from the lane root of the measured tree:

  python3 -B reports/round-53/clauses.py --base-tree DIR

DIR is an export of the claim base a9cf95f. Legs, each printed PASS or FAIL:
  C1  "one new entry": the set of corpus/knowledge/**/*.md files differs from the base set by
      exactly one added path, the gesture entry, and no removed path
  C2  "on co-speech gesture, pointing ...": the entry's `- topic:` line names gesture and pointing
  C3  no draft ids in the gesture entry: no `NEW-<Name>-<n>` token and no `, -N` token
  D1  D repaired lines in place: the speech-surrogates entry has the same line count as at base
  D2  D dropped no source: every S-id the speech-surrogates entry cites at base is still cited
Exit 0 when all pass, 1 otherwise, 2 on unreadable input.
"""
import argparse
import os
import re
import sys

ED = "corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md"
EC = "corpus/knowledge/linguistics/gesture-co-speech-pointing.md"


def knowledge(root):
    base = os.path.join(root, "corpus/knowledge")
    return {os.path.relpath(os.path.join(d, f), root) for d, _, fs in os.walk(base)
            for f in fs if f.endswith(".md")}


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-tree", required=True)
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root, base = os.path.abspath(args.root), os.path.abspath(args.base_tree)
    legs = []
    try:
        now, then = knowledge(root), knowledge(base)
        added, removed = sorted(now - then), sorted(then - now)
        legs.append(("C1", added == [EC] and not removed, f"added={added} removed={removed}"))
        entry = read(root, EC) if os.path.isfile(os.path.join(root, EC)) else ""
        topic = next((l for l in entry.split("\n") if l.startswith("- topic:")), "")
        phrase = "- topic: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method"
        legs.append(("C2", topic.startswith(phrase), f"topic_chars={len(topic)} phrase_ok={topic.startswith(phrase)}"))
        drafts = re.findall(r"NEW-[A-Za-z0-9]+-\d+|, -\d+\b", entry)
        legs.append(("C3", bool(entry) and not drafts, f"draft_tokens={drafts[:5]}"))
        d_now, d_then = read(root, ED), read(base, ED)
        n_now, n_then = len(d_now.split("\n")), len(d_then.split("\n"))
        legs.append(("D1", n_now == n_then, f"lines={n_now} base={n_then}"))
        lost = sorted(set(re.findall(r"\bS\d{3}\b", d_then)) - set(re.findall(r"\bS\d{3}\b", d_now)))
        legs.append(("D2", not lost, f"lost={lost}"))
    except OSError as error:
        print(f"CLAUSES_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    return 0 if all(ok for _, ok, _ in legs) else 1


if __name__ == "__main__":
    sys.exit(main())
