# ScoutReadmeIndex — README index, footer and SOURCES.md mechanics for the round-76 landing

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base `98c486bdb4650ba5b8e651d332910e8ee60ad121`; lane HEAD at read time `98c486b…` (`git rev-parse HEAD` printed it; `git status --short` showed only `?? .ufo/waves/round-76/` and `?? reports/round-76/`). All reads used `cd $L` plus plain `git show` / `grep` / `python3`; nothing mutated. Line numbers below are of the working tree = base bytes for `corpus/README.md` and `corpus/SOURCES.md`.

Round-75 landing commit: `4f5e3b2535c2c06c51627dc2736c40183847cae1` (parent `012e8d3` = round-75 claim Ca landing). Round-75 claim-C diff scope — `git show 4f5e3b2 --stat`: `corpus/README.md | 9 +-` (7 insertions-ish: 3 rows, 1 heading edit, blank + 2 footer lines), `corpus/SOURCES.md | 9 +` (9 appended rows, one hunk `@@ -837,6 +837,15 @@`, zero removed lines — `git show 4f5e3b2 -- corpus/SOURCES.md | grep '^-'` prints only the `--- a/` header), 3 entries, `corpus/lessons/round-75.md`, 9 evidence files `reports/round-75/evidence/S885..S893.txt`, `reports/round-75/telemetry/census-end.txt`. No Paths row, no Search-log note, no Leads change in round 75.

## 1. Six-partition vector at base (re-derived)

- Total — `git ls-tree -r --name-only 98c486b corpus/knowledge | grep -c '\.md$'` → `252`
- Per partition — `git ls-tree -r --name-only 98c486b corpus/knowledge | grep '\.md$' | awk -F/ '{print $3}' | sort | uniq -c` →
  `95 civilizations`, `40 culture-material`, `32 linguistics`, `32 myth-symbol`, `29 synthesis`, `24 verification`.
- The README writes the vector in README section order, NOT alphabetical: **32/32/40/29/24/95** = linguistics/myth-symbol/culture-material/synthesis/verification/civilizations.
- Live README headings agree (`grep -n '^## .*/ (' corpus/README.md`): 344 `## linguistics/ (32)`, 376 `## myth-symbol/ (32)`, 410 `## culture-material/ (40)`, 452 `## synthesis/ (29)`, 484 `## verification/ (24)`, 510 `## civilizations/ (95)`.
- Row census per section (python over README sections vs `os.listdir`): linguistics heading 32 / rows 30 / files 32 — missing from section: `conlang-scholarship.md`, `conlang-scholarship.amend-2026-10-23.md` (their rows live at README:792-793 inside `## Round 73 additions`, not in the section); myth-symbol 32/32/32; culture-material 40/40/40; synthesis 29/29/29; verification 24/24/24; civilizations 95/95/95. No ghosts anywhere. `grep -c '^- `' corpus/README.md` = 253 = 250 in-section rows (30+32+40+29+24+95) + 2 round-73 block rows (792-793) + 1 frontier bullet that starts with a backtick (README:634 `python3 tools/replay-frozen.py …`) — derived by arithmetic, not separately grepped.

## 2. Index-row shape (README)

One line per entry, in the partition section, shape `- \`<basename>.md\` — <entry's own \`- topic:\` text VERBATIM>` (em dash U+2014 with single spaces; regex used by round-75 counter: `^- \`([^\`]+\.md)\` — (.*)$`, README-side body not stripped, compared to the entry's `- topic:` value). Example (README:406-408 region, from the r75 diff):
`- \`narrative-structure-frameworks.amend-2026-10-23.md\` — how three articles of *Communications* 8 (1966) describe a narrative — …`
Source of the text: `grep -n '^- topic' <entry>` (e.g. `calendar-festival-systems.md` line 3, `era-periodization-models.md` line 3).

Row ORDER differs by section in practice:
- culture-material: filename order is sorted INSERT for r75 heritage rows (between `headgear-head-covering-codes.md` and `hunting-foraging-subsistence.md`; amend row before `.md` row) but the r74 worldbuilding rows are APPENDED after `writing-media-surface-economy.md` (README:450 > 449 order break: `writing-media-surface-economy.md > worldbuilding-setting-practice.amend-2026-10-23.md`).
- myth-symbol: r75 rows APPENDED after `trickster.md` (break at README:406).
- So the section lists are not strictly sorted (myth-symbol and culture-material fail `rows==sorted(rows)`; the other four pass). An accept counter must check set membership (one row per file in its section), not order.
- Sort order for the four candidate calendar/era files in plain Python `sorted()` (dot-amend sorts before `.md`; `-` < `.`): `calendar-festival-systems.amend-2026-10-23c.md`, `…amend-2026-10-24-r10.md`, `…amend-2026-10-24.md`, `calendar-festival-systems.md`, `era-periodization-models.amend-2026-10-23b.md`, `era-periodization-models.md`. Existing rows: `calendar-festival-systems.md` README:416, `era-periodization-models.md` README:423. Sorted insert would put the three calendar amend rows immediately BEFORE line 416 and the era amend row immediately BEFORE line 423 (the r75 heritage precedent).

## 3. `## culture-material/ (N)` heading

Exact text at base: `## culture-material/ (40)` (README:410; followed by a blank line, then the first row `adornment-body-codes.md`). Regex `^## ([a-z-]+)/ \((\d+)\)\s*$`. r75 edited the myth-symbol heading in place (`## myth-symbol/ (29)` → `(32)`, the only non-row/non-footer README change in 4f5e3b2); the counter exempted partition-heading lines. With n admitted culture-material files (n≥2 per CLAIMS-DRAFT, 4 candidates), the heading would read `(40+n)` and the total `252+n`. The r71 revision-block history shows the header drift hazard (heading stale vs. files); `## linguistics/ (32)` is currently correct but has 30 in-section rows (the 2 round-73 rows are in the append block).

## 4. Newest `Counts checked` footer (README:829-831, last lines of file; line count 831)

```
Total knowledge entries: 252.

Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 252 files; directory totals 32/32/40/29/24/95).
```
Shape: blank line, `Total knowledge entries: N.`, blank line, `Counts checked <YYYY-MM-DD> from the repo root: \`find corpus/knowledge -type f -name '*.md' | wc -l\` (total N files; directory totals a/b/c/d/e/f).` — r75 APPENDED these 3 lines after the previous footer block (README:818-820 is the r74 block `Total … 249` / `Counts checked 2026-10-25 … (total 249 files; directory totals 32/32/40/29/24/95)` + a paragraph about older footers). Earlier footers (README:754/756 `243`, 797/799 `247`, 818/820 `249`) are kept byte-identical, the append-only dated record (counter rule R4 "every base `Counts checked` block byte-identical"; R5 "the appended footer = last `Counts checked` line"; R7 "every base README line survives verbatim, only partition-count heading lines change"). Footer regexes: `\(total (\d+) files; directory totals ([\d/]+)\)`. Note `reports/round-28/readme/sweep.py` still parses the FIRST footer (README:756 era), so its totals legs stay red by design (README:822-828 says so). Round-76 footer for n landed files: `Total knowledge entries: <252+n>.` + `Counts checked 2026-10-27 …` (total <252+n> files; directory totals 32/32/<40+n>/29/24/95 if all n are culture-material).

No `revision:` block was added by rounds 72-75 (latest at README:3 is `revision: 2.21` r71); r73/r74 used `## Round 73 additions` / `## Round 74 landing` appended blocks, r75 used only rows + footer. r74 block (README:801-826) deliberately carries no row-shaped line.

## 5. SOURCES.md structure (945 lines)

`grep -n '^## ' corpus/SOURCES.md`: `# SOURCES — where kotodama learns` (1), `## Registry` (26), `## Paths` (849), `## Search log` (884), `## Leads (unopened)` (896). Registry rows end at line 847 (S893) and `## Paths` starts at 849; r75's hunk shows the S885-S893 rows are followed directly by `## Paths` with NO blank line in between (diff context: row S893, then `## Paths`, `` blank ``, first Path bullet). A new row S894+ goes after S893 line (847), before `## Paths`; keep the same no-blank adjacency or counter regexes may differ — copy the r75 shape.

Registry: `grep -c '^| S[0-9]'` = 817; unique ids = 817; `grep -c 'S894\|S898'` = 0 (no S894-S898 held, matches the draft's before-state).

Row shape — 11 pipe-cells (`split(' | ')` = 11): `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`; header at line 28, separator line 29. S885: kind `paper`, tier `A`, status `mined`, opened `2026-10-27`, recheck `180d`, used-by = comma-joined repo-relative entry paths with trailing ` |` (e.g. `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md, …amend-2026-10-23.md, …amend-2026-10-23b.md |`). The `source` cell carries author/title/venue + URL + the access sentence (HTTP status, bytes, UA when browser-shaped, any challenge "met and left unsolved", Wayback `id_` capture URL when the live URL failed — see S891, S892). Kinds seen: paper/docs/community; tiers A/B/C, tier C never sole support. The anchor cell: page/section + "quote located: «…»" (the Gate quote). `S885`/`S892` used-by cells (in place editable: only `status`, `recheck`, `used-by` may change): S885 used-by = three narrative-structure files; **S892 used-by = `…narrative-structure-frameworks.amend-2026-10-23b.md |` only**. The draft maps campaign S919→lane S892 and S921→lane S885, so if admitted calendar amend files cite them, those two used-by cells are extended IN PLACE (precedent: r74 extended `S877` used-by; `S877` now ends `…conlang-scholarship.md, …worldbuilding-setting-practice.md |`; changed pre-existing-row lines are append-only-exempt only inside `used-by`/`status`/`recheck`, per r75 accept-ca APPENDONLY leg text).

## 6. `## Paths` shape

Bullets `- <slug> — S001 → S002 → …: <sentence>` (some with `Typology evidence chain —` capitalised first word, later ones lowercase), one per chain of rows that should be read in order. Last Path (line ~882): `- signed-language design — S071 → S096 → S133 → S095 → S087 → S100 → S118: Stokoe's parameters first, …`. No round after the sign-language round (r22) has added a Path; r73-r75 added none. A Path row is optional; if the scribe adds one for calendar sources, shape = `- calendar and era instruments — S894 → S896 → S897 → S898 → S895: <order of reading>` (INFERENCE: no round-75-style precedent; copy the dash/arrow form above).

## 7. `## Search log` shape and where a round-76 note goes

Lines 886-894: five entries separated by blank lines, each one paragraph starting `**<Theme> (rows S0NN–S0MM).**` then `Question: …`, `Where searched: …`, counts `Identified N, screened N, included N … excluded … rejected …`, and some `corrections` clauses. Headings: S001–S015 (886), S016–S030 (888), S031–S043 (890), S048–S069 (892, "Round 50, 2026-10-21."), and the LAST entry **line 894: `**Sign languages and manual modality (rows S071–S124).** 2026-10-22. Question: which opened sources can ground a sign-language and manual-communication register …`** (1868 bytes). Line 895 is blank and line 896 is `## Leads (unopened)`. So: NO Search-log note exists for any row after S124 (rows S125–S893, rounds 51-75, added none — header text at SOURCES.md:7-10 says the lesson `## Gate` holds each row's evidence and "from S071 onward the lesson of the round dated in the row's `opened` cell and search-log note"; in practice the lesson is the carrier). A round-76 Search-log note would be a new `**Calendar and era instruments (rows S894–S898).** 2026-10-27. Question: … Where searched: … Identified/screened/included/excluded …` paragraph inserted after line 894 + blank, before `## Leads`. It is optional by precedent (r72-r75 skipped), so the scribe must decide; if added, it is an addition (append-only compatible, zero removed lines). `## Leads (unopened)` (896-945): `**Linguistics, folktale, period, costume and iconography** (rows S001–S030) — …` (900) and `**Hunting and foraging** (rows S031–S043):` (935) lists; bullets `- <citation> — <URL> (to-verify)`. Nothing after S043; leads from round 76 would go as a new bold-headed block at the end of the file (INFERENCE — no precedent after S043).

## 8. README `## Known gaps (frontier)` list (README:608-787) — exact bullets, so a scribe can name rows that advance

Heading `## Known gaps (frontier)` at README:608; the bullets, by first line (`awk 'NR>=608&&NR<=787 && /^- /'`):
1. 610 `- The five carried civilization entries have per-claim supplemental rechecks (Ottoman, early Slavic, Sogdian, Tibetan, Turkic)…`
2. 621 `- Round 6 adds 24 fixed questions across twelve existing earlier-reference entries…`
3. 634 `- \`python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv\` now verifies gate/input/output digests…`
4. 642 `- Most historical entries lack the fleet's complete \`source\`, \`verified-at\`, \`recheck\` header…`
5. 645 `- D2 still needs typed native-form/translated-label handling…` (superseded note inside)
6. 656 `- D3 (\`examples/culture-d3/\`) adds a separate source-bounded NON-CANON miniature-culture exercise…`
7. 670 `- Five round7 live constraint rechecks remain three scoped and two partial supports…`
8. 675 `- Round 10 adds ten thin-partition entries…`
9. 689 `- Earlier round-local acceptance scripts retain strict historical path whitelists…`
10. 693 `- Cultural permission, real-language name screening, a lore receipt and…`
11. 695 `- Round 19 adds ten thin-partition entries (verification 5, synthesis 5…`
12. 713 `- Round 20 reconciles the index (199 rows vs 199 files; 0 missing, 0 ghosts…`
13. 734 `- Round 64 adds one linguistics entry, \`linguistics/language-socialization-and-acquisition.md\`…`
14. 735 `- Round 66 adds \`scent-perfume-aromatics-codes.md\` … (22 new registry rows S779-S800)…`
15. 736 `- Round 67 adds \`medicine-healing-codes.md\` … (24 new registry rows S805-S828)…`
16. 737 `- Round 65 adds \`games-play-sport-contests.md\` … Partial scopes remain in … \`culture-material/calendar-festival-systems.md\`…`
17. 738-748 `- Round 74 adds the culture-material entry \`worldbuilding-setting-practice.md\` (…) and its amendment … At the pinned base \`f7104cb\` the theme had 0 filename owners and 0 registry rows naming the theme's venues. Partial one-way owners remain …`
Then the "Total knowledge entries: 243." footer era (754-) and index re-measure paragraphs, then `## Round 73 additions` (788) and `## Round 74 landing` (801).

Observations for the scribe: (a) the frontier list holds NO bullet for calendar/era-name tables or GB/T 33661 — `awk 'NR>=608&&NR<=830' corpus/README.md | grep -n -i 'calendar\|era-name\|era name\|periodiz\|GB/T'` hits only the Round-65 bullet (the games entry names `culture-material/calendar-festival-systems.md` as a partial-scope owner) — so the claim's "frontier -> core" movement has no existing bullet to advance; the scribe should state the move in a NEW appended block or bullet (precedent: r74 appended `Round 74 adds …` bullet at 738 AND a `## Round 74 landing` block; r75 added neither, only rows + footer — so r76 minimum precedent = rows + footer, which is what the r75 counter's README leg enforces: README diff scope = {index rows, partition heading counts, `Total knowledge entries`/`Counts checked` block}; any other changed/removed line fails; an appended block is allowed only if the counter's scope names it — copy r75's accept-c.py README leg text (lines 3836-3882) and widen the scope explicitly if a frontier bullet is added). (b) Rows inside frontier bullets are never `- \`x.md\` — ` shaped except the Round-73 block (792-793) — a row-shaped line outside a partition gets attributed to the wrong place (r74's block comment: "this block deliberately carries no row-shaped line").

## 9. `tools/check-cited-lines.py` CLI

- `python3 tools/check-cited-lines.py --help` →
  ```
  usage: check-cited-lines.py [-h] [--selftest] [PATH ...]
  Report knowledge lines that carry several source ids, and table rows that carry one.
  positional arguments:  PATH  file, or directory walked for *.md
  options:  -h, --help  show this help message and exit;  --selftest  run the in-process cases
  ```
- `python3 tools/check-cited-lines.py --selftest` → 26 PASS lines ending `selftest 26/26`, exit 0.
- Output: `MULTI-ID <path>:<lineno> <ids>` (≥2 distinct `\bS\d{3,}\b` ids on the line) and `TABLE-ID <path>:<lineno> <ids>` (line starting `|` after whitespace carrying ≥1 id; a row with 2 ids is 2 findings); last line `CITED-LINES: <k> finding(s) in <m> file(s)`; exit 1 when k>0, 0 when k=0, 2 with `CITED_LINES_ERROR` on stderr (no PATH, missing PATH, unreadable/invalid UTF-8; `--selftest` with a path errors). Read-only, stdlib only, deterministic.
- At base: `python3 tools/check-cited-lines.py corpus/SOURCES.md >/dev/null; echo exit=$?` → `exit=1` (`CITED-LINES: 916 finding(s) in 1 file(s)`: every registry row is a TABLE-ID finding plus the multi-id Search-log/Leads/Paths lines, e.g. `MULTI-ID corpus/SOURCES.md:892 S048,S053,S069`, `:894 S071,S111,S122,S123,S124`, `:900 S001,S030`, `:935 S031,S043`). `corpus/README.md` → `exit=1`, 5 MULTI-ID findings (lines 11, 20, 735, 736, 812: `S861,S873`, `S833,S856`, `S779,S800`, `S805,S828`, `S881,S884`). It is therefore a lint for KNOWLEDGE entries (its intended target: `corpus/knowledge`), not for SOURCES/README; do not gate the landing on exit 0 for those two files. A round-76 README/SOURCES text that writes ranges like `S894-S898` on one line adds a MULTI-ID finding only if two distinct ids are written out literally (the tool matches ids, not ranges; `S894-S898` carries two ids → finding), the same way r74's block line 812 does — so for the entries themselves (calendar amend files) keep one id per cited line.

## 10. Unrun / not established
- I did not run `reports/round-28/readme/sweep.py` or the r75 `accept-c.py` (read-only recon; both are scribe/L1 instruments).
- The 253 raw bullet count is reconciled by arithmetic only (see §1), not by a separate grep.
- No install performed. No scratch directory created (nothing needed under `/fast/scratch`).
