'''
1. 사이클
2. 사이클에 합류하는 애들
3. 벽 밖으로 이탈하는애들
"사이클"을 set으로 볼수잇겟군!

벽 이탈 처리는 어떢하지..
암튼 사이클이랑 벽이탈 이 두개로 ㄱㄱ
풀이
0. for 돌면서 탐색
1. cycle을 1, 2,로 만들어 root화
2.

'''

import sys
input = sys.stdin.readline

# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         parent[x] = find(x) # 경로 최적화
#         return parent[x]
#
# def union(x, y):
#     root_x = find(x)
#     root_y = find(y)
#
#     if rank[root_x] > rank[root_y]:
#         parent[root_y] = root_x
#     elif rank[root_x] < rank[root_y]:
#         parent[root_x] = root_y
#     else:
#         parent[root_y] = root_x
#         rank[root_x] += 1

def search(r, c, cnt):
    first = (r, c)
    q = [(r, c)]

    while q:
        y, x = q[-1]
        if visited[y][x] == 0:
            visited[y][x] = 1
            if my_map[y][x] == 'U':
                if y == 0:
                    return cnt + 1  # 사이클 특정할수 있는 무언가
                ny, nx = y - 1, x
            elif my_map[y][x] == 'D':
                if y == N-1:
                    return cnt + 1  # 사이클 특정할수 있는 무언가
                ny, nx = y + 1, x
            elif my_map[y][x] == 'L':
                if x == 0:
                    return cnt + 1  # 사이클 특정할수 있는 무언가
                ny, nx = y, x - 1
            else:
                if x == M-1:
                    return cnt + 1  # 사이클 특정할수 있는 무언가
                ny, nx = y, x + 1
            q.append((ny, nx))
            print(y, x, q[1:])

        elif visited[y][x] == 1:    # 기존의 사이클인지 원래 사이클인지 판별
            # print('yes')
            if (x,y) in q[1:]:
                print(q[1:], (r,c))
                cnt += 1
            return cnt



N, M = map(int, input().split())
my_map = []

for _ in range(N):
    row = input().strip()
    my_map.append(row)

visited = [[0]*M for _ in range(N)]

answer = 0
for y in range(N):
    for x in range(M):
        # if visited[y][x] == 0:
        answer = search(y, x, answer)
        print(answer)

print(answer)


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

visited = [[0]*M for _ in range(N)]  # 0: 미방문, 1: 방문 중, 2: 방문 완료
answer = 0

def dfs(y, x):
    global answer
    visited[y][x] = 1  # 방문 중

    if grid[y][x] == 'U':
        ny, nx = y - 1, x
    elif grid[y][x] == 'D':
        ny, nx = y + 1, x
    elif grid[y][x] == 'L':
        ny, nx = y, x - 1
    else:
        ny, nx = y, x + 1

    if visited[ny][nx] == 0:
        dfs(ny, nx)
    elif visited[ny][nx] == 1:
        # 방문 중인 노드에 다시 닿았다면 사이클 형성
        answer += 1

    visited[y][x] = 2  # 방문 완료

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)

print(answer)