NONE-MET

# AuditA3R11 — pre-freeze build attack

Assigned ids: S634, S635, S636. Axes: **depth** (source-to-proposition entailment), with calibration and operability affected by an over-strong teaches cell or inaccessible evidence. This is a wording audit, not a support-seat verdict or canonical judgment. No control fixture or ACCEPT-D-60 counter was run; no PASS is claimed. No installs, delegation, background jobs, lane edits other than this report, or other runtime invocation.

Registry schema was checked: `scope` and `teaches` are separate columns (`corpus/SOURCES.md:28`); the packet reads `teaches`, not `scope` (`reports/round-60/accept-d.py:536-539`). All four candidate lines citing these three ids were examined. None has a second id, so all its factual clauses rest on the assigned source. No S648-S651/round-59 mapping is assigned here.

## AUDIT S634 OK

Page: https://booksalongthesilkroads.library.utoronto.ca/items/show/2415

Plain GET: **HTTP 200; 15,015 bytes**. Saved as `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R11/S634.html`; SHA-256 `82ea5ef24ef530f6dd05713877c422b2f46c6b108bbdbfbdd2b301d0efa5107e`.

The registry quote is a verbatim substring of the **Description field's prose**, not its heading, title, image caption, navigation, cookie or promotional text. Canonical `to_text`/`locate_in` on the fetched bytes: `literal_quote=True locate_in=True`.

Exact candidate lines:

```text
- Worn scroll: an Ethiopian amulet scroll inscribed with healing prayers, talismans and images of armed angels might be placed in a leather case to be worn (S634). **B**
- Prayers and angels: an Ethiopian amulet scroll is inscribed with healing prayers, talismans and images of armed angels (S634). **B**
```

Body evidence, covering every clause:

> Used for protection against illness, difficult childbirth, and the evil eye, this Ethiopian amulet scroll (Amharic, kitab; Arabic for 'book') was created by an ordained minister (Amharic, debtara) from pieces of parchment tailored to the height of the owner's body.

> Inscribed with healing prayers, talismans, and images of armed angels, amulet scrolls like this one might be placed in a leather case to be worn or hung on a wall, and could also be wrapped around the body of the deceased as a form of prayer.

The first sentence supplies Ethiopian/object identity. The second supplies prayers, talismans, armed angels and the **possible**, not compulsory, leather-case/worn placement. It also carries the actual teaches cell: `An amulet scroll carries healing prayers, talismans and armed angels, and can travel in a leather case worn on the body.` No universal or new mechanism is added. Keep both entry lines and the teaches cell.

Ancillary metadata distinction: the separate **scope** cell says `the leather case, wall or shroud that receives it`. The page says the scroll can wrap around the deceased's **body**, not that a shroud receives it. That is not a teaches/entry defect under the stated packet check. If this metadata is touched before freezing, the smallest accurate scope-only substitution is `its possible placement in a leather case, on a wall or around the body of the deceased`; do not misreport this as a failure of the actual teaches cell.

## AUDIT S635 OK

Live page: https://journal.thewalters.org/volume/78/note/ethiopian-manuscripts/

Ordinary `read` returned the article through content negotiation (`text/markdown`). Separately, a plain curl GET returned **HTTP 403; 5,555 bytes**, `Just a moment...`, with `cf-mitigated: challenge`. No challenge was solved or bypassed. The listed capture was then opened by an ordinary GET:

https://web.archive.org/web/20260712234731id_/https://journal.thewalters.org/volume/78/note/ethiopian-manuscripts/

Listed capture: **HTTP 200; 168,444 bytes**. Saved as `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R11/S635-wayback.html`; SHA-256 `2f4dccede7d24b22f9c1d4bd2a6216374da2dcc14f93bf80fece8711be8587c9`. It carries the full relevant article paragraphs; the evidence below is independently present in those saved capture bytes, not inferred from the successful live reader.

Exact candidate line:

```text
- Ink: the inks of Ethiopian healing scrolls often contained unusual materials, intended to make the prayers more effective and to ward off evil spirits (S635). **B**
```

The quote is a complete **body paragraph sentence** under Writing Inks, not the section heading or a caption:

> The inks of healing scrolls often contained several unusual materials, intended to make the prayers more effective and to ward off evil spirits.

The following body sentences clarify the materials and purpose:

> For example, some recipes included the horn of a black sheep and the hair of a black goat for black ink, while the bones of bulls were used for brown ink.

> Red inks used to write important words and the name of the client might contain the sap of ritual plants or drops of blood from the animal sacrificed to make the parchment in order to increase the magic powers of the scroll.

The article's Ethiopian setting and healing-scroll identity are explicit in its introduction and body:

> In preparation for Ethiopia at the Crossroads, a major exhibition of ancient to contemporary Ethiopian art that was on view at the Walters Art Museum and two other venues from 2023 to 2024, technical research was undertaken on sixty-seven Ethiopian manuscripts in the collection that date from the early fourteenth to the early twentieth century.

> Healing or magic scrolls (kǝtab) were made of long, vertically oriented strips of parchment that were sewn together, written with special prayers and painted on one side with figurative images and magical talismans.

Every entry clause is carried: Ethiopian scope, healing-scroll inks, **often** rather than universally, unusual ingredients, intended prayer-strengthening and intended warding. The actual teaches cell, `The inks of healing scrolls held unusual materials meant to strengthen the prayers against evil spirits.`, retains intention rather than asserting efficacy. The article's later warning that most collected recipes are modern does not contradict this undated, non-universal sentence; do not add an ancient/traditional recipe claim. Keep the entry and teaches.

Canonical `to_text`/`locate_in` on the listed capture: `literal_quote=True locate_in=True`. Operational caution only: retain the listed Wayback URL in the packet so ordinary access does not depend on the live site's challenge behavior.

## AUDIT S636 TEACHES

Page: https://diskoproject.kelsey.lsa.umich.edu/object/stomach-amulet/

Plain GET: **HTTP 200; 200,383 bytes**. Saved as `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R11/S636.html`; SHA-256 `21c3bd543223d92ad39996cc8b804071ddb9bc765ab1dbef5014414171f1d1bc`.

The registry quote is a complete **Description body sentence**, not a heading, caption, navigation, cookie or promotional text. Canonical `to_text`/`locate_in`: `literal_quote=True locate_in=True`.

Exact candidate line:

```text
- Stone with a figure: the Kelsey Museum reads the lion-headed serpent on a steatite Chnoubis amulet as the amulet's protective nature, associated with both the Egyptian god Chnum and the Greek god Agathodaimon (S636). **B**
```

Body evidence:

> The Chnoubis amulet showcases a lion-headed serpent facing left.

> The lion-headed snake design embodies the strength of a lion and solar attributes from Egyptian mythology.

> It represents the amulet’s protective nature, associated with both the Egyptian god Chnum and the Greek god Agathodaimon.

The Object Information prose/fields identify inventory `1963.04.0008` and material `Steatite`. This covers the candidate's object identity, stone/material, image, protective reading and **association with both** named gods. The entry line itself needs no change.

Counterexample: **association with two gods is not a statement that those gods are joined to one another.** The actual teaches cell strengthens the relation from the page's `associated with both` to `joining ... with ...`; a strict blind reader can reject the teaches even though the entry and quote are supported. No sentence in the complete Description supplies the asserted joining/fusion. This is a fixable pre-freeze calibration/depth defect, not an unavoidable axis tradeoff.

Smallest safe correction — change only the teaches cell, preserve S636 and the candidate line:

old: The Kelsey entry reads the lion-headed serpent on this steatite Chnoubis amulet as the object's protective force, joining the Egyptian god Chnum with the Greek Agathodaimon.

new: The Kelsey entry reads the lion-headed serpent on this steatite Chnoubis amulet as the object's protective force, associated with both the Egyptian god Chnum and the Greek god Agathodaimon.

The separate scope cell also says `the Egyptian Chnum joined to the Greek Agathodaimon`; if corrected in the same pre-freeze pass, replace that phrase with `its association with both the Egyptian god Chnum and the Greek god Agathodaimon`. The **teaches** replacement above is the packet-facing correction; the scope wording is not a second packet authority.

## Exercised quote-location evidence

Command (completed; exit 0):

```text
timeout 30 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/AuditA3R11/locate-assigned.py
```

It loads only the lane locator's existing functions and checks the three fetched local bodies; it does not fetch, run a counter or modify lane files. Full stdout:

```text
S634 file=S634.html bytes=15015 literal_quote=True locate_in=True quote_words=25
quote: Inscribed with healing prayers, talismans, and images of armed angels, amulet scrolls like this one might be placed in a leather case to be worn
S635 file=S635-wayback.html bytes=168444 literal_quote=True locate_in=True quote_words=23
quote: The inks of healing scrolls often contained several unusual materials, intended to make the prayers more effective and to ward off evil spirits.
S636 file=S636.html bytes=200383 literal_quote=True locate_in=True quote_words=19
quote: It represents the amulet’s protective nature, associated with both the Egyptian god Chnum and the Greek god Agathodaimon.
```

Conclusion: retain all four assigned candidate lines and all three ids. Narrow S636's teaches from joining the gods to association with both before freezing. No source quote is a disallowed heading/caption/promo/cookie/navigation fragment. No process remains running.
