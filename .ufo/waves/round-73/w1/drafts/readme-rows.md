# corpus/README.md change draft — round 73 (claim C rows + Ca footer pair)

- **seat:** `ScribeReadmeIndex` (leaf, no dispatch). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **base revision:** `8841ad3b896a0227674fa0725b818c999118046f` (lane HEAD at read time).
- **`corpus/README.md` measured at base:** `sha256
  35e2cf6d07869ffd1bd3d6ec72c7385dc7f62ccbbb04f3fa859d1c164248687b`,
  763 lines, `revision: 2.21` at line 3.
- **the enforcing measurement:** `reports/round-28/readme/sweep.py`
  (`sha256 9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`);
  it owns the row shape (`^- \`<file>.md\` — <topic>`), the verbatim-topic rule,
  the `## <part>/ (N)` header rule, the `Total knowledge entries: N.` line and
  the `Counts checked …` footer block. `python3 3.14.8`; **no tool installed,
  no network fetch** (nothing to record under the UA clause).
- **status:** DRAFT ONLY. `corpus/README.md` was **not** edited (lane
  `git status --porcelain` shows it unmodified). Scratch and the two measured
  candidates live in `/tmp/ScribeReadmeIndex/`.

## 0. Verdict at a glance

| item | measured | status |
|---|---|---|
| two linguistics rows | derived by the sweep's own `topic_of()` from the staged entries; sim sweep `topic_mismatch 0` | **ready**, but the text is provisional on the landed entry bytes (§3.2) |
| footer `Total knowledge entries` | stated **243**, live **245** (`find`, inventory `totals.files`), sweep `FOOTER_TOTAL` | **correction line drafted** (§2.2) |
| footer directory totals | stated `30/29/36/29/24/95`, live `30/29/38/29/24/95` | **correction drafted** (§2.2) |
| post-landing count (+2) | 245 → **247**, `## linguistics/` 30 → **32** | **drafted** (§3.4) |
| known-gaps bullet | drafted in the round-64..67 shape | **ready** (§3.5) |
| README green after the assigned scope | **NO** — variant A sweep `ok false` (2 missing rows + culture-material header drift) | **finding F1/F2** (§6) |
| README green with the adjacent repair | **YES** — variant B sweep `ok true`, 247 rows vs 247 files | **needs a freeze decision** (§4, §6) |

## 1. Measurements (commands and outputs, run 2026-10-25)

```sh
find corpus/knowledge -type f -name '*.md' | wc -l          # 245
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
#   totals.files 245 ; per-dir (from .files[].path) civilizations 95,
#   culture-material 38, linguistics 30, myth-symbol 29, synthesis 29, verification 24
python3 -B reports/round-28/readme/sweep.py                  # exit 1
```

```
parts {"civilizations": 95, "culture-material": 38, "linguistics": 30, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 243 files 245
missing_from_index 2 ['culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md', 'culture-material/heritage-taxonomy-models.md']
topic_mismatch 0 []
orphan_rows 0 []
header_drift {'culture-material': {'declared': 36, 'files': 38}}
totals_line 243 totals_ok False
footer {"date": "2026-10-25", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 243, "dir_totals": [30, 29, 36, 29, 24, 95]}
footer_live {"total": 245, "dir_totals": [30, 29, 38, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [{"class": "FOOTER_TOTAL", "declared": 243, "live": 245, "date": "2026-10-25"}, {"class": "FOOTER_DIR_TOTALS", "declared": [30, 29, 36, 29, 24, 95], "live": [30, 29, 38, 29, 24, 95], "order": [...]}] footer_ok False
readme_sha256 35e2cf6d07869ffd1bd3d6ec72c7385dc7f62ccbbb04f3fa859d1c164248687b
```

**Cause of the 243 → 245 delta, measured not inferred:**

```sh
git -C . log --oneline -3 -- corpus/knowledge/culture-material/heritage-taxonomy-models.md \
                              corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md
# 3adbd4a round-72: SimplifierRows cuts …
# ba8ad3a round-72 C: canonical entry review cuts C1-C4 …
# 770100f round-72 C: heritage-taxonomy assimilation — two entries admitted, registry S874/S875 appended (797->799), lesson round-72
git -C . log --oneline -2 -- corpus/README.md
# 75d1675 round-71: post-filing hardening — accept-ca.py slice/id fixes, entry S873 cite, README footer date, …
# 498db73 round-71: claim C data lands — dance register entry + 13 mined rows S861-S873 + README reconcile
```

The round-72 landing (`770100f`) admitted two culture-material files and never
touched `corpus/README.md`; the README's last write is the round-71 commit.
So the footer's **stated 243 was true at round 71** and the round-72 landing
moved the tree by 2 without moving the file — the same class as the round-72
routed defect the claim Ca ledger carries, and the reason two index rows are
missing (`heritage-taxonomy-models.md` and its `.amend-2026-10-24-r13.md`).

**Gap sweep for the known-gaps bullet (re-measured here, 2026-10-25):**

```sh
find corpus/knowledge -iname '*conlang-scholarship*' | wc -l                       # 0
grep -rilE 'conlang scholarship|constructed[- ]language (scholarship|research)|conlang research' corpus/knowledge | wc -l   # 0
grep -cE 'ojs\.unito\.it|philol\.msu\.ru|journals\.rudn\.ru|cyberleninka\.ru/article/n/klassifikatsii|sanders\.phonologist\.org' corpus/SOURCES.md   # 0
grep -oE '^\s*\| S[0-9]+' corpus/SOURCES.md | tail -1                              # | S875
grep -cE '^\s*\| S[0-9]+' corpus/SOURCES.md                                        # 799
```

## 2. Block A — Ca: the footer correction (no claim-C path, no S-id ≥ S876)

Claim Ca permits in-place edits **only** to `SKILL.md` registry rows and the
README footer, plus an appended dated line. Both edits below are footer text.

### 2.1 In-place token edits (exact strings, each asserted unique)

| line at base | old (verbatim) | new (verbatim) |
|---|---|---|
| 732 | `Total knowledge entries: 243.` | `Total knowledge entries: 245.` |
| 736 | `(total 243 files; directory totals 30/29/36/29/24/95).` | `(total 245 files; directory totals 30/29/38/29/24/95).` |

The `Counts checked 2026-10-25` date and its command line stay unchanged (same
day, same command). The `30/…` linguistics figure stays 30 here — the +2
linguistics move belongs to claim C (§3.4), which is what keeps the Ca leg
`SEPARABLE`.

### 2.2 Appended dated correction line (paste after the `Revision 2.0 moved …` paragraph)

```
Corrected 2026-10-25 (round 73, appended correction — the earlier line is kept
as the dated record it was): the counts footer above read `Total knowledge
entries: 243.` and `(total 243 files; directory totals 30/29/36/29/24/95)`;
the live tree measures `Total knowledge entries: 245.` and `(total 245 files;
directory totals 30/29/38/29/24/95)`, and `## culture-material/` reads (36)
against 38 files. The delta is the round-72 heritage-taxonomy landing
(`heritage-taxonomy-models.md` + `heritage-taxonomy-models.amend-2026-10-24-r13.md`,
commit 770100f), which moved the tree and not this file. Re-derivation, from
the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l` → 245 and
`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
→ `totals.files 245`; `python3 reports/round-28/readme/sweep.py` names the same
delta as `FOOTER_TOTAL 243 vs 245`, `FOOTER_DIR_TOTALS`, `header_drift
{culture-material: declared 36, files 38}` and two `missing_from_index` rows.
```

Shape check against the Ca legs: pair id implied (`P-README-TOTALS`), **old
token** (`243`), **new token** (`245`), **re-derivation command** (`find` +
inventory + sweep) — the NOSTUB minimum, not a stub row naming only an id.

### 2.3 Ca ledger pair objects (drop-in for `reports/round-73/ledger.json`)

`observe_cmd` is an argv list run inside the materialized clone of `<lands>`;
`sweep.py` resolves its own lane root from its path, so in a clone it reads the
clone's README. `parse` is one capture group over the command's stdout.

```json
[
  {
    "id": "P-README-TOTALS",
    "stated_at": "corpus/README.md:732",
    "stated_text": "Total knowledge entries: 243.",
    "observe_cmd": ["python3", "-B", "reports/round-28/readme/sweep.py", "--json"],
    "parse": "\"totals_line\":\\s*(\\d+)",
    "observed_at_base": "243",
    "expected_after": "245",
    "disposition": "REPAIR",
    "why": "footer token vs live tree; delta is the round-72 heritage landing 770100f, which moved the tree and not the README"
  },
  {
    "id": "P-README-DIRTOTALS",
    "stated_at": "corpus/README.md:736",
    "stated_text": "(total 243 files; directory totals 30/29/36/29/24/95).",
    "observe_cmd": ["python3", "-B", "reports/round-28/readme/sweep.py", "--json"],
    "parse": "\"dir_totals\":\\s*\\[([^\\]]*)\\]",
    "observed_at_base": "30, 29, 36, 29, 24, 95",
    "expected_after": "30, 29, 38, 29, 24, 95",
    "disposition": "REPAIR",
    "why": "same landing; culture-material 36 -> 38. The second element must read 30 (not 32): the +2 linguistics move is claim C's, and a 32 here would break SEPARABLE"
  }
]
```

**A third pair is available but blocked — see F2.** `## culture-material/ (36)`
(`corpus/README.md:407`) is a live false statement (`header_drift`), and the two
missing rows are a live false statement of completeness, but neither is footer
text, so repairing them is forbidden by Ca's `APPENDONLY` leg as frozen:

```json
  {
    "id": "P-README-CMHEADER",
    "stated_at": "corpus/README.md:407",
    "stated_text": "## culture-material/ (36)",
    "observe_cmd": ["python3", "-B", "reports/round-28/readme/sweep.py", "--json"],
    "parse": "\"header_drift\":\\s*\\{\"culture-material\":\\s*\\{\"declared\":\\s*(\\d+)",
    "observed_at_base": "36",
    "expected_after": "38",
    "disposition": "REPAIR",
    "why": "BLOCKED by APPENDONLY as drafted ('in-place edits permitted only to SKILL.md registry rows and README footer'). Needs a freeze amendment or an ANNOTATE disposition; see F2"
  }
```

## 3. Block B — claim C: the README changes for the two linguistics files

### 3.1 Revision block (recommended addition — not one of the three named items)

Every prior landing added one, and `tools/check-readme-revisions.py` requires
unique, ascending labels (`2.21` → `2.22` is clean). Insert as the first
paragraph after the H1:

```
revision: 2.22 — Round-73 linguistics landing (2026-10-25): two linguistics
files landed (`conlang-scholarship.md`, constructed-language scholarship as a
research literature, and its dated amendment
`conlang-scholarship.amend-2026-10-23.md`, the method detail behind the
peer-reviewed conlang-pedagogy claim). Their rows are added in filename order
after `conlang-methodology.md`, with each entry's first `- topic:` text verbatim;
`## linguistics/` moved 30 → **32**; the totals and footer moved 245 → **247**;
registry moved from its 799 rows by the round-73 mined append, which continues
from S876 upward (the row set is fixed at claim freeze).
```

If Ca and C land in the same commit, one `2.22` block carries both moves and
the "moved 245 → 247" clause becomes "243 → **247**" with the heritage cause
named in the same paragraph.

### 3.2 The two rows (verbatim; insert in filename order after `conlang-methodology.md`, line 346)

```
- `conlang-scholarship.amend-2026-10-23.md` — the method detail behind the peer-reviewed conlang-pedagogy claim: a semester-long language-construction project at introductory level, in which phonological systems of natural *and* constructed languages were presented alongside instruction in language universals and typology, as a multi-part creative project.
- `conlang-scholarship.md` — constructed-language scholarship as a literature, in two languages: the peer-reviewed argument that conlang construction is a method that yields analysable linguistic data rather than decoration, and the Russian-language scholarly framing of imaginary languages, including the taxonomy of artificial languages and the vocabulary that separates вымышленные языки from auxiliary languages.
```

**These bytes are PROVISIONAL.** They were derived from the *staged* entries
(`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/…`),
not from the lane drafts `ScribeEntryBase` / `ScribeEntryAmend` are writing into
this same `drafts/` directory, which did not exist when this file was written.
The verbatim rule is mechanical, so the landing seat must **regenerate** the two
lines from the landed entries rather than paste these:

```sh
python3 -B - <<'PY'
import importlib.util
spec = importlib.util.spec_from_file_location('sweep', 'reports/round-28/readme/sweep.py')
sw = importlib.util.module_from_spec(spec); spec.loader.exec_module(sw)
for f in ['corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md',
          'corpus/knowledge/linguistics/conlang-scholarship.md']:
    print('- `%s` — %s' % (f.rsplit('/', 1)[1], sw.topic_of(f)))
PY
```

Row order: filename sort puts the `.amend-…` file **before** its base file
(`.a` < `.m`). The sweep does **not** check order (`orphan_rows` / `topic_mismatch`
only), so this is convention, not measurement — see F5.

### 3.3 Section header

`## linguistics/ (30)` → `## linguistics/ (32)` (line 344). Required: the sweep
fails on `header_drift` otherwise.

### 3.4 Post-landing footer move (+2) and its appended line

In-place, at landing: `Total knowledge entries: 245.` → `247.` and
`(total 245 files; directory totals 30/29/38/29/24/95).` →
`(total 247 files; directory totals 32/29/38/29/24/95).` (245/30 here assume
Block A landed first; if not, the old tokens are `243` and `30/29/36/…`).

Append, immediately after Block A's correction paragraph:

```
Landed 2026-10-25 (round 73, claim C): the two linguistics files indexed above
moved the tree by 2 — `Total knowledge entries:` 245 → 247, `## linguistics/`
30 → 32, directory totals `30/29/38/29/24/95` → `32/29/38/29/24/95`; re-derived
by the same two commands (`find corpus/knowledge -type f -name '*.md' | wc -l`
→ 247; `python3 tools/source-audit-inventory.py --json --summary --root
corpus/knowledge` → `totals.files 247`).
```

### 3.5 Known-gaps bullet (append after the round-65 bullet, before `Total knowledge entries:`)

Shape follows the round-64/66/67 bullets: round + path(s) + what the surface is
+ the registry rows + partial-scope neighbours.

```
- Round 73 adds `linguistics/conlang-scholarship.md` and its dated amendment
  `linguistics/conlang-scholarship.amend-2026-10-23.md` as a sourced
  linguistics register for constructed-language research as a literature (the
  round-73 registry append continues S876 upward; the row set is fixed at
  claim freeze). The surface had 0 filename owners and 0 topic-line owners
  before the landing; partial-scope neighbours remain
  `linguistics/conlang-methodology.md` (the craft pipeline, which had no
  research venue), `linguistics/naming-systems.md` (the naming half of
  construction), `linguistics/phonetics-phonology.md` (the sound-system
  side) and `synthesis/conlang-blueprint-template.md` (the build packet).
  The entries point to these without claiming a research literature for the
  lane's craft manuals.
```

The "0 owners" clause is my measurement (§1), not a quotation of the claim.
The registry-row count is deliberately **not** a number: the row set is fixed at
freeze and the tentative five (S876–S880) are a wave-1 hypothesis.

## 4. Block C — the adjacent repair neither claim as drafted permits

Without this block the README cannot go green (§5.2 vs §5.3). It is the
round-72 landing's debt, not claim C's:

```
- `heritage-taxonomy-models.amend-2026-10-24-r13.md` — what a state's own heritage-category list does over time, and how it should be cited, with dated captures as the durable carriers.
- `heritage-taxonomy-models.md` — the two states' official category models for material and intangible culture, read as design systems: the PRC's ten-门类 intangible-heritage taxonomy with its 罗马数字 category code, its batch/扩展项目 mechanism and dated batch growth; Japan's cultural-property 分野 domain tree with its 時代 period ladder, its 指定区分 designation facet, and record-level fields (材質・構造・技法 / サイズ / 所在地).
```

Insert in filename order between `headgear-head-covering-codes.md` and
`hunting-foraging-subsistence.md`; then `## culture-material/ (36)` → `(38)`.
Both strings were derived with the same `topic_of()` call and are verbatim
against the **committed** files (sim sweep: `topic_mismatch 0`).

## 5. Validation — measured on a simulated post-landing tree

`/tmp/ScribeReadmeIndex/knowledge` = copy of `corpus/knowledge` (245 files) plus
the two staged linguistics files = **247 files**; candidates built by
`/tmp/ScribeReadmeIndex/build_candidate.py`; measured by
`sweep.sweep(text, root_override=…)`.

### 5.1 Variant A = assigned scope only (Block A + Block B)

```
parts {"civilizations": 95, "culture-material": 38, "linguistics": 32, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 245 files 247
missing_from_index 2 ['culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md', 'culture-material/heritage-taxonomy-models.md']
topic_mismatch 0 []
orphan_rows 0 []
header_drift {'culture-material': {'declared': 36, 'files': 38}}
totals_line 247 totals_ok True
footer_findings [] footer_ok True
ok False        readme_sha256 728885afe4c6fd3ad79899af411954cba510ebccb4160acc014cb0945e381b1b
```

### 5.2 Variant B = A + Block C

```
rows 247 files 247
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 247 totals_ok True
footer_findings [] footer_ok True
ok True         readme_sha256 50b3395ef9c24b3e0199fc93ab9695a2b3b8430d2376e9fb11472362dc63e0fc
```

### 5.3 Controls on variant B (the green must be able to fail)

| control | perturbation | result |
|---|---|---|
| C0 | none | `ok True`, 0 mismatch |
| C1 | base row paraphrased ("conlang research as a literature…") | `ok False`, `REWRITE linguistics/conlang-scholarship.md` |
| C2 | amend row carrying the file's **second** `- topic:` | `ok False`, `REWRITE …conlang-scholarship.amend-2026-10-23.md` |
| C3 | amend row deleted | `ok False`, `missing_from_index` names it |
| C4 | totals line reverted to 245 | `ok False` (`totals_ok False`) |
| C5 | footer reverted to 245 / `30/29/38/…` | `ok False`, `FOOTER_TOTAL 245 vs 247` + `FOOTER_DIR_TOTALS` |

C2 is the empirical confirmation of the multi-topic rule: `TOPIC_RE` takes the
**first** `- topic:` of a file and stops at the next `- <word>` line, so the
amend row must carry its first topic only (see F4).

### 5.4 Other README controls on the candidate

```sh
python3 -B tools/check-readme-revisions.py --readme /tmp/ScribeReadmeIndex/README-B.md   # findings 0, exit 0
python3 -B tools/check-readme-heading.py    --readme /tmp/ScribeReadmeIndex/README-B.md   # findings 0, exit 0
```
`check-readme-revisions` also reports the **pre-existing** `REVISION-ORPHAN`
warning (base: lines 225/236; candidate: 235/246 — same paragraph, shifted by the
new block). Not introduced here.

### 5.5 Diffs

`/tmp/ScribeReadmeIndex/README-A.diff` (4 hunks) and `README-B.diff` (6 hunks).
Variant A's four hunks are: the revision block, `## linguistics/ (30)→(32)` with
the two rows, the known-gaps bullet + totals/footer tokens, and the two appended
dated paragraphs. Variant B adds exactly: `## culture-material/ (36)→(38)` and
the two heritage rows.

## 6. Findings for the integrator

- **F1 — the README is red at base on four finding classes** (`missing_from_index`
  2, `header_drift`, `totals_line`, `footer_findings` 2). Claim Ca names only the
  totals pair; the other three are unowned. If Ca's `REPAIR` leg is read as "the
  README is green", it cannot pass; read it as "the named tokens are green" and
  say so, or widen the pair set.
- **F2 — Ca `APPENDONLY` vs the header repair.** `## culture-material/ (36)` and
  the two missing rows cannot be repaired under "in-place edits permitted only to
  SKILL.md registry rows and README footer". Options, measured consequences:
  (a) amend the freeze to read "the README's count surface — the footer block and
  the six `## <part>/ (N)` headers" → variant B is legal and the sweep goes green;
  (b) keep it literal → the README keeps a false header and two missing rows
  through round 73 (the correction line names them, so the record is honest but
  the file stays red); (c) drop the header from the repair set and add an
  ANNOTATE row. Recommend (a), with Block C listed in the ledger.
- **F3 — claim C has no README leg.** None of C's ten legs mentions
  `corpus/README.md`, so a C landing can ship with no rows and nothing fails —
  which is exactly how round 72 produced F1. Either add a README leg to C before
  freeze or record the convention as a Ca pair; the sweep command above is the
  ready-made observe_cmd.
- **F4 — first multi-topic file in the lane.** `TOPIC_RE` takes the first
  `- topic:` only; the only other amend file at base has one topic, so the rule
  has never been exercised. The staged amend carries two topics (method detail;
  the three peer-reviewed positions), so a first-topic row **under-describes** the
  file. The sweep-faithful fix is in the entry, not the row: the landed
  `conlang-scholarship.amend-2026-10-23.md` should carry one merged `- topic:`
  covering both sections. If it keeps two, the row describes half the file and
  the row-level record says so.
- **F5 — row order.** Filename sort puts the `.amend-…` row first; the sweep
  does not check order, so any order passes. Convention (round-20 note: "rows
  ordered by filename") says filename order.
- **F6 — provisional row text.** If `ScribeEntryBase` / `ScribeEntryAmend` change
  the `- topic:` text, the two rows above are stale; regenerate (§3.2) and re-run
  the sweep. `REWRITE` is the failure signature.
- **F7 — landing order.** Block A must land before or with Block B, and Block B's
  tokens (245/30) assume A landed. One commit is simpler: one `2.22` revision
  line, one correction paragraph, tokens 243 → 247 and `30/29/36/…` → `32/29/38/…`,
  and the Ca `SEPARABLE` leg still holds if the Ca-added sentences cite no C path
  and no S-id ≥ S876 (they do not, as drafted).
- **F8 — re-measure at landing.** Every token here is a 2026-10-25 reading of the
  working tree; if another seat lands a file before the README commit, the
  numbers move and the correction line becomes a second false statement.

## 7. What this seat did not do

- Did not edit `corpus/README.md`, `reports/round-73/claims.json`, `SCORECARD.md`,
  `LOG.md`, `SKILL.md`, the registry, or any knowledge entry.
- Did not run the claim-C or claim-Ca counters (not yet drafted when this seat
  ran; `reports/round-73/accept-c.py` and `.ufo/waves/round-73/counters/` were
  absent). The sweep, `find`, the inventory, `check-readme-revisions` and
  `check-readme-heading` are the only measurements claimed here.
- Did not message any other seat; did not install any tool; made no network fetch.
- Wrote only `.ufo/waves/round-73/w1/drafts/readme-rows.md` (this file) and
  `.ufo/waves/round-73/w1/ScribeReadmeIndex.md`; scratch in
  `/tmp/ScribeReadmeIndex/` (`build_candidate.py`, `README-A.md`, `README-B.md`,
  `README-A.diff`, `README-B.diff`, `sweep-base.txt`, `rev-check.txt`,
  `head-check.txt`, `knowledge/` 247-file sim tree, 7.8 MB).
