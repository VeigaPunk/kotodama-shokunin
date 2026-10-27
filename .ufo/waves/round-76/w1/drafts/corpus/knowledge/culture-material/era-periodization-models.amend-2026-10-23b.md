# Amendment — the archive's own era table: three tabs, three bounded working sets

- source: S894 — https://www.digital.archives.go.jp/search — 国立公文書館デジタルアーカイブ「詳細検索」, the 元号選択 dialog's three tables (和暦元号 / 中国元号 / 朝鮮元号), each headed by the columns 元号名称 and 開始西暦年, with the form's own date row labelled 年月日(元号) — fetched 2026-10-27 (browser-shaped User-Agent, HTTP/2 200, 311,308 B, sha256 204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8; two fetches the same day were byte-identical; the three tables are in the served HTML, no script execution needed to read them)
- verified-at: 2026-10-27
- recheck: 180d — `curl -fsSL -A '<browser-shaped UA>' 'https://www.digital.archives.go.jp/search' | grep -c '開始西暦年'` -> 3 and `| grep -c '文治'` -> 3 on 2026-10-27; then re-extract the three tables from `#gengo-modal` and re-count rows (248 / 94 / 8) and re-locate 令和 2019, 文治 1185, 大化 645, 康徳 1934, 金収国 1115, 朝鮮乾隆 1736 and 朝鮮永楽 1403. A span that stops locating marks this row unverifiable; a lost span is never softened into a paraphrase. The receipt and the extracted window are this round's `stage/ScribeEntryC/window.txt`, beside the raw bytes as `stage/ScribeEntryC/na-search.html`.
- ground: at base 98c486b the lane's knowledge corpus holds no archive's era table — `git grep -c '元号名称\|開始西暦年\|国立公文書館' 98c486b -- corpus/knowledge` matches 0 files, and `git ls-tree -r --name-only 98c486b -- corpus/knowledge | grep -ci 'era-period'` returns 1, the base entry this file amends. The host named above appears once in the whole corpus, in a round-68 lesson line recording a refused candidate, and in no knowledge entry.
- topic: one institution's era-name table as it is operated rather than as it is described — the National Archives of Japan's detailed-search date picker, which offers three era-name traditions in three tabs of very unequal size, keys a search as an era name plus a year rather than as an absolute date, and resolves colliding names by a polity prefix and a start year.
- gap filled: the era entry this amends carries the Sinosphere era-name system as culture and craft — §2's typology, §3's selection rules, §4's seam logistics, §13's build order — but nothing in it records a working catalogue's version of the same instrument: which names a real archive actually offers a searcher, how each list is bounded, and what the table does when two names collide. This amendment adds that one instrument, its three coverages and its two collision rules, and no further theory.
- sources: the one row above, tier A — the archive's own live search interface, read by a plain request with no challenge, no cookie and no second route. Tier A is scoped to what this archive's form offers; it is not tier A for the history of any era name, and it does not extend to how any era's years are officially read.
- couples: `culture-material/era-periodization-models.md` (the base this amends); `culture-material/calendar-festival-systems.md` (the calendar machinery an era count rides on); `linguistics/naming-systems.md` (era names as the most regulated name coinage there is); `myth-symbol/celestial-symbolism-calendars.md` (the cycle machinery an era sequence sits inside); `synthesis/worldbible-integration-contract.md` (where a period table becomes a world-bible record that lore owns).
- scope: an amendment to the era entry. It records one archive's dating instrument — three tables, their boundaries, and the two ways a name collides — and the checks a period table has to pass if a searcher is to use it. It decides no era, asserts no completeness for any list, and makes no ruling about any real or invented polity's legitimacy.

## 1. The table is a form's input, not a reference list

The page is titled 詳細検索 and carries a date row labelled 年月日(元号), set through a dialog headed 元号選択; the dialog divides into the tabs 和暦元号, 中国元号 and 朝鮮元号, and each tab is a table headed 元号名称 and 開始西暦年, with a 選択 cell on every row (S894). The form carries the chosen era as two named values, `date_e_from_era` and `date_y_from_era` — the era name and the year inside it (S894).

That pairing is the whole design decision. A query is built as "this era, year n", so the catalogue stays addressable in the vocabulary its records were written in, and the Western year appears only as a column printed beside each name. The table's job is to let a searcher reproduce the phrase a clerk wrote, not to convert that phrase into a modern date.

The consequence for a period table is checkable: if the instrument cannot be searched by the phrase on the document, the table is decoration. A catalogue that only accepts absolute years has silently re-dated its holdings before anyone reads them.

## 2. Three tabs, and three coverages that differ by a factor of thirty-one

The 和暦元号 tab holds 248 rows, beginning 令和 2019 and ending 大化 645, with 文治 1185 at index 141 and 106 names after it; no name appears twice (S894). The 中国元号 tab holds 94 rows, beginning 康徳 1934 and ending 金収国 1115, composed of 南宋 23 names, 金 21, 明 20, 元 14 and 清 13, plus 康徳, 大同 and 民国 one each — with no Tang, no Northern Song, and nothing earlier than 1115 (S894). The 朝鮮元号 tab holds 8 rows, 朝鮮乾隆 1736 to 朝鮮永楽 1403, every name prefixed 朝鮮 (S894).

Three era-name traditions, one tab each, and sizes of 248, 94 and 8. The page states no reason for either boundary, and it does not say which holdings each list serves (to-verify). What the served bytes do show is the shape of a working set rather than a historical corpus: the Chinese tab is not a history of nianhao — a list that stopped at 1115 and skipped the Tang and the Northern Song is not one — and the Korean tab's eight rows are a sample, not the Joseon record. A search form offers the names its holdings need.

The ordering is part of what the table says. The 和暦元号 tab runs in descending start year from 令和 2019 to 暦応 1338, then breaks: eight rows run 元中 1384 down to 延元 1336, after which the descending run resumes at 建武 1334 (S894). The page attaches no label to that eight-row block and gives no reason for it; that the block is the Southern Court's count, kept beside the Northern line's, is not stated on the page (to-verify), and no sentence here depends on the identification — what the bytes show is a run that does not follow the tab's own ordering. The 中国元号 tab is grouped by dynasty instead: 康徳, 大同 and 民国 one row each, then 清 13, 明 20, 元 14, 南宋 23 and 金 21, each group descending by start year, so the tab's order is a classification first and a chronology second (S894).

## 3. Two collisions, and the two rules that resolve them

The tables collide twice, and both collisions are visible in the served rows.

Within one tab, a name repeats. 元至元 stands at index 37 with 1335 and again at index 48 with 1264, so only the year column separates the two entries (S894). Across tabs, a name and a year repeat together: 清乾隆 1736 in 中国元号 and 朝鮮乾隆 1736 in 朝鮮元号 are the same two characters with the same start year, separated only by the polity prefix the archive added (S894). A third case is a placement rather than a collision: 康徳 1934, 大同 1932 and 民国 1912 are filed inside the 中国元号 tab, and the page gives no rationale for putting them there (S894) — a classification the page makes and does not argue.

Three rules follow, and they are the reason this file exists. Key an era on the pair (name, start year); a name alone is not a key. Where a name is shared across polities, make the polity part of the key, as the 朝鮮 prefix does, because the same characters can start in the same year in two states. And when a table files one polity's eras under another's heading, label that filing as a decision, since a reader can reasonably file them elsewhere.

## 4. What a period table must carry

The instrument question first, then the table it implies.

| Instrument question | What this archive's table does | What a period table must therefore carry |
|---|---|---|
| What phrase does a searcher have? | accepts an era name plus a year inside it | a name-plus-ordinal key, not only an absolute year |
| Which traditions does the holding use? | three tabs, one per tradition | one list per tradition, never one merged list |
| How far does each list reach? | 248, 94 and 8 rows, boundaries unstated | the first and last entry of each list, printed |
| What happens when names collide? | year separates within a tab; polity prefix across tabs | both separators, in the key itself |
| What if a polity is filed elsewhere? | 康徳 and 民国 sit in the Chinese tab, unexplained | the filing decision stated, with its rationale |

Drafting checklist, in order. Write the first and last entry of each list before writing any middle entry, because the boundary is the claim. Decide the key before the display column: name plus ordinal year, or name alone, and say which. Add the polity prefix where two states can share a name. Record every filing decision the table makes about a polity, and record it as a decision. Then test the instrument: take one document your world would hold, write the date as its clerk wrote it, and see whether the table can be searched by that phrase without re-dating it first.

Worked example, canon-free: a port town's charter is dated in its own third era, year 4, and the town changed hands once. A usable table lists that era with its start year, lists the previous era it replaced, prefixes the town's count and the conqueror's count differently if both are in use, and says which list the town's records now sit under. The table decides nothing about the town; it only makes the charter findable in the words the charter used.

## 5. Calibration

**The archive's era table as an instrument — mainstream, because it is observed in operation.** This is a live public search form, not a claim about history; the row is tier A for what the archive offers a searcher and for nothing else.

**The 248-name 和暦 sequence — mainstream as the standard nengō list of the institution that owns the count.** What is recorded here is the tab's row count and its two ends, not an ordinal: the page does not say which number 令和 is, and this file does not supply one from elsewhere.

**The 中国元号 tab as a history of Chinese era names — discredited as soon as it is stated that way.** Ninety-four rows running 1115 to 1934, with no Tang and no Northern Song, is a working set. Reading it as the corpus of nianhao is the error this section exists to stop.

**The 朝鮮元号 tab as the Korean record — discredited by its own size.** Eight rows, and every one of the eight also stands in the 中国元号 tab under a dynasty prefix, the same name in a different tab; a list that small is a pointer, not a coverage.

**The placement of 康徳, 大同 and 民国 inside the Chinese tab — contested, and unresolved on the page.** The filing is observable; its reason is not stated, and this file records the filing without adopting the rationale.

**Reading the three lists as the archive's holdings — (to-verify).** The page shows the picker's options; it does not state which records fall under each era, and no sentence here infers that.

## 6. Limits, the capture that was not used, and the handoff

The live page served the tables, so no capture was needed, and none is claimed: the Wayback copy this round's plan paired with the row was unreachable from this host on 2026-10-27 — three attempts, of which two were connection failures and the third an HTTP 302 that returned no body — and the row therefore rests on the live response alone, as its source line records. Nothing here describes what any capture holds.

One earlier lane record needs correcting rather than repeating. A round-68 verdict refused this same URL as "a portal landing, not the table page"; the 2026-10-27 served bytes carry three era tables under `#gengo-modal`, so that reason does not hold for this scope. That is a correction of this lane's own record about the artifact, not a claim about the source, and it belongs in the round's collision guard.

Two further limits. The served HTML wraps the 年月日(元号) row in a container class named `enHideArea`; the site's English surface was not opened this round, so what that class does there is unobserved and no sentence above depends on it. And a tab's row order is not a claim about succession: the 中国元号 tab orders by dynasty before year, the 和暦元号 tab carries eight rows outside its own descending run, and one tab can carry two courts' counts in a single list, as the 南宋 and 金 groups in the 中国元号 tab do — the rule that one reign takes one era belongs to the held entry, not to this table.

This amendment appends to `culture-material/era-periodization-models.md`, whose base points here through its `couples:` line. It records one archive's dating instrument and the checks a period table passes or fails; canon, consistency verification, and any ruling about what a fictional world holds belong to lore-shokunin, and this file ends at that handoff.
