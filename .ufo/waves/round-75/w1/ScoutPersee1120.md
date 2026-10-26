# ScoutPersee1120 — Todorov / Persée S902

## Finding

**Verdict: ADMIT (proposed lane row S886).** The staged amendment does not actually quote a sentence from Todorov: it anchors the heading `§La Déformation temporelle, p. 139` and paraphrases the argument as “temporality as the decisive axis, with temporal deformation as what distinguishes discourse from history.” The heading `La Déformation temporelle` and the supporting passage are both on printed p. 139. The paraphrase is supported there: Todorov says the Russian formalists regarded temporal deformation as the sole feature distinguishing discourse from history, and put it at the centre of their research. The primary page-level transcription opened by an ordinary public request and serves the text directly. The separate PDF request returned an altcha wall; it was not passed or bypassed and is not used as evidence.

**Staged text inspected:** `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` (read-only source tree). Its opening `source:` line names S902 and `§La Déformation temporelle, p. 139`; the body sentence is a paraphrase, not a verbatim quote. `git show f556d1049fe651d3d63975600b13acd9fb686f15:corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` returned `fatal: path ... does not exist in ...`; that staged amendment is not present at the lane base. The read-only shokuknow file is the staged text actually checked.

## Fetch record and exact commands

All HTTP requests used this exact UA: `Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0`.

Notice request:

```sh
curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -o notice.html -w 'HTTP %{http_code} bytes=%{size_download} url=%{url_effective}\n' 'https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120'
sha256sum notice.html
```

Raw output:

```text
HTTP 200 bytes=109368 url=https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120
aa9eea626f3ac7a7e797b879e3d840796aa14705c7b564b7e0fbc24415ad6592  notice.html
```

The notice's raw HTML exposed the page-level URL shape in `data-content-url`: `/doc/page/<article-slug>/<page-slug>`. It also says `DC.rights=free`, names Tzvetan Todorov, and gives article pagination 125–151. For printed p. 139, the discovered URL is `https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1120/comm_0588-8018_1966_num_8_1_T1_0139_0000`.

Page transcription request:

```sh
curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -o page139.trans.html -w 'HTTP %{http_code} bytes=%{size_download}\n' 'https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1120/comm_0588-8018_1966_num_8_1_T1_0139_0000'
sha256sum page139.trans.html
```

Raw output:

```text
HTTP 200 bytes=3939
16992c94b5e8b314afc2fb8c4ccc297cdc3199855d6fff68f518006b4e17d724  page139.trans.html
```

The fetched body has `alt="Page 139"`, a `<div class="text" itemprop="articleBody">` transcription, and ends with printed page number 139. The exact relevant transcription is: `La Déformation temporelle. Les formalistes russes voyaient dans la déformation temporelle le seul trait du discours qui le distingue de l'histoire; c'est pourquoi ils mettaient celle-là au centre de leurs recherches.`

PDF attempt (not relied on):

```sh
curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -o article.pdf -w 'HTTP %{http_code} bytes=%{size_download} content-type=%{content_type}\n' 'https://www.persee.fr/docAsPDF/comm_0588-8018_1966_num_8_1_1120.pdf'
sha256sum article.pdf
```

Raw output:

```text
HTTP 403 bytes=294 content-type=text/html; charset=UTF-8
4768c2bbb4f164a9106eb4023efe437db2edfd0a6f5309b1d4928391f541ff5f  article.pdf
```

Raw response body: `<!DOCTYPE html> <html><body><div id="announcement-page"><h1 class="title">This resource is protected by altcha</h1><p>Please visit <a href="https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120">the document page</a> to view its content or download the PDF version</p></div></body></html>`.

## Located replacement quote(s)

Best concise replacement: **“voyaient dans la déformation temporelle le seul trait du discours”** — printed p. 139, under `La Déformation temporelle`; 10 whitespace tokens, 65 characters. This contiguous quote explicitly includes the deformation concept and supports the paraphrase.

Alternative: **“le seul trait du discours qui le distingue de l'histoire”** — same p. 139 sentence; 10 whitespace tokens, 56 characters. It is verbatim and within both limits, though less independently descriptive. The longer contiguous quote `la déformation temporelle le seul trait du discours qui le distingue de l'histoire` has 13 whitespace tokens and 82 characters, so it exceeds an 80-character Gate ceiling and should not be used as the Gate quote. Counts were computed on the NFKC-normalized quote strings; location was checked against NFKC-normalized transcription with whitespace folded.

## Proposed registry row

Schema: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`

| S886 | https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | original article | A | Todorov's temporal deformation as a distinction between discourse and history in this article | p. 139, “voyaient dans la déformation temporelle le seul trait du discours” | Primary-source account of the formalists' temporal-deformation claim and its distinction of discourse from history | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md |

**Tier A:** this is Todorov's original article, a primary source for the narrowly scoped claim, satisfying the lane's A definition in `corpus/SOURCES.md` (original paper). This is not a community source. Scope is limited to what the passage says, not to narrative theory in general.

## Wayback CDX canonical-slug probe (QUALITY 21/24)

The exact canonical article slug was queried, not an invented or composed alias. Positive control used the same CDX query shape against the known Persée Barthes article slug. UA for both requests was the Firefox UA stated above.

Todorov command:

```sh
curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -G 'https://web.archive.org/cdx/search/cdx' --data-urlencode 'url=https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120' --data-urlencode 'output=json' --data-urlencode 'filter=statuscode:200' --data-urlencode 'fl=timestamp,original,statuscode,digest' --data-urlencode 'collapse=digest'
```

Probed URL: `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120`
Raw response metadata: HTTP 200, 2245 bytes; SHA-256 `3083d250529510972e0ac083ea46226bc61fde4753d2e92751355165a6358262`.
Raw body begins with the CDX header and contains 17 status-200 captures, latest `20261002231615`:

```text
[["timestamp","original","statuscode","digest"],
["20180603175645","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","KDOGJWFLY5WDZBT3RCD4UPJOQNOBNRKX"],
["20190503133954","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","3KYVVTKXXDXNEBX7LBZ3A35QEUB3SAV5"],
["20261002231615","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","FQXJD3PQRA7ZRFUHQHEPGUJ4NYK5C5K7"]]
```
Complete raw Todorov CDX body:

```text
[["timestamp","original","statuscode","digest"],
["20180603175645","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","KDOGJWFLY5WDZBT3RCD4UPJOQNOBNRKX"],
["20190503133954","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","3KYVVTKXXDXNEBX7LBZ3A35QEUB3SAV5"],
["20201210093851","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","JYFOI4CINEQRXFNFTC5X6N7UIUDSVHFS"],
["20211026102648","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","KIUM7OLMQC3HNOCL6WYW53OSQERMHE7Y"],
["20220207193648","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","JDWZMTYZRSKSEZWANR5Z3WIDYQRXMRLB"],
["20220303033915","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","HPNCVADM6HGQOAHZYRTXZ56J7GRNCQA5"],
["20220630214656","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","TWC5AVWAILXXHSHMH67WWVP4NDQU3I7T"],
["20230605015236","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","CNYU5RVD6MCTEGO3FKMK6JCMHF4JQFQW"],
["20230605015239","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","NBRXNJNUPCZ2EIUTV24VAACJXXO7W6RV"],
["20231202152703","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","RW6CEZGKZJ3AHFBDHVTXQXNIMJRBZGHD"],
["20231202152816","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","SRNMUAZNWEQC3HYADMK5PPWYGEWB7QLC"],
["20240304155200","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","NOWR7EYNB3ZP7S6IR6UZPQRZ7YDIK37O"],
["20240304155203","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","5UESKDKLD6EPGCYXLB5BCTRY4KQ4V74Y"],
["20240528093533","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","55WTWMY3V34DE7NIEGEJ42F32II6Y3TQ"],
["20240528093541","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","YNBWFU6TCBEQERQZQRHLCUMTTWJBANVD"],
["20241216142242","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","AK36I63JLKHFVS4POZB75I3VDZJ22QUQ"],
["20251108180909","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","EAJJMCUXVWFUFPTRGFNAXAWR6GOIJEC7"],
["20261002231615","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120","200","FQXJD3PQRA7ZRFUHQHEPGUJ4NYK5C5K7"]]
```

Positive-control command (same query parameters):

```sh
curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -G 'https://web.archive.org/cdx/search/cdx' --data-urlencode 'url=https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113' --data-urlencode 'output=json' --data-urlencode 'filter=statuscode:200' --data-urlencode 'fl=timestamp,original,statuscode,digest' --data-urlencode 'collapse=digest'
```

Positive-control URL: `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`
Raw response metadata: HTTP 200, 4439 bytes; SHA-256 `ac865aa3afd6517595e63a95945e5fdd05645fa5d5571bc34c6225499d097c18`. Its raw JSON likewise has the CDX header and status-200 capture rows (latest returned `20261005135926`). The positive control succeeded; the canonical Todorov slug has captures, so there is no “no capture” ruling. No front-door DOI/identifier URL was used as the source URL, so no redirect-target inference is made.

Complete raw positive-control CDX body:

```text
[["timestamp","original","statuscode","digest"],
["20170301225114","http://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","VL44NXFEOCPALP7EWASI5JMZQKMLDBWZ"],
["20171230195425","http://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","PFPCRYAR5K7WMLYV3SLNGIUWSPSSD3VG"],
["20190503112608","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","YGEFFYZERARB6LTVV3QINHXIJMUS3J34"],
["20210226002013","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","O2ISPL5ZKVMSVATHNBFQWAXQLDUIWJJA"],
["20210304172212","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","ZRHNFU3PKVXCEYJSDKMNBNLTWLQOI2PS"],
["20210606043144","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","4T5EN5WZSQ4Q4OR5I3KFXIQCSR2HFQQU"],
["20211011184908","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","L4S3GS6EN254WERAPMBIT2G6AFPWFTKR"],
["20211113145233","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","SFIULZC6MF7TKZ6H3OGR5DQBZCOM6BPI"],
["20220120144700","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","JNDUGAHJMLLRZ4UNRZPJ2LMPYTFYTQFQ"],
["20220120201528","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","SGVRC5U76WV6JXYXNYHNYCOTCAGXD5UV"],
["20220121031434","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","N4G6OAHZFKQSHTYPFCKIYXJEHEOOYQHI"],
["20220121112913","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","P7J34A2E3OLBJEI4KCMDJHTEXJMWK2Z4"],
["20220305091310","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","NCXQY7CCIPZCR7KKMVP36GKA73ERXDQK"],
["20220427080544","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","CJHAUII2GVE67BRSWZZR6RUMDU3M7LG5"],
["20220618070848","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","ZDY5BXBBR5OXX3R7H4SMX4YR6CTHM6PB"],
["20220624045330","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","O7N22GLL6HRO6LKAUE5XU7CNC3EICLG6"],
["20220830194530","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","WPN2XDFDC35DGGORKJS6MTHREKMWLX55"],
["20220930133724","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","GFKJ7S5TXSEGWEDLLVQIDE2HHJAZNLDP"],
["20221018013609","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","VQ2UXL7JGJBLH5XPYYJNAPEMRY2ELNXH"],
["20230118073138","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","L3SD6AHHFDMEG6S5S6SRZTSCWXJGNBFO"],
["20240101071223","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","37XPOIS2DDWPWJADG6MI3VAIDNYAGKD2"],
["20240228233148","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","OQY3INC2XOPZS75JKLKJFFUP6CPSWF5V"],
["20240518044732","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","LYKPY4SV5HQSEBO7UFU3ZRD2BLUXJF5F"],
["20241204094204","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","APOH2FILR6C5GKR64CP3F4ZBRHWW4S6J"],
["20250623100213","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","LXPFP4R56HU2SW3GGYSYFQ7UCJU2SV5X"],
["20250705083722","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","WFBD5NQAYQF7WM7XRWCG4RDDOAT3ZMKJ"],
["20251123103450","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","73AJUD2CRSTYVY2IH7PNHRVIIZIKRAHL"],
["20260129123534","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","YQQMT3UY3VPG7Q33D75WM63J5JJZ7WZJ"],
["20260405140111","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","RHKOF5EKBXZWIGANOSTCXQLUUCYZ226O"],
["20260518224813","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","7P4F2JHGIVZDBJ6UE5SRJ77SOLBM24DZ"],
["20260519011834","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","HX3B4GANWXZRVKGKLF4JUM4YBEEMFNT6"],
["20260622185056","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","JQBCC6ZWR2SZHGY57WDX5QU2BYD6SSPS"],
["20260724175910","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","TV4C73VFAZYED5JIBG3TO6AEILUY7J4Y"],
["20260831165946","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","NJP7ZS6XTA6CNNBNY2PFGSM4YABJBTER"],
["20261004024132","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","RIGWXDUIVZJSUXZBI7Z3FV6QIZMPDY2F"],
["20261005135926","https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","200","NBTCSVRJHODGQV2KAGGK4MISZ3EPQO7T"]]
```

## Flip condition

Keep ADMIT while the ordinary page-level text remains available and the page-139 anchor remains locatable. Flip to **REFUSE** if re-opening the public page transcription cannot reproduce the cited p. 139 passage or if its content contradicts the scoped paraphrase; if access is only possible by passing a challenge, classify the source as unopened rather than treating the PDF response as evidence.
