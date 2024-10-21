from collections import deque
'''
상어먹이는 bfs with cnt
delta ulrd
bfs 리턴값 cnt
물고기 크기는 2 3 4 5 크기 커질때마다 규격?도 1씩 쑥쑥
'''
dxy = [(0, -1), (-1, 0), (1, 0), (0, 1)]
def bfs(r, c, cnt):
    q = deque()
    q.append()
    q.popleft()