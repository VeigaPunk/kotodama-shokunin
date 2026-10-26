# ScribeEntryAmend23Final — final text of the amend-2026-10-23 entry (claim C, round 75 wave 2)

Seat: scribe, leaf. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`.
No subagent, no background job, no `task` spawn. No install or upgrade (nothing needed; `curl`, `python3`, `wc`,
`sha256sum` sufficed — recorded here per the tooling ruling). Read-only git only; no git/jj mutation anywhere.
Nothing outside my report and my one staged file was written.

## 1. Behaviour — what this seat produced

| Path | Bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` | 24,166 | `25992609cdb303353dbbb60b98a03abd01d56d1ec7349ceddcc365c429a8a717` |

Shape, measured after the last edit:

```
CITED-LINES: 0 finding(s) in 1 file(s)      (exit 0)
wc -w  = 3951 ; body words from the first `## ` = 3401 (floor 478 = the smallest entry at base)
sections `## ` = 8 ; header `- ` lines = 11 ; S-ids = {S885:6, S886:7, S887:8} — no other id
```

Header order: `source` ×3 (one id each), `verified-at`, `recheck`, `ground`, `topic`, `gap filled`, `sources`,
`couples`, `scope`. No header value is a placeholder and none carries a `<...>` token (the earlier `<base>` in the
`ground` command was replaced by the full base hash). `- topic:` is one line and is the text the README index row
must copy verbatim.

The entry is method and design orders only — an 8-step checklist, three decision tables, an attribution table and
a calibration table — and ends at the canon handoff to lore-shokunin through
`synthesis/worldbible-integration-contract.md`. It makes no rights or attribution ruling.

The closing section the seat prompt flagged is fixed: the file no longer says the five *S/Z* codes are unrecovered.
It says the codes are not in the 1966 article, that they are not asserted here, and that they are carried with
their attribution by the sibling `narrative-structure-frameworks.amend-2026-10-23b.md` (staged by seat
ScribeEntry23bFinal). §2 likewise defers the levels' count and the four classes to that sibling instead of
restating them, so the two amendments do not duplicate each other.

## 2. Fetch record — every User-Agent bound to the response it got (QUALITY 22)

All requests were plain `GET`s (`automation: none`, no browser automation, no login, no cookie reuse), UA
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, scratch
`/fast/scratch/hyaku/kotodama-r75/ScribeEntryAmend23Final/` (removed before yield).

Pass 1 (before a mid-run scratch loss) and pass 2 (after recreating the directory) agreed **byte for byte** on
every page-level URL, which is the cross-pass stability record:

| URL | HTTP | bytes | sha256 (both passes) |
|---|---:|---:|---|
| `…/doc/comm_0588-8018_1966_num_8_1_1113` (Barthes notice) | 200 | 111,487 | `2a26fa8c…` (pass 2); pass 1 body `6b1f19bb…`, same length |
| `…/doc/page/…_1113/…_T1_0005_0000` (Barthes p. 5) | 200 | 4,286 | `8998f55ea7e913d0a82fbed9aacbf312d3fbdb3b1a33066288688c102834fbdf` |
| `…/doc/page/…_1113/…_T1_0006_0000` (Barthes p. 6) | 200 | 3,811 | `efee74ba5aaa3723f32e2fe2f983467645d0db3c6db7ec223194c82cd2f0348d` |
| `…/doc/page/…_1113/…_T1_0026_0000` (Barthes p. 26) | 200 | 4,390 | `fbe16353fb945c97811db21b9f5d414c04f39f0c1be513e67668fe32b356807b` |
| `…/doc/comm_0588-8018_1966_num_8_1_1120` (Todorov notice) | 200 | 109,336 | `13accad2…` (pass 1 body 109,335 B, `81f256a9…`) |
| `…/doc/page/…_1120/…_T1_0125_0000` (Todorov p. 125) | 200 | 3,054 | `12b0d50a82f074de…` |
| `…/doc/page/…_1120/…_T1_0138_0000` (Todorov p. 138) | 200 | 3,865 | `e83fb9fc9288b1904e3a07dc70b461549329bc783ccb76ef313f980f3ecfd09c` |
| `…/doc/page/…_1120/…_T1_0139_0000` (Todorov p. 139) | 200 | 3,939 | `16992c94b5e8b314afc2fb8c4ccc297cdc3199855d6fff68f518006b4e17d724` |
| `…/doc/comm_0588-8018_1966_num_8_1_1114` (Greimas notice) | 200 | 116,879 | `cba68ecc…` (pass 1 bodies 118,777 / 116,878 B) |
| `…/doc/page/…_1114/…_T1_0029_0000` (Greimas p. 29) | 200 | 3,451 | `84557aef3cac190d5f838e03aa2d1abcf24420e51b4c99c5671c48afe6e42773` |
| `…/doc/page/…_1114/…_T1_0030_0000` (Greimas p. 30) | 200 | 3,737 | `2502768202dbd0e0b17f6310ad4b0c6cfe7e3d1edbd490efab5f7c4f71fe082f` |
| `…/docAsPDF/comm_0588-8018_1966_num_8_1_1113.pdf` | **403** | 294 | `1cb8d16f4f529352194cb2f2dab681bc…` — body contains `altcha` |

The three notice bodies are assembled server-side and vary a little between fetches (lengths 111,487 / 109,335–109,336
/ 116,878–118,777 B); the page-level transcription URLs are stable across passes. The round's committed evidence
window, not this table, is the authority for the notice text. No challenge was present on any page used; the PDF
endpoint's challenge was met and not passed and no attempt was made to pass it (QUALITY 10, 22).

## 3. Quote verification — every fact-bearing sentence re-opened

I extracted every `"…"` span from the staged file and located it, after NFKC + whitespace folding, in the fetched
body of the page its sentence names. Result: **32 of 38 spans located**, each on the page cited. The six not found
are English phrasings in the author's own voice and not quotations of a source (`Does this people tell stories?`,
`narrative grammar`, `is this detail interesting?`, `what can this detail be correlated with, and does the draft
actually correlate it?`, `natural`, `structuralism says`). The earlier uncited framing `"narrative is universal"`
was removed in review rather than kept as a quotation.

Page bindings actually tested: Barthes p. 1 → notice body; Barthes p. 5 → `T1_0005`; Todorov p. 125 → notice body;
Todorov p. 139 → `T1_0139`; Greimas p. 28 → notice body; Greimas pp. 29–30 → `T1_0029`/`T1_0030`. The OCR-damage
examples quoted in §7 were each confirmed in place: `V analyse` and `Vhistoire` on Barthes p. 5, `Psychologie de
Vart` on Todorov p. 139, `de'` on Greimas p. 29, `iso- topies` on Greimas p. 30.

Claims deleted or softened against the pages:

1. Todorov's "three groups" sentence is on printed p. 138, which the S886 row does not name — the quotation was
   **removed**, and the threefold cut is now stated from p. 139's own clauses.
2. The Barthes p. 26 quotes of the draft were **cut**: p. 26 is outside S885's declared pages, and the "two
   readings" proposition is carried by Greimas p. 30 (hoisting the duplicate out, as SimplifierRows §3 required).
3. The Greimas "equivalence to establish" and the "formulation théorique" hedge are on p. 31, outside the row's
   declared pages — **not asserted**; §4 says only that the page describes two readings and nothing on it makes
   them one.
4. The staged "the two must be set equivalent" and "characters' words against the narrator's" phrasings are absent
   from the file (the latter is on p. 141, not a page any of my rows names).
5. The paper's own résumé-level claims ("arrived at independently") never appear here.

## 4. RevEntryQuality F1–F13 — each applied, or not applicable, with the reason

The named review file did **not** exist at the lane path (see finding W2-1). Its text was read at
`/home/vgpnk/Projects/shokunin/.ufo/waves/round-75/w1/RevEntryQuality.md` (read-only) and each finding is disposed of
below for *this* file.

| F | Applies to my file? | Disposition |
|---|---|---|
| F1 campaign ids (S744/S763) | No | my file carries no campaign id; the only ids are S885/S886/S887, each on its own `source:` line. Verified by id census (§1). |
| F2 S870 unmapped | No | S870 is cited nowhere; the S893 re-quote belongs to the base entry, not this amendment. |
| F3 criterion-15 shape / multi-id recheck | Yes | `recheck:` is cadence-only and id-free; no line carries two ids; the lint prints 0 findings. |
| F4 four Barthes locators folded into one window | Yes | applied as the "one window rule" paragraph: the window is stated to be the served notice, the p. 5 spans are stated **not** to be inside it, every span carries its printed page, and the p. 6/p. 10/p. 11 material is deferred to the sibling. |
| F5 dangling `couples:` targets | Yes | `couples:` names the base entry, the sibling `-23b` (a frozen entry), `comparative-frameworks.md`, `hero-journey-variants.md`, `era-periodization-models.md` (the existing file, **not** the pending `…amend-2026-10-23.md`), and `synthesis/worldbible-integration-contract.md`; all exist at base except the two frozen entries, which land with this claim. |
| F6 "four levels" error | Yes | the file asserts no count at all and hands the count to the sibling; no "four levels" phrase. |
| F7 row-membership vs conditional entries | Partly | my three rows each have this entry as a citing file, so none is orphaned. The defect survives in the *row cells*: see W2-4. |
| F8 calibration absent | Yes | §6 is a calibration table naming **mainstream / contested / discredited** with the reason, plus the grade sentence (primary documents of a research programme, not consensus results). |
| F9 "arrived at independently" | No | no such claim exists in the file. |
| F10 campaign-local pointers | Yes | no `CANNOT-ANSWER.md`, `SOURCES-PROPOSED.md` or round-chronology pointer; `ground:` is re-derived from the base commit. |
| F11 not yet usable | Yes | three decision tables, an attribution table, a calibration table and a 9-step checklist with failure symptoms, runnable without the articles. |
| F12 uncited Eco/Bremond characterisations | No | neither name appears; Bremond is mentioned only as a credit Barthes himself makes on p. 5 — and that mention was dropped from my file (it lives in the sibling). |
| F13 challenge disposition | Yes | §7 says the PDF endpoint's altcha challenge "was met and not passed, no attempt was made to pass it", and states that nothing rests on the PDF or the walled surface; the page-level transcriptions are described as an ordinary public surface, never as access-controlled (the claim's kill-rule clause). |

## 5. Findings the L1 must settle before freeze

**W2-1 (HIGH, process) — the wave-1 entry review is in the wrong repository.** `RevEntryQuality.md` is absent from
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/w1/` and exists at
`/home/vgpnk/Projects/shokunin/.ufo/waves/round-75/w1/RevEntryQuality.md` (fleet root, 96 lines). Its own
transcript (`history://RevEntryQuality`) records `mkdir -p /home/vgpnk/Projects/shokunin/…` after failing to find
the lane wave directory, so the fleet write is that seat's, not mine. Consequence: every wave-2 entry seat was
pointed at a lane path that does not resolve. My read was read-only; the fleet file should be moved/relinked by the
L1, and no one should grade from the fleet copy without noting where it lives.

**W2-2 (HIGH, entry family) — the S885 evidence window and the sibling's §7 disagree.** The staged
`reports/round-75/evidence/S885.txt` has `window-scope: whole-document`, `visible-chars: 3720`, and its quote is the
notice's opening sentence (printed p. 1). The staged `-23b` entry's §7 asserts the opposite ("the window holds one
page — printed p. 5"). One of the two must change before freeze: either the S885 evidence is re-pointed to
`T1_0005_0000`, or the `-23b` sentence is corrected. My file states the staged state and names the condition under
which it stops being true, so it stays true under either fix.

**W2-3 (HIGH, rows) — three `used-by` cells do not match the entries that cite them.** From
`…/assimilation/validate/corpus/SOURCES.md`:

- `S885` lists the base entry and `…amend-2026-10-23.md`, but `…amend-2026-10-23b.md` also carries a `source: S885`
  line — the cell is missing the third citing entry.
- `S891` and `S892` each list `…amend-2026-10-23.md`, which cites **neither** document; the citing file is
  `…amend-2026-10-23b.md`.

The ROWS leg requires `used-by` to be exactly the admitted entries whose `source:` lines cite the row, so as staged
these three cells fail it. (My file is not the fix site: rows belong to the executor seats.)

**W2-4 (MEDIUM, rows → entries) — the S886 scope cell asserts content the entry does not and cannot cite.** The cell
names "the relation between the characters' words and the narrator's, and the level of appreciation each part of a
story carries". The w1 scribe could not locate either phrase on pp. 139–141 as paraphrased; the character/narrator
relation is on printed p. 141, which the row does not name among its pages, and no page read supports "level of
appreciation … each part". A scope cell that overstates the entry is a review defect the counter cannot see
(ENTRIES is shape-only). Either the cell is trimmed to the entry's actual ground (temporality and the
time/aspect/mode cut) or the entry gains a p. 141 row.

**W2-5 (LOW, hygiene) — my scratch directory disappeared mid-run.** At 16:56 the directory
`/fast/scratch/hyaku/kotodama-r75/ScribeEntryAmend23Final/` was gone while sibling seat directories under the same
root survived; the tree was recreated and every URL re-fetched (pass 2, §2). Nothing citied in this report pointed
at the lost copy; the page-level hashes are identical across passes. Worth knowing if another seat's cleanup uses a
broad glob.

## 6. Out of scope for this seat (untouched)

Registry rows and their cells, `id-renumber-map.json`, Gate records and evidence windows, `corpus/README.md` index
rows and footers, `corpus/lessons/round-75.md`, `claims.json`/`ledger.json`, both counters, controls, fixtures,
commits. The sibling entry `-23b` and the base entry were read only (the base entry is staged by another seat; at
the time of writing only `-23b` existed under `w2/stage/corpus/knowledge/myth-symbol/`).

## 7. Scratch and artifacts

Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeEntryAmend23Final/` (fetch bodies, `verify.py`) is removed before
yield; the receipts above are the fetch table and hashes in this file, not a scratch path. No `/tmp` path is cited
anywhere.

Artifacts:

- `.ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md`
  — sha256 `25992609cdb303353dbbb60b98a03abd01d56d1ec7349ceddcc365c429a8a717`
- `.ufo/waves/round-75/w2/ScribeEntryAmend23Final.md` (this report)
