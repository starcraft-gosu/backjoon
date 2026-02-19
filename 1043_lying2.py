import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

N, M = map(int, input().split())
_m, *truth = list(map(int, input().split()))

parties = []
for _ in range(M):
    _, *party = list(map(int, input().split()))
    parties.append(party)

parent = [i for i in range(N+1)]
rank = [0] * (N+1)

# 같은 파티에 참석한 사람들 union
for party in parties:
    for i in range(len(party) - 1):
        union(parent, rank, party[i], party[i+1])

# 진실을 아는 사람들 루트노드를 set에 저장?
truth_roots = set()
for person in truth:
    truth_roots.add(find(parent, person))

answer = 0
for party in parties:
    # 파티에서 임의의 인원 0번 인덱스를 확인
    party_root = find(parent, party[0])
    # 파티에 한명이라도 진실을 아는 사람이 있으면 parent가 root노드가 됐을것
    if party_root not in truth_roots:
        answer += 1

print(answer)