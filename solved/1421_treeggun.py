# while True:

N, C, W = map(int, input().split())
trees = list(int(input()) for _ in range(N))
trees.sort()

length = 1 # 나무 자르는 길이 단위
result = 0
while length <= trees[N-1]: # 1부터 제일 긴 나무 개수까지 반복
    current_result = 0
    for i in range(N):  # 나무마다 파는돈 계산
        price = 0
        price += (trees[i] - trees[i]%length) * W
        cuts = trees[i] // length
        if trees[i] % length == 0:
            cuts -= 1 # 나머지가 없어 나눠 떨어져서 1회 덜 자르는 경우
        price -= cuts * C
        if price <= 0:
            continue
        current_result += price

    if current_result > result: result = current_result
    length += 1
print(result)
