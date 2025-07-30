import sys
input = sys.stdin.readline
### 1. 중복조합으로 풀기
'''
(N+K-1)!/N!(K-1)!
팩토리얼 구현만 하면 끝!
'''
N, K = map(int, input().split())
numerator = 1   # 분자
denominator = 1 # 분모

for i in range(1, N+K):
    numerator *= i

for n in range(1, N+1):
    denominator *= n
for k in range(1, K):
    denominator *= k

ans = (numerator // denominator)
print(ans % 1000000000)