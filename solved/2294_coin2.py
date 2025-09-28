import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
coins.sort(reverse=True)
inf = float('inf')

dp = [0]+[inf]*(k)
# print(dp)

'''
동전 하나 올릴때마다 해당 가격에 + 1
dp는 k보다 큰수로 초기화시켜야한다!
'''

for coin in coins:
    for amount in range(coin, k+1):
        dp[amount] = min(dp[amount-coin] + 1, dp[amount])

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])