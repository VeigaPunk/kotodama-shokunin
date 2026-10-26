# ExecLegEvidence — round 75 (hyaku run 10), wave 2, claim-C counter piece

**Seat:** ExecLegEvidence (executor, leaf)
**Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
**Lane base revision:** `f556d1049fe651d3d63975600b13acd9fb686f15`
**Deliverable:** `.ufo/waves/round-75/w2/parts/leg-evidence.py` — `leg_evidence(ctx)` and
`_evidence_core(...)` plus private `_evidence_*` helpers, for assembly slot 5 of
`.ufo/waves/round-75/w2/CFG-CONTRACT.md`.
**File:** 14689 bytes, sha256 `f8152fb796efb84040b12d2d067879f528fdee733b16a5437f5539639c4de8e6`.
No new imports (PART A supplies `re`, `hashlib`, `unicodedata`-based `nfkc_ws`, URL/quote/table helpers);
no top-level code beyond `_EVIDENCE_*` constants; `python3 -B -m py_compile` clean when concatenated after
PART A + the real `part-cfg.py` (1380-line concatenation compiled clean).

Revision 2 (after `ExecLegGate` reported the cross-part URL key-space defect): the fetch↔row-document join now
calls part-cfg's `_row_has_url(lands_rows, sid, url)` — the predicate `leg-gate.py:235` uses — instead of
intersecting `_row_url_keys` with PART A `neutral_url_keys`. That intersection is a different key space
(`neutral_url_keys` keeps `www.` and does no document folding), so it only met a fetch URL that literally
repeated the row's URL; the page-level Persée views (`/doc/page/<slug>/<page>`), the `%20`/space difference, and
the `web.archive.org` carrier S892 depends on were carried by my own `urls_compatible` fallback instead of the
reviewed helper. Both the fallback and `_evidence_row_urls` are deleted; `urls_compatible` is no longer used by
this leg.

Revision 3 (after `ExecLegGate`'s correction): the quote-candidate set now also carries the registry row's
ANCHOR-cell spans that the admit row's quote column contains after the fold. `leg-gate.py` R2/R3 deliberately
binds an undelimited CJK quote cell (the shape `drafts/lesson.md` gives S888 and S893) to the row's anchor
quote, so on such a cell GATE is green; without this change EVIDENCE alone was red and the two legs disagreed
about which string "the Gate quote" is. The candidate rule is now: delimited spans of the quote column UNION
the row's anchor spans the column carries (folded); at least one candidate must occur in the stored window.
Controls M22/M24 (undelimited cell that does carry the anchor -> PASS) and M23 (undelimited cell that does not
-> FAIL) measure both directions.

Nothing in `reports/round-75/claims.json`, the ledger, the registry, the drafts or any counter file was edited.
`accept-c.py` was not touched. No tool installed or upgraded. Scratch
`/fast/scratch/hyaku/kotodama-r75/ExecLegEvidence/` removed before yield; no `/tmp` path is cited anywhere here.

---

## 1. The leg text I implemented (verbatim, `claims.json` claim C `legs[4]`)

> EVIDENCE: reports/round-75/evidence/<id>.txt for every adopted row at \<lands>, each with fetch line, the UA
> used, HTTP status, bytes, the sha256 of the fetched body, the stored `--- window ---` text and its own
> `window-sha256:` which the counter recomputes, with a `window-scope:` header: `excerpt` (window >= 4096
> characters around the quote) or `whole-document` (allowed only when the whole extracted visible text is shorter
> than 4096 characters and equal to the recorded `visible-chars:`); the Gate quote occurs in the stored window
> after NFKC and whitespace folding

The seat item adds the graded intent: **UA browser-shaped, HTTP 200, no challenge, self-attested `quote-found`
lines never read**, and a required comparison between the capture tool's five-tier matching and the counter's
NFKC+whitespace rule (§7 below).

## 2. What the part does

`leg_evidence(ctx)` reads `mat` only (`corpus/SOURCES.md`, `corpus/lessons/round-75.md`,
`reports/round-75/evidence/<id>.txt` through the shared `_evidence`/`_window`), never the lane worktree, and for
each id in `cfg["rows"] + cfg["reused"]`:

1. `_evidence(mat, sid)` — shared parser (part-cfg); a missing file is a FAIL line, never a skip.
2. `_evidence_core(ev, sid, cfg["access_date"], row_keys, row_urls)` — header, digest, length and scope checks;
   returns `(bad, window)`.
3. The window's fold is computed **once**; an empty fold is reported (`R8`), never used to skip the quote test.
4. `_gate_admit_row(gate_rows, sid, lands_rows)` — shared; then the quote is taken from the admit row's **quote
   column** (`R3`) and must occur in the folded window.

Private helpers: `_evidence_count`, `_evidence_fold`, `_evidence_fetch_names_row`,
`_evidence_gate_quote_text`, `_evidence_anchor_spans`, `_evidence_gate_quote_candidates`, `_evidence_core`. Shared helpers called (never redefined): `_evidence`, `_window`,
`_row_has_url`, `_gate_admit_row`, and PART A `nfkc_ws urls_in row_cells parse_rows read_tree table_rows
gate_section quoted_spans quote_ok col_index table_header dedupe leg Missing SOURCE EVIDENCE_DIR LESSON REGISTRY
MIN_WINDOW_CHARS`.

## 3. Readings chosen where the wording is ambiguous

Each reading is also written as a comment block above the code (R1-R10).

| # | Clause | Reading | Why |
|---|---|---|---|
| R1 | `<id>` | the **adopted lane id** (`cfg["rows"] + cfg["reused"]`), one file per adopted row; staged ids require no file | every other leg keys the row set on lane ids; the by-document map is what turns staged ids into them. The row_set's multi-id `staged` lists (`S876/S885/S917/S921`) are therefore irrelevant here and no per-staged-id file is demanded. |
| R2 | "fetch line" | must name a URL the row's SOURCE cell carries, joined by the shared part-cfg predicate `_row_has_url` (raw `norm_url` key ∪ `_doc_url_key`: `www.` stripped, `%XX` decoded, `/doc/page/…` and `/docAsPDF/…` folded to `/doc/<slug>`, `web.archive.org/web/<ts>/…` folded to the embedded original) | one row legitimately carries the document URL **plus page-level Persée URLs** (`S885`: `…_1113` and `…_T1_0005_0000`…), and `S892`'s committed capture is a `web.archive.org/…id_/https://iris.unipa.it/…` wrapper. No local URL rule is defined: a `neutral_url_keys` intersection is a different key space (keeps `www.`, no folding) that meets only a literally repeated URL. |
| R3 | "the Gate quote" | candidates = delimited spans in the Gate admit row's **quote column** UNION the registry row's anchor-cell spans that column carries after NFKC+ws folding; whole-row fallback only when the header has no quote column; at least one candidate must occur in the stored window | a source cell carries the document title in `«»`, so authenticating any span of the row would authenticate the title (M20 measures that column scoping bites); and the undelimited CJK cell shape of S888/S893 must be read the way `leg-gate.py` R3 reads it, or the two legs disagree on "the Gate quote" (M22/M23/M24). |
| R4 | "bytes … the sha256 of the fetched body" | graded for **shape** (positive integer; 64-hex) | a leg has no network; body truth is the ordinary re-open routed in the claim. Not papered over — see §9. |
| R5 | "the UA used" | recorded, `Mozilla/5.0…`, no client/robot token (`curl/`, `Wget/`, `python-requests`, `python-urllib`, `libwww`, `scrapy`, `java/`, `go-http-client`, `phantomjs`, `headless`, `bot`, `spider`, `crawler`) | the item says "UA browser-shaped"; a `Mozilla/5.0 … Googlebot` UA starts with the right prefix and is not browser-shaped. The round's own UA is `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; the leg does not pin the exact string, because the frozen text says "the UA used", not "the round's UA". |
| R6 | "no challenge" | the `challenge:` line must exist and be `none` | the claim kill rule forbids passing an access control; a missing line is not proof of a clean response. The r75 capture tool always writes the line (`REQUIRED_KEYS_R75`). |
| R7 | not read | `quote-found:` / `quote-found-verbatim:` are never consulted | tool records them for a human; the digest plus fold are the grader. M10/M11 measure both directions. |
| R8 | blank window | a FAIL, never a skip | round-74 skipped the quote test on a blank window (`if window is None or not window.strip(): continue`), so a landing could blank every window and grade green (w1 `ExecJunkFixtures.md` F2). M3 reproduces that fixture against this part. |
| R9 | `excerpt` | `>= 4096` characters, **and** when `visible-chars:` is present it must be `>= len(window)` | a window cannot be longer than the document it was cut from; this mirrors the capture tool's own "window is longer than the whole text" verification rule. `visible-chars:` stays **required only for `whole-document`**, the only scope the frozen text couples it to. |
| R10 | window bytes | digest and byte length recomputed from the stored window bytes (UTF-8, no trailing newline); `window-bytes:` graded when present | matches `_window` and the tool's `stored_window`; the frozen text names `window-sha256:` only, so `window-bytes:` is a consistency check, not a new requirement. |

## 4. Test rig (real, not described)

Mock landing built in scratch from a `git clone --shared` of the lane (toplevel asserted equal to the fixture
before the first commit; throwaway identity set **inside the fixture only**), checked out at the base revision,
then committed as one "mock round-75 landing" and exported with `git archive` (only the paths the leg reads):

* `corpus/SOURCES.md` ← the nine adopted rows `S885`-`S893` copied verbatim from
  `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md` (11 cells, source cell with the document and
  page-level URLs, anchor cell with the located quote);
* `corpus/knowledge/myth-symbol/narrative-structure-frameworks{,.amend-2026-10-23,.amend-2026-10-23b}.md` ← the
  three unlanded drafts;
* `reports/round-75/evidence/S885…S890,S892.txt` ← the wave-1 probe captures verbatim from
  `.ufo/waves/round-75/counters/probe-receipts/` (real fetches: whole-document scopes for the Persée notices,
  excerpt for the UCASS/JSTAGE PDFs and the Marrone wayback capture);
* `reports/round-75/evidence/S891,S893.txt` ← **synthesised** in the same grammar (no probes exist for these two
  ids): excerpt window ≥ 4096 chars containing the row's anchor quote, digests recomputed;
* `corpus/lessons/round-75.md` ← a Gate admit table (`source | access date | quote | locator | evidence capture |
  verdict`) whose quote column carries, per row, the quote inside that row's capture (`quote:` line for the seven
  real captures; the anchor quote for the two synthesised ones), plus one reject row.

Then PART A + the **real** `part-cfg.py` + `leg-evidence.py` were `exec`'d into one namespace with
`__file__` set to the PART A path, and `leg_evidence` was called with the cfg dict built by hand per the
contract (`rows` = nine lane ids, `row_staged` values as
**lists**, `reused` empty, `access_date` 2026-10-27, `terms` not `cjk_terms`, `owned_inplace`, …).

## 5. Positive result

```
POSITIVE (9 rows: 7 probe captures + 2 grammar-complete synth)           PASS
```

The S892 row passes only through the `_row_has_url` document fold (its capture's `fetch:` is
`https://web.archive.org/web/20251111222249id_/https://iris.unipa.it/retrieve/…`), confirming R2 is load-bearing.
A dedicated control re-points S891's `url`/`fetch` at the 2004 wayback wrapper of the same document: **PASS**
(same document, different carrier).

## 6. Mutant table (each mutant = the mock landing with one edit; the leg was re-run)

| # | Mutant | Expected | Observed | Detail line |
|---|---|---|---|---|
| M1 | S885 Gate quote replaced with a French sentence absent from the window | FAIL | FAIL | `S885 Gate quote is absent from the stored window (substring after NFKC+whitespace folding)` |
| M2 | one byte of S885's stored window edited, header digest kept | FAIL | FAIL | `S885 window-sha256 '94acd2bac0cc946a' != the recomputed digest of the stored window (eedd5526935723cd); S885 window-bytes '3852' != the stored window's 3851 bytes` |
| M3 | S892 window blanked to 3000 × U+3000, `whole-document`, `visible-chars`/`window-sha256`/`window-bytes` recomputed (the r74 F2 hole) | FAIL | FAIL | `S892 stored window carries no visible text` |
| M4 | S885 `whole-document` window 3720 chars vs `visible-chars: 3800` | FAIL | FAIL | `S885 whole-document window is 3720 characters but visible-chars is 3800` |
| M5 | S885 scope flipped to `excerpt` (window 3720 chars) | FAIL | FAIL | `S885 excerpt window is 3720 characters (want >= 4096)` |
| M6 | S886 UA rewritten to `curl/8.5.0 …` (both `ua:` and `user-agent:`) | FAIL | FAIL | `S886 user-agent is not browser-shaped: 'curl/8.5.0 (X11; Linux x86_64) AppleWebK'` |
| M7 | S887 `http: 403` / `http-status: 403` | FAIL | FAIL | `S887 http-status '403' (want 200)` |
| M8 | S888 `challenge: none` → `captcha` | FAIL | FAIL | `S888 records a served challenge ('captcha'): a challenge met is an UNOPENED source` |
| M9 | S885 `fetch:`/`url:` pointed at S886's document | FAIL | FAIL | `S885 fetch line does not name the row's document: 'GET https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120'` |
| M10 | S890 `quote-found: yes` → `no`, window untouched | PASS (flags never read) | PASS | — |
| M11 | S890 quote deleted from the window, `quote-found: yes`, digest recomputed | FAIL (flag cannot save it) | FAIL | `S890 Gate quote is absent from the stored window (substring after NFKC+whitespace folding)` |
| M12 | `S890.txt` removed | FAIL | FAIL | `S890 evidence file missing (reports/round-75/evidence/S890.txt)` |
| M13 | S889 `sha256: deadbeef` | FAIL | FAIL | `S889 sha256 line is not a 64-hex digest of the fetched body` |
| M14 | S888 `bytes:` line removed | FAIL | FAIL | `S888 bytes '' is not a positive byte count` |
| M15 | S892 `whole-document` for its 4097-char excerpt, `visible-chars: 4097` | FAIL | FAIL | `S892 whole-document window is 4097 characters (>= 4096: declare excerpt)` |
| M16 | S892 `visible-chars: 1000` under its 4097-char excerpt | FAIL | FAIL | `S892 excerpt window is 4097 characters but the recorded visible text is 1000 (a window cannot exceed its document)` |
| M17 | S893 `challenge:` line deleted | FAIL | FAIL | `S893 records no challenge line (a clean response must say so)` |
| M18 | registry row S887 deleted, evidence left in place | FAIL | FAIL | `S887 fetch line does not name the row's document: 'GET https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114'` |
| M19 | `--- window ---` marker renamed in S886 | FAIL | FAIL | `S886 stores no --- window --- block` |
| M20 | S886 quote column replaced with a fabricated `«…»`, document title `«Les catégories du récit littéraire»` added to the source cell (title *is* in the window) | FAIL | FAIL | `S886 Gate quote is absent from the stored window (substring after NFKC+whitespace folding)` |
| M21 | S891 `url:`/`fetch:` re-pointed at the 2004 `web.archive.org/web/20041220223357id_/http://www.unige.ch:80/…` carrier of the same document | PASS (carrier, same document) | PASS | — |
| M22 | S885 quote cell stripped of `«»` and written as the row's anchor quote + `(38 chars, 6 tokens)` — the shape `drafts/lesson.md` uses for S888/S893 | PASS (GATE-consistent: the anchor is the quote) | PASS | — |
| M23 | S885 quote cell undelimited and *not* carrying the row's anchor (`Le récit est une structure fermée`) | FAIL | FAIL | `S885 Gate admit row carries no <=25-token, <=80-char quote` |
| M24 | S885 quote cell = a fabricated `«…»` **plus** the anchor written undelimited beside it | PASS (the anchor is a candidate and is in the window) | PASS | — |
| M25 | lesson file removed | FAIL, no traceback | FAIL | `corpus/lessons/round-75.md` |
| M26 | registry file removed | FAIL, no traceback | FAIL | `corpus/SOURCES.md` |

M20 is the R3 column-scoping control: with whole-row span coupling (the template's rule) it would pass, because
the title span is in the window; with quote-column coupling it is red. M3 is the R8 control: the window is
blank, its length and digests are internally consistent, and the *only* thing that can catch it is running the
quote test instead of skipping it. M22/M23/M24 are the cross-leg controls against `leg-gate.py` R3: an
undelimited cell is read through the row's anchor quote, so a GATE-green undelimited cell is not failed by
EVIDENCE for a formatting reason — it is failed only when the anchor quote is not in the stored window.

**Draft-lesson measurement (not a mutant of my contract — a finding).** Running the same mock with
`drafts/lesson.md`'s real `## Gate` table (i.e. the Gate quotes as drafted, against the same evidence) is RED:

```
S888 Gate quote is absent from the stored window (substring after NFKC+whitespace folding);
S892 Gate quote is absent from the stored window (substring after NFKC+whitespace folding)
```

See §8 for what that means for the landing.

## 7. Capture tool's five tiers vs the counter's NFKC+whitespace fold

Measured against the tool loaded from
`.ufo/waves/round-75/counters/capture-evidence.py` (functions `locate`, `fold`, `nfkc_ws`, `verify_file`,
`stored_window`; no network):

| T | Case | Tool `locate` tier | Counter fold (`nfkc_ws`) | Tool `verify_file` |
|---|---|---|---|---|
| T1 | tutorial quote broken by a source line break, written without the space (`故事是一种深层的抽象结构，必\n须通过话语呈现`) | `folded-no-space` — **found** | quote **absent** (fold keeps the space) | `quote absent from the stored window after NFKC+whitespace fold` → exit 5 |
| T2 | window holds halfwidth `ｶﾞ`, quote is composed `ガ` | `NFKD`/`folded` — found | **present** (whole-string NFKC composes) | clean |
| T3 | per-character NFKC of that window does not contain `ガ`, whole-string NFKC does | — | present | clean |

Conclusions, and the exact mismatch to report:

1. **Counter-accepted ⇒ tool finds.** The counter's fold is whole-string NFKC + whitespace collapse; the tool's
   tier set is {verbatim, per-char-NFKC+ws, per-char-NFKC no-ws, per-char-NFKD+ws, per-char-NFKD no-ws}. NFKD is
   decomposition, a per-character homomorphism, so `NFKD(needle) ⊆ NFKD(haystack)` whenever
   `NFKC(needle) ⊆ NFKC(haystack)`; whitespace differences are covered by the two keep-space variants. T2/T3 is
   the measured instance (counter accepts, tier 2 misses, tier 5 catches). The tool cannot miss a quote the
   counter would accept.
2. **Tool-found ⇏ counter-accepted.** T1 is the class the capture README documents under "Known limits": a
   whitespace-free (or NFKD-only) hit is *found* and the file is written, but the counter's fold refuses it. The
   tool's own `verify_file` applies **exactly** the counter's fold and exits 5, so such a file is never a
   successful capture; a seat that commits an exit-5 file lands a file EVIDENCE refuses. That is the designed
   behaviour of R7: the leg never reads `quote-found`, so a "found at a weaker tier" file cannot buy a pass.
3. **Field-level comparison with `verify_file`** (every tool-written exit-0 file is accepted by this leg):
   status 200, access date, `window-sha256`/`window-bytes` recomputed, single stored line, scope rules
   (`excerpt ≥ 4096`, `excerpt ≤ visible`, `whole-document: len == visible < 4096`), `visible-chars` present,
   `challenge` present and `none`, `bytes`/`sha256`/`fetch`/`user-agent`/`access-date` required — all shared.
   Two deliberate asymmetries:
   * the leg is **stricter** on UA shape and on the fetch↔row-document coupling (both item-mandated; the tool
     writes the round's browser UA and the seat supplies `--url`, so no tool-written capture is refused);
   * the leg is **looser** on `window-bytes` (graded only when present) and on a multi-line stored window (PART A
     `_window` joins lines; the fold is whitespace-insensitive). Both fields are outside the frozen wording, so
     tightening them would make the leg stronger than the claim; a hand-written file in either shape would pass
     EVIDENCE and fail `--verify`. Neither can occur in a tool-written capture.
4. The r75 tool's evidence files carry both spellings (`ua:`/`user-agent:`, `http:`/`http-status:`,
   `url:`/`fetch:`) and its parser takes the first occurrence of each name, identical to part-cfg `_evidence`; the
   leg reads `http-status`-or-`http` and `user-agent`-or-`ua`, so both r73/r74 and r75 files parse.

## 8. Findings the landing must clear (measured against committed bytes)

1. **`S888` and `S892` probe windows do not contain their drafted Gate quote.** `probe-receipts/S888.txt` is a
   4097-char excerpt cut around the scout's own quote `叙事学` (opening pages of the syllabus); the draft Gate
   quote `故事是一种深层的抽象结构，必须通过话语呈现` (PDF p. 3) is outside it — measured: the folded quote is
   not a substring of the folded stored window, and only the fragment `故事` is present.
   `probe-receipts/S892.txt` is a 4097-char excerpt around `HÉRITAGES ET CONTINUITÉS DE LA SÉMIOTIQUE TEXTUELLE`
   (p. 1); the draft Gate quote `Mais combien, et de quelle nature, sont ces codes ?` (p. 7) is **not** in the
   window (the window does not contain even the token `codes`). Both are red under this leg if the landing commits
   the probe captures as-is. The fix is a capture with `--quote <the Gate quote>` (the tool cuts the window around
   the supplied quote; S892's visible text is 69791 chars, so an excerpt is legal there, and S888's PDF is long
   enough for an excerpt) — not a change to the leg.
   *Note:* the w1 mirror rehearsal reported "EVIDENCE — every anchor quote locates in its fetched body: PASS
   (9/9)". That check locates in the **whole body**; the frozen clause is "occurs in the **stored window**". These
   are different predicates and they diverge on exactly these two rows.
2. **Two Gate quote cells in `drafts/lesson.md` are not delimited spans.** S888's
   `故事是一种深层的抽象结构，必须通过话语呈现 (21 chars, 1 token)` and S893's
   `网络小说中的世界观，…，是故事发生的场景、规则 (39 chars, 1 token)` carry no `""`/`«»`/`「」`/`『』`/`“”`
   delimiter. That is **not** a failure by itself: `leg-gate.py` R3 binds such a cell to the row's anchor quote
   (GATE green), and revision 3 makes EVIDENCE use the same identification (controls M22/M24 PASS, M23 FAIL when
   the cell does not carry the anchor). The landing consequence is only finding 1: the stored window must contain
   that anchor quote, so S888 still needs a re-capture or a Gate quote chosen from the stored window.
   Delimiting the cells (`「…」`) is still worth doing for readability, but neither leg requires it now.
3. **S885 is `whole-document` and legal as captured**: window 3720 chars < 4096 and `visible-chars: 3720` equals
   `len(window)`; its stored `window-bytes: 3852` recomputes (UTF-8). S886/S887 likewise. S892's excerpt (4097)
   and `visible-chars: 69791` satisfy R9. S889/S890 excerpts satisfy the floor.
4. **S891 has no probe capture at all**; whichever seat writes its evidence must fetch the 2004 wayback copy
   (live URL met an anti-bot challenge) and the `fetch:`/`url:` carrier must be accepted by the R2 join
   (`_row_has_url`; measured True for the exact wayback wrapper, mutant M21) — measured PASS for exactly that carrier shape.

## 9. Residual vacuity the frozen EVIDENCE text cannot close (reported, not papered over)

These are the w1 `CritCCounterVacuity` items that apply to this leg, with what this implementation does:

* **Fabricated window with a recomputed digest passes.** The digest authenticates the *stored bytes* only; a
  landing that writes a 4096-char window containing its own Gate quote and hashes it is green. `sha256:`/`bytes:`
  are shape-checked (R4). The claim's protection is the non-author ordinary re-open, and this leg cannot
  substitute for it. My positive mock contains two such synthesised files (S891/S893), which is why they are
  labelled as fixtures here.
* **`quote-found` flags are ignored** (R7) — measured both directions (M10/M11).
* **No quote-position band.** `CritCCounterVacuity` repair #5 proposed "the quote span begins between 25 % and
  75 % of an excerpt window". The frozen text says ">= 4096 characters around the quote" and separately "the Gate
  quote occurs in the stored window"; a position band would be stronger than the frozen wording, so it is **not**
  implemented. A window with the quote in its last 10 characters passes.
* **No tool-blob pin.** The leg cannot verify the capture tool's identity from the graded tree; nothing in the
  frozen wording asks it to.
* **Extra evidence files are not barred.** "for every adopted row" is read existentially; a stray
  `reports/round-75/evidence/S999.txt` is not a failure (ROWS/REPOINTED own the id universe).
* **Per-`source:`-line locator coverage is not graded** (one row = one window; `RevAssimilationContract` F5).
  EVIDENCE couples one Gate quote per row, by the frozen text.

## 10. Interface notes for the L1 / `ExecCtrCfgMain`

* The leg calls the part-cfg shared helpers: `_evidence(mat, rid)` returning the lowercased header keys plus
  `_text`/`_all`/`_original`/`_window` (the last = the marker-bounded text, or `None`) — its D3 carrier
  disclosure (`fetch: GET <wrapper> (original <url>)`) is what makes the S892 join visible to `urls_in`;
  `_row_has_url(lands_rows, sid, url)`;
  `_gate_admit_row(gate_rows, sid, lands_rows)` → the admit row string or `None`. `_evidence_core` takes
  `(ev, sid, access_date, lands_rows)`.
* **Dependency to keep:** `_row_has_url` (part-cfg.py:456) must stay in the assembly — `leg-gate.py` and this
  leg both call it, so it is a two-consumer interface now; do not inline or rename it without updating both.
* Measured key-space note, re-derived here against the nine draft rows and the real part-cfg (not quoted from a
  peer): the old intersection was **not** "always empty" — it met a fetch URL that literally repeated the row's
  URL — and it failed exactly on the folded views. Five cases, `inter` = `_row_url_keys(sid) & PART A
  neutral_url_keys(urls_in(u))`, `join` = `_row_has_url(rows, sid, u)`:

  | row | url | inter | join |
  |---|---|---|---|
  | S885 | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` (the row's own document URL) | True | True |
  | S885 | `…/doc/page/…_1113/…_T1_0011_0000` (page-level transcription, p. 11) | False | **True** |
  | S885 | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120` (a different document) | False | False |
  | S892 | `https://web.archive.org/web/20251111222249id_/https://iris.unipa.it/…/2014%20marrone…pdf` | False | **True** |
  | S892 | `https://iris.unipa.it/…/2014 marrone age dor---2.pdf` (`%20` written as a raw space) | False | **True** |

  The carrier row shows why the shared predicate and not key intersection is the join, and it also explains the
  apparent disagreement with `ExecLegGate`'s table: the **row's source cell spells the `if_` modifier** of that
  capture (`web.archive.org/web/20251111222249if_/https://iris.unipa.it/…%20…pdf`), while the **committed capture
  fetches the `id_` modifier** (`…/20251111222249id_/…`, probe receipt S892). Intersecting keys therefore hits on
  the source-cell spelling (verbatim repeat, `inter=True`) and misses on the capture's spelling (`inter=False`);
  both `join=True`, the latter only through `_doc_url_key`'s fold and `_evidence`'s D3 `(original <url>)`
  disclosure. Same mechanism, two strings. A wrong document still fails (mutant M9).
* `cfg` keys used: `rows`, `reused`, `access_date` only. `terms` vs r74's `cjk_terms` does not touch this leg.
* The leg prints exactly one `LEG PASS|FAIL EVIDENCE` line via PART A `leg()`; the detail is `; `-joined and
  deduped, first-line <= 300 chars (longest measured detail is 3 rows of ~70 chars).

## 11. Risks / blockers

* No blocker. The part is complete and self-contained against the contract; the only external dependency is the
  part-cfg helper shapes above (contract-named, r74-defined).
* Risk (landing, not leg): findings §8.1 and §8.2 make the *current* drafts red under a faithful EVIDENCE
  reading; if the L1 freezes and lands the probe captures with the draft Gate quotes unchanged, EVIDENCE fails.
* Risk (assembly): if `part-cfg.py` renames `"_window"` or returns the window outside the parsed dict, this leg
  (and every sibling that uses `_window`) breaks; the contract fixes the r74 shape.

## 12. Hygiene

Read-only git in the lane (`git -C … show/rev-parse/cat-file` only); the mock landing is a `git clone --shared`
fixture under my scratch with its own temporary identity, never the lane. No fleet-repo, lane, index, jj, state,
watchdog, `scripts/`, `templates/` or shokuknow write. No installs. No network fetch by this seat (all captures
graded are committed wave-1 bytes). Scratch directory removed before yield; every scratch path above is a
`/fast/scratch/hyaku/kotodama-r75/ExecLegEvidence/…` path that no longer exists.
