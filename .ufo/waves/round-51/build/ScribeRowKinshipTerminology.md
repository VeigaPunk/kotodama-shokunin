# ADD — kinship terminology is a distinct neighbour

## Assigned item and axes

Claim D candidate review only: depth through a substantive ownership seam, with anchor support, neighbour distinctness and the 250-line ceiling as constraints. Author-lane advice, not admission or a canonical judgment.

Both candidate entries were read fully at the lane worktree, including initially truncated long lines. Claim provenance: `reports/round-51/claims.json:15-27`; declared base `bff83ba65bf9559af4d7567e81703059667a0005`. No independent byte comparison against that base was performed.

## Ready-to-paste row

| `kinship-terminology.md:64` | kin terminology as weighted evidence about residence, inheritance and marriage | herd inheritance and bridewealth transfer rules, specified separately rather than inferred from kin labels |

Anchored line, verbatim (`corpus/knowledge/linguistics/kinship-terminology.md:64`):

> - Procedure: weight terminology as one vote among (a) residence, (b) inheritance, (c) marriage rule, (d) economy. A mismatch among them is a *feature*: assign it an in-world history (conquest, conversion, class divergence between elite and folk registers).

The neighbouring entry explicitly rejects treating terms as transcriptions of social rules at `corpus/knowledge/linguistics/kinship-terminology.md:60`; its descent/alliance discussion is at line 82. These support a deliberately narrow ownership cell, not a claim that kin terminology owns property law.

## Body development

Existing foothold: pastoralism §7, `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:101-108`, already asks who gains rights, describes bridewealth between kin, and distinguishes transfers. It does not yet explicitly separate kin labels from transfer entitlements. Add this one sentence after the opening paragraph at line 101:

> Use `kinship-terminology.md:60,:64` to label relatives and test social inferences; specify herd inheritance and bridewealth recipients, retained use-rights and offspring claims separately, since kin terms do not determine who acquires an animal.

The sentence is under 40 words. It adds a design check, not an empirical inheritance rule or new external-source claim. One table row plus the sentence and a separating blank line would take the observed 204-line entry to 207 lines, if integrated exactly without other changes; this is arithmetic, not an observed integration result.

## Distinctness and falsifier

The existing eleven neighbours occupy pastoralism lines 31-41; none is this file. The nearest overlaps are money words (line 35), the pastoral vocabulary field (line 37), and livestock-as-wealth symbolism (line 39). None owns the inference from kin categories to inheritance or marriage arrangements. This adds a separate diagnostic dependency, not another money-word, herd-word or symbolism row.

Falsifier: reject this row if a non-author review finds line 64 does not support the stated weighted-evidence ownership, if the target duplicates an existing neighbour at integration, or if the body still infers animal entitlements from a kin label without separately specifying the transfer rule. A row added without the proposed narrowing does not establish the full recommended seam.

## Observed execution, gates and limits

One read-only shell call was made, exactly:

```sh
wc -l /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/linguistics/kinship-terminology.md && cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-51/boundary-count.py
```

Observed output:

```text
164 /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/linguistics/kinship-terminology.md
rows=11 resolved=11 distinct=11
```

The baseline counter execution went beyond the source-review-only need; it was not rerun. No post-edit counter, test, build, formatter, separability check or canonical judge was run. The observed baseline is not evidence that this proposed row has landed or that the four-row claim passes. Integration must still satisfy the declared exact total of fifteen supported, resolving, distinct neighbours.

Touched surface: this report only. No product code, corpus entry, source registry, index, Git index or deployment state was changed. No tools installed, external sources opened, new source IDs introduced, or Claim C work performed.

Artifact: `.ufo/waves/round-51/build/ScribeRowKinshipTerminology.md`.
