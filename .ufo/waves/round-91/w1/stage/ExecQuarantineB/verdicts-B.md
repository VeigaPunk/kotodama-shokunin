# verdicts-B — ExecQuarantineB (kotodama round-91 quarantine hand-check)

Fetched 2026-11-05T08:19:51-03:00; one `curl -sS -L --max-time 40` per URL; captures in `caps/<id>.bin`.

| id | class-as-registered | verdict | http | bytes | fragments found/total | reason |
|---|---|---|---|---|---|---|
| S807 | `the cited source could not be fetched, so no quote was checked` | UNVERIFIABLE | 200 | 597992 | 0/0 | Prose row ("could not be fetched"); fetched and reported what the DOI serves. |
| S812 | `the cited source could not be fetched, so no quote was checked` | UNREACHABLE | 429 | 1478 | 0/0 | Prose row ("could not be fetched"); fetched and reported what the DOI serves. |
| S814 | ``payload-absent`` | UNREACHABLE | 403 | 162 | 0/1 | curl rc=0 http=403 bytes=162 type=text/html |
| S816 | ``payload-absent`` | ABSENT | 200 | 48536 | 0/1 | 2xx body served but no fragment found in folded copy (see note / diagnostics) |
| S817 | ``payload-absent`` | ABSENT | 200 | 62604 | 0/1 | 2xx body served but no fragment found in folded copy (see note / diagnostics) |
| S820 | ``payload-absent`` | ABSENT | 200 | 417093 | 0/1 | 2xx body served but no fragment found in folded copy (see note / diagnostics) |
| S823 | ``payload-absent`` | UNREACHABLE | 468 | 14863 | 0/1 | curl rc=0 http=468 bytes=14863 type=text/html |
| S824 | ``payload-absent`` | ABSENT | 200 | 504441 | 0/1 | 2xx body served but no fragment found in folded copy (see note / diagnostics) |
| S825 | ``payload-absent`` | ABSENT | 200 | 311308 | 0/2 | 2xx body served but no fragment found in folded copy (see note / diagnostics) |
| S827 | ``payload-absent`` | LOCATED | 200 | 325782 | 3/3 | every fragment found in the folded copy |
| S835 | `the cited source could not be fetched, so no quote was checked` | UNREACHABLE | 503 | 690 | 0/0 | Prose row ("could not be fetched"); fetched and reported what the record URL serves. |

## Commands run

```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S807.bin -w %{http_code} %{size_download} %{content_type} https://doi.org/10.34158/ONOMA.51/2016/8
```
```
curl -sS -I -L --max-time 40 -o /dev/null -w %{url_effective} %{http_code} https://doi.org/10.34158/ONOMA.51/2016/8
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S812.bin -w %{http_code} %{size_download} %{content_type} https://doi.org/10.1017/cnj.2024.21
```
```
curl -sS -I -L --max-time 40 -o /dev/null -w %{url_effective} %{http_code} https://doi.org/10.1017/cnj.2024.21
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S814.bin -w %{http_code} %{size_download} %{content_type} http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S816.bin -w %{http_code} %{size_download} %{content_type} https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S817.bin -w %{http_code} %{size_download} %{content_type} https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S820.bin -w %{http_code} %{size_download} %{content_type} https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S823.bin -w %{http_code} %{size_download} %{content_type} https://www.chinafolklore.org/web/index.php?NewsID=10867
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S824.bin -w %{http_code} %{size_download} %{content_type} https://ir.library.osaka-u.ac.jp/repo/ouka/all/77834/gbg_018_197.pdf
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S825.bin -w %{http_code} %{size_download} %{content_type} https://www.digital.archives.go.jp/search
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S827.bin -w %{http_code} %{size_download} %{content_type} https://doi.org/10.1007/978-3-032-03277-5_15
```
```
curl -sS -I -L --max-time 40 -o /dev/null -w %{url_effective} %{http_code} https://doi.org/10.1007/978-3-032-03277-5_15
```
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/S835.bin -w %{http_code} %{size_download} %{content_type} https://omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf
```

## Notes (full)

- **S807** (UNVERIFIABLE): prose row (no quote in register cell); served http=200 bytes=597992 type=application/pdf; body text head: '%pdf-1.7 %���� 1 0 obj >] /metadata 353 0 r/viewerpreferences 354 0 r>> endobj 2 0 obj > endobj 3 0 obj >/xobject >/procset[/pdf/text/imageb/imagec/imagei] >>/annots[ 12 0 r 18 0 r 26 0 r] /mediabox[ ' | DOI -I -L final: https://onomajournal.org/wp-content/uploads/2019/09/Onoma-51-08.-Kaluzynska-final-25.08.2019.pdf 200 (rc=0)
- **S812** (UNREACHABLE): curl rc=0 http=429 bytes=1478 type=text/html; charset=utf-8 | DOI -I -L final: https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article 429 (rc=0)
- **S814** (UNREACHABLE): curl rc=0 http=403 bytes=162 type=text/html
- **S816** (ABSENT): 2xx body (48536 B, type=text/html); no fragment in folded copy; folded head: "爱潜水的乌贼:“我先设定世界观,再考虑怎么升级”--网络文学--中国作家网 您在使用一个 旧版本的 浏览器,请 更新你的浏览器 来更好的体验本网站。 (function(){ var bp = document.createelement('script'); var curprotocol = window.loca"
- **S817** (ABSENT): 2xx body (62604 B, type=text/html); no fragment in folded copy; folded head: "爱潜水的乌贼:网络文学不断“升级”的“奥术”--网络文学--中国作家网 您在使用一个 旧版本的 浏览器,请 更新你的浏览器 来更好的体验本网站。 (function(){ var bp = document.createelement('script'); var curprotocol = window.locati"
- **S820** (ABSENT): 2xx body (417093 B, type=application/pdf); no fragment in folded copy; folded head: '%pdf-1.6 %���� 642 0 obj > endobj 659 0 obj >/filter/flatedecode/id[ ]/index[642 30]/info 641 0 r/length 90/prev 416539/root 643 0 r/size 672/type/xref/w[1 3 1]' | PDF text-layer diagnostic (pdftotext): 0/1 fragments found in extracted text (diagnostic only; prescribed pipeline is byte-level)
- **S823** (UNREACHABLE): curl rc=0 http=468 bytes=14863 type=text/html
- **S824** (ABSENT): 2xx body (504441 B, type=application/pdf); no fragment in folded copy; folded head: '%pdf-1.6 %���� 1 0 obj > endobj 2 0 obj > stream x�]�� �0\x10��}�bv�hq\x12ӛ�bi�b\x16�>m\x06)h�����b\x10ܞ��]\x01�q��\x0ed���b#�i�i�($*��^ug jij�v r�.i�c�� �m{�������� %\x1b�~� 쓣�̞w��\x05^m' | PDF text-layer diagnostic (pdftotext): 0/1 fragments found in extracted text (diagnostic only; prescribed pipeline is byte-level)
- **S825** (ABSENT): 2xx body (311308 B, type=text/html;charset=UTF-8); no fragment in folded copy; folded head: "const cookieexpirationdays = 400; window.datalayer = window.datalayer || []; function gtag(){datalayer.push(arguments);} gtag('consent', 'default', { 'ad_user_d"
- **S827** (LOCATED): DOI -I -L final: https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15?error=cookies_not_supported&code=b375910e-d041-4c29-8fa3-07c092f6a0bb 200 (rc=0)
- **S835** (UNREACHABLE): curl rc=0 http=503 bytes=690 type=text/html
