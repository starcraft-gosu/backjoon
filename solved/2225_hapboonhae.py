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

### 2. dp로 풀기
# 2차원 배열 1로 초기화
N, K = map(int, input().split())

# DP 테이블 초기화
MOD = 1000000000
dp = [[0] * (N + 1) for _ in range(K + 1)]

# dp[i][0]은 1로 초기화 (모든 i에 대해 0을 만드는 방법은 한 가지)
for i in range(K + 1):
    dp[i][0] = 1

# 점화식을 이용해 DP 테이블 채우기
for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

# 결과 출력
print(dp[K][N])