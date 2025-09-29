'''
M개의 구간
최소값 시작 - 안구해도될지도
N-M+1개의 구간으로 직접 1부터 돌아보면될듯
최소값보다 작게 만드는법을 이분탐색 진행 - 최대값이 k보다 작아야된다
이분탐색 활용
1. 정렬돼있어서 순서에 따라 돼야하고
2. FFFFFTTTTTTTT식으로 돼야해
3. 그래서 최대값의 최소값을 이분탐색의 객체로 삼고
4. 각 탐색 시에 TF를 판별.
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

print(array)

# TF 판별함수
# 하나씩 옆으로 가면서 k를 만족시키지 못하는 값이 나오면 다음 구간으로
def is_true(mid, N, M):
    min_cur = max_cur = array[0]

    for x in array[1:]:
        max_cur = max(max_cur, x)
        min_cur = min(min_cur, x)
        score = max_cur - min_cur
        if score > mid:
            min_cur = max_cur = x
            cnt += 1

    return cnt <= M


print(is_true(4, N, M))

left = 0
right = max(array)

while left < right: # 종료 조건 : left가 right보다 크다
    mid = (left + right) // 2 # mid = left + 1/ mid = right
    # print(mid, right)
    if is_true(mid, N, M):
        # print(1)
        right = mid
    else:
        # print(2)
        left = mid + 1

# print(left)

print(is_true(4, N, M))