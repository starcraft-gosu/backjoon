from collections import deque
'''
1. 2차원배열로 받아와서
2. for문으로 돌아댕기며 1찾기, visited찍기
3. 1 찾으면 냅다 bfs 갈겻
4. 재귀 값은 차곡차곡 result에
'''
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs(a, b):
    cnt = 0
    que = deque()
    que.append((a, b))
    visited[a][b] = 1
    while que:
        row, col = que.popleft()
        for i in range(len(dxy)):
            nr, nc = row+dxy[i][0], col+dxy[i][1]           # 큐에 넣을 넘
            if 0 <= nr < N and 0 <= nc < N:                 # 인덱스 에러 방지
                if apt[nr][nc] and not visited[nr][nc]:     #
                    que.append((nr, nc))
                visited[nr][nc] = 1
        cnt += 1
    return cnt




N = int(input())
apt = [list(map(int, input())) for _ in range(N)]
result = []
visited = [[0]*N for _ in range(N)]
# print(visited)
for r in range(N):
    for c in range(N):
        if not visited[r][c] and apt[r][c]:
            result.append(bfs(r, c))

result.sort()
print(len(result))
for j in range(len(result)):
    print(result[j])