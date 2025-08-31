
import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
bo1mul_map = list(input().strip() for _ in range(H))


# print(bo1mul_map, visited)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(r, c, H, W): # 해당 좌표와 가로세로
    stack = []
    visited = list([0] * W for _ in range(H))
    stack.append((r, c, 0)) # 0은 cnt가 될놈
    H, W = len(bo1mul_map), len(bo1mul_map[0])
    max_cnt = 0
    while stack:
        cur = stack.pop()
        y, x, cnt = cur
        max_cnt = max(max_cnt, cnt)
        print(cur)
        # 시계방향 델타 탐색
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            # 조건에 맞으면 stack에 넣고 visited 처리
            if 0 <= ny < H and 0 <= nx < W and bo1mul_map[ny][nx] == 'L' and visited[ny][nx] != 1:
                # print(ny, nx)
                stack.append((ny, nx, cnt+1))
                visited[ny][nx] = 1

                # 원래 자리는 빼야하므로 여기서 cnt를 더해줌
    return max_cnt

# 보(물)지(도)를 하나씩 순회하며 bfs 갈기는 모습
ans = 0
result = 0
for i in range(H):
    for j in range(W):
        if bo1mul_map[i][j] == 'L':
            result = bfs(i, j, H, W)

        ans = max(result, ans)

print(ans)


