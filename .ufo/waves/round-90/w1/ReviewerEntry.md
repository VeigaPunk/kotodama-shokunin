# ReviewerEntry — round-90, claim C (coverage) — adversarial review

Seat: ReviewerEntry-3 · 2026-11-04 · milestone r90-v1 · lane kotodama
Frozen predicate read first: `reports/round-90/claims.json` (unamended).

**Draft status.** `.ufo/waves/round-90/w1/stage/ScribeEntry/` was EMPTY at review time
(2026-11-04T20:10:06-03:00: only an empty `evidence/` directory — no entry.md, rows.md,
gates.md, evidence files, manifest.json). Per seat spec I therefore reviewed the **frozen
claim C's predicate and constants against the lane's real state**, and derived the
grader-conformance traps the draft must clear. Draft-dependent axes (unbound claims, tier
inflation, scope, in-draft filler, NON-CANON) could not be exercised and are listed as
gaps. L1 was messaged about the blocking finding.

---

## Blocking

### B1 — The frozen counter's C `ENTRY` leg can never PASS: claim C is unpassable as frozen
`reports/round-90/measure90.py:210-212`:

```python
seen = dict(re.findall(r'^LEG (PASS|FAIL) (\S+)', out, re.M)[::-1])
missing = [l for l in want_legs if l not in seen]
failed  = [l for l in want_legs if seen.get(l) == 'FAIL']
```

`findall` returns `(verdict, name)` tuples, so `seen`'s **keys are the verdicts**
`'PASS'`/`'FAIL'`, never leg names. `missing` is therefore always all six C legs
(`ENTRY,SHAPE,TOPIC,NEWIDS,GATE,CAPTURE`), `ok` is always False regardless of rc, and
`failed` is always empty (the receipt can never name the failing leg).

**Empirical proof** (fixture repo in reviewer scratch, since deleted after capture; base
`093e74a2…`, freeze `1f0b9a50…`, lands `428a1ba2…` — a minimal repo whose freeze holds
the frozen claims.json with only `base` re-pointed at the fixture commit, plus byte-identical
copies of the two pinned tools, and whose lands holds a conforming entry, registry rows
S942–S944, lesson gates, committed captures, manifest):

- The **freeze-pinned grader alone**, run over the materialized lands tree with the exact
  flags measure90 passes (`tools/check-advance-evidence.py:376-485`), printed:
  `ENTRY-EVIDENCE: PASS legs=6/6`, rc=0.
- The **frozen counter** over the same lands revision printed:

  ```
  LEG FAIL ENTRY expected=entry mode passes ENTRY,SHAPE,TOPIC,NEWIDS,GATE,CAPTURE observed=rc=0 missing=['ENTRY', 'SHAPE', 'TOPIC', 'NEWIDS', 'GATE', 'CAPTURE'] failed=[]
  MEASURE90-C: FAIL legs=1/4 failed=ENTRY,INDEX,APPENDONLY
  ```

  (fixture INDEX/APPENDONLY failures are fixture artifacts — minimal corpus — and are not
  the point; `observed=rc=0 … missing=[all six]` against a clean 6/6 grader run is.)

One-line parse demonstration anyone can run against any clean grader output:

```python
import re; out=open('<grader PASS legs=6/6 receipt>').read()
seen=dict(re.findall(r'^LEG (PASS|FAIL) (\S+)', out, re.M)[::-1])
print([l for l in ['ENTRY','SHAPE','TOPIC','NEWIDS','GATE','CAPTURE'] if l not in seen])
# -> ['ENTRY', 'SHAPE', 'TOPIC', 'NEWIDS', 'GATE', 'CAPTURE']
```

**Consequence.** claims.json C kill rule: "Any FAIL leg kills C." The ENTRY leg is a
permanent FAIL, so `MEASURE90-C` fails at **every** lands revision — the coverage claim
cannot land under the frozen counter no matter how conforming the scribe's draft is.
The defect is in the counter, not claims.json: every claims.json C constant is faithfully
passed by measure90 (A2 below). Resolution belongs to L1 (counter is frozen to seats):
re-freeze `measure90.py` with the tuple order inverted so keys are leg names. No seat may
amend it; I did not.

O is unaffected (its legs parse differently: `measure90.py:144-152` uses `m.group(1)`/`m.group(3)`
positionally).

**Status after L1's fix (counter revision 6).** L1 amended the working tree
(`reports/round-90/measure90.py:210`: `seen = {name: verdict for verdict, name in re.findall(...)}`,
diff `d0a81ac2..11706813`), claims.json and the grader bytes untouched. My independent rerun of
the **fixed** counter (sha256 `6e1ea6a5f96c6e92660e7a18c18b896d46dee3bf6368231e1a4a8fd7895406cd`
at the time of the run) over the same perfect landing now prints
`LEG PASS ENTRY … observed=clean` — see Appendix R, receipt 3. The fix is verified from this
seat; the ENTRY leg's predicate is unchanged.

---

## Advisory

### A1 — Frozen surface/pre-state claims verified accurate against the lane
- `git ls-tree -r --name-only 6b0b86e4 -- corpus/knowledge | grep -Eic "prayer|petition|votive|supplicat"` → `0`; `… -- corpus/knowledge/linguistics | wc -l` → `34`. Matches claims.json C.surface.
- Working tree (c0c628d8): `python3 -B tools/check-corpus-index.py --root .` → `CORPUS-INDEX: OK files=261 rows=261 findings=0`.
- Registry max id is S941 (`corpus/SOURCES.md:896-897`); reserved S942–S949 are all free.
- APPENDONLY cell indexing (`measure90.py:231-244`) matches the 11-column schema at `corpus/SOURCES.md:28` (tier=cells[3], status=cells[7], opened=cells[8], used-by=cells[10]). Correct.

### A2 — claims.json C constants ↔ counter ↔ grader: no drift
measure90 passes `--min-bytes 12000 --min-headings 6 --min-new-ids 3 --min-topic-overlap 10 --table-min-rows 5 --table-min-cols 3` (`measure90.py:189-199`) == claims.json C. The grader's quote-bound defaults `--quote-max-words 25 --quote-min-chars 20` (`check-advance-evidence.py:930-931`) == claims.json quote constants (measure90 relies on the defaults; they agree). Header keys hardcoded in `grade_entry` (`check-advance-evidence.py:391`) == claims.json `header_keys`. `reports/round-90/mutation-score.txt:1` = `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern` ≥ frozen `mutation_min` 42, tool sha matches the pin.

### A3 — Trap that kills C: the entry must NOT cite S949
The reserved S949 is the lesson's **reject** row. If the entry text mentions S949:
- with the reject row committed (round-89 precedent, `corpus/SOURCES.md:897`): new + cited → NEWIDS requires A/B + mined (`check-advance-evidence.py:439-441`) → `S949: tier C not A/B` → **FAIL NEWIDS**;
- without the row in the registry: `cited ids missing from registry` (`:457`) → **FAIL NEWIDS**.

Round-89 handled this correctly: the reject row S941 is marked "Not cited by the entry" (`corpus/lessons/round-89.md:66`). The reject row belongs in the lesson only; the entry's prose must refer to the rejected class without the S-id.

### A4 — Trap: gate lines must be the FIRST lesson line pairing each id with a quote
`gate_quotes` (`check-advance-evidence.py:162-174`) collects every lesson line containing the id and a quoted span; GATE/CAPTURE validate **only `qs[0]`** — the first such line. If a verdict-summary or disposition line that quotes the id precedes the gate line, the wrong quote gets the ≤25-word/≥20-char bounds check and the wrong line must carry the row URL and `2026-11-04`. Order the lesson: gate lines first, any quoting summary lines after — or keep quotes out of non-gate lines.

### A5 — Trap: the INDEX leg forces README count edits that earlier prose calls rewrites
`tools/check-corpus-index.py` enforces, over the lands tree:
- one row per file or `MISSING_ROW` (`:119`) → add `- \`petitionary-and-votive-formulae.md\` — …` inside the linguistics section;
- `TOPIC_MISMATCH` (`:135-136`): the row's text after `— ` must equal the entry's `- topic:` field **verbatim** (newlines collapsed) — copy, don't paraphrase;
- `HEADER_DRIFT` (`:140`): `## linguistics/ (34)` (`corpus/README.md:344`) must become `(35)` in place — this contradicts the round-79 note "an in-place heading edit would be a rewrite" (`corpus/README.md:793`), which predates this tool; the tool wins or INDEX fails;
- `TOTALS_DRIFT` (`:149`) uses the **last** totals line → append `Total knowledge entries: 262.` (current last: `corpus/README.md:933` = 261);
- `FOOTER_TOTAL`/`FOOTER_DIR_TOTALS` (`:167-170`) use the **last** footer → append a fresh `Counts checked 2026-11-04 … (total 262 files; directory totals 35/36/43/29/24/95).` block (current last: `corpus/README.md:934-936`).

### A6 — Trap: captures must be committed lands bytes with strict manifest fields
The counter materializes via `git archive` (`measure90.py:53-63`), so an uncommitted capture is `capture not committed` (`check-advance-evidence.py:203-205`). Each manifest row needs: capture path inside `reports/round-90/evidence/`, sha256 of the committed bytes, integer 2xx `http_status`, `fetched_at` = ISO instant **with offset** dated 2026-11-04 (regex `:46`), and the gate quote must occur in the capture after NFKC/whitespace normalization (`:216-217`). Captures equal to `corpus/SOURCES.md` or `corpus/lessons/round-90.md` are refused (`:196-198`). Captures must be plain UTF-8 text.

### A7 — Draft-dependent review checklist (unexercised; ScribeEntry empty)
- **Unbound claims** (axis 1): every non-trivial statement needs an S-id citation whose `teaches` cell supports it; the tool checks only existence/tier/date/used-by, so support is on reviewer/critic/closure.
- **Tier inflation** (axis 2): round-89 calibration precedent — WALS chapter / author PDF with stated scope = A (`round-89.md:61-64`), signed glossary = B (`:65`), unreferenced community stub = C reject (`:66`). A tertiary page badged A/B, or a chapter cited for a claim it does not make, must be flagged.
- **Scope** (axis 3): the entry must stay linguistic-cultural design reference; lore canon, chousa research method, tabi pilgrimage practice, kotoba craft belong out.
- **Filler** (axis 4): SHAPE refuses any ≥6-word sentence occurring >2× (`:399-404`), even across case/punctuation variants (norm() casefolds); sub-300-byte sections and content-free table rows are review findings, not just tool ones.
- **Topic floor note**: `words()` drops <4-char words (`:77-79`), so **"vow" does not count** toward `min_topic_overlap=10`; the declared topic still supplies 22 eligible content words, so the floor is easy for an on-topic entry — but a generic prose pad that avoids the topic vocabulary fails TOPIC (`:411-418`) and the filename-stem check needs at least one of petitionary/votive/formulae in the text.

### A8 — APPENDONLY correctly enforces the freshness pause
`measure90.py:228-233` compares **every cell of every base row**; any re-verified, re-dated or repaired old row kills C. Adding rows is the only registry mutation available. Consistent with claims.json C.bounds and the L0 round-11/round-89 pause — no defect, recorded as verified leg fit.

---

## Leg-fit summary (post-fix state; see B1 status note)

| Leg | Verdict | Reason |
|---|---|---|
| ENTRY/SHAPE/TOPIC/NEWIDS/GATE/CAPTURE | pass-able | Grader passes a conforming landing (proved 6/6); fixed counter now honors it — Appendix R, receipt 3 |
| INDEX | pass-able | Requires A5's README edits; tool verified clean at current tree |
| APPENDONLY | pass-able | Requires ≥3 cited new A/B/mined rows opened 2026-11-04 with used-by + README row; verified mechanics A1/A8 |
| O legs | out of scope | Reviewed only where C shares the tool (sha pin verified) |

## Appendix R — B1 reproduction recipe, shas and receipts (requested by L1)

Everything below is persisted in my stage dir at
`.ufo/waves/round-90/w1/stage/ReviewerEntry/b1-repro/` (`build_fixture.py`,
`measure90-frozen.py`, `receipt-grader.txt`, `receipt-counter-frozen.txt`,
`receipt-counter-fixed.txt`). The builder is deterministic (author/committer name, email and
dates pinned via env), so rebuilding reproduces the same three revisions.

**Fixture revisions** (minimal scratch repo, not the lane):

| role | revision | contents |
|---|---|---|
| base | `093e74a2b4346fb8881dcae10bca1ac5ac745cf2` | `corpus/SOURCES.md` with the 11-column header + one base row `S001` |
| freeze | `1f0b9a5012f36d5032f0d8c9c68f823a4af5b58c` | `reports/round-90/claims.json` = the frozen file with **only `base` re-pointed** at the fixture base hash; byte-identical copies of `tools/check-advance-evidence.py` (sha `121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed`, the freeze pin) and `tools/check-corpus-index.py` |
| lands | `428a1ba2f1580bf56cb3d30afd713c9194bfac34` | the freeze + a conforming entry (`corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, ≥12000 B, 6×`## `, header keys, 6×3 table, unique sentences, topic words, cites S001+S942–S944) + registry rows S942–S944 (A/mined/2026-11-04/used-by the entry) + `corpus/lessons/round-90.md` gate lines + committed `reports/round-90/evidence/S94{2,3,4}.txt` + `manifest.json` + minimal `corpus/README.md` |

**Commands** (recipe; full generator is `b1-repro/build_fixture.py`, run with
`python3 build_fixture.py` — it prints all three hashes and all three receipts):

```bash
# 1. the freeze-pinned grader alone, over the materialized lands tree, with the
#    exact flags measure90 passes  -> PASS legs=6/6, rc=0
python3 -B <fix>/tools/check-advance-evidence.py entry \
  --root <mat> --entry <mat>/corpus/knowledge/linguistics/petitionary-and-votive-formulae.md \
  --base-registry <base-SOURCES.md> --lands-registry <mat>/corpus/SOURCES.md \
  --lesson <mat>/corpus/lessons/round-90.md \
  --manifest <mat>/reports/round-90/evidence/manifest.json \
  --capture-dir reports/round-90/evidence --as-of 2026-11-04 --topic "<claims.json C.topic>" \
  --min-bytes 12000 --min-headings 6 --min-new-ids 3 --min-topic-overlap 10 \
  --table-min-rows 5 --table-min-cols 3 \
  --graded corpus/SOURCES.md --graded corpus/lessons/round-90.md

# 2. the frozen counter over the same lands  -> ENTRY FAIL despite rc=0 above
python3 -B measure90-frozen.py --root <fix> --lands 428a1ba2… --freeze 1f0b9a50… \
  --claim C --work <existing-dir>

# 3. the fixed counter over the same lands -> ENTRY PASS (green control)
python3 -B measure90-fixed.py  --root <fix> --lands 428a1ba2… --freeze 1f0b9a50… \
  --claim C --work <existing-dir>
```

**sha256 of the counter bytes I ran:**
- frozen (HEAD blob at review time, pre-fix): `80a07a579be80376d2ba6227011a7231bff47e75ad92c6e4a6e415676aad835a` (`git show HEAD:reports/round-90/measure90.py | sha256sum`; the file was unmodified in the tree when I ran it)
- fixed (worktree at my rerun): `6e1ea6a5f96c6e92660e7a18c18b896d46dee3bf6368231e1a4a8fd7895406cd`

**Receipt 1 — grader alone (lands tree):** `receipt-grader.txt`

```
LEG PASS ENTRY expected=>=12000B, >=6 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=10 shared content words with the declared topic observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-04 and cited observed=clean
LEG PASS GATE expected=each new id has a located gate line observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
ENTRY-EVIDENCE: PASS legs=6/6
```

**Receipt 2 — frozen counter, same lands:** `receipt-counter-frozen.txt`

```
LEG PASS MATERIALIZE expected=lands 428a1ba2f1580bf56cb3d30afd713c9194bfac34 materialized observed=…/work-frozen/mat
LEG FAIL ENTRY expected=entry mode passes ENTRY,SHAPE,TOPIC,NEWIDS,GATE,CAPTURE observed=rc=0 missing=['ENTRY', 'SHAPE', 'TOPIC', 'NEWIDS', 'GATE', 'CAPTURE'] failed=[]
LEG FAIL INDEX expected=index tool exit 0 over the lands tree observed=CORPUS-INDEX: FINDINGS files=1 rows=0 findings=14 ids=FOOTER_ABSENT,MISSING_ROW,PARTITION_DIR_MISSING,PARTITION_MISSING,TOTALS_ABSENT
LEG FAIL APPENDONLY expected=no base row changed; >=3 new mined A/B rows cited; README row observed=entry absent from corpus/README.md
MEASURE90-C: FAIL legs=1/4 failed=ENTRY,INDEX,APPENDONLY
```

**Receipt 3 — fixed counter, same lands (green control):** `receipt-counter-fixed.txt`

```
LEG PASS MATERIALIZE expected=lands 428a1ba2f1580bf56cb3d30afd713c9194bfac34 materialized observed=…/work-fixed/mat
LEG PASS ENTRY expected=entry mode passes ENTRY,SHAPE,TOPIC,NEWIDS,GATE,CAPTURE observed=clean
LEG FAIL INDEX expected=index tool exit 0 over the lands tree observed=CORPUS-INDEX: FINDINGS files=1 rows=0 findings=14 ids=FOOTER_ABSENT,MISSING_ROW,PARTITION_DIR_MISSING,PARTITION_MISSING,TOTALS_ABSENT
LEG FAIL APPENDONLY expected=no base row changed; >=3 new mined A/B rows cited; README row observed=entry absent from corpus/README.md
MEASURE90-C: FAIL legs=2/4 failed=INDEX,APPENDONLY
```

Receipts 2 and 3: the INDEX/APPENDONLY FAILs are **fixture artifacts** (my fixture corpus holds
one file, no partition directories, a stub README) and are not evidence about the lane; the
graded line in both is the ENTRY leg. Receipt 2 shows ENTRY failing against `rc=0`; receipt 3
shows the same ENTRY leg passing `observed=clean` under the fixed parse.

---

## Residual risk and verification gaps

1. The actual draft, lesson, captures and manifest did not exist at review time; axes 1–4 and 6 of the seat spec are unexercised. Recommend L1 route the landed draft back through this checklist (A3–A7) or a re-invocation of this seat.
2. The fixture proof of B1 ran against a fixture clone with `base` re-pointed (the real base hash cannot exist in a scratch repo); the parse-inversion is also demonstrated statically and by the one-liner against clean grader output — the conclusion does not depend on the fixture. The full repro bundle is persisted at `.ufo/waves/round-90/w1/stage/ReviewerEntry/b1-repro/` (Appendix R).
3. No external sources were fetched by this seat (internal artifacts only; content truth is the closure's re-open per claims.json C.bounds). No tools installed (none needed).
4. Scratch `/fast/scratch/hyaku/kotodama-r90/ReviewerEntry/` deleted before yield.
