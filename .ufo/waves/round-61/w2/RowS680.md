# Row S680 — one-row one-clause review (round 61, wave 2 falsify)

## Scope
- URL reviewed: `https://cplorg.contentdm.oclc.org/digital/api/singleitem/collection/p4014coll10/id/836` (CONTENTdm single-item JSON; HTTP 200, `application/json`, 3949 bytes, fetched live 2026-10-23 UTC; no archive capture needed).
- Quoted passage: "A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs."
- Clause: "A Serbian child's pair of opanci has soles attached to the uppers with knotted leather thongs."

## QUOTE — LOCATED
The `descri` (Description) field of the item record reads verbatim:
> "A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs. The shoes have buckled straps and turned up toes."

The quoted sentence is the first sentence of that Description field — the substantive body text of the item record (a museum catalog description, not navigation chrome and not a truncated caption fragment; it is a complete grammatical sentence carried verbatim on the item's record page). Exact byte-for-byte match including the comma splice construction "shoes, their soles".

## CLAUSE — SUPPORTED
Every part of the clause is carried by the record:

- "Serbian" — `title`: "Serbian Shoes, Child's (Opanci)"; reinforced by `subjec`: "Folk art--Serbia; Ethnic costumes--Serbia".
- "child's" — `title`: "Serbian Shoes, Child's (Opanci)".
- "opanci" — `title`: "(Opanci)"; `identi`/`filena`: "241-36802_Serbian shoes, child's (opanci).jpg".
- "pair of ... shoes" and "soles attached to the uppers with knotted leather thongs" — `descri` verbatim.

≥10 consecutive words of page text carrying the clause:
> "A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs."
(17 words; plus the title string "Serbian Shoes, Child's (Opanci)" supplying the Serbian / child's / opanci attributes.)

Nothing added: the clause asserts no date, no place beyond the "Serbia" the record itself gives, no cause, no comparison, no universal quantifier, and removes no hedge (the source contains none — the Description states the construction flatly). The clause is a faithful join of the record's Title and Description fields.

## Evidence excerpt (verbatim JSON field values)
- title: "Serbian Shoes, Child's (Opanci)"
- subjec: "Folk art--Serbia; Ethnic costumes--Serbia"
- descri: "A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs. The shoes have buckled straps and turned up toes."
- locati: "Cleveland Public Library. Fine Arts and Special Collections Department."

No installs performed; live fetch by `read` tool and plain `curl` (HTTP 200).

QUOTE S680 LOCATED
CLAUSE S680 SUPPORTED
