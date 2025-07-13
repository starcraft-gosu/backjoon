from collections import deque

N, M, V = map(int, input().split())
vertexes = list(tuple(map(int, input().split())) for _ in range(M))
# print(vertexes)

def dfs(V):
    stack = [V]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            print(current, end=' ')
            # 방문할 수 있는 정점들을 정렬하기 위한 리스트 생성
            nodes = []

            # 방문 가능한 노드 리스트 생성
            for vertex in vertexes:
                if vertex[0] == current:
                    nodes.append(vertex[1])
                elif vertex[1] == current:
                    nodes.append((vertex[0]))

            # 정렬된 노드들을 기존 스택에 추가
            nodes.sort(reverse=True)
            stack = stack + nodes


def bfs(V):
    q = deque()
    q.append(V)
    visited = []
    while q:
        current = q.popleft()
        if current not in visited:
            visited.append(current)
            print(current, end=' ')
            # 방문할 수 있는 정점들을 정렬하기 위한 리스트 생성
            nodes = deque()

            # 방문 가능한 노드 리스트 생성
            for vertex in vertexes:
                if vertex[0] == current:
                    nodes.append(vertex[1])
                elif vertex[1] == current:
                    nodes.append(vertex[0])

            # 정렬된 노드들을 기존 큐에 추가
            nodes = deque(sorted(nodes))
            q = q + nodes


dfs(V)
print()
bfs(V)