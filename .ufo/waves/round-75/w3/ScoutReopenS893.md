# S893 independent reopen — W3

## Fetch and quote

Independent ordinary GET to the registered URL using `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`: HTTP **200**, final URL unchanged, downloaded body **17,005 bytes**, SHA-256 `51251e22c617617af797d164684e8927dc792a06140ff35fbaebc158515415f0`. `reports/round-75/evidence/S893.txt` records HTTP 200, body 45,238 bytes, same SHA-256. Thus **hash equal, byte count differs**; same digest despite transfer size discrepancy. The evidence extractor says UTF-8, visible text 7,711 chars; its excerpt window is chars=4103, min=4096, pad=400, before=2032/after=2032, 12,231 UTF-8 bytes, window SHA-256 `5e197a57a89464e641435aa0be1519db1e0b3e0bfc61120500d3483c7ef22a6c`. The committed window is excerpted from the paragraph immediately preceding the quote, then includes the quote in its own `--- quote ---` block. The observed body hash exactly matches the evidence body's hash, so this is not page-content drift.

Normalized (NFKC + whitespace folding) Gate quote is found verbatim: `网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则`. Evidence locator: §「世界观是打开小说幻想屋的钥匙」, byline 三九音域, paragraph 1, sentence 2. The page text and stored window agree for this passage.

## Registry row

S893 is community/C, scope “the native practitioner vocabulary of Chinese web-fiction world-building …” and explicitly limits the claim to a lead-level register, never sole support. **Tier agrees**: this is an industry-outlet practitioner account, not peer-reviewed scholarship or authoritative universal theory; C is appropriate for vocabulary/practice framing. Scope matches the page: its sentence defines the term 世界观 in the context of network fiction and story-setting rules. Row recheck is **180d**; the lesson normalizes recheck cells to cadence-only 180d, which is coherent. `used-by` should be exactly `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`: grep finds S893 only there; neither dated amendment cites S893.

## Entry claim audit

The only S893-cited explanatory prose is in `narrative-structure-frameworks.md`:

- “The practitioner section opens with the figure the term belongs to: the author likes to imagine writing a novel as inviting the reader into a fantasy house he has built, and the key that opens the house is 世界观 (S893).” — The page's section heading itself is «世界观是打开小说幻想屋的钥匙» and the body discusses that analogy. **Carried.**
- “It then gives the working definition: in a web novel, 世界观 refers to the way the ten thousand things of the story's setting operate, the scene and the rules in which the story happens — rules that differ from those of the real world we live in, and it is precisely because of th…” — the quote directly supports the definition and scene/rules language. **Carried for the definition.** The fetched snippet has no contrary content; the remaining comparison is presented as the article's continuation. No sentence-level mismatch found.
- “That is a rule-system reading of the term rather than a props list, and it is exactly the reading a world bible can store. The status is **tier-C vocabulary**: an industry outlet, one author's account of his own practice, and never sole support for an admitted claim. This entry borrows the word and the rule-system sense, and borrows no warrant from it.” — first sentence is the entry's characterization/application, not a claim attributed as page wording; C limitation accurately describes source type; no unsupported page-specific assertion identified.
- “It does not read 世界观 as a warrant of any kind; the term is vocabulary at tier C (S893).” — accurately scopes citation as terminology, not warrant.

No page-unsupported sentence identified among the S893 citations. **Verdict: HOLDS** (one metadata anomaly: evidence records 45,238 body bytes while independent GET transferred 17,005; matching SHA-256 establishes same body bytes notwithstanding the reported size discrepancy).
