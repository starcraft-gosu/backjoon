import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
# print(board)

dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = 0
dq = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            cost = board[nx][ny]  # 벽이면 1, 빈칸이면 0

            # 최소 비용으로 갱신
            if dist[x][y] + cost < dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + cost

                # 비용이 작은 칸을 먼저 배치
                if cost == 0:
                    dq.appendleft((nx, ny))  # 앞에 추가
                else:
                    dq.append((nx, ny))  # 뒤에 추가
# print(dist)
# print(m,n)
print(dist[n-1][m-1])