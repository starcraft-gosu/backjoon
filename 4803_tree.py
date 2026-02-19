'''
테케가 여러개
0. 각 트리를 root로 묶고
1. 사이클인지 아닌지 확인해야하고
2. root 개수를 취하면 완료
'''

import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, cycle, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    # 더 작은 root를 기준으로 union
    if root_x < root_y:
        parent[root_y] = root_x
    elif root_x > root_y:
        parent[root_x] = root_y
    else:   # root_x == root_y는 사이클
        cycle.append(root_x)


# 한 테케를 실행하는 함수
def tc(n, m):
    parent = [i for i in range(n + 1)]
    cycle = []
    for _ in range(m):
        a, b = map(int, input().split())
        union(parent, cycle, a, b)
    parent, cycle = set(parent), set(cycle)
    # print(parent)

    # 그래프 중 사이클 색출
    for i in cycle:
        parent.remove(i)

    # parent = {0, @, @, @...}
    return len(parent) - 1

cnt = 0
while True:
    cnt += 1
    n, m = map(int, input().split())
    # print(n,m)
    if (n, m) == (0, 0):
        break
    elif m == 0:
        print(f"Case {cnt}: A forest of {n} trees.")
        continue

    answer = tc(n, m)
    if answer == 0:
        print(f"Case {cnt}: No trees.")
    elif answer == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {answer} trees.")