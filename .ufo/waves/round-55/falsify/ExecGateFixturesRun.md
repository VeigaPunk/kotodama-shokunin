Verdict: 14/17 expected rows match; runner exits 1. S901 and S915 expose checker gaps; S904's expectation lacks the registry input the checker requires. No lane implementation files changed.

## Per-row results

- S901 — DEFECT (tool): `MISMATCH S901 expected=doubled-locator got=none`; `fixtures-r55.md:5` says “The locator is repeated before the quoted excerpt.” The detector returns false without an `accessed` marker (`check-gate-quotes.py:176-179`), although this row has an unambiguous repeated locator. Exact code replacement: replace `if accessed is None: return False` with:
  ```python
  if accessed is None:
      accessed = re.search(r"^-\s+S\d+\b\s+—\s+", line)
      if accessed is None:
          return False
  ```
  Then the existing span search can use the row prefix as its start when no access marker exists.
- S902 — CARRIED: `MATCH S902 expected=no finding got=none`; `fixtures-r55.md:6` says “A single-quoted section name is only a locator here.”
- S903 — CARRIED: `MATCH S903 expected=no finding got=none`; `fixtures-r55.md:7` says “The quotation legitimately repeats a heading word.”
- S904 — UNSUPPORTED (fixture expectation): `MISMATCH S904 expected=truncated-grounds got=none`; the checker says “Missing registry files or rows are skipped” (`check-gate-quotes.py:48-51`). The copied lane `corpus/SOURCES.md` has no S904 row, so there is no `teaches` value to compare. Preserve this red case by adding this exact row to a fixture-local `SOURCES.md` beside the fixture's parent: `| S904 | Fixture source | fixture | A | fixture | p. 18 | The source says its guardians protect travellers. | mined | 2026-10-22 | 90d | Fixture |`.
- S905 — CARRIED: `MATCH S905 expected=no finding got=none`; `fixtures-r55.md:9` says “The locator abbreviates page as p.”
- S906 — CARRIED: `MATCH S906 expected=no finding got=none`; `fixtures-r55.md:10` says “The source introduces examples with e.g.”
- S907 — CARRIED: `MATCH S907 expected=no finding got=none`; `fixtures-r55.md:11` says “The grounds statement ends in a full stop..”
- S908 — CARRIED: `MATCH S908 expected=words=26 got=words=26`; `fixtures-r55.md:12-13` says “The quoted passage crosses a hard line wrap.”
- S909 — CARRIED: `MATCH S909 expected=no finding got=none`; `fixtures-r55.md:14` says “An internal hyphen is not a line break.”
- S910 — CARRIED: `MATCH S910 expected=words=26 got=words=26`; `fixtures-r55.md:15` says “The source prints the long passage in guillemets.”
- S911 — CARRIED: `MATCH S911 expected=no finding got=none`; `fixtures-r55.md:16` says “This short guillemet passage is within the cap.”
- S912 — CARRIED: `MATCH S912 expected=words=22 got=words=22`; `fixtures-r55.md:17` says “An ellipsis joins two quoted fragments.”
- S913 — CARRIED: `MATCH S913 expected=no finding got=none`; `fixtures-r55.md:18` says “A leading ellipsis is within one span.”
- S914 — CARRIED: `MATCH S914 expected=no finding got=none`; `fixtures-r55.md:19` says “A trailing ellipsis is within one span.”
- S915 — DEFECT (tool): `MISMATCH S915 expected=words=26 got=none`; `fixtures-r55.md:20` says “This long excerpt uses an asterisk list marker.” `ROW` only recognizes a leading hyphen (`check-gate-quotes.py:18,79-80`), so it skips this valid Markdown `*` list item. Exact replacement: `ROW = re.compile(r"^(?:-\s+(?:\*\s+)?|\*\s+)(S\d+)\b")`. Update the documented row rule at line 18 to: `  * Only `- S### ` and `* S### ` rows inside that section, including `- * S### ` rows.`
- S916 — CARRIED: `MATCH S916 expected=no finding got=none`; `fixtures-r55.md:21` says “An asterisk inside content is not a list marker.”
- S917 — CARRIED (vacuous): `MATCH S917 expected=no finding got=none`; `fixtures-r55.md:22` says “This short asterisk-bulleted quote is within the cap.” The tool skips this `*` row too, so this match does not show the short quote was actually evaluated.

## Exact retained evidence

Copied the complete fixture directory and landed checker to `/fast/scratch/hyaku/kotodama-r55-falsify/ExecGateFixturesRun/`; copied lane `corpus/SOURCES.md` beside the fixture copy to test the documented registry lookup. Source and scratch-copy SHA-256 values matched:

- Checker: `cee36b40f2b355a4c8b4100abf821cdddb5650b68fc1650159a641481d3dbe9d`
- `fixtures-r55.md`: `1ae81bb18abbb4a90d20376d3d3243d44a04ed16a272895c3029cd3f413d23b6`
- `expect.tsv`: `7ce9272252ee651b4cd8d742bc5d54fbdbe5b9136ebc9273bb4170072d67c555`
- `run-fixtures.py`: `d3307e725ee9b50d3ee521805e371c5c30cf80a16d428a9e551d5521fff8ec00`
- Copied registry: `5a542a597d96e25b33f486d619c67757d51627fb7dbba4928247928135a7f6dc`; search for `| S904 |` returned no matches.

Command: `python3 -B /fast/scratch/hyaku/kotodama-r55-falsify/ExecGateFixturesRun/ExecGateFixtures/run-fixtures.py /fast/scratch/hyaku/kotodama-r55-falsify/ExecGateFixturesRun/lane/tools/check-gate-quotes.py`

```text
MISMATCH S901 expected=doubled-locator got=none
MATCH S902 expected=no finding got=none
MATCH S903 expected=no finding got=none
MISMATCH S904 expected=truncated-grounds got=none
MATCH S905 expected=no finding got=none
MATCH S906 expected=no finding got=none
MATCH S907 expected=no finding got=none
MATCH S908 expected=words=26 got=words=26
MATCH S909 expected=no finding got=none
MATCH S910 expected=words=26 got=words=26
MATCH S911 expected=no finding got=none
MATCH S912 expected=words=22 got=words=22
MATCH S913 expected=no finding got=none
MATCH S914 expected=no finding got=none
MISMATCH S915 expected=words=26 got=none
MATCH S916 expected=no finding got=none
MATCH S917 expected=no finding got=none
FIXTURES: 14/17 match; checker=/fast/scratch/hyaku/kotodama-r55-falsify/ExecGateFixturesRun/lane/tools/check-gate-quotes.py
EXIT=1
```

Files changed: only this report. No tools installed or updated. Risks: S904 is not a test of `truncated-grounds` until the fixture includes its registry row; S917's green result is currently vacuous. Blockers: none. Unrun: checker `--selftest`, claim-O acceptance, and other lane gates (outside this fixture assignment).