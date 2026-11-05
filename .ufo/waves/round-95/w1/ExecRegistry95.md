# ExecRegistry95 report — claim C registry, captures, index

Rows finalized (5, A/mined, opened 2026-11-05, 180d, used-by corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md):
- S970 A — Seto choral/antiphonal lament; evidence/S970.txt sha256 dc7394e9862003b0b26e7631520e3dcb19832d25b19ddd4e6898cda06c371316, S970.pdf e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e; anchor quote "the antiphonal way of performing Seto songs" (7 words)
- S971 A — Corsican voceru antiphony + feminine mode; S971.txt 656c45388dbfcab8f9de8a233eada5d8f8571647a1f04955605bff71cbc4a26a; anchor quote "The antiphonal nature of voceru performance" (6 words)
- S972 A — Irish wake professional keeners; S972.txt d3ff0209b9d80418bcc9345535f5fd440a3fc8a2433da6982c42a65d777293ce; anchor quote "Professional keeners took over." (4 words)
- S973 A — bean chaointe female professional mourner / gendered rules; S973.txt e017b3958dac14b32ff08a11f1750638e997c5df43ec9674a91413f5c42cac76; anchor quote "was important in the role of the female professional mourner" (10 words)
- S974 A — Svan refrain + praise; S974.txt 251b4d3f420164baa4bdc6508e54736cb0d00a42bc66940363203c264060159d; anchor quote "ends with a refrain exclamation" (5 words)

Quote verification (python count == 1 against staged bytes): each anchor above count=1, 4-10 words <=25. Each row uses one Quote1 anchor; S970 Quote2 was excluded (count_norm 2) — not used in registry. All evidence copied byte-exact from ScoutTopic95 stage; sha256 match scout manifest.

Collision: assimilation/reg-ids.txt 893 rows (base, tail S969), staged-ids.txt 5 (S970-S974), comm -12 = 0 lines (empty intersection). Union 898, highest S974.

Mirror validation (scratch $S/mirror, cleaned after run): census rc 0, 0 E-lines, 35 W-lines (pre-existing), 0 findings on S970-S974 (stage/census.txt); index CORPUS-INDEX OK files=267 rows=267 findings=0 rc 0 (stage/index.txt). README.new.md inserts funerary row after evidentiality, bumps linguistics (39)->(40), adds revision 2.24 and ## Round 95 lament entry footer (267, 40/36/43/29/24/95); README.diff touches only 3 hunks (revision, header+row, footer). Predispatch on mirror: C1 PASS bytes=50148 h2=12 table=11x5 phrases=6/6 topic-equal; C2 PASS rows=898 highest=S974 qualifying=5; C4 PASS; C5 rc0 by direct index call (mirror lacks tools/check-corpus-index.py, so predispatch C5 reports tool-missing there — expected); C3 PASS added=0 removed=0 on base tree (append-only, append-before-##-Paths verified in mirror).

Stage files: SOURCES.append.md sha256 8c728f8b7a1575e0a7716e204be89aa12a24dda353ddd5cbe58add88c3caefd5 (4221 B); README.new.md 194800 B; README.diff 5.0K; census.txt; index.txt; evidence/*.txt/*.pdf (10 files); DONE contains that sha256. Tools installed: none.
