#!/usr/bin/env python3
r"""Round-59 claim D acceptance (depth: sentence-level fidelity of two knowledge entries to their
cited sources). Written before any round-59 data seat. Run from the lane root:

  python3 -B reports/round-59/accept-d.py [--root DIR] [--base REV]

Inputs: reports/round-59/d-fixes.json (frozen with this file; the fixes were drafted and verified
on the served sources by round-58 seats ReviewKongoA58, ReviewKongoB58, ReviewCarry135to147 and
ReviewCarry151to159) and the base bytes of both entries, read with `git show REV:PATH` (REV
defaults to the claim base named in reports/round-59/claims.json).

Legs, each printed with PASS or FAIL:
  KONGO   corpus/knowledge/civilizations/kongo-kingdom.md equals, byte for byte, its base bytes
          with each of the 14 frozen (old -> new) substitutions applied once, in file order; each
          old string occurs exactly once in the base bytes (else exit 2). Nothing else may differ:
          leaving a sentence unfixed, appending the new sentences while keeping the old ones, or
          any other edit to the entry fails.
  SPEECH  corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md equals its base bytes
          with every whole-word S135, S141, S147, S151 and S159 replaced by S570, S571, S572, S573
          and S574; the base carries them 16/2/3/2/4 times (else exit 2), and the tip carries none
          of the five old ids.
  CARRY   each of the 14 fixes' frozen support quote is located (reports/round-59/reopen-quote.py
          rules, at least 8 words) in the text one of its listed source URLs serves now, under
          FETCH-59 (reports/round-59/rowcheck.py: one fetch per URL per run; a URL whose fetch
          fails is skipped, never a pass; a listed Wayback capture is an ordinary copy). This leg
          shows each new sentence's wording is on its page; it does not discriminate a do-nothing
          tree (the base passes it too), which KONGO and SPEECH do.
Frozen predicate (the same sentence in reports/round-59/claims.json and in the receipts):
  ACCEPT-D-59: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg): whether each new sentence is the best reading of its page (round-58
reviewers' verdicts; round-59 falsify seats re-read a sample).
"""
import argparse
import concurrent.futures
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
FIXES = "reports/round-59/d-fixes.json"
CLAIMS = "reports/round-59/claims.json"


def base_bytes(root, rev, path):
    out = subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"], capture_output=True, timeout=60)
    if out.returncode != 0:
        raise OSError(f"git show {rev}:{path} exit {out.returncode}")
    return out.stdout.decode("utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--base", default=None)
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    try:
        spec = json.load(open(os.path.join(root, FIXES), encoding="utf-8"))
        rev = args.base or json.load(open(os.path.join(root, CLAIMS), encoding="utf-8"))["base"]
        kongo, speech = spec["kongo"], spec["speech"]
        k_base = base_bytes(root, rev, kongo["path"])
        s_base = base_bytes(root, rev, speech["path"])
        k_tip = open(os.path.join(root, kongo["path"]), encoding="utf-8", newline="").read()
        s_tip = open(os.path.join(root, speech["path"]), encoding="utf-8", newline="").read()
        loader = importlib.util.spec_from_file_location("rowcheck_59d", os.path.join(root, "reports/round-59/rowcheck.py"))
        rowcheck = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(rowcheck)
    except (OSError, ValueError, KeyError, TypeError, SyntaxError, UnicodeDecodeError, subprocess.SubprocessError) as error:
        print(f"ACCEPT_D_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    expected = k_base
    for fix in kongo["fixes"]:
        if k_base.count(fix["old"]) != 1 or expected.count(fix["old"]) != 1:
            print(f"ACCEPT_D_INPUT_ERROR fix {fix['id']} old string occurs {k_base.count(fix['old'])} times at base", file=sys.stderr)
            return 2
        expected = expected.replace(fix["old"], fix["new"], 1)
    unfixed = [f["id"] for f in kongo["fixes"] if f["old"] in k_tip]
    missing = [f["id"] for f in kongo["fixes"] if f["new"] not in k_tip]
    legs = [("KONGO", k_tip == expected,
             f"equal={k_tip == expected} fixes={len(kongo['fixes'])} old_still_present={unfixed} new_absent={missing}")]
    counts = {old: len(re.findall(rf"\b{old}\b", s_base)) for old in speech["remap"]}
    if counts != speech["base_counts"]:
        print(f"ACCEPT_D_INPUT_ERROR speech base counts {counts} != {speech['base_counts']}", file=sys.stderr)
        return 2
    s_expected = s_base
    for old, new in speech["remap"].items():
        s_expected = re.sub(rf"\b{old}\b", new, s_expected)
    left = {old: len(re.findall(rf"\b{old}\b", s_tip)) for old in speech["remap"]}
    legs.append(("SPEECH", s_tip == s_expected and not any(left.values()),
                 f"equal={s_tip == s_expected} old_ids_left={left}"))

    def probe(fix):
        stray = rowcheck.not_same_page(fix["support_urls"])
        if stray:
            return fix["id"], (False, f"not-same-page {stray}")
        return fix["id"], rowcheck.locator.locate(fix["support_urls"], fix["support_quote"])

    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        located = dict(pool.map(probe, kongo["fixes"]))
    misses = [f"{fid}: {detail[:160]}" for fid, (ok, detail) in sorted(located.items()) if not ok]
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    legs.append(("CARRY", not misses, f"located={len(located) - len(misses)}/{len(located)} at={stamp} failing={misses}"))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    verdict = all(ok for _, ok, _ in legs)
    print(f"ACCEPT-D-59: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
