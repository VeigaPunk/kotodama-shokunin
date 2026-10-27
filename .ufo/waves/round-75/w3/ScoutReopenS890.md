# S890 independent reopen (W3)

## Fetch and Gate quote

- Independent plain GET to `https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf`, using `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`: HTTP **200**, final URL unchanged, **697092** downloaded bytes. SHA-256: `1dccf9d1427defb0e07e99461301cfd0ef5b5734716783a8ba0bb782de422272`.
- Frozen committed receipt `reports/round-75/evidence/S890.txt` records the same UA, HTTP 200, 697092 bytes, and same SHA-256. **Hash equality: yes; no content movement observed.**
- After per-character NFKC and whitespace folding, Gate quote `describe a story as a hierarchical structure consisting of three major layers` found **yes**, PDF p. 1 English abstract (extracted-text normalized index 688). Context: “In this research, a method to describe a story as a hierarchical structure consisting of three major layers of story, quest, and scene is proposed.” The committed stored window also contains it; its recorded window SHA-256/bytes are `0b3a5e7b59bc4f31901d9c024d8790258ecf5bf7c15a3d7f6a98e8736bdbb127` / 9920. 
- Evidence re-fetch/capture details: GET, browser-shaped UA above, HTTP 200, 697092 bytes; independently hashed downloaded PDF. Scratch copy was deleted before report completion.

## Registry checks

Registry row `corpus/SOURCES.md:845` is Tier **B**, with reason “the author's own proposal, in a conference presentation abstract”; this agrees with its own framework being a proposal rather than established result (entry §6). Scope is explicitly a Japanese-language, machine-writable three-layer description format and its treatment of 起承転結 as a completable minimal unit. Status `mined`; recheck `180d`. Used-by is exactly `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`, the sole document whose `source:` line cites S890; neither named amendment contains S890 in its source/citation lines.

## Claim sentence check

The following S890-attributed entry claims were compared with the reopened article. All are carried by the paper; no unsupported sentence identified.

- §4: the six listed actant kinds and their roles changing per goal, hence assignment at quest rather than character level. The paper's description discusses the six actant types and explains role change relative to goals as reason for quest-level placement.
- §4: the consequent character having different roles across quests. This is the paper's stated implication; the invented-culture boundary-map interpretation is explicitly marked as the entry's own reading, not source fact.
- §6 opening: three layers (story/quest/scene), unified description of plot, characters, events; borrowed analytic reference points (Propp, Greimas, Genette). The paper's abstract/introduction carries these.
- §6 layer account: scene/function and within-place segmentation, 起承転結 fitting within a scene; quest as minimum goal-centered 起承転結 unit; multiple quests and their relations. The paper's discussion carries these.
- §6 layer assignments for story, quest, scene; character and event layers. Paper sections 2–4 carry these details.
- §6 limitation: components checked against existing-work analyses, whole structure validity/usefulness left for empirical accumulation. Paper's conclusion carries this qualification.
- §8 checklist: assign actant slots per quest; split quests into scenes at function changes and state relations between neighboring quests. These operational recommendations reflect the paper.
- §9 caveat: framework remains a proposal, not a finding, pending empirical work. Supported by the conclusion.

The only S890 citations are in the base entry. Amendment `...amend-2026-10-23.md` and `...amend-2026-10-23b.md` have no S890 mentions. Confidence: high for file/hash/quote and registry cells; high for the located textual claims based on independent PDF extraction and comparison. No unresolved S890-specific gap found.
