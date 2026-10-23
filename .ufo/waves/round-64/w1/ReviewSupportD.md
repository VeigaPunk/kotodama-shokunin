# ReviewSupportD — blind support falsifier, claim C spot sample (round 64 wave 1)

Role: reviewer (claim-C blind support). I authored no rows; all 32 staged rows
(S718-S743, S744-S749) were authored by sibling ScribeRowS*/ScribeRej* seats, so
no exclusion was needed beyond "exclude any you authored" — none apply.

## Method

Spot sample of 8 rows, chosen for spread: full id range, both tiers (4×A, 4×B),
both media (3 HTML, 5 PDF), and overlap with the LIVE frozen subset
(S718, S728, S738 are also in accept-c.py LIVE_IDS = every 5th from S718).
Sampled: **S718, S719, S724, S728, S730, S735, S738, S741.**

1. Re-opened the live URL fresh (22:59 local / 2026-10-24T02:59Z) with plain
   curl (desktop UA, -L, --max-time 90), independently of the scribe's
   recorded ACCESS line. All 8 returned HTTP 200.
2. Located the anchor quote under the same normalization as the pinned locator
   (NFKC, casefold, \W_→space, substring match); PDFs via pdftotext 26.08 and,
   where extraction differed, the canonical pypdf 5.4.0 path the locator uses.
3. Then ran the canonical instrument itself —
   `python3 -B reports/round-61/reopen-quote.py URL QUOTE` — on every sampled
   row's live URL (URL-QUOTE mode, same thing `--row` does per URL).
4. Judged the bullet's faithfulness to the quote at the row's declared tier
   (registry rule: A = primary/authoritative for scope; B = strong secondary).

Receipts: raw bodies, extracted text, locator outputs, and the check script are
in scratch `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewSupportD/`
(`s7*.body`, `s7*.txt`, `loc-s7*.txt`, `check_quote.py`, `loc.sh`).

## Per-row verdicts

| id | tier | live re-open | canonical locator | verdict |
|----|------|--------------|-------------------|---------|
| S718 | A | curl HTTP 200, article body, quote verbatim | live URL `NOT_LOCATED quote-absent`; archive capture `LOCATED` | **SUPPORTED** (note 1) |
| S719 | B | PDF HTTP 200 (14 pp) | `LOCATED` | **SUPPORTED** (note 2) |
| S724 | B | HTTP 200 live | `LOCATED` | **SUPPORTED** (note 3) |
| S728 | B | PDF HTTP 200 | `LOCATED` | **SUPPORTED** |
| S730 | B | PDF HTTP 200 (34 pp) | `LOCATED` | **SUPPORTED** |
| S735 | A | PDF HTTP 200 | `LOCATED` | **SUPPORTED** (note 4) |
| S738 | A | PDF HTTP 200 | `LOCATED` | **SUPPORTED** (note 5) |
| S741 | A | HTTP 200 live | `LOCATED` | **SUPPORTED** |

**S718** — Farran et al. 2016 (PLOS ONE, PMC). Quote located verbatim in my live
body: "The tabulated results for rate in utterances per minute also indicate
that Lebanese mothers, compared to American mothers, produced more IDS (a fact
reflected in Fig. 1)". Bullet "Lebanese mothers produced more infant-directed
speech than American mothers in this sample" is a faithful restatement and keeps
the sample-bound hedge the scope cell demands ("sampled … only"). Tier A
correct: original paper's own result.
Note 1 (non-blocking): minutes later the canonical locator fetched the same
URL and got PMC's interstitial ("Checking your browser … recaptcha", 20,573 B
vs my 197,724 B article body) → `quote-absent`. The quote IS present on the
live page; the gate is intermittent bot-defense, not absence. In `--row` mode
the locator proceeds to the row's second URL, the wayback capture, which I ran
separately: `LOCATED https://web.archive.org/web/20250212134043id_/…`. The LIVE
leg therefore still resolves LOCATED through the capture; residual risk is a
three-reopen window landing on three captcha responses at gate time (bounded,
and mitigated exactly by the capture fallback the counter pins).

**S719** — Cristia 2013 (Language & Linguistics Compass, MPG.PuRe PDF). Quote
verbatim at §4 opening. Bullet restates the finding; "helping caregivers
attract a baby's attention" is a functional gloss consistent with the article's
own framing (Sec. 3–4 discuss caregiver attraction of infant attention).
Dropped "(with the aforementioned caveats)" — acceptable compression for a
tier-B review synthesis, but the loosest bullet in my sample; note 2, flagged
for the other reviewers' overlap to confirm. Tier B correct: review article.

**S724** — Anderson et al., Essentials of Linguistics 2e §11.7 (Pressbooks).
Quote verbatim in the opening paragraph. Bullet restates content-word-heavy,
few-inflection telegraphic phrases; drops "few function words", no distortion.
Tier B correct: textbook. Note 3: recorded ACCESS says live GET returned 403
and access was via archive; my live GET today returned HTTP 200 — drift in the
favorable direction, recorded for the record.

**S728** — Frye 2022, "Corrective input" (ANU Press ch. 8 PDF). Quote verbatim
in §8.1; it is Frye's secondary report of Schieffelin 1990 on Kaluli elema —
the scope cell says exactly that, so tier B is honest (the bullet could not be
tier-A-supported since the claim is Schieffelin's via Frye). Bullet "Kaluli
caregivers teach children to correct non-target-like speech with explicit
prompts" is faithful, and "non-target-like" matches the sentence's continuation.

**S730** — Genesee & Nicoladis 2007, BFLA chapter. Quote verbatim, chapter
opening. Bullet is a near-literal faithful restatement. Tier B correct:
handbook chapter (secondary synthesis), used for its own definitional claim.

**S735** — Michaels 1981, "Sharing time" (Language in Society). pdftotext
merges spaces ("throughher", "structureand") so a naive extraction misses the
quote; the canonical pypdf path locates it verbatim in the Abstract — and the
locator itself prints `LOCATED`, which is the evidence that counts. Note 4:
the same sentence appears in the Discussion with reversed clause order
("focus and structure"), but the abstract anchor is exact. Bullet faithful,
including the literacy-bridge claim present in the abstract's next sentence.
Tier A correct: original article.

**S738** — Kozminska & Zhu 2021, Bloomsbury chapter (eprints.bbk.ac.uk PDF).
Quote verbatim in the named section. I confirmed "the language" refers to
Polish (immediately following line: "planned to gradually introduce Polish"),
so the bullet's naming Polish is faithful, not an overreach. Bullet faithful.
Tier A defensible: for the scope — the studied family's practices — the chapter
is the primary source, matching registry precedent (analyses cited for their
own scope are A); note 5 for the other support seats to cross-check.

**S741** — Carvalho & Gouvea 2020 (SciELO HTML). Quote verbatim as Tomás's
utterance in the classroom dialogue; the article itself paraphrases it as the
social transmission of swear-word taboo ("We know that it's ugly because
people tell us that it's ugly"), exactly what the bullet states. Tier A
correct: original observational study.

## Findings by severity

No NOT-SUPPORTED rows. All 8 sampled rows: anchor quote located on the live
source (or for S718, on the live page plus verified via the pinned capture),
bullet faithful at declared tier.

Minor observations (not blocking):
1. **S718** — PMC intermittently serves a reCAPTCHA interstitial to non-browser
   fetches; the canonical locator's live-URL attempt returned `quote-absent`
   while the quote is genuinely on the page (my curl body has it verbatim) and
   the wayback capture LOCATED. LIVE-leg resilience: capture fallback works;
   worst case is a transient three-strike on the live URL, which the row still
   survives via capture.
2. **S719** — bullet drops the quote's "(with the aforementioned caveats)"
   hedge; faithful in substance but the loosest restatement in this sample.
3. **S724** — scribe's ACCESS records live-403/archive-200; today live returns
   200. ACCESS is a historical record; no action needed, noted for freshness.
4. **S735** — naive extractors (pdftotext) mangle the quote with merged words;
   only the canonical pypdf path finds it. Locator handles this correctly.

## Verification gaps / residual risk

- Spot sample only: 8 of 24 staged rows (S723 and S740 absent from staging,
  as already declared MISSING under check-rows.py — outside this item's remit).
  Rows not sampled: S720, S721, S722, S725, S726, S727, S729, S731, S732,
  S733, S734, S736, S737, S739, S742, S743. Other blind-support seats cover
  their own samples; overlapping verdicts are the intended cross-check.
- I verified the quote→bullet faithfulness leg only; registry-side legs
  (ROWS/ONEID/RESTATE/APPEND etc.) belong to the counter, not this falsifier.
- S718's captcha behavior could differ at integration time (rate of PMC's
  bot-check is unknown to me).

## Tooling

No installs or upgrades performed. Used: curl 8.23.0 (host), pdftotext
26.08.0 (host), python3 + urllib, uv 0.13.0 (existing) to run pypdf 5.4.0 —
the same pypdf version the pinned locator uses. Pacman untouched per
host-wide pause.
