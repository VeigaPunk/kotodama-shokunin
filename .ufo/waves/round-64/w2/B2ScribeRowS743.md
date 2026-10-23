# S743 — scoped source report

## Behavior
Akita’s original 2012 paper treats Japanese child-directed verbs as a register-specific construction. Section 2.2 explicitly names the register “child-directed”; the row’s scope is limited to that analysis. Tier A is appropriate because this is the original research paper making the scoped linguistic analysis, published in BLS 38 by the Berkeley Linguistics Society / Linguistic Society of America. It is not evidence for broader child-language acquisition outcomes.

## Gates
- Source access: direct plain-curl fetch returned HTTP 200.
- Archive: a same-PDF capture was available with timestamp `20250628010953` and original URL `https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857` (closest snapshot status 200). The first unencoded availability request returned HTTP 429; the percent-encoded request succeeded.
- Quote locator: the final 10-normalized-word quote returned `LOCATED` twice. An earlier longer quote containing “instantiating” returned `NOT_LOCATED ... quote-absent`; the final quote is a contiguous fragment directly naming the register.
- Row shape: `awk -F'|'` reported 13 fields, i.e. 11 cells plus the two delimiter fields. The final quote has 10 words under the lane locator’s NFKC/non-word normalization (within 8–25). The simple whitespace-token awk subcheck printed 11; the normalized count is 10.
- `ACCEPT-C-64` was not run; no whole-claim pass is asserted.

## Touched surfaces
- Created `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS743/row.txt` with the five required labelled lines.
- Downloaded the source PDF to `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS743/source.pdf`.
- Created this requested report at `.ufo/waves/round-64/w2/B2ScribeRowS743.md`.
- No corpus entry, registry, product code, Git index, or jj state was changed. No tools were installed.

## Out of scope / known limits
This seat supplies only S743’s source row and its scoped finding. It does not establish that the row is integrated or that claim C passes its full acceptance predicate. No test/build/lint or full acceptance script was run. The initial 429 and initial long-quote locator failure are recorded above.

## Provenance and commands
Search query used: `Japanese "ikujigo" register infant-directed speech linguistic paper`. The selected publisher landing page identifies Kimi Akita, title, 2012 publication date, DOI `10.3765/bls.v38i0.3267`, and pages 3–17; the downloaded paper’s §2.2 is headed “Child-Directed Verbs.”

Source fetch command:
```sh
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS743 && curl -sL --max-time 60 -w '\nHTTP_STATUS=%{http_code}\nEFFECTIVE_URL=%{url_effective}\n' -o /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS743/source.pdf 'https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857'
```
Outcome: `HTTP_STATUS=200`; effective URL was the requested PDF URL.

Archive commands:
```sh
curl -s 'https://archive.org/wayback/available?url=https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857'
curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fjournals.linguisticsociety.org%2Fproceedings%2Findex.php%2FBLS%2Farticle%2Fdownload%2F3267%2F2956%2F3857'
```
First outcome: `429 Too Many Requests`. Second outcome: `available: true`, closest `status: 200`, timestamp `20250628010953`, original PDF URL as above. The row uses `https://web.archive.org/web/20250628010953id_/https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857`.

Final locator command (run twice from the lane root; both runs printed the same line):
```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857' 'Since this construction has a register specification as “child-directed,”'
```
Outcome: `LOCATED https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857`.

The initial longer-quote locator command and outcome were:
```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857' 'Since this construction has a register specification as “child-directed,” verbs instantiating it are unlikely to be used in adult-directed speech'
```
`NOT_LOCATED https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 quote-absent`


The row-field check was:
```sh
awk -F'|' '/^ROW:/ {print "ROW_FIELDS=" NF; a=$7; sub(/^.*: "/,"",a); sub(/"$/,"",a); gsub(/[^[:alnum:]]+/," ",a); n=split(a,w,/ +/); print "QUOTE_WORDS=" n}' /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS743/row.txt
```
Outcome: `ROW_FIELDS=13`, `QUOTE_WORDS=11` for that simple token counter; using the locator’s normalization, the quote is 10 words.

## Deliverable excerpt
ROW: | S743 | Kimi Akita, 2012 "Register-Specific Morphophonological Constructions in Japanese", Proceedings of the Annual Meeting of the Berkeley Linguistics Society 38: 3–17 - https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 ; capture https://web.archive.org/web/20250628010953id_/https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 | paper | A | Japanese child-directed verbs as register-specific forms | §2.2 “Child-Directed Verbs”: "Since this construction has a register specification as “child-directed,”" | Helps learners treat child-directed verb forms as context-bound Japanese usage rather than as ordinary adult forms. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Register specification marks child-directed verbs as a distinct pattern for worldbuilders. (S743)
VERIFY: LOCATED https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857
