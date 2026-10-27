# Round 75 — staged narrative-entry admission review

Scope: staged base plus four amendments under `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/`; DRAFT claims/ledger only. This is an admission review, not an edit. Severity reflects admission impact. Source opening performed only by plain `curl` requests; no challenge was passed or routed around in this review.

## Findings

### F1 — HIGH — Campaign IDs in an adopted amendment resolve to unrelated lane rows

`narrative-structure-frameworks.amend-2026-10-23.md:11` cites `round 3's S744` in the proposed gap-filled text. The same campaign ID appears in the staged `23b` at line 12 and `23c` at lines 12–13 (`S744`, `S763`). The adopted `23` file alone therefore contains a hidden campaign citation. At lane base `f556d1049fe651d3d63975600b13acd9fb686f15`, registry IDs S860–S884 already exist; S744/S763 are within the existing lane namespace as well, so copying them into the entry would resolve to unrelated lane documents, not the campaign documents. This violates the claim kill rule against unrelated-document IDs and the REPOINTED/document-identity requirement.

**Fix:** replace `S744` with the lane ID for the Barthes 1966 document (claim row-set maps that document to S885), and `S763` with the mapped lane ID for the Greimas article (S887); normalize every campaign round/ID reference in prose. Extend REPOINTED to verify every cited ID's frozen row URL matches the claim it supports, not merely that an ID resolves or falls in a checked numeric range.

### F2 — HIGH — S870 has no by-document mapping, yet the base passage cites it

The base file cites S870 in its source list, recheck line, and practitioner-register section (§8). The claims row-set maps S864→S888, S865→S889, S866→S890, S876→S885, S902→S886, S904→S887, S905→S891, S919→S892, and folds S885/S917/S921 into S885. S870 is the sole staged source ID not mapped; claims explicitly say it remains refused unless re-quoted this round. Its sole supported content in the entry is the practitioner `世界观` claim. If refused, that claim has no source and the `S870` citation cannot remain. The by-document map file was not present at the specified fleet path when checked; claims also have `map.sha256: null`, so actual map coverage is not yet verifiable (the mapping above is only the draft row-set).

**Fix:** if S870 remains refused, remove §8, all S870 citations, and its recheck reference; if re-opened/admitted, add the row, Gate quote, evidence window, used-by and map record before freeze. Commit a non-null map digest and verify the map against all staged IDs before freezing.

### F3 — HIGH — Staged lines fail criterion 15 as written

Ran lane `tools/check-cited-lines.py` over unmodified scratch copies of all five staged files. Four fail with `MULTI-ID`: base file line 34 (`S864,S865,S866,S870`); amendment 23 line 7 (`S902,S904`); amendment 23c line 12 (`S744,S763`); amendment 24 line 7 (`S919,S921`). Amendment 23b reports zero findings. These are multi-ID recheck/ground lines, not table-row findings. The claims CITEDLINES leg requires `CITED-LINES: 0 finding(s)`.

**Fix:** replace each entry's campaign-command recheck header with a cadence-only recheck value without IDs (as the claims ROWS leg already requires for registry rows); split any remaining multi-source factual clauses into one cited ID per line. Re-run the lint on final entry bytes before admission.

### F4 — HIGH — The row-set fold collapses four distinct Barthes locators into one evidence quote/window

The draft maps staged Barthes IDs S876, S885, S917, S921 to a single lane row S885, although the staged locators support materially different claims: opening framing, p.5/p.26 levels and readings, p.11 functional classes, and p.6's three-level enumeration. The draft ROWS/GATE/EVIDENCE legs require one anchor quote per row and an evidence window around that quote; the excerpt window cannot record all those separate page passages. If the selected anchor is not the quote for a cited claim, the entry's locator is unsupported by the committed evidence window; if it is, the other staged quotes are omitted from the round record.

**Fix:** before freeze, either retain separate source rows for the distinct page-level claims, or explicitly identify the single anchor quote and restrict/phrase entry claims so the committed evidence window supports them; do not silently treat four staged quotes as one evidenced quote. At minimum, use the p.6 three-level quote as the anchor if the three-vs-four-level issue is retained, and make the other page-specific claims conditional on independently recorded locators/windows.

### F5 — HIGH — Pending amendments have dangling `couples:` targets

The four required base targets exist at lane base: `myth-symbol/comparative-frameworks.md`, `myth-symbol/hero-journey-variants.md`, `culture-material/era-periodization-models.md`, and `culture-material/heritage-taxonomy-models.md`. However, adopted amendment 23 names `culture-material/era-periodization-models.amend-2026-10-23.md`; claims list the era-periodization amendments among refused/pending files. Amendment 23b names `culture-material/era-periodization-models.amend-2026-10-23b.md`, also pending. Amendment 24 names `linguistics/naming-systems.amend-2026-10-24.md`, also pending. If those amendments are refused, these targets will not exist in the lane. The claims ENTRIES leg checks header shape but not target existence.

**Fix:** point amendment 23 to the existing `culture-material/era-periodization-models.md`; for 23b/24 either couple to existing lane files or admit the named target in the same landing. Add a review/check that every `couples:` path exists at the materialized lands tree.

### F6 — HIGH — Amendment 23b misstates four unit classes as four 1966 “levels”

Amendment 23b's topic and proposed §N+1 call `fonctions, actions, indices, informants` the 1966 article's “four levels.” But staged amendment 24 quotes the article's own p.6 enumeration as `trois niveaux de description` and names `fonctions, actions, narration` (S921); staged 23c identifies noyaux/catalyses/indices/informants as *classes* of units (S917). The proposed “four levels” formulation conflates levels and unit classes, and contradicts the staged primary quote. If 23b is adopted, readers receive both counts as claims about the same article.

**Fix:** in 23b replace “four levels (functions, actions, indices, informants)” with “three levels (functions, actions, narration); the four unit classes (noyaux, catalyses, indices, informants) are a separate classification,” citing the appropriate mapped rows. Keep the scholarly “en partie” qualification in 24 rather than the unqualified “reworking” language in 23b.

### F7 — MEDIUM — The frozen eight-row set conflicts with conditional amendment admission and exact `used-by`

Claims freeze eight appended rows, including S891 (S/Z excerpt, staged S905) and S892 (Marrone, staged S919). Those staged sources are cited only by pending amendments 23b and 24 respectively; claims say those files are adopted only if every cited document opens with a located quote, otherwise refused. If either is refused while the row-set remains eight, its row has no admitted citing entry, yet the ROWS leg requires `used-by` exactly the admitted entries that cite it. The draft does not state whether zero `used-by` is legal or whether the row disappears.

**Fix:** make S891/S892 row membership conditional on 23b/24 admission before freezing, or make the final adoption decision before data and give each row a non-empty exact `used-by`. Do not freeze both the unconditional eight-row set and conditional entry set.

### F8 — MEDIUM — Calibration status required by QUALITY 2 is absent

None of the five staged files names the framework's status as mainstream, contested, or discredited with a reason. “Calibration key” and “Calibration limits” in the proposed outlines concern source authority/limits, not the framework's scholarly status. The claims ENTRIES field-shape list does not include calibration, so the counter does not establish this review requirement.

**Fix:** add a concise in-body calibration statement, e.g. classical structuralist narratology is a historically influential descriptive framework; its categories are useful for formal specification but are contested as universal/exhaustive accounts of narrative. Scope each status claim to its supporting source and do not treat the Japanese/Chinese examples as proof of independent intellectual development.

### F9 — MEDIUM — “arrived at independently” overstates the evidence

Base file proposed §N says Chinese and Japanese theories make the same levels-of-description move “arrived at independently.” The cited syllabus/papers support descriptions of those theories, but the staged material supplies no source establishing independent historical development or absence of transmission. Amendment 23's safer phrase says the traditions are “converging ... from a different direction,” which also avoids asserting historical independence.

**Fix:** replace “arrived at independently” with “a comparable move appears in the cited Chinese and Japanese sources” (or mark the independence claim `(to-verify)` and omit it from the design rule).

### F10 — MEDIUM — Round/campaign-local source pointers are unresolved in the lane

The entries refer repeatedly to `CANNOT-ANSWER.md` and `SOURCES-PROPOSED.md` and to “round 1/2/3…” campaign artifacts. Neither `CANNOT-ANSWER.md` nor any `SOURCES-PROPOSED` file exists in the lane base tree. Cadence-only recheck normalization is already required by the claims, but the `ground:` prose and proposed-body links remain dangling and are not checked by ENTRIES.

**Fix:** replace those pointers with lane-local, committed references (for example the round-75 Gate/lesson once landed) or rewrite the ground statement as the durable corpus gap; remove campaign chronology that is not needed for the reference method.

### F11 — MEDIUM — Proposed outlines are not yet a usable worldbuilding entry

The staged files mostly name sections to write, including “Boundary table,” the three time axes, the narrative-generation format, and the world-bible handoff; they do not provide the actual decision tables/checklists/worked examples required by QUALITY 4. The claims ENTRIES leg explicitly describes its floor as “a length-and-shape gate only,” so word count does not establish usability.

**Fix:** realize at least the promised boundary/typology table and a worked, non-canonical worldbuilding example; make the handoff actionable and end before choosing or recording a world's canon.

### F12 — LOW — Uncited names in amendment 23's proposed issue overview

Amendment 23 §N+2 proposes to characterize “Eco's combinatorics” and “Bremond's logic of narrative possibilities,” but its source lines cite only Todorov (S902) and Greimas (S904). These are substantive characterizations of works/authors not supported by those two cited articles as written.

**Fix:** remove those characterizations or cite and open authoritative source rows that support each exact claim; do not add them as uncited context.

### F13 — LOW — The amended source-opening account omits the ordinary-copy challenge disposition

Amendment 24 says the publisher deposit returned 403 to an automated client and that the claim was read via an Internet Archive capture. QUALITY 10 says a challenge met and routed around by an ordinary copy is not a bypass, but the row should say that the challenge was met and not passed. The current staged account says “via ... capture” but does not explicitly say the challenge was not passed; any new Gate record must preserve the distinction and the exact UA-response binding if a wall/status refusal is recorded.

**Fix:** record “challenge met, not passed; opened via ordinary Wayback capture,” and ensure any in-scope wall/status Gate line binds each actual UA to its own response per QUALITY 22.

## Checks and evidence

- Claims and ledger read as DRAFT; claims freeze map path is `.ufo/waves/round-75/assimilation/id-renumber-map.json`, `map.sha256` is null. A read of that path returned not found. No claims/ledger edits made.
- Staged-ID coverage from the draft row-set (not a verified map): S864→S888; S865→S889; S866→S890; S870→unmapped/refused; S876→S885; S885→S885; S902→S886; S904→S887; S905→S891; S917→S885; S919→S892; S921→S885. Campaign prose IDs S744 and S763 are outside that listed staged-ID set and need document-correct lane replacements (S885 and S887 respectively).
- Base lane tree at `f556d104…`: the four named base coupling files exist; S860–S884 are already present in the registry; no `CANNOT-ANSWER.md` or `SOURCES-PROPOSED.md` exists. Amendment entries are an existing lane convention (e.g. `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`, `worldbuilding-setting-practice.amend-2026-10-23.md`, `linguistics/conlang-scholarship.amend-2026-10-23.md`).
- Plain-request PDF re-test: S864 syllabus extracted to text; `查特曼`, `格雷马斯`, and `行动元` each occur (3 matches). S865 JCSS paper contains `解説` (6) and `序説` (5), and `多重物語` (7); `起承転結` is absent there and in S864. S866 JSIK PDF fetched 200/697,092 B and extracted; `起承転結` occurs twice, as do `クエスト` (15) and `シーン` (20). These checks support the named attributions; they do not replace the round's required Gate/evidence receipts.
- `tools/check-cited-lines.py` on the five staged files: base, 23, 23c, 24 each fail with the MULTI-ID findings listed in F3; 23b passes. No other test/build/lint run.

## Residual risk / verification gaps

No final lane landing, by-document map, Gate records, source rows, evidence windows, lesson, or materialized lands tree was available to verify. In particular the map's actual contents/digest and the final quote/window choice for the folded Barthes row remain unverified. The S870 row's possible round-75 re-quote is unresolved. Admission remains conditional on resolving F1–F11 and rechecking final bytes against the claim's frozen legs.
