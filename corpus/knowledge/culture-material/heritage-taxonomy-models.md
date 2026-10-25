# Heritage taxonomies — how states classify their own intangible and material culture

- source: S874 — https://www.ihchina.cn/project.html — 清单页「国务院先后于2006年…公布了…批国家级项目名录」段 + 「国家级名录将非物质文化遗产分为十大门类」段 — fetched 2026-10-25 live (HTTP 200, after one initial 25 s timeout) and via the Internet Archive captures 2020-02-16 (四批) and 2026-10-20 (五批)
- source: S875 — https://online.bunka.go.jp/db/heritages/search — 検索フォーム「時代」選択肢 + 「分野」選択肢 + 検索条件「指定区分」 + 記録行「材質・構造・技法」等 — fetched 2026-10-25 (live)
- verified-at: 2026-10-25
- ground: assimilated from the shokuknow corpus-expansion-1 package (merge/kotodama, staged for this lane 2026-10-23/24) under the round-72 §10 adoption; the package's staged rows were re-opened by this lane on 2026-10-25 and re-pointed by document (old staged ids listed in the round-72 lesson Gate; one staged row was the same PRC document family, a dated capture).
- recheck: 180d — re-open both rows' URLs/captures and re-locate the quoted spans (carriers: the PRC row's two web.archive.org captures 20200216023423id_ and 20261020183948id_ plus its live page as served 2026-10-25; the Japanese row's live page)

- gap filled: the lane held no state-published heritage classification at all before this entry: `grep -inE 'ihchina|非物质|非物質|文化遺産|heritage online|bunka' corpus/SOURCES.md` prints nothing at the 797-row registry (re-run 2026-10-25, receipt reports/round-72/telemetry/gap-sweep.txt), and `find corpus/knowledge -name '*heritage-taxonomy*'` prints nothing. The lane's era knowledge (`era-periodization-models.md`) is political and archaeological; it never had the ladder a museum uses to date an object, nor a state's own filing taxonomy for craft and ritual. Both are directly reusable as an invented culture's craft-and-ritual taxonomy and museum-era ladder.
- topic: the two states' official category models for material and intangible culture, read as design systems: the PRC's ten-门类 intangible-heritage taxonomy with its 罗马数字 category code, its batch/扩展项目 mechanism and dated batch growth; Japan's cultural-property 分野 domain tree with its 時代 period ladder, its 指定区分 designation facet, and record-level fields (材質・構造・技法 / サイズ / 所在地).
- sources: the two rows above, both opened this round (2026-10-25), tier A, mined, each with a located quote in the round-72 lesson Gate. The ihchina live page was opened from this host on 2026-10-25 (HTTP 200 after one initial 25 s timeout); its two Internet Archive captures carry the register's dated states, and the row says so. Live record counters on both pages are treated as unstable and are not used as anchors.
- couples: `culture-material/material-culture-inference-method.md` (how to *read* an object; this entry is how a state *files* one), `culture-material/era-periodization-models.md` (political eras against heritage eras), `culture-material/calendar-festival-systems.md` (the festivals a taxonomy's projects carry), `synthesis/worldbible-integration-contract.md` (handoff of any invented taxonomy to lore).
- scope: a reference method for the culture-material partition. It describes real classification schemes so a worldbuilder can build an invented culture's craft and ritual taxonomy; it decides no world's canon.
- refuses: claims of canon or historical truth for any world; universal heritage taxonomies; real-world attribution rulings on the cited registers.

## §1 Calibration key — what an official catalogue can and cannot carry

An official catalogue is a state's own statement of how it files culture. It can carry:
a category list, a code rule, a batch history, a domain tree, a period ladder, and record-level
fields. It cannot carry: the lives of the classified practices, or stable counters (the register
counts move with every batch and were not used as anchors here). Read the PRC register as a
filing grammar, not as ethnography. (S874)
Read the Japanese database the same way. (S875)

## §2 A state-grade category model — the PRC's ten 门类

The PRC's national register states that the national list divides intangible cultural heritage
into ten 门类 (categories) (S874). The page names them: 民间文学, 传统音乐, 传统舞蹈, 传统戏剧,
曲艺, 传统体育、游艺与杂技, 传统美术, 传统技艺, 传统医药, 民俗 (all present in the captured
register text; five of the names were adjusted in 2008 and remain in use — the page says so
verbatim). The register's code rule is stated on the same page: 编号中的罗马数字代表所属门类 —
the Roman numeral in a project number encodes its category (S874).
For an invented culture, the reusable shape is: a fixed, named category set; a code rule that makes
the category recoverable from the identifier; and a named mechanism for extension (the page also
carries 扩展项目, extension projects under an inscribed item).

## §3 A state-grade domain taxonomy — Japan's 分野 tree

The Agency for Cultural Affairs' 文化遺産データベース files cultural properties under a 分野
(domain) tree whose 16 top-level options, as served, run: 建造物, 伝統的建造物群, 絵画, 版画,
彫刻, 工芸, 考古, 歴史, その他の美術, 民俗, 伝統芸能, 工芸技術, 文化財保存技術, 史跡, 名勝,
天然記念物 — with sub-options under each expressed by leading whitespace (e.g. 建造物 breaks
into 宗教建築, 城郭建築, 住居建築, 近世以前その他, 近代その他) (S875). This is a material-domain grammar: it
answers "what kind of thing is it" before "when is it from".
A worldbuilder can lift the shape — a small top-level domain set with per-domain sub-vocabulary —
without lifting the labels.

## §4 Two period ladders — the 時代 ladder against the political era names

The same Japanese search form carries a 時代 (period) select whose [日本] branch runs 旧石器, 縄文,
弥生, 古墳, 飛鳥, 奈良, 平安, 鎌倉, 南北朝, 室町, 安土・桃山, 江戸, 明治, 大正, 昭和, 平成, 令和 —
an archaeological-to-reign ladder — and parallel [中国] (旧石器 … 清) and [朝鮮半島] branches (S875).
Against the political era names in `era-periodization-models.md`, the ladder a museum uses to date
an object is a different, emic-period vocabulary. A world bible wants both: reign names for
documents and law, ladder names for objects and digs.

## §5 Record-level fields — what each buys a builder

The Japanese register's record rows carry 材質・構造・技法 (material, structure, technique),
サイズ (size), 所在地 (location) as per-record labels, and the search form adds 指定区分
(designation class) as a filter facet (S875). Each field buys a concrete design decision:
材質・構造・技法 forces a craft ontology; a designation facet forces a protection tier (national /
prefectural / municipal — the invented analogue is a custody chain); 所在地 forces a geography
of custody. The PRC register's
counterpart is the project row: a stable 编号 (identifier) plus category and batch (S874).

## §6 Building an invented culture's taxonomy — take the state-shaped fields, not the labels

The transferable unit is the field set, not the category names. A build order:
(1) fix the category set size and name style (the PRC uses ten functional 门类; Japan uses a
material 分野 tree — the choice is a cultural claim about whether heritage is practice-typed or
object-typed); (2) fix the code rule so category is recoverable from the identifier
(one Roman-numeral slot vs a prefix letter); (3) decide the extension mechanism (扩展項目-style
sub-items under a stable parent); (4) fix the period ladder(s) the catalogue dates by, separate
from reign names; (5) fix record fields (material/technique, size, location, designation class).
Both registers show the category system outliving batch updates: the ten 门类 and the code rule
are word-for-word identical in the 2020 and 2026 captures, while the batch count grew from four
to five (S874, and see `heritage-taxonomy-models.amend-2026-10-24-r13.md`).

## §7 Coupling to the world bible

An invented culture's taxonomy lands in lore through the handoff contract
(`synthesis/worldbible-integration-contract.md`): this entry supplies the field grammar and the
two worked state models; lore decides the invented category names, code rules, and which bodies
keep the register. Kotodama hands off systems; lore records and verifies them.
