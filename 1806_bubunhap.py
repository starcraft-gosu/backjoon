import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))
print(lst)

def search(N, S):
    l, r = 0, 0
    ans = 0
    while r <= N:
        print(l, r)
        if ans > S:
            ans -= lst[l]
            l += 1
        elif ans < S:
            if r >= N:
                break
            ans += lst[r]
            r += 1
        else:
            # 0이 있을경우 0 제거
            while lst[l] == 0:
                l += 1
            return r-l

    return 0

print(search(N, S))