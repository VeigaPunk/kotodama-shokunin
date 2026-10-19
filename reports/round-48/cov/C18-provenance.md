# C18 — provenance verification (claim C)

- Seat: `C18` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19); `git status --porcelain` → `?? reports/round-46/review/`, `?? reports/round-48/` only.
- Out path: `reports/round-48/cov/C18-provenance.md` (this file).
- Mission: every `(to-verify)` mark honestly placed (external shelf, edition/page locators); no external work presented as inspected; in-lane registrations accurate.
- Target audited: the r48 head block in `reports/round-48/cov/C02-header.md:111-135` (fenced, 23 lines), plus the body fragments that carry external citations — `reports/round-48/cov/M02-calibration.md:25-45,128-141` — and the right-sized shelf spec at `reports/round-48/scout/K01-rightsized-spec.md:116-128`.

**Verdict: PASS on the head block's own provenance mechanics, with four carry-forward fixes.** Independently reproduced: **11/11** sha256 pins match the live files; **26/26** needle-in-line checks pass over 22 distinct anchors (the block claims 23/23 over 22, and adds three recheck anchors outside that count); **19/19** backticked `- couples:` file tokens resolve (the block states 18 — see P5); **10/10** external shelf items carry `(to-verify)`; **zero** lines present an unread work as inspected; the r44 seed's unverified volume count was **not** restored. The open risk is not the header's bytes but shelf/body reconciliation: the body cites four works absent from the shelf (P2), and one of them — Boone (2000) — is registered in-corpus and must not be classed as external (P1).

---

## 1. Method and scope

For each provenance claim I re-read the cited bytes at `a01405d` rather than trusting the fragment, and recomputed every count/digest. Rules applied:

- `corpus/knowledge/verification/citation-format-and-source-registry.md:35` — `(to-verify)` attaches "beside that specific reference/claim", not in a distant list.
- `corpus/knowledge/verification/to-verify-triage-protocol.md:15` — the mark attaches "to the smallest uncertain proposition, not to a whole culture or bibliography".
- `corpus/QUALITY.md:5-8` — every factual claim carries a checkable citation; unverifiable claims are marked inline.

**Could not evaluate:** external bibliographic accuracy (no network; I can certify *marking*, not that Harley & Woodward's volume history or Snyder's paper number is correct); the assembled entry body (no assembled body was filed at my read cut — `reports/round-48/cov/` contained C02, C04, C06, C07, C09, C11, C14, C15, C16, E01, M01, M02, N03, V01, W01, but no `C01-entry` file); the final landing and length (other seats). Findings P2/P6 are conditional on which body sections survive integration.

---

## 2. Digest ledger — 11/11 pins match

Recomputed with `python3` + `hashlib.sha256` over the live files at `a01405d`:

```text
MATCH corpus/knowledge/myth-symbol/cosmology-cosmography.md          165f292b…
MATCH corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md  241113b5…
MATCH corpus/knowledge/myth-symbol/direction-symbolism.md            5a6ef38f…
MATCH corpus/knowledge/culture-material/architecture-settlement-lexicon.md 9af04e75…
MATCH corpus/knowledge/culture-material/writing-media-surface-economy.md    f039e6e1…
MATCH corpus/knowledge/culture-material/transport-mobility-lexicon.md      86e5f952…
MATCH corpus/knowledge/culture-material/craft-artisan-lexicon.md           fd678d82…
MATCH corpus/knowledge/culture-material/trade-economy-lexicon.md           760a9df6…
MATCH corpus/knowledge/civilizations/mesoamerica-primary-sources.md        d04d8913…
MATCH corpus/knowledge/linguistics/naming-systems.md                       d972a1d6…
MATCH corpus/knowledge/verification/calibration-registry.md                cf7cceee…
11/11 match
```

`corpus/README.md` sha256 → `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`, equal to `C02-header.md:132` and to the sweep's own `readme_sha256` line.

**Topic provenance.** `C02-header.md:114` is byte-equal to the r44 seed `reports/round-44/scout/K02-gap-scout.md:227` and to `reports/round-47/cov/C04-entry-header.md:114`: 775 characters, `sha256(line + "\n")` = `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a`. The bare line without its LF hashes to `a42926b1d0fe5ac5d608bb4ebd8e16873b3ed2f43a74c34392f0e4d5632496f8`. `C02-header.md:109` quotes the first digest without naming the LF convention; the claim is true, the convention is unstated (P6).

**No unread work presented as inspected.** `C02-header.md:129` opens the shelf "**not consulted this round** (no network at seat time) … no unread work is presented as inspected"; `:131` repeats "**none fetched or inspected this run**"; `:132` ends "**Not claimed:** any … external edition, volume or page." A scan for `consulted|inspected|fetched` finds only these disclaimers.

**The r44 over-specific claim was not restored.** The seed said "6 vols. in 7 … 1987–2022 … vol. 1 (1987) … vol. 3 (2007)" (`reports/round-44/scout/K02-gap-scout.md:267`). The r48 shelf says only "University of Chicago Press, 1987–" with `(to-verify)` — the correct offline posture.

---

## 3. Anchor ledger — 26/26 pass (23 claimed + 3 recheck)

Every quoted phrase was tested against the exact live line. The 23 assertions listed at `C02-header.md:174-197` all pass, including the two on `architecture-settlement-lexicon.md:95` ("groma", "cadastral") which give 23 assertions over 22 distinct anchors — the arithmetic is correct. I additionally verified the three anchors used only in `- recheck:` (`C02-header.md:133`):

```text
OK  direction-symbolism.md:26            "never as a compass rose with a legend"
OK  real-world-inspiration-boundaries.md:6 "reuse"
OK  myth-consistency-gate.md:34          "Do not expose restricted ritual knowledge"
26/26 pass
```

Spot-checks of the r47 defect fixes the block claims:

- **B2 (count):** `grep -rni cartograph corpus/knowledge/` → 2 lines (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`); `:71` contains "Mappa Mundi"/"survey maps", not `cartograph`. The block's "2 files / 2 lines" is correct.
- **B3 (false accusation):** `naming-systems.md:70` ends "Every renaming is datable; a map is an archive of coups." — the quote is verbatim; no correction is proposed.
- **B4 (ladder line):** `craft-artisan-lexicon.md:54` is the table header, `:56-63` the seven systems, `:65` the design rule; `:44` is the steel-grading row. The block cites `:54-65` and labels `:44` correctly.
- **B8 (ownership overstatement):** `cosmology-cosmography.md:27` does say cosmography covers "how the world is drawn (maps)"; the block quotes it and dispositions it (cosmography owns the world-drawn content, this entry owns production).

---

## 4. External shelf — 10/10 items marked, honest frame

`C02-header.md:129` carries ten works: Harley & Woodward; Harley 1989; Wood; Monmonier; Jacob; Ptolemy (*Geography*); Campbell; Kain & Baigent; Snyder; Dilke. Paren-aware split gives **10 items, 10/10 with `(to-verify)`** (11 occurrences on the line including the blanket rule). Edition/page details that are asserted in the same breath are marked: Harley's `26(2):1–20`, Campbell's volume, Wood's 2nd ed., Monmonier's 3rd ed., Jacob's French/English editions.

This is a legitimate right-sizing of r47's 18-item shelf **for the works that remain**. It is not yet reconciled with the body (P2).

---

## 5. In-lane registrations audit

| Item | Live evidence | Ruling for the entry |
|---|---|---|
| **Boone (2000), *Stories in Red and Black*** | Registered at `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:12`; reused at `direction-symbolism.md:8,78` | **Tier A**, not external-only. Cite the registration path; page-level quotations remain `(to-verify)`. `M02-calibration.md:34,137` currently lists it among external items — P1. |
| **Boone (2007), *Cycles of Time…*** | `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:17` | A **different work**; do not conflate with Boone 2000 (the r47 C06 warning stands). |
| **Needham (1959), vol. 3** | Registered in `cosmology-cosmography.md` `- sources:` at `:12` (body uses at `:66,:100,:114`) | Registered in-corpus; cite `:12` for registration. `M02-calibration.md:36` cites `:100` as the registration — P3. |
| **Harley** | `corpus/knowledge/civilizations/celts.md:167` mentions "British Library Harley MS 5280" | A manuscript **shelfmark**, not J. B. Harley. Do not promote or cite as an in-corpus registration of the historian. |
| **Ptolemy** | Corpus mentions Ptolemy's *Canon* (`era-periodization-models.md:13,98`) and *Analemma* (`timekeeping-instruments.md:5`), not the *Geography* | Keep *Geography* on the external shelf with `(to-verify)`; do not say it is registered in-corpus. |
| ***Tabula Peutingeriana*** | One incidental mention at `transport-mobility-lexicon.md:8` ("the network map") | Evidence the object is known in-lane, **not** a source registration. If the body names it, keep it `(to-verify)` and cite `:8` only as a coupling. |
| **OED** | Not on the r48 shelf | If the assembled body keeps the r47 §9 etymology/word-bank section (it named the OED as its check, r47 `C02-entry-b.md:369`), add OED to the shelf with `(to-verify)` or cut the section. `K01-rightsized-spec.md:98` recommends cutting §9, which would remove the need. |

No shelf item is claimed as inspected, and no in-corpus registration is falsely attributed in the head block itself.

---

## 6. Findings (provenance-specific)

**P1 — MEDIUM — Boone (2000) misclassified as external.** `M02-calibration.md:34` ("Mundy (1996), Boone (2000) — `(to-verify)`") and `:137` (lists Boone among "all external" items) present a work registered in-corpus as external. **Fix:** in the assembled entry, cite `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:12` as the registration and keep `(to-verify)` only for page-level use; or drop the name from the calibration row. Do not conflate with Boone (2007) at `mesoamerica-primary-sources.md:17`.

**P2 — MEDIUM — shelf/body mismatch.** The body cites works absent from `C02-header.md:129`:
- Mundy (1996) — `M02-calibration.md:34`
- al-Idrisi (1154) — `M02-calibration.md:36`
- Needham (1959) — `M02-calibration.md:36` (in-corpus Tier A; see P3)
- Boone (2000) — `M02-calibration.md:34` (Tier A; see P1)

The spec's own shelf groups also include Buisseret, Pickles, Edson, the *Tabula Peutingeriana*/*Antonine Itinerary*, and Ortelius (`K01-rightsized-spec.md:120-124`); the r47 body used Ortelius, Mercator, al-Idrisi, Blaeu and the *Tabula Peutingeriana* (`reports/round-47/cov/C02-entry-b.md:177,227-229,357,362`). **Fix:** C13/integrator reconciles the shelf to the surviving body citations — every named external work either appears on the shelf with `(to-verify)` or is cut from the body. Inline marks alone satisfy the smallest-proposition rule but not shelf completeness.

**P3 — LOW — Needham registration miscite.** `M02-calibration.md:36` says "registered in-corpus … at `corpus/knowledge/myth-symbol/cosmology-cosmography.md:100`". Live `:100` is a body row citing Needham; the `- sources:` registration is `:12`. **Fix:** cite `:12` for registration and `:100` for the body use, matching the r47 C06 distinction between "registered at" and "used at".

**P4 — LOW — one-line-off claims.json citation.** `C02-header.md:4` cites `reports/round-48/claims.json:6` for `baseline_commit`; the field is on line **7** (`grep -n baseline_commit` → `7:  "baseline_commit": "a01405d"`). This is the same file-correct/line-wrong class as r47's B4. **Fix:** `claims.json:7`.

**P5 — LOW — couples count says 18, line has 19 tokens.** The `- couples:` line backticks 19 `.md` paths, all of which resolve, including `../synthesis/worldbible-integration-contract.md` (`C02-header.md:130`). `C02-header.md:132` and §4.3 (`:202-227`) claim "18/18" and call the synthesis token "prose-side"; it is a backticked token like the rest. **Fix:** state 19/19, or remove the backticks if it is meant as prose.

**P6 — ADVISORY — topic digest convention.** `C02-header.md:109` gives `9424fb81…` as "sha256 of the seed line". The digest is over the line **including its trailing LF**; the bare line hashes to `a42926b1…` (§2). **Fix:** say "sha256 over the line plus its LF" or publish the bare-line digest, so the next verifier reproduces the same value.

**Adjacent, not mine to rule:** `M02-calibration.md:135` lists `civilizations/maori.md` among the neighbours it relies on, and `C02-header.md:130` does not couple it. `maori.md` exists and `M02:101` cites `maori.md:20`. Couples ownership is C09/A02; flagged here only because it surfaced during the registration audit.

---

## 7. Carry-forward checklist for C13/integrator

1. Fix P4 (`claims.json:7`) and P5 (19/19, or drop the synthesis token) in the header before lifting it.
2. Add the P6 LF convention beside the topic digest.
3. Reconcile the shelf with the surviving body: add Mundy, al-Idrisi, Needham (Tier A), Boone (Tier A) if cited; add or cut OED, Ortelius/Mercator/Blaeu, *Tabula Peutingeriana* per body.
4. In M02 rows 4 and 6, split Tier A (in-corpus registration path) from external `(to-verify)` works; do not call registered works external.
5. Keep every `(to-verify)` adjacent to its specific locator — no section-level blanket substituting for a per-item mark (citation-format `:35`).
6. Re-run §8 after assembly; the expected result is 11/11 pins (or the then-current pin count), all couples resolving, and every shelf item marked.

---

## 8. Re-runnable audit (alternate digest check needs no hash of a hand-built string)

```python
import re, hashlib, os
p='reports/round-48/cov/C02-header.md'
t=open(p).read()
pins=re.findall(r'`(corpus/knowledge/[^`]+\.md)` \(sha256 `([0-9a-f]{64})`\)', t)
for f,h in pins:
    assert hashlib.sha256(open(f,'rb').read()).hexdigest()==h, f
topic=[l for l in t.split('\n') if l.startswith('- topic:')][0]
seed=open('reports/round-44/scout/K02-gap-scout.md').read().split('\n')[226]
assert topic==seed
assert hashlib.sha256((topic+'\n').encode()).hexdigest().startswith('9424fb81')
cou=[l for l in t.split('\n') if l.startswith('- couples:')][0]
for tok in re.findall(r'`([^`]+\.md)`',cou):
    path=tok if tok.startswith('corpus/') else os.path.normpath(os.path.join('corpus/knowledge/culture-material',tok))
    assert os.path.exists(path), tok
# every shelf item marked: split on top-level semicolons
shelf=[l for l in t.split('\n') if 'External standard shelf' in l][0]
s=shelf.split('no unread work is presented as inspected:')[1]
items=[];buf='';depth=0
for ch in s:
    depth += ch=='('; depth -= ch==')'
    if ch==';' and depth==0: items.append(buf); buf=''
    else: buf+=ch
items.append(buf)
assert all('(to-verify)' in x for x in items if x.strip())
print(f'PASS pins={len(pins)} couples={len(re.findall(r"`([^`]+.md)`",cou))} shelf={len(items)}')
```

---

## 9. Limits

- **No network.** I certify that no external work is *presented as inspected*; I do not certify bibliographic accuracy (volume counts, page ranges, edition years). Those stay `(to-verify)` by design.
- **Body unassembled at my read cut.** P2's shelf/body mismatch and P1/P3's body-side fixes are conditional on the body sections that survive integration; they are not defects in the head block's own bytes.
- **Not mine:** entry length/structure (C05/C17), arithmetic (C03), landing safety (N03/V01), couples ownership (C09/A02).

## 10. Write surface

Wrote only `reports/round-48/cov/C18-provenance.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, frozen gate, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network, no in-tree `run-validation.py`.
