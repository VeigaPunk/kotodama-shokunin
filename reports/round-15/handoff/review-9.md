# R15-O09 — reviewer: claim-ledger semantics (zero-boilerplate uncertainty + claim-to-record links)

- seat: **R15-O09** (reviewer, claim O, round 15 — operator regimen loop 1, GLM round 1 of 2), 2026-10-17 local (-03:00); window 21:24–22:05 local = 2026-10-18T00:24–01:05Z.
- assignment (verbatim): "O R15-O09..O10 (reviewers): adversarial — boilerplate basis = finding; dangling link = finding; aggregated coupling surviving = finding; reports/round-15/handoff/review-<n>.md."
- write scope: **this file only** (plus in-lane scratch `.scratch/r15-review/`; `TMPDIR=$PWD/.scratch` set before every scratch-writing command). No tool, packet, corpus, or filed round-8–14 byte was written; no git operation; no canon, rank, or real-world rights claim. All artifacts reviewed are NON-CANON.
- tree at review: HEAD `c60b17c` ("round-15: declare GLM-1 claims O/D…"), all round-15 work untracked.
- adversarial stance: this seat does not trust the round-15 tools; every tool result below was re-derived by an independent census, and the tools themselves were probed with falsification fixtures.

## 0. Object under review, stamped

The packet iterated three times inside the window. This review is **pinned to the 21:55:57 -0300 bytes**:

| object | sha256 | note |
|---|---|---|
| `reports/round-15/handoff/packet-v2-05.md` | `24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b` | gate-facing markdown, mtime 21:55:57 -0300 |
| `reports/round-15/handoff/packet-v2-05.yml` | `39cf4d53b02a1a9026e3a9a302cd1031d1b6a55fc2b8ea9d7b7eb877fa1dfcd6` | machine twin, same mtime |
| `reports/round-15/handoff/v2-design.md` (O01) | `9a6057315e4a63598ab3c70209a41aa466ebbd42768308b42f40f1328ac00a26` | the spec the packet is judged against |
| `reports/round-15/handoff/shard-1.md` / `shard-2.md` | `173dc03c…` / `3499152f…` | O03/O04 impl evidence (mtimes 21:50) |
| `tools/harness/packet_uncertainty.py` | `cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26` | uncertainty judge |
| `tools/harness/packet_links.py` | `f81bc9f77527a16184f9ad5a5a8ba80a945e0431ec80a63f426dfb3cab8176bc` | link judge |
| `reports/round-15/run-validation.py` | `25314d2b60feba2ad9785c0d492b7e0cda6bce25e277958caa5427e91237fb90` | round counting command |

Byte-drift warning: if these digests no longer match the tree, the parent must re-run §4's battery on the final bytes before recording the O verdict; §5's findings are stated against the stamped bytes only.

## 1. Verdict — the assigned criteria

**Boilerplate basis: none found (PASS). Dangling link: none found in the packet (PASS); one dangling-link detector bypass found in the harness (F9-1, harness-level).**

Supporting measurements, all run 2026-10-17 21:57–22:03 -0300 from the lane root unless noted:

### 1.1 Zero-boilerplate (15/15 claims)

- Tool leg: `python3 tools/harness/packet_uncertainty.py --packet reports/round-15/handoff/packet-v2-05.yml` → `claims=15 findings=0`, exit 0. Its `--selftest` → 19/19 checks.
- Independent census (own parser, not the module's): ledger rows = **15** (`packet-v2-05.md:82` section); statuses all in enum — **supported 8, partial 5, unresolved 2**; exact-duplicate bases after whitespace normalization = **0**; nearest basis pair by word-trigram Jaccard = **0.24 (CL08, CL12)** — no pair above 0.5, i.e. no template boilerplate; all 15 bases contain a repo locator; clause rules hold per status (5/5 partials carry `restriction:`; 2/2 unresolved carry `open:` + `owner:`; 15/15 carry `grounding:`).
- Basis specificity spot-checks: CL08–CL12 each name a distinct reconciliation row + spotcheck (R6-05-A/P04, R6-03-B/P02, R6-13-A/P03, R6-13-B/P01, R6-09-A/P05); all ten ids verified present in `reports/round-6/parent-reconciliation.json` bytes (python `in` check, 22:01). CL01/CL04–CL05/CL07 name dated check events; CL13 cites `screening.real_language_sweep_performed: false`; D2-CL01's counts (58/46/10/2, findings 16, 15 hold-or-fail) match my own earlier JSON read of `examples/culture-d2/typed-labels.d2.yml`.
- Check-event reproduction: `python3 tools/assemble-culture-d3.py --check` → exit 0 (22:02); `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` → exit 0 (22:02) — the two events the packet's supported bases cite.

### 1.2 Claim-to-record links (no dangling link in the packet)

- Tool leg: `python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .` → `links=50 resolved=50 findings=0`, exit 0. Its `--selftest` → 31/31 checks.
- Independent resolution of **36 distinct `path#token` locators** across ledger, `record_links`, and edge cells: all resolve — JSON selectors as exact keys/values/elements, YAML/MD tokens by word-boundary (script in `.scratch/r15-review/`; 1 apparent miss was my own tokenizer splitting `R6-05-A` at the hyphen; presence confirmed directly).
- Manifest: **26/26 file-backed digest rows re-measured (sha256) and matched**; the one non-file row is the inline `A-GLOSS` payload (same convention the round-12 audit accepted, `reports/round-12/adjacency/contract.md:11`).
- The `path#L<digits>` line-anchor trap (F9-1) is **not triggered by this packet**: census of `packet-v2-05.md` for bare `path#L\d+` specs → **0 occurrences**.

## 2. Findings

### F9-1 (harness, dangling-link class) — `#L<n>` selectors line-anchor before record semantics

`tools/harness/packet_links.py` compiles `LINE_ANCHOR_RE = re.compile(r"^L(\d+)$")` and checks it **before** any record-token semantics; on a `.json` artifact the JSON-record branch is then skipped because the token was consumed as a line anchor. Consequence: the D3 lexeme namespace (`L01`–`L20`, no hyphen) collides with the anchor grammar, and a **nonexistent record resolves "ok" whenever the file has that many lines**.

Reproduction (21:44–21:46 -0300, lane root):

```
python3 tools/harness/packet_links.py --links "examples/culture-d3/packet.json#L99" --repo-root .
→ ok [examples/culture-d3/packet.json#L99]   (exit 0; "L99" occurs 0 times in the file's 990 lines; line 99 is "},")
python3 tools/harness/packet_links.py --packet <fixture with claim links ["examples/culture-d3/packet.json#L99","A-02#L77"]>
→ links=2 resolved=2 findings=0, exit 0       (end-to-end, via the artifact_manifest record index)
```

Impact on the stamped packet: none (0 bare `#L<n>` specs). Impact on the claim: real — "dangling link" detection has a systematic bypass exactly on the record-id shape v2-design §3.1 showcases.
**Owner:** O-impl (shard-2). Fix shape: resolve record-id selectors through the JSON record index first (`A-02#lexicon.L01` form), or reject bare `#L<n>` on JSON artifacts. **Control:** rerun the two probes above; expected after fix: `L-SELECTOR-UNRESOLVED`, exit 1.

### F9-2 (packet, coverage class) — design §3.2.4 record-coverage rule unmet for lexemes/names

v2-design §3.2.4: "every delivered record id (D3 lexicon/names/…; D2 records surfaced by the packet) appears in ≥1 claim link or edge target — no orphan records". Census on the stamped bytes: **18/20 lexemes (L03–L20), all 6 names (N01–N06), M01–M03, O02–O03, U03–U06** carry no claim link and no edge target; the lexemes ride only on the inline glossary payload (gate-counted 20/20) and prose mentions. Direction of travel is right — links grew 40 → 50 between 21:52 and 21:55 and L01, L02, E0/E1, SY02, C04 gained coverage — but the rule is still unmet. Severity: residual (this rule is a v2-design builder assertion, not a round-12 reject reason).
**Owner:** O-packet — either add per-record links (the dotted-key form `A-02#lexicon.L03`, which also sidesteps F9-1) or file a design amendment explaining payload-level coverage as satisfying rule 4. **Control:** rerun the orphan census (script kept in `.scratch/r15-review/`); expected: 0 orphaned delivered records.

### F9-3 (residual, boilerplate class) — near-duplicate bases pass the module

`packet_uncertainty.py` catches exact-normalized duplicates only. Fixture probe (21:41 -0300): three bases identical except one word ("Sanskrit" → "cuneiform") — only the exact pair is flagged; the one-word variant pair passes. On the stamped packet this residual does not fire (nearest pair 0.24, §1.1), so zero-boilerplate stands; the gap is detector coverage.
**Owner:** O-impl/O-design — add a pairwise-similarity assertion or accept a reviewer census as the standing control. **Control:** the trigram census in §1.1, rerun per packet.

### F9-4 (packet, minor design conformance) — no supersedes naming

v2-design §5 says the v2 packet "names what it supersedes (§9 supersedes/derived_from discipline)"; `grep -c "supersedes\|derived_from" reports/round-15/handoff/packet-v2-05.md` → **0** (22:01). `packet_version` is correctly `2.0.0` (`packet-v2-05.md:12`).
**Owner:** O-packet. **Control:** grep count > 0 after fix.

## 3. Observations (no action required by this seat)

- **Fix evidence observed mid-window:** the 21:47 bytes failed the shape gate — `FINDING HO-CANON-CLAIM … line 53: "this packet's markdown surface is judged by it); envelope + canon"`, exit 1; the 21:55 A-17 row reads "shape gate judge of the markdown surface; envelope and canon-wording kernel" (`packet-v2-05.md:53`) and the gate is clean. Before/after control recorded for the parent.
- **Judge divergence:** `packet_uncertainty.py` requires the literal `grounding:`/`restriction:`/`open:`/`owner:` grammar; `run-validation.py`'s cell parser accepts any status token + locator. The stamped packet satisfies both; the parent should know the two judges are not equivalent, so tool-green on one is not tool-green on the other.
- Packet md/yml twin consistency: 15 claim rows in md and yml; 34 edge rows in both (yml rows use two-space-indented `- claim_id:` entries).

## 4. Method summary

Independent censuses (own parsers in `.scratch/r15-review/`): status/clause/duplicate/near-duplicate ledger census; locator resolution; manifest digest re-measure; orphan census; edge crosswalk subset check; harness falsification fixtures (u1–u6, pk1, pk2, link-spec battery). Tool runs: gate, `packet_uncertainty.py`, `packet_links.py`, both `--selftest`s, `run-validation.py --selftest` (37/37 controls, exit 0, 21:49). Every number in this file carries its command inline; every command ran with `TMPDIR=$PWD/.scratch` where scratch was written.

## 5. Re-run battery for the parent (if bytes changed)

```
python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2-05.md   # expect 16/16, 20, findings=0, exit 0
python3 tools/harness/packet_uncertainty.py --packet reports/round-15/handoff/packet-v2-05.yml   # expect claims=15 findings=0
python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .   # expect 0 findings
```
