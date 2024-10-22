N, M = map(int, input().split())
trains = [[0] * 20 for _ in range(N)]
# print(trains)
for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        trains[command[1]-1][command[2]-1] = 1

    elif command[0] == 2:
        trains[command[1] - 1][command[2] - 1] = 0

    elif command[0] == 3:
        trains[command[1] - 1].insert(0, 0)
        trains[command[1] - 1].pop()
    else:                                           # 맨앞 4일때
        trains[command[1] - 1].append(0)
        trains[command[1] - 1].pop(0)

answer = set(tuple(train) for train in trains)
print(len(answer))