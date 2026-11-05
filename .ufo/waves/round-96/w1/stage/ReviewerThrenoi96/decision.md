# ReviewerThrenoi96 — re-decision of the round-95 Thrênoi-to-Moirológia reject (2026-11-05)

Target: "Thrênoi to Moirológia: Female Voices of Solitude, Resistance, and Solidarity",
Andrea Fishman, Oral Tradition 23/2 (2008): 267-295.
Round-95 reject (corpus/lessons/round-95.md line 26): UNREACHABLE, class access — curl exit 28,
connection timed out after 30001 ms, on the PDF, the site root and the issue page; max-time 30, no retry.

## 1. Re-open attempts (plain curl, -L, --max-time 30, default user agent)

Loop: `for i in 1 2 3; do code=$(curl -sS -L --max-time 30 -o "$OUT" -w '%{http_code}' "$U"); rc=$?; bytes=$(stat -c%s "$OUT"); echo attempt$i rc=$rc http=$code bytes=$bytes; [ $rc -eq 0 ] && break; [ $i -lt 3 ] && sleep 20; done` (rc 0).

| URL | attempt | curl rc | HTTP | bytes |
|---|---|---|---|---|
| https://journal.oraltradition.org/issues/23ii/ | 1 | 0 | 200 | 43010 |
| https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf | 1 | 0 | 200 | 302080 |

Both URLs answered on the first attempt; no retries were consumed. (Two earlier tool dispatches of the
same loops failed to start because the scratch cwd did not exist yet — harness start error, no HTTP
request was made by them.) The PDF size 302080 B matches the round-95 closure re-open byte for byte.

Captures (sha256sum, rc 0):
- captures/R1-issue.html — 936d9e1ce9ad608d91efd0559aa45fdd45f979ccedfab3a01e4c18ebc895d6dc (43010 B, HTML)
- captures/R1-article.pdf — 1e53dabf880576270d134fa285914b17c802d62ee84b159a72e535fc3fc5599a (302080 B, PDF)
- pdfinfo: Title "ORAL TRADITION 23.2 - Thrênoi to Moirológia: Female Voices of Solitude, Resistance, and Solidarity", Pages 29, File size 302080 bytes (rc 0). file(1) said "8 page(s)" — wrong; pdfinfo is authoritative and pdftotext's 1497 lines / works-cited ending confirm the whole article.
- Issue page corroborates the article: python3 bytes.count → "07_23.2.pdf" count 1, "Fishman" count 1 (rc 0).

## 2. Text extraction and located quotes

pdftotext (poppler 26.10.0, already installed — no install performed) rc 0 → 83367 B / 1497 lines.
Counts via python3 `data.count(q.encode('utf-8'))` on the extracted text (rc 0).

- Title line (count 1, 7 words): `Thrênoi to Moirológia: Female Voices of Solitude,`
  (the shorter core "Thrênoi to Moirológia" occurs 2× — title plus running head — hence the longer line).
- Q1, antiphonal thrēnoi, author's voice (count 1, 19 words; the line break shown is the extracted text's own):
  `the antiphonal structure and style of lament performance contribute to⏎social bonding among women; they mourn in a fugue.`
- Q2, antiphony, quoting Seremetakis (count 1, 18 words):
  `Antiphonic reciprocity between women in the mourning ritual entails the intensive⏎interpenetration of collective and individual poetic creation`
- Q3, dirge leader, supplementary (count 1, 11 words): `the leader of the dirge (koriféa), twice widowed, asks her audience`

Supporting context in the capture: the modern Greek village `moiroloyístres` (lament singers) are named
in the article's framing; the "ethics of antiphony" chapter of Seremetakis is discussed with page cites;
an ancient-tragedy kommos (antiphonal lament between actor and chorus) is compared point by point with
Maniat antiphonal lament.

## 3. Decisions

(a) Access reason: DID NOT HOLD. The round-95 exit-28 timeout was a transient connection failure, not
unreachability: on 2026-11-05 both URLs answer HTTP 200 on the first attempt within the same 30 s
budget the round-95 probe used. Class confirmed: transient-timeout misread as unreachable (the class
the frozen claims.json frontier_step records).

(b) Content: ADMIT-AS-CANDIDATE, tier A (peer-reviewed journal, publisher-hosted PDF, mined secondary
synthesis with page-cited Seremetakis/Alexiou/Caraveli-Chaves material). The lament entry
(corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md, rows S970-S974) does NOT already
cover it: grep -c -i -E "greek|maniat|maniot|kommos|seremetakis|alexiou|epiros|moirolog|thr[eê]noi|korif"
= 2 (rc 0), both mentions being Seremetakis-truth-claim material reported secondhand inside the S971
(Corsican voceru) discussion (entry lines 90 and 157). The article would add, first-hand: the
professional-leader facet (moiroloyístra, koriféa) for section 3 "The professional mourner", and the
kommos → Maniat moirológia antiphonal continuity for section 4 "Antiphonal lament". Not a duplicate
of S970-S974 (Seto, voceru, keeners, Sima); Greek material currently exists in the entry only as a
footnote-level report through another source.

## 4. Reject reason class vs the bounded row re-opener

Retry rule read from tools/reopen-row.py (no run against the registry): a transient result — HTTP 429,
any 5xx, an expired 30 s per-request wall budget, a connection error — is retried at most 3 attempts
per URL per pass, waiting min(gap, 5) s between attempts (docstring lines 84-92); socket.timeout /
TimeoutError / ConnectionError / URLError all raise TransientFetch (fetch(), lines 488-566; class
TransientFetch line 174); another pass runs after gap seconds only when the pass was not LOCATED and
some URL ended transient, at most --passes passes (default 3, gap 60 s). curl exit 28 (timeout) maps
to TransientFetch, so the round-95 failure would have been retried, not recorded UNREACHABLE.

Would it have returned LOCATED for the PDF URL? NO — but not because of access: with the site answering
200, the verdict for the PDF URL would be ABSENT, because split_content (lines 350-361) treats
non-HTML bodies (application/pdf) as raw decoded text, in which no English anchor quote can match.
LOCATED requires the anchor quote to be visible in an HTML body — e.g. a row anchored on the issue
page (title and author are body-visible there) would come back LOCATED on 2026-11-05. Either way the
UNREACHABLE class was wrong: the re-opener replaces it with a fetched verdict, which is exactly the
QUALITY.md requirement (reject-by-access must pass the re-opener first).

## 5. Nomination (ExecRegistry96 is the only registry writer — not exercised here)

Nominate a future registry row (id after ExecRegistry96's S975-S977; its choice): source
https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf (issue page
https://journal.oraltradition.org/issues/23ii/ as secondary URL), tier A, mined, opened 2026-11-05,
used-by corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md; anchor quotes Q1 and Q2 above
(Q3 optional), capture under reports/round-96/evidence/ per the claim C7 machinery. Flip condition:
if a later full bounded re-open (3 attempts × 3 passes) again times out on all of the row's URLs on a
different day, the reject is reinstated with class access-transient.

## 6. Tooling, bounds

Tools installed: none (pdftotext/pdfinfo poppler 26.10.0 already present; pacman untouched per the
host-wide pause). No git/jj mutation; registry, claims.json, predispatch.py, predispatch-base.txt,
reports/round-95/ untouched; reopen-row.py not executed. Scratch /fast/scratch/hyaku/kotodama-r96/ReviewerThrenoi96/
deleted before yield.
