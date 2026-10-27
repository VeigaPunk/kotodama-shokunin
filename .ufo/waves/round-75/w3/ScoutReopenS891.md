# S891 independent reopen

## Fetch

- Requested archived URL: `https://web.archive.org/web/20041220223357id_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html`
- Method: ordinary `curl -sS -L --compressed`, browser-shaped UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.
- Response: HTTP 200; final URL is the requested capture; transferred/body bytes 1896; SHA-256 `69b5987240ccd7287e4e297f7333be9ed2ceb47a91cf697d196d5cd6b1f2b494`.
- Evidence file `reports/round-75/evidence/S891.txt` records the same HTTP status, 3898 bytes, and exact same full-body SHA-256. Therefore the archived page body hash is equal; bytes differ (1896 transferred vs 3898 recorded). This is consistent with compressed transfer size versus decompressed downloaded body, and does not indicate body drift. Evidence also records 2169 extracted visible chars, whole-document window and 2226 UTF-8 window bytes / window hash `6dfb7ed9c2f1d1a1c2ff3f11b58a534b31316c44917209e0bc4df6240385add4`.
- Independent rendered archive page contains the quote once in the paragraph beginning «Par hasard», after the lexie discussion; evidence window is whole document, and includes it (the stored evidence file's `quote-found-verbatim: yes`, `--- quote ---` confirms). NFKC + whitespace-folded quote: **found**, exact wording «les premières lexies suscitent l'établissement des cinq grands codes».

## Registry and Gate

Observed `corpus/SOURCES.md` S891 row (line 846): tier **B**, scope “the five codes of S/Z and their definitions … and the statement that they are five simultaneous voices the text's signifieds join, not rules for reading”; reason: opened artefact is a university course-server excerpt, not edition of record. URL/anchor and evidence capture correspond to the Gate. Tier **agrees** with the row's explicit rationale; it is secondary to the 1970 book. Scope is broadly supported, but its wording “five simultaneous voices the text's signifieds join” is not literally what the source says: the page says the codes are the *topical network through which the whole text passes* and “the place of disappearance of the voices” woven into the text. The Gate's listed accessed capture and quote agree.

Gate `## Gate` states the S891 anchor quote (68 chars, 9 tokens), archived capture and paragraph on five codes, and reports no probe receipt. Current fetch confirms the quoted text and same body digest. Caveat: evidence's `bytes: 3898` is decoded body size while curl reported 1896 transferred bytes; same digest establishes no page movement.

## Entry claims citing S891

Grep found S891 citations only in `corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md`; no S891 citations in the base entry or `.amend-2026-10-23.md`. The entry cites S891 only at `source:` line 4, and prose at lines 31–39, 45–47, 116. Page comparison:

- Line 31: identity and bibliographic claims (“Fiche de lecture”, DKW, May 2000, S/Z, Paris: Seuil 1970) are supported by the page header/byline. The quote claims about applied reading, typology, and lisible/scriptible are carried by its opening paragraphs.
- Lines 33, 35, 37, 39: lexies, 3–4 senses, “réseau à mille entrées”, five-code quote and names/glosses, topical network, voice disappearance, and structuration are all explicitly present in the fiche. The distinction from 1966 is also supported by this fiche's subject being S/Z; the broader 1966 contrast is additionally attributed to other source material in the entry.
- Line 37 final sentence: “A design order follows: the codes describe how signification is distributed in a text already written; they are not five stages to build in order, and they are not rules a reader applies.” **Not carried as written.** The page says lexies are selected in practice and their meanings enumerated; “par hasard” the first lexies prompt establishment of five codes that all signifieds join. It does not state a design order, explicitly reject stages, or say codes are not rules a reader applies. The entry presents that sentence as a deduction (“A design order follows”), not a direct quotation; nevertheless it exceeds the page as an evidentiary claim.
- Line 45: the fiche uses *sémique* and *gnomique* and gives “code culturel” as the latter's gloss; carried.
- Line 47's comparative claim that the scholar uses different spellings cites S892, not S891. The S891 portion (that this fiche is not quoting the scholar) is consistent with the fiche but not directly demonstrable solely from its text.
- Line 116: challenge status is a fetch observation, not a proposition carried by page content; the page itself does not speak to challenge handling. The archive document identity is corroborated by the page.

Exact unsupported S891-backed sentence: “A design order follows: the codes describe how signification is distributed in a text already written; they are not five stages to build in order, and they are not rules a reader applies.”

Verdict: **PARTIAL** — fresh capture hash and quote hold; one overclaim sentence in the cited amendment is not carried by the source. No other S891-cited substantive sentence identified as unsupported.