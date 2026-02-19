'''
전형적인 u-f 문제
1. 친구관계를 먼저 정립
    이때 rank는 친구비
2. set로 만든 다음
3. for문으로 set를 순회하면서 친구비를 검사하자
'''
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y, ans):
    root_x = find(x)
    root_y = find(y)
    # print(root_x, root_y)

    # 같을때 union하면 전체 비용 상승
    if root_x != root_y:
        # 친구비가 더 크면 작은쪽에 union
        if rank[root_y] >= rank[root_x]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


N, M, k = map(int, input().split())
rank = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]
ans = 0
# print(parent, rank)


for _ in range(M):
    v, w = map(int, input().split())
    union(v, w, ans)
    # print(parent)

# 리프 노드들 경로압축 - 이거에서 고생했다..
for j in range(1, N+1):
    parent[j] = find(j)
parent = set(parent)
ans = sum(rank[p] for p in parent)


if ans <= k:
    print(ans)
else:
    print("Oh no")