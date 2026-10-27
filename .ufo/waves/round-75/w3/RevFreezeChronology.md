# Round 75 W3 — freeze chronology

**Verdict: PARTIAL.** The freeze-before-live-landings chronology and immutable counter inputs hold. The literal assertion “no landed byte existed at any point” is too broad: exact bytes later landed in live documents were already committed in the frozen wave staging area. No evidence shows those bytes were already applied to live documents before the landing commits.

## Evidence table

| Question / input | Evidence | Result |
|---|---|---|
| Commit order | First-parent chain: `f556d10` → `5d01674` → `012e8d3` → `4f5e3b2` (three commits from base through C). `5d01674` committer date 2026-10-27 17:43:38; Ca committer 17:44:16; C committer 17:44:45. | Freeze precedes both landings. Freeze author date is 2026-10-26 01:12:01, but its committer date and parent chain place the committed freeze on 2026-10-27 before Ca. Treat author-date mismatch as chronology caveat, not evidence of early content. |
| `reports/round-75/claims.json` | Blob `e54df48240fea66dee854da0907d2ec58246127d` at freeze, Ca, and C; working file hashes to the same blob. `git log -- reports/round-75/claims.json` shows only the freeze commit. | Identical at both landings; no post-freeze predicate change. |
| `reports/round-75/ledger.json` | Blob `bce768fa8432d5cf597a936ee9fa894a377c3d29` at freeze, Ca, C; matches the working file. | Identical. |
| `reports/round-75/accept-c.py` / `accept-ca.py` | Blobs `1773b82a3a353e9e4dcf66f7cdefc9aace8fa246` / `05a4196faac78f54bc01ccfb1c803a2f06438fbf` at freeze, Ca, C; both match working files. Claims define 13 C legs and 12 Ca legs. | Identical frozen counters. |
| By-document map | `.ufo/waves/round-75/assimilation/id-renumber-map.json` blob `fe4d30aa97081d6b451738911de13d3fbd7e8dfc` at freeze, Ca, C. Its SHA-256 is `778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155`, matching `claims.json` and the working file. | Identical and pinned correctly. |
| R1EXEMPT fixtures | Three `reports/round-75/fixtures/r1exempt-{green,mixed,red}.json` blobs are unchanged in the freeze/Ca/C trees (respectively `7551803f…`, `7e3ef492…`, `2efa71e…`). | Identical control inputs. |
| Predicate corrections | Five `build-claims-final*.py` scripts are included in the freeze commit. Their code records W2-F1 (plus A2-note), W2-F2, W2-F3, W2-F4, W2-F5; each mutation asserts its expected prior text/state, and each correction is recorded in the freeze `pre_data_corrections` (six records total). The claims file was first committed at freeze and never changed afterward. | All recorded corrections predate the first committed claims blob; no predicate edits after landed-data scoring. Exact draft-to-freeze replay was not attempted because the pre-script draft is not established by the snapshot evidence. |
| Base tree vs wave files/live surfaces | Freeze is a direct child of base. Its diff adds `.ufo/waves/round-75/**` and `reports/round-75/**`; it changes no live corpus/README/SOURCES/SHONEN/SKILL/SCORECARD surfaces. Ca and C then modify their declared live surfaces. | No live landing at base or freeze; live changes occur in the later landing commits. |
| Literal “no landed byte existed” | At freeze, staged files already have exact blobs later committed live: narrative base `29baa515…`, amendment `8642a43c…`, amendment `e52c0991…`, and evidence S885 `8666bec4…` match their C-landing paths. The staged round-75 lesson (`c4fec637…`) differs from its C-tree version (`9903ee1f…`). | Exact later-landed bytes existed in staged wave files before the live landing; “no landed byte existed at any point” is false if read literally. If “landed” means applied to live corpus paths, that narrower claim holds. |

## Defect and residual risk

- **Defect:** the A2-note wording “no landed byte existed at any point” overstates the evidence/meaning. At the freeze, the wave staging tree contains byte-identical copies of multiple later-landed artifacts. Prefer the precise claim: “no landing had been applied to live corpus paths at the freeze; round-75 landings first appear in the later Ca/C commits.”
- The freeze commit's author timestamp is older than its committer timestamp by over a day; the committer timestamp and parent order are consistent with the observed landing chronology. This review does not infer that the author date establishes when the frozen tree's contents were created.
- No counters were run for this review; byte-identity and commit-tree evidence were checked directly. No tools installed.
