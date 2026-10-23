# Round 61 W1 — source coverage findings (ScribeSrc08)

## Axes
- **Coverage:** Dutch wooden clogs/klompen and French *sabot* / *sabotage* etymology.
- **Evidence quality:** source scope and tier.
- **Locatability/access:** direct quote reopening and source-URL freshness.

## Behavior
Four integration-ready source drafts, two per assigned subtopic. All four final quotes are 8–25 words, contain a frozen footwear-lexicon word, and were LOCATED by the round-61 quote locator. Each proposed entry line is one bullet with one S-id, shares at least three 4+ letter words with its anchor, and avoids copying more than 12 consecutive quote words.

Draft IDs are S652–S655. ScribeSrc07's report records S656–S659; Src09 and Src10 separately confirmed S668–S673 and S674–S679, so this block does not overlap those reports. The source registry did not yet contain these IDs or URLs at the final grep. Main integration may reassign IDs.

## Draft source rows, entry clauses, and Gate lines

### S652 — Dutch clogmaking

| S652 | Internationaal Klompenmuseum, Museum.nl (no publication date shown) — https://www.museum.nl/en/internationaal-klompenmuseum | docs | B | Museum.nl's description of the Eelde museum's clogmaking craft and 1920 machinery | English Clogmaking section, machinery sentence: "Aside from the large collection of wooden shoes, discover the craft of clogmaking, for example through the specialized machinery dating from 1920." | The listing presents the craft of clogmaking through specialized machinery dating from 1920. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- The museum presents clogmaking through specialized machinery dating from 1920. (S652)`

Gate: `- S652 | https://www.museum.nl/en/internationaal-klompenmuseum | 2026-10-23 | "Aside from the large collection of wooden shoes, discover the craft of clogmaking, for example through the specialized machinery dating from 1920."`

Locator command: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.museum.nl/en/internationaal-klompenmuseum' "Aside from the large collection of wooden shoes, discover the craft of clogmaking, for example through the specialized machinery dating from 1920."; echo exit=$?`

Full locator output:
```text
LOCATED https://www.museum.nl/en/internationaal-klompenmuseum
exit=0
```

### S653 — Dutch clog forms and collection examples

| S653 | Wooden Shoe Workshop De Zaanse Schans, Zaanse Schans, 2 June 2024 — https://www.zaanseschans.com/en/wooden-shoe-workshop-de-zaanse-schans/ | docs | A | The workshop's own Clog Museum collection examples and its description of the Hindeloopen church clogs | Clog Museum collection paragraph, special-specimens sentence: "such as beautiful bridal clogs, work clogs and the famous church clogs from Hindeloopen, dating all the way back to 1675" | The Clog Museum page lists bridal and work clogs, plus church clogs from Hindeloopen dating to 1675. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- Examples include bridal and work clogs, plus church clogs from Hindeloopen dating to 1675. (S653)`

Gate: `- S653 | https://www.zaanseschans.com/en/wooden-shoe-workshop-de-zaanse-schans/ | 2026-10-23 | "such as beautiful bridal clogs, work clogs and the famous church clogs from Hindeloopen, dating all the way back to 1675"`

Locator command: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.zaanseschans.com/en/wooden-shoe-workshop-de-zaanse-schans/' "such as beautiful bridal clogs, work clogs and the famous church clogs from Hindeloopen, dating all the way back to 1675"; echo exit=$?`

Full locator output:
```text
LOCATED https://www.zaanseschans.com/en/wooden-shoe-workshop-de-zaanse-schans/
exit=0
```

### S654 — French root in *sabotage*

| S654 | sabotage, Wordorigins.org, 6 October 2021 — https://www.wordorigins.org/big-list-entries/sabotage | docs | B | Wordorigins' historical account of the French borrowing and the root *sabot* | Opening paragraph, French-borrowing clause through root definition: "borrowing from French, and that borrowing occurred in the opening years of the twentieth century. The root, sabot, literally means a wooden shoe or clog." | The article identifies *sabotage* as a French borrowing and names *sabot*, meaning a wooden shoe or clog, as its root. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- The French borrowing's root is *sabot*, literally a wooden shoe or clog. (S654)`

Gate: `- S654 | https://www.wordorigins.org/big-list-entries/sabotage | 2026-10-23 | "borrowing from French, and that borrowing occurred in the opening years of the twentieth century. The root, sabot, literally means a wooden shoe or clog."`

Locator command: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.wordorigins.org/big-list-entries/sabotage' "borrowing from French, and that borrowing occurred in the opening years of the twentieth century. The root, sabot, literally means a wooden shoe or clog."; echo exit=$?`

Full locator output:
```text
LOCATED https://www.wordorigins.org/big-list-entries/sabotage
exit=0
```

### S655 — French *sabot* form and use

| S655 | SABOT Definition & Meaning, Dictionary.com / Random House Unabridged Dictionary, © 2023 — https://www.dictionary.com/browse/sabot | book | B | Dictionary.com sense 1: single-block wooden sabot form and the named traditional wearers/regions | American noun, sense 1: "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc." | Dictionary.com defines a sabot as a wooden shoe hollowed from one block and notes use by farmers and workers in the named countries. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, and Belgium. (S655)`

Gate: `- S655 | https://www.dictionary.com/browse/sabot | 2026-10-23 | "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc."`

Locator command: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.dictionary.com/browse/sabot' "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc."; echo exit=$?`

Full locator output:
```text
LOCATED https://www.dictionary.com/browse/sabot
exit=0
```

## Freshness and source quality

The final `functions.grep` call on `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` used pattern `museum\\.nl/en/internationaal-klompenmuseum|zaanseschans\\.com/en/wooden-shoe-workshop-de-zaanse-schans|wordorigins\\.org/big-list-entries/sabotage|dictionary\\.com/browse/sabot|\\bS65[2-5]\\b`; full result: `No matches found.` Earlier host/path greps for each candidate also returned `No matches found.`

Tier rationale: S652 is a Museum.nl listing (strong secondary for the museum profile); S653 is the Zaanse Schans site's own description of its collection (primary for that display); S654 is a specialist etymology write-up with historical-dictionary and period-publication references; S655 is a dictionary definition based on the Random House Unabridged Dictionary.

## Access attempts not kept

- **Etymonline, sabotage:** ordinary `read` of `https://www.etymonline.com/word/sabotage` failed with HTTP 403. The allowed Wayback availability request, `timeout 300 curl -s 'https://archive.org/wayback/available?url=https://www.etymonline.com/word/sabotage'`, returned closest snapshot `20260322153956`, status 200. Static `read` of `https://web.archive.org/web/20260322153956id_/https://www.etymonline.com/word/sabotage` showed the entry text, but the required locator did not locate it: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.etymonline.com/word/sabotage' "that the modern meaning derives from strikers' supposed tactic of throwing shoes into machinery is not supported by the etymology"; echo exit=$?` → `NOT_LOCATED https://www.etymonline.com/word/sabotage HTTPError`, `exit=1`; the same locator on the archive `id_` URL returned `NOT_LOCATED ... HTTPError`, `exit=1`. A direct urllib diagnostic to that archive URL returned `HTTPError HTTP Error 429: Too Many Requests`. Access challenge met, not passed; the capture was not used because it failed the locator.
- **OED, sabotage:** direct `read` of `https://www.oed.com/dictionary/sabotage_n` returned a generic OED landing page, not the entry. The Wayback availability request, `timeout 300 curl -s 'https://archive.org/wayback/available?url=https://www.oed.com/dictionary/sabotage_n'`, returned closest snapshot `20250503102218`, status 200. Static `read` of `https://web.archive.org/web/20250503102218id_/https://www.oed.com/dictionary/sabotage_n` showed the entry and etymology. The live locator for `"French, < saboter to make a noise with sabots, to perform or execute badly"` returned `NOT_LOCATED https://www.oed.com/dictionary/sabotage_n quote-absent`, `exit=1`; the `id_` capture and an HTTP archive variant both returned `NOT_LOCATED ... HTTPError`, `exit=1`. No OED row retained.
- **Merriam-Webster:** direct static reads of its `sabot` and `sabotage` pages yielded dictionary text, but locator attempts returned `NOT_LOCATED <URL> HTTPError`, `exit=1`; neither was retained.
- **Other discovery attempts:** Collins and Cambridge direct reads returned HTTP 403; CNRTL reads returned only its generic Portail lexical page; neither was used. The Rijksmuseum object record for *The Wooden Shoes* returned a Dutch description containing *klompen*, while its English title is only three words; no 8–25-word quote with a frozen English footwear word was available from that read. The Boerenbondsmuseum page was also Dutch-only for the candidate manufacturing quote (*klompenmakerijen*), so neither it nor the Rijksmuseum record was retained. No challenge was bypassed and no headless browser was used.

A first Wordorigins/Dictionary.com locator attempt emitted a traceback (`NameError: name 'base64' is not defined` at `reopen-quote.py:173`). After re-reading the current locator, the same commands above returned `LOCATED`; the runtime fault was reported to `xd://report_issue`.

## Gates, touched surfaces, and limits

- **Passed for these four drafts:** all four final quote locators returned `LOCATED` with exit 0; URL/ID freshness grep returned no matches.
- **Not run:** `accept-c.py`, `accept-o.py`, build, tests, lint, or any whole-claim gate. This research report does not assert `ACCEPT-C-61: PASS` and is not evidence that the entry or registry has landed.
- **Touched surfaces:** only this requested report was written. No product code, corpus entry, `corpus/SOURCES.md`, `corpus/README.md`, lint tool, or lesson was edited. No package was installed.
- **Out of scope:** integration and all other footwear subtopics.

## Artifact path

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/ScribeSrc08.md`
