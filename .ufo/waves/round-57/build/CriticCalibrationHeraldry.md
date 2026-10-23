# CriticCalibrationHeraldry — claim C calibration traps (round 57)

Seat: critic, leaf. Scope: the seven popular claims named in the assignment, plus the traps found while testing them. Ten sources were opened this session by ordinary means. There were 45 runs of `reports/round-57/reopen-quote.py` and all printed `LOCATED`. The 43 quotes offered below are all 8 to 25 words; one 31-word run was replaced by a trimmed span. Each URL was checked with `grep -cF '<host/path>' corpus/SOURCES.md`, and each check printed 0. No installs or updates were made. Scratch files are under `/fast/scratch/hyaku/kotodama-r57/CriticCalibrationHeraldry/`: `locate.log` and `locate2.log` hold the locator output.

## Findings (attacks on the approach)

**F1 — premise defect: the dispatch says Mamluk blazons are "not hereditary", and the opened sources do not settle that.**
- Where it appears: `.ufo/waves/round-57/gen-build-spec.py:26` and `build-spec.json:11` frame the scope as "office and rank emblems that are not hereditary (Mamluk blazons, …)". `.ufo/waves/round-57/build/ScribeEntrySkeleton.md:57` copies this as its §7 heading.
- What Mayer says: he lists the earlier authorities as split. He then advances his own hedged hypothesis: "I venture to submit the hypothesis that the blazon was hereditary in the case of sons of amirial rank" (NEW-CriticCalibrationHeraldry-3, p. 41).
- What Pier says: "as a rule renk were not hereditary". He says this in a caption that shows a descendant of Ezbek bearing a renk (NEW-CriticCalibrationHeraldry-4).
- Risk: if the entry echoes the dispatch wording, it states a contested reading as settled. That is a calibration regression.
- Axes: calibration (primary), coverage.
- Smallest fix: change `ScribeEntrySkeleton.md:57` from `## 7. Office and rank emblems that are not hereditary` to `## 7. Office and rank emblems (heredity varies by system)`. Code Mamluk heredity **C**.

**F2 — duplicate authority: the assignment's code key conflicts with the lane registry.**
- The assignment defines "B well-supported, T tradition".
- The registry defines **B** as "Bounded, usable within a named domain" and **T** as "Unresolved provenance or claim check — Mark `(to-verify)` inline" (`corpus/knowledge/verification/calibration-registry.md:35-39`).
- Every existing bank opens with "Codes as in `../verification/calibration-registry.md:35-39`" (for example `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md:171`).
- Risk: a "T — tradition" line would tell a reader that a claim is unverified, when the intended meaning is "true as a tradition". That changes what the code identifies.
- Smallest fix: use the registry codes, and express a tradition as a bounded B, following the existing precedent "**B, as Latin word history only**" (`monsters-hybrid-beings.md:175`).
- The table below gives both keys. **Use the registry column.**

**F3 — the strongest counterexample: the obvious rebuttal over-corrects.**
- The College of Arms answer "Coats of arms belong to individuals" holds within its own jurisdiction (England, Wales and Northern Ireland).
- Polish clan arms break it: "A number of unrelated families (sometimes hundreds of them), usually with a number of different family names, may use the same, undifferenced coat of arms" (NEW-CriticCalibrationHeraldry-10).
- Other opened systems also attach marks to groups:
  - Tamga attach to a tribe, clan or family (-7).
  - Late Mamluk blazons became "a collective badge of military groups" (-3).
  - Shops adopted kamon (-6, page text).
- Smallest fix: write "arms belong to individuals" as **B, under the English law of arms only**, never as a universal.
- Axes: calibration, coverage.

**F4 — false-provenance trap on tinctures.**
- The same College of Arms FAQ says "There are no fixed shades for heraldic colours". That answer is about which shade of a colour to paint, not about what a colour means.
- Smallest fix: do not cite it for the tincture-symbolism claim. Cite Fox-Davies (-2) and the Tincture page (-8) instead.

**F5 — row-mode anchor trap from inner double quotes.**
- Row mode takes the first double-quoted span of the anchor: `QUOTE = re.compile(r'"([^"]+)"|“([^“”]+)”')` at `reports/round-57/reopen-quote.py`, used in `row_target`.
- An anchor such as `"Unlike in European heraldry, however, this "blazon" is not prescriptive"` would be cut to `Unlike in European heraldry, however, this ` (6 words). The locator rejects quotes under 8 words, so the row fails LOCATE even though URL mode printed `LOCATED`.
- Smallest fix: put only quotes without inner `"` into anchors. Every source below has such an alternate, and each alternate was located.

**F6 — access route and licence flags.**
- College of Arms:
  - The live site served a reCAPTCHA "Bot Verification" page: challenge met, not passed.
  - The newest Wayback capture (20261016042143) also serves that bot page, so it is unusable.
  - The route that works is capture 20140801170715. Its content is from 2014, so the row should carry that date.
- Mayer, *Saracenic Heraldry* (1933):
  - Served from the Digital Library of India collection on archive.org, with no rights statement in its metadata.
  - The author died in 1959, so the book is not obviously public domain. This is close to the round-56 R56-M4 lesson about licence-uncertain scans (`corpus/lessons/round-56-verifier-spotcheck.md:150,166`).
  - QUALITY criterion 10 accepts "a library scan that a fresh session could repeat", so whether to use it is the L1's call.
  - Pier 1908 (-4), which is JSTOR Early Journal Content explicitly "Free to Anyone in the World", is a licence-clean fallback for the Mamluk claim.
- Tier: the tamga, kamon, tincture-tradition, crest and Polish rows are Wikipedia (tier C). None of them should be the only support for a load-bearing sentence (see F7).

**F7 — one-sided support.**
- "Tamgas were a source of the Old Turkic script" and "the tincture-meaning tradition ran 15th–17th c." rest only on tier-C pages.
- Pier's "heraldry had its inspiration in the East" (-4) is a further popular claim I found. I opened only that one 1908 assertion of it, with no counter-source.
- Code these **T** (to-verify, registry sense) until a tier A or B row backs them.

## Calibration bank (one line per claim)

| # | Popular claim | Assignment key | **Registry key** | What the opened source says instead |
|---|---|---|---|---|
| 1 | "Every surname has a coat of arms" | R | **R**. The corrective "arms belong to individuals" is **B, English law of arms only** (F3). | College of Arms: "There is no such thing as a 'coat of arms for a surname'" (-1, FAQ Q1). Fox-Davies shows the mechanism behind the myth: people named Cooper using the Ashley coat "without authority" (-2, ch. XII p. 207). Polish arms invert it: one coat is shared across many surnames (-10). |
| 2 | "Heraldic tinctures have fixed symbolic meanings" | R (T for the old tradition) | **R** as a rule of heraldry. **B, as 15th–17th-c. treatise tradition only**, flagged **T** (tier C only). | Fox-Davies: "That an argent field meant purity, that a field of gules meant royal or even martial ancestors … I utterly deny" (-2, ch. I p. 6). The Tincture page: tinctures were "sometimes associated with the planets, precious stones, virtues, and elements", but "in contemporary heraldry they are not assigned any particular meaning" (-8). |
| 3 | "Only nobles bore arms" | R | **R** as a universal. **B** where a system restricted arms: Mamluk amirs (-3); Polish szlachta (-10); and the English theory that a grant confers gentility (-2). | The Kings of Arms grant "to individuals and corporate bodies" (-1). A merchant could obtain a grant "as he was in the reign of Henry VIII. and earlier" (-2, ch. II p. 23). Merchants' brasses bear "his coat of arms and merchant's mark beside" (-2, ch. IV p. 51). The closed helmet in Germany sank "to the grade of a mere burgess's helmet" (-2, ch. XX p. 319). Commoners without kamon borrowed a patron's (-6). Residue: Mayer finds that amirs' sons in civil careers "apparently had no right to arms" (-3, p. 4). |
| 4 | "Kamon are Japanese coats of arms (same system)" | R for "same system"; B for the analogy | **R** for "same system". **B** for "a functional analogue that identifies families". | Kamon naming "is not prescriptive" (-6). Mon "are essentially monochrome" and may be drawn in any colour (-6). "Japanese heraldry does not have a cadency or quartering system" (-6). Chamberlain draws the analogy but names a different development path: no "tournaments and the crusades" (-5, s.v. Heraldry, p. 201). |
| 5 | "The tamga is a Turkic writing system" | R | **R** as a definition. The script-origin hypothesis is reported as widely rejected (tier C) → **T** until a tier A/B row backs it. | A tamga "is an abstract seal or brand … initially as a livestock branding". The idea that tamgas were a source of the Old Turkic script "is widely rejected as being unverifiable" (-7). |
| 6 | "Mamluk blazons are family arms" | C | **C** | Mayer: earlier authorities were split; emblems "with very few exceptions represented the office held by the amir"; his hedged hypothesis is that blazons were hereditary for sons of amirial rank; in the 15th c. they became "a collective badge of military groups" (-3, pp. 3-4, 40-41). Pier: two kinds of renk, arms proper and an office mark, and "as a rule renk were not hereditary" (-4). |
| 7 | "The crest is the whole achievement" | R | **R** | College of Arms: "It is a popular misconception that the word 'crest' describes a whole coat of arms"; the crest is "the three-dimensional object placed on top of the helm" (-1). Fox-Davies: "achievement" is the correct term for the whole (-2, ch. V p. 60). The Crest page: the term is "frequently but erroneously used" for the shield or the whole achievement (-9). |
| + | "European heraldry was inspired by the Saracens" (extra, found in -4) | — | **T** (one-sided, 1908) | Pier asserts it ("we are led to believe that heraldry had its inspiration in the East", -4). No counter-source was opened, so do not cite it as settled. |

## Sources

### NEW-CriticCalibrationHeraldry-1
citation: College of Arms, "FAQs: heraldry", college-of-arms.gov.uk/resources/faqs, page © 2014, captured by the Wayback Machine 2014-08-01.
url: https://web.archive.org/web/20140801170715id_/http://www.college-of-arms.gov.uk/resources/faqs
route: Wayback capture 20140801170715 (id_ raw). The live site served a reCAPTCHA "Bot Verification" page: challenge met, not passed. The 20261016042143 capture is the same bot page.
kind: docs
tier: A — the official heraldic authority of the English Crown, speaking on its own jurisdiction; the content dates from 2014.
scope: Surname arms, who may be granted arms, and what a crest is, under the law of arms of England, Wales and Northern Ireland. Not other jurisdictions; not tincture meaning (F4).
quotes:
- FAQ Q1: "There is no such thing as a 'coat of arms for a surname'."
  `LOCATED https://web.archive.org/web/20140801170715id_/http://www.college-of-arms.gov.uk/resources/faqs`
- FAQ Q1: "Many people of the same surname will often be entitled to completely different coats of arms"
  `LOCATED https://web.archive.org/web/20140801170715id_/http://www.college-of-arms.gov.uk/resources/faqs`
- FAQ Q2: "The Kings of Arms are deputed by the Crown to make grants of new arms to individuals and corporate bodies within their jurisdiction."
  `LOCATED https://web.archive.org/web/20140801170715id_/http://www.college-of-arms.gov.uk/resources/faqs`
- FAQ Q4: "It is a popular misconception that the word 'crest' describes a whole coat of arms or any heraldic device."
  `LOCATED https://web.archive.org/web/20140801170715id_/http://www.college-of-arms.gov.uk/resources/faqs`
- FAQ Q4: "A crest is a specific part of a full achievement of arms: the three-dimensional object placed on top of the helm."
  `LOCATED https://web.archive.org/web/20140801170715id_/http://www.college-of-arms.gov.uk/resources/faqs`
teaches: Under the English law of arms a coat belongs to a person by grant or male-line descent, never to a surname, and the crest is one part.
draft sentences:
- The College of Arms answers the surname question flatly: there is no such thing as a coat of arms for a surname, and many people sharing a surname are entitled to different arms or to none (NEW-CriticCalibrationHeraldry-1, FAQ Q1).
- In its jurisdiction the Kings of Arms, deputed by the Crown, grant new arms to individuals and to corporate bodies, so a world's guilds and towns can be armigerous without being noble (NEW-CriticCalibrationHeraldry-1, FAQ Q2).
- The College calls it a popular misconception that "crest" means a whole coat of arms; a crest is the three-dimensional object on top of the helm (NEW-CriticCalibrationHeraldry-1, FAQ Q4).
- A worldbuilder who copies this model needs an authority that grants and records arms, because the right to bear arms comes from a grant or from legitimate male-line descent from a grantee (NEW-CriticCalibrationHeraldry-1, FAQ Q1).

### NEW-CriticCalibrationHeraldry-2
citation: Arthur Charles Fox-Davies, *A Complete Guide to Heraldry* (London: T. C. & E. C. Jack, 1909), Project Gutenberg eBook #41617.
url: https://www.gutenberg.org/cache/epub/41617/pg41617.txt
route: direct, HTTP 200
kind: book
tier: B — a standard English manual by a practising heraldic writer; opinionated and dated (1909), and centred on English usage.
scope: The English view of tincture symbolism, the status of arms, merchants' and burgesses' arms, and the achievement/crest distinction. Not continental or non-European systems.
quotes:
- ch. I, p. 6: "That an argent field meant purity, that a field of gules meant royal or even martial ancestors"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. I, p. 6: "that a saltire meant the capture of a city, or a lion rampant noble and enviable qualities, I utterly deny."
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. II, p. 23: "the successful trader or merchant is now at liberty, as he was in the reign of Henry VIII. and earlier"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. II, p. 23: "some of the earliest distinctly recite that the recipients are made noble and created gentlemen"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. IV, p. 51: "many a merchant's brass bears his coat of arms and merchant's mark beside"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. V, p. 60: "a term most frequently employed to signify the whole, but which can correctly be used to signify anything"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. V, p. 60 (inner quotes — URL mode only, not for an anchor, F5): "the correct term for the whole emblazonment is an "achievement,""
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. VII, p. 89 (Fox-Davies quoting Ströhl): "Of very little heraldic worth are the old house and home signs as they were used by landed proprietors, tradesmen, and artisans"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. XII, pp. 207-208: "innumerable people of the name of Cooper are still using without authority the old Ashley coat pure and simple."
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
- ch. XX, p. 319: "The closed helmet consequently sank gradually in Germany to the grade of a mere burgess's helmet"
  `LOCATED https://www.gutenberg.org/cache/epub/41617/pg41617.txt`
teaches: Fox-Davies rejects fixed tincture meanings, records merchants and burgesses bearing arms, and calls the whole display an achievement.
draft sentences:
- Fox-Davies flatly denied the old handbook meanings, such as argent for purity or gules for royal or martial ancestors, while accepting punning symbolism such as arrows in the arms of Fletcher (NEW-CriticCalibrationHeraldry-2, ch. I p. 6).
- He records that a successful trader or merchant could obtain a grant of arms, as in Henry VIII's reign and earlier, and that early grants made the recipients noble and gentlemen (NEW-CriticCalibrationHeraldry-2, ch. II p. 23).
- Medieval merchants' brasses often show a coat of arms with a merchant's mark beside it, so a world can let both systems sit on one monument (NEW-CriticCalibrationHeraldry-2, ch. IV p. 51).
- The surname myth has a visible mechanism: people named Cooper widely used, without authority, a coat that actually belonged to Ashley (NEW-CriticCalibrationHeraldry-2, ch. XII pp. 207-208).
- The correct term for the whole display is "achievement"; Fox-Davies calls calling any stamped device "a crest" an uneducated habit (NEW-CriticCalibrationHeraldry-2, ch. V p. 60).

### NEW-CriticCalibrationHeraldry-3
citation: L. A. Mayer, *Saracenic Heraldry: A Survey* (Oxford: Clarendon Press, 1933), archive.org item in.ernet.dli.2015.178234 (Digital Library of India scan).
url: https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt
route: direct, HTTP 200. **Licence flag (F6):** DLI collection, no rights statement, author died 1959. The L1 decides; -4 is the clean fallback.
kind: book
tier: B — the standard monograph on Mamluk/Ayyubid blazons; 1933, so its hypotheses are dated and hedged.
scope: Mamluk and Ayyubid blazons — office meaning, grant or choice, the heredity debate, collective badges. Not other Islamic dynasties (Mayer excludes them).
quotes:
- Introduction, pp. 3-4: "the emblems, so far as we can understand them, with very few exceptions represented the office held by the amir"
  `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Introduction, p. 4: "until in the fifteenth century it became a collective badge of military groups."
  `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Introduction, p. 4: "Although the Saracenic blazon was hereditary among amirs, yet those of their sons who"
  `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Introduction, p. 4: "chose an ecclesiastic or administrative career, apparently had no right to arms."
  `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- The Problem of Heredity, p. 40: "Rogers was convinced that the blazon was not hereditary."
  `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- The Problem of Heredity, p. 41: "I venture to submit the hypothesis that the blazon was hereditary in the case of sons of amirial rank"
  `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
teaches: Mamluk blazons mostly marked the office an amir held, and whether they passed to sons remained contested, Mayer favouring heredity only within amirial rank.
draft sentences:
- Mayer found that Mamluk emblems, as far as they can be read, with very few exceptions represented the office the amir held when he was made amir (NEW-CriticCalibrationHeraldry-3, Introduction pp. 3-4).
- Earlier authorities split on heredity; Rogers was convinced the blazon was not hereditary, while Mayer ventured the hypothesis that it was hereditary for sons of amirial rank (NEW-CriticCalibrationHeraldry-3, pp. 40-41).
- Sons of amirs who chose religious or administrative careers apparently had no right to arms, so a world modelled on this system ties the right to arms to military rank (NEW-CriticCalibrationHeraldry-3, Introduction p. 4).
- By the fifteenth century the blazon had become a collective badge of military groups, which makes it a model for a mark that drifts from office to faction (NEW-CriticCalibrationHeraldry-3, Introduction p. 4).

### NEW-CriticCalibrationHeraldry-4
citation: Garrett C. Pier, "Saracenic Heraldry in Ceramic Decoration", *Bulletin of the Metropolitan Museum of Art* 3 (1908), JSTOR 10.2307/3252531 (Early Journal Content), archive.org item jstor-3252531.
url: https://archive.org/download/jstor-3252531/3252531_djvu.txt
route: direct, HTTP 200. The text carries JSTOR's "Early Journal Content … Free to Anyone in the World" statement.
kind: paper
tier: B for the curator's period statements on office versus arms; C for his origin claim (a one-sided 1908 assertion).
scope: Two kinds of renk (arms proper versus office mark), heredity "as a rule", renk on ceramics; the eastern-origin claim only as an attributed 1908 view (T).
quotes:
- p. 7: "There appear to have been two kinds of renk, the coat-of-arms proper, and another which served to define the office of its owner"
  `LOCATED https://archive.org/download/jstor-3252531/3252531_djvu.txt`
- figure list, fig. 19: "A descendant of Ezbek, though as a rule renk were not hereditary"
  `LOCATED https://archive.org/download/jstor-3252531/3252531_djvu.txt`
- p. 7: "we are led to believe that heraldry had its inspiration in the East"
  `LOCATED https://archive.org/download/jstor-3252531/3252531_djvu.txt`
teaches: Pier in 1908 split Mamluk renk into arms proper and office marks and called them as a rule not hereditary, while noting a descendant's case.
draft sentences:
- Pier, writing for the Metropolitan Museum in 1908, distinguished two kinds of renk: the coat of arms proper, and one that defined its owner's office, such as a polo master's polo sticks (NEW-CriticCalibrationHeraldry-4, p. 7).
- He captions one renk as belonging to a descendant of Ezbek while adding that as a rule renk were not hereditary, an exception a world can keep as a contested case (NEW-CriticCalibrationHeraldry-4, fig. 19).
- Pier believed heraldry had its inspiration in the East; treat this as his 1908 view, not an established origin (NEW-CriticCalibrationHeraldry-4, p. 7).

### NEW-CriticCalibrationHeraldry-5
citation: Basil Hall Chamberlain, *Things Japanese: Being Notes on Various Subjects Connected with Japan* (London: Kegan Paul, Trench, Trübner, 1891), s.v. "Heraldry", archive.org item thingsjapanesebe00cham_0.
url: https://archive.org/download/thingsjapanesebe00cham_0/thingsjapanesebe00cham_0_djvu.txt
route: direct, HTTP 200
kind: book
tier: C — a dated 1891 handbook entry that Chamberlain says is a précis of McClatchie; the OCR is noisy around the quotes.
scope: The 1891 comparison of Japanese and European heraldry, and where the mon was worn. Not current kamon practice.
quotes:
- s.v. Heraldry, p. 201: "the absence of such powerful stimuli as tournaments and the crusades prevented Japanese"
  `LOCATED https://archive.org/download/thingsjapanesebe00cham_0/thingsjapanesebe00cham_0_djvu.txt`
- s.v. Heraldry, p. 201: "In time of peace the crest was worn, as indeed it still is by those who retain the native garb"
  `LOCATED https://archive.org/download/thingsjapanesebe00cham_0/thingsjapanesebe00cham_0_djvu.txt`
- s.v. Heraldry, p. 201 (curly inner quotes; prefer the first quote for an anchor): "feudalism produced the “nobyl and gentyl sciaunce” of heraldry, though the absence of such powerful stimuli as tournaments and the crusades prevented Japanese"
  `LOCATED https://archive.org/download/thingsjapanesebe00cham_0/thingsjapanesebe00cham_0_djvu.txt`
teaches: Chamberlain in 1891 compared Japanese and European heraldry as feudal products but said Japan's lacked tournament and crusade stimuli and stayed simpler.
draft sentences:
- Chamberlain in 1891 called Japanese heraldry, like Europe's, a product of feudalism, but said the absence of tournaments and the crusades kept it from European complexity (NEW-CriticCalibrationHeraldry-5, s.v. Heraldry p. 201).
- In peacetime the mon was worn in five places on the upper garment — at the back of the neck, on each sleeve and on each breast (NEW-CriticCalibrationHeraldry-5, s.v. Heraldry p. 201).
- In his account great daimyō held three crests, lesser daimyō two and ordinary samurai one, so a world can let the number of marks track rank (NEW-CriticCalibrationHeraldry-5, s.v. Heraldry p. 201; OCR noisy, opened page).

### NEW-CriticCalibrationHeraldry-6
citation: Wikipedia contributors, "Mon (emblem)", English Wikipedia, revision served 2026-10-22.
url: https://en.wikipedia.org/wiki/Mon_(emblem)
route: direct, HTTP 200
kind: web
tier: C — an encyclopedia article; adequate for structural contrasts, not for dates.
scope: Structural differences between mon and European arms: non-prescriptive naming, monochrome, no cadency or quartering, use by commoners and shops, the reserved paulownia variant.
quotes:
- Design: "the depiction of a mon does not follow the name— instead, the names only serve to describe the mon."
  `LOCATED https://en.wikipedia.org/wiki/Mon_(emblem)`
- Design (inner quotes — URL mode only, F5): "Unlike in European heraldry, however, this "blazon" is not prescriptive"
  `LOCATED https://en.wikipedia.org/wiki/Mon_(emblem)`
- Design: "Mon are essentially monochrome; the color does not constitute part of the design, and they may be drawn in any color."
  `LOCATED https://en.wikipedia.org/wiki/Mon_(emblem)`
- Design: "Japanese heraldry does not have a cadency or quartering system"
  `LOCATED https://en.wikipedia.org/wiki/Mon_(emblem)`
- History: "Commoners without kamon often used those of their patron or the organization they belonged."
  `LOCATED https://en.wikipedia.org/wiki/Mon_(emblem)`
- Design: "the paulownia crest with 5-7-5 flowers is reserved for the prime minister, whereas paulownia with fewer flowers could be used by anyone"
  `LOCATED https://en.wikipedia.org/wiki/Mon_(emblem)`
teaches: Mon identify families like European arms but differ structurally: names describe rather than prescribe, colour is not part of the design, and there is no cadency.
draft sentences:
- A mon's name only describes the design and does not prescribe it, the reverse of European blazon (NEW-CriticCalibrationHeraldry-6, Design).
- Mon are essentially monochrome and may be drawn in any colour, so a kamon-like system has no tincture rules to break (NEW-CriticCalibrationHeraldry-6, Design).
- Japanese heraldry has no cadency or quartering system, though cadet branches often chose a slightly different mon (NEW-CriticCalibrationHeraldry-6, Design).
- Commoners without a mon of their own often used their patron's or their organization's, so a mark can signal affiliation rather than descent (NEW-CriticCalibrationHeraldry-6, History).
- One variant can be reserved for an office — the 5-7-5 paulownia for the prime minister — while plainer variants stay open to anyone (NEW-CriticCalibrationHeraldry-6, Design).

### NEW-CriticCalibrationHeraldry-7
citation: Wikipedia contributors, "Tamga", English Wikipedia, revision served 2026-10-22.
url: https://en.wikipedia.org/wiki/Tamga
route: direct, HTTP 200
kind: web
tier: C — an encyclopedia article (it carries a needs-references flag); the script-origin verdict rests on its footnote [14], which was not opened.
scope: What a tamga is (a seal or brand, used first on livestock) and the reported status of the script-origin hypothesis. Load-bearing only alongside a tier A/B row (F7).
quotes:
- lead: "is an abstract seal or brand that was used by Eurasian nomads and cultures influenced by them, initially as a livestock branding"
  `LOCATED https://en.wikipedia.org/wiki/Tamga`
- lead: "It has been speculated that Turkic tamgas represent one of the sources of the Old Turkic script of the 6th–10th centuries"
  `LOCATED https://en.wikipedia.org/wiki/Tamga`
- lead: "but since the mid-20th century, this hypothesis is widely rejected as being unverifiable."
  `LOCATED https://en.wikipedia.org/wiki/Tamga`
teaches: A tamga is a seal or brand mark of tribe, clan or family, not a script; its claimed role in Old Turkic writing is reported as widely rejected.
draft sentences:
- A tamga is an abstract seal or brand used by Eurasian nomads, first as a livestock brand for a tribe, clan or family (NEW-CriticCalibrationHeraldry-7, lead).
- The idea that tamgas were one source of the Old Turkic script is reported as widely rejected since the mid-twentieth century as unverifiable (to-verify) (NEW-CriticCalibrationHeraldry-7, lead).
- The page also records tamgas as dynastic and state symbols on coins and seals, so one mark can climb from herd to state (NEW-CriticCalibrationHeraldry-7, lead).

### NEW-CriticCalibrationHeraldry-8
citation: Wikipedia contributors, "Tincture (heraldry)", English Wikipedia, revision served 2026-10-22.
url: https://en.wikipedia.org/wiki/Tincture_(heraldry)
route: direct, HTTP 200. Row mode is safe: `trim` keeps a balanced `)` (`reopen-quote.py:194-198`).
kind: web
tier: C — an encyclopedia article; the period claim rests on its footnote [1], which was not opened.
scope: That modern heraldry assigns tinctures no meaning, and that a 15th–17th-century associative tradition existed (T until backed by A/B).
quotes:
- Overview: "However, in contemporary heraldry they are not assigned any particular meaning."
  `LOCATED https://en.wikipedia.org/wiki/Tincture_(heraldry)`
- Overview: "the tinctures were sometimes associated with the planets, precious stones, virtues, and elements"
  `LOCATED https://en.wikipedia.org/wiki/Tincture_(heraldry)`
teaches: Tinctures carried associations to planets, stones and virtues in some early-modern treatises, but contemporary heraldry assigns them no particular meaning.
draft sentences:
- Between the fifteenth and seventeenth centuries tinctures were sometimes associated with planets, precious stones, virtues and elements (to-verify) (NEW-CriticCalibrationHeraldry-8, Overview).
- In contemporary heraldry tinctures are not assigned any particular meaning, so an in-world herald who reads virtues into colours is voicing a period treatise, not a rule (NEW-CriticCalibrationHeraldry-8, Overview).
- A world can give its own heralds a colour-meaning doctrine, but should mark it as that institution's in-world assertion (NEW-CriticCalibrationHeraldry-8, Overview).

### NEW-CriticCalibrationHeraldry-9
citation: Wikipedia contributors, "Crest (heraldry)", English Wikipedia (Good Article), revision served 2026-10-22.
url: https://en.wikipedia.org/wiki/Crest_(heraldry)
route: direct, HTTP 200
kind: web
tier: C — an encyclopedia article; it corroborates -1 and -2.
scope: The parts of an achievement and the misuse of "crest".
quotes:
- lead: "A normal heraldic achievement consists of the shield, above which is set the helm, on which sits the crest"
  `LOCATED https://en.wikipedia.org/wiki/Crest_(heraldry)`
- lead: "frequently but erroneously used to refer to the arms displayed on the shield, or to the achievement as a whole."
  `LOCATED https://en.wikipedia.org/wiki/Crest_(heraldry)`
- lead (inner quotes — URL mode only, F5): "has led the term "crest" to be frequently but erroneously used to refer to the arms displayed on the shield"
  `LOCATED https://en.wikipedia.org/wiki/Crest_(heraldry)`
teaches: A crest sits on the helm above the shield; using crest for the shield or the whole achievement is a common error from paper heraldry.
draft sentences:
- A normal achievement sets the helm above the shield and the crest on the helm, encircled at its base by a torse (NEW-CriticCalibrationHeraldry-9, lead).
- Using the crest apart from the rest of the achievement led to "crest" being wrongly used for the shield or the whole achievement (NEW-CriticCalibrationHeraldry-9, lead).
- Lore that calls a family's whole arms its "crest" should be voiced by a character, not the narrator (NEW-CriticCalibrationHeraldry-9, lead).

### NEW-CriticCalibrationHeraldry-10
citation: Wikipedia contributors, "Polish heraldry", English Wikipedia, revision served 2026-10-22.
url: https://en.wikipedia.org/wiki/Polish_heraldry
route: direct, HTTP 200
kind: web
tier: C — an encyclopedia article; it is the counterexample source for F3 and should be paired with any A/B Polish row a scout files.
scope: Clan arms shared by unrelated families with different surnames; naming by coat-of-arms name.
quotes:
- Unique features: "A number of unrelated families (sometimes hundreds of them), usually with a number of different family names, may use the same, undifferenced coat of arms"
  `LOCATED https://en.wikipedia.org/wiki/Polish_heraldry`
- Unique features: "The most striking peculiarity of the system is that a coat of arms does not belong to a single family."
  `LOCATED https://en.wikipedia.org/wiki/Polish_heraldry`
teaches: In Polish heraldry one named, undifferenced coat could be borne by many unrelated families with different surnames, so arms are not individual property everywhere.
draft sentences:
- In the Polish system a coat of arms does not belong to a single family; unrelated families, sometimes hundreds, with different surnames may bear the same undifferenced arms (NEW-CriticCalibrationHeraldry-10, Unique features).
- Each such coat has its own name, and nobles were referred to by surname plus arms name, as in Jan Zamoyski herbu Jelita (NEW-CriticCalibrationHeraldry-10, Unique features).
- A world can therefore hang arms on a clan-like fellowship instead of a person, which breaks the English rule that arms belong to individuals (NEW-CriticCalibrationHeraldry-10, Unique features).

### Rejected
- https://www.college-of-arms.gov.uk/resources/faqs (live): served a reCAPTCHA "Bot Verification" page. Challenge met, not passed; routed to Wayback (-1).
- https://web.archive.org/web/20261016042143/https://www.college-of-arms.gov.uk/resources/faqs: the capture is the same bot page.
- https://www.college-of-arms.gov.uk/services/granting-arms (live): the same bot page; not pursued.
- https://www.courtofthelordlyon.scot/faqs/: HTTP 404, and the Wayback availability API returned no snapshot.
- https://www.metmuseum.org/essays/the-art-of-the-mamluk-period-1250-1517: HTTP 429; not retried.
- https://www.britannica.com/topic/heraldry: HTTP 403 (access control); not pursued.
- https://en.wikipedia.org/wiki/Mamluk_heraldry, https://en.wikipedia.org/wiki/Islamic_heraldry: HTTP 404 (no such article).

## Checks the L1 should run at integration
- Row mode on each filed row: `python3 -B reports/round-57/reopen-quote.py --row S###`. Use quote-free anchors only (F5).
- Before filing -3, decide on the licence question (F6). If -3 is dropped, -4 alone carries claim 6 at tier B.
