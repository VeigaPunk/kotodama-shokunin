# ---------------------------------------------- part-selftest-fixtures.py ---
# owner: ExecSelftestFixtures.  Function definitions only (the CFG-CONTRACT
# item 5 slot, concatenated before part-main.py's `__main__` guard): the
# fixture builder `build_fixture(prefix, mut=None)`, the named mutation table
# `MUTANTS`, the documented non-red survivors `SURVIVORS`, and `_sfx_`-prefixed
# private helpers.  `_selftest_scratch()` is also here: part-selftest-run.py
# calls it with no arguments to agree on one scratch root.  This part defines
# no `_run_counter` and no `run_selftest` (owner ExecSelftestMutants) and
# removes nothing: the runner owns every cleanup.
#
# WHAT IS BUILT
#   One throw-away git repository per call, three commits, in the
#   `$HYAKU_SCRATCH/kotodama-r75/<prefix>` scratch tree (never /tmp; the
#   operator default `/fast/scratch/hyaku/kotodama-r75` is used only when no
#   env var is set):
#     base    the 808-row fixture registry (S077..S884), the 249-file
#             knowledge tree (six partitions 32/29/40/29/24/95, every file
#             exactly 478 words so the frozen ENTRIES floor is the derived
#             floor too), corpus/README.md with two preserved footers,
#             tools/check-cited-lines.py (the lane's real linter), and the
#             standing quarantine verdicts;
#     freeze  reports/round-75/claims.json (claim C: 9 rows, 3 entries, the
#             40-file triage prose, 9 fragments + 2 terms, the map pin, the 13
#             frozen leg names), the hash-pinned by-document renumber map, the
#             scratch-mirror receipt, the three collision id files and the two
#             guard proofs;
#     lands   the nine registry rows S885..S893, the three myth-symbol entries,
#             the lesson (`## Gate` admit + reject tables, triage counts,
#             `## Quarantine`), nine evidence captures, the gap-sweep receipt,
#             the README index rows + myth-symbol heading + appended footer.
#   The positive lands satisfies all thirteen frozen legs at round-75 shape.
#   Every fixture is independent: distinct prefixes get distinct lane and fleet
#   directories, no ports, no module state, no fixed paths beyond the scratch
#   root.
#
# MUTANTS: `(name, expected_leg, spec)` 3-tuples; `spec` is a dict (or a
#   zero-arg callable returning one).  Each spec applies ONE named defect.
#   Some defects necessarily redden a second leg - a missing row takes its
#   evidence coupling with it - and the table names the PRIMARY leg (the leg
#   whose own clause the defect violates).  Two spec forms are special:
#   `{"no_data": True}` (a lands commit after the freeze with no claim-C
#   artefact) and `{"lands_is_freeze": True}` (the graded `lands == freeze`
#   control).
#
# SURVIVORS: junk landings the w1 vacuity critique (CritCCounterVacuity.md)
#   showed the FROZEN wording cannot refuse offline (fabricated page truth,
#   filler-only entry prose, a fabricated mirror receipt).  They are recorded,
#   not asserted red: a mutant whose expected leg could not go red would make
#   the selftest lie.  The structural half of each survivor IS a mutant.
#
# Round-74 provenance: `.ufo/waves/round-74/counters/accept-c.py` lines
# 1991-2835 (`_pad_to _evidence_text claims_fixture build_fixture` and the
# git helpers), reshaped for the round-75 leg set and the by-document map.
# No new imports (PART A's imports only); no network; stdlib only.

_SFX_ACCESS = "2026-10-27"
_SFX_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
_SFX_CLAIMS = "reports/round-75/claims.json"
_SFX_REGISTRY = "corpus/SOURCES.md"
_SFX_LESSON = "corpus/lessons/round-75.md"
_SFX_EVIDENCE = "reports/round-75/evidence"
_SFX_README = "corpus/README.md"
_SFX_KNOWLEDGE = "corpus/knowledge"
_SFX_ASSIM = ".ufo/waves/round-75/assimilation"
_SFX_RECEIPT = _SFX_ASSIM + "/validate-receipt.txt"
_SFX_GROUND = "reports/round-75/telemetry/gap-sweep.txt"
_SFX_GUARD = _SFX_ASSIM + "/guard-proof"
_SFX_MAP = _SFX_ASSIM + "/id-renumber-map.json"
_SFX_CITED = "tools/check-cited-lines.py"
_SFX_VERDICTS = "reports/round-71/telemetry/quarantine-verdicts.md"

_SFX_BASE_FIRST = 77          # base rows S077..S884 = 808 rows, last id S884
_SFX_BASE_LAST = 884
_SFX_BASE_PARTITIONS = (("linguistics", 32), ("myth-symbol", 29),
                        ("culture-material", 40), ("synthesis", 29),
                        ("verification", 24), ("civilizations", 95))
_SFX_LANDS_MYTH = 32          # 29 base + the three adopted entries
_SFX_BASE_WORDS = 478         # the frozen ENTRIES floor, and the derived floor
_SFX_BODY_WORDS = 620         # every fixture entry body clears the floor

_SFX_U1113 = ("https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113")
_SFX_U1120 = ("https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120")
_SFX_U1114 = ("https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114")
_SFX_UUCASS = "https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf"
_SFX_UJCSS = "https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf"
_SFX_UJSIK = ("https://www.jstage.jst.go.jp/article/jsik/32/2/"
              "32_2022_017/_pdf")
_SFX_UUNIGE = ("https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html")
_SFX_UUNIPA = ("https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-"
               "e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf")
_SFX_UCW23 = ("https://www.chinawriter.com.cn/n1/2023/0922/"
              "c404024-40083104.html")

# (id, staged ids, document url, kind, tier, source-cell lead, scope,
#  located quote, teaches) - the round-75 row_set, one row per DOCUMENT.
_SFX_ROWS = (
    ("S885", ("S876", "S885", "S917", "S921"), _SFX_U1113, "paper", "A",
     "Roland Barthes, «Introduction à l'analyse structurale des récits», "
     "Communications 8 (1966), 1-27",
     "the article's own structural method, in the article's own words",
     "Innombrables sont les récits du monde.",
     "narrative described at several levels of description at once, and the "
     "hierarchy between those levels"),
    ("S886", ("S902",), _SFX_U1120, "paper", "A",
     "Tzvetan Todorov, «Les catégories du récit littéraire», Communications 8 "
     "(1966), 125-151",
     "a primary structuralist account of the categories of narrative",
     "Les catégories du récit littéraire",
     "temporal deformation as the feature that separates discourse from "
     "history"),
    ("S887", ("S904",), _SFX_U1114, "paper", "A",
     "A. J. Greimas, «Éléments pour une théorie de l'interprétation du récit "
     "mythique», Communications 8 (1966), 28-59",
     "the two isotopies of a mythic narrative",
     "Loin de se limiter à l'interprétation des énoncés, la théorie sémantique",
     "one message read twice, on the discursive plane and on the structural "
     "plane"),
    ("S888", ("S864",), _SFX_UUCASS, "docs", "B",
     "中国社会科学院大学 研究生院,《叙事学》课程大纲 (课程编号 102072020193)",
     "the Chinese-language narratology canon and course architecture",
     "故事是一种深层的抽象结构，必须通过话语呈现",
     "story as deep structure against discourse as its presentation"),
    ("S889", ("S865",), _SFX_UJCSS, "paper", "B",
     "小方 孝,「物語生成の物語論あるいはポストナラトロジー」, Cognitive Studies "
     "25(2), 200-217 (2018)",
     "a Japanese-language systematic theory of narrative generation",
     "a new research area called “narratology of narrative generation”",
     "narratives modelled as generated across layers and disciplines"),
    ("S890", ("S866",), _SFX_UJSIK, "paper", "B",
     "村井 源,「物語構造の階層的記述方式の提案」, 情報知識学会誌 32(2), 246-251 "
     "(2022)",
     "a machine-writable three-layer description format for narrative",
     "describe a story as a hierarchical structure consisting of three major "
     "layers",
     "ストーリー / クエスト / シーン as a writable three-layer spec"),
    ("S891", ("S905",), _SFX_UUNIGE, "paper", "B",
     "Roland Barthes, S/Z (Paris: Seuil, 1970), the five codes in the "
     "accessible excerpt",
     "the five codes of S/Z and their definitions",
     "les premières lexies suscitent l'établissement des cinq grands codes",
     "hermeneutic, semantic, symbolic, proairetic and gnomic codes as five "
     "simultaneous voices"),
    ("S892", ("S919",), _SFX_UUNIPA, "paper", "B",
     "Gianfranco Marrone, «L'âge d'or de la sémiotique littéraire», Signata 5 "
     "(2014), 57-72",
     "what the scholarly literature says about where the five codes come from",
     "Mais combien, et de quelle nature, sont ces codes ?",
     "the codes read as a received typology rather than a rule system"),
    ("S893", ("S870",), _SFX_UCW23, "community", "C",
     "三九音域「世界观是打开小说幻想屋的钥匙」, 中国作家网, 2023-09-22",
     "the native practitioner vocabulary of Chinese web-fiction world-building",
     "网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则",
     "世界观 as the rules by which a world's things operate (Tier C, "
     "lead-level only)"),
)

_SFX_LOCATORS = {
    "S885": "notice de l'article and the article's opening paragraph",
    "S886": "p. 125, the article's opening paragraph",
    "S887": "p. 29, the paragraph on the two isotopies",
    "S888": "课程教学计划「第二讲 故事：事件（一）」第 1 点",
    "S889": "PDF p. 1, the 解 説 abstract",
    "S890": "PDF p. 1, the 抄録 abstract",
    "S891": "the «S/Z» paragraph on the five great codes",
    "S892": "p. 58, the paragraph posing the question",
    "S893": "§世界观是打开小说幻想屋的钥匙, paragraph 1, sentence 2",
}

_SFX_ENTRY_A = (_SFX_KNOWLEDGE + "/myth-symbol/"
                "narrative-structure-frameworks.md")
_SFX_ENTRY_B = (_SFX_KNOWLEDGE + "/myth-symbol/"
                "narrative-structure-frameworks.amend-2026-10-23.md")
_SFX_ENTRY_C = (_SFX_KNOWLEDGE + "/myth-symbol/"
                "narrative-structure-frameworks.amend-2026-10-23b.md")
_SFX_ENTRIES = (_SFX_ENTRY_A, _SFX_ENTRY_B, _SFX_ENTRY_C)

_SFX_ENTRY_SPECS = (
    {"path": _SFX_ENTRY_A,
     "title": "Narrative structure frameworks — the Western anchor beside the "
              "Chinese and Japanese frames",
     "sources": ("S885", "S888", "S889", "S890", "S893"),
     "ground": "round 1's CANNOT-ANSWER — the narrative entry was sourced only "
               "from Chinese and Japanese theory, and the wave brief names the "
               "Western primary source as the question to close.",
     "topic": "narrative structure as a build order for an invented culture, "
              "from the Chinese, Japanese and Western structuralist sources "
              "side by side: the story/discourse split, the actantial model, "
              "the three time axes, the Japanese three-layer description "
              "format and the 1966 structuralist method of describing a "
              "narrative at several levels at once — a reference method for "
              "the myth-symbol partition, deciding no culture's story",
     "gap": "the lane held the four Western etic toolkits in "
            "`myth-symbol/comparative-frameworks.md` and held no file that "
            "governed narrative structure as such.",
     "couples": "`myth-symbol/comparative-frameworks.md` (the four mythic "
                "toolkits this entry does not repeat).",
     "scope": "a reference method for the myth-symbol partition; it decides no "
              "culture's story (lore-shokunin owns canon).",
     "heading": "The Western anchor beside the Chinese and Japanese frames",
     "beats": (
         "- **§1 The structuralist premise** — narrative as a formal object "
         "described at several levels at once rather than a genre surveyed "
         "(S885).",
         "- **§2 The Chinese frame** — 故事 as deep structure against 话语 as "
         "surface presentation, with the actantial model and the three time "
         "axes beside it (S888).",
         "- **§3 The Japanese frame** — a three-layer description format with "
         "its character sub-layer, and 起承転結 as a minimal completable unit "
         "rather than a four-beat plot (S890).",
         "- **§4 The generation side** — a systematic theory of how narratives "
         "are produced, not only how they are read (S889).",
         "- **§5 The practitioner register** — 世界观 as a rule-system, "
         "recorded as vocabulary and never as authority (S893).",
     )},
    {"path": _SFX_ENTRY_B,
     "title": "Amendment — a second and a mythic primary voice for narrative "
              "description",
     "sources": ("S885", "S886", "S887", "S891", "S892"),
     "ground": "round 3's CANNOT-ANSWER — the five codes could not be recovered "
               "from the transcription, so the Western anchor was one article "
               "read partly.",
     "topic": "the two 1966 Communications primary voices the notice-only "
              "anchor could not carry — Todorov on the categories of narrative "
              "and Greimas on the two isotopies of a mythic narrative — "
              "together with the five codes of S/Z and the scholarly statement "
              "of where those codes come from — an amendment correcting an "
              "attribution rather than re-teaching the codes",
     "gap": "the lane held Greimas's Sémantique structurale and the four etic "
            "toolkits, and held no primary source from the issue the Western "
            "structuralist canon was written in.",
     "couples": "`myth-symbol/hero-journey-variants.md` (Campbell's variants "
                "this amendment does not restate).",
     "scope": "an amendment to the narrative-structure entry; it adds primary "
              "sources and corrects an attribution.",
     "heading": "The dated addition",
     "beats": (
         "- **§N Narrative categories** — temporality as the decisive axis, "
         "with temporal deformation separating discourse from history (S886).",
         "- **§N+1 Two readings of a mythic narrative** — the message occupies "
         "two isotopies at once and the narrative is a single semantic "
         "structure to begin with (S887).",
         "- **§N+2 The levels of description** — the hierarchy of levels and "
         "the rule that no level produces sense alone (S885).",
         "- **§N+3 The five codes** — hermeneutic, semantic, symbolic, "
         "proairetic and gnomic as five simultaneous voices (S891).",
         "- **§N+4 Where the codes come from** — the scholarly statement of the "
         "typology's provenance, so the codes are not conflated with a rule "
         "system (S892).",
     )},
    {"path": _SFX_ENTRY_C,
     "title": "Amendment b — the mythic reading folded from the refused drafts",
     "sources": ("S885", "S887"),
     "ground": "round 4's CANNOT-ANSWER — the mythic reading was carried by two "
               "separate amendment drafts that were refused as separate paths.",
     "topic": "the mythic reading folded from the refused 23c and 24 amendment "
              "drafts into one admitted amendment path — Greimas's two "
              "isotopies beside Barthes's levels of description, with the "
              "folded material carried as prose here and never as a separate "
              "file path",
     "gap": "the refused drafts' material had no admitted path, so the mythic "
            "reading had no file of its own.",
     "couples": "`myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` "
                "(the amendment this one folds into).",
     "scope": "a folded amendment path; it adds no document the registry does "
              "not already hold.",
     "heading": "The folded reading",
     "beats": (
         "- **§F1 Why a fold** — two drafts were refused as separate paths, so "
         "their material lands here as prose and no separate file path is "
         "claimed (S887).",
         "- **§F2 The reading itself** — the mythic message read on the "
         "discursive plane and on the structural plane, set equivalent rather "
         "than ranked (S885).",
         "- **§F3 What the fold does not do** — it adds no new document, no new "
         "registry row and no new claim about mythic narrative.",
     )},
)

_SFX_PREFIX_HEAD = """\
# SOURCES — selftest fixture registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
"""

_SFX_FILLER = ("fixture entry padding carries no claim about the lane and keeps "
               "the derived length floor stable").split()


# --------------------------------------------------------------- scratch ---

def _selftest_scratch():
    """The selftest scratch ROOT (`<HYAKU_SCRATCH>/kotodama-r75`).

    Honours $HYAKU_SCRATCH, then the older $SHOKUNIN_SCRATCH spelling, then
    the operator default `/fast/scratch/hyaku/kotodama-r75`, and only as a
    last resort the system temporary directory (never a hardcoded /tmp).
    """
    base = (os.environ.get("HYAKU_SCRATCH")
            or os.environ.get("SHOKUNIN_SCRATCH") or "").strip()
    if base:
        return os.path.join(os.path.abspath(base), "kotodama-r75")
    fast = "/fast/scratch/hyaku"
    if os.path.isdir(fast) and os.access(fast, os.W_OK):
        return os.path.join(fast, "kotodama-r75")
    return os.path.join(tempfile.gettempdir(), "kotodama-r75")


def _sfx_slug(text):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(text)).strip("-") or "fixture"


# ----------------------------------------------------------- git helpers ---

def _sfx_git(lane, *args, **kw):
    env = dict(os.environ)
    when = kw.get("when")
    if when:
        env["GIT_AUTHOR_DATE"] = when
        env["GIT_COMMITTER_DATE"] = when
    return subprocess.run(["git", "-C", lane] + list(args),
                          capture_output=True, text=True, env=env)


def _sfx_write(root, rel, text):
    path = os.path.join(root, rel)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _sfx_read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


def _sfx_init(lane):
    r = _sfx_git(lane, "init", "-q")
    if r.returncode != 0:
        raise RuntimeError("git init failed in %s: %s" % (lane, r.stderr))
    top = _sfx_git(lane, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(lane):
        raise RuntimeError("fixture toplevel %r is not %r" % (top, lane))


def _sfx_commit(lane, message, when):
    r = _sfx_git(lane, "add", "-A")
    if r.returncode != 0:
        raise RuntimeError("git add failed: %s" % r.stderr.strip())
    r = _sfx_git(lane, "-c", "user.name=selftest",
                 "-c", "user.email=selftest@fixture.invalid",
                 "commit", "-q", "-m", message, when=when)
    if r.returncode != 0:
        raise RuntimeError("git commit failed: %s" % r.stderr.strip())
    head = _sfx_git(lane, "rev-parse", "HEAD").stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise RuntimeError("fixture commit yielded no 40-hex revision")
    return head


# -------------------------------------------------------------- content ---

def _sfx_tokens(n, seed=0):
    out = []
    for i in range(n):
        out.append(_SFX_FILLER[(i + seed) % len(_SFX_FILLER)])
    return out


def _sfx_knowledge_text(name, words=_SFX_BASE_WORDS):
    """A base knowledge file of exactly `words` whitespace tokens.

    The header words count too, so the smallest base entry is exactly the
    frozen 478-word floor: the derived floor and the frozen floor agree and the
    ENTRIES leg prints no provenance note.
    """
    head = ["#", name]
    body = _sfx_tokens(max(0, words - len(head)))
    return " ".join(head + body) + "\n"


def _sfx_url_of(sid):
    for row in _SFX_ROWS:
        if row[0] == sid:
            return row[2]
    raise KeyError(sid)


def _sfx_usedby(sid, specs):
    return [spec["path"] for spec in specs if sid in spec["sources"]]


def _sfx_registry_row(row, specs, quotes, over=None):
    """One 11-cell registry row; `over` names the mutation's single defect."""
    over = over or {}
    sid, _staged, url, kind, tier, lead, scope, _quote, teaches = row
    quote = quotes.get(sid, row[7])
    anchor = "quote located: «%s»" % quote
    used = ", ".join(_sfx_usedby(sid, specs))
    opened = over.get("opened", _SFX_ACCESS)
    recheck = over.get("recheck", "180d")
    status = over.get("status", "mined")
    anchor = over.get("anchor", anchor)
    used = over.get("usedby", used)
    if over.get("drop_teaches"):
        return ("| %s | %s — %s | %s | %s | %s | %s | mined | %s | %s | %s |"
                % (sid, lead, url, kind, tier, scope, anchor, opened, recheck,
                   used))
    teaches = over.get("teaches", teaches)
    return ("| %s | %s — %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
            % (sid, lead, url, kind, tier, scope, anchor, teaches, status,
               opened, recheck, used))


def _sfx_base_registry(mut):
    lines = [_SFX_PREFIX_HEAD]
    for num in range(_SFX_BASE_FIRST, _SFX_BASE_LAST + 1):
        sid = "S%03d" % num
        url = "https://example.invalid/src/%03d" % num
        if mut.get("ground_fragment_at_base") and num == 500:
            url = _SFX_UUNIPA
        lines.append(
            "| %s | fixture source %03d — %s | docs | B | fixture scope %03d | "
            "fixture anchor %03d | fixture teaches %03d | queued | 2026-10-19 | "
            "180d | %s/linguistics/linguistics-fixture-01.md |\n"
            % (sid, num, url, num, num, num, _SFX_KNOWLEDGE))
    return "".join(lines)


def _sfx_base_knowledge(mut):
    out = {}
    for part, count in _SFX_BASE_PARTITIONS:
        for i in range(1, count + 1):
            name = "%s-fixture-%02d.md" % (part, i)
            out["%s/%s/%s" % (_SFX_KNOWLEDGE, part, name)] = \
                _sfx_knowledge_text(name)
    return out


def _sfx_readme_base():
    parts = []
    for part, count in _SFX_BASE_PARTITIONS:
        parts.append("## %s/ (%d)\n- `%s-fixture-01.md` — a fixture topic line\n"
                     % (part, count, part))
    return ("""\
# kotodama-shokunin corpus index

revision: 2.21 — fixture index for the round-75 selftest lane.

""" + "\n".join(parts) + """
Total knowledge entries: 246.

Counts checked 2026-10-25 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 246 files; directory totals 32/29/40/29/24/92).

Total knowledge entries: 249.

Counts checked 2026-10-26 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 249 files; directory totals 32/29/40/29/24/95).

""")


def _sfx_readme_lands(base_text, specs, mut):
    """The lands README: myth-symbol heading, three index rows, new footer.

    Every change is inside the frozen INDEX exemption set; `index_*` keys inject
    exactly one defect each.
    """
    myth_heading = "## myth-symbol/ (%d)" % (_SFX_LANDS_MYTH
                                             if not mut.get("index_heading_stale")
                                             else 29)
    rows = []
    for spec in specs:
        topic = spec["topic"]
        if mut.get("index_topic_mismatch") and spec["path"] == _SFX_ENTRY_B:
            topic = spec["topic"].replace("an amendment correcting", "a note "
                                          "on")
        rows.append("- `%s` — %s" % (os.path.basename(spec["path"]), topic))
    if mut.get("index_missing_row"):
        rows = rows[:-1]
    if mut.get("index_row_duplicated"):
        rows.append(rows[0])
    text = base_text.replace("## myth-symbol/ (29)", myth_heading, 1)
    block = "\n".join(rows) + "\n"
    if mut.get("index_row_outside_section"):
        # one row moves into the linguistics section: the only row that is
        # then not inside myth-symbol.
        moved = rows[-1]
        text = text.replace("## linguistics/ (32)\n",
                            "## linguistics/ (32)\n" + moved + "\n", 1)
        block = "\n".join(rows[:-1]) + "\n"
    text = text.replace(myth_heading + "\n", myth_heading + "\n" + block, 1)
    if mut.get("index_sid_row"):
        text = text.replace(myth_heading + "\n",
                            myth_heading + "\n| S885 | registry row |\n", 1)
    total = 251 if mut.get("index_footer_total") else 252
    vector = ("32/31/40/29/24/95" if mut.get("index_footer_vector")
              else "32/32/40/29/24/95")
    text += ("Total knowledge entries: %d.\n\n"
             "Counts checked %s from the repo root:\n"
             "`find corpus/knowledge -type f -name '*.md' | wc -l`\n"
             "(total %d files; directory totals %s).\n"
             % (total, _SFX_ACCESS, total, vector))
    if mut.get("index_older_footer_edited"):
        text = text.replace("(total 246 files; directory totals "
                            "32/29/40/29/24/92).",
                            "(total 246 files; directory totals "
                            "32/29/40/29/24/93).", 1)
    return text


def _sfx_entry_text(spec, mut):
    """One entry: nine-field provenance header, one `## ` section, long body."""
    path = spec["path"]
    lines = ["# " + spec["title"], ""]
    for sid in spec["sources"]:
        lines.append("source: %s — %s — %s — fetched %s"
                     % (sid, _sfx_url_of(sid), _SFX_LOCATORS[sid], _SFX_ACCESS))
    if mut.get("source_staged_id") and path == _SFX_ENTRY_A:
        lines = [line.replace("source: S893 — ", "source: S870 — ")
                 if line.startswith("source: S893 ") else line
                 for line in lines]
    if mut.get("source_url_mismatch") and path == _SFX_ENTRY_B:
        lines = [line.replace("source: S886 — %s" % _SFX_U1120,
                              "source: S886 — https://example.invalid/other")
                 if line.startswith("source: S886 ") else line
                 for line in lines]
    lines += [
        "verified-at: " + _SFX_ACCESS,
        "recheck: 180d — re-run each row's own recheck command; every row's "
        "cadence is 180d (ran %s)" % _SFX_ACCESS,
        "ground: " + spec["ground"],
        "- topic: " + spec["topic"],
        "- gap filled: " + spec["gap"],
        "- sources: the rows above, each opened this round with a located "
        "quote.",
        "- couples: " + spec["couples"],
        "- scope: " + spec["scope"],
        "",
        "## " + spec["heading"],
        "",
    ]
    beats = list(spec["beats"])
    if mut.get("inline_staged") and path == _SFX_ENTRY_C:
        beats.append("- **§F4 A stray staged id** — the refused campaign id "
                     "S864 stands here (a defect).")
    if mut.get("inline_base_row") and path == _SFX_ENTRY_A:
        beats.append("- **§6 A base row** — the unrelated lane row S500 stands "
                     "here (a defect).")
    if mut.get("citedlines_multi_id") and path == _SFX_ENTRY_A:
        beats.append("- **§7 Two ids on one line** — S885 and S888 both stand "
                     "here (a defect).")
    if mut.get("citedlines_table_id") and path == _SFX_ENTRY_A:
        beats.append("| S885 | a table row carrying an id (a defect) |")
    text = "\n".join(lines + beats)
    if mut.get("entry_stub") and path == _SFX_ENTRY_C:
        text = "\n".join(lines[:-1])
    if mut.get("entry_body_short") and path == _SFX_ENTRY_C:
        return _sfx_pad(text, 200)
    if mut.get("entry_header_placeholder") and path == _SFX_ENTRY_A:
        text = re.sub(r"(?m)^- scope:.*$", "- scope: TODO", text, count=1)
    if mut.get("entry_template_token") and path == _SFX_ENTRY_B:
        text = re.sub(r"(?m)^ground:.*$", "ground: <the gap>", text, count=1)
    return _sfx_pad_body(text, _SFX_BODY_WORDS)


def _sfx_pad(text, target):
    pad = ("The fixture body is padding only and exists to keep this entry "
           "comfortably above the length floor the counter reads from the "
           "frozen claim. ")
    while len(text.split()) < target:
        text += pad
    return text


def _sfx_pad_body(text, target):
    """Pad the SECTION BODY (everything from the first `## `) to `target` words.

    The ENTRIES leg counts only the body, so padding the whole file lets a long
    provenance header eat the body's length: pad where the gate looks.
    """
    idx = text.find("\n## ")
    if idx < 0:
        return text
    return text[:idx] + _sfx_pad(text[idx:], target)


def _sfx_window(quote, total, lead=560):
    head = " ".join(_sfx_tokens(4000, 5))[:lead]
    tail_len = max(0, total - len(head) - len(quote) - 2)
    tail = " ".join(_sfx_tokens(4200, 9))[:tail_len]
    return (head + " " + quote + " " + tail)[:total]


def _sfx_evidence_text(sid, url, quote, scope="excerpt", total=4200,
                       body_sha=None, window_sha=None, window_bytes=None,
                       status="200", ua=None, visible=None, access=None,
                       fetch_url=None, challenge="none", window=None):
    if window is None:
        window = _sfx_window(quote, total)
    payload = window.encode("utf-8")
    digest = window_sha or hashlib.sha256(payload).hexdigest()
    if visible is None:
        visible = len(window) + (900 if scope == "excerpt" else 0)
    ua = ua or _SFX_UA
    body_sha = body_sha or ("ab" * 32)
    if window_bytes is None:
        window_bytes = len(payload)
    return (
        "# evidence %s — claim C GATE (round 75 selftest fixture)\n"
        "url: %s\n"
        "ua: %s\n"
        "http: 200\n"
        "bytes: %d\n"
        "sha256: %s\n"
        "fetched: %sT10:00:00Z\n"
        "quote-found: yes\n"
        "quote-words: %d\n"
        "quote-chars: %d\n"
        "visible-chars: %s\n"
        "window-scope: %s\n"
        "window: chars=%d min=4096 pad=400 before=%d after=%d\n"
        "window-sha256: %s\n"
        "window-bytes: %d\n"
        "window-rule: sha256 of the single stored window line, UTF-8, no "
        "trailing newline\n"
        "quote-found-verbatim: yes\n"
        "challenge: %s\n"
        "challenge-detail: (none)\n"
        "content-type: text/html;charset=UTF-8\n"
        "final-url: %s\n"
        "extract: fixture text (synthetic; no network was used)\n"
        "fetch: GET %s\n"
        "user-agent: %s\n"
        "access-date: %s\n"
        "http-status: %s\n"
        "content-length: -\n"
        "transferred-bytes: %d\n"
        "fetch-attempts: 1\n"
        "locator: %s\n"
        "normalise: NFKC(per-character)+whitespace-fold; matched=verbatim\n"
        "quote: %s\n"
        "--- window ---\n"
        "%s\n"
        "--- quote ---\n"
        "%s\n"
        % (sid, url, ua, 12345, body_sha, _SFX_ACCESS, len(quote.split()),
           len(quote), visible, scope, len(window), 560, max(0, len(window) - 560),
           digest, window_bytes, challenge, url, fetch_url or url, ua,
           access or _SFX_ACCESS, status, 12345,
           _SFX_LOCATORS.get(sid, "fixture locator"), quote, window, quote))


def _sfx_evidence_files(specs, mut, quotes):
    """{path: text} for the nine adopted rows, one defect each when keyed."""
    out = {}
    for row in _SFX_ROWS:
        sid = row[0]
        if mut.get("evidence_missing") and sid == "S892":
            continue
        quote = quotes.get(sid, row[7])
        url = row[2]
        kwargs = {}
        scope = "excerpt"
        total = 4200
        if sid == "S885":
            # the one whole-document capture: 3720 visible chars < 4096.
            scope, total = "whole-document", 3720
        if mut.get("evidence_quote_absent") and sid == "S889":
            kwargs["window"] = _sfx_window("", total)
        if mut.get("window_sha_tamper") and sid == "S885":
            kwargs["window_sha"] = "0" * 64
        if mut.get("window_bytes_mismatch") and sid == "S890":
            kwargs["window_bytes"] = 17
        if mut.get("evidence_bad_ua") and sid == "S893":
            kwargs["ua"] = "curl/8.7.1"
        if mut.get("evidence_bad_status") and sid == "S891":
            kwargs["status"] = "403"
        if mut.get("evidence_bad_body_sha") and sid == "S886":
            kwargs["body_sha"] = "abc123"
        if mut.get("evidence_short_window") and sid == "S888":
            scope, total = "excerpt", 2000
        if mut.get("evidence_whole_4096") and sid == "S885":
            scope, total = "whole-document", 4200
            kwargs["visible"] = 4200
        if mut.get("evidence_visible_mismatch") and sid == "S886":
            scope, total = "whole-document", 3000
            kwargs["visible"] = 3005
        if mut.get("evidence_scope_unknown") and sid == "S892":
            scope = "full-page"
        if mut.get("evidence_fetch_other") and sid == "S892":
            kwargs["fetch_url"] = "https://example.invalid/other"
        text = _sfx_evidence_text(sid, url, quote, scope=scope, total=total,
                                  **kwargs)
        out["%s/%s.txt" % (_SFX_EVIDENCE, sid)] = text
    return out


def _sfx_lesson(specs, rows, mut, quotes):
    """The round-75 lesson: Gate admit + reject tables, triage, Quarantine."""
    admit = ["| source | access date | quote (<=25 words) | locator | evidence "
             "capture | verdict |",
             "|---|---|---|---|---|---|"]
    for row in rows:
        sid, _staged, url = row[0], row[1], row[2]
        quote = quotes.get(sid, row[7])
        date = _SFX_ACCESS
        cell_url = url
        locator = _SFX_LOCATORS[sid]
        if mut.get("gate_admit_date") and sid == "S890":
            date = "2026-10-26"
        if mut.get("gate_admit_locator") and sid == "S891":
            locator = "—"
        if mut.get("gate_admit_url") and sid == "S887":
            cell_url = "https://example.invalid/other"
        admit.append("| %s — %s | %s | \"%s\" | %s | %s/%s.txt (HTTP 200) | "
                     "admitted |"
                     % (sid, cell_url, date, quote, locator, _SFX_EVIDENCE, sid))
    reject = ["| item | reason | flip | probed URL | verdict |",
              "|---|---|---|---|---|",
              "| staged S870 quote | the staged quoted span is absent from the "
              "served page (a URL-quote mispairing) | re-open the document and "
              "quote afresh as lane S893 | %s | rejected |" % _SFX_UCW23]
    families = (
        ("naming-systems family (11)", "payload outside the declared "
         "narrative-structure theme", "a later round takes the naming-systems "
         "family", "probe/naming-systems"),
        ("calendar-festival-systems family (3)", "payload outside the declared "
         "theme", "a later round takes the calendar family",
         "probe/calendar-festival"),
        ("era-periodization-models family (2)", "payload outside the declared "
         "theme", "a later round takes the era family", "probe/era"),
        ("verification amendments (9)", "amendments with no admitted entry "
         "path", "a later round re-probes the amendments",
         "probe/verification"),
        ("conlang-scholarship amendments (3)", "the staged documents are "
         "already held by another leaf", "a later round re-probes them",
         "probe/conlang-scholarship"),
        ("conlang-methodology amendment (1)", "the staged document is already "
         "held by another leaf", "a later round re-probes it",
         "probe/conlang-methodology"),
        ("narrative-structure-frameworks amendment drafts (2)",
         "refused as separate paths; their material is folded into the "
         "admitted amendment", "no separate path is claimed again",
         "probe/narrative-amend"),
    )
    for label, why, flip, probe in families:
        line = ("| %s | %s | %s | https://example.invalid/%s | rejected |"
                % (label, why, flip, probe))
        if mut.get("rejects_family_renamed") and label.startswith("naming"):
            line = line.replace("naming-systems", "other-systems")
        reject.append(line)
    reject.append("| probe-only candidate | payload outside the declared "
                  "theme | a later round re-probes it | "
                  "https://example.invalid/probe/extra | rejected |")
    if mut.get("gate_reject_no_flip"):
        reject[-1] = reject[-1].replace("a later round re-probes it", "—")
    if mut.get("gate_reject_no_url"):
        reject[-1] = reject[-1].replace(
            "https://example.invalid/probe/extra", "the probed page")
    counts = ("Triage counts for the 40 staged knowledge files: 3 adopted / 6 "
              "path-present / 31 refused.")
    quarantine = """\
## Quarantine

The standing register verdicts (reports/round-71/telemetry/
quarantine-verdicts.md): 4 verdicts — PRESENT 1, REFUSED 2, UNVERIFIABLE 1.
The REFUSED register rows S816 and S817 stay refused; each document is
re-opened as new rows and no refused id is reused.

The narrative-structure staging refused no register row; the register records
are unchanged this round.
"""
    text = ("# Round 75 — narrative-structure-frameworks landing\n\n"
            "## Gate\n\n"
            "Admitted this round (every row opened %s by a plain request with "
            "the recorded browser-shaped UA):\n\n" % _SFX_ACCESS)
    text += "\n".join(admit) + "\n\n"
    text += ("Refused or not adopted from the assimilation set (reason + flip; "
             "every row names its probed URL):\n\n")
    text += "\n".join(reject) + "\n\n"
    if not mut.get("rejects_no_counts"):
        text += counts + "\n\n"
    if mut.get("rejects_no_s870"):
        text = text.replace("| staged S870 quote |", "| staged quote |")
    if mut.get("quarantine_missing"):
        quarantine = quarantine.replace("## Quarantine", "## Clearing notes")
    if mut.get("quarantine_no_refused"):
        quarantine = quarantine.replace(
            "The standing register verdicts (reports/round-71/telemetry/\n"
            "quarantine-verdicts.md): 4 verdicts — PRESENT 1, REFUSED 2, "
            "UNVERIFIABLE 1.\nThe REFUSED register rows S816 and S817 stay "
            "refused; each document is\nre-opened as new rows and no refused "
            "id is reused.\n\n", "")
    return text + quarantine


def _sfx_ground(mut):
    if mut.get("ground_missing"):
        return None
    lines = ["# round-75 gap sweep (selftest fixture)",
             "# stamp: %s 09:00:00 UTC" % _SFX_ACCESS,
             "gap-sweep at the %s-row registry (the claim base): 0 matches per "
             "fragment" % (817 if mut.get("ground_rows_wrong") else 808),
             "persee.fr/doc/comm_0588-8018_1966_num_8_1_1113: 0",
             "persee.fr/doc/comm_0588-8018_1966_num_8_1_1120: 0",
             "persee.fr/doc/comm_0588-8018_1966_num_8_1_1114: 0",
             "jw.ucass.edu.cn: 0",
             "jstage.jst.go.jp/article/jcss: 0",
             "jstage.jst.go.jp/article/jsik: 0",
             "unige.ch/lettres/framo: 0",
             "iris.unipa.it: 0",
             "chinawriter.com.cn/n1/2023/0922/c404024-40083104.html: 0",
             "narrative structure: 0",
             "narratology: 0"]
    if mut.get("ground_fragment_missing"):
        lines = [l for l in lines if not l.startswith("iris.unipa.it")]
    return "\n".join(lines) + "\n"


def _sfx_receipt(mut):
    if mut.get("receipt_missing"):
        return None
    flag = "validate" if mut.get("receipt_no_file_flag") else \
        "sources-census.sh validate --file"
    lines = ["# round-75 scratch-mirror validation receipt (selftest fixture)",
             "# stamp: %s 08:00:00 UTC" % _SFX_ACCESS,
             "$ %s <scratch>/mirror/corpus/SOURCES.md" % flag,
             "exit 1" if mut.get("receipt_no_exit") else "exit 0",
             "rows present in mirror: S885 S886 S887 S888 S889 S890 S891 S892 "
             "S893",
             "entries in mirror: %s" % ", ".join(_SFX_ENTRIES),
             "E-lines: 0"]
    if mut.get("receipt_missing_id"):
        lines = [l.replace("S888 ", "") if l.startswith("rows present") else l
                 for l in lines]
    return "\n".join(lines) + "\n"


def _sfx_guard_positive(mut):
    planted = "S884" if mut.get("coll_plant_real_id") else "S902"
    indent = "\t" if mut.get("coll_tab_plant") else "   "
    if mut.get("coll_lowercase_plant"):
        planted = "s902"
    return ("# 0-3-space-indent guard proof (selftest fixture)\n\n"
            "PLANTED at 1-3 spaces (staged id %s):\n"
            "%s| %s | planted indented row — https://example.invalid/planted | "
            "docs | B | s | §1 | planted | queued | %s | 90d | — |\n\n"
            "parser output: collision detected, the guard sees the plant: "
            "%s -> 1\nexit 1\n"
            % (planted, indent, planted, _SFX_ACCESS, planted))


def _sfx_guard_fourspace(mut):
    found = "4-space plant found: 1" if mut.get("coll_fourspace_found") else \
        "4-space plant: not found (0) — four or more spaces are indented code"
    return ("# four-space control (selftest fixture)\n\n"
            "4-space plant (staged id S904):\n"
            "    | S904 | four-space planted row | docs | B | s | §1 | planted "
            "| queued | %s | 90d | — |\n\n%s\n" % (_SFX_ACCESS, found))


def _sfx_map_text(mut):
    assignments = []
    for row in _SFX_ROWS:
        sid, staged, url = row[0], row[1], row[2]
        for old in staged:
            assignments.append({"staged_id": old, "new_lane_id": sid,
                                "url": url})
    mapping = {}
    for item in assignments:
        mapping[item["staged_id"]] = item["new_lane_id"]
    doc = {
        "round": 75,
        "status": "selftest fixture — the by-document renumber map",
        "join_key": "normalized document URL (host without www., path "
                    "percent-decoded, persee /doc/page/<slug>/… folded to "
                    "/doc/<slug>, web.archive.org wrapper stripped)",
        "assignments": assignments,
        "map": mapping,
    }
    return json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=False) + "\n"


def _sfx_claims_text(base, map_sha, rows, specs, mut):
    staged_text = {}
    for row in rows:
        staged_text[row[0]] = "/".join(row[1])
    row_set = [{"id": row[0], "staged": staged_text[row[0]],
                "document": "%s (%s)" % (row[2], row[5])} for row in rows]
    rejects = {
        "refused_staged_not_appended": [
            "S870's staged quote (absent on page; source re-opened as S893 "
            "with a fresh quote)"],
        "refused_files_pending_triage": [
            "naming-systems x11",
            "calendar-festival-systems x3",
            "era-periodization-models x2",
            "verification amendments x9",
            "conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24 x3",
            "conlang-methodology.amend-2026-10-24",
            "narrative-structure-frameworks.amend-2026-10-23c and "
            "amend-2026-10-24 refused as separate paths; their Barthes "
            "material is folded into the admitted amend-2026-10-23b entry; no "
            "separate file path is claimed"],
        # the L1 ruling (claims.json edited pre-data): the lesson's triple and
        # the frozen counts must agree, and the three numbers sum to the total.
        "counts": {
            "adopted": 3,
            "path_present": 6,
            "refused": 31,
            "total_staged_files": 40,
        },
    }
    legs = ["%s: selftest fixture leg (access date %s)" % (name, _SFX_ACCESS)
            for name in ("ENTRIES", "ROWS", "REPOINTED", "GATE", "EVIDENCE",
                         "REJECTS", "GROUND", "CITEDLINES", "CENSUS",
                         "SCRATCHMIRROR", "COLLCHECK", "FROZENCFG", "INDEX")]
    claim = {
        "id": "C",
        "axis": "coverage",
        "kind": "assimilation-sourced",
        "title": "shokuknow assimilation: narrative-structure-frameworks "
                 "theme (selftest fixture)",
        "before": "the fixture base holds 808 rows (S077..S884) and 249 "
                  "knowledge files, and no narrative-named knowledge file.",
        "after": "the fixture lands adds rows S885..S893, three myth-symbol "
                 "entries, the lesson, the evidence captures and the receipts.",
        "row_set": row_set,
        "reused_rows": [],
        "entries": list(_SFX_ENTRIES),
        "rejects": rejects,
        "ground": {
            "fragments": [
                "persee.fr/doc/comm_0588-8018_1966_num_8_1_1113",
                "persee.fr/doc/comm_0588-8018_1966_num_8_1_1120",
                "persee.fr/doc/comm_0588-8018_1966_num_8_1_1114",
                "jw.ucass.edu.cn",
                "jstage.jst.go.jp/article/jcss",
                "jstage.jst.go.jp/article/jsik",
                "unige.ch/lettres/framo",
                "iris.unipa.it",
                "chinawriter.com.cn/n1/2023/0922/c404024-40083104.html"],
            "terms": ["narrative structure", "narratology"],
        },
        "map": {"path": _SFX_MAP,
                "sha256": "0" * 64 if mut.get("map_sha_mismatch") else map_sha},
        "legs": legs,
        "access_date": _SFX_ACCESS,
        "owned_inplace": [{"path": _SFX_README, "base_line": 1,
                           "base_text": "## myth-symbol/ (29)",
                           "after_text": "## myth-symbol/ (32)"}],
    }
    doc = {"round": 75,
           "status": "selftest fixture — NOT the frozen round-75 claims",
           "frozen": "selftest",
           "base": base,
           "claims": [claim]}
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def _sfx_collision_files(mut):
    base_ids = ["S%03d" % n for n in range(_SFX_BASE_FIRST, _SFX_BASE_LAST + 1)]
    staged = []
    for row in _SFX_ROWS:
        for sid in row[1]:
            if sid not in staged:
                staged.append(sid)
    if mut.get("coll_staged_missing"):
        staged = [s for s in staged if s != "S921"]
    reg = list(base_ids)
    if mut.get("coll_adopted_in_regids"):
        reg.append("S885")
    collide = sorted(set(reg) & set(staged))
    if mut.get("coll_adopted_in_collisions"):
        collide.append("S890")
    return {"%s/reg-ids" % _SFX_ASSIM: "\n".join(reg) + "\n",
            "%s/staged-ids" % _SFX_ASSIM: "\n".join(staged) + "\n",
            "%s/collisions" % _SFX_ASSIM: "\n".join(collide) + "\n"}


_SFX_CENSUS_OK = ("#!/bin/sh\n"
                  "# selftest census stub (the counter only reads the TSV)\n"
                  "printf 'file\\tok\\tstub\\n'\n"
                  "exit 0\n")
_SFX_CENSUS_FAIL = ("#!/bin/sh\n"
                    "printf 'file\\tE06\\tS885 tier=Z\\n'\n"
                    "exit 1\n")


# ------------------------------------------------------------- builder ---

def build_fixture(prefix, mut=None):
    """A fresh three-commit fixture lane + its fleet root.

    Returns (lane, fleet, base, freeze, lands) as absolute paths/shas.  Every
    git call names the fixture (`git -C <lane>`), and the toplevel is asserted
    before the first commit.  The scratch directory `<root>/<prefix>` is this
    call's own and is recreated, never shared.
    """
    mut = dict(mut or {})
    root = os.path.join(_selftest_scratch(), _sfx_slug(prefix))
    shutil.rmtree(root, ignore_errors=True)
    lane = os.path.join(root, "lane")
    fleet = os.path.join(root, "fleet")
    os.makedirs(lane)
    os.makedirs(fleet)

    _sfx_write(fleet, "scripts/sources-census.sh",
               _SFX_CENSUS_FAIL if mut.get("census_fail") else _SFX_CENSUS_OK)
    os.chmod(os.path.join(fleet, "scripts/sources-census.sh"), 0o755)

    _sfx_init(lane)
    specs = [dict(s) for s in _SFX_ENTRY_SPECS]
    quotes = {}
    if mut.get("gate_quote_tokens"):
        # 26 single-letter whitespace tokens (51 characters): inside the
        # 80-character cap, over the 25-token cap.
        quotes["S890"] = " ".join("abcdefghijklmnopqrstuvwxyz"[i % 26]
                                  for i in range(26))
    if mut.get("gate_quote_chars"):
        # four 25-character tokens (103 characters): inside the token cap, over
        # the character cap.
        quotes["S886"] = " ".join(ch * 25 for ch in "ABCD")

    # ---- base ------------------------------------------------------------
    _sfx_write(lane, _SFX_REGISTRY, _sfx_base_registry(mut))
    for rel, text in _sfx_base_knowledge(mut).items():
        _sfx_write(lane, rel, text)
    _sfx_write(lane, _SFX_README, _sfx_readme_base())
    _sfx_write(lane, _SFX_VERDICTS,
               "# standing register verdicts (selftest fixture)\n\n"
               "| id | verdict |\n|---|---|\n"
               "| S816 | REFUSED |\n| S817 | REFUSED |\n"
               "| S820 | PRESENT |\n| S821 | UNVERIFIABLE |\n")
    _sfx_write(lane, _SFX_CITED, _sfx_citedlines_tool())
    if mut.get("entry_at_base"):
        _sfx_write(lane, _SFX_ENTRY_A,
                   _sfx_entry_text(specs[0], {}))
    base = _sfx_commit(lane, "base: fixture registry, knowledge tree, README",
                       "2026-10-27T09:00:00+00:00")

    # ---- freeze ----------------------------------------------------------
    map_text = _sfx_map_text(mut)
    map_sha = hashlib.sha256(map_text.encode("utf-8")).hexdigest()
    _sfx_write(lane, _SFX_MAP, map_text)
    _sfx_write(lane, _SFX_CLAIMS,
               _sfx_claims_text(base, map_sha, _SFX_ROWS, specs, mut))
    receipt = _sfx_receipt(mut)
    if receipt is not None and not mut.get("receipt_in_append"):
        _sfx_write(lane, _SFX_RECEIPT, receipt)
    for rel, text in _sfx_collision_files(mut).items():
        _sfx_write(lane, rel, text)
    _sfx_write(lane, _SFX_GUARD + "/guard-proof.txt", _sfx_guard_positive(mut))
    _sfx_write(lane, _SFX_GUARD + "/four-space-control.txt",
               _sfx_guard_fourspace(mut))
    freeze = _sfx_commit(
        lane, "freeze: claims.json, the by-document map, the mirror receipt, "
              "the collision files and the guard proofs",
        "2026-10-27T10:00:00+00:00")

    if mut.get("lands_is_freeze"):
        return lane, fleet, base, freeze, freeze

    # ---- lands -----------------------------------------------------------
    if mut.get("no_data"):
        _sfx_write(lane, _SFX_KNOWLEDGE + "/synthesis/scratch.md",
                   "# a scratch file that lands no claim-C artefact\n")
        lands = _sfx_commit(lane, "lands: no claim-C data (do-nothing control)",
                            "2026-10-27T11:00:00+00:00")
        return lane, fleet, base, freeze, lands

    registry = _sfx_base_registry(mut)
    extra = []
    for row in _SFX_ROWS:
        sid = row[0]
        if mut.get("row_missing_s890") and sid == "S890":
            continue
        over = {}
        if mut.get("row_staged_opened") and sid == "S886":
            over["opened"] = "2026-10-23"
        if mut.get("row_recheck_prose") and sid == "S887":
            over["recheck"] = "180d — re-read (ran %s)" % _SFX_ACCESS
        if mut.get("row_escaped_pipe") and sid == "S888":
            over["teaches"] = row[8] + " \\| planted"
        if mut.get("row_cell_count") and sid == "S893":
            over["drop_teaches"] = True
        if mut.get("row_status_queued") and sid == "S889":
            over["status"] = "queued"
        if mut.get("row_usedby_extra") and sid == "S892":
            over["usedby"] = ", ".join(_sfx_usedby(sid, specs) + [_SFX_ENTRY_A])
        if mut.get("row_usedby_missing") and sid == "S886":
            over["usedby"] = "—"
        if mut.get("row_anchor_no_quote") and sid == "S885":
            over["anchor"] = "page header"
        extra.append(_sfx_registry_row(row, specs, quotes, over))
    if mut.get("row_extra"):
        extra.append("| S894 | extra fixture row — https://example.invalid/extra "
                     "| docs | B | s | a | teaches extra | mined | %s | 180d | "
                     "%s |" % (_SFX_ACCESS, _SFX_ENTRY_A))
    registry = registry + "\n".join(extra) + "\n"
    if mut.get("row_removed_pre_existing"):
        registry = "\n".join(l for l in registry.splitlines()
                             if not l.startswith("| S500 |")) + "\n"
    if mut.get("row_pre_existing_edited"):
        registry = registry.replace("fixture teaches 500",
                                    "fixture teaches 500 (edited)", 1)
    _sfx_write(lane, _SFX_REGISTRY, registry)

    for spec in specs:
        if mut.get("entry_missing") and spec["path"] == _SFX_ENTRY_C:
            continue
        _sfx_write(lane, spec["path"], _sfx_entry_text(spec, mut))

    _sfx_write(lane, _SFX_LESSON, _sfx_lesson(specs, _SFX_ROWS, mut, quotes))
    ground = _sfx_ground(mut)
    if ground is not None:
        _sfx_write(lane, _SFX_GROUND, ground)
    for rel, text in _sfx_evidence_files(specs, mut, quotes).items():
        _sfx_write(lane, rel, text)
    _sfx_write(lane, _SFX_README, _sfx_readme_lands(
        _sfx_readme_base(), specs, mut))
    if mut.get("citedlines_tool_missing"):
        os.unlink(os.path.join(lane, _SFX_CITED))
    if mut.get("receipt_in_append") and receipt is not None:
        _sfx_write(lane, _SFX_RECEIPT, receipt)
    lands = _sfx_commit(
        lane, "lands: rows, entries, lesson, evidence, ground sweep, README",
        "2026-10-27T11:00:00+00:00")

    if mut.get("config_edited_at_lands"):
        text = _sfx_read(lane, _SFX_CLAIMS) + " "
        _sfx_write(lane, _SFX_CLAIMS, text)
        lands = _sfx_commit(lane, "lands: config edited after the freeze",
                            "2026-10-27T12:00:00+00:00")
    if mut.get("claims_missing_at_lands"):
        os.unlink(os.path.join(lane, _SFX_CLAIMS))
        lands = _sfx_commit(lane, "lands: claims.json removed",
                            "2026-10-27T12:00:00+00:00")
    return lane, fleet, base, freeze, lands


_SFX_CITED_TOOL = '''#!/usr/bin/env python3
"""Clause-scoping lint for cited lines (fixture copy).

A faithful reimplementation of the lane's tools/check-cited-lines.py contract
(round 61, claim O): per line, the distinct S-ids; MULTI-ID when a line carries
two or more, TABLE-ID when a line whose leading whitespace is stripped starts
with `|` and carries at least one.  The last stdout line is
`CITED-LINES: <k> finding(s) in <m> file(s)`; exit 1 when k > 0, 0 when k == 0.

Embedded in the fixture so the graded tool is the fixture's own bytes and does
not depend on where the assembled counter happens to live.
"""
import os
import re
import sys

SID = re.compile(r"\\bS\\d{3,}\\b")


def main(argv):
    paths = [a for a in argv if not a.startswith("-")]
    if not paths:
        sys.stderr.write("CITED_LINES_ERROR: no PATH given\\n")
        return 2
    findings = 0
    files = 0
    for path in paths:
        if os.path.isdir(path):
            todo = []
            for base, _dirs, names in os.walk(path):
                todo.extend(os.path.join(base, n) for n in sorted(names)
                            if n.endswith(".md"))
        elif os.path.isfile(path):
            todo = [path]
        else:
            sys.stderr.write("CITED_LINES_ERROR: cannot read %s\\n" % path)
            return 2
        for one in todo:
            try:
                with open(one, encoding="utf-8") as fh:
                    text = fh.read()
            except (OSError, UnicodeDecodeError) as exc:
                sys.stderr.write("CITED_LINES_ERROR: %s\\n" % exc)
                return 2
            files += 1
            for number, line in enumerate(text.splitlines(), 1):
                ids = sorted(set(SID.findall(line)), key=lambda t: int(t[1:]))
                if not ids:
                    continue
                kinds = []
                if len(ids) >= 2:
                    kinds.append("MULTI-ID")
                if line.lstrip().startswith("|"):
                    kinds.append("TABLE-ID")
                for kind in kinds:
                    findings += 1
                    print("%s %s:%d %s" % (kind, one, number, ",".join(ids)))
    print("CITED-LINES: %d finding(s) in %d file(s)" % (findings, files))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
'''


def _sfx_citedlines_tool():
    """The fixture's clause-scoping linter (see `_SFX_CITED_TOOL`).

    The frozen CITEDLINES wording pins no tool blob, so the fixture ships its
    own faithful implementation rather than reaching for the lane's copy (an
    assembled counter in a scratch directory has no lane to read, and a stub
    would hide the multi-id mutants - the w1 vacuity finding).
    """
    return _SFX_CITED_TOOL


# --------------------------------------------------------------- table ---
#
# Coverage of the w1 junk paths (each mutant is the structural half of a named
# junk landing; the survivors that no offline counter can refuse are in
# SURVIVORS):
#
#   CritCCounterVacuity.md per-leg junk
#     ENTRIES    filler-only body         -> mutant `entry_stub`/`entry_body_short`
#                (the pure filler body is SURVIVOR `entry_filler_body`)
#     ROWS       normalized copied row    -> `row_staged_opened`,
#                                           `row_recheck_prose`, `row_usedby_*`
#     REPOINTED  id/URL-only compliance   -> `source_url_mismatch`,
#                                           `inline_base_row`
#     GATE       fabricated short quote   -> `gate_quote_tokens/_chars`;
#                (page truth is SURVIVOR `gate_fabricated_quote`)
#     EVIDENCE   fabricated window        -> `window_sha_tamper`,
#                (the window's truth is SURVIVOR `evidence_fabricated_window`)
#     REJECTS    global reason/flip words -> `rejects_family_renamed`,
#                                           `rejects_no_s870`
#     GROUND     fabricated sweep         -> `ground_fragment_missing`,
#                                           `ground_rows_wrong`,
#                                           `ground_fragment_at_base`
#     CITEDLINES stub tool printed zero   -> `citedlines_multi_id`,
#                                           `citedlines_table_id`
#     CENSUS     semantically false cells -> `census_fail` (E-code/exit)
#     SCRATCHMIRROR fabricated receipt    -> `receipt_missing`, `receipt_no_exit`,
#                (prose-only mirror is SURVIVOR `mirror_fabricated_receipt`)
#     COLLCHECK  fabricated marker        -> `coll_plant_real_id`,
#                                           `coll_fourspace_found`
#     FROZENCFG  graded-tree config edit  -> `config_edited_at_lands`
#     INDEX      ghost/wrong-topic row    -> `index_missing_row`,
#                                           `index_topic_mismatch`,
#                                           `index_row_duplicated`
#
#   MutRegistryCollision.md m1..m8 (8 cases)
#     m1  2-space plant found             POSITIVE control: the clean guard
#                                        proof is exactly this fixture
#     m2  3-space plant found             POSITIVE control (same proof)
#     m3  4-space NOT found               `coll_fourspace_found` (states found)
#     m4  column-zero plant               `coll_plant_real_id`-class: the plant
#                                        must be a staged id AND inside the
#                                        1-3-space grammar
#     m5  tab plant is silent             `coll_tab_plant`
#     m6  lowercase id missed by guard    `coll_lowercase_plant`
#     m7  4-digit id survives             SURVIVOR `guard_four_digit_id`
#     m8  adopted id in the collision set `coll_adopted_in_collisions`,
#                                        `coll_adopted_in_regids`
#
#   junk-fixtures.py claim-C cases
#     J1  header-only stub entry          `entry_stub`
#     J2  Gate quote absent from windows  `evidence_quote_absent`
#     J3  graded-tree claims.json shrink  `config_edited_at_lands`,
#                                        `claims_missing_at_lands`
#     J4x/J5-J10/G/R are claim Ca's and are not fixtures of this counter.

MUTANTS = (
    # ENTRIES
    ("entry_missing", "ENTRIES", {"entry_missing": True}),
    ("entry_stub", "ENTRIES", {"entry_stub": True}),
    ("entry_body_short", "ENTRIES", {"entry_body_short": True}),
    ("entry_header_placeholder", "ENTRIES",
     {"entry_header_placeholder": True}),
    ("entry_template_token", "ENTRIES", {"entry_template_token": True}),
    ("entry_at_base", "ENTRIES", {"entry_at_base": True}),
    # ROWS
    ("row_extra", "ROWS", {"row_extra": True}),
    ("row_removed_pre_existing", "ROWS", {"row_removed_pre_existing": True}),
    ("row_pre_existing_edited", "ROWS", {"row_pre_existing_edited": True}),
    ("row_staged_opened", "ROWS", {"row_staged_opened": True}),
    ("row_recheck_prose", "ROWS", {"row_recheck_prose": True}),
    ("row_escaped_pipe", "ROWS", {"row_escaped_pipe": True}),
    ("row_cell_count", "ROWS", {"row_cell_count": True}),
    ("row_status_queued", "ROWS", {"row_status_queued": True}),
    ("row_usedby_extra", "ROWS", {"row_usedby_extra": True}),
    ("row_usedby_missing", "ROWS", {"row_usedby_missing": True}),
    ("row_anchor_no_quote", "ROWS", {"row_anchor_no_quote": True}),
    ("row_missing_s890", "ROWS", {"row_missing_s890": True}),
    # REPOINTED
    ("source_url_mismatch", "REPOINTED", {"source_url_mismatch": True}),
    ("source_staged_id", "REPOINTED", {"source_staged_id": True}),
    ("inline_staged", "REPOINTED", {"inline_staged": True}),
    ("inline_base_row", "REPOINTED", {"inline_base_row": True}),
    # GATE
    ("gate_quote_tokens", "GATE", {"gate_quote_tokens": True}),
    ("gate_quote_chars", "GATE", {"gate_quote_chars": True}),
    ("gate_admit_date", "GATE", {"gate_admit_date": True}),
    ("gate_admit_locator", "GATE", {"gate_admit_locator": True}),
    ("gate_admit_url", "GATE", {"gate_admit_url": True}),
    ("gate_reject_no_flip", "GATE", {"gate_reject_no_flip": True}),
    ("gate_reject_no_url", "GATE", {"gate_reject_no_url": True}),
    # EVIDENCE
    ("evidence_missing", "EVIDENCE", {"evidence_missing": True}),
    ("evidence_quote_absent", "EVIDENCE", {"evidence_quote_absent": True}),
    ("window_sha_tamper", "EVIDENCE", {"window_sha_tamper": True}),
    ("window_bytes_mismatch", "EVIDENCE", {"window_bytes_mismatch": True}),
    ("evidence_bad_ua", "EVIDENCE", {"evidence_bad_ua": True}),
    ("evidence_bad_status", "EVIDENCE", {"evidence_bad_status": True}),
    ("evidence_bad_body_sha", "EVIDENCE", {"evidence_bad_body_sha": True}),
    ("evidence_short_window", "EVIDENCE", {"evidence_short_window": True}),
    ("evidence_whole_4096", "EVIDENCE", {"evidence_whole_4096": True}),
    ("evidence_visible_mismatch", "EVIDENCE",
     {"evidence_visible_mismatch": True}),
    ("evidence_scope_unknown", "EVIDENCE", {"evidence_scope_unknown": True}),
    ("evidence_fetch_other", "EVIDENCE", {"evidence_fetch_other": True}),
    # REJECTS
    ("rejects_no_s870", "REJECTS", {"rejects_no_s870": True}),
    ("rejects_no_counts", "REJECTS", {"rejects_no_counts": True}),
    ("rejects_family_renamed", "REJECTS", {"rejects_family_renamed": True}),
    ("quarantine_missing", "REJECTS", {"quarantine_missing": True}),
    ("quarantine_no_refused", "REJECTS", {"quarantine_no_refused": True}),
    # GROUND
    ("ground_missing", "GROUND", {"ground_missing": True}),
    ("ground_fragment_missing", "GROUND", {"ground_fragment_missing": True}),
    ("ground_rows_wrong", "GROUND", {"ground_rows_wrong": True}),
    ("ground_fragment_at_base", "GROUND", {"ground_fragment_at_base": True}),
    # CITEDLINES
    ("citedlines_multi_id", "CITEDLINES", {"citedlines_multi_id": True}),
    ("citedlines_table_id", "CITEDLINES", {"citedlines_table_id": True}),
    ("citedlines_tool_missing", "CITEDLINES", {"citedlines_tool_missing": True}),
    # CENSUS
    ("census_fail", "CENSUS", {"census_fail": True}),
    # SCRATCHMIRROR
    ("receipt_missing", "SCRATCHMIRROR", {"receipt_missing": True}),
    ("receipt_no_exit", "SCRATCHMIRROR", {"receipt_no_exit": True}),
    ("receipt_missing_id", "SCRATCHMIRROR", {"receipt_missing_id": True}),
    ("receipt_in_append", "SCRATCHMIRROR", {"receipt_in_append": True}),
    ("receipt_no_file_flag", "SCRATCHMIRROR", {"receipt_no_file_flag": True}),
    # COLLCHECK
    ("coll_adopted_in_regids", "COLLCHECK", {"coll_adopted_in_regids": True}),
    ("coll_adopted_in_collisions", "COLLCHECK",
     {"coll_adopted_in_collisions": True}),
    ("coll_fourspace_found", "COLLCHECK", {"coll_fourspace_found": True}),
    ("coll_plant_real_id", "COLLCHECK", {"coll_plant_real_id": True}),
    ("coll_tab_plant", "COLLCHECK", {"coll_tab_plant": True}),
    ("coll_lowercase_plant", "COLLCHECK", {"coll_lowercase_plant": True}),
    ("coll_staged_missing", "COLLCHECK", {"coll_staged_missing": True}),
    # FROZENCFG
    ("config_edited_at_lands", "FROZENCFG", {"config_edited_at_lands": True}),
    ("claims_missing_at_lands", "FROZENCFG", {"claims_missing_at_lands": True}),
    ("map_sha_mismatch", "FROZENCFG", {"map_sha_mismatch": True}),
    # INDEX
    ("index_missing_row", "INDEX", {"index_missing_row": True}),
    ("index_topic_mismatch", "INDEX", {"index_topic_mismatch": True}),
    ("index_heading_stale", "INDEX", {"index_heading_stale": True}),
    ("index_footer_total", "INDEX", {"index_footer_total": True}),
    ("index_footer_vector", "INDEX", {"index_footer_vector": True}),
    ("index_older_footer_edited", "INDEX", {"index_older_footer_edited": True}),
    ("index_row_outside_section", "INDEX", {"index_row_outside_section": True}),
    ("index_row_duplicated", "INDEX", {"index_row_duplicated": True}),
    ("index_sid_row", "INDEX", {"index_sid_row": True}),
)

# Junk landings the FROZEN wording cannot refuse offline (w1
# CritCCounterVacuity.md): recorded, never asserted red.  Each survivor's
# structural half is one of the MUTANTS above (`entry_stub` for F7's shape,
# `window_sha_tamper` for F4's digest, `receipt_no_exit` for F2's prose).
SURVIVORS = (
    ("entry_filler_body", "ENTRIES",
     "a >=478-word filler body with a valid header is explicitly a "
     "length-and-shape gate (CritCCounterVacuity F7)"),
    ("gate_fabricated_quote", "GATE",
     "a plausible quote on a page nobody re-opened cannot be falsified by a "
     "committed-bytes counter (F5/F14); the routed ordinary re-open owns it"),
    ("evidence_fabricated_window", "EVIDENCE",
     "a fabricated window with a correct digest authenticates stored bytes, "
     "not a fetch (F4); the body sha256 is shape-graded"),
    ("mirror_fabricated_receipt", "SCRATCHMIRROR",
     "a receipt naming a mirror that never ran is prose-only evidence (F2); "
     "CENSUS owns the executed census"),
    ("guard_fabricated_marker", "COLLCHECK",
     "the guard is pattern-matched, not executed (F3); the planted id must at "
     "least be a staged id"),
    ("guard_four_digit_id", "COLLCHECK",
     "a 4-digit id (S1005) planted at 1-3 spaces is seen by the guard and, "
     "with no staged counterpart, collides with nothing (MutRegistryCollision "
     "m7/F3); the fixture's plant is a staged 3-digit id instead"),
    ("citedlines_stub_tool", "CITEDLINES",
     "the frozen wording pins no tool blob, so a stub printing the line "
     "passes (F1); this fixture ships the real tool instead"),
    ("ground_fabricated_receipt", "GROUND",
     "a syntactically matching sweep receipt is not provable offline (F8); "
     "the independent base re-derivation is what bites"),
)
