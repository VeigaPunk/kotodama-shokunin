# RevEntryBaseFinal — round 73 wave 2 FALSIFY, seat report

Seat: RevEntryBaseFinal (leaf, read-only). Target: landed base entry
`corpus/knowledge/linguistics/conlang-scholarship.md` at lane revision
`0316b8883b4f8d44b8efd720140e7f52f734a102` (HEAD verified; freeze `af65165` present),
checked against `corpus/QUALITY.md` criteria 1–23, `PROVINCE.md`, couples paths,
decision-table-vs-essay, and the README coverage claim.

## Verdict: ADMIT-STANDS

One MINOR finding (stale/mispointed couples gloss). No BLOCKER, no MAJOR.
Claims the entry makes about its two sources (S876 abstract, S877 monograph) were
re-verified against the live sources; every checked quote/paraphrase holds.

---

## Per-criterion sweep (1–23)

| Crit | Scope | Result |
|---|---|---|
| 1 provenance | every factual claim cited; `(to-verify)` markers | PASS — S876/S877 cited per claim; two inline `(to-verify)` markers at lines 24 and 92; no unmarked unverifiable claim found |
| 2 calibration | framework entries name status + reason | PASS — §1 calibration table gives status and why for all six entries (Enguehard, Sidorova & Shuvalova, Henning, Yaguello, Schnapp, Higley), incl. "contested", "not peer-reviewed", "hostile pole" |
| 3 coupling | `- couples:` names connected files | PASS with 1 MINOR — all six couples paths exist; but the `linguistics/naming-systems.md` (§4's naming-language volume rule) gloss mispoints: naming-systems.md §4 is Theonymy and the file contains no "volume rule" anywhere (see Finding 1) |
| 4 usability | decision tables, no essays | PASS — 4 tables (§1 status, §3 taxonomy, §4 volume, §7 languages); per-row design questions; design consequences; no essay prose. 105 lines / 1,986 words vs neighbours (conlang-methodology 158/2,869; naming-systems 136/3,797; phonetics-phonology 325/2,750; historical-linguistics 252/2,551; writing-systems 161/3,608) — shorter than neighbours but table-driven, not prose |
| 5 canon hygiene | no world-canon decision | PASS — header `refuses: canon for any world …`; §9 explicitly hands off to `synthesis/worldbible-integration-contract.md`; no class assignment/depth/history-direction fixed for any setting |
| 6 tier scope | claim-scoped tier A/B/C | PASS — rows S876/S877 tier B; entry reports them as B-scoped (one author's argument; descriptive taxonomy, terminology contested); no tier-A claim made |
| 7 separability | claim-level | N/A for entry bytes (checked by other seats); entry cites only its own claim's rows (S876/S877) |
| 8/9 declared inputs | claim-level receipts | N/A here; entry-level `check-cited-lines.py` run below |
| 10 opened by ordinary means | no automation/captcha bypass | PASS — fetch lines are plain `curl -A <browser-shaped UA>` GETs; no headless/captcha/paywall bypass in evidence S876/S877 |
| 11 clauses able to fail | claim-level | N/A |
| 12 re-test reject grounds | claim-level Gate | N/A here (Gate rows S894/S910 carry verbatim UA/status/bytes records, checked by others) |
| 13 unreachable handled pre-data | claim-level | N/A (S894 ruled via 429 + CDX 0, pre-data) |
| 14 judged object frozen | packet adjudication | N/A (no blind packet for this entry) |
| 15 one-id-per-line | lint | PASS — `python3 -B tools/check-cited-lines.py` on the entry: `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 (also on the amend file). Tables carry no S-ids |
| 16 bounded fetches/body-scoped quotes | fetch budget + quote source | PASS — evidence quotes are abstract body (S876) and PDF body text (S877); not caption/alt/gallery |
| 17 receipts pin revision | claim-level | N/A |
| 18 anchors resolvable | live + same-page capture, quote findable | PASS — S876/S877 rows name live URL + Wayback capture, anchor quote findable in the capture's body (evidence files quote the same span; S877 capture 20260208005339). S879 (amend) is live-leg-only by design, documented in lesson (CDX 0; SPN shell lacks span) — not in this base entry |
| 19 receipt placement | claim-level | N/A |
| 20 trend verdicts | claim-level | N/A |
| 21 "no capture" ruling probes canonical slug | Gate rejects | N/A here (no no-capture ruling in the base entry; S879's ruling is in the amend/lesson) |
| 22 wall/UA binding | Gate records | N/A for adopted rows (no wall); evidence still records UA/status/bytes per fetch |
| 23 counter selftest receipts | claim-level | N/A (telemetry has selftest.txt/-r2/-r3, red-before-r3.txt) |

## PROVINCE.md

PASS — entry sits in `corpus/knowledge/linguistics` (owned partition); domain is
linguistic-cultural worldbuilding. Refuses match: it decides no world's canon
(lore owns canon), makes no real-world rights/attribution rulings (it reports
what the sources say, incl. Yaguello's hostile framing, Schnapp/Higley
positions), touches no game mechanics, no chousa/web-publishing/kotoba craft.
§9 terminates at the worldbible handoff contract.

## Source re-verification (the reproducing commands)

All S877 checks re-run by me on a fresh live fetch (recorded below), text via
`pdftotext -enc UTF-8`.

Fetch records (this seat, 2026-10-25):
- `curl -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` → HTTP 200, 1,055,723 B, sha256 `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` (identical to evidence S877 bytes/sha) — no wall.
- `curl` same UA `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` → HTTP 200, 30,289 B (identical to evidence S876), line 267 (1-indexed) of served HTML = the Abstract paragraph start; keywords list includes Constructed languages, Linguistic Analysis, Linguistics Teaching, Method-Oriented Teaching.

Verbatim hits (grep patterns on extracted text):
- §5 modality: `Эти языки и их создатели не «должны», а «могут».` — found verbatim.
- §5 axes: `Вспомогательные языки призваны а) стремиться к охвату как можно большего числа пользователей; б) … отражать … действительность … образ мыслей людей Земли; в) выполнять (в идеале) требование равной структурной простоты`; `Вымышленные языки, в отличие от вспомогательных: а) не претендуют на широкий круг пользователей; б) призваны передавать картину мира, принципиально отличную от привычной нам; в) не связаны требованиями структурной простоты`.
- §5 manifesto: `неприемлем такой жанр, как меморандум или манифест, указывающий другим, по каким принципам должен строиться «правильный» ВЯ … предложить им набор возможностей`.
- §5 poetic function: `поэтическая функция языка, по Р.О. Якобсону, связанная с «вниманием к сообщению ради самого сообщения»`.
- §6: `первичность описания языка` (line 209) + `Пока автор ВЯ не напишет в грамматике, что … есть частица da или пассивный залог … в этом ВЯ нет ни частицы da, ни пассивного залога`; `описывают то, что уже существует, проектирование подразумевает создание объекта` (lines 213–214); `прерывистый, «скачкообразный» процесс … сознательном внесении изменений автором или пользователями языка (с санкции автора) … добавление новых слов или новых грамматических правил, снятие фонотактических ограничений или добавление морфонологического процесса`; `Естественный язык развивается в одном хронологическом направлении – из прошлого в будущее. А конструктор ВЯ может идти … в прошлое … восстанавливая древние стадии развития языка, якобы предшествовавшие первоначально придуманной системе, так и в будущее, моделируя последующее развитие … «наличные ресурсы» можно в любой момент изменить, отредактировать, если они мешают` (line 875).
- §3 taxonomy (printed pp. 11–12): `1. Auxlangs. Вспомогательные языки … эсперанто, идо, ложбан`; `2.1. Artlangs. Фантастические языки, придуманные авторами литературных и кинематографических произведений, а также компьютерных игр`; `2.1.1 … язык D'ni из мира компьютерной игры «Myst»` (book spells D'ni in Latin); `2.1.2 … «функционирующие» или просто упоминающиеся только в пределах соответствующего художественного произведения`; `2.2. Рersonal languages … «авторскими языками» … Основной средой бытования авторских языков является Интернет`; `«языками-набросками» … зародышевой стадии … частичной ревизии естественных языков`; `ни у ученых-лингвистов, ни в среде конлангеров нет терминологического единства`.
- §3 rival classifications: Rosenfelder `критериями структуры (structure) и назначения (purpose)`; Harrison `классификация Ричарда Харрисона … противопоставление априорности/апостериорности` with tradition `восходящей к работам Г. Мока, но еще больше к знаменитым трудам Л. Кутюра и Л. Ло`; Capuzzo `потенциальное использование языка и потенциальные пользователи языка — использован Роберто Капуззо (Roberto Capuzzo)`; HK composite index `http://web.hku.hk/~antonioc/conLang/class.htm … каждый язык получает буквенно-цифровое обозначение плюс характеристику по порядку компонентов – SVO`.
- §4 volume rule: `Для жаргона достаточно горсточки слов, передающих «вкус другой культуры», и правил образования множественного числа`; `Для «языка имен собственных» … не требуется особой грамматики`; `Для языка, который должен обслуживать реальную коммуникацию или художественную литературу, нужно гораздо большее`.
- §7: Tolkien `почти двух десятков языков своего фантастического мира — Арды`; `на двух основных эльфийских языках – Квенья и Синдарине – имеется обширный корпус поэтических произведений … молитва «Отче наш»`; `горсточки собственных и нарицательных имен и зачатки грамматики`; Klingon `Марком Окрандом на основе исчезнувших языков американских индейцев, при этом с установкой на максимальное отличие от языков Земли … OVS … нет категории времени, нет рода, нет прилагательных; … оригинальная система письма`; `С 1992 года в США существует Институт клингонского языка … «HolQeD» … ISSN 1061-2327 … ряд диссертаций`; D'ni `Ричардом А. Ватсоном … поклонники … принимают допущение, что язык уже существует в готовом виде, однако открывается им по частям … под руководством самого создателя языка Ватсона … расшифровывая имеющиеся надписи`; standing `обусловлено не исключительной популярностью «Мист» … а тем статусом, который авторы серии придали языковому компоненту … лингвистической «интриге»`; father `Толкин как вдохновитель движения конлангеров … многочисленные попытки конструирования языков в художественной литературе известны и до Дж. Р. Толкина, «отцом» движения … все-таки следует считать его`.
- §8: `работы, серьезно трактующие проблему вымышленных языков, исчисляются единицами`; Yaguello `В 1985 г. … «Лингвистические лунатики» (английский перевод — «Lunatic Lovers of Language …», translated by Catherine Slater, 1991, London) … «дилетантами, влюбленными в язык …» … настаивает на патологическом характере лингвоконструирования`; Schnapp `он называет конлангеров «филологами воображаемых миров», хотя и настаивает … изобретение языков – занятие инфантильное, что любой вымышленный язык всегда беднее естественного`; Higley `конланги – это действительно модели, артефакты … Никто не плавает на модели парусника. Никто не думает и не говорит на конланге, хотя с конланга и на конланг можно переводить … Возражая Шнаппу и поддерживая Хеннинга` (book names her article «Аудитория, углоссия и конланг», cites [Higley 2000]; venue not given — the entry's `(to-verify)` marker is appropriate); counters `в 1999 году насчитывало около 20 000 членов … langmaker.com – включает около 1 500 конлангов`; `773 представленных в мировой сети языка, у которых указаны даты создания (по состоянию на 28 июля 2005 года)`.
- §2 (S876): abstract (page line 267) contains both quoted sentences verbatim; keywords include the four the entry lists. (Matches evidence S876.)

Base-revision ground claims re-derived:
- `git show 8841ad3b896a0227674fa0725b818c999118046f:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 799; S876 at base → 0; fragments ojs/philol/rudn/cyberleninka/sanders at base → 0; `conlang-scholarship*` absent at base (only conlang-methodology.md, conlang-blueprint-template.md).
- README coverage claim: `corpus/README.md` holds no conlang-research ground before the round-73 footer (only craft-method entries: conlang-methodology, gesture-co-speech-pointing, sign-languages, speech-surrogates, conlang-blueprint-template, era-language-staging). `conlang-methodology.md` cites Rosenfelder (6), Peterson (5), Okrent (2), Higley (2), WALS (8), PHOIBLE (7), APiCS (4) — no research-venue row.
- Body size leg: 1,986 words ≥ base minimum knowledge entry (478 words) — satisfied.

## Findings

1. **MINOR — couples gloss mispoints (§3 / line 11).** `- couples:` says
   `` `linguistics/naming-systems.md` (§4's naming-language volume rule) ``.
   `naming-systems.md` §4 is "Theonymy: names of gods"; grep for
   volume/grammar/enough/how-much/minimum over the whole file returns nothing
   resembling a "naming-language volume rule" (only an Inuit grief-management
   grammar note). The entry body's use (line 64: "Read that rule against
   `linguistics/naming-systems.md`") is acceptable in spirit — the volume rule
   is for naming languages and naming-systems is the names file — but the
   section pointer in the header is false. Fix: drop "§4's" or re-gloss
   (e.g. "the names file this entry's naming row bears on"). Not a path break
   (file exists). Criterion 3.
2. Observation (no action): S879 (amend) is live-leg-only with no same-page
   capture; fully documented in `corpus/lessons/round-73.md` (CDX 0 on the
   canonical slug; SPN shell 23443 B lacks the span; deliberately not named
   per QUALITY 18). Not part of this base entry; the live URL serves the quote
   to a re-opener, so no 18-rejection applies.

## What I could NOT check

- The amend entry's body quotes (S878/S879/S880) beyond the evidence captures'
  context windows and the Gate rows (not in my item; I only ran the lint on
  it, 0 findings).
- Whether the served monograph PDF byte-for-byte equals the printed 2006 book
  (ISBN 5-98789-005-5); I verified only what the served PDF contains, and the
  evidence sha matched my fetch exactly.
- The line-267 claim under the original serving conditions (line numbering is
  server-HTML-dependent); my fresh fetch shows the abstract starting at line
  267 in the current served HTML.
- Counter-run legs (ROWS/REPOINTED/CITEDLINES/GATE/…) at lands — those are
  other seats' items; I only ran `check-cited-lines.py` directly on the two
  entry files, as instructed.
- The Gate reject rows' probed URLs (S869/S894/S910) were not re-probed by me.

## Tooling record

- `curl/8.7.1` (system) — two fetches, UA recorded above; matches evidence
  bytes + sha256 for both S876 (30,289 B) and S877 (1,055,723 B,
  e512a20d…).
- `pdftotext` (poppler, system) with `-enc UTF-8` and `-layout`.
- `python3 -B tools/check-cited-lines.py` — 0 findings, exit 0, both files.
- No installs performed (operator rule consulted; nothing needed). PACMAN not
  used.
