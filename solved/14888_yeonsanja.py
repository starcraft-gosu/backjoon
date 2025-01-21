# 계산 함수랑 스택 함수 각각 생성

import sys
from itertools import permutations
# from collections import deque
sys.stdin = open('../input.txt', 'r')

N = int(input())
num = list(map(int, input().split()))
arr = list(map(int, input().split()))

# print(num, arr)

lst = []
# 이거 간소화 어케 하지 흐음
for _ in range(arr[0]):
    lst.append('+')
for _ in range(arr[1]):
    lst.append('-')
for _ in range(arr[2]):
    lst.append('*')
for _ in range(arr[3]):
    lst.append('//')
# print(lst)

bundles = set(permutations(lst, N - 1))
# print(bundles)

results = []
for bundle in bundles:
    result = num[0]
    for i in range(len(bundle)):
        c = bundle[i]
        if c == '+':
            result += num[i+1]
        elif c == '-':
            result -= num[i+1]
        elif c == '*':
            result *= num[i+1]
        else:
            if result >= 0:
                result //= num[i+1]
            else:
                result = abs(result)//num[i+1]
    results.append(result)

print(max(results))
print(min(results))








# 연산자 우선순위 고려한 경우
# # 경우 당 계산 드감
# for bundle in bundles:
#     # 계산을 위한 큐 생성
#     stack = deque()
#     stack.append(num[0])
#     # 더하기빼기는 스택에 때려박고
#     for i in range(len(bundle)):
#         c = bundle[i]
#         if c == '+' or c == '-':
#             stack.append(c)
#             stack.append(num[i + 1])
#         else:  # 곱하기 나누기는 계산하고 떄려박고
#             a = stack.pop()
#             if c == '*':
#                 a *= num[i + 1]
#             else:
#                 a //= num[i + 1]
#             stack.append(a)
#     # print(stack)
#     result = stack.popleft()
#     while stack:
#         if stack.popleft() == '+':
#             result += stack.popleft()
#         else:
#             result -= stack.popleft()
#     # print(result)
#     results.append(result)
#
# print(max(results))
# print(min(results))
