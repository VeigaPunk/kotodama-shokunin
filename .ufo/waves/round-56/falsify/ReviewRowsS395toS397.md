# ReviewRowsS395toS397

**Verdict: actionable findings: S395's recorded capture does not support its artist credit; S396 has a wrong quote locator and a hedge-stripping entry sentence; S397's entry narrows the object's date range. The remaining checked quotes, tiers, cited entry claims, and Gate/teaches equality carry.**

- S395 anchor 1 and Gate quote — CARRIED — “collaborative creations of Kongo sculptors and ritual specialists” (Met capture 20210208082447, essay ¶1; 8 words; also present in the later capture 20230308010409).
- S395 anchor 2 — CARRIED — “identified with Mangaaka, the preeminent force of jurisprudence” (Met capture 20210208082447, essay ¶1; 8 words).
- S395 anchor 3 — CARRIED — “Its crowning element is the distinctive mpu headdress worn by chiefs or priests.” (Met capture 20210208082447, essay ¶2; 13 words).
- S395 anchor 4 — CARRIED — “They document vows sealed, treaties signed” (Met capture 20210208082447, essay ¶2; 6 words).
- S395 tier — CARRIED — A is scoped to the holding museum's exact object essay and its own attribution; its note says “authoritative for the Met's description and attribution.”
- kongo-kingdom.md:90 — CARRIED — “They document vows sealed, treaties signed” (S395 essay ¶2); the entry attributes the jurisprudence and metal-record claims to the Met.
- round-56.md:60 Grounds — CARRIED — It exactly matches the S395 teaches cell in SOURCES.md:424.
- SOURCES.md:424 citation/teaches — UNSUPPORTED at the recorded route — the 20210208082447 capture's object details say “Kongo peoples, Yombe group” and do not credit an artist/nganga; a later ordinary Wayback capture, 20230308010409, has the title “Kongo artist and nganga, Yombe group” and retains all four anchor quotes. Exact correction: `Wayback capture 20210208082447` -> `Wayback capture 20230308010409`; `artist credited as Yombe-Kongo artist and nganga` -> `artist credited as Kongo artist and nganga, Yombe group`; update the matching teaches/Grounds phrase `The Met credits a Yombe-Kongo artist with an nganga` -> `The Met credits a Kongo artist and nganga from the Yombe group`.

- S396 anchor 1 and Gate quote — CARRIED — “This work was the product of an intense collaboration between a sculptor and the initiated priest” (Met capture 20230529091312, essay ¶1; 16 words).
- S396 anchor 2 — CARRIED — “may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels” (Met capture 20230529091312, essay ¶1; 14 words).
- S396 anchor 3 — CARRIED — “The cross alludes to the division between the land of the living and the land of the dead” (Met capture 20230529091312, essay ¶2; 18 words).
- S396 anchor 4 — WRONG-LOCATOR — “Knots and the act of tying are associated with the binding and capturing of a spirit.” (Met capture 20230529091312, essay ¶3, the “Cloth and tied bundles” block; 16 words), not the fourth paragraph. Exact correction: `essay, fourth paragraph` -> `essay, third paragraph`.
- S396 tier — CARRIED — A is scoped to the Met's own description of this held object; the tier note says “authoritative for the Met's description.”
- kongo-kingdom.md:89 — OVER-READ — the Met says the term “may relate to a wide spectrum of physical receptacles” (S396 essay ¶1), but the entry removes that hedge and states the term “covers” them. Exact replacement: `The Met says the term covers cloth packets and filled vessels as well as carved wood (S396, essay, first paragraph).` -> `The Met says the term nkisi may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, and carved wood sculptures (S396, essay, first paragraph).`
- round-56.md:61 Grounds — CARRIED — It exactly matches the S396 teaches cell in SOURCES.md:425.

- S397 anchor 1 and Gate quote — CARRIED — “Zimpu (singular: mpu) are intricately knotted caps worn by men in parts of Central Africa.” (Cleveland API, Description, object 1997.180; 15 words).
- S397 anchor 2 — CARRIED — “Ringed with leopard claws, this long cap (mpu ngola) once belonged to a high-status man” (Cleveland API, Description; 15 words).
- S397 anchor 3 — CARRIED — “the fierce feline attachments alluded to his personal qualities, as both were seen as leaders in their domains” (Cleveland API, Description; 18 words).
- S397 anchor 4 — CARRIED — “Known since at least 1607 in the former Loango Kingdom, as well as the adjacent Kongo Kingdom” (Cleveland API, Description; 17 words).
- S397 tier — CARRIED, scoped — A fits the museum's own catalog data, naming, and reading for this cap; the tier note explicitly says broader history is “the museum's summary, not a primary account.” Do not treat it as an independent historical study.
- kongo-kingdom.md:16 — CARRIED — the API Culture field says “Kongo-style maker, possibly Yombe subgroup”; the entry retains “possibly.”
- kongo-kingdom.md:97 — OVER-READ — the API dates this object “late 1800s–early 1900s,” not only late 1800s. Exact correction: `a late-1800s cap` -> `a late-1800s–early-1900s cap`.
- round-56.md:62 Grounds — CARRIED — It exactly matches the S397 teaches cell in SOURCES.md:426.

**Unrun checks:** LSP status/references/definition/diagnostics; `read xd://lsp` returned “No such tool” (only `ast_edit` and `debug` are mounted). Grep was used only to locate citations; source and entry judgments above come from the opened text. No tools were installed.