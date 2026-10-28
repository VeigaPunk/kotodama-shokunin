# ExecCapEvidence — round-77 wave 2: D2/S898 capture on the real live+Wayback pair

Seat: `ExecCapEvidence` (executor, leaf). Lane: `kotodama-shokunin`, base
`211f9526800906e0c585d878d265c37e5e090c15`. Assigned: run the new capture tool
on the actual D2 live/capture pair in scratch, emit a candidate `S898` evidence
file under my stage dir only, and make it record the 5-word Gate quote, the
17-word attributed anchor *with its folded status*, journal p. 114 / PDF p. 4,
and a window that reaches p. 4 — with `verify_file` returning OK.

Verdict: **evidence produced and graded OK; one assigned fact is not recordable
by the tool as written.** The capture runs, both candidates pass `verify_file`
(exit 0), the window is byte-reproducible (`window-sha256 fb65bae1…` matches the
W1 §5b run), and every claim the draft makes about the D2 spans is
independently reproduced — except that **the anchor's folded status is not a
field in the receipt**: the tool computes the anchor's tier, never emits it, and
`verify_file` does not grade a match tier for either span. The plain candidate
therefore contains the string `folded` zero times. A second candidate records
the folded status in `locator:` prose (the only free-text slot), which is
recorded but ungraded. Exact tool delta recommended in §7.

## Artifacts (all under my stage dir; no lane production file touched)

`<stage>` = `.ufo/waves/round-77/w2/stage/ExecCapEvidence/`

```
capture-evidence.py        used in place from W1, sha256 bab5ca44f78540059b07f22c1ee2254ae310075c865355841b24c0d49030f8b5
claims-rehearsal.json      W1 rehearsal capture block, sha256 3a313fb69443c348982432e61add3b4e1ec294bf770ace17b236496a65047a34
S898-candidate.txt         plain locator, id S898, sha256 ca709825b8d000f2ce8892ef2f5d1a98f7ab04d3043215ce7612cbd3d7d03f4d
S898-candidate-anchorfolded.txt  same capture, locator carries the anchor's folded status, id S898,
                                 sha256 c2e42f72816978fb80b42cce0a50e14cb20f211f695c63ea2819361a78c44cda
capture.log                        first capture run (plain locator), exit 0
capture-anchorfolded.log           second capture run + its verify, exit 0
verify-final.log                   final verify of both candidates + digests + window equality
verify-and-mutations.log           verify + 4 header mutations
verify-probes2.log                 3 further mutations (verbatim flag, anchor flag, stored quote)
verify-scout-s898.log              round-77 verify of W1's stage/ScoutDocS898/evidence.txt
measure-s898.py / measure-s898.log independent span/tier/page measurement (imports the tool's own locate())
anchor-linebreak.log               raw extraction slice at the anchor, both extraction modes
page-map.log                       PDF page -> printed journal folio map
```

Tool digest is the W1 file: `sha256sum` printed
`bab5ca44f78540059b07f22c1ee2254ae310075c865355841b24c0d49030f8b5`. The lane has
no installed `tools/capture-evidence.py` and the whole `.ufo/waves/round-77/`
tree is untracked (`git status --porcelain` → `?? .ufo/waves/round-77/`), so the
tool is identified here by digest only.

## 1. Capture run (plain, claims-draft locator)

```
$ python3 -B <tool> --claims-file <stage>/claims-rehearsal.json --id S898 \
    --url 'https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/' \
    --wayback-url 'https://web.archive.org/web/20260901045105id_/https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/' \
    --quote 'there were altogether 88 terms' \
    --anchor-quote 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees' \
    --find 'According to Kałużyńska (2008, pp. 223, 232)' \
    --locator '§3 first paragraph, second sentence, journal p. 114 / PDF p. 4' \
    --out <stage>/S898-candidate.txt --work /fast/scratch/hyaku/kotodama-r77/ExecCapEvidence
EVIDENCE S898: quote-found=yes verbatim=yes anchor-in-window=yes window-source=live live-http=200 wayback-http=200 wayback-same-page=yes memento=Tue, 01 Sep 2026 04:51:05 GMT bytes=417093 sha256=5d1bfa5a5f01bee6 window-chars=4098 window-scope=excerpt window-sha256=fb65bae17dc50fe3 find-page=4 -> <stage>/S898-candidate.txt
VERIFY OK: … window-sha256=fb65bae17dc50fe3c3b25b1ebe234e024fdb501819314a253a93ee18717e52a5 window-bytes=4384 window-chars=4098 quote-in-window=yes anchor-in-window=yes window-source=live wayback-same-page=yes wayback-memento=Tue, 01 Sep 2026 04:51:05 GMT
ACCEPT-C-77: CAPTURE OK: … claims-frozen=no
exit=0
```

Both fetches answered 200 with **identical bytes**: `live-sha256` = `wayback-sha256`
= `5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc`,
417093 bytes each (re-checked outside the tool: `curl` on both URLs into scratch,
`sha256sum d2-live.pdf d2-wb.pdf` printed that digest twice). The draft's
"(byte-identical to the live PDF in W1)" holds for the cited capture.

## 2. Standalone `verify_file` on the candidate

```
$ python3 -B <tool> --claims-file <stage>/claims-rehearsal.json --verify <stage>/S898-candidate.txt \
    --quote 'there were altogether 88 terms' \
    --anchor-quote 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees'
VERIFY OK: <stage>/S898-candidate.txt window-sha256=fb65bae17dc50fe3c3b25b1ebe234e024fdb501819314a253a93ee18717e52a5 window-bytes=4384 window-chars=4098 quote-in-window=yes anchor-in-window=yes window-source=live wayback-same-page=yes wayback-memento=Tue, 01 Sep 2026 04:51:05 GMT access-date=2026-10-27 http-status=200
exit=0
```

Same result for `S898-candidate-anchorfolded.txt` (exit 0, identical window
digest). The two files differ only in the `locator:` line; their stored windows
are the same string (`window-A sha256` = `window-B sha256` =
`fb65bae1…`, `identical: True`).

## 3. What the candidate records (the four assigned facts)

```
$ grep -E '^anchor|^quote-found|^normalise|^locator' <stage>/S898-candidate.txt
quote-found: yes
quote-found-verbatim: yes
anchor-quote: According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees
anchor-quote-chars: 111
anchor-quote-words: 17
anchor-found: yes
anchor-in-window: yes
anchor-char: 10433
anchor-page: 4
locator: §3 first paragraph, second sentence, journal p. 114 / PDF p. 4
normalise: NFKC(per-character)+whitespace-fold; matched=verbatim
```

plus the file's `quote-words: 5`, `quote-chars: 30`, `quote-page: 4`,
`find-page: 4`, `find-hits: 1`, `page-count: 13`, `window-pages: 3..5`,
`quote-in-anchor: yes`, `quote-anchor-distance: 46`, `anchor-in-window: yes`.

Date pairing: `fetched: 2026-10-28T02:10:26Z` (UTC) with `access-date: 2026-10-27`,
which is the local date at capture (`date '+%F %T %z'` → `2026-10-27 23:10:45
-0300`); the tool refuses an `--access-date` other than the claims' date, so the
recorded pair is by construction and matches round 76's committed files.

- 5-word Gate quote: `there were altogether 88 terms` — `quote-words: 5`,
  `quote-found-verbatim: yes`, `matched=verbatim`.
- 17-word attributed anchor: the span above, `anchor-quote-words: 17`,
  `anchor-quote-chars: 111`, found at char 10433 with the 5-word quote 46 chars
  into it (`quote-anchor-distance: 46`).
- p4/114: `quote-page: 4`, `anchor-page: 4`, `find-page: 4`, locator names
  journal p. 114 / PDF p. 4.
- window reaches p. 4: `window-pages: 3..5` with `quote-page: 4` inside it.

**Folded status: absent.** `grep -c 'folded' <stage>/S898-candidate.txt` → `0`.
The receipt carries the anchor's presence and position, never its match tier.
The `anchor-matched`/`anchor-found-verbatim` key does not exist in the grammar
(`R76_KEYS`/`R77_KEYS` in the tool list `anchor-quote`, `anchor-quote-chars`,
`anchor-found`, `anchor-in-window` only), and `anchor_hit["tier"]` is computed by
`locate()` but read nowhere in the tool (`grep -n 'anchor_hit\[.tier.\]\|anchor_hit\[.verbatim.\]'`
→ no match).

## 4. Independent measurement of the assigned facts

`measure-s898.py` imports the tool's own `fold()/locate()/folded_has()` and
extracts both fetched PDFs with `pdftotext -enc UTF-8` (the tool's mode) and with
`-layout` (the mode W1's scout file says it used). `measure-s898.log`, identical
for the live and the capture PDF:

```
quote5   tier=verbatim verbatim=True form=NFKC start=10479 page=4  verbatim_occurrences=1 verbatim_pages=[4]
anchor17 tier=folded   verbatim=False form=NFKC start=10433 page=4 verbatim_occurrences=0 verbatim_pages=[]
find     verbatim=True tier=verbatim start=10433 page=4
page4_head "114\n\nIrena Kałużyńska\n\nLiu (1996, p. 46) stated: “Flowers, plants and trees are "
page4_chars 2678   page_chars [2896, 3188, 2721, 2678, 3201, 2240, 2304, 2333, 2217, 1896, 2377, 2868, 2758, 0]
anchor_in_stored_window=True quote_in_stored_window=True quote_in_anchor=True
```

`-layout` gives the same verdicts (quote `verbatim` once on p. 4; anchor `folded`,
0 verbatim occurrences; locator verbatim on p. 4). The line break is real in both
modes — `anchor-linebreak.log`:

```
== extraction: pdftotext -enc UTF-8 (default) ==
raw slice repr: 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms\ndenoting plants, flowers and trees (general terms, species or the parts of flowers '
newline inside the 17-word span: True
== extraction: pdftotext -enc UTF-8 -layout ==
raw slice repr: 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms\ndenoting plants, flowers and trees (general terms, species or the parts of flow-\ner'
newline inside the 17-word span: True
```

So the draft's D2 statement is **confirmed as written**: Gate quote verbatim and
unique on journal p. 114 / PDF p. 4; anchor folded only ("not claimed verbatim"
is correct) and also on p. 4.

Page-folio mapping from the document itself (`page-map.log`):

```
pdf page  1 | https://doi.org/10.17651/ONOMAST.69.7 Onomastica LXIX, 2025 PL ISSN 0078-4648 IRENA KAŁUŻY…
pdf page  2 | 112 Irena Kałużyńska …
pdf page  4 | 114 Irena Kałużyńska Liu (1996, p. 46) stated: …
pdf page  5 | FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA  115 data: …
…
pdf page 13 | FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA 123 He, X. 何, 晓明. (2001). …
```

PDF p. 4 prints "114" in its running head and p. 5 prints "115", so the capture's
`quote-page: 4` ↔ journal 114 is read off the document. Page 1 carries no printed
folio (title page: DOI, `Onomastica LXIX, 2025`, CC BY-ND line), so the article's
first journal page (111 by arithmetic) is not printed anywhere — which matters
below because W1's scout file claims "journal pp. 112–124".

## 5. Falsification probes (mutations go to scratch copies, never the stage files)

`verify-and-mutations.log` / `verify-probes2.log`, all against the same claims
block:

| mutation | verify result |
|---|---|
| `locator:` prose changed to `journal p. 115 / PDF p. 5` | **VERIFY OK, exit 0** |
| `quote-page: 4` → `quote-page: 5` (still inside `window-pages: 3..5`) | **VERIFY OK, exit 0** |
| `quote-found-verbatim: yes` → `no` (receipt now disclaims the verbatim match) | **VERIFY OK, exit 0** |
| `anchor-found: yes` → `no` | VERIFY FAIL, exit 5 (`anchor-found 'no' (want yes)`) |
| stored `--- quote ---` block changed to an absent span | VERIFY FAIL, exit 5 (`quote absent from the stored window after NFKC+whitespace fold`) |
| `anchor-quote` changed `88 terms` → `89 terms` | VERIFY FAIL, exit 5 (`the anchor span is absent from the stored window after NFKC+whitespace fold (R75-M2)`) |

Raw lines of the three permissive probes:

```
== var-locator: locator prose says journal p. 115 / PDF p. 5 ==
VERIFY OK: var-locator.txt … exit=0
== var-quotepage: quote-page forged 4 -> 5 (inside window-pages 3..5) ==
VERIFY OK: var-quotepage.txt … exit=0
== var-verbflag: quote-found-verbatim flipped yes -> no ==
VERIFY OK: var-verbflag.txt … exit=0
```

R77 verify of W1's `stage/ScoutDocS898/evidence.txt` (`verify-scout-s898.log`):
`ACCEPT-C-77: VERIFY FAIL … (49 problem(s))`, exit 5 — missing 37 round-77/76
keys (`anchor-quote`, `window-source`, `wayback-url`, `response-bind-live`,
`quote-page`, …), `access-date '2026-10-28' (want 2026-10-27)`,
`user-agent is not browser-shaped: 'curl/8.23.0'`,
`window is 2116 characters (want >= 4096 for an excerpt)`, `PDF evidence lacks
'find'`, `window-pages None is not a..b`.

## 6. Findings on the named item (attack)

**F1 (material, blocks the assigned wording).** The receipt cannot record the
anchor's folded status: no such key exists and `verify_file` grades no match tier
for either span. Evidence: the plain candidate holds zero occurrences of
`folded`; `R77_KEYS` has no anchor-tier key; mutation "quote-found-verbatim
yes→no" still verifies OK. Consequence: the claims draft's parenthetical
"(folded across a PDF line break, not claimed verbatim)" is prose only — nothing
in `reports/round-77/evidence/S898.txt` will distinguish this receipt from one
asserting a verbatim 17-word span. That is exactly the shape of W1's scout file,
which asserts `normalise: whitespace-fold (PDF line-wrap only); matched=verbatim`
for the 17-word span; my measurement refutes it at both extraction tiers
(0 verbatim occurrences, `tier=folded`).

**F2 (material).** Because no tier is graded, `verify_file` OK does **not**
establish "verbatim" for the Gate quote either. The 5-word span is in fact
verbatim and unique on p. 4 (measured), but the receipt's `quote-found-verbatim:
yes` is self-declared: flipping it to `no` still exits 0. A counter that needs
the Gate quote verbatim must recompute the tier from the fetched body (as
`measure-s898.py` does), not read the flag.

**F3 (material).** The page facts are self-asserted and only range-checked.
`quote-page`/`anchor-page`/`find-page` are graded solely as integers inside
`window-pages`; a forged `quote-page: 5` passes. The locator's "journal p. 114 /
PDF p. 4" is free text — rewriting it to "journal p. 115 / PDF p. 5" passes. So
"p4/114" is checkable only by recomputation (`--find` → page, running head →
journal folio), which is what `measure-s898.log` and `page-map.log` do.

**F4 (operational).** "window p4" cannot mean `window-pages: 4..4` under the
frozen grammar: `min_window` is 4096 and PDF p. 4 is 2678 characters
(`page_chars` above), so an `excerpt` window must span p. 3–5 (measured
`window-pages: 3..5`, `window: chars=4098 … before=2071 after=1997`). It is
satisfied as "the window covers p. 4 and both cited spans are on p. 4"
(`quote-page: 4`, `anchor-page: 4`, `find-page: 4`). A counter written to demand
`window-pages == 4..4` would be unsatisfiable against the current capture
constants.

**F5 (do not install).** W1's `stage/ScoutDocS898/evidence.txt` is not a
round-77 receipt (49 verify problems) and its `matched=verbatim` claim for the
17-word span is false at both extraction tiers. Its "journal pp. 112–124" is also
off by one: p. 5 prints 115 and p. 13 prints 123, so the body is pp. 111–123
(p. 1 carries no printed folio). The entry text must not inherit either statement.

**F6 (handoff).** The candidate is not install-as-is: it carries
`claims-frozen: no` (`claims-source: file:…/claims-rehearsal.json`) because
`reports/round-77/claims.json` does not exist yet (`ls reports/round-77/` →
`telemetry`). At the freeze the same argv with `--repo . --freeze <rev>` must be
re-run so the receipt says `claims-frozen: yes`. Re-running is safe: the stored
window is byte-stable across runs — my run's `window-sha256 fb65bae1…` equals the
W1 §5b run's digest.

## 7. Recommendation before freeze

1. Run the S898 capture at freeze with the §1 argv plus `--repo . --freeze <rev>`
   (and `--out reports/round-77/evidence/S898.txt`). Keep `--quote` at the 5-word
   span and `--anchor-quote` at the 17-word attributed sentence — that is the
   pair that makes both spans land on PDF p. 4 with `quote-in-anchor: yes`.
2. Either install the tool unchanged and accept that the folded status lives only
   in prose (record it in this round's Gate/search log and in the entry's
   evidence note), **or** land this two-line additive delta in
   `capture-evidence.py` before freeze and re-emit:
   - emit after `anchor-char:`: `anchor-matched: <hit["tier"]>` and
     `anchor-matched-form: <hit["form"]>` (values `verbatim` /
     `folded` / `folded-no-space`, form `NFKC`/`NFKD`), from the
     document-level `bind["anchor_hit"]` already computed in
     `__init__` (`locate(text, anchor)`; the window-level
     `locate(window_text, bind["anchor"])` at ~1277 yields the same tier);
   - in `verify_file()`, after the `anchor-in-window` check, require
     `anchor-matched:` to be present and to equal the stored anchor's tier as
     recomputed from `folded_has`/verbatim probe of the window — i.e. refuse a
     receipt that claims `verbatim` for a span the window only holds folded
     (the scout-file defect, made checkable).
   The grammar stays additive (round-76 readers ignore new keys), and the delta
   has a failing scenario available for free: W1's scout file.
3. Feed the counter (EVIDENCE leg) these recomputable facts: quote tier and
   uniqueness, anchor tier, `find-page` = page of the locator, and the printed
   folio on `quote-page` — none of which `verify_file` grades (F1–F3).

## 8. Scope, risks, cleanup

- Wrote only `<stage>/…` and this report. No lane production file, no
  `reports/round-77` content, no `corpus/`, no registry, no git/jj index. No
  fixture git repo was needed (the tool ran with `--claims-file`); nothing in
  `/fast/scratch` used a relative path.
- Scratch `/fast/scratch/hyaku/kotodama-r77/ExecCapEvidence` (PDFs, mutation
  copies, tool work dir) is deleted at the end of this seat.
- Risk if ignored: an `S898` receipt promoted as-is would be
  `claims-frozen: no` (F6), and a Gate that reads "folded" or "verbatim" off the
  receipt rather than recomputing it would grade a claim the file does not carry
  (F1/F2) — the routed r76 defect class.
- Blocker encountered: none. The one unmet assigned wording (folded status in
  the file) is a tool-grammar gap, evidenced above, with both a stopgap artifact
  and the durable fix specified.
