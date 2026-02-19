import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    # if rank[x] < rank[y]:
    #     parent[x] = root_y
    # elif rank[x] >rank[y]:
    #     parent[y] = root_x
    # else:
    #     parent[y] = root_x
    #     rank[x] += 1


n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
rank = [0] * (n+1)

answer = 0
nets = []
for _ in range(m):
    net = tuple(map(int, input().split()))
    nets.append(net)
nets.sort(key = lambda x: x[2])

for net in nets:
    x, y, c = net
    if find(parent, x) != find(parent, y):
        union(parent, rank, x, y)
        answer += c
print(answer)

#
# netss = defaultdict(int)
#
#
# if n < 3:
#     print(sum(net[2] for net in nets))
# else:
#     answer = sum(net[2] for net in nets)
#     x, y, z = 1, 2, 3
#     for i in range(n-2):
#
#         '''
#         3 수를 가진 3개의 넷이 잇으면 하나를 제외한다.
#         '''
#         # answer -=
#         pass
