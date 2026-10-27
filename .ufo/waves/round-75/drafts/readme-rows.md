# Draft — `corpus/README.md` changes for round 75

Seat: **ScribeReadmeIndex** (leaf, wave 1). Lane base: `f556d1049fe651d3d63975600b13acd9fb686f15`.
Status: **DRAFT. This seat edits no product byte.** Nothing below is applied; the L1 (or the
landing executor it names) applies it.

Read against, never edited: `reports/round-75/claims.json` (claim C legs `ENTRIES`, `INDEX`;
claim Ca legs `REPAIR`, `APPENDONLY`, `COMBINED`) and `reports/round-75/ledger.json`
(pairs `L75-02`, `L75-03` = the two heading repairs; `L75-04` = the sweep repair whose
`sweep-green-after.txt` receipt depends on this file being green).

**Landing precondition.** The landing tree that carries claim C's index rows must also carry
claim Ca's two heading repairs and Ca's four index rows (§2.1, §2.2, §2.3), because the footer
in §2.6 states them and because the repaired sweep only greens with all of them present. If
Ca and C land in separate commits, Ca's commit must come first (Ca is the calibration claim of
this round; every prior round landed it first).

---

## 0. Measured base state (read-only commands, run at `f556d10`, 2026-10-27)

```
$ for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
    printf "%s %s\n" "$d" "$(find corpus/knowledge/$d -type f -name '*.md' | wc -l)"; done
linguistics 32
myth-symbol 29
culture-material 40
synthesis 29
verification 24
civilizations 95
$ find corpus/knowledge -type f -name '*.md' | wc -l
249
```

```
$ python3 -B reports/round-28/readme/sweep.py --json | jq '{ok,total_files,total_rows,missing_from_index,orphan_rows,header_drift,footer_findings,totals_line}'
ok False                 total_files 249        total_rows 247
missing_from_index ["culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md",
                     "culture-material/heritage-taxonomy-models.md",
                     "linguistics/conlang-scholarship.amend-2026-10-23.md",
                     "linguistics/conlang-scholarship.md"]
orphan_rows ["civilizations/conlang-scholarship.amend-2026-10-23.md",
             "civilizations/conlang-scholarship.md"]
header_drift {"culture-material": {"declared": 36, "files": 40},
              "linguistics":     {"declared": 30, "files": 32}}
footer_findings [{"class":"FOOTER_TOTAL","date":"2026-10-25","declared":243,"live":249},
                 {"class":"FOOTER_DIR_TOTALS","declared":[30,29,36,29,24,95],
                  "live":[32,29,40,29,24,95]}]
totals_line 243
topic_mismatch []
```

Two facts this measurement pins and the draft is built on:

1. **The two `orphan_rows` are the round-73 block's row-shaped lines** (`corpus/README.md:787`
   and `:788`). `sweep.py`'s `SECTION_RE` only closes a partition at the next
   `## <part>/ (<n>)` heading, so every line after `## civilizations/ (95)` — including the
   round-73 and round-74 appended blocks — is read as part of the **civilizations** section.
   The round-74 block says so in its own words ("this block deliberately carries no
   row-shaped line, so no row is attributed outside a partition"), but the round-73 block did
   carry such lines. **Adding rows to the sections does not remove these two findings**
   (see §6.2: the closure is the sweep repair, not this README edit).
2. The headings `## linguistics/ (30)` (line 344), `## myth-symbol/ (29)` (line 376) and
   `## culture-material/ (36)` (line 407) are each byte-exactly one line, no trailing space.

---

## 1. Edit set (one commit, applied top-down)

| # | owner | at base line | change | graded by |
|---|-------|--------------|--------|-----------|
| E1 | Ca (`L75-02`) | 344 | `## linguistics/ (30)` → `## linguistics/ (32)` | accept-ca-75 `REPAIR` |
| E2 | Ca | 346 (after) | insert 2 rows, `linguistics/` | accept-ca-75 `REPAIR` (L75-04 sweep) |
| E3 | C | 376 | `## myth-symbol/ (29)` → `## myth-symbol/ (31)` — **conditional, §6.1** | accept-c's `INDEX` (recommended: add the heading to that leg pre-freeze) |
| E4 | C | 396 (after) | insert 2 rows, `myth-symbol/` | accept-c-75 `INDEX` |
| E5 | Ca (`L75-03`) | 407 | `## culture-material/ (36)` → `## culture-material/ (40)` | accept-ca-75 `REPAIR` |
| E6 | Ca | 428 (after) | insert 2 rows, `culture-material/` | accept-ca-75 `REPAIR` (L75-04 sweep) |
| E7 | C | after 822 (EOF) | append the round-75 landing block, footer total 249+N | accept-c-75 `INDEX` |

Rows are inserted **immediately after** the named anchor row and keep the section's
byte-alphabetical filename order (`…amend-….md` sorts before `….md`, as
`worldbuilding-setting-practice.amend-2026-10-23.md` (445) before
`worldbuilding-setting-practice.md` (446)). No blank line is inserted between rows.

---

## 2. Exact bytes

### 2.1 Ca — `## linguistics/` rows (insert after line 346, the `conlang-methodology.md` row)

```
- `conlang-scholarship.amend-2026-10-23.md` — the content behind the classification the base could only name — purpose-first typologies in Russian- and English-language scholarship, the a priori/a posteriori dichotomy argued down to a scale, and the design of one conlang-construction course as a companion article reports it.
- `conlang-scholarship.md` — constructed-language scholarship as a literature in two languages — an English-language argument that language construction teaches linguistic analysis, and a Russian-language monograph's taxonomy of artificial languages, its separation of вымышленные языки from auxiliary languages, its volume rule, and its account of which conlangs left their fictions
```

### 2.2 Ca — `## culture-material/` rows (insert after line 428, the `headgear-head-covering-codes.md` row)

```
- `heritage-taxonomy-models.amend-2026-10-24-r13.md` — what a state's own heritage-category list does over time, and how it should be cited, with dated captures as the durable carriers.
- `heritage-taxonomy-models.md` — the two states' official category models for material and intangible culture, read as design systems: the PRC's ten-门类 intangible-heritage taxonomy with its 罗马数字 category code, its batch/扩展项目 mechanism and dated batch growth; Japan's cultural-property 分野 domain tree with its 時代 period ladder, its 指定区分 designation facet, and record-level fields (材質・構造・技法 / サイズ / 所在地).
```

Both texts above are the entries' own `- topic:` blocks, continuation lines space-joined and
stripped exactly as `sweep.py:topic_of()` folds them, extracted from the **base** blobs of the
four files (`sha256` of each working-tree file equals `sha256` of the `f556d10` blob, checked
2026-10-27; those four files are untouched since round 74, so their topic text is stable at
`<lands>` unless another seat edits them — re-run §4.2 after landing).

### 2.3 C — `## myth-symbol/` rows (insert after line 396, the `myth-ritual-theories.md` row)

Row text is bound to the **landed** entry's own `- topic:` line; the strings below are the
candidate text from the staged shokuknow files and MUST be replaced by the landed topic if the
entry scribes changed it (the binding check in §4.2 is the authority, not this quote):

```
- `narrative-structure-frameworks.amend-2026-10-23.md` — how three articles of *Communications* 8 (1966) describe a narrative — Todorov's three categories and the temporal deformation that separates discourse from history, Greimas's message readable on two isotopies at once, and Barthes's hierarchy of levels with its horizontal and vertical readings — read in the French original from the page-level transcription.
- `narrative-structure-frameworks.md` — how narrative structure is theorised and specified as a build order for an invented culture — the structuralist premise that narrative is a formal object analysed by levels of description, carried by one Western row at the scope the Gate locates, beside the Chinese and Japanese half that is not a translation of that canon: the story/discourse split (故事 as deep structure, 话语 as surface presentation), the actantial model (行动元), the three time axes (次序, 时长, 频率), focalisation and the levels-and-voices problem (查特曼's participant grid), 起承転結 held as a completable minimal unit rather than a four-beat plot, a three-layer machine-writable description format (ストーリー, クエスト, シーン, with キャラクター as a hierarchical sub-layer), the Japanese narratology of narrative generation (物語生成の物語論), and 世界观 kept as tier-C practitioner vocabulary; decision tables and calibration statuses, never a ruling on any culture's story
```

Provenance of those two strings (both taken 2026-10-27 from the entry scribes' own drafts, which
are the documents that land; neither string is a paraphrase):

- **base entry** — the `- topic:` line of `.ufo/waves/round-75/drafts/narrative-structure-frameworks.md`
  (906 characters, one physical line, no backticks — so it is safe inside a `- \`name\` — ` row).
  **Revision note:** an earlier 892-char version of this topic said "carried by one Western row
  at notice scope"; the scribe superseded it on 2026-10-27 with "carried by one Western row at
  the scope the Gate locates" (the page-level text turned out locatable on S885, so a
  notice-scope claim would have asserted a narrower scope than the Gate may keep). The row
  above carries the 906-char version; the 892-char one must not be restored.
  That draft carries a **second** `- topic:` inside its Part 2 provenance block (the
  Chinese/Japanese half's own scope line, 275 chars); `TOPIC_RE`'s first-match rule stops at the
  next `- \w` line, so the second one never reaches the row and must not be substituted here.
  The staged shokuknow base text ("the Western framing claim that round 1's entry had to assert
  from memory … Round 2 adds …") is superseded and must not be shipped.
- **amendment** — the `- topic:` line of
  `.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23.md` (359
  characters, one physical line, no backticks; the file has exactly one `- topic:`). The staged
  shokuknow wording ("two primary articles from *Communications* 8 (1966) … opened page by page
  in this round") is superseded twice over: the draft covers three articles, and "opened page by
  page" overstates what was read (11 pages, not the full articles). The row above is the draft's
  own wording, confirmed by the entry's scribe.
- `ROWS-BOUND: PASS` (§4.2) is the gate for both strings: if a landing-time edit changes either
  `- topic:` line, the row is re-derived from the landed entry, never from this block. Both
  rows were re-bound byte-for-byte against those two draft files after inlining (0 mismatches),
  and again after the 906-char revision.

#### 2.3a Conditional third row — `.amend-2026-10-23b.md` (only if claim C's `entries` grows)

The amendment scribe also drafts `.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23b.md`
(the S/Z five-codes file, citing S885/S891/S892). It is **not** in claim C's frozen `entries`
list, so it gets no row and no footer increment. If the L1 adds it to `entries` before the
freeze, the row is (insert between the two rows above, i.e. filename order `.amend-2026-10-23.md`
< `.amend-2026-10-23b.md` < `.md`):

```
- `narrative-structure-frameworks.amend-2026-10-23b.md` — where Barthes's five codes come from — the 1966 article's own three levels and its four classes of the functional level, the five codes as an *S/Z* reading sheet names them, and a peer-reviewed account that states the relation as a partial reformulation rather than an identity.
```

with `N` = 3 (`Total knowledge entries: 252.`, vector `32/32/40/29/24/95`, myth-symbol heading
`(32)`), and §4.2's file list gaining that path.

If `N` (the frozen `entries` length) is 1 or 0, this block shrinks: N rows, myth-symbol
heading `29+N` (§6.1), footer total `249+N` and vector `32/(29+N)/40/29/24/95`.

### 2.4 Heading replacements (three single-line, whole-line replacements)

```
## linguistics/ (30)            ->  ## linguistics/ (32)
## myth-symbol/ (29)            ->  ## myth-symbol/ (31)     [§6.1: conditional]
## culture-material/ (36)       ->  ## culture-material/ (40)
```

`(32)` and `(40)` are `L75-02` / `L75-03`'s `expected_after` tokens; both observe commands
pin the base revision (`git diff <empty-tree> f556d10 -- 'corpus/knowledge/linguistics/*.md'`
→ `32 files changed`, and `…/culture-material/*.md` → `40 files changed`), so neither value
moves when claim C lands. `(31)` = base 29 + claim C's 2 entries, and is the only one of the
three that is *not* red at base (29 is true at base) — which is exactly why it cannot be a
Ca pair (§6.1).

### 2.5 Appended block (E7) — append after the current last byte (`…not verified facts.\n`)

Primary shape (variant A — matches the **existing** `FOOTER_RE` in
`reports/round-28/readme/sweep.py` byte-for-byte in its line structure, so a repair that reads
the *last regex match* needs no regex change):

```
## Round 75 landing (appended 2026-10-27, hyaku run 10)

Claim C adds two myth-symbol files (assimilation of the shokuknow `merge/kotodama`
narrative-structure-frameworks theme): `narrative-structure-frameworks.md` and
`narrative-structure-frameworks.amend-2026-10-23.md`. Their rows are in the
`## myth-symbol/` section above, each carrying its entry's own `- topic:` text verbatim
under the `` - `name.md` — `` prefix; this block deliberately carries no row-shaped line,
so no row is attributed outside a partition.

The same round repairs the index debt this file had been naming rather than closing: the
headings `## linguistics/` 30 -> 32 (claim Ca, pair L75-02) and `## culture-material/` 36 -> 40
(claim Ca, pair L75-03), and the four rows those two partitions carried unindexed since rounds
73-74 (`conlang-scholarship.md` and its `amend-2026-10-23`; `heritage-taxonomy-models.md` and
its `amend-2026-10-24-r13`), which are now inside their sections. The round-73 block's two
row-shaped lines stay exactly as filed; the round-75 repair to
`reports/round-28/readme/sweep.py` (pair L75-04) reads the last footer and ends a partition at
any level-2 heading, so no filed row is attributed to a partition it never belonged to.

Registry: claim C's ROWS leg appends the frozen row set; the count and the ids live in
`reports/round-75/claims.json`, not in this footer.

Total knowledge entries: 251.

Counts checked 2026-10-27 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 251 files; directory totals 32/31/40/29/24/95).
The three older footers above (the pre-round-73 reading, the round-73 landing reading and the
round-74 landing reading) are kept byte-identical as the dated record they were; this block is
the live reading, and it is the footer the repaired sweep reads. The inventory command
`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
counts markers, not verified facts.
```

Variant B (only if the sweep repair broadens `FOOTER_RE` to the round-74 one-line shape; then
the last *paragraph* must be one line and the three-line shape above would not match):

```
Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 251 files; directory totals 32/31/40/29/24/95).
```

§6.3 states which variant to pick and why A is the recommendation. Both carry identical
numbers, so nothing else in the draft changes between them.

With `N` entries adopted, substitute: `251` → `249+N` on the `Total knowledge entries:` line
and in `(total … files;`, and `32/31/40/29/24/95` → `32/(29+N)/40/29/24/95`.

---

## 3. Apply procedure (anchors, not line numbers)

Line numbers in §1/§2 are base-`f556d10` numbers and shift as rows are inserted. Apply by
anchor:

1. replace the whole line `## linguistics/ (30)` with `## linguistics/ (32)`;
2. insert the §2.1 two lines immediately after the single line that starts
   ``- `conlang-methodology.md` — ``;
3. replace the whole line `## myth-symbol/ (29)` with `## myth-symbol/ (31)` (§6.1) and the
   whole line `## culture-material/ (36)` with `## culture-material/ (40)`;
4. insert the §2.2 two lines immediately after the single line that starts
   ``- `headgear-head-covering-codes.md` — ``;
5. insert the §2.3 two lines immediately after the single line that starts
   ``- `myth-ritual-theories.md` — ``;
6. append §2.5 after the file's final newline, with one blank line between the old last line
   and the new `## Round 75 landing …` heading (the appended block itself starts at a `## `
   heading, matching the round-73 and round-74 blocks).

Each of the five anchor strings occurs exactly once in the file at base (checked).

---

## 4. Post-apply verification

### 4.1 Diff shape (the whole edit, and nothing else)

```
git diff -U0 f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/README.md
```

must show exactly: 3 paired `-`/`+` heading lines; 6 pure `+` row lines (three groups of two,
after the three named anchors); 1 pure `+` block at EOF (one blank separator line plus the
appended block). **No other changed line, and no `-` line outside the three headings** — that
is the operative reading of "older footers byte-identical" (and of claim Ca's
`changed lines elsewhere` clause, §6.1).

### 4.2 Row ↔ topic binding (the leg claim C's `INDEX` grades)

The rows must be the entries' own `- topic:` text, so re-derive them and diff:

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 -B - <<'PY'
import re
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
README = open("corpus/README.md", encoding="utf-8").read()
bad = 0
for f in [
    "corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md",
    "corpus/knowledge/linguistics/conlang-scholarship.md",
    "corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md",
    "corpus/knowledge/culture-material/heritage-taxonomy-models.md",
    "corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md",
    "corpus/knowledge/myth-symbol/narrative-structure-frameworks.md",
]:
    t = open(f, encoding="utf-8").read()
    m = TOPIC_RE.search(t)
    if not m:
        print("NO_TOPIC_FIELD", f); bad += 1; continue
    topic = " ".join(p for p in (ln.strip() for ln in m.group(1).strip("\n").splitlines()) if p)
    want = f"- `{f.rsplit('/', 1)[1]}` — {topic}"
    hits = sum(1 for ln in README.splitlines() if ln == want)
    print(("OK   " if hits else "MISS ") + f"  hits={hits}  {f}")
    bad += (hits == 0)
print("ROWS-BOUND:", "PASS" if bad == 0 else f"FAIL ({bad})")
PY
```

Expected: six `OK` lines, `ROWS-BOUND: PASS`. Note the duplicate exposure: `conlang-scholarship.md`
and `conlang-scholarship.amend-2026-10-23.md` each match **2** lines file-wide — their new
in-section row plus the round-73 block's row-shaped line (base lines 787-788, §6.4) — and both
of those pairs are word-for-word identical, because the block's rows were already the entries'
own `- topic:` text. The other four files match exactly one line each. `hits` is therefore
`>= 1` by design; the section-scoped (exactly-one) check is §4.6, not this script.

### 4.3 Index sweep (with the `L75-04` repair in the tree)

```bash
python3 -B reports/round-28/readme/sweep.py --json
```

Expected at the landing tree, after the `L75-04` repair: `ok: true` with
`missing_from_index: []`, `orphan_rows: []`, `topic_mismatch: []`, `header_drift: {}`,
`footer_findings: []`, `totals_line == total_files == 249+N`, and per-partition
`rows == files == declared`:
`linguistics 32, myth-symbol 29+N, culture-material 40, synthesis 29, verification 24,
civilizations 95`.

At base, with the *unrepaired* sweep, the residual reds after this edit but **without** the
`L75-04` repair are: `footer` (it reads the FIRST footer, §6.3), `totals_line: 243`,
`orphan_rows` (the two round-73 lines, §6.2) and `header_drift` empty. With the repair but
*without* the heading in E3, `header_drift` would carry `myth-symbol {declared: 29, files: 31}`
— that is the only reason E3 exists.

### 4.3.1 The four-variant matrix, measured (not asserted)

This draft was falsified before delivery by applying §3 to a copy of the base README, dropping
the two entry files into a **scratch copy** of `corpus/knowledge` (249 + 2 = 251 files; the
amendment stood in as the staged shokuknow file, whose `- topic:` the row in §2.3 was bound
to), and re-measuring with `reports/round-28/readme/sweep.py`'s own `disk_files` /
`topic_of` / regexes under two switches: `boundary` (a partition ends at any `^## ` heading)
and `lastfooter` (the last `FOOTER_RE` and `TOTALS_RE` match instead of the first).

| variant | missing | ghosts | mismatch | drift | footer | totals | ok |
|---|---|---|---|---|---|---|---|
| base README, unrepaired instrument | 6 | 2 | 0 | `culture-material 36/40, linguistics 30/32, myth-symbol 29/31` | `FOOTER_TOTAL 243!=251`, `FOOTER_DIR [30,29,36,29,24,95]` | 243 | **False** |
| **§2/§3 applied**, unrepaired instrument | 0 | 2 | 0 | `{}` | `FOOTER_TOTAL 243!=251`, `FOOTER_DIR …` | 243 | **False** |
| applied, `lastfooter` only (no boundary) | 0 | 2 | 0 | `{}` | `[]` | 251 | **False** |
| applied, `boundary` only (no lastfooter) | 0 | 0 | 0 | `{}` | `FOOTER_TOTAL 243!=251`, `FOOTER_DIR …` | 243 | **False** |
| **applied, both switches** | 0 | 0 | 0 | `{}` | `[]` | 251 | **True** |
| applied, both switches, **E3 dropped** | 0 | 0 | 0 | `myth-symbol {declared: 29, files: 31}` | `[]` | 251 | **False** |

Per-partition reading in the green row: `linguistics 32, myth-symbol 31,
culture-material 40, synthesis 29, verification 24, civilizations 95`; `rows == files` in all
six (251 rows, 251 files — no stray row-shaped line anywhere in the patched file);
`totals_line 251 == total_files 251`; footer vector `[32, 31, 40, 29, 24, 95]`. Two
consequences worth stating because they are the parts a reader will doubt: (a) the two
round-73 ghost rows disappear **only** with the `boundary` switch, confirming §6.2; (b) the
heading E3 is load-bearing for `drift` and for nothing else.


### 4.4 Heading controls (siblings, both read-only over README)

```bash
python3 -B tools/check-readme-heading.py   # exit 0: one H1, no duplicate heading text
python3 -B tools/check-readme-revisions.py # exit 0: labels unique, no stub, non-increasing
```

`## Round 75 landing (appended 2026-10-27, hyaku run 10)` is a new, unique H2 text and the
block adds no `revision:` line, so neither control moves.

Measured on the patched copy of the base README (scratch, 2026-10-27):

```
$ python3 -B tools/check-readme-heading.py --readme <patched>
findings 0            headings {"1": 1, "2": 10}    h1_lines [1]     exit 0
$ python3 -B tools/check-readme-revisions.py --readme <patched>
findings 0            warnings 1 (REVISION-ORPHAN lines=[225, 236])   exit 0
```

Base for comparison: `headings {"1": 1, "2": 9}` (so the appended block adds exactly one H2),
and the same single `REVISION-ORPHAN` warning at the same lines — the new block introduces no
warning of its own.


### 4.5 Footer arithmetic (independent of the instrument)

```bash
find corpus/knowledge -type f -name '*.md' | wc -l
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  printf "%s " "$(find corpus/knowledge/$d -type f -name '*.md' | wc -l)"; done; echo
```

must print `251` and `32 31 40 29 24 95` for N=2, matching §2.5's two numbers.

### 4.6 Re-runnable index self-check (the §4.3.1 green row, on the landing tree)

Run at the landing tree; it reads only, and it must print `INDEX-SELFCHECK: PASS`. It is the
§4.3.1 matrix's last row expressed as one command, so the L1 does not need to reconstruct the
simulation:

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 -B - <<'PY'
import importlib.util, os, re, sys
spec = importlib.util.spec_from_file_location("sweep", "reports/round-28/readme/sweep.py")
sw = importlib.util.module_from_spec(spec); spec.loader.exec_module(sw)
text = open("corpus/README.md", encoding="utf-8").read()
root = os.path.join(os.getcwd(), "corpus", "knowledge")
marks = []
for m in re.finditer(r"^## (.*)$", text, re.M):          # a partition ends at ANY h2
    mm = sw.SECTION_RE.match(m.group(0))
    marks.append((m.start(), mm.group(1) if mm else None, int(mm.group(2)) if mm else None))
parts, missing, ghosts, mism, drift = {}, [], [], [], {}
for i, (pos, part, decl) in enumerate(marks):
    if part is None:
        continue
    end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
    rows = [(m.group(1), m.group(2)) for m in sw.ROW_RE.finditer(text[pos:end])]
    files = sw.disk_files(root, part); seen = {f for f, _ in rows}
    missing += [f"{part}/{f}" for f in sorted(set(files) - seen)]
    ghosts += [f"{part}/{f}" for f in sorted(seen - set(files))]
    for f, tp in rows:
        if f in set(files) and sw.topic_of(os.path.join(root, part, f)) != tp:
            mism.append(f"{part}/{f}")
    if decl != len(files):
        drift[part] = {"declared": decl, "files": len(files)}
    parts[part] = len(files)
total = sum(parts.values())
foot = list(sw.FOOTER_RE.finditer(text))[-1]
tot = int(list(sw.TOTALS_RE.finditer(text))[-1].group(1))
vec = [int(x) for x in foot.group(4).split("/")]
live = [parts[p] for p in sw.PARTS if p in parts]
ok = (not (missing or ghosts or mism or drift) and int(foot.group(3)) == total
      and vec == live and tot == total)
print("parts", parts, "total", total)
print("missing", missing, "ghosts", ghosts, "mismatch", mism, "drift", drift)
print("footer", foot.group(1), int(foot.group(3)), vec, "totals", tot)
print("INDEX-SELFCHECK:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
PY
```

It grades exactly the `INDEX` leg's wording (one row per entry in its partition, topic text
equal, last footer total and vector equal to the live tree) plus the drift the sweep grades —
and nothing else. It is **not** `accept-c.py`; it is the cheap pre-commit instrument.

Both directions were measured on 2026-10-27, with the code block above extracted from this
file and executed verbatim (so what ships is what ran). Four runs, each in its own scratch
copy of a pseudo-lane (`corpus/README.md` + `corpus/knowledge` + a copy of `sweep.py`):

| run | tree | result | exit |
|---|---|---|---|
| green | patched README over the 251-file tree (both entry drafts in `myth-symbol/`) | `INDEX-SELFCHECK: PASS` | 0 |
| do-nothing control | `f556d10` README over the 249-file base tree | `FAIL`; `missing` = the four files, `drift` = `linguistics 30/32, culture-material 36/40`, `footer 2026-10-25 243 [30,29,36,29,24,95]`, `totals 249` | 1 |
| topic mutant | green tree, one row's text changed (`how three articles` → `how four articles`) | `FAIL`; `mismatch ['myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md']` — the topic-equality clause bites | 1 |
| ghost mutant | green tree plus a row naming `narrative-structure-frameworks-ghost.md` | `FAIL`; `ghosts ['myth-symbol/narrative-structure-frameworks-ghost.md']` — the ghost-row clause bites | 1 |




---

## 5. Byte identity of the parts this edit must not touch

Everything from the file's first byte up to the last byte of the round-74 block
(`…counts markers, not verified facts.\n`, base line 822) is preserved byte-for-byte except
the three heading lines of E1/E3/E5 and the six inserted row lines of E2/E4/E6. In
particular the four `Counts checked` readings already in the file (base lines 749-753,
the round-20 one that the unrepaired sweep parses) and the round-73/round-74 footers are
untouched — they are the dated record, and `claim C`'s `INDEX` leg's "older footers are
byte-identical" is satisfied by construction (only EOF append).

---

## 6. Open decisions for the L1 (each is a rule choice, not a drafting choice)

### 6.1 E3 (myth-symbol heading) collides with claim Ca's `APPENDONLY` clause

`claim Ca`'s `APPENDONLY` leg reads: "changed lines elsewhere are a subset of the stated_at
lines of REPAIR pairs plus appended lines". Under the operative reading of §4.1 (a *changed*
line = a removed-and-readded line), `## myth-symbol/ (29) → (31)` is a changed line at
`corpus/README.md:376` that is **not** the `stated_at` of any REPAIR pair, so at the combined
tree (`claim Ca`'s `COMBINED` leg materializes both landings and runs all 12 legs)
`APPENDONLY` would go red.

It cannot become a Ca pair: `L75-02`/`L75-03` are legitimate because 30≠32 and 36≠40 at base,
but `## myth-symbol/ (29)` is **true at base**, so a pair naming it is not red at base and
`ExecLedger` drops it by rule. The choice is the L1's, pre-freeze:

- **Option 1 (recommended, keeps the file true).** Keep E3 and extend claim Ca's `APPENDONLY`
  clause, pre-freeze, by exactly one class: "plus the partition-count heading of a partition
  claim C's own entries move, and claim C's index rows, at `corpus/README.md`". This is the
  same shape as the round-74 R1 exemption and is red-free at base. Cost: one clause in
  `claims.json` (the file is DRAFT, `pre_data_corrections` is the field for it).
- **Option 2 (no rule change).** Drop E3, ship the heading stale at `(29)`, and name it as
  stale in the §2.5 block (the round-73/74 house pattern). Cost: a fresh instance of the exact
  defect class `L75-02`/`L75-03` repair, `header_drift` red at the landing tree, and a
  `sweep-green-after` receipt that cannot be reproduced at the combined tree.
- **Option 3.** Have claim C's `INDEX` leg state the heading equality explicitly (six headings
  = six live partition counts) instead of relying on the sweep; E3 then lands as a graded leg
  rather than an ungraded byte. This is compatible with Option 1 and costs nothing extra.

I recommend 1 + 3. Without either, a reviewer is entitled to call the round's own heading
repair vacuous — it repairs two of the three stale headings it measured.

### 6.2 The two `orphan_rows` are closed by the sweep repair, not by this edit

`corpus/README.md:787-788` (round-73 block) are row-shaped and therefore read as
`civilizations/` ghosts under `SECTION_RE`. Adding the four in-section rows does not remove
them, so `sweep-green-after.txt` (pair `L75-04`) requires the repaired sweep to **end a
partition at any level-2 heading** (`^## `), not only at `^## <part>/ (<n>)$`. That is also
what the round-74 block already asserts in prose ("no row is attributed outside a
partition"). The alternative — de-shaping lines 787-788 — is a *changed line* in an older
block, unreachable by any REPAIR pair (the lines are true as filed), so it would break
`APPENDONLY` exactly as `E3` would (hence: one exemption, or none).

Consequence for claim C's `INDEX` leg if the instrument is **not** repaired this way: the two
in-section rows are still correct and still "exactly one index row per adopted entry in the
`myth-symbol/` section"; only Ca's sweep receipt is unreachable. State that in Ca's
`do_nothing_control`/`why`, not in C's leg.

### 6.3 Footer shape (variant A vs B) follows the sweep repair

- The current `FOOTER_RE` needs `Counts checked <date> from the repo root:` \n `` `cmd` `` \n
  `(total N files; directory totals a/b/c/d/e/f).` on three lines. Two footers in the file
  match it: the round-20 reading (`total 243`, base lines 751-753) and — after this edit — the
  new one. The round-73 and round-74 footers are single-line and match **nothing**.
- A repair that reads "the last **match**" therefore reads **variant A**. A repair that
  broadens the regex to the round-74 one-line shape reads **variant B**. A is the smaller
  change to a filed instrument and the reason it is primary.
- Either way the `Total knowledge entries:` read must also take the **last** match (base's
  only match is `243` at line 813's predecessor, base line 745), or `totals_line` stays red
  whatever the footer says. This is one more line of `L75-04`; it is not a README change.

### 6.4 Duplicate rows, named rather than hidden

After E2 the file carries two rows for each `conlang-scholarship` file (one in
`## linguistics/`, one in the round-73 block at 787-788). `sweep.py`'s duplicate leg is
per-section and not part of its `ok`, so nothing grades it, but a reviewer will see it. Both
readings of the file (in-section row + filed block row) are honest: the block is a dated
landing record that says the row belongs in the section "and a later reconcile may merge them
into the section". This edit is the reconcile; the block's bytes stay. If the L1 wants a
single row file-wide, that requires de-shaping 787-788 and then §6.2's `APPENDONLY` exemption
covers it too.

### 6.5 The critic's `INDEX` ghost-row repair is already satisfied by these bytes

`CritCCounterVacuity.md` (§ "Ranked predicate repairs", item 8) asks the `INDEX` leg to add: "every
README index row in the myth-symbol section names an existing `.md` file under
`corpus/knowledge` at `<lands>`, and each adopted entry has exactly one such row whose topic
equals its own `- topic:` value." The draft is built to that wording, not only to the filed one:

- both §2.3 rows name files claim C lands (they exist at `<lands>` by construction; at base
  they do not, which is the point);
- exactly one row per adopted entry **inside** `## myth-symbol/` — the round-73 precedent of
  duplicate row-shaped lines outside a partition does not repeat here (§2.5's block carries
  none);
- topic equality is measured, not assumed (§4.2, §4.6 — the latter reports `mismatch` and
  `ghosts` per partition, i.e. exactly this repair's two clauses).

So the strengthened wording costs claim C nothing in this file; it is the L1's call whether to
add it to `claims.json` before the freeze.

---

## 7. Provenance and limits

- Every measurement above was taken read-only at `f556d10` in
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin` on 2026-10-27; `git diff --name-only` was
  empty before the draft was written (the four topic sources are the base blobs, sha256
  matched against `git show f556d10:<path>`).
- The §2.3 row text is final **as drafted** and bound to the entry scribes' own drafts
  (`.ufo/waves/round-75/drafts/narrative-structure-frameworks{,.amend-2026-10-23}.md`), re-bound
  byte-for-byte after inlining (6 rows, 0 mismatches). If either entry's `- topic:` line changes
  before landing, the row must be re-derived from the entry (§4.2/§4.6), not from this file.
- `N` is the frozen `entries` length of claim C. `claims.json` is DRAFT and currently lists 2;
  if the freeze adopts 1 or 0, §2.3/§2.5 substitute per §2.5's note and E3 becomes `(30)`.
- No receipt is claimed here: this is a draft for the L1's landing, and no counter in
  `reports/round-75/` (`accept-c.py`, `accept-ca.py`) existed when it was written — §4 states
  the expected readings of the *existing* instrument (`reports/round-28/readme/sweep.py`) and
  of the two heading controls, and the expected leg names from the draft claims file only.
- Out of scope, deliberately: `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, the registry
  (`corpus/SOURCES.md`), the entries themselves, `reports/round-75/*` config, and
  `reports/round-28/readme/sweep.py` (the `L75-04` repair is ExecSweepFix's).
