'''
무언가 하나를 변경할때?
n, p
n이 뒤로가면?
    p< x <=n
해당 숫자가 앞으로 가면?
    n<= x <p
    2345671
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

# 2포인터로 접근 -> 실패
answer = 0
l, r = 0, n-1
while l <= r:
    if arr[l] != l+1:
        arr.remove(l+1)
        arr.insert(l, l+1)
        answer += 1
        print(arr)
    if arr[r] != r+1:
        arr.remove(r + 1)
        arr.insert(r, r + 1)
        answer += 1
        print(arr)
    l += 1
    r -= 1
print(answer)