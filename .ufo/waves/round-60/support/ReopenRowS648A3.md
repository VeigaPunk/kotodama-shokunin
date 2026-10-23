HOLDS
S648’s first URL, the pinned capture, and S602’s listed Wayback capture are one PDF (sha256 2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a, 197505 bytes). The anchor quote is verbatim in §I Introduction. Tier B, the narrowed scope, and the access note match the fetch. The entry line’s two clauses are both carried by that one sentence. S648’s source cell lists no Wayback URL of its own.

Axes: byte identity (live / pin / S602 capture); quote location; same page as S602; tier, scope, access vs the fetch; entry-clause carry. No axis failed.

Frozen row at 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626, corpus/SOURCES.md line 603 (worktree row equal):

| S648 | Heeßel, Nils P. 2007, "Pazuzu," Iconography of Deities and Demons in the Ancient Near East (IDD), Electronic Pre-Publication, University of Zurich, last revision 10 December 2007 — https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf (direct plain request, HTTP 200, application/pdf, 197,505 bytes; accessed 2026-10-23) | paper | B | the article's statements that Pazuzu served as antagonist of Lamashtu (identified there as a baby-snatching demon) and was a favourite amulet of pregnant women and young mothers | §I Introduction; locate_in: LOCATED https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf; "P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers." | supersedes S602 — The IDD article describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

S602 line 557, same commit (first URL identical; S602 additionally lists the Wayback capture):

| S602 | Heeßel, Nils P. 2007, "Pazuzu," Iconography of Deities and Demons in the Ancient Near East (IDD), Electronic Pre-Publication, University of Zurich, last revision 10 December 2007 — https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf (direct plain request, HTTP 200, application/pdf, 197,505 bytes); capture https://web.archive.org/web/20210303023053id_/https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf | paper | B | the iconography, materials, forms and protective use of Pazuzu images in the first millennium BCE | §I Introduction: "P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers." | Pazuzu was favoured as an amulet by pregnant women and young mothers because he opposed the baby-snatching demon Lamashtu. | rejected | 2026-10-23 | 2027-10-23 | — |

FIRST_URL_EQUAL True. S648 source-cell URLs: only the live PDF. S602 source-cell URLs: that PDF plus the id_ Wayback URL above.

## Fetch, hash, headers

Command (sandbox /fast/scratch/hyaku/kotodama-r60a3/ReopenRowS648A3, UA Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0):

timeout 120 curl -sS -L -A "$UA" -D live.hdr -o live.pdf -w '...' live URL
timeout 120 curl -sS -L -A "$UA" -D wayback.hdr -o wayback.pdf -w '...' S602's Wayback URL
sha256sum live.pdf wayback.pdf reports/round-60/captures/S648.bin

```
live_http=200 size=197505 ctype=application/pdf url=https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf
wb_http=200 size=197505 ctype=application/pdf url=https://web.archive.org/web/20210303023053id_/https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf
2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a  live.pdf
2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a  wayback.pdf
2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a  .../reports/round-60/captures/S648.bin
197505 live.pdf
197505 wayback.pdf
197505 .../captures/S648.bin
live.pdf b'%PDF-1.6'
wayback.pdf b'%PDF-1.6'
```

cmp live.pdf pin; cmp live.pdf wayback.pdf; cmp wayback.pdf pin → cmp_live_pin:0 cmp_live_wb:0 cmp_wb_pin:0.

Live response headers:

```
HTTP/2 200
date: Fri, 23 Oct 2026 07:52:05 GMT
server: Apache
last-modified: Mon, 10 Dec 2007 06:01:05 GMT
etag: "30381-440e852590a40"
accept-ranges: bytes
content-length: 197505
content-type: application/pdf
```

Wayback response (archive originals; full header also carried memento-datetime Wed, 03 Mar 2021 02:30:53 GMT):

```
HTTP/2 200
content-type: application/pdf
content-length: 197505
x-archive-orig-last-modified: Mon, 10 Dec 2007 06:01:05 GMT
x-archive-orig-etag: "30381-440e852590a40"
x-archive-orig-content-length: 197505
memento-datetime: Wed, 03 Mar 2021 02:30:53 GMT
```

Pin manifest reports/round-60/captures/manifest.json S648: bytes 197505, content_type application/pdf, sha256 2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a, url the live PDF. Match.

## Quote locate

`PYTHONDONTWRITEBYTECODE=1 timeout 180 python3 -B reports/round-60/reopen-quote.py --row S648` (lane root; worktree row equals the frozen row):

```
LOCATED https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf
exit:0
```

Anchor quote vs pypdf 5.4.0 extract of live.pdf: QUOTE_EQ_SENTENCE True, both length 143. Sentence (§I, page 1):

P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers.

The arrow is U+2192. Same sentence is in the saved wayback.pdf extract (TEXT_HAS_SENTENCE True; locate_in True).

Official script on the Wayback URL, three runs, each:

```
NOT_LOCATED https://web.archive.org/web/20210303023053id_/https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf HTTPError
exit:1
```

Wall times 20.71–20.72 s, which is the script’s two 8 s sleeps. A direct urllib replay of the same UA got HTTP 429 (text/html, “suspected abusive bot traffic”), 429 again, then status 200 application/pdf magic %PDF-1.6. The 429 is archive.org throttling, not a different document: the earlier curl body is byte-identical to the pin and contains the quote. S648 does not list this capture; S602 does.

## Tier, scope, access

PDF running header on every page: “Iconography of Deities and Demons: Electronic Pre-Publication N/5 Last Revision: 10 December 2007” and “IDD website: http://www.religionswissenschaft.unizh.ch/idd”. Signed byline after §VI: “Nils P. Heeßel”. Metadata CreationDate/ModDate 2007-12-10; metadata Author is “Jürg Eggler” (Word/Quartz producer), not the signed author. Title on page 1: “Pazuzu”. Section label: “I. Introduction.”

- Tier B. The legend defines B as a strong secondary (expert write-up, survey). This is a five-page IDD lexicon pre-publication synthesizing other literature (it cites HEEßEL 2002 throughout). B fits. It is not a primary ancient text.
- Scope matches the sentence and does not keep S602’s “because”: Pazuzu served as antagonist of Lamashtu, Lamashtu is identified there as a baby-snatching demon, and he was a favourite amulet of pregnant women and young mothers. The scope drops “particularly” and the article “the”; it adds no further claim.
- Access note matches the live fetch: plain GET, HTTP 200, application/pdf, 197505 bytes, date 2026-10-23. “last revision 10 December 2007” matches the PDF header and Last-Modified.

Observed, not a break: the PDF body does not contain the strings “Ancient Near East”, “University”, or “Zurich”. The host uzh.ch and the printed unizh.ch IDD footer are that university’s IDD series; the row’s series expansion is not a quoted span.

## Entry line at 47f27bd0

corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md line 58, the only S648 hit:

- The IDD article describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers (S648).

Page sentence carrying both clauses: “P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers.”

1. The IDD article describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu — CARRIED. “P.” is the article’s abbreviation for Pazuzu (heading “Pazuzu”, and “annû qaqqad Pazuzu ‘this is the head of P.’”). “served particularly as the antagonist of the baby-snatching demon →Lamashtu” is the same predication; the arrow is the lexicon’s cross-reference mark. “The IDD article describes” is the entry’s reporting frame; the PDF states the fact in its own voice under the IDD pre-publication header.
2. and [describes Pazuzu] as a favourite amulet of pregnant women and young mothers — CARRIED by “and was a favourite amulet of pregnant women and young mothers.”

No clause is NOT CARRIED. The line does not restore S602’s causal “because he opposed”.

No tool was installed. Sandbox files only under /fast/scratch/hyaku/kotodama-r60a3/ReopenRowS648A3/. Lane repo was not written except this report.
