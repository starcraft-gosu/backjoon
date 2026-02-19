import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
# n 300만, d, k < 3000
# 걍 누적합 때린다음 set하면 되는거아냐?
sushi = [int(input()) for _ in range(n)]
# print(sushi)

# list
eat = deque(sushi[0:k])
ans = 0
for i in range(0, n):
    eat.popleft() # 이 부분이 문제
    eat.append(sushi[(i+k) % n])
    eat_c = set(eat)
    eat_c.add(c)
    ans = max(ans, len(eat_c))
print(ans)
