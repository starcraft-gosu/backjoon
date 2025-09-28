#
# N = int(input())
# p_lst = []
# n_lst = []
# # 양수 음수 리스트 생성
# for num in map(int, input().split()):       # gpt 짱!
#     (p_lst if num > 0 else n_lst).append(num)
#
# p_lst.sort()
# n_lst.sort()
#
# print(n_lst, p_lst)
#
# def solution():
#     left = 0
#     # 특성값 초기화
#     trait = 1000000000
#     answer = []
#
#     if len(p_lst) == 0:
#         answer = [n_lst[-2], n_lst[-1]]
#     elif len(n_lst) == 0:
#         answer = [p_lst[0], p_lst[1]]
#
#     # 양수가 음수보다 적으면 양수를 기준으로 이진탐색
#     elif len(p_lst) < len(n_lst):
#         right = len(p_lst) -1
#         for n in n_lst:
#             number = bin_search(trait, n, left, right)
#             if n+number == 0:
#                 return n, number
#             elif abs(n+number) < trait:
#                 trait = abs(n+number)
#                 answer = [n, number]
#         else:
#             return answer
#
#     # 음수가 양수보다 적거나 같으면 음수를 기준으로 이진탐색
#     else:
#         right = len(n_lst) -1
#         lst = n_lst
#         for p in p_lst:
#             result, number = bin_search(trait, p, left, right)
#             if result == 0:
#                 return number, p
#             elif abs(result) < trait:
#                 trait = abs(result)
#                 answer = [number, p]
#         else:
#             return answer
#
#
#
#
# def bin_search(target, num, left, right):
#     middle = (left + right) // 2
#     # 용액 값이 0이거나 left right 차이가 1이면 종료
#     result = target[middle] + num
#     if result == 0:
#         return result, target[middle]
#
#     if result < target:
#
#     return None
#     pass


'''
투포인터

'''

N = int(input())
liquids = sorted(list(map(int, input().split())))

positive = []
negative = []
zeros = []

# 0을 어케 처리해줄까
# 0이 두개면 겜끝, 0이 한개면 따로 담아서 최소값 저장
for liquid in liquids:
    if liquid < 0:
        negative.append(liquid)
    elif liquid > 0:
        positive.append(liquid)
    else:
        zeros.append(liquid)

print(liquids)


def minimum():
    # 최소값 양수 or 음수 최소값으로
    mini = min(negative[-1]+negative[-2], positive[0]+positive[1])
    if len(zeros) == 1:
        mini = min(negative[-1], positive[0])

def bin_search(a, b, minimum):
    for l in a:

        pass
    pass # return 정답

def mix():
    # 0이 두개면 바로 끝!
    if len(zeros) >= 2:
        return (0,0)
    minimum = minimum()
    # a를 기준으로 순회돌기
    if len(positive) <= len(negative):
        a = positive
        b = negative
    else:
        a = negative
        b = positive
    for l in a:
        result = bin_search(l, b)
        total = sum(result)
        if minimum > total:
            minimum = total
    return result