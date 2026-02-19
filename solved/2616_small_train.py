'''
클로드대로 해보면
1. 누적합 계산
2. 누적합으로 칸별 계산
3. dp 스따뚜 1, 2, 3번 기차별로 만들어서
4. 다음칸의 결과 = 이전결과 or 이전 기차의 결과 + 현재 기차의 칸
'''
import sys
input = sys.stdin.readline

N = int(input())
train = [0] + list(map(int, input().split()))
tr = int(input())

segment = [0] * (N+1)
prefix = [0] * (N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + train[i]
for j in range(tr, N+1):
    segment[j] = prefix[j] - prefix[j-tr]

dp = [[0] * (N+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-tr] + segment[j])
print(dp[3][N])