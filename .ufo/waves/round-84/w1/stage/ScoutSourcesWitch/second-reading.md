# Second reading — the four claim-D sources

Seat ScoutSourcesWitch, round 84 wave 1. Independent reading of the four candidate sources, opened by ordinary
plain HTTP GET on 2026-11-04. Per-row evidence is in `S914.txt`, `S915.txt`, `S916.txt`, `S917.txt` beside this
file. Nothing here is copied from another seat's reading.

## 1. Verdicts

- **S914 — EB11 "Witchcraft" (N. W. Thomas), vol. 28, pp. 755-758.** Serves body prose, 4458 words, and is the
  only row that states the institutional thesis in one sentence. Usable.
- **S915 — EB11 "Sorcery", vol. 25, p. 431.** Serves body prose, but the body is a 71-word dictionary
  definition. Not usable for claim D. Substituted: **Howard Williams, "The Superstitions of Witchcraft" (1865),
  Gutenberg #22822**, 71,246 words, opened and measured.
- **S916 — Malleus Maleficarum, Summers 1928, Wikisource.** The root page is a cover page (2174 words of front
  matter and contents; body subpages return 404). The Bull of Innocent VIII is a separate, complete page and
  is the citable text. Usable, with the anchor on the Bull.
- **S917 — Upham, "Salem Witchcraft" (1867), Gutenberg #17845.** Serves body prose, 31,370 lines with 1051
  `[i.N]`/`[ii.N]` page markers. The widest scope coverage of the four. Usable.

## 2. Scope coverage, row by row

The claim's six scopes: vocabulary set, accusation grammar, proof technology, confession, slander law, social
functions.

- **S914** carries five of the six. Vocabulary: hexe, lamia, striga, Unholde, malefica, incubus/succubus,
  sortiariae, "white witchcraft", "evil eye", "ligature". Accusation grammar: the three-period scheme and "the
  modern idea of witchcraft is largely a learned product". Proof technology: the Malleus passage on questions
  under torture and admissions "described as voluntary". Confession: the same passage, plus "the valueless
  declaration of the victims of torture". Social functions: victim estimates, the Inquisition's role, the rise
  of the critical spirit. It has no slander-law content and no trial record.
- **S915 (Williams)** carries four, and two of them better than S914. Accusation grammar: the 1604 statute
  detached sorcery from the political indictment it used to ride on. Proof technology: the Garnier case gives
  the chain in one sentence — fifty witnesses, the rack, an unreserved confession, the sentence. Slander law:
  weak (one occurrence of "slander" in 71,246 words) but the 1736 repeal passage is present. Social functions:
  the continental geography of persecution. No vocabulary set, no doctrine.
- **S916 (the Bull)** carries two, and one of them uniquely. Vocabulary set: the bull's own list — devils,
  incubi and succubi, incantations, spells, conjurations, "accursed charms and crafts", "enormities and horrid
  offences". Accusation grammar: the delegation of coercive jurisdiction "to the just correction, imprisonment,
  and punishment of any persons", "without any right of appeal". Proof technology: absent from the Bull; the
  root page's Part III contents names the sequence (witnesses, enemy-witnesses, imprisonment, detention and
  torture, sentence, appeal) but supplies no text. Confession: absent. Slander law: absent. Social functions:
  the bull's framing of heresy as a spreading disease.
- **S917 (Upham)** carries four and is the only one with a working court. Accusation grammar: the commission
  of the special court and the indictment practice. Proof technology: spectral evidence, the "afflicted
  children", and Brattle's charge that the judges took testimony from the Devil. Confession: the examination
  records. Slander law: the strongest item in the round — Godfrey's defamation actions, won in damages and
  still leaving him "rendred suspicious". Social functions: village faction and the salary dispute. No
  vocabulary set, no European statute text.

Union of the four rows covers all six scopes. No single row covers more than five, and the two rows that carry
the law (S915 Williams, S917 Upham) carry different laws: the English statute and the colonial vacuum.

## 3. Where the sources disagree, and what the entry must not smooth over

1. **The year of the Witch Act.** Williams: "The 'Witch Act' of James I. was passed in the year 1604."
   Upham: "the proceedings were under an act of James the First, passed in 1603." Both are in my fetch, both
   verbatim. The difference is consistent with the regnal-year convention (the first year of James I ran from
   March 1603) [INFERENCE]. The entry should attribute each figure to its source, not pick one and not average
   them.
2. **Torture in England.** S914: "the absence of judicial torture made the cases proportionately less numerous
   than they were on the European continent", while listing the prick, the water test and the sleepless
   watch as English practice. Williams prints the rack at Dole. These are different jurisdictions, not a
   contradiction; a sentence that says "Europe tortured, England did not" will be true to S914 and false to
   the Garnier record if left unqualified.
3. **The Malleus date.** S914 gives "(1489)"; the Bull it names is dated 9 December 1484. The printed Malleus
   is 1486/1487. Quote S914's figure as printed or cite the Bull's own date; do not silently reconcile.
4. **Who owns the procedure.** S916 gives the procedure as a papal delegation (the office is granted); S917
   gives it as a colonial commission (the office is improvised, and "a shade of illegality rests upon the very
   existence of this special court"). The entry should present these as two ends of one institution, not as
   one mechanism described twice.

## 4. What the four rows cannot supply at all

- No row supplies a continuous passage of the Malleus' own interrogation text. The Wikisource transcription
  does not carry Parts I-III (404 on `/Part_I`, `/Part_I/Question_I`, `/Part_III`), Gutenberg has no Malleus,
  and Summers' Introduction mentions torture once in 22,801 words, in a modern political analogy. The
  confession clause must be carried by S914's summary and S917's records, or by a fifth row.
- No row supplies the text of the 1604 or 1736 statutes. Williams describes them; Upham reports Hutchinson on
  them. A statute quotation would need a new source (the Statutes of the Realm or the 1736 act text).
- No row supplies a non-European comparison. S914 has three paragraphs on "primitive peoples" (Congo,
  Australia, Bengal) but they are 1911 folklore summary, not evidence.

## 5. Access limits observed, in one place

- All six URLs answered 200 and were byte-identical across the two request shapes (plain and browser-shaped);
  the byte counts and sha256 pairs are in the receipts.
- The Wayback availability API returned 429 Too Many Requests for every URL; the CDX endpoint answered 200 for
  all of them. S916's Bull URL has **no capture at all** (CDX returns `[]`).
- S914's only capture is from 2008-10-06 (27,225 bytes) and predates the Proofreadpage transcription; it does
  not contain the quoted text. S917's capture (2022-01-23) is byte-different but body-identical and carries all
  four quoted spans. Williams' capture (2024-03-23) carries both quoted spans but is not byte-identical.
- Both Wikisource pages are Parsoid-rendered and inject unexpanded template payloads as literal JSON at the
  transclusion points. A stripper that keeps those spans shows "sorci …" mid-word on the Sorcery page and
  intersperses JSON through the Witchcraft article. The text is intact underneath; the payload must be
  stripped or the `Page:` subpages read directly.
- The S915 "Sorcery" page renders its full article. It is not truncated and not a template shell — it is a
  71-word stub, which is a different and worse problem for claim D.
