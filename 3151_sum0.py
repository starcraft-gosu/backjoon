import sys
input = sys.stdin.readline


n = int(input())
coding = list(map(int, input().split()))

# counter를 구현하자
count = dict()
for i in range(n-1):
    for j in range(i+1, n):
        score = coding[i]+coding[j]

        a = count.get(score, 0)
        count[score] = a + 1

print(count)

ans = 0
# 앞서 선택한 두놈 빼야지
for i in range(n): # 8개를 봐야하는데 걍 전체 10개를 다돌려버리기 (a, b, c)
    c = -coding[i]
    ans += count.get(c, 0)

print(ans)