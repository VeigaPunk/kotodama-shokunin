# ReviewEntryContract — round 54 attempt 2, claim C entry contract attack

- Seat: KotodamaR54a2.ReviewEntryContract (leaf; no delegation, no background jobs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, claim base `260c68d58c5d3c2b9a6463ca5c667b7e0fff5987`. Read-only in the lane except this report; all checks ran on bytes pinned into scratch with `git show` (read-only git only; no jj command run).
- Inputs read this session: `.ufo/waves/round-50/build/ReviewEntryContract.md` (contract checklist and validated §2.9 checker), `corpus/lessons/round-53-verifier-spotcheck.md:107-129` (the four partly supported sentences), `reports/round-54/claims.json` (accept-c seven legs, falsifier), the gesture entry at base and at the round-53 tip `e0bfb13`, `tools/check-draft-ids.py`, and registry rows S189, S201, S202, S212, S219, S220, S221, S223, S233, S234 of `corpus/SOURCES.md` at base.
- Scratch (all demonstration bytes): `/fast/scratch/hyaku/kotodama-r54-a2/ReviewEntryContract/` — `gesture-at-base.md` (223 lines, from `260c68d`), `gesture-at-e0bfb13.md` (223 lines, pre-fix), `gesture-corrupt.md` (228 lines, 7 planted defects), `SOURCES-at-base.md` (365 lines), `entry_checks.py` (the checker, exact version that produced every output pasted below).
- Axes judged: coverage (failure modes named and grounded), calibration (every check demonstrated on real corpus bytes, pass side and fail side).

## 0. Result

- The five assigned failure modes each get a mechanical check, and every check is demonstrated three ways on the round-53 gesture entry: it fires on a corrupted fixture carrying all seven planted defect classes (16 hard, 9 soft), it is silent on those classes in the corrected entry at base (F2/F3a/F3b/F4/F5 all zero), and run against the pre-fix entry at `e0bfb13` it independently recovers the round-53 verifier's findings at lines 133, 150 and 199 (`corpus/lessons/round-53-verifier-spotcheck.md:114-121`).
- F1 (locators) is honest about its power: the mechanical reconciler catches gross slips (wrong page, no row, rejected row) but demonstrably does NOT catch the subtle round-53 slip (entry cited a page the opened proof contradicts while the page set stays inside the row's record). That class needs the re-open step; the check's value is converting silent drift into a flagged list.
- The clean corpus run produced two findings the L1 should act on when writing rows S239+: the registry systematically under-records locators and quotes (70 of the entry's quoted spans are recorded in no row; entry locators for S202 p. 94, S212 pp. 27–28 and S223 pp. 698–708 are not in those rows' scope/anchor/teaches). Recording rule: paste every locator and every verbatim quote the entry will use into the kept row at write time — then the reconciler's remaining output means a real slip.
- One corpus-hygiene fact discovered on the way: `SOURCES.md` at base carries the same paper twice — S219 (kept, mined, Springer abstract) and S233 (rejected duplicate, PubMed efetch) — and the verbatim nodding quote "in Bulgaria, this response pattern is reversed" is recorded only in the rejected row. Checks must ignore `rejected` rows as quote carriers (the checker does; a cited rejected row is a HARD finding, which is also what accept-c's STATUS leg enforces).

## 1. Where the failure modes come from

Round-53's verifier found exactly four sentence-level defects in a landed entry (lesson lines 114–121): a locator copied from the wrong pagination (line 68, S201 pp. 145/146 vs the proof's 146/147), a deposit record over-read as "the corpus behind the study" (line 133, S221), a one-culture report generalised to "some communities" (line 150, S223 on Barai), and examples attributed to a row that does not carry them (line 199, thumbs-up/OK live in S234, the entry cited only the generic S189). The round-50 contract adds the shape rules the entry must keep (§2.1–§2.5: head, length, H3 ban, placeholder ban) and the registry contract (§2.6: row columns, `used-by`, mined status). The round-54 claim's falsifier is precisely "the entry states a claim its cited row's page does not carry" (`reports/round-54/claims.json`, claim C falsifier) — these checks are the mechanical net under that falsifier. Accept-c's seven legs already enforce set/sweep/floor/range/status/used-by/access; this checklist covers what those legs cannot see: whether the prose tells the truth about what the rows say.

## 2. The checklist

Order of use at integration: write rows S239+ first, then the entry, then run checks 1–6. Checks 1–5 are one script (`entry_checks.py`, core pasted in §2.7); check 6 is the lane's own tool plus accept-c.

### 2.1 F1 — page locators copied wrong

**Failure.** The entry cites `(Sxxx, p. N)` where N came from a different edition, a different row, or a mistyped digit; or cites a page the row's record contradicts; or cites an id with no row / a rejected row.

**Mechanical check.** Pair every page locator with the nearest preceding S-id inside its citation (mixed citations like "(Sherzer, 1983, p. 169, as reported in S203, p. 207)" must not cross-attribute), and check the page sits inside the pages recorded in that row's scope+anchor+teaches columns (`line.split("|")[5:8]`). Cited id must exist and not be `rejected`.

```python
TOKEN = re.compile(r"\bS\d{3}\b|pp?\.\s*\d{1,5}(?:\s*[-\u2013/]\s*\d{1,5})?")
def sid_page_pairs(group):
    out, last = [], None
    for m in TOKEN.finditer(group):
        if m.group(0).startswith("S"): last = m.group(0)
        elif last:
            pm = PAGE.match(m.group(0))
            if pm: out.append((last, int(pm.group(1)),
                               int(pm.group(2) or pm.group(1))))
    return out
# per citation group: every (sid, a, b) must satisfy:
#   sid in rows, rows[sid].status != "rejected", and
#   pages(rows[sid].line.split("|")[5:8]) intersects range(a, b+1)
```

**Demonstration (fail side, fixture).** `(S201, p. 999)` planted over a row recording 145–147: `HARD F1:69 S201 locator p.999 not in row record [145, 146, 147] -> re-open`. Planted `(S241, -2)` and `(S241)` citations: `HARD F1:226 S241 has no registry row (cited here)` + `HARD F1:227 S241 has no registry row (cited here)`.

**Demonstration (pass side, base).** No fabricated-locator flags: the entry's S201 pages (146, 147) sit inside the S201 row's record "pp. 145–146 … and p. 147" (`SOURCES.md` row S201). 

**Honest limit, demonstrated.** Run on the pre-fix entry at `e0bfb13`, the reconciler does NOT fire on the actual round-53 locator slip (line 68): the entry cited pp. 145/146 where the proof reads 146/147, but 145–147 all sit inside the row's recorded span, so the page SET reconciles even though the item-to-page mapping was wrong. The same run shows the tripwire variant (row-recorded spans the entry never cites) also stays silent for S201 because the entry cites p. 147 elsewhere. Conclusion for the L1: F1 mechanically blocks gross slips and dead ids; the subtle slip is caught only by re-opening the source. Write rows so that each item's own locator is in the anchor column (the S201 row's "pp. 145–46 (items…) and p. 147 (items…)" shape), and re-open any row whose anchor bundles several items under one span.

**Residuals this check surfaced on the clean base (recording gaps, not proven slips):** entry `(S202, p. 94)` (base lines 134, 137) vs S202 row record {89, 90, 91}; entry `(S212, pp. 27–28)` (base line 135, the Taiwanese-mothers/Mediterranean cell) vs S212 row record {2, 16–19} (accepted-manuscript pagination); entry `(S223, pp. 698/699/701/702/705/708)` vs S223 row record {700, 28}. The round-53 verifier verified the underlying quotes against opened pages, so the likely fix is recording, not deletion — but each is a locator the registry cannot account for, and every one would be a re-open trigger had the row not been verifiable. Do not reproduce this gap in S239+.

### 2.2 F2 — "some communities" generalised from one

**Failure.** A sentence asserts a plural over communities/cultures while citing a single row that reports one community (round-53 line 150: S223 reports one culture, Barai, on a missionary's hearsay).

**Mechanical check.** Per line: skip calibration-bank rows (second cell is a lone R/C/B/H/T — those rows assert the strawman in cell 1, not a finding), skip quoted spans (a source's own hedged plurals are attributed), then flag a hedge noun-phrase (`some|many|most|several|numerous|various` + ≤2 words + `communities|cultures|peoples|societies|languages|traditions|groups`, or `across cultures|in all cultures|every culture`) on a line citing exactly one distinct S-id. Skip matches containing digits ("some 20 million people" is a quantity, not a generalisation).

```python
HEDGE_NP = re.compile(r"\b(some|many|most|several|numerous|various)\s+"
    r"(?:\w+\s+){0,2}(communities|cultures|peoples|societies|languages|"
    r"traditions|groups)\b|\b(across cultures|in all cultures|every culture)\b", re.I)
# flag when: not CALROW.match(line) and len(ids)==1 and HEDGE_NP.search(stripped)
#            and not re.search(r"\d", m.group(0))
```

**Demonstration.** Fail side, pre-fix line 150: `SOFT F2:150 hedge 'some communities' over communities with a single source (S223)` — the exact round-53 finding. Fixture sentinel "Some communities point with the chin and many cultures find it rude (S200).": `SOFT F2:2 hedge 'Some communities' over communities with a single source (S200)`. Pass side: zero F2 flags on the corrected base entry (the fixed line reads "the report that one culture (Barai) lacks index-finger pointing altogether is `(to-verify)`" — no plural hedge), and the greps stay quiet on legitimate single-source rows ("a town repertoire: 30 or more entries, the survey's own cut-off (S190)") because the hedge noun is absent or the noun phrase carries a digit.

**L1 rule.** `(to-verify)` marks an unverified claim; it does not license wording broader than the row's content. Write the community count the row actually carries: "one culture (Barai)", "one community", "seven field sites" — with the number the source states.

### 2.3 F3 — a quote or exemplar attributed to a row that does not carry it

**Failure.** Round-53 line 199: the entry's claim cell names thumbs-up/OK emblem collisions but cites only S189, whose record is generic; the specifics live in S234, uncited.

**Mechanical check (carrier direction, not containment).** Naive containment ("every entry quote must appear in the cited row") floods: most rows record paraphrase in `teaches`, not verbatim text (the clean entry has ~70 quoted spans recorded in no row — see §4). The check that recovers the round-53 defect is the inverse: for each quoted span ≥15 normalized chars, and for each distinctive token in a calibration claim cell (hyphenated compounds; capitalized words ≥5 letters), find the rows that carry it, ignoring `rejected` rows; flag when carriers exist and none is cited on that line. Output names the carrier rows: the fix is one citation.

```python
nq = norm(quote)   # NFKC, curly quotes folded, non-alnum -> space, lower
carriers = {sid for sid, r in rows.items()
            if r["status"] != "rejected" and nq in norm(r["line"])}
if carriers and not (carriers & ids): flag(f"quote lives in {sorted(carriers)}, not cited here")
```

**Demonstration.** Fail side, pre-fix line 199: `SOFT F3a:199 claim token 'thumbs-up' lives in rows ['S234'], none cited here` — the lesson's wording ("the thumbs-up and OK-ring examples are in S234, which that row does not cite") recovered mechanically. Fixture: a line quoting "an offensive gesture in Sardinia (Italy) and some parts of Greece" but citing (S189): `SOFT F3b:228 quote lives in ['S234'], not cited here`. Pass side: zero F3a/F3b flags on base (the corrected line 199 cites S234 for the Sardinia quote, whose verbatim text is recorded in S234's scope column).

**L1 rule.** For every sentence the entry writes, at least one cited row's recorded text must carry the specific exemplar (place name, community, emblem). When the carrier row exists but is uncited, add the citation; when no row carries it, either the quote was never recorded (fix the row, §4) or the entry says something the round never opened (delete or mark `(to-verify)`).

### 2.4 F4 — deposit or catalogue records over-read as studies

**Failure.** Round-53 line 133: "the corpus behind the study is Ewe route-description recordings … (S221)" — S221 is an archive deposit record (kind `dataset`); the page records a deposit, not a finding.

**Mechanical check.** Parse each row's kind (column 3). For every citation of a non-study kind (`dataset, record, web, community, docs, tool, spec`), look ±140 characters for study language (`study|experiment|fieldwork|researchers|participants|respondents|survey found|corpus behind`); suppress when a record caveat sits in the same window (`record|deposit|archive|abstract|…` within 100 chars of `does not|not itself|only`, or `not itself|screen data|not field observation|record only`). HARD on fire.

```python
if rows[sid]["kind"] in NONSTUDY_KINDS and STUDYW.search(ctx) \
   and not (DISCLAIM.search(ctx) or DISCLAIM2.search(ctx)): hard(...)
```

**Demonstration.** Fail side, pre-fix line 133: `HARD F4:133 study-language on S221 (kind=dataset) without a record caveat` — plus `HARD F4:133 study-language on S220 (kind=docs)`, a true positive with nuance: the K&E study numbers sat next to the MPI annual-report row (docs) with the "reported through" caveat only in the section's Status line, not adjacent. Fixture: "(S221 confirms the corpus behind the study)" → `HARD F4:134 …`. Pass side: zero F4 flags on base, where the same cell reads "(S221; the archive record does not itself tie the deposit to this study)" and the screen-data cell reads "(S226; screen data, not field observation)" — both caveats land inside the window and suppress.

**L1 rule (matches QUALITY item 6 and the round-53 discernment row).** Deposit, catalogue, abstract and publisher-description rows are tier B claims about the work. Cite them for the record's existence and the work's own abstract-level claims, never as if the entry had read the study; keep the caveat in the same sentence as the citation, not in a section-level footnote. Masks sources will hit this constantly: museum collection records and UNESCO nomination fulfilment documents are records, and "the community states" rows are community kind — neither is a study of effect.

### 2.5 F5 — draft ids left in text

**Failure.** A seat's draft id `NEW-<SeatName>-<n>` (or a separated citation fragment like `, -2` / `S157-2` left by a half-copied locator) survives into the landed entry. The entry must cite only S239+ registry ids; accept-c's RANGE leg cannot see a token that never became a row.

**Mechanical check.** The lane's own record tool, run from the lane root (this exact command, exit 0 required):

```
python3 -B tools/check-draft-ids.py corpus/knowledge/culture-material/masks-masquerade.md
```

It detects `NEW-<Seat>-<n>` tokens, `, -N` and `; -N` fragments, and glued `S###-N` fragments, with negative controls for page ranges and temperature-style minus numbers (selftest cases in the tool). Grep equivalent for a quick look: `grep -nE 'NEW-[A-Za-z0-9_]+(-[A-Za-z0-9_]+)*-[0-9]+' <entry>`.

**Demonstration.** Fixture line "As NEW-ScoutNuo-3 reports, the deposit row is (S241, -2).": my checker prints `HARD F5:226 draft id left in text: NEW-ScoutNuo-3` and `HARD F5:226 separated citation fragment: ', -2)'`; the lane tool prints `DRAFT_ID gesture-corrupt.md:226 'NEW-ScoutNuo-3'`, `DRAFT_ID gesture-corrupt.md:226 ', -2'`, `DRAFT_IDS: 2 findings` (exit 1). Same tool on the base entry: `DRAFT_IDS: 0 findings` (exit 0).

### 2.6 F6 — the shape and registry gates the L1 must not re-derive

Already landed as acceptance; run them, do not re-implement: `python3 -B reports/round-54/accept-c.py` (SET/SWEEP/FLOOR/RANGE/STATUS/USEDBY/ACCESS, exit 0). Three tightenings the legs leave open, each one line:

```
wc -l corpus/knowledge/culture-material/masks-masquerade.md        # <= 230 (claim bound, not r50's 250)
grep -cE '^#{3,} ' <entry>                                          # 0 (no H3; round-50 §2.2)
grep -nE '\b(TODO|TBD|placeholder|scaffold|MVP)\b' <entry>          # 0
grep -n 'lessons/round-54' <entry>                                  # 0 (must_not_cite)
```

USEDBY is a substring test (declared in the claim's predispatch notes); make it exact-path before trusting it: every cited id's row line must contain `corpus/knowledge/culture-material/masks-masquerade.md` as a path, not merely the stem (guards a future `masks-masquerade-old.md`):

```
python3 -c "import re; reg=open('corpus/SOURCES.md').read().splitlines(); e='corpus/knowledge/culture-material/masks-masquerade.md'; ids=sorted(set(re.findall(r'\bS\d{3}\b', open(e).read()))); print([i for i in ids if not any(i+' |' in l and e in l for l in reg)])"
```

(Empty list is the pass; run from the lane root after rows land.) The round-50 report's validated head-shape checker (§2.9-A there) remains reusable with the length constant changed 250 → 230.

### 2.7 The consolidated checker

Full exact version: `/fast/scratch/hyaku/kotodama-r54-a2/ReviewEntryContract/entry_checks.py` (run: `python3 entry_checks.py ENTRY.md SOURCES.md`; exit 1 iff HARD). Core, faithful to the run version: registry parsed as `{id: line, kind, status}` from `^\| (S\d{3}) \| … \| ([a-z]+) \|` with status = column 8; normalisation folds curly quotes/dashes and non-alphanumerics; citations read from parenthesised groups only (bare `S211` mentions outside parentheses are a known blind spot — the entry's prose uses them only for already-cited rows); F1 pairs locators to the nearest preceding id per citation (§2.1), flags no-row/rejected-row/locator-outside-record (HARD) and row-recorded spans the entry never cites (SOFT tripwire); F2 hedge with single cited id, quotes and calibration rows exempt, digit-bearing matches skipped (SOFT); F3a claim-cell tokens and F3b quoted spans against non-rejected carriers (SOFT, with an INVENTORY count of quotes recorded in no row); F4 kind-gated study language with windowed caveat suppression (HARD); F5 draft ids and fragments (HARD).

## 3. Demonstration protocol (what produced the pasted outputs)

- Base bytes: `git show 260c68d58c5…:corpus/knowledge/linguistics/gesture-co-speech-pointing.md` (223 lines) and `:corpus/SOURCES.md` (365 lines) into scratch; pre-fix bytes from `git show e0bfb13:…` (the round-53 tip, parent of the routed-fixes prerequisite `d761ee8`).
- Fixture: the base copy with seven planted defects — (1) `(S201, p. 999)`; (2) sentinel hedge line citing only S200; (3) calibration claim cell "The Aymara…" → "The Yupno…" while support still cites S208; (4) the S221 caveat replaced by "(S221 confirms the corpus behind the study)"; (5) a `NEW-ScoutNuo-3` sentence with `(S241, -2)`; (6) an unrecorded quote cited to nonexistent S241; (7) the Sardinia quote cited to S189.
- Runs (all this session, system python3, no installs): fixture → **16 hard, 9 soft, exit 1**, with every planted class represented among the findings (the other hard lines are the inherited recording-gap flags from the underlying clean text, listed in §2.1); base → **0 hard on F2/F3a/F3b/F4/F5**, 10 hard all of the F1 recording-gap class, 6 soft all F1-soft tripwires, 70-quote inventory; pre-fix → **F2:150, F3a:199, F4:133 (S221 dataset and S220 docs)** — three of the four round-53 findings recovered mechanically, the fourth (line 68 locators) honestly out of mechanical reach (§2.1).
- The lane tool check ran on scratch copies via absolute paths, so no lane state was touched: `DRAFT_IDS: 2 findings` (fixture), `DRAFT_IDS: 0 findings` (base).

## 4. Registry-side rules for S239+ (what the demonstrations cost the round-53 corpus)

1. **Record every locator the entry will cite in the row's anchor column, per item.** The clean base still has three rows whose records cannot account for locators the entry cites (S202 p. 94; S212 pp. 27–28 — where the row records accepted-manuscript pp. 2, 16–19 and the entry cites a different pagination; S223 pp. 698–708 against a record of {700, 28}). Each is either a recording gap or an unreconciled slip; the L1 cannot tell which without re-opening, and neither could the round-53 sample.
2. **Record every verbatim quote the entry will use in the kept row.** 70 of the base entry's quoted spans are recorded in no row; the F3 carrier check only has teeth when rows carry the quotes. The mask seats' `draft sentences` already end with `(NEW-<Seat>-<n>, <locator>)` — paste those locators and the quotes behind them into the rows as written, not later.
3. **Never leave a verbatim quote only in a rejected duplicate row.** S233 (rejected) carries "in Bulgaria, this response pattern is reversed" while the kept S219 row paraphrases it; the F3 check correctly ignores rejected carriers, so a future entry quoting that sentence would show an unrecorded quote with no carrier. Keep rejected rows for taste evidence; keep quotes in kept rows.
4. **Kind discipline at row-write time.** This round's mask ground is record-heavy (museum catalogues, nomination files, community statements). Write the kind honestly (dataset/record/web/community/docs vs paper/book) — F4's gate reads exactly that column, and a row miscast as `paper` silences the study-language check for every sentence that cites it.

## 5. Unrun checks and limits

- Nothing in the lane was executed against the working tree except read-only `git show`/`git log`; accept-c, sweep and the provenance gates were not run (they are the L1's landing gate, and the worktree is mid-integration by the L1).
- Checks read parenthesised citations only; bare `S211`-style mentions outside parentheses are invisible to them (in the base entry these duplicate already-cited rows). A one-pass `grep -noE '\bS[0-9]{3}\b' <entry>` eyeball against the cited set closes that.
- F1's subtle-slip blindness (item mapped to the wrong page inside a reconciling span) is demonstrated, not fixed; it is closed only by the re-open step in the recheck field, or by item-level anchors per §4.1.
- F2/F3 token lists are calibrated on one entry (gesture); the mask entry's vocabulary (community names, object names) may need the noun list extended — the failure mode of the check is then under-flagging, never wrong HARD output.
- No external sources were opened or needed; no tools were installed or updated (system python3 only; no pacman, uv or binary installs).

## 6. Tooling record

- No installs or updates. All commands: `git show`/`git log` (read-only), `grep -n` on scratch copies, `wc -c`, and `python3` running the scratch checker and the lane's `tools/check-draft-ids.py` in read mode. The only lane file written is this report.
