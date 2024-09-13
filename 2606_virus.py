def make(n):
    p = []
    r = [0] * n
    for i in range(n):
        p.append(p)
    return p, r

def find_p(x):
    if parents[x] == x:
        return x
    return find_p(parents[x])
    pass

def union(y, z):
    if parents[y] == parents[z]:

    pass


N = int(input())
E = int(input())

parents, ranks = make(N)
