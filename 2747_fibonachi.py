# 1. memoization
num = int(input())
dp = [0]*(num+1)
def fibo(num):
    dp[0] = 0
    dp[1] = 1
    if num <= 2:
        return 1
    else:
        for n in range(2, num+1):
            dp[n] = dp[n-1] + dp[n-2]

        return dp[num]
print(fibo(num))


# 2. Bottom-up
def bottom_up(n):
    first = 1
    sec = 1

    if n <= 2:
        return sec
    else:
        for _ in range(n-2):
            next_num = first+sec
            first = sec
            sec = next_num
        return next_num

print(bottom_up(num))