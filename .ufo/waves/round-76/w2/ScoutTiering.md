# ScoutTiering — round 76 W2 source-tier falsification

**Verdict: A/A/B is supported for the three landed rows, within their stated scopes.** I found no surviving tier inflation or source-role confusion in the landed rows or their admitted amendment. The most important boundary is that S896 supports what the press reported, not the standard's normative clauses; S895 supports registry fields, not clauses or drafting authorship; S894 supports what the archive's selector lists, not a state's chronology or naming authority.

## Rubric

At C landing `722e69ff`, `corpus/SOURCES.md:14-18` defines tiers as scoped to each row: A is primary/authoritative for that scope; B is strong secondary; C is lead-only and never sole support. `corpus/QUALITY.md:29` likewise reserves A for sources primary or authoritative for the exact scope. These definitions make each narrow scope, rather than the institution's general prestige, decisive.

## Row assessments

| Landed row | Assessment | Evidence and boundary |
|---|---|---|
| **S894 — archive instrument, A** (`corpus/SOURCES.md:849`) | **A appropriate; no inflation found.** | The row scopes A to the National Archives of Japan's own era-name search table, used as a comparison instrument. W1 `ScoutDocS894.md`, §§2–3, reports the mapping in static HTML returned by plain GET, identical row counts in live and same-page capture, and the exact selector/table location. Its §8 explicitly limits A to what the archive's form offers, not how it dates holdings, who has naming authority, or a supposed 詔勅・勅令・勅書 database. The amendment uses it for the selector's rows and form (§3; `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md:44-54`), and expressly says the Chinese/Korean tabs are the archive's filing, not a chronology of any state (`:64`). The row's descriptor “comparison instrument” and the path at `SOURCES.md:854` also disclaim support for the standard's clauses. |
| **S895 — official registry, A** (`corpus/SOURCES.md:850`) | **A appropriate; no inflation found.** | The row is expressly limited to the registry's identity, status, dates, classification, and custodial fields, and excludes normative clause text. W1 `ScoutDocS896.md`, §§2–4 and §7, records the live/capture field contents and states that A applies to the registry's own holding fields, not drafting authorship or clause text. The amendment uses S895 for those metadata fields (`…calendar-festival-systems.amend-2026-10-24.md:32-40`), distinguishes the press's drafter attribution from registry custody (`:38`), and calls the registry an identity carrier, not a clause carrier (`:40`). |
| **S896 — state-press account, B** (`corpus/SOURCES.md:851`) | **B appropriate; no inflation found in the landed tier.** | The row is scoped to a state-press report of announced rules and explicitly excludes normative wording. W1 `stage/ScribeEntryA/gate-notes.md`, “Row S898 — the 2017 report,” documents the report and its located content. W1 `ScoutDocS898.md:183-187` recommends tier B and specifically says to refuse if the row remains A. In the landed amendment, the rules are repeatedly attributed to S896 as an announcement, while §4 says they are “as announced, never ‘as enacted’” and that clause text remains unread (`…calendar-festival-systems.amend-2026-10-24.md:16-30,60`). |

The amendment's source declaration explicitly identifies one B press report and two A sources with their respective roles, and says the clause text was not read (`…calendar-festival-systems.amend-2026-10-24.md:12`). The path sequence `S896 → S895 → S894` is correspondingly press announcement → registry metadata → archive comparison instrument (`corpus/SOURCES.md:854`).

## Tier-inflation/source-role findings

- **A residual inflation risk is controlled, not present in the landed scopes:** the prior staged press row had been described as tier A. W1 `ScoutDocS898.md:183-187` explicitly rejects that tier; landed S896 is B (`SOURCES.md:851`). This is a successful correction, not a remaining defect.
- **The archive row is not being used as Chinese-calendar evidence.** The amendment's explicit limits around S894 prevent the archive's Japanese/Chinese/Korean era picker from being miscast as the Chinese standard or a state's authoritative chronology (`SOURCES.md:849,854`; amendment `:46-54,64`).
- **The registry is not being used to prove the rules or drafter.** The amendment keeps S895 to record fields and assigns the drafter statement to the press source S896 (`:26,34-40,60`).
- **The press is not being laundered into the standard itself.** It supports the announcement's reported rules; the entry marks the leap-month selection rule and normative clause text as absent/unverified (`:60`, `:100-107`).
- The third-party reproduction of the drafter's interpretation was **refused**, not appended as an A/B source: the round-76 lesson at `corpus/lessons/round-76.md:19,27-29` records the refusal because it was tier C and not normative clause text. The landed rows S894–S896 are therefore not masking that reproduction's role.

## Minor locator note (not a tier defect)

The round-76 lesson Gate labels S895's locator “标准信息表, 标准号 field” (`corpus/lessons/round-76.md:12`). W1 `ScoutDocS896.md` §4 reports that “标准信息表” is absent from the page, which presents the fields in an unlabelled table/div rows, and recommends renaming the locator. The landed SOURCES row instead says “record page, 标准号 field” (`corpus/SOURCES.md:850`), so the registry row's tier/scope remains sound; the lesson locator wording is a small evidence-label mismatch, not source-role or tier inflation.

**Confidence:** high for the A/A/B verdict and scoped usage, based on committed C-landing rows and amendment plus W1 source-gate reports. The report does not independently refetch the external pages; it assesses the committed evidence only. No tools installed.