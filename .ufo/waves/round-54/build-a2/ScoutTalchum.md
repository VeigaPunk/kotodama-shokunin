# ScoutTalchum — Korean talchum / talnori mask dance drama, round 54 attempt 2

Scope of this seat: Korean mask dance drama (talchum, talnori, sandae nori, yaryu, ogwangdae,
byeolsingut) as worn object and licensed voice — what the mask is said to be, who wears it,
who may see it, when and where it appears, what it licenses, what is restricted, and what
happens to it afterwards. Seven sources opened this session, all on 2026-10-22; every row was
read from the URL in its `url:` line. No tools installed or upgraded.

Integration notes for the L1, before the rows:

- The element number is **01742**, not 01711. `01711` is Congolese rumba; a search result that
  gave `...-01711` for Talchum is wrong. The Talchum element page is
  `https://ich.unesco.org/en/RL/talchum-mask-dance-drama-in-the-republic-of-korea-01742`, and
  the 2022 inscription decision is 17.COM 7.b.22.
- `english.cha.go.kr` no longer resolves (DNS ENOTFOUND on 2026-10-22). The Korea Heritage
  Service now serves the same English pages at `english.khs.go.kr` (host verified, HTTP 200).
  The KHS host answered page fetches earlier in this session and then timed out on later
  status probes — the pages below were read, but the host is flaky.
- The KHS Gangnyeong record's English gloss says "(Mask Dance Drama of Gangneung)" in its
  second sentence while the title, the Korean name and the place are Gangnyeong
  (Gangnyeong-eup, Hwanghaenam-do). Treat "Gangneung" there as a translation slip.
- Rows 1 and 2 are the two sources the seat brief named (UNESCO element page; Korea Heritage
  Service page). Rows 3 to 7 are additional opened sources, each independently quoted and
  scoped; the L1 may take or drop any of them. Rows 5 and 6 are the only rows that carry the
  post-performance burning of masks, and row 7 is the only row that carries an exclusion rule
  for elites — row 7 is a popular article (single-source claims should be marked `(to-verify)`
  if the entry uses them).

Draft ids are NEW-ScoutTalchum-1 through NEW-ScoutTalchum-7; the L1 assigns the S-ids
(S239 upward) at integration.

### NEW-ScoutTalchum-1

citation: UNESCO, Intangible Cultural Heritage Section. "Talchum, mask dance drama in the Republic of Korea" (Republic of Korea), element 01742, Representative List of the Intangible Cultural Heritage of Humanity, inscribed 2022 (17.COM). Element page, https://ich.unesco.org/en/RL/talchum-mask-dance-drama-in-the-republic-of-korea-01742.
url: https://ich.unesco.org/en/RL/talchum-mask-dance-drama-in-the-republic-of-korea-01742 (direct fetch; quotes also verified in the Wayback capture https://web.archive.org/web/20231227074841id_/https://ich.unesco.org/en/RL/talchum-mask-dance-drama-in-the-republic-of-korea-01742)
route: direct plain request (curl, HTTP 200, 157,668 bytes, no bot-challenge marker, accessed 2026-10-22); quotes checked against Wayback capture id 20231227074841 (id_ raw, HTTP 200). A read-tool request to the sibling URL ...-01711 was served the site's bot challenge (image code) — challenge met, not passed; that URL was the wrong element and no content was taken from it.
kind: web
tier: A — UNESCO is the body that inscribed the element, and this is its own element page and official description; the tier covers the inscription and its description, not Korean mask craft.
scope: the official description of talchum as inscribed in 2022: its performance form, the caricature-and-equality frame, the no-fixed-stage rule, the audience's role, the 1970s-1980s student transmission, the shift from men to men-and-women, and mask-making as a transmitted skill. Not individual mask types, not materials, not regional rules.
quotes:
- element page, description, sentence 1: "Talchum is a performing art that encompasses dance, music and theatre."
- element page, description, sentence 3: "The practice uses caricatures of everyday characters to convey its underlying appeal to universal equality and criticism of social hierarchy."
- element page, description, sentence 4: "Talchum performances do not require a formal stage: any empty space can become a venue."
- element page, description, sentence 5: "The audience plays an essential role, contributing to the production with their cheers and jeers as the drama unfolds."
teaches: the masked drama is carried by caricature types rather than individuals, it claims ordinary space as its venue, and the crowd is a licensed participant, not a spectator.
draft sentences:
- Decide what the mask licenses before deciding who may wear one: UNESCO frames the whole practice as caricatures of everyday characters used to appeal to universal equality and to criticize social hierarchy (NEW-ScoutTalchum-1, element page, description, sentence 3).
- Do not build a theatre for it: the performance needs no formal stage, and any empty space can become a venue, so the rule is about who claims a ground and when, not about a building (NEW-ScoutTalchum-1, element page, description, sentence 4).
- Give the audience a role with teeth: cheers and jeers are part of the production as the drama unfolds, so the crowd's noise is licensed speech, not interruption (NEW-ScoutTalchum-1, element page, description, sentence 5).
- Decide whether masking is tied to sex: the practice was initially performed by men and now includes women, so the wearer rule is a changeable convention, not a property of the mask (NEW-ScoutTalchum-1, element page, description, sentence 8).
- Decide what is transmitted with the mask: knowledge and skills of both performance and mask-making pass to younger generations through local associations, clubs, camps and public schools (NEW-ScoutTalchum-1, element page, description, sentence 7).

### NEW-ScoutTalchum-2

citation: Korea Heritage Service (Cultural Heritage Administration, Republic of Korea). "Talchum, mask dance drama in the Republic of Korea", UNESCO Heritage / Intangible Cultural Heritage of Humanity article, nttId 84820. English site.
url: https://english.khs.go.kr/cop/bbs/selectBoardArticle.do?ctgryLrcls=&nttId=84820&bbsId=BBSMSTR_1205&uniq=0&mn=EN_03_01
route: direct (read tool fetch of the live page, served and read 2026-10-22); later plain-request status probes to english.khs.go.kr timed out (curl 000) — the host was intermittently unreachable this session. The legacy URL on english.cha.go.kr for the same article (nttId 84820) does not resolve (DNS ENOTFOUND).
kind: web
tier: A — the national heritage service's own statement on the element: the designations it made and the inscription it reports; scoped to that, not to mask craft.
scope: how the national service presents talchum (masked performers, six to ten musicians, caricatures), its 1964 national and local designations of Yangjubyeolsandae-nori and other local variants, the 2022 UNESCO inscription, and its framing as community and local identity. Not mask types or materials.
quotes:
- article body, first paragraph: "masked performers humorously explore social issues through dramatic combinations of dances, songs, movements and dialogue"
- article body, second paragraph: "Talchum has been recognized as a symbol of Korea’s traditional performing arts and intangible cultural heritage"
- article body, third paragraph: "Yangjubyeolsandae-nori, mask dance drama of Yangju and other local variants of talchum were designated as intangible cultural heritage"
- article body, third paragraph: "reinforcing a sense of community and local cultural identities in the lives of the Korean people"
teaches: "talchum" is a family of regional traditions designated one by one since 1964, and the heritage service attaches the practice to community and local identity rather than to a single authorized version.
draft sentences:
- Do not write one canonical talchum: the service dates safeguarding to 1964, when Yangjubyeolsandae-nori and other local variants were designated at national and local levels, so the tradition is a set of regional variants (NEW-ScoutTalchum-2, article body, third paragraph).
- Attach the mask drama to a community, not only to a stage: the service presents it as reinforcing a sense of community and local cultural identities in people's lives (NEW-ScoutTalchum-2, article body, third paragraph).
- Keep the comic register inside the social problem: masked performers humorously explore social issues through dance, song, movement and dialogue with a small band (NEW-ScoutTalchum-2, article body, first paragraph).

### NEW-ScoutTalchum-3

citation: Korea Heritage Service (Cultural Heritage Administration, Republic of Korea). "Gangnyeong Talchum (Mask Dance Drama of Gangnyeong)", National Intangible Cultural Heritage record no. 34, Heritage Search. English site.
url: https://english.khs.go.kr/chaen/search/selectGeneralSearchDetail.do?mn=EN_01_01&sCcebKdcd=17&ccebAsno=0000340000000&sCcebCtcd=11
route: direct plain request (curl, page served and read 2026-10-22); later status probes to the same host timed out (000), noted once under `unopened:`.
kind: record
tier: A — the national heritage service's own inventory record for this designated element.
scope: one regional talchum: its Dano date and Gangnyeong-eup (Hwanghaenam-do) place, its seven named acts, the troupe's march, its satire targets, its dance character, and the record's own statement that its masks show realistic facial expressions. Not the masks' materials, not who carves them.
quotes:
- record description, sentence 1: "Talchum (mask dance) was performed across the country up to the early Joseon Period (1392 – 1910)."
- record description, sentence 4: "The Mask Dance Drama of Gangnyeong is performed on Dano (May 5 on the lunar calendar) in Gangnyeong-eup, Hwanghaenam-do"
- record description, sentence 7: "The play includes satire about such issues as nobles harassing commoners, depraved monks, and male chauvinism"
- record description, last sentence: "Performers wearing masks displaying realistic facial expressions and engaging in elegant and slow dancing movements are features of Gangnyeong Talchum"
teaches: a regional mask drama fixes a festival date and a place, breaks into named acts (including a Mokjung dance and a scene of Chwibari and the Old Monk), itemizes its satire targets, and treats mask appearance and dance tempo as the tradition's identifying features.
draft sentences:
- Fix the calendar and the ground: this talchum is performed on Dano, lunar May 5, in Gangnyeong-eup, Hwanghaenam-do, so the mask appears on a set day in a set place (NEW-ScoutTalchum-3, record description, sentence 4).
- Itemize what the satire is licensed to hit: the record names nobles harassing commoners, depraved monks, and male chauvinism in plural marriage as the play's targets (NEW-ScoutTalchum-3, record description, sentence 7).
- Decide how the mask reads: these masks display realistic facial expressions and are worn with elegant, slow dancing, which the record uses to distinguish Gangnyeong from Bongsan talchum — mask appearance and movement style are one design decision (NEW-ScoutTalchum-3, record description, last sentence).
- Build the play as acts, not as a plot: the record lists seven acts, including a Lion Dance, a Mokjung Dance, and a Dance of Chwibari and the Old Monk (NEW-ScoutTalchum-3, record description, sentence 5).
- Give the troupe a public approach: before the performance the twenty members march, playing music to entertain spectators along the road (NEW-ScoutTalchum-3, record description, sentence 6).

### NEW-ScoutTalchum-4

citation: Korea Heritage Service (Cultural Heritage Administration, Republic of Korea). "Bongsan Talchum (Mask Dance Drama of Bongsan)", National Intangible Cultural Heritage record no. 17 (designated 1967.06.17), Heritage Search. English site.
url: https://english.khs.go.kr/chaen/search/selectGeneralSearchDetail.do?mn=EN_01_01&sCcebKdcd=17&ccebAsno=0000170000000&sCcebCtcd=11
route: direct plain request (curl, page served and read 2026-10-22); later status probes to the same host timed out (000), noted once under `unopened:`.
kind: record
tier: A — the national heritage service's own inventory record for this designated element.
scope: the service's definition of mask dance (masked people acting as person, animal or god), Bongsan's dates, its monk-heavy act list, the masked fraction of the troupe, the pre-play rite, and its satire targets. Not mask materials or custody rules.
quotes:
- record description, sentence 1: "one person or several people wearing a mask act as a person, an animal, or a supernatural being (god)"
- record description, sentence 4: "Performed on the night of Dano (fifth day of the fifth lunar month) and Haji (Summer Solstice)"
- record description, sentence 5: "the 36 members of the play (27 of them wearing masks) march to the site of the play while playing music"
- record description, sentence 6: "They also hold a sacrificial rite."
teaches: the mask is the license to be a person, an animal or a god; masking is partial inside the troupe (27 of 36); the play opens with a march and a rite, and its act list is built around monks.
draft sentences:
- Say what the mask is for: the service defines mask dance as a play in which masked people act as a person, an animal, or a supernatural being (god), so the mask is a license to be something other than the wearer (NEW-ScoutTalchum-4, record description, sentence 1).
- Decide who is masked and who is not: of the 36 members of this play, 27 wear masks and the rest supply the march and music (NEW-ScoutTalchum-4, record description, sentence 5).
- Put a rite in front of the play: the troupe holds a sacrificial rite before performing, so the comic license is opened by ritual (NEW-ScoutTalchum-4, record description, sentence 6).
- Fix the night: Bongsan talchum is performed on the night of Dano and at the summer solstice (Haji) (NEW-ScoutTalchum-4, record description, sentence 4).
- Decide how much of the clergy is on stage: the act list runs through four monks, eight monks in black robe, a female troupe member, an old monk, a nobleman and an old wife, and the play satirizes nobles, depraved monks and plural marriage (NEW-ScoutTalchum-4, record description, sentences 4 and 7).

### NEW-ScoutTalchum-5

citation: ICHCAP (International Information and Networking Centre for Intangible Cultural Heritage in the Asia-Pacific Region, UNESCO Category 2 Centre). "Hahoe Byeolsingut Tallori (Mask Dance Drama of Hahoe)" (EE00002169), ichLinks archive, description credited to "National Intangible Cultural Heritage, Republic of Korea". English record.
url: https://www.ichlinks.com/archive/elements/elementsV.do?nation=KR&elementsUid=13877678342441298705
route: direct, HTTP 200 (plain-request status check 2026-10-22); record text read through the read tool's fetch of the live page.
kind: record
tier: B — a UNESCO Category 2 centre's archive reproducing the national inventory description; authoritative for the wording as published by ICHCAP, not itself the designating body.
scope: the Hahoe village ritual mask drama: its ritual frame and eight acts, its monk-and-noble satire, the guardian-symbol bride mask and its restricted visibility, the eleven alder-wood masks, the National Treasure designation, and the record's statement that the play ends without the mask-burning rite used elsewhere. Not who carves the masks, not the full type list.
quotes:
- record description, sentence 4: "The play includes ridicule of depraved monks, satires about nobles, and other humorous content."
- record description, sentence 5: "It is believed that the mask for a newly-wed woman symbolizes the village guardian."
- record description, sentence 6: "Thus, the mask is shown to people only during Byeolsingut."
- record description, sentence 10: "This play performed in Hahoe ends without the post-event rite of burning the masks used as in mask play events that are held elsewhere."
teaches: a mask can be a restricted object shown only inside its ritual (the bride mask is the village guardian and appears only during the byeolsingut), the drama is a village ritual held every three, five or ten years, and Hahoe is the exception to a post-event burning rite that other mask play events perform.
draft sentences:
- Make one mask an object of restricted visibility: at Hahoe the mask of the newly-wed woman is held to symbolize the village guardian, and it is shown to people only during the byeolsingut ritual (NEW-ScoutTalchum-5, record description, sentences 5 and 6).
- Decide how often the mask may appear at all: the village performs the ritual about once every ten years (December 15) or on special occasions, so the mask's public life is rare by design (NEW-ScoutTalchum-5, record description, sentence 2).
- Decide what happens to the mask afterwards: this play ends without the post-event rite of burning masks that other mask play events perform, which is exactly why its eleven alder-wood masks survive as National Treasure No. 121 (NEW-ScoutTalchum-5, record description, sentences 7, 8 and 10).
- Keep the satire targets explicit: the eight acts include a Depraved Monk Act and an Act of Nobleman and Scholar, and the record names ridicule of depraved monks and satires about nobles (NEW-ScoutTalchum-5, record description, sentences 3 and 4).

### NEW-ScoutTalchum-6

citation: ICHCAP (International Information and Networking Centre for Intangible Cultural Heritage in the Asia-Pacific Region, UNESCO Category 2 Centre). "Suyeong Yaryu (Mask Dance Drama of Suyeong)" (EE00002149), ichLinks archive, description credited to "National Intangible Cultural Heritage, Republic of Korea". English record.
url: https://www.ichlinks.com/archive/elements/elementsV.do?nation=KR&elementsUid=13877572958550259534
route: direct, HTTP 200 (plain-request status check 2026-10-22); record text read through the read tool's fetch of the live page.
kind: record
tier: B — a UNESCO Category 2 centre's archive reproducing the national inventory description; authoritative for the wording as published by ICHCAP, not itself the designating body.
scope: one village mask drama in Busan (designated 1971): who performs it, the night it is performed and the rite before it, and the explicit statement that the used masks are collected and burned at the end as a rite for the village's peace. Not mask materials, not who makes them.
quotes:
- record description, sentence 3: "This mask play was performed by non-professionals such as villagers."
- record description, sentence 4: "Suyeong Yaryu is performed by villagers when the full moon rises on the night of January 15 on the lunar calendar"
- record description, sentence 8: "At the end of the performance, they collect the masks used and burn them as a rite of praying for the peace of the village."
- record description, sentence 10: "The performance includes a satire about nobles and deals with the problem of concubines."
teaches: here the performers are non-professional villagers, the mask night is the first full moon of the year, the masks are deliberately destroyed as a closing rite, and the satire targets nobles and concubinage.
draft sentences:
- Decide whether masks are made to survive: at Suyeong the troupe collects the masks at the end of the performance and burns them as a rite praying for the village's peace, so the mask is single-use by rule (NEW-ScoutTalchum-6, record description, sentence 8).
- Decide who may wear a mask: this mask play was performed by non-professionals such as villagers, not by a licensed troupe (NEW-ScoutTalchum-6, record description, sentence 3).
- Fix the night and the rite before it: the play is performed when the full moon rises on lunar January 15, after a sacrificial rite for the mountain guardian deities, the village spring water and the spirit of General Choe Yeong (NEW-ScoutTalchum-6, record description, sentence 4).
- Decide who gets the last word at the end of the mask's life: burning closes the performance as a rite for communal peace, so destruction is part of the ceremony rather than waste (NEW-ScoutTalchum-6, record description, sentence 8).

### NEW-ScoutTalchum-7

citation: Alper, Tim (2020). "Tal Tales: Magic of Traditional Masks", KOREA webzine, March 2020, Culture Vulture, Korean Culture and Information Service (KOCIS), Ministry of Culture, Sports and Tourism.
url: https://www.korean-culture.org/eng/webzine/202003/sub07.html
route: direct, HTTP 200 (plain-request status check 2026-10-22); article text read through the read tool's fetch of the live page.
kind: web
tier: B — an official government culture webzine with a named author; popular secondary, not an inventory record, so its claims stand alone here and should be marked `(to-verify)` if the entry uses them.
scope: a popular account that states the single-use burning practice and its agricultural rationale, names the stock villains, and claims the elite classes were de facto excluded from tal culture. Not an inventory record; not a mask typology.
quotes:
- lead section, paragraph beginning "What most tourists are unaware of", sentence 3: "The masks were single-use items that were carefully crafted, used just once and then burned on a raging bonfire."
- section "Original K-dance", paragraph beginning "Talchum speaks volumes", sentence 2: "burning the masks after their use would win yet more agricultural favor from supernatural forces"
- section "Original K-dance", paragraph beginning "Dance was a way for villagers", sentence 2: "their villains were greedy and oppressive nobles, degenerate monks, and grumpy, snobby and ivory-tower scholars"
- section "Original K-dance", paragraph beginning "Nobles and both the priestly", sentence 1: "Nobles and both the priestly and scholarly class, all of whom frowned on tal culture, were de facto excluded from it."
teaches: the popular account ties mask burning to agricultural blessing, lists nobles, monks and scholars as the stock villains, and claims the same classes were excluded from the practice — an access rule that the inventory rows above do not state.
draft sentences:
- Decide why the mask is destroyed: this account says the masks were crafted for one use and burned on a bonfire, and that burning them was thought to win agricultural favor from supernatural forces (NEW-ScoutTalchum-7, lead section, paragraph beginning "What most tourists are unaware of", sentence 3; section "Original K-dance", paragraph beginning "Talchum speaks volumes", sentence 2).
- Stock the villain roles from the same list the inventory records give: greedy and oppressive nobles, degenerate monks, and snobbish scholars (NEW-ScoutTalchum-7, section "Original K-dance", paragraph beginning "Dance was a way for villagers", sentence 2).
- If the entry states an exclusion rule, cite this row and mark it `(to-verify)`: the article claims nobles and the priestly and scholarly class were de facto excluded from tal culture (NEW-ScoutTalchum-7, section "Original K-dance", paragraph beginning "Nobles and both the priestly", sentence 1).

Not carried by any row above: who may carve or make a mask (no opened page names a mask maker, a workshop or a carving rule for talchum), what materials talchum masks are made of (the opened pages give alder wood only for Hahoe, and materials for gourd-and-paper Songpa and Dongnae appear only in the related-element blocks of the ICHCAP pages, not in a page quoted here), any price, sale or artisan-licensing rule, any rule on women wearing masks in the historical period, and any statement about who may not watch a talchum performance.

unopened:
- https://ich.unesco.org/en/RL/talchum-mask-dance-drama-in-the-republic-of-korea-01711 — wrong element id (01711 is Congolese rumba); the read-tool request was served the site's bot challenge (image code), challenge met, not passed, and no content was taken from it.
- https://english.cha.go.kr/cop/bbs/selectBoardArticle.do?ctgryLrcls=&nttId=84820&bbsId=BBSMSTR_1205&uniq=0&mn=EN_03_01 — legacy KHS English domain: DNS ENOTFOUND (host no longer resolves); the same article was read at english.khs.go.kr (row 2).
- https://folkency.nfm.go.kr/en/topic/detail/5226 (National Folk Museum of Korea, Korean Folklore Encyclopedia, "Hahoe Byeolsin Mask Dance Performance") — fetched page is a 1 KB JavaScript shell with no article text; no readable content.
- KHS detail pages for other mask-drama records (Yangju Byeolsandae 0-2, Namsadang 0-3, Dongnae Yaryu 0-18, Songpa Sandae Nori 0-49, record 0-61, Hahoe 0-69) — those asno/ctcd combinations returned a 404 page or an empty body; the same national inventory texts were instead read on the ICHCAP ichLinks pages (rows 5 and 6), whose related-element blocks also quote Songpa (33 masks of gourd, pine skin and paper), Dongnae (gourd masks with movable chins) and Yangju (32 characters) — not filed as rows because the pages themselves were not opened.
- UNESCO nomination file PDF for element 01742 — not located: the element page copy fetched this session contains no `doc/src` links, so the nomination form was not opened.
- UNESCO decision page 17.COM 7.b.22 — not opened; unnecessary once the element page (row 1) was read, and the ich.unesco.org host served a bot challenge to the read tool.
