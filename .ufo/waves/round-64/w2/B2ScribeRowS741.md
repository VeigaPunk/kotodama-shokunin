# S741 — taboo words and children's avoidance

## Behavior and findings
Prepared one mined registry row and the matching learner bullet for the observed social learning of swear-word taboo and prohibition. The source is Carvalho and Gouvea's 2020 *Educação em Revista* research article, an original observation of a classroom dialogue among children aged 6–7. It records a child's account that people tell children a word is ugly; the authors interpret this as children understanding both the social dimension and prohibition of swearing, and adults transmitting bad-language meanings and teaching that such words should not be used.

**Tier A:** the row is scoped to the observed 6–7-year-old children's understanding in this one classroom; the article is the primary report of its own observation. It does not establish a general causal effect of correction on children's later avoidance. The authors identify the group’s specific sociocultural setting and caution that its concept of swear words cannot be generalized to other groups.

## Gates and evidence
- Web search queries: `taboo words children avoidance socialization study`; `children learn taboo words forbidden language acquisition taboo socialization paper`; `children learn what words are taboo avoidance taught to children linguistics taboo language socialization`.
- Opened the live SciELO HTML by plain `curl -sL --max-time 60` GET. Outcome: `HTTP_STATUS:200`; final URL remained `https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en`.
- The Wayback availability request initially returned HTTP 429 twice (the first saved response was `429 Too Many Requests`). A subsequent `curl -s --max-time 60 --get --data-urlencode 'url=https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en' 'https://archive.org/wayback/available'` returned HTTP 200 and `available: true`, status `200`, timestamp `20250115003509`; returned `closest.url` was `http://web.archive.org/web/20250115003509/https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en`. The row uses the requested `https://web.archive.org/web/<timestamp>id_/<original>` form.
- Lane locator, initial and required repeat: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en' 'We know it’s ugly because people tell us it’s ugly.'`; both printed `LOCATED https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en`.
- Row-format count: `awk -F'|' 'NR == 1 {print "ROW_FIELDS=" NF}' /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS741/row.txt` printed `ROW_FIELDS=13` (11 cells plus leading/trailing delimiter fields). Quote count: `printf '%s\n' 'We know it’s ugly because people tell us it’s ugly.' | wc -w` printed `10`.
- These are row-level checks only. `ACCEPT-C-64` and other round acceptance scripts were not run; no end-to-end claim is made.

## Touched surfaces and artifacts
- Wrote `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS741/row.txt` with the five required labelled lines.
- Saved source/capture lookup responses in `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS741/article.html`, `wayback.json`, `wayback-encoded.json`, and `wayback-retry.json`.
- Wrote this explicitly requested report at `.ufo/waves/round-64/w2/B2ScribeRowS741.md`.
- No registry, corpus entry, product code, judge, or lane state was edited. No tools were installed. No build, test, lint, or acceptance run was performed.

## Row deliverable
ROW: | S741 | Cibele Noronha de Carvalho and Maria Cristina Soares de Gouvea, 2020, “BAD WORD IS WHAT DOESN’T EXISTS ON GOD BODY”: A STUDY OF CHILDHOOD OBSCENE, Educação em Revista 36, e221704 - https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en ; capture https://web.archive.org/web/20250115003509id_/https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en | paper | A | observed 6–7-year-old children’s understanding of swear-word taboo and prohibition in one classroom | observed classroom dialogue, Tomás’s utterance: "We know it’s ugly because people tell us it’s ugly." | Helps worldbuilders portray children learning taboo status when adults label and prohibit words. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Children learn taboo status when people tell them words are ugly, giving worldbuilders a basis for everyday speech rules (S741)
VERIFY: LOCATED https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en
CAPTURE: timestamp=20250115003509; closest.url=http://web.archive.org/web/20250115003509/https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en
ACCESS: plain curl -sL --max-time 60 to the live SciELO HTML page, HTTP 200, 2026-10-23