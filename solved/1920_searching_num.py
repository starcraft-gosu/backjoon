N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

'''
1. 정렬
2. 인덱스를 기준으로 중간값()
3. 중간값과 비교해서 작으면 (left, middle)를 크면 (middle, right)를
4. 반복해서 더이상 나눠지지 않을때까지
'''

def binary_searching(num, left, right):
    # 중간값 찾기
    mid = (left + right) // 2

    ## 더 못 나누는 경우
    if mid == left:
        # 남은 두 값 중 찾던 숫자와 일치하는게 있으면 1, 아님 0
        if num == A[left] or num == A[right]:
            return 1
        else:
            return 0

    ## 찾던 숫자가 중간보다 왼쪽의 경우
    if num < A[mid]:
        left = left
        right = mid
        return binary_searching(num, left, right)
    ## 찾던 숫자가 중간보다 오른쪽의 경우
    elif num > A[mid]:
        left = mid
        right = right
        return binary_searching(num, left, right)
    ## 중간값이 찾던 숫자인 경우
    else:
        return 1

for number in numbers:
    print(binary_searching(number, 0, N-1))