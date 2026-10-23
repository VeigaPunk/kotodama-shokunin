# B2ReviewRowS732 — row falsification review, S732

Seat: KotodamaR64.B2ReviewRowS732. Item: falsify wave-1 draft row S732 in
`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS732/row.txt` against claim C
rules (`reports/round-64/accept-c.py`, legs ROWS and RESTATE).

## HTTP results (verbatim)

- Live: `LIVE 200 https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/` — 167038 bytes, plain `curl -sL`
- Capture: `CAPTURE 200 https://web.archive.org/web/20261003105239id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/` — 167038 bytes
- Lane locator re-run first line: `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/` (exit 0)

## Checks

- Quote verbatim: the draft quote (curly apostrophe "family’s") appears exactly once in the
  fetched body, inside a `<p>` paragraph (nearest enclosing tag check: last `<p` at byte 64501
  after last heading tag at 64416). Counter-normalised (NFKC, casefold, non-word→space) it is
  19 words and contiguous; hit context: "…relevant for acquiring heritage languages because
  bilingual children in immigrant households sometimes avoid using the family s heritage
  language in favor of the majority language 37 38 a common pattern in spanish english
  bilingual homes…". Not a heading/caption/alt/nav string.
- Citation: `citation_author=Erika Hoff`, `citation_title=Bilingual Development in Children
  of Immigrant Families`, `citation_journal_title=Child development perspectives`, `12(2):80–86`
  (en dash matches draft). Page shows epub `2017 Oct 30` plus issue line `2018 Jun`; the 12(2)
  issue is the 2018 citation year, so draft's "Hoff, 2018" is correct.
- Heading locator "Effects of Children’s Output on Bilingual Development" present verbatim.
- Tier B: defensible — the page is a synthesis/review article and the quoted sentence cites
  refs 37–38, i.e. the scoped fact is reported secondarily; B (strong secondary) is the right
  tier for this scope.
- BULLET "Children sometimes avoid heritage language and favor majority-language speech,
  shifting family conversation. (S732)": RESTATE-clean (≥5 content words; in-order quote words
  children→avoid→heritage→language→favor→majority; novel words speech/shifting/conversation;
  copied run ≤12). "shifting family conversation" goes beyond the 19 quoted words but is
  established by the quoting paragraph's next sentence (parents speak Spanish, children answer
  English); no invented number, no scope overreach.
- Row shape: 11 cells, tier B, status mined, opened 2026-10-23, recheck 180d, used-by names
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`; capture original
  equals live URL.

Full table: /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS732/review.md

VERDICT: CLEAN — all fields independently verified; no required fix.
