# ScoutQuarantine816817 — item-10 quarantine hand-check, register S816 / S817 (round 74, wave 1)

Read-only seat. Fetched with User-Agent `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
(curl -sSL, 2026-10-25 21:14 local), downloads at `/tmp/ScoutQuarantine816817/` (live16.html, live17.html, h16.txt, h17.txt, quarantine-slice). No tool installed. No Wayback probe was needed (both pages HTTP 200 live).

## 1. Slice (derived with the prompt's awk, prompt lines 517-521) — 21 lines

```
A=.../.ufo/waves/round-74/assimilation ; R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' "$R"
```
Result (21 lines, every line carries an S-id; copy at /tmp/ScoutQuarantine816817/quarantine-slice):
```
 S776   `payload-absent`   S778 …  S779 …  S786 …  S787 …  S791 …  S792 …  S795 …  S796 …  S804 …  S814 …
 S816   `payload-absent`   S817   `payload-absent`   S820 …  S823 …  S824 …  S825 …  S827   (all `payload-absent`, 18 rows)
 S807`   the cited source could not be fetched, so no quote was checked
 S812`   the cited source could not be fetched, so no quote was checked
 S835`   the cited source could not be fetched, so no quote was checked
```
Note the awk prints the 3 prose-class rows with a stray backtick after the id and the prose in column 5 (their register row has an extra backtick column layout) — still 21 lines with S-ids; 18 payload-absent + 3 unreachable-class, matching round 71.

Register rows under test (register lines 129-130, observed):
- S816 | round4 | payload-absent | `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | quote `这个我肯定考虑过。我自己就是资深读者…`
- S817 | round4 | payload-absent | `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | quote `Sowers-Wills's 'Phonology from the inside out…'`

## 2. Fetch results and byte identity (observed)

| URL | HTTP | bytes | sha256 (prefix) | vs committed round-71 capture |
|---|---|---|---|---|
| …/2025/0605/c404024-40494534.html | 200 text/html (Last-Modified Tue, 10 Jun 2025 01:40:55 GMT) | 48536 | a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d | **byte-identical** to `.ufo/waves/round-71/assimilation/fetches/s816.html` (full sha equal; file tracked in base f7104cbc) |
| …/2022/1207/c404024-32582252.html | 200 text/html (Last-Modified Thu, 24 Oct 2024 02:17:46 GMT) | 62604 | 344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659 | **byte-identical** to `…/fetches/s817.html` (full sha equal; tracked in base) |

The round-71 byte-identity claim ("committed capture s816.html byte-identical to live re-fetch") is CONFIRMED, and extends to s817. The round-68 handcheck json (`.ufo/waves/round-68/assimilation/quarantine-handcheck.json`) recorded the same sizes and sha prefixes (48536 `a3b6640ce2b1ca30`, 62604 `344de345cef7f5f9`) — the two pages have been served unchanged across rounds 68, 71 and 74. Also identical to the L1's /tmp/q74 copies (same sizes 48536/62604). Not a dead payload and not a UA wall.

Page identities (title tag, observed): 2025 page = `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”--网络文学--中国作家网`, byline `来源：文汇报 | 邵燕君 谭天 项蕾  2025年06月10日09:01`. 2022 page = `爱潜水的乌贼：网络文学不断“升级”的“奥术”--网络文学--中国作家网`, byline `来源：《青春》 | 李玮 爱潜水的乌贼  2022年12月07日10:07`. Both match the staged row text (S899 / S900 titles, dates, sources).

## 3. Quote search (UTF-8 decoded, `str.count` on the raw bytes' decode; 0 = absent)

| string | 2025 page (register S816 URL) | 2022 page (register S817 URL) |
|---|---|---|
| `这个我肯定考虑过。我自己就是资深读者` (register S816 quote) | **0** | **1** |
| `Sowers` / `Phonology` / `inside out` / `Wills` (register S817 quote) | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| `先做的是世界观` (staged S899 recheck-cell target) | 1 | 0 |
| `非凡特性来自最初造物主` (staged S899 row's cited answer) | 1 | 0 |
| `20章之内慢慢来` (staged S900 recheck-cell target) | 0 | 1 |

## 4. Per-row verdict under the prompt rule (quote absent → refuse the ROW AS STAGED; present → adopt with located anchor)

**Register S816 (staged S899 URL) — REFUSED as staged.** The register row's quote `这个我肯定考虑过。我自己就是资深读者…` is absent from its own URL (2025 page, 0 hits; also consistent with round-68 `found: null` and round-71 RevQuarantine HIGH-1: the round-71 ScoutQuarantineFetch2 PRESENT claim was a false PRESENT and was overturned). Verdict stands.

**Register S817 (staged S900 URL) — REFUSED as staged.** `Sowers-Wills's 'Phonology from the inside out…'` is absent from the 2022 page (0 hits for each of Sowers, Wills, Phonology, inside out). Verdict stands.

### URL↔quote mispairing (confirmed from the register's own adjudication data)
Yes — both REFUSED verdicts are a URL↔quote mispairing, not a dead payload and not a fabricated page:

- Register S816's quote `这个我肯定考虑过。我自己就是资深读者` IS on the page of the OTHER URL: the 2022 article (S817's URL), 1 hit, and it is exactly the quote staged row S900 carries (staged S900's cell 7: `这个我肯定考虑过。我自己就是资深读者…`). So the span is real and genuinely sourced; it was bound to the 2025 URL.
- Register S817's quote is the Sowers-Wills clause, which belongs to neither chinawriter page; it is the clause of the Anderson/Grant/Sanders opening article (lane registry S880, sanders.phonologist.org) — a linguistics document.
- Mechanism (observed, `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/census-adjudication.json`, `still_absent` entries at lines ~1913-1938): campaign id S758 carries `url` = 2025 page but `quote` taken from its `line`'s NEXT row S759 (the 2022-article row, which holds the 这个我肯定考虑过 span); campaign id S759 carries `url` = 2022 page but `quote` taken from S760's row (the Anderson/Grant/Sanders row); both `"binding": "id"`. I.e. the census paired each id's URL with the following row's quote (off-by-one). That is the fabrication class for the REGISTER PAIR as filed (a quote not on its cited page), but the fault sits in the census row binding, not in either source page or in the staged row text itself.
- Consequence for the staged rows themselves: staged S899 (2025 URL) is cited for `非凡特性来自最初造物主` / the build-order answer and staged S900 (2022 URL) for `这个我肯定考虑过…`/`20章` delivery schedule — each pairing is correct against the live bytes (table §3, rows 3-5). I did not inspect the staged rows' recheck-command output beyond the greps above; those greps return 1 for each page as stated (`先做的是世界观` on 2025, `20章之内慢慢来` on 2022).

### Is a FRESH row with a located quote honest? — YES (with conditions)
The rule is "refuse the row as staged; present → adopt with the anchor located". Both pages are live, byte-stable since round 68, carry the key terms, and the real quotes are on the intended URLs. A fresh lane row opened this round (tentative lane ids S883 for the 2025 page, S884 for the 2022 page per the by-document map) is honest provided that:
1. the Gate quote is located on the page it cites (not carried from the register/staged cell without re-checking), the row does not inherit the REFUSED register/staged quote-binding, and the lesson names the refused register ids (S816, S817) and their mispairing as the reason the old rows stay refused while the documents are re-opened by fresh quote;
2. the used-by/Gate text does not claim the register's quote for the wrong URL (the Sowers-Wills clause stays with lane S880; staged S882/philol.msu.ru is lane S877 — not part of this item).

Re-quotes located by this seat (verbatim from the fetched bytes, each 1 whitespace token under `wc -w` because CJK has no spaces; character counts via Python `len`, all ≤25 "words"):

| page | quote | location | wc -w | chars |
|---|---|---|---|---|
| 2025 (S883 candidate) | `整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。` | raw HTML line 215 of the capture; answer of 爱潜水的乌贼 to 项蕾's question `为什么会让人在服用魔药后产生剧烈的痛苦和症状呢？`; 96th non-empty line of the tag-stripped text; page title/heading `“我先设定世界观，再考虑怎么升级”` | 1 | 32 |
| 2025 | `在设定上，非凡特性来自最初造物主，是外来物。` | same paragraph (HTML line 215), first sentence | 1 | 22 |
| 2022 (S884 candidate) | `这个我肯定考虑过。我自己就是资深读者，` | raw HTML line 220; answer of 乌贼 to 李's question about front-loaded world-view (`看来您是很坚定地相信这样的方式是没有问题的…`); 64th non-empty text line | 1 | 19 |
| 2022 | `把它放在前面大概20章之内慢慢来，我觉得是问题不大的。` | same paragraph (HTML line 220), closing sentence — the full sentence `如果开头足够有趣，有钩子，有悬念，那么你把整个世界观和设定逐渐地抛入，把它放在前面大概20章之内慢慢来，我觉得是问题不大的。` (62 chars, 1 token) also verified contiguous | 1 | 27 (short form) |

(`wc -w` on the 32-char sentence printed `1 32` with `-m`; the others were verified by Python `str.split()` = 1 and `len`. The 27-char short form was re-counted by Python `len`/`split` after the first draft said 26.)

Not run: Wayback/CDX probes (not needed — live 200 under the browser UA); no plain-curl UA comparison was run (browser UA returned the full page both times).

## 5. Standing verdicts for all 21 slice rows (round-71 table, `reports/round-71/telemetry/quarantine-verdicts.md`; not re-fetched — S816/S817 re-fetched here)

| register id | round-71 verdict | one-line note |
|---|---|---|
| S776 | PRESENT | SAMR GB/T 33661-2017 record metadata; lane S776 is a different source (id namespace mismatch) |
| S778 | PRESENT | page declares EUC-JP; both spans present when decoded as EUC-JP |
| S779 | REFUSED | NAOJ page is a Japanese calendar announcement; spans absent |
| S786 | REFUSED | Conlanging 101 PDF has quote 1 only; Chinese quote absent (multi-quote rule) |
| S787 | REFUSED | China Writers network-fiction page; span absent |
| S791 | UNVERIFIABLE | registry URL truncated; document unfetchable |
| S792 | REFUSED | quoted slash-joined span absent (round-72 F-1: the four headings ARE present; only the stated reason was wrong) |
| S795 | PRESENT | Obirin PDF ch. II §II names the taxonomy |
| S796 | PRESENT | Kankyo-U PDF discussion paragraph |
| S804 | PRESENT | Kotobank 苗字 entry quote |
| S814 | REFUSED | CSSN Han-Jin names article; classification passage absent |
| S816 | REFUSED | **confirmed this seat**: byte-identical capture; span absent from the 2025 URL (present on the 2022 URL — mispairing) |
| S817 | REFUSED | **confirmed this seat**: Sowers-Wills span absent from the 2022 URL (belongs to lane S880 document) |
| S820 | PRESENT | Onoma PDF §2 quote (curly quotes) |
| S823 | PRESENT | China Folklore article first paragraph |
| S824 | PRESENT | Osaka-U PDF (text extraction partial; round-71 RevQuarantine MEDIUM-3 flagged the located span as search-result-derived) |
| S825 | PRESENT | National Archives era-table page, both fragments (round-68 had REFUSED it as a portal landing) |
| S827 | PRESENT | DOI → Crossref metadata record (landing page itself is a JS challenge; PRESENT rests on registered metadata — a policy call per RevQuarantine) |
| S807 | UNVERIFIABLE | DOI now resolves to open metadata; register gives no quoted span |
| S812 | UNVERIFIABLE | DOI now resolves to metadata/abstract (Sowers-Wills 2024 CJL); no quoted span in register |
| S835 | UNVERIFIABLE | PDF now fetchable; no quoted span in register |

Tally (round-71, re-derived by RevQuarantine): PRESENT 10 (S776 S778 S795 S796 S804 S820 S823 S824 S825 S827) · REFUSED 7 (S779 S786 S787 S792 S814 S816 S817) · UNVERIFIABLE 4 (S791 S807 S812 S835) = 21. Note the round-71 w1 file ScoutQuarantineFetch2 originally filed S816 PRESENT; the committed tally (table) is the corrected REFUSED. Lesson text should cite the table, not the w1 scout file.

Staged↔register↔lane bridging for the lesson (by document): register S816 ↔ staged S899 ↔ candidate lane S883; register S817 ↔ staged S900 ↔ candidate lane S884. Round-72 `## Quarantine` already records "staged REFUSED set (register ids S779, S786, S787, S792, S814, S816, S817 → staged S862, S869, S870, S875, S897, S899, S900, S933) not adoptable" and rejected the worldbuilding amend entry in round 72 for citing S899/S900. The re-open path is a fresh row with a located quote, not a reversal of the REFUSED verdict.

## 6. Residual unknowns
- I did not diff the staged S899/S900 knowledge text against the pages beyond the cited quote cells and recheck greps; the amend file only carries the 「…」 fragment `非凡特性来自最初造物主` in its source header (no verbatim quote sentences).
- The mispairing mechanism is read from `census-adjudication.json` (campaign ids S758/S759, `binding: id`); I did not audit the census tool.
- Live fetch not run under a plain-curl UA; not needed for the verdict.
