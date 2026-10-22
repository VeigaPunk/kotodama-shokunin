# ScoutS256Tier — S256 vs S258 tier harmonisation

Carried item: `corpus/lessons/round-54-verifier-spotcheck.md` §5 item 4 (S256 filed A, S258 filed B; `corpus/QUALITY.md:29` corrects a filed tier only by a superseding row). Round 55, lane base `f4015e70b829523ed81e14ce4279bfab0e0233e4`. Access date for every source below: 2026-10-22.

## Decision

**S256 is the row to supersede, at tier B.** S258's B is correct and stays. Both element pages are the same kind of object: the inscribing body's published summary of a State Party's nomination, authoritative for what the register states and secondary for claims about the living practice. S256's A is the outlier.

Three grounds, strongest first.

1. **Criterion 6, on the row's own scope.** S256's scope names practice topics: who performs the monastery mask dance, where the mask first appears, the two registers of the dance, the occasion, and the benefit claimed for the audience (`corpus/SOURCES.md:285`). Its own tier note already concedes the page "is not a community statement". UNESCO is authoritative for the listing, not for what the Drametse monastery does; A is therefore reserved for the inscription facts (year, list, decision), which the row does not claim. B is the honest tier for the practice topics it does claim.
2. **The description field is demonstrably an edited condensation.** For element 00252 the State Party's nomination form is on the page and I opened it: field D gives "The busó [boosho] festivities at Mohács are an end-of-winter custom performed by persons in special masks as a ritual aiming to expel winter." and "It beings on the Thursday of Carnival week and goes on till Pancake Tuesday." The page's six-day-late-February sentence rewrites both. So the field is the Secretariat's edited summary, exactly as S258's tier note says — the note is verified, not assumed.
3. **Lane convention.** Of the ten rows citing a UNESCO element page, six are B (S157, S163, S186, S264, S270, S271) and the three A rows are the Committee decision S069 and the earlier page rows S062, S063. Harmonising to B matches the majority and criterion 6.

The same test could not be run against the Bhutanese form: the element page carries no nomination-file link, and every `doc/src/00161-*` path I tried either 404s or serves an unrelated document (see `unopened`). For S256 the authorship point is therefore [INFERENCE] from the shared template and the 00252 result; the criterion-6 scope argument in ground 1 does not depend on it.

## Re-open record

| row | url read | route | observed |
|---|---|---|---|
| S256 | https://ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 | direct plain `curl`, one request | HTTP 200, `text/html; charset=UTF-8`, 211,091 bytes; no challenge marker (no Anubis, captcha or "just a moment" text); full description present. Description wording identical to the round-54 quotes; the 178-byte growth is page furniture. |
| S258 | https://ich.unesco.org/en/RL/busojaras-carnival-at-mohacs-00252 | direct plain `curl`, one request | HTTP 200, `text/html; charset=UTF-8`, 154,474 bytes, `X-Cache: HIT`; no challenge marker; full description present. This is a change from the row's recorded session, where direct requests met the bot challenge. |
| S258 nomination form | https://ich.unesco.org/doc/src/25926-EN.doc?v=1392804264 | direct plain `curl` | HTTP 200, `application/msword`, 244,736 bytes; 16 pages, 7,918 words, title `ICH-02-2009-EN-ver-03`; field D read after `soffice --headless --convert-to txt` in scratch. |

Both element pages were read directly this session, so neither row needs a Wayback route for this check. S258's source cell still records the challenge it met in round 54; a source cell is append-only, so that note is not editable in place and is left alone.

## The superseding row

Paste-ready, in the registry's 11-column shape (`corpus/SOURCES.md:28-29`):

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScoutS256Tier-1 | UNESCO Intangible Cultural Heritage, "Mask dance of the drums from Drametse" (Drametse Ngacham), Bhutan, inscribed 2008 (3.COM, decision 3.COM 1) on the Representative List, originally proclaimed 2005, element 00161 — https://ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 (direct plain request, HTTP 200, text/html, 211,091 bytes, 2026-10-22; the element page links no nomination file) | docs | B | the register entry's published summary of the Drametse Ngacham: who performs it, the shrine-to-courtyard order, the two registers of the dance, the occasion, and the benefit claimed for the audience; not the Bhutanese nomination file, not a community statement, no rule about secrecy. (tier note: B — the inscribing body's edited condensation of the State Party's file, as the same description field demonstrably rewords element 00252's form (S258); authoritative for what the register states, secondary for claims about the practice. Tier A stays with the inscription facts — year, list, decision — which this row does not claim.) | Element description ¶1 s1: "The mask dance of the Drametse community is a sacred dance performed during the Drametse festival in honour of Padmasambhava, a Buddhist guru."; ¶2 s1: "The dance features sixteen masked male dancers wearing colourful costumes and ten other men making up the orchestra."; ¶2 s2: "The dance has a calm and contemplative part that represents the peaceful deities"; ¶2 s3: "Dancers dressed in monastic robes and wearing wooden masks with features of real and mythical animals"; ¶3 s4: "For the audience, the dance is a source of spiritual empowerment" | supersedes S256 — UNESCO's element description is a condensed summary, B for practice claims, A only for inscription facts such as year and list. | mined | 2026-10-22 | 365d | corpus/knowledge/culture-material/masks-masquerade.md |

### NEW-ScoutS256Tier-1

citation: UNESCO Intangible Cultural Heritage, "Mask dance of the drums from Drametse" (Drametse Ngacham), Bhutan, element 00161, inscribed 2008 (3.COM) on the Representative List, originally proclaimed 2005.
url: https://ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161
route: direct plain request, HTTP 200, text/html, 211,091 bytes, 2026-10-22
kind: docs
tier: B — the inscribing body's edited summary of the State Party's nomination; authoritative for what the register states, secondary for claims about the practice. Same field and template as S258, whose summary I could compare against the form itself.
scope: the register entry's summary of the Drametse Ngacham — performers, shrine-to-courtyard order, the two dance registers, the occasion, the audience benefit; not the nomination file, not community statements, no secrecy rule.
quotes:
- Element description ¶1 s1: "The mask dance of the Drametse community is a sacred dance performed during the Drametse festival in honour of Padmasambhava, a Buddhist guru."
- Element description ¶2 s1: "The dance features sixteen masked male dancers wearing colourful costumes and ten other men making up the orchestra."
- Element description ¶2 s2: "The dance has a calm and contemplative part that represents the peaceful deities"
- Element description ¶2 s3: "Dancers dressed in monastic robes and wearing wooden masks with features of real and mythical animals"
- Element description ¶3 s4: "For the audience, the dance is a source of spiritual empowerment"
teaches: supersedes S256 — UNESCO's element description is a condensed summary, B for practice claims, A only for inscription facts such as year and list.
draft sentences:
- A monastery can own a mask dance outright: one monastery organizes the twice-yearly Drametse festival and sixteen masked male dancers perform with a ten-man orchestra (NEW-ScoutS256Tier-1, Element description ¶1 s2; ¶2 s1).
- A mask's first public appearance can be ordered: the dancers perform inside the main shrine before appearing one by one in the courtyard (NEW-ScoutS256Tier-1, Element description ¶2 s3).
- One dance can carry two registers, a calm part for peaceful deities and a rapid part for wrathful ones, so a single mask set may need two contrasting behaviours (NEW-ScoutS256Tier-1, Element description ¶2 s2).
- The audience is there for a stated benefit, blessings obtained by people from the village and neighbouring districts, which makes the performance a transaction and not only a spectacle (NEW-ScoutS256Tier-1, Element description ¶3 s4).
- A worldbuilder should treat this page as the register's summary, not the practice's rulebook: it names performers and order but states no rule about secrecy (NEW-ScoutS256Tier-1, tier note).

## Change line for the superseded row

Per `corpus/SOURCES.md:10-12` only `status`, `recheck` and `used-by` may change in place, and the round-50 precedent (`corpus/lessons/round-50.md:60`: S070 supersedes S060, "S060 itself is unchanged in place") keeps the superseded row intact. So the S256 change line is a no-change line, to be logged old→new in the round-55 lesson:

`S256 — status mined→mined (no change); used-by corpus/knowledge/culture-material/masks-masquerade.md (no change); recheck 365d→365d (no change) — tier A corrected to B by NEW-ScoutS256Tier-1; row unchanged in place.`

If the integrator instead moves the masks entry's two S256 citations onto NEW-ScoutS256Tier-1, the same line becomes a real change and must read:

`S256 — status mined→queued; used-by corpus/knowledge/culture-material/masks-masquerade.md→—; recheck 365d→365d.`

Do not do both halves: `mined` with an empty `used-by` is false, and `queued` while the entry still cites S256 is false the other way.

## Notes and residual risk

- **S258 needs no row.** Its tier note is verified by the form comparison above; its route note is stale (direct now returns 200) but a source cell is append-only, so this observation belongs in the round lesson, not in an edit.
- **The new row's `mined` claim needs a citation.** For `status: mined` to be true, the masks entry must cite `NEW-ScoutS256Tier-1` at least once. Either swap the two S256 citations (`corpus/knowledge/culture-material/masks-masquerade.md:62,89`) to the new id while keeping the existing locators, or leave them and downgrade the new row to `queued`.
- **Gate line for the new row**, shaped to avoid the round-54 doubled-locator and truncated-grounds defects: `- NEW-ScoutS256Tier-1 — https://ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 — accessed 2026-10-22 — element description ¶1 s1: "The mask dance of the Drametse community is a sacred dance performed during the Drametse festival in honour of Padmasambhava, a Buddhist guru." — ¶2 s1: "The dance features sixteen masked male dancers wearing colourful costumes and ten other men making up the orchestra." — ¶3 s4: "For the audience, the dance is a source of spiritual empowerment". Grounds the register-summary scope and the B tier. Seat: ScoutS256Tier.`
- **Out of scope but adjacent:** S062 and S063 are the two surviving A rows for element descriptions (their tier notes argue "UNESCO's own inscribed description"). If the lane wants one rule, those two are the next candidates for superseding rows; I did not open them this session and make no recommendation about their content.
- **Tooling:** no installs were needed; `soffice` and `pdftotext` were already present. All downloads and conversions were confined to `/fast/scratch/hyaku/kotodama-r55/ScoutS256Tier/`. Nothing in the lane was written except this report.

## unopened

- Bhutanese nomination form for element 00161 — `https://ich.unesco.org/doc/src/00161-EN.doc` and variants returned HTTP 404; `https://ich.unesco.org/doc/src/00161-EN.pdf` returned HTTP 200 but served an unrelated 2004 paper on women and intangible heritage in the Arab world (the same unrelated-page hazard S159 records for another `doc/src` path). The element page carries the text "Nomination file No. 00161" without a link. Not opened, so the S256 authorship point stays an inference.
- Wayback capture `20250807133317` of the S258 page — not needed; the direct page answered HTTP 200 this session.
- UNESCO decision 3.COM 1 for element 00161 — linked from the element page but not opened; no claim here depends on it.
