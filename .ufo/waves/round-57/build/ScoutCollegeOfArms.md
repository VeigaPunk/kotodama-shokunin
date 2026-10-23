# ScoutCollegeOfArms — the College of Arms (London): who grants, who may apply, arms are not surnames

- seat: `KotodamaR57.ScoutCollegeOfArms` (scout, claim C ground: heraldry, emblems and inherited identity marks)
- round: kotodama 57 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `0314aa981071220d206760b5263467faeea05b60`, declaration `13226c18aa352e3f3d1bfbe567f221acfb8b8344`
- assignment: the College of Arms official site (college-of-arms.gov.uk) — who grants arms in England, Wales and Northern Ireland, who may apply, and the statement that arms belong to an individual, not to a surname; quote the official pages, aimed at worldbuilder design decisions.
- rows: this seat files two rows, `NEW-ScoutCollegeOfArms-1` (Granting of Arms page) and `NEW-ScoutCollegeOfArms-2` (FAQs: heraldry page). The L1 assigns final `S` ids in S413-S480 at integration.
- access date for every source below: 2026-10-22
- no tools installed.

## Route summary

| source | file actually read | route |
|---|---|---|
| Granting of Arms | `http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms` | Wayback capture `20251031191334` of the live page; read via plain `curl` GET, text extracted by stripping HTML tags |
| FAQs: heraldry | `http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs` | Wayback capture `20251010095509` of the live page; same method |

**Challenge met, not passed.** The live pages were tried first by ordinary GET: the `read` fetcher of `https://www.college-of-arms.gov.uk/services/granting-arms` returned HTTP 200 with a "Bot Verification — Verifying that you are not a robot..." interstitial (the URL was not solved or routed around by any tool); a plain `curl` GET with a desktop User-Agent returned 200 once and then flapped to TLS failures (`curl` exit 35, status 000). `https://www.college-of-arms.gov.uk/about` is HTTP 404 (no such path). Both pages were therefore read through Wayback captures, which the round's locator sanctions; no challenge was passed.

## Verification

- Every quote below carries its pasted locator line: 16 quotes offered, 16 `LOCATED` (each fetched live this session by `python3 -B reports/round-57/reopen-quote.py '<url>' '<quote>'`).
- Freshness legs: `grep -c 'college-of-arms' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` prints `0`; `grep -c 'web.archive.org/web/20251031191334' ...` prints `0`; `grep -c 'web.archive.org/web/20251010095509' ...` prints `0`.
- Wayback operational note for the L1: `web.archive.org` reset connections (locator `URLError`) under bursts of concurrent locator runs and again immediately after the burst; after a ~40 s backoff all runs passed when issued serially with pauses. Locate legs on these rows should be re-run serially, not 8-at-once.
- Locator interaction note for the L1: the locator normalises hyphens in URLs, so any quote containing the literal trigram "College of Arms" is refused as `url-reflects-quote` against every URL on this host. No quote below contains it; keep drafted anchor quotes free of the phrase "College of Arms" for these rows.
- No source below was already registered (both host and capture-id greps 0). Nothing opened was rejected as redundant; rejections are route-level and listed at the end.

---

### NEW-ScoutCollegeOfArms-1

citation: College of Arms (London). "Granting of Arms," Services section, college-of-arms.gov.uk, page captured 31 October 2025. Wayback capture id 20251031191334.

url: http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms

route: Wayback capture id 20251031191334 (live page met a bot-verification interstitial and flapped TLS on plain GET — challenge met, not passed; capture fetched by plain GET).

kind: web

tier: A — the heraldic authority's own operational statement of who grants arms, on whose authority, through whom one petitions, and what the grant consists of; exactly the rule-set the entry needs for the European arms section.

scope: who grants (Kings of Arms, letters patent, Crown authority); the petition/memorial route through the Earl Marshal; discretionary eligibility criteria; fee-setting by Earl Marshal's Warrant; territorial scope for corporate applicants with Scotland and Canada named as separate authorities; corporate grant history from 1439; blazon as the governing description; badges as the mark others may wear, including on garments. Not a source for Scottish, Canadian or Irish practice itself, cadency, or medieval origins.

quotes:
- Granting of Arms, opening paragraph: "Arms and crests, badges and supporters, are granted by letters patent issued by the most senior heralds, the Kings of Arms"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- Granting of Arms, opening paragraph: "They act according to powers delegated to them by the Crown and all grants are therefore made under Crown authority"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- Petitioning for Arms: "The first step in applying for a grant of arms is to submit a petition, or memorial as it is called, to the Earl Marshal"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- Petitioning for Arms: "There are no fixed criteria of eligibility for a grant of arms"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- Corporate Arms: "must be registered or situated in England, Wales, Northern Ireland, or in another territory or country of which The King is Head of State"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- The Design of the Arms: "but by the concise verbal description of them in the text, known as the blazon"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- Badges: "While arms and crest are personal to their bearers the badge may be used by others wishing to show connection or allegiance"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`
- Badges: "it is appropriate for the employees of a company to wear a tie bearing the company's badge, but not the company's arms"
  `LOCATED http://web.archive.org/web/20251031191334/https://www.college-of-arms.gov.uk/services/granting-arms`

teaches: English grants of arms issue as letters patent from the Kings of Arms under Crown authority, petitioned through the Earl Marshal, with blazon governing each grant's form.

draft sentences:
- Grants are an act of delegated authority: arms, crests, badges and supporters are granted by letters patent issued by the Kings of Arms, who act on powers delegated by the Crown, so a fictional realm should name the office that holds the granting power and speaks for the crown (NEW-ScoutCollegeOfArms-1, Granting of Arms, opening paragraph).
- Access runs through a named gatekeeper, not a form: the first step is a petition, called a memorial, submitted to the Earl Marshal and drafted by an officer of arms, which gives stories a courtier between applicant and grant (NEW-ScoutCollegeOfArms-1, Petitioning for Arms).
- Eligibility is discretionary and achievement-weighted: the page states there are no fixed criteria, but Crown awards or honours, civil or military commissions, degrees, professional qualifications, public and charitable service and eminence or good standing are taken into account — so bearing a grant can mark standing rather than birth (NEW-ScoutCollegeOfArms-1, Petitioning for Arms).
- The authority is territorial, and neighbours with their own heralds are named as exceptions: a corporate applicant must be registered or situated in England, Wales, Northern Ireland or another territory of which The King is Head of State, with Scotland and Canada excepted as holders of their own heraldic authorities (NEW-ScoutCollegeOfArms-1, Corporate Arms).
- The verbal description, not the painted shield, is the law of the grant: once granted, the form is governed not by the painting on the letters patent but by the concise verbal description called the blazon, so one blazon may be correctly rendered in many artistic styles (NEW-ScoutCollegeOfArms-1, The Design of the Arms).
- Badges are the mark designed for other people to wear: arms and crest are personal to their bearers, while the badge may be used by others to show connection or allegiance — employees may wear a tie bearing the company's badge but not its arms (NEW-ScoutCollegeOfArms-1, Badges).

---

### NEW-ScoutCollegeOfArms-2

citation: College of Arms (London). "FAQs: heraldry," Resources section, college-of-arms.gov.uk, page captured 10 October 2025. Wayback capture id 20251010095509.

url: http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs

route: Wayback capture id 20251010095509 (same live-site bot-verification interstitial — challenge met, not passed; capture fetched by plain GET).

kind: web

tier: A — the authority's own FAQ refuting the two most common outsider over-reads (surname arms; "crest" = whole achievement) and stating transmission rules in plain terms; ideal counterweight for the entry's "where popular accounts over-read" passages.

scope: the surname statement and grant to one person plus male-line descendants; the right to arms by grant or descent; Crown deputation and jurisdiction of the Kings of Arms; the crest as helm-top object; women bearing and transmitting arms as quarterings; cadency marks as historical and now little used. Not a source for blazon vocabulary, ordinaries, tamgas, kamon, or non-hereditary office emblems.

quotes:
- Q. Do coats of arms belong to surnames?: "There is no such thing as a 'coat of arms for a surname'. Coats of arms are inherited in the male line"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. Do coats of arms belong to surnames?: "a coat of arms is granted or confirmed to one person and their descendants in the legitimate male line"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. Do coats of arms belong to surnames?: "must either have had it granted to them or be descended in the legitimate male line from a person to whom arms were granted"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. How do I seek a new coat of arms?: "The Kings of Arms are deputed by the Crown to make grants of new arms to individuals and corporate bodies within their jurisdiction"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. What is a crest?: "It is a popular misconception that the word 'crest' describes a whole coat of arms or any heraldic device. It does not"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. What is a crest?: "A crest is a specific part of a full achievement of arms: the three-dimensional object placed on top of the helm"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. Can women bear arms?: "Yes, a woman can bear arms by inheritance or by a grant of arms to herself"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`
- Q. What are cadency marks?: "Despite still appearing in heraldic text books this system is little used in modern heraldry"
  `LOCATED http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs`

teaches: The College states arms belong to individuals by grant or male-line descent, not surnames, that crests are only the helm-top object, and that cadency marks are now little used.

draft sentences:
- The surname trap is named and closed in one line: there is no such thing as a 'coat of arms for a surname', because a coat of arms is granted or confirmed to one person and their descendants in the legitimate male line — an outsider's popular account that sells "family arms" over-reads from the start (NEW-ScoutCollegeOfArms-2, Q. Do coats of arms belong to surnames?).
- A right to arms has two gates only: the holder must either have had it granted to them or be descended in the legitimate male line from a person to whom arms were granted, so inheritance is a provable chain rather than a name shared with strangers (NEW-ScoutCollegeOfArms-2, Q. Do coats of arms belong to surnames?).
- The grant is a deputation with a defined jurisdiction: the Kings of Arms are deputed by the Crown to make grants of new arms to individuals and corporate bodies within their jurisdiction, which lets a worldbuilder bound each heraldic authority by territory and by whom it serves (NEW-ScoutCollegeOfArms-2, Q. How do I seek a new coat of arms?).
- Keep the word crest precise: the page calls it a popular misconception that 'crest' means the whole achievement — a crest is the three-dimensional object placed on top of the helm, one part among several an outsider tends to conflate (NEW-ScoutCollegeOfArms-2, Q. What is a crest?).
- Transmission is not male-only: a woman can bear arms by inheritance or by a grant to herself, and female grantees and heraldic heiresses pass their arms on as a quartering to their descendants under the laws of arms (NEW-ScoutCollegeOfArms-2, Q. Can women bear arms?).
- Treat cadency as a fossil, not a rule in force: the system of small temporary marks showing a son's place among his brothers, though still printed in heraldic text books, is described as little used in modern heraldry, family members tending to bear arms undifferenced (NEW-ScoutCollegeOfArms-2, Q. What are cadency marks?).

---

### Rejected

- live `https://www.college-of-arms.gov.uk/services/granting-arms` — "Bot Verification" interstitial ("Verifying that you are not a robot...") served to the plain fetch; not solved, not bypassed; routed to Wayback capture `20251031191334`. Subsequent plain `curl` GET flapped to TLS failure (exit 35). Reported as challenge met, not passed.
- live `https://www.college-of-arms.gov.uk/about` — HTTP 404; no such page (the About material sits under "About Us" paths not needed for the assigned statements).
- Wayback CDX domain query (`web.archive.org/cdx/search/cdx?url=college-of-arms.gov.uk&matchType=domain`) — returned no rows; the FAQs page was located via the availability API and the capture page's own navigation instead.
- Any quote containing the literal phrase "College of Arms" (e.g. the FAQ answer on clan matters naming Lord Lyon) — unusable on this host because the locator refuses URLs carrying three consecutive quote words once hyphens normalise (`college-of-arms` → "college of arms"). Excluded before filing, not a fetch failure.
- `collegeofarms.euclid.int` (EUCLID page "Grant of Arms / Obtain a Coat of Arms") — surfaced in discovery search, is not the College of Arms, and was not opened or used.
