# ScribeTable100 — round-100 w1 report

**Item:** repair the support of the round-99 praise entry's §7 table, flagged by the frozen feasibility reference with 21 findings (observation work, not a claim).
**Entry:** `corpus/knowledge/linguistics/praise-poetry-panegyric.md`
**Checker:** `reports/round-100/controls/feasibility/table_support_ref.py` (frozen L1 control; not edited)
**Scope actually written:** §7's nine table rows and the one binding line below them. Nothing else.
**Entry sha256 after:** `9aaca1baee6ed6825b8ac97749389fb1b21f13c7c473f6a01f734240bfb4ee84` (45611 B).

## 1. Behaviour

Before: the frozen reference reported 21 `UNSUPPORTED-CELL` findings in 1 scoped table (no `UNBOUND-ROW`, no `NO-CAPTURE`, no `NO-PATH`). Every finding was a cell whose content words did not co-locate with the row's bound capture inside an 80-token window.

After: 0 findings, rc 0. All 21 cells were rewritten from the words of their bound capture, and one binding line was extended to name the source that actually carries the Xhosa greeting/exhortation sequence (S1008). No cell was padded with keyword lists; each rewritten cell is a prose summary of a passage that was read in full, and where the capture's sense differed from the old cell's sense (Hausa reward, Xhosa reward, Greek limit) the cell follows the capture.

## 2. Gates measured

| gate | command | rc | result |
|---|---|---|---|
| before | `python3 -B reports/round-100/controls/feasibility/table_support_ref.py --entry corpus/knowledge/linguistics/praise-poetry-panegyric.md --root /home/vgpnk/Projects/shokunin/kotodama-shokunin $(ls -d reports/round-*/evidence \| sed 's/^/--evidence /')` | 1 | 21 findings, 1 scoped table |
| after | same command | 0 | 0 findings, 1 scoped table |
| diff | `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --stat -- corpus/knowledge/linguistics/praise-poetry-panegyric.md` | 0 | 1 file changed, 9 insertions(+), 9 deletions(-) |
| index | `python3 -B tools/check-corpus-index.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` | 0 | `CORPUS-INDEX: OK files=271 rows=271 findings=0` |
| spans | `python3 -B spans.py` (scratch helper, 22 spans) | 0 | 22 checked, 0 bad; every span exact, `count == 1` whitespace-collapsed, <= 25 words |
| hash | `sha256sum corpus/knowledge/linguistics/praise-poetry-panegyric.md` | 0 | `9aaca1ba…bfb4ee84` |

## 3. Support table (21 changed cells)

Bound ids are the S-ids on the binding lines that bind each row; spans are exact substrings of the named round-99 capture, whitespace-collapsed, count 1.

| row | column | bound | decisive span | words |
|---|---|---|---|---|
| Southern Bantu court | singer and office | S1007 | `Tswana mmoki) were much respected members of the chief’s official retinue` | 11 |
| Southern Bantu court | patron and reward | S1007 | `at the installation of a new chief, or at the distribution of royal bounty` | 14 |
| Southern Bantu court | form and order | S1007 | `starting with the famous praises of the king’s or chief’s ancestors` | 11 |
| Southern Bantu court | limit on the praise | S1007 | `criticism which can provide a kind of social pressure on an unpopular chief` | 13 |
| Yoruba | patron and reward | S1007 | `the drummers go about the streets formally addressing the passers-by and receiving a small reward` | 15 |
| Yoruba | form and order | S1007 | `the praises of the king, with the complete list of his predecessors and their praises, must be recited once a year in public` | 23 |
| Hausa | patron and reward | S1007 | `allocated compounds, farm-lands, and titles by the king` | 8 |
| Hausa | limit on the praise | S1007 | `of people frequently include derogatory remarks, veiled or otherwise, or give advice as well as praise` | 16 |
| Mande and Soninke | patron and reward | S1007 | `reputedly wealthy individual for their praises` | 6 |
| Mande and Soninke | form and order | S1007 | `to wander through the streets or attend festivals on their own initiative` | 12 |
| Mande and Soninke | limit on the praise | S1007 | `even those who refer to them contemptuously as ‘beggars’ are in fact glad to reward them with gifts` | 18 |
| Greek epinician | singer and office | S1012 | `For his very calling of song-writer to all Hellenic states without discrimination` | 12 |
| Greek epinician | patron and reward | S1012 | `For the magnificent Sicilian princes, Hieron of Syracuse and Theron of Akragas` | 12 |
| Greek epinician | form and order | S1012 | `triumphal odes for victories in those great games` | 8 |
| Greek epinician | limit on the praise | S1012 | `he answered that he had chosen to live his own life, and not to be the property of another` | 19 |
| contemporary Xhosa | patron and reward | S1011 | `poetry in the form of izibongo is alive and well within trade unions and political organizations` | 16 |
| contemporary Xhosa | form and order | S1008 | `Manisi turns next to exhortation` | 5 |
| Tamil puram | patron and reward | S1014 | `The kings, chieftains and other headmen of small cities have patronized bards` | 12 |
| Tamil puram | limit on the praise | S1014 | `They were good friends, counsellors and ambassadors too.` | 8 |
| Welsh and Irish bardic | singer and office | S1013 | `By the rules of his order a Bard was not permitted ordinarily to bear arms` | 15 |
| Welsh and Irish bardic | form and order | S1013 | `It is divided into stanzas` | 5 |

Binding-line change (Xhosa): `…the censorship finding (S1011) and the conference performance's greeting and exhortation (S1008).` — spans `He then greets the audience of academics before him (lines 6-9)` (11 words, count 1) and `Manisi turns next to exhortation` (5, count 1), both in S1008. The added line binds no other row (its tokens carry no other row's label tokens).

## 4. Invariants (counter leg O3 depends on them)

Verified against `git show HEAD:…` by a comparison script, rc 0:

- table header and separator byte-identical;
- all 9 row labels byte-identical;
- Yoruba row's last cell byte-identical (`an epithet can recall danger or contested reputation rather than flatter`);
- Norse row byte-identical in all five cells;
- whole-file diff = 18 changed lines (9 table rows + 1 binding line); no heading, topic line, §7 prose paragraph or §8 text changed.

## 5. Residuals / known limits

- No type-(c) residual: nothing was kept on the strength of a passage the window misses. `after.txt` is 0 findings.
- Dropped content (no co-located support; removed rather than padded): "graded by skill", "chained into stanzas", "withholding", "rewarded by the praised", "*oriki* recited or drummed", "District Head and graded chiefs; instrument rank marks status", "*kirari*", "chosen notable", "commissioned", "patronage and public honour", "myth and moral counsel", "civic … public standing", "gifts before the bard moves on", "counsel and embassy", "*fili* attached to a lord", "praise in song and commemorative naming of warriors".
- One partial-sequence loss: the Xhosa "greeting, praise, exhortation, closing praise" cannot be one cell — in S1008 the greeting is more than 80 tokens from the exhortation and conclusion. The cell keeps exhortation→conclusion; the binding line records both greeting and exhortation, and both spans are cited.
- Semantic correction: the Xhosa reward cell no longer asserts a reward, because neither S1011 nor S1008 records payment; the old "public standing" was an unsupported inference.
- Checker limit (inherited from `claims.json` `residual_honesty`): lexical co-location is not meaning. Each cell was checked against the passage's sense, not only its vocabulary.
- Not run here (other seats' legs): battery100, mutation100, the O3 forged-cell replay, the O and C legs, and any commit. This seat wrote no other file.

## 6. Artifacts

- `corpus/knowledge/linguistics/praise-poetry-panegyric.md` — repaired entry (sha256 above).
- `.ufo/waves/round-100/w1/stage/ScribeTable100/before.txt` — 21 findings, rc 1.
- `.ufo/waves/round-100/w1/stage/ScribeTable100/after.txt` — 0 findings, rc 0.
- `.ufo/waves/round-100/w1/stage/ScribeTable100/support.md` — full per-cell before/after table, spans, residuals.
- `.ufo/waves/round-100/w1/stage/ScribeTable100/DONE` — sha256 of the entry.

Tooling installed or upgraded: none.
