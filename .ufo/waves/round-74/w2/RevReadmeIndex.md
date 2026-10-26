# RevReadmeIndex — round 74 w2 (falsify) — `corpus/README.md` change

Seat: `RevReadmeIndex`. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Read-only role: the only file written by this seat is this report. No tool installed, no
network fetch performed (all evidence is repo-local), no `pacman`, no background jobs, no
subagents, no writes anywhere under the fleet root, sibling lanes, `.ufo/state`,
`MANIFEST.json`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `corpus/**`, `reports/**`, or
`/home/vgpnk/Projects/shokuknow` (shokuknow was read only, no campaign tool run there).

Revisions measured (all reads by absolute path or `git -C` from the lane):

| item | value |
|---|---|
| base | `f7104cbce186bc2e1522abf0cfd619cc834628bb` |
| operative freeze F3 | `00c408a0af2fa5ddf65af2224152ce258b26d896` |
| claim C lands | `c4bf61a8d722f9168ce0fd8021a6261c000610c5` |
| lane `main` / `HEAD` at measurement | `1d7add3f7b9eaf6f3349c56c36f6d06325d74236` |
| README commits base..main | one: `d7a3840` (claim C landing) |

`git diff --stat c4bf61a8 main -- corpus/README.md` is empty: the bytes measured at `main`
are the graded bytes at claim C's lands. Nothing else in the round touched the file
(`git log --oneline f7104cb..main -- corpus/README.md` → `d7a3840` only).

Tooling notes required by the seat contract:
- **No `lsp` device is mounted in this seat** (inventory: read, bash, edit, eval, glob,
  grep, task, wait, web_search, write, yield). Caller/definition/diagnostics checks were
  therefore not available; every structural check below is a recorded shell/python
  measurement and is presented as literal text evidence, never as semantic proof.
- **No fetch**: the attack is entirely derivable from the lane's committed bytes; no
  User-Agent applies because no request was made. No "no capture" ruling is asserted.

---

## 0. Verdict in one line

The four invariants named in the ticket (two verbatim rows; zero edited bytes; footer
totals 249 and 32/29/40/29/24/95; the Known-gaps "0 owners / five partial-owner paths"
claims) **hold as defined**, and the appended block's self-descriptions are byte-accurate —
but the same Known-gaps bullet's additional *venue* clause is false under the theme's own
source set (F1), the insertion breaks the file's own filename-order invariant (F2), its
owner list is incomplete (F3), and the sweep-redness sentence tells only part of the story
(F4). No `sweep.py` red leg is new from round 74.

---

## 1. Attacks that FAILED (the claim survived) — with raw evidence

### A1. "Two index rows must equal the entries' own `- topic:` text verbatim" — SURVIVED

Command (python, exact codepoint equality after stripping only the fixed
`` - `name.md` — `` prefix):

```
$ python3 - <<'EOF'
import re
readme=open('corpus/README.md',encoding='utf-8').read().splitlines()
rows={}
for i,l in enumerate(readme,1):
    m=re.match(r"^- `(worldbuilding-setting-practice[^`]*\.md)` — (.*)$", l)
    if m: rows[m.group(1)]=(i,m.group(2))
for name,(ln,txt) in rows.items():
    p=f"corpus/knowledge/culture-material/{name}"
    t=[x for x in open(p,encoding='utf-8').read().splitlines() if x.startswith('- topic: ')]
    topic=t[0][len('- topic: '):]
    print(name,"line",ln,"len_row",len(txt),"len_topic",len(topic),"EQUAL",txt==topic)
EOF
worldbuilding-setting-practice.amend-2026-10-23.md line 445 len_row 284 len_topic 284 EQUAL True
worldbuilding-setting-practice.md line 446 len_row 445 len_topic 445 EQUAL True
```

Independent cross-check with the round-28 instrument: `topic_mismatch 0` over all 247 rows
at `main` (§3), i.e. no row in the file is a paraphrase, the two new ones included. The
sweep's own planted-paraphrase control passes (`PASS control: planted paraphrase flagged`).

### A2. "No existing byte edited (diff has no `-` lines)" — SURVIVED

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --numstat \
    f7104cbce186bc2e1522abf0cfd619cc834628bb main -- corpus/README.md
45	0	corpus/README.md
$ git diff f7104cb..main -- corpus/README.md | grep -c '^-[^-]'
0
```

45 insertions, 0 deletions. Because the change is a pure insertion, every base byte is
preserved — including both older footers (lines 749-780 region and 792-794), which
therefore *are* byte-identical to base.

### A3. "Appended footer totals 249; per-directory 32/29/40/29/24/95 equal `find` per partition at main" — SURVIVED

```
$ find corpus/knowledge -type f -name '*.md' | wc -l
249
$ for d in corpus/knowledge/*/; do printf '%s %s\n' \
    "$(find "$d" -maxdepth 1 -type f -name '*.md' | wc -l)" "$d"; done
95 corpus/knowledge/civilizations/
40 corpus/knowledge/culture-material/
32 corpus/knowledge/linguistics/
29 corpus/knowledge/myth-symbol/
29 corpus/knowledge/synthesis/
24 corpus/knowledge/verification/
```

README section order is `linguistics, myth-symbol, culture-material, synthesis,
verification, civilizations` (`## linguistics/` L344, `## myth-symbol/` L376,
`## culture-material/` L407, `## synthesis/` L447, `## verification/` L479,
`## civilizations/` L505). Mapping that order onto the measured counts gives
32/29/40/29/24/95 — the appended vector at L815 exactly. There are no nested
directories (`find corpus/knowledge -mindepth 2 -type d | wc -l` → 0) and no non-`.md`
files (`find corpus/knowledge -type f ! -name '*.md' | wc -l` → 0), so a recursive `find`
and a per-partition `find` cannot diverge. The footer's own command reproduces 249.

### A4. "At the pinned base `f7104cb` the theme had 0 filename owners" — SURVIVED

```
$ git ls-tree -r --name-only f7104cbce186bc2e1522abf0cfd619cc834628bb corpus/knowledge \
    | grep -i 'worldbuilding\|setting-practice'   # (no output, exit 1)
$ git ls-tree -r --name-only f7104cbce186bc2e1522abf0cfd619cc834628bb corpus/knowledge \
    | grep -ciE 'setting'
0
$ git grep -lE '設定ノート|世界観|世界观' f7104cb -- corpus/knowledge | wc -l
0
```

The broader reading (any filename carrying `setting`) is also 0, so the claim is not
narrower than its phrasing.

### A5. "Five partial one-way owner paths exist" — SURVIVED

```
$ for f in corpus/knowledge/synthesis/coupling-model.md \
           corpus/knowledge/synthesis/consistency-verification-checklist.md \
           corpus/knowledge/synthesis/worldbible-integration-contract.md \
           corpus/knowledge/culture-material/cartography-and-mapmaking.md \
           corpus/knowledge/linguistics/naming-systems.md; do
    printf '%-70s ' "$f"
    git cat-file -e main:$f && echo exists
    git diff --quiet f7104cbce186bc2e1522abf0cfd619cc834628bb main -- "$f" \
      && echo "  UNCHANGED base..main"
  done
corpus/knowledge/synthesis/coupling-model.md                           exists  UNCHANGED base..main
corpus/knowledge/synthesis/consistency-verification-checklist.md       exists  UNCHANGED base..main
corpus/knowledge/synthesis/worldbible-integration-contract.md           exists  UNCHANGED base..main
corpus/knowledge/culture-material/cartography-and-mapmaking.md         exists  UNCHANGED base..main
corpus/knowledge/linguistics/naming-systems.md                         exists  UNCHANGED base..main
```

All five also exist at base (`git cat-file -e f7104cb:<path>` → present), so "remain" is
true. Byte-unchanged in the round means they cannot cite the new entries: the citation is
one-way, as stated.

### A6. "The entries cite them without restating them" — SURVIVED (mechanical lower bound)

All five are named in the main entry's `- couples:` line (L12) with per-file glosses; the
amendment's `- couples:` line (L12) names `synthesis/worldbible-integration-contract.md`.
An 8-token verbatim n-gram comparison between each new entry and each of the five files
returns **0 shared 8-grams** in all ten pairs (`python3` set intersection, no output),
i.e. no copied run of text; "without restating them" is supported at least at the
copy level (semantic paraphrase is not machine-checkable and is not claimed).

### A7. "Two culture-material files remain unindexed and are named" — SURVIVED

```
$ sed -n '407,446p' corpus/README.md | grep -c '^- `'
38
$ comm -13 <section rows sorted> <ls culture-material sorted>
heritage-taxonomy-models.amend-2026-10-24-r13.md
heritage-taxonomy-models.md
```

Exactly the two files the block names; no other file in the partition is unindexed, and no
section row lacks a file (`comm -23` empty). The block's "the live directory holds 40 files
and the section 38 rows" is exact (40 = 38 + 2).

### A8. "This block deliberately carries no row-shaped line" — SURVIVED

```
block lines 27
row-shaped lines in block: []
```

Regex `^- \`[^\`]+\.md\` — ` applied to L796-822 (the whole appended block): zero matches.
Consequence as claimed: the sweep's ghost/missing legs are unchanged by this block.

### A9. Block's remaining numbers — SURVIVED

- `Registry: 804 -> 808`: the claim's own regex
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` gives **804** at base and
  **808** at main. `git diff --numstat base..main -- corpus/SOURCES.md` → `5 1`, the one
  deleted line being S877's in-place row rewrite (used-by cell) and the five additions
  being S877 (new cell) + S881..S884; exactly four new rows.
- `used-by exactly the two files above`: S881 and S882 → `...worldbuilding-setting-practice.md`;
  S883 and S884 → `...worldbuilding-setting-practice.amend-2026-10-23.md`; no other path in
  any of the four cells. (S877 additionally names the base entry after its in-place change —
  see residual risk R2.)
- `by the round-74 document map`: `.ufo/waves/round-74/assimilation/id-renumber-map.json`
  assignments are staged S883→S881, S884→S882, S899→S883, S900→S884, reused S882→S877, each
  with `new_id_present_in_reg_ids: false` — consistent.
- `census receipts under reports/round-74/telemetry/`: both receipts are committed
  (`census-start.txt` 804-state, `census-end.txt` with `exit=0`). The end receipt's `W01`
  lines list only S881/S882/S884 (three, not four) — that is **not** a defect: `W01` is
  "tier-C mined with non-`—` used-by", and S883 is tier **B**, so its absence is correct.

### A10. Stale headings — the two that drift are both named somewhere in the file

Measured declared-vs-files for all six sections: `linguistics 30/32` and
`culture-material 36/40` drift; `myth-symbol 29/29`, `synthesis 29/29`,
`verification 24/24`, `civilizations 95/95` do not. The round-74 block names the
`## culture-material/ (36)` heading stale (L805-806) with both live numbers (40 files,
38 rows); the `## linguistics/ (30)` heading is named stale in the round-73 block
(L785) and by the round-73 footer. No unflagged *partition* heading remains stale.

---

## 2. Findings

### F1 — MEDIUM — "0 registry rows naming the theme's venues" is false under the theme's own source set

The Known-gaps bullet (README L740-742) says:

```
   `f7104cb` the theme had 0 filename owners and 0 registry rows naming the
   theme's venues.
```

The theme is named by the round-74 block itself: "assimilation of the shokuknow
`merge/kotodama` worldbuilding-setting-practice theme" (L798-799). That theme's own proposed
entry declares **three** sources in one header block
(`lanes/kotodama/round2/KNOWLEDGE-PROPOSED.md:90-95`):

```
## corpus/knowledge/culture-material/worldbuilding-setting-practice.md
source: S882 — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf — аннотация — fetched 2026-10-23
source: S883 — https://litmemo.com/ja/blog/novel-worldbuilding-guide — … — fetched 2026-10-23
source: S884 — https://tuduku.space/column/novel-worldbuilding — … — fetched 2026-10-23
```

so the theme's venues are the MSU monograph host, litmemo and tuduku (round 3/4 add the
chinawriter pair, S899/S900 → lane S883/S884). The map agrees that staged S882 belongs to
this adoption set (`reused_rows`: `staged_id S882 → lane S877`, same philol URL). One of those venues is therefore already in the base registry:

```
$ git show f7104cbce186bc2e1522abf0cfd619cc834628bb:corpus/SOURCES.md | grep -c 'philol.msu.ru'
1
$ git show f7104cb:corpus/SOURCES.md | grep -o '^| S[0-9]* | [^|]*philol\.msu\.ru[^|]*' | cut -c1-60
| S877 | М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышле
$ for h in litmemo.com tuduku.space chinawriter.com.cn; do printf '%s ' "$h"; \
    git show f7104cb:corpus/SOURCES.md | grep -c "$h"; done
litmemo.com 0
tuduku.space 0
chinawriter.com.cn 0
```

So the sentence is true only for the three CJK host venues and false for the theme's fourth
venue, which the base registry names (S877). The entries' own `- ground:` lines state the
precise, defensible version —
`...the registry's 804 rows held no row naming litmemo.com, tuduku.space or chinawriter.com.cn`
(`culture-material/worldbuilding-setting-practice.md:8`) — so the compression in the README
is strictly weaker than the entry's evidence and overclaims.

Proposed fix (README L741-742):

> `... the theme had 0 filename owners and 0 registry rows naming its three CJK venues
> (litmemo.com, tuduku.space, chinawriter.com.cn); the theme's Russian monograph venue was
> already held as S877.`

(Under the other plausible reading — "the theme's *new* venues" — the sentence is true and
this collapses to LOW. The wording, not the fact, is the defect.)

### F2 — MEDIUM — the two rows are appended after `writing-media-surface-economy.md`, breaking the index's own filename-order invariant

The section was fully sorted at base, and the README states filename order as the landing
convention in every revision block ("Its row is added in filename order between …",
"in filename order before …", 20+ occurrences starting at L7). Measured sortedness per
section at base and main:

```
linguistics      main declared=30 rows=30 sorted=True | base declared=30 rows=30 sorted=True
myth-symbol      main declared=29 rows=29 sorted=True | base declared=29 rows=29 sorted=True
culture-material main declared=36 rows=38 sorted=False | base declared=36 rows=36 sorted=True
synthesis        main declared=29 rows=29 sorted=True | base declared=29 rows=29 sorted=True
verification     main declared=24 rows=24 sorted=True | base declared=24 rows=24 sorted=True
```

and the single deviation is exactly the round-74 pair:

```
first deviation at index 35 readme= writing-media-surface-economy.md
                            sorted= worldbuilding-setting-practice.amend-2026-10-23.md
last 4 readme: ['warrior-material-culture.md', 'writing-media-surface-economy.md',
                'worldbuilding-setting-practice.amend-2026-10-23.md',
                'worldbuilding-setting-practice.md']
last 4 sorted: ['warrior-material-culture.md',
                'worldbuilding-setting-practice.amend-2026-10-23.md',
                'worldbuilding-setting-practice.md', 'writing-media-surface-economy.md']
```

(`worldbuilding` < `writing` because `o` < `r`.) No instrument catches this: neither
`reports/round-27/readme/sweep.py` nor `reports/round-28/readme/sweep.py` has an order leg,
and claim C's INDEX leg (`accept-c.py:1756-1830`) checks membership, section containment and
topic equality only. It is therefore a live convention break that a green counter cannot see.

Proposed fix: move the two rows (L445-446) above `- \`writing-media-surface-economy.md\` …`
(L444), i.e. restore `sorted(rows)`; nothing else changes, the topic bytes stay as measured
in A1, and the section's declared-row arithmetic (36 declared / 38 rows) is unaffected.

### F3 — LOW/MEDIUM — the "partial one-way owners" list omits `linguistics/conlang-scholarship.md`, which the entry itself couples

README L742-746 names five partial one-way owners. The main entry's `- couples:` line names
**six** (`culture-material/worldbuilding-setting-practice.md:12`):

```
`culture-material/cartography-and-mapmaking.md` … `linguistics/naming-systems.md` …
`linguistics/conlang-scholarship.md` (how much language a world's function needs),
`synthesis/coupling-model.md` … `synthesis/consistency-verification-checklist.md` …
`synthesis/worldbible-integration-contract.md` …
```

and `conlang-scholarship.md` is a genuine partial scope of setting practice, not a
neighbour in name only — its §4 is titled "How much language the world actually needs" and
concludes (`corpus/knowledge/linguistics/conlang-scholarship.md:65`):

```
Design consequence: a setting that only needs names is not under-built, and dialogue that carries weight …
```

It also exists at base (`git cat-file -e f7104cb:corpus/knowledge/linguistics/conlang-scholarship.md`
→ present) and is byte-unchanged base..main (`git diff --quiet f7104cb main -- <path>` → 0),
so it satisfies the bullet's own definition ("partial one-way owner") and is omitted from
the enumerated set. The bullet's construction ("Partial one-way owners remain X, Y, Z") is
used elsewhere in this section as a complete list (cf. the round-64 bullet's three), so a
reader will read these five as exhaustive.

Proposed fix: add `` `linguistics/conlang-scholarship.md` `` to the list (six), or qualify
the sentence with "among others".

### F4 — LOW — the sweep-redness sentence explains the totals legs but only them, and its implied remedy cannot make the instrument green

README:818-820 (operative clause, 14 whitespace tokens):

> …one, so its own totals legs stay red until a successor instrument names the
> authoritative footer.

The first-footer parse is real and I reproduced it: `sweep.py:66` compiles `FOOTER_RE`,
`sweep.py:108` does `FOOTER_RE.search(text)` and `sweep.py:160` does
`TOTALS_RE.search(readme_text)` — both take the *first* match, i.e. the pre-round-73 reading
at L751-753 / `Total knowledge entries: 243.` at L749, while the live reading is the third
footer block at L815-816 (`Total knowledge entries: 249.` at L813). So "its own totals legs stay red" is literally true.

But the sweep is red on **six** leg classes, only two of which are totals legs (§3). A
reader who takes the sentence as the explanation and installs a successor instrument that
"names the authoritative footer" will still see exit 1 from `missing_from_index` (4),
`orphan_rows` (2), and `header_drift` (2). Of those, the *only* cause the round-74 text never
names anywhere is the mis-sectioning of the round-73 rows at L787-788 (attributed by the
sweep to `civilizations`, counted missing from `linguistics`), even though the round-74 block
goes out of its way to say its own block "carries no row-shaped line, so no row is attributed
outside a partition" (L803-804) — i.e. it names the hazard and leaves the existing instance
unnamed. The claim is not false; the disclosure is incomplete at exactly the point where the
document is explaining redness.

Proposed fix: extend the sentence, e.g. "…so its own totals legs stay red. The remaining red
legs are not footer-driven: `heritage-taxonomy-models{,.amend-2026-10-24-r13}.md` have no row
(this block names them), and the two round-73 rows at L787-788 sit outside any partition
section, so the sweep reads them as `civilizations` ghosts and `linguistics` gaps."

### F5 — LOW — the file's revision header is stale by three rounds and round 74 does not name it

README L3 still begins `revision: 2.21 — Round-71 culture-material landing (2026-10-25)`;
there is no `revision:` entry for rounds 72, 73 or 74 (`grep -c '^revision:'` → 28 blocks,
newest 2.21). The round-73 block does disclose the append-only reason for leaving the head
as filed (L785, "the revision block above stay as filed"), and both other stale
denominators (the two older footers, the `## culture-material/ (36)` heading) are named. The
revision line is the one stale self-description the round-74 block does not name, so a
reader who trusts L3 gets a file state three landings old.

Proposed fix: add one clause to the round-74 block — "the `revision:` header stays as filed
and is named stale: its newest entry is 2.21 (round 71)" — or record the same sentence the
round-73 block already carries.

---

## 3. `reports/round-28/readme/sweep.py` — leg-by-leg, and the "new defect?" question

### 3.1 Exact run at lane main (read-only; the tool opens files for reading only)

```
$ python3 -B reports/round-28/readme/sweep.py; echo "EXIT=$?"
parts {"civilizations": 95, "culture-material": 40, "linguistics": 32, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 247 files 249
missing_from_index 4 ['culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md', 'culture-material/heritage-taxonomy-models.md', 'linguistics/conlang-scholarship.amend-2026-10-23.md', 'linguistics/conlang-scholarship.md']
topic_mismatch 0 []
orphan_rows 2 ['civilizations/conlang-scholarship.amend-2026-10-23.md', 'civilizations/conlang-scholarship.md']
header_drift {'culture-material': {'declared': 36, 'files': 40}, 'linguistics': {'declared': 30, 'files': 32}}
totals_line 243 totals_ok False
footer {"date": "2026-10-25", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 243, "dir_totals": [30, 29, 36, 29, 24, 95]}
footer_live {"total": 249, "dir_totals": [32, 29, 40, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [{"class": "FOOTER_TOTAL", "declared": 243, "live": 249, "date": "2026-10-25"}, {"class": "FOOTER_DIR_TOTALS", "declared": [30, 29, 36, 29, 24, 95], "live": [32, 29, 40, 29, 24, 95], ...}]
readme_sha256 0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e
EXIT=1
```

### 3.2 Same instrument at the pinned base (clone in `/tmp/RevReadmeIndex/base`, checked out at base)

```
$ git clone -q --no-hardlinks --shared <lane> /tmp/RevReadmeIndex/base \
  && git -C /tmp/RevReadmeIndex/base checkout -q f7104cbce186bc2e1522abf0cfd619cc834628bb
$ python3 -B /tmp/RevReadmeIndex/base/reports/round-28/readme/sweep.py; echo EXIT=$?
parts {"civilizations": 95, "culture-material": 38, "linguistics": 32, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 245 files 247
missing_from_index 4 [heritage-taxonomy-models.amend-2026-10-24-r13.md, heritage-taxonomy-models.md, conlang-scholarship.amend-2026-10-23.md, conlang-scholarship.md]
topic_mismatch 0 []
orphan_rows 2 [civilizations/conlang-scholarship.amend-2026-10-23.md, civilizations/conlang-scholarship.md]
header_drift {'culture-material': {'declared': 36, 'files': 38}, 'linguistics': {'declared': 30, 'files': 32}}
totals_line 243 totals_ok False
footer {"total": 243, "dir_totals": [30, 29, 36, 29, 24, 95], ...}
footer_live {"total": 247, "dir_totals": [32, 29, 38, 29, 24, 95], ...}
EXIT=1
```

### 3.3 Which legs are red, and why

| leg | main | cause | round-74? |
|---|---|---|---|
| `missing_from_index` (4) | red | `heritage-taxonomy-models{,.amend-2026-10-24-r13}.md` have no row in `culture-material`; `conlang-scholarship{,.amend-2026-10-23}.md` have rows but not inside `## linguistics/` (they sit in the round-73 append block, L787-788) | **no** — identical 4 at base |
| `orphan_rows` (2) | red | `parse_readme` attributes every row after the last `## part/ (N)` header (`## civilizations/ (95)`, L505) to `civilizations`; the two round-73 rows at L787-788 are read as `civilizations/conlang-scholarship*.md` ghosts | **no** — identical 2 at base |
| `topic_mismatch` | **green** | `sweep.py:TOPIC_RE` value vs row body; 0 mismatches over 247 rows — this is the leg that grades the two new rows, and they pass byte-exact (A1) | green, and the new rows keep it green |
| `header_drift` | red | declared 36 vs 40 files (`culture-material`) and 30 vs 32 (`linguistics`) | **class pre-existing**; base was 36 vs 38. Round 74 moved only the live side (38→40), as it must: the heading may not be edited in place under the append-only rule, and the block names the heading stale (L805-806) |
| `totals_line` | red | first `Total knowledge entries:` match is 243 (L749), not the live 249 (L813); `sweep.py:160` `TOTALS_RE.search` | **no** — first match was 243 vs live 247 at base |
| `footer` total + vector | red | first `Counts checked` block is L751-753 (243 / 30-29-36-29-24-95), not the appended live block L815-816 (249 / 32-29-40-29-24-95); `sweep.py:108` `FOOTER_RE.search` | **no** — first block was the same 243/[30,29,36,29,24,95] at base (live 247/[32,29,38,29,24,95]) |

Answer to the ticket's question: **no red leg is a new defect of round 74.** The set of red
leg classes and the set of offending rows/paths/headings are identical at base and at main;
only the *live* side of two legs moved (249 instead of 247; culture-material 40 instead of
38) because the landing added two files. The round-74 rows themselves are green on the only
leg that measures them (`topic_mismatch 0`), and they are absent from both
`missing_from_index` and `orphan_rows`; the appended block's row-shaped-line avoidance is why
(§A8). The footer redness is (i) pre-existing by construction — claim C's INDEX leg
(`accept-c.py:1756-1830`) requires the *older* footers to stay byte-identical and reads only
the **last** one, so the first one can never be repaired without breaking either the
append-only rule or that leg — and (ii) exactly what README L818-820 says.

### 3.4 The instrument's own selftest is red at both revisions (context, not a round-74 finding)

```
$ python3 -B reports/round-28/readme/sweep.py --selftest; echo EXIT=$?
FAIL live: rows == files / 0 missing / 0 topic mismatches / 0 ghosts / 0 drift / footer ok {...}
… (11 PASS controls) …
selftest: FAILED
EXIT=1
```

11 planted controls pass (paraphrase, ghost, missing, header count, totals, duplicate, stale
footer total, stale footer vector, absent footer, correct footer, continuation lines); the
single failing control is the one asserting the **live tree** is clean, and it fails
identically at base (`/tmp/RevReadmeIndex/base` run: same FAIL, `rows 245 files 247`). So the
sweep has never been green on this tree and its `--selftest` is not a usable baseline for
"round 74 broke it". The README sentence does not mention the selftest; that is consistent
with its scoped wording ("its own totals legs"), but see F4 for the completeness problem.

---

## 4. Residual risk and verification gaps

- **R1 — the graded INDEX leg is weaker than the file's own convention.** `accept-c.py`
  `leg_index` (L1756-1830) checks: exactly one row per adopted entry, inside the
  `## culture-material/ (N)` section, body == `- topic:` verbatim, and the **last** footer's
  total + vector against the landed tree. It has no order leg (so F2 passes green) and its
  older-footer loop is `_footer_blocks(base_text)[:-1]`, which skips base's *last* footer —
  the round-73 reading that the round-74 landing is appended after. The README happens to
  satisfy the stronger property (A2: zero deletions), but the counter alone would not have
  caught an edit to that footer. No other leg reads the file at claim C's grading revision:
  accept-ca's APPENDONLY (`accept-ca.py:1361-1404`) would flag any modified (non-appended)
  README hunk, but it is graded at Ca's lands `5e4796c0`, where `git diff --stat base..5e4796c0
  -- corpus/README.md` is empty — the file is still base-identical there, so that backstop
  never sees the round-74 bytes. Not a README defect; recorded because it is the reason the
  README stays coupled to an instrument that cannot see the convention it states.
- **R2 — the registry's fifth touch is unmentioned in the README.** Base..main registry diff
  is `5 1`: four new rows plus an in-place rewrite of S877's used-by cell (now names the base
  entry as well). The block's "four new rows … used-by exactly the two files above" is true
  of the four rows, but a reader can meet S877's second used-by path without any README
  sentence introducing it. Claim C's ROWS leg requires the *lesson* to log that change, not
  the README; recorded as an observation, not scored.
- **R3 — no `lsp` device in this seat.** Caller/definition/diagnostics checks could not be
  run at all; every check above is a literal text measurement with its command shown. No
  claim here rests on grep-as-semantic-proof: the only semantic-looking statements (A6
  "without restating", A10 "named stale") are explicitly bounded to mechanical evidence.
- **R4 — unrun checks are not claimed.** The two round-74 counters were **not** re-run by this
  seat: they materialize clones and temp fleets under `/tmp/r74-*`, which is outside this
  seat's allowed write paths (report file + `/tmp/<seatname>/` + `.ufo/waves/round-74/`
  scratch). The committed receipt `reports/round-74/telemetry/measures-c.txt` attests
  `LEG PASS INDEX` / `ACCEPT-C-74: PASS legs=13/13` at `c4bf61a8`; I verified the same
  properties directly (§1-§2), which is the stronger check for this file because it does not
  depend on the counter's looser footer/order semantics (R1).
- **R5 — no new-defect claim is made for anything outside `corpus/README.md`.** The entries'
  content, the registry's row facts, and the lesson are other seats' scope; they were read
  only where the README change asserts something about them.

---

### Severity roll-up

| id | severity | one-line | fix |
|---|---|---|---|
| F1 | MEDIUM | "0 registry rows naming the theme's venues" is false for the theme's MSU-monograph venue (base row S877) | name the three CJK hosts, as the entry's `- ground:` line does |
| F2 | MEDIUM | two rows appended after `writing-media-surface-economy.md`; sole break of the section's filename order, no instrument catches it | move L445-446 above L444 |
| F3 | LOW/MEDIUM | "partial one-way owners" list omits `linguistics/conlang-scholarship.md`, which the entry couples and which §4 owns part of the theme | add it or qualify the list |
| F4 | LOW | sweep-redness sentence covers only the totals legs; the round-73 rows' mis-sectioning (L787-788) is the one red cause left unnamed while the block explains redness | extend the sentence with the remaining causes |
| F5 | LOW | `revision: 2.21` (round 71) is stale by three landings and is the one stale self-description round 74 does not name | add the same "left as filed and named stale" clause |

Attacks that failed (claims survived): **A1 verbatim rows, A2 zero deleted bytes, A3 footer
249 + 32/29/40/29/24/95, A4 zero filename owners at base, A5 five owner paths exist and are
one-way, A6 no restatement at 8-gram level, A7 exactly two unindexed culture-material files,
A8 no row-shaped line in the appended block, A9 registry 804→808 and the four rows' used-by,
A10 every drifting partition heading is named.** Sweep verdict: six red leg classes, all
present at base, none new from round 74.
