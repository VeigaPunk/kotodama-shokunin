- Seat: C11 | executor | claim C (coverage) | date 2026-10-19 | baseline 4a7aede

# C11 — `corpus/README.md` reconciliation draft (+6 culture-material, +4 myth-symbol)

Integrator-applied draft. This seat wrote **no** byte of `corpus/README.md`; every edit
below is a before/after block plus a tested generator that recomputes the row
bytes and anchors from the live tree at integration time.

Deliverable for the mission "the exact `corpus/README.md` count-line and index
deltas for +6/+4 as before/after blocks (integrator applies)": §2 holds the five
name-independent edits byte-exact against the pinned README (sha256
`053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`, 106 218 bytes,
493 lines, measured at HEAD `4a7aede`); §3 holds the ten row insertions as a rule
plus a generator that emits each row's exact bytes and insertion line; §4 is the
acceptance procedure, measured end-to-end on a synthetic +10 tree.

## 0. The invariant the delta must satisfy (measured, not assumed)

An index row is `- \`<file>.md\` — <text>` where `<text>` is the entry's own
`- topic:` head-block text with continuation lines space-joined to one line.
That is what the lane's index instrument measures:
`reports/round-28/readme/sweep.py:21` (`ROW_RE`), `:22` (`TOPIC_RE`),
`:74-79` (`topic_of`), `:140` (equality test), and its control
`control: continuation lines space-joined` (`sweep.py:398-401`). Instrument
digest `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`,
`--selftest` 12/12 (`python3 -B reports/round-28/readme/sweep.py --selftest`),
read-only in live mode (writes only inside `--selftest` synthetic trees).

Baseline reading at authoring (all three methods agree):

| method | command | reading |
|---|---|---|
| plain count | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21 / 19 / 18 / 29 / 20 / 94 = 201 |
| lane inventory | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 201` |
| index instrument | `python3 -B reports/round-28/readme/sweep.py` | `rows 201 files 201`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_ok True`, `footer_ok True`, exit 0 |

Structural facts verified programmatically at the pin: rows are filename-sorted
(ASCII ascending) inside every section; 0 duplicate rows; every row byte-equal to
its entry's continuation-joined `- topic:`; the last row of each section is the
section's final line before the next blank; section headers carry the live count
in parentheses.

## 1. Line map of the pinned README (all edits below reference these)

| line | content (pinned bytes) |
|---|---|
| 1 | `# kotodama-shokunin corpus index` |
| 3 | `revision: 1.9 — Round-28 register-lexicon-ceiling landing (2026-10-18): the` (start of the newest revision block, lines 3–15) |
| 147 | `## myth-symbol/ (19)` |
| 149–167 | 19 myth-symbol rows |
| 169 | `## culture-material/ (18)` |
| 171–188 | 18 culture-material rows |
| 469 | `Total knowledge entries: 201.` |
| 471 | `Counts checked 2026-10-18 from the repo root:` |
| 472 | `` `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` `` |
| 473 | `(total 201 files; directory totals 21/19/18/29/20/94).` |
| 475–480 | `Superseded reading, preserved as the dated record it was: …` (ends `the totals 200 → 201 and \`## linguistics/\` 20 → 21 with the ceiling entry.`) |
| 482–493 | three dated `Index rows …` paragraphs (last: round-20 re-measurement) |

## 2. Byte-exact, name-independent edits (apply in this order)

### E1 — new revision block (insert between line 2 and line 3)

before (lines 1–3):

```
# kotodama-shokunin corpus index

revision: 1.9 — Round-28 register-lexicon-ceiling landing (2026-10-18): the
```

after (lines 1–6):

```
# kotodama-shokunin corpus index

revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
round-35 entries landed — culture-material six (`⟨c01⟩.md`, `⟨c02⟩.md`, `⟨c03⟩.md`,
`⟨c04⟩.md`, `⟨c05⟩.md`, `⟨c06⟩.md`) and myth-symbol four (`⟨c07⟩.md`, `⟨c08⟩.md`,
```

…continued in §5 (the block is drafted there in full; ⟨…⟩ slots are filled from
the C01–C10 fragments). Precedent for block shape and the closing sentence:
`corpus/README.md:3-15` (revision 1.9). Revision numbering follows the file's
0.1-step convention (`1.4→1.5→1.6→1.7→1.8→1.9`), so the next value is `2.0`;
if the integrator prefers `1.10`, that is a naming decision, not a byte risk.

### E2 — myth-symbol header (line 147)

```
-## myth-symbol/ (19)
+## myth-symbol/ (23)
```

### E3 — culture-material header (line 169)

```
-## culture-material/ (18)
+## culture-material/ (24)
```

### E4 — totals line (line 469)

```
-Total knowledge entries: 201.
+Total knowledge entries: 211.
```

### E5 — counts footer (lines 471, 473, and the tail of the superseded paragraph at 480)

```
-Counts checked 2026-10-18 from the repo root:
+Counts checked 2026-10-19 from the repo root:
```

```
-(total 201 files; directory totals 21/19/18/29/20/94).
+(total 211 files; directory totals 21/23/24/29/20/94).
```

```
-re-measured by the command above and a plain `find` count. Revision 1.9 moved
-the totals 200 → 201 and `## linguistics/` 20 → 21 with the ceiling entry.
+re-measured by the command above and a plain `find` count. Revision 1.9 moved
+the totals 200 → 201 and `## linguistics/` 20 → 21 with the ceiling entry.
+Revision 2.0 moved the totals 201 → 211, `## myth-symbol/` 19 → 23 and
+`## culture-material/` 18 → 24 with the ten round-35 entries.
```

Line 472 (the inventory command) and line 474 (`The inventory counts markers,
not verified facts.`) are unchanged. The superseded-reading paragraph keeps the
199/19 record verbatim — the edit only appends, per the file's own rule
(`corpus/README.md:475-480`; the round-19 lesson "must re-measure, not
arithmetic-guess, and must not silently rewrite the round-10 receipt it
supersedes (append a new dated block)", `corpus/lessons/round-19.md:115`).

### E6 — new dated index paragraph (append after line 493, the round-20 paragraph)

```
Index rows re-measured 2026-10-19 at HEAD `⟨sha⟩` after the round-35 wave
(211 rows vs 211 files; the ten new rows above added to the culture-material and
myth-symbol sections; 0 missing, 0 ghosts, 0 duplicate rows, 0 header drift,
0 topic mismatches; partition counts 21/23/24/29/20/94).
```

⟨sha⟩ and the reading are **measured at close**, never carried over from this
draft; if the sweep is not green, E6 is not written. Precedent for the shape:
`corpus/README.md:486-493`.

Deliberately **not** in this delta: a new `## Known gaps (frontier)` bullet. The
last such bullet is the round-20 one (`corpus/README.md:447-467`); revisions
1.7–1.9 added none, and the round-35 coverage record belongs to the C receipt
(C15/S01), not the index. If the integrator wants one, that is an addition to
route, not a reconciliation gap.

## 3. The ten row insertions (name-dependent)

**Rule.** Each new row is `- \`<file>.md\` — <entry's own continuation-joined
`- topic:` text>` inserted where `<file>.md` sorts (ASCII) among that section's
existing rows. Existing rows are filename-sorted today (verified, §0), so
"filename order" and "row order" are the same thing.

**Anchors (current rows, by line, pinned README).**

myth-symbol (insert among 149–167; a name sorting before `animal-symbolism.md`
goes after line **148**, i.e. after the header's blank line):

```
149 animal-symbolism.md          153 cosmology-cosmography.md     158 hero-journey-variants.md     163 pantheon-archetypes.md
150 celestial-symbolism-calendars 154 creation-myths-taxonomy.md  159 motif-index-usage.md        164 plant-symbolism.md
151 color-symbolism.md           155 direction-symbolism.md      160 myth-folktale-genres.md     165 ritual-liminality.md
152 comparative-frameworks.md    156 divination-omen-systems.md  161 myth-ritual-theories.md     166 symbolism-synthesis-method.md
                                 157 flood-traditions.md          162 number-symbolism.md         167 trickster.md
```

culture-material (insert among 171–188; a name sorting before
`adornment-body-codes.md` goes after line **170**):

```
171 adornment-body-codes.md              177 dress-through-eras.md              183 sumptuary-law-rank-display.md
172 architecture-settlement-lexicon.md   178 era-periodization-models.md       184 textile-technology.md
173 calendar-festival-systems.md         179 garment-lexicon-crosslinguistic.md 185 trade-economy-lexicon.md
174 costume-semiotics.md                 180 material-culture-inference-method.md 186 transport-mobility-lexicon.md
175 craft-artisan-lexicon.md             181 music-instrument-lexicon.md       187 vessel-container-lexicon.md
176 cuisine-food-lexicon.md              182 ritual-garments.md                188 warrior-material-culture.md
```

Line numbers are as of the pinned README and **shift as soon as anything above
them is inserted** — use the generator, not hand arithmetic.

**Apply order (two bugs measured in the synthetic run; do not "fix" these by
hand):** (1) all row insertions must run in **one global bottom-up pass** over the
whole file — a per-section pass shifts later sections' anchors and lands rows in
the wrong section (measured: a culture-material row appeared inside myth-symbol,
sweep `orphan_rows 1`, `missing_from_index 1`); (2) two new rows sharing one
anchor must be inserted with the larger merged index first (descending), or the
pair comes out alphabetically reversed (measured on the probe pair anchored at
line 179); (3) a row that sorts first in a section must be inserted **after** the
header's blank line (index = header line + 1), not between header and blank.

**Generator (tested; integrator places it, e.g.
`reports/round-35/readme/readme-delta.py`).** Read-only unless `--apply` names a
path. `--json` emits the machine delta (per part: header before/after, each
missing row with `insert_after_line`, `merged_index`, `after_row`, and the exact
`row` bytes, plus the totals and footer replacements).

```python
#!/usr/bin/env python3
"""Round-35 C11 — corpus/README.md index-delta generator (read-only by default).

Computes the exact corpus/README.md edits that reconcile the index to the live
tree: section-header counts, missing index rows (with insertion anchors and the
byte-exact row text), the `Total knowledge entries:` line, and the counts footer.
Row text is the entry's own `- topic:` head-block text with continuation lines
space-joined — the equality `reports/round-28/readme/sweep.py` measures.

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
TOTALS_RE = re.compile(r"^Total knowledge entries: (\d+)\.$")
FOOTER_RE = re.compile(r"^\(total (\d+) files; directory totals ([0-9/]+)\)\.$")


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
    ap.add_argument("--parts", nargs="*", default=None,
                    help="partitions to diff rows for (default: all in the README)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--apply", metavar="OUT.md")
    a = ap.parse_args()

    raw = open(a.readme, "rb").read()
    lines = raw.decode("utf-8").split("\n")
    secs = read_index(lines)
    parts = a.parts or [p for p in PARTS if p in secs]
    live = {}
    for p in PARTS:
        live[p] = sorted(os.path.basename(x)
                         for x in glob.glob(os.path.join(a.root, p, "*.md")))
    report = {"readme": a.readme, "root": a.root,
              "readme_sha256": hashlib.sha256(raw).hexdigest(),
              "live_counts": {p: len(live[p]) for p in PARTS}, "parts": {}}

    for p in parts:
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
                            "merged_index": idx,
                            "after_row": pred, "row": None if topic is None else
                            "- `%s` — %s" % (f, topic),
                            "topic_resolved": topic is not None})
        report["parts"][p] = {
            "declared": s["declared"], "rows": len(s["rows"]), "live": len(live[p]),
            "header_line": s["hdr_line"],
            "header_before": lines[s["hdr_line"] - 1],
            "header_after": "## %s/ (%d)" % (p, len(live[p])),
            "missing_rows": entries, "ghost_rows": extra,
        }

    total = sum(len(live[p]) for p in PARTS)
    tl = next((i for i, l in enumerate(lines, 1) if TOTALS_RE.match(l)), None)
    report["totals_line"] = {"line": tl, "before": lines[tl - 1],
                             "after": "Total knowledge entries: %d." % total}
    fi = next((i for i, l in enumerate(lines, 1) if FOOTER_RE.match(l)), None)
    vec = "/".join(str(len(live[p])) for p in PARTS)
    report["footer"] = {"line": fi, "before": lines[fi - 1],
                        "after": "(total %d files; directory totals %s)." % (total, vec)}
    report["date_line"] = {"line": fi - 2, "before": lines[fi - 3]}

    if a.apply:
        out = list(lines)
        for p in parts:
            out[secs[p]["hdr_line"] - 1] = report["parts"][p]["header_after"]
        ops = [(e["insert_after_line"], e["merged_index"], e["row"])
               for p in parts for e in report["parts"][p]["missing_rows"]
               if e["row"] is not None]
        for idx, _mi, row in sorted(ops, key=lambda x: (-x[0], -x[1])):
            out.insert(idx, row)                    # global, bottom-up single pass
        tl2 = next(i for i, l in enumerate(out, 1) if TOTALS_RE.match(l))
        out[tl2 - 1] = "Total knowledge entries: %d." % total
        fi2 = next(i for i, l in enumerate(out, 1) if FOOTER_RE.match(l))
        out[fi2 - 1] = report["footer"]["after"]
        open(a.apply, "w", encoding="utf-8").write("\n".join(out))
        report["applied_to"] = a.apply

    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
    else:
        print("readme", report["readme_sha256"][:12], "live_counts", report["live_counts"])
        for p in parts:
            d = report["parts"][p]
            print("%-16s declared %d rows %d live %d  header %r -> %r  ghosts %s"
                  % (p, d["declared"], d["rows"], d["live"], d["header_before"],
                     d["header_after"], d["ghost_rows"]))
            for e in d["missing_rows"]:
                print("   + %-40s insert after line %-4d (after %s) row_chars=%s"
                      % (e["file"], e["insert_after_line"], e["after_row"],
                         "?" if e["row"] is None else len(e["row"])))
        print("totals", report["totals_line"]["before"], "->", report["totals_line"]["after"])
        print("footer", report["footer"]["before"], "->", report["footer"]["after"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Note on `--apply`: it writes only the path given and only the three
name-independent families (headers, rows, totals/footer line). E1/E5's appended
sentence/E6 are **not** written by it — apply them by hand from §2/§5 so the
prose is authored, not templated. The round-35 rule is integrator-applies-in-tree;
`--apply` exists so the integrator can dry-run on a copy first.

## 4. Acceptance for the reconciliation (measured end-to-end)

Run after applying, from the repo root, `export TMPDIR=$PWD/.scratch`:

```sh
python3 -B reports/round-28/readme/sweep.py --selftest   # 12/12, exit 0
python3 -B reports/round-28/readme/sweep.py              # exit 0 required
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
grep -c '^- `[A-Za-z0-9._-]*\.md`' corpus/README.md       # 211 (peer C16's row count)
```

Required readings: `parts {"civilizations": 94, "culture-material": 24,
"linguistics": 21, "myth-symbol": 23, "synthesis": 29, "verification": 20}`,
`rows 211 files 211`, `missing_from_index 0`, `topic_mismatch 0`,
`orphan_rows 0`, `header_drift {}`, `totals_line 211 totals_ok True`,
`footer_ok True`, exit 0; inventory `totals.files 211`.

Proof this procedure works — synthetic +10 tree in `.scratch/c11/synth/`
(a copy of the live README plus all 201 real entries plus 10 probe entries,
6 culture-material + 4 myth-symbol, with multi-line `- topic:` heads):

- generator on the **live** tree: 0 missing rows in all six sections, totals and
  footer before == after (no-op) — the reader is calibrated;
- generator on the synthetic tree: 10 rows emitted, anchors correct including the
  three hard cases (first-in-section → header+1; adjacent pair sharing an anchor;
  tail insert);
- `--apply` to a scratch copy, then a scratch copy of the r28 sweep with only its
  `KNOWLEDGE` root redirected (`.scratch/c11/sweep-synth.py`): **211 rows vs 211
  files, 0 missing, 0 topic mismatches, 0 orphans, 0 header drift, totals 211,
  footer ok, exit 0**;
- independent post-apply check (own re-implementation): every section
  filename-sorted, no duplicate rows, no row directly after a header, every row
  byte-equal to its entry's continuation-joined `- topic:` — no findings;
- negative controls: deleting one inserted row → exit 1,
  `missing_from_index 1 ['culture-material/bead-currency-systems.md']`; reverting
  the totals line to 201 → exit 1, `totals_line 201 totals_ok False`.

## 5. Drafted revision 2.0 block (fill ⟨…⟩ at integration time)

```
revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
round-35 entries landed — culture-material six (`⟨c01⟩.md`, `⟨c02⟩.md`, `⟨c03⟩.md`,
`⟨c04⟩.md`, `⟨c05⟩.md`, `⟨c06⟩.md`) and myth-symbol four (`⟨c07⟩.md`, `⟨c08⟩.md`,
`⟨c09⟩.md`, `⟨c10⟩.md`) — each naming the gap it fills, with the author fragments
under `reports/round-35/cov/` and the audits under `reports/round-35/review/`.
`## culture-material/` moved 18 → **24** and `## myth-symbol/` moved 19 → **23**;
their ten rows were added in filename order with each entry's own `- topic:`
text byte-equal; the totals line and the counts footer moved 201 → **211** and
the footer vector 21/19/18/29/20/94 → **21/23/24/29/20/94**. Re-measured with
`python3 reports/round-28/readme/sweep.py`: ⟨rows N vs N files, 0 missing, 0
ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches, totals line 211,
footer 211 / 21/23/24/29/20/94, exit 0 — measured at close⟩. Non-canon examples
and passing structural gates do not certify historical truth.
```

⟨…⟩ slots: the ten filenames (from C01–C10 / P01) and the sweep reading measured
after the entries land. Do not write this block with a predicted reading — the
round-28 defect (`corpus/README.md:17-35`) was exactly a present-tense claim that
was never re-measured.

## 6. Limits

- The ten filenames and their `- topic:` bytes do not exist at authoring time;
  §3's rule + generator produce them mechanically once C01–C10 land. This seat
  cannot emit the ten row bytes now, and does not guess them.
- This draft does not decide: entry admission or quality (C13/C14/C17/R01–R03),
  the coverage receipt's before→after (C15/S01), or the cross-surface count census
  (`reports/round-35/review/R09-cross-review.md` owns "any counting command the
  integrator must update beyond corpus/README.md"). Live surfaces carrying the
  201 count today: `corpus/README.md:469,473` and `LOG.md` (parent-owned,
  append-only). Exactly one file in the tree carries a literal
  `^Total knowledge entries: ` line — `corpus/README.md:469`
  (`grep -rln '^Total knowledge entries: ' --include=*.md .`, 2026-10-19); the
  phrase also appears as quoted prose inside filed, read-only records
  (`corpus/lessons/round-{19,20,27,28}.md`, `reports/round-10/**`,
  `reports/round-27/**`, `reports/round-28/**`, `reports/supplement-opencode-1/**`)
  — those are dated readings, not count surfaces, and take no edit.
- Cross-fragment consistency (peers' drafts, same anchors): `cov/C15-receipt.md:96-107`
  (header/totals/footer before→after table), `cov/C16-scribe.md:162-165` (same
  four surfaces, plus the row-count command
  ``grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md``), `scribe/S01-c-receipt.md:130,351`
  (review of this draft, recorded **AGREE**), `scribe/S04-integration-draft.md:96,829`
  (integration order: rows drafted here, applied by the integrator),
  `cross/X02-conformance.md:177` (rows must be byte-equal to each entry's
  `- topic:`). No peer draft proposes a different count-line or row rule.
- `corpus/README.md` is not a filed round byte and is not in the frozen set, but
  this seat wrote none of it: every edit above is the integrator's to apply.
- Integration gate: `reports/round-35/review/R03-c-review.md` (the adversarial
  pass on this delta + the audit runbook) was absent at authoring. C's threshold
  ("README counts == live census") is a claim-level requirement, so the delta
  should be applied only after R03 lands and its findings are dispositioned;
  nothing in this draft depends on R03's bytes, only on its verdict.

## Owed

- `reports/round-35/plan/P01-c-plan.md` — the 10 entry topics + author
  assignments; absent at authoring (`reports/round-35/` held only `claims.json`,
  `targets.json`, `telemetry/*`). Without it the ten filenames are unknown.
- `reports/round-35/cov/C01-entry-1.md` … `reports/round-35/cov/C10-entry-10.md`
  — the entries whose `- topic:` bytes become the ten row texts; absent at
  authoring. The integrator runs §3's generator after these land.

## Citations

- `corpus/README.md:1-3,123,147-167,169-188,190,222,245,469,471-480,482-493` —
  pinned bytes, line map, revision convention (read at sha256
  `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`)
- `reports/round-28/readme/sweep.py:21,22,61,74-79,140,398-401` — row/topic
  equality contract and its continuation control; instrument sha256
  `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`
- `corpus/lessons/round-19.md:115` — "must re-measure, not arithmetic-guess …
  append a new dated block"
- `reports/round-28/readme/reconcile.md:1-70` — the round-28 reconciliation
  precedent (two-pin readings, instrument digest, writes list)
- Peer fragments cross-checked at authoring (same anchors, no conflict):
  `reports/round-35/cov/C15-receipt.md:96-107,138-141`,
  `reports/round-35/cov/C16-scribe.md:58,162-165`,
  `reports/round-35/scribe/S01-c-receipt.md:130,351` (review of this draft:
  **AGREE**), `reports/round-35/scribe/S04-integration-draft.md:96,614,686,829`,
  `reports/round-35/cross/X02-conformance.md:177,236`,
  `reports/round-35/scout/K02-entry-audit-method.md:188,206`
- Commands run (all from the repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, HEAD `4a7aede`):
  - `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21 19 18 29 20 94
  - `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 201`
  - `python3 -B reports/round-28/readme/sweep.py` → 201/201, all legs green, exit 0
  - `python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12 checks passed`
  - `python3 -B .scratch/c11/readme-delta.py` → no-op delta on the live tree
  - `python3 -B .scratch/c11/readme-delta.py --readme .scratch/c11/synth/readme/README.md --root .scratch/c11/synth/knowledge --json` → 10 rows, anchors per §3
  - `python3 -B .scratch/c11/readme-delta.py … --apply .scratch/c11/synth/readme/README.applied.md` → exit 0
  - `python3 -B .scratch/c11/sweep-synth.py --readme .scratch/c11/synth/readme/README.applied.md` → 211/211, exit 0
  - negative controls: `… --readme .scratch/c11/synth/readme/README.neg.md` → exit 1, `missing_from_index 1`; `README.neg2.md` → exit 1, `totals_ok False`
- Scratch (disposable, not evidence): `.scratch/c11/readme-delta.py` (source
  embedded in §3), `.scratch/c11/synth/**`, `.scratch/c11/sweep-synth.py`
