# Round 72 (2026-10-25, hyaku run 6, L1 kotodama-r72)

Claims: Ca (calibration — round-71 routed defects K71-1..K71-8 land as append-only
corrections) and C (coverage — shokuknow assimilation of the heritage-taxonomy theme,
two entries, staged rows re-pointed by document to lane rows S874/S875). Round shape:
one v1 wave, 32 seats (7 scout, 6 reviewer, 5 critic, 4 executor, 3 scribe,
3 mutation-tester, 1 sentinel, 1 connector, 1 revenger, 1 simplifier; 16/32 attack
roles = 50%), one batched dispatch under policy v1 (band 32-64).

## Gate

Admitted this round (both opened by this lane 2026-10-25; re-pointed by document
from staged rows — old staged ids S863/S867/S967, listed per CORPUS.md rule 2's
old→new convention in the adoption note below):

| source | access date | quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|
| S874 — https://www.ihchina.cn/project.html (live, HTTP 200 2026-10-25 after one initial 25 s timeout; carriers: captures 20200216023423id_ and 20261020183948id_) | 2026-10-25 | “国家级名录将非物质文化遗产分为十大门类” | 清单页 taxonomy paragraph, verbatim in the 2020 capture, the 2026 capture, and the live page | admitted |
| S875 — https://online.bunka.go.jp/db/heritages/search (live, HTTP 200 2026-10-25) | 2026-10-25 | “安土・桃山” | 検索フォーム「時代」select option, verbatim as served | admitted |

Adoption old→new (by document, never arithmetic): staged S863 (ihchina 清单页) →
lane S874; staged S867 (bunka 文化財検索) → lane S875; staged S967 (the 2020 Archive
capture of the same PRC page) → the S874 row's dated carrier, cited in text. The
staged set's own S874/S875 (onomastics rows, register S791 unverifiable / S792
refused) are NOT adopted; the collision receipt records them as not-adopted.

Rejected from the assimilation set (reason + flip):

| staged entry | refused staged rows | reason | flip |
|---|---|---|---|
| myth-symbol/narrative-structure-frameworks.md | S870 (register S787) | staged row's quoted span absent from the fetched page (round-71 quarantine REFUSED; fabrication class — the staged quote is not on the page) | a re-opened source carrying the quoted span, written as a new row |
| culture-material/worldbuilding-setting-practice.amend-2026-10-23.md | S899, S900 (registers S816, S817) | both cited rows quarantine-REFUSED (round-68 and round-71: quoted spans absent) | the same, per row |

Per-row re-open evidence: the ihchina live page and both captures were fetched
2026-10-25 (scout + L1, artifacts .ufo/waves/round-72/assimilation/ and
/tmp/r72-entries/); the bunka page fetched live 2026-10-25 (231736 B). All four
Gate quotes above are 1 token under `wc -w` (CJK); over-length is impossible for
these quotes, and the ≤25-word cap is checked by direct word count (never by
tools/check-gate-quotes.py — its pipe-row blind spot is routed, not claimed).

Sibling-overlap note (connector, 2026-10-25): the heritage-taxonomy surface is
in-lane, uncontested — lore's PROVINCE assigns culture-material design models to
kotodama by path; chousa claims research method only; no sibling claims the
surface. Handoff obligation: none fires (rows are used-by lane-internal method
entries; no handoff packet fields); lore-side §1 activation of the integration
contract is pending, so §7 of the canonical entry describes the route, not an
active transfer.

## Mistakes

| class | evidence | captured-by | fix | state |
|---|---|---|---|---|
| in-place-edit | LOG.md:4274 and corpus/lessons/round-71.md:83 were edited in place at 99e3d63 (S861→S992 → S874→S1005) and LOG.md at 1721fbd (<RECORDS> placeholder line, misroot-sweep line), against LOG.md:1's append-only invariant; the fleet report was rewritten in place three times (bc418b99, 98873dfd, 8380f703) | PROTOCOL append-only invariant; K71-3/K71-4 | appended corrections only this round (claim Ca); QUALITY criterion 21 not needed for this class — it is a Gate-discipline criterion; the round-72 corrections are the fix, proven able to fail by MutCaAppend (m2/m4 mutations FAIL the APPENDONLY leg design) | fixed |

## Quarantine

Adoption OPEN this round (wave-4 quarantine-first completed by rounds 68-71:
21/21 register rows verdicted). Admitted: the two heritage-taxonomy entries above.
The staged REFUSED set (register ids S779, S786, S787, S792, S814, S816, S817 →
staged S862, S869, S870, S875, S897, S899, S900, S933) is not adoptable; both
rejected entries above cite staged rows from that set.

F-1 correction (ScoutQuarantineCross, 2026-10-25): the filed round-71 note for
register S792 says "the four Chinese headings absent" — that reason is factually
wrong (the four headings 实际影响取向 / 社会认知取向 / 自我信息加工取向 / 文化产品取向
are present on the fetched page, two hits each); the slash-joined quoted span is
genuinely absent, so the REFUSED verdict and the staged S875/S933 refusal stand,
only the stated reason is corrected here.

F-2 note: register ids are a third namespace (corpus-expansion-1 census ids), not
live registry ids; the slice joins to staged rows by URL only
(.ufo/waves/round-72/assimilation/reg-to-staged.txt; MutRegistryCollision verified
the join on all 21 rows).

## Corrections (pre-data, claims freeze)

Round-72 claims were frozen before data; wave-1 attacks forced these pre-data
corrections (full text: reports/round-72/claims.json `pre_data_corrections`):
CASTAMP reworded (the base receipt already carried the true pairing — the leg now
requires a NEW receipt naming the defective pairing); the counters read
id-renumber-map.json at its real path and the fleet report from the fleet repo;
W2FILES enumerates the actual seven files; APPENDONLY enumerates its file set and
the fleet-report last-touch check; QUAL21 gained command terms; the C kill-rule's
"opened this round" clause restated as enumerable Gate bytes; do-nothing controls
committed; the ihchina live page was opened HTTP 200 on 2026-10-25 (one initial
timeout) so entry/row texts say opened-live, captures as dated carriers.

## Frontier-step

Registry 797 → 799 rows (S874, S875 opened and mined this round); census exit 0 at
start (reports/round-72/telemetry/census-start.txt) and end (census-end.txt). The
two rows are this round's sourced claim (claim C).
