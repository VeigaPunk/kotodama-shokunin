# Round 77 DRAFT claim critique — CritClaims1

Review scope: claim design only, before freeze. No counter, tests, or campaign commands were run.

## F1 — C's narrow gap is plausible; preserve the partial-coverage distinction (low)

The base is not wholly blank on Chinese personal-name structure: it already says Chinese surname-first plus a generation-pool character, explicitly labels 姓/名 order, discusses compound surnames and multi-character personal names, and warns against imposing a later 姓/氏 distinction on early records. These are partial coverage, not the specific diachronic claims (名 predates 姓; 姓+名 as a contact-era acquisition) or the finite female given-name lexeme classification proposed here. The updated DRAFT acknowledges those neighboring facts and reports claim-specific term sweeps; my independent sweep found no match for the target terms in Chinese naming material. This is a wording/ground-boundary risk, not evidence that the proposed target is already covered.

Evidence:
- Command: `git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/knowledge/linguistics/naming-systems.md | grep -nE '姓|名|China|Chinese|bìhuì|lexeme|given name|personal name|single|double|mono|disyll' | head -60`
  Raw output: `54:- Chinese | surname first + given + generation-pool character; hereditary surname ~ancient; emperor's personal name banned in print (see §6)` and `60:- Formation rules ...`; `61:- The name lexicon ...` (Japanese character restrictions, not Chinese-name classification).
- Command: `git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/knowledge/civilizations/china-song.md | grep -nE '姓|名|China|Chinese|bìhuì|lexeme|given name|personal name|single|double|mono|disyll' | head -15`
  Raw output: `176:| Surname and personal name, 姓 / 名 | Surname normally precedes the personal name in Chinese order | Do not treat a European-style given-name-first display as indigenous order |`.
- Command: `git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/knowledge/civilizations/china-han.md | grep -nE '姓|名|China|Chinese|bìhuì|lexeme|given name|personal name|single|double|mono|disyll' | head -15`
  Raw output: `144:| Family + personal name | 董｜仲舒, Dong Zhongshu; 公孫｜弘, Gongsun Hong; separators show surname/given-name boundaries. [HS 56] | Compound surnames and multi-character personal names both occur; do not impose one fixed syllable count or split every name after its first character. |`.
- Command: `git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/knowledge/civilizations/china-shang-zhou.md | grep -nE '姓|名|China|Chinese|bìhuì|lexeme|given name|personal name|single|double|mono|disyll' | head -15`
  Raw output: `167:- Do not impose a later, fully regularized xìng 姓 / shì 氏 distinction on every inscription; exact reconstruction of a named individual's affiliation remains (to-verify).`
- Command: `git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge; echo "EXIT:$?"`
  Raw output: `EXIT:1` (no matching files).
- Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -n -E '名 predates|predates 姓|contact-era acquisition|單名|雙名|female naming|Flowers, Plants|88 terms denoting plants|植物|花卉' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge`
  Raw output: `211f9526800906e0c585d878d265c37e5e090c15:corpus/knowledge/civilizations/celts.md:190:- **Thin coverage:** Celtiberian ritual, Galatian local dress, Pictish inscriptional problems, regional textile cuts, and detailed female naming practice are not adequately reconstructed here. Exact local forms and associations are not established by the sources checked here, not gaps to fill with Irish analogies.`; command exit 0. This is an unrelated Celtiberian note, not coverage of the proposed Chinese naming target.

Smallest correction: state explicitly that the gap is the *diachronic 姓/名 account and the cited finite given-name classification*, acknowledge the existing partial coverage, and ground the negative sweep in those claim-specific concepts/scope as well as source absence. The proposed one-entry/two-row target is falsifiable and appears reachable in one round; the analogous r76 acceptance receipt recorded one admitted knowledge entry and three new source rows in one landing. The freeze==lands control is structurally falsifiable because the required entry/rows/data legs cannot be satisfied by an unchanged freeze; keep the exact red data-leg list in the frozen control receipt.

## F2 — ROWS scope fix needs a global non-row-diff guard, not just row counting (medium)

The proposed `required_sections[]` addresses the actual r76 counterexample: the prior ROWS leg rejected non-row prose added to the `## Paths` and `## Search log` sections of `corpus/SOURCES.md`. But “ROWS counts only S-row lines” by itself stops validating unrelated non-row changes everywhere else in SOURCES.md. Unless INDEX checks an exact whole-file diff partition, an extra non-row line outside the enumerated sections—or deletion of an existing non-row line—could escape both the row-set comparison and a section-local check. A row-shaped line added in an exempt section must still fail unless it is exactly in `row_set`.

Evidence:
- Command: `tail -60 reports/round-76/telemetry/measures-c.txt`
  Raw output includes `LEG FAIL ROWS` and `registry line added outside the frozen row_set: '- calendar-standard design — S896 → S895 → S894: start with '; registry line added outside the frozen row_set: '**State-standard calendar compilation (round 76).** Question`.
- Command: `git show 722e69ff6361aadf148cb46acbf6ac8fd147f59a:corpus/SOURCES.md | grep -n -F -e 'calendar-standard design' -e 'State-standard calendar compilation' -e 'Paths' -e 'Search log' | tail -25`
  Raw output: `853:## Paths`; `854:- calendar-standard design — ...`; `890:## Search log`; `902:**State-standard calendar compilation (round 76).** Question: ...`.

Smallest correction: define the SOURCES delta as a partition: globally require added row-shaped lines to equal the frozen `row_set` with no duplicate/removal; globally reject removed pre-existing non-row lines; permit added non-row lines only when byte-exactly enumerated by `required_sections[]`; have INDEX verify those exact sections and reject all other non-row additions/removals. This both permits the two r76 lines and prevents a broad section exemption from becoming a bypass.

## F3 — Ca's kill rule is narrower than its 12-leg acceptance contract (low)

The updated DRAFT does retain NOSTUB and enumerates it in the exact 12-leg lineage list; this closes the earlier placeholder-token omission. It also fixes the r76 schema defects directly: disposition-specific `stated_at` allowlists, base-line `stated_text` presence, constrained argv grammar, committed receipts, and a path+line for the combined README exemption. The remaining precision issue is that the kill rule does not state that *any* failed leg fails the claim (notably an R1EXEMPT or COMBINED failure); the counter's required PASS 12/12 should enforce that operationally, but the declaration-level rule should say so to avoid a gap between named kill cases and the pass contract.

Evidence:
- Read: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/CLAIMS-DRAFT.md:25-34`
  Raw output: line 29 names all 12 legs including `NOSTUB`, says “COMBINED README exemptions carry actual path+line” and “strict APPENDONLY/SEPARABLE and NOSTUB remain”; line 31 requires `PASS 12/12`; line 33 lists kill conditions but no general false-leg condition.
- Read: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-76/accept-ca.py:2074-2122`
  Raw output includes the `NOSTUB` leg's `if tokval is not None and _placeholder(tokval)` check and `return leg(out, "NOSTUB", not stubs, ...)`.

Smallest correction: add `any leg false (including R1EXEMPT/COMBINED) => claim fails` to the kill rule. No separate NOSTUB implementation gap remains in this DRAFT.

## F4 — Ca/C has deliberate APPENDONLY path overlap; combined boundaries must stay exact (low, integration risk)

Ca and C are not path-disjoint: C appends source rows in `corpus/SOURCES.md` and changes `corpus/README.md`; Ca's APPENDONLY/R1-exemption and README repair/combined rules also inspect those files. This is separable, and the updated DRAFT explicitly pins the combined README exemption to path+line and says APPENDONLY is strict. The residual integration requirement is that the combined evaluator allow only C's frozen new row-set additions and exact C-owned README edits while still rejecting other non-rule-2 edits to pre-existing SOURCES rows. A generic path exemption would hide Ca changes; a strict no-change rule would reject C.

Evidence:
- Read: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/CLAIMS-DRAFT.md:21`
  Raw output: C requires `registry 820→822 rows (S897/S898...)` and a README index/footer update.
- Read: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/CLAIMS-DRAFT.md:29`
  Raw output: “COMBINED README exemptions carry actual path+line; strict APPENDONLY/SEPARABLE...”
- Read: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-76/accept-ca.py:554-620`
  Raw output: `sources_diff` compares pre-existing rows cell-wise, rejects changed cells outside rule-2, and rejects removed non-row lines; appended rows are not edits to pre-existing rows.
- Command: `tail -60 reports/round-76/telemetry/measures-ca.txt`
  Raw output: `LEG FAIL COMBINED — the C-owned README heading change at line 410 is outside Ca's frozen APPENDONLY exemption; the owned_inplace config has no valid line number.`

Smallest correction: retain the DRAFT's path+line pin, and make the combined APPENDONLY clause explicitly recognize only C's frozen row-set additions and exact README ownership lines. Reject all other changed pre-existing SOURCES cells, unrelated README edits, and removals. The numbered exemption resolves the specific r76 failure; no demonstrated causal-separability blocker remains if the counter enforces this boundary.

## Overall

The updated DRAFT addresses NOSTUB and the named r76 ledger/REPAIR/ANNOTATE/R1EXEMPT/COMBINED defects in its 12-leg set and schema notes; the remaining Ca wording improvement is a generic false-leg kill clause. F2 needs a global SOURCES non-row-diff partition, not a broad section exemption. C's underlying gap is supportable when phrased narrowly: the base has partial 姓/名/name-length coverage, but the specific diachronic account and finite female-given-name classification are not evidenced by those base entries.
