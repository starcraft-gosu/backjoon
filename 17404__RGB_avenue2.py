'''
dp[i][R] = cost[i][R] + min(dp[i-1][G], dp[i-1][B])
dp[i][G] = cost[i][G] + min(dp[i-1][R], dp[i-1][B])
dp[i][B] = cost[i][B] + min(dp[i-1][R], dp[i-1][G])
첫집 색 정해놓고
마지막 색은 첫집 색과 다르게
'''

N = int(input())

cost = list(list(map(int, input().split())) for _ in range(N))

dp = [[0]*3 for _ in range(N)]

def rgb(n, first):
    if first == 0:
        dp[0] = [cost[0][0], cost[0][0], cost[0][0]]
    elif first == 1:
        dp[1] = [cost[0][1], cost[0][1], cost[0][1]]
    else:
        dp[2] = [cost[0][2], cost[0][2], cost[0][2]]
    for i in range(1, N-1):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][1], dp[i-1][0])
    return dp[n-1]

r = rgb(N, cost[0][0])
g = rgb(N, cost[0][1])
b = rgb(N, cost[0][2])


    # 마지막 집이 처음집과 달라야함
    # 맨처음껄 어케 아냐...
    # 마지막꺼는 처음과 색깔이 다르고 마지막과 색깔이 달라야함

# def rgb1(n):
#     if n == 0:
#         return
#     rgb1[n][0] = cost[n][0] + min(rgb1[n - 1][1], rgb1[n - 1][2])
#     rgb1[n][1] = cost[n][1] + min(rgb1[n - 1][0], rgb1[n - 1][2])
#     rgb1[n][2] = cost[n][2] + min(rgb1[n - 1][1], rgb1[n - 1][0])

    pass