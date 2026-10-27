# Round 75 — kotodama: the narrative-structure thread closes (structuralist primaries + CJK narratology, assimilated)

**Claims line.** Lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15` (also HEAD;
no freeze commit exists — `git cat-file -e HEAD:reports/round-75/claims.json` → absent, so the round's
files are untracked working bytes and this lesson grades none of them), hyaku run 10, attempt 2
(attempt 1 filed nothing — R75-M1). **C (coverage, sourced):** nine rows S885–S893 opened and mined, one
row per document — staged S876/S885/S917/S921 → S885, S902 → S886, S904 → S887, S864 → S888, S865 → S889,
S866 → S890, S905 → S891, S919 → S892, staged S870 → S893 (the document re-opened) — over ground the lane
did not hold at base (`git ls-tree -r --name-only f556d1… corpus/knowledge | grep -c narrative` → 0);
three entries (`corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`, `…amend-2026-10-23.md`,
`…amend-2026-10-23b.md`); registry 808 → 817 rows; knowledge files 249 → 252; `reports/round-75/accept-c.py`
printing `ACCEPT-C-75: PASS legs=13/13`. **Ca (calibration):** `reports/round-75/ledger.json` as staged
holds **10 pairs, 6 REPAIR / 4 ANNOTATE**, L75-01…L75-10 (the w1 draft said eleven, 4 REPAIR / 7 ANNOTATE —
R75-M3), with `accept-ca.py` printing `ACCEPT-CA-75: PASS legs=12/12`. The predicate wording in
`reports/round-75/claims.json` is the authority this lesson is measured against; the claims are `DRAFT`.

## Gate

Access date for all nine rows: **2026-10-27**. One plain request per URL under the browser-shaped UA
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, each
request's UA bound to the response that request got (QUALITY 22); the per-row fetch line lives in the
receipt named in the evidence column. Every quote below is the text inside that row's `anchor` cell in
`.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md`, and each is inside both caps — 25
whitespace tokens and 80 characters; the measured lengths are given per row.

| source | access date | quote (≤25 words, ≤80 chars) | locator | evidence capture (this wave's stored record) | verdict |
|---|---|---|---|---|---|
| S885 — Roland Barthes, «Introduction à l'analyse structurale des récits», *Communications* 8 (1966) 1–27, https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | 2026-10-27 | «Innombrables sont les récits du monde.» (38 chars, 6 tokens) | notice body, opening sentence of the article (article p. 1); method passages read on the transcription pages p. 5 (T1_0005_0000), p. 6 (T1_0006_0000), p. 11 (T1_0011_0000) | `counters/probe-receipts/S885.txt` — HTTP 200, 111486 B, body sha256 `2bcdd019…`, `window-scope: whole-document` (visible 3720 < 4096), anchor quote found in the stored window after NFKC + whitespace folding | admitted |
| S886 — Tzvetan Todorov, «Les catégories du récit littéraire», *Communications* 8 (1966) 125–151, https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | 2026-10-27 | «Étudier la « littérarité » et non la littérature» (48 chars, 9 tokens) | notice body, first sentence (article p. 125); argument read on the transcription pages p. 125 (T1_0125_0000) and p. 139 (T1_0139_0000) | `counters/probe-receipts/S886.txt` — HTTP 200, 109335 B, sha256 `207ca821…`, whole-document (visible 3526), quote found folded in the window | admitted |
| S887 — A. J. Greimas, «Éléments pour une théorie de l'interprétation du récit mythique», *Communications* 8 (1966) 28–59, https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | 2026-10-27 | «Loin de se limiter à l'interprétation des énoncés, la théorie sémantique» (72 chars, 11 tokens) | notice body, §I opening paragraph (article p. 28); claim read on the transcription pages p. 29 (T1_0029_0000) and p. 30 (T1_0030_0000) | `counters/probe-receipts/S887.txt` — HTTP 200, 118776 B, sha256 `fbf48ad2…`, whole-document (visible 3073), quote found folded in the window | admitted |
| S888 — 中国社会科学院大学 研究生院,《叙事学》课程大纲 (课程编号 102072020193), https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf | 2026-10-27 | 故事是一种深层的抽象结构，必须通过话语呈现 (21 chars, 1 token) | PDF p. 3, 课程教学计划 section, 第二讲 故事：事件（一）, item 一 | `counters/probe-receipts/S888.txt` — HTTP 200, 225123 B, sha256 `62a13e92…`, `excerpt` window 4097 (visible 5481); the anchor quote is **not** in that stored window (note 2), and is present once in the fetched body per `assimilation/validate-receipt-draft.txt` | admitted |
| S889 — 小方 孝,「物語生成の物語論あるいはポストナラトロジー」, *Cognitive Studies* 25(2) 200–217 (2018), https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf | 2026-10-27 | a new research area called “narratology of narrative generation” (64 chars, 9 tokens) | PDF p. 1, English abstract under the 解 説 heading | `counters/probe-receipts/S889.txt` — HTTP 200, 1085244 B, sha256 `fdf60d27…`, `excerpt` 4098 (visible 45276), quote found folded in the window | admitted |
| S890 — 村井 源,「物語構造の階層的記述方式の提案」, *情報知識学会誌* 32(2) 246–251 (2022), https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf | 2026-10-27 | describe a story as a hierarchical structure consisting of three major layers (77 chars, 12 tokens) | PDF p. 1, English abstract | `counters/probe-receipts/S890.txt` — HTTP 200, 697092 B, sha256 `1dccf9d1…`, `excerpt` 4098 (visible 7205), quote found folded in the window | admitted |
| S891 — Roland Barthes, *S/Z* (Seuil, 1970), five-code excerpt «RB: S/Z», live https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html and durable https://web.archive.org/web/20041220223357id_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html | 2026-10-27 | les premières lexies suscitent l'établissement des cinq grands codes (68 chars, 9 tokens) | archived capture body, the paragraph on the five codes (*S/Z* fiche: «Par hasard, les premières lexies suscitent l'établissement…») | **no probe receipt exists — not yet captured as one.** The capture itself is recorded in `assimilation/validate-fetch/W891.meta` and `validate-receipt-draft.txt` (HTTP 200, 3898 B, sha256 `69b59872…`, anchor quote located once); the paragraph is described in `w1/ScoutUnigeSZ.md:40-42`, whose own recommended Gate span is a different clause of that paragraph | admitted on the archive copy; the live URL met an anti-bot challenge and the challenge was not passed |
| S892 — Gianfranco Marrone, «L'âge d'or de la sémiotique littéraire, et quelques conséquences théoriques», *Signata* 5 (2014) 57–72, live https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf and durable https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | 2026-10-27 | Mais combien, et de quelle nature, sont ces codes ? (51 chars, 10 tokens) | archived capture, PDF p. 7 of 25, the passage on Barthes's five-code typology (the round's entries cite it at printed p. 58) | `counters/probe-receipts/S892.txt` — HTTP 200, 763802 B, sha256 `8c030367…`, `excerpt` 4097 (visible 69791); the anchor quote is **not** in that stored window (note 2), and is present once in the fetched body per `validate-receipt-draft.txt` | admitted on the archive copy; the live URL answered HTTP 403 |
| S893 — 三九音域「世界观是打开小说幻想屋的钥匙」, in《我是怎样创作网络小说的——网络文学名家六人谈》, 中国作家网 2023-09-22, https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | 2026-10-27 | 网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则 (39 chars, 1 token) | §世界观是打开小说幻想屋的钥匙, byline □三九音域, paragraph 1, sentence 2 | **no probe receipt exists — not yet captured as one.** The page record is `assimilation/validate-fetch/S893.meta` (HTTP 200, 45238 B, sha256 `51251e22…`); `w1/ScoutChinawriter2023.md:36,41` carries the 14-character heading and the first 27 characters of this span (「网络小说中的世界观，指的是故事设定中世间万物运转的方式」), not its full 39 characters | admitted; the document re-opened from staged S870 |

Gate notes, each one a decision a reader can re-check:

1. **The quote is the row's anchor cell, not the probe receipt's `quote:` field.** For all seven probed
   rows the receipt's `quote:` is a page title or a 1–2 character token — S885/S886/S887 the article
   title, S888 `叙事学`, S889 `narrative`, S890 `物語`, S892 the dossier section title — because each
   probe was run with a title locator. The anchor quotes are locatable in the stored windows for five
   rows (S885, S886, S887, S889, S890: one hit each after NFKC + whitespace folding) and are absent from
   the stored windows for S888 and S892. This is R75-M2.
2. **Two stored windows would fail the EVIDENCE leg as they stand.** The leg requires the Gate quote to
   occur in the stored `--- window ---` text. S888's window (`chars=4097 before=10`) and S892's
   (`chars=4097 before=284`) both start at the document head and stop well before p. 3 and p. 7, where
   their anchors sit; each full body carries the quote exactly once
   (`validate-receipt-draft.txt`, `EVIDENCE-LOCATE PASS`, hits=1 for all nine). The committed evidence
   files at `reports/round-75/evidence/` must therefore window p. 3 and p. 7, not the title. Same class
   as R75-M2.
3. **Whole-document windows are honest here, four times.** S885 (3720 visible chars), S886 (3526), S887 (3073) and S891 (2169) are each shorter than the 4096-character floor, so `window-scope: whole-document` is the
   maximum available — the round-74 R74-M6 allowance, used as written. The other five declare `excerpt`
   with a window of at least 4096 characters.
4. **The Persée notices are not byte-stable, and the difference is not sha256-only.** Three stored
   observations of S885 disagree in both bytes and digest: the w1 seat fetch (111487 B, `9be2c68d…`),
   the probe receipt (111486 B, `2bcdd019…`) and the mirror rehearsal (109589 B, `25cfd7f6…`). The
   rehearsal's own note calls the drift "same length, different sha256", which is false of these three
   (the lengths differ too). S886 and S887 drift the same way (109335 vs 111234; 118776 vs 118777). Each
   evidence file records its own fetch line and its own `window-sha256:`; this lesson cites the probe
   receipts and names no byte count as canonical. Recorded, not repaired.
5. **S891 and S893 have no probe receipt.** Both quotes are the row anchor cells; S891's is located once
   in the 3898-byte archived capture, S893's once in the 45238-byte page. Neither is upgraded to
   execution evidence beyond that: the receipts that would bind them (`probe-receipts/S891.txt`,
   `S893.txt`) do not exist at this wave.

Rejections — each with the URL it was observed on, the reason, and the flip:

| reason | flip | probed URL | verdict |
|---|---|---|---|
| staged S870's quote `作品中的人物名字和地名也一样…` is absent from the page it is bound to: 0 hits on the 45238 B body, and the three shorter fragments `人物的名字` / `名字和地名` / `地名也一样` also 0, while the page's own 世界观 passage returns 1. The row is not appended | a fresh quote located on the same page — which S893 carries | https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | refused as staged; the document re-opened as S893 |
| the article-level PDF endpoint is CAPTCHA-protected: `docAsPDF/…1120.pdf` → HTTP 403 with body `<h1 class="title">This resource is protected by altcha</h1>`, and `/doc/…1113.pdf` → HTTP 404. A challenge met and **not** passed, so the endpoint is NOT used as an anchor and no `docAsPDF` fetch line may enter an evidence file | the per-page transcription service is ordinary and public: `/doc/page/…/…_T1_0005_0000`, `…_T1_0006_0000`, `…_T1_0011_0000` each answer HTTP 200 with article text under the same UA and no login, paywall or challenge, so every deeper locator is cited from a transcription page with its own capture | https://www.persee.fr/docAsPDF/comm_0588-8018_1966_num_8_1_1120.pdf | refused; not used |
| the live URL of S891 is not an openable anchor by ordinary means: HTTP 200, 46013 B, sha256 `c08372f1…`, a shell that sets a `bobcmn` script and asks for a code — a challenge met and not passed; no attempt was made to pass it | the same page's Wayback capture (2004-12-22) answers 200 with the fiche's body text; the row names live URL + capture and states the challenge was met and not passed | https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html | refused as a live-only anchor |
| the live URL of S892 answers HTTP 403 with a Cloudflare interstitial (`<title>Just a moment...</title>`, 5867 B, sha256 `92a72928…`) — a challenge met and not passed | the Wayback capture of the identical retrieve path answers 200 (763802 B) and carries the quote at PDF p. 7 | https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | refused as a live-only anchor |

The four reject rows above quote the numbers their seats recorded (`w1/SentinelScope.md` S-75-9,
`w1/ScoutPersee1120.md:45-59`, the w1 draft's S891/S892 rows, `w1/ScoutChinawriter2023.md`); this seat
re-fetched none of them and does not upgrade them.

**Triage of the 40 staged knowledge files.** Command:
`find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge -type f -name '*.md' | wc -l`
→ **40** (2026-10-27; culture-material 9, linguistics 17, myth-symbol 5, verification 9). Disposition, as
the round's triage line: **40 staged .md files in merge/kotodama/knowledge: 3 adopted / 6 path-present /
31 refused of the 40 (3 + 6 + 31 = 40)**. Path presence and byte equality were re-measured against the
base tree, not taken from round 74; the lane holds **0** files whose path matches `narrative` at base, so
all three adopted paths are new. The four files under `merge/kotodama/amendments`
(`naming-systems.md`, `calendar-festival-systems.md`, `era-periodization-models.md`,
`conlang-methodology.md`) are outside the 40 and are not triaged here.

- **Adopted (3, from 3 staged entries):** `myth-symbol/narrative-structure-frameworks.md` (30920 B),
  `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` (24166 B),
  `myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` (23049 B). The first two are the
  round's base entry and its dated amendment; the third is the five-codes amendment, admitted as its own
  path so the 1966/1970 attribution correction has a citable home.
- **Refused (31), by family** — 11 + 9 + 3 + 2 + 3 + 1 + 2 = 31, each row with a substantive reason and a
  flip:

| family | files | why not adopted | flip |
|---|---|---|---|
| naming-systems amendments | 11 | no lane row holds the document; the amendment chain re-states one topic without a located quote per claim | one row per document, each with a round-N capture and a located quote |
| calendar-festival-systems amendments | 3 | parent entry and sources are not lane rows; dates asserted from memory of the text | register the parent and the calendar sources, then re-quote |
| era-periodization-models amendments | 2 | same class as calendar: no parent row, no located span | register the parent and its sources first |
| verification amendments (citation-format r10–r16, journal-serial r16, reopen-gate) | 9 | lane-internal process texts, not source-backed domain knowledge; no registry row can support them | an own-work `source:` path with a lane-relative locator, or keep them as lessons |
| conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24 and conlang-methodology.amend-2026-10-24 | 3 + 1 | amendments to entries the lane already holds; their quoted spans were not re-opened this round and the staged bytes differ from the lane's | re-open each amend's quotes against the parent entry's rows and land as an appended amendment, one round per parent |
| narrative-structure-frameworks.amend-2026-10-23c.md and …amend-2026-10-24.md | 2 | refused **as separate extending paths**: their cited material is already carried by this round's admitted entries — 23c's four classes of the functional level on S885 (p. 11 transcription) in `…amend-2026-10-23.md` §N+2, and 24's Marrone statement on S892 (printed p. 58) in §N+3. Landing either file whole would register the same material twice | the two cited pieces are cited where they land, each with its own row and capture; a future round may re-open either file as its own amendment with a fresh located quote |

- **Path-present (6), staged bytes differ from the lane's** — a diff-for-new-claims-or-supersession
  decision is owed per file, which is not an adoption: `heritage-taxonomy-models` ×2,
  `worldbuilding-setting-practice` ×2 (the pair the lane adopted in round 74, whose staged copies differ
  from the landed bytes), and `conlang-scholarship.md` with its `.amend-2026-10-23.md`. Staged digest vs
  the lane's blob at base (12 hex digits each):
  `culture-material/heritage-taxonomy-models.md` `b17223b9a04b` / `09175b1849fb`;
  `…heritage-taxonomy-models.amend-2026-10-24-r13.md` `9ed5ceefe5b1` / `8544fe1ec531`;
  `culture-material/worldbuilding-setting-practice.md` `44a0899c5054` / `990e667c34bf`;
  `…worldbuilding-setting-practice.amend-2026-10-23.md` `39ac34ea0292` / `49a4432ae83b`;
  `linguistics/conlang-scholarship.md` `ce666a2bf15d` / `fe7e214adb04`;
  `…conlang-scholarship.amend-2026-10-23.md` `8f889666b32c` / `01029a642c9f`.
  All six differ from the lane's bytes, none was written this round, and no decision is taken here.

**S870's disposition, stated once.** The staged row stays REFUSED (its span is absent from the page, 0
hits, re-test in the reject table). The *document* is re-opened as lane S893 with a fresh located quote:
a re-opened document, not a reversal of the round-71/72 register verdict.

## Quarantine

**The standing register verdicts, re-derived this round, not re-fetched.** Slice derived with the
prompt's own command (`R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`,
`awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' "$R"`):

- **21 lines**, every one carrying an S-id → **21 data rows** (18 `payload-absent` + 3 unreachable-class),
  matching the round-71 ledger. Derivation note: the three unreachable-class lines print their id with a
  trailing backtick (`S807\``, `S812\``, `S835\``) because that register cell has no leading space before
  the class text; a parser that trims whitespace only keeps the backtick and would report three unknown
  ids. The count is unaffected.
- Re-counted over `reports/round-71/telemetry/quarantine-verdicts.md` (`grep -c`): `| PRESENT |` → **10**,
  `| REFUSED |` → **7**, `| UNVERIFIABLE |` → **4**, rows matching `^| S[0-9]{3} |` → **21**.
  **PRESENT 10:** S776, S778, S795, S796, S804, S820, S823, S824, S825, S827. **REFUSED 7:** S779, S786,
  S787, S792, S814, S816, S817. **UNVERIFIABLE 4:** S791, S807, S812, S835.

| row | verdict (round 71, standing) | note |
|---|---|---|
| S776, S778, S795, S796, S804, S820, S823, S824, S825, S827 | PRESENT | two travel with the table: S792's stated reason was wrong (the headings are present) and S824's span came from a search result rather than the PDF's own text |
| S779, S786, S792, S814 | REFUSED | source fetched cleanly, quoted span absent |
| **S787** | REFUSED | the China Writers 2023-09-22 page (`…/n1/2023/0922/c404024-40083104.html`) is about network fiction and its quoted span `作品中的人物名字和地名也一样…` is absent — re-confirmed by this round's S893 reject re-test (0 hits on four probes) |
| S816 | REFUSED | its span `这个我肯定考虑过。我自己就是资深读者…` is absent from the 2025 page it is bound to; the URL↔quote mispairing is the register's |
| S817 | REFUSED | the Sowers-Wills clause is absent from the 2022 page; the mispairing is the register's |

**Which rows this round's S885–S893 touched: none of the 21 by verdict, one by document.** No id in
S885–S893 appears in the slice. The single relation is by document: lane **S893** is the document behind
register **S787**, whose verdict stays REFUSED (the span is still absent, this round re-tested it) while
the document is registered fresh. S816/S817 — the pair the round-74 lesson's Correction below concerns —
are untouched: no row this round cites their pages, and their verdicts are not upgraded, retired or
re-opened. Bridging for the reader, by document only: register S787 ↔ staged S870 ↔ lane S893;
register S816 ↔ staged S899 ↔ lane S883 (round 74); register S817 ↔ staged S900 ↔ lane S884 (round 74).

Four clearing conditions govern any future adoption touching these rows: (1) the refused register rows
stay refused and are never edited in place; (2) a document is re-opened as a *new* row, never as a
reversal of the register verdict; (3) the quote must be located on the page in the round that adopts it,
from that round's capture; (4) the admitted bytes must be that round's entry, not the staged text.

## Collision guard (item 10)

**The guard, as CORPUS item 10 specifies.** Extractor `^ {0,3}\|[[:space:]]*S[0-9]{3,}` over the lane
registry and the staged package; ids normalised, then intersected. Files under
`.ufo/waves/round-75/assimilation/`:

| artifact | lines | range | sha256 |
|---|---|---|---|
| `reg-ids` | 808 | S001…S884 | `dd090b02e0f5c1e1b0eca105c9c37f913a9c937930737ec2c6450d74244e859e` |
| `staged-ids` | 132 | S859…S990 | `bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad` |
| `collisions` | 26 | S859…S884 | `01ad6576b56d150ad9505beda35775a2cf982ab110affd6c425704e21a357754` |

Re-derived by this seat: `grep -cE '^S(88[5-9]|89[0-3])$' reg-ids` → **0**, the same grep over
`collisions` → **0**; `collisions` spans S859..S884, `reg-ids` S001..S884, `staged-ids` S859..S990 (41
ids starting `S8`, 91 starting `S9`). **The adopted ids S885–S893 are free at base**, and none of the 26
numeric collisions names an adopted id. `collision-documents.txt` joins each of the 26 by URL:
**0 same-document pairs, 26 different-document pairs** — so the intersections are namespace drift, not
duplicate registrations, and the guard's acceptance is *by document*, not "collisions is empty".

**Guard proof** (`assimilation/guard-proof/proof.txt`, fixtures built by `make-fixtures.py` and run by
`run-guard.sh`; the planted ids S985–S989 are staged ids the registry does not hold at base):

| fixture | planted indent | 0–3-space extractor | column-zero-only control |
|---|---|---|---|
| `plant-1sp` S985 | 1 space | **found** (listed in collisions, exit 1) | not run on this fixture |
| `plant-2sp` S986 | 2 spaces | **found** (exit 1) | — |
| `plant-3sp` S987 | 3 spaces | **found** (exit 1) | sees **0 of the three** indented plants (the false green the contract warns about) |
| `plant-4sp` S988 | 4 spaces | not found (correct — indented code per the census parser note) | — |
| `plant-tab` S989 | 1 tab | not found (correct) | — |
| `real` (no plant) | 0 | 808 reg-ids, 26 collisions, census rows 808, census exit 0 | 808 reg-ids, 0 planted |

**Old → new map, by document, never by arithmetic** (`assimilation/id-renumber-map.json`; join key =
normalised URL: host lowercased without `www.`, percent-escapes decoded, `persee.fr/doc/page/<slug>/<transcription>`
collapsed to `/doc/<slug>` because a transcription page is a view of the document, and a
`web.archive.org` wrapper stripped because a capture is a carrier of the document):

| staged | document | lane id |
|---|---|---|
| S876, S885, S917, S921 | persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | **S885** |
| S902 | persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | **S886** |
| S904 | persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | **S887** |
| S864 | jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf | **S888** |
| S865 | jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf | **S889** |
| S866 | jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf | **S890** |
| S905 | unige.ch/lettres/framo/cernet/biblio/barth70.html | **S891** |
| S919 | iris.unipa.it/retrieve/…/2014 marrone age dor---2.pdf | **S892** |
| S870 | chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | **S893** (CONDITIONAL in the map; the condition — a fresh located quote — is met) |

The substitution must be one **simultaneous pass** over a single lookup table: staged `S885` is itself a
lane id this round adopts, so any sequential per-id replacement re-maps an already-mapped id. The
round-local prose ids are not keys: `S744 → S885` and `S763 → S887` are same-document rewrites (as staged
ids they would land as lane S744, the Dictionary.com ushanka page, and lane S763, the tafl-games
article); `S870 → S893` is the re-opened document, not an arithmetic neighbour.

## Normalization

**Every row is 11 cells and no cell carries a pipe.** `awk -F'|'` over the nine mirror rows prints
`NF=13` for each (id plus ten cells); `grep -cE '^\| *S(88[5-9]|89[0-3]) .*\\\|'` → **0**. Round 74's
failure mode — a backticked curl pipeline plus an escaped pipe splitting a recheck cell into twelve cells —
does not occur here, because the recheck cells are cadence-only as staged.

**Recheck prose stripped, per row.** The staged entries' `recheck:` lines carry the prose (the registry
cells never did); each row's cell is `180d` and nothing else:

| row | staged recheck prose it replaces | cell |
|---|---|---|
| S885 | `recheck: 180d — re-run the row recheck command in round 3's SOURCES-PROPOSED.md (S885 -> 1) (ran 2026-10-23)` | `180d` |
| S886 | `recheck: 180d — re-run the two row recheck commands in round 4's SOURCES-PROPOSED.md (S902 -> 1, S904 -> 1) (ran 2026-10-23)` | `180d` |
| S887 | same line as S886 (S904 is the second command) | `180d` |
| S888 | `recheck: 180d — re-run the four row recheck commands in SOURCES-PROPOSED.md (S864 → 1, S865 → 3, S866 → 2, S870 → 1) (ran 2026-10-23)` | `180d` |
| S889 | same line as S888 (S865 second) | `180d` |
| S890 | same line as S888 (S866 third) | `180d` |
| S891 | `recheck: 180d — re-run the row recheck command in round 5's SOURCES-PROPOSED.md (S905 -> 1) (ran 2026-10-23)` | `180d` |
| S892 | `recheck: 180d — re-run the two row recheck commands in round 7's SOURCES-PROPOSED.md (S919 -> 1, S921 -> 1) (ran 2026-10-24)` | `180d` |
| S893 | same line as S888 (S870 fourth) | `180d` |

The re-fetch and span checks now live in this Gate and in the seats' reports; the capture files are the
re-verification instrument. No staged recheck count (`S864 → 1`, `S865 → 3`, `S870 → 1`, …) is carried
into a cell, and R75-M3's relative is the reason: a cell that asserts a count its own span fails is
worse than a cadence.

**`used-by` rewrite.** Each row lists exactly the admitted entries whose `source:` lines cite it, checked
both ways (`assimilation/validate-receipt-draft.txt`, `USEDBY PASS`): S885 → base + `amend-2026-10-23`;
S886, S887, S891, S892 → `amend-2026-10-23`; S888, S889, S890, S893 → base. `source:` ids were rewritten
by document in the same pass (`S876/S885/S917/S921 → S885`, `S902 → S886`, …, `S870 → S893`), one id per
line, never by arithmetic.

**One normalization defect found and not repaired here.** In `…amend-2026-10-23.md:11` the S892 `source:`
line's URL is hard-wrapped mid-percent-escape — the line ends `…2014%20marrone%20age%` and the
continuation `  dor---2.pdf — « Mais combien… », p. 58` sits on line 12 as prose. A line-scoped reader
therefore sees a truncated URL: the mirror's own REPOINTED cross-check prints
`match: False` for S892 against `True` for the other eight. The entry owner must keep that URL on one
line before the freeze, or the REPOINTED leg reads a URL that names no document.

## Census

**Before:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`
→ **exit 0, 808 rows** (`.ufo/waves/round-75/census-start.txt`; the run also emits W01 ×3 for the
round-74 tier-C rows S881/S882/S884 and the standing W04 duplicate-URL warnings).

**After:** the round-end run of the same command, pasted by the L1 at landing in place of the line below.

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	W04	S358 duplicate url ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 across scopes
kotodama	W04	S482 duplicate url periodicos.ufpb.br/index.php/srh/article/view/13999/7921 across scopes
kotodama	W04	S483 duplicate url web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 across scopes
kotodama	W04	S485 duplicate url revistas.usp.br/sankofa/article/view/187402 across scopes
kotodama	W04	S490 duplicate url glottolog.org/resource/languoid/id/kiko1235.json across scopes
kotodama	W04	S561 duplicate url archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt across scopes
kotodama	W04	S564 duplicate url en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm across scopes
kotodama	W04	S565 duplicate url ag.colorado.gov/brands/about-brands across scopes
kotodama	W04	S566 duplicate url collections.vam.ac.uk/item/O1053476 across scopes
kotodama	W04	S569 duplicate url www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm across scopes
kotodama	W04	S570 duplicate url www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf across scopes
kotodama	W04	S571 duplicate url www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf across scopes
kotodama	W04	S572 duplicate url www.icphs2007.de/conference/Papers/1286/1286.pdf across scopes
kotodama	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	W04	S830 duplicate url collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals across scopes
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
```

Rows 808 → 817, exit 0 both times, no E-code line; W01 rows S881/S882/S884 as at start plus the new tier-C row S893 (the same class); the standing W04 duplicate-URL warnings are unchanged.

## Mistakes

Rules: `CORPUS.md` §"Rules added from the kaika campaign" — one row per mistake, class · evidence
pointer · captured-by · fix; a fix counts only once shown able to fail.

| id | class | evidence | captured-by | fix | state |
|---|---|---|---|---|---|
| R75-M1 | sequencing | Attempt 1 of this round ran a 42-seat build wave (15 scout · 2 connector · 6 scribe · 8 executor · 3 reviewer · 4 critic · 2 mutation-tester · 1 sentinel · 1 simplifier) and ended with unfinished counters, no freeze and no report. `.ufo/watchdog.log:1778` — `2026-10-27T16:37:22-03:00 lane-dead-no-report kotodama round=75; retry same round (hyaku-inline attempt=1: KotodamaR75 force-wrapped incomplete: 42-seat w1 only, no freeze, no report)`. At this wave `git cat-file -e HEAD:reports/round-75/claims.json` still fails: nothing of the round is committed | none — no criterion in `QUALITY.md` or `PROTOCOL.md` binds a wave's shape to a freeze, and the driver's completion line reports it only after the seat is dead | the round's plan states the freeze order (build → freeze → land) and the round is filed when the wave ends early: an early end lands the lesson, both counters' selftest receipts and the controls as the frozen set, rather than leaving 42 reports with no artifact. Shown able to fail: claim C's `do_nothing_control` runs the counter with `--lands` set to the freeze commit itself and must print FAIL with the data legs red, so a freeze with no data cannot pass as a landing | open |
| R75-M2 | instrument | The probe receipts bind a `quote:` that is not the row's anchor span, so a receipt cannot verify the Gate quote. `counters/probe-receipts/S885.txt` `quote: Introduction à l'analyse structurale des récits` (the title, 47 chars) against the row anchor `Innombrables sont les récits du monde.` (38 chars); likewise S886/S887 (titles), S888 (`叙事学`), S889 (`narrative`), S890 (`物語`), S892 (the dossier section title). Consequence: the anchor quote is absent from the stored windows of S888 and S892 — `grep -F` of each anchor span over its receipt returns 0, and a folded NFKC search over the window returns 0 too | none — the receipts record `quote-found: yes` honestly for the quote they were given, and nothing bound that field to the row's anchor cell | the probe quotes the row's anchor span (and, for a PDF, windows the page the anchor names, not the head); the GATE and EVIDENCE cross-check requires receipt `quote:` == row anchor cell and the anchor to occur in the stored window. Shown able to fail: on the current bytes the check flags exactly 7 of 7 probed rows at the `quote:` comparison and 2 of 7 at the window comparison | open — pre-freeze |
| R75-M3 | number-drift | The w1 lesson draft's claims line says "eleven ledger pairs (4 REPAIR, 7 ANNOTATE)"; the staged `reports/round-75/ledger.json` holds **10** pairs, ids L75-01…L75-10, with **6 REPAIR / 4 ANNOTATE** (`json` over `pairs`, 2026-10-27). Ca's own LEDGER leg asks for ">= 10 unique pairs", so 10 passes and 11 is stale | none — QUALITY 17/19 pin a receipt's stamp, not a prose restatement of a count | the lesson's claims line reads the counts out of `ledger.json` at write time and names the divergence, instead of copying the draft; the counter's LEDGER leg re-derives the pair count and the disposition histogram from the frozen blob. Shown able to fail: a lesson line claiming 11 against a 10-pair ledger is a one-command diff | resolved in this lesson |

**Pointers carried from round 74's `## Mistakes` — not re-derived, not re-scored this round:**

- **R74-M3 (survivor).** Four counter channels survived round 73 and were hardened in the round-74
  counters; the junk-landing receipts post-date that freeze (R74 corrections item 2). Pointer only.
- **R74-M4 (number-drift).** "Ca 9 scenarios" in `LOG.md:4297` and the fleet report against
  `SELFTEST OK: 10 scenarios`. Pointer only; ledger L75-10 is this round's separate table-fact pair.
- **R74-M5 (attribution).** Register S816/S817 bind each URL to the *next* row's quote; the checker that
  pairs a register row's URL with its quote still needs an adjacency guard. Still open — see Routed.
- **R74-M6 (vacuous).** The EVIDENCE leg's 4096-character floor is unsatisfiable on a short page; the
  `window-scope: whole-document` allowance is the fix, and this round exercises it four times (Gate
  note 3), which is its first real use on new rows.
- **R74-M7 (scope).** The GATE cell cap is 25 tokens **and** 80 characters; the two limbs disagree on
  which span a cell may carry. This round every anchor is inside both (longest 77 chars / 12 tokens,
  72 chars / 11 tokens), so the conflict is untested here — pointer only.
- **R74-M8 (reference-drift).** Drafts cited counters at paths where no counter existed. This round the
  claims name `reports/round-75/accept-c.py` / `accept-ca.py`, and at this wave neither is committed
  (`git cat-file -e HEAD:reports/round-75/accept-c.py` fails); the freeze must install both at the
  declared paths with their selftest receipts. Open until freeze.
- **Round-74 closure routed defects R1–R4** (`corpus/lessons/round-74-verifier-spotcheck.md` §5): R1 the
  APPENDONLY leg over-protects a contract-permitted `used-by` cell; R2 the S899/S900 reject reasons (this
  lesson's `## Corrections`); R3 the dangling pushed-hash pointer; R4 the carried-over lane items. R2 is
  answered below; R1, R3 and R4 stay pointers.

## Routed to round 76

1. **The six path-present files need a byte-level decision** (sha256 pairs in Gate): diff for new claims,
   or record as superseded, one decision per file.
2. **Register adjacency guard (R74-M5, still open).** The checker that pairs a register row's URL with its
   quote needs an adjacency guard; register S816/S817 bind each URL to the next row's quote, and the same
   class reached a Gate reject reason in round 74 (R75-M1's relative there).
3. **S877 scope-cell supersede row (round 74 routed item 5).** The round-74 entries cite S877 outside its
   registered scope cell and the append-only rule forbids widening the cell; a superseding row with its
   own scope and window is owed. No S877 successor is in this round's row set.
4. **R75-M2 in the counter.** Bind each evidence receipt's `quote:` to the row's anchor cell and require
   the anchor to occur in the stored window; window a PDF by the page the anchor names, not by the head.
5. **Persée byte-instability (Gate note 4).** Three observations of one URL disagree in bytes and digest;
   an evidence file must record its own fetch and its own `window-sha256:`, and no lesson or row should
   present a byte count as canonical. A future row could state which fetch it names.
6. **The S892 `source:` line wrap** (Normalization) — keep the URL on one line or the REPOINTED leg reads
   a URL that names no document. Same class: any 100-character wrap inside a URL.
7. **Register S787's verdict and its document are now split.** The register row stays REFUSED (span
   absent); lane S893 registers the same document with a fresh quote. The register is read-only, so the
   pointer is owed to the campaign, never written there: register S787 ↔ lane S893.
8. **R74-M3, R74-M4, R74-M6, R74-M7, R74-M8 and closure R1/R3/R4** stay pointers as listed under
   Mistakes; none is closed by this round.

## Sources & frontier

- **Registry rows: 808 → 817** (nine new rows, one per distinct document). Tiers verified against the
  rows themselves, not taken from a report: **A ×3** (S885, S886, S887 — the printed 1966 articles, opened
  page by page this round), **B ×5** (S888 the course syllabus, S889 and S890 the Japanese journal
  papers, S891 the university-hosted *S/Z* reading sheet, S892 the peer-reviewed account), **C ×1**
  (S893 the practitioner page, an industry outlet, never sole support for an entry). Status `mined` on
  all nine; `opened 2026-10-27`; `recheck 180d`.
- **Knowledge files: 249 → 252** (three entries on myth-symbol ground the lane did not hold; base count
  `git ls-tree -r --name-only f556d1 corpus/knowledge | grep -c '\.md$'` → 249, base files matching
  `narrative` → 0).
- **Frontier ground entered:** structuralist narrative theory as a design source (Barthes, Todorov,
  Greimas, plus the *S/Z* five-code apparatus) and its Chinese and Japanese counterparts (a Chinese
  narratology syllabus, two Japanese narrative-generation papers), plus one practitioner row for the
  Chinese web-fiction vocabulary of world-building.
- **`considerthese`: absent for this lane** (`ls considerthese` → no such directory), so no proposal is
  mined and no ledger row is added. **Assimilation:** adopted — one theme, three entries, nine rows.

## Corrections

Append-only; `corpus/lessons/round-74.md` is not edited. The two rows below are the round-74 closure's
routed defect **R2** and the ledger's ANNOTATE pairs L75-08/L75-09. Re-derived by this seat over the base
bytes; commands pasted exactly.

**The round-74 Gate reject rows for staged S899/S900 gave reasons that are false as written.** The staged
rows' own anchor spans are present on their own pages; the absent spans belong to register S816 and S817.
The disposition actually taken was adopt-with-renumber, so the Gate text is the defect, not the landing.

| where | old (as filed) | new (reclassified) | re-derivation command | output 2026-10-27 |
|---|---|---|---|---|
| `corpus/lessons/round-74.md:37` (staged S899 → lane S883) | "staged S899's quoted span was absent from the page it was bound to (register S816 mispairing; the span belongs to the 2022 interview) — the row stays refused and the document is re-opened as the new S883" | the staged span `非凡特性来自最初造物主` is present once on its own 2025 page in the committed round-74 capture; the absent span (`这个我肯定考虑过`) is register S816's, bound to that page. Disposition: **adopt-with-renumber (S899 → S883)**, not a reject; the mispairing belongs to register S816 | `git grep -c '非凡特性来自最初造物主' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S883.txt` | `1` |
| `corpus/lessons/round-74.md:38` (staged S900 → lane S884) | "staged S900's quoted span was the Sowers-Wills clause, absent from this page (register S817 mispairing) — the row stays refused and the document is re-opened as the new S884" | the staged span `这个我肯定考虑过` is present once on its own 2022 page in the committed round-74 capture; the Sowers-Wills clause is register S817's and belongs to lane S880's document. Disposition: **adopt-with-renumber (S900 → S884)**; the mispairing belongs to register S817 | `git grep -c '这个我肯定考虑过' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S884.txt` | `1` |

Cross-checks that fix which artifact carries the defect: `这个我肯定考虑过` in
`reports/round-74/evidence/S883.txt` → `0`; `非凡特性来自最初造物主` in
`reports/round-74/evidence/S884.txt` → `0`; `Sowers` in `reports/round-74/evidence/S884.txt` → `0`. So the
spans are on their own pages and the register pairs bind each URL to the other row's quote.

Scope of this correction: it reclassifies the *staged rows'* reject reasons. It does **not** touch
register S816/S817, whose own verdicts stay REFUSED (Quarantine), and it does not edit the round-74
lesson. The criterion this needs — a reject reason names the artifact it was observed on, staged row or
register row — is `QUALITY.md` criterion 27 in the round-75 claim Ca set.

## Status at landing

Appended by the L1 after the landings; the sections above were written by wave-2 seats before the freeze and
are kept as written. Where they speak in the present tense of the pre-freeze state ("no freeze commit exists",
"the claims are `DRAFT`", "neither counter is committed", "no probe receipt exists", "at this wave"), this
section supersedes them:

- **Freeze** `5d0167464309d8133991b30f7d7a7011a6a0fd14` carries `reports/round-75/claims.json` (`FINAL`),
  `ledger.json`, `accept-c.py`, `accept-ca.py`, the R1EXEMPT fixtures and receipts, the selftest receipts
  (`SELFTEST: 85/85`, `154/154`), the by-document map (sha256 `778068a4…` pinned in the claims) and the wave
  1-2 evidence; no landed data existed at the freeze (controls: `telemetry/controls-c.txt` 4/13 FAIL,
  `controls-ca.txt` 7/12 FAIL, both `lands == base` refused, exit 2).
- **Landings** Ca `012e8d3c8b92f47c734f735d58d118d574fe6a14`, then C `4f5e3b2535c2c06c51627dc2736c40183847cae1`.
  Measured: `telemetry/measures-ca.txt` `ACCEPT-CA-75: PASS legs=12/12`, `telemetry/measures-c.txt`
  `ACCEPT-C-75: PASS legs=13/13`; junk sweep `telemetry/junk-r75-run.txt`: no junk landing accepted.
- **Evidence captures.** All nine rows have committed `reports/round-75/evidence/S885..S893.txt` captured
  2026-10-27 by `counters/capture-evidence.py` with the row's own anchor quote (the w1 probe receipts, which
  bound a title locator instead, are superseded — R75-M2 is closed for the nine rows by these files and by the
  EVIDENCE leg, which graded all nine green at the C landing).
- **Pre-freeze claim edits (disclosed).** claims.json was edited five times after wave 1 and before the freeze
  (INDEX scope and SHONEN ownership, `rejects.counts` 3/6/31, integer-only counts, LEDGER pattern-operand
  wording, map sha pin); each is recorded in `claims.json` `pre_data_corrections` W2-F1…F5 and no seat had
  scored landed data at any of them.
- **Counter defects found by the first full rehearsal and repaired before the freeze:** PART A `table_rows`
  folded the Gate-notes list into the last Gate row (a blank line must end a table); the S892 `source:` line
  carried a truncated archive URL (completed); `leg_rejects` graded a path-present table-row bucket the claim
  wording does not require (relaxed to the claim text); the Ca LEDGER leg accepted a missing `parse`
  (now refused). Each is covered by the 85/85 and 154/154 selftests as committed.
- **A wave-2 seat wiped the round's shared scratch root** (`rm -rf /fast/scratch/hyaku/kotodama-r75`,
  ExecTmpSweep, 16:53); live seats rebuilt their directories and no committed byte was lost. The wave-3
  context now forbids removing anything above a seat's own directory.

## Wave-3 falsification of the landed bytes (filed by the L1; defects routed, not repaired this round)

Wave 3 = 36 seats against Ca `012e8d3c` and C `4f5e3b25`; reports in `.ufo/waves/round-75/w3/` (35 report files; ConnectorW2 of wave 2 and
three wave-3 mutation seats returned partial or inconclusive reports — `MutLandedC` ran M1 only, `MutIndexRejectsGround` ran nothing,
`MutEvidenceWindows` was incomplete — so no full mutation verdict exists for the landed bytes beyond the counters' own 85/85 and 154/154 selftests).
Held: both counters reproduce PASS at their landings (ExecRerunBoth, RevReadmeSkillQuality, ExecSeparability); assimilation item 10 all seven
obligations MET (RevAssimilationItem10); SCORECARD correction rows re-derive (RevScorecardCorrections); lore boundary (ConnectorLanded); the claims,
ledger, counters and map are byte-identical at freeze, Ca and C (RevFreezeChronology). **Defects found, all open:**

1. **Counting statements in this lesson that are false at `4f5e3b2`** (ExecCountsSweep F1-F13): the lines at the top and R75-M1 / R74-M8 describing the
   pre-freeze state (superseded by `## Status at landing`, not rewritten); adopted-entry byte sizes quoted from the staged copies (6862/5933/2514 vs
   30920/24166/23049 landed); Gate note 3 says three whole-document windows (landed: four); Gate notes 2 and cells for S888/S892 say the anchor is absent
   from the stored window (landed windows contain it); S885/S887 byte counts are the probe receipts', the committed evidence says 109588/116878; the
   Normalization note about a wrapped S892 URL in `amend-2026-10-23.md:11` describes a defect that was repaired before landing; the Gate path
   `assimilation/validate/corpus/SOURCES.md` was deleted before the freeze.
2. **Claim Ca's published command lacks `--combined`** and prints `FAIL legs=11/12` without it (ExecRunHygiene D2, ExecSeparability): the claim text is
   frozen; the measurement receipt `measures-ca.txt` carries the `--combined` form and a pinned local main.
3. **`accept-ca.py` writes under `/tmp`** when it re-runs the round-74 counter (`R74_TMPDIR = "/tmp"`, 121 mkdirs measured) and falls back to the system
   tempdir with no `--work`; accept-c refuses that. A frozen-counter amendment for round 76 (prompt section 7.4).
4. **The round's accept-c.py fails the QUALITY 23 addendum it lands** (limb 1 prints `GROUND_RECEIPT`) and QUALITY 27's selector matches none of this
   lesson's reject rows (RevReadmeSkillQuality F3/F4).
5. **Entry fact-check findings** (CritFactBase1/2, CritFactAmend23/23b, ScoutReopenS891): the syllabus participants table is labelled a transcription
   of six participants but has five questions; two §10 calibration rows use labels outside the entry's own vocabulary; Todorov adopting the Formalist
   position and the Greimas checklist generalise beyond the page; the S/Z "design order follows" sentence is not carried by the S891 page; the literal
   `grep -n 'four levels'` still matches the negated mentions in `amend-2026-10-23b.md`. ScoutReopenS892's `used-by` finding is a false positive (the landed
   S892 row names `...amend-2026-10-23b.md`, verified in the C tree).
6. **`selftest-c.txt` and SKILL.md:707 cite counter sha `fa5060b9…`**, bytes that exist in no commit (the committed counter is `315c5f3f…`); SKILL.md:701
   also rewords `receipt:` to `recorded in` beyond the declared sentence.
7. **A2-note wording "no landed byte existed at any point" is too broad**: the wave staging tree held byte-identical copies of later-landed files at the
   freeze; the precise statement is that no landing had been applied to live corpus paths at the freeze.
8. **The S870 chinawriter row**, the six path-present files and the round-74 routed items stay as routed in `## Routed to round 76`; repairs 1-7 are added to it.
