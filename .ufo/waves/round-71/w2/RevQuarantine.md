# RevQuarantine — round 71 wave 2 (falsify seat, read-only)

Seat: `L1Kotodama71.RevQuarantine`. Target: `reports/round-71/telemetry/quarantine-verdicts.md`
(sha256 `ad3f05f6…bf4e`, landed in `1d1b432`), its wave-1 evidence
(`.ufo/waves/round-71/w1/ScoutQuarantineFetch{1,2,3}.md`, `RevQuarantineCrossCheck.md`),
the Ca counter leg (`reports/round-71/accept-ca.py`) and the frozen Ca counting command.
Lane HEAD at review: `ccadb59`. Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
(sha256 `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833`). No tools installed.

## Verdict on the four requested checks

| Check | Result |
|---|---|
| Register slice awk yields 21 ids | **PASS** — 21 rows (18 `payload-absent` + 3 unreachable) |
| Table id set == slice id set (bijection, no dupes) | **PASS** — `diff` empty, 21 unique |
| Label counts PRESENT 10 / REFUSED 6 / UNVERIFIABLE 5 | **PASS as filed**, **FAIL on re-derivation**: S816 and S778 are mislabeled; the re-derived tally is **PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4** |
| Every PRESENT row cites a fetch report with a located span | **FAIL** — S816 (the cited "located" span is not in the served bytes) and S824 (the span was located in a search-engine result, not in the fetched bytes) |

Commands (lane root, register path as `R`):

```sh
awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $3, $4, $5}' "$R" > /tmp/rq_awk.txt
wc -l < /tmp/rq_awk.txt                                   # 21
rg -o 'S[0-9]+' /tmp/rq_awk.txt | sort -u > /tmp/rq_reg_ids.txt   # 21
awk -F'|' '$2 ~ /^ *S[0-9]+ *$/ {gsub(/ /,"",$2); gsub(/ /,"",$3); print $2, $3}' \
  reports/round-71/telemetry/quarantine-verdicts.md > /tmp/rq_tab.txt
awk '{print $1}' /tmp/rq_tab.txt | sort | uniq -d        # (empty)
awk '{print $1}' /tmp/rq_tab.txt | sort -u | diff /tmp/rq_reg_ids.txt - && echo IDSET_EQUAL
awk '{print $2}' /tmp/rq_tab.txt | sort | uniq -c         # 10 PRESENT / 6 REFUSED / 5 UNVERIFIABLE
```

## Findings by severity

### HIGH-1 — S816 is a false PRESENT: the "located" span does not exist on the cited page

- Register quote: `这个我肯定考虑过。我自己就是资深读者…` at
  `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html`.
- ScoutQuarantineFetch2 claims an interviewer answer by 乌贼:
  `这个我肯定考虑过。我自己就是资深读者，作为读者，我对不同的小说有不同的容忍度…`.
- The committed capture `.ufo/waves/round-71/assimilation/fetches/s816.html`
  (sha256 `a3b6640c…d5c`) is **byte-identical** to my live re-fetch on 2026-10-25
  (HTTP 200, 48536 B, UTF-8, title `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”`).
  The article is served whole (empty `zdfy` pagination div; `-2/-3/-4.html` return 404).
- After stripping tags, the 8106-character body has **0** hits for `考虑过`, `资深`, `肯定`, `容忍度`,
  `作为读者`, `我自己就是` and `不同的小说`. `考虑` occurs only in the title and in `再考虑怎么升级`.
- Round 68 also refused it: `.ufo/waves/round-68/assimilation/quarantine-handcheck.json` S816 `found: None`.
- **Correct verdict: REFUSED.** The scout's extended "quote" is not in any served bytes. This is the
  "PRESENT without locating the quote" fake that `CritQuarantineDesign.md` §4 (Fake 2) predicted.

```sh
curl -sSL -A "$UA" -o /tmp/rq_live_s816 https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
sha256sum /tmp/rq_live_s816 .ufo/waves/round-71/assimilation/fetches/s816.html   # identical
python3 -c "import re,html;t=open('/tmp/rq_live_s816').read();b=re.sub(r'\s+','',html.unescape(re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>','',t,flags=re.S)));print([ (k,b.count(k)) for k in ('考虑过','资深','肯定','容忍度')])"
# [('考虑过', 0), ('资深', 0), ('肯定', 0), ('容忍度', 0)]
```

### HIGH-2 — S778 is a false UNVERIFIABLE: both quoted spans are on the cited page

- The table says "live URL resolves to calendar-room feed, not the quoted passage". In fact
  `https://eco.mtk.nao.ac.jp/koyomi/` returns HTTP 200, 10291 B, and declares `charset=EUC-JP`.
  Its title `国立天文台 天文情報センター 暦計算室` is the page's real title, not a feed alternate.
- Decoded as EUC-JP, the NFKC/whitespace-folded body contains both register spans:
  `暦要項は国立天文台で計算した翌年の暦をまとめたものです（官報より転載）。` (FOUND @768) and
  `暦要項・暦象年表について知りたい` (FOUND @749).
- When decoded as UTF-8, the same bytes give mojibake and 0 hits, which most likely explains the
  scout's misread [INFERENCE].
- The table's own legend makes UNVERIFIABLE impossible here: the source fetched cleanly, so the row
  can only be PRESENT or REFUSED. Round 68 recorded PRESENT (handcheck `found` = the span).
- **Correct verdict: PRESENT.**

```sh
curl -sSL -A "$UA" -o /tmp/rq_live_s778 https://eco.mtk.nao.ac.jp/koyomi/   # 200 text/html 10291
python3 -c "import re,html,unicodedata as u;t=open('/tmp/rq_live_s778','rb').read().decode('euc_jp');b=re.sub(r'\s+','',u.normalize('NFKC',html.unescape(re.sub(r'<[^>]+>','',t))));print(b.find(u.normalize('NFKC','暦要項は国立天文台で計算した翌年の暦をまとめたものです（官報より転載）。')))"   # 768
```

### HIGH-3 — `accept-ca.py` QUARANTINE leg does not check the slice; three mutations pass

`accept-ca.py` defines `SLICE_IDS = None  # derived from the register row shape below`, but nothing
ever derives or reads it. Its docstring says the leg checks "exactly the 21 slice ids", but the leg
only tests `len(rows)==21`, that the 21 ids are unique, and that each label is in VERDICTS. It never
reads the register. In a fresh clone (`git clone --no-hardlinks`, HEAD `ccadb59`), all three of these
mutations print `LEG PASS QUARANTINE` and `ACCEPT-CA-71: PASS`:

| Mutation | Result |
|---|---|
| M1 — rename `S776` to non-slice `S999` | PASS (bijection not enforced) |
| M2 — relabel all 21 rows UNVERIFIABLE (the no-fetch dodge) | PASS (no class admissibility) |
| M3 — blank every PRESENT note to `x` | PASS (no evidence join) |

None of the three guards that wave-1 `CritQuarantineDesign.md` §4/§6 proposed was implemented
(bijection against the register, class admissibility, evidence join). The receipt
`reports/round-71/telemetry/measures-ca.txt:14` reports `labels-ok`, which is true but cannot catch
HIGH-1 or HIGH-2.

```sh
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/rq-mut/lane && cd /tmp/rq-mut/lane
sed -i 's/^| S776 |/| S999 |/' reports/round-71/telemetry/quarantine-verdicts.md && python3 -B reports/round-71/accept-ca.py --root . | tail -3
```

### MEDIUM-1 — The frozen Ca counting command prints 0 for the quarantine leg, not 21

The quarantine leg of the `claims.json` `counting_command`
`awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}' reports/round-71/telemetry/quarantine-verdicts.md`
prints **0** against target "21". The rows start with `|`, so `$1` is empty. The cells are also
space-padded, so `^…$` never matches. With trimmed `$2`/`$3` the count is 21.

The receipt `measures-ca.txt` shows the Python counter's output, not the frozen counting command.
The frozen command's own kill rule is therefore never exercised, and it would report the claim as
failing. The command shown in `CritQuarantineDesign.md` (`awk -F'|' 'NR>1 {print $1}' … | wc -l`)
prints 37, so it is not a valid counter either.

### MEDIUM-2 — Five committed round-68 verdicts are reversed without acknowledgement

The round-68 lesson (`corpus/lessons/round-68.md:111-114`, raw evidence in
`.ufo/waves/round-68/assimilation/quarantine-{handcheck,pdf-pass}.json`) verdicted the same 21 rows as
PRESENT 9 / REFUSED 8 / UNVERIFIABLE 4. Neither the round-71 table nor `corpus/lessons/round-71.md`
(§Quarantine, lines 78-86) mentions round 68. The table differs on five rows:

| id | r68 | r71 table | re-derived here | evidence |
|---|---|---|---|---|
| S778 | PRESENT | UNVERIFIABLE | **PRESENT** | HIGH-2 |
| S786 | PRESENT | REFUSED | REFUSED (stricter all-quotes rule) | live `cl101.pdf`: quote 1 found @67; quote 2 absent; the PDF text has 0 CJK characters. r68 counted quote 1 only. r71's rule is defensible, but the legend does not state it. |
| S816 | REFUSED | PRESENT | **REFUSED** | HIGH-1 |
| S825 | REFUSED | PRESENT | PRESENT | live `digital.archives.go.jp/search` (200, 311308 B) serves the era table `元号名称 開始西暦年 令和 2019 選択 平成 1989 選択 …`. The span is located with the interleaved `選択` button labels folded out, so r68's "portal landing" was wrong. |
| S827 | REFUSED | PRESENT | PRESENT (metadata) | The DOI landing `link.springer.com` returns a 3038 B JS "Client Challenge" page with 0 hits. The three strings are in `api.crossref.org/works/10.1007/978-3-032-03277-5_15` (FOUND @1290/@13112/@254). The anchor is the DOI's registered metadata, not the served landing. The scout's phrase "the register's noted Crossref record" is unsupported: the register has no `crossref` mention (`rg -i crossref "$R"` → 0). |

### MEDIUM-3 — S824's PRESENT rests on a search result, not on fetched bytes

`ScoutQuarantineFetch3.md` S824 says its text extraction omitted pages 2–13, and that the span came
from an "independent search result" pointing at the PDF. That is not a span located in a fetch.

The verdict is still substantively right. My live PDF (HTTP 200, 504441 B, 13 pages, Acrobat Paper
Capture OCR layer) reads `…「避祖諒」習俗、輩行字を使って名づける輩行字\n)は中国の広い地域…\n命名の習俗`.
The span is split by a footnote-marker line. The round-68 `quarantine-pdf-pass.json` S824 has
`found: "習俗、輩行字を使って名づける輩行字命名の習俗"`. The evidence chain the table cites is the
defect, not the label.

### LOW-1 — Captures are missing for 6 of 10 PRESENT rows, and the table does not cite the 7 that exist

The `fetches/` captures (s795, s796, s804, s814, s816, s817, s820, each with sha256) arrived in
`ccadb59` ("misroot relocation"), after the table landed in `1d1b432`. The table cites only the prose
fetch reports. PRESENT rows S776, S778, S823, S824, S825 and S827 have no committed capture or
sha256, so no mechanical evidence join is possible for them.

### LOW-2 — The evidence files contradict the table's labels

- `ScoutQuarantineFetch1.md` S786 has the header label **UNVERIFIABLE**, but its body concludes REFUSED.
- `ScoutQuarantineFetch3.md` labels S807, S812 and S835 **PRESENT**. A trailing note then re-reads them
  as UNVERIFIABLE at quote level.

The table's 10/6/5 depends on those silent relabels. The final labels follow the table legend, but
the cited evidence files say otherwise verbatim.

## Span-location receipt (normalized: NFKC, whitespace removed, `，、。／－` and curly quotes folded)

| id | source (bytes) | result |
|---|---|---|
| S776 | live SAMR 200 24142 B | 5/5 fragments FOUND |
| S795 | capture s795.pdf | FOUND across page break (`（五）別号\n\n1\n\n\f（六）法名`) |
| S796 | capture s796.pdf | FOUND in order, interleaved with the two-column layout |
| S804 | capture s804.html | FOUND @1043 (exact after folds) |
| S816 | capture = live, identical sha256 | **ABSENT** (2/18 prefix chars) |
| S820 | capture s820.pdf | FOUND with a quote-mark fold (register `'` vs source `“`) |
| S823 | live chinafolklore 200 41259 B | FOUND @554 |
| S824 | live OCR PDF | FOUND with a footnote-interleave fold (see MEDIUM-3) |
| S825 | live archives 200 311308 B | FOUND with a `選択` interleave fold |
| S827 | Crossref API JSON | 3/3 FOUND; DOI landing is a bot challenge |
| S814 (REFUSED) | capture s814.html | ABSENT (1/30), consistent |
| S817 (REFUSED) | capture s817.html | ABSENT (0/12, 1/25), consistent |
| S778 (UNVERIFIABLE) | live, EUC-JP | **FOUND** @768/@749 (HIGH-2) |

Not re-fetched by this seat: S779, S787 and S792 (REFUSED) and S791 (UNVERIFIABLE). Their labels
agree with round 68, and `ScoutReopenRows` owns S779.

## Re-derived table (net)

PRESENT 10 = S776 S778 S795 S796 S804 S820 S823 S824 S825 S827 ·
REFUSED 7 = S779 S786 S787 S792 S814 S816 S817 ·
UNVERIFIABLE 4 = S791 S807 S812 S835. The lesson's "PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5" and the
`measures-ca.txt:14` tally do not hold as true verdicts.

## Residual risk and verification gaps

- My live fetches are dated 2026-10-25 and are not committed (seat is read-only). Their hashes:
  S778 `63fd256e…33d6`; S816 is identical to the committed capture.
- S827 PRESENT depends on accepting DOI registration metadata as the cited source. That is a policy
  call; the round-68 REFUSED rests on the bot-challenge page.
- S786's verdict depends on the multi-quote rule (all quotes or REFUSED). It is not stated in the
  table legend or the claim.
- No change to adoption: the table says CLOSED, and nothing here argues for opening it.
