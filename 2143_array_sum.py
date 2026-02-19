'''
원소 개수별로 부배열 합 만들어
카운터로 집어넣어
개수 세
'''
import sys
# from collections import defaultdict
input = sys.stdin.readline

def counter(n, arr):
    total = 0
    cnt = dict()
    for i in range(n):  # 0~999
        for j in range(n - i):  # 개수가 i+1개기 때문에 인덱스 관리 필요
            total = sum(arr[j:j + i + 1])
            # print(total)
            cur = cnt.get(total, 0)
            cnt[total] = cur + 1
    return cnt

t = int(input())

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

answer = 0

cnt_a = counter(n, a)
cnt_b = counter(m, b)
# print(cnt_a, cnt_a.keys())
# print(cnt_b)

for x in cnt_a.keys():
    answer += cnt_a.get(x) * cnt_b.get(t-x, 0)
print(answer)

# # cnt_a = defaultdict(int)
# # cnt_b = defaultdict(int)
# # a에 0~n개까지의 합
# for i in range(n):  # 0~999
#     for j in range(n-i):    # 개수가 i+1개기 때문에 인덱스 관리 필요
#         sum_a = sum(a[j:j+i+1])
#         print(sum_a)
#         cnt_a[sum_a] +=1
# print(cnt_a)



