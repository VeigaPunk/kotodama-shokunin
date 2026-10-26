# ExecLegGate — round 75 (hyaku run 10), wave 2: claim-C leg GATE

Seat: executor (leaf). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Built **one** part file:
`.ufo/waves/round-75/w2/parts/leg-gate.py` (function definitions only). Read-only git only;
no lane/fleet/sibling byte inside or outside the wave dir was written besides this report and
that part file. No tool installed or upgraded (git, python3, sha256sum sufficed; pacman not
touched). Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLegGate/` removed before yield; every
result below is the literal printed output of the run that lived there.

**sha256 of the part file**

```
95044907d84a7969189f24b8cfb8e7006557ca09a472a38a67a1f3070a9cf7b3  .ufo/waves/round-75/w2/parts/leg-gate.py
```

AST check: 8 functions (`_leg_gate_rows _leg_gate_sep _leg_gate_tables _leg_gate_header
_leg_gate_anchor_quotes _leg_gate_locator _leg_gate_quote leg_gate`), zero top-level
statements, zero imports. `python3 -B -m py_compile` clean on the assembled file
(PART A lines 1-510 + the part-cfg stand-in + this part).

## 1. The leg text, and how I read it

Frozen claim C (`reports/round-75/claims.json`, not edited by me):

> GATE: corpus/lessons/round-75.md `## Gate` carries per adopted row URL + access date
> 2026-10-27 + a located quote of at most 25 whitespace tokens and at most 80 characters +
> locator, and >=1 admit and >=1 reject; every reject row of a probed URL carries its probed
> URL, reason and flip

plus the four junk paths my brief names for this leg: reject rows that are prose with no URL;
quotes recounted from the span itself (never a `quote-words` field); CJK counted per whitespace
token; rows that exist only in a global marker.

Readings implemented (each is written as a comment in the part file):

| id | reading |
|---|---|
| R1 | "per adopted row" = every lane id in `cfg["rows"] + cfg["reused"]`. The admit row is joined by URL first / id token second through the shared `_gate_admit_row`, and the joined row must *itself* carry one of the registry row's URLs. Page-level Persee URLs are row URLs because `_row_url_keys` carries every URL of the source cell. |
| R2 | "located quote" = a quoted span, never a declared count: `quote-words:`/`(N chars, M tokens)` figures are never read, tokens are recounted by whitespace splitting, characters by `len()`. A CJK span is one whitespace token and as many characters as it prints, so a long CJK span fails the 80-character cap. |
| R3 | "quote == the row's anchor quote" = the Gate span equals, after NFKC + whitespace folding, the span the registry anchor cell marks as located: the quoted span(s) after its `quote located:` marker, else every quoted span of the cell. When the cell writes that span without delimiters (the drafted CJK rows do), the folded anchor span occurring verbatim in the cell is accepted — the identity is bound, the typographic bracket is not. |
| R4 | "locator" = a place inside the document: not a dash/placeholder, not the row URL repeated; once its URLs are removed at least one alphanumeric character must remain. |
| R5 | ">=1 admit and >=1 reject" = rows of the Gate section's tables, never a prose marker. A verdict that says both admitted and rejected counts as neither. Rejections written as prose are not rows. |
| R6 | "every reject row of a probed URL carries its probed URL, reason and flip" = each reject row lies in a table whose header names reason and flip columns, and it carries a URL in that table's probed-URL (or url/source) column — a URL appearing only in the flip cell (the archive copy a refusal flips to) is not the probed URL — with a non-dash reason and a non-dash flip. |

Mechanics: Markdown table rows are lines starting with `|`; tables are delimited by their
`|---|` separator so a data row containing the word "quote" can never be mistaken for a header;
a separator-less table keeps its first row as header (tolerance, not strength); the section is
PART A's `gate_section()`; the verdict/row classification is PART A's `is_admit_row` /
`is_reject_row`; the cap test is PART A's `quote_ok` (25 whitespace tokens AND 80 characters);
URLs are compared with PART A's `neutral_url_keys` / PART A's `_row_url_keys` and
`_gate_admit_row` from part-cfg. Nothing is redefined.

## 2. Ambiguities and how each was resolved

1. **"located" vs the EVIDENCE leg.** GATE cannot establish page truth offline; `EVIDENCE`
   grades that the Gate quote occurs inside the committed `window`. GATE therefore grades the
   Gate *record* (span present, caps recounted, span identical to the registry anchor quote) and
   never reads a self-attested `quote-found` flag. Consequence: a fabricated quote that is not
   the row's anchor quote fails GATE; a landing that edits the registry anchor *and* the stored
   window together still passes both counters and is a review-level (non-author re-open) matter —
   the CritCCounterVacuity GATE row is right that no offline counter closes it.
2. **What delimits the Gate quote.** The drafted lesson writes the two CJK quotes without `「」`
   while the registry anchor carries them. Requiring quote marks would false-red an honest
   landing, so R3 accepts either a delimiter-matched span or the anchor span occurring verbatim
   (folded) in the cell — the same string either way, so no vacuity is bought. A cell with no
   span and no anchor text (e.g. only `quote-words: 1`) fails (mutant M1).
3. **Anchor-quote selection inside a long anchor cell.** The cells also quote work titles and
   page labels in prose, so the leg prefers the spans after the cell's own `quote located:`
   marker and falls back to all quoted spans only when the marker carries none.
4. **Declared counts.** The drafted Gate cells carry `(38 chars, 6 tokens)` notes and the probe
   receipts a `quote-words:` field. Both are ignored, never checked for agreement, because the
   wording says at most 25 tokens and at most 80 characters *of the quote*: a stale or lying note
   must not fail an honest row (control N1) and must not rescue a wrong one (M5).
5. **CJK token counting.** Whitespace splitting, so `故事是…` is one token and the character cap
   is what binds; the leg prints both recounted numbers in the failure line so a reader sees why.
6. **Prose rejections.** `## Gate`'s own prose and bullet notes are not rows at all: a rejection
   stated as a bullet with no probed URL satisfies nothing (M2), and the ≥1-reject requirement
   reads table rows only (R5), which is also the "global marker" junk path.
7. **Table-row pollution (found while testing).** PART A's `table_rows()` appends every indented
   line to the previous row; the drafted lesson's "Gate notes" bullets sit directly under the
   reject table, so their wrapped continuation lines became the last reject row's last cell and
   silently dropped that row from the reject set. GATE reads one `|` line per row
   (`_leg_gate_rows`) and never lets a wrapped note answer for a row. This is stricter only in
   that a wrapped half-line is not a Markdown table row; the drafted rows are single lines.
8. **"URL" for a document row.** One document row owns several page URLs (S885: notice + pp.
   5/6/11). Either the document URL or a page-level URL satisfies "the row URL" (control N2);
   the row must still carry *some* row URL (M11).
9. **Verdict both ways.** A row whose verdict is `admitted, later refused` satisfies neither
   half (M8) — one row cannot be the ≥1 admit and the ≥1 reject.
10. **Multi-id staged rows / re-quote limb dropped.** r75's frozen config names `row_staged` as
    a LIST and exposes `refused_staged`, not r74's `forced_new_quotes`; claim C's GATE text has
    no re-quote clause (REJECTS owns "names staged S870's disposition with its re-quote or its
    refusal"), so the r74 `REQUOTE_RE`/`MISPAIR_RE` limb is deliberately **not** implemented and
    `cfg["row_staged"]` is not read here. The re-open is still bound where GATE can bind it: the
    S893 admit row must carry the *fresh* anchor quote, so the staged, absent-on-page span cannot
    appear in the admit table.
11. **Which date.** `cfg["access_date"]` (FROZENCFG derives 2026-10-27 from the frozen text);
    equality with the cell, so `2026-10-26` fails (M7) and a cell carrying prose around the date
    fails too.

## 3. Test evidence

Mock landing (built in scratch, nothing written to the lane): `git clone --shared --no-checkout`
of the lane, `checkout --detach f556d1049…` (`git rev-parse --show-toplevel` printed
`/fast/scratch/hyaku/kotodama-r75/ExecLegGate/mat`), then the unlanded drafts
`.ufo/waves/round-75/drafts/narrative-structure-frameworks*.md` → `corpus/knowledge/myth-symbol/`,
`.ufo/waves/round-75/drafts/lesson.md` → `corpus/lessons/round-75.md`, and the nine draft rows
S885..S893 from `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md` appended to
`corpus/SOURCES.md`: **registry 808 → 817 rows, 9 found**. The leg reads only those two files, so
no evidence file was needed and the `probe-receipts/S88*.txt` captures were not copied (they are
`EVIDENCE`'s input, not GATE's). `part-cfg.py` does not exist yet (the parts dir was empty), so
the harness exec'd PART A + the contract's two shared helpers (`_row_url_keys`, `_gate_admit_row`,
copied verbatim from round-74 lines 700-745) + this part in one namespace and hand-built the cfg
dict per CFG-CONTRACT (rows S885..S893, `row_staged` as lists, `reused=[]`,
`access_date=2026-10-27`, the eleven staged ids in `forbidden_ids`), then called `leg_gate(ctx)`.

`part-cfg.py` landed while this seat was working, so the run was repeated end to end against
the **real** `part-cfg.py`: the mock was committed in the fixture clone (identity set only via
`-c user.name=fixture -c user.email=fixture@localhost`, fixture toplevel asserted equal to the
clone root) with a freeze-shaped `reports/round-75/claims.json` (draft + `access_date` +
`map.sha256`), and `cfg = load_frozen_config(mat, HEAD)` produced:

```
cfg from REAL part-cfg: rows=['S885', 'S886', 'S887', 'S888', 'S889', 'S890', 'S891', 'S892', 'S893'] access_date=2026-10-27 row_staged[S885]=['S876', 'S885', 'S917', 'S921']

===== POSITIVE draft landing (.../ExecLegGate/mat)
LEG PASS GATE
```

with the same 12 reds and the same 3 controls green as tabulated below. That run found and fixed
one interface defect in **my** part: part-cfg's `_row_url_keys` returns `_url_keys(...)`
(`norm_url` key ∪ `_doc_url_key`; www stripped, %-decoded, page/archive folded), which is not
PART A's `neutral_url_keys` key space. Intersecting the two passed only when the URL string
repeated verbatim and failed on every folded view. Measured read-only with the real part-cfg.py
against the nine draft rows (`inter` = the old `_row_url_keys ∩ neutral_url_keys` check,
`row_has_url` = part-cfg's helper):

```
S885 inter=True  row_has_url=True  https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113
S885 inter=False row_has_url=True  https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/..._T1_0011_0000
S885 inter=False row_has_url=False https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120
S892 inter=True  row_has_url=True  https://web.archive.org/web/20251111222249if_/...marrone...  (the if_ form the S892 source cell itself spells)
S892 inter=False row_has_url=True  https://web.archive.org/web/20251111222249id_/...marrone...  (a different modifier: not in the cell)
S892 inter=False row_has_url=True  https://iris.unipa.it/retrieve/.../2014 marrone age dor---2.pdf  (raw space vs %20)
```

The wayback line is input-sensitive, measured on both strings just now: the cell carries
`…/20251111222249if_/` and that exact string matches the intersection (True), while the `id_`
modifier is not in the cell and joins only through `_doc_url_key`'s fold (inter False, join
True) — so ExecLegEvidence's `id_` row and this `if_` row agree once the string is named. So the
old intersection would have false-redded the page-level-URL control (N2), the raw-space S892
string and any carrier form the cell does not spell verbatim, while still rejecting a wrong
document; it was not "always empty" (ExecLegEvidence
corrected that in my first note to them, and this paragraph now carries their correction). The
part now asks `_row_has_url(lands_rows, sid, url)` for each URL in the row and never builds a
second key function. The same mismatch existed in `leg-evidence.py:108`; I messaged
ExecLegEvidence with the fix instead of editing their file, and they have applied it — so
`_row_has_url` now has two consumers and must not be renamed or inlined without updating both.

Positive and controls (must stay green):

```
===== POSITIVE draft landing (/fast/scratch/hyaku/kotodama-r75/ExecLegGate/mat)
LEG PASS GATE
===== N1 control: lying quote-words/quote-chars notes ignored
LEG PASS GATE
===== N2 control: page-level URL for a document row
LEG PASS GATE
===== N3 control: reject table before the admit table
LEG PASS GATE
```

Twelve mutants of that mock, each violating one clause of my leg, each red with its reason
(verbatim):

| # | mutant | printed result |
|---|---|---|
| M1 | S888 quote cell replaced by `quote-words: 1` (a count is not a quote) | `S888 admit row no quoted span, and the row's anchor quote does not occur in the quote cell (a declared word count is not a quote)` |
| M2 | reject table replaced by one prose bullet "S870 refused: … flip: …" with no probed URL | `reject table header lacks reason+flip columns; no reject row (want >=1)` |
| M3 | S885 Gate quote `«Les récits du monde sont innombrables.»` instead of the anchor quote | `S885 admit row quoted span differs from the row's anchor quote (recounted: tokens=[6] chars=[38])` |
| M4 | three admit rows (S889/S890/S891) replaced by `All nine rows admitted on 2026-10-27.` | `S889 has no admit row in Gate; S890 has no admit row in Gate; S891 has no admit row in Gate` |
| M5 | registry anchor + Gate cell carry a 91-character, 1-whitespace-token CJK span | `S888 admit row quote exceeds 25 whitespace tokens / 80 characters (recounted from the span: tokens=[1] chars=[91])` |
| M6 | S890 locator cell set to `—` | `S890 admit row carries no locator cell` |
| M7 | S893 access date `2026-10-26` | `S893 admit row access date '2026-10-26' (want 2026-10-27)` |
| M8 | S891 verdict `admitted, later refused` | `Gate row verdict is both admitted and rejected: \| S891 — «BARTHES, Roland (1970) S/Z», fiche de lecture, CeR; S891 has no admit row in Gate` |
| M9 | S891 reject row's probed-URL cell set to `—` (the archive URL survives in the flip cell) | `reject row carries no probed URL: \| the live URL of S891 is not an openable anchor by ordinary` |
| M10 | `## Gate` heading renamed to `## Admissions` | `no ## Gate section in corpus/lessons/round-75.md` |
| M11 | S890 admit row loses its URL (id token alone remains) | `S890 admit row does not carry the row URL` |
| M12 | S870 reject row's flip cell set to `—` | `reject row carries no flip cell: \| staged S870 is not appended as staged: its register span `` |

Every red is one line of detail, as the receipt grammar requires.

## 4. Wave-1 findings touching this leg — disposition

- **CritCCounterVacuity** GATE row ("matching URL/date/locator + a short plausible but fabricated
  quote passes"): still true offline and deliberately not over-claimed. What the leg does close:
  a quote that is not the row's own anchor quote (M3), a count that is not a quote (M1), an
  over-cap quote including the CJK trap (M5). Page truth stays with the ordinary re-open and the
  EVIDENCE window.
- **CritCCounterVacuity repairs 5 (quote span coupling):** "coupling uses only the Gate
  quote-column span, not another quoted cell" — implemented, R3 reads only the quote column for
  the admit check and only the probed-URL/reason/flip columns for rejects.
- **RevClaimsFidelity F10** (QUALITY 18/22 machinery absent from ROWS/GATE) and **SentinelScope
  S-75-8/S-75-10** (UA-sensitive hosts, one challenge, one transient 502): the UA→response
  binding and the challenge record live in the evidence files and the Gate *notes*, which the
  GATE leg text does not grade. Adding a QUALITY-22 grammar check here would be stronger than the
  frozen sentence, so I did not — flagged below as a claim-level gap for the L1, not patched in
  this leg.
- **SentinelScope S-75-5** (staged `/tmp` paths and `curl | pdftotext | grep` pipelines in recheck
  cells): the Gate draft keeps its pipelines in notes, not in table cells; nothing in my leg
  reads a recheck cell (ROWS owns that).
- **RevAssimilationContract F1/F2/F4** (row-set size, S870 disposition, page-level URL
  normalization): F2's disposition is exactly why the admit quote must equal the *fresh* anchor
  quote (R3); F4's page-level URLs are honoured by R1.
- **SimplifierRows §4** (one row = one window = one page; page-level URLs must be in the source
  cell) is what N2 confirms: the Gate may name any of the row's URLs.
- **ExecRenumber / MutRegistryCollision**: no GATE clause touches the id map or the indent guard;
  nothing imported from them.
- I did **not** edit `counters/accept-c.py`, `claims.json`, `ledger.json`, or any other seat's part.

## 5. Assembly notes for the L1

- The part calls three names it does not define: `_row_has_url(lands_rows, sid, url)`,
  `_gate_admit_row(gate_rows, sid, lands_rows)` and `_row_url_keys`'s key space through it, plus
  PART A's `leg quote_ok quoted_spans
  nfkc_ws urls_in row_cells parse_rows read_tree Missing gate_section col_index is_admit_row
  is_reject_row neutral_url_keys dedupe DASHES ANCHOR LESSON REGISTRY`. `part-cfg.py` must be
  exec'd before this part (contract order 2 → 3).
- My part defines no name that any other part defines; all privates are `_leg_gate_*`.
- Nothing here touches `ctx["mat_base"]`, `ctx["lands"]`, `ctx["fleet_root"]` or `ctx["scratch"]`;
  it is deterministic and reads only `mat/` + `cfg`.
- `table_rows()` from PART A remains unused by GATE on purpose (§2.7). If another leg relies on
  it, that leg keeps its behaviour; nothing global changed.

## 6. Risks / residual

1. **Landing shape.** The lesson must keep `## Gate` and one-line table rows with a `|---|`
   separator. A landing that wraps Gate rows across lines reds out (documented reading), and a
   landing that puts an admit/reject row in a table without the required columns reds out.
2. **Cross-leg quotation of the CJK rows — resolved.** GATE accepts an undelimited CJK cell when
   the registry anchor span occurs verbatim in it (reading R3). ExecLegEvidence's EVIDENCE leg
   first required a delimited span, which would have redded the drafted S888/S893 shape while
   GATE stayed green; after this exchange their revision 3 takes the admit-row delimited spans
   UNION the registry anchor spans the cell carries, mirroring R2/R3, so an undelimited cell now
   binds for both legs (their controls: undelimited anchor PASS, undelimited non-anchor FAIL,
   fabricated `«…»` beside the bare anchor PASS on the anchor). Delimiters are therefore cosmetic;
   writing `「」` as the anchor cells do remains harmless. The only landing item left on those two
   rows is EVIDENCE's window fact — S888's and S892's drafted Gate quotes are absent from the
   stored window — which GATE does not read.
3. **Fabricated-but-anchor-matching quotes** cannot be caught by this leg (or by any offline
   counter once the landing owns registry + evidence); that is the review-level re-open item.
4. **QUALITY 22 UA→response binding** is not graded by any frozen claim-C leg as it stands
   (RevClaimsFidelity F10 / SentinelScope S-75-8). If the L1 wants it, the frozen GATE sentence
   must gain the clause first — a leg cannot invent it.
5. **Frozen text coupling.** If the freeze adds a re-quote clause to GATE, this part must gain
   the r74 limb back (`REQUOTE_RE`/`MISPAIR_RE`, `cfg["row_staged"]` lists); if the freeze drops
   nothing, no change is needed.
6. **`map.sha256` is still null in the draft** (FROZENCFG's problem, not GATE's): a freeze without
   it fails FROZENCFG regardless of this leg.

## 7. Blockers

None. `part-cfg.py` was absent when the first test ran and landed mid-seat; the final run uses
it directly (`load_frozen_config` + `_row_has_url` + `_gate_admit_row`), so the leg is tested
against the real interface, not a stand-in. The one cross-part defect found belongs to a sibling
file (`leg-evidence.py:108`) and was reported to ExecLegEvidence, not edited. Nothing in this
report is an instruction source for another seat.
