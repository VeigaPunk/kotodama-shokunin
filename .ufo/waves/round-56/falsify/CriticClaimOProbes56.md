# Claim O landed probes

**Advisory verdict: the landed decoder carries the requested boundaries and survives all 14 probes under its documented row-only, semicolon-required policy.** S978 exposes an intentional policy limitation, not a failed acceptance leg. Acceptance alone does not establish these properties.

Axes: operability (diagnostic completeness and continued multi-file evaluation); calibration (one-pass and semicolon boundaries).

Target: commit `7576fd43bbbe34a00341e4b1956c907f2760e7d8`, extracted read-only; tool SHA-256 `3a13ab9cb93e211bd8c79bd2dfe78e6fb6cd76df0a87efebb315e68688bf6b67`. Scratch and reproducible runner: `/fast/scratch/hyaku/kotodama-r56-falsify/CriticClaimOProbes56/run-probes.py`; adjacent JSON files capture stdout, stderr and exits. Probe locators below are `probe/lessons/falsify.md` in that scratch directory. No tools installed.

## Checked items

1. `reports/round-56/fixtures/lessons/entities.md:8-16` — CARRIED, S-id generalisation. Renumbered lesson and registry produce all ten expected findings, exit 1. Evidence: “GATE_QUOTES: 10 findings” (`probe-1-renumbered.json`, stdout). Replacement: none.
2. S971 — CARRIED, named curly quotation marks decode before counting. Evidence: “S971 words=26” (`probes-2-through-12.json`, stdout; fixture line 5); also exactly one html-entity finding. Replacement: none.
3. S972 — CARRIED, named nonbreaking space becomes a word separator. Evidence: “S972 words=26” (same output; fixture line 6); also html-entity. Replacement: none.
4. S973 — CARRIED, named em dash decodes in Grounds. Evidence: “S973 truncated-grounds” (same output; fixture line 7); also html-entity. Replacement: none.
5. S974 — CARRIED, legal uppercase quotation-mark name recognized. Evidence: “S974 html-entity” (same output; fixture line 8). Replacement: none.
6. S975 — CARRIED, semicolon-free legacy names inside quote material remain untouched and produce no findings. Evidence: “S975 changed False has_reference False findings []” (direct decoder/scan probe, session output; fixture line 9). Replacement: none.
7. S976 — CARRIED, double-encoded marks decode once only. Evidence: “S976 changed True has_reference True findings [(1, 'S976', 0, 'html-entity')]” (direct probe; fixture line 10). No over-cap finding. Replacement: none.
8. S977 — CARRIED, continuation-line reference attributed to the first physical row line. Evidence: “falsify.md:11 S977 html-entity” (`probes-2-through-12.json`, stdout; reference physically at line 12). Replacement: none.
9. S979 — CARRIED, registry pipe escape does not break cell parsing. Evidence: “S979 truncated-grounds” (same output; fixture line 14; registry line 13). Replacement: none.
10. S978 — CARRIED under the declared row-only policy, with a diagnostic limitation: decoded Grounds are compared to an encoded teaches cell, losing the truncated diagnosis. Evidence: “S978 html-entity” (same output; fixture line 13; registry line 12); no truncated-grounds. The row still fails. Smallest optional correction, only if L1 chooses symmetric comparison: replace tool line 245 with `source_teaches = comparable_teaches(decode_html_references(source_teaches)[0])`. Do not decode registry lines before splitting cells. This broadens the declared policy; it is not required by the current acceptance.
11. S980 — CARRIED under the documented semicolon boundary: numeric forms without a semicolon are not decoded or flagged. Evidence: “S980 changed False has_reference False findings []” (direct probe; fixture line 15). This is narrower than browser HTML parsing. Calibration replacement for the declaration's ambiguous parenthesis: “a semicolon-terminated decimal numeric reference, hexadecimal numeric reference, or named reference whose exact name is an HTML5 entity name”. No tool change needed.
12. S981 — CARRIED, invalid numeric code points are recognized and replaced with U+FFFD. Evidence: “PROBE12_DECODE ('� �', True)” (runner output; fixture line 16); html-entity reported once. Optional exact docstring addition after line 68: “Invalid numeric code points follow Python's HTML5 replacement rules, including U+FFFD for null and surrogate code points.”
13. `tools/check-gate-quotes.py:315-317` — CARRIED, an invalid first file does not suppress later findings. Evidence: “GATE_QUOTES: 16 findings” (`probe-13-multipath.json`, stdout); exit 2 and a path-naming GATE_QUOTES_ERROR on stderr, no traceback. Stderr/stdout have no guaranteed cross-stream ordering. Replacement: none.
14. `tools/check-gate-quotes.py:439-465` — CARRIED, selftest kills disabled html-entity detection. Pristine CLI: “SELFTEST: 38/38 pass”, exit 0 (`probe-14-pristine-selftest.json`). In-memory mutation forcing the decoder's reference flag false, retaining decoding: “SELFTEST: 30/38 pass”, return 1 (`probe-14-mutant.json`). Eight new-class cases fail. Replacement: none.

## What acceptance cannot see

These are acceptance-coverage gaps, not evidence that the landed implementation takes a shortcut. Locators refer to `reports/round-56/accept-o.py`.

- **Identity shortcut:** moved-copy lines 103-110 preserve S-ids; line 169 only shifts line numbers. Renumbering is not tested. Smallest correction: rewrite fixture and registry ids together in the moved copy and rewrite expected triples correspondingly.
- **Decoder policy and vocabulary:** fixture lines 78-81 do not distinguish one-pass versus repeated decoding, semicolon-free decoding inside quotation material, named curly delimiters, nonbreaking-space word splitting, uppercase names, invalid numeric values, or numeric forms without semicolons. The landed tool passes those probes independently. Smallest correction: add the corresponding rows and exact expectations from probes 2-7 and 11-12; do not silently change pinned instruments.
- **Continuation and registry grammar:** no fixture tests reference attribution on continuation lines, pipe escapes in non-teaches registry cells, or encoded teaches-cell asymmetry (probes 8-10). Smallest correction: add those fixtures; first decide explicitly whether teaches decoding is in scope.
- **Batch failure isolation:** BADUTF8 lines 159 and 186-188 exercise only one path. A later file can disappear without that leg noticing. Smallest correction: add an invalid-first plus valid-second invocation and require the second file's exact findings with exit 2.
- **Selftest relevance:** line 190 checks only exit 0, not case inventory or mutation sensitivity. The landed selftest independently kills the requested mutation, but an old always-green selftest would satisfy that leg. Smallest correction: retain the mutation probe as a separate falsifier rather than treating a green exit as coverage proof.
- **NOFALSE and KEEP do not pin decoder semantics:** lines 179 and 185 test only fixed existing rows and base outputs. They cannot substitute for the missing boundary fixtures above. No change to their existing expectations is needed.

No blanket acceptance rerun or new mutants through all eight legs were run by this seat; historical mutant-pass claims in the build critic were not adopted as fresh results. No C/source-page checks were assigned here. All 14 assigned probes were exercised; no assigned check remains unrun. No lane implementation or instrument was edited.
