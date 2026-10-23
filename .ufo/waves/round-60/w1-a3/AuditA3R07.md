NONE-MET

# AuditA3R07 — pre-freeze build wording attack

Scope: S621, S622, S624 only. This is build-review evidence, not a support-seat verdict or canonical claim judgment. No counter fixtures or ACCEPT-D-60 runs were assigned or executed; NONE-MET records no met control in this scoped audit, not a counter-soundness finding.

Axes: **depth** (the declared axis: complete source entailment); calibration risk is noted where wording is stronger than its source. Quote provenance, clause coverage, and preservation of source identity are audit dimensions, not additional round claims.

Read claims.json first. Searched every occurrence of the three ids in L1/candidate-entry.md and their complete registry rows. All six citing lines are covered below; none has a second source id. Opened all three first-listed live URLs with the read tool and independently captured each with ordinary curl GET, bounded by timeout and size. No access challenge occurred; no archive fallback was needed. The lane's reopen-quote.py to_text/locate_in/normalise functions locate all three quoted spans in the captured HTML. All three quotes are article body text, not headings, captions, navigation, cookies, or promotion.

## AUDIT S621 OK

Page: https://www.provanhall.org/exhibitions — **HTTP 200; 229010 bytes**. Section “Witches' Marks”, Lauren McCarthy's body paragraph beginning “Upon further investigation”.

Registry quote, verbatim body sentence:

> Witches’ marks were a common form of ritual protection in which symbols or patterns were carved into the stonework or woodwork of historic buildings.

This carries every substantive clause of candidate line 102: the common ritual-protection practice; symbols/patterns; carving; stonework/woodwork; historic buildings. The entry repeats this sentence with straight apostrophes and a bullet label. The registry teaches cell's carved marks, stone/timber, and ritual-defence characterization are carried by this sentence and the next:

> They are usually found at the thresholds of buildings to prevent witches and evil spirits from entering, thus protecting inhabitants and visitors from harm.

No claim is made in this entry line that the particular Provan Hall marks are certainly apotropaic; the page's uncertainty about identifying those particular marks therefore does not contradict the line. No rewrite requested.

## AUDIT S622 OK

Page: https://museum.wales/blog/1203/Witch-bottles-and-healing-charms/ — **HTTP 200; 88910 bytes**. The relevant body paragraph is under **“Conjurers or dynion hysbys”**, not the registry anchor's stated “Witch-bottles and pots”. This is an anchor-location defect, not an absent or non-body quotation.

Verbatim body evidence:

> People who had been bewitched could also carry out their own counter-magic rituals by placing sharp objects like thorns and pins inside a bottle, which was usually filled with the victim's urine. It was then sealed and boiled over the fire or buried under the hearthstone. This was believed to torment the witch into revealing her identity, thereby breaking the spell. The bottle symbolised the witch's bladder, and so the sharp objects were believed to cause her much pain.

The last sentence is the registry's exact quote. Together these sentences carry the teaches cell: witch's-bladder symbolism, sharp contents, sealing, and intended pain to the witch. Candidate line 72's bladder correspondence, sealed sharp contents, and believed pain are all present. Candidate line 104's sealed contents, believed effect on the witch, and bladder correspondence are also all present. “Welsh” in line 72 is grounded in the article's opening “In Wales it was a common practice” and the surrounding Welsh conjurer discussion. The entry preserves belief language rather than asserting effective magic. No entry rewrite requested. Record the anchor-location discrepancy through the registry's authorized correction process, not an unlogged in-place edit.

## AUDIT S624 TEACHES

Page: https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 — **HTTP 200; 17563 bytes**. Evidence is the article's **Text** table cell, HTML line 269, not its title or image captions.

Verbatim body sentences:

> Shinsatsu are a type of thaumaturgic talisman (also known as gofu) distributed at shrines and symbolic of a spiritual being or its supranormal power.

> The term is generally used to refer to the relatively large kind of amulets enshrined in kamidana, or affixed above gates, on doors and pillars, or on ceilings.

The registry quote locates and is body text. **The teaches cell itself changes the source's disjunction to a conjunction**:

old teaches: A shrine-issued talisman called shinsatsu is understood as a symbolic token of a spiritual being and its power.

source-carried teaches wording: A shrine-issued talisman called shinsatsu is understood as a symbolic token of a spiritual being or its supranormal power.

Counterexample to entailment: the source permits symbolism of the supranormal power without asserting that the talisman also symbolizes the being. The current teaches and candidate line 41 assert both. This is not a quote-location failure and not cured by changing the entry alone.

Candidate line 41 also repeats that conjunction. Minimal source-only replacement removes the additional geographical gloss and restores “or”:

old: - A shrine talisman in Japan, shinsatsu (also called gofu), is distributed at shrines as a symbolic token of a spiritual being and its supranormal power (S624). **B**

new: - A shrine talisman, shinsatsu (also called gofu), is distributed at shrines as a symbolic token of a spiritual being or its supranormal power (S624). **B**

Candidate line 107 changes the source's distinct placement relations, “above gates, on doors and pillars, or on ceilings”, to “above gates, doors, pillars or ceilings”. Read literally, that licenses placement above doors/pillars/ceilings rather than the placements this page states. “Household” is also an explanatory gloss not supplied by this article's definition of kamidana. Preserve the id and bullet structure while matching the page:

old: - Shrine talisman in the house: shinsatsu, distributed at shrines, may be enshrined in a household kamidana or fixed above gates, doors, pillars or ceilings (S624). **B**

new: - Shrine talisman placement: shinsatsu, distributed at shrines, may be enshrined in a kamidana or affixed above gates, on doors and pillars, or on ceilings (S624). **B**

Candidate line 130 needs no rewrite: “The shrine: shinsatsu are distributed at shrines” is explicitly carried by the first quoted sentence. The synonyms shinsatsu/gofu and shrine distribution in line 41 are carried too.

**Smallest safe correction / integration constraint:** restore the source disjunction and exact placement relations; preserve the source page and all three citing lines. The existing S624 teaches cell still requires an authorized registry correction. CORPUS.md's append-only rule does not permit silently editing that cell, while the declared exact-id set retains S624. This is a pre-freeze compatibility issue for the integration owner, not an instruction to alter the predicate, drop an id, silently mutate a row, or deem the defect harmless. Entry-only narrowing does not resolve a TEACHES failure. No lane content was changed by this seat.

## Reopening evidence

Saved bodies and response headers are under /fast/scratch/hyaku/kotodama-r60a3/AuditA3R07/. Curl used literal source URLs, followed redirects, and reported the same effective URLs. Canonical locator probe: timeout 40 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/AuditA3R07/locate-quotes.py; exited successfully; locate_in=True for all three, with 24/19/24 normalized quote words respectively.

| id | body bytes | body SHA-256 |
|---|---:|---|
| S621 | 229010 | 500655159f3a4c6ad7423867c34d61e45516d05528b89b91cf3586029b5cd4db |
| S622 | 88910 | 03662b65c421656db45961dd07b11270406c4cc9ba01d1c809a85b63507f551b |
| S624 | 17563 | 2fd9a0b22a71b13edbac487ed6ad2ee10ccf946429c91b06140d95ed0dfaf739 |

Installs/updates: none. No background jobs, delegated seats, git/jj writes, candidate edits, or registry edits. S648–S651 rejection comparisons are outside this assignment.
