# 가로세로대각선 0 다 잇으면 삥고
# 빙고가 되는 최소 수는 12
# index 메소드로 못푸나?
# 일렬로 놓으면 5의 배수마다&5씩마다&5 9 13 17 21&1 7 13 19 25 확인

bingo = []
pick = []
for _ in range(5):
    bingo.extend(map(int, input().split()))
for _ in range(5):
    pick.extend(map(int, input().split()))
# print(bingo)

for i in range(len(pick)):
    a = bingo.index(pick[i])
    bingo[a] = 0
    # 빙고 검사
    cnt = 0
    while i >= 11:      # 12개부터 빙고 3개 나올수잇음
        for j in range(5):
            # 가로 췤
            if bingo[5*j] or bingo[5*j + 1] or bingo[5*j + 2] or bingo[5*j + 3] or bingo[5*j + 4]:
                pass
            else:
                 cnt += 1
            # 세로 췤
            for k in range(5):
                if bingo[5*k + j]:
                    break
            else:
                cnt += 1
        # 대각 췤
        for n in range(1, 6):
            if bingo[4 * n]:
                break
        else:
            cnt += 1
        # 대각 췤22
        for m in range(5):
            if bingo[6 * m]:
                break
        else:
            cnt += 1

        break

    if cnt >= 3:
        print(i+1)
        break
