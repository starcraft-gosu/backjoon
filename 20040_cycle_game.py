# '''
# 무방향 그래프.
# 간선의 양 점 중
# 한 점만 parent에 있으면 union해줌
# 두 점 다 parent에 있을때 종료
# 간선 개수 500k
# 매번
# '''
import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        # 경로단축!!
        parent[x] = find(parent, parent[x])
        return parent[x]
    else:
        return x

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:   # 두개가 같으면 둘중 한놈으로 통일하고 rank 상승
        parent[root_y] = root_x
        rank[root_x] += 1


n, m = map(int, input().split())
lines = []
for _ in range(m):
    line = tuple(map(int, input().split()))
    lines.append(line)
# print(lines)

parent = [n for n in range(n)]
rank = [0 for i in range(n)]
# print(parent)

cnt = 0
for line in lines:
    cnt += 1
    a, b = line[0], line[1]
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        print(cnt)
        break
    union(parent, rank, root_a, root_b)
else:
    print(0)