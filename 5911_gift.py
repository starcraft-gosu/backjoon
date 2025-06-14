'''
N명에게 B원으로 선물
근데 이놈이 반값쿠폰 하나 on
물건값만 반이고 배송비는 같음
몇놈한테 줄수잇나
1. 총합 순으로 나열
2. 냅다 더하기
3. 오버되면 딱 끊
4. 안에서 반갈죽하면 하나 더 되는지 조사
    총합 젤 작은애가 오버한 수치보다 물건값이 두배 이상인 애가 잇는지
5. 없으면
    1. 차례대로 다 반갈죽해서 더해보기
    2. 물건 비싼순으로 정렬후 반갈죽 - 딱히 무쓸모일듯
'''
# import sys
# sys.stdin = open('input.txt', 'r')
N, B = map(int, input().split())

friends = []
for _ in range(N):
    cost, fee = map(int, input().split())
    gift = tuple([cost+fee, cost, fee])     # # (총합, 가격, 배송비)
    friends.append(gift)
# print(friends)
friends.sort()
# print(friends)

total = 0 # 총 비용
idx = 0 # 친구 수
for friend in friends:              # 친구 선물비용 차곡차곡 더함
    total += friend[0]
    idx += 1  # 준 친구들 수 저장
    if total > B:
        over = total - B            # 가장 작게 오버된 경우의 차 저장
        break

else:                               # 친구 선물 총비용이 가진돈 이하면 N 출력
    print(N)

# 한놈 더 집어넣을수 있냐없냐

for i in range(idx):                    # 이미 더한 애들 중
    if friends[i][1] >= over*2:         # 마지막에 더한애의 초과 폭보다 할인하는게 더 큰 경우
        break
else:                                   # 이미 더한 애들 외의 놈들
    total - friends[idx][0]             # 아까 마지막에 더해서 값이 넘게 한 애를 총합에서 빼줌
    for j in range(idx, N-1):
        dc = friends[j][0] - friends[j][1] / 2  # 할인쿠폰 적용
        if total + dc <= B:
            break
    else:
        idx -= 1
print(idx)


