N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]

for medal in medals:
    if medal[0] == K:
        gold, silver, bronze = medal[1], medal[2], medal[3]
        break

rank = 1
for medal in medals:
    if medal[1] > gold:
        rank += 1
    elif medal[1] == gold:
        if medal[2] > silver:
            rank += 1
        elif medal[2] == silver:
            if medal[3] > bronze:
                rank += 1

print(rank)