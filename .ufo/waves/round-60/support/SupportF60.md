# SupportF60 — blind source review (Round 60 A3 wave 2)

VERDICT P01 SUPPORTED — "Shinsatsu may be made of wood, paper, or metal and bear a written or printed inscription." — The quote appears verbatim (whitespace aside) as the body sentence of the article "Shinsatsu, Mamorifuda": "...thaumaturgic talisman (also known as gofu ) distributed at shrines and symbolic of a spiritual being or its supranormal power." The teaches is carried by that same sentence; entry claim 1 and entry claim 3 restate it; entry claim 2 (placement: enshrined in kamidana, affixed above gates, on doors and pillars, or on ceilings) is carried by the immediately following sentence.

VERDICT P02 NOT-SUPPORTED — The quote is verbatim and the teaches is carried, but condition (3) fails: the entry bullet appends "the form was carried from Ming-dynasty Nanjing by returning envoys", and no such claim exists anywhere in the PDF (strings "ming-dynasty", "nanjing", "envoys" are all absent from the extracted text).

VERDICT P03 SUPPORTED — "The specific arrangement of texts and elements on the amulet or talisman is achieved by carving, modeling, or assembling the materials into symbolic shapes" — The quote is verbatim in the article body: "Amulets or talismans gain their power firstly through their customized shape and form and secondly through their application by simply being worn or placed, while others can only be activated by reading the text written on them." The teaches is carried by that sentence, and both entry claims ("customized shape and form ... being worn or placed" as the two power sources, and the "others can only be activated by reading the text written on them" clause) appear in the same sentence.

VERDICT P04 NOT-SUPPORTED — Condition (1) fails: the page body reads "inscribed with prayers and invocations for safe delivery, birthing girdles were one of the most common spiritual charms loaned out by monasteries to their parishioners", whereas the packet quote says "inscribed with firstly and invocations..."; "firstly" occurs nowhere on the page, so the quote is not verbatim body text. The teaches and the entry claims (which use "prayers") are otherwise carried by that sentence.

VERDICT P05 NOT-SUPPORTED — unreachable: neither listed URL opened the article. The live page https://www.metmuseum.org/art/collection/search/464456 returns HTTP 429 (a Vercel Security Checkpoint challenge page) to the required curl command on three attempts and to the read tool; the listed web.archive.org capture is unreachable (connection refused to web.archive.org on every attempt, via curl and read). No listed URL yielded the article body.

VERDICT P06 SUPPORTED — "In Hellenistic times, we hear how a 'wonderworker' named Laiios successfully protected the city of Antioch by commanding the city to carve a giant face of Charon into the side of the mountain that overlooks the city." — The quote is verbatim in the book-sample PDF text: "A frontal face was also used as a protective amulet to ward off the plague." The teaches is carried by that sentence and by "Eyes also appear as a common apotropaic device on ships."; both entry claims (frontal face plague amulet; eyes as common apotropaic device on ships) appear on the page.

VERDICT P07 SUPPORTED — "These elements consist of its being an earthenware bowl that was inscribed with an incantation, adorned with an image, and buried upside-down." — The quote is verbatim in the "The image" section: "The amuletic object is a combination of elements, all of which are significant factors in making it potent." The teaches and the entry claim (vessel, written incantation, image of a shackled/bound demon, burial upside down) are carried by these two sentences together.

VERDICT P08 SUPPORTED — "These creases indicate that the person or people who used the amulet folded it up so that it was small enough to carry around or hold onto." — The quote is verbatim in the article body: "This elaborately detailed amulet from Kerala, Kochi was used to guard against both infertility and infant death." The teaches is carried by that sentence; entry claim 1 restates it, and entry claim 2 (creases indicate users folded it small enough to carry/hold) is carried by the later sentence quoted as the page passage.

## URLs opened (HTTP status, bytes)

- P01 live https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 — 200, 17563 B
- P01 wayback https://web.archive.org/web/20260415164210id_/https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 — connection failed (web.archive.org unreachable), 0 B
- P02 https://openaccess.iku.edu.tr/bitstreams/8b0b8456-e29b-4568-b622-5859e4029189/download — 200, 12295670 B (PDF, pdftotext)
- P03 https://pmc.ncbi.nlm.nih.gov/articles/PMC12701302/ — 200, 273314 B
- P04 https://www.cam.ac.uk/research/news/medieval-birthing-girdle-parchment-was-worn-during-labour-study-suggests — 200, 142514 B
- P05 live https://www.metmuseum.org/art/collection/search/464456 — 429 (Vercel Security Checkpoint), 34243 B / 34222 B (curl, twice); read tool also 429
- P05 wayback https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456 — connection failed (web.archive.org unreachable), 0 B
- P06 https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf — 200, 1227583 B (PDF, pdftotext)
- P07 live https://jnjr.div.ed.ac.uk/primary-sources/biblical/jewish-aramaic-incantation-bowls/ — curl 403 (548 B error body); read tool succeeded (native fetch, full article text)
- P07 wayback https://web.archive.org/web/20260115161151id_/https://jnjr.div.ed.ac.uk/primary-sources/biblical/jewish-aramaic-incantation-bowls/ — connection failed (web.archive.org unreachable), 0 B
- P08 https://jwa.org/blog/fromthearchive/archive-amulet-protection-pregnant-women-and-newborn-children — 200, 78059 B

Tool installs: none performed (curl, python3, pdftotext already present; no installs needed).
