
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
spots = list(int(input()) for _ in range(N))
# print(spots)
distances = []



def estimate(N, spots):
    q = deque()
    max_d = sum(spots) // 2

    # 0번째부터 N-1번째까지를 시작점으로 최대 거리 계산
    # 최초 계산 시에 이분탐색 갈겨야겠다
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        total = sum(spots[0:mid])
        if total > max_d:
            right = mid - 1
        else:
            left = mid + 1
    end = right
    # print(end)
    # 0 기준으로 거리 최대인 최초 연결리스트 생성
    for i in range(end):
        q.append(spots[i])
    cur_d = sum(q)
    distances.append(cur_d)
    # print(q, sum(q), distances)

    # sum(q)가 max_d보다 작으면 append
    for j in range(N-1):
        if q:
            x = q.popleft()
            cur_d -= x
        # 중간에 절반보다 큰게 있어서 q가 비어버리는 경우
        else:
            q.append(0)
            end += 1
        # 다음 거리를 더한게 max_d보다 작으면
        # print(end+1)
        while cur_d + spots[end % N] <= max_d:
            next_spot = spots[end % N]
            cur_d += next_spot
            q.append(next_spot)
            end += 1
        # print(q)
        distances.append(cur_d)

if N == 2:
    print(min(spots))
else:
    estimate(N,spots)
    print(max(distances))