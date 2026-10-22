Verdict: No actionable census or access defect found for C. The 54-row block and both claim acceptance commands passed. No replacement text required.

- `../CORPUS.md:141` — CARRIED — At base `045f458ceaa35d40baa7c56727c346d60ae210bf`, the documented status histogram gave 358 rows: mined 313, queued 35, rejected 10. Quote: “s=$9”.
- `../CORPUS.md:141` — CARRIED — At C land `767040e0d8b9f9fe9e69b9a7ab8bc75a93b33b6b`, the same histogram gave 412 rows: mined 367, queued 35, rejected 10. Quote: “s=$9”.
- `../CORPUS.md:137` — CARRIED — The documented malformed-row command reported 0 rows with `NF!=13` at both revisions. Quote: “NF!=13 {n++}”.
- `../CORPUS.md:143` — CARRIED — The documented duplicate-ID command produced no IDs at either revision: 0 duplicates. Quote: “sort | uniq -d”.
- `../scripts/sources-census.sh:33` — CARRIED — `validate` exited 0 at both revisions and on the current lane. The identical warnings were W04 on S127–S133, S185–S186, and S358; none was new in S359–S412. Quote: “W04 same URL across scopes”.
- `corpus/SOURCES.md:388-441` — CARRIED — C’s S359–S412 block has 54 unique rows; `accept-c.py` reported FLOOR 54, RANGE, STATUS, USEDBY, and ACCESS PASS. All cited rows are mined and use the entry path as a whole used-by item. Quote: “corpus/knowledge/civilizations/kongo-kingdom.md”.
- `tools/check-source-access.py:19` — CARRIED — At base, C land, and the current lane, the checker exited 0 with 2 flagged rows and 0 findings. The flagged rows are S094 and S132, both rejected. Quote: “ACCESS: <flagged> flagged rows, <n> findings”.
- `corpus/knowledge/civilizations/kongo-kingdom.md:99` — CARRIED — Re-opened S359’s OCR at ordinary Archive.org URL. Doc. 139, pp. 455–457 lists the garments Afonso received. Quote: “os tres vestidos que nos por elle emuyastes”.
- `corpus/knowledge/civilizations/kongo-kingdom.md:18` — CARRIED — S359 doc. 142, p. 469 begins Afonso’s complaint about merchants taking Kongo people; the letter asks for the trade to stop. Quote: “nam aja trato de esprauos nem sayda pera elles”.
- `corpus/knowledge/civilizations/kongo-kingdom.md:140` — CARRIED — S359 doc. 147, p. 489 describes the royal review of purchases and the distinction between captive and free people. Quote: “se sam catiuos, se forros”.
- `reports/round-56/claims.json:125` — CARRIED — `accept-o.py --root <C-land>` exited 0; ENTITY, NOFALSE, EXIT, DECODE, KEEP, BADUTF8, FORMAT, and SELFTEST all passed. Quote: “reports/round-56/accept-o.py exits 0”.
- `tools/check-gate-quotes.py:348` — CARRIED — Its selftest passed 38/38; running it on `corpus/lessons/round-56.md` returned `GATE_QUOTES: 0 findings`. Quote: “GATE_QUOTES: 0 findings”.
- `../scripts/sources-census.sh:7` — CARRIED — The census selftest passed. Quote: “writes only stdout or --out”.

Unrun checks: this seat did not reopen the cited pages for S360–S412 or perform a full sentence-by-sentence review of the Kongo entry; those content checks remain outside this census rerun. No tools installed.