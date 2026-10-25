# SimplifierRows — minimal honest row set for claim C (round 73, w1)

Seat: SimplifierRows (leaf — no delegation, no background jobs, no `task` spawns, no `agent://all`).
Date: 2026-10-25. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at base `8841ad3b896a0227674fa0725b818c999118046f`.
Item: minimality attack on claim C's row set — keep/cut each of the five tentative rows, test the opposite (a cited source with no row), name the entry cuts, give the kill-rule consequence of each.
Claims text read at `reports/round-73/claims.json` (DRAFT-v0; not edited by this seat).

**Verdict in one line:** the minimal honest row set is **five rows, S876..S880, one per document, none cut** — and the sixth source the staged entry cites (**S894**) must be **cut from the entry, not rowed**; a sixth row is excluded by claim C's own ROWS predicate (`all status mined`), and the entry's remaining citations are the ones to cut.

---

## 0. What I attacked, and against what bytes

- The scribes have **not** written entry drafts yet: `.ufo/waves/round-73/w1/drafts/` holds only `ca72-rerun-3adbd4ab.txt` and `ca72-rerun-8841ad3b.txt` (both claim-Ca material). I therefore reasoned against the **staged entries** the claim names, which are the only entry bytes in existence:
  - `shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md` (24 lines)
  - `shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` (50 lines, two amendment blocks)
- Staged rows read at `shokuknow/merge/kotodama/SOURCES.append.md` lines 29, 30, 40, 41, 49.
- Wave-1 scout verdicts read: `ScoutS881.md`, `ScoutS882.md`, `ScoutS892.md`, `ScoutS893.md`, `ScoutS901.md`, `ScoutMapIds.md`; collision receipt `.ufo/waves/round-73/assimilation/theme-row-collision.txt`.
- Because no draft exists, each keep/cut below carries a **decision rule**: if a scribe later drops the one clause a row uniquely carries, that row drops with it (the rule is stated per row).

---

## 1. Per-row keep / cut

Every row below is needed by at least one staged entry line, and each carries **one clause no other row carries** — which is also the clause that must be the row's only cited line under QUALITY 15. No row is redundant with another: the two Russian sources overlap on the taxonomy, but not on anything else (§3.2).

| row | staged | needed by (file:line) | the clause only this row carries | drop → what fails |
|---|---|---|---|---|
| **S876** | S881 | `conlang-scholarship.md:4` (source), `:19` (§2), `:12` (sources) | the teaching/research asymmetry: "the reasons that lead me to marginalize natural languages from teaching are the same ones that lead most linguists to marginalize constructed languages from research" (ScoutS881 §3, abstract p. 267) | REPOINTED (line 4 has no lane id), ROWS (union no longer covers the base entry), CITEDLINES unaffected, QUALITY 1 (the §2 claim loses its checkable source) |
| **S877** | S882 | `conlang-scholarship.md:5` (source), `:20` (§3), `:21` (§4), `:18`, `:12` | the book's **literature survey** (printed p. 27: Yaguello, Schnapp, Eco, Hennig) and the natural-language contrast (p. 21) — no other row carries these | same three legs, plus the claim's own "the literature is not English-only" loses its only Russian row |
| **S878** | S892 | `amend:30` (source), `:45` (§N), `:37` (topic), `:39` | the purpose→features correlation and the **Eurocentrism** problem: "attention is also drawn to the problem of eurocentrism in constructed languages" (ScoutS892 §4, abstract p. 455) | REPOINTED (line 30), ROWS, QUALITY 1 for §N |
| **S879** | S893 | `amend:31` (source), `:38` (gap-filled, inline id), `:46` (§N+1), `:37`, `:39` | the **Peterson comparison**: `Наиболее детализированной классификацией, по всей видимости, является типология Д. Питерсона` (11 tokens, comparison section, printed p. 32) and the article's assessment that categories are under-specified | REPOINTED (lines 31 and 38), ROWS, QUALITY 1 for §N+1 |
| **S880** | S901 | `amend:4` (source), `:17` (§N), `:9` (topic), `:11` | the Sowers-Wills **course design**: "In the course, examples of phonological systems in natural languages and constructed languages were presented along with instruction in language universals and typology." (23 words, §3 "These papers", p. 5) | REPOINTED (line 4), ROWS, QUALITY 1 for the whole first amendment block |

**No row is cut.** The minimality test found no row that a drafted sentence does not need, and no two rows that could collapse into one document (five distinct URLs; URL-join against the 799-row lane is 0 for all five, `theme-row-collision.txt` §D).

### 1.1 The rows are not minimal until normalized — measured

The staged row text **cannot** be appended as-is, and the reason is mechanical, not stylistic (this is exactly the clause claim C's kill rule names: "un-normalized recheck cell, escaped pipe"):

```
$ awk -F'|' '/^ {0,3}\| S[0-9][0-9][0-9]+ /{ n++; if (NF!=13) c++ } END{print "rows="n" bad="c+0}' corpus/SOURCES.md
rows=799 bad=0
$ grep -c '\\|' corpus/SOURCES.md
0
$ python3 - (rows 799) recheck cells containing a backtick command: 0
```

- All 799 lane rows have `NF=13`; **no** lane row contains an escaped pipe; **no** lane row puts a command in its `recheck` cell (the cell is a bare cadence: `180d`, `90d`, `on-release`).
- Each staged row carries a shell pipeline in `recheck` (`… \`curl … \| grep -c 'marginalize'\` -> 2`), which parses as **12 cells** and, once the pipe splits the row, pushes the `used-by` cell out of the table. Escaping the pipe does **not** help: `gawk -F'|'` splits on `\|` too.

Exercised proof (`scripts/sources-census.sh validate --file`, fixture root `/tmp/SimplifierRows/reg2`, a symlink farm of the lane with a real copy of `corpus/knowledge` and the two land paths created):

| fixture | rows appended | result |
|---|---|---|
| V1 | the five rows, **bare cadence `recheck`, no pipe anywhere, `used-by` = exactly the admitted entry paths** | `exit=0`, 0 E-codes, `file ok`, W04 count unchanged at the 28 pre-existing (`telemetry/census-start.txt`) |
| V2 | V1 + `S877` `used-by` also names `corpus/knowledge/culture-material/worldbuilding-setting-practice.md` | `exit=1`: `E11 S877 missing used-by corpus/knowledge/culture-material/worldbuilding-setting-practice.md` |
| V3 | staged `S881` row appended as-is | `exit=1`: `E01 S881 fields=12` **and** `E11 S881 missing used-by grep -c 'marginalize'\` -> 2 (ran 2026-10-23)` |
| V4 | the five rows + a sixth `S894` row with `status=rejected`, `used-by=—` | `exit=0` structurally — but see §2.1: inadmissible under ROWS' `all status mined` |

Consequences for the freeze, all mechanical:

1. `recheck` must be a bare cadence; the recheck **command** belongs in `corpus/lessons/round-73.md ## Gate records` (the GATE leg already demands URL + access date + quote there).
2. `used-by` must name **exactly** `corpus/knowledge/linguistics/conlang-scholarship.md` (S876, S877) or `…/conlang-scholarship.amend-2026-10-23.md` (S878, S879, S880). ScoutS882's proposed `used-by` naming `worldbuilding-setting-practice.md` fails census **E11** (path absent in the lane) *and* ROWS ("used-by naming exactly the admitted entries") — the two legs fail together.
3. `opened` normalizes to `2026-10-25` (all five scouts opened today; the staged `2026-10-23` is the campaign date and would also make the GATE access date disagree with the row).

---

## 2. The opposite test — a cited-in-entry source with no row

### 2.1 S894 (`https://doi.org/10.1017/cnj.2024.21`) is cited and has no row: cut it, do not row it

It is cited at `amend:32` (`source: S894`), `:34` (recheck id set) and `:47` (`§N+2 … from S894: a semester-long language-construction project …`), and named in prose at `:7` and `:37`.

My own probes today (browser-shaped UA, recorded below; downloads in `/tmp/SimplifierRows/`):

```
$ curl -sS -A '<browser UA>' -L 'https://doi.org/10.1017/cnj.2024.21'
  → HTTP 302 → cambridge.org/core/product/identifier/S0008413124000215/type/journal_article → HTTP 429 (1302 bytes)
  attempt 2 (same DOI, after 20 s)            → HTTP 429
  attempt 3 (journal article slug)            → HTTP 429
$ curl CDX url=cambridge.org/core/product/identifier/S0008413124000215/type/journal_article → []
$ curl CDX url=doi.org/10.1017/cnj.2024.21                                               → []
```

The staged entry already recorded "HTTP 429 on four attempts across two URL variants" (`amend:7`). So the payload is **unreachable by ordinary means** and **has no same-page Wayback capture**: QUALITY 18's rejection conjunction ("no working same-page capture AND the live URL cannot serve the quote to a re-opener") is satisfied, and QUALITY 10 forbids recording it as opened. A row for it would be `status=rejected` with `used-by=—`.

That is why the honest move is **cut, not row**:

- **Row it (rejected)** → ROWS says "one per source the two entries cite … **all status mined**" → leg false → claim C fails as declared. V4 shows census alone would pass it, so this is a *claim-predicate* failure, not a census failure — the distinction matters because a later seat could "fix" it by appending a rejected row and still fail.
- **Row it (mined)** → GATE demands a located ≤25-word quote with access date 2026-10-25; no seat has opened it and no quote exists → GATE false, and QUALITY 1/10 are violated → claim fails.
- **Cut it** → REPOINTED, ROWS, GATE all stay true, and the refusal is recorded where claim C's REJECTS leg wants it: the lesson, with reason, flip and the probed URLs (QUALITY 21). `amend:7` (the 429 sentence, which carries no id) is the entry-side record to keep.

Cut list for S894: `amend:32` (source line), the `S894` token in `:34`, the whole `:47` bullet, "three" → "two" at `:37` and `:39`, and the "English-language journal article" element of the topic at `:37`. Note the S901 flip condition forbids the alternative of back-filling "semester-long" onto S880 (ScoutS901 §7), so the two cuts are coupled.

### 2.2 S728 is a campaign id, not a missing row

`conlang-scholarship.md:11` cites `S728` as "a conference paper" from round 1; lane `S728` is Frye, *Child-directed Speech in Qaqet* (`theme-row-collision.txt`, ScoutMapIds §1b). No row can make this true — the document is unrelated. REPOINTED requires it to "appear nowhere in the entries"; keeping it trips the kill rule's first clause verbatim ("a campaign id naming an unrelated lane document"). **Cut the sentence, keep the gap claim** (the gap sweep receipt `reports/round-73/telemetry/gap-sweep.txt` carries the same fact without the id).

### 2.3 Two path citations that no row can carry

`amend:6`, `amend:34`, `conlang-scholarship.md:7` point at `SOURCES-PROPOSED.md` (round 2 / 3 / 4), and `amend:48` points at `CANNOT-ANSWER.md`. Neither file exists anywhere in the lane (`find . -name 'SOURCES-PROPOSED.md' -o -name 'CANNOT-ANSWER.md'` → 0 hits). These are recheck/ground provenance pointing at non-existent bytes; the recheck lines must be rewritten anyway (§1.1 item 1), and `amend:48` must name the row-less missing-venue fact without a dead path.

---

## 3. Cuts to the entries, each with its kill-rule consequence

| # | cut | why (evidence) | if kept |
|---|---|---|---|
| 1 | `conlang-scholarship.md:7` and `amend:34` — the two multi-id recheck lines | measured: `tools/check-cited-lines.py` on the staged pair prints `MULTI-ID …conlang-scholarship.md:7 S881,S882` and `MULTI-ID …amend…md:34 S892,S893,S894` → `CITED-LINES: 2 finding(s)`, exit 1. QUALITY 15: "each line that cites a source carries exactly one distinct S-id" | **CITEDLINES leg false** (the leg is "prints 0 findings") → claim fails |
| 2 | `amend:32`, `:34`'s `S894`, `:47`; `:37`/`:39` "three"→"two" | §2.1 | ROWS (`all status mined`) or GATE/QUALITY 1 → claim fails |
| 3 | `conlang-scholarship.md:11` — the `S728` sentence | §2.2 | REPOINTED + kill rule's first clause → claim fails |
| 4 | `amend:9` "a semester-long language-construction project" and `:17` "the semester-long construction project" | the S880 PDF contains the token **zero** times (ScoutS901 §3, `grep -ci semester` = 0 on live and on the 2024-08-01 archive copy). The design detail S880 *does* carry is the 23-word quote in §1 | GATE: the row's quote cannot support the row's `teaches`/`scope`; ScoutS901's declared flip turns ADMIT→REFUSE for the row → GATE false |
| 5 | `amend:46` "personal or **автоконланги**" | the lexeme appears 0 times in S879's HTML and PDF; the source's own terms are `Personal languages` / `личные, или персональные` / `авторские языки` (ScoutS893 §5) | QUALITY 1 (a claim the source does not carry). Not a claim-C leg, but a reviewer catch |
| 6 | `amend:31` location label "§1" (source line) and `:38`'s "which round 2 could only reach as a table of contents" | the passage sits in the comparison section (printed p. 32), not §1; and S877 is the **complete typeset book** (185 PDF pages), so "only as a table of contents" is false (ScoutS893 §5; ScoutS882 §6.1) | the row's `anchor` would be mislocated and the entry's gap claim would rest on a false characterization of S877 — QUALITY 1, and it makes the S879 row's justification dishonest |
| 7 | `conlang-scholarship.md:18` "a scholarly **book announcement**" and `:12` "both tier **B**" | S877 is the full monograph, not an announcement (ScoutS882 §6.1). Tier: if the row is fixed at A, "both tier B" becomes false | entry/row disagreement on the one fact the claim's ENTRIES/ROWS legs both name (tier is in the row, tier text in the entry) |
| 8 | `conlang-scholarship.md:20` "why the distinction matters for a fictional world that merely *has* languages" and `:21` "the survey literature **behind them**" | the PDF carries neither: the first is the entry's own application (ScoutS882 §6.3); the survey is general, not "behind" Tolkien/Klingon/D'ni (ScoutS882 §5) | QUALITY 1 (application laundered as source claim) |
| 9 | `couples:` targets absent from the lane — `linguistics/phonology-systems.md`, `culture-material/worldbuilding-setting-practice.md`, `linguistics/naming-systems.amend-2026-10-23.md`, `culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` | verified absent; `naming-systems.md`, `phonetics-phonology.md`, `conlang-methodology.md` exist | QUALITY 3 (an entry that couples nothing says so; it must not couple to nothing). No claim-C leg tests this, so it cannot fail the claim — but it is a free repair |
| 10 | `amend:46` taxonomy restatement | §N+1 repeats §3's taxonomy from a secondary report of the same book (S877 p. 11). Minimal honest shape: §3 carries the taxonomy from S877; §N+1 carries only the Peterson comparison + the under-specification assessment | not a leg failure; a duplicate-clause reviewer catch (QUALITY 15's second sentence: one-id lines still need one clause each) |

Demonstrated fix, exercised: a corrected pair in `/tmp/SimplifierRows/candidate/` (one id per citing line, no campaign ids, S894 refused in prose, "semester-long" removed) prints `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0 — while the staged pair prints 2 findings, exit 1. So cuts 1–3 are sufficient to green CITEDLINES; cuts 4–10 are QUALITY-side.

---

## 4. Freeze-time decisions this seat cannot take (each with the minimal branch)

1. **S894 — cut (recommended) or refuse-in-lesson only.** Cutting is the only branch consistent with ROWS' `all status mined` + GATE + QUALITY 1/10/18 at today's evidence. If the owner instead wants the English classroom position kept, the row set becomes **six** and ROWS' predicate must be re-frozen before dispatch (and the sixth row must be `mined`, which today's evidence cannot support).
2. **S877 tier — B with a corrected reason (recommended) vs A.** The scout proposed A because the full book was opened, with its own caveat that a cover-to-cover reading was not performed (ScoutS882 §8). B + the corrected reason ("complete typeset text, author-hosted, not an announcement booklet") keeps the entry's "both tier B" true and needs no new claim about a reading no seat exercised. A would require that reading claim and would force an entry edit at `:12`.
3. **One provenance header vs two in the amend file.** The lane precedent is one header per amend entry (`heritage-taxonomy-models.amend-2026-10-24-r13.md`: one `- source:`, one `- verified-at:`; no lane amend file has 2+ `verified-at:`). The staged amend file has two header blocks (lines 4–13 and 30–41). Claim C's ENTRIES leg says "the full provenance header (source/verified-at/recheck/ground/topic/gap-filled/sources/couples/scope)" without saying "exactly one". Keeping both headers preserves the dated record and passes a presence check; consolidating matches precedent and the claim's singular wording. This is a counter-shape decision the freeze must state, because the two readings differ on the same bytes.

---

## 5. Tradeoff and what I did not do

- **No scribe draft existed**, so the keep/cut rests on the staged entries. If a scribe cuts a clause, the paired row drops: S876←`§2`, S877←`§4`'s survey, S878←`§N`, S879←`§N+1`'s Peterson comparison, S880←`§N`. Each of those clauses is the row's only unique contribution (§1), so the rule is exact.
- I did **not** write any row text into the registry: `/tmp/SimplifierRows/reg2` is a throwaway fixture and the executor owns the landed bytes. The validated cell-shape contract is §1.1, not a second copy of the rows.
- I did **not** judge claim Ca, the map arithmetic (ScoutMapIds owns it), or the quarantine register. One adjacency worth passing on: the five adopted ids **S876..S880 numerically equal five *other* staged rows** (naming/narrative documents, `theme-row-collision.txt` §C) — a later adoption of those staged rows must renumber by document, and the regenerated map must say so.
- Shared tree untouched: `git -C kotodama-shokunin status --porcelain` lists only the untracked wave dirs (`?? .ufo/waves/round-73/`, `?? reports/round-73/`, and the two round-72 seat files that claim Ca already owns); `HEAD` = base `8841ad3b`.

## 6. Evidence hygiene

- User-Agent on every fetch by this seat (recorded per QUALITY 21/22 draft): `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. No challenge wall was bypassed; a 429 was recorded as a 429, and the CDX probes that returned `[]` are filed with their verbatim URLs (§2.1).
- Downloads, all under `/tmp/SimplifierRows/` only: `doi.html`, `doi2.html`, `doi3.html`, `hdr.txt` (S894 probes); `reg2/` (census fixture: symlink farm + copied `corpus/knowledge` + `corpus/SOURCES.md`); `candidate/` (the two-entry CITEDLINES demonstration). Nothing fetched was written to the fleet root, the lane root, or `shokuknow`.
- Tools installed or upgraded: **none**. `curl`, `gawk`, `python3`, `pdftotext` were already present; no pacman, no uv, no npx.
- Commands run read-only against lane and fleet bytes: `scripts/sources-census.sh validate --file` (fixture paths only), `tools/check-cited-lines.py` (read-only), `git status/rev-parse`.
