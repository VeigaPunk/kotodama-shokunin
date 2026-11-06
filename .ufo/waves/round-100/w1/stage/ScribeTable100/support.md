# ScribeTable100 — §7 table support repair (observation, not a claim)

Entry: `corpus/knowledge/linguistics/praise-poetry-panegyric.md` (round-99 praise entry).
Checker: `reports/round-100/controls/feasibility/table_support_ref.py` (L1 feasibility reference, frozen).
Scope: §7 table (header, separator, 9 data rows) and the binding paragraph immediately below it. Nothing else touched.
Base: `60010a55fb5f04ee728070c463b1a57ae1cc17fc`; freeze commit `255d84776c12c918b7bfb2a7173d7b495e3f966e`.

## 1. Measurement

Before (on the unmodified entry):

```
python3 -B reports/round-100/controls/feasibility/table_support_ref.py \
  --entry corpus/knowledge/linguistics/praise-poetry-panegyric.md \
  --root /home/vgpnk/Projects/shokunin/kotodama-shokunin \
  $(ls -d reports/round-*/evidence | sed 's/^/--evidence /')
```

rc = 1. Output: `TABLE-SUPPORT: 21 finding(s) in 1 scoped table(s)` — 21 `UNSUPPORTED-CELL`, no `UNBOUND-ROW`, no `NO-CAPTURE`, no `NO-PATH`. Saved as `before.txt` (22 lines).

After (same command, same bytes of the checker, same evidence dirs):

rc = 0. Output: `TABLE-SUPPORT: 0 finding(s) in 1 scoped table(s)`. Saved as `after.txt` (1 line).

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --stat -- corpus/knowledge/linguistics/praise-poetry-panegyric.md
```
rc = 0: `1 file changed, 9 insertions(+), 9 deletions(-)`.

```
python3 -B tools/check-corpus-index.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
```
rc = 0: `CORPUS-INDEX: OK files=271 rows=271 findings=0`.

Entry sha256 after repair: `9aaca1baee6ed6825b8ac97749389fb1b21f13c7c473f6a01f734240bfb4ee84` (45611 B).

## 2. Invariants held (counter leg O3 depends on these)

Verified against `git show HEAD:corpus/knowledge/linguistics/praise-poetry-panegyric.md` by a comparison script (rc 0):

- Table header `| tradition | singer and office | patron and reward | form and order | limit on the praise |` — byte-identical.
- Separator row `|---|---|---|---|---|` — byte-identical.
- All 9 row labels (first cell) — byte-identical: Southern Bantu court, Yoruba, Hausa, Mande and Soninke, Greek epinician, contemporary Xhosa, Norse skaldic court, Tamil puram, Welsh and Irish bardic.
- Yoruba row's last cell `an epithet can recall danger or contested reputation rather than flatter` — byte-identical (O3 replays the forged Yoruba cell against this table).
- Norse row — byte-identical in all five cells (it had no finding).
- Whole-file diff is 18 changed lines: the 9 table rows (9 removed, 9 added) plus the one binding line (1 removed, 1 added). No heading, no topic line, no §7 prose paragraph, no §8 text changed.

## 3. Binding repair (one line)

The Xhosa row's greeting/exhortation sequence is the S1008 conference performance (Opland, "Lord of the Singers"), not the S1011 rally paper. The line was extended, not replaced:

- before: `The contemporary Xhosa row reports the rally performance and the censorship finding (S1011).`
- after: `The contemporary Xhosa row reports the rally performance and the censorship finding (S1011) and the conference performance's greeting and exhortation (S1008).`

Decisive spans in `reports/round-99/evidence/S1008.txt` (whitespace-collapsed, `bytes.count == 1`):

| span | words | count |
|---|---|---|
| `He then greets the audience of academics before him (lines 6-9)` | 11 | 1 |
| `Manisi turns next to exhortation` | 5 | 1 |

The added line binds only the Xhosa row: its tokens contain no other row's label tokens (`southern`, `bantu`, `court`, `yoruba`, `hausa`, `mande`, `soninke`, `greek`, `epinician`, `norse`, `skaldic`, `tamil`, `puram`, `welsh`, `irish`, `bardic`), so no other row's support pool changed.

## 4. Cell repairs — 21 cells, one per finding

Each row below is one changed cell: before text, after text, the S-id that binds the row, and the decisive capture span with its whitespace-collapsed word count and occurrence count. All spans verified by `python3 -B spans.py` (rc 0, 22 spans checked, 0 bad); every span is an exact substring of the named capture after whitespace collapse, `count == 1`, and <= 25 words.

| # | row | column | before | after | bound | decisive span (capture) | words | count |
|---|---|---|---|---|---|---|---|---|
| 1 | Southern Bantu court | singer and office | *imbongi* / *mmoki* in the chief's retinue, graded by skill | *imbongi* / *mmoki*, respected members of the chief's official retinue | S1007 | `Tswana mmoki) were much respected members of the chief’s official retinue` | 11 | 1 |
| 2 | Southern Bantu court | patron and reward | chief and court; gifts and royal bounty, often public | the chief's victory and installation; the distribution of royal bounty | S1007 | `at the installation of a new chief, or at the distribution of royal bounty` | 14 | 1 |
| 3 | Southern Bantu court | form and order | praise names chained into stanzas, ancestors first, present chief last | a series of eulogies, starting with the chief's ancestors and reaching the present chief | S1007 | `starting with the famous praises of the king’s or chief’s ancestors` | 11 | 1 |
| 4 | Southern Bantu court | limit on the praise | criticism, sarcasm and withholding licensed as social pressure | criticism and sarcastic remarks, a kind of social pressure on an unpopular chief | S1007 | `criticism which can provide a kind of social pressure on an unpopular chief` | 13 | 1 |
| 5 | Yoruba | patron and reward | drummers rewarded by the praised and by passers-by | drummers go about the streets addressing passers-by, receiving a small reward | S1007 | `the drummers go about the streets formally addressing the passers-by and receiving a small reward` | 15 | 1 |
| 6 | Yoruba | form and order | *oriki* recited or drummed, royal list recited annually in public | the king's praises with the complete list of his predecessors, recited once a year in public | S1007 | `the praises of the king, with the complete list of his predecessors and their praises, must be recited once a year in public` | 23 | 1 |
| 7 | Hausa | patron and reward | District Head and graded chiefs; instrument rank marks status | the king has allocated them compounds, farm-lands and titles, and provides clothes and money | S1007 | `allocated compounds, farm-lands, and titles by the king` | 8 | 1 |
| 8 | Hausa | limit on the praise | derogatory *kirari* and advice inside the praise | derogatory remarks, or advice as well as praise | S1007 | `of people frequently include derogatory remarks, veiled or otherwise, or give advice as well as praise` | 16 | 1 |
| 9 | Mande and Soninke | patron and reward | wealthy individuals; gifts to avoid public shame | a reputedly wealthy individual; gifts and thanks, avoiding public shaming | S1007 | `reputedly wealthy individual for their praises` | 6 | 1 |
| 10 | Mande and Soninke | form and order | praise of a chosen notable, delivered on the street or at festivals | singers wander through the streets or attend festivals on their own initiative | S1007 | `to wander through the streets or attend festivals on their own initiative` | 12 | 1 |
| 11 | Mande and Soninke | limit on the praise | the singer may be called a beggar and still be paid | even those who refer to them as beggars reward them with gifts | S1007 | `even those who refer to them contemptuously as ‘beggars’ are in fact glad to reward them with gifts` | 18 | 1 |
| 12 | Greek epinician | singer and office | commissioned poet working for states and princes | song-writer to all Hellenic states | S1012 | `For his very calling of song-writer to all Hellenic states without discrimination` | 12 | 1 |
| 13 | Greek epinician | patron and reward | victorious patron and city; patronage and public honour | the Sicilian princes Hieron and Theron, for whom he wrote odes | S1012 | `For the magnificent Sicilian princes, Hieron of Syracuse and Theron of Akragas` | 12 | 1 |
| 14 | Greek epinician | form and order | victory, myth and moral counsel, praise of house and city | triumphal odes for victories in the great games | S1012 | `triumphal odes for victories in those great games` | 8 | 1 |
| 15 | Greek epinician | limit on the praise | the poet keeps independence and may refuse a court | he would not quit his home to ornament their courts; he had chosen to live his own life | S1012 | `he answered that he had chosen to live his own life, and not to be the property of another` | 19 | 1 |
| 16 | contemporary Xhosa | patron and reward | political and civic patrons; public standing | political organizations and trade unions; the imbongi as political orator | S1011 | `poetry in the form of izibongo is alive and well within trade unions and political organizations` | 16 | 1 |
| 17 | contemporary Xhosa | form and order | greeting, praise, exhortation, closing praise | the imbongi turns to exhortation, then praise in conclusion | S1008 | `Manisi turns next to exhortation` | 5 | 1 |
| 18 | Tamil puram | patron and reward | king, chieftain or headman; gifts before the bard moves on | kings, chieftains and headmen of small cities patronized bards, who stay till patrons honour them with gifts | S1014 | `The kings, chieftains and other headmen of small cities have patronized bards` | 12 | 1 |
| 19 | Tamil puram | limit on the praise | the same voice also carries counsel and embassy | the same bards were friends, counsellors and ambassadors too | S1014 | `They were good friends, counsellors and ambassadors too.` | 8 | 1 |
| 20 | Welsh and Irish bardic | singer and office | bard or *fili* attached to a lord | a herald bard; by the rules of his order he might not bear arms | S1013 | `By the rules of his order a Bard was not permitted ordinarily to bear arms` | 15 | 1 |
| 21 | Welsh and Irish bardic | form and order | praise in song and commemorative naming of warriors | stanzas of commemoration, one for each chieftain | S1013 | `It is divided into stanzas` | 5 | 1 |

Unchanged cells (no finding): Yoruba singer/office and limit; Hausa singer/office and form; Mande singer/office; all five Norse cells; Xhosa singer/office and limit; Tamil singer/office and form; Welsh patron/reward and limit.

## 5. Why each rewrite, in one line

1. The capture's own description of the office is "much respected members of the chief's official retinue"; "graded by skill" is not near it.
2. The Southern Bantu section names the occasions and the bounty: victory, installation, distribution of royal bounty.
3. The order stated in the capture is a series of eulogies beginning with the ancestors and ending with the present chief; "stanzas" is not its word.
4. The capture's limit for the Southern Bantu (Swazi/Ngoni) is criticism and sarcastic remarks as social pressure.
5. The Yoruba reward in the capture is the small reward from passers-by in the street, not from "the praised".
6. The royal list is recited "once a year in public"; the capture does not say "annually", and the *oriki*/*drummed* sentence is a different window.
7. The Hausa reward recorded is the king's allocation of compounds, farm-lands, titles, clothes and money to the maroka.
8. The Hausa emirs' praises include derogatory remarks "or give advice as well as praise"; the *kirari* passage is a separate window.
9. The Mande singer picks a "reputedly wealthy individual"; gifts and thanks follow, to avoid public shaming.
10. The Mande singers "wander through the streets or attend festivals on their own initiative".
11. Even those who call them beggars reward them with gifts — the capture's own formulation.
12. Pindar's office in the capture is "song-writer to all Hellenic states without discrimination"; "commissioned" is the entry's §3 gloss, not the capture's word.
13. The named patrons are the Sicilian princes Hieron and Theron, for whom he wrote odes.
14. The genre in the capture is the triumphal ode for victories in the great games.
15. The limit is the refusal of a court: he would not quit his home to be an ornament of their courts, and had chosen his own life.
16. The contemporary patrons in the capture are trade unions and political organizations; the imbongi acts as political orator. Neither S1011 nor S1008 records a payment, so the cell no longer claims one ("public standing" was an unsupported inference).
17. The S1008 conference performance turns "next to exhortation" and ends in praise; the greeting half is recorded in the binding line.
18. The Tamil patrons are kings, chieftains and headmen of small cities who patronized bards and honoured them with gifts.
19. The bards were "good friends, counsellors and ambassadors too" — the capture's nouns, not "counsel and embassy".
20. The Welsh bard in S1013 is a herald bard bound by the rules of his order; "fili" is not in S1013 (it remains in §8, line 210, bound to S1017).
21. The Gododin "is divided into stanzas" supposed to correspond in number with the chieftains, and its object is their commemoration.

## 6. Residuals and known limits

- **No type-(c) residual.** No cell was kept on the strength of a passage the 80-token window misses: all 21 findings were cleared by rewriting the cell or the binding. `after.txt` is `0 finding(s)`.
- **Content dropped, not hidden.** These elements of the old cells have no co-located support in the bound capture and were removed rather than keyword-padded: "graded by skill" (SB), "chained into stanzas" (SB), "withholding" (SB), "rewarded by the praised" (Yoruba), "*oriki* recited or drummed" (Yoruba, different window from the royal list), "District Head and graded chiefs; instrument rank marks status" (Hausa — the grade/instrument material is a different window; the row's unchanged form cell still carries "accompaniment fixed by the ruler's grade"), "*kirari*" (Hausa), "chosen notable" (Mande), "commissioned" (Greek), "patronage and public honour" (Greek), "myth and moral counsel" (Greek), "keeps independence and may refuse a court" (Greek — replaced by the capture's own refusal sentence), "civic … public standing" (Xhosa), "gifts before the bard moves on" (Tamil), "counsel and embassy" (Tamil), "*fili* attached to a lord" (Welsh/Irish — S1013 has no *fili*), "praise in song and commemorative naming of warriors" (Welsh/Irish).
- **Partial-sequence loss (Xhosa form and order).** The four-part sequence "greeting, praise, exhortation, closing praise" cannot be stated as one cell: in S1008 the greeting is more than 80 tokens from the exhortation and conclusion (greeting at the "in greeting similar audiences" sentence; exhortation and conclusion in the later paragraph). The cell keeps the exhortation→conclusion half; the binding line records both greeting and exhortation, and both spans are cited above. This is the one place where the repaired cell says less than the original intended.
- **Semantic correction, not a checker workaround.** The Xhosa reward cell no longer asserts a reward because neither bound capture records one; the old "public standing" was an inference the capture does not carry.
- **Checker limit (inherited from claims.json `residual_honesty`).** The checker measures lexical co-location, not meaning: a cell assembled from capture words in a false order can pass. Each rewritten cell was checked against the sense of its passage, not only against its vocabulary; where the capture's sense and the old cell's sense differed (Hausa reward, Xhosa reward, Greek limit), the cell follows the capture.
- **Not measured here.** This seat did not run battery100, the mutation driver, the O3 replay, or any other claim leg; those belong to the L1 and the O seats. This report is an observation on the entry only.

## 7. Commands and return codes

| command | rc |
|---|---|
| `python3 -B reports/round-100/controls/feasibility/table_support_ref.py --entry corpus/knowledge/linguistics/praise-poetry-panegyric.md --root /home/vgpnk/Projects/shokunin/kotodama-shokunin $(ls -d reports/round-*/evidence \| sed 's/^/--evidence /')` (before) | 1 (21 findings) |
| same command (after) | 0 (0 findings) |
| `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --stat -- corpus/knowledge/linguistics/praise-poetry-panegyric.md` | 0 (9 insertions, 9 deletions) |
| `python3 -B tools/check-corpus-index.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` | 0 (files=271 rows=271 findings=0) |
| `python3 -B spans.py` (22 spans, whitespace-collapsed count) | 0 (0 bad) |
| `sha256sum corpus/knowledge/linguistics/praise-poetry-panegyric.md` | 0 (`9aaca1ba…bfb4ee84`) |

Tooling installed or upgraded: none. No pacman, no network fetch, no new sources; only the round-99 captures and existing corpus lines were read.
