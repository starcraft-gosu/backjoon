N = int(input())

# 규칙 따라가는 함수 생성
# n보다 작은 정수 loop돌렷?
# 규칙에 따라 돌리고 count 1추가

def relay(N, n):
    a = [N, n]
    idx = 2
    while a[idx-1] >= 0:
        new = a[idx-2] - a[idx-1]
        if new < 0:
            return idx, a
        else:
            a.append(new)
            idx += 1
    return idx, a

max = 0
lst = []
for i in range(N, 0, -1):
    if max < relay(N, i)[0]:
        max = relay(N, i)[0]
        lst = relay(N, i)[1]

print(max)
print(*lst)

