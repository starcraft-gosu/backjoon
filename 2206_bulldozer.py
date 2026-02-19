import sys
from collections import deque
input = sys.stdin.readline

def search():
    '''
    1. 갈수 잇는놈들을 다 때려박는다
    2. dfs로 다 때려박아주겟으
    3. 좌표의 dist 비교해서 작으면 업뎃해야하는데...
        dist를 두개놓자 뚫을수잇을때랑 없을때
    4. True일때 board 값이 0이면 그대로 1이면 False로
    5. False일때는 1인놈 X
    '''
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]
    stack = [(0, 0, 1)]

    while stack:
        x, y, bomb = stack.pop()
        # 더 못뚫을때
        if bomb - board[y][x] < 0:
            continue
        elif bomb - board[y][x] == 0:
            # 현재 거리가 dist보다 짧을때
            if <dist[y][x]:
                pass

        # 다음 좌표 추가
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if bomb:
                    pass
                else:
                    pass

                pass
            pass

    pass
'''
출발도착도 포함
벽은 하나만 부수기 가능
저번처럼 작은 경우로 갱신하는 방법을써볼까?
갱신할때는 부술수잇는지 없는지도 판별해야겟다
못가는거 판별은?
일단은 while or for문 다 돌고 n,m이 inf일때??
'''
m, n = map(int, input().split())
board = [input().strip() for _ in range(m)] # 여기는 string 1차원 배열

dist = [[[float('inf'), float('inf')]] * n for _ in range(m)]   # 여기만 2차원 배열
print(board, dist)




