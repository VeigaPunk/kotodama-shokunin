#!/usr/bin/env python3
"""Round-77 LEGCOUNT gate: frozen claims.json legs[] == the counter's own table.

The rule (round 77, both claims): the `legs[]` list frozen in
`reports/round-77/claims.json` must be exactly the leg table the counter
implements — same names, same order, duplicates included.  A frozen list that
is shorter, longer, re-spelled or re-ordered is a freeze blocker, because both
round-76 counters refuse (exit 2) on LEGCOUNT and a refusal grades
`FAIL legs=0/N`: the claim then never even runs.

Measured precedent (round 76), receipts in the wave dir:
`.ufo/waves/round-76/w1/stage/L1/freeze-control-legcount-redbefore.txt` shows
the real freeze refusing with

  REFUSED: LEGCOUNT: the frozen claims.json lists 13 legs
  (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,
   COLLCHECK,FROZENCFG,INDEX); this counter implements 13
  (...,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX)

i.e. slot 9 was designed as INDEX and implemented as SCRATCHMIRROR.  Nothing
caught it before the freeze commit.

How the names are obtained — never hand-typed:
  * counter side: the module-level table assignment is parsed out of the
    counter source with `ast` (no import, no `exec`, no shell), so the table's
    own literal spelling is what gets compared.  Two literal shapes are
    accepted:
      LEGS = (("ENTRIES", leg_entries), ...)      # (name, function) pairs
      REQUIRED_LEGS = ("LEDGER", "BASEMISMATCH")  # bare names
  * claims side: each frozen leg is the prose string `NAME: sentence`; the
    name is the text before the first ':'.  A leg that does not start with an
    UPPER_SNAKE token (for example the draft's `LEDGELIST?`) is a placeholder
    and fails — a freeze may not carry a typed question mark.

usage:
  legcount.py --claim C  [--root DIR] [--claims P] [--counter P] [--symbol S]
  legcount.py --claim Ca [--root DIR] [--claims P] [--counter P] [--symbol S]
  legcount.py --claim C --rev <commit>        # authoritative: read committed blobs
  legcount.py --claim C --print frozen|counter|both
  legcount.py --claim C --json

defaults: --root  the lane worktree toplevel of this script's directory
          --claims  reports/round-77/claims.json
          --counter reports/round-77/accept-c.py  for C
                    reports/round-77/accept-ca.py for Ca
          --symbol  LEGS (C) / REQUIRED_LEGS (Ca); a table under the other
                    accepted symbol is used when the preferred one is absent

exit:
  0  PASS — the frozen names equal the counter table (order and set)
  1  FAIL — names differ (set, order or multiplicity); freeze blocker
  2  usage / IO / parse error (never a silent pass)
  3  PENDING — claims.json or the counter does not exist yet (build time);
     the exact freeze-time command is printed

Read-only: this script opens files, or `git show`s a revision.  It writes
nothing, mutates no git state and creates no temp files.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys

DEFAULTS = {
    "C": {"claims": "reports/round-77/claims.json",
          "counter": "reports/round-77/accept-c.py",
          "symbols": ("LEGS", "REQUIRED_LEGS")},
    "Ca": {"claims": "reports/round-77/claims.json",
           "counter": "reports/round-77/accept-ca.py",
           "symbols": ("REQUIRED_LEGS", "LEGS")},
}

LEG_NAME_RE = re.compile(r"[A-Z][A-Z0-9_]*\Z")


class TableError(Exception):
    pass


def _read(root: str, rel: str, rev: str | None) -> str:
    """Source text of `rel`: the committed blob at `rev`, else the worktree file."""
    if rev:
        proc = subprocess.run(["git", "-C", root, "show", "%s:%s" % (rev, rel)],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            raise TableError("git show %s:%s failed: %s"
                             % (rev, rel, proc.stderr.decode("utf-8", "replace").strip()))
        return proc.stdout.decode("utf-8", "surrogateescape")
    path = os.path.join(root, rel)
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8", "surrogateescape")


def _table_node(tree: ast.AST, symbol: str):
    for node in getattr(tree, "body", ()):
        targets = ()
        if isinstance(node, ast.Assign):
            targets, value = node.targets, node.value
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets, value = (node.target,), node.value
        else:
            continue
        if any(isinstance(t, ast.Name) and t.id == symbol for t in targets):
            return value
    return None


def counter_table(src: str, symbols, path: str) -> tuple[str, list[str]]:
    """(symbol, names) from the counter's module-level leg table literal."""
    try:
        tree = ast.parse(src, filename=path)
    except SyntaxError as exc:
        raise TableError("%s does not parse: %s" % (path, exc))
    tried = []
    for symbol in symbols:
        value = _table_node(tree, symbol)
        if value is None:
            tried.append("%s: absent" % symbol)
            continue
        if not isinstance(value, (ast.Tuple, ast.List)):
            tried.append("%s: not a tuple/list literal" % symbol)
            continue
        names = []
        for index, el in enumerate(value.elts):
            if isinstance(el, ast.Constant) and isinstance(el.value, str):
                name = el.value                              # bare-name table
            elif (isinstance(el, (ast.Tuple, ast.List)) and el.elts
                  and isinstance(el.elts[0], ast.Constant)
                  and isinstance(el.elts[0].value, str)):
                name = el.elts[0].value                      # (name, fn) pair
            else:
                tried.append("%s[%d]: neither a string nor a (name, fn) pair"
                             % (symbol, index))
                names = None
                break
            names.append(name)
        if names is None:
            continue
        if not names:
            tried.append("%s: empty table" % symbol)
            continue
        return symbol, names
    raise TableError("%s: no usable leg table (%s)" % (path, "; ".join(tried)))


def frozen_table(doc, claim_id: str) -> tuple[list[str], list[str]]:
    """(names, problems) from the frozen claims document's claim `claim_id`."""
    problems = []
    claims = doc.get("claims")
    if not isinstance(claims, list):
        raise TableError("claims.json has no claims[] list")
    match = None
    for claim in claims:
        if isinstance(claim, dict) and claim.get("id") == claim_id:
            match = claim
            break
    if match is None:
        raise TableError("claims.json holds no claim with id %r (ids: %s)"
                         % (claim_id, ",".join(str(c.get("id")) for c in claims
                                               if isinstance(c, dict))))
    legs = match.get("legs")
    if not isinstance(legs, list) or not legs:
        raise TableError("claim %s has no non-empty legs[] list" % claim_id)
    names = []
    for index, text in enumerate(legs):
        if not isinstance(text, str):
            problems.append("legs[%d] is not a string" % index)
            continue
        if ":" not in text:
            problems.append("legs[%d] does not begin with `NAME: ` (%r)"
                            % (index, text[:40]))
            continue
        name = text.split(":", 1)[0].strip()
        if not LEG_NAME_RE.match(name):
            problems.append("legs[%d] name %r is not UPPER_SNAKE — an unresolved "
                            "placeholder cannot be frozen" % (index, name))
            continue
        names.append(name)
    return names, problems


def first_divergence(got, want):
    for index, (a, b) in enumerate(zip(got, want)):
        if a != b:
            return index, a, b
    if len(got) != len(want):
        long, short = (got, want) if len(got) > len(want) else (want, got)
        return len(short), (long[len(short)] if len(got) > len(want) else None), \
               (long[len(short)] if len(want) > len(got) else None)
    return None


def duplicates(names):
    seen, dup = set(), []
    for name in names:
        if name in seen and name not in dup:
            dup.append(name)
        seen.add(name)
    return dup


def repo_root(start: str) -> str:
    proc = subprocess.run(["git", "-C", start, "rev-parse", "--show-toplevel"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise TableError("%s is not inside a git worktree" % start)
    return proc.stdout.decode().strip()


def main(argv=None) -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(add_help=True,
                                 description="LEGCOUNT gate for kotodama round 77")
    ap.add_argument("--claim", choices=("C", "Ca"), required=True)
    ap.add_argument("--root", default=None,
                    help="lane repository root (default: toplevel above this script)")
    ap.add_argument("--claims", default=None, help="claims.json, repo-relative")
    ap.add_argument("--counter", default=None, help="counter source, repo-relative")
    ap.add_argument("--symbol", default=None,
                    help="counter table symbol (default: LEGS / REQUIRED_LEGS)")
    ap.add_argument("--rev", default=None,
                    help="read both files from this commit (authoritative post-freeze)")
    ap.add_argument("--print", dest="show", choices=("frozen", "counter", "both"),
                    default=None, help="print names one per line and exit")
    ap.add_argument("--json", action="store_true", help="machine-readable result")
    args = ap.parse_args(argv)

    defaults = DEFAULTS[args.claim]
    claims_rel = args.claims or defaults["claims"]
    counter_rel = args.counter or defaults["counter"]
    symbols = (args.symbol,) if args.symbol else defaults["symbols"]

    try:
        root = repo_root(args.root or here)
    except TableError as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2

    missing = []
    try:
        counter_src = _read(root, counter_rel, args.rev)
    except FileNotFoundError:
        missing.append(counter_rel)
        counter_src = None
    except TableError as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    # `--print counter` regenerates the frozen list from the counter alone, so it
    # must work even when claims.json has not been written yet
    need_claims = args.show != "counter"
    claims_src = None
    if need_claims:
        try:
            claims_src = _read(root, claims_rel, args.rev)
        except FileNotFoundError:
            missing.append(claims_rel)
        except TableError as exc:
            print("ERROR: %s" % exc, file=sys.stderr)
            return 2

    pending_cmd = ("python3 -B %s --claim %s%s"
                   % (os.path.relpath(os.path.abspath(__file__), root or here),
                      args.claim, "" if args.rev else " --rev <freeze>"))
    if missing:
        if args.json:
            print(json.dumps({"claim": args.claim, "status": "PENDING",
                              "missing": missing, "command": pending_cmd}, indent=1))
        else:
            print("LEGCOUNT %s: PENDING — absent: %s" % (args.claim, ", ".join(missing)))
            print("LEGCOUNT %s: run at freeze: %s" % (args.claim, pending_cmd))
        return 3

    try:
        symbol, counter_names = counter_table(counter_src, symbols, counter_rel)
    except TableError as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    if args.show == "counter":
        for name in counter_names:
            print(name)
        return 0
    try:
        doc = json.loads(claims_src)
    except ValueError as exc:
        print("ERROR: %s does not parse as JSON: %s" % (claims_rel, exc), file=sys.stderr)
        return 2
    try:
        frozen_names, problems = frozen_table(doc, args.claim)
    except TableError as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2

    if args.show in ("frozen", "both"):
        for name in frozen_names:
            print(name)
    if args.show == "both":
        print("--")
    if args.show in ("counter", "both"):
        for name in counter_names:
            print(name)
    if args.show:
        return 1 if problems else 0

    order_ok = frozen_names == counter_names
    set_ok = sorted(frozen_names) == sorted(counter_names)
    verdict = "PASS" if order_ok and not problems else "FAIL"
    divergence = None if order_ok else first_divergence(frozen_names, counter_names)

    if args.json:
        print(json.dumps({
            "claim": args.claim, "claims": claims_rel, "counter": counter_rel,
            "symbol": symbol, "rev": args.rev, "status": verdict,
            "frozen": frozen_names, "counter_names": counter_names,
            "order_ok": order_ok, "set_ok": set_ok,
            "first_divergence": (None if divergence is None else
                                 {"index": divergence[0], "frozen": divergence[1],
                                  "counter": divergence[2]}),
            "duplicates_frozen": duplicates(frozen_names),
            "duplicates_counter": duplicates(counter_names),
            "problems": problems,
        }, indent=1))
        return 0 if verdict == "PASS" else 1

    print("LEGCOUNT %s: counter=%s symbol=%s rev=%s"
          % (args.claim, counter_rel, symbol, args.rev or "worktree"))
    print("LEGCOUNT %s: frozen (%d): %s"
          % (args.claim, len(frozen_names), ",".join(frozen_names)))
    print("LEGCOUNT %s: counter (%d): %s"
          % (args.claim, len(counter_names), ",".join(counter_names)))
    for name in duplicates(frozen_names):
        print("LEGCOUNT %s: NOTE frozen lists %r more than once (the counter's "
              "order decides the position)" % (args.claim, name))
    for problem in problems:
        print("LEGCOUNT %s: PROBLEM %s" % (args.claim, problem))
    if divergence is not None:
        index, frozen_at, counter_at = divergence
        print("LEGCOUNT %s: DIVERGES at index %d: frozen=%r counter=%r "
              "(set %s)" % (args.claim, index, frozen_at, counter_at,
                            "equal" if set_ok else "differs"))
    print("LEGCOUNT %s: %s (%s)" % (args.claim, verdict,
                                    "order and set equal" if order_ok and not problems
                                    else "freeze blocker: regenerate legs[] from the "
                                         "counter table, never hand-type"))
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
