#!/usr/bin/env python3
"""RevMalformed (round-79 W1) — observed behaviour probe for malformed ledgers.

Runs every fixture committed by build_fixtures.py through the EXISTING round-76
Ca counter functions (the committed source, imported unmodified from a scratch
copy whose sha256 is printed):

  * read:      module.show(fixrepo, FIXCOMMIT, "fixtures/<ID>.json")  (real git plumbing)
  * load:      a verbatim mirror of reports/round-76/accept-ca.py load_frozen
               lines 893-906 (json.loads default parser, list/dict pair filter)
  * evaluate:  module.evaluate_pairs(pairs, base, base)
  * LEDGER:    module.leg_ledger(out, cfg, pairs, base, ev)

It also reports the parse-level diagnostics a strict loader would see (duplicate keys,
non-finite constants) so each fixture's expectation can be compared with what the
default parser silently does.  This is NOT the guard: the guard does not exist yet.

Usage:
  python3 -B probe_malformed.py --work <scratch> --stage <stage> --counter-src <r76 copy>
"""
import argparse
import collections
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import sys
import traceback


def load_counter(path):
    spec = importlib.util.spec_from_file_location("r76_accept_ca", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def strict_diag(raw):
    """Diagnostics only: duplicate keys and non-finite constants a strict parser would flag."""
    dups = []
    nonfinite = []

    def hook(pairs):
        counts = collections.Counter(k for k, _ in pairs)
        for k, c in counts.items():
            if c > 1:
                dups.append(k)
        return dict(pairs)

    def const(name):
        nonfinite.append(name)
        return float(name.replace("Infinity", "inf"))

    try:
        json.loads(raw, object_pairs_hook=hook, parse_constant=const)
        status = "ok"
    except RecursionError as exc:
        status = "RecursionError: %s" % exc
    except ValueError as exc:
        status = "ValueError: %s" % str(exc)[:120]
    return status, sorted(set(dups)), sorted(set(nonfinite))


def r76_load(mod, raw_text):
    """Verbatim mirror of reports/round-76/accept-ca.py load_frozen lines 893-906."""
    problems = []
    if raw_text is None:
        return None, {}, ["ledger absent"], None
    ledger = None
    try:
        ledger = json.loads(raw_text)
    except ValueError as exc:
        problems.append("ledger JSON at --freeze: %s" % exc)
    raw_items = None
    if isinstance(ledger, dict):
        raw_items = ledger.get("pairs", []) if "pairs" in ledger else []
    if isinstance(ledger, list):
        meta = {"pairs": [p for p in ledger if isinstance(p, dict)]}
        ledger = meta
        raw_items = len(meta["pairs"])
    elif isinstance(ledger, dict):
        meta = dict(ledger)
        meta["pairs"] = [p for p in ledger.get("pairs", []) if isinstance(p, dict)]
    else:
        meta = {}
        problems.append("ledger at --freeze is neither object nor list")
    return ledger, meta, problems, raw_items


def describe_raw_items(raw_items):
    if raw_items is None:
        return "n/a"
    if isinstance(raw_items, (int, float)) and not isinstance(raw_items, bool):
        return str(raw_items)
    if isinstance(raw_items, list):
        return "list(%d)" % len(raw_items)
    return type(raw_items).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--stage", required=True)
    ap.add_argument("--counter-src", required=True)
    args = ap.parse_args()
    stage = os.path.abspath(args.stage)
    work = os.path.abspath(args.work)
    fix = os.path.join(work, "fixrepo")
    manifest = json.load(open(os.path.join(stage, "manifest.json"), encoding="utf-8"))
    src_sha = hashlib.sha256(open(args.counter_src, "rb").read()).hexdigest()
    print("counter source:", args.counter_src)
    print("counter source sha256:", src_sha)
    print("fixture repo:", fix, "base:", manifest["base"], "fixcommit:", manifest["fixcommit"])
    mod = load_counter(args.counter_src)
    base = manifest["base"]
    base_clone = {"path": fix}
    summary = []
    for case in manifest["cases"]:
        fid = case["id"]
        print("")
        print("== %s %s strict_expect=%s strict_label=%s bytes=%d" %
              (fid, case["class"], case["strict_expect"], case["strict_label"], case["bytes"]))
        print("   desc: %s" % case["description"])
        # read through the counter's own show()
        try:
            raw = mod.show(fix, manifest["fixcommit"], "fixtures/%s.json" % fid)
        except Exception as exc:  # noqa: BLE001 - probe records every crash
            print("   read: CRASH %s: %s" % (type(exc).__name__, str(exc)[:160]))
            summary.append((fid, case["class"], case["strict_expect"], "CRASH:read:%s" % type(exc).__name__))
            continue
        if raw is None:
            print("   read: absent")
            summary.append((fid, case["class"], case["strict_expect"], "absent"))
            continue
        print("   read: ok chars=%d" % len(raw))
        dstat, dups, nonf = strict_diag(raw)
        print("   parse-diag: status=%s dup_keys=%s nonfinite=%s" % (dstat, dups, nonf))
        try:
            ledger, meta, problems, raw_items = r76_load(mod, raw)
        except Exception as exc:  # noqa: BLE001
            print("   load: CRASH %s: %s" % (type(exc).__name__, str(exc)[:160]))
            summary.append((fid, case["class"], case["strict_expect"], "CRASH:load:%s" % type(exc).__name__))
            continue
        print("   load: raw_pairs=%s kept_dict_pairs=%s problems=%s" %
              (describe_raw_items(raw_items), len(meta.get("pairs", [])) if isinstance(meta, dict) else "n/a",
               problems[:2]))
        pairs = meta.get("pairs", []) if isinstance(meta, dict) else []
        cfg = {"round": 76, "claim": "Ca", "base": base, "min_pairs": 10,
               "ledger_rel": "fixtures/%s.json" % fid, "ledger_raw": raw,
               "ledger_meta": meta, "fleet_root": fix, "repair_mutable": [],
               "annotate_append": []}
        # the state main_check (accept-ca.py lines 2688-2691, 2727) sets before any observation
        mod.CTX["fleet_root"] = fix
        mod.CTX["root"] = fix
        mod.CTX["cfg"] = cfg
        mod.RUN_STATE["outside_clone"] = False
        mod.RUN_STATE["work"] = work
        out = []
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                ev = mod.evaluate_pairs(pairs, base_clone, base_clone)
        except Exception as exc:  # noqa: BLE001
            print("   evaluate: CRASH %s: %s" % (type(exc).__name__, str(exc)[:200]))
            print("   evaluate-trace: %s" % traceback.format_exc().strip().splitlines()[-3:])
            summary.append((fid, case["class"], case["strict_expect"], "CRASH:evaluate:%s" % type(exc).__name__))
            continue
        try:
            with contextlib.redirect_stdout(buf):
                mod.leg_ledger(out, cfg, pairs, base_clone, ev)
        except Exception as exc:  # noqa: BLE001
            print("   LEDGER: CRASH %s: %s" % (type(exc).__name__, str(exc)[:200]))
            summary.append((fid, case["class"], case["strict_expect"], "CRASH:leg:%s" % type(exc).__name__))
            continue
        for line in buf.getvalue().splitlines():
            print("   " + line)
        name, passed, detail = out[0]
        verdict = "PASS" if passed else "FAIL"
        print("   R76-OBSERVED: LEDGER %s" % verdict)
        summary.append((fid, case["class"], case["strict_expect"], verdict + " " + (detail[:150] if detail else "")))
    print("")
    print("== SUMMARY (R76 counter LEDGER leg, observed; strict expectation from manifest)")
    for fid, cls, exp, obs in summary:
        print("%-4s %-24s strict=%-7s r76=%s" % (fid, cls, exp, obs))


if __name__ == "__main__":
    main()
