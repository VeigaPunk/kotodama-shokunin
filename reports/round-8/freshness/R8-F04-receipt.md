# R8-F04 — Melqart / *mlqrt* freshness receipt (round 8)

- **id**: R8-F04 · **prior row**: R6-07-A (`unresolved`) · **entry**: `corpus/knowledge/civilizations/levant-canaan-phoenician.md` (§4 bullet 1 — line 76 at retrieval, now line 79 after the round-8 metadata frontmatter pass; sha256 at retrieval `0af3cbff…9812`, current `a2c548aa…` — frontmatter-only change by the M-shard, claim text unchanged)
- **designated source_url**: https://en.wikipedia.org/wiki/Melqart (re-fetched live) · **prior ledger**: `corpus/lessons/round-6-sources/07.json`
- **result (raw worker label)**: `partial-support` — reconciled dispositions live in `reports/round-8/freshness/reconciliation.json`
- **accessed**: 2026-10-17, session ~20:12–20:16 UTC (clock readings 20:14:39Z / 20:15:30Z / 20:16:32Z)

Tested claim (line 76): *"The name mlqrt, conventionally Melqart, is understood as 'king of the city'; its civic semantics are more productive than assigning the god the modern job 'patron of merchants' alone (Bonnet 1988)."*

## Passages retrieved (primary first)

**P1 — Primary inscription, KAI 201 (Melqart / Bir-Hadad stele, Aramaic).** [m-saunders.com](http://m-saunders.com/bir-hadad-stele-melqart-stele/) (specialist page quoting Hackett & Wilson-Wright 2022, SAOC 73, p. 108), locator: sections *Text* / *Translation*.

> "The statue which Bir-Hadad, son of ˁAttar-sumkī, Bir-Guš, king of Aram, set up [šm, line 1] for his lord, for Melqart, which he [Bir-Hadad] had vowed to him [Melqart], because he [Melqart] heard his [h, line 5 = Bir-Hadad's] voice."

Supports: epigraphic attestation of *mlqrt* addressed as "his lord" by an Aramaean king (~late 9th/early 8th c. BCE; Hackett–Wilson-Wright assign 790–760). Does **not** evidence Tyrian civic institutions (Aramaic context; WiBiLex gives the same caution). Corroborating relay: [Wikipedia, "Melqart stele"](https://en.wikipedia.org/wiki/Melqart_stele) — same five-line formula, object now National Museum of Aleppo, AO 8185.

**P2 — Primary inscription, KAI 47 / CIS I 122 (Cippe de Malte, Phoenician–Greek bilingual, 2nd c. BCE).** [Louvre collection record AO 4818](https://collections.louvre.fr/en/ark:/53355/cl010165603), locator: *Inscriptions* field.

> Phoenician: "A notre Seigneur Milqart, Maître de Tyr, qu'ont dédié … ton serviteur 'Abd'osir et son frère 'Osirshamar … car il a écouté leur voix, qu'il les bénisse". Greek: "Dionysos et Sérapion les fils de Sérapion, Tyriens, à Héraklès l'archégète."

Supports: the *bʿl ṣr* ("lord of Tyre") civic formula on a primary object, and *interpretatio graeca* as a translation act (Heracles *archegetes*). Late date forbids projecting its setting backward. Corroborating relay: [Wikipedia, "Cippi of Melqart"](https://en.wikipedia.org/wiki/Cippi_of_Melqart) gives the Phoenician text `lʾdnn lmlqrt bʿl ṣr`.

**P3 — Scholarly philological passage, WiBiLex "Melqart".** [die-bibel.de](https://www.die-bibel.de/ressourcen/wibilex/altes-testament/melqart) (erstellt Januar 2018), locator §1 first paragraph; §2; §4.

> "Der Name Melqart müsste nach der phönizischen Schreibung *mlqrt* eigentlich Milqart vokalisiert werden. Es handelt sich bei ihm um eine Kontraktion von *mlk* „König" und *qrt* „Stadt". Er bedeutet also „Stadtkönig"."

Also: earliest name attestation only to ~800 BCE (KAI 201); ~20 Mediterranean inscriptions link Melqart with Tyre (*mlqrt bʿl ṣr*); KAI 47 as "ihrem Herrn Melqart von Tyrus" vs Greek "Herakles, dem Gründer"; Melqart among the oath gods of the Hannibal–Philip V treaty (Polybius 7,9). Profile: "Gott der Stadt Tyrus, des (dortigen) Königtums sowie der Erneuerung". City-variation: "Erstaunlich dürftig sind indes die Zeugnisse eines Melqart-Kultus in Karthago". Author line not exposed in retrieval (limit).

**P4 — Peer-reviewed passage, Euphrosyne 45 (2017).** [Fernández Camacho, RODIN PDF](https://rodin.uca.es/bitstream/handle/10498/38777/J.EUPHR.5.125169.pdf?sequence=1), locator §2 opening (p. 44).

> "The main god worshipped in the city of Tyre was the Semitic god Melqart, a name derived from the roots mlk and qrt ("King of the City"). He had several known facets, such as being the protector of royalty, a solar god, a resurrection god, and later, with the rise of Western colonization, a god of seafaring…"

**P5 — Designated URL re-fetch, Wikipedia "Melqart" (tertiary).** [en.wikipedia.org/wiki/Melqart](https://en.wikipedia.org/wiki/Melqart).

> "Edward Lipinski theorizes that it was derived from MLK QRT (𐤌𐤋𐤊 𐤒𐤓𐤕 Mīlk-Qārt), which means "King of the City"." — ref Lipiński 2002, p. 235 (unchanged relay). Merchant framing still only as an Aubet relay: temple to Melqart "as protector of Tyrian traders".

## Access failures (commands + status)

- **melqart.huma-num.fr** — `curl -sS -o /dev/null -w … --max-time 25 http://melqart.huma-num.fr/` → `curl: (6) Could not resolve host`, HTTP 000, exit 6; FetchURL: `getaddrinfo ENOTFOUND`. **Second consecutive round.** Wayback probe `archive.org/wayback/available` → "Internet Archive services are temporarily offline" (2026-10-17).
- **livius.org/articles/religion/melqart/** — `curl … -w "%{http_code}"` → **HTTP 404** (second round).
- **Lipiński 2002 p. 235** — archive.org advancedsearch `creator:(Lipinski) AND title:(Semitic Languages)` → `numFound: 0` (during archive.org outage window). Page still unread.
- **Bonnet 1988** — HAL API `halId_s:hal-01853704` → record exists, **no `fileMain_s`/`files_s`** (metadata only). Book still unread.

## Passage support vs whole-claim support

- **Passage support**: both legs of line 76 are now covered by fresh retrievals — etymology stated directly by WiBiLex (scholarly) and Euphrosyne 45 (peer-reviewed), not only the Lipiński relay; civic semantics witnessed on two primary inscriptions; the anti-fixing leg supported as calibrated absence (no retrieved source fixes a merchant-patron job; the trader-protector wording appears once, via the Aubet relay).
- **Whole-claim support**: `partial-support` — the entry's named authority (Bonnet 1988) and Lipiński's page remain unread, so the attribution itself is unverified end-to-end; nothing retrieved contradicts the claim.

## Limits and open questions

1. Bonnet 1988 unread (metadata-only HAL record; no accessible edition found in the sweep) — the book-level upgrade stays open.
2. Lipiński 2002 p. 235 unread; archive.org outage limits this session's sweep.
3. KAI 201 is Aramaic, its date and royal identity are disputed — use only for the god's cross-regional standing and the "lord" votive formula.
4. KAI 47 is 2nd-c.-BCE Malta — the civic title in late use, not evidence for earlier Tyrian institutions.
5. WiBiLex author unnamed (extraction/grep could not expose the author line).
6. Search sweep (5 queries, listed in the JSON) found no accessible full text of Bonnet 1988 or Lipiński's page; snippets were used only for discovery.
7. Entry-hash drift mid-round: the M-shard's frontmatter pass changed the entry file hash (`0af3cbff…` → `a2c548aa…`, 3 frontmatter insertions per `git diff`); the tested sentence is unchanged and was re-grepped after the pass.
