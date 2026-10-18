# R22-D04–D06 — family-clean projection implementation

Status: **IMPLEMENTED — SOURCE READY FOR FINAL RE-PIN** (`design.md`: family-clean removal, not borrowed-reference relabeling). Final source `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` and expected holds `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` have been stable since the 2026-10-18T14:50:49Z 163/163 selftest and 14:51:18Z consumer/pin check. No further code, derived-output, or expected-hold change will be made by this seat; remaining changes here are evidence only. This seat owns the projector-adjacent implementation, embedded controls, and live D4 projection/typed packet/expected holds; the re-pin seat owns profile/frozen successor rows, and the handoff owner owns the renderer/baseline. The concurrent alias-only changes in `tools/d2-typed-labels.py` are preserved. No filed rounds 8–21, profile/frozen rows, or handoff runner are changed by this seat.

## Baseline and source

At 2026-10-18T14:40:00Z, command `runpy.run_path('tools/d2-typed-labels.py'); run_pipeline(ROOT / 'examples/culture-{d2,d4}/packet.{d2,d4}.yml'); serialize(result['projection'])` captured the pre-edit bytes under `.scratch/r22-d04/`.

- D2 projection: 84,614 bytes; SHA-256 `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`.
- D4 projection: 92,108 bytes; SHA-256 `cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f`.
- `run_pipeline` calls `build_payload()` unconditionally. That function reads the embedded D2 rank fixture, independent of packet family; absence of a foreign examples tree therefore does not prove absence of D2 material.
- Family-local alias resolution already exists. The label constructors still name D2 component owners and `d2-roman`, and the projection name/canon text is D2-specific.

At 2026-10-18T14:40:08Z, with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

- `python3 tools/d2-typed-labels.py --selftest` → exit 0, 50/50 controls.
- `python3 tools/assemble-d4-typed.py --selftest` → exit 0, 12/12 controls.

The unchanged D2 output and the pre-fix D4 output are retained as byte-comparison controls, not overwritten filed evidence.

## Implementation ready for re-pin

**Source and live D4 derived outputs are ready at 2026-10-18T14:49:12Z.** No further source change is planned; the re-pin owner may bind the hashes below. The canonical D4 gate currently refuses the old profile pin as intended; no post-re-pin 19/19 or v3 pass is claimed yet.

- `run_pipeline` selects the family before parsing labels or constructing rank data. D2 alone uses `build_payload`, its fixture constants, inversion, rank tokens and conflict triage. D4 uses its packet-native four RK records, preserving all declared authority/jurisdiction/era/rite/property/effect/rank fields. Its `#g` rows name the same RK source IDs. D2-only residual/act/quarantine/assay arrays are empty, not imported as borrowed data.
- Label constructors retain their D2 defaults. The D4 path supplies `09-costumes`, `04-lexicon`, `05-naming`, fully qualified D4 component citations, and the exact `orthography.scheme` declaration. Texts, kinds, record IDs, owed slots and all six linguistic borrow ledgers are unchanged. The costume-slot requirement still applies after changing the owner name.
- Structured ownership checks refuse a foreign source/component, owner or scheme, including explicit hand-authored typed labels. Packet-native rank rows must be shaped and unique; malformed declarations fail with `P-FAMILY-RANK` or `P-FAMILY-SOURCE` before emitting. Unsupported local properties stay held and unprojected; absent rank rules are an explicit skip. Shared tool/schema references, shared `D2L-*` diagnostic names and genuine D4 orthographic `WR-*` IDs are not globally substring-banned.
- Local conflicts use local declarations only, without D2 wearer-license inversion or D2 rank-token defaults. A possible declared scope overlap is held without inventing a prose jurisdiction priority.
- `examples/culture-d4/expected-holds.json` removes exactly three inherited D2 rank holds and one D2 rank note. The twelve garment/owed-slot form holds remain; no D2 debt or garment-form obligation was resolved. This delta was specified in `design.md` before the output was built, not copied from a newly green result.

### Regeneration and current bindings

With `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, on **2026-10-18**:

- **14:48:29Z** — `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit examples/culture-d4/typed-labels.d4.yml` → exit 1 (expected open holds); writes the deterministic projection.
- **14:48:30Z** — `python3 tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml` → exit 0; 89,218 bytes and twelve routing rows. The adapter source is unchanged.
- **14:46:34Z**, command `run_pipeline + serialize` → D4: 74 labels (56 native / 12 translated / 6 borrowed), four component/normalized/gate-projected rank rows, zero unresolved rank items/quarantine/conflicts, twelve form findings. D2 remains 84,614 bytes at its exact baseline digest.

SHA-256 at regeneration (source/adapter) and after the live expected-hold edit:

- **Final projector after the comment-consistency sweep:** `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3`. The previously measured `c3eb2261e5398c76b2acee91be9dbf7cb3e416b228654935001125d11161dd07` predates two documentation-only corrections to the old verbatim-lift claim. Projection and typed-packet bytes did not move. The expected-hold source pin has been updated; the re-pin owner must take this final combined source hash rather than c3eb2261….
- D4 projection: `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` (76,262 bytes).
- D4 typed packet: `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e`.
- **Final D4 expected holds:** `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` — verified with `sha256sum examples/culture-d4/expected-holds.json` at 2026-10-18T14:50:47Z. The source-only pin update supersedes the intermediate `88c21ff3cd31776e3838f3e3140f42d7389ae3558d55e9761dbe549b8175475c` measured at 14:49:43Z; expected rows and all generated projection/typed-packet bytes are unchanged.
- Unchanged adapter: `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0`.
- Unchanged D2 projection: `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`.

### Controls and initial isolated regressions

The clone `.scratch/r22-d04/verify` was created before the repair and receives only named current implementation/derived files. No historical round validator runs in the live repository. Raw dated command records are under `.scratch/r22-d04/`.

At **14:49:09–14:49:12Z on 2026-10-18**, from that clone with `TMPDIR` set to the clone's `.scratch`:

- `python3 tools/d2-typed-labels.py --selftest` → exit 0, **163/163**. This is 50 original controls + 82 concurrent alias controls + **31 family-boundary controls**.
- `python3 tools/d2-typed-labels.py --check` and the D4 `--packet ... --check ...` invocation → exit 0, byte-identical.
- `python3 tools/assemble-d4-typed.py --selftest` → exit 0, **12/12**; `--check` → exit 0.
- `python3 tools/assemble-d2-typed.py --selftest` → exit 0, **11/11**.
- `python3 tools/assemble-culture-d4.py --selftest` → exit 0, **81/81**.
- `python3 tools/gates/typed-pipeline-gate.py --selftest` → exit 0, **12/12**; `--selftest-generalized` → exit 0, **14/14**.
- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → expected **exit 2 / L1-profile** because the clone intentionally still has the old projection and expected-hold pins. This proves stale pins refuse; re-pin is not bypassed.

The 31 new embedded controls include a D4 packet-only mirror plus raising sentinels for all D2 fixture build/projection/rank/conflict hooks; exact D2 baseline bytes plus a D2-only rank mutation; local RK-01 authority/property/rank mutations; one-row add/remove/absent coverage checks; unsupported-property hold and local-conflict checks; duplicate/malformed/cited-foreign ranks; foreign owner/scheme/absolute and short component citations; same-ID explicit foreign labels refusing both absent and existing output; unchanged form/loan data; and the D4 costume-slot requirement.

The actual captured pre-fix D4 document was separately passed to `validate_family_projection` at 14:49:12Z and refused with `P-FAMILY-SOURCE ... GAR-01.owner: foreign owner '11-costumes'`. Thus the semantic boundary rejects the formerly deterministic artifact. A SHA-256 sweep against the pre-edit manifest found **zero changed files in `examples/culture-d2/`** at the same time.

An initial boundary probe caught that the strict loader preserves JSON/YAML `null` as authored text; required rank strings now reject null-ish spellings. The corrected 31/31 boundary matrix and combined 163/163 selftest pass. This correction affects only the non-D2 rank path.

### Final source seal and downstream dependencies

- **2026-10-18T14:50:49Z**, isolated `python3 tools/d2-typed-labels.py --selftest` → exit 0, **163/163**, on final source `2819f687…` (after the documentation-only sweep).
- **2026-10-18T14:51:18Z**, command `structured source/consumer/hold-pin checks + sha256 baseline D2 sweep + protected git status` (`.scratch/r22-d04/final-contract.json`) → pass. The D4 typed packet carries exactly the projector's finding set, counts equal the independently declared 12/0/0 expectation, both internal expected-file pins equal the live bytes, and all twelve routing rows name `09-costumes`. All **35** pre-captured D2 files match their original SHA-256; `git status --porcelain -- reports/round-{8..21}` is empty.
- `git diff --check -- tools/d2-typed-labels.py examples/culture-d4/{typed-labels.d4.yml,packet.d4.typed.yml,expected-holds.json} reports/round-22/bleed/impl.md` → exit 0 at 14:49:43Z.

At the **14:53:54Z** dependency observation, the shared D4 profile still pins the intermediate expected-file hash `88c21ff3…`, not final `3826ba68…`. The source and expected file themselves are mutually consistent and sealed; updating that profile can proceed independently of the handoff prose, and should precede freezing the next v3 manifest. The implementation owner will not change these source/output pins again.

The re-pin seat separately filed stale new-v3 claim wording in `reports/round-22/bleed/repin.md:26-37` and `evidence/handoff-content-review.json`: D4-CL05/06/07/09 and OQ-V3-05 still describe the removed rank passengers. A renderer/claim-map supersession is required; neither a profile re-pin nor a 105/105 link-resolution count repairs those statements. That work is outside this seat's assigned writes. No final integrated 19/19 or 105/105 pass is asserted until the assigned owners land their new rows and claim wording.
