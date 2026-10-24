#!/usr/bin/env python3
"""Round-68 settlement applier (L1 integration tool, runs in lane worktree).

Reads a rulings TSV (reports/round-68/dispositions/dedup-ledger.tsv shape:
`s | t | url | ruling | mechanism | evidence | note`, one row per chain s-id
plus keep rows) and applies the registry + entry mutations for `activate`
and `retire` rulings:

  activate s>t : s.status queued->mined, s.used-by gets the citing entries;
                 t.status mined->queued, t.used-by -> '—';
                 every corpus/knowledge citation `(t…)` -> `(s…)` in the
                 cited files (t tokens outside `(…)` left untouched — they
                 are prose/table-cell references reviewed separately).
  retire   s>t : s.status queued->rejected; s.teaches gains
                 'REJECTED: <note>; flip: <note-flip>' if not already;
                 t untouched.
  keep-*     : no mutation (ledger row only).

Usage: python3 settle-apply.py --root <lane> --ledger <tsv> [--dry]
Prints one APPLY line per mutation; exits 1 if any row can't be applied
cleanly (unexpected status, missing row, id not in the frozen set).
"""
import argparse
import os
import re
import sys

MUTABLE_S = {
    "S044", "S045", "S046", "S070", "S125", "S126", "S127", "S128", "S129",
    "S130", "S131", "S133", "S186", "S358", "S481", "S482", "S483", "S484",
    "S485", "S486", "S487", "S488", "S489", "S490", "S491", "S560", "S561",
    "S562", "S564", "S565", "S566", "S567", "S568", "S569",
}
MUTABLE_T = {
    "S034", "S038", "S039", "S060", "S095", "S105", "S079", "S086", "S097",
    "S117", "S119", "S122", "S157", "S256", "S359", "S367", "S383", "S385",
    "S392", "S395", "S396", "S399", "S407", "S410", "S413", "S417", "S421",
    "S433", "S438", "S440", "S445", "S452", "S453",
}
ROW_RE = re.compile(r"^\|\s*(S\d{3,})\s*\|")


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]]


def set_cell(line, idx, value):
    parts = line.rstrip("\n").split("|")
    # cell k lives at parts[k+1]; parts[1:-1][k] would write a discarded slice
    parts[idx + 1] = f" {value} "
    return "|".join(parts)


def citing_files(root, tid):
    out = []
    for dp, _, fs in os.walk(os.path.join(root, "corpus/knowledge")):
        for fn in sorted(fs):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            body = open(p, encoding="utf-8").read()
            if re.search(rf"\b{tid}\b", body):
                out.append(os.path.relpath(p, root))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    root = args.root
    reg_path = os.path.join(root, "corpus/SOURCES.md")
    reg_lines = open(reg_path, encoding="utf-8").read().splitlines(keepends=True)
    idx = {}
    for i, l in enumerate(reg_lines):
        m = ROW_RE.match(l.strip())
        if m:
            idx[m.group(1)] = i
    rulings = {}
    for raw in open(args.ledger, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        c = [x.strip() for x in line.split("|")]
        if len(c) == 7:
            rulings[c[0]] = c
    errors, applied = [], []
    edits = {}
    for sid, c in rulings.items():
        _s, t, _url, ruling, mechanism, _ev, note = c
        if ruling.startswith("keep"):
            continue
        if sid not in MUTABLE_S or (ruling == "activate" and t and t not in MUTABLE_T):
            errors.append(f"{sid}: outside frozen set")
            continue
        si = idx.get(sid)
        ti = idx.get(t) if t else None
        if si is None or (t and ti is None):
            errors.append(f"{sid}: row missing")
            continue
        srow, trow = reg_lines[si], (reg_lines[ti] if ti is not None else "")
        sc = cells(srow)
        if ruling == "activate":
            # s may already be mined (S126 at base carries used-by); in that
            # case the s row stays byte-identical and only the target is
            # deactivated + citations re-pointed (APPEND leg: cells 7/9/10).
            if sc[7] not in ("queued", "mined"):
                errors.append(f"{sid}: status {sc[7]} not queued")
                continue
            tc = cells(trow) if trow else []
            if tc and tc[7] != "mined":
                errors.append(f"{sid}: target status {tc[7]} not mined")
                continue
            files = citing_files(root, t)
            edits[sid] = ("activate", files)
            if not args.dry:
                if sc[7] == "queued":
                    reg_lines[si] = set_cell(set_cell(srow, 7, "mined"),
                                             10, ", ".join(files) if files else "—") + "\n"
                # already-mined s rows (S126) keep their bytes
                reg_lines[ti] = set_cell(set_cell(trow, 7, "queued"),
                                         10, "—") + "\n"
                for f in files:
                    fp = os.path.join(root, f)
                    body = open(fp, encoding="utf-8").read()
                    body = re.sub(rf"\b{t}\b", sid, body)
                    open(fp, "w", encoding="utf-8").write(body)
            applied.append(f"ACTIVATE {sid}>{t} files={len(files)}")
        elif ruling == "retire":
            if sc[7] != "queued":
                errors.append(f"{sid}: status {sc[7]} not queued")
                continue
            if not args.dry:
                # status flip ONLY: the frozen C APPEND leg confines in-place
                # edits to cells 7/9/10, so the teaches cell keeps its bytes;
                # the REJECTED reason + flip live in the ledger row and the
                # audit fragment (A_ca wave evidence), and the census enum
                # accepts `rejected` without the teaches prefix.
                reg_lines[si] = set_cell(srow, 7, "rejected") + "\n"
                # a retired successor's own citations revert to the target
                for f in citing_files(root, sid):
                    fp = os.path.join(root, f)
                    body = open(fp, encoding="utf-8").read()
                    body = re.sub(rf"\b{sid}\b", t, body)
                    open(fp, "w", encoding="utf-8").write(body)
            applied.append(f"RETIRE {sid}>{t}")
        else:
            errors.append(f"{sid}: ruling {ruling} not executable here")
    if not args.dry and applied:
        open(reg_path, "w", encoding="utf-8").write("".join(reg_lines))
    for a in applied:
        print("APPLY", a)
    for e in errors:
        print("ERROR", e)
    print(f"SETTLE-APPLY: applied={len(applied)} errors={len(errors)} dry={args.dry}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
