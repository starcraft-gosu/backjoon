import sys
# from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a, b, c, d = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())



cd = dict()
for i in range(n):
    for j in range(n):
        cd_sum = c[i] + d[j]
        cd[cd_sum] = cd.get(cd_sum, 0) + 1

answer = 0

for k in range(n):
    for l in range(n):
        ab_sum = a[k] + b[l]
        result = cd.get(-ab_sum, 0)
        answer += result
print(answer)