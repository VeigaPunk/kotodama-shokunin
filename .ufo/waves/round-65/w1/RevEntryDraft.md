# RevEntryDraft — pre-integration checklist for the round-65 games entry

Seat: `kotodama-r65.RevEntryDraft` (reviewer, claim C entry draft). Lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base = `main` = `17c32302c6845c8f164b985a8cb312d3181c8788`
(measured: `git rev-parse main` prints the base; the wave is only minutes old, so a
declaration commit that moves `main` later does not change any command below).

Read for this review: `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
(the round-64 model entry, unchanged from base — `git diff 17c32302 -- <entry>` is empty),
`.ufo/waves/round-64/rows/ScribeRowS718/row.txt` (model fragment; note the real directory
name is `ScribeRowS718`, not `ScribeRow718`), the per-row artifacts S724/S732/S740/S741/S743,
`corpus/lessons/round-64.md` R64-M1..M19, `reports/round-65/accept-{c,o,ca}.py`,
`reports/round-65/claims.json`, `tools/check-row-fragments.py`,
`.ufo/waves/round-65/stage/assemble-entry.py` + `assemble-audit.json` + `entry-draft.md`,
`reports/round-65/telemetry/*`.

Tooling: none installed, nothing upgraded. No `lsp` device is in this seat's inventory; the
review targets are prose/data rows and Python counters, so the semantic authority used here is
the counters' own execution plus `git`/`curl` — no text-grep result below is presented as a
substitute for a counter leg.

Verdict up front: the draft is pre-data (0 of 26 rows landed) and cannot be scored yet; the
checklist below is the gate to run before the entry is staged at its corpus path. Three of the
checks fail on today's bytes (M1, M10, X3), and the model itself carries two defects the draft
has already copied (X1, X9).

---

## A. Findings, severity order

### F1 HIGH — the O claim's FRAG leg is format-coupled to `ROW=`/`BULLET=`, and every real row fragment in this lane uses `ROW:`/`BULLET:`
`tools/check-row-fragments.py:44` accepts only `^(ROW|BULLET|VERIFY|CAPTURE|ACCESS)=…`, while
the assembler the wave actually uses accepts both separators
(`.ufo/waves/round-65/stage/assemble-entry.py:38`, `\s*[=:]\s?`), and the model fragment every row
seat is told to read uses colons (`ROW: | S718 | …`, `BULLET: - …`).
Measured: `python3 -B tools/check-row-fragments.py --rows .ufo/waves/round-64/rows` →
`33 finding(s) in 33 file(s)`, every one `no-ROW`, exit 1. So the live leg
`python3 -B reports/round-65/accept-o.py --only FRAG` (bytes at 01:53 enforce
`files == 26`, lines 1232-1241) will print FAIL over 26 colon-format fragments, and the
teaches-length/URL-normalisation checks it exists to run never execute. The vacuous-empty-dir
half of the round-64 residual IS closed (`files=0/26` now fails); the format half is not.
Pre-integration check: **X3**. Fix before data: state the `ROW=`/`BULLET=` contract in the
row-seat briefs (fragments are claim-C build artifacts, not a frozen land), or widen the
checker's `LABEL_RE` pre-data with a new forcing control. Do not let the O seat "fix" this by
pointing `--rows` at an empty or `=`-only fixture.

### F2 HIGH — R64-M1 is repeating: the round-65 counters and claims exist only as untracked worktree bytes while the wave runs
`git ls-tree --name-only main reports/round-65/` prints **nothing**; `git status --porcelain
reports/round-65` prints `?? reports/round-65/`. `main` is still the declared base
`17c32302`, so none of `accept-c.py` (rev1), `accept-o.py`, `accept-ca.py`, `claims.json` or the
receipts is bound to any committed revision the wave declares. This is the exact class the
round-64 lesson records as still open (R64-M1) and the reason a post-hoc receipt cannot be
re-attributed. Pre-integration check: **M1**.

### F3 HIGH — the rev1 near-copy hardening has no forcing control on disk, and control 1 records an impossible exit code
`grep -c 'teaches_nearcopy=' reports/round-65/telemetry/controls-c.txt` → **0**: the rule's name
appears only in the file's own prose note (line 23), never in a printed leg detail, so the artifact
at the canonical controls path does not show the new rule firing. The same note defers the
demonstration to another seat ("the nearcopy-first demonstration rides seat MutCounterC's crafted
fixtures"). Worse, control 1 records
`ACCEPT-C-64: FAIL` immediately followed by `exit=0` (lines 6-7) — `accept-c.py` returns 1 on a
FAIL verdict (`return 0 if verdict else 1`), so the recorded exit is the wrapper's, not the
counter's; a receipt line that cannot come from the measured binary (R64-M17/M8 class).
Pre-integration check: **M10**. A correct forcing control must print the FAIL detail
`teaches_nearcopy=0.9x` on a fixture whose only failing property is the teaches reuse.

### F4 MEDIUM — the model entry ships a stale pre-data stamp, and the round-65 draft has copied the pattern
`corpus/knowledge/linguistics/language-socialization-and-acquisition.md:5` (present at base
`17c32302`, unchanged):
`- verified-at: 2026-10-23 — skeleton structure prepared; cited source claims await L1 insertion and review.`
The shipped entry carries 26 cited claims, so that line is false on its face. The draft
`.ufo/waves/round-65/stage/entry-draft.md:5` already carries the analogue
(`DRAFT assembled from 0 of 26 row fragments; cited source claims await L1 insertion and review.`)
plus a second stale stamp at line 8, `<!-- assembly: 0 of 26 row fragments landed at generation
time; … -->`, plus line 82 `No cross-row pattern is asserted: no supporting row had landed at
assembly time.` The counter's MARK_RE only inspects lines that carry an S-id
(`accept-c.py`, ONEID leg), so none of these lines is caught by ACCEPT-C-65.
Pre-integration check: **X1**.

### F5 MEDIUM — model bullets widen or add beyond their anchored row (M7/M15 class)
- `:49` — `Children sometimes avoid heritage language and favor majority-language speech, shifting
  family conversation. (S732)` — S732's scope is "children's choice … **in immigrant households**"
  and its quote says "bilingual children **in immigrant households** sometimes avoid …". The
  bullet drops the sampled population, so it asserts a generalisation the row does not support.
- `:18` — `Early child phrases favor content words … shaping terse dialogue (S724)` — the quote
  says "mostly content words … **with few function words** and few inflectional morphemes"; the
  bullet drops the function-word half and adds "shaping terse dialogue", which is not in the
  quote (S724's own teaches cell says "content-word-heavy phrases and sparse inflectional
  marking" — no dialogue claim).
Pre-integration check: **X2** (mechanical qualifier test) plus the M7 blind table.

### F6 MEDIUM — claim C's frontier command is not reproducible as quoted
`claims.json` claim C states
`git ls-tree -r --name-only 17c32302 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'`
prints 0. Measured at base: **2** —
`corpus/knowledge/culture-material/sumptuary-law-rank-display.md` (`play` inside "display") and
`corpus/knowledge/culture-material/transport-mobility-lexicon.md` (`sport` inside "transport").
The word-boundary variant prints 0:
`… | grep -ciwE 'game|play|sport|contest|toy|mancala'` → 0. The conclusion (no games/sport
owner) holds; the quoted command in the frozen claim sentence does not. Pre-integration check:
**X7** — restate the frontier with `-w` (or with the matched file list) in the round-65 lesson;
do not let a report copy the substring command as evidence.

### F7 MEDIUM — teaches-length is bounded in characters, not the lane's ≤25 words
`tools/check-row-fragments.py:36` sets `TEACHES_MAX = 240` (**chars**) and the C ROWS leg does not
check teaches at all. A 26-34-word teaches cell (~200-230 chars) passes both while violating the
round-64 M15 rule ("the ≤25-word rule"). Existing rows are 14-15 words, so the gap is latent, not
active. Pre-integration check: **X5**.

### F8 MEDIUM — the near-copy rule is order-sensitive; a shuffled teaches paraphrase passes
`accept-c.py:145` computes in-order subsequence coverage. Measured with the counter's own
functions on S718's teaches cell:
verbatim + one trailing word → `cov=0.941` (caught, the intended fix);
same content reordered → `cov=0.533` (**PASS**), even though it reuses nearly every content word
of the teaches cell; the separate "no novel content word" test compares against the *quote*, so
reordering introduces quote-novel words and clears it. The claim's wording ("RESTATE … near-copy
rule") should not be read as closing word-order-shuffled reuse. Pre-integration check: **X6**
adds an order-free teaches-reuse floor to the seat-local pre-check.

### F9 MEDIUM — the draft carries internal review vocabulary into the entry body
`.ufo/waves/round-65/stage/entry-draft.md` has five unnumbered lowercase H2s after nine numbered
ones (`## What a worldbuilder does with this`, `## cross-cultural patterns`, `## calibration`,
`## one-way pointing to partial owners`, `## lore handoff`). `one-way pointing to partial owners`
is verbatim the `claims.json` review_only phrase, and `## calibration` is registry/verification
meta (`tier A marks a peer-reviewed paper …`) that the model entry keeps out of the body. This is
process leakage into a corpus land, plus a heading-style inconsistency the model does not have
(`## 9. What a worldbuilder does with this`, `## 10. Handoff`). Pre-integration checks: **X8**,
**X9**.

### F10 LOW — the model's bullets are inconsistently punctuated
10 of the model entry's 26 bullets end without a terminal period (`:18`, `:24`, `:26`, `:33`,
`:39`, `:40`, `:41`, `:42`, `:47`, `:64`) while the others end with one. Cosmetic, but the draft
inherits whichever the assembler copies. Pre-integration check: **X8**.

### F11 LOW — the frozen C counter emits a SyntaxWarning on every run
`reports/round-65/accept-c.py:99` — `maximal [\w]+ runs.` in a non-raw docstring →
`SyntaxWarning: "\w" is an invalid escape sequence` on stderr. It is already pasted into the heads
of `dry-run-c.txt` and `controls-c.txt`, so receipts carry interpreter noise (and will break on a
future Python). `python3 -W error::SyntaxWarning -m py_compile reports/round-65/accept-c.py` fails
today. Pre-integration check: **M18**.

### F12 LOW/INFO — O's FRAG leg makes ACCEPT-O-65 depend on claim C's build artifacts
`accept-o.py` FRAG scans the default `.ufo/waves/round-65/rows` and requires exactly 26 files.
`claims.json.separability` says the counters are re-runnable in any order as record lands; that
holds for lands, but it should not be read as O being scorable before C's row seats deliver.
Measured now: `--only FRAG` → `FRAG FAIL … files=0/26` (the count check itself is good; it is the
dependency that needs saying). Check: **X4**.

---

## B. Checklist — R64-M1..M19, each as a pre-integration check

Run from the lane root. "PASS" is the condition that must hold before the entry is staged at
`corpus/knowledge/culture-material/games-play-sport-contests.md`. `$E` below is that path.

### M1 — counters and receipts are committed before the wave scores anything (R64-M1)
```sh
git ls-tree --name-only main reports/round-65/
git status --porcelain reports/round-65
```
PASS: the first lists `accept-c.py accept-o.py accept-ca.py claims.json`; the second is empty.
**Today: FAIL** (`?? reports/round-65/`).

### M2 — attribution names the canonical file and cites real mistake ids (R64-M2)
```sh
grep -n 'corpus/LOG.md' corpus/lessons/round-65.md
for id in $(grep -ohE 'R6[0-9]-M[0-9]+' corpus/lessons/round-65.md LOG.md | sort -u); do
  r=${id:1:2}; f=corpus/lessons/round-$r.md
  [ -f "$f" ] && ! grep -q "$id" "$f" && echo "MISSING $id in $f"
done
```
PASS: no `corpus/LOG.md` attribution (root `LOG.md` is canonical); no `MISSING` lines.

### M3 — no dead seat: all 26 row fragments exist exactly once (R64-M3)
```sh
grep -rhoE 'ROW\s*[:=]\s*\|\s*S7(5[0-9]|6[0-9]|7[0-5])\s*\|' .ufo/waves/round-65/rows \
  | grep -oE 'S7[0-9]{2}' | sort | uniq -c | awk '$1!=1'
grep -rhoE 'ROW\s*[:=]\s*\|\s*S7(5[0-9]|6[0-9]|7[0-5])\s*\|' .ufo/waves/round-65/rows | wc -l
```
PASS: first empty; second prints 26. A dead row seat must be re-dispatched to land `row.txt`,
not merely a report (`check-rows.py` MISSING class).

### M4 — anchor cell shape: one quoted span, body sentence first, 8-25 words (R64-M4)
```sh
python3 - "$E" <<'EOF'
import glob,re,sys
Q=re.compile(r'"([^"]+)"|\u201c([^\u201c\u201d]+)\u201d')
W=re.compile(r'[\W_]+')
bad=0
for p in sorted(glob.glob('.ufo/waves/round-65/rows/**/row*.txt',recursive=True)):
    for ln in open(p,encoding='utf-8'):
        if re.match(r'\s*ROW\s*[:=]',ln):
            cs=[c.strip() for c in ln.strip().split('|')[1:-1]]
            if len(cs)!=11: print('cells',p,len(cs)); bad+=1; continue
            ms=Q.findall(cs[5])
            if len(ms)!=1: print('quotes',p,len(ms)); bad+=1; continue
            q=(ms[0][0] or ms[0][1]); n=len([w for w in W.sub(' ',q).split() if w])
            if not 8<=n<=25: print('words',p,n); bad+=1
print('M4', 'PASS' if not bad else 'FAIL', bad)
EOF
```
PASS: `M4 PASS 0`. Counter `anchor_quote()` takes the **first** quoted span, so a curly-quoted
locator in front of the body sentence silently becomes "the quote" (exactly R64-M4); keep the
locator unquoted.
Then locate the quote on the cited page (per row):
```sh
curl -sL --max-time 30 "$URL" | tr -s '[:space:]' ' ' | grep -Foc "$QUOTE"
```
PASS: ≥1. PDFs: extract with the locator's own `pypdf 5.4.0`, not `pdftotext` (R64 Gate note,
S735 extraction difference).

### M5 — one row per work: no duplicate work behind different URLs (R64-M5)
```sh
grep -rhoE '10\.[0-9]{4,}/[^ |;]+' .ufo/waves/round-65/rows | sort | uniq -d
python3 -B tools/check-row-fragments.py | grep dup-url
```
PASS: both empty. Also compare title/author-year stems:
`grep -rhoE 'ROW\s*[:=]\s*\| S7[0-9]+ \| [^|]{10,120}' .ufo/waves/round-65/rows | sed -E 's/.*\| //' | sort | uniq -d` → empty.
The LINK leg counts URL strings and cannot see work identity, so this leg is reviewer-owned.

### M6 — the entry is assembled from current row artifacts, not a second authority (R64-M6)
```sh
python3 -B .ufo/waves/round-65/stage/assemble-entry.py
python3 -c "import json;d=json.load(open('.ufo/waves/round-65/stage/assemble-audit.json'));print(d['landed_count'],d['fragment_conflicts'],d['url_duplicates'],d['missing'])"
grep -n 'bullets.json\|stage/report.txt' .ufo/waves/round-65/stage/assemble-entry.py
diff <(grep -h '^BULLET[:=]' .ufo/waves/round-65/rows/**/row*.txt | sed -E 's/^BULLET[:=]\s*//' | sort) \
     <(grep -E '^- .*\(S7[0-9]{2}\)$' "$E" | sort)
```
PASS: `26 [] [] []`; no reference to the round-64 dead inputs; the bullet diff is empty (or each
difference is a stated rewrite with its row).

### M7 — no bullet overreach past its quote (R64-M7)
Mechanical half: **X2** (population/limit qualifiers). Review half — print the blind table:
```sh
python3 - <<'EOF'
import glob,re
Q=re.compile(r'"([^"]+)"|\u201c([^\u201c\u201d]+)\u201d')
rows={}
for p in sorted(glob.glob('.ufo/waves/round-65/rows/**/row*.txt',recursive=True)):
    for ln in open(p,encoding='utf-8'):
        if re.match(r'\s*ROW\s*[:=]',ln):
            cs=[c.strip() for c in ln.strip().split('|')[1:-1]]
            if len(cs)==11:
                q=Q.search(cs[5]); rows[cs[0]]=(q.group(1) or q.group(2)) if q else '', cs[6], cs[4]
for sid in sorted(rows): print(sid,'|Q|',rows[sid][0],'|SCOPE|',rows[sid][2])
EOF
```
PASS: a reviewer marks every bullet's clause entailed by quote+scope, with each qualifier
("in this sample", "in immigrant households", "one classroom", "Japanese", "North American")
kept; a design implication ("giving worldbuilders …") must be grounded in the quote, not invented.
Model precedents that failed this: S732 (population dropped), S724 (added effect), S737 (invented
worldbuilding outcome, repaired in round 64).

### M8 — receipt identity binds a revision and a sha (R64-M8)
```sh
sha256sum reports/round-65/accept-c.py reports/round-65/accept-o.py reports/round-65/accept-ca.py
head -8 reports/round-65/telemetry/final-measures-c.txt
tail -2 reports/round-65/telemetry/final-measures-c.txt
grep -nE 'revision [0-9]' reports/round-65/accept-c.py | head -3
```
PASS: the receipt header's counter sha equals the live sha, the measured revision is named, the
tail has `ACCEPT-C-65: PASS` and `exit=0`, and each docstring's revision agrees with its body
(the round-64 label-vs-bytes defect: cite by sha, not by label).

### M9 — claim text says only what the counter measures (R64-M9)
```sh
grep -nE 'exactly|exclusiv|superset|every leg' reports/round-65/claims.json
timeout 1800 python3 -B reports/round-65/accept-o.py --only MUTEX | tail -3
```
PASS: any exclusivity word is backed by MUTEX's disclosed expectation table (m1
+EDGE_USERINFO+EDGE_HTTPS; m2 +EDGE_MALTARG; the rest pinned-only), and no sentence claims
exclusivity for mutants the table does not cover. If the sentence and the table disagree, revise
the sentence **pre-data** (frozen-predicate rule allows the prose, not the predicate).

### M10 — controls are forcing, not vacuous (R64-M10)
```sh
grep -c 'teaches_nearcopy=' reports/round-65/telemetry/controls-c.txt       # ≥1
grep -nE 'ACCEPT-C-65: (PASS|FAIL)' reports/round-65/telemetry/controls-c.txt
grep -nE 'ACCEPT-C-64: (PASS|FAIL)' reports/round-65/telemetry/controls-c.txt
grep -nE 'exit=[0-9]+' reports/round-65/telemetry/controls-c.txt
grep -n 'NITS FAIL' reports/round-65/telemetry/controls-ca.txt
grep -nE 'FRAG (PASS|FAIL)' reports/round-65/telemetry/controls-o.txt
```
PASS: the round-65 form fails on the intended leg **via the intended rule** (a printed
`teaches_nearcopy=` detail, `norm_dup_of`, `NITS correction_record=False`, `FRAG files=0/26`), the
old form passes the same fixture, and every recorded `exit=` is the counter's own (FAIL ⇒ 1).
**Today: FAIL** — 0 printed `teaches_nearcopy=` details; control 1 shows `ACCEPT-C-64: FAIL` +
`exit=0` at lines 6-7.

### M11 — every declared land has an owner and a receipt (R64-M11)
```sh
python3 - <<'EOF'
import json,os
d=json.load(open('reports/round-65/claims.json'))
for c in d['claims']:
    for p in c['lands']:
        print('OK' if os.path.exists(p) else 'MISSING', c['id'], p)
EOF
ls reports/round-65/telemetry/controls-*.txt
```
PASS: no `MISSING` for record lands that must exist pre-data (the entry path is expected absent
until staging); exactly `controls-c.txt controls-o.txt controls-ca.txt`.

### M12 — the registry edit is the enactment; the log may only say "selected" (R64-M12)
```sh
awk -F'|' '/^\| S7(5|6|7)/ {gsub(/ /,"",$2);gsub(/ /,"",$9);print $2,$9}' corpus/SOURCES.md | sort | uniq -c
grep -nE 'S7(5|6|7)[0-9]' LOG.md
```
PASS: every new row reads `mined` in the registry; `LOG.md` never claims a status flip that the
registry cell does not carry (the S687 precedent); the APPEND leg confirms all 675 base lines
verbatim and 701 measured.

### M13 — one id per cited line; no id ranges on a cited line (R64-M13)
```sh
python3 -B tools/check-cited-lines.py "$E"
grep -nE 'S7[0-9]{2}[[:space:]]*[-–—][[:space:]]*S7[0-9]{2}' "$E"
awk '/S7[0-9][0-9]/{n=gsub(/S7[0-9][0-9]/,"&"); if(n!=1) print NR": ids="n}' "$E"
```
PASS: `0 finding`; no id range anywhere in the entry; every id-bearing line carries exactly one
id. The metadata line must stay id-free (`- source: the round-65 registry rows …`), because an
`S750–S775` range trips MULTI-ID and ONEID.

### M14 — environmental access recorded honestly (R64-M14)
```sh
grep -rhoE 'https?://[^ |;)]+' .ufo/waves/round-65/rows | sort -u | while read u; do
  printf '%s %s\n' "$(curl -s -o /dev/null --max-time 20 -w '%{http_code}' "$u")" "$u"
done
```
PASS: each row's live URL returns 200 **or** its `ACCESS` line records a challenge/transient
(403/429/000) as met-and-not-passed and routes to the archived same-page capture; the capture
itself must serve 200:
```sh
curl -sI --max-time 20 'https://web.archive.org/web/<timestamp>id_/<original>' | head -1
```
Never record 429/000 as absence; a `VERIFY: LOCATED` line against a challenge page is not
reproducible and must not be copied into the entry's provenance.

### M15 — tier and scope match the anchored evidence; teaches inside the word rule (R64-M15)
```sh
awk -F'|' '/^\| S7(5|6|7)/ {gsub(/ /,"",$2);gsub(/ /,"",$3);gsub(/ /,"",$4);print $2,$3,$4}' corpus/SOURCES.md | sort
```
PASS, per row: tier A ⇒ the quote is located on the primary URL actually served (M4 curl) or the
row is re-tiered; tier B ⇒ the `source` cell states the read-at-a-remove relation; `kind` ∈
{paper, book, docs, community} with Wikipedia rows as `docs` (`community` is the one-row S749
anomaly); the scope cell names no population or claim the quote does not carry; teaches ≤25 words
(**X5**).

### M16 — the locator label is true, not just the quote (R64-M16)
```sh
curl -sL --max-time 30 "$URL" | grep -Fic "<section title or paragraph label from the row>"
```
PASS: ≥1 for every row's locator string (PDFs via pypdf). A wrong section label is a provenance
defect even when the quote is verbatim elsewhere in the document.

### M17 — receipts are complete, all-legs, and not a killed run's fragment (R64-M17)
```sh
tail -2 reports/round-65/telemetry/final-measures-o.txt
grep -c 'SKIP' reports/round-65/telemetry/final-measures-o.txt      # 0
grep -c -- '--only' reports/round-65/telemetry/final-measures-o.txt # 0
wc -c reports/round-65/telemetry/final-measures-*.txt
```
PASS: the canonical receipt is an all-legs run (no `SKIP`, no `--only`), its verdict line matches
`exit=`, and its size is consistent with the declared leg count; a `--only` or aborted run is
never left at a canonical path (the round-64 1818-byte fragment).

### M18 — the revision's forcing control was run on the revision's own bytes (R64-M18)
```sh
python3 -W error::SyntaxWarning -m py_compile reports/round-65/accept-c.py reports/round-65/accept-o.py reports/round-65/accept-ca.py
timeout 1800 python3 -B reports/round-65/accept-c.py --root .
timeout 1800 python3 -B reports/round-65/accept-o.py --only MUT,FRAG,FULL,MUTEX | tail -5
```
PASS: byte set compiles warning-free (**today FAIL** on `accept-c.py:99`), and each new leg is
green on the same sha it will be cited at. A revision is not good because its diff reads right.

### M19 — the acceptance leg reads a ref the wave owns (R64-M19)
```sh
git rev-parse main
git diff --name-only 17c32302 main -- corpus/knowledge
```
PASS: `main` is the commit that carries the entry, and the diff is exactly
`corpus/knowledge/culture-material/games-play-sport-contests.md`. **Today: diff `[]`** — an
untracked draft at the corpus path cannot satisfy NOHARM; commit the land, then score.

---

## C. New checks derived from the model and the instruments

### X1 — no stale pre-data stamp survives in the entry
```sh
grep -niE 'skeleton|await|assembly time|0 of 26|placeholder|to-verify|unverified|todo|fixme|tbd|draft' "$E"
```
PASS: empty. The counter's MARK_RE only sees id-bearing lines, and `verified-at` carries no id, so
this check is reviewer-owned. The draft's line 5, line 8 (HTML comment) and line 82 currently
match — all three must be replaced with the post-land verified-at text.

### X2 — qualifiers and populations are preserved mechanically
Run after assembly (it reads the entry); before assembly it falls back to the row `BULLET` lines,
so it is never vacuous:
```sh
python3 - "$E" <<'EOF'
import glob,re,sys
Q=re.compile(r'"([^"]+)"|\u201c([^\u201c\u201d]+)\u201d')
LIM=re.compile(r'in this sample|immigrant|classroom|North American|Japanese|Lebanese|American|second-grade|urban parents|one sample',re.I)
clauses={}
try:
    for m in re.finditer(r'^-\s+(.*?)\s*\((S7[0-9]{2})\)\s*$',open(sys.argv[1]).read(),re.M):
        clauses[m.group(2)]=m.group(1)
except OSError:
    pass
for p in sorted(glob.glob('.ufo/waves/round-65/rows/**/row*.txt',recursive=True)):
    txt=open(p,encoding='utf-8').read()
    row=next((l for l in txt.splitlines() if re.match(r'\s*ROW\s*[:=]',l)),'')
    bul=next((l for l in txt.splitlines() if re.match(r'\s*BULLET\s*[:=]',l)),'')
    cs=[c.strip() for c in row.strip().split('|')[1:-1]]
    if len(cs)!=11: continue
    cl=clauses.get(cs[0]) or re.sub(r'^BULLET\s*[:=]\s*','',bul.strip())
    q=Q.search(cs[5]); q=q and (q.group(1) or q.group(2))
    for lim in set(LIM.findall(q or '')):
        if lim.lower() not in cl.lower():
            print(cs[0],'qualifier-dropped:',lim,'scope_has=',lim.lower() in cs[4].lower())
EOF
```
PASS: no output. Model failure this catches: S732 (model line 49 drops "immigrant households").

### X3 — row fragments use the label syntax the frozen FRAG leg parses
```sh
grep -rhoE '^(ROW|BULLET)[:=]' .ufo/waves/round-65/rows | sort | uniq -c
python3 -B tools/check-row-fragments.py
```
PASS: only `ROW=`/`BULLET=` counts; scan prints `FRAG: 0 finding(s) in 26 file(s)` and exit 0
(no `no-ROW`, no `teaches-length`, no `dup-url`). **Today the model format fails this** — 33/33
`no-ROW` on the round-64 rows and 33/33 on the round-64 directories. Decide pre-data: brief the
seats on `=`, or widen `LABEL_RE` with a control.

### X4 — the FRAG leg is non-vacuous (26 files, not 0)
```sh
timeout 180 python3 -B reports/round-65/accept-o.py --only FRAG | grep -E 'FRAG (PASS|FAIL)'
```
PASS: `FRAG PASS … files=26/26`. A `0 finding(s) in 0 file(s)` scan is a vacuity, not evidence
(the round-64 residual the rev2 count check now closes — keep it).

### X5 — teaches cells are inside the 25-word rule, not only 240 chars
```sh
python3 - <<'EOF'
import glob,re
for p in sorted(glob.glob('.ufo/waves/round-65/rows/**/row*.txt',recursive=True)):
    for ln in open(p,encoding='utf-8'):
        if re.match(r'\s*ROW\s*[:=]',ln):
            cs=[c.strip() for c in ln.strip().split('|')[1:-1]]
            if len(cs)==11 and len(cs[6].split())>25:
                print(cs[0],'teaches_words',len(cs[6].split()))
EOF
```
PASS: no output. `TEACHES_MAX=240` chars would allow ~35 words; this check enforces the lane's
stated 25-word cap.

### X6 — bullets pass the RESTATE predicates *and* an order-free teaches-reuse floor
```sh
python3 - <<'EOF'
import glob,re,unicodedata
STOP=set('a an and are as at be been but by for from has have he her his i if in into is it its of on or she so that the their them they this to was we were with you your not no nor'.split())
NON=re.compile(r'[\W_]+',re.U); W=re.compile(r'\w+',re.U)
def nw(t): return [x for x in NON.sub(' ',unicodedata.normalize('NFKC',t).casefold()).split() if x]
def cw(t): return [w for w in nw(t) if len(w)>=4 and w not in STOP and w.isalpha()]
def toks(t): return W.findall(unicodedata.normalize('NFKC',t).casefold())
def cov(a,b):
    pos=h=0
    for w in a:
        for j in range(pos,len(b)):
            if b[j]==w: pos=j+1; h+=1; break
    return h/len(a) if a else 0
Q=re.compile(r'"([^"]+)"|\u201c([^\u201c\u201d]+)\u201d')
for p in sorted(glob.glob('.ufo/waves/round-65/rows/**/row*.txt',recursive=True)):
    for ln in open(p,encoding='utf-8'):
        if re.match(r'\s*BULLET\s*[:=]',ln):
            cl=re.sub(r'^(BULLET\s*[:=]\s*-\s*)','',ln.strip())
            sid=re.search(r'\((S7[0-9]{2})\)\s*$',cl)
            if not sid: print(p,'shape'); continue
            cl=re.sub(r'\s*\(S7[0-9]{2}\)\s*$','',cl)
            row=None
            for p2 in sorted(glob.glob('.ufo/waves/round-65/rows/**/row*.txt',recursive=True)):
                for l2 in open(p2,encoding='utf-8'):
                    if re.match(r'\s*ROW\s*[:=]',l2):
                        cs=[c.strip() for c in l2.strip().split('|')[1:-1]]
                        if len(cs)==11 and cs[0]==sid.group(1): row=cs
            if not row: continue
            q=Q.search(row[5]); q=q and (q.group(1) or q.group(2))
            c=cw(cl); 
            if len(c)<5: print(sid.group(1),'content<5')
            hits=cov(c,nw(q or ''))*len(c)
            if hits<3: print(sid.group(1),'in_order',round(hits,2))
            tc=cw(row[6]); 
            if tc and (cov(toks(cl),toks(row[6]))>=0.8 or cov(c,tc)>=0.8 or cov(tc,c)>=0.8):
                print(sid.group(1),'teaches_reuse')
EOF
```
PASS: no output. The third clause is the order-free floor: the frozen rule only catches in-order
reuse (`cov=0.533` for a shuffled teaches copy — measured with the counter's own functions), so a
row bullet that reuses the teaches cell's content in a different order must be caught here, before
the assembled entry inherits it (entry bullets are verbatim row `BULLET` lines).

### X7 — the frontier is restated with word boundaries
```sh
git ls-tree -r --name-only 17c32302 -- corpus/knowledge | grep -ciwE 'game|play|sport|contest|toy|mancala'
git ls-tree -r --name-only 17c32302 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'
```
PASS: the first prints 0 (and is the variant the report quotes); the second prints 2 —
`sumptuary-law-rank-display.md`, `transport-mobility-lexicon.md` — so it must never be cited as 0.

### X8 — heading and punctuation consistency with the model
```sh
grep -c '^## ' "$E"
grep -cE '^## [0-9]+\. ' "$E"
grep -E '^- .*\(S7[0-9]{2}\)$' "$E" | grep -vc '\.$'
```
PASS: the first two counts are equal (every H2 numbered — the model has 10/10); the third prints 0
(every bullet ends with a period — the model currently has 10 offenders). This is style, but an
entry that mixes both forms is visibly unfinished next to the model.

### X9 — no internal review vocabulary leaks into the entry
```sh
grep -niE 'one-way pointing|calibration|assembly time|0 of 26|tier A marks|review_only|gap list' "$E"
python3 -c "
import json
d=json.load(open('reports/round-65/claims.json'))
text=open('corpus/knowledge/culture-material/games-play-sport-contests.md').read()
for s in d.get('review_only_global',[])+[x for c in d['claims'] for x in c.get('review_only',[])]:
    if s.split('(')[0].strip().lower()[:40] in text.lower(): print('LEAK',s[:60])
"
```
PASS: empty. The draft currently has `## calibration`, `## one-way pointing to partial owners`,
and "no supporting row had landed at assembly time" — the first two are review-only phrases from
`claims.json`, the third is an assembly stamp (**X1**).

---

## D. Dependencies absent at review time (recorded, not waited on)

- `.ufo/waves/round-65/rows/` holds **0** row fragments (`assemble-audit.json`:
  `landed_count 0`, `missing` = S750-S775). No bullet, RESTATE, tier, or live-location check can
  be scored yet.
- The draft `.ufo/waves/round-65/stage/entry-draft.md` exists (104 lines, 1 H1, 14 H2, 0 H3,
  `- topic:` present, 0 cited ids); the corpus-path land does not.
- `corpus/lessons/round-65.md` does not exist yet (claim Ca land).
- `reports/round-65/telemetry/controls-ca.txt` does not exist yet; `controls-o.txt` exists
  (01:53) but `controls-c.txt` lacks the near-copy forcing evidence (**F3**).
- `reports/round-65/accept-o.py` changed under review (the FRAG block moved from no count check to
  `files == 26` at lines 1232-1241) — re-read the bytes before citing leg line numbers.
- The round-65 entry cannot be scored end-to-end until it exists at
  `corpus/knowledge/culture-material/games-play-sport-contests.md` on a ref named `main`
  (**M19**); stage it in a scratch root only to exercise individual legs, never as acceptance.

## E. Residual risk and verification gaps

1. **Review-only surfaces not mechanised here.** Topic fit, per-sentence support, and the lore
   handoff remain blind judgments (the counter's own docstring says so). My X2/X9 catch the model's
   known failure shapes (population drop, invented outcome, process vocabulary), not semantic
   overreach in new prose.
2. **RESTATE coverage is asymmetric.** The rev1 rule is order-sensitive (F8); the draft's bullets
   come from row `BULLET` lines, so X6 must pass **before** assembly or the entry inherits a
   failure that no pre-land check will see. X6 is my emulation of the leg, not the leg.
3. **FRAG format coupling (F1)** is the highest-risk item: if it is discovered after rows land,
   the choice is between reshaping 26 build artifacts and revising a frozen counter. Decide
   pre-data.
4. **Committed-bytes binding (F2/M19)** cannot be closed by any reviewer; only the L1's commit
   path closes it. Every receipt produced before that commit is a worktree measurement and must
   say so (the round-64 convention).
5. **Sample of one model.** The round-64 entry is the only same-shape precedent; its own shipped
   defects (lines 5, 18, 49) are the reason X1/X2 exist, and they should be dispositioned by the
   Ca/R-record path if not already covered.

Report: .ufo/waves/round-65/w1/RevEntryDraft.md
