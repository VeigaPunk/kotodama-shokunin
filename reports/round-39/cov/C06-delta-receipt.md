- Seat: C06 | executor (claim C) | README rev-2.2 delta draft + coverage receipt draft | date 2026-10-19 | baseline dfb0719

# C06 — `corpus/README.md` revision-2.2 delta draft + claim-C coverage receipt draft

**Assignment** (`reports/round-39/targets.json:68-74`, seat C06): "README rev 2.2 delta draft
(verification header 24, totals 216, vector 21/23/25/29/24/94, 4 rows in filename order) +
coverage receipt draft." Out path: this file only. Binding shared rules read at
`reports/round-39/targets.json:4-9`; claim C read at `reports/round-39/claims.json:13-18`;
obligations for this seat read at `reports/round-39/plan/P01-plan.md:110-118` (delta legs a–e +
post-apply-sweep receipt rule + do-not-repair rule).

**Status: DRAFT — integrator-applied.** This seat wrote **zero** bytes outside this file: no
corpus entry, no README byte, no tool byte, no filed-round byte. No `reports/round-*/run-validation.py`
was executed anywhere (absolute rule, `reports/round-39/targets.json:8`). Every *before* figure
below is this seat's own measurement at the pinned state (§2); every *after* figure is either the
declared target (`reports/round-39/claims.json:16`) or a mechanically generated value, and the
sweep reading that certifies the landing is **measured at close, never predicted** (§7, §8 — the
`readme-prediction-vs-delivery` rule, `reports/round-37/op/defect-queue.json:242-251`).

**What landed at this seat's cut** (polls 12:20:10Z–12:31:29Z): C01, C02, C03, C04 entry drafts
+ K01/K02 scouts + P01 plan + X00 matrix + C03's fragment (folded 12:31:29Z). **C05's audit
was still absent** at the 12:34:22Z poll — the
audit leg stays owed (§Owed). All four rows are now known byte-exact (§5, §6); C03's late
landing and the corpus-tree staging file it explains are recorded in the Addendum.

---

## 1. The invariant the delta must satisfy (measured, not assumed)

An index row is ``- `<file>.md` — <text>`` where `<text>` is the entry's own `- topic:`
head-block text with continuation lines space-joined to one line. That is what the lane's index
instrument measures: `reports/round-28/readme/sweep.py:60` (`ROW_RE`), `:61` (`TOPIC_RE`),
`:74-79` (`topic_of`, docstring "continuations space-joined"), and its control
"continuation lines space-joined" (`sweep.py:394-401`). Instrument sha256
`9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`; `--selftest` 12/12
(`python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12 checks passed`,
run this seat 2026-10-19); read-only in live mode (`sweep.py:28-30`, writes only inside
`--selftest` synthetic trees).

Baseline reading at authoring (all legs green, measured this seat 2026-10-19 at HEAD `dfb0719`):

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 21, "myth-symbol": 23,
       "synthesis": 29, "verification": 20}
rows 212 files 212; missing_from_index 0; topic_mismatch 0; orphan_rows 0; header_drift {}
totals_line 212 totals_ok True
footer total 212, dir_totals [21, 23, 25, 29, 20, 94]; footer_ok True; exit 0
```

The X00 connector measured the identical reading independently (~12:04Z,
`reports/round-39/cross/X00-connector.md:44-51`) and confirmed the mission vector
**21/23/25/29/24/94 is in the README's own section order** (`sweep.py:50-57`), i.e. only the
fifth slot moves 20 → 24 (`X00-connector.md:53-57`). P01's plan states the same
(`reports/round-39/plan/P01-plan.md:26-31`). Three seats, one reading — no off-by-order defect
in the target vector.

## 2. Before state — measured (claim-C receipt, counting commands)

`git rev-parse HEAD` → `dfb0719711204b5943432034bd80c8dc248acddd` (== the declared baseline
`dfb0719`, `reports/round-39/claims.json:7`; the r38 admission commit). `git status --porcelain
corpus/` → empty: the working tree is byte-identical to HEAD for every corpus path measured
here. Env for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, lane root.

### 2.1 Counting command 1 (verbatim, `reports/round-39/claims.json:17`)

```sh
$ ls corpus/knowledge/verification/*.md | wc -l
20
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21
23
25
29
20
94
$ find corpus/knowledge -name "*.md" -type f | wc -l
212
```

The loop order is the README footer vector's order (`corpus/README.md:509` = `21/23/25/29/20/94`,
linguistics-first), so the after vector is **21/23/25/29/24/94** — same string in the census
loop's order; writing it in any other order would not be.

### 2.2 Counting command 2 (verbatim, `reports/round-39/claims.json:17`)

```sh
$ python3 -B reports/round-28/readme/sweep.py
# exit 0; readings quoted in §1; readme_sha256 b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# exit 0; totals.files 212   (per-directory derivation: [21, 23, 25, 29, 20, 94])
```

The inventory counts markers, not verified facts (`corpus/README.md:510`); a marker count is not
a quality score. Entry quality is C05's and R01's evidence; this receipt owns **counts and their
reconciliation** only.

### 2.3 State pins (the before state is recoverable from git alone)

| pin | value | command |
|---|---|---|
| baseline commit | `dfb0719711204b5943432034bd80c8dc248acddd` | `git rev-parse HEAD` |
| corpus tree object | `0eb2392717cf0eb7e8476a1035b333abbb0a1a4b` | `git rev-parse HEAD:corpus/knowledge` |
| pinned path-manifest digest | `5c7b84e5231596bb180feae265891fbb5d5bae52cdeda901f7e2caf02c953c32` | `git ls-tree -r --name-only 0eb23927… \| sort \| sha256sum` |
| live manifest digest (same value) | `5c7b84e5…` (212 paths) | `find corpus/knowledge -name '*.md' -type f \| sort \| sed 's\|^corpus/knowledge/\|\|' \| sha256sum` |
| `corpus/README.md` digest | `b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74` | `sha256sum corpus/README.md` |
| README size | 536 lines / 127,797 bytes | `wc -lc corpus/README.md` |
| sweep instrument digest | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` | `sha256sum reports/round-28/readme/sweep.py` |

The two manifest digests agreeing is the measurement that the before state is exactly the
baseline commit's corpus. §8's A7 leg reads `new 0 / removed 0` against this pin at the before
state (observed, §8.1) — the pin is real, not decorative.

## 3. Line map of the pinned README (all edits reference these)

| line | content (pinned bytes) |
|---|---|
| 1, 3 | `# kotodama-shokunin corpus index` — **duplicated H1, carried defect** (`R36-README-DUPLICATE-HEADING`, `reports/round-37/op/defect-queue.json:103-131`; X00-7 `reports/round-39/cross/X00-connector.md:252-256`) — **not touched by this delta** |
| 5–12 | `revision: 2.1 — Round-36 timekeeping-instruments landing…` block |
| 14, 16 | duplicated `revision: 2.0` opening line — **carried defect** (`R36-README-E3-PLACEHOLDERS` family, same queue rows) — **not touched by this delta** |
| 149 / 173 / 199 / 226 / 258 / 281 | section headers `## linguistics/ (21)` / `## myth-symbol/ (23)` / `## culture-material/ (25)` / `## synthesis/ (29)` / `## verification/ (20)` / `## civilizations/ (94)` |
| 260–279 | the 20 verification rows, filename-sorted (260 `calibration-registry.md` … 279 `verification-method-overview.md`) |
| 505 | `Total knowledge entries: 212.` |
| 507 | `Counts checked 2026-10-19 from the repo root:` — date already current; **no edit** |
| 508 | the inventory command line — **no edit** |
| 509 | `(total 212 files; directory totals 21/23/25/29/20/94).` |
| 510 | `The inventory counts markers, not verified facts.` — **no edit** |
| 511–518 | superseded-reading paragraph, ends `…with the ten round-35 entries.` (records moves up to rev 2.0; rev 2.1 did **not** append to it) |
| 520–522 / 524–526 / 528–531 / 533–536 | dated `Index rows …` paragraphs (round-10 / round-19 / round-20 / round-35; 536 is the file's last line) |

## 4. Byte-exact, name-independent edits (apply in this order; rows in §5 land in the same motion)

### E1 — new revision block (insert between line 4 and line 5)

before (lines 3–5):

```
# kotodama-shokunin corpus index

revision: 2.1 — Round-36 timekeeping-instruments landing (2026-10-19): the routed
```

after (lines 3–6):

```
# kotodama-shokunin corpus index

revision: 2.2 — Round-39 verification-partition expansion landing (2026-10-19): the four
```

The full block is drafted in §7 with ⟨…⟩ slots filled at integration time. Insertion goes
**after the blank line following the duplicated H1 (line 3) and before `revision: 2.1`** — the
exact position rev 2.1 itself took above rev 2.0 (pinned lines 3–5). The duplicated-H1 and
duplicated-rev-2.0-line defects are inserted around, never repaired here (P01
`reports/round-39/plan/P01-plan.md:119-125`; X00-7).

### E2 — verification section header (line 258)

```
-## verification/ (20)
+## verification/ (24)
```

### E3 — totals line (line 505)

```
-Total knowledge entries: 212.
+Total knowledge entries: 216.
```

### E4 — counts footer (line 509 only)

```
-(total 212 files; directory totals 21/23/25/29/20/94).
+(total 216 files; directory totals 21/23/25/29/24/94).
```

Lines 507 (date — already 2026-10-19) and 508 (command) are unchanged; the sweep's footer leg
(`sweep.py:64-71,345-380`) compares the declared total and six directory totals against the live
tree and does not parse the date, but the block remains an honest present-tense claim only if
re-measured at landing — §8's post-apply sweep is that re-measurement.

### E5 — new dated index paragraph (append after line 536, the current last line)

```
Index rows re-measured 2026-10-19 at HEAD `⟨sha⟩` after the round-39 wave
(216 rows vs 216 files; the four new rows above added to the verification section;
0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches; partition
counts 21/23/25/29/24/94).
```

⟨sha⟩ and the reading are **measured at close** (the landing commit and the post-apply sweep);
if the sweep is not green, E5 is not written. Precedent for the shape: the round-35 paragraph at
`corpus/README.md:533-536`.

**Deliberately not in this delta:** (a) any edit to the superseded-reading paragraph (:511–518).
Revision 2.0 appended its move there (C11's E5, `reports/round-35/cov/C11-readme-delta.md:121-128`,
applied at `corpus/README.md:517-518`); revision 2.1 did not (its move lives only in its block,
:5-12). This delta follows the **most recent landing precedent (rev 2.1)** and records the move
in the §7 block only; if the integrator prefers the rev-2.0 style, the optional append after line
518 is `Revision 2.2 moved the totals 212 → 216 and \`## verification/\` 20 → 24 with the four
round-39 entries.` — one decision, either reading sweeps green. (b) A new `## Known gaps
(frontier)` bullet — revisions 1.7–2.1 added none; the round-39 coverage record belongs to this
receipt and S01's dossier, not the index. (c) Any repair of the carried H1/rev-2.0 duplication
defects (see E1).

## 5. The four row insertions (name-dependent — rule + tested generator, not guessed bytes)

**Rule.** Each new row is ``- `<file>.md` — <entry's own continuation-joined `- topic:` text>``
inserted where `<file>.md` sorts (ASCII) among the section's rows. Existing rows are
filename-sorted today (verified in §1's sweep: `orphan_rows 0`, and structurally in the synthetic
check, §5.3), so "filename order" and "row order" coincide.

**Anchors, measured by the generator's staged dry-run with all four landed entries staged as
real files under `.scratch/c06/staged-knowledge/`** (final poll 12:31:29Z; the generator run
read-only against the pinned README):

| proposed file (author fragment) | sorts | insert after line | after row |
|---|---|---|---|
| `append-only-record-verification.md` (C04) | **first** in section | **259** (header + 1 — the live first-in-section case) | — (header) |
| `contact-strata-verification-gate.md` (C03) | after `citation-format-and-source-registry.md` | **261** | `citation-format-and-source-registry.md` |
| `index-sweep-verification.md` (C02) | after `header-conformance-readings.md` | **266** | `header-conformance-readings.md` |
| `worked-example-verification.md` (C01) | **last** in section | **279** | `verification-method-overview.md` |

Staged-dry-run footer output, matching the mission vector exactly: totals `212 → 216`, footer
`(total 212 files; directory totals 21/23/25/29/20/94). → (total 216 files; directory totals
21/23/25/29/24/94).` — measured, not hand arithmetic. The generator recomputes all anchors
mechanically at integration time anyway — use it, not this table (C11's measured bugs, one
global bottom-up pass, larger `merged_index` first on shared anchors:
`reports/round-35/cov/C11-readme-delta.md:191-199`).

### 5.1 Generator (tested; integrator places it, e.g. `reports/round-39/readme/readme-delta.py`)

Read-only unless `--apply` names a path. Adapted from the round-35 C11 generator (field-tested
there end-to-end) narrowed to the verification partition; totals/footer always computed over all
six partitions.

```python
#!/usr/bin/env python3
"""Round-39 C06 — corpus/README.md index-delta generator (read-only by default).

Computes the exact corpus/README.md edits that reconcile the index to the live
tree when the four round-39 verification entries land: the verification section
header count, the missing index rows (with insertion anchors and byte-exact row
text = the entry's own continuation-joined `- topic:` text), the
`Total knowledge entries:` line, and the counts footer. Same row contract the
round-28 sweep measures (`reports/round-28/readme/sweep.py:60,61,74-79`).

    python3 readme-delta.py                     # text report
    python3 readme-delta.py --json              # machine delta
    python3 readme-delta.py --apply OUT.md      # write reconciled copy to OUT.md

Never writes unless --apply names a path.
"""
import argparse, glob, hashlib, json, os, re, sys

PARTS = ["linguistics", "myth-symbol", "culture-material",
         "synthesis", "verification", "civilizations"]
SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)$")
ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$")
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
TOTALS_RE = re.compile(r"^Total knowledge entries: (\d+)\.\s*$", re.M)
FOOTER_RE = re.compile(
    r"^\(total (\d+) files; directory totals ([0-9/]+)\)\.$", re.M)


def topic_of(path):
    m = TOPIC_RE.search(open(path, encoding="utf-8").read())
    return None if m is None else " ".join(m.group(1).split())


def read_index(lines):
    secs, cur = {}, None
    for i, l in enumerate(lines, 1):
        m = SECTION_RE.match(l)
        if m:
            cur = m.group(1)
            secs[cur] = {"hdr_line": i, "declared": int(m.group(2)), "rows": []}
        elif cur:
            r = ROW_RE.match(l)
            if r:
                secs[cur]["rows"].append({"file": r.group(1), "topic": r.group(2), "line": i})
    return secs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default="corpus/README.md")
    ap.add_argument("--root", default="corpus/knowledge")
    ap.add_argument("--parts", nargs="*", default=["verification"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--apply", metavar="OUT.md")
    a = ap.parse_args()

    raw = open(a.readme, "rb").read()
    lines = raw.decode("utf-8").split("\n")
    secs = read_index(lines)
    live = {}
    for p in PARTS:
        live[p] = sorted(os.path.basename(x)
                         for x in glob.glob(os.path.join(a.root, p, "*.md")))
    report = {"readme": a.readme, "root": a.root,
              "readme_sha256": hashlib.sha256(raw).hexdigest(),
              "live_counts": {p: len(live[p]) for p in PARTS}, "parts": {}}

    for p in a.parts:
        s = secs[p]
        rownames = [r["file"] for r in s["rows"]]
        missing = [f for f in live[p] if f not in rownames]
        extra = [f for f in rownames if f not in live[p]]
        merged = sorted(rownames + missing)
        entries = []
        line_of = {r["file"]: r["line"] for r in s["rows"]}
        for f in missing:
            idx = merged.index(f)
            pred = next((merged[j] for j in range(idx - 1, -1, -1)
                         if merged[j] in line_of), None)
            anchor_line = s["hdr_line"] + 1 if pred is None else line_of[pred]
            topic = topic_of(os.path.join(a.root, p, f))
            entries.append({"file": f, "insert_after_line": anchor_line,
                            "merged_index": idx, "after_row": pred,
                            "row": None if topic is None else "- `%s` — %s" % (f, topic),
                            "topic_resolved": topic is not None})
        report["parts"][p] = {
            "declared": s["declared"], "rows": len(s["rows"]), "live": len(live[p]),
            "header_line": s["hdr_line"],
            "header_before": lines[s["hdr_line"] - 1],
            "header_after": "## %s/ (%d)" % (p, len(live[p])),
            "missing_rows": entries, "ghost_rows": extra,
        }

    total = sum(len(live[p]) for p in PARTS)
    tl = next((i for i, l in enumerate(lines, 1) if TOTALS_RE.search(l)), None)
    report["totals_line"] = {"line": tl, "before": lines[tl - 1],
                             "after": "Total knowledge entries: %d." % total}
    fi = next((i for i, l in enumerate(lines, 1) if FOOTER_RE.search(l)), None)
    vec = "/".join(str(len(live[p])) for p in PARTS)
    report["footer"] = {"line": fi, "before": lines[fi - 1],
                        "after": "(total %d files; directory totals %s)." % (total, vec)}
    report["date_line"] = {"line": fi - 2, "before": lines[fi - 3]}

    if a.apply:
        out = list(lines)
        for p in a.parts:
            out[secs[p]["hdr_line"] - 1] = report["parts"][p]["header_after"]
        ops = [(e["insert_after_line"], e["merged_index"], e["row"])
               for p in a.parts for e in report["parts"][p]["missing_rows"]
               if e["row"] is not None]
        for idx, _mi, row in sorted(ops, key=lambda x: (-x[0], -x[1])):
            out.insert(idx, row)                    # global, bottom-up single pass
        tl2 = next(i for i, l in enumerate(out, 1) if TOTALS_RE.search(l))
        out[tl2 - 1] = "Total knowledge entries: %d." % total
        fi2 = next(i for i, l in enumerate(out, 1) if FOOTER_RE.search(l))
        out[fi2 - 1] = report["footer"]["after"]
        open(a.apply, "w", encoding="utf-8").write("\n".join(out))
        report["applied_to"] = a.apply

    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
    else:
        print("readme", report["readme_sha256"][:12], "live_counts", report["live_counts"])
        for p in a.parts:
            d = report["parts"][p]
            print("%-16s declared %d rows %d live %d  header %r -> %r  ghosts %s"
                  % (p, d["declared"], d["rows"], d["live"], d["header_before"],
                     d["header_after"], d["ghost_rows"]))
            for e in d["missing_rows"]:
                print("   + %-44s insert after line %-4d (after %s) row_chars=%s"
                      % (e["file"], e["insert_after_line"], e["after_row"],
                         "?" if e["row"] is None else len(e["row"])))
        print("totals", report["totals_line"]["before"], "->", report["totals_line"]["after"])
        print("footer", report["footer"]["before"], "->", report["footer"]["after"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`--apply` writes only the path given and only the three mechanical families (header, rows,
totals/footer line). E1/E5's prose is **not** written by it — apply those by hand from §4/§7 so
the prose is authored, not templated (the r35 placeholder lesson:
`reports/round-35/review`-filed defect, `SCORECARD.md:681-684` via
`reports/round-39/cross/X00-connector.md:97`).

### 5.2 Apply-order rules (measured in the r35 synthetic run; not re-derived here)

One global bottom-up pass over the whole file for all row insertions; on a shared anchor, larger
`merged_index` first; a row that sorts first in a section inserts after the header's blank line
(index = header line + 1). Entries land **before** the README delta in one motion, or the tree
sits in an intermediate red state (expected reds: entries-without-rows = 4 `missing_from_index`;
rows-without-entries = 4 ghosts — X00 integration steps 3→4→5,
`reports/round-39/cross/X00-connector.md:192-194`).

### 5.3 Acceptance of the generator itself (measured end-to-end this seat)

Synthetic tree `.scratch/c06/synth/` (copy of the live README + all 212 real entries + **5 probe
verification entries** with multi-line `- topic:` heads, chosen to cover the three hard cases:
`aaa-probe-first.md` first-in-section; `verification-method-overview-aaa.md` /
`-bbb.md` an adjacent pair sharing anchor 278; `index-sweep-verification.md` mid-section;
`worked-example-verification.md` tail; a redirected sweep copy `.scratch/c06/sweep-synth.py`
with only its `KNOWLEDGE` root re-pointed, the r35 C11 method):

- generator on the **live** tree: 0 missing rows, totals/footer before == after — no-op (the
  reader is calibrated), run twice (before and after a one-line cleanup edit, same result);
- generator on the synthetic tree: 5 rows emitted, anchors exactly `259 / 266 / 278 / 278 / 279`
  — all three hard cases hit;
- `--apply` to a scratch copy → sweep on the applied copy: **217 rows vs 217 files, 0 missing,
  0 ghosts, 0 topic mismatches, 0 header drift, totals 217, footer_ok True, exit 0**;
- independent post-apply structural check (own re-implementation, not the generator's own
  logic): all six sections filename-sorted, no duplicate rows, header == rows == files in every
  section, every row byte-equal to its entry's continuation-joined `- topic:` — **CLEAN**;
- negative controls, both observed: deleting one applied row → exit 1,
  `missing_from_index 1 ['verification/verification-method-overview-bbb.md']`; reverting the
  totals line to 212 → exit 1, `totals_line 212 totals_ok False`.

Scratch paths are disposable, not evidence; the generator source above is the tested bytes.

## 6. The four rows, byte-pinned to the landed draft fences

The row bytes below are **derived from the landed draft fences** (the fence's own `- topic:`,
continuation-joined) at the fragment digests pinned here. They are a cross-check for the
integrator, not a substitute for the generator: the landing equality is whatever the landed
bytes say at apply time, and §8's post-apply sweep is what certifies it
(`readme-prediction-vs-delivery` discipline). Full fragment sha256s and fence sha256s
measured this seat:

| fragment | sha256 (whole file) | fence sha256 | proposed path | row sha256 (full) |
|---|---|---|---|---|
| `reports/round-39/cov/C04-entry-4.md` | `94348f9601d7f92480e36027cfce86ec51e48bdbf5168fadb389589bed210ad4` | `31cf12f028c08eaf…` | `verification/append-only-record-verification.md` | `0ba6104ba1ef69cfe6589da63ad5fe6abc812fc633044219fe166b5ccf189d69` |
| `reports/round-39/cov/C03-entry-3.md` | `5ac5ae74534a0a953dc3bb4fabbf1b157fc82ea3614a84d0ee3cd7c184a83510` | `3fa037ae9f95de74…` | `verification/contact-strata-verification-gate.md` | `5784b191a690388a4d8a25c4060aeb4f06db05c9d29b4c7107a2c1b103f5eaa7` |
| `reports/round-39/cov/C02-entry-2.md` | `788af6bccbf2baab9b940f1fdd94cd1e054fc5d15d7637a2b8bcae08f1260342` | `c2b5756e234c112d…` | `verification/index-sweep-verification.md` | `8733b2cc1ff6ea0fd55267ee93f092fbe7873cf462d72b54aa9ec22b2e3c5e19` |
| `reports/round-39/cov/C01-entry-1.md` | `91ba710d95c9f4a8e0168236caa0d85042bc3534de160e6ea9c5a405d8c8185b` | `7e6beefd9aef1900…` | `verification/worked-example-verification.md` | `3c3fb3e6616b2f093619c1238b662177edd503d749b210b0d80b383c942005fe` |

(Table in landing-order = index-order; C03's fence sha equals the untracked corpus-tree
staging file's sha — see the Addendum.)

**Filename/allocation finding (resolved at the 12:31:29Z fold):** K01's scout recommended four
contact/taboo/dialect/translation topics (`reports/round-39/scout/K01-verification-gaps.md:192-196`),
and C01/C02/C04 self-derived different topics before K01 landed (P01's declared self-derive rule,
`reports/round-39/plan/P01-plan.md:44-49`; C01 and C02 record the absence explicitly; C04:
"Topic self-scouted"). **C03 then took K01's G1 explicitly as "the allocator of record"**
(`reports/round-39/cov/C03-entry-3.md` §1: "a conformance, not an independent pick") and names
the other three slugs, measuring four-way disjointness at its write time. The final allocation is
therefore: one K01-list topic (G1 → C03) + three self-derived topics (worked examples, index
sweeps, append-only records — all method gaps this lane exercises every round). K01's G2/G3/G4
remain **unallocated candidates** on the partition's gap list. No collision exists among the
four names or against the 20 existing entries (`ls` census §2.1; four distinct names; the final
census re-check stays the integrator's, X00 §5.2).

**The three derived rows (from the pinned draft fences):**

```
- `append-only-record-verification.md` — The verification procedure for **append-only records** — how a filed lane record (a round receipt, a telemetry snapshot, a recount ledger, an index revision, a LOG entry) is verified to have stayed unedited after filing: the open/closed record lifecycle (`open-at-seat-close` with a finalization note), the closing snapshot that fills an open record's fields as a new file, each filled value citing the durable artifact it was read from or recording `could-not-recover` with an owner and reason, the close digest (the record's SHA-256 at close time, recorded by the snapshot that closes it) that turns any later in-place edit into a detectable digest mismatch, and successor-row correction (a correction is a new row or snapshot with its own provenance; the superseded reading is preserved as the dated record it was). Method and lane policy only; canon belongs to lore-shokunin.
```

```
- `contact-strata-verification-gate.md` — The verification gate for **contact strata** in a built linguistic-cultural artifact: a culture packet that declares borrowed words, imported things, and the contact events that carried them is audited on three legs — the CHRONOLOGY leg (each stratum's adaptation stage must sit inside its declared window; the adaptation-freezes-phonology rule makes a form's shape dating evidence, so a shape that presupposes a sound change earlier than that change's declared window fails), the ORDERING leg (the strata's partial order must not contradict the declared event sequence; doublets and specialist-register licensing are read as evidence, never normalized away), and the THING-CHAIN leg (a borrowed word carries an object-and-knowledge chain — source, route, adoption, supply — and the two one-sided failures, a word without its thing and a thing without its word, are distinct findings); plus the declaration the gate requires before it runs, the failure-mode table, the fail-closed verdict mapping (a missing record is UNKNOWN, a contradiction is FAIL), the receipt the checker records, and the calibration that keeps the gate inside internal consistency — it audits a packet against its own declared history, never against real-world truth. Method and lane policy only; canon decisions belong to lore-shokunin.
```

```
- `index-sweep-verification.md` — The verification procedure for the **corpus-index sweep** — the recurring, selftested instrument that re-measures `corpus/README.md` against the file tree it indexes (index rows vs `.md` files, missing rows, ghost rows, duplicate rows, row-topic byte-equality, section-header counts, the totals line, the counts footer) — and the contract that keeps a sweep honest: every present-tense claim the index makes gets a measured leg, a claim with no leg is a finding rather than a pass, and a green reading is a digest-pinned reading of one tree state, never a state of the world. Covers the leg table, the three filed failures that wrote the contract (r19 paraphrase rows "asserted rather than measured", r20's never-committed `.scratch` sweep, r27's footer-blind green over rev 1.7's stale counts footer), the planted-control battery, green-reading discipline, and the append-only repair rule. Method and lane policy only; canon belongs to lore-shokunin.
```

```
- `worked-example-verification.md` — the verification procedure for **worked examples**: every `corpus/knowledge/` entry that ends in a worked example, micro-example, fixture, or filled worksheet owes a check that the example does four things — instantiates the decision rules it names, derives each stated consequence from a named rule id, rejects at least one counterexample the rules actually forbid, and carries the right label (NON-CANON for invented examples, source + locator for attested-world ones) — with a receipt recording what was checked; covers the five example classes measured in this corpus, per-class obligations, negative-control and mutation discipline, freshness versus copying, the receipt schema, and the failure modes this lane's own examples exhibit (uncited consequences, under-citation, green-by-construction controls, label drift, dead rules, stale verdicts, canon bleed). Method and lane policy only; canon decisions belong to lore-shokunin.
```

(All four rows above are in index order — the order they land in the README. Each was extracted
programmatically from its fragment's fence with the sweep's own topic rule
(`TOPIC_RE`, continuation-joined) and byte-checked against the staged row files; the §6 table
pins the digests.)

## 7. Drafted revision 2.2 block (fill ⟨…⟩ at integration time)

```
revision: 2.2 — Round-39 verification-partition expansion landing (2026-10-19): the four
round-39 entries landed — `⟨n1⟩.md`, `⟨n2⟩.md`, `⟨n3⟩.md`, `⟨n4⟩.md` — each naming the gap it
fills, with the author fragments under `reports/round-39/cov/` and the audit under
`reports/round-39/cov/C05-audit.md`. `## verification/` moved 20 → **24**; its four rows were
added in filename order with each entry's own `- topic:` text byte-equal; the totals line and
the counts footer moved 212 → **216** and the footer vector 21/23/25/29/20/94 →
**21/23/25/29/24/94**. Re-measured with `python3 reports/round-28/readme/sweep.py`: ⟨rows N vs
N files, 0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches, totals line
216, footer 216 / 21/23/25/29/24/94, exit 0 — measured at close⟩. Non-canon examples and
passing structural gates do not certify historical truth.
```

⟨…⟩ slots: the four filenames (from C01–C04 / X00's census — three known, §6) and the sweep
reading measured **after** the entries + README land. Do not write this block with a predicted
reading — the round-28 defect was exactly a present-tense claim that was never re-measured
(`corpus/README.md:43-61`, reason statement :52-55; P01 `reports/round-39/plan/P01-plan.md:117-118`).

## 8. Receipt — after-state assertion block and its negative control

### 8.1 The block (read-only; runs from the lane root; `PIN` is §2.3's tree object)

```python
python3 - <<'PY'
import pathlib, re, subprocess, json
PARTS=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
TARGET={'linguistics':21,'myth-symbol':23,'culture-material':25,'synthesis':29,'verification':24,'civilizations':94}
PIN='0eb2392717cf0eb7e8476a1035b333abbb0a1a4b'
fails=[]
def chk(leg, ok, detail):
    print(('PASS ' if ok else 'FAIL ')+leg+' :: '+detail)
    if not ok: fails.append(leg)
live={p:len(sorted(pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))) for p in PARTS}
chk('A1_census_counts', live==TARGET, f'live {live} target {TARGET}')
out=subprocess.run(['python3','-B','tools/source-audit-inventory.py','--json','--summary','--root','corpus/knowledge'],capture_output=True,text=True)
inv=json.loads(out.stdout)
chk('A2_inventory_total', inv['totals']['files']==216, f"totals.files {inv['totals']['files']} target 216 (exit {out.returncode})")
rd=pathlib.Path('corpus/README.md').read_text()
hdr={m.group(1):int(m.group(2)) for m in re.finditer(r'^## (linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/ \((\d+)\)$', rd, re.M)}
chk('A3_readme_headers', hdr==TARGET, f'headers {hdr}')
tot=[l for l in rd.splitlines() if l.startswith('Total knowledge entries')][0]
chk('A4_readme_total', tot=='Total knowledge entries: 216.', tot)
footline=[l for l in rd.splitlines() if re.match(r'^\(total \d+ files; directory totals ', l)]
chk('A5_readme_footer', any('(total 216 files; directory totals 21/23/25/29/24/94)' in l for l in footline), f'footer now: {footline[0] if footline else "absent"}')
rows={}
for p in PARTS:
    m=re.search(r'^## '+re.escape(p)+r'/ \(\d+\)\n(.*?)(?=^## )', rd, re.M|re.S)
    rows[p]=len(re.findall(r'^- `[^`]+\.md` — ', m.group(1), re.M))
chk('A6_rows_eq_files', rows==live, f'rows {rows} == files {live}')
pinned=set('corpus/knowledge/'+l for l in subprocess.run(['git','ls-tree','-r','--name-only',PIN],capture_output=True,text=True).stdout.split('\n') if l)
liveset=set(f'corpus/knowledge/{p}/{f.name}' for p in PARTS for f in pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))
new=sorted(liveset-pinned); gone=sorted(pinned-liveset)
chk('A7_delta_4_files', len(new)==4 and not gone and all('/verification/' in n for n in new), f'new {len(new)} removed {len(gone)}')
for n in new: print('  + '+n)
print('VERDICT', 'GREEN' if not fails else 'RED legs '+str(fails))
PY
```

**Negative control — observed at the before state (this seat's run, 2026-10-19):**

```
FAIL A1_census_counts :: live {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 20, 'civilizations': 94} target {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A2_inventory_total :: totals.files 212 target 216 (exit 0)
FAIL A3_readme_headers :: headers {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 20, 'civilizations': 94}
FAIL A4_readme_total :: Total knowledge entries: 212.
FAIL A5_readme_footer :: footer now: (total 212 files; directory totals 21/23/25/29/20/94).
PASS A6_rows_eq_files :: rows {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 20, 'civilizations': 94} == files {'linguistics': 21, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 20, 'civilizations': 94}
FAIL A7_delta_4_files :: new 0 removed 0
VERDICT RED legs ['A1_census_counts', 'A2_inventory_total', 'A3_readme_headers', 'A4_readme_total', 'A5_readme_footer', 'A7_delta_4_files']
```

Readings: (a) every after-leg **fails at the before state**, so a later GREEN is informative, not
green-by-construction; (b) A6 is an equality *invariant* — green now, required to stay green
after; (c) A7 read `new 0 / removed 0`, the positive proof that the §2.3 pin matches the live
tree. The block shells out only to `git ls-tree` and the read-only inventory tool; it writes
nothing. It counts rows — it does **not** compare row text with `- topic:` bytes; that verbatim
leg is §1's sweep and §5.3's structural check, and a count-only green must never be quoted as
index-text reconciliation (the r19 lesson, `corpus/README.md:95-101`).

### 8.2 The integrator's acceptance sequence (claim C thresholds, `reports/round-39/claims.json:18`)

1. C05's audit over all four drafts lands, clean or defect-listed (audit leg — C05/R01's
   evidence; absent at this seat's cut).
2. Apply the four entries (X00 step 3), then E1–E5 + the four generated rows in one motion
   (X00 steps 3→4 are NOT free — see §5.2).
3. `python3 -B reports/round-28/readme/sweep.py` → **must** read `rows 216 files 216`,
   `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
   `totals_line 216 totals_ok True`, footer `{total 216, dir_totals [21, 23, 25, 29, 24, 94]}`,
   `footer_ok True`, exit 0. `ls corpus/knowledge/verification/*.md | wc -l` → **24**.
4. Diff the landed README against this draft before trusting the sweep (X00-3:
   `reports/round-39/cross/X00-connector.md:230-234` — the r35 apply left placeholder lines the
   sweep then caught; the r36 staged prediction diverged from the delivered digest).
5. Re-run §8.1's block → VERDICT GREEN; fill §7's ⟨…⟩ and write E5 with the landing sha.
6. Inventory cross-check: `python3 -B tools/source-audit-inventory.py --json --summary --root
   corpus/knowledge` → `totals.files 216`.

Until step 3/5 read green on the landed tree, **no after-count in this fragment may be quoted as
measured** — every after value here is target or generated, never landed.

## 9. Limits and cross-fragment consistency

- All before figures are point-in-time at `dfb0719` with a byte-clean corpus tree; any landing
  invalidates §2 until re-measured (the §2.3 pins make the before state recoverable from git
  alone). The three §6 row bytes are draft-derived: if an executor fragment is amended before
  landing, the pinned fence digests detect it and the generator re-emits the row mechanically.
- This receipt certifies **counts and their reconciliation** — never entry quality, source
  resolvability, or canon status (`corpus/README.md:510`; the audit is C05's, the adversarial
  fabrication hunt is R01's, the admission verdict is the integrator's per REGIMEN.md:41-43).
- The census command globs only `*.md` at each partition's top level; the inventory and
  `find -type f` legs are the wider nets and agree at 212 (nesting case closed at this baseline
  by the r35 receipt's measurement — `reports/round-35/cov/C15-receipt.md:273-278` — re-derivable
  with the same two commands).
- No `reports/round-*/run-validation.py` was executed anywhere by this seat (absolute rule). The
  round's close-time runner does not exist yet and is the integrator's artifact (X00 §2 #6,
  `reports/round-39/cross/X00-connector.md:101`); REGIMEN.md:57's exit-0-at-close requirement
  stands regardless of this fragment.
- Cross-fragment readings, no divergence found: K01 §5 "Index implications for C06" states the
  identical target set (24 / 216 / `21/23/25/29/24/94` / filename order / byte-equal topics /
  sweep green — `reports/round-39/scout/K01-verification-gaps.md:186-191`); P01 §1.4 C06
  obligations (delta legs a–e + post-apply-sweep rule + do-not-repair list) are all carried
  (`reports/round-39/plan/P01-plan.md:110-125`); X00 collision #2 names this delta's exact edit
  set and control (`reports/round-39/cross/X00-connector.md:97`), its §0 confirms this §1/§2
  baseline, and X00-3/X00-7 are adopted (§4-E1, §8.2-4). No peer fragment proposes a different
  count-line, vector order, or row rule.

## Addendum — second read: C03's corpus-tree draft (2026-10-19T12:29:48Z)

**Observation (this seat's own measurement).** Between the §8.1 negative-control run (~12:24–12:26Z)
and this read, an untracked file appeared at `corpus/knowledge/verification/C03-draft.md`
(`git status --porcelain` → `?? corpus/knowledge/verification/C03-draft.md`; sha256
`3fa037ae9f95de7449f4df937ed2ef0871bd85d75194c15f79c76053df3c841f`; 165 lines / 33,526 bytes;
mtime 09:28 local). Its `- topic:` is the **contact-strata verification gate** — K01's G1
recommendation — so the C04 fragment's prose ("with C01–C03's three") and K01's allocation
picture resolve as: C03 took G1, G2/G3/G4 remain unallocated candidates.

**Why no §2–§8 measurement above is invalidated.** The file is **untracked**: every §2.3 pin is a
git-object pin, and `git ls-tree -r --name-only 0eb23927…` still enumerates exactly the 212
before-state paths — the before state remains recoverable from git alone, which is the property
§2.3 claims. §8.1's control run measured that pinned before state and predates this write; it
stands as the before-state control.

**The live working tree now reads (measured 12:29Z):** census verification **21** / total **213**;
the generator on the live tree reports exactly one missing row (`C03-draft.md`, first-in-section
anchor 259) and would move totals 212 → 213 — the **expected intermediate red** (an
entry-without-rows state; X00 §5.2: "an intermediate sweep is expected red"). A7 re-run reads
`new 1 ['corpus/knowledge/verification/C03-draft.md'] removed 0`. None of this is a landing:
the shared rules route entry bytes through fenced fragments applied by the integrator
(`reports/round-39/targets.json:6`), and C03's out-path fragment `cov/C03-entry-3.md` **still
does not exist** at this poll.

**Recorded, not absorbed.** Whether the corpus-tree draft is C03's intended staging channel, and
what its final filename will be (the draft carries no landing-path declaration this seat could
find), are C03's/X00's/R01's and the integrator's to disposition. For this delta the consequence
is mechanical only: the fourth row is emitted from the **landed bytes under their final name**,
whatever the integrator applies — `C03-draft.md` as a name must not survive into the index (an
index row for `C03-draft.md` would freeze a staging filename into the corpus record), and the
§7 block's ⟨n3⟩ slot waits for that final name.

**Third read — resolved (12:31:29Z).** C03's out-path fragment
`reports/round-39/cov/C03-entry-3.md` landed. It declares the final filename
`contact-strata-verification-gate.md` (K01's G1, "taken as the allocator of record"), its sort
position ("third, between `citation-format-and-source-registry.md` and
`costume-era-consistency-gate.md`" — the generator's staged dry-run confirms: anchor 261), and
measures four-way slug disjointness against C01/C02/C04. **Provenance of the corpus-tree file
solved by digest:** the untracked `corpus/knowledge/verification/C03-draft.md` sha256
(`3fa037ae…`) is **byte-identical to C03's fragment fence** (`3fa037ae9f95de74…`, §6 table) —
the corpus-tree file is C03's own draft bytes staged in-corpus, not a foreign write. It remains
an untracked staging artifact in a shared surface: the integrator removes or renames it when
applying C03's fence (the final entry lands under the declared name; the index never sees
`C03-draft.md`). With C03 folded, all four rows are known byte-exact (§5 anchors, §6 rows) and
the §5 staged dry-run reads the full target: header 24, totals 216, footer
`21/23/25/29/24/94`. C05's audit remains the one owed C-block leg.

## Owed

- ~~`reports/round-39/cov/C03-entry-3.md`~~ — **resolved at the 12:31:29Z fold**: the fragment
  landed, declaring `contact-strata-verification-gate.md` (K01's G1, allocator-of-record
  conformance); its fence sha matches the untracked corpus-tree staging file byte-for-byte
  (Addendum, third read). All four rows are known (§5, §6); the fourth row's landing bytes are
  C03's fence under its declared name. Still owed from this item: the integrator's removal or
  rename of the untracked `corpus/knowledge/verification/C03-draft.md` staging file at apply
  time, so no `C03-draft.md` row can ever exist.
- `reports/round-39/cov/C05-audit.md` — the audit leg of claim C's threshold ("entries audited
  before landing", `reports/round-39/claims.json:16`); absent at this seat's cut. Apply gate:
  entries land only after C05 is clean or its defects are filed (X00 step 3).
- The integrator's application of §4/§5/§7 to `corpus/README.md` + the four entries, then the
  §8.2 sequence (post-apply sweep + GREEN §8.1 + diff-vs-draft). Nothing is landed until then.
- `reports/round-39/run-validation.py` — not among claim C's counting commands but required by
  `REGIMEN.md:57` at close; integrator-authored, isolated-copy execution only.
- Optional integrator decision recorded in E5-note: append-style for the superseded paragraph
  (rev-2.0 style) vs block-only record (rev-2.1 style, this draft's default).

## Citations

- `reports/round-39/claims.json:7` (baseline `dfb0719`), `:9` (axes), `:13-18` (claim C: `:15`
  before, `:16` after_required, `:17` counting commands, `:18` thresholds), `:26-27` (non_goals)
- `reports/round-39/targets.json:4-9` (shared rules), `:68-74` (seat C06)
- `REGIMEN.md:27-30` (per-round contract), `:41-43` (admit rule), `:57` (close-time runner)
- `corpus/README.md` pinned bytes: `:1,3` (duplicated H1), `:5-12` (rev 2.1), `:14,16`
  (duplicated rev-2.0 line), `:258` (`## verification/ (20)`), `:260-279` (20 rows), `:281`,
  `:505` (totals), `:507-510` (counts footer block), `:511-518` (superseded paragraph, ends at
  rev 2.0), `:520-536` (dated index paragraphs), `:43-61` (rev 1.8's stale-footer defect record),
  `:95-101` (r19 paraphrase-rows defect). Read at sha256
  `b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74` (536 lines / 127,797 bytes)
- `reports/round-28/readme/sweep.py:28-30,47,50-57,60-66,74-79,119-212,394-401,411-419`;
  instrument sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`
- Peer fragments read, not absorbed: `reports/round-39/scout/K01-verification-gaps.md`
  (§4 recommendations `:77-168`, §5 contract inputs + index implications + filename
  recommendations `:179-196`), `reports/round-39/plan/P01-plan.md` (§1.1 baseline `:24-40`,
  §1.2 self-derive rule `:44-55`, §1.4 C06 obligations `:110-125`, §1.5 `:127-132`), 
  `reports/round-39/cross/X00-connector.md` (§0 baseline controls `:42-57`, collision #2 `:97`,
  steps 3–5 `:192-194`, §5.2 census `:204-209`, X00-3 `:230-234`, X00-7 `:252-256`),
  `reports/round-39/cov/C01-entry-1.md`, `reports/round-39/cov/C02-entry-2.md`,
  `reports/round-39/cov/C04-entry-4.md` (proposed paths + fenced entry bytes; digests in §6),
  `reports/round-39/cov/C03-entry-3.md` (final name declaration + disjointness measurement §1,
  folded at 12:31:29Z)
- Filed precedent: `reports/round-35/cov/C11-readme-delta.md` (the generator's ancestor, apply
  order bugs `:191-199`, synthetic acceptance `:356-391`), `reports/round-35/cov/C15-receipt.md`
  (receipt shape, pins `:78-92`, A-block + negative control `:150-207`, nesting limit `:273-278`),
  `reports/round-37/op/defect-queue.json:242-251` (`readme-prediction-vs-delivery`), `:103-131`
  (R36 README carried defects), `SCORECARD.md:681-684` (r35 placeholder root cause, via X00)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  HEAD `dfb0719`): `git rev-parse HEAD`; `git status --porcelain corpus/` (empty); `git rev-parse
  HEAD:corpus/knowledge`; `git ls-tree -r --name-only 0eb23927… | sort | sha256sum`; `find
  corpus/knowledge -name '*.md' -type f | sort | sed 's|^corpus/knowledge/||' | sha256sum`;
  `sha256sum corpus/README.md reports/round-28/readme/sweep.py`; `wc -lc corpus/README.md`;
  `grep -n '^## \|^Total knowledge entries\|^Counts checked\|^(total '` corpus/README.md; the
  `claims.json:17` census loop + verification-only count + `find | wc -l` (§2.1); `python3 -B
  tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 212`
  (exit 0); `python3 -B reports/round-28/readme/sweep.py` → green 212/212 exit 0;
  `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12; generator no-op on the live
  tree (twice); synthetic +5 tree: anchors 259/266/278/278/279, `--apply` + redirected sweep
  217/217 exit 0, negative controls exit 1 (`missing_from_index 1`; `totals_ok False`),
  independent structural check CLEAN; staged 3-known dry-run (anchors 259/266/279); fence/row
  digest extraction (§6 values); the §8.1 A-block (RED, §8.1 output); `ls`/`find` polls of
  `reports/round-39/**` (§Owed timestamps); Addendum second read (12:29:48Z): `git status
  --porcelain` (`?? corpus/knowledge/verification/C03-draft.md` + `?? reports/round-39/`),
  `sha256sum` + `wc -lc` over that draft, `grep -n "landing path|final name|rename|proposed|
  C06|README|revision 2.2|integrator"` over it (no landing-path declaration found), live census
  (21/213), generator on the live tree (1 missing row, anchor 259), A7 re-run (`new 1`,
  `removed 0`); third read (12:31:29Z): C03 fragment landed — fence extracted, fourth row
  derived (row_chars 1352, sha `5784b191…`), staged dry-run with all four (anchors
  259/261/266/279; totals 212 → 216; footer vector 21/23/25/29/24/94), fence-sha match against
  the corpus-tree staging file (`3fa037ae…` both sides)
- Scratch (disposable, not evidence): `.scratch/c06/readme-delta.py` (source = §5.1),
  `.scratch/c06/synth/**`, `.scratch/c06/sweep-synth.py`, `.scratch/c06/staged-knowledge/`,
  `.scratch/c06/row-*.md`, `.scratch/c06-inventory.json`
