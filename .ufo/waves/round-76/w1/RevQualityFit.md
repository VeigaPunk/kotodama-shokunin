# RevQualityFit — wave 1: the QUALITY.md bar against the round-76 DRAFT claims

Seat RevQualityFit (leaf; no dispatch, no installs). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `98c486bdb4650ba5b8e651d332910e8ee60ad121` (all base reads via `git -C <lane> show 98c486bdb465…:<path>`).
Attack target: `.ufo/waves/round-76/CLAIMS-DRAFT.md` (read 2026-10-27; never edited by this seat) against
`corpus/QUALITY.md` criteria 1–28 + criterion-23 addendum. QUALITY line cites: c1 :5, c2 :9, c3 :13, c4 :16,
c5 :18, tier preamble :22-24, c6 :29, c7 :31, c8 :33, c9 :35, c10 :37, c11 :39, c12 :41, c13 :43, c14 :45,
c15 :47, c16 :49, c17 :55, c18 :57, c19 :59, c20 :61, c21 :63, c22 :66-74, c23 :77, c24 :79, c25 :81-123,
c26 :125, c27 :127-148, c28 :150-162, addendum :164-197. Scratch `/fast/scratch/hyaku/kotodama-r76/RevQualityFit`
(deleted at yield; receipts copied to `.ufo/waves/round-76/w1/stage/RevQualityFit/`). No tool installed; no
pacman; no lane/repo mutation; staged package read-only under `/home/vgpnk/Projects/shokuknow` (READ-ONLY).

**Verdict: the DRAFT is attackable on five fronts before data** — (F1) both Before greps are false as declared;
(F2) the re-point plan misses six campaign ids the staged entries cite, two of which have no target row at all,
so the draft's own kill rule fires and its k-arithmetic contradicts its S894–S898 row plan; (F3) showGb and
newGbInfo are one document (302 alias, measured), so two planned rows S896+S897 violate one-row-per-document;
(F4) candidate a fails QUALITY 15's lint as staged (exit 1, MULTI-ID ×3); (F5) candidate d's only source is a
tier-C row, which the draft's own after-state forbids as sole support, and that page has zero Wayback captures.
The draft's numbers that DO re-derive: 817 rows, 252 files, last id S893, 35 collisions S859–S893,
`considerthese` absent.

---

## Findings (by severity)

### F1 — CRITICAL (c8 :33, c9 :35, c11 :39, c13 :43) — the Before greps are false as declared

DRAFT (Claim C, declared after-state): "`git grep -l -E 'GB/T 33661' 98c486b -- corpus` and
`git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` each print nothing (exit 1)."

Measured (this seat, 2026-10-27):
```
$ git -C $L grep -l -E 'GB/T 33661' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/lessons/round-68.md
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/lessons/round-69.md     (exit 0, not 1)
$ git -C $L grep -l -E 'digital\.archives\.go\.jp' 98c486b… -- corpus
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/lessons/round-68.md     (exit 0, not 1)
```
Hits: `corpus/lessons/round-68.md:111` ("S776 (openstd.samr.gov.cn GB/T 33661-2017 page, HTTP 200)"),
`round-69.md:39,111`. Scoped sweep, which is what the claim's ground actually needs:
```
$ git -C $L grep -n -E 'GB/T 33661|openstd|gmw\.cn|xingzuobaike|digital\.archives\.go\.jp' 98c486b… -- corpus/knowledge corpus/SOURCES.md
(no output)  exit=1
```
So the "ground the lane does not hold" is TRUE over `corpus/knowledge` + `corpus/SOURCES.md` and FALSE over
`-- corpus`. Consequence: any counter leg or dry-run receipt that runs the declared argv verbatim (c9's two-way
check) goes red at the freeze for a reason the claim did not anticipate — the honest-stop kills the round on a
scoping typo. Fix before freeze: rescope both greps to `-- corpus/knowledge corpus/SOURCES.md` (or exclude
lessons explicitly and name the two lesson hits in the claim text).

### F2 — CRITICAL (kill rule; c7 :31 REPOINTED class; c11 :39) — six campaign ids cited by the staged entries are outside the re-point plan; two have no target row

The DRAFT's re-point plan covers exactly: S937→S898, S935→(S894 capture), S932→S896, S938→S897, S908→S894,
S916→S895, S919→S892, S921→S885. The four staged entries additionally cite:

| id | where (staged file:line) | what the prose means | lane row at base 98c486b | document match |
|---|---|---|---|---|
| S777 | `…amend-2026-10-24.md:15` | "the drafter's interpretation PDF was already held (S777)" | **no row exists** (`git show $B:corpus/SOURCES.md \| grep -c S777` → `0`) | — |
| S750 | `…amend-2026-10-24.md:86` | "the official registry record (S750)" | `S718? no —` lane S750 = Stewart Culin, *Games of the North American Indians* (1907) | NO |
| S807 | `…amend-2026-10-24.md:65,90` | "a third-party reproduction (S807)" of the standard | lane S807 = Li 2021, median artery / meridians (J Anat) | NO |
| S718 | `…amend-2026-10-23c.md:15` | "the standard's registry record (S718)" | lane S718 = Farran et al. 2016, infant-directed speech (PLOS ONE) | NO |
| S719 | `…amend-2026-10-23c.md:7,14` | "the drafter's interpretation (S719)" | lane S719 = Cristia 2013, infant-directed speech | NO |
| S757 | `…era-periodization-models.amend-2026-10-23b.md:7` | "the library's classification (round 4's S757)" | lane S757 = Huizinga, *Homo Ludens* | NO |

S-id inventory commands: `grep -noE 'S[0-9]{3}' <staged file>` (full listing in
`stage/RevQualityFit/receipts.txt`); row lookups `git -C $L show $B:corpus/SOURCES.md \| grep -E '^\| *(S718\|S719\|S750\|S757\|S777\|S807) '`.

Consequences, each mechanical:
1. The kill rule "a cited campaign-namespace id → fails as declared" fires on every one of the six left
   as-is. The draft's DRAFT-note "(+S757 coupling only)" and "(S718/S719 coupling only)" treat them as if
   they were lane ids; they are campaign ids whose lane twins name different documents — citing them is the
   R75 `used-by`/`S899` mispairing class, worse because a reader who resolves lane S750 lands on Culin's
   games monograph.
2. S777, S719, S757 name documents (drafter's interpretation PDF; library classification source) the draft
   plans **no row for**, so "k = number of distinct documents cited by the admitted entries that the registry
   did not hold" counts them (k ≥ 8 if a–d all land: archives, newGbInfo, gmw, xingzuobaike, drafter PDF,
   classification source, + anything in a's folded half), while the row plan names only S894–S898 (5). The
   declared after-state and the row plan are mutually inconsistent until the L1 either extends the map/row set
   or declares the entry rewrites that drop these attributions.
3. Candidate a's folded §N+1 depends on the reproduction document (S807) having a lane row — that row is
   S895, which exists only if candidate **d** lands. A cross-candidate dependency the DRAFT never declares
   (c7 separability is claim-level, but the admission logic needs the dependency said).

Fix owner: L1 + id-map seat, before freeze: extend the by-document map to every inline id in the four files
(rule: `S718→S896-or-S897, S750→S896` by document; `S807→S895 conditional on d landing`; decide
`S777/S719/S757` = new rows or entry edits), pin the map sha256 in claims.json (round-75 precedent
`map.sha256`), and make the counter's inline-id sweep read the map, not a hardcoded table.

### F3 — HIGH (c18 :57; one-row-per-document) — showGb and newGbInfo are one document; S896+S897 double-count

Measured 2026-10-27, browser-shaped UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/130.0 Safari/537.36`, plain curl:
```
$ curl -sS --max-time 40 -A "$UA" -D headers -o showgb2.html -w '%{http_code} %{size_download} %{num_redirects} %{url_effective}' \
    'https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296'
302 (0 B) 1 https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter
(headers: HTTP/1.1 302, Location: …newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter)
$ curl -sS --compressed … 'https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E10…'
200, 8075 B, <title>国家标准|GB/T 33661-2017</title>, 'GB/T 33661' ×2, 发布日期/实施日期 ×2
$ curl -sS -L … showGb (live today) → 200, 24144 B, same <title>, 'GB/T 33661' ×2
```
`showGb` is a 302 redirect alias of `newGbInfo` — one document, one effective URL. The DRAFT plans **two**
rows (S896 capture-only + S897 live), which (a) violates one-row-per-document (the DRAFT itself reserves
"two URLs are one document" as a plan-change trigger — this is that case, measured), (b) overcounts k by 1,
(c) leaves S897 as a row whose source cell names a URL that never serves content (302 shell). Fix: one row
S896 = live `newGbInfo?hcno=E10…` + the S932 Wayback capture of that same page (pairing verified above);
record the showGb alias inside the row the way round-75 recorded Persée transcription pages inside S885.
Red-before: the 302 Location line goes in the row/lesson; the collapsed row set is re-derived in claims.json.

Bonus defect in the same family: candidate b asserts "byte-identical — 24148 bytes each, md5
`9791d9dc0f17384eeab4ff4791eed437`". Today's live body is **24144 B** with sha256
`80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9` — the campaign's numbers already drift
(the round-75 F10/F11 class: another round's bytes carried as standing facts). Any landed sentence citing
byte counts/md5 must re-measure this round under its own UA-bound record (c12 :41, c22 :66, c27 :127) or be
dated as the campaign's observation.

### F4 — HIGH (c15 :47) — candidate a fails the clause-scope lint as staged

```
$ python3 -B $L/tools/check-cited-lines.py <staged>/calendar-festival-systems.amend-2026-10-24.md
MULTI-ID …amend-2026-10-24.md:8 S932,S935,S937
MULTI-ID …amend-2026-10-24.md:62 S919,S921
MULTI-ID …amend-2026-10-24.md:95 S919,S921
CITED-LINES: 3 finding(s) in 1 file(s)      (exit 1; re-run without pipe: exit=1)
```
Line 8 is the staged prose `recheck:` line (three ids with counts) — the round-75 Normalization rule
(strip to cadence-only `180d`) removes it; lines 62 and 95 are body bullets citing S919+S921 together and
must be split one-clause-per-line at landing. The other three candidates lint clean (b, c, d: `0 finding(s)`,
exit 0). Red-before for the C counter: the lint must exit 0 on every landed entry path (round-75 CITEDLINES
leg shape — and per c28 :150 the lint tool must be pinned at the freeze, not read from the graded tree).

### F5 — HIGH (tier preamble :22-24; c18 :57; c21 :63; c24 :79) — candidate d rests on a tier-C row with zero captures

1. Candidate d's only `source:` row is S916 → S895 (xingzuobaike reproduction, tier C, "declared as such in
   the row"). The DRAFT's own after-state: "no tier-C row is the sole support of an admitted entry". As
   staged, d **cannot** be admitted without violating the after-state: it cites no A/B row (S718/S719 are
   coupling-line mentions per the DRAFT — and per F2 they are foreign ids anyway). Fix: give d a non-C
   source (the registry-record row for identity, or the gmw report row for the rules' content) or refuse d.
2. The xingzuobaike page has **zero** Wayback captures (CDX exact, measured):
```
$ curl -sS 'https://web.archive.org/cdx/search/cdx?url=www.xingzuobaike.com/huangli/wannianli/d165803.html&output=text&limit=4&fl=timestamp,statuscode,digest'
(empty body, exit 0)
$ # positive control, same query shape:
$ curl -sS '…url=www.unige.ch/lettres/framo/cernet/biblio/barth70.html…'
20030908073936 200 J3LCWQ46LN7YBZJMDL5ANWA7ZUMC6IG4
20041220223357 200 J3LCWQ46LN7YBZJMDL5ANWA7ZUMC6IG4
```
   Any "no capture" ruling on S895 must be filed per c21/c24 (probed URL verbatim, provenance, live probe
   result, exact CDX query + raw count, positive control, redirect target). Durability then rests on the live
   URL serving the quote to a re-opener — measure that before freezing the row.
3. By contrast, the gmw.cn report HAS a capture — `news.gmw.cn/2017-05/23/content_24559485.htm` →
   `20170523024955 200 IHP5SRJMWRHJIGMLJVZ4LWLYYUS37MLD` (CDX exact, measured) — so S898 can satisfy c18's
   live+capture pairing; the DRAFT never says so. And S894's pairing is viable: the S935 capture
   (`web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search`) returns 200, 34997 B
   with 28 hits of `明治|令和|大正|元号`; the live form returns 200, 311308 B with the same 28 — the anchor
   span is pinnable inside the capture's stored window (round-68's S825 "portal landing" refusal does not
   recur on these bytes). Red-before: pin the exact anchor quote inside the S935 capture window before freeze.

### F6 — MEDIUM (c10 :37, c12 :41, c13 :43, c16 :49, c22 :66) — wall-class claims and live legs lack a frozen treatment

(a) Candidate a carries wall/refusal claims about the openstd full-text route ("behind a script-driven reader
that serves no standard text to a non-browser client", "the page the round fetched at 200 bytes"). If any
round-76 Gate reason cell opens `wall:`/`captcha:`/`status:` — these claims make that likely — c22's record
shape binds: per-request `UA "<exact>" -> HTTP <code>, <bytes> B, wall present("<marker>")|wall absent`,
twice (plain + the pinned browser UA), `automation: none`, three controls filed. The DRAFT never mentions the
c22 shape or its controls. Note the record pages themselves are NOT walled (measured: plain 200s above); only
the full-text preview route is modal-limited — the Gate must not over-file the record page as walled.
(b) No unreachable-live treatment is declared for S895 (no capture exists), S897 (alias), S898 (live+capture
exists — name it), or any re-fetch: no retry budget (attempts/passes/gap), no paired budget control (c16),
no frozen "unreachable ⇒ capture row" rule beyond the S894 case (c13). Fix before data; never relaxed after.
(c) Cross-round /tmp hazard: the DRAFT requires "the round-76 counters honour TMPDIR/--work/$HYAKU_SCRATCH
and write nothing under a literal /tmp". But the Ca RECEIPTS leg re-runs the **frozen** round-75 accept-ca,
whose subprocess chain hardcodes `R74_TMPDIR = "/tmp"` (round-75 wave-3 finding 3; 121 mkdirs measured
there). Frozen bytes cannot be edited; the claim must declare the bounded allowance (env TMPDIR passed where
honoured; the frozen predecessor's literal `/tmp` mkdir disclosed as frozen behavior) before data, or the
round's own counter leg contradicts its own receipt.

### F7 — MEDIUM (c7 :31, c20 :61) — ownership split for shared surfaces is undeclared

Round-75 needed `owned_inplace`, `fixed_surfaces`, frozen exemptions and a COMBINED leg because C and Ca both
touch README.md and the lesson. Round 76 has the same overlap and the DRAFT names none of it:
- `SHONEN.md:6` tuple must move 817 → 817+k when C lands (the round-75 L75-01 `why` says claim C updates the
  same line C moves) — owner not stated.
- `corpus/README.md`: C adds index rows + culture-material count parenthetical (40 → 40+n) + footer; Ca (per
  round-75 routed items) repairs stale headings — the exemptions must be frozen.
- `corpus/lessons/round-76.md`: C's Gate admits vs Ca's correction rows — split must be frozen.
- `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8` (`verified-at` asserts 111487 B for
  S885; committed evidence says 109588 — ExecCountsSweep F11): the surface is `corpus/knowledge/**`, which
  the round-75 Ca SEPARABLE leg excluded from Ca's read set; under the DRAFT's Ca surfaces (SHONEN, SKILL,
  README) this false token has **no owner**. Assign it explicitly (C amendment surface, or a declared Ca
  exception naming the line).
- QUALITY.md fix for the inert c27 selector (round-75 routed item 3: "fix the selector or supersede 27 with a
  row naming it") is a Ca surface below the highest criterion (append-only, c25/26 append rule) — the DRAFT
  lists QUALITY 27 only as a pair *source*, not as a fixed surface.

### F8 — MEDIUM (c3 :13) — dangling `- couples:` targets in the staged entries

Base holds only `culture-material/calendar-festival-systems.md` and `era-periodization-models.md` (no
amend files; `ls-tree` measured). Couples targets absent at base AND not in the landing plan:
`linguistics/naming-systems.amend-2026-10-24.md` (a:33), `era-periodization-models.amend-2026-10-23.md`
(c), `calendar-festival-systems.amend-2026-10-23.md` (d) — the round-74 R3 dangling-pointer class. Also
b couples a's path and d couples c's path: admission of {b} without {a} (or {d} without {c}) leaves a
couples line naming a file that will never exist. Each landed entry's couples line must resolve or say why
not (round-75 triage precedent: refused families get a flip, not a silence).

### F9 — LOW (c6 :29) — tier call on S937 is scope-sensitive

Candidate a labels the gmw.cn state-press report "tier A … for the state press's promulgation report". For
the scope "what the announcement said" the report is primary; for "what GB/T 33661-2017 requires" it is
secondhand (the standard's clause text is tier-C reproduction S916 / unread authoritative copy). The row's
scope cell must pin the first scope; a correction lands as a superseding SOURCES row, never an in-place tier
edit (c6). Review-only.

### F10 — LOW (c4 :16, entry shape) — scaffolding language inside candidate a

Candidate a lands with `### Proposed body (dated addition)` headers, a `## Superseded passage — the round7
entry … Trim it if the later entry supersedes it outright.` instruction, and a ground line citing the
campaign's round numbering. Round 75 admitted entries as rewritten craft (staged 6862 B → landed 30920 B);
an admitted entry carrying trim-instructions/process scaffolding is the "lane-internal process text" class
round 75 refused outright (verification amendments family). The kill rule covers "a row appended as staged"
but nothing requires entry de-scaffolding — add an ENTRIES-leg clause (no `Proposed body`/`Superseded
passage`/round-N-of-the-campaign scaffolding) or a declared normalization note.

### F11 — verified-good (for balance; commands above)

- Registry 817 rows / knowledge 252 .md at base: `git show $B:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → `817`; `git ls-tree -r --name-only $B corpus/knowledge | grep -c '\.md$'` → `252`.
- Last id S893; S894+ free: max id `S893`; `grep -cE '\| *S(89[4-9]|9[0-9]{2}) '` → `0`.
- Collisions: `comm -12 reg-ids staged-ids` → `35` lines, S859…S893 (reg-ids 817, staged-ids 132 from
  `merge/kotodama/SOURCES.append.md`) — the DRAFT's "35 collisions S859-S893" re-derives exactly.
- `considerthese` absent: `ls …/considerthese` → exit 2, "No such file or directory" — matches the DRAFT.
- S885/S892 held and document-correct for the S921/S919 re-points (base rows read).
- Candidates b/c/d pass the c15 lint (0 findings).

---

## Conformance checklist (criterion | applies to | satisfying artifact | owner | red-before check)

Legend: C = claim C (coverage), Ca = claim Ca (calibration), L1 = L1/freeze, W2 = wave-2 seat. "RB" = the
check that must be red/capable-of-red before data, run from committed bytes.

| # | criterion (QUALITY.md line) | applies | artifact that satisfies it | owner | red-before check |
|---|---|---|---|---|---|
| 1 | Provenance (:5) | C | each entry's `source:`/`verified-at:`/`recheck:` trio; `(to-verify)` markers for anything not re-opened this round | W2 entry owners | grep entries for assertion-without-row (F2 sweep); no invented rows |
| 2 | Calibration (:9) | C (weak) | entries are instruments, not frameworks; keep status vocabulary inside the entry (round-75 wave-3 finding 5 class) | W2 | review-only |
| 3 | Coupling (:13) | C | `- couples:` lines resolving to base-or-landing files; F8 dangling targets resolved or annotated | W2 + L1 | resolve each couples path at `<lands>`; exit 0 |
| 4 | Usability (:16) | C | decision/typology tables in a–d (candidate c is thin — expand or refuse) | W2 | review-only + ENTRIES word floor |
| 5 | Canon hygiene (:18) | C | "decides no era / no culture's calendar" scope lines already staged | W2 | grep scope lines present |
| — | Tier-C not sole support (:22-24) | C | F5: d gains an A/B source or is refused; after-state clause already declared | L1 | counter leg: every admitted entry cites ≥1 non-C row |
| 6 | Claim-scoped tiers (:29) | C | SOURCES rows with scope cells; F9 gmw scope pinned | L1 | review-only; corrections via superseding row |
| 7 | Separability (:31) | both | declared export block (exact S894–S898 ids, no open range); owned_inplace/fixed_surfaces/exemptions (F7); F7's F11 ownership | L1 | `tools/check-claim-separability.py` on manifest, exit 0; loop S000–S999 equals declared block |
| 8 | Declared inputs run (:33) | both | pre-dispatch receipts committed with declaration, incl. corrected F1 greps | L1 | receipt commands match declaration verbatim |
| 9 | Dry runs both ways (:35) | both | receipt names absent-land exits + before-values; no first-absent-stop | L1 | two-way diff receipt vs declarations |
| 10 | Ordinary means (:37) | C | plain requests + Wayback captures only; F3/F6 records; no bypass anywhere; `tools/check-source-access.py` exit 0 | W2 scouts | checker exit 0; reviewer re-open sample |
| 11 | Clauses able to fail (:39) | both | clause list in claims.json checked by a non-author seat (this report = the w1 pass); per-clause red controls; no pipefail-less pipes | W2 critic | controls receipt: green control exit 0 + one red control per mechanical clause |
| 12 | Re-test rejection grounds (:41) | C | Gate reject rows carry re-test tool + verbatim output | W2 | each reject row's command re-run, output in Gate |
| 13 | Unreachable handling frozen (:43) | C | F6(b): capture-row rule for S895/S897/S898 frozen before data | L1 | clause present in claims.json at freeze |
| 14 | Judged object frozen (:45) | neither | no blind packets declared | — | n/a (revisit if L1 builds packets) |
| 15 | Cited-line shape (:47) | C | F4: lint exit 0 on all landed entries; tool pinned per c28 | W2 | `check-cited-lines.py <entry>` exit 0 ×n |
| 16 | Bounded fetches, body-scoped quotes (:49) | C | F6(b) budget + paired controls; quotes from body text (era table = form text — confirm body vs UI chrome before anchoring) | L1 | control receipt LOCATE-CONTROL shape |
| 17 | Receipt pins (:55) | both | stamped/evaluated/measured/tree/counter-sha headers | L1 | `tools/check-receipt-seq.py --lands …` exit 0 |
| 18 | Row anchors resolve (:57) | C | F3/F5: one live + same-page capture per row (S894 ✓ measured, S896 ✓ measured, S898 capture 20170523024955, S895 none — ruling filed); anchors in capture windows | W2 | anchor grep in stored window, hits ≥ 1 per row |
| 19 | Runs at stamped rev (:59) | both | `--lands <40hex>` required; clone materialized at lands; `--topo` post-records | L1 | receipt headers equal; SEQ exit 0 |
| 20 | Trends on observables (:61) | both | C = coverage improvement; Ca = record repairs → declare `unchanged` where no observable; discernment needs the outside spot-check | L1 | SCORECARD axes rows present (round-75 stale-minor c class) |
| 21 | No-capture probe discipline (:63) | C | F5: xingzuobaike ruling filed with probed URL/provenance/CDX raw + positive control + redirect target | W2 | the filed probe lines exist in Gate/evidence |
| 22 | UA-bound wall records (:66) | C (if any wall/status reason) | F6(a): two-UA records, exact browser UA string, bytes+marker, `automation: none`, three controls | W2 | `grep -Ec GROUND == grep -Ec SHAPE` over `## Gate`; controls filed |
| 23 | Selftest receipts + red-before (:77) | both | selftest receipts before falsify wave; counters run at FREEZE commit; `counter-revisions.md` for post-freeze changes; addendum limbs (fixture names constants; `clean -> exit=0` first) | L1 | `head -2 selftest-ca.txt \| grep -q 'clean -> exit=0'`; limb-1 one-liner prints nothing |
| 24 | CDX positive control (:79) | C | F5 probes (measured above; re-filed by W2 with provenance) | W2 | positive-control line present beside every no-capture ruling |
| 25/26 | Freeze constants + junk landings (:81, :125) | both | `--freeze` required; constants via `git show <freeze>:…`; FROZENCFG; do-nothing `lands==freeze` FAILS data legs; J1–J7 fixtures + receipts committed after freeze; c26(c) shapes; c25 one-liner exit 0 both counters | L1 | one-liner over both counters; controls-c/ca receipts; junk receipts name generator sha + fixture commits |
| 27 | Reject reason names artifact (:127) | C | every round-76 Gate reject row carries repo-relative capture + 「span」 + absent/present; ALSO the routed fix: c27 selector repaired or superseded (round-75 routed item 3) | W2 + Ca | one-liner over `round-76.md` exit 0, no NO-FIELD/MISFILED; fixture row first |
| 28 | Tool authority pinned at freeze (:150) | both | pins for every repo tool a leg executes (`check-cited-lines.py`, any generator); **incl. the fleet-side `scripts/sources-census.sh` sha pinned in claims.json and compared before the CENSUS leg runs** (it is outside the lane; neither --lands nor --freeze can pin it) | L1 | c28 one-liner prints nothing; census sha compare leg |
| add. | c23 addendum (:164) | both | re-pointed read paths move with their fixtures; clean-green-first selftest | L1 | limb-1 + limb-2 one-liners (QUALITY :176-181) |
| Ca | Ledger (DRAFT) | Ca | ≥10 pairs from ExecCountsSweep F1–F13 + spotcheck §7 1–7 + routed 1–8; dispositions honor append-only surfaces (lesson/LOG/SCORECARD/QUALITY = ANNOTATE; SHONEN/SKILL/README = REPAIR); F11's entry token gets an owner (F7); claims.json F6 token annotated, not edited | W2 ledger seat + L1 | BASEMISMATCH at 98c486b for every pair; observe_cmd allowlist excludes interpreters/echo; NOSTUB |
| Frontier | census/lesson (DRAFT) | C | census-start exit 0 committed at base; lesson sections Gate/Quarantine/Collision guard/Normalization/Census/Mistakes/Routed-77; ≥1 mined mistake + criterion when none caught it; census prints no row count (do not claim it does — round-75 stale-minor b) | L1 | `bash census-start.txt` tail shows `exit=0`; lesson grep per section |

## Landing-violation flags the assignment names, answered

- **c10 openstd access control**: record pages answer plain 200s (measured; no challenge met). The only
  wall-class surface is the full-text preview route. No bypass needed or attempted; any wall claim in the
  entries must carry c22 records, and the Gate must not file the record page as walled.
- **c15 cited-line shape**: candidate a exit 1 today (F4, measured); b/c/d exit 0.
- **c18 live+archive pairing**: S894 ✓ (both sides carry the era strings, 28/28), S896 ✓ (capture decodes to
  the record page, same title/fields), S898 ✓ (capture exists), S895 ✗ (zero captures — ruling must be filed;
  live-only durability), S897 ✗ (redirect alias — not a row).
- **c22 wall records**: shape + controls missing from the DRAFT (F6a).
- **c26 receipts**: freeze must carry claims/ledger/counters/do-nothing/selftests (c26a); junk receipts after
  freeze (c26b); J4/J4b fail FROZENCFG not LEDGER (c26b); `accept-c` passes a complete landing as its own
  freeze — the do-nothing leg is control-only (c26c); gate rows citing counter shas re-derived from installed
  bytes (c26d — round-75 finding 6 class: `fa5060b9` vs committed `315c5f3f`).
- **c27 reject-reason shape**: selector currently inert (round-75 routed item 3); round 76's own rejects must
  pass the one-liner, and the selector fix/supersede is a Ca surface (F7).

## Residual risk and verification gaps (unrun checks, honestly)

- I did not fetch gmw.cn, xingzuobaike, or the NA capture *contents* beyond grep counts; the anchor spans for
  S894/S896/S898 are pinned only to "era strings present" / "record fields present", not to exact located
  quotes — W2 must locate the exact spans inside stored windows (c18 RB).
- I did not probe the showGb→newGbInfo alias under the plain `curl/8.7.1` UA (c22 wants both UAs for any wall
  record; no wall was met, so no record is owed — but a W2 Gate row that files one must do both).
- The k arithmetic (F2) is derived from the staged bytes as they stand; if the L1 rewrites entries before
  freeze, re-run the id sweep.
- Candidate bodies beyond the cited lines were read once (criteria 1/2/4 review-only pass), not
  fact-checked against pages — that is the entry-owner's admission work, not this seat's.
- Scratch fetches used `curl --compressed` after the first uncompressed S932 fetch stored gzip bytes
  (sha `870bd7ad…` over compressed bytes) — evidence files must store decoded bytes; window-sha256 recomputes
  over decoded text (c17 class).

## Disclosure

No tools installed (nothing needed); pacman untouched. Scratch `/fast/scratch/hyaku/kotodama-r76/RevQualityFit`
created, receipts copied to `.ufo/waves/round-76/w1/stage/RevQualityFit/` (`receipts.txt` + four fetched
bodies: `std/newgb2.html` decoded S932 capture, `std/showgb2.html` live showGb→newGbInfo body,
`na/na-capture.html`, `na/na-live.html`), scratch deleted before yield. All git use read-only (`show`, `grep`,
`ls-tree`); no lane file outside this report and the stage dir was written.

Report: .ufo/waves/round-76/w1/RevQualityFit.md
