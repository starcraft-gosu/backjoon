length_1, length_2 = map(int, input().split())
socket_1 = sorted(list(map(int, input().split())), reverse=True)
socket_2 = sorted(list(map(int, input().split())))

# print(length_1, length_2)
# print(socket_1, socket_2)

cnt = 0
for i in range(len(socket_1)):
    # A콘센트를 1구 소모하여 1번 멀티탭을 꽂는경우
    if i != 0:
        cnt -= 1
    for j in range(socket_1[i]):
        if socket_2:
            cnt += socket_2.pop()   # 제일 큰 콘센트부터 더해줌 - 예외 방지
            # print(cnt)
        else:
            break
    if not socket_2:
        break
print(cnt)
