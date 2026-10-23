# Row S682 — one-row one-clause review

- URL: https://aasjournal.spbu.ru/article/download/20521/12582/76573
- Fetch (live, ordinary GET via curl): HTTP 200, `application/pdf`, 1,001,970 bytes, 9-page PDF (v1.7). No redirect chain needed beyond the URL itself; live page reachable, so no archive capture was required. (Wayback `available` API returned 429 — irrelevant since the live URL serves the document.)
- Text extraction: `uv run --no-project --quiet --with pypdf==5.4.0 python3 -B` (pypdf 5.4.0, disclosed per source rules). 22,913 chars extracted.

## (1) QUOTE

Verdict: **LOCATED**.

The quoted passage is verbatim body text — the second sentence of the article's "Introduction" section (main body, not navigation, header, or a caption fragment). Raw extracted text (PDF line-wrap splits the sentence across two lines; whitespace-normalized match is exact):

> "The traditions of Arab countries related to footwear are of interest to ethnographers. For instance, a deliberate demonstration of the soles of shoes is considered indecent in Arab society; while hitting someone with a shoe is regarded as a humiliating insult."

The abstract independently restates the same claim ("the deliberate display of shoe soles is considered indecent in Arab society"), confirming this is the article's own text, not a stray fragment.

## (2) CLAUSE

Clause under test: "Deliberately displaying shoe soles is considered indecent in Arab society."

Verdict: **SUPPORTED**.

Every part of the clause is carried by the page with nothing added and nothing hedged away: "a deliberate demonstration of the soles of shoes" = deliberately displaying shoe soles; "is considered indecent" = is considered indecent (the clause preserves the attributive "considered", not asserting it as universal fact); "in Arab society" = in Arab society. No date, place, cause, comparison, or universal quantifier is introduced by the clause; no hedge ("probably", "researchers believe") attached to this specific sentence was dropped — the hedging in the next sentence concerns the *causes* of the traditions, not the indecency judgment itself.

Supporting page text (≥10 consecutive words, Introduction):

> "For instance, a deliberate demonstration of the soles of shoes is considered indecent in Arab society;"

Corroborating page text (abstract):

> "the deliberate display of shoe soles is considered indecent in Arab society, and hitting with shoes is regarded as a humiliating insult"

QUOTE S682 LOCATED
CLAUSE S682 SUPPORTED
