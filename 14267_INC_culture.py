'''
인풋을 sort하고
관계가 안정해지는건 마지막 뿌리 밖에 없어
해당 숫자에 가지를 쥰내 만들어

6 4
-1 1 1 1 1 1
100000 1
99999 1
99998 1
2 1
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
members = sorted(list(map(int, input().split())))
sangsas = [0] * 100000
chingchan = [0] * n

# 직원 별 자리 인덱스
for idx, member in enumerate(members):
    sangsas[member] = idx - 1
print(sangsas)
print(members)

# 직원 별로 받은 칭찬 누적 ex) [0, 2, 4, 0, 6]
for _ in range(m):
    i, w = map(int, input().split())
    if i not in members:
        chingchan[n-1] += w
    else:
        chingchan[sangsas[i]] += w

# 이전꺼 더하기 ex) [0, 2, 6, 6, 12]
for j in range(1, n):
    chingchan[j] += chingchan[j-1]

for ans in chingchan:
    print(ans, end=' ')
