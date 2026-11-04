# ReviewerEntry — round 85, wave 1

Axes: **depth, operability**, bounded by calibration. Non-author, lane-authored review; not external promotion, admission, or canon acceptance. No production edit.

**Final disposition:** no open actionable finding remains in this scope. The MEDIUM finding below is retained as historical red-before and was repaired by L1. Directly inspected repaired `reports/round-85/metallurgy-craft.json:5,12–15,23–30`: all twelve records now carry distinct sense ids, translated-label form kind, explicit composition status, independent form/sense/object/process clocks, source/design status and uncertainty. Native form clocks remain null; E1/E2 intervals are explicitly fictional use horizons, not historical attestations or invented native dates. Preserved as `craft-repaired-reviewed.json`, sha256 `d2ba76b556d9409a57126ff549bdf13e1b0ba8822b1f2eeb0ae2598490cc2a0b`. Filed `craft-ledger-repair-receipt.json` records L1's red incomplete=12/exit 1 → green incomplete=0/exit 0, with command and matching repaired input hash. Reviewer read these bytes and receipt; did not rerun the repair check. This supersedes the open-repair wording below, without deleting its evidence.

## Reviewed objects

The originally assigned ScribeEntryMetal/ScribeRows artifacts did not arrive. Planner KotodamaR85 explicitly supplied actual replacement draft readiness at `stage/L1/metallurgy-metal-register.md` and subsequently `stage/L1/rows.md`, both below `.ufo/waves/round-85/w1/`. This review inspected their actual bytes, not readiness messages as evidence of content.

Preserved under this seat stage:

- `candidate-reviewed.md`: sha256 `fb9dcae43951d5be478ed69cb6ada0998dd9433f8dcb0aee0f50b96071a151d1`.
- `rows-reviewed.md`: sha256 `cb1fa72a80b0b8ced8d22da9553279c997be82193e2e45fe688817efcbab87e2`.
- `craft-reviewed.json`: sha256 `fa8bd650927e1b8e6a444f7d9d835b18bbf323f0be5e092a01bab6eecc568f56`, copied from `reports/round-85/metallurgy-craft.json` when inspected.

References below use snapshot line numbers. They apply to those bytes; integration or later repairs require their own final-byte checks.

## Findings by severity

### MEDIUM, REPAIRED — worked ledger initially omitted the independent clock/sense records

**Evidence:** `candidate-reviewed.md:32` says every ledger row has a sense, an era interval, a language channel and evidence status; `:84–94` specifies stable `sense_id`, composition status and separate word/referent fields. `:104–109` requires four independently writable form/sense/object/process-institution clocks. `:121` designates `reports/round-85/metallurgy-craft.json` as the machine-readable companion, and `:129–133` says the twelve records constitute the worked output.

But `craft-reviewed.json:11–14,22–29` contains gloss/category fragments, not that interface: no record has a `sense_id`, no record has the four independent intervals/statuses, and the only `clock` value (`:11`) is the statement “word arrival and object arrival recorded separately,” not two recorded values. Several records, including ore stone/washed charge/slag, also omit composition status rather than explicitly storing unknown/not-applicable. Global NON-CANON and translated-label declarations appropriately constrain all records but do not supply the missing per-sense clock data.

**Observable effect:** a user cannot follow the worked example to distinguish an imported object's arrival from first local production or a retained word from its changed sense. The implementation of the example drops precisely the distinctions the entry says prevent word/material-clock conflation; its broad CRAFT-85 PASS receipt checks only two era containers, count/categories and selected semantic flags, not the promised ledger fields.

**Repair:** populate stable sense ids and explicitly independent form/sense/object/process-institution fields on the actual companion records, with declared fictional values or explicit unknowns and evidence/design status. Preserve genuinely unknown production dates instead of manufacturing historical evidence. Alternatively make the entry accurately describe a partial semantic sketch rather than a completed instance of its ledger. This is an operability defect, not a falsified EB11 quotation. Routed to KotodamaR85; reviewer did not edit the draft or companion.

No HIGH finding. No additional MEDIUM source-attribution finding found in the inspected entry/rows.

## Independent source findings

All four EB11 articles and rejected Bronze_Age were independently fetched 2026-11-04, ordinary HTTP 200 on first live attempt. Same-page archive captures were independently fetched after CDX queries with a successful positive control. Exact URLs, raw bodies, normalized text, access receipts and source hashes are preserved under `evidence/`. See `source-review.md` for article-specific scope traps, including archive-original encoding and compressed-body handling.

- **20/20 entry quotes locate:** `quote-locations.json` records one folded occurrence in the live page and one in its named same-page archive for every anchor (`candidate-reviewed.md:55–74`). Distribution is 6 Metallurgy, 4 Iron, 5 Bronze, 5 Alloys. Manual surrounding-text inspection confirms all twenty are body statements, not captions, navigation, attributes or another article. In Alloys, the “not the only method possible” statement is the prose immediately after the plate; superficial uniformity is prose before it. The plate's micrograph annotations were not used as broad body claims.
- **Unsupported 1911 claims:** none found in the inspected source-attributed factual clauses. The text keeps the distinction between a dated witness and a proposed design consequence. For example, the silvery-white iron anchor motivates a possible vocabulary distinction without claiming a universal colour taxonomy.
- **Anachronisms:** none asserted as historical fact. E1/E2, casting households, assay office, grades and twelve display glosses are expressly fictional. Named 1911 engineering alloy vocabulary is not retrojected as an ancient recipe. Four titles in one encyclopedia are expressly not represented as four independent modern corroborations (`:76,173`).
- **Iron etymology:** explicitly refused (`:26,145,169`), consistent with the chemistry-only scope of the actual Iron body. No etymology is inferred from Fe/ferrum or from material properties.
- **Word/material clocks:** prose distinguishes all four and rejects universal metal-age staging (`:102–117`). The operational gap in the companion, above, remains; the prose does not itself assert that a word dates a furnace.
- **Smith social status:** hereditary, secret or ritually marginal status is presented as unsupported unless fictional or separately sourced (`:144`). No universal smith caste/taboo is taught.
- **One-id lines:** the initial live view's multi-id metadata header had been split before the pinned review snapshot. Assigned frozen checker ran exactly once in own scratch against that snapshot: exit 0, `CITED-LINES: 0 finding(s) in 1 file(s)`. See `lint-receipt.txt`; checker sha256 `a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a`. No claim of a lint result for earlier or later bytes.

## Source rows and existing scopes

`rows-reviewed.md:1–5`: each actual row has eleven populated cells; `row-quote-locations.json` independently locates all five anchor quotes in both live and archived bodies. S919–S922 are B, mined, opened 2026-11-04, used by the entry, and scoped to 1911 technical vocabulary rather than current archaeology/engineering. Iron's teaches cell explicitly disclaims etymology. The Alloys qualification about fusion being general, not exclusive, survives in the entry.

S923 is C/rejected for its offered racial-stage/external-diffusion model, not missing prose. The substantial Bronze_Age body actually contains the Phoenician/Greek teaching passage quoted by the row, “most races passed”, and the hand-size/racial inference discussed in `source-review.md`. Its rejection is calibrated to refusing that model as current bounded archaeological authority; a newer locally bounded evidence chain is the stated flip. It does not assert the page is universally useless or inaccessible.

No pre-existing source row or used-by mutation is proposed in the supplied five-row candidate. Therefore no old → new cell is needed for this supplied delta; any existing-row changes L1 later introduces still require literal old → new cells. Existing craft-artisan and trade-economy owners are acknowledged and not silently superseded. The base count/basename observation was independently reproduced, while the absence claim remains explicitly filename-bounded (`candidate-reviewed.md:11`). No assertion that an index checker never existed is made; the frozen O contract acknowledges round-28 sweep.

## Residual risk and verification gaps

- Source findings concern dated EB11 wording, not modern scientific/historical validation or cultural authenticity. No canon or real-language clearance was assessed or implied.
- The frozen D measure was read from FREEZE, not run. Its structural predicates cannot decide source faithfulness. L1 should run the frozen D counter on the exact final integrated revision and retain its source-body review alongside the receipt.
- Registry uniqueness/integration and later old-row changes were not certified from the staged five-row delta. L1 should compare the final registry delta with the base and retain any literal old → new cells.
- The assigned cited-line lint was the sole checker executed; no broad tests/build/formatters, live-lane fixture-writing gate, or alternate runtime was invoked. No tooling installed or upgraded.
- `xd://lsp` discovery returned “No such tool”; semantic status/references/definition/diagnostics were unavailable. Direct Markdown/source reading is a literal fallback, not semantic caller proof. All substantive material is prose/JSON here.
- Final entry, row and companion bytes may change after these snapshots. This report recommends repairing the worked-ledger gap; it is not an admission decision.

## Self-evaluation

Accuracy 4/5: body locations and hashes retained; no modern external adjudication attempted. Completeness 4/5: entry, five rows and companion reviewed; final integration deliberately remains L1's job. Clarity 4/5: snapshot-relative evidence separates actual defects from source traps. Actionability 4/5: missing record fields and honest-unknown repair identified concretely. Conciseness 4/5: the longer source inventory lives separately in source-review.md. Overall 4.0/5; highest-impact improvement is the explicitly identified worked-ledger repair, not additional unsourced historical detail.
