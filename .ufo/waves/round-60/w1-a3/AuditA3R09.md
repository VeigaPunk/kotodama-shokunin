NONE-MET

# AuditA3R09 — pre-freeze wording audit

Scope: S628, S629, S630 only; candidate `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md`, citing lines 55/61, 74/126, and 81 respectively; registry rows read in full at `corpus/SOURCES.md:583-585`. This is build-review evidence, not a support-seat verdict or canonical acceptance judgment. No control fixture or counter was run.

Axis: **depth**. Audit dimensions: verbatim body quotation, teaches entailment, every cited clause, and preservation of the source's object/cultural scope. The one fixable defect is S629's loss of the article's expressly restricted definition of “amulet”; line 126 also loses the belief framing already present on line 74. No unavoidable axis trade is identified: the proposed narrowing retains the id, both lines, their structure, and all supported maker detail.

All three first-listed live URLs opened by ordinary curl GET, with literal URLs, without cookies, challenge solving, browser automation, or archive fallback. HTTP statuses and downloaded byte counts below are observed curl output. Tools installed/updated: none. All shell work ran in `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R09/`, bounded by timeout; no background process was launched.

## AUDIT S628 OK

URL: https://rubinmuseum.org/projecthimalayanart/essays/amulet-box-gau-with-its-contents/

Observed: `S628 HTTP=200 bytes=239349 content_type=text/html; charset=UTF-8`.

- Anchor is verbatim prose in the essay's **Summary**, inside `<p>` at downloaded HTML line 147, not the `<summary>` heading, navigation, promotional copy, or a caption: “People wear amulets to bring long life, good fortune, success in love, and protection against harm.” This carries the remedies on candidate line 55, the enumerated worldly aims on line 61, and the teaches cell: “Wearers expect an amulet to deliver specific worldly benefits, from long life and fortune to love and protection from harm.” These are purposes/expectations, not demonstrated efficacy.
- I specifically attacked line 55's stronger danger label, “harm of every kind, plus wished-for goods.” The main essay, **Amulets and Their Purpose**, supplies the missing breadth: “Tibetans have used them to protect against misfortune during travel, injury during battle, illness, harmful spirits, and any other potential calamity.” This is full body prose at HTML line 219, not a heading/caption. Thus the phrase is not supported solely by an unjustified expansion of the short anchor's word “harm.”
- The next body paragraph (HTML line 220) says: “Gaus and the amulets they house have a range of other functions, too. They can be worn to extend longevity, personal power (wangtang), and good fortune (lungta), and to enhance wealth and intelligence, among other desirable aims.” Together with the Summary's express love clause, this carries line 61's “plural and this-worldly” characterization.
- Every clause of both citing lines was checked; neither is a shared-id line. No rewrite or teaches correction requested.

Fetched HTML sha256: `3732be7376337e1eac2301cef78922ba4af693dac4d181b1ce81da33cbc0ce2e`.

## AUDIT S629 REWRITE

URL: https://englishkyoto-seas.org/wp-content/uploads/SEAS_0202_Baker-and-Pasuk.pdf

Observed: `S629 HTTP=200 bytes=1159618 content_type=application/pdf`.

**Counterexample / scope evidence:** the article expressly refuses the broad definition that the candidate entry otherwise uses. On printed p. 215, footnote 1: “The term ‘amulet’ is sometimes used to describe protective devices of all kinds. In this article, the term refers to this specific type.” The immediately preceding opening paragraph defines that type as “an amulet (พระเครื่อง phra khrueang), a small image of the Buddha or of a famous monk usually enclosed in some form of casing and attached to a cord or chain worn around the neck.” Dropping this restriction turns a statement about the article's Thai Buddha amulets into a maker condition on an unspecified Thai amulet.

This distinction is substantive within the same page set, not hypothetical pedantry: on printed pp. 224–225, the article separately describes naturally occurring substances “believed to be intrinsically powerful,” including cat's eye and tusk splinters, and says, “Mostly these objects are carried to convey protection or invulnerability.” It does not put all Thai carried protective objects into its restricted Buddha-amulet category. This is evidence of the domain distinction, not an assertion that the paper proves an empirical exception to every possible maker rule.

**Positive evidence for the retained clauses:** printed p. 235, **From Yantra to Amulet**, body paragraph following the discussion of Somdet To's manual: “Also like yantra, an amulet is effective only if made by a monk or adept famous for supernatural power (like Somdet To).” The preceding sentences place this in Somdet To's description of amulet manufacture and ritual activation. This carries the maker, supernatural-reputation, necessity, and yantra comparison clauses, within the article's restricted category. The quote is full body prose, not a heading or figure caption. Registry teaches already correctly says “Thai Buddha amulets were held to work only when a famous monk or adept made them, the same efficacy rule the article says governed yantra.” No teaches correction is needed.

Candidate line 74:

old: - The maker's power: in Thailand an amulet, like a yantra, was held effective only if made by a monk or adept famous for supernatural power (S629). **B**

new: - The maker's power: in Thailand a Buddha amulet, like a yantra, was held effective only if made by a monk or adept famous for supernatural power (S629). **B**

Candidate line 126:

old: - The famous maker: a Thai amulet is effective only if made by a monk or adept famous for supernatural power (S629). **B**

new: - The famous maker: a Thai Buddha amulet was held effective only if made by a monk or adept famous for supernatural power (S629). **B**

The scope narrowing is the primary defect correction. Restoring “was held” on line 126 also makes its epistemic status consistent with line 74 and the registry, rather than asserting supernatural efficacy in the entry's own voice. Both citing lines were checked in full; neither is a shared-id line.

Fetched PDF sha256: `260496397a4cc0ccfcf7dcbdadb3209efcdf6fc0ffdf00a247106af49fef15a5`.

## AUDIT S630 OK

URL: https://collections.vam.ac.uk/item/O472426/amulet/

Observed: `S630 HTTP=200 bytes=47986 content_type=text/html`.

- Anchor is verbatim object-record Summary prose, repeated in the object's detailed Summary field: “This amulet was made to protect the wearer from harm or misfortune and has been fashioned in white nephrite jade.” This is body text, not a heading, image caption, navigation, cookie, or promotional fragment. It carries both line 81's protective purpose and its specific material.
- The **Brief description** field states: “Amulet, generally oval, scalloped ends, white nephrite jade, Persian inscription, Mughal empire”. That record field carries the additional “Mughal” object classification; the quote alone need not carry that classification because the page does. The entry stays at one object (“a Mughal amulet”), not a universal about jade or Mughal amulets.
- The teaches cell, “A white jade amulet was made to shield its wearer from harm and misfortune,” is carried by the quoted Summary. Neither teaches nor the entry claims that the material caused protection, was more important than the inscription, or empirically protected anyone.
- Full physical-description prose additionally says: “It has been fashioned in white nephrite jade, polished and then the front face has been engraved with a central inscription in Persian that is surrounded with further text which itself lies within a decorative border of numerous small \" + \" within their own individual boxes.” This also carries the registry scope's material/script/border description.
- Every clause of the sole citing line was checked. No rewrite or teaches correction requested.

Fetched HTML sha256: `eed12284fe00e3ac8bb63883cfda488aa725d42b61b139da8a0dff4914c1e2f2`.

## Quote-location receipts

HTML was converted with the lane locator's `to_text`; PDF text was extracted using permitted `pdftotext -layout`. All three anchors were checked with the lane locator's unmodified `locate_in` / `normalise`, imported read-only with bytecode disabled. Full stdout of that local quote-location run (exit 0):

```text
S628: located=True normalized_words=16 method=canonical to_text and locate_in
quote=People wear amulets to bring long life, good fortune, success in love, and protection against harm.
S629: located=True normalized_words=22 method=pdftotext -layout, then canonical locate_in
quote=Also like yantra, an amulet is effective only if made by a monk or adept famous for supernatural power (like Somdet To).
S630: located=True normalized_words=20 method=canonical to_text and locate_in
quote=This amulet was made to protect the wearer from harm or misfortune and has been fashioned in white nephrite jade.
```

Local evidence: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R09/` contains the fetched page/PDF bytes, response headers, extracted text, and the bounded `locate-quotes.py` invocation source. No corpus, registry, candidate, or instrument was edited. S648–S651 / round-59 mapped-rejection comparison is outside these assigned ids; no finding is claimed for those rows.
