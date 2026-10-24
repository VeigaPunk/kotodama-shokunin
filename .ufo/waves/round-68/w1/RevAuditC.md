# RevAuditC — report (round 68 residual, attempt 2, 2026-10-24)

Seat: L1-kotodama-r68-attempt2.RevAuditC. Assignment: rule on pending supersedes chains S130>S119, S131>S122, S133>S097, S186>S157 (claims.json frozen_sets.CHAIN_PAIRS), modeled on rows/AuditChain8/audit.md. Full ruling file: .ufo/waves/round-68/rows/RevAuditC/audit.md. No registry or entry edits were made; every edit below is specified for the L1 (bounded to the frozen MUTABLE set and citation-sites map).

## Rulings

1. **S130>S119 — activate, repoint.** Live PMC6818964 (HTTP 200, 175,558 B) serves the authors' *reply*, not the keynote S119 claims: no abstract, reply headings ("Points of agreement", "What we did not claim", …), "As we noted in our original article" verbatim; Crossref separates this 938–944 record (DOI …585) from the same-title 886–905 keynote (DOI …724). The cutoff caveat serves verbatim: "across L2 AoA studies, the cutoff points … span nearly a decade: age 12 … and age 20" — S130's "the 12–20 cutoffs … come from second-language studies" is exact. Edit: sign-languages-manual-modality.md:209 `(S119)` -> `(S130)`; S130 queued->mined + used-by, S119 mined->queued.

2. **S131>S122 — activate, repoint.** Live Springer and the BMC mirror both serve a 3,038-byte "Client Challenge" page (browser UA; europepmc 403) — recorded honestly; the anchor verifies via the Wayback capture of the same URL (441,963 B): article type "Commentary" (tier A->B repair justified) and Background ¶1 verbatim: "(In writing deaf , it is common convention to use a capital \"D\" when talking about communities that use a sign language as their major language, and \"d\" when talking about auditory status.)" — exactly S131's scope and the entry's :212 claim. Edits: :212 `(S122)` -> `(S131)`; :7 and :9 shelf enumeration `**S071–S122** and **S126**` -> `**S071–S122**, **S126** and **S131**`; S131 queued->mined + used-by, S122 mined->queued.

3. **S133>S097 — activate, repoint.** Live CSLDS module 7 (HTTP 200, 94,879 B) has exactly one structural heading (the module title); "Type 1/2/3" and "References" are `<strong>` paragraph labels; "Dominance Condition" appears only in prose — S097's anchor names sections the page does not have, S133's anchor cell is verbatim-accurate. Content-as-S097 confirmed: "Out of the 45 possible handshapes in ASL, only 7 can appear as the passive hand…", "A, S, B, 5, G (i.e., 1), C and O", "95.9% and 87% of Type 3 signs adhere to the Dominance Condition (Channon 2004)". Edits: :87 and :92 `(S097)` -> `(S133)`; S133 queued->mined + used-by, S097 mined->queued.

4. **S186>S157 — retire, cell-flip.** The correction is an access note only (content as S157, identical anchors). On 2026-10-24 the live UNESCO element URL serves the full anchor verbatim (HTTP 200, 155,823 B, zero challenge markers: "replicates the islanders' habitual language (Castilian Spanish) with whistling", "more than 22,000 inhabitants", "two distinct whistles replace the five Spanish vowels…", "Inscribed in 2009 (4.COM)"), and S186's Wayback capture (20260204103108, 158,701 B) is content-identical — the 2026-10-22 captcha premise no longer holds, so the row repairs nothing. Rejecting S186 settles the chain SETTLED-RETIRED and keeps the five speech-surrogates citations (:170,:171,:173,:179,:181) on the live-verifiable row. No entry edits.

Net: 4/4 chains ruled, all settle (pending contribution 0); 6 entry citation-site edits + 2 shelf-enumeration edits specified; registry mutations bounded to the eight chain ids.

## Residual risk / verification gaps

- S157's third anchor locator ("metadata block 'Biomes: Mountains'") no longer matches the element page's design (only a sidebar browse link remains; capture identical) — not repairable by any chain in this round; noted in the audit for a future recheck.
- S131's anchor is currently re-verifiable only through the Wayback capture (publisher challenge-walled); future rechecks of S131 should say so.
- S130 ruling rests on PMC `<p>` paragraph numbering (PoA ¶2, LM ¶6); PoA ¶1 carries the consensus sentence, so a consumer quoting ¶1 instead of ¶2 still lands on served text.

## Tooling

No tools installed or upgraded (operator directive 2026-10-19 record): used system curl and python3 only; pacman untouched per the 2026-10-20 pause.
