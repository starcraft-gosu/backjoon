'''
높이 별 안전지대 최대 개수 구하기
cnt만들어 놓고 순회하면서 dfs 끝날때마다 cnt+=1하기
최대높이 먼저 봐놓고 순회할 높이 정하자
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
zone = [list(map(int, input().split())) for _ in range(N)]

# 위쪽부터 시계방향
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 안전영역 탐색 함수
def dfs(h, y, x):
    visited[y][x] = 1
    n = len(visited[y])
    for idx in range(4):
        new_y = y + dy[idx]
        new_x = x + dx[idx]
        # 조건이 기네요...
        if 0 <= new_y < n and 0 <= new_x < n and zone[new_y][new_x] > h and visited[new_y][new_x] == 0:
            visited[new_y][new_x] = 1
            dfs(h, new_y, new_x)



max_h = 0
for i in range(N):
    for j in range(N):
        if zone[i][j] > max_h:
            max_h = zone[i][j]

h = 0
max_cnt = 0

# 높이마다 안전 영역 개수 구하기
while h < max_h:
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # h보다 높고 방문하지 않은 곳에서 출발
            if zone[i][j] > h and not visited[i][j]:
                dfs(h, i, j)
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
    h += 1
print(max_cnt)
