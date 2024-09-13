n, m = map(int, input().split()) # garo, cero
k = int(input())                # store
'''
동글이 위치따라 경우 나누기
상점들에 대해
동글이랑 같은 줄이면 뺀다음 절대값
동글이 바로 옆줄이면 왼, 오 방향 나눠서 구하기
동글이 반대편이면 두가지 조건 나눠서 구하기
'''


stores = []
distance = 0
for _ in range(k):
    d, s = map(int, input().split())        # 방향, 거리
    stores.append((d, s))

# print(stores)

dongle_side, dongle_r = tuple(map(int, input().split()))   # 동글이
# print(dongle_side, dongle_r)

sum_result = 0
for store in stores:
    store_side, store_r = store[0], store[1]

    if dongle_side == store_side:
        result = abs(dongle_r - store_r)

    elif dongle_side == 1:              # 동글이 북쪽
        if store_side == 2:
            if store_r <= n - dongle_r:
                result = dongle_r + m + store_r
            else:
                result = (n-dongle_r) + m + (n-store_r)
        elif store_side == 3:
            result = store_r + dongle_r
        else:
            result =  store_r + (n - dongle_r)

    elif dongle_side == 2:              # 동글이 남쪽
        if store_side == 1:
            if store_r <= n - dongle_r:
                result = dongle_r + m + store_r
            else:
                result = (n-dongle_r) + m + (n-store_r)
        elif store_side == 3:  # 서쪽
            result = (m-store_r) + dongle_r
        else:               # 가게 동쪽
            result =  (m-store_r) + (n - dongle_r)

    elif dongle_side == 3:              # 동글이 서쪽
        if store_side == 4:
            if store_r <= m - dongle_r:
                result = dongle_r + n + store_r
            else:
                result = (m-dongle_r) + n+ (m-store_r)
        elif store_side == 1:
            result = store_r + dongle_r
        else:
            result = store_r + (m - dongle_r)

    else:
        if store_side == 3:  # 가게 남쪽
            if store_r <= m - dongle_r:
                result = dongle_r + n + store_r
            else:
                result = (m - dongle_r) + n + (m - store_r)
        elif store_side == 1:  # 서쪽
            result = (n-store_r) + dongle_r
        else:  # 가게 동쪽
            result = (n-store_r) + (m - dongle_r)

    sum_result += result

print(sum_result)