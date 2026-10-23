# ScoutRenamingCities — claim C source item (city renaming as politics), S536-S537

Seat: KotodamaR58A2.ScoutRenamingCities. Accessed 2026-10-23 by plain GET (rowcheck's urllib fetch, curl, pypdf 5.4.0 via `uv run`). Two rows offered; both pass rowcheck on all four legs, with and without a scratch `--entry` built from the draft sentences below.

Design decisions these rows serve: **who may change a name and under what rule** (India: the state proposes, the Ministry of Home Affairs approves, the Survey of India fixes the spelling, the state gazettes it) and **renaming as politics at scale** (Ukraine: a mass renaming of names inside settlements under a decolonization-of-toponymy law, plus the restoration of Crimean Tatar names).

Host note for DISTINCT: both rows are on `unstats.un.org`. The DISTINCT leg needs at least 10 hosts across the entry's cited rows, so weigh these two against other seats' unstats rows.

## Rows

| S536 | State Service of Ukraine for Geodesy, Cartography and Cadastre (StateGeoCadastre) for Ukraine, 2025, National report of Ukraine for the period 2023-2024 (GEGN.2/2025/32/CRP.32, UNGEGN 2025 session, item 4(b)) — https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_32_CRP32_item4b.pdf (direct, HTTP 200) | record | A | Ukraine's 2023-2024 mass renaming of names within settlements under its decolonization-of-toponymy law | p. 2, section B: "In 2023-2024, there was a massive renaming of place names of settlements (mainly streets, boulevards, alleys, avenues, squares, parks, embankments, bridges, subway stations, etc.)" | Ukraine renamed place names inside its settlements on a mass scale in 2023-2024, chiefly streets, squares, parks, bridges and metro stations. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S537 | Survey of India for the Government of India, 2025, Report of India (GEGN.2/2025/138/CRP.138, UNGEGN 2025 session, item 5(a)) — https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_138_CRP138_item5a.pdf (direct, HTTP 200) | record | A | India's official procedure for changing a geographical name | p. 4, section Transliteration workflow for Geographical Name Changes: "The process of changing geographical names follows a structured procedure to ensure accuracy and standardization." | India renames places through a fixed official procedure meant to keep each new geographical name accurate and standardised. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Kind is `record` for both: each is a government's own report filed with UNGEGN (the S536 report was prepared by Ukraine's StateGeoCadastre; the S537 report says it was "Prepared by Survey of India, Department of Science & Technology, Government of India"). I confirmed the page locators with pypdf. In CRP32, "massive renaming" and "Decolonization of Toponymy" are on page 2 and "Crimean Tatar names" is on page 4. In CRP138, "structured procedure" is on page 4.

## Gate lines

- S536 — https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_32_CRP32_item4b.pdf — accessed 2026-10-23 — p. 2, section B: “In 2023-2024, there was a massive renaming of place names of settlements (mainly streets, boulevards, alleys, avenues, squares, parks, embankments, bridges, subway stations, etc.)”. Grounds: Ukraine renamed place names inside its settlements on a mass scale in 2023-2024, chiefly streets, squares, parks, bridges and metro stations. Seat: ScoutRenamingCities.
- S537 — https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_138_CRP138_item5a.pdf — accessed 2026-10-23 — p. 4, section Transliteration workflow for Geographical Name Changes: “The process of changing geographical names follows a structured procedure to ensure accuracy and standardization.” Grounds: India renames places through a fixed official procedure meant to keep each new geographical name accurate and standardised. Seat: ScoutRenamingCities.

## rowcheck output

`timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutRenamingCities/rows.md` (exit 0):

```
S536 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_32_CRP32_item4b.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['2023', '2024', 'bridg', 'name', 'park', 'place'] | TOPIC: quote_hits=2 function_words=4 page_hits=91 page_terms=66 need=1/2/3/2
S537 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_138_CRP138_item5a.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['accur', 'geogr', 'name', 'proce', 'stand'] | TOPIC: quote_hits=1 function_words=5 page_hits=53 page_terms=49 need=1/2/3/2
```

The same command with `--entry /fast/scratch/hyaku/kotodama-r58/ScoutRenamingCities/entry-draft.md`, a scratch file holding exactly the six draft sentences below, printed the same two all-PASS lines and exited 0. That covers RELEVANCE rules (c) and (d).

An alternative anchor for S537, from the same URL and page, also passed all four legs: "Following this approval, the respective State/UT government publishes a gazette notification, formally announcing the change and implementing it on the ground." (teaches: "After central approval, the state or union territory government makes a renaming official by publishing a gazette notification."). I did not offer it because the sentence never says "name" itself; it passes TOPIC only through `gazette`. A strict SUPPORT reviewer could read "the change" as not about place names.

## draft sentences

S536:
- Renaming as politics can run at mass scale: in 2023-2024 Ukraine saw a massive renaming of place names inside its settlements, mainly streets, squares, parks, bridges and subway stations (S536).
- Ukraine's national report ties that wave to its law of 21 March 2023 on condemning the propaganda of Russian imperial policy and on the decolonization of toponymy, so the renaming of names is framed as decolonization (S536).
- Renaming can also restore an older layer: a 2023 Ukrainian law provides for the return of historical Crimean Tatar names in the Autonomous Republic of Crimea (S536).

S537:
- India treats renaming as a structured procedure: a state or union territory government sends a formal request with justifications to the Ministry of Home Affairs, the national names authority, for approval of the proposed geographical name change (S537).
- Before approving, the ministry asks the Survey of India for the correct spelling of the new geographical name, so standardization is built into the change itself (S537).
- The process ends when the state publishes a gazette notification and the Survey of India puts the changed name on its official topographical maps (S537).

Page support for the sentences beyond the quotes:
- CRP32 p. 2 names the law of March 21, 2023, "On Condemnation and Prohibition of Propaganda of Russian Imperial Policy in Ukraine and Decolonization of Toponymy".
- CRP32 p. 4: the 2023 law "provides for the return of historical Crimean Tatar names in the Autonomous Republic of Crimea".
- CRP138 summary: "The Ministry of Home Affairs, Government of India, is the National Names Authority".
- CRP138 p. 4: the state or union territory government submits "a formal request to the Ministry of Home Affairs (MHA) for approval of the proposed name change", which "includes justifications and supporting documents". "MHA consults the Survey of India (S oI), to provide the correct spelling", then the state government "publishes a gazette notification", and "The updated name is subsequently incorporated into Survey of India's topographical maps based on the official notification."

## rejected

The brief allowed 1 to 3 sources. I opened more than that while looking for a page that passes BOILER and TOPIC, and every one is listed here.

- https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=113433 (Press Information Bureau, "Renaming of Cities", 2014; MHA no-objection procedure). Fails TOPIC: the page has 0 terms from the field's own vocabulary, and the leg needs 2. Probe output (rowcheck `window_hits` and `DISCIPLINE`): `== https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=113433 text/html; charset=utf-8 2578 hits 8 terms 0`.
- https://archive.pib.gov.in/newsite/PrintRelease.aspx?relid=113433. Unfetchable: `ERR ... <urlopen error [Errno 111] Connection refused>`.
- https://assets.publishing.service.gov.uk/media/634e6ecfe90e0731ada4d0c6/Kazakhstan_Toponymic_factfile_2022.pdf (UK PCGN, Kazakhstan factfile; the Nur-Sultan to Astana renaming and post-Soviet renaming types). Fails BOILER because the host's root page is unfetchable. rowcheck: `S536 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | ... | BOILER: root-unfetchable https://assets.publishing.service.gov.uk/ HTTPError`. curl on the root returns `404`.
- https://assets.publishing.service.gov.uk/media/6ab67e78997a4b2950ccef41/India_Toponymic_Factfile.pdf and https://assets.publishing.service.gov.uk/media/6717aa96a71f39bdb1c9c166/India_Factfile.pdf (UK PCGN, India factfile; Karnataka's 2014 renaming of 12 settlement names, Madras to Chennai). Same host, so BOILER fails the same way (root `404`). The key sentence also extracts as `the Karn ātaka government renamed 12 English settlement names`, so a verbatim quote cannot match.
- https://www.gov.kz/memleket/entities/abay-cultura-arhiv/press/article/details/144714 and https://www.gov.kz/memleket/entities/aktobe-til/activities/7532?lang=ru (Kazakhstan onomastics pages). Each serves only a script shell: `text/html 246 hits 0 terms 0`.
- https://www.mha.gov.in/MHA1/Par2017/pdfs/par2014-pdfs/ls-161214/3797.pdf and https://www.mha.gov.in/MHA1/Par2017/pdfs/par2013-pdfs/ls-230413/4794.pdf (MHA Lok Sabha answers). Both return `HTTP Error 404: Not Found`.
- https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_137_CRP137_item4b.pdf (Report of the Republic of India). This page would pass TOPIC (`hits 39 terms 36`), but its renaming-authority sentences are 33 and 40 words, over the 25-word limit. CRP138 carries the procedure instead.
- https://unstats.un.org/unsd/geoinfo/UNGEGN/docs/29th-gegn-docs/WP/WP24_4_Report%20of%20the%20Eastern%20Europe,%20Northern%20and%20Central%20Asia%20Divsiion_english.pdf (UNGEGN 2016 divisional report). Its naming-law sentences are generic rather than about city renaming as politics. The Kazakhstan onomastic-commission sentence is over 25 words and extracts with a split word (`circul a- tion`).
- https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_86_CRP86_item4a_e.pdf and https://unstats.un.org/unsd/ungegn/sessions/3rd_session_2023/documents/GEGN.2_2023_58_CRP58_E.pdf (2025 and 2023 divisional reports). A grep for `renam|Astana|Nur-Sultan|decommun|derussif` found no matching sentence (empty output).
- https://digitallibrary.un.org/record/4020108 (Kazakhstan 2017 report, "National standardization of place names in the Republic of Kazakhstan"). The site root answered `root 202`, and no PDF link came back from a plain GET. I did not pursue it further because of the access-control rule.
- https://www.dsac.gov.za/geographical_council, https://www.dsac.gov.za/South%20African%20Geographical%20Names%20process and https://www.dsac.gov.za/SAGN_Process (South Africa's names council pages). All three are unfetchable by the locator: `<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1082)>`.
- https://www.gov.za/sites/default/files/gcis_document/202603/54281gon7208.pdf and https://www.gov.za/sites/default/files/gcis_document/202501/51949gon5770.pdf (notices on the bill amending the South African Geographical Names Council Act). Both are about consultation on the bill, with no renaming sentence. gon5770 has only `terms 2`.

## installs:

None.
