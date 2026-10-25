# Item-10 quarantine verdicts — kotodama slice (2026-10-25, round 71)

Wave-4 quarantine-first hand-check: every row of the lane's absent-defect-register
slice (21 data rows: 18 `payload-absent` + 3 unreachable-class) was fetched by a
wave-1 scout seat and verdicted. PRESENT = quoted span located with anchor on a
fetched page; REFUSED = source fetched cleanly, quote absent; UNVERIFIABLE =
source unreachable/truncated or no quote span provided by the register. Verdict
evidence lives in `.ufo/waves/round-71/w1/ScoutQuarantineFetch{1,2,3}.md` and
`RevQuarantineCrossCheck.md` (21-row re-derivation; S778 absent from the lane
registry).

| id | verdict | note |
|---|---|---|
| S776 | PRESENT | SAMR GB/T 33661-2017 record metadata contains the quoted span; lane registry S776 is a different source (Penn Museum) — register id mismatch recorded |
| S778 | UNVERIFIABLE | live URL resolves to calendar-room feed, not the quoted passage; no lane registry row for S778 |
| S779 | REFUSED | NAOJ page is a Japanese calendar announcement; quoted spans absent |
| S786 | REFUSED | cited PDF (Conlanging 101) contains quote 1 but not the Chinese quote — multi-quote row fails |
| S787 | REFUSED | China Writers page is about network fiction; quoted span absent |
| S791 | UNVERIFIABLE | registry URL truncated, exact document unfetchable |
| S792 | REFUSED | journal page is the English article; the four Chinese headings absent |
| S795 | PRESENT | Obirin PDF, chapter II §II names taxonomy; quote located across the layout break |
| S796 | PRESENT | Kankyo-U PDF discussion paragraph quote located |
| S804 | PRESENT | Kotobank 苗字 entry quote located (Japanese comma/ellipsis variation) |
| S814 | REFUSED | CSSN article on Han-Jin names; quoted classification passage absent |
| S816 | PRESENT | China Writers interview answer quote located |
| S817 | REFUSED | China Writers 2022 article; Sowers-Wills span absent |
| S820 | PRESENT | Onoma PDF §2 quote located (curly quotes) |
| S823 | PRESENT | China Folklore article first paragraph quote located |
| S824 | PRESENT | Osaka-U PDF exact-span corroboration (text extraction partial) |
| S825 | PRESENT | National Archives era-table page confirms both quote fragments |
| S827 | PRESENT | DOI resolves to Crossref record containing all three cited strings (metadata) |
| S807 | UNVERIFIABLE | DOI now resolves to open metadata/abstract; register gives no quoted span |
| S812 | UNVERIFIABLE | DOI now resolves to open metadata/abstract; register gives no quoted span |
| S835 | UNVERIFIABLE | PDF now fetchable; register gives no quoted span |

Tally: PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5 = 21. Adoption stays CLOSED;
no shokuknow bytes appended or renumbered (id collisions S859/S860 recorded at
`.ufo/waves/round-71/assimilation/`).
