NONE-MET

# AuditA3R13 — pre-freeze build attack

Scope: S640, S641, S642 only; completed 2026-10-23T07:05:49Z. This is a wording/source audit, not a support-seat verdict or a canonical claim judgment. No control fixture, probe, or ACCEPT-D-60 counter was run, so the first line does not claim that controls were exhausted.

Axes: **depth** — body-quote fidelity, teaches entailment, every cited entry clause, preservation of attribution and evidential uncertainty. Ordinary retrievability is also a prerequisite under FETCH-60, not a new claim axis.

Reviewed candidate: `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md`, SHA-256 `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`. Registry read: `corpus/SOURCES.md:595-597`, whole-file SHA-256 at inspection `53b5a5f293cdf4199e7db1b8fc42d37bea4b4d830e1d9c375c50dcfad2028fca`. The grep-tool searches were `\bS64[012]\b` on the candidate and `^\| S64[012] ` on the registry; all matches were inspected.

## AUDIT S640 TEACHES

**Counterexample:** the article describes one particular Kerala/Kochi object and its intended use. The teaches cell generalizes to Kerala birth amulets and converts intended use into an unqualified protective result. The current packet also has a concrete reachability defect: its only listed URL returned 403, and the accessible archive found below is **not listed in S640**.

Current teaches:

> Birth amulets from Kerala guarded women against infertility and against the death of an infant.

Smallest source-scoped teaches text:

> An amulet from Kerala, Kochi was used to guard against both infertility and infant death.

### Fetch and body evidence

- Listed live URL: <https://jwa.org/blog/fromthearchive/archive-amulet-protection-pregnant-women-and-newborn-children>. Ordinary curl: **HTTP 403, 118 bytes**; the read tool independently returned HTTP 403. Saved response: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R13/S640.html`; it contains only a Forbidden page, not the article.
- No Wayback URL appears in this registry row. Archive availability API returned **HTTP 429, 117 bytes**; no article evidence was inferred from that response.
- Ordinary Wayback nearest-capture retrieval succeeded and redirected to <https://web.archive.org/web/20250106130507id_/https://jwa.org/blog/fromthearchive/archive-amulet-protection-pregnant-women-and-newborn-children>: **HTTP 200, 70,383 bytes**. The read tool also opened that exact resulting capture. Saved HTML: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R13/S640-archive.html`, SHA-256 `93017614b486ee7e9cd390f99de6737759f173a5a40b309c14843e1f36b1d81b`.
- Body under **What we found**, saved HTML line 877: “This elaborately detailed amulet from Kerala, Kochi was used to guard against both infertility and infant death.” This is the registry's quoted sentence, not the preceding image caption. It supports the object's detail, Kerala/Kochi attribution, and both intended protective purposes.
- Next body paragraph, line 878: “One thing that makes this paper object unique within the Posen Library are the visible fold marks. The page is creased. These creases indicate that the person or people who used the amulet folded it up so that it was small enough to carry around or hold onto.” This carries the folding and portability clauses, as an interpretation of physical traces.
- The later body generalizes Jewish newborn-protection traditions across communities, but does not establish that Kerala birth amulets generally had both of this object's purposes. It calls the Kerala object an example, not a universal.

### Every citing line

Line 51:

```text
| infertility and infant death | an amulet from Kerala, Kochi was used to guard against both infertility and infant death | S640 (B) |
```

Supported directly by the first quoted body sentence; no change needed.

Line 59 removes “was used to” and thereby loses the source's intended-use framing. Minimal correction, retaining its structure and id:

old:
```text
- A detailed amulet from Kerala, Kochi guarded against both infertility and infant death (S640).
```
new:
```text
- A detailed amulet from Kerala, Kochi was used to guard against both infertility and infant death (S640).
```

Line 108 has the right object, purposes and portability, but should preserve how the article knows about folding:

old:
```text
- Carried and folded: the Kerala amulet was folded up so that it was small enough to carry around or hold onto, and it was used to guard against both infertility and infant death (S640). **B**
```
new:
```text
- Carried and folded: the JWA article says the Kerala amulet's creases indicate that users folded it small enough to carry around or hold onto, and it was used to guard against both infertility and infant death (S640). **B**
```

The anchor locates in the archive using the lane's `to_text`/`locate_in`; it does not locate in the live Forbidden response. No anchor-as-heading/caption/navigation/promo issue was found. The archive is useful pre-freeze evidence, but a later confined reader may use only packet URLs: the currently unlisted archive cannot silently rescue that reader's failed live fetch.

## AUDIT S641 TEACHES

**Counterexample:** the museum says these amulets **are worn as protection** and that their appearance **was thought** to divert the glance. The teaches cell instead states that they protected wearers. Its origin hedge is retained, but its protective-effect hedge/purpose is not.

Current teaches:

> Horned-hand amulets, held to come from ancient Italy, protected their wearers from the Evil Eye's harmful glance.

Smallest source-scoped teaches text:

> Horned-hand amulets, thought to be of ancient Italian origin, are worn as protection against the Evil Eye's harmful glance.

### Fetch and body evidence

Listed live URL <https://web.prm.ox.ac.uk/amulets/index.php/protection-2/>: **HTTP 200, 17,704 bytes**, also successfully opened by the read tool. No fallback was necessary. Saved HTML: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R13/S641.html`, SHA-256 `db3f05683daec27fc9459cbb30b71c83be0678d2a0fac33b47b4aa2191daaa7b`.

Body paragraphs immediately after the object image and accession caption:

1. Line 153: “Mano cornuta, or ‘horned hand’ amulets are thought to be of ancient Italian origin and are worn as protection against the harmful glance of the Evil Eye.” This supports the entire line-50 remedy and line-67 origin/purpose clauses.
2. Line 155: “This minute mani cornute is from Ajaccio, Corsica, and is made of coral. Coral horned hands were especially popular in the Mediterranean, but they could also be made of mother-of-pearl, silver, gold, amber, or lava.” This supports coral and every alternative material in line 89, all explicitly for horned hands.
3. Same paragraph: “Sparkling and brightly coloured, their striking appearance was thought to divert attention away from the wearer so that she or he could escape from the dangerous glance of the Evil Eye unharmed.” This supports the line-67 ‘Turning the glance’ label as a reported belief, not demonstrated efficacy.
4. Line 157: “The glance itself is thought to be caused by excessive admiration or envy, and children and domestic animals are believed to be most at risk.” This directly supports the last clause of line 67.

### Every citing line

```text
| the evil eye's harmful glance | horned hand amulets are worn as protection against the harmful glance of the Evil Eye | S641 (C) |
- Turning the glance: horned-hand amulets, thought to be of ancient Italian origin, are worn against the harmful glance of the Evil Eye; the museum says children and domestic animals are believed to be most at risk (S641). **C**
- Coral and its substitutes: the horned-hand amulet appears in coral and, by the museum's list, in mother-of-pearl, silver, gold, amber or lava for the same horned-hand form (S641). **B**
```

These entry clauses are carried by the paragraphs above; no entry rewrite is required on this evidence. ‘Substitutes’ is supported as alternative materials, not as a claim that a documented chronological replacement occurred. The teaches cell still needs intended-use framing under the strict reader contract.

Quote fidelity: the quote is body prose, not the image/accession caption or title. The registry elides the closing curly quotation mark after `hand`; thus it is not punctuation-exact, but the named lane normalizer removes that distinction and `locate_in` returns true. No substantive word discrepancy was found.

## AUDIT S642 REWRITE

**Counterexample:** the article's disjunctive classification of amulets across a category does not establish the three capacities of **the same worn object**. The candidate appends that inference, with present-tense efficacy language. The registry's teaches cell is narrower and explicitly presents three distinct jobs as the article's account of Pliny; it can remain unchanged.

Listed live URL <https://journal.sciencemuseum.ac.uk/article/history-of-amulets/>: **HTTP 200, 502,294 bytes**, also successfully opened by the read tool. Saved HTML: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R13/S642.html`, SHA-256 `a46fca90dcb9161fb866d2362e13a886eda3afe9184fba19abf763144f90b3d3`.

The registry's exact sentence appears in a full **body paragraph**, saved HTML line 2617, discussing whether a carillon wheel belongs in an amulet collection:

> Yet most importantly (as described by Pliny since the first century CE) amulets were worn and used for therapeutic, apotropaic or exorcistic benefit.

An earlier introduction paragraph, line 2273, supplies the body relationship and date:

> The word ‘amulet’ originates from the Latin ‘amulētum’, and was used by Pliny the Elder (23–79 CE) to denote an item worn on the body for therapeutic, apotropaic or exorcistic benefit (Skemer, 2006, pp 6–7).

These sentences carry the historical attribution and the three purposes. Neither sentence identifies one object with all three capacities. The following “They are invested with the power to heal or protect” remains a category-level characterization, not the candidate's same-object conclusion. A targeted search of the saved full HTML for `same (?:worn )?object|three (?:distinct )?(?:jobs|functions)|heal,? ward|therapeutic, apotropaic or exorcistic` returned the classification passages at 2273 and 2617, not a same-object statement.

Only one entry line cites S642, line 76. Minimal source-scoped replacement:

old:
```text
- Three jobs: since Pliny's account in the first century CE, amulets were worn and used for therapeutic, apotropaic or exorcistic benefit, so the same worn object can heal, ward off or drive out (S642). **B**
```
new:
```text
- Three jobs: Thwaite reports that, as described by Pliny since the first century CE, amulets were worn and used for therapeutic, apotropaic or exorcistic benefit (S642). **B**
```

The anchor is verbatim body prose and locates with the lane locator. It is not a heading, caption, navigation, cookie or promotional fragment. The correction retains S642, the bullet, the ‘Three jobs’ structure and the grade; it removes only the unsupported same-object inference and makes the reporting authority explicit.

## Correction boundary and checks exercised

- Entry rewrites above are fixable before the freeze without losing any cited id. No candidate or registry bytes were edited by this seat.
- The S640/S641 teaches findings are **not fixed by entry-only rewrites**. The frozen exact-id predicate also prevents silently replacing old ids with new superseding ids. Meanwhile `CORPUS.md`'s append-only registry contract allows in-place changes only to status, recheck and used-by, not teaches/source. The source-scoped texts above therefore describe the smallest semantic corrections, **not authorization to overwrite old rows**. The integration owner must resolve that contract/declaration incompatibility before freezing, or report it as an unmet prerequisite; no hidden row edits, id substitution, or post-verdict narrowing is safe.
- Likewise, the discovered S640 capture must become an authorized packet URL through a contract-compliant pre-data resolution before it can cure the observed reachability defect. This audit does not count its discovery as a current packet pass.
- No assigned line is shared between two source ids. S648–S651 and the round-59 mapped rejections were outside this seat's scope.
- Ordinary curl GETs, read-tool openings, saved-HTML inspection and the named quote locator were exercised. Locator SHA-256: `64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8`. With `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`, its `to_text`/`locate_in` returned S640 live false, S640 archive true, S641 true, S642 true. A separate trial of a paraphrased folding sentence returned false; it was not the registry anchor and was not used to reject the actual folding body sentence.
- All shell commands ran under `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R13/`, with explicit `timeout` bounds of at most 110 seconds; all completed. No background jobs, child agents, git/jj writes, other runtime invocation, installs or updates. Only this report was written inside the lane.
