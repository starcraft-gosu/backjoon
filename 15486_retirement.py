'''
배열에 그날의 최대값 저장
순회할때가되면 max해서 최대값
'''
N = int(input())
consulting = [0] + list(tuple(map(int, input().split())) for _ in range(N))

# 일자별 최대값 저장할 리스트
dp = [[0] for _ in range(N+1)]

for i in range(1, N+1):
    # dp[i-1]에 저장된 값들 중 최대값으로 dp[i-1] 초기화
    dp[i-1] = max(dp[i-1])

    # i번째 날의 t와 p
    t_i = consulting[i][0]
    p_i = consulting[i][1]

    # 상담 날짜
    date = i + t_i - 1
    # 상담 날짜가 N+1 이하면 상담 금액을 dp[date]에 저장
    if date < N+1:
        dp[date].append(dp[i-1] + p_i)

    # dp[i] 값들이 전날 최대값보다 작은경우 전날 최대값 가져오기
    if max(dp[i]) <= dp[i-1]:
        dp[i].append(dp[i-1])
print(max(dp[-1]))