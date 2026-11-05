# Round 91 — entry-mode grader hardening and secret registers

author: kotodama lane, 2026-11-05.
Base: `d39434b3bc8458e1b66edd2d0d0fea9ea32f3331`. Freeze: `691aebf247ebea4dd50577bb64ac99d12fa1145a`.
Claims O (operability) and C (coverage) remain exactly as frozen in `reports/round-91/claims.json`.
Freshness remains paused by unresolved L0 round-11 and round-89. The lowest-axis duty is neither met nor waived; no admission is asserted on that procedural gap.

## Gate

Sources opened by plain HTTP on 2026-11-05. Raw response bodies, their sha256, URL, 2xx status and offset-bearing access instants are in `reports/round-91/evidence/manifest.json`. Quotes below are whitespace-normalized spans of those captured bytes; no browser or access-control bypass was used. S953 is a publisher description, not a read of the complete book. S954 proves a printed hostile framing, not the behavior of the community being described.

- S952 admit B/mined. https://www.lancaster.ac.uk/staff/bakerjp/polari/home.htm — accessed 2026-11-05 — body: “Polari is a more recent spelling. In the past, it was also known as Palari, Palare, Parlaree”
- S953 admit B/mined. https://www.taylorfrancis.com/books/mono/10.4324/9780203167045/polari-lost-language-gay-men-paul-baker — accessed 2026-11-05 — body: “Polari is a secret form of language mainly used by homosexual men in London and other cities during the twentieth century”
- S954 admit A/mined. https://leme.library.utoronto.ca/lexicons/109/ — accessed 2026-11-05 — body: “Here I set before thee good Reader, the leud lousey language of these lewtering Luskes”
- S955 admit B/mined. https://journals.openedition.org/cdlm/729 — accessed 2026-11-05 — body: “argot à la fois d’exclusion et de reconnaissance”

S952 locator: introductory Polari overview paragraphs. S953 locator: book description. S954 locator: lexicon title. S955 locator: paragraph discussing exclusion and recognition.

- S956 rejected C. https://en.wikipedia.org/wiki/Argot — accessed 2026-11-05 — lead span “Argot is” is present in `reports/round-91/evidence/S956.txt`. Rejection is insufficient tier for sole substantive support, not absence of text. Flip: independently inspected authored support for the exact claim. The short reject quote is not used as an admitted-row quote.

Registry delta: S952–S955 new mined rows, S956 new rejected row. No old row's status, recheck, or used-by changes. New used-by paths are the entry for S952–S955 and this lesson for S956. Existing rows stay unchanged.

## Corrections to round 90

The following supersede statements, not historical bytes:

1. The round-90 entry has eight `## ` headings, not ten. The earlier report, SCORECARD and LOG number is an erratum; measure with `git show 6394ad43:corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` and count lines beginning `## `.
2. The round-90 `O.before` pointer `reports/round-89/mutation-score.txt` was absent at base. The resolving evidence is `.ufo/waves/round-89/w1/MutationCounter.md`.
3. The frozen round-90 sentence claiming the stub failed SELFTEST is false: that stub printed SELFTEST PASS. Its refusals/mutation results, not the tally string, discriminated it. Round 91 uses an actual stub subprocess, exact ok-line count and actual mutation execution, not the presence of prose tokens in a receipt.
4. The round-90 S951 quote's locator uses tag-stripped lead text. Raw markup split the span; quote existence was not an exact raw-byte hit.
5. Instrument gains do not imply `quality: improved`. This round's quality trend stays unchanged unless an actual corpus re-verification/deepening observable is documented.
6. No stagnation waiver or operator ruling has been located for the freshness pause. This remains a conformance gap, not an implied permission.
7. The round report is committed by the lane through fleet-commit.sh, not left for a sweep. The current mission is progressing; no second kotodama mission is claimed.

## Mistakes

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R91-M1 | survivor | round-90 CriticClaims attacks 5/6/8: entry-mode shadow rows, self-quotes and off-topic token padding passed | QUALITY36 | New UNIQUENESS, heading/table phrase anchors, gate self-quote and graded-content hash checks. The committed mutation receipt and before fixtures show which finite classes are tested; semantic truth remains review-only. |
| R91-M2 | vacuous | first v2 mutation run killed 49/52; char-floor fixture also triggered self-quote, phrase fixture also triggered stem/overlap | QUALITY23 and QUALITY36 | Isolate char-floor with efficacy register, align fixture date, and lower prose-only overlap floor. Final finite mutation receipt reports 53/53. Earlier red is not a claimed pass. |
| R91-M3 | attribution | mutation receipt header prints the last mutant verdict beside hardcoded clean rc0 because head is reused in the loop | QUALITY29 | Retained frozen harness defect. Clean-green-before-loop is checked by rc, but its displayed head is misattributed. Direct clean 77/77 and mutation count are separate evidence; no silent frozen-instrument rewrite. |
| R91-M4 | reference-drift | initial quarantine TSV extracted URL instead of quote cell, producing blank spans | QUALITY27 | Corrected before verdict integration; the slice now carries 18 quote cells and three prose-only rows. Verdicts must name the register artifact, not infer absent quotes from empty strings. |
| R91-M5 | stale-premise | PubMed served a JS shell; AnthroSource refused; a compressed PDF had only a trivial Baker hit | QUALITY10 and QUALITY30 | None supports this entry. Final five captures were freshly fetched and their raw text quotes located. No claim of source absence or fabrication follows from a wall. |
| R91-M6 | missing receipt | the frozen `O.before` names `reports/round-91/controls/before-v1-entry.txt`, which existed neither at base, at freeze, nor in the worktree (ReviewerFreeze D1) | QUALITY29 | The receipt was produced on 2026-11-05 **after** the freeze from the round-90 critic's documented fixture recipe and says so in its own header. Its measurement corrects the frozen sentence: the naive bakery body is already refused by v1 (`entry shares 4 content words < 10`), so the real v1 survivor is the **topic-line-padded** entry, which v1 scores PASS 6/6 and v2 refuses on `TOPIC` (0/6 phrase anchors) and `GATE` (self-quote). The frozen text is not edited. |
| R91-M7 | matching-method | `ExecQuarantineA` copied backtick-wrapped TSV cells into its fragment strings, so rows that the bytes do contain scored ABSENT; its late trailer fixed the backticks but then reported S786's two fragments inverted (it put the Chinese sentence present and the English gloss absent; `pdftotext` finds the English line at offset 79 and not the Chinese one) | the independent re-check duty (ReviewerQuarantine) and the L1 fold pass | Verdicts were re-derived from the same bytes after stripping backticks and folding punctuation; the seat's defect is recorded rather than silently overwritten, and `reports/round-91/quarantine/verdicts.json` names the agreed verdict per row with the reason. |

## Quarantine

Assimilation: no package adoption. The register slice contains 21 data rows (re-derived this round; the register's own header and `## By lane` totals are stale and were not trusted). Adopt nothing; every row below is a hand-check verdict, not an append. `considerthese/` is absent. The id-collision guard ran anyway and found 98 collisions between the lane registry and the package's staged rows (`.ufo/waves/round-91/assimilation/{reg-ids,staged-ids,collisions}`: 880 vs 132 ids), so even a later adoption round must renumber in scratch.

Method: three independent reads of the same register slice — `ExecQuarantineA` (S776–S804), `ExecQuarantineB` (S807–S835), `ReviewerQuarantine` (seven rows, fetch-first), and the L1 pass (`reports/round-91/quarantine/l1-handcheck.py`, one fetch per URL, retries only on 429/5xx/network, pdftotext for PDFs, charset sniffing, bot-wall detection, punctuation folding). Verdicts consolidated in `reports/round-91/quarantine/verdicts.json`. A row is ABSENT only when the served bytes lack the quote; that is the register's own claim, not a fabrication verdict, and every row stays quarantined.

| id | verdict | basis |
|---|---|---|
| S776 | PARTIAL | 4 of 5 fragments contiguous; the 标准状态：现行 pair matches only after punctuation folding |
| S778 | LOCATED | both fragments present once the EUC-JP body is decoded correctly |
| S779 | ABSENT | 2xx Japanese calendar page; the cited spans are Chinese intangible-heritage text from another page |
| S786 | PARTIAL | pdftotext finds the English title line; the cited Chinese prose is not in the English deck |
| S787 | ABSENT | 2xx body lacks the span |
| S791 | UNREACHABLE | server answered HTTP 400 for the URI |
| S792 | ABSENT | article page served (159831 B); the cited Chinese span is not in the bytes |
| S795 | ABSENT | PDF fetched; extracted text lacks the span |
| S796 | ABSENT | PDF fetched; extracted text lacks the span |
| S804 | LOCATED | sentence present; the source uses a half-width comma the fold absorbs |
| S807 | UNVERIFIABLE | prose row (no quote); the URL served a PDF, so nothing was quoted to locate |
| S812 | UNVERIFIABLE | prose row (no quote); the live fetch answered 429 |
| S814 | ABSENT | L1 read a 200 body of 143252 B without the span; two seats got 403 for the same URL |
| S816 | ABSENT | 2xx body is a different chinawriter item |
| S817 | ABSENT | 2xx body lacks the span |
| S820 | ABSENT | PDF fetched; extracted text lacks the span |
| S823 | UNREACHABLE | server answered HTTP 468 |
| S824 | ABSENT | PDF fetched; extracted text lacks the span |
| S825 | PARTIAL | era-name values present; the quoted table span is not contiguous |
| S827 | LOCATED | Springer chapter page carries the title, handbook and publisher strings (verified in B's committed capture) |
| S835 | UNREACHABLE | HTTP 503 maintenance page |

Counts: LOCATED 3, PARTIAL 3, ABSENT 10, UNREACHABLE 3, UNVERIFIABLE 2 = 21. Existing round-74/76 assimilation records are not retroactively erased by this repeat audit.

## Understanding and trial

The new entry separates social boundary from word-transformation rule: a mechanically reversed word need not be secret; a closed lexicon need not have separate grammar; a hostile glossary is an outsider's record, not transparent social testimony. Worked NON-CANON design records retain audience, transformation, register and uncertainty. Lore alone decides canon.

Outside non-author spot-check: pending closure. Dispatched seats are still the lane; no SHONEN box becomes [x].
