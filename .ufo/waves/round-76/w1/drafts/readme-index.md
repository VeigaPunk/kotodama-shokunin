# Draft — round 76 `corpus/README.md`: culture-material index rows, heading, footer

Stage-only draft against lane base `98c486bdb4650ba5b8e651d332910e8ee60ad121`. **Not applied to the
lane** (the L1 installs it at the freeze). Seat: ScribeIndex.

Inputs read for this draft: round-76 `CLAIMS-DRAFT.md` (the four candidate paths and the declared
after-state), the four staged entries in the read-only package
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/`, and the
base `corpus/README.md` itself. Round-75's shape was read as
`git diff f556d104 4f5e3b25 -- corpus/README.md corpus/SOURCES.md`.

Order convention as observed at base: 38 of the 40 culture-material rows are in `LC_ALL=C` byte order of
the file name, which is why `heritage-taxonomy-models.amend-2026-10-24-r13.md` precedes
`heritage-taxonomy-models.md` (`-` sorts before `m` after the shared stem). The two exceptions are the
`worldbuilding-setting-practice*` rows, which round 74 appended at the end of the section instead of
inserting before `writing-media-surface-economy.md`; the base section therefore carries exactly **one**
inversion, `writing-media-surface-economy.md` > `worldbuilding-setting-practice.amend-2026-10-23.md`.
Round 75 inserted its two `heritage-taxonomy-models*` rows in byte order rather than appending, so both
precedents exist. This draft inserts in byte order — the dominant convention, and the one that keeps the
index usable as a lookup table — which puts the three `calendar-festival-systems.amend-*` rows before
`calendar-festival-systems.md` and `era-periodization-models.amend-2026-10-23b.md` before
`era-periodization-models.md` (`printf '%s\n' … | LC_ALL=C sort`, output in the round-76 seat report).
Appending all four rows at the end of the section instead would match the round-74 precedent and is the
one-line alternative if the L1 prefers it; the heading and footer arithmetic is identical either way.

**All four rows are CONDITIONAL.** The frozen claim declares `252 -> 252+n` with `n >= 2` counted over
these four candidate paths only, one row per admitted entry, and the Gate decides which entries land.
The heading and footer arithmetic below is parameterised on `n`; the row set for a given `n` is
whichever `n` of these four entries the Gate admits. Rows for entries that are rejected are removed at
install, not rewritten.

---

## 1. Index rows — `## culture-material/` section

### 1.1 Insert three rows immediately before the existing row `- \`calendar-festival-systems.md\``

```markdown
- `calendar-festival-systems.amend-2026-10-23c.md` — the standard's own clause text: the 编排规则 (1)–(5), the calculation model and its one-second precision, the representation methods (gan-zhi year naming, sequential month naming, the "闰" prefix for a leap month, sequential and gan-zhi day naming, and the date-label format), and the promulgation requirements — including that a published 农历 calendar must state its source and must carry a 农历/公历对照 with the twenty-four solar terms.
- `calendar-festival-systems.amend-2026-10-24-r10.md` — the authoritative copy's own statements about GB/T 33661-2017, and the mechanical reason its clause text cannot be reached by a plain client.
- `calendar-festival-systems.amend-2026-10-24.md` — what GB/T 33661-2017 actually requires, as the promulgation announcement and the official registry state it, and the era-name table the lane can now check at a citable address.
```

### 1.2 Insert one row immediately before the existing row `- \`era-periodization-models.md\``

```markdown
- `era-periodization-models.amend-2026-10-23b.md` — one institution's own dating vocabulary, as it is actually applied: the National Archives of Japan's detailed-search form carries an era-name table mapping 令和 (2019), 平成 (1989), 昭和 (1926), 大正 (1912), 明治 (1868), 慶応 (1865) … 文治 (1185) and onward to the earliest names, so that a catalogue search can be bounded by era.
```

### 1.3 Row text provenance (verbatim source of the `— <topic>` half)

| row | topic text source | conditionality |
|---|---|---|
| `calendar-festival-systems.amend-2026-10-23c.md` | that file's own `- topic:` field, line-wrapped continuation joined to one line | CONDITIONAL — its sole cited document (campaign S916, planned lane row S895) is a tier-C reproduction; the claim forbids a tier-C row as the sole support of an admitted entry |
| `calendar-festival-systems.amend-2026-10-24-r10.md` | same | CONDITIONAL — one cited document (campaign S938, planned S897) |
| `calendar-festival-systems.amend-2026-10-24.md` | same | CONDITIONAL — three cited documents (S937 -> S898, S935 + S908 -> S894, S932 -> S896) |
| `era-periodization-models.amend-2026-10-23b.md` | same | CONDITIONAL — one cited document (campaign S908, planned S894, shared with the row above as one document) |

The `- topic:` field was taken as the text between `- topic:` and the next `- key:` line, with the
continuation lines' indentation collapsed to a single space; no word was changed, added or reordered.

---

## 2. `## culture-material/` heading edit

Base line (one occurrence in the file):

```
## culture-material/ (40)
```

Replace with, by variant:

| n | replacement heading |
|---|---|
| 4 | `## culture-material/ (44)` |
| 3 | `## culture-material/ (43)` |
| 2 | `## culture-material/ (42)` |

Base 40 is the measured count at `98c486b`: `git ls-tree -r --name-only 98c486b corpus/knowledge/culture-material | grep -c '\.md$'` -> 40, and the base heading already reads `(40)` and the base index lists 40 rows.

---

## 3. Newest `Counts checked` footer

The base file ends with the round-75 block (three lines: `Total knowledge entries: 252.`, a blank line,
then the counts line). Earlier footers are kept byte-identical as the dated record; round 76 therefore
**appends a new block after it** rather than editing it. Both rounds ran on 2026-10-27, so the date is
the same and the totals are what distinguish the reading.

Variant n=4:

```markdown
Total knowledge entries: 256.

Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 256 files; directory totals 32/32/44/29/24/95).
```

Variant n=3:

```markdown
Total knowledge entries: 255.

Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 255 files; directory totals 32/32/43/29/24/95).
```

Variant n=2:

```markdown
Total knowledge entries: 254.

Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 254 files; directory totals 32/32/42/29/24/95).
```

Vector order is the README's own section order, not alphabetical: linguistics / myth-symbol /
culture-material / synthesis / verification / civilizations. Base derivation, one command per partition:

```
civilizations 95   culture-material 40   linguistics 32
myth-symbol 32     synthesis 29          verification 24   total 252
```

(`git ls-tree -r --name-only 98c486b corpus/knowledge/<partition> | grep -c '\.md$'` per partition;
sum 252 = the base total.)

Arithmetic check: 32+32+40+29+24+95 = 252; 32+32+44+29+24+95 = 256; 32+32+43+29+24+95 = 255;
32+32+42+29+24+95 = 254.

---

## 4. Pre-install checks the L1 can run once the entries land

```
# 1. the insert adds no NEW inversion: count adjacent inversions in the section
#    base (98c486b) = 1 (the round-74 worldbuilding append); after install must still be 1
git show <frozen>:corpus/README.md | sed -n '/^## culture-material\//,/^## synthesis\//p' \
  | grep -o '^- `[^`]*`' | sed 's/^- `//; s/`$//' \
  | LC_ALL=C awk 'NR>1 && $0<prev{c++} {prev=$0} END{print c+0}'

# 2. heading equals the row count in the section
git show <frozen>:corpus/README.md | sed -n '/^## culture-material\//,/^## synthesis\//p' \
  | grep -c '^- `'          # must equal the (N) in the heading

# 3. footer equals the tree
git ls-tree -r --name-only <frozen> corpus/knowledge | grep -c '\.md$'

# 4. every index row names a file that exists, and every culture-material file has a row
comm -3 <(git ls-tree -r --name-only <frozen> corpus/knowledge/culture-material | sed 's|.*/||' | LC_ALL=C sort) \
        <(git show <frozen>:corpus/README.md | sed -n '/^## culture-material\//,/^## synthesis\//p' \
          | grep -o '^- `[^`]*`' | sed 's/^- `//; s/`$//' | LC_ALL=C sort)   # empty = clean
```

Base values for the four checks, measured at `98c486b`: check 1 = 1 (the single pre-existing
worldbuilding inversion, which the insert must not increase); check 2 = 40 rows against heading `(40)`;
check 3 = 252; check 4 = empty (every culture-material file has an index row and every row names a file).
The round-75 myth-symbol section does not satisfy check 1 (its three `narrative-structure-frameworks*`
rows were appended after `trickster.md` rather than byte-sorted) — a pre-existing condition of the base,
**not** something this draft touches, recorded so the check is not mistaken for a regression caused by
the round-76 insert.

---

## 5. Standing notes

- Row text is the entry's own `- topic:` text; nothing in it is paraphrased, so it must be re-checked
  against the actually-installed entry file if the Gate edits an entry's topic text at install.
- No row is drafted for any entry the claim does not name; the five other staged culture-material files
  are handled elsewhere (four are already held by the lane, one is a duplicate target in the package's
  own merge report).
- If `n = 0` or `1` the claim fails as declared (kill rule: fewer than two candidate files landing);
  there is deliberately no heading/footer variant for it.
