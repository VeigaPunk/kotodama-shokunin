# ReviewerRows — round-93 row/capture attack (2026-11-05)

Inputs: `reports/round-93/source-rows.md`, `reports/round-93/gate-lines.md`,
`reports/round-93/evidence/manifest.json`, captures `S961.html`–`S964.html`.
Frozen tool imported read-only as a module:
`importlib.util.spec_from_file_location('cae', '/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py')`
— used `cae.norm`, `cae.html_body_text`, `cae.capture_error`, `cae.FETCH_RE`. No selftest run in the lane tree.

## Command + rc ledger (all 2026-11-05)

1. `sha256sum <ev>/S96*.html` → rc 0; four digests identical to `manifest.json` `.sha256` (see per-id blocks).
2. `python3 check_captures.py` (scratch; imports frozen tool; recomputes sha, FETCH_RE/fetched_at, quote-in-body via `norm(html_body_text(raw))`, gate-vs-manifest quote equality, `capture_error(...)` per entry) → rc 0; per id: sha_match=true, fetched_at_regex_ok=true, fetched_at_date_ok=true (group(1)=='2026-11-05'), offset non-None (−03:00), http_status=200, quote_in_body=true (unique normalized-body hit), gate_quote_matches_manifest=true, capture_error=None.
3. `grep -c -F` in `corpus/SOURCES.md` (1064 lines) for `bop.unibe.ch`, `pressto.amu.edu.pl`, `oaj.fupress.net`, `article/view/1426`, `srp/article/view/21548`, `article/view/3847`, `article/view/17732`, `10.13092/lo.20.1063`, `10.14746/strop.2019.464.002`, `10.13092/lo.84.3847`, `studi_slavis-17732` → all `0`. No registry duplication by host, path, or DOI.

All byte offsets below are byte offsets into the committed capture files (last occurrence = visible body copy; `<body` starts at 5869/12054/6882/17796 respectively, each cited span after it). The hyphens in `con-tact`, `mem-bers` are in the source HTML itself.

---

## S961 — Rash (2004), Linguistik Online 20(3) — VERDICT: PASS

1. sha256 recomputed `61f464e407b3245e6f3db7b7efa6ba7a658080e0832ff851efdc07e661214af1` == manifest. ✔
2. `http_status` 200; `fetched_at` `2026-11-05T12:12:13-03:00` — local ISO instant with offset, date 2026-11-05. ✔
3. Manifest quote `the speech acts of greeting and leave-taking denoted by the German verb` located in body text via frozen normalization (unique normalized-body char offset 711; raw bytes 1046 meta, 3756 body). `cae.capture_error(...)` → None. ✔
4. Gate line quote == manifest quote (programmatic equality). ✔
5. Teaches: "Greeting and leave-taking form one speech-act family denoted by one verb (grüssen), and Swiss speakers treat the formulae as the core of politeness." Supported. Support: `greetings formulae are especially important` (raw byte offset 11672; full sentence: "speakers of swiss german, both young and old, and from all walks of life, believe that it is important to retain their traditional politeness rituals, and that greetings formulae are especially important"). The verb claim is the manifest quote itself (raw 3756). "core of politeness" is a fair compression of "especially important" within "strict conventions of polite behaviour" (raw 3878/…). ✔
6. Tier A scope: "greeting and leave-taking speech acts in German-speaking Switzerland" — abstract: "research into linguistic politeness in german-speaking switzerland (gss) and into one type of politeness in particular, namely the speech acts of greeting and leave-taking". Original research paper ("this paper describes the results of research…", published 2004-07-01, bd. 20 nr. 3). Scope matches. ✔
7. Registry: 0 hits for `bop.unibe.ch`, `article/view/1426`, DOI `10.13092/lo.20.1063`. ✔

## S962 — Zieliński (2019), Studia Romanica Posnaniensia 46(4) — VERDICT: PASS

1. sha256 recomputed `098eed5cda92aa440dd645d223970b2457d7d7748d6c6fa35bccea80a5b8fbdc` == manifest. ✔
2. `http_status` 200; `fetched_at` `2026-11-05T12:12:17-03:00` — valid local ISO instant with offset, 2026-11-05. ✔
3. Manifest quote `despite their apparent formal resemblance, came to codify totally opposite` in body text (unique normalized-body char offset 1389; raw bytes 1002 meta, 1621 body). `capture_error` → None. ✔
4. Gate quote == manifest quote. ✔
5. Teaches: "Two greeting formulae from one predicate (besar las manos) codify opposite social values, so formal resemblance does not fix meaning." Supported. Support: `came to codify totally opposite socio-pragmatic values` (raw byte offset 29307, body copy; abstract: "two spanish greeting formulas derivated from the atelic predicate besar las manos (y los pies) … which, despite their apparent formal resemblance, came to codify totally opposite socio-pragmatic values"). "(besar las manos)" is the shorter member of the named predicate — no overclaim. ✔
6. Tier A scope: "two Spanish kissing-hands greeting formulae and their social values" — abstract matches (epistolary-corpus method "the systematic search in epistolary texts", raw 1101/1716). Original paper ("the aim of the paper is to analyse…", published 2019-12-15, pp. 17–27). Scope matches; scope does not claim modern usage, so the historical corpus is no mismatch. ✔
7. Registry: 0 hits for `pressto.amu.edu.pl`, `srp/article/view/21548`, DOI `10.14746/strop.2019.464.002`. ✔

## S963 — Mapunda & Sommer (2017), Linguistik Online 84(5) — VERDICT: FINDING (RR-1, LOW)

1. sha256 recomputed `3eb97d8a59c7af45cbcf64c2ec234b674233921c5957f8bad8d4ed4d66d57a9c` == manifest. ✔
2. `http_status` 200; `fetched_at` `2026-11-05T12:12:40-03:00` — valid local ISO instant with offset, 2026-11-05. ✔
3. Manifest quote `greetings tend to be brief today` in body text (unique normalized-body char offset 1599; raw bytes 1938 meta, 5141 body). `capture_error` → None. ✔
4. Gate quote == manifest quote. ✔
5. **RR-1 (LOW): teaches second clause compresses the source's attribution.** Teaches: "…and older speakers read the brief forms as lack of respect." The abstract attaches the respect judgment to the *shift to Swahili*, not to brevity: `The tendency to prefer Swahili is viewed by older mem-bers of the community as lack of respect` (raw byte offset 5241, body copy). Brevity itself is supported separately: `due to pervasive con-tact between Ngoni and Swahili, greetings tend to be brief today` (raw byte offset 5088, body copy). Under the entry's content rule ("state nothing about a source the quoted spans and abstracts do not support"), the teaches cell as written supports "older speakers read the turn to Swahili (whose briefer forms are displacing Ngoni greetings) as lack of respect", not a judgment on brevity per se. Suggested fix: reword to "…and older speakers read the turn to Swahili as lack of respect." Severity LOW — first clause and source framing (title: shikamoo replacing tukuwoni) make the conflation unlikely to propagate as a false fact, but the cell is one word stronger than the abstract.
6. Tier A scope: "Tanzanian Ngoni access rituals (greetings) under contact with Swahili" — abstract: "an ethnographic description of tanzanian ngoni access rituals (greetings)" with role-play/interview/observation and contact findings. Original paper, published 2017-09-17, bd. 84 nr. 5. Scope matches. ✔
7. Registry: 0 hits for `bop.unibe.ch`, `article/view/3847`, DOI `10.13092/lo.84.3847`. ✔

## S964 — Trubnikova (2025), Studi Slavistici — VERDICT: PASS

1. sha256 recomputed `c8eba504c3c049d281e49d5fd1b267295bb578c84c379e48e8bf6b77140188ed` == manifest. ✔
2. `http_status` 200; `fetched_at` `2026-11-05T12:12:45-03:00` — valid local ISO instant with offset, 2026-11-05. ✔
3. Manifest quote `compiled a pool of words, expressions, and sayings` in body text (unique normalized-body char offset 1748; raw bytes 1476 meta, 30357 body). `capture_error` → None. ✔
4. Gate quote == manifest quote. ✔
5. Teaches: "A questionnaire elicited situationally bound farewell expressions, and the authors compiled a pool of words, expressions and sayings; a pilot study, not a population sample." Supported. Support: `the results of a pilot study examining farewell expressions and conversational moves` (raw byte offset 29874, body copy) and `purpose-designed questionnaire that elicited situationally bound responses` (raw byte offset 29988, body copy). "not a population sample" is a caveat consistent with the source's own "pilot study" label — no overclaim. ✔
6. Tier A scope: "Russian leave-taking formulae and conversational moves, pilot questionnaire" — abstract: "investigates strategies of leave-taking behavior in contemporary russian … pilot study examining farewell expressions and conversational moves … purpose-designed questionnaire". Original paper, published 2025-07-18, DOI 10.36253/studi_slavis-17732, CC BY 4.0. Scope matches. ✔
7. Registry: 0 hits for `oaj.fupress.net`, `article/view/17732`, `studi_slavis-17732`. ✔

---

## Findings summary

- **RR-1 (LOW, S963 teaches cell):** "older speakers read the brief forms as lack of respect" — the abstract attributes the lack-of-respect judgment to the preference for Swahili, not to brevity; reword before the entry cites it. Evidence offsets: 5088 and 5241 in `reports/round-93/evidence/S963.html`.

## Not measured / residual

- Pages were graded from the committed captures only; I did not re-open the four URLs live (freshness of capture == manifest hash is what the contract pins). The stray file `unreachable-mdpi-403.raw` is not referenced by any row and was not audited beyond noting it exists (403 log, consistent with the lane's unreachable-source discipline).
- Tier-A originality is judged from the landing pages' abstracts and metadata (article vs review cannot be distinguished further without the paywalled PDFs; all four landing pages present original-research abstracts with methods, and none self-describes as a review).
