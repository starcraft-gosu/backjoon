'''
이게 왜 이분탐색..?
mid를 키워나가는 방식으로 해보라는데...
'''

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
print(houses)

# 다음집 - 마지막 집이 distance보다 멀면 +1
def can_install(N, distance):
    count = 1
    last = houses[0]
    for i in range(N):
        if houses[i] - last >= distance:
            count += 1
    if 
    pass