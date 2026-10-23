NONE-MET

# AuditA3R01 — pre-freeze wording audit

Scope: S600, S601, S603 only. This is build criticism, not a support-seat verdict or a judgment of claim D. No control fixture or counter was run; NONE-MET does not assert that any counter rejected a fixture.

Axes: **depth** (declared claim D: every cited clause is source-carried); **calibration** (belief versus fact, source scope, faithful attribution); **freshness** (ordinary reopening). The latter two are diagnostic axes, not additional round claims.

Read the declaration first. Candidate audited: `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md`, SHA-256 `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`. Assigned rows were read from the lane's working-tree `corpus/SOURCES.md:555-558`; all matching entry lines were found with `\bS(?:600|601|603)\b`. None is a multiple-id line. S648–S651 and their round-59 mapping are outside this assignment.

## Ordinary reopening receipts

All requests were plain curl GETs with literal URLs, a 100-second request limit, an outer 120-second timeout, and a 25,000,000-byte cap. No challenge was solved; each inaccessible live page was followed by its registry-listed capture. Full stdout from the six fetches:

```text
S600 live HTTP=403 bytes=5595 url=https://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html
S601 live HTTP=429 bytes=34225 url=https://www.metmuseum.org/art/collection/search/566845
S603 live HTTP=200 bytes=212 url=https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf
S600 capture HTTP=200 bytes=11240 url=https://web.archive.org/web/20141126174231id_/http://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html
S601 capture HTTP=200 bytes=212855 url=https://web.archive.org/web/20250125005512id_/https://www.metmuseum.org/art/collection/search/566845
S603 capture HTTP=200 bytes=16579613 url=https://web.archive.org/web/20240703133613id_/https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf
```

The S600 live body is Cloudflare's “Just a moment...” page. S601 is “Vercel Security Checkpoint.” S603's HTTP 200 is **not a PDF or article**: its Content-Type is text/html and its 212-byte body has an Incapsula script and an empty body. All three listed captures actually carry the relevant source text. In particular, a successful status alone would falsely establish S603's live accessibility.

Artifacts: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R01/` holds the fetched bodies, headers, extracted text, request manifest, and `locate-captures.py`. HTML went through the lane locator's `to_text`; PDF text through `pdftotext -layout`. The lane locator's unmodified `locate_in` and `normalise` then checked the three exact registry quotes. Observed stdout:

```text
S600 canonical-locate_in=True normalised-quote-words=17
S601 canonical-locate_in=True normalised-quote-words=22
S603 canonical-locate_in=True normalised-quote-words=20
```

The locator file's SHA-256 was `64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8`. This checks quote location, not the semantic support of every clause; that audit follows.

## AUDIT S600 OK

Page used: [UCL Digital Egypt, listed 2014 capture](https://web.archive.org/web/20141126174231id_/http://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html), HTTP 200, 11,240 bytes.

Every citing line (candidate line 38):

```text
- Egyptology's narrow sense: amulets are items worn to protect their wearer by their religious associations, a religious equivalent to armour, and in Egyptology the word amulet is generally reserved for bodily adornments of unambiguous religious form or context (S600). **B**
```

Page evidence, first body paragraph, capture HTML lines 26–34:

> Amulets are items worn to protect their wearer by their religious associations, a religious equivalent to armour.

This carries worn objects, protection of the wearer, religious association, and the armour comparison. The same paragraph ends:

> In Egyptology the word amulet is therefore generally reserved for bodily adornments of unambiguous religious form or context.

This carries the disciplinary limitation, “generally,” bodily adornment, and the unambiguous form/context condition. “Narrow sense” summarizes that expressly stated restriction; it does not universalize the definition across traditions.

Registry teaches: “UCL's Digital Egypt page defines an amulet as worn protection whose force comes from religious association.” This is carried by the first sentence. The registry's quoted sentence is verbatim body prose after whitespace normalization, not the separate “Amulets” heading, navigation, caption, or promotional material. No correction identified.

## AUDIT S601 TEACHES

Page used: [Met object 566845, listed 2025 capture](https://web.archive.org/web/20250125005512id_/https://www.metmuseum.org/art/collection/search/566845), HTTP 200, 212,855 bytes.

Every citing line (candidate line 84):

```text
- Shape as power: an amulet in the shape of the wedjat eye, the healed eye of Horus, was thought to protect its wearer and to transfer the power of regeneration onto him or her (S601). **C**
```

The **entry line is source-carried**. The object-description paragraph at capture HTML line 531 states:

> One of the most popular amulets in ancient Egypt, the wedjat eye represents the healed eye of the god Horus.

and:

> An amulet in this shape was thought to protect its wearer and to transfer the power of regeneration onto him or her.

The first sentence carries identity and the healed-eye clause; the second carries shape, protective function, regenerative transmission, and the essential **was thought to** qualification. The registry quote is this second sentence verbatim, inside the object's `<div ... itemprop="description"><p>` body, not a heading, image caption, navigation, or promo.

The defect is in the registry teaches cell, which drops that qualification:

old: `The Met's record says a wedjat-eye amulet of this form guarded its wearer and carried regenerative power.`

new: `The Met's record says a wedjat-eye amulet of this form was thought to protect its wearer and to transfer the power of regeneration.`

Counterexample: “was thought to protect ... and to transfer” reports a belief in both effects, not demonstrated guarding or power transmission. “The Met's record says” attributes the assertion to a source but does not preserve the source's attribution to belief. The strongest counter-reading is that the original teaches intended ordinary shorthand for traditional amuletic function; the paragraph also says “The wedjat eye embodies healing power and symbolizes rebirth.” Under the assigned strict no-hedge-to-fact rule, however, the specific protection-and-transfer sentence supplies an explicit qualifier that the teaches should retain.

Impacted axes: depth and calibration. This is a fixable wording defect, not a reason to delete the entry line or its id. **Do not silently edit the existing teaches cell:** the registry's append-only contract permits in-place changes only to status, recheck, and used-by. L1 must route a compliant correction before freeze, accounting for D's exact-id predicate if a superseding row is required. This seat neither changes that predicate nor authorizes a registry exception.

## AUDIT S603 OK

Page used: [Said 2020, listed 2024 PDF capture](https://web.archive.org/web/20240703133613id_/https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf), HTTP 200, 16,579,613 bytes.

Every citing line (candidate lines 49 and 57):

```text
| the same demon, answered directly | a palm-sized amulet provides protection from the Mesopotamian demon Lamashtu | S603 (B) |
- A palm-sized amulet could itself provide protection from the demon Lamashtu, so the protective object may be small enough to keep in the hand (S603).
```

Page evidence: opening body paragraph, p. 101, extracted text lines 248–256:

> Among the various figurines, pendants, and fragments of cuneiform ritual tablets in The Metropolitan Museum of Art’s collection of ancient Near Eastern art is a nearly pristine obsidian amulet of the first millennium b.c.

> This amulet, small enough to fit in the palm of one’s hand, provides protection from the Mesopotamian demon Lamaštu.

> On one side is a representation of the demon surrounded by various ritual paraphernalia (fig. 1), and on the other, a ritual incantation carved in cuneiform script (fig. 2).

The second sentence carries the amulet's palm size and its protection from this named Mesopotamian demon. The immediately following sentence identifies the representation of that same demon; together these carry the table's “same demon, answered directly” label. Neither entry line asserts that every Lamaštu amulet has this size or mechanism. “A ... could” / “may be small enough” draws the existential size conclusion from this one stated example, not a universal rule or an actual holding practice.

Registry teaches: “A palm-sized amulet provides protection against the Mesopotamian demon Lamashtu.” This tracks the quoted body sentence. “Lamashtu” is the entry's diacritic-free rendering of “Lamaštu,” not a different demon. The quote locates in the running first paragraph; it is not the adjacent figure caption. No correction identified.

## Handoff

Finding: one strict belief-scope teaches defect (S601); no entry-line replacement recommended for the three assigned ids. All three registry quotes locate and are body text. The live S603 response is a false-positive HTTP success, but its listed capture is reachable and supports the audited content.

No source, candidate, declaration, counter, or integration file was edited. Only this report was written in the lane. No git/jj writes, delegation, background jobs, browser, or alternate judgment runtime. No tool installs or updates. All finite shell calls returned; own scratch measured 16,984,262 bytes, below the 200 MB cap.
