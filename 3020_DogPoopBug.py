'''
일단 냅다 그냥 해보기
'''

import sys
input = sys.stdin.readline
#
# N, H = map(int, input().split())
# conflicts = [0] * H
# odd, even = [], []
# for i in range(1, N+1):
#     x = int(input())
#     if i % 2 == 1:
#         odd.append(x)
#     else:
#         even.append(x)
# for num in odd:
#     for j in range(num):
#         conflicts[j] += 1
#
# for num in even:
#     for k in range(-1, -(num+1), -1):
#         conflicts[k] += 1
#
# # print(conflicts)
# cnt = 0
# min_c = min(conflicts)
# for c in conflicts:
#     if c == min_c:
#         cnt += 1
# print(min_c, cnt)


'''
2번째 순회 한번에 높이를 다 만들 수 없나? - 아마 불가리스
높이별 이분탐색
'''
#
# import sys
# input = sys.stdin.readline
#
# N, H = map(int, input().split())
#
# conflicts = [0] * H
# odd = []
# even = []
#
# for i in range(1, N+1):
#     x = int(input())
#     if i % 2 == 1:
#         odd.append(x)
#     else:
#         even.append(x)
#
# odd.sort()
# even.sort()
#
# down_sum = [0] * H # 홀수에서 k보다 큰거 시작점(1~k 장애물)
# up_sum = [0] * H # 짝수에서 H-k+1 작은거 시작점(H-k+1~H-1 장애물)
# half = N // 2
#
# min_hits = float('inf')
# cnt = 0
#
# # 이분탐색 함수
# def bin_search(lst, target):
#     left, right = 0, len(lst)
#
#     while left < right:
#         mid = (left+right) // 2
#         if lst[mid] < target:
#             left = mid+1
#         else:
#             right = mid
#
#     return left
#
#
# # 높이별 장애물 개수 탐색
# for k in range(1, H+1):
#     # 아래쪽 장애물 충돌 횟수
#     down_hits = half - bin_search(odd, k)
#     # 위쪽 장애물 충돌 횟수
#     up_hits = half - bin_search(even, H-k+1)
#
#     total_hits = up_hits+down_hits
#     if total_hits < min_hits:
#         min_hits = total_hits
#         cnt = 1
#     elif total_hits == min_hits:
#         cnt += 1
#
# print(min_hits, cnt)

##################3
#3
N, H = map(int, input().split())

odd = [0] * (H+1)
even = [0] * (H+1)

for i in range(N):
    height = int(input())
    if i % 2 == 0:
        even[height] += 1
    else:
        odd[height] += 1

# 여기가 핵심!!!!!!!!!!1
for j in range(H-1, 0, -1):
    odd[j] += odd[j+1]
    even[j] += even[j+1]

min_obstacles = N  # 최대는 N (모든 장애물에 부딪히는 경우)
count = 0

for i in range(1, H + 1):
    # i번째 높이로 날면, 석순은 높이 i 이상인 것에 부딪히고
    # 종유석은 높이 H - i + 1 이상인 것에 부딪힘
    obstacles = odd[i] + even[H - i + 1]
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        count = 1
    elif obstacles == min_obstacles:
        count += 1

print(min_obstacles, count)