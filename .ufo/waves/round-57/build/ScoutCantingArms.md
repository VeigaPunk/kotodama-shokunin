# ScoutCantingArms — round-57 report

Seat: `KotodamaR57.ScoutCantingArms` (scout, claim C: heraldry/emblems/identity-marks entry).
Scope: canting arms (armes parlantes) — arms that pun on the bearer's name.
Result: two NEW sources, both fresh in `corpus/SOURCES.md` (grep counts 0), every quote locator-verified this session.

Installed tools: none (no installs needed; plain `urllib`/`curl` GETs only).

---

## NEW-ScoutCantingArms-1

- **citation:** Fox-Davies, Arthur Charles (1909), *A Complete Guide to Heraldry*, London: T.C. & E.C. Jack; scan by Cornell University Library, digitised by the Internet Archive, item `cu31924029796608` (stable id: https://archive.org/details/cu31924029796608).
- **url:** https://archive.org/download/cu31924029796608/cu31924029796608_djvu.txt
- **route:** direct, HTTP 200 (ordinary GET via curl; 1,868,841-byte UTF-8 OCR text).
- **kind:** book
- **tier:** A — public-domain primary treatise, opened in this session; the claim's own named source for canting arms.
- **scope:** terminology and examples of canting/allusive arms; the heredity claim of armory; badge vs rebus distinction (what is heraldic and what is not).
- **quotes:**
  - FD-1: "whereon, together with the shield and ailettes, are seven winnowing fans — another instance of canting arms"
    - `LOCATED https://archive.org/download/cu31924029796608/cu31924029796608_djvu.txt`
  - FD-2: "you assert your descent from the person to whom those arms were granted, confirmed, or allowed"
    - `LOCATED https://archive.org/download/cu31924029796608/cu31924029796608_djvu.txt`
  - FD-3: "It was the definite sign of hereditary nobility and rank, and it was practically an integral part of warfare"
    - `LOCATED https://archive.org/download/cu31924029796608/cu31924029796608_djvu.txt`
  - FD-4: "The rebus had never an heraldic status, and it had seldom more than a temporary existence"
    - `LOCATED https://archive.org/download/cu31924029796608/cu31924029796608_djvu.txt`
- **teaches:** Fox-Davies 1909 explains canting arms by example and separates inherited arms from badges and rebuses.
- **draft sentences:**
  - A canting coat makes its charges pun on the bearer's name: Sir Robert de Setvans (formerly Septvans) bore seven winnowing fans on shield, ailettes and surcoat. (NEW-ScoutCantingArms-1, FD-1)
  - Using a coat of arms asserts descent from the person to whom those arms were granted, confirmed, or allowed — the system's whole claim. (NEW-ScoutCantingArms-1, FD-2)
  - Armory was from its infancy a definite sign of hereditary nobility and rank and an integral part of warfare, so a mark doubles as family claim and battlefield identifier. (NEW-ScoutCantingArms-1, FD-3)
  - A rebus, a pictorial rendering of a name, never had heraldic status and seldom outlived a moment; unlike arms it was temporary and decorative. (NEW-ScoutCantingArms-1, FD-4)

---

## NEW-ScoutCantingArms-2

- **citation:** Canadian Heraldic Authority, Office of the Governor General of Canada, *Public Register of Arms, Flags and Badges of Canada*, registration of James Turner (Thunder Bay, Ontario), 20 November 2025, Vol. VIII, p. 452; page id https://www.gg.ca/en/heraldry/public-register/project/3810.
- **url:** https://www.gg.ca/en/heraldry/public-register/project/3810
- **route:** direct, HTTP 200 (ordinary GET; one transient HTTP 403 on a rapid re-fetch, succeeded on retry with backoff).
- **kind:** record
- **tier:** A — an official grant record, opened this session, containing the formal blazon and the authority's own symbolism statement.
- **scope:** one contemporary granted canting coat: blazon wording, the symbolism paragraph naming the pun, registration metadata (date, volume/page, grantee).
- **quotes:**
  - C-1: "Azure an anchor between two Catherine wheels in pale between two pallets Or"
    - `LOCATED https://www.gg.ca/en/heraldry/public-register/project/3810`
  - C-2: "The wheels are a pun on the surname Turner, which originally referred to a person who turned mill wheels"
    - `LOCATED https://www.gg.ca/en/heraldry/public-register/project/3810`
- **teaches:** The Canadian Heraldic Authority's register presents a granted canting coat, its blazon, and the authority's own statement of the pun.
- **draft sentences:**
  - The official record blazons James Turner's canting arms as "Azure an anchor between two Catherine wheels in pale between two pallets Or". (NEW-ScoutCantingArms-2, C-1)
  - The registering authority itself states the pun: the wheels allude to the surname Turner, originally a person who turned mill wheels. (NEW-ScoutCantingArms-2, C-2)
  - The blazon names the tinctures, the charges and their placement, while a separate symbolism paragraph records why each charge was chosen. (NEW-ScoutCantingArms-2, C-1)
  - The register entry dates the arms (20 November 2025, Vol. VIII, p. 452) and names the grantee and city, so the design is anchored to a holder and moment. (NEW-ScoutCantingArms-2, C-2)

---

## Rejected

- College of Arms (`college-of-arms.gov.uk`): homepage served a "Bot Verification" reCAPTCHA to a plain GET — challenge met, not passed; no quote taken. (Would have needed a Wayback capture; not needed given CHA record.)
- `www.canada.ca`: plain GET timed out on read (network); the CHA register is served from reachable `gg.ca` instead.
- `www.ox.ac.uk`, `www.parliament.uk`, `www.bridgwater-tc.gov.uk`: HTTP 403 to plain GET.
- `www.castinestyle.ca` (guessed public register mirror): DNS NXDOMAIN.
- Woodward & Burnett (1892), *A Treatise on Heraldry, British and Foreign*, item `treatiseonherald00wooduoft` — opened (djvu.txt), quote locator-verified ("Plate XL, fig. 5, is the well-known coat of STEWART, or STUART, in Scotland : Or, a fess chequy azure and argent"), but dropped to keep this seat's two-source scope; Fox-Davies 1909 carries the treatise slot.
