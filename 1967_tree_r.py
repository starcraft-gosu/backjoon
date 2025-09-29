'''
모앙으로 접근 x
루트 노드 별로 접근해야하나?
최대 log2^10000 = 13
루트 별에서 오른쯕으로 큰거만 고르고 왼쪽으로 큰거만 골라서 ㄱㄱ 하면 되지!

'''
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# n = int(input())
# graph = [[] for _ in range(n + 1)]
#
# # 연결리스트 생성
# for _ in range(n - 1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))
#
# print(graph)
#
# def dfs(start, dist):
#     for nxt, w in graph[start]:
#         # 아직 방문하지 않은 노드이면
#         if distance[nxt] == -1:
#             distance[nxt] = dist + w
#             dfs(nxt, dist + w)
#
# # 1단계: 루트에서 가장 먼 노드 찾기
# distance = [-1] * (n + 1)
# distance[1] = 0
# dfs(1, 0)
# far_node = distance.index(max(distance))
#
# print(far_node)
#
# # 2단계: 그 노드에서 가장 먼 거리 구하기
# distance = [-1] * (n + 1)
# distance[far_node] = 0
# dfs(far_node, 0)
#
# print(max(distance))

# def dfs(start, dist):
#     stack = [(start, dist)]
#     while stack:
#         cur, total = stack.pop()
#         for nxt, w in graph[cur]:
#             # 아직 방문하지 않은 노드이면
#             if distance[nxt] == -1:
#                 stack.append((nxt, dist+w))
#                 distance[nxt] = total + w




    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dfs(start):
        distance = [-1] * (n + 1)
        distance[start] = 0
        stack = [(start, 0)]  # (현재노드, 현재거리)

        while stack:
            cur, dist = stack.pop()
            for nxt, w in graph[cur]:
                if distance[nxt] == -1:
                    distance[nxt] = dist + w
                    stack.append((nxt, dist + w))
        return distance

    # 1단계: 임의의 노드(1)에서 가장 먼 노드 찾기
    first_far = dfs(1)
    far_node = first_far.index(max(first_far))

    # 2단계: far_node에서 가장 먼 거리 구하기
    second_far = dfs(far_node)
    print(max(second_far))