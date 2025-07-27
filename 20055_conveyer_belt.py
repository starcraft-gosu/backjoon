import sys
input = sys.stdin.readline

'''
벨트(로봇 여부, 내구도, 최초번호)
'''

N, K = map(int, input().split())
durability = list(map(int, input().split()))

print(durability)

belt = [[0, dur, i] for i, dur in enumerate(durability)] # 로봇, 내구도, 칸
print(belt)

def phase(n):
    inspect = 0
    # 한칸씩 이동
    for idx, place in enumerate(belt):
        # print(place)
        place[2] = (place[2] + 1) % (2*n)
        # 자리가 n-2이면
        if place[2] == n-2:
            inspect = idx
        if place[2] == n-1:
            place[0] = 0
            print("내림", belt)
    print("이동", belt)
    # 로봇 이동 조건 확인

    cnt = 0
    while cnt <= n-2: # 여기가 잘못됨 belt 인덱스가 아니라 자리로 해야지
        cur = inspect-cnt
        print(cur)
        # 자리가 n-2인 곳을 찾아서
        # n-1번만큼 로봇울 확인하고
        # 이번 칸에 로봇이 있고 내구도가 0이 아니고 다음칸에 로봇이 없으면
        next_can = (cur+1) % n
        if belt[cur][0] and belt[next_can][1] and not belt[next_can][0]:
            # 다음 자리 로봇 채우고
            belt[next_can][0] = 1
            # 다음 자리 내구도 하락시키고
            belt[next_can][1] -= 1
            # 이번 자리 로봇 빼고
            belt[cur][0] = 0
        cnt += 1
        print("로봇이동", belt)
    belt[inspect][0] = 0
    # 올리는 조건 확인
    for place in belt:
        # 0번째 칸이고 내구도가 1이상이고 로봇이 없으면
        if place[2] == 0 and place[1] and place[0] ==0:
            place[0] = 1
            place[1] -=1
    print("올림", belt)
    # 로봇 내리기 이것도 자리를 기준

ans = 0
while True:
    ans += 1
    phase(N)
    cnt = 0

    for place in belt:
        if place[1] == 0:
            cnt+=1
    if cnt >= K:
        break
    print(ans, belt)
    print()
print(ans)

##    종료조건
##    내구도 0인 K가 N개 잇는지

