import sys
input = sys.stdin.readline

n = int(input())
nums = input().split()

# 버블 정렬로 직접 구현
for i in range(n):
    for j in range(n - 1):
        # a+b와 b+a를 비교해서 b+a가 더 크면 swap
        if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

result = ''.join(nums)

# 전부 0이면 0 출력
print(0 if result[0] == '0' else result)