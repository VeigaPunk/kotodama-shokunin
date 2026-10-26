# ExecCensusEnd — round 74 W2 falsification: frontier census and registry

Seat: `ExecCensusEnd` (leaf; no dispatch, no background jobs, no counter edits).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (all reads absolute; writes only
this report and `/tmp/ExecCensusEnd/`).
Revisions: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands
`c4bf61a8d722f9168ce0fd8021a6261c000610c5`; claim Ca lands
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; lane main observed at dispatch
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236`.
Claims read before attacking at `reports/round-74/claims.json`, then verified byte-identical to
the frozen blob `git show 00c408a:reports/round-74/claims.json` (both sha256
`270e31790e2932c8d418904e16e721a6ae5343e4e2c157e5409c1c27dfdeca19`); the CENSUS leg text and
the frozen counter were read from that frozen blob. Census script: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`.

## Verdict

**The census-state attack FAILED — the claim survived.** At main, the registry is exactly the
base registry plus the four predicted rows (S881, S882, S883, S884) and the single predicted
in-place S877 `used-by` edit; every manual census invariant holds; the validator exits 0 with
0 E-codes. All histograms move exactly as the assignment predicted.

One defect was found **in the check text, not in the landed data**: the frozen CENSUS leg's
independent E-code scan (`^E[0-9][0-9]`) can never match the validator's TSV line format, so
that clause is dead (F1). The leg still fails on real E output through the script's exit code,
which I proved with a planted control — so no false PASS occurred here.

One new-at-main **signal** is reported for completeness (F2): three new `W01` warnings on the
tier-C rows. They are disclosed in the lesson and the `census-end` receipt and are
status-neutral by contract; the assignment's own predicted row set implies them.

## Findings

### F1 — MEDIUM — CENSUS leg's E-code clause is vacuous against the script's TSV

**What it attacks:** claim C leg `CENSUS`, frozen text:
`… exits 0 … with no output line matching ^E[0-9][0-9] in the TSV`.

**Evidence (exact).** The frozen counter implements the clause as a line-start scan:

```
$ git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/accept-c.py | grep -n '\^E'
1463:    errs = re.findall(r"^E[0-9][0-9]", r.stdout, re.M)
$ sha256sum reports/round-74/accept-c.py
8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a
```

But every line the validator emits begins with the lane id, not with the code
(`lane<TAB>code<TAB>value`). Raw output from the landed main registry:

```
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

Planted control (malformed row inserted inside `## Registry`, file served to `validate --file`):

```
$ bash -c '/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
    --file /tmp/ExecCensusEnd/planted2/kotodama/corpus/SOURCES.md --today 2026-10-25 \
    > /tmp/ExecCensusEnd/planted2-out.txt 2>&1; echo $? > /tmp/ExecCensusEnd/planted2-rc.txt'
$ cat /tmp/ExecCensusEnd/planted2-rc.txt
1
$ grep -E '	E01	' /tmp/ExecCensusEnd/planted2-out.txt
file	E01	S999 fields=3
$ python3 - <<'PY'
import re
s=open('/tmp/ExecCensusEnd/planted2-out.txt').read()
print('claim regex ^E[0-9][0-9] matches:', re.findall(r'^E[0-9][0-9]', s, re.M))
print('column regex \\tE[0-9]{2}\\t matches:', sorted(set(re.findall(r'\t(E[0-9]{2})\t', s)))[:5])
PY
claim regex ^E[0-9][0-9] matches: []
column regex \tE[0-9]{2}\t matches: ['E01', 'E11']
```

The script exits 1 on any E code (`[ "$findings" = 1 ] && exit 1`, tail of
`sources-census.sh`), so the leg is not currently unsound. The defect is that the leg's
*second, independent* assertion is dead: E detection rests entirely on an **unpinned** script's
exit status (the script lives under the fleet root, not in the frozen commit), and the clause
as written would keep "passing" if a script emitted E lines with exit 0. This is the
self-attestation/survivor class the round claims to harden.

**Proposed fix:** in `accept-c.py` (a new freeze, since the claim is frozen), replace
`r"^E[0-9][0-9]"` with `r"\tE[0-9]{2}\t"` (or `r"^\S+\tE[0-9]{2}\t"`) and state the leg
clause as "the TSV carries no `\tE\d\d\t` line". Keep the exit-code check; optionally pin the
census script's sha256 in the frozen claims/counter so the exit-code contract is also frozen.

**Impact on this round:** none to the data — independent manual censuses at base and main
(below) found no E-class defect, and the accept-c rerun passed CENSUS with exit 0.

### F2 — LOW — three new-at-main `W01` warnings (tier-C mined with non-`—` used-by)

**What it attacks:** "report any census finding that is new at main".

**Evidence (exact lines, main `1d7add3` / lands `c4bf61a`):**

```
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
```

Base `f7104cb` emits `W01 = 0`; main emits `W01 = 3`. `W04 = 28` at both. There is **no** new
`E` code and no new `W02`/`W03`.

**Assessment:** not a claim failure. `W01` is the contract's advisory for a tier-C row that is
mined *and* used (`SOURCES-CONTRACT-v1: tier C = lead only, never sole support`); warnings do
not change the validator's exit status, and the claim's CENSUS leg only requires exit 0 plus
no E. The rows' own scope cells declare the C pages non-sole and paired, and the assignment's
predicted row set (`S881 S882 S884 tier C community mined`) entails exactly these warnings.
The lesson discloses them (`corpus/lessons/round-74.md:183`, "W01 ×3 … are status-neutral") and
the committed receipt carries the same three lines. Reported as a signal, not a censure; no
fix proposed (changing tier or status to silence the warning would corrupt honest curation).

## Attack-failed evidence (claim survived)

### 1. Census command, fleet root, at main (literal assignment command)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama \
    > /tmp/ExecCensusEnd-main-validate.tsv 2>/tmp/ExecCensusEnd-main-validate.err
$ echo "exit=$?"
exit=0
$ tail -1 /tmp/ExecCensusEnd-main-validate.tsv
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
$ grep -cE '^kotodama	W[0-9]' /tmp/ExecCensusEnd-main-validate.tsv
31
$ grep -cE '^kotodama	E[0-9]' /tmp/ExecCensusEnd-main-validate.tsv
0
$ awk -F'\t' '{print $2}' /tmp/ExecCensusEnd-main-validate.tsv | sort | uniq -c
      1 ok
      3 W01
     28 W04
```

Because the lane worktree registry is byte-identical to the clone's lands registry
(`sha256 c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614` both), the
fleet-root run grades the lands bytes. `W/E counts = 31/0`; last line as above; exit 0.

### 2. Fresh clone and materialized-fleet runs (own clone, per the counter constraint)

```
$ D=$(mktemp -d) && git -C "$D" init -q && T=$(git -C "$D" rev-parse --show-toplevel) \
    && [ "$T" = "$D" ] && echo "toplevel-ok:$T"
toplevel-ok:/tmp/tmp.NRTO7VPJfr
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/ExecCensusEnd/lane
$ git -C /tmp/ExecCensusEnd/lane log --oneline -1
1d7add3 round-74: junk-landing receipts, measured receipts at each claim's own landing, wave-2 builder
# synthetic materialized fleet: mkdir fleet; ln -s lane fleet/kotodama-shokunin;
#   printf 'LANES="\nkotodama|kotodama-shokunin|round-74 materialized lands tree\n"\n' > fleet/shokunin.conf
```

| revision | rows | exit | W | E | last line |
|---|---|---|---|---|---|
| base `f7104cb` | 804 | 0 | 28 (all W04) | 0 | `kotodama ok …/corpus/SOURCES.md` |
| lands C `c4bf61a` | 808 | 0 | 31 (28 W04 + 3 W01) | 0 | `kotodama ok …/corpus/SOURCES.md` |
| freeze `00c408a` | 804 | 0 | 28 | 0 | `kotodama ok …/corpus/SOURCES.md` |
| Ca lands `5e4796c` | 804 | 0 | 28 | 0 | `kotodama ok …/corpus/SOURCES.md` |
| lane main `1d7add3` | 808 | 0 | 31 | 0 | `kotodama ok …/corpus/SOURCES.md` |

`--today`: the clone runs used `--today 2026-10-25`; the fleet-root run used the script default
(`date -u +%F` = `2026-10-26` at run time, local date 2026-10-25). Both exit 0: the only
date-sensitive check is E08 (`opened` not in the future), and `opened = 2026-10-25` is not after
either date.

The CENSUS leg's own acceptance path was re-executed in the clone (local `main` forced to the
lands, as the counter requires):

```
$ git -C /tmp/ExecCensusEnd/lane checkout --detach c4bf61a8d722…
$ git -C /tmp/ExecCensusEnd/lane branch -f main c4bf61a8d722…
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722… \
    --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin | tail -1
ACCEPT-C-74: PASS legs=13/13
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r74-fleet-…/kotodama-shokunin/corpus/SOURCES.md
```

(`accept-ca.py` was not run: it has no CENSUS leg, so it cannot inform this attack; this report
makes no claim about it.)

### 3. CORPUS.md manual census, base vs main (histogram diff as predicted)

Run from each materialized lane root (base = clone at `f7104cb`; main = both the real lane root
and the clone at `1d7add3`, outputs identical — `MAIN-MANUAL-IDENTICAL`).

```
########## base f7104cb
rows: 804
malformed: 0
tiers: A=488 B=304 C=12
status: mined=709 queued=58 rejected=37
dup ids:
enum violations:
missing used-by:

########## main 1d7add3
rows: 808
malformed: 0
tiers: A=488 B=305 C=15
status: mined=713 queued=58 rejected=37
dup ids:
enum violations:
missing used-by:
```

Delta: `+4` rows; tier `B +1`, `C +3` (A unchanged); status `mined +4` (queued/rejected
unchanged). This is exactly the permitted set: S881/S882/S884 tier C community mined, S883
tier B docs mined. Malformed rows (`NF!=13`) = 0; duplicate ids = none; enum violations = none
(tier/status/kind; no community-at-A); mined rows with missing `used-by` paths = none — at both
revisions, from both the real tree and the clone.

### 4. Registry diff shape (nothing else moved)

```
$ git diff --stat f7104cb..main -- corpus/SOURCES.md
 corpus/SOURCES.md | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)
```

Pipe-split cell diff, base vs main:

- added ids exactly `['S881', 'S882', 'S883', 'S884']` (contiguous after S880); removed: none;
- changed lines: `['S877']` only; differing pipe-index: `[11]` only, i.e.
  `base: corpus/knowledge/linguistics/conlang-scholarship.md`
  `main: corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`
  (base value plus exactly the new base-entry path; all other S877 cells byte-identical);
- every other row byte-identical; registry sha `c8da0a5a…5614` is identical at `c4bf61a` and
  `1d7add3`; base/freeze/Ca-lands registry sha `93d60464…8774` (Ca does not touch the registry).

### 5. New-row cell checks (assignment item)

For each of S881–S884 at main: pipe-split `NF = 13` ⇒ **11 cells**; inner `|` count **0**;
`opened = 2026-10-25` (ISO, equals the frozen access date, not future); `recheck = 180d`
(cadence-only); `status = mined`; every cell non-empty; `| S88x | … |` line ends ` |`.

| id | kind | tier | scope cell opens | anchor quote (verbatim) | used-by |
|---|---|---|---|---|---|
| S881 | community | C | Tier C: Japanese writing-app vendor blog… | `「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。」` | base entry |
| S882 | community | C | Japanese web-fiction editorial-service… | `「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」` + settings-note item | base entry |
| S883 | docs | B | one author's self-reported order… | `"整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。"` | amend entry |
| S884 | community | C | one web-fiction author's own tolerance rule… | `「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」` | amend entry |

All four `used-by` targets exist on disk at main (no `E11`; manual missing-path scan empty).
Every `source:` cell carries the mapped URL verbatim; S883/S884 also carry the archive URL in
the same cell (no pipe). The entries' source lines match the cells exactly: the base entry
cites S877 + S881 + S882, the amendment cites S883 + S884, so `used-by` is exact.

### 6. Stronger URL-duplication scan (beyond the script's first-URL check)

All http(s) URLs in every registry source cell were normalized (scheme dropped, host
lowercased, `www.` stripped, trailing `/`/`#` stripped, `web.archive.org/web/<ts>id_/<url>`
unwrapped to the inner URL) and grouped. 808 rows / 1020 raw URLs / 854 normalized keys:
**no normalized URL is shared by a new row and any other row**; S883/S884's archive URLs unwrap
to exactly the direct URLs named in the same cell. The 50 shared normalized keys all involve
pre-existing rows (the registry is byte-identical except the appended rows and S877's used-by
cell), and the 28 `W04` lines are the script's narrower first-URL/scope view of that overlap;
none is touched or added by this round.

### 7. Receipts reproduce

- `reports/round-74/telemetry/census-start.txt`: W04 28, W01 0, E 0, `exit=0`, 804 rows —
  reproduced at base (W lines identical after normalizing the lane name/path; only W04 present).
- `reports/round-74/telemetry/census-end.txt`: W04 28, W01 3, E 0, `exit=0`, 808 rows — all
  W lines reproduce exactly at main (`diff` of W lines empty after normalizing the lane name).
- `gap-sweep.txt` facts re-derived at base: registry 804 / last id S880 / 0 host fragments
  (litmemo.com, tuduku.space, chinawriter.com.cn) / 0 CJK-term knowledge files / 247
  knowledge `.md` files. At main: 808 / last id S884 / 4 fragment rows / 2 CJK-hit files /
  249 files. (The lesson's scratch-mirror `804a805,808` refers to the mirror's own row
  numbering, not the real registry lines 836–839.)

## New at main (state delta, no undisclosed state defect)

| metric | base `f7104cb` | main `1d7add3` |
|---|---|---|
| registry rows | 804 | 808 |
| last id | S880 | S884 |
| tier A / B / C | 488 / 304 / 12 | 488 / 305 / 15 |
| status queued / mined / rejected | 58 / 709 / 37 | 58 / 713 / 37 |
| malformed (`NF!=13`) | 0 | 0 |
| duplicate ids / enum violations / missing used-by | none / none / none | none / none / none |
| validator exit | 0 | 0 |
| E codes | 0 | 0 |
| W01 / W04 | 0 / 28 | 3 / 28 |
| last line | `… ok …/corpus/SOURCES.md` | `… ok …/corpus/SOURCES.md` |

The only census findings new at main are the three `W01` lines in F2 (disclosed, status-neutral)
and the counts above. No new E code, no malformed row, no id reuse, no stale registry count in
`corpus/`/`SKILL.md` (the only "804 rows" strings are the entries' correctly base-pinned ground
statements; README's smaller-number registry histories are historical round notes).

## Residual observations (not scored as findings)

- **accept-c materialization flake.** First clone run printed
  `# materialized: git archive of c4bf61a8d722 (the clone refused the revision)`; an immediate
  rerun printed
  `# materialized: git clone of /tmp/ExecCensusEnd/lane, checkout --detach c4bf61a8d722 …`.
  Both runs PASSed CENSUS with `exit=0` and the same last line, and `git archive <lands>` is
  byte-identical to the checkout, so the graded registry is unaffected. The clone fallback
  swallows its stderr, so a transient refusal is not diagnosable from the receipt; a future
  counter change could record the refusal text.
- **W01 is advisory by design.** It fires on any tier-C row with `used-by != —`; it cannot
  express the contract's real condition ("never sole support"), so it is expected on honestly
  tiered practitioner rows and should not be "cleared".

## Hygiene

- No network fetch was performed by this seat, so no User-Agent was sent and no UA is recorded;
  no "unreachable"/"no capture" ruling was made, so no CDX probe was needed. All checks are
  offline against committed bytes, local git objects, and local files.
- No tool was installed or upgraded (nothing needed; pacman not used).
- No write outside `/tmp/ExecCensusEnd/**` (clone, synthetic fleets, receipts) and this report.

## Files changed

- `.ufo/waves/round-74/w2/ExecCensusEnd.md` (this report) — the only lane-tree write.
