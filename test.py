import sys

def fibonacci_top_down(n):
    if memo[n] > 0:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return memo[n]
    else:
        memo[n] = fibonacci_top_down(n-1) + fibonacci_top_down(n-2)
        return memo[n]

if __name__ == '__main__':
    memo = [0 for i in range (100)]
    n = int(sys.stdin.readline())
    print(fibonacci_top_down(n))