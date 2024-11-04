'''
1. 가장 왼쪽 최대값
2. 직전 애보다 작은 애들 append
3. 최대값보다 큰애들 나오면 중단
4. 적당히 큰애 나오면 앞에 애들 쳐내
5. while문으로 돌려잇
'''
import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
arr = list(map(int, input().split()))
# print(N, arr)

idx = 0
bundle = []
while idx < N:          # idx가 N보다 작을때
    left = arr[idx]
    part = [left]       # 부분집합 한덩이
    idx += 1
    while idx < N and left > arr[idx]:              # 부분집합 만드는 while/  현재 최대값보다 더 큰 수가 나올때 중단
        while arr[idx] > part[-1]:                   # 맨마지막 애보다 큰애면
            part.pop()
        part.append(arr[idx])
        if arr[idx] == 1:                           # 1이 등장했을땐 여기서 끝내는게 나은지 뒤에껄 붙이는게 나은지 비교해봐야함
            break
        idx += 1
    # print(part)
    bundle.append(len(part))


print(N-max(bundle))
