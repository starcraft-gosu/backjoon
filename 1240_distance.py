'''
트리 사이 노드 거리 찾는거
N-1개의 줄에 노드랑 거리가 나옴
BFS로 하나하나 찾아보자
0. visited는 필요(한큐에 끝내므로)
1. 입력받은 애들을 2차원 리스트로 관리해보자
2.
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    x, y, d = map(int, input().split())
    tree[y][x] = d
    tree[x][y] = d

def bfs(s, f, N):
    visited = [0] * (N + 1)
    q = deque()
    q.append((s,0))
    # 해당 노드와 연결된 노드 검사
    while q:
        node, d = q.popleft()
        # 종료조건
        if node == f:
            return d
        if visited[node] == 0:
            # visited 1 찍고 노드 추가하고 거리 추가
            visited[node] = 1
            for v in range(N+1): # v가 다음 노드, w가 거리
                if tree[node][v] != 0 and visited[v] == 0:
                    # node 추가
                    new_d = d + tree[node][v]
                    q.append((v, new_d))
for i in range(M):
    s, f = map(int, input().split())
    print(bfs(s,f, N))