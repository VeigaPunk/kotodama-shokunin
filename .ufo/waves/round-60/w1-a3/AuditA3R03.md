NONE-MET

# AuditA3R03 — pre-freeze build attack: S608, S609, S610

Axes: depth; clause-level source entailment; body-quote fidelity; reproducible access; minimal correction without changing citation identity.

Scope: reviewed every candidate-entry line citing these three ids and their complete working-tree registry rows. This is a build audit, not a control receipt: no fixture, counter, probe, judgment runtime or data seat was run. NONE-MET does not establish counter resistance. No candidate or registry edit was made.

Object: `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md`, SHA-256 `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`.

All three first URLs reopened by ordinary curl GET with literal URLs, without challenge bypass. Live pages succeeded; no Wayback fallback was necessary. Cached response bodies and headers are under `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R03/`. Using the lane's `reopen-quote.py` `row_target`, `to_text`, `normalise` and `locate_in` on these downloaded bytes located all three registry quotes. Locator SHA-256: `64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8`.

## AUDIT S608 TEACHES

URL: https://islamicart.museumwnf.org/database_item.php?id=object;EPM;qt;Mus22;21;en

Fetch evidence:

```text
source=S608 status=200 bytes=33124 final=https://islamicart.museumwnf.org/database_item.php?id=object;EPM;qt;Mus22;21;en
```

Response SHA-256: `4ea613b8c256e5142ba777dbdb077dcfad6f8b914f861525e618ae7af801f8cc`.

The quoted anchor is verbatim prose in **Description**, not a heading, caption, navigation, cookie or promotional text; `locate_in=True` (23 normalized words):

> Jewish silversmiths in Morocco became known for casting and engraving pieces such as this one, used as a talismanic doorknob or jewellery pendant.

The preceding body sentence establishes that the pieces are hands:

> This object represents the "Hand of Fatima" also known as Khamsa (the Arabic word for "Five"), "Hand of Venus" or "Aphrodite".

**Registry defect:** the teaches cell adds a physical suspension claim, **hung**, which the description does not establish. A hand piece fixed as a doorknob, rather than suspended, is consistent with the quoted account. Jewellery-pendant use does not establish how the door version is mounted. Searches of the locator-extracted live page found zero occurrences of `hung` or `hanging`; the positive body evidence says only `used as`.

teaches old: Moroccan Jewish silversmiths cast and engraved hand-shaped amulets that hung as talismanic doorknobs or were worn as jewellery pendants.

teaches minimal supported wording: Moroccan Jewish silversmiths cast and engraved hand-shaped pieces used as a talismanic doorknob or jewellery pendant.

**Entry defect, candidate line 96:** `at once` additionally suggests simultaneous placement. The source expressly offers alternative uses (`or`); it does not establish one object occupying door and body simultaneously.

old: - Door and body at once: Moroccan Jewish silversmiths cast and engraved hand pieces used as a talismanic doorknob or a jewellery pendant (S608). **B**

new: - Door or body: Moroccan Jewish silversmiths cast and engraved hand pieces used as a talismanic doorknob or a jewellery pendant (S608). **B**

**Other citing line, 128:** unchanged; the body sentence above carries makers, Morocco, becoming known, casting, engraving and hand pieces:

> - The craft maker: Jewish silversmiths in Morocco became known for casting and engraving talismanic hand pieces (S608). **B**

Impacted axes: depth/source entailment; source-record integrity. Both wording defects are fixable before freeze, but **do not silently edit the historical teaches cell**: SOURCES.md lines 9–12 permit only status/recheck/used-by changes in place and require a superseding row for a correction. The declared entry-id set also fixes S608. If the teaches defect is accepted, the integration owner must resolve that append-only/fixed-id constraint explicitly before freeze; changing the entry rubric alone does not repair the teaches claim. This audit neither changes that contract nor decides admission.

## AUDIT S609 REWRITE

URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/

Fetch evidence:

```text
source=S609 status=200 bytes=112796 final=https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/
```

Response SHA-256: `b2143d589179da3b7f1b62c4bdda9a22133cf6ddc70855fea9182ed394916846`.

The registry quote is verbatim **Abstract** prose, not its heading or any caption/navigation/promo/cookie fragment; `locate_in=True` (18 normalized words):

> In Arabic cultures, the Hamsa is a palm-shaped amulet that is popular in jewelry and wall hangings.

The immediately following sentence is:

> It is a symbol of protection against evil.

These carry Arabic-cultural context, palm shape, amulet identity and popularity in the two display forms. The teaches cell stays within that evidence:

> The palm-shaped hamsa amulet is popular in Arabic cultures both as jewellery and as a wall hanging.

**Counterexample:** different objects can display the same Hamsa design as jewellery and as wall hangings, without one physical amulet protecting both locations or a wall hanging protecting its room. The page's designation as a protective symbol does not supply that extra spatial/effectiveness claim. The live page has no `room` or `covers` occurrence; the relevant positive evidence is exactly the two sentences above.

Only citing line, candidate line 98:

old: - Body and wall: in Arabic cultures the palm-shaped Hamsa amulet is popular in jewelry and in wall hangings, so the same amulet covers a person and a room (S609). **B**

new: - Body and wall: in Arabic cultures the palm-shaped Hamsa amulet is popular in jewelry and in wall hangings (S609). **B**

Smallest safe correction: remove the unsupported concluding inference while preserving the bullet structure, supported placements and S609. Impacted axis: depth/source entailment. This is an entry-wording defect, not a quote or teaches failure.

## AUDIT S610 OK

URL: https://www.myjewishlearning.com/article/mezuzah/

Fetch evidence:

```text
source=S610 status=200 bytes=295561 final=https://www.myjewishlearning.com/article/mezuzah/
```

Response SHA-256: `93bf989f05702b310fb2f4d64a0f5cccf263c33ecc4f8d3ec7c8c4aa78841586`.

The registry quote is a verbatim substring of ordinary prose under **Is the Mezuzah an Amulet?**, not the heading itself or promotional/navigation/cookie/caption text; `locate_in=True` (13 normalized words). Full carrying sentence:

> Partly as a result of this lettering, partly because some people naturally tend toward superstition, the mezuzah sometimes has been accorded the status of amulet, a magical charm.

The teaches cell is supported by that scoped account:

> Popular custom has sometimes classed the mezuzah as an amulet, a magical charm.

Placement is independently carried by prose under **Where and When to Hang a Mezuzah**:

> A mezuzah should be fixed to the doorpost of every living space in the house, not just the entrance door.

The ritual instructions also state:

> Immediately the mezuzah is nailed or glued to the right doorpost.

For the line-42 framing of disagreement within the Jewish tradition, the article contrasts the popular attribution above with its own explicit instruction:

> A mezuzah is not meant to be a protective device, nor lack thereof a source of direct punishment.

> A mezuzah is a sign and reminder of the Covenant, of our love and commitment and our willingness to create a Jewish household.

Both citing lines therefore remain within the page's claims:

> - The words are disputed inside one tradition: the mezuzah on a Jewish doorpost has sometimes been accorded the status of an amulet, a magical charm, by popular custom (S610). **B**

> - Doorpost: the mezuzah, fixed on the doorpost, has sometimes been treated as an amulet, a magical charm (S610). **B**

No correction proposed. The lines preserve `sometimes` and report classification, not actual protective efficacy.

## Operational bounds

No installs or updates. No delegation, background jobs, git/jj writes, counter execution or support-seat contact. All shell commands ran under the assigned sandbox and were timeout-capped; Python used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`. All started commands completed. Only this report was written in the lane. No S648–S651 or round-59 mapped-id finding is asserted: those ids were outside this seat's assignment.
