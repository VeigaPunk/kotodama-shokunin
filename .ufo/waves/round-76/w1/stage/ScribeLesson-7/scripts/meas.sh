#!/usr/bin/env bash
set -u
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
B=98c486bdb4650ba5b8e651d332910e8ee60ad121
W=$L/.ufo/waves/round-76
P=/home/vgpnk/Projects/shokuknow/merge/kotodama
R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
run(){ echo; echo "### \$ $*"; bash -c "$*" 2>&1; echo "[exit=$?]"; }
echo "# measurements — round 76, seat ScribeLesson-7 (2026-10-27)"
echo "# every block is a command and its raw output; cwd = $L unless a command cd's"
run "git -C $L cat-file -e $B && echo base-present"
run "git -C $L grep -l -E 'GB/T 33661' $B -- corpus   # the claims draft's own Before leg, as written"
run "git -C $L grep -l -E 'digital\\.archives\\.go\\.jp' $B -- corpus   # ditto"
run "git -C $L grep -l -E 'GB/T 33661' $B -- corpus/knowledge"
run "git -C $L grep -l -E 'digital\\.archives\\.go\\.jp' $B -- corpus/knowledge"
run "git -C $L ls-tree -r --name-only $B corpus/knowledge | grep -c '\\.md$'"
run "git -C $L show $B:corpus/SOURCES.md | grep -cE '^ {0,3}\\|[[:space:]]*S[0-9]{3,}'"
run "wc -l $W/assimilation/reg-ids $W/assimilation/staged-ids $W/assimilation/collisions"
run "sha256sum $W/assimilation/reg-ids $W/assimilation/staged-ids $W/assimilation/collisions"
run "grep -cE '^S89[4-8]\$' $W/assimilation/reg-ids; grep -cE '^S89[4-8]\$' $W/assimilation/staged-ids; grep -cE '^S89[4-8]\$' $W/assimilation/collisions"
run "python3 -c \"ids=[l.strip() for l in open('$W/assimilation/reg-ids') if l.strip()]; n={int(i[1:]) for i in ids}; m=[f'S{x:03d}' for x in range(1,894) if x not in n]; print(len(ids),'rows',len(n),'unique;',len(m),'missing:', ' '.join(m))\""
run "grep -E '^\\| *S(894|895|896|897|898) ' $P/SOURCES.append.md | sed -E 's/^\\| *(S[0-9]+).*?(https?:[^ |]+).*/\\1 \\2/; s/^\\| *(S[0-9]+).{0,140}.*/\\1 (no bare url)/'"
run "grep -E '^\\| *S(894|895|896|897|898) ' $P/SOURCES.append.md | cut -c1-150"
run "grep -E '^\\| *S(908|916|932|935|937|938) ' $P/SOURCES.append.md | awk -F'|' '{print \$2\",\"\$4\",\"\$5}'"
run "grep -cE '^\\| *S[0-9]{3} ' $P/SOURCES.append.md; grep -oE '^\\| *S[0-9]{3}' $P/SOURCES.append.md | tr -d '| ' | sort -u | tail -1"
run "sed -n '118p;134p' $R"
run "awk -F'|' -v l='kotodama' '\$2 ~ (\"\`\" l \"\`\") && \$3 ~ /round[0-9]+/ && \$4 ~ /S[0-9]+/' $R | wc -l"
run "awk -F'|' -v l='kotodama' '\$2 ~ (\"\`\" l \"\`\") && \$3 ~ /round[0-9]+/ && \$4 ~ /S[0-9]+/ {print \$7}' $R | grep -c '…'"
run "awk -F'|' -v l='kotodama' '\$2 ~ (\"\`\" l \"\`\") && \$3 ~ /round[0-9]+/ && \$4 ~ /S[0-9]+/ {print \$7}' $R | grep -c '<br>'"
run "git -C $L show $B:corpus/SOURCES.md | grep -E '^\\| *S(776|825) ' | cut -c1-120"
run "git -C $L log --oneline -S '| S777 ' -- corpus/SOURCES.md | wc -l"
run "tail -2 $L/reports/round-76/telemetry/census-start.txt; wc -l < $L/reports/round-76/telemetry/census-start.txt; grep -c \$'\\tW04\\t' $L/reports/round-76/telemetry/census-start.txt; grep -c \$'\\tW01\\t' $L/reports/round-76/telemetry/census-start.txt"
run "ls $L/considerthese"
G=$W/assimilation/guard-proof
run "EX='^ {0,3}\\|[[:space:]]*S[0-9]{3,}'; for f in $G/planted-1space-registry.md $G/planted-4space-registry.md $G/col0-registry.md; do echo \"== \$f 0-3sp:\$(grep -cE \"\$EX\" \$f) col0:\$(grep -cE '^\\|[[:space:]]*S[0-9]{3,}' \$f)\"; done"
run "wc -c $G/planted-1space.collisions $G/planted-4space.collisions; cat $G/planted-1space.collisions"
