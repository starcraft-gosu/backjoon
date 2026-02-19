# 1. 벌통 맨 오른쪽 1번 벌 맨 왼쪽
#     벌1의 꿀 = sum[2~N] = (전체합) - honey[1]
#     벌2의 꿀 = sum[i+1~N] = (전체합) - sum[1~i]
# 2. 벌통 맨 왼쪽 1번 벌 맨 오른쪽
#     벌1의 꿀 = sum[1~N-1] = (전체합) - honey[N]
#     벌2의 꿀 = sum[1~i-1] = sum[1~i] - honey[i]
# 3. 벌통 가운데 1번 벌 맨 왼쪽
#     총 꿀 = sum[1~i] - honey[1] + sum[i~N] - honey[N]
#           = sum[1~i] + sum[i~N] - honey[1] - honey[N]
#           = (전체합) + honey[i] - honey[1] - honey[N]

import sys
import copy
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

# 누적합
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + honey[i]

total = prefix[n]
answer = 0

# 케이스 1: 벌통 맨 오른쪽
for i in range(2, n):
    bee1 = total - honey[1] - honey[i]  # 벌1(위치1)
    bee2 = total - prefix[i]            # 벌2(위치i)
    answer = max(answer, bee1 + bee2)

# 케이스 2: 벌통 맨 왼쪽
for i in range(2, n):
    bee1 = total - honey[n] - honey[i]  # 벌1(위치n)
    bee2 = prefix[i] - honey[i]          # 벌2(위치i)
    answer = max(answer, bee1 + bee2)

# 케이스 3: 벌통 중간, 벌 양쪽 끝
for i in range(2, n):
    result = total + honey[i] - honey[1] - honey[n]
    answer = max(answer, result)

print(answer)