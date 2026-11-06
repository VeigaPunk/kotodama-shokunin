# ExecRegistry99 — appended registry rows (S1007–S1017)

- lane: kotodama, round 99, wave w1
- registry: corpus/SOURCES.md, appended at the end of the ## Registry table after S1006
- used-by (all rows): corpus/knowledge/linguistics/praise-poetry-panegyric.md
- opened (all rows): 2026-11-06; recheck: 180d; status: mined
- evidence: reports/round-99/evidence/<id>.<ext>; manifest reports/round-99/evidence/manifest.json

| id | key | url | tier | quote | capture | sha256 (quote capture) | bytes | quote count |
|---|---|---|---|---|---|---|---|---|
| S1007 | C1 | https://archive.org/download/80204dff-c8a9-4155-a539-7ee980102875/80204dff-c8a9-4155-a539-7ee980102875_djvu.txt | B | In return the ruler acknowledges their praise by gifts or money which are often given publicly. | S1007.txt | 73df25c214bd03c2a36784c9d7faef3adaeb265b8ef1a7566713493a09f892b8 | 1431723 | 1 |
| S1008 | C2 | https://journal.oraltradition.org/wp-content/uploads/files/articles/3iii/6_opland.pdf | A | it is his duty to greet Lord with a royal praise name | S1008.txt | 112fdd45b5e24828fc9df0410e265c8801a909bfef0ae661f9654a1bdd64d3e9 | 122076 | 1 |
| S1009 | C3 | https://journal.oraltradition.org/wp-content/uploads/files/articles/20ii/Barber.pdf | A | Obscurity in praise poetry could be deployed for political reasons. | S1009.txt | 3f704d182cd42e6777adae87104a03c343318762ec3227ad089a8580d43a1215 | 895589 | 1 |
| S1010 | C4 | https://journal.oraltradition.org/wp-content/uploads/files/articles/16i/Groenewald.pdf | A | The praise poem for kings and chiefs has also been adapted to serve the trade union movement | S1010.txt | 9012091306dcb31614f0d47a95870f984af3324690b6f2827bc2fe588f7e73d0 | 941966 | 1 |
| S1011 | C5 | https://www.journal.oraltradition.org/wp-content/uploads/files/articles/10i/8_kaschula.pdf | A | directed at the Chief, decrying what was unworthy, praising what was worthy | S1011.txt | 499cd45fbdc4f5e42a4310afd43e93d97e8069be7e0e64c8e18d3e84cd2462f8 | 678241 | 1 |
| S1012 | C7 | https://www.gutenberg.org/cache/epub/10717/pg10717.txt | A | Yet praise is overtaken of distaste, wherewith is no justice, but from covetous men it cometh | S1012.txt | d8823d133ebb59059827379baca2af38ba5e36209d3d7fd553c0f5976dde5074 | 320993 | 1 |
| S1013 | C9 | https://www.gutenberg.org/files/9842/9842-h/9842-h.htm | A | A more choice act of mine will be To celebrate thy praise in song | S1013.txt | 594b3caeb20232af055530e36f153da090317bb7bb955469497e7b6c5a449753 | 412673 | 1 |
| S1014 | C10 | https://archive.org/stream/book-3-purananuru/BOOK3-Purananuru_djvu.txt | B | The main themes found in Purananuuru are praise of the ruler, patronage, heroism in battles | S1014.txt | 2042577c69e571c1ac0be78a9872612a50d365f3ad8b5e05e0709b80f87a0591 | 191267 | 1 |
| S1015 | C11 | https://journals.uni-goettingen.de/wom/article/download/2303/1986/5234 | B | the praise-singing function is by far the most obvious and audible manifestation | S1015.txt | 6b50724cf0bc32dcb7fa41376b446fb23224ac118a0da6ac29321188617a5be2 | 121791 | 1 |
| S1016 | C12 | https://www.asnc.cam.ac.uk/resources/mpvp/wp-content/uploads/2013/02/Introduction-to-Skaldic-Poetry_Debbie-Potts.pdf | B | There certainly was money in poetry for the skald; court poets would receive generous rewards | S1016.txt | e72c8e13d55cd152439aba2fca541885f9e4b9b23a64452e5e538264ac5e4bb3 | 294812 | 1 |
| S1017 | C13 | https://mural.maynoothuniversity.ie/id/eprint/19500/1/Kavanagh%20Emer%20Signs%20and%20Wonders.pdf | B | a poet should not satirize or over-praise a subject, as the fili depended on the wealth of his patron | S1017.txt | 4a54f3a8cb9600f98810af0217e83b0a1d5090773f48b73673192b097aa9d63c | 1897884 | 1 |

## Re-verification

Each admitted candidate was re-fetched by plain `curl -L --max-time 30 -sS` (default user agent)
from this seat, and each scout capture was re-hashed. Fresh sha256 equals the shipped capture for
every direct-file URL (C1, C2, C3, C4, C5, C7, C9 html, C11 pdf, C12 pdf, C13 pdf); C10's stream
page changed bytes between the scout fetch (191267) and this seat's fetch (184993) while the quote
still counts 1 in the fresh bytes, so the scout capture is shipped and the change is recorded here.

Quote counts are `re.sub(r"\s+"," ")` collapses of the named .txt capture; every count is 1.
