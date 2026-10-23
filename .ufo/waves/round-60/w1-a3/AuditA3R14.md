# AuditA3R14 — pre-freeze wording audit, ids S644, S645, S646

Scope: `grep -n '\bS64[456]\b' /fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md` → candidate lines 39 (S644), 40 (S645), 131 (S646), 132 (S645), 139 (S646). SOURCES rows: `corpus/SOURCES.md` lines 599, 600, 601 (working tree). All three quotes locate under the lane locator (`reopen-quote.py` `normalise`, NFKC + casefold) — verified locally on the fetched bytes.

Fetches (ordinary means, literal URLs, into /fast/scratch/hyaku/kotodama-r60a3/AuditA3R14/):
- S644 `https://prm.web.ox.ac.uk/files/amuletspdf` → HTTP 200, 449,625 bytes, application/pdf → pdftotext → s644.txt
- S645 `https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx` → HTTP 200, 84,952 bytes, text/html → tag-stripped → s645.txt
- S646 `https://asianethnology.scholasticahq.com/article/149559.pdf` → HTTP 200, 287,476 bytes, application/pdf → pdftotext → s646.txt

---

AUDIT S644 REWRITE

Page evidence: quote is verbatim body text of the leaflet introduction (pdftotext lines 20–26): "An amulet is defined by the Oxford English Dictionary as: 'Anything worn about the person as a charm preventative against evil, mischief, disease, witchcraft, etc.' The definition of charm is very similar: 'Anything worn about the person to avert evil or ensure prosperity', though a charm may also be a spell or incantation believed to have a magical power." — body prose, not heading/caption/nav. Teaches cell ("the museum's own working definition of amulet and charm, quoted from the OED, and its caveat that not every ritual object is one") is carried: the quote itself and the following page sentence "Some of the objects on display are technically not amulets or charms…" carry both halves.

Defect in candidate line 39: the clause "a charm can also be a spoken spell" adds the qualifier "spoken" — the page says "a spell or incantation believed to have a magical power" (an incantation is spoken, a spell need not be). Under the support-seat rule "no added … attribute", the narrowed "spoken spell" is NOT carried by the page. Everything else on the line is carried: "worn about the person as a charm preventative against evil, mischief, disease or witchcraft" matches the OED quote (the dropped "etc." makes the list read exhaustive but does not add content — low residual risk, flag only).

old: - A museum leaflet adopts the dictionary sense: an amulet is anything worn about the person as a charm preventative against evil, mischief, disease or witchcraft, and a charm can also be a spoken spell (S644). **B**
new: - A museum leaflet adopts the dictionary sense: an amulet is anything worn about the person as a charm preventative against evil, mischief, disease or witchcraft, and a charm can also be a spell or incantation believed to have a magical power (S644). **B**

---

AUDIT S645 OK

Page evidence: quote is verbatim body text, second paragraph: "The amulet is an object with natural magical properties, whereas a talisman must be charged with magical powers by a creator; it is this act of consecration or 'charging' that gives the talisman its alleged magical powers." — body prose.

Line 40 "A university museum separates the pair by where the power comes from: an amulet is an object with natural magical properties, while a talisman must be charged with power by its creator" — every clause rests on S645 and is carried: "object with natural magical properties" verbatim; "charged with magical powers by a creator" → "charged with power by its creator" is entailed (a creator is its creator); "separates the pair by where the power comes from" is the "whereas" contrast itself. Attribution "a university museum" matches the page (AUB Archaeological Museum). No universal, no added comparison/cause/date/place.

Line 132 "The charging creator: a talisman must be charged with magical powers by a creator" — verbatim subset of the quote. OK.

Teaches cell ("how a university museum splits amulet from talisman by the origin of the power, and what that split does to who may make the object") is carried: the split is verbatim; "who may make the object" is implied by "must be charged … by a creator". No over-reach.

---

AUDIT S646 OK

Page evidence: quote locates on PDF p. 251 (pdftotext lines 482–484), section "The changing world of amulet makers": "The ritual masters empower mass-produced amulets in their own temples and sell them to clients for from twenty thousand to fifty thousand VND." — body prose of the article, not caption/nav. Casefold in normalise reconciles registry "Vnd" vs page "VND".

Line 131 "The ritual market: in Vietnam, ritual masters empower mass-produced amulets in their own temples and sell them to clients for twenty to fifty thousand dong" — every clause carried: verbatim core; "in Vietnam" is the article's scope (keywords "Vietnam—amulet—popular religion"; fieldwork Hanoi/Bắc Ninh/Bắc Giang, line 486 "in Vietnam today"); "dong" = VND (page line 115 "Vietnamese dong"); "twenty to fifty thousand" = "from twenty thousand to fifty thousand". The price is what masters charge clients (preceding sentence distinguishes the 2,000–2,500 VND purchase price) — the line claims only the selling price. No over-reach.

Line 139 "Mass production: ritual masters empower mass-produced amulets in their own temples and sell them to clients" — verbatim subset minus price. OK.

Teaches cell explicitly scopes to "as observed at Hanoi ritual masters' workshops …; not the whole of Vietnamese popular religion" — honest scope, no over-reach.

---

Residual risk: S644's dropped "etc." from the OED list (harmless — list is presented as the dictionary's, not exhaustive); S645 teaches cell's "who may make the object" is implication, not verbatim (fine — teaches is not judged verbatim). No heading/caption/cookie/promo/nav quotes among the three. Installs: none.
