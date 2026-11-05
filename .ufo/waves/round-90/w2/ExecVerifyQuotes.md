# ExecVerifyQuotes — round-90 w2 — independent re-fetch and quote agreement

Seat: ExecVerifyQuotes. Date of re-fetch: 2026-11-05T00:11:51-03:00 … 00:11:57-03:00.
Scratch: /fast/scratch/hyaku/kotodama-r90/ExecVerifyQuotes/ (TMPDIR=$SCRATCH/tmp; removed on exit; receipt copies staged in my stage dir).
Production untouched: read-only probes only; all writes confined to my scratch, my stage dir, and this report.

Method: `curl -sS -L --max-time 90` per URL (seven admitted + one rejected), one file per id, with per-request http code, byte count, sha256 and a local ISO-8601 instant with offset. Byte comparison `cmp`-equivalent via sha256; where bytes differed, `diff` for the content-line diff. Then the w1 comparator `recheck.py` and the frozen counter `measure90.py`, both run from scratch copies/clones (details below). Manifest integrity checked row by row against the committed files it names.

## 1. Eight-row agreement table (my fetch vs manifest pin vs committed capture)

| id | url (host/path) | manifest sha256 (first8…last8) | my sha256 | bytes (man = mine) | http (man = mine) | byte agreement | differing lines |
|----|-----------------|-------------------------------|-----------|--------------------|-------------------|----------------|-----------------|
| S942 | wals.info/chapter/72 | e28b23dc…c004c6 | same | 41840 = 41840 | 200 = 200 | IDENTICAL | none |
| S943 | wals.info/chapter/73 | b3f0f850…88bbc3 | same | 50562 = 50562 | 200 = 200 | IDENTICAL | none |
| S944 | wals.info/chapter/71 | e939d949…b02dce | same | 46113 = 46113 | 200 = 200 | IDENTICAL | none |
| S945 | glossary.sil.org/term/vocative-case | f3ac4093…f60ea00 | same | 11053 = 11053 | 200 = 200 | IDENTICAL | none |
| S946 | atticinscriptions.com/inscription/IGI3/646 | 26bb20bd…220b1c | same | 13536 = 13536 | 200 = 200 | IDENTICAL | none |
| S947 | pmc.ncbi.nlm.nih.gov/articles/PMC13671548/ | aa81f3a7…6de5cb | 1d42ab0c…b27ee1 | 295969 = 295969 | 200 = 200 | CHANGED — session tokens only | line 77 `ncbi_phid`; line 2769 `csrfmiddlewaretoken` |
| S948 | drops.dagstuhl.de/entities/document/10.4230/OASIcs.CMN.2016.12 | c1a7de09…d84936 | afe783a9…e6b0d8 | 105415 = 105415 | 200 = 200 | CHANGED — session tokens only | line 12 `csrf-token` meta; line 783 hidden `_token` |
| S949 | en.wikipedia.org/wiki/Votive_offering | 8bfab02c…50dc9345 | same | 182403 = 182403 | 200 = 200 | IDENTICAL | none |

Exact differing content (from diffs staged in my stage dir):

- S947: `<meta name="ncbi_phid" content="C1ED6C35…254.m_1" />` → `C1ED6DF3…FF4.m_1`; `<input type="hidden" name="csrfmiddlewaretoken" value="Ln41Kqla…jxxdci">` → `ilIjCpo9…iLXDM5`. 2 changed lines, both per-request session tokens; no prose line differs.
- S948: `<meta name="csrf-token" content="7rcQAlSl…Kj0L2crk">` → `iPRjK0kt…mQDAR`; `<input type="hidden" name="_token" value="7rcQAlSl…Kj0L2crk" …>` → same new value. 2 changed lines, both the same per-request token; no prose line differs.

Score: 6/8 byte-identical, 2/8 changed and both changes are exactly per-request session/CSRF tokens (PMC `ncbi_phid`+`csrfmiddlewaretoken`; Dagstuhl `csrf-token`+`_token`). This matches the w1 seat's independent fetch profile (their agreement.json records the same two rows as `differs-only-in-session-token` with the same two fields each), so the sites' volatile surface is bounded and the landed captures are faithful.

## 2. Manifest integrity verdict: CLEAN

Every row of reports/round-90/evidence/manifest.json checked against the committed file it names:

- sha256: 8/8 match `sha256sum` of the committed capture (S942–S949). Verified twice (probes at 00:12 and 00:13).
- bytes: 8/8 match `stat -c%s`.
- capture path: 8/8 exist, relative and confined to reports/round-90/evidence/, none a graded file, no `..`.
- http_status: 8/8 recorded 200; my own independent fetch returned 200 on all eight URLs today.
- fetched_at: 8/8 parse as ISO-8601 local instants with -03:00 offset; 8/8 dated the as_of 2026-11-04; monotone non-decreasing; 7 unique seconds with S944/S945 sharing one second; the S948→S949 gap of +2m18s matches the lesson's account (S949 re-fetched after the rejection screening).

No fabrication vector found: no hash mismatch, no size mismatch, no path escape, no impossible instant.

## 3. w1 comparator recheck.py — rc=1, 7/8 quotes located (single FINDING: S949)

The comparator resolves its lane root as four `..` above its own file, so a verbatim in-place run would look for the manifest under `.ufo/waves/reports/…` (wrong depth) and would overwrite the sibling stage's `agreement.json` (a write into another seat's stage). I therefore ran a byte-identical copy (recheck.py + fetch.json + caps/ + agreement.json, sha-verified) inside a sandbox lane laid out for its depth resolution, with byte-identical copies of the landed manifest.json (81786114…67b0b7) and lessons/round-90.md (d758b2a9…54983). All logic paths are then the committed code against the landed bytes.

Observed output (rc=1):

```
FINDING S949: quote no - missing span: 'A votive offering or votive deposit is one or more objects displayed or deposited, without the intention of recovery or use'
AGREEMENT: 7/8 scribe quotes located in this seat's captures
```

Nothing fixed in production (none needed). Mechanism of the single miss, verified three ways:

- The capture S949.txt stores the Wikipedia lead as Parsoid HTML: `A <b id="mwIw">votive offering</b> or <b id="mwJA">votive deposit</b> is one or more objects displayed or deposited, without the intention of recovery or use, in a…`. The lesson quote is the tag-stripped reading of exactly that sentence — a char-exact PREFIX of the stripped lead (123 of 129 chars). It is not a source-cell quote, not chrome, and not drift: committed capture, w1 caps copy and my fresh fetch all carry sha256 8bfab02c…50dc9345 today.
- S949 is the REJECTED row: the frozen grader's GATE/CAPTURE legs grade only `qualifying` ids (status `mined`, opened as_of, used-by the entry), so S949's quote is outside every graded C leg. Measured, not inferred: the frozen counter passes C 4/4 at the lands with these same lesson bytes (below), and its own prose band (w1 companion `prose-check.py`, run against the landed manifest/lesson/registry) also classifies S949 `ABSENT` while the seven admitted rows are all `PROSE` (rc=0, `PROSE-CHECK: 8 prose-or-listed / 0 CHROME`).

## 4. Quote agreement of the seven admitted gate lines at the landed bytes

All seven admitted lesson quotes locate byte-exactly in the committed captures (grep -F, whole-file): S942 (offset 7274), S943 (8904), S944 (5142), S945 (856), S946 (11850), S947 (46261), S948 (2365). Note on S948: the Dagstuhl page carries the n-selection sentence three times — twice as `can&#039;t` (abstract HTML) and once with a plain apostrophe (metadata variant); the lesson quote's plain-apostrophe form matches the third occurrence exactly, so there is no normalization gap against the frozen oracle. Six of seven (S942–S947) also locate byte-exactly in my fresh fetch; S948's fresh bytes differ only in the two token lines, and the quoted sentence is present in both.

## 5. Frozen counter measure90.py run by this seat (scratch clone, freeze-pinned receipts)

Clone: /fast/scratch/…/ExecVerifyQuotes/clone (git clone of the lane; freeze d0b6f2a7…f0c8, base 6b0b86e4…58c4 and lands 7f3a7aa6…4761 all present).

- Claim C at lands 7f3a7aa6…: `MEASURE90-C: PASS legs=4/4` (MATERIALIZE, ENTRY clean across ENTRY,SHAPE,TOPIC,NEWIDS,GATE,CAPTURE; INDEX `CORPUS-INDEX: OK files=262 rows=262 findings=0`; APPENDONLY clean). rc=0. Receipt staged: measure90-C-receipt.txt.
- Negative control, claim C at the freeze revision itself: `MEASURE90-C: FAIL legs=2/4 failed=ENTRY,APPENDONLY` (`entry absent at lands`; `0 qualifying new ids < 3; entry absent from corpus/README.md`) with MATERIALIZE and INDEX still passing — the expected instrument contrast. rc=1. Receipt staged: measure90-C-neg-receipt.txt.
- Claim O at lands 7f3a7aa6…: `MEASURE90-O: PASS legs=6/6` (TOOL sha 121888f0…828ed; SELFTEST 67/67; REFUSALS all 13 ok; MUTATION 43/43 killed, 0 survived, 0 broken-pattern; STUB recorded). rc=0, wall ~242 s. Receipt: measure90-O-receipt2.txt (clean, uncontended run).
- My first O attempt printed FAIL 3/6 (SELFTEST FileNotFoundError on a selftest fixture path; REFUSALS/MUTATION cascading). That was my own concurrency artifact — I had two overlapping measure90 O invocations sharing one --work dir; one run's fixture staging removed the other's `st-o/st/corpus/knowledge/myth-symbol/twocol.md` mid-selftest. The clean single-run rerun (fresh --work, one invocation) passes 6/6 as the committed receipts at reports/round-90/final/lands-O.txt also record. No production defect; noted so the reviewer does not misread the transient.

## 6. Cross-bindings checked along the way

- Registry rows S942–S948: used-by = corpus/knowledge/linguistics/petitionary-and-votive-formulae.md for all seven; entry header `sources: S942 S943 S944 S945 S946 S947 S948` — one-to-one, no extra, no missing. S949 used-by = corpus/lessons/round-90.md, status `rejected`, tier C.
- corpus/README.md names the entry (lines 360 and 942).
- Gate quotes fit the frozen bounds (claims.json: <=25 words, >=20 chars): S942 17w/138c, S943 15w/99c, S944 20w/148c, S945 14w/76c, S946 19w/124c, S947 14w/92c, S948 21w/124c, S949 21w/123c (S949 informational only).
- Workspace note: at probe time the lane working tree carries an uncommitted one-line change to the entry (commit 3f56892f "…minimal/maximal definitions…" is HEAD; working tree replaces the em-dash Greek/Latin clause with an uninflected-foreign-name clause) and an extended census-end.txt header. The registry at HEAD equals the lands registry byte-for-byte (65c32390…4e1903), and my comparisons used the landed bytes via the archive/clone.

## 7. Verdict

- Re-fetch agreement: 6/8 identical, 2/8 session-token-only — captures at the landed bytes are faithful; no content drift on any quoted span.
- Manifest integrity: CLEAN on all four checked dimensions (sha256, bytes, capture path, http_status/fetched_at format+date).
- Quote agreement: 7/8 under the committed comparator; the single miss is the rejected row S949's tag-stripped lead quote, outside every graded leg, confirmed as a capture-format artifact by three same-sha captures and by the w1 seat's independent prose check.
- Counter state at the lands: C PASS 4/4, O PASS 6/6, freeze negative for C fails as designed.

Blockers: none. Risks: none found in the landed evidence surface; the S949 lesson line will keep failing any quote-in-capture locator that ever widens to rejected rows, because the capture is Parsoid HTML — worth knowing if a future round reuses this comparator's norm against rejected-row lines.
