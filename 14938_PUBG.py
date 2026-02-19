import sys
input = sys.stdin.readline

def farming(n):

    pass

n, m, r = map(int, (input().split()))
items = list(map(int, input().split()))
spot = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(r):
    x, y, d = map(int, input().split())
    spot[x][y], spot[y][x] = d, d
    print(spot[i+1])
print(spot)
answer = 0

'''
1. 무식하게 모든 지역을 다 찍어본다 (ㄱㄴ할듯?)
2. 인접 지역으로 옮기며 바뀌는 부분만 갈아낀다
'''

