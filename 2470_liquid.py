'''
N은 10만 이하
-1,000,000,000~1,000,000,000까지의 값

두개를 쓰까서 0에 가장 가까운거 -> abs()값이 작아져야한다
이분탐색인게 양수 or 음수 최소값 두 개 합이랑 0 사이라서 그런건가?
0이면 탐색 멈추고 해당 경우
출력은 오름차순


1. 산성 염기성 정렬
2. 산성 염기성 가장 작은애 두개 합쳐서 걔네보다 작은애들만
3. 그래도 5만 한바꾸 다 돌아야하는데?
4. 5만번마다 이진탐색을 다 돌려주면? 이거다!

예외
1. 산성 염기성 다 주어져도 산성+산성이 더 작을수 있음
2. 산성이나 염기성만 주어지는 경우
'''

N = int(input())
p_lst = []
n_lst = []
# 양수 음수 리스트 생성
for num in map(int, input().split()):       # gpt 짱!
    (p_lst if num > 0 else n_lst).append(num)

p_lst.sort()
n_lst.sort()

print(n_lst, p_lst)

def solution():
    left = 0
    # 특성값 초기화
    trait = 1000000000
    answer = []

    if len(p_lst) == 0:
        answer = [n_lst[-2], n_lst[-1]]
    elif len(n_lst) == 0:
        answer = [p_lst[0], p_lst[1]]

    # 양수가 음수보다 적으면 양수를 기준으로 이진탐색
    elif len(p_lst) < len(n_lst):
        right = len(p_lst) -1
        for n in n_lst:
            number = bin_search(trait, n, left, right)
            if n+number == 0:
                return n, number
            elif abs(n+number) < trait:
                trait = abs(n+number)
                answer = [n, number]
        else:
            return answer

    # 음수가 양수보다 적거나 같으면 음수를 기준으로 이진탐색
    else:
        right = len(n_lst) -1
        lst = n_lst
        for p in p_lst:
            result, number = bin_search(trait, p, left, right)
            if result == 0:
                return number, p
            elif abs(result) < trait:
                trait = abs(result)
                answer = [number, p]
        else:
            return answer




def bin_search(target, num, left, right):
    middle = (left + right) // 2
    # 용액 값이 0이거나 left right 차이가 1이면 종료
    result = target[middle] + num
    if result == 0:
        return result, target[middle]

    if result < target:

    return None
    pass


