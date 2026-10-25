# Seat ScribeEntryAmend — amendment entry drafted, three sources opened, cuts recorded

Round 73 (hyaku run 7), leaf scribe. Deliverable: `.ufo/waves/round-73/w1/drafts/conlang-scholarship.amend-2026-10-23.md` (90 lines, 1559 words). Sources opened by me on 2026-10-25; nothing was taken on a sibling's word.

## 1. Behavior

Drafted the amendment entry as a dated section appended to the base `linguistics/conlang-scholarship.md`, from the staged `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md`, to the base's bar: provenance trio first (`source:` ×3 → `verified-at` → `recheck`), then `ground / topic / gap filled / sources / couples / scope`, then five dated body sections. It cites **only** S878, S879, S880 — 11 / 14 / 10 occurrences, no other S-id anywhere (`grep -o 'S[0-9]\{3\}' | sort -u` → exactly those three).

The entry's content, all newly grounded (none of it restates the base):

- §1 the a priori/a posteriori dichotomy argued down to a scale (S878), with the calibration line naming it a contested refinement;
- §2 the three Russian-language typologies and Peterson's, as S879 restates and compares them, including the two-sided verdict and the article's own Lojban footnote;
- §3 what the classroom study consisted of, verbatim from S880, plus the explicit negative that S880 never says "semester-long";
- §4 four decision rules the lane can act on;
- §5 provenance limits: the publisher abstract was not opened, and the two dropped staged elements.

## 2. Gates — what I opened, and what each carries

Every fetch used UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. All three are body text, not captions or attributes (QUALITY 16).

| Row | URL | Access | Located quote (≤25 words/tokens) | Verdict |
|---|---|---|---|---|
| S878 | https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 | 2026-10-25, HTTP 200, application/pdf, 959171 B, 13 pp | "the author examines the existing classifications of constructed languages and attempts to establish a connection between purposes of their creation and their linguistic features" — **24 words**, Abstract, p. 455 | ADMIT |
| S879 | https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike | 2026-10-25, HTTP 200, text/html, 97656 B | "Наиболее детализированной классификацией, по всей видимости, является типология Д. Питерсона" — **10 tokens**, comparison section, paragraph on differences | ADMIT (no Wayback capture — §5) |
| S880 | https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf | 2026-10-25, HTTP 200, application/pdf, 193610 B, 9 pp, md5 `00151e4bf251e2b338542d10efba02c5` | "In the course, examples of phonological systems in natural languages and constructed languages were presented along with instruction in language universals and typology" — **23 words**, §3 "These papers", p. 5 | ADMIT |

Supporting quotes used in the entry, each verified verbatim against the extracted text and counted: S878 "this division should be seen as a scale rather than a binary system" (13w, p. 458); S878 "challenge the integrity of the seemingly well-established dichotomies of a priori and a posteriori, auxiliary and artistic languages" (18w, Conclusion p. 464); S880 "Sara Sowers-Wills assesses students’ command of concepts in phonology through their creation of a constructed language" (16w, p. 5); S880 "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level" (25w, p. 5); S880 "an active learning approach in a project-based phonology course" (9w, p. 5); S879 «1. Auxlangs. Вспомогательные языки» (4 tokens); S879 «2. Вымышленные языки (ВЯ) в широком смысле» (7 tokens); S879 «авторскими языками» (2 tokens).

Row recheck commands, run 2026-10-25 (outputs verbatim):

```
S878: curl -fsSL <url> -o rc878.pdf && pdftotext -enc UTF-8 rc878.pdf - | grep -c 'eurocentrism in constructed'   -> 1
S879: curl -fsSL <url> | grep -c 'Наиболее детализированной классификацией'                                        -> 1
S880: curl -fsSL <url> -o rc880.pdf && pdftotext -enc UTF-8 rc880.pdf - | grep -c 'multi-part, creative project'   -> 1
```

## 3. Cuts, each with its reason

1. **S894 (Sowers-Wills, DOI 10.1017/cnj.2024.21) dropped as a source.** Probed independently: DOI → `https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article`, `HTTP=429` under the browser-shaped UA **and** under `curl/8.9.1`. The entry's §5 records that the publisher abstract was not opened and that §3 rests on S880's account alone; no row cites S894 and no URL for it appears in the entry.
2. **"semester-long" cut.** `pdftotext -enc UTF-8 S880 | grep -ci semester` → **0** (nine pages; S878 also 0). The staged file attached the duration to S901's PDF and to S894's abstract; with S894 dropped, no cited source carries it, so the entry says the negative out loud instead of inheriting the token.
3. **"what it teaches that lectures do not" and "a method for teaching analysis" cut.** S880 supports exactly one pedagogy claim — that creating a language assesses students' command of phonological concepts — and makes no comparison with lectures. The staged §N+2 sentence ("not decoration … a method for teaching analysis") is an inference past S880, and its "not decoration" framing belongs to the base's S876 claim, which this amendment must not restate.
4. **«автоконланги» cut; «авторскими языками» substituted.** `grep -c 'автоко'` on S879 → 0. The article's own term for the personal-language group is «авторскими языками» (instrumental form quoted verbatim).
5. **"the language of Myst" corrected to "the Э'П language of the game Myst".** S879 names Э'П explicitly; the staged wording is under-specified to the point of not being locatable.
6. **The staged topic's "a Russian-language review article that sets out and assesses the Шувалова/Сидорова classification" corrected.** S879's own title, abstract and conclusion make Peterson's classification and its advantages over the Russian typologies the article's subject; Шувалова/Сидорова is one of three compared typologies. The entry now says so.
7. **"how that classification compares with Peterson's, which is finer-grained" corrected to the two-sided verdict.** S879 says Peterson's is the most detailed classification *and* that it systematizes worse than the Russian typologies because it was delivered orally as a podcast — the second half is the part a reviewer would have caught.
8. **The staged `## Superseded passage` fold-in block cut.** It carries S892/S893/S894 and re-tells the round-3 entry. In the lane the base is a separate admitted file (claim C's ENTRIES leg requires both files to exist), so folding it in would restate the base and duplicate rows; it also cites the dropped S894 and staged ids.
9. **Staged `recheck:` rewritten.** "re-run the row recheck command in round 4's `SOURCES-PROPOSED.md` (S901 -> 1)" names a campaign file and a staged id. Replaced by the three runnable greps above with their 2026-10-25 outputs.
10. **Staged `ground:` rewritten.** "round 3's CANNOT-ANSWER §6" is a campaign pointer and **no `CANNOT-ANSWER.md` exists in the lane** (`find . -iname '*CANNOT-ANSWER*'` → 0). Ground is now the base's own two source rows and what they cannot carry.
11. **Staged `couples:` re-pointed to existing lane paths.** `linguistics/naming-systems.md` exists; the staged `naming-systems.amend-2026-10-23.md`, `culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` do not exist in the lane and are not named.
12. **Staged §N+3 "What is still missing" (Journal of Constructed Linguistics, Palgrave Handbook route) cut.** No cited row backs it, and the Palgrave row is S910 — not one of my three ids.
13. **Fetch dates corrected** from the staged 2026-10-23 to 2026-10-25, the date of my own fetches.

## 4. Verification exercised (nothing else claimed)

- `python3 -B tools/check-cited-lines.py <draft>` → `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0. Three findings were found and fixed on the way (header `recheck:` and `ground:` lines each carried two ids; one §5 line carried two): all three restructured to one id per line.
- Id audit: only S878/S879/S880 present; regex for staged/campaign ids (S728, S729, S769, S760–S809, S881–S919) → none.
- Quote audit: every quoted span extracted from the draft (19 spans) and matched against whitespace-normalized source text: **16 matched verbatim**, longest 25 words. The 3 unmatched are the tokens under discussion as *absent* (`semester-long` twice, `автоконланги` once); the S879 heading matches on the site's own case-mangled form, which is the form quoted.
- Restatement check against the staged base: no 8-gram overlap survives except the couples path name (varied) and the lane's canon-hygiene formula "decides no world's language".
- No tables in the entry (`grep -c '^|'` → 0), so the TABLE-ID lint class cannot fire.

## 5. Findings other seats need

1. **S878 recheck trap.** The obvious phrase `eurocentrism in constructed languages` straddles a `pdftotext` line break: `grep -c` returns **0**. A filed recheck must use `'eurocentrism in constructed'` (→1) or pipe through `tr '\n' ' '`. This is a live instance of the "reason naming a tool, contradicted by its own output" class QUALITY 12 guards.
2. **S879 has no Wayback capture.** CDX exact, prefix and wildcard all return `[]`:
   - `https://web.archive.org/cdx/search/cdx?url=cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike&matchType=exact&output=json&limit=5` → `[]`
   - same with `matchType=prefix` → `[]`
   - `url=cyberleninka.ru/article/n/klassifikatsii-konlangov*` → `[]`
   The live URL does serve the quote to a plain-UA client (`curl -A curl/8.9.1 … | grep -c` → 1), so the row clears QUALITY 18 on the live leg; the no-capture ruling must be filed with these three probed URLs (QUALITY 21).
3. **S879's text layer mangles heading case.** The served heading is `сОпОсТАВЛЕНИЕ КЛАССИФИКАцИИ д. питерсона с типологиями современных отечественных ЛИНГВИсТОВ`. A heading quote in normalized case would be a misquote; the entry quotes the served form and says it is case-mangled.
4. **S880's bytes are the scout's bytes.** md5 `00151e4bf251e2b338542d10efba02c5` matches ScoutS901's recorded md5, so my re-fetch and the scout's fetch are the same document.
5. **S894 is unreachable by ordinary means, confirmed twice.** HTTP 429 under both UAs, final URL recorded above. The claim's REJECTS leg ("staged S894/S910 if their payload stays unreachable by ordinary means") has its evidence.
6. **The base entry is not in the lane yet.** `find corpus/knowledge -iname '*conlang-scholarship*'` → 0 files at this revision, so the entry's `ground:` line describes a sibling deliverable; claim C's ENTRIES leg needs both files at `<lands>`. The sibling base draft landed in `drafts/` at 19:15 while I worked: it cites **S876 and S877 only** (5 / 24 occurrences), so my ground line ("its two source rows") holds and the two drafts share no cited id.
7. **Staged-text defects found (for the lesson's reject/admit record):** the staged amendment mis-describes S893's subject (item 6 above), attributes a term S893 does not use (item 4), and attributes a duration S901 does not carry (item 2) — three separate ungrounded elements in one staged block.

## 6. Known limits

- `(to-verify)` in the entry, deliberately: the page for S879's items 1–2.2 (cyberleninka serves extracted HTML with no page markers; pp. 28–34 from the citation line), and whether the study itself reports a semester-long curriculum or a lecture comparison (needs the article's own text, not opened).
- S878's own recheck pattern in the staged row was not re-used; my pattern is the one that survives the line break (§5.1). A row filer should adopt it rather than the obvious phrase.
- I did not open the Sowers-Wills article, S910, or anything in the naming-systems / calendar / era / verification staged families.
- Tier assignment for the three rows is not mine to make (scout's); the entry states the staged tier (B) for all three.

## 7. Touched surfaces

- Written: `.ufo/waves/round-73/w1/drafts/conlang-scholarship.amend-2026-10-23.md` (the assigned draft) and this report. Nothing else in the lane was written; no file in the fleet root, shokuknow source tree, registry, claims file, or jj/git state was touched. No git commands were run.
- Downloads, all under `/tmp/ScribeEntryAmend/`: `S878-novikov.pdf` (959171 B, md5 `58e764f69123db4f78d3e67dada60c31`), `S879-kostyukhin.html` (97656 B), `S880-anderson.pdf` (193610 B), extracted `S878.txt` / `S879.txt` / `S880.txt`, recheck copies `rc878.pdf` / `rc880.pdf`.
- Tool installs: **none** (curl, pdftotext, pdfinfo, python3 all preinstalled). PACMAN not invoked.
- Out of scope, untouched: `reports/round-73/claims.json`, `corpus/SOURCES.md` (registry append is not this seat's), `corpus/lessons/round-73.md` (Gate records are the lesson seat's — §2 above supplies the material), the counters, the base entry itself, and every other wave-1 draft.

## 8. Artifact paths

- Draft: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/w1/drafts/conlang-scholarship.amend-2026-10-23.md`
- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/w1/ScribeEntryAmend.md`
- Fetch scratch: `/tmp/ScribeEntryAmend/`
