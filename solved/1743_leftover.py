from collections import deque
import sys
sys.setrecursionlimit(10500)
# sys.stdin = open('input.txt', 'r')
'''
음식물이 붙어잇는 칸이라~ bfs로 gogoringo
1인 칸 발견시 bfs 시작
재귀돌려서 붙어잇는거 cnt 드개재
visited 안 찍고 0으로 바꿔줘도 될듯
bfs는~ 큐 만들어서 델타탐색으로 집어넣고 popleft
'''
def bfs(r, c, cnt):
    for i in range(len(dxy)):
        nx, ny = c + dxy[i][0], r + dxy[i][1]
        if 0 <= ny < N and 0 <= nx < M and aisle[ny][nx]:
            queue.append((ny, nx))
            aisle[ny][nx] = 0
    if queue:
        nr, nc = queue.popleft()
        return bfs(nr, nc, cnt+1)
    else:
        return cnt

dxy = [(-1, 0),(0, -1), (1, 0), (0, 1)]
queue = deque()

N, M, K = map(int, input().split())
aisle = [[0]*M for _ in range(N)]
result = []
# print(aisle)
for _ in range(K):
    r, c = map(int, input().split())
    aisle[r-1][c-1] = 1

# print(aisle)

for i in range(N):
    for j in range(M):
        if aisle[i][j]:
            aisle[i][j] = 0
            result.append(bfs(i, j, 1))

print(max(result))
