NONE-MET

# AuditA3R05 — pre-freeze build wording review

Completed 2026-10-23T07:05:08Z. Assigned ids: S614, S615, S617. Axis: **depth**, specifically body-quote provenance, clause-level entailment, and source scope. These are build-audit findings, not blind support verdicts or a claim/admission judgment.

Read `reports/round-60/claims.json` first. Searched every occurrence of the three ids in `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md` and their complete rows in `corpus/SOURCES.md`. There is one candidate line per assigned id: S614 at 105, S615 at 140, S617 at 86. None is a shared-id line. No S648–S651 rejection comparison is applicable to this assignment.

Build-only seat: no control fixture, frozen-counter run, probe, or ACCEPT-D-60 receipt was produced; NONE-MET does not assert that the counter defeats unrun controls. No lane source, candidate, instrument, or judgment artifact was edited. Installs/updates: none. All started processes completed synchronously.

## AUDIT S614 TEACHES

**Counterexample / defect:** the page's discussion is of the particular illustrated bowl, but the entry turns its four-element combination into a generic description of an Aramaic incantation bowl, and the registry teaches broadens this further to “An amulet's”. The page expressly allows other images and says images occur often, not invariably. Thus a bowl depicting an animal or abstract magical sign, rather than a bound demon, is a counterexample supplied by this same page. The source does not establish the four listed features for every incantation bowl, still less for amulets generally.

- URL opened directly: https://jnjr.div.ed.ac.uk/primary-sources/biblical/jewish-aramaic-incantation-bowls/
- Observed HTTP **200**, **117,164 bytes**, `text/html; charset=UTF-8`; no redirect/challenge.
- Body sha256: `cf22f0577e3471fd319faf76c795c415cd3f14887a308279b5a51154c7b1a364`.
- Saved bytes/text: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/S614.body` and `S614.txt`.
- The registry quote locates under the lane's `to_text`/`locate_in` implementation. It is body prose in §3, beneath “The image”, **not** that heading, a caption, navigation, cookie or promo.

**Page sentences carrying the scoped claims** (`S614.txt:582`; HTML paragraph at `S614.body:537`):

> The amuletic object is a combination of elements, all of which are significant factors in making it potent.

> These elements consist of its being an earthenware bowl that was inscribed with an incantation, adorned with an image, and buried upside-down.

> The image of a shackled demoness, in this bow,l shares some of the characteristics found in other Jewish and non-Jewish bowl illustrations.

The first carries combination/significance; the second carries vessel, incantation, image and burial; the third identifies this image as a bound demoness and explicitly refers to this bowl. The contrary general context (`S614.txt:439`; HTML `S614.body:489`) includes:

> Other types of images include a variety of animals and abstract magical symbols, known as characteres.

**Exact candidate correction, preserving the id and bullet structure:**

old: - Buried bowl: an Aramaic incantation bowl is an amuletic object whose potency comes from a combination of elements, each a significant factor: the earthenware vessel, the written incantation, the image of a bound demon and burial upside down (S614). **B**

new: - Buried bowl: Levene describes one Aramaic incantation bowl as an amuletic object whose reputed potency comes from a combination of elements, each a significant factor: the earthenware vessel, the written incantation, the image of a bound demon and burial upside down (S614). **B**

**Registry teaches also needs attention; entry narrowing alone leaves this issue:**

old teaches: An amulet's potency comes from a combination of elements, so vessel, text, image and burial each carry part of the protection.

source-supported teaches: In the incantation bowl discussed by Levene, the earthenware vessel, incantation, image and upside-down burial are described as significant factors in its reputed potency.

**Smallest safe correction / ownership:** scope both statements to the discussed bowl and attribute potency rather than implying demonstrated efficacy. This is a fixable wording defect, not an unavoidable axis tradeoff. The registry's append-only rule does not authorize editing its old teaches cell in place; its normal correction is a superseding row. Because the declared 47-id object still requires S614, L1 must resolve that pre-freeze contract/identity constraint openly rather than silently overwrite the filed row, omit the id, or assume the entry-only rewrite cures the teaches issue. No counter or freeze change is made or adjudicated here.

## AUDIT S615 OK

- Candidate line audited: `candidate-entry.md:140` — “Made to order: late antique incantation bowls sold as talismans were customized to fit individual clients' needs, against bad luck, financial struggles and even severe migraines”.
- URL opened directly: https://www.smithsonianmag.com/smart-news/1500-year-old-magic-bowls-seized-in-jerusalem-raid-180979705/
- Observed HTTP **200**, **58,161 bytes**, `text/html; charset=utf-8`; no redirect/challenge.
- Body sha256: `eb4d902580d9dfb4be9da3f2ad34272c05649caf7ffd23dfce2d0bf322cb775a`.
- Saved bytes/text: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/S615.body` and `S615.txt`.
- Canonical `to_text`/`locate_in`: **True** for the registry quote.

**Page sentences carrying the clauses** (`S615.txt:760–772`; HTML paragraphs `S615.body:664,666`):

> Per Samuel Thrope of Aeon, scribes in what is now Iraq produced thousands of these bowls between the fifth and eighth centuries C.E.

> Customized to fit individual clients’ needs, the talismans were used to fight off bad luck, financial struggles and even severe migraines.

> To activate the bowl’s protection, a buyer would bury it beneath their house’s floor.

The first grounds the period descriptor; the second explicitly grounds talismans, individual customization and every named trouble; the buyer grounds purchase rather than requiring the modern antiquities sale to stand for ancient sales. The article also describes the practitioners offering services in local marketplaces (`S615.txt:802–804`). The teaches cell restates the second sentence's client/trouble relationship without an added mechanism or comparison. The registry quote is ordinary article **body prose**, not the nearby photograph caption; no heading/caption/promo/cookie/navigation issue found. No rewrite recommended.

## AUDIT S617 OK

- Candidate line audited: `candidate-entry.md:86` — “Stone as icon: icons survive in the amuletic form of engraved stones to be worn on the body, alongside holy icons and unorthodox amulets”.
- URL opened directly: http://hierotopy.ru/contents/ComparativeStudySacredSpaces_06_Tuerk_NarrativeAmulets_2008_Eng.pdf
- Observed HTTP **200**, **319,854 bytes**, `application/pdf`; no redirect/challenge.
- Body sha256: `c24f67ff98e1f4c134ed68fd779911a9bca775a5e7f3b357ddb21f3acf6b3a21`.
- Saved PDF/text: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/S617.body` and `S617.txt`; extracted with `pdftotext -layout`.
- Lane `locate_in` applied to the extracted text: **True**, registry quote **24 normalized words**.

**Page sentence carrying every clause**, printed p. 100, main article paragraph (`S617.txt:1027–1028`):

> In addition to holy icons and unorthodox amulets, there survive icons in the amuletic form of engraved stones to be worn on the body.

This carries survival, icon identity, engraved-stone amuletic form, wearing on the body, and the alongside/in-addition relationship. The following sentences give museum examples; the cited sentence is **main body prose**, not a heading, running header, illustration caption or footnote. The teaches cell stays within this same sentence; it adds no material-versus-image comparison or stronger efficacy claim. No rewrite recommended.

## Reproducibility

Fetches used the bounded plain-urllib helper `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/fetch-source.py`, which imports the lane locator for HTML extraction and quote matching, retains at most 6 MiB per response, and uses the locator's ordinary User-Agent. Commands were run with that sandbox as cwd:

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/fetch-source.py S614 'https://jnjr.div.ed.ac.uk/primary-sources/biblical/jewish-aramaic-incantation-bowls/'
timeout 120 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/fetch-source.py S615 'https://www.smithsonianmag.com/smart-news/1500-year-old-magic-bowls-seized-in-jerusalem-raid-180979705/'
timeout 120 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/fetch-source.py S617 'http://hierotopy.ru/contents/ComparativeStudySacredSpaces_06_Tuerk_NarrativeAmulets_2008_Eng.pdf'
timeout 60 pdftotext -layout /fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/S617.body /fast/scratch/hyaku/kotodama-r60a3/AuditA3R05/S617.txt
```

No Wayback fallback, access-control workaround, headless browser, support-seat contact, delegation, background job, or other judgment runtime was used.
