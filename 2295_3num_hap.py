'''
x+y+z = k # xyz 중복 ㄱㄴ
k가 최대가 되도록 한다
이분탐색을 쓰라고..?
k랑 z를 정해놓고 이분탐색?
백만 *log2N = 천만

1. sort
2. 가장 큰 숫자와 근접하는 세수의 합
'''
import sys
input = sys.stdin.readline

def two_pointer(k, z):
    others = U[0] + U[z]
    k_z = U[k] - U[z]

    # 탐색 시작점을 이분탐색으로 최적화하여 찾기
    if others > k_z:
        # 0를 기준으로 r시작점을
        l = 0
        r = bin_search_r(z, U[l], k_z)
    elif others < k_z:
        # r을 기준으로 l시작점을
        r = z
        l = bin_search_l(z, U[r], k_z)
    else:   # 정답일때
        return True
    while l <= r:
        two_sum = U[l] + U[r]
        if two_sum < k_z:
            l += 1
        elif two_sum > k_z:
            r -= 1
        else:
            return True
    return

def bin_search_l(z, mx, k_z):
    l = 0
    r = z
    while l <= r:
        mid = (l+r) // 2
        if U[mid] + mx < k_z:
            l = mid + 1
        elif U[mid] + mx > k_z:
            r = mid - 1
        else:
            return mid
    return r

def bin_search_r(z, mn, k_z):
    l = 0
    r = z
    while l <= r:
        mid = (l+r) // 2
        if U[mid] + mn < k_z:
            l = mid + 1
        elif U[mid] + mn > k_z:
            r = mid - 1
        else:
            return mid
    return l

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()

stop = 0
for k in range(N-1, 0, -1): # 2번째까지
    for z in range(k-1, -1, -1): # 자연수
        if two_pointer(k, z):
            print(U[k])
            stop = 1
            break
    if stop:
        break