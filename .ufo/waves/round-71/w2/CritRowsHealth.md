# CritRowsHealth — round-71 wave-2 critic: registry census health after S861–S873

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only; this file is the only write).
Measured revision: `ccadb5989bc33b230dfd496441ddafefa1ab4b73` (HEAD, working tree clean for
`corpus/SOURCES.md` and the new entry — `git status --porcelain` empty for both).
Frozen command source: `/home/vgpnk/Projects/shokunin/CORPUS.md:131-147` (§Census, "run from the lane root").

## Verdict

**7/7 frozen census commands PASS at HEAD with 0 findings.** The claim holds. It holds for a
narrower property than the round's prose implies — see Findings 1–3, which the seven commands
structurally cannot see. None of them changes the row count, the histograms, or the receipt
result; Finding 2 is a live receipt defect at HEAD and has a one-command fix.

## 1. The seven commands, re-run verbatim from the lane root

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
```
`797`

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
```
`0`

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
```
`A=486 B=299 C=12 ` → sum **797** ✓

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
```
`mined=702 queued=58 rejected=37 ` → sum **797** ✓

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
```
(empty) ✓

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
```
(empty) ✓

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```
(empty) ✓

Maintained validator (`sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`):
exit `0`, `28` W04 records, final line `kotodama ok …/corpus/SOURCES.md`. 28 = the round-71
baseline count (w1 `ScoutCensusBaseline.md`), i.e. **no new duplicate-URL warning from the 13 rows**.

## 2. Delta attribution — the census was also run at the declaration revision

Base `b94a543c70f40dba7e49fff96d05bfb8bbd8c678` (declared in `reports/round-71/claims.json`),
extracted to `/tmp/base-SOURCES.md` and fed to the same seven commands from the lane root:

```text
rows 784 | malformed 0 | A=474 B=298 C=12 | mined=689 queued=58 rejected=37 | dup empty | enum empty | usedby empty
```

784 → 797 = +13 exactly; histograms move A +12, B +1, mined +13 (S861–S872 `A`, S873 `B`, all
`mined`). The delta is fully attributed to S861–S873 and nothing else **in count terms**.

## 3. Non-vacuity — mutation test (all seven commands fire)

Copy of HEAD `SOURCES.md` in `/tmp/census-mut` with six injected defects (dup id `S873`;
`NF=12` row `S900`; `kind=widget`; `tier=D`; `status=pending`; `A`+`community`):

```text
C2 malformed -> 1        (S900)
C3 tier      -> A=491 B=299 C=12 D=1
C4 status    -> mined=707 pending=1 queued=58 rejected=37
C5 dup       -> S873
C6 enum      -> kind S901 widget | tier S902 D | status S903 pending | tier-inflation S904
C7 usedby    -> missing: nope/missing-file.md  (+ corpus/knowledge/x.md x3)
```

Clean control (`/tmp/census-mut2`, knowledge/lessons symlinked to the real tree): C7 prints
nothing; appending one row with `used-by=corpus/knowledge/nope.md` prints exactly
`missing: corpus/knowledge/nope.md`. C7 is live and precise, not vacuous.

## Finding 1 — MEDIUM: the frozen census cannot see section placement; this round had a live false negative

`498db73` ("claim C data lands — dance register entry + 13 mined rows S861-S873") placed the 13
rows **after `## Leads (unopened)` at line 913**, i.e. outside the `## Registry` table
(`| id | source | …` header at line 28). Re-running the frozen commands on that blob:

```sh
git show 498db73:corpus/SOURCES.md > /tmp/mid-SOURCES.md
# rows 797 | malformed 0 | dup empty | usedby empty | enum: tier-inflation S870 (kind=community)
```

Six of seven commands returned clean and the row count was even "correct" (797) with the rows in
the wrong section. Only the enum command fired, and only on S870's `community`+`A` combination —
not on placement. The placement defect was fixed in `8c203bd` ("rows inside Registry section,
S870 kind docs"), i.e. **by a check other than the census**. At HEAD placement is correct:

```sh
grep -nE '^## ' corpus/SOURCES.md      # Registry 26 | Paths 829 | Search log 864 | Leads 876
awk 'f && /^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/{n++} /^## Paths/{f=1} END{print n+0}' corpus/SOURCES.md
# 0
```

Impacted axis: evidence validity of the "census exit 0" claim — it certifies row *shape*, not row
*address*. The census is frozen, so the correction belongs in the round lesson, not in the frozen
bytes: record the section-bound check next to the census block, e.g.
`awk` over the span from the `| id |` header to the next `^## ` and require its row count to equal
the census row count. (HEAD: 797 = 797.)

## Finding 2 — MEDIUM (live at HEAD): `census-end.txt` is a doubled capture

```sh
wc -l reports/round-71/telemetry/census-end.txt            # 59
grep -c W04 reports/round-71/telemetry/census-end.txt      # 56
grep W04 reports/round-71/telemetry/census-end.txt | sort -u | wc -l   # 28
sed -n '30,58p' …/census-end.txt | diff - /tmp/val-out.txt  # identical to a fresh run
sed -n '1,29p' …/census-end.txt | diff - <(sed -n '30,58p' …)  # identical (duplicate block)
```

Lines 1–29 are a first capture (28 W04 + `ok`, no exit line); lines 30–58 are the same run again;
line 59 is `CENSUS_EXIT=0`. `census-start.txt` is a clean single capture (30 lines). The lesson's
statement "census exit 0 at end (`census-end.txt`, W04=28 standing)" is true of the *run* but not
of the *receipt*: `grep -c W04` on the receipt yields 56, so the next verifier reading the receipt
by count gets a contradiction. Smallest safe correction: keep lines 30–59 (the copy carrying
`CENSUS_EXIT=0`) and drop lines 1–29, so the receipt is one run.

## Finding 3 — INFO: "0 findings" certifies existence, not append-only, and not used-by shape

`git diff --numstat b94a543…..HEAD -- corpus/SOURCES.md` → `14  1` (14 added, 1 removed), and the
added ids include **S860**. Field diff of the S860 row, base vs HEAD:

```text
FIELD 6 (anchor):
  OLD: … file blob 6a314e9c… at lane revision 6cb51a447043a9691c59794d7479c1a81c0626a4
  NEW: … file blob 6a314e9c… at lane revision acc2d614a097484d8dc41230229dc4ead07d8a19
```

This is an in-place rewrite of a pre-existing (round-70) row's `anchor` column — not one of the
three columns (`status`, `recheck`, `used-by`) the SOURCES.md append-only rule permits in place.
It **is** declared and logged (claims.json Ca surface V70-2; `corpus/lessons/round-71.md`, the
corrections row reading "S860 verify-at old `6cb51a4` → new `acc2d614` (logged in
corrections-r70.md)" — cited by content because the lesson is under concurrent wave-2 edit and its
line numbers moved from 57-58 to 63-64 between my two reads; `reports/round-71/corrections-r70.md:10`),
so it is not an undeclared violation. The critic-relevant consequence stands: the seven commands would pass an
*unlogged* anchor rewrite identically, and "784 → 797" is therefore not a pure append. Two further
shape properties the seven commands do not test, with live instances:

- `used-by` shape: rows **S859/S860** list `SKILL.md`, which exists, so C7 passes — but the
  SOURCES.md shape rule says `used-by` is "repo-relative paths of the knowledge entries or
  lessons citing the row". Existence ≠ shape.
- C1 is column-zero while the maintained parser accepts 0–3 leading spaces. Today
  `grep -cE '^ {1,3}\|…'` = `0`, so C1 (797) equals the spacing-tolerant count (797); an appended
  row indented 1–3 spaces would be invisible to **all seven** commands.

## 4. Append integrity that does hold (bidirectional, checked)

- All 13 ids appear in `corpus/knowledge/culture-material/dance-performance-movement-codes.md`
  (`S861`…`S873`, count ≥1 each); provenance trio present (`- source:` ×13, `- verified-at:`,
  `- recheck:`); file is git-tracked.
- All 13 rows point at that one existing entry (13/13 distinct `used-by` values = 1 path).
- All 13 ids have exactly one `| S86x |` Gate row in `corpus/lessons/round-71.md`.
- No new duplicate URL: 28 W04 before (w1 baseline) and 28 after; the 7 UNESCO element slugs each
  occur once in the registry.
- Tier/kind mix of the new rows (`docs`×11, `spec`×2; A×12, B×1) is not distributionally anomalous:
  registry `docs|A` = 223 rows before this append. QUALITY.md:29 (abstracts/descriptions → B) does
  not obviously bite institution-primary documentation; S870 (ICKL homepage) is the most
  borderline A and belongs to RevRows/RevEntry, not to census health.

## Impacted axes

| Axis | Effect |
|---|---|
| registry shape (rows/malformed/enum/dup) | intact, 7/7 clean at HEAD, mutation-proven live |
| census evidence validity | weakened by Finding 1 (placement-blind) — lesson should say so |
| receipt fidelity | Finding 2 is a live defect in `census-end.txt` |
| append-only provenance | Finding 3: one declared in-place anchor repoint; census cannot certify it |
| claim C coverage | unaffected (counts and citations reconcile) |

## Smallest safe corrections (in priority order)

1. `reports/round-71/telemetry/census-end.txt`: drop lines 1–29 (keep the capture that ends
   `CENSUS_EXIT=0`). One command, no claim byte touched.
2. `corpus/lessons/round-71.md`, census paragraph: add the section-bound leg (row count between the
   `| id |` header and the next `^## ` must equal the census row count) and note that the frozen
   census is placement-blind — evidenced by `498db73`.
3. Optional, next round: extend C7 (or a new row-shape check) to require `used-by` targets under
   `corpus/knowledge/` or `corpus/lessons/`, and to make C1 spacing-tolerant to match the
   maintained parser.

Tooling: nothing installed or updated. No lane file other than this report was written; scratch
copies live under `/tmp/census-mut*` and `/tmp/{base,mid}-SOURCES.md`.
