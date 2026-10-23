# CtlOffTopicEcho59 — round-59 off-topic echo control

Axes at risk: **coverage** (a new filename need not contain new domain knowledge), **depth** (stem echoes need not teach anything), and **calibration** (TOPIC/RELEVANCE can accept plainly irrelevant prose). These are counterexample impacts, not admission or axis verdicts. LOCATE and BOILER are provenance filters, not semantic endorsement.

## Result and scope

- Built **24 distinct real-body rows over 20 hosts**. All 24 individually passed LOCATE, BOILER, RELEVANCE and TOPIC in five unchanged `rowcheck.py --draft` invocations. The first four invocations ran concurrently; no subagents or background jobs were used.
- The complete **23-row / 19-host** control passed all **14 non-SUPPORT legs**: **MEETS-MECHANICAL**. The full counter still exited 1, `ACCEPT-C-59: FAIL`.
- SUPPORT failed for missing registry/planted-key inputs (`FileNotFoundError`), consequently no verdicts or qualified seats. There was **no substantive NOT-SUPPORTED review** and no SUPPORT reviewer was dispatched. This is a missing-input failure, not evidence that SUPPORT actually distinguished these rows. No MEETS-COUNTER result was obtained.
- The initial 20-row control additionally failed BOILER because the Allrecipes root and its declared fallback failed in that run. Its draft check had passed. I did not re-run that error to seek a green result: the second, different control removes that citation and adds four other real pages, using new IDs.
- Frozen declaration: `1b80ee41f544d17c0410733a47a3eecac01bf25e`; claim base: `39c9ce8a6be5e5625d8befb54df53d621a3a7929`. Counters were not edited, monkey-patched, or supplied replacement network bodies/caches. Claim D was read as required but not attacked in this assignment.
- All data changes and commands were confined to `/fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/clone` and its scratch parent, apart from this report and its bounded fixture copies. Sources were opened by ordinary urllib GET; no challenge, login or paywall was crossed. No tools were installed or updated.

## Full frozen-counter controls

All commands below ran with the clone root as cwd. The counter subprocess command was `timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py`; its actual stdout and exit status were captured by the scratch-only `score.py` wrapper. The wrapper’s outer invocation used `timeout 910`.

CONTROL off-topic-echo20 | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [BOILER, SUPPORT]

Command:
```sh
timeout 910 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/score.py
# counter subprocess:
timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py
```

Pasted counter stdout:
```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:49Z failing=[]
BOILER FAIL passing=19 cited=20 at=2026-10-23T02:49Z failing=['S611: root-unfetchable https://www.allrecipes.com/ HTTPError; capture https://web.archive.org/web/2026id_/https://www.allrecipes.com/ HTTPError']
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:49Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:49Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=19 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

CONTROL MEETS-MECHANICAL-off-topic-echo23 | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SUPPORT]

Command:
```sh
timeout 910 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/score.py accept-c-v2.json
# counter subprocess:
timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py
```

Pasted counter stdout:
```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=23 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=23 cited=23 at=2026-10-23T02:51Z failing=[]
BOILER PASS passing=23 cited=23 at=2026-10-23T02:51Z failing=[]
RELEVANCE PASS passing=23 cited=23 at=2026-10-23T02:51Z failing=[]
TOPIC PASS passing=23 cited=23 at=2026-10-23T02:51Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=19 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict', 'S622:no verdict', 'S623:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

## Every row that passed the four draft legs

Every row below has an observed **LOCATE PASS / BOILER PASS / RELEVANCE PASS / TOPIC PASS**. Numbers are quote windows / page windows / page DISCIPLINE matches from the opened body. All selected quotes have exactly one CHARM-GUARD window. The linked page is the real source, not an echo/search endpoint.

S611 passed its draft run but is **not cited by the 23-row control**, because of the later root-fetch failure above. The 23-row control cites S600–S610 and S612–S623 individually, with no range notation in the entry. S-ids are fixture identities only; none was reused for a different source. The uncited original S611 row remains in the sandbox registry.

| Row | Off-topic content | Source | Windows/terms | Real body quotation (anchor typography normalized where necessary) |
|---|---|---|---|---|
| S600 | cereal, food marketing or recipe | [www.generalmills.com](https://www.generalmills.com/news-and-stories/stories/the-history-of-lucky-charms) | 1/28/29 | Lucky Charms made its magical debut in 1964, thanks to product developer John Holahan’s creativity. |
| S601 | cereal, food marketing or recipe | [www.generalmills.com](https://www.generalmills.com/news-and-stories/stories/celebrating-60-years-of-magical-marshmallows-with-lucky-charms) | 1/26/27 | Lucky Charms has been a breakfast staple for six decades with its beloved frosted oat pieces and magically delicious marshmallows. |
| S602 | cereal, food marketing or recipe | [www.luckycharms.com](https://www.luckycharms.com/about) | 1/12/12 | Made with whole grain Lucky Charms is fortified with 12 vitamins and minerals, and is a good source of calcium. |
| S603 | cereal, food marketing or recipe | [www.smithsonianmag.com](https://www.smithsonianmag.com/sponsored/patents-and-trademarks-behind-lucky-charms-cereal-180962517/) | 1/6/2 | Since their release, Lucky Charms™ have evolved considerably, and their history can be traced in registered trademarks and patents. |
| S604 | cereal, food marketing or recipe | [www.backthenhistory.com](https://www.backthenhistory.com/articles/the-history-of-lucky-charms) | 1/5/5 | Today, Lucky Charms remains a popular breakfast cereal, so there's a good chance that even more marbits will be introduced in the future. |
| S605 | cereal, food marketing or recipe | [www.popsugar.com](https://www.popsugar.com/food/lucky-charms-cereal-boxes-34087858) | 1/12/11 | From the shape of the mallows to Lucky the Leprechaun's appearance, Lucky Charms and its boxes have seen a lot of changes in half a century. |
| S606 | cereal, food marketing or recipe | [www.delish.com](https://www.delish.com/cooking/recipe-ideas/a30982529/lucky-charms-marshmallow-treats-recipe/) | 1/11/11 | Think of the classic Rice Krispies treats you know and love, but with Lucky Charms added into the mix. |
| S607 | cereal, food marketing or recipe | [www.theslowroasteditalian.com](https://www.theslowroasteditalian.com/lucky-charms-marshmallow-treats-recipe/) | 1/24/24 | Whether they’re made with Lucky Charms or Rice Krispies , cereal treats are all about sugar structure and heat control. |
| S608 | cereal, food marketing or recipe | [www.thepioneerwoman.com](https://www.thepioneerwoman.com/food-cooking/recipes/a46913349/lucky-charms-bars-recipe/) | 1/10/10 | They're a dessert bar made with Lucky Charms cereal. |
| S609 | cereal, food marketing or recipe | [ourzestylife.com](https://ourzestylife.com/lucky-charms-treats/) | 1/16/19 | Lucky Charms bars are chewy, crunchy, and ready in 20 minutes. |
| S610 | cereal, food marketing or recipe | [crayonsandcravings.com](https://crayonsandcravings.com/lucky-charms-bars/) | 1/22/22 | You will need an entire box of Lucky Charms cereal, a whole bag of mini marshmallows, and a stick of butter. |
| S611 | cereal, food marketing or recipe | [www.allrecipes.com](https://www.allrecipes.com/lucky-charms-treats-recipe-7488435) | 1/8/8 | Remove from heat and stir in Lucky Charms Cereal, coating cereal with marshmallow mixture. |
| S612 | cereal, food marketing or recipe | [howtomakecerealtreats.com](https://howtomakecerealtreats.com/lucky-charms-treats/) | 1/23/22 | You'll of course need Lucky Charms cereal by General Mills. (Any store-brand version will work, but we prefer the original.) |
| S613 | cereal, food marketing or recipe | [emilyscook.com](https://emilyscook.com/lucky-charms-marshmallow-treats-recipe/) | 1/28/27 | The marshmallows inside Lucky Charms cereal tend to hold up well because they’re baked into the cereal pieces. |
| S614 | cereal, food marketing or recipe | [cozyplatter.com](https://cozyplatter.com/lucky-charms-marshmallow-treats-recipe/) | 1/25/26 | If you want to switch things up, try substituting the Lucky Charms with a gluten-free cereal if you have dietary restrictions. |
| S615 | cereal, food marketing or recipe | [saraflavors.com](https://saraflavors.com/lucky-charms-treats-recipe/) | 1/24/23 | Lucky Charms cereal is labeled gluten-free in many regions, but be sure to check your package ingredients to confirm. |
| S616 | film criticism/casting | [variety.com](https://variety.com/2020/film/reviews/amulet-review-1203483464/) | 1/12/11 | Actress Romola Garai makes a distinctive feature directorial debut with ’ Amulet ,’ even if this upscale horror drama is ultimately more impressive in the realm of style than substance. |
| S617 | film criticism/casting | [filmcarnage.com](https://filmcarnage.com/2022/01/24/review-amulet/) | 1/6/6 | Amulet is unfortunately a swing and a miss, the story isn’t entirely original and for the most part its atmosphere and aesthetic fall flat. |
| S618 | film criticism/casting | [signalhorizon.com](https://signalhorizon.com/amulet-explained-atonement-hurts-like-a-mother/) | 1/17/17 | Amulet is a layered film about stereotypes and retribution. |
| S619 | film criticism/casting | [itsblogginevil.com](https://itsblogginevil.com/2020/07/20/evil-uses-evil-as-a-conduit-in-amulet-reviewed-digital-screener-magnet-releasing/) | 1/17/17 | Cast in ’Amulet’s’ only male role is the Romanian born Alec Secareanu as Tomaz. |
| S620 | cereal, food marketing or recipe | [crayonsandcravings.com](https://crayonsandcravings.com/lucky-charms-sheet-cake/) | 1/25/25 | I will share how to easily make cereal milk and use it to make your cake packed with authentic Lucky Charms flavor. |
| S621 | cereal, food marketing or recipe | [crayonsandcravings.com](https://crayonsandcravings.com/st-patricks-day-pudding-parfaits/) | 1/16/16 | While pudding is setting, add a layer of Lucky Charms cereal to the bottom of your cups. |
| S622 | cereal, food marketing or recipe | [www.theslowroasteditalian.com](https://www.theslowroasteditalian.com/lucky-charms-no-bake-ice-box-pie-recipe/) | 1/20/20 | It all starts with a custom pie crust made from ground Lucky Charms cereal. |
| S623 | cereal, food marketing or recipe | [thesoccermomblog.com](https://thesoccermomblog.com/lucky-charms-cake/) | 1/29/29 | We infused the flavor of the Lucky Charms cereal into milk that we used to make the cake batter. |

### Exact rowcheck commands and pasted output

These are the actual five invocations, each exiting 0. The first four cover the initial twenty rows in interleaved partitions; the fifth covers the four additional rows. Full pasted stdout is also preserved in [rowcheck-receipts.txt](CtlOffTopicEcho59/rowcheck-receipts.txt).

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/draft-0.md --entry /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/entry.md
```
```text
S600 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.generalmills.com/news-and-stories/stories/the-history-of-lucky-charms | BOILER: root-clear https://www.generalmills.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'debut', 'lucky', 'magic'] | TOPIC: quote_hits=1 function_words=3 page_hits=28 page_terms=29 need=1/2/3/2
S604 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.backthenhistory.com/articles/the-history-of-lucky-charms | BOILER: root-clear https://www.backthenhistory.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'lucky', 'remai', 'today'] | TOPIC: quote_hits=1 function_words=5 page_hits=5 page_terms=5 need=1/2/3/2
S608 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.thepioneerwoman.com/food-cooking/recipes/a46913349/lucky-charms-bars-recipe/ | BOILER: root-clear https://www.thepioneerwoman.com/; not a title, h1 or meta label | RELEVANCE: shared=['cerea', 'charm', 'desse', 'lucky'] | TOPIC: quote_hits=1 function_words=2 page_hits=10 page_terms=10 need=1/2/3/2
S612 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://howtomakecerealtreats.com/lucky-charms-treats/ | BOILER: root-clear https://howtomakecerealtreats.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'cours', 'lucky', 'need'] | TOPIC: quote_hits=1 function_words=3 page_hits=23 page_terms=22 need=1/2/3/2
S616 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://variety.com/2020/film/reviews/amulet-review-1203483464/ | BOILER: root-clear https://variety.com/; not a title, h1 or meta label | RELEVANCE: shared=['actre', 'garai', 'make', 'romol'] | TOPIC: quote_hits=1 function_words=7 page_hits=12 page_terms=11 need=1/2/3/2
```

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/draft-1.md --entry /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/entry.md
```
```text
S601 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.generalmills.com/news-and-stories/stories/celebrating-60-years-of-magical-marshmallows-with-lucky-charms | BOILER: root-clear https://www.generalmills.com/; not a title, h1 or meta label | RELEVANCE: shared=['break', 'charm', 'lucky', 'stapl'] | TOPIC: quote_hits=1 function_words=6 page_hits=26 page_terms=27 need=1/2/3/2
S605 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.popsugar.com/food/lucky-charms-cereal-boxes-34087858 | BOILER: root-clear https://www.popsugar.com/; not a title, h1 or meta label | RELEVANCE: shared=['lepre', 'lucky', 'mallo', 'shape'] | TOPIC: quote_hits=1 function_words=8 page_hits=12 page_terms=11 need=1/2/3/2
S609 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://ourzestylife.com/lucky-charms-treats/ | BOILER: root-clear https://ourzestylife.com/; not a title, h1 or meta label | RELEVANCE: shared=['bars', 'charm', 'chewy', 'lucky'] | TOPIC: quote_hits=1 function_words=3 page_hits=16 page_terms=19 need=1/2/3/2
S613 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://emilyscook.com/lucky-charms-marshmallow-treats-recipe/ | BOILER: root-clear https://emilyscook.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'insid', 'lucky', 'marsh'] | TOPIC: quote_hits=1 function_words=2 page_hits=28 page_terms=27 need=1/2/3/2
S617 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://filmcarnage.com/2022/01/24/review-amulet/ | BOILER: root-clear https://filmcarnage.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'miss', 'swing', 'unfor'] | TOPIC: quote_hits=1 function_words=6 page_hits=6 page_terms=6 need=1/2/3/2
```

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/draft-2.md --entry /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/entry.md
```
```text
S602 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.luckycharms.com/about | BOILER: root-clear https://www.luckycharms.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'grain', 'lucky', 'whole'] | TOPIC: quote_hits=1 function_words=5 page_hits=12 page_terms=12 need=1/2/3/2
S606 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.delish.com/cooking/recipe-ideas/a30982529/lucky-charms-marshmallow-treats-recipe/ | BOILER: root-clear https://www.delish.com/; not a title, h1 or meta label | RELEVANCE: shared=['class', 'krisp', 'rice', 'think'] | TOPIC: quote_hits=1 function_words=4 page_hits=11 page_terms=11 need=1/2/3/2
S610 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://crayonsandcravings.com/lucky-charms-bars/ | BOILER: root-clear https://crayonsandcravings.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'entir', 'lucky', 'need'] | TOPIC: quote_hits=1 function_words=4 page_hits=22 page_terms=22 need=1/2/3/2
S614 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://cozyplatter.com/lucky-charms-marshmallow-treats-recipe/ | BOILER: root-clear https://cozyplatter.com/; not a title, h1 or meta label | RELEVANCE: shared=['subst', 'switc', 'thing', 'want'] | TOPIC: quote_hits=1 function_words=4 page_hits=25 page_terms=26 need=1/2/3/2
S618 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://signalhorizon.com/amulet-explained-atonement-hurts-like-a-mother/ | BOILER: root-clear https://signalhorizon.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'film', 'layer', 'stere'] | TOPIC: quote_hits=1 function_words=3 page_hits=17 page_terms=17 need=1/2/3/2
```

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/draft-3.md --entry /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/entry.md
```
```text
S603 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.smithsonianmag.com/sponsored/patents-and-trademarks-behind-lucky-charms-cereal-180962517/ | BOILER: root-clear https://www.smithsonianmag.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'evolv', 'lucky', 'relea'] | TOPIC: quote_hits=1 function_words=4 page_hits=6 page_terms=2 need=1/2/3/2
S607 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.theslowroasteditalian.com/lucky-charms-marshmallow-treats-recipe/ | BOILER: root-clear https://www.theslowroasteditalian.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'krisp', 'lucky', 'rice'] | TOPIC: quote_hits=1 function_words=4 page_hits=24 page_terms=24 need=1/2/3/2
S611 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.allrecipes.com/lucky-charms-treats-recipe-7488435 | BOILER: root-clear https://www.allrecipes.com/; not a title, h1 or meta label | RELEVANCE: shared=['heat', 'lucky', 'remov', 'stir'] | TOPIC: quote_hits=1 function_words=4 page_hits=8 page_terms=8 need=1/2/3/2
S615 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://saraflavors.com/lucky-charms-treats-recipe/ | BOILER: root-clear https://saraflavors.com/; not a title, h1 or meta label | RELEVANCE: shared=['cerea', 'charm', 'label', 'lucky'] | TOPIC: quote_hits=1 function_words=4 page_hits=24 page_terms=23 need=1/2/3/2
S619 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://itsblogginevil.com/2020/07/20/evil-uses-evil-as-a-conduit-in-amulet-reviewed-digital-screener-magnet-releasing/ | BOILER: root-clear https://itsblogginevil.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'cast', 'male', 'role'] | TOPIC: quote_hits=1 function_words=4 page_hits=17 page_terms=17 need=1/2/3/2
```

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/draft-extra.md --entry /fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59/entry-extra.md
```
```text
S620 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://crayonsandcravings.com/lucky-charms-sheet-cake/ | BOILER: root-clear https://crayonsandcravings.com/; not a title, h1 or meta label | RELEVANCE: shared=['cerea', 'easil', 'milk', 'share'] | TOPIC: quote_hits=1 function_words=3 page_hits=25 page_terms=25 need=1/2/3/2
S621 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://crayonsandcravings.com/st-patricks-day-pudding-parfaits/ | BOILER: root-clear https://crayonsandcravings.com/; not a title, h1 or meta label | RELEVANCE: shared=['layer', 'lucky', 'puddi', 'setti'] | TOPIC: quote_hits=1 function_words=5 page_hits=16 page_terms=16 need=1/2/3/2
S622 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.theslowroasteditalian.com/lucky-charms-no-bake-ice-box-pie-recipe/ | BOILER: root-clear https://www.theslowroasteditalian.com/; not a title, h1 or meta label | RELEVANCE: shared=['crust', 'custo', 'groun', 'start'] | TOPIC: quote_hits=1 function_words=3 page_hits=20 page_terms=20 need=1/2/3/2
S623 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://thesoccermomblog.com/lucky-charms-cake/ | BOILER: root-clear https://thesoccermomblog.com/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'flavo', 'infus', 'lucky'] | TOPIC: quote_hits=1 function_words=4 page_hits=29 page_terms=29 need=1/2/3/2
```

## Echo construction: no domain reading needed

The generator selects the first four quote words with different non-stop content stems, `a,b,c,d`, then emits exactly:

```text
teaches: A mechanical echo associates {a} with {b} and records {c} beside {d}.
entry:   For the working note, {d} accompanies {c} while {b} frames {a} (S###).
```

It checks that teaches copies no six-word run. Both cells deliberately share four stems with the quote but convey no protective-object knowledge. Initial twenty rows were generated before their draft checks. The four additional rows follow the identical algorithm; the expanded generator emitted all 24 rows as well (`GENERATED rows=24 hosts=20 six_word_runs=0`). Source sentences were selected from HTML `<p>` content, excluding script/style, then checked against the home page and title/h1/meta text. Apostrophe/quotation typography in two film anchors is normalized only to keep the outer anchor delimiter parseable; the locator’s word sequence is unchanged.

Strongest short examples:

- **S608**, a cooking page: “They're a dessert bar made with Lucky Charms cereal.” TOPIC passed with `quote_hits=1 function_words=2 page_hits=10 page_terms=10`. No claim about ritual protection is present.
- **S618**, a film review: “Amulet is a layered film about stereotypes and retribution.” TOPIC passed with `quote_hits=1 function_words=3 page_hits=17 page_terms=17`. The film title alone supplies both CHARM and GUARD through `amule`.
- S618 teaches is “A mechanical echo associates amulet with layered and records film beside stereotypes.” Its entry line is “For the working note, stereotypes accompanies film while layered frames amulet (S618).” RELEVANCE passed, without paraphrase, interpretation, or any fact about amulets.

The index fixture changes only the new entry’s index row, myth-symbol count 28→29, total 234→235 and footer vector 29/28/29/29/24/95→29/29/29/29/24/95. Tier B and mined status are deliberately supplied control cells, not endorsements of these sources for the claimed domain. SET/SWEEP/FLOOR therefore do not imply knowledge was acquired.

## Negative scouting and retained evidence

Scouted 47 distinct candidate URLs. Cereal marketing/history/recipes and *Amulet* film reviews produced the controls. Six charm-physics pages were also opened: CERN outreach, Space, Wikipedia, Scientific American, Gizmodo and Interesting Engineering. Their page window counts were respectively 0, 0, 1, 0, 1, 0, so none met PAGE_HITS=3; they were not smuggled into the passing draft. Other rejected candidates had ordinary HTTP errors, no usable body sentence, or no qualifying quote; errors were not treated as passes. The complete candidate results and captured body hashes are in [scouted.json](CtlOffTopicEcho59/scouted.json). HTML scouting bodies remain only in the scratch `bodies/` directory, not the lane and not a counter fetch cache.

Fixture copies (108,017 bytes total, below the 200 KB bound): [24 source rows](CtlOffTopicEcho59/rows.md), [initial entry](CtlOffTopicEcho59/entry-20.md), [23-row entry](CtlOffTopicEcho59/entry-23.md), [generator](CtlOffTopicEcho59/echo-generator.py), [row/quote metadata](CtlOffTopicEcho59/rows.json), [scouting results](CtlOffTopicEcho59/scouted.json), [initial counter receipt](CtlOffTopicEcho59/counter-20.json), [MEETS-MECHANICAL counter receipt](CtlOffTopicEcho59/counter-23.json), and [draft receipts](CtlOffTopicEcho59/rowcheck-receipts.txt). All report and fixture paths are lane-relative; the clone remains available at the absolute scratch path above. No live processes or services were left running.

## Counterexample and smallest safe correction

Evidence in frozen `reports/round-59/rowcheck.py`:

1. `window_hits` (267–274) permits the same stem to satisfy both sets. A movie title containing *Amulet* is consequently already a complete “protection” window, regardless of what the sentence asserts. `Lucky Charms` similarly pairs GUARD `lucky` with CHARM `charm`.
2. `topic` (296–311) counts DISCIPLINE occurrences, not distinct senses or asserted protective functions. Repeating a cereal brand or film title supplies the page thresholds. Ordinary sentence function words do not establish domain relevance.
3. `relevance` (218–239) checks shared stems, word count, final period and absence of a six-word copy. Interleaving four selected words defeats it mechanically; the entry need not state a grounded fact at all. Raising the overlap threshold cannot cure this type of echo.

This is a **fixable mechanical discriminator defect**, not an observed full-predicate bypass. SUPPORT remains the only possible substantive barrier in the passing mechanical control, and that barrier was absent rather than exercised here. Accepting filename/row-count gains in exchange for irrelevant content would be a coverage/quality/calibration trade for the canonical judge to reject, not a conclusion this critic can admit or judge. No native judge was invoked.

counter weaknesses: TOPIC admits cereal brands and film titles, and RELEVANCE admits deterministic stem echoes. Before data, the smallest safe correction is to freeze these negatives into the blind planted SUPPORT material, require explicit rejection of off-topic/echo statements, and retain mandatory substantive review of each cited entry sentence. To strengthen TOPIC itself, require the quoted assertion to identify a protective carrier/mark **and its apotropaic function in an attributed cultural context**, not just co-occurring stems; a same-word match or repeated proper name must not establish that relation. Do not fix this with a brand/title blacklist or a larger stem quota. Preserve the ordinary-fetch rule: the Allrecipes root failure was a correctly reported fetch failure, not permission to waive BOILER.
