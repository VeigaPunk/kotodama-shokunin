# ReviewGateToolCode

VERDICT: DEFECT — commit `454a2dc813c8e4caa0b3811266bbf8864e7286f5` reproduces all 30 new-class findings on round 54 and passes its declared acceptance command, but has two false-negative edges and an uncaught input-decoding error; its docstring also overstates the complete-Grounds boundary.

## Findings (severity order)

- `tools/check-gate-quotes.py:272-276` — DEFECT (medium): the lesson read catches `OSError` only; invalid UTF-8 raises `UnicodeDecodeError` outside `check()`, yielding a traceback/exit 1 instead of the documented path-error/exit 2. Exact replacement:
  ```python
          except (OSError, UnicodeError) as exc:
              reason = getattr(exc, "strerror", None) or str(exc)
              results.append((path, None, "unreadable: %s" % reason))
              continue
  ```
- `tools/check-gate-quotes.py:194-210` — DEFECT (medium): Grounds/teaches comparison does not decode HTML entities. Probe: `Grounds: Bread &amp; butter.` with teaches `Bread & butter makes a meal.` returned no finding although the decoded Grounds is a proper prefix. The actual entity-bearing Grounds in rounds 49–55 were also checked; none became a prefix after decoding. Exact replacement text (and add `import html`):
  ```python
      grounds = comparable_teaches(html.unescape(match.group(1)))
      source_teaches = comparable_teaches(html.unescape(source_teaches))
  ```
- `tools/check-gate-quotes.py:176` — DEFECT (low): the landed regex requires the date to be followed immediately by an em dash, so an access note between them prevents this class from recognizing a duplicated locator. The corpus uses this shape at `corpus/lessons/round-50.md:47`: “accessed 2026-10-21 via Wayback 20260103060250 (live page CAPTCHA) —”. Exact replacement:
  ```python
      accessed = re.search(r" — accessed \d{4}-\d{2}-\d{2}[^—]* — ", line)
  ```
- `tools/check-gate-quotes.py:48-52` — DEFECT (low, documentation): the claim that a “complete Grounds sentence” is not reported is too broad. A complete sentence that is only the opening part of a longer teaches cell is a proper prefix and is reported; probe with Grounds `The keeper was owed.` and teaches `The keeper was owed. The registry adds a second sentence.` returned `truncated-grounds`. Replace the final two sentences of this bullet with: “A Grounds value equal to the whole teaches cell, including a single final full stop, is not reported. A complete sentence that is only a prefix of a longer teaches cell is reported.”
- `tools/check-gate-quotes.py:44-47,191` — DEFECT (low, documentation boundary): doubled-locator uses plain substring containment, so `Cartography: "art": "quoted passage"` returns `doubled-locator`; the landed docstring does not state this false-positive boundary, although claim O's review-only criterion asks for it. Add: “The comparison is a case-sensitive plain substring check; a span occurring inside a longer locator word also matches.”

## Round 49–55 run: new-class findings

Every line below was emitted by the landed checker. `CARRIED` means the class/row is present in the checker output; acceptance also confirmed the exact round-54 ID sets.

- `corpus/lessons/round-54.md:23` — S239 doubled-locator — CARRIED — “'Transformations', ¶1: \"Transformations\"”.
- `corpus/lessons/round-54.md:24` — S240 doubled-locator — CARRIED — “'The African Masking Configuration', ¶2: \"The African Masking Configuration\"”.
- `corpus/lessons/round-54.md:25` — S241 truncated-grounds — CARRIED — “the mask is a household portrait kept in a shrine”.
- `corpus/lessons/round-54.md:26` — S242 truncated-grounds — CARRIED — “the mask set is stored procession equipment and a drawn pedigree at once”.
- `corpus/lessons/round-54.md:27` — S243 doubled-locator — CARRIED — “'Nanfeng Nuo Dance Masks': \"Nanfeng Nuo Dance Masks\"”.
- `corpus/lessons/round-54.md:28` — S244 truncated-grounds — CARRIED — “a commedia Mask is a place-plus-class-plus-speech package”.
- `corpus/lessons/round-54.md:30` — S246 doubled-locator — CARRIED — “'History of use', first paragraph: \"History of use\"”.
- `corpus/lessons/round-54.md:32` — S248 truncated-grounds — CARRIED — “the mask set is property that travels between institutions”.
- `corpus/lessons/round-54.md:33` — S249 doubled-locator — CARRIED — “'Belief System', symbolic components: \"Belief System\"”.
- `corpus/lessons/round-54.md:34` — S250 truncated-grounds — CARRIED — “mask removal is a rare, scripted revelation rather than stage business”.
- `corpus/lessons/round-54.md:35` — S251 truncated-grounds — CARRIED — “cham is performed by monastics in a monastery courtyard for protection of the community”.
- `corpus/lessons/round-54.md:37` — S253 truncated-grounds — CARRIED — “the surviving commedia mask is a reproducible type-face”.
- `corpus/lessons/round-54.md:39` — S255 truncated-grounds — CARRIED — “office, not wealth or blood alone, earns a mask”.
- `corpus/lessons/round-54.md:43` — S259 doubled-locator — CARRIED — “'I did not know of firam': \"I did not know of firam\"”.
- `corpus/lessons/round-54.md:43` — S259 truncated-grounds — CARRIED — “the mask is a spirit men know they make; sight is a purchased grade”.
- `corpus/lessons/round-54.md:46` — S262 doubled-locator — CARRIED — “'My focus on the carved headpiece': \"My focus on the carved headpiece\"”.
- `corpus/lessons/round-54.md:47` — S263 truncated-grounds — CARRIED — “Gelede as a stage play compared by its author to the Roman theatre and to Noh”.
- `corpus/lessons/round-54.md:48` — S264 truncated-grounds — CARRIED — “UNESCO's record of the inscribed element — Yoruba-Nago communities across Benin, Nigeria and Togo”.
- `corpus/lessons/round-54.md:49` — S265 doubled-locator — CARRIED — “'Status of Masks', paragraph 1: \"Status of Masks\"”.
- `corpus/lessons/round-54.md:49` — S265 truncated-grounds — CARRIED — “a mask policy written by the mask-owning authority itself — sacred from the moment of making”.
- `corpus/lessons/round-54.md:50` — S266 doubled-locator — CARRIED — “'Intellectual Property Rights' ¶2: \"Intellectual Property Rights\"”.
- `corpus/lessons/round-54.md:51` — S267 doubled-locator — CARRIED — “'Sources of power within the Mande buzz aesthetic': \"Sources of power within the Mande buzz aesthetic\"”.
- `corpus/lessons/round-54.md:52` — S268 doubled-locator — CARRIED — “'The Boki voice-disguiser – an object of design?': \"The Boki voice-disguiser – an object of design?\"”.
- `corpus/lessons/round-54.md:59` — S275 doubled-locator — CARRIED — “'Malagan traditions': \"Malagan traditions\"”.
- `corpus/lessons/round-54.md:59` — S275 truncated-grounds — CARRIED — “malagan is a family of ritual objects across New Ireland and the Tabar Islands”.
- `corpus/lessons/round-54.md:60` — S276 truncated-grounds — CARRIED — “the effigy is animated during production, installed, treated as alive, then ritually killed”.
- `corpus/lessons/round-54.md:61` — S277 doubled-locator — CARRIED — “'Happy is he who dreams of forest spirits': \"Happy is he who dreams of forest spirits\"”.
- `corpus/lessons/round-54.md:61` — S277 truncated-grounds — CARRIED — “masks are men's business by a myth of stolen technique”.
- `corpus/lessons/round-54.md:62` — S278 truncated-grounds — CARRIED — “kavat are made for male night dances in which masked spirits come out of the bush”.
- `corpus/lessons/round-54.md:63` — S279 truncated-grounds — CARRIED — “Greek does not lexically separate the face, the mask worn over it, the ancestor image and the person”.

## Checks and residual risk

- `python3 -B tools/check-gate-quotes.py corpus/lessons/round-49.md … round-55.md` — exit 1, summary `GATE_QUOTES: 51 findings`; only round 54 emitted new classes (30). Rounds 51–53 emitted only existing `words=<n>` findings; rounds 49, 50, and 55 emitted none.
- `python3 -B reports/round-55/accept-o.py` — all eight legs PASS: doubled 13, truncated 17, no-false, exits, escapes, keep53, format, selftest.
- `python3 -B tools/check-gate-quotes.py --selftest` — `SELFTEST: 24/24 pass`.
- No-argument, missing-file, and no-Gate invocations returned exit 2 with `GATE_QUOTES_ERROR:` on stderr; acceptance's format leg passed for the round-54, fixture, and round-53 runs.
- Registry path resolution is correct for these lesson paths: `dirname(corpus/lessons/round-N.md)/../SOURCES.md` resolves to `corpus/SOURCES.md`. Missing registry rows return no truncated finding; a Grounds longer than teaches is not reported. Wrapped quotes, guillemets, inter-span ellipsis, and `- * ` rows passed the 24-case selftest/fixture checks.
- Unrun: a malformed-UTF-8 file was not created for an end-to-end decoder test; the uncaught `UnicodeDecodeError` follows from the read/exception code path. LSP is unavailable (`xd://lsp` was not mounted), so no LSP checks were possible. During review the tool worktree acquired uncommitted edits; checks above were run against the landed version before that change, and no repository files were edited by this reviewer.
- No tools installed.
