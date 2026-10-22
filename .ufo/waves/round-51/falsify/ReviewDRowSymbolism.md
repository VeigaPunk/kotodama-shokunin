# ReviewDRowSymbolism: falsify attack on claim D, row 45

Seat: KotodamaR51a3.ReviewDRowSymbolism (leaf, read-only on the lane).
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. Date: 2026-10-22.
Landed claim D: commit 35f0d49. The entry's worktree equals HEAD (`git diff --stat HEAD` empty).

## Item attacked

Row 45 of the section-2 one-owner boundary table, `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:45`, anchor `symbolism-synthesis-method.md:69`. Axis: depth.

## Verdict: FAILS (row 45 as landed)

The anchored line supports only the first clause of the ownership cell. The boundary repeats a herd-side rite cost that row 44 already holds, and it rests on the body's one `(to-verify)` herd claim without the marker. The repairs are local (one row and one lead sentence), but the row fails the claim's own falsifier as written.

## Answers to the four questions

**1. Does the anchored line support the "What it owns" cell?**
Anchored line, `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:69` (§4.2 "Animal", a register note; §4 header at :57, §4.2 at :66):

> "**Prey apologetics**: a hunting culture that keys a prey animal symbolically generates apology and release rites for the kill — the Circumpolar bear ceremonial is the classic case (Hallowell 1926). An animal taboo implies a rite; write both or neither."

Cell: "the consistency rule that an animal taboo implies a rite, and the symbol grammar that enforces it".

- Clause 1 matches the line's last sentence. The label "consistency rule" is not the source's category. Its §5 "Consistency rules" (:93) lists R1–R8 (:95–102), and none of them states the taboo→rite implication.
- Clause 2 ("and the symbol grammar that enforces it") is not on :69. The line has no "grammar", "enforce" or "audit" wording. Support exists elsewhere in the same file: title :1, topic :3 (which names "the consistency rules … and the symbol-audit checklist"), R1–R8 (:95–102), and the audit checklist (:120–146). The row anchors none of these. `synthesis/symbolism-consistency-rules.md:53–64` (§4, "Invariants for a closed symbolic grammar") also owns enforcement and is not named.
- Result: the cell overclaims relative to its anchor. The falsifier ("anchored line does not support its ownership cell") is met as worded.

**2. Is the boundary developed or narrowed in the body at the section the cell names (§10)?**
Body line, `pastoralism-animal-husbandry.md:155`, §10 "Sacrifice economy":

> "| Sacrifice economy | offerings drawn from the herd's surplus males `(to-verify)` | an animal taboo implies a rite (`symbolism-synthesis-method.md:69`); sacrifice belongs to myth-symbol |"

- Narrowed: yes, for the rite ("sacrifice belongs to myth-symbol").
- Developed: only as a `(to-verify)` herd cost. §10 (:146–158) develops no herd taboo: it cites the rule once, as the antecedent in the "Sacrifice economy" row. The only herd taboo–rite pair is in the NON-CANON example at :184 ("…no shears may touch a fleece on the day of the count (rite and taboo written together, `symbolism-synthesis-method.md:69`)"). That example sits under the heading "NON-CANON" at :180–182. §11 step 8 (:171: "each taboo written with its rite | §10") sends the reader to §10 for a herd taboo that §10 does not develop.
- Round 51 added no body text for this row. `git show bff83ba` shows the §10 row at base line 147 (now :155), the §11 step at base :163 (now :171), and the §12 example at base :176 (now :184). The D diff hunks touch only :29, :42, :44–47 and :93.

**3. Duplicate authority, or laundering of a `(to-verify)` claim (check "surplus")?**
- Duplicate: yes. Row 44 (`pastoralism-animal-husbandry.md:44`, neighbour `ritual-liminality.md:63`) gives the boundary "which animals and products the herd can spare; the rite's form, meaning and budget stay there (§10)". Row 45 gives "the herd-side cost of each paired taboo and rite (§10)". Both assign the herd-side cost of rites to the same single body row (:155). The §10 intro (:148, "write the rite from the herd's books outward") routes the same books to row 44's neighbour. The two rows are not split.
- Laundering: yes. A search for "surplus" on the entry returns one line, :155, and it is marked `(to-verify)`. Row 45's boundary makes that unsourced herd offering load-bearing without the marker. `corpus/QUALITY.md:5–8` says a claim the author cannot verify "is marked `(to-verify)` inline — never laundered into assertion". `calibration-registry.md:39` (code T) says "do not make it load-bearing".
- Checked, no duplicate: row 41 (`animal-symbolism.md:73,:110`) owns the herd's signs and the livestock idiom. `animal-symbolism.md` §5 (:59–75) owns food-law taboo content. Neither owns the taboo→rite implication. The hunting entry cites the same line for wild prey (`hunting-foraging-subsistence.md:15, :65, :133, :145`) and assigns it to the synthesis method, which is consistent with row 45. No competing owner.

**4. Genuine neighbour or filler?**
Genuine as a method neighbour; filler in depth this round.
- The synthesis method is the right owner of the implication rule, and the entry applies it (§11 step 8, §12).
- But the synthesis file has no herd, pastoral, sacrifice or offering content (a search returns no matches).
- The anchored example is a hunting culture's prey. The herd use relies on the rule's generality, which the cell does not say.
- The row adds a count for a neighbour the body already cites twice (:155, :171), both of which predate round 51.

## Findings

| # | Severity | Location | Finding | Smallest fix |
|---|---|---|---|---|
| F1 | high | `pastoralism-animal-husbandry.md:45`, cell "What it owns" | Clause 2 ("and the symbol grammar that enforces it") is not supported by the anchored line `symbolism-synthesis-method.md:69`. This meets the falsifier as worded. "The consistency rule" also mislabels a §4.2 register note as one of the §5 rules R1–R8. | Delete ", and the symbol grammar that enforces it", and change "the consistency rule" to "the register rule". If enforcement stays, anchor `symbolism-synthesis-method.md:95-102` or `:120-146` and name `synthesis/symbolism-consistency-rules.md:53-64` as the other owner. |
| F2 | medium | `:45` boundary; `:44` boundary; `:148`; `:155` | Two rows own the same herd-side rite cost (`ritual-liminality.md:63` and `symbolism-synthesis-method.md:69`), and both point at the one body row `:155`. | Narrow row 45's boundary to the implication only: "a herd taboo is written with its paired rite (§11 step 8); the rite's herd-side cost stays with row 44 (§10)". |
| F3 | medium | `:45` boundary → `:155` | An unsourced herd offering ("surplus males", `(to-verify)`) becomes a §2 boundary with no marker. Row 44 ("can spare", `:44`) rests on the same claim; it is not my row, flagged for the integration owner. | Drop the herd-side cost from row 45 (F2 fix). Add the `(to-verify)` marker at the dependency in row 44, or narrow row 44 too. |
| F4 | medium | `:45` boundary; `:155`; `:171`; `:184` | Depth: "each paired taboo" is not developed at the named §10. The only taboo–rite pair is the NON-CANON example at :184. Round 51 added no body text for row 45. | Narrow the cell to what §10 develops: "the rite side narrowed to myth-symbol (§10, :155); the herd-side offering `(to-verify)`". Drop "each paired taboo". Alternatively, add one §10 sentence on herd taboos with a `(to-verify)` flag, if it can be sourced. |
| F5 | medium | `:29` (D's lead sentence) | The lead says "the body section named in the boundary cell develops it". That is false for row 45 (F4). | Change `:29` to "narrows or develops it", or fix row 45 per F4. |
| F6 | low | `:45`, anchor context | The anchored bullet's example is wild prey. The herd use is by analogy, and the cell does not say so. | Fold into the F1 fix, or add "by the rule's generality" to the boundary. |
| F7 | low | `reports/round-51/boundary-count.py:85`, `:44–60` | Measurement blind spot. The counter reads only the Neighbour cell (`row.split("|")[1]`) and checks only file uniqueness and line range. "15/15/15" says nothing about the ownership or boundary cells. | None to the row. Do not cite the counter as support for row 45's content. |

## Checked and clear

- Must-not-cite: an entry-wide search for `S(07[1-9]|0[89]\d|[1-9]\d\d)\b|sign-lang|manual-modality|round-51|boundary-count|finger count` returns no matches. Row 45 cites no S-id and no claim-C path.
- Anchor line 69 is unchanged since base (`git diff --stat bff83ba HEAD` on the synthesis file is empty; last touched in `e1694ba`).
- The counter output `rows=15 resolved=15 distinct=15` matches the required value. Row 45 names one neighbour, distinct from the other fourteen.

## Commands run (lane root; exit codes as shown)

| # | Command | Output (abridged) | Exit |
|---|---|---|---|
| 1 | `python3 -B reports/round-51/boundary-count.py` | `rows=15 resolved=15 distinct=15` | 0 |
| 2 | `git rev-parse --short HEAD`; `git log --oneline -3 -- <synthesis file>`; `git diff --stat bff83ba HEAD -- <synthesis file> <pastoral entry>` | HEAD `9feb69e`; synthesis last touched `e1694ba`; the diff touches the pastoral entry only (9 insertions, 1 deletion) | 0 |
| 3 | `git diff -U0 bff83ba HEAD -- <pastoral entry>` | hunks `+29,2`, `-40 +42`, `-41,0 +44,4`, `-86,0 +93,2` | 0 |
| 4 | `git show bff83ba:<pastoral entry> \| grep -n "Sacrifice economy\|Sky figures\|Shepherd-king\|symbolism-synthesis-method"` | base lines 146, 147, 148, 163, 176 | 0 |
| 5 | `git log --oneline -3 -- <pastoral entry>`; `git diff --stat HEAD -- <pastoral entry>`; `git diff --stat HEAD -- <synthesis file>`; `realpath`/`test -d` on the falsify folder | `35f0d49` is the latest; both diffs empty; falsify folder present inside the lane | 0 (all) |

Search-tool calls (not shell; no exit code):
- `symbol grammar|symbolic grammar|sign grammar` over `corpus/`: many hits; none is at synthesis line 69.
- `taboo|tabu|prohibit|forbidden` in the pastoral entry: matches at :45, :155, :171, :184 only.
- `herd|pastoral|sacrific|offering` in the synthesis file: no matches.
- `surplus` in the pastoral entry: :155 only.
- `symbolism-synthesis-method\.md:69` over `corpus/`: hunting-foraging-subsistence.md (:15, :22, :65, :133, :145) and the pastoral entry (:6, :45, :155, :171, :184).
- Must-not-cite pattern (above) in the pastoral entry: no matches.
- `taboo|rite|sacrific` in `synthesis/symbolism-consistency-rules.md`: :58, :75, :79. None states a taboo→rite rule.

Read calls (line ranges): claims.json; pastoral entry 1–100, 104–212, :8 and :184 raw; synthesis file 1–44, 54–88, 89–172; animal-symbolism 69–78, 107–115; ritual-liminality 60–68; consistency rules 1–15, 49–79; calibration-registry 32–43 and :39; `corpus/QUALITY.md` 1–12.

## Sources opened

None. Row 45 cites only in-corpus anchors and no S-id. Hallowell (1926) appears inside the anchored line but is not part of the cell. No URL was opened and nothing was downloaded.

## Tooling

No installs. No package or binary was added. Tools used: python3 (standard library, already present), git (read-only), and the read and search tools. The `lsp` device is not present in this seat. Markdown has no code callers, so text search was used only as a literal check.

## Residual risk and verification gaps

- Unrun (outside row 45): the separability command, `reports/round-28/readme/sweep.py`, and the claims-agree check.
- The round-50 finding that "surplus males" are unsourced appears only in an author-lane note (`.ufo/waves/round-51/build/CriticClaimD.md:94`). I did not verify it.
- I read the §12 example as illustrative, because it is labelled NON-CANON. I did not treat it as herd-side evidence.
- The strict reading holds the cell to the anchored line. File-level support for clause 2 exists at :1 and :3, so an author could argue the cell describes the file. That argument does not meet the claim's own test ("supported by the anchored line(s)").

## Context (author-lane notes; not evidence)

- `.ufo/waves/round-51/build/CriticClaimD.md:93–96` and `:150–151` raise the same concerns as F2–F5: zero-development rows, laundered "surplus males", and duplicate authority.
- `.ufo/waves/round-51/build/ExecBoundaryCounterControls.md:37` labels this anchor "herd supply, not symbolic grammar". That contradicts the landed clause 2.
- `.ufo/waves/round-51/build/ScribeRowSymbolismSynthesisMeth.md` section (b) says "No new body text is required". Its line 24 notes that the ownership-supporting sentence is the 11-word "An animal taboo implies a rite; write both or neither."
